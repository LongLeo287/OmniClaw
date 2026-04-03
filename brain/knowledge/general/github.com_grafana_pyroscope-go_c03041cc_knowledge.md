---
id: github.com-grafana-pyroscope-go-c03041cc-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:04.420859
---

# KNOWLEDGE EXTRACT: github.com_grafana_pyroscope-go_c03041cc
> **Extracted on:** 2026-04-01 13:30:06
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522498/github.com_grafana_pyroscope-go_c03041cc

---

## File: `.gitignore`
```
.idea/
.vscode/
.tools/

main
timing
```

## File: `.golangci.yml`
```yaml
version: "2"

formatters:
  enable:
    - gofmt
    - goimports
  settings:
    gofmt:
      simplify: true
    goimports:
      local-prefixes:
        - github.com/grafana/pyroscope-go


run:
  timeout: 10m
  tests: true

linters:
  default: all
  disable:
    - wsl
    - wsl_v5
    - cyclop
    - depguard
    - funcorder
    - funlen
    - mnd
    - varnamelen
    - wrapcheck
    - exhaustruct
    - paralleltest
    - godot
    - godox
    - testpackage
    - canonicalheader
    - tagliatelle
    - noinlineerr
    - ireturn
    - gochecknoinits
    - nonamedreturns
    - gomoddirectives # TODO can this be re-enabled?

  settings:
    revive:
      rules:
        - name: exported
          disabled: true # TODO this is nice to enable for an SDK

```

## File: `CODEOWNERS`
```
* @grafana/pyroscope-go @grafana/pyroscope-team
```

## File: `LICENSE`
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

   Copyright 2020 Pyroscope

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

## File: `Makefile`
```
TEST_PACKAGES := ./... ./godeltaprof/compat/... ./godeltaprof/...
GO ?= go

GOLANGCI_LINT_VERSION ?= v2.2.2
TOOLS_DIR := $(CURDIR)/.tools
GOLANGCI_LINT := $(TOOLS_DIR)/golangci-lint

.PHONY: test
test:
	$(GO) test -race $(shell $(GO) list $(TEST_PACKAGES) | grep -v /example)

.PHONY: go/mod
go/mod:
	GO111MODULE=on go mod download
	go work sync
	GO111MODULE=on go mod tidy
	cd godeltaprof/compat/ && GO111MODULE=on go mod download
	cd godeltaprof/compat/ && GO111MODULE=on go mod tidy
	cd godeltaprof/ && GO111MODULE=on go mod download
	cd godeltaprof/ && GO111MODULE=on go mod tidy

.PHONY: install-lint
install-lint:
	@ mkdir -p $(TOOLS_DIR)
	@ GOBIN=$(TOOLS_DIR) $(GO) install github.com/golangci/golangci-lint/v2/cmd/golangci-lint@$(GOLANGCI_LINT_VERSION)

.PHONY: lint
lint: install-lint
	$(GOLANGCI_LINT) run
	cd godeltaprof && $(GOLANGCI_LINT) run
	cd godeltaprof/compat && $(GOLANGCI_LINT) run

.PHONY: examples
examples:
	 go build example/http/main.go
	 go build example/simple/main.go
	 go build example/timing/timing.go
```

## File: `README.md`
```markdown
# Pyroscope Golang Client

This is a golang integration for Pyroscope — open source continuous profiling platform.

For more information, please visit our [golang integration documentation](https://grafana.com/docs/pyroscope/latest/configure-client/language-sdks/go_push/).

## Profiling Go applications

To start profiling a Go application, you need to include our Go module in your app:

```
go get github.com/grafana/pyroscope-go
```

Then add the following code to your application:

```go
package main

import "github.com/grafana/pyroscope-go"

func main() {
  pyroscope.Start(pyroscope.Config{
    ApplicationName: "simple.golang.app",

    // replace this with the address of pyroscope server
    ServerAddress:   "http://pyroscope-server:4040",

    // you can disable logging by setting this to nil
    Logger:          pyroscope.StandardLogger,

    // Optional HTTP Basic authentication (Grafana Cloud)
    BasicAuthUser:     "<User>",
    BasicAuthPassword: "<Password>",
    // Optional Pyroscope tenant ID (only needed if using multi-tenancy). Not needed for Grafana Cloud.
    // TenantID:          "<TenantID>",

    // by default all profilers are enabled,
    // but you can select the ones you want to use:
    ProfileTypes: []pyroscope.ProfileType{
      pyroscope.ProfileCPU,
      pyroscope.ProfileAllocObjects,
      pyroscope.ProfileAllocSpace,
      pyroscope.ProfileInuseObjects,
      pyroscope.ProfileInuseSpace,
    },
  })

  // your code goes here
}
```

### Tags

It is possible to add tags (labels) to the profiling data. These tags can be used to filter the data in the UI.

```go
// these two ways of adding tags are equivalent:
pyroscope.TagWrapper(context.Background(), pyroscope.Labels("controller", "slow_controller"), func(c context.Context) {
  slowCode()
})

pprof.Do(context.Background(), pprof.Labels("controller", "slow_controller"), func(c context.Context) {
  slowCode()
})
```

### Pull Mode

Go integration supports pull mode, which means that you can profile applications without adding any extra code. For that to work you will need to make sure you have profiling routes (`/debug/pprof`) enabled in your http server. Generally, that means that you need to add `net/http/pprof` package:

```go
import _ "net/http/pprof"
```

## Examples

Check out the [examples](https://github.com/grafana/pyroscope-go/tree/main/example) directory in our repository to learn more. 🔥

## Maintainers

This package is maintained by [@grafana/pyroscope-go](https://github.com/orgs/grafana/teams/pyroscope-go). Mention this team on issues or PRs for feedback.
```

## File: `api.go`
```go
package pyroscope

import (
	"context"
	"fmt"
	"os"
	"runtime/pprof"
	"time"

	"github.com/grafana/pyroscope-go/upstream/remote"
)

type Config struct {
	ApplicationName   string // e.g backend.purchases
	Tags              map[string]string
	ServerAddress     string // e.g http://pyroscope.services.internal:4040
	BasicAuthUser     string // http basic auth user
	BasicAuthPassword string // http basic auth password
	TenantID          string // specify TenantId when using phlare multi-tenancy
	UploadRate        time.Duration
	Logger            Logger
	ProfileTypes      []ProfileType
	DisableGCRuns     bool // this will disable automatic runtime.GC runs between getting the heap profiles
	HTTPHeaders       map[string]string
	HTTPClient        remote.HTTPClient

	// Deprecated: the field will be removed in future releases.
	// Use BasicAuthUser and BasicAuthPassword instead.
	AuthToken string // specify this token when using pyroscope cloud
	// Deprecated: the field will be removed in future releases.
	// Use UploadRate instead.
	DisableAutomaticResets bool
	// Deprecated: the field will be removed in future releases.
	// DisableCumulativeMerge is ignored.
	DisableCumulativeMerge bool
	// Deprecated: the field will be removed in future releases.
	// SampleRate is set to 100 and is not configurable.
	SampleRate uint32
}

type Profiler struct {
	session  *Session
	uploader *remote.Remote
}

// Start starts continuously profiling go code
func Start(cfg Config) (*Profiler, error) {
	if len(cfg.ProfileTypes) == 0 {
		cfg.ProfileTypes = DefaultProfileTypes
	}
	if cfg.Logger == nil {
		cfg.Logger = noopLogger
	}

	// Override the address to use when the environment variable is defined.
	// This is useful to support adhoc push ingestion.
	if address, ok := os.LookupEnv("PYROSCOPE_ADHOC_SERVER_ADDRESS"); ok {
		cfg.ServerAddress = address
	}

	rc := remote.Config{
		AuthToken:         cfg.AuthToken,
		TenantID:          cfg.TenantID,
		BasicAuthUser:     cfg.BasicAuthUser,
		BasicAuthPassword: cfg.BasicAuthPassword,
		HTTPHeaders:       cfg.HTTPHeaders,
		HTTPClient:        cfg.HTTPClient,
		Address:           cfg.ServerAddress,
		Threads:           5, // per each profile type upload
		Timeout:           30 * time.Second,
		Logger:            cfg.Logger,
	}
	uploader, err := remote.NewRemote(rc)
	if err != nil {
		return nil, err
	}

	sc := SessionConfig{
		Upstream:               uploader,
		Logger:                 cfg.Logger,
		AppName:                cfg.ApplicationName,
		Tags:                   cfg.Tags,
		ProfilingTypes:         cfg.ProfileTypes,
		DisableGCRuns:          cfg.DisableGCRuns,
		DisableAutomaticResets: cfg.DisableAutomaticResets,
		UploadRate:             cfg.UploadRate,
	}

	s, err := NewSession(sc)
	if err != nil {
		return nil, fmt.Errorf("new session: %w", err)
	}
	uploader.Start()
	if err = s.Start(); err != nil {
		return nil, fmt.Errorf("start session: %w", err)
	}

	return &Profiler{session: s, uploader: uploader}, nil
}

// Stop stops continuous profiling session and uploads the remaining profiling data
func (p *Profiler) Stop() error {
	p.session.Stop()
	p.uploader.Stop()

	return nil
}

// Flush resets current profiling session. if wait is true, also waits for all profiles to be uploaded synchronously
func (p *Profiler) Flush(wait bool) {
	p.session.flush(wait)
}

type LabelSet = pprof.LabelSet

var Labels = pprof.Labels //nolint:gochecknoglobals

func TagWrapper(ctx context.Context, labels LabelSet, cb func(context.Context)) {
	pprof.Do(ctx, labels, func(c context.Context) { cb(c) })
}
```

## File: `api_test.go`
```go
package pyroscope

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestProfilerStartStop(t *testing.T) {
	profiler, err := Start(Config{
		ApplicationName: "test",
	})
	require.NoError(t, err)
	err = profiler.Stop()
	require.NoError(t, err)
}
```

## File: `collector.go`
```go
package pyroscope

import (
	"bytes"
	"errors"
	"io"
	"time"

	internal "github.com/grafana/pyroscope-go/internal/pprof"
	"github.com/grafana/pyroscope-go/upstream"
)

type cpuProfileCollector struct {
	name string
	dur  time.Duration

	upstream  upstream.Upstream
	collector internal.Collector
	logger    Logger

	buf         *bytes.Buffer
	timeStarted time.Time

	// started indicates whether the collector
	// is interrupted with StartCPUProfile.
	started bool
	events  chan event

	halt chan struct{}
	done chan struct{}
}

type event struct {
	typ  eventType
	done chan error
	w    io.Writer
}

type eventType int

const (
	startEvent eventType = iota
	stopEvent
	flushEvent
)

func newEvent(typ eventType) event {
	return event{typ: typ, done: make(chan error, 1)}
}

func (e event) send(c chan<- event) error {
	c <- e

	return <-e.done
}

func newStartEvent(w io.Writer) event {
	e := newEvent(startEvent)
	e.w = w

	return e
}

func newCPUProfileCollector(
	name string,
	upstream upstream.Upstream,
	logger Logger,
	period time.Duration,
) *cpuProfileCollector {
	buf := bytes.NewBuffer(make([]byte, 0, 1<<10))

	return &cpuProfileCollector{
		name:      name,
		dur:       period,
		upstream:  upstream,
		logger:    logger,
		collector: internal.DefaultCollector(),
		buf:       buf,
		events:    make(chan event),
		halt:      make(chan struct{}),
		done:      make(chan struct{}),
	}
}

func (c *cpuProfileCollector) Start() {
	c.logger.Debugf("starting cpu profile collector")
	// From now on, internal pprof.StartCPUProfile
	// is handled by this collector.
	internal.SetCollector(c)
	t := time.NewTicker(c.dur)

	// Force pprof.StartCPUProfile: if CPU profiling is already
	// in progress (pprof.StartCPUProfile called outside the
	// package), profiling will start once it finishes.
	_ = c.reset(nil)
	for {
		select {
		case n := <-t.C:
			// Skip and adjust the timer, if the actual
			// profile duration is less than the desired,
			// which may happen if the collector has been
			// interrupted and then resumed, or flushed.
			if d := n.Sub(c.timeStarted); d < c.dur {
				if d < 0 {
					// Ticker fired after the StartCPUProfile
					// call, that interrupted background
					// profiling.
					d = c.dur
				}
				t.Reset(d)

				continue
			}
			t.Reset(c.dur)
			if !c.started {
				// Collector can't start collecting profiles
				// in background while profiling started with
				// StartCPUProfile (foreground).
				_ = c.reset(nil)
			}

		case <-c.halt:
			t.Stop()
			if c.started {
				// Collector can't be stopped in-between
				// StartCPUProfile and StopCPUProfile calls.
				continue
			}
			c.collector.StopCPUProfile()
			c.upload()
			close(c.done)

			return

		case e := <-c.events:
			c.handleEvent(e)
		}
	}
}

func (c *cpuProfileCollector) handleEvent(e event) {
	var err error
	defer func() {
		e.done <- err
		close(e.done)
	}()

	switch e.typ {
	case startEvent:
		if c.started { // Misuse.
			// Just to avoid interruption of the background
			// profiling that will fail immediately.
			err = errAlreadyStarted
		} else {
			err = c.reset(e.w)
			c.started = err == nil
		}

	case stopEvent:
		if c.started {
			err = c.reset(nil)
			c.started = false
		}

	case flushEvent:
		if c.started {
			// Flush can't be done if StartCPUProfile is called,
			// as we'd need stopping the foreground collector first.
			err = errFlushRejected
		} else {
			err = c.reset(nil)
		}
	}
}

func (c *cpuProfileCollector) Stop() {
	c.logger.Debugf("stopping cpu profile collector")
	// Switches back to the standard pprof collector.
	// If internal pprof.StartCPUProfile is called,
	// the function blocks until StopCPUProfile.
	internal.SetCollector(c.collector)
	// Note that "halt" is not an event, but rather state
	// of the collector: the channel can be read multiple
	// times before the collector stops.
	close(c.halt)
	<-c.done
	c.logger.Debugf("stopping cpu profile collector stopped")
}

func (c *cpuProfileCollector) StartCPUProfile(w io.Writer) error {
	c.logger.Debugf("cpu profile collector interrupted with StartCPUProfile")

	return newStartEvent(w).send(c.events)
}

func (c *cpuProfileCollector) StopCPUProfile() {
	c.logger.Debugf("cpu profile collector restored")
	_ = newEvent(stopEvent).send(c.events)
}

func (c *cpuProfileCollector) Flush() error {
	return newEvent(flushEvent).send(c.events)
}

func (c *cpuProfileCollector) reset(w io.Writer) error {
	c.collector.StopCPUProfile()
	c.upload()
	var d io.Writer = c.buf
	if w != nil {
		// pprof.StopCPUProfile dumps gzipped
		// profile ignoring any writer failure.
		d = io.MultiWriter(d, w)
	}
	c.timeStarted = time.Now()

	if err := c.collector.StartCPUProfile(d); err != nil {
		c.logger.Errorf("failed to start CPU profiling: %v", err)
		c.timeStarted = time.Time{}
		c.buf.Reset()

		return err
	}

	return nil
}

func (c *cpuProfileCollector) upload() {
	if c.timeStarted.IsZero() {
		return
	}
	buf := c.buf.Bytes()
	if len(buf) == 0 {
		return
	}
	c.upstream.Upload(&upstream.UploadJob{
		Name:            c.name,
		StartTime:       c.timeStarted,
		EndTime:         time.Now(),
		SpyName:         "gospy",
		SampleRate:      DefaultSampleRate,
		Units:           "samples",
		AggregationType: "sum",
		Format:          upstream.FormatPprof,
		Profile:         copyBuf(buf),
	})
	c.buf.Reset()
}

var (
	errAlreadyStarted = errors.New("cpu profiling already started")
	errFlushRejected  = errors.New("flush rejected: cpu profiling is in progress")
)
```

## File: `collector_test.go`
```go
package pyroscope

import (
	"io"
	"reflect"
	"sync"
	"testing"
	"time"

	"github.com/grafana/pyroscope-go/internal/testutil"
	"github.com/grafana/pyroscope-go/upstream"
)

func Test_StartCPUProfile_interrupts_background_profiling(t *testing.T) {
	logger := testutil.NewTestLogger()
	collector := new(mockCollector)
	c := newCPUProfileCollector(
		"test",
		new(mockUpstream),
		logger,
		100*time.Millisecond,
	)
	c.collector = collector

	go c.Start()
	<-collector.waitStartCPUProfile()

	// Background profile is being collected.
	// Try to interrupt it with StartCPUProfile.
	start := collector.waitStartCPUProfile()
	stop := collector.waitStopCPUProfile()

	if err := c.StartCPUProfile(io.Discard); err != nil {
		t.Fatal("failed to start CPU profiling")
	}
	<-stop
	<-start

	// Foreground profile is being collected.
	// Resume background profiling with StopCPUProfile.
	start = collector.waitStartCPUProfile()
	stop = collector.waitStopCPUProfile()
	c.StopCPUProfile()
	<-stop
	<-start

	c.Stop()

	if !reflect.DeepEqual(logger.Lines(), []string{
		"starting cpu profile collector",
		"cpu profile collector interrupted with StartCPUProfile",
		"cpu profile collector restored",
		"stopping cpu profile collector",
		"stopping cpu profile collector stopped",
	}) {
		for _, line := range logger.Lines() {
			t.Log(line)
		}
		t.Fatal("^ unexpected even sequence")
	}
}

func Test_StartCPUProfile_blocks_Stop(t *testing.T) {
	logger := testutil.NewTestLogger()
	collector := new(mockCollector)
	c := newCPUProfileCollector(
		"test",
		new(mockUpstream),
		logger,
		100*time.Millisecond,
	)
	c.collector = collector

	go c.Start()
	<-collector.waitStartCPUProfile()

	// Background profile is being collected.
	// Try to interrupt it with StartCPUProfile.
	start := collector.waitStartCPUProfile()
	stop := collector.waitStopCPUProfile()

	if err := c.StartCPUProfile(io.Discard); err != nil {
		t.Fatal("failed to start CPU profiling")
	}
	<-stop
	<-start

	go c.StopCPUProfile()
	c.Stop()

	if !reflect.DeepEqual(logger.Lines(), []string{
		"starting cpu profile collector",
		"cpu profile collector interrupted with StartCPUProfile",
		"stopping cpu profile collector",
		"cpu profile collector restored",
		"stopping cpu profile collector stopped",
	}) {
		for _, line := range logger.Lines() {
			t.Log(line)
		}
		t.Fatal("^ unexpected even sequence")
	}
}

type mockCollector struct {
	sync.Mutex

	start chan struct{}
	stop  chan struct{}
}

func (m *mockCollector) waitStartCPUProfile() <-chan struct{} {
	m.Lock()
	c := make(chan struct{})
	m.start = c
	m.Unlock()

	return c
}

func (m *mockCollector) waitStopCPUProfile() <-chan struct{} {
	m.Lock()
	c := make(chan struct{})
	m.stop = c
	m.Unlock()

	return c
}

func (m *mockCollector) StartCPUProfile(_ io.Writer) error {
	m.Lock()
	if m.start != nil {
		close(m.start)
		m.start = nil
	}
	m.Unlock()

	return nil
}

func (m *mockCollector) StopCPUProfile() {
	m.Lock()
	if m.stop != nil {
		close(m.stop)
		m.stop = nil
	}
	m.Unlock()
}

type mockUpstream struct{ uploaded []*upstream.UploadJob }

func (m *mockUpstream) Upload(j *upstream.UploadJob) { m.uploaded = append(m.uploaded, j) }

func (*mockUpstream) Flush() {}
```

## File: `go.mod`
```
module github.com/grafana/pyroscope-go

go 1.18

// todo can we remove this replace?
replace github.com/grafana/pyroscope-go/godeltaprof => ./godeltaprof

require (
	github.com/grafana/pyroscope-go/godeltaprof v0.1.9
	github.com/stretchr/testify v1.11.1
)

require (
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/klauspost/compress v1.17.8 // indirect
	github.com/kr/pretty v0.3.1 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	github.com/stretchr/objx v0.5.2 // indirect
	gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
```

## File: `go.sum`
```
github.com/creack/pty v1.1.9/go.mod h1:oKZEueFk5CKHvIhNR5MUki03XCEU+Q6VDXinZuGJ33E=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/klauspost/compress v1.17.8 h1:YcnTYrq7MikUT7k0Yb5eceMmALQPYBW/Xltxn0NAMnU=
github.com/klauspost/compress v1.17.8/go.mod h1:Di0epgTjJY877eYKx5yC51cX2A2Vl2ibi7bDH9ttBbw=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/pkg/diff v0.0.0-20210226163009-20ebb0f2a09e/go.mod h1:pJLUxLENpZxwdsKMEsNbx1VGcRFpLqf3715MtcvvzbA=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rogpeppe/go-internal v1.9.0 h1:73kH8U+JUqXU8lRuOHeVHaa/SZPifC7BkcraZVejAe8=
github.com/rogpeppe/go-internal v1.9.0/go.mod h1:WtVeX8xhTBvf0smdhujwtBcq4Qrzq/fJaraNFVN+nFs=
github.com/stretchr/objx v0.5.2 h1:xuMeJ0Sdp5ZMRXx/aWO6RZxdr3beISkG5/G/aIRr3pY=
github.com/stretchr/objx v0.5.2/go.mod h1:FRsXN1f5AsAjCGJKqEizvkpNtU+EGNCLh3NxZ/8L+MA=
github.com/stretchr/testify v1.11.1 h1:7s2iGBzp5EwR7/aIZr8ao5+dra3wiQyKjjFuvgVKu7U=
github.com/stretchr/testify v1.11.1/go.mod h1:wZwfW3scLgRK+23gO65QZefKpKQRnfz6sD981Nm4B6U=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `go.work`
```
go 1.18

use (
	.
	godeltaprof
	godeltaprof/compat
)
```

## File: `go.work.sum`
```
cel.dev/expr v0.16.0 h1:yloc84fytn4zmJX2GU3TkXGsaieaV7dQ057Qs4sIG2Y=
cel.dev/expr v0.16.0/go.mod h1:TRSuuV7DlVCE/uwv5QbAiW/v8l5O8C4eEPHeu7gf7Sg=
cloud.google.com/go v0.105.0 h1:DNtEKRBAAzeS4KyIory52wWHuClNaXJ5x1F7xa4q+5Y=
cloud.google.com/go v0.105.0/go.mod h1:PrLgOJNe5nfE9UMxKxgXj4mD3voiP+YQ6gdt6KMFOKM=
cloud.google.com/go/accessapproval v1.5.0 h1:/nTivgnV/n1CaAeo+ekGexTYUsKEU9jUVkoY5359+3Q=
cloud.google.com/go/accessapproval v1.5.0/go.mod h1:HFy3tuiGvMdcd/u+Cu5b9NkO1pEICJ46IR82PoUdplw=
cloud.google.com/go/accesscontextmanager v1.4.0 h1:CFhNhU7pcD11cuDkQdrE6PQJgv0EXNKNv06jIzbLlCU=
cloud.google.com/go/accesscontextmanager v1.4.0/go.mod h1:/Kjh7BBu/Gh83sv+K60vN9QE5NJcd80sU33vIe2IFPE=
cloud.google.com/go/aiplatform v1.27.0 h1:DBi3Jk9XjCJ4pkkLM4NqKgj3ozUL1wq4l+d3/jTGXAI=
cloud.google.com/go/aiplatform v1.27.0/go.mod h1:Bvxqtl40l0WImSb04d0hXFU7gDOiq9jQmorivIiWcKg=
cloud.google.com/go/analytics v0.12.0 h1:NKw6PpQi6V1O+KsjuTd+bhip9d0REYu4NevC45vtGp8=
cloud.google.com/go/analytics v0.12.0/go.mod h1:gkfj9h6XRf9+TS4bmuhPEShsh3hH8PAZzm/41OOhQd4=
cloud.google.com/go/apigateway v1.4.0 h1:IIoXKR7FKrEAQhMTz5hK2wiDz2WNFHS7eVr/L1lE/rM=
cloud.google.com/go/apigateway v1.4.0/go.mod h1:pHVY9MKGaH9PQ3pJ4YLzoj6U5FUDeDFBllIz7WmzJoc=
cloud.google.com/go/apigeeconnect v1.4.0 h1:AONoTYJviyv1vS4IkvWzq69gEVdvHx35wKXc+e6wjZQ=
cloud.google.com/go/apigeeconnect v1.4.0/go.mod h1:kV4NwOKqjvt2JYR0AoIWo2QGfoRtn/pkS3QlHp0Ni04=
cloud.google.com/go/appengine v1.5.0 h1:lmG+O5oaR9xNwaRBwE2XoMhwQHsHql5IoiGr1ptdDwU=
cloud.google.com/go/appengine v1.5.0/go.mod h1:TfasSozdkFI0zeoxW3PTBLiNqRmzraodCWatWI9Dmak=
cloud.google.com/go/area120 v0.6.0 h1:TCMhwWEWhCn8d44/Zs7UCICTWje9j3HuV6nVGMjdpYw=
cloud.google.com/go/area120 v0.6.0/go.mod h1:39yFJqWVgm0UZqWTOdqkLhjoC7uFfgXRC8g/ZegeAh0=
cloud.google.com/go/artifactregistry v1.9.0 h1:3d0LRAU1K6vfqCahhl9fx2oGHcq+s5gftdix4v8Ibrc=
cloud.google.com/go/artifactregistry v1.9.0/go.mod h1:2K2RqvA2CYvAeARHRkLDhMDJ3OXy26h3XW+3/Jh2uYc=
cloud.google.com/go/asset v1.10.0 h1:aCrlaLGJWTODJX4G56ZYzJefITKEWNfbjjtHSzWpxW0=
cloud.google.com/go/asset v1.10.0/go.mod h1:pLz7uokL80qKhzKr4xXGvBQXnzHn5evJAEAtZiIb0wY=
cloud.google.com/go/assuredworkloads v1.9.0 h1:hhIdCOowsT1GG5eMCIA0OwK6USRuYTou/1ZeNxCSRtA=
cloud.google.com/go/assuredworkloads v1.9.0/go.mod h1:kFuI1P78bplYtT77Tb1hi0FMxM0vVpRC7VVoJC3ZoT0=
cloud.google.com/go/automl v1.8.0 h1:BMioyXSbg7d7xLibn47cs0elW6RT780IUWr42W8rp2Q=
cloud.google.com/go/automl v1.8.0/go.mod h1:xWx7G/aPEe/NP+qzYXktoBSDfjO+vnKMGgsApGJJquM=
cloud.google.com/go/baremetalsolution v0.4.0 h1:g9KO6SkakcYPcc/XjAzeuUrEOXlYPnMpuiaywYaGrmQ=
cloud.google.com/go/baremetalsolution v0.4.0/go.mod h1:BymplhAadOO/eBa7KewQ0Ppg4A4Wplbn+PsFKRLo0uI=
cloud.google.com/go/batch v0.4.0 h1:1jvEBY55OH4Sd2FxEXQfxGExFWov1A/IaRe+Z5Z71Fw=
cloud.google.com/go/batch v0.4.0/go.mod h1:WZkHnP43R/QCGQsZ+0JyG4i79ranE2u8xvjq/9+STPE=
cloud.google.com/go/beyondcorp v0.3.0 h1:w+4kThysgl0JiKshi2MKDCg2NZgOyqOI0wq2eBZyrzA=
cloud.google.com/go/beyondcorp v0.3.0/go.mod h1:E5U5lcrcXMsCuoDNyGrpyTm/hn7ne941Jz2vmksAxW8=
cloud.google.com/go/bigquery v1.44.0 h1:Wi4dITi+cf9VYp4VH2T9O41w0kCW0uQTELq2Z6tukN0=
cloud.google.com/go/bigquery v1.44.0/go.mod h1:0Y33VqXTEsbamHJvJHdFmtqHvMIY28aK1+dFsvaChGc=
cloud.google.com/go/billing v1.7.0 h1:Xkii76HWELHwBtkQVZvqmSo9GTr0O+tIbRNnMcGdlg4=
cloud.google.com/go/billing v1.7.0/go.mod h1:q457N3Hbj9lYwwRbnlD7vUpyjq6u5U1RAOArInEiD5Y=
cloud.google.com/go/binaryauthorization v1.4.0 h1:pL70vXWn9TitQYXBWTK2abHl2JHLwkFRjYw6VflRqEA=
cloud.google.com/go/binaryauthorization v1.4.0/go.mod h1:tsSPQrBd77VLplV70GUhBf/Zm3FsKmgSqgm4UmiDItk=
cloud.google.com/go/certificatemanager v1.4.0 h1:tzbR4UHBbgsewMWUD93JHi8EBi/gHBoSAcY1/sThFGk=
cloud.google.com/go/certificatemanager v1.4.0/go.mod h1:vowpercVFyqs8ABSmrdV+GiFf2H/ch3KyudYQEMM590=
cloud.google.com/go/channel v1.9.0 h1:pNuUlZx0Jb0Ts9P312bmNMuH5IiFWIR4RUtLb70Ke5s=
cloud.google.com/go/channel v1.9.0/go.mod h1:jcu05W0my9Vx4mt3/rEHpfxc9eKi9XwsdDL8yBMbKUk=
cloud.google.com/go/cloudbuild v1.4.0 h1:TAAmCmAlOJ4uNBu6zwAjwhyl/7fLHHxIEazVhr3QBbQ=
cloud.google.com/go/cloudbuild v1.4.0/go.mod h1:5Qwa40LHiOXmz3386FrjrYM93rM/hdRr7b53sySrTqA=
cloud.google.com/go/clouddms v1.4.0 h1:UhzHIlgFfMr6luVYVNydw/pl9/U5kgtjCMJHnSvoVws=
cloud.google.com/go/clouddms v1.4.0/go.mod h1:Eh7sUGCC+aKry14O1NRljhjyrr0NFC0G2cjwX0cByRk=
cloud.google.com/go/cloudtasks v1.8.0 h1:faUiUgXjW8yVZ7XMnKHKm1WE4OldPBUWWfIRN/3z1dc=
cloud.google.com/go/cloudtasks v1.8.0/go.mod h1:gQXUIwCSOI4yPVK7DgTVFiiP0ZW/eQkydWzwVMdHxrI=
cloud.google.com/go/compute v1.15.1 h1:7UGq3QknM33pw5xATlpzeoomNxsacIVvTqTTvbfajmE=
cloud.google.com/go/compute v1.15.1/go.mod h1:bjjoF/NtFUrkD/urWfdHaKuOPDR5nWIs63rR+SXhcpA=
cloud.google.com/go/compute/metadata v0.2.3 h1:mg4jlk7mCAj6xXp9UJ4fjI9VUI5rubuGBW5aJ7UnBMY=
cloud.google.com/go/compute/metadata v0.2.3/go.mod h1:VAV5nSsACxMJvgaAuX6Pk2AawlZn8kiOGuCv6gTkwuA=
cloud.google.com/go/compute/metadata v0.5.0 h1:Zr0eK8JbFv6+Wi4ilXAR8FJ3wyNdpxHKJNPos6LTZOY=
cloud.google.com/go/compute/metadata v0.5.0/go.mod h1:aHnloV2TPI38yx4s9+wAZhHykWvVCfu7hQbF+9CWoiY=
cloud.google.com/go/contactcenterinsights v1.4.0 h1:tTQLI/ZvguUf9Hv+36BkG2+/PeC8Ol1q4pBW+tgCx0A=
cloud.google.com/go/contactcenterinsights v1.4.0/go.mod h1:L2YzkGbPsv+vMQMCADxJoT9YiTTnSEd6fEvCeHTYVck=
cloud.google.com/go/container v1.7.0 h1:nbEK/59GyDRKKlo1SqpohY1TK8LmJ2XNcvS9Gyom2A0=
cloud.google.com/go/container v1.7.0/go.mod h1:Dp5AHtmothHGX3DwwIHPgq45Y8KmNsgN3amoYfxVkLo=
cloud.google.com/go/containeranalysis v0.6.0 h1:2824iym832ljKdVpCBnpqm5K94YT/uHTVhNF+dRTXPI=
cloud.google.com/go/containeranalysis v0.6.0/go.mod h1:HEJoiEIu+lEXM+k7+qLCci0h33lX3ZqoYFdmPcoO7s4=
cloud.google.com/go/datacatalog v1.8.0 h1:6kZ4RIOW/uT7QWC5SfPfq/G8sYzr/v+UOmOAxy4Z1TE=
cloud.google.com/go/datacatalog v1.8.0/go.mod h1:KYuoVOv9BM8EYz/4eMFxrr4DUKhGIOXxZoKYF5wdISM=
cloud.google.com/go/dataflow v0.7.0 h1:CW3541Fm7KPTyZjJdnX6NtaGXYFn5XbFC5UcjgALKvU=
cloud.google.com/go/dataflow v0.7.0/go.mod h1:PX526vb4ijFMesO1o202EaUmouZKBpjHsTlCtB4parQ=
cloud.google.com/go/dataform v0.5.0 h1:vLwowLF2ZB5J5gqiZCzv076lDI/Rd7zYQQFu5XO1PSg=
cloud.google.com/go/dataform v0.5.0/go.mod h1:GFUYRe8IBa2hcomWplodVmUx/iTL0FrsauObOM3Ipr0=
cloud.google.com/go/datafusion v1.5.0 h1:j5m2hjWovTZDTQak4MJeXAR9yN7O+zMfULnjGw/OOLg=
cloud.google.com/go/datafusion v1.5.0/go.mod h1:Kz+l1FGHB0J+4XF2fud96WMmRiq/wj8N9u007vyXZ2w=
cloud.google.com/go/datalabeling v0.6.0 h1:dp8jOF21n/7jwgo/uuA0RN8hvLcKO4q6s/yvwevs2ZM=
cloud.google.com/go/datalabeling v0.6.0/go.mod h1:WqdISuk/+WIGeMkpw/1q7bK/tFEZxsrFJOJdY2bXvTQ=
cloud.google.com/go/dataplex v1.4.0 h1:cNxeA2DiWliQGi21kPRqnVeQ5xFhNoEjPRt1400Pm8Y=
cloud.google.com/go/dataplex v1.4.0/go.mod h1:X51GfLXEMVJ6UN47ESVqvlsRplbLhcsAt0kZCCKsU0A=
cloud.google.com/go/dataproc v1.8.0 h1:gVOqNmElfa6n/ccG/QDlfurMWwrK3ezvy2b2eDoCmS0=
cloud.google.com/go/dataproc v1.8.0/go.mod h1:5OW+zNAH0pMpw14JVrPONsxMQYMBqJuzORhIBfBn9uI=
cloud.google.com/go/dataqna v0.6.0 h1:gx9jr41ytcA3dXkbbd409euEaWtofCVXYBvJz3iYm18=
cloud.google.com/go/dataqna v0.6.0/go.mod h1:1lqNpM7rqNLVgWBJyk5NF6Uen2PHym0jtVJonplVsDA=
cloud.google.com/go/datastore v1.10.0 h1:4siQRf4zTiAVt/oeH4GureGkApgb2vtPQAtOmhpqQwE=
cloud.google.com/go/datastore v1.10.0/go.mod h1:PC5UzAmDEkAmkfaknstTYbNpgE49HAgW2J1gcgUfmdM=
cloud.google.com/go/datastream v1.5.0 h1:PgIgbhedBtYBU6POGXFMn2uSl9vpqubc3ewTNdcU8Mk=
cloud.google.com/go/datastream v1.5.0/go.mod h1:6TZMMNPwjUqZHBKPQ1wwXpb0d5VDVPl2/XoS5yi88q4=
cloud.google.com/go/deploy v1.5.0 h1:kI6dxt8Ml0is/x7YZjLveTvR7YPzXAUD/8wQZ2nH5zA=
cloud.google.com/go/deploy v1.5.0/go.mod h1:ffgdD0B89tToyW/U/D2eL0jN2+IEV/3EMuXHA0l4r+s=
cloud.google.com/go/dialogflow v1.19.0 h1:HYHVOkoxQ9bSfNIelSZYNAtUi4CeSrCnROyOsbOqPq8=
cloud.google.com/go/dialogflow v1.19.0/go.mod h1:JVmlG1TwykZDtxtTXujec4tQ+D8SBFMoosgy+6Gn0s0=
cloud.google.com/go/dlp v1.7.0 h1:9I4BYeJSVKoSKgjr70fLdRDumqcUeVmHV4fd5f9LR6Y=
cloud.google.com/go/dlp v1.7.0/go.mod h1:68ak9vCiMBjbasxeVD17hVPxDEck+ExiHavX8kiHG+Q=
cloud.google.com/go/documentai v1.10.0 h1:jfq09Fdjtnpnmt/MLyf6A3DM3ynb8B2na0K+vSXvpFM=
cloud.google.com/go/documentai v1.10.0/go.mod h1:vod47hKQIPeCfN2QS/jULIvQTugbmdc0ZvxxfQY1bg4=
cloud.google.com/go/domains v0.7.0 h1:pu3JIgC1rswIqi5romW0JgNO6CTUydLYX8zyjiAvO1c=
cloud.google.com/go/domains v0.7.0/go.mod h1:PtZeqS1xjnXuRPKE/88Iru/LdfoRyEHYA9nFQf4UKpg=
cloud.google.com/go/edgecontainer v0.2.0 h1:hd6J2n5dBBRuAqnNUEsKWrp6XNPKsaxwwIyzOPZTokk=
cloud.google.com/go/edgecontainer v0.2.0/go.mod h1:RTmLijy+lGpQ7BXuTDa4C4ssxyXT34NIuHIgKuP4s5w=
cloud.google.com/go/errorreporting v0.3.0 h1:kj1XEWMu8P0qlLhm3FwcaFsUvXChV/OraZwA70trRR0=
cloud.google.com/go/errorreporting v0.3.0/go.mod h1:xsP2yaAp+OAW4OIm60An2bbLpqIhKXdWR/tawvl7QzU=
cloud.google.com/go/essentialcontacts v1.4.0 h1:b6csrQXCHKQmfo9h3dG/pHyoEh+fQG1Yg78a53LAviY=
cloud.google.com/go/essentialcontacts v1.4.0/go.mod h1:8tRldvHYsmnBCHdFpvU+GL75oWiBKl80BiqlFh9tp+8=
cloud.google.com/go/eventarc v1.8.0 h1:AgCqrmMMIcel5WWKkzz5EkCUKC3Rl5LNMMYsS+LvsI0=
cloud.google.com/go/eventarc v1.8.0/go.mod h1:imbzxkyAU4ubfsaKYdQg04WS1NvncblHEup4kvF+4gw=
cloud.google.com/go/filestore v1.4.0 h1:yjKOpzvqtDmL5AXbKttLc8j0hL20kuC1qPdy5HPcxp0=
cloud.google.com/go/filestore v1.4.0/go.mod h1:PaG5oDfo9r224f8OYXURtAsY+Fbyq/bLYoINEK8XQAI=
cloud.google.com/go/firestore v1.9.0 h1:IBlRyxgGySXu5VuW0RgGFlTtLukSnNkpDiEOMkQkmpA=
cloud.google.com/go/firestore v1.9.0/go.mod h1:HMkjKHNTtRyZNiMzu7YAsLr9K3X2udY2AMwDaMEQiiE=
cloud.google.com/go/functions v1.9.0 h1:35tgv1fQOtvKqH/uxJMzX3w6usneJ0zXpsFr9KAVhNE=
cloud.google.com/go/functions v1.9.0/go.mod h1:Y+Dz8yGguzO3PpIjhLTbnqV1CWmgQ5UwtlpzoyquQ08=
cloud.google.com/go/gaming v1.8.0 h1:97OAEQtDazAJD7yh/kvQdSCQuTKdR0O+qWAJBZJ4xiA=
cloud.google.com/go/gaming v1.8.0/go.mod h1:xAqjS8b7jAVW0KFYeRUxngo9My3f33kFmua++Pi+ggM=
cloud.google.com/go/gkebackup v0.3.0 h1:4K+jiv4ocqt1niN8q5Imd8imRoXBHTrdnJVt/uFFxF4=
cloud.google.com/go/gkebackup v0.3.0/go.mod h1:n/E671i1aOQvUxT541aTkCwExO/bTer2HDlj4TsBRAo=
cloud.google.com/go/gkeconnect v0.6.0 h1:zAcvDa04tTnGdu6TEZewaLN2tdMtUOJJ7fEceULjguA=
cloud.google.com/go/gkeconnect v0.6.0/go.mod h1:Mln67KyU/sHJEBY8kFZ0xTeyPtzbq9StAVvEULYK16A=
cloud.google.com/go/gkehub v0.10.0 h1:JTcTaYQRGsVm+qkah7WzHb6e9sf1C0laYdRPn9aN+vg=
cloud.google.com/go/gkehub v0.10.0/go.mod h1:UIPwxI0DsrpsVoWpLB0stwKCP+WFVG9+y977wO+hBH0=
cloud.google.com/go/gkemulticloud v0.4.0 h1:8F1NhJj8ucNj7lK51UZMtAjSWTgP1zO18XF6vkfiPPU=
cloud.google.com/go/gkemulticloud v0.4.0/go.mod h1:E9gxVBnseLWCk24ch+P9+B2CoDFJZTyIgLKSalC7tuI=
cloud.google.com/go/gsuiteaddons v1.4.0 h1:TGT2oGmO5q3VH6SjcrlgPUWI0njhYv4kywLm6jag0to=
cloud.google.com/go/gsuiteaddons v1.4.0/go.mod h1:rZK5I8hht7u7HxFQcFei0+AtfS9uSushomRlg+3ua1o=
cloud.google.com/go/iam v0.8.0 h1:E2osAkZzxI/+8pZcxVLcDtAQx/u+hZXVryUaYQ5O0Kk=
cloud.google.com/go/iam v0.8.0/go.mod h1:lga0/y3iH6CX7sYqypWJ33hf7kkfXJag67naqGESjkE=
cloud.google.com/go/iap v1.5.0 h1:BGEXovwejOCt1zDk8hXq0bOhhRu9haXKWXXXp2B4wBM=
cloud.google.com/go/iap v1.5.0/go.mod h1:UH/CGgKd4KyohZL5Pt0jSKE4m3FR51qg6FKQ/z/Ix9A=
cloud.google.com/go/ids v1.2.0 h1:LncHK4HHucb5Du310X8XH9/ICtMwZ2PCfK0ScjWiJoY=
cloud.google.com/go/ids v1.2.0/go.mod h1:5WXvp4n25S0rA/mQWAg1YEEBBq6/s+7ml1RDCW1IrcY=
cloud.google.com/go/iot v1.4.0 h1:Y9+oZT9jD4GUZzORXTU45XsnQrhxmDT+TFbPil6pRVQ=
cloud.google.com/go/iot v1.4.0/go.mod h1:dIDxPOn0UvNDUMD8Ger7FIaTuvMkj+aGk94RPP0iV+g=
cloud.google.com/go/kms v1.6.0 h1:OWRZzrPmOZUzurjI2FBGtgY2mB1WaJkqhw6oIwSj0Yg=
cloud.google.com/go/kms v1.6.0/go.mod h1:Jjy850yySiasBUDi6KFUwUv2n1+o7QZFyuUJg6OgjA0=
cloud.google.com/go/language v1.8.0 h1:3Wa+IUMamL4JH3Zd3cDZUHpwyqplTACt6UZKRD2eCL4=
cloud.google.com/go/language v1.8.0/go.mod h1:qYPVHf7SPoNNiCL2Dr0FfEFNil1qi3pQEyygwpgVKB8=
cloud.google.com/go/lifesciences v0.6.0 h1:tIqhivE2LMVYkX0BLgG7xL64oNpDaFFI7teunglt1tI=
cloud.google.com/go/lifesciences v0.6.0/go.mod h1:ddj6tSX/7BOnhxCSd3ZcETvtNr8NZ6t/iPhY2Tyfu08=
cloud.google.com/go/logging v1.6.1 h1:ZBsZK+JG+oCDT+vaxwqF2egKNRjz8soXiS6Xv79benI=
cloud.google.com/go/logging v1.6.1/go.mod h1:5ZO0mHHbvm8gEmeEUHrmDlTDSu5imF6MUP9OfilNXBw=
cloud.google.com/go/longrunning v0.3.0 h1:NjljC+FYPV3uh5/OwWT6pVU+doBqMg2x/rZlE+CamDs=
cloud.google.com/go/longrunning v0.3.0/go.mod h1:qth9Y41RRSUE69rDcOn6DdK3HfQfsUI0YSmW3iIlLJc=
cloud.google.com/go/managedidentities v1.4.0 h1:3Kdajn6X25yWQFhFCErmKSYTSvkEd3chJROny//F1A0=
cloud.google.com/go/managedidentities v1.4.0/go.mod h1:NWSBYbEMgqmbZsLIyKvxrYbtqOsxY1ZrGM+9RgDqInM=
cloud.google.com/go/maps v0.1.0 h1:kLReRbclTgJefw2fcCbdLPLhPj0U6UUWN10ldG8sdOU=
cloud.google.com/go/maps v0.1.0/go.mod h1:BQM97WGyfw9FWEmQMpZ5T6cpovXXSd1cGmFma94eubI=
cloud.google.com/go/mediatranslation v0.6.0 h1:qAJzpxmEX+SeND10Y/4868L5wfZpo4Y3BIEnIieP4dk=
cloud.google.com/go/mediatranslation v0.6.0/go.mod h1:hHdBCTYNigsBxshbznuIMFNe5QXEowAuNmmC7h8pu5w=
cloud.google.com/go/memcache v1.7.0 h1:yLxUzJkZVSH2kPaHut7k+7sbIBFpvSh1LW9qjM2JDjA=
cloud.google.com/go/memcache v1.7.0/go.mod h1:ywMKfjWhNtkQTxrWxCkCFkoPjLHPW6A7WOTVI8xy3LY=
cloud.google.com/go/metastore v1.8.0 h1:3KcShzqWdqxrDEXIBWpYJpOOrgpDj+HlBi07Grot49Y=
cloud.google.com/go/metastore v1.8.0/go.mod h1:zHiMc4ZUpBiM7twCIFQmJ9JMEkDSyZS9U12uf7wHqSI=
cloud.google.com/go/monitoring v1.8.0 h1:c9riaGSPQ4dUKWB+M1Fl0N+iLxstMbCktdEwYSPGDvA=
cloud.google.com/go/monitoring v1.8.0/go.mod h1:E7PtoMJ1kQXWxPjB6mv2fhC5/15jInuulFdYYtlcvT4=
cloud.google.com/go/networkconnectivity v1.7.0 h1:BVdIKaI68bihnXGdCVL89Jsg9kq2kg+II30fjVqo62E=
cloud.google.com/go/networkconnectivity v1.7.0/go.mod h1:RMuSbkdbPwNMQjB5HBWD5MpTBnNm39iAVpC3TmsExt8=
cloud.google.com/go/networkmanagement v1.5.0 h1:mDHA3CDW00imTvC5RW6aMGsD1bH+FtKwZm/52BxaiMg=
cloud.google.com/go/networkmanagement v1.5.0/go.mod h1:ZnOeZ/evzUdUsnvRt792H0uYEnHQEMaz+REhhzJRcf4=
cloud.google.com/go/networksecurity v0.6.0 h1:qDEX/3sipg9dS5JYsAY+YvgTjPR63cozzAWop8oZS94=
cloud.google.com/go/networksecurity v0.6.0/go.mod h1:Q5fjhTr9WMI5mbpRYEbiexTzROf7ZbDzvzCrNl14nyU=
cloud.google.com/go/notebooks v1.5.0 h1:AC8RPjNvel3ExgXjO1YOAz+teg9+j+89TNxa7pIZfww=
cloud.google.com/go/notebooks v1.5.0/go.mod h1:q8mwhnP9aR8Hpfnrc5iN5IBhrXUy8S2vuYs+kBJ/gu0=
cloud.google.com/go/optimization v1.2.0 h1:7PxOq9VTT7TMib/6dMoWpMvWS2E4dJEvtYzjvBreaec=
cloud.google.com/go/optimization v1.2.0/go.mod h1:Lr7SOHdRDENsh+WXVmQhQTrzdu9ybg0NecjHidBq6xs=
cloud.google.com/go/orchestration v1.4.0 h1:39d6tqvNjd/wsSub1Bn4cEmrYcet5Ur6xpaN+SxOxtY=
cloud.google.com/go/orchestration v1.4.0/go.mod h1:6W5NLFWs2TlniBphAViZEVhrXRSMgUGDfW7vrWKvsBk=
cloud.google.com/go/orgpolicy v1.5.0 h1:erF5PHqDZb6FeFrUHiYj2JK2BMhsk8CyAg4V4amJ3rE=
cloud.google.com/go/orgpolicy v1.5.0/go.mod h1:hZEc5q3wzwXJaKrsx5+Ewg0u1LxJ51nNFlext7Tanwc=
cloud.google.com/go/osconfig v1.10.0 h1:NO0RouqCOM7M2S85Eal6urMSSipWwHU8evzwS+siqUI=
cloud.google.com/go/osconfig v1.10.0/go.mod h1:uMhCzqC5I8zfD9zDEAfvgVhDS8oIjySWh+l4WK6GnWw=
cloud.google.com/go/oslogin v1.7.0 h1:pKGDPfeZHDybtw48WsnVLjoIPMi9Kw62kUE5TXCLCN4=
cloud.google.com/go/oslogin v1.7.0/go.mod h1:e04SN0xO1UNJ1M5GP0vzVBFicIe4O53FOfcixIqTyXo=
cloud.google.com/go/phishingprotection v0.6.0 h1:OrwHLSRSZyaiOt3tnY33dsKSedxbMzsXvqB21okItNQ=
cloud.google.com/go/phishingprotection v0.6.0/go.mod h1:9Y3LBLgy0kDTcYET8ZH3bq/7qni15yVUoAxiFxnlSUA=
cloud.google.com/go/policytroubleshooter v1.4.0 h1:NQklJuOUoz1BPP+Epjw81COx7IISWslkZubz/1i0UN8=
cloud.google.com/go/policytroubleshooter v1.4.0/go.mod h1:DZT4BcRw3QoO8ota9xw/LKtPa8lKeCByYeKTIf/vxdE=
cloud.google.com/go/privatecatalog v0.6.0 h1:Vz86uiHCtNGm1DeC32HeG2VXmOq5JRYA3VRPf8ZEcSg=
cloud.google.com/go/privatecatalog v0.6.0/go.mod h1:i/fbkZR0hLN29eEWiiwue8Pb+GforiEIBnV9yrRUOKI=
cloud.google.com/go/pubsub v1.27.1 h1:q+J/Nfr6Qx4RQeu3rJcnN48SNC0qzlYzSeqkPq93VHs=
cloud.google.com/go/pubsub v1.27.1/go.mod h1:hQN39ymbV9geqBnfQq6Xf63yNhUAhv9CZhzp5O6qsW0=
cloud.google.com/go/pubsublite v1.5.0 h1:iqrD8vp3giTb7hI1q4TQQGj77cj8zzgmMPsTZtLnprM=
cloud.google.com/go/pubsublite v1.5.0/go.mod h1:xapqNQ1CuLfGi23Yda/9l4bBCKz/wC3KIJ5gKcxveZg=
cloud.google.com/go/recaptchaenterprise/v2 v2.5.0 h1:UqzFfb/WvhwXGDF1eQtdHLrmni+iByZXY4h3w9Kdyv8=
cloud.google.com/go/recaptchaenterprise/v2 v2.5.0/go.mod h1:O8LzcHXN3rz0j+LBC91jrwI3R+1ZSZEWrfL7XHgNo9U=
cloud.google.com/go/recommendationengine v0.6.0 h1:6w+WxPf2LmUEqX0YyvfCoYb8aBYOcbIV25Vg6R0FLGw=
cloud.google.com/go/recommendationengine v0.6.0/go.mod h1:08mq2umu9oIqc7tDy8sx+MNJdLG0fUi3vaSVbztHgJ4=
cloud.google.com/go/recommender v1.8.0 h1:9kMZQGeYfcOD/RtZfcNKGKtoex3DdoB4zRgYU/WaIwE=
cloud.google.com/go/recommender v1.8.0/go.mod h1:PkjXrTT05BFKwxaUxQmtIlrtj0kph108r02ZZQ5FE70=
cloud.google.com/go/redis v1.10.0 h1:/zTwwBKIAD2DEWTrXZp8WD9yD/gntReF/HkPssVYd0U=
cloud.google.com/go/redis v1.10.0/go.mod h1:ThJf3mMBQtW18JzGgh41/Wld6vnDDc/F/F35UolRZPM=
cloud.google.com/go/resourcemanager v1.4.0 h1:NDao6CHMwEZIaNsdWy+tuvHaavNeGP06o1tgrR0kLvU=
cloud.google.com/go/resourcemanager v1.4.0/go.mod h1:MwxuzkumyTX7/a3n37gmsT3py7LIXwrShilPh3P1tR0=
cloud.google.com/go/resourcesettings v1.4.0 h1:eTzOwB13WrfF0kuzG2ZXCfB3TLunSHBur4s+HFU6uSM=
cloud.google.com/go/resourcesettings v1.4.0/go.mod h1:ldiH9IJpcrlC3VSuCGvjR5of/ezRrOxFtpJoJo5SmXg=
cloud.google.com/go/retail v1.11.0 h1:N9fa//ecFUOEPsW/6mJHfcapPV0wBSwIUwpVZB7MQ3o=
cloud.google.com/go/retail v1.11.0/go.mod h1:MBLk1NaWPmh6iVFSz9MeKG/Psyd7TAgm6y/9L2B4x9Y=
cloud.google.com/go/run v0.3.0 h1:AWPuzU7Xtaj3Jf+QarDWIs6AJ5hM1VFQ+F6Q+VZ6OT4=
cloud.google.com/go/run v0.3.0/go.mod h1:TuyY1+taHxTjrD0ZFk2iAR+xyOXEA0ztb7U3UNA0zBo=
cloud.google.com/go/scheduler v1.7.0 h1:K/mxOewgHGeKuATUJNGylT75Mhtjmx1TOkKukATqMT8=
cloud.google.com/go/scheduler v1.7.0/go.mod h1:jyCiBqWW956uBjjPMMuX09n3x37mtyPJegEWKxRsn44=
cloud.google.com/go/secretmanager v1.9.0 h1:xE6uXljAC1kCR8iadt9+/blg1fvSbmenlsDN4fT9gqw=
cloud.google.com/go/secretmanager v1.9.0/go.mod h1:b71qH2l1yHmWQHt9LC80akm86mX8AL6X1MA01dW8ht4=
cloud.google.com/go/security v1.10.0 h1:KSKzzJMyUoMRQzcz7azIgqAUqxo7rmQ5rYvimMhikqg=
cloud.google.com/go/security v1.10.0/go.mod h1:QtOMZByJVlibUT2h9afNDWRZ1G96gVywH8T5GUSb9IA=
cloud.google.com/go/securitycenter v1.16.0 h1:QTVtk/Reqnx2bVIZtJKm1+mpfmwRwymmNvlaFez7fQY=
cloud.google.com/go/securitycenter v1.16.0/go.mod h1:Q9GMaLQFUD+5ZTabrbujNWLtSLZIZF7SAR0wWECrjdk=
cloud.google.com/go/servicecontrol v1.5.0 h1:ImIzbOu6y4jL6ob65I++QzvqgFaoAKgHOG+RU9/c4y8=
cloud.google.com/go/servicecontrol v1.5.0/go.mod h1:qM0CnXHhyqKVuiZnGKrIurvVImCs8gmqWsDoqe9sU1s=
cloud.google.com/go/servicedirectory v1.7.0 h1:f7M8IMcVzO3T425AqlZbP3yLzeipsBHtRza8vVFYMhQ=
cloud.google.com/go/servicedirectory v1.7.0/go.mod h1:5p/U5oyvgYGYejufvxhgwjL8UVXjkuw7q5XcG10wx1U=
cloud.google.com/go/servicemanagement v1.5.0 h1:TpkCO5M7dhKSy1bKUD9o/sSEW/U1Gtx7opA1fsiMx0c=
cloud.google.com/go/servicemanagement v1.5.0/go.mod h1:XGaCRe57kfqu4+lRxaFEAuqmjzF0r+gWHjWqKqBvKFo=
cloud.google.com/go/serviceusage v1.4.0 h1:b0EwJxPJLpavSljMQh0RcdHsUrr5DQ+Nelt/3BAs5ro=
cloud.google.com/go/serviceusage v1.4.0/go.mod h1:SB4yxXSaYVuUBYUml6qklyONXNLt83U0Rb+CXyhjEeU=
cloud.google.com/go/shell v1.4.0 h1:b1LFhFBgKsG252inyhtmsUUZwchqSz3WTvAIf3JFo4g=
cloud.google.com/go/shell v1.4.0/go.mod h1:HDxPzZf3GkDdhExzD/gs8Grqk+dmYcEjGShZgYa9URw=
cloud.google.com/go/spanner v1.41.0 h1:NvdTpRwf7DTegbfFdPjAWyD7bOVu0VeMqcvR9aCQCAc=
cloud.google.com/go/spanner v1.41.0/go.mod h1:MLYDBJR/dY4Wt7ZaMIQ7rXOTLjYrmxLE/5ve9vFfWos=
cloud.google.com/go/speech v1.9.0 h1:yK0ocnFH4Wsf0cMdUyndJQ/hPv02oTJOxzi6AgpBy4s=
cloud.google.com/go/speech v1.9.0/go.mod h1:xQ0jTcmnRFFM2RfX/U+rk6FQNUF6DQlydUSyoooSpco=
cloud.google.com/go/storagetransfer v1.6.0 h1:fUe3OydbbvHcAYp07xY+2UpH4AermGbmnm7qdEj3tGE=
cloud.google.com/go/storagetransfer v1.6.0/go.mod h1:y77xm4CQV/ZhFZH75PLEXY0ROiS7Gh6pSKrM8dJyg6I=
cloud.google.com/go/talent v1.4.0 h1:MrekAGxLqAeAol4Sc0allOVqUGO8j+Iim8NMvpiD7tM=
cloud.google.com/go/talent v1.4.0/go.mod h1:ezFtAgVuRf8jRsvyE6EwmbTK5LKciD4KVnHuDEFmOOA=
cloud.google.com/go/texttospeech v1.5.0 h1:ccPiHgTewxgyAeCWgQWvZvrLmbfQSFABTMAfrSPLPyY=
cloud.google.com/go/texttospeech v1.5.0/go.mod h1:oKPLhR4n4ZdQqWKURdwxMy0uiTS1xU161C8W57Wkea4=
cloud.google.com/go/tpu v1.4.0 h1:ztIdKoma1Xob2qm6QwNh4Xi9/e7N3IfvtwG5AcNsj1g=
cloud.google.com/go/tpu v1.4.0/go.mod h1:mjZaX8p0VBgllCzF6wcU2ovUXN9TONFLd7iz227X2Xg=
cloud.google.com/go/trace v1.4.0 h1:qO9eLn2esajC9sxpqp1YKX37nXC3L4BfGnPS0Cx9dYo=
cloud.google.com/go/trace v1.4.0/go.mod h1:UG0v8UBqzusp+z63o7FK74SdFE+AXpCLdFb1rshXG+Y=
cloud.google.com/go/translate v1.4.0 h1:AOYOH3MspzJ/bH1YXzB+xTE8fMpn3mwhLjugwGXvMPI=
cloud.google.com/go/translate v1.4.0/go.mod h1:06Dn/ppvLD6WvA5Rhdp029IX2Mi3Mn7fpMRLPvXT5Wg=
cloud.google.com/go/video v1.9.0 h1:ttlvO4J5c1VGq6FkHqWPD/aH6PfdxujHt+muTJlW1Zk=
cloud.google.com/go/video v1.9.0/go.mod h1:0RhNKFRF5v92f8dQt0yhaHrEuH95m068JYOvLZYnJSw=
cloud.google.com/go/videointelligence v1.9.0 h1:RPFgVVXbI2b5vnrciZjtsUgpNKVtHO/WIyXUhEfuMhA=
cloud.google.com/go/videointelligence v1.9.0/go.mod h1:29lVRMPDYHikk3v8EdPSaL8Ku+eMzDljjuvRs105XoU=
cloud.google.com/go/vision/v2 v2.5.0 h1:TQHxRqvLMi19azwm3qYuDbEzZWmiKJNTpGbkNsfRCik=
cloud.google.com/go/vision/v2 v2.5.0/go.mod h1:MmaezXOOE+IWa+cS7OhRRLK2cNv1ZL98zhqFFZaaH2E=
cloud.google.com/go/vmmigration v1.3.0 h1:A2Tl2ZmwMRpvEmhV2ibISY85fmQR+Y5w9a0PlRz5P3s=
cloud.google.com/go/vmmigration v1.3.0/go.mod h1:oGJ6ZgGPQOFdjHuocGcLqX4lc98YQ7Ygq8YQwHh9A7g=
cloud.google.com/go/vmwareengine v0.1.0 h1:JMPZaOT/gIUxVlTqSl/QQ32Y2k+r0stNeM1NSqhVP9o=
cloud.google.com/go/vmwareengine v0.1.0/go.mod h1:RsdNEf/8UDvKllXhMz5J40XxDrNJNN4sagiox+OI208=
cloud.google.com/go/vpcaccess v1.5.0 h1:woHXXtnW8b9gLFdWO9HLPalAddBQ9V4LT+1vjKwR3W8=
cloud.google.com/go/vpcaccess v1.5.0/go.mod h1:drmg4HLk9NkZpGfCmZ3Tz0Bwnm2+DKqViEpeEpOq0m8=
cloud.google.com/go/webrisk v1.7.0 h1:ypSnpGlJnZSXbN9a13PDmAYvVekBLnGKxQ3Q9SMwnYY=
cloud.google.com/go/webrisk v1.7.0/go.mod h1:mVMHgEYH0r337nmt1JyLthzMr6YxwN1aAIEc2fTcq7A=
cloud.google.com/go/websecurityscanner v1.4.0 h1:y7yIFg/h/mO+5Y5aCOtVAnpGUOgqCH5rXQ2Oc8Oq2+g=
cloud.google.com/go/websecurityscanner v1.4.0/go.mod h1:ebit/Fp0a+FWu5j4JOmJEV8S8CzdTkAS77oDsiSqYWQ=
cloud.google.com/go/workflows v1.9.0 h1:7Chpin9p50NTU8Tb7qk+I11U/IwVXmDhEoSsdccvInE=
cloud.google.com/go/workflows v1.9.0/go.mod h1:ZGkj1aFIOd9c8Gerkjjq7OW7I5+l6cSvT3ujaO/WwSA=
github.com/census-instrumentation/opencensus-proto v0.4.1 h1:iKLQ0xPNFxR/2hzXZMrBo8f1j86j5WHzznCCQxV/b8g=
github.com/census-instrumentation/opencensus-proto v0.4.1/go.mod h1:4T9NM4+4Vw91VeyqjLS6ao50K5bOcLKN6Q42XnYaRYw=
github.com/cespare/xxhash/v2 v2.2.0 h1:DC2CZ1Ep5Y4k3ZQ899DldepgrayRUGE6BBZ/cd9Cj44=
github.com/cespare/xxhash/v2 v2.2.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/cespare/xxhash/v2 v2.3.0 h1:UL815xU9SqsFlibzuggzjXhog7bL6oX9BbNZnL2UFvs=
github.com/cespare/xxhash/v2 v2.3.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/chromedp/cdproto v0.0.0-20230802225258-3cf4e6d46a89 h1:aPflPkRFkVwbW6dmcVqfgwp1i+UWGFH6VgR1Jim5Ygc=
github.com/chromedp/cdproto v0.0.0-20230802225258-3cf4e6d46a89/go.mod h1:GKljq0VrfU4D5yc+2qA6OVr8pmO/MBbPEWqWQ/oqGEs=
github.com/chromedp/chromedp v0.9.2 h1:dKtNz4kApb06KuSXoTQIyUC2TrA0fhGDwNZf3bcgfKw=
github.com/chromedp/chromedp v0.9.2/go.mod h1:LkSXJKONWTCHAfQasKFUZI+mxqS4tZqhmtGzzhLsnLs=
github.com/chromedp/sysutil v1.0.0 h1:+ZxhTpfpZlmchB58ih/LBHX52ky7w2VhQVKQMucy3Ic=
github.com/chromedp/sysutil v1.0.0/go.mod h1:kgWmDdq8fTzXYcKIBqIYvRRTnYb9aNS9moAV0xufSww=
github.com/chzyer/readline v1.5.1 h1:upd/6fQk4src78LMRzh5vItIt361/o4uq553V8B5sGI=
github.com/chzyer/readline v1.5.1/go.mod h1:Eh+b79XXUwfKfcPLepksvw2tcLE/Ct21YObkaSkeBlk=
github.com/cncf/udpa/go v0.0.0-20220112060539-c52dc94e7fbe h1:QQ3GSy+MqSHxm/d8nCtnAiZdYFd45cYZPs8vOOIYKfk=
github.com/cncf/udpa/go v0.0.0-20220112060539-c52dc94e7fbe/go.mod h1:6pvJx4me5XPnfI9Z40ddWsdw2W/uZgQLFXToKeRcDiI=
github.com/cncf/xds/go v0.0.0-20230105202645-06c439db220b h1:ACGZRIr7HsgBKHsueQ1yM4WaVaXh21ynwqsF8M8tXhA=
github.com/cncf/xds/go v0.0.0-20230105202645-06c439db220b/go.mod h1:eXthEFrGJvWHgFFCl3hGmgk+/aYT6PnTQLykKQRLhEs=
github.com/cncf/xds/go v0.0.0-20240723142845-024c85f92f20 h1:N+3sFI5GUjRKBi+i0TxYVST9h4Ie192jJWpHvthBBgg=
github.com/cncf/xds/go v0.0.0-20240723142845-024c85f92f20/go.mod h1:W+zGtBO5Y1IgJhy4+A9GOqVhqLpfZi+vwmdNXUehLA8=
github.com/creack/pty v1.1.9 h1:uDmaGzcdjhF4i/plgjmEsriH11Y0o7RKapEf/LDaM3w=
github.com/envoyproxy/go-control-plane v0.10.3 h1:xdCVXxEe0Y3FQith+0cj2irwZudqGYvecuLB1HtdexY=
github.com/envoyproxy/go-control-plane v0.10.3/go.mod h1:fJJn/j26vwOu972OllsvAgJJM//w9BV6Fxbg2LuVd34=
github.com/envoyproxy/go-control-plane v0.13.0 h1:HzkeUz1Knt+3bK+8LG1bxOO/jzWZmdxpwC51i202les=
github.com/envoyproxy/go-control-plane v0.13.0/go.mod h1:GRaKG3dwvFoTg4nj7aXdZnvMg4d7nvT/wl9WgVXn3Q8=
github.com/envoyproxy/protoc-gen-validate v0.9.1 h1:PS7VIOgmSVhWUEeZwTe7z7zouA22Cr590PzXKbZHOVY=
github.com/envoyproxy/protoc-gen-validate v0.9.1/go.mod h1:OKNgG7TCp5pF4d6XftA0++PMirau2/yoOwVac3AbF2w=
github.com/envoyproxy/protoc-gen-validate v1.1.0 h1:tntQDh69XqOCOZsDz0lVJQez/2L6Uu2PdjCQwWCJ3bM=
github.com/envoyproxy/protoc-gen-validate v1.1.0/go.mod h1:sXRDRVmzEbkM7CVcM06s9shE/m23dg3wzjl0UWqJ2q4=
github.com/go-logr/logr v1.4.1 h1:pKouT5E8xu9zeFC39JXRDukb6JFQPXM5p5I91188VAQ=
github.com/go-logr/logr v1.4.1/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
github.com/go-logr/stdr v1.2.2 h1:hSWxHoqTgW2S2qGc0LTAI563KZ5YKYRhT3MFKZMbjag=
github.com/go-logr/stdr v1.2.2/go.mod h1:mMo/vtBO5dYbehREoey6XUKy/eSumjCCveDpRre4VKE=
github.com/gobwas/httphead v0.1.0 h1:exrUm0f4YX0L7EBwZHuCF4GDp8aJfVeBrlLQrs6NqWU=
github.com/gobwas/httphead v0.1.0/go.mod h1:O/RXo79gxV8G+RqlR/otEwx4Q36zl9rqC5u12GKvMCM=
github.com/gobwas/pool v0.2.1 h1:xfeeEhW7pwmX8nuLVlqbzVc7udMDrwetjEv+TZIz1og=
github.com/gobwas/pool v0.2.1/go.mod h1:q8bcK0KcYlCgd9e7WYLm9LpyS+YeLd8JVDW6WezmKEw=
github.com/gobwas/ws v1.2.1 h1:F2aeBZrm2NDsc7vbovKrWSogd4wvfAxg0FQ89/iqOTk=
github.com/gobwas/ws v1.2.1/go.mod h1:hRKAFb8wOxFROYNsT1bqfWnhX+b5MFeJM9r2ZSwg/KY=
github.com/golang/glog v1.0.0 h1:nfP3RFugxnNRyKgeWd4oI1nYvXpxrx8ck8ZrcizshdQ=
github.com/golang/glog v1.0.0/go.mod h1:EWib/APOK0SL3dFbYqvxE3UYd8E6s1ouQ7iEp/0LWV4=
github.com/golang/glog v1.2.2 h1:1+mZ9upx1Dh6FmUTFR1naJ77miKiXgALjWOZ3NVFPmY=
github.com/golang/glog v1.2.2/go.mod h1:6AhwSGph0fcJtXVM/PEHPqZlFeoLxhs7/t5UDAwmO+w=
github.com/golang/protobuf v1.5.0 h1:LUVKkCeviFUMKqHa4tXIIij/lbhnMbP7Fn5wKdKkRh4=
github.com/golang/protobuf v1.5.0/go.mod h1:FsONVRAS9T7sI+LIUmWTfcYkHO4aIWwzhcaSAoJOfIk=
github.com/google/go-cmp v0.6.0 h1:ofyhxvXcZhMsU5ulbFiLKl/XBFqE1GSq7atu8tAmTRI=
github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/uuid v1.3.0 h1:t6JiXgmwXMjEs8VusXIJk2BXHsn+wx8BZdTaoZ5fu7I=
github.com/google/uuid v1.3.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/ianlancetaylor/demangle v0.0.0-20230524184225-eabc099b10ab h1:BA4a7pe6ZTd9F8kXETBoijjFJ/ntaa//1wiH9BZu4zU=
github.com/ianlancetaylor/demangle v0.0.0-20230524184225-eabc099b10ab/go.mod h1:gx7rwoVhcfuVKG5uya9Hs3Sxj7EIvldVofAWIUtGouw=
github.com/josharian/intern v1.0.0 h1:vlS4z54oSdjm0bgjRigI+G1HpF+tI+9rE5LLzOg8HmY=
github.com/josharian/intern v1.0.0/go.mod h1:5DoeVV0s6jJacbCEi61lwdGj/aVlrQvzHFFd8Hwg//Y=
github.com/kr/pty v1.1.1 h1:VkoXIwSboBpnk99O/KFauAEILuNHv5DVFKZMBN/gUgw=
github.com/mailru/easyjson v0.7.7 h1:UGYAvKxe3sBsEDzO8ZeWOSlIQfWFlxbzLZe7hwFURr0=
github.com/mailru/easyjson v0.7.7/go.mod h1:xzfreul335JAWq5oZzymOObrkdz5UnU4kGfJJLY9Nlc=
github.com/pkg/diff v0.0.0-20210226163009-20ebb0f2a09e h1:aoZm08cpOy4WuID//EZDgcC4zIxODThtZNPirFr42+A=
github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10 h1:GFCKgmp0tecUJ0sJuv4pzYCqS9+RGSn52M3FUwPs+uo=
github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10/go.mod h1:t/avpk3KcrXxUnYOhZhMXJlSEyie6gQbtLq5NM3loB8=
github.com/stretchr/testify v1.11.1/go.mod h1:wZwfW3scLgRK+23gO65QZefKpKQRnfz6sD981Nm4B6U=
github.com/yuin/goldmark v1.4.13 h1:fVcFKWvrslecOb/tg+Cc05dkeYx540o0FuFt3nUVDoE=
github.com/yuin/goldmark v1.4.13/go.mod h1:6yULJ656Px+3vBD8DxQVa3kxgyrAnzto9xy5taEt/CY=
go.opentelemetry.io/otel v1.13.0 h1:1ZAKnNQKwBBxFtww/GwxNUyTf0AxkZzrukO8MeXqe4Y=
go.opentelemetry.io/otel v1.13.0/go.mod h1:FH3RtdZCzRkJYFTCsAKDy9l/XYjMdNv6QrkFFB8DvVg=
go.opentelemetry.io/otel/metric v1.24.0 h1:6EhoGWWK28x1fbpA4tYTOWBkPefTDQnb8WSGXlc88kI=
go.opentelemetry.io/otel/metric v1.24.0/go.mod h1:VYhLe1rFfxuTXLgj4CBiyz+9WYBA8pNGJgDcSFRKBco=
go.opentelemetry.io/otel/trace v1.24.0 h1:CsKnnL4dUAr/0llH9FKuc698G04IrpWV0MQA/Y1YELI=
go.opentelemetry.io/otel/trace v1.24.0/go.mod h1:HPc3Xr/cOApsBI154IU0OI0HJexz+aw5uPdbs3UCjNU=
golang.org/x/crypto v0.23.0 h1:dIJU/v2J8Mdglj/8rJ6UUOM3Zc9zLZxVZwwxMooUSAI=
golang.org/x/crypto v0.23.0/go.mod h1:CKFgDieR+mRhux2Lsu27y0fO304Db0wZe70UKqHu0v8=
golang.org/x/crypto v0.26.0 h1:RrRspgV4mU+YwB4FYnuBoKsUapNIL5cohGAmSH3azsw=
golang.org/x/crypto v0.26.0/go.mod h1:GY7jblb9wI+FOo5y8/S2oY4zWP07AkOJ4+jxCqdqn54=
golang.org/x/crypto v0.39.0 h1:SHs+kF4LP+f+p14esP5jAoDpHU8Gu/v9lFRK6IT5imM=
golang.org/x/crypto v0.39.0/go.mod h1:L+Xg3Wf6HoL4Bn4238Z6ft6KfEpN0tJGo53AAPC632U=
golang.org/x/mod v0.8.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/net v0.19.0 h1:zTwKpTd2XuCqf8huc7Fo2iSy+4RHPd10s4KzeTnVr1c=
golang.org/x/net v0.19.0/go.mod h1:CfAk/cbD4CthTvqiEl8NpboMuiuOYsAr/7NOjZJtv1U=
golang.org/x/net v0.25.0 h1:d/OCCoBEUq33pjydKrGQhw7IlUPI2Oylr+8qLx49kac=
golang.org/x/net v0.25.0/go.mod h1:JkAGAh7GEvH74S6FOH42FLoXpXbE/aqXSrIQjXgsiwM=
golang.org/x/oauth2 v0.4.0 h1:NF0gk8LVPg1Ml7SSbGyySuoxdsXitj7TvgvuRxIMc/M=
golang.org/x/oauth2 v0.4.0/go.mod h1:RznEsdpjGAINPTOF0UH/t+xJ75L18YO3Ho6Pyn+uRec=
golang.org/x/oauth2 v0.22.0 h1:BzDx2FehcG7jJwgWLELCdmLuxk2i+x9UDpSiss2u0ZA=
golang.org/x/oauth2 v0.22.0/go.mod h1:XYTD2NtWslqkgxebSiOHnXEap4TF09sJSc7H1sXbhtI=
golang.org/x/sync v0.7.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sys v0.5.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.6.0 h1:MVltZSvRTcU2ljQOhs94SXPftV6DCNnZViHeQps87pQ=
golang.org/x/sys v0.6.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.20.0 h1:Od9JTbYCk261bKm4M/mw7AklTlFYIa0bIp9BgSm1S8Y=
golang.org/x/sys v0.20.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.33.0 h1:q3i8TbbEz+JRD9ywIRlyRAQbM0qF7hu24q3teo2hbuw=
golang.org/x/sys v0.33.0/go.mod h1:BJP2sWEmIv4KK5OTEluFJCKSidICx8ciO85XgH3Ak8k=
golang.org/x/telemetry v0.0.0-20240228155512-f48c80bd79b2 h1:IRJeR9r1pYWsHKTRe/IInb7lYvbBVIqOgsX/u0mbOWY=
golang.org/x/telemetry v0.0.0-20240228155512-f48c80bd79b2/go.mod h1:TeRTkGYfJXctD9OcfyVLyj2J3IxLnKwHJR8f4D8a3YE=
golang.org/x/term v0.20.0 h1:VnkxpohqXaOBYJtBmEppKUG6mXpi+4O6purfc2+sMhw=
golang.org/x/term v0.20.0/go.mod h1:8UkIAJTvZgivsXaD6/pH6U9ecQzZ45awqEOzuCvwpFY=
golang.org/x/term v0.23.0 h1:F6D4vR+EHoL9/sWAWgAR1H2DcHr4PareCbAaCo1RpuU=
golang.org/x/term v0.23.0/go.mod h1:DgV24QBUrK6jhZXl+20l6UWznPlwAHm1Q1mGHtydmSk=
golang.org/x/term v0.32.0 h1:DR4lr0TjUs3epypdhTOkMmuF5CDFJ/8pOnbzMZPQ7bg=
golang.org/x/term v0.32.0/go.mod h1:uZG1FhGx848Sqfsq4/DlJr3xGGsYMu/L5GW4abiaEPQ=
golang.org/x/text v0.26.0 h1:P42AVeLghgTYr4+xUnTRKDMqpar+PtX7KWuNQL21L8M=
golang.org/x/text v0.26.0/go.mod h1:QK15LZJUUQVJxhz7wXgxSy/CJaTFjd0G+YLonydOVQA=
golang.org/x/tools v0.6.0/go.mod h1:Xwgl3UAJ/d3gWutnCtw505GrjyAbvKui8lOU390QaIU=
golang.org/x/tools v0.13.0/go.mod h1:HvlwmtVNQAhOuCjW7xxvovg8wbNq7LwfXh/k7wXUl58=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543 h1:E7g+9GITq07hpfrRu66IVDexMakfv52eLZ2CXBWiKr4=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/appengine v1.6.7 h1:FZR1q0exgwxzPzp/aF+VccGrSfxfPpkBqjIIEq3ru6c=
google.golang.org/appengine v1.6.7/go.mod h1:8WjMMxjGQR8xUklV/ARdw2HLXBOI7O7uCIDZVag1xfc=
google.golang.org/genproto/googleapis/api v0.0.0-20240814211410-ddb44dafa142 h1:wKguEg1hsxI2/L3hUYrpo1RVi48K+uTyzKqprwLXsb8=
google.golang.org/genproto/googleapis/api v0.0.0-20240814211410-ddb44dafa142/go.mod h1:d6be+8HhtEtucleCbxpPW9PA9XwISACu8nvpPqF0BVo=
google.golang.org/grpc v1.51.0 h1:E1eGv1FTqoLIdnBCZufiSHgKjlqG6fKFf6pPWtMTh8U=
google.golang.org/grpc v1.51.0/go.mod h1:wgNDFcnuBGmxLKI/qn4T+m5BtEBYXJPvibbUPsAIPww=
```

## File: `logger.go`
```go
package pyroscope

import "fmt"

// these loggers implement the types.Logger interface

type noopLoggerImpl struct{}

func (*noopLoggerImpl) Infof(_ string, _ ...interface{})  {}
func (*noopLoggerImpl) Debugf(_ string, _ ...interface{}) {}
func (*noopLoggerImpl) Errorf(_ string, _ ...interface{}) {}

type standardLoggerImpl struct{}

func (*standardLoggerImpl) Infof(a string, b ...interface{}) {
	fmt.Printf("[INFO]  "+a+"\n", b...) //nolint:forbidigo
}
func (*standardLoggerImpl) Debugf(a string, b ...interface{}) {
	fmt.Printf("[DEBUG] "+a+"\n", b...) //nolint:forbidigo
}
func (*standardLoggerImpl) Errorf(a string, b ...interface{}) {
	fmt.Printf("[ERROR] "+a+"\n", b...) //nolint:forbidigo
}

var (
	noopLogger     = &noopLoggerImpl{}     //nolint:gochecknoglobals
	StandardLogger = &standardLoggerImpl{} //nolint:gochecknoglobals
)
```

## File: `sample_types.go`
```go
package pyroscope

import (
	"github.com/grafana/pyroscope-go/upstream"
)

var (
	sampleTypeConfigHeap = map[string]*upstream.SampleType{ //nolint:gochecknoglobals
		"alloc_objects": {
			Units:      "objects",
			Cumulative: false,
		},
		"alloc_space": {
			Units:      "bytes",
			Cumulative: false,
		},
		"inuse_space": {
			Units:       "bytes",
			Aggregation: "average",
			Cumulative:  false,
		},
		"inuse_objects": {
			Units:       "objects",
			Aggregation: "average",
			Cumulative:  false,
		},
	}
	sampleTypeConfigMutex = map[string]*upstream.SampleType{ //nolint:gochecknoglobals
		"contentions": {
			DisplayName: "mutex_count",
			Units:       "lock_samples",
			Cumulative:  false,
		},
		"delay": {
			DisplayName: "mutex_duration",
			Units:       "lock_nanoseconds",
			Cumulative:  false,
		},
	}
	sampleTypeConfigBlock = map[string]*upstream.SampleType{ //nolint:gochecknoglobals
		"contentions": {
			DisplayName: "block_count",
			Units:       "lock_samples",
			Cumulative:  false,
		},
		"delay": {
			DisplayName: "block_duration",
			Units:       "lock_nanoseconds",
			Cumulative:  false,
		},
	}
)
```

## File: `session.go`
```go
package pyroscope

import (
	"bytes"
	"math"
	"runtime"
	"runtime/debug"
	"runtime/pprof"
	"sync"
	"time"

	"github.com/grafana/pyroscope-go/godeltaprof"
	"github.com/grafana/pyroscope-go/internal/labelset"
	"github.com/grafana/pyroscope-go/upstream"
)

type Session struct {
	// configuration, doesn't change
	upstream      upstream.Upstream
	profileTypes  []ProfileType
	uploadRate    time.Duration
	disableGCRuns bool
	// Deprecated: the field will be removed in future releases.
	DisableAutomaticResets bool

	logger   Logger
	stopOnce sync.Once
	stopCh   chan struct{}
	wg       sync.WaitGroup
	flushCh  chan *flush

	// these things do change:
	memBuf *bytes.Buffer

	goroutinesBuf *bytes.Buffer
	mutexBuf      *bytes.Buffer
	blockBuf      *bytes.Buffer

	lastGCGeneration uint32
	appName          string
	startTime        time.Time

	deltaBlock *godeltaprof.BlockProfiler
	deltaMutex *godeltaprof.BlockProfiler
	deltaHeap  *godeltaprof.HeapProfiler
	cpu        *cpuProfileCollector
}

type SessionConfig struct {
	Upstream       upstream.Upstream
	Logger         Logger
	AppName        string
	Tags           map[string]string
	ProfilingTypes []ProfileType
	DisableGCRuns  bool
	UploadRate     time.Duration

	// Deprecated: the field will be removed in future releases.
	// Use UploadRate instead.
	DisableAutomaticResets bool
	// Deprecated: the field will be removed in future releases.
	// DisableCumulativeMerge is ignored.
	DisableCumulativeMerge bool
	// Deprecated: the field will be removed in future releases.
	// SampleRate is set to 100 and is not configurable.
	SampleRate uint32
}

type flush struct {
	wg   sync.WaitGroup
	wait bool
}

func NewSession(c SessionConfig) (*Session, error) {
	if c.UploadRate == 0 {
		// For backward compatibility.
		c.UploadRate = 15 * time.Second
	}

	c.Logger.Infof("starting profiling session:")
	c.Logger.Infof("  AppName:        %+v", c.AppName)
	c.Logger.Infof("  Tags:           %+v", c.Tags)
	c.Logger.Infof("  ProfilingTypes: %+v", c.ProfilingTypes)
	c.Logger.Infof("  DisableGCRuns:  %+v", c.DisableGCRuns)
	c.Logger.Infof("  UploadRate:     %+v", c.UploadRate)

	if c.DisableAutomaticResets {
		c.UploadRate = math.MaxInt64
	}

	appName, err := mergeTagsWithAppName(c.AppName, newSessionID(), c.Tags)
	if err != nil {
		return nil, err
	}

	ps := &Session{
		upstream:      c.Upstream,
		appName:       appName,
		profileTypes:  c.ProfilingTypes,
		disableGCRuns: c.DisableGCRuns,
		uploadRate:    c.UploadRate,
		stopCh:        make(chan struct{}),
		flushCh:       make(chan *flush),
		logger:        c.Logger,
		memBuf:        &bytes.Buffer{},
		goroutinesBuf: &bytes.Buffer{},
		mutexBuf:      &bytes.Buffer{},
		blockBuf:      &bytes.Buffer{},

		deltaBlock: godeltaprof.NewBlockProfiler(),
		deltaMutex: godeltaprof.NewMutexProfiler(),
		deltaHeap:  godeltaprof.NewHeapProfiler(),
		cpu:        newCPUProfileCollector(appName, c.Upstream, c.Logger, c.UploadRate),
	}

	return ps, nil
}

// mergeTagsWithAppName validates user input and merges explicitly specified
// tags with tags from app name.
//
// App name may be in the full form including tags (app.name{foo=bar,baz=qux}).
// Returned application name is always short, any tags that were included are
// moved to tags map. When merged with explicitly provided tags (config/CLI),
// last take precedence.
//
// App name may be an empty string. Tags must not contain reserved keys,
// the map is modified in place.
func mergeTagsWithAppName(appName string, sid sessionID, tags map[string]string) (string, error) {
	k, err := labelset.Parse(appName)
	if err != nil {
		return "", err
	}
	for tagKey, tagValue := range tags {
		if labelset.IsLabelNameReserved(tagKey) {
			continue
		}
		err = labelset.ValidateLabelName(tagKey)
		if err != nil {
			return "", err
		}
		k.Add(tagKey, tagValue)
	}
	k.Add(sessionIDLabelName, sid.String())

	return k.Normalized(), nil
}

// revive:disable-next-line:cognitive-complexity complexity is fine
func (ps *Session) takeSnapshots() {
	t := time.NewTicker(ps.uploadRate)
	defer t.Stop()
	for {
		select {
		case endTime := <-t.C:
			ps.reset(ps.startTime, endTime)

		case f := <-ps.flushCh:
			ps.reset(ps.startTime, ps.truncatedTime())
			_ = ps.cpu.Flush()
			ps.upstream.Flush()
			f.wg.Done()

		case <-ps.stopCh:
			if ps.isCPUEnabled() {
				ps.cpu.Stop()
			}

			return
		}
	}
}

func copyBuf(b []byte) []byte {
	r := make([]byte, len(b))
	copy(r, b)

	return r
}

func (ps *Session) Start() error {
	t := ps.truncatedTime()
	ps.reset(t, t)

	ps.wg.Add(1)
	go func() {
		defer ps.wg.Done()
		ps.takeSnapshots()
	}()

	if ps.isCPUEnabled() {
		ps.wg.Add(1)
		go func() {
			defer ps.wg.Done()
			ps.cpu.Start()
		}()
	}

	return nil
}

func (ps *Session) isCPUEnabled() bool {
	for _, t := range ps.profileTypes {
		if t == ProfileCPU {
			return true
		}
	}

	return false
}

func (ps *Session) isMemEnabled() bool {
	for _, t := range ps.profileTypes {
		if t == ProfileInuseObjects || t == ProfileAllocObjects || t == ProfileInuseSpace || t == ProfileAllocSpace {
			return true
		}
	}

	return false
}

func (ps *Session) isBlockEnabled() bool {
	for _, t := range ps.profileTypes {
		if t == ProfileBlockCount || t == ProfileBlockDuration {
			return true
		}
	}

	return false
}

func (ps *Session) isMutexEnabled() bool {
	for _, t := range ps.profileTypes {
		if t == ProfileMutexCount || t == ProfileMutexDuration {
			return true
		}
	}

	return false
}

func (ps *Session) isGoroutinesEnabled() bool {
	for _, t := range ps.profileTypes {
		if t == ProfileGoroutines {
			return true
		}
	}

	return false
}

func (ps *Session) reset(startTime, endTime time.Time) {
	ps.logger.Debugf("profiling session reset %s", startTime.String())
	// first reset should not result in an upload
	if !ps.startTime.IsZero() {
		ps.uploadData(startTime, endTime)
	}
	ps.startTime = endTime
}

func (ps *Session) uploadData(startTime, endTime time.Time) {
	if ps.isGoroutinesEnabled() {
		p := pprof.Lookup("goroutine")
		if p != nil {
			err := p.WriteTo(ps.goroutinesBuf, 0)
			if err != nil {
				ps.logger.Errorf("failed to dump goroutines profile: %s", err)

				return
			}
			ps.upstream.Upload(&upstream.UploadJob{
				Name:            ps.appName,
				StartTime:       startTime,
				EndTime:         endTime,
				SpyName:         "gospy",
				Units:           "goroutines",
				AggregationType: "average",
				Format:          upstream.FormatPprof,
				Profile:         copyBuf(ps.goroutinesBuf.Bytes()),
				SampleTypeConfig: map[string]*upstream.SampleType{
					"goroutine": {
						DisplayName: "goroutines",
						Units:       "goroutines",
						Aggregation: "average",
					},
				},
			})
			ps.goroutinesBuf.Reset()
		}
	}

	if ps.isBlockEnabled() {
		ps.dumpBlockProfile(startTime, endTime)
	}
	if ps.isMutexEnabled() {
		ps.dumpMutexProfile(startTime, endTime)
	}
	if ps.isMemEnabled() {
		ps.dumpHeapProfile(startTime, endTime)
	}
}

func (ps *Session) dumpHeapProfile(startTime time.Time, endTime time.Time) {
	defer func() {
		if r := recover(); r != nil {
			ps.logger.Errorf("dump heap profiler panic %s", string(debug.Stack()))
		}
	}()
	currentGCGeneration := numGC()
	// sometimes GC doesn't run within 10 seconds
	//   in such cases we force a GC run
	//   users can disable it with disableGCRuns option
	if currentGCGeneration == ps.lastGCGeneration && !ps.disableGCRuns {
		runtime.GC()
		currentGCGeneration = numGC()
	}
	if currentGCGeneration != ps.lastGCGeneration {
		ps.memBuf.Reset()
		err := ps.deltaHeap.Profile(ps.memBuf)
		if err != nil {
			ps.logger.Errorf("failed to dump heap profile: %s", err)

			return
		}
		curMemBytes := copyBuf(ps.memBuf.Bytes())
		job := &upstream.UploadJob{
			Name:             ps.appName,
			StartTime:        startTime,
			EndTime:          endTime,
			SpyName:          "gospy",
			SampleRate:       100,
			Format:           upstream.FormatPprof,
			Profile:          curMemBytes,
			SampleTypeConfig: sampleTypeConfigHeap,
		}
		ps.upstream.Upload(job)
		ps.lastGCGeneration = currentGCGeneration
	}
}

func (ps *Session) dumpMutexProfile(startTime time.Time, endTime time.Time) {
	defer func() {
		if r := recover(); r != nil {
			ps.logger.Errorf("dump mutex profiler panic %s", string(debug.Stack()))
		}
	}()
	ps.mutexBuf.Reset()
	err := ps.deltaMutex.Profile(ps.mutexBuf)
	if err != nil {
		ps.logger.Errorf("failed to dump mutex profile: %s", err)

		return
	}
	curMutexBuf := copyBuf(ps.mutexBuf.Bytes())
	job := &upstream.UploadJob{
		Name:             ps.appName,
		StartTime:        startTime,
		EndTime:          endTime,
		SpyName:          "gospy",
		Format:           upstream.FormatPprof,
		Profile:          curMutexBuf,
		SampleTypeConfig: sampleTypeConfigMutex,
	}
	ps.upstream.Upload(job)
}

func (ps *Session) dumpBlockProfile(startTime time.Time, endTime time.Time) {
	defer func() {
		if r := recover(); r != nil {
			ps.logger.Errorf("dump block profiler panic %s", string(debug.Stack()))
		}
	}()
	ps.blockBuf.Reset()
	err := ps.deltaBlock.Profile(ps.blockBuf)
	if err != nil {
		ps.logger.Errorf("failed to dump block profile: %s", err)

		return
	}
	curBlockBuf := copyBuf(ps.blockBuf.Bytes())
	job := &upstream.UploadJob{
		Name:             ps.appName,
		StartTime:        startTime,
		EndTime:          endTime,
		SpyName:          "gospy",
		Format:           upstream.FormatPprof,
		Profile:          curBlockBuf,
		SampleTypeConfig: sampleTypeConfigBlock,
	}
	ps.upstream.Upload(job)
}

func (ps *Session) Stop() {
	ps.stopOnce.Do(func() {
		close(ps.stopCh)
		ps.wg.Wait()
	})
}

func (ps *Session) flush(wait bool) {
	f := &flush{
		wg:   sync.WaitGroup{},
		wait: wait,
	}
	f.wg.Add(1)
	ps.flushCh <- f
	if wait {
		f.wg.Wait()
	}
}

func (ps *Session) truncatedTime() time.Time {
	return time.Now().Truncate(ps.uploadRate)
}

func numGC() uint32 {
	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)

	return memStats.NumGC
}
```

## File: `session_id.go`
```go
package pyroscope

import (
	crand "crypto/rand"
	"encoding/binary"
	"encoding/hex"
	"hash/fnv"
	"math/rand"
	"os"
	"sync"
)

const sessionIDLabelName = "__session_id__"

type sessionID uint64

func (s sessionID) String() string {
	var b [8]byte
	binary.LittleEndian.PutUint64(b[:], uint64(s))

	return hex.EncodeToString(b[:])
}

func newSessionID() sessionID { return globalSessionIDGenerator.newSessionID() }

var globalSessionIDGenerator = newSessionIDGenerator() //nolint:gochecknoglobals

type sessionIDGenerator struct {
	sync.Mutex

	src *rand.Rand
}

func (gen *sessionIDGenerator) newSessionID() sessionID {
	var b [8]byte
	gen.Lock()
	_, _ = gen.src.Read(b[:])
	gen.Unlock()

	return sessionID(binary.LittleEndian.Uint64(b[:]))
}

func newSessionIDGenerator() *sessionIDGenerator {
	s, ok := sessionIDHostSeed()
	if !ok {
		s = sessionIDRandSeed()
	}

	return &sessionIDGenerator{src: rand.New(rand.NewSource(s))} //nolint:gosec
}

func sessionIDRandSeed() int64 {
	var rndSeed int64
	_ = binary.Read(crand.Reader, binary.LittleEndian, &rndSeed)

	return rndSeed
}

func sessionIDHostSeed() (int64, bool) {
	v, err := os.Hostname()
	if err != nil {
		return 0, false
	}
	h := fnv.New64a()
	_, _ = h.Write([]byte(v))

	return int64(h.Sum64()), true //nolint:gosec
}
```

## File: `types.go`
```go
package pyroscope

type ProfileType string

// Logger is an interface that library users can use
// It is based on logrus, but much smaller — That's because we don't want library users to have to implement
// all of the logrus's methods
type Logger interface {
	Infof(_ string, _ ...interface{})
	Debugf(_ string, _ ...interface{})
	Errorf(_ string, _ ...interface{})
}

const (
	ProfileCPU           ProfileType = "cpu"
	ProfileInuseObjects  ProfileType = "inuse_objects"
	ProfileAllocObjects  ProfileType = "alloc_objects"
	ProfileInuseSpace    ProfileType = "inuse_space"
	ProfileAllocSpace    ProfileType = "alloc_space"
	ProfileGoroutines    ProfileType = "goroutines"
	ProfileMutexCount    ProfileType = "mutex_count"
	ProfileMutexDuration ProfileType = "mutex_duration"
	ProfileBlockCount    ProfileType = "block_count"
	ProfileBlockDuration ProfileType = "block_duration"
	DefaultSampleRate                = 100
)

var DefaultProfileTypes = []ProfileType{ //nolint:gochecknoglobals
	ProfileCPU,
	ProfileAllocObjects,
	ProfileAllocSpace,
	ProfileInuseObjects,
	ProfileInuseSpace,
}
```

## File: `example/http/Dockerfile`
```
FROM golang:1.21.5

WORKDIR /go/src/app

COPY main.go go.mod go.sum ./

RUN go get -d ./
RUN go build -o main .

CMD ["./main"]
```

## File: `example/http/README.md`
```markdown
# Pyroscope CPU Profiler HTTP Handler

This is an example of how you can use `github.com/grafana/pyroscope-go/http/pprof` package to use standard Go `/debug/pprof/profile` profiler along with Pyroscope continuous profiler.

### Problem

The standard Go pprof HTTP endpoint `/debug/pprof/profile` returns an error if profiling
is already started:

> Could not enable CPU profiling: CPU profiling already in use

This prevents you from using the standard Go pprof HTTP endpoint `/debug/pprof/profile` along with Pyroscope continuous profiler.

### Solution

This package facilitates the collection of CPU profiles via HTTP without disrupting the background operation of the Pyroscope profiler. It enables you to seamlessly gather CPU profiles through HTTP while continuously sending them to Pyroscope.

### How Does It Work

With each invocation of the handler, it suspends the Pyroscope profiler, gathers a CPU profile, dispatches the collected profile to both the caller and the Pyroscope profiler, and subsequently resumes the Pyroscope profiler.

### Recommendations

Standard `net/http/pprof` package registers its handlers automatically for the default HTTP server, but this package does not to avoid runtime errors due to the standard Go pprof HTTP endpoint `/debug/pprof/profile` being already registered.

It is highly recommended that you create a separate HTTP server and register pprof handlers on it. Then you can use Pyroscope's `github.com/grafana/pyroscope-go/http/pprof` package to register a handler that will collect CPU profiles and send them to Pyroscope while allowing you to still use the standard Go pprof HTTP endpoint `/debug/pprof/profile`.

### Example

```go
package main

import (
	"net/http"
	"net/http/pprof"
	"time"

	"github.com/grafana/pyroscope-go"
	pyroscope_pprof "github.com/grafana/pyroscope-go/http/pprof"
)

func main() {
	// Starting pyroscope profiler
	pyroscope.Start(pyroscope.Config{
		ApplicationName: "example-app",
		ServerAddress:   "http://pyroscope:4040",
	})

	// Setting up HTTP server
	mux := http.NewServeMux()
	server := &http.Server{
		Addr:    ":8080",
		Handler: mux,
	}

	// Standard pprof routes (copied from /net/http/pprof)
	mux.HandleFunc("/debug/pprof/", pprof.Index)
	mux.HandleFunc("/debug/pprof/cmdline", pprof.Cmdline)
	mux.HandleFunc("/debug/pprof/symbol", pprof.Symbol)
	mux.HandleFunc("/debug/pprof/trace", pprof.Trace)

	// This route is special: note that we're using Pyroscope handler here
	mux.HandleFunc("/debug/pprof/profile", pyroscope_pprof.Profile)

	go doMeaninglessWork()

	server.ListenAndServe()
}

// doMeaninglessWork does meaningless work to show CPU usage
func doMeaninglessWork() {
	for {
		for t := time.Now(); time.Now().Sub(t).Seconds() < 1; {
		}
	}
}
```

### Docker Compose Example

You can find a complete example of how to use this package in the [docker-compose.yml](./docker-compose.yml) file.

To run it:
```bash
docker-compose up --build
```

You can see Pyroscope data at [`http://localhost:4040/`](http://localhost:4040/?query=process_cpu%3Acpu%3Ananoseconds%3Acpu%3Ananoseconds%7Bservice_name%3D%22example-app%22%7D&from=now-5m), and if you want to see data from the standard Go pprof HTTP endpoint you can go to `http://localhost:8080/debug/pprof/profile`. Note that when you do that it does not disrupt the Pyroscope profiler:

```bash
curl http://localhost:8080/debug/pprof/profile > profile.pprof
pprof -http=:8081 profile.pprof
```

```

## File: `example/http/docker-compose.yml`
```yaml
---
version: '3.9'
services:
  pyroscope:
    image: 'grafana/pyroscope:latest'
    ports:
      - '4040:4040'

  app:
    build: .
    ports:
      - '8080:8080'
```

## File: `example/http/go.mod`
```
module http

go 1.21.3

require github.com/grafana/pyroscope-go v1.1.0
```

## File: `example/http/go.sum`
```
github.com/grafana/pyroscope-go v1.1.0 h1:Ds35iZ+xyZCx3+sw1qfSbPujSiMeyGvvXoH5BX4+J7Y=
github.com/grafana/pyroscope-go v1.1.0/go.mod h1:Mw26jU7jsL/KStNSGGuuVYdUq7Qghem5P8aXYXSXG88=
```

## File: `example/http/main.go`
```go
package main

import (
	"net/http"
	"net/http/pprof"
	"time"

	"github.com/grafana/pyroscope-go"
	pyroscope_pprof "github.com/grafana/pyroscope-go/http/pprof"
)

func main() {
	// Starting pyroscope profiler
	pyroscope.Start(pyroscope.Config{
		ApplicationName: "example-app",
		ServerAddress:   "http://pyroscope:4040",
	})

	// Setting up HTTP server
	mux := http.NewServeMux()
	server := &http.Server{
		Addr:    ":8080",
		Handler: mux,
	}

	// Standard pprof routes (copied from /net/http/pprof)
	mux.HandleFunc("/debug/pprof/", pprof.Index)
	mux.HandleFunc("/debug/pprof/cmdline", pprof.Cmdline)
	mux.HandleFunc("/debug/pprof/symbol", pprof.Symbol)
	mux.HandleFunc("/debug/pprof/trace", pprof.Trace)

	// This route is special: note that we're using Pyroscope handler here
	mux.HandleFunc("/debug/pprof/profile", pyroscope_pprof.Profile)

	go doMeaninglessWork()

	server.ListenAndServe()
}

// doMeaninglessWork does meaningless work to show CPU usage
func doMeaninglessWork() {
	for {
		for t := time.Now(); time.Now().Sub(t).Seconds() < 1; {
		}
	}
}
```

## File: `example/simple/main.go`
```go
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"runtime"
	"runtime/pprof"
	"sync"

	"github.com/grafana/pyroscope-go"
)

//go:noinline
func work(n int) {
	// revive:disable:empty-block this is fine because this is a example app, not real production code
	for i := 0; i < n; i++ {
	}
	fmt.Printf("work\n") //nolint:forbidigo
	// revive:enable:empty-block
}

var m sync.Mutex //nolint:gochecknoglobals

func fastFunction(c context.Context, wg *sync.WaitGroup) {
	m.Lock()
	defer m.Unlock()

	pyroscope.TagWrapper(c, pyroscope.Labels("function", "fast"), func(c context.Context) {
		work(200000000)
	})
	wg.Done()
}

func slowFunction(c context.Context, wg *sync.WaitGroup) {
	m.Lock()
	defer m.Unlock()

	// standard pprof.Do wrappers work as well
	pprof.Do(c, pprof.Labels("function", "slow"), func(c context.Context) {
		work(800000000)
	})
	wg.Done()
}

func main() {
	runtime.SetMutexProfileFraction(5)
	runtime.SetBlockProfileRate(5)
	p, err := pyroscope.Start(pyroscope.Config{
		ApplicationName:   "simple.golang.app-new",
		ServerAddress:     "http://localhost:4040",
		Logger:            pyroscope.StandardLogger,
		AuthToken:         os.Getenv("PYROSCOPE_AUTH_TOKEN"),
		TenantID:          os.Getenv("PYROSCOPE_TENANT_ID"),
		BasicAuthUser:     os.Getenv("PYROSCOPE_BASIC_AUTH_USER"),
		BasicAuthPassword: os.Getenv("PYROSCOPE_BASIC_AUTH_PASSWORD"),
		ProfileTypes: []pyroscope.ProfileType{
			pyroscope.ProfileCPU,
			pyroscope.ProfileInuseObjects,
			pyroscope.ProfileAllocObjects,
			pyroscope.ProfileInuseSpace,
			pyroscope.ProfileAllocSpace,
			pyroscope.ProfileGoroutines,
			pyroscope.ProfileMutexCount,
			pyroscope.ProfileMutexDuration,
			pyroscope.ProfileBlockCount,
			pyroscope.ProfileBlockDuration,
		},
		HTTPHeaders: map[string]string{"X-Extra-Header": "extra-header-value"},
	})
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		err = p.Stop()
		if err != nil {
			log.Fatal(err)
		}
	}()

	pyroscope.TagWrapper(context.Background(), pyroscope.Labels("foo", "bar"), func(c context.Context) {
		for {
			wg := sync.WaitGroup{}
			wg.Add(2)
			go fastFunction(c, &wg)
			go slowFunction(c, &wg)
			wg.Wait()
		}
	})
}
```

## File: `example/timing/timing.go`
```go
package main

import (
	"log"
	"math"
	"math/rand"
	"time"

	"github.com/grafana/pyroscope-go"
)

//go:noinline
func isPrime(n int64) bool {
	for i := int64(2); i <= n; i++ {
		if i*i > n {
			return true
		}
		if n%i == 0 {
			return false
		}
	}

	return false
}

//go:noinline
func slow(n int64) int64 {
	sum := int64(0)
	for i := int64(1); i <= n; i++ {
		sum += i
	}

	return sum
}

//go:noinline
func fast(n int64) int64 {
	sum := int64(0)
	root := int64(math.Sqrt(float64(n)))
	for a := int64(1); a <= n; a += root {
		b := a + root - 1
		if n < b {
			b = n
		}
		sum += (b - a + 1) * (a + b) / 2
	}

	return sum
}

//go:noinline
func slow0(n int64) int64 { return slow(n) }

//go:noinline
func slow1(n int64) int64 { return slow(n) }

//go:noinline
func slow2(n int64) int64 { return slow(n) }

//go:noinline
func slow3(n int64) int64 { return slow(n) }

//go:noinline
func slow4(n int64) int64 { return slow(n) }

//go:noinline
func slow5(n int64) int64 { return slow(n) }

//go:noinline
func slow6(n int64) int64 { return slow(n) }

//go:noinline
func slow7(n int64) int64 { return slow(n) }

//go:noinline
func slow8(n int64) int64 { return slow(n) }

//go:noinline
func slow9(n int64) int64 { return slow(n) }

//go:noinline
func slow10(n int64) int64 { return slow(n) }

//go:noinline
func slow11(n int64) int64 { return slow(n) }

//go:noinline
func slow12(n int64) int64 { return slow(n) }

//go:noinline
func slow13(n int64) int64 { return slow(n) }

//go:noinline
func slow14(n int64) int64 { return slow(n) }

//go:noinline
func slow15(n int64) int64 { return slow(n) }

//go:noinline
func fast0(n int64) int64 { return fast(n) }

//go:noinline
func fast1(n int64) int64 { return fast(n) }

//go:noinline
func fast2(n int64) int64 { return fast(n) }

//go:noinline
func fast3(n int64) int64 { return fast(n) }

//go:noinline
func fast4(n int64) int64 { return fast(n) }

//go:noinline
func fast5(n int64) int64 { return fast(n) }

//go:noinline
func fast6(n int64) int64 { return fast(n) }

//go:noinline
func fast7(n int64) int64 { return fast(n) }

//go:noinline
func fast8(n int64) int64 { return fast(n) }

//go:noinline
func fast9(n int64) int64 { return fast(n) }

//go:noinline
func fast10(n int64) int64 { return fast(n) }

//go:noinline
func fast11(n int64) int64 { return fast(n) }

//go:noinline
func fast12(n int64) int64 { return fast(n) }

//go:noinline
func fast13(n int64) int64 { return fast(n) }

//go:noinline
func fast14(n int64) int64 { return fast(n) }

//go:noinline
func fast15(n int64) int64 { return fast(n) }

//go:noinline
func isPrime0(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime1(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime2(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime3(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime4(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime5(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime6(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime7(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime8(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime9(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime10(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime11(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime12(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime13(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime14(n int64) bool { return isPrime(n) }

//go:noinline
func isPrime15(n int64) bool { return isPrime(n) }

//go:noinline
func slowMux(n, d int64) int64 {
	switch d {
	case 0:
		return slow0(n)
	case 1:
		return slow1(n)
	case 2:
		return slow2(n)
	case 3:
		return slow3(n)
	case 4:
		return slow4(n)
	case 5:
		return slow5(n)
	case 6:
		return slow6(n)
	case 7:
		return slow7(n)
	case 8:
		return slow8(n)
	case 9:
		return slow9(n)
	case 10:
		return slow10(n)
	case 11:
		return slow11(n)
	case 12:
		return slow12(n)
	case 13:
		return slow13(n)
	case 14:
		return slow14(n)
	default:
		return slow15(n)
	}
}

//go:noinline
func fastMux(n, d int64) int64 {
	switch d {
	case 0:
		return fast0(n)
	case 1:
		return fast1(n)
	case 2:
		return fast2(n)
	case 3:
		return fast3(n)
	case 4:
		return fast4(n)
	case 5:
		return fast5(n)
	case 6:
		return fast6(n)
	case 7:
		return fast7(n)
	case 8:
		return fast8(n)
	case 9:
		return fast9(n)
	case 10:
		return fast10(n)
	case 11:
		return fast11(n)
	case 12:
		return fast12(n)
	case 13:
		return fast13(n)
	case 14:
		return fast14(n)
	default:
		return fast15(n)
	}
}

//go:noinline
func isPrimeMux(n, d int64) bool {
	switch d {
	case 0:
		return isPrime0(n)
	case 1:
		return isPrime1(n)
	case 2:
		return isPrime2(n)
	case 3:
		return isPrime3(n)
	case 4:
		return isPrime4(n)
	case 5:
		return isPrime5(n)
	case 6:
		return isPrime6(n)
	case 7:
		return isPrime7(n)
	case 8:
		return isPrime8(n)
	case 9:
		return isPrime9(n)
	case 10:
		return isPrime10(n)
	case 11:
		return isPrime11(n)
	case 12:
		return isPrime12(n)
	case 13:
		return isPrime13(n)
	case 14:
		return isPrime14(n)
	default:
		return isPrime15(n)
	}
}

//go:noinline
func main() {
	pyroscopeProfiler, err := pyroscope.Start(pyroscope.Config{
		ApplicationName: "timing-demo",
		ServerAddress:   "http://localhost:4040",
		ProfileTypes: []pyroscope.ProfileType{
			pyroscope.ProfileCPU,
		},
		Logger: pyroscope.StandardLogger,
	})
	if err != nil {
		log.Fatal(err)

		return
	}
	defer func() {
		err = pyroscopeProfiler.Stop()
		if err != nil {
			log.Fatal(err)
		}
	}()

	startTime := time.Now()
	base := rand.Int63n(1000000) + 1 //nolint:gosec
	for i := int64(0); i < 40000000; i++ {
		secs := int64(time.Since(startTime) / time.Second)
		if secs > 15 {
			break
		}
		n := rand.Int63n(10000) + 1 //nolint:gosec

		if isPrimeMux(base+i, secs) {
			_ = slowMux(n, secs)
		} else {
			_ = fastMux(n, secs)
		}
	}
}
```

## File: `godeltaprof/.gitignore`
```
.idea/
```

## File: `godeltaprof/README.md`
```markdown
# godeltaprof

godeltaprof is an efficient delta profiler for memory, mutex, and block.

# Why

In Golang, allocation, mutex and block profiles are cumulative. They only grow over time and show allocations that happened since the beginning of the running program.
Not only values grow, but the size of the profile itself grows as well. It could grow up to megabytes in size for long-running processes. These megabytes profiles are called huge profiles in this document.

In many cases, it's more useful to see the differences between two points in time.
You can use the original runtime/pprof package, called a delta profile, to see these differences. 
Using the delta profile requires passing seconds argument to the pprof endpoint query.

```
go tool pprof http://localhost:6060/debug/pprof/heap?seconds=30
```

What this does:
1. Dump profile `p0`
2. Sleep
3. Dump profile `p1`
4. Decompress and parse protobuf `p0`
5. Decompress and parse protobuf `p1`
6. Subtract `p0` from `p1`
7. Serialize protobuf and compress the result

The resulting profile is *usually* much smaller (`p0` may be megabytes, while result is usually tens of kilobytes).

There are number of issues with this approach:

1. Heap profile contains both allocation values and in-use values. In-use values are not cumulative. In-use values are corrupted by the subtraction.
  **Note:** It can be fixed if runtime/pprof package uses `p0.ScaleN([]float64{-1,-1,0,0})`, instead of `p0.Scale(-1)` - that would subtract allocation values and zero out in-use values in `p0`.
2. It requires dumping two profiles.
3. It produces a lot of allocations putting pressure on GC.


## DataDog's fastdelta

DataDog's [fastdelta profiler](https://github.com/DataDog/dd-trace-go/blob/30e1406c2cb62af749df03d559853e1d1de0e3bf/profiler/internal/fastdelta/fd.go#L75) uses another approach. 

It improves the runtime/pprof approach by keeping a copy of the previous profile and subtracting the current profile from it.
The fastdelta profiler uses a custom protobuf pprof parser that doesn't allocate as much memory.
This approach is more efficient, faster, and produces less garbage. It also doesn't require using two profiles. 
However, the fastdelta profiler still parses huge profiles up to megabytes, just to discard most of it.

## godeltaprof

godeltaprof does a similar job but slightly differently.

Delta computation happens before serializing any pprof files using `runtime.MemprofileRecord` and `BlockProfileRecord`.
This way, huge profiles don't need to be parsed. The delta is computed on raw records, all zeros are rejected, and results are serialized and compressed.

The source code for godeltaprof is based (forked) on the original [runtime/pprof package](https://github.com/golang/go/tree/master/src/runtime/pprof).
godeltaprof is modified to include delta computation before serialization and to expose the new endpoints.
There are other small improvements and benefits:
- Using `github.com/klauspost/compress/gzip` instead of `compress/gzip`
- Optional lazy mappings reading (they don't change over time for most applications)
- Separate package from runtime, so updated independently 

# benchmarks

These benchmarks used memory profiles from the [pyroscope](https://github.com/grafana/pyroscope) server.

BenchmarkOG - dumps memory profile with runtime/pprof package
BenchmarkFastDelta - dumps memory profile with runtime/pprof package and computes delta using fastdelta
BenchmarkGodeltaprof - does not dump profile with runtime/pprof, computes delta, outputs it results

Each benchmark also outputs produced profile sizes.
```
BenchmarkOG
      63         181862189 ns/op
profile sizes: [209117 209107 209077 209089 209095 209076 209088 209082 209090 209092]

BenchmarkFastDelta
      43         273936764 ns/op
profile sizes: [169300 10815 8969 9511 9752 9376 9545 8959 10357 9536]

BenchmarkGodeltaprof
     366          31148264 ns/op
profile sizes: [208898 11485 9347 9967 10291 9848 10085 9285 11033 9986]
```

Notice how BenchmarkOG profiles sizes are ~200k and BenchmarkGodeltaprof and BenchmarkFastDelta are ~10k - that is because a lof of samples
with zero values are discarded after delta computation.

Source code of benchmarks could be found [here](https://github.com/grafana/pyroscope/compare/godeltaprofbench?expand=1) 

CPU profiles: [BenchmarkOG](https://flamegraph.com/share/a8f68312-98c7-11ee-a502-466f68d203a5), [BenchmarkFastDelta](https://flamegraph.com/share/c23821f3-98c7-11ee-a502-466f68d203a5),  [BenchmarkGodeltaprof]( https://flamegraph.com/share/ea66df36-98c7-11ee-9a0d-f2c25703e557)



# upstreaming

In the perfect world, this functionality exists in golang runtime/stdlib and we don't need godeltaprof library at all.

See golang proposals:
https://github.com/golang/go/issues/57765
https://github.com/golang/go/issues/67942



```

## File: `godeltaprof/block.go`
```go
package godeltaprof

import (
	"io"
	"runtime"
	"sort"
	"sync"

	"github.com/grafana/pyroscope-go/godeltaprof/internal/pprof"
)

// BlockProfiler is a stateful profiler for goroutine blocking events and mutex contention in Go programs.
// Depending on the function used to create the BlockProfiler, it uses either runtime.BlockProfile or
// runtime.MutexProfile.
// The BlockProfiler provides similar functionality to pprof.Lookup("block").WriteTo and pprof.Lookup("mutex").WriteTo,
// but with some key differences.
//
// The BlockProfiler tracks the delta of blocking events or mutex contention since the last
// profile was written, effectively providing a snapshot of the changes
// between two points in time. This is in contrast to the
// pprof.Lookup functions, which accumulate profiling data
// and result in profiles that represent the entire lifetime of the program.
//
// The BlockProfiler is safe for concurrent use, as it serializes access to
// its internal state using a sync.Mutex. This ensures that multiple goroutines
// can call the Profile method without causing any data race issues.
type BlockProfiler struct {
	impl           pprof.DeltaMutexProfiler
	mutex          sync.Mutex
	runtimeProfile func([]runtime.BlockProfileRecord) (int, bool)
	scaleProfile   pprof.MutexProfileScaler
	options        pprof.ProfileBuilderOptions
	gz             gz
}

// NewMutexProfiler creates a new BlockProfiler instance for profiling mutex contention.
// The resulting BlockProfiler uses runtime.MutexProfile as its data source.
//
// Usage:
//
//		mp := godeltaprof.NewMutexProfiler()
//	    ...
//	    err := mp.Profile(someWriter)
func NewMutexProfiler() *BlockProfiler {
	return &BlockProfiler{
		runtimeProfile: runtime.MutexProfile,
		scaleProfile:   pprof.ScalerMutexProfile,
		impl:           pprof.DeltaMutexProfiler{},
		options: pprof.ProfileBuilderOptions{
			GenericsFrames: true,
			LazyMapping:    true,
		},
	}
}

func NewMutexProfilerWithOptions(options ProfileOptions) *BlockProfiler {
	return &BlockProfiler{
		runtimeProfile: runtime.MutexProfile,
		scaleProfile:   pprof.ScalerMutexProfile,
		impl:           pprof.DeltaMutexProfiler{},
		options: pprof.ProfileBuilderOptions{
			GenericsFrames: options.GenericsFrames,
			LazyMapping:    options.LazyMappings,
		},
	}
}

// NewBlockProfiler creates a new BlockProfiler instance for profiling goroutine blocking events.
// The resulting BlockProfiler uses runtime.BlockProfile as its data source.
//
// Usage:
//
//	bp := godeltaprof.NewBlockProfiler()
//	...
//	err := bp.Profile(someWriter)
func NewBlockProfiler() *BlockProfiler {
	return &BlockProfiler{
		runtimeProfile: runtime.BlockProfile,
		scaleProfile:   pprof.ScalerBlockProfile,
		impl:           pprof.DeltaMutexProfiler{},
		options: pprof.ProfileBuilderOptions{
			GenericsFrames: true,
			LazyMapping:    true,
		},
	}
}

func NewBlockProfilerWithOptions(options ProfileOptions) *BlockProfiler {
	return &BlockProfiler{
		runtimeProfile: runtime.BlockProfile,
		scaleProfile:   pprof.ScalerBlockProfile,
		impl:           pprof.DeltaMutexProfiler{},
		options: pprof.ProfileBuilderOptions{
			GenericsFrames: options.GenericsFrames,
			LazyMapping:    options.LazyMappings,
		},
	}
}

func (d *BlockProfiler) Profile(w io.Writer) error {
	d.mutex.Lock()
	defer d.mutex.Unlock()

	var p []runtime.BlockProfileRecord
	var ok bool
	n, _ := d.runtimeProfile(nil)
	for {
		p = make([]runtime.BlockProfileRecord, n+50)
		n, ok = d.runtimeProfile(p)
		if ok {
			p = p[:n]

			break
		}
	}

	sort.Slice(p, func(i, j int) bool { return p[i].Cycles > p[j].Cycles })

	zw := d.gz.get(w)
	stc := pprof.MutexProfileConfig()
	b := pprof.NewProfileBuilder(w, zw, &d.options, stc)

	return d.impl.PrintCountCycleProfile(b, d.scaleProfile, p)
}
```

## File: `godeltaprof/go.mod`
```
module github.com/grafana/pyroscope-go/godeltaprof

go 1.18

require github.com/klauspost/compress v1.17.8
```

## File: `godeltaprof/go.sum`
```
github.com/klauspost/compress v1.17.8 h1:YcnTYrq7MikUT7k0Yb5eceMmALQPYBW/Xltxn0NAMnU=
github.com/klauspost/compress v1.17.8/go.mod h1:Di0epgTjJY877eYKx5yC51cX2A2Vl2ibi7bDH9ttBbw=
```

## File: `godeltaprof/gzip.go`
```go
package godeltaprof

import (
	"io"

	"github.com/klauspost/compress/gzip"
)

type gz struct {
	w *gzip.Writer
}

func (g *gz) get(w io.Writer) *gzip.Writer {
	if g.w == nil {
		zw, _ := gzip.NewWriterLevel(w, gzip.BestSpeed)
		g.w = zw
	}
	g.w.Reset(w)

	return g.w
}
```

## File: `godeltaprof/gzip_test.go`
```go
package godeltaprof

import (
	"bytes"
	"compress/gzip"
	"io"
	"testing"
)

func TestGz(t *testing.T) {
	blobs := [][]byte{
		[]byte("Hello, World! This is the first test blob with some data to compress."),
		[]byte("This is a second blob with different content for compression testing."),
	}

	var g gz
	bufs := make([]bytes.Buffer, 0, len(blobs))

	for i, blob := range blobs {
		var buf bytes.Buffer
		gzw := g.get(&buf)
		if _, err := gzw.Write(blob); err != nil {
			t.Fatalf("Failed to write blob %d: %v", i, err)
		}
		if err := gzw.Close(); err != nil {
			t.Fatalf("Failed to close gzip writer %d: %v", i, err)
		}
		bufs = append(bufs, buf)
	}

	for i, blob := range blobs {
		gzr, err := gzip.NewReader(&bufs[i])
		if err != nil {
			t.Fatalf("Failed to create gzip reader for blob %d: %v", i, err)
		}
		decompressed, err := io.ReadAll(gzr)
		if err != nil {
			if closeErr := gzr.Close(); closeErr != nil {
				t.Errorf("Failed to close gzip reader for blob %d: %v", i, closeErr)
			}
			t.Fatalf("Failed to decompress blob %d: %v", i, err)
		}
		if err := gzr.Close(); err != nil {
			t.Errorf("Failed to close gzip reader for blob %d: %v", i, err)
		}

		if !bytes.Equal(blob, decompressed) {
			t.Errorf("Blob %d mismatch:\nOriginal:     %q\nDecompressed: %q", i, blob, decompressed)
		}

		if bytes.Equal(blob, bufs[i].Bytes()) {
			t.Errorf("Buffer %d should contain compressed data, not original", i)
		}
	}
}
```

## File: `godeltaprof/heap.go`
```go
package godeltaprof

import (
	"io"
	"runtime"
	"sync"

	"github.com/grafana/pyroscope-go/godeltaprof/internal/pprof"
)

// HeapProfiler is a stateful profiler for heap allocations in Go programs.
// It is based on runtime.MemProfile and provides similar functionality to
// pprof.WriteHeapProfile, but with some key differences.
//
// The HeapProfiler tracks the delta of heap allocations since the last
// profile was written, effectively providing a snapshot of the changes
// in heap usage between two points in time. This is in contrast to the
// pprof.WriteHeapProfile function, which accumulates profiling data
// and results in profiles that represent the entire lifetime of the program.
//
// The HeapProfiler is safe for concurrent use, as it serializes access to
// its internal state using a sync.Mutex. This ensures that multiple goroutines
// can call the Profile method without causing any data race issues.
//
// Usage:
//
//	hp := godeltaprof.NewHeapProfiler()
//	...
//	err := hp.Profile(someWriter)
type HeapProfiler struct {
	impl    pprof.DeltaHeapProfiler
	mutex   sync.Mutex
	options pprof.ProfileBuilderOptions
	gz      gz
}

func NewHeapProfiler() *HeapProfiler {
	return &HeapProfiler{
		impl: pprof.DeltaHeapProfiler{},
		options: pprof.ProfileBuilderOptions{
			GenericsFrames: true,
			LazyMapping:    true,
		}}
}

func NewHeapProfilerWithOptions(options ProfileOptions) *HeapProfiler {
	return &HeapProfiler{
		impl: pprof.DeltaHeapProfiler{},
		options: pprof.ProfileBuilderOptions{
			GenericsFrames: options.GenericsFrames,
			LazyMapping:    options.LazyMappings,
		},
	}
}

func (d *HeapProfiler) Profile(w io.Writer) error {
	d.mutex.Lock()
	defer d.mutex.Unlock()

	// Find out how many records there are (MemProfile(nil, true)),
	// allocate that many records, and get the data.
	// There's a race—more records might be added between
	// the two calls—so allocate a few extra records for safety
	// and also try again if we're very unlucky.
	// The loop should only execute one iteration in the common case.
	var p []runtime.MemProfileRecord
	var ok bool
	n, _ := runtime.MemProfile(nil, true)
	for {
		// Allocate room for a slightly bigger profile,
		// in case a few more entries have been added
		// since the call to MemProfile.
		p = make([]runtime.MemProfileRecord, n+50)
		n, ok = runtime.MemProfile(p, true)
		if ok {
			p = p[0:n]

			break
		}
		// Profile grew; try again.
	}
	rate := int64(runtime.MemProfileRate)

	zw := d.gz.get(w)
	b := pprof.NewProfileBuilder(w, zw, &d.options, pprof.HeapProfileConfig(rate))

	return d.impl.WriteHeapProto(b, p, rate)
}
```

## File: `godeltaprof/heap_test.go`
```go
package godeltaprof

import (
	"bytes"
	"testing"
)

func BenchmarkHeap(b *testing.B) {
	p := NewHeapProfiler()
	buf := bytes.NewBuffer(nil)
	for i := 0; i < b.N; i++ {
		err := p.Profile(buf)
		if err != nil {
			b.Fatal(err)
		}
	}
}
```

## File: `godeltaprof/proto.go`
```go
package godeltaprof

type ProfileOptions struct {
	// for go1.21+ if true - use runtime_FrameSymbolName - produces frames with generic types, for example [go.shape.int]
	// for go1.21+ if false - use runtime.Frame->Function - produces frames with generic types omitted [...]
	// pre 1.21 - always use runtime.Frame->Function - produces frames with generic types omitted [...]
	GenericsFrames bool
	LazyMappings   bool
}
```

## File: `godeltaprof/compat/README.md`
```markdown
This module is separate from the godeltaprof to keep the godeltaprof zero dependencies.
```

## File: `godeltaprof/compat/compression_test.go`
```go
package compat

import (
	"io"
	"runtime"
	"testing"
)

const (
	scalerMutexProfileName = "ScalerMutexProfile"
	scalerBlockProfileName = "ScalerBlockProfile"
)

func BenchmarkHeapCompression(b *testing.B) {
	h := newHeapTestHelper()
	fs := h.generateMemProfileRecords(512, 32)
	h.rng.Seed(239)
	nmutations := int(h.rng.Int63() % int64(len(fs)))

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		if i == 1000 {
			v := h.rng.Int63()
			if v != 7817861117094116717 {
				b.Errorf("unexpected random value: %d. "+
					"The bench should be deterministic for better comparison.", v)
			}
		}
		_ = WriteHeapProto(h.dp, h.opt, io.Discard, fs, int64(runtime.MemProfileRate))
		h.mutate(nmutations, fs)
	}
}

func BenchmarkMutexCompression(b *testing.B) {
	for i, scaler := range mutexProfileScalers {
		name := scalerMutexProfileName
		if i == 1 {
			name = scalerBlockProfileName
		}
		b.Run(name, func(b *testing.B) {
			prevMutexProfileFraction := runtime.SetMutexProfileFraction(-1)
			runtime.SetMutexProfileFraction(5)
			defer runtime.SetMutexProfileFraction(prevMutexProfileFraction)

			h := newMutexTestHelper()
			h.scaler = scaler
			fs := h.generateBlockProfileRecords(512, 32)
			h.rng.Seed(239)
			nmutations := int(h.rng.Int63() % int64(len(fs)))
			b.ResetTimer()

			for i := 0; i < b.N; i++ {
				if i == 1000 {
					v := h.rng.Int63()
					if v != 7817861117094116717 {
						b.Errorf("unexpected random value: %d. "+
							"The bench should be deterministic for better comparison.", v)
					}
				}
				_ = PrintCountCycleProfile(h.dp, h.opt, io.Discard, scaler, fs)
				h.mutate(nmutations, fs)
			}
		})
	}
}
```

## File: `godeltaprof/compat/delta_test.go`
```go
//nolint:gochecknoglobals,gochecknoglobals
package compat

import (
	"fmt"
	"reflect"
	"runtime"
	"strings"
	"testing"

	gprofile "github.com/google/pprof/profile"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/grafana/pyroscope-go/godeltaprof/internal/pprof"
)

var (
	stack0       = [32]uintptr{}
	stack0Marker string
	stack1       = [32]uintptr{}
	stack1Marker string
	stack2       = [32]uintptr{}
	stack2Marker string
	stack3       = [32]uintptr{}
	stack4       = [32]uintptr{}
)

func init() {
	stack0 = [32]uintptr{
		reflect.ValueOf(assert.Truef).Pointer(),
		reflect.ValueOf(assert.CallerInfo).Pointer(),
	}
	stack1 = [32]uintptr{
		reflect.ValueOf(assert.Condition).Pointer(),
		reflect.ValueOf(assert.Conditionf).Pointer(),
	}
	stack2 = [32]uintptr{
		reflect.ValueOf(runtime.GC).Pointer(),
		reflect.ValueOf(runtime.FuncForPC).Pointer(),
		reflect.ValueOf(TestDeltaBlockProfile).Pointer(),
		reflect.ValueOf(TestDeltaHeap).Pointer(),
	}
	stack3 = [32]uintptr{ // equal , but difference in runtime
		reflect.ValueOf(runtime.GC).Pointer() + 1,
		reflect.ValueOf(runtime.FuncForPC).Pointer(),
		reflect.ValueOf(TestDeltaBlockProfile).Pointer(),
		reflect.ValueOf(TestDeltaHeap).Pointer(),
	}

	stack4 = [32]uintptr{ // equal , but difference in non runtime frame
		reflect.ValueOf(runtime.GC).Pointer(),
		reflect.ValueOf(runtime.FuncForPC).Pointer(),
		reflect.ValueOf(TestDeltaBlockProfile).Pointer() + 1,
		reflect.ValueOf(TestDeltaHeap).Pointer(),
	}
	marker := func(stk []uintptr) string {
		res := []string{}
		for i := range stk {
			f := stk[len(stk)-1-i]
			res = append(res, runtime.FuncForPC(f).Name())
		}

		return strings.Join(res, ";")
	}
	stack0Marker = marker(stack0[:2])
	stack1Marker = marker(stack1[:2])
	stack2Marker = marker(stack2[2:4])
}

func TestDeltaHeap(t *testing.T) {
	// scale 0 0 0
	// scale 1 2 705084
	// scale 2 4 1410169
	// scale 3 6 2115253
	// scale 4 8 2820338
	// scale 5 10 3525422
	// scale 6 12 4230507
	// scale 7 15 4935592
	// scale 8 17 5640676
	// scale 9 19 6345761

	const testMemProfileRate = 524288
	const testObjectSize = 327680

	h := newHeapTestHelper()
	h.rate = testMemProfileRate

	p1 := h.dump(
		h.r(0, 0, 0, 0, stack0),
		h.r(0, 0, 0, 0, stack1),
	)
	expectEmptyProfile(t, p1)

	p2 := h.dump(
		h.r(5, 5*testObjectSize, 0, 0, stack0),
		h.r(3, 3*testObjectSize, 3, 3*testObjectSize, stack1),
	)
	expectStackFrames(t, p2, stack0Marker, 10, 3525422, 10, 3525422)
	expectStackFrames(t, p2, stack1Marker, 6, 2115253, 0, 0)

	for i := 0; i < 3; i++ {
		// if we write same data, stack0 is in use, stack1 should not be present
		p3 := h.dump(
			h.r(5, 5*testObjectSize, 0, 0, stack0),
			h.r(3, 3*testObjectSize, 3, 3*testObjectSize, stack1),
		)
		expectStackFrames(t, p3, stack0Marker, 0, 0, 10, 3525422)
		expectNoStackFrames(t, p3, stack1Marker)
	}

	p4 := h.dump(
		h.r(5, 5*testObjectSize, 5, 5*testObjectSize, stack0),
		h.r(3, 3*testObjectSize, 3, 3*testObjectSize, stack1),
	)
	expectEmptyProfile(t, p4)

	p5 := h.dump(
		h.r(8, 8*testObjectSize, 5, 5*testObjectSize, stack0),
		h.r(3, 3*testObjectSize, 3, 3*testObjectSize, stack1),
	)
	// note, this value depends on scale order, it currently tests the current implementation, but we may change it
	// to alloc objects to be scale(8) - scale(5) = 17-10 = 7
	expectStackFrames(t, p5, stack0Marker, 6, 2115253, 6, 2115253)
	expectNoStackFrames(t, p5, stack1Marker)
}

func TestDeltaBlockProfile(t *testing.T) {
	for i, scaler := range mutexProfileScalers {
		name := scalerMutexProfileName
		if i == 1 {
			name = scalerBlockProfileName
		}
		t.Run(name, func(t *testing.T) {
			prevMutexProfileFraction := runtime.SetMutexProfileFraction(-1)
			runtime.SetMutexProfileFraction(5)
			defer runtime.SetMutexProfileFraction(prevMutexProfileFraction)

			h := newMutexTestHelper()
			h.scaler = scaler

			p1 := h.dump(
				h.r(0, 0, stack0),
				h.r(0, 0, stack1),
			)
			expectEmptyProfile(t, p1)

			const cycles = 42
			p2 := h.dump(
				h.r(239, 239*cycles, stack0),
				h.r(0, 0, stack1),
			)
			count0, nanos0 := h.scale(239, 239*cycles)
			expectStackFrames(t, p2, stack0Marker, count0, nanos0)
			expectNoStackFrames(t, p2, stack1Marker)

			for j := 0; j < 2; j++ {
				p3 := h.dump(
					h.r(239, 239*cycles, stack0),
					h.r(0, 0, stack1),
				)
				expectEmptyProfile(t, p3)
			}

			count1, nanos1 := h.scale(240, 240*cycles)
			p4 := h.dump(
				h.r(240, 240*cycles, stack0),
			)
			expectStackFrames(t, p4, stack0Marker, count1-count0, nanos1-nanos0)
			expectNoStackFrames(t, p4, stack1Marker)
		})
	}
}

func BenchmarkHeapDelta(b *testing.B) {
	h := newHeapTestHelper()
	fs := h.generateMemProfileRecords(512, 32)
	builder := &noopBuilder{}
	h.rng.Seed(239)
	nmutations := int(h.rng.Int63() % int64(len(fs)))

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		if i == 1000 {
			v := h.rng.Int63()
			if v != 7817861117094116717 {
				b.Errorf("unexpected random value: %d. "+
					"The bench should be deterministic for better comparison.", v)
			}
		}
		_ = h.dp.WriteHeapProto(builder, fs, int64(runtime.MemProfileRate))
		h.mutate(nmutations, fs)
	}
}

func BenchmarkMutexDelta(b *testing.B) {
	for i, scaler := range mutexProfileScalers {
		name := scalerMutexProfileName
		if i == 1 {
			name = scalerBlockProfileName
		}
		b.Run(name, func(b *testing.B) {
			prevMutexProfileFraction := runtime.SetMutexProfileFraction(-1)
			runtime.SetMutexProfileFraction(5)
			defer runtime.SetMutexProfileFraction(prevMutexProfileFraction)

			h := newMutexTestHelper()
			h.scaler = scaler
			fs := h.generateBlockProfileRecords(512, 32)
			builder := &noopBuilder{}
			h.rng.Seed(239)
			nmutations := int(h.rng.Int63() % int64(len(fs)))
			b.ResetTimer()

			for i := 0; i < b.N; i++ {
				if i == 1000 {
					v := h.rng.Int63()
					if v != 7817861117094116717 {
						b.Errorf("unexpected random value: %d. "+
							"The bench should be deterministic for better comparison.", v)
					}
				}
				_ = h.dp.PrintCountCycleProfile(builder, scaler, fs)
				h.mutate(nmutations, fs)
			}
		})
	}
}

func TestMutexDuplicates(t *testing.T) {
	prev := runtime.SetMutexProfileFraction(-1)
	runtime.SetMutexProfileFraction(1)
	defer runtime.SetMutexProfileFraction(prev)

	h := newMutexTestHelper()
	const cycles = 42
	p := h.dump(
		h.r(239, 239*cycles, stack0),
		h.r(42, 42*cycles, stack1),
		h.r(7, 7*cycles, stack0),
	)

	expectStackFrames(t, p, stack0Marker, h.scale2(239+7, (239+7)*cycles)...)
	expectStackFrames(t, p, stack1Marker, h.scale2(42, (42)*cycles)...)

	expectPPROFLocations(t, p, fmt.Sprintf("^%s$", stack0Marker), 1, h.scale2(239+7, (239+7)*cycles)...)
	expectPPROFLocations(t, p, fmt.Sprintf("^%s$", stack1Marker), 1, h.scale2(42, 42*cycles)...)

	p = h.dump(
		h.r(239, 239*cycles, stack0),
		h.r(42, 42*cycles, stack1),
		h.r(7, 7*cycles, stack0),
	)
	expectEmptyProfile(t, p)
}

func TestHeapDuplicates(t *testing.T) {
	const testMemProfileRate = 524288
	h := newHeapTestHelper()
	h.rate = testMemProfileRate
	const blockSize = 1024
	const blockSize2 = 2048
	p := h.dump(
		h.r(239, 239*blockSize, 239, 239*blockSize, stack0),
		h.r(3, 3*blockSize2, 3, 3*blockSize2, stack0),
		h.r(42, 42*blockSize, 42, 42*blockSize, stack1),
		h.r(7, 7*blockSize, 7, 7*blockSize, stack0),
		h.r(3, 3*blockSize, 3, 3*blockSize, stack2),
		h.r(5, 5*blockSize, 5, 5*blockSize, stack3),
		h.r(11, 11*blockSize, 11, 11*blockSize, stack4),
	)
	pp, err := gprofile.ParseData(p.Bytes())
	require.NoError(t, err)

	scale := func(c, b int) []int64 {
		c1, b1 := pprof.ScaleHeapSample(int64(c), int64(b), testMemProfileRate)

		return []int64{c1, b1, 0, 0}
	}

	expectPPROFLocations(t, p, fmt.Sprintf("^%s$", stack0Marker), 1, scale(239+7, (239+7)*blockSize)...)
	expectPPROFLocations(t, p, fmt.Sprintf("^%s$", stack1Marker), 1, scale(42, 42*blockSize)...)
	expectPPROFLocations(t, p, fmt.Sprintf("^%s$", stack2Marker), 1, scale(3, 3*blockSize)...)
	expectPPROFLocations(t, p, fmt.Sprintf("^%s$", stack2Marker), 1, scale(5, 5*blockSize)...)
	expectPPROFLocations(t, p, fmt.Sprintf("^%s$", stack2Marker), 1, scale(11, 11*blockSize)...)
	assert.Len(t, pp.Sample, 6)

	p = h.dump(
		h.r(239, 239*blockSize, 239, 239*blockSize, stack0),
		h.r(3, 3*blockSize2, 3, 3*blockSize2, stack0),
		h.r(42, 42*blockSize, 42, 42*blockSize, stack1),
		h.r(7, 7*blockSize, 7, 7*blockSize, stack0),
		h.r(3, 3*blockSize, 3, 3*blockSize, stack2),
		h.r(5, 5*blockSize, 5, 5*blockSize, stack3),
		h.r(11, 11*blockSize, 11, 11*blockSize, stack4),
	)
	expectEmptyProfile(t, p)
}
```

## File: `godeltaprof/compat/generics_go20_test.go`
```go
//go:build go1.18 && !go1.21
// +build go1.18,!go1.21

package compat

import (
	"bytes"
	"runtime"
	"runtime/pprof"
	"sync"
	"testing"
	"time"

	"github.com/grafana/pyroscope-go/godeltaprof"
	"github.com/stretchr/testify/require"
)

func genericAllocFunc[T any](n int) []T {
	return make([]T, n)
}

func genericBlock[T any](n int) {
	for i := 0; i < n; i++ {
		m.Lock()
		time.Sleep(100 * time.Millisecond)
		m.Unlock()
	}
}

func triggerGenericBlock() {
	const iters = 2
	const workers = 10

	wg := sync.WaitGroup{}
	wg.Add(workers)
	for j := 0; j < workers; j++ {
		go func() {
			genericBlock[int](iters)
			wg.Done()
		}()
	}
	wg.Wait()
}

// TestGenerics tests that pre go1.21 we emmit [...] as generics
func TestGenericsShape(t *testing.T) {

	prev := runtime.MemProfileRate
	runtime.MemProfileRate = 1
	runtime.GC()

	defer func() {
		runtime.MemProfileRate = prev
	}()

	_ = genericAllocFunc[int](239)

	runtime.GC()

	const expectedOmmitedShape = "github.com/grafana/pyroscope-go/godeltaprof/compat.TestGenericsShape;github.com/grafana/pyroscope-go/godeltaprof/" +
		"compat.genericAllocFunc\\[\\.\\.\\.\\]$"

	t.Run("go runtime", func(t *testing.T) {
		buffer := bytes.NewBuffer(nil)
		err := pprof.WriteHeapProfile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 1, 2048)
	})

	t.Run("godeltaprof generics enabled by default", func(t *testing.T) {
		profiler := godeltaprof.NewHeapProfiler()
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 1, 2048)
	})

	t.Run("godeltaprof generics disabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewHeapProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: false,
		})
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 1, 2048)
	})

	t.Run("godeltaprof generics enabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewHeapProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: true,
		})
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 1, 2048)
	})
}

func TestBlock(t *testing.T) {
	defer runtime.SetBlockProfileRate(0)

	runtime.SetBlockProfileRate(1) // every block

	triggerGenericBlock()

	const expectedOmmitedShape = "github.com/grafana/pyroscope-go/godeltaprof/compat.triggerGenericBlock.func1;github.com/grafana/pyroscope-go/godeltaprof/" +
		"compat\\.genericBlock\\[\\.\\.\\.\\];sync\\.\\(\\*Mutex\\)\\.Lock"

	t.Run("go runtime", func(t *testing.T) {
		buffer := bytes.NewBuffer(nil)
		err := pprof.Lookup("block").WriteTo(buffer, 0)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 19)
	})

	t.Run("godeltaprof generics enabled by default", func(t *testing.T) {
		profiler := godeltaprof.NewBlockProfiler()
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 19)
	})

	t.Run("godeltaprof generics disabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewBlockProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: false,
		})
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 19)
	})

	t.Run("godeltaprof generics enabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewBlockProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: true,
		})
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 19)
	})
}

func TestMutex(t *testing.T) {
	prev := runtime.SetMutexProfileFraction(-1)
	defer runtime.SetMutexProfileFraction(prev)
	runtime.SetMutexProfileFraction(1)

	triggerGenericBlock()

	const expectedOmmitedShape = "github.com/grafana/pyroscope-go/godeltaprof/compat.triggerGenericBlock.func1;github.com/grafana/pyroscope-go/godeltaprof/" +
		"compat\\.genericBlock\\[\\.\\.\\.\\];sync\\.\\(\\*Mutex\\)\\.Unlock"

	t.Run("go runtime", func(t *testing.T) {
		buffer := bytes.NewBuffer(nil)
		err := pprof.Lookup("mutex").WriteTo(buffer, 0)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 19)
	})

	t.Run("godeltaprof generics enabled by default", func(t *testing.T) {
		profiler := godeltaprof.NewMutexProfiler()
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 19)
	})

	t.Run("godeltaprof generics disabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewMutexProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: false,
		})
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 19)
	})

	t.Run("godeltaprof generics enabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewMutexProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: true,
		})
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 19)
	})
}
```

## File: `godeltaprof/compat/generics_go21_test.go`
```go
//go:build go1.21
// +build go1.21

//nolint:gochecknoglobals,lll
package compat

import (
	"bytes"
	"fmt"
	"io"
	"runtime"
	"runtime/pprof"
	"slices"
	"strings"
	"sync"
	"testing"
	"time"

	"github.com/google/pprof/profile"
	"github.com/stretchr/testify/require"

	"github.com/grafana/pyroscope-go/godeltaprof"
)

func genericAllocFunc[T any](n int) []T {
	return make([]T, n)
}

func genericBlock[T any](n int) {
	for i := 0; i < n; i++ {
		m.Lock()
		time.Sleep(100 * time.Millisecond)
		m.Unlock()
	}
}

func triggerGenericBlock() {
	const iters = 2
	const workers = 10

	wg := sync.WaitGroup{}
	wg.Add(workers)
	for j := 0; j < workers; j++ {
		go func() {
			genericBlock[int](iters)
			wg.Done()
		}()
	}
	wg.Wait()
}

// TestGenerics tests that post go1.21 we emmit [...] as generics by default and [go.shape.int] if enabled
func TestGenericsShape(t *testing.T) {
	var buffer *bytes.Buffer
	var err error

	prev := runtime.MemProfileRate
	runtime.MemProfileRate = 1
	runtime.GC()

	defer func() {
		runtime.MemProfileRate = prev
	}()

	it := genericAllocFunc[int](239)
	escape(it)

	runtime.GC()

	const expectedRealShape = "github.com/grafana/pyroscope-go/godeltaprof/compat.TestGenericsShape;github.com/grafana/pyroscope-go/godeltaprof/compat.genericAllocFunc\\[go\\.shape\\.int\\]$"
	const expectedOmmitedShape = "github.com/grafana/pyroscope-go/godeltaprof/compat.TestGenericsShape;github.com/grafana/pyroscope-go/godeltaprof/compat.genericAllocFunc\\[\\.\\.\\.\\]$"

	t.Run("go runtime", func(t *testing.T) {
		buffer = bytes.NewBuffer(nil)
		err = pprof.WriteHeapProfile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedRealShape, 1, 2048)
	})

	t.Run("godeltaprof generics enabled by default", func(t *testing.T) {
		profiler := godeltaprof.NewHeapProfiler()
		buffer = bytes.NewBuffer(nil)
		err = profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedRealShape, 1, 2048)
	})

	t.Run("godeltaprof generics disabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewHeapProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: false,
		})
		buffer = bytes.NewBuffer(nil)
		err = profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 1, 2048)
	})

	t.Run("godeltaprof generics enabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewHeapProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: true,
		})
		buffer = bytes.NewBuffer(nil)
		err = profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedRealShape, 1, 2048)
	})
}

func TestBlock(t *testing.T) {
	defer runtime.SetBlockProfileRate(0)
	runtime.SetBlockProfileRate(1) // every block

	triggerGenericBlock()

	const expectedOmmitedShape = "github.com/grafana/pyroscope-go/godeltaprof/compat.triggerGenericBlock.func1;github.com/grafana/pyroscope-go/godeltaprof/" +
		"compat\\.genericBlock\\[\\.\\.\\.\\];sync\\.\\(\\*Mutex\\)\\.Lock"

	const expectedRealShape = "github.com/grafana/pyroscope-go/godeltaprof/compat.triggerGenericBlock.func1;github.com/grafana/pyroscope-go/godeltaprof/" +
		"compat\\.genericBlock\\[go\\.shape\\.int];sync\\.\\(\\*Mutex\\)\\.Lock"

	t.Run("go runtime", func(t *testing.T) {
		buffer := bytes.NewBuffer(nil)
		err := pprof.Lookup("block").WriteTo(buffer, 0)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedRealShape, 19)
	})

	t.Run("godeltaprof generics enabled by default", func(t *testing.T) {
		profiler := godeltaprof.NewBlockProfiler()
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedRealShape, 19)
	})

	t.Run("godeltaprof generics disabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewBlockProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: false,
		})
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 19)
	})

	t.Run("godeltaprof generics enabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewBlockProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: true,
		})
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedRealShape, 19)
	})
}

func TestMutex(t *testing.T) {
	prev := runtime.SetMutexProfileFraction(-1)
	defer runtime.SetMutexProfileFraction(prev)
	runtime.SetMutexProfileFraction(1)

	triggerGenericBlock()

	const expectedOmmitedShape = "github.com/grafana/pyroscope-go/godeltaprof/compat.triggerGenericBlock.func1;github.com/grafana/pyroscope-go/godeltaprof/" +
		"compat\\.genericBlock\\[\\.\\.\\.\\];sync\\.\\(\\*Mutex\\)\\.Unlock"

	const expectedRealShape = "github.com/grafana/pyroscope-go/godeltaprof/compat.triggerGenericBlock.func1;github.com/grafana/pyroscope-go/godeltaprof/" +
		"compat\\.genericBlock\\[go\\.shape\\.int];sync\\.\\(\\*Mutex\\)\\.Unlock"

	t.Run("go runtime", func(t *testing.T) {
		buffer := bytes.NewBuffer(nil)
		err := pprof.Lookup("mutex").WriteTo(buffer, 0)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedRealShape, 19)
	})

	t.Run("godeltaprof generics enabled by default", func(t *testing.T) {
		profiler := godeltaprof.NewMutexProfiler()
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedRealShape, 19)
	})

	t.Run("godeltaprof generics disabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewMutexProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: false,
		})
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedOmmitedShape, 19)
	})

	t.Run("godeltaprof generics enabled explicitly", func(t *testing.T) {
		profiler := godeltaprof.NewMutexProfilerWithOptions(godeltaprof.ProfileOptions{
			GenericsFrames: true,
		})
		buffer := bytes.NewBuffer(nil)
		err := profiler.Profile(buffer)
		require.NoError(t, err)
		expectStackFrames(t, buffer, expectedRealShape, 19)
	})
}

func profileToStrings(p *profile.Profile) []string {
	var res = make([]string, 0, len(p.Sample))
	for _, s := range p.Sample {
		res = append(res, sampleToString(s))
	}

	return res
}

func sampleToString(s *profile.Sample) string {
	var funcs []string
	for i := len(s.Location) - 1; i >= 0; i-- {
		loc := s.Location[i]
		funcs = locationToStrings(loc, funcs)
	}

	return fmt.Sprintf("%s %v", strings.Join(funcs, ";"), s.Value)
}

func locationToStrings(loc *profile.Location, funcs []string) []string {
	for j := range loc.Line {
		line := loc.Line[len(loc.Line)-1-j]
		funcs = append(funcs, line.Function.Name)
	}

	return funcs
}

// This is a regression test for https://go.dev/issue/64528 .
func TestGenericsHashKeyInPprofBuilder(t *testing.T) {
	previousRate := runtime.MemProfileRate
	runtime.MemProfileRate = 1
	defer func() {
		runtime.MemProfileRate = previousRate
	}()
	for _, sz := range []int{128, 256} {
		it := genericAllocFunc[uint32](sz / 4)
		escape(it)
	}
	for _, sz := range []int{32, 64} {
		it := genericAllocFunc[uint64](sz / 8)
		escape(it)
	}

	runtime.GC()
	buf := bytes.NewBuffer(nil)
	if err := WriteHeapProfile(buf); err != nil {
		t.Fatalf("writing profile: %v", err)
	}
	p, err := profile.Parse(buf)
	if err != nil {
		t.Fatalf("profile.Parse: %v", err)
	}

	actual := profileToStrings(p)
	expected := []string{
		"testing.tRunner;github.com/grafana/pyroscope-go/godeltaprof/compat.TestGenericsHashKeyInPprofBuilder;github.com/grafana/pyroscope-go/godeltaprof/compat.genericAllocFunc[go.shape.uint32] [1 128 0 0]",
		"testing.tRunner;github.com/grafana/pyroscope-go/godeltaprof/compat.TestGenericsHashKeyInPprofBuilder;github.com/grafana/pyroscope-go/godeltaprof/compat.genericAllocFunc[go.shape.uint32] [1 256 0 0]",
		"testing.tRunner;github.com/grafana/pyroscope-go/godeltaprof/compat.TestGenericsHashKeyInPprofBuilder;github.com/grafana/pyroscope-go/godeltaprof/compat.genericAllocFunc[go.shape.uint64] [1 32 0 0]",
		"testing.tRunner;github.com/grafana/pyroscope-go/godeltaprof/compat.TestGenericsHashKeyInPprofBuilder;github.com/grafana/pyroscope-go/godeltaprof/compat.genericAllocFunc[go.shape.uint64] [1 64 0 0]",
	}

	for _, l := range expected {
		if !slices.Contains(actual, l) {
			t.Errorf("profile = %v\nwant = %v", strings.Join(actual, "\n"), l)
		}
	}
}

type opAlloc struct {
	buf [128]byte //nolint:unused
}

type opCall struct {
}

var sink []byte

func storeAlloc() {
	sink = make([]byte, 16)
}

func nonRecursiveGenericAllocFunction[CurrentOp any, OtherOp any](alloc bool) {
	if alloc {
		storeAlloc()
	} else {
		nonRecursiveGenericAllocFunction[OtherOp, CurrentOp](true)
	}
}

func TestGenericsInlineLocations(t *testing.T) {
	if OptimizationOff() {
		t.Skip("skipping test with optimizations disabled")
	}

	previousRate := runtime.MemProfileRate
	runtime.MemProfileRate = 1
	defer func() {
		runtime.MemProfileRate = previousRate
		sink = nil
	}()

	nonRecursiveGenericAllocFunction[opAlloc, opCall](true)
	nonRecursiveGenericAllocFunction[opCall, opAlloc](false)

	runtime.GC()

	buf := bytes.NewBuffer(nil)
	if err := WriteHeapProfile(buf); err != nil {
		t.Fatalf("writing profile: %v", err)
	}
	p, err := profile.Parse(buf)
	if err != nil {
		t.Fatalf("profile.Parse: %v", err)
	}

	const expectedSample = "testing.tRunner;github.com/grafana/pyroscope-go/godeltaprof/compat.TestGenericsInlineLocations;github.com/grafana/pyroscope-go/godeltaprof/compat.nonRecursiveGenericAllocFunction[go.shape.struct {},go.shape.struct { github.com/grafana/pyroscope-go/godeltaprof/compat.buf [128]uint8 }];github.com/grafana/pyroscope-go/godeltaprof/compat.nonRecursiveGenericAllocFunction[go.shape.struct { github.com/grafana/pyroscope-go/godeltaprof/compat.buf [128]uint8 },go.shape.struct {}];github.com/grafana/pyroscope-go/godeltaprof/compat.storeAlloc [1 16 1 16]"
	const expectedLocation = "github.com/grafana/pyroscope-go/godeltaprof/compat.nonRecursiveGenericAllocFunction[go.shape.struct {},go.shape.struct { github.com/grafana/pyroscope-go/godeltaprof/compat.buf [128]uint8 }];github.com/grafana/pyroscope-go/godeltaprof/compat.nonRecursiveGenericAllocFunction[go.shape.struct { github.com/grafana/pyroscope-go/godeltaprof/compat.buf [128]uint8 },go.shape.struct {}];github.com/grafana/pyroscope-go/godeltaprof/compat.storeAlloc"
	const expectedLocationNewInliner = "github.com/grafana/pyroscope-go/godeltaprof/compat.TestGenericsInlineLocations;" + expectedLocation
	var s *profile.Sample
	for _, sample := range p.Sample {
		if sampleToString(sample) == expectedSample {
			s = sample

			break
		}
	}
	if s == nil {
		t.Fatalf("expected \n%s\ngot\n%s", expectedSample, strings.Join(profileToStrings(p), "\n"))
	}
	loc := s.Location[0]
	actual := strings.Join(locationToStrings(loc, nil), ";")
	if expectedLocation != actual && expectedLocationNewInliner != actual {
		t.Errorf("expected a location with at least 3 functions\n%s\ngot\n%s\n", expectedLocation, actual)
	}
}

func OptimizationOff() bool {
	optimizationMarker := func() uintptr {
		pc, _, _, _ := runtime.Caller(0)

		return pc
	}
	pc := optimizationMarker()
	f := runtime.FuncForPC(runtime.FuncForPC(pc).Entry())

	return f.Name() == "github.com/grafana/pyroscope-go/godeltaprof/compat.OptimizationOff.func1"
}

func WriteHeapProfile(w io.Writer) error {
	runtime.GC()
	dh := godeltaprof.NewHeapProfilerWithOptions(godeltaprof.ProfileOptions{
		GenericsFrames: true,
		LazyMappings:   true,
	})

	return dh.Profile(w)
}

var blackhole []any

// make sure a is on the heap
// https://go-review.googlesource.com/c/go/+/649035
// https://go-review.googlesource.com/c/go/+/653856
func escape(a any) {
	blackhole = append(blackhole, a)
	blackhole[0] = nil
	blackhole = blackhole[:0]
}
```

## File: `godeltaprof/compat/go.mod`
```
module github.com/grafana/pyroscope-go/godeltaprof/compat

go 1.18

require (
	github.com/google/pprof v0.0.0-20231127191134-f3a68a39ae15
	github.com/grafana/pyroscope-go/godeltaprof v0.1.5
	github.com/klauspost/compress v1.17.8
	github.com/stretchr/testify v1.11.1
)

require (
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/kr/pretty v0.3.1 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
```

## File: `godeltaprof/compat/go.sum`
```
github.com/creack/pty v1.1.9/go.mod h1:oKZEueFk5CKHvIhNR5MUki03XCEU+Q6VDXinZuGJ33E=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/google/pprof v0.0.0-20231127191134-f3a68a39ae15 h1:t2sLhFuGXwoomaKLTuoxFfFqqlG1Gp2DpsupXq3UvZ0=
github.com/google/pprof v0.0.0-20231127191134-f3a68a39ae15/go.mod h1:czg5+yv1E0ZGTi6S6vVK1mke0fV+FaUhNGcd6VRS9Ik=
github.com/grafana/pyroscope-go/godeltaprof v0.1.5 h1:gkFVqihFRL1Nro2FCC0u6mW47jclef96Zu8I/ykq+4E=
github.com/grafana/pyroscope-go/godeltaprof v0.1.5/go.mod h1:1HSPtjU8vLG0jE9JrTdzjgFqdJ/VgN7fvxBNq3luJko=
github.com/klauspost/compress v1.17.8 h1:YcnTYrq7MikUT7k0Yb5eceMmALQPYBW/Xltxn0NAMnU=
github.com/klauspost/compress v1.17.8/go.mod h1:Di0epgTjJY877eYKx5yC51cX2A2Vl2ibi7bDH9ttBbw=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/pkg/diff v0.0.0-20210226163009-20ebb0f2a09e/go.mod h1:pJLUxLENpZxwdsKMEsNbx1VGcRFpLqf3715MtcvvzbA=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rogpeppe/go-internal v1.9.0 h1:73kH8U+JUqXU8lRuOHeVHaa/SZPifC7BkcraZVejAe8=
github.com/rogpeppe/go-internal v1.9.0/go.mod h1:WtVeX8xhTBvf0smdhujwtBcq4Qrzq/fJaraNFVN+nFs=
github.com/stretchr/testify v1.11.1 h1:7s2iGBzp5EwR7/aIZr8ao5+dra3wiQyKjjFuvgVKu7U=
github.com/stretchr/testify v1.11.1/go.mod h1:wZwfW3scLgRK+23gO65QZefKpKQRnfz6sD981Nm4B6U=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `godeltaprof/compat/reject_order_test.go`
```go
package compat

import (
	"bytes"
	"io"
	"runtime"
	"testing"

	gprofile "github.com/google/pprof/profile"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/grafana/pyroscope-go/godeltaprof/internal/pprof"
)

func TestHeapReject(t *testing.T) {
	h := newHeapTestHelper()
	fs := h.generateMemProfileRecords(512, 32)
	p1 := bytes.NewBuffer(nil)
	err := WriteHeapProto(h.dp, h.opt, p1, fs, int64(runtime.MemProfileRate))
	require.NoError(t, err)
	p1Size := p1.Len()
	profile, err := gprofile.Parse(p1)
	require.NoError(t, err)
	ls := stackCollapseProfile(profile)
	assert.Len(t, ls, 512)
	assert.Len(t, profile.Location, 141)
	t.Log("p1 size", p1Size)

	p2 := bytes.NewBuffer(nil)
	err = WriteHeapProto(h.dp, h.opt, p2, fs, int64(runtime.MemProfileRate))
	require.NoError(t, err)
	p2Size := p2.Len()
	assert.Less(t, p2Size, 1000)
	profile, err = gprofile.Parse(p2)
	require.NoError(t, err)
	ls = stackCollapseProfile(profile)
	assert.Empty(t, ls)
	assert.Empty(t, profile.Location)
	t.Log("p2 size", p2Size)
}

func BenchmarkHeapRejectOrder(b *testing.B) {
	h := newHeapTestHelper()
	fs := h.generateMemProfileRecords(512, 32)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		err := WriteHeapProto(h.dp, h.opt, io.Discard, fs, int64(runtime.MemProfileRate))
		if err != nil {
			b.Fatal(err)
		}
	}
}

var mutexProfileScalers = []pprof.MutexProfileScaler{ //nolint:gochecknoglobals
	pprof.ScalerMutexProfile,
	pprof.ScalerBlockProfile,
}

func TestMutexReject(t *testing.T) {
	for i, scaler := range mutexProfileScalers {
		name := scalerMutexProfileName
		if i == 1 {
			name = scalerBlockProfileName
		}
		t.Run(name, func(t *testing.T) {
			prevMutexProfileFraction := runtime.SetMutexProfileFraction(-1)
			runtime.SetMutexProfileFraction(5)
			defer runtime.SetMutexProfileFraction(prevMutexProfileFraction)

			h := newMutexTestHelper()
			h.scaler = scaler
			fs := h.generateBlockProfileRecords(512, 32)
			p1 := bytes.NewBuffer(nil)
			err := PrintCountCycleProfile(h.dp, h.opt, p1, scaler, fs)
			require.NoError(t, err)
			profile, err := gprofile.Parse(p1)
			require.NoError(t, err)
			ls := stackCollapseProfile(profile)
			assert.Len(t, ls, 512)
			assert.Len(t, profile.Location, 141)

			p2 := bytes.NewBuffer(nil)
			err = PrintCountCycleProfile(h.dp, h.opt, p2, scaler, fs)
			require.NoError(t, err)
			p2Size := p2.Len()
			assert.Less(t, p2Size, 1000)
			profile, err = gprofile.Parse(p2)
			require.NoError(t, err)
			ls = stackCollapseProfile(profile)
			assert.Empty(t, ls)
			assert.Empty(t, profile.Location)
		})
	}
}

func BenchmarkMutexRejectOrder(b *testing.B) {
	for i, scaler := range mutexProfileScalers {
		name := scalerMutexProfileName
		if i == 1 {
			name = scalerBlockProfileName
		}
		b.Run(name, func(b *testing.B) {
			prevMutexProfileFraction := runtime.SetMutexProfileFraction(-1)
			runtime.SetMutexProfileFraction(5)
			defer runtime.SetMutexProfileFraction(prevMutexProfileFraction)
			h := newMutexTestHelper()
			h.scaler = scaler
			fs := h.generateBlockProfileRecords(512, 32)
			b.ResetTimer()

			for i := 0; i < b.N; i++ {
				err := PrintCountCycleProfile(h.dp, h.opt, io.Discard, scaler, fs)
				if err != nil {
					b.Fatal(err)
				}
			}
		})
	}
}
```

## File: `godeltaprof/compat/scale_test.go`
```go
//nolint:gochecknoglobals,gochecknoglobals,lll
package compat

import (
	"bytes"
	"io"
	"math"
	"runtime"
	"sync"
	"testing"
	"time"

	gprofile "github.com/google/pprof/profile"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/grafana/pyroscope-go/godeltaprof"
)

var m sync.Mutex

func TestScaleMutex(t *testing.T) {
	prev := runtime.SetMutexProfileFraction(-1)
	defer runtime.SetMutexProfileFraction(prev)

	buffer := bytes.NewBuffer(make([]byte, 0, 1024*1024))
	profiler := godeltaprof.NewMutexProfiler()
	err := profiler.Profile(io.Discard)
	require.NoError(t, err)

	const fraction = 5
	const iters = 5000
	const workers = 2
	const expectedCount = workers * iters
	const expectedTime = expectedCount * 1000000
	const e = 0.4

	runtime.SetMutexProfileFraction(fraction)

	wg := sync.WaitGroup{}
	wg.Add(workers)
	for j := 0; j < workers; j++ {
		go func() {
			for i := 0; i < iters; i++ {
				m.Lock()
				time.Sleep(time.Millisecond)
				m.Unlock()
			}
			wg.Done()
		}()
	}
	wg.Wait()

	err = profiler.Profile(buffer)
	require.NoError(t, err)

	profile, err := gprofile.Parse(buffer)
	require.NoError(t, err)

	res := stackCollapseProfile(profile)

	my := findStack(res, "github.com/grafana/pyroscope-go/godeltaprof/compat.TestScaleMutex")
	require.NotNil(t, my)

	assert.Less(t, math.Abs(float64(my.value[0])-float64(expectedCount)), e*float64(expectedCount))
	assert.Less(t, math.Abs(float64(my.value[1])-float64(expectedTime)), e*float64(expectedTime))
}

func TestScaleBlock(t *testing.T) {
	defer runtime.SetBlockProfileRate(0)

	buffer := bytes.NewBuffer(make([]byte, 0, 1024*1024))
	profiler := godeltaprof.NewBlockProfiler()
	err := profiler.Profile(io.Discard)
	require.NoError(t, err)

	const fraction = 5
	const iters = 5000
	const workers = 2
	const expectedCount = workers * iters
	const expectedTime = expectedCount * 1000000

	runtime.SetBlockProfileRate(fraction)

	wg := sync.WaitGroup{}
	wg.Add(workers)
	for j := 0; j < workers; j++ {
		go func() {
			for i := 0; i < iters; i++ {
				m.Lock()
				time.Sleep(time.Millisecond)
				m.Unlock()
			}
			wg.Done()
		}()
	}
	wg.Wait()

	err = profiler.Profile(buffer)
	require.NoError(t, err)

	profile, err := gprofile.Parse(buffer)
	require.NoError(t, err)

	res := stackCollapseProfile(profile)

	my := findStack(res, "github.com/grafana/pyroscope-go/godeltaprof/compat.TestScaleBlock")
	require.NotNil(t, my)

	assert.Less(t, math.Abs(float64(my.value[0])-float64(expectedCount)), 0.4*float64(expectedCount))
	assert.Less(t, math.Abs(float64(my.value[1])-float64(expectedTime)), 0.4*float64(expectedTime))
}

var bufs [][]byte

//go:noinline
func appendBuf(sz int) {
	elems := make([]byte, 0, sz)
	bufs = append(bufs, elems)
}

func TestScaleHeap(t *testing.T) {
	prev := runtime.MemProfileRate
	runtime.MemProfileRate = 0

	const size = 64 * 1024
	const iters = 1024

	bufs = make([][]byte, 0, iters)
	defer func() {
		bufs = nil
		runtime.MemProfileRate = prev
	}()

	buffer := bytes.NewBuffer(make([]byte, 0, 1024*1024))
	profiler := godeltaprof.NewHeapProfiler()
	err := profiler.Profile(io.Discard)
	require.NoError(t, err)

	runtime.MemProfileRate = 1
	for i := 0; i < iters; i++ {
		appendBuf(size)
	}

	time.Sleep(time.Second)
	runtime.GC()
	time.Sleep(time.Second)

	expected := []int64{iters, iters * size, iters, iters * size}
	err = profiler.Profile(buffer)
	require.NoError(t, err)

	profile, err := gprofile.Parse(buffer)
	require.NoError(t, err)

	res := stackCollapseProfile(profile)

	my := findStack(res, "github.com/grafana/pyroscope-go/godeltaprof/compat.TestScaleHeap;github.com/grafana/pyroscope-go/godeltaprof/compat.appendBuf")
	require.NotNil(t, my)

	for i := range my.value {
		assert.Less(t, math.Abs(float64(my.value[i])-float64(expected[i])), 0.1*float64(expected[i]))
	}
}
```

## File: `godeltaprof/compat/stackcollapse.go`
```go
package compat

import (
	"bytes"
	"io"
	"reflect"
	"regexp"
	"sort"
	"strings"
	"testing"

	gprofile "github.com/google/pprof/profile"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

type stack struct {
	funcs []string
	line  string
	value []int64
}

func expectEmptyProfile(t *testing.T, buffer io.Reader) {
	t.Helper()
	profile, err := gprofile.Parse(buffer)
	require.NoError(t, err)
	ls := stackCollapseProfile(profile)
	assert.Empty(t, ls)
}

func expectNoStackFrames(t *testing.T, buffer *bytes.Buffer, sfPattern string) {
	t.Helper()
	profile, err := gprofile.ParseData(buffer.Bytes())
	require.NoError(t, err)
	line := findStack(stackCollapseProfile(profile), sfPattern)
	assert.Nilf(t, line, "stack frame %s found", sfPattern)
}

func expectStackFrames(t *testing.T, buffer *bytes.Buffer, sfPattern string, values ...int64) {
	t.Helper()
	profile, err := gprofile.ParseData(buffer.Bytes())
	require.NoError(t, err)
	line := findStack(stackCollapseProfile(profile), sfPattern)
	assert.NotNilf(t, line, "stack frame %s not found", sfPattern)
	if line != nil {
		for i := range values {
			assert.Equalf(t, values[i], line.value[i], "expected %v got %v", values, line.value)
		}
	}
}

//nolint:unparam
func expectPPROFLocations(t *testing.T, buffer *bytes.Buffer,
	samplePattern string, expectedCount int, expectedValues ...int64) {
	t.Helper()
	profile, err := gprofile.ParseData(buffer.Bytes())
	require.NoError(t, err)
	cnt := 0
	samples := grepSamples(profile, samplePattern)
	for _, s := range samples {
		if reflect.DeepEqual(s.Value, expectedValues) {
			cnt++
		}
	}
	assert.Equalf(t, expectedCount, cnt, "expected samples re: %s\n"+
		"   values: %v\n"+
		"    count:%d\n"+
		"    all samples:%+v\n", samplePattern, expectedValues, expectedCount, samples)
}

func grepSamples(profile *gprofile.Profile, samplePattern string) []*gprofile.Sample {
	rr := regexp.MustCompile(samplePattern)
	var samples = make([]*gprofile.Sample, 0, len(profile.Sample))
	for i := range profile.Sample {
		ss := pprofSampleStackToString(profile.Sample[i])
		if !rr.MatchString(ss) {
			continue
		}
		samples = append(samples, profile.Sample[i])
	}

	return samples
}

func findStack(res []stack, re string) *stack {
	rr := regexp.MustCompile(re)
	for i, re := range res {
		if rr.MatchString(re.line) {
			return &res[i]
		}
	}

	return nil
}

func stackCollapseProfile(p *gprofile.Profile) []stack {
	var ret = make([]stack, 0, len(p.Sample))
	for _, s := range p.Sample {
		funcs, strSample := pprofSampleStackToStrings(s)
		ret = append(ret, stack{
			line:  strSample,
			funcs: funcs,
			value: s.Value,
		})
	}
	sort.Slice(ret, func(i, j int) bool {
		return strings.Compare(ret[i].line, ret[j].line) < 0
	})
	var unique = make([]stack, 0, len(ret))
	for _, s := range ret {
		if len(unique) == 0 {
			unique = append(unique, s)

			continue
		}
		if unique[len(unique)-1].line == s.line {
			for i := 0; i < len(s.value); i++ {
				unique[len(unique)-1].value[i] += s.value[i]
			}

			continue
		}
		unique = append(unique, s)
	}

	return unique
}

func pprofSampleStackToString(s *gprofile.Sample) string {
	_, v := pprofSampleStackToStrings(s)

	return v
}

func pprofSampleStackToStrings(s *gprofile.Sample) ([]string, string) {
	var funcs []string
	for i := range s.Location {
		loc := s.Location[i]
		for _, line := range loc.Line {
			f := line.Function
			// funcs = append(funcs, fmt.Sprintf("%s:%d", f.Name, line.Line))
			funcs = append(funcs, f.Name)
		}
	}
	for i := 0; i < len(funcs)/2; i++ {
		j := len(funcs) - i - 1
		funcs[i], funcs[j] = funcs[j], funcs[i]
	}

	strSample := strings.Join(funcs, ";")

	return funcs, strSample
}
```

## File: `godeltaprof/compat/stub_go20_test.go`
```go
//go:build go1.16 && !go1.21
// +build go1.16,!go1.21

package compat

//nolint:lll
import "testing"

func TestRuntimeFrameSymbolName(t *testing.T) {
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_FrameSymbolName",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_FrameSymbolName(f *runtime.Frame) string")
}

func TestRuntimeFrameStartLine(t *testing.T) {
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_FrameStartLine",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_FrameStartLine(f *runtime.Frame) int")
}

func TestRuntimeExpandFinalInlineFrame(t *testing.T) {
	checkSignature(t, "runtime/pprof",
		"runtime_expandFinalInlineFrame",
		"func runtime/pprof.runtime_expandFinalInlineFrame(stk []uintptr) []uintptr")
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_expandFinalInlineFrame",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_expandFinalInlineFrame(stk []uintptr) []uintptr")
}

func TestRuntimeCyclesPerSecond(t *testing.T) {
	checkSignature(t, "runtime/pprof",
		"runtime_cyclesPerSecond",
		"func runtime/pprof.runtime_cyclesPerSecond() int64")
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_cyclesPerSecond",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_cyclesPerSecond() int64")
}
```

## File: `godeltaprof/compat/stub_go22_test.go`
```go
//go:build go1.21 && !go1.23
// +build go1.21,!go1.23

//nolint:lll
package compat

import (
	"testing"
)

func TestRuntimeFrameSymbolName(t *testing.T) {
	checkSignature(t, "runtime/pprof",
		"runtime_FrameSymbolName",
		"func runtime/pprof.runtime_FrameSymbolName(f *runtime.Frame) string")
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_FrameSymbolName",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_FrameSymbolName(f *runtime.Frame) string")
}

func TestRuntimeFrameStartLine(t *testing.T) {
	checkSignature(t, "runtime/pprof",
		"runtime_FrameStartLine",
		"func runtime/pprof.runtime_FrameStartLine(f *runtime.Frame) int")
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_FrameStartLine",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_FrameStartLine(f *runtime.Frame) int")
}

func TestRuntimeExpandFinalInlineFrame(t *testing.T) {
	checkSignature(t, "runtime/pprof",
		"runtime_expandFinalInlineFrame",
		"func runtime/pprof.runtime_expandFinalInlineFrame(stk []uintptr) []uintptr")
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_expandFinalInlineFrame",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_expandFinalInlineFrame(stk []uintptr) []uintptr")
}

func TestRuntimeCyclesPerSecond(t *testing.T) {
	checkSignature(t, "runtime/pprof",
		"runtime_cyclesPerSecond",
		"func runtime/pprof.runtime_cyclesPerSecond() int64")
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_cyclesPerSecond",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_cyclesPerSecond() int64")
}
```

## File: `godeltaprof/compat/stub_go23_test.go`
```go
//go:build go1.23
// +build go1.23

//nolint:lll
package compat

import "testing"

func TestRuntimeFrameSymbolName(t *testing.T) {
	checkSignature(t, "runtime/pprof",
		"runtime_FrameSymbolName",
		"func runtime/pprof.runtime_FrameSymbolName(f *runtime.Frame) string")
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_FrameSymbolName",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_FrameSymbolName(f *runtime.Frame) string")
}

func TestRuntimeFrameStartLine(t *testing.T) {
	checkSignature(t, "runtime/pprof",
		"runtime_FrameStartLine",
		"func runtime/pprof.runtime_FrameStartLine(f *runtime.Frame) int")
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_FrameStartLine",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_FrameStartLine(f *runtime.Frame) int")
}

func TestRuntimeExpandFinalInlineFrame(t *testing.T) {
	checkSignature(t, "runtime/pprof",
		"runtime_expandFinalInlineFrame",
		"func runtime/pprof.runtime_expandFinalInlineFrame(stk []uintptr) []uintptr")
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_expandFinalInlineFrame",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_expandFinalInlineFrame(stk []uintptr) []uintptr")
}

func TestRuntimeCyclesPerSecond(t *testing.T) {
	checkSignature(t, "runtime",
		"pprof_cyclesPerSecond",
		"func runtime.pprof_cyclesPerSecond() int64")
	checkSignature(t, "runtime/pprof",
		"pprof_cyclesPerSecond",
		"func runtime/pprof.pprof_cyclesPerSecond() int64")
	checkSignature(t, "github.com/grafana/pyroscope-go/godeltaprof/internal/pprof",
		"runtime_cyclesPerSecond",
		"func github.com/grafana/pyroscope-go/godeltaprof/internal/pprof.runtime_cyclesPerSecond() int64")
}
```

## File: `godeltaprof/compat/stub_test.go`
```go
package compat

import (
	"encoding/json"
	"errors"
	"fmt"
	"go/ast"
	"go/importer"
	"go/parser"
	"go/token"
	"go/types"
	"io"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

var errNoExportFile = errors.New("no export file")

//nolint:gochecknoglobals // cache shared across test helpers
var exportFileCache = make(map[string]string)

func goListExport(pkg string) (string, error) {
	if v, ok := exportFileCache[pkg]; ok {
		return v, nil
	}
	out, err := exec.Command("go", "list", "-export", "-f", "{{.Export}}", pkg).Output()
	if err != nil {
		return "", fmt.Errorf("go list -export %s: %w", pkg, err)
	}
	path := strings.TrimSpace(string(out))
	if path == "" {
		return "", fmt.Errorf("%s: %w", pkg, errNoExportFile)
	}
	exportFileCache[pkg] = path

	return path, nil
}

type goListJSON struct {
	Dir     string   `json:"Dir"`
	GoFiles []string `json:"GoFiles"`
}

func checkSignature(t *testing.T, pkg string, name string, expectedSignature string) {
	t.Helper()

	// Use go list -json to find source files for the package.
	// We need source (not just export data) because the functions
	// we're checking are unexported.
	out, err := exec.Command("go", "list", "-json", pkg).Output()
	require.NoError(t, err, "go list -json failed for %s", pkg)

	var pkgInfo goListJSON
	require.NoError(t, json.Unmarshal(out, &pkgInfo))

	fset := token.NewFileSet()
	files := make([]*ast.File, 0, len(pkgInfo.GoFiles))
	for _, fname := range pkgInfo.GoFiles {
		f, err := parser.ParseFile(fset, filepath.Join(pkgInfo.Dir, fname), nil, 0)
		require.NoError(t, err)
		files = append(files, f)
	}

	// Type-check the package from source.
	// Dependencies are loaded from export data via go list -export.
	conf := types.Config{
		Importer: importer.ForCompiler(fset, "gc", func(path string) (io.ReadCloser, error) {
			exportFile, err := goListExport(path)
			if err != nil {
				return nil, err
			}

			return os.Open(exportFile) //nolint:gosec // export file path from go list is trusted
		}),
	}
	p, err := conf.Check(pkg, fset, files, nil)
	require.NoError(t, err, "type-check failed for %s", pkg)

	f := p.Scope().Lookup(name)
	require.NotNilf(t, f, "function %s not found in %s", name, pkg)
	ff, ok := f.(*types.Func)
	require.True(t, ok)
	assert.Equal(t, expectedSignature, ff.String())
}
```

## File: `godeltaprof/compat/testdata.go`
```go
package compat

import (
	"bytes"
	"io"
	"math/rand"
	"reflect"
	"runtime"

	"github.com/klauspost/compress/gzip"
	"github.com/stretchr/testify/assert"

	"github.com/grafana/pyroscope-go/godeltaprof/internal/pprof"
)

func getFunctionPointers() []uintptr {
	return []uintptr{
		reflect.ValueOf(assert.Truef).Pointer(),
		reflect.ValueOf(assert.CallerInfo).Pointer(),
		reflect.ValueOf(assert.Condition).Pointer(),
		reflect.ValueOf(assert.Conditionf).Pointer(),
		reflect.ValueOf(assert.Contains).Pointer(),
		reflect.ValueOf(assert.Containsf).Pointer(),
		reflect.ValueOf(assert.DirExists).Pointer(),
		reflect.ValueOf(assert.DirExistsf).Pointer(),
		reflect.ValueOf(assert.ElementsMatch).Pointer(),
		reflect.ValueOf(assert.ElementsMatchf).Pointer(),
		reflect.ValueOf(assert.Empty).Pointer(),
		reflect.ValueOf(assert.Emptyf).Pointer(),
		reflect.ValueOf(assert.Equal).Pointer(),
		reflect.ValueOf(assert.EqualError).Pointer(),
		reflect.ValueOf(assert.EqualErrorf).Pointer(),
		reflect.ValueOf(assert.EqualValues).Pointer(),
		reflect.ValueOf(assert.EqualValuesf).Pointer(),
		reflect.ValueOf(assert.Equalf).Pointer(),
		reflect.ValueOf(assert.Error).Pointer(),
		reflect.ValueOf(assert.ErrorAs).Pointer(),
		reflect.ValueOf(assert.ErrorAsf).Pointer(),
		reflect.ValueOf(assert.ErrorIs).Pointer(),
		reflect.ValueOf(assert.ErrorIsf).Pointer(),
		reflect.ValueOf(assert.Errorf).Pointer(),
		reflect.ValueOf(assert.Eventually).Pointer(),
		reflect.ValueOf(assert.Eventuallyf).Pointer(),
		reflect.ValueOf(assert.Exactly).Pointer(),
		reflect.ValueOf(assert.Exactlyf).Pointer(),
		reflect.ValueOf(assert.Fail).Pointer(),
		reflect.ValueOf(assert.FailNow).Pointer(),
		reflect.ValueOf(assert.FailNowf).Pointer(),
		reflect.ValueOf(assert.Failf).Pointer(),
		reflect.ValueOf(assert.False).Pointer(),
		reflect.ValueOf(assert.Falsef).Pointer(),
		reflect.ValueOf(assert.FileExists).Pointer(),
		reflect.ValueOf(assert.FileExistsf).Pointer(),
		reflect.ValueOf(assert.Greater).Pointer(),
		reflect.ValueOf(assert.GreaterOrEqual).Pointer(),
		reflect.ValueOf(assert.GreaterOrEqualf).Pointer(),
		reflect.ValueOf(assert.Greaterf).Pointer(),
		reflect.ValueOf(assert.HTTPBody).Pointer(),
		reflect.ValueOf(assert.HTTPBodyContains).Pointer(),
		reflect.ValueOf(assert.HTTPBodyContainsf).Pointer(),
		reflect.ValueOf(assert.HTTPBodyNotContains).Pointer(),
		reflect.ValueOf(assert.HTTPBodyNotContainsf).Pointer(),
		reflect.ValueOf(assert.HTTPError).Pointer(),
		reflect.ValueOf(assert.HTTPErrorf).Pointer(),
		reflect.ValueOf(assert.HTTPRedirect).Pointer(),
		reflect.ValueOf(assert.HTTPRedirectf).Pointer(),
		reflect.ValueOf(assert.HTTPStatusCode).Pointer(),
		reflect.ValueOf(assert.HTTPStatusCodef).Pointer(),
		reflect.ValueOf(assert.HTTPSuccess).Pointer(),
		reflect.ValueOf(assert.HTTPSuccessf).Pointer(),
		reflect.ValueOf(assert.Implements).Pointer(),
		reflect.ValueOf(assert.Implementsf).Pointer(),
		reflect.ValueOf(assert.InDelta).Pointer(),
		reflect.ValueOf(assert.InDeltaMapValues).Pointer(),
		reflect.ValueOf(assert.InDeltaMapValuesf).Pointer(),
		reflect.ValueOf(assert.InDeltaSlice).Pointer(),
		reflect.ValueOf(assert.InDeltaSlicef).Pointer(),
		reflect.ValueOf(assert.InDeltaf).Pointer(),
		reflect.ValueOf(assert.InEpsilon).Pointer(),
		reflect.ValueOf(assert.InEpsilonSlice).Pointer(),
		reflect.ValueOf(assert.InEpsilonSlicef).Pointer(),
		reflect.ValueOf(assert.InEpsilonf).Pointer(),
		reflect.ValueOf(assert.IsDecreasing).Pointer(),
		reflect.ValueOf(assert.IsDecreasingf).Pointer(),
		reflect.ValueOf(assert.IsIncreasing).Pointer(),
		reflect.ValueOf(assert.IsIncreasingf).Pointer(),
		reflect.ValueOf(assert.IsNonDecreasing).Pointer(),
		reflect.ValueOf(assert.IsNonDecreasingf).Pointer(),
		reflect.ValueOf(assert.IsNonIncreasing).Pointer(),
		reflect.ValueOf(assert.IsNonIncreasingf).Pointer(),
		reflect.ValueOf(assert.IsType).Pointer(),
		reflect.ValueOf(assert.IsTypef).Pointer(),
		reflect.ValueOf(assert.JSONEq).Pointer(),
		reflect.ValueOf(assert.JSONEqf).Pointer(),
		reflect.ValueOf(assert.Len).Pointer(),
		reflect.ValueOf(assert.Lenf).Pointer(),
		reflect.ValueOf(assert.Less).Pointer(),
		reflect.ValueOf(assert.LessOrEqual).Pointer(),
		reflect.ValueOf(assert.LessOrEqualf).Pointer(),
		reflect.ValueOf(assert.Lessf).Pointer(),
		reflect.ValueOf(assert.Negative).Pointer(),
		reflect.ValueOf(assert.Negativef).Pointer(),
		reflect.ValueOf(assert.Never).Pointer(),
		reflect.ValueOf(assert.Neverf).Pointer(),
		reflect.ValueOf(assert.New).Pointer(),
		reflect.ValueOf(assert.Nil).Pointer(),
		reflect.ValueOf(assert.Nilf).Pointer(),
		reflect.ValueOf(assert.NoDirExists).Pointer(),
		reflect.ValueOf(assert.NoDirExistsf).Pointer(),
		reflect.ValueOf(assert.NoError).Pointer(),
		reflect.ValueOf(assert.NoErrorf).Pointer(),
		reflect.ValueOf(assert.NoFileExists).Pointer(),
		reflect.ValueOf(assert.NoFileExistsf).Pointer(),
		reflect.ValueOf(assert.NotContains).Pointer(),
		reflect.ValueOf(assert.NotContainsf).Pointer(),
		reflect.ValueOf(assert.NotEmpty).Pointer(),
		reflect.ValueOf(assert.NotEmptyf).Pointer(),
		reflect.ValueOf(assert.NotEqual).Pointer(),
		reflect.ValueOf(assert.NotEqualValues).Pointer(),
		reflect.ValueOf(assert.NotEqualValuesf).Pointer(),
		reflect.ValueOf(assert.NotEqualf).Pointer(),
		reflect.ValueOf(assert.NotErrorIs).Pointer(),
		reflect.ValueOf(assert.NotErrorIsf).Pointer(),
		reflect.ValueOf(assert.NotNil).Pointer(),
		reflect.ValueOf(assert.NotNilf).Pointer(),
		reflect.ValueOf(assert.NotPanics).Pointer(),
		reflect.ValueOf(assert.NotPanicsf).Pointer(),
		reflect.ValueOf(assert.NotRegexp).Pointer(),
		reflect.ValueOf(assert.NotRegexpf).Pointer(),
		reflect.ValueOf(assert.NotSame).Pointer(),
		reflect.ValueOf(assert.NotSamef).Pointer(),
		reflect.ValueOf(assert.NotSubset).Pointer(),
		reflect.ValueOf(assert.NotSubsetf).Pointer(),
		reflect.ValueOf(assert.NotZero).Pointer(),
		reflect.ValueOf(assert.NotZerof).Pointer(),
		reflect.ValueOf(assert.ObjectsAreEqual).Pointer(),
		reflect.ValueOf(assert.ObjectsAreEqualValues).Pointer(),
		reflect.ValueOf(assert.Panics).Pointer(),
		reflect.ValueOf(assert.PanicsWithError).Pointer(),
		reflect.ValueOf(assert.PanicsWithErrorf).Pointer(),
		reflect.ValueOf(assert.PanicsWithValue).Pointer(),
		reflect.ValueOf(assert.PanicsWithValuef).Pointer(),
		reflect.ValueOf(assert.Panicsf).Pointer(),
		reflect.ValueOf(assert.Positive).Pointer(),
		reflect.ValueOf(assert.Positivef).Pointer(),
		reflect.ValueOf(assert.Regexp).Pointer(),
		reflect.ValueOf(assert.Regexpf).Pointer(),
		reflect.ValueOf(assert.Same).Pointer(),
		reflect.ValueOf(assert.Samef).Pointer(),
		reflect.ValueOf(assert.Subset).Pointer(),
		reflect.ValueOf(assert.Subsetf).Pointer(),
		reflect.ValueOf(assert.True).Pointer(),
		reflect.ValueOf(assert.Truef).Pointer(),
		reflect.ValueOf(assert.WithinDuration).Pointer(),
		reflect.ValueOf(assert.WithinDurationf).Pointer(),
		reflect.ValueOf(assert.YAMLEq).Pointer(),
		reflect.ValueOf(assert.YAMLEqf).Pointer(),
		reflect.ValueOf(assert.Zero).Pointer(),
		reflect.ValueOf(assert.Zerof).Pointer(),
	}
}

//nolint:unparam
func (h *heapTestHelper) generateMemProfileRecords(n, depth int) []runtime.MemProfileRecord {
	var records []runtime.MemProfileRecord

	fs := getFunctionPointers()
	for i := 0; i < n; i++ {
		nobj := int(uint64(h.rng.Int63())) % 1000000 //nolint:gosec
		r := runtime.MemProfileRecord{
			AllocObjects: int64(nobj),
			AllocBytes:   int64(nobj * 1024),
			FreeObjects:  int64(nobj), // pretend inuse is zero
			FreeBytes:    int64(nobj * 1024),
		}
		for j := 0; j < depth; j++ {
			r.Stack0[j] = fs[int(uint64(h.rng.Int63()))%len(fs)] //nolint:gosec
		}
		records = append(records, r)
	}

	return records
}

//nolint:unparam
func (h *mutexTestHelper) generateBlockProfileRecords(n, depth int) []runtime.BlockProfileRecord {
	var records []runtime.BlockProfileRecord
	fs := getFunctionPointers()
	for i := 0; i < n; i++ {
		nobj := int(uint64(h.rng.Int63())) % 1000000 //nolint:gosec
		r := runtime.BlockProfileRecord{
			Count:  int64(nobj),
			Cycles: int64(nobj * 10),
		}
		for j := 0; j < depth; j++ {
			r.Stack0[j] = fs[int(uint64(h.rng.Int63()))%len(fs)] //nolint:gosec
		}
		records = append(records, r)
	}

	return records
}

type mutexTestHelper struct {
	dp     *pprof.DeltaMutexProfiler
	opt    *pprof.ProfileBuilderOptions
	scaler pprof.MutexProfileScaler
	rng    rand.Source
}

func newMutexTestHelper() *mutexTestHelper {
	res := &mutexTestHelper{
		dp: &pprof.DeltaMutexProfiler{},
		opt: &pprof.ProfileBuilderOptions{
			GenericsFrames: true,
			LazyMapping:    true,
		},
		scaler: pprof.ScalerMutexProfile,
		rng:    rand.NewSource(239),
	}

	return res
}

func (h *mutexTestHelper) scale(rcount, rcycles int64) (int64, int64) {
	cpuGHz := float64(pprof.Runtime_cyclesPerSecond()) / 1e9
	count, nanosec := pprof.ScaleMutexProfile(h.scaler, rcount, float64(rcycles)/cpuGHz)
	inanosec := int64(nanosec)

	return count, inanosec
}

func (h *mutexTestHelper) scale2(rcount, rcycles int64) []int64 {
	c, n := h.scale(rcount, rcycles)

	return []int64{c, n}
}

func (h *mutexTestHelper) dump(r ...runtime.BlockProfileRecord) *bytes.Buffer {
	buf := bytes.NewBuffer(nil)
	err := PrintCountCycleProfile(h.dp, h.opt, buf, h.scaler, r)
	if err != nil { // never happens
		panic(err)
	}

	return buf
}

func (h *mutexTestHelper) r(count, cycles int64, s [32]uintptr) runtime.BlockProfileRecord {
	return runtime.BlockProfileRecord{
		Count:  count,
		Cycles: cycles,
		StackRecord: runtime.StackRecord{
			Stack0: s,
		},
	}
}

func (h *mutexTestHelper) mutate(nmutations int, fs []runtime.BlockProfileRecord) {
	oneBlockCycles := fs[0].Cycles / fs[0].Count
	for j := 0; j < nmutations; j++ {
		idx := int(uint(h.rng.Int63())) % len(fs) //nolint:gosec
		fs[idx].Count += 1
		fs[idx].Cycles += oneBlockCycles
	}
}

type heapTestHelper struct {
	dp   *pprof.DeltaHeapProfiler
	opt  *pprof.ProfileBuilderOptions
	rate int64
	rng  rand.Source
}

func newHeapTestHelper() *heapTestHelper {
	res := &heapTestHelper{
		dp: &pprof.DeltaHeapProfiler{},
		opt: &pprof.ProfileBuilderOptions{
			GenericsFrames: true,
			LazyMapping:    true,
		},
		rng:  rand.NewSource(239),
		rate: int64(runtime.MemProfileRate),
	}

	return res
}

func (h *heapTestHelper) dump(r ...runtime.MemProfileRecord) *bytes.Buffer {
	buf := bytes.NewBuffer(nil)
	err := WriteHeapProto(h.dp, h.opt, buf, r, h.rate)
	if err != nil { // never happens
		panic(err)
	}

	return buf
}

func (h *heapTestHelper) r(allocObjects, allocBytes, freeObjects, freeBytes int64,
	s [32]uintptr) runtime.MemProfileRecord {
	return runtime.MemProfileRecord{
		AllocObjects: allocObjects,
		AllocBytes:   allocBytes,
		FreeBytes:    freeBytes,
		FreeObjects:  freeObjects,
		Stack0:       s,
	}
}

func (h *heapTestHelper) mutate(nmutations int, fs []runtime.MemProfileRecord) {
	objSize := fs[0].AllocBytes / fs[0].AllocObjects
	for j := 0; j < nmutations; j++ {
		idx := int(uint(h.rng.Int63())) % len(fs) //nolint:gosec
		fs[idx].AllocObjects += 1
		fs[idx].AllocBytes += objSize
		fs[idx].FreeObjects += 1
		fs[idx].FreeBytes += objSize
	}
}

func WriteHeapProto(dp *pprof.DeltaHeapProfiler, opt *pprof.ProfileBuilderOptions, w io.Writer,
	p []runtime.MemProfileRecord, rate int64) error {
	stc := pprof.HeapProfileConfig(rate)
	zw, _ := gzip.NewWriterLevel(w, gzip.BestSpeed)
	b := pprof.NewProfileBuilder(w, zw, opt, stc)

	return dp.WriteHeapProto(b, p, rate)
}

func PrintCountCycleProfile(d *pprof.DeltaMutexProfiler, opt *pprof.ProfileBuilderOptions, w io.Writer,
	scaler pprof.MutexProfileScaler, records []runtime.BlockProfileRecord) error {
	stc := pprof.MutexProfileConfig()
	zw, _ := gzip.NewWriterLevel(w, gzip.BestSpeed)
	b := pprof.NewProfileBuilder(w, zw, opt, stc)

	return d.PrintCountCycleProfile(b, scaler, records)
}

type noopBuilder struct {
}

func (b *noopBuilder) LocsForStack(_ []uintptr) []uint64 {
	return nil
}

func (b *noopBuilder) Sample(_ []int64, _ []uint64, _ int64) {

}

func (b *noopBuilder) Build() {

}
```

## File: `godeltaprof/example/main.go`
```go
package main

import (
	"bytes"
	"fmt"
	"net/http"
	_ "net/http/pprof" //nolint:gosec
	"runtime"
	"sync"
	"time"

	"github.com/grafana/pyroscope-go/godeltaprof"
	_ "github.com/grafana/pyroscope-go/godeltaprof/http/pprof"
)

//go:noinline
func work(n int) {
	// revive:disable:empty-block this is fine because this is a example app, not real production code
	for i := 0; i < n; i++ {
	}
	fmt.Printf("work\n") //nolint:forbidigo
	// revive:enable:empty-block
}

var m sync.Mutex //nolint:gochecknoglobals

func fastFunction(wg *sync.WaitGroup) {
	m.Lock()
	defer m.Unlock()

	work(200000000)

	wg.Done()
}

func slowFunction(wg *sync.WaitGroup) {
	m.Lock()
	defer m.Unlock()

	work(800000000)
	wg.Done()
}

func main() {
	go func() {
		err := http.ListenAndServe("localhost:6060", http.DefaultServeMux) //nolint:gosec
		if err != nil {
			panic(err)
		}
	}()
	go func() {
		deltaHeapProfiler := godeltaprof.NewHeapProfiler()
		deltaBlockProfiler := godeltaprof.NewBlockProfiler()
		deltaMutexProfiler := godeltaprof.NewMutexProfiler()
		for {
			time.Sleep(10 * time.Second)
			_ = deltaHeapProfiler.Profile(bytes.NewBuffer(nil))
			_ = deltaBlockProfiler.Profile(bytes.NewBuffer(nil))
			_ = deltaMutexProfiler.Profile(bytes.NewBuffer(nil))
		}
	}()
	runtime.SetMutexProfileFraction(5)
	runtime.SetBlockProfileRate(5)

	for {
		wg := sync.WaitGroup{}
		wg.Add(2)
		go fastFunction(&wg)
		go slowFunction(&wg)
		wg.Wait()
	}
}
```

## File: `godeltaprof/http/pprof/pprof.go`
```go
package pprof

import (
	"fmt"
	"io"
	"net/http"
	"runtime"
	"strconv"

	"github.com/grafana/pyroscope-go/godeltaprof"
)

var (
	deltaHeapProfiler  = godeltaprof.NewHeapProfiler()  //nolint:gochecknoglobals
	deltaBlockProfiler = godeltaprof.NewBlockProfiler() //nolint:gochecknoglobals
	deltaMutexProfiler = godeltaprof.NewMutexProfiler() //nolint:gochecknoglobals
)

type deltaProfiler interface {
	Profile(w io.Writer) error
}

func init() {
	prefix := routePrefix()
	http.HandleFunc(prefix+"/debug/pprof/delta_heap", Heap)
	http.HandleFunc(prefix+"/debug/pprof/delta_block", Block)
	http.HandleFunc(prefix+"/debug/pprof/delta_mutex", Mutex)
}

func Heap(w http.ResponseWriter, r *http.Request) {
	gc, _ := strconv.Atoi(r.FormValue("gc"))
	if gc > 0 {
		runtime.GC()
	}
	writeDeltaProfile(deltaHeapProfiler, "heap", w)
}

func Block(w http.ResponseWriter, r *http.Request) {
	writeDeltaProfile(deltaBlockProfiler, "block", w)
}

func Mutex(w http.ResponseWriter, r *http.Request) {
	writeDeltaProfile(deltaMutexProfiler, "mutex", w)
}

func writeDeltaProfile(p deltaProfiler, name string, w http.ResponseWriter) {
	w.Header().Set("X-Content-Type-Options", "nosniff")
	w.Header().Set("Content-Type", "application/octet-stream")
	w.Header().Set("Content-Disposition", fmt.Sprintf(`attachment; filename="%s.pprof.gz"`, name))
	_ = p.Profile(w)
}
```

## File: `godeltaprof/http/pprof/pprof_go21.go`
```go
//go:build !go1.22

package pprof

func routePrefix() string {
	return ""
}
```

## File: `godeltaprof/http/pprof/pprof_go22.go`
```go
//go:build go1.22

package pprof

func routePrefix() string {
	// As of go 1.23 we will panic if we don't prefix with "GET "
	// https://github.com/golang/go/blob/9fcffc53593c5cd103630d0d24ef8bd91e17246d/src/net/http/pprof/pprof.go#L98-L97
	// https://github.com/golang/go/commit/9fcffc53593c5cd103630d0d24ef8bd91e17246d
	return "GET "
}
```

## File: `godeltaprof/internal/pprof/builder.go`
```go
package pprof

type ProfileBuilder interface {
	LocsForStack(stk []uintptr) (newLocs []uint64)
	Sample(values []int64, locs []uint64, blockSize int64)
	Build()
}

type ProfileConfig struct {
	PeriodType        ValueType
	Period            int64
	SampleType        []ValueType
	DefaultSampleType string
}

type ValueType struct {
	Typ, Unit string
}
```

## File: `godeltaprof/internal/pprof/delta_heap.go`
```go
package pprof

import (
	"math"
	"runtime"
	"strings"
)

type heapPrevValue struct {
	allocObjects int64
}

type heapAccValue struct {
	allocObjects int64
	inuseObjects int64
}

type DeltaHeapProfiler struct {
	m profMap[heapPrevValue, heapAccValue]
	// todo consider adding an option to remove block size label and merge allocations of different size
}

// WriteHeapProto writes the current heap profile in protobuf format to w.
//
//nolint:gocognit
func (d *DeltaHeapProfiler) WriteHeapProto(b ProfileBuilder, p []runtime.MemProfileRecord, rate int64) error {
	values := []int64{0, 0, 0, 0}
	var locs []uint64
	// deduplicate: accumulate allocObjects and inuseObjects in entry.acc for equal stacks
	for i := range p {
		r := &p[i]
		if r.AllocBytes == 0 && r.AllocObjects == 0 && r.FreeObjects == 0 && r.FreeBytes == 0 {
			// it is a fresh bucket and it will be published after next 1-2 gc cycles
			continue
		}
		var blockSize int64
		if r.AllocObjects > 0 {
			blockSize = r.AllocBytes / r.AllocObjects
		}
		entry := d.m.Lookup(r.Stack(), uintptr(blockSize))
		entry.acc.allocObjects += r.AllocObjects
		entry.acc.inuseObjects += r.InUseObjects()
	}
	// do the delta using the accumulated values and previous values
	for i := range p {
		r := &p[i]
		if r.AllocBytes == 0 && r.AllocObjects == 0 && r.FreeObjects == 0 && r.FreeBytes == 0 {
			// it is a fresh bucket and it will be published after next 1-2 gc cycles
			continue
		}
		var blockSize int64
		if r.AllocObjects > 0 {
			blockSize = r.AllocBytes / r.AllocObjects
		}
		entry := d.m.Lookup(r.Stack(), uintptr(blockSize))
		if entry.acc == (heapAccValue{}) {
			continue
		}

		allocObjects := entry.acc.allocObjects - entry.prev.allocObjects
		if allocObjects < 0 {
			continue
		}

		// allocBytes, inuseBytes is calculated as multiplication of number of objects by blockSize
		// This is done to reduce the size of the map entry (i.e. heapAccValue for deduplication and
		// heapPrevValue for keeping the delta).

		allocBytes := allocObjects * blockSize
		entry.prev.allocObjects = entry.acc.allocObjects
		inuseBytes := entry.acc.inuseObjects * blockSize

		values[0], values[1] = ScaleHeapSample(allocObjects, allocBytes, rate)
		values[2], values[3] = ScaleHeapSample(entry.acc.inuseObjects, inuseBytes, rate)

		entry.acc = heapAccValue{}

		if values[0] == 0 && values[1] == 0 && values[2] == 0 && values[3] == 0 {
			continue
		}

		hideRuntime := true
		for tries := 0; tries < 2; tries++ {
			stk := r.Stack()
			// For heap profiles, all stack
			// addresses are return PCs, which is
			// what appendLocsForStack expects.
			if hideRuntime {
				for i, addr := range stk {
					if f := runtime.FuncForPC(addr); f != nil && strings.HasPrefix(f.Name(), "runtime.") {
						continue
					}
					// Found non-runtime. Show any runtime uses above it.
					stk = stk[i:]

					break
				}
			}
			locs = b.LocsForStack(stk)
			if len(locs) > 0 {
				break
			}
			hideRuntime = false // try again, and show all frames next time.
		}

		b.Sample(values, locs, blockSize)
	}
	b.Build()

	return nil
}

// ScaleHeapSample adjusts the data from a heap Sample to
// account for its probability of appearing in the collected
// data. heap profiles are a sampling of the memory allocations
// requests in a program. We estimate the unsampled value by dividing
// each collected sample by its probability of appearing in the
// profile. heap profiles rely on a poisson process to determine
// which samples to collect, based on the desired average collection
// rate R. The probability of a sample of size S to appear in that
// profile is 1-exp(-S/R).
func ScaleHeapSample(count, size, rate int64) (int64, int64) {
	if count == 0 || size == 0 {
		return 0, 0
	}

	if rate <= 1 {
		// if rate==1 all samples were collected so no adjustment is needed.
		// if rate<1 treat as unknown and skip scaling.
		return count, size
	}

	avgSize := float64(size) / float64(count)
	scale := 1 / (1 - math.Exp(-avgSize/float64(rate)))

	return int64(float64(count) * scale), int64(float64(size) * scale)
}

func HeapProfileConfig(rate int64) ProfileConfig {
	return ProfileConfig{
		PeriodType: ValueType{Typ: "space", Unit: "bytes"},
		Period:     rate,
		SampleType: []ValueType{
			{"alloc_objects", "count"},
			{"alloc_space", "bytes"},
			{"inuse_objects", "count"},
			{"inuse_space", "bytes"},
		},
		DefaultSampleType: "",
	}
}
```

## File: `godeltaprof/internal/pprof/delta_mutex.go`
```go
package pprof

import (
	"runtime"
)

type mutexPrevValue struct {
	count    int64
	inanosec int64
}

type mutexAccValue struct {
	count  int64
	cycles int64
}

type DeltaMutexProfiler struct {
	m profMap[mutexPrevValue, mutexAccValue]
}

// PrintCountCycleProfile outputs block profile records (for block or mutex profiles)
// as the pprof-proto format output. Translations from cycle count to time duration
// are done because The proto expects count and time (nanoseconds) instead of count
// and the number of cycles for block, contention profiles.
// Possible 'scaler' functions are scaleBlockProfile and scaleMutexProfile.
func (d *DeltaMutexProfiler) PrintCountCycleProfile(b ProfileBuilder, scaler MutexProfileScaler,
	records []runtime.BlockProfileRecord) error {
	cpuGHz := float64(runtime_cyclesPerSecond()) / 1e9

	values := []int64{0, 0}
	var locs []uint64
	// deduplicate: accumulate count and cycles in entry.acc for equal stacks
	for i := range records {
		r := &records[i]
		entry := d.m.Lookup(r.Stack(), 0)
		entry.acc.count += r.Count // accumulate unscaled
		entry.acc.cycles += r.Cycles
	}

	// do the delta using the accumulated values and previous values
	for i := range records {
		r := &records[i]
		stk := r.Stack()
		entry := d.m.Lookup(stk, 0)
		accCount := entry.acc.count
		accCycles := entry.acc.cycles
		if accCount == 0 && accCycles == 0 {
			continue
		}
		entry.acc = mutexAccValue{}
		count, nanosec := ScaleMutexProfile(scaler, accCount, float64(accCycles)/cpuGHz)
		inanosec := int64(nanosec)

		// do the delta
		values[0] = count - entry.prev.count
		values[1] = inanosec - entry.prev.inanosec
		entry.prev.count = count
		entry.prev.inanosec = inanosec

		if values[0] < 0 || values[1] < 0 {
			continue
		}
		if values[0] == 0 && values[1] == 0 {
			continue
		}

		// For count profiles, all stack addresses are
		// return PCs, which is what appendLocsForStack expects.
		locs = b.LocsForStack(stk)
		b.Sample(values, locs, 0)
	}
	b.Build()

	return nil
}

func MutexProfileConfig() ProfileConfig {
	return ProfileConfig{
		PeriodType: ValueType{"contentions", "count"},
		Period:     1,
		SampleType: []ValueType{
			{"contentions", "count"},
			{"delay", "nanoseconds"},
		},
	}
}
```

## File: `godeltaprof/internal/pprof/elf.go`
```go
// Copyright 2017 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package pprof

import (
	"encoding/binary"
	"encoding/hex"
	"errors"
	"os"
)

var (
	errBadELF    = errors.New("malformed ELF binary")
	errNoBuildID = errors.New("no NT_GNU_BUILD_ID found in ELF binary")
)

// elfBuildID returns the GNU build ID of the named ELF binary,
// without introducing a dependency on debug/elf and its dependencies.
//
//nolint:gocognit
func elfBuildID(file string) (string, error) {
	buf := make([]byte, 256)
	f, err := os.Open(file) //nolint:gosec
	if err != nil {
		return "", err
	}
	defer func() {
		_ = f.Close()
	}()

	if _, err := f.ReadAt(buf[:64], 0); err != nil {
		return "", err
	}

	// ELF file begins with \x7F E L F.
	if buf[0] != 0x7F || buf[1] != 'E' || buf[2] != 'L' || buf[3] != 'F' {
		return "", errBadELF
	}

	var byteOrder binary.ByteOrder
	switch buf[5] {
	default:
		return "", errBadELF
	case 1: // little-endian
		byteOrder = binary.LittleEndian
	case 2: // big-endian
		byteOrder = binary.BigEndian
	}

	var shnum int
	var shoff, shentsize int64
	switch buf[4] {
	default:
		return "", errBadELF
	case 1: // 32-bit file header
		shoff = int64(byteOrder.Uint32(buf[32:]))
		shentsize = int64(byteOrder.Uint16(buf[46:]))
		if shentsize != 40 {
			return "", errBadELF
		}
		shnum = int(byteOrder.Uint16(buf[48:]))
	case 2: // 64-bit file header
		shoff = int64(byteOrder.Uint64(buf[40:])) //nolint:gosec
		shentsize = int64(byteOrder.Uint16(buf[58:]))
		if shentsize != 64 {
			return "", errBadELF
		}
		shnum = int(byteOrder.Uint16(buf[60:]))
	}

	for i := 0; i < shnum; i++ {
		if _, err := f.ReadAt(buf[:shentsize], shoff+int64(i)*shentsize); err != nil {
			return "", err
		}
		if typ := byteOrder.Uint32(buf[4:]); typ != 7 { // SHT_NOTE
			continue
		}
		var off, size int64
		if shentsize == 40 {
			// 32-bit section header
			off = int64(byteOrder.Uint32(buf[16:]))
			size = int64(byteOrder.Uint32(buf[20:]))
		} else {
			// 64-bit section header
			off = int64(byteOrder.Uint64(buf[24:]))  //nolint:gosec
			size = int64(byteOrder.Uint64(buf[32:])) //nolint:gosec
		}
		size += off
		for off < size {
			if _, err := f.ReadAt(buf[:16], off); err != nil { // room for header + name GNU\x00
				return "", err
			}
			nameSize := int(byteOrder.Uint32(buf[0:]))
			descSize := int(byteOrder.Uint32(buf[4:]))
			noteType := int(byteOrder.Uint32(buf[8:]))
			descOff := off + int64(12+(nameSize+3)&^3)
			off = descOff + int64((descSize+3)&^3)
			if nameSize != 4 || noteType != 3 || buf[12] != 'G' || buf[13] != 'N' || buf[14] != 'U' || buf[15] != '\x00' { //nolint:lll    // want name GNU\x00 type 3 (NT_GNU_BUILD_ID)
				continue
			}
			if descSize > len(buf) {
				return "", errBadELF
			}
			if _, err := f.ReadAt(buf[:descSize], descOff); err != nil {
				return "", err
			}

			return hex.EncodeToString(buf[:descSize]), nil
		}
	}

	return "", errNoBuildID
}
```

## File: `godeltaprof/internal/pprof/map.go`
```go
// Copyright 2017 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package pprof

import "unsafe"

// A profMap is a map from (stack, tag) to mapEntry.
// It grows without bound, but that's assumed to be OK.
type profMap[PREV any, ACC any] struct {
	hash    map[uintptr]*profMapEntry[PREV, ACC]
	free    []profMapEntry[PREV, ACC]
	freeStk []uintptr
}

// A profMapEntry is a single entry in the profMap.
// todo use unsafe.Pointer + len for stk ?
type profMapEntry[PREV any, ACC any] struct {
	nextHash *profMapEntry[PREV, ACC] // next in hash list
	stk      []uintptr
	tag      uintptr
	prev     PREV
	acc      ACC
}

func (m *profMap[PREV, ACC]) Lookup(stk []uintptr, tag uintptr) *profMapEntry[PREV, ACC] {
	// Compute hash of (stk, tag).
	h := uintptr(0)
	for _, x := range stk {
		h = h<<8 | (h >> (8 * (unsafe.Sizeof(h) - 1)))
		h += x * 41
	}
	h = h<<8 | (h >> (8 * (unsafe.Sizeof(h) - 1)))
	h += tag * 41

	// Find entry if present.
	var last *profMapEntry[PREV, ACC]
Search:
	for e := m.hash[h]; e != nil; last, e = e, e.nextHash {
		if len(e.stk) != len(stk) || e.tag != tag {
			continue
		}
		for j := range stk {
			if e.stk[j] != stk[j] {
				continue Search
			}
		}
		// Move to the front.
		if last != nil {
			last.nextHash = e.nextHash
			e.nextHash = m.hash[h]
			m.hash[h] = e
		}

		return e
	}

	// Add a new entry.
	if len(m.free) < 1 {
		m.free = make([]profMapEntry[PREV, ACC], 128)
	}
	e := &m.free[0]
	m.free = m.free[1:]
	e.nextHash = m.hash[h]
	e.tag = tag

	if len(m.freeStk) < len(stk) {
		m.freeStk = make([]uintptr, 1024)
	}
	// Limit cap to prevent append from clobbering freeStk.
	e.stk = m.freeStk[:len(stk):len(stk)]
	m.freeStk = m.freeStk[len(stk):]

	copy(e.stk, stk)
	if m.hash == nil {
		m.hash = make(map[uintptr]*profMapEntry[PREV, ACC])
	}
	m.hash[h] = e

	return e
}
```

## File: `godeltaprof/internal/pprof/mutex_scale_go19.go`
```go
//go:build go1.16 && !go1.20
// +build go1.16,!go1.20

package pprof

import "runtime"

type MutexProfileScaler struct {
	f func(cnt int64, ns float64) (int64, float64)
}

func ScaleMutexProfile(scaler MutexProfileScaler, cnt int64, ns float64) (int64, float64) {
	return scaler.f(cnt, ns)
}

var ScalerMutexProfile = MutexProfileScaler{func(cnt int64, ns float64) (int64, float64) {
	period := runtime.SetMutexProfileFraction(-1)
	return cnt * int64(period), ns * float64(period)
}}

var ScalerBlockProfile = MutexProfileScaler{func(cnt int64, ns float64) (int64, float64) {
	// Do nothing.
	// The current way of block profile sampling makes it
	// hard to compute the unsampled number. The legacy block
	// profile parse doesn't attempt to scale or unsample.
	return cnt, ns
}}
```

## File: `godeltaprof/internal/pprof/mutex_scale_go20.go`
```go
//go:build go1.20
// +build go1.20

package pprof

type MutexProfileScaler struct {
}

// ScaleMutexProfile is a no-op for go1.20+.
// https://github.com/golang/go/commit/30b1af00ff142a3f1a5e2a0f32cf04a649bd5e65
func ScaleMutexProfile(_ MutexProfileScaler, cnt int64, ns float64) (int64, float64) {
	return cnt, ns
}

var ScalerMutexProfile = MutexProfileScaler{} //nolint:gochecknoglobals

var ScalerBlockProfile = MutexProfileScaler{} //nolint:gochecknoglobals
```

## File: `godeltaprof/internal/pprof/proto.go`
```go
// Copyright 2016 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package pprof

import (
	"bytes"
	"io"
	"os"
	"runtime"
	"strconv"
	"strings"
	"time"

	"github.com/klauspost/compress/gzip"
)

type ProfileBuilderOptions struct {
	// for go1.21+ if true - use runtime_FrameSymbolName - produces frames with generic types, for example [go.shape.int]
	// for go1.21+ if false - use runtime.Frame->Function - produces frames with generic types omitted [...]
	// pre 1.21 - always use runtime.Frame->Function - produces frames with generic types omitted [...]
	GenericsFrames bool
	LazyMapping    bool
	mem            []memMap
}

func (d *ProfileBuilderOptions) mapping() []memMap {
	if d.mem == nil || !d.LazyMapping {
		d.mem = readMapping()
	}

	return d.mem
}

// A profileBuilder writes a profile incrementally from a
// stream of profile samples delivered by the runtime.
type profileBuilder struct {
	start      time.Time
	end        time.Time
	havePeriod bool
	period     int64

	// encoding state
	w         io.Writer
	zw        *gzip.Writer
	pb        protobuf
	strings   []string
	stringMap map[string]int
	locs      map[uintptr]locInfo // list of locInfo starting with the given PC.
	funcs     map[string]int      // Package path-qualified function name to Function.ID
	mem       []memMap
	deck      pcDeck
	tmplocs   []uint64

	opt *ProfileBuilderOptions
}

type memMap struct {
	// initialized as reading mapping
	start   uintptr // Address at which the binary (or DLL) is loaded into memory.
	end     uintptr // The limit of the address range occupied by this mapping.
	offset  uint64  // Offset in the binary that corresponds to the first mapped address.
	file    string  // The object this entry is loaded from.
	buildID string  // A string that uniquely identifies a particular program version with high probability.

	funcs symbolizeFlag
	fake  bool // map entry was faked; /proc/self/maps wasn't available
}

// symbolizeFlag keeps track of symbolization result.
//
//	0                  : no symbol lookup was performed
//	1<<0 (lookupTried) : symbol lookup was performed
//	1<<1 (lookupFailed): symbol lookup was performed but failed
type symbolizeFlag uint8

const (
	lookupTried  symbolizeFlag = 1 << iota
	lookupFailed symbolizeFlag = 1 << iota
)

const (
	// message Profile
	tagProfile_SampleType        = 1  // repeated ValueType
	tagProfile_Sample            = 2  // repeated Sample
	tagProfile_Mapping           = 3  // repeated Mapping
	tagProfile_Location          = 4  // repeated Location
	tagProfile_Function          = 5  // repeated Function
	tagProfile_StringTable       = 6  // repeated string
	tagProfile_DropFrames        = 7  // int64 (string table index)
	tagProfile_KeepFrames        = 8  // int64 (string table index)
	tagProfile_TimeNanos         = 9  // int64
	tagProfile_DurationNanos     = 10 // int64
	tagProfile_PeriodType        = 11 // ValueType (really optional string???)
	tagProfile_Period            = 12 // int64
	tagProfile_Comment           = 13 // repeated int64
	tagProfile_DefaultSampleType = 14 // int64

	// message ValueType
	tagValueType_Type = 1 // int64 (string table index)
	tagValueType_Unit = 2 // int64 (string table index)

	// message Sample
	tagSample_Location = 1 // repeated uint64
	tagSample_Value    = 2 // repeated int64
	tagSample_Label    = 3 // repeated Label

	// message Label
	tagLabel_Key = 1 // int64 (string table index)
	tagLabel_Str = 2 // int64 (string table index)
	tagLabel_Num = 3 // int64

	// message Mapping
	tagMapping_ID              = 1  // uint64
	tagMapping_Start           = 2  // uint64
	tagMapping_Limit           = 3  // uint64
	tagMapping_Offset          = 4  // uint64
	tagMapping_Filename        = 5  // int64 (string table index)
	tagMapping_BuildID         = 6  // int64 (string table index)
	tagMapping_HasFunctions    = 7  // bool
	tagMapping_HasFilenames    = 8  // bool
	tagMapping_HasLineNumbers  = 9  // bool
	tagMapping_HasInlineFrames = 10 // bool

	// message Location
	tagLocation_ID        = 1 // uint64
	tagLocation_MappingID = 2 // uint64
	tagLocation_Address   = 3 // uint64
	tagLocation_Line      = 4 // repeated Line

	// message Line
	tagLine_FunctionID = 1 // uint64
	tagLine_Line       = 2 // int64

	// message Function
	tagFunction_ID         = 1 // uint64
	tagFunction_Name       = 2 // int64 (string table index)
	tagFunction_SystemName = 3 // int64 (string table index)
	tagFunction_Filename   = 4 // int64 (string table index)
	tagFunction_StartLine  = 5 // int64
)

// stringIndex adds s to the string table if not already present
// and returns the index of s in the string table.
func (b *profileBuilder) stringIndex(s string) int64 {
	id, ok := b.stringMap[s]
	if !ok {
		id = len(b.strings)
		b.strings = append(b.strings, s)
		b.stringMap[s] = id
	}

	return int64(id)
}

func (b *profileBuilder) flush() {
	const dataFlush = 4096
	if b.pb.nest == 0 && len(b.pb.data) > dataFlush {
		_, _ = b.zw.Write(b.pb.data)
		b.pb.data = b.pb.data[:0]
	}
}

// pbValueType encodes a ValueType message to b.pb.
func (b *profileBuilder) pbValueType(tag int, typ, unit string) {
	start := b.pb.startMessage()
	b.pb.int64(tagValueType_Type, b.stringIndex(typ))
	b.pb.int64(tagValueType_Unit, b.stringIndex(unit))
	b.pb.endMessage(tag, start)
}

// Sample encodes a Sample message to b.pb.
func (b *profileBuilder) Sample(values []int64, locs []uint64, blockSize int64) {
	start := b.pb.startMessage()
	b.pb.int64s(tagSample_Value, values)
	b.pb.uint64s(tagSample_Location, locs)
	if blockSize != 0 {
		b.pbLabel(tagSample_Label, "bytes", "", blockSize)
	}
	b.pb.endMessage(tagProfile_Sample, start)
	b.flush()
}

// pbLabel encodes a Label message to b.pb.
func (b *profileBuilder) pbLabel(tag int, key, str string, num int64) {
	start := b.pb.startMessage()
	b.pb.int64Opt(tagLabel_Key, b.stringIndex(key))
	b.pb.int64Opt(tagLabel_Str, b.stringIndex(str))
	b.pb.int64Opt(tagLabel_Num, num)
	b.pb.endMessage(tag, start)
}

// pbLine encodes a Line message to b.pb.
func (b *profileBuilder) pbLine(tag int, funcID uint64, line int64) {
	start := b.pb.startMessage()
	b.pb.uint64Opt(tagLine_FunctionID, funcID)
	b.pb.int64Opt(tagLine_Line, line)
	b.pb.endMessage(tag, start)
}

// pbMapping encodes a Mapping message to b.pb.
func (b *profileBuilder) pbMapping(tag int, id, base, limit, offset uint64, file, buildID string, hasFuncs bool) {
	start := b.pb.startMessage()
	b.pb.uint64Opt(tagMapping_ID, id)
	b.pb.uint64Opt(tagMapping_Start, base)
	b.pb.uint64Opt(tagMapping_Limit, limit)
	b.pb.uint64Opt(tagMapping_Offset, offset)
	b.pb.int64Opt(tagMapping_Filename, b.stringIndex(file))
	b.pb.int64Opt(tagMapping_BuildID, b.stringIndex(buildID))
	// TODO: we set HasFunctions if all symbols from samples were symbolized (hasFuncs).
	// Decide what to do about HasInlineFrames and HasLineNumbers.
	// Also, another approach to handle the mapping entry with
	// incomplete symbolization results is to dupliace the mapping
	// entry (but with different Has* fields values) and use
	// different entries for symbolized locations and unsymbolized locations.
	if hasFuncs {
		b.pb.bool(tagMapping_HasFunctions, true)
	}
	b.pb.endMessage(tag, start)
}

func allFrames(addr uintptr) ([]runtime.Frame, symbolizeFlag) {
	// Expand this one address using CallersFrames so we can cache
	// each expansion. In general, CallersFrames takes a whole
	// stack, but in this case we know there will be no skips in
	// the stack and we have return PCs anyway.
	frames := runtime.CallersFrames([]uintptr{addr})
	frame, more := frames.Next()
	if frame.Function == "runtime.goexit" {
		// Short-circuit if we see runtime.goexit so the loop
		// below doesn't allocate a useless empty location.
		return nil, 0
	}

	symbolizeResult := lookupTried
	if frame.PC == 0 || frame.Function == "" || frame.File == "" || frame.Line == 0 {
		symbolizeResult |= lookupFailed
	}

	if frame.PC == 0 {
		// If we failed to resolve the frame, at least make up
		// a reasonable call PC. This mostly happens in tests.
		frame.PC = addr - 1
	}
	ret := []runtime.Frame{frame}
	for frame.Function != "runtime.goexit" && more {
		frame, more = frames.Next()
		ret = append(ret, frame)
	}

	return ret, symbolizeResult
}

type locInfo struct {
	// location id assigned by the profileBuilder
	id uint64

	// sequence of PCs, including the fake PCs returned by the traceback
	// to represent inlined functions
	// https://github.com/golang/go/blob/d6f2f833c93a41ec1c68e49804b8387a06b131c5/src/runtime/traceback.go#L347-L368
	pcs []uintptr

	// firstPCFrames and firstPCSymbolizeResult hold the results of the
	// allFrames call for the first (leaf-most) PC this locInfo represents
	firstPCFrames          []runtime.Frame
	firstPCSymbolizeResult symbolizeFlag
}

// NewProfileBuilder returns a new profileBuilder.
// CPU profiling data obtained from the runtime can be added
// by calling b.addCPUData, and then the eventual profile
// can be obtained by calling b.finish.
func NewProfileBuilder(w io.Writer, zw *gzip.Writer, opt *ProfileBuilderOptions, stc ProfileConfig) ProfileBuilder {
	b := &profileBuilder{
		w:         w,
		zw:        zw,
		start:     time.Now(),
		strings:   []string{""},
		stringMap: map[string]int{"": 0},
		locs:      map[uintptr]locInfo{},
		funcs:     map[string]int{},
		opt:       opt,
		tmplocs:   make([]uint64, 0, 128),
	}
	b.mem = opt.mapping()
	b.pbValueType(tagProfile_PeriodType, stc.PeriodType.Typ, stc.PeriodType.Unit)
	b.pb.int64Opt(tagProfile_Period, stc.Period)
	for _, st := range stc.SampleType {
		b.pbValueType(tagProfile_SampleType, st.Typ, st.Unit)
	}
	if stc.DefaultSampleType != "" {
		b.pb.int64Opt(tagProfile_DefaultSampleType, b.stringIndex(stc.DefaultSampleType))
	}

	return b
}

// Build completes and returns the constructed profile.
func (b *profileBuilder) Build() {
	b.end = time.Now()

	b.pb.int64Opt(tagProfile_TimeNanos, b.start.UnixNano())
	if b.havePeriod { // must be CPU profile
		b.pbValueType(tagProfile_SampleType, "samples", "count")
		b.pbValueType(tagProfile_SampleType, "cpu", "nanoseconds")
		b.pb.int64Opt(tagProfile_DurationNanos, b.end.Sub(b.start).Nanoseconds())
		b.pbValueType(tagProfile_PeriodType, "cpu", "nanoseconds")
		b.pb.int64Opt(tagProfile_Period, b.period)
	}

	for i, m := range b.mem {
		hasFunctions := m.funcs == lookupTried                                                                                  //nolint:lll    // lookupTried but not lookupFailed
		b.pbMapping(tagProfile_Mapping, uint64(i+1), uint64(m.start), uint64(m.end), m.offset, m.file, m.buildID, hasFunctions) //nolint:lll,gosec
	}

	// TODO: Anything for tagProfile_DropFrames?
	// TODO: Anything for tagProfile_KeepFrames?

	b.pb.strings(tagProfile_StringTable, b.strings)
	_, _ = b.zw.Write(b.pb.data)
	_ = b.zw.Close()
}

// LocsForStack appends the location IDs for the given stack trace to the given
// location ID slice, locs. The addresses in the stack are return PCs or 1 + the PC of
// an inline marker as the runtime traceback function returns.
//
// It may return an empty slice even if locs is non-empty, for example if locs consists
// solely of runtime.goexit. We still count these empty stacks in profiles in order to
// get the right cumulative sample count.
//
// It may emit to b.pb, so there must be no message encoding in progress.
func (b *profileBuilder) LocsForStack(stk []uintptr) (newLocs []uint64) {
	locs := b.tmplocs[:0]
	b.deck.reset()

	// The last frame might be truncated. Recover lost inline frames.
	stk = runtime_expandFinalInlineFrame(stk)

	for len(stk) > 0 {
		addr := stk[0]
		if l, ok := b.locs[addr]; ok {
			// When generating code for an inlined function, the compiler adds
			// NOP instructions to the outermost function as a placeholder for
			// each layer of inlining. When the runtime generates tracebacks for
			// stacks that include inlined functions, it uses the addresses of
			// those NOPs as "fake" PCs on the stack as if they were regular
			// function call sites. But if a profiling signal arrives while the
			// CPU is executing one of those NOPs, its PC will show up as a leaf
			// in the profile with its own Location entry. So, always check
			// whether addr is a "fake" PC in the context of the current call
			// stack by trying to add it to the inlining deck before assuming
			// that the deck is complete.
			if len(b.deck.pcs) > 0 {
				if added := b.deck.tryAdd(addr, l.firstPCFrames, l.firstPCSymbolizeResult); added {
					stk = stk[1:]

					continue
				}
			}

			// first record the location if there is any pending accumulated info.
			if id := b.emitLocation(); id > 0 {
				locs = append(locs, id)
			}

			// then, record the cached location.
			locs = append(locs, l.id)

			// Skip the matching pcs.
			//
			// Even if stk was truncated due to the stack depth
			// limit, expandFinalInlineFrame above has already
			// fixed the truncation, ensuring it is long enough.
			stk = stk[len(l.pcs):]

			continue
		}

		frames, symbolizeResult := allFrames(addr)
		if len(frames) == 0 { // runtime.goexit.
			if id := b.emitLocation(); id > 0 {
				locs = append(locs, id)
			}
			stk = stk[1:]

			continue
		}

		if added := b.deck.tryAdd(addr, frames, symbolizeResult); added {
			stk = stk[1:]

			continue
		}
		// add failed because this addr is not inlined with the
		// existing PCs in the deck. Flush the deck and retry handling
		// this pc.
		if id := b.emitLocation(); id > 0 {
			locs = append(locs, id)
		}

		// check cache again - previous emitLocation added a new entry
		if l, ok := b.locs[addr]; ok {
			locs = append(locs, l.id)
			stk = stk[len(l.pcs):] // skip the matching pcs.
		} else {
			b.deck.tryAdd(addr, frames, symbolizeResult) // must succeed.
			stk = stk[1:]
		}
	}
	if id := b.emitLocation(); id > 0 { // emit remaining location.
		locs = append(locs, id)
	}

	return locs
}

// Here's an example of how Go 1.17 writes out inlined functions, compiled for
// linux/amd64. The disassembly of main.main shows two levels of inlining: main
// calls b, b calls a, a does some work.
//
//   inline.go:9   0x4553ec  90              NOPL                 // func main()    { b(v) }
//   inline.go:6   0x4553ed  90              NOPL                 // func b(v *int) { a(v) }
//   inline.go:5   0x4553ee  48c7002a000000  MOVQ $0x2a, 0(AX)    // func a(v *int) { *v = 42 }
//
// If a profiling signal arrives while executing the MOVQ at 0x4553ee (for line
// 5), the runtime will report the stack as the MOVQ frame being called by the
// NOPL at 0x4553ed (for line 6) being called by the NOPL at 0x4553ec (for line
// 9).
//
// The role of pcDeck is to collapse those three frames back into a single
// location at 0x4553ee, with file/line/function symbolization info representing
// the three layers of calls. It does that via sequential calls to pcDeck.tryAdd
// starting with the leaf-most address. The fourth call to pcDeck.tryAdd will be
// for the caller of main.main. Because main.main was not inlined in its caller,
// the deck will reject the addition, and the fourth PC on the stack will get
// its own location.

// pcDeck is a helper to detect a sequence of inlined functions from
// a stack trace returned by the runtime.
//
// The stack traces returned by runtime's trackback functions are fully
// expanded (at least for Go functions) and include the fake pcs representing
// inlined functions. The profile proto expects the inlined functions to be
// encoded in one Location message.
// https://github.com/google/pprof/blob/5e965273ee43930341d897407202dd5e10e952cb/proto/profile.proto#L177-L184
//
// Runtime does not directly expose whether a frame is for an inlined function
// and looking up debug info is not ideal, so we use a heuristic to filter
// the fake pcs and restore the inlined and entry functions. Inlined functions
// have the following properties:
//
//	Frame's Func is nil (note: also true for non-Go functions), and
//	Frame's Entry matches its entry function frame's Entry (note: could also be true for recursive calls and non-Go
//	functions), and Frame's Name does not match its entry function frame's name (note: inlined functions cannot be
//	directly recursive).
//
// As reading and processing the pcs in a stack trace one by one (from leaf to the root),
// we use pcDeck to temporarily hold the observed pcs and their expanded frames
// until we observe the entry function frame.
type pcDeck struct {
	pcs             []uintptr
	frames          []runtime.Frame
	symbolizeResult symbolizeFlag

	// firstPCFrames indicates the number of frames associated with the first
	// (leaf-most) PC in the deck
	firstPCFrames int
	// firstPCSymbolizeResult holds the results of the allFrames call for the
	// first (leaf-most) PC in the deck
	firstPCSymbolizeResult symbolizeFlag
}

func (d *pcDeck) reset() {
	d.pcs = d.pcs[:0]
	d.frames = d.frames[:0]
	d.symbolizeResult = 0
	d.firstPCFrames = 0
	d.firstPCSymbolizeResult = 0
}

// tryAdd tries to add the pc and Frames expanded from it (most likely one,
// since the stack trace is already fully expanded) and the symbolizeResult
// to the deck. If it fails the caller needs to flush the deck and retry.
func (d *pcDeck) tryAdd(pc uintptr, frames []runtime.Frame, symbolizeResult symbolizeFlag) (success bool) {
	if existing := len(d.frames); existing > 0 {
		// 'd.frames' are all expanded from one 'pc' and represent all
		// inlined functions so we check only the last one.
		newFrame := frames[0]
		last := d.frames[existing-1]
		if last.Func != nil { // the last frame can't be inlined. Flush.
			return false
		}
		if last.Entry == 0 || newFrame.Entry == 0 { // Possibly not a Go function. Don't try to merge.
			return false
		}

		if last.Entry != newFrame.Entry { // newFrame is for a different function.
			return false
		}
		if runtime_FrameSymbolName(&last) == runtime_FrameSymbolName(&newFrame) { // maybe recursion.
			return false
		}
	}
	d.pcs = append(d.pcs, pc)
	d.frames = append(d.frames, frames...)
	d.symbolizeResult |= symbolizeResult
	if len(d.pcs) == 1 {
		d.firstPCFrames = len(d.frames)
		d.firstPCSymbolizeResult = symbolizeResult
	}

	return true
}

// emitLocation emits the new location and function information recorded in the deck
// and returns the location ID encoded in the profile protobuf.
// It emits to b.pb, so there must be no message encoding in progress.
// It resets the deck.
func (b *profileBuilder) emitLocation() uint64 {
	if len(b.deck.pcs) == 0 {
		return 0
	}
	defer b.deck.reset()

	addr := b.deck.pcs[0]
	firstFrame := b.deck.frames[0]

	// We can't write out functions while in the middle of the
	// Location message, so record new functions we encounter and
	// write them out after the Location.
	type newFunc struct {
		id         uint64
		name, file string
		startLine  int64
	}
	newFuncs := make([]newFunc, 0, 8)

	id := uint64(len(b.locs)) + 1
	b.locs[addr] = locInfo{
		id:                     id,
		pcs:                    append([]uintptr{}, b.deck.pcs...),
		firstPCSymbolizeResult: b.deck.firstPCSymbolizeResult,
		firstPCFrames:          append([]runtime.Frame{}, b.deck.frames[:b.deck.firstPCFrames]...),
	}

	start := b.pb.startMessage()
	b.pb.uint64Opt(tagLocation_ID, id)
	b.pb.uint64Opt(tagLocation_Address, uint64(firstFrame.PC))
	for k := range b.deck.frames {
		frame := &b.deck.frames[k]
		// Write out each line in frame expansion.
		funcName := runtime_FrameSymbolName(frame)
		funcID := uint64(b.funcs[funcName]) //nolint:gosec
		if funcID == 0 {
			funcID = uint64(len(b.funcs)) + 1
			b.funcs[funcName] = int(funcID) //nolint:gosec
			var name string
			if b.opt.GenericsFrames {
				name = funcName
			} else {
				name = frame.Function
			}
			newFuncs = append(newFuncs, newFunc{
				id:        funcID,
				name:      name,
				file:      frame.File,
				startLine: int64(runtime_FrameStartLine(frame)),
			})
		}
		b.pbLine(tagLocation_Line, funcID, int64(frame.Line))
	}
	for i := range b.mem {
		if b.mem[i].start <= addr && addr < b.mem[i].end || b.mem[i].fake {
			b.pb.uint64Opt(tagLocation_MappingID, uint64(i+1)) //nolint:gosec

			m := b.mem[i]
			m.funcs |= b.deck.symbolizeResult
			b.mem[i] = m

			break
		}
	}
	b.pb.endMessage(tagProfile_Location, start)

	// Write out functions we found during frame expansion.
	for _, fn := range newFuncs {
		start := b.pb.startMessage()
		b.pb.uint64Opt(tagFunction_ID, fn.id)
		b.pb.int64Opt(tagFunction_Name, b.stringIndex(fn.name))
		b.pb.int64Opt(tagFunction_SystemName, b.stringIndex(fn.name))
		b.pb.int64Opt(tagFunction_Filename, b.stringIndex(fn.file))
		b.pb.int64Opt(tagFunction_StartLine, fn.startLine)
		b.pb.endMessage(tagProfile_Function, start)
	}

	b.flush()

	return id
}

func readMapping() []memMap {
	data, _ := os.ReadFile("/proc/self/maps")
	var mem []memMap
	parseProcSelfMaps(data, func(lo, hi, offset uint64, file, buildID string) {
		mem = append(mem, memMap{
			start:   uintptr(lo),
			end:     uintptr(hi),
			offset:  offset,
			file:    file,
			buildID: buildID,
			fake:    false,
		})
	})
	if len(mem) == 0 { // pprof expects a map entry, so fake one.
		mem = []memMap{{
			start:   uintptr(0),
			end:     uintptr(0),
			offset:  0,
			file:    "",
			buildID: "",
			fake:    true,
		}}
	}

	return mem
}

var space = []byte(" ")    //nolint:gochecknoglobals
var newline = []byte("\n") //nolint:gochecknoglobals

func parseProcSelfMaps(data []byte, addMapping func(lo, hi, offset uint64, file, buildID string)) {
	// $ cat /proc/self/maps
	// 00400000-0040b000 r-xp 00000000 fc:01 787766                             /bin/cat
	// 0060a000-0060b000 r--p 0000a000 fc:01 787766                             /bin/cat
	// 0060b000-0060c000 rw-p 0000b000 fc:01 787766                             /bin/cat
	// 014ab000-014cc000 rw-p 00000000 00:00 0                                  [heap]
	// 7f7d76af8000-7f7d7797c000 r--p 00000000 fc:01 1318064                    /usr/lib/locale/locale-archive
	// 7f7d7797c000-7f7d77b36000 r-xp 00000000 fc:01 1180226                    /lib/x86_64-linux-gnu/libc-2.19.so
	// 7f7d77b36000-7f7d77d36000 ---p 001ba000 fc:01 1180226                    /lib/x86_64-linux-gnu/libc-2.19.so
	// 7f7d77d36000-7f7d77d3a000 r--p 001ba000 fc:01 1180226                    /lib/x86_64-linux-gnu/libc-2.19.so
	// 7f7d77d3a000-7f7d77d3c000 rw-p 001be000 fc:01 1180226                    /lib/x86_64-linux-gnu/libc-2.19.so
	// 7f7d77d3c000-7f7d77d41000 rw-p 00000000 00:00 0
	// 7f7d77d41000-7f7d77d64000 r-xp 00000000 fc:01 1180217                    /lib/x86_64-linux-gnu/ld-2.19.so
	// 7f7d77f3f000-7f7d77f42000 rw-p 00000000 00:00 0
	// 7f7d77f61000-7f7d77f63000 rw-p 00000000 00:00 0
	// 7f7d77f63000-7f7d77f64000 r--p 00022000 fc:01 1180217                    /lib/x86_64-linux-gnu/ld-2.19.so
	// 7f7d77f64000-7f7d77f65000 rw-p 00023000 fc:01 1180217                    /lib/x86_64-linux-gnu/ld-2.19.so
	// 7f7d77f65000-7f7d77f66000 rw-p 00000000 00:00 0
	// 7ffc342a2000-7ffc342c3000 rw-p 00000000 00:00 0                          [stack]
	// 7ffc34343000-7ffc34345000 r-xp 00000000 00:00 0                          [vdso]
	// ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]

	var line []byte
	// next removes and returns the next field in the line.
	// It also removes from line any spaces following the field.
	next := func() []byte {
		var f []byte
		f, line, _ = bytesCut(line, space)
		line = bytes.TrimLeft(line, " ")

		return f
	}

	for len(data) > 0 {
		line, data, _ = bytesCut(data, newline)
		addr := next()
		loStr, hiStr, ok := stringsCut(string(addr), "-")
		if !ok {
			continue
		}
		lo, err := strconv.ParseUint(loStr, 16, 64)
		if err != nil {
			continue
		}
		hi, err := strconv.ParseUint(hiStr, 16, 64)
		if err != nil {
			continue
		}
		perm := next()
		if len(perm) < 4 || perm[2] != 'x' {
			// Only interested in executable mappings.
			continue
		}
		offset, err := strconv.ParseUint(string(next()), 16, 64)
		if err != nil {
			continue
		}
		next()          // dev
		inode := next() // inode
		if line == nil {
			continue
		}
		file := string(line)

		// Trim deleted file marker.
		deletedStr := " (deleted)"
		deletedLen := len(deletedStr)
		if len(file) >= deletedLen && file[len(file)-deletedLen:] == deletedStr {
			file = file[:len(file)-deletedLen]
		}

		if len(inode) == 1 && inode[0] == '0' && file == "" {
			// Huge-page text mappings list the initial fragment of
			// mapped but unpopulated memory as being inode 0.
			// Don't report that part.
			// But [vdso] and [vsyscall] are inode 0, so let non-empty file names through.
			continue
		}

		// TODO: pprof's remapMappingIDs makes one adjustment:
		// 1. If there is an /anon_hugepage mapping first and it is
		// consecutive to a next mapping, drop the /anon_hugepage.
		// There's no indication why this is needed.
		// Let's try not doing this and see what breaks.
		// If we do need it, it would go here, before we
		// enter the mappings into b.mem in the first place.

		buildID, _ := elfBuildID(file)
		addMapping(lo, hi, offset, file, buildID)
	}
}

// Cut slices s around the first instance of sep,
// returning the text before and after sep.
// The found result reports whether sep appears in s.
// If sep does not appear in s, cut returns s, nil, false.
//
// Cut returns slices of the original slice s, not copies.
//
//nolint:unparam
func bytesCut(s, sep []byte) (before, after []byte, found bool) {
	if i := bytes.Index(s, sep); i >= 0 {
		return s[:i], s[i+len(sep):], true
	}

	return s, nil, false
}

// Cut slices s around the first instance of sep,
// returning the text before and after sep.
// The found result reports whether sep appears in s.
// If sep does not appear in s, cut returns s, "", false.
func stringsCut(s, sep string) (before, after string, found bool) {
	if i := strings.Index(s, sep); i >= 0 {
		return s[:i], s[i+len(sep):], true
	}

	return s, "", false
}
```

## File: `godeltaprof/internal/pprof/protobuf.go`
```go
// Copyright 2014 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package pprof

// A protobuf is a simple protocol buffer encoder.
type protobuf struct {
	data []byte
	tmp  [16]byte
	nest int
}

func (b *protobuf) varint(x uint64) {
	for x >= 128 {
		b.data = append(b.data, byte(x)|0x80)
		x >>= 7
	}
	b.data = append(b.data, byte(x))
}

func (b *protobuf) length(tag int, l int) {
	b.varint(uint64(tag)<<3 | 2) //nolint:gosec
	b.varint(uint64(l))          //nolint:gosec
}

func (b *protobuf) uint64(tag int, x uint64) {
	// append varint to b.data
	b.varint(uint64(tag) << 3) //nolint:gosec
	b.varint(x)
}

func (b *protobuf) uint64s(tag int, x []uint64) {
	if len(x) > 2 {
		// Use packed encoding
		n1 := len(b.data)
		for _, u := range x {
			b.varint(u)
		}
		n2 := len(b.data)
		b.length(tag, n2-n1)
		n3 := len(b.data)
		copy(b.tmp[:], b.data[n2:n3])
		copy(b.data[n1+(n3-n2):], b.data[n1:n2])
		copy(b.data[n1:], b.tmp[:n3-n2])

		return
	}
	for _, u := range x {
		b.uint64(tag, u)
	}
}

func (b *protobuf) uint64Opt(tag int, x uint64) {
	if x == 0 {
		return
	}
	b.uint64(tag, x)
}

func (b *protobuf) int64(tag int, x int64) {
	u := uint64(x) //nolint:gosec
	b.uint64(tag, u)
}

func (b *protobuf) int64Opt(tag int, x int64) {
	if x == 0 {
		return
	}
	b.int64(tag, x)
}

func (b *protobuf) int64s(tag int, x []int64) {
	if len(x) > 2 {
		// Use packed encoding
		n1 := len(b.data)
		for _, u := range x {
			b.varint(uint64(u)) //nolint:gosec
		}
		n2 := len(b.data)
		b.length(tag, n2-n1)
		n3 := len(b.data)
		copy(b.tmp[:], b.data[n2:n3])
		copy(b.data[n1+(n3-n2):], b.data[n1:n2])
		copy(b.data[n1:], b.tmp[:n3-n2])

		return
	}
	for _, u := range x {
		b.int64(tag, u)
	}
}

func (b *protobuf) string(tag int, x string) {
	b.length(tag, len(x))
	b.data = append(b.data, x...)
}

func (b *protobuf) strings(tag int, x []string) {
	for _, s := range x {
		b.string(tag, s)
	}
}

func (b *protobuf) bool(tag int, x bool) {
	if x {
		b.uint64(tag, 1)
	} else {
		b.uint64(tag, 0)
	}
}

type msgOffset int

func (b *protobuf) startMessage() msgOffset {
	b.nest++

	return msgOffset(len(b.data))
}

func (b *protobuf) endMessage(tag int, start msgOffset) {
	n1 := int(start)
	n2 := len(b.data)
	b.length(tag, n2-n1)
	n3 := len(b.data)
	copy(b.tmp[:], b.data[n2:n3])
	copy(b.data[n1+(n3-n2):], b.data[n1:n2])
	copy(b.data[n1:], b.tmp[:n3-n2])
	b.nest--
}
```

## File: `godeltaprof/internal/pprof/stub.go`
```go
package pprof

func Runtime_cyclesPerSecond() int64 {
	return runtime_cyclesPerSecond()
}
```

## File: `godeltaprof/internal/pprof/stub_go20.go`
```go
//go:build go1.16 && !go1.21
// +build go1.16,!go1.21

package pprof

import (
	"runtime"
	_ "unsafe"
)

// runtime_FrameStartLine is defined in runtime/symtab.go.
func runtime_FrameStartLine(f *runtime.Frame) int {
	return 0
}

// runtime_FrameSymbolName is defined in runtime/symtab.go.
func runtime_FrameSymbolName(f *runtime.Frame) string {
	return f.Function
}

//go:linkname runtime_expandFinalInlineFrame runtime/pprof.runtime_expandFinalInlineFrame
func runtime_expandFinalInlineFrame(stk []uintptr) []uintptr

//go:linkname runtime_cyclesPerSecond runtime/pprof.runtime_cyclesPerSecond
func runtime_cyclesPerSecond() int64
```

## File: `godeltaprof/internal/pprof/stub_go22.go`
```go
//go:build go1.21 && !go1.23
// +build go1.21,!go1.23

package pprof

import (
	"runtime"
	_ "unsafe"
)

// runtime_FrameStartLine is defined in runtime/symtab.go.
//
//go:noescape
//go:linkname runtime_FrameStartLine runtime/pprof.runtime_FrameStartLine
func runtime_FrameStartLine(f *runtime.Frame) int

// runtime_FrameSymbolName is defined in runtime/symtab.go.
//
//go:noescape
//go:linkname runtime_FrameSymbolName runtime/pprof.runtime_FrameSymbolName
func runtime_FrameSymbolName(f *runtime.Frame) string

//go:linkname runtime_expandFinalInlineFrame runtime/pprof.runtime_expandFinalInlineFrame
func runtime_expandFinalInlineFrame(stk []uintptr) []uintptr

//go:linkname runtime_cyclesPerSecond runtime/pprof.runtime_cyclesPerSecond
func runtime_cyclesPerSecond() int64
```

## File: `godeltaprof/internal/pprof/stub_go23.go`
```go
//go:build go1.23
// +build go1.23

package pprof

import (
	"runtime"
	_ "unsafe"
)

// runtime_FrameStartLine is defined in runtime/symtab.go.
//
//go:noescape
//go:linkname runtime_FrameStartLine runtime/pprof.runtime_FrameStartLine
func runtime_FrameStartLine(f *runtime.Frame) int

// runtime_FrameSymbolName is defined in runtime/symtab.go.
//
//go:noescape
//go:linkname runtime_FrameSymbolName runtime/pprof.runtime_FrameSymbolName
func runtime_FrameSymbolName(f *runtime.Frame) string

//go:linkname runtime_expandFinalInlineFrame runtime/pprof.runtime_expandFinalInlineFrame
func runtime_expandFinalInlineFrame(stk []uintptr) []uintptr

//go:linkname runtime_cyclesPerSecond runtime/pprof.runtime_cyclesPerSecond
func runtime_cyclesPerSecond() int64
```

## File: `http/pprof/README.md`
```markdown
# Pyroscope CPU Profiler HTTP Handler

This package facilitates the collection of CPU profiles via HTTP without disrupting
the background operation of the Pyroscope profiler. It enables you to seamlessly gather
CPU profiles through HTTP while continuously sending them to Pyroscope.

The standard Go pprof HTTP endpoint `/debug/pprof/profile` returns an error if profiling
is already started:

> Could not enable CPU profiling: CPU profiling already in use

The Pyroscope CPU Profiler HTTP handler serve this gracefully by communicating with
the Pyroscope profiler, which collects profiles in the background.

## Usage

The package does not register the handler automatically. It is highly recommended to
avoid using the standard path `/debug/pprof/profile` and the default mux because
attempting to register the handler on the same path will cause a panic. In many cases,
the `net/http/pprof` package is imported by dependencies, and therefore there is no
reliable way to avoid the conflict.

```go
package main

import (
    "net/http"

    "github.com/grafana/pyroscope-go/http/pprof"
)

func main() {
	http.HandleFunc("/debug/pprof/cpu", pprof.Profile)
}
```

With each invocation of the handler, it suspends the Pyroscope profiler, gathers a CPU
profile, dispatches the collected profile to both the caller and the Pyroscope profiler,
and subsequently resumes the profiler.
```

## File: `http/pprof/pprof.go`
```go
// Copyright 2010 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package pprof

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"strconv"
	"time"

	internal "github.com/grafana/pyroscope-go/internal/pprof"
)

// Profile responds with the pprof-formatted cpu profile.
// Profiling lasts for duration specified in seconds GET parameter, or for 30 seconds if not specified.
// The package initialization registers it as /debug/pprof/profile.
func Profile(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("X-Content-Type-Options", "nosniff")
	sec, err := strconv.ParseInt(r.FormValue("seconds"), 10, 64)
	if sec <= 0 || err != nil {
		sec = 30
	}

	if durationExceedsWriteTimeout(r, float64(sec)) {
		serveError(w, http.StatusBadRequest, "profile duration exceeds server's WriteTimeout")

		return
	}

	// Set Content Type assuming StartCPUProfile will work,
	// because if it does it start writing.
	w.Header().Set("Content-Type", "application/octet-stream")
	w.Header().Set("Content-Disposition", `attachment; filename="profile"`)
	ctx, cancel := context.WithTimeout(r.Context(), time.Duration(sec)*time.Second)
	defer cancel()
	if err = collectCPUProfile(ctx, w); err != nil {
		serveError(w, http.StatusInternalServerError, fmt.Sprintf("Could not enable CPU profiling: %s", err))
	}
}

func durationExceedsWriteTimeout(r *http.Request, seconds float64) bool {
	srv, ok := r.Context().Value(http.ServerContextKey).(*http.Server)

	return ok && srv.WriteTimeout != 0 && seconds >= srv.WriteTimeout.Seconds()
}

func serveError(w http.ResponseWriter, status int, txt string) {
	w.Header().Set("Content-Type", "text/plain; charset=utf-8")
	w.Header().Set("X-Go-Pprof", "1")
	w.Header().Del("Content-Disposition")
	w.WriteHeader(status)
	_, _ = fmt.Fprintln(w, txt)
}

func collectCPUProfile(ctx context.Context, w io.Writer) error {
	if err := internal.StartCPUProfile(w); err != nil {
		return err
	}
	<-ctx.Done()
	internal.StopCPUProfile()

	return nil
}
```

## File: `internal/labelset/labelset.go`
```go
// Package labelset implements parsing/normalizing of string representation of the Label Set of a
// profile.
//
// This is used by the /ingest endpoint, as described in the original Pyroscope API. We keep
// this mainly for backwards compatibility.
// The package is copied from pyroscope/api module
package labelset

import (
	"bytes"
	"errors"
	"sort"
	"strconv"
	"strings"
	"sync"
	"time"
)

type LabelSet struct {
	labels map[string]string
}

type ParserState int

const (
	nameParserState ParserState = iota
	tagLabelSetParserState
	tagValueParserState
	doneParserState
)

func New(labels map[string]string) *LabelSet { return &LabelSet{labels: labels} }

func Parse(name string) (*LabelSet, error) {
	k := &LabelSet{labels: make(map[string]string)}
	p, ok := parserPool.Get().(*parser)
	if !ok {
		return nil, errParserPoolFailure
	}
	defer parserPool.Put(p)
	p.reset()
	var err error
	for _, r := range name + "{" {
		switch p.parserState {
		case nameParserState:
			err = p.nameParserCase(r, k)
		case tagLabelSetParserState:
			p.tagLabelSetParserCase(r)
		case tagValueParserState:
			err = p.tagValueParserCase(r, k)
		case doneParserState:
			// No action needed
		}
		if err != nil {
			return nil, err
		}
	}

	return k, nil
}

func ValidateLabelSet(k *LabelSet) error {
	if k == nil {
		return ErrInvalidLabelSet
	}

	for key, v := range k.labels {
		if key == ReservedLabelNameName {
			if err := ValidateServiceName(v); err != nil {
				return err
			}
		} else {
			if err := ValidateLabelName(key); err != nil {
				return err
			}
		}
	}

	return nil
}

type parser struct {
	parserState ParserState
	key         *bytes.Buffer
	value       *bytes.Buffer
}

var parserPool = sync.Pool{ //nolint:gochecknoglobals
	New: func() any {
		return &parser{
			parserState: nameParserState,
			key:         new(bytes.Buffer),
			value:       new(bytes.Buffer),
		}
	},
}

func (p *parser) reset() {
	p.parserState = nameParserState
	p.key.Reset()
	p.value.Reset()
}

// Parse's nameParserState switch case
func (p *parser) nameParserCase(r int32, k *LabelSet) error {
	switch r {
	case '{':
		p.parserState = tagLabelSetParserState
		serviceName := strings.TrimSpace(p.value.String())
		if err := ValidateServiceName(serviceName); err != nil {
			return err
		}
		k.labels["__name__"] = serviceName
	default:
		p.value.WriteRune(r)
	}

	return nil
}

// Parse's tagLabelSetParserState switch case
func (p *parser) tagLabelSetParserCase(r rune) {
	switch r {
	case '}':
		p.parserState = doneParserState
	case '=':
		p.parserState = tagValueParserState
		p.value.Reset()
	default:
		p.key.WriteRune(r)
	}
}

// Parse's tagValueParserState switch case
func (p *parser) tagValueParserCase(r rune, k *LabelSet) error {
	switch r {
	case ',', '}':
		p.parserState = tagLabelSetParserState
		key := strings.TrimSpace(p.key.String())
		if !IsLabelNameReserved(key) {
			if err := ValidateLabelName(key); err != nil {
				return err
			}
		}
		k.labels[key] = strings.TrimSpace(p.value.String())
		p.key.Reset()
	default:
		p.value.WriteRune(r)
	}

	return nil
}

func (k *LabelSet) LabelSet() string {
	return k.Normalized()
}

const ProfileIDLabelName = "profile_id"

func (k *LabelSet) HasProfileID() bool {
	v, ok := k.labels[ProfileIDLabelName]

	return ok && v != ""
}

func (k *LabelSet) ProfileID() (string, bool) {
	id, ok := k.labels[ProfileIDLabelName]

	return id, ok
}

func ServiceNameLabelSet(appName string) string { return appName + "{}" }

func TreeLabelSet(k string, depth int, unixTime int64) string {
	return k + ":" + strconv.Itoa(depth) + ":" + strconv.FormatInt(unixTime, 10)
}

func (k *LabelSet) TreeLabelSet(depth int, t time.Time) string {
	return TreeLabelSet(k.Normalized(), depth, t.Unix())
}

var (
	errLabelSetInvalid   = errors.New("invalid key")
	errParserPoolFailure = errors.New("failed to get parser from pool")
)

// ParseTreeLabelSet retrieves tree time and depth level from the given key.
func ParseTreeLabelSet(k string) (time.Time, int, error) {
	a := strings.Split(k, ":")
	if len(a) < 3 {
		return time.Time{}, 0, errLabelSetInvalid
	}
	level, err := strconv.Atoi(a[1])
	if err != nil {
		return time.Time{}, 0, err
	}
	v, err := strconv.Atoi(a[2])
	if err != nil {
		return time.Time{}, 0, err
	}

	return time.Unix(int64(v), 0), level, err
}

func (k *LabelSet) DictLabelSet() string {
	return k.labels[ReservedLabelNameName]
}

// FromTreeToDictLabelSet returns app name from tree key k: given tree key
// "foo{}:0:1234567890", the call returns "foo".
//
// Before tags support, segment key form (i.e. app name + tags: foo{key=value})
// has been used to reference a dictionary (trie).
func FromTreeToDictLabelSet(k string) string {
	return k[0:strings.IndexAny(k, "{")]
}

func (l *LabelSet) Normalized() string {
	var sb strings.Builder

	labelNames := make([]string, 0, len(l.labels))
	for k, v := range l.labels {
		if k == ReservedLabelNameName {
			sb.WriteString(v)
		} else {
			labelNames = append(labelNames, k)
		}
	}

	sort.Slice(labelNames, func(i, j int) bool {
		return labelNames[i] < labelNames[j]
	})

	sb.WriteString("{")
	for i, k := range labelNames {
		v := l.labels[k]
		if i != 0 {
			sb.WriteString(",")
		}
		sb.WriteString(k)
		sb.WriteString("=")
		sb.WriteString(v)
	}
	sb.WriteString("}")

	return sb.String()
}

func (k *LabelSet) Clone() *LabelSet {
	newMap := make(map[string]string)
	for k, v := range k.labels {
		newMap[k] = v
	}

	return &LabelSet{labels: newMap}
}

func (k *LabelSet) ServiceName() string {
	return k.labels[ReservedLabelNameName]
}

func (k *LabelSet) Labels() map[string]string {
	return k.labels
}

func (k *LabelSet) Add(key, value string) {
	if value == "" {
		delete(k.labels, key)
	} else {
		k.labels[key] = value
	}
}
```

## File: `internal/labelset/labelset_bench_test.go`
```go
package labelset

import (
	"math/rand"
	"testing"
)

func BenchmarkKey_Parse(b *testing.B) {
	const (
		labelsSize = 10
		minLen     = 6
		maxLen     = 16
	)

	// Duplicates are okay.
	labels := make(map[string]string, labelsSize+1)
	for i := 0; i < labelsSize; i++ {
		labels[randString(randInt(minLen, maxLen))] = randString(randInt(minLen, maxLen))
	}

	labels["__name__"] = "benchmark.key.parse"
	keyStr := New(labels).Normalized()

	b.ReportAllocs()
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		if _, err := Parse(keyStr); err != nil {
			b.Fatal(err)
		}
	}
}

func randInt(minVal, maxVal int) int { return rand.Intn(maxVal-minVal) + minVal } //nolint:gosec

// TODO(kolesnikovae): This is not near perfect way of generating strings.
//  It makes sense to create a package for util functions like this.

const letterBytes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

func randString(n int) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = letterBytes[rand.Intn(len(letterBytes))] //nolint:gosec
	}

	return string(b)
}
```

## File: `internal/labelset/labelset_test.go`
```go
package labelset

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestParseLabelSet(t *testing.T) {
	t.Run("no tags version works", func(t *testing.T) {
		k, err := Parse("foo")
		require.NoError(t, err)
		require.Equal(t, map[string]string{"__name__": "foo"}, k.labels)
	})

	t.Run("simple values work", func(t *testing.T) {
		k, err := Parse("foo{bar=1,baz=2}")
		require.NoError(t, err)
		require.Equal(t, map[string]string{"__name__": "foo", "bar": "1", "baz": "2"}, k.labels)
	})

	t.Run("simple values with spaces work", func(t *testing.T) {
		k, err := Parse(" foo { bar = 1 , baz = 2 } ")
		require.NoError(t, err)
		require.Equal(t, map[string]string{"__name__": "foo", "bar": "1", "baz": "2"}, k.labels)
	})
}

func TestKeyNormalize(t *testing.T) {
	t.Run("no tags version works", func(t *testing.T) {
		k, err := Parse("foo")
		require.NoError(t, err)
		require.Equal(t, "foo{}", k.Normalized())
	})

	t.Run("simple values work", func(t *testing.T) {
		k, err := Parse("foo{bar=1,baz=2}")
		require.NoError(t, err)
		require.Equal(t, "foo{bar=1,baz=2}", k.Normalized())
	})

	t.Run("unsorted values work", func(t *testing.T) {
		k, err := Parse("foo{baz=1,bar=2}")
		require.NoError(t, err)
		require.Equal(t, "foo{bar=2,baz=1}", k.Normalized())
	})
}
```

## File: `internal/labelset/validate.go`
```go
package labelset

import (
	"errors"
	"fmt"
)

var (
	ErrInvalidServiceName    = errors.New("invalid service name")
	ErrInvalidLabelSet       = errors.New("invalid label set")
	ErrInvalidLabelName      = errors.New("invalid label name")
	ErrServiceNameIsRequired = errors.New("service name is required")
	ErrLabelNameIsRequired   = errors.New("label name is required")
	ErrLabelNameReserved     = errors.New("label name is reserved")
)

const ReservedLabelNameName = "__name__"

var reservedLabelNames = []string{ //nolint:gochecknoglobals
	ReservedLabelNameName,
}

type Error struct {
	Inner error
	Expr  string
	// TODO: add offset?
}

func newErr(err error, expr string) *Error { return &Error{Inner: err, Expr: expr} }

func (e *Error) Error() string { return e.Inner.Error() + ": " + e.Expr }

func (e *Error) Unwrap() error { return e.Inner }

func newInvalidLabelNameRuneError(k string, r rune) *Error {
	return newInvalidRuneError(ErrInvalidLabelName, k, r)
}

func NewInvalidServiceNameRuneError(k string, r rune) *Error {
	return newInvalidRuneError(ErrInvalidServiceName, k, r)
}

func newInvalidRuneError(err error, k string, r rune) *Error {
	return newErr(err, fmt.Sprintf("%s: character is not allowed: %q", k, r))
}

// ValidateLabelName report an error if the given key k violates constraints.
//
// The function should be used to validate user input. The function returns
// ErrLabelNameReserved if the key is valid but reserved for internal use.
func ValidateLabelName(k string) error {
	if len(k) == 0 {
		return ErrLabelNameIsRequired
	}
	for _, r := range k {
		if !IsLabelNameRuneAllowed(r) {
			return newInvalidLabelNameRuneError(k, r)
		}
	}
	if IsLabelNameReserved(k) {
		return newErr(ErrLabelNameReserved, k)
	}

	return nil
}

// ValidateServiceName report an error if the given app name n violates constraints.
func ValidateServiceName(n string) error {
	if len(n) == 0 {
		return ErrServiceNameIsRequired
	}
	for _, r := range n {
		if !IsServiceNameRuneAllowed(r) {
			return NewInvalidServiceNameRuneError(n, r)
		}
	}

	return nil
}

func IsLabelNameRuneAllowed(r rune) bool {
	return (r >= 'a' && r <= 'z') || (r >= 'A' && r <= 'Z') || (r >= '0' && r <= '9') || r == '_' || r == '.'
}

func IsServiceNameRuneAllowed(r rune) bool {
	return r == '-' || r == '.' || r == '/' || IsLabelNameRuneAllowed(r)
}

func IsLabelNameReserved(k string) bool {
	for _, s := range reservedLabelNames {
		if s == k {
			return true
		}
	}

	return false
}
```

## File: `internal/pprof/pprof.go`
```go
package pprof

import (
	"io"
	"runtime/pprof"
	"sync"
)

var c struct { //nolint:gochecknoglobals
	sync.Mutex
	Collector

	ref int64
	fn  func()
}

type Collector interface {
	StartCPUProfile(w io.Writer) error
	StopCPUProfile()
}

func DefaultCollector() Collector { return defaultCollector{} }

type defaultCollector struct{}

func (c defaultCollector) StartCPUProfile(w io.Writer) error { return pprof.StartCPUProfile(w) }
func (c defaultCollector) StopCPUProfile()                   { pprof.StopCPUProfile() }

func StartCPUProfile(w io.Writer) error {
	c.Lock()
	defer c.Unlock()
	if c.Collector == nil {
		c.Collector = defaultCollector{}
	}
	err := c.StartCPUProfile(w)
	if err == nil {
		c.ref++
	}

	return err
}

func StopCPUProfile() {
	c.Lock()
	defer c.Unlock()
	c.StopCPUProfile()
	if c.ref--; c.ref == 0 && c.fn != nil {
		c.fn()
		c.fn = nil
	}
}

func SetCollector(collector Collector) {
	c.Lock()
	if c.ref == 0 {
		c.Collector = collector
		c.Unlock()

		return
	}
	ch := make(chan struct{})
	fn := c.fn
	c.fn = func() {
		if fn != nil {
			fn()
		}
		c.Collector = collector
		close(ch)
	}
	c.Unlock()
	<-ch
}

func ResetCollector() { SetCollector(nil) }
```

## File: `internal/pprof/pprof_test.go`
```go
package pprof

import (
	"io"
	"runtime"
	"testing"
)

func Test_SetCollector(t *testing.T) {
	for i := 0; i < 20; i++ {
		_ = StartCPUProfile(io.Discard)
		// SetCollector blocks until StopCPUProfile is called.
		done := make(chan struct{})
		go func() {
			ResetCollector()
			close(done)
		}()
		runtime.Gosched()
		StopCPUProfile()
		<-done
		if c.Collector != nil {
			t.Fatal("collector was not reset")
		}
	}
}

func Test_DefaultCollector(t *testing.T) {
	err := StartCPUProfile(io.Discard)
	if err != nil {
		t.Fatalf("Default collector StartCPUProfile: %v", err)
	}
	err = StartCPUProfile(io.Discard)
	if err == nil {
		t.Fatalf("Default collector must fail on consecuitive StartCPUProfile")
	}
	StopCPUProfile()
}
```

## File: `internal/testutil/logging.go`
```go
package testutil

import (
	"fmt"
	"sync"
)

type TestLogger struct {
	sync.Mutex

	lines []string
}

func NewTestLogger() *TestLogger {
	return &TestLogger{lines: make([]string, 0)}
}

func (t *TestLogger) Debugf(format string, args ...interface{}) { t.putf(format, args...) }
func (t *TestLogger) Infof(format string, args ...interface{})  { t.putf(format, args...) }
func (t *TestLogger) Errorf(format string, args ...interface{}) { t.putf(format, args...) }

func (t *TestLogger) putf(format string, args ...interface{}) {
	t.Lock()
	t.lines = append(t.lines, fmt.Sprintf(format, args...))
	t.Unlock()
}

// Lines returns a copy of the logged lines
func (t *TestLogger) Lines() []string {
	t.Lock()
	defer t.Unlock()

	return append([]string(nil), t.lines...)
}
```

## File: `upstream/upstream.go`
```go
package upstream

import (
	"time"
)

type Format string

const FormatPprof Format = "pprof"

type Upstream interface {
	Upload(job *UploadJob)
	Flush()
}

type SampleType struct {
	Units       string `json:"units,omitempty"`
	Aggregation string `json:"aggregation,omitempty"`
	DisplayName string `json:"display-name,omitempty"`
	Sampled     bool   `json:"sampled,omitempty"`
	Cumulative  bool   `json:"cumulative,omitempty"`
}

type UploadJob struct {
	Name            string
	StartTime       time.Time
	EndTime         time.Time
	SpyName         string
	SampleRate      uint32
	Units           string
	AggregationType string
	Format          Format
	Profile         []byte
	// Deprecated
	PrevProfile      []byte
	SampleTypeConfig map[string]*SampleType
}
```

## File: `upstream/remote/remote.go`
```go
package remote

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"mime/multipart"
	"net/http"
	"net/url"
	"path"
	"runtime/debug"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/grafana/pyroscope-go/upstream"
)

var errCloudTokenRequired = errors.New("please provide an authentication token." +
	" You can find it here: https://pyroscope.io/cloud")

const (
	authTokenDeprecationWarning = "Authtoken is specified, but deprecated and ignored. " +
		"Please switch to BasicAuthUser and BasicAuthPassword. " +
		"If you need to use Bearer token authentication for a custom setup, " +
		"you can use the HTTPHeaders option to set the Authorization header manually."
	cloudHostnameSuffix = "pyroscope.cloud"
)

type Remote struct {
	mu     sync.Mutex
	cfg    Config
	jobs   chan job
	client HTTPClient
	logger Logger

	done chan struct{}
	wg   sync.WaitGroup

	flushWG *sync.WaitGroup
}

type HTTPClient interface {
	Do(req *http.Request) (*http.Response, error)
}

type Config struct {
	// Deprecated: AuthToken will be removed in future releases.
	// Use BasicAuthUser and BasicAuthPassword instead.
	AuthToken         string
	BasicAuthUser     string // http basic auth user
	BasicAuthPassword string // http basic auth password
	TenantID          string
	HTTPHeaders       map[string]string
	Threads           int
	Address           string
	Timeout           time.Duration
	Logger            Logger
	HTTPClient        HTTPClient // optional, custom client
}

type Logger interface {
	Infof(_ string, _ ...interface{})
	Debugf(_ string, _ ...interface{})
	Errorf(_ string, _ ...interface{})
}

func NewRemote(cfg Config) (*Remote, error) {
	r := &Remote{
		cfg:  cfg,
		jobs: make(chan job, 20),
		client: &http.Client{
			Transport: &http.Transport{
				MaxConnsPerHost: cfg.Threads,
			},
			// Don't follow redirects
			// Since the go http client strips the Authorization header when doing redirects (eg http -> https)
			// https://github.com/golang/go/blob/a41763539c7ad09a22720a517a28e6018ca4db0f/src/net/http/client_test.go#L1764
			// making an authorized server return a 401
			// which is confusing since the user most likely already set up an API Key
			CheckRedirect: func(req *http.Request, via []*http.Request) error {
				return http.ErrUseLastResponse
			},
			Timeout: cfg.Timeout,
		},
		logger:  cfg.Logger,
		done:    make(chan struct{}),
		flushWG: new(sync.WaitGroup),
	}
	if cfg.HTTPClient != nil {
		r.client = cfg.HTTPClient
	}

	// parse the upstream address
	u, err := url.Parse(cfg.Address)
	if err != nil {
		return nil, err
	}

	// authorize the token first
	if cfg.AuthToken == "" && isOGPyroscopeCloud(u) {
		return nil, errCloudTokenRequired
	}

	return r, nil
}

func (r *Remote) Start() {
	r.wg.Add(r.cfg.Threads)
	for i := 0; i < r.cfg.Threads; i++ {
		go r.handleJobs()
	}
}

func (r *Remote) Stop() {
	if r.done != nil {
		close(r.done)
	}

	// wait for uploading goroutines exit
	r.wg.Wait()
}

func (r *Remote) Upload(uj *upstream.UploadJob) {
	r.mu.Lock()
	defer r.mu.Unlock()
	r.flushWG.Add(1)
	j := job{
		upload: uj,
		flush:  r.flushWG,
	}
	select {
	case r.jobs <- j:
	default:
		j.flush.Done()
		r.logger.Errorf("remote upload queue is full, dropping a profile job")
	}
}

func (r *Remote) Flush() {
	r.mu.Lock()
	flush := r.flushWG
	r.flushWG = new(sync.WaitGroup)
	r.mu.Unlock()
	flush.Wait()
}

func (r *Remote) uploadProfile(j *upstream.UploadJob) error {
	u, err := url.Parse(r.cfg.Address)
	if err != nil {
		return fmt.Errorf("url parse: %w", err)
	}

	body := &bytes.Buffer{}

	writer := multipart.NewWriter(body)
	fw, err := writer.CreateFormFile("profile", "profile.pprof")
	if err != nil {
		return err
	}
	_, _ = fw.Write(j.Profile)
	if j.SampleTypeConfig != nil {
		fw, err = writer.CreateFormFile("sample_type_config", "sample_type_config.json")
		if err != nil {
			return err
		}
		b, err := json.Marshal(j.SampleTypeConfig)
		if err != nil {
			return err
		}
		_, _ = fw.Write(b)
	}
	if err = writer.Close(); err != nil {
		return err
	}

	q := u.Query()
	q.Set("name", j.Name)
	q.Set("from", strconv.FormatInt(j.StartTime.UnixNano(), 10))
	q.Set("until", strconv.FormatInt(j.EndTime.UnixNano(), 10))
	q.Set("spyName", j.SpyName)
	q.Set("sampleRate", strconv.Itoa(int(j.SampleRate)))
	q.Set("units", j.Units)
	q.Set("aggregationType", j.AggregationType)

	u.Path = path.Join(u.Path, "ingest")
	u.RawQuery = q.Encode()

	r.logger.Debugf("uploading at %s", u.String())
	// new a request for the job
	request, err := http.NewRequestWithContext(context.Background(), http.MethodPost, u.String(), body)
	if err != nil {
		return fmt.Errorf("new http request: %w", err)
	}
	contentType := writer.FormDataContentType()
	r.logger.Debugf("content type: %s", contentType)
	request.Header.Set("Content-Type", contentType)
	// request.Header.Set("Content-Type", "binary/octet-stream+"+string(j.Format))

	switch {
	case r.cfg.AuthToken != "" && isOGPyroscopeCloud(u):
		request.Header.Set("Authorization", "Bearer "+r.cfg.AuthToken)
	case r.cfg.BasicAuthUser != "" && r.cfg.BasicAuthPassword != "":
		request.SetBasicAuth(r.cfg.BasicAuthUser, r.cfg.BasicAuthPassword)
	case r.cfg.AuthToken != "":
		request.Header.Set("Authorization", "Bearer "+r.cfg.AuthToken)
		r.logger.Infof(authTokenDeprecationWarning)
	}
	if r.cfg.TenantID != "" {
		request.Header.Set("X-Scope-OrgID", r.cfg.TenantID)
	}
	for k, v := range r.cfg.HTTPHeaders {
		request.Header.Set(k, v)
	}

	// do the request and get the response
	response, err := r.client.Do(request)
	if err != nil {
		return fmt.Errorf("do http request: %w", err)
	}
	defer func() {
		_ = response.Body.Close()
	}()

	// read all the response body
	respBody, err := io.ReadAll(response.Body)
	if err != nil {
		return fmt.Errorf("read response body: %w", err)
	}

	if response.StatusCode != http.StatusOK {
		return fmt.Errorf("failed to upload: (%d) '%s'", //nolint:err113
			response.StatusCode, string(respBody))
	}

	return nil
}

// handle the jobs
func (r *Remote) handleJobs() {
	for {
		select {
		case <-r.done:
			r.wg.Done()

			return
		case j := <-r.jobs:
			r.safeUpload(j.upload)
			j.flush.Done()
		}
	}
}

func isOGPyroscopeCloud(u *url.URL) bool {
	return strings.HasSuffix(u.Host, cloudHostnameSuffix)
}

// do safe upload
func (r *Remote) safeUpload(job *upstream.UploadJob) {
	defer func() {
		if catch := recover(); catch != nil {
			r.logger.Errorf("recover stack: %v: %v", catch, string(debug.Stack()))
		}
	}()

	// update the profile data to server
	if err := r.uploadProfile(job); err != nil {
		r.logger.Errorf("upload profile: %v", err)
	}
}

type job struct {
	upload *upstream.UploadJob
	flush  *sync.WaitGroup
}
```

## File: `upstream/remote/remote_test.go`
```go
package remote

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
	"sync"
	"testing"
	"time"

	"github.com/stretchr/testify/require"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"

	"github.com/grafana/pyroscope-go/internal/testutil"
	"github.com/grafana/pyroscope-go/upstream"
)

func TestUploadProfile(t *testing.T) {
	tests := []struct {
		name               string
		cfg                Config
		serverAddress      string
		expectedAuthHeader string
		expectWarning      bool
	}{
		{
			name: "OG Pyroscope Cloud with AuthToken",
			cfg: Config{
				AuthToken: "test-token",
				Address:   "https://example.pyroscope.cloud",
			},
			expectedAuthHeader: "Bearer test-token",
			expectWarning:      false,
		},
		{
			name: "Non-OG Server with BasicAuth",
			cfg: Config{
				BasicAuthUser:     "user",
				BasicAuthPassword: "pass",
				Address:           "https://example.com",
			},
			expectedAuthHeader: "Basic dXNlcjpwYXNz", // Base64 encoded "user:pass"
			expectWarning:      false,
		},
		{
			name: "Non-OG Server with AuthToken (Deprecated)",
			cfg: Config{
				AuthToken: "deprecated-token",
				Address:   "https://example.com",
			},
			expectedAuthHeader: "Bearer deprecated-token",
			expectWarning:      true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			logger := testutil.NewTestLogger()
			mockClient := new(MockHTTPClient)

			mockClient.On("Do", mock.Anything).Return(&http.Response{
				StatusCode: http.StatusOK,
				Body:       io.NopCloser(bytes.NewBufferString("OK")),
			}, nil)

			r := &Remote{
				cfg:    tt.cfg,
				client: mockClient,
				logger: logger,
			}

			err := r.uploadProfile(&upstream.UploadJob{
				Name:       "test-profile",
				StartTime:  time.Now(),
				EndTime:    time.Now().Add(time.Minute),
				SpyName:    "test-spy",
				SampleRate: 100,
				Units:      "samples",
			})
			require.NoError(t, err)

			if tt.expectWarning {
				assert.Contains(t, logger.Lines(), authTokenDeprecationWarning)
			} else {
				assert.NotContains(t, logger.Lines(), authTokenDeprecationWarning)
			}

			mockClient.AssertCalled(t, "Do", mock.MatchedBy(func(req *http.Request) bool {
				return req.Header.Get("Authorization") == tt.expectedAuthHeader
			}))

			mockClient.AssertExpectations(t)
		})
	}
}

type MockHTTPClient struct {
	mock.Mock
}

func (m *MockHTTPClient) Do(req *http.Request) (*http.Response, error) {
	args := m.Called(req)
	err := args.Error(1)
	a0 := args.Get(0)
	switch typed := a0.(type) {
	case *http.Response:
		return typed, err
	case func() *http.Response:
		return typed(), err
	default:
		return nil, fmt.Errorf("unknown mock arg type arg %+v %w", a0, err)
	}
}

func TestConcurrentUploadFlushRace(t *testing.T) {
	mockClient := new(MockHTTPClient)
	mockClient.On("Do", mock.Anything).Return(func() *http.Response {
		return &http.Response{
			StatusCode: http.StatusOK,
			Body:       io.NopCloser(bytes.NewBufferString("OK")),
		}
	}, nil)
	r, err := NewRemote(Config{
		Threads:    2,
		Logger:     testutil.NewTestLogger(),
		HTTPClient: mockClient,
	})
	require.NoError(t, err)
	r.Start()
	defer r.Stop()

	var wg sync.WaitGroup
	wg.Add(2)
	loop := func(f func()) {
		timeout := time.After(10 * time.Millisecond)
		go func() {
			defer wg.Done()
			for {
				select {
				case <-timeout:
					return
				default:
					f()
				}
			}
		}()
	}
	loop(func() {
		r.Upload(newJob("job1"))
	})
	loop(func() {
		r.Flush()
	})
	wg.Wait()
}

func newJob(name string) *upstream.UploadJob {
	return &upstream.UploadJob{
		Name: name,
	}
}
```

## File: `x/k6/Makefile`
```
.PHONY: test
test:
	go test -race ./...

.PHONY: go/mod
go/mod:
	GO111MODULE=on go mod download
	go work sync
	GO111MODULE=on go mod tidy
```

## File: `x/k6/README.md`
```markdown
# Pyroscope Go SDK k6 extension

This library provides extension functions to provide support for Grafana's
integration between Pyroscope and k6. Namely, it provides HTTP and gRPC
middleware to dynamically label the profiling context with k6 test metadata.

> [!CAUTION]
> Maintainers: Be aware this project has its own `go.work` file and is built
> independently of the rest of the Go SDK. This is because this project has a
> dependency on `google.golang.org/grpc` which is only supported for the last
> 2 major versions of Go. Since it's not acceptable to extend this restriction
> to the remainder of the SDK, this module remains independent from the rest of
> the code base.
```

## File: `x/k6/baggage.go`
```go
package k6

import (
	"context"
	grpcmiddleware "github.com/grpc-ecosystem/go-grpc-middleware/v2"
	"net/http"
	"runtime/pprof"
	"strings"

	"github.com/grafana/pyroscope-go"
	"go.opentelemetry.io/otel/baggage"
	"google.golang.org/grpc"
	"google.golang.org/grpc/metadata"
)

// LabelsFromBaggageHandler is a middleware that will extract key-value pairs
// from the request baggage and make them profiling labels.
func LabelsFromBaggageHandler(handler http.Handler) http.Handler {
	lh := &labelHandler{
		innerHandler: handler,
	}

	return lh
}

func LabelsFromBaggageUnaryInterceptor(ctx context.Context, req interface{}, _ *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
	var found bool
	ctx, found = setBaggageContextFromMetadata(ctx)
	if !found {
		return handler(ctx, req)
	}

	labels := getBaggageLabelsFromContext(ctx)
	if labels == nil {
		return handler(ctx, req)
	}

	// Inlined version of pyroscope.TagWrapper and pprof.Do to reduce noise in
	// the stack trace.
	defer pprof.SetGoroutineLabels(ctx)
	ctx = pprof.WithLabels(ctx, *labels)
	pprof.SetGoroutineLabels(ctx)

	return handler(ctx, req)
}

func LabelsFromBaggageStreamInterceptor(srv interface{}, ss grpc.ServerStream, _ *grpc.StreamServerInfo, handler grpc.StreamHandler) error {
	ctx := ss.Context()

	var found bool
	ctx, found = setBaggageContextFromMetadata(ctx)
	if !found {
		return handler(srv, ss)
	}

	labels := getBaggageLabelsFromContext(ctx)
	if labels == nil {
		return handler(srv, ss)
	}

	// Inlined version of pyroscope.TagWrapper and pprof.Do to reduce noise in
	// the stack trace.
	defer pprof.SetGoroutineLabels(ctx)
	ctx = pprof.WithLabels(ctx, *labels)
	pprof.SetGoroutineLabels(ctx)

	return handler(srv, &grpcmiddleware.WrappedServerStream{
		ServerStream:   ss,
		WrappedContext: ctx,
	})
}

type labelHandler struct {
	innerHandler http.Handler
}

func (lh *labelHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	var found bool
	r, found = setBaggageContextFromHeader(r)
	if !found {
		lh.innerHandler.ServeHTTP(w, r)
		return
	}

	ctx := r.Context()
	labels := getBaggageLabelsFromContext(ctx)
	if labels == nil {
		lh.innerHandler.ServeHTTP(w, r)
		return
	}

	// Inlined version of pyroscope.TagWrapper and pprof.Do to reduce noise in
	// the stack trace.
	defer pprof.SetGoroutineLabels(ctx)
	ctx = pprof.WithLabels(ctx, *labels)
	pprof.SetGoroutineLabels(ctx)

	lh.innerHandler.ServeHTTP(w, r.WithContext(ctx))
}

func setBaggageContextFromHeader(r *http.Request) (*http.Request, bool) {
	baggageHeader := r.Header.Get("Baggage")
	if baggageHeader == "" {
		return r, false
	}

	b, err := baggage.Parse(baggageHeader)
	if err != nil {
		return r, false
	}

	ctx := baggage.ContextWithBaggage(r.Context(), b)
	return r.WithContext(ctx), true
}

func setBaggageContextFromMetadata(ctx context.Context) (context.Context, bool) {
	md, ok := metadata.FromIncomingContext(ctx)
	if !ok {
		return ctx, false
	}

	baggageHeader := md.Get("Baggage")
	if baggageHeader == nil || len(baggageHeader) == 0 {
		return ctx, false
	}

	b, err := baggage.Parse(baggageHeader[0])
	if err != nil {
		return ctx, false
	}

	ctx = baggage.ContextWithBaggage(ctx, b)
	return ctx, true
}

// getBaggageLabels applies filters and transformations to request baggage and
// returns the resulting LabelSet.
func getBaggageLabelsFromContext(ctx context.Context) *pyroscope.LabelSet {
	b := baggage.FromContext(ctx)
	if b.Len() == 0 {
		return nil
	}

	return baggageToLabels(b)
}

// baggageToLabels converts request baggage to a LabelSet.
func baggageToLabels(b baggage.Baggage) *pyroscope.LabelSet {
	labelPairs := make([]string, 0, len(b.Members())*2)
	for _, m := range b.Members() {
		if !strings.HasPrefix(m.Key(), "k6.") {
			continue
		}

		if m.Value() == "" {
			continue
		}

		key := strings.ReplaceAll(m.Key(), ".", "_")
		labelPairs = append(labelPairs, key, m.Value())
	}

	if len(labelPairs) == 0 {
		return nil
	}

	labels := pyroscope.Labels(labelPairs...)
	return &labels
}
```

## File: `x/k6/baggage_test.go`
```go
package k6

import (
	"context"
	grpcmiddleware "github.com/grpc-ecosystem/go-grpc-middleware/v2"
	"net/http"
	"net/http/httptest"
	"runtime/pprof"
	"sort"
	"testing"

	"github.com/stretchr/testify/require"
	"go.opentelemetry.io/otel/baggage"
	"google.golang.org/grpc"
	"google.golang.org/grpc/metadata"
)

func TestLabelsFromBaggageHandler(t *testing.T) {
	t.Run("adds_k6_labels_from_baggage", func(t *testing.T) {
		req := httptest.NewRequest("GET", "http://example.com", nil)
		req = testAddBaggageToRequest(t, req,
			"k6.test_run_id", "123",
			"not_k6.some_other_key", "value",
		)

		handler := LabelsFromBaggageHandler(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			b := baggage.FromContext(r.Context())
			require.NotNil(t, b)
			testAssertEqualMembers(t, b.Members(),
				"k6.test_run_id", "123",
				"not_k6.some_other_key", "value",
			)

			val, ok := pprof.Label(r.Context(), "k6_test_run_id")
			require.True(t, ok)
			require.Equal(t, "123", val)

			_, ok = pprof.Label(r.Context(), "not_k6_some_other_key")
			require.False(t, ok)
		}))

		handler.ServeHTTP(httptest.NewRecorder(), req)
	})

	t.Run("passthrough_requests_with_no_baggage", func(t *testing.T) {
		req := httptest.NewRequest("GET", "http://example.com", nil)

		handler := LabelsFromBaggageHandler(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			b := baggage.FromContext(r.Context())
			require.Equal(t, 0, b.Len())
		}))

		handler.ServeHTTP(httptest.NewRecorder(), req)
	})

	t.Run("passthrough_requests_with_no_k6_baggage", func(t *testing.T) {
		req := httptest.NewRequest("GET", "http://example.com", nil)
		req = testAddBaggageToRequest(t, req,
			"not_k6.some_other_key", "value",
		)

		handler := LabelsFromBaggageHandler(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			b := baggage.FromContext(r.Context())
			require.NotNil(t, b)
			testAssertEqualMembers(t, b.Members(),
				"not_k6.some_other_key", "value",
			)

			_, ok := pprof.Label(r.Context(), "not_k6_some_other_key")
			require.False(t, ok)
		}))

		handler.ServeHTTP(httptest.NewRecorder(), req)
	})
}

func TestLabelsFromBaggageUnaryInterceptor(t *testing.T) {
	info := &grpc.UnaryServerInfo{
		FullMethod: "/example.ExampleService/Test",
	}

	t.Run("adds_k6_labels_from_grpc_baggage", func(t *testing.T) {
		testCtx := testAddBaggageToGRPCRequest(t, context.Background(),
			"k6.test_run_id", "123",
			"not_k6.some_other_key", "value",
		)

		handler := func(ctx context.Context, req interface{}) (interface{}, error) {
			require.Equal(t, "test-request", req)

			b := baggage.FromContext(ctx)
			require.NotNil(t, b)
			testAssertEqualMembers(t, b.Members(),
				"k6.test_run_id", "123",
				"not_k6.some_other_key", "value",
			)

			val, ok := pprof.Label(ctx, "k6_test_run_id")
			require.True(t, ok)
			require.Equal(t, "123", val)

			_, ok = pprof.Label(ctx, "not_k6_some_other_key")
			require.False(t, ok)

			return "test-response", nil
		}

		res, err := LabelsFromBaggageUnaryInterceptor(testCtx, "test-request", info, handler)
		require.NoError(t, err)
		require.Equal(t, "test-response", res)
	})

	t.Run("passthrough_requests_with_no_baggage", func(t *testing.T) {
		testCtx := testAddBaggageToGRPCRequest(t, context.Background())

		handler := func(ctx context.Context, req interface{}) (interface{}, error) {
			require.Equal(t, "test-request", req)

			b := baggage.FromContext(ctx)
			require.NotNil(t, b)
			require.Equal(t, 0, b.Len())

			return "test-response", nil
		}

		res, err := LabelsFromBaggageUnaryInterceptor(testCtx, "test-request", info, handler)
		require.NoError(t, err)
		require.Equal(t, "test-response", res)
	})

	t.Run("passthrough_requests_with_no_k6_baggage", func(t *testing.T) {
		testCtx := testAddBaggageToGRPCRequest(t, context.Background(),
			"not_k6.some_other_key", "value",
		)

		handler := func(ctx context.Context, req interface{}) (interface{}, error) {
			require.Equal(t, "test-request", req)

			b := baggage.FromContext(ctx)
			require.NotNil(t, b)
			testAssertEqualMembers(t, b.Members(),
				"not_k6.some_other_key", "value",
			)

			_, ok := pprof.Label(ctx, "not_k6_some_other_key")
			require.False(t, ok)

			return "test-response", nil
		}

		res, err := LabelsFromBaggageUnaryInterceptor(testCtx, "test-request", info, handler)
		require.NoError(t, err)
		require.Equal(t, "test-response", res)
	})
}

func TestLabelsFromBaggageStreamInterceptor(t *testing.T) {
	info := &grpc.StreamServerInfo{
		FullMethod: "/example.ExampleService/Test",
	}

	t.Run("adds_k6_labels_from_grpc_baggage", func(t *testing.T) {
		testCtx := testAddBaggageToGRPCRequest(t, context.Background(),
			"k6.test_run_id", "123",
			"not_k6.some_other_key", "value",
		)

		handler := func(srv any, stream grpc.ServerStream) error {
			ctx := stream.Context()

			b := baggage.FromContext(ctx)
			require.NotNil(t, b)
			testAssertEqualMembers(t, b.Members(),
				"k6.test_run_id", "123",
				"not_k6.some_other_key", "value",
			)

			val, ok := pprof.Label(ctx, "k6_test_run_id")
			require.True(t, ok)
			require.Equal(t, "123", val)

			_, ok = pprof.Label(ctx, "not_k6_some_other_key")
			require.False(t, ok)

			return nil
		}

		err := LabelsFromBaggageStreamInterceptor(nil, &grpcmiddleware.WrappedServerStream{WrappedContext: testCtx}, info, handler)
		require.NoError(t, err)
	})

	t.Run("passthrough_requests_with_no_baggage", func(t *testing.T) {
		testCtx := testAddBaggageToGRPCRequest(t, context.Background())

		handler := func(srv any, stream grpc.ServerStream) error {
			ctx := stream.Context()

			b := baggage.FromContext(ctx)
			require.NotNil(t, b)
			require.Equal(t, 0, b.Len())

			return nil
		}

		err := LabelsFromBaggageStreamInterceptor(nil, &grpcmiddleware.WrappedServerStream{WrappedContext: testCtx}, info, handler)
		require.NoError(t, err)
	})

	t.Run("passthrough_requests_with_no_k6_baggage", func(t *testing.T) {
		testCtx := testAddBaggageToGRPCRequest(t, context.Background(),
			"not_k6.some_other_key", "value",
		)

		handler := func(srv any, stream grpc.ServerStream) error {
			ctx := stream.Context()

			b := baggage.FromContext(ctx)
			require.NotNil(t, b)
			testAssertEqualMembers(t, b.Members(),
				"not_k6.some_other_key", "value",
			)

			_, ok := pprof.Label(ctx, "not_k6_some_other_key")
			require.False(t, ok)

			return nil
		}

		err := LabelsFromBaggageStreamInterceptor(nil, &grpcmiddleware.WrappedServerStream{WrappedContext: testCtx}, info, handler)
		require.NoError(t, err)
	})
}

func Test_setBaggageContextFromHeader(t *testing.T) {
	t.Run("sets_baggage_context", func(t *testing.T) {
		req := httptest.NewRequest("GET", "http://example.com", nil)
		req = testAddBaggageToRequest(t, req,
			"k6.test_run_id", "123",
			"not_k6.some_other_key", "value",
		)

		req, found := setBaggageContextFromHeader(req)
		require.True(t, found)

		b := baggage.FromContext(req.Context())
		testAssertEqualMembers(t, b.Members(),
			"k6.test_run_id", "123",

			// Also passthrough non-k6 baggage. We should avoid clobbering
			// other baggage members that the system might also be using.
			"not_k6.some_other_key", "value",
		)
	})

	t.Run("does_not_set_baggage_context_with_no_baggage", func(t *testing.T) {
		req := httptest.NewRequest("GET", "http://example.com", nil)

		req, found := setBaggageContextFromHeader(req)
		require.False(t, found)

		b := baggage.FromContext(req.Context())
		require.Equal(t, 0, b.Len())
	})

	t.Run("does_not_set_baggage_context_invalid_baggage", func(t *testing.T) {
		req := httptest.NewRequest("GET", "http://example.com", nil)
		req.Header.Add("Baggage", "invalid")

		req, found := setBaggageContextFromHeader(req)
		require.False(t, found)

		b := baggage.FromContext(req.Context())
		require.Equal(t, 0, b.Len())
	})
}

func Test_getBaggageLabels(t *testing.T) {
	t.Run("with_k6_baggage", func(t *testing.T) {
		req := httptest.NewRequest("GET", "http://example.com", nil)
		req = testAddBaggageToRequest(t, req,
			"k6.test_run_id", "123",
			"not_k6.some_other_key", "value",
		)

		labelSet := getBaggageLabelsFromContext(req.Context())
		require.NotNil(t, labelSet)

		gotLabels := testPprofLabelsToMap(t, *labelSet)
		expectedLabels := map[string]string{
			"k6_test_run_id": "123",
		}

		require.Equal(t, expectedLabels, gotLabels)
	})

	t.Run("empty_values_are_skipped", func(t *testing.T) {
		req := httptest.NewRequest("GET", "http://example.com", nil)
		req = testAddBaggageToRequest(t, req)

		labelSet := getBaggageLabelsFromContext(req.Context())
		require.Nil(t, labelSet)
	})

	t.Run("skips_missing_baggage_header", func(t *testing.T) {
		req := httptest.NewRequest("GET", "http://example.com", nil)

		labelSet := getBaggageLabelsFromContext(req.Context())
		require.Nil(t, labelSet)
	})

	t.Run("skips_invalid_baggage_header", func(t *testing.T) {
		req := httptest.NewRequest("GET", "http://example.com", nil)
		req.Header.Add("Baggage", "invalid")

		labelSet := getBaggageLabelsFromContext(req.Context())
		require.Nil(t, labelSet)
	})
}

func Test_baggageToLabels(t *testing.T) {
	t.Run("with_k6_baggage", func(t *testing.T) {
		b := testMustNewBaggage(t,
			"k6.test_run_id", "123",
			"not_k6.some_other_key", "value",
		)

		labelSet := baggageToLabels(b)
		require.NotNil(t, labelSet)

		gotLabels := testPprofLabelsToMap(t, *labelSet)
		expectedLabels := map[string]string{
			"k6_test_run_id": "123",
		}

		require.Equal(t, expectedLabels, gotLabels)
	})

	t.Run("with_empty_baggage", func(t *testing.T) {
		b := testMustNewBaggage(t)

		labelSet := baggageToLabels(b)
		require.Nil(t, labelSet)
	})

	t.Run("with_no_k6_baggage", func(t *testing.T) {
		b := testMustNewBaggage(t,
			"not_k6.some_other_key", "value",
		)

		labelSet := baggageToLabels(b)
		require.Nil(t, labelSet)
	})
}
func Test_setBaggageContextFromMetadata(t *testing.T) {
	t.Run("sets_baggage_context", func(t *testing.T) {
		ctx := testAddBaggageToGRPCRequest(t, context.Background(),
			"k6.test_run_id", "123",
			"not_k6.some_other_key", "value",
		)

		ctx, found := setBaggageContextFromMetadata(ctx)
		require.True(t, found)

		b := baggage.FromContext(ctx)
		testAssertEqualMembers(t, b.Members(),
			"k6.test_run_id", "123",
			"not_k6.some_other_key", "value",
		)
	})

	t.Run("does_not_set_baggage_context_with_no_baggage", func(t *testing.T) {
		ctx := context.Background()

		ctx, found := setBaggageContextFromMetadata(ctx)
		require.False(t, found)

		b := baggage.FromContext(ctx)
		require.Equal(t, 0, b.Len())
	})
}

func Test_getBaggageLabelsFromContext(t *testing.T) {
	t.Run("with_k6_baggage", func(t *testing.T) {
		ctx := testAddBaggageToRequest(t, httptest.NewRequest("GET", "http://example.com", nil),
			"k6.test_run_id", "123",
			"not_k6.some_other_key", "value",
		).Context()

		labelSet := getBaggageLabelsFromContext(ctx)
		require.NotNil(t, labelSet)

		gotLabels := testPprofLabelsToMap(t, *labelSet)
		expectedLabels := map[string]string{
			"k6_test_run_id": "123",
		}

		require.Equal(t, expectedLabels, gotLabels)
	})

	t.Run("empty_values_are_skipped", func(t *testing.T) {
		ctx := testAddBaggageToRequest(t, httptest.NewRequest("GET", "http://example.com", nil)).Context()

		labelSet := getBaggageLabelsFromContext(ctx)
		require.Nil(t, labelSet)
	})

	t.Run("skips_missing_baggage_header", func(t *testing.T) {
		ctx := httptest.NewRequest("GET", "http://example.com", nil).Context()

		labelSet := getBaggageLabelsFromContext(ctx)
		require.Nil(t, labelSet)
	})
}

func testAddBaggageToRequest(t *testing.T, req *http.Request, kvPairs ...string) *http.Request {
	t.Helper()

	require.Equal(t, 0, len(kvPairs)%2, "kvPairs must be a multiple of 2")

	members := make([]baggage.Member, 0, len(kvPairs)/2)
	for i := 0; i < len(kvPairs); i += 2 {
		key := kvPairs[i]
		value := kvPairs[i+1]

		member, err := baggage.NewMember(key, value)
		require.NoError(t, err)

		members = append(members, member)
	}

	b, err := baggage.New(members...)
	require.NoError(t, err)

	ctx := baggage.ContextWithBaggage(req.Context(), b)
	req = req.WithContext(ctx)
	req.Header.Add("Baggage", b.String())

	return req
}

func testAddBaggageToGRPCRequest(t *testing.T, ctx context.Context, kvPairs ...string) context.Context {
	t.Helper()

	require.Equal(t, 0, len(kvPairs)%2, "kvPairs must be a multiple of 2")

	members := make([]baggage.Member, 0, len(kvPairs)/2)
	for i := 0; i < len(kvPairs); i += 2 {
		key := kvPairs[i]
		value := kvPairs[i+1]
		members = append(members, testMustNewMember(t, key, value))
	}

	b, err := baggage.New(members...)
	require.NoError(t, err)

	ctx = baggage.ContextWithBaggage(ctx, b)
	return metadata.NewIncomingContext(ctx, metadata.New(map[string]string{
		"Baggage": b.String(),
	}))
}

func testMustNewBaggage(t *testing.T, kvPairs ...string) baggage.Baggage {
	t.Helper()

	require.Equal(t, 0, len(kvPairs)%2, "kvPairs must be a multiple of 2")

	members := make([]baggage.Member, 0, len(kvPairs)/2)
	for i := 0; i < len(kvPairs); i += 2 {
		key := kvPairs[i]
		value := kvPairs[i+1]
		members = append(members, testMustNewMember(t, key, value))
	}

	b, err := baggage.New(members...)
	require.NoError(t, err)

	return b
}

func testMustNewMember(t *testing.T, key string, value string) baggage.Member {
	t.Helper()

	member, err := baggage.NewMember(key, value)
	require.NoError(t, err)

	return member
}

// testAssertEqualMembers verifies the two slices of Members are equal by
// sorting them and comparing them as pairs of key-value strings.
//
// This is necessary because Baggage.Members() returns an unordered slice of
// Members.
func testAssertEqualMembers(t *testing.T, got []baggage.Member, wants ...string) {
	t.Helper()

	type Pair struct {
		Key   string
		Value string
	}

	require.Equal(t, 0, len(wants)%2, "wants must be a multiple of 2")
	require.Equal(t, len(wants)/2, len(got))

	wantPairs := make([]Pair, 0, len(wants)/2)
	for i := 0; i < len(wants); i += 2 {
		key := wants[i]
		value := wants[i+1]

		wantPairs = append(wantPairs, Pair{
			Key:   key,
			Value: value,
		})
	}

	gotPairs := make([]Pair, 0, len(got))
	for _, m := range got {
		gotPairs = append(gotPairs, Pair{m.Key(), m.Value()})
	}

	sort.Slice(wantPairs, func(i, j int) bool {
		return wantPairs[i].Key < wantPairs[j].Key
	})
	sort.Slice(gotPairs, func(i, j int) bool {
		return gotPairs[i].Key < gotPairs[j].Key
	})

	require.Equal(t, wantPairs, gotPairs)
}

func testPprofLabelsToMap(t *testing.T, labelSet pprof.LabelSet) map[string]string {
	t.Helper()

	gotLabels := map[string]string{}
	ctx := pprof.WithLabels(context.Background(), labelSet)
	pprof.ForLabels(ctx, func(key, value string) bool {
		gotLabels[key] = value
		return true
	})

	return gotLabels
}
```

## File: `x/k6/go.mod`
```
module github.com/grafana/pyroscope-go/x/k6

go 1.24.0

toolchain go1.24.13

replace github.com/grafana/pyroscope-go => ../../

require (
	github.com/grafana/pyroscope-go v1.1.1
	github.com/grpc-ecosystem/go-grpc-middleware/v2 v2.3.0
	github.com/stretchr/testify v1.11.1
	go.opentelemetry.io/otel v1.39.0
	google.golang.org/grpc v1.79.3
)

require (
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/grafana/pyroscope-go/godeltaprof v0.1.9 // indirect
	github.com/klauspost/compress v1.17.8 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	github.com/rogpeppe/go-internal v1.9.0 // indirect
	golang.org/x/net v0.48.0 // indirect
	golang.org/x/sys v0.39.0 // indirect
	golang.org/x/text v0.32.0 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20251202230838-ff82c1b0f217 // indirect
	google.golang.org/protobuf v1.36.10 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
```

## File: `x/k6/go.sum`
```
github.com/cespare/xxhash/v2 v2.3.0 h1:UL815xU9SqsFlibzuggzjXhog7bL6oX9BbNZnL2UFvs=
github.com/cespare/xxhash/v2 v2.3.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/go-logr/logr v1.4.3 h1:CjnDlHq8ikf6E492q6eKboGOC0T8CDaOvkHCIg8idEI=
github.com/go-logr/logr v1.4.3/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
github.com/go-logr/stdr v1.2.2 h1:hSWxHoqTgW2S2qGc0LTAI563KZ5YKYRhT3MFKZMbjag=
github.com/go-logr/stdr v1.2.2/go.mod h1:mMo/vtBO5dYbehREoey6XUKy/eSumjCCveDpRre4VKE=
github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek=
github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/grafana/pyroscope-go/godeltaprof v0.1.9 h1:c1Us8i6eSmkW+Ez05d3co8kasnuOY813tbMN8i/a3Og=
github.com/grafana/pyroscope-go/godeltaprof v0.1.9/go.mod h1:2+l7K7twW49Ct4wFluZD3tZ6e0SjanjcUUBPVD/UuGU=
github.com/grpc-ecosystem/go-grpc-middleware/v2 v2.3.0 h1:FbSCl+KggFl+Ocym490i/EyXF4lPgLoUtcSWquBM0Rs=
github.com/grpc-ecosystem/go-grpc-middleware/v2 v2.3.0/go.mod h1:qOchhhIlmRcqk/O9uCo/puJlyo07YINaIqdZfZG3Jkc=
github.com/klauspost/compress v1.17.8 h1:YcnTYrq7MikUT7k0Yb5eceMmALQPYBW/Xltxn0NAMnU=
github.com/klauspost/compress v1.17.8/go.mod h1:Di0epgTjJY877eYKx5yC51cX2A2Vl2ibi7bDH9ttBbw=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rogpeppe/go-internal v1.9.0 h1:73kH8U+JUqXU8lRuOHeVHaa/SZPifC7BkcraZVejAe8=
github.com/rogpeppe/go-internal v1.9.0/go.mod h1:WtVeX8xhTBvf0smdhujwtBcq4Qrzq/fJaraNFVN+nFs=
github.com/stretchr/objx v0.5.2 h1:xuMeJ0Sdp5ZMRXx/aWO6RZxdr3beISkG5/G/aIRr3pY=
github.com/stretchr/objx v0.5.2/go.mod h1:FRsXN1f5AsAjCGJKqEizvkpNtU+EGNCLh3NxZ/8L+MA=
github.com/stretchr/testify v1.11.1 h1:7s2iGBzp5EwR7/aIZr8ao5+dra3wiQyKjjFuvgVKu7U=
github.com/stretchr/testify v1.11.1/go.mod h1:wZwfW3scLgRK+23gO65QZefKpKQRnfz6sD981Nm4B6U=
go.opentelemetry.io/auto/sdk v1.2.1 h1:jXsnJ4Lmnqd11kwkBV2LgLoFMZKizbCi5fNZ/ipaZ64=
go.opentelemetry.io/auto/sdk v1.2.1/go.mod h1:KRTj+aOaElaLi+wW1kO/DZRXwkF4C5xPbEe3ZiIhN7Y=
go.opentelemetry.io/otel v1.39.0 h1:8yPrr/S0ND9QEfTfdP9V+SiwT4E0G7Y5MO7p85nis48=
go.opentelemetry.io/otel v1.39.0/go.mod h1:kLlFTywNWrFyEdH0oj2xK0bFYZtHRYUdv1NklR/tgc8=
go.opentelemetry.io/otel/metric v1.39.0 h1:d1UzonvEZriVfpNKEVmHXbdf909uGTOQjA0HF0Ls5Q0=
go.opentelemetry.io/otel/metric v1.39.0/go.mod h1:jrZSWL33sD7bBxg1xjrqyDjnuzTUB0x1nBERXd7Ftcs=
go.opentelemetry.io/otel/sdk v1.39.0 h1:nMLYcjVsvdui1B/4FRkwjzoRVsMK8uL/cj0OyhKzt18=
go.opentelemetry.io/otel/sdk v1.39.0/go.mod h1:vDojkC4/jsTJsE+kh+LXYQlbL8CgrEcwmt1ENZszdJE=
go.opentelemetry.io/otel/sdk/metric v1.39.0 h1:cXMVVFVgsIf2YL6QkRF4Urbr/aMInf+2WKg+sEJTtB8=
go.opentelemetry.io/otel/sdk/metric v1.39.0/go.mod h1:xq9HEVH7qeX69/JnwEfp6fVq5wosJsY1mt4lLfYdVew=
go.opentelemetry.io/otel/trace v1.39.0 h1:2d2vfpEDmCJ5zVYz7ijaJdOF59xLomrvj7bjt6/qCJI=
go.opentelemetry.io/otel/trace v1.39.0/go.mod h1:88w4/PnZSazkGzz/w84VHpQafiU4EtqqlVdxWy+rNOA=
golang.org/x/net v0.48.0 h1:zyQRTTrjc33Lhh0fBgT/H3oZq9WuvRR5gPC70xpDiQU=
golang.org/x/net v0.48.0/go.mod h1:+ndRgGjkh8FGtu1w1FGbEC31if4VrNVMuKTgcAAnQRY=
golang.org/x/sys v0.39.0 h1:CvCKL8MeisomCi6qNZ+wbb0DN9E5AATixKsvNtMoMFk=
golang.org/x/sys v0.39.0/go.mod h1:OgkHotnGiDImocRcuBABYBEXf8A9a87e/uXjp9XT3ks=
golang.org/x/text v0.32.0 h1:ZD01bjUt1FQ9WJ0ClOL5vxgxOI/sVCNgX1YtKwcY0mU=
golang.org/x/text v0.32.0/go.mod h1:o/rUWzghvpD5TXrTIBuJU77MTaN0ljMWE47kxGJQ7jY=
gonum.org/v1/gonum v0.16.0 h1:5+ul4Swaf3ESvrOnidPp4GZbzf0mxVQpDCYUQE7OJfk=
gonum.org/v1/gonum v0.16.0/go.mod h1:fef3am4MQ93R2HHpKnLk4/Tbh/s0+wqD5nfa6Pnwy4E=
google.golang.org/genproto/googleapis/rpc v0.0.0-20251202230838-ff82c1b0f217 h1:gRkg/vSppuSQoDjxyiGfN4Upv/h/DQmIR10ZU8dh4Ww=
google.golang.org/genproto/googleapis/rpc v0.0.0-20251202230838-ff82c1b0f217/go.mod h1:7i2o+ce6H/6BluujYR+kqX3GKH+dChPTQU19wjRPiGk=
google.golang.org/grpc v1.79.3 h1:sybAEdRIEtvcD68Gx7dmnwjZKlyfuc61Dyo9pGXXkKE=
google.golang.org/grpc v1.79.3/go.mod h1:KmT0Kjez+0dde/v2j9vzwoAScgEPx/Bw1CYChhHLrHQ=
google.golang.org/protobuf v1.36.10 h1:AYd7cD/uASjIL6Q9LiTjz8JLcrh/88q5UObnmY3aOOE=
google.golang.org/protobuf v1.36.10/go.mod h1:HTf+CrKn2C3g5S8VImy6tdcUvCska2kB7j23XfzDpco=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `x/k6/go.work`
```
go 1.24.0

toolchain go1.24.13

use (
	.
	../..
)
```

## File: `x/k6/go.work.sum`
```
buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go v1.36.4-20250130201111-63bb56e20495.1 h1:4erM3WLgEG/HIBrpBDmRbs1puhd7p0z7kNXDuhHthwM=
buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go v1.36.4-20250130201111-63bb56e20495.1/go.mod h1:novQBstnxcGpfKf8qGRATqn1anQKwMJIbH5Q581jibU=
cel.dev/expr v0.16.0 h1:yloc84fytn4zmJX2GU3TkXGsaieaV7dQ057Qs4sIG2Y=
cel.dev/expr v0.16.0/go.mod h1:TRSuuV7DlVCE/uwv5QbAiW/v8l5O8C4eEPHeu7gf7Sg=
cel.dev/expr v0.19.1 h1:NciYrtDRIR0lNCnH1LFJegdjspNx9fI59O7TWcua/W4=
cel.dev/expr v0.19.1/go.mod h1:MrpN08Q+lEBs+bGYdLxxHkZoUSsCp0nSKTs0nTymJgw=
cel.dev/expr v0.25.1 h1:1KrZg61W6TWSxuNZ37Xy49ps13NUovb66QLprthtwi4=
cel.dev/expr v0.25.1/go.mod h1:hrXvqGP6G6gyx8UAHSHJ5RGk//1Oj5nXQ2NI02Nrsg4=
cloud.google.com/go v0.26.0 h1:e0WKqKTd5BnrG8aKH3J3h+QvEIQtSUcf2n5UZ5ZgLtQ=
cloud.google.com/go v0.115.0 h1:CnFSK6Xo3lDYRoBKEcAtia6VSC837/ZkJuRduSFnr14=
cloud.google.com/go v0.115.0/go.mod h1:8jIM5vVgoAEoiVxQ/O4BFTfHqulPZgs/ufEzMcFMdWU=
cloud.google.com/go/accessapproval v1.7.11 h1:MgtE8CI+YJWPGGHnxQ9z1VQqV87h+vSGy2MeM/m0ggQ=
cloud.google.com/go/accessapproval v1.7.11/go.mod h1:KGK3+CLDWm4BvjN0wFtZqdFUGhxlTvTF6PhAwQJGL4M=
cloud.google.com/go/accesscontextmanager v1.8.11 h1:IQ3KLJmNKPgstN0ZcRw0niU4KfsiOZmzvcGCF+NT618=
cloud.google.com/go/accesscontextmanager v1.8.11/go.mod h1:nwPysISS3KR5qXipAU6cW/UbDavDdTBBgPohbkhGSok=
cloud.google.com/go/aiplatform v1.68.0 h1:EPPqgHDJpBZKRvv+OsB3cr0jYz3EL2pZ+802rBPcG8U=
cloud.google.com/go/aiplatform v1.68.0/go.mod h1:105MFA3svHjC3Oazl7yjXAmIR89LKhRAeNdnDKJczME=
cloud.google.com/go/analytics v0.23.6 h1:BY8ZY7hQwKBi+lNp1IkiMTOK4xe4lxZCeYv3S9ARXtE=
cloud.google.com/go/analytics v0.23.6/go.mod h1:cFz5GwWHrWQi8OHKP9ep3Z4pvHgGcG9lPnFQ+8kXsNo=
cloud.google.com/go/apigateway v1.6.11 h1:VtEvpnqqY2T5gZBzo+p7C87yGH3omHUkPIbRQkmGS9I=
cloud.google.com/go/apigateway v1.6.11/go.mod h1:4KsrYHn/kSWx8SNUgizvaz+lBZ4uZfU7mUDsGhmkWfM=
cloud.google.com/go/apigeeconnect v1.6.11 h1:CftZgGXFRLJeD2/5ZIdWuAMxW/88UG9tHhRPI/NY75M=
cloud.google.com/go/apigeeconnect v1.6.11/go.mod h1:iMQLTeKxtKL+sb0D+pFlS/TO6za2IUOh/cwMEtn/4g0=
cloud.google.com/go/apigeeregistry v0.8.9 h1:3vLwk0tS9L++6ZyV4RDH4UCydfVoqxJbpWvqG6MTtUw=
cloud.google.com/go/apigeeregistry v0.8.9/go.mod h1:4XivwtSdfSO16XZdMEQDBCMCWDp3jkCBRhVgamQfLSA=
cloud.google.com/go/appengine v1.8.11 h1:ZLoWWwakgRzRnXX2bsgk2g1sdzti3wq+ebunTJsZNog=
cloud.google.com/go/appengine v1.8.11/go.mod h1:xET3coaDUj+OP4TgnZlgQ+rG2R9fG2nblya13czP56Q=
cloud.google.com/go/area120 v0.8.11 h1:UID1dl7lW2zs8OpYVtVZ5WsXU9kUcxC1nd3nnToHW70=
cloud.google.com/go/area120 v0.8.11/go.mod h1:VBxJejRAJqeuzXQBbh5iHBYUkIjZk5UzFZLCXmzap2o=
cloud.google.com/go/artifactregistry v1.14.13 h1:NNK4vYVA5NGQmbmYidfJhnfmYU6SSSRUM2oopNouJNs=
cloud.google.com/go/artifactregistry v1.14.13/go.mod h1:zQ/T4xoAFPtcxshl+Q4TJBgsy7APYR/BLd2z3xEAqRA=
cloud.google.com/go/asset v1.19.5 h1:/R2XZS6lR8oj/Y3L+epD2yy7mf44Zp62H4xZ4vzaR/Y=
cloud.google.com/go/asset v1.19.5/go.mod h1:sqyLOYaLLfc4ACcn3YxqHno+J7lRt9NJTdO50zCUcY0=
cloud.google.com/go/assuredworkloads v1.11.11 h1:pwZp9o8aF5QmX4Z0YNlRe1ZOUzDw0UALmkem3aPobZc=
cloud.google.com/go/assuredworkloads v1.11.11/go.mod h1:vaYs6+MHqJvLKYgZBOsuuOhBgNNIguhRU0Kt7JTGcnI=
cloud.google.com/go/automl v1.13.11 h1:FBCLjGS+Did/wtRHqyS055bRs/EJXx3meTvHPcdZgk8=
cloud.google.com/go/automl v1.13.11/go.mod h1:oMJdXRDOVC+Eq3PnGhhxSut5Hm9TSyVx1aLEOgerOw8=
cloud.google.com/go/baremetalsolution v1.2.10 h1:VvBiXT9QJ4VpNVyfzHhLScY1aymZxpQgOa20yUvgphw=
cloud.google.com/go/baremetalsolution v1.2.10/go.mod h1:eO2c2NMRy5ytcNPhG78KPsWGNsX5W/tUsCOWmYihx6I=
cloud.google.com/go/batch v1.9.2 h1:o1RAjc0ExGAAm41YB9LbJZyJDgZR4M6SKyITsd/Smr4=
cloud.google.com/go/batch v1.9.2/go.mod h1:smqwS4sleDJVAEzBt/TzFfXLktmWjFNugGDWl8coKX4=
cloud.google.com/go/beyondcorp v1.0.10 h1:K4blSIQZn3YO4F4LmvWrH52pb8Y0L3NOrwkf22+x67M=
cloud.google.com/go/beyondcorp v1.0.10/go.mod h1:G09WxvxJASbxbrzaJUMVvNsB1ZiaKxpbtkjiFtpDtbo=
cloud.google.com/go/bigquery v1.62.0 h1:SYEA2f7fKqbSRRBHb7g0iHTtZvtPSPYdXfmqsjpsBwo=
cloud.google.com/go/bigquery v1.62.0/go.mod h1:5ee+ZkF1x/ntgCsFQJAQTM3QkAZOecfCmvxhkJsWRSA=
cloud.google.com/go/bigtable v1.27.2-0.20240802230159-f371928b558f h1:UR2/6M/bSN8PPQlhaq+57w21VZLcEvq4ujsHd1p/G2s=
cloud.google.com/go/bigtable v1.27.2-0.20240802230159-f371928b558f/go.mod h1:avmXcmxVbLJAo9moICRYMgDyTTPoV0MA0lHKnyqV4fQ=
cloud.google.com/go/billing v1.18.9 h1:sGRWx7PvsfHuZyx151Xr6CrORIgjvCMO4GRabihSdQQ=
cloud.google.com/go/billing v1.18.9/go.mod h1:bKTnh8MBfCMUT1fzZ936CPN9rZG7ZEiHB2J3SjIjByc=
cloud.google.com/go/binaryauthorization v1.8.7 h1:ItT9uR/0/ok2Ru3LCcbSIBUPsKqTA49ZmxCupqQaeFo=
cloud.google.com/go/binaryauthorization v1.8.7/go.mod h1:cRj4teQhOme5SbWQa96vTDATQdMftdT5324BznxANtg=
cloud.google.com/go/certificatemanager v1.8.5 h1:ASC9N81NU8JnGzi9kiY2QTqtTgOziwGv48sjt3YG420=
cloud.google.com/go/certificatemanager v1.8.5/go.mod h1:r2xINtJ/4xSz85VsqvjY53qdlrdCjyniib9Jp98ZKKM=
cloud.google.com/go/channel v1.17.11 h1:AkKyMl2pSoJxBQtjAd6LYOtMgOaCl/kuiKoSg/Gf/H4=
cloud.google.com/go/channel v1.17.11/go.mod h1:gjWCDBcTGQce/BSMoe2lAqhlq0dIRiZuktvBKXUawp0=
cloud.google.com/go/cloudbuild v1.16.5 h1:RvK5r8JBCLNg9XmfGPy05t3bmhLJV3Xh3sDHGHAATgM=
cloud.google.com/go/cloudbuild v1.16.5/go.mod h1:HXLpZ8QeYZgmDIWpbl9Gs22p6o6uScgQ/cV9HF9cIZU=
cloud.google.com/go/clouddms v1.7.10 h1:EA3y9v5TZiAlwgHJh2vPOEelqYiCxXBYZRCNnGK5q+g=
cloud.google.com/go/clouddms v1.7.10/go.mod h1:PzHELq0QDyA7VaD9z6mzh2mxeBz4kM6oDe8YxMxd4RA=
cloud.google.com/go/cloudtasks v1.12.12 h1:p91Brp4nJkyRRI/maYdO+FT+e9tU+2xoGr20s2rvalU=
cloud.google.com/go/cloudtasks v1.12.12/go.mod h1:8UmM+duMrQpzzRREo0i3x3TrFjsgI/3FQw3664/JblA=
cloud.google.com/go/compute v1.27.4 h1:XM8ulx6crjdl09XBfji7viFgZOEQuIxBwKmjRH9Rtmc=
cloud.google.com/go/compute v1.27.4/go.mod h1:7JZS+h21ERAGHOy5qb7+EPyXlQwzshzrx1x6L9JhTqU=
cloud.google.com/go/compute/metadata v0.5.0 h1:Zr0eK8JbFv6+Wi4ilXAR8FJ3wyNdpxHKJNPos6LTZOY=
cloud.google.com/go/compute/metadata v0.5.0/go.mod h1:aHnloV2TPI38yx4s9+wAZhHykWvVCfu7hQbF+9CWoiY=
cloud.google.com/go/compute/metadata v0.9.0 h1:pDUj4QMoPejqq20dK0Pg2N4yG9zIkYGdBtwLoEkH9Zs=
cloud.google.com/go/compute/metadata v0.9.0/go.mod h1:E0bWwX5wTnLPedCKqk3pJmVgCBSM6qQI1yTBdEb3C10=
cloud.google.com/go/contactcenterinsights v1.13.6 h1:LRcI5RAlLIbjwT312sGt+gyXcaXTr+v7uEQlNyArO9g=
cloud.google.com/go/contactcenterinsights v1.13.6/go.mod h1:mL+DbN3pMQGaAbDC4wZhryLciwSwHf5Tfk4Itr72Zyk=
cloud.google.com/go/container v1.38.0 h1:GP5zLamfvPZeOTifnGBSER/br76D5eJ97xhcXXrh5tM=
cloud.google.com/go/container v1.38.0/go.mod h1:U0uPBvkVWOJGY/0qTVuPS7NeafFEUsHSPqT5pB8+fCY=
cloud.google.com/go/containeranalysis v0.12.1 h1:Xb8Eu7vVmWR5nAl5WPTGTx/dCr+R+oF7VbuYV47EHHs=
cloud.google.com/go/containeranalysis v0.12.1/go.mod h1:+/lcJIQSFt45TC0N9Nq7/dPbl0isk6hnC4EvBBqyXsM=
cloud.google.com/go/datacatalog v1.21.0 h1:vl0pQT9TZ5rKi9e69FgtXNCR7I8MVRj4+CnbeXhz6UQ=
cloud.google.com/go/datacatalog v1.21.0/go.mod h1:DB0QWF9nelpsbB0eR/tA0xbHZZMvpoFD1XFy3Qv/McI=
cloud.google.com/go/dataflow v0.9.11 h1:YIhStasKFDESaUdpnsHsp/5bACYL/yvW0OuZ6zPQ6nY=
cloud.google.com/go/dataflow v0.9.11/go.mod h1:CCLufd7I4pPfyp54qMgil/volrL2ZKYjXeYLfQmBGJs=
cloud.google.com/go/dataform v0.9.8 h1:oNtTx9PdH7aPnvrKIsPrh+Y6Mw+8Bw5/ZgLWVHAev/c=
cloud.google.com/go/dataform v0.9.8/go.mod h1:cGJdyVdunN7tkeXHPNosuMzmryx55mp6cInYBgxN3oA=
cloud.google.com/go/datafusion v1.7.11 h1:GVcVisjVKmoj1eNnIp3G3qjjo+7koHr0Kf8tF6Cjqe0=
cloud.google.com/go/datafusion v1.7.11/go.mod h1:aU9zoBHgYmoPp4dzccgm/Gi4xWDMXodSZlNZ4WNeptw=
cloud.google.com/go/datalabeling v0.8.11 h1:7jSuJEAc7upeMmyICzqfU0OyxUV38JSWW+8r5GmoHX0=
cloud.google.com/go/datalabeling v0.8.11/go.mod h1:6IGUV3z7hlkAU5ndKVshv/8z+7pxE+k0qXsEjyzO1Xg=
cloud.google.com/go/dataplex v1.18.2 h1:bIU1r1YnsX6P1qTnaRnah/STHoLJ3EHUZVCjJl2+1Eo=
cloud.google.com/go/dataplex v1.18.2/go.mod h1:NuBpJJMGGQn2xctX+foHEDKRbizwuiHJamKvvSteY3Q=
cloud.google.com/go/dataproc/v2 v2.5.3 h1:OgTfUARkF8AfkNmoyT0wyLLXNh4LbT3l55s5gUlvFOk=
cloud.google.com/go/dataproc/v2 v2.5.3/go.mod h1:RgA5QR7v++3xfP7DlgY3DUmoDSTaaemPe0ayKrQfyeg=
cloud.google.com/go/dataqna v0.8.11 h1:bEUidOYRS0EQ7qHbZtcnospuks72iTapboszXU9poz8=
cloud.google.com/go/dataqna v0.8.11/go.mod h1:74Icl1oFKKZXPd+W7YDtqJLa+VwLV6wZ+UF+sHo2QZQ=
cloud.google.com/go/datastore v1.17.1 h1:6Me8ugrAOAxssGhSo8im0YSuy4YvYk4mbGvCadAH5aE=
cloud.google.com/go/datastore v1.17.1/go.mod h1:mtzZ2HcVtz90OVrEXXGDc2pO4NM1kiBQy8YV4qGe0ZM=
cloud.google.com/go/datastream v1.10.10 h1:klGhjQCLoLIRHMzMFIqM73cPNKliGveqC+Vrms+ce6A=
cloud.google.com/go/datastream v1.10.10/go.mod h1:NqchuNjhPlISvWbk426/AU/S+Kgv7srlID9P5XOAbtg=
cloud.google.com/go/deploy v1.21.0 h1:/qnNETfztKemA9JmUBOrnH/rG/XFkHOBHygN1Vy5lkg=
cloud.google.com/go/deploy v1.21.0/go.mod h1:PaOfS47VrvmYnxG5vhHg0KU60cKeWcqyLbMBjxS8DW8=
cloud.google.com/go/dialogflow v1.55.0 h1:H28O0WAm2waHpNAz2n9jbv8FApfXxeKAkfHObdP2MMk=
cloud.google.com/go/dialogflow v1.55.0/go.mod h1:0u0hSlJiFpMkMpMNoFrQETwDjaRm8Q8hYKv+jz5JeRA=
cloud.google.com/go/dlp v1.16.0 h1:mYjBqgVjseYXlx1TOOFsxSeZLboqxxKR7TqRGOG9vIU=
cloud.google.com/go/dlp v1.16.0/go.mod h1:LtPZxZAenBXKzvWIOB2hdHIXuEcK0wW0En8//u+/nNA=
cloud.google.com/go/documentai v1.31.0 h1:YRkFK+0ZgEciz1svDkuL9fjbQLq8xvVa1d3NUlhO6B4=
cloud.google.com/go/documentai v1.31.0/go.mod h1:5ajlDvaPyl9tc+K/jZE8WtYIqSXqAD33Z1YAYIjfad4=
cloud.google.com/go/domains v0.9.11 h1:8peNiXtaMNIF9Wybci859M/yprFcEve1R2z08pErUBs=
cloud.google.com/go/domains v0.9.11/go.mod h1:efo5552kUyxsXEz30+RaoIS2lR7tp3M/rhiYtKXkhkk=
cloud.google.com/go/edgecontainer v1.2.5 h1:wTo0ulZDSsDzeoVjICJZjZMzZ1Nn9y//AwAQlXbaTbs=
cloud.google.com/go/edgecontainer v1.2.5/go.mod h1:OAb6tElD3F3oBujFAup14PKOs9B/lYobTb6LARmoACY=
cloud.google.com/go/errorreporting v0.3.1 h1:E/gLk+rL7u5JZB9oq72iL1bnhVlLrnfslrgcptjJEUE=
cloud.google.com/go/errorreporting v0.3.1/go.mod h1:6xVQXU1UuntfAf+bVkFk6nld41+CPyF2NSPCyXE3Ztk=
cloud.google.com/go/essentialcontacts v1.6.12 h1:JaQXS+qCFYs8yectfZHpzw4+NjTvFqTuDMCtfPzMvbw=
cloud.google.com/go/essentialcontacts v1.6.12/go.mod h1:UGhWTIYewH8Ma4wDRJp8cMAHUCeAOCKsuwd6GLmmQLc=
cloud.google.com/go/eventarc v1.13.10 h1:HVJmOVc+7eVFAqMpJRrq0nY0KlYBEBVZW7Gz7TxTio8=
cloud.google.com/go/eventarc v1.13.10/go.mod h1:KlCcOMApmUaqOEZUpZRVH+p0nnnsY1HaJB26U4X5KXE=
cloud.google.com/go/filestore v1.8.7 h1:LF9t5MClPyFJMuXdez/AjF1uyO9xHKUFF3GUqA+xFPI=
cloud.google.com/go/filestore v1.8.7/go.mod h1:dKfyH0YdPAKdYHqAR/bxZeil85Y5QmrEVQwIYuRjcXI=
cloud.google.com/go/firestore v1.16.0 h1:YwmDHcyrxVRErWcgxunzEaZxtNbc8QoFYA/JOEwDPgc=
cloud.google.com/go/firestore v1.16.0/go.mod h1:+22v/7p+WNBSQwdSwP57vz47aZiY+HrDkrOsJNhk7rg=
cloud.google.com/go/functions v1.16.6 h1:tPe3/48RpjcFk96VeB6jOKQpK8nliGJLsgjh6pUOyFQ=
cloud.google.com/go/functions v1.16.6/go.mod h1:wOzZakhMueNQaBUJdf0yjsJIe0GBRu+ZTvdSTzqHLs0=
cloud.google.com/go/gkebackup v1.5.4 h1:mufh0PNpvqbfLV+TcxzSGESX8jGBcjKgctldv7kwQns=
cloud.google.com/go/gkebackup v1.5.4/go.mod h1:V+llvHlRD0bCyrkYaAMJX+CHralceQcaOWjNQs8/Ymw=
cloud.google.com/go/gkeconnect v0.8.11 h1:4bZAzvqhuv1uP+i4yG9cEMQ6ggdP26nBVjUgroPU6IM=
cloud.google.com/go/gkeconnect v0.8.11/go.mod h1:ejHv5ehbceIglu1GsMwlH0nZpTftjxEY6DX7tvaM8gA=
cloud.google.com/go/gkehub v0.14.11 h1:hQkVCcOiW/vPVYsthvKl1nje430/TpdFfgeIuqcYVOA=
cloud.google.com/go/gkehub v0.14.11/go.mod h1:CsmDJ4qbBnSPkoBltEubK6qGOjG0xNfeeT5jI5gCnRQ=
cloud.google.com/go/gkemulticloud v1.2.4 h1:6zV05tyl37HoEjCGGY+zHFNxnKQCjvVpiqWAUVgGaEs=
cloud.google.com/go/gkemulticloud v1.2.4/go.mod h1:PjTtoKLQpIRztrL+eKQw8030/S4c7rx/WvHydDJlpGE=
cloud.google.com/go/gsuiteaddons v1.6.11 h1:zydWX0nVT0Ut/P1X25Sy+4Rqe2PH04IzhwlF1BJd8To=
cloud.google.com/go/gsuiteaddons v1.6.11/go.mod h1:U7mk5PLBzDpHhgHv5aJkuvLp9RQzZFpa8hgWAB+xVIk=
cloud.google.com/go/iam v1.1.12 h1:JixGLimRrNGcxvJEQ8+clfLxPlbeZA6MuRJ+qJNQ5Xw=
cloud.google.com/go/iam v1.1.12/go.mod h1:9LDX8J7dN5YRyzVHxwQzrQs9opFFqn0Mxs9nAeB+Hhg=
cloud.google.com/go/iap v1.9.10 h1:j7jQqqSkZ2nWAOCiyaZfnJ+REycTJ2NP2dUEjLoW4aA=
cloud.google.com/go/iap v1.9.10/go.mod h1:pO0FEirrhMOT1H0WVwpD5dD9r3oBhvsunyBQtNXzzc0=
cloud.google.com/go/ids v1.4.11 h1:JhlR1d0XhMsj6YmSmbLbbXV5CGkffnUkPj0HNxJYNtc=
cloud.google.com/go/ids v1.4.11/go.mod h1:+ZKqWELpJm8WcRRsSvKZWUdkriu4A3XsLLzToTv3418=
cloud.google.com/go/iot v1.7.11 h1:UBqSUZA6+7bM+mv6uvhl8tVsyT2Fi50njtBFRbrKSlI=
cloud.google.com/go/iot v1.7.11/go.mod h1:0vZJOqFy9kVLbUXwTP95e0dWHakfR4u5IWqsKMGIfHk=
cloud.google.com/go/kms v1.18.4 h1:dYN3OCsQ6wJLLtOnI8DGUwQ5shMusXsWCCC+s09ATsk=
cloud.google.com/go/kms v1.18.4/go.mod h1:SG1bgQ3UWW6/KdPo9uuJnzELXY5YTTMJtDYvajiQ22g=
cloud.google.com/go/language v1.13.0 h1:6Pl97Ei85A3wBJwjXW2S/1IWeUvhQf/lIPQBItnp0FA=
cloud.google.com/go/language v1.13.0/go.mod h1:B9FbD17g1EkilctNGUDAdSrBHiFOlKNErLljO7jplDU=
cloud.google.com/go/lifesciences v0.9.11 h1:xyPSYICJWZElcELYgWCKs5PltyNX3TzOKaQAZA7d/I0=
cloud.google.com/go/lifesciences v0.9.11/go.mod h1:NMxu++FYdv55TxOBEvLIhiAvah8acQwXsz79i9l9/RY=
cloud.google.com/go/logging v1.11.0 h1:v3ktVzXMV7CwHq1MBF65wcqLMA7i+z3YxbUsoK7mOKs=
cloud.google.com/go/logging v1.11.0/go.mod h1:5LDiJC/RxTt+fHc1LAt20R9TKiUTReDg6RuuFOZ67+A=
cloud.google.com/go/longrunning v0.5.11 h1:Havn1kGjz3whCfoD8dxMLP73Ph5w+ODyZB9RUsDxtGk=
cloud.google.com/go/longrunning v0.5.11/go.mod h1:rDn7//lmlfWV1Dx6IB4RatCPenTwwmqXuiP0/RgoEO4=
cloud.google.com/go/managedidentities v1.6.11 h1:YU6NtRRBX5R1f3a8ryqhh1dUb1/pt3rnhSO50b63yZY=
cloud.google.com/go/managedidentities v1.6.11/go.mod h1:df+8oZ1D4Eri+NrcpuiR5Hd6MGgiMqn0ZCzNmBYPS0A=
cloud.google.com/go/maps v1.11.6 h1:HMI0drvgnT+BtsjBofb1Z80P53n63ybmm7l+1w1og9I=
cloud.google.com/go/maps v1.11.6/go.mod h1:MOS/NN0L6b7Kumr8bLux9XTpd8+D54DYxBMUjq+XfXs=
cloud.google.com/go/mediatranslation v0.8.11 h1:QvO405ocKTmcJqjfqL1zps08yrKk8rE+0E1ZNSWfjbw=
cloud.google.com/go/mediatranslation v0.8.11/go.mod h1:3sNEm0fx61eHk7rfzBzrljVV9XKr931xI3OFacQBVFg=
cloud.google.com/go/memcache v1.10.11 h1:DGPEJOVL4Qix2GLKQKcgzGpNLD7gAnCFLr9ch9YSIhU=
cloud.google.com/go/memcache v1.10.11/go.mod h1:ubJ7Gfz/xQawQY5WO5pht4Q0dhzXBFeEszAeEJnwBHU=
cloud.google.com/go/metastore v1.13.10 h1:E5eAxzIRoVP0DrV+ZtTLMYkkjSs4fcfsbL7wv1mXV2U=
cloud.google.com/go/metastore v1.13.10/go.mod h1:RPhMnBxUmTLT1fN7fNbPqtH5EoGHueDxubmJ1R1yT84=
cloud.google.com/go/monitoring v1.20.3 h1:v/7MXFxYrhXLEZ9sSfwXdlTLLB/xrU7xTyYjY5acynQ=
cloud.google.com/go/monitoring v1.20.3/go.mod h1:GPIVIdNznIdGqEjtRKQWTLcUeRnPjZW85szouimiczU=
cloud.google.com/go/networkconnectivity v1.14.10 h1:2EE8pKiv1AI8fBdZCdiUjNgQ+TaBgwE4GxIze4fDdY0=
cloud.google.com/go/networkconnectivity v1.14.10/go.mod h1:f7ZbGl4CV08DDb7lw+NmMXQTKKjMhgCEEwFbEukWuOY=
cloud.google.com/go/networkmanagement v1.13.6 h1:6TGn7ZZXyj5rloN0vv5Aw0awYbfbheNRg8BKroT7/2g=
cloud.google.com/go/networkmanagement v1.13.6/go.mod h1:WXBijOnX90IFb6sberjnGrVtZbgDNcPDUYOlGXmG8+4=
cloud.google.com/go/networksecurity v0.9.11 h1:6wUzyHCwDEOkDbAJjT6jxsAi+vMfe3aj2JWwqSFVXOQ=
cloud.google.com/go/networksecurity v0.9.11/go.mod h1:4xbpOqCwplmFgymAjPFM6ZIplVC6+eQ4m7sIiEq9oJA=
cloud.google.com/go/notebooks v1.11.9 h1:c8I0EaLGqStRmvX29L7jb4mOrpigxn1mGyBt65OdS0s=
cloud.google.com/go/notebooks v1.11.9/go.mod h1:JmnRX0eLgHRJiyxw8HOgumW9iRajImZxr7r75U16uXw=
cloud.google.com/go/optimization v1.6.9 h1:++U21U9LWFdgnnVFaq4kDeOafft6gI/CHzsiJ173c6U=
cloud.google.com/go/optimization v1.6.9/go.mod h1:mcvkDy0p4s5k7iSaiKrwwpN0IkteHhGmuW5rP9nXA5M=
cloud.google.com/go/orchestration v1.9.6 h1:xfczjtNDabsXTnDySAwD/TMfDSkcxEgH1rxfS6BVQtM=
cloud.google.com/go/orchestration v1.9.6/go.mod h1:gQvdIsHESZJigimnbUA8XLbYeFlSg/z+A7ppds5JULg=
cloud.google.com/go/orgpolicy v1.12.7 h1:StymaN9vS7949m15Nwgf5aKd9yaRtzWJ4VqHdbXcOEM=
cloud.google.com/go/orgpolicy v1.12.7/go.mod h1:Os3GlUFRPf1UxOHTup5b70BARnhHeQNNVNZzJXPbWYI=
cloud.google.com/go/osconfig v1.13.2 h1:IbbTg7jtTEn4+iEJwgbCYck5NLMOc2eKrqVpQb7Xx6c=
cloud.google.com/go/osconfig v1.13.2/go.mod h1:eupylkWQJCwSIEMkpVR4LqpgKkQi0mD4m1DzNCgpQso=
cloud.google.com/go/oslogin v1.13.7 h1:q9x7tjKtfBpXMpiJKwb5UyhMA3GrwmJHvx56uCEuS8M=
cloud.google.com/go/oslogin v1.13.7/go.mod h1:xq027cL0fojpcEcpEQdWayiDn8tIx3WEFYMM6+q7U+E=
cloud.google.com/go/phishingprotection v0.8.11 h1:3Kr7TINZ+8pbdWe3JnJf9c84ibz60NRTvwLdVtI3SK8=
cloud.google.com/go/phishingprotection v0.8.11/go.mod h1:Mge0cylqVFs+D0EyxlsTOJ1Guf3qDgrztHzxZqkhRQM=
cloud.google.com/go/policytroubleshooter v1.10.9 h1:EHXkBYgHQtVH8P41G2xxmQbMwQh+o5ggno8l3/9CXaA=
cloud.google.com/go/policytroubleshooter v1.10.9/go.mod h1:X8HEPVBWz8E+qwI/QXnhBLahEHdcuPO3M9YvSj0LDek=
cloud.google.com/go/privatecatalog v0.9.11 h1:t8dJpQf22H6COeDvp7TDl7+KuwLT6yVmqAVRIUIUj6U=
cloud.google.com/go/privatecatalog v0.9.11/go.mod h1:awEF2a8M6UgoqVJcF/MthkF8SSo6OoWQ7TtPNxUlljY=
cloud.google.com/go/pubsub v1.41.0 h1:ZPaM/CvTO6T+1tQOs/jJ4OEMpjtel0PTLV7j1JK+ZrI=
cloud.google.com/go/pubsub v1.41.0/go.mod h1:g+YzC6w/3N91tzG66e2BZtp7WrpBBMXVa3Y9zVoOGpk=
cloud.google.com/go/pubsublite v1.8.2 h1:jLQozsEVr+c6tOU13vDugtnaBSUy/PD5zK6mhm+uF1Y=
cloud.google.com/go/pubsublite v1.8.2/go.mod h1:4r8GSa9NznExjuLPEJlF1VjOPOpgf3IT6k8x/YgaOPI=
cloud.google.com/go/recaptchaenterprise/v2 v2.14.2 h1:80Mx0i3uyv5dPNUYsNPFk9GJ+19AmTlnWnXFCTC9NkI=
cloud.google.com/go/recaptchaenterprise/v2 v2.14.2/go.mod h1:MwPgdgvBkE46aWuuXeBTCB8hQJ88p+CpXInROZYCTkc=
cloud.google.com/go/recommendationengine v0.8.11 h1:STJYdA/e/MAh2ZSdjss5YE/d0t0nt0WotBF9V0pgpPQ=
cloud.google.com/go/recommendationengine v0.8.11/go.mod h1:cEkU4tCXAF88a4boMFZym7U7uyxvVwcQtKzS85IbQio=
cloud.google.com/go/recommender v1.12.7 h1:asEAoj4a3inPCdH8nbPaZDJWhR/xwfKi4tuSmIlaS2I=
cloud.google.com/go/recommender v1.12.7/go.mod h1:lG8DVtczLltWuaCv4IVpNphONZTzaCC9KdxLYeZM5G4=
cloud.google.com/go/redis v1.16.4 h1:9CO6EcuM9/CpgtcjG6JZV+GFw3oDrRfwLwmvwo/uM1o=
cloud.google.com/go/redis v1.16.4/go.mod h1:unCVfLP5eFrVhGLDnb7IaSaWxuZ+7cBgwwBwbdG9m9w=
cloud.google.com/go/resourcemanager v1.9.11 h1:N8CmqszjKNOgJnrQVsg+g8VWIEGgcwsD5rPiay9cMC4=
cloud.google.com/go/resourcemanager v1.9.11/go.mod h1:SbNAbjVLoi2rt9G74bEYb3aw1iwvyWPOJMnij4SsmHA=
cloud.google.com/go/resourcesettings v1.7.4 h1:1VwLfvJi8QtGrKPwuisGqr6gcgaCSR6A57wIvN+fqkM=
cloud.google.com/go/resourcesettings v1.7.4/go.mod h1:seBdLuyeq+ol2u9G2+74GkSjQaxaBWF+vVb6mVzQFG0=
cloud.google.com/go/retail v1.17.4 h1:YJgpBwCarAPqzaJS8ycIhyn2sAQT1RhTJRiTVBjtJAI=
cloud.google.com/go/retail v1.17.4/go.mod h1:oPkL1FzW7D+v/hX5alYIx52ro2FY/WPAviwR1kZZTMs=
cloud.google.com/go/run v1.4.0 h1:ai1rnbX92iPqWg9MrbDbebsxlUSAiOK6N9dEDDQeVA0=
cloud.google.com/go/run v1.4.0/go.mod h1:4G9iHLjdOC+CQ0CzA0+6nLeR6NezVPmlj+GULmb0zE4=
cloud.google.com/go/scheduler v1.10.12 h1:8BxDXoHCcsAe2fXsvFrkBbTxgl+5JBrIy1+/HRS0nxY=
cloud.google.com/go/scheduler v1.10.12/go.mod h1:6DRtOddMWJ001HJ6MS148rtLSh/S2oqd2hQC3n5n9fQ=
cloud.google.com/go/secretmanager v1.13.5 h1:tXlHvpm97mFD0Lv50N4U4zlXfkoTNay3BmpNA/W7/oI=
cloud.google.com/go/secretmanager v1.13.5/go.mod h1:/OeZ88l5Z6nBVilV0SXgv6XJ243KP2aIhSWRMrbvDCQ=
cloud.google.com/go/security v1.17.4 h1:ERhxAa02mnMEIIAXvzje+qJ+yWniP6l5uOX+k9ELCaA=
cloud.google.com/go/security v1.17.4/go.mod h1:KMuDJH+sEB3KTODd/tLJ7kZK+u2PQt+Cfu0oAxzIhgo=
cloud.google.com/go/securitycenter v1.33.1 h1:K+jfFUTum2jl//uWCN+QKkKXRgidxTyGfGTqXPyDvUY=
cloud.google.com/go/securitycenter v1.33.1/go.mod h1:jeFisdYUWHr+ig72T4g0dnNCFhRwgwGoQV6GFuEwafw=
cloud.google.com/go/servicedirectory v1.11.11 h1:8Ky2lY0CWJJIIlsc+rKTn6C3SqOuVEwT3brDC6TJCjk=
cloud.google.com/go/servicedirectory v1.11.11/go.mod h1:pnynaftaj9LmRLIc6t3r7r7rdCZZKKxui/HaF/RqYfs=
cloud.google.com/go/shell v1.7.11 h1:RobTXyL33DQITYQh//KJ9GjS4bsdj4fGmm2rkb/ywzM=
cloud.google.com/go/shell v1.7.11/go.mod h1:SywZHWac7onifaT9m9MmegYp3GgCLm+tgk+w2lXK8vg=
cloud.google.com/go/spanner v1.65.0 h1:XK15cs9lFFQo5n4Wh9nfrcPXAxWln6NdodDiQKmoD08=
cloud.google.com/go/spanner v1.65.0/go.mod h1:dQGB+w5a67gtyE3qSKPPxzniedrnAmV6tewQeBY7Hxs=
cloud.google.com/go/speech v1.24.0 h1:3j+WpeBY57C0FDJxg317vpKgOLjL/kNxlcNPGSqXkqE=
cloud.google.com/go/speech v1.24.0/go.mod h1:HcVyIh5jRXM5zDMcbFCW+DF2uK/MSGN6Rastt6bj1ic=
cloud.google.com/go/storagetransfer v1.10.10 h1:GfxaYqX+kwlrSrJAENNmRTCGmSTgvouvS3XhgwKpOT8=
cloud.google.com/go/storagetransfer v1.10.10/go.mod h1:8+nX+WgQ2ZJJnK8e+RbK/zCXk8T7HdwyQAJeY7cEcm0=
cloud.google.com/go/talent v1.6.12 h1:JN721EjG+UTfHVVaMhyxwKCCJPjUc8PiS0RnW/7kWfE=
cloud.google.com/go/talent v1.6.12/go.mod h1:nT9kNVuJhZX2QgqKZS6t6eCWZs5XEBYRBv6bIMnPmo4=
cloud.google.com/go/texttospeech v1.7.11 h1:jzko1ahItjLYEWr6n3lTIoBSinD1JzavEuDzYLWZNko=
cloud.google.com/go/texttospeech v1.7.11/go.mod h1:Ua125HU+WT2IkIo5MzQtuNpNEk72soShJQVdorZ1SAE=
cloud.google.com/go/tpu v1.6.11 h1:uMrwnK05cocNt3OOp+mZ16xlvIKaXUt3QUXkUbG4LdM=
cloud.google.com/go/tpu v1.6.11/go.mod h1:W0C4xaSj1Ay3VX/H96FRvLt2HDs0CgdRPVI4e7PoCDk=
cloud.google.com/go/trace v1.10.11 h1:+Y1emOgcyGy6OdJ2KQbT4t2oecPp49GtJn8j3GM1pWo=
cloud.google.com/go/trace v1.10.11/go.mod h1:fUr5L3wSXerNfT0f1bBg08W4axS2VbHGgYcfH4KuTXU=
cloud.google.com/go/translate v1.10.7 h1:W16MpZ2Z3TWoHbNHmyHz9As276lGVTSwxRcquv454R0=
cloud.google.com/go/translate v1.10.7/go.mod h1:mH/+8tvcItuy1cOWqU+/Y3iFHgkVUObNIQYI/kiFFiY=
cloud.google.com/go/video v1.22.0 h1:+FTZi7NtT4FV2Y1j3zC3zYjaRrlGqKsZpbLweredEWM=
cloud.google.com/go/video v1.22.0/go.mod h1:CxPshUNAb1ucnzbtruEHlAal9XY+SPG2cFqC/woJzII=
cloud.google.com/go/videointelligence v1.11.11 h1:zl8xijOEavernn/t6mZZ4fg0pIVc2yquHH73oj0Leo4=
cloud.google.com/go/videointelligence v1.11.11/go.mod h1:dab2Ca3AXT6vNJmt3/6ieuquYRckpsActDekLcsd6dU=
cloud.google.com/go/vision/v2 v2.8.6 h1:HyFEUXQa0SvlF0LASCn/x+juNCH4kIXQrUqi6SIcYvE=
cloud.google.com/go/vision/v2 v2.8.6/go.mod h1:G3v0uovxCye3u369JfrHGY43H6u/IQ08x9dw5aVH8yY=
cloud.google.com/go/vmmigration v1.7.11 h1:yqwkTPpvSw9dUfnl9/APAVrwO9UW1jJZtgbZpNQ+WdU=
cloud.google.com/go/vmmigration v1.7.11/go.mod h1:PmD1fDB0TEHGQR1tDZt9GEXFB9mnKKalLcTVRJKzcQA=
cloud.google.com/go/vmwareengine v1.2.0 h1:9Fjn/RoeOMo8UQt1TbXmmw7rJApC26BqnISAI1AERcc=
cloud.google.com/go/vmwareengine v1.2.0/go.mod h1:rPjCHu6hG9N8d6PhkoDWFkqL9xpbFY+ueVW+0pNFbZg=
cloud.google.com/go/vpcaccess v1.7.11 h1:1XgRP+Q2X6MvE/xnexpQ7ydgav+IO5UcKUIJEbL65J8=
cloud.google.com/go/vpcaccess v1.7.11/go.mod h1:a2cuAiSCI4TVK0Dt6/dRjf22qQvfY+podxst2VvAkcI=
cloud.google.com/go/webrisk v1.9.11 h1:2qwEqnXrToIv2Y4xvsUSxCk7R2Ki+3W2+GNyrytoKTQ=
cloud.google.com/go/webrisk v1.9.11/go.mod h1:mK6M8KEO0ZI7VkrjCq3Tjzw4vYq+3c4DzlMUDVaiswE=
cloud.google.com/go/websecurityscanner v1.6.11 h1:r3ePI3YN7ujwX8c9gIkgbVjYVwP4yQA4X2z6P7+HNxI=
cloud.google.com/go/websecurityscanner v1.6.11/go.mod h1:vhAZjksELSg58EZfUQ1BMExD+hxqpn0G0DuyCZQjiTg=
cloud.google.com/go/workflows v1.12.10 h1:EGJeZmwgE71jxFOI5s9iKST2Bivif3DSzlqVbiXACXQ=
cloud.google.com/go/workflows v1.12.10/go.mod h1:RcKqCiOmKs8wFUEf3EwWZPH5eHc7Oq0kamIyOUCk0IE=
github.com/BurntSushi/toml v0.3.1 h1:WXkYYl6Yr3qBf1K79EBnL4mak0OimBfB0XUf9Vl28OQ=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.30.0 h1:sBEjpZlNHzK1voKq9695PJSX2o5NEXl7/OL3coiIY0c=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.30.0/go.mod h1:P4WPRUkOhJC13W//jWpyfJNDAIpvRbAUIYLX/4jtlE0=
github.com/antlr4-go/antlr/v4 v4.13.0 h1:lxCg3LAv+EUK6t1i0y1V6/SLeUi0eKEKdhQAlS8TVTI=
github.com/antlr4-go/antlr/v4 v4.13.0/go.mod h1:pfChB/xh/Unjila75QW7+VU4TSnWnnk9UTnmpPaOR2g=
github.com/benbjohnson/clock v1.1.0 h1:Q92kusRqC1XV2MjkWETPvjJVqKetz1OzxZB7mHJLju8=
github.com/bufbuild/protovalidate-go v0.9.1 h1:cdrIA33994yCcJyEIZRL36ZGTe9UDM/WHs5MBHEimiE=
github.com/bufbuild/protovalidate-go v0.9.1/go.mod h1:5jptBxfvlY51RhX32zR6875JfPBRXUsQjyZjm/NqkLQ=
github.com/census-instrumentation/opencensus-proto v0.4.1 h1:iKLQ0xPNFxR/2hzXZMrBo8f1j86j5WHzznCCQxV/b8g=
github.com/census-instrumentation/opencensus-proto v0.4.1/go.mod h1:4T9NM4+4Vw91VeyqjLS6ao50K5bOcLKN6Q42XnYaRYw=
github.com/client9/misspell v0.3.4 h1:ta993UF76GwbvJcIo3Y68y/M3WxlpEHPWIGDkJYwzJI=
github.com/cncf/udpa/go v0.0.0-20191209042840-269d4d468f6f h1:WBZRG4aNOuI15bLRrCgN8fCq8E5Xuty6jGbmSNEvSsU=
github.com/cncf/xds/go v0.0.0-20240723142845-024c85f92f20 h1:N+3sFI5GUjRKBi+i0TxYVST9h4Ie192jJWpHvthBBgg=
github.com/cncf/xds/go v0.0.0-20240723142845-024c85f92f20/go.mod h1:W+zGtBO5Y1IgJhy4+A9GOqVhqLpfZi+vwmdNXUehLA8=
github.com/cncf/xds/go v0.0.0-20251210132809-ee656c7534f5 h1:6xNmx7iTtyBRev0+D/Tv1FZd4SCg8axKApyNyRsAt/w=
github.com/cncf/xds/go v0.0.0-20251210132809-ee656c7534f5/go.mod h1:KdCmV+x/BuvyMxRnYBlmVaq4OLiKW6iRQfvC62cvdkI=
github.com/creack/pty v1.1.9 h1:uDmaGzcdjhF4i/plgjmEsriH11Y0o7RKapEf/LDaM3w=
github.com/envoyproxy/go-control-plane v0.13.0 h1:HzkeUz1Knt+3bK+8LG1bxOO/jzWZmdxpwC51i202les=
github.com/envoyproxy/go-control-plane v0.13.0/go.mod h1:GRaKG3dwvFoTg4nj7aXdZnvMg4d7nvT/wl9WgVXn3Q8=
github.com/envoyproxy/go-control-plane v0.14.0 h1:hbG2kr4RuFj222B6+7T83thSPqLjwBIfQawTkC++2HA=
github.com/envoyproxy/go-control-plane v0.14.0/go.mod h1:NcS5X47pLl/hfqxU70yPwL9ZMkUlwlKxtAohpi2wBEU=
github.com/envoyproxy/go-control-plane/envoy v1.36.0 h1:yg/JjO5E7ubRyKX3m07GF3reDNEnfOboJ0QySbH736g=
github.com/envoyproxy/go-control-plane/envoy v1.36.0/go.mod h1:ty89S1YCCVruQAm9OtKeEkQLTb+Lkz0k8v9W0Oxsv98=
github.com/envoyproxy/go-control-plane/ratelimit v0.1.0 h1:/G9QYbddjL25KvtKTv3an9lx6VBE2cnb8wp1vEGNYGI=
github.com/envoyproxy/go-control-plane/ratelimit v0.1.0/go.mod h1:Wk+tMFAFbCXaJPzVVHnPgRKdUdwW/KdbRt94AzgRee4=
github.com/envoyproxy/protoc-gen-validate v1.1.0 h1:tntQDh69XqOCOZsDz0lVJQez/2L6Uu2PdjCQwWCJ3bM=
github.com/envoyproxy/protoc-gen-validate v1.1.0/go.mod h1:sXRDRVmzEbkM7CVcM06s9shE/m23dg3wzjl0UWqJ2q4=
github.com/envoyproxy/protoc-gen-validate v1.3.0 h1:TvGH1wof4H33rezVKWSpqKz5NXWg5VPuZ0uONDT6eb4=
github.com/envoyproxy/protoc-gen-validate v1.3.0/go.mod h1:HvYl7zwPa5mffgyeTUHA9zHIH36nmrm7oCbo4YKoSWA=
github.com/go-jose/go-jose/v4 v4.1.3 h1:CVLmWDhDVRa6Mi/IgCgaopNosCaHz7zrMeF9MlZRkrs=
github.com/go-jose/go-jose/v4 v4.1.3/go.mod h1:x4oUasVrzR7071A4TnHLGSPpNOm2a21K9Kf04k1rs08=
github.com/go-kit/log v0.1.0 h1:DGJh0Sm43HbOeYDNnVZFl8BvcYVvjD5bqYJvp0REbwQ=
github.com/go-logfmt/logfmt v0.5.0 h1:TrB8swr/68K7m9CcGut2g3UOihhbcbiMAYiuTXdEih4=
github.com/go-logr/logr v1.4.1 h1:pKouT5E8xu9zeFC39JXRDukb6JFQPXM5p5I91188VAQ=
github.com/go-logr/logr v1.4.1/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
github.com/go-stack/stack v1.8.0 h1:5SgMzNM5HxrEjV0ww2lTmX6E2Izsfxas4+YHWRs3Lsk=
github.com/gogo/protobuf v1.3.2 h1:Ov1cvc58UF3b5XjBnZv7+opcTcQFZebYjWzi34vdm4Q=
github.com/golang/glog v1.2.2 h1:1+mZ9upx1Dh6FmUTFR1naJ77miKiXgALjWOZ3NVFPmY=
github.com/golang/glog v1.2.2/go.mod h1:6AhwSGph0fcJtXVM/PEHPqZlFeoLxhs7/t5UDAwmO+w=
github.com/golang/glog v1.2.5 h1:DrW6hGnjIhtvhOIiAKT6Psh/Kd/ldepEa81DKeiRJ5I=
github.com/golang/glog v1.2.5/go.mod h1:6AhwSGph0fcJtXVM/PEHPqZlFeoLxhs7/t5UDAwmO+w=
github.com/golang/mock v1.1.1 h1:G5FRp8JnTd7RQH5kemVNlMeyXQAztQ3mOWV95KxsXH8=
github.com/golang/protobuf v1.5.0 h1:LUVKkCeviFUMKqHa4tXIIij/lbhnMbP7Fn5wKdKkRh4=
github.com/golang/protobuf v1.5.0/go.mod h1:FsONVRAS9T7sI+LIUmWTfcYkHO4aIWwzhcaSAoJOfIk=
github.com/google/cel-go v0.23.0 h1:knsnzeUOcREUFo0ZFJqZI8Rk6uEVyobAlir7GEbf5v0=
github.com/google/cel-go v0.23.0/go.mod h1:52Pb6QsDbC5kvgxvZhiL9QX1oZEkcUF/ZqaPx1J5Wwo=
github.com/kisielk/errcheck v1.5.0 h1:e8esj/e4R+SAOwFwN+n3zr0nYeCyeweozKfO23MvHzY=
github.com/kisielk/gotool v1.0.0 h1:AV2c/EiW3KqPNT9ZKl07ehoAGi4C5/01Cfbblndcapg=
github.com/konsorten/go-windows-terminal-sequences v1.0.1 h1:mweAR1A6xJ3oS2pRaGiHgQ4OO8tzTaLawm8vnODuwDk=
github.com/kr/pty v1.1.1 h1:VkoXIwSboBpnk99O/KFauAEILuNHv5DVFKZMBN/gUgw=
github.com/opentracing/opentracing-go v1.1.0 h1:pWlfV3Bxv7k65HYwkikxat0+s3pV4bsqf19k25Ur8rU=
github.com/pkg/diff v0.0.0-20210226163009-20ebb0f2a09e h1:aoZm08cpOy4WuID//EZDgcC4zIxODThtZNPirFr42+A=
github.com/pkg/errors v0.8.1 h1:iURUrRGxPUNPdy5/HRSm+Yj6okJ6UtLINN0Q9M4+h3I=
github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10 h1:GFCKgmp0tecUJ0sJuv4pzYCqS9+RGSn52M3FUwPs+uo=
github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10/go.mod h1:t/avpk3KcrXxUnYOhZhMXJlSEyie6gQbtLq5NM3loB8=
github.com/prometheus/client_model v0.0.0-20190812154241-14fe0d1b01d4 h1:gQz4mCbXsO+nc9n1hCxHcGA3Zx3Eo+UHZoInFGUIXNM=
github.com/sirupsen/logrus v1.4.2 h1:SPIRibHv4MatM3XXNO2BJeFLZwZ2LvZgfQ5+UNI2im4=
github.com/spiffe/go-spiffe/v2 v2.6.0 h1:l+DolpxNWYgruGQVV0xsfeya3CsC7m8iBzDnMpsbLuo=
github.com/spiffe/go-spiffe/v2 v2.6.0/go.mod h1:gm2SeUoMZEtpnzPNs2Csc0D/gX33k1xIx7lEzqblHEs=
github.com/stoewer/go-strcase v1.3.0 h1:g0eASXYtp+yvN9fK8sH94oCIk0fau9uV1/ZdJ0AVEzs=
github.com/stoewer/go-strcase v1.3.0/go.mod h1:fAH5hQ5pehh+j3nZfvwdk2RgEgQjAoM8wodgtPmh1xo=
github.com/yuin/goldmark v1.4.13 h1:fVcFKWvrslecOb/tg+Cc05dkeYx540o0FuFt3nUVDoE=
github.com/yuin/goldmark v1.4.13/go.mod h1:6yULJ656Px+3vBD8DxQVa3kxgyrAnzto9xy5taEt/CY=
go.opentelemetry.io/contrib/detectors/gcp v1.39.0 h1:kWRNZMsfBHZ+uHjiH4y7Etn2FK26LAGkNFw7RHv1DhE=
go.opentelemetry.io/contrib/detectors/gcp v1.39.0/go.mod h1:t/OGqzHBa5v6RHZwrDBJ2OirWc+4q/w2fTbLZwAKjTk=
go.opentelemetry.io/otel/metric v1.24.0 h1:6EhoGWWK28x1fbpA4tYTOWBkPefTDQnb8WSGXlc88kI=
go.opentelemetry.io/otel/metric v1.24.0/go.mod h1:VYhLe1rFfxuTXLgj4CBiyz+9WYBA8pNGJgDcSFRKBco=
go.opentelemetry.io/otel/trace v1.24.0 h1:CsKnnL4dUAr/0llH9FKuc698G04IrpWV0MQA/Y1YELI=
go.opentelemetry.io/otel/trace v1.24.0/go.mod h1:HPc3Xr/cOApsBI154IU0OI0HJexz+aw5uPdbs3UCjNU=
go.uber.org/atomic v1.7.0 h1:ADUqmZGgLDDfbSL9ZmPxKTybcoEYHgpYfELNoN+7hsw=
go.uber.org/goleak v1.1.10 h1:z+mqJhf6ss6BSfSM671tgKyZBFPTTJM+HLxnhPC3wu0=
go.uber.org/multierr v1.6.0 h1:y6IPFStTAIT5Ytl7/XYmHvzXQ7S3g/IeZW9hyZ5thw4=
go.uber.org/zap v1.18.1 h1:CSUJ2mjFszzEWt4CdKISEuChVIXGBn3lAPwkRGyVrc4=
golang.org/x/crypto v0.26.0 h1:RrRspgV4mU+YwB4FYnuBoKsUapNIL5cohGAmSH3azsw=
golang.org/x/crypto v0.26.0/go.mod h1:GY7jblb9wI+FOo5y8/S2oY4zWP07AkOJ4+jxCqdqn54=
golang.org/x/crypto v0.31.0 h1:ihbySMvVjLAeSH1IbfcRTkD/iNscyz8rGzjF/E5hV6U=
golang.org/x/crypto v0.31.0/go.mod h1:kDsLvtWBEx7MV9tJOj9bnXsPbxwJQ6csT/x4KIN4Ssk=
golang.org/x/crypto v0.35.0 h1:b15kiHdrGCHrP6LvwaQ3c03kgNhhiMgvlhxHQhmg2Xs=
golang.org/x/crypto v0.35.0/go.mod h1:dy7dXNW32cAb/6/PRuTNsix8T+vJAqvuIy5Bli/x0YQ=
golang.org/x/crypto v0.39.0 h1:SHs+kF4LP+f+p14esP5jAoDpHU8Gu/v9lFRK6IT5imM=
golang.org/x/crypto v0.39.0/go.mod h1:L+Xg3Wf6HoL4Bn4238Z6ft6KfEpN0tJGo53AAPC632U=
golang.org/x/crypto v0.46.0 h1:cKRW/pmt1pKAfetfu+RCEvjvZkA9RimPbh7bhFjGVBU=
golang.org/x/crypto v0.46.0/go.mod h1:Evb/oLKmMraqjZ2iQTwDwvCtJkczlDuTmdJXoZVzqU0=
golang.org/x/exp v0.0.0-20190121172915-509febef88a4 h1:c2HOrn5iMezYjSlGPncknSEr/8x5LELb/ilJbXi9DEA=
golang.org/x/exp v0.0.0-20240325151524-a685a6edb6d8 h1:aAcj0Da7eBAtrTp03QXWvm88pSyOt+UgdZw2BFZ+lEw=
golang.org/x/exp v0.0.0-20240325151524-a685a6edb6d8/go.mod h1:CQ1k9gNrJ50XIzaKCRR2hssIjF07kZFEiieALBM/ARQ=
golang.org/x/lint v0.0.0-20190930215403-16217165b5de h1:5hukYrvBGR8/eNkX5mdUezrA6JiaEZDtJb9Ei+1LlBs=
golang.org/x/mod v0.17.0 h1:zY54UmvipHiNd+pm+m0x9KhZ9hl1/7QNMyxXbc6ICqA=
golang.org/x/mod v0.17.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/mod v0.25.0 h1:n7a+ZbQKQA/Ysbyb0/6IbB1H/X41mKgbhfv7AfG/44w=
golang.org/x/mod v0.25.0/go.mod h1:IXM97Txy2VM4PJ3gI61r1YEk/gAj6zAHN3AdZt6S9Ww=
golang.org/x/mod v0.30.0 h1:fDEXFVZ/fmCKProc/yAXXUijritrDzahmwwefnjoPFk=
golang.org/x/mod v0.30.0/go.mod h1:lAsf5O2EvJeSFMiBxXDki7sCgAxEUcZHXoXMKT4GJKc=
golang.org/x/oauth2 v0.22.0 h1:BzDx2FehcG7jJwgWLELCdmLuxk2i+x9UDpSiss2u0ZA=
golang.org/x/oauth2 v0.22.0/go.mod h1:XYTD2NtWslqkgxebSiOHnXEap4TF09sJSc7H1sXbhtI=
golang.org/x/oauth2 v0.34.0 h1:hqK/t4AKgbqWkdkcAeI8XLmbK+4m4G5YeQRrmiotGlw=
golang.org/x/oauth2 v0.34.0/go.mod h1:lzm5WQJQwKZ3nwavOZ3IS5Aulzxi68dUSgRHujetwEA=
golang.org/x/sync v0.8.0 h1:3NFvSEYkUoMifnESzZl15y791HH1qU2xm6eCJU5ZPXQ=
golang.org/x/sync v0.8.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.10.0 h1:3NQrjDixjgGwUOCaF8w2+VYHv0Ve/vGYSbdkTa98gmQ=
golang.org/x/sync v0.11.0 h1:GGz8+XQP4FvTTrjZPzNKTMFtSXH80RAzG+5ghFPgK9w=
golang.org/x/sync v0.11.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.15.0 h1:KWH3jNZsfyT6xfAfKiz6MRNmd46ByHDYaZ7KSkCtdW8=
golang.org/x/sync v0.15.0/go.mod h1:1dzgHSNfp02xaA81J2MS99Qcpr2w7fw1gpm99rleRqA=
golang.org/x/sync v0.19.0 h1:vV+1eWNmZ5geRlYjzm2adRgW2/mcpevXNg50YZtPCE4=
golang.org/x/sync v0.19.0/go.mod h1:9KTHXmSnoGruLpwFjVSX0lNNA75CykiMECbovNTZqGI=
golang.org/x/sys v0.33.0 h1:q3i8TbbEz+JRD9ywIRlyRAQbM0qF7hu24q3teo2hbuw=
golang.org/x/sys v0.33.0/go.mod h1:BJP2sWEmIv4KK5OTEluFJCKSidICx8ciO85XgH3Ak8k=
golang.org/x/telemetry v0.0.0-20240228155512-f48c80bd79b2 h1:IRJeR9r1pYWsHKTRe/IInb7lYvbBVIqOgsX/u0mbOWY=
golang.org/x/telemetry v0.0.0-20240521205824-bda55230c457 h1:zf5N6UOrA487eEFacMePxjXAJctxKmyjKUsjA11Uzuk=
golang.org/x/telemetry v0.0.0-20240521205824-bda55230c457/go.mod h1:pRgIJT+bRLFKnoM1ldnzKoxTIn14Yxz928LQRYYgIN0=
golang.org/x/term v0.23.0 h1:F6D4vR+EHoL9/sWAWgAR1H2DcHr4PareCbAaCo1RpuU=
golang.org/x/term v0.23.0/go.mod h1:DgV24QBUrK6jhZXl+20l6UWznPlwAHm1Q1mGHtydmSk=
golang.org/x/term v0.27.0 h1:WP60Sv1nlK1T6SupCHbXzSaN0b9wUmsPoRS9b61A23Q=
golang.org/x/term v0.27.0/go.mod h1:iMsnZpn0cago0GOrHO2+Y7u7JPn5AylBrcoWkElMTSM=
golang.org/x/term v0.29.0 h1:L6pJp37ocefwRRtYPKSWOWzOtWSxVajvz2ldH/xi3iU=
golang.org/x/term v0.29.0/go.mod h1:6bl4lRlvVuDgSf3179VpIxBF0o10JUpXWOnI7nErv7s=
golang.org/x/term v0.32.0 h1:DR4lr0TjUs3epypdhTOkMmuF5CDFJ/8pOnbzMZPQ7bg=
golang.org/x/term v0.32.0/go.mod h1:uZG1FhGx848Sqfsq4/DlJr3xGGsYMu/L5GW4abiaEPQ=
golang.org/x/term v0.38.0 h1:PQ5pkm/rLO6HnxFR7N2lJHOZX6Kez5Y1gDSJla6jo7Q=
golang.org/x/term v0.38.0/go.mod h1:bSEAKrOT1W+VSu9TSCMtoGEOUcKxOKgl3LE5QEF/xVg=
golang.org/x/text v0.26.0 h1:P42AVeLghgTYr4+xUnTRKDMqpar+PtX7KWuNQL21L8M=
golang.org/x/text v0.26.0/go.mod h1:QK15LZJUUQVJxhz7wXgxSy/CJaTFjd0G+YLonydOVQA=
golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d h1:vU5i/LfpvrRCpgM/VPfJLg5KjxD3E+hfT1SH+d9zLwg=
golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d/go.mod h1:aiJjzUbINMkxbQROHiO6hDPo2LHcIPhhQsa9DLh0yGk=
golang.org/x/tools v0.33.0 h1:4qz2S3zmRxbGIhDIAgjxvFutSvH5EfnsYrRBj0UI0bc=
golang.org/x/tools v0.33.0/go.mod h1:CIJMaWEY88juyUfo7UbgPqbC8rU2OqfAV1h2Qp0oMYI=
golang.org/x/tools v0.39.0 h1:ik4ho21kwuQln40uelmciQPp9SipgNDdrafrYA4TmQQ=
golang.org/x/tools v0.39.0/go.mod h1:JnefbkDPyD8UU2kI5fuf8ZX4/yUeh9W877ZeBONxUqQ=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543 h1:E7g+9GITq07hpfrRu66IVDexMakfv52eLZ2CXBWiKr4=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1 h1:go1bK/D/BFZV2I8cIQd1NKEZ+0owSTG1fDTci4IqFcE=
google.golang.org/appengine v1.4.0 h1:/wp5JvzpHIxhs/dumFmF7BXTf3Z+dd4uXta4kVyO508=
google.golang.org/genproto v0.0.0-20200423170343-7949de9c1215 h1:0Uz5jLJQioKgVozXa1gzGbzYxbb/rhQEVvSWxzw5oUs=
google.golang.org/genproto/googleapis/api v0.0.0-20240814211410-ddb44dafa142 h1:wKguEg1hsxI2/L3hUYrpo1RVi48K+uTyzKqprwLXsb8=
google.golang.org/genproto/googleapis/api v0.0.0-20240814211410-ddb44dafa142/go.mod h1:d6be+8HhtEtucleCbxpPW9PA9XwISACu8nvpPqF0BVo=
google.golang.org/genproto/googleapis/api v0.0.0-20240826202546-f6391c0de4c7 h1:YcyjlL1PRr2Q17/I0dPk2JmYS5CDXfcdb2Z3YRioEbw=
google.golang.org/genproto/googleapis/api v0.0.0-20240826202546-f6391c0de4c7/go.mod h1:OCdP9MfskevB/rbYvHTsXTtKC+3bHWajPdoKgjcYkfo=
google.golang.org/genproto/googleapis/api v0.0.0-20251202230838-ff82c1b0f217 h1:fCvbg86sFXwdrl5LgVcTEvNC+2txB5mgROGmRL5mrls=
google.golang.org/genproto/googleapis/api v0.0.0-20251202230838-ff82c1b0f217/go.mod h1:+rXWjjaukWZun3mLfjmVnQi18E1AsFbDN9QdJ5YXLto=
gopkg.in/yaml.v2 v2.2.8 h1:obN1ZagJSUGI0Ek/LBmuj4SNLPfIny3KsKFopxRdj10=
honnef.co/go/tools v0.0.0-20190523083050-ea95bdfd59fc h1:/hemPrYIhOhy8zYrNj+069zDB68us2sMGsfkFJO0iZs=
```

