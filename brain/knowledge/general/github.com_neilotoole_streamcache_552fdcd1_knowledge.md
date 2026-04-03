---
id: github.com-neilotoole-streamcache-552fdcd1-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:04.647118
---

# KNOWLEDGE EXTRACT: github.com_neilotoole_streamcache_552fdcd1
> **Extracted on:** 2026-04-01 09:09:59
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519969/github.com_neilotoole_streamcache_552fdcd1

---

## File: `.gitignore`
```
# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary, built with `go test -c`
*.test

# Output of the go coverage tool, specifically when used with LiteIDE
*.out

# Dependency directories (remove the comment below to include it)
# vendor/
### Go template
# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary, built with `go test -c`
*.test

# Output of the go coverage tool, specifically when used with LiteIDE
*.out

# Dependency directories (remove the comment below to include it)
# vendor/

*.iml
.idea


```

## File: `.golangci.yml`
```yaml
# This code is licensed under the terms of the MIT license.

## Golden config for golangci-lint v1.55.2
#
# This is the best config for golangci-lint based on my experience and opinion.
# It is very strict, but not extremely strict.
# Feel free to adopt and change it for your needs.
#
# @neilotoole: ^^ Well, it's less strict now!
# Based on: https://gist.github.com/maratori/47a4d00457a92aa426dbd48a18776322

run:
  # Timeout for analysis, e.g. 30s, 5m.
  # Default: 1m
  timeout: 5m

  tests: true

  skip-dirs:

  skip-files:
    - internal/chanmu/stdlib_test.go

output:
  sort-results: true

# This file contains only configs which differ from defaults.
# All possible options can be found here https://github.com/golangci/golangci-lint/blob/master/.golangci.reference.yml
linters-settings:
  cyclop:
    # The maximal code complexity to report.
    # Default: 10
    max-complexity: 50
    # The maximal average package complexity.
    # If it's higher than 0.0 (float) the check is enabled
    # Default: 0.0
    package-average: 10.0

  errcheck:
    # Report about not checking of errors in type assertions: `a := b.(MyStruct)`.
    # Such cases aren't reported by default.
    # Default: false
    check-type-assertions: true

  exhaustive:
    # Program elements to check for exhaustiveness.
    # Default: [ switch ]
    check:
      - switch
      - map

  funlen:
    # Checks the number of lines in a function.
    # If lower than 0, disable the check.
    # Default: 60
    lines: 150
    # Checks the number of statements in a function.
    # If lower than 0, disable the check.
    # Default: 40
    statements: 100

  gocognit:
    # Minimal code complexity to report
    # Default: 30 (but we recommend 10-20)
    min-complexity: 50

  gocritic:
    # Settings passed to gocritic.
    # The settings key is the name of a supported gocritic checker.
    # The list of supported checkers can be find in https://go-critic.github.io/overview.
    settings:
      captLocal:
        # Whether to restrict checker to params only.
        # Default: true
        paramsOnly: false
      underef:
        # Whether to skip (*x).method() calls where x is a pointer receiver.
        # Default: true
        skipRecvDeref: false

  gocyclo:
    # Minimal code complexity to report.
    # Default: 30 (but we recommend 10-20)
    min-complexity: 50

  gofumpt:
    # Module path which contains the source code being formatted.
    # Default: ""
    module-path: github.com/neilotoole/streamcache
    # Choose whether to use the extra rules.
    # Default: false
    extra-rules: true

  gomnd:
    # List of function patterns to exclude from analysis.
    # Values always ignored: `time.Date`,
    # `strconv.FormatInt`, `strconv.FormatUint`, `strconv.FormatFloat`,
    # `strconv.ParseInt`, `strconv.ParseUint`, `strconv.ParseFloat`.
    # Default: []
    ignored-functions:
      - make
      - os.Chmod
      - os.Mkdir
      - os.MkdirAll
      - os.OpenFile
      - os.WriteFile
      - prometheus.ExponentialBuckets
      - prometheus.ExponentialBucketsRange
      - prometheus.LinearBuckets
    ignored-numbers:
      - "2"
      - "3"

  gomodguard:
    blocked:
      # List of blocked modules.
      # Default: []
      modules:
        - github.com/golang/protobuf:
            recommendations:
              - google.golang.org/protobuf
            reason: "see https://developers.google.com/protocol-buffers/docs/reference/go/faq#modules"
        - github.com/satori/go.uuid:
            recommendations:
              - github.com/google/uuid
            reason: "satori's package is not maintained"
        - github.com/gofrs/uuid:
            recommendations:
              - github.com/google/uuid
            reason: "gofrs' package is not go module"

  govet:
    # Enable all analyzers.
    # Default: false
    enable-all: true
    # Disable analyzers by name.
    # Run `go tool vet help` to see all analyzers.
    # Default: []
    disable:
#      - fieldalignment # too strict
    # Settings per analyzer.
    settings:
      shadow:
        # Whether to be strict about shadowing; can be noisy.
        # Default: false
        strict: false

  lll:
    # Max line length, lines longer will be reported.
    # '\t' is counted as 1 character by default, and can be changed with the tab-width option.
    # Default: 120.
    line-length: 120
    # Tab width in spaces.
    # Default: 1
    tab-width: 1

  nakedret:
    # Make an issue if func has more lines of code than this setting, and it has naked returns.
    # Default: 30
    max-func-lines: 0

  nestif:
    # Minimal complexity of if statements to report.
    # Default: 5
    min-complexity: 20

  nolintlint:
    # Exclude following linters from requiring an explanation.
    # Default: []
    allow-no-explanation: [ funlen, gocognit, lll ]
    # Enable to require an explanation of nonzero length after each nolint directive.
    # Default: false
    require-explanation: false
    # Enable to require nolint directives to mention the specific linter being suppressed.
    # Default: false
    require-specific: true

  revive:
    # https://golangci-lint.run/usage/linters/#revive
    rules:

      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#add-constant
      - name: add-constant
        disabled: true
        arguments:
          - maxLitCount: "3"
            allowStrs: '""'
            allowInts: "0,1,2"
            allowFloats: "0.0,0.,1.0,1.,2.0,2."
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#argument-limit
      - name: argument-limit
        disabled: false
        arguments: [ 7 ]
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#atomic
      - name: atomic
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#banned-characters
      - name: banned-characters
        disabled: true
        arguments: [ "Ω", "Σ", "σ", "7" ]
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#bare-return
      - name: bare-return
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#blank-imports
      - name: blank-imports
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#bool-literal-in-expr
      - name: bool-literal-in-expr
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#call-to-gc
      - name: call-to-gc
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#cognitive-complexity
      - name: cognitive-complexity
        disabled: true
        arguments: [ 7 ]
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#comment-spacings
      - name: comment-spacings
        disabled: true
        arguments:
          - mypragma
          - otherpragma
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#confusing-naming
      - name: confusing-naming
        disabled: true
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#confusing-results
      - name: confusing-results
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#constant-logical-expr
      - name: constant-logical-expr
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#context-as-argument
      - name: context-as-argument
        disabled: false
        arguments:
          - allowTypesBefore: "*testing.T,*github.com/user/repo/testing.Harness"
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#context-keys-type
      - name: context-keys-type
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#cyclomatic
      - name: cyclomatic
        disabled: true
        arguments: [ 3 ]
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#datarace
      - name: datarace
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#deep-exit
      - name: deep-exit
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#defer
      - name: defer
        disabled: false
        arguments:
          - [ "call-chain", "loop" ]
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#dot-imports
      - name: dot-imports
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#duplicated-imports
      - name: duplicated-imports
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#early-return
      - name: early-return
        disabled: false
        arguments:
          - "preserveScope"
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#empty-block
      - name: empty-block
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#empty-lines
      - name: empty-lines
        disabled: true # Covered by "whitespace" linter.
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#enforce-map-style
      - name: enforce-map-style
        disabled: true
        arguments:
          - "make"
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#error-naming
      - name: error-naming
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#error-return
      - name: error-return
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#error-strings
      - name: error-strings
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#errorf
      - name: errorf
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#file-header
      - name: file-header
        disabled: true
#        arguments:
#          - This is the text that must appear at the top of source files.
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#flag-parameter
      - name: flag-parameter
        disabled: true
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#function-result-limit
      - name: function-result-limit
        disabled: false
        arguments: [ 4 ]
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#function-length
      - name: function-length
        disabled: true
        arguments: [ 10, 0 ]
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#get-return
      - name: get-return
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#identical-branches
      - name: identical-branches
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#if-return
      - name: if-return
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#increment-decrement
      - name: increment-decrement
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#indent-error-flow
      - name: indent-error-flow
        disabled: false
        arguments:
          - "preserveScope"
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#import-alias-naming
      - name: import-alias-naming
        disabled: false
        arguments:
          - "^[a-z][a-z0-9]{0,}$"
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#imports-blacklist
      - name: imports-blacklist
        disabled: false
        arguments:
          - "crypto/md5"
          - "crypto/sha1"
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#import-shadowing
      - name: import-shadowing
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#line-length-limit
      - name: line-length-limit
        disabled: true
        arguments: [ 80 ]
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#max-public-structs
      - name: max-public-structs
        disabled: true
        arguments: [ 3 ]
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#modifies-parameter
      - name: modifies-parameter
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#modifies-value-receiver
      - name: modifies-value-receiver
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#nested-structs
      - name: nested-structs
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#optimize-operands-order
      - name: optimize-operands-order
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#package-comments
      - name: package-comments
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#range
      - name: range
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#range-val-in-closure
      - name: range-val-in-closure
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#range-val-address
      - name: range-val-address
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#receiver-naming
      - name: receiver-naming
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#redundant-import-alias
      - name: redundant-import-alias
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#redefines-builtin-id
      - name: redefines-builtin-id
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#string-of-int
      - name: string-of-int
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#string-format
      - name: string-format
        disabled: false
        arguments:
          - - 'core.WriteError[1].Message'
            - '/^([^A-Z]|$)/'
            - must not start with a capital letter
          - - 'fmt.Errorf[0]'
            - '/(^|[^\.!?])$/'
            - must not end in punctuation
          - - panic
            - '/^[^\n]*$/'
            - must not contain line breaks
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#struct-tag
      - name: struct-tag
        arguments:
          - "json,inline"
          - "bson,outline,gnu"
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#superfluous-else
      - name: superfluous-else
        disabled: false
        arguments:
          - "preserveScope"
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#time-equal
      - name: time-equal
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#time-naming
      - name: time-naming
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#var-naming
      - name: var-naming
        disabled: false
        arguments:
          - [ "ID" ] # AllowList
          - [ "VM" ] # DenyList
          - - upperCaseConst: true
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#var-declaration
      - name: var-declaration
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#unconditional-recursion
      - name: unconditional-recursion
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#unexported-naming
      - name: unexported-naming
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#unexported-return
      - name: unexported-return
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#unhandled-error
      - name: unhandled-error
        disabled: false
        arguments:
          - "fmt.Printf"
          - "fmt.Fprintf"
          - "fmt.Fprint"
          - "fmt.Fprintln"
          - "bytes.Buffer.Write"
          - "bytes.Buffer.WriteByte"
          - "bytes.Buffer.WriteString"
          - "bytes.Buffer.WriteRune"
          - "strings.Builder.WriteString"
          - "strings.Builder.WriteRune"
          - "strings.Builder.Write"
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#unnecessary-stmt
      - name: unnecessary-stmt
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#unreachable-code
      - name: unreachable-code
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#unused-parameter
      - name: unused-parameter
        disabled: false
        arguments:
          - allowRegex: "^_"
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#unused-receiver
      - name: unused-receiver
        disabled: true
        arguments:
          - allowRegex: "^_"
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#useless-break
      - name: useless-break
        disabled: false
      # https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md#waitgroup-by-value
      - name: waitgroup-by-value
        disabled: false

  rowserrcheck:
    # database/sql is always checked
    # Default: []
    packages:
      - github.com/jmoiron/sqlx

  tenv:
    # The option `all` will run against whole test files (`_test.go`) regardless of method/function signatures.
    # Otherwise, only methods that take `*testing.T`, `*testing.B`, and `testing.TB` as arguments are checked.
    # Default: false
    all: true


linters:
  disable-all: true

  enable:
    ## enabled by default
    - errcheck # checking for unchecked errors, these unchecked errors can be critical bugs in some cases
    - gosimple # specializes in simplifying a code
    - govet # reports suspicious constructs, such as Printf calls whose arguments do not align with the format string
    - ineffassign # detects when assignments to existing variables are not used
    - staticcheck # is a go vet on steroids, applying a ton of static analysis checks
    - typecheck # like the front-end of a Go compiler, parses and type-checks Go code
    - unused # checks for unused constants, variables, functions and types


#    ## disabled by default
    - asasalint # checks for pass []any as any in variadic func(...any)
    - asciicheck # checks that your code does not contain non-ASCII identifiers
    - bidichk # checks for dangerous unicode character sequences
    - bodyclose # checks whether HTTP response body is closed successfully
    - cyclop # checks function and package cyclomatic complexity
    - dupl # tool for code clone detection
    - durationcheck # checks for two durations multiplied together
    - errname # checks that sentinel errors are prefixed with the Err and error types are suffixed with the Error
    - errorlint # finds code that will cause problems with the error wrapping scheme introduced in Go 1.13
    - execinquery # checks query string in Query function which reads your Go src files and warning it finds
    - exhaustive # checks exhaustiveness of enum switch statements
    - exportloopref # checks for pointers to enclosing loop variables
    - forbidigo # forbids identifiers
    - funlen # tool for detection of long functions
    - gochecknoinits # checks that no init functions are present in Go code
    - gocognit # computes and checks the cognitive complexity of functions
    - goconst # finds repeated strings that could be replaced by a constant
    - gocritic # provides diagnostics that check for bugs, performance and style issues
    - gocyclo # computes and checks the cyclomatic complexity of functions
    - godot # checks if comments end in a period
    - gofumpt
    - goimports # in addition to fixing imports, goimports also formats your code in the same style as gofmt
#    - gomoddirectives # manages the use of 'replace', 'retract', and 'excludes' directives in go.mod
    - gomodguard # allow and block lists linter for direct Go module dependencies. This is different from depguard where there are different block types for example version constraints and module recommendations
    - goprintffuncname # checks that printf-like functions are named with f at the end
    - gosec # inspects source code for security problems
    - lll # reports long lines
    - loggercheck # checks key value pairs for common logger libraries (kitlog,klog,logr,zap)
    - makezero # finds slice declarations with non-zero initial length
    - nakedret # finds naked returns in functions greater than a specified function length
    - nestif # reports deeply nested if statements
    - nilerr # finds the code that returns nil even if it checks that the error is not nil
    - nilnil # checks that there is no simultaneous return of nil error and an invalid value
    - noctx # finds sending http request without context.Context
    - nolintlint # reports ill-formed or insufficient nolint directives
    - nosprintfhostport # checks for misuse of Sprintf to construct a host with port in a URL
    - predeclared # finds code that shadows one of Go's predeclared identifiers
    - promlinter # checks Prometheus metrics naming via promlint
    - reassign # checks that package variables are not reassigned
    - revive # fast, configurable, extensible, flexible, and beautiful linter for Go, drop-in replacement of golint
    - stylecheck # is a replacement for golint
    - tenv # detects using os.Setenv instead of t.Setenv since Go1.17
    - testableexamples # checks if examples are testable (have an expected output)
    - tparallel # detects inappropriate usage of t.Parallel() method in your Go test codes
    - unconvert # removes unnecessary type conversions
    - unparam # reports unused function parameters
    - usestdlibvars # detects the possibility to use variables/constants from the Go standard library
    - whitespace # detects leading and trailing whitespace

    ## These three linters are disabled for now due to generics: https://github.com/golangci/golangci-lint/issues/2649
    #- rowserrcheck # checks whether Err of rows is checked successfully  # Disabled because:  https://github.com/golangci/golangci-lint/issues/2649
    #- sqlclosecheck # checks that sql.Rows and sql.Stmt are closed
    #- wastedassign # finds wasted assignment statements


    ## you may want to enable
    #- decorder # checks declaration order and count of types, constants, variables and functions
    #- exhaustruct # checks if all structure fields are initialized
    #- gochecknoglobals # checks that no global variables exist
    #- godox # detects FIXME, TODO and other comment keywords
    #- goheader # checks is file header matches to pattern
    #- gomnd # detects magic numbers
    #- interfacebloat # checks the number of methods inside an interface
    #- ireturn # accept interfaces, return concrete types
    #- prealloc # [premature optimization, but can be used in some cases] finds slice declarations that could potentially be preallocated
    #- varnamelen # [great idea, but too many false positives] checks that the length of a variable's name matches its scope
    #- wrapcheck # checks that errors returned from external packages are wrapped

    ## disabled
    #- containedctx # detects struct contained context.Context field
    #- contextcheck # [too many false positives] checks the function whether use a non-inherited context
    #- depguard # [replaced by gomodguard] checks if package imports are in a list of acceptable packages
    #- dogsled # checks assignments with too many blank identifiers (e.g. x, _, _, _, := f())
    #- dupword # [useless without config] checks for duplicate words in the source code
    #- errchkjson # [don't see profit + I'm against of omitting errors like in the first example https://github.com/breml/errchkjson] checks types passed to the json encoding functions. Reports unsupported types and optionally reports occasions, where the check for the returned error can be omitted
    #- forcetypeassert # [replaced by errcheck] finds forced type assertions
    #- goerr113 # [too strict] checks the errors handling expressions
    #- gofmt # [replaced by goimports] checks whether code was gofmt-ed
    #- gofumpt # [replaced by goimports, gofumports is not available yet] checks whether code was gofumpt-ed
    #- grouper # analyzes expression groups
    #- importas # enforces consistent import aliases
    #- maintidx # measures the maintainability index of each function
    #- misspell # [useless] finds commonly misspelled English words in comments
    #- nlreturn # [too strict and mostly code is not more readable] checks for a new line before return and branch statements to increase code clarity
    #- paralleltest # [too many false positives] detects missing usage of t.Parallel() method in your Go test
    #- tagliatelle # checks the struct tags
    #- thelper # detects golang test helpers without t.Helper() call and checks the consistency of test helpers
    #- wsl # [too strict and mostly code is not more readable] whitespace linter forces you to use empty lines

    ## deprecated
    #- deadcode # [deprecated, replaced by unused] finds unused code
    #- exhaustivestruct # [deprecated, replaced by exhaustruct] checks if all struct's fields are initialized
    #- golint # [deprecated, replaced by revive] golint differs from gofmt. Gofmt reformats Go source code, whereas golint prints out style mistakes
    #- ifshort # [deprecated] checks that your code uses short syntax for if-statements whenever possible
    #- interfacer # [deprecated] suggests narrower interface types
    #- maligned # [deprecated, replaced by govet fieldalignment] detects Go structs that would take less memory if their fields were sorted
    #- nosnakecase # [deprecated, replaced by revive var-naming] detects snake case of variable naming and function name
    #- scopelint # [deprecated, replaced by exportloopref] checks for unpinned variables in go programs
    #- structcheck # [deprecated, replaced by unused] finds unused struct fields
    #- varcheck # [deprecated, replaced by unused] finds unused global variables and constants


issues:
  # Maximum count of issues with the same text.
  # Set to 0 to disable.
  # Default: 3
  max-same-issues: 3

  exclude-rules:
    - source: "^//\\s*go:generate\\s"
      linters: [ lll ]
    - source: "(noinspection|TODO)"
      linters: [ godot ]
    - source: "//noinspection"
      linters: [ gocritic ]
    - source: "^\\s+if _, ok := err\\.\\([^.]+\\.InternalError\\); ok {"
      linters: [ errorlint ]
    - path: "_test\\.go"
      linters:
        - bodyclose
        - dupl
        - funlen
        - goconst
        - gosec
        - noctx
        - wrapcheck
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2021+ Neil O'Toole

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# streamcache: in-memory caching stream reader

[![Go Reference](https://pkg.go.dev/badge/github.com/neilotoole/streamcache.svg)](https://pkg.go.dev/github.com/neilotoole/streamcache)
[![Go Report Card](https://goreportcard.com/badge/neilotoole/streamcache)](https://goreportcard.com/report/neilotoole/streamcache)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/neilotoole/streamcache/blob/master/LICENSE)
![Workflow](https://github.com/neilotoole/streamcache/actions/workflows/go.yml/badge.svg)


Package [`streamcache`](https://pkg.go.dev/github.com/neilotoole/streamcache)
implements a Go in-memory byte cache mechanism that allows multiple callers to
read some or all of the contents of a source `io.Reader`, while only reading
from the source reader once. When only the final reader remains, the cache is
discarded and the final reader reads directly from the source. This is particularly
useful for scenarios where multiple readers may wish to sample the start of a
stream, but only one reader will read the entire stream.

Let's say we have a program [`typedetect`](./examples/typedetect),
and we're reading from ``stdin``. For example:

```shell
$ cat myfile.ext | typedetect  
```

In this scenario, `typedetect` wants to detect
and print the type of data in the file/pipe, and then print the contents.
That detection sampling could be done in a separate goroutine per sampler type.
The input file could be, let's say, a JSON file, or an XML file.

The obvious approach is to inspect the first few tokens of the
input, and check if the tokens are either valid JSON or valid XML.
After that process, let's say we want to dump out a preview of the file contents.

Package `streamcache` provides a facility to create a `Stream` from an
underlying `io.Reader` (`os.Stdin` in this scenario), and spawn multiple
readers, each of which can operate independently, in their own
goroutines if desired. The underlying source (again, `os.Stdin` in this
scenario) will only once be read from, but its data is available to
multiple readers, because that data is cached in memory.

That is, until there's only one final reader left, (after invoking
`Stream.Seal`), at which point the cache is discarded, and
the final `Reader` reads directly from the underlying source.

## Usage

Add to your `go.mod` via `go get`:

```shell
go get github.com/neilotoole/streamcache
```

Here's a simple [example](./examples/in-out-err) that copies the contents
of `stdin` to `stdout` and `stderr`, and prints the number of bytes read.

```go
package main

