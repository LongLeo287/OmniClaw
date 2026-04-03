---
id: github.com-neilotoole-tailbuf-7c616bc1-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:04.662888
---

# KNOWLEDGE EXTRACT: github.com_neilotoole_tailbuf_7c616bc1
> **Extracted on:** 2026-04-01 09:39:13
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520347/github.com_neilotoole_tailbuf_7c616bc1

---

## File: `.gitignore`
```
# If you prefer the allow list template instead of the deny list, see community template:
# https://github.com/github/gitignore/blob/main/community/Golang/Go.AllowList.gitignore
#
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

# Go workspace file
go.work
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
    module-path: github.com/neilotoole/tailbuf
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
          - "fmt.Println"
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

Copyright (c) 2024 Neil O'Toole

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
# tailbuf: tail, for Go objects

[![Go Reference](https://pkg.go.dev/badge/github.com/neilotoole/tailbuf.svg)](https://pkg.go.dev/github.com/neilotoole/tailbuf)
[![Go Report Card](https://goreportcard.com/badge/neilotoole/tailbuf)](https://goreportcard.com/report/neilotoole/tailbuf)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/neilotoole/tailbuf/blob/master/LICENSE)
![Workflow](https://github.com/neilotoole/tailbuf/actions/workflows/go.yml/badge.svg)

Package [`neilotoole/tailbuf`](https://pkg.go.dev/github.com/neilotoole/tailbuf) implements a fixed-size object tail buffer that provides a window
on the tail of items written to the buffer.

## Install

Add to your `go.mod` via `go get`:

```shell
go get github.com/neilotoole/tailbuf
```

## Usage

> [!WARNING]  
> Note that `tailbuf` is still in its `v0.0.x` infancy. There's a few things in
> the package API that probably need to be dialed in, so expect some churn.
> [Feedback](https://github.com/neilotoole/tailbuf/issues) is appreciated.

Below we'll create a [`tailbuf.Buf`](https://pkg.go.dev/github.com/neilotoole/tailbuf#Buf)
of type `string` with a capacity of `3`. You write to the buffer using [`buf.Write`](https://pkg.go.dev/github.com/neilotoole/tailbuf#Buf.Write)
or [`buf.WriteAll`](https://pkg.go.dev/github.com/neilotoole/tailbuf#Buf.WriteAll), and
you can access the tail slice using [`Buf.Tail`](https://pkg.go.dev/github.com/neilotoole/tailbuf#Buf.Tail).

```go
package main

import (
    "fmt"
    "github.com/neilotoole/tailbuf"
)

func main() {
    buf := tailbuf.New[string](3)

    buf.WriteAll("a", "b", "c")
    fmt.Println(buf.Tail())   // [a b c]

    buf.WriteAll("d", "e", "f", "g")
    fmt.Println(buf.Tail())   // [e f g]

    fmt.Println("Written:", buf.Written()) // Written: 7
}
```

Note that `Buf.Tail` returns a slice into the buffer's internal storage, so it's
only valid until the next write operation. If you need to retain the tail slice,
you should copy the returned slice, or instead use [`tailbuf.SliceTail`](https://pkg.go.dev/github.com/neilotoole/tailbuf#SliceTail), which
always returns a freshly-allocated slice.

There are various functions for popping, dropping, or peeking into the tail buffer.

```go
  buf := tailbuf.New[string](3)

  buf.WriteAll("a", "b", "c")
  fmt.Println(buf.Peek(0))      // a
  fmt.Println(buf.Peek(1))      // b

  fmt.Println(buf.PopBackN(2))  // [a b]
  fmt.Println(buf.Tail())       // [c]
```

There are also basic methods for interacting with the buffer:

```go
  buf := tailbuf.New[string](3)

  fmt.Println(buf.Cap())                   // 3
  fmt.Println(buf.Len())                   // 0
  buf.WriteAll("a", "b", "c")
  fmt.Println(buf.Len())                   // 3

  buf.WriteAll("d", "e", "f", "g")
  fmt.Println(buf.Len())                   // 3

  fmt.Println("Written:", buf.Written())   // 7
  buf.Reset()                              // Reset the buffer, including "written" count
  fmt.Println(buf.Len())                   // 0
  fmt.Println("Written:", buf.Written())   // 0

  buf.WriteAll("h", "i")
  fmt.Println(buf.Len())                   // 2
  fmt.Println("Written:", buf.Written())   // 2

  buf.Clear()                              // Clear is like Reset, but doesn't reset "written" count
  fmt.Println(buf.Len())                   // 0
  fmt.Println("Written:", buf.Written())   // 2
```


And then there's the [`Apply`](https://pkg.go.dev/github.com/neilotoole/tailbuf#Buf.Apply) method, which applies a func to each element in the buffer,
and also its bigger brother [`Do`](https://pkg.go.dev/github.com/neilotoole/tailbuf#Buf.Do), which does the same thing, but with context and
error awareness.

```go
  buf := tailbuf.New[string](3)
  buf.WriteAll("In", "Xanadu  ", "   did", "Kubla  ", "Khan")
  buf.Apply(strings.ToUpper).Apply(strings.TrimSpace)
  fmt.Println(buf.Tail()) // [DID KUBLA KHAN]
```


See the [package reference](https://pkg.go.dev/github.com/neilotoole/tailbuf) for more details.
```

## File: `go.mod`
```
module github.com/neilotoole/tailbuf

go 1.20

require github.com/stretchr/testify v1.9.0

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
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/stretchr/testify v1.9.0 h1:HtqpIVDClZ4nwg75+f6Lvsy/wHu+3BoSGCbBAcpTsTg=
github.com/stretchr/testify v1.9.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `internal_test.go`
```go
package tailbuf

import (
	"testing"

	"github.com/stretchr/testify/require"
)

// InternalWindow exposes Buf's internal window for testing.
func InternalWindow[T any](b *Buf[T]) []T {
	return b.window
}

