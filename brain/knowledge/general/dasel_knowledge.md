---
id: dasel-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:16.446536
---

# KNOWLEDGE EXTRACT: dasel
> **Extracted on:** 2026-03-30 17:35:42
> **Source:** dasel

---

## File: `.gitignore`
```
.idea/
dasel
```

## File: `.golangci.yaml`
```yaml
version: "2"
linters:
  default: standard
run:
  timeout: 2m
```

## File: `.pre-commit-hooks.yaml`
```yaml
- id: dasel-validate-docker
  name: Validate JSON, YAML, XML, TOML files
  description: Validate JSON files
  language: docker_image
  types_or:
    - json
    - yaml
    - xml
    - toml
  entry: ghcr.io/tomwright/dasel
  args:
    - validate

- id: dasel-validate-bin
  name: Validate JSON, YAML, XML, TOML
  description: Validate JSON, YAML, XML, TOML files
  language: system
  types_or:
    - json
    - yaml
    - xml
    - toml
  entry: dasel
  args:
    - validate

- id: dasel-validate
  name: Validate JSON, YAML, XML, TOML
  description: Validate JSON, YAML, XML, TOML files
  language: golang
  types_or:
    - json
    - yaml
    - xml
    - toml
  entry: dasel
  args:
    - validate
```

## File: `api.go`
```go
// Package dasel contains everything you'll need to use dasel from a go application.
package dasel

import (
	"context"
	"github.com/tomwright/dasel/v3/execution"
	"github.com/tomwright/dasel/v3/model"
)

// Query queries the data using the selector and returns the results.
func Query(ctx context.Context, data any, selector string, opts ...execution.ExecuteOptionFn) ([]*model.Value, int, error) {
	options := execution.NewOptions(opts...)
	val := model.NewValue(data)
	out, err := execution.ExecuteSelector(ctx, selector, val, options)
	if err != nil {
		return nil, 0, err
	}

	if out.IsBranch() || out.IsSpread() {
		res := make([]*model.Value, 0)
		if err := out.RangeSlice(func(i int, v *model.Value) error {
			res = append(res, v)
			return nil
		}); err != nil {
			return nil, 0, err
		}
		return res, len(res), nil
	}

	return []*model.Value{out}, 1, nil
}

// Select queries the data using the selector and returns the results as native Go types.
// Ordering within maps is not guaranteed.
func Select(ctx context.Context, data any, selector string, opts ...execution.ExecuteOptionFn) (any, int, error) {
	res, count, err := Query(ctx, data, selector, opts...)
	if err != nil {
		return nil, 0, err
	}
	out := make([]any, 0)
	for _, v := range res {
		goValue, err := v.GoValue()
		if err != nil {
			return nil, 0, err
		}
		out = append(out, goValue)
	}
	return out, count, err
}

// Modify runs the query against the given data and updates it in-place.
// Given data must be a pointer to a mutable data structure.
func Modify(ctx context.Context, data any, selector string, newValue any, opts ...execution.ExecuteOptionFn) (int, error) {
	res, count, err := Query(ctx, data, selector, opts...)
	if err != nil {
		return 0, err
	}
	for _, v := range res {
		if err := v.Set(model.NewValue(newValue)); err != nil {
			return 0, err
		}
	}
	return count, nil
}
```

## File: `api_example_test.go`
```go
package dasel_test

import (
	"context"
	"fmt"
	"github.com/tomwright/dasel/v3"
	"github.com/tomwright/dasel/v3/execution"
)

func ExampleSelect() {
	myData := map[string]any{
		"users": []map[string]any{
			{"name": "Alice", "age": 30},
			{"name": "Bob", "age": 25},
			{"name": "Tom", "age": 40},
		},
	}
	query := `users.filter(age > 27).map(name)...`
	selectResult, numResults, err := dasel.Select(context.Background(), myData, query, execution.WithUnstable())
	if err != nil {
		panic(err)
	}
	fmt.Printf("Found %d results:\n", numResults)

	// You should validate the type assertion in real code.
	selectResults := selectResult.([]any)

	// Results can be of various types, handle accordingly.
	for _, result := range selectResults {
		fmt.Println(result)
	}

	// Output:
	// Found 2 results:
	// Alice
	// Tom
}
```

## File: `api_test.go`
```go
package dasel_test

import (
	"testing"

	"github.com/google/go-cmp/cmp"
	"github.com/tomwright/dasel/v3"
)

type modifyTestCase struct {
	selector string
	in       any
	value    any
	exp      any
	count    int
}

func (tc modifyTestCase) run(t *testing.T) {
	count, err := dasel.Modify(t.Context(), &tc.in, tc.selector, tc.value)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if count != tc.count {
		t.Errorf("unexpected count: %d", count)
	}
	if !cmp.Equal(tc.exp, tc.in) {
		t.Errorf("unexpected result: %s", cmp.Diff(tc.exp, tc.in))
	}
}

func TestQuery(t *testing.T) {
	t.Run("basic query", func(t *testing.T) {
		inputData := map[string]any{
			"users": []map[string]any{
				{"name": "Alice", "age": 30},
				{"name": "Bob", "age": 25},
			},
		}
		results, count, err := dasel.Query(t.Context(), inputData, "users.map(name)...")
		if err != nil {
			t.Fatalf("unexpected error: %v", err)
		}
		if count != 2 {
			t.Errorf("unexpected count: %d", count)
		}
		exp := []string{"Alice", "Bob"}
		for i, r := range results {
			strVal, err := r.StringValue()
			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if strVal != exp[i] {
				t.Errorf("unexpected result at index %d: %s", i, strVal)
			}
		}
	})
}

func TestSelect(t *testing.T) {
	t.Run("basic select", func(t *testing.T) {
		inputData := map[string]any{
			"users": []map[string]any{
				{"name": "Alice", "age": 30},
				{"name": "Bob", "age": 25},
			},
		}
		result, count, err := dasel.Select(t.Context(), inputData, "users.map(name)...")
		if err != nil {
			t.Fatalf("unexpected error: %v", err)
		}
		if count != 2 {
			t.Errorf("unexpected count: %d", count)
		}
		exp := []any{"Alice", "Bob"}
		if !cmp.Equal(exp, result) {
			t.Errorf("unexpected result: %s", cmp.Diff(exp, result))
		}
	})
}

func TestModify(t *testing.T) {
	t.Run("index", func(t *testing.T) {
		t.Run("int over int", modifyTestCase{
			selector: "$this[1]",
			in:       []int{1, 2, 3},
			value:    4,
			exp:      []int{1, 4, 3},
			count:    1,
		}.run)
		t.Run("string over int", modifyTestCase{
			selector: "$this[1]",
			in:       []any{1, 2, 3},
			value:    "4",
			exp:      []any{1, "4", 3},
			count:    1,
		}.run)
	})
}
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- Fixed a bug that caused the `get` function to return `false` instead of an error when doing an invalid lookup.
- Fixed an issue with reading/writing null values in YAML.
- Fixed a nil pointer dereference when reading/writing null YAML documents.

## [v3.3.1] - 2026-02-26

### Fixed

- Fixed query selector parsing issue that incorrectly parsed array accessors when they followed a `filter` or `map` call.

## [v3.3.0] - 2026-02-25

### Added
- `replace` function to replace occurrences of a substring in a string with another string. [See docs](https://daseldocs.tomwright.me/functions/replace).

## [v3.2.3] - 2026-02-23

### Added
- XML parser now preserves comments and processing instructions during round-trip (#175).

### Fixed
- Spread operator within array construction is now honoured.

## [v3.2.2] - 2026-02-13

### Changed
- Swapped to use goccy/go-json for improved performance. Thanks @imix
- Updated model `IsScalar` internals to improve efficiency. Thanks @imix
- General dependency updates.

### Fixed
- TOML parser sub table parsing. Thanks @pmeier

## [v3.2.1] - 2026-01-05

### Fixed
- XML parser now correctly handles empty CDATA.

## [v3.2.0] - 2025-12-26

### Added
- `join` function to join array elements into a single string with a specified separator. [See docs](https://daseldocs.tomwright.me/functions/join).

## [v3.1.4] - 2025-12-18

### Fixed
- `Select` func in the exposed go API now correctly maps return values to the respective types.

## [v3.1.3] - 2025-12-18

### Fixed
- XML documents no longer create redundant `root` or `item` elements.
- Dasel no longer loses value metadata when reading/writing to internal models.

## [v3.1.2] - 2025-12-17

### Fixed

- Fix XML reading/writing when XML processing instructions are present.

## [v3.1.1] - 2025-12-16

### Fixed

- Homebrew release.

## [v3.1.0] - 2025-12-16

### Added
- `sum` function to sum numeric values in an array. [See docs](https://daseldocs.tomwright.me/functions/sum).

## [v3.0.0] - 2025-12-15

### Added
- Major new version release.
- INI support.
- HCL support.
- Dasel syntax now supports variables and expressions.
- Files can now be read and parsed inside a dasel query.
- Variables can now be passed to dasel from the command line.
- Support for comments in queries.
- Dasel config file to define default file format.
- Interactive mode for dasel CLI (alpha).

### Changed
- Go module path changed to `github.com/tomwright/dasel/v3`.
- Internal changes to support new version.
- Query/selector syntax revamp. See [docs](https://daseldocs.tomwright.me) for more information.
- Majority of read/write operations will now maintain ordering.
- Migrated from Cobra to Kong for CLI parsing/processing.
- Removed `put` and `delete` commands. Instead, modify within the query and use `--root` flag.

### Fixed
- File redirect now works in the same way as piped input.
- Various other bug fixes and improvements.
- Whitespace in query syntax is now handled correctly.

## [v2.8.1] - 2024-06-30

### Fixed
- Fixed a bug related to yaml aliases.

## [v2.8.0] - 2024-06-28

### Fixed

- Fixed a bug that could cause a panic.
- `type()` now returns `null` instead of `unknown` for null values.
- Added YAML support for merge tag/aliases. Thanks to [pmeier](https://github.com/pmeier). [Issue 285](https://github.com/TomWright/dasel/issues/285).

## [v2.7.0] - 2024-03-14

### Added

- `null()` function. [See docs](https://daseldocs.tomwright.me/functions/null)

### Fixed

- Dasel now correctly handles `null` values.

## [v2.6.0] - 2024-02-15

### Added

- Support for `--indent` flag.
- More descriptive errors when dasel fails to open a file.

### Changed

- Docker build improvements in workflows.

## [v2.5.0] - 2023-11-28

### Added

- Add `man` that generates manpages for all dasel subcommands.

### Fixed

- Fixed an issue when [parsing empty input documents](https://github.com/TomWright/dasel/issues/374).

## [v2.4.1] - 2023-10-18

### Fixed

- JSON output now acts as expected regarding the EscapeHTML flag.

## [v2.4.0] - 2023-10-18

### Added

- `orDefault()` function. [See docs](https://daseldocs.tomwright.me/functions/ordefault)
- `--csv-comma` flag to change the csv separator.
- `--csv-write-comma` flag to change the csv separator specifically for writes.
- `--csv-comment` flag to change the csv comment character.
- `--csv-crlf` flag to enable or disable CRLF output when working with csv files.

### Fixed

- Resolved an issue with YAML parser that was causing strings to be read as booleans.
- Fix a parsing issue with CSV types that forced you to expand and merge in order for it selects to work [Issue 364](https://github.com/TomWright/dasel/issues/364).

## [v2.3.6] - 2023-08-30

### Fixed

- XML is now formatted correctly. (https://github.com/TomWright/dasel/issues/354)

## [v2.3.5] - 2023-08-29

### Changed

- Small internal optimisation (https://github.com/TomWright/dasel/pull/341)
- Update to go 1.21
- Upgrade dependencies

### Fixed

- Resolved an issue with YAML parser that was causing strings to be read as numbers.
- Timestamps can now be resolved as expected in YAML.

## [v2.3.4] - 2023-06-01

### Fixed

- `len` function now works with new map type.
- `keys` function now works with new map type.

## [v2.3.3] - 2023-05-31

### Fixed

- Errors when selecting data are now correctly handled.

## [v2.3.2] - 2023-05-31

### Fixed

- Restored previous octal, binary and hex number parsing support in YAML and `put` command.

## [v2.3.1] - 2023-05-29

### Fixed

- `version` command now outputs correct version information (only affected v2 onwards)

## [v2.3.0] - 2023-05-29

### Changed

- Maps are now ordered internally.
- JSON and YAML maps maintain ordering on read/write.
- `all()` func now works with strings.
- `index()` func now works with strings.

### Fixed

- Multi-document output should now be displayed correctly.
- Index shorthand selector now works with multiple indexes.
- Null values are now correctly handled.

## [v2.2.0] - 2023-04-17

### Added

- `keys()` function.

## [v2.1.2] - 2023-03-27

### Added

- Join function.
- String function.

### Fixed

- Null error caused by null values in arrays. See [PR 307](https://github.com/TomWright/dasel/pull/307).

## [v2.1.1] - 2023-01-19

### Fixed

- Changed go module to `github.com/tomwright/dasel/v3` to ensure it works correctly with go modules.

## [v2.1.0] - 2023-01-11

### Added

- Ability to jump to a parent x levels up with `parent(x)`. Defaults to 1 level.

## [v2.0.2] - 2022-12-07

### Fixed

- Argument parsing issue that caused files to be written to the wrong place. See [discussion 268](https://github.com/TomWright/dasel/discussions/268).

## [v2.0.1] - 2022-12-07

### Added

- `float` type in `put` command.

### Fixed

- Output values are now correctly de-referenced. This fixed issues with encoded values not appearing correctly.
- Escape characters in selector strings now work as expected.

## [v2.0.0] - 2022-12-02

See [documentation](https://daseldocs.tomwright.me) for all changes.

- Selector syntax

## [v1.27.3] - 2022-10-18

### Fixed

- The compact flag now works with the XML parser.

## [v1.27.2] - 2022-10-18

### Fixed

- Help text for select and delete commands now contain all available parsers.
- Errors now implement the `Is` interface so they are easier to use from go.
- Floats are now formatted in decimal format instead of scientific notification when writing to CSV ([Issue 245](https://github.com/TomWright/dasel/issues/245), [Issue 229](https://github.com/TomWright/dasel/issues/229))

## [v1.27.1] - 2022-09-28

### Fixed

- Improved selector comparison parsing to allow matching on values containing special characters.

## [v1.27.0] - 2022-09-26

### Added

- New `value-file` flag allows you to `put` values read from a file ([Issue 246](https://github.com/TomWright/dasel/issues/246))

## [v1.26.1] - 2022-08-24

### Fixed

- Make the completion command available for use ([Issue 216](https://github.com/TomWright/dasel/issues/216))
- Make the `__complete` command available for use

## [v1.26.0] - 2022-07-09

### Added

- Search optional selector - `(#:key=value)`

## [v1.25.1] - 2022-06-29

### Added

- Pre-commit hooks for validate command.

## [v1.25.0] - 2022-06-26

### Added

- Support for struct type usage in go package.
- Validate command.

## [v1.24.3] - 2022-04-23

### Added

- Gzip compressed binaries on releases.

## [v1.24.2] - 2022-04-22

### Fixed

- Update a package to avoid a High Vulnerability in golang.org/x/crypto with CVE ID [CVE-2022-27191](https://github.com/advisories/GHSA-8c26-wmh5-6g9v)

## [v1.24.1] - 2022-03-28

### Changed

- `storage` package has been moved outside the `internal` package.

### Fixed

- New funcs added in `v1.24.0` can now be used as expected since you can now access the `storage.ReadWriteOption`.

## [v1.24.0] - 2022-03-18

### Added

- `Node.NewFromFile` func to load a root node from a file.
- `Node.NewFromReader` func to load a root node from an `io.Reader`.
- `Node.WriteToFile` func to write results to a file.
- `Node.Write` func to write results to an `io.Writer`.

## [v1.23.0] - 2022-03-10

### Fixed

- Update github.com/pelletier/go-toml to consume fix for https://github.com/TomWright/dasel/issues/191.

### Added

- Sprig functions to output formatter template.

## [v1.22.1] - 2021-11-09

### Fixed

- Cleaned up error output

## [v1.22.0] - 2021-11-09

### Added

- Type selector `[@]`.

### Fixed

- Errors are now written to stderr as expected.

## [v1.21.2] - 2021-10-21

### Added

- Linux arm32 build target.

## [v1.21.1] - 2021-09-30

### Changed
- `--escape-html` flag now defaults to false.

## [v1.21.0] - 2021-09-29

### Added
- `--escape-html` flag.

### Fixed
- `put document` and `put object` are now aware of the `--merge-input-documents` flag.

## [v1.20.1] - 2021-09-28

### Added

- `buster-slim` and `alpine` tags to built docker images.

### Fixed

- Different encodings in XML files are now [handled as expected](https://github.com/TomWright/dasel/issues/164).

## [v1.20.0] - 2021-08-30

### Added

- `-v`, `--value` flag to workaround [dash issue](https://github.com/TomWright/dasel/issues/117).

### Fixed

- Fixed an issue in which unicode characters could cause issues when parsing selectors.

## [v1.19.0] - 2021-08-14

### Added

- `--colour`,`--color` flag to enable colourised output in select command.

## [v1.18.0] - 2021-08-11

### Added

- `--format` flag to `select` command.

## [v1.17.0] - 2021-08-08

### Added

- Support for `!=` comparison operator in dynamic and search selectors.
- Support for `-`/`keyValue` key in dynamic selectors.

## [v1.16.1] - 2021-08-02

### Fixed

- Fixed a bug that stopped the delete command editing files in place.

## [v1.16.0] - 2021-08-01

### Added

- Delete command.

## [v1.15.0] - 2021-05-06

### Added

- `--merge-input-documents` flag.

### Changed

- Optional `noupdater` build tag to disable the self-update command.

### Fixed

- Empty XML documents are now parsed correctly.
  - https://github.com/TomWright/dasel/issues/131

## [v1.14.1] - 2021-04-15

### Added

- arm64 build support.

## [v1.14.0] - 2021-04-11

### Added

- `.[#]` length selector.
- `>` comparison operator.
- `>=` comparison operator.
- `<` comparison operator.
- `<=` comparison operator.

## [v1.13.6] - 2021-03-29

### Changed

- Development versions of dasel will now include more specific version information where possible.

### Fixed

- Fix an issue that stopped dasel being able to output CSV documents when parsed from JSON.

## [v1.13.5] - 2021-03-22

### Fixed

- Empty map values are now initialised as `map[string]interface{}` rather than `map[interface{}]interface{}`.

## [v1.13.4] - 2021-03-11

### Fixed

- Empty document input is now treated different in select and put commands.
  - https://github.com/TomWright/dasel/issues/99
  - https://github.com/TomWright/dasel/issues/102

## [v1.13.3] - 2021-03-05

### Fixed

- Blank YAML and CSV input is now treated as an empty document.

### Changed

- Blank JSON input is now treated as an empty document.

## [v1.13.2] - 2021-02-25

### Changed

- Improved information provided in `UnsupportedTypeForSelector` errors.
- Upgrade to go 1.16.

### Fixed

- Make sure the `-n`,`--null` flag has an effect in multi-select queries.

## [v1.13.1] - 2021-02-18

### Fixed

- Added `CGO_ENABLED=0` build flag to ensure linux_amd64 builds are statically linked.

## [v1.13.0] - 2021-02-11

### Added

- `--length` flag to select command.

## [v1.12.2] - 2021-01-05

### Fixed

- Fix a bug that stopped the write parser being properly detected when writing to the input file.

## [v1.12.1] - 2021-01-05

### Changed

- Build workflows now updated to run on ubuntu-latest and use a matrix to build assets for `linux`, `darwin` and
  `windows` for both `amd64` and `386`.

### Fixed

- Release asset for macos/darwin is now named `dasel_darwin_amd64` instead of `dasel_macos_amd64`.
- Self-updater now identifies `dev` version as development.

## [v1.12.0] - 2021-01-02

### Added

- Add `-c`, `--compact` flag to remove pretty-print formatting from JSON output.
- Defined `storage.IndentOption(indent string) ReadWriteOption`.
- Defined `storage.PrettyPrintOption(enabled bool) ReadWriteOption`.

### Changed

- Changed `storage.Parser` funcs to allow the passing of `...ReadWriteOption`.

## [v1.11.0] - 2020-12-22

### Added

- Benchmark info now contains graphs.
- `update` command to self-update dasel.

### Changed

- Benchmark info now directly compares dasel, jq and yq.

## [v1.10.0] - 2020-12-19

### Added

- Add `dasel put document` command.
- Benchmark information.

### Fixed

- `-r`,`--read` and `-w`,`--write` flags are now used in `dasel put object`.
- Fix issues that occurred when writing to the root node.

### Changed

- Command names and descriptions.

## [v1.9.1] - 2020-12-12

### Fixed

- Stopped parsing XML entities in strings.

## [v1.9.0] - 2020-12-12

### Added

- Add keys/index selector in multi queries.
- Add `-n`,`--null` flag.

## [v1.8.0] - 2020-12-01

### Added

- Add ability to use `ANY_INDEX` (`[*]`) and `DYNAMIC` (`(x=y)`) selectors on maps/objects.

## [v1.7.0] - 2020-11-30

### Added

- Add `-r`,`--read` and `-w`,`--write` flags to specifically choose input/output parsers. This allows you to convert data between formats.

## [v1.6.2] - 2020-11-18

### Added

- Add support for multi-document JSON files.

## [v1.6.1] - 2020-11-17

### Changed

- Remove some validation on `dasel put object` to allow you to put empty objects.

## [v1.6.0] - 2020-11-17

### Added

- Add search selector to allow recursive searching from the current node.

## [v1.5.1] - 2020-11-14

### Fixed

- Fixed an issue that stopped new values being saved.

## [v1.5.0] - 2020-11-12

### Added

- Add ability to use `\` as an escape character in selectors.

## [v1.4.1] - 2020-11-11

### Fixed

- Fix an issue when parsing dynamic selectors.

## [v1.4.0] - 2020-11-08

### Added

- Add `-m`,`--multiple` flag to deal with multi-value queries.
- Add `ANY_INDEX` or `[*]` selector.
- Add `NextMultiple` property to the `Node` struct - this is used when processing multi-value queries.
- Add `Node.QueryMultiple` func.
- Add `Node.PutMultiple` func.

## [v1.3.0] - 2020-11-08

### Added

- Add support for CSV files.

## [v1.2.0] - 2020-11-07

### Added

- Add support for multi-document YAML files.
- Add CodeQL step in github actions.

### Changed

- Docker image is now pushed to ghcr instead of github packages.

## [v1.1.0] - 2020-11-01

### Added

- Add sub-selector support in dynamic selectors.

## [v1.0.4] - 2020-10-30

### Added

- Add `--plain` flag to tell dasel to output un-formatted values.

## [v1.0.3] - 2020-10-29

### Changed

- Command output is now followed by a newline.

## [v1.0.2] - 2020-10-28

### Added

- Docker image is now built and pushed when a new release is tagged.

## [v1.0.1] - 2020-10-28

### Added

- Add support for XML.

### Changed

- Add `-` as an alias for `stdin`/`stdout` in `--file` and `--output` flags.
- Selector can now be given as the first argument making the flag itself optional.
- `select` is now the default command.

## [v1.0.0] - 2020-10-27

### Added

- Add lots of tests.
- Add docs.
- Got accepted to go-awesome.

## [v0.0.5] - 2020-09-27

### Added

- Add support for TOML.

## [v0.0.4] - 2020-09-27

### Added

- Ability to check against the node value in a dynamic selector.
- Code coverage.

### Changed

- Use reflection instead of fixed type checks.

## [v0.0.3] - 2020-09-24

### Changed

- Use reflection instead of fixed type checks.
- Extract commands into their own functions to make them testable.

## [v0.0.2] - 2020-09-23

### Added

- Add ability to pipe data in/out of dasel.
- Add dasel put command.

## [v0.0.1] - 2020-09-22

### Added

- Everything!

[unreleased]: https://github.com/TomWright/dasel/compare/v3.3.1...HEAD
[v3.3.1]: https://github.com/TomWright/dasel/compare/v3.3.0...v3.3.1
[v3.3.0]: https://github.com/TomWright/dasel/compare/v3.2.3...v3.3.0
[v3.2.3]: https://github.com/TomWright/dasel/compare/v3.2.2...v3.2.3
[v3.2.2]: https://github.com/TomWright/dasel/compare/v3.2.1...v3.2.2
[v3.2.1]: https://github.com/TomWright/dasel/compare/v3.2.0...v3.2.1
[v3.2.0]: https://github.com/TomWright/dasel/compare/v3.1.4...v3.2.0
[v3.1.4]: https://github.com/TomWright/dasel/compare/v3.1.3...v3.1.4
[v3.1.3]: https://github.com/TomWright/dasel/compare/v3.1.2...v3.1.3
[v3.1.2]: https://github.com/TomWright/dasel/compare/v3.1.1...v3.1.2
[v3.1.1]: https://github.com/TomWright/dasel/compare/v3.1.0...v3.1.1
[v3.1.0]: https://github.com/TomWright/dasel/compare/v3.0.0...v3.1.0
[v3.0.0]: https://github.com/TomWright/dasel/compare/v2.8.1...v3.0.0
[v2.8.1]: https://github.com/TomWright/dasel/compare/v2.8.0...v2.8.1
[v2.8.0]: https://github.com/TomWright/dasel/compare/v2.7.0...v2.8.0
[v2.7.0]: https://github.com/TomWright/dasel/compare/v2.6.0...v2.7.0
[v2.6.0]: https://github.com/TomWright/dasel/compare/v2.5.0...v2.6.0
[v2.5.0]: https://github.com/TomWright/dasel/compare/v2.4.1...v2.5.0
[v2.4.1]: https://github.com/TomWright/dasel/compare/v2.4.0...v2.4.1
[v2.4.0]: https://github.com/TomWright/dasel/compare/v2.3.6...v2.4.0
[v2.3.6]: https://github.com/TomWright/dasel/compare/v2.3.5...v2.3.6
[v2.3.5]: https://github.com/TomWright/dasel/compare/v2.3.4...v2.3.5
[v2.3.4]: https://github.com/TomWright/dasel/compare/v2.3.3...v2.3.4
[v2.3.3]: https://github.com/TomWright/dasel/compare/v2.3.2...v2.3.3
[v2.3.2]: https://github.com/TomWright/dasel/compare/v2.3.1...v2.3.2
[v2.3.1]: https://github.com/TomWright/dasel/compare/v2.3.0...v2.3.1
[v2.3.0]: https://github.com/TomWright/dasel/compare/v2.2.0...v2.3.0
[v2.2.0]: https://github.com/TomWright/dasel/compare/v2.1.2...v2.2.0
[v2.1.2]: https://github.com/TomWright/dasel/compare/v2.1.1...v2.1.2
[v2.1.1]: https://github.com/TomWright/dasel/compare/v2.1.0...v2.1.1
[v2.1.0]: https://github.com/TomWright/dasel/compare/v2.0.2...v2.1.0
[v2.0.2]: https://github.com/TomWright/dasel/compare/v2.0.1...v2.0.2
[v2.0.1]: https://github.com/TomWright/dasel/compare/v2.0.0...v2.0.1
[v2.0.0]: https://github.com/TomWright/dasel/compare/v1.27.3...v2.0.0
[v1.27.3]: https://github.com/TomWright/dasel/compare/v1.27.2...v1.27.3
[v1.27.2]: https://github.com/TomWright/dasel/compare/v1.27.1...v1.27.2
[v1.27.1]: https://github.com/TomWright/dasel/compare/v1.27.0...v1.27.1
[v1.27.0]: https://github.com/TomWright/dasel/compare/v1.26.1...v1.27.0
[v1.26.1]: https://github.com/TomWright/dasel/compare/v1.26.0...v1.26.1
[v1.26.0]: https://github.com/TomWright/dasel/compare/v1.25.1...v1.26.0
[v1.25.1]: https://github.com/TomWright/dasel/compare/v1.25.0...v1.25.1
[v1.25.0]: https://github.com/TomWright/dasel/compare/v1.24.3...v1.25.0
[v1.24.3]: https://github.com/TomWright/dasel/compare/v1.24.2...v1.24.3
[v1.24.2]: https://github.com/TomWright/dasel/compare/v1.24.1...v1.24.2
[v1.24.1]: https://github.com/TomWright/dasel/compare/v1.24.0...v1.24.1
[v1.24.0]: https://github.com/TomWright/dasel/compare/v1.23.0...v1.24.0
[v1.23.0]: https://github.com/TomWright/dasel/compare/v1.22.1...v1.23.0
[v1.22.1]: https://github.com/TomWright/dasel/compare/v1.22.0...v1.22.1
[v1.22.0]: https://github.com/TomWright/dasel/compare/v1.21.2...v1.22.0
[v1.21.2]: https://github.com/TomWright/dasel/compare/v1.21.1...v1.21.2
[v1.21.1]: https://github.com/TomWright/dasel/compare/v1.21.0...v1.21.1
[v1.21.0]: https://github.com/TomWright/dasel/compare/v1.20.1...v1.21.0
[v1.20.1]: https://github.com/TomWright/dasel/compare/v1.20.0...v1.20.1
[v1.20.0]: https://github.com/TomWright/dasel/compare/v1.19.0...v1.20.0
[v1.19.0]: https://github.com/TomWright/dasel/compare/v1.18.0...v1.19.0
[v1.18.0]: https://github.com/TomWright/dasel/compare/v1.17.0...v1.18.0
[v1.17.0]: https://github.com/TomWright/dasel/compare/v1.16.1...v1.17.0
[v1.16.1]: https://github.com/TomWright/dasel/compare/v1.16.0...v1.16.1
[v1.16.0]: https://github.com/TomWright/dasel/compare/v1.15.0...v1.16.0
[v1.15.0]: https://github.com/TomWright/dasel/compare/v1.14.1...v1.15.0
[v1.14.1]: https://github.com/TomWright/dasel/compare/v1.14.0...v1.14.1
[v1.14.0]: https://github.com/TomWright/dasel/compare/v1.13.6...v1.14.0
[v1.13.6]: https://github.com/TomWright/dasel/compare/v1.13.5...v1.13.6
[v1.13.5]: https://github.com/TomWright/dasel/compare/v1.13.4...v1.13.5
[v1.13.4]: https://github.com/TomWright/dasel/compare/v1.13.3...v1.13.4
[v1.13.3]: https://github.com/TomWright/dasel/compare/v1.13.2...v1.13.3
[v1.13.2]: https://github.com/TomWright/dasel/compare/v1.13.1...v1.13.2
[v1.13.1]: https://github.com/TomWright/dasel/compare/v1.13.0...v1.13.1
[v1.13.0]: https://github.com/TomWright/dasel/compare/v1.12.2...v1.13.0
[v1.12.2]: https://github.com/TomWright/dasel/compare/v1.12.1...v1.12.2
[v1.12.1]: https://github.com/TomWright/dasel/compare/v1.12.0...v1.12.1
[v1.12.0]: https://github.com/TomWright/dasel/compare/v1.11.0...v1.12.0
[v1.11.0]: https://github.com/TomWright/dasel/compare/v1.10.0...v1.11.0
[v1.10.0]: https://github.com/TomWright/dasel/compare/v1.9.1...v1.10.0
[v1.9.1]: https://github.com/TomWright/dasel/compare/v1.9.0...v1.9.1
[v1.9.0]: https://github.com/TomWright/dasel/compare/v1.8.0...v1.9.0
[v1.8.0]: https://github.com/TomWright/dasel/compare/v1.7.0...v1.8.0
[v1.7.0]: https://github.com/TomWright/dasel/compare/v1.6.2...v1.7.0
[v1.6.2]: https://github.com/TomWright/dasel/compare/v1.6.1...v1.6.2
[v1.6.1]: https://github.com/TomWright/dasel/compare/v1.6.0...v1.6.1
[v1.6.0]: https://github.com/TomWright/dasel/compare/v1.5.1...v1.6.0
[v1.5.1]: https://github.com/TomWright/dasel/compare/v1.5.0...v1.5.1
[v1.5.0]: https://github.com/TomWright/dasel/compare/v1.4.1...v1.5.0
[v1.4.1]: https://github.com/TomWright/dasel/compare/v1.4.0...v1.4.1
[v1.4.0]: https://github.com/TomWright/dasel/compare/v1.3.0...v1.4.0
[v1.3.0]: https://github.com/TomWright/dasel/compare/v1.2.0...v1.3.0
[v1.1.0]: https://github.com/TomWright/dasel/compare/v1.0.4...v1.1.0
[v1.0.4]: https://github.com/TomWright/dasel/compare/v1.0.3...v1.0.4
[v1.0.3]: https://github.com/TomWright/dasel/compare/v1.0.2...v1.0.3
[v1.0.2]: https://github.com/TomWright/dasel/compare/v1.0.1...v1.0.2
[v1.0.1]: https://github.com/TomWright/dasel/compare/v1.0.0...v1.0.1
[v1.0.0]: https://github.com/TomWright/dasel/compare/v0.0.5...v1.0.0
[v0.0.5]: https://github.com/TomWright/dasel/compare/v0.0.4...v0.0.5
[v0.0.4]: https://github.com/TomWright/dasel/compare/v0.0.3...v0.0.4
[v0.0.3]: https://github.com/TomWright/dasel/compare/v0.0.2...v0.0.3
[v0.0.2]: https://github.com/TomWright/dasel/compare/v0.0.1...v0.0.2
[v0.0.1]: https://github.com/TomWright/dasel/releases/tag/v0.0.1
```

## File: `codecov.yaml`
```yaml
comment: no # do not comment PR with the result

coverage:
  range: 50..90 # coverage lower than 50 is red, higher than 90 green, between color code

  status:
    project: # settings affecting project coverage
      default:
        target: auto # auto % coverage target
        threshold: 5%  # allow for 5% reduction of coverage without failing

    # do not run coverage on patch nor changes
    patch: false
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or
  advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic
  address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at contact@tomwright.me. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Dasel

Thank you for considering contributing to Dasel! Contributions of all kinds are welcome — whether it's fixing bugs, improving documentation, or adding new features.

## How to Contribute

### 1. Reporting Issues

* Check the [issue tracker](https://github.com/TomWright/dasel/issues) to see if your issue has already been reported.
* If not, open a new issue with a clear description. Please include:

    * Steps to reproduce (if it's a bug)
    * Expected vs actual behavior
    * Versions of Dasel, Go, and your OS

### 2. Suggesting Features

* Open a [discussion](https://github.com/TomWright/dasel/discussions) if you'd like feedback before implementing.
* If the idea is well-defined, create an issue describing the use case and possible syntax.

### 3. Submitting Pull Requests

1. Fork the repository and clone your fork.
2. Create a new branch for your work:

   ```bash
   git checkout -b feature/my-new-feature
   ```
3. Make your changes and add tests if relevant.
4. Run the test suite to ensure nothing is broken:

   ```bash
   go test ./...
   ```
5. Commit your changes with a clear message:

   ```bash
   git commit -m "Add support for XYZ selector"
   ```
6. Push your branch and open a Pull Request.

### 4. Code Style

* Follow Go best practices and conventions.
* Keep code simple and readable.
* Add comments for complex logic.

### 5. Documentation

* Ensure documentation requirements are listed on your PR so docs site can be updated.
* Ensure examples are clear and consistent with the style of existing docs.

### 6. Communication

* Be respectful and constructive in discussions.
* Aim to keep contributions focused and incremental.

---

## Getting Help

If you have questions, feel free to:

* Start a [discussion](https://github.com/TomWright/dasel/discussions)
* Ask in an open issue related to your question

We appreciate your contribution and for helping improve Dasel!
```

## File: `Dockerfile`
```
ARG GOLANG_VERSION=1.25.0
ARG TARGET_BASE_IMAGE=debian:bookworm-slim
FROM golang:${GOLANG_VERSION} AS builder

ARG MAJOR_VERSION=v3
ARG RELEASE_VERSION=master
ARG CGO_ENABLED=0

COPY . .

RUN go build -o /dasel -ldflags="-w -s -X 'github.com/tomwright/dasel/${MAJOR_VERSION}/internal.Version=${RELEASE_VERSION}'" ./cmd/dasel

FROM ${TARGET_BASE_IMAGE}

COPY --from=builder --chmod=755 /dasel /usr/local/bin/dasel

ENTRYPOINT ["/usr/local/bin/dasel"]
CMD ["--help"]
```

## File: `go.mod`
```
module github.com/tomwright/dasel/v3

go 1.25

require (
	github.com/alecthomas/kong v1.14.0
	github.com/charmbracelet/bubbles v1.0.0
	github.com/charmbracelet/bubbletea v1.3.10
	github.com/charmbracelet/lipgloss v1.1.0
	github.com/goccy/go-json v0.10.5
	github.com/google/go-cmp v0.7.0
	github.com/hashicorp/hcl/v2 v2.24.0
	github.com/pelletier/go-toml/v2 v2.2.5-0.20250826075308-a0e846496753
	github.com/zclconf/go-cty v1.17.0
	go.yaml.in/yaml/v4 v4.0.0-rc.3
	gopkg.in/ini.v1 v1.67.0
)

require (
	github.com/agext/levenshtein v1.2.1 // indirect
	github.com/apparentlymart/go-textseg/v15 v15.0.0 // indirect
	github.com/atotto/clipboard v0.1.4 // indirect
	github.com/aymanbagabas/go-osc52/v2 v2.0.1 // indirect
	github.com/charmbracelet/colorprofile v0.4.1 // indirect
	github.com/charmbracelet/x/ansi v0.11.6 // indirect
	github.com/charmbracelet/x/cellbuf v0.0.15 // indirect
	github.com/charmbracelet/x/term v0.2.2 // indirect
	github.com/clipperhouse/displaywidth v0.9.0 // indirect
	github.com/clipperhouse/stringish v0.1.1 // indirect
	github.com/clipperhouse/uax29/v2 v2.5.0 // indirect
	github.com/erikgeiser/coninput v0.0.0-20211004153227-1c3628e74d0f // indirect
	github.com/lucasb-eyer/go-colorful v1.3.0 // indirect
	github.com/mattn/go-isatty v0.0.20 // indirect
	github.com/mattn/go-localereader v0.0.1 // indirect
	github.com/mattn/go-runewidth v0.0.19 // indirect
	github.com/mitchellh/go-wordwrap v1.0.1 // indirect
	github.com/muesli/ansi v0.0.0-20230316100256-276c6243b2f6 // indirect
	github.com/muesli/cancelreader v0.2.2 // indirect
	github.com/muesli/termenv v0.16.0 // indirect
	github.com/rivo/uniseg v0.4.7 // indirect
	github.com/stretchr/testify v1.11.1 // indirect
	github.com/xo/terminfo v0.0.0-20220910002029-abceb7e1c41e // indirect
	golang.org/x/mod v0.26.0 // indirect
	golang.org/x/sync v0.16.0 // indirect
	golang.org/x/sys v0.38.0 // indirect
	golang.org/x/text v0.28.0 // indirect
	golang.org/x/tools v0.35.0 // indirect
)
```

## File: `go.sum`
```
github.com/MakeNowJust/heredoc v1.0.0 h1:cXCdzVdstXyiTqTvfqk9SDHpKNjxuom+DOlyEeQ4pzQ=
github.com/MakeNowJust/heredoc v1.0.0/go.mod h1:mG5amYoWBHf8vpLOuehzbGGw0EHxpZZ6lCpQ4fNJ8LE=
github.com/agext/levenshtein v1.2.1 h1:QmvMAjj2aEICytGiWzmxoE0x2KZvE0fvmqMOfy2tjT8=
github.com/agext/levenshtein v1.2.1/go.mod h1:JEDfjyjHDjOF/1e4FlBE/PkbqA9OfWu2ki2W0IB5558=
github.com/alecthomas/assert/v2 v2.11.0 h1:2Q9r3ki8+JYXvGsDyBXwH3LcJ+WK5D0gc5E8vS6K3D0=
github.com/alecthomas/assert/v2 v2.11.0/go.mod h1:Bze95FyfUr7x34QZrjL+XP+0qgp/zg8yS+TtBj1WA3k=
github.com/alecthomas/kong v1.14.0 h1:gFgEUZWu2ZmZ+UhyZ1bDhuutbKN1nTtJTwh19Wsn21s=
github.com/alecthomas/kong v1.14.0/go.mod h1:wrlbXem1CWqUV5Vbmss5ISYhsVPkBb1Yo7YKJghju2I=
github.com/alecthomas/repr v0.5.2 h1:SU73FTI9D1P5UNtvseffFSGmdNci/O6RsqzeXJtP0Qs=
github.com/alecthomas/repr v0.5.2/go.mod h1:Fr0507jx4eOXV7AlPV6AVZLYrLIuIeSOWtW57eE/O/4=
github.com/apparentlymart/go-textseg/v15 v15.0.0 h1:uYvfpb3DyLSCGWnctWKGj857c6ew1u1fNQOlOtuGxQY=
github.com/apparentlymart/go-textseg/v15 v15.0.0/go.mod h1:K8XmNZdhEBkdlyDdvbmmsvpAG721bKi0joRfFdHIWJ4=
github.com/atotto/clipboard v0.1.4 h1:EH0zSVneZPSuFR11BlR9YppQTVDbh5+16AmcJi4g1z4=
github.com/atotto/clipboard v0.1.4/go.mod h1:ZY9tmq7sm5xIbd9bOK4onWV4S6X0u6GY7Vn0Yu86PYI=
github.com/aymanbagabas/go-osc52/v2 v2.0.1 h1:HwpRHbFMcZLEVr42D4p7XBqjyuxQH5SMiErDT4WkJ2k=
github.com/aymanbagabas/go-osc52/v2 v2.0.1/go.mod h1:uYgXzlJ7ZpABp8OJ+exZzJJhRNQ2ASbcXHWsFqH8hp8=
github.com/aymanbagabas/go-udiff v0.3.1 h1:LV+qyBQ2pqe0u42ZsUEtPiCaUoqgA9gYRDs3vj1nolY=
github.com/aymanbagabas/go-udiff v0.3.1/go.mod h1:G0fsKmG+P6ylD0r6N/KgQD/nWzgfnl8ZBcNLgcbrw8E=
github.com/charmbracelet/bubbles v1.0.0 h1:12J8/ak/uCZEMQ6KU7pcfwceyjLlWsDLAxB5fXonfvc=
github.com/charmbracelet/bubbles v1.0.0/go.mod h1:9d/Zd5GdnauMI5ivUIVisuEm3ave1XwXtD1ckyV6r3E=
github.com/charmbracelet/bubbletea v1.3.10 h1:otUDHWMMzQSB0Pkc87rm691KZ3SWa4KUlvF9nRvCICw=
github.com/charmbracelet/bubbletea v1.3.10/go.mod h1:ORQfo0fk8U+po9VaNvnV95UPWA1BitP1E0N6xJPlHr4=
github.com/charmbracelet/colorprofile v0.4.1 h1:a1lO03qTrSIRaK8c3JRxJDZOvhvIeSco3ej+ngLk1kk=
github.com/charmbracelet/colorprofile v0.4.1/go.mod h1:U1d9Dljmdf9DLegaJ0nGZNJvoXAhayhmidOdcBwAvKk=
github.com/charmbracelet/lipgloss v1.1.0 h1:vYXsiLHVkK7fp74RkV7b2kq9+zDLoEU4MZoFqR/noCY=
github.com/charmbracelet/lipgloss v1.1.0/go.mod h1:/6Q8FR2o+kj8rz4Dq0zQc3vYf7X+B0binUUBwA0aL30=
github.com/charmbracelet/x/ansi v0.11.6 h1:GhV21SiDz/45W9AnV2R61xZMRri5NlLnl6CVF7ihZW8=
github.com/charmbracelet/x/ansi v0.11.6/go.mod h1:2JNYLgQUsyqaiLovhU2Rv/pb8r6ydXKS3NIttu3VGZQ=
github.com/charmbracelet/x/cellbuf v0.0.15 h1:ur3pZy0o6z/R7EylET877CBxaiE1Sp1GMxoFPAIztPI=
github.com/charmbracelet/x/cellbuf v0.0.15/go.mod h1:J1YVbR7MUuEGIFPCaaZ96KDl5NoS0DAWkskup+mOY+Q=
github.com/charmbracelet/x/term v0.2.2 h1:xVRT/S2ZcKdhhOuSP4t5cLi5o+JxklsoEObBSgfgZRk=
github.com/charmbracelet/x/term v0.2.2/go.mod h1:kF8CY5RddLWrsgVwpw4kAa6TESp6EB5y3uxGLeCqzAI=
github.com/clipperhouse/displaywidth v0.9.0 h1:Qb4KOhYwRiN3viMv1v/3cTBlz3AcAZX3+y9OLhMtAtA=
github.com/clipperhouse/displaywidth v0.9.0/go.mod h1:aCAAqTlh4GIVkhQnJpbL0T/WfcrJXHcj8C0yjYcjOZA=
github.com/clipperhouse/stringish v0.1.1 h1:+NSqMOr3GR6k1FdRhhnXrLfztGzuG+VuFDfatpWHKCs=
github.com/clipperhouse/stringish v0.1.1/go.mod h1:v/WhFtE1q0ovMta2+m+UbpZ+2/HEXNWYXQgCt4hdOzA=
github.com/clipperhouse/uax29/v2 v2.5.0 h1:x7T0T4eTHDONxFJsL94uKNKPHrclyFI0lm7+w94cO8U=
github.com/clipperhouse/uax29/v2 v2.5.0/go.mod h1:Wn1g7MK6OoeDT0vL+Q0SQLDz/KpfsVRgg6W7ihQeh4g=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/erikgeiser/coninput v0.0.0-20211004153227-1c3628e74d0f h1:Y/CXytFA4m6baUTXGLOoWe4PQhGxaX0KpnayAqC48p4=
github.com/erikgeiser/coninput v0.0.0-20211004153227-1c3628e74d0f/go.mod h1:vw97MGsxSvLiUE2X8qFplwetxpGLQrlU1Q9AUEIzCaM=
github.com/go-test/deep v1.0.3 h1:ZrJSEWsXzPOxaZnFteGEfooLba+ju3FYIbOrS+rQd68=
github.com/go-test/deep v1.0.3/go.mod h1:wGDj63lr65AM2AQyKZd/NYHGb0R+1RLqB8NKt3aSFNA=
github.com/goccy/go-json v0.10.5 h1:Fq85nIqj+gXn/S5ahsiTlK3TmC85qgirsdTP/+DeaC4=
github.com/goccy/go-json v0.10.5/go.mod h1:oq7eo15ShAhp70Anwd5lgX2pLfOS3QCiwU/PULtXL6M=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
github.com/hashicorp/hcl/v2 v2.24.0 h1:2QJdZ454DSsYGoaE6QheQZjtKZSUs9Nh2izTWiwQxvE=
github.com/hashicorp/hcl/v2 v2.24.0/go.mod h1:oGoO1FIQYfn/AgyOhlg9qLC6/nOJPX3qGbkZpYAcqfM=
github.com/hexops/gotextdiff v1.0.3 h1:gitA9+qJrrTCsiCl7+kh75nPqQt1cx4ZkudSTLoUqJM=
github.com/hexops/gotextdiff v1.0.3/go.mod h1:pSWU5MAI3yDq+fZBTazCSJysOMbxWL1BSow5/V2vxeg=
github.com/lucasb-eyer/go-colorful v1.3.0 h1:2/yBRLdWBZKrf7gB40FoiKfAWYQ0lqNcbuQwVHXptag=
github.com/lucasb-eyer/go-colorful v1.3.0/go.mod h1:R4dSotOR9KMtayYi1e77YzuveK+i7ruzyGqttikkLy0=
github.com/mattn/go-isatty v0.0.20 h1:xfD0iDuEKnDkl03q4limB+vH+GxLEtL/jb4xVJSWWEY=
github.com/mattn/go-isatty v0.0.20/go.mod h1:W+V8PltTTMOvKvAeJH7IuucS94S2C6jfK/D7dTCTo3Y=
github.com/mattn/go-localereader v0.0.1 h1:ygSAOl7ZXTx4RdPYinUpg6W99U8jWvWi9Ye2JC/oIi4=
github.com/mattn/go-localereader v0.0.1/go.mod h1:8fBrzywKY7BI3czFoHkuzRoWE9C+EiG4R1k4Cjx5p88=
github.com/mattn/go-runewidth v0.0.19 h1:v++JhqYnZuu5jSKrk9RbgF5v4CGUjqRfBm05byFGLdw=
github.com/mattn/go-runewidth v0.0.19/go.mod h1:XBkDxAl56ILZc9knddidhrOlY5R/pDhgLpndooCuJAs=
github.com/mitchellh/go-wordwrap v1.0.1 h1:TLuKupo69TCn6TQSyGxwI1EblZZEsQ0vMlAFQflz0v0=
github.com/mitchellh/go-wordwrap v1.0.1/go.mod h1:R62XHJLzvMFRBbcrT7m7WgmE1eOyTSsCt+hzestvNj0=
github.com/muesli/ansi v0.0.0-20230316100256-276c6243b2f6 h1:ZK8zHtRHOkbHy6Mmr5D264iyp3TiX5OmNcI5cIARiQI=
github.com/muesli/ansi v0.0.0-20230316100256-276c6243b2f6/go.mod h1:CJlz5H+gyd6CUWT45Oy4q24RdLyn7Md9Vj2/ldJBSIo=
github.com/muesli/cancelreader v0.2.2 h1:3I4Kt4BQjOR54NavqnDogx/MIoWBFa0StPA8ELUXHmA=
github.com/muesli/cancelreader v0.2.2/go.mod h1:3XuTXfFS2VjM+HTLZY9Ak0l6eUKfijIfMUZ4EgX0QYo=
github.com/muesli/termenv v0.16.0 h1:S5AlUN9dENB57rsbnkPyfdGuWIlkmzJjbFf0Tf5FWUc=
github.com/muesli/termenv v0.16.0/go.mod h1:ZRfOIKPFDYQoDFF4Olj7/QJbW60Ol/kL1pU3VfY/Cnk=
github.com/pelletier/go-toml/v2 v2.2.5-0.20250826075308-a0e846496753 h1:aTpyfgn3dz2npHl011BHQehdSavqjzhZdE6fJuJlO3A=
github.com/pelletier/go-toml/v2 v2.2.5-0.20250826075308-a0e846496753/go.mod h1:2gIqNv+qfxSVS7cM2xJQKtLSTLUE9V8t9Stt+h56mCY=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rivo/uniseg v0.4.7 h1:WUdvkW8uEhrYfLC4ZzdpI2ztxP1I582+49Oc5Mq64VQ=
github.com/rivo/uniseg v0.4.7/go.mod h1:FN3SvrM+Zdj16jyLfmOkMNblXMcoc8DfTHruCPUcx88=
github.com/stretchr/testify v1.11.1 h1:7s2iGBzp5EwR7/aIZr8ao5+dra3wiQyKjjFuvgVKu7U=
github.com/stretchr/testify v1.11.1/go.mod h1:wZwfW3scLgRK+23gO65QZefKpKQRnfz6sD981Nm4B6U=
github.com/xo/terminfo v0.0.0-20220910002029-abceb7e1c41e h1:JVG44RsyaB9T2KIHavMF/ppJZNG9ZpyihvCd0w101no=
github.com/xo/terminfo v0.0.0-20220910002029-abceb7e1c41e/go.mod h1:RbqR21r5mrJuqunuUZ/Dhy/avygyECGrLceyNeo4LiM=
github.com/zclconf/go-cty v1.17.0 h1:seZvECve6XX4tmnvRzWtJNHdscMtYEx5R7bnnVyd/d0=
github.com/zclconf/go-cty v1.17.0/go.mod h1:wqFzcImaLTI6A5HfsRwB0nj5n0MRZFwmey8YoFPPs3U=
github.com/zclconf/go-cty-debug v0.0.0-20240509010212-0d6042c53940 h1:4r45xpDWB6ZMSMNJFMOjqrGHynW3DIBuR2H9j0ug+Mo=
github.com/zclconf/go-cty-debug v0.0.0-20240509010212-0d6042c53940/go.mod h1:CmBdvvj3nqzfzJ6nTCIwDTPZ56aVGvDrmztiO5g3qrM=
go.yaml.in/yaml/v4 v4.0.0-rc.3 h1:3h1fjsh1CTAPjW7q/EMe+C8shx5d8ctzZTrLcs/j8Go=
go.yaml.in/yaml/v4 v4.0.0-rc.3/go.mod h1:aZqd9kCMsGL7AuUv/m/PvWLdg5sjJsZ4oHDEnfPPfY0=
golang.org/x/exp v0.0.0-20231006140011-7918f672742d h1:jtJma62tbqLibJ5sFQz8bKtEM8rJBtfilJ2qTU199MI=
golang.org/x/exp v0.0.0-20231006140011-7918f672742d/go.mod h1:ldy0pHrwJyGW56pPQzzkH36rKxoZW1tw7ZJpeKx+hdo=
golang.org/x/mod v0.26.0 h1:EGMPT//Ezu+ylkCijjPc+f4Aih7sZvaAr+O3EHBxvZg=
golang.org/x/mod v0.26.0/go.mod h1:/j6NAhSk8iQ723BGAUyoAcn7SlD7s15Dp9Nd/SfeaFQ=
golang.org/x/sync v0.16.0 h1:ycBJEhp9p4vXvUZNszeOq0kGTPghopOL8q0fq3vstxw=
golang.org/x/sync v0.16.0/go.mod h1:1dzgHSNfp02xaA81J2MS99Qcpr2w7fw1gpm99rleRqA=
golang.org/x/sys v0.0.0-20210809222454-d867a43fc93e/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.6.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.38.0 h1:3yZWxaJjBmCWXqhN1qh02AkOnCQ1poK6oF+a7xWL6Gc=
golang.org/x/sys v0.38.0/go.mod h1:OgkHotnGiDImocRcuBABYBEXf8A9a87e/uXjp9XT3ks=
golang.org/x/text v0.28.0 h1:rhazDwis8INMIwQ4tpjLDzUhx6RlXqZNPEM0huQojng=
golang.org/x/text v0.28.0/go.mod h1:U8nCwOR8jO/marOQ0QbDiOngZVEBB7MAiitBuMjXiNU=
golang.org/x/tools v0.35.0 h1:mBffYraMEf7aa0sB+NuKnuCy8qI/9Bughn8dC2Gu5r0=
golang.org/x/tools v0.35.0/go.mod h1:NKdj5HkL/73byiZSJjqJgKn3ep7KjFkBOkR/Hps3VPw=
gopkg.in/ini.v1 v1.67.0 h1:Dgnx+6+nfE+IfzjUEISNeydPJh9AXNNsWbGP9KzCsOA=
gopkg.in/ini.v1 v1.67.0/go.mod h1:pNLf8WUiyNEtQjuu5G5vTm06TEv9tsIgeAvK8hOrP4k=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2020 Tom Wright

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
[![Gitbook](https://badges.aleen42.com/src/gitbook_1.svg)](https://daseldocs.tomwright.me)
[![Go Report Card](https://goreportcard.com/badge/github.com/tomwright/dasel/v3)](https://goreportcard.com/report/github.com/tomwright/dasel/v3)
[![PkgGoDev](https://pkg.go.dev/badge/github.com/tomwright/dasel)](https://pkg.go.dev/github.com/tomwright/dasel/v3)
![Test](https://github.com/TomWright/dasel/workflows/Test/badge.svg)
![Build](https://github.com/TomWright/dasel/workflows/Build/badge.svg)
[![codecov](https://codecov.io/gh/TomWright/dasel/branch/master/graph/badge.svg)](https://codecov.io/gh/TomWright/dasel)
[![Mentioned in Awesome Go](https://awesome.re/mentioned-badge.svg)](https://github.com/avelino/awesome-go)
![GitHub Downloads](https://img.shields.io/github/downloads/TomWright/dasel/total)
![Homebrew Formula Downloads](https://img.shields.io/homebrew/installs/dy/dasel?label=brew%20installs)
![GitHub License](https://img.shields.io/github/license/TomWright/dasel)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/TomWright/dasel?label=latest%20release)](https://github.com/TomWright/dasel/releases/latest)
[![Homebrew tag (latest by date)](https://img.shields.io/homebrew/v/dasel)](https://formulae.brew.sh/formula/dasel)

<div align="center">
    <img src="./daselgopher.png" alt="Dasel mascot" width="250"/>
</div>

# Dasel

Dasel (short for **Data-Select**) is a command-line tool and library for querying, modifying, and transforming data structures such as JSON, YAML, TOML, XML, and CSV.

It provides a consistent, powerful syntax to traverse and update data — making it useful for developers, DevOps, and data wrangling tasks.

---

## Features

* **Multi-format support**: JSON, YAML, TOML, XML, CSV, HCL, INI.
* **Unified query syntax**: Access data in any format with the same selectors.
* **Query & search**: Extract values, lists, or structures with intuitive syntax.
* **Modify in place**: Update, insert, or delete values directly in structured files.
* **Convert between formats**: Seamlessly transform data from JSON → YAML, TOML → JSON, etc.
* **Script-friendly**: Simple CLI integration for shell scripts and pipelines.
* **Library support**: Import and use in Go projects.

---

## Installation

### Homebrew (macOS/Linux)

```sh
brew install dasel
```

### Go Install

```sh
go install github.com/tomwright/dasel/v3/cmd/dasel@master
```

### Prebuilt Binaries

Prebuilt binaries are available on the [Releases](https://github.com/TomWright/dasel/releases) page for Linux, macOS, and Windows.

### None of the above?

See the [installation docs](https://daseldocs.tomwright.me/getting-started/installation) for more options.

---

## Basic Usage

### Selecting Values

By default, Dasel evaluates the final selector and prints the result.

```sh
echo '{"foo": {"bar": "baz"}}' | dasel -i json 'foo.bar'
# Output: "baz"
```

### Modifying Values

Update values inline:

```sh
echo '{"foo": {"bar": "baz"}}' | dasel -i json 'foo.bar = "bong"'
# Output: "bong"
```

Use `--root` to output the full document after modification:

```sh
echo '{"foo": {"bar": "baz"}}' | dasel -i json --root 'foo.bar = "bong"'
# Output:
{
  "foo": {
    "bar": "bong"
  }
}
```

Update values based on previous value:

```sh
echo '[1,2,3,4,5]' | dasel -i json --root 'each($this = $this*2)'
# Output:
[
    2,
    4,
    6,
    8,
    10
]
```

### Format Conversion

```sh
cat data.json | dasel -i json -o yaml
```

### Recursive Descent (`..`)

Searches all nested objects and arrays for a matching key or index.

```sh
echo '{"foo": {"bar": "baz"}}' | dasel -i json '..bar'
# Output:
[
    "baz"
]

```

### Search (`search`)

Finds all values matching a condition anywhere in the structure.

```sh
echo '{"foo": {"bar": "baz"}}' | dasel -i json 'search(bar == "baz")'
# Output:
[
    {
        "bar": "baz"
    }
]

```

---

## Documentation

Full documentation is available at [daseldocs.tomwright.me](https://daseldocs.tomwright.me).

---

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

---

## License

MIT License. See [LICENSE](./LICENSE) for details.

## Stargazers over time

[![Stargazers over time](https://starchart.cc/TomWright/dasel.svg)](https://starchart.cc/TomWright/dasel)
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions

Only the latest major version of Dasel is currently supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 3.x.x   | :white_check_mark: |
| 2.x.x   | :x:                |
| 1.x.x   | :x:                |

## Reporting a Vulnerability

If you believe you have found a security vulnerability in Dasel, please report it privately and directly via one of the following:

- [GitHub vulnerability submission](https://github.com/TomWright/dasel/security/advisories/new)
- [contact@tomwright.me](mailto:contact@tomwright.me)

Please do **not** create a public GitHub issue for security vulnerabilities.  
This allows proper investigation and remediation before disclosure.

### What to Expect

- You will receive an acknowledgement of your report within **7 days**.
- If the vulnerability is confirmed, we will work to release a fix as quickly as possible and will notify you once resolved.
- If the report is declined, we will provide reasoning where possible.

### Important Notes

Security vulnerabilities are not the same as bugs, feature requests, or integration issues.  
For non-security bugs, please use the standard GitHub issue tracker:

👉 https://github.com/TomWright/dasel/issues  

Thank you for helping keep Dasel and its users safe.
```

## File: `cmd/dasel/main.go`
```go
package main

import (
	"io"
	"os"

	"github.com/tomwright/dasel/v3/internal/cli"
	_ "github.com/tomwright/dasel/v3/parsing/csv"
	_ "github.com/tomwright/dasel/v3/parsing/d"
	_ "github.com/tomwright/dasel/v3/parsing/hcl"
	_ "github.com/tomwright/dasel/v3/parsing/ini"
	_ "github.com/tomwright/dasel/v3/parsing/json"
	_ "github.com/tomwright/dasel/v3/parsing/toml"
	_ "github.com/tomwright/dasel/v3/parsing/xml"
	_ "github.com/tomwright/dasel/v3/parsing/yaml"
)

func main() {
	var stdin io.Reader = os.Stdin
	fi, err := os.Stdin.Stat()
	if err != nil || (fi.Mode()&os.ModeCharDevice != 0) {
		stdin = nil
	}
	cli.MustRun(stdin, os.Stdout, os.Stderr)
}
```

## File: `execution/context.go`
```go
package execution

import (
	"context"
	"fmt"
)

type ctxKey string

const (
	executorIDCtxKey    ctxKey = "executorID"
	executorPathCtxKey  ctxKey = "executorPath"
	executorDepthCtxKey ctxKey = "executorDepth"
)

func WithExecutorID(ctx context.Context, executorID string) context.Context {
	currentPath := ExecutorPath(ctx)
	newPath := fmt.Sprintf("%s/%s", currentPath, executorID)
	currentDepth := ExecutorDepth(ctx)
	newDepth := currentDepth + 1
	ctx = context.WithValue(ctx, executorIDCtxKey, executorID)
	ctx = context.WithValue(ctx, executorPathCtxKey, newPath)
	ctx = context.WithValue(ctx, executorDepthCtxKey, newDepth)
	return ctx
}

func ExecutorID(ctx context.Context) string {
	v, ok := ctx.Value(executorIDCtxKey).(string)
	if !ok {
		return ""
	}
	return v
}

func ExecutorPath(ctx context.Context) string {
	v, ok := ctx.Value(executorPathCtxKey).(string)
	if !ok {
		return ""
	}
	return v
}

func ExecutorDepth(ctx context.Context) int {
	v, ok := ctx.Value(executorDepthCtxKey).(int)
	if !ok {
		return 0
	}
	return v
}
```

## File: `execution/execute.go`
```go
package execution

import (
	"context"
	"errors"
	"fmt"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector"
	"github.com/tomwright/dasel/v3/selector/ast"
	"os"
	"reflect"
	"slices"
)

// ExecuteSelector parses the selector and executes the resulting AST with the given input.
func ExecuteSelector(ctx context.Context, selectorStr string, value *model.Value, opts *Options) (*model.Value, error) {
	if selectorStr == "" {
		return value, nil
	}

	expr, err := selector.Parse(selectorStr)
	if err != nil {
		return nil, fmt.Errorf("error parsing selector: %w", err)
	}

	res, err := ExecuteAST(ctx, expr, value, opts)
	if err != nil {
		return nil, fmt.Errorf("error executing selector: %w", err)
	}

	return res, nil
}

type expressionExecutor func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error)

// ExecuteAST executes the given AST with the given input.
func ExecuteAST(ctx context.Context, expr ast.Expr, value *model.Value, options *Options) (*model.Value, error) {
	if expr == nil {
		return value, nil
	}

	executorFn, err := exprExecutor(options, expr)
	if err != nil {
		return nil, fmt.Errorf("error evaluating expression %T: %w", expr, err)
	}

	executor := func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		options.Vars["this"] = data
		out, err := executorFn(ctx, options, data)
		if err != nil {
			return out, err
		}
		return out, nil
	}

	if !value.IsBranch() {
		res, err := executor(ctx, options, value)
		if err != nil {
			return nil, fmt.Errorf("execution error when processing %T: %w", expr, err)
		}
		return res, nil
	}

	res := model.NewSliceValue()
	res.MarkAsBranch()

	if err := value.RangeSlice(func(i int, v *model.Value) error {
		r, err := executor(ctx, options, v)
		if err != nil {
			return err
		}
		if r.IsIgnore() {
			return nil
		}
		return res.Append(r)
	}); err != nil {
		return nil, fmt.Errorf("branch execution error when processing %T: %w", expr, err)
	}

	return res, nil
}

var unstableAstTypes = []reflect.Type{
	reflect.TypeFor[ast.BranchExpr](),
}

func exprExecutor(options *Options, expr ast.Expr) (expressionExecutor, error) {
	if !options.Unstable && (slices.Contains(unstableAstTypes, reflect.TypeOf(expr)) ||
		slices.Contains(unstableAstTypes, reflect.ValueOf(expr).Type())) {
		return nil, errors.New("unstable ast types are not enabled. to enable them use --unstable")
	}

	switch e := expr.(type) {
	case ast.BinaryExpr:
		return binaryExprExecutor(e)
	case ast.UnaryExpr:
		return unaryExprExecutor(e)
	case ast.CallExpr:
		return callExprExecutor(options, e)
	case ast.ChainedExpr:
		return chainedExprExecutor(e)
	case ast.SpreadExpr:
		return spreadExprExecutor()
	case ast.RangeExpr:
		return rangeExprExecutor(e)
	case ast.IndexExpr:
		return indexExprExecutor(e)
	case ast.PropertyExpr:
		return propertyExprExecutor(e)
	case ast.VariableExpr:
		return variableExprExecutor(e)
	case ast.NumberIntExpr:
		return numberIntExprExecutor(e)
	case ast.NumberFloatExpr:
		return numberFloatExprExecutor(e)
	case ast.StringExpr:
		return stringExprExecutor(e)
	case ast.BoolExpr:
		return boolExprExecutor(e)
	case ast.ObjectExpr:
		return objectExprExecutor(e)
	case ast.MapExpr:
		return mapExprExecutor(e)
	case ast.EachExpr:
		return eachExprExecutor(e)
	case ast.FilterExpr:
		return filterExprExecutor(e)
	case ast.SearchExpr:
		return searchExprExecutor(e)
	case ast.RecursiveDescentExpr:
		return recursiveDescentExprExecutor2(e)
	case ast.ConditionalExpr:
		return conditionalExprExecutor(e)
	case ast.BranchExpr:
		return branchExprExecutor(e)
	case ast.ArrayExpr:
		return arrayExprExecutor(e)
	case ast.RegexExpr:
		// Noop
		return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
			//ctx = WithExecutorID(ctx, "regexExpr")
			return data, nil
		}, nil
	case ast.SortByExpr:
		return sortByExprExecutor(e)
	case ast.NullExpr:
		return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
			//ctx = WithExecutorID(ctx, "nullExpr")
			return model.NewNullValue(), nil
		}, nil
	default:
		return nil, fmt.Errorf("unhandled expression type: %T", e)
	}
}

func chainedExprExecutor(e ast.ChainedExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "chainedExpr")
		var curData = data
		for _, expr := range e.Exprs {
			res, err := ExecuteAST(ctx, expr, curData, options)
			if err != nil {
				return nil, fmt.Errorf("error executing expression: %w", err)
			}
			curData = res
		}
		return curData, nil
	}, nil
}

func variableExprExecutor(e ast.VariableExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		//ctx = WithExecutorID(ctx, "variableExpr")
		varName := e.Name
		res, ok := options.Vars[varName]
		if ok {
			return res, nil
		}

		envVarValue := os.Getenv(varName)
		if envVarValue != "" {
			return model.NewStringValue(envVarValue), nil
		}

		return nil, fmt.Errorf("variable %s not found", varName)
	}, nil
}
```

## File: `execution/execute_array.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func arrayExprExecutor(e ast.ArrayExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "arrayExpr")
		res := model.NewSliceValue()

		for _, expr := range e.Exprs {
			el, err := ExecuteAST(ctx, expr, data, options)
			if err != nil {
				return nil, err
			}

			if el.IsSpread() {
				if err := el.RangeSlice(func(_ int, value *model.Value) error {
					if err := res.Append(value); err != nil {
						return err
					}
					return nil
				}); err != nil {
					return nil, err
				}
			} else {
				if err := res.Append(el); err != nil {
					return nil, err
				}
			}
		}

		return res, nil
	}, nil
}

func rangeExprExecutor(e ast.RangeExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "rangeExpr")
		var start, end int64 = 0, -1
		if e.Start != nil {
			startE, err := ExecuteAST(ctx, e.Start, data, options)
			if err != nil {
				return nil, fmt.Errorf("error evaluating start expression: %w", err)
			}

			start, err = startE.IntValue()
			if err != nil {
				return nil, fmt.Errorf("error getting start int value: %w", err)
			}
		}

		if e.End != nil {
			endE, err := ExecuteAST(ctx, e.End, data, options)
			if err != nil {
				return nil, fmt.Errorf("error evaluating end expression: %w", err)
			}

			end, err = endE.IntValue()
			if err != nil {
				return nil, fmt.Errorf("error getting end int value: %w", err)
			}
		}

		var res *model.Value
		var err error

		switch data.Type() {
		case model.TypeString:
			res, err = data.StringIndexRange(int(start), int(end))
		case model.TypeSlice:
			res, err = data.SliceIndexRange(int(start), int(end))
		default:
			err = fmt.Errorf("range expects a slice or string, got %s", data.Type())
		}

		if err != nil {
			return nil, err
		}

		return res, nil
	}, nil
}

func indexExprExecutor(e ast.IndexExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "indexExpr")
		indexE, err := ExecuteAST(ctx, e.Index, data, options)
		if err != nil {
			return nil, fmt.Errorf("error evaluating index expression: %w", err)
		}

		index, err := indexE.IntValue()
		if err != nil {
			return nil, fmt.Errorf("error getting index int value: %w", err)
		}

		return data.GetSliceIndex(int(index))
	}, nil
}
```

## File: `execution/execute_array_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestArray(t *testing.T) {
	inSlice := func() *model.Value {
		s := model.NewSliceValue()
		if err := s.Append(model.NewIntValue(1)); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		if err := s.Append(model.NewIntValue(2)); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		if err := s.Append(model.NewIntValue(3)); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		return s
	}
	inMap := func() *model.Value {
		m := model.NewMapValue()
		if err := m.SetMapKey("numbers", inSlice()); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		return m
	}

	runArrayTests := func(in func() *model.Value, prefix string) func(t *testing.T) {
		return func(t *testing.T) {
			t.Run("1:2", testCase{
				s:    prefix + `[1:2]`,
				inFn: in,
				outFn: func() *model.Value {
					res := model.NewSliceValue()
					if err := res.Append(model.NewIntValue(2)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					if err := res.Append(model.NewIntValue(3)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					return res
				},
			}.run)
			t.Run("1:0", testCase{
				s:    prefix + `[1:0]`,
				inFn: in,
				outFn: func() *model.Value {
					res := model.NewSliceValue()
					if err := res.Append(model.NewIntValue(2)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					if err := res.Append(model.NewIntValue(1)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					return res
				},
			}.run)
			t.Run("1:", testCase{
				s:    prefix + `[1:]`,
				inFn: in,
				outFn: func() *model.Value {
					res := model.NewSliceValue()
					if err := res.Append(model.NewIntValue(2)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					if err := res.Append(model.NewIntValue(3)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					return res
				},
			}.run)
			t.Run(":1", testCase{
				s:    prefix + `[:1]`,
				inFn: in,
				outFn: func() *model.Value {
					res := model.NewSliceValue()
					if err := res.Append(model.NewIntValue(1)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					if err := res.Append(model.NewIntValue(2)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					return res
				},
			}.run)
			t.Run("reverse", testCase{
				s:    prefix + `[len($this)-1:0]`,
				inFn: in,
				outFn: func() *model.Value {
					res := model.NewSliceValue()
					if err := res.Append(model.NewIntValue(3)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					if err := res.Append(model.NewIntValue(2)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					if err := res.Append(model.NewIntValue(1)); err != nil {
						t.Fatalf("unexpected error: %s", err)
					}
					return res
				},
			}.run)
		}
	}

	t.Run("direct to slice", runArrayTests(inSlice, "$this"))
	t.Run("property to slice", runArrayTests(inMap, "numbers"))
}
```

## File: `execution/execute_assign.go`
```go
package execution

import (
	"context"
	"fmt"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func executeAssign(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
	err := left.Set(right)
	if err != nil {
		return nil, fmt.Errorf("error setting value: %w", err)
	}
	return right, nil
}
```

## File: `execution/execute_assign_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/execution"
	"github.com/tomwright/dasel/v3/model"
)

func TestAssignVariable(t *testing.T) {
	t.Run("single assign", testCase{
		s: `$x=1`,
		outFn: func() *model.Value {
			r := model.NewIntValue(1)
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
	t.Run("double assign", testCase{
		s: `$x=1;$y=$x+1`,
		outFn: func() *model.Value {
			r := model.NewIntValue(2)
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
	t.Run("multiple assign with final statement", testCase{
		s: `$first = 'Tom';
$last = 'Wright';
$full = $first + ' ' + $last;
{first: $first, last: $last, full: $full}`,
		outFn: func() *model.Value {
			r := model.NewMapValue()
			if err := r.SetMapKey("first", model.NewStringValue("Tom")); err != nil {
				t.Fatalf("Unexpected error: %s", err)
			}
			if err := r.SetMapKey("last", model.NewStringValue("Wright")); err != nil {
				t.Fatalf("Unexpected error: %s", err)
			}
			if err := r.SetMapKey("full", model.NewStringValue("Tom Wright")); err != nil {
				t.Fatalf("Unexpected error: %s", err)
			}
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
	t.Run("multiple assign with final statement and mixed case variables", testCase{
		s: `$firstName = 'Tom';
$lastName = 'Wright';
$fullName = $firstName + ' ' + $lastName;
{firstName: $firstName, lastName: $lastName, fullName: $fullName}`,
		outFn: func() *model.Value {
			r := model.NewMapValue()
			if err := r.SetMapKey("firstName", model.NewStringValue("Tom")); err != nil {
				t.Fatalf("Unexpected error: %s", err)
			}
			if err := r.SetMapKey("lastName", model.NewStringValue("Wright")); err != nil {
				t.Fatalf("Unexpected error: %s", err)
			}
			if err := r.SetMapKey("fullName", model.NewStringValue("Tom Wright")); err != nil {
				t.Fatalf("Unexpected error: %s", err)
			}
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
	t.Run("self referencing variable", testCase{
		s: `$x=1;$x=$x*2`,
		outFn: func() *model.Value {
			r := model.NewIntValue(2)
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
}
```

## File: `execution/execute_binary.go`
```go
package execution

import (
	"context"
	"errors"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

type binaryExpressionExecutorFn func(ctx context.Context, expr ast.BinaryExpr, value *model.Value, options *Options) (*model.Value, error)

func basicBinaryExpressionExecutorFn(handler func(ctx context.Context, left *model.Value, right *model.Value, e ast.BinaryExpr) (*model.Value, error)) binaryExpressionExecutorFn {
	return func(ctx context.Context, expr ast.BinaryExpr, value *model.Value, options *Options) (*model.Value, error) {
		left, err := ExecuteAST(ctx, expr.Left, value, options)
		if err != nil {
			return nil, fmt.Errorf("error evaluating left expression: %w", err)
		}

		if !left.IsBranch() {
			right, err := ExecuteAST(ctx, expr.Right, value, options)
			if err != nil {
				return nil, fmt.Errorf("error evaluating right expression: %w", err)
			}
			res, err := handler(ctx, left, right, expr)
			if err != nil {
				return nil, err
			}
			return res, nil
		}

		res := model.NewSliceValue()
		res.MarkAsBranch()
		if err := left.RangeSlice(func(i int, v *model.Value) error {
			right, err := ExecuteAST(ctx, expr.Right, v, options)
			if err != nil {
				return fmt.Errorf("error evaluating right expression: %w", err)
			}
			r, err := handler(ctx, v, right, expr)
			if err != nil {
				return err
			}
			if err := res.Append(r); err != nil {
				return err
			}
			return nil
		}); err != nil {
			return nil, err
		}
		return res, nil
	}
}

var binaryExpressionExecutors = map[lexer.TokenKind]binaryExpressionExecutorFn{}

func binaryExprExecutor(e ast.BinaryExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "binaryExpr")
		if e.Left == nil || e.Right == nil {
			return nil, fmt.Errorf("left and right expressions must be provided")
		}

		exec, ok := binaryExpressionExecutors[e.Operator.Kind]
		if !ok {
			return nil, fmt.Errorf("unhandled operator: %s", e.Operator.Value)
		}

		return exec(ctx, e, data, options)
	}, nil
}

func init() {
	binaryExpressionExecutors[lexer.Plus] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.Add(right)
	})
	binaryExpressionExecutors[lexer.Dash] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.Subtract(right)
	})
	binaryExpressionExecutors[lexer.Star] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.Multiply(right)
	})
	binaryExpressionExecutors[lexer.Slash] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.Divide(right)
	})
	binaryExpressionExecutors[lexer.Percent] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.Modulo(right)
	})
	binaryExpressionExecutors[lexer.GreaterThan] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.GreaterThan(right)
	})
	binaryExpressionExecutors[lexer.GreaterThanOrEqual] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.GreaterThanOrEqual(right)
	})
	binaryExpressionExecutors[lexer.LessThan] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.LessThan(right)
	})
	binaryExpressionExecutors[lexer.LessThanOrEqual] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.LessThanOrEqual(right)
	})
	binaryExpressionExecutors[lexer.Equal] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.Equal(right)
	})
	binaryExpressionExecutors[lexer.NotEqual] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		return left.NotEqual(right)
	})
	binaryExpressionExecutors[lexer.Equals] = func(ctx context.Context, expr ast.BinaryExpr, value *model.Value, options *Options) (*model.Value, error) {
		if leftVar, ok := expr.Left.(ast.VariableExpr); ok {
			// It is expected that the left side of an assignment may not exist yet.
			if _, ok := options.Vars[leftVar.Name]; !ok {
				options.Vars[leftVar.Name] = model.NewNullValue()
			}
		}
		return basicBinaryExpressionExecutorFn(executeAssign)(ctx, expr, value, options)
	}
	binaryExpressionExecutors[lexer.And] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		leftBool, err := left.BoolValue()
		if err != nil {
			return nil, fmt.Errorf("error getting left bool value: %w", err)
		}
		rightBool, err := right.BoolValue()
		if err != nil {
			return nil, fmt.Errorf("error getting right bool value: %w", err)
		}
		return model.NewBoolValue(leftBool && rightBool), nil
	})
	binaryExpressionExecutors[lexer.Or] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, right *model.Value, _ ast.BinaryExpr) (*model.Value, error) {
		leftBool, err := left.BoolValue()
		if err != nil {
			return nil, fmt.Errorf("error getting left bool value: %w", err)
		}
		rightBool, err := right.BoolValue()
		if err != nil {
			return nil, fmt.Errorf("error getting right bool value: %w", err)
		}
		return model.NewBoolValue(leftBool || rightBool), nil
	})
	binaryExpressionExecutors[lexer.Like] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, _ *model.Value, e ast.BinaryExpr) (*model.Value, error) {
		leftStr, err := left.StringValue()
		if err != nil {
			return nil, fmt.Errorf("like requires left side to be a string, got %s", left.Type().String())
		}
		rightPatt, ok := e.Right.(ast.RegexExpr)
		if !ok {
			return nil, fmt.Errorf("like requires right side to be a regex pattern")
		}
		res := rightPatt.Regex.MatchString(leftStr)
		return model.NewBoolValue(res), nil
	})
	binaryExpressionExecutors[lexer.NotLike] = basicBinaryExpressionExecutorFn(func(ctx context.Context, left *model.Value, _ *model.Value, e ast.BinaryExpr) (*model.Value, error) {
		leftStr, err := left.StringValue()
		if err != nil {
			return nil, fmt.Errorf("like requires left side to be a string, got %s", left.Type().String())
		}
		rightPatt, ok := e.Right.(ast.RegexExpr)
		if !ok {
			return nil, fmt.Errorf("like requires right side to be a regex pattern")
		}
		res := rightPatt.Regex.MatchString(leftStr)
		return model.NewBoolValue(!res), nil
	})
	binaryExpressionExecutors[lexer.DoubleQuestionMark] = func(ctx context.Context, expr ast.BinaryExpr, value *model.Value, options *Options) (*model.Value, error) {
		left, err := ExecuteAST(ctx, expr.Left, value, options)

		if err == nil && !left.IsNull() {
			return left, nil
		}

		if err != nil {
			handleErrs := []any{
				model.ErrIncompatibleTypes{},
				model.ErrUnexpectedType{},
				model.ErrUnexpectedTypes{},
				model.SliceIndexOutOfRange{},
				model.MapKeyNotFound{},
			}
			for _, e := range handleErrs {
				if errors.As(err, &e) {
					err = nil
					break
				}
			}

			if err != nil {
				return nil, fmt.Errorf("error evaluating left expression: %w", err)
			}
		}

		// Do we need to handle branches here?
		right, err := ExecuteAST(ctx, expr.Right, value, options)
		if err != nil {
			return nil, fmt.Errorf("error evaluating right expression: %w", err)
		}
		return right, nil
	}
}
```

## File: `execution/execute_binary_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/model/orderedmap"
)

func TestBinary(t *testing.T) {
	t.Run("math", func(t *testing.T) {
		t.Run("literals", func(t *testing.T) {
			t.Run("addition", testCase{
				s:   `1 + 2`,
				out: model.NewIntValue(3),
			}.run)
			t.Run("subtraction", testCase{
				s:   `5 - 2`,
				out: model.NewIntValue(3),
			}.run)
			t.Run("multiplication", testCase{
				s:   `5 * 2`,
				out: model.NewIntValue(10),
			}.run)
			t.Run("division", testCase{
				s:   `10 / 2`,
				out: model.NewIntValue(5),
			}.run)
			t.Run("modulus", testCase{
				s:   `10 % 3`,
				out: model.NewIntValue(1),
			}.run)
			t.Run("ordering", testCase{
				s:   `45.2 + 5 * 4 - 2 / 2`, // 45.2 + (5 * 4) - (2 / 2) = 45.2 + 20 - 1 = 64.2
				out: model.NewFloatValue(64.2),
			}.run)
			t.Run("ordering with groups", testCase{
				s:   `(45.2 + 5) * ((4 - 2) / 2)`, // (45.2 + 5) * ((4 - 2) / 2) = (50.2) * ((2) / 2) = (50.2) * (1) = 50.2
				out: model.NewFloatValue(50.2),
			}.run)
			t.Run("ordering with groups", testCase{
				s:   `1 + 1 - 1 + 1 * 2`, // 1 + 1 - 1 + (1 * 2) = 1 + 1 - 1 + 2 = 3
				out: model.NewIntValue(3),
			}.run)
		})
		t.Run("variables", func(t *testing.T) {
			in := func() *model.Value {
				return model.NewValue(orderedmap.NewMap().
					Set("one", 1).
					Set("two", 2).
					Set("three", 3).
					Set("four", 4).
					Set("five", 5).
					Set("six", 6).
					Set("seven", 7).
					Set("eight", 8).
					Set("nine", 9).
					Set("ten", 10).
					Set("fortyfivepoint2", 45.2))
			}
			t.Run("addition", testCase{
				inFn: in,
				s:    `one + two`,
				out:  model.NewIntValue(3),
			}.run)
			t.Run("subtraction", testCase{
				inFn: in,
				s:    `five - two`,
				out:  model.NewIntValue(3),
			}.run)
			t.Run("multiplication", testCase{
				inFn: in,
				s:    `five * two`,
				out:  model.NewIntValue(10),
			}.run)
			t.Run("division", testCase{
				inFn: in,
				s:    `ten / two`,
				out:  model.NewIntValue(5),
			}.run)
			t.Run("modulus", testCase{
				inFn: in,
				s:    `ten % three`,
				out:  model.NewIntValue(1),
			}.run)
			t.Run("ordering", testCase{
				inFn: in,
				s:    `fortyfivepoint2 + five * four - two / two`, // 45.2 + (5 * 4) - (2 / 2) = 45.2 + 20 - 1 = 64.2
				out:  model.NewFloatValue(64.2),
			}.run)
			t.Run("ordering with groups", testCase{
				inFn: in,
				s:    `(fortyfivepoint2 + five) * ((four - two) / two)`, // (45.2 + 5) * ((4 - 2) / 2) = (50.2) * ((2) / 2) = (50.2) * (1) = 50.2
				out:  model.NewFloatValue(50.2),
			}.run)
		})
	})
	t.Run("comparison", func(t *testing.T) {
		t.Run("literals", func(t *testing.T) {
			t.Run("equal", testCase{
				s:   `1 == 1`,
				out: model.NewBoolValue(true),
			}.run)
			t.Run("not equal", testCase{
				s:   `1 != 1`,
				out: model.NewBoolValue(false),
			}.run)
			t.Run("greater than", testCase{
				s:   `2 > 1`,
				out: model.NewBoolValue(true),
			}.run)
			t.Run("greater than or equal", testCase{
				s:   `2 >= 2`,
				out: model.NewBoolValue(true),
			}.run)
			t.Run("less than", testCase{
				s:   `1 < 2`,
				out: model.NewBoolValue(true),
			}.run)
			t.Run("less than or equal", testCase{
				s:   `2 <= 2`,
				out: model.NewBoolValue(true),
			}.run)
			t.Run("like", testCase{
				s:   `"hello world" =~ r/ello/`,
				out: model.NewBoolValue(true),
			}.run)
			t.Run("not like", testCase{
				s:   `"hello world" !~ r/helloworld/`,
				out: model.NewBoolValue(true),
			}.run)
		})

		t.Run("variables", func(t *testing.T) {
			in := func() *model.Value {
				return model.NewValue(orderedmap.NewMap().
					Set("one", 1).
					Set("two", 2).
					Set("nested", orderedmap.NewMap().
						Set("three", 3).
						Set("four", 4)))
			}
			t.Run("equal", testCase{
				inFn: in,
				s:    `one == one`,
				out:  model.NewBoolValue(true),
			}.run)
			t.Run("not equal", testCase{
				inFn: in,
				s:    `one != one`,
				out:  model.NewBoolValue(false),
			}.run)
			t.Run("greater than", testCase{
				inFn: in,
				s:    `two > one`,
				out:  model.NewBoolValue(true),
			}.run)
			t.Run("greater than or equal", testCase{
				inFn: in,
				s:    `two >= two`,
				out:  model.NewBoolValue(true),
			}.run)
			t.Run("less than", testCase{
				inFn: in,
				s:    `one < two`,
				out:  model.NewBoolValue(true),
			}.run)
			t.Run("less than or equal", testCase{
				inFn: in,
				s:    `two <= two`,
				out:  model.NewBoolValue(true),
			}.run)
			t.Run("nested with math more than", testCase{
				inFn: in,
				s:    `nested.three + nested.four * 0 > one * 1`,
				out:  model.NewBoolValue(true),
			}.run)
			t.Run("nested with grouped math more than", testCase{
				inFn: in,
				s:    `(nested.three + nested.four) * 0 > one * 1`,
				out:  model.NewBoolValue(false),
			}.run)
		})

		t.Run("coalesce", func(t *testing.T) {
			t.Run("literals", func(t *testing.T) {
				t.Run("coalesce", testCase{
					s:   `null ?? 1`,
					out: model.NewIntValue(1),
				}.run)
				t.Run("coalesce with null", testCase{
					s:   `null ?? null`,
					out: model.NewNullValue(),
				}.run)
				t.Run("coalesce with null and value", testCase{
					s:   `null ?? 2`,
					out: model.NewIntValue(2),
				}.run)
				t.Run("coalesce with value", testCase{
					s:   `1 ?? 2`,
					out: model.NewIntValue(1),
				}.run)
			})
			t.Run("variables", func(t *testing.T) {
				in := func() *model.Value {
					return model.NewValue(orderedmap.NewMap().
						Set("one", 1).
						Set("two", 2).
						Set("nested", orderedmap.NewMap().
							Set("one", 1).
							Set("two", 2).
							Set("three", 3).
							Set("four", 4)).
						Set("list", []any{1, 2, 3}))
				}
				t.Run("coalesce", testCase{
					inFn: in,
					s:    `nested.five ?? one`,
					out:  model.NewIntValue(1),
				}.run)
				t.Run("coalesce with null", testCase{
					inFn: in,
					s:    `nested.five ?? null`,
					out:  model.NewNullValue(),
				}.run)
				t.Run("coalesce with null and value", testCase{
					inFn: in,
					s:    `nested.five ?? 2`,
					out:  model.NewIntValue(2),
				}.run)
				t.Run("coalesce with value", testCase{
					inFn: in,
					s:    `nested.three ?? 2`,
					out:  model.NewIntValue(3),
				}.run)
				t.Run("coalesce with bad map key", testCase{
					inFn: in,
					s:    `nope ?? 2`,
					out:  model.NewIntValue(2),
				}.run)
				t.Run("coalesce with nested bad map key", testCase{
					inFn: in,
					s:    `nested.nope ?? 2`,
					out:  model.NewIntValue(2),
				}.run)
				t.Run("coalesce with list index", testCase{
					inFn: in,
					s:    `list[1] ?? 5`,
					out:  model.NewIntValue(2),
				}.run)
				t.Run("coalesce with list bad index", testCase{
					inFn: in,
					s:    `list[3] ?? 5`,
					out:  model.NewIntValue(5),
				}.run)
				t.Run("chained coalesce execute left to right", func(t *testing.T) {
					// These tests ensure the coalesces run in order.
					t.Run("no match", testCase{
						inFn: in,
						s:    `nested.five ?? nested.six ?? nested.seven ?? 10`,
						out:  model.NewIntValue(10),
					}.run)
					t.Run("first match when all exist", testCase{
						inFn: in,
						s:    `nested.one ?? nested.two ?? nested.three ?? 10`,
						out:  model.NewIntValue(1),
					}.run)
					t.Run("second match", testCase{
						inFn: in,
						s:    `nested.five ?? nested.two ?? nested.three ?? 10`,
						out:  model.NewIntValue(2),
					}.run)
					t.Run("third match", testCase{
						inFn: in,
						s:    `nested.five ?? nested.six ?? nested.three ?? 10`,
						out:  model.NewIntValue(3),
					}.run)
				})
			})
		})
	})
}
```

## File: `execution/execute_branch.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func branchExprExecutor(e ast.BranchExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "branchExpr")
		res := model.NewSliceValue()
		res.MarkAsBranch()

		if len(e.Exprs) == 0 {
			// No expressions given. We'll branch on the input data.
			if err := data.RangeSlice(func(_ int, value *model.Value) error {
				if err := res.Append(value); err != nil {
					return fmt.Errorf("failed to append branch result: %w", err)
				}
				return nil
			}); err != nil {
				return nil, fmt.Errorf("failed to range slice: %w", err)
			}
		} else {
			for _, expr := range e.Exprs {
				r, err := ExecuteAST(ctx, expr, data, options)
				if err != nil {
					return nil, fmt.Errorf("failed to execute branch expr: %w", err)
				}

				// This deals with the spread operator in the branch expression.
				valsToAppend, err := prepareSpreadValues(r)
				if err != nil {
					return nil, fmt.Errorf("error handling spread values: %w", err)
				}
				for _, v := range valsToAppend {
					if err := res.Append(v); err != nil {
						return nil, fmt.Errorf("failed to append branch result: %w", err)
					}
				}
			}
		}

		return res, nil
	}, nil
}
```

## File: `execution/execute_branch_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/execution"
	"github.com/tomwright/dasel/v3/model"
)

func TestBranch(t *testing.T) {
	t.Run("single branch", testCase{
		s: "branch(1)",
		outFn: func() *model.Value {
			r := model.NewSliceValue()
			r.MarkAsBranch()
			if err := r.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
	t.Run("many branches", testCase{
		s: "branch(1, 1+1, 3/1, 123)",
		outFn: func() *model.Value {
			r := model.NewSliceValue()
			r.MarkAsBranch()
			if err := r.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(3)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(123)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
	t.Run("spread into many branches", testCase{
		s: "[1,2,3].branch(...)",
		outFn: func() *model.Value {
			r := model.NewSliceValue()
			r.MarkAsBranch()
			if err := r.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(3)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
	//t.Run("chained branch set", testCase{
	//	s: "branch(1, 2, 3).=5",
	//	outFn: func() *model.Value {
	//		r := model.NewSliceValue()
	//		r.MarkAsBranch()
	//		if err := r.Append(model.NewIntValue(5)); err != nil {
	//			t.Fatalf("unexpected error: %v", err)
	//		}
	//		if err := r.Append(model.NewIntValue(5)); err != nil {
	//			t.Fatalf("unexpected error: %v", err)
	//		}
	//		if err := r.Append(model.NewIntValue(5)); err != nil {
	//			t.Fatalf("unexpected error: %v", err)
	//		}
	//		return r
	//	},
	//	opts: []execution.ExecuteOptionFn{
	//		execution.WithUnstable(),
	//	},
	//}.run)
	t.Run("chained branch math", testCase{
		s: "(branch(1, 2, 3)) * 2",
		outFn: func() *model.Value {
			r := model.NewSliceValue()
			r.MarkAsBranch()
			if err := r.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(4)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(6)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
	t.Run("chained branch math using branched value", testCase{
		s: `branch({"x":1}, {"x":2}, {"x":3}).x * $this`,
		outFn: func() *model.Value {
			r := model.NewSliceValue()
			r.MarkAsBranch()
			if err := r.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(4)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(9)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
	t.Run("map on branch", testCase{
		s: `branch([1], [2], [3]).map($this * 2).branch()`,
		outFn: func() *model.Value {
			r := model.NewSliceValue()
			r.MarkAsBranch()
			if err := r.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(4)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewIntValue(6)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return r
		},
		opts: []execution.ExecuteOptionFn{
			execution.WithUnstable(),
		},
	}.run)
}
```

## File: `execution/execute_conditional.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func conditionalExprExecutor(e ast.ConditionalExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "conditionalExpr")
		cond, err := ExecuteAST(ctx, e.Cond, data, options)
		if err != nil {
			return nil, fmt.Errorf("error evaluating condition: %w", err)
		}

		condBool, err := cond.BoolValue()
		if err != nil {
			return nil, fmt.Errorf("error converting condition to boolean: %w", err)
		}

		if condBool {
			res, err := ExecuteAST(ctx, e.Then, data, options)
			if err != nil {
				return nil, fmt.Errorf("error executing then block: %w", err)
			}
			return res, nil
		}

		if e.Else != nil {
			res, err := ExecuteAST(ctx, e.Else, data, options)
			if err != nil {
				return nil, fmt.Errorf("error executing else block: %w", err)
			}
			return res, nil
		}

		return model.NewNullValue(), nil
	}, nil
}
```

## File: `execution/execute_conditional_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestConditional(t *testing.T) {
	t.Run("true", testCase{
		s:   `if (true) { "yes" } else { "no" }`,
		out: model.NewStringValue("yes"),
	}.run)
	t.Run("false", testCase{
		s:   `if (false) { "yes" } else { "no" }`,
		out: model.NewStringValue("no"),
	}.run)
	t.Run("nested", testCase{
		s: `
				if (true) {
					if (true) { "yes" }
					else { "no" }
				} else { "no" }`,
		out: model.NewStringValue("yes"),
	}.run)
	t.Run("nested false", testCase{
		s: `
				if (true) {
					if (false) { "yes" }
					else { "no" }
				} else { "no" }`,
		out: model.NewStringValue("no"),
	}.run)
	t.Run("else if", testCase{
		s: `
				if (false) { "yes" }
				elseif (true) { "no" }
				else { "maybe" }`,
		out: model.NewStringValue("no"),
	}.run)
	t.Run("else if else", testCase{
		s: `
				if (false) { "yes" }
				elseif (false) { "no" }
				else { "maybe" }`,
		out: model.NewStringValue("maybe"),
	}.run)
	t.Run("if elseif elseif else", testCase{
		s: `
				if (false) { "yes" }
				elseif (false) { "no" }
				elseif (false) { "maybe" }
				else { "nope" }`,
		out: model.NewStringValue("nope"),
	}.run)
}
```

## File: `execution/execute_each.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func eachExprExecutor(e ast.EachExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "eachExpr")
		if !data.IsSlice() {
			return nil, fmt.Errorf("cannot each over non-array")
		}

		if err := data.RangeSlice(func(i int, item *model.Value) error {
			_, err := ExecuteAST(ctx, e.Expr, item, options)
			if err != nil {
				return err
			}
			return nil
		}); err != nil {
			return nil, fmt.Errorf("error ranging over slice: %w", err)
		}

		return data, nil
	}, nil
}
```

## File: `execution/execute_each_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestEach(t *testing.T) {
	t.Run("all true", testCase{
		s: "[1,2,3].each($this = $this + 1)",
		outFn: func() *model.Value {
			s := model.NewSliceValue()
			if err := s.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if err := s.Append(model.NewIntValue(3)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if err := s.Append(model.NewIntValue(4)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			return s
		},
	}.run)
}
```

## File: `execution/execute_filter.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func filterExprExecutor(e ast.FilterExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "filterExpr")
		if !data.IsSlice() {
			return nil, fmt.Errorf("cannot filter over non-array")
		}
		res := model.NewSliceValue()

		if err := data.RangeSlice(func(i int, item *model.Value) error {
			v, err := ExecuteAST(ctx, e.Expr, item, options)
			if err != nil {
				return err
			}

			boolV, err := v.BoolValue()
			if err != nil {
				return err
			}

			if !boolV {
				return nil
			}
			if err := res.Append(item); err != nil {
				return fmt.Errorf("error appending item to result: %w", err)
			}
			return nil
		}); err != nil {
			return nil, fmt.Errorf("error ranging over slice: %w", err)
		}

		return res, nil
	}, nil
}
```

## File: `execution/execute_filter_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestFilter(t *testing.T) {
	inSlice := func() *model.Value {
		s := model.NewSliceValue()
		if err := s.Append(model.NewIntValue(1)); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		if err := s.Append(model.NewIntValue(2)); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		if err := s.Append(model.NewIntValue(3)); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		return s
	}
	t.Run("all true", testCase{
		inFn: inSlice,
		s:    "filter(true)",
		outFn: func() *model.Value {
			s := model.NewSliceValue()
			if err := s.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if err := s.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if err := s.Append(model.NewIntValue(3)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			return s
		},
	}.run)
	t.Run("all !false", testCase{
		inFn: inSlice,
		s:    "filter(!false)",
		outFn: func() *model.Value {
			s := model.NewSliceValue()
			if err := s.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if err := s.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if err := s.Append(model.NewIntValue(3)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			return s
		},
	}.run)
	t.Run("all false", testCase{
		inFn: inSlice,
		s:    "filter(false)",
		outFn: func() *model.Value {
			s := model.NewSliceValue()
			return s
		},
	}.run)
	t.Run("all !true", testCase{
		inFn: inSlice,
		s:    "filter(!true)",
		outFn: func() *model.Value {
			s := model.NewSliceValue()
			return s
		},
	}.run)
	t.Run("equal 2", testCase{
		inFn: inSlice,
		s:    "filter($this == 2)",
		outFn: func() *model.Value {
			s := model.NewSliceValue()
			if err := s.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			return s
		},
	}.run)
	t.Run("not equal 2", testCase{
		inFn: inSlice,
		s:    "filter($this != 2)",
		outFn: func() *model.Value {
			s := model.NewSliceValue()
			if err := s.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if err := s.Append(model.NewIntValue(3)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			return s
		},
	}.run)
}
```

## File: `execution/execute_func.go`
```go
package execution

import (
	"context"
	"errors"
	"fmt"
	"slices"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func prepareArgs(ctx context.Context, opts *Options, data *model.Value, argsE ast.Expressions) (model.Values, error) {
	args := make(model.Values, 0)
	for i, arg := range argsE {
		res, err := ExecuteAST(ctx, arg, data, opts)
		if err != nil {
			return nil, fmt.Errorf("error evaluating argument %d: %w", i, err)
		}

		argVals, err := prepareSpreadValues(res)
		if err != nil {
			return nil, fmt.Errorf("error handling spread values: %w", err)
		}

		args = append(args, argVals...)
	}
	return args, nil
}

func callFnExecutor(f FuncFn, argsE ast.Expressions) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "callFnExpr")
		args, err := prepareArgs(ctx, options, data, argsE)
		if err != nil {
			return nil, fmt.Errorf("error preparing arguments: %w", err)
		}

		res, err := f(ctx, data, args)
		if err != nil {
			return nil, fmt.Errorf("error executing function: %w", err)
		}

		return res, nil
	}, nil
}

var unstableFuncs = []string{
	"ignore",
}

func callExprExecutor(options *Options, e ast.CallExpr) (expressionExecutor, error) {
	if !options.Unstable && (slices.Contains(unstableFuncs, e.Function)) {
		return nil, errors.New("unstable function are not enabled. to enable them use --unstable")
	}
	if f, ok := options.Funcs.Get(e.Function); ok {
		res, err := callFnExecutor(f, e.Args)
		if err != nil {
			return nil, fmt.Errorf("error executing function %q: %w", e.Function, err)
		}
		return res, nil
	}

	return nil, fmt.Errorf("unknown function: %q", e.Function)
}
```

## File: `execution/execute_func_test.go`
```go
package execution_test

import (
	"context"
	"testing"

	"github.com/tomwright/dasel/v3/execution"
	"github.com/tomwright/dasel/v3/model"
)

func TestFunc(t *testing.T) {
	returnInputData := execution.NewFunc(
		"returnInputData",
		func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
			return data, nil
		},
		execution.ValidateArgsExactly(0),
	)

	returnFirstArg := execution.NewFunc(
		"returnFirstArg",
		func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
			return args[0], nil
		},
		execution.ValidateArgsExactly(1),
	)

	funcs := execution.NewFuncCollection(
		returnInputData,
		returnFirstArg,
	)

	opts := []execution.ExecuteOptionFn{
		func(options *execution.Options) {
			options.Funcs = funcs
		},
	}

	t.Run("returnInputData", testCase{
		s:    `1.returnInputData()`,
		out:  model.NewIntValue(1),
		opts: opts,
	}.run)

	t.Run("returnFirstArg", testCase{
		s:    `1.returnFirstArg(2)`,
		out:  model.NewIntValue(2),
		opts: opts,
	}.run)
}
```

## File: `execution/execute_literal.go`
```go
package execution

import (
	"context"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func numberIntExprExecutor(e ast.NumberIntExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		//ctx = WithExecutorID(ctx, "numberIntExpr")
		return model.NewIntValue(e.Value), nil
	}, nil
}

func numberFloatExprExecutor(e ast.NumberFloatExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		//ctx = WithExecutorID(ctx, "numberFloatExpr")
		return model.NewFloatValue(e.Value), nil
	}, nil
}

func stringExprExecutor(e ast.StringExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		//ctx = WithExecutorID(ctx, "stringExpr")
		return model.NewStringValue(e.Value), nil
	}, nil
}

func boolExprExecutor(e ast.BoolExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		//ctx = WithExecutorID(ctx, "boolExpr")
		return model.NewBoolValue(e.Value), nil
	}, nil
}
```

## File: `execution/execute_literal_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestLiteral(t *testing.T) {
	t.Run("string", testCase{
		s:   `"hello"`,
		out: model.NewStringValue("hello"),
	}.run)
	t.Run("int", testCase{
		s:   `123`,
		out: model.NewIntValue(123),
	}.run)
	t.Run("float", testCase{
		s:   `123.4`,
		out: model.NewFloatValue(123.4),
	}.run)
	t.Run("true", testCase{
		s:   `true`,
		out: model.NewBoolValue(true),
	}.run)
	t.Run("false", testCase{
		s:   `false`,
		out: model.NewBoolValue(false),
	}.run)
	t.Run("empty array", testCase{
		s: `[]`,
		outFn: func() *model.Value {
			r := model.NewSliceValue()
			return r
		},
	}.run)
	t.Run("array with one element", testCase{
		s: `[1]`,
		outFn: func() *model.Value {
			r := model.NewSliceValue()
			if err := r.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return r
		},
	}.run)
	t.Run("array with many elements", testCase{
		s: `[1, 2.2, "foo", true, [1, 2, 3]]`,
		outFn: func() *model.Value {
			nested := model.NewSliceValue()
			if err := nested.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := nested.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := nested.Append(model.NewIntValue(3)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}

			r := model.NewSliceValue()
			if err := r.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewFloatValue(2.2)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewStringValue("foo")); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewBoolValue(true)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(nested); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return r
		},
	}.run)
	t.Run("array with expressions", testCase{
		s: `[1 + 1, 2f - 2, "foo" + "bar", true || false, [1 + 1, 2 * 2, 3 / 3]]`,
		outFn: func() *model.Value {
			nested := model.NewSliceValue()
			if err := nested.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := nested.Append(model.NewIntValue(4)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := nested.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}

			r := model.NewSliceValue()
			if err := r.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewFloatValue(0)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewStringValue("foobar")); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(model.NewBoolValue(true)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := r.Append(nested); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return r
		},
	}.run)
}
```

## File: `execution/execute_map.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func mapExprExecutor(e ast.MapExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "mapExpr")
		if !data.IsSlice() {
			return nil, fmt.Errorf("cannot map over non-array")
		}
		res := model.NewSliceValue()

		if err := data.RangeSlice(func(i int, item *model.Value) error {
			item, err := ExecuteAST(ctx, e.Expr, item, options)
			if err != nil {
				return err
			}
			if err := res.Append(item); err != nil {
				return fmt.Errorf("error appending item to result: %w", err)
			}
			return nil
		}); err != nil {
			return nil, fmt.Errorf("error ranging over slice: %w", err)
		}
		return res, nil
	}, nil
}
```

## File: `execution/execute_map_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/model/orderedmap"
)

func TestMap(t *testing.T) {
	t.Run("property from slice of maps", testCase{
		inFn: func() *model.Value {
			return model.NewValue([]any{
				orderedmap.NewMap().Set("number", 1),
				orderedmap.NewMap().Set("number", 2),
				orderedmap.NewMap().Set("number", 3),
			})
		},
		s: `map(number)`,
		outFn: func() *model.Value {
			return model.NewValue([]any{1, 2, 3})
		},
	}.run)
	t.Run("with chain of selectors", testCase{
		inFn: func() *model.Value {
			return model.NewValue([]any{
				orderedmap.NewMap().Set("foo", 1).Set("bar", 4),
				orderedmap.NewMap().Set("foo", 2).Set("bar", 5),
				orderedmap.NewMap().Set("foo", 3).Set("bar", 6),
			})
		},
		s: `
				map (
					{
						total: add( foo, bar, 1 )
					}
				)
				.map ( total )`,
		outFn: func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewValue(6)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewValue(8)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewValue(10)); err != nil {
				t.Fatal(err)
			}
			return res
		},
	}.run)
}
```

## File: `execution/execute_object.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func objectExprExecutor(e ast.ObjectExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "objectExpr")
		obj := model.NewMapValue()
		for _, p := range e.Pairs {

			if ast.IsType[ast.SpreadExpr](p.Key) {
				var val *model.Value
				var err error
				if p.Value != nil {
					// We need to spread the resulting value.
					val, err = ExecuteAST(ctx, p.Value, data, options)
					if err != nil {
						return nil, fmt.Errorf("error evaluating spread values: %w", err)
					}
				} else {
					val = data
				}

				if err := val.RangeMap(func(key string, value *model.Value) error {
					if err := obj.SetMapKey(key, value); err != nil {
						return fmt.Errorf("error setting map key: %w", err)
					}
					return nil
				}); err != nil {
					return nil, fmt.Errorf("error spreading into object: %w", err)
				}
				continue
			}

			key, err := ExecuteAST(ctx, p.Key, data, options)
			if err != nil {
				return nil, fmt.Errorf("error evaluating key: %w", err)
			}
			if !key.IsString() {
				return nil, fmt.Errorf("expected key to resolve to string, got %s", key.Type())
			}

			val, err := ExecuteAST(ctx, p.Value, data, options)
			if err != nil {
				return nil, fmt.Errorf("error evaluating value: %w", err)
			}

			keyStr, err := key.StringValue()
			if err != nil {
				return nil, fmt.Errorf("error getting string value: %w", err)
			}
			if err := obj.SetMapKey(keyStr, val); err != nil {
				return nil, fmt.Errorf("error setting map key: %w", err)
			}
		}
		return obj, nil
	}, nil
}

func propertyExprExecutor(e ast.PropertyExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "propertyExpr")
		key, err := ExecuteAST(ctx, e.Property, data, options)
		if err != nil {
			return nil, fmt.Errorf("error evaluating property: %w", err)
		}
		switch {
		case key.IsString():
			keyStr, err := key.StringValue()
			if err != nil {
				return nil, fmt.Errorf("error getting string value: %w", err)
			}

			return data.GetMapKey(keyStr)
		case key.IsInt():
			keyInt, err := key.IntValue()
			if err != nil {
				return nil, fmt.Errorf("error getting int value: %w", err)
			}
			return data.GetSliceIndex(int(keyInt))
		default:
			return nil, fmt.Errorf("expected key to be a string or int, got %s", key.Type())
		}
	}, nil
}
```

## File: `execution/execute_object_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/model/orderedmap"
)

func TestObject(t *testing.T) {
	inputMap := func() *model.Value {
		return model.NewValue(orderedmap.NewMap().
			Set("title", "Mr").
			Set("age", int64(30)).
			Set("name", orderedmap.NewMap().
				Set("first", "Tom").
				Set("last", "Wright")))
	}
	t.Run("get", testCase{
		in: inputMap(),
		s:  `{title}`,
		outFn: func() *model.Value {
			return model.NewValue(orderedmap.NewMap().Set("title", "Mr"))
		},
	}.run)
	t.Run("get multiple", testCase{
		in: inputMap(),
		s:  `{title, age}`,
		outFn: func() *model.Value {
			return model.NewValue(orderedmap.NewMap().Set("title", "Mr").Set("age", int64(30)))
		},
	}.run)
	t.Run("get with spread", testCase{
		in: inputMap(),
		s:  `{...}`,
		outFn: func() *model.Value {
			res := inputMap()
			return res
		},
	}.run)
	t.Run("set", testCase{
		in: inputMap(),
		s:  `{title:"Mrs"}`,
		outFn: func() *model.Value {
			res := model.NewMapValue()
			_ = res.SetMapKey("title", model.NewStringValue("Mrs"))
			return res
		},
	}.run)
	t.Run("set with spread", testCase{
		in: inputMap(),
		s:  `{..., title:"Mrs"}`,
		outFn: func() *model.Value {
			res := inputMap()
			_ = res.SetMapKey("title", model.NewStringValue("Mrs"))
			return res
		},
	}.run)
	t.Run("merge with spread", testCase{
		inFn: func() *model.Value {
			a := model.NewMapValue()
			if err := a.SetMapKey("foo", model.NewStringValue("afoo")); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			if err := a.SetMapKey("bar", model.NewStringValue("abar")); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			b := model.NewMapValue()
			if err := b.SetMapKey("bar", model.NewStringValue("bbar")); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			if err := b.SetMapKey("baz", model.NewStringValue("bbaz")); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			res := model.NewMapValue()
			if err := res.SetMapKey("a", a); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			if err := res.SetMapKey("b", b); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			return res
		},
		s: `{a..., b..., x: 1}`,
		outFn: func() *model.Value {
			b := model.NewMapValue()
			if err := b.SetMapKey("foo", model.NewStringValue("afoo")); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := b.SetMapKey("bar", model.NewStringValue("bbar")); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := b.SetMapKey("baz", model.NewStringValue("bbaz")); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := b.SetMapKey("x", model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return b
		},
	}.run)
}
```

## File: `execution/execute_recursive_descent.go`
```go
package execution

import (
	"context"
	"errors"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func recursiveDescentExprExecutor2(e ast.RecursiveDescentExpr) (expressionExecutor, error) {
	var doSearch func(ctx context.Context, options *Options, data *model.Value) ([]*model.Value, error)
	findValue := func(ctx context.Context, options *Options, v *model.Value) (*model.Value, error) {
		property, err := ExecuteAST(ctx, e.Expr, v, options)
		if err != nil {
			handleErrs := []any{
				model.ErrIncompatibleTypes{},
				model.ErrUnexpectedType{},
				model.ErrUnexpectedTypes{},
				model.SliceIndexOutOfRange{},
				model.MapKeyNotFound{},
			}
			for _, e := range handleErrs {
				if errors.As(err, &e) {
					err = nil
					break
				}
			}
		}

		if err != nil {
			return nil, err
		}
		return property, nil
	}
	doSearch = func(ctx context.Context, options *Options, data *model.Value) ([]*model.Value, error) {
		res := make([]*model.Value, 0)

		switch data.Type() {
		case model.TypeMap:
			if err := data.RangeMap(func(key string, v *model.Value) error {
				if v.IsScalar() {
					if e.IsWildcard {
						res = append(res, v)
					}
				} else {
					if !e.IsWildcard {
						property, err := findValue(ctx, options, v)
						if err != nil {
							return err
						}
						if property != nil {
							res = append(res, property)
						}
					}

					gotNext, err := doSearch(ctx, options, v)
					if err != nil {
						return err
					}
					res = append(res, gotNext...)
				}
				return nil
			}); err != nil {
				return nil, err
			}
		case model.TypeSlice:
			if err := data.RangeSlice(func(i int, v *model.Value) error {
				if v.IsScalar() {
					if e.IsWildcard {
						res = append(res, v)
					}
				} else {
					if !e.IsWildcard {
						property, err := findValue(ctx, options, v)
						if err != nil {
							return err
						}
						if property != nil {
							res = append(res, property)
						}
					}

					gotNext, err := doSearch(ctx, options, v)
					if err != nil {
						return err
					}
					res = append(res, gotNext...)
				}
				return nil
			}); err != nil {
				return nil, err
			}
		}

		return res, nil
	}

	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "recursiveDescentExpr")
		matches := model.NewSliceValue()

		found, err := doSearch(ctx, options, data)
		if err != nil {
			return nil, err
		}

		for _, f := range found {
			if err := matches.Append(f); err != nil {
				return nil, err
			}
		}

		return matches, nil
	}, nil
}
```

## File: `execution/execute_search.go`
```go
package execution

import (
	"context"
	"errors"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func searchExprExecutor(e ast.SearchExpr) (expressionExecutor, error) {
	var doSearch func(ctx context.Context, options *Options, data *model.Value) ([]*model.Value, error)
	processValue := func(ctx context.Context, v *model.Value, options *Options) (bool, error) {
		got, err := ExecuteAST(ctx, e.Expr, v, options)
		if err != nil {
			handleErrs := []any{
				model.ErrIncompatibleTypes{},
				model.ErrUnexpectedType{},
				model.ErrUnexpectedTypes{},
				model.SliceIndexOutOfRange{},
				model.MapKeyNotFound{},
			}
			for _, e := range handleErrs {
				if errors.As(err, &e) {
					err = nil
					break
				}
			}
		}
		if err != nil {
			return false, err
		}

		if got == nil {
			return false, nil
		}

		gotV, err := got.BoolValue()
		if err != nil {
			return false, err
		}
		return gotV, nil
	}
	doSearch = func(ctx context.Context, options *Options, data *model.Value) ([]*model.Value, error) {
		res := make([]*model.Value, 0)

		switch data.Type() {
		case model.TypeMap:
			if err := data.RangeMap(func(key string, v *model.Value) error {
				match, err := processValue(ctx, v, options)
				if err != nil {
					return err
				}

				if match {
					res = append(res, v)
				}

				gotNext, err := doSearch(ctx, options, v)
				if err != nil {
					return err
				}
				res = append(res, gotNext...)

				return nil
			}); err != nil {
				return nil, err
			}
		case model.TypeSlice:
			if err := data.RangeSlice(func(i int, v *model.Value) error {
				match, err := processValue(ctx, v, options)
				if err != nil {
					return err
				}

				if match {
					res = append(res, v)
				}

				gotNext, err := doSearch(ctx, options, v)
				if err != nil {
					return err
				}
				res = append(res, gotNext...)

				return nil
			}); err != nil {
				return nil, err
			}
		}

		return res, nil
	}

	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "searchExpr")
		matches := model.NewSliceValue()

		found, err := doSearch(ctx, options, data)
		if err != nil {
			return nil, err
		}

		for _, f := range found {
			if err := matches.Append(f); err != nil {
				return nil, err
			}
		}

		return matches, nil
	}, nil
}
```

## File: `execution/execute_sort_by.go`
```go
package execution

import (
	"context"
	"fmt"
	"slices"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
)

func sortByExprExecutor(e ast.SortByExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "sortByExpr")
		if !data.IsSlice() {
			return nil, fmt.Errorf("cannot sort by on non-slice data")
		}

		type sortableValue struct {
			index int
			value *model.Value
		}
		values := make([]sortableValue, 0)

		if err := data.RangeSlice(func(i int, item *model.Value) error {
			item, err := ExecuteAST(ctx, e.Expr, item, options)
			if err != nil {
				return err
			}
			values = append(values, sortableValue{
				index: i,
				value: item,
			})
			return nil
		}); err != nil {
			return nil, fmt.Errorf("error ranging over slice: %w", err)
		}

		slices.SortFunc(values, func(i, j sortableValue) int {
			res, err := i.value.Compare(j.value)
			if err != nil {
				return 0
			}
			if e.Descending {
				return -res
			}
			return res
		})

		res := model.NewSliceValue()

		for _, i := range values {
			item, err := data.GetSliceIndex(i.index)
			if err != nil {
				return nil, fmt.Errorf("error getting slice index: %w", err)
			}
			if err := res.Append(item); err != nil {
				return nil, fmt.Errorf("error appending item to result: %w", err)
			}
		}

		return res, nil
	}, nil
}
```

## File: `execution/execute_sort_by_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestFuncSortBy(t *testing.T) {
	runSortTests := func(in func() *model.Value, outAsc func() *model.Value, outDesc func() *model.Value) func(*testing.T) {
		return func(t *testing.T) {
			t.Run("asc default", testCase{
				inFn:  in,
				s:     `sortBy($this)`,
				outFn: outAsc,
			}.run)
			t.Run("asc", testCase{
				inFn:  in,
				s:     `sortBy($this, asc)`,
				outFn: outAsc,
			}.run)
			t.Run("desc", testCase{
				inFn:  in,
				s:     `sortBy($this, desc)`,
				outFn: outDesc,
			}.run)
		}
	}

	t.Run("int", runSortTests(
		func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewIntValue(2)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewIntValue(1)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewIntValue(4)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewIntValue(3)); err != nil {
				t.Fatal(err)
			}
			return res
		},
		func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewIntValue(1)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewIntValue(2)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewIntValue(3)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewIntValue(4)); err != nil {
				t.Fatal(err)
			}
			return res
		},
		func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewIntValue(4)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewIntValue(3)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewIntValue(2)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewIntValue(1)); err != nil {
				t.Fatal(err)
			}
			return res
		},
	))

	t.Run("float", runSortTests(
		func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewFloatValue(2.23)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewFloatValue(2)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewFloatValue(5.123)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewFloatValue(4.2)); err != nil {
				t.Fatal(err)
			}
			return res
		},
		func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewFloatValue(2)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewFloatValue(2.23)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewFloatValue(4.2)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewFloatValue(5.123)); err != nil {
				t.Fatal(err)
			}
			return res
		},
		func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewFloatValue(5.123)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewFloatValue(4.2)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewFloatValue(2.23)); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewFloatValue(2)); err != nil {
				t.Fatal(err)
			}
			return res
		},
	))
	t.Run("string", runSortTests(
		func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewStringValue("def")); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewStringValue("abc")); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewStringValue("cde")); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewStringValue("bcd")); err != nil {
				t.Fatal(err)
			}
			return res
		},
		func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewStringValue("abc")); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewStringValue("bcd")); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewStringValue("cde")); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewStringValue("def")); err != nil {
				t.Fatal(err)
			}
			return res
		},
		func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewStringValue("def")); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewStringValue("cde")); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewStringValue("bcd")); err != nil {
				t.Fatal(err)
			}
			if err := res.Append(model.NewStringValue("abc")); err != nil {
				t.Fatal(err)
			}
			return res
		},
	))
}
```

## File: `execution/execute_spread.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
)

func spreadExprExecutor() (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		//ctx = WithExecutorID(ctx, "spreadExpr")
		s := model.NewSliceValue()

		s.MarkAsSpread()

		switch {
		case data.IsSlice():
			if err := data.RangeSlice(func(key int, value *model.Value) error {
				if err := s.Append(value); err != nil {
					return fmt.Errorf("error appending value to slice: %w", err)
				}
				return nil
			}); err != nil {
				return nil, fmt.Errorf("error ranging slice: %w", err)
			}
		case data.IsMap():
			if err := data.RangeMap(func(key string, value *model.Value) error {
				if err := s.Append(value); err != nil {
					return fmt.Errorf("error appending value to slice: %w", err)
				}
				return nil
			}); err != nil {
				return nil, fmt.Errorf("error ranging map: %w", err)
			}
		default:
			return nil, fmt.Errorf("cannot spread on type %s", data.Type())
		}

		return s, nil
	}, nil
}

// prepareSpreadValues looks at the incoming value, and if we detect a spread value, we return the individual values.
func prepareSpreadValues(val *model.Value) (model.Values, error) {
	if val.IsSlice() && val.IsSpread() {
		sliceLen, err := val.SliceLen()
		if err != nil {
			return nil, fmt.Errorf("error getting slice length: %w", err)
		}
		values := make(model.Values, sliceLen)
		for i := 0; i < sliceLen; i++ {
			v, err := val.GetSliceIndex(i)
			if err != nil {
				return nil, fmt.Errorf("error getting slice index %d: %w", i, err)
			}
			values[i] = v
		}
		return values, nil
	}
	return model.Values{val}, nil
}
```

## File: `execution/execute_spread_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestSpread(t *testing.T) {
	t.Run("build new array", testCase{
		s: "[[1,2,3]..., 4]",
		outFn: func() *model.Value {
			s := model.NewSliceValue()
			if err := s.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if err := s.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if err := s.Append(model.NewIntValue(3)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if err := s.Append(model.NewIntValue(4)); err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			return s
		},
	}.run)
}
```

## File: `execution/execute_test.go`
```go
package execution_test

import (
	"context"
	"testing"

	"github.com/google/go-cmp/cmp"
	"github.com/tomwright/dasel/v3/execution"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/model/orderedmap"
)

type testCase struct {
	in          *model.Value
	inFn        func() *model.Value
	s           string
	out         *model.Value
	outFn       func() *model.Value
	compareRoot bool
	opts        []execution.ExecuteOptionFn
}

func (tc testCase) run(t *testing.T) {
	in := tc.in
	if tc.inFn != nil {
		in = tc.inFn()
	}
	if in == nil {
		in = model.NewValue(nil)
	}
	exp := tc.out
	if tc.outFn != nil {
		exp = tc.outFn()
	}
	res, err := execution.ExecuteSelector(context.Background(), tc.s, in, execution.NewOptions(tc.opts...))
	if err != nil {
		t.Fatal(err)
	}

	if tc.compareRoot {
		res = in
	}

	equal, err := res.EqualTypeValue(exp)
	if err != nil {
		t.Fatal(err)
	}
	if !equal {
		t.Errorf("unexpected output:\nexp: %s\ngot: %s", exp.String(), res.String())
	}

	expMeta := exp.Metadata
	gotMeta := res.Metadata
	if !cmp.Equal(expMeta, gotMeta) {
		t.Errorf("unexpected output metadata: %v", cmp.Diff(expMeta, gotMeta))
	}
}

func TestExecuteSelector_HappyPath(t *testing.T) {
	t.Run("get", func(t *testing.T) {
		inputMap := func() *model.Value {
			return model.NewValue(
				orderedmap.NewMap().
					Set("title", "Mr").
					Set("age", int64(31)).
					Set("name", orderedmap.NewMap().
						Set("first", "Tom").
						Set("last", "Wright")),
			)
		}
		t.Run("property", testCase{
			in:  inputMap(),
			s:   `title`,
			out: model.NewStringValue("Mr"),
		}.run)
		t.Run("nested property", testCase{
			in:  inputMap(),
			s:   `name.first`,
			out: model.NewStringValue("Tom"),
		}.run)
		t.Run("concat with grouping", testCase{
			in:  inputMap(),
			s:   `title + " " + (name.first) + " " + (name.last)`,
			out: model.NewStringValue("Mr Tom Wright"),
		}.run)
		t.Run("concat", testCase{
			in:  inputMap(),
			s:   `title + " " + name.first + " " + name.last`,
			out: model.NewStringValue("Mr Tom Wright"),
		}.run)
		t.Run("add evaluated fields", testCase{
			in: inputMap(),
			s:  `{..., "over30": age > 30}`,
			outFn: func() *model.Value {
				return model.NewValue(
					orderedmap.NewMap().
						Set("title", "Mr").
						Set("age", int64(31)).
						Set("name", orderedmap.NewMap().
							Set("first", "Tom").
							Set("last", "Wright")).
						Set("over30", true),
				)
			},
		}.run)
	})

	t.Run("set", func(t *testing.T) {
		inputMap := func() *model.Value {
			return model.NewValue(
				orderedmap.NewMap().
					Set("title", "Mr").
					Set("age", int64(31)).
					Set("name", orderedmap.NewMap().
						Set("first", "Tom").
						Set("last", "Wright")),
			)
		}
		inputSlice := func() *model.Value {
			return model.NewValue([]any{1, 2, 3})
		}

		t.Run("set property", testCase{
			in: inputMap(),
			s:  `title = "Mrs"`,
			outFn: func() *model.Value {
				res := inputMap()
				if err := res.SetMapKey("title", model.NewStringValue("Mrs")); err != nil {
					t.Fatalf("unexpected error: %s", err)
				}
				return res
			},
			compareRoot: true,
		}.run)

		t.Run("set index", testCase{
			in: inputSlice(),
			s:  `$this[1] = 4`,
			outFn: func() *model.Value {
				res := inputSlice()
				if err := res.SetSliceIndex(1, model.NewIntValue(4)); err != nil {
					t.Fatalf("unexpected error: %s", err)
				}
				return res
			},
			compareRoot: true,
		}.run)
	})
}
```

## File: `execution/execute_unary.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func unaryExprExecutor(e ast.UnaryExpr) (expressionExecutor, error) {
	return func(ctx context.Context, options *Options, data *model.Value) (*model.Value, error) {
		ctx = WithExecutorID(ctx, "unaryExpr")
		right, err := ExecuteAST(ctx, e.Right, data, options)
		if err != nil {
			return nil, fmt.Errorf("error evaluating right expression: %w", err)
		}

		switch e.Operator.Kind {
		case lexer.Exclamation:
			boolV, err := right.BoolValue()
			if err != nil {
				return nil, fmt.Errorf("error converting value to boolean: %w", err)
			}
			return model.NewBoolValue(!boolV), nil
		default:
			return nil, fmt.Errorf("unhandled unary operator: %s", e.Operator.Value)
		}
	}, nil
}
```

## File: `execution/execute_unary_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/model/orderedmap"
)

func TestUnary(t *testing.T) {
	t.Run("not", func(t *testing.T) {
		t.Run("literals", func(t *testing.T) {
			t.Run("not true", testCase{
				s:   `!true`,
				out: model.NewBoolValue(false),
			}.run)
			t.Run("not not true", testCase{
				s:   `!!true`,
				out: model.NewBoolValue(true),
			}.run)
			t.Run("not not not true", testCase{
				s:   `!!!true`,
				out: model.NewBoolValue(false),
			}.run)
			t.Run("not false", testCase{
				s:   `!false`,
				out: model.NewBoolValue(true),
			}.run)
			t.Run("not not false", testCase{
				s:   `!!false`,
				out: model.NewBoolValue(false),
			}.run)
			t.Run("not not not false", testCase{
				s:   `!!!false`,
				out: model.NewBoolValue(true),
			}.run)
		})
		t.Run("variables", func(t *testing.T) {
			in := func() *model.Value {
				return model.NewValue(orderedmap.NewMap().
					Set("t", true).
					Set("f", false))
			}
			t.Run("not true", testCase{
				s:    `!t`,
				inFn: in,
				out:  model.NewBoolValue(false),
			}.run)
			t.Run("not not true", testCase{
				s:    `!!t`,
				inFn: in,
				out:  model.NewBoolValue(true),
			}.run)
			t.Run("not not not true", testCase{
				s:    `!!!t`,
				inFn: in,
				out:  model.NewBoolValue(false),
			}.run)
			t.Run("not false", testCase{
				s:    `!f`,
				inFn: in,
				out:  model.NewBoolValue(true),
			}.run)
			t.Run("not not false", testCase{
				s:    `!!f`,
				inFn: in,
				out:  model.NewBoolValue(false),
			}.run)
			t.Run("not not not false", testCase{
				s:    `!!!f`,
				inFn: in,
				out:  model.NewBoolValue(true),
			}.run)
		})
	})
}
```

## File: `execution/func.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
)

var (
	// DefaultFuncCollection is the default collection of functions that can be executed.
	DefaultFuncCollection = NewFuncCollection(
		FuncLen,
		FuncAdd,
		FuncToString,
		FuncToInt,
		FuncToFloat,
		FuncMerge,
		FuncReverse,
		FuncTypeOf,
		FuncMax,
		FuncMin,
		FuncIgnore,
		FuncBase64Encode,
		FuncBase64Decode,
		FuncParse,
		FuncReadFile,
		FuncHas,
		FuncGet,
		FuncContains,
		FuncSum,
		FuncJoin,
		FuncReplace,
	)
)

// ArgsValidator is a function that validates the arguments passed to a function.
type ArgsValidator func(ctx context.Context, name string, args model.Values) error

// ValidateArgsExactly returns an ArgsValidator that validates that the number of arguments passed to a function is exactly the expected number.
func ValidateArgsExactly(expected int) ArgsValidator {
	return func(ctx context.Context, name string, args model.Values) error {
		if len(args) == expected {
			return nil
		}
		return fmt.Errorf("func %q expects exactly %d arguments, got %d", name, expected, len(args))
	}
}

// ValidateArgsMin returns an ArgsValidator that validates that the number of arguments passed to a function is at least the expected number.
func ValidateArgsMin(expected int) ArgsValidator {
	return func(ctx context.Context, name string, args model.Values) error {
		if len(args) >= expected {
			return nil
		}
		return fmt.Errorf("func %q expects at least %d arguments, got %d", name, expected, len(args))
	}
}

// ValidateArgsMax returns an ArgsValidator that validates that the number of arguments passed to a function is at most the expected number.
func ValidateArgsMax(expected int) ArgsValidator {
	return func(ctx context.Context, name string, args model.Values) error {
		if len(args) <= expected {
			return nil
		}
		return fmt.Errorf("func %q expects no more than %d arguments, got %d", name, expected, len(args))
	}
}

// ValidateArgsMinMax returns an ArgsValidator that validates that the number of arguments passed to a function is between the min and max expected numbers.
func ValidateArgsMinMax(min int, max int) ArgsValidator {
	return func(ctx context.Context, name string, args model.Values) error {
		if len(args) >= min && len(args) <= max {
			return nil
		}
		return fmt.Errorf("func %q expects between %d and %d arguments, got %d", name, min, max, len(args))
	}
}

// Func represents a function that can be executed.
type Func struct {
	name          string
	handler       FuncFn
	argsValidator ArgsValidator
}

// Handler returns a FuncFn that can be used to execute the function.
func (f *Func) Handler() FuncFn {
	return func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		if f.argsValidator != nil {
			if err := f.argsValidator(ctx, f.name, args); err != nil {
				return nil, err
			}
		}
		res, err := f.handler(ctx, data, args)
		if err != nil {
			return nil, fmt.Errorf("error execution func %q: %w", f.name, err)
		}
		return res, nil
	}
}

// NewFunc creates a new Func.
func NewFunc(name string, handler FuncFn, argsValidator ArgsValidator) *Func {
	return &Func{
		name:          name,
		handler:       handler,
		argsValidator: argsValidator,
	}
}

// FuncFn is a function that can be executed.
type FuncFn func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error)

// FuncCollection is a collection of functions that can be executed.
type FuncCollection map[string]FuncFn

// NewFuncCollection creates a new FuncCollection with the given functions.
func NewFuncCollection(funcs ...*Func) FuncCollection {
	return FuncCollection{}.Register(funcs...)
}

// Register registers the given functions with the FuncCollection.
func (fc FuncCollection) Register(funcs ...*Func) FuncCollection {
	for _, f := range funcs {
		fc[f.name] = f.Handler()
	}
	return fc
}

// Get returns the function with the given name.
func (fc FuncCollection) Get(name string) (FuncFn, bool) {
	fn, ok := fc[name]
	return fn, ok
}

// Delete deletes the functions with the given names.
func (fc FuncCollection) Delete(names ...string) FuncCollection {
	for _, name := range names {
		delete(fc, name)
	}
	return fc
}

// Copy returns a copy of the FuncCollection.
func (fc FuncCollection) Copy() FuncCollection {
	c := NewFuncCollection()
	for k, v := range fc {
		c[k] = v
	}
	return c
}
```

## File: `execution/func_add.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
)

// FuncAdd is a function that adds the given values together.
var FuncAdd = NewFunc(
	"add",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		var foundInts, foundFloats int
		var intRes int64
		var floatRes float64
		for _, arg := range args {
			if arg.IsFloat() {
				foundFloats++
				v, err := arg.FloatValue()
				if err != nil {
					return nil, fmt.Errorf("error getting float value: %w", err)
				}
				floatRes += v
				continue
			}
			if arg.IsInt() {
				foundInts++
				v, err := arg.IntValue()
				if err != nil {
					return nil, fmt.Errorf("error getting int value: %w", err)
				}
				intRes += v
				continue
			}
			return nil, fmt.Errorf("expected int or float, got %s", arg.Type())
		}
		if foundFloats > 0 {
			return model.NewFloatValue(floatRes + float64(intRes)), nil
		}
		return model.NewIntValue(intRes), nil
	},
	ValidateArgsMin(1),
)
```

## File: `execution/func_add_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/model/orderedmap"
)

func TestFuncAdd(t *testing.T) {
	t.Run("int", testCase{
		s:   `add(1, 2, 3)`,
		out: model.NewIntValue(6),
	}.run)
	t.Run("float", testCase{
		s:   `add(1f, 2.5, 3.5)`,
		out: model.NewFloatValue(7),
	}.run)
	t.Run("mixed", testCase{
		s:   `add(1, 2f)`,
		out: model.NewFloatValue(3),
	}.run)
	t.Run("properties", func(t *testing.T) {
		in := func() *model.Value {
			return model.NewValue(orderedmap.NewMap().
				Set("numbers", orderedmap.NewMap().
					Set("one", 1).
					Set("two", 2).
					Set("three", 3)).
				Set("nums", []any{1, 2, 3}))
		}
		t.Run("nested props", testCase{
			inFn: in,
			s:    `numbers.one + add(numbers.two, numbers.three)`,
			out:  model.NewIntValue(6),
		}.run)
		t.Run("add on end of chain", testCase{
			inFn: in,
			s:    `numbers.one + numbers.add(two, three)`,
			out:  model.NewIntValue(6),
		}.run)
		t.Run("add with map and spread on slice with $this addition and grouping", testCase{
			inFn: in,
			s:    `add(nums.map(($this + 1))...)`,
			out:  model.NewIntValue(9),
		}.run)
		t.Run("add with map and spread on slice with $this addition", testCase{
			inFn: in,
			s:    `add(nums.map($this + 1 - 2)...)`,
			out:  model.NewIntValue(3),
		}.run)
	})
}
```

## File: `execution/func_base64.go`
```go
package execution

import (
	"context"
	"encoding/base64"

	"github.com/tomwright/dasel/v3/model"
)

// FuncBase64Encode base64 encodes the given value.
var FuncBase64Encode = NewFunc(
	"base64e",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		arg := args[0]
		strVal, err := arg.StringValue()
		if err != nil {
			return nil, err
		}
		out := base64.StdEncoding.EncodeToString([]byte(strVal))
		return model.NewStringValue(out), nil
	},
	ValidateArgsExactly(1),
)

// FuncBase64Decode base64 decodes the given value.
var FuncBase64Decode = NewFunc(
	"base64d",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		arg := args[0]
		strVal, err := arg.StringValue()
		if err != nil {
			return nil, err
		}
		out, err := base64.StdEncoding.DecodeString(strVal)
		if err != nil {
			return nil, err
		}
		return model.NewStringValue(string(out)), nil
	},
	ValidateArgsExactly(1),
)
```

## File: `execution/func_contains.go`
```go
package execution

import (
	"context"
	"fmt"
	"github.com/tomwright/dasel/v3/model"
)

// FuncContains is a function that returns the highest number.
var FuncContains = NewFunc(
	"contains",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		var contains bool

		target := args[0]

		length, err := data.SliceLen()
		if err != nil {
			return nil, fmt.Errorf("error getting slice length: %w", err)
		}

		for i := 0; i < length; i++ {
			v, err := data.GetSliceIndex(i)
			if err != nil {
				return nil, fmt.Errorf("error getting slice index %d: %w", i, err)
			}
			matches, err := v.Equal(target)
			if err != nil {
				continue
			}
			matchesBool, err := matches.BoolValue()
			if err != nil {
				return nil, err
			}
			if matchesBool {
				contains = true
				break
			}
		}

		return model.NewBoolValue(contains), nil
	},
	ValidateArgsExactly(1),
)
```

## File: `execution/func_contains_test.go`
```go
package execution_test

import (
	"github.com/tomwright/dasel/v3/model"
	_ "github.com/tomwright/dasel/v3/parsing/json"
	"testing"
)

func TestFuncContains(t *testing.T) {
	t.Run("array true", testCase{
		s:   `[1,2,3,4,5].contains(3)`,
		out: model.NewBoolValue(true),
	}.run)
	t.Run("array false", testCase{
		s:   `[1,2,3,4,5].contains(6)`,
		out: model.NewBoolValue(false),
	}.run)
}
```

## File: `execution/func_get.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
)

// FuncGet is a function returns the value at the given key/index.
var FuncGet = NewFunc(
	"get",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {

		arg := args[0]

		switch arg.Type() {
		case model.TypeInt:
			index, err := arg.IntValue()
			if err != nil {
				return nil, err
			}
			return data.GetSliceIndex(int(index))
		case model.TypeString:
			key, err := arg.StringValue()
			if err != nil {
				return nil, err
			}
			return data.GetMapKey(key)
		default:
			return nil, fmt.Errorf("get expects string or int argument")
		}
	},
	ValidateArgsExactly(1),
)
```

## File: `execution/func_get_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
	_ "github.com/tomwright/dasel/v3/parsing/json"
)

func TestFuncGet(t *testing.T) {
	t.Run("returns array element", testCase{
		s:   `[1,2,3,4,5].get(3)`,
		out: model.NewIntValue(4),
	}.run)
	t.Run("returns map key", testCase{
		s:   `{"a": 3, "b": 4, "c": 5}.get("b")`,
		out: model.NewIntValue(4),
	}.run)
	t.Run("coalesce with invalid map accessor", testCase{
		s:   `{}.get("a") ?? "missing"`,
		out: model.NewStringValue("missing"),
	}.run)
	t.Run("returns null when string accessor used on slice", testCase{
		s:   `[].get(0) ?? "missing"`,
		out: model.NewStringValue("missing"),
	}.run)
}
```

## File: `execution/func_has.go`
```go
package execution

import (
	"context"
	"fmt"
	"github.com/tomwright/dasel/v3/model"
)

// FuncHas is a function that true or false if the input has the given key/index.
var FuncHas = NewFunc(
	"has",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {

		arg := args[0]

		switch arg.Type() {
		case model.TypeInt:
			// Given key is int, expect a slice.
			if data.Type() != model.TypeSlice {
				return model.NewBoolValue(false), nil
			}
			index, err := arg.IntValue()
			if err != nil {
				return nil, err
			}
			sliceLen, err := data.SliceLen()
			if err != nil {
				return nil, err
			}
			return model.NewBoolValue(index >= 0 && index < int64(sliceLen)), nil
		case model.TypeString:
			// Given key is string, expect a map.
			if data.Type() != model.TypeMap {
				return model.NewBoolValue(false), nil
			}
			key, err := arg.StringValue()
			if err != nil {
				return nil, err
			}
			exists, err := data.MapKeyExists(key)
			if err != nil {
				return nil, err
			}
			return model.NewBoolValue(exists), nil
		default:
			return nil, fmt.Errorf("has expects string or int argument")
		}
	},
	ValidateArgsMin(1),
)
```

## File: `execution/func_has_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestFuncHas(t *testing.T) {
	t.Run("index in range", testCase{
		s:   `[1,2,3].has(0)`,
		out: model.NewBoolValue(true),
	}.run)
	t.Run("negative index", testCase{
		s:   `[1,2,3].has(-1)`,
		out: model.NewBoolValue(false),
	}.run)
	t.Run("index overflow", testCase{
		s:   `[1,2,3].has(3)`,
		out: model.NewBoolValue(false),
	}.run)
	t.Run("index string", testCase{
		s:   `[1,2,3].has("foo")`,
		out: model.NewBoolValue(false),
	}.run)
	t.Run("has map key", testCase{
		s:   `{"x":1}.has("x")`,
		out: model.NewBoolValue(true),
	}.run)
	t.Run("does not have map key", testCase{
		s:   `{"x":1}.has("y")`,
		out: model.NewBoolValue(false),
	}.run)
	t.Run("does not have map index", testCase{
		s:   `{"x":1}.has(1)`,
		out: model.NewBoolValue(false),
	}.run)
}
```

## File: `execution/func_ignore.go`
```go
package execution

import (
	"context"
	"github.com/tomwright/dasel/v3/model"
)

// FuncIgnore is a function that ignores the value, causing it to be rejected from a branch.
var FuncIgnore = NewFunc(
	"ignore",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		data.MarkAsIgnore()
		return data, nil
	},
	ValidateArgsExactly(0),
)
```

## File: `execution/func_join.go`
```go
package execution

import (
	"context"
	"fmt"
	"strings"

	"github.com/tomwright/dasel/v3/model"
)

// FuncJoin is a function that joins the given data or args to a string.
var FuncJoin = NewFunc(
	"join",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		separator, err := args[0].StringValue()
		if err != nil {
			return nil, fmt.Errorf("join expects a string separator as the first argument: %w", err)
		}

		var valuesToJoin []string

		if len(args) == 2 && args[1].IsSlice() {
			if err := args[1].RangeSlice(func(i int, value *model.Value) error {
				strVal, err := value.StringValue()
				if err != nil {
					return fmt.Errorf("could not read string value of index %d: %w", i, err)
				}
				valuesToJoin = append(valuesToJoin, strVal)
				return nil
			}); err != nil {
				return nil, err
			}
		} else if len(args) > 1 {
			// Join the args
			for i := 1; i < len(args); i++ {
				strVal, err := args[i].StringValue()
				if err != nil {
					return nil, fmt.Errorf("could not read string value of argument index %d: %w", i, err)
				}
				valuesToJoin = append(valuesToJoin, strVal)
			}
		} else {
			if err := data.RangeSlice(func(i int, value *model.Value) error {
				strVal, err := value.StringValue()
				if err != nil {
					return fmt.Errorf("could not read string value of index %d: %w", i, err)
				}
				valuesToJoin = append(valuesToJoin, strVal)
				return nil
			}); err != nil {
				return nil, err
			}
		}

		joined := strings.Join(valuesToJoin, separator)

		return model.NewStringValue(joined), nil
	},
	ValidateArgsMin(1),
)
```

## File: `execution/func_join_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
	_ "github.com/tomwright/dasel/v3/parsing/json"
)

func TestFuncJoin(t *testing.T) {
	t.Run("chained input", testCase{
		s:   `["a","b","c"].join(",")`,
		out: model.NewStringValue("a,b,c"),
	}.run)
	t.Run("vararg input", testCase{
		s:   `join(",", "a", "b", "c")`,
		out: model.NewStringValue("a,b,c"),
	}.run)
	t.Run("array input", testCase{
		s:   `join(",", ["a", "b", "c"])`,
		out: model.NewStringValue("a,b,c"),
	}.run)
}
```

## File: `execution/func_len.go`
```go
package execution

import (
	"context"
	"github.com/tomwright/dasel/v3/model"
)

// FuncLen is a function that returns the length of the given value.
var FuncLen = NewFunc(
	"len",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		arg := args[0]

		l, err := arg.Len()
		if err != nil {
			return nil, err
		}

		return model.NewIntValue(int64(l)), nil
	},
	ValidateArgsExactly(1),
)
```

## File: `execution/func_len_test.go`
```go
package execution_test

import (
	"github.com/tomwright/dasel/v3/model"
	_ "github.com/tomwright/dasel/v3/parsing/json"
	"testing"
)

func TestFuncLen(t *testing.T) {
	t.Run("array", testCase{
		s:   `len([1,2,3])`,
		out: model.NewIntValue(3),
	}.run)
	t.Run("object", testCase{
		s:   `len({"foo":1,"bar":2,"baz":3})`,
		out: model.NewIntValue(3),
	}.run)
	t.Run("string", testCase{
		s:   `len("hello")`,
		out: model.NewIntValue(5),
	}.run)
}
```

## File: `execution/func_max.go`
```go
package execution

import (
	"context"
	"github.com/tomwright/dasel/v3/model"
)

// FuncMax is a function that returns the highest number.
var FuncMax = NewFunc(
	"max",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		res := model.NewNullValue()
		for _, arg := range args {
			if res.IsNull() {
				res = arg
				continue
			}
			gt, err := arg.GreaterThan(res)
			if err != nil {
				return nil, err
			}
			gtBool, err := gt.BoolValue()
			if err != nil {
				return nil, err
			}
			if gtBool {
				res = arg
			}
		}
		return res, nil
	},
	ValidateArgsMin(1),
)
```

## File: `execution/func_max_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestFuncMax(t *testing.T) {
	t.Run("int", testCase{
		s:   `max(1, 2, 3)`,
		out: model.NewIntValue(3),
	}.run)
	t.Run("float", testCase{
		s:   `max(1f, 2.5, 3.5)`,
		out: model.NewFloatValue(3.5),
	}.run)
	t.Run("mixed", testCase{
		s:   `max(1, 2f)`,
		out: model.NewFloatValue(2),
	}.run)
}
```

## File: `execution/func_merge.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
)

// FuncMerge is a function that merges two or more items together.
var FuncMerge = NewFunc(
	"merge",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		if len(args) == 1 {
			return args[0], nil
		}

		expectedType := args[0].Type()

		switch expectedType {
		case model.TypeMap:
			break
		default:
			return nil, fmt.Errorf("merge exects a map, found %s", expectedType)
		}

		// Validate types match
		for _, a := range args {
			if a.Type() != expectedType {
				return nil, fmt.Errorf("merge expects all arguments to be of the same type. expected %s, got %s", expectedType.String(), a.Type().String())
			}
		}

		base := model.NewMapValue()

		for i := 0; i < len(args); i++ {
			next := args[i]

			nextKVs, err := next.MapKeyValues()
			if err != nil {
				return nil, fmt.Errorf("merge failed to extract key values for arg %d: %w", i, err)
			}

			for _, kv := range nextKVs {
				if err := base.SetMapKey(kv.Key, kv.Value); err != nil {
					return nil, fmt.Errorf("merge failed to set map key %s: %w", kv.Key, err)
				}
			}
		}

		return base, nil
	},
	ValidateArgsMin(1),
)
```

## File: `execution/func_merge_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestFuncMerge(t *testing.T) {
	t.Run("shallow", testCase{
		inFn: func() *model.Value {
			a := model.NewMapValue()
			if err := a.SetMapKey("foo", model.NewStringValue("afoo")); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			if err := a.SetMapKey("bar", model.NewStringValue("abar")); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			b := model.NewMapValue()
			if err := b.SetMapKey("bar", model.NewStringValue("bbar")); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			if err := b.SetMapKey("baz", model.NewStringValue("bbaz")); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			res := model.NewMapValue()
			if err := res.SetMapKey("a", a); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			if err := res.SetMapKey("b", b); err != nil {
				t.Errorf("unexpected error: %v", err)
			}
			return res
		},
		s: `merge(a, b)`,
		outFn: func() *model.Value {
			b := model.NewMapValue()
			if err := b.SetMapKey("foo", model.NewStringValue("afoo")); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := b.SetMapKey("bar", model.NewStringValue("bbar")); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := b.SetMapKey("baz", model.NewStringValue("bbaz")); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return b
		},
	}.run)
}
```

## File: `execution/func_min.go`
```go
package execution

import (
	"context"
	"github.com/tomwright/dasel/v3/model"
)

// FuncMin is a function that returns the smalled number.
var FuncMin = NewFunc(
	"min",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		res := model.NewNullValue()
		for _, arg := range args {
			if res.IsNull() {
				res = arg
				continue
			}
			lt, err := arg.LessThan(res)
			if err != nil {
				return nil, err
			}
			ltBool, err := lt.BoolValue()
			if err != nil {
				return nil, err
			}
			if ltBool {
				res = arg
			}
		}
		return res, nil
	},
	ValidateArgsMin(1),
)
```

## File: `execution/func_min_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestFuncMin(t *testing.T) {
	t.Run("int", testCase{
		s:   `min(1, 2, 3)`,
		out: model.NewIntValue(1),
	}.run)
	t.Run("float", testCase{
		s:   `min(1f, 2.5, 3.5)`,
		out: model.NewFloatValue(1),
	}.run)
	t.Run("mixed", testCase{
		s:   `min(1, 2f)`,
		out: model.NewIntValue(1),
	}.run)
}
```

## File: `execution/func_parse.go`
```go
package execution

import (
	"context"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
)

// FuncParse parses the given data at runtime.
var FuncParse = NewFunc(
	"parse",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		var format parsing.Format
		var content []byte
		{
			strVal, err := args[0].StringValue()
			if err != nil {
				return nil, err
			}
			format = parsing.Format(strVal)
		}
		{
			strVal, err := args[1].StringValue()
			if err != nil {
				return nil, err
			}
			content = []byte(strVal)
		}

		reader, err := format.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			return nil, err
		}

		doc, err := reader.Read(content)
		if err != nil {
			return nil, err
		}

		return doc, nil
	},
	ValidateArgsExactly(2),
)
```

## File: `execution/func_parse_test.go`
```go
package execution_test

import (
	"github.com/tomwright/dasel/v3/model"
	_ "github.com/tomwright/dasel/v3/parsing/json"
	"testing"
)

func TestFuncParse(t *testing.T) {
	t.Run("json", testCase{
		s:   `parse('json', '{"foo":"bar"}').foo`,
		out: model.NewStringValue("bar"),
	}.run)
}
```

## File: `execution/func_readfile.go`
```go
package execution

import (
	"context"
	"fmt"
	"github.com/tomwright/dasel/v3/model"
	"io"
	"os"
)

// FuncReadFile reads the given filepath at runtime.
var FuncReadFile = NewFunc(
	"readFile",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		filepath, err := args[0].StringValue()
		if err != nil {
			return nil, fmt.Errorf("readFile: %w", err)
		}

		f, err := os.Open(filepath)
		if err != nil {
			return nil, fmt.Errorf("readFile: %w", err)
		}
		defer func() {
			_ = f.Close()
		}()

		fileBytes, err := io.ReadAll(f)
		if err != nil {
			return nil, fmt.Errorf("readFile: %w", err)
		}

		return model.NewStringValue(string(fileBytes)), nil
	},
	ValidateArgsExactly(1),
)
```

## File: `execution/func_replace.go`
```go
package execution

import (
	"context"
	"strings"

	"github.com/tomwright/dasel/v3/model"
)

// FuncReplace is a function that replaces all occurrences of a substring with another string.
var FuncReplace = NewFunc(
	"replace",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		inputData := data
		if len(args)%2 != 0 {
			inputData = args[0]
			args = args[1:]
		}

		argStrings := make([]string, len(args))
		for i, arg := range args {
			s, err := arg.StringValue()
			if err != nil {
				return nil, err
			}
			argStrings[i] = s
		}
		replacer := strings.NewReplacer(argStrings...)

		inputString, err := inputData.StringValue()
		if err != nil {
			return nil, err
		}

		outputString := replacer.Replace(inputString)

		return model.NewStringValue(outputString), nil
	},
	ValidateArgsMin(2),
)
```

## File: `execution/func_replace_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestFuncReplace(t *testing.T) {
	t.Run("input arg", testCase{
		s:   `replace("hello world", "world", "there")`,
		out: model.NewStringValue("hello there"),
	}.run)

	t.Run("multiple data arg", testCase{
		s:   `replace("hello world", "o", "0", "l", "1")`,
		out: model.NewStringValue("he110 w0r1d"),
	}.run)

	t.Run("data arg", testCase{
		s:   `"hello world".replace("o", "0")`,
		out: model.NewStringValue("hell0 w0rld"),
	}.run)

	t.Run("multiple data arg", testCase{
		s:   `"hello world".replace("o", "0", "h", "H")`,
		out: model.NewStringValue("Hell0 w0rld"),
	}.run)

	t.Run("data arg with input arg ignores data arg", testCase{
		s:   `"bob".replace("hello world", "o", "0", "world", "there")`,
		out: model.NewStringValue("hell0 there"),
	}.run)
}
```

## File: `execution/func_reverse.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
)

// FuncReverse is a function that reverses the input.
var FuncReverse = NewFunc(
	"reverse",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		arg := args[0]

		switch arg.Type() {
		case model.TypeString:
			return arg.StringIndexRange(-1, 0)
		case model.TypeSlice:
			return arg.SliceIndexRange(-1, 0)
		default:
			return nil, fmt.Errorf("reverse expects a slice or string, got %s", arg.Type())
		}
	},
	ValidateArgsExactly(1),
)
```

## File: `execution/func_reverse_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestFuncReverse(t *testing.T) {
	t.Run("array", testCase{
		s: `reverse([1, 2, 3])`,
		outFn: func() *model.Value {
			res := model.NewSliceValue()
			if err := res.Append(model.NewIntValue(3)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := res.Append(model.NewIntValue(2)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if err := res.Append(model.NewIntValue(1)); err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			return res
		},
	}.run)

	t.Run("string", testCase{
		s:   `reverse("hello")`,
		out: model.NewStringValue("olleh"),
	}.run)
}
```

## File: `execution/func_sum.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
)

// FuncSum is a function that returns the sum of the given numbers.
var FuncSum = NewFunc(
	"sum",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		returnType := model.TypeInt

		for _, arg := range args {
			if arg.IsInt() {
				continue
			}
			if arg.IsFloat() {
				returnType = model.TypeFloat
				break
			}
			return nil, fmt.Errorf("cannot sum non-numeric value of type %s", arg.Type().String())
		}

		switch returnType {
		case model.TypeInt:
			var sum int64
			for _, arg := range args {
				if arg.IsInt() {
					intVal, err := arg.IntValue()
					if err != nil {
						return nil, err
					}
					sum += intVal
					continue
				}

				floatVal, err := arg.FloatValue()
				if err != nil {
					return nil, err
				}
				sum += int64(floatVal)
			}
			return model.NewIntValue(sum), nil
		case model.TypeFloat:
			var sum float64
			for _, arg := range args {
				if arg.IsInt() {
					intVal, err := arg.IntValue()
					if err != nil {
						return nil, err
					}
					sum += float64(intVal)
					continue
				}

				floatVal, err := arg.FloatValue()
				if err != nil {
					return nil, err
				}
				sum += floatVal
			}
			return model.NewFloatValue(sum), nil
		default:
			return nil, fmt.Errorf("unsupported return type %s", returnType.String())
		}
	},
	ValidateArgsMin(1),
)
```

## File: `execution/func_sum_test.go`
```go
package execution_test

import (
	"github.com/tomwright/dasel/v3/model"
	"testing"
)

func TestFuncSum(t *testing.T) {
	t.Run("int", testCase{
		s:   `sum(1, 2, 3)`,
		out: model.NewIntValue(6),
	}.run)
	t.Run("float", testCase{
		s:   `sum(1.1, 2.2, 3.3)`,
		out: model.NewFloatValue(6.6),
	}.run)
	t.Run("negative int", testCase{
		s:   `sum(-1, -2, -3)`,
		out: model.NewIntValue(-6),
	}.run)
	t.Run("negative float", testCase{
		s:   `sum(-1.1, -2.2, -3.3)`,
		out: model.NewFloatValue(-6.6),
	}.run)
	t.Run("using int and float together returns float", testCase{
		s:   `sum(1, 1.1)`,
		out: model.NewFloatValue(2.1),
	}.run)
}
```

## File: `execution/func_to_float.go`
```go
package execution

import (
	"context"
	"fmt"
	"strconv"

	"github.com/tomwright/dasel/v3/model"
)

// FuncToFloat is a function that converts the given value to a string.
var FuncToFloat = NewFunc(
	"toFloat",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		switch args[0].Type() {
		case model.TypeString:
			stringValue, err := args[0].StringValue()
			if err != nil {
				return nil, err
			}

			i, err := strconv.ParseFloat(stringValue, 64)
			if err != nil {
				return nil, err
			}

			return model.NewFloatValue(i), nil
		case model.TypeInt:
			i, err := args[0].IntValue()
			if err != nil {
				return nil, err
			}
			return model.NewFloatValue(float64(i)), nil
		case model.TypeFloat:
			return args[0], nil
		case model.TypeBool:
			i, err := args[0].BoolValue()
			if err != nil {
				return nil, err
			}
			if i {
				return model.NewFloatValue(1), nil
			}
			return model.NewFloatValue(0), nil
		default:
			return nil, fmt.Errorf("cannot convert %s to float", args[0].Type())
		}
	},
	ValidateArgsExactly(1),
)
```

## File: `execution/func_to_float_test.go`
```go
package execution_test

import (
	"github.com/tomwright/dasel/v3/model"
	"testing"
)

func TestFuncToFloat(t *testing.T) {
	t.Run("string", testCase{
		s:   `toFloat("1.1")`,
		out: model.NewFloatValue(1.1),
	}.run)
	t.Run("int", testCase{
		s:   `toFloat(1)`,
		out: model.NewFloatValue(1),
	}.run)
	t.Run("float", testCase{
		s:   `toFloat(1.1)`,
		out: model.NewFloatValue(1.1),
	}.run)
	t.Run("bool", testCase{
		s:   `toFloat(true)`,
		out: model.NewFloatValue(1),
	}.run)
}
```

## File: `execution/func_to_int.go`
```go
package execution

import (
	"context"
	"fmt"
	"strconv"

	"github.com/tomwright/dasel/v3/model"
)

// FuncToInt is a function that converts the given value to a string.
var FuncToInt = NewFunc(
	"toInt",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		switch args[0].Type() {
		case model.TypeString:
			stringValue, err := args[0].StringValue()
			if err != nil {
				return nil, err
			}

			i, err := strconv.ParseInt(stringValue, 10, 64)
			if err != nil {
				return nil, err
			}

			return model.NewIntValue(i), nil
		case model.TypeInt:
			return args[0], nil
		case model.TypeFloat:
			i, err := args[0].FloatValue()
			if err != nil {
				return nil, err
			}
			return model.NewIntValue(int64(i)), nil
		case model.TypeBool:
			i, err := args[0].BoolValue()
			if err != nil {
				return nil, err
			}
			if i {
				return model.NewIntValue(1), nil
			}
			return model.NewIntValue(0), nil
		default:
			return nil, fmt.Errorf("cannot convert %s to int", args[0].Type())
		}
	},
	ValidateArgsExactly(1),
)
```

## File: `execution/func_to_int_test.go`
```go
package execution_test

import (
	"github.com/tomwright/dasel/v3/model"
	"testing"
)

func TestFuncToInt(t *testing.T) {
	t.Run("string", testCase{
		s:   `toInt("2")`,
		out: model.NewIntValue(2),
	}.run)
	t.Run("int", testCase{
		s:   `toInt(1)`,
		out: model.NewIntValue(1),
	}.run)
	t.Run("float", testCase{
		s:   `toInt(1.1)`,
		out: model.NewIntValue(1),
	}.run)
	t.Run("bool", testCase{
		s:   `toInt(true)`,
		out: model.NewIntValue(1),
	}.run)
}
```

## File: `execution/func_to_string.go`
```go
package execution

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
)

// FuncToString is a function that converts the given value to a string.
var FuncToString = NewFunc(
	"toString",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		switch args[0].Type() {
		case model.TypeString:
			stringValue, err := args[0].StringValue()
			if err != nil {
				return nil, err
			}
			model.NewStringValue(stringValue)
			return args[0], nil
		case model.TypeInt:
			i, err := args[0].IntValue()
			if err != nil {
				return nil, err
			}
			return model.NewStringValue(fmt.Sprintf("%d", i)), nil
		case model.TypeFloat:
			i, err := args[0].FloatValue()
			if err != nil {
				return nil, err
			}
			return model.NewStringValue(fmt.Sprintf("%g", i)), nil
		case model.TypeBool:
			i, err := args[0].BoolValue()
			if err != nil {
				return nil, err
			}
			return model.NewStringValue(fmt.Sprintf("%v", i)), nil
		default:
			return nil, fmt.Errorf("cannot convert %s to string", args[0].Type())
		}
	},
	ValidateArgsExactly(1),
)
```

## File: `execution/func_to_string_test.go`
```go
package execution_test

import (
	"github.com/tomwright/dasel/v3/model"
	"testing"
)

func TestFuncToString(t *testing.T) {
	t.Run("string", testCase{
		s:   `toString("Hello")`,
		out: model.NewStringValue("Hello"),
	}.run)
	t.Run("int", testCase{
		s:   `toString(1)`,
		out: model.NewStringValue("1"),
	}.run)
	t.Run("float", testCase{
		s:   `toString(1.1)`,
		out: model.NewStringValue("1.1"),
	}.run)
	t.Run("bool", testCase{
		s:   `toString(true)`,
		out: model.NewStringValue("true"),
	}.run)
}
```

## File: `execution/func_type_of.go`
```go
package execution

import (
	"context"
	"github.com/tomwright/dasel/v3/model"
)

// FuncTypeOf is a function that returns the type of the first argument as a string.
var FuncTypeOf = NewFunc(
	"typeOf",
	func(ctx context.Context, data *model.Value, args model.Values) (*model.Value, error) {
		return model.NewStringValue(args[0].Type().String()), nil
	},
	ValidateArgsExactly(1),
)
```

## File: `execution/func_type_of_test.go`
```go
package execution_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestFuncTypeOf(t *testing.T) {
	t.Run("string", testCase{
		s:   `typeOf("hello")`,
		out: model.NewStringValue("string"),
	}.run)
	t.Run("int", testCase{
		s:   `typeOf(123)`,
		out: model.NewStringValue("int"),
	}.run)
	t.Run("float", testCase{
		s:   `typeOf(12.3)`,
		out: model.NewStringValue("float"),
	}.run)
	t.Run("bool", testCase{
		s:   `typeOf(true)`,
		out: model.NewStringValue("bool"),
	}.run)
	t.Run("array", testCase{
		s:   `typeOf([])`,
		out: model.NewStringValue("array"),
	}.run)
	t.Run("map", testCase{
		s:   `typeOf({})`,
		out: model.NewStringValue("map"),
	}.run)
	t.Run("null", testCase{
		s:   `typeOf(null)`,
		out: model.NewStringValue("null"),
	}.run)
}
```

## File: `execution/options.go`
```go
package execution

import "github.com/tomwright/dasel/v3/model"

// ExecuteOptionFn is a function that can be used to set options on the execution of the selector.
type ExecuteOptionFn func(*Options)

// Options contains the options for the execution of the selector.
type Options struct {
	Funcs    FuncCollection
	Vars     map[string]*model.Value
	Unstable bool
}

// NewOptions creates a new Options struct with the given options.
func NewOptions(opts ...ExecuteOptionFn) *Options {
	o := &Options{
		Funcs: DefaultFuncCollection,
		Vars:  map[string]*model.Value{},
	}
	for _, opt := range opts {
		if opt == nil {
			continue
		}
		opt(o)
	}
	return o
}

// WithFuncs sets the functions that can be used in the selector.
func WithFuncs(fc FuncCollection) ExecuteOptionFn {
	return func(o *Options) {
		o.Funcs = fc
	}
}

// WithVariable sets a variable for use in the selector.
func WithVariable(key string, val *model.Value) ExecuteOptionFn {
	return func(o *Options) {
		o.Vars[key] = val
	}
}

// WithUnstable allows access to potentially unstable features.
func WithUnstable() ExecuteOptionFn {
	return func(o *Options) {
		o.Unstable = true
	}
}

// WithoutUnstable disallows access to potentially unstable features.
func WithoutUnstable() ExecuteOptionFn {
	return func(o *Options) {
		o.Unstable = false
	}
}
```

## File: `execution/README.md`
```markdown
# Execution

The execution package accepts a `model.Value`, parses a selector and executes the resulting AST on the value.
```

## File: `internal/version.go`
```go
package internal

import (
	"runtime/debug"
)

// Version represents the current version of dasel.
// The real version number is injected at build time using ldflags.
var Version = "development"

func init() {
	// Version is set by ldflags on build.
	if Version != "development" {
		return
	}

	info, ok := debug.ReadBuildInfo()
	if !ok {
		return
	}

	// https://github.com/golang/go/issues/29228
	if info.Main.Version == "(devel)" || info.Main.Version == "" {
		return
	}

	Version += "-" + info.Main.Version
}
```

## File: `internal/cli/command.go`
```go
package cli

import (
	"errors"
	"io"
	"reflect"

	"github.com/alecthomas/kong"
	"github.com/tomwright/dasel/v3/internal"
)

var ErrNoArgsGiven = errors.New("no arguments given")

type Globals struct {
	Stdin       io.Reader        `kong:"-"`
	Stdout      io.Writer        `kong:"-"`
	Stderr      io.Writer        `kong:"-"`
	helpPrinter kong.HelpPrinter `kong:"-"`
}

type CLI struct {
	Globals

	Query       QueryCmd       `cmd:"" default:"withargs" help:"[default] Execute a query"`
	Version     VersionCmd     `cmd:"" help:"Print the version"`
	Interactive InteractiveCmd `cmd:"" help:"Start an interactive session (alpha)"`
}

func MustRun(stdin io.Reader, stdout, stderr io.Writer) {
	ctx, err := Run(stdin, stdout, stderr)
	if err == nil {
		return
	}

	if ctx == nil {
		panic(err)
	}

	ctx.Errorf("%s", err.Error())
	if errors.Is(err, ErrNoArgsGiven) {
		if err := ctx.PrintUsage(false); err != nil {
			panic(err)
		}
	}

	ctx.Exit(1)
}

func Run(stdin io.Reader, stdout, stderr io.Writer) (*kong.Context, error) {
	cli := &CLI{
		Globals: Globals{
			Stdin:       stdin,
			Stdout:      stdout,
			Stderr:      stderr,
			helpPrinter: kong.DefaultHelpPrinter,
		},
	}

	ctx := kong.Parse(
		cli,
		kong.Name("dasel"),
		kong.Description("Query and modify data structures from the command line."),
		kong.UsageOnError(),
		kong.ConfigureHelp(kong.HelpOptions{Compact: true}),
		kong.Vars{
			"version": internal.Version,
		},
		kong.Bind(&cli.Globals),
		kong.TypeMapper(reflect.TypeFor[variables](), &variableMapper{}),
		kong.TypeMapper(reflect.TypeFor[extReadWriteFlags](), &extReadWriteFlagMapper{}),
		kong.OptionFunc(func(k *kong.Kong) error {
			k.Stdout = cli.Stdout
			k.Stderr = cli.Stderr
			return nil
		}),
		kong.Help(cli.helpPrinter),
	)
	err := ctx.Run()
	return ctx, err
}
```

## File: `internal/cli/command_test.go`
```go
package cli_test

import (
	"bytes"
	"errors"
	"os"
	"reflect"
	"testing"

	"github.com/tomwright/dasel/v3/internal/cli"
)

func runDasel(args []string, in []byte) ([]byte, []byte, error) {
	stdOut := bytes.NewBuffer([]byte{})
	stdErr := bytes.NewBuffer([]byte{})
	stdIn := bytes.NewReader(in)

	originalArgs := os.Args
	defer func() {
		os.Args = originalArgs
	}()

	os.Args = append([]string{"dasel", "query"}, args...)

	_, err := cli.Run(stdIn, stdOut, stdErr)

	return stdOut.Bytes(), stdErr.Bytes(), err
}

type testCase struct {
	args   []string
	in     []byte
	stdout []byte
	stderr []byte
	err    error
}

func runTest(tc testCase) func(t *testing.T) {
	return func(t *testing.T) {
		if tc.stdout == nil {
			tc.stdout = []byte{}
		}
		if tc.stderr == nil {
			tc.stderr = []byte{}
		}

		gotStdOut, gotStdErr, gotErr := runDasel(tc.args, tc.in)
		if !errors.Is(gotErr, tc.err) && !errors.Is(tc.err, gotErr) {
			t.Errorf("expected error %v, got %v", tc.err, gotErr)
			return
		}

		if !reflect.DeepEqual(tc.stderr, gotStdErr) {
			t.Errorf("expected stderr %s, got %s", string(tc.stderr), string(gotStdErr))
		}

		if !reflect.DeepEqual(tc.stdout, gotStdOut) {
			t.Errorf("expected stdout %s, got %s", string(tc.stdout), string(gotStdOut))
		}
	}
}

func TestRun(t *testing.T) {
	t.Run("complex set", func(t *testing.T) {
		t.Run("set nested with spread", runTest(testCase{
			args: []string{"-i", "json", "-o", "json", "--root", `user = {user..., name: {"first": $this.user.name, "last": "Doe"}}`},
			in:   []byte(`{"user": {"name": "John"}}`),
			stdout: []byte(`{
    "user": {
        "name": {
            "first": "John",
            "last": "Doe"
        }
    }
}
`),
			stderr: nil,
			err:    nil,
		}))
		t.Run("set nested", runTest(testCase{
			args: []string{"-i", "json", "-o", "json", "--root", `user.name = {"first": user.name, "last": "Doe"}`},
			in:   []byte(`{"user": {"name": "John"}}`),
			stdout: []byte(`{
    "user": {
        "name": {
            "first": "John",
            "last": "Doe"
        }
    }
}
`),
			stderr: nil,
			err:    nil,
		}))
		t.Run("set nested with localised group", runTest(testCase{
			args: []string{"-i", "json", "-o", "json", "--root", `user.(name = {"first": name, "last": "Doe"})`},
			in:   []byte(`{"user": {"name": "John"}}`),
			stdout: []byte(`{
    "user": {
        "name": {
            "first": "John",
            "last": "Doe"
        }
    }
}
`),
			stderr: nil,
			err:    nil,
		}))
		t.Run("set recursive descent", func(t *testing.T) {

			t.Run("property", runTest(testCase{
				args: []string{"-i", "json", "-o", "json", "--root", `$root..x.each($this = $this+1)`},
				in:   []byte(`[{"x":1},{"x":2},{"x":3}]`),
				stdout: []byte(`[
    {
        "x": 2
    },
    {
        "x": 3
    },
    {
        "x": 4
    }
]
`),
				stderr: nil,
				err:    nil,
			}))

			t.Run("index", runTest(testCase{
				args: []string{"-i", "json", "-o", "json", "--root", `$root..[1].each($this = $this+1)`},
				in:   []byte(`[ {"x":[1,2,3]} , {"y":[4,5,6]} , {"z":[7,8,9]} ]`),
				stdout: []byte(`[
    {
        "x": [
            1,
            3,
            3
        ]
    },
    {
        "y": [
            4,
            6,
            6
        ]
    },
    {
        "z": [
            7,
            9,
            9
        ]
    }
]
`),
				stderr: nil,
				err:    nil,
			}))

			t.Run("wildcard", runTest(testCase{
				args: []string{"-i", "json", "-o", "json", "--root", `$root..*.each($this = 4)`},
				in:   []byte(`[{"x":1},{"x":2},{"x":3}]`),
				stdout: []byte(`[
    {
        "x": 4
    },
    {
        "x": 4
    },
    {
        "x": 4
    }
]
`),
				stderr: nil,
				err:    nil,
			}))

		})
		t.Run("create object with empty stdin", runTest(testCase{
			args: []string{`{"name":"Tom"}`},
			in:   []byte{},
			stdout: []byte(`{
    "name": "Tom"
}
`),
			stderr: nil,
			err:    nil,
		}))
	})
	t.Run("set search", runTest(testCase{
		args: []string{"-i", "json", "-o", "json", "--root", `search(has("x")).each(x = x+1)`},
		in:   []byte(`[{"x":1},{"x":2},{"x":3}]`),
		stdout: []byte(`[
    {
        "x": 2
    },
    {
        "x": 3
    },
    {
        "x": 4
    }
]
`),
		stderr: nil,
		err:    nil,
	}))
	t.Run("recursive descent", func(t *testing.T) {
		t.Run("wildcard", runTest(testCase{
			args: []string{"-i", "json", `..*`},
			in: []byte(`{
  "user": {
    "name": "Alice",
    "roles": ["admin", "editor"],
    "meta": {
      "active": true,
      "score": 42
    }
  },
  "tags": ["x", "y"],
  "count": 10
}`),
			stdout: []byte(`[
    "Alice",
    "admin",
    "editor",
    true,
    42,
    "x",
    "y",
    10
]
`),
			stderr: nil,
			err:    nil,
		}))

		t.Run("property", runTest(testCase{
			args: []string{"-i", "json", `..name`},
			in: []byte(`{
  "user": {
    "name": "Alice",
    "roles": ["admin", "editor"],
    "meta": {
      "active": true,
      "score": 42
    }
  },
  "tags": ["x", "y"],
  "count": 10
}`),
			stdout: []byte(`[
    "Alice"
]
`),
			stderr: nil,
			err:    nil,
		}))

		t.Run("property2", runTest(testCase{
			args: []string{"-i", "json", `..name`},
			in:   []byte(`[{"name":"Tom"}, {"name":"Jim"}, {"foo": "Bar"}]`),
			stdout: []byte(`[
    "Tom",
    "Jim"
]
`),
			stderr: nil,
			err:    nil,
		}))

		t.Run("index", runTest(testCase{
			args: []string{"-i", "json", `..[0]`},
			in: []byte(`{
  "user": {
    "name": "Alice",
    "roles": ["admin", "editor"],
    "meta": {
      "active": true,
      "score": 42
    }
  },
  "tags": ["x", "y"],
  "count": 10
}`),
			stdout: []byte(`[
    "admin",
    "x"
]
`),
			stderr: nil,
			err:    nil,
		}))
	})
}
```

## File: `internal/cli/config.go`
```go
package cli

import (
	"errors"
	"fmt"
	"io"
	"os"
	"os/user"
	"strings"

	"go.yaml.in/yaml/v4"
)

// Config holds the contents of a config file.
type Config struct {
	DefaultFormat string `yaml:"default_format"`
}

var cfg = Config{
	DefaultFormat: "json",
}
var cfgLoaded = false

// LoadConfig loads the config from the given path.
// If already loaded, returned previously loaded config.
func LoadConfig(path string) (Config, error) {
	if cfgLoaded {
		return cfg, nil
	}

	if strings.HasPrefix(path, "~/") {
		usr, err := user.Current()
		if err != nil {
			return cfg, fmt.Errorf("error getting current user: %v", err)
		}
		path = usr.HomeDir + path[1:]
	}

	f, err := os.Open(path)
	if errors.Is(err, os.ErrNotExist) {
		cfgLoaded = true
		return cfg, nil
	}
	if err != nil {
		return cfg, fmt.Errorf("error opening config file at path %q: %w", path, err)
	}
	defer func() {
		_ = f.Close()
	}()
	decoder := yaml.NewDecoder(f)
	err = decoder.Decode(&cfg)
	if err != nil && !errors.Is(err, io.EOF) {
		return cfg, fmt.Errorf("error parsing config file: %w", err)
	}
	cfgLoaded = true
	return cfg, nil
}
```

## File: `internal/cli/generic_test.go`
```go
package cli_test

import (
	"fmt"
	"slices"
	"testing"

	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/json"
	"github.com/tomwright/dasel/v3/parsing/toml"
	"github.com/tomwright/dasel/v3/parsing/yaml"
)

func newStringWithFormat(format parsing.Format, data string) bytesWithFormat {
	return bytesWithFormat{
		format: format,
		data:   append([]byte(data), []byte("\n")...),
	}
}

type bytesWithFormat struct {
	format parsing.Format
	data   []byte
}

type testCases struct {
	selector string
	in       []bytesWithFormat
	out      []bytesWithFormat
	args     []string
	skip     []string
}

func (tcs testCases) run(t *testing.T) {
	for _, i := range tcs.in {
		for _, o := range tcs.out {
			tcName := fmt.Sprintf("%s to %s", i.format.String(), o.format.String())

			if slices.Contains(tcs.skip, tcName) {
				// Run a test and skip for visibility.
				t.Run(tcName, func(t *testing.T) {
					t.Skip()
				})
				continue
			}

			args := slices.Clone(tcs.args)
			args = append(args, "-i", i.format.String(), "-o", o.format.String())
			if tcs.selector != "" {
				args = append(args, tcs.selector)
			}
			tc := testCase{
				args:   args,
				in:     i.data,
				stdout: o.data,
			}
			t.Run(tcName, runTest(tc))
		}
	}
}

func TestCrossFormatHappyPath(t *testing.T) {
	jsonInputData := newStringWithFormat(json.JSON, `{
	"oneTwoThree": 123,
	"oneTwoDotThree": 12.3,
	"hello": "world",
	"boolFalse": false,
	"boolTrue": true,
	"stringFalse": "false",
	"stringTrue": "true",
	"sliceOfNumbers": [1, 2, 3, 4, 5],
	"mapData": {
		"oneTwoThree": 123,
		"oneTwoDotThree": 12.3,
		"hello": "world",
		"boolFalse": false,
		"boolTrue": true,
		"stringFalse": "false",
		"stringTrue": "true",
		"sliceOfNumbers": [1, 2, 3, 4, 5],
		"mapData": {
			"oneTwoThree": 123,
			"oneTwoDotThree": 12.3,
			"hello": "world",
			"boolFalse": false,
			"boolTrue": true,
			"stringFalse": "false",
			"stringTrue": "true",
			"sliceOfNumbers": [1, 2, 3, 4, 5]
		}
	}
}`)
	yamlInputData := newStringWithFormat(yaml.YAML, `oneTwoThree: 123
oneTwoDotThree: 12.3
hello: world
boolFalse: false
boolTrue: true
stringFalse: "false"
stringTrue: "true"
sliceOfNumbers:
- 1
- 2
- 3
- 4
- 5
mapData:
    oneTwoThree: 123
    oneTwoDotThree: 12.3
    hello: world
    boolFalse: false
    boolTrue: true
    stringFalse: "false"
    stringTrue: "true"
    sliceOfNumbers:
    - 1
    - 2
    - 3
    - 4
    - 5
    mapData:
        oneTwoThree: 123
        oneTwoDotThree: 12.3
        hello: world
        boolFalse: false
        boolTrue: true
        stringFalse: "false"
        stringTrue: "true"
        sliceOfNumbers:
        - 1
        - 2
        - 3
        - 4
        - 5
`)

	tomlInputData := newStringWithFormat(toml.TOML, `
oneTwoThree = 123
oneTwoDotThree = 12.3
hello = 'world'
boolFalse = false
boolTrue = true
stringFalse = 'false'
stringTrue = 'true'
sliceOfNumbers = [1, 2, 3, 4, 5]

[mapData]
oneTwoThree = 123
oneTwoDotThree = 12.3
hello = 'world'
boolFalse = false
boolTrue = true
stringFalse = 'false'
stringTrue = 'true'
sliceOfNumbers = [1, 2, 3, 4, 5]

[mapData.mapData]
oneTwoThree = 123
oneTwoDotThree = 12.3
hello = 'world'
boolFalse = false
boolTrue = true
stringFalse = 'false'
stringTrue = 'true'
sliceOfNumbers = [1, 2, 3, 4, 5]
`)

	t.Run("select", func(t *testing.T) {
		newTestsWithPrefix := func(prefix string) func(*testing.T) {
			return func(t *testing.T) {
				t.Run("string", testCases{
					selector: prefix + "hello",
					in: []bytesWithFormat{
						jsonInputData,
						yamlInputData,
						tomlInputData,
					},
					out: []bytesWithFormat{
						newStringWithFormat(json.JSON, `"world"`),
						newStringWithFormat(yaml.YAML, `world`),
						newStringWithFormat(toml.TOML, `'world'`),
					},
				}.run)
				t.Run("int", testCases{
					selector: prefix + "oneTwoThree",
					in: []bytesWithFormat{
						jsonInputData,
						yamlInputData,
						tomlInputData,
					},
					out: []bytesWithFormat{
						newStringWithFormat(json.JSON, `123`),
						newStringWithFormat(yaml.YAML, `123`),
						newStringWithFormat(toml.TOML, `123`),
					},
				}.run)
				t.Run("float", testCases{
					selector: prefix + "oneTwoDotThree",
					in: []bytesWithFormat{
						jsonInputData,
						yamlInputData,
						tomlInputData,
					},
					out: []bytesWithFormat{
						newStringWithFormat(json.JSON, `12.3`),
						newStringWithFormat(yaml.YAML, `12.3`),
						newStringWithFormat(toml.TOML, `12.3`),
					},
				}.run)
				t.Run("bool", func(t *testing.T) {
					t.Run("true", testCases{
						selector: prefix + "boolTrue",
						in: []bytesWithFormat{
							jsonInputData,
							yamlInputData,
						},
						out: []bytesWithFormat{
							newStringWithFormat(json.JSON, `true`),
							newStringWithFormat(yaml.YAML, `true`),
							newStringWithFormat(toml.TOML, `true`),
						},
					}.run)
					t.Run("false", testCases{
						selector: prefix + "boolFalse",
						in: []bytesWithFormat{
							jsonInputData,
							yamlInputData,
						},
						out: []bytesWithFormat{
							newStringWithFormat(json.JSON, `false`),
							newStringWithFormat(yaml.YAML, `false`),
							newStringWithFormat(toml.TOML, `false`),
						},
					}.run)
					t.Run("true string", testCases{
						selector: prefix + "stringTrue",
						in: []bytesWithFormat{
							jsonInputData,
							yamlInputData,
						},
						out: []bytesWithFormat{
							newStringWithFormat(json.JSON, `"true"`),
							newStringWithFormat(yaml.YAML, `"true"`),
							newStringWithFormat(toml.TOML, `'true'`),
						},
					}.run)
					t.Run("false string", testCases{
						selector: prefix + "stringFalse",
						in: []bytesWithFormat{
							jsonInputData,
							yamlInputData,
						},
						out: []bytesWithFormat{
							newStringWithFormat(json.JSON, `"false"`),
							newStringWithFormat(yaml.YAML, `"false"`),
							newStringWithFormat(toml.TOML, `'false'`),
						},
					}.run)
				})
			}
		}

		t.Run("root", newTestsWithPrefix(""))
		t.Run("nested once", newTestsWithPrefix("mapData."))
		t.Run("nested twice", newTestsWithPrefix("mapData.mapData."))
	})
}
```

## File: `internal/cli/interactive.go`
```go
package cli

import (
	"bytes"
	"fmt"
	"io"

	"github.com/tomwright/dasel/v3/parsing"
)

func NewInteractiveCmd(queryCmd *QueryCmd) *InteractiveCmd {
	return &InteractiveCmd{
		Vars:              queryCmd.Vars,
		ExtReadWriteFlags: queryCmd.ExtReadWriteFlags,
		ExtReadFlags:      queryCmd.ExtReadFlags,
		ExtWriteFlags:     queryCmd.ExtWriteFlags,
		InFormat:          queryCmd.InFormat,
		OutFormat:         queryCmd.OutFormat,

		Query: queryCmd.Query,
	}
}

type InteractiveCmd struct {
	Vars              variables         `flag:"" name:"var" help:"Variables to pass to the query. E.g. --var foo=\"bar\" --var baz=json:file:./some/file.json"`
	ExtReadWriteFlags extReadWriteFlags `flag:"" name:"rw-flag" help:"Read/Write flag to customise parsing/output. Applies to read + write E.g. --rw-flag csv-delimiter=;"`
	ExtReadFlags      extReadWriteFlags `flag:"" name:"read-flag" help:"Reader flag to customise parsing. E.g. --read-flag xml-mode=structured"`
	ExtWriteFlags     extReadWriteFlags `flag:"" name:"write-flag" help:"Writer flag to customise output. E.g. --write-flag csv-delimiter=;"`
	InFormat          string            `flag:"" name:"in" short:"i" help:"The format of the input data."`
	OutFormat         string            `flag:"" name:"out" short:"o" help:"The format of the output data."`

	ConfigPath string `name:"config" short:"c" help:"Path to config file" default:"~/dasel.yaml"`

	Query string `arg:"" help:"The query to execute." optional:"" default:""`
}

func (c *InteractiveCmd) Run(ctx *Globals) error {
	var stdInBytes []byte = nil

	if ctx.Stdin != nil {
		var err error
		stdInBytes, err = io.ReadAll(ctx.Stdin)
		if err != nil {
			return err
		}
	}

	cfg, err := LoadConfig(c.ConfigPath)
	if err != nil {
		return err
	}

	if c.InFormat == "" && c.OutFormat == "" {
		c.InFormat = cfg.DefaultFormat
		c.OutFormat = cfg.DefaultFormat
	} else if c.InFormat == "" {
		c.InFormat = c.OutFormat
	} else if c.OutFormat == "" {
		c.OutFormat = c.InFormat
	}

	var runDasel interactiveDaselExecutor = func(selector string, root bool, formatIn parsing.Format, formatOut parsing.Format, in string) (res string, err error) {
		defer func() {
			if r := recover(); r != nil {
				err = fmt.Errorf("panic: %v", r)
			}
		}()
		var stdIn *bytes.Reader
		if in != "" {
			stdIn = bytes.NewReader([]byte(in))
		} else {
			stdIn = bytes.NewReader([]byte{})
		}

		o := runOpts{
			Vars:              c.Vars,
			ExtReadWriteFlags: c.ExtReadWriteFlags,
			ExtReadFlags:      c.ExtReadFlags,
			ExtWriteFlags:     c.ExtWriteFlags,
			InFormat:          formatIn.String(),
			OutFormat:         formatOut.String(),
			ReturnRoot:        root,
			Unstable:          true,
			Query:             selector,

			ConfigPath: c.ConfigPath,

			Stdin: stdIn,
		}

		outBytes, err := run(o)
		return string(outBytes), err
	}

	p, selectorFn := newInteractiveTeaProgram(string(stdInBytes), c.Query, parsing.Format(c.InFormat), parsing.Format(c.OutFormat), runDasel)

	_, err = p.Run()
	if err != nil {
		return err
	}

	if selectorFn != nil {
		s := selectorFn()
		if s != "" {
			if _, err := fmt.Fprintf(ctx.Stdout, "%s\n", s); err != nil {
				return fmt.Errorf("error writing output: %w", err)
			}
		}
	}

	return nil
}
```

## File: `internal/cli/interactive_tea.go`
```go
package cli

import (
	"fmt"
	"slices"
	"strings"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
	"github.com/tomwright/dasel/v3/internal"
	"github.com/tomwright/dasel/v3/parsing"
)

var (
	interactiveKeyQuit       = tea.KeyCtrlC
	interactiveKeyCycleRead  = tea.KeyCtrlE
	interactiveKeyCycleWrite = tea.KeyCtrlD

	headingStyle = func() lipgloss.Style {
		return lipgloss.NewStyle().Padding(0, 1, 1, 1)
	}()
	shortcutStyle = func() lipgloss.Style {
		return lipgloss.NewStyle().Padding(0, 1).Align(lipgloss.Left)
	}()
	headerStyle = func() lipgloss.Style {
		return lipgloss.NewStyle().Padding(1).Align(lipgloss.Center)
	}()
	inputStyle = func() lipgloss.Style {
		return lipgloss.NewStyle().Margin(0, 0, 1, 0)
	}()
	outputContentStyle = func() lipgloss.Style {
		return lipgloss.NewStyle().Padding(0, 1).Border(lipgloss.RoundedBorder())
	}()
	outputHeaderStyle = func() lipgloss.Style {
		return lipgloss.NewStyle().Padding(0, 2).Margin(0, 0, 1, 0).Underline(true)
	}()
)

type interactiveDaselExecutor func(selector string, root bool, formatIn parsing.Format, formatOut parsing.Format, in string) (res string, err error)

func newInteractiveTeaProgram(initialInput string, initialSelector string, formatIn parsing.Format, formatOut parsing.Format, run interactiveDaselExecutor) (*tea.Program, func() string) {
	m := newInteractiveRootModel(initialInput, initialSelector, formatIn, formatOut, run)
	return tea.NewProgram(m, tea.WithAltScreen()), func() string {
		return m.sharedData.selector
	}
}

type interactiveSharedData struct {
	formatIn  parsing.Format
	formatOut parsing.Format
	selector  string
	input     string
}

type interactiveRootModel struct {
	sharedData   *interactiveSharedData
	inputModel   *interactiveInputModel
	outputModels []*interactiveOutputModel
}

func newInteractiveRootModel(initialInput string, initialSelector string, formatIn parsing.Format, formatOut parsing.Format, run interactiveDaselExecutor) *interactiveRootModel {
	res := &interactiveRootModel{
		sharedData: &interactiveSharedData{
			formatIn:  formatIn,
			formatOut: formatOut,
			selector:  initialSelector,
			input:     initialInput,
		},
		outputModels: make([]*interactiveOutputModel, 0),
	}

	res.inputModel = newInteractiveInputModel(res.sharedData)

	outputRootModel := newInteractiveOutputModel(res.sharedData, true, run)
	outputResultModel := newInteractiveOutputModel(res.sharedData, false, run)

	res.outputModels = append(res.outputModels, outputRootModel, outputResultModel)

	return res
}

func (m *interactiveRootModel) Init() tea.Cmd {
	return nil
}

func cycleFormats(all []parsing.Format, current parsing.Format) parsing.Format {
	slices.SortFunc(all, func(i, j parsing.Format) int {
		return strings.Compare(string(i), string(j))
	})
	cur := -1
	for i, format := range all {
		if format == current {
			cur = i
			break
		}
	}
	next := cur + 1
	if next > len(all)-1 {
		next = 0
	}
	return all[next]
}

func (m *interactiveRootModel) cycleReader() {
	m.sharedData.formatIn = cycleFormats(parsing.RegisteredReaders(), m.sharedData.formatIn)
}

func (m *interactiveRootModel) cycleWriter() {
	m.sharedData.formatOut = cycleFormats(parsing.RegisteredWriters(), m.sharedData.formatOut)
}

func (m *interactiveRootModel) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	var cmds []tea.Cmd
	var cmd tea.Cmd

	switch msg := msg.(type) {
	case tea.KeyMsg:
		switch msg.Type {
		case interactiveKeyQuit:
			return m, tea.Quit
		case interactiveKeyCycleRead:
			m.cycleReader()
		case interactiveKeyCycleWrite:
			m.cycleWriter()
		default:
		}

	case tea.WindowSizeMsg:
		headerStyle = headerStyle.Width(msg.Width).MaxWidth(msg.Width)

		var headerHeight int
		{
			headerHeight += lipgloss.Height(m.headerView())
			headerHeight += lipgloss.Height(m.inputView())
		}
		verticalMarginHeight := headerHeight

		numCols := len(m.outputModels)

		viewportHeight := msg.Height - verticalMarginHeight - (2 * numCols)
		viewportWidth := (msg.Width / numCols) - (2 * numCols)

		for _, outputModel := range m.outputModels {
			outputModel.setSize(viewportWidth, viewportHeight)
			outputModel.setVerticalPosition(verticalMarginHeight)
		}
	}

	{
		var model tea.Model
		model, cmd = m.inputModel.Update(msg)
		m.inputModel = model.(*interactiveInputModel)
		cmds = append(cmds, cmd)
	}

	for i, outputModel := range m.outputModels {
		var model tea.Model
		model, cmd = outputModel.Update(msg)
		m.outputModels[i] = model.(*interactiveOutputModel)
		cmds = append(cmds, cmd)
	}

	return m, tea.Batch(cmds...)
}

func (m *interactiveRootModel) headerView() string {
	header := headingStyle.Render("Dasel interactive mode - " + internal.Version)

	shortcuts := "\n"
	shortcuts += fmt.Sprintf("%s: %s\n", interactiveKeyQuit, "Quit")
	shortcuts += fmt.Sprintf("%s: %s\n", interactiveKeyCycleRead, "Cycle reader")
	shortcuts += fmt.Sprintf("%s: %s\n", interactiveKeyCycleWrite, "Cycle writer")

	out := append([]string{header}, shortcutStyle.Render(shortcuts))

	out = append(out, fmt.Sprintf("\nReader: %s | Writer: %s", m.sharedData.formatIn, m.sharedData.formatOut))

	return headerStyle.Render(out...)
}

func (m *interactiveRootModel) inputView() string {
	return inputStyle.Render(m.inputModel.View())
}

func (m *interactiveRootModel) View() string {
	rows := make([]string, 0)

	rows = append(rows, m.headerView())

	rows = append(rows, m.inputView())

	{
		cols := make([]string, 0)
		for _, outputModel := range m.outputModels {
			cols = append(cols, outputModel.View())
		}
		if len(cols) > 0 {
			rows = append(rows, lipgloss.JoinHorizontal(lipgloss.Top, cols...))
		}
	}

	return lipgloss.JoinVertical(lipgloss.Left, rows...)
}
```

## File: `internal/cli/interactive_tea_input.go`
```go
package cli

import (
	"github.com/charmbracelet/bubbles/textarea"
	tea "github.com/charmbracelet/bubbletea"
)

type interactiveInputModel struct {
	sharedData *interactiveSharedData
	inputModel textarea.Model
}

func newInteractiveInputModel(sharedData *interactiveSharedData) *interactiveInputModel {
	ti := textarea.New()
	ti.Placeholder = "Enter a query..."
	ti.SetValue(sharedData.selector)
	ti.Focus()
	ti.SetHeight(5)
	ti.ShowLineNumbers = false

	return &interactiveInputModel{
		sharedData: sharedData,
		inputModel: ti,
	}
}

func (m *interactiveInputModel) Init() tea.Cmd {
	return textarea.Blink
}

func (m *interactiveInputModel) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	var cmds []tea.Cmd
	var cmd tea.Cmd

	m.sharedData.selector = m.inputModel.Value()

	switch msg := msg.(type) {
	case tea.WindowSizeMsg:
		m.inputModel.SetWidth(msg.Width)
	}

	m.inputModel, cmd = m.inputModel.Update(msg)
	cmds = append(cmds, cmd)

	return m, tea.Batch(cmds...)
}

func (m *interactiveInputModel) View() string {
	return m.inputModel.View()
}
```

## File: `internal/cli/interactive_tea_output.go`
```go
package cli

import (
	"github.com/charmbracelet/bubbles/viewport"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
	"github.com/tomwright/dasel/v3/parsing"
)

type interactiveOutputModel struct {
	sharedData          *interactiveSharedData
	hasUpdatedBefore    bool
	lastSeenSelector    string
	lastSeenFormatIn    parsing.Format
	lastSeenFormatOut   parsing.Format
	lastSeenInput       string
	root                bool
	run                 interactiveDaselExecutor
	output              string
	outputViewport      viewport.Model
	outputViewportReady bool
}

func newInteractiveOutputModel(sharedData *interactiveSharedData, root bool, run interactiveDaselExecutor) *interactiveOutputModel {
	m := &interactiveOutputModel{
		sharedData: sharedData,
		root:       root,
		run:        run,
	}
	m.outputViewport = viewport.New(10, 10)
	return m
}

func (m *interactiveOutputModel) Init() tea.Cmd {
	return nil
}

func (m *interactiveOutputModel) setOutput(output string) {
	m.output = output
	if m.outputViewportReady {
		m.outputViewport.SetContent(m.output)
	}
}

func (m *interactiveOutputModel) setSize(width int, height int) {
	if !m.outputViewportReady {
		m.outputViewportReady = true
	}

	m.outputViewport.Width = width
	m.outputViewport.Height = height
	m.outputViewport.SetContent(m.output)
}

func (m *interactiveOutputModel) setVerticalPosition(pos int) {
	m.outputViewport.YPosition = pos
}

func (m *interactiveOutputModel) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	var cmds []tea.Cmd
	var cmd tea.Cmd

	defer func() {
		m.lastSeenSelector = m.sharedData.selector
		m.lastSeenFormatIn = m.sharedData.formatIn
		m.lastSeenFormatOut = m.sharedData.formatOut
		m.lastSeenInput = m.sharedData.input
	}()
	firstUpdate := !m.hasUpdatedBefore
	m.hasUpdatedBefore = true

	queryChanged := m.lastSeenSelector != m.sharedData.selector ||
		m.lastSeenFormatIn != m.sharedData.formatIn ||
		m.lastSeenFormatOut != m.sharedData.formatOut ||
		m.lastSeenInput != m.sharedData.input

	// Take care of dasel execution + output.
	if firstUpdate || queryChanged {
		m.setOutput("Executing...")
		out, err := m.run(m.sharedData.selector, m.root, m.sharedData.formatIn, m.sharedData.formatOut, m.sharedData.input)
		if err != nil {
			m.setOutput(err.Error())
		} else {
			m.setOutput(out)
		}
	}

	m.outputViewport, cmd = m.outputViewport.Update(msg)
	cmds = append(cmds, cmd)

	return m, tea.Batch(cmds...)
}

func (m *interactiveOutputModel) View() string {
	title := "Result"
	if m.root {
		title = "Root"
	}

	content := "Initializing..."
	if m.outputViewportReady {
		content = m.outputViewport.View()
	}

	return lipgloss.JoinVertical(lipgloss.Left, outputHeaderStyle.Render(title), outputContentStyle.Render(content))
}
```

## File: `internal/cli/query.go`
```go
package cli

import "fmt"

type QueryCmd struct {
	Vars              variables         `flag:"" name:"var" help:"Variables to pass to the query. E.g. --var foo=\"bar\" --var baz=json:file:./some/file.json"`
	ExtReadWriteFlags extReadWriteFlags `flag:"" name:"rw-flag" help:"Read/Write flag to customise parsing/output. Applies to read + write E.g. --rw-flag csv-delimiter=;"`
	ExtReadFlags      extReadWriteFlags `flag:"" name:"read-flag" help:"Reader flag to customise parsing. E.g. --read-flag xml-mode=structured"`
	ExtWriteFlags     extReadWriteFlags `flag:"" name:"write-flag" help:"Writer flag to customise output. E.g. --write-flag csv-delimiter=;"`
	InFormat          string            `flag:"" name:"in" short:"i" help:"The format of the input data."`
	OutFormat         string            `flag:"" name:"out" short:"o" help:"The format of the output data."`
	ReturnRoot        bool              `flag:"" name:"root" help:"Return the root value."`
	Unstable          bool              `flag:"" name:"unstable" help:"Allow access to potentially unstable features."`
	Interactive       bool              `flag:"" name:"it" help:"Run in interactive mode (alpha)."`

	ConfigPath string `name:"config" short:"c" help:"Path to config file" default:"~/dasel.yaml"`

	Query string `arg:"" help:"The query to execute." optional:"" default:""`
}

func (c *QueryCmd) Run(ctx *Globals) error {
	cfg, err := LoadConfig(c.ConfigPath)
	if err != nil {
		return err
	}

	if c.InFormat == "" && c.OutFormat == "" {
		c.InFormat = cfg.DefaultFormat
		c.OutFormat = cfg.DefaultFormat
	}

	if c.Query == "" && c.InFormat == "" && ctx.Stdin == nil {
		return ErrNoArgsGiven
	}

	if c.Interactive {
		return NewInteractiveCmd(c).Run(ctx)
	}

	o := runOpts{
		Vars:              c.Vars,
		ExtReadWriteFlags: c.ExtReadWriteFlags,
		ExtReadFlags:      c.ExtReadFlags,
		ExtWriteFlags:     c.ExtWriteFlags,
		InFormat:          c.InFormat,
		OutFormat:         c.OutFormat,
		ReturnRoot:        c.ReturnRoot,
		Unstable:          c.Unstable,
		Query:             c.Query,

		ConfigPath: c.ConfigPath,

		Stdin: ctx.Stdin,
	}
	outBytes, err := run(o)
	if err != nil {
		return err
	}

	_, err = ctx.Stdout.Write(outBytes)
	if err != nil {
		return fmt.Errorf("error writing output: %w", err)
	}

	return nil
}
```

## File: `internal/cli/read_write_flag.go`
```go
package cli

import (
	"fmt"
	"reflect"
	"strings"

	"github.com/alecthomas/kong"
	"github.com/tomwright/dasel/v3/parsing"
)

type extReadWriteFlag struct {
	Name  string
	Value string
}

type extReadWriteFlags *[]extReadWriteFlag

func applyReaderFlags(readerOptions *parsing.ReaderOptions, readerFlags extReadWriteFlags, readWriterFlags extReadWriteFlags) {
	if readWriterFlags != nil {
		for _, flag := range *readWriterFlags {
			readerOptions.Ext[flag.Name] = flag.Value
		}
	}
	if readerFlags != nil {
		for _, flag := range *readerFlags {
			readerOptions.Ext[flag.Name] = flag.Value
		}
	}
}

func applyWriterFlags(writerOptions *parsing.WriterOptions, writerFlags extReadWriteFlags, readWriterFlags extReadWriteFlags) {
	if readWriterFlags != nil {
		for _, flag := range *readWriterFlags {
			writerOptions.Ext[flag.Name] = flag.Value
		}
	}
	if writerFlags != nil {
		for _, flag := range *writerFlags {
			writerOptions.Ext[flag.Name] = flag.Value
		}
	}
}

type extReadWriteFlagMapper struct {
}

func (vm *extReadWriteFlagMapper) Decode(ctx *kong.DecodeContext, target reflect.Value) error {
	t := ctx.Scan.Pop()

	strVal, ok := t.Value.(string)
	if !ok {
		return fmt.Errorf("expected string value for variable")
	}

	nameValueSplit := strings.SplitN(strVal, "=", 2)
	if len(nameValueSplit) != 2 {
		return fmt.Errorf("invalid read/write flag format, expect foo=bar")
	}

	res := extReadWriteFlag{
		Name:  nameValueSplit[0],
		Value: nameValueSplit[1],
	}

	target.Elem().Set(reflect.Append(target.Elem(), reflect.ValueOf(res)))

	return nil
}
```

## File: `internal/cli/run.go`
```go
package cli

import (
	"context"
	"fmt"
	"io"

	"github.com/tomwright/dasel/v3/execution"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
)

type runOpts struct {
	Vars              variables
	ExtReadWriteFlags extReadWriteFlags
	ExtReadFlags      extReadWriteFlags
	ExtWriteFlags     extReadWriteFlags
	InFormat          string
	OutFormat         string
	ReturnRoot        bool
	Unstable          bool
	Query             string

	ConfigPath string

	Stdin io.Reader
}

func run(o runOpts) ([]byte, error) {
	cfg, err := LoadConfig(o.ConfigPath)
	if err != nil {
		return nil, fmt.Errorf("error loading config: %w", err)
	}

	var opts []execution.ExecuteOptionFn

	if o.OutFormat == "" && o.InFormat != "" {
		o.OutFormat = o.InFormat
	} else if o.OutFormat != "" && o.InFormat == "" {
		o.InFormat = o.OutFormat
	} else if o.OutFormat == "" {
		o.OutFormat = cfg.DefaultFormat
	}

	readerOptions := parsing.DefaultReaderOptions()
	applyReaderFlags(&readerOptions, o.ExtReadFlags, o.ExtReadWriteFlags)

	var reader parsing.Reader
	if len(o.InFormat) > 0 {
		reader, err = parsing.Format(o.InFormat).NewReader(readerOptions)
		if err != nil {
			return nil, fmt.Errorf("failed to get input reader: %w", err)
		}
	}

	writerOptions := parsing.DefaultWriterOptions()
	applyWriterFlags(&writerOptions, o.ExtWriteFlags, o.ExtReadWriteFlags)

	writer, err := parsing.Format(o.OutFormat).NewWriter(writerOptions)
	if err != nil {
		return nil, fmt.Errorf("failed to get output writer: %w", err)
	}

	opts = append(opts, variableOptions(o.Vars)...)

	// Default to null. If stdin is being read then this will be overwritten.
	inputData := model.NewNullValue()

	var inputBytes []byte
	if o.Stdin != nil {
		inputBytes, err = io.ReadAll(o.Stdin)
		if err != nil {
			return nil, fmt.Errorf("error reading stdin: %w", err)
		}
	}

	if len(inputBytes) > 0 {
		if reader == nil {
			return nil, fmt.Errorf("input format is required when reading stdin")
		}
		inputData, err = reader.Read(inputBytes)
		if err != nil {
			return nil, fmt.Errorf("error reading input: %w", err)
		}
	}

	opts = append(opts, execution.WithVariable("root", inputData))

	if o.Unstable {
		opts = append(opts, execution.WithUnstable())
	}

	options := execution.NewOptions(opts...)
	out, err := execution.ExecuteSelector(context.Background(), o.Query, inputData, options)
	if err != nil {
		return nil, err
	}

	if o.ReturnRoot {
		out = inputData
	}

	outputBytes, err := writer.Write(out)
	if err != nil {
		return nil, fmt.Errorf("error writing output: %w", err)
	}

	return outputBytes, nil
}
```

## File: `internal/cli/variable.go`
```go
package cli

import (
	"fmt"
	"io"
	"os"
	"reflect"
	"strings"

	"github.com/alecthomas/kong"
	"github.com/tomwright/dasel/v3/execution"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
)

type variable struct {
	Name  string
	Value *model.Value
}

type variables *[]variable

func variableOptions(vars variables) []execution.ExecuteOptionFn {
	var opts []execution.ExecuteOptionFn
	if vars != nil {
		for _, v := range *vars {
			opts = append(opts, execution.WithVariable(v.Name, v.Value))
		}
	}
	return opts
}

type variableMapper struct {
}

// Decode decodes a variable from a flag.
// E.g. --var foo=bar
// E.g. --var foo=json:{"bar":"baz"}
// E.g. --var foo=json:file:/path/to/file.json
func (vm *variableMapper) Decode(ctx *kong.DecodeContext, target reflect.Value) error {
	t := ctx.Scan.Pop()

	strVal, ok := t.Value.(string)
	if !ok {
		return fmt.Errorf("expected string value for variable")
	}

	nameValueSplit := strings.SplitN(strVal, "=", 2)
	if len(nameValueSplit) != 2 {
		return fmt.Errorf("invalid variable format, expect foo=bar, or foo=format:file:path")
	}

	res := variable{
		Name: nameValueSplit[0],
	}

	format := "dasel"
	valueRaw := nameValueSplit[1]

	firstSplit := strings.SplitN(valueRaw, ":", 2)
	if len(firstSplit) == 2 {
		format = firstSplit[0]
		valueRaw = firstSplit[1]
	}
	if strings.HasPrefix(valueRaw, "file:") {
		filePath := valueRaw[len("file:"):]

		f, err := os.Open(filePath)
		if err != nil {
			return fmt.Errorf("failed to open file: %w", err)
		}
		defer func() {
			_ = f.Close()
		}()
		contents, err := io.ReadAll(f)
		if err != nil {
			return fmt.Errorf("failed to read file contents: %w", err)
		}
		valueRaw = string(contents)
	}

	reader, err := parsing.Format(format).NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		return fmt.Errorf("failed to create reader: %w", err)
	}
	res.Value, err = reader.Read([]byte(valueRaw))
	if err != nil {
		return fmt.Errorf("failed to read value: %w", err)
	}

	target.Elem().Set(reflect.Append(target.Elem(), reflect.ValueOf(res)))

	return nil
}
```

## File: `internal/cli/version.go`
```go
package cli

import "github.com/tomwright/dasel/v3/internal"

type VersionCmd struct {
}

func (c *VersionCmd) Run(ctx *Globals) error {
	_, err := ctx.Stdout.Write([]byte(internal.Version + "\n"))
	return err
}
```

## File: `internal/ptr/to.go`
```go
package ptr

// To returns a pointer to the value passed in.
func To[T any](v T) *T {
	return &v
}
```

## File: `internal/ptr/to_test.go`
```go
package ptr_test

import (
	"github.com/tomwright/dasel/v3/internal/ptr"
	"testing"
)

func TestTo(t *testing.T) {
	a := 1
	if exp, got := a, *(ptr.To(a)); exp != a {
		t.Errorf("expected %d, got %d", exp, got)
	}
}
```

## File: `model/error.go`
```go
package model

import "fmt"

// MapKeyNotFound is returned when a key is not found in a map.
type MapKeyNotFound struct {
	Key string
}

// Error returns the error message.
func (e MapKeyNotFound) Error() string {
	return fmt.Sprintf("map key not found: %q", e.Key)
}

// SliceIndexOutOfRange is returned when an index is invalid.
type SliceIndexOutOfRange struct {
	Index int
}

// Error returns the error message.
func (e SliceIndexOutOfRange) Error() string {
	return fmt.Sprintf("slice index out of range: %d", e.Index)
}

// ErrIncompatibleTypes is returned when two values are incompatible.
type ErrIncompatibleTypes struct {
	A *Value
	B *Value
}

// Error returns the error message.
func (e ErrIncompatibleTypes) Error() string {
	return fmt.Sprintf("incompatible types: %s and %s", e.A.Type(), e.B.Type())
}

type ErrUnexpectedType struct {
	Expected Type
	Actual   Type
}

func (e ErrUnexpectedType) Error() string {
	return fmt.Sprintf("unexpected type: expected %s, got %s", e.Expected, e.Actual)
}

type ErrUnexpectedTypes struct {
	Expected []Type
	Actual   Type
}

func (e ErrUnexpectedTypes) Error() string {
	return fmt.Sprintf("unexpected type: expected %v, got %s", e.Expected, e.Actual)
}
```

## File: `model/go_value.go`
```go
package model

import "fmt"

// GoValue returns the value as a native Go value.
func (v *Value) GoValue() (any, error) {
	var res any
	var err error

	switch v.Type() {
	case TypeString:
		res, err = v.StringValue()
	case TypeInt:
		res, err = v.IntValue()
	case TypeFloat:
		res, err = v.FloatValue()
	case TypeBool:
		res, err = v.BoolValue()
	case TypeMap:
		m := make(map[string]any)
		err = v.RangeMap(func(k string, v *Value) error {
			val, err := v.GoValue()
			if err != nil {
				return err
			}
			m[k] = val
			return nil
		})
		res = m
	case TypeSlice:
		s := make([]any, 0)
		err = v.RangeSlice(func(i int, v *Value) error {
			val, err := v.GoValue()
			if err != nil {
				return err
			}
			s = append(s, val)
			return nil
		})
		res = s
	case TypeUnknown:
		res = nil
		err = fmt.Errorf("cannot convert unknown type to Go value")
	case TypeNull:
		res = nil
	default:
		err = fmt.Errorf("unhandled type %v", v.Type())
	}

	return res, err
}
```

## File: `model/go_value_test.go`
```go
package model_test

import (
	"github.com/google/go-cmp/cmp"
	"github.com/tomwright/dasel/v3/model"
	"testing"
)

type goValueTestCase struct {
	in   *model.Value
	inFn func() *model.Value
	exp  any
}

func (tc goValueTestCase) run(t *testing.T) {
	if tc.inFn != nil {
		tc.in = tc.inFn()
	}
	out, err := tc.in.GoValue()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if !cmp.Equal(tc.exp, out) {
		t.Errorf("unexpected result: %s", cmp.Diff(tc.exp, out))
	}
}

func TestValue_GoValue(t *testing.T) {
	t.Run("null", goValueTestCase{
		in:  model.NewNullValue(),
		exp: nil,
	}.run)
	t.Run("int", goValueTestCase{
		in:  model.NewIntValue(42),
		exp: int64(42),
	}.run)
	t.Run("float", goValueTestCase{
		in:  model.NewFloatValue(3.14),
		exp: 3.14,
	}.run)
	t.Run("string", goValueTestCase{
		in:  model.NewStringValue("hello"),
		exp: "hello",
	}.run)
	t.Run("bool", goValueTestCase{
		in:  model.NewBoolValue(true),
		exp: true,
	}.run)
	t.Run("slice", goValueTestCase{
		inFn: func() *model.Value {
			s := model.NewSliceValue()
			_ = s.Append(model.NewIntValue(1))
			_ = s.Append(model.NewIntValue(2))
			_ = s.Append(model.NewIntValue(3))
			return s
		},
		exp: []any{int64(1), int64(2), int64(3)},
	}.run)
	t.Run("map", goValueTestCase{
		inFn: func() *model.Value {
			m := model.NewMapValue()
			_ = m.SetMapKey("a", model.NewStringValue("apple"))
			return m
		},
		exp: map[string]any{
			"a": "apple",
		},
	}.run)
}
```

## File: `model/README.md`
```markdown
# Model

The model package contains the Value struct and functionality for the application.

`model.Value` is just a wrapper around `reflect.Value` but provides some additional logic for easier use.
```

## File: `model/value.go`
```go
package model

import (
	"fmt"
	"reflect"
	"slices"
	"strings"
)

type Type string

func (t Type) String() string {
	return string(t)
}

const (
	TypeString  Type = "string"
	TypeInt     Type = "int"
	TypeFloat   Type = "float"
	TypeBool    Type = "bool"
	TypeMap     Type = "map"
	TypeSlice   Type = "array"
	TypeUnknown Type = "unknown"
	TypeNull    Type = "null"
)

// KeyValue represents a key value pair.
type KeyValue struct {
	Key   string
	Value *Value
}

// Values represents a list of values.
type Values []*Value

// ToSliceValue converts a list of values to a slice value.
func (v Values) ToSliceValue() (*Value, error) {
	slice := NewSliceValue()
	for _, val := range v {
		if err := slice.Append(val); err != nil {
			return nil, err
		}
	}
	return slice, nil
}

// Value represents a value.
type Value struct {
	value    reflect.Value
	Metadata map[string]any

	setFn func(*Value) error
}

// String returns the value as a formatted string, along with type info.
func (v *Value) String() string {
	return v.string(0)
}

func indentStr(indent int) string {
	return strings.Repeat("    ", indent)
}

func (v *Value) string(indent int) string {
	switch v.Type() {
	case TypeString:
		val, err := v.StringValue()
		if err != nil {
			panic(err)
		}
		return fmt.Sprintf("string{%s}", val)
	case TypeInt:
		val, err := v.IntValue()
		if err != nil {
			panic(err)
		}
		return fmt.Sprintf("int{%d}", val)
	case TypeFloat:
		val, err := v.FloatValue()
		if err != nil {
			panic(err)
		}
		return fmt.Sprintf("float(%g)", val)
	case TypeBool:
		val, err := v.BoolValue()
		if err != nil {
			panic(err)
		}
		return fmt.Sprintf("bool{%t}", val)
	case TypeMap:
		res := "{\n"
		if err := v.RangeMap(func(k string, v *Value) error {
			res += fmt.Sprintf("%s%s: %s,\n", indentStr(indent+1), k, v.string(indent+1))
			return nil
		}); err != nil {
			panic(err)
		}
		return res + indentStr(indent) + "}"
	case TypeSlice:
		md := ""
		if v.IsSpread() {
			md = "spread, "
		}
		if v.IsBranch() {
			md += "branch, "
		}
		res := fmt.Sprintf("array[%s]{\n", strings.TrimSuffix(md, ", "))
		if err := v.RangeSlice(func(k int, v *Value) error {
			res += fmt.Sprintf("%s%d: %s,\n", indentStr(indent+1), k, v.string(indent+1))
			return nil
		}); err != nil {
			panic(err)
		}
		return res + indentStr(indent) + "}"
	case TypeNull:
		return indentStr(indent) + "null"
	default:
		return fmt.Sprintf("unknown[%s]", v.Interface())
	}
}

// NewValue creates a new value.
func NewValue(v any) *Value {
	switch val := v.(type) {
	case *Value:
		return NewNestedValue(val)
	case reflect.Value:
		return &Value{
			value:    val,
			Metadata: nil,
		}
	case nil:
		return NewNullValue()
	default:
		res := newPtr()
		if v != nil {
			res.Elem().Set(reflect.ValueOf(v))
		}
		return &Value{
			value:    res,
			Metadata: nil,
		}
	}
}

// NewNestedValue creates a new nested value.
func NewNestedValue(v *Value) *Value {
	return &Value{
		value:    reflect.ValueOf(v),
		Metadata: nil,
	}
}

func (v *Value) isDaselValue() bool {
	cur := v.value
	for cur.Kind() == reflect.Interface && !cur.IsNil() {
		cur = cur.Elem()
	}
	return cur.Type() == reflect.TypeFor[*Value]()
}

func (v *Value) daselValue() (*Value, error) {
	if v.isDaselValue() {
		m, err := v.UnpackUntilType(reflect.TypeFor[*Value]())
		if err != nil {
			return nil, fmt.Errorf("error getting dasel value: %w", err)
		}
		return m.value.Interface().(*Value), nil
	}
	return nil, fmt.Errorf("value is not a dasel value")
}

// Interface returns the value as an interface.
func (v *Value) Interface() any {
	if v.IsNull() {
		return nil
	}
	return v.value.Interface()
}

// Kind returns the reflect kind of the value.
func (v *Value) Kind() reflect.Kind {
	return v.value.Kind()
}

// UnpackKinds unpacks the reflect value until it no longer matches the given kinds.
func (v *Value) UnpackKinds(kinds ...reflect.Kind) *Value {
	val := v
	for val.isDaselValue() {
		var err error
		val, err = val.daselValue()
		if err != nil {
			panic(err)
		}
	}
	res := val.value
	for {
		if !slices.Contains(kinds, res.Kind()) || res.IsNil() {
			return NewValue(res)
		}
		res = res.Elem()
	}
}

type ErrCouldNotUnpackToType struct {
	Type reflect.Type
}

func (e ErrCouldNotUnpackToType) Error() string {
	return fmt.Sprintf("could not unpack to type: %s", e.Type)
}

// UnpackUntilType unpacks the reflect value until it matches the given type.
func (v *Value) UnpackUntilType(t reflect.Type) (*Value, error) {
	res := v.value
	var daselValueType = reflect.TypeFor[*Value]()
	for {
		if res.Type() == t {
			return NewValue(res), nil
		}
		if t != daselValueType && res.Type() == daselValueType {
			m, err := v.daselValue()
			if err != nil {
				return nil, fmt.Errorf("error getting dasel value: %w", err)
			}
			res = m.value
			continue

		}
		if res.Kind() == reflect.Interface || res.Kind() == reflect.Pointer && !res.IsNil() {
			res = res.Elem()
			continue
		}
		return nil, &ErrCouldNotUnpackToType{Type: t}
	}
}

// UnpackUntilAddressable unpacks the reflect value until it is addressable.
func (v *Value) UnpackUntilAddressable() (*Value, error) {
	res := v.value
	for {
		if res.CanAddr() {
			return NewValue(res), nil
		}
		if res.Kind() == reflect.Interface || res.Kind() == reflect.Pointer && !res.IsNil() {
			res = res.Elem()
			continue
		}
		return nil, fmt.Errorf("could not unpack addressable value")
	}
}

// UnpackUntilKind unpacks the reflect value until it matches the given kind.
func (v *Value) UnpackUntilKind(k reflect.Kind) (*Value, error) {
	res := v.value
	for {
		if res.Kind() == k {
			return NewValue(res), nil
		}
		if res.Kind() == reflect.Interface || res.Kind() == reflect.Pointer && !res.IsNil() {
			res = res.Elem()
			continue
		}
		return nil, fmt.Errorf("could not unpack to kind: %s", k)
	}
}

// UnpackUntilKinds unpacks the reflect value until it matches the given kind.
func (v *Value) UnpackUntilKinds(kinds ...reflect.Kind) (*Value, error) {
	res := v.value
	for {
		if slices.Contains(kinds, res.Kind()) {
			return NewValue(res), nil
		}
		if res.Kind() == reflect.Interface || res.Kind() == reflect.Pointer && !res.IsNil() {
			res = res.Elem()
			continue
		}
		return nil, fmt.Errorf("could not unpack to kinds: %v", kinds)
	}
}

// Type returns the type of the value.
func (v *Value) Type() Type {
	switch {
	case v.IsString():
		return TypeString
	case v.IsInt():
		return TypeInt
	case v.IsFloat():
		return TypeFloat
	case v.IsBool():
		return TypeBool
	case v.IsMap():
		return TypeMap
	case v.IsSlice():
		return TypeSlice
	case v.IsNull():
		return TypeNull
	default:
		return TypeUnknown
	}
}

func (v *Value) IsScalar() bool {
	unpacked := v.UnpackKinds(reflect.Interface, reflect.Pointer)
	kind := unpacked.Kind()

	switch kind {
	case reflect.String, reflect.Bool, reflect.Int, reflect.Int8, reflect.Int16,
		reflect.Int32, reflect.Int64, reflect.Uint, reflect.Uint8, reflect.Uint16,
		reflect.Uint32, reflect.Uint64, reflect.Float32, reflect.Float64:
		return true
	default:
		return unpacked.isNull()
	}
}

// Len returns the length of the value.
func (v *Value) Len() (int, error) {
	var l int
	var err error

	switch {
	case v.IsSlice():
		l, err = v.SliceLen()
	case v.IsMap():
		l, err = v.MapLen()
	case v.IsString():
		l, err = v.StringLen()
	default:
		err = ErrUnexpectedTypes{
			Expected: []Type{TypeSlice, TypeMap, TypeString},
			Actual:   v.Type(),
		}
	}

	if err != nil {
		return l, err
	}

	return l, nil
}

func (v *Value) Copy() (*Value, error) {
	switch v.Type() {
	case TypeMap:
		return v.MapCopy()
	default:
		return nil, fmt.Errorf("copy not supported for type: %s", v.Type())
	}
}
```

## File: `model/value_comparison.go`
```go
package model

// Compare compares two values.
func (v *Value) Compare(other *Value) (int, error) {
	eq, err := v.Equal(other)
	if err != nil {
		return 0, err
	}
	eqVal, err := eq.BoolValue()
	if err != nil {
		return 0, err
	}
	if eqVal {
		return 0, nil
	}

	lt, err := v.LessThan(other)
	if err != nil {
		return 0, err
	}
	ltVal, err := lt.BoolValue()
	if err != nil {
		return 0, err
	}
	if ltVal {
		return -1, nil
	}

	return 1, nil
}

// Equal compares two values.
func (v *Value) Equal(other *Value) (*Value, error) {
	if v.IsInt() && other.IsFloat() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(float64(a) == b), nil
	}
	if v.IsFloat() && other.IsInt() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a == float64(b)), nil
	}

	if v.Type() != other.Type() {
		return nil, ErrIncompatibleTypes{A: v, B: other}
	}

	isEqual, err := v.EqualTypeValue(other)
	if err != nil {
		return nil, err
	}
	return NewValue(isEqual), nil
}

// NotEqual compares two values.
func (v *Value) NotEqual(other *Value) (*Value, error) {
	equals, err := v.Equal(other)
	if err != nil {
		return nil, err
	}
	boolValue, err := equals.BoolValue()
	if err != nil {
		return nil, err
	}
	return NewValue(!boolValue), nil
}

// LessThan compares two values.
func (v *Value) LessThan(other *Value) (*Value, error) {
	if v.IsInt() && other.IsInt() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a < b), nil
	}
	if v.IsFloat() && other.IsFloat() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a < b), nil
	}
	if v.IsInt() && other.IsFloat() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(float64(a) < b), nil
	}
	if v.IsFloat() && other.IsInt() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a < float64(b)), nil
	}

	if v.IsString() && other.IsString() {
		a, err := v.StringValue()
		if err != nil {
			return nil, err
		}
		b, err := other.StringValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a < b), nil
	}

	return nil, ErrIncompatibleTypes{A: v, B: other}
}

// LessThanOrEqual compares two values.
func (v *Value) LessThanOrEqual(other *Value) (*Value, error) {
	lessThan, err := v.LessThan(other)
	if err != nil {
		return nil, err
	}
	boolValue, err := lessThan.BoolValue()
	if err != nil {
		return nil, err
	}
	equals, err := v.Equal(other)
	if err != nil {
		return nil, err
	}
	boolEquals, err := equals.BoolValue()
	if err != nil {
		return nil, err
	}
	return NewValue(boolValue || boolEquals), nil
}

// GreaterThan compares two values.
func (v *Value) GreaterThan(other *Value) (*Value, error) {
	lessThanOrEqual, err := v.LessThanOrEqual(other)
	if err != nil {
		return nil, err
	}
	boolValue, err := lessThanOrEqual.BoolValue()
	if err != nil {
		return nil, err
	}
	return NewValue(!boolValue), nil
}

// GreaterThanOrEqual compares two values.
func (v *Value) GreaterThanOrEqual(other *Value) (*Value, error) {
	lessThan, err := v.LessThan(other)
	if err != nil {
		return nil, err
	}
	boolValue, err := lessThan.BoolValue()
	if err != nil {
		return nil, err
	}
	return NewValue(!boolValue), nil
}

// EqualTypeValue compares two values of the same type.
func (v *Value) EqualTypeValue(other *Value) (bool, error) {
	if v.Type() != other.Type() {
		return false, nil
	}

	switch v.Type() {
	case TypeString:
		a, err := v.StringValue()
		if err != nil {
			return false, err
		}
		b, err := other.StringValue()
		if err != nil {
			return false, err
		}
		return a == b, nil
	case TypeInt:
		a, err := v.IntValue()
		if err != nil {
			return false, err
		}
		b, err := other.IntValue()
		if err != nil {
			return false, err
		}
		return a == b, nil
	case TypeFloat:
		a, err := v.FloatValue()
		if err != nil {
			return false, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return false, err
		}
		return a == b, nil
	case TypeBool:
		a, err := v.BoolValue()
		if err != nil {
			return false, err
		}
		b, err := other.BoolValue()
		if err != nil {
			return false, err
		}
		return a == b, nil
	case TypeMap:
		a, err := v.MapKeys()
		if err != nil {
			return false, err
		}
		b, err := other.MapKeys()
		if err != nil {
			return false, err
		}
		if len(a) != len(b) {
			return false, nil
		}
		for _, key := range a {
			valA, err := v.GetMapKey(key)
			if err != nil {
				return false, err
			}
			valB, err := other.GetMapKey(key)
			if err != nil {
				return false, err
			}
			equal, err := valA.EqualTypeValue(valB)
			if err != nil {
				return false, err
			}
			if !equal {
				return false, nil
			}
		}
		return true, nil
	case TypeSlice:
		a, err := v.SliceLen()
		if err != nil {
			return false, err
		}
		b, err := other.SliceLen()
		if err != nil {
			return false, err
		}
		if a != b {
			return false, nil
		}
		for i := 0; i < a; i++ {
			valA, err := v.GetSliceIndex(i)
			if err != nil {
				return false, err
			}
			valB, err := other.GetSliceIndex(i)
			if err != nil {
				return false, err
			}
			equal, err := valA.EqualTypeValue(valB)
			if err != nil {
				return false, err
			}
			if !equal {
				return false, nil
			}
		}
		return true, nil
	case TypeNull:
		return other.Type() == TypeNull, nil
	default:
		return false, nil
	}
}
```

## File: `model/value_comparison_test.go`
```go
package model_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

type compareTestCase struct {
	a   *model.Value
	b   *model.Value
	exp bool
}

func TestValue_Equal(t *testing.T) {
	run := func(tc compareTestCase) func(t *testing.T) {
		return func(t *testing.T) {
			got, err := tc.a.Equal(tc.b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			gotBool, err := got.BoolValue()
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if gotBool != tc.exp {
				t.Errorf("expected %v, got %v", tc.exp, got)
			}
		}
	}
	t.Run("string", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a:   model.NewStringValue("hello"),
			b:   model.NewStringValue("hello"),
			exp: true,
		}))
		t.Run("not equal", run(compareTestCase{
			a:   model.NewStringValue("hello"),
			b:   model.NewStringValue("world"),
			exp: false,
		}))
	})
	t.Run("int", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(1),
			exp: true,
		}))
		t.Run("not equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(2),
			exp: false,
		}))
		t.Run("equal float", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(1),
			exp: true,
		}))
		t.Run("not equal float", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(2),
			exp: false,
		}))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.1),
			exp: true,
		}))
		t.Run("not equal", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.2),
			exp: false,
		}))
		t.Run("equal int", run(compareTestCase{
			a:   model.NewFloatValue(1),
			b:   model.NewIntValue(1),
			exp: true,
		}))
		t.Run("not equal int", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewIntValue(1),
			exp: false,
		}))
	})
	t.Run("bool", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a:   model.NewBoolValue(true),
			b:   model.NewBoolValue(true),
			exp: true,
		}))
		t.Run("not equal", run(compareTestCase{
			a:   model.NewBoolValue(true),
			b:   model.NewBoolValue(false),
			exp: false,
		}))
	})
	t.Run("map", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a: model.NewValue(map[string]interface{}{
				"hello": "world",
			}),
			b: model.NewValue(map[string]interface{}{
				"hello": "world",
			}),
			exp: true,
		}))
		t.Run("not equal", run(compareTestCase{
			a: model.NewValue(map[string]interface{}{
				"hello": "world",
			}),
			b: model.NewValue(map[string]interface{}{
				"hello": "world2",
			}),
			exp: false,
		}))
	})
	t.Run("array", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a: model.NewValue([]interface{}{
				"hello", "world",
			}),
			b: model.NewValue([]interface{}{
				"hello", "world",
			}),
			exp: true,
		}))
		t.Run("not equal", run(compareTestCase{
			a: model.NewValue([]interface{}{
				"hello", "world",
			}),
			b: model.NewValue([]interface{}{
				"hello", "world2",
			}),
			exp: false,
		}))
	})
	t.Run("null", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a:   model.NewValue(nil),
			b:   model.NewValue(nil),
			exp: true,
		}))
	})
}

func TestValue_NotEqual(t *testing.T) {
	run := func(tc compareTestCase) func(t *testing.T) {
		return func(t *testing.T) {
			got, err := tc.a.NotEqual(tc.b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			gotBool, err := got.BoolValue()
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if gotBool != tc.exp {
				t.Errorf("expected %v, got %v", tc.exp, got)
			}
		}
	}
	t.Run("string", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a:   model.NewStringValue("hello"),
			b:   model.NewStringValue("hello"),
			exp: false,
		}))
		t.Run("not equal", run(compareTestCase{
			a:   model.NewStringValue("hello"),
			b:   model.NewStringValue("world"),
			exp: true,
		}))
	})
	t.Run("int", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(1),
			exp: false,
		}))
		t.Run("not equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(2),
			exp: true,
		}))
		t.Run("equal float", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(1),
			exp: false,
		}))
		t.Run("not equal float", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(2),
			exp: true,
		}))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.1),
			exp: false,
		}))
		t.Run("not equal", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.2),
			exp: true,
		}))
		t.Run("equal int", run(compareTestCase{
			a:   model.NewFloatValue(1),
			b:   model.NewIntValue(1),
			exp: false,
		}))
		t.Run("not equal int", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewIntValue(1),
			exp: true,
		}))
	})
	t.Run("bool", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a:   model.NewBoolValue(true),
			b:   model.NewBoolValue(true),
			exp: false,
		}))
		t.Run("not equal", run(compareTestCase{
			a:   model.NewBoolValue(true),
			b:   model.NewBoolValue(false),
			exp: true,
		}))
	})
	t.Run("map", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a: model.NewValue(map[string]interface{}{
				"hello": "world",
			}),
			b: model.NewValue(map[string]interface{}{
				"hello": "world",
			}),
			exp: false,
		}))
		t.Run("not equal", run(compareTestCase{
			a: model.NewValue(map[string]interface{}{
				"hello": "world",
			}),
			b: model.NewValue(map[string]interface{}{
				"hello": "world2",
			}),
			exp: true,
		}))
	})
	t.Run("array", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a: model.NewValue([]interface{}{
				"hello", "world",
			}),
			b: model.NewValue([]interface{}{
				"hello", "world",
			}),
			exp: false,
		}))
		t.Run("not equal", run(compareTestCase{
			a: model.NewValue([]interface{}{
				"hello", "world",
			}),
			b: model.NewValue([]interface{}{
				"hello", "world2",
			}),
			exp: true,
		}))
	})
	t.Run("null", func(t *testing.T) {
		t.Run("equal", run(compareTestCase{
			a:   model.NewValue(nil),
			b:   model.NewValue(nil),
			exp: false,
		}))
	})
}

func TestValue_LessThan(t *testing.T) {
	run := func(tc compareTestCase) func(t *testing.T) {
		return func(t *testing.T) {
			got, err := tc.a.LessThan(tc.b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			gotBool, err := got.BoolValue()
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if gotBool != tc.exp {
				t.Errorf("expected %v, got %v", tc.exp, got)
			}
		}
	}
	t.Run("int", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(2),
			exp: true,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewIntValue(2),
			b:   model.NewIntValue(1),
			exp: false,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(1),
			exp: false,
		}))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.2),
			exp: true,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewFloatValue(1.2),
			b:   model.NewFloatValue(1.1),
			exp: false,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.1),
			exp: false,
		}))
	})
	t.Run("int float", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(2),
			exp: true,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewIntValue(2),
			b:   model.NewFloatValue(1),
			exp: false,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(1),
			exp: false,
		}))
	})
	t.Run("float int", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewIntValue(2),
			exp: true,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewFloatValue(2),
			b:   model.NewIntValue(1),
			exp: false,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewFloatValue(1),
			b:   model.NewIntValue(1),
			exp: false,
		}))
	})
	t.Run("string", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewStringValue("a"),
			b:   model.NewStringValue("b"),
			exp: true,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewStringValue("b"),
			b:   model.NewStringValue("a"),
			exp: false,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewStringValue("a"),
			b:   model.NewStringValue("a"),
			exp: false,
		}))
	})
}

func TestValue_LessThanOrEqual(t *testing.T) {
	run := func(tc compareTestCase) func(t *testing.T) {
		return func(t *testing.T) {
			got, err := tc.a.LessThanOrEqual(tc.b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			gotBool, err := got.BoolValue()
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if gotBool != tc.exp {
				t.Errorf("expected %v, got %v", tc.exp, got)
			}
		}
	}
	t.Run("int", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(2),
			exp: true,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewIntValue(2),
			b:   model.NewIntValue(1),
			exp: false,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(1),
			exp: true,
		}))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.2),
			exp: true,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewFloatValue(1.2),
			b:   model.NewFloatValue(1.1),
			exp: false,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.1),
			exp: true,
		}))
	})
	t.Run("int float", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(2),
			exp: true,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewIntValue(2),
			b:   model.NewFloatValue(1),
			exp: false,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(1),
			exp: true,
		}))
	})
	t.Run("float int", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewIntValue(2),
			exp: true,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewFloatValue(2),
			b:   model.NewIntValue(1),
			exp: false,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewFloatValue(1),
			b:   model.NewIntValue(1),
			exp: true,
		}))
	})
	t.Run("string", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewStringValue("a"),
			b:   model.NewStringValue("b"),
			exp: true,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewStringValue("b"),
			b:   model.NewStringValue("a"),
			exp: false,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewStringValue("a"),
			b:   model.NewStringValue("a"),
			exp: true,
		}))
	})
}

func TestValue_GreaterThan(t *testing.T) {
	run := func(tc compareTestCase) func(t *testing.T) {
		return func(t *testing.T) {
			got, err := tc.a.GreaterThan(tc.b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			gotBool, err := got.BoolValue()
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if gotBool != tc.exp {
				t.Errorf("expected %v, got %v", tc.exp, got)
			}
		}
	}
	t.Run("int", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(2),
			exp: false,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewIntValue(2),
			b:   model.NewIntValue(1),
			exp: true,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(1),
			exp: false,
		}))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.2),
			exp: false,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewFloatValue(1.2),
			b:   model.NewFloatValue(1.1),
			exp: true,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.1),
			exp: false,
		}))
	})
	t.Run("int float", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(2),
			exp: false,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewIntValue(2),
			b:   model.NewFloatValue(1),
			exp: true,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(1),
			exp: false,
		}))
	})
	t.Run("float int", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewIntValue(2),
			exp: false,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewFloatValue(2),
			b:   model.NewIntValue(1),
			exp: true,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewFloatValue(1),
			b:   model.NewIntValue(1),
			exp: false,
		}))
	})
	t.Run("string", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewStringValue("a"),
			b:   model.NewStringValue("b"),
			exp: false,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewStringValue("b"),
			b:   model.NewStringValue("a"),
			exp: true,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewStringValue("a"),
			b:   model.NewStringValue("a"),
			exp: false,
		}))
	})
}

func TestValue_GreaterThanOrEqual(t *testing.T) {
	run := func(tc compareTestCase) func(t *testing.T) {
		return func(t *testing.T) {
			got, err := tc.a.GreaterThanOrEqual(tc.b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			gotBool, err := got.BoolValue()
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if gotBool != tc.exp {
				t.Errorf("expected %v, got %v", tc.exp, got)
			}
		}
	}
	t.Run("int", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(2),
			exp: false,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewIntValue(2),
			b:   model.NewIntValue(1),
			exp: true,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewIntValue(1),
			exp: true,
		}))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.2),
			exp: false,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewFloatValue(1.2),
			b:   model.NewFloatValue(1.1),
			exp: true,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewFloatValue(1.1),
			exp: true,
		}))
	})
	t.Run("int float", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(2),
			exp: false,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewIntValue(2),
			b:   model.NewFloatValue(1),
			exp: true,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewIntValue(1),
			b:   model.NewFloatValue(1),
			exp: true,
		}))
	})
	t.Run("float int", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewFloatValue(1.1),
			b:   model.NewIntValue(2),
			exp: false,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewFloatValue(2),
			b:   model.NewIntValue(1),
			exp: true,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewFloatValue(1),
			b:   model.NewIntValue(1),
			exp: true,
		}))
	})
	t.Run("string", func(t *testing.T) {
		t.Run("less", run(compareTestCase{
			a:   model.NewStringValue("a"),
			b:   model.NewStringValue("b"),
			exp: false,
		}))
		t.Run("greater", run(compareTestCase{
			a:   model.NewStringValue("b"),
			b:   model.NewStringValue("a"),
			exp: true,
		}))
		t.Run("equal", run(compareTestCase{
			a:   model.NewStringValue("a"),
			b:   model.NewStringValue("a"),
			exp: true,
		}))
	})
}

func TestValue_Compare(t *testing.T) {
	run := func(a *model.Value, b *model.Value, exp int) func(t *testing.T) {
		return func(t *testing.T) {
			got, err := a.Compare(b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if got != exp {
				t.Errorf("expected %d, got %d", exp, got)
			}
		}
	}
	t.Run("int", func(t *testing.T) {
		t.Run("less", run(
			model.NewIntValue(1),
			model.NewIntValue(2),
			-1,
		))
		t.Run("greater", run(
			model.NewIntValue(2),
			model.NewIntValue(1),
			1,
		))
		t.Run("equal", run(
			model.NewIntValue(1),
			model.NewIntValue(1),
			0,
		))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("less", run(
			model.NewFloatValue(1.1),
			model.NewFloatValue(1.2),
			-1,
		))
		t.Run("greater", run(
			model.NewFloatValue(1.2),
			model.NewFloatValue(1.1),
			1,
		))
		t.Run("equal", run(
			model.NewFloatValue(1.1),
			model.NewFloatValue(1.1),
			0,
		))
	})
	t.Run("int float", func(t *testing.T) {
		t.Run("less", run(
			model.NewIntValue(1),
			model.NewFloatValue(2),
			-1,
		))
		t.Run("greater", run(
			model.NewIntValue(2),
			model.NewFloatValue(1),
			1,
		))
		t.Run("equal", run(
			model.NewIntValue(1),
			model.NewFloatValue(1),
			0,
		))
	})
	t.Run("float int", func(t *testing.T) {
		t.Run("less", run(
			model.NewFloatValue(1.1),
			model.NewIntValue(2),
			-1,
		))
		t.Run("greater", run(
			model.NewFloatValue(1.1),
			model.NewIntValue(1),
			1,
		))
		t.Run("equal", run(
			model.NewFloatValue(1),
			model.NewIntValue(1),
			0,
		))
	})
	t.Run("string", func(t *testing.T) {
		t.Run("less", run(
			model.NewStringValue("a"),
			model.NewStringValue("b"),
			-1,
		))
		t.Run("greater", run(
			model.NewStringValue("b"),
			model.NewStringValue("a"),
			1,
		))
		t.Run("equal", run(
			model.NewStringValue("a"),
			model.NewStringValue("a"),
			0,
		))
	})
}
```

## File: `model/value_literal.go`
```go
package model

import (
	"reflect"
	"slices"
)

func newPtr() reflect.Value {
	return reflect.New(reflect.TypeFor[any]())
}

// NewNullValue creates a new Value with a nil value.
func NewNullValue() *Value {
	return NewValue(newPtr())
}

// IsNull returns true if the value is null.
func (v *Value) IsNull() bool {
	return v.UnpackKinds(reflect.Pointer, reflect.Interface).isNull()
}

func (v *Value) isNull() bool {
	// This logic can be cleaned up.
	unpacked, err := v.UnpackUntilKinds(reflect.Chan, reflect.Func, reflect.Map, reflect.Pointer, reflect.UnsafePointer, reflect.Interface, reflect.Slice)
	if err != nil {
		return false
	}
	return unpacked.value.IsNil()
}

// NewStringValue creates a new Value with a string value.
func NewStringValue(x string) *Value {
	res := newPtr()
	res.Elem().Set(reflect.ValueOf(x))
	return NewValue(res)
}

// IsString returns true if the value is a string.
func (v *Value) IsString() bool {
	return v.UnpackKinds(reflect.Pointer, reflect.Interface).isString()
}

func (v *Value) isString() bool {
	return v.value.Kind() == reflect.String
}

// StringValue returns the string value of the Value.
func (v *Value) StringValue() (string, error) {
	unpacked := v.UnpackKinds(reflect.Pointer, reflect.Interface)
	if !unpacked.isString() {
		return "", ErrUnexpectedType{
			Expected: TypeString,
			Actual:   v.Type(),
		}
	}
	return unpacked.value.String(), nil
}

// StringLen returns the length of the string.
func (v *Value) StringLen() (int, error) {
	val, err := v.StringValue()
	if err != nil {
		return 0, err
	}
	return len(val), nil
}

// StringIndexRange returns a new string containing the values between the start and end indexes.
// Comparable to go's string[start:end].
func (v *Value) StringIndexRange(start, end int) (*Value, error) {
	strVal, err := v.StringValue()
	if err != nil {
		return nil, err
	}

	inBytes := []rune(strVal)
	l := len(inBytes)

	if start < 0 {
		start = l + start
	}
	if end < 0 {
		end = l + end
	}

	resBytes := make([]rune, 0)

	if start > end {
		for i := start; i >= end; i-- {
			resBytes = append(resBytes, inBytes[i])
		}
	} else {
		for i := start; i <= end; i++ {
			resBytes = append(resBytes, inBytes[i])
		}
	}

	res := string(resBytes)

	return NewStringValue(res), nil
}

// NewIntValue creates a new Value with an int value.
func NewIntValue(x int64) *Value {
	res := newPtr()
	res.Elem().Set(reflect.ValueOf(x))
	return NewValue(res)
}

// IsInt returns true if the value is an int.
func (v *Value) IsInt() bool {
	return v.UnpackKinds(reflect.Pointer, reflect.Interface).isInt()
}

func (v *Value) isInt() bool {
	return slices.Contains([]reflect.Kind{reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64}, v.value.Kind())
}

// IntValue returns the int value of the Value.
func (v *Value) IntValue() (int64, error) {
	unpacked := v.UnpackKinds(reflect.Pointer, reflect.Interface)
	if !unpacked.isInt() {
		return 0, ErrUnexpectedType{
			Expected: TypeInt,
			Actual:   v.Type(),
		}
	}
	return unpacked.value.Int(), nil
}

// NewFloatValue creates a new Value with a float value.
func NewFloatValue(x float64) *Value {
	res := newPtr()
	res.Elem().Set(reflect.ValueOf(x))
	return NewValue(res)
}

// IsFloat returns true if the value is a float.
func (v *Value) IsFloat() bool {
	return v.UnpackKinds(reflect.Pointer, reflect.Interface).isFloat()
}

func (v *Value) isFloat() bool {
	return slices.Contains([]reflect.Kind{reflect.Float32, reflect.Float64}, v.value.Kind())
}

// FloatValue returns the float value of the Value.
func (v *Value) FloatValue() (float64, error) {
	unpacked := v.UnpackKinds(reflect.Pointer, reflect.Interface)
	if !unpacked.IsFloat() {
		return 0, ErrUnexpectedType{
			Expected: TypeFloat,
			Actual:   v.Type(),
		}
	}
	return unpacked.value.Float(), nil
}

// NewBoolValue creates a new Value with a bool value.
func NewBoolValue(x bool) *Value {
	res := newPtr()
	res.Elem().Set(reflect.ValueOf(x))
	return NewValue(res)
}

// IsBool returns true if the value is a bool.
func (v *Value) IsBool() bool {
	return v.UnpackKinds(reflect.Pointer, reflect.Interface).isBool()
}

func (v *Value) isBool() bool {
	return v.value.Kind() == reflect.Bool
}

// BoolValue returns the bool value of the Value.
func (v *Value) BoolValue() (bool, error) {
	unpacked := v.UnpackKinds(reflect.Pointer, reflect.Interface)
	if !unpacked.IsBool() {
		return false, ErrUnexpectedType{
			Expected: TypeBool,
			Actual:   v.Type(),
		}
	}
	return unpacked.value.Bool(), nil
}
```

## File: `model/value_literal_test.go`
```go
package model_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestValue_IsNull(t *testing.T) {
	v := model.NewNullValue()
	if !v.IsNull() {
		t.Fatalf("expected value to be null")
	}
}
```

## File: `model/value_map.go`
```go
package model

import (
	"errors"
	"fmt"
	"reflect"

	"github.com/tomwright/dasel/v3/model/orderedmap"
)

// NewMapValue creates a new map value.
func NewMapValue() *Value {
	return NewValue(orderedmap.NewMap())
}

// IsMap returns true if the value is a map.
func (v *Value) IsMap() bool {
	return v.isStandardMap() || v.isDencodingMap()
}

func (v *Value) isStandardMap() bool {
	return v.UnpackKinds(reflect.Interface, reflect.Pointer).Kind() == reflect.Map
}

func (v *Value) isDencodingMap() bool {
	return v.UnpackKinds(reflect.Interface, reflect.Pointer).value.Type() == reflect.TypeFor[orderedmap.Map]()
}

func (v *Value) dencodingMapValue() (*orderedmap.Map, error) {
	if v.isDencodingMap() {
		m, err := v.UnpackUntilType(reflect.TypeFor[*orderedmap.Map]())
		if err != nil {
			return nil, fmt.Errorf("error getting map: %w", err)
		}
		return m.value.Interface().(*orderedmap.Map), nil
	}
	return nil, fmt.Errorf("value is not a dencoding map")
}

// SetMapKey sets the value at the specified key in the map.
func (v *Value) SetMapKey(key string, value *Value) error {
	switch {
	case v.isDencodingMap():
		m, err := v.dencodingMapValue()
		if err != nil {
			return fmt.Errorf("error getting map: %w", err)
		}
		m.Set(key, value)
		return nil
	case v.isStandardMap():
		unpacked, err := v.UnpackUntilKind(reflect.Map)
		if err != nil {
			return fmt.Errorf("error unpacking value: %w", err)
		}
		unpacked.value.SetMapIndex(reflect.ValueOf(key), value.value)
		return nil
	default:
		return fmt.Errorf("value is not a map")
	}
}

func (v *Value) MapCopy() (*Value, error) {
	res := NewMapValue()
	kvs, err := v.MapKeyValues()
	if err != nil {
		return nil, fmt.Errorf("error getting map key values: %w", err)
	}
	for _, kv := range kvs {
		if err := res.SetMapKey(kv.Key, kv.Value); err != nil {
			return nil, fmt.Errorf("error setting map key: %w", err)
		}
	}
	return res, nil
}

func (v *Value) MapKeyExists(key string) (bool, error) {
	_, err := v.GetMapKey(key)
	if err != nil && !errors.As(err, &MapKeyNotFound{}) {
		return false, err
	}
	return err == nil, nil
}

// GetMapKey returns the value at the specified key in the map.
func (v *Value) GetMapKey(key string) (*Value, error) {
	switch {
	case v.isDencodingMap():
		m, err := v.dencodingMapValue()
		if err != nil {
			return nil, fmt.Errorf("error getting map: %w", err)
		}
		val, ok := m.Get(key)
		if !ok {
			return nil, MapKeyNotFound{Key: key}
		}
		if modelValue, isValue := val.(*Value); isValue {
			modelValue.setFn = func(newValue *Value) error {
				m.Set(key, newValue)
				return nil
			}
			return modelValue, nil
		}
		res := NewValue(val)
		res.setFn = func(newValue *Value) error {
			m.Set(key, newValue)
			return nil
		}
		return res, nil
	case v.isStandardMap():
		unpacked, err := v.UnpackUntilKind(reflect.Map)
		if err != nil {
			return nil, fmt.Errorf("error unpacking value: %w", err)
		}
		i := unpacked.value.MapIndex(reflect.ValueOf(key))
		if !i.IsValid() {
			return nil, MapKeyNotFound{Key: key}
		}
		res := NewValue(i)
		res.setFn = func(newValue *Value) error {
			mapRv, err := v.UnpackUntilKind(reflect.Map)
			if err != nil {
				return fmt.Errorf("error unpacking value: %w", err)
			}
			mapRv.value.SetMapIndex(reflect.ValueOf(key), newValue.value)
			return nil
		}
		return res, nil
	default:
		return nil, ErrUnexpectedType{
			Expected: TypeMap,
			Actual:   v.Type(),
		}
	}
}

// DeleteMapKey deletes the key from the map.
func (v *Value) DeleteMapKey(key string) error {
	switch {
	case v.isDencodingMap():
		m, err := v.dencodingMapValue()
		if err != nil {
			return fmt.Errorf("error getting map: %w", err)
		}
		m.Delete(key)
		return nil
	case v.isStandardMap():
		unpacked, err := v.UnpackUntilKind(reflect.Map)
		if err != nil {
			return fmt.Errorf("error unpacking value: %w", err)
		}
		unpacked.value.SetMapIndex(reflect.ValueOf(key), reflect.Value{})
		return nil
	default:
		return ErrUnexpectedType{
			Expected: TypeMap,
			Actual:   v.Type(),
		}
	}
}

// MapKeys returns a list of keys in the map.
func (v *Value) MapKeys() ([]string, error) {
	switch {
	case v.isDencodingMap():
		m, err := v.dencodingMapValue()
		if err != nil {
			return nil, fmt.Errorf("error getting map: %w", err)
		}
		return m.Keys(), nil
	case v.isStandardMap():
		unpacked, err := v.UnpackUntilKind(reflect.Map)
		if err != nil {
			return nil, fmt.Errorf("error unpacking value: %w", err)
		}
		keys := unpacked.value.MapKeys()
		strKeys := make([]string, len(keys))
		for i, k := range keys {
			strKeys[i] = k.String()
		}
		return strKeys, nil
	default:
		return nil, ErrUnexpectedType{
			Expected: TypeMap,
			Actual:   v.Type(),
		}
	}
}

// RangeMap iterates over each key in the map and calls the provided function with the key and value.
func (v *Value) RangeMap(f func(string, *Value) error) error {
	keys, err := v.MapKeys()
	if err != nil {
		return fmt.Errorf("error getting map keys: %w", err)
	}

	for _, k := range keys {
		va, err := v.GetMapKey(k)
		if err != nil {
			return fmt.Errorf("error getting map key: %w", err)
		}
		if err := f(k, va); err != nil {
			return err
		}
	}

	return nil
}

// MapKeyValues returns a list of key value pairs in the map.
func (v *Value) MapKeyValues() ([]KeyValue, error) {
	keys, err := v.MapKeys()
	if err != nil {
		return nil, fmt.Errorf("error getting map keys: %w", err)
	}

	kvs := make([]KeyValue, len(keys))

	for i, k := range keys {
		va, err := v.GetMapKey(k)
		if err != nil {
			return nil, fmt.Errorf("error getting map key: %w", err)
		}
		kvs[i] = KeyValue{
			Key:   k,
			Value: va,
		}
	}

	return kvs, nil
}

// MapLen returns the length of the slice.
func (v *Value) MapLen() (int, error) {
	keys, err := v.MapKeys()
	if err != nil {
		return 0, err
	}
	return len(keys), nil
}
```

## File: `model/value_map_test.go`
```go
package model_test

import (
	"errors"
	"testing"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/model/orderedmap"
)

func TestMap(t *testing.T) {
	standardMap := func() *model.Value {
		return model.NewValue(map[string]interface{}{
			"foo": "foo1",
			"bar": "bar1",
		})
	}

	dencodingMap := func() *model.Value {
		return model.NewValue(orderedmap.NewMap().
			Set("foo", "foo1").
			Set("bar", "bar1"))
	}

	modelMap := func() *model.Value {
		res := model.NewMapValue()
		if err := res.SetMapKey("foo", model.NewValue("foo1")); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		if err := res.SetMapKey("bar", model.NewValue("bar1")); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		return res
	}

	runTests := func(v func() *model.Value) func(t *testing.T) {
		return func(t *testing.T) {
			t.Run("IsMap", func(t *testing.T) {
				v := v()
				if !v.IsMap() {
					t.Errorf("expected value to be a map")
				}
			})
			t.Run("GetMapKey", func(t *testing.T) {
				v := v()
				foo, err := v.GetMapKey("foo")
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				got, err := foo.StringValue()
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				if got != "foo1" {
					t.Errorf("expected foo1, got %s", got)
				}
			})
			t.Run("SetMapKey", func(t *testing.T) {
				v := v()
				if err := v.SetMapKey("baz", model.NewValue("baz1")); err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				baz, err := v.GetMapKey("baz")
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				got, err := baz.StringValue()
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				if got != "baz1" {
					t.Errorf("expected baz1, got %s", got)
				}
			})
			t.Run("MapKeys", func(t *testing.T) {
				v := v()
				keys, err := v.MapKeys()
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				if len(keys) != 2 {
					t.Errorf("expected 2 keys, got %d", len(keys))
				}
				exp := []string{"foo", "bar"}
				for _, k := range exp {
					var found bool
					for _, e := range keys {
						if e == k {
							found = true
							break
						}
					}
					if !found {
						t.Errorf("expected key %s not found", k)
					}
				}
			})
			t.Run("RangeMap", func(t *testing.T) {
				v := v()
				var keys []string
				err := v.RangeMap(func(k string, v *model.Value) error {
					keys = append(keys, k)
					return nil
				})
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				if len(keys) != 2 {
					t.Errorf("expected 2 keys, got %d", len(keys))
				}
				exp := []string{"foo", "bar"}
				for _, k := range exp {
					var found bool
					for _, e := range keys {
						if e == k {
							found = true
							break
						}
					}
					if !found {
						t.Errorf("expected key %s not found", k)
					}
				}
			})
			t.Run("DeleteMapKey", func(t *testing.T) {
				v := v()
				if _, err := v.GetMapKey("foo"); err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				if err := v.DeleteMapKey("foo"); err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				_, err := v.GetMapKey("foo")
				if !errors.As(err, &model.MapKeyNotFound{}) {
					t.Errorf("expected key not found error, got %s", err)
				}
			})
		}
	}

	t.Run("standard map", runTests(standardMap))
	t.Run("dencoding map", runTests(dencodingMap))
	t.Run("model map", runTests(modelMap))
}
```

## File: `model/value_math.go`
```go
package model

import (
	fmt "fmt"
	"math"
)

// Add adds two values together.
func (v *Value) Add(other *Value) (*Value, error) {
	if v.IsInt() && other.IsInt() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a + b), nil
	}
	if v.IsFloat() && other.IsFloat() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a + b), nil
	}
	if v.IsInt() && other.IsFloat() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(float64(a) + b), nil
	}
	if v.IsFloat() && other.IsInt() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a + float64(b)), nil
	}
	if v.IsString() && other.IsString() {
		a, err := v.StringValue()
		if err != nil {
			return nil, err
		}
		b, err := other.StringValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a + b), nil
	}
	return nil, fmt.Errorf("could not add: %w", ErrIncompatibleTypes{A: v, B: other})
}

// Subtract returns the difference between two values.
func (v *Value) Subtract(other *Value) (*Value, error) {
	if v.IsInt() && other.IsInt() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a - b), nil
	}
	if v.IsFloat() && other.IsFloat() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a - b), nil
	}
	if v.IsInt() && other.IsFloat() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(float64(a) - b), nil
	}
	if v.IsFloat() && other.IsInt() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a - float64(b)), nil
	}
	return nil, fmt.Errorf("could not subtract: %w", ErrIncompatibleTypes{A: v, B: other})
}

// Multiply returns the product of the two values.
func (v *Value) Multiply(other *Value) (*Value, error) {
	if v.IsInt() && other.IsInt() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a * b), nil
	}
	if v.IsFloat() && other.IsFloat() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a * b), nil
	}
	if v.IsInt() && other.IsFloat() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(float64(a) * b), nil
	}
	if v.IsFloat() && other.IsInt() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a * float64(b)), nil
	}
	return nil, fmt.Errorf("could not multiply: %w", ErrIncompatibleTypes{A: v, B: other})
}

// Divide returns the result of dividing the value by another value.
func (v *Value) Divide(other *Value) (*Value, error) {
	if v.IsInt() && other.IsInt() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a / b), nil
	}
	if v.IsFloat() && other.IsFloat() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a / b), nil
	}
	if v.IsInt() && other.IsFloat() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(float64(a) / b), nil
	}
	if v.IsFloat() && other.IsInt() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a / float64(b)), nil
	}
	return nil, fmt.Errorf("could not divide: %w", ErrIncompatibleTypes{A: v, B: other})
}

// Modulo returns the remainder of the division of two values.
func (v *Value) Modulo(other *Value) (*Value, error) {
	if v.IsInt() && other.IsInt() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(a % b), nil
	}
	if v.IsFloat() && other.IsFloat() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(math.Mod(a, b)), nil
	}
	if v.IsInt() && other.IsFloat() {
		a, err := v.IntValue()
		if err != nil {
			return nil, err
		}
		b, err := other.FloatValue()
		if err != nil {
			return nil, err
		}
		return NewValue(math.Mod(float64(a), b)), nil
	}
	if v.IsFloat() && other.IsInt() {
		a, err := v.FloatValue()
		if err != nil {
			return nil, err
		}
		b, err := other.IntValue()
		if err != nil {
			return nil, err
		}
		return NewValue(math.Mod(a, float64(b))), nil
	}
	return nil, fmt.Errorf("could not modulo: %w", ErrIncompatibleTypes{A: v, B: other})
}
```

## File: `model/value_math_test.go`
```go
package model_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestValue_Add(t *testing.T) {
	run := func(a, b *model.Value, exp *model.Value) func(*testing.T) {
		return func(t *testing.T) {
			got, err := a.Add(b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			eq, err := got.EqualTypeValue(exp)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if !eq {
				t.Errorf("expected %v, got %v", exp, got)
			}
		}
	}
	t.Run("int", func(t *testing.T) {
		t.Run("int", run(model.NewIntValue(1), model.NewIntValue(2), model.NewIntValue(3)))
		t.Run("float", run(model.NewIntValue(1), model.NewFloatValue(2), model.NewFloatValue(3)))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("int", run(model.NewFloatValue(1), model.NewIntValue(2), model.NewFloatValue(3)))
		t.Run("float", run(model.NewFloatValue(1), model.NewFloatValue(2), model.NewFloatValue(3)))
	})
	t.Run("string", func(t *testing.T) {
		t.Run("string", run(model.NewStringValue("hello"), model.NewStringValue(" world"), model.NewStringValue("hello world")))
	})
}

func TestValue_Subtract(t *testing.T) {
	run := func(a, b *model.Value, exp *model.Value) func(*testing.T) {
		return func(t *testing.T) {
			got, err := a.Subtract(b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			eq, err := got.EqualTypeValue(exp)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if !eq {
				t.Errorf("expected %v, got %v", exp, got)
			}
		}
	}
	t.Run("int", func(t *testing.T) {
		t.Run("int", run(model.NewIntValue(3), model.NewIntValue(2), model.NewIntValue(1)))
		t.Run("float", run(model.NewIntValue(3), model.NewFloatValue(2), model.NewFloatValue(1)))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("int", run(model.NewFloatValue(3), model.NewIntValue(2), model.NewFloatValue(1)))
		t.Run("float", run(model.NewFloatValue(3), model.NewFloatValue(2), model.NewFloatValue(1)))
	})
}

func TestValue_Multiply(t *testing.T) {
	run := func(a, b *model.Value, exp *model.Value) func(*testing.T) {
		return func(t *testing.T) {
			got, err := a.Multiply(b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			eq, err := got.EqualTypeValue(exp)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if !eq {
				t.Errorf("expected %v, got %v", exp, got)
			}
		}
	}
	t.Run("int", func(t *testing.T) {
		t.Run("int", run(model.NewIntValue(3), model.NewIntValue(2), model.NewIntValue(6)))
		t.Run("float", run(model.NewIntValue(3), model.NewFloatValue(2), model.NewFloatValue(6)))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("int", run(model.NewFloatValue(3), model.NewIntValue(2), model.NewFloatValue(6)))
		t.Run("float", run(model.NewFloatValue(3), model.NewFloatValue(2), model.NewFloatValue(6)))
	})
}

func TestValue_Divide(t *testing.T) {
	run := func(a, b *model.Value, exp *model.Value) func(*testing.T) {
		return func(t *testing.T) {
			got, err := a.Divide(b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			eq, err := got.EqualTypeValue(exp)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if !eq {
				t.Errorf("expected %v, got %v", exp, got)
			}
		}
	}
	t.Run("int", func(t *testing.T) {
		t.Run("int", run(model.NewIntValue(6), model.NewIntValue(2), model.NewIntValue(3)))
		t.Run("float", run(model.NewIntValue(6), model.NewFloatValue(2), model.NewFloatValue(3)))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("int", run(model.NewFloatValue(6), model.NewIntValue(2), model.NewFloatValue(3)))
		t.Run("float", run(model.NewFloatValue(6), model.NewFloatValue(2), model.NewFloatValue(3)))
	})
}

func TestValue_Modulo(t *testing.T) {
	run := func(a, b *model.Value, exp *model.Value) func(*testing.T) {
		return func(t *testing.T) {
			got, err := a.Modulo(b)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			eq, err := got.EqualTypeValue(exp)
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if !eq {
				t.Errorf("expected %v, got %v", exp, got)
			}
		}
	}
	t.Run("int", func(t *testing.T) {
		t.Run("int", run(model.NewIntValue(10), model.NewIntValue(3), model.NewIntValue(1)))
		t.Run("float", run(model.NewIntValue(10), model.NewFloatValue(3), model.NewFloatValue(1)))
	})
	t.Run("float", func(t *testing.T) {
		t.Run("int", run(model.NewFloatValue(10), model.NewIntValue(3), model.NewFloatValue(1)))
		t.Run("float", run(model.NewFloatValue(10), model.NewFloatValue(3), model.NewFloatValue(1)))
	})
}
```

## File: `model/value_metadata.go`
```go
package model

// MetadataValue returns a metadata value.
func (v *Value) MetadataValue(key string) (any, bool) {
	if v.Metadata == nil {
		return nil, false
	}
	val, ok := v.Metadata[key]
	return val, ok
}

// SetMetadataValue sets a metadata value.
func (v *Value) SetMetadataValue(key string, val any) {
	if v.Metadata == nil {
		v.Metadata = map[string]any{}
	}
	v.Metadata[key] = val
}

// IsSpread returns true if the value is a spread value.
// Spread values are used to represent the spread operator.
func (v *Value) IsSpread() bool {
	if v == nil {
		return false
	}
	val, ok := v.MetadataValue("spread")
	if !ok {
		return false
	}
	spread, ok := val.(bool)
	return ok && spread
}

// MarkAsSpread marks the value as a spread value.
// Spread values are used to represent the spread operator.
func (v *Value) MarkAsSpread() {
	v.SetMetadataValue("spread", true)
}

// IsBranch returns true if the value is a branched value.
func (v *Value) IsBranch() bool {
	if v == nil {
		return false
	}
	val, ok := v.MetadataValue("branch")
	if !ok {
		return false
	}
	branch, ok := val.(bool)
	return ok && branch
}

// MarkAsBranch marks the value as a branch value.
func (v *Value) MarkAsBranch() {
	v.SetMetadataValue("branch", true)
}

// IsIgnore returns true if value should be ignored.
func (v *Value) IsIgnore() bool {
	if v == nil {
		return false
	}
	val, ok := v.MetadataValue("ignore")
	if !ok {
		return false
	}
	ignore, ok := val.(bool)
	return ok && ignore
}

// MarkAsIgnore marks the value to be ignored.
func (v *Value) MarkAsIgnore() {
	v.SetMetadataValue("ignore", true)
}
```

## File: `model/value_metadata_test.go`
```go
package model_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestValue_IsBranch(t *testing.T) {
	val := model.NewNullValue()
	if exp, got := false, val.IsBranch(); exp != got {
		t.Errorf("expected %v, got %v", exp, got)
	}
	val.MarkAsBranch()
	if exp, got := true, val.IsBranch(); exp != got {
		t.Errorf("expected %v, got %v", exp, got)
	}
}

func TestValue_IsSpread(t *testing.T) {
	val := model.NewNullValue()
	if exp, got := false, val.IsSpread(); exp != got {
		t.Errorf("expected %v, got %v", exp, got)
	}
	val.MarkAsSpread()
	if exp, got := true, val.IsSpread(); exp != got {
		t.Errorf("expected %v, got %v", exp, got)
	}
}
```

## File: `model/value_set.go`
```go
package model

import (
	"fmt"
	"reflect"
)

// Set sets the value of the value.
func (v *Value) Set(newValue *Value) error {
	if v.isDaselValue() {
		dv, err := v.daselValue()
		if err != nil {
			return err
		}
		return dv.Set(newValue)
	}

	if v.setFn != nil {
		return v.setFn(newValue)
	}

	a, err := v.UnpackUntilAddressable()
	if err != nil {
		return err
	}

	b := newValue.UnpackKinds(reflect.Pointer)
	if a.Kind() == b.Kind() {
		a.value.Set(b.value)
		return nil
	}

	b = newValue.UnpackKinds(reflect.Pointer, reflect.Interface)
	if a.Kind() == b.Kind() {
		a.value.Set(b.value)
		return nil
	}

	// These are commented out because I don't think they are needed.

	//if a.Kind() == newValue.Kind() {
	//	a.Value.Set(newValue.Value)
	//	return nil
	//}

	//b = newValue.UnpackKinds(reflect.Interface)
	//if a.Kind() == b.Kind() {
	//	a.Value.Set(b.Value)
	//	return nil
	//}

	//b = newValue.UnpackKinds(reflect.Pointer, reflect.Interface)
	//if a.Kind() == b.Kind() {
	//	a.Value.Set(b.Value)
	//	return nil
	//}

	//b, err = newValue.UnpackUntilAddressable()
	//if err != nil {
	//	return err
	//}
	//if a.Kind() == b.Kind() {
	//	a.Value.Set(b.Value)
	//	return nil
	//}

	// This is a hard limitation at the moment.
	// If the types are not the same, we cannot set the value.
	return fmt.Errorf("could not set %s value on %s value", newValue.Type(), v.Type())
}
```

## File: `model/value_set_test.go`
```go
package model_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

type setTestCase struct {
	valueFn    func() *model.Value
	value      *model.Value
	newValueFn func() *model.Value
	newValue   *model.Value
}

func (tc setTestCase) run(t *testing.T) {
	val := tc.value
	if tc.valueFn != nil {
		val = tc.valueFn()
	}
	newVal := tc.newValue
	if tc.newValueFn != nil {
		newVal = tc.newValueFn()
	}
	if err := val.Set(newVal); err != nil {
		t.Errorf("unexpected error: %s", err)
		return
	}

	eq, err := val.EqualTypeValue(newVal)
	if err != nil {
		t.Errorf("unexpected error: %s", err)
		return
	}
	if !eq {
		t.Errorf("expected values to be equal")
	}
}

func TestValue_Set(t *testing.T) {
	testCases := []struct {
		name        string
		stringValue func() *model.Value
		intValue    func() *model.Value
		floatValue  func() *model.Value
		boolValue   func() *model.Value
		mapValue    func() *model.Value
		sliceValue  func() *model.Value
		nullValue   func() *model.Value
	}{
		{
			name: "model constructor",
			stringValue: func() *model.Value {
				return model.NewStringValue("hello")
			},
			intValue: func() *model.Value {
				return model.NewIntValue(1)
			},
			floatValue: func() *model.Value {
				return model.NewFloatValue(1)
			},
			boolValue: func() *model.Value {
				return model.NewBoolValue(true)
			},
			mapValue: func() *model.Value {
				res := model.NewMapValue()
				if err := res.SetMapKey("greeting", model.NewStringValue("hello")); err != nil {
					t.Fatal(err)
				}
				return res
			},
			sliceValue: func() *model.Value {
				res := model.NewSliceValue()
				if err := res.Append(model.NewStringValue("hello")); err != nil {
					t.Fatal(err)
				}
				return res
			},
			nullValue: func() *model.Value {
				return model.NewNullValue()
			},
		},
		{
			name: "go types non ptr",
			stringValue: func() *model.Value {
				v := "hello"
				return model.NewValue(v)
			},
			intValue: func() *model.Value {
				v := int64(1)
				return model.NewValue(v)
			},
			floatValue: func() *model.Value {
				v := 1.0
				return model.NewValue(v)
			},
			boolValue: func() *model.Value {
				v := true
				return model.NewValue(v)
			},
			mapValue: func() *model.Value {
				v := map[string]interface{}{
					"greeting": "hello",
				}
				return model.NewValue(v)
			},
			sliceValue: func() *model.Value {
				v := []interface{}{
					"hello",
				}
				return model.NewValue(v)
			},
			nullValue: func() *model.Value {
				return model.NewValue(nil)
			},
		},
		{
			name: "go types ptr",
			stringValue: func() *model.Value {
				v := "hello"
				return model.NewValue(&v)
			},
			intValue: func() *model.Value {
				v := int64(1)
				return model.NewValue(&v)
			},
			floatValue: func() *model.Value {
				v := 1.0
				return model.NewValue(&v)
			},
			boolValue: func() *model.Value {
				v := true
				return model.NewValue(&v)
			},
			mapValue: func() *model.Value {
				v := map[string]interface{}{
					"greeting": "hello",
				}
				return model.NewValue(&v)
			},
			sliceValue: func() *model.Value {
				v := []interface{}{
					"hello",
				}
				return model.NewValue(&v)
			},
			nullValue: func() *model.Value {
				var x any
				return model.NewValue(&x)
			},
		},
	}

	for _, testCase := range testCases {
		tc := testCase
		t.Run(tc.name, func(t *testing.T) {
			t.Run("string", setTestCase{
				valueFn:  tc.stringValue,
				newValue: model.NewStringValue("world"),
			}.run)
			t.Run("int", setTestCase{
				valueFn:  tc.intValue,
				newValue: model.NewIntValue(2),
			}.run)
			t.Run("float", setTestCase{
				valueFn:  tc.floatValue,
				newValue: model.NewFloatValue(2),
			}.run)
			t.Run("bool", setTestCase{
				valueFn:  tc.boolValue,
				newValue: model.NewBoolValue(false),
			}.run)
			t.Run("map", setTestCase{
				valueFn: tc.mapValue,
				newValueFn: func() *model.Value {
					res := model.NewMapValue()
					if err := res.SetMapKey("greeting", model.NewStringValue("world")); err != nil {
						t.Fatal(err)
					}
					return res
				},
			}.run)
			t.Run("slice", setTestCase{
				valueFn: tc.sliceValue,
				newValueFn: func() *model.Value {
					res := model.NewSliceValue()
					if err := res.Append(model.NewStringValue("world")); err != nil {
						t.Fatal(err)
					}
					return res
				},
			}.run)
			t.Run("string over int", setTestCase{
				valueFn:  tc.intValue,
				newValue: model.NewStringValue("world"),
			}.run)
			t.Run("int over float", setTestCase{
				valueFn:  tc.floatValue,
				newValue: model.NewIntValue(2),
			}.run)
			t.Run("float over bool", setTestCase{
				valueFn:  tc.boolValue,
				newValue: model.NewFloatValue(2),
			}.run)
			t.Run("bool over map", setTestCase{
				valueFn:  tc.mapValue,
				newValue: model.NewBoolValue(true),
			}.run)
			t.Run("map over slice", setTestCase{
				valueFn: tc.sliceValue,
				newValueFn: func() *model.Value {
					res := model.NewMapValue()
					if err := res.SetMapKey("greeting", model.NewStringValue("world")); err != nil {
						t.Fatal(err)
					}
					return res
				},
			}.run)
			t.Run("string over slice", setTestCase{
				valueFn:  tc.sliceValue,
				newValue: model.NewStringValue("world"),
			}.run)
			t.Run("slice over map", setTestCase{
				valueFn: tc.mapValue,
				newValueFn: func() *model.Value {
					res := model.NewSliceValue()
					if err := res.Append(model.NewStringValue("world")); err != nil {
						t.Fatal(err)
					}
					return res
				},
			}.run)
			t.Run("string over null", setTestCase{
				valueFn:  tc.nullValue,
				newValue: model.NewStringValue("world"),
			}.run)
		})
	}
}
```

## File: `model/value_slice.go`
```go
package model

import (
	"fmt"
	"reflect"
)

// NewSliceValue returns a new slice value.
func NewSliceValue() *Value {
	res := newPtr()
	s := reflect.MakeSlice(reflect.SliceOf(reflect.TypeFor[any]()), 0, 0)
	ptr := reflect.New(reflect.SliceOf(reflect.TypeFor[any]()))
	ptr.Elem().Set(s)
	res.Elem().Set(ptr)
	return NewValue(res)
}

// IsSlice returns true if the value is a slice.
func (v *Value) IsSlice() bool {
	return v.UnpackKinds(reflect.Interface, reflect.Pointer).isSlice()
}

func (v *Value) isSlice() bool {
	return v.value.Kind() == reflect.Slice
}

// Append appends a value to the slice.
func (v *Value) Append(val *Value) error {
	// Branches behave differently when appending to a slice.
	// We expect each item in a branch to be its own value.
	if val.IsBranch() {
		return val.RangeSlice(func(_ int, item *Value) error {
			return v.Append(item)
		})
	}

	unpacked := v.UnpackKinds(reflect.Interface, reflect.Pointer)
	if !unpacked.isSlice() {
		return ErrUnexpectedType{
			Expected: TypeSlice,
			Actual:   v.Type(),
		}
	}

	// Wrap the value to preserve metadata and set functions.
	valToAppend := reflect.ValueOf(val)
	newVal := reflect.Append(unpacked.value, valToAppend)
	unpacked.value.Set(newVal)
	return nil
}

// SliceLen returns the length of the slice.
func (v *Value) SliceLen() (int, error) {
	unpacked := v.UnpackKinds(reflect.Interface, reflect.Pointer)
	if !unpacked.isSlice() {
		return 0, ErrUnexpectedType{
			Expected: TypeSlice,
			Actual:   v.Type(),
		}
	}
	return unpacked.value.Len(), nil
}

// GetSliceIndex returns the value at the specified index in the slice.
func (v *Value) GetSliceIndex(i int) (*Value, error) {
	unpacked := v.UnpackKinds(reflect.Interface, reflect.Pointer)
	if !unpacked.isSlice() {
		return nil, ErrUnexpectedType{
			Expected: TypeSlice,
			Actual:   v.Type(),
		}
	}
	if i < 0 || i >= unpacked.value.Len() {
		return nil, SliceIndexOutOfRange{Index: i}
	}

	item := unpacked.value.Index(i)
	if item.Kind() == reflect.Pointer && item.Type() == reflect.TypeFor[*Value]() {
		return item.Interface().(*Value), nil
	}
	if item.Kind() == reflect.Interface && !item.IsNil() {
		interfaceVal := item.Interface()
		if val, ok := interfaceVal.(*Value); ok {
			return val, nil
		}
	}

	res := NewValue(item)
	return res, nil
}

// SetSliceIndex sets the value at the specified index in the slice.
func (v *Value) SetSliceIndex(i int, val *Value) error {
	unpacked := v.UnpackKinds(reflect.Interface, reflect.Pointer)
	if !unpacked.isSlice() {
		return ErrUnexpectedType{
			Expected: TypeSlice,
			Actual:   v.Type(),
		}
	}
	if i < 0 || i >= unpacked.value.Len() {
		return SliceIndexOutOfRange{Index: i}
	}
	unpacked.value.Index(i).Set(reflect.ValueOf(val))
	return nil
}

// RangeSlice iterates over each item in the slice and calls the provided function.
func (v *Value) RangeSlice(f func(int, *Value) error) error {
	length, err := v.SliceLen()
	if err != nil {
		return fmt.Errorf("error getting slice length: %w", err)
	}

	for i := 0; i < length; i++ {
		va, err := v.GetSliceIndex(i)
		if err != nil {
			return fmt.Errorf("error getting slice index %d: %w", i, err)
		}
		if err := f(i, va); err != nil {
			return err
		}
	}

	return nil
}

// SliceIndexRange returns a new slice containing the values between the start and end indexes.
// Comparable to go's slice[start:end].
func (v *Value) SliceIndexRange(start, end int) (*Value, error) {
	l, err := v.SliceLen()
	if err != nil {
		return nil, fmt.Errorf("error getting slice length: %w", err)
	}

	if start < 0 {
		start = l + start
	}
	if end < 0 {
		end = l + end
	}

	res := NewSliceValue()

	if start > end {
		for i := start; i >= end; i-- {
			item, err := v.GetSliceIndex(i)
			if err != nil {
				return nil, fmt.Errorf("error getting slice index: %w", err)
			}
			if err := res.Append(item); err != nil {
				return nil, fmt.Errorf("error appending value to slice: %w", err)
			}
		}
	} else {
		for i := start; i <= end; i++ {
			item, err := v.GetSliceIndex(i)
			if err != nil {
				return nil, fmt.Errorf("error getting slice index: %w", err)
			}
			if err := res.Append(item); err != nil {
				return nil, fmt.Errorf("error appending value to slice: %w", err)
			}
		}
	}

	return res, nil
}
```

## File: `model/value_slice_test.go`
```go
package model_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestSlice(t *testing.T) {
	standardSlice := func() *model.Value {
		return model.NewValue([]any{"foo", "bar"})
	}

	modelSlice := func() *model.Value {
		res := model.NewSliceValue()
		if err := res.Append(model.NewValue("foo")); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		if err := res.Append(model.NewValue("bar")); err != nil {
			t.Fatalf("unexpected error: %s", err)
		}
		return res
	}

	runTests := func(v func() *model.Value) func(t *testing.T) {
		return func(t *testing.T) {
			t.Run("IsSlice", func(t *testing.T) {
				v := v()
				if !v.IsSlice() {
					t.Errorf("expected value to be a slice")
				}
			})
			t.Run("GetSliceIndex", func(t *testing.T) {
				v := v()
				foo, err := v.GetSliceIndex(0)
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				got, err := foo.StringValue()
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				if got != "foo" {
					t.Errorf("expected foo, got %s", got)
				}
			})
			t.Run("SetSliceIndex", func(t *testing.T) {
				v := v()
				if err := v.SetSliceIndex(0, model.NewValue("baz")); err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				baz, err := v.GetSliceIndex(0)
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				got, err := baz.StringValue()
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				if got != "baz" {
					t.Errorf("expected baz, got %s", got)
				}
			})
			t.Run("Len", func(t *testing.T) {
				v := v()
				got, err := v.SliceLen()
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				if got != 2 {
					t.Errorf("expected len of 2, got %d", got)
				}
			})
			t.Run("RangeSlice", func(t *testing.T) {
				v := v()
				var keys []int
				var vals []string
				err := v.RangeSlice(func(k int, v *model.Value) error {
					keys = append(keys, k)
					s, err := v.StringValue()
					if err != nil {
						return err
					}
					vals = append(vals, s)
					return nil
				})
				if err != nil {
					t.Errorf("unexpected error: %s", err)
					return
				}
				if len(keys) != 2 {
					t.Errorf("expected 2 keys, got %d", len(keys))
				}
				if len(vals) != 2 {
					t.Errorf("expected 2 vals, got %d", len(keys))
				}
				exp := []string{"foo", "bar"}

				for k, e := range exp {
					if keys[k] != k {
						t.Errorf("expected key %d, got %d", k, keys[k])
					}
					if vals[k] != e {
						t.Errorf("expected val %s, got %s", e, vals[k])
					}
				}
			})
			//t.Run("DeleteMapKey", func(t *testing.T) {
			//	v := v()
			//	if _, err := v.GetSliceIndex(1); err != nil {
			//		t.Errorf("unexpected error: %s", err)
			//		return
			//	}
			//	if err := v.DeleteSliceIndex(1); err != nil {
			//		t.Errorf("unexpected error: %s", err)
			//		return
			//	}
			//	_, err := v.GetSliceIndex(1)
			//	notFoundErr := &model.SliceIndexOutOfRange{}
			//	if !errors.As(err, &notFoundErr) {
			//		t.Errorf("expected index not found error, got %s", err)
			//	}
			//})
			t.Run("SliceIndexRange", func(t *testing.T) {
				t.Run("last element", func(t *testing.T) {
					v := v()
					s, err := v.SliceIndexRange(-1, -1)
					if err != nil {
						t.Errorf("unexpected error: %s", err)
						return
					}
					length, err := s.SliceLen()
					if err != nil {
						t.Errorf("unexpected error: %s", err)
						return
					}
					if length != 1 {
						t.Errorf("expected length of 1, got %d", length)
					}

					val, err := s.GetSliceIndex(0)
					if err != nil {
						t.Errorf("unexpected error: %s", err)
						return
					}
					got, err := val.StringValue()
					if err != nil {
						t.Errorf("unexpected error: %s", err)
						return
					}
					if got != "bar" {
						t.Errorf("expected bar, got %s", got)
					}
				})
				t.Run("first element", func(t *testing.T) {
					v := v()
					s, err := v.SliceIndexRange(0, 0)
					if err != nil {
						t.Errorf("unexpected error: %s", err)
						return
					}
					length, err := s.SliceLen()
					if err != nil {
						t.Errorf("unexpected error: %s", err)
						return
					}
					if length != 1 {
						t.Errorf("expected length of 1, got %d", length)
					}

					val, err := s.GetSliceIndex(0)
					if err != nil {
						t.Errorf("unexpected error: %s", err)
						return
					}
					got, err := val.StringValue()
					if err != nil {
						t.Errorf("unexpected error: %s", err)
						return
					}
					if got != "foo" {
						t.Errorf("expected foo, got %s", got)
					}
				})
			})
		}
	}

	t.Run("standard slice", runTests(standardSlice))
	t.Run("model slice", runTests(modelSlice))
}
```

## File: `model/value_test.go`
```go
package model_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/model"
)

func TestType_String(t *testing.T) {
	run := func(ty model.Type, exp string) func(*testing.T) {
		return func(t *testing.T) {
			got := ty.String()
			if got != exp {
				t.Errorf("expected %s, got %s", exp, got)
			}
		}
	}
	t.Run("string", run(model.TypeString, "string"))
	t.Run("int", run(model.TypeInt, "int"))
	t.Run("float", run(model.TypeFloat, "float"))
	t.Run("bool", run(model.TypeBool, "bool"))
	t.Run("map", run(model.TypeMap, "map"))
	t.Run("slice", run(model.TypeSlice, "array"))
	t.Run("unknown", run(model.TypeUnknown, "unknown"))
	t.Run("null", run(model.TypeNull, "null"))
}

func TestValue_Len(t *testing.T) {
	run := func(v *model.Value, exp int) func(*testing.T) {
		return func(t *testing.T) {
			got, err := v.Len()
			if err != nil {
				t.Errorf("unexpected error: %s", err)
				return
			}
			if got != exp {
				t.Errorf("expected %d, got %d", exp, got)
			}
		}
	}
	t.Run("string", func(t *testing.T) {
		t.Run("empty", run(model.NewStringValue(""), 0))
		t.Run("non-empty", run(model.NewStringValue("hello"), 5))
	})
	t.Run("slice", func(t *testing.T) {
		t.Run("empty", run(model.NewSliceValue(), 0))
		t.Run("non-empty", run(model.NewValue([]any{1, 2, 3}), 3))
	})
	t.Run("map", func(t *testing.T) {
		t.Run("empty", run(model.NewMapValue(), 0))
		t.Run("non-empty", run(model.NewValue(map[string]any{"one": 1, "two": 2, "three": 3}), 3))
	})
}

func TestValue_IsScalar(t *testing.T) {
	run := func(v *model.Value, exp bool) func(*testing.T) {
		return func(t *testing.T) {
			got := v.IsScalar()
			if got != exp {
				t.Errorf("expected %v, got %v", exp, got)
			}
		}
	}
	t.Run("string", run(model.NewStringValue("foo"), true))
	t.Run("bool", run(model.NewBoolValue(true), true))
	t.Run("int", run(model.NewIntValue(1), true))
	t.Run("float", run(model.NewFloatValue(1.0), true))
	t.Run("null", run(model.NewNullValue(), true))
	t.Run("map", run(model.NewMapValue(), false))
	t.Run("slice", run(model.NewSliceValue(), false))

	t.Run("nested", func(t *testing.T) {
		t.Run("nested string", run(model.NewNestedValue(model.NewStringValue("foo")), true))
		t.Run("nested bool", run(model.NewNestedValue(model.NewBoolValue(true)), true))
		t.Run("nested int", run(model.NewNestedValue(model.NewIntValue(1)), true))
		t.Run("nested float", run(model.NewNestedValue(model.NewFloatValue(1.0)), true))
		t.Run("nested null", run(model.NewNestedValue(model.NewNullValue()), true))
		t.Run("nested map", run(model.NewNestedValue(model.NewMapValue()), false))
		t.Run("nested slice", run(model.NewNestedValue(model.NewSliceValue()), false))

		t.Run("double nested string", run(model.NewNestedValue(model.NewNestedValue(model.NewStringValue("foo"))), true))
	})
}
```

## File: `model/orderedmap/map.go`
```go
package orderedmap

import (
	"reflect"
)

// KeyValue is a single key value pair from a *Map.
type KeyValue struct {
	Key   string
	Value any
}

// NewMap returns a new *Map that has its values initialised.
func NewMap() *Map {
	keys := make([]string, 0)
	data := make(map[string]any)
	return &Map{
		keys: keys,
		data: data,
	}
}

// FromMap creates a *Map from the input map.
// Note that while the contents will be ordered, the ordering is not
// guaranteed since the input map is unordered.
func FromMap(source map[string]any) *Map {
	m := NewMap()
	for k, v := range source {
		m.Set(k, v)
	}
	return m
}

// Map is a map implementation that maintains ordering of keys.
type Map struct {
	// keys contains the keys within the map in the order they were added.
	keys []string
	// data contains the actual map data.
	data map[string]any
}

func (m *Map) Len() int {
	return len(m.keys)
}

func (m *Map) Equal(other *Map) bool {
	if m.Len() != other.Len() {
		return false
	}

	for i, k := range m.keys {
		if k != other.keys[i] {
			return false
		}

		if !reflect.DeepEqual(m.data[k], other.data[k]) {
			return false
		}
	}

	return true
}

// Get returns the value found under the given key.
func (m *Map) Get(key string) (any, bool) {
	v, ok := m.data[key]
	return v, ok
}

// Set sets a value under the given key.
func (m *Map) Set(key string, value any) *Map {
	if _, ok := m.data[key]; ok {
		m.data[key] = value
	} else {
		m.keys = append(m.keys, key)
		m.data[key] = value
	}
	return m
}

// Delete deletes the value found under the given key.
func (m *Map) Delete(key string) *Map {
	// Delete the data entry.
	delete(m.data, key)

	// Remove the item from the keys.
	foundIndex := -1
	for i, k := range m.keys {
		if k == key {
			foundIndex = i
			break
		}
	}

	if foundIndex >= 0 {
		m.keys = append((m.keys)[:foundIndex], (m.keys)[foundIndex+1:]...)
	}

	return m
}

// KeyValues returns the KeyValue pairs within the map, in the order that they were added.
func (m *Map) KeyValues() []KeyValue {
	res := make([]KeyValue, 0)
	for _, key := range m.keys {
		res = append(res, KeyValue{
			Key:   key,
			Value: m.data[key],
		})
	}
	return res
}

// Keys returns all the keys from the map.
func (m *Map) Keys() []string {
	return m.keys
}

// UnorderedData returns all the data from the map.
func (m *Map) UnorderedData() map[string]any {
	return m.data
}
```

## File: `parsing/format.go`
```go
package parsing

import (
	"fmt"
)

// Format represents a file format.
type Format string

// NewReader creates a new reader for the format.
func (f Format) NewReader(options ReaderOptions) (Reader, error) {
	fn, ok := readers[f]
	if !ok {
		return nil, fmt.Errorf("unsupported reader file format: %s", f)
	}
	return fn(options)
}

// NewWriter creates a new writer for the format.
func (f Format) NewWriter(options WriterOptions) (Writer, error) {
	fn, ok := writers[f]
	if !ok {
		return nil, fmt.Errorf("unsupported writer file format: %s", f)
	}
	w, err := fn(options)
	if err != nil {
		return nil, err
	}
	return MultiDocumentWriter(w), nil
}

// String returns the string representation of the format.
func (f Format) String() string {
	return string(f)
}

// RegisteredReaders returns a list of registered readers.
func RegisteredReaders() []Format {
	var formats []Format
	for format := range readers {
		formats = append(formats, format)
	}
	return formats
}

// RegisteredWriters returns a list of registered writers.
func RegisteredWriters() []Format {
	var formats []Format
	for format := range writers {
		formats = append(formats, format)
	}
	return formats
}
```

## File: `parsing/reader.go`
```go
package parsing

import "github.com/tomwright/dasel/v3/model"

var readers = map[Format]NewReaderFn{}

type ReaderOptions struct {
	Ext map[string]string
}

// DefaultReaderOptions returns the default reader options.
func DefaultReaderOptions() ReaderOptions {
	return ReaderOptions{
		Ext: make(map[string]string),
	}
}

// Reader reads a value from a byte slice.
type Reader interface {
	// Read reads a value from a byte slice.
	Read([]byte) (*model.Value, error)
}

// NewReaderFn is a function that creates a new reader.
type NewReaderFn func(options ReaderOptions) (Reader, error)

// RegisterReader registers a new reader for the format.
func RegisterReader(format Format, fn NewReaderFn) {
	readers[format] = fn
}
```

## File: `parsing/writer.go`
```go
package parsing

import (
	"bytes"
	"fmt"

	"github.com/tomwright/dasel/v3/model"
)

var writers = map[Format]NewWriterFn{}

type WriterOptions struct {
	Compact bool
	Indent  string
	Ext     map[string]string
}

// DefaultWriterOptions returns the default writer options.
func DefaultWriterOptions() WriterOptions {
	return WriterOptions{
		Compact: false,
		Indent:  "  ",
		Ext:     make(map[string]string),
	}
}

// Writer writes a value to a byte slice.
type Writer interface {
	// Write writes a value to a byte slice.
	Write(*model.Value) ([]byte, error)
}

// NewWriterFn is a function that creates a new writer.
type NewWriterFn func(options WriterOptions) (Writer, error)

// RegisterWriter registers a new writer for the format.
func RegisterWriter(format Format, fn NewWriterFn) {
	writers[format] = fn
}

// DocumentSeparator is an interface that can be implemented by writers to allow for custom document separators.
type DocumentSeparator interface {
	// Separator returns the document separator.
	Separator() []byte
}

// MultiDocumentWriter is a writer that can write multiple documents.
func MultiDocumentWriter(w Writer) Writer {
	return &multiDocumentWriter{w: w}
}

type multiDocumentWriter struct {
	w Writer
}

// Write writes a value to a byte slice.
func (w *multiDocumentWriter) Write(value *model.Value) ([]byte, error) {
	if value.IsBranch() || value.IsSpread() {
		buf := new(bytes.Buffer)

		documentSeparator := []byte("\n")
		if ds, ok := w.w.(DocumentSeparator); ok {
			documentSeparator = ds.Separator()
		}

		totalDocuments, err := value.SliceLen()
		if err != nil {
			return nil, fmt.Errorf("failed to get document length: %w", err)
		}

		if err := value.RangeSlice(func(i int, v *model.Value) error {
			docBytes, err := w.w.Write(v)
			if err != nil {
				return fmt.Errorf("failed to write document %d: %w", i, err)
			}
			buf.Write(docBytes)

			if i < totalDocuments-1 {
				buf.Write(documentSeparator)
			}

			return nil
		}); err != nil {
			return nil, err
		}

		return buf.Bytes(), nil
	}
	return w.w.Write(value)
}
```

## File: `parsing/csv/csv.go`
```go
package csv

import (
	"fmt"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
)

// CSV represents the CSV file format.
const CSV parsing.Format = "csv"

var _ parsing.Reader = (*csvReader)(nil)
var _ parsing.Writer = (*csvWriter)(nil)

func init() {
	parsing.RegisterReader(CSV, newCSVReader)
	parsing.RegisterWriter(CSV, newCSVWriter)
}

func newCSVWriter(options parsing.WriterOptions) (parsing.Writer, error) {
	w := &csvWriter{
		separator: ',',
	}
	if v, ok := options.Ext["csv-delimiter"]; ok && v != "" {
		w.separator = rune(v[0])
	}
	return w, nil
}

func valueFromString(s string) (*model.Value, error) {
	return model.NewStringValue(s), nil
}

func valueToString(v *model.Value) (string, error) {
	if v.IsNull() {
		return "", nil
	}

	switch v.Type() {
	case model.TypeString:
		stringValue, err := v.StringValue()
		if err != nil {
			return "", err
		}
		return stringValue, nil
	case model.TypeInt:
		i, err := v.IntValue()
		if err != nil {
			return "", err
		}
		return fmt.Sprintf("%d", i), nil
	case model.TypeFloat:
		i, err := v.FloatValue()
		if err != nil {
			return "", err
		}
		return fmt.Sprintf("%g", i), nil
	case model.TypeBool:
		i, err := v.BoolValue()
		if err != nil {
			return "", err
		}
		return fmt.Sprintf("%t", i), nil
	default:
		return "", fmt.Errorf("csv writer cannot format type %s to string", v.Type())
	}
}
```

## File: `parsing/csv/csv_test.go`
```go
package csv

import (
	"github.com/tomwright/dasel/v3/model"
	"testing"
)

func TestValueToString(t *testing.T) {
	tests := []struct {
		desc string
		in   func() (*model.Value, error)
		exp  string
	}{
		{
			desc: "basic string",
			in: func() (*model.Value, error) {
				return model.NewStringValue("hello"), nil
			},
			exp: "hello",
		},
		{
			desc: "string",
			in: func() (*model.Value, error) {
				return model.NewStringValue("hello, there!!"), nil
			},
			exp: "hello, there!!",
		},
		{
			desc: "int",
			in: func() (*model.Value, error) {
				return model.NewIntValue(123), nil
			},
			exp: "123",
		},
		{
			desc: "float",
			in: func() (*model.Value, error) {
				return model.NewFloatValue(1.234), nil
			},
			exp: "1.234",
		},
		{
			desc: "null",
			in: func() (*model.Value, error) {
				return model.NewNullValue(), nil
			},
			exp: "",
		},
		{
			desc: "bool true",
			in: func() (*model.Value, error) {
				return model.NewBoolValue(true), nil
			},
			exp: "true",
		},
		{
			desc: "bool false",
			in: func() (*model.Value, error) {
				return model.NewBoolValue(false), nil
			},
			exp: "false",
		},
	}

	for _, testCase := range tests {
		tc := testCase
		t.Run(tc.desc, func(t *testing.T) {
			in, err := tc.in()
			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			got, err := valueToString(in)
			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if got != tc.exp {
				t.Errorf("expected '%s' but got '%s'", tc.exp, got)
			}
		})
	}
}
```

## File: `parsing/csv/reader.go`
```go
package csv

import (
	"bytes"
	"encoding/csv"
	"errors"
	"fmt"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"io"
)

func newCSVReader(options parsing.ReaderOptions) (parsing.Reader, error) {
	r := &csvReader{
		separator: ',',
	}
	if v, ok := options.Ext["csv-delimiter"]; ok && v != "" {
		r.separator = rune(v[0])
	}
	return r, nil
}

type csvReader struct {
	separator rune
}

// Read reads a value from a byte slice.
func (j *csvReader) Read(data []byte) (*model.Value, error) {
	r := csv.NewReader(bytes.NewReader(data))
	r.Comma = j.separator

	res := model.NewSliceValue()

	var headers []string

	for rowI := 0; ; rowI++ {
		record, err := r.Read()
		if err != nil {
			if errors.Is(err, io.EOF) {
				break
			}
			return nil, err
		}

		if headers == nil {
			headers = append(headers, record...)
			continue
		}

		row := model.NewMapValue()
		for colI, field := range record {
			if colI >= len(headers) {
				return nil, fmt.Errorf("row %d has more columns than headers", rowI)
			}
			headerKey := headers[colI]

			colV, err := valueFromString(field)
			if err != nil {
				return nil, fmt.Errorf("failed reading column %q for row %d: %w", field, colI, err)
			}

			if err := row.SetMapKey(headerKey, colV); err != nil {
				return nil, fmt.Errorf("failed to set map key %q: %w", headerKey, err)
			}
		}

		if err := res.Append(row); err != nil {
			return nil, fmt.Errorf("failed to append row %d: %w", rowI, err)
		}
	}

	return res, nil
}
```

## File: `parsing/csv/reader_test.go`
```go
package csv_test

import (
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/csv"
	"testing"
)

func TestCsvReader_Read(t *testing.T) {
	inputBytes := []byte(`name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago`)

	r, err := csv.CSV.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	got, err := r.Read(inputBytes)
	if err != nil {
		t.Errorf("unexpected error: %v", err)
		return
	}

	exp := model.NewSliceValue()
	row1 := model.NewMapValue()
	if err := row1.SetMapKey("name", model.NewStringValue("Alice")); err != nil {
		t.Fatal(err)
	}
	if err := row1.SetMapKey("age", model.NewStringValue("30")); err != nil {
		t.Fatal(err)
	}
	if err := row1.SetMapKey("city", model.NewStringValue("New York")); err != nil {
		t.Fatal(err)
	}
	if err := exp.Append(row1); err != nil {
		t.Fatal(err)
	}
	row2 := model.NewMapValue()
	if err := row2.SetMapKey("name", model.NewStringValue("Bob")); err != nil {
		t.Fatal(err)
	}
	if err := row2.SetMapKey("age", model.NewStringValue("25")); err != nil {
		t.Fatal(err)
	}
	if err := row2.SetMapKey("city", model.NewStringValue("Los Angeles")); err != nil {
		t.Fatal(err)
	}
	if err := exp.Append(row2); err != nil {
		t.Fatal(err)
	}
	row3 := model.NewMapValue()
	if err := row3.SetMapKey("name", model.NewStringValue("Charlie")); err != nil {
		t.Fatal(err)
	}
	if err := row3.SetMapKey("age", model.NewStringValue("35")); err != nil {
		t.Fatal(err)
	}
	if err := row3.SetMapKey("city", model.NewStringValue("Chicago")); err != nil {
		t.Fatal(err)
	}
	if err := exp.Append(row3); err != nil {
		t.Fatal(err)
	}
	matchRes, err := got.Equal(exp)
	if err != nil {
		t.Fatalf("error comparing values: %v", err)
	}
	match, err := matchRes.BoolValue()
	if err != nil {
		t.Fatalf("error getting bool value: %v", err)
	}
	if !match {
		t.Errorf("expected %v, got %v", exp, got)
	}
}
```

## File: `parsing/csv/writer.go`
```go
package csv

import (
	"bytes"
	"encoding/csv"
	"fmt"
	"github.com/tomwright/dasel/v3/model"
)

type csvWriter struct {
	separator rune
}

// Write writes a value to a byte slice.
func (j *csvWriter) Write(value *model.Value) ([]byte, error) {
	if !value.IsSlice() {
		return nil, fmt.Errorf("csv writer expects root output to be a slice/array, got %s", value.Type())
	}

	buf := new(bytes.Buffer)
	w := csv.NewWriter(buf)
	w.Comma = j.separator

	var headers []string

	if err := value.RangeSlice(func(i int, row *model.Value) error {
		if i == 0 {
			var err error
			headers, err = row.MapKeys()
			if err != nil {
				return fmt.Errorf("error getting map keys: %w", err)
			}
			if err := w.Write(headers); err != nil {
				return fmt.Errorf("error writing headers: %w", err)
			}
		}

		var values []string

		for _, headerKey := range headers {
			colV, err := row.GetMapKey(headerKey)
			if err != nil {
				return fmt.Errorf("error getting map key %q: %w", headerKey, err)
			}

			csvVal, err := valueToString(colV)
			if err != nil {
				return fmt.Errorf("error converting value to string: %w", err)
			}

			values = append(values, csvVal)
		}

		if err := w.Write(values); err != nil {
			return fmt.Errorf("error writing row: %w", err)
		}

		return nil
	}); err != nil {
		return nil, fmt.Errorf("error ranging slice: %w", err)
	}

	w.Flush()

	return buf.Bytes(), nil
}
```

## File: `parsing/csv/writer_test.go`
```go
package csv_test

import (
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/csv"
	"testing"
)

func TestCsvWriter_Write(t *testing.T) {
	expBytes := []byte(`name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
`)

	r, err := csv.CSV.NewWriter(parsing.DefaultWriterOptions())
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	rows := model.NewSliceValue()
	row1 := model.NewMapValue()
	if err := row1.SetMapKey("name", model.NewStringValue("Alice")); err != nil {
		t.Fatal(err)
	}
	if err := row1.SetMapKey("age", model.NewStringValue("30")); err != nil {
		t.Fatal(err)
	}
	if err := row1.SetMapKey("city", model.NewStringValue("New York")); err != nil {
		t.Fatal(err)
	}
	if err := rows.Append(row1); err != nil {
		t.Fatal(err)
	}
	row2 := model.NewMapValue()
	if err := row2.SetMapKey("name", model.NewStringValue("Bob")); err != nil {
		t.Fatal(err)
	}
	if err := row2.SetMapKey("age", model.NewStringValue("25")); err != nil {
		t.Fatal(err)
	}
	if err := row2.SetMapKey("city", model.NewStringValue("Los Angeles")); err != nil {
		t.Fatal(err)
	}
	if err := rows.Append(row2); err != nil {
		t.Fatal(err)
	}
	row3 := model.NewMapValue()
	if err := row3.SetMapKey("name", model.NewStringValue("Charlie")); err != nil {
		t.Fatal(err)
	}
	if err := row3.SetMapKey("age", model.NewStringValue("35")); err != nil {
		t.Fatal(err)
	}
	if err := row3.SetMapKey("city", model.NewStringValue("Chicago")); err != nil {
		t.Fatal(err)
	}
	if err := rows.Append(row3); err != nil {
		t.Fatal(err)
	}

	got, err := r.Write(rows)
	if err != nil {
		t.Errorf("unexpected error: %v", err)
		return
	}

	if string(expBytes) != string(got) {
		t.Errorf("expected:\n%s\ngot:\n%s", string(expBytes), string(got))
	}
}
```

## File: `parsing/d/reader.go`
```go
package json

import (
	"context"
	"fmt"

	"github.com/tomwright/dasel/v3/execution"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
)

const (
	// Dasel represents the dasel format.
	Dasel parsing.Format = "dasel"
)

var _ parsing.Reader = (*daselReader)(nil)

func init() {
	parsing.RegisterReader(Dasel, newDaselReader)
}

func newDaselReader(options parsing.ReaderOptions) (parsing.Reader, error) {
	return &daselReader{}, nil
}

type daselReader struct {
}

func (dr *daselReader) Read(in []byte) (*model.Value, error) {
	if len(in) == 0 {
		return model.NewNullValue(), nil
	}
	out, err := execution.ExecuteSelector(context.Background(), string(in), model.NewNullValue(), execution.NewOptions())
	if err != nil {
		return nil, fmt.Errorf("failed to read value: %w", err)
	}
	return out, nil
}
```

## File: `parsing/hcl/hcl.go`
```go
package hcl

import (
	"github.com/tomwright/dasel/v3/parsing"
)

const (
	// HCL represents the hcl2 file format.
	HCL parsing.Format = "hcl"
)

var _ parsing.Reader = (*hclReader)(nil)
var _ parsing.Writer = (*hclWriter)(nil)

func init() {
	parsing.RegisterReader(HCL, newHCLReader)
	parsing.RegisterWriter(HCL, newHCLWriter)
}
```

## File: `parsing/hcl/reader.go`
```go
package hcl

import (
	"fmt"

	"github.com/hashicorp/hcl/v2"
	"github.com/hashicorp/hcl/v2/gohcl"
	"github.com/hashicorp/hcl/v2/hclsyntax"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"github.com/zclconf/go-cty/cty"
)

func newHCLReader(options parsing.ReaderOptions) (parsing.Reader, error) {
	return &hclReader{
		alwaysReadLabelsToSlice: options.Ext["hcl-block-format"] == "array",
	}, nil
}

type hclReader struct {
	alwaysReadLabelsToSlice bool
}

// Read reads a value from a byte slice.
// Reads the HCL data into a model that follows the HCL JSON spec.
// See https://github.com/hashicorp/hcl/blob/main/json%2Fspec.md
func (r *hclReader) Read(data []byte) (*model.Value, error) {
	f, _ := hclsyntax.ParseConfig(data, "input", hcl.InitialPos)

	body, ok := f.Body.(*hclsyntax.Body)
	if !ok {
		return nil, fmt.Errorf("failed to assert file body type")
	}

	return r.decodeHCLBody(body)
}

func (r *hclReader) decodeHCLBody(body *hclsyntax.Body) (*model.Value, error) {
	res := model.NewMapValue()
	var err error

	for _, attr := range body.Attributes {
		val, err := r.decodeHCLExpr(attr.Expr)
		if err != nil {
			return nil, fmt.Errorf("failed to decode attr %q: %w", attr.Name, err)
		}

		if err := res.SetMapKey(attr.Name, val); err != nil {
			return nil, err
		}
	}

	res, err = r.decodeHCLBodyBlocks(body, res)
	if err != nil {
		return nil, err
	}

	return res, nil
}

func (r *hclReader) decodeHCLBodyBlocks(body *hclsyntax.Body, res *model.Value) (*model.Value, error) {
	for _, block := range body.Blocks {
		if err := r.decodeHCLBlock(block, res); err != nil {
			return nil, err
		}
	}
	return res, nil
}

func (r *hclReader) decodeHCLBlock(block *hclsyntax.Block, res *model.Value) error {
	key := block.Type
	v := res
	for _, label := range block.Labels {
		exists, err := v.MapKeyExists(key)
		if err != nil {
			return err
		}

		if exists {
			keyV, err := v.GetMapKey(key)
			if err != nil {
				return err
			}
			v = keyV
		} else {
			keyV := model.NewMapValue()
			if err := v.SetMapKey(key, keyV); err != nil {
				return err
			}
			v = keyV
		}

		key = label
	}

	body, err := r.decodeHCLBody(block.Body)
	if err != nil {
		return err
	}

	exists, err := v.MapKeyExists(key)
	if err != nil {
		return err
	}
	if exists {
		keyV, err := v.GetMapKey(key)
		if err != nil {
			return err
		}

		switch keyV.Type() {
		case model.TypeSlice:
			if err := keyV.Append(body); err != nil {
				return err
			}
		case model.TypeMap:
			// Previous value was a map.
			// Create a new slice containing the previous map and the new map.
			newKeyV := model.NewSliceValue()
			previousKeyV, err := keyV.Copy()
			if err != nil {
				return err
			}
			if err := newKeyV.Append(previousKeyV); err != nil {
				return err
			}
			if err := newKeyV.Append(body); err != nil {
				return err
			}
			if err := keyV.Set(newKeyV); err != nil {
				return err
			}
		default:
			return fmt.Errorf("unexpected type: %s", keyV.Type())
		}
	} else {
		if r.alwaysReadLabelsToSlice {
			slice := model.NewSliceValue()
			if err := slice.Append(body); err != nil {
				return err
			}
			if err := v.SetMapKey(key, slice); err != nil {
				return err
			}
		} else {
			if err := v.SetMapKey(key, body); err != nil {
				return err
			}
		}
	}

	return nil
}

func (r *hclReader) decodeHCLExpr(expr hcl.Expression) (*model.Value, error) {
	source := cty.Value{}
	_ = gohcl.DecodeExpression(expr, nil, &source)

	return r.decodeCtyValue(source)
}

func (r *hclReader) decodeCtyValue(source cty.Value) (res *model.Value, err error) {
	defer func() {
		r := recover()
		if r != nil {
			err = fmt.Errorf("failed to decode: %v", r)
			return
		}
	}()
	if source.IsNull() {
		return model.NewNullValue(), nil
	}

	sourceT := source.Type()
	if sourceT.HasDynamicTypes() {
		// TODO : Handle DynamicPseudoType.
		// I haben't found a clear way to do this.
		return model.NewNullValue(), nil
	}
	switch {
	case sourceT.IsListType(), sourceT.IsTupleType():
		res = model.NewSliceValue()
		it := source.ElementIterator()
		for it.Next() {
			k, v := it.Element()
			// We don't need the index as they should be in order.
			// Just validates the key is correct.
			_, _ = k.AsBigFloat().Float64()

			val, err := r.decodeCtyValue(v)
			if err != nil {
				return nil, fmt.Errorf("failed to decode tuple value: %w", err)
			}

			if err := res.Append(val); err != nil {
				return nil, err
			}
		}
		return res, nil
	case sourceT.IsMapType(), sourceT.IsObjectType(), sourceT.IsSetType():
		v := model.NewMapValue()
		it := source.ElementIterator()
		for it.Next() {
			k, el := it.Element()
			if k.Type() != cty.String {
				return nil, fmt.Errorf("object key must be a string")
			}
			kStr := k.AsString()

			elVal, err := r.decodeCtyValue(el)
			if err != nil {
				return nil, fmt.Errorf("failed to decode object value: %w", err)
			}

			if err := v.SetMapKey(kStr, elVal); err != nil {
				return nil, err
			}
		}
		return v, nil
	case sourceT.IsPrimitiveType():
		switch sourceT {
		case cty.String:
			v := source.AsString()
			return model.NewStringValue(v), nil
		case cty.Bool:
			v := source.True()
			return model.NewBoolValue(v), nil
		case cty.Number:
			v := source.AsBigFloat()
			f64, _ := v.Float64()
			if v.IsInt() {
				return model.NewIntValue(int64(f64)), nil
			}
			return model.NewFloatValue(f64), nil
		default:
			return nil, fmt.Errorf("unhandled primitive type %q", source.Type())
		}
	default:
		return nil, fmt.Errorf("unsupported type: %s", sourceT.FriendlyName())
	}
}
```

## File: `parsing/hcl/reader_test.go`
```go
package hcl_test

import (
	"fmt"
	"testing"

	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/hcl"
)

type readTestCase struct {
	in string
}

func (tc readTestCase) run(t *testing.T) {
	r, err := hcl.HCL.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	in := []byte(tc.in)

	got, err := r.Read(in)
	if err != nil {
		t.Errorf("unexpected error: %v", err)
		return
	}

	fmt.Println(got)
}

func TestHclReader_Read(t *testing.T) {
	t.Run("document a", readTestCase{
		in: `io_mode = "async"

service "http" "web_proxy" {
  listen_addr = "127.0.0.1:8080"

  process "main" {
    command = ["/usr/local/bin/awesome-app", "server"]
  }

  process "mgmt" {
    command = ["/usr/local/bin/awesome-app", "mgmt"]
  }
}`,
	}.run)
	t.Run("document b", readTestCase{
		in: `resource "aws_instance" "example" {
  # (resource configuration omitted for brevity)

  provisioner "local-exec" {
    command = "echo 'Hello World' >example.txt"
  }
  provisioner "file" {
    source      = "example.txt"
    destination = "/tmp/example.txt"
  }
  provisioner "remote-exec" {
    inline = [
      "sudo install-something -f /tmp/example.txt",
    ]
  }
}`,
	}.run)
	t.Run("document c", readTestCase{
		in: `image_id = "ami-123"
cluster_min_nodes = 2
cluster_decimal_nodes = 2.2
cluster_max_nodes = true
availability_zone_names = [
"us-east-1a",
"us-west-1c",
]
docker_ports = [{
internal = 8300
external = 8300
protocol = "tcp"
},
{
internal = 8301
external = 8301
protocol = "tcp"
}
]`,
	}.run)
}
```

## File: `parsing/hcl/writer.go`
```go
package hcl

import (
	"bytes"
	"fmt"
	"github.com/hashicorp/hcl/v2/hclwrite"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"github.com/zclconf/go-cty/cty"
)

func newHCLWriter(options parsing.WriterOptions) (parsing.Writer, error) {
	return &hclWriter{
		options: options,
	}, nil
}

type hclWriter struct {
	options parsing.WriterOptions
}

// Write writes a value to a byte slice.
func (j *hclWriter) Write(value *model.Value) ([]byte, error) {
	f, err := j.valueToFile(value)
	if err != nil {
		return nil, err
	}

	buf := new(bytes.Buffer)
	if _, err := f.WriteTo(buf); err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

func (j *hclWriter) valueToFile(v *model.Value) (*hclwrite.File, error) {
	f := hclwrite.NewEmptyFile()

	body := f.Body()

	if err := j.addValueToBody(nil, v, body); err != nil {
		return nil, err
	}

	return f, nil
}

func (j *hclWriter) addValueToBody(previousLabels []string, v *model.Value, body *hclwrite.Body) error {
	if !v.IsMap() {
		return fmt.Errorf("hcl body is expected to be a map, got %s", v.Type())
	}

	kvs, err := v.MapKeyValues()
	if err != nil {
		return err
	}

	blocks := make([]*hclwrite.Block, 0)
	for _, kv := range kvs {
		switch kv.Value.Type() {
		case model.TypeMap:
			block, err := j.valueToBlock(kv.Key, previousLabels, kv.Value)
			if err != nil {
				return fmt.Errorf("failed to encode %q to hcl block: %w", kv.Key, err)
			}
			blocks = append(blocks, block)
		case model.TypeSlice:
			vals := make([]cty.Value, 0)

			allMaps := true

			if err := kv.Value.RangeSlice(func(_ int, value *model.Value) error {
				ctyVal, err := j.valueToCty(value)
				if err != nil {
					return err
				}
				vals = append(vals, ctyVal)

				if !value.IsMap() {
					allMaps = false
				}
				return nil
			}); err != nil {
				return err
			}

			if allMaps {
				if err := kv.Value.RangeSlice(func(_ int, value *model.Value) error {
					block, err := j.valueToBlock(kv.Key, previousLabels, value)
					if err != nil {
						return fmt.Errorf("failed to encode %q to hcl block: %w", kv.Key, err)
					}
					blocks = append(blocks, block)
					return nil
				}); err != nil {
					return err
				}
			} else {
				body.SetAttributeValue(kv.Key, cty.TupleVal(vals))
			}

		default:
			ctyVal, err := j.valueToCty(kv.Value)
			if err != nil {
				return fmt.Errorf("failed to encode attribute %q: %w", kv.Key, err)
			}
			body.SetAttributeValue(kv.Key, ctyVal)
		}
	}

	for _, block := range blocks {
		body.AppendBlock(block)
	}

	return nil
}

func (j *hclWriter) valueToCty(v *model.Value) (cty.Value, error) {
	switch v.Type() {
	case model.TypeString:
		val, err := v.StringValue()
		if err != nil {
			return cty.Value{}, err
		}
		return cty.StringVal(val), nil
	case model.TypeBool:
		val, err := v.BoolValue()
		if err != nil {
			return cty.Value{}, err
		}
		return cty.BoolVal(val), nil
	case model.TypeInt:
		val, err := v.IntValue()
		if err != nil {
			return cty.Value{}, err
		}
		return cty.NumberIntVal(val), nil
	case model.TypeFloat:
		val, err := v.FloatValue()
		if err != nil {
			return cty.Value{}, err
		}
		return cty.NumberFloatVal(val), nil
	case model.TypeNull:
		return cty.NullVal(cty.NilType), nil
	case model.TypeSlice:
		var vals []cty.Value
		if err := v.RangeSlice(func(_ int, value *model.Value) error {
			ctyVal, err := j.valueToCty(value)
			if err != nil {
				return err
			}
			vals = append(vals, ctyVal)
			return nil
		}); err != nil {
			return cty.Value{}, err
		}
		return cty.TupleVal(vals), nil
	case model.TypeMap:
		mapV := map[string]cty.Value{}
		if err := v.RangeMap(func(s string, value *model.Value) error {
			ctyVal, err := j.valueToCty(value)
			if err != nil {
				return err
			}
			mapV[s] = ctyVal
			return nil
		}); err != nil {
			return cty.Value{}, err
		}
		return cty.ObjectVal(mapV), nil
	default:
		return cty.Value{}, fmt.Errorf("unhandled type when converting to cty value %q", v.Type())
	}
}

func (j *hclWriter) valueToBlock(key string, labels []string, v *model.Value) (*hclwrite.Block, error) {
	if !v.IsMap() {
		return nil, fmt.Errorf("must be map")
	}

	b := hclwrite.NewBlock(key, labels)

	if err := j.addValueToBody(labels, v, b.Body()); err != nil {
		return nil, err
	}

	return b, nil
}
```

## File: `parsing/hcl/writer_test.go`
```go
package hcl_test

import (
	"testing"

	"github.com/google/go-cmp/cmp"

	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/hcl"
)

type readWriteTestCase struct {
	in string
}

func (tc readWriteTestCase) run(t *testing.T) {
	r, err := hcl.HCL.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	w, err := hcl.HCL.NewWriter(parsing.DefaultWriterOptions())
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	in := []byte(tc.in)

	data, err := r.Read(in)
	if err != nil {
		t.Errorf("unexpected error: %v", err)
		return
	}

	got, err := w.Write(data)
	if err != nil {
		t.Errorf("unexpected error: %v", err)
		return
	}
	gotStr := string(got)

	if !cmp.Equal(tc.in, gotStr) {
		t.Errorf("unexpected output: %s", cmp.Diff(tc.in, gotStr))
	}
}

func TestHclReader_ReadWrite(t *testing.T) {
	t.Run("document a", readWriteTestCase{
		in: `io_mode = "async"
service {
  http {
    listen_addr = "127.0.0.1:8080"
    process {
      main {
        command = ["/usr/local/bin/awesome-app", "server"]
      }
      mgmt {
        command = ["/usr/local/bin/awesome-app", "mgmt"]
      }
      mgmt {
        command = ["/usr/local/bin/awesome-app", "mgmt2"]
      }
    }
  }
}
`,
	}.run)
}
```

## File: `parsing/ini/ini.go`
```go
package ini

import (
	"github.com/tomwright/dasel/v3/parsing"
)

const (
	// INI represents the ini file format.
	INI parsing.Format = "ini"
)

func init() {
	parsing.RegisterReader(INI, newINIReader)
	parsing.RegisterWriter(INI, newINIWriter)
}
```

## File: `parsing/ini/ini_reader.go`
```go
package ini

import (
	"fmt"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"gopkg.in/ini.v1"
)

var _ parsing.Reader = (*iniReader)(nil)

func init() {
	parsing.RegisterReader(INI, newINIReader)
	parsing.RegisterWriter(INI, newINIWriter)
}

func newINIReader(options parsing.ReaderOptions) (parsing.Reader, error) {
	return &iniReader{}, nil
}

type iniReader struct{}

// Read reads a value from a byte slice.
func (j *iniReader) Read(data []byte) (*model.Value, error) {
	f, err := ini.LoadSources(ini.LoadOptions{}, data)
	if err != nil {
		return nil, fmt.Errorf("failed to parse ini: %w", err)
	}

	res, err := j.readSection(f.Section(ini.DefaultSection))
	if err != nil {
		return nil, err
	}

	for _, s := range f.Sections() {
		if s.Name() == ini.DefaultSection {
			continue
		}
		sectionValue, err := j.readSection(s)
		if err != nil {
			return nil, err
		}
		if err := res.SetMapKey(s.Name(), sectionValue); err != nil {
			return nil, err
		}
	}

	return res, nil
}

func (j *iniReader) readSection(s *ini.Section) (*model.Value, error) {
	res := model.NewMapValue()
	for _, k := range s.Keys() {
		keyName := k.Name()
		keyValue := k.Value()

		if err := res.SetMapKey(keyName, model.NewStringValue(keyValue)); err != nil {
			return nil, err
		}
	}
	for _, s := range s.ChildSections() {
		childSection, err := j.readSection(s)
		if err != nil {
			return nil, err
		}
		if err := res.SetMapKey(s.Name(), childSection); err != nil {
			return nil, err
		}
	}
	return res, nil
}
```

## File: `parsing/ini/ini_test.go`
```go
package ini_test

import (
	"github.com/google/go-cmp/cmp"
	"github.com/tomwright/dasel/v3/parsing/ini"
	"testing"

	"github.com/tomwright/dasel/v3/parsing"
)

func TestIni(t *testing.T) {
	doc := []byte(`app_mode = development

[paths]
data = /home/git/grafana

[server]
protocol       = http
http_port      = 9999
enforce_domain = true

[profile testing]
something = foo
`)
	reader, err := ini.INI.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatal(err)
	}
	writer, err := ini.INI.NewWriter(parsing.DefaultWriterOptions())
	if err != nil {
		t.Fatal(err)
	}

	value, err := reader.Read(doc)
	if err != nil {
		t.Fatal(err)
	}

	newDoc, err := writer.Write(value)
	if err != nil {
		t.Fatal(err)
	}

	if string(doc) != string(newDoc) {
		t.Fatalf("expected %s, got %s...\n%s", string(doc), string(newDoc), cmp.Diff(string(doc), string(newDoc)))
	}
}
```

## File: `parsing/ini/ini_writer.go`
```go
package ini

import (
	"bytes"
	"fmt"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"gopkg.in/ini.v1"
	"strings"
)

var _ parsing.Writer = (*iniWriter)(nil)

func newINIWriter(options parsing.WriterOptions) (parsing.Writer, error) {
	return &iniWriter{
		options: options,
	}, nil
}

type iniWriter struct {
	options parsing.WriterOptions
}

// Write writes a value to a byte slice.
func (j *iniWriter) Write(value *model.Value) ([]byte, error) {
	if !value.IsMap() {
		return nil, fmt.Errorf("ini can only represent map values")
	}

	f := ini.Empty(ini.LoadOptions{
		AllowNestedValues: true,
	})

	if err := j.write(f, ini.DefaultSection, value); err != nil {
		return nil, err
	}

	buf := new(bytes.Buffer)

	if _, err := f.WriteTo(buf); err != nil {
		return nil, fmt.Errorf("failed to write ini: %w", err)
	}

	return buf.Bytes(), nil
}

func (j *iniWriter) write(f *ini.File, path string, value *model.Value) error {
	section, err := f.NewSection(path)
	if err != nil {
		return fmt.Errorf("failed to create section %s: %w", path, err)
	}

	nextSectionName := func(x string) string {
		path := strings.TrimSpace(strings.TrimPrefix(path, ini.DefaultSection))
		return strings.TrimSpace(path + " " + x)
	}

	switch value.Type() {
	case model.TypeMap:
		if err := value.RangeMap(func(s string, value *model.Value) error {
			switch {
			case value.IsScalar():
				strVal, err := valueToString(value)
				if err != nil {
					return fmt.Errorf("failed to convert value to string: %w", err)
				}
				_, err = section.NewKey(s, strVal)
				if err != nil {
					return fmt.Errorf("failed to create key %s: %w", s, err)
				}
				return nil

			case value.IsSlice():
				return fmt.Errorf("ini writer cannot represent slice values directly; consider using nested sections")

			case value.IsMap():
				if err := j.write(f, nextSectionName(s), value); err != nil {
					return err
				}
				return nil

			default:
				return fmt.Errorf("ini writer cannot represent value of type %s", value.Type())
			}
		}); err != nil {
			return err
		}
	default:
		return fmt.Errorf("ini sections can only represent map values")
	}
	return nil
}

func valueToString(v *model.Value) (string, error) {
	if v.IsNull() {
		return "", nil
	}

	switch v.Type() {
	case model.TypeString:
		stringValue, err := v.StringValue()
		if err != nil {
			return "", err
		}
		return stringValue, nil
	case model.TypeInt:
		i, err := v.IntValue()
		if err != nil {
			return "", err
		}
		return fmt.Sprintf("%d", i), nil
	case model.TypeFloat:
		i, err := v.FloatValue()
		if err != nil {
			return "", err
		}
		return fmt.Sprintf("%g", i), nil
	case model.TypeBool:
		i, err := v.BoolValue()
		if err != nil {
			return "", err
		}
		return fmt.Sprintf("%t", i), nil
	default:
		return "", fmt.Errorf("csv writer cannot format type %s to string", v.Type())
	}
}
```

## File: `parsing/json/json.go`
```go
package json

import (
	json "github.com/goccy/go-json"
	"github.com/tomwright/dasel/v3/parsing"
)

const (
	// JSON represents the JSON file format.
	JSON parsing.Format = "json"

	jsonOpenObject  = json.Delim('{')
	jsonCloseObject = json.Delim('}')
	jsonOpenArray   = json.Delim('[')
	jsonCloseArray  = json.Delim(']')
)

func init() {
	parsing.RegisterReader(JSON, newJSONReader)
	parsing.RegisterWriter(JSON, newJSONWriter)
}
```

## File: `parsing/json/json_reader.go`
```go
package json

import (
	"bytes"
	"fmt"
	json "github.com/goccy/go-json"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"strings"
)

var _ parsing.Reader = (*jsonReader)(nil)

func newJSONReader(options parsing.ReaderOptions) (parsing.Reader, error) {
	return &jsonReader{}, nil
}

type jsonReader struct{}

// Read reads a value from a byte slice.
func (j *jsonReader) Read(data []byte) (*model.Value, error) {
	decoder := json.NewDecoder(bytes.NewReader(data))
	decoder.UseNumber()

	t, err := decoder.Token()
	if err != nil {
		return nil, err
	}

	var res *model.Value

	switch t {
	case jsonOpenObject:
		res, err = j.decodeObject(decoder)
		if err != nil {
			return nil, fmt.Errorf("could not decode object: %w", err)
		}
	case jsonOpenArray:
		res, err = j.decodeArray(decoder)
		if err != nil {
			return nil, fmt.Errorf("could not decode array: %w", err)
		}
	default:
		res, err = j.decodeToken(decoder, t)
		if err != nil {
			return nil, err
		}
	}

	return res, nil
}

func (j *jsonReader) decodeObject(decoder *json.Decoder) (*model.Value, error) {
	res := model.NewMapValue()

	var key any = nil

	for {
		t, err := decoder.Token()
		if err != nil {
			// We don't expect an EOF here since we're in the middle of processing an object.
			return res, err
		}

		switch t {
		case jsonOpenArray:
			if key == nil {
				return res, fmt.Errorf("unexpected token: %v", t)
			}
			value, err := j.decodeArray(decoder)
			if err != nil {
				return res, err
			}
			if err := res.SetMapKey(key.(string), value); err != nil {
				return res, err
			}
			key = nil
		case jsonCloseArray:
			return res, fmt.Errorf("unexpected token: %v", t)
		case jsonCloseObject:
			return res, nil
		case jsonOpenObject:
			if key == nil {
				return res, fmt.Errorf("unexpected token: %v", t)
			}
			value, err := j.decodeObject(decoder)
			if err != nil {
				return res, err
			}
			if err := res.SetMapKey(key.(string), value); err != nil {
				return res, err
			}
			key = nil
		default:
			if key == nil {
				if tStr, ok := t.(string); ok {
					key = tStr
				} else {
					return nil, fmt.Errorf("unexpected token: %v", t)
				}
			} else {
				value, err := j.decodeToken(decoder, t)
				if err != nil {
					return nil, err
				}
				if err := res.SetMapKey(key.(string), value); err != nil {
					return res, err
				}
				key = nil
			}
		}
	}
}

func (j *jsonReader) decodeArray(decoder *json.Decoder) (*model.Value, error) {
	res := model.NewSliceValue()
	for {
		t, err := decoder.Token()
		if err != nil {
			// We don't expect an EOF here since we're in the middle of processing an object.
			return res, err
		}

		switch t {
		case jsonOpenArray:
			value, err := j.decodeArray(decoder)
			if err != nil {
				return res, err
			}
			if err := res.Append(value); err != nil {
				return res, err
			}
		case jsonCloseArray:
			return res, nil
		case jsonCloseObject:
			return res, fmt.Errorf("unexpected token: %t", t)
		case jsonOpenObject:
			value, err := j.decodeObject(decoder)
			if err != nil {
				return res, err
			}
			if err := res.Append(value); err != nil {
				return res, err
			}
		default:
			value, err := j.decodeToken(decoder, t)
			if err != nil {
				return nil, err
			}
			if err := res.Append(value); err != nil {
				return res, err
			}
		}
	}
}

func (j *jsonReader) decodeToken(decoder *json.Decoder, t json.Token) (*model.Value, error) {
	switch tv := t.(type) {
	case json.Number:
		strNum := tv.String()
		if strings.Contains(strNum, ".") {
			floatNum, err := tv.Float64()
			if err == nil {
				return model.NewFloatValue(floatNum), nil
			}
			return nil, err
		}
		intNum, err := tv.Int64()
		if err == nil {
			return model.NewIntValue(intNum), nil
		}

		return nil, err
	default:
		return model.NewValue(tv), nil
	}
}
```

## File: `parsing/json/json_test.go`
```go
package json_test

import (
	"testing"

	"github.com/google/go-cmp/cmp"
	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/json"
)

func TestJson(t *testing.T) {
	doc := []byte(`{
    "string": "foo",
    "int": 1,
    "float": 1.1,
    "bool": true,
    "null": null,
    "array": [
        1,
        2,
        3
    ],
    "object": {
        "key": "value"
    }
}
`)
	reader, err := json.JSON.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatal(err)
	}
	writer, err := json.JSON.NewWriter(parsing.DefaultWriterOptions())
	if err != nil {
		t.Fatal(err)
	}

	value, err := reader.Read(doc)
	if err != nil {
		t.Fatal(err)
	}

	newDoc, err := writer.Write(value)
	if err != nil {
		t.Fatal(err)
	}

	if string(doc) != string(newDoc) {
		t.Fatalf("expected %s, got %s...\n%s", string(doc), string(newDoc), cmp.Diff(string(doc), string(newDoc)))
	}
}
```

## File: `parsing/json/json_writer.go`
```go
package json

import (
	"bytes"
	"fmt"
	json "github.com/goccy/go-json"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"io"
	"strings"
)

var _ parsing.Writer = (*jsonWriter)(nil)

// NewJSONWriter creates a new JSON writer.
func newJSONWriter(options parsing.WriterOptions) (parsing.Writer, error) {
	return &jsonWriter{
		options: options,
	}, nil
}

type jsonWriter struct {
	options parsing.WriterOptions
}

// Write writes a value to a byte slice.
func (j *jsonWriter) Write(value *model.Value) ([]byte, error) {
	buf := new(bytes.Buffer)

	es := encoderState{indentStr: "    "}

	encoderFn := func(v any) error {
		res, err := json.Marshal(v)
		if err != nil {
			return err
		}
		_, err = buf.Write(res)
		return err
	}

	if err := j.write(buf, encoderFn, es, value); err != nil {
		return nil, err
	}

	if _, err := buf.Write([]byte("\n")); err != nil {
		return nil, err
	}

	return buf.Bytes(), nil
}

type encoderState struct {
	indent    int
	indentStr string
}

func (es encoderState) inc() encoderState {
	es.indent++
	return es
}

func (es encoderState) writeIndent(w io.Writer) error {
	if es.indent == 0 || es.indentStr == "" {
		return nil
	}
	i := strings.Repeat(es.indentStr, es.indent)
	if _, err := w.Write([]byte(i)); err != nil {
		return err
	}
	return nil
}

type encoderFn func(v any) error

func (j *jsonWriter) write(w io.Writer, encoder encoderFn, es encoderState, value *model.Value) error {
	switch value.Type() {
	case model.TypeMap:
		return j.writeMap(w, encoder, es, value)
	case model.TypeSlice:
		return j.writeSlice(w, encoder, es, value)
	case model.TypeString:
		val, err := value.StringValue()
		if err != nil {
			return err
		}
		return encoder(val)
	case model.TypeInt:
		val, err := value.IntValue()
		if err != nil {
			return err
		}
		return encoder(val)
	case model.TypeFloat:
		val, err := value.FloatValue()
		if err != nil {
			return err
		}
		return encoder(val)
	case model.TypeBool:
		val, err := value.BoolValue()
		if err != nil {
			return err
		}
		return encoder(val)
	case model.TypeNull:
		return encoder(nil)
	default:
		return fmt.Errorf("unsupported type: %s", value.Type())
	}
}

func (j *jsonWriter) writeMap(w io.Writer, encoder encoderFn, es encoderState, value *model.Value) error {
	kvs, err := value.MapKeyValues()
	if err != nil {
		return err
	}

	if _, err := w.Write([]byte(`{`)); err != nil {
		return err
	}

	if len(kvs) > 0 {
		if _, err := w.Write([]byte("\n")); err != nil {
			return err
		}

		incEs := es.inc()
		for i, kv := range kvs {
			if err := incEs.writeIndent(w); err != nil {
				return err
			}

			if _, err := fmt.Fprintf(w, `"%s": `, kv.Key); err != nil {
				return err
			}

			if err := j.write(w, encoder, incEs, kv.Value); err != nil {
				return err
			}

			if i < len(kvs)-1 {
				if _, err := w.Write([]byte(`,`)); err != nil {
					return err
				}
			}

			if _, err := w.Write([]byte("\n")); err != nil {
				return err
			}
		}
		if err := es.writeIndent(w); err != nil {
			return err
		}
	}

	if _, err := w.Write([]byte(`}`)); err != nil {
		return err
	}

	return nil
}

func (j *jsonWriter) writeSlice(w io.Writer, encoder encoderFn, es encoderState, value *model.Value) error {
	if _, err := w.Write([]byte(`[`)); err != nil {
		return err
	}

	length, err := value.SliceLen()
	if err != nil {
		return fmt.Errorf("error getting slice length: %w", err)
	}

	if length > 0 {
		if _, err := w.Write([]byte("\n")); err != nil {
			return err
		}
		incEs := es.inc()
		for i := 0; i < length; i++ {
			if err := incEs.writeIndent(w); err != nil {
				return err
			}
			va, err := value.GetSliceIndex(i)
			if err != nil {
				return fmt.Errorf("error getting slice index %d: %w", i, err)
			}
			if err := j.write(w, encoder, incEs, va); err != nil {
				return err
			}
			if i < length-1 {
				if _, err := w.Write([]byte(`,`)); err != nil {
					return err
				}
			}
			if _, err := w.Write([]byte("\n")); err != nil {
				return err
			}
		}
		if err := es.writeIndent(w); err != nil {
			return err
		}
	}

	if _, err := w.Write([]byte(`]`)); err != nil {
		return err
	}

	return nil
}
```

## File: `parsing/toml/toml.go`
```go
package toml

import (
	"github.com/tomwright/dasel/v3/parsing"
)

// TODO : Implement using https://github.com/pelletier/go-toml/blob/v2/unstable/ast.go

// TOML represents the TOML file format.
const TOML parsing.Format = "toml"

func init() {
	parsing.RegisterReader(TOML, newTOMLReader)
	parsing.RegisterWriter(TOML, newTOMLWriter)
}
```

## File: `parsing/toml/toml_reader.go`
```go
package toml

import (
	"bytes"
	"fmt"
	"strconv"

	"github.com/pelletier/go-toml/v2/unstable"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
)

var _ parsing.Reader = (*tomlReader)(nil)

func newTOMLReader(options parsing.ReaderOptions) (parsing.Reader, error) {
	return &tomlReader{}, nil
}

const (
	tomlStringStyleKey = "toml_string_style"

	tomlStringStyleMultilineLiteral = "multiline_literal"
	tomlStringStyleMultilineBasic   = "multiline_basic"
	tomlStringStyleLiteral          = "literal"
	tomlStringStyleBasic            = "basic"

	tomlTableStyleKey      = "toml_table_style"
	tomlTableStyleStandard = "standard"
	tomlTableStyleArray    = "array"
	tomlTableStyleInline   = "inline"
)

type tomlReader struct{}

// Read reads a value from a byte slice.
func (j *tomlReader) Read(data []byte) (*model.Value, error) {
	p := &unstable.Parser{}
	p.Reset(data)

	root := model.NewMapValue()

	var active *model.Value

	for p.NextExpression() {
		expr := p.Expression()
		switch expr.Kind {
		case unstable.Invalid, unstable.Comment:
			// ignore
			continue
		case unstable.KeyValue:
			keyParts, val, err := j.parseKeyValueNode(p, expr)
			if err != nil {
				return nil, err
			}
			if active != nil {
				if err := setDottedKey(root, active, keyParts, val); err != nil {
					return nil, err
				}
			} else {
				if err := setDottedKey(root, nil, keyParts, val); err != nil {
					return nil, err
				}
			}

		case unstable.Table:
			parts, quoted, err := extractKeyFromTableNode(p, expr)
			if err != nil {
				return nil, err
			}
			m, err := ensureMapAt(root, parts)
			if err != nil {
				return nil, err
			}
			// Record table header parts and quoting info on the map so the writer
			// can reproduce the header exactly if needed.
			m.SetMetadataValue(tomlTableStyleKey, tomlTableStyleStandard)
			m.SetMetadataValue("toml_table_header_parts", parts)
			m.SetMetadataValue("toml_table_header_quoted", quoted)
			active = m

		case unstable.ArrayTable:
			parts, quoted, err := extractKeyFromTableNode(p, expr)
			if err != nil {
				return nil, err
			}
			slice, err := ensureSliceAt(root, parts)
			if err != nil {
				return nil, err
			}
			obj := model.NewMapValue()
			// Mark this object as created via an array table so the writer can
			// emit [[...]] headers for it.
			obj.SetMetadataValue(tomlTableStyleKey, tomlTableStyleArray)
			obj.SetMetadataValue("toml_table_header_parts", parts)
			obj.SetMetadataValue("toml_table_header_quoted", quoted)
			if err := slice.Append(obj); err != nil {
				return nil, err
			}
			active = obj

		default:
			// top-level value nodes are unexpected; ignore
		}
	}

	return root, nil
}

// readNode parses a value node (not table/keyvalue headers).
func (j *tomlReader) readNode(p *unstable.Parser, n *unstable.Node) (string, *model.Value, error) {
	switch n.Kind {
	// Meta
	case unstable.Invalid:
		return "", nil, nil
	case unstable.Comment:
		return "", nil, nil
	case unstable.Key:
		return "", model.NewStringValue(string(n.Data)), nil

	// Container values
	case unstable.Array:
		v, err := j.readArrayValue(p, n)
		return "", v, err
	case unstable.InlineTable:
		return j.readInlineTable(p, n)

	// Values
	case unstable.String:
		v := model.NewStringValue(string(n.Data))

		raw := p.Raw(n.Raw)
		switch {
		case len(raw) >= 3 && bytes.HasPrefix(raw, []byte("''")) && bytes.HasPrefix(raw, []byte("'''")):
			v.SetMetadataValue(tomlStringStyleKey, tomlStringStyleMultilineLiteral)
		case len(raw) >= 3 && bytes.HasPrefix(raw, []byte("\"\"\"")):
			v.SetMetadataValue(tomlStringStyleKey, tomlStringStyleMultilineBasic)
		case len(raw) >= 1 && raw[0] == '\'':
			v.SetMetadataValue(tomlStringStyleKey, tomlStringStyleLiteral)
		default:
			v.SetMetadataValue(tomlStringStyleKey, tomlStringStyleBasic)
		}

		return "", v, nil
	case unstable.Bool:
		return "", model.NewBoolValue(string(n.Data) == "true"), nil
	case unstable.Float:
		f, err := strconv.ParseFloat(string(n.Data), 64)
		if err != nil {
			return "", nil, err
		}
		return "", model.NewFloatValue(f), nil
	case unstable.Integer:
		i64, err := strconv.ParseInt(string(n.Data), 10, 64)
		if err != nil {
			return "", nil, err
		}
		return "", model.NewIntValue(int64(i64)), nil
	case unstable.LocalDate:
		return "", model.NewStringValue(string(n.Data)), nil
	case unstable.LocalTime:
		return "", model.NewStringValue(string(n.Data)), nil
	case unstable.LocalDateTime:
		return "", model.NewStringValue(string(n.Data)), nil
	case unstable.DateTime:
		return "", model.NewStringValue(string(n.Data)), nil
	default:
		return "", nil, fmt.Errorf("unhandled node kind: %s", n.Kind.String())
	}
}

// parseKeyValueNode extracts the key segments and value from a KeyValue node without consuming parser expressions.
func (j *tomlReader) parseKeyValueNode(p *unstable.Parser, n *unstable.Node) ([]string, *model.Value, error) {
	i := n.Children()
	var keyParts []string
	var val *model.Value

	for i.Next() {
		child := i.Node()
		if child.Kind == unstable.Key {
			keyParts = append(keyParts, string(child.Data))
			continue
		}
		_, v, err := j.readNode(p, child)
		if err != nil {
			return nil, nil, err
		}
		val = v
	}

	if len(keyParts) == 0 {
		return nil, nil, fmt.Errorf("missing key in key/value node")
	}
	if val == nil {
		return nil, nil, fmt.Errorf("missing value in key/value node")
	}

	return keyParts, val, nil
}

// extractKeyFromTableNode returns the key segments from a Table/ArrayTable node.
func extractKeyFromTableNode(p *unstable.Parser, n *unstable.Node) ([]string, []bool, error) {
	i := n.Children()
	var parts []string
	var quoted []bool
	for i.Next() {
		child := i.Node()
		if child.Kind == unstable.Key {
			parts = append(parts, string(child.Data))
			raw := p.Raw(child.Raw)
			isQuoted := false
			if len(raw) > 0 && (raw[0] == '"' || raw[0] == '\'') {
				isQuoted = true
			}
			quoted = append(quoted, isQuoted)
			continue
		}
		return nil, nil, fmt.Errorf("expected table child node, got %s", child.Kind.String())
	}
	if len(parts) == 0 {
		return nil, nil, fmt.Errorf("missing table child key node")
	}
	return parts, quoted, nil
}

// ensureMapAt ensures a map exists at the dotted path under root and returns it.
func ensureMapAt(root *model.Value, path []string) (*model.Value, error) {
	if len(path) == 0 {
		return root, nil
	}
	cur := root
	for _, seg := range path {
		exists, err := cur.MapKeyExists(seg)
		if err != nil {
			return nil, err
		}
		if !exists {
			m := model.NewMapValue()
			if err := cur.SetMapKey(seg, m); err != nil {
				return nil, err
			}
			cur = m
			continue
		}
		next, err := cur.GetMapKey(seg)
		if err != nil {
			return nil, err
		}
		if next.IsSlice() {
			sliceLen, err := next.Len()
			if err != nil {
				return nil, err
			}
			next, err = next.GetSliceIndex(sliceLen - 1)
			if err != nil {
				return nil, err
			}
		}
		if !next.IsMap() {
			return nil, fmt.Errorf("conflicting types at path '%s': expected map", seg)
		}
		cur = next
	}
	return cur, nil
}

// ensureSliceAt ensures a slice exists at the dotted path under root and returns it.
func ensureSliceAt(root *model.Value, path []string) (*model.Value, error) {
	if len(path) == 0 {
		return nil, fmt.Errorf("empty path for array table")
	}
	parentPath := path[:len(path)-1]
	finalSeg := path[len(path)-1]
	parent, err := ensureMapAt(root, parentPath)
	if err != nil {
		return nil, err
	}
	exists, err := parent.MapKeyExists(finalSeg)
	if err != nil {
		return nil, err
	}
	if !exists {
		s := model.NewSliceValue()
		if err := parent.SetMapKey(finalSeg, s); err != nil {
			return nil, err
		}
		return s, nil
	}
	v, err := parent.GetMapKey(finalSeg)
	if err != nil {
		return nil, err
	}
	if !v.IsSlice() {
		return nil, fmt.Errorf("conflicting types at path '%s': expected slice", finalSeg)
	}
	return v, nil
}

// setDottedKey sets a value at a (possibly dotted) key within the given container (creating intermediate maps).
// If active is non-nil, it is the current table object to set keys relative to; root is only used when active is nil to
// create implicit parent maps on the root.
func setDottedKey(root, active *model.Value, parts []string, val *model.Value) error {
	if len(parts) == 0 {
		return fmt.Errorf("empty key")
	}
	// If active table provided, we should set relative to it. But parts may be dotted (i.e., multiple segments).
	if active != nil {
		if len(parts) == 1 {
			return active.SetMapKey(parts[0], val)
		}
		parent, err := ensureMapAt(active, parts[:len(parts)-1])
		if err != nil {
			return err
		}
		return parent.SetMapKey(parts[len(parts)-1], val)
	}
	// No active table: set on root
	if len(parts) == 1 {
		return root.SetMapKey(parts[0], val)
	}
	parent, err := ensureMapAt(root, parts[:len(parts)-1])
	if err != nil {
		return err
	}
	return parent.SetMapKey(parts[len(parts)-1], val)
}

func (j *tomlReader) readInlineTable(p *unstable.Parser, n *unstable.Node) (string, *model.Value, error) {
	res := model.NewMapValue()
	res.SetMetadataValue(tomlTableStyleKey, tomlTableStyleInline)

	i := n.Children()
	for i.Next() {
		childNode := i.Node()
		// Inline table children are key/value pairs. Handle KeyValue specially.
		switch childNode.Kind {
		case unstable.KeyValue:
			kparts, v, err := j.parseKeyValueNode(p, childNode)
			if err != nil {
				return "", nil, err
			}
			if err := setDottedKey(res, nil, kparts, v); err != nil {
				return "", nil, err
			}
		default:
			// fallback to readNode for other kinds (e.g., Key)
			key, val, err := j.readNode(p, childNode)
			if err != nil {
				return "", nil, err
			}
			if key == "" {
				return "", nil, fmt.Errorf("missing key in inline table child")
			}
			if err := res.SetMapKey(key, val); err != nil {
				return "", nil, err
			}
		}
	}

	return "", res, nil
}

func (j *tomlReader) readArrayValue(p *unstable.Parser, n *unstable.Node) (*model.Value, error) {
	res := model.NewSliceValue()

	i := n.Children()

	for i.Next() {
		childNode := i.Node()

		_, val, err := j.readNode(p, childNode)
		if err != nil {
			return nil, err
		}

		val.SetMetadataValue(tomlTableStyleKey, tomlTableStyleArray)

		if err := res.Append(val); err != nil {
			return nil, err
		}
	}

	return res, nil
}
```

## File: `parsing/toml/toml_reader_test.go`
```go
package toml_test

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/toml"
)

func tomlReaderTest(data []byte, exp func() *model.Value) func(*testing.T) {
	return func(t *testing.T) {
		exp := exp()
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error: %v", err)
		}

		got, err := r.Read(data)
		if err != nil {
			t.Errorf("unexpected error: %v", err)
			return
		}

		matchResult, err := got.Equal(exp)
		if err != nil {
			t.Fatalf("unexpected error: %v", err)
		}
		matchResultBool, err := matchResult.BoolValue()
		if err != nil {
			t.Fatalf("unexpected error: %v", err)
		}
		if !matchResultBool {
			t.Errorf("expected\n%s\ngot\n%s", exp.String(), got.String())
		}
	}
}

func TestTomlReader_Read(t *testing.T) {
	t.Run("key value", func(t *testing.T) {
		t.Run(
			"string",
			tomlReaderTest([]byte(`foo = "Bar"`), func() *model.Value {
				res := model.NewMapValue()
				_ = res.SetMapKey("foo", model.NewStringValue("Bar"))
				return res
			}),
		)

		t.Run(
			"int",
			tomlReaderTest([]byte(`foo = 123`), func() *model.Value {
				res := model.NewMapValue()
				_ = res.SetMapKey("foo", model.NewIntValue(123))
				return res
			}),
		)

		t.Run(
			"float",
			tomlReaderTest([]byte(`foo = 12.3`), func() *model.Value {
				res := model.NewMapValue()
				_ = res.SetMapKey("foo", model.NewFloatValue(12.3))
				return res
			}),
		)

		t.Run(
			"true",
			tomlReaderTest([]byte(`foo = true`), func() *model.Value {
				res := model.NewMapValue()
				_ = res.SetMapKey("foo", model.NewBoolValue(true))
				return res
			}),
		)

		t.Run(
			"false",
			tomlReaderTest([]byte(`foo = false`), func() *model.Value {
				res := model.NewMapValue()
				_ = res.SetMapKey("foo", model.NewBoolValue(false))
				return res
			}),
		)
	})

	t.Run("inline table", tomlReaderTest([]byte(`props = { key1 = "value1", key2 = "value2" }`), func() *model.Value {
		res := model.NewMapValue()
		inlineTable := model.NewMapValue()
		_ = inlineTable.SetMapKey("key1", model.NewStringValue("value1"))
		_ = inlineTable.SetMapKey("key2", model.NewStringValue("value2"))
		_ = res.SetMapKey("props", inlineTable)
		return res
	}))

	t.Run("table", tomlReaderTest([]byte(`[props]
key1 = "value1"
key2 = "value2"`), func() *model.Value {
		res := model.NewMapValue()
		inlineTable := model.NewMapValue()
		_ = inlineTable.SetMapKey("key1", model.NewStringValue("value1"))
		_ = inlineTable.SetMapKey("key2", model.NewStringValue("value2"))
		_ = res.SetMapKey("props", inlineTable)
		return res
	}))

	t.Run("array table", tomlReaderTest([]byte(`[[products]]
name = "foo"
id = 1

[[products]]
name = "bar"
id = 2`), func() *model.Value {
		productsArray := model.NewSliceValue()
		product1 := model.NewMapValue()
		_ = product1.SetMapKey("name", model.NewStringValue("foo"))
		_ = product1.SetMapKey("id", model.NewIntValue(1))
		_ = productsArray.Append(product1)

		product2 := model.NewMapValue()
		_ = product2.SetMapKey("name", model.NewStringValue("bar"))
		_ = product2.SetMapKey("id", model.NewIntValue(2))
		_ = productsArray.Append(product2)

		res := model.NewMapValue()
		_ = res.SetMapKey("products", productsArray)
		return res
	}))

	//	dataBytes := []byte(`title = "TOML Example"
	//[owner]
	//name = "Tom Preston-Werner"
	//props = { key1 = "value1", key2 = "value2" }
	//
	//[[products]]
	//name = "Hammer"
	//sku = 738594937
	//
	//[[products]]
	//name = "Screwdriver"
	//sku = 12341234
	//`)
	//	//dob = 1979-05-27T07:32:00-08:00
	//	dataModel := model.NewMapValue()
	//	//parsedTime, err := time.Parse(time.RFC3339, "1979-05-27T07:32:00-08:00")
	//	//if err != nil {
	//	//	t.Fatalf("unexpected error: %v", err)
	//	//}
	//	ownerMap := model.NewMapValue()
	//	_ = ownerMap.SetMapKey("name", model.NewStringValue("Tom Preston-Werner"))
	//	//_ = ownerMap.SetMapKey("dob", model.NewValue(parsedTime))
	//	_ = dataModel.SetMapKey("title", model.NewStringValue("TOML Example"))
	//	_ = dataModel.SetMapKey("owner", ownerMap)
}

func TestTomlReader_MoreCases(t *testing.T) {
	// simple array of ints
	t.Run("simple array", tomlReaderTest([]byte(`nums = [1, 2, 3]`), func() *model.Value {
		res := model.NewMapValue()
		s := model.NewSliceValue()
		_ = s.Append(model.NewIntValue(1))
		_ = s.Append(model.NewIntValue(2))
		_ = s.Append(model.NewIntValue(3))
		_ = res.SetMapKey("nums", s)
		return res
	}))

	// mixed type array
	t.Run("mixed array", tomlReaderTest([]byte(`mix = [1, "two", true]`), func() *model.Value {
		res := model.NewMapValue()
		s := model.NewSliceValue()
		_ = s.Append(model.NewIntValue(1))
		_ = s.Append(model.NewStringValue("two"))
		_ = s.Append(model.NewBoolValue(true))
		_ = res.SetMapKey("mix", s)
		return res
	}))

	// inline nested table and array
	t.Run("inline nested table", tomlReaderTest([]byte(`props = { sub = { a = 1 }, arr = [1,2] }`), func() *model.Value {
		res := model.NewMapValue()
		props := model.NewMapValue()
		sub := model.NewMapValue()
		_ = sub.SetMapKey("a", model.NewIntValue(1))
		_ = props.SetMapKey("sub", sub)
		arr := model.NewSliceValue()
		_ = arr.Append(model.NewIntValue(1))
		_ = arr.Append(model.NewIntValue(2))
		_ = props.SetMapKey("arr", arr)
		_ = res.SetMapKey("props", props)
		return res
	}))

	// quoted key with space
	t.Run("quoted key with space", tomlReaderTest([]byte(`"a b" = "val"`), func() *model.Value {
		res := model.NewMapValue()
		_ = res.SetMapKey("a b", model.NewStringValue("val"))
		return res
	}))

	// dotted+quoted mixture
	t.Run("dotted and quoted mixture", tomlReaderTest([]byte(`a."b.c".d = "x"`), func() *model.Value {
		res := model.NewMapValue()
		a := model.NewMapValue()
		b := model.NewMapValue()
		_ = b.SetMapKey("d", model.NewStringValue("x"))
		_ = a.SetMapKey("b.c", b)
		_ = res.SetMapKey("a", a)
		return res
	}))

	// negative integer
	t.Run("negative integer", tomlReaderTest([]byte(`n = -5`), func() *model.Value {
		res := model.NewMapValue()
		_ = res.SetMapKey("n", model.NewIntValue(-5))
		return res
	}))

	// scientific float
	t.Run("scientific float", tomlReaderTest([]byte(`f = 1e3`), func() *model.Value {
		res := model.NewMapValue()
		_ = res.SetMapKey("f", model.NewFloatValue(1000.0))
		return res
	}))

	// array of inline tables
	t.Run("array of inline tables", tomlReaderTest([]byte(`items = [{a = 1}, {a = 2}]`), func() *model.Value {
		res := model.NewMapValue()
		items := model.NewSliceValue()
		p1 := model.NewMapValue()
		_ = p1.SetMapKey("a", model.NewIntValue(1))
		_ = items.Append(p1)
		p2 := model.NewMapValue()
		_ = p2.SetMapKey("a", model.NewIntValue(2))
		_ = items.Append(p2)
		_ = res.SetMapKey("items", items)
		return res
	}))

	// nested tables using headers
	t.Run("nested table headers", tomlReaderTest([]byte(`[server]
ip = "127.0.0.1"
[server.db]
name = "maindb"`), func() *model.Value {
		res := model.NewMapValue()
		server := model.NewMapValue()
		_ = server.SetMapKey("ip", model.NewStringValue("127.0.0.1"))
		db := model.NewMapValue()
		_ = db.SetMapKey("name", model.NewStringValue("maindb"))
		_ = server.SetMapKey("db", db)
		_ = res.SetMapKey("server", server)
		return res
	}))

	t.Run("sub-table in array of tables", tomlReaderTest([]byte(`[[products]]
name = "Hammer"
sku = 738594937

[products.appearance]
color = "red"

[[products]]
name = "Screwdriver"
sku = 12341234`), func() *model.Value {
		res := model.NewMapValue()
		products := model.NewSliceValue()
		hammer := model.NewMapValue()
		_ = hammer.SetMapKey("name", model.NewStringValue("Hammer"))
		_ = hammer.SetMapKey("sku", model.NewIntValue(738594937))
		appearance := model.NewMapValue()
		_ = appearance.SetMapKey("color", model.NewStringValue("red"))
		_ = hammer.SetMapKey("appearance", appearance)
		_ = products.Append(hammer)
		screwdriver := model.NewMapValue()
		_ = screwdriver.SetMapKey("name", model.NewStringValue("Screwdriver"))
		_ = screwdriver.SetMapKey("sku", model.NewIntValue(12341234))
		_ = products.Append(screwdriver)
		_ = res.SetMapKey("products", products)
		return res
	}))
}

func TestTomlReader_QuotedKeys(t *testing.T) {
	// quoted single key with dot should be a single key
	t.Run("quoted single segment containing dot", tomlReaderTest([]byte(`"a.b" = 1`), func() *model.Value {
		res := model.NewMapValue()
		_ = res.SetMapKey("a.b", model.NewIntValue(1))
		return res
	}))

	// unquoted dotted key should create nested maps
	t.Run("unquoted dotted key creates nested maps", tomlReaderTest([]byte(`a.b = 2`), func() *model.Value {
		res := model.NewMapValue()
		a := model.NewMapValue()
		_ = a.SetMapKey("b", model.NewIntValue(2))
		_ = res.SetMapKey("a", a)
		return res
	}))

	// mixture: first segment unquoted, second quoted containing dot
	t.Run("mixed quoted segment", tomlReaderTest([]byte(`a."b.c" = 3`), func() *model.Value {
		res := model.NewMapValue()
		a := model.NewMapValue()
		_ = a.SetMapKey("b.c", model.NewIntValue(3))
		_ = res.SetMapKey("a", a)
		return res
	}))
}

func TestTomlReader_ComplexFile(t *testing.T) {
	dataPath := filepath.Join("testdata", "complex_example.toml")
	b, err := os.ReadFile(dataPath)
	if err != nil {
		t.Fatalf("failed reading test data: %v", err)
	}

	r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error creating reader: %v", err)
	}

	val, err := r.Read(b)
	if err != nil {
		t.Fatalf("unexpected error reading toml: %v", err)
	}

	// spot check some keys
	owner, err := val.GetMapKey("owner")
	if err != nil {
		t.Fatalf("missing owner: %v", err)
	}
	name, err := owner.GetMapKey("name")
	if err != nil {
		t.Fatalf("missing owner.name: %v", err)
	}
	if got, _ := name.StringValue(); got != "Tom Preston-Werner" {
		t.Fatalf("unexpected owner.name: %s", got)
	}

	// quoted key
	qk, err := val.GetMapKey("quoted key")
	if err != nil {
		t.Fatalf("missing quoted key: %v", err)
	}
	if s, _ := qk.StringValue(); s != "quoted value" {
		t.Fatalf("unexpected quoted key value: %s", s)
	}

	// products array length
	products, err := val.GetMapKey("products")
	if err != nil {
		t.Fatalf("missing products: %v", err)
	}
	if l, _ := products.SliceLen(); l != 2 {
		t.Fatalf("expected 2 products, got %d", l)
	}

	// a.b quoted
	ab, err := val.GetMapKey("a.b")
	if err != nil {
		t.Fatalf("missing a.b: %v", err)
	}
	if i, _ := ab.IntValue(); i != 42 {
		t.Fatalf("unexpected a.b: %d", i)
	}

	// nested table header value
	db, err := val.GetMapKey("database")
	if err != nil {
		t.Fatalf("missing database: %v", err)
	}
	rep, err := db.GetMapKey("replica")
	if err != nil {
		t.Fatalf("missing database.replica: %v", err)
	}
	if n, _ := rep.GetMapKey("name"); n == nil {
		t.Fatalf("missing database.replica.name")
	}
}

func TestTomlReader_EdgeCases(t *testing.T) {
	// conflict: scalar then dotted key
	t.Run("scalar then dotted key conflict", func(t *testing.T) {
		src := []byte("a = 1\na.b = 2")
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		_, err = r.Read(src)
		if err == nil {
			t.Fatalf("expected error for scalar then dotted key conflict, got nil")
		}
	})

	// array-table conflict: scalar then array-table
	t.Run("scalar then array-table conflict", func(t *testing.T) {
		src := []byte("a = 1\n[[a]]\nname = \"x\"")
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		_, err = r.Read(src)
		if err == nil {
			t.Fatalf("expected error for scalar then array-table conflict, got nil")
		}
	})

	// repeated table headers should merge keys
	t.Run("repeated explicit table headers merge", func(t *testing.T) {
		src := []byte("[t]\na = 1\n[t]\nb = 2")
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		val, err := r.Read(src)
		if err != nil {
			t.Fatalf("unexpected error: %v", err)
		}
		m, err := val.GetMapKey("t")
		if err != nil {
			t.Fatalf("missing table t: %v", err)
		}
		if a, err := m.GetMapKey("a"); err != nil || a == nil {
			t.Fatalf("expected a in t: %v", err)
		}
		if b, err := m.GetMapKey("b"); err != nil || b == nil {
			t.Fatalf("expected b in t: %v", err)
		}
	})

	// inline table then explicit table should merge
	t.Run("inline table then explicit header merges", func(t *testing.T) {
		src := []byte("t = {a = 1}\n[t]\nb = 2")
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		val, err := r.Read(src)
		if err != nil {
			t.Fatalf("unexpected error: %v", err)
		}
		m, err := val.GetMapKey("t")
		if err != nil {
			t.Fatalf("missing table t: %v", err)
		}
		if a, err := m.GetMapKey("a"); err != nil || a == nil {
			t.Fatalf("expected a in t: %v", err)
		}
		if b, err := m.GetMapKey("b"); err != nil || b == nil {
			t.Fatalf("expected b in t: %v", err)
		}
	})

	// integer overflow
	t.Run("integer overflow", func(t *testing.T) {
		src := []byte("big = 9223372036854775808") // int64 max + 1
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		_, err = r.Read(src)
		if err == nil {
			t.Fatalf("expected error for integer overflow, got nil")
		}
	})

	// ensure arrays with trailing commas parse (already covered elsewhere but add explicit check)
	t.Run("array trailing comma parse", func(t *testing.T) {
		src := []byte("arr = [1,2,]")
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		val, err := r.Read(src)
		if err != nil {
			t.Fatalf("unexpected error: %v", err)
		}
		arr, err := val.GetMapKey("arr")
		if err != nil {
			t.Fatalf("missing arr: %v", err)
		}
		if l, _ := arr.SliceLen(); l != 2 {
			t.Fatalf("expected 2 items in arr, got %d", l)
		}
	})

	// ensure arrays of inline tables types preserved
	t.Run("array of inline tables preserves types", func(t *testing.T) {
		src := []byte("items = [{a = 1}, {a = 2}]")
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		val, err := r.Read(src)
		if err != nil {
			t.Fatalf("unexpected error: %v", err)
		}
		items, err := val.GetMapKey("items")
		if err != nil {
			t.Fatalf("missing items: %v", err)
		}
		if l, _ := items.SliceLen(); l != 2 {
			t.Fatalf("expected 2 items, got %d", l)
		}
		// first element has a=1
		it0, _ := items.GetSliceIndex(0)
		if a, err := it0.GetMapKey("a"); err != nil {
			t.Fatalf("missing a in first item: %v", err)
		} else if ai, _ := a.IntValue(); ai != 1 {
			t.Fatalf("unexpected a in first item: %d", ai)
		}
	})
}

func TestTomlReader_TimeStrings(t *testing.T) {
	// Local date
	t.Run("local date string", func(t *testing.T) {
		src := []byte("d = 1979-05-27")
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		val, err := r.Read(src)
		if err != nil {
			t.Fatalf("unexpected error parsing: %v", err)
		}
		v, err := val.GetMapKey("d")
		if err != nil {
			t.Fatalf("missing key d: %v", err)
		}
		s, err := v.StringValue()
		if err != nil {
			t.Fatalf("value not string: %v", err)
		}
		if s != "1979-05-27" {
			t.Fatalf("expected %q got %q", "1979-05-27", s)
		}
	})

	// Local time
	t.Run("local time string", func(t *testing.T) {
		src := []byte("t = 07:32:00")
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		val, err := r.Read(src)
		if err != nil {
			t.Fatalf("unexpected error parsing: %v", err)
		}
		v, err := val.GetMapKey("t")
		if err != nil {
			t.Fatalf("missing key t: %v", err)
		}
		s, err := v.StringValue()
		if err != nil {
			t.Fatalf("value not string: %v", err)
		}
		if s != "07:32:00" {
			t.Fatalf("expected %q got %q", "07:32:00", s)
		}
	})

	// Local date-time
	t.Run("local datetime string", func(t *testing.T) {
		src := []byte("dt = 1979-05-27T07:32:00")
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		val, err := r.Read(src)
		if err != nil {
			t.Fatalf("unexpected error parsing: %v", err)
		}
		v, err := val.GetMapKey("dt")
		if err != nil {
			t.Fatalf("missing key dt: %v", err)
		}
		s, err := v.StringValue()
		if err != nil {
			t.Fatalf("value not string: %v", err)
		}
		if s != "1979-05-27T07:32:00" {
			t.Fatalf("expected %q got %q", "1979-05-27T07:32:00", s)
		}
	})

	// DateTime with timezone (RFC3339)
	t.Run("datetime with tz string", func(t *testing.T) {
		src := []byte("dt = 1979-05-27T07:32:00-08:00")
		r, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("unexpected error creating reader: %v", err)
		}
		val, err := r.Read(src)
		if err != nil {
			t.Fatalf("unexpected error parsing: %v", err)
		}
		v, err := val.GetMapKey("dt")
		if err != nil {
			t.Fatalf("missing key dt: %v", err)
		}
		s, err := v.StringValue()
		if err != nil {
			t.Fatalf("value not string: %v", err)
		}
		if s != "1979-05-27T07:32:00-08:00" {
			t.Fatalf("expected %q got %q", "1979-05-27T07:32:00-08:00", s)
		}
	})
}
```

## File: `parsing/toml/toml_writer.go`
```go
package toml

import (
	"bytes"
	"fmt"
	"reflect"
	"strconv"
	"strings"

	pkg "github.com/pelletier/go-toml/v2"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
)

var _ parsing.Writer = (*tomlWriter)(nil)

func newTOMLWriter(options parsing.WriterOptions) (parsing.Writer, error) {
	w := &tomlWriter{}
	return w, nil
}

type tomlWriter struct {
}

// Write converts the dasel model.Value into Go values backed by dynamically
// generated struct types (reflect.StructOf) that preserve key ordering, then
// delegates to go-toml Marshal to produce canonical TOML output.
// This implementation doesn't preserve all formatting metadata (multiline strings, etc)
// and needs some work to do so.
func (j *tomlWriter) Write(value *model.Value) ([]byte, error) {
	if value == nil {
		return nil, fmt.Errorf("nil value")
	}

	var goValue interface{}
	var err error

	if value.IsMap() {
		goValue, err = buildGoValueForMap(value)
		if err != nil {
			return nil, fmt.Errorf("failed to construct go value: %w", err)
		}
	} else {
		// handle scalars, slices, etc. Use goTypeAndValue to get a concrete reflect.Value
		typ, rv, err := goTypeAndValue(value)
		if err != nil {
			return nil, fmt.Errorf("failed to convert non-map top-level value: %w", err)
		}
		// For nil/zero interface, ensure we pass nil interface rather than a typed zero.
		if typ.Kind() == reflect.Interface && rv.IsZero() {
			goValue = nil
		} else {
			goValue = rv.Interface()
		}
	}

	// We currently encode the top level value directly. We have little control over nested values.
	// Perhaps it would be better to implement a custom Encoder that respects metadata on nested values?
	var buf bytes.Buffer
	encoder := pkg.NewEncoder(&buf)

	if err := encoder.Encode(goValue); err != nil {
		return nil, fmt.Errorf("toml encode failed: %w", err)
	}
	outBytes := buf.Bytes()

	// Ensure trailing newline for consistency with other format writers/tests.
	if len(outBytes) == 0 || outBytes[len(outBytes)-1] != '\n' {
		outBytes = append(outBytes, '\n')
	}

	return outBytes, nil
}

// buildGoValueForMap constructs a reflect.Value that is a struct with fields in
// the same order as keys in the provided map Value. The struct fields are
// tagged with `toml:"<original key>"` so go-toml will use the original key
// names when encoding.
func buildGoValueForMap(v *model.Value) (interface{}, error) {
	kvs, err := v.MapKeyValues()
	if err != nil {
		return nil, err
	}

	// Build struct fields in order
	fields := make([]reflect.StructField, 0, len(kvs))
	fieldValues := make([]reflect.Value, 0, len(kvs))

	for i, kv := range kvs {
		ft, fv, err := goTypeAndValue(kv.Value)
		if err != nil {
			return nil, fmt.Errorf("error converting key %q: %w", kv.Key, err)
		}

		tomlTagContents := []string{kv.Key}

		//  These currently do not take effect. They are placeholders for future functionality.
		if v, ok := kv.Value.MetadataValue(tomlStringStyleKey); ok {
			if style, ok := v.(string); ok && style != "" {
				switch style {
				case tomlStringStyleMultilineBasic, tomlStringStyleMultilineLiteral:
					tomlTagContents = append(tomlTagContents, "multiline")
				}
			}
		}
		if v, ok := kv.Value.MetadataValue(tomlTableStyleKey); ok {
			if style, ok := v.(string); ok && style != "" {
				switch style {
				case tomlTableStyleInline:
					tomlTagContents = append(tomlTagContents, "inline")
				}
			}
		}

		// create exported field name (F0, F1...) and set tag to preserve toml key
		field := reflect.StructField{
			Name: "F" + strconv.Itoa(i),
			Type: ft,
			Tag:  reflect.StructTag(fmt.Sprintf(`toml:"%s"`, strings.Join(tomlTagContents, ","))),
		}
		fields = append(fields, field)
		fieldValues = append(fieldValues, fv)
	}

	structType := reflect.StructOf(fields)
	val := reflect.New(structType).Elem()

	for i := range fieldValues {
		val.Field(i).Set(fieldValues[i])
	}

	return val.Interface(), nil
}

// goTypeAndValue returns a reflect.Type and a reflect.Value suitable for use as a
// struct field/type for the given model.Value. It converts nested maps into
// reflect.StructOf types recursively (preserving key order), converts slices to
// slices of appropriate element types when possible, or []interface{} otherwise.
func goTypeAndValue(v *model.Value) (reflect.Type, reflect.Value, error) {
	switch v.Type() {
	case model.TypeString:
		s, err := v.StringValue()
		if err != nil {
			return nil, reflect.Value{}, err
		}
		return reflect.TypeOf(""), reflect.ValueOf(s), nil
	case model.TypeInt:
		i, err := v.IntValue()
		if err != nil {
			return nil, reflect.Value{}, err
		}
		// use int64 to be safe
		return reflect.TypeOf(int64(0)), reflect.ValueOf(i), nil
	case model.TypeFloat:
		f, err := v.FloatValue()
		if err != nil {
			return nil, reflect.Value{}, err
		}
		return reflect.TypeOf(float64(0)), reflect.ValueOf(f), nil
	case model.TypeBool:
		b, err := v.BoolValue()
		if err != nil {
			return nil, reflect.Value{}, err
		}
		return reflect.TypeOf(true), reflect.ValueOf(b), nil
	case model.TypeNull:
		// represent null as interface{}(nil)
		return reflect.TypeOf((*interface{})(nil)).Elem(), reflect.Zero(reflect.TypeOf((*interface{})(nil)).Elem()), nil
	case model.TypeMap:
		// For nested maps, prefer map[string]interface{} values rather than
		// generating nested struct types. Using struct types for nested maps
		// causes go-toml to emit explicit table headers for those nested
		// structures which can change the document shape on round-trip. The
		// top-level map is still handled by buildGoValueForMap which generates
		// a struct to preserve ordering.
		kvs, err := v.MapKeyValues()
		if err != nil {
			return nil, reflect.Value{}, err
		}
		m := make(map[string]interface{})
		for _, kv := range kvs {
			_, rv, err := goTypeAndValue(kv.Value)
			if err != nil {
				return nil, reflect.Value{}, fmt.Errorf("error in nested key %q: %w", kv.Key, err)
			}
			m[kv.Key] = rv.Interface()
		}
		return reflect.TypeOf(map[string]interface{}{}), reflect.ValueOf(m), nil
	case model.TypeSlice:
		// Decide element types. If all elements are maps and have compatible keys,
		// build a struct type for elements and return a slice of that struct type.
		length, _ := v.SliceLen()
		if length == 0 {
			// empty slice -> use []interface{}
			elemType := reflect.TypeOf((*interface{})(nil)).Elem()
			return reflect.SliceOf(elemType), reflect.MakeSlice(reflect.SliceOf(elemType), 0, 0), nil
		}

		// inspect first element
		first, _ := v.GetSliceIndex(0)
		if first.IsMap() {
			// Collect union of keys across elements in order of appearance
			seen := map[string]bool{}
			keys := make([]string, 0)
			_ = v.RangeSlice(func(_ int, item *model.Value) error {
				if !item.IsMap() {
					// mixed types -> fallback to []interface{}
					keys = nil
					return nil
				}
				kvs, _ := item.MapKeyValues()
				for _, kv := range kvs {
					if !seen[kv.Key] {
						seen[kv.Key] = true
						keys = append(keys, kv.Key)
					}
				}
				return nil
			})

			if keys != nil {
				// Build []map[string]interface{} to preserve keys and values without
				// forcing a generated struct type which can cause conversion issues.
				sliceMaps := make([]map[string]interface{}, 0, length)
				_ = v.RangeSlice(func(_ int, item *model.Value) error {
					m := map[string]interface{}{}
					if item.IsMap() {
						kvs, _ := item.MapKeyValues()
						for _, kv := range kvs {
							_, rv, err := goTypeAndValue(kv.Value)
							if err != nil {
								return err
							}
							m[kv.Key] = rv.Interface()
						}
					}
					sliceMaps = append(sliceMaps, m)
					return nil
				})
				return reflect.TypeOf([]map[string]interface{}{}), reflect.ValueOf(sliceMaps), nil
			}
		}

		// fallback: build []interface{}
		elems := make([]interface{}, 0, length)
		_ = v.RangeSlice(func(_ int, item *model.Value) error {
			gt, rv, err := goTypeAndValue(item)
			if err != nil {
				return err
			}
			// convert reflect.Value to interface{}
			elems = append(elems, rv.Interface())
			_ = gt
			return nil
		})
		return reflect.TypeOf([]interface{}{}), reflect.ValueOf(elems), nil
	default:
		// fallback to stringified interface
		s := fmt.Sprintf("%v", v.Interface())
		return reflect.TypeOf(""), reflect.ValueOf(s), nil
	}
}
```

## File: `parsing/toml/toml_writer_test.go`
```go
package toml_test

import (
	"os"
	"strings"
	"testing"

	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/toml"
)

func TestTomlWriter_RoundTripSimple(t *testing.T) {
	doc := []byte(`title = "TOML Example"
[owner]
name = "Tom Preston-Werner"

[database]
ports = [8001, 8001, 8002]
enabled = true
`)

	reader, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error creating reader: %v", err)
	}
	writer, err := toml.TOML.NewWriter(parsing.DefaultWriterOptions())
	if err != nil {
		t.Fatalf("unexpected error creating writer: %v", err)
	}

	v, err := reader.Read(doc)
	if err != nil {
		t.Fatalf("failed to read doc: %v", err)
	}

	out, err := writer.Write(v)
	if err != nil {
		t.Fatalf("failed to write doc: %v", err)
	}

	v2, err := reader.Read(out)
	if err != nil {
		t.Fatalf("failed to read generated doc: %v", err)
	}

	res, err := v.Equal(v2)
	if err != nil {
		t.Fatalf("failed to compare values: %v", err)
	}
	b, err := res.BoolValue()
	if err != nil {
		t.Fatalf("failed to get bool from equal result: %v", err)
	}
	if !b {
		t.Fatalf("round-trip value mismatch\norig:\n%s\nnew:\n%s", string(doc), string(out))
	}
}

func TestTomlWriter_OrderPreserved(t *testing.T) {
	doc := []byte("a = 1\nb = 2\nc = 3\n")
	reader, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error creating reader: %v", err)
	}
	writer, err := toml.TOML.NewWriter(parsing.DefaultWriterOptions())
	if err != nil {
		t.Fatalf("unexpected error creating writer: %v", err)
	}

	v, err := reader.Read(doc)
	if err != nil {
		t.Fatalf("failed to read doc: %v", err)
	}

	out, err := writer.Write(v)
	if err != nil {
		t.Fatalf("failed to write doc: %v", err)
	}

	// Ensure key order a, b, c appears in the output
	outStr := string(out)
	ia := strings.Index(outStr, "a =")
	ib := strings.Index(outStr, "b =")
	ic := strings.Index(outStr, "c =")
	if ia == -1 || ib == -1 || ic == -1 {
		t.Fatalf("expected keys missing in output: %s", outStr)
	}
	if ia >= ib || ib >= ic {
		t.Fatalf("expected order a,b,c in output; got:\n%s", outStr)
	}
}

func TestTomlWriter_ArrayOfTables_RoundTrip(t *testing.T) {
	doc := []byte(`[[products]]
name = "Hammer"
sku = 738594937

[[products]]
name = "Screwdriver"
sku = 12341234
`)

	reader, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error creating reader: %v", err)
	}
	writer, err := toml.TOML.NewWriter(parsing.DefaultWriterOptions())
	if err != nil {
		t.Fatalf("unexpected error creating writer: %v", err)
	}

	v, err := reader.Read(doc)
	if err != nil {
		t.Fatalf("failed to read doc: %v", err)
	}

	out, err := writer.Write(v)
	if err != nil {
		t.Fatalf("failed to write doc: %v", err)
	}

	v2, err := reader.Read(out)
	if err != nil {
		t.Fatalf("failed to read generated doc: %v", err)
	}

	res, err := v.Equal(v2)
	if err != nil {
		t.Fatalf("failed to compare values: %v", err)
	}
	b, err := res.BoolValue()
	if err != nil {
		t.Fatalf("failed to get bool from equal result: %v", err)
	}
	if !b {
		t.Fatalf("array-table round-trip mismatch\norig:\n%s\nnew:\n%s", string(doc), string(out))
	}
}

func TestTomlWriter_MoreCases(t *testing.T) {
	cases := map[string][]byte{
		"simple array":           []byte("nums = [1, 2, 3]"),
		"mixed array":            []byte("mix = [1, \"two\", true]"),
		"inline nested table":    []byte("props = { sub = { a = 1 }, arr = [1,2] }"),
		"quoted key with space":  []byte("\"a b\" = \"val\""),
		"dotted and quoted mix":  []byte("a.\"b.c\".d = \"x\""),
		"negative integer":       []byte("n = -5"),
		"scientific float":       []byte("f = 1e3"),
		"array of inline tables": []byte("items = [{a = 1}, {a = 2} ]"),
		"nested table headers":   []byte("[server]\nip = \"127.0.0.1\"\n[server.db]\nname = \"maindb\""),
		"quoted single dot":      []byte("\"a.b\" = 1"),
		"unquoted dotted":        []byte("a.b = 2"),
		"mixed quoted segment":   []byte("a.\"b.c\" = 3"),
		"inline then explicit":   []byte("t = {a = 1}\n[t]\nb = 2"),
		"array trailing comma":   []byte("arr = [1,2,]"),
		"local date":             []byte("d = 1979-05-27"),
		"local time":             []byte("t = 07:32:00"),
		"local datetime":         []byte("dt = 1979-05-27T07:32:00"),
		"datetime with tz":       []byte("dt = 1979-05-27T07:32:00-08:00"),
		"multiline basic string": []byte("m = '''not used'''\n"),
	}

	reader, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error creating reader: %v", err)
	}
	writer, err := toml.TOML.NewWriter(parsing.DefaultWriterOptions())
	if err != nil {
		t.Fatalf("unexpected error creating writer: %v", err)
	}

	for name, src := range cases {
		src := src
		name := name
		t.Run(name, func(t *testing.T) {
			v, err := reader.Read(src)
			if err != nil {
				t.Fatalf("reader error for %s: %v", name, err)
			}

			out, err := writer.Write(v)
			if err != nil {
				t.Fatalf("writer error for %s: %v", name, err)
			}

			v2, err := reader.Read(out)
			if err != nil {
				t.Fatalf("reader error for generated output %s: %v", name, err)
			}

			res, err := v.Equal(v2)
			if err != nil {
				t.Fatalf("compare error for %s: %v", name, err)
			}
			b, err := res.BoolValue()
			if err != nil {
				t.Fatalf("bool extraction error for %s: %v", name, err)
			}
			if !b {
				t.Fatalf("round-trip mismatch for %s\norig:\n%s\nnew:\n%s", name, string(src), string(out))
			}
		})
	}

	// Complex example file round-trip
	t.Run("complex example file", func(t *testing.T) {
		//t.Skip("Multiline string formatting not yet preserved")
		dataPath := "testdata/complex_example.toml"
		b, err := os.ReadFile(dataPath)
		if err != nil {
			t.Fatalf("failed reading test data: %v", err)
		}

		v, err := reader.Read(b)
		if err != nil {
			t.Fatalf("reader error for complex file: %v", err)
		}

		out, err := writer.Write(v)
		if err != nil {
			t.Fatalf("writer error for complex file: %v", err)
		}

		v2, err := reader.Read(out)
		if err != nil {
			t.Fatalf("failed to re-read generated complex doc: %v", err)
		}

		res, err := v.Equal(v2)
		if err != nil {
			t.Fatalf("compare error for complex file: %v", err)
		}
		b2, err := res.BoolValue()
		if err != nil {
			t.Fatalf("bool extraction error for complex file: %v", err)
		}
		if !b2 {
			// Print original and written output for debugging.
			t.Fatalf("complex-example round-trip mismatch\n--- ORIGINAL ---\n%s\n--- WRITTEN ---\n%s\n", string(b), string(out))
		}
	})
}

func TestTomlWriter_StrictOutput(t *testing.T) {
	reader, err := toml.TOML.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error creating reader: %v", err)
	}
	writer, err := toml.TOML.NewWriter(parsing.DefaultWriterOptions())
	if err != nil {
		t.Fatalf("unexpected error creating writer: %v", err)
	}

	tests := map[string]struct {
		src []byte
		exp string
	}{
		"ordered scalars": {
			src: []byte("a = 1\nb = 2\nc = 3\n"),
			exp: "a = 1\nb = 2\nc = 3\n",
		},
		"inline array": {
			src: []byte("nums = [1,2,3]"),
			exp: "nums = [1, 2, 3]\n",
		},
		"quoted key": {
			src: []byte("\"a b\" = \"val\""),
			exp: "'a b' = 'val'\n",
		},
		"array of tables": {
			src: []byte(`[[products]]
name = "Hammer"
sku = 738594937

[[products]]
name = "Screwdriver"
sku = 12341234
`),
			exp: `[[products]]
name = 'Hammer'
sku = 738594937

[[products]]
name = 'Screwdriver'
sku = 12341234
`,
		},
	}

	for name, tc := range tests {
		name := name
		tc := tc
		t.Run(name, func(t *testing.T) {
			v, err := reader.Read(tc.src)
			if err != nil {
				t.Fatalf("reader error for %s: %v", name, err)
			}

			out, err := writer.Write(v)
			if err != nil {
				t.Fatalf("writer error for %s: %v", name, err)
			}

			got := string(out)
			if got != tc.exp {
				t.Fatalf("strict output mismatch for %s\nexpected:\n%s\n got:\n%s", name, tc.exp, got)
			}
		})
	}
}
```

## File: `parsing/toml/testdata/complex_example.toml`
```
# Comprehensive TOML example exercising many features

"quoted key" = "quoted value"

"a.b" = 42

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
organization = "GitHub"
bio = "Developer\nMaintainer"

# Quoted keys and dotted keys
[server]
ip = "192.168.0.1"
port = 8080

[server.settings]
# inline table-like structure but using table header
max_connections = 100
enabled = true

# Inline table example
props = { key1 = "value1", key2 = "value2" }

# Arrays
nums = [1, 2, 3]
mix = [1, "two", true]
empty = []
trailing = ["a", "b",]

# Nested inline table and array
props2 = { sub = { a = 1 }, arr = [1,2] }


# Mixed dotted and quoted
[a."b.c"]
d = "x"

# Negative and scientific numbers
n = -5
f = 1e3

# Arrays of inline tables
items = [{a = 1}, {a = 2}]

# Array of tables
[[products]]
name = "Hammer"
sku = 738594937

[products.appearance]
color = "red"

[[products]]
name = "Screwdriver"
sku = 12341234

# Nested table headers
[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true

[database.replica]
name = "replica1"

# Multi-line basic string
multiline = """
This is a
multiline string.
"""

# Literal multi-line string
literal = '''
This is a 'literal' multiline
string with no escapes.
'''

# Comments and spacing
# End of file
```

## File: `parsing/xml/reader.go`
```go
package xml

import (
	"bytes"
	"encoding/xml"
	"errors"
	"fmt"
	"io"
	"strings"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
)

// Security limits for XML parsing to prevent DoS attacks.
// These limits are intentionally conservative to balance usability and safety.
const (
	maxCommentLength = 10_000     // Maximum bytes per comment (10KB) - prevents memory exhaustion from single large comments
	maxTotalComments = 1_000      // Maximum comments per document - prevents abuse via comment flooding
	maxXMLSize       = 10_000_000 // Maximum XML input size (10MB) - prevents processing of excessively large files
)

func newXMLReader(options parsing.ReaderOptions) (parsing.Reader, error) {
	return &xmlReader{
		structured: options.Ext["xml-mode"] == "structured",
	}, nil
}

type xmlReader struct {
	structured bool
}

// Read reads a value from a byte slice.
func (j *xmlReader) Read(data []byte) (*model.Value, error) {
	if len(data) > maxXMLSize {
		return nil, fmt.Errorf("XML input exceeds maximum size of %d bytes", maxXMLSize)
	}

	decoder := xml.NewDecoder(bytes.NewReader(data))
	decoder.Strict = true

	totalComments := 0
	el, err := j.parseElement(decoder, xml.StartElement{
		Name: xml.Name{
			Local: "root",
		},
	}, &totalComments)
	if err != nil {
		return nil, err
	}

	if j.structured {
		return el.toStructuredModel()
	}
	return el.toFriendlyModel()
}

func (e *xmlElement) toStructuredModel() (*model.Value, error) {
	attrs := model.NewMapValue()
	for _, attr := range e.Attrs {
		if err := attrs.SetMapKey(attr.Name, model.NewStringValue(attr.Value)); err != nil {
			return nil, err
		}
	}
	res := model.NewMapValue()
	if len(e.ProcessingInstructions) > 0 {
		res.SetMetadataValue("xml_processing_instructions", e.ProcessingInstructions)
	}
	if len(e.Comments) > 0 {
		res.SetMetadataValue("xml_comments", e.Comments)
	}
	if err := res.SetMapKey("name", model.NewStringValue(e.Name)); err != nil {
		return nil, err
	}
	if err := res.SetMapKey("attrs", attrs); err != nil {
		return nil, err
	}

	if err := res.SetMapKey("content", model.NewStringValue(e.Content)); err != nil {
		return nil, err
	}
	children := model.NewSliceValue()
	for _, child := range e.Children {
		childModel, err := child.toStructuredModel()
		if err != nil {
			return nil, err
		}
		if err := children.Append(childModel); err != nil {
			return nil, err
		}
	}
	if err := res.SetMapKey("children", children); err != nil {
		return nil, err
	}
	return res, nil
}

func (e *xmlElement) toFriendlyModel() (*model.Value, error) {
	if len(e.Attrs) == 0 && len(e.Children) == 0 && len(e.Comments) == 0 {
		return model.NewStringValue(e.Content), nil
	}

	res := model.NewMapValue()
	if len(e.ProcessingInstructions) > 0 {
		res.SetMetadataValue("xml_processing_instructions", e.ProcessingInstructions)
	}
	if len(e.Comments) > 0 {
		res.SetMetadataValue("xml_comments", e.Comments)
	}
	for _, attr := range e.Attrs {
		if err := res.SetMapKey("-"+attr.Name, model.NewStringValue(attr.Value)); err != nil {
			return nil, err
		}
	}

	if len(e.Content) > 0 {
		if err := res.SetMapKey("#text", model.NewStringValue(e.Content)); err != nil {
			return nil, err
		}
	}

	if len(e.Children) > 0 {
		childElementKeys := make([]string, 0)
		childElements := make(map[string][]*xmlElement)

		for _, child := range e.Children {
			if _, ok := childElements[child.Name]; !ok {
				childElementKeys = append(childElementKeys, child.Name)
			}
			childElements[child.Name] = append(childElements[child.Name], child)
		}

		for _, key := range childElementKeys {
			cs := childElements[key]
			switch len(cs) {
			case 0:
				continue
			case 1:
				childModel, err := cs[0].toFriendlyModel()
				if err != nil {
					return nil, err
				}
				if err := res.SetMapKey(key, childModel); err != nil {
					return nil, err
				}
			default:
				children := model.NewSliceValue()
				for _, child := range cs {
					childModel, err := child.toFriendlyModel()
					if err != nil {
						return nil, err
					}
					if err := children.Append(childModel); err != nil {
						return nil, err
					}
				}
				if err := res.SetMapKey(key, children); err != nil {
					return nil, err
				}
			}
		}
	}

	return res, nil
}

func (j *xmlReader) parseElement(decoder *xml.Decoder, element xml.StartElement, totalComments *int) (*xmlElement, error) {
	el := &xmlElement{
		Name:                   element.Name.Local,
		Attrs:                  make([]xmlAttr, 0),
		Children:               make([]*xmlElement, 0),
		ProcessingInstructions: make([]*xmlProcessingInstruction, 0),
		Comments:               make([]*xmlComment, 0),
	}

	for _, attr := range element.Attr {
		el.Attrs = append(el.Attrs, xmlAttr{
			Name:  attr.Name.Local,
			Value: attr.Value,
		})
	}

	var processingInstructions []*xmlProcessingInstruction
	var comments []*xmlComment

	for {
		t, err := decoder.Token()
		if errors.Is(err, io.EOF) {
			if el.Name == "root" {
				return el, nil
			}
			return nil, fmt.Errorf("unexpected EOF")
		}
		if err != nil {
			return nil, fmt.Errorf("failed to read token: %w", err)
		}
		if t == nil {
			if el.Name == "root" {
				return el, nil
			}
			return nil, fmt.Errorf("unexpected nil token")
		}

		switch t := t.(type) {
		case xml.StartElement:
			child, err := j.parseElement(decoder, t, totalComments)
			if err != nil {
				return nil, err
			}
			if len(comments) > 0 {
				child.Comments = append(comments, child.Comments...)
				comments = nil
			}
			if len(processingInstructions) > 0 {
				child.ProcessingInstructions = processingInstructions
				processingInstructions = nil
			}
			el.Children = append(el.Children, child)
		case xml.CharData:
			stringContent := string(t)
			if strings.TrimSpace(stringContent) == "" {
				continue
			}
			el.Content += stringContent
		case xml.EndElement:
			if len(comments) > 0 {
				el.Comments = append(el.Comments, comments...)
			}
			return el, nil
		case xml.Comment:
			commentText := string(t)
			if len(commentText) > maxCommentLength {
				return nil, fmt.Errorf("comment exceeds maximum length of %d bytes", maxCommentLength)
			}
			if *totalComments >= maxTotalComments {
				return nil, fmt.Errorf("document exceeds maximum comment count of %d", maxTotalComments)
			}
			comment := &xmlComment{
				Text: commentText,
			}
			comments = append(comments, comment)
			*totalComments++
			continue
		case xml.ProcInst:
			pi := &xmlProcessingInstruction{
				Target: t.Target,
				Value:  string(t.Inst),
			}
			processingInstructions = append(processingInstructions, pi)
			continue
		case xml.Directive:
			continue
		case xml.Attr:
			continue
		default:
			return nil, fmt.Errorf("unexpected token: %v", t)
		}
	}
}
```

## File: `parsing/xml/reader_test.go`
```go
package xml_test

import (
	"testing"

	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/json"
	"github.com/tomwright/dasel/v3/parsing/xml"
)

func TestXmlReader_Read(t *testing.T) {
	t.Run("nested xml elements", func(t *testing.T) {
		r, err := xml.XML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		w, err := json.JSON.NewWriter(parsing.DefaultWriterOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		data, err := r.Read([]byte(`<Document>
  <Sender>Ivanov</Sender>
  <In_N_Document>
    <N_Document>1024</N_Document>
    <Date_Reg>2024-06-21T15:07:29.0451517+03:00</Date_Reg>
  </In_N_Document>
  <Out_N_Document>
    <N_Document>2043</N_Document>
    <Date_Reg>2024-05-01T00:00:00</Date_Reg>
  </Out_N_Document>
  <Content>Skzzkz</Content>
  <DSP>true</DSP>
</Document>
`))
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		jsonBytes, err := w.Write(data)
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		expected := `{
    "Document": {
        "Sender": "Ivanov",
        "In_N_Document": {
            "N_Document": "1024",
            "Date_Reg": "2024-06-21T15:07:29.0451517+03:00"
        },
        "Out_N_Document": {
            "N_Document": "2043",
            "Date_Reg": "2024-05-01T00:00:00"
        },
        "Content": "Skzzkz",
        "DSP": "true"
    }
}
`
		if string(jsonBytes) != expected {
			t.Fatalf("Expected:\n%s\nGot:\n%s", expected, string(jsonBytes))
		}
	})

	t.Run("nested xml elements with processing instruction", func(t *testing.T) {
		r, err := xml.XML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		w, err := json.JSON.NewWriter(parsing.DefaultWriterOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		data, err := r.Read([]byte(`<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<Document>
  <Sender>Ivanov</Sender>
  <In_N_Document>
    <N_Document>1024</N_Document>
    <Date_Reg>2024-06-21T15:07:29.0451517+03:00</Date_Reg>
  </In_N_Document>
  <Out_N_Document>
    <N_Document>2043</N_Document>
    <Date_Reg>2024-05-01T00:00:00</Date_Reg>
  </Out_N_Document>
  <Content>Skzzkz</Content>
  <DSP>true</DSP>
</Document>
`))
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		jsonBytes, err := w.Write(data)
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		expected := `{
    "Document": {
        "Sender": "Ivanov",
        "In_N_Document": {
            "N_Document": "1024",
            "Date_Reg": "2024-06-21T15:07:29.0451517+03:00"
        },
        "Out_N_Document": {
            "N_Document": "2043",
            "Date_Reg": "2024-05-01T00:00:00"
        },
        "Content": "Skzzkz",
        "DSP": "true"
    }
}
`
		if string(jsonBytes) != expected {
			t.Fatalf("Expected:\n%s\nGot:\n%s", expected, string(jsonBytes))
		}
	})

	t.Run("cdata tag", func(t *testing.T) {
		r, err := xml.XML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		data, err := r.Read([]byte(`<foo>
	<![CDATA[<bar>baz</bar>]]>
</foo>
`))
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		x, err := data.GetMapKey("foo")
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}
		got, err := x.StringValue()
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		exp := "<bar>baz</bar>"
		if exp != got {
			t.Fatalf("Expected value %q but got %q", exp, got)
		}
	})

	t.Run("empty cdata tag", func(t *testing.T) {
		r, err := xml.XML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		data, err := r.Read([]byte(`<foo>
	<![CDATA[]]>
</foo>
`))
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		x, err := data.GetMapKey("foo")
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}
		got, err := x.StringValue()
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		exp := ""
		if exp != got {
			t.Fatalf("Expected value %q but got %q", exp, got)
		}
	})
}
```

## File: `parsing/xml/structured_comment_test.go`
```go
package xml_test

import (
	"strings"
	"testing"

	"github.com/tomwright/dasel/v3/parsing"
	daselxml "github.com/tomwright/dasel/v3/parsing/xml"
)

// newTestReaderWriter creates a reader and writer for round-trip testing.
func newTestReaderWriter(t *testing.T) (parsing.Reader, parsing.Writer) {
	t.Helper()
	r, err := daselxml.XML.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("Unexpected error creating reader: %s", err)
	}
	w, err := daselxml.XML.NewWriter(parsing.DefaultWriterOptions())
	if err != nil {
		t.Fatalf("Unexpected error creating writer: %s", err)
	}
	return r, w
}

// assertRoundTrip performs a read-write round-trip and verifies expected strings are present.
func assertRoundTrip(t *testing.T, r parsing.Reader, w parsing.Writer, input string, expected []string) {
	t.Helper()
	data, err := r.Read([]byte(input))
	if err != nil {
		t.Fatalf("Unexpected error reading XML: %s", err)
	}

	output, err := w.Write(data)
	if err != nil {
		t.Fatalf("Unexpected error writing XML: %s", err)
	}

	outputStr := string(output)
	for _, exp := range expected {
		if !strings.Contains(outputStr, exp) {
			t.Errorf("Expected output to contain %q, got:\n%s", exp, outputStr)
		}
	}
}

// TestXmlReader_StructuredModeWithComments tests comment preservation in structured mode
func TestXmlReader_StructuredModeWithComments(t *testing.T) {
	t.Run("basic_comment_structured", func(t *testing.T) {
		options := parsing.DefaultReaderOptions()
		options.Ext = map[string]string{"xml-mode": "structured"}
		r, err := daselxml.XML.NewReader(options)
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		input := `<!--comment--><root><child>text</child></root>`
		data, err := r.Read([]byte(input))
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		childrenNode, err := data.GetMapKey("children")
		if err != nil {
			t.Fatalf("Expected 'children' key in structured mode: %s", err)
		}

		childrenLen, err := childrenNode.SliceLen()
		if err != nil {
			t.Fatalf("Expected children to be a slice: %s", err)
		}

		if childrenLen == 0 {
			t.Fatalf("Expected at least one child element")
		}

		rootElement, err := childrenNode.GetSliceIndex(0)
		if err != nil {
			t.Fatalf("Expected to get first child: %s", err)
		}

		comments, ok := rootElement.MetadataValue("xml_comments")
		if !ok {
			t.Errorf("Expected xml_comments metadata to exist")
		}

		if comments == nil {
			t.Errorf("Expected comments to be preserved in structured mode")
		}
	})
}

// TestXmlRoundTrip_CommentPreservation tests round-trip preservation of XML comments
func TestXmlRoundTrip_CommentPreservation(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected []string
	}{
		{
			name: "single comment",
			input: `<!--This is a comment-->
<root>
  <child>text</child>
</root>
`,
			expected: []string{"<!--This is a comment-->", "<root>", "<child>text</child>"},
		},
		{
			name: "multiple comments before root",
			input: `<!--First comment-->
<!--Second comment-->
<root>
  <child>text</child>
</root>
`,
			expected: []string{"<!--First comment-->", "<!--Second comment-->"},
		},
		{
			name:     "comment before complex child element",
			input:    `<root><!--Section comment--><section><item>text</item></section></root>`,
			expected: []string{"<!--Section comment-->", "<section>"},
		},
		{
			name: "processing instruction and comments",
			input: `<?xml version="1.0" encoding="UTF-8"?>
<!--Document comment-->
<root>
  <child>text</child>
</root>
`,
			expected: []string{`<?xml version="1.0" encoding="UTF-8"?>`, "<!--Document comment-->", "<root>"},
		},
		{
			name: "nested elements and comments",
			input: `<!--Root level comment-->
<Document>
  <!--Section comment-->
  <Section>
    <Item>value1</Item>
    <Item>value2</Item>
  </Section>
</Document>
`,
			expected: []string{"<!--Root level comment-->", "<!--Section comment-->", "<Document>", "<Section>"},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			r, w := newTestReaderWriter(t)
			assertRoundTrip(t, r, w, tt.input, tt.expected)
		})
	}
}

// TestXmlRoundTrip_EdgeCases tests edge cases for comment handling
func TestXmlRoundTrip_EdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected []string
	}{
		{
			name:     "empty comment",
			input:    `<!----><root><child>text</child></root>`,
			expected: []string{"<!---->", "<root>"},
		},
		{
			name:     "whitespace-only comment",
			input:    `<!--   --><root><child>text</child></root>`,
			expected: []string{"<!--   -->"},
		},
		{
			name:     "comment between sibling elements",
			input:    `<root><first>one</first><!--between siblings--><second>two</second></root>`,
			expected: []string{"<!--between siblings-->", "<first>one</first>", "<second>two</second>"},
		},
		{
			name:     "multiple comments between siblings",
			input:    `<root><a>1</a><!--comment1--><!--comment2--><b>2</b></root>`,
			expected: []string{"<!--comment1-->", "<!--comment2-->"},
		},
		{
			name:     "trailing comment after last child",
			input:    `<root><child>text</child><!--trailing comment--></root>`,
			expected: []string{"<!--trailing comment-->", "<child>text</child>"},
		},
		{
			name:     "multiple trailing comments",
			input:    `<root><child>text</child><!--trailing1--><!--trailing2--></root>`,
			expected: []string{"<!--trailing1-->", "<!--trailing2-->"},
		},
		{
			name:     "trailing comment in nested structure",
			input:    `<root><parent><child>text</child><!--inner trailing--></parent><!--outer trailing--></root>`,
			expected: []string{"<!--inner trailing-->", "<!--outer trailing-->"},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			r, w := newTestReaderWriter(t)
			assertRoundTrip(t, r, w, tt.input, tt.expected)
		})
	}
}

// TestXmlRoundTrip_SpecialCommentContent tests comments with special but valid content
func TestXmlRoundTrip_SpecialCommentContent(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected []string
	}{
		{
			name:     "special characters",
			input:    `<!--Comment with <special> & "characters" 'here'--><root><child>text</child></root>`,
			expected: []string{"<!--Comment with <special>"},
		},
		{
			name:     "single dash",
			input:    `<!--Comment with a-single-dash--><root><child>text</child></root>`,
			expected: []string{"<!--Comment with a-single-dash-->"},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			r, w := newTestReaderWriter(t)
			assertRoundTrip(t, r, w, tt.input, tt.expected)
		})
	}
}

// TestXmlReader_SecurityLimits tests error handling for security limits
func TestXmlReader_SecurityLimits(t *testing.T) {
	t.Run("reject oversized XML input", func(t *testing.T) {
		r, err := daselxml.XML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("Unexpected error creating reader: %s", err)
		}

		largeContent := strings.Repeat("x", 10_000_001)
		input := "<root>" + largeContent + "</root>"

		_, err = r.Read([]byte(input))
		if err == nil {
			t.Errorf("Expected error for oversized XML input")
		}
		if !strings.Contains(err.Error(), "exceeds maximum size") {
			t.Errorf("Expected error about maximum size, got: %s", err)
		}
	})

	t.Run("reject oversized comment", func(t *testing.T) {
		r, err := daselxml.XML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("Unexpected error creating reader: %s", err)
		}

		largeComment := strings.Repeat("x", 10_001)
		input := "<!--" + largeComment + "--><root><child>text</child></root>"

		_, err = r.Read([]byte(input))
		if err == nil {
			t.Errorf("Expected error for oversized comment")
		}
		if !strings.Contains(err.Error(), "exceeds maximum length") {
			t.Errorf("Expected error about maximum length, got: %s", err)
		}
	})

	t.Run("reject document with too many comments", func(t *testing.T) {
		r, err := daselxml.XML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("Unexpected error creating reader: %s", err)
		}

		var builder strings.Builder
		builder.WriteString("<root>")
		for i := 0; i < 1001; i++ {
			builder.WriteString("<!--comment-->")
		}
		builder.WriteString("<child>text</child></root>")
		input := builder.String()

		_, err = r.Read([]byte(input))
		if err == nil {
			t.Errorf("Expected error for too many comments")
		}
		if !strings.Contains(err.Error(), "exceeds maximum comment count") {
			t.Errorf("Expected error about maximum comment count, got: %s", err)
		}
	})
}

// TestXmlRoundTrip_ProcessingInstructionReset tests that processing instructions are not duplicated across siblings
func TestXmlRoundTrip_ProcessingInstructionReset(t *testing.T) {
	t.Run("processing instructions not duplicated to siblings", func(t *testing.T) {
		r, w := newTestReaderWriter(t)

		input := `<?xml version="1.0"?><root><first>one</first><second>two</second></root>`

		data, err := r.Read([]byte(input))
		if err != nil {
			t.Fatalf("Unexpected error reading XML: %s", err)
		}

		output, err := w.Write(data)
		if err != nil {
			t.Fatalf("Unexpected error writing XML: %s", err)
		}

		outputStr := string(output)

		piCount := strings.Count(outputStr, `<?xml version="1.0"?>`)
		if piCount != 1 {
			t.Errorf("Expected PI to appear exactly once, but found %d occurrences in:\n%s", piCount, outputStr)
		}

		if !strings.Contains(outputStr, "<first>one</first>") {
			t.Errorf("Expected first element to be preserved in:\n%s", outputStr)
		}
		if !strings.Contains(outputStr, "<second>two</second>") {
			t.Errorf("Expected second element to be preserved in:\n%s", outputStr)
		}
	})

	t.Run("sibling elements do not inherit each others processing instructions", func(t *testing.T) {
		options := parsing.DefaultReaderOptions()
		options.Ext = map[string]string{"xml-mode": "structured"}
		r, err := daselxml.XML.NewReader(options)
		if err != nil {
			t.Fatalf("Unexpected error creating reader: %s", err)
		}

		input := `<root><?target instruction?><first>one</first><second>two</second></root>`

		data, err := r.Read([]byte(input))
		if err != nil {
			t.Fatalf("Unexpected error reading XML: %s", err)
		}

		children, err := data.GetMapKey("children")
		if err != nil {
			t.Fatalf("Expected children key: %s", err)
		}

		childLen, _ := children.SliceLen()
		if childLen < 1 {
			t.Fatalf("Expected at least one child")
		}

		rootEl, err := children.GetSliceIndex(0)
		if err != nil {
			t.Fatalf("Expected to get root element: %s", err)
		}

		rootChildren, err := rootEl.GetMapKey("children")
		if err != nil {
			t.Fatalf("Expected root children: %s", err)
		}

		rootChildLen, _ := rootChildren.SliceLen()
		if rootChildLen < 2 {
			t.Fatalf("Expected at least two children in root, got %d", rootChildLen)
		}

		firstChild, _ := rootChildren.GetSliceIndex(0)
		_, hasPI := firstChild.MetadataValue("xml_processing_instructions")
		if !hasPI {
			t.Log("First child does not have PI (which is expected behavior after fix)")
		}

		secondChild, _ := rootChildren.GetSliceIndex(1)
		_, secondHasPI := secondChild.MetadataValue("xml_processing_instructions")
		if secondHasPI {
			t.Errorf("Second child should NOT have processing instructions (PI was incorrectly duplicated)")
		}
	})
}

// TestXmlRoundTrip_ProcessingInstructions tests round-trip preservation of processing instructions
func TestXmlRoundTrip_ProcessingInstructions(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected []string
	}{
		{
			name: "xml declaration",
			input: `<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<root>
  <child>text</child>
</root>
`,
			expected: []string{`<?xml version="1.0" encoding="utf-8" standalone="yes"?>`},
		},
		{
			name: "multiple processing instructions",
			input: `<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="style.xsl"?>
<root>
  <child>text</child>
</root>
`,
			expected: []string{`<?xml version="1.0" encoding="UTF-8"?>`, `<?xml-stylesheet type="text/xsl" href="style.xsl"?>`},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			r, w := newTestReaderWriter(t)
			assertRoundTrip(t, r, w, tt.input, tt.expected)
		})
	}
}
```

## File: `parsing/xml/writer.go`
```go
package xml

import (
	"bytes"
	"encoding/xml"
	"fmt"
	"strings"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
)

func newXMLWriter(options parsing.WriterOptions) (parsing.Writer, error) {
	return &xmlWriter{
		options: options,
	}, nil
}

type xmlWriter struct {
	options parsing.WriterOptions
}

// Write writes a value to a byte slice.
func (j *xmlWriter) Write(value *model.Value) ([]byte, error) {
	buf := new(bytes.Buffer)
	writer := xml.NewEncoder(buf)
	defer func() {
		_ = writer.Close()
	}()
	writer.Indent("", "  ")

	element, err := j.toElement("root", value)
	if err != nil {
		return nil, fmt.Errorf("failed to convert to element: %w", err)
	}
	for _, c := range element.Children {
		if err := writer.Encode(c); err != nil {
			return nil, err
		}
		if err := writer.EncodeToken(xml.CharData("\n")); err != nil {
			return nil, err
		}
	}

	if err := writer.Flush(); err != nil {
		return nil, err
	}
	outBytes := buf.Bytes()
	if !bytes.HasSuffix(outBytes, []byte("\n")) {
		outBytes = append(outBytes, '\n')
	}
	return outBytes, nil
}

func (j *xmlWriter) toElement(key string, value *model.Value) (*xmlElement, error) {
	readProcessingInstructions := func() []*xmlProcessingInstruction {
		if piMeta, ok := value.MetadataValue("xml_processing_instructions"); ok && piMeta != nil {
			if pis, ok := piMeta.([]*xmlProcessingInstruction); ok {
				return pis
			}
		}
		return nil
	}
	readComments := func() []*xmlComment {
		if commentMeta, ok := value.MetadataValue("xml_comments"); ok && commentMeta != nil {
			if comments, ok := commentMeta.([]*xmlComment); ok {
				return comments
			}
		}
		return nil
	}
	switch value.Type() {

	case model.TypeString:
		strVal, err := valueToString(value)
		return &xmlElement{
			Name:                   key,
			Content:                strVal,
			ProcessingInstructions: readProcessingInstructions(),
			Comments:               readComments(),
		}, err

	case model.TypeMap:
		kvs, err := value.MapKeyValues()
		if err != nil {
			return nil, err
		}

		el := &xmlElement{
			Name:                   key,
			ProcessingInstructions: readProcessingInstructions(),
			Comments:               readComments(),
		}

		for _, kv := range kvs {
			if strings.HasPrefix(kv.Key, "-") {
				attr := xmlAttr{
					Name: kv.Key[1:],
				}
				attr.Value, err = valueToString(kv.Value)
				if err != nil {
					return nil, fmt.Errorf("failed to convert attribute %q to string: %w", attr.Name, err)
				}
				el.Attrs = append(el.Attrs, attr)
				continue
			}

			if kv.Key == "#text" {
				el.Content, err = valueToString(kv.Value)
				if err != nil {
					return nil, fmt.Errorf("failed to convert content to string: %w", err)
				}
				continue
			}

			childEl, err := j.toElement(kv.Key, kv.Value)
			if err != nil {
				return nil, fmt.Errorf("failed to convert child element %q to element: %w", kv.Key, err)
			}
			if childEl.useChildrenOnly {
				el.Children = append(el.Children, childEl.Children...)
			} else {
				el.Children = append(el.Children, childEl)
			}
		}

		return el, nil
	case model.TypeSlice:
		el := &xmlElement{
			Name:                   "root",
			ProcessingInstructions: readProcessingInstructions(),
			Comments:               readComments(),
			useChildrenOnly:        true,
		}
		if err := value.RangeSlice(func(i int, value *model.Value) error {
			childEl, err := j.toElement(key, value)
			if err != nil {
				return err
			}
			if childEl.useChildrenOnly {
				el.Children = append(el.Children, childEl.Children...)
			} else {
				el.Children = append(el.Children, childEl)
			}

			return nil
		}); err != nil {
			return nil, err
		}
		return el, nil
	default:
		return nil, fmt.Errorf("xml writer does not support value type: %s", value.Type())
	}
}

func valueToString(v *model.Value) (string, error) {
	if v.IsNull() {
		return "", nil
	}

	switch v.Type() {
	case model.TypeString:
		stringValue, err := v.StringValue()
		if err != nil {
			return "", err
		}
		return stringValue, nil
	case model.TypeInt:
		i, err := v.IntValue()
		if err != nil {
			return "", err
		}
		return fmt.Sprintf("%d", i), nil
	case model.TypeFloat:
		i, err := v.FloatValue()
		if err != nil {
			return "", err
		}
		return fmt.Sprintf("%g", i), nil
	case model.TypeBool:
		i, err := v.BoolValue()
		if err != nil {
			return "", err
		}
		return fmt.Sprintf("%t", i), nil
	default:
		return "", fmt.Errorf("xml writer cannot format type %s to string", v.Type())
	}
}

// indentString returns the indentation for a given depth level.
func indentString(depth int) string {
	return strings.Repeat("  ", depth)
}

func (e *xmlElement) MarshalXML(enc *xml.Encoder, start xml.StartElement) error {
	// Write processing instructions before the element (document-level)
	if len(e.ProcessingInstructions) > 0 {
		for _, pi := range e.ProcessingInstructions {
			if err := enc.EncodeToken(xml.ProcInst{
				Target: pi.Target,
				Inst:   []byte(pi.Value),
			}); err != nil {
				return err
			}
			if err := enc.EncodeToken(xml.CharData("\n")); err != nil {
				return err
			}
		}
	}
	// Write comments before the element (document-level comments only)
	// Child-level comments are written by the parent inside its body
	if e.depth == 0 && len(e.Comments) > 0 {
		for _, comment := range e.Comments {
			if strings.Contains(comment.Text, "--") {
				return fmt.Errorf("comment text cannot contain '--' sequence (invalid XML comment)")
			}
			if err := enc.EncodeToken(xml.Comment(comment.Text)); err != nil {
				return fmt.Errorf("failed to encode comment: %w", err)
			}
			if err := enc.EncodeToken(xml.CharData("\n")); err != nil {
				return err
			}
		}
	}
	start.Name = xml.Name{Local: e.Name}

	if len(e.Attrs) > 0 {
		for _, attr := range e.Attrs {
			start.Attr = append(start.Attr, xml.Attr{
				Name:  xml.Name{Local: attr.Name},
				Value: attr.Value,
			})
		}
	}

	if err := enc.EncodeToken(start); err != nil {
		return err
	}

	// TODO : Handle CDATA sections on write.

	if len(e.Content) > 0 {
		if err := enc.EncodeToken(xml.CharData(e.Content)); err != nil {
			return err
		}
	}

	// Write children with their preceding comments
	childDepth := e.depth + 1
	for _, child := range e.Children {
		// Write child's comments inside parent, before the child element
		if len(child.Comments) > 0 {
			for _, comment := range child.Comments {
				if strings.Contains(comment.Text, "--") {
					return fmt.Errorf("comment text cannot contain '--' sequence (invalid XML comment)")
				}
				// Add newline + indentation before comment
				if err := enc.EncodeToken(xml.CharData("\n" + indentString(childDepth))); err != nil {
					return err
				}
				if err := enc.EncodeToken(xml.Comment(comment.Text)); err != nil {
					return fmt.Errorf("failed to encode comment: %w", err)
				}
			}
			// Clear comments so child doesn't write them again
			child.Comments = nil
		}
		// Set child depth for recursive calls
		child.depth = childDepth
		if err := enc.Encode(child); err != nil {
			return err
		}
	}

	return enc.EncodeToken(start.End())
}
```

## File: `parsing/xml/writer_internal_test.go`
```go
package xml

import (
	"strings"
	"testing"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
)

// TestXmlWriter_CommentValidation tests validation of comment content during write
func TestXmlWriter_CommentValidation(t *testing.T) {
	t.Run("reject comment containing double dash sequence", func(t *testing.T) {
		w, err := newXMLWriter(parsing.DefaultWriterOptions())
		if err != nil {
			t.Fatalf("Unexpected error creating writer: %s", err)
		}

		// Create a child value with an invalid comment containing -- sequence
		// The comments are attached to child elements, not the root
		childValue := model.NewMapValue()
		childValue.SetMetadataValue("xml_comments", []*xmlComment{{Text: "invalid--comment"}})
		if err := childValue.SetMapKey("item", model.NewStringValue("text")); err != nil {
			t.Fatalf("Unexpected error setting map key: %s", err)
		}

		// Create root value containing the child
		rootValue := model.NewMapValue()
		if err := rootValue.SetMapKey("child", childValue); err != nil {
			t.Fatalf("Unexpected error setting map key: %s", err)
		}

		_, err = w.Write(rootValue)
		if err == nil {
			t.Errorf("Expected error for comment containing double dash")
		}
		if err != nil && !strings.Contains(err.Error(), "cannot contain '--'") {
			t.Errorf("Expected error about double dash sequence, got: %s", err)
		}
	})

	t.Run("accept valid comment without double dash", func(t *testing.T) {
		w, err := newXMLWriter(parsing.DefaultWriterOptions())
		if err != nil {
			t.Fatalf("Unexpected error creating writer: %s", err)
		}

		// Create a child value with a valid comment
		childValue := model.NewMapValue()
		childValue.SetMetadataValue("xml_comments", []*xmlComment{{Text: "valid comment with single - dash"}})
		if err := childValue.SetMapKey("item", model.NewStringValue("text")); err != nil {
			t.Fatalf("Unexpected error setting map key: %s", err)
		}

		// Create root value containing the child
		rootValue := model.NewMapValue()
		if err := rootValue.SetMapKey("child", childValue); err != nil {
			t.Fatalf("Unexpected error setting map key: %s", err)
		}

		output, err := w.Write(rootValue)
		if err != nil {
			t.Fatalf("Unexpected error writing XML: %s", err)
		}

		outputStr := string(output)
		if !strings.Contains(outputStr, "<!--valid comment with single - dash-->") {
			t.Errorf("Expected output to contain valid comment, got:\n%s", outputStr)
		}
	})
}

// Test_valueToString tests the valueToString function for all supported types
func Test_valueToString(t *testing.T) {
	t.Run("null value returns empty string", func(t *testing.T) {
		v := model.NewNullValue()
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for null value: %s", err)
		}
		if result != "" {
			t.Errorf("Expected empty string for null value, got: %q", result)
		}
	})

	t.Run("string value", func(t *testing.T) {
		v := model.NewStringValue("hello world")
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for string value: %s", err)
		}
		if result != "hello world" {
			t.Errorf("Expected 'hello world', got: %q", result)
		}
	})

	t.Run("empty string value", func(t *testing.T) {
		v := model.NewStringValue("")
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for empty string value: %s", err)
		}
		if result != "" {
			t.Errorf("Expected empty string, got: %q", result)
		}
	})

	t.Run("int value positive", func(t *testing.T) {
		v := model.NewIntValue(42)
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for int value: %s", err)
		}
		if result != "42" {
			t.Errorf("Expected '42', got: %q", result)
		}
	})

	t.Run("int value negative", func(t *testing.T) {
		v := model.NewIntValue(-123)
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for negative int value: %s", err)
		}
		if result != "-123" {
			t.Errorf("Expected '-123', got: %q", result)
		}
	})

	t.Run("int value zero", func(t *testing.T) {
		v := model.NewIntValue(0)
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for zero int value: %s", err)
		}
		if result != "0" {
			t.Errorf("Expected '0', got: %q", result)
		}
	})

	t.Run("float value", func(t *testing.T) {
		v := model.NewFloatValue(3.14159)
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for float value: %s", err)
		}
		if result != "3.14159" {
			t.Errorf("Expected '3.14159', got: %q", result)
		}
	})

	t.Run("float value negative", func(t *testing.T) {
		v := model.NewFloatValue(-2.5)
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for negative float value: %s", err)
		}
		if result != "-2.5" {
			t.Errorf("Expected '-2.5', got: %q", result)
		}
	})

	t.Run("float value zero", func(t *testing.T) {
		v := model.NewFloatValue(0.0)
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for zero float value: %s", err)
		}
		if result != "0" {
			t.Errorf("Expected '0', got: %q", result)
		}
	})

	t.Run("bool value true", func(t *testing.T) {
		v := model.NewBoolValue(true)
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for bool true value: %s", err)
		}
		if result != "true" {
			t.Errorf("Expected 'true', got: %q", result)
		}
	})

	t.Run("bool value false", func(t *testing.T) {
		v := model.NewBoolValue(false)
		result, err := valueToString(v)
		if err != nil {
			t.Errorf("Unexpected error for bool false value: %s", err)
		}
		if result != "false" {
			t.Errorf("Expected 'false', got: %q", result)
		}
	})

	t.Run("map value returns error", func(t *testing.T) {
		v := model.NewMapValue()
		_, err := valueToString(v)
		if err == nil {
			t.Errorf("Expected error for map value")
		}
		if err != nil && !strings.Contains(err.Error(), "cannot format type") {
			t.Errorf("Expected error about formatting type, got: %s", err)
		}
	})

	t.Run("slice value returns error", func(t *testing.T) {
		v := model.NewSliceValue()
		_, err := valueToString(v)
		if err == nil {
			t.Errorf("Expected error for slice value")
		}
		if err != nil && !strings.Contains(err.Error(), "cannot format type") {
			t.Errorf("Expected error about formatting type, got: %s", err)
		}
	})
}
```

## File: `parsing/xml/writer_test.go`
```go
package xml_test

import (
	"github.com/tomwright/dasel/v3/model"
	"testing"

	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/xml"
)

func TestXmlReader_Write(t *testing.T) {
	t.Run("nested xml elements", func(t *testing.T) {
		r, err := xml.XML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		w, err := xml.XML.NewWriter(parsing.DefaultWriterOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		data, err := r.Read([]byte(`<Document>
  <Sender>Ivanov</Sender>
  <In_N_Document>
    <N_Document>1024</N_Document>
    <Date_Reg>2024-06-21T15:07:29.0451517+03:00</Date_Reg>
  </In_N_Document>
  <Out_N_Document>
    <N_Document>2043</N_Document>
    <Date_Reg>2024-05-01T00:00:00</Date_Reg>
  </Out_N_Document>
  <Content>Skzzkz</Content>
  <DSP>true</DSP>
</Document>
`))
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		xmlBytes, err := w.Write(data)
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		expected := `<Document>
  <Sender>Ivanov</Sender>
  <In_N_Document>
    <N_Document>1024</N_Document>
    <Date_Reg>2024-06-21T15:07:29.0451517+03:00</Date_Reg>
  </In_N_Document>
  <Out_N_Document>
    <N_Document>2043</N_Document>
    <Date_Reg>2024-05-01T00:00:00</Date_Reg>
  </Out_N_Document>
  <Content>Skzzkz</Content>
  <DSP>true</DSP>
</Document>
`
		if string(xmlBytes) != expected {
			t.Fatalf("Expected:\n%s\nGot:\n%s", expected, string(xmlBytes))
		}
	})

	t.Run("nested xml elements with processing instruction", func(t *testing.T) {
		r, err := xml.XML.NewReader(parsing.DefaultReaderOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		w, err := xml.XML.NewWriter(parsing.DefaultWriterOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		data, err := r.Read([]byte(`<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<Document>
  <Sender>Ivanov</Sender>
  <In_N_Document>
    <N_Document>1024</N_Document>
    <Date_Reg>2024-06-21T15:07:29.0451517+03:00</Date_Reg>
  </In_N_Document>
  <Out_N_Document>
    <N_Document>2043</N_Document>
    <Date_Reg>2024-05-01T00:00:00</Date_Reg>
  </Out_N_Document>
  <Content>Skzzkz</Content>
  <DSP>true</DSP>
</Document>
`))
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		doc, err := data.GetMapKey("Document")
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}
		docProcessingInstructions, ok := doc.MetadataValue("xml_processing_instructions")
		if !ok || docProcessingInstructions == nil {
			t.Fatalf("Expected processing instructions on Document element")
		}

		jsonBytes, err := w.Write(data)
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		expected := `<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<Document>
  <Sender>Ivanov</Sender>
  <In_N_Document>
    <N_Document>1024</N_Document>
    <Date_Reg>2024-06-21T15:07:29.0451517+03:00</Date_Reg>
  </In_N_Document>
  <Out_N_Document>
    <N_Document>2043</N_Document>
    <Date_Reg>2024-05-01T00:00:00</Date_Reg>
  </Out_N_Document>
  <Content>Skzzkz</Content>
  <DSP>true</DSP>
</Document>
`
		if string(jsonBytes) != expected {
			t.Fatalf("Expected:\n%s\nGot:\n%s", expected, string(jsonBytes))
		}
	})

	t.Run("encode attributes", func(t *testing.T) {
		w, err := xml.XML.NewWriter(parsing.DefaultWriterOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}

		toEncode := model.NewMapValue()
		foo := model.NewMapValue()
		_ = foo.SetMapKey("-fiz", model.NewStringValue("hello"))
		_ = foo.SetMapKey("bar", model.NewStringValue(""))
		_ = toEncode.SetMapKey("foo", foo)

		got, err := w.Write(toEncode)
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}
		exp := []byte(`<foo fiz="hello">
  <bar></bar>
</foo>
`)
		if string(got) != string(exp) {
			t.Errorf("Expected:\n%s\nGot:\n%s", string(exp), string(got))
		}
	})

	t.Run("encode cdata", func(t *testing.T) {
		w, err := xml.XML.NewWriter(parsing.DefaultWriterOptions())
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}
		toEncode := model.NewMapValue()
		_ = toEncode.SetMapKey("foo", model.NewStringValue("<bar>baz</bar>"))
		got, err := w.Write(toEncode)
		if err != nil {
			t.Fatalf("Unexpected error: %s", err)
		}
		// TODO : Change this to use CDATA sections rather than escaping.
		exp := []byte(`<foo>&lt;bar&gt;baz&lt;/bar&gt;</foo>
`)
		if string(got) != string(exp) {
			t.Errorf("Expected:\n%s\nGot:\n%s", string(exp), string(got))
		}
	})
}
```

## File: `parsing/xml/xml.go`
```go
package xml

import (
	"github.com/tomwright/dasel/v3/parsing"
)

const (
	// XML represents the XML file format.
	XML parsing.Format = "xml"
)

var _ parsing.Reader = (*xmlReader)(nil)
var _ parsing.Writer = (*xmlWriter)(nil)

func init() {
	parsing.RegisterReader(XML, newXMLReader)
	parsing.RegisterWriter(XML, newXMLWriter)
}

type xmlAttr struct {
	Name  string
	Value string
}

type xmlProcessingInstruction struct {
	Target string
	Value  string
}

type xmlComment struct {
	Text string
}

type xmlElement struct {
	Name                   string
	Attrs                  []xmlAttr
	Children               []*xmlElement
	Content                string
	ProcessingInstructions []*xmlProcessingInstruction
	Comments               []*xmlComment
	useChildrenOnly        bool
	depth                  int // Tracks nesting depth for proper indentation
}
```

## File: `parsing/yaml/yaml.go`
```go
package yaml

import (
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"go.yaml.in/yaml/v4"
)

// YAML represents the YAML file format.
const YAML parsing.Format = "yaml"

func init() {
	parsing.RegisterReader(YAML, newYAMLReader)
	parsing.RegisterWriter(YAML, newYAMLWriter)
}

type yamlValue struct {
	node  *yaml.Node
	value *model.Value
}
```

## File: `parsing/yaml/yaml_reader.go`
```go
package yaml

import (
	"bytes"
	"fmt"
	"io"
	"strconv"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"go.yaml.in/yaml/v4"
)

var _ parsing.Reader = (*yamlReader)(nil)

func newYAMLReader(options parsing.ReaderOptions) (parsing.Reader, error) {
	return &yamlReader{}, nil
}

type yamlReader struct{}

// Read reads a value from a byte slice.
func (j *yamlReader) Read(data []byte) (*model.Value, error) {
	d := yaml.NewDecoder(bytes.NewReader(data))
	res := make([]*yamlValue, 0)
	for {
		unmarshalled := &yamlValue{}
		if err := d.Decode(&unmarshalled); err != nil {
			if err == io.EOF {
				break
			}
			return nil, err
		}
		if unmarshalled == nil {
			unmarshalled = &yamlValue{
				node:  nil,
				value: model.NewNullValue(),
			}
		}
		res = append(res, unmarshalled)
	}

	switch len(res) {
	case 0:
		return model.NewNullValue(), nil
	case 1:
		return res[0].value, nil
	default:
		slice := model.NewSliceValue()
		slice.MarkAsBranch()
		for _, v := range res {
			if v == nil {
				continue
			}
			if err := slice.Append(v.value); err != nil {
				return nil, err
			}
		}
		return slice, nil
	}
}

func (yv *yamlValue) UnmarshalYAML(value *yaml.Node) error {
	yv.node = value
	switch value.Kind {
	case yaml.ScalarNode:
		switch value.Tag {
		case "!!bool":
			yv.value = model.NewBoolValue(value.Value == "true")
		case "!!int":
			i, err := strconv.Atoi(value.Value)
			if err != nil {
				return err
			}
			yv.value = model.NewIntValue(int64(i))
		case "!!float":
			f, err := strconv.ParseFloat(value.Value, 64)
			if err != nil {
				return err
			}
			yv.value = model.NewFloatValue(f)
		case "!!null":
			yv.value = model.NewNullValue()
		case "!!str":
			yv.value = model.NewStringValue(value.Value)
		default:
			yv.value = model.NewStringValue(value.Value)
		}
	case yaml.DocumentNode:
		yv.value = model.NewNullValue()
	case yaml.SequenceNode:
		res := model.NewSliceValue()
		for _, item := range value.Content {
			newItem := &yamlValue{}
			if err := newItem.UnmarshalYAML(item); err != nil {
				return err
			}
			if err := res.Append(newItem.value); err != nil {
				return err
			}
		}
		yv.value = res
	case yaml.MappingNode:
		res := model.NewMapValue()
		for i := 0; i < len(value.Content); i += 2 {
			key := value.Content[i]
			val := value.Content[i+1]

			newKey := &yamlValue{}
			if err := newKey.UnmarshalYAML(key); err != nil {
				return err
			}

			newVal := &yamlValue{}
			if err := newVal.UnmarshalYAML(val); err != nil {
				return err
			}

			keyStr, err := newKey.value.StringValue()
			if err != nil {
				return fmt.Errorf("keys are expected to be strings: %w", err)
			}

			if err := res.SetMapKey(keyStr, newVal.value); err != nil {
				return err
			}
		}
		yv.value = res
	case yaml.AliasNode:
		newVal := &yamlValue{}
		if err := newVal.UnmarshalYAML(value.Alias); err != nil {
			return err
		}
		yv.value = newVal.value
		yv.value.SetMetadataValue("yaml-alias", value.Value)
	}
	return nil
}
```

## File: `parsing/yaml/yaml_test.go`
```go
package yaml_test

import (
	"bytes"
	"testing"

	"github.com/google/go-cmp/cmp"
	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"github.com/tomwright/dasel/v3/parsing/yaml"
)

type testCase struct {
	in     string
	assert func(t *testing.T, res *model.Value)
}

func (tc testCase) run(t *testing.T) {
	r, err := yaml.YAML.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error: %s", err)
	}
	res, err := r.Read([]byte(tc.in))
	if err != nil {
		t.Fatalf("unexpected error: %s", err)
	}

	tc.assert(t, res)
}

type rwTestCase struct {
	in  string
	out string
}

func (tc rwTestCase) run(t *testing.T) {
	if tc.out == "" {
		tc.out = tc.in
	}
	r, err := yaml.YAML.NewReader(parsing.DefaultReaderOptions())
	if err != nil {
		t.Fatalf("unexpected error: %s", err)
	}
	w, err := yaml.YAML.NewWriter(parsing.WriterOptions{})
	if err != nil {
		t.Fatalf("unexpected error: %s", err)
	}
	res, err := r.Read([]byte(tc.in))
	if err != nil {
		t.Fatalf("unexpected error: %s", err)
	}
	out, err := w.Write(res)
	if err != nil {
		t.Fatalf("unexpected error: %s", err)
	}

	if !bytes.Equal([]byte(tc.out), out) {
		t.Errorf("unexpected output: %s", cmp.Diff(tc.out, string(out)))
	}
}

func TestYamlValue_UnmarshalYAML(t *testing.T) {
	t.Run("simple key value", testCase{
		in: `name: Tom`,
		assert: func(t *testing.T, res *model.Value) {
			got, err := res.GetMapKey("name")
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}

			gotStr, err := got.StringValue()
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}

			if gotStr != "Tom" {
				t.Errorf("unexpected value: %s", gotStr)
			}
		},
	}.run)

	t.Run("multi document", testCase{
		in: `name: Tom
---
name: Jerry`,
		assert: func(t *testing.T, res *model.Value) {
			a, err := res.GetSliceIndex(0)
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			got, err := a.GetMapKey("name")
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			gotStr, err := got.StringValue()
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if gotStr != "Tom" {
				t.Errorf("unexpected value: %s", gotStr)
			}

			b, err := res.GetSliceIndex(1)
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			got, err = b.GetMapKey("name")
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			gotStr, err = got.StringValue()
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if gotStr != "Jerry" {
				t.Errorf("unexpected value: %s", gotStr)
			}
		},
	}.run)

	t.Run("multi document", testCase{
		in: `name: Tom
---
name: Jerry`,
		assert: func(t *testing.T, res *model.Value) {
			a, err := res.GetSliceIndex(0)
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			got, err := a.GetMapKey("name")
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			gotStr, err := got.StringValue()
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if gotStr != "Tom" {
				t.Errorf("unexpected value: %s", gotStr)
			}

			b, err := res.GetSliceIndex(1)
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			got, err = b.GetMapKey("name")
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			gotStr, err = got.StringValue()
			if err != nil {
				t.Fatalf("unexpected error: %s", err)
			}
			if gotStr != "Jerry" {
				t.Errorf("unexpected value: %s", gotStr)
			}
		},
	}.run)

	t.Run("multi document", rwTestCase{
		in: `name: Tom
---
name: Jerry
`,
	}.run)

	t.Run("generic", rwTestCase{
		in: `str: foo
int: 1
float: 1.1
bool: true
map:
    key: value
list:
    - item1
    - item2
`,
	}.run)

	// This test is technically wrong because we're only supporting the alias on read and not write.
	t.Run("alias", rwTestCase{
		in: `name: &name Tom
name2: *name
`,
		out: `name: Tom
name2: Tom
`,
	}.run)

	t.Run("null read write", rwTestCase{
		in: `name: null
`,
		out: `name: null
`,
	}.run)

	t.Run("null document read write", rwTestCase{
		in: `null
`,
		out: `null
`,
	}.run)
}
```

## File: `parsing/yaml/yaml_writer.go`
```go
package yaml

import (
	"fmt"

	"github.com/tomwright/dasel/v3/model"
	"github.com/tomwright/dasel/v3/parsing"
	"go.yaml.in/yaml/v4"
)

var _ parsing.Writer = (*yamlWriter)(nil)

func newYAMLWriter(options parsing.WriterOptions) (parsing.Writer, error) {
	return &yamlWriter{}, nil
}

type yamlWriter struct{}

func (j *yamlWriter) Separator() []byte {
	return []byte("---\n")
}

// Write writes a value to a byte slice.
func (j *yamlWriter) Write(value *model.Value) ([]byte, error) {
	yv := &yamlValue{value: value}
	res, err := yv.ToNode()
	if err != nil {
		return nil, err
	}
	return yaml.Marshal(res)
}

func (yv *yamlValue) ToNode() (*yaml.Node, error) {
	res := &yaml.Node{}

	// TODO : Handle yaml aliases.
	//yamlAlias, ok := yv.value.Metadata["yaml-alias"].(string)
	//if ok {
	//res.Kind = yaml.AliasNode
	//res.Value = yamlAlias
	//return res, nil
	//}

	switch yv.value.Type() {
	case model.TypeString:
		v, err := yv.value.StringValue()
		if err != nil {
			return nil, err
		}
		res.Kind = yaml.ScalarNode
		res.Value = v
		res.Tag = "!!str"
	case model.TypeBool:
		v, err := yv.value.BoolValue()
		if err != nil {
			return nil, err
		}
		res.Kind = yaml.ScalarNode
		res.Value = fmt.Sprintf("%t", v)
		res.Tag = "!!bool"
	case model.TypeInt:
		v, err := yv.value.IntValue()
		if err != nil {
			return nil, err
		}
		res.Kind = yaml.ScalarNode
		res.Value = fmt.Sprintf("%d", v)
		res.Tag = "!!int"
	case model.TypeFloat:
		v, err := yv.value.FloatValue()
		if err != nil {
			return nil, err
		}
		res.Kind = yaml.ScalarNode
		res.Value = fmt.Sprintf("%g", v)
		res.Tag = "!!float"
	case model.TypeMap:
		res.Kind = yaml.MappingNode
		if err := yv.value.RangeMap(func(key string, val *model.Value) error {
			keyNode := &yamlValue{value: model.NewStringValue(key)}
			valNode := &yamlValue{value: val}

			marshalledKey, err := keyNode.ToNode()
			if err != nil {
				return err
			}
			marshalledVal, err := valNode.ToNode()
			if err != nil {
				return err
			}

			res.Content = append(res.Content, marshalledKey)
			res.Content = append(res.Content, marshalledVal)

			return nil
		}); err != nil {
			return nil, err
		}
	case model.TypeSlice:
		res.Kind = yaml.SequenceNode
		if err := yv.value.RangeSlice(func(i int, val *model.Value) error {
			valNode := &yamlValue{value: val}
			marshalledVal, err := valNode.ToNode()
			if err != nil {
				return err
			}
			res.Content = append(res.Content, marshalledVal)
			return nil
		}); err != nil {
			return nil, err
		}
	case model.TypeNull:
		res.Kind = yaml.ScalarNode
		res.Value = "null"
		res.Tag = "!!null"
	case model.TypeUnknown:
		return nil, fmt.Errorf("unknown type: %s", yv.value.Type())
	}

	return res, nil
}

func (yv *yamlValue) MarshalYAML() (any, error) {
	res, err := yv.ToNode()
	if err != nil {
		return nil, err
	}
	return res, nil
}
```

## File: `selector/parser.go`
```go
package selector

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
	"github.com/tomwright/dasel/v3/selector/parser"
)

func Parse(selector string) (ast.Expr, error) {
	tokens, err := lexer.NewTokenizer(selector).Tokenize()
	if err != nil {
		return nil, err
	}

	return parser.NewParser(tokens).Parse()
}
```

## File: `selector/README.md`
```markdown
# Selector

The selector package contains everything needed to parse a selector string into an AST, which we can then execute.
```

## File: `selector/ast/ast.go`
```go
package ast

type Program struct {
	Statements []Statement
}

type Statement struct {
	Expressions Expr
}

type Expressions []Expr

type Expr interface {
	expr()
}

func IsType[T Expr](e Expr) bool {
	_, ok := AsType[T](e)
	return ok
}

func AsType[T Expr](e Expr) (T, bool) {
	v, ok := e.(T)
	return v, ok
}

func LastAsType[T Expr](e Expr) (T, bool) {
	return AsType[T](Last(e))
}

func Last(e Expr) Expr {
	if v, ok := e.(ChainedExpr); ok {
		return v.Exprs[len(v.Exprs)-1]
	}
	return e
}

func RemoveLast(e Expr) Expr {
	var res Expressions
	if v, ok := e.(ChainedExpr); ok {
		res = v.Exprs[0 : len(v.Exprs)-1]
	}
	return ChainExprs(res...)
}
```

## File: `selector/ast/ast_test.go`
```go
package ast

import "testing"

// TestExpr_expr tests the expr method of all the types in the ast package.
// Note that this doesn't actually do anything and is just forcing test coverage.
// The expr func only exists for type safety with the Expr interface.
func TestExpr_expr(t *testing.T) {
	NumberFloatExpr{}.expr()
	NumberIntExpr{}.expr()
	StringExpr{}.expr()
	BoolExpr{}.expr()
	BinaryExpr{}.expr()
	UnaryExpr{}.expr()
	CallExpr{}.expr()
	ChainedExpr{}.expr()
	SpreadExpr{}.expr()
	RangeExpr{}.expr()
	IndexExpr{}.expr()
	ArrayExpr{}.expr()
	PropertyExpr{}.expr()
	ObjectExpr{}.expr()
	MapExpr{}.expr()
	EachExpr{}.expr()
	VariableExpr{}.expr()
	GroupExpr{}.expr()
	ConditionalExpr{}.expr()
	BranchExpr{}.expr()
}
```

## File: `selector/ast/expression_complex.go`
```go
package ast

import "github.com/tomwright/dasel/v3/selector/lexer"

type BinaryExpr struct {
	Left     Expr
	Operator lexer.Token
	Right    Expr
}

func (BinaryExpr) expr() {}

type UnaryExpr struct {
	Operator lexer.Token
	Right    Expr
}

func (UnaryExpr) expr() {}

type CallExpr struct {
	Function string
	Args     Expressions
}

func (CallExpr) expr() {}

type ChainedExpr struct {
	Exprs Expressions
}

func ChainExprs(exprs ...Expr) Expr {
	if len(exprs) == 0 {
		return nil
	}
	if len(exprs) == 1 {
		return exprs[0]
	}
	return ChainedExpr{
		Exprs: exprs,
	}
}

func (ChainedExpr) expr() {}

type SpreadExpr struct{}

func (SpreadExpr) expr() {}

type RangeExpr struct {
	Start Expr
	End   Expr
}

func (RangeExpr) expr() {}

type IndexExpr struct {
	Index Expr
}

func (IndexExpr) expr() {}

type ArrayExpr struct {
	Exprs Expressions
}

func (ArrayExpr) expr() {}

type PropertyExpr struct {
	// Property can resolve to a string or number.
	// If it resolves to a number, we expect to be reading from an array.
	// If it resolves to a string, we expect to be reading from a map.
	Property Expr
}

func (PropertyExpr) expr() {}

type KeyValue struct {
	Key   Expr
	Value Expr
}

type ObjectExpr struct {
	Pairs []KeyValue
}

func (ObjectExpr) expr() {}

type MapExpr struct {
	Expr Expr
}

func (MapExpr) expr() {}

type EachExpr struct {
	Expr Expr
}

func (EachExpr) expr() {}

type FilterExpr struct {
	Expr Expr
}

func (FilterExpr) expr() {}

type SearchExpr struct {
	Expr Expr
}

func (SearchExpr) expr() {}

type RecursiveDescentExpr struct {
	IsWildcard bool
	Expr       Expr
}

func (RecursiveDescentExpr) expr() {}

type SortByExpr struct {
	Expr       Expr
	Descending bool
}

func (SortByExpr) expr() {}

type VariableExpr struct {
	Name string
}

func (VariableExpr) expr() {}

type GroupExpr struct {
	Expr Expr
}

func (GroupExpr) expr() {}

type ConditionalExpr struct {
	Cond Expr
	Then Expr
	Else Expr
}

func (ConditionalExpr) expr() {}

type BranchExpr struct {
	Exprs []Expr
}

func (BranchExpr) expr() {}

func BranchExprs(exprs ...Expr) Expr {
	return BranchExpr{
		Exprs: exprs,
	}
}

type AssignExpr struct {
	Variable VariableExpr
	Value    Expr
}

func (AssignExpr) expr() {}
```

## File: `selector/ast/expression_literal.go`
```go
package ast

import "regexp"

type NumberFloatExpr struct {
	Value float64
}

func (NumberFloatExpr) expr() {}

type NumberIntExpr struct {
	Value int64
}

func (NumberIntExpr) expr() {}

type StringExpr struct {
	Value string
}

func (StringExpr) expr() {}

type BoolExpr struct {
	Value bool
}

func (BoolExpr) expr() {}

type RegexExpr struct {
	Regex *regexp.Regexp
}

func (RegexExpr) expr() {}

type NullExpr struct{}

func (NullExpr) expr() {}
```

## File: `selector/lexer/token.go`
```go
package lexer

import (
	"fmt"
	"slices"
)

type TokenKind int

func TokenKinds(tk ...TokenKind) []TokenKind {
	return tk
}

const (
	EOF TokenKind = iota
	Symbol
	Comma
	Colon
	OpenBracket  // [
	CloseBracket // ]
	OpenCurly
	CloseCurly
	OpenParen
	CloseParen
	Equal    // ==
	Equals   // =
	NotEqual // !=
	And
	Or
	Like    // =~
	NotLike // !~
	String
	Number
	Bool
	Plus
	Increment
	IncrementBy
	Dash
	Decrement
	DecrementBy
	Star
	Slash
	Percent
	Dot
	Spread           // ...
	RecursiveDescent // ..
	Dollar
	Variable
	GreaterThan
	GreaterThanOrEqual
	LessThan
	LessThanOrEqual
	Exclamation
	Null
	If
	Else
	ElseIf
	Branch
	Map
	Each
	Filter
	Search
	RegexPattern
	SortBy
	Asc
	Desc
	QuestionMark
	DoubleQuestionMark
	Semicolon
)

type Tokens []Token

func (tt Tokens) Split(kind TokenKind) []Tokens {
	var res []Tokens
	var cur Tokens
	for _, t := range tt {
		if t.Kind == kind {
			if len(cur) > 0 {
				res = append(res, cur)
			}
			cur = nil
			continue
		}
		cur = append(cur, t)
	}
	if len(cur) > 0 {
		res = append(res, cur)
	}
	return res
}

type Token struct {
	Kind  TokenKind
	Value string
	Pos   int
	Len   int
}

func NewToken(kind TokenKind, value string, pos int, len int) Token {
	return Token{
		Kind:  kind,
		Value: value,
		Pos:   pos,
		Len:   len,
	}
}

func (t Token) IsKind(kind ...TokenKind) bool {
	return slices.Contains(kind, t.Kind)
}

type UnexpectedTokenError struct {
	Pos   int
	Token rune
}

func (e *UnexpectedTokenError) Error() string {
	return fmt.Sprintf("failed to tokenize: unexpected token: %s at position %d.", string(e.Token), e.Pos)
}

type UnexpectedEOFError struct {
	Pos int
}

func (e *UnexpectedEOFError) Error() string {
	return fmt.Sprintf("failed to tokenize: unexpected EOF at position %d.", e.Pos)
}
```

## File: `selector/lexer/tokenize.go`
```go
package lexer

import (
	"strings"
	"unicode"

	"github.com/tomwright/dasel/v3/internal/ptr"
)

type Tokenizer struct {
	i      int
	src    string
	srcLen int
}

func NewTokenizer(src string) *Tokenizer {
	return &Tokenizer{
		i:      0,
		src:    src,
		srcLen: len([]rune(src)),
	}
}

func (p *Tokenizer) Tokenize() (Tokens, error) {
	var tokens Tokens
	for {
		tok, err := p.Next()
		if err != nil {
			return nil, err
		}
		if tok.Kind == EOF {
			break
		}
		tokens = append(tokens, tok)
	}
	return tokens, nil
}

func (p *Tokenizer) peekRuneEqual(i int, to rune) bool {
	if i >= p.srcLen {
		return false
	}
	return rune(p.src[i]) == to
}

func (p *Tokenizer) peekRuneMatches(i int, fn func(rune) bool) bool {
	if i >= p.srcLen {
		return false
	}
	return fn(rune(p.src[i]))
}

func (p *Tokenizer) parseCurRune() (Token, error) {
	// Skip over whitespace
	for p.i < p.srcLen && unicode.IsSpace(rune(p.src[p.i])) {
		p.i++
	}

	// Skip over comments
	if p.src[p.i] == '/' && p.i+1 < p.srcLen && p.src[p.i+1] == '/' {
		p.i += 2
		for p.i < p.srcLen && p.src[p.i] != '\n' {
			p.i++
		}
		// After skipping the comment, skip any whitespace again.
		for p.i < p.srcLen && unicode.IsSpace(rune(p.src[p.i])) {
			p.i++
		}
		if p.i >= p.srcLen {
			return NewToken(EOF, "", p.i, 0), nil
		}
	}

	switch p.src[p.i] {
	case '.':
		if p.peekRuneEqual(p.i+1, '.') && p.peekRuneEqual(p.i+2, '.') {
			return NewToken(Spread, "...", p.i, 3), nil
		}
		if p.peekRuneEqual(p.i+1, '.') {
			return NewToken(RecursiveDescent, "..", p.i, 2), nil
		}
		return NewToken(Dot, ".", p.i, 1), nil
	case ',':
		return NewToken(Comma, ",", p.i, 1), nil
	case ':':
		return NewToken(Colon, ":", p.i, 1), nil
	case ';':
		return NewToken(Semicolon, ";", p.i, 1), nil
	case '[':
		return NewToken(OpenBracket, "[", p.i, 1), nil
	case ']':
		return NewToken(CloseBracket, "]", p.i, 1), nil
	case '(':
		return NewToken(OpenParen, "(", p.i, 1), nil
	case ')':
		return NewToken(CloseParen, ")", p.i, 1), nil
	case '{':
		return NewToken(OpenCurly, "{", p.i, 1), nil
	case '}':
		return NewToken(CloseCurly, "}", p.i, 1), nil
	case '*':
		return NewToken(Star, "*", p.i, 1), nil
	case '/':
		return NewToken(Slash, "/", p.i, 1), nil
	case '%':
		return NewToken(Percent, "%", p.i, 1), nil
	case '$':
		if p.peekRuneMatches(p.i+1, unicode.IsLetter) || p.peekRuneEqual(p.i+1, '_') {
			pos := p.i + 1
			for pos < p.srcLen && (unicode.IsLetter(rune(p.src[pos])) ||
				unicode.IsDigit(rune(p.src[pos])) ||
				p.src[pos] == '_') {
				pos++
			}
			return NewToken(Variable, p.src[p.i+1:pos], p.i, pos-p.i), nil
		}
		return NewToken(Dollar, "$", p.i, 1), nil
	case '=':
		if p.peekRuneEqual(p.i+1, '=') {
			return NewToken(Equal, "==", p.i, 2), nil
		}
		if p.peekRuneEqual(p.i+1, '~') {
			return NewToken(Like, "=~", p.i, 2), nil
		}
		return NewToken(Equals, "=", p.i, 1), nil
	case '+':
		if p.peekRuneEqual(p.i+1, '=') {
			return NewToken(IncrementBy, "+=", p.i, 2), nil
		}
		if p.peekRuneEqual(p.i+1, '+') {
			return NewToken(Increment, "++", p.i, 2), nil
		}
		return NewToken(Plus, "+", p.i, 1), nil
	case '-':
		if p.peekRuneEqual(p.i+1, '=') {
			return NewToken(DecrementBy, "-=", p.i, 2), nil
		}
		if p.peekRuneEqual(p.i+1, '-') {
			return NewToken(Decrement, "--", p.i, 2), nil
		}
		return NewToken(Dash, "-", p.i, 1), nil
	case '>':
		if p.peekRuneEqual(p.i+1, '=') {
			return NewToken(GreaterThanOrEqual, ">=", p.i, 2), nil
		}
		return NewToken(GreaterThan, ">", p.i, 1), nil
	case '<':
		if p.peekRuneEqual(p.i+1, '=') {
			return NewToken(LessThanOrEqual, "<>>=", p.i, 2), nil
		}
		return NewToken(LessThan, "<", p.i, 1), nil
	case '!':
		if p.peekRuneEqual(p.i+1, '=') {
			return NewToken(NotEqual, "!=", p.i, 2), nil
		}
		if p.peekRuneEqual(p.i+1, '~') {
			return NewToken(NotLike, "!~", p.i, 2), nil
		}
		return NewToken(Exclamation, "!", p.i, 1), nil
	case '&':
		if p.peekRuneEqual(p.i+1, '&') {
			return NewToken(And, "&&", p.i, 2), nil
		}
		return Token{}, &UnexpectedTokenError{
			Pos:   p.i,
			Token: rune(p.src[p.i]),
		}
	case '|':
		if p.peekRuneEqual(p.i+1, '|') {
			return NewToken(Or, "||", p.i, 2), nil
		}
		return Token{}, &UnexpectedTokenError{
			Pos:   p.i,
			Token: rune(p.src[p.i]),
		}
	case '?':
		if p.peekRuneEqual(p.i+1, '?') {
			return NewToken(DoubleQuestionMark, "??", p.i, 2), nil
		}
		return NewToken(QuestionMark, "?", p.i, 1), nil
	case '"', '\'':
		pos := p.i
		buf := make([]rune, 0)
		pos++
		foundCloseRune := false
		for pos < p.srcLen {
			if p.src[pos] == p.src[p.i] {
				foundCloseRune = true
				break
			}
			if p.src[pos] == '\\' {
				pos++
				buf = append(buf, rune(p.src[pos]))
				pos++
				continue
			}
			buf = append(buf, rune(p.src[pos]))
			pos++
		}
		if !foundCloseRune {
			// We didn't find a closing quote.
			if pos < p.srcLen {
				// This shouldn't be possible.
				return Token{}, &UnexpectedTokenError{
					Pos:   p.i,
					Token: rune(p.src[pos]),
				}
			}
			// This can happen if the selector ends before the closing quote.
			return Token{}, &UnexpectedEOFError{
				Pos: pos,
			}
		}
		res := NewToken(String, string(buf), p.i, pos+1-p.i)
		return res, nil
	default:
		pos := p.i

		matchStr := func(pos int, m string, caseInsensitive bool, kind TokenKind) *Token {
			l := len(m)
			if pos+(l-1) >= p.srcLen {
				return nil
			}
			other := p.src[pos : pos+l]
			if m != other && (!caseInsensitive || !strings.EqualFold(m, other)) {
				return nil
			}

			if pos+(l) < p.srcLen && (unicode.IsLetter(rune(p.src[pos+l])) || unicode.IsDigit(rune(p.src[pos+l]))) {
				// There is a follow letter or digit.
				return nil
			}

			return ptr.To(NewToken(kind, other, pos, l))
		}

		matchRegexPattern := func(pos int) *Token {
			if p.src[pos] != 'r' || !p.peekRuneEqual(pos+1, '/') {
				return nil
			}
			start := pos
			pos += 2
			for !p.peekRuneEqual(pos, '/') {
				pos++
			}
			pos++
			return ptr.To(NewToken(RegexPattern, p.src[start+2:pos-1], start, pos-start))
		}

		if t := matchStr(pos, "null", true, Null); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "true", true, Bool); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "false", true, Bool); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "elseif", false, ElseIf); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "if", false, If); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "else", false, Else); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "branch", false, Branch); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "map", false, Map); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "each", false, Each); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "filter", false, Filter); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "search", false, Search); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "sortBy", false, SortBy); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "asc", false, Asc); t != nil {
			return *t, nil
		}
		if t := matchStr(pos, "desc", false, Desc); t != nil {
			return *t, nil
		}

		if t := matchRegexPattern(pos); t != nil {
			return *t, nil
		}

		if unicode.IsDigit(rune(p.src[pos])) {
			// Handle whole numbers
			for pos < p.srcLen && unicode.IsDigit(rune(p.src[pos])) {
				pos++
			}
			// Handle floats
			if pos < p.srcLen && p.src[pos] == '.' && pos+1 < p.srcLen && unicode.IsDigit(rune(p.src[pos+1])) {
				pos++
				for pos < p.srcLen && unicode.IsDigit(rune(p.src[pos])) {
					pos++
				}
			}
			return NewToken(Number, p.src[p.i:pos], p.i, pos-p.i), nil
		}

		if unicode.IsLetter(rune(p.src[pos])) || p.src[pos] == '_' {
			for pos < p.srcLen && (unicode.IsLetter(rune(p.src[pos])) ||
				unicode.IsDigit(rune(p.src[pos])) ||
				p.src[pos] == '_') {
				pos++
			}
			return NewToken(Symbol, p.src[p.i:pos], p.i, pos-p.i), nil
		}

		return Token{}, &UnexpectedTokenError{
			Pos:   p.i,
			Token: rune(p.src[p.i]),
		}
	}
}

func (p *Tokenizer) Next() (Token, error) {
	if p.i >= len(p.src) {
		return NewToken(EOF, "", p.i, 0), nil
	}

	t, err := p.parseCurRune()
	if err != nil {
		return Token{}, err
	}
	p.i += t.Len
	return t, nil
}
```

## File: `selector/lexer/tokenize_test.go`
```go
package lexer_test

import (
	"errors"
	"testing"

	"github.com/tomwright/dasel/v3/selector/lexer"
)

type testCase struct {
	in  string
	out []lexer.TokenKind
}

func (tc testCase) run(t *testing.T) {
	tok := lexer.NewTokenizer(tc.in)
	tokens, err := tok.Tokenize()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if len(tokens) != len(tc.out) {
		t.Fatalf("unexpected number of tokens: %d", len(tokens))
	}
	for i := range tokens {
		if tokens[i].Kind != tc.out[i] {
			t.Errorf("unexpected token kind at position %d: exp %v, got %v", i, tc.out[i], tokens[i].Kind)
			return
		}
	}
}

type errTestCase struct {
	in    string
	match func(error) bool
}

func (tc errTestCase) run(t *testing.T) {
	tok := lexer.NewTokenizer(tc.in)
	tokens, err := tok.Tokenize()
	if !tc.match(err) {
		t.Errorf("unexpected error, got %v", err)
	}
	if tokens != nil {
		t.Errorf("unexpected tokens: %v", tokens)
	}
}

// nolint:unused
func matchUnexpectedError(r rune, p int) func(error) bool {
	return func(err error) bool {
		var e *lexer.UnexpectedTokenError
		if !errors.As(err, &e) {
			return false
		}

		return e.Token == r && e.Pos == p
	}
}

func matchUnexpectedEOFError(p int) func(error) bool {
	return func(err error) bool {
		var e *lexer.UnexpectedEOFError
		if !errors.As(err, &e) {
			return false
		}

		return e.Pos == p
	}
}

func TestTokenizer_Parse(t *testing.T) {
	t.Run("variables", testCase{
		in: "$foo $bar123 $baz $ $quietLoudSCREAM $_hello $hello_world",
		out: []lexer.TokenKind{
			lexer.Variable,
			lexer.Variable,
			lexer.Variable,
			lexer.Dollar,
			lexer.Variable,
			lexer.Variable,
			lexer.Variable,
		},
	}.run)

	t.Run("if", testCase{
		in: `if elseif else`,
		out: []lexer.TokenKind{
			lexer.If,
			lexer.ElseIf,
			lexer.Else,
		},
	}.run)

	t.Run("regex", testCase{
		in: `r/asd/ r/hello there/`,
		out: []lexer.TokenKind{
			lexer.RegexPattern,
			lexer.RegexPattern,
		},
	}.run)

	t.Run("sort by", testCase{
		in: `sortBy(foo, asc)`,
		out: []lexer.TokenKind{
			lexer.SortBy,
			lexer.OpenParen,
			lexer.Symbol,
			lexer.Comma,
			lexer.Asc,
			lexer.CloseParen,
		},
	}.run)

	t.Run("recursive descent", func(t *testing.T) {
		t.Run("key", testCase{
			in: `..foo`,
			out: []lexer.TokenKind{
				lexer.RecursiveDescent,
				lexer.Symbol,
			},
		}.run)
		t.Run("index", testCase{
			in: `..[1]`,
			out: []lexer.TokenKind{
				lexer.RecursiveDescent,
				lexer.OpenBracket,
				lexer.Number,
				lexer.CloseBracket,
			},
		}.run)
		t.Run("wildcard", testCase{
			in: `..*`,
			out: []lexer.TokenKind{
				lexer.RecursiveDescent,
				lexer.Star,
			},
		}.run)
	})

	t.Run("everything", testCase{
		in: "foo.bar.baz[1] != 42.123 || foo.b_a_r.baz['hello'] == 42 && x == 'a\\'b' + false true . .... asd... $name null",
		out: []lexer.TokenKind{
			lexer.Symbol, lexer.Dot, lexer.Symbol, lexer.Dot, lexer.Symbol, lexer.OpenBracket, lexer.Number, lexer.CloseBracket, lexer.NotEqual, lexer.Number,
			lexer.Or,
			lexer.Symbol, lexer.Dot, lexer.Symbol, lexer.Dot, lexer.Symbol, lexer.OpenBracket, lexer.String, lexer.CloseBracket, lexer.Equal, lexer.Number,
			lexer.And,
			lexer.Symbol, lexer.Equal, lexer.String,
			lexer.Plus, lexer.Bool, lexer.Bool,
			lexer.Dot, lexer.Spread, lexer.Dot,
			lexer.Symbol, lexer.Spread,
			lexer.Variable, lexer.Null,
		},
	}.run)

	t.Run("unhappy", func(t *testing.T) {
		t.Run("unfinished double quote", errTestCase{
			in:    `"hello`,
			match: matchUnexpectedEOFError(6),
		}.run)
		t.Run("unfinished single quote", errTestCase{
			in:    `'hello`,
			match: matchUnexpectedEOFError(6),
		}.run)
	})
}
```

## File: `selector/parser/denotations.go`
```go
package parser

import "github.com/tomwright/dasel/v3/selector/lexer"

// left denotation tokens are tokens that expect a token to the left of them.
var leftDenotationTokens = []lexer.TokenKind{
	lexer.Plus,
	lexer.Dash,
	lexer.Slash,
	lexer.Star,
	lexer.Percent,
	lexer.Equal,
	lexer.NotEqual,
	lexer.GreaterThan,
	lexer.GreaterThanOrEqual,
	lexer.LessThan,
	lexer.LessThanOrEqual,
	lexer.And,
	lexer.Or,
	lexer.Like,
	lexer.NotLike,
	lexer.Equals,
	lexer.DoubleQuestionMark,
}

// right denotation tokens are tokens that expect a token to the right of them.
var rightDenotationTokens = []lexer.TokenKind{
	lexer.Exclamation, // Not operator
}

type bindingPower int

const (
	bpDefault bindingPower = iota
	bpAssignment
	bpLogical
	bpEarlyLogical
	bpRelational
	bpAdditive
	bpMultiplicative
	bpUnary
	bpCall
	bpProperty
	bpLiteral
)

var tokenBindingPowers = map[lexer.TokenKind]bindingPower{
	lexer.String: bpLiteral,
	lexer.Number: bpLiteral,
	lexer.Bool:   bpLiteral,
	lexer.Null:   bpLiteral,

	lexer.Variable:    bpProperty,
	lexer.Dot:         bpProperty,
	lexer.OpenBracket: bpProperty,

	lexer.OpenParen: bpCall,

	lexer.Exclamation: bpUnary,

	lexer.Star:    bpMultiplicative,
	lexer.Slash:   bpMultiplicative,
	lexer.Percent: bpMultiplicative,

	lexer.Plus: bpAdditive,
	lexer.Dash: bpAdditive,

	lexer.Equal:              bpRelational,
	lexer.NotEqual:           bpRelational,
	lexer.GreaterThan:        bpRelational,
	lexer.GreaterThanOrEqual: bpRelational,
	lexer.LessThan:           bpRelational,
	lexer.LessThanOrEqual:    bpRelational,

	lexer.And:     bpLogical,
	lexer.Or:      bpLogical,
	lexer.Like:    bpLogical,
	lexer.NotLike: bpLogical,

	lexer.DoubleQuestionMark: bpEarlyLogical,

	lexer.Equals: bpAssignment,
}

func getTokenBindingPower(t lexer.TokenKind) bindingPower {
	if bp, ok := tokenBindingPowers[t]; ok {
		return bp
	}
	return bpDefault
}
```

## File: `selector/parser/error.go`
```go
package parser

import (
	"fmt"

	"github.com/tomwright/dasel/v3/selector/lexer"
)

type PositionalError struct {
	Position int
	Err      error
}

func (e *PositionalError) Error() string {
	return fmt.Sprintf("%v. Position %d.", e.Err, e.Position)
}

type UnexpectedTokenError struct {
	Token lexer.Token
}

func (e *UnexpectedTokenError) Error() string {
	return fmt.Sprintf("failed to parse: unexpected token %v %q at position %d.", e.Token.Kind, e.Token.Value, e.Token.Pos)
}
```

## File: `selector/parser/parser.go`
```go
package parser

import (
	"slices"

	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

type Parser struct {
	tokens lexer.Tokens
	i      int
}

func NewParser(tokens lexer.Tokens) *Parser {
	return &Parser{
		tokens: tokens,
	}
}

func (p *Parser) parseExpressionsAsSlice(
	breakOn []lexer.TokenKind,
	splitOn []lexer.TokenKind,
	requireExpressions bool,
	bp bindingPower,
	advanceOnBreak bool,
) (ast.Expressions, error) {
	var finalExpr ast.Expressions
	var current ast.Expressions
	for p.hasToken() {
		if p.current().IsKind(breakOn...) {
			if advanceOnBreak {
				p.advance()
			}
			break
		}
		if p.current().IsKind(splitOn...) {
			if requireExpressions && len(current) == 0 {
				return nil, &UnexpectedTokenError{Token: p.current()}
			}
			finalExpr = append(finalExpr, ast.ChainExprs(current...))
			current = nil
			p.advance()
			continue
		}
		expr, err := p.parseExpression(bp)
		if err != nil {
			return nil, err
		}
		current = append(current, expr)
	}

	if len(current) > 0 {
		finalExpr = append(finalExpr, ast.ChainExprs(current...))
	}

	if len(finalExpr) == 0 {
		return nil, nil
	}

	return finalExpr, nil
}

func (p *Parser) parseExpressions(
	breakOn []lexer.TokenKind,
	splitOn []lexer.TokenKind,
	requireExpressions bool,
	bp bindingPower,
	advanceOnBreak bool,
) (ast.Expr, error) {
	expressions, err := p.parseExpressionsAsSlice(breakOn, splitOn, requireExpressions, bp, advanceOnBreak)
	if err != nil {
		return nil, err
	}
	switch len(expressions) {
	case 0:
		return nil, nil
	default:
		return ast.ChainExprs(expressions...), nil
	}
}

func (p *Parser) Parse() (ast.Expr, error) {
	return p.parseExpressions([]lexer.TokenKind{lexer.EOF}, []lexer.TokenKind{lexer.Semicolon}, true, bpDefault, true)
}

func (p *Parser) parseExpression(bp bindingPower) (left ast.Expr, err error) {
	if p.hasToken() && slices.Contains(rightDenotationTokens, p.current().Kind) {
		unary := ast.UnaryExpr{
			Operator: p.current(),
			Right:    nil,
		}
		p.advance()
		expr, err := p.parseExpression(getTokenBindingPower(unary.Operator.Kind))
		if err != nil {
			return nil, err
		}
		p.advance()
		unary.Right = expr
		left = unary
	}

	if !p.hasToken() {
		return
	}

	switch p.current().Kind {
	case lexer.String:
		left, err = parseStringLiteral(p)
	case lexer.Number:
		left, err = parseNumberLiteral(p)
	case lexer.Dash:
		if p.peek().Kind == lexer.Number {
			left, err = parseNumberLiteral(p)
		} else {
			return nil, &UnexpectedTokenError{
				Token: p.current(),
			}
		}
	case lexer.Symbol:
		left, err = parseSymbol(p, true, true)
	case lexer.OpenBracket:
		left, err = parseArray(p)
	case lexer.OpenCurly:
		left, err = parseObject(p)
	case lexer.Bool:
		left, err = parseBoolLiteral(p)
	case lexer.Spread:
		left, err = parseSpread(p)
	case lexer.Variable:
		left, err = parseVariable(p)
	case lexer.OpenParen:
		left, err = parseGroup(p)
	case lexer.If:
		left, err = parseIf(p)
	case lexer.Branch:
		left, err = parseBranch(p)
	case lexer.Map:
		left, err = parseMap(p)
	case lexer.Each:
		left, err = parseEach(p)
	case lexer.Filter:
		left, err = parseFilter(p)
	case lexer.Search:
		left, err = parseSearch(p)
	case lexer.RecursiveDescent:
		left, err = parseRecursiveDescent(p)
	case lexer.RegexPattern:
		left, err = parseRegexPattern(p)
	case lexer.SortBy:
		left, err = parseSortBy(p)
	case lexer.Null:
		left = ast.NullExpr{}
		err = nil
		p.advance()
	default:
		return nil, &UnexpectedTokenError{
			Token: p.current(),
		}
	}

	if err != nil {
		return
	}

	toChain := ast.Expressions{left}
	// Ensure dot separated chains are parsed as a sequence of expressions
	if p.hasToken() && p.current().IsKind(lexer.Dot) {
		for p.hasToken() && p.current().IsKind(lexer.Dot) {
			p.advance()
			expr, err := p.parseExpression(bpUnary)
			if err != nil {
				return nil, err
			}
			toChain = append(toChain, expr)
		}
	}

	// Handle spread
	if p.hasToken() && p.current().IsKind(lexer.Spread) {
		expr, err := p.parseExpression(bpLiteral)
		if err != nil {
			return nil, err
		}
		toChain = append(toChain, expr)
	}

	if len(toChain) > 1 {
		left = ast.ChainExprs(toChain...)
	}

	// Handle binding powers
	for p.hasToken() && slices.Contains(leftDenotationTokens, p.current().Kind) && getTokenBindingPower(p.current().Kind) > bp {
		left, err = parseBinary(p, left)
		if err != nil {
			return
		}
	}

	return
}

func (p *Parser) hasToken() bool {
	return p.hasTokenN(0)
}

func (p *Parser) hasTokenN(n int) bool {
	return p.i+n < len(p.tokens) && !p.tokens[p.i+n].IsKind(lexer.EOF)
}

func (p *Parser) current() lexer.Token {
	if p.hasToken() {
		return p.tokens[p.i]
	}
	return lexer.Token{Kind: lexer.EOF}
}

func (p *Parser) advance() lexer.Token {
	return p.advanceN(1)
}

func (p *Parser) advanceN(n int) lexer.Token {
	p.i += n
	return p.current()
}

func (p *Parser) peek() lexer.Token {
	return p.peekN(1)
}

func (p *Parser) peekN(n int) lexer.Token {
	if p.i+n >= len(p.tokens) {
		return lexer.Token{Kind: lexer.EOF}
	}
	return p.tokens[p.i+n]
}

func (p *Parser) expect(kind ...lexer.TokenKind) error {
	t := p.current()
	if p.current().IsKind(kind...) {
		return nil
	}
	return &UnexpectedTokenError{
		Token: t,
	}
}

func (p *Parser) expectN(n int, kind ...lexer.TokenKind) error {
	t := p.peekN(n)
	if t.IsKind(kind...) {
		return nil
	}
	return &UnexpectedTokenError{
		Token: t,
	}
}
```

## File: `selector/parser/parser_binary.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
)

func parseBinary(p *Parser, left ast.Expr) (ast.Expr, error) {
	if err := p.expect(leftDenotationTokens...); err != nil {
		return nil, err
	}
	operator := p.current()
	p.advance()
	right, err := p.parseExpression(getTokenBindingPower(operator.Kind))
	if err != nil {
		return nil, err
	}

	//if l, ok := left.(ast.BinaryExpr); ok && l.Operator.Kind == lexer.DoubleQuestionMark {
	//	if r, ok := right.(ast.BinaryExpr); ok && r.Operator.Kind == lexer.DoubleQuestionMark {
	//		return ast.BinaryExpr{
	//			Left:     l.Left,
	//			Operator: l.Operator,
	//			Right: ast.BinaryExpr{
	//				Left:     l.Right,
	//				Operator: r.Operator,
	//				Right:    r.Right,
	//			},
	//		}, nil
	//	}
	//}
	//
	//if r, ok := right.(ast.BinaryExpr); ok && r.Operator.Kind == lexer.DoubleQuestionMark {
	//	return ast.BinaryExpr{
	//		Left: ast.BinaryExpr{
	//			Left:     left,
	//			Operator: operator,
	//			Right:    r.Left,
	//		},
	//		Operator: r.Operator,
	//		Right:    r.Right,
	//	}, nil
	//}
	//
	//if l, ok := left.(ast.BinaryExpr); ok && l.Operator.Kind == lexer.DoubleQuestionMark {
	//	return ast.BinaryExpr{
	//		Left:     l.Left,
	//		Operator: l.Operator,
	//		Right: ast.BinaryExpr{
	//			Left:     l.Right,
	//			Operator: operator,
	//			Right:    right,
	//		},
	//	}, nil
	//}

	return ast.BinaryExpr{
		Left:     left,
		Operator: operator,
		Right:    right,
	}, nil
}
```

## File: `selector/parser/parser_test.go`
```go
package parser_test

import (
	"testing"

	"github.com/google/go-cmp/cmp"
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
	"github.com/tomwright/dasel/v3/selector/parser"
)

type happyTestCase struct {
	input    string
	expected ast.Expr
}

func (tc happyTestCase) run(t *testing.T) {
	tokens, err := lexer.NewTokenizer(tc.input).Tokenize()
	if err != nil {
		t.Fatal(err)
	}
	got, err := parser.NewParser(tokens).Parse()
	if err != nil {
		t.Fatal(err)
	}
	if !cmp.Equal(tc.expected, got) {
		t.Errorf("unexpected result: %s", cmp.Diff(tc.expected, got))
	}
}

func TestParser_Parse_HappyPath(t *testing.T) {
	t.Run("branching", func(t *testing.T) {
		t.Run("two branches", happyTestCase{
			input: `branch("hello", len("world"))`,
			expected: ast.BranchExprs(
				ast.StringExpr{Value: "hello"},
				ast.ChainExprs(
					ast.CallExpr{
						Function: "len",
						Args:     ast.Expressions{ast.StringExpr{Value: "world"}},
					},
				),
			),
		}.run)
		t.Run("three branches", happyTestCase{
			input: `branch("foo", "bar", "baz")`,
			expected: ast.BranchExprs(
				ast.StringExpr{Value: "foo"},
				ast.StringExpr{Value: "bar"},
				ast.StringExpr{Value: "baz"},
			),
		}.run)
	})

	t.Run("literal access", func(t *testing.T) {
		t.Run("string", happyTestCase{
			input:    `"hello world"`,
			expected: ast.StringExpr{Value: "hello world"},
		}.run)
		t.Run("int", happyTestCase{
			input:    "42",
			expected: ast.NumberIntExpr{Value: 42},
		}.run)
		t.Run("float", happyTestCase{
			input:    "42.1",
			expected: ast.NumberFloatExpr{Value: 42.1},
		}.run)
		t.Run("whole number float", happyTestCase{
			input:    "42f",
			expected: ast.NumberFloatExpr{Value: 42},
		}.run)
		t.Run("bool true lowercase", happyTestCase{
			input:    "true",
			expected: ast.BoolExpr{Value: true},
		}.run)
		t.Run("bool true uppercase", happyTestCase{
			input:    "TRUE",
			expected: ast.BoolExpr{Value: true},
		}.run)
		t.Run("bool true mixed case", happyTestCase{
			input:    "TrUe",
			expected: ast.BoolExpr{Value: true},
		}.run)
		t.Run("bool false lowercase", happyTestCase{
			input:    "false",
			expected: ast.BoolExpr{Value: false},
		}.run)
		t.Run("bool false uppercase", happyTestCase{
			input:    "FALSE",
			expected: ast.BoolExpr{Value: false},
		}.run)
		t.Run("bool false mixed case", happyTestCase{
			input:    "FaLsE",
			expected: ast.BoolExpr{Value: false},
		}.run)
	})

	t.Run("property access", func(t *testing.T) {
		t.Run("single property access", happyTestCase{
			input:    "foo",
			expected: ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
		}.run)
		t.Run("chained property access", happyTestCase{
			input: "foo.bar",
			expected: ast.ChainExprs(
				ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
				ast.PropertyExpr{Property: ast.StringExpr{Value: "bar"}},
			),
		}.run)
		t.Run("property access spread", happyTestCase{
			input: "foo...",
			expected: ast.ChainExprs(
				ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
				ast.SpreadExpr{},
			),
		}.run)
		t.Run("property access spread into property access", happyTestCase{
			input: "foo....bar",
			expected: ast.ChainExprs(
				ast.ChainExprs(
					ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
					ast.SpreadExpr{},
				),
				ast.PropertyExpr{Property: ast.StringExpr{Value: "bar"}},
			),
		}.run)
	})

	t.Run("array access", func(t *testing.T) {
		t.Run("chained with filter", happyTestCase{
			input: "filter(name == \"foo\")[0]",
			expected: ast.ChainExprs(
				ast.FilterExpr{
					Expr: ast.BinaryExpr{
						Left: ast.PropertyExpr{Property: ast.StringExpr{Value: "name"}},
						Operator: lexer.Token{
							Kind:  lexer.Equal,
							Value: "==",
							Pos:   12,
							Len:   2,
						},
						Right: ast.StringExpr{Value: "foo"},
					},
				},
				ast.PropertyExpr{Property: ast.NumberIntExpr{Value: 0}},
			),
		}.run)
		t.Run("chained with map", happyTestCase{
			input: "map(foo)[0]",
			expected: ast.ChainExprs(
				ast.MapExpr{
					Expr: ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
				},
				ast.PropertyExpr{Property: ast.NumberIntExpr{Value: 0}},
			),
		}.run)
		t.Run("root array", func(t *testing.T) {
			t.Run("index", happyTestCase{
				input: "$this[1]",
				expected: ast.ChainExprs(
					ast.VariableExpr{Name: "this"},
					ast.PropertyExpr{Property: ast.NumberIntExpr{Value: 1}},
				),
			}.run)
			t.Run("range", func(t *testing.T) {
				t.Run("start and end funcs", happyTestCase{
					input: "$this[calcStart(1):calcEnd()]",
					expected: ast.ChainExprs(
						ast.VariableExpr{Name: "this"},
						ast.RangeExpr{
							Start: ast.CallExpr{
								Function: "calcStart",
								Args: ast.Expressions{
									ast.NumberIntExpr{Value: 1},
								},
							},
							End: ast.CallExpr{
								Function: "calcEnd",
							},
						},
					),
				}.run)
				t.Run("start and end", happyTestCase{
					input: "$this[5:10]",
					expected: ast.ChainExprs(
						ast.VariableExpr{Name: "this"},
						ast.RangeExpr{Start: ast.NumberIntExpr{Value: 5}, End: ast.NumberIntExpr{Value: 10}},
					),
				}.run)
				t.Run("start", happyTestCase{
					input: "$this[5:]",
					expected: ast.ChainExprs(
						ast.VariableExpr{Name: "this"},
						ast.RangeExpr{Start: ast.NumberIntExpr{Value: 5}},
					),
				}.run)
				t.Run("end", happyTestCase{
					input: "$this[:10]",
					expected: ast.ChainExprs(
						ast.VariableExpr{Name: "this"},
						ast.RangeExpr{End: ast.NumberIntExpr{Value: 10}},
					),
				}.run)
			})
			t.Run("spread", func(t *testing.T) {
				t.Run("standard", happyTestCase{
					input: "$this...",
					expected: ast.ChainExprs(
						ast.VariableExpr{Name: "this"},
						ast.SpreadExpr{},
					),
				}.run)
				t.Run("brackets", happyTestCase{
					input: "$this[...]",
					expected: ast.ChainExprs(
						ast.VariableExpr{Name: "this"},
						ast.SpreadExpr{},
					),
				}.run)
			})
		})
		t.Run("property array", func(t *testing.T) {
			t.Run("index", happyTestCase{
				input: "foo[1]",
				expected: ast.ChainExprs(
					ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
					ast.PropertyExpr{Property: ast.NumberIntExpr{Value: 1}},
				),
			}.run)
			t.Run("range", func(t *testing.T) {
				t.Run("start and end funcs", happyTestCase{
					input: "foo[calcStart(1):calcEnd()]",
					expected: ast.ChainExprs(
						ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
						ast.RangeExpr{
							Start: ast.CallExpr{
								Function: "calcStart",
								Args: ast.Expressions{
									ast.NumberIntExpr{Value: 1},
								},
							},
							End: ast.CallExpr{
								Function: "calcEnd",
							},
						},
					),
				}.run)
				t.Run("start and end", happyTestCase{
					input: "foo[5:10]",
					expected: ast.ChainExprs(
						ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
						ast.RangeExpr{Start: ast.NumberIntExpr{Value: 5}, End: ast.NumberIntExpr{Value: 10}},
					),
				}.run)
				t.Run("start", happyTestCase{
					input: "foo[5:]",
					expected: ast.ChainExprs(
						ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
						ast.RangeExpr{Start: ast.NumberIntExpr{Value: 5}},
					),
				}.run)
				t.Run("end", happyTestCase{
					input: "foo[:10]",
					expected: ast.ChainExprs(
						ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
						ast.RangeExpr{End: ast.NumberIntExpr{Value: 10}},
					),
				}.run)
			})
			t.Run("spread", func(t *testing.T) {
				t.Run("standard", happyTestCase{
					input: "foo...",
					expected: ast.ChainExprs(
						ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
						ast.SpreadExpr{},
					),
				}.run)
				t.Run("brackets", happyTestCase{
					input: "foo[...]",
					expected: ast.ChainExprs(
						ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
						ast.SpreadExpr{},
					),
				}.run)
			})
		})
	})

	t.Run("map", func(t *testing.T) {
		t.Run("single property", happyTestCase{
			input: "foo.map(x)",
			expected: ast.ChainExprs(
				ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
				ast.MapExpr{
					Expr: ast.PropertyExpr{Property: ast.StringExpr{Value: "x"}},
				},
			),
		}.run)
		t.Run("nested property", happyTestCase{
			input: "foo.map(x.y)",
			expected: ast.ChainExprs(
				ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
				ast.MapExpr{
					Expr: ast.ChainExprs(
						ast.PropertyExpr{Property: ast.StringExpr{Value: "x"}},
						ast.PropertyExpr{Property: ast.StringExpr{Value: "y"}},
					),
				},
			),
		}.run)
	})

	t.Run("object", func(t *testing.T) {
		t.Run("get single property", happyTestCase{
			input: "{foo}",
			expected: ast.ObjectExpr{Pairs: []ast.KeyValue{
				{Key: ast.StringExpr{Value: "foo"}, Value: ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}}},
			}},
		}.run)
		t.Run("get multiple properties", happyTestCase{
			input: "{foo, bar, baz}",
			expected: ast.ObjectExpr{Pairs: []ast.KeyValue{
				{Key: ast.StringExpr{Value: "foo"}, Value: ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}}},
				{Key: ast.StringExpr{Value: "bar"}, Value: ast.PropertyExpr{Property: ast.StringExpr{Value: "bar"}}},
				{Key: ast.StringExpr{Value: "baz"}, Value: ast.PropertyExpr{Property: ast.StringExpr{Value: "baz"}}},
			}},
		}.run)
		t.Run("set single property", happyTestCase{
			input: `{"foo":1}`,
			expected: ast.ObjectExpr{Pairs: []ast.KeyValue{
				{Key: ast.StringExpr{Value: "foo"}, Value: ast.NumberIntExpr{Value: 1}},
			}},
		}.run)
		t.Run("set multiple properties", happyTestCase{
			input: `{foo: 1, bar: 2, baz: 3}`,
			expected: ast.ObjectExpr{Pairs: []ast.KeyValue{
				{Key: ast.StringExpr{Value: "foo"}, Value: ast.NumberIntExpr{Value: 1}},
				{Key: ast.StringExpr{Value: "bar"}, Value: ast.NumberIntExpr{Value: 2}},
				{Key: ast.StringExpr{Value: "baz"}, Value: ast.NumberIntExpr{Value: 3}},
			}},
		}.run)
		t.Run("combine get set", happyTestCase{
			input: `{
				...,
				nestedSpread...,
				foo,
				bar: 2,
				"baz": evalSomething(),
				"Name": "Tom",
			}`,
			expected: ast.ObjectExpr{Pairs: []ast.KeyValue{
				{Key: ast.SpreadExpr{}, Value: nil},
				{Key: ast.SpreadExpr{}, Value: ast.PropertyExpr{Property: ast.StringExpr{Value: "nestedSpread"}}},
				{Key: ast.StringExpr{Value: "foo"}, Value: ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}}},
				{Key: ast.StringExpr{Value: "bar"}, Value: ast.NumberIntExpr{Value: 2}},
				{Key: ast.StringExpr{Value: "baz"}, Value: ast.CallExpr{Function: "evalSomething"}},
				{Key: ast.StringExpr{Value: "Name"}, Value: ast.StringExpr{Value: "Tom"}},
			}},
		}.run)
	})

	t.Run("variables", func(t *testing.T) {
		t.Run("single variable", happyTestCase{
			input:    `$foo`,
			expected: ast.VariableExpr{Name: "foo"},
		}.run)
		t.Run("variable passed to func", happyTestCase{
			input:    `len($foo)`,
			expected: ast.CallExpr{Function: "len", Args: ast.Expressions{ast.VariableExpr{Name: "foo"}}},
		}.run)
	})

	t.Run("combinations and grouping", func(t *testing.T) {
		t.Run("string concat with grouping", happyTestCase{
			input: `(foo.a) + (foo.b)`,
			expected: ast.BinaryExpr{
				Left:     ast.ChainExprs(ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}}, ast.PropertyExpr{Property: ast.StringExpr{Value: "a"}}),
				Operator: lexer.Token{Kind: lexer.Plus, Value: "+", Pos: 8, Len: 1},
				Right:    ast.ChainExprs(ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}}, ast.PropertyExpr{Property: ast.StringExpr{Value: "b"}}),
			},
		}.run)
		t.Run("string concat with nested properties", happyTestCase{
			input: `foo.a + foo.b`,
			expected: ast.BinaryExpr{
				Left:     ast.ChainExprs(ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}}, ast.PropertyExpr{Property: ast.StringExpr{Value: "a"}}),
				Operator: lexer.Token{Kind: lexer.Plus, Value: "+", Pos: 6, Len: 1},
				Right:    ast.ChainExprs(ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}}, ast.PropertyExpr{Property: ast.StringExpr{Value: "b"}}),
			},
		}.run)
	})

	t.Run("conditional", func(t *testing.T) {
		t.Run("if", happyTestCase{
			input: `if (foo == 1) { "yes" } else { "no" }`,
			expected: ast.ConditionalExpr{
				Cond: ast.BinaryExpr{
					Left:     ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
					Operator: lexer.Token{Kind: lexer.Equal, Value: "==", Pos: 8, Len: 2},
					Right:    ast.NumberIntExpr{Value: 1},
				},
				Then: ast.StringExpr{Value: "yes"},
				Else: ast.StringExpr{Value: "no"},
			},
		}.run)
		t.Run("if elseif else", happyTestCase{
			input: `if (foo == 1) { "yes" } elseif (foo == 2) { "maybe" } else { "no" }`,
			expected: ast.ConditionalExpr{
				Cond: ast.BinaryExpr{
					Left:     ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
					Operator: lexer.Token{Kind: lexer.Equal, Value: "==", Pos: 8, Len: 2},
					Right:    ast.NumberIntExpr{Value: 1},
				},
				Then: ast.StringExpr{Value: "yes"},
				Else: ast.ConditionalExpr{
					Cond: ast.BinaryExpr{
						Left:     ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
						Operator: lexer.Token{Kind: lexer.Equal, Value: "==", Pos: 36, Len: 2},
						Right:    ast.NumberIntExpr{Value: 2},
					},
					Then: ast.StringExpr{Value: "maybe"},
					Else: ast.StringExpr{Value: "no"},
				},
			},
		}.run)
		t.Run("if elseif elseif else", happyTestCase{
			input: `if (foo == 1) { "yes" } elseif (foo == 2) { "maybe" } elseif (foo == 3) { "probably" } else { "no" }`,
			expected: ast.ConditionalExpr{
				Cond: ast.BinaryExpr{
					Left:     ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
					Operator: lexer.Token{Kind: lexer.Equal, Value: "==", Pos: 8, Len: 2},
					Right:    ast.NumberIntExpr{Value: 1},
				},
				Then: ast.StringExpr{Value: "yes"},
				Else: ast.ConditionalExpr{
					Cond: ast.BinaryExpr{
						Left:     ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
						Operator: lexer.Token{Kind: lexer.Equal, Value: "==", Pos: 36, Len: 2},
						Right:    ast.NumberIntExpr{Value: 2},
					},
					Then: ast.StringExpr{Value: "maybe"},
					Else: ast.ConditionalExpr{
						Cond: ast.BinaryExpr{
							Left:     ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
							Operator: lexer.Token{Kind: lexer.Equal, Value: "==", Pos: 66, Len: 2},
							Right:    ast.NumberIntExpr{Value: 3},
						},
						Then: ast.StringExpr{Value: "probably"},
						Else: ast.StringExpr{Value: "no"},
					},
				},
			},
		}.run)
	})

	t.Run("coalesce", func(t *testing.T) {
		t.Run("chained on left side", happyTestCase{
			input: `foo ?? bar ?? baz`,
			expected: ast.BinaryExpr{
				Left: ast.BinaryExpr{
					Left:     ast.PropertyExpr{Property: ast.StringExpr{Value: "foo"}},
					Operator: lexer.Token{Kind: lexer.DoubleQuestionMark, Value: "??", Pos: 4, Len: 2},
					Right:    ast.PropertyExpr{Property: ast.StringExpr{Value: "bar"}},
				},
				Operator: lexer.Token{Kind: lexer.DoubleQuestionMark, Value: "??", Pos: 11, Len: 2},
				Right:    ast.PropertyExpr{Property: ast.StringExpr{Value: "baz"}},
			},
		}.run)

		t.Run("chained nested on left side", happyTestCase{
			input: `nested.one ?? nested.two ?? nested.three ?? 10`,
			expected: ast.BinaryExpr{
				Left: ast.BinaryExpr{
					Left: ast.BinaryExpr{
						Left: ast.ChainExprs(
							ast.PropertyExpr{Property: ast.StringExpr{Value: "nested"}},
							ast.PropertyExpr{Property: ast.StringExpr{Value: "one"}},
						),
						Operator: lexer.Token{Kind: lexer.DoubleQuestionMark, Value: "??", Pos: 11, Len: 2},
						Right: ast.ChainExprs(
							ast.PropertyExpr{Property: ast.StringExpr{Value: "nested"}},
							ast.PropertyExpr{Property: ast.StringExpr{Value: "two"}},
						),
					},
					Operator: lexer.Token{Kind: lexer.DoubleQuestionMark, Value: "??", Pos: 25, Len: 2},
					Right: ast.ChainExprs(
						ast.PropertyExpr{Property: ast.StringExpr{Value: "nested"}},
						ast.PropertyExpr{Property: ast.StringExpr{Value: "three"}},
					),
				},
				Operator: lexer.Token{Kind: lexer.DoubleQuestionMark, Value: "??", Pos: 41, Len: 2},
				Right:    ast.NumberIntExpr{Value: 10},
			},
		}.run)
	})
}
```

## File: `selector/parser/parse_array.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseArray(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.OpenBracket); err != nil {
		return nil, err
	}
	p.advance()

	elements, err := p.parseExpressionsAsSlice(
		lexer.TokenKinds(lexer.CloseBracket),
		lexer.TokenKinds(lexer.Comma),
		false,
		bpDefault,
		true,
	)
	if err != nil {
		return nil, err
	}

	arr := ast.ArrayExpr{
		Exprs: elements,
	}

	res, err := parseFollowingSymbol(p, arr)
	if err != nil {
		return nil, err
	}

	return res, nil
}

// parseIndexSquareBrackets parses square bracket array access.
// E.g. [0], [0:1], [0:], [:2]
func parseIndexSquareBrackets(p *Parser, expectIndex bool) (ast.Expr, error) {
	// Handle index (from bracket)
	if err := p.expect(lexer.OpenBracket); err != nil {
		return nil, err
	}

	p.advance()

	// Spread [...]
	if p.current().IsKind(lexer.Spread) {
		p.advance()
		if err := p.expect(lexer.CloseBracket); err != nil {
			return nil, err
		}
		p.advance()
		return ast.SpreadExpr{}, nil
	}

	var (
		start ast.Expr
		end   ast.Expr
		err   error
	)

	if p.current().IsKind(lexer.Colon) {
		p.advance()
		// We have no start index
		end, err = p.parseExpression(bpDefault)
		if err != nil {
			return nil, err
		}
		p.advance()
		return ast.RangeExpr{
			End: end,
		}, nil
	}

	start, err = p.parseExpression(bpDefault)
	if err != nil {
		return nil, err
	}

	if p.current().IsKind(lexer.CloseBracket) {
		// This is an index
		p.advance()
		return ast.IndexExpr{
			Index: start,
		}, nil
	}
	if expectIndex {
		if err := p.expect(lexer.CloseBracket); err != nil {
			return nil, err
		}
	}

	if err := p.expect(lexer.Colon); err != nil {
		return nil, err
	}

	p.advance()

	if p.current().IsKind(lexer.CloseBracket) {
		// There is no end
		p.advance()
		return ast.RangeExpr{
			Start: start,
		}, nil
	}

	end, err = p.parseExpression(bpDefault)
	if err != nil {
		return nil, err
	}

	p.advance()
	return ast.RangeExpr{
		Start: start,
		End:   end,
	}, nil
}
```

## File: `selector/parser/parse_branch.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseBranch(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.Branch); err != nil {
		return nil, err
	}

	p.advance()
	if err := p.expect(lexer.OpenParen); err != nil {
		return nil, err
	}
	p.advance()

	expressions, err := p.parseExpressionsAsSlice(
		[]lexer.TokenKind{lexer.CloseParen},
		[]lexer.TokenKind{lexer.Comma},
		true,
		bpDefault,
		true,
	)
	if err != nil {
		return nil, err
	}

	return ast.BranchExpr{
		Exprs: expressions,
	}, nil
}
```

## File: `selector/parser/parse_each.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseEach(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.Each); err != nil {
		return nil, err
	}
	p.advance()

	expr, err := p.parseExpressionsFromTo(
		lexer.OpenParen,
		lexer.CloseParen,
		[]lexer.TokenKind{},
		true,
		bpDefault,
	)
	if err != nil {
		return nil, err
	}

	return ast.EachExpr{
		Expr: expr,
	}, nil
}
```

## File: `selector/parser/parse_filter.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseFilter(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.Filter); err != nil {
		return nil, err
	}
	p.advance()

	expr, err := p.parseExpressionsFromTo(
		lexer.OpenParen,
		lexer.CloseParen,
		[]lexer.TokenKind{},
		true,
		bpDefault,
	)
	if err != nil {
		return nil, err
	}

	filterExpr := ast.FilterExpr{
		Expr: expr,
	}

	res, err := parseFollowingSymbol(p, filterExpr)
	if err != nil {
		return nil, err
	}

	return res, nil
}
```

## File: `selector/parser/parse_func.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseFunc(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.Symbol); err != nil {
		return nil, err
	}
	if err := p.expectN(1, lexer.OpenParen); err != nil {
		return nil, err
	}

	token := p.current()

	p.advanceN(2)
	args, err := parseArgs(p)
	if err != nil {
		return nil, err
	}
	return ast.CallExpr{
		Function: token.Value,
		Args:     args,
	}, nil
}

func parseArgs(p *Parser) (ast.Expressions, error) {
	return p.parseExpressionsAsSlice(
		[]lexer.TokenKind{lexer.CloseParen},
		[]lexer.TokenKind{lexer.Comma},
		false,
		bpCall,
		true,
	)
}
```

## File: `selector/parser/parse_group.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseGroup(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.OpenParen); err != nil {
		return nil, err
	}
	p.advance() // skip the open paren

	return p.parseExpressions(
		[]lexer.TokenKind{lexer.CloseParen},
		[]lexer.TokenKind{},
		true,
		bpDefault,
		true,
	)
}
```

## File: `selector/parser/parse_if.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseIfBody(p *Parser) (ast.Expr, error) {
	return p.parseExpressionsFromTo(lexer.OpenCurly, lexer.CloseCurly, []lexer.TokenKind{}, true, bpDefault)
}

func parseIfCondition(p *Parser) (ast.Expr, error) {
	return p.parseExpressionsFromTo(lexer.OpenParen, lexer.CloseParen, []lexer.TokenKind{}, true, bpDefault)
}

func parseIf(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.If); err != nil {
		return nil, err
	}
	p.advance()

	var exprs []*ast.ConditionalExpr

	process := func(parseCond bool) error {
		var err error
		var cond ast.Expr
		if parseCond {
			cond, err = parseIfCondition(p)
			if err != nil {
				return err
			}
		}

		body, err := parseIfBody(p)
		if err != nil {
			return err
		}

		exprs = append(exprs, &ast.ConditionalExpr{
			Cond: cond,
			Then: body,
		})

		return nil
	}

	if err := process(true); err != nil {
		return nil, err
	}

	for p.current().IsKind(lexer.ElseIf) {
		p.advance()

		if err := process(true); err != nil {
			return nil, err
		}
	}

	if p.current().IsKind(lexer.Else) {
		p.advance()

		body, err := parseIfBody(p)
		if err != nil {
			return nil, err
		}
		exprs[len(exprs)-1].Else = body
	}

	for i := len(exprs) - 1; i >= 0; i-- {
		if i > 0 {
			exprs[i-1].Else = *exprs[i]
		}
	}

	return *exprs[0], nil
}

func (p *Parser) parseExpressionsFromTo(
	from lexer.TokenKind,
	to lexer.TokenKind,
	splitOn []lexer.TokenKind,
	requireExpressions bool,
	bp bindingPower,
) (ast.Expr, error) {
	if err := p.expect(from); err != nil {
		return nil, err
	}
	p.advance()

	t, err := p.parseExpressions(
		[]lexer.TokenKind{to},
		splitOn,
		requireExpressions,
		bp,
		true,
	)
	if err != nil {
		return nil, err
	}

	return t, nil
}
```

## File: `selector/parser/parse_literal.go`
```go
package parser

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"

	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseStringLiteral(p *Parser) (ast.Expr, error) {
	token := p.current()
	p.advance()
	return ast.StringExpr{
		Value: token.Value,
	}, nil
}

func parseBoolLiteral(p *Parser) (ast.Expr, error) {
	token := p.current()
	p.advance()
	return ast.BoolExpr{
		Value: strings.EqualFold(token.Value, "true"),
	}, nil
}

func parseSpread(p *Parser) (ast.Expr, error) {
	p.advance()
	return ast.SpreadExpr{}, nil
}

func parseNumberLiteral(p *Parser) (ast.Expr, error) {
	token := p.current()

	var negative bool
	if token.IsKind(lexer.Dash) {
		negative = true
		token = p.advance()
	}

	next := p.advance()
	switch {
	case next.IsKind(lexer.Symbol) && strings.EqualFold(next.Value, "f"):
		value, err := strconv.ParseFloat(token.Value, 64)
		if err != nil {
			return nil, err
		}
		p.advance()
		if negative {
			value = -value
		}
		return ast.NumberFloatExpr{
			Value: value,
		}, nil

	case strings.Contains(token.Value, "."):
		value, err := strconv.ParseFloat(token.Value, 64)
		if err != nil {
			return nil, err
		}
		if negative {
			value = -value
		}
		return ast.NumberFloatExpr{
			Value: value,
		}, nil

	default:
		value, err := strconv.ParseInt(token.Value, 10, 64)
		if err != nil {
			return nil, err
		}
		if negative {
			value = -value
		}
		return ast.NumberIntExpr{
			Value: value,
		}, nil
	}
}

func parseRegexPattern(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.RegexPattern); err != nil {
		return nil, err
	}

	pattern := p.current()

	p.advance()

	comp, err := regexp.Compile(pattern.Value)
	if err != nil {
		return nil, fmt.Errorf("failed to compile regexp pattern: %w", err)
	}

	return ast.RegexExpr{
		Regex: comp,
	}, nil
}
```

## File: `selector/parser/parse_map.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseMap(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.Map); err != nil {
		return nil, err
	}
	p.advance()

	expr, err := p.parseExpressionsFromTo(
		lexer.OpenParen,
		lexer.CloseParen,
		[]lexer.TokenKind{},
		true,
		bpDefault,
	)
	if err != nil {
		return nil, err
	}

	mapExpr := ast.MapExpr{
		Expr: expr,
	}

	res, err := parseFollowingSymbol(p, mapExpr)
	if err != nil {
		return nil, err
	}

	return res, nil
}
```

## File: `selector/parser/parse_object.go`
```go
package parser

import (
	"fmt"

	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseObject(p *Parser) (ast.Expr, error) {

	//p.parseExpressionsFromTo(
	//	lexer.OpenCurly,
	//	lexer.CloseCurly,
	//	lexer.TokenKinds(lexer.Comma),
	//	false,
	//	bpDefault,
	//)

	if err := p.expect(lexer.OpenCurly); err != nil {
		return nil, err
	}
	p.advance()

	pairs := make([]ast.KeyValue, 0)

	parseKeyValue := func() (ast.KeyValue, error) {
		var res ast.KeyValue
		k, err := p.parseExpression(bpDefault)
		if err != nil {
			return res, err
		}

		// Handle spread
		kSpread, isSpread := ast.LastAsType[ast.SpreadExpr](k)
		if isSpread {
			res.Key = kSpread
			res.Value = ast.RemoveLast(k)
			if err := p.expect(lexer.Comma, lexer.CloseCurly); err != nil {
				return res, err
			}
			return res, nil
		}

		kProp, kIsProp := ast.AsType[ast.PropertyExpr](k)
		if p.current().IsKind(lexer.Comma, lexer.CloseCurly) {
			if !kIsProp {
				return res, fmt.Errorf("invalid shorthand property")
			}
			res.Key = kProp.Property
			res.Value = kProp
			return res, nil
		}

		// Handle unquoted keys
		if kIsProp {
			if kStr, ok := ast.AsType[ast.StringExpr](kProp.Property); ok {
				k = kStr
			}
		}

		if err := p.expect(lexer.Colon); err != nil {
			return res, err
		}
		p.advance()

		v, err := p.parseExpression(bpDefault)
		if err != nil {
			return res, err
		}

		res.Key = k
		res.Value = v
		return res, nil
	}

	for !p.current().IsKind(lexer.CloseCurly) {
		kv, err := parseKeyValue()
		if err != nil {
			return nil, err
		}

		pairs = append(pairs, kv)

		if err := p.expect(lexer.Comma, lexer.CloseCurly); err != nil {
			return nil, fmt.Errorf("expected end of object element: %w", err)
		}
		if p.current().IsKind(lexer.Comma) {
			p.advance()
		}
	}

	if err := p.expect(lexer.CloseCurly); err != nil {
		return nil, fmt.Errorf("expected end of object: %w", err)
	}
	p.advance()

	obj := ast.ObjectExpr{
		Pairs: pairs,
	}

	res, err := parseFollowingSymbol(p, obj)
	if err != nil {
		return nil, err
	}

	return res, nil
}
```

## File: `selector/parser/parse_recursive_descent.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseRecursiveDescent(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.RecursiveDescent); err != nil {
		return nil, err
	}
	p.advance()

	cur := p.current()

	res := ast.RecursiveDescentExpr{}

	var err error
	switch cur.Kind {
	case lexer.Star:
		res.IsWildcard = true
		p.advance()
	case lexer.OpenBracket:
		res.Expr, err = parseIndexSquareBrackets(p, true)
	default:
		res.Expr, err = parseSymbol(p, false, false)
	}

	if err != nil {
		return nil, err
	}

	return res, nil
}
```

## File: `selector/parser/parse_search.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseSearch(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.Search); err != nil {
		return nil, err
	}
	p.advance()

	expr, err := p.parseExpressionsFromTo(
		lexer.OpenParen,
		lexer.CloseParen,
		[]lexer.TokenKind{},
		true,
		bpDefault,
	)
	if err != nil {
		return nil, err
	}

	return ast.SearchExpr{
		Expr: expr,
	}, nil
}
```

## File: `selector/parser/parse_sort_by.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

func parseSortBy(p *Parser) (ast.Expr, error) {
	if err := p.expect(lexer.SortBy); err != nil {
		return nil, err
	}
	p.advance()

	if err := p.expect(lexer.OpenParen); err != nil {
		return nil, err
	}
	p.advance()

	sortExpr, err := p.parseExpressions(
		lexer.TokenKinds(lexer.CloseParen, lexer.Comma),
		nil,
		true,
		bpDefault,
		false,
	)
	if err != nil {
		return nil, err
	}

	res := ast.SortByExpr{
		Expr:       sortExpr,
		Descending: false,
	}

	if p.current().IsKind(lexer.CloseParen) {
		p.advance()
		return res, nil
	}

	if err := p.expect(lexer.Comma); err != nil {
		return nil, err
	}
	p.advance()

	if err := p.expect(lexer.Asc, lexer.Desc); err != nil {
		return nil, err
	}

	if p.current().IsKind(lexer.Desc) {
		res.Descending = true
	}

	p.advance()
	if err := p.expect(lexer.CloseParen); err != nil {
		return nil, err
	}
	p.advance()

	return res, nil
}
```

## File: `selector/parser/parse_symbol.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
	"github.com/tomwright/dasel/v3/selector/lexer"
)

// parseFollowingSymbols deals with the expressions following symbols/variables, e.g.
// $this[0][1]['name']
// foo['bar']['baz'][1]
func parseFollowingSymbol(p *Parser, prev ast.Expr) (ast.Expr, error) {
	res := ast.Expressions{prev}

	for p.hasToken() {
		if p.current().IsKind(lexer.Spread) {
			p.advanceN(1)
			res = append(res, ast.SpreadExpr{})
			continue
		}

		// String based indexes
		if p.current().IsKind(lexer.OpenBracket) {

			if p.peekN(1).IsKind(lexer.Spread) && p.peekN(2).IsKind(lexer.CloseBracket) {
				p.advanceN(3)
				res = append(res, ast.SpreadExpr{})
				continue
			}

			if p.peekN(1).IsKind(lexer.Star) && p.peekN(2).IsKind(lexer.CloseBracket) {
				p.advanceN(3)
				res = append(res, ast.SpreadExpr{})
				continue
			}

			e, err := parseIndexSquareBrackets(p, false)
			if err != nil {
				return nil, err
			}
			switch ex := e.(type) {
			case ast.RangeExpr:
				res = append(res, ex)
			case ast.IndexExpr:
				// Convert this to a property expr. This property executor deals
				// with maps + arrays.
				res = append(res, ast.PropertyExpr{
					Property: ex.Index,
				})
			}

			//e, err := p.parseExpressionsFromTo(lexer.OpenBracket, lexer.CloseBracket, nil, true, bpDefault)
			//if err != nil {
			//	return nil, err
			//}
			//res = append(res, ast.PropertyExpr{
			//	Property: e,
			//})
			continue
		}

		break
	}

	return ast.ChainExprs(res...), nil
}

func parseSymbol(p *Parser, withFollowing bool, allowFunc bool) (ast.Expr, error) {
	token := p.current()

	next := p.peek()

	// Handle functions
	if next.IsKind(lexer.OpenParen) && allowFunc {
		return parseFunc(p)
	}

	prop := ast.PropertyExpr{
		Property: ast.StringExpr{Value: token.Value},
	}

	p.advance()

	if withFollowing {
		res, err := parseFollowingSymbol(p, prop)
		if err != nil {
			return nil, err
		}
		return res, nil
	}

	return prop, nil
}
```

## File: `selector/parser/parse_variable.go`
```go
package parser

import (
	"github.com/tomwright/dasel/v3/selector/ast"
)

func parseVariable(p *Parser) (ast.Expr, error) {
	token := p.current()

	prop := ast.VariableExpr{
		Name: token.Value,
	}

	p.advance()

	res, err := parseFollowingSymbol(p, prop)
	if err != nil {
		return nil, err
	}

	return res, nil
}
```