import (
    "context"
    "errors"
    "fmt"
    "io"
    "os"

    "github.com/neilotoole/streamcache"
)

// Write stdin to both stdout and stderr.
// Some error handling omitted for brevity.
func main() {
    ctx := context.Background()
    stream := streamcache.New(os.Stdin)

    r1 := stream.NewReader(ctx)
    go func() {
        defer r1.Close()
        io.Copy(os.Stdout, r1)
    }()

    r2 := stream.NewReader(ctx)
    go func() {
        defer r2.Close()
        io.Copy(os.Stderr, r2)
    }()
    
    stream.Seal()   // Indicate that there'll be no more readers...
    <-stream.Done() // Receives when all readers are closed.

    if err := stream.Err(); err != nil && !errors.Is(err, io.EOF) {
        fmt.Fprintln(os.Stderr, "error:", err)
        os.Exit(1)
    }

    fmt.Fprintf(os.Stdout, "Read %d bytes from stdin\n", stream.Size())
}
```

Executing the above program:

```shell
$ go install github.com/neilotoole/streamcache/examples/in-out-err
$ echo "hello world" | in-out-err
hello world
hello world
Read 12 bytes from stdin
```

## Examples

- [`in-out-err`](./examples/in-out-err): copy `stdin` to both `stdout` and `stderr`.
- [`typedetect`](./examples/typedetect): detect the type of input data, and print the head and tail
  of the contents.
  ![streamcache_typedetect.png](examples/typedetect/streamcache_typedetect.png)
- [`multicase`](./examples/multicase): transform each line of input to upper, lower, and title case.
  ![streamcache_multicase.png](examples/multicase/streamcache_multicase.png)

## Related work

- [`djherbis/fscache`](https://github.com/djherbis/fscache)
- [`sq`](https://github.com/neilotoole/sq) uses `streamcache` to stream stdin / HTTP response bodies,
  allowing `sq` to being processing data on the fly.
  ![sq streamcache](https://github.com/neilotoole/sq/blob/master/.images/sq_inspect_remote_s3.png)
- [`fifomu`](https://github.com/neilotoole/fifomu) is a FIFO mutex, used by `streamcache`, which in turn is used by [`sq`](https://github.com/neilotoole/sq).
```

## File: `go.mod`
```
module github.com/neilotoole/streamcache

go 1.20

require (
	github.com/neilotoole/fifomu v0.1.2
	github.com/stretchr/testify v1.9.0
)

require (
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
```

## File: `go.sum`
```
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/neilotoole/fifomu v0.1.2 h1:sgJhcOTlEXGVj/nS5Bb8/qV+1wgmk+KPavcNuDw0rDM=
github.com/neilotoole/fifomu v0.1.2/go.mod h1:9di2j+xBgr+nX6IPmpwQVxKt6yzgPLk9WXEj/aLwcao=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/stretchr/testify v1.9.0 h1:HtqpIVDClZ4nwg75+f6Lvsy/wHu+3BoSGCbBAcpTsTg=
github.com/stretchr/testify v1.9.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
golang.org/x/sync v0.6.0 h1:5BMeUDZ7vkXGfEr1x9B4bRcTH4lpkTkpdh0T/J+qjbQ=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `helper_test.go`
```go
package streamcache_test

// File helper_test.go contains test helper functionality.

import (
	"context"
	crand "crypto/rand"
	"errors"
	"fmt"
	"io"
	mrand "math/rand"
	"os"
	"strconv"
	"sync"
	"testing"
	"time"

	"github.com/stretchr/testify/require"

	"github.com/neilotoole/streamcache"
)

var _ io.Reader = (*delayReader)(nil)

// newDelayReader returns an io.Reader that delays on each read from r.
// If jitter is true, a randomized jitter factor is added to the delay.
// If r implements io.Closer, the returned reader will also
// implement io.Closer; if r doesn't implement io.Closer,
// the returned reader will not implement io.Closer.
// If r is nil, nil is returned.
func newDelayReader(r io.Reader, delay time.Duration, jitter bool) io.Reader {
	if r == nil {
		return nil
	}

	dr := delayReader{r: r, delay: delay, jitter: jitter}
	if _, ok := r.(io.Closer); ok {
		return delayReadCloser{dr}
	}
	return dr
}

var _ io.Reader = (*delayReader)(nil)

type delayReader struct {
	r      io.Reader
	delay  time.Duration
	jitter bool
}

// Read implements io.Reader.
func (d delayReader) Read(p []byte) (n int, err error) {
	delay := d.delay
	if d.jitter {
		delay += time.Duration(mrand.Int63n(int64(d.delay))) / 3
	}

	time.Sleep(delay)
	return d.r.Read(p)
}

type delayReadCloser struct {
	delayReader
}

// Close implements io.Closer.
func (d delayReadCloser) Close() error {
	if c, ok := d.r.(io.Closer); ok {
		return c.Close()
	}
	return nil
}

// newErrorAfterNReader returns an io.Reader that returns err after
// reading n random bytes from crypto/rand.Reader.
func newErrorAfterNReader(n int, err error) io.Reader {
	return &errorAfterNReader{afterN: n, err: err}
}

type errorAfterNReader struct {
	err    error
	mu     sync.Mutex
	afterN int
	count  int
}

func (r *errorAfterNReader) Read(p []byte) (n int, err error) {
	r.mu.Lock()
	defer r.mu.Unlock()

	if r.count >= r.afterN {
		return 0, r.err
	}

	// There's some bytes to read
	allowed := r.afterN - r.count
	if allowed > len(p) {
		n, _ = crand.Read(p)
		r.count += n
		return n, nil
	}
	n, _ = crand.Read(p[:allowed])
	if n != allowed {
		panic(fmt.Sprintf("expected to readMain %d bytes, got %d", allowed, n))
	}
	r.count += n
	return n, r.err
}

// newLimitRandReader returns an io.Reader that reads up to limit bytes
// from crypto/rand.Reader.
func newLimitRandReader(limit int64) io.Reader {
	return io.LimitReader(crand.Reader, limit)
}

var _ io.Reader = (*rcRecorder)(nil)

// rcRecorder wraps an io.Reader and records stats.
type rcRecorder struct {
	r          io.Reader
	closeCount int
	size       int
	mu         sync.Mutex
}

func (rc *rcRecorder) Read(p []byte) (n int, err error) {
	rc.mu.Lock()
	defer rc.mu.Unlock()

	n, err = rc.r.Read(p)
	rc.size += n
	return n, err
}

// Close implements io.Close, and increments its closed field each
// time that Close is invoked.
func (rc *rcRecorder) Close() error {
	rc.mu.Lock()
	defer rc.mu.Unlock()
	rc.closeCount++
	if c, ok := rc.r.(io.ReadCloser); ok {
		return c.Close()
	}

	return nil
}

var _ io.Reader = (*tweakableReader)(nil)

// tweakableReader is an io.Reader that can be configured
// by test code. Each call to Read consults the reader's fields anew.
// It is typical for test code to manipulate those fields between
// calls to Read. Note that if the unblock channel field is non-nil,
// it must be closed or have a value sent on it for Read to proceed.
type tweakableReader struct {
	unblock chan struct{}
	err     error
	data    []byte
}

// Read implements io.Reader. Each call to Read consults the
// reader's fields.
func (r *tweakableReader) Read(p []byte) (n int, err error) {
	if r.unblock != nil {
		<-r.unblock
	}
	n = copy(p, r.data)
	return n, r.err
}

// requireNoTake fails if a value is taken from c.
func requireNoTake[C any](tb testing.TB, c <-chan C, msgAndArgs ...any) {
	tb.Helper()
	select {
	case <-c:
		require.Fail(tb, "unexpected take from channel", msgAndArgs...)
	default:
	}
}

// requireTake fails if a value is not taken from c.
func requireTake[C any](tb testing.TB, c <-chan C, msgAndArgs ...any) {
	tb.Helper()
	select {
	case <-c:
	default:
		require.Fail(tb, "unexpected failure to take from channel", msgAndArgs...)
	}
}

// totalTimeout is used by requireTotal and requireNoTotal.
const totalTimeout = time.Millisecond * 100

// requireNoTotal requires that s.Total blocks.
func requireNoTotal(tb testing.TB, s *streamcache.Stream) {
	tb.Helper()

	failErr := errors.New("fail")
	ctx, cancel := context.WithCancelCause(context.Background())

	var (
		size int
		err  error
		wait = make(chan struct{})
	)

	go func() {
		time.AfterFunc(totalTimeout, func() {
			cancel(failErr)
		})
		size, err = s.Total(ctx)
		wait <- struct{}{}
	}()

	<-wait
	require.Error(tb, err)
	require.True(tb, errors.Is(err, failErr))
	require.Equal(tb, 0, size)
}

// requireTotal requires that s.Total doesn't block, and
// that s.Total returns want and no error.
func requireTotal(tb testing.TB, s *streamcache.Stream, want int) {
	tb.Helper()

	var (
		ctx, cancel = context.WithCancelCause(context.Background())
		err         error
		size        int
		wait        = make(chan struct{})
	)

	go func() {
		time.AfterFunc(totalTimeout, func() {
			cancel(errors.New("fail"))
		})
		size, err = s.Total(ctx)
		wait <- struct{}{}
	}()

	<-wait
	require.NoError(tb, err)
	require.Equal(tb, want, size)
}

// generateSampleFile generates a temp file of sample data with the
// specified number of rows. It is the caller's responsibility to
// close the file. Note that the file is removed by t.Cleanup.
func generateSampleFile(tb testing.TB, rows int) (size int, fp string) {
	f, err := os.CreateTemp("", "")
	require.NoError(tb, err)
	fp = f.Name()

	const line = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
	for i := 0; i < rows; i++ {
		// Actual data lines will look like:
		//  0,A,B,C...
		//  1,A,B,C...
		s := strconv.Itoa(i) + "," + line
		_, err = fmt.Fprintln(f, s)
		require.NoError(tb, err)
	}

	require.NoError(tb, f.Close())
	fi, err := os.Stat(fp)
	require.NoError(tb, err)
	size = int(fi.Size())
	tb.Logf("Generated sample file [%d]: %s", size, fp)
	return int(fi.Size()), fp
}

func sleepJitter() {
	const jitterFactor = 30
	d := time.Millisecond * time.Duration(mrand.Intn(jitterFactor))
	time.Sleep(d)
}
```

## File: `internal_test.go`
```go
package streamcache

// internal_test.go contains functions that
// expose internal state for testing.

// ReaderOffset returns the current offset of the reader.
func ReaderOffset(r *Reader) int {
	return r.offset
}