// TailNewSlice exposes Buf's internal tailNewSlice for testing.
func TailNewSlice[T any](b *Buf[T]) []T {
	return b.tailNewSlice()
}

// RequireEqualInternalState asserts that a and b have the same internal state.
func RequireEqualInternalState[T any](tb testing.TB, a, b *Buf[T]) {
	tb.Helper()
	require.Equal(tb, a.window, b.window)
	require.Equal(tb, a.len, b.len)
	require.Equal(tb, a.back, b.back)
	require.Equal(tb, a.front, b.front)
	require.Equal(tb, cap(a.window), cap(b.window))
	require.Equal(tb, len(a.window), len(b.window))
	require.Equal(tb, a.window, b.window)
}
```

## File: `tailbuf.go`
```go
// Package tailbuf contains a tail buffer [Buf] of fixed size that provides a
// window on the tail of the items written via [Buf.Write] or [Buf.WriteAll].
// Start with [tailbuf.New] to create a [Buf].
package tailbuf

import "context"

// Buf is an append-only fixed-size circular buffer that provides a window on
// the tail of items written to the buffer. The zero value is technically
// usable, but not very useful. Instead, invoke [tailbuf.New] to create a Buf.
// Buf is not safe for concurrent use.
//
// Note the terms "nominal buffer" and "tail window" (or just "window"). The
// nominal buffer is the complete list of items written to Buf via the
// [Buf.Write] or [Buf.WriteAll] methods. However, Buf drops the oldest items as
// it fills (which is the entire point of this package): the tail window is the
// subset of the nominal buffer that is currently available.
type Buf[T any] struct {
	// zero is the zero value of T, used for zeroing elements of the in-use
	// window so that after operations like Buf.DropBack we don't accidentally
	// hold on to references. This is probably a premature optimization; needs
	// benchmarks.
	zero T

	// window is the circular buffer.
	window []T

	// len is the number of items currently in the buffer.
	len int

	// back is the cursor for the oldest item.
	back int

	// REVISIT: Do we need both back and front?
	// Could we just use back and len?

	// front is the cursor for the newest item.
	front int

	// written is the total number of items added via Buf.Write or Buf.WriteAll.
	written int
}

// New returns a new Buf with the specified capacity. It panics if capacity is
// less than 1.
func New[T any](capacity int) *Buf[T] {
	if capacity < 0 {
		panic("capacity must be >= 0") // FIXME: make zero value usable
	}

	return &Buf[T]{
		window: make([]T, capacity),
		back:   -1,
		front:  -1,
	}
}

// Write appends t to the buffer. If the buffer fills, the oldest item is
// overwritten. The buffer is returned for chaining.
func (b *Buf[T]) Write(t T) *Buf[T] {
	if len(b.window) == 0 {
		// We won't actually store the item, but we still count it.
		b.written++
		return b
	}

	b.write(t)
	return b
}

// WriteAll appends items to the buffer. If the buffer fills, the oldest items
// are overwritten. The buffer is returned for chaining.
func (b *Buf[T]) WriteAll(a ...T) *Buf[T] {
	if len(b.window) == 0 {
		// We won't actually store the items, but we still count them.
		b.written += len(a)
		return b
	}

	for i := range a {
		b.write(a[i])
	}
	return b
}

// write appends item [Buf]. If the buffer is full, the oldest item is
// overwritten.
func (b *Buf[T]) write(item T) {
	b.written++
	switch {
	case b.front == -1:
		b.back = 0
	case b.written > len(b.window):
		b.back = (b.back + 1) % len(b.window)
	default:
	}

	b.front = (b.front + 1) % len(b.window)
	b.window[b.front] = item
	if b.len < len(b.window) {
		b.len++
	}
}

// Tail returns a slice containing the items currently in the buffer, in
// oldest-to-newest order. If possible, the returned slice shares the buffer's
// internal window, but a fresh slice is allocated if necessary. Thus you
// should copy the returned slice before modifying it, or instead use
// [SliceTail].
func (b *Buf[T]) Tail() []T {
	switch {
	case b.len == 0:
		return b.window[:0]
	case b.len == 1:
		return b.window[b.front : b.front+1]
	case b.front > b.back:
		return b.window[b.back : b.front+1]
	default:
		s := make([]T, b.len)
		copy(s, b.window[b.back:])
		copy(s[len(b.window)-b.back:], b.window[:b.front+1])
		return s
	}
}

// tailNewSlice is like Buf.Tail but it always returns a fresh slice.
func (b *Buf[T]) tailNewSlice() []T {
	switch {
	case b.len == 0:
		return make([]T, 0)
	case b.len == 1:
		return []T{b.window[b.front]}
	case b.front > b.back:
		s := make([]T, b.front-b.back+1)
		copy(s, b.window[b.back:b.front+1])
		return s
	default:
		s := make([]T, b.len)
		copy(s, b.window[b.back:])
		copy(s[len(b.window)-b.back:], b.window[:b.front+1])
		return s
	}
}

// Written returns the total number of items written to the buffer.
func (b *Buf[T]) Written() int {
	return b.written
}

// InBounds returns true if the index i of the nominal buffer is within the
// bounds of the tail window. That is to say, InBounds returns true if the ith
// item written to the buffer is still in the tail window.
func (b *Buf[T]) InBounds(i int) bool {
	if b.written == 0 || i < 0 || len(b.window) == 0 {
		return false
	}
	start, end := b.Bounds()
	return i >= start && i < end
}

// Bounds returns the start and end indices of the tail window vs the nominal
// buffer. If the buffer is empty, start and end are both 0. The returned
// values are the same as [Buf.Offset] and [Buf.Written].
func (b *Buf[T]) Bounds() (start, end int) {
	return b.Offset(), b.Written()
}

// Cap returns the capacity of Buf, which is the fixed size specified when
// the buffer was created.
func (b *Buf[T]) Cap() int {
	return len(b.window)
}

// Len returns the number of items currently in the buffer.
func (b *Buf[T]) Len() int {
	return b.len
}

