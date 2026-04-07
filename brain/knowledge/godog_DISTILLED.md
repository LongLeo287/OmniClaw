---
id: godog
type: knowledge
owner: OA_Triage
---
# godog
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![#StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://vshymanskyy.github.io/StandWithUkraine)
[![Build Status](https://github.com/cucumber/godog/workflows/test/badge.svg)](https://github.com/cucumber/godog/actions?query=branch%main+workflow%3Atest)
[![PkgGoDev](https://pkg.go.dev/badge/github.com/cucumber/godog)](https://pkg.go.dev/github.com/cucumber/godog)
[![codecov](https://codecov.io/gh/cucumber/godog/branch/master/graph/badge.svg)](https://codecov.io/gh/cucumber/godog)
[![pull requests](https://oselvar.com/api/badge?label=pull%20requests&csvUrl=https%3A%2F%2Fraw.githubusercontent.com%2Fcucumber%2Foselvar-github-metrics%2Fmain%2Fdata%2Fcucumber%2Fgodog%2FpullRequests.csv)](https://oselvar.com/github/cucumber/oselvar-github-metrics/main/cucumber/godog)
[![issues](https://oselvar.com/api/badge?label=issues&csvUrl=https%3A%2F%2Fraw.githubusercontent.com%2Fcucumber%2Foselvar-github-metrics%2Fmain%2Fdata%2Fcucumber%2Fgodog%2Fissues.csv)](https://oselvar.com/github/cucumber/oselvar-github-metrics/main/cucumber/godog)

# Godog

<p align="center"><img src="logo.png" alt="Godog logo" style="width:250px;" /></p>

**The API is likely to change a few times before we reach 1.0.0**

Please read the full README, you may find it very useful. And do not forget to peek into the [Release Notes](https://github.com/cucumber/godog/blob/master/release-notes) and the [CHANGELOG](https://github.com/cucumber/godog/blob/master/CHANGELOG.md) from time to time.

Package godog is the official Cucumber BDD framework for Golang, it merges specification and test documentation into one cohesive whole, using Gherkin formatted scenarios in the format of Given, When, Then.

The project was inspired by [behat][behat] and [cucumber][cucumber].

## Why Godog/Cucumber

### A single source of truth

Godog merges specification and test documentation into one cohesive whole.

### Living documentation

Because they're automatically tested by Godog, your specifications are
always being up-to-date.

### Focus on the customer

Business and IT don't always understand each other. Godog's executable specifications encourage closer collaboration, helping teams keep the business goal in mind at all times.

### Less rework

When automated testing is this much fun, teams can easily protect themselves from costly regressions.

### Read more
- [Behaviour-Driven Development](https://cucumber.io/docs/bdd/)
- [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)

## Contributions

Godog is a community driven Open Source Project within the Cucumber organization. We [welcome contributions from everyone](https://cucumber.io/blog/open-source/tackling-structural-racism-(and-sexism)-in-open-so/), and we're ready to support you if you have the enthusiasm to contribute.

See the [contributing guide] for more detail on how to get started.

See the [releasing guide] for release flow details.

## Getting help

We have a [community Discord](https://cucumber.io/docs/community/get-in-touch/#discord) where you can chat with other users, developers, and BDD practitioners.

## Examples

You can find a few examples [here](/_examples).

**Note** that if you want to execute any of the examples and have the Git repository checked out in the `$GOPATH`, you need to use: `GO111MODULE=off`. [Issue](https://github.com/cucumber/godog/issues/344) for reference.

### Godogs

The following example can be [found here](/_examples/godogs).

#### Step 1 - Setup a go module

Create a new go module named **godogs** in your go workspace by running `mkdir godogs`

From now on, use **godogs** as your working directory by running `cd godogs`

Initiate the go module inside the **godogs** directory by running `go mod init godogs`

#### Step 2 - Create gherkin feature

Imagine we have a **godog cart** to serve godogs for lunch.

First of all, we describe our feature in plain text:

``` gherkin
Feature: eat godogs
  In order to be happy
  As a hungry gopher
  I need to be able to eat godogs

  Scenario: Eat 5 out of 12
    Given there are 12 godogs
    When I eat 5
    Then there should be 7 remaining
```

Run `vim features/godogs.feature` and add the text above into the vim editor and save the file.

#### Step 3 - Create godog step definitions

**NOTE:** Same as **go test**, godog respects package level isolation. All your step definitions should be in your tested package root directory. In this case: **godogs**.

Create and copy the step definitions below into a new file by running `vim godogs_test.go`:
``` go
package main

import "github.com/cucumber/godog"

func iEat(arg1 int) error {
        return godog.ErrPending
}

func thereAreGodogs(arg1 int) error {
        return godog.ErrPending
}

func thereShouldBeRemaining(arg1 int) error {
        return godog.ErrPending
}

func InitializeScenario(ctx *godog.ScenarioContext) {
        ctx.Step(`^there are (\d+) godogs$`, thereAreGodogs)
        ctx.Step(`^I eat (\d+)$`, iEat)
        ctx.Step(`^there should be (\d+) remaining$`, thereShouldBeRemaining)
}
```

Alternatively, you can also specify the keyword (Given, When, Then...) when creating the step definitions:
``` go
func InitializeScenario(ctx *godog.ScenarioContext) {
        ctx.Given(`^there are (\d+) godogs$`, thereAreGodogs)
        ctx.When(`^I eat (\d+)$`, iEat)
        ctx.Then(`^there should be (\d+) remaining$`, thereShouldBeRemaining)
}
```

Our module should now look like this:
```
godogs
- features
  - godogs.feature
- go.mod
- go.sum
- godogs_test.go
```

Run `go test` in the **godogs** directory to run the steps you have defined. You should now see that the scenario runs 
with a warning stating there are no tests to run. 
```
testing: warning: no tests to run
PASS
ok      godogs  0.225s
```

By adding some logic to these steps, you will be able to thoroughly test the feature you just defined.

#### Step 4 - Create the main program to test

Let's keep it simple by only requiring an amount of **godogs** for now.

Create and copy the code below into a new file by running `vim godogs.go`
```go
package main

// Godogs available to eat
var Godogs int

func main() { /* usual main func */ }
```

Our module should now look like this:
```
godogs
- features
  - godogs.feature
- go.mod
- go.sum
- godogs.go
- godogs_test.go
```

#### Step 5 - Add some logic to the step definitions

Now lets implement our step definitions to test our feature requirements.

Replace the contents of `godogs_test.go` with the code below by running `vim godogs_test.go`.

```go
package main

import (
  "context"
  "errors"
  "fmt"
  "testing"

  "github.com/cucumber/godog"
)

// godogsCtxKey is the key used to store the available godogs in the context.Context.
type godogsCtxKey struct{}

func thereAreGodogs(ctx context.Context, available int) (context.Context, error) {
  return context.WithValue(ctx, godogsCtxKey{}, available), nil
}

func iEat(ctx context.Context, num int) (context.Context, error) {
  available, ok := ctx.Value(godogsCtxKey{}).(int)
  if !ok {
    return ctx, errors.New("there are no godogs available")
  }

  if available < num {
    return ctx, fmt.Errorf("you cannot eat %d godogs, there are %d available", num, available)
  }

  available -= num

  return context.WithValue(ctx, godogsCtxKey{}, available), nil
}

func thereShouldBeRemaining(ctx context.Context, remaining int) error {
  available, ok := ctx.Value(godogsCtxKey{}).(int)
  if !ok {
    return errors.New("there are no godogs available")
  }

  if available != remaining {
    return fmt.Errorf("expected %d godogs to be remaining, but there is %d", remaining, available)
  }

  return nil
}

func TestFeatures(t *testing.T) {
  suite := godog.TestSuite{
    ScenarioInitializer: InitializeScenario,
    Options: &godog.Options{
      Format:   "pretty",
      Paths:    []string{"features"},
      TestingT: t, // Testing instance that will run subtests.
    },
  }

  if suite.Run() != 0 {
    t.Fatal("non-zero status returned, failed to run feature tests")
  }
}

func InitializeScenario(sc *godog.ScenarioContext) {
  sc.Step(`^there are (\d+) godogs$`, thereAreGodogs)
  sc.Step(`^I eat (\d+)$`, iEat)
  sc.Step(`^there should be (\d+) remaining$`, thereShouldBeRemaining)
}
```

In this example, we are using `context.Context` to pass the state between the steps. 
Every scenario starts with an empty context and then steps and hooks can add relevant information to it.
Instrumented context is chained through the steps and hooks and is safe to use when multiple scenarios are running concurrently.

When you run godog again with `go test -v godogs_test.go`, you should see a passing run:
```
=== RUN   TestFeatures
Feature: eat godogs
  In order to be happy
  As a hungry gopher
  I need to be able to eat godogs
=== RUN   TestFeatures/Eat_5_out_of_12

  Scenario: Eat 5 out of 12          # features/godogs.feature:6
    Given there are 12 godogs        # godog_test.go:15 -> command-line-arguments.thereAreGodogs
    When I eat 5                     # godog_test.go:19 -> command-line-arguments.iEat
    Then there should be 7 remaining # godog_test.go:34 -> command-line-arguments.thereShouldBeRemaining

1 scenarios (1 passed)
3 steps (3 passed)
279.917µs
--- PASS: TestFeatures (0.00s)
    --- PASS: TestFeatures/Eat_5_out_of_12 (0.00s)
PASS
ok      command-line-arguments  0.164s
```

You may hook to `ScenarioContext` **Before** event in order to reset or pre-seed the application state before each scenario. 
You may hook into more events, like `sc.StepContext()` **After** to print all state in case of an error. 
Or **BeforeSuite** to prepare a database.

By now, you should have figured out, how to use **godog**. Another piece of advice is to make steps orthogonal, small and simple to read for a user. 
Whether the user is a dumb website user or an API developer, who may understand a little more technical context - it should target that user.

When steps are orthogonal and small, you can combine them just like you do with Unix tools. Look how to simplify or remove ones, which can be composed.

`TestFeatures` acts as a regular Go test, so you can leverage your IDE facilities to run and debug it.

### Attachments

An example showing how to make attachments (aka embeddings) to the results is shown in [_examples/attachments](/_examples/attachments/)

## Code of Conduct

Everyone interacting in this codebase and issue tracker is expected to follow the Cucumber [code of conduct](https://github.com/cucumber/cucumber/blob/master/CODE_OF_CONDUCT.md).

## References and Tutorials

- [cucumber-html-reporter](https://github.com/gkushang/cucumber-html-reporter),
  may be used in order to generate **html** reports together with **cucumber** output formatter. See the [following docker image](https://github.com/myie/cucumber-html-reporter) for usage details.
- [how to use godog by semaphoreci](https://semaphoreci.com/community/tutorials/how-to-use-godog-for-behavior-driven-development-in-go)
- see [examples](https://github.com/cucumber/godog/tree/master/_examples)
- see extension [AssistDog](https://github.com/hellomd/assistdog),
  which may have useful **gherkin.DataTable** transformations or comparison methods for assertions.

## Documentation

See [pkg documentation][godoc] for general API details.
See **[Circle Config](/.circleci/config.yml)** for supported **go** versions.
See `godog -h` for general command options.

See implementation examples:

- [rest API server](/_examples/api)
- [rest API with Database](/_examples/db)
- [godogs](/_examples/godogs)

## FAQ

### Running Godog with go test

You may integrate running **godog** in your **go test** command. 

#### Subtests of *testing.T

You can run test suite using go [Subtests](https://pkg.go.dev/testing#hdr-Subtests_and_Sub_benchmarks).
In this case it is not necessary to have **godog** command installed. See the following example.

```go
package main_test

import (
	"testing"

	"github.com/cucumber/godog"
)

func TestFeatures(t *testing.T) {
  suite := godog.TestSuite{
    ScenarioInitializer: func(s *godog.ScenarioContext) {
      // Add step definitions here.
    },
    Options: &godog.Options{
      Format:   "pretty",
      Paths:    []string{"features"},
      TestingT: t, // Testing instance that will run subtests.
    },
  }

  if suite.Run() != 0 {
    t.Fatal("non-zero status returned, failed to run feature tests")
  }
}
```

Then you can run suite.
```
go test -test.v -test.run ^TestFeatures$
```

Or a particular scenario.
```
go test -test.v -test.run ^TestFeatures$/^my_scenario$
```

#### TestMain

You can run test suite using go [TestMain](https://golang.org/pkg/testing/#hdr-Main) func available since **go 1.4**. 
In this case it is not necessary to have **godog** command installed. See the following examples.

The following example binds **godog** flags with specified prefix `godog` in order to prevent flag collisions.

```go
package main

import (
	"os"
	"testing"

	"github.com/cucumber/godog"
	"github.com/cucumber/godog/colors"
	"github.com/spf13/pflag" // godog v0.11.0 and later
)

var opts = godog.Options{
	Output: colors.Colored(os.Stdout),
	Format: "progress", // can define default values
}

func init() {
	godog.BindFlags("godog.", pflag.CommandLine, &opts) // godog v0.10.0 and earlier
	godog.BindCommandLineFlags("godog.", &opts)        // godog v0.11.0 and later
}

func TestMain(m *testing.M) {
	pflag.Parse()
	opts.Paths = pflag.Args()

	status := godog.TestSuite{
		Name: "godogs",
		TestSuiteInitializer: InitializeTestSuite,
		ScenarioInitializer:  InitializeScenario,
		Options: &opts,
	}.Run()

	// Optional: Run `testing` package's logic besides godog.
	if st := m.Run(); st > status {
		status = st
	}

	os.Exit(status)
}
```

Then you may run tests with by specifying flags in order to filter features.

```
go test -v --godog.random --godog.tags=wip
go test -v --godog.format=pretty --godog.random -race -coverprofile=coverage.txt -covermode=atomic
```

The following example does not bind godog flags, instead manually configuring needed options.

```go
func TestMain(m *testing.M) {
	opts := godog.Options{
		Format:    "progress",
		Paths:     []string{"features"},
		Randomize: time.Now().UTC().UnixNano(), // randomize scenario execution order
	}

	status := godog.TestSuite{
		Name: "godogs",
		TestSuiteInitializer: InitializeTestSuite,
		ScenarioInitializer:  InitializeScenario,
		Options: &opts,
	}.Run()

	// Optional: Run `testing` package's logic besides godog.
	if st := m.Run(); st > status {
		status = st
	}

	os.Exit(status)
}
```

You can even go one step further and reuse **go test** flags, like **verbose** mode in order to switch godog **format**. See the following example:

```go
func TestMain(m *testing.M) {
	format := "progress"
	for _, arg := range os.Args[1:] {
		if arg == "-test.v=true" { // go test transforms -v option
			format = "pretty"
			break
		}
	}

	opts := godog.Options{
		Format: format,
		Paths:    
... [TRUNCATED]
```

### File: _examples\db\README.md
```md
# An example of API with DB

The following example demonstrates steps how we describe and test our API with DB using **godog**.
To start with, see [API example](https://github.com/cucumber/godog/tree/master/_examples/api) before.
We have extended it to be used with database.

The interesting point is, that we have [go-txdb](https://github.com/DATA-DOG/go-txdb) library,
which has an implementation of custom sql.driver to allow execute every and each scenario
within a **transaction**. After it completes, transaction is rolled back so the state could
be clean for the next scenario.

To run **users.feature** you need MySQL installed on your system with an anonymous root password.
Then run:

    make test

The json comparisom function should be improved and we should also have placeholders for primary
keys when comparing a json result.

```

### File: attachment_test.go
```go
package godog

import (
	"context"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestAttach(t *testing.T) {

	ctx := context.Background()

	ctx = Attach(ctx, Attachment{Body: []byte("body1"), FileName: "fileName1", MediaType: "mediaType1"})
	ctx = Attach(ctx, Attachment{Body: []byte("body2"), FileName: "fileName2", MediaType: "mediaType2"})

	attachments := Attachments(ctx)

	assert.Equal(t, 2, len(attachments))

	assert.Equal(t, []byte("body1"), attachments[0].Body)
	assert.Equal(t, "fileName1", attachments[0].FileName)
	assert.Equal(t, "mediaType1", attachments[0].MediaType)

	assert.Equal(t, []byte("body2"), attachments[1].Body)
	assert.Equal(t, "fileName2", attachments[1].FileName)
	assert.Equal(t, "mediaType2", attachments[1].MediaType)
}

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](http://semver.org).

This document is formatted according to the principles of [Keep A CHANGELOG](http://keepachangelog.com).

## Unreleased

## [v0.15.1]

### Added
- Step text is added to "step is undefined" error - ([669](https://github.com/cucumber/godog/pull/669) - [vearutop](https://github.com/vearutop))
- Localisation support by @MegaGrindStone in https://github.com/cucumber/godog/pull/665
- feat: support uint types by @chengxilo in https://github.com/cucumber/godog/pull/695

### Changed
- Replace deprecated `::set-output` - ([681](https://github.com/cucumber/godog/pull/681) - [nodeg](https://github.com/nodeg))

### Fixed
- fix(errors): fix(errors): Fix expected Step argument count for steps with `context.Context` ([679](https://github.com/cucumber/godog/pull/679) - [tigh-latte](https://github.com/tigh-latte))
- fix(formatter): On concurrent execution, execute formatter at end of Scenario - ([645](https://github.com/cucumber/godog/pull/645) - [tigh-latte](https://github.com/tigh-latte))
- Pretty printing results now prints the line where the step is declared instead of the line where the handler is declared. ([668](https://github.com/cucumber/godog/pull/668) - [spencerc](https://github.com/SpencerC))
- Update honnef.co/go/tools/cmd/staticcheck version in Makefile by @RezaZareiii in https://github.com/cucumber/godog/pull/670
- fix: verify dogT exists in the context before using it by @cakoolen in https://github.com/cucumber/godog/pull/692
- fix: change bang to being in README by @nahomEagleLion in https://github.com/cucumber/godog/pull/687
- Mark junit test cases as skipped if no pickle step results available by @mrsheepuk in https://github.com/cucumber/godog/pull/597
- Print step declaration line instead of handler declaration line by @SpencerC in https://github.com/cucumber/godog/pull/668

## [v0.15.0]

### Added
- Improved the type checking of step return types and improved the error messages - ([647](https://github.com/cucumber/godog/pull/647) - [johnlon](https://github.com/johnlon))
- Ambiguous step definitions will now be detected when strict mode is activated - ([636](https://github.com/cucumber/godog/pull/636)/([648](https://github.com/cucumber/godog/pull/648) - [johnlon](https://github.com/johnlon))
- Provide support for attachments / embeddings including a new example in the examples dir - ([623](https://github.com/cucumber/godog/pull/623) - [johnlon](https://github.com/johnlon))

### Changed
- Formatters now have a `Close` method and associated `io.Writer` changed to `io.WriteCloser`.

## [v0.14.1]

### Added
- Provide testing.T-compatible interface on test context, allowing usage of assertion libraries such as testify's assert/require - ([571](https://github.com/cucumber/godog/pull/571) - [mrsheepuk](https://github.com/mrsheepuk))
- Created releasing guidelines - ([608](https://github.com/cucumber/godog/pull/608) - [glibas](https://github.com/glibas))

### Fixed
- Step duration calculation - ([616](https://github.com/cucumber/godog/pull/616) - [iaroslav-ciupin](https://github.com/iaroslav-ciupin))
- Invalid memory address or nil pointer dereference in RetrieveFeatures - ([566](https://github.com/cucumber/godog/pull/566) - [corneldamian](https://github.com/corneldamian))

## [v0.14.0]
### Added
- Improve ErrSkip handling, add test for Summary and operations order ([584](https://github.com/cucumber/godog/pull/584) - [vearutop](https://github.com/vearutop))

### Fixed
- Remove line overwriting for scenario outlines in cucumber formatter ([605](https://github.com/cucumber/godog/pull/605) - [glibas](https://github.com/glibas))
- Remove duplicate warning message ([590](https://github.com/cucumber/godog/pull/590) - [vearutop](https://github.com/vearutop))
- updated base formatter to set a scenario as passed unless there exist ([582](https://github.com/cucumber/godog/pull/582) - [roskee](https://github.com/roskee))

### Changed
- Update test.yml ([583](https://github.com/cucumber/godog/pull/583) - [vearutop](https://github.com/vearutop))

## [v0.13.0]
### Added
- Support for reading feature files from an `fs.FS` ([550](https://github.com/cucumber/godog/pull/550) - [tigh-latte](https://github.com/tigh-latte))
- Added keyword functions. ([509](https://github.com/cucumber/godog/pull/509) - [otrava7](https://github.com/otrava7))
- Prefer go test to use of godog cli in README ([548](https://github.com/cucumber/godog/pull/548) - [danielhelfand](https://github.com/danielhelfand))
- Use `fs.FS` abstraction for filesystem ([550](https://github.com/cucumber/godog/pull/550) - [tigh-latte](https://github.com/tigh-latte))
- Cancel context for each scenario ([514](https://github.com/cucumber/godog/pull/514) - [draganm](https://github.com/draganm))

### Fixed
- Improve hooks invocation flow ([568](https://github.com/cucumber/godog/pull/568) - [vearutop](https://github.com/vearutop))
- Result of testing.T respect strict option ([539](https://github.com/cucumber/godog/pull/539) - [eiel](https://github.com/eiel))

### Changed
- BREAKING CHANGE, upgraded cucumber and messages dependencies = ([515](https://github.com/cucumber/godog/pull/515) - [otrava7](https://github.com/otrava7))

## [v0.12.6]
### Changed
- Each scenario is run with a cancellable `context.Context` which is cancelled at the end of the scenario. ([514](https://github.com/cucumber/godog/pull/514) - [draganm](https://github.com/draganm))
- README example is updated with `context.Context` and `go test` usage. ([477](https://github.com/cucumber/godog/pull/477) - [vearutop](https://github.com/vearutop))
- Removed deprecation of `godog.BindFlags`. ([498](https://github.com/cucumber/godog/pull/498) - [vearutop](https://github.com/vearutop))
- Pretty Print when using rules. ([480](https://github.com/cucumber/godog/pull/480) - [dumpsterfireproject](https://github.com/dumpsterfireproject))

### Fixed
- Fixed a bug which would ignore the context returned from a substep.([488](https://github.com/cucumber/godog/pull/488) - [wichert](https://github.com/wichert))
- Fixed a bug which would cause a panic when using the pretty formatter with a feature that contained a rule. ([480](https://github.com/cucumber/godog/pull/480) - [dumpsterfireproject](https://github.com/dumpsterfireproject))
- Multiple invocations of AfterScenario hooks in case of undefined steps. ([494](https://github.com/cucumber/godog/pull/494) - [vearutop](https://github.com/vearutop))
- Add a check for missing test files and raise a more helpful error. ([468](https://github.com/cucumber/godog/pull/468) - [ALCooper12](https://github.com/ALCooper12))
- Fix version subcommand. Do not print usage if run subcommand fails. ([475](https://github.com/cucumber/godog/pull/475) - [coopernurse](https://github.com/coopernurse))

### Added
- Add new option for created features with parsing from byte slices. ([476](https://github.com/cucumber/godog/pull/476) - [akaswenwilk](https://github.com/akaswenwilk))

### Deprecated
- `godog` CLI tool prints deprecation warning. ([489](https://github.com/cucumber/godog/pull/489) - [vearutop](https://github.com/vearutop))

## [v0.12.5]
### Changed
- Changed underlying cobra command setup to return errors instead of calling `os.Exit` directly to enable simpler testing. ([454](https://github.com/cucumber/godog/pull/454) - [mxygem](https://github.com/mxygem))
- Remove use of deprecated methods from `_examples`. ([460](https://github.com/cucumber/godog/pull/460) - [ricardogarfe](https://github.com/ricardogarfe))

### Fixed
- Support for go1.18 in `godog` cli mode ([466](https://github.com/cucumber/godog/pull/466) - [vearutop](https://github.com/vearutop))

## [v0.12.4]
### Added
- Allow suite-level configuration of steps and hooks ([453](https://github.com/cucumber/godog/pull/453) - [vearutop](https://github.com/vearutop))

## [v0.12.3]
### Added
- Automated binary releases with GitHub Actions ([437](https://github.com/cucumber/godog/pull/437) - [vearutop](https://github.com/vearutop))
- Automated binary versioning with `go install` ([437](https://github.com/cucumber/godog/pull/437) - [vearutop](https://github.com/vearutop))
- Module with local replace in examples ([437](https://github.com/cucumber/godog/pull/437) - [vearutop](https://github.com/vearutop))

### Changed
- suggest to use `go install` instead of the deprecated `go get` to install the `godog` binary ([449](https://github.com/cucumber/godog/pull/449) - [dmitris](https://github.com/dmitris))

### Fixed
- After Scenario hook is called before After Step ([444](https://github.com/cucumber/godog/pull/444) - [vearutop](https://github.com/vearutop))
- `check-go-version` in Makefile to run on WSL. ([443](https://github.com/cucumber/godog/pull/443) - [mxygem](https://github.com/mxygem))

## [v0.12.2]
### Fixed
- Error in `go mod tidy` with `GO111MODULE=off` ([436](https://github.com/cucumber/godog/pull/436) - [vearutop](https://github.com/vearutop))

## [v0.12.1]
### Fixed
- Unintended change of behavior in before step hook ([424](https://github.com/cucumber/godog/pull/424) - [nhatthm](https://github.com/nhatthm))

## [v0.12.0]
### Added
- Support for step definitions without return ([364](https://github.com/cucumber/godog/pull/364) - [titouanfreville](https://github.com/titouanfreville))
- Contextualized hooks for scenarios and steps ([409](https://github.com/cucumber/godog/pull/409) - [vearutop](https://github.com/vearutop))
- Step result status in After hook ([409](https://github.com/cucumber/godog/pull/409) - [vearutop](https://github.com/vearutop))
- Support auto converting doc strings to plain strings ([380](https://github.com/cucumber/godog/pull/380) - [chirino](https://github.com/chirino))
- Use multiple formatters in the same test run ([392](https://github.com/cucumber/godog/pull/392) - [vearutop](https://github.com/vearutop))
- Added `RetrieveFeatures()` method to `godog.TestSuite` ([276](https://github.com/cucumber/godog/pull/276) - [radtriste](https://github.com/radtriste))
- Added support to create custom formatters ([372](https://github.com/cucumber/godog/pull/372) - [leviable](https://github.com/leviable))

### Changed
- Upgraded gherkin-go to v19 and messages-go to v16 ([402](https://github.com/cucumber/godog/pull/402) - [mbow](https://github.com/mbow))
- Generate simpler snippets that use *godog.DocString and *godog.Table ([379](https://github.com/cucumber/godog/pull/379) - [chirino](https://github.com/chirino))

### Deprecated
- `ScenarioContext.BeforeScenario`, use `ScenarioContext.Before` ([409](https://github.com/cucumber/godog/pull/409)) - [vearutop](https://github.com/vearutop))
- `ScenarioContext.AfterScenario`, use `ScenarioContext.After` ([409](https://github.com/cucumber/godog/pull/409)) - [vearutop](https://github.com/vearutop))
- `ScenarioContext.BeforeStep`, use `ScenarioContext.StepContext().Before` ([409](https://github.com/cucumber/godog/pull/409)) - [vearutop](https://github.com/vearutop))
- `ScenarioContext.AfterStep`, use `ScenarioContext.StepContext().After` ([409](https://github.com/cucumber/godog/pull/409)) - [vearutop](https://github.com/vearutop))

### Fixed
- Incorrect step definition output for Data Tables ([411](https://github.com/cucumber/godog/pull/411) - [karfrank](https://github.com/karfrank))
- `ScenarioContext.AfterStep` not invoked after a failed case ([409](https://github.com/cucumber/godog/pull/409) - [vearutop](https://github.com/vearutop)))
- Can't execute multiple specific scenarios in the same feature file ([414](https://github.com/cucumber/godog/pull/414) - [vearutop](https://github.com/vearutop)))

## [v0.11.0]
### Added
- Created a simple example for a custom formatter ([330](https://github.com/cucumber/godog/pull/330) - [lonnblad](https://github.com/lonnblad))
- --format junit:result.xml will now write to result.xml ([331](https://github.com/cucumber/godog/pull/331) - [lonnblad](https://github.com/lonnblad))
- Added make commands to create artifacts and upload them to a github release ([333](https://github.com/cucumber/godog/pull/333) - [lonnblad](https://github.com/lonnblad))
- Created release notes and changelog for v0.11.0 ([355](https://github.com/cucumber/godog/pull/355) - [lonnblad](https://github.com/lonnblad))
- Created v0.11.0-rc2 ([362](https://github.com/cucumber/godog/pull/362) - [lonnblad](https://github.com/lonnblad))

### Changed
- Added Cobra for the Command Line Interface ([321](https://github.com/cucumber/godog/pull/321) - [lonnblad](https://github.com/lonnblad))
- Added internal packages for formatters, storage and models ([323](https://github.com/cucumber/godog/pull/323) - [lonnblad](https://github.com/lonnblad))
- Added an internal package for tags filtering ([326](https://github.com/cucumber/godog/pull/326) - [lonnblad](https://github.com/lonnblad))
- Added an internal pkg for the builder ([327](https://github.com/cucumber/godog/pull/327) - [lonnblad](https://github.com/lonnblad))
- Moved the parser code to a new internal pkg ([329](https://github.com/cucumber/godog/pull/329) - [lonnblad](https://github.com/lonnblad))
- Moved StepDefinition to the formatters pkg ([332](https://github.com/cucumber/godog/pull/332) - [lonnblad](https://github.com/lonnblad))
- Removed go1.12 and added go1.15 to CI config ([356](https://github.com/cucumber/godog/pull/356) - [lonnblad](https://github.com/lonnblad))

### Fixed
- Improved the help text of the formatter flag in the run command ([347](https://github.com/cucumber/godog/pull/347) - [lonnblad](https://github.com/lonnblad))
- Removed $GOPATH from the README.md and updated the example ([349](https://github.com/cucumber/godog/pull/349) - [lonnblad](https://github.com/lonnblad))
- Fixed the undefined step definitions help ([350](https://github.com/cucumber/godog/pull/350) - [lonnblad](https://github.com/lonnblad))
- Added a comment regarding running the examples within the $GOPATH ([352](https://github.com/cucumber/godog/pull/352) - [lonnblad](https://github.com/lonnblad))
- doc(FAQ/TestMain): `testing.M.Run()` is optional ([353](https://github.com/cucumber/godog/pull/353) - [hansbogert](https://github.com/hansbogert))
- Made a fix for the unstable Randomize Run tests ([354](https://github.com/cucumber/godog/pull/354) - [lonnblad](https://github.com/lonnblad))
- Fixed an issue when go test is parsing command-line flags ([359](https://github.com/cucumber/godog/pull/359) - [lonnblad](https://github.com/lonnblad))
- Make pickleStepIDs unique accross multiple paths ([366](https://github.com/cucumber/godog/pull/366) - [rickardenglund](https://github.com/rickardenglund))

### Removed
- Removed deprecated code ([322](https://github.com/cucumber/godog/pull/322) - [lonnblad](https://github.com/lonnblad))

## [v0.10.0]
### Added
- Added concurrency support to the pretty formatter ([275](https://github.com/cucumber/godog/pull/275) - [lonnblad](https://github.com/lonnblad))
- Added concurrency support 
... [TRUNCATED]
```

### File: CHANGELOG_OLD.md
```md
# Change LOG

**2020-02-06**
- move to new [CHANGELOG.md](CHANGELOG.md)

**2020-01-31**
- change license to MIT and moving project repository to **cucumber**
  organization.

**2018-11-16**
- added formatter output test suite, currently mainly pretty format
  tested.
- these tests, helped to identify some output format issues.

**2018-11-12**
- proper go module support added for `godog` command build.
- added build tests.

**2018-10-27**
- support go1.11 new compiler and linker changes for **godog** command.
- support go1.11 modules and `go mod` builds.
- `BindFlags` now has a prefix option for flags, so that `go test` command
  can avoid flag name collisions.
- `BindFlags` respect default options provided for binding, so that it
  does not override predefined options when flags are bind, see #144.
- Minor patch to support tag filters on example tables for
  ScenarioOutline.
- Minor patch for pretty printer, when scenario has no steps, comment
  possition computation was in panic.

**2018-03-04**
- support go1.10 new compiler and linker changes for **godog** command.

**2017-08-31**
- added **BeforeFeature** and **AfterFeature** hooks.
- failed multistep error is now prepended with a parent step text in order
  to determine failed nested step.
- pretty format now removes the step definition location package name in
  comment next to step if the step definition matches tested package. If
  step definition is imported from other package, full package name will
  be printed.

**2017-05-04**
- added **--strict** option in order to fail suite when there are pending
  or undefined steps. By default, suite passes and treats pending or
  undefined steps as TODOs.

**2017-04-29** - **v0.7.0**
- added support for nested steps. From now on, it is possible to return
  **godog.Steps** instead of an **error** in the step definition func.
  This change introduced few minor changes in **Formatter** interface. Be
  sure to adapt the changes if you have custom formatters.

**2017-04-27**
- added an option to randomize scenario execution order, so we could
  ensure that scenarios do not depend on global state.
- godog was manually sorting feature files by name. Now it just runs them
  in given order, you may sort them anyway you like. For example `godog
  $(find . -name '*.feature' | sort)`

**2016-10-30** - **v0.6.0**
- added experimental **events** format, this might be used for unified
  cucumber formats. But should be not adapted widely, since it is highly
  possible that specification will change.
- added **RunWithOptions** method which allows to easily run godog from
  **TestMain** without needing to simulate flag arguments. These options
  now allows to configure output writer.
- added flag **-o, --output=runner.binary** which only compiles the test
  runner executable, but does not execute it.
- **FlagSet** initialization now takes io.Writer as output for help text
  output. It was not showing nice colors on windows before.
  **--no-colors** option only applies to test run output.

**2016-06-14** - **v0.5.0**
- godog now uses **go tool compile** and **go tool link** to support
  vendor directory dependencies. It also compiles test executable the same
  way as standard **go test** utility. With this change, only go
  versions from **1.5** are now supported.

**2016-06-01**
- parse flags in main command, to show version and help without needing
  to compile test package and buildable go sources.

**2016-05-28**
- show nicely formatted called step func name and file path

**2016-05-26**
- pack gherkin dependency in a subpackage to prevent compatibility
  conflicts in the future. If recently upgraded, probably you will need to
  reference gherkin as `github.com/DATA-DOG/godog/gherkin` instead.

**2016-05-25**
- refactored test suite build tooling in order to use standard **go test**
  tool. Which allows to compile package with godog runner script in **go**
  idiomatic way. It also supports all build environment options as usual.
- **godog.Run** now returns an **int** exit status. It was not returning
  anything before, so there is no compatibility breaks.

**2016-03-04**
- added **junit** compatible output formatter, which prints **xml**
  results to **os.Stdout**
- fixed #14 which skipped printing background steps when there was
  scenario outline in feature.

**2015-07-03**
- changed **godog.Suite** from interface to struct. Context registration should be updated accordingly. The reason
for change: since it exports the same methods and there is no need to mock a function in tests, there is no
obvious reason to keep an interface.
- in order to support running suite concurrently, needed to refactor an entry point of application. The **Run** method
now is a func of godog package which initializes and run the suite (or more suites). Method **New** is removed. This
change made godog a little cleaner.
- renamed **RegisterFormatter** func to **Format** to be more consistent.


```

### File: CONTRIBUTING.md
```md
# Welcome 💖

Before anything else, thank you for taking some of your precious time to help this project move forward. ❤️

If you're new to open source and feeling a bit nervous 😳, we understand! We recommend watching [this excellent guide](https://egghead.io/talks/git-how-to-make-your-first-open-source-contribution)
to give you a grounding in some of the basic concepts. You could also watch [this talk](https://www.youtube.com/watch?v=tuSk6dMoTIs) from our very own wonderful [Marit van Dijk](https://github.com/mlvandijk) on her experiences contributing to Cucumber.

We want you to feel safe to make mistakes, and ask questions. If anything in this guide or anywhere else in the codebase doesn't make sense to you, please let us know! It's through your feedback that we can make this codebase more welcoming, so we'll be glad to hear thoughts.

You can chat with us in the `#committers` channel in our [community Discord](https://cucumber.io/docs/community/get-in-touch/#discord), or feel free to [raise an issue] if you're experiencing any friction trying make your contribution.

## Setup

To get your development environment set up, you'll need to [install Go]. We're currently using version 1.17 for development.

Once that's done, try running the tests:

    make test

If everything passes, you're ready to hack!

[install go]: https://golang.org/doc/install
[community Discord]: https://cucumber.io/community#discord
[raise an issue]: https://github.com/cucumber/godog/issues/new/choose

## Changing dependencies

If dependencies have changed, you will also need to update the _examples module. `go mod tidy` should be sufficient.
```

### File: example_subtests_test.go
```go
package godog_test

import (
	"testing"

	"github.com/cucumber/godog"
)

func ExampleTestSuite_Run_subtests() {
	var t *testing.T // Comes from your test function, e.g. func TestFeatures(t *testing.T).

	suite := godog.TestSuite{
		ScenarioInitializer: func(s *godog.ScenarioContext) {
			// Add step definitions here.
		},
		Options: &godog.Options{
			Format:   "pretty",
			Paths:    []string{"features"},
			TestingT: t, // Testing instance that will run subtests.
		},
	}

	if suite.Run() != 0 {
		t.Fatal("non-zero status returned, failed to run feature tests")
	}
}

func TestFeatures(t *testing.T) {
	suite := godog.TestSuite{
		ScenarioInitializer: func(s *godog.ScenarioContext) {
			godog.InitializeScenario(s)

			// Add step definitions here.
		},
		Options: &godog.Options{
			Format:   "pretty",
			Paths:    []string{"features"},
			TestingT: t, // Testing instance that will run subtests.
		},
	}

	if suite.Run() != 0 {
		t.Fatal("non-zero status returned, failed to run feature tests")
	}
}

```

### File: flags.go
```go
package godog

import (
	"flag"
	"fmt"
	"io"
	"sort"
	"strconv"
	"strings"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/internal/utils"
)

// repeats a space n times
var s = utils.S

var descFeaturesArgument = "Optional feature(s) to run. Can be:\n" +
	s(4) + "- dir " + colors.Yellow("(features/)") + "\n" +
	s(4) + "- feature " + colors.Yellow("(*.feature)") + "\n" +
	s(4) + "- scenario at specific line " + colors.Yellow("(*.feature:10)") + "\n" +
	"If no feature paths are listed, suite tries " + colors.Yellow("features") + " path by default.\n" +
	"Multiple comma-separated values can be provided.\n"

var descConcurrencyOption = "Run the test suite with concurrency level:\n" +
	s(4) + "- " + colors.Yellow(`= 1`) + ": supports all types of formats.\n" +
	s(4) + "- " + colors.Yellow(`>= 2`) + ": only supports " + colors.Yellow("progress") + ". Note, that\n" +
	s(4) + "your context needs to support parallel execution."

var descTagsOption = "Filter scenarios by tags. Expression can be:\n" +
	s(4) + "- " + colors.Yellow(`"@wip"`) + ": run all scenarios with wip tag\n" +
	s(4) + "- " + colors.Yellow(`"~@wip"`) + ": exclude all scenarios with wip tag\n" +
	s(4) + "- " + colors.Yellow(`"@wip && ~@new"`) + ": run wip scenarios, but exclude new\n" +
	s(4) + "- " + colors.Yellow(`"@wip,@undone"`) + ": run wip or undone scenarios"

var descRandomOption = "Randomly shuffle the scenario execution order.\n" +
	"Specify SEED to reproduce the shuffling from a previous run.\n" +
	s(4) + `e.g. ` + colors.Yellow(`--random`) + " or " + colors.Yellow(`--random=5738`)

// FlagSet allows to manage flags by external suite runner
// builds flag.FlagSet with godog flags binded
//
// Deprecated:
func FlagSet(opt *Options) *flag.FlagSet {
	set := flag.NewFlagSet("godog", flag.ExitOnError)
	BindFlags("", set, opt)
	set.Usage = usage(set, opt.Output)
	return set
}

// BindFlags binds godog flags to given flag set prefixed
// by given prefix, without overriding usage
func BindFlags(prefix string, set *flag.FlagSet, opt *Options) {
	set.Usage = usage(set, set.Output())

	descFormatOption := "How to format tests output. Built-in formats:\n"

	type fm struct {
		name string
		desc string
	}
	var fms []fm
	for name, desc := range AvailableFormatters() {
		fms = append(fms, fm{
			name: name,
			desc: desc,
		})
	}
	sort.Slice(fms, func(i, j int) bool {
		return fms[i].name < fms[j].name
	})

	for _, fm := range fms {
		descFormatOption += s(4) + "- " + colors.Yellow(fm.name) + ": " + fm.desc + "\n"
	}

	descFormatOption = strings.TrimSpace(descFormatOption)

	// override flag defaults if any corresponding properties were supplied on the incoming `opt`
	defFormatOption := "pretty"
	if opt.Format != "" {
		defFormatOption = opt.Format
	}

	defTagsOption := ""
	if opt.Tags != "" {
		defTagsOption = opt.Tags
	}

	defConcurrencyOption := 1
	if opt.Concurrency != 0 {
		defConcurrencyOption = opt.Concurrency
	}

	defShowStepDefinitions := false
	if opt.ShowStepDefinitions {
		defShowStepDefinitions = opt.ShowStepDefinitions
	}

	defStopOnFailure := false
	if opt.StopOnFailure {
		defStopOnFailure = opt.StopOnFailure
	}

	defStrict := false
	if opt.Strict {
		defStrict = opt.Strict
	}

	defNoColors := false
	if opt.NoColors {
		defNoColors = opt.NoColors
	}

	set.StringVar(&opt.Format, prefix+"format", defFormatOption, descFormatOption)
	set.StringVar(&opt.Format, prefix+"f", defFormatOption, descFormatOption)
	set.StringVar(&opt.Tags, prefix+"tags", defTagsOption, descTagsOption)
	set.StringVar(&opt.Tags, prefix+"t", defTagsOption, descTagsOption)
	set.IntVar(&opt.Concurrency, prefix+"concurrency", defConcurrencyOption, descConcurrencyOption)
	set.IntVar(&opt.Concurrency, prefix+"c", defConcurrencyOption, descConcurrencyOption)
	set.BoolVar(&opt.ShowStepDefinitions, prefix+"definitions", defShowStepDefinitions, "Print all available step definitions.")
	set.BoolVar(&opt.ShowStepDefinitions, prefix+"d", defShowStepDefinitions, "Print all available step definitions.")
	set.BoolVar(&opt.StopOnFailure, prefix+"stop-on-failure", defStopOnFailure, "Stop processing on first failed scenario.")
	set.BoolVar(&opt.Strict, prefix+"strict", defStrict, "Fail suite when there are pending or undefined or ambiguous steps.")
	set.BoolVar(&opt.NoColors, prefix+"no-colors", defNoColors, "Disable ansi colors.")
	set.Var(&randomSeed{&opt.Randomize}, prefix+"random", descRandomOption)
	set.BoolVar(&opt.ShowHelp, "godog.help", false, "Show usage help.")
	set.Func(prefix+"paths", descFeaturesArgument, func(paths string) error {
		if paths != "" {
			opt.Paths = strings.Split(paths, ",")
		}

		return nil
	})
}

type flagged struct {
	short, long, descr, dflt string
}

func (f *flagged) name() string {
	var name string
	switch {
	case len(f.short) > 0 && len(f.long) > 0:
		name = fmt.Sprintf("-%s, --%s", f.short, f.long)
	case len(f.long) > 0:
		name = fmt.Sprintf("--%s", f.long)
	case len(f.short) > 0:
		name = fmt.Sprintf("-%s", f.short)
	}

	if f.long == "random" {
		// `random` is special in that we will later assign it randomly
		// if the user specifies `--random` without specifying one,
		// so mask the "default" value here to avoid UI confusion about
		// what the value will end up being.
		name += "[=SEED]"
	} else if f.dflt != "true" && f.dflt != "false" {
		name += "=" + f.dflt
	}
	return name
}

func usage(set *flag.FlagSet, w io.Writer) func() {
	return func() {
		var list []*flagged
		var longest int
		set.VisitAll(func(f *flag.Flag) {
			var fl *flagged
			for _, flg := range list {
				if flg.descr == f.Usage {
					fl = flg
					break
				}
			}
			if nil == fl {
				fl = &flagged{
					dflt:  f.DefValue,
					descr: f.Usage,
				}
				list = append(list, fl)
			}
			if len(f.Name) > 2 {
				fl.long = f.Name
			} else {
				fl.short = f.Name
			}
		})

		for _, f := range list {
			if len(f.name()) > longest {
				longest = len(f.name())
			}
		}

		// prints an option or argument with a description, or only description
		opt := func(name, desc string) string {
			var ret []string
			lines := strings.Split(desc, "\n")
			ret = append(ret, s(2)+colors.Green(name)+s(longest+2-len(name))+lines[0])
			if len(lines) > 1 {
				for _, ln := range lines[1:] {
					ret = append(ret, s(2)+s(longest+2)+ln)
				}
			}
			return strings.Join(ret, "\n")
		}

		// --- GENERAL ---
		fmt.Fprintln(w, colors.Yellow("Usage:"))
		fmt.Fprintf(w, s(2)+"go test [options]\n\n")

		// --- OPTIONS ---
		fmt.Fprintln(w, colors.Yellow("Options:"))
		for _, f := range list {
			fmt.Fprintln(w, opt(f.name(), f.descr))
		}
		fmt.Fprintln(w, "")
	}
}

// randomSeed implements `flag.Value`, see https://golang.org/pkg/flag/#Value
type randomSeed struct {
	ref *int64
}

func (rs *randomSeed) Set(s string) error {
	if s == "true" {
		*rs.ref = makeRandomSeed()
		return nil
	}

	if s == "false" {
		*rs.ref = 0
		return nil
	}

	i, err := strconv.ParseInt(s, 10, 64)
	*rs.ref = i
	return err
}

func (rs *randomSeed) String() string {
	if rs.ref == nil {
		return "0"
	}
	return strconv.FormatInt(*rs.ref, 10)
}

// If a Value has an IsBoolFlag() bool method returning true, the command-line
// parser makes -name equivalent to -name=true rather than using the next
// command-line argument.
func (rs *randomSeed) IsBoolFlag() bool {
	return *rs.ref == 0
}

```

### File: flags_test.go
```go
package godog

import (
	"bytes"
	"flag"
	"fmt"
	"strings"
	"testing"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/internal/formatters"
)

func TestFlagsShouldRandomizeAndGenerateSeed(t *testing.T) {
	var opt Options
	flags := FlagSet(&opt)
	if err := flags.Parse([]string{"--random"}); err != nil {
		t.Fatalf("unable to parse flags: %v", err)
	}

	if opt.Randomize <= 0 {
		t.Fatal("should have generated random seed")
	}
}

func TestFlagsShouldRandomizeByGivenSeed(t *testing.T) {
	var opt Options
	flags := FlagSet(&opt)
	if err := flags.Parse([]string{"--random=123"}); err != nil {
		t.Fatalf("unable to parse flags: %v", err)
	}

	if opt.Randomize != 123 {
		t.Fatalf("expected random seed to be: 123, but it was: %d", opt.Randomize)
	}
}

func TestFlagsShouldParseFormat(t *testing.T) {
	cases := map[string][]string{
		"pretty":   {},
		"progress": {"-f", "progress"},
		"junit":    {"-f=junit"},
		"custom":   {"--format", "custom"},
		"cust":     {"--format=cust"},
	}

	for format, args := range cases {
		var opt Options
		flags := FlagSet(&opt)
		if err := flags.Parse(args); err != nil {
			t.Fatalf("unable to parse flags: %v", err)
		}

		if opt.Format != format {
			t.Fatalf("expected format: %s, but it was: %s", format, opt.Format)
		}
	}
}

func TestFlagsUsageShouldIncludeFormatDescriptons(t *testing.T) {
	var buf bytes.Buffer
	output := colors.Uncolored(&buf)

	// register some custom formatter
	Format("custom", "custom format description", formatters.JUnitFormatterFunc)

	var opt Options
	flags := FlagSet(&opt)
	usage(flags, output)()

	out := buf.String()

	for name, desc := range AvailableFormatters() {
		match := fmt.Sprintf("%s: %s\n", name, desc)
		if idx := strings.Index(out, match); idx == -1 {
			t.Fatalf("could not locate format: %s description in flag usage", name)
		}
	}
}

func TestBindFlagsShouldRespectFlagDefaults(t *testing.T) {
	opts := Options{}

	BindFlags("flagDefaults.", flag.CommandLine, &opts)

	if opts.Format != "pretty" {
		t.Fatalf("expected Format: pretty, but it was: %s", opts.Format)
	}
	if opts.Tags != "" {
		t.Fatalf("expected Tags: '', but it was: %s", opts.Tags)
	}
	if opts.Concurrency != 1 {
		t.Fatalf("expected Concurrency: 1, but it was: %d", opts.Concurrency)
	}
	if opts.ShowStepDefinitions {
		t.Fatalf("expected ShowStepDefinitions: false, but it was: %t", opts.ShowStepDefinitions)
	}
	if opts.StopOnFailure {
		t.Fatalf("expected StopOnFailure: false, but it was: %t", opts.StopOnFailure)
	}
	if opts.Strict {
		t.Fatalf("expected Strict: false, but it was: %t", opts.Strict)
	}
	if opts.NoColors {
		t.Fatalf("expected NoColors: false, but it was: %t", opts.NoColors)
	}
	if opts.Randomize != 0 {
		t.Fatalf("expected Randomize: 0, but it was: %d", opts.Randomize)
	}
}

func TestBindFlagsShouldRespectOptDefaults(t *testing.T) {
	opts := Options{
		Format:              "progress",
		Tags:                "test",
		Concurrency:         2,
		ShowStepDefinitions: true,
		StopOnFailure:       true,
		Strict:              true,
		NoColors:            true,
		Randomize:           int64(7),
	}

	flagSet := flag.FlagSet{}

	BindFlags("optDefaults.", &flagSet, &opts)

	if opts.Format != "progress" {
		t.Fatalf("expected Format: progress, but it was: %s", opts.Format)
	}
	if opts.Tags != "test" {
		t.Fatalf("expected Tags: 'test', but it was: %s", opts.Tags)
	}
	if opts.Concurrency != 2 {
		t.Fatalf("expected Concurrency: 2, but it was: %d", opts.Concurrency)
	}
	if !opts.ShowStepDefinitions {
		t.Fatalf("expected ShowStepDefinitions: true, but it was: %t", opts.ShowStepDefinitions)
	}
	if !opts.StopOnFailure {
		t.Fatalf("expected StopOnFailure: true, but it was: %t", opts.StopOnFailure)
	}
	if !opts.Strict {
		t.Fatalf("expected Strict: true, but it was: %t", opts.Strict)
	}
	if !opts.NoColors {
		t.Fatalf("expected NoColors: true, but it was: %t", opts.NoColors)
	}
	if opts.Randomize != 7 {
		t.Fatalf("expected Randomize: 7, but it was: %d", opts.Randomize)
	}
}

func TestBindFlagsShouldRespectFlagOverrides(t *testing.T) {
	opts := Options{
		Format:              "progress",
		Tags:                "test",
		Concurrency:         2,
		ShowStepDefinitions: true,
		StopOnFailure:       true,
		Strict:              true,
		NoColors:            true,
		Randomize:           11,
	}
	flagSet := flag.FlagSet{}

	BindFlags("optOverrides.", &flagSet, &opts)

	flagSet.Parse([]string{
		"--optOverrides.format=junit",
		"--optOverrides.tags=test2",
		"--optOverrides.concurrency=3",
		"--optOverrides.definitions=false",
		"--optOverrides.stop-on-failure=false",
		"--optOverrides.strict=false",
		"--optOverrides.no-colors=false",
		"--optOverrides.random=2",
	})

	if opts.Format != "junit" {
		t.Fatalf("expected Format: junit, but it was: %s", opts.Format)
	}
	if opts.Tags != "test2" {
		t.Fatalf("expected Tags: 'test2', but it was: %s", opts.Tags)
	}
	if opts.Concurrency != 3 {
		t.Fatalf("expected Concurrency: 3, but it was: %d", opts.Concurrency)
	}
	if opts.ShowStepDefinitions {
		t.Fatalf("expected ShowStepDefinitions: true, but it was: %t", opts.ShowStepDefinitions)
	}
	if opts.StopOnFailure {
		t.Fatalf("expected StopOnFailure: true, but it was: %t", opts.StopOnFailure)
	}
	if opts.Strict {
		t.Fatalf("expected Strict: true, but it was: %t", opts.Strict)
	}
	if opts.NoColors {
		t.Fatalf("expected NoColors: true, but it was: %t", opts.NoColors)
	}
	if opts.Randomize != 2 {
		t.Fatalf("expected Randomize: 2, but it was: %d", opts.Randomize)
	}
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