// CacheInternal returns c's internal cache byte slice.
func CacheInternal(c *Stream) []byte {
	return c.cache
}
```

## File: `streamcache.go`
```go
// Package streamcache implements an in-memory cache mechanism that allows
// multiple callers to read some or all of the contents of a source reader,
// while only reading from the source reader once; when there's only one final
// reader remaining, the cache is discarded and the final reader reads directly
// from the source.
//
// Let's say we're reading from stdin. For example:
//
//	$ cat myfile.ext | myprogram
//
// In this scenario, myprogram wants to detect the type of data in the
// file/pipe, and then print it out. That sampling could be done in a separate
// goroutine per sampler type. The input file could be, let's say, a CSV file,
// or a JSON file.
//
// The obvious approach is to inspect the first few lines of the input, and
// check if the input is either valid CSV, or valid JSON. After that process,
// let's say we want to dump out the entire contents of the input.
//
// Package streamcache provides a facility to create a caching Stream from an
// underlying io.Reader (os.Stdin in this scenario), and spawn multiple readers,
// each of which can operate independently, in their own goroutines if desired.
// The underlying source (again, os.Stdin in this scenario) will only be read
// from once, but its data is available to multiple readers, because that data
// is cached in memory.
//
// That is, until after Stream.Seal is invoked: when there's only one final
// reader left, the cache is discarded, and the final reader reads directly from
// the underlying source.
//
// The entrypoint to this package is streamcache.New, which returns a new Stream
// instance, from which readers can be created via Stream.NewReader.
package streamcache

import (
	"context"
	"errors"
	"io"
	"sync"

	"github.com/neilotoole/fifomu"
)

// ErrAlreadyClosed is returned by Reader.Read if the reader is
// already closed.
var ErrAlreadyClosed = errors.New("reader is already closed")

// Stream mediates access to the bytes of an underlying source io.Reader.
// Multiple callers can invoke Stream.NewReader to obtain a Reader, each of
// which can read the full or partial contents of the source reader. Note that
// the source is only read from once, and the returned bytes are cached in
// memory. After Stream.Seal is invoked and readers are closed, the final reader
// discards the cache and reads directly from the source for the remaining
// bytes.
type Stream struct {
	// src is the underlying reader from which bytes are read.
	src io.Reader

	// readErr is the first (and only) error returned by src's Read method. Once
	// readErr has been set to a non-nil value, src is never read from again.
	readErr error

	// rdrsDoneCh is closed after the Stream is sealed and the last reader is
	// closed. See Stream.Done.
	rdrsDoneCh chan struct{}

	// srcDoneCh is closed when the underlying source reader returns an error,
	// including io.EOF. See Stream.Filled.
	srcDoneCh chan struct{}

	// rdrs is the set of unclosed Reader instances created by Stream.NewReader.
	// When a Reader is closed, it is removed from this slice. Note that the
	// element order may not match the Reader creation order, as the slice may
	// be reordered by removeElement during Stream.close.
	rdrs []*Reader

	// cache holds the accumulated bytes read from src. It is nilled when the
	// final reader switches to readSrcDirect.
	cache []byte

	// srcMu guards concurrent access to reading from src. Note that it is not
	// an instance of sync.Mutex, but instead fifomu.Mutex, which is a mutex
	// whose Lock method returns the lock to callers in FIFO call order. This is
	// important in Stream.readMain because, as implemented, a reader could get
	// the src lock on repeated calls, starving the other readers, which is a
	// big problem if that greedy reader blocks on reading from src. Most likely
	// our use of locks could be improved to avoid this scenario, but that's
	// where we're at today.
	srcMu fifomu.Mutex

	// size is the count of bytes read from src.
	size int

	// cMu guards concurrent access to Stream's fields and methods.
	cMu sync.RWMutex

	// sealed is set to true when Seal is called. When sealed is true,
	// no more calls to NewReader are allowed.
	sealed bool

	// Consider our two mutexes cMu and srcMu above. There are effectively three
	// locks that can be acquired.
	//
	//  - cMu's read lock
	//  - cMu's write lock
	//  - srcMu's lock
	//
	// These three locks are referred to in the comments as the read, write, and
	// src locks.
}

// New returns a new Stream that wraps src. Use Stream.NewReader to read from src.
func New(src io.Reader) *Stream {
	c := &Stream{
		src:        src,
		cache:      make([]byte, 0),
		rdrsDoneCh: make(chan struct{}),
		srcDoneCh:  make(chan struct{}),
	}

	return c
}

// NewReader returns a new Reader from Stream. If ctx is non-nil, it is checked
// for cancellation at the start of Reader.Read (and possibly at other
// checkpoints).
//
// It is the caller's responsibility to close the returned Reader.
//
// NewReader panics if s is already sealed via Stream.Seal (but note that you
// can first test via Stream.Sealed).
//
// See: Reader.Read, Reader.Close.
func (s *Stream) NewReader(ctx context.Context) *Reader {
	s.cMu.Lock()         // write lock
	defer s.cMu.Unlock() // write unlock

	if s.sealed {
		panic("streamcache: Stream.NewReader invoked on sealed Stream")
	}

	r := &Reader{
		ctx:    ctx,
		s:      s,
		readFn: s.readMain,
	}
	s.rdrs = append(s.rdrs, r)
	return r
}

// Source returns the Stream's underlying source io.Reader.
//
// This can be useful if you need to force close the source
// for some reason, e.g.
//
//	stream.Source().(io.Closer).Close()
//
// The Stream's behavior is undefined if the caller reads from
// the source directly.
func (s *Stream) Source() io.Reader {
	return s.src
}

// readFunc is the type of the Reader.readFn field.
type readFunc func(r *Reader, p []byte, offset int) (n int, err error)

var (
	_ readFunc = (*Stream)(nil).readMain
	_ readFunc = (*Stream)(nil).readSrcDirect
)

// readSrcDirect reads directly from Stream.src. The src's size is incremented
// as bytes are read from src, and Stream.readErr is set if src returns an
// error.
func (s *Stream) readSrcDirect(_ *Reader, p []byte, _ int) (n int, err error) {
	n, err = s.src.Read(p)

	// Get the write lock before updating s's fields.
	s.cMu.Lock()         // write lock
	defer s.cMu.Unlock() // write unlock
	s.size += n
	s.readErr = err
	if err != nil {
		// We received an error from src, so it's done.
		close(s.srcDoneCh)
	}

	return n, err
}

// readMain reads from Stream.cache and/or Stream.src. If Stream is sealed
// and r is the final Reader, this method may switch r's Reader.readFn
// to Stream.readSrcDirect, such that the remaining reads occur
// directly against src, bypassing Stream.cache entirely.
func (s *Stream) readMain(r *Reader, p []byte, offset int) (n int, err error) {
TOP:
	s.cMu.RLock() // read lock

	if s.sealed && len(s.rdrs) == 1 {
		// The stream is sealed, and this is the final reader.
		// We can release the read lock (because this is the only possible
		// reader), and delegate to readFinal.
		s.cMu.RUnlock() // read unlock
		return s.readFinal(r, p, offset)
	}

	if s.isSatisfiedFromCache(p, offset) {
		// There's some data in the cache that can be returned.
		// Even if the amount of data is not enough to fill p,
		// we return what we can, and let the caller decide
		// whether to read more.
		n, err = s.fillFromCache(p, offset)
		s.cMu.RUnlock() // read unlock
		return n, err
	}

	// We don't have enough in the cache to satisfy the read.
	// We're going to need to read from src.

	// First we give up the read lock.
	s.cMu.RUnlock() // read unlock

	// And try to get the src lock.
	if !s.srcMu.TryLock() { // try src lock
		// We couldn't get the src lock. Another reader has the src lock,
		// and could be blocked on io. But, in the time since we released
		// the read lock above, it's possible that more data was added to
		// the cache. If that's the case we return that fresh cache data
		// so that r can catch up to the current cache state while some other
		// reader holds src lock.

		if !s.cMu.TryRLock() { // try read lock
			// We couldn't get the read lock, because another reader
			// is updating the cache after having read from src, and thus
			// has the write lock. There's only a tiny window where the
			// write lock is held, so our naive strategy here is to just
			// go back to the top.
			goto TOP
		}

		// We've got the read lock, let's see if there's any fresh bytes
		// in the cache that can be returned.
		if s.isSatisfiedFromCache(p, offset) {
			// Yup, there are bytes available in the cache. Return them.
			n, err = s.fillFromCache(p, offset)
			s.cMu.RUnlock() // read unlock
			return n, err
		}

		// There's nothing in the cache for r to consume.
		// So, we really need to get more data from src.

		// First we give up the read lock.
		s.cMu.RUnlock() // read unlock

		// And now we acquire the src lock so that we
		// can read from src.
		s.srcMu.Lock() // src lock
	}

	// If we've gotten this far, we have the src lock, but not the
	// read or write lock. We're here because there was nothing new in
	// the cache for r the last time we checked. However, it's possible
	// that another reader has since updated the cache, so we check again,
	// and also check if a read error has occurred.

	// We don't need to acquire the read lock, because we already have the
	// src lock, and only the src lock holder ever acquires the write lock,
	// so it's safe to proceed.
	if s.isSatisfiedFromCache(p, offset) {
		// There's some new stuff in the cache. Return it.
		n, err = s.fillFromCache(p, offset)
		s.srcMu.Unlock() // src unlock
		return n, err
	}

	// We're almost ready to read from src. Because src read is potentially
	// a blocking operation, we first check context cancellation. After all,
	// it's possible that r has been waiting around for a while trying to
	// acquire the src lock, and the context has been canceled in the
	// meantime.
	if r.ctx != nil {
		select {
		case <-r.ctx.Done():
			s.srcMu.Unlock() // src unlock
			return 0, context.Cause(r.ctx)
		default:
		}
	}

	// OK, this time, we're REALLY going to read from src.
	n, err = s.src.Read(p)
	if n == 0 && err == nil {
		// For this special case, there's no need to update the cache,
		// so we can just return now.
		s.srcMu.Unlock() // src unlock
		return 0, nil
	}

	// Now we need to update the cache, so we need to get the write lock.
	s.cMu.Lock() // write lock
	s.readErr = err
	if n > 0 {
		s.size += n
		s.cache = append(s.cache, p[:n]...)
	}

	if err != nil {
		// We received an error from src, so it's done.
		close(s.srcDoneCh)
	}

	// We're done updating the cache, so we can release the write and src
	// locks, and return.
	s.cMu.Unlock()   // write unlock
	s.srcMu.Unlock() // src unlock
	return n, err
}

// isSatisfiedFromCache returns true if the read can be satisfied from
// the cache due to the cache's size or because a read from source
// would encounter the non-nil s.readErr.
func (s *Stream) isSatisfiedFromCache(p []byte, offset int) bool {
	return s.size > offset || (s.readErr != nil && offset+len(p) >= s.size)
}

// fillFromCache copies bytes from Stream.cache to p, starting at offset,
// returning the number of bytes copied. If readErr is non-nil and we've
// reached the end of the cache, readErr is returned.
func (s *Stream) fillFromCache(p []byte, offset int) (n int, err error) {
	n = copy(p, s.cache[offset:])
	if s.readErr != nil && n+offset >= s.size {
		err = s.readErr
	}
	return n, err
}

// readFinal is invoked by Stream.readMain when the Stream is sealed
// and r is the final Reader. There are four possibilities for this read:
//
//  1. This read is entirely satisfied by the cache, with some
//     unread bytes still left in the cache. The next read
//     will still need to use the cache.
//  2. This read exactly matches the end of the cache, with no
//     unread bytes left in the cache. The subsequent read will be
//     directly against src and cache can be nilled.
//  3. The read offset aligns exactly with src's offset, thus this
//     read can be satisfied directly from src, as will all future
//     reads. We no longer need the cache.
//  4. The read is an overlap of the cache and src, so we need to
//     combine bytes from both. The subsequent read will be direct
//     from src and thus cache can be nilled.
func (s *Stream) readFinal(r *Reader, p []byte, offset int) (n int, err error) {
	if s.readErr != nil && offset+len(p) >= s.size {
		return s.fillFromCache(p, offset)
	}

	end := offset + len(p)
	switch {
	// This logic should be revisited. It might be possible that
	// some of these cases are unreachable?
	case end < s.size:
		// The read can be satisfied entirely from the cache.
		// Subsequent reads could also be satisfied by the
		// cache, so we can't nil out s.cache yet.
		return s.fillFromCache(p, offset)
	case end == s.size:
		n, err = s.fillFromCache(p, offset)
		// The read is satisfied completely by the cache with
		// no unread cache bytes. Thus, we can nil out s.cache,
		// because the next read will be directly from src, and
		// the cache will never be used again.
		s.cache = nil
		r.readFn = s.readSrcDirect
		return n, err
	case offset == s.size:
		// The read is entirely beyond what's cached, so we switch
		// to reading directly from src. We can nil out s.cache,
		// as it'll never be used again.
		s.cache = nil
		r.readFn = s.readSrcDirect

		// We don't need to get the src lock, because this is the final reader.
		n, err = s.src.Read(p)

		// Because we're updating s's fields, we need to get the write lock.
		s.cMu.Lock() // write lock
		s.size += n
		s.readErr = err
		if err != nil {
			// We received an error from src, so it's done.
			close(s.srcDoneCh)
		}
		s.cMu.Unlock() // write unlock
		return n, err
	case offset > s.size:
		// Should be impossible.
		panic("Offset is beyond end of cache")
	default:
		// This read is an overlap of cache and src.
	}

	// This read request is fully satisfied only by combining bytes from
	// the cache with new bytes from src. However, we're not going to do that.
	// We just return the cache bytes, and let the caller decide if they want
	// to read more.
	n, err = s.fillFromCache(p, offset)
	// Now that we've got what we need from the cache,
	// we can nil it out. It'll never be used again.
	s.cache = nil
	// Any subsequent reads will be direct from src.
	r.readFn = s.readSrcDirect
	return n, err
}

// Done returns a channel that is closed when the Stream is
// sealed and all remaining readers are closed.
//
//	s.Seal()
//	select {
//	case <-s.Done():
//	  fmt.Println("All readers are closed")
//	  if err := s.Err(); err != nil {
//	    fmt.Println("But an error occurred:", err)
//	  }
//	default:
//	  fmt.Println("The stream still is being read from")
//	}
//
// IMPORTANT: Don't wait on the Done channel without also calling Stream.Seal,
// as you may end up in deadlock. The returned channel will never be closed
// unless Stream.Seal is invoked.
//
// Note that Stream.Err returning a non-nil value does not of itself indicate
// that all readers are closed. There could be other readers still consuming
// earlier parts of the cache.
//
// Note also that it's possible that even after the returned channel is closed,
// Stream may not have closed its underlying source reader. For example, if
// a Stream is created and immediately sealed, the channel returned by Done is
// closed, although the underlying source reader was never closed. The source
// reader is closed only by closing the final Reader instance that was active
// after Seal is invoked.
//
// See also: Stream.Filled.
func (s *Stream) Done() <-chan struct{} {
	return s.rdrsDoneCh
}

// Filled returns a channel that is closed when the underlying source reader
// returns an error, including io.EOF. If the source reader returns an error, it
// is never read from again. If the source reader does not return an error, this
// channel is never closed.
//
// See also: Stream.Done.
func (s *Stream) Filled() <-chan struct{} {
	return s.srcDoneCh
}

// Size returns the current count of bytes read from the source reader.
// This value increases as readers read from the Stream.
//
// See also: Stream.Total.
func (s *Stream) Size() int {
	s.cMu.RLock()         // read lock
	defer s.cMu.RUnlock() // read unlock
	return s.size
}

// Total blocks until the source reader is fully read, and returns the total
// number of bytes read from the source, and any read error other than io.EOF
// returned by the source. If ctx is cancelled, zero and the context's cause
// error (per context.Cause) are returned. If source returned a non-EOF error,
// that error and the total number of bytes read are returned.
//
// Note that Total only returns if the channel returned by Stream.Filled
// is closed, but Total can return even if Stream.Done is not closed.
// That is to say, Total returning does not necessarily mean that all readers
// are closed.
//
// See also: Stream.Size, Stream.Err, Stream.Filled, Stream.Done.
func (s *Stream) Total(ctx context.Context) (size int, err error) {
	if ctx == nil {
		ctx = context.Background()
	}

	select {
	case <-ctx.Done():
		return 0, context.Cause(ctx)
	case <-s.srcDoneCh:
		// We don't need to lock here, because if srcDoneCh is
		// closed, it means that s.size and s.readErr are final.
		size = s.size
		if s.readErr != nil && !errors.Is(s.readErr, io.EOF) {
			err = s.readErr
		}

		return size, err
	}
}

// Err returns the first error (if any) that was returned by the underlying
// source reader, which may be io.EOF. After the source reader returns an
// error, it is never read from again, and the channel returned by Stream.Filled
// is closed.
func (s *Stream) Err() error {
	s.cMu.RLock()         // read lock
	defer s.cMu.RUnlock() // read unlock
	return s.readErr
}

// Seal is called to indicate that no more calls to NewReader are permitted.
// If there are no unclosed readers when Seal is invoked, the Stream.Done
// channel is closed, and the Stream is considered finished. Subsequent
// invocations are no-op.
func (s *Stream) Seal() {
	s.cMu.Lock()         // write lock
	defer s.cMu.Unlock() // write unlock

	if s.sealed {
		return
	}

	s.sealed = true
	if len(s.rdrs) == 0 {
		close(s.rdrsDoneCh)
	}
}