// zeroTail zeroes out the items in the tail window.
func (b *Buf[T]) zeroTail() {
	if b.front > b.back {
		for i := b.back; i <= b.front; i++ {
			b.window[i] = b.zero
		}
	} else {
		for i := b.back; i < len(b.window); i++ {
			b.window[i] = b.zero
		}
		for i := 0; i <= b.front; i++ {
			b.window[i] = b.zero
		}
	}
}

// Reset resets the buffer to its initial state, including the value returned
// by [Buf.Written]. The buffer is returned for chaining. Any items in the
// buffer are zeroed out.
//
// See also: [Buf.Clear].
func (b *Buf[T]) Reset() *Buf[T] {
	b.Clear()
	b.written = 0
	return b
}

// Clear removes all items from the buffer, zeroing all values. This is similar
// to [Buf.Reset], but note that the value returned by [Buf.Written] is
// unchanged. The buffer is returned for chaining.
//
// See also: [Buf.Reset].
func (b *Buf[T]) Clear() *Buf[T] {
	b.zeroTail()

	b.back = -1
	b.front = -1
	b.len = 0

	return b
}

// Offset returns the offset of the current window vs the nominal complete list
// of items written to the buffer. It is effectively the count of items that
// have slipped out of the tail window. If the buffer is empty, the returned
// offset is 0.
func (b *Buf[T]) Offset() int {
	if b.written <= len(b.window) {
		return 0
	}

	return b.written - len(b.window)
}

// Front returns the newest item in the tail window. If Buf is empty, the zero
// value of T is returned.
func (b *Buf[T]) Front() T {
	if b.front == -1 {
		var t T
		return t
	}
	return b.window[b.front]
}

// PopFront removes and returns the newest item in the tail window.
func (b *Buf[T]) PopFront() T {
	if b.front == -1 {
		var zero T
		return zero
	}

	item := b.window[b.front]
	b.window[b.front] = b.zero
	if b.front == b.back {
		b.back = -1
		b.front = -1
	} else {
		b.front = (b.front - 1 + len(b.window)) % len(b.window)
	}
	b.len--
	return item
}

// Back returns the oldest item in the tail window. If Buf is empty, the zero
// value of T is returned.
func (b *Buf[T]) Back() T {
	if b.back == -1 {
		var t T
		return t
	}
	return b.window[b.back]
}

// DropBack removes the oldest item in the tail window.
// See also: [Buf.PopBack].
func (b *Buf[T]) DropBack() {
	if b.back == -1 {
		return
	}

	b.window[b.back] = b.zero
	if b.front == b.back {
		b.back = -1
		b.front = -1
	} else {
		b.back = (b.back + 1) % len(b.window)
	}
	b.len--
}

// DropBackN removes the oldest n items from the tail, zeroing out the items.
// If n >= [Buf.Len], all items in the tail window are removed.
func (b *Buf[T]) DropBackN(n int) {
	if b.len == 0 || n < 1 {
		return
	}

	if n >= b.len {
		b.Clear()
		return
	}

	b.len -= n

	if b.front > b.back {
		for i := 0; i < n; i++ {
			b.window[b.back] = b.zero
			b.back = (b.back + 1) % len(b.window)
		}
		return
	}

	for i := 0; i < n; i++ {
		b.window[b.back] = b.zero
		b.back = (b.back + 1) % len(b.window)
	}
}

// Peek returns the nth item in the tail window. Peek panics if n is not a valid
// index, or if the buffer is empty.
func (b *Buf[T]) Peek(n int) T {
	if b.len == 0 || n < 0 || n >= b.len {
		panic("tailbuf: Peek out of bounds")
	}

	if b.front > b.back {
		return b.window[(b.back+n)%len(b.window)]
	}

	return b.window[(b.back+n)%len(b.window)]
}

// PopBack removes and returns the oldest item in the tail window. If the buffer
// is empty, the zero value of T is returned.
func (b *Buf[T]) PopBack() T {
	if b.back == -1 {
		var zero T
		return zero
	}

	item := b.window[b.back]
	b.window[b.back] = b.zero
	if b.front == b.back {
		b.back = -1
		b.front = -1
	} else {
		b.back = (b.back + 1) % len(b.window)
	}
	b.len--
	return item
}

// PopBackN removes and returns the oldest n items in the tail window. Any
// removed items are zeroed out from the buffer's internal window. On return,
// the slice (which is always freshly allocated) contains the removed items, in
// oldest-to-newest order, and Buf.Len is reduced by n. If n is greater than the
// number of items in the tail window, all items in the tail window are removed
// and returned.
func (b *Buf[T]) PopBackN(n int) []T {
	if b.len == 0 || n < 1 {
		return make([]T, 0)
	}

	if n >= b.len {
		s := b.tailNewSlice()
		b.Clear()
		return s
	}

	b.len -= n
	if b.front > b.back {
		s := make([]T, n)
		for i := 0; i < n; i++ {
			s[i] = b.window[b.back]
			b.window[b.back] = b.zero
			b.back = (b.back + 1) % len(b.window)
		}
		return s
	}

	s := make([]T, n)
	for i := 0; i < n; i++ {
		s[i] = b.window[b.back]
		b.window[b.back] = b.zero
		b.back = (b.back + 1) % len(b.window)
	}
	return s
}

// PopFrontN removes and returns the newest n items in the tail window. Any
// removed items are zeroed out from the buffer's internal window. On return,
// the slice (which is always freshly allocated) contains the removed items, in
// oldest-to-newest order, and Buf.Len is reduced by n. If n is greater than the
// number of items in the tail window, all items in the tail window are removed
// and returned.
func (b *Buf[T]) PopFrontN(n int) []T {
	if b.len == 0 || n < 1 {
		return make([]T, 0)
	}

	if n >= b.len {
		s := b.tailNewSlice()
		b.Clear()
		return s
	}

	b.len -= n

	if b.front > b.back {
		s := make([]T, n)
		for i := n - 1; i >= 0; i-- {
			s[i] = b.window[b.front]
			b.window[b.front] = b.zero
			b.front = (b.front - 1 + len(b.window)) % len(b.window)
		}
		return s
	}

	s := make([]T, n)
	for i := n - 1; i >= 0; i-- {
		s[i] = b.window[b.front]
		b.window[b.front] = b.zero
		b.front = (b.front - 1 + len(b.window)) % len(b.window)
	}
	return s
}

// Apply applies fn to each item in the tail window, in oldest-to-newest order,
// mutating the items in place. If Buf is empty, fn is not invoked. The buffer
// is returned for chaining.
//
//	buf := tailbuf.New[string](3)
//	buf.WriteAll("a", "b  ", "   c  ")
//	buf.Apply(strings.TrimSpace).Apply(strings.ToUpper)
//	fmt.Println(buf.Tail())
//	// Output: [A B C]
//
// Using Apply is cheaper than getting the slice via [Buf.Tail] and applying fn
// manually, as it avoids the possible allocation of a new slice by Buf.Tail.
//
// The behavior of Apply is undefined if the buffer is modified during
// execution.
//
// For more control, or to handle errors, use [Buf.Do].
func (b *Buf[T]) Apply(fn func(item T) T) *Buf[T] {
	if b.len == 0 {
		return b
	}

	if b.front > b.back {
		for i := b.back; i <= b.front; i++ {
			b.window[i] = fn(b.window[i])
		}
		return b
	}

	for i := b.back; i < len(b.window); i++ {
		b.window[i] = fn(b.window[i])
	}

	for i := 0; i <= b.front; i++ {
		b.window[i] = fn(b.window[i])
	}
	return b
}

// Do applies fn to each item in the tail window, in oldest-to-newest order,
// replacing each item with the value returned by successful invocation of fn.
// If fn returns an error, the item is not replaced. Execution is halted if any
// invocation of fn returns an error, and that error is returned to the caller.
// Thus a partial application of fn may occur.
//
// If Buf is empty, fn is not invoked.
//
// The index arg to fn is the index of the item in the tail window. The
// tailOffset arg is the offset of the first item in the tail window vs the
// nominal buffer. That is to say, it's the value of [Buf.Offset].
// You can use these values to calculate the nominal index of the item:
//
//	nominalIndex := index + tailOffset
//
// The context is not checked for cancellation between invocations of fn. If you
// need to check for cancellation, do so inside fn.
//
// The behavior of Do is undefined if the buffer is modified during execution.
func (b *Buf[T]) Do(ctx context.Context, fn func(ctx context.Context, item T, index, tailOffset int) (T, error)) error {
	if b.len == 0 {
		return nil
	}

	if ctx == nil {
		ctx = context.Background()
	}

	var v T
	var err error

	if b.front > b.back {
		for i := b.back; i <= b.front; i++ {
			v, err = fn(ctx, b.window[i], i, i-b.back)
			if err != nil {
				return err
			}
			b.window[i] = v
		}
		return nil
	}

	for i := b.back; i < len(b.window); i++ {
		v, err = fn(ctx, b.window[i], i, i-b.back)
		if err != nil {
			return err
		}
		b.window[i] = v
	}

	for i := 0; i <= b.front; i++ {
		v, err = fn(ctx, b.window[i], i, i-b.back)
		if err != nil {
			return err
		}
		b.window[i] = v
	}

	return nil
}

// SliceNominal is a convenience function that returns a fresh slice into the
// nominal buffer, using the standard [inclusive:exclusive] slicing mechanics.
//
// Boundary checking is relaxed. If the buffer is empty, the returned slice is
// empty. Otherwise, if the requested range is completely outside the bounds of
// the tail window, the returned slice is empty; if the range overlaps with the
// tail window, the returned slice contains the overlapping items. If strict
// boundary checking is important to you, use [Buf.InBounds] to check the start
// and end indices.
//
// SliceNominal is approximately functionally equivalent to reslicing the result
// of [Buf.Tail], but it may avoid wasteful copying (and has relaxed bounds
// checking).
//
//	buf := tailbuf.New[int](3).WriteAll(1, 2, 3)
//	a := buf.Tail()[0:2]
//	b := buf.SliceNominal(0, 2)
//	assert.Equal(t, a, b)
//
// If start < 0, zero is used. SliceNominal panics if end is less than start.
func SliceNominal[T any](b *Buf[T], start, end int) []T {
	offset := b.Offset()
	start -= offset
	if start < 0 {
		start = 0
	}
	end -= offset
	if end <= start {
		return make([]T, 0)
	}

	return SliceTail(b, start, end)
}

// SliceTail returns a slice of the tail window, using the standard
// [inclusive:exclusive] slicing mechanics, but with permissive bounds checking.
// The slice is freshly allocated, so the caller is free to mutate it.
//
// A call to SliceTail is equivalent to reslicing the result of [Buf.Tail], but
// it may avoid unnecessary copying, depending on the state of Buf.
//
//	buf := tailbuf.New[int](3).WriteAll(1, 2, 3)
//	a := buf.Tail()[0:2]
//	b := buf.SliceTail(0, 2)
//	fmt.Println("a:", a, "b:", b)
//	// Output: a: [1 2] b: [1 2]
//
// If Buf is empty, the returned slice is empty. Otherwise, if the requested
// range is completely outside the bounds of the tail window, the returned slice
// is empty; if the range overlaps with the tail window, the returned slice
// contains the overlapping items. If strict boundary checking is important, use
// [Buf.InBounds] to check the start and end indices.
//
// SliceTail panics if start is negative or end is less than start.
//
// See also: [SliceNominal], [Buf.Tail], [Buf.Bounds], [Buf.InBounds].
func SliceTail[T any](b *Buf[T], start, end int) []T {
	switch {
	case start < 0:
		panic("start must be >= 0")
	case end < start:
		panic("end must be >= start")
	case len(b.window) == 0, end == start, b.written == 0, start >= b.written:
		return make([]T, 0)
	case b.written == 1, b.front == b.back:
		// Special case: the buffer has only one item.
		if start == 0 && end >= 1 {
			return []T{b.window[0]}
		}
		return make([]T, 0)
	case b.front > b.back:
		if end > b.written {
			end = b.written
		}
		if end > len(b.window) {
			end = len(b.window)
		}
		s := make([]T, 0, end-start)
		return append(s, b.window[start:end]...)
	default: // b.back > b.front
		if end >= b.written {
			end = b.written - 1
		}
		if end > len(b.window) {
			end = len(b.window)
		}
		s := make([]T, 0, end-start)
		s = append(s, b.window[b.back+start:]...)
		frontIndex := b.front + end - len(b.window) + 1

		return append(s, b.window[:frontIndex]...)
	}
}
```

## File: `tailbuf_test.go`
```go
package tailbuf_test