// Sealed returns true if Seal has been invoked.
func (s *Stream) Sealed() bool {
	s.cMu.RLock()         // read lock
	defer s.cMu.RUnlock() // read unlock
	return s.sealed
}

// close is invoked by Reader.Close to close itself. If the Stream
// is sealed and r is the final unclosed reader, this method closes
// the src reader, if it implements io.Closer.
func (s *Stream) close(r *Reader) error {
	s.cMu.Lock()         // write lock
	defer s.cMu.Unlock() // write unlock

	s.rdrs = removeElement(s.rdrs, r)

	if !s.sealed {
		return nil
	}

	if len(s.rdrs) == 0 {
		defer close(s.rdrsDoneCh)
		// r is last Reader, so we can close the source
		// reader, if it implements io.Closer.
		if rc, ok := s.src.(io.Closer); ok {
			return rc.Close()
		}
	}

	return nil
}

var _ io.ReadCloser = (*Reader)(nil)

// Reader is returned by Stream.NewReader. It implements io.ReadCloser; the
// caller must close the Reader when finished with it.
type Reader struct {
	// ctx is the context provided to Stream.NewReader. If non-nil,
	// every invocation of Reader.Read checks ctx for cancellation
	// before proceeding (and possibly later at other checkpoints).
	// Note that Reader.Close ignores ctx.
	ctx context.Context

	// readErr is set by Reader.Read when an error is returned
	// from the source, and its non-nil value is returned by
	// subsequent calls to Read. That is to say: the same non-nil
	// read error is returned every time.
	readErr error

	// s is the Reader's parent Stream.
	s *Stream

	// readFn is the func that Reader.Read invokes to read bytes.
	// Initially it is set to Stream.readMain, but if this reader
	// becomes the last man standing, this field may be set
	// to Stream.readSrcDirect.
	readFn readFunc

	// pCloseErr is set by Reader.Close, and the set value is
	// returned by any subsequent calls to Close. We use a pointer
	// to error so Reader.Read can check if the Reader is closed.
	pCloseErr *error

	// offset is the offset into the stream from which the next
	// call to Read will read. It is incremented by each Read.
	offset int

	// closeOnce guards Reader's Close method.
	closeOnce sync.Once
}

// Read reads from the stream. If a non-nil context was provided to Stream.NewReader
// to create this Reader, that context is checked at the start of each call
// to Read (and possibly at other checkpoints): if the context has been
// canceled, Read will return the context's error via context.Cause. Note
// however that Read can still block on reading from the Stream source. If this
// reader has already been closed via Reader.Close, Read will return ErrAlreadyClosed.
// If a previous invocation of Read returned an error from the source, that
// error is returned.
//
// Otherwise Read reads from Stream, which may return bytes from Stream's cache
// or new bytes from the source, or a combination of both. Note in particular
// that Read preferentially returns available bytes from the cache rather than
// waiting to read from the source, even if that means the returned n < len(p).
// This is in line with the io.Reader convention:
//
//	If some data is available but not len(p) bytes, Read conventionally
//	returns what is available instead of waiting for more.
//
// Use io.ReadFull or io.ReadAtLeast if you want to ensure that p is filled.
//
// Read is not safe for concurrent use.
func (r *Reader) Read(p []byte) (n int, err error) {
	if r.ctx != nil {
		select {
		case <-r.ctx.Done():
			return 0, context.Cause(r.ctx)
		default:
		}
	}

	if r.readErr != nil {
		return 0, r.readErr
	}

	if r.pCloseErr != nil {
		return 0, ErrAlreadyClosed
	}

	n, err = r.readFn(r, p, r.offset)
	r.readErr = err
	r.offset += n

	return n, err
}

// Close closes this Reader. If the parent Stream is not sealed, this method
// ultimately returns nil. If the parent Stream is sealed and this is the last
// remaining reader, the Stream's source reader is closed, if it implements
// io.Closer. At that point, the channel returned by Stream.Done is closed.
//
// If you don't want the source to be closed, wrap it via io.NopCloser before
// passing it to streamcache.New.
//
// The Close operation proceeds even if the non-nil context provided to
// Stream.NewReader is cancelled. That is to say, Reader.Close ignores context.
//
// Note that subsequent calls to Close are no-op and return the same result
// as the first call.
func (r *Reader) Close() error {
	r.closeOnce.Do(func() {
		closeErr := r.s.close(r)
		r.pCloseErr = &closeErr
	})

	if r.pCloseErr != nil {
		// Already closed. Return the same error as the first call
		// to Close (which may be nil).
		return *r.pCloseErr
	}

	return nil
}

// removeElement returns a (possibly new) slice that contains the
// elements of a without the first occurrence of v.
// Element order may not be preserved.
func removeElement[T any](a []*T, v *T) []*T {
	// https://stackoverflow.com/a/37335777/6004734
	for i := range a {
		if a[i] == v {
			return append(a[:i], a[i+1:]...)
		}
	}
	return a
}
```

## File: `streamcache_bench_test.go`
```go
package streamcache_test

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"math"
	"strconv"
	"sync"
	"sync/atomic"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/neilotoole/streamcache"
)

// BenchmarkDevelop is used during development as a standard benchmark
// for A/B testing.
//
//	$ go test -count=10 -bench BenchmarkDevelop > old.bench.txt
//	$ go test -count=10 -bench BenchmarkDevelop > new.bench.txt
//	$ benchstat old.bench.txt new.bench.txt
//
// The above is a useful way to compare the performance of different
// implementations.
func BenchmarkDevelop(b *testing.B) {
	const testBlobContents = false
	const numReaders = 1389

	initBlobs()
	wantBlob := blobs[size100KB]
	ctx := context.Background()

	b.ReportAllocs()
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		stream := streamcache.New(bytes.NewReader(wantBlob))
		rdrs := make([]*streamcache.Reader, numReaders)
		for j := range rdrs {
			rdrs[j] = stream.NewReader(ctx)
		}

		stream.Seal()

		wg := &sync.WaitGroup{}
		wg.Add(len(rdrs))
		for j := range rdrs {
			go func(j int) {
				defer wg.Done()
				defer rdrs[j].Close()
				p, err := io.ReadAll(rdrs[j])
				assert.NoError(b, err)
				assert.Equal(b, len(wantBlob), len(p))
				if testBlobContents {
					assert.Equal(b, wantBlob, p)
				}
			}(j)
		}
		wg.Wait()
		requireTake(b, stream.Done())
	}

	b.StopTimer()
}

func BenchmarkReaders_RunParallel(b *testing.B) {
	// I'm not sure if this benchmark setup is correct.
	// See also BenchmarkReaders_Goroutines.
	initBlobs()

	for _, blobSize := range blobSizes {
		wantBlob := blobs[blobSize]

		b.Run("blob-"+humanSize(blobSize), func(b *testing.B) {
			for _, sealed := range []bool{true, false} {
				sealed := sealed
				b.Run(cond(sealed, "sealed", "unsealed"), func(b *testing.B) {
					stream := streamcache.New(bytes.NewReader(wantBlob))
					rdrCount := &atomic.Int64{}
					b.ReportAllocs()
					b.ResetTimer()

					b.RunParallel(func(pb *testing.PB) {
						ctx := context.Background()
						for pb.Next() {
							rdr := stream.NewReader(ctx)
							if sealed && rdrCount.Add(1) == int64(b.N) {
								stream.Seal()
							}

							p, err := io.ReadAll(rdr)
							assert.NoError(b, err)
							assert.Equal(b, len(wantBlob), len(p))
							assert.NoError(b, rdr.Close())
						}
					})
				})
			}
		})
	}
}

func BenchmarkReaders_Goroutines(b *testing.B) {
	initBlobs()

	for _, blobSize := range blobSizes {
		wantBlob := blobs[blobSize]

		b.Run("blob-"+humanSize(blobSize), func(b *testing.B) {
			for _, numReaders := range rdrCounts {
				numReaders := numReaders

				b.Run("rdrs-"+strconv.Itoa(numReaders), func(b *testing.B) {
					for _, sealed := range []bool{true, false} {
						sealed := sealed
						b.Run(cond(sealed, "sealed", "unsealed"), func(b *testing.B) {
							b.ReportAllocs()
							b.ResetTimer()

							ctx := context.Background()

							for i := 0; i < b.N; i++ {
								stream := streamcache.New(bytes.NewReader(wantBlob))
								rdrs := make([]*streamcache.Reader, numReaders)
								for j := range rdrs {
									rdrs[j] = stream.NewReader(ctx)
								}

								if sealed {
									stream.Seal()
								}

								wg := &sync.WaitGroup{}
								wg.Add(len(rdrs))
								for j := range rdrs {
									go func(j int) {
										defer wg.Done()
										defer rdrs[j].Close()
										p, err := io.ReadAll(rdrs[j])
										assert.NoError(b, err)
										assert.Equal(b, len(wantBlob), len(p))
									}(j)
								}
								wg.Wait()
							}
						})
					}
				})
			}
		})
	}
}

// BenchmarkVsStdlib compares streamcache, using a single Reader,
// to stdlib's bytes.Reader.
func BenchmarkVsStdlib(b *testing.B) {
	initBlobs()

	for _, blobSize := range blobSizes {
		wantBlob := blobs[blobSize]

		b.Run("blob-"+humanSize(blobSize), func(b *testing.B) {
			b.Run("stdlib-bytes-reader", func(b *testing.B) {
				newRdrFn := func() io.ReadCloser {
					return io.NopCloser(bytes.NewReader(wantBlob))
				}

				b.ReportAllocs()
				b.ResetTimer()

				for i := 0; i < b.N; i++ {
					readAll(b, newRdrFn, len(wantBlob))
				}
			})

			b.Run("streamcache-sealed", func(b *testing.B) {
				newRdrFn := func() io.ReadCloser {
					stream := streamcache.New(io.NopCloser(bytes.NewReader(wantBlob)))
					r := stream.NewReader(context.Background())
					stream.Seal()
					return r
				}

				b.ReportAllocs()
				b.ResetTimer()

				for i := 0; i < b.N; i++ {
					readAll(b, newRdrFn, len(wantBlob))
				}
			})

			b.Run("streamcache-unsealed", func(b *testing.B) {
				newRdrFn := func() io.ReadCloser {
					stream := streamcache.New(io.NopCloser(bytes.NewReader(wantBlob)))
					r := stream.NewReader(context.Background())
					return r
				}
				b.ReportAllocs()
				b.ResetTimer()
				for i := 0; i < b.N; i++ {
					readAll(b, newRdrFn, len(wantBlob))
				}
			})
		})
	}
}

func readAll(b *testing.B, newRdrFn func() io.ReadCloser, wantSize int) {
	b.Helper()
	rc := newRdrFn()
	p, err := io.ReadAll(rc)
	require.NoError(b, err)
	require.Equal(b, wantSize, len(p))
	require.NoError(b, rc.Close())
}

// humanSize produces a human-friendly byte size, e.g. 1.2MB.
func humanSize(i int) string {
	sizes := []string{"B", "KB", "MB", "GB", "TB", "PB", "EB"}
	base := float64(1000)
	if i < 10 {
		return fmt.Sprintf("%dB", i)
	}
	e := math.Floor(math.Log(float64(i)) / math.Log(base))
	suffix := sizes[int(e)]
	val := math.Floor(float64(i)/math.Pow(base, e)*10+0.5) / 10
	f := "%.0f%s"
	if val < 10 {
		f = "%.1f%s"
	}

	return fmt.Sprintf(f, val, suffix)
}

// cond returns a if cond is true, else b.
func cond[T any](cond bool, a, b T) T {
	if cond {
		return a
	}
	return b
}

// gCounts is the number of readers to use in various tests.
var rdrCounts = []int{
	1,
	2,
	7,
	93,
	17001,
}

const (
	size0B    = 0
	size1B    = 1
	size9B    = 9
	size1K    = 1537
	size12KB  = 12289
	size100KB = 98304
	size786KB = 786432
	size6MB   = 6291456
	size50MB  = 50331649
	size500MB = 502653184
)

var blobSizes = []int{
	size0B,
	size1B,
	size9B,
	size1K,
	size12KB,
	size100KB,
	size786KB,
	size6MB,
	size50MB,
	size500MB,
}

// blobs is a map of blob sizes to the blob data. The blob data
// is random bytes of the given size, generated once via initBlobs.
var (
	blobs     = make(map[int][]byte, len(blobSizes))
	blobsOnce sync.Once
)

func initBlobs() {
	blobsOnce.Do(func() {
		var err error
		for _, size := range blobSizes {
			if blobs[size], err = io.ReadAll(newLimitRandReader(int64(size))); err != nil {
				panic(err)
			}
		}
	})
}
```

## File: `streamcache_test.go`
```go
package streamcache_test

import (
	"bytes"
	"context"
	"errors"
	"io"
	"os"
	"path/filepath"
	"strings"
	"sync"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/neilotoole/streamcache"
)

const (
	numSampleRows = 4321
	numG          = 2000

	anything = "anything"
)

func TestStream(t *testing.T) {
	t.Parallel()

	ctx := context.Background()

	s := streamcache.New(strings.NewReader(anything))
	requireNoTake(t, s.Done())
	requireNoTake(t, s.Filled())
	require.Equal(t, 0, s.Size())
	require.Nil(t, s.Err())
	requireNoTotal(t, s)

	r := s.NewReader(ctx)
	requireNoTake(t, s.Done())
	requireNoTake(t, s.Filled())
	requireNoTotal(t, s)

	// We'll read half the bytes.
	buf := make([]byte, 4)
	gotN, gotErr := r.Read(buf)
	require.NoError(t, gotErr)
	require.Equal(t, 4, gotN)
	require.Equal(t, "anyt", string(buf))
	require.Equal(t, 4, streamcache.ReaderOffset(r))
	require.Equal(t, 4, s.Size())
	require.Equal(t, 4, len(streamcache.CacheInternal(s)))
	requireNoTake(t, s.Done())
	requireNoTake(t, s.Filled())
	requireNoTotal(t, s)

	// Seal the source; after this, no more readers can be created.
	s.Seal()
	require.True(t, s.Sealed())
	requireNoTake(t, s.Done())
	requireNoTake(t, s.Filled())
	requireNoTotal(t, s)

	require.Panics(t, func() {
		_ = s.NewReader(ctx)
	}, "should panic because cache is already sealed")

	// Read the remaining bytes.
	gotN, gotErr = r.Read(buf)
	require.NoError(t, gotErr)
	require.Nil(t, s.Err())
	requireNoTake(t, s.Done())
	requireNoTake(t, s.Filled())
	requireNoTotal(t, s)
	require.Equal(t, 4, gotN)
	require.Equal(t, "hing", string(buf))
	require.Equal(t, 8, streamcache.ReaderOffset(r))
	require.Equal(t, 8, s.Size())

	// Read again, but this time we should get io.EOF.
	gotN, gotErr = r.Read(buf)
	require.Error(t, gotErr)
	require.Equal(t, 0, gotN)
	require.Equal(t, io.EOF, gotErr)
	require.Equal(t, io.EOF, s.Err())
	requireTotal(t, s, 8)
	requireTake(t, s.Filled())
	requireNoTake(t, s.Done())
	require.Equal(t, 8, streamcache.ReaderOffset(r))
	require.Equal(t, 8, s.Size())

	// Read one more time, and we should get io.EOF again.
	gotN, gotErr = r.Read(buf)
	require.Error(t, gotErr)
	require.Equal(t, 0, gotN)
	require.Equal(t, io.EOF, gotErr)
	require.Equal(t, io.EOF, s.Err())
	require.Equal(t, 8, streamcache.ReaderOffset(r))
	require.Equal(t, 8, s.Size())
	requireTotal(t, s, 8)
	requireNoTake(t, s.Done())
	requireTake(t, s.Filled())

	// Close the reader, which should close the underlying source.
	gotErr = r.Close()
	require.NoError(t, gotErr)
	requireTotal(t, s, 8)
	requireTake(t, s.Done())
	requireTake(t, s.Filled())

	// Closing again should be no-op.
	gotErr = r.Close()
	require.Nil(t, gotErr)
	requireTotal(t, s, 8)
	requireTake(t, s.Done())
	requireTake(t, s.Filled())
}

func TestReaderAlreadyClosed(t *testing.T) {
	s := streamcache.New(strings.NewReader(anything))
	r := s.NewReader(context.Background())
	buf := make([]byte, 4)
	_, err := r.Read(buf)
	require.NoError(t, err)

	// After closing, we should get ErrAlreadyClosed if we try to read again.
	require.NoError(t, r.Close())
	_, err = r.Read(buf)
	require.Error(t, err)
	require.Equal(t, streamcache.ErrAlreadyClosed, err)
	requireNoTotal(t, s)
	requireNoTake(t, s.Done())
	requireNoTake(t, s.Filled())
	requireNoTotal(t, s)
}