import (
	"context"
	"fmt"
	"strings"
	"testing"

	"github.com/stretchr/testify/require"

	"github.com/neilotoole/tailbuf"
)

func ExampleBuf() {
	buf := tailbuf.New[string](3)

	buf.WriteAll("a", "b", "c")
	fmt.Println(buf.Tail())

	buf.WriteAll("d", "e", "f", "g")
	fmt.Println(buf.Tail())

	fmt.Println("Written:", buf.Written())

	// Output:
	// [a b c]
	// [e f g]
	// Written: 7
}

func ExampleBuf_Peek() {
	buf := tailbuf.New[string](3)

	buf.WriteAll("a", "b", "c")
	fmt.Println(buf.Peek(0))
	fmt.Println(buf.Peek(1))

	fmt.Println(buf.PopBackN(2))
	fmt.Println(buf.Tail())
	// Output:
	// a
	// b
	// [a b]
	// [c]
}

func ExampleBuf_Len() {
	buf := tailbuf.New[string](3)

	fmt.Println(buf.Cap())
	fmt.Println(buf.Len())
	buf.WriteAll("a", "b", "c")
	fmt.Println(buf.Len())

	buf.WriteAll("d", "e", "f", "g")
	fmt.Println(buf.Len())

	fmt.Println("Written:", buf.Written())
	buf.Reset()
	fmt.Println(buf.Len())
	fmt.Println("Written:", buf.Written())

	buf.WriteAll("h", "i")
	fmt.Println(buf.Len())
	fmt.Println("Written:", buf.Written())

	buf.Clear() // Clear is like Reset, but doesn't reset the written counter
	fmt.Println(buf.Len())
	fmt.Println("Written:", buf.Written())

	// Output:
	// 3
	// 0
	// 3
	// 3
	// Written: 7
	// 0
	// Written: 0
	// 2
	// Written: 2
	// 0
	// Written: 2
}

func ExampleBuf_Apply() {
	buf := tailbuf.New[string](3)
	buf.WriteAll("In", "Xanadu  ", "   did", "Kubla  ", "Khan")
	buf.Apply(strings.ToUpper).Apply(strings.TrimSpace)
	fmt.Println(buf.Tail())

	// Output:
	// [DID KUBLA KHAN]
}

func TestTail(t *testing.T) {
	buf := tailbuf.New[rune](3)
	gotLen := buf.Len()
	require.Equal(t, 0, gotLen)
	require.Equal(t, 0, buf.Written())
	require.Empty(t, buf.Tail())
	require.Empty(t, tailbuf.TailNewSlice(buf))

	buf.Write('a')
	require.Equal(t, 1, buf.Written())
	gotLen = buf.Len()
	require.Equal(t, 1, gotLen)
	gotTail := buf.Tail()
	require.Equal(t, []rune{'a'}, gotTail)
	require.Equal(t, gotTail, tailbuf.TailNewSlice(buf))

	buf.Write('b')
	require.Equal(t, 2, buf.Written())
	gotLen = buf.Len()
	require.Equal(t, 2, gotLen)
	gotTail = buf.Tail()
	require.Equal(t, []rune{'a', 'b'}, gotTail)
	require.Equal(t, gotTail, tailbuf.TailNewSlice(buf))

	buf.Write('c')
	require.Equal(t, 3, buf.Written())
	gotLen = buf.Len()
	require.Equal(t, 3, gotLen)
	gotTail = buf.Tail()
	require.Equal(t, []rune{'a', 'b', 'c'}, gotTail)
	require.Equal(t, gotTail, tailbuf.TailNewSlice(buf))

	buf.Write('d')
	require.Equal(t, 4, buf.Written())
	gotLen = buf.Len()
	require.Equal(t, 3, gotLen)
	gotTail = buf.Tail()
	require.Equal(t, []rune{'b', 'c', 'd'}, gotTail)
	require.Equal(t, gotTail, tailbuf.TailNewSlice(buf))

	buf.Write('e')
	require.Equal(t, 5, buf.Written())
	gotLen = buf.Len()
	require.Equal(t, 3, gotLen)
	gotTail = buf.Tail()
	require.Equal(t, []rune{'c', 'd', 'e'}, gotTail)
	require.Equal(t, gotTail, tailbuf.TailNewSlice(buf))

	buf.Write('f')
	require.Equal(t, 6, buf.Written())
	gotLen = buf.Len()
	require.Equal(t, 3, gotLen)
	gotTail = buf.Tail()
	require.Equal(t, []rune{'d', 'e', 'f'}, gotTail)
	require.Equal(t, gotTail, tailbuf.TailNewSlice(buf))

	buf.Write('g')
	require.Equal(t, 7, buf.Written())
	gotLen = buf.Len()
	require.Equal(t, 3, gotLen)
	gotTail = buf.Tail()
	require.Equal(t, []rune{'e', 'f', 'g'}, gotTail)
	require.Equal(t, gotTail, tailbuf.TailNewSlice(buf))

	buf.WriteAll('h', 'i', 'j')
	require.Equal(t, 10, buf.Written())
	gotLen = buf.Len()
	require.Equal(t, 3, gotLen)
	gotTail = buf.Tail()
	require.Equal(t, []rune{'h', 'i', 'j'}, gotTail)
	require.Equal(t, gotTail, tailbuf.TailNewSlice(buf))
}

func TestBuf(t *testing.T) {
	testCases := []struct {
		wantWindow         []rune
		add                rune
		wantStart, wantEnd int
	}{
		{add: 'a', wantStart: 0, wantEnd: 1, wantWindow: []rune{'a'}},
		{add: 'b', wantStart: 0, wantEnd: 2, wantWindow: []rune{'a', 'b'}},
		{add: 'c', wantStart: 0, wantEnd: 3, wantWindow: []rune{'a', 'b', 'c'}},
		{add: 'd', wantStart: 1, wantEnd: 4, wantWindow: []rune{'b', 'c', 'd'}},
		{add: 'e', wantStart: 2, wantEnd: 5, wantWindow: []rune{'c', 'd', 'e'}},
		{add: 'f', wantStart: 3, wantEnd: 6, wantWindow: []rune{'d', 'e', 'f'}},
		{add: 'g', wantStart: 4, wantEnd: 7, wantWindow: []rune{'e', 'f', 'g'}},
		{add: 'h', wantStart: 5, wantEnd: 8, wantWindow: []rune{'f', 'g', 'h'}},
	}

	buf := tailbuf.New[rune](3)

	for i, tc := range testCases {
		tc := tc
		t.Run(fmt.Sprintf("%d_%s", i, string(tc.add)), func(t *testing.T) {
			buf.Write(tc.add)
			require.Equal(t, tc.wantEnd, buf.Written())
			require.Equal(t, tc.add, buf.Front())
			window := buf.Tail()
			require.Equal(t, tc.wantWindow, window)
			start, end := buf.Bounds()
			require.Equal(t, tc.wantStart, start)
			require.Equal(t, tc.wantEnd, end)
			s := tailbuf.SliceNominal(buf, start, end+1)
			require.Equal(t, window, s)
		})
	}
}

func TestBounds(t *testing.T) {
	buf := tailbuf.New[string](3)
	start, end := buf.Bounds()
	require.Equal(t, 0, start)
	require.Equal(t, 0, end)

	require.False(t, buf.InBounds(-1))
	require.False(t, buf.InBounds(0))
	require.False(t, buf.InBounds(1))

	buf.WriteAll("a", "b", "c")
	start, end = buf.Bounds()
	require.Equal(t, 0, start)
	require.Equal(t, 3, end)
	require.True(t, buf.InBounds(0))
	require.True(t, buf.InBounds(1))
	require.True(t, buf.InBounds(2))
	require.False(t, buf.InBounds(3))

	buf.WriteAll("d", "e")
	start, end = buf.Bounds()
	require.Equal(t, 2, start)
	require.Equal(t, 5, end)
	require.False(t, buf.InBounds(0))
	require.False(t, buf.InBounds(1))
	for i := 2; i < 5; i++ {
		require.True(t, buf.InBounds(i))
	}
	require.False(t, buf.InBounds(5))
}

func TestSlice(t *testing.T) {
	buf := tailbuf.New[int](3)
	buf.WriteAll(0, 1, 2)

	start, end := buf.Bounds()
	require.Equal(t, 0, start)
	require.Equal(t, 3, end)
	s := tailbuf.SliceNominal(buf, start, end)
	require.Equal(t, []int{0, 1, 2}, s)

	s = tailbuf.SliceNominal(buf, 0, 0)
	require.Empty(t, s)

	s = tailbuf.SliceNominal(buf, 0, 1)
	require.Equal(t, []int{0}, s)
	s = tailbuf.SliceNominal(buf, 0, 2)
	require.Equal(t, []int{0, 1}, s)
	s = tailbuf.SliceNominal(buf, 0, 3)
	require.Equal(t, []int{0, 1, 2}, s)

	s = tailbuf.SliceNominal(buf, 1, 1)
	require.Empty(t, s)
	s = tailbuf.SliceNominal(buf, 1, 3)
	require.Equal(t, []int{1, 2}, s)

	buf.WriteAll(3, 4, 5)
	start, end = buf.Bounds()
	require.Equal(t, 3, start)
	require.Equal(t, 6, end)
	s = tailbuf.SliceNominal(buf, start, end)
	require.Equal(t, []int{3, 4, 5}, s)

	s = tailbuf.SliceNominal(buf, 3, 3)
	require.Empty(t, s)
	s = tailbuf.SliceNominal(buf, 3, 4)
	require.Equal(t, []int{3}, s)
	s = tailbuf.SliceNominal(buf, 3, 5)
	require.Equal(t, []int{3, 4}, s)

	buf.WriteAll(6, 7)
	s = tailbuf.SliceNominal(buf, 6, 7)
	require.Equal(t, []int{6}, s)
}

func TestApply_Do(t *testing.T) {
	buf := tailbuf.New[string](3)
	buf.WriteAll("In", "Xanadu  ", "   did", "Kubla  ", "Khan")
	buf.Apply(strings.ToUpper).Apply(strings.TrimSpace)
	got := buf.Tail()
	require.Equal(t, []string{"DID", "KUBLA", "KHAN"}, got)

	err := buf.Do(context.Background(), func(_ context.Context, item string, _, _ int) (string, error) {
		return strings.ToLower(item), nil
	})
	require.NoError(t, err)
	got = buf.Tail()
	require.Equal(t, []string{"did", "kubla", "khan"}, got)
}

func TestPeek(t *testing.T) {
	buf := tailbuf.New[int](3)

	require.Panics(t, func() {
		_ = buf.Peek(0) // panics on empty buffer
	})

	buf.WriteAll(0, 1, 2)

	got := buf.Peek(0)
	require.Equal(t, 0, got)
	got = buf.Peek(1)
	require.Equal(t, 1, got)
	got = buf.Peek(2)
	require.Equal(t, 2, got)

	require.Panics(t, func() {
		_ = buf.Peek(-1)
	})

	require.Panics(t, func() {
		_ = buf.Peek(3)
	})
}