func TestSingleReaderImmediateSeal(t *testing.T) {
	t.Parallel()

	s := streamcache.New(strings.NewReader(anything))
	r := s.NewReader(context.Background())
	s.Seal()

	requireNoTotal(t, s)
	gotData, err := io.ReadAll(r)
	require.NoError(t, err)
	requireTotal(t, s, len(anything))
	require.Equal(t, anything, string(gotData))
	requireNoTake(t, s.Done())
	require.NoError(t, r.Close())
	requireTake(t, s.Done())
}

func TestReader_NoSeal(t *testing.T) {
	t.Parallel()

	s := streamcache.New(strings.NewReader(anything))
	r := s.NewReader(context.Background())
	gotData, err := io.ReadAll(r)
	require.NoError(t, err)
	require.Equal(t, anything, string(gotData))
	require.NoError(t, r.Close())
	requireNoTake(t, s.Done(), "not done because not sealed")
	requireTake(t, s.Filled())
	require.Equal(t, io.EOF, s.Err())
	requireTotal(t, s, len(anything))
}

func TestStream_File(t *testing.T) {
	ctx := context.Background()
	wantSize, fp := generateSampleFile(t, numSampleRows)
	wantData, err := os.ReadFile(fp)
	require.NoError(t, err)

	f, err := os.Open(fp)
	require.NoError(t, err)
	recorder := &rcRecorder{r: f}
	s := streamcache.New(recorder)

	r := s.NewReader(ctx)
	require.NoError(t, err)

	s.Seal()

	gotData, err := io.ReadAll(r)
	require.NoError(t, err)
	requireTotal(t, s, wantSize)
	requireTake(t, s.Filled())
	requireNoTake(t, s.Done())
	require.Equal(t, wantSize, s.Size())
	require.True(t, errors.Is(s.Err(), io.EOF))

	require.Equal(t, string(wantData), string(gotData))

	assert.NoError(t, r.Close())
	assert.Equal(t, 1, recorder.closeCount)
	require.Equal(t, wantSize, s.Size())
	requireTake(t, s.Filled())
	requireTake(t, s.Done())
	requireTotal(t, s, wantSize)
}

func TestStream_File_Concurrent_SealLate(t *testing.T) {
	t.Parallel()

	ctx := context.Background()
	wantSize, fp := generateSampleFile(t, numSampleRows)
	wantData, err := os.ReadFile(fp)
	require.NoError(t, err)
	f, err := os.Open(fp)
	require.NoError(t, err)

	s := streamcache.New(f)
	for i := 0; i < numG; i++ {
		r := s.NewReader(ctx)
		require.NoError(t, err)

		go func(r *streamcache.Reader) {
			defer func() { assert.NoError(t, r.Close()) }()

			sleepJitter()

			gotData, err := io.ReadAll(r)
			assert.NoError(t, err)
			assert.Equal(t, string(wantData), string(gotData))
			requireTake(t, s.Filled())
			requireTotal(t, s, wantSize)
		}(r)
	}

	requireNoTake(t, s.Done())

	s.Seal()

	<-s.Done()

	require.Equal(t, wantSize, s.Size())
	requireTotal(t, s, wantSize)
}

func TestStream_File_Concurrent_SealMiddle(t *testing.T) {
	t.Parallel()

	ctx := context.Background()
	wantSize, fp := generateSampleFile(t, numSampleRows)
	wantData, err := os.ReadFile(fp)
	require.NoError(t, err)

	f, err := os.Open(fp)
	require.NoError(t, err)

	recorder := &rcRecorder{r: f}
	s := streamcache.New(recorder)
	require.NoError(t, err)

	t.Logf("Iterations: %d", numG)

	rdrs := make([]*streamcache.Reader, numG)
	for i := 0; i < numG; i++ {
		rdrs[i] = s.NewReader(ctx)
	}

	// This time, we'll seal in the middle of the reads.
	sealOnce := &sync.Once{}

	for i := range rdrs {
		go func(i int, r *streamcache.Reader) {
			defer func() {
				assert.NoError(t, r.Close())
			}()

			sleepJitter()

			if i > numG/2 {
				sealOnce.Do(func() {
					t.Logf("Sealing once on iter %d", i)
					s.Seal()
					t.Logf("SEALED once on iter %d", i)
				})
			}

			gotData, gotErr := io.ReadAll(r)
			require.NoError(t, gotErr)
			requireTotal(t, s, wantSize)
			requireTake(t, s.Filled())

			assert.Equal(t, string(wantData), string(gotData))
		}(i, rdrs[i])
	}

	t.Logf("Waiting on <-s.Done()")
	<-s.Done()

	assert.NoError(t, err)
	require.Equal(t, wantSize, s.Size())
	requireTotal(t, s, wantSize)
	requireTake(t, s.Filled())
}

func TestSeal_AlreadySealed(t *testing.T) {
	t.Parallel()

	ctx := context.Background()
	s := streamcache.New(strings.NewReader(anything))
	_ = s.NewReader(ctx)

	s.Seal()

	require.Panics(t, func() {
		_ = s.NewReader(ctx)
	}, "should panic because stream is already sealed")

	requireNoTotal(t, s)
	requireNoTake(t, s.Done())
	requireNoTake(t, s.Filled())
}

func TestSeal_AfterRead(t *testing.T) {
	t.Parallel()

	want := strings.Repeat(anything, 100)
	ctx := context.Background()
	s := streamcache.New(strings.NewReader(want))
	r1 := s.NewReader(ctx)
	require.NotNil(t, r1)
	gotData1, err := io.ReadAll(r1)
	require.NoError(t, err)
	require.Equal(t, want, string(gotData1))
	requireTotal(t, s, len(want))
	requireTake(t, s.Filled())
	requireNoTake(t, s.Done())

	r2 := s.NewReader(ctx)
	require.NoError(t, err)

	s.Seal()

	requireTotal(t, s, len(want))
	requireTake(t, s.Filled())
	requireNoTake(t, s.Done())

	gotData2, err := io.ReadAll(r2)
	require.NoError(t, err)
	require.Equal(t, want, string(gotData2))

	require.NotPanics(t, func() {
		s.Seal()
	}, "subsequent calls to s.Seal shouldn't panic")
}

func TestSeal_NoReaders(t *testing.T) {
	t.Parallel()

	s := streamcache.New(strings.NewReader(anything))
	s.Seal()
	requireTake(t, s.Done())
	requireNoTake(t, s.Filled())
	requireNoTotal(t, s)
}

func TestContextAwareness(t *testing.T) {
	t.Parallel()

	wantErr := errors.New("oh noes")
	srcRdr := newDelayReader(newLimitRandReader(100000), time.Second, true)
	s := streamcache.New(srcRdr)

	ctx := context.Background()
	ctx, cancel := context.WithCancelCause(ctx)
	time.AfterFunc(time.Second, func() {
		cancel(wantErr)
	})

	r := s.NewReader(ctx)
	_, gotErr := io.ReadAll(r)
	require.Error(t, gotErr)
	require.True(t, errors.Is(gotErr, wantErr))
}

func TestErrorHandling(t *testing.T) {
	t.Parallel()

	ctx := context.Background()
	wantErr := errors.New("oh noes")
	const errAfterN = 50

	s := streamcache.New(newErrorAfterNReader(errAfterN, wantErr))

	r1 := s.NewReader(ctx)
	gotData1, err := io.ReadAll(r1)
	require.Error(t, err)
	require.True(t, errors.Is(err, wantErr))
	require.Equal(t, errAfterN, len(gotData1))

	r2 := s.NewReader(ctx)
	gotData2, err := io.ReadAll(r2)
	require.Error(t, err)
	require.True(t, errors.Is(err, wantErr))
	require.Equal(t, errAfterN, len(gotData2))
}

func TestSizeTotal(t *testing.T) {
	t.Parallel()

	ctx := context.Background()
	wantData := make([]byte, 0)
	s := streamcache.New(bytes.NewReader(wantData))
	require.Equal(t, 0, s.Size())
	requireNoTotal(t, s)

	r := s.NewReader(ctx)
	gotData, err := io.ReadAll(r)
	require.NoError(t, err)
	require.Equal(t, wantData, gotData)
	require.Equal(t, 0, s.Size())
	requireTotal(t, s, 0)
}

func TestClose(t *testing.T) {
	t.Parallel()

	ctx := context.Background()

	wantData := []byte(anything)
	recorder := &rcRecorder{r: strings.NewReader(anything)}
	s := streamcache.New(recorder)

	requireNoTake(t, s.Done())
	r1 := s.NewReader(ctx)

	gotData1, err := io.ReadAll(r1)
	require.NoError(t, err)
	require.Equal(t, wantData, gotData1)
	requireTake(t, s.Filled())
	requireNoTake(t, s.Done())
	require.NoError(t, r1.Close())
	requireNoTake(t, s.Done())
	require.Equal(t, 0, recorder.closeCount)

	r2 := s.NewReader(ctx)
	s.Seal()

	requireNoTake(t, s.Done())
	gotData2, err := io.ReadAll(r2)
	require.NoError(t, err)
	require.Equal(t, wantData, gotData2)
	requireNoTake(t, s.Done())
	require.NoError(t, r2.Close())
	requireTake(t, s.Done())
	require.Equal(t, 1, recorder.closeCount)
}

// TestReader_Read_PartialCacheHit tests the scenario where
// a Reader.Read request is only partially satisfied by Stream's
// cache. Reader.Read will return the bytes available to
// it in the cache, thus the returned n may be < len(p).
func TestReader_Read_PartialCacheHit(t *testing.T) {
	ctx := context.Background()
	s := streamcache.New(strings.NewReader(anything))

	r1 := s.NewReader(ctx)
	buf1 := make([]byte, 3)
	n1, err := r1.Read(buf1)
	require.NoError(t, err)
	require.Equal(t, 3, n1)
	require.Equal(t, 3, s.Size())

	r2 := s.NewReader(ctx)
	buf2 := make([]byte, 5)
	n2, err := r2.Read(buf2)
	require.NoError(t, err)
	require.Equal(t, 3, n2)
	require.Equal(t, 3, s.Size())

	buf2 = make([]byte, 10)
	n2, err = r2.Read(buf2)
	require.NoError(t, err)
	require.Equal(t, 5, n2)
	require.Equal(t, len(anything), s.Size())

	r3 := s.NewReader(ctx)
	buf3 := make([]byte, 10)
	n3, err := io.ReadFull(r3, buf3)
	require.Equal(t, len(anything), n3)
	require.True(t, errors.Is(err, io.ErrUnexpectedEOF))
}

func TestEmptyStream_EOF(t *testing.T) {
	t.Parallel()

	ctx := context.Background()
	s := streamcache.New(strings.NewReader(""))

	r := s.NewReader(ctx)
	gotData, err := io.ReadAll(r)
	require.NoError(t, err)
	require.Equal(t, "", string(gotData))
	requireNoTake(t, s.Done())
	requireTake(t, s.Filled())
	require.Equal(t, 0, s.Size())
	requireTotal(t, s, 0)
	require.Equal(t, io.EOF, s.Err())
}

func TestEmptyStream_NoEOF(t *testing.T) {
	t.Parallel()

	ctx := context.Background()
	src := &tweakableReader{}
	s := streamcache.New(src)

	r := s.NewReader(ctx)
	buf := make([]byte, 10)
	gotN, gotErr := r.Read(buf)
	require.NoError(t, gotErr)
	require.Equal(t, 0, gotN)
	requireNoTake(t, s.Done())
	requireNoTake(t, s.Filled())
	require.Equal(t, 0, s.Size())
	requireNoTotal(t, s)

	src.err = io.EOF
	gotN, gotErr = r.Read(buf)
	require.Equal(t, 0, gotN)
	require.True(t, errors.Is(gotErr, io.EOF))
	requireTake(t, s.Filled())
	requireNoTake(t, s.Done())
	require.Equal(t, 0, s.Size())
	requireTotal(t, s, 0)
}

// TestContextCancelBeforeSrcRead tests the scenario where
// Reader r2 is blocked due to r1 having the src lock,
// and then r2's context is canceled before the lock is released.
// On lock release, r2 proceeds and acquires the src lock, but
// instead of reading from src, r2 should return the cancellation
// cause before even attempting to read from the source.
func TestContextCancelBeforeSrcRead(t *testing.T) {
	t.Parallel()
	sleep := time.Millisecond * 100

	src := &tweakableReader{unblock: make(chan struct{}, 1), data: []byte(anything)}
	s := streamcache.New(src)

	r1 := s.NewReader(context.Background())
	// buf1 is zero length, because we don't actually
	// want to fill up the cache when r1 reads.
	buf1 := make([]byte, 0)

	wg := &sync.WaitGroup{}
	wg.Add(2)
	go func() {
		defer wg.Done()
		// r1 will block until it receives from src.unblock.
		n, err := r1.Read(buf1)
		require.NoError(t, err)
		require.Equal(t, 0, n)
	}()

	time.Sleep(sleep)

	wantErr := errors.New("doh")
	ctx, cancelFn := context.WithCancelCause(context.Background())
	r2 := s.NewReader(ctx)
	buf2 := make([]byte, 10)
	go func() {
		defer wg.Done()
		// r2 will block on acquiring the src lock, until r1
		// releases it. But before r1 releases it, r2's context
		// will be cancelled, and thus wantErr should be returned.
		n, err := r2.Read(buf2)
		assert.Equal(t, 0, n)
		assert.Error(t, err)
		assert.True(t, errors.Is(err, wantErr))
	}()

	time.Sleep(sleep)
	// r1 is blocked on src.unblock, and r2 is blocked on src lock.
	// Cancel r2's context.
	cancelFn(wantErr)
	time.Sleep(sleep)
	// Now, unblock r1, and r2 should then acquire the src lock,
	// but then r2 should consult its context, and return the
	// cancellation cause.
	src.unblock <- struct{}{}
	wg.Wait()
}

func TestStreamSource(t *testing.T) {
	t.Parallel()

	// Write some data to a test file.
	fp := filepath.Join(t.TempDir(), "streamcache_test.txt")
	require.NoError(t, os.WriteFile(fp, []byte(anything), 0o600))

	f, fErr := os.Open(fp)
	require.NoError(t, fErr)

	// Create a stream (and reader) that reads from the file.
	stream := streamcache.New(f)
	r := stream.NewReader(context.Background())

	// Read a small chunk from the file.
	buf := make([]byte, 2)
	n, readErr := r.Read(buf)
	require.NoError(t, readErr)
	require.Equal(t, 2, n)

	gotSrc := stream.Source()
	require.Equal(t, f, gotSrc)

	// Close the source (i.e. the file), and then try
	// to read from the reader.
	require.NoError(t, gotSrc.(io.ReadCloser).Close())

	n, readErr = r.Read(buf)
	require.Error(t, readErr)
	require.Equal(t, 0, n)
	readPathErr := new(os.PathError)
	require.True(t, errors.As(readErr, &readPathErr))
	require.Equal(t, "read", readPathErr.Op)
	require.Equal(t, "file already closed", readPathErr.Err.Error())
	require.Equal(t, 2, stream.Size())
	require.Equal(t, readErr, stream.Err())
	total, totalErr := stream.Total(context.Background())
	require.Error(t, totalErr)
	require.Equal(t, 2, total)
	require.True(t, errors.Is(totalErr, readErr))
	requireTake(t, stream.Filled())

	// Now check what happens when we close the reader.
	requireNoTake(t, stream.Done(),
		"stream is not done until sealed and reader is closed")
	stream.Seal()
	closeErr := r.Close()
	require.Error(t, closeErr)
	closePathErr := new(os.PathError)
	require.True(t, errors.As(closeErr, &closePathErr))
	require.Equal(t, "close", closePathErr.Op)
	require.Equal(t, "file already closed", closePathErr.Err.Error())
	requireTake(t, stream.Done())
}
```

## File: `examples/in-out-err/README.md`
```markdown
# in-out-err