func TestTailSlice(t *testing.T) {
	buf := tailbuf.New[int](10).WriteAll(1, 2, 3, 4, 5)
	a := buf.Tail()[0:2]
	b := tailbuf.SliceTail(buf, 0, 2)
	require.Equal(t, []int{1, 2}, b)
	require.Equal(t, a, b)
}

func TestTail_Slice_Equivalence(t *testing.T) {
	buf := tailbuf.New[int](10).WriteAll(1, 2, 3, 4, 5)
	a := buf.Tail()[0:2]
	b := tailbuf.SliceNominal(buf, 0, 2)
	require.Equal(t, []int{1, 2}, b)
	require.Equal(t, a, b)
}

func TestWrittenGTCapacity(t *testing.T) {
	buf := tailbuf.New[string](1)
	buf.WriteAll("a", "b")
	require.Equal(t, 1, buf.Cap())
	require.Equal(t, 2, buf.Written())
	tail := buf.Tail()
	require.Equal(t, []string{"b"}, tail)
	tailSlice := tailbuf.SliceTail(buf, 0, 1)
	require.Equal(t, []string{"b"}, tailSlice)
	nomSlice := tailbuf.SliceNominal(buf, 0, 2)
	require.Equal(t, []string{"b"}, nomSlice)
	nomSlice = tailbuf.SliceNominal(buf, 0, 1)
	require.Empty(t, nomSlice)
}

func TestZeroCapacity(t *testing.T) {
	buf := tailbuf.New[rune](0)
	require.Equal(t, 0, buf.Cap())
	require.Equal(t, 0, buf.Written())
	require.Equal(t, 0, buf.Len())
	require.Empty(t, buf.Tail())

	buf.Write('a')

	require.Equal(t, 1, buf.Written())
	gotLen := buf.Len()
	require.Equal(t, 0, gotLen)
	require.Empty(t, buf.Tail())
	require.Empty(t, tailbuf.SliceNominal(buf, 0, 1))
}

func TestPopFront(t *testing.T) {
	buf := tailbuf.New[rune](3)
	buf.WriteAll('a', 'b', 'c')
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 3, buf.Len())
	require.Equal(t, 'c', buf.Front())
	require.Equal(t, 'a', buf.Back())
	require.Equal(t, []rune{'a', 'b', 'c'}, buf.Tail())

	got := buf.PopFront()
	require.Equal(t, 'c', got)
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 2, buf.Len())
	require.Equal(t, 'b', buf.Front())
	require.Equal(t, []rune{'a', 'b', 0}, tailbuf.InternalWindow(buf))
	require.Equal(t, []rune{'a', 'b'}, buf.Tail())

	got = buf.PopFront()
	require.Equal(t, 'b', got)
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 1, buf.Len())
	require.Equal(t, 'a', buf.Front())
	require.Equal(t, []rune{'a', 0, 0}, tailbuf.InternalWindow(buf))
	require.Equal(t, []rune{'a'}, buf.Tail())

	got = buf.PopFront()
	require.Equal(t, 'a', got)
	require.Equal(t, 3, buf.Written())
	require.Empty(t, buf.Front())
	requireZeroInternalWindow(t, buf)
	require.Equal(t, 0, buf.Len())
	require.Equal(t, []rune{}, buf.Tail())

	got = buf.PopFront()
	require.Zero(t, got)
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 0, buf.Len())
	require.Empty(t, buf.Front())
	requireZeroInternalWindow(t, buf)
	require.Equal(t, []rune{}, buf.Tail())
}

func TestPopBack(t *testing.T) {
	buf := tailbuf.New[rune](3)
	buf.WriteAll('a', 'b', 'c')
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 3, buf.Len())
	require.Equal(t, 'c', buf.Front())
	require.Equal(t, 'a', buf.Back())
	require.Equal(t, []rune{'a', 'b', 'c'}, tailbuf.InternalWindow(buf))
	require.Equal(t, []rune{'a', 'b', 'c'}, buf.Tail())

	got := buf.PopBack()
	require.Equal(t, 'a', got)
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 2, buf.Len())
	require.Equal(t, 'b', buf.Back())
	require.Equal(t, []rune{0, 'b', 'c'}, tailbuf.InternalWindow(buf))
	require.Equal(t, []rune{'b', 'c'}, buf.Tail())

	got = buf.PopBack()
	require.Equal(t, 'b', got)
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 1, buf.Len())
	require.Equal(t, 'c', buf.Back())
	require.Equal(t, []rune{0, 0, 'c'}, tailbuf.InternalWindow(buf))

	got = buf.PopBack()
	require.Equal(t, 'c', got)
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 0, buf.Len())
	require.Empty(t, buf.Back())
	requireZeroInternalWindow(t, buf)

	got = buf.PopBack()
	require.Zero(t, got)
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 0, buf.Len())
	require.Empty(t, buf.Back())
	requireZeroInternalWindow(t, buf)
}

func TestDropBack(t *testing.T) {
	buf := tailbuf.New[rune](3)
	buf.WriteAll('a', 'b', 'c')
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 3, buf.Len())
	require.Equal(t, 'a', buf.Back())
	require.Equal(t, []rune{'a', 'b', 'c'}, buf.Tail())

	buf.DropBack()
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 2, buf.Len())
	require.Equal(t, 'b', buf.Back())
	require.Equal(t, []rune{0, 'b', 'c'}, tailbuf.InternalWindow(buf))
	require.Equal(t, []rune{'b', 'c'}, buf.Tail())

	buf.DropBack()
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 1, buf.Len())
	require.Equal(t, 'c', buf.Back())
	require.Equal(t, []rune{0, 0, 'c'}, tailbuf.InternalWindow(buf))
	require.Equal(t, []rune{'c'}, buf.Tail())

	buf.DropBack()
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 0, buf.Len())
	require.Empty(t, buf.Back())
	requireZeroInternalWindow(t, buf)
	require.Empty(t, buf.Tail())

	buf.DropBack()
	require.Equal(t, 3, buf.Written())
	require.Equal(t, 0, buf.Len())
	require.Empty(t, buf.Back())
	requireZeroInternalWindow(t, buf)
	require.Empty(t, buf.Tail())
}