`in-out-err` is a trivial example program that copies the contents of stdin
to stdout and stderr, and prints the number of bytes read. It exists to
demonstrate the use of [`neilotoole/streamcache`](https://github.com/neilotoole/streamcache).

## Usage

```shell
$ go install github.com/neilotoole/streamcache/examples/in-out-err

$ echo "hello world" | in-out-err
hello world
hello world
Read 12 bytes from stdin
```

Note that the `in-out-err` code ignores most errors; don't do that in real life.
See the [`multicase`](../multicase) example for a more complete program.
```

## File: `examples/in-out-err/main.go`
```go
// Package main contains the "in-out-err" example program, which reads
// from stdin and writes to both stdout and stderr. It exists to
// demonstrate the use of neilotoole/streamcache.
//
// Usage:
//
//	$ go install github.com/neilotoole/streamcache/examples/in-out-err
//	$ echo "hello world" | in-out-err
//	hello world
//	hello world
//	Read 12 bytes from stdin
//
// Note that the code ignores most errors; don't do that in real life.
package main

import (
	"context"
	"errors"
	"fmt"
	"io"
	"os"

	"github.com/neilotoole/streamcache"
)

// Write stdin to both stdout and stderr.
// Some error handling omitted for brevity.
//
//nolint:errcheck,revive
func main() {
	ctx := context.Background()
	stream := streamcache.New(os.Stdin)

	r1 := stream.NewReader(ctx)
	go func() {
		defer r1.Close()
		io.Copy(os.Stdout, r1)
	}()

	r2 := stream.NewReader(ctx)
	go func() {
		defer r2.Close()
		io.Copy(os.Stderr, r2)
	}()

	stream.Seal()   // Indicate that there'll be no more readers...
	<-stream.Done() // Receives when all readers are closed.

	if err := stream.Err(); err != nil && !errors.Is(err, io.EOF) {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}

	fmt.Fprintf(os.Stdout, "Read %d bytes from stdin\n", stream.Size())
}
```

## File: `examples/multicase/README.md`
```markdown
# multicase

`multicase` is a trivial program that reads input from `stdin` and echoes
it to `stdout` in lower, upper, and title case. It demonstrates
use of the [`neilotoole/streamcache`](https://github.com/neilotoole/streamcache)
Go package.

## Usage

```shell
$ go install github.com/neilotoole/streamcache/examples/multicase
$ echo "hello world" | multicase
```

![streamcache_multicase.png](streamcache_multicase.png)
```

## File: `examples/multicase/main.go`
```go
// Package main provides the "multicase" example CLI that reads from
// stdin and outputs each line in lower, upper, and title case. Usage:
//
//	$ cat FILE | multicase
//	# Or interactive mode (user enters input)
//	$ multicase
//
// "multicase" exists to demonstrate use of neilotoole/streamcache.
package main

import (
	"bufio"
	"context"
	"errors"
	"fmt"
	"io"
	"os"
	"os/signal"
	"strings"

	"github.com/neilotoole/streamcache"
)

// main sets up the CLI, and invokes exec to do the actual work.
func main() {
	ctx, cancelFn := context.WithCancel(context.Background())
	var err error
	defer func() {
		cancelFn()
		if err != nil {
			os.Exit(1)
		}
	}()

	go func() {
		stopCh := make(chan os.Signal, 1)
		signal.Notify(stopCh, os.Interrupt)

		<-stopCh
		cancelFn()
	}()

	var fi os.FileInfo
	if fi, err = os.Stdin.Stat(); err != nil {
		printErr(err)
		return
	}

	if os.ModeNamedPipe&fi.Mode() == 0 && fi.Size() == 0 {
		// No data on stdin, thus interactive mode: print a prompt.
		fmt.Fprintln(os.Stdout, colorize(ansiFaint, "multicase: enter text and press [ENTER]"))
	}

	if err = exec(ctx, os.Stdin, os.Stdout); err != nil {
		printErr(err)
	}
}

func exec(ctx context.Context, in io.Reader, out io.Writer) error {
	toUpper := func(s string) string {
		return colorize(ansiRed, strings.ToUpper(s))
	}
	toLower := func(s string) string {
		return colorize(ansiGreen, strings.ToLower(s))
	}
	toTitle := func(s string) string {
		return colorize(ansiBlue, strings.Title(s)) //nolint:staticcheck
	}
	transforms := []func(string) string{toUpper, toLower, toTitle}

	stream := streamcache.New(in)
	rdrs := make([]*streamcache.Reader, len(transforms))
	for i := range rdrs {
		rdrs[i] = stream.NewReader(ctx)
	}

	// Seal the stream to indicate no more readers.
	stream.Seal()

	errCh := make(chan error, 1)
	for i := range transforms {
		go func(i int) {
			r, t := rdrs[i], transforms[i]
			defer r.Close()

			sc := bufio.NewScanner(r)
			for sc.Scan() {
				select {
				case <-ctx.Done():
					errCh <- ctx.Err()
					return
				default:
				}

				text := sc.Text()
				fmt.Fprintln(out, t(text))
			}

			if err := sc.Err(); err != nil {
				errCh <- err
			}
		}(i)
	}

	var err error
	select {
	case <-ctx.Done():
		err = ctx.Err()
	case err = <-errCh:
	case <-stream.Done():
		err = stream.Err()
	}

	if errors.Is(err, io.EOF) {
		err = nil
	}
	return err
}

func colorize(ansi, s string) string {
	return ansi + s + ansiReset
}

const (
	ansiFaint = "\033[2m"
	ansiReset = "\033[0m"
	ansiRed   = "\033[31m"
	ansiGreen = "\033[32m"
	ansiBlue  = "\033[34m"
)

func printErr(err error) {
	fmt.Fprintln(os.Stderr, colorize(ansiRed, "multicase: error: "+err.Error()))
}
```

## File: `examples/multicase/testdata/input.txt`
```
In Xanadu did Kubla Khan
A stately pleasure-dome decree:
Where Alph, the sacred river, ran
Through caverns measureless to man
   Down to a sunless sea.
```

## File: `examples/typedetect/README.md`
```markdown
# typedetect

`typedetect` is a trivial program that reads input from `stdin` or a specified
file, attempts to determine its file type (`json` and `xml` are
supported), and prints the file type, and a preview (head and tail) of the
file contents. It demonstrates use of the [`neilotoole/streamcache`](https://github.com/neilotoole/streamcache)
Go package.

## Usage

```shell
$ go install github.com/neilotoole/streamcache/examples/typedetect

$ typedetect testdata/data.json
# Or:
$ cat testdata/data.xml | typedetect
```

![streamcache_typedetect.png](streamcache_typedetect.png)
```

## File: `examples/typedetect/main.go`
```go
// Package main provides the "typedetect" example CLI that detects the type
// of a data file, e.g. JSON, XML, etc. Usage:
//
//	$ typedetect FILE
//	$ cat FILE | typedetect
//
// The tool prints the detected type, and a preview of the
// file contents.
//
// "typedetect" exists to demonstrate use of neilotoole/streamcache.
package main

import (
	"bufio"
	"context"
	"encoding/json"
	"encoding/xml"
	"errors"
	"fmt"
	"io"
	"os"
	"os/signal"
	"strings"
	"sync"

	"github.com/neilotoole/streamcache"
)

// main sets up the CLI, and invokes exec to do the actual work.
func main() {
	ctx, cancelFn := context.WithCancel(context.Background())
	var err error
	defer func() {
		cancelFn()
		if err != nil {
			os.Exit(1)
		}
	}()

	go func() {
		stopCh := make(chan os.Signal, 1)
		signal.Notify(stopCh, os.Interrupt)

		<-stopCh
		cancelFn()
	}()

	// Determine if input is coming from stdin (`cat FILE | typedetect`),
	// or via args (`typedetect FILE`).

	var fi os.FileInfo
	if fi, err = os.Stdin.Stat(); err != nil {
		printErr(err)
		return
	}

	var in *os.File
	if os.ModeNamedPipe&fi.Mode() > 0 || fi.Size() > 0 {
		// Input is from stdin.
		if len(os.Args) > 1 {
			// If input is from stdin, then we don't want any args.
			// - `cat FILE | typedetect` is ok, but...
			// - `cat FILE | typedetect FILE` is not.
			err = errUsage
			printErr(err)
			return
		}
		in = os.Stdin
	} else {
		// Input is from args, e.g. `typedetect FILE`.
		if len(os.Args) != 2 || (os.Args[1] == "") {
			err = errUsage
			printErr(err)
			return
		}
		in, err = os.Open(os.Args[1])
		if err != nil {
			printErr(err)
			return
		}
		defer in.Close()
	}

	// The CLI is set up, now we can get on with the work.
	if err = exec(ctx, in, os.Stdout); err != nil {
		printErr(err)
	}
}

// exec does the actual work of typedetect.
func exec(ctx context.Context, in io.Reader, out io.Writer) error {
	detectors := []detectFunc{detectJSON, detectXML}

	stream := streamcache.New(in)
	rdrs := make([]*streamcache.Reader, len(detectors))
	for i := range detectors {
		rdrs[i] = stream.NewReader(ctx)
	}

	detectionCh := make(chan string, len(detectors))
	wg := &sync.WaitGroup{}
	wg.Add(len(detectors))
	for i := range detectors {
		go func(i int) {
			defer wg.Done()
			r, detector := rdrs[i], detectors[i]
			defer r.Close()

			if typ := detector(ctx, r); typ != "" {
				detectionCh <- typ
			}
		}(i)
	}

	wg.Wait()

	// In theory multiple detectors could succeed, so we
	// gather all the results and print them.
	close(detectionCh)
	var types []string
	for typ := range detectionCh {
		types = append(types, typ)
	}

	if len(types) == 0 {
		fmt.Fprintln(out, colorize(ansiRed, "typedetect: unable to detect type"))
		// Even if we can't detect the type, we still continue below
		// to print the head and tail preview.
	} else {
		fmt.Fprint(out, colorize(ansiGreen, "typedetect: "+strings.Join(types, ", "))+"\n")
	}

	// previewRdr reads the content, from which we print the head
	// and tail, each up to numPreviewLines lines.
	previewRdr := stream.NewReader(ctx)
	defer previewRdr.Close()

	// There will be no new readers after this point, so we can
	// seal the stream. This results in previewRdr switching to
	// reading directly from the source reader, as soon as it has
	// exhausted the stream's cache. This mode switch is internal
	// to streamcache; the caller knows nothing of it.
	stream.Seal()

	// Scan and print up to numPreviewLines from input head.
	var lineCount int
	sc := bufio.NewScanner(previewRdr)
	for i := 0; i < numPreviewLines && sc.Scan(); i++ {
		select {
		// Offer a chance to bail out early on Ctrl-C.
		case <-ctx.Done():
			return ctx.Err()
		default:
		}
		printPreviewLine(out, sc.Text())
		lineCount++
	}

	if err := sc.Err(); err != nil {
		return err
	}

	// Use a channel as a sliding window / circular buffer of input lines
	// so that, at the end, we can print the final numPreviewLines of
	// the tail, and just skip the stuff in the middle.
	window := make(chan string, numPreviewLines)
	var line string
	for sc.Scan() {
		line = sc.Text()
		select {
		case <-ctx.Done():
			return ctx.Err()
		case window <- line:
			// The window is not yet full, so just add the line.
		default:
			// The window is full, so pop the oldest line.
			<-window
			// And now add the new line.
			window <- line
		}
		lineCount++
	}

	if err := sc.Err(); err != nil {
		return err
	}

	// We're done with processing the input now. We can
	// close the window.
	close(window)

	skipCount := lineCount - len(window) - numPreviewLines
	if skipCount > 0 {
		skipMsg := fmt.Sprintf("[Skipped %d lines]", skipCount)
		fmt.Fprintln(out, colorize(ansiGreen, skipMsg))
	}

	for line = range window {
		printPreviewLine(out, line)
	}

	summary := fmt.Sprintf("%d lines (%d bytes)", lineCount, stream.Size())
	fmt.Fprintln(out, colorize(ansiGreen, summary))
	return nil
}

// detectFunc is a function that detects the type of data on rc.
// On success, the function returns a non-empty string, e.g. "json"
// or "xml". On failure, the function returns empty string. The
// function must close rc in either case.
type detectFunc func(ctx context.Context, rc io.ReadCloser) (typ string)

// detectJSON returns "json" if rc appears to contain JSON, otherwise
// it returns empty string. It closes rc in either case.
func detectJSON(ctx context.Context, rc io.ReadCloser) (typ string) {
	defer rc.Close()

	dec := json.NewDecoder(rc)
	var err error
	for i := 0; i < tokenDetectThreshold; i++ {
		select {
		case <-ctx.Done():
			return ""
		default:
		}
		if _, err = dec.Token(); err != nil {
			return ""
		}
	}

	return "json"
}

// detectXML returns "xml" if rc appears to contain XML, otherwise
// it returns empty string. It closes rc in either case.
func detectXML(ctx context.Context, rc io.ReadCloser) (typ string) {
	defer rc.Close()

	dec := xml.NewDecoder(rc)
	var err error
	for i := 0; i < tokenDetectThreshold; i++ {
		select {
		case <-ctx.Done():
			return ""
		default:
		}
		if _, err = dec.Token(); err != nil {
			return ""
		}
	}

	return "xml"
}

const (
	// tokenDetectThreshold is the number of tokens to be read
	// successfully before we consider the type to be detected.
	tokenDetectThreshold = 10

	// numPreviewLines is the number of preview lines to print from the
	// head and tail of the input. So, the total number of lines printed
	// is numPreviewLines*2.
	numPreviewLines = 5

	// maxPreviewLineWidth is the width at which a preview line
	// is truncate before printing.
	maxPreviewLineWidth = 80

	// terminal colors.
	ansiReset = "\033[0m"
	ansiFaint = "\033[2m"
	ansiRed   = "\033[31m"
	ansiGreen = "\033[32m"
)

// printPreviewLine prints a line of the input to out. Long lines are
// truncated at maxPreviewLineWidth and have an ellipsis added.
func printPreviewLine(out io.Writer, line string) {
	const ellipsis = ansiGreen + "…" + ansiReset

	if len(line) <= maxPreviewLineWidth {
		fmt.Fprintln(out, colorize(ansiFaint, line))
		return
	}

	fmt.Fprintln(out, colorize(ansiFaint, line[:maxPreviewLineWidth-3])+ellipsis)
}

func colorize(ansi, s string) string {
	return ansi + s + ansiReset
}

func printErr(err error) {
	fmt.Fprintln(os.Stderr, colorize(ansiRed, "typedetect: error: "+err.Error()))
}

var errUsage = errors.New("usage: `typedetect FILE` or `cat FILE | typedetect`")
```

## File: `examples/typedetect/testdata/data.json`
```json
[
  {
    "actor_id": 1,
    "first_name": "PENELOPE",
    "last_name": "GUINESS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 2,
    "first_name": "NICK",
    "last_name": "WAHLBERG",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 3,
    "first_name": "ED",
    "last_name": "CHASE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 4,
    "first_name": "JENNIFER",
    "last_name": "DAVIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 5,
    "first_name": "JOHNNY",
    "last_name": "LOLLOBRIGIDA",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 6,
    "first_name": "BETTE",
    "last_name": "NICHOLSON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 7,
    "first_name": "GRACE",
    "last_name": "MOSTEL",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 8,
    "first_name": "MATTHEW",
    "last_name": "JOHANSSON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 9,
    "first_name": "JOE",
    "last_name": "SWANK",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 10,
    "first_name": "CHRISTIAN",
    "last_name": "GABLE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 11,
    "first_name": "ZERO",
    "last_name": "CAGE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 12,
    "first_name": "KARL",
    "last_name": "BERRY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 13,
    "first_name": "UMA",
    "last_name": "WOOD",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 14,
    "first_name": "VIVIEN",
    "last_name": "BERGEN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 15,
    "first_name": "CUBA",
    "last_name": "OLIVIER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 16,
    "first_name": "FRED",
    "last_name": "COSTNER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 17,
    "first_name": "HELEN",
    "last_name": "VOIGHT",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 18,
    "first_name": "DAN",
    "last_name": "TORN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 19,
    "first_name": "BOB",
    "last_name": "FAWCETT",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 20,
    "first_name": "LUCILLE",
    "last_name": "TRACY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 21,
    "first_name": "KIRSTEN",
    "last_name": "PALTROW",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 22,
    "first_name": "ELVIS",
    "last_name": "MARX",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 23,
    "first_name": "SANDRA",
    "last_name": "KILMER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 24,
    "first_name": "CAMERON",
    "last_name": "STREEP",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 25,
    "first_name": "KEVIN",
    "last_name": "BLOOM",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 26,
    "first_name": "RIP",
    "last_name": "CRAWFORD",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 27,
    "first_name": "JULIA",
    "last_name": "MCQUEEN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 28,
    "first_name": "WOODY",
    "last_name": "HOFFMAN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 29,
    "first_name": "ALEC",
    "last_name": "WAYNE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 30,
    "first_name": "SANDRA",
    "last_name": "PECK",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 31,
    "first_name": "SISSY",
    "last_name": "SOBIESKI",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 32,
    "first_name": "TIM",
    "last_name": "HACKMAN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 33,
    "first_name": "MILLA",
    "last_name": "PECK",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 34,
    "first_name": "AUDREY",
    "last_name": "OLIVIER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 35,
    "first_name": "JUDY",
    "last_name": "DEAN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 36,
    "first_name": "BURT",
    "last_name": "DUKAKIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 37,
    "first_name": "VAL",
    "last_name": "BOLGER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 38,
    "first_name": "TOM",
    "last_name": "MCKELLEN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 39,
    "first_name": "GOLDIE",
    "last_name": "BRODY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 40,
    "first_name": "JOHNNY",
    "last_name": "CAGE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 41,
    "first_name": "JODIE",
    "last_name": "DEGENERES",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 42,
    "first_name": "TOM",
    "last_name": "MIRANDA",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 43,
    "first_name": "KIRK",
    "last_name": "JOVOVICH",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 44,
    "first_name": "NICK",
    "last_name": "STALLONE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 45,
    "first_name": "REESE",
    "last_name": "KILMER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 46,
    "first_name": "PARKER",
    "last_name": "GOLDBERG",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 47,
    "first_name": "JULIA",
    "last_name": "BARRYMORE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 48,
    "first_name": "FRANCES",
    "last_name": "DAY-LEWIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 49,
    "first_name": "ANNE",
    "last_name": "CRONYN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 50,
    "first_name": "NATALIE",
    "last_name": "HOPKINS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 51,
    "first_name": "GARY",
    "last_name": "PHOENIX",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 52,
    "first_name": "CARMEN",
    "last_name": "HUNT",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 53,
    "first_name": "MENA",
    "last_name": "TEMPLE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 54,
    "first_name": "PENELOPE",
    "last_name": "PINKETT",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 55,
    "first_name": "FAY",
    "last_name": "KILMER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 56,
    "first_name": "DAN",
    "last_name": "HARRIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 57,
    "first_name": "JUDE",
    "last_name": "CRUISE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 58,
    "first_name": "CHRISTIAN",
    "last_name": "AKROYD",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 59,
    "first_name": "DUSTIN",
    "last_name": "TAUTOU",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 60,
    "first_name": "HENRY",
    "last_name": "BERRY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 61,
    "first_name": "CHRISTIAN",
    "last_name": "NEESON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 62,
    "first_name": "JAYNE",
    "last_name": "NEESON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 63,
    "first_name": "CAMERON",
    "last_name": "WRAY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 64,
    "first_name": "RAY",
    "last_name": "JOHANSSON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 65,
    "first_name": "ANGELA",
    "last_name": "HUDSON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 66,
    "first_name": "MARY",
    "last_name": "TANDY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 67,
    "first_name": "JESSICA",
    "last_name": "BAILEY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 68,
    "first_name": "RIP",
    "last_name": "WINSLET",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 69,
    "first_name": "KENNETH",
    "last_name": "PALTROW",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 70,
    "first_name": "MICHELLE",
    "last_name": "MCCONAUGHEY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 71,
    "first_name": "ADAM",
    "last_name": "GRANT",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 72,
    "first_name": "SEAN",
    "last_name": "WILLIAMS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 73,
    "first_name": "GARY",
    "last_name": "PENN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 74,
    "first_name": "MILLA",
    "last_name": "KEITEL",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 75,
    "first_name": "BURT",
    "last_name": "POSEY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 76,
    "first_name": "ANGELINA",
    "last_name": "ASTAIRE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 77,
    "first_name": "CARY",
    "last_name": "MCCONAUGHEY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 78,
    "first_name": "GROUCHO",
    "last_name": "SINATRA",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 79,
    "first_name": "MAE",
    "last_name": "HOFFMAN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 80,
    "first_name": "RALPH",
    "last_name": "CRUZ",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 81,
    "first_name": "SCARLETT",
    "last_name": "DAMON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 82,
    "first_name": "WOODY",
    "last_name": "JOLIE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 83,
    "first_name": "BEN",
    "last_name": "WILLIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 84,
    "first_name": "JAMES",
    "last_name": "PITT",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 85,
    "first_name": "MINNIE",
    "last_name": "ZELLWEGER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 86,
    "first_name": "GREG",
    "last_name": "CHAPLIN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 87,
    "first_name": "SPENCER",
    "last_name": "PECK",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 88,
    "first_name": "KENNETH",
    "last_name": "PESCI",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 89,
    "first_name": "CHARLIZE",
    "last_name": "DENCH",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 90,
    "first_name": "SEAN",
    "last_name": "GUINESS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 91,
    "first_name": "CHRISTOPHER",
    "last_name": "BERRY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 92,
    "first_name": "KIRSTEN",
    "last_name": "AKROYD",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 93,
    "first_name": "ELLEN",
    "last_name": "PRESLEY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 94,
    "first_name": "KENNETH",
    "last_name": "TORN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 95,
    "first_name": "DARYL",
    "last_name": "WAHLBERG",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 96,
    "first_name": "GENE",
    "last_name": "WILLIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 97,
    "first_name": "MEG",
    "last_name": "HAWKE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 98,
    "first_name": "CHRIS",
    "last_name": "BRIDGES",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 99,
    "first_name": "JIM",
    "last_name": "MOSTEL",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 100,
    "first_name": "SPENCER",
    "last_name": "DEPP",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 101,
    "first_name": "SUSAN",
    "last_name": "DAVIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 102,
    "first_name": "WALTER",
    "last_name": "TORN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 103,
    "first_name": "MATTHEW",
    "last_name": "LEIGH",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 104,
    "first_name": "PENELOPE",
    "last_name": "CRONYN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 105,
    "first_name": "SIDNEY",
    "last_name": "CROWE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 106,
    "first_name": "GROUCHO",
    "last_name": "DUNST",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 107,
    "first_name": "GINA",
    "last_name": "DEGENERES",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 108,
    "first_name": "WARREN",
    "last_name": "NOLTE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 109,
    "first_name": "SYLVESTER",
    "last_name": "DERN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 110,
    "first_name": "SUSAN",
    "last_name": "DAVIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 111,
    "first_name": "CAMERON",
    "last_name": "ZELLWEGER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 112,
    "first_name": "RUSSELL",
    "last_name": "BACALL",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 113,
    "first_name": "MORGAN",
    "last_name": "HOPKINS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 114,
    "first_name": "MORGAN",
    "last_name": "MCDORMAND",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 115,
    "first_name": "HARRISON",
    "last_name": "BALE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 116,
    "first_name": "DAN",
    "last_name": "STREEP",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 117,
    "first_name": "RENEE",
    "last_name": "TRACY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 118,
    "first_name": "CUBA",
    "last_name": "ALLEN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 119,
    "first_name": "WARREN",
    "last_name": "JACKMAN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 120,
    "first_name": "PENELOPE",
    "last_name": "MONROE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 121,
    "first_name": "LIZA",
    "last_name": "BERGMAN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 122,
    "first_name": "SALMA",
    "last_name": "NOLTE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 123,
    "first_name": "JULIANNE",
    "last_name": "DENCH",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 124,
    "first_name": "SCARLETT",
    "last_name": "BENING",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 125,
    "first_name": "ALBERT",
    "last_name": "NOLTE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 126,
    "first_name": "FRANCES",
    "last_name": "TOMEI",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 127,
    "first_name": "KEVIN",
    "last_name": "GARLAND",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 128,
    "first_name": "CATE",
    "last_name": "MCQUEEN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 129,
    "first_name": "DARYL",
    "last_name": "CRAWFORD",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 130,
    "first_name": "GRETA",
    "last_name": "KEITEL",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 131,
    "first_name": "JANE",
    "last_name": "JACKMAN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 132,
    "first_name": "ADAM",
    "last_name": "HOPPER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 133,
    "first_name": "RICHARD",
    "last_name": "PENN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 134,
    "first_name": "GENE",
    "last_name": "HOPKINS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 135,
    "first_name": "RITA",
    "last_name": "REYNOLDS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 136,
    "first_name": "ED",
    "last_name": "MANSFIELD",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 137,
    "first_name": "MORGAN",
    "last_name": "WILLIAMS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 138,
    "first_name": "LUCILLE",
    "last_name": "DEE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 139,
    "first_name": "EWAN",
    "last_name": "GOODING",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 140,
    "first_name": "WHOOPI",
    "last_name": "HURT",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 141,
    "first_name": "CATE",
    "last_name": "HARRIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 142,
    "first_name": "JADA",
    "last_name": "RYDER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 143,
    "first_name": "RIVER",
    "last_name": "DEAN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 144,
    "first_name": "ANGELA",
    "last_name": "WITHERSPOON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 145,
    "first_name": "KIM",
    "last_name": "ALLEN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 146,
    "first_name": "ALBERT",
    "last_name": "JOHANSSON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 147,
    "first_name": "FAY",
    "last_name": "WINSLET",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 148,
    "first_name": "EMILY",
    "last_name": "DEE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 149,
    "first_name": "RUSSELL",
    "last_name": "TEMPLE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 150,
    "first_name": "JAYNE",
    "last_name": "NOLTE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 151,
    "first_name": "GEOFFREY",
    "last_name": "HESTON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 152,
    "first_name": "BEN",
    "last_name": "HARRIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 153,
    "first_name": "MINNIE",
    "last_name": "KILMER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 154,
    "first_name": "MERYL",
    "last_name": "GIBSON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 155,
    "first_name": "IAN",
    "last_name": "TANDY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 156,
    "first_name": "FAY",
    "last_name": "WOOD",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 157,
    "first_name": "GRETA",
    "last_name": "MALDEN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 158,
    "first_name": "VIVIEN",
    "last_name": "BASINGER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 159,
    "first_name": "LAURA",
    "last_name": "BRODY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 160,
    "first_name": "CHRIS",
    "last_name": "DEPP",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 161,
    "first_name": "HARVEY",
    "last_name": "HOPE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 162,
    "first_name": "OPRAH",
    "last_name": "KILMER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 163,
    "first_name": "CHRISTOPHER",
    "last_name": "WEST",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 164,
    "first_name": "HUMPHREY",
    "last_name": "WILLIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 165,
    "first_name": "AL",
    "last_name": "GARLAND",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 166,
    "first_name": "NICK",
    "last_name": "DEGENERES",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 167,
    "first_name": "LAURENCE",
    "last_name": "BULLOCK",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 168,
    "first_name": "WILL",
    "last_name": "WILSON",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 169,
    "first_name": "KENNETH",
    "last_name": "HOFFMAN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 170,
    "first_name": "MENA",
    "last_name": "HOPPER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 171,
    "first_name": "OLYMPIA",
    "last_name": "PFEIFFER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 172,
    "first_name": "GROUCHO",
    "last_name": "WILLIAMS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 173,
    "first_name": "ALAN",
    "last_name": "DREYFUSS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 174,
    "first_name": "MICHAEL",
    "last_name": "BENING",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 175,
    "first_name": "WILLIAM",
    "last_name": "HACKMAN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 176,
    "first_name": "JON",
    "last_name": "CHASE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 177,
    "first_name": "GENE",
    "last_name": "MCKELLEN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 178,
    "first_name": "LISA",
    "last_name": "MONROE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 179,
    "first_name": "ED",
    "last_name": "GUINESS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 180,
    "first_name": "JEFF",
    "last_name": "SILVERSTONE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 181,
    "first_name": "MATTHEW",
    "last_name": "CARREY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 182,
    "first_name": "DEBBIE",
    "last_name": "AKROYD",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 183,
    "first_name": "RUSSELL",
    "last_name": "CLOSE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 184,
    "first_name": "HUMPHREY",
    "last_name": "GARLAND",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 185,
    "first_name": "MICHAEL",
    "last_name": "BOLGER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 186,
    "first_name": "JULIA",
    "last_name": "ZELLWEGER",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 187,
    "first_name": "RENEE",
    "last_name": "BALL",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 188,
    "first_name": "ROCK",
    "last_name": "DUKAKIS",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 189,
    "first_name": "CUBA",
    "last_name": "BIRCH",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 190,
    "first_name": "AUDREY",
    "last_name": "BAILEY",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 191,
    "first_name": "GREGORY",
    "last_name": "GOODING",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 192,
    "first_name": "JOHN",
    "last_name": "SUVARI",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 193,
    "first_name": "BURT",
    "last_name": "TEMPLE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 194,
    "first_name": "MERYL",
    "last_name": "ALLEN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 195,
    "first_name": "JAYNE",
    "last_name": "SILVERSTONE",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 196,
    "first_name": "BELA",
    "last_name": "WALKEN",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 197,
    "first_name": "REESE",
    "last_name": "WEST",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 198,
    "first_name": "MARY",
    "last_name": "KEITEL",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 199,
    "first_name": "JULIA",
    "last_name": "FAWCETT",
    "last_update": "2020-06-11T02:50:54Z"
  },
  {
    "actor_id": 200,
    "first_name": "THORA",
    "last_name": "TEMPLE",
    "last_update": "2020-06-11T02:50:54Z"
  }
]
```

## File: `examples/typedetect/testdata/data.jsonl`
```
{"actor_id": 1, "first_name": "PENELOPE", "last_name": "GUINESS", "last_update": "2020-06-11T02:50:54Z"}
{"actor_id": 2, "first_name": "NICK", "last_name": "WAHLBERG", "last_update": "2020-06-11T02:50:54Z"}
{"actor_id": 3, "first_name": "ED", "last_name": "CHASE", "last_update": "2020-06-11T02:50:54Z"}
{"actor_id": 4, "first_name": "JENNIFER", "last_name": "DAVIS", "last_update": "2020-06-11T02:50:54Z"}
{"actor_id": 5, "first_name": "JOHNNY", "last_name": "LOLLOBRIGIDA", "last_update": "2020-06-11T02:50:54Z"}
{"actor_id": 6, "first_name": "BETTE", "last_name": "NICHOLSON", "last_update": "2020-06-11T02:50:54Z"}
{"actor_id": 7, "first_name": "GRACE", "last_name": "MOSTEL", "last_update": "2020-06-11T02:50:54Z"}
{"actor_id": 8, "first_name": "MATTHEW", "last_name": "JOHANSSON", "last_update": "2020-06-11T02:50:54Z"}
{"actor_id": 9, "first_name": "JOE", "last_name": "SWANK", "last_update": "2020-06-11T02:50:54Z"}
{"actor_id": 10, "first_name": "CHRISTIAN", "last_name": "GABLE", "last_update": "2020-06-11T02:50:54Z"}
{"actor_id": 11, "first_name": "ZERO", "last_name": "CAGE", "last_update": "2020-06-11T02:50:54Z"}
```

## File: `examples/typedetect/testdata/data.xml`
```xml
<?xml version="1.0"?>
<records>
  <record>
    <actor_id>1</actor_id>
    <first_name>PENELOPE</first_name>
    <last_name>GUINESS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>2</actor_id>
    <first_name>NICK</first_name>
    <last_name>WAHLBERG</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>3</actor_id>
    <first_name>ED</first_name>
    <last_name>CHASE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>4</actor_id>
    <first_name>JENNIFER</first_name>
    <last_name>DAVIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>5</actor_id>
    <first_name>JOHNNY</first_name>
    <last_name>LOLLOBRIGIDA</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>6</actor_id>
    <first_name>BETTE</first_name>
    <last_name>NICHOLSON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>7</actor_id>
    <first_name>GRACE</first_name>
    <last_name>MOSTEL</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>8</actor_id>
    <first_name>MATTHEW</first_name>
    <last_name>JOHANSSON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>9</actor_id>
    <first_name>JOE</first_name>
    <last_name>SWANK</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>10</actor_id>
    <first_name>CHRISTIAN</first_name>
    <last_name>GABLE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>11</actor_id>
    <first_name>ZERO</first_name>
    <last_name>CAGE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>12</actor_id>
    <first_name>KARL</first_name>
    <last_name>BERRY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>13</actor_id>
    <first_name>UMA</first_name>
    <last_name>WOOD</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>14</actor_id>
    <first_name>VIVIEN</first_name>
    <last_name>BERGEN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>15</actor_id>
    <first_name>CUBA</first_name>
    <last_name>OLIVIER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>16</actor_id>
    <first_name>FRED</first_name>
    <last_name>COSTNER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>17</actor_id>
    <first_name>HELEN</first_name>
    <last_name>VOIGHT</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>18</actor_id>
    <first_name>DAN</first_name>
    <last_name>TORN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>19</actor_id>
    <first_name>BOB</first_name>
    <last_name>FAWCETT</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>20</actor_id>
    <first_name>LUCILLE</first_name>
    <last_name>TRACY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>21</actor_id>
    <first_name>KIRSTEN</first_name>
    <last_name>PALTROW</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>22</actor_id>
    <first_name>ELVIS</first_name>
    <last_name>MARX</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>23</actor_id>
    <first_name>SANDRA</first_name>
    <last_name>KILMER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>24</actor_id>
    <first_name>CAMERON</first_name>
    <last_name>STREEP</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>25</actor_id>
    <first_name>KEVIN</first_name>
    <last_name>BLOOM</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>26</actor_id>
    <first_name>RIP</first_name>
    <last_name>CRAWFORD</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>27</actor_id>
    <first_name>JULIA</first_name>
    <last_name>MCQUEEN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>28</actor_id>
    <first_name>WOODY</first_name>
    <last_name>HOFFMAN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>29</actor_id>
    <first_name>ALEC</first_name>
    <last_name>WAYNE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>30</actor_id>
    <first_name>SANDRA</first_name>
    <last_name>PECK</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>31</actor_id>
    <first_name>SISSY</first_name>
    <last_name>SOBIESKI</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>32</actor_id>
    <first_name>TIM</first_name>
    <last_name>HACKMAN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>33</actor_id>
    <first_name>MILLA</first_name>
    <last_name>PECK</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>34</actor_id>
    <first_name>AUDREY</first_name>
    <last_name>OLIVIER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>35</actor_id>
    <first_name>JUDY</first_name>
    <last_name>DEAN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>36</actor_id>
    <first_name>BURT</first_name>
    <last_name>DUKAKIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>37</actor_id>
    <first_name>VAL</first_name>
    <last_name>BOLGER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>38</actor_id>
    <first_name>TOM</first_name>
    <last_name>MCKELLEN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>39</actor_id>
    <first_name>GOLDIE</first_name>
    <last_name>BRODY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>40</actor_id>
    <first_name>JOHNNY</first_name>
    <last_name>CAGE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>41</actor_id>
    <first_name>JODIE</first_name>
    <last_name>DEGENERES</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>42</actor_id>
    <first_name>TOM</first_name>
    <last_name>MIRANDA</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>43</actor_id>
    <first_name>KIRK</first_name>
    <last_name>JOVOVICH</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>44</actor_id>
    <first_name>NICK</first_name>
    <last_name>STALLONE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>45</actor_id>
    <first_name>REESE</first_name>
    <last_name>KILMER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>46</actor_id>
    <first_name>PARKER</first_name>
    <last_name>GOLDBERG</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>47</actor_id>
    <first_name>JULIA</first_name>
    <last_name>BARRYMORE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>48</actor_id>
    <first_name>FRANCES</first_name>
    <last_name>DAY-LEWIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>49</actor_id>
    <first_name>ANNE</first_name>
    <last_name>CRONYN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>50</actor_id>
    <first_name>NATALIE</first_name>
    <last_name>HOPKINS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>51</actor_id>
    <first_name>GARY</first_name>
    <last_name>PHOENIX</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>52</actor_id>
    <first_name>CARMEN</first_name>
    <last_name>HUNT</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>53</actor_id>
    <first_name>MENA</first_name>
    <last_name>TEMPLE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>54</actor_id>
    <first_name>PENELOPE</first_name>
    <last_name>PINKETT</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>55</actor_id>
    <first_name>FAY</first_name>
    <last_name>KILMER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>56</actor_id>
    <first_name>DAN</first_name>
    <last_name>HARRIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>57</actor_id>
    <first_name>JUDE</first_name>
    <last_name>CRUISE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>58</actor_id>
    <first_name>CHRISTIAN</first_name>
    <last_name>AKROYD</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>59</actor_id>
    <first_name>DUSTIN</first_name>
    <last_name>TAUTOU</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>60</actor_id>
    <first_name>HENRY</first_name>
    <last_name>BERRY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>61</actor_id>
    <first_name>CHRISTIAN</first_name>
    <last_name>NEESON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>62</actor_id>
    <first_name>JAYNE</first_name>
    <last_name>NEESON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>63</actor_id>
    <first_name>CAMERON</first_name>
    <last_name>WRAY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>64</actor_id>
    <first_name>RAY</first_name>
    <last_name>JOHANSSON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>65</actor_id>
    <first_name>ANGELA</first_name>
    <last_name>HUDSON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>66</actor_id>
    <first_name>MARY</first_name>
    <last_name>TANDY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>67</actor_id>
    <first_name>JESSICA</first_name>
    <last_name>BAILEY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>68</actor_id>
    <first_name>RIP</first_name>
    <last_name>WINSLET</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>69</actor_id>
    <first_name>KENNETH</first_name>
    <last_name>PALTROW</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>70</actor_id>
    <first_name>MICHELLE</first_name>
    <last_name>MCCONAUGHEY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>71</actor_id>
    <first_name>ADAM</first_name>
    <last_name>GRANT</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>72</actor_id>
    <first_name>SEAN</first_name>
    <last_name>WILLIAMS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>73</actor_id>
    <first_name>GARY</first_name>
    <last_name>PENN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>74</actor_id>
    <first_name>MILLA</first_name>
    <last_name>KEITEL</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>75</actor_id>
    <first_name>BURT</first_name>
    <last_name>POSEY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>76</actor_id>
    <first_name>ANGELINA</first_name>
    <last_name>ASTAIRE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>77</actor_id>
    <first_name>CARY</first_name>
    <last_name>MCCONAUGHEY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>78</actor_id>
    <first_name>GROUCHO</first_name>
    <last_name>SINATRA</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>79</actor_id>
    <first_name>MAE</first_name>
    <last_name>HOFFMAN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>80</actor_id>
    <first_name>RALPH</first_name>
    <last_name>CRUZ</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>81</actor_id>
    <first_name>SCARLETT</first_name>
    <last_name>DAMON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>82</actor_id>
    <first_name>WOODY</first_name>
    <last_name>JOLIE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>83</actor_id>
    <first_name>BEN</first_name>
    <last_name>WILLIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>84</actor_id>
    <first_name>JAMES</first_name>
    <last_name>PITT</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>85</actor_id>
    <first_name>MINNIE</first_name>
    <last_name>ZELLWEGER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>86</actor_id>
    <first_name>GREG</first_name>
    <last_name>CHAPLIN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>87</actor_id>
    <first_name>SPENCER</first_name>
    <last_name>PECK</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>88</actor_id>
    <first_name>KENNETH</first_name>
    <last_name>PESCI</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>89</actor_id>
    <first_name>CHARLIZE</first_name>
    <last_name>DENCH</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>90</actor_id>
    <first_name>SEAN</first_name>
    <last_name>GUINESS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>91</actor_id>
    <first_name>CHRISTOPHER</first_name>
    <last_name>BERRY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>92</actor_id>
    <first_name>KIRSTEN</first_name>
    <last_name>AKROYD</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>93</actor_id>
    <first_name>ELLEN</first_name>
    <last_name>PRESLEY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>94</actor_id>
    <first_name>KENNETH</first_name>
    <last_name>TORN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>95</actor_id>
    <first_name>DARYL</first_name>
    <last_name>WAHLBERG</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>96</actor_id>
    <first_name>GENE</first_name>
    <last_name>WILLIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>97</actor_id>
    <first_name>MEG</first_name>
    <last_name>HAWKE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>98</actor_id>
    <first_name>CHRIS</first_name>
    <last_name>BRIDGES</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>99</actor_id>
    <first_name>JIM</first_name>
    <last_name>MOSTEL</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>100</actor_id>
    <first_name>SPENCER</first_name>
    <last_name>DEPP</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>101</actor_id>
    <first_name>SUSAN</first_name>
    <last_name>DAVIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>102</actor_id>
    <first_name>WALTER</first_name>
    <last_name>TORN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>103</actor_id>
    <first_name>MATTHEW</first_name>
    <last_name>LEIGH</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>104</actor_id>
    <first_name>PENELOPE</first_name>
    <last_name>CRONYN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>105</actor_id>
    <first_name>SIDNEY</first_name>
    <last_name>CROWE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>106</actor_id>
    <first_name>GROUCHO</first_name>
    <last_name>DUNST</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>107</actor_id>
    <first_name>GINA</first_name>
    <last_name>DEGENERES</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>108</actor_id>
    <first_name>WARREN</first_name>
    <last_name>NOLTE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>109</actor_id>
    <first_name>SYLVESTER</first_name>
    <last_name>DERN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>110</actor_id>
    <first_name>SUSAN</first_name>
    <last_name>DAVIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>111</actor_id>
    <first_name>CAMERON</first_name>
    <last_name>ZELLWEGER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>112</actor_id>
    <first_name>RUSSELL</first_name>
    <last_name>BACALL</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>113</actor_id>
    <first_name>MORGAN</first_name>
    <last_name>HOPKINS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>114</actor_id>
    <first_name>MORGAN</first_name>
    <last_name>MCDORMAND</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>115</actor_id>
    <first_name>HARRISON</first_name>
    <last_name>BALE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>116</actor_id>
    <first_name>DAN</first_name>
    <last_name>STREEP</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>117</actor_id>
    <first_name>RENEE</first_name>
    <last_name>TRACY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>118</actor_id>
    <first_name>CUBA</first_name>
    <last_name>ALLEN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>119</actor_id>
    <first_name>WARREN</first_name>
    <last_name>JACKMAN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>120</actor_id>
    <first_name>PENELOPE</first_name>
    <last_name>MONROE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>121</actor_id>
    <first_name>LIZA</first_name>
    <last_name>BERGMAN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>122</actor_id>
    <first_name>SALMA</first_name>
    <last_name>NOLTE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>123</actor_id>
    <first_name>JULIANNE</first_name>
    <last_name>DENCH</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>124</actor_id>
    <first_name>SCARLETT</first_name>
    <last_name>BENING</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>125</actor_id>
    <first_name>ALBERT</first_name>
    <last_name>NOLTE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>126</actor_id>
    <first_name>FRANCES</first_name>
    <last_name>TOMEI</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>127</actor_id>
    <first_name>KEVIN</first_name>
    <last_name>GARLAND</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>128</actor_id>
    <first_name>CATE</first_name>
    <last_name>MCQUEEN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>129</actor_id>
    <first_name>DARYL</first_name>
    <last_name>CRAWFORD</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>130</actor_id>
    <first_name>GRETA</first_name>
    <last_name>KEITEL</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>131</actor_id>
    <first_name>JANE</first_name>
    <last_name>JACKMAN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>132</actor_id>
    <first_name>ADAM</first_name>
    <last_name>HOPPER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>133</actor_id>
    <first_name>RICHARD</first_name>
    <last_name>PENN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>134</actor_id>
    <first_name>GENE</first_name>
    <last_name>HOPKINS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>135</actor_id>
    <first_name>RITA</first_name>
    <last_name>REYNOLDS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>136</actor_id>
    <first_name>ED</first_name>
    <last_name>MANSFIELD</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>137</actor_id>
    <first_name>MORGAN</first_name>
    <last_name>WILLIAMS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>138</actor_id>
    <first_name>LUCILLE</first_name>
    <last_name>DEE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>139</actor_id>
    <first_name>EWAN</first_name>
    <last_name>GOODING</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>140</actor_id>
    <first_name>WHOOPI</first_name>
    <last_name>HURT</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>141</actor_id>
    <first_name>CATE</first_name>
    <last_name>HARRIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>142</actor_id>
    <first_name>JADA</first_name>
    <last_name>RYDER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>143</actor_id>
    <first_name>RIVER</first_name>
    <last_name>DEAN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>144</actor_id>
    <first_name>ANGELA</first_name>
    <last_name>WITHERSPOON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>145</actor_id>
    <first_name>KIM</first_name>
    <last_name>ALLEN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>146</actor_id>
    <first_name>ALBERT</first_name>
    <last_name>JOHANSSON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>147</actor_id>
    <first_name>FAY</first_name>
    <last_name>WINSLET</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>148</actor_id>
    <first_name>EMILY</first_name>
    <last_name>DEE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>149</actor_id>
    <first_name>RUSSELL</first_name>
    <last_name>TEMPLE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>150</actor_id>
    <first_name>JAYNE</first_name>
    <last_name>NOLTE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>151</actor_id>
    <first_name>GEOFFREY</first_name>
    <last_name>HESTON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>152</actor_id>
    <first_name>BEN</first_name>
    <last_name>HARRIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>153</actor_id>
    <first_name>MINNIE</first_name>
    <last_name>KILMER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>154</actor_id>
    <first_name>MERYL</first_name>
    <last_name>GIBSON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>155</actor_id>
    <first_name>IAN</first_name>
    <last_name>TANDY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>156</actor_id>
    <first_name>FAY</first_name>
    <last_name>WOOD</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>157</actor_id>
    <first_name>GRETA</first_name>
    <last_name>MALDEN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>158</actor_id>
    <first_name>VIVIEN</first_name>
    <last_name>BASINGER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>159</actor_id>
    <first_name>LAURA</first_name>
    <last_name>BRODY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>160</actor_id>
    <first_name>CHRIS</first_name>
    <last_name>DEPP</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>161</actor_id>
    <first_name>HARVEY</first_name>
    <last_name>HOPE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>162</actor_id>
    <first_name>OPRAH</first_name>
    <last_name>KILMER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>163</actor_id>
    <first_name>CHRISTOPHER</first_name>
    <last_name>WEST</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>164</actor_id>
    <first_name>HUMPHREY</first_name>
    <last_name>WILLIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>165</actor_id>
    <first_name>AL</first_name>
    <last_name>GARLAND</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>166</actor_id>
    <first_name>NICK</first_name>
    <last_name>DEGENERES</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>167</actor_id>
    <first_name>LAURENCE</first_name>
    <last_name>BULLOCK</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>168</actor_id>
    <first_name>WILL</first_name>
    <last_name>WILSON</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>169</actor_id>
    <first_name>KENNETH</first_name>
    <last_name>HOFFMAN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>170</actor_id>
    <first_name>MENA</first_name>
    <last_name>HOPPER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>171</actor_id>
    <first_name>OLYMPIA</first_name>
    <last_name>PFEIFFER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>172</actor_id>
    <first_name>GROUCHO</first_name>
    <last_name>WILLIAMS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>173</actor_id>
    <first_name>ALAN</first_name>
    <last_name>DREYFUSS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>174</actor_id>
    <first_name>MICHAEL</first_name>
    <last_name>BENING</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>175</actor_id>
    <first_name>WILLIAM</first_name>
    <last_name>HACKMAN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>176</actor_id>
    <first_name>JON</first_name>
    <last_name>CHASE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>177</actor_id>
    <first_name>GENE</first_name>
    <last_name>MCKELLEN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>178</actor_id>
    <first_name>LISA</first_name>
    <last_name>MONROE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>179</actor_id>
    <first_name>ED</first_name>
    <last_name>GUINESS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>180</actor_id>
    <first_name>JEFF</first_name>
    <last_name>SILVERSTONE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>181</actor_id>
    <first_name>MATTHEW</first_name>
    <last_name>CARREY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>182</actor_id>
    <first_name>DEBBIE</first_name>
    <last_name>AKROYD</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>183</actor_id>
    <first_name>RUSSELL</first_name>
    <last_name>CLOSE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>184</actor_id>
    <first_name>HUMPHREY</first_name>
    <last_name>GARLAND</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>185</actor_id>
    <first_name>MICHAEL</first_name>
    <last_name>BOLGER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>186</actor_id>
    <first_name>JULIA</first_name>
    <last_name>ZELLWEGER</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>187</actor_id>
    <first_name>RENEE</first_name>
    <last_name>BALL</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>188</actor_id>
    <first_name>ROCK</first_name>
    <last_name>DUKAKIS</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>189</actor_id>
    <first_name>CUBA</first_name>
    <last_name>BIRCH</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>190</actor_id>
    <first_name>AUDREY</first_name>
    <last_name>BAILEY</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>191</actor_id>
    <first_name>GREGORY</first_name>
    <last_name>GOODING</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>192</actor_id>
    <first_name>JOHN</first_name>
    <last_name>SUVARI</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>193</actor_id>
    <first_name>BURT</first_name>
    <last_name>TEMPLE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>194</actor_id>
    <first_name>MERYL</first_name>
    <last_name>ALLEN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>195</actor_id>
    <first_name>JAYNE</first_name>
    <last_name>SILVERSTONE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>196</actor_id>
    <first_name>BELA</first_name>
    <last_name>WALKEN</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>197</actor_id>
    <first_name>REESE</first_name>
    <last_name>WEST</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>198</actor_id>
    <first_name>MARY</first_name>
    <last_name>KEITEL</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>199</actor_id>
    <first_name>JULIA</first_name>
    <last_name>FAWCETT</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
  <record>
    <actor_id>200</actor_id>
    <first_name>THORA</first_name>
    <last_name>TEMPLE</last_name>
    <last_update>2020-06-11T02:50:54Z</last_update>
  </record>
</records>
```