func TestPopBackN(t *testing.T) {
	all := []rune{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
	buf := tailbuf.New[rune](10)
	buf.WriteAll(all...)
	require.Equal(t, 10, buf.Len())
	require.Equal(t, 10, buf.Written())
	require.Equal(t, all, buf.Tail())

	got := buf.PopBackN(0)
	require.Empty(t, got)
	require.Equal(t, 10, buf.Len())
	require.Equal(t, 10, buf.Written())
	require.Equal(t, all, buf.Tail())

	got = buf.PopBackN(1)
	require.Equal(t, []rune{'a'}, got)
	require.Equal(t, 9, buf.Len())
	require.Equal(t, 10, buf.Written())
	window := tailbuf.InternalWindow(buf)
	require.Equal(t, []rune{0, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}, window)
	gotTail := buf.Tail()
	require.Equal(t, all[1:], gotTail)

	got = buf.PopBackN(3)
	require.Equal(t, []rune{'b', 'c', 'd'}, got)
	require.Equal(t, 6, buf.Len())
	require.Equal(t, 10, buf.Written())
	gotTail = buf.Tail()
	require.Equal(t, all[4:], gotTail)

	got = buf.PopBackN(10)
	require.Equal(t, []rune{'e', 'f', 'g', 'h', 'i', 'j'}, got)
	require.Equal(t, 0, buf.Len())
	require.Equal(t, 10, buf.Written())
	require.Empty(t, buf.Tail())
}

func TestPopFrontN(t *testing.T) {
	all := []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
	buf := tailbuf.New[string](10)
	buf.WriteAll(all...)
	require.Equal(t, 10, buf.Len())
	require.Equal(t, 10, buf.Written())
	require.Equal(t, all, buf.Tail())

	got := buf.PopFrontN(0)
	require.Empty(t, got)
	require.Equal(t, 10, buf.Len())
	require.Equal(t, 10, buf.Written())
	require.Equal(t, all, buf.Tail())

	got = buf.PopFrontN(1)
	require.Equal(t, []string{"j"}, got)
	require.Equal(t, 9, buf.Len())
	require.Equal(t, 10, buf.Written())
	window := tailbuf.InternalWindow(buf)
	require.Equal(t, []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", ""}, window)
	gotTail := buf.Tail()
	require.Equal(t, []string{"a", "b", "c", "d", "e", "f", "g", "h", "i"}, gotTail)

	got = buf.PopFrontN(2)
	require.Equal(t, []string{"h", "i"}, got)
	require.Equal(t, 7, buf.Len())
	require.Equal(t, 10, buf.Written())
	gotTail = buf.Tail()
	require.Equal(t, []string{"a", "b", "c", "d", "e", "f", "g"}, gotTail)

	got = buf.PopFrontN(10)
	require.Equal(t, []string{"a", "b", "c", "d", "e", "f", "g"}, got)
	require.Equal(t, 0, buf.Len())
	require.Equal(t, 10, buf.Written())
	gotTail = buf.Tail()
	require.Empty(t, gotTail)
}

func TestLen(t *testing.T) {
	all := []string{"a", "b", "c"}
	buf := tailbuf.New[string](3)
	require.Equal(t, 0, buf.Len())
	buf.Write("a")
	require.Equal(t, 1, buf.Len())
	buf.Write("b")
	require.Equal(t, 2, buf.Len())
	buf.Write("c")
	require.Equal(t, 3, buf.Len())
	buf.Clear()
	require.Equal(t, 0, buf.Len())
	buf.WriteAll(all...)
	require.Equal(t, 3, buf.Len())
}

func TestDropBackN(t *testing.T) {
	all := []rune{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
	buf := tailbuf.New[rune](10)
	buf.WriteAll(all...)
	require.Equal(t, 10, buf.Len())
	require.Equal(t, 10, buf.Written())
	require.Equal(t, all, buf.Tail())

	buf.DropBackN(0)
	require.Equal(t, 10, buf.Len())
	require.Equal(t, 10, buf.Written())
	require.Equal(t, all, buf.Tail())

	buf.DropBackN(1)
	require.Equal(t, 9, buf.Len())
	require.Equal(t, 10, buf.Written())
	window := tailbuf.InternalWindow(buf)
	require.Equal(t, []rune{0, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}, window)
	gotTail := buf.Tail()
	require.Equal(t, all[1:], gotTail)

	buf.DropBackN(3)
	require.Equal(t, 6, buf.Len())
	require.Equal(t, 10, buf.Written())
	gotTail = buf.Tail()
	require.Equal(t, all[4:], gotTail)

	buf.DropBackN(10)
	require.Equal(t, 0, buf.Len())
	require.Equal(t, 10, buf.Written())
	require.Empty(t, buf.Tail())
}

func TestPopBack_PopBackN_Equivalence(t *testing.T) {
	all := []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
	buf1 := tailbuf.New[string](10)
	buf2 := tailbuf.New[string](10)

	tailbuf.RequireEqualInternalState(t, buf1, buf2)

	buf1.WriteAll(all...)
	buf2.WriteAll(all...)

	tailbuf.RequireEqualInternalState(t, buf1, buf2)
	tail1 := buf1.Tail()
	tail2 := buf2.Tail()

	require.Equal(t, tail1, tail2)

	buf1.PopBackN(5)
	for i := 0; i < 5; i++ {
		buf2.PopBack()
	}

	tailbuf.RequireEqualInternalState(t, buf1, buf2)
	require.Equal(t, tail1, tail2)

	require.Equal(t, buf1.Tail(), buf2.Tail())
}

func requireZeroInternalWindow[T any](tb testing.TB, buf *tailbuf.Buf[T]) {
	tb.Helper()
	window := tailbuf.InternalWindow(buf)
	for i := range window {
		require.Zero(tb, window[i])
	}
}
```

