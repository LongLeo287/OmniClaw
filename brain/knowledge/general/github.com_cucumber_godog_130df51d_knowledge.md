---
id: github.com-cucumber-godog-130df51d-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:42.544803
---

# KNOWLEDGE EXTRACT: github.com_cucumber_godog_130df51d
> **Extracted on:** 2026-04-01 15:45:06
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524738/github.com_cucumber_godog_130df51d

---

## File: `.gitignore`
```
/cmd/godog/godog
/example/example
**/vendor/*
Gopkg.lock
Gopkg.toml

.DS_Store
.idea
.vscode

_artifacts

vendor
```

## File: `CHANGELOG.md`
```markdown
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
- Added concurrency support to the events formatter ([274](https://github.com/cucumber/godog/pull/274) - [lonnblad](https://github.com/lonnblad))
- Added concurrency support to the cucumber formatter ([273](https://github.com/cucumber/godog/pull/273) - [lonnblad](https://github.com/lonnblad))
- Added an example for how to use assertion pkgs like testify with godog ([289](https://github.com/cucumber/godog/pull/289) - [lonnblad](https://github.com/lonnblad))
- Added the new TestSuiteInitializer and ScenarioInitializer ([294](https://github.com/cucumber/godog/pull/294) - [lonnblad](https://github.com/lonnblad))
- Added an in-mem storage for pickles ([304](https://github.com/cucumber/godog/pull/304) - [lonnblad](https://github.com/lonnblad))
- Added Pickle and PickleStep results to the in-mem storage ([305](https://github.com/cucumber/godog/pull/305) - [lonnblad](https://github.com/lonnblad))
- Added features to the in-mem storage ([306](https://github.com/cucumber/godog/pull/306) - [lonnblad](https://github.com/lonnblad))
- Broke out some code from massive files into new files ([307](https://github.com/cucumber/godog/pull/307) - [lonnblad](https://github.com/lonnblad))
- Added support for concurrent scenarios ([311](https://github.com/cucumber/godog/pull/311) - [lonnblad](https://github.com/lonnblad))

### Changed
- Broke out snippets gen and added sorting on method name ([271](https://github.com/cucumber/godog/pull/271) - [lonnblad](https://github.com/lonnblad))
- Updated so that we run all tests concurrent now ([278](https://github.com/cucumber/godog/pull/278) - [lonnblad](https://github.com/lonnblad))
- Moved fmt tests to a godog_test pkg and restructured the fmt output tests ([295](https://github.com/cucumber/godog/pull/295) - [lonnblad](https://github.com/lonnblad))
- Moved builder tests to a godog_test pkg ([296](https://github.com/cucumber/godog/pull/296) - [lonnblad](https://github.com/lonnblad))
- Made the builder tests run in parallel ([298](https://github.com/cucumber/godog/pull/298) - [lonnblad](https://github.com/lonnblad))
- Refactored suite_context.go ([300](https://github.com/cucumber/godog/pull/300) - [lonnblad](https://github.com/lonnblad))
- Added better testing of the Context Initializers and TestSuite{}.Run() ([301](https://github.com/cucumber/godog/pull/301) - [lonnblad](https://github.com/lonnblad))
- Updated the README.md ([302](https://github.com/cucumber/godog/pull/302) - [lonnblad](https://github.com/lonnblad))
- Unexported some exported properties in unexported structs ([303](https://github.com/cucumber/godog/pull/303) - [lonnblad](https://github.com/lonnblad))
- Refactored some states in the formatters and feature struct ([310](https://github.com/cucumber/godog/pull/310) - [lonnblad](https://github.com/lonnblad))

### Deprecated
- Deprecated SuiteContext and ConcurrentFormatter ([314](https://github.com/cucumber/godog/pull/314) - [lonnblad](https://github.com/lonnblad))

### Fixed
- Fixed failing builder tests due to the v0.9.0 change ([lonnblad](https://github.com/lonnblad))
- Update paths to screenshots for examples ([270](https://github.com/cucumber/godog/pull/270) - [leviable](https://github.com/leviable))
- Made progress formatter verification a bit more accurate ([lonnblad](https://github.com/lonnblad))
- Added comparison between single and multi threaded runs ([272](https://github.com/cucumber/godog/pull/272) - [lonnblad](https://github.com/lonnblad))
- Fixed issue with empty feature file causing nil pointer deref ([288](https://github.com/cucumber/godog/pull/288) - [lonnblad](https://github.com/lonnblad))
- Updated linting checks in circleci config and fixed linting issues ([290](https://github.com/cucumber/godog/pull/290) - [lonnblad](https://github.com/lonnblad))
- Readded some legacy doc for FeatureContext ([297](https://github.com/cucumber/godog/pull/297) - [lonnblad](https://github.com/lonnblad))
- Fixed an issue with calculating time for junit testsuite ([308](https://github.com/cucumber/godog/pull/308) - [lonnblad](https://github.com/lonnblad))
- Fixed so that we don't execute features with zero scenarios ([315](https://github.com/cucumber/godog/pull/315) - [lonnblad](https://github.com/lonnblad))
- Fixed the broken --random flag ([317](https://github.com/cucumber/godog/pull/317) - [lonnblad](https://github.com/lonnblad))

### Removed
- Removed pre go112 build code ([293](https://github.com/cucumber/godog/pull/293) - [lonnblad](https://github.com/lonnblad))
- Removed the deprecated feature hooks ([312](https://github.com/cucumber/godog/pull/312) - [lonnblad](https://github.com/lonnblad))

## [0.9.0]
### Changed
- Run godog features in CircleCI in strict mode ([mxygem](https://github.com/mxygem))
- Removed TestMain call in `suite_test.go` for CI. ([mxygem](https://github.com/mxygem))
- Migrated to [gherkin-go - v11.0.0](https://github.com/cucumber/gherkin-go/releases/tag/v11.0.0). ([240](https://github.com/cucumber/godog/pull/240) - [lonnblad](https://github.com/lonnblad))

### Fixed
- Fixed the time attributes in the JUnit formatter. ([232](https://github.com/cucumber/godog/pull/232) - [lonnblad](https://github.com/lonnblad))
- Re enable custom formatters. ([238](https://github.com/cucumber/godog/pull/238) - [ericmcbride](https://github.com/ericmcbride))
- Added back suite_test.go ([mxygem](https://github.com/mxygem))
- Normalise module paths for use on Windows ([242](https://github.com/cucumber/godog/pull/242) - [gjtaylor](https://github.com/gjtaylor))
- Fixed panic in indenting function `s` ([247](https://github.com/cucumber/godog/pull/247) - [titouanfreville](https://github.com/titouanfreville))
- Fixed wrong version in API example ([263](https://github.com/cucumber/godog/pull/263) - [denis-trofimov](https://github.com/denis-trofimov))

## [0.8.1]
### Added
- Link in Readme to the Slack community. ([210](https://github.com/cucumber/godog/pull/210) - [smikulcik](https://github.com/smikulcik))
- Added run tests for Cucumber formatting. ([214](https://github.com/cucumber/godog/pull/214), [216](https://github.com/cucumber/godog/pull/216) - [lonnblad](https://github.com/lonnblad))

### Changed
- Renamed the `examples` directory to `_examples`, removing dependencies from the Go module ([218](https://github.com/cucumber/godog/pull/218) - [axw](https://github.com/axw))

### Fixed
- Find/Replaced references to DATA-DOG/godog -> cucumber/godog for docs. ([209](https://github.com/cucumber/godog/pull/209) - [smikulcik](https://github.com/smikulcik))
- Fixed missing links in changelog to be correctly included! ([mxygem](https://github.com/mxygem))

## [0.8.0]
### Added
- Added initial CircleCI config. ([mxygem](https://github.com/mxygem))
- Added concurrency support for JUnit formatting ([lonnblad](https://github.com/lonnblad))

### Changed
- Changed code references to DATA-DOG/godog to cucumber/godog to help get things building correctly. ([mxygem](https://github.com/mxygem))

[v0.15.1]: https://github.com/cucumber/godog/compare/v0.15.0...v0.15.1
[v0.15.0]: https://github.com/cucumber/godog/compare/v0.14.1...v0.15.0
[v0.14.1]: https://github.com/cucumber/godog/compare/v0.14.0...v0.14.1
[v0.14.0]: https://github.com/cucumber/godog/compare/v0.13.0...v0.14.0
[v0.13.0]: https://github.com/cucumber/godog/compare/v0.12.6...v0.13.0
[v0.12.6]: https://github.com/cucumber/godog/compare/v0.12.5...v0.12.6
[v0.12.5]: https://github.com/cucumber/godog/compare/v0.12.4...v0.12.5
[v0.12.4]: https://github.com/cucumber/godog/compare/v0.12.3...v0.12.4
[v0.12.3]: https://github.com/cucumber/godog/compare/v0.12.2...v0.12.3
[v0.12.2]: https://github.com/cucumber/godog/compare/v0.12.1...v0.12.2
[v0.12.1]: https://github.com/cucumber/godog/compare/v0.12.0...v0.12.1
[v0.12.0]: https://github.com/cucumber/godog/compare/v0.11.0...v0.12.0
[v0.11.0]: https://github.com/cucumber/godog/compare/v0.10.0...v0.11.0
[v0.10.0]: https://github.com/cucumber/godog/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/cucumber/godog/compare/v0.8.1...v0.9.0
[0.8.1]: https://github.com/cucumber/godog/compare/v0.8.0...v0.8.1
[0.8.0]: https://github.com/cucumber/godog/compare/v0.7.13...v0.8.0
```

## File: `CHANGELOG_OLD.md`
```markdown
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

## File: `CONTRIBUTING.md`
```markdown
# Welcome 💖

Before anything else, thank you for taking some of your precious time to help this project move forward. ❤️

If you're new to open source and feeling a bit nervous 😳, we understand! We recommend watching [this excellent guide](https://egghead.io/talks/git-how-to-make-your-first-open-source-contribution)
to give you a grounding in some of the basic concepts. You could also watch [this talk](https://www.youtube.com/watch?v=tuSk6dMoTIs) from our very own wonderful [Marit van Dijk](https://github.com/mlvandijk) on her experiences contributing to Cucumber.

We want you to feel safe to make mistakes, and ask questions. If anything in this guide or anywhere else in the codebase doesn't make sense to you, please let us know! It's through your feedback that we can make this codebase more welcoming, so we'll be glad to hear thoughts.

You can chat with us in the `#committers` channel in our [community Discord](https://cucumber.io/brain/knowledge/docs_legacy/community/get-in-touch/#discord), or feel free to [raise an issue] if you're experiencing any friction trying make your contribution.

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

## File: `LICENSE`
```
The MIT License (MIT)

Copyright (c) SmartBear

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

## File: `Makefile`
```
.PHONY: test gherkin bump cover

VERS ?= $(shell git symbolic-ref -q --short HEAD || git describe --tags --exact-match)

GO_MAJOR_VERSION = $(shell go version | cut -c 14- | cut -d' ' -f1 | cut -d'.' -f1)
GO_MINOR_VERSION = $(shell go version | cut -c 14- | cut -d' ' -f1 | cut -d'.' -f2)
MINIMUM_SUPPORTED_GO_MAJOR_VERSION = 1
MINIMUM_SUPPORTED_GO_MINOR_VERSION = 16
GO_VERSION_VALIDATION_ERR_MSG = Go version $(GO_MAJOR_VERSION).$(GO_MINOR_VERSION) is not supported, please update to at least $(MINIMUM_SUPPORTED_GO_MAJOR_VERSION).$(MINIMUM_SUPPORTED_GO_MINOR_VERSION)

.PHONY: check-go-version
check-go-version:
	@if [ $(GO_MAJOR_VERSION) -gt $(MINIMUM_SUPPORTED_GO_MAJOR_VERSION) ]; then \
		exit 0 ;\
	elif [ $(GO_MAJOR_VERSION) -lt $(MINIMUM_SUPPORTED_GO_MAJOR_VERSION) ]; then \
		echo '$(GO_VERSION_VALIDATION_ERR_MSG)';\
		exit 1; \
	elif [ $(GO_MINOR_VERSION) -lt $(MINIMUM_SUPPORTED_GO_MINOR_VERSION) ] ; then \
		echo '$(GO_VERSION_VALIDATION_ERR_MSG)';\
		exit 1; \
	fi

test: check-go-version
	@echo "running all tests"
	@go fmt ./...
	@go run honnef.co/go/tools/cmd/staticcheck@v0.5.1 github.com/cucumber/godog
	@go run honnef.co/go/tools/cmd/staticcheck@v0.5.1 github.com/cucumber/godog/cmd/godog
	go vet ./...
	go test -race ./...
	go run ./cmd/godog -f progress -c 4

gherkin:
	@if [ -z "$(VERS)" ]; then echo "Provide gherkin version like: 'VERS=commit-hash'"; exit 1; fi
	@rm -rf gherkin
	@mkdir gherkin
	@curl -s -L https://github.com/cucumber/gherkin-go/tarball/$(VERS) | tar -C gherkin -zx --strip-components 1
	@rm -rf gherkin/{.travis.yml,.gitignore,*_test.go,gherkin-generate*,*.razor,*.jq,Makefile,CONTRIBUTING.md}

bump:
	@if [ -z "$(VERSION)" ]; then echo "Provide version like: 'VERSION=$(VERS) make bump'"; exit 1; fi
	@echo "bumping version from: $(VERS) to $(VERSION)"
	@sed -i.bak 's/$(VERS)/$(VERSION)/g' godog.go
	@sed -i.bak 's/$(VERS)/$(VERSION)/g' _examples/api/features/version.feature
	@find . -name '*.bak' | xargs rm

cover:
	go test -race -coverprofile=coverage.txt
	go tool cover -html=coverage.txt
	rm coverage.txt

ARTIFACT_DIR := _artifacts

# To upload artifacts for the current version;
# execute: make upload
#
# Check https://github.com/tcnksm/ghr for usage of ghr
upload: artifacts
	ghr -replace $(VERS) $(ARTIFACT_DIR)

# To build artifacts for the current version;
# execute: make artifacts
artifacts: 
	rm -rf $(ARTIFACT_DIR)
	mkdir $(ARTIFACT_DIR)

	$(call _build,darwin,amd64)
	$(call _build,linux,amd64)
	$(call _build,linux,arm64)

define _build
	mkdir $(ARTIFACT_DIR)/godog-$(VERS)-$1-$2
	env GOOS=$1 GOARCH=$2 go build -ldflags "-X github.com/cucumber/godog.Version=$(VERS)" -o $(ARTIFACT_DIR)/godog-$(VERS)-$1-$2/godog ./cmd/godog
	cp README.md $(ARTIFACT_DIR)/godog-$(VERS)-$1-$2/README.md
	cp LICENSE $(ARTIFACT_DIR)/godog-$(VERS)-$1-$2/LICENSE
	cd $(ARTIFACT_DIR) && tar -c --use-compress-program="pigz --fast" -f godog-$(VERS)-$1-$2.tar.gz godog-$(VERS)-$1-$2 && cd ..
	rm -rf $(ARTIFACT_DIR)/godog-$(VERS)-$1-$2
endef
```

## File: `README.md`
```markdown
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
- [Behaviour-Driven Development](https://cucumber.io/brain/knowledge/docs_legacy/bdd/)
- [Gherkin Reference](https://cucumber.io/brain/knowledge/docs_legacy/gherkin/reference/)

## Contributions

Godog is a community driven Open Source Project within the Cucumber organization. We [welcome contributions from everyone](https://cucumber.io/blog/open-source/tackling-structural-racism-(and-sexism)-in-open-so/), and we're ready to support you if you have the enthusiasm to contribute.

See the [contributing guide] for more detail on how to get started.

See the [releasing guide] for release flow details.

## Getting help

We have a [community Discord](https://cucumber.io/brain/knowledge/docs_legacy/community/get-in-touch/#discord) where you can chat with other users, developers, and BDD practitioners.

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
		Paths:     []string{"features"},
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

Now when running `go test -v` it will use **pretty** format.

### Tags

If you want to filter scenarios by tags, you can use the `-t=<expression>` or `--tags=<expression>` where `<expression>` is one of the following:

- `@wip` - run all scenarios with wip tag
- `~@wip` - exclude all scenarios with wip tag
- `@wip && ~@new` - run wip scenarios, but exclude new
- `@wip,@undone` - run wip or undone scenarios

### Using assertion packages like testify with Godog
A more extensive example can be [found here](/_examples/assert-godogs).

```go
func thereShouldBeRemaining(ctx context.Context, remaining int) error {
	assert.Equal(
    godog.T(ctx), Godogs, remaining, 
    "Expected %d godogs to be remaining, but there is %d", remaining, Godogs,
  )
	return nil
}
```

### Embeds

If you're looking to compile your test binary in advance of running, you can compile the feature files into the binary via `go:embed`:

```go

//go:embed features/*
var features embed.FS

var opts = godog.Options{
	Paths: []string{"features"},
	FS:    features,
}
```

Now, the test binary can be compiled with all feature files embedded, and can be ran independently from the feature files:

```sh
> go test -c ./test/integration/integration_test.go
> mv integration.test /some/random/dir
> cd /some/random/dir
> ./integration.test
```

**NOTE:** `godog.Options.FS` is as `fs.FS`, so custom filesystem loaders can be used.

## CLI Mode

**NOTE:** The [`godog` CLI has been deprecated](https://github.com/cucumber/godog/discussions/478). It is recommended to use `go test` instead.  

Another way to use `godog` is to run it in CLI mode.

In this mode `godog` CLI will use `go` under the hood to compile and run your test suite.

**Godog** does not intervene with the standard **go test** command behavior. You can leverage both frameworks to functionally test your application while maintaining all test related source code in **_test.go** files.

**Godog** acts similar compared to **go test** command, by using go compiler and linker tool in order to produce test executable. Godog contexts need to be exported the same way as **Test** functions for go tests. Note, that if you use **godog** command tool, it will use `go` executable to determine compiler and linker.

### Install
```
go install github.com/cucumber/godog/cmd/godog@latest
```
Adding `@v0.12.0` will install v0.12.0 specifically instead of master.

With `go` version prior to 1.17, use `go get github.com/cucumber/godog/cmd/godog@v0.12.0`.
Running `within the $GOPATH`, you would also need to set `GO111MODULE=on`, like this:
```
GO111MODULE=on go get github.com/cucumber/godog/cmd/godog@v0.12.0
```

### Configure common options for godog CLI

There are no global options or configuration files. Alias your common or project based commands: `alias godog-wip="godog --format=progress --tags=@wip"`

## Concurrency

When concurrency is configured in options, godog will execute the scenarios concurrently, which is supported by all supplied formatters.

In order to support concurrency well, you should reset the state and isolate each scenario. They should not share any state. It is suggested to run the suite concurrently in order to make sure there is no state corruption or race conditions in the application.

It is also useful to randomize the order of scenario execution, which you can now do with `--random` command option or `godog.Options.Randomize` setting.

### Building your own custom formatter
A simple example can be [found here](/_examples/custom-formatter).

## License
**Godog** and **Gherkin** are licensed under the [MIT][license] and developed as a part of the [cucumber project][cucumber]

[godoc]: https://pkg.go.dev/github.com/cucumber/godog "Documentation on godog"
[golang]: https://golang.org/  "GO programming language"
[behat]: http://docs.behat.org/ "Behavior driven development framework for PHP"
[cucumber]: https://cucumber.io/ "Behavior driven development framework"
[license]: https://en.wikipedia.org/wiki/MIT_License "The MIT license"
[contributing guide]: https://github.com/cucumber/godog/blob/main/CONTRIBUTING.md
[releasing guide]: https://github.com/cucumber/godog/blob/main/RELEASING.md
[community Discord]: https://cucumber.io/community#discord



```

## File: `RELEASING.md`
```markdown
# Releasing Guidelines for Cucumber Godog

This document provides guidelines for releasing new versions of Cucumber Godog. Follow these steps to ensure a smooth and consistent release process.

## Versioning

Cucumber Godog follows [Semantic Versioning]. Version numbers are in the format `MAJOR.MINOR.PATCH`.

### Current (for v0.MINOR.PATCH)

- **MINOR**: Incompatible API changes.
- **PATCH**: Backward-compatible new features and bug fixes.

### After v1.X.X release

- **MAJOR**: Incompatible API changes.
- **MINOR**: Backward-compatible new features.
- **PATCH**: Backward-compatible bug fixes.

## Release Process

1. **Update Changelog:**
    - Open `CHANGELOG.md` and add an entry for the upcoming release formatting according to the principles of [Keep A CHANGELOG].
    - Include details about new features, enhancements, and bug fixes.

2. **Run Tests:**
    - Run the test suite to ensure all existing features are working as expected.

3. **Manual Testing for Backwards Compatibility:**
    - Manually test the new release with external libraries that depend on Cucumber Godog.
    - Look for any potential backwards compatibility issues, especially with widely-used libraries.
    - Address any identified issues before proceeding.

4. **Create Release on GitHub:**
    - Go to the [Releases] page on GitHub.
    - Click on "Draft a new release."
    - Tag version should be set to the new tag vMAJOR.MINOR.PATCH
    - Title the release using the version number (e.g., "vMAJOR.MINOR.PATCH").
    - Click 'Generate release notes'

5. **Publish Release:**
    - Click "Publish release" to make the release public.

6. **Announce the Release:**
    - Make an announcement on relevant communication channels (e.g., [community Discord]) about the new release.

## Additional Considerations

- **Documentation:**
    - Update the project documentation on the [website], if applicable.

- **Deprecation Notices:**
    - If any features are deprecated, clearly document them in the release notes and provide guidance on migration.

- **Compatibility:**
    - Clearly state any compatibility requirements or changes in the release notes.

- **Feedback:**
    - Encourage users to provide feedback and report any issues with the new release.

Following these guidelines, including manual testing with external libraries, will help ensure a thorough release process for Cucumber Godog, allowing detection and resolution of potential backwards compatibility issues before tagging the release.

[community Discord]: https://cucumber.io/community#discord
[website]: https://cucumber.github.io/godog/
[Releases]: https://github.com/cucumber/godog/releases
[Semantic Versioning]: http://semver.org
[Keep A CHANGELOG]: http://keepachangelog.com
```

## File: `attachment_test.go`
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

## File: `codecov.yml`
```yaml
coverage:
  status:
    project:
      default:
        threshold: 0.5%
    patch:
      default:
        threshold: 0.5%
```

## File: `example_subtests_test.go`
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

## File: `flags.go`
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

## File: `flags_test.go`
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

## File: `flags_v0110.go`
```go
package godog

import (
	"errors"
	"flag"
	"math/rand"
	"time"

	"github.com/spf13/pflag"

	"github.com/cucumber/godog/internal/flags"
)

// Choose randomly assigns a convenient pseudo-random seed value.
// The resulting seed will be between `1-99999` for later ease of specification.
func makeRandomSeed() int64 {
	return rand.New(rand.NewSource(time.Now().UTC().UnixNano())).Int63n(99998) + 1
}

func flagSet(opt *Options) *pflag.FlagSet {
	set := pflag.NewFlagSet("godog", pflag.ExitOnError)
	flags.BindRunCmdFlags("", set, opt)
	pflag.ErrHelp = errors.New("godog: help requested")
	return set
}

// BindCommandLineFlags binds godog flags to given flag set prefixed
// by given prefix, without overriding usage
func BindCommandLineFlags(prefix string, opts *Options) {
	flagSet := pflag.CommandLine
	flags.BindRunCmdFlags(prefix, flagSet, opts)
	pflag.CommandLine.AddGoFlagSet(flag.CommandLine)
}
```

## File: `flags_v0110_test.go`
```go
package godog

import (
	"testing"

	"github.com/cucumber/godog/internal/flags"
	"github.com/stretchr/testify/assert"
)

func Test_BindFlagsShouldRespectFlagDefaults(t *testing.T) {
	opts := flags.Options{}

	BindCommandLineFlags("flagDefaults.", &opts)

	assert.Equal(t, "pretty", opts.Format)
	assert.Equal(t, "", opts.Tags)
	assert.Equal(t, 1, opts.Concurrency)
	assert.False(t, opts.ShowStepDefinitions)
	assert.False(t, opts.StopOnFailure)
	assert.False(t, opts.Strict)
	assert.False(t, opts.NoColors)
	assert.Equal(t, int64(0), opts.Randomize)
}
```

## File: `fmt.go`
```go
package godog

import (
	"fmt"
	"io"
	"strings"
	"unicode/utf8"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/formatters"
	internal_fmt "github.com/cucumber/godog/internal/formatters"
	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/storage"
)

// FindFmt searches available formatters registered
// and returns FormaterFunc matched by given
// format name or nil otherwise
func FindFmt(name string) FormatterFunc {
	return formatters.FindFmt(name)
}

// Format registers a feature suite output
// formatter by given name, description and
// FormatterFunc constructor function, to initialize
// formatter with the output recorder.
func Format(name, description string, f FormatterFunc) {
	formatters.Format(name, description, f)
}

// AvailableFormatters gives a map of all
// formatters registered with their name as key
// and description as value
func AvailableFormatters() map[string]string {
	return formatters.AvailableFormatters()
}

// Formatter is an interface for feature runner
// output summary presentation.
//
// New formatters may be created to represent
// suite results in different ways. These new
// formatters needs to be registered with a
// godog.Format function call
type Formatter = formatters.Formatter

type storageFormatter interface {
	SetStorage(*storage.Storage)
}

// FormatterFunc builds a formatter with given
// suite name and io.Writer to record output
type FormatterFunc = formatters.FormatterFunc

func printStepDefinitions(steps []*models.StepDefinition, w io.Writer) {
	var longest int
	for _, def := range steps {
		n := utf8.RuneCountInString(def.Expr.String())
		if longest < n {
			longest = n
		}
	}

	for _, def := range steps {
		n := utf8.RuneCountInString(def.Expr.String())
		location := internal_fmt.DefinitionID(def)
		spaces := strings.Repeat(" ", longest-n)
		fmt.Fprintln(w,
			colors.Yellow(def.Expr.String())+spaces,
			colors.Bold(colors.Black)("# "+location))
	}

	if len(steps) == 0 {
		fmt.Fprintln(w, "there were no contexts registered, could not find any step definition..")
	}
}

// NewBaseFmt creates a new base formatter.
func NewBaseFmt(suite string, out io.Writer) *BaseFmt {
	return internal_fmt.NewBase(suite, out)
}

// NewProgressFmt creates a new progress formatter.
func NewProgressFmt(suite string, out io.Writer) *ProgressFmt {
	return internal_fmt.NewProgress(suite, out)
}

// NewPrettyFmt creates a new pretty formatter.
func NewPrettyFmt(suite string, out io.Writer) *PrettyFmt {
	return &PrettyFmt{Base: NewBaseFmt(suite, out)}
}

// NewEventsFmt creates a new event streaming formatter.
func NewEventsFmt(suite string, out io.Writer) *EventsFmt {
	return &EventsFmt{Base: NewBaseFmt(suite, out)}
}

// NewCukeFmt creates a new Cucumber JSON formatter.
func NewCukeFmt(suite string, out io.Writer) *CukeFmt {
	return &CukeFmt{Base: NewBaseFmt(suite, out)}
}

// NewJUnitFmt creates a new JUnit formatter.
func NewJUnitFmt(suite string, out io.Writer) *JUnitFmt {
	return &JUnitFmt{Base: NewBaseFmt(suite, out)}
}

// BaseFmt exports Base formatter.
type BaseFmt = internal_fmt.Base

// ProgressFmt exports Progress formatter.
type ProgressFmt = internal_fmt.Progress

// PrettyFmt exports Pretty formatter.
type PrettyFmt = internal_fmt.Pretty

// EventsFmt exports Events formatter.
type EventsFmt = internal_fmt.Events

// CukeFmt exports Cucumber JSON formatter.
type CukeFmt = internal_fmt.Cuke

// JUnitFmt exports JUnit formatter.
type JUnitFmt = internal_fmt.JUnit
```

## File: `fmt_test.go`
```go
package godog_test

import (
	"io"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/cucumber/godog"
)

func Test_FindFmt(t *testing.T) {
	cases := map[string]bool{
		"cucumber": true,
		"custom":   true, // is available for test purposes only
		"events":   true,
		"junit":    true,
		"pretty":   true,
		"progress": true,
		"unknown":  false,
		"undef":    false,
	}

	for name, expected := range cases {
		t.Run(
			name,
			func(t *testing.T) {
				actual := godog.FindFmt(name)

				if expected {
					assert.NotNilf(t, actual, "expected %s formatter should be available", name)
				} else {
					assert.Nilf(t, actual, "expected %s formatter should be available", name)
				}
			},
		)
	}
}

func Test_AvailableFormatters(t *testing.T) {
	expected := map[string]string{
		"cucumber": "Produces cucumber JSON format output.",
		"custom":   "custom format description", // is available for test purposes only
		"events":   "Produces JSON event stream, based on spec: 0.1.0.",
		"junit":    "Prints junit compatible xml to stdout",
		"pretty":   "Prints every feature with runtime statuses.",
		"progress": "Prints a character per step.",
	}

	actual := godog.AvailableFormatters()
	assert.Equal(t, expected, actual)
}

func Test_Format(t *testing.T) {
	actual := godog.FindFmt("Test_Format")
	require.Nil(t, actual)

	godog.Format("Test_Format", "...", testFormatterFunc)
	actual = godog.FindFmt("Test_Format")

	assert.NotNil(t, actual)
}

func testFormatterFunc(suiteName string, out io.Writer) godog.Formatter {
	return nil
}
```

## File: `go.mod`
```
module github.com/cucumber/godog

go 1.16

require (
	github.com/cucumber/gherkin/go/v26 v26.2.0
	github.com/hashicorp/go-memdb v1.3.4
	github.com/spf13/cobra v1.7.0
	github.com/spf13/pflag v1.0.10
	github.com/stretchr/testify v1.8.2
)

require (
	github.com/cucumber/messages/go/v21 v21.0.1
	github.com/hashicorp/go-immutable-radix v1.3.1 // indirect
	github.com/hashicorp/go-uuid v1.0.2 // indirect
	gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c // indirect
)
```

## File: `go.sum`
```
github.com/cpuguy83/go-md2man/v2 v2.0.2/go.mod h1:tgQtvFlXSQOSOSIRvRPT7W67SCa46tRHOmNcaadrF8o=
github.com/cucumber/gherkin/go/v26 v26.2.0 h1:EgIjePLWiPeslwIWmNQ3XHcypPsWAHoMCz/YEBKP4GI=
github.com/cucumber/gherkin/go/v26 v26.2.0/go.mod h1:t2GAPnB8maCT4lkHL99BDCVNzCh1d7dBhCLt150Nr/0=
github.com/cucumber/messages/go/v21 v21.0.1 h1:wzA0LxwjlWQYZd32VTlAVDTkW6inOFmSM+RuOwHZiMI=
github.com/cucumber/messages/go/v21 v21.0.1/go.mod h1:zheH/2HS9JLVFukdrsPWoPdmUtmYQAQPLk7w5vWsk5s=
github.com/cucumber/messages/go/v22 v22.0.0/go.mod h1:aZipXTKc0JnjCsXrJnuZpWhtay93k7Rn3Dee7iyPJjs=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/gofrs/uuid v4.2.0+incompatible/go.mod h1:b2aQJv3Z4Fp6yNu3cdSllBxTCLRxnplIgP/c0N/04lM=
github.com/gofrs/uuid v4.3.1+incompatible h1:0/KbAdpx3UXAx1kEOWHJeOkpbgRFGHVgv+CFIY7dBJI=
github.com/gofrs/uuid v4.3.1+incompatible/go.mod h1:b2aQJv3Z4Fp6yNu3cdSllBxTCLRxnplIgP/c0N/04lM=
github.com/hashicorp/go-immutable-radix v1.3.0/go.mod h1:0y9vanUI8NX6FsYoO3zeMjhV/C5i9g4Q3DwcSNZ4P60=
github.com/hashicorp/go-immutable-radix v1.3.1 h1:DKHmCUm2hRBK510BaiZlwvpD40f8bJFeZnpfm2KLowc=
github.com/hashicorp/go-immutable-radix v1.3.1/go.mod h1:0y9vanUI8NX6FsYoO3zeMjhV/C5i9g4Q3DwcSNZ4P60=
github.com/hashicorp/go-memdb v1.3.4 h1:XSL3NR682X/cVk2IeV0d70N4DZ9ljI885xAEU8IoK3c=
github.com/hashicorp/go-memdb v1.3.4/go.mod h1:uBTr1oQbtuMgd1SSGoR8YV27eT3sBHbYiNm53bMpgSg=
github.com/hashicorp/go-uuid v1.0.0/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/go-uuid v1.0.2 h1:cfejS+Tpcp13yd5nYHWDI6qVCny6wyX2Mt5SGur2IGE=
github.com/hashicorp/go-uuid v1.0.2/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/golang-lru v0.5.0/go.mod h1:/m3WP610KZHVQ1SGc6re/UDhFvYD7pJ4Ao+sR/qLZy8=
github.com/hashicorp/golang-lru v0.5.4 h1:YDjusn29QI/Das2iO9M0BHnIbxPeyuCHsjMW+lJfyTc=
github.com/hashicorp/golang-lru v0.5.4/go.mod h1:iADmTwqILo4mZ8BN3D2Q6+9jd8WM5uGBxy+E8yxSoD4=
github.com/inconshreveable/mousetrap v1.1.0 h1:wN+x4NVGpMsO7ErUn/mUI3vEoE6Jt13X2s0bqwp9tc8=
github.com/inconshreveable/mousetrap v1.1.0/go.mod h1:vpF70FUmC8bwa3OWnCshd2FqLfsEA9PFc4w1p2J65bw=
github.com/kr/pretty v0.2.1 h1:Fmg33tUaq4/8ym9TJN1x7sLJnHVwhP33CNkpYV/7rwI=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/russross/blackfriday/v2 v2.1.0/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/spf13/cobra v1.7.0 h1:hyqWnYt1ZQShIddO5kBpj3vu05/++x6tJ6dg8EC572I=
github.com/spf13/cobra v1.7.0/go.mod h1:uLxZILRyS/50WlhOIKD7W6V5bgeIt+4sICxh6uRMrb0=
github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/pflag v1.0.7 h1:vN6T9TfwStFPFM5XzjsvmzZkLuaLX+HS+0SeFLRgU6M=
github.com/spf13/pflag v1.0.7/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/pflag v1.0.9 h1:9exaQaMOCwffKiiiYk6/BndUBv+iRViNW+4lEMi0PvY=
github.com/spf13/pflag v1.0.9/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/pflag v1.0.10 h1:4EBh2KAYBwaONj6b2Ye1GiHfwjqyROoF4RwYO+vPwFk=
github.com/spf13/pflag v1.0.10/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.4.0/go.mod h1:YvHI0jy2hoMjB+UWwv71VJQ9isScKT/TqJzVSSt89Yw=
github.com/stretchr/objx v0.5.0/go.mod h1:Yh+to48EsGEfYuaHDzXPcE3xhTkx73EhmCGUpEOglKo=
github.com/stretchr/testify v1.7.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.8.0/go.mod h1:yNjHg4UonilssWZ8iaSj1OCr/vHnekPRkoO+kdMU+MU=
github.com/stretchr/testify v1.8.1/go.mod h1:w2LPCIKwWwSfY2zedu0+kehJoqGctiVI29o6fzry7u4=
github.com/stretchr/testify v1.8.2 h1:+h33VjcLVPDHtOdpUCuF+7gSuG3yGIftsP1YvFihtJ8=
github.com/stretchr/testify v1.8.2/go.mod h1:w2LPCIKwWwSfY2zedu0+kehJoqGctiVI29o6fzry7u4=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `godog.go`
```go
/*
Package godog is the official Cucumber BDD framework for Golang, it merges specification
and test documentation into one cohesive whole.

Godog does not intervene with the standard "go test" command and it's behavior.
You can leverage both frameworks to functionally test your application while
maintaining all test related source code in *_test.go files.

Godog acts similar compared to go test command. It uses go
compiler and linker tool in order to produce test executable. Godog
contexts needs to be exported same as Test functions for go test.

For example, imagine you're about to create the famous UNIX ls command.
Before you begin, you describe how the feature should work, see the example below..

Example:

	Feature: ls
	  In order to see the directory structure
	  As a UNIX user
	  I need to be able to list the current directory's contents

	  Scenario:
		Given I am in a directory "test"
		And I have a file named "foo"
		And I have a file named "bar"
		When I run ls
		Then I should get output:
		  """
		  bar
		  foo
		  """

Now, wouldn't it be cool if something could read this sentence and use it to actually
run a test against the ls command? Hey, that's exactly what this package does!
As you'll see, Godog is easy to learn, quick to use, and will put the fun back into tests.

Godog was inspired by Behat and Cucumber the above description is taken from it's documentation.
*/
package godog

// Version of package - based on Semantic Versioning 2.0.0 http://semver.org/
var Version = "v0.0.0-dev"
```

## File: `mod_version.go`
```go
//go:build go1.12
// +build go1.12

package godog

import (
	"runtime/debug"
)

func init() {
	if info, available := debug.ReadBuildInfo(); available {
		if Version == "v0.0.0-dev" && info.Main.Version != "(devel)" {
			Version = info.Main.Version
		}
	}
}
```

## File: `options.go`
```go
package godog

import "github.com/cucumber/godog/internal/flags"

// Options are suite run options
// flags are mapped to these options.
//
// It can also be used together with godog.RunWithOptions
// to run test suite from go source directly
//
// See the flags for more details
type Options = flags.Options
```

## File: `run.go`
```go
package godog

import (
	"context"
	"flag"
	"fmt"
	"go/build"
	"io"
	"io/fs"
	"math/rand"
	"os"
	"path/filepath"
	"runtime"
	"strconv"
	"strings"
	"sync"
	"testing"

	messages "github.com/cucumber/messages/go/v21"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/formatters"
	ifmt "github.com/cucumber/godog/internal/formatters"
	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/parser"
	"github.com/cucumber/godog/internal/storage"
	"github.com/cucumber/godog/internal/utils"
)

const (
	exitSuccess int = iota
	exitFailure
	exitOptionError
)

type (
	testSuiteInitializer func(*TestSuiteContext)
	scenarioInitializer  func(*ScenarioContext)
)

type runner struct {
	randomSeed            int64
	stopOnFailure, strict bool

	defaultContext context.Context
	testingT       *testing.T

	features []*models.Feature

	testSuiteInitializer testSuiteInitializer
	scenarioInitializer  scenarioInitializer

	storage *storage.Storage
	fmt     Formatter
}

func (r *runner) concurrent(rate int) (failed bool) {
	var copyLock sync.Mutex

	if fmt, ok := r.fmt.(storageFormatter); ok {
		fmt.SetStorage(r.storage)
	}

	testSuiteContext := TestSuiteContext{
		suite: &suite{
			fmt:            r.fmt,
			randomSeed:     r.randomSeed,
			strict:         r.strict,
			storage:        r.storage,
			defaultContext: r.defaultContext,
			testingT:       r.testingT,
		},
	}
	if r.testSuiteInitializer != nil {
		r.testSuiteInitializer(&testSuiteContext)
	}

	testRunStarted := models.TestRunStarted{StartedAt: utils.TimeNowFunc()}
	r.storage.MustInsertTestRunStarted(testRunStarted)
	r.fmt.TestRunStarted()

	// run before suite handlers
	for _, f := range testSuiteContext.beforeSuiteHandlers {
		f()
	}

	queue := make(chan int, rate)
	for _, ft := range r.features {
		pickles := make([]*messages.Pickle, len(ft.Pickles))
		if r.randomSeed != 0 {
			r := rand.New(rand.NewSource(r.randomSeed))
			perm := r.Perm(len(ft.Pickles))
			for i, v := range perm {
				pickles[v] = ft.Pickles[i]
			}
		} else {
			copy(pickles, ft.Pickles)
		}

		for i, p := range pickles {
			pickle := *p

			queue <- i // reserve space in queue

			if i == 0 {
				r.fmt.Feature(ft.GherkinDocument, ft.Uri, ft.Content)
			}

			runPickle := func(fail *bool, pickle *messages.Pickle) {
				defer func() {
					<-queue // free a space in queue
				}()

				if r.stopOnFailure && *fail {
					return
				}

				// Copy base suite.
				suite := *testSuiteContext.suite
				if rate > 1 {
					// if running concurrently, only print at end of scenario to keep
					// scenario logs segregated
					ffmt := ifmt.WrapOnFlush(testSuiteContext.suite.fmt)
					suite.fmt = ffmt
					defer ffmt.Flush()
				}

				if r.scenarioInitializer != nil {
					sc := ScenarioContext{suite: &suite}
					r.scenarioInitializer(&sc)
				}

				err := suite.runPickle(pickle)
				if suite.shouldFail(err) {
					copyLock.Lock()
					*fail = true
					copyLock.Unlock()
				}
			}

			if rate == 1 {
				// Running within the same goroutine for concurrency 1
				// to preserve original stacks and simplify debugging.
				runPickle(&failed, &pickle)
			} else {
				go runPickle(&failed, &pickle)
			}
		}
	}

	// wait until last are processed
	for i := 0; i < rate; i++ {
		queue <- i
	}

	close(queue)

	// run after suite handlers
	for _, f := range testSuiteContext.afterSuiteHandlers {
		f()
	}

	// print summary
	r.fmt.Summary()
	return
}

func runWithOptions(suiteName string, runner runner, opt Options) int {
	var output io.Writer = os.Stdout
	if nil != opt.Output {
		output = opt.Output
	}

	multiFmt := ifmt.MultiFormatter{}

	for _, formatter := range strings.Split(opt.Format, ",") {
		out := output
		formatterParts := strings.SplitN(formatter, ":", 2)

		if len(formatterParts) > 1 {
			f, err := os.Create(formatterParts[1])
			if err != nil {
				err = fmt.Errorf(
					`couldn't create file with name: "%s", error: %s`,
					formatterParts[1], err.Error(),
				)
				fmt.Fprintln(os.Stderr, err)

				return exitOptionError
			}

			defer f.Close()

			out = f
		}

		if opt.NoColors {
			out = colors.Uncolored(out)
		} else {
			out = colors.Colored(out)
		}

		if nil == formatters.FindFmt(formatterParts[0]) {
			var names []string
			for name := range formatters.AvailableFormatters() {
				names = append(names, name)
			}
			fmt.Fprintln(os.Stderr, fmt.Errorf(
				`unregistered formatter name: "%s", use one of: %s`,
				opt.Format,
				strings.Join(names, ", "),
			))
			return exitOptionError
		}

		multiFmt.Add(formatterParts[0], out)
	}

	if opt.ShowStepDefinitions {
		s := suite{}
		sc := ScenarioContext{suite: &s}
		runner.scenarioInitializer(&sc)
		printStepDefinitions(s.steps, output)
		return exitOptionError
	}

	if len(opt.Paths) == 0 && len(opt.FeatureContents) == 0 {
		inf, err := func() (fs.FileInfo, error) {
			file, err := opt.FS.Open("features")
			if err != nil {
				return nil, err
			}
			defer file.Close()

			return file.Stat()
		}()
		if err == nil && inf.IsDir() {
			opt.Paths = []string{"features"}
		}
	}

	if opt.Concurrency < 1 {
		opt.Concurrency = 1
	}

	runner.fmt = multiFmt.FormatterFunc(suiteName, output)
	opt.FS = storage.FS{FS: opt.FS}

	if len(opt.FeatureContents) > 0 {
		features, err := parser.ParseFromBytes(opt.Tags, opt.Dialect, opt.FeatureContents)
		if err != nil {
			fmt.Fprintln(os.Stderr, err)
			return exitOptionError
		}
		runner.features = append(runner.features, features...)
	}

	if len(opt.Paths) > 0 {
		features, err := parser.ParseFeatures(opt.FS, opt.Tags, opt.Dialect, opt.Paths)
		if err != nil {
			fmt.Fprintln(os.Stderr, err)
			return exitOptionError
		}
		runner.features = append(runner.features, features...)
	}

	runner.storage = storage.NewStorage()
	for _, feat := range runner.features {
		runner.storage.MustInsertFeature(feat)

		for _, pickle := range feat.Pickles {
			runner.storage.MustInsertPickle(pickle)
		}
	}

	// user may have specified -1 option to create random seed
	runner.randomSeed = opt.Randomize
	if runner.randomSeed == -1 {
		runner.randomSeed = makeRandomSeed()
	}

	runner.stopOnFailure = opt.StopOnFailure
	runner.strict = opt.Strict
	runner.defaultContext = opt.DefaultContext
	runner.testingT = opt.TestingT

	// store chosen seed in environment, so it could be seen in formatter summary report
	os.Setenv("GODOG_SEED", strconv.FormatInt(runner.randomSeed, 10))
	// determine tested package
	_, filename, _, _ := runtime.Caller(1)
	os.Setenv("GODOG_TESTED_PACKAGE", runsFromPackage(filename))

	failed := runner.concurrent(opt.Concurrency)

	// @TODO: should prevent from having these
	os.Setenv("GODOG_SEED", "")
	os.Setenv("GODOG_TESTED_PACKAGE", "")
	if failed && opt.Format != "events" {
		return exitFailure
	}
	return exitSuccess
}

func runsFromPackage(fp string) string {
	dir := filepath.Dir(fp)

	gopaths := filepath.SplitList(build.Default.GOPATH)
	for _, gp := range gopaths {
		gp = filepath.Join(gp, "src")
		if strings.Index(dir, gp) == 0 {
			return strings.TrimLeft(strings.Replace(dir, gp, "", 1), string(filepath.Separator))
		}
	}
	return dir
}

// TestSuite allows for configuration
// of the Test Suite Execution
type TestSuite struct {
	Name                 string
	TestSuiteInitializer func(*TestSuiteContext)
	ScenarioInitializer  func(*ScenarioContext)
	Options              *Options
}

// Run will execute the test suite.
//
// If options are not set, it will reads
// all configuration options from flags.
//
// The exit codes may vary from:
//
//	0 - success
//	1 - failed
//	2 - command line usage error
//	128 - or higher, os signal related error exit codes
//
// If there are flag related errors they will be directed to os.Stderr
func (ts TestSuite) Run() int {
	if ts.Options == nil {
		var err error
		ts.Options, err = getDefaultOptions()
		if err != nil {
			return exitOptionError
		}
	}
	if ts.Options.FS == nil {
		ts.Options.FS = storage.FS{}
	}
	if ts.Options.ShowHelp {
		flag.CommandLine.Usage()

		return 0
	}

	r := runner{testSuiteInitializer: ts.TestSuiteInitializer, scenarioInitializer: ts.ScenarioInitializer}
	return runWithOptions(ts.Name, r, *ts.Options)
}

// RetrieveFeatures will parse and return the features based on test suite option
// Any modification on the parsed features will not have any impact on the next Run of the Test Suite
func (ts TestSuite) RetrieveFeatures() ([]*models.Feature, error) {
	opt := ts.Options

	if opt == nil {
		var err error
		opt, err = getDefaultOptions()
		if err != nil {
			return nil, err
		}
	}

	if ts.Options.FS == nil {
		ts.Options.FS = storage.FS{}
	}

	if len(opt.Paths) == 0 {
		inf, err := func() (fs.FileInfo, error) {
			file, err := opt.FS.Open("features")
			if err != nil {
				return nil, err
			}
			defer file.Close()

			return file.Stat()
		}()
		if err == nil && inf.IsDir() {
			opt.Paths = []string{"features"}
		}
	}

	return parser.ParseFeatures(opt.FS, opt.Tags, opt.Dialect, opt.Paths)
}

func getDefaultOptions() (*Options, error) {
	opt := &Options{}
	opt.Output = colors.Colored(os.Stdout)

	flagSet := flagSet(opt)
	if err := flagSet.Parse(os.Args[1:]); err != nil {
		fmt.Fprintln(os.Stderr, err)
		return nil, err
	}

	opt.Paths = flagSet.Args()
	opt.FS = storage.FS{}

	return opt, nil
}
```

## File: `run_progress_test.go`
```go
package godog

import (
	"bytes"
	"strings"
	"testing"

	messages "github.com/cucumber/messages/go/v21"

	gherkin "github.com/cucumber/gherkin/go/v26"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/internal/formatters"
	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/storage"
)

var basicGherkinFeature = `
Feature: basic

  Scenario: passing scenario
	When one
	Then two
`

func Test_ProgressFormatterWhenStepPanics(t *testing.T) {
	const path = "any.feature"

	gd, err := gherkin.ParseGherkinDocument(strings.NewReader(basicGherkinFeature), (&messages.Incrementing{}).NewId)
	require.NoError(t, err)

	gd.Uri = path
	ft := models.Feature{GherkinDocument: gd}
	ft.Pickles = gherkin.Pickles(*gd, path, (&messages.Incrementing{}).NewId)

	var buf bytes.Buffer
	w := colors.Uncolored(&buf)
	r := runner{
		fmt:      formatters.ProgressFormatterFunc("progress", w),
		features: []*models.Feature{&ft},
		scenarioInitializer: func(ctx *ScenarioContext) {
			ctx.Step(`^one$`, func() error { return nil })
			ctx.Step(`^two$`, func() error { panic("omg") })
		},
	}

	r.storage = storage.NewStorage()
	r.storage.MustInsertFeature(&ft)
	for _, pickle := range ft.Pickles {
		r.storage.MustInsertPickle(pickle)
	}

	failed := r.concurrent(1)
	require.True(t, failed)

	actual := buf.String()
	assert.Contains(t, actual, "run_progress_test.go:")
}

func Test_ProgressFormatterWithPanicInMultistep(t *testing.T) {
	const path = "any.feature"

	gd, err := gherkin.ParseGherkinDocument(strings.NewReader(basicGherkinFeature), (&messages.Incrementing{}).NewId)
	require.NoError(t, err)

	gd.Uri = path
	ft := models.Feature{GherkinDocument: gd}
	ft.Pickles = gherkin.Pickles(*gd, path, (&messages.Incrementing{}).NewId)

	var buf bytes.Buffer
	w := colors.Uncolored(&buf)
	r := runner{
		fmt:      formatters.ProgressFormatterFunc("progress", w),
		features: []*models.Feature{&ft},
		scenarioInitializer: func(ctx *ScenarioContext) {
			ctx.Step(`^sub1$`, func() error { panic("DELIBERATE FAILURE") })
			ctx.Step(`^sub-sub$`, func() error { return nil })
			ctx.Step(`^sub2$`, func() Steps { return Steps{"sub-sub", "sub1", "one"} })
			ctx.Step(`^one$`, func() error { return nil })
			ctx.Step(`^two$`, func() Steps { return []string{"sub1", "sub2"} })
		},
	}

	r.storage = storage.NewStorage()
	r.storage.MustInsertFeature(&ft)
	for _, pickle := range ft.Pickles {
		r.storage.MustInsertPickle(pickle)
	}

	failed := r.concurrent(1)
	require.True(t, failed)
}

func Test_ProgressFormatterMultistepTemplates(t *testing.T) {
	const path = "any.feature"

	gd, err := gherkin.ParseGherkinDocument(strings.NewReader(basicGherkinFeature), (&messages.Incrementing{}).NewId)
	require.NoError(t, err)

	gd.Uri = path
	ft := models.Feature{GherkinDocument: gd}
	ft.Pickles = gherkin.Pickles(*gd, path, (&messages.Incrementing{}).NewId)

	var buf bytes.Buffer
	w := colors.Uncolored(&buf)
	r := runner{
		fmt:      formatters.ProgressFormatterFunc("progress", w),
		features: []*models.Feature{&ft},
		scenarioInitializer: func(ctx *ScenarioContext) {
			ctx.Step(`^sub-sub$`, func() error { return nil })
			ctx.Step(`^substep$`, func() Steps { return Steps{"sub-sub", `unavailable "John" cost 5`, "one", "three"} })
			ctx.Step(`^one$`, func() error { return nil })
			ctx.Step(`^(t)wo$`, func(s string) Steps { return Steps{"undef", "substep"} })
		},
	}

	r.storage = storage.NewStorage()
	r.storage.MustInsertFeature(&ft)
	for _, pickle := range ft.Pickles {
		r.storage.MustInsertPickle(pickle)
	}

	failed := r.concurrent(1)
	require.False(t, failed)

	expected := `.U 2


1 scenarios (1 undefined)
2 steps (1 passed, 1 undefined)
0s

You can implement step definitions for undefined steps with these snippets:

func three() error {
	return godog.ErrPending
}

func unavailableCost(arg1 string, arg2 int) error {
	return godog.ErrPending
}

func undef() error {
	return godog.ErrPending
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Step(` + "`^three$`" + `, three)
	ctx.Step(` + "`^unavailable \"([^\"]*)\" cost (\\d+)$`" + `, unavailableCost)
	ctx.Step(` + "`^undef$`" + `, undef)
}

`

	actual := buf.String()
	assert.Equal(t, expected, actual)
}

func Test_ProgressFormatterWhenMultiStepHasArgument(t *testing.T) {
	const path = "any.feature"

	var featureSource = `
Feature: basic

  Scenario: passing scenario
	When one
	Then two:
	"""
	text
	"""
`

	gd, err := gherkin.ParseGherkinDocument(strings.NewReader(featureSource), (&messages.Incrementing{}).NewId)
	require.NoError(t, err)

	gd.Uri = path
	ft := models.Feature{GherkinDocument: gd}
	ft.Pickles = gherkin.Pickles(*gd, path, (&messages.Incrementing{}).NewId)

	var buf bytes.Buffer
	w := colors.Uncolored(&buf)
	r := runner{
		fmt:      formatters.ProgressFormatterFunc("progress", w),
		features: []*models.Feature{&ft},
		scenarioInitializer: func(ctx *ScenarioContext) {
			ctx.Step(`^one$`, func() error { return nil })
			ctx.Step(`^two:$`, func(doc *messages.PickleDocString) Steps { return Steps{"one"} })
		},
	}

	r.storage = storage.NewStorage()
	r.storage.MustInsertFeature(&ft)
	for _, pickle := range ft.Pickles {
		r.storage.MustInsertPickle(pickle)
	}

	failed := r.concurrent(1)

	require.False(t, failed)
}

func Test_ProgressFormatterWhenMultiStepHasStepWithArgument(t *testing.T) {
	const path = "any.feature"

	var featureSource = `
Feature: basic

  Scenario: passing scenario
	When one
	Then two`

	gd, err := gherkin.ParseGherkinDocument(strings.NewReader(featureSource), (&messages.Incrementing{}).NewId)
	require.NoError(t, err)

	gd.Uri = path
	ft := models.Feature{GherkinDocument: gd}
	ft.Pickles = gherkin.Pickles(*gd, path, (&messages.Incrementing{}).NewId)

	var subStep = `three:
	"""
	content
	"""`

	var buf bytes.Buffer
	w := colors.Uncolored(&buf)
	r := runner{
		fmt:      formatters.ProgressFormatterFunc("progress", w),
		features: []*models.Feature{&ft},
		scenarioInitializer: func(ctx *ScenarioContext) {
			ctx.Step(`^one$`, func() error { return nil })
			ctx.Step(`^two$`, func() Steps { return Steps{subStep} })
			ctx.Step(`^three:$`, func(doc *messages.PickleDocString) error { return nil })
		},
	}

	r.storage = storage.NewStorage()
	r.storage.MustInsertFeature(&ft)
	for _, pickle := range ft.Pickles {
		r.storage.MustInsertPickle(pickle)
	}

	failed := r.concurrent(1)
	require.True(t, failed)

	expected := `.F 2


--- Failed steps:

  Scenario: passing scenario # any.feature:4
    Then two # any.feature:6
      Error: nested steps cannot be multiline and have table or content body argument


1 scenarios (1 failed)
2 steps (1 passed, 1 failed)
0s
`

	actual := buf.String()
	assert.Equal(t, expected, actual)
}
```

## File: `run_test.go`
```go
package godog

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"io/fs"
	"io/ioutil"
	"os"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"
	"testing"
	"testing/fstest"

	gherkin "github.com/cucumber/gherkin/go/v26"
	messages "github.com/cucumber/messages/go/v21"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/internal/formatters"
	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/storage"
)

func okStep() error {
	return nil
}

func TestPrintsStepDefinitions(t *testing.T) {
	var buf bytes.Buffer
	w := colors.Uncolored(&buf)
	s := suite{}
	ctx := ScenarioContext{suite: &s}

	steps := []string{
		"^passing step$",
		`^with name "([^"])"`,
	}

	for _, step := range steps {
		ctx.Step(step, okStep)
	}

	printStepDefinitions(s.steps, w)

	out := buf.String()
	ref := `okStep`
	for i, def := range strings.Split(strings.TrimSpace(out), "\n") {
		if idx := strings.Index(def, steps[i]); idx == -1 {
			t.Fatalf(`step "%s" was not found in output`, steps[i])
		}
		if idx := strings.Index(def, ref); idx == -1 {
			t.Fatalf(`step definition reference "%s" was not found in output: "%s"`, ref, def)
		}
	}
}

func TestPrintsNoStepDefinitionsIfNoneFound(t *testing.T) {
	var buf bytes.Buffer
	w := colors.Uncolored(&buf)
	s := &suite{}

	printStepDefinitions(s.steps, w)

	out := strings.TrimSpace(buf.String())
	assert.Equal(t, "there were no contexts registered, could not find any step definition..", out)
}

func Test_FailsOrPassesBasedOnStrictModeWhenHasPendingSteps(t *testing.T) {
	const path = "any.feature"

	gd, err := gherkin.ParseGherkinDocument(strings.NewReader(basicGherkinFeature), (&messages.Incrementing{}).NewId)
	require.NoError(t, err)

	gd.Uri = path
	ft := models.Feature{GherkinDocument: gd}
	ft.Pickles = gherkin.Pickles(*gd, path, (&messages.Incrementing{}).NewId)

	var beforeScenarioFired, afterScenarioFired int

	r := runner{
		fmt:      formatters.ProgressFormatterFunc("progress", ioutil.Discard),
		features: []*models.Feature{&ft},
		testSuiteInitializer: func(ctx *TestSuiteContext) {
			ctx.ScenarioContext().Before(func(ctx context.Context, sc *Scenario) (context.Context, error) {
				beforeScenarioFired++
				return ctx, nil
			})

			ctx.ScenarioContext().After(func(ctx context.Context, sc *Scenario, err error) (context.Context, error) {
				afterScenarioFired++
				return ctx, nil
			})
		},
		scenarioInitializer: func(ctx *ScenarioContext) {
			ctx.Step(`^one$`, func() error { return nil })
			ctx.Step(`^two$`, func() error { return ErrPending })
		},
		testingT: t,
	}

	r.storage = storage.NewStorage()
	r.storage.MustInsertFeature(&ft)
	for _, pickle := range ft.Pickles {
		r.storage.MustInsertPickle(pickle)
	}

	failed := r.concurrent(1)
	require.False(t, r.testingT.Failed())
	require.False(t, failed)
	assert.Equal(t, 1, beforeScenarioFired)
	assert.Equal(t, 1, afterScenarioFired)

	// avoid t is Failed because this testcase Failed
	r.testingT = nil
	r.strict = true
	failed = r.concurrent(1)
	require.True(t, failed)
	assert.Equal(t, 2, beforeScenarioFired)
	assert.Equal(t, 2, afterScenarioFired)
}

func Test_FailsOrPassesBasedOnStrictModeWhenHasUndefinedSteps(t *testing.T) {
	const path = "any.feature"

	gd, err := gherkin.ParseGherkinDocument(strings.NewReader(basicGherkinFeature), (&messages.Incrementing{}).NewId)
	require.NoError(t, err)

	gd.Uri = path
	ft := models.Feature{GherkinDocument: gd}
	ft.Pickles = gherkin.Pickles(*gd, path, (&messages.Incrementing{}).NewId)

	r := runner{
		fmt:      formatters.ProgressFormatterFunc("progress", ioutil.Discard),
		features: []*models.Feature{&ft},
		scenarioInitializer: func(ctx *ScenarioContext) {
			ctx.Step(`^one$`, func() error { return nil })
			// two - is undefined
		},
	}

	r.storage = storage.NewStorage()
	r.storage.MustInsertFeature(&ft)
	for _, pickle := range ft.Pickles {
		r.storage.MustInsertPickle(pickle)
	}

	failed := r.concurrent(1)
	require.False(t, failed)

	r.strict = true
	failed = r.concurrent(1)
	require.True(t, failed)
}

func Test_ShouldFailOnError(t *testing.T) {
	const path = "any.feature"

	gd, err := gherkin.ParseGherkinDocument(strings.NewReader(basicGherkinFeature), (&messages.Incrementing{}).NewId)
	require.NoError(t, err)

	gd.Uri = path
	ft := models.Feature{GherkinDocument: gd}
	ft.Pickles = gherkin.Pickles(*gd, path, (&messages.Incrementing{}).NewId)

	r := runner{
		fmt:      formatters.ProgressFormatterFunc("progress", ioutil.Discard),
		features: []*models.Feature{&ft},
		scenarioInitializer: func(ctx *ScenarioContext) {
			ctx.Step(`^two$`, func() error { return fmt.Errorf("error") })
			ctx.Step(`^one$`, func() error { return nil })
		},
	}

	r.storage = storage.NewStorage()
	r.storage.MustInsertFeature(&ft)
	for _, pickle := range ft.Pickles {
		r.storage.MustInsertPickle(pickle)
	}

	failed := r.concurrent(1)
	require.True(t, failed)
}

func Test_FailsWithUnknownFormatterOptionError(t *testing.T) {
	stderr, closer := bufErrorPipe(t)
	defer closer()
	defer stderr.Close()

	opts := Options{
		Format: "unknown",
		Paths:  []string{"features/load:6"},
		Output: ioutil.Discard,
	}

	status := TestSuite{
		Name:                "fails",
		ScenarioInitializer: func(_ *ScenarioContext) {},
		Options:             &opts,
	}.Run()

	require.Equal(t, exitOptionError, status)

	closer()

	b, err := ioutil.ReadAll(stderr)
	require.NoError(t, err)

	out := strings.TrimSpace(string(b))
	assert.Contains(t, out, `unregistered formatter name: "unknown", use one of`)
}

func Test_FailsWithOptionErrorWhenLookingForFeaturesInUnavailablePath(t *testing.T) {
	stderr, closer := bufErrorPipe(t)
	defer closer()
	defer stderr.Close()

	opts := Options{
		Format: "progress",
		Paths:  []string{"unavailable"},
		Output: ioutil.Discard,
	}

	status := TestSuite{
		Name:                "fails",
		ScenarioInitializer: func(_ *ScenarioContext) {},
		Options:             &opts,
	}.Run()

	require.Equal(t, exitOptionError, status)

	closer()

	b, err := ioutil.ReadAll(stderr)
	require.NoError(t, err)

	out := strings.TrimSpace(string(b))
	assert.Equal(t, `feature path "unavailable" is not available`, out)
}

func Test_ByDefaultRunsFeaturesPath(t *testing.T) {
	opts := Options{
		Format: "progress",
		Output: ioutil.Discard,
		Strict: true,
	}

	status := TestSuite{
		Name:                "fails",
		ScenarioInitializer: func(_ *ScenarioContext) {},
		Options:             &opts,
	}.Run()

	// should fail in strict mode due to undefined steps
	assert.Equal(t, exitFailure, status)

	opts.Strict = false
	status = TestSuite{
		Name:                "succeeds",
		ScenarioInitializer: func(_ *ScenarioContext) {},
		Options:             &opts,
	}.Run()

	// should succeed in non strict mode due to undefined steps
	assert.Equal(t, exitSuccess, status)
}

func Test_RunsWithFeatureContentsOption(t *testing.T) {
	items, err := ioutil.ReadDir("./features")
	require.NoError(t, err)

	var featureContents []Feature
	for _, item := range items {
		if !item.IsDir() && strings.Contains(item.Name(), ".feature") {
			contents, err := os.ReadFile("./features/" + item.Name())
			require.NoError(t, err)
			featureContents = append(featureContents, Feature{
				Name:     item.Name(),
				Contents: contents,
			})
		}
	}

	opts := Options{
		Format:          "progress",
		Output:          ioutil.Discard,
		Strict:          true,
		FeatureContents: featureContents,
	}

	status := TestSuite{
		Name:                "fails",
		ScenarioInitializer: func(_ *ScenarioContext) {},
		Options:             &opts,
	}.Run()

	// should fail in strict mode due to undefined steps
	assert.Equal(t, exitFailure, status)

	opts.Strict = false
	status = TestSuite{
		Name:                "succeeds",
		ScenarioInitializer: func(_ *ScenarioContext) {},
		Options:             &opts,
	}.Run()

	// should succeed in non strict mode due to undefined steps
	assert.Equal(t, exitSuccess, status)
}

func Test_RunsWithFeatureContentsAndPathsOptions(t *testing.T) {
	featureContents := []Feature{
		{
			Name: "MySuperCoolFeature",
			Contents: []byte(`
Feature: run features from bytes
  Scenario: should run a normal feature
    Given a feature "normal.feature" file:
      """
      Feature: normal feature

        Scenario: parse a scenario
          Given a feature path "features/load.feature:6"
          When I parse features
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      a feature path "features/load.feature:6"
      I parse features
      I should have 1 scenario registered
      """`),
		},
	}

	opts := Options{
		Format:          "progress",
		Output:          ioutil.Discard,
		Paths:           []string{"./features"},
		FeatureContents: featureContents,
	}

	status := TestSuite{
		Name:                "succeeds",
		ScenarioInitializer: func(_ *ScenarioContext) {},
		Options:             &opts,
	}.Run()

	assert.Equal(t, exitSuccess, status)
}

func bufErrorPipe(t *testing.T) (io.ReadCloser, func()) {
	stderr := os.Stderr
	r, w, err := os.Pipe()
	require.NoError(t, err)

	os.Stderr = w
	return r, func() {
		w.Close()
		os.Stderr = stderr
	}
}

func Test_RandomizeRun_WithStaticSeed(t *testing.T) {
	const noRandomFlag = 0
	const noConcurrencyFlag = 1
	const formatter = "pretty"
	const featurePath = "internal/formatters/formatter-tests/features/with_few_empty_scenarios.feature"

	fmtOutputScenarioInitializer := func(ctx *ScenarioContext) {
		ctx.Step(`^(?:a )?failing step`, failingStepDef)
		ctx.Step(`^(?:a )?pending step$`, pendingStepDef)
		ctx.Step(`^(?:a )?passing step$`, passingStepDef)
		ctx.Step(`^odd (\d+) and even (\d+) number$`, oddEvenStepDef)
	}

	expectedStatus, expectedOutput := testRun(t,
		fmtOutputScenarioInitializer,
		formatter, noConcurrencyFlag,
		noRandomFlag, []string{featurePath},
	)

	const staticSeed int64 = 1
	actualStatus, actualOutput := testRun(t,
		fmtOutputScenarioInitializer,
		formatter, noConcurrencyFlag,
		staticSeed, []string{featurePath},
	)

	actualSeed := parseSeed(actualOutput)
	assert.Equal(t, staticSeed, actualSeed)

	// Removes "Randomized with seed: <seed>" part of the output
	actualOutputSplit := strings.Split(actualOutput, "\n")
	actualOutputSplit = actualOutputSplit[:len(actualOutputSplit)-2]
	actualOutputReduced := strings.Join(actualOutputSplit, "\n")

	assert.Equal(t, expectedStatus, actualStatus)
	assert.NotEqual(t, expectedOutput, actualOutputReduced)
	assertOutput(t, formatter, expectedOutput, actualOutputReduced)
}

func Test_RandomizeRun_RerunWithSeed(t *testing.T) {
	const createRandomSeedFlag = -1
	const noConcurrencyFlag = 1
	const formatter = "pretty"
	const featurePath = "internal/formatters/formatter-tests/features/with_few_empty_scenarios.feature"

	fmtOutputScenarioInitializer := func(ctx *ScenarioContext) {
		ctx.Step(`^(?:a )?failing step`, failingStepDef)
		ctx.Step(`^(?:a )?pending step$`, pendingStepDef)
		ctx.Step(`^(?:a )?passing step$`, passingStepDef)
		ctx.Step(`^odd (\d+) and even (\d+) number$`, oddEvenStepDef)
	}

	expectedStatus, expectedOutput := testRun(t,
		fmtOutputScenarioInitializer,
		formatter, noConcurrencyFlag,
		createRandomSeedFlag, []string{featurePath},
	)

	expectedSeed := parseSeed(expectedOutput)
	assert.NotZero(t, expectedSeed)

	actualStatus, actualOutput := testRun(t,
		fmtOutputScenarioInitializer,
		formatter, noConcurrencyFlag,
		expectedSeed, []string{featurePath},
	)

	actualSeed := parseSeed(actualOutput)

	assert.Equal(t, expectedSeed, actualSeed)
	assert.Equal(t, expectedStatus, actualStatus)
	assert.Equal(t, expectedOutput, actualOutput)
}

func Test_FormatOutputRun(t *testing.T) {
	const noRandomFlag = 0
	const noConcurrencyFlag = 1
	const formatter = "junit"
	const featurePath = "internal/formatters/formatter-tests/features/with_few_empty_scenarios.feature"

	fmtOutputScenarioInitializer := func(ctx *ScenarioContext) {
		ctx.Step(`^(?:a )?failing step`, failingStepDef)
		ctx.Step(`^(?:a )?pending step$`, pendingStepDef)
		ctx.Step(`^(?:a )?passing step$`, passingStepDef)
		ctx.Step(`^odd (\d+) and even (\d+) number$`, oddEvenStepDef)
	}

	expectedStatus, expectedOutput := testRun(t,
		fmtOutputScenarioInitializer,
		formatter, noConcurrencyFlag,
		noRandomFlag, []string{featurePath},
	)

	dir := filepath.Join(os.TempDir(), t.Name())
	err := os.MkdirAll(dir, 0755)
	require.NoError(t, err)

	defer os.RemoveAll(dir)

	file := filepath.Join(dir, "result.xml")

	actualStatus, actualOutput := testRun(t,
		fmtOutputScenarioInitializer,
		formatter+":"+file, noConcurrencyFlag,
		noRandomFlag, []string{featurePath},
	)

	result, err := ioutil.ReadFile(file)
	require.NoError(t, err)
	actualOutputFromFile := string(result)

	assert.Equal(t, expectedStatus, actualStatus)
	assert.Empty(t, actualOutput)
	assert.Equal(t, expectedOutput, actualOutputFromFile)
}

func Test_FormatOutputRun_Error(t *testing.T) {
	const noRandomFlag = 0
	const noConcurrencyFlag = 1
	const formatter = "junit"
	const featurePath = "internal/formatters/formatter-tests/features/with_few_empty_scenarios.feature"

	fmtOutputScenarioInitializer := func(ctx *ScenarioContext) {
		ctx.Step(`^(?:a )?failing step`, failingStepDef)
		ctx.Step(`^(?:a )?pending step$`, pendingStepDef)
		ctx.Step(`^(?:a )?passing step$`, passingStepDef)
		ctx.Step(`^odd (\d+) and even (\d+) number$`, oddEvenStepDef)
	}

	expectedStatus, expectedOutput := exitOptionError, ""

	dir := filepath.Join(os.TempDir(), t.Name())
	file := filepath.Join(dir, "result.xml")

	// next test is expected to log: couldn't create file with name: )
	actualStatus, actualOutput := testRun(t,
		fmtOutputScenarioInitializer,
		formatter+":"+file, noConcurrencyFlag,
		noRandomFlag, []string{featurePath},
	)

	assert.Equal(t, expectedStatus, actualStatus)
	assert.Equal(t, expectedOutput, actualOutput)

	_, err := ioutil.ReadFile(file)
	assert.Error(t, err)
}

func Test_AllFeaturesRun(t *testing.T) {
	const concurrency = 100
	const noRandomFlag = 0
	const format = "progress"

	const expected = `...................................................................... 70
...................................................................... 140
...................................................................... 210
...................................................................... 280
...................................................................... 350
...................................................................... 420
...                                                                    423


108 scenarios (108 passed)
423 steps (423 passed)
0s
`

	actualStatus, actualOutput := testRun(t,
		InitializeScenario,
		format, concurrency,
		noRandomFlag, []string{"features"},
	)

	assert.Equal(t, exitSuccess, actualStatus)
	assert.Equal(t, expected, actualOutput)
}

func Test_AllFeaturesRunAsSubtests(t *testing.T) {
	const concurrency = 100
	const noRandomFlag = 0
	const format = "progress"

	const expected = `...................................................................... 70
...................................................................... 140
...................................................................... 210
...................................................................... 280
...................................................................... 350
...................................................................... 420
...                                                                    423


108 scenarios (108 passed)
423 steps (423 passed)
0s
`

	actualStatus, actualOutput := testRunWithOptions(
		t,
		Options{
			Format:      format,
			Concurrency: concurrency,
			Paths:       []string{"features"},
			Randomize:   noRandomFlag,
			TestingT:    t,
		},
		InitializeScenario,
	)

	assert.Equal(t, exitSuccess, actualStatus)
	assert.Equal(t, expected, actualOutput)
}

func Test_FormatterConcurrencyRun(t *testing.T) {
	formatters := []string{
		"progress",
		"junit",
		"pretty",
		"events",
		"cucumber",
	}

	featurePaths := []string{"internal/formatters/formatter-tests/features"}

	const concurrency = 100
	const noRandomFlag = 0
	const noConcurrency = 1

	fmtOutputScenarioInitializer := func(ctx *ScenarioContext) {
		ctx.Step(`^(?:a )?failing step`, failingStepDef)
		ctx.Step(`^(?:a )?pending step$`, pendingStepDef)
		ctx.Step(`^(?:a )?passing step$`, passingStepDef)
		ctx.Step(`^odd (\d+) and even (\d+) number$`, oddEvenStepDef)
	}

	for _, formatter := range formatters {
		t.Run(
			fmt.Sprintf("%s/concurrency/%d", formatter, concurrency),
			func(t *testing.T) {
				expectedStatus, expectedOutput := testRun(t,
					fmtOutputScenarioInitializer,
					formatter, noConcurrency,
					noRandomFlag, featurePaths,
				)
				actualStatus, actualOutput := testRun(t,
					fmtOutputScenarioInitializer,
					formatter, concurrency,
					noRandomFlag, featurePaths,
				)

				assert.Equal(t, expectedStatus, actualStatus)
				assertOutput(t, formatter, expectedOutput, actualOutput)
			},
		)
	}
}

func testRun(
	t *testing.T,
	scenarioInitializer func(*ScenarioContext),
	format string,
	concurrency int,
	randomSeed int64,
	featurePaths []string,
) (int, string) {
	t.Helper()

	opts := Options{
		Format:      format,
		Paths:       featurePaths,
		Concurrency: concurrency,
		Randomize:   randomSeed,
	}

	return testRunWithOptions(t, opts, scenarioInitializer)
}

func testRunWithOptions(
	t *testing.T,
	opts Options,
	scenarioInitializer func(*ScenarioContext),
) (int, string) {
	t.Helper()

	output := new(bytes.Buffer)

	opts.Output = output
	opts.NoColors = true

	status := TestSuite{
		Name:                "succeed",
		ScenarioInitializer: scenarioInitializer,
		Options:             &opts,
	}.Run()

	actual, err := ioutil.ReadAll(output)
	require.NoError(t, err)

	return status, string(actual)
}

func assertOutput(t *testing.T, formatter string, expected, actual string) {
	switch formatter {
	case "cucumber", "junit", "pretty", "events":
		expectedRows := strings.Split(expected, "\n")
		actualRows := strings.Split(actual, "\n")
		assert.ElementsMatch(t, expectedRows, actualRows)
	case "progress":
		expectedOutput := parseProgressOutput(expected)
		actualOutput := parseProgressOutput(actual)

		assert.Equal(t, expectedOutput.passed, actualOutput.passed)
		assert.Equal(t, expectedOutput.skipped, actualOutput.skipped)
		assert.Equal(t, expectedOutput.failed, actualOutput.failed)
		assert.Equal(t, expectedOutput.undefined, actualOutput.undefined)
		assert.Equal(t, expectedOutput.pending, actualOutput.pending)
		assert.Equal(t, expectedOutput.noOfStepsPerRow, actualOutput.noOfStepsPerRow)
		assert.ElementsMatch(t, expectedOutput.bottomRows, actualOutput.bottomRows)
	}
}

func parseProgressOutput(output string) (parsed progressOutput) {
	mainParts := strings.Split(output, "\n\n\n")

	topRows := strings.Split(mainParts[0], "\n")
	parsed.bottomRows = strings.Split(mainParts[1], "\n")

	parsed.noOfStepsPerRow = make([]string, len(topRows))
	for idx, row := range topRows {
		rowParts := strings.Split(row, " ")
		stepResults := strings.Split(rowParts[0], "")
		parsed.noOfStepsPerRow[idx] = rowParts[1]

		for _, stepResult := range stepResults {
			switch stepResult {
			case ".":
				parsed.passed++
			case "-":
				parsed.skipped++
			case "F":
				parsed.failed++
			case "U":
				parsed.undefined++
			case "P":
				parsed.pending++
			}
		}
	}

	return parsed
}

type progressOutput struct {
	passed          int
	skipped         int
	failed          int
	undefined       int
	pending         int
	noOfStepsPerRow []string
	bottomRows      []string
}

func passingStepDef() error { return nil }

func oddEvenStepDef(odd, even int) error { return oddOrEven(odd, even) }

func oddOrEven(odd, even int) error {
	if odd%2 == 0 {
		return fmt.Errorf("%d is not odd", odd)
	}
	if even%2 != 0 {
		return fmt.Errorf("%d is not even", even)
	}
	return nil
}

func pendingStepDef() error { return ErrPending }

func failingStepDef() error { return fmt.Errorf("step failed") }

func parseSeed(str string) (seed int64) {
	re := regexp.MustCompile(`Randomized with seed: (\d*)`)
	match := re.FindStringSubmatch(str)

	if len(match) > 0 {
		var err error
		if seed, err = strconv.ParseInt(match[1], 10, 64); err != nil {
			seed = 0
		}
	}

	return
}

func Test_TestSuite_RetreiveFeatures(t *testing.T) {
	tests := map[string]struct {
		fsys fs.FS

		expFeatures int
	}{
		"standard features": {
			fsys: fstest.MapFS{
				"features/test.feature": {
					Data: []byte(`Feature: test retrieve features
  To test the feature
  I must use this feature

  Scenario: Test function RetrieveFeatures
    Given I create a TestSuite
	When I call TestSuite.RetrieveFeatures
	Then I should have one feature`),
				},
			},
			expFeatures: 1,
		},
	}

	for name, test := range tests {
		t.Run(name, func(t *testing.T) {
			features, err := TestSuite{
				Name:    "succeed",
				Options: &Options{FS: test.fsys},
			}.RetrieveFeatures()

			assert.NoError(t, err)
			assert.Equal(t, test.expFeatures, len(features))
		})
	}
}
```

## File: `stacktrace.go`
```go
package godog

import (
	"fmt"
	"go/build"
	"io"
	"path"
	"path/filepath"
	"runtime"
	"strings"
)

// Frame represents a program counter inside a stack frame.
type stackFrame uintptr

// pc returns the program counter for this frame;
// multiple frames may have the same PC value.
func (f stackFrame) pc() uintptr { return uintptr(f) - 1 }

// file returns the full path to the file that contains the
// function for this Frame's pc.
func (f stackFrame) file() string {
	fn := runtime.FuncForPC(f.pc())
	if fn == nil {
		return "unknown"
	}
	file, _ := fn.FileLine(f.pc())
	return file
}

func trimGoPath(file string) string {
	for _, p := range filepath.SplitList(build.Default.GOPATH) {
		file = strings.Replace(file, filepath.Join(p, "src")+string(filepath.Separator), "", 1)
	}
	return file
}

// line returns the line number of source code of the
// function for this Frame's pc.
func (f stackFrame) line() int {
	fn := runtime.FuncForPC(f.pc())
	if fn == nil {
		return 0
	}
	_, line := fn.FileLine(f.pc())
	return line
}

// Format formats the frame according to the fmt.Formatter interface.
//
//	%s    source file
//	%d    source line
//	%n    function name
//	%v    equivalent to %s:%d
//
// Format accepts flags that alter the printing of some verbs, as follows:
//
//	%+s   path of source file relative to the compile time GOPATH
//	%+v   equivalent to %+s:%d
func (f stackFrame) Format(s fmt.State, verb rune) {
	funcname := func(name string) string {
		i := strings.LastIndex(name, "/")
		name = name[i+1:]
		i = strings.Index(name, ".")
		return name[i+1:]
	}

	switch verb {
	case 's':
		switch {
		case s.Flag('+'):
			pc := f.pc()
			fn := runtime.FuncForPC(pc)
			if fn == nil {
				io.WriteString(s, "unknown")
			} else {
				file, _ := fn.FileLine(pc)
				fmt.Fprintf(s, "%s\n\t%s", fn.Name(), trimGoPath(file))
			}
		default:
			io.WriteString(s, path.Base(f.file()))
		}
	case 'd':
		fmt.Fprintf(s, "%d", f.line())
	case 'n':
		name := runtime.FuncForPC(f.pc()).Name()
		io.WriteString(s, funcname(name))
	case 'v':
		f.Format(s, 's')
		io.WriteString(s, ":")
		f.Format(s, 'd')
	}
}

// stack represents a stack of program counters.
type stack []uintptr

func (s *stack) Format(st fmt.State, verb rune) {
	switch verb {
	case 'v':
		switch {
		case st.Flag('+'):
			for _, pc := range *s {
				f := stackFrame(pc)
				fmt.Fprintf(st, "\n%+v", f)
			}
		}
	}
}

func callStack() *stack {
	const depth = 32
	var pcs [depth]uintptr
	n := runtime.Callers(3, pcs[:])
	var st stack = pcs[0:n]
	return &st
}

// fundamental is an error that has a message and a stack, but no caller.
type traceError struct {
	msg string
	*stack
}

func (f *traceError) Error() string { return f.msg }

func (f *traceError) Format(s fmt.State, verb rune) {
	switch verb {
	case 'v':
		if s.Flag('+') {
			io.WriteString(s, f.msg)
			f.stack.Format(s, verb)
			return
		}
		fallthrough
	case 's':
		io.WriteString(s, f.msg)
	case 'q':
		fmt.Fprintf(s, "%q", f.msg)
	}
}
```

## File: `stacktrace_test.go`
```go
package godog

import (
	"fmt"
	"runtime"
	"testing"

	"github.com/stretchr/testify/assert"
)

func callstack1() *stack {
	return callstack2()
}

func callstack2() *stack {
	return callstack3()
}

func callstack3() *stack {
	const depth = 4
	var pcs [depth]uintptr
	n := runtime.Callers(1, pcs[:])
	var st stack = pcs[0:n]
	return &st
}

func Test_Stacktrace(t *testing.T) {
	err := &traceError{
		msg:   "err msg",
		stack: callstack1(),
	}

	expected := "err msg"
	actual := fmt.Sprintf("%s", err)

	assert.Equal(t, expected, actual)
	assert.NotContains(t, actual, "stacktrace_test.go")
}
```

## File: `suite.go`
```go
package godog

import (
	"context"
	"errors"
	"fmt"
	"reflect"
	"strings"
	"testing"

	messages "github.com/cucumber/messages/go/v21"

	"github.com/cucumber/godog/formatters"
	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/storage"
	"github.com/cucumber/godog/internal/utils"
)

var (
	errorInterface   = reflect.TypeOf((*error)(nil)).Elem()
	contextInterface = reflect.TypeOf((*context.Context)(nil)).Elem()
)

// more than one regex matched the step text
var ErrAmbiguous = fmt.Errorf("ambiguous step definition")

// ErrUndefined is returned in case if step definition was not found
var ErrUndefined = fmt.Errorf("step is undefined")

// ErrPending should be returned by step definition if
// step implementation is pending
var ErrPending = fmt.Errorf("step implementation is pending")

// ErrSkip should be returned by step definition or a hook if scenario and further steps are to be skipped.
var ErrSkip = fmt.Errorf("skipped")

// StepResultStatus describes step result.
type StepResultStatus = models.StepResultStatus

const (
	// StepPassed indicates step that passed.
	StepPassed StepResultStatus = models.Passed
	// StepFailed indicates step that failed.
	StepFailed = models.Failed
	// StepSkipped indicates step that was skipped.
	StepSkipped = models.Skipped
	// StepUndefined indicates undefined step.
	StepUndefined = models.Undefined
	// StepPending indicates step with pending implementation.
	StepPending = models.Pending
	// StepAmbiguous indicates step text matches more than one step def
	StepAmbiguous = models.Ambiguous
)

type suite struct {
	steps []*models.StepDefinition

	fmt     Formatter
	storage *storage.Storage

	failed        bool
	randomSeed    int64
	stopOnFailure bool
	strict        bool

	defaultContext context.Context
	testingT       *testing.T

	// suite event handlers
	beforeScenarioHandlers []BeforeScenarioHook
	beforeStepHandlers     []BeforeStepHook
	afterStepHandlers      []AfterStepHook
	afterScenarioHandlers  []AfterScenarioHook
}

type Attachment struct {
	Body      []byte
	FileName  string
	MediaType string
}

type attachmentKey struct{}

func Attach(ctx context.Context, attachments ...Attachment) context.Context {
	existing := Attachments(ctx)
	updated := append(existing, attachments...)
	return context.WithValue(ctx, attachmentKey{}, updated)
}

func Attachments(ctx context.Context) []Attachment {
	v := ctx.Value(attachmentKey{})

	if v == nil {
		return []Attachment{}
	}
	return v.([]Attachment)
}

func clearAttach(ctx context.Context) context.Context {
	return context.WithValue(ctx, attachmentKey{}, nil)
}

func pickleAttachments(ctx context.Context) []models.PickleAttachment {

	pickledAttachments := []models.PickleAttachment{}
	attachments := Attachments(ctx)

	for _, a := range attachments {
		pickledAttachments = append(pickledAttachments, models.PickleAttachment{
			Name:     a.FileName,
			Data:     a.Body,
			MimeType: a.MediaType,
		})
	}

	return pickledAttachments
}

func (s *suite) matchStep(step *messages.PickleStep) (*models.StepDefinition, error) {
	def, err := s.matchStepTextAndType(step.Text, step.Type)
	if err != nil {
		return nil, err
	}

	if def != nil && step.Argument != nil {
		def.Args = append(def.Args, step.Argument)
	}
	return def, nil
}

func (s *suite) runStep(ctx context.Context, pickle *Scenario, step *Step, scenarioErr error, isFirst, isLast bool) (rctx context.Context, err error) {
	var match *models.StepDefinition

	rctx = ctx

	// user multistep definitions may panic
	defer func() {
		if e := recover(); e != nil {
			pe, isErr := e.(error)
			switch {
			case isErr && errors.Is(pe, errStopNow):
				// FailNow or SkipNow called on dogTestingT, so clear the error to let the normal
				// below getTestingT(ctx).isFailed() call handle the reasons.
				err = nil
			case err != nil:
				err = &traceError{
					msg:   fmt.Sprintf("%s: %v", err.Error(), e),
					stack: callStack(),
				}
			default:
				err = &traceError{
					msg:   fmt.Sprintf("%v", e),
					stack: callStack(),
				}
			}
		}

		earlyReturn := scenarioErr != nil || errors.Is(err, ErrUndefined)

		// Check for any calls to Fail on dogT
		if err == nil {
			if t := getTestingT(ctx); t != nil {
				err = t.isFailed()
			}
		}

		status := StepUndefined

		switch {
		case errors.Is(err, ErrAmbiguous):
			status = StepAmbiguous
		case errors.Is(err, ErrPending):
			status = StepPending
		case errors.Is(err, ErrSkip), err == nil && scenarioErr != nil:
			status = StepSkipped
		case errors.Is(err, ErrUndefined):
			status = StepUndefined
		case err != nil:
			status = StepFailed
		case err == nil && scenarioErr == nil:
			status = StepPassed
		}

		// Run after step handlers.
		rctx, err = s.runAfterStepHooks(ctx, step, status, err)

		// Trigger after scenario on failing or last step to attach possible hook error to step.
		if !s.shouldFail(scenarioErr) && (isLast || s.shouldFail(err)) {
			rctx, err = s.runAfterScenarioHooks(rctx, pickle, err)
		}

		// extract any accumulated attachments and clear them
		pickledAttachments := pickleAttachments(rctx)
		rctx = clearAttach(rctx)

		if earlyReturn {
			return
		}

		switch {
		case err == nil:
			sr := models.NewStepResult(models.Passed, pickle.Id, step.Id, match, pickledAttachments, nil)
			s.storage.MustInsertPickleStepResult(sr)
			s.fmt.Passed(pickle, step, match.GetInternalStepDefinition())
		case errors.Is(err, ErrPending):
			sr := models.NewStepResult(models.Pending, pickle.Id, step.Id, match, pickledAttachments, nil)
			s.storage.MustInsertPickleStepResult(sr)
			s.fmt.Pending(pickle, step, match.GetInternalStepDefinition())
		case errors.Is(err, ErrSkip):
			sr := models.NewStepResult(models.Skipped, pickle.Id, step.Id, match, pickledAttachments, nil)
			s.storage.MustInsertPickleStepResult(sr)
			s.fmt.Skipped(pickle, step, match.GetInternalStepDefinition())
		case errors.Is(err, ErrAmbiguous):
			sr := models.NewStepResult(models.Ambiguous, pickle.Id, step.Id, match, pickledAttachments, err)
			s.storage.MustInsertPickleStepResult(sr)
			s.fmt.Ambiguous(pickle, step, match.GetInternalStepDefinition(), err)
		default:
			sr := models.NewStepResult(models.Failed, pickle.Id, step.Id, match, pickledAttachments, err)
			s.storage.MustInsertPickleStepResult(sr)
			s.fmt.Failed(pickle, step, match.GetInternalStepDefinition(), err)
		}
	}()

	// run before scenario handlers
	if isFirst {
		ctx, err = s.runBeforeScenarioHooks(ctx, pickle)
	}

	// run before step handlers
	ctx, err = s.runBeforeStepHooks(ctx, step, err)

	var matchError error
	match, matchError = s.matchStep(step)

	s.storage.MustInsertStepDefintionMatch(step.AstNodeIds[0], match)
	s.fmt.Defined(pickle, step, match.GetInternalStepDefinition())

	if err != nil {
		pickledAttachments := pickleAttachments(ctx)
		ctx = clearAttach(ctx)

		sr := models.NewStepResult(models.Failed, pickle.Id, step.Id, match, pickledAttachments, nil)
		s.storage.MustInsertPickleStepResult(sr)
		return ctx, err
	}

	if matchError != nil {
		return ctx, matchError
	}

	if ctx, undef, err := s.maybeUndefined(ctx, step.Text, step.Argument, step.Type); err != nil {
		return ctx, err
	} else if len(undef) > 0 {
		if match != nil {
			match = &models.StepDefinition{
				StepDefinition: formatters.StepDefinition{
					Expr:    match.Expr,
					Handler: match.Handler,
					Keyword: match.Keyword,
				},
				Args:         match.Args,
				HandlerValue: match.HandlerValue,
				File:         match.File,
				Line:         match.Line,
				Nested:       match.Nested,
				Undefined:    undef,
			}
		}

		pickledAttachments := pickleAttachments(ctx)
		ctx = clearAttach(ctx)

		sr := models.NewStepResult(models.Undefined, pickle.Id, step.Id, match, pickledAttachments, nil)
		s.storage.MustInsertPickleStepResult(sr)

		s.fmt.Undefined(pickle, step, match.GetInternalStepDefinition())
		return ctx, fmt.Errorf("%w: %s", ErrUndefined, step.Text)
	}

	if scenarioErr != nil {
		pickledAttachments := pickleAttachments(ctx)
		ctx = clearAttach(ctx)

		sr := models.NewStepResult(models.Skipped, pickle.Id, step.Id, match, pickledAttachments, nil)
		s.storage.MustInsertPickleStepResult(sr)

		s.fmt.Skipped(pickle, step, match.GetInternalStepDefinition())
		return ctx, nil
	}

	ctx, err = s.maybeSubSteps(match.Run(ctx))

	return ctx, err
}

func (s *suite) runBeforeStepHooks(ctx context.Context, step *Step, err error) (context.Context, error) {
	hooksFailed := false

	for _, f := range s.beforeStepHandlers {
		hctx, herr := f(ctx, step)
		if herr != nil {
			hooksFailed = true

			if err == nil {
				err = herr
			} else {
				err = fmt.Errorf("%v, %w", herr, err)
			}
		}

		if hctx != nil {
			ctx = hctx
		}
	}

	if hooksFailed {
		err = fmt.Errorf("before step hook failed: %w", err)
	}

	return ctx, err
}

func (s *suite) runAfterStepHooks(ctx context.Context, step *Step, status StepResultStatus, err error) (context.Context, error) {
	for _, f := range s.afterStepHandlers {
		hctx, herr := f(ctx, step, status, err)

		// Adding hook error to resulting error without breaking hooks loop.
		if herr != nil {
			if err == nil {
				err = herr
			} else {
				err = fmt.Errorf("%v, %w", herr, err)
			}
		}

		if hctx != nil {
			ctx = hctx
		}
	}

	return ctx, err
}

func (s *suite) runBeforeScenarioHooks(ctx context.Context, pickle *messages.Pickle) (context.Context, error) {
	var err error

	// run before scenario handlers
	for _, f := range s.beforeScenarioHandlers {
		hctx, herr := f(ctx, pickle)
		if herr != nil {
			if err == nil {
				err = herr
			} else {
				err = fmt.Errorf("%v, %w", herr, err)
			}
		}

		if hctx != nil {
			ctx = hctx
		}
	}

	if err != nil {
		err = fmt.Errorf("before scenario hook failed: %w", err)
	}

	return ctx, err
}

func (s *suite) runAfterScenarioHooks(ctx context.Context, pickle *messages.Pickle, lastStepErr error) (context.Context, error) {
	err := lastStepErr

	hooksFailed := false
	isStepErr := true

	// run after scenario handlers
	for _, f := range s.afterScenarioHandlers {
		hctx, herr := f(ctx, pickle, err)

		// Adding hook error to resulting error without breaking hooks loop.
		if herr != nil {
			hooksFailed = true

			if err == nil {
				isStepErr = false
				err = herr
			} else {
				if isStepErr {
					err = fmt.Errorf("step error: %w", err)
					isStepErr = false
				}
				err = fmt.Errorf("%v, %w", herr, err)
			}
		}

		if hctx != nil {
			ctx = hctx
		}
	}

	if hooksFailed {
		err = fmt.Errorf("after scenario hook failed: %w", err)
	}

	return ctx, err
}

func (s *suite) maybeUndefined(ctx context.Context, text string, arg interface{}, stepType messages.PickleStepType) (context.Context, []string, error) {
	var undefined []string
	step, err := s.matchStepTextAndType(text, stepType)
	if err != nil {
		return ctx, undefined, err
	}

	if nil == step {
		return ctx, []string{text}, nil
	}

	if !step.Nested {
		return ctx, undefined, nil
	}

	if arg != nil {
		step.Args = append(step.Args, arg)
	}

	ctx, steps := step.Run(ctx)

	for _, next := range steps.(Steps) {
		lines := strings.Split(next, "\n")
		// @TODO: we cannot currently parse table or content body from nested steps
		if len(lines) > 1 {
			return ctx, undefined, fmt.Errorf("nested steps cannot be multiline and have table or content body argument")
		}
		if len(lines[0]) > 0 && lines[0][len(lines[0])-1] == ':' {
			return ctx, undefined, fmt.Errorf("nested steps cannot be multiline and have table or content body argument")
		}
		ctx, undef, err := s.maybeUndefined(ctx, next, nil, messages.PickleStepType_UNKNOWN)
		if err != nil {
			return ctx, undefined, err
		}
		undefined = append(undefined, undef...)
	}
	return ctx, undefined, nil
}

func (s *suite) maybeSubSteps(ctx context.Context, result interface{}) (context.Context, error) {
	if nil == result {
		return ctx, nil
	}

	if err, ok := result.(error); ok {
		return ctx, err
	}

	steps, ok := result.(Steps)
	if !ok {
		return ctx, fmt.Errorf("unexpected error, should have been godog.Steps: %T - %+v", result, result)
	}

	for _, text := range steps {
		def, err := s.matchStepTextAndType(text, messages.PickleStepType_UNKNOWN)
		if err != nil {
			return ctx, err
		}

		if def == nil {
			return ctx, fmt.Errorf("%w: %s", ErrUndefined, text)
		} else {
			ctx, err = s.runSubStep(ctx, text, def)
			if err != nil {
				return ctx, err
			}
		}
	}
	return ctx, nil
}

func (s *suite) runSubStep(ctx context.Context, text string, def *models.StepDefinition) (_ context.Context, err error) {
	st := &Step{}
	st.Text = text
	st.Type = messages.PickleStepType_ACTION

	defer func() {
		status := StepPassed

		switch {
		case errors.Is(err, ErrUndefined):
			status = StepUndefined
		case errors.Is(err, ErrPending):
			status = StepPending
		case err != nil:
			status = StepFailed
		}

		ctx, err = s.runAfterStepHooks(ctx, st, status, err)
	}()

	ctx, err = s.runBeforeStepHooks(ctx, st, nil)
	if err != nil {
		return ctx, fmt.Errorf("%s: %+v", text, err)
	}

	if ctx, err = s.maybeSubSteps(def.Run(ctx)); err != nil {
		return ctx, fmt.Errorf("%s: %+v", text, err)
	}

	return ctx, nil
}

func (s *suite) matchStepTextAndType(text string, stepType messages.PickleStepType) (*models.StepDefinition, error) {
	var first *models.StepDefinition
	matchingExpressions := make([]string, 0)

	for _, h := range s.steps {
		if m := h.Expr.FindStringSubmatch(text); len(m) > 0 {
			if !keywordMatches(h.Keyword, stepType) {
				continue
			}
			var args []interface{}
			for _, m := range m[1:] {
				args = append(args, m)
			}

			matchingExpressions = append(matchingExpressions, h.Expr.String())

			// since we need to assign arguments
			// better to copy the step definition
			match := &models.StepDefinition{
				StepDefinition: formatters.StepDefinition{
					Expr:    h.Expr,
					Handler: h.Handler,
					Keyword: h.Keyword,
				},
				Args:         args,
				HandlerValue: h.HandlerValue,
				File:         h.File,
				Line:         h.Line,
				Nested:       h.Nested,
			}

			if first == nil {
				first = match
			}
		}
	}

	if s.strict {
		if len(matchingExpressions) > 1 {
			errs := "\n        " + strings.Join(matchingExpressions, "\n        ")
			return nil, fmt.Errorf("%w, step text: %s\n    matches:%s", ErrAmbiguous, text, errs)
		}
	}

	return first, nil
}

func keywordMatches(k formatters.Keyword, stepType messages.PickleStepType) bool {
	if k == formatters.None {
		return true
	}
	switch stepType {
	case messages.PickleStepType_CONTEXT:
		return k == formatters.Given
	case messages.PickleStepType_ACTION:
		return k == formatters.When
	case messages.PickleStepType_OUTCOME:
		return k == formatters.Then
	default:
		return true
	}
}

func (s *suite) runSteps(ctx context.Context, pickle *Scenario, steps []*Step) (context.Context, error) {
	var (
		stepErr, scenarioErr error
	)

	for i, step := range steps {
		isLast := i == len(steps)-1
		isFirst := i == 0
		ctx, stepErr = s.runStep(ctx, pickle, step, scenarioErr, isFirst, isLast)
		if scenarioErr == nil || s.shouldFail(stepErr) {
			scenarioErr = stepErr
		}
	}

	return ctx, scenarioErr
}

func (s *suite) shouldFail(err error) bool {
	if err == nil || errors.Is(err, ErrSkip) {
		return false
	}

	if errors.Is(err, ErrUndefined) || errors.Is(err, ErrPending) {
		return s.strict
	}

	return true
}

func (s *suite) runPickle(pickle *messages.Pickle) (err error) {
	ctx := s.defaultContext
	if ctx == nil {
		ctx = context.Background()
	}

	ctx, cancel := context.WithCancel(ctx)

	defer cancel()

	if len(pickle.Steps) == 0 {
		pr := models.PickleResult{PickleID: pickle.Id, StartedAt: utils.TimeNowFunc()}
		s.storage.MustInsertPickleResult(pr)

		s.fmt.Pickle(pickle)
		return fmt.Errorf("%w: no steps in scenario", ErrUndefined)
	}

	// Before scenario hooks are called in context of first evaluated step
	// so that error from handler can be added to step.

	pr := models.PickleResult{PickleID: pickle.Id, StartedAt: utils.TimeNowFunc()}
	s.storage.MustInsertPickleResult(pr)

	s.fmt.Pickle(pickle)

	dt := &testingT{
		name: pickle.Name,
	}
	ctx = setContextTestingT(ctx, dt)
	// scenario
	if s.testingT != nil {
		// Running scenario as a subtest.
		s.testingT.Run(pickle.Name, func(t *testing.T) {
			dt.t = t
			ctx, err = s.runSteps(ctx, pickle, pickle.Steps)
			if s.shouldFail(err) {
				t.Errorf("%+v", err)
			}
		})
	} else {
		ctx, err = s.runSteps(ctx, pickle, pickle.Steps)
	}

	// After scenario handlers are called in context of last evaluated step
	// so that error from handler can be added to step.

	return err
}
```

## File: `suite_context_test.go`
```go
package godog

import (
	"bytes"
	"context"
	"encoding/json"
	"encoding/xml"
	"errors"
	"fmt"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"
	"testing"
	"time"

	gherkin "github.com/cucumber/gherkin/go/v26"
	messages "github.com/cucumber/messages/go/v21"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/internal/formatters"
	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/parser"
	"github.com/cucumber/godog/internal/storage"
	"github.com/cucumber/godog/internal/tags"
	"github.com/cucumber/godog/internal/utils"
)

// InitializeScenario provides steps for godog suite execution and
// can be used for meta-testing of godog features/steps themselves.
//
// Beware, steps or their definitions might change without backward
// compatibility guarantees. A typical user of the godog library should never
// need this, rather it is provided for those developing add-on libraries for godog.
//
// For an example of how to use, see godog's own `features/` and `suite_test.go`.
func InitializeScenario(ctx *ScenarioContext) {
	tc := &godogFeaturesScenario{}

	ctx.Before(tc.ResetBeforeEachScenario)

	ctx.Step(`^(?:a )?feature path "([^"]*)"$`, tc.featurePath)
	ctx.Step(`^I parse features$`, tc.parseFeatures)
	ctx.Step(`^I'm listening to suite events$`, tc.iAmListeningToSuiteEvents)
	ctx.Step(`^I run feature suite$`, tc.iRunFeatureSuite)
	ctx.Step(`^I run feature suite with tags "([^"]*)"$`, tc.iRunFeatureSuiteWithTags)
	ctx.Step(`^I run feature suite with formatter "([^"]*)"$`, tc.iRunFeatureSuiteWithFormatter)
	ctx.Step(`^(?:I )(allow|disable) variable injection`, tc.iSetVariableInjectionTo)
	ctx.Step(`^(?:a )?feature "([^"]*)"(?: file)?:$`, tc.aFeatureFile)
	ctx.Step(`^the suite should have (passed|failed)$`, tc.theSuiteShouldHave)

	ctx.Step(`^I should have ([\d]+) features? files?:$`, tc.iShouldHaveNumFeatureFiles)
	ctx.Step(`^I should have ([\d]+) scenarios? registered$`, tc.numScenariosRegistered)
	ctx.Step(`^there (was|were) ([\d]+) "([^"]*)" events? fired$`, tc.thereWereNumEventsFired)
	ctx.Step(`^there was event triggered before scenario "([^"]*)"$`, tc.thereWasEventTriggeredBeforeScenario)
	ctx.Step(`^these events had to be fired for a number of times:$`, tc.theseEventsHadToBeFiredForNumberOfTimes)

	ctx.Step(`^(?:a )?failing step`, tc.aFailingStep)
	ctx.Step(`^this step should fail`, tc.aFailingStep)
	ctx.Step(`^the following steps? should be (passed|failed|skipped|undefined|pending):`, tc.followingStepsShouldHave)
	ctx.Step(`^the undefined step snippets should be:$`, tc.theUndefinedStepSnippetsShouldBe)

	// event stream
	ctx.Step(`^the following events should be fired:$`, tc.thereShouldBeEventsFired)

	// lt
	ctx.Step(`^savybių aplankas "([^"]*)"$`, tc.featurePath)
	ctx.Step(`^aš išskaitau savybes$`, tc.parseFeatures)
	ctx.Step(`^aš turėčiau turėti ([\d]+) savybių failus:$`, tc.iShouldHaveNumFeatureFiles)

	ctx.Step(`^(?:a )?pending step$`, func() error {
		return ErrPending
	})
	ctx.Step(`^(?:a )?passing step$`, func() error {
		return nil
	})
	ctx.Given(`^(?:a )?given step$`, func() error {
		return nil
	})
	ctx.When(`^(?:a )?when step$`, func() error {
		return nil
	})
	ctx.Then(`^(?:a )?then step$`, func() error {
		return nil
	})

	// Introduced to test formatter/cucumber.feature
	ctx.Step(`^the rendered json will be as follows:$`, tc.theRenderJSONWillBe)

	// Introduced to test formatter/pretty.feature
	ctx.Step(`^the rendered output will be as follows:$`, tc.theRenderOutputWillBe)

	// Introduced to test formatter/junit.feature
	ctx.Step(`^the rendered xml will be as follows:$`, tc.theRenderXMLWillBe)

	ctx.Step(`^(?:a )?failing multistep$`, func() Steps {
		return Steps{"passing step", "failing step"}
	})

	ctx.Step(`^(?:a |an )?undefined multistep$`, func() Steps {
		return Steps{"passing step", "undefined step", "passing step"}
	})

	ctx.Then(`^(?:a |an )?undefined multistep using 'then' function$`, func() Steps {
		return Steps{"given step", "undefined step", "then step"}
	})

	ctx.Step(`^(?:a )?passing multistep$`, func() Steps {
		return Steps{"passing step", "passing step", "passing step"}
	})

	ctx.Then(`^(?:a )?passing multistep using 'then' function$`, func() Steps {
		return Steps{"given step", "when step", "then step"}
	})

	ctx.Step(`^(?:a )?failing nested multistep$`, func() Steps {
		return Steps{"passing step", "passing multistep", "failing multistep"}
	})
	// Default recovery step
	ctx.Step(`Ignore.*`, func() error {
		return nil
	})

	ctx.Step(`^call func\(\*godog\.DocString\) with:$`, func(arg *DocString) error {
		return nil
	})
	ctx.Step(`^call func\(string\) with:$`, func(arg string) error {
		return nil
	})

	ctx.Step(`^passing step without return$`, func() {})

	ctx.Step(`^having correct context$`, func(ctx context.Context) (context.Context, error) {
		if ctx.Value(ctxKey("BeforeScenario")) == nil {
			return ctx, errors.New("missing BeforeScenario in context")
		}

		if ctx.Value(ctxKey("BeforeStep")) == nil {
			return ctx, errors.New("missing BeforeStep in context")
		}

		if ctx.Value(ctxKey("StepState")) == nil {
			return ctx, errors.New("missing StepState in context")
		}

		return context.WithValue(ctx, ctxKey("Step"), true), nil
	})

	ctx.Step(`^adding step state to context$`, func(ctx context.Context) context.Context {
		return context.WithValue(ctx, ctxKey("StepState"), true)
	})

	ctx.Step(`^I return a context from a step$`, tc.iReturnAContextFromAStep)
	ctx.Step(`^I should see the context in the next step$`, tc.iShouldSeeTheContextInTheNextStep)
	ctx.Step(`^I can see contexts passed in multisteps$`, func() Steps {
		return Steps{
			"I return a context from a step",
			"I should see the context in the next step",
		}
	})

	// introduced to test testingT
	ctx.Step(`^my step (?:fails|skips) the test by calling (FailNow|Fail|SkipNow|Skip) on testing T$`, tc.myStepCallsTFailErrorSkip)
	ctx.Step(`^my step fails the test by calling (Fatal|Error) on testing T with message "([^"]*)"$`, tc.myStepCallsTErrorFatal)
	ctx.Step(`^my step fails the test by calling (Fatalf|Errorf) on testing T with message "([^"]*)" and argument "([^"]*)"$`, tc.myStepCallsTErrorfFatalf)
	ctx.Step(`^my step calls Log on testing T with message "([^"]*)"$`, tc.myStepCallsTLog)
	ctx.Step(`^my step calls Logf on testing T with message "([^"]*)" and argument "([^"]*)"$`, tc.myStepCallsTLogf)
	ctx.Step(`^my step calls testify's assert.Equal with expected "([^"]*)" and actual "([^"]*)"$`, tc.myStepCallsTestifyAssertEqual)
	ctx.Step(`^my step calls testify's require.Equal with expected "([^"]*)" and actual "([^"]*)"$`, tc.myStepCallsTestifyRequireEqual)
	ctx.Step(`^my step calls testify's assert.Equal ([0-9]+) times(| with match)$`, tc.myStepCallsTestifyAssertEqualMultipleTimes)
	ctx.Step(`^my step calls godog.Log with message "([^"]*)"$`, tc.myStepCallsDogLog)
	ctx.Step(`^my step calls godog.Logf with message "([^"]*)" and argument "([^"]*)"$`, tc.myStepCallsDogLogf)
	ctx.Step(`^the logged messages should include "([^"]*)"$`, tc.theLoggedMessagesShouldInclude)

	ctx.StepContext().Before(tc.inject)
}

type ctxKey string

func (tc *godogFeaturesScenario) inject(ctx context.Context, step *Step) (context.Context, error) {
	if !tc.allowInjection {
		return ctx, nil
	}

	step.Text = injectAll(step.Text)

	if step.Argument == nil {
		return ctx, nil
	}

	if table := step.Argument.DataTable; table != nil {
		for i := 0; i < len(table.Rows); i++ {
			for n, cell := range table.Rows[i].Cells {
				table.Rows[i].Cells[n].Value = injectAll(cell.Value)
			}
		}
	}

	if doc := step.Argument.DocString; doc != nil {
		doc.Content = injectAll(doc.Content)
	}

	return ctx, nil
}

func injectAll(src string) string {
	re := regexp.MustCompile(`{{[^{}]+}}`)
	return re.ReplaceAllStringFunc(
		src,
		func(key string) string {
			injectRegex := regexp.MustCompile(`^{{.+}}$`)

			if injectRegex.MatchString(key) {
				return "someverylonginjectionsoweacanbesureitsurpasstheinitiallongeststeplenghtanditwillhelptestsmethodsafety"
			}

			return key
		},
	)
}

type firedEvent struct {
	name string
	args []interface{}
}

type godogFeaturesScenario struct {
	paths            []string
	features         []*models.Feature
	testedSuite      *suite
	testSuiteContext TestSuiteContext
	events           []*firedEvent
	out              bytes.Buffer
	allowInjection   bool
}

func (tc *godogFeaturesScenario) ResetBeforeEachScenario(ctx context.Context, sc *Scenario) (context.Context, error) {
	// reset whole suite with the state
	tc.out.Reset()
	tc.paths = []string{}

	tc.features = []*models.Feature{}
	tc.testedSuite = &suite{}
	tc.testSuiteContext = TestSuiteContext{}

	// reset all fired events
	tc.events = []*firedEvent{}
	tc.allowInjection = false

	return ctx, nil
}

func (tc *godogFeaturesScenario) iSetVariableInjectionTo(to string) error {
	tc.allowInjection = to == "allow"
	return nil
}

func (tc *godogFeaturesScenario) iRunFeatureSuiteWithTags(tags string) error {
	return tc.iRunFeatureSuiteWithTagsAndFormatter(tags, formatters.BaseFormatterFunc)
}

func (tc *godogFeaturesScenario) iRunFeatureSuiteWithFormatter(name string) error {
	f := FindFmt(name)
	if f == nil {
		return fmt.Errorf(`formatter "%s" is not available`, name)
	}

	return tc.iRunFeatureSuiteWithTagsAndFormatter("", f)
}

func (tc *godogFeaturesScenario) iRunFeatureSuiteWithTagsAndFormatter(filter string, fmtFunc FormatterFunc) error {
	if err := tc.parseFeatures(); err != nil {
		return err
	}

	for _, feat := range tc.features {
		feat.Pickles = tags.ApplyTagFilter(filter, feat.Pickles)
	}

	tc.testedSuite.storage = storage.NewStorage()
	for _, feat := range tc.features {
		tc.testedSuite.storage.MustInsertFeature(feat)

		for _, pickle := range feat.Pickles {
			tc.testedSuite.storage.MustInsertPickle(pickle)
		}
	}

	tc.testedSuite.fmt = fmtFunc("godog", colors.Uncolored(&tc.out))
	if fmt, ok := tc.testedSuite.fmt.(storageFormatter); ok {
		fmt.SetStorage(tc.testedSuite.storage)
	}

	testRunStarted := models.TestRunStarted{StartedAt: utils.TimeNowFunc()}
	tc.testedSuite.storage.MustInsertTestRunStarted(testRunStarted)
	tc.testedSuite.fmt.TestRunStarted()

	for _, f := range tc.testSuiteContext.beforeSuiteHandlers {
		f()
	}

	for _, ft := range tc.features {
		tc.testedSuite.fmt.Feature(ft.GherkinDocument, ft.Uri, ft.Content)

		for _, pickle := range ft.Pickles {
			if tc.testedSuite.stopOnFailure && tc.testedSuite.failed {
				continue
			}

			sc := ScenarioContext{suite: tc.testedSuite}
			InitializeScenario(&sc)

			err := tc.testedSuite.runPickle(pickle)
			if tc.testedSuite.shouldFail(err) {
				tc.testedSuite.failed = true
			}
		}
	}

	for _, f := range tc.testSuiteContext.afterSuiteHandlers {
		f()
	}

	tc.testedSuite.fmt.Summary()

	return nil
}

func (tc *godogFeaturesScenario) thereShouldBeEventsFired(doc *DocString) error {
	actual := strings.Split(strings.TrimSpace(tc.out.String()), "\n")
	expect := strings.Split(strings.TrimSpace(doc.Content), "\n")

	if len(expect) != len(actual) {
		return fmt.Errorf("expected %d events, but got %d", len(expect), len(actual))
	}

	type ev struct {
		Event string
	}

	for i, event := range actual {
		exp := strings.TrimSpace(expect[i])
		var act ev

		if err := json.Unmarshal([]byte(event), &act); err != nil {
			return fmt.Errorf("failed to read event data: %v", err)
		}

		if act.Event != exp {
			return fmt.Errorf(`expected event: "%s" at position: %d, but actual was "%s"`, exp, i, act.Event)
		}
	}

	return nil
}

func (tc *godogFeaturesScenario) cleanupSnippet(snip string) string {
	lines := strings.Split(strings.TrimSpace(snip), "\n")
	for i := 0; i < len(lines); i++ {
		lines[i] = strings.TrimSpace(lines[i])
	}

	return strings.Join(lines, "\n")
}

func (tc *godogFeaturesScenario) theUndefinedStepSnippetsShouldBe(body *DocString) error {
	f, ok := tc.testedSuite.fmt.(*formatters.Base)
	if !ok {
		return fmt.Errorf("this step requires *formatters.Base, but there is: %T", tc.testedSuite.fmt)
	}

	actual := tc.cleanupSnippet(f.Snippets())
	expected := tc.cleanupSnippet(body.Content)

	if actual != expected {
		return fmt.Errorf("snippets do not match actual: %s", f.Snippets())
	}

	return nil
}

type multiContextKey struct{}

func (tc *godogFeaturesScenario) iReturnAContextFromAStep(ctx context.Context) (context.Context, error) {
	return context.WithValue(ctx, multiContextKey{}, "value"), nil
}

func (tc *godogFeaturesScenario) iShouldSeeTheContextInTheNextStep(ctx context.Context) error {
	value, ok := ctx.Value(multiContextKey{}).(string)
	if !ok {
		return errors.New("context does not contain our key")
	}
	if value != "value" {
		return errors.New("context has the wrong value for our key")
	}
	return nil
}

func (tc *godogFeaturesScenario) myStepCallsTFailErrorSkip(ctx context.Context, op string) error {
	switch op {
	case "FailNow":
		T(ctx).FailNow()
	case "Fail":
		T(ctx).Fail()
	case "SkipNow":
		T(ctx).SkipNow()
	case "Skip":
		T(ctx).Skip()
	default:
		return fmt.Errorf("operation %s not supported by iCallTFailErrorSkip", op)
	}
	return nil
}

func (tc *godogFeaturesScenario) myStepCallsTErrorFatal(ctx context.Context, op string, message string) error {
	switch op {
	case "Error":
		T(ctx).Error(message)
	case "Fatal":
		T(ctx).Fatal(message)
	default:
		return fmt.Errorf("operation %s not supported by iCallTErrorFatal", op)
	}
	return nil
}

func (tc *godogFeaturesScenario) myStepCallsTErrorfFatalf(ctx context.Context, op string, message string, arg string) error {
	switch op {
	case "Errorf":
		T(ctx).Errorf(message, arg)
	case "Fatalf":
		T(ctx).Fatalf(message, arg)
	default:
		return fmt.Errorf("operation %s not supported by iCallTErrorfFatalf", op)
	}
	return nil
}

func (tc *godogFeaturesScenario) myStepCallsTestifyAssertEqual(ctx context.Context, a string, b string) error {
	assert.Equal(T(ctx), a, b)
	return nil
}

func (tc *godogFeaturesScenario) myStepCallsTestifyAssertEqualMultipleTimes(ctx context.Context, times string, withMatch string) error {
	timesInt, err := strconv.Atoi(times)
	if err != nil {
		return fmt.Errorf("test step has invalid times value %s: %w", times, err)
	}
	for i := 0; i < timesInt; i++ {
		if withMatch == " with match" {
			assert.Equal(T(ctx), fmt.Sprintf("exp%v", i), fmt.Sprintf("exp%v", i))
		} else {
			assert.Equal(T(ctx), "exp", fmt.Sprintf("notexp%v", i))
		}
	}
	return nil
}

func (tc *godogFeaturesScenario) myStepCallsTestifyRequireEqual(ctx context.Context, a string, b string) error {
	require.Equal(T(ctx), a, b)
	return nil
}

func (tc *godogFeaturesScenario) myStepCallsTLog(ctx context.Context, message string) error {
	T(ctx).Log(message)
	return nil
}

func (tc *godogFeaturesScenario) myStepCallsTLogf(ctx context.Context, message string, arg string) error {
	T(ctx).Logf(message, arg)
	return nil
}

func (tc *godogFeaturesScenario) myStepCallsDogLog(ctx context.Context, message string) error {
	Log(ctx, message)
	return nil
}

func (tc *godogFeaturesScenario) myStepCallsDogLogf(ctx context.Context, message string, arg string) error {
	Logf(ctx, message, arg)
	return nil
}

func (tc *godogFeaturesScenario) theLoggedMessagesShouldInclude(ctx context.Context, message string) error {
	messages := LoggedMessages(ctx)
	for _, m := range messages {
		if strings.Contains(m, message) {
			return nil
		}
	}
	return fmt.Errorf("the message %q was not logged (logged messages: %v)", message, messages)
}

func (tc *godogFeaturesScenario) followingStepsShouldHave(status string, steps *DocString) error {
	expected := strings.Split(steps.Content, "\n")
	var actual, unmatched, matched []string

	storage := tc.testedSuite.storage

	switch status {
	case "passed":
		for _, st := range storage.MustGetPickleStepResultsByStatus(models.Passed) {
			pickleStep := storage.MustGetPickleStep(st.PickleStepID)
			actual = append(actual, pickleStep.Text)
		}
	case "failed":
		for _, st := range storage.MustGetPickleStepResultsByStatus(models.Failed) {
			pickleStep := storage.MustGetPickleStep(st.PickleStepID)
			actual = append(actual, pickleStep.Text)
		}
	case "skipped":
		for _, st := range storage.MustGetPickleStepResultsByStatus(models.Skipped) {
			pickleStep := storage.MustGetPickleStep(st.PickleStepID)
			actual = append(actual, pickleStep.Text)
		}
	case "undefined":
		for _, st := range storage.MustGetPickleStepResultsByStatus(models.Undefined) {
			pickleStep := storage.MustGetPickleStep(st.PickleStepID)
			actual = append(actual, pickleStep.Text)
		}
	case "pending":
		for _, st := range storage.MustGetPickleStepResultsByStatus(models.Pending) {
			pickleStep := storage.MustGetPickleStep(st.PickleStepID)
			actual = append(actual, pickleStep.Text)
		}
	default:
		return fmt.Errorf("unexpected step status wanted: %s", status)
	}

	if len(expected) > len(actual) {
		return fmt.Errorf("number of expected %s steps: %d is less than actual %s steps: %d", status, len(expected), status, len(actual))
	}

	for _, a := range actual {
		for _, e := range expected {
			if a == e {
				matched = append(matched, e)
				break
			}
		}
	}

	if len(matched) >= len(expected) {
		return nil
	}

	for _, s := range expected {
		var found bool
		for _, m := range matched {
			if s == m {
				found = true
				break
			}
		}

		if !found {
			unmatched = append(unmatched, s)
		}
	}

	return fmt.Errorf("the steps: %s - are not %s", strings.Join(unmatched, ", "), status)
}

func (tc *godogFeaturesScenario) iAmListeningToSuiteEvents() error {
	tc.testSuiteContext.BeforeSuite(func() {
		tc.events = append(tc.events, &firedEvent{"BeforeSuite", []interface{}{}})
	})

	tc.testSuiteContext.AfterSuite(func() {
		tc.events = append(tc.events, &firedEvent{"AfterSuite", []interface{}{}})
	})

	scenarioContext := ScenarioContext{suite: tc.testedSuite}

	scenarioContext.Before(func(ctx context.Context, pickle *Scenario) (context.Context, error) {
		tc.events = append(tc.events, &firedEvent{"BeforeScenario", []interface{}{pickle}})

		if ctx.Value(ctxKey("BeforeScenario")) != nil {
			return ctx, errors.New("unexpected BeforeScenario in context (double invocation)")
		}

		return context.WithValue(ctx, ctxKey("BeforeScenario"), pickle.Name), nil
	})

	scenarioContext.Before(func(ctx context.Context, sc *Scenario) (context.Context, error) {
		if sc.Name == "failing before and after scenario" || sc.Name == "failing before scenario" {
			return context.WithValue(ctx, ctxKey("AfterStep"), sc.Name), errors.New("failed in before scenario hook")
		}

		return ctx, nil
	})

	scenarioContext.After(func(ctx context.Context, sc *Scenario, err error) (context.Context, error) {
		if sc.Name == "failing before and after scenario" || sc.Name == "failing after scenario" {
			return ctx, errors.New("failed in after scenario hook")
		}

		return ctx, nil
	})

	scenarioContext.After(func(ctx context.Context, pickle *Scenario, err error) (context.Context, error) {
		tc.events = append(tc.events, &firedEvent{"AfterScenario", []interface{}{pickle, err}})

		if ctx.Value(ctxKey("BeforeScenario")) == nil {
			return ctx, errors.New("missing BeforeScenario in context")
		}

		if ctx.Value(ctxKey("AfterStep")) == nil {
			return ctx, errors.New("missing AfterStep in context")
		}

		return context.WithValue(ctx, ctxKey("AfterScenario"), pickle.Name), nil
	})

	scenarioContext.StepContext().Before(func(ctx context.Context, step *Step) (context.Context, error) {
		tc.events = append(tc.events, &firedEvent{"BeforeStep", []interface{}{step}})

		if ctx.Value(ctxKey("BeforeScenario")) == nil {
			return ctx, errors.New("missing BeforeScenario in context")
		}

		return context.WithValue(ctx, ctxKey("BeforeStep"), step.Text), nil
	})

	scenarioContext.StepContext().After(func(ctx context.Context, step *Step, status StepResultStatus, err error) (context.Context, error) {
		tc.events = append(tc.events, &firedEvent{"AfterStep", []interface{}{step, err}})

		if ctx.Value(ctxKey("BeforeScenario")) == nil {
			return ctx, errors.New("missing BeforeScenario in context")
		}

		if ctx.Value(ctxKey("AfterScenario")) != nil && status != models.Skipped {
			panic("unexpected premature AfterScenario during AfterStep: " + ctx.Value(ctxKey("AfterScenario")).(string))
		}

		if ctx.Value(ctxKey("BeforeStep")) == nil {
			return ctx, errors.New("missing BeforeStep in context")
		}

		if step.Text == "having correct context" && ctx.Value(ctxKey("Step")) == nil {
			if status != StepSkipped {
				return ctx, fmt.Errorf("unexpected step result status: %s", status)
			}

			return ctx, errors.New("missing Step in context")
		}

		return context.WithValue(ctx, ctxKey("AfterStep"), step.Text), nil
	})

	return nil
}

func (tc *godogFeaturesScenario) aFailingStep() error {
	return fmt.Errorf("intentional failure")
}

// parse a given feature file body as a feature
func (tc *godogFeaturesScenario) aFeatureFile(path string, body *DocString) error {
	gd, err := gherkin.ParseGherkinDocument(strings.NewReader(body.Content), (&messages.Incrementing{}).NewId)
	gd.Uri = path

	pickles := gherkin.Pickles(*gd, path, (&messages.Incrementing{}).NewId)
	tc.features = append(tc.features, &models.Feature{GherkinDocument: gd, Pickles: pickles})

	return err
}

func (tc *godogFeaturesScenario) featurePath(path string) {
	tc.paths = append(tc.paths, path)
}

func (tc *godogFeaturesScenario) parseFeatures() error {
	fts, err := parser.ParseFeatures(storage.FS{}, "", "", tc.paths)
	if err != nil {
		return err
	}

	tc.features = append(tc.features, fts...)

	return nil
}

func (tc *godogFeaturesScenario) theSuiteShouldHave(state string) error {
	if tc.testedSuite.failed && state == "passed" {
		return fmt.Errorf("the feature suite has failed")
	}

	if !tc.testedSuite.failed && state == "failed" {
		return fmt.Errorf("the feature suite has passed")
	}

	return nil
}

func (tc *godogFeaturesScenario) iShouldHaveNumFeatureFiles(num int, files *DocString) error {
	if len(tc.features) != num {
		return fmt.Errorf("expected %d features to be parsed, but have %d", num, len(tc.features))
	}

	expected := strings.Split(files.Content, "\n")

	var actual []string

	for _, ft := range tc.features {
		actual = append(actual, ft.Uri)
	}

	if len(expected) != len(actual) {
		return fmt.Errorf("expected %d feature paths to be parsed, but have %d", len(expected), len(actual))
	}

	for i := 0; i < len(expected); i++ {
		var matched bool
		split := strings.Split(expected[i], "/")
		exp := filepath.Join(split...)

		for j := 0; j < len(actual); j++ {
			split = strings.Split(actual[j], "/")
			act := filepath.Join(split...)

			if exp == act {
				matched = true
				break
			}
		}

		if !matched {
			return fmt.Errorf(`expected feature path "%s" at position: %d, was not parsed, actual are %+v`, exp, i, actual)
		}
	}

	return nil
}

func (tc *godogFeaturesScenario) iRunFeatureSuite() error {
	return tc.iRunFeatureSuiteWithTags("")
}

func (tc *godogFeaturesScenario) numScenariosRegistered(expected int) (err error) {
	var num int
	for _, ft := range tc.features {
		num += len(ft.Pickles)
	}

	if num != expected {
		err = fmt.Errorf("expected %d scenarios to be registered, but got %d", expected, num)
	}

	return
}

func (tc *godogFeaturesScenario) thereWereNumEventsFired(_ string, expected int, typ string) error {
	var num int
	for _, event := range tc.events {
		if event.name == typ {
			num++
		}
	}

	if num != expected {
		if typ == "BeforeFeature" || typ == "AfterFeature" {
			return nil
		}

		return fmt.Errorf("expected %d %s events to be fired, but got %d", expected, typ, num)
	}

	return nil
}

func (tc *godogFeaturesScenario) thereWasEventTriggeredBeforeScenario(expected string) error {
	var found []string
	for _, event := range tc.events {
		if event.name != "BeforeScenario" {
			continue
		}

		var name string
		switch t := event.args[0].(type) {
		case *Scenario:
			name = t.Name
		}

		if name == expected {
			return nil
		}

		found = append(found, name)
	}

	if len(found) == 0 {
		return fmt.Errorf("before scenario event was never triggered or listened")
	}

	return fmt.Errorf(`expected "%s" scenario, but got these fired %s`, expected, `"`+strings.Join(found, `", "`)+`"`)
}

func (tc *godogFeaturesScenario) theseEventsHadToBeFiredForNumberOfTimes(tbl *Table) error {
	if len(tbl.Rows[0].Cells) != 2 {
		return fmt.Errorf("expected two columns for event table row, got: %d", len(tbl.Rows[0].Cells))
	}

	for _, row := range tbl.Rows {
		num, err := strconv.ParseInt(row.Cells[1].Value, 10, 0)
		if err != nil {
			return err
		}

		if err := tc.thereWereNumEventsFired("", int(num), row.Cells[0].Value); err != nil {
			return err
		}
	}

	return nil
}

func (tc *godogFeaturesScenario) theRenderJSONWillBe(docstring *DocString) error {
	expectedSuiteCtxReg := regexp.MustCompile(`suite_context.go:\d+`)
	actualSuiteCtxReg := regexp.MustCompile(`(suite_context_test\.go|\\u003cautogenerated\\u003e):\d+`)

	expectedString := docstring.Content
	expectedString = expectedSuiteCtxReg.ReplaceAllString(expectedString, `<autogenerated>:0`)

	actualString := tc.out.String()
	actualString = actualSuiteCtxReg.ReplaceAllString(actualString, `<autogenerated>:0`)

	var expected []formatters.CukeFeatureJSON
	if err := json.Unmarshal([]byte(expectedString), &expected); err != nil {
		return err
	}

	var actual []formatters.CukeFeatureJSON
	if err := json.Unmarshal([]byte(actualString), &actual); err != nil {
		return err
	}

	return assertExpectedAndActual(assert.Equal, expected, actual)
}

func (tc *godogFeaturesScenario) theRenderOutputWillBe(docstring *DocString) error {
	expectedSuiteCtxReg := regexp.MustCompile(`(suite_context\.go|suite_context_test\.go):\d+`)
	actualSuiteCtxReg := regexp.MustCompile(`(suite_context_test\.go|\<autogenerated\>):\d+`)

	expectedSuiteCtxFuncReg := regexp.MustCompile(`SuiteContext.func(\d+)`)
	actualSuiteCtxFuncReg := regexp.MustCompile(`github.com/cucumber/godog.InitializeScenario.func(\d+)`)

	suiteCtxPtrReg := regexp.MustCompile(`\*suiteContext`)

	expected := docstring.Content
	expected = trimAllLines(expected)
	expected = expectedSuiteCtxReg.ReplaceAllString(expected, "<autogenerated>:0")
	expected = expectedSuiteCtxFuncReg.ReplaceAllString(expected, "InitializeScenario.func$1")
	expected = suiteCtxPtrReg.ReplaceAllString(expected, "*godogFeaturesScenario")

	actual := tc.out.String()
	actual = actualSuiteCtxReg.ReplaceAllString(actual, "<autogenerated>:0")
	actual = actualSuiteCtxFuncReg.ReplaceAllString(actual, "InitializeScenario.func$1")
	actualTrimmed := actual
	actual = trimAllLines(actual)

	return assertExpectedAndActual(assert.Equal, expected, actual, actualTrimmed)
}

func (tc *godogFeaturesScenario) theRenderXMLWillBe(docstring *DocString) error {
	expectedString := docstring.Content
	actualString := tc.out.String()

	var expected formatters.JunitPackageSuite
	if err := xml.Unmarshal([]byte(expectedString), &expected); err != nil {
		return err
	}

	var actual formatters.JunitPackageSuite
	if err := xml.Unmarshal([]byte(actualString), &actual); err != nil {
		return err
	}

	return assertExpectedAndActual(assert.Equal, expected, actual)
}

func assertExpectedAndActual(a expectedAndActualAssertion, expected, actual interface{}, msgAndArgs ...interface{}) error {
	var t asserter
	a(&t, expected, actual, msgAndArgs...)

	if t.err != nil {
		return t.err
	}

	return t.err
}

type expectedAndActualAssertion func(t assert.TestingT, expected, actual interface{}, msgAndArgs ...interface{}) bool

type asserter struct {
	err error
}

func (a *asserter) Errorf(format string, args ...interface{}) {
	a.err = fmt.Errorf(format, args...)
}

func trimAllLines(s string) string {
	var lines []string
	for _, ln := range strings.Split(strings.TrimSpace(s), "\n") {
		lines = append(lines, strings.TrimSpace(ln))
	}
	return strings.Join(lines, "\n")
}

func TestScenarioContext_After_cancelled(t *testing.T) {
	ctxDone := make(chan struct{})
	suite := TestSuite{
		ScenarioInitializer: func(scenarioContext *ScenarioContext) {
			scenarioContext.When(`^foo$`, func() {})
			scenarioContext.After(func(ctx context.Context, sc *Scenario, err error) (context.Context, error) {
				go func() {
					<-ctx.Done()
					close(ctxDone)
				}()

				return ctx, nil
			})
		},
		Options: &Options{
			Format:   "pretty",
			TestingT: t,
			FeatureContents: []Feature{
				{
					Name: "Scenario Context Cancellation",
					Contents: []byte(`
Feature: dummy
  Scenario: Context should be cancelled by the end of scenario
    When foo
`),
				},
			},
		},
	}

	require.Equal(t, 0, suite.Run(), "non-zero status returned, failed to run feature tests")

	select {
	case <-ctxDone:
		return
	case <-time.After(5 * time.Second):
		assert.Fail(t, "failed to wait for context cancellation")
	}
}

func TestTestSuite_Run(t *testing.T) {
	for _, tc := range []struct {
		name          string
		body          string
		afterStepCnt  int
		beforeStepCnt int
		log           string
		noStrict      bool
		suitePasses   bool
	}{
		{
			name: "fail_then_pass_fails_scenario", afterStepCnt: 2, beforeStepCnt: 2,
			body: `
					When step fails
					Then step passes`,
			log: `
					>>>> Before suite
					>> Before scenario "test"
					Before step "step fails"
					After step "step fails", error: oops, status: failed
					<< After scenario "test", error: oops
					Before step "step passes"
					After step "step passes", error: <nil>, status: skipped
					<<<< After suite`,
		},
		{
			name: "pending_then_pass_fails_scenario", afterStepCnt: 2, beforeStepCnt: 2,
			body: `
					When step is pending
					Then step passes`,
			log: `
					>>>> Before suite
					>> Before scenario "test"
					Before step "step is pending"
					After step "step is pending", error: step implementation is pending, status: pending
					<< After scenario "test", error: step implementation is pending
					Before step "step passes"
					After step "step passes", error: <nil>, status: skipped
					<<<< After suite`,
		},
		{
			name: "pending_then_pass_no_strict_doesnt_fail_scenario", afterStepCnt: 2, beforeStepCnt: 2, noStrict: true, suitePasses: true,
			body: `
					When step is pending
					Then step passes`,
			log: `
					>>>> Before suite
					>> Before scenario "test"
					Before step "step is pending"
					After step "step is pending", error: step implementation is pending, status: pending
					Before step "step passes"
					After step "step passes", error: <nil>, status: skipped
					<< After scenario "test", error: <nil>
					<<<< After suite`,
		},
		{
			name: "undefined_then_pass_no_strict_doesnt_fail_scenario", afterStepCnt: 2, beforeStepCnt: 2, noStrict: true, suitePasses: true,
			body: `
					When something unknown happens
					Then step passes`,
			log: `
					>>>> Before suite
					>> Before scenario "test"
					Before step "something unknown happens"
					After step "something unknown happens", error: step is undefined: something unknown happens, status: undefined
					Before step "step passes"
					After step "step passes", error: <nil>, status: skipped
					<< After scenario "test", error: <nil>
					<<<< After suite`,
		},
		{
			name: "undefined_then_pass_fails_scenario", afterStepCnt: 2, beforeStepCnt: 2,
			body: `
					When something unknown happens
					Then step passes`,
			log: `
					>>>> Before suite
					>> Before scenario "test"
					Before step "something unknown happens"
					After step "something unknown happens", error: step is undefined: something unknown happens, status: undefined
					<< After scenario "test", error: step is undefined: something unknown happens
					Before step "step passes"
					After step "step passes", error: <nil>, status: skipped
					<<<< After suite`,
		},
		{
			name: "fail_then_undefined_fails_scenario", afterStepCnt: 2, beforeStepCnt: 2,
			body: `
					When step fails
					Then something unknown happens`,
			log: `
					>>>> Before suite
					>> Before scenario "test"
					Before step "step fails"
					After step "step fails", error: oops, status: failed
					<< After scenario "test", error: oops
					Before step "something unknown happens"
					After step "something unknown happens", error: step is undefined: something unknown happens, status: undefined
					<<<< After suite`,
		},
		{
			name: "passes", afterStepCnt: 2, beforeStepCnt: 2,
			body: `
					When step passes
					Then step passes`,
			suitePasses: true,
			log: `
					>>>> Before suite
					>> Before scenario "test"
					Before step "step passes"
					<step action>
					After step "step passes", error: <nil>, status: passed
					Before step "step passes"
					<step action>
					After step "step passes", error: <nil>, status: passed
					<< After scenario "test", error: <nil>
					<<<< After suite`,
		},
		{
			name: "skip_does_not_fail_scenario", afterStepCnt: 2, beforeStepCnt: 2,
			body: `
					When step skips scenario
					Then step fails`,
			suitePasses: true,
			log: `
					>>>> Before suite
					>> Before scenario "test"
					Before step "step skips scenario"
					After step "step skips scenario", error: skipped, status: skipped
					Before step "step fails"
					After step "step fails", error: <nil>, status: skipped
					<< After scenario "test", error: <nil>
					<<<< After suite`,
		},
		{
			name: "multistep_passes", afterStepCnt: 6, beforeStepCnt: 6,
			body: `
					When multistep passes
					Then multistep passes`,
			suitePasses: true,
			log: `
					>>>> Before suite
					>> Before scenario "test"
					Before step "multistep passes"
					Before step "step passes"
					<step action>
					After step "step passes", error: <nil>, status: passed
					Before step "step passes"
					<step action>
					After step "step passes", error: <nil>, status: passed
					After step "multistep passes", error: <nil>, status: passed
					Before step "multistep passes"
					Before step "step passes"
					<step action>
					After step "step passes", error: <nil>, status: passed
					Before step "step passes"
					<step action>
					After step "step passes", error: <nil>, status: passed
					After step "multistep passes", error: <nil>, status: passed
					<< After scenario "test", error: <nil>
					<<<< After suite`,
		},
		{
			name: "ambiguous", afterStepCnt: 1, beforeStepCnt: 1,
			body: `
					Then step is ambiguous`,
			log: `
					>>>> Before suite
					>> Before scenario "test"
					Before step "step is ambiguous"
					After step "step is ambiguous", error: ambiguous step definition, step text: step is ambiguous
		        	            		matches:
		        	            			^step is ambiguous$
		        	            			^step is ambiguous$, status: ambiguous
					<< After scenario "test", error: ambiguous step definition, step text: step is ambiguous
		        	            		matches:
		        	            			^step is ambiguous$
		        	            			^step is ambiguous$
					<<<< After suite`,
		},
		{
			name: "ambiguous nested steps", afterStepCnt: 1, beforeStepCnt: 1,
			body: `
				Then multistep has ambiguous`,
			log: `
				>>>> Before suite
				>> Before scenario "test"
				Before step "multistep has ambiguous"
				After step "multistep has ambiguous", error: ambiguous step definition, step text: step is ambiguous
            	            		matches:
            	            			^step is ambiguous$
            	            			^step is ambiguous$, status: ambiguous
				<< After scenario "test", error: ambiguous step definition, step text: step is ambiguous
            	            		matches:
            	            			^step is ambiguous$
            	            			^step is ambiguous$
				<<<< After suite`,
		},
	} {
		t.Run(tc.name, func(t *testing.T) {
			afterScenarioCnt := 0
			beforeScenarioCnt := 0

			afterStepCnt := 0
			beforeStepCnt := 0

			var log string

			suite := TestSuite{
				TestSuiteInitializer: func(suiteContext *TestSuiteContext) {
					suiteContext.BeforeSuite(func() {
						log += fmt.Sprintln(">>>> Before suite")
					})

					suiteContext.AfterSuite(func() {
						log += fmt.Sprintln("<<<< After suite")
					})
				},
				ScenarioInitializer: func(s *ScenarioContext) {
					s.Before(func(ctx context.Context, sc *Scenario) (context.Context, error) {
						log += fmt.Sprintf(">> Before scenario %q\n", sc.Name)
						beforeScenarioCnt++

						return ctx, nil
					})

					s.After(func(ctx context.Context, sc *Scenario, err error) (context.Context, error) {
						log += fmt.Sprintf("<< After scenario %q, error: %v\n", sc.Name, err)
						afterScenarioCnt++

						return ctx, nil
					})

					s.StepContext().Before(func(ctx context.Context, st *Step) (context.Context, error) {
						log += fmt.Sprintf("Before step %q\n", st.Text)
						beforeStepCnt++

						return ctx, nil
					})

					s.StepContext().After(func(ctx context.Context, st *Step, status StepResultStatus, err error) (context.Context, error) {
						log += fmt.Sprintf("After step %q, error: %v, status: %s\n", st.Text, err, status.String())
						afterStepCnt++

						return ctx, nil
					})

					s.Step("^step fails$", func() error {
						return errors.New("oops")
					})

					s.Step("^step skips scenario$", func() error {
						return ErrSkip
					})

					s.Step("^step passes$", func() {
						log += "<step action>\n"
					})

					s.Step("^multistep passes$", func() Steps {
						return Steps{"step passes", "step passes"}
					})

					s.Step("pending", func() error {
						return ErrPending
					})

					s.Step("^step is ambiguous$", func() {
						log += "<step action>\n"
					})
					s.Step("^step is ambiguous$", func() {
						log += "<step action>\n"
					})
					s.Step("^multistep has ambiguous$", func() Steps {
						return Steps{"step is ambiguous"}
					})
				},
				Options: &Options{
					Format:   "pretty",
					Strict:   !tc.noStrict,
					NoColors: true,
					FeatureContents: []Feature{
						{
							Name: tc.name,
							Contents: []byte(trimAllLines(`
								Feature: test
								Scenario: test
								` + tc.body)),
						},
					},
				},
			}

			suitePasses := suite.Run() == 0
			assert.Equal(t, tc.suitePasses, suitePasses)
			assert.Equal(t, 1, afterScenarioCnt)
			assert.Equal(t, 1, beforeScenarioCnt)
			assert.Equal(t, tc.afterStepCnt, afterStepCnt)
			assert.Equal(t, tc.beforeStepCnt, beforeStepCnt)
			assert.Equal(t, trimAllLines(tc.log), trimAllLines(log), log)
		})
	}
}
```

## File: `test_context.go`
```go
package godog

import (
	"context"
	"fmt"
	"reflect"
	"regexp"
	"runtime"

	messages "github.com/cucumber/messages/go/v21"

	"github.com/cucumber/godog/formatters"
	"github.com/cucumber/godog/internal/builder"
	"github.com/cucumber/godog/internal/flags"
	"github.com/cucumber/godog/internal/models"
)

// GherkinDocument represents gherkin document.
type GherkinDocument = messages.GherkinDocument

// Scenario represents the executed scenario
type Scenario = messages.Pickle

// Step represents the executed step
type Step = messages.PickleStep

// Steps allows to nest steps
// instead of returning an error in step func
// it is possible to return combined steps:
//
//	func multistep(name string) godog.Steps {
//	  return godog.Steps{
//	    fmt.Sprintf(`an user named "%s"`, name),
//	    fmt.Sprintf(`user "%s" is authenticated`, name),
//	  }
//	}
//
// These steps will be matched and executed in
// sequential order. The first one which fails
// will result in main step failure.
type Steps []string

// StepDefinition is a registered step definition
// contains a StepHandler and regexp which
// is used to match a step. Args which
// were matched by last executed step
//
// This structure is passed to the formatter
// when step is matched and is either failed
// or successful
type StepDefinition = formatters.StepDefinition

// DocString represents the DocString argument made to a step definition
type DocString = messages.PickleDocString

// Table represents the Table argument made to a step definition
type Table = messages.PickleTable

// TestSuiteContext allows various contexts
// to register event handlers.
//
// When running a test suite, the instance of TestSuiteContext
// is passed to all functions (contexts), which
// have it as a first and only argument.
//
// Note that all event hooks does not catch panic errors
// in order to have a trace information
type TestSuiteContext struct {
	beforeSuiteHandlers []func()
	afterSuiteHandlers  []func()

	suite *suite
}

// BeforeSuite registers a function or method
// to be run once before suite runner.
//
// Use it to prepare the test suite for a spin.
// Connect and prepare database for instance...
func (ctx *TestSuiteContext) BeforeSuite(fn func()) {
	ctx.beforeSuiteHandlers = append(ctx.beforeSuiteHandlers, fn)
}

// AfterSuite registers a function or method
// to be run once after suite runner
func (ctx *TestSuiteContext) AfterSuite(fn func()) {
	ctx.afterSuiteHandlers = append(ctx.afterSuiteHandlers, fn)
}

// ScenarioContext allows registering scenario hooks.
func (ctx *TestSuiteContext) ScenarioContext() *ScenarioContext {
	return &ScenarioContext{
		suite: ctx.suite,
	}
}

// ScenarioContext allows various contexts
// to register steps and event handlers.
//
// When running a scenario, the instance of ScenarioContext
// is passed to all functions (contexts), which
// have it as a first and only argument.
//
// Note that all event hooks does not catch panic errors
// in order to have a trace information. Only step
// executions are catching panic error since it may
// be a context specific error.
type ScenarioContext struct {
	suite *suite
}

// StepContext allows registering step hooks.
type StepContext struct {
	suite *suite
}

// Before registers a function or method
// to be run before every scenario.
//
// It is a good practice to restore the default state
// before every scenario, so it would be isolated from
// any kind of state.
func (ctx ScenarioContext) Before(h BeforeScenarioHook) {
	ctx.suite.beforeScenarioHandlers = append(ctx.suite.beforeScenarioHandlers, h)
}

// BeforeScenarioHook defines a hook before scenario.
type BeforeScenarioHook func(ctx context.Context, sc *Scenario) (context.Context, error)

// After registers a function or method
// to be run after every scenario.
func (ctx ScenarioContext) After(h AfterScenarioHook) {
	ctx.suite.afterScenarioHandlers = append(ctx.suite.afterScenarioHandlers, h)
}

// AfterScenarioHook defines a hook after scenario.
type AfterScenarioHook func(ctx context.Context, sc *Scenario, err error) (context.Context, error)

// StepContext exposes StepContext of a scenario.
func (ctx ScenarioContext) StepContext() StepContext {
	return StepContext(ctx)
}

// Before registers a function or method
// to be run before every step.
func (ctx StepContext) Before(h BeforeStepHook) {
	ctx.suite.beforeStepHandlers = append(ctx.suite.beforeStepHandlers, h)
}

// BeforeStepHook defines a hook before step.
type BeforeStepHook func(ctx context.Context, st *Step) (context.Context, error)

// After registers a function or method
// to be run after every step.
//
// It may be convenient to return a different kind of error
// in order to print more state details which may help
// in case of step failure
//
// In some cases, for example when running a headless
// browser, to take a screenshot after failure.
func (ctx StepContext) After(h AfterStepHook) {
	ctx.suite.afterStepHandlers = append(ctx.suite.afterStepHandlers, h)
}

// AfterStepHook defines a hook after step.
type AfterStepHook func(ctx context.Context, st *Step, status StepResultStatus, err error) (context.Context, error)

// BeforeScenario registers a function or method
// to be run before every scenario.
//
// It is a good practice to restore the default state
// before every scenario, so it would be isolated from
// any kind of state.
//
// Deprecated: use Before.
func (ctx ScenarioContext) BeforeScenario(fn func(sc *Scenario)) {
	ctx.Before(func(ctx context.Context, sc *Scenario) (context.Context, error) {
		fn(sc)

		return ctx, nil
	})
}

// AfterScenario registers a function or method
// to be run after every scenario.
//
// Deprecated: use After.
func (ctx ScenarioContext) AfterScenario(fn func(sc *Scenario, err error)) {
	ctx.After(func(ctx context.Context, sc *Scenario, err error) (context.Context, error) {
		fn(sc, err)

		return ctx, nil
	})
}

// BeforeStep registers a function or method
// to be run before every step.
//
// Deprecated: use ScenarioContext.StepContext() and StepContext.Before.
func (ctx ScenarioContext) BeforeStep(fn func(st *Step)) {
	ctx.StepContext().Before(func(ctx context.Context, st *Step) (context.Context, error) {
		fn(st)

		return ctx, nil
	})
}

// AfterStep registers a function or method
// to be run after every step.
//
// It may be convenient to return a different kind of error
// in order to print more state details which may help
// in case of step failure
//
// In some cases, for example when running a headless
// browser, to take a screenshot after failure.
//
// Deprecated: use ScenarioContext.StepContext() and StepContext.After.
func (ctx ScenarioContext) AfterStep(fn func(st *Step, err error)) {
	ctx.StepContext().After(func(ctx context.Context, st *Step, status StepResultStatus, err error) (context.Context, error) {
		fn(st, err)

		return ctx, nil
	})
}

// Step allows to register a *StepDefinition in the
// Godog feature suite, the definition will be applied
// to all steps matching the given Regexp expr.
//
// It will panic if expr is not a valid regular
// expression or stepFunc is not a valid step
// handler.
//
// The expression can be of type: *regexp.Regexp, string or []byte
//
// The stepFunc may accept one or several arguments of type:
// - int, int8, int16, int32, int64
// - uint, uint8, uint16, uint32, uint64
// - float32, float64
// - string
// - []byte
// - *godog.DocString
// - *godog.Table
//
// The stepFunc need to return either an error or []string for multistep
//
// Note that if there are two definitions which may match
// the same step, then only the first matched handler
// will be applied.
//
// If none of the *StepDefinition is matched, then
// ErrUndefined error will be returned when
// running steps.
func (ctx ScenarioContext) Step(expr, stepFunc interface{}) {
	ctx.stepWithKeyword(expr, stepFunc, formatters.None)
}

// Given functions identically to Step, but the *StepDefinition
// will only be matched if the step starts with "Given". "And"
// and "But" keywords copy the keyword of the last step for the
// purpose of matching.
func (ctx ScenarioContext) Given(expr, stepFunc interface{}) {
	ctx.stepWithKeyword(expr, stepFunc, formatters.Given)
}

// When functions identically to Step, but the *StepDefinition
// will only be matched if the step starts with "When". "And"
// and "But" keywords copy the keyword of the last step for the
// purpose of matching.
func (ctx ScenarioContext) When(expr, stepFunc interface{}) {
	ctx.stepWithKeyword(expr, stepFunc, formatters.When)
}

// Then functions identically to Step, but the *StepDefinition
// will only be matched if the step starts with "Then". "And"
// and "But" keywords copy the keyword of the last step for the
// purpose of matching.
func (ctx ScenarioContext) Then(expr, stepFunc interface{}) {
	ctx.stepWithKeyword(expr, stepFunc, formatters.Then)
}

func (ctx ScenarioContext) stepWithKeyword(expr interface{}, stepFunc interface{}, keyword formatters.Keyword) {
	var regex *regexp.Regexp

	// Validate the first input param is regex compatible
	switch t := expr.(type) {
	case *regexp.Regexp:
		regex = t
	case string:
		regex = regexp.MustCompile(t)
	case []byte:
		regex = regexp.MustCompile(string(t))
	default:
		panic(fmt.Sprintf("expecting expr to be a *regexp.Regexp or a string or []byte, got type: %T", expr))
	}

	// Validate that the handler is a function.
	handlerType := reflect.TypeOf(stepFunc)
	if handlerType.Kind() != reflect.Func {
		panic(fmt.Sprintf("expected handler to be func, but got: %T", stepFunc))
	}

	// FIXME = Validate the handler function param types here so
	// that any errors are discovered early.
	// StepDefinition.Run defines the supported types but fails at run time not registration time

	// Validate the function's return types.
	helpPrefix := "expected handler to return one of error or context.Context or godog.Steps or (context.Context, error)"
	isNested := false

	numOut := handlerType.NumOut()
	switch numOut {
	case 0:
		// No return values.
	case 1:
		// One return value: should be error, Steps, or context.Context.
		outType := handlerType.Out(0)
		if outType == reflect.TypeOf(Steps{}) {
			isNested = true
		} else {
			if outType != errorInterface && outType != contextInterface {
				panic(fmt.Sprintf("%s, but got: %v", helpPrefix, outType))
			}
		}
	case 2:
		// Two return values: should be (context.Context, error).
		if handlerType.Out(0) != contextInterface || handlerType.Out(1) != errorInterface {
			panic(fmt.Sprintf("%s, but got: %v, %v", helpPrefix, handlerType.Out(0), handlerType.Out(1)))
		}
	default:
		// More than two return values.
		panic(fmt.Sprintf("expected handler to return either zero, one or two values, but it has: %d", numOut))
	}

	// Register the handler
	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: stepFunc,
			Expr:    regex,
			Keyword: keyword,
		},
		HandlerValue: reflect.ValueOf(stepFunc),
		Nested:       isNested,
	}

	// Get the file and line number of the call that created this step with a
	// call to one of the Step, Given, When, or Then wrappers.
	_, def.File, def.Line, _ = runtime.Caller(2)

	// stash the step
	ctx.suite.steps = append(ctx.suite.steps, def)
}

// Build creates a test package like go test command at given target path.
// If there are no go files in tested directory, then
// it simply builds a godog executable to scan features.
//
// If there are go test files, it first builds a test
// package with standard go test command.
//
// Finally, it generates godog suite executable which
// registers exported godog contexts from the test files
// of tested package.
//
// Returns the path to generated executable
func Build(bin string) error {
	return builder.Build(bin)
}

type Feature = flags.Feature
```

## File: `test_context_test.go`
```go
package godog

import (
	"context"
	"regexp"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestScenarioContext_Step(t *testing.T) {
	ctx := ScenarioContext{suite: &suite{}}
	re := `(?:it is a test)?.{10}x*`

	type tc struct {
		f func()
		n string
		p interface{}
	}

	for _, c := range []tc{
		{n: "ScenarioContext should accept steps defined with regexp.Regexp",
			f: func() { ctx.Step(regexp.MustCompile(re), okVoidResult) }},
		{n: "ScenarioContext should accept steps defined with bytes slice",
			f: func() { ctx.Step([]byte(re), okVoidResult) }},

		{n: "ScenarioContext should accept steps handler with no return",
			f: func() { ctx.Step(".*", okVoidResult) }},
		{n: "ScenarioContext should accept steps handler with error return",
			f: func() { ctx.Step(".*", okErrorResult) }},
		{n: "ScenarioContext should accept steps handler with godog.Steps return",
			f: func() { ctx.Step(".*", okStepsResult) }},
		{n: "ScenarioContext should accept steps handler with (Context, error) return",
			f: func() { ctx.Step(".*", okContextErrorResult) }},
	} {
		t.Run(c.n, func(t *testing.T) {
			assert.NotPanics(t, c.f)
		})
	}

	for _, c := range []tc{
		{n: "ScenarioContext should panic if step expression is neither a string, regex or byte slice",
			p: "expecting expr to be a *regexp.Regexp or a string or []byte, got type: int",
			f: func() { ctx.Step(1251, okVoidResult) }},
		{n: "ScenarioContext should panic if step handler is not a function",
			p: "expected handler to be func, but got: int",
			f: func() { ctx.Step(".*", 124) }},
		{n: "ScenarioContext should panic if step handler has more than 2 return values",
			p: "expected handler to return either zero, one or two values, but it has: 3",
			f: func() { ctx.Step(".*", nokLimitCase3) }},
		{n: "ScenarioContext should panic if step handler has more than 2 return values (5)",
			p: "expected handler to return either zero, one or two values, but it has: 5",
			f: func() { ctx.Step(".*", nokLimitCase5) }},

		{n: "ScenarioContext should panic if step expression is neither a string, regex or byte slice",
			p: "expecting expr to be a *regexp.Regexp or a string or []byte, got type: int",
			f: func() { ctx.Step(1251, okVoidResult) }},

		{n: "ScenarioContext should panic if step return type is []string",
			p: "expected handler to return one of error or context.Context or godog.Steps or (context.Context, error), but got: []string",
			f: func() { ctx.Step(".*", nokSliceStringResult) }},
		{n: "ScenarioContext should panic if step handler return type is not an error or string slice or void (interface)",
			p: "expected handler to return one of error or context.Context or godog.Steps or (context.Context, error), but got: interface {}",
			f: func() { ctx.Step(".*", nokInvalidReturnInterfaceType) }},
		{n: "ScenarioContext should panic if step handler return type is not an error or string slice or void (slice)",
			p: "expected handler to return one of error or context.Context or godog.Steps or (context.Context, error), but got: []int",
			f: func() { ctx.Step(".*", nokInvalidReturnSliceType) }},
		{n: "ScenarioContext should panic if step handler return type is not an error or string slice or void (other)",
			p: "expected handler to return one of error or context.Context or godog.Steps or (context.Context, error), but got: chan int",
			f: func() { ctx.Step(".*", nokInvalidReturnOtherType) }},
	} {
		t.Run(c.n, func(t *testing.T) {
			assert.PanicsWithValue(t, c.p, c.f)
		})
	}
}

func okVoidResult()                                  {}
func okErrorResult() error                           { return nil }
func okStepsResult() Steps                           { return nil }
func okContextErrorResult() (context.Context, error) { return nil, nil }
func nokSliceStringResult() []string                 { return nil }
func nokLimitCase3() (string, int, error)            { return "", 0, nil }
func nokLimitCase5() (int, int, int, int, error)     { return 0, 0, 0, 0, nil }
func nokInvalidReturnInterfaceType() interface{}     { return 0 }
func nokInvalidReturnSliceType() []int               { return nil }
func nokInvalidReturnOtherType() chan int            { return nil }
```

## File: `testingt.go`
```go
package godog

import (
	"context"
	"fmt"
	"strings"
	"testing"
)

// T returns a TestingT compatible interface from the current test context. It will return nil if
// called outside the context of a test. This can be used with (for example) testify's assert and
// require packages.
func T(ctx context.Context) TestingT {
	return getTestingT(ctx)
}

// TestingT is a subset of the public methods implemented by go's testing.T. It allows assertion
// libraries to be used with godog, provided they depend only on this subset of methods.
type TestingT interface {
	// Name returns the name of the current pickle under test
	Name() string
	// Log will log to the current testing.T log if set, otherwise it will log to stdout
	Log(args ...interface{})
	// Logf will log a formatted string to the current testing.T log if set, otherwise it will log
	// to stdout
	Logf(format string, args ...interface{})
	// Error fails the current test and logs the provided arguments. Equivalent to calling Log then
	// Fail.
	Error(args ...interface{})
	// Errorf fails the current test and logs the formatted message. Equivalent to calling Logf then
	// Fail.
	Errorf(format string, args ...interface{})
	// Fail marks the current test as failed, but does not halt execution of the step.
	Fail()
	// FailNow marks the current test as failed and halts execution of the step.
	FailNow()
	// Fatal logs the provided arguments, marks the test as failed and halts execution of the step.
	Fatal(args ...interface{})
	// Fatal logs the formatted message, marks the test as failed and halts execution of the step.
	Fatalf(format string, args ...interface{})
	// Skip logs the provided arguments and marks the test as skipped but does not halt execution
	// of the step.
	Skip(args ...interface{})
	// Skipf logs the formatted message and marks the test as skipped but does not halt execution
	// of the step.
	Skipf(format string, args ...interface{})
	// SkipNow marks the current test as skipped and halts execution of the step.
	SkipNow()
	// Skipped returns true if the test has been marked as skipped.
	Skipped() bool
}

// Logf will log test output. If called in the context of a test and testing.T has been registered,
// this will log using the step's testing.T, else it will simply log to stdout.
func Logf(ctx context.Context, format string, args ...interface{}) {
	if t := getTestingT(ctx); t != nil {
		t.Logf(format, args...)
		return
	}
	fmt.Printf(format+"\n", args...)
}

// Log will log test output. If called in the context of a test and testing.T has been registered,
// this will log using the step's testing.T, else it will simply log to stdout.
func Log(ctx context.Context, args ...interface{}) {
	if t := getTestingT(ctx); t != nil {
		t.Log(args...)
		return
	}
	fmt.Println(args...)
}

// LoggedMessages returns an array of any logged messages that have been recorded during the test
// through calls to godog.Log / godog.Logf or via operations against godog.T(ctx)
func LoggedMessages(ctx context.Context) []string {
	if t := getTestingT(ctx); t != nil {
		return t.logMessages
	}
	return nil
}

// errStopNow should be returned inside a panic within the test to immediately halt execution of that
// test
var errStopNow = fmt.Errorf("FailNow or SkipNow called")

type testingT struct {
	name         string
	t            *testing.T
	failed       bool
	skipped      bool
	failMessages []string
	logMessages  []string
}

// check interface against our testingT and the upstream testing.B/F/T:
var (
	_ TestingT = &testingT{}
	_ TestingT = (*testing.T)(nil)
)

func (dt *testingT) Name() string {
	if dt.t != nil {
		return dt.t.Name()
	}
	return dt.name
}

func (dt *testingT) Log(args ...interface{}) {
	dt.logMessages = append(dt.logMessages, fmt.Sprint(args...))
	if dt.t != nil {
		dt.t.Log(args...)
		return
	}
	fmt.Println(args...)
}

func (dt *testingT) Logf(format string, args ...interface{}) {
	dt.logMessages = append(dt.logMessages, fmt.Sprintf(format, args...))
	if dt.t != nil {
		dt.t.Logf(format, args...)
		return
	}
	fmt.Printf(format+"\n", args...)
}

func (dt *testingT) Error(args ...interface{}) {
	dt.Log(args...)
	dt.failMessages = append(dt.failMessages, fmt.Sprintln(args...))
	dt.Fail()
}

func (dt *testingT) Errorf(format string, args ...interface{}) {
	dt.Logf(format, args...)
	dt.failMessages = append(dt.failMessages, fmt.Sprintf(format, args...))
	dt.Fail()
}

func (dt *testingT) Fail() {
	dt.failed = true
}

func (dt *testingT) FailNow() {
	dt.Fail()
	panic(errStopNow)
}

func (dt *testingT) Fatal(args ...interface{}) {
	dt.Log(args...)
	dt.FailNow()
}

func (dt *testingT) Fatalf(format string, args ...interface{}) {
	dt.Logf(format, args...)
	dt.FailNow()
}

func (dt *testingT) Skip(args ...interface{}) {
	dt.Log(args...)
	dt.skipped = true
}

func (dt *testingT) Skipf(format string, args ...interface{}) {
	dt.Logf(format, args...)
	dt.skipped = true
}

func (dt *testingT) SkipNow() {
	dt.skipped = true
	panic(errStopNow)
}

func (dt *testingT) Skipped() bool {
	return dt.skipped
}

// isFailed will return an error representing the calls to Fail made during this test
func (dt *testingT) isFailed() error {
	if dt.skipped {
		return ErrSkip
	}
	if !dt.failed {
		return nil
	}
	switch len(dt.failMessages) {
	case 0:
		return fmt.Errorf("fail called on TestingT")
	case 1:
		return fmt.Errorf(dt.failMessages[0])
	default:
		return fmt.Errorf("checks failed:\n* %s", strings.Join(dt.failMessages, "\n* "))
	}
}

type testingTCtxVal struct{}

func setContextTestingT(ctx context.Context, dt *testingT) context.Context {
	return context.WithValue(ctx, testingTCtxVal{}, dt)
}

func getTestingT(ctx context.Context) *testingT {
	dt, ok := ctx.Value(testingTCtxVal{}).(*testingT)
	if !ok {
		return nil
	}
	return dt
}
```

## File: `utils_test.go`
```go
package godog

import (
	"testing"
	"time"

	"github.com/cucumber/godog/internal/utils"
)

// this zeroes the time throughout whole test suite
// and makes it easier to assert output
// activated only when godog tests are being run
func init() {
	utils.TimeNowFunc = func() time.Time {
		return time.Time{}
	}
}

func TestTimeNowFunc(t *testing.T) {
	now := utils.TimeNowFunc()
	if !now.IsZero() {
		t.Fatalf("expected zeroed time, but got: %s", now.Format(time.RFC3339))
	}
}
```

## File: `_examples/doc.go`
```go
package examples
```

## File: `_examples/go.mod`
```
module github.com/cucumber/godog/_examples

go 1.21

replace github.com/cucumber/godog => ../

require (
	github.com/DATA-DOG/go-txdb v0.2.1
	github.com/cucumber/godog v0.15.1
	github.com/go-sql-driver/mysql v1.7.1
	github.com/spf13/pflag v1.0.10
	github.com/stretchr/testify v1.8.2
)

require (
	github.com/cpuguy83/go-md2man/v2 v2.0.2 // indirect
	github.com/creack/pty v1.1.9 // indirect
	github.com/cucumber/gherkin/go/v26 v26.2.0 // indirect
	github.com/cucumber/messages/go/v21 v21.0.1 // indirect
	github.com/cucumber/messages/go/v22 v22.0.0 // indirect
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/gofrs/uuid v4.3.1+incompatible // indirect
	github.com/hashicorp/go-immutable-radix v1.3.1 // indirect
	github.com/hashicorp/go-memdb v1.3.4 // indirect
	github.com/hashicorp/go-uuid v1.0.2 // indirect
	github.com/hashicorp/golang-lru v0.5.4 // indirect
	github.com/inconshreveable/mousetrap v1.1.0 // indirect
	github.com/kr/pretty v0.3.0 // indirect
	github.com/kr/pty v1.1.1 // indirect
	github.com/kr/text v0.2.0 // indirect
	github.com/lib/pq v1.10.3 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	github.com/rogpeppe/go-internal v1.6.1 // indirect
	github.com/russross/blackfriday/v2 v2.1.0 // indirect
	github.com/spf13/cobra v1.7.0 // indirect
	github.com/stretchr/objx v0.5.0 // indirect
	gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c // indirect
	gopkg.in/errgo.v2 v2.1.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
```

## File: `_examples/go.sum`
```
github.com/DATA-DOG/go-txdb v0.1.6 h1:D1Ob/L79mCW6UCFL6vwM/9TWs/rshZujxTsvy7+gicw=
github.com/DATA-DOG/go-txdb v0.1.6/go.mod h1:DhAhxMXZpUJVGnT+p9IbzJoRKvlArO2pkHjnGX7o0n0=
github.com/DATA-DOG/go-txdb v0.2.1 h1:ic/cKLheUcjOHvqduJ349umI9KqQWny4idfnDyPEJWk=
github.com/DATA-DOG/go-txdb v0.2.1/go.mod h1:Flb/TrTNAFotdSRIwUnM7BoJgT9AEX1Ysf863nYr5yk=
github.com/cpuguy83/go-md2man/v2 v2.0.2/go.mod h1:tgQtvFlXSQOSOSIRvRPT7W67SCa46tRHOmNcaadrF8o=
github.com/creack/pty v1.1.9/go.mod h1:oKZEueFk5CKHvIhNR5MUki03XCEU+Q6VDXinZuGJ33E=
github.com/cucumber/gherkin/go/v26 v26.2.0 h1:EgIjePLWiPeslwIWmNQ3XHcypPsWAHoMCz/YEBKP4GI=
github.com/cucumber/gherkin/go/v26 v26.2.0/go.mod h1:t2GAPnB8maCT4lkHL99BDCVNzCh1d7dBhCLt150Nr/0=
github.com/cucumber/messages/go/v21 v21.0.1 h1:wzA0LxwjlWQYZd32VTlAVDTkW6inOFmSM+RuOwHZiMI=
github.com/cucumber/messages/go/v21 v21.0.1/go.mod h1:zheH/2HS9JLVFukdrsPWoPdmUtmYQAQPLk7w5vWsk5s=
github.com/cucumber/messages/go/v22 v22.0.0/go.mod h1:aZipXTKc0JnjCsXrJnuZpWhtay93k7Rn3Dee7iyPJjs=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/go-sql-driver/mysql v1.7.1 h1:lUIinVbN1DY0xBg0eMOzmmtGoHwWBbvnWubQUrtU8EI=
github.com/go-sql-driver/mysql v1.7.1/go.mod h1:OXbVy3sEdcQ2Doequ6Z5BW6fXNQTmx+9S1MCJN5yJMI=
github.com/gofrs/uuid v4.2.0+incompatible/go.mod h1:b2aQJv3Z4Fp6yNu3cdSllBxTCLRxnplIgP/c0N/04lM=
github.com/gofrs/uuid v4.3.1+incompatible h1:0/KbAdpx3UXAx1kEOWHJeOkpbgRFGHVgv+CFIY7dBJI=
github.com/gofrs/uuid v4.3.1+incompatible/go.mod h1:b2aQJv3Z4Fp6yNu3cdSllBxTCLRxnplIgP/c0N/04lM=
github.com/hashicorp/go-immutable-radix v1.3.0/go.mod h1:0y9vanUI8NX6FsYoO3zeMjhV/C5i9g4Q3DwcSNZ4P60=
github.com/hashicorp/go-immutable-radix v1.3.1 h1:DKHmCUm2hRBK510BaiZlwvpD40f8bJFeZnpfm2KLowc=
github.com/hashicorp/go-immutable-radix v1.3.1/go.mod h1:0y9vanUI8NX6FsYoO3zeMjhV/C5i9g4Q3DwcSNZ4P60=
github.com/hashicorp/go-memdb v1.3.4 h1:XSL3NR682X/cVk2IeV0d70N4DZ9ljI885xAEU8IoK3c=
github.com/hashicorp/go-memdb v1.3.4/go.mod h1:uBTr1oQbtuMgd1SSGoR8YV27eT3sBHbYiNm53bMpgSg=
github.com/hashicorp/go-uuid v1.0.0/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/go-uuid v1.0.2 h1:cfejS+Tpcp13yd5nYHWDI6qVCny6wyX2Mt5SGur2IGE=
github.com/hashicorp/go-uuid v1.0.2/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/golang-lru v0.5.0/go.mod h1:/m3WP610KZHVQ1SGc6re/UDhFvYD7pJ4Ao+sR/qLZy8=
github.com/hashicorp/golang-lru v0.5.4 h1:YDjusn29QI/Das2iO9M0BHnIbxPeyuCHsjMW+lJfyTc=
github.com/hashicorp/golang-lru v0.5.4/go.mod h1:iADmTwqILo4mZ8BN3D2Q6+9jd8WM5uGBxy+E8yxSoD4=
github.com/inconshreveable/mousetrap v1.1.0/go.mod h1:vpF70FUmC8bwa3OWnCshd2FqLfsEA9PFc4w1p2J65bw=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pretty v0.3.0 h1:WgNl7dwNpEZ6jJ9k1snq4pZsg7DOEN8hP9Xw0Tsjwk0=
github.com/kr/pretty v0.3.0/go.mod h1:640gp4NfQd8pI5XOwp5fnNeVWj67G7CFk/SaSQn7NBk=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/lib/pq v1.10.3 h1:v9QZf2Sn6AmjXtQeFpdoq/eaNtYP6IN+7lcrygsIAtg=
github.com/lib/pq v1.10.3/go.mod h1:AlVN5x4E4T544tWzH6hKfbfQvm3HdbOxrmggDNAPY9o=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rogpeppe/go-internal v1.6.1 h1:/FiVV8dS/e+YqF2JvO3yXRFbBLTIuSDkuC7aBOAvL+k=
github.com/rogpeppe/go-internal v1.6.1/go.mod h1:xXDCJY+GAPziupqXw64V24skbSoqbTEfhy4qGm1nDQc=
github.com/russross/blackfriday/v2 v2.1.0/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/spf13/cobra v1.7.0/go.mod h1:uLxZILRyS/50WlhOIKD7W6V5bgeIt+4sICxh6uRMrb0=
github.com/spf13/pflag v1.0.5 h1:iy+VFUOCP1a+8yFto/drg2CJ5u0yRoB7fZw3DKv/JXA=
github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/pflag v1.0.6 h1:jFzHGLGAlb3ruxLB8MhbI6A8+AQX/2eW4qeyNZXNp2o=
github.com/spf13/pflag v1.0.6/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/pflag v1.0.7 h1:vN6T9TfwStFPFM5XzjsvmzZkLuaLX+HS+0SeFLRgU6M=
github.com/spf13/pflag v1.0.7/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/pflag v1.0.9 h1:9exaQaMOCwffKiiiYk6/BndUBv+iRViNW+4lEMi0PvY=
github.com/spf13/pflag v1.0.9/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/pflag v1.0.10 h1:4EBh2KAYBwaONj6b2Ye1GiHfwjqyROoF4RwYO+vPwFk=
github.com/spf13/pflag v1.0.10/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.4.0/go.mod h1:YvHI0jy2hoMjB+UWwv71VJQ9isScKT/TqJzVSSt89Yw=
github.com/stretchr/objx v0.5.0/go.mod h1:Yh+to48EsGEfYuaHDzXPcE3xhTkx73EhmCGUpEOglKo=
github.com/stretchr/testify v1.7.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.8.0/go.mod h1:yNjHg4UonilssWZ8iaSj1OCr/vHnekPRkoO+kdMU+MU=
github.com/stretchr/testify v1.8.1/go.mod h1:w2LPCIKwWwSfY2zedu0+kehJoqGctiVI29o6fzry7u4=
github.com/stretchr/testify v1.8.2 h1:+h33VjcLVPDHtOdpUCuF+7gSuG3yGIftsP1YvFihtJ8=
github.com/stretchr/testify v1.8.2/go.mod h1:w2LPCIKwWwSfY2zedu0+kehJoqGctiVI29o6fzry7u4=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/errgo.v2 v2.1.0/go.mod h1:hNsd1EY+bozCKY1Ytp96fpM3vjJbqLJn88ws8XvfDNI=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `_examples/api/README.md`
```markdown
# An example of API feature

The following example demonstrates steps how we describe and test our API using **godog**.

### Step 1

Describe our feature. Imagine we need a REST API with `json` format. Lets from the point, that
we need to have a `/version` endpoint, which responds with a version number. We also need to manage
error responses.

``` gherkin
# file: version.feature
Feature: get version
  In order to know godog version
  As an API user
  I need to be able to request version

  Scenario: does not allow POST method
    When I send "POST" request to "/version"
    Then the response code should be 405
    And the response should match json:
      """
      {
        "error": "Method not allowed"
      }
      """

  Scenario: should get version number
    When I send "GET" request to "/version"
    Then the response code should be 200
    And the response should match json:
      """
      {
        "version": "v0.0.0-dev"
      }
      """
```

Save it as `features/version.feature`.
Now we have described a success case and an error when the request method is not allowed.

### Step 2

Execute `godog run`. You should see the following result, which says that all of our
steps are yet undefined and provide us with the snippets to implement them.

![Screenshot](https://raw.github.com/cucumber/godog/master/_examples/api/screenshots/undefined.png)

### Step 3

Lets copy the snippets to `api_test.go` and modify it for our use case. Since we know that we will
need to store state within steps (a response), we should introduce a structure with some variables.

``` go
// file: api_test.go
package main

import (
	"github.com/cucumber/godog"
)

type apiFeature struct {
}

func (a *apiFeature) iSendrequestTo(method, endpoint string) error {
	return godog.ErrPending
}

func (a *apiFeature) theResponseCodeShouldBe(code int) error {
	return godog.ErrPending
}

func (a *apiFeature) theResponseShouldMatchJSON(body *godog.DocString) error {
	return godog.ErrPending
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

func InitializeScenario(s *godog.ScenarioContext) {
	api := &apiFeature{}
	s.Step(`^I send "([^"]*)" request to "([^"]*)"$`, api.iSendrequestTo)
	s.Step(`^the response code should be (\d+)$`, api.theResponseCodeShouldBe)
	s.Step(`^the response should match json:$`, api.theResponseShouldMatchJSON)
}
```

### Step 4

Now we can implement steps, since we know what behavior we expect:

``` go
// file: api_test.go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
	"reflect"
	"testing"

	"github.com/cucumber/godog"
)

type apiFeature struct {
	resp *httptest.ResponseRecorder
}

func (a *apiFeature) resetResponse(*godog.Scenario) {
	a.resp = httptest.NewRecorder()
}

func (a *apiFeature) iSendrequestTo(method, endpoint string) (err error) {
	req, err := http.NewRequest(method, endpoint, nil)
	if err != nil {
		return
	}

	// handle panic
	defer func() {
		switch t := recover().(type) {
		case string:
			err = fmt.Errorf(t)
		case error:
			err = t
		}
	}()

	switch endpoint {
	case "/version":
		getVersion(a.resp, req)
	default:
		err = fmt.Errorf("unknown endpoint: %s", endpoint)
	}
	return
}

func (a *apiFeature) theResponseCodeShouldBe(code int) error {
	if code != a.resp.Code {
		return fmt.Errorf("expected response code to be: %d, but actual is: %d", code, a.resp.Code)
	}
	return nil
}

func (a *apiFeature) theResponseShouldMatchJSON(body *godog.DocString) (err error) {
	var expected, actual interface{}

	// re-encode expected response
	if err = json.Unmarshal([]byte(body.Content), &expected); err != nil {
		return
	}

	// re-encode actual response too
	if err = json.Unmarshal(a.resp.Body.Bytes(), &actual); err != nil {
		return
	}

	// the matching may be adapted per different requirements.
	if !reflect.DeepEqual(expected, actual) {
		return fmt.Errorf("expected JSON does not match actual, %v vs. %v", expected, actual)
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

func InitializeScenario(ctx *godog.ScenarioContext) {
	api := &apiFeature{}

	ctx.Before(func(ctx context.Context, sc *godog.Scenario) (context.Context, error) {
		api.resetResponse(sc)
		return ctx, nil
	})
	ctx.Step(`^I send "(GET|POST|PUT|DELETE)" request to "([^"]*)"$`, api.iSendrequestTo)
	ctx.Step(`^the response code should be (\d+)$`, api.theResponseCodeShouldBe)
	ctx.Step(`^the response should match json:$`, api.theResponseShouldMatchJSON)
}
```

**NOTE:** the `getVersion` handler is called on `/version` endpoint.
Executing `godog run` or `go test -v` will provide `undefined: getVersion` error, so we actually need to implement it now.
If we made some mistakes in step implementations, we will know about it when we run the tests.

Though, we could also improve our `JSON` comparison function to range through the interfaces and
match their types and values.

In case if some router is used, you may search the handler based on the endpoint. Current example
uses a standard http package.

### Step 5

Finally, lets implement the `API` server:

``` go
// file: api.go
// Example - demonstrates REST API server implementation tests.
package main

import (
	"encoding/json"
	"net/http"

	"github.com/cucumber/godog"
)

func getVersion(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		fail(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	data := struct {
		Version string `json:"version"`
	}{Version: godog.Version}

	ok(w, data)
}

// fail writes a json response with error msg and status header
func fail(w http.ResponseWriter, msg string, status int) {
	w.WriteHeader(status)

	data := struct {
		Error string `json:"error"`
	}{Error: msg}
	resp, _ := json.Marshal(data)

	w.Header().Set("Content-Type", "application/json")
	w.Write(resp)
}

// ok writes data to response with 200 status
func ok(w http.ResponseWriter, data interface{}) {
	resp, err := json.Marshal(data)
	if err != nil {
		fail(w, "Oops something evil has happened", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(resp)
}

func main() {
	http.HandleFunc("/version", getVersion)
	http.ListenAndServe(":8080", nil)
}
```

The implementation details are clearly production ready and the imported **godog** package is only
used to respond with the correct constant version number.

### Step 6

Run our tests to see whether everything is happening as we have expected: `go test -v`

![Screenshot](https://raw.github.com/cucumber/godog/master/_examples/api/screenshots/passed.png)

### Conclusions

Hope you have enjoyed it like I did.

Any developer (who is the target of our application) can read and remind himself about how API behaves.
```

## File: `_examples/api/api.go`
```go
// Example - demonstrates REST API server implementation tests.
package main

import (
	"encoding/json"
	"net/http"

	"github.com/cucumber/godog"
)

func getVersion(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		fail(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	data := struct {
		Version string `json:"version"`
	}{Version: godog.Version}

	ok(w, data)
}

// fail writes a json response with error msg and status header
func fail(w http.ResponseWriter, msg string, status int) {
	w.WriteHeader(status)

	data := struct {
		Error string `json:"error"`
	}{Error: msg}
	resp, _ := json.Marshal(data)

	w.Header().Set("Content-Type", "application/json")
	w.Write(resp)
}

// ok writes data to response with 200 status
func ok(w http.ResponseWriter, data interface{}) {
	resp, err := json.Marshal(data)
	if err != nil {
		fail(w, "Oops something evil has happened", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(resp)
}

func main() {
	http.HandleFunc("/version", getVersion)
	http.ListenAndServe(":8080", nil)
}
```

## File: `_examples/api/api_test.go`
```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
	"reflect"
	"testing"

	"github.com/cucumber/godog"
)

type apiFeature struct {
	resp *httptest.ResponseRecorder
}

func (a *apiFeature) resetResponse(*godog.Scenario) {
	a.resp = httptest.NewRecorder()
}

func (a *apiFeature) iSendrequestTo(method, endpoint string) (err error) {
	req, err := http.NewRequest(method, endpoint, nil)
	if err != nil {
		return
	}

	// handle panic
	defer func() {
		switch t := recover().(type) {
		case string:
			err = fmt.Errorf(t)
		case error:
			err = t
		}
	}()

	switch endpoint {
	case "/version":
		getVersion(a.resp, req)
	default:
		err = fmt.Errorf("unknown endpoint: %s", endpoint)
	}
	return
}

func (a *apiFeature) theResponseCodeShouldBe(code int) error {
	if code != a.resp.Code {
		return fmt.Errorf("expected response code to be: %d, but actual is: %d", code, a.resp.Code)
	}
	return nil
}

func (a *apiFeature) theResponseShouldMatchJSON(body *godog.DocString) (err error) {
	var expected, actual interface{}

	// re-encode expected response
	if err = json.Unmarshal([]byte(body.Content), &expected); err != nil {
		return
	}

	// re-encode actual response too
	if err = json.Unmarshal(a.resp.Body.Bytes(), &actual); err != nil {
		return
	}

	// the matching may be adapted per different requirements.
	if !reflect.DeepEqual(expected, actual) {
		return fmt.Errorf("expected JSON does not match actual, %v vs. %v", expected, actual)
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

func InitializeScenario(ctx *godog.ScenarioContext) {
	api := &apiFeature{}

	ctx.Before(func(ctx context.Context, sc *godog.Scenario) (context.Context, error) {
		api.resetResponse(sc)
		return ctx, nil
	})
	ctx.Step(`^I send "(GET|POST|PUT|DELETE)" request to "([^"]*)"$`, api.iSendrequestTo)
	ctx.Step(`^the response code should be (\d+)$`, api.theResponseCodeShouldBe)
	ctx.Step(`^the response should match json:$`, api.theResponseShouldMatchJSON)
}
```

## File: `_examples/api/features/version.feature`
```
# file: version.feature
Feature: get version
  In order to know godog version
  As an API user
  I need to be able to request version

  Scenario: does not allow POST method
    When I send "POST" request to "/version"
    Then the response code should be 405
    And the response should match json:
      """
      {
        "error": "Method not allowed"
      }
      """

  Scenario: should get version number
    When I send "GET" request to "/version"
    Then the response code should be 200
    And the response should match json:
      """
      {
        "version": "v0.0.0-dev"
      }
      """
```

## File: `_examples/assert-godogs/godogs.go`
```go
package main

// Godogs available to eat
var Godogs int

func main() { /* usual main func */ }
```

## File: `_examples/assert-godogs/godogs_test.go`
```go
package main

import (
	"context"
	"os"
	"testing"

	"github.com/cucumber/godog"
	"github.com/cucumber/godog/colors"
	"github.com/spf13/pflag"
	"github.com/stretchr/testify/assert"
)

var opts = godog.Options{Output: colors.Colored(os.Stdout)}

func init() {
	godog.BindCommandLineFlags("godog.", &opts)
}

func TestMain(m *testing.M) {
	pflag.Parse()
	opts.Paths = pflag.Args()

	status := godog.TestSuite{
		Name:                "godogs",
		ScenarioInitializer: InitializeScenario,
		Options:             &opts,
	}.Run()

	os.Exit(status)
}

func thereAreGodogs(available int) error {
	Godogs = available
	return nil
}

func iEat(ctx context.Context, num int) error {
	if !assert.GreaterOrEqual(godog.T(ctx), Godogs, num, "You cannot eat %d godogs, there are %d available", num, Godogs) {
		return nil
	}
	Godogs -= num
	return nil
}

func thereShouldBeRemaining(ctx context.Context, remaining int) error {
	assert.Equal(godog.T(ctx), Godogs, remaining, "Expected %d godogs to be remaining, but there is %d", remaining, Godogs)
	return nil
}

func thereShouldBeNoneRemaining(ctx context.Context) error {
	assert.Empty(godog.T(ctx), Godogs, "Expected none godogs to be remaining, but there is %d", Godogs)
	return nil
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Before(func(ctx context.Context, sc *godog.Scenario) (context.Context, error) {
		Godogs = 0 // clean the state before every scenario
		return ctx, nil
	})

	ctx.Step(`^there are (\d+) godogs$`, thereAreGodogs)
	ctx.Step(`^I eat (\d+)$`, iEat)
	ctx.Step(`^there should be (\d+) remaining$`, thereShouldBeRemaining)
	ctx.Step(`^there should be none remaining$`, thereShouldBeNoneRemaining)
}
```

## File: `_examples/assert-godogs/features/godogs.feature`
```
# file: $GOPATH/godogs/features/godogs.feature
Feature: eat godogs
  In order to be happy
  As a hungry gopher
  I need to be able to eat godogs

  Scenario: Eat 5 out of 12
    Given there are 12 godogs
    When I eat 5
    Then there should be 7 remaining

  Scenario: Eat 12 out of 12
    Given there are 12 godogs
    When I eat 12
    Then there should be none remaining
```

## File: `_examples/attachments/README.md`
```markdown
# An example of Making attachments to the reports

The JSON (and in future NDJSON) report formats allow the inclusion of data attachments.

These attachments could be console logs or file data or images for instance.

The example in this directory shows how the godog API is used to add attachments to the JSON report.


## Run the example

You must use the '-v' flag or you will not see the cucumber JSON output.

go test -v attachments_test.go


```

## File: `_examples/attachments/attachments_test.go`
```go
package attachments_test

// This "demo" doesn't actually get run as a test by the build.

// This "example" shows how to attach data to the cucumber reports
// Run the sample with : go test -v attachments_test.go
// Then review the "embeddings" within the JSON emitted on the console.

import (
	"context"
	"os"
	"testing"

	"github.com/cucumber/godog"
	"github.com/cucumber/godog/colors"
)

var opts = godog.Options{
	Output: colors.Colored(os.Stdout),
	Format: "cucumber", // cucumber json format
}

func TestFeatures(t *testing.T) {
	o := opts
	o.TestingT = t

	status := godog.TestSuite{
		Name:                "attachments",
		Options:             &o,
		ScenarioInitializer: InitializeScenario,
	}.Run()

	if status == 2 {
		t.SkipNow()
	}

	if status != 0 {
		t.Fatalf("zero status code expected, %d received", status)
	}
}

func InitializeScenario(ctx *godog.ScenarioContext) {

	ctx.Before(func(ctx context.Context, sc *godog.Scenario) (context.Context, error) {
		ctx = godog.Attach(ctx,
			godog.Attachment{Body: []byte("BeforeScenarioAttachment"), FileName: "Step Attachment 1", MediaType: "text/plain"},
		)
		return ctx, nil
	})
	ctx.After(func(ctx context.Context, sc *godog.Scenario, err error) (context.Context, error) {
		ctx = godog.Attach(ctx,
			godog.Attachment{Body: []byte("AfterScenarioAttachment"), FileName: "Step Attachment 2", MediaType: "text/plain"},
		)
		return ctx, nil
	})

	ctx.StepContext().Before(func(ctx context.Context, st *godog.Step) (context.Context, error) {
		ctx = godog.Attach(ctx,
			godog.Attachment{Body: []byte("BeforeStepAttachment"), FileName: "Step Attachment 3", MediaType: "text/plain"},
		)
		return ctx, nil
	})
	ctx.StepContext().After(func(ctx context.Context, st *godog.Step, status godog.StepResultStatus, err error) (context.Context, error) {
		ctx = godog.Attach(ctx,
			godog.Attachment{Body: []byte("AfterStepAttachment"), FileName: "Step Attachment 4", MediaType: "text/plain"},
		)
		return ctx, nil
	})

	ctx.Step(`^I have attached two documents in sequence$`, func(ctx context.Context) (context.Context, error) {
		// the attached bytes will be base64 encoded by the framework and placed in the embeddings section of the cuke report
		ctx = godog.Attach(ctx,
			godog.Attachment{Body: []byte("TheData1"), FileName: "Step Attachment 5", MediaType: "text/plain"},
		)
		ctx = godog.Attach(ctx,
			godog.Attachment{Body: []byte("{ \"a\" : 1 }"), FileName: "Step Attachment 6", MediaType: "application/json"},
		)

		return ctx, nil
	})
	ctx.Step(`^I have attached two documents at once$`, func(ctx context.Context) (context.Context, error) {
		ctx = godog.Attach(ctx,
			godog.Attachment{Body: []byte("TheData1"), FileName: "Step Attachment 7", MediaType: "text/plain"},
			godog.Attachment{Body: []byte("TheData2"), FileName: "Step Attachment 8", MediaType: "text/plain"},
		)

		return ctx, nil
	})
}
```

## File: `_examples/attachments/features/attachments.feature`
```
Feature: Attaching content to the cucumber report
  The cucumber JSON and NDJSON support the inclusion of attachments.
  These can be text or images or any data really. 

  Scenario: Attaching files to the report
    Given I have attached two documents in sequence 
    And I have attached two documents at once
```

## File: `_examples/custom-formatter/README.md`
```markdown

# Custom Formatter Example

This example custom formatter demonstrates some ways to build and use custom formatters with godog


## Emoji Progress

The first example is the Emoji formatter, built on top of the Progress formatter that is included with godog.

To run it:

```
$ godog -f emoji
```

Which would output step progress as emojis rather than text:

![](imgs/emoji-output-example.png)
```

## File: `_examples/custom-formatter/emoji.go`
```go
package main

import (
	"fmt"
	"io"
	"math"

	"github.com/cucumber/godog"
)

const (
	passedEmoji    = "✅"
	skippedEmoji   = "➖"
	failedEmoji    = "❌"
	undefinedEmoji = "❓"
	pendingEmoji   = "🚧"
)

func init() {
	godog.Format("emoji", "Progress formatter with emojis", emojiFormatterFunc)
}

func emojiFormatterFunc(suite string, out io.Writer) godog.Formatter {
	return newEmojiFmt(suite, out)
}

func newEmojiFmt(suite string, out io.Writer) *emojiFmt {
	return &emojiFmt{
		ProgressFmt: godog.NewProgressFmt(suite, out),
		out:         out,
	}
}

type emojiFmt struct {
	*godog.ProgressFmt

	out io.Writer
}

func (f *emojiFmt) TestRunStarted() {}

func (f *emojiFmt) Passed(scenario *godog.Scenario, step *godog.Step, match *godog.StepDefinition) {
	f.ProgressFmt.Base.Passed(scenario, step, match)

	f.ProgressFmt.Base.Lock.Lock()
	defer f.ProgressFmt.Base.Lock.Unlock()

	f.step(step.Id)
}

func (f *emojiFmt) Skipped(scenario *godog.Scenario, step *godog.Step, match *godog.StepDefinition) {
	f.ProgressFmt.Base.Skipped(scenario, step, match)

	f.ProgressFmt.Base.Lock.Lock()
	defer f.ProgressFmt.Base.Lock.Unlock()

	f.step(step.Id)
}

func (f *emojiFmt) Undefined(scenario *godog.Scenario, step *godog.Step, match *godog.StepDefinition) {
	f.ProgressFmt.Base.Undefined(scenario, step, match)

	f.ProgressFmt.Base.Lock.Lock()
	defer f.ProgressFmt.Base.Lock.Unlock()

	f.step(step.Id)
}

func (f *emojiFmt) Failed(scenario *godog.Scenario, step *godog.Step, match *godog.StepDefinition, err error) {
	f.ProgressFmt.Base.Failed(scenario, step, match, err)

	f.ProgressFmt.Base.Lock.Lock()
	defer f.ProgressFmt.Base.Lock.Unlock()

	f.step(step.Id)
}

func (f *emojiFmt) Pending(scenario *godog.Scenario, step *godog.Step, match *godog.StepDefinition) {
	f.ProgressFmt.Base.Pending(scenario, step, match)

	f.ProgressFmt.Base.Lock.Lock()
	defer f.ProgressFmt.Base.Lock.Unlock()

	f.step(step.Id)
}

func (f *emojiFmt) Summary() {
	f.printSummaryLegend()
	f.ProgressFmt.Summary()
}

func (f *emojiFmt) printSummaryLegend() {
	fmt.Fprint(f.out, "\n\nOutput Legend:\n")
	fmt.Fprint(f.out, fmt.Sprintf("\t%s Passed\n", passedEmoji))
	fmt.Fprint(f.out, fmt.Sprintf("\t%s Failed\n", failedEmoji))
	fmt.Fprint(f.out, fmt.Sprintf("\t%s Skipped\n", skippedEmoji))
	fmt.Fprint(f.out, fmt.Sprintf("\t%s Undefined\n", undefinedEmoji))
	fmt.Fprint(f.out, fmt.Sprintf("\t%s Pending\n", pendingEmoji))
}

func (f *emojiFmt) step(pickleStepID string) {
	pickleStepResult := f.Storage.MustGetPickleStepResult(pickleStepID)

	switch pickleStepResult.Status {
	case godog.StepPassed:
		fmt.Fprint(f.out, fmt.Sprintf(" %s", passedEmoji))
	case godog.StepSkipped:
		fmt.Fprint(f.out, fmt.Sprintf(" %s", skippedEmoji))
	case godog.StepFailed:
		fmt.Fprint(f.out, fmt.Sprintf(" %s", failedEmoji))
	case godog.StepUndefined:
		fmt.Fprint(f.out, fmt.Sprintf(" %s", undefinedEmoji))
	case godog.StepPending:
		fmt.Fprint(f.out, fmt.Sprintf(" %s", pendingEmoji))
	}

	*f.Steps++

	if math.Mod(float64(*f.Steps), float64(f.StepsPerRow)) == 0 {
		fmt.Fprintf(f.out, " %d\n", *f.Steps)
	}
}
```

## File: `_examples/custom-formatter/godogs.go`
```go
package main

// Godogs available to eat
var Godogs int

func main() { /* usual main func */ }
```

## File: `_examples/custom-formatter/godogs_test.go`
```go
package main

import (
	"context"
	"fmt"
	"os"
	"testing"

	"github.com/cucumber/godog"
	"github.com/cucumber/godog/colors"
	flag "github.com/spf13/pflag"
)

var opts = godog.Options{
	Output: colors.Colored(os.Stdout),
	Format: "emoji",
}

func init() {
	godog.BindCommandLineFlags("godog.", &opts)
}

func TestMain(m *testing.M) {
	flag.Parse()
	opts.Paths = flag.Args()

	status := godog.TestSuite{
		Name:                 "godogs",
		TestSuiteInitializer: InitializeTestSuite,
		ScenarioInitializer:  InitializeScenario,
		Options:              &opts,
	}.Run()

	// This example test is expected to fail to showcase custom formatting, suppressing status.
	if status != 1 {
		os.Exit(1)
	}
}

func thereAreGodogs(available int) error {
	Godogs = available
	return nil
}

func iEat(num int) error {
	if Godogs < num {
		return fmt.Errorf("you cannot eat %d godogs, there are %d available", num, Godogs)
	}
	Godogs -= num
	return nil
}

func thereShouldBeRemaining(remaining int) error {
	if Godogs != remaining {
		return fmt.Errorf("expected %d godogs to be remaining, but there is %d", remaining, Godogs)
	}
	return nil
}
func thisStepIsPending() error {
	return godog.ErrPending
}

func InitializeTestSuite(ctx *godog.TestSuiteContext) {
	ctx.BeforeSuite(func() { Godogs = 0 })
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Before(func(ctx context.Context, sc *godog.Scenario) (context.Context, error) {
		Godogs = 0 // clean the state before every scenario

		return ctx, nil
	})

	ctx.Step(`^there are (\d+) godogs$`, thereAreGodogs)
	ctx.Step(`^I eat (\d+)$`, iEat)
	ctx.Step(`^there should be (\d+) remaining$`, thereShouldBeRemaining)
	ctx.Step(`^this step is pending$`, thisStepIsPending)
}
```

## File: `_examples/custom-formatter/features/emoji.feature`
```
# file: $GOPATH/godogs/features/godogs.feature
Feature: Custom emoji formatter examples
  In order to be happy
  As a hungry gopher
  I need to be able to eat godogs

  Scenario: Passing test
    Given there are 12 godogs
    When I eat 5
    Then there should be 7 remaining

  Scenario: Failing and Skipped test
    Given there are 12 godogs
    When I eat 5
    Then there should be 6 remaining
     And there should be 4 remaining

  Scenario: Undefined steps
    Given there are 12 godogs
    When I eat 5
    Then this step is not defined

  Scenario: Pending step
    Given there are 12 godogs
    When I eat 5
    Then this step is pending
```

## File: `_examples/db/Makefile`
```

define DB_SQL
CREATE TABLE users (
  `id` BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
  `username` VARCHAR(32) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uniq_email` (`email`)
) DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ENGINE = InnoDB;
endef

export DB_SQL

SQL := "$$DB_SQL"

test:
	mysql -u root -e 'DROP DATABASE IF EXISTS `godog_test`'
	mysql -u root -e 'CREATE DATABASE IF NOT EXISTS `godog_test`'
	@mysql -u root godog_test -e $(SQL)
	godog users.feature

.PHONY: test
```

## File: `_examples/db/README.md`
```markdown
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

## File: `_examples/db/api.go`
```go
package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

type server struct {
	db *sql.DB
}

type user struct {
	ID       int64  `json:"-"`
	Username string `json:"username"`
	Email    string `json:"-"`
}

func (s *server) users(w http.ResponseWriter, r *http.Request) {
	if r.Method != "GET" {
		fail(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	var users []*user
	rows, err := s.db.Query("SELECT id, email, username FROM users")
	defer rows.Close()
	switch err {
	case nil:
		for rows.Next() {
			user := &user{}
			if err := rows.Scan(&user.ID, &user.Email, &user.Username); err != nil {
				fail(w, fmt.Sprintf("failed to scan an user: %s", err), http.StatusInternalServerError)
				return
			}
			users = append(users, user)
		}
		if len(users) == 0 {
			users = make([]*user, 0) // an empty array in this case
		}
	default:
		fail(w, fmt.Sprintf("failed to fetch users: %s", err), http.StatusInternalServerError)
		return
	}

	data := struct {
		Users []*user `json:"users"`
	}{Users: users}

	ok(w, data)
}

func main() {
	db, err := sql.Open("mysql", "root@/godog")
	if err != nil {
		panic(err)
	}
	s := &server{db: db}
	http.HandleFunc("/users", s.users)
	http.ListenAndServe(":8080", nil)
}

// fail writes a json response with error msg and status header
func fail(w http.ResponseWriter, msg string, status int) {
	w.Header().Set("Content-Type", "application/json")

	data := struct {
		Error string `json:"error"`
	}{Error: msg}

	resp, _ := json.Marshal(data)
	w.WriteHeader(status)

	fmt.Fprintf(w, string(resp))
}

// ok writes data to response with 200 status
func ok(w http.ResponseWriter, data interface{}) {
	w.Header().Set("Content-Type", "application/json")

	if s, ok := data.(string); ok {
		fmt.Fprintf(w, s)
		return
	}

	resp, err := json.Marshal(data)
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		fail(w, "oops something evil has happened", 500)
		return
	}

	fmt.Fprintf(w, string(resp))
}
```

## File: `_examples/db/api_test.go`
```go
package main

import (
	"context"
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
	"reflect"
	"strings"

	txdb "github.com/DATA-DOG/go-txdb"
	"github.com/cucumber/godog"
)

func init() {
	// we register an sql driver txdb
	txdb.Register("txdb", "mysql", "root@/godog_test")
}

type apiFeature struct {
	server
	resp *httptest.ResponseRecorder
}

func (a *apiFeature) resetResponse(*godog.Scenario) {
	a.resp = httptest.NewRecorder()
	if a.db != nil {
		a.db.Close()
	}
	db, err := sql.Open("txdb", "api")
	if err != nil {
		panic(err)
	}
	a.db = db
}

func (a *apiFeature) iSendrequestTo(method, endpoint string) (err error) {
	req, err := http.NewRequest(method, endpoint, nil)
	if err != nil {
		return
	}

	// handle panic
	defer func() {
		switch t := recover().(type) {
		case string:
			err = fmt.Errorf(t)
		case error:
			err = t
		}
	}()

	switch endpoint {
	case "/users":
		a.users(a.resp, req)
	default:
		err = fmt.Errorf("unknown endpoint: %s", endpoint)
	}
	return
}

func (a *apiFeature) theResponseCodeShouldBe(code int) error {
	if code != a.resp.Code {
		if a.resp.Code >= 400 {
			return fmt.Errorf("expected response code to be: %d, but actual is: %d, response message: %s", code, a.resp.Code, string(a.resp.Body.Bytes()))
		}
		return fmt.Errorf("expected response code to be: %d, but actual is: %d", code, a.resp.Code)
	}
	return nil
}

func (a *apiFeature) theResponseShouldMatchJSON(body *godog.DocString) (err error) {
	var expected, actual interface{}

	// re-encode expected response
	if err = json.Unmarshal([]byte(body.Content), &expected); err != nil {
		return
	}

	// re-encode actual response too
	if err = json.Unmarshal(a.resp.Body.Bytes(), &actual); err != nil {
		return
	}

	// the matching may be adapted per different requirements.
	if !reflect.DeepEqual(expected, actual) {
		return fmt.Errorf("expected JSON does not match actual, %v vs. %v", expected, actual)
	}
	return nil
}

func (a *apiFeature) thereAreUsers(users *godog.Table) error {
	var fields []string
	var marks []string
	head := users.Rows[0].Cells
	for _, cell := range head {
		fields = append(fields, cell.Value)
		marks = append(marks, "?")
	}

	stmt, err := a.db.Prepare("INSERT INTO users (" + strings.Join(fields, ", ") + ") VALUES(" + strings.Join(marks, ", ") + ")")
	if err != nil {
		return err
	}
	for i := 1; i < len(users.Rows); i++ {
		var vals []interface{}
		for n, cell := range users.Rows[i].Cells {
			switch head[n].Value {
			case "username":
				vals = append(vals, cell.Value)
			case "email":
				vals = append(vals, cell.Value)
			default:
				return fmt.Errorf("unexpected column name: %s", head[n].Value)
			}
		}
		if _, err = stmt.Exec(vals...); err != nil {
			return err
		}
	}
	return nil
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	api := &apiFeature{}

	ctx.Before(func(ctx context.Context, sc *godog.Scenario) (context.Context, error) {
		api.resetResponse(sc)
		return ctx, nil
	})

	ctx.Step(`^I send "(GET|POST|PUT|DELETE)" request to "([^"]*)"$`, api.iSendrequestTo)
	ctx.Step(`^the response code should be (\d+)$`, api.theResponseCodeShouldBe)
	ctx.Step(`^the response should match json:$`, api.theResponseShouldMatchJSON)
	ctx.Step(`^there are users:$`, api.thereAreUsers)
}
```

## File: `_examples/db/features/users.feature`
```
Feature: users
  In order to use users api
  As an API user
  I need to be able to manage users

  Scenario: should get empty users
    When I send "GET" request to "/users"
    Then the response code should be 200
    And the response should match json:
      """
      {
        "users": []
      }
      """

  Scenario: should get users
    Given there are users:
      | username | email             |
      | john     | john.doe@mail.com |
      | jane     | jane.doe@mail.com |
    When I send "GET" request to "/users"
    Then the response code should be 200
    And the response should match json:
      """
      {
        "users": [
          {
            "username": "john"
          },
          {
            "username": "jane"
          }
        ]
      }
      """

  Scenario: should get users when there is only one
    Given there are users:
      | username | email           |
      | gopher   | gopher@mail.com |
    When I send "GET" request to "/users"
    Then the response code should be 200
    And the response should match json:
      """
      {
        "users": [
          {
            "username": "gopher"
          }
        ]
      }
      """
```

## File: `_examples/godogs/godogs.go`
```go
package godogs

import (
	"fmt"
)

// Godogs is an example behavior holder.
type Godogs int

// Add increments Godogs count.
func (g *Godogs) Add(n int) {
	*g = *g + Godogs(n)
}

// Eat decrements Godogs count or fails if there is not enough available.
func (g *Godogs) Eat(n int) error {
	ng := Godogs(n)

	if (g == nil && ng > 0) || ng > *g {
		return fmt.Errorf("you cannot eat %d godogs, there are %d available", n, g.Available())
	}

	if ng > 0 {
		*g = *g - ng
	}

	return nil
}

// Available returns the number of currently available Godogs.
func (g *Godogs) Available() int {
	if g == nil {
		return 0
	}

	return int(*g)
}
```

## File: `_examples/godogs/godogs_test.go`
```go
package godogs_test

// This example shows how to set up test suite runner with Go subtests and godog command line parameters.
// Sample commands:
// * run all scenarios from default directory (features): go test -test.run "^TestFeatures/"
// * run all scenarios and list subtest names: go test -test.v -test.run "^TestFeatures/"
// * run all scenarios from one feature file: go test -test.v -godog.paths features/nodogs.feature -test.run "^TestFeatures/"
// * run all scenarios from multiple feature files: go test -test.v -godog.paths features/nodogs.feature,features/godogs.feature -test.run "^TestFeatures/"
// * run single scenario as a subtest: go test -test.v -test.run "^TestFeatures/Eat_5_out_of_12$"
// * show usage help: go test -godog.help
// * show usage help if there were other test files in directory: go test -godog.help godogs_test.go
// * run scenarios with multiple formatters: go test -test.v -godog.format cucumber:cuc.json,pretty -test.run "^TestFeatures/"

import (
	"context"
	"flag"
	"fmt"
	"github.com/cucumber/godog/_examples/godogs"
	"os"
	"testing"

	"github.com/cucumber/godog"
	"github.com/cucumber/godog/colors"
)

var opts = godog.Options{
	Output:      colors.Colored(os.Stdout),
	Concurrency: 4,
}

func init() {
	godog.BindFlags("godog.", flag.CommandLine, &opts)
}

func TestFeatures(t *testing.T) {
	o := opts
	o.TestingT = t

	status := godog.TestSuite{
		Name:                 "godogs",
		Options:              &o,
		TestSuiteInitializer: InitializeTestSuite,
		ScenarioInitializer:  InitializeScenario,
	}.Run()

	if status == 2 {
		t.SkipNow()
	}

	if status != 0 {
		t.Fatalf("zero status code expected, %d received", status)
	}
}

type godogsCtxKey struct{}

func godogsToContext(ctx context.Context, g godogs.Godogs) context.Context {
	return context.WithValue(ctx, godogsCtxKey{}, &g)
}

func godogsFromContext(ctx context.Context) *godogs.Godogs {
	g, _ := ctx.Value(godogsCtxKey{}).(*godogs.Godogs)

	return g
}

// Concurrent execution of scenarios may lead to race conditions on shared resources.
// Use context to maintain data separation and avoid data races.

// Step definition can optionally receive context as a first argument.

func thereAreGodogs(ctx context.Context, available int) {
	godogsFromContext(ctx).Add(available)
}

// Step definition can return error, context, context and error, or nothing.

func iEat(ctx context.Context, num int) error {
	return godogsFromContext(ctx).Eat(num)
}

func thereShouldBeRemaining(ctx context.Context, remaining int) error {
	available := godogsFromContext(ctx).Available()
	if available != remaining {
		return fmt.Errorf("expected %d godogs to be remaining, but there is %d", remaining, available)
	}

	return nil
}

func thereShouldBeNoneRemaining(ctx context.Context) error {
	return thereShouldBeRemaining(ctx, 0)
}

func InitializeTestSuite(ctx *godog.TestSuiteContext) {
	ctx.BeforeSuite(func() { fmt.Println("Get the party started!") })
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Before(func(ctx context.Context, sc *godog.Scenario) (context.Context, error) {
		// Add initial godogs to context.
		return godogsToContext(ctx, 0), nil
	})

	ctx.Step(`^there are (\d+) godogs$`, thereAreGodogs)
	ctx.Step(`^I eat (\d+)$`, iEat)
	ctx.Step(`^there should be (\d+) remaining$`, thereShouldBeRemaining)
	ctx.Step(`^there should be none remaining$`, thereShouldBeNoneRemaining)
}
```

## File: `_examples/godogs/features/godogs.feature`
```
Feature: eat godogs
  In order to be happy
  As a hungry gopher
  I need to be able to eat godogs

  Scenario: Eat 5 out of 12
    Given there are 12 godogs
    When I eat 5
    Then there should be 7 remaining

  Scenario: Eat 12 out of 12
    Given there are 12 godogs
    When I eat 12
    Then there should be none remaining
```

## File: `_examples/godogs/features/nodogs.feature`
```
Feature: do not eat godogs
  In order to be fit
  As a well-fed gopher
  I need to be able to avoid godogs

  Scenario: Eat 0 out of 12
    Given there are 12 godogs
    When I eat 0
    Then there should be 12 remaining

  Scenario: Eat 0 out of 0
    Given there are 0 godogs
    When I eat 0
    Then there should be none remaining
```

## File: `_examples/incorrect-project-structure/README.md`
```markdown
This example is to help reproduce issue [#383](https://github.com/cucumber/godog/issues/383)

To run the example: 

    cd _examples/incorrect-project-structure
    go run ../../cmd/godog
```

## File: `_examples/incorrect-project-structure/go.mod`
```
module incorrect-project-structure

go 1.13

require github.com/cucumber/godog v0.15.1

replace github.com/cucumber/godog => ../../
```

## File: `_examples/incorrect-project-structure/go.sum`
```
github.com/cpuguy83/go-md2man/v2 v2.0.1/go.mod h1:tgQtvFlXSQOSOSIRvRPT7W67SCa46tRHOmNcaadrF8o=
github.com/cpuguy83/go-md2man/v2 v2.0.2/go.mod h1:tgQtvFlXSQOSOSIRvRPT7W67SCa46tRHOmNcaadrF8o=
github.com/cucumber/gherkin/go/v26 v26.0.2 h1:DjNKtTIv5VG0F1XaJ2xYNk+ck8pJWRNFzyajkc/Y4l4=
github.com/cucumber/gherkin/go/v26 v26.0.2/go.mod h1:Xf+SrSuFbivEDZvmHjTShord3zlEkqsj7QB4sxl1SuU=
github.com/cucumber/gherkin/go/v26 v26.2.0 h1:EgIjePLWiPeslwIWmNQ3XHcypPsWAHoMCz/YEBKP4GI=
github.com/cucumber/gherkin/go/v26 v26.2.0/go.mod h1:t2GAPnB8maCT4lkHL99BDCVNzCh1d7dBhCLt150Nr/0=
github.com/cucumber/messages/go/v21 v21.0.1 h1:wzA0LxwjlWQYZd32VTlAVDTkW6inOFmSM+RuOwHZiMI=
github.com/cucumber/messages/go/v21 v21.0.1/go.mod h1:zheH/2HS9JLVFukdrsPWoPdmUtmYQAQPLk7w5vWsk5s=
github.com/cucumber/messages/go/v22 v22.0.0/go.mod h1:aZipXTKc0JnjCsXrJnuZpWhtay93k7Rn3Dee7iyPJjs=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/gofrs/uuid v4.2.0+incompatible h1:yyYWMnhkhrKwwr8gAOcOCYxOOscHgDS9yZgBrnJfGa0=
github.com/gofrs/uuid v4.2.0+incompatible/go.mod h1:b2aQJv3Z4Fp6yNu3cdSllBxTCLRxnplIgP/c0N/04lM=
github.com/gofrs/uuid v4.3.1+incompatible h1:0/KbAdpx3UXAx1kEOWHJeOkpbgRFGHVgv+CFIY7dBJI=
github.com/gofrs/uuid v4.3.1+incompatible/go.mod h1:b2aQJv3Z4Fp6yNu3cdSllBxTCLRxnplIgP/c0N/04lM=
github.com/gopherjs/gopherjs v0.0.0-20181017120253-0766667cb4d1 h1:EGx4pi6eqNxGaHF6qqu48+N2wcFQ5qg5FXgOdqsJ5d8=
github.com/gopherjs/gopherjs v0.0.0-20181017120253-0766667cb4d1/go.mod h1:wJfORRmW1u3UXTncJ5qlYoELFm8eSnnEO6hX4iZ3EWY=
github.com/hashicorp/go-immutable-radix v1.3.0/go.mod h1:0y9vanUI8NX6FsYoO3zeMjhV/C5i9g4Q3DwcSNZ4P60=
github.com/hashicorp/go-immutable-radix v1.3.1 h1:DKHmCUm2hRBK510BaiZlwvpD40f8bJFeZnpfm2KLowc=
github.com/hashicorp/go-immutable-radix v1.3.1/go.mod h1:0y9vanUI8NX6FsYoO3zeMjhV/C5i9g4Q3DwcSNZ4P60=
github.com/hashicorp/go-memdb v1.3.2 h1:RBKHOsnSszpU6vxq80LzC2BaQjuuvoyaQbkLTf7V7g8=
github.com/hashicorp/go-memdb v1.3.2/go.mod h1:Mluclgwib3R93Hk5fxEfiRhB+6Dar64wWh71LpNSe3g=
github.com/hashicorp/go-memdb v1.3.4 h1:XSL3NR682X/cVk2IeV0d70N4DZ9ljI885xAEU8IoK3c=
github.com/hashicorp/go-memdb v1.3.4/go.mod h1:uBTr1oQbtuMgd1SSGoR8YV27eT3sBHbYiNm53bMpgSg=
github.com/hashicorp/go-uuid v1.0.0/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/go-uuid v1.0.2 h1:cfejS+Tpcp13yd5nYHWDI6qVCny6wyX2Mt5SGur2IGE=
github.com/hashicorp/go-uuid v1.0.2/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/golang-lru v0.5.0/go.mod h1:/m3WP610KZHVQ1SGc6re/UDhFvYD7pJ4Ao+sR/qLZy8=
github.com/hashicorp/golang-lru v0.5.4 h1:YDjusn29QI/Das2iO9M0BHnIbxPeyuCHsjMW+lJfyTc=
github.com/hashicorp/golang-lru v0.5.4/go.mod h1:iADmTwqILo4mZ8BN3D2Q6+9jd8WM5uGBxy+E8yxSoD4=
github.com/inconshreveable/mousetrap v1.0.0/go.mod h1:PxqpIevigyE2G7u3NXJIT2ANytuPF1OarO4DADm73n8=
github.com/inconshreveable/mousetrap v1.1.0/go.mod h1:vpF70FUmC8bwa3OWnCshd2FqLfsEA9PFc4w1p2J65bw=
github.com/jtolds/gls v4.20.0+incompatible h1:xdiiI2gbIgH/gLH7ADydsJ1uDOEzR8yvV7C0MuV77Wo=
github.com/jtolds/gls v4.20.0+incompatible/go.mod h1:QJZ7F/aHp+rZTRtaJ1ow/lLfFfVYBRgL+9YlvaHOwJU=
github.com/kr/pretty v0.2.1 h1:Fmg33tUaq4/8ym9TJN1x7sLJnHVwhP33CNkpYV/7rwI=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/russross/blackfriday/v2 v2.1.0/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/smartystreets/assertions v0.0.0-20180927180507-b2de0cb4f26d h1:zE9ykElWQ6/NYmHa3jpm/yHnI4xSofP+UP6SpjHcSeM=
github.com/smartystreets/assertions v0.0.0-20180927180507-b2de0cb4f26d/go.mod h1:OnSkiWE9lh6wB0YB77sQom3nweQdgAjqCqsofrRNTgc=
github.com/smartystreets/goconvey v1.6.4 h1:fv0U8FUIMPNf1L9lnHLvLhgicrIVChEkdzIKYqbNC9s=
github.com/smartystreets/goconvey v1.6.4/go.mod h1:syvi0/a8iFYH4r/RixwvyeAJjdLS9QV7WQ/tjFTllLA=
github.com/spf13/cobra v1.4.0/go.mod h1:Wo4iy3BUC+X2Fybo0PDqwJIv3dNRiZLHQymsfxlB84g=
github.com/spf13/cobra v1.7.0/go.mod h1:uLxZILRyS/50WlhOIKD7W6V5bgeIt+4sICxh6uRMrb0=
github.com/spf13/pflag v1.0.5 h1:iy+VFUOCP1a+8yFto/drg2CJ5u0yRoB7fZw3DKv/JXA=
github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/pflag v1.0.7 h1:vN6T9TfwStFPFM5XzjsvmzZkLuaLX+HS+0SeFLRgU6M=
github.com/spf13/pflag v1.0.7/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.4.0/go.mod h1:YvHI0jy2hoMjB+UWwv71VJQ9isScKT/TqJzVSSt89Yw=
github.com/stretchr/objx v0.5.0/go.mod h1:Yh+to48EsGEfYuaHDzXPcE3xhTkx73EhmCGUpEOglKo=
github.com/stretchr/testify v1.7.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.8.0/go.mod h1:yNjHg4UonilssWZ8iaSj1OCr/vHnekPRkoO+kdMU+MU=
github.com/stretchr/testify v1.8.1 h1:w7B6lhMri9wdJUVmEZPGGhZzrYTPvgJArz7wNPgYKsk=
github.com/stretchr/testify v1.8.1/go.mod h1:w2LPCIKwWwSfY2zedu0+kehJoqGctiVI29o6fzry7u4=
github.com/stretchr/testify v1.8.2/go.mod h1:w2LPCIKwWwSfY2zedu0+kehJoqGctiVI29o6fzry7u4=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/net v0.0.0-20190311183353-d8887717615a/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/tools v0.0.0-20190328211700-ab21143f2384/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `_examples/incorrect-project-structure/main.go`
```go
package main

import "github.com/cucumber/godog"

func InitializeScenario(ctx *godog.ScenarioContext) {

}
```

## File: `cmd/godog/main.go`
```go
package main

import (
	"fmt"
	"os"

	"github.com/cucumber/godog/cmd/godog/internal"
)

func main() {
	rootCmd := internal.CreateRootCmd()
	buildCmd := internal.CreateBuildCmd()
	runCmd := internal.CreateRunCmd()
	versionCmd := internal.CreateVersionCmd()

	rootCmd.AddCommand(&buildCmd, &runCmd, &versionCmd)

	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
```

## File: `cmd/godog/internal/cmd_build.go`
```go
package internal

import (
	"fmt"
	"go/build"
	"path/filepath"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/internal/builder"

	"github.com/spf13/cobra"
)

var buildOutput string
var buildOutputDefault = "godog.test"

// CreateBuildCmd creates the build subcommand.
func CreateBuildCmd() cobra.Command {
	if build.Default.GOOS == "windows" {
		buildOutputDefault += ".exe"
	}

	buildCmd := cobra.Command{
		Use:   "build",
		Short: "Compiles a test runner",
		Long: `Compiles a test runner. Command should be run from the directory of tested
package and contain buildable go source.

The test runner can be executed with the same flags as when using godog run.`,
		Example: `  godog build
  godog build -o ` + buildOutputDefault,
		RunE: buildCmdRunFunc,
	}

	buildCmd.Flags().StringVarP(&buildOutput, "output", "o", buildOutputDefault, `compiles the test runner to the named file
`)

	return buildCmd
}

func buildCmdRunFunc(cmd *cobra.Command, args []string) error {
	fmt.Println(colors.Yellow("Use of godog CLI is deprecated, please use *testing.T instead."))
	fmt.Println(colors.Yellow("See https://github.com/cucumber/godog/discussions/478 for details."))

	bin, err := filepath.Abs(buildOutput)
	if err != nil {
		return fmt.Errorf("could not locate absolute path for: %q. reason: %v", buildOutput, err)
	}

	if err = builder.Build(bin); err != nil {
		return fmt.Errorf("could not build binary at: %q. reason: %v", buildOutput, err)
	}

	return nil
}
```

## File: `cmd/godog/internal/cmd_root.go`
```go
package internal

import (
	"github.com/spf13/cobra"
	"github.com/spf13/pflag"

	"github.com/cucumber/godog/internal/flags"
)

var version bool
var output string

// CreateRootCmd creates the root command.
func CreateRootCmd() cobra.Command {
	rootCmd := cobra.Command{
		Use: "godog",
		Long: `Creates and runs test runner for the given feature files.
Command should be run from the directory of tested package
and contain buildable go source.`,
		Args: cobra.ArbitraryArgs,
		// Deprecated: Use godog build, godog run or godog version.
		// This is to support the legacy direct usage of the root command.
		RunE: runRootCmd,
	}

	bindRootCmdFlags(rootCmd.Flags())

	return rootCmd
}

func runRootCmd(cmd *cobra.Command, args []string) error {
	if version {
		versionCmdRunFunc(cmd, args)
		return nil
	}

	if len(output) > 0 {
		buildOutput = output
		if err := buildCmdRunFunc(cmd, args); err != nil {
			return err
		}
	}

	return runCmdRunFunc(cmd, args)
}

func bindRootCmdFlags(flagSet *pflag.FlagSet) {
	flagSet.StringVarP(&output, "output", "o", "", "compiles the test runner to the named file")
	flagSet.BoolVar(&version, "version", false, "show current version")

	flags.BindRunCmdFlags("", flagSet, &opts)

	// Since using the root command directly is deprecated.
	// All flags will be hidden
	flagSet.MarkHidden("output")
	flagSet.MarkHidden("version")
	flagSet.MarkHidden("no-colors")
	flagSet.MarkHidden("concurrency")
	flagSet.MarkHidden("tags")
	flagSet.MarkHidden("format")
	flagSet.MarkHidden("definitions")
	flagSet.MarkHidden("stop-on-failure")
	flagSet.MarkHidden("strict")
	flagSet.MarkHidden("random")
}
```

## File: `cmd/godog/internal/cmd_run.go`
```go
package internal

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"syscall"

	"github.com/spf13/cobra"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/internal/builder"
	"github.com/cucumber/godog/internal/flags"
)

var opts flags.Options

// CreateRunCmd creates the run subcommand.
func CreateRunCmd() cobra.Command {
	runCmd := cobra.Command{
		Use:   "run [features]",
		Short: "Compiles and runs a test runner",
		Long: `Compiles and runs test runner for the given feature files.
Command should be run from the directory of tested package and contain
buildable go source.`,
		Example: `  godog run
  godog run <feature>
  godog run <feature> <feature>

  Optional feature(s) to run:
    dir (features/)
    feature (*.feature)
    scenario at specific line (*.feature:10)
  If no feature arguments are supplied, godog will use "features/" by default.`,
		RunE:         runCmdRunFunc,
		SilenceUsage: true,
	}

	flags.BindRunCmdFlags("", runCmd.Flags(), &opts)

	return runCmd
}

func runCmdRunFunc(cmd *cobra.Command, args []string) error {
	fmt.Println(colors.Yellow("Use of godog CLI is deprecated, please use *testing.T instead."))
	fmt.Println(colors.Yellow("See https://github.com/cucumber/godog/discussions/478 for details."))

	osArgs := os.Args[1:]

	if len(osArgs) > 0 && osArgs[0] == "run" {
		osArgs = osArgs[1:]
	}

	if err := buildAndRunGodog(osArgs); err != nil {
		return err
	}

	return nil
}

func buildAndRunGodog(args []string) (err error) {
	bin, err := filepath.Abs(buildOutputDefault)
	if err != nil {
		return err
	}

	if err = builder.Build(bin); err != nil {
		return err
	}

	defer os.Remove(bin)

	return runGodog(bin, args)
}

func runGodog(bin string, args []string) (err error) {
	cmd := exec.Command(bin, args...)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	cmd.Stdin = os.Stdin
	cmd.Env = os.Environ()

	if err = cmd.Start(); err != nil {
		return err
	}

	if err = cmd.Wait(); err == nil {
		return nil
	}

	exiterr, ok := err.(*exec.ExitError)
	if !ok {
		return err
	}

	st, ok := exiterr.Sys().(syscall.WaitStatus)
	if !ok {
		return fmt.Errorf("failed to convert error to syscall wait status. original error: %w", exiterr)
	}

	// This works on both Unix and Windows. Although package
	// syscall is generally platform dependent, WaitStatus is
	// defined for both Unix and Windows and in both cases has
	// an ExitStatus() method with the same signature.
	if st.ExitStatus() > 0 {
		return err
	}

	return nil
}
```

## File: `cmd/godog/internal/cmd_version.go`
```go
package internal

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"

	"github.com/cucumber/godog"
)

// CreateVersionCmd creates the version subcommand.
func CreateVersionCmd() cobra.Command {
	versionCmd := cobra.Command{
		Use:     "version",
		Short:   "Show current version",
		Run:     versionCmdRunFunc,
		Version: godog.Version,
	}

	return versionCmd
}

func versionCmdRunFunc(cmd *cobra.Command, args []string) {
	fmt.Fprintln(os.Stdout, "Godog version is:", godog.Version)
}
```

## File: `colors/ansi_others.go`
```go
// Copyright 2014 shiena Authors. All rights reserved.
// Use of this source code is governed by a MIT-style
// license that can be found in the LICENSE file.

//go:build !windows
// +build !windows

package colors

import "io"

type ansiColorWriter struct {
	w    io.Writer
	mode outputMode
}

func (cw *ansiColorWriter) Write(p []byte) (int, error) {
	return cw.w.Write(p)
}
```

## File: `colors/ansi_windows.go`
```go
// Copyright 2014 shiena Authors. All rights reserved.
// Use of this source code is governed by a MIT-style
// license that can be found in the LICENSE file.

//go:build windows
// +build windows

package colors

import (
	"bytes"
	"io"
	"strings"
	"syscall"
	"unsafe"
)

type csiState int

const (
	outsideCsiCode csiState = iota
	firstCsiCode
	secondCsiCode
)

type parseResult int

const (
	noConsole parseResult = iota
	changedColor
	unknown
)

type ansiColorWriter struct {
	w             io.Writer
	mode          outputMode
	state         csiState
	paramStartBuf bytes.Buffer
	paramBuf      bytes.Buffer
}

const (
	firstCsiChar   byte = '\x1b'
	secondeCsiChar byte = '['
	separatorChar  byte = ';'
	sgrCode        byte = 'm'
)

const (
	foregroundBlue      = uint16(0x0001)
	foregroundGreen     = uint16(0x0002)
	foregroundRed       = uint16(0x0004)
	foregroundIntensity = uint16(0x0008)
	backgroundBlue      = uint16(0x0010)
	backgroundGreen     = uint16(0x0020)
	backgroundRed       = uint16(0x0040)
	backgroundIntensity = uint16(0x0080)
	underscore          = uint16(0x8000)

	foregroundMask = foregroundBlue | foregroundGreen | foregroundRed | foregroundIntensity
	backgroundMask = backgroundBlue | backgroundGreen | backgroundRed | backgroundIntensity
)

const (
	ansiReset        = "0"
	ansiIntensityOn  = "1"
	ansiIntensityOff = "21"
	ansiUnderlineOn  = "4"
	ansiUnderlineOff = "24"
	ansiBlinkOn      = "5"
	ansiBlinkOff     = "25"

	ansiForegroundBlack   = "30"
	ansiForegroundRed     = "31"
	ansiForegroundGreen   = "32"
	ansiForegroundYellow  = "33"
	ansiForegroundBlue    = "34"
	ansiForegroundMagenta = "35"
	ansiForegroundCyan    = "36"
	ansiForegroundWhite   = "37"
	ansiForegroundDefault = "39"

	ansiBackgroundBlack   = "40"
	ansiBackgroundRed     = "41"
	ansiBackgroundGreen   = "42"
	ansiBackgroundYellow  = "43"
	ansiBackgroundBlue    = "44"
	ansiBackgroundMagenta = "45"
	ansiBackgroundCyan    = "46"
	ansiBackgroundWhite   = "47"
	ansiBackgroundDefault = "49"

	ansiLightForegroundGray    = "90"
	ansiLightForegroundRed     = "91"
	ansiLightForegroundGreen   = "92"
	ansiLightForegroundYellow  = "93"
	ansiLightForegroundBlue    = "94"
	ansiLightForegroundMagenta = "95"
	ansiLightForegroundCyan    = "96"
	ansiLightForegroundWhite   = "97"

	ansiLightBackgroundGray    = "100"
	ansiLightBackgroundRed     = "101"
	ansiLightBackgroundGreen   = "102"
	ansiLightBackgroundYellow  = "103"
	ansiLightBackgroundBlue    = "104"
	ansiLightBackgroundMagenta = "105"
	ansiLightBackgroundCyan    = "106"
	ansiLightBackgroundWhite   = "107"
)

type drawType int

const (
	foreground drawType = iota
	background
)

type winColor struct {
	code     uint16
	drawType drawType
}

var colorMap = map[string]winColor{
	ansiForegroundBlack:   {0, foreground},
	ansiForegroundRed:     {foregroundRed, foreground},
	ansiForegroundGreen:   {foregroundGreen, foreground},
	ansiForegroundYellow:  {foregroundRed | foregroundGreen, foreground},
	ansiForegroundBlue:    {foregroundBlue, foreground},
	ansiForegroundMagenta: {foregroundRed | foregroundBlue, foreground},
	ansiForegroundCyan:    {foregroundGreen | foregroundBlue, foreground},
	ansiForegroundWhite:   {foregroundRed | foregroundGreen | foregroundBlue, foreground},
	ansiForegroundDefault: {foregroundRed | foregroundGreen | foregroundBlue, foreground},

	ansiBackgroundBlack:   {0, background},
	ansiBackgroundRed:     {backgroundRed, background},
	ansiBackgroundGreen:   {backgroundGreen, background},
	ansiBackgroundYellow:  {backgroundRed | backgroundGreen, background},
	ansiBackgroundBlue:    {backgroundBlue, background},
	ansiBackgroundMagenta: {backgroundRed | backgroundBlue, background},
	ansiBackgroundCyan:    {backgroundGreen | backgroundBlue, background},
	ansiBackgroundWhite:   {backgroundRed | backgroundGreen | backgroundBlue, background},
	ansiBackgroundDefault: {0, background},

	ansiLightForegroundGray:    {foregroundIntensity, foreground},
	ansiLightForegroundRed:     {foregroundIntensity | foregroundRed, foreground},
	ansiLightForegroundGreen:   {foregroundIntensity | foregroundGreen, foreground},
	ansiLightForegroundYellow:  {foregroundIntensity | foregroundRed | foregroundGreen, foreground},
	ansiLightForegroundBlue:    {foregroundIntensity | foregroundBlue, foreground},
	ansiLightForegroundMagenta: {foregroundIntensity | foregroundRed | foregroundBlue, foreground},
	ansiLightForegroundCyan:    {foregroundIntensity | foregroundGreen | foregroundBlue, foreground},
	ansiLightForegroundWhite:   {foregroundIntensity | foregroundRed | foregroundGreen | foregroundBlue, foreground},

	ansiLightBackgroundGray:    {backgroundIntensity, background},
	ansiLightBackgroundRed:     {backgroundIntensity | backgroundRed, background},
	ansiLightBackgroundGreen:   {backgroundIntensity | backgroundGreen, background},
	ansiLightBackgroundYellow:  {backgroundIntensity | backgroundRed | backgroundGreen, background},
	ansiLightBackgroundBlue:    {backgroundIntensity | backgroundBlue, background},
	ansiLightBackgroundMagenta: {backgroundIntensity | backgroundRed | backgroundBlue, background},
	ansiLightBackgroundCyan:    {backgroundIntensity | backgroundGreen | backgroundBlue, background},
	ansiLightBackgroundWhite:   {backgroundIntensity | backgroundRed | backgroundGreen | backgroundBlue, background},
}

var (
	kernel32                       = syscall.NewLazyDLL("kernel32.dll")
	procSetConsoleTextAttribute    = kernel32.NewProc("SetConsoleTextAttribute")
	procGetConsoleScreenBufferInfo = kernel32.NewProc("GetConsoleScreenBufferInfo")
	defaultAttr                    *textAttributes
)

func init() {
	screenInfo := getConsoleScreenBufferInfo(uintptr(syscall.Stdout))
	if screenInfo != nil {
		colorMap[ansiForegroundDefault] = winColor{
			screenInfo.WAttributes & (foregroundRed | foregroundGreen | foregroundBlue),
			foreground,
		}
		colorMap[ansiBackgroundDefault] = winColor{
			screenInfo.WAttributes & (backgroundRed | backgroundGreen | backgroundBlue),
			background,
		}
		defaultAttr = convertTextAttr(screenInfo.WAttributes)
	}
}

type coord struct {
	X, Y int16
}

type smallRect struct {
	Left, Top, Right, Bottom int16
}

type consoleScreenBufferInfo struct {
	DwSize              coord
	DwCursorPosition    coord
	WAttributes         uint16
	SrWindow            smallRect
	DwMaximumWindowSize coord
}

func getConsoleScreenBufferInfo(hConsoleOutput uintptr) *consoleScreenBufferInfo {
	var csbi consoleScreenBufferInfo
	ret, _, _ := procGetConsoleScreenBufferInfo.Call(
		hConsoleOutput,
		uintptr(unsafe.Pointer(&csbi)))
	if ret == 0 {
		return nil
	}
	return &csbi
}

func setConsoleTextAttribute(hConsoleOutput uintptr, wAttributes uint16) bool {
	ret, _, _ := procSetConsoleTextAttribute.Call(
		hConsoleOutput,
		uintptr(wAttributes))
	return ret != 0
}

type textAttributes struct {
	foregroundColor     uint16
	backgroundColor     uint16
	foregroundIntensity uint16
	backgroundIntensity uint16
	underscore          uint16
	otherAttributes     uint16
}

func convertTextAttr(winAttr uint16) *textAttributes {
	fgColor := winAttr & (foregroundRed | foregroundGreen | foregroundBlue)
	bgColor := winAttr & (backgroundRed | backgroundGreen | backgroundBlue)
	fgIntensity := winAttr & foregroundIntensity
	bgIntensity := winAttr & backgroundIntensity
	underline := winAttr & underscore
	otherAttributes := winAttr &^ (foregroundMask | backgroundMask | underscore)
	return &textAttributes{fgColor, bgColor, fgIntensity, bgIntensity, underline, otherAttributes}
}

func convertWinAttr(textAttr *textAttributes) uint16 {
	var winAttr uint16
	winAttr |= textAttr.foregroundColor
	winAttr |= textAttr.backgroundColor
	winAttr |= textAttr.foregroundIntensity
	winAttr |= textAttr.backgroundIntensity
	winAttr |= textAttr.underscore
	winAttr |= textAttr.otherAttributes
	return winAttr
}

func changeColor(param []byte) parseResult {
	screenInfo := getConsoleScreenBufferInfo(uintptr(syscall.Stdout))
	if screenInfo == nil {
		return noConsole
	}

	winAttr := convertTextAttr(screenInfo.WAttributes)
	strParam := string(param)
	if len(strParam) <= 0 {
		strParam = "0"
	}
	csiParam := strings.Split(strParam, string(separatorChar))
	for _, p := range csiParam {
		c, ok := colorMap[p]
		switch {
		case !ok:
			switch p {
			case ansiReset:
				winAttr.foregroundColor = defaultAttr.foregroundColor
				winAttr.backgroundColor = defaultAttr.backgroundColor
				winAttr.foregroundIntensity = defaultAttr.foregroundIntensity
				winAttr.backgroundIntensity = defaultAttr.backgroundIntensity
				winAttr.underscore = 0
				winAttr.otherAttributes = 0
			case ansiIntensityOn:
				winAttr.foregroundIntensity = foregroundIntensity
			case ansiIntensityOff:
				winAttr.foregroundIntensity = 0
			case ansiUnderlineOn:
				winAttr.underscore = underscore
			case ansiUnderlineOff:
				winAttr.underscore = 0
			case ansiBlinkOn:
				winAttr.backgroundIntensity = backgroundIntensity
			case ansiBlinkOff:
				winAttr.backgroundIntensity = 0
			default:
				// unknown code
			}
		case c.drawType == foreground:
			winAttr.foregroundColor = c.code
		case c.drawType == background:
			winAttr.backgroundColor = c.code
		}
	}
	winTextAttribute := convertWinAttr(winAttr)
	setConsoleTextAttribute(uintptr(syscall.Stdout), winTextAttribute)

	return changedColor
}

func parseEscapeSequence(command byte, param []byte) parseResult {
	if defaultAttr == nil {
		return noConsole
	}

	switch command {
	case sgrCode:
		return changeColor(param)
	default:
		return unknown
	}
}

func (cw *ansiColorWriter) flushBuffer() (int, error) {
	return cw.flushTo(cw.w)
}

func (cw *ansiColorWriter) resetBuffer() (int, error) {
	return cw.flushTo(nil)
}

func (cw *ansiColorWriter) flushTo(w io.Writer) (int, error) {
	var n1, n2 int
	var err error

	startBytes := cw.paramStartBuf.Bytes()
	cw.paramStartBuf.Reset()
	if w != nil {
		n1, err = cw.w.Write(startBytes)
		if err != nil {
			return n1, err
		}
	} else {
		n1 = len(startBytes)
	}
	paramBytes := cw.paramBuf.Bytes()
	cw.paramBuf.Reset()
	if w != nil {
		n2, err = cw.w.Write(paramBytes)
		if err != nil {
			return n1 + n2, err
		}
	} else {
		n2 = len(paramBytes)
	}
	return n1 + n2, nil
}

func isParameterChar(b byte) bool {
	return ('0' <= b && b <= '9') || b == separatorChar
}

func (cw *ansiColorWriter) Write(p []byte) (int, error) {
	r, nw, first, last := 0, 0, 0, 0
	if cw.mode != discardNonColorEscSeq {
		cw.state = outsideCsiCode
		cw.resetBuffer()
	}

	var err error
	for i, ch := range p {
		switch cw.state {
		case outsideCsiCode:
			if ch == firstCsiChar {
				cw.paramStartBuf.WriteByte(ch)
				cw.state = firstCsiCode
			}
		case firstCsiCode:
			switch ch {
			case firstCsiChar:
				cw.paramStartBuf.WriteByte(ch)
				break
			case secondeCsiChar:
				cw.paramStartBuf.WriteByte(ch)
				cw.state = secondCsiCode
				last = i - 1
			default:
				cw.resetBuffer()
				cw.state = outsideCsiCode
			}
		case secondCsiCode:
			if isParameterChar(ch) {
				cw.paramBuf.WriteByte(ch)
			} else {
				nw, err = cw.w.Write(p[first:last])
				r += nw
				if err != nil {
					return r, err
				}
				first = i + 1
				result := parseEscapeSequence(ch, cw.paramBuf.Bytes())
				if result == noConsole || (cw.mode == outputNonColorEscSeq && result == unknown) {
					cw.paramBuf.WriteByte(ch)
					nw, err := cw.flushBuffer()
					if err != nil {
						return r, err
					}
					r += nw
				} else {
					n, _ := cw.resetBuffer()
					// Add one more to the size of the buffer for the last ch
					r += n + 1
				}

				cw.state = outsideCsiCode
			}
		default:
			cw.state = outsideCsiCode
		}
	}

	if cw.mode != discardNonColorEscSeq || cw.state == outsideCsiCode {
		nw, err = cw.w.Write(p[first:])
		r += nw
	}

	return r, err
}
```

## File: `colors/colors.go`
```go
package colors

import (
	"fmt"
	"strings"
)

const ansiEscape = "\x1b"

// a color code type
type color int

// some ansi colors
const (
	black color = iota + 30
	red
	green
	yellow
	blue    // unused
	magenta // unused
	cyan
	white
)

func colorize(s interface{}, c color) string {
	return fmt.Sprintf("%s[%dm%v%s[0m", ansiEscape, c, s, ansiEscape)
}

// ColorFunc is a helper type to create colorized strings.
type ColorFunc func(interface{}) string

// Bold will accept a ColorFunc and return a new ColorFunc
// that will make the string bold.
func Bold(fn ColorFunc) ColorFunc {
	return ColorFunc(func(input interface{}) string {
		return strings.Replace(fn(input), ansiEscape+"[", ansiEscape+"[1;", 1)
	})
}

// Green will accept an interface and return a colorized green string.
func Green(s interface{}) string {
	return colorize(s, green)
}

// Red will accept an interface and return a colorized red string.
func Red(s interface{}) string {
	return colorize(s, red)
}

// Cyan will accept an interface and return a colorized cyan string.
func Cyan(s interface{}) string {
	return colorize(s, cyan)
}

// Black will accept an interface and return a colorized black string.
func Black(s interface{}) string {
	return colorize(s, black)
}

// Yellow will accept an interface and return a colorized yellow string.
func Yellow(s interface{}) string {
	return colorize(s, yellow)
}

// White will accept an interface and return a colorized white string.
func White(s interface{}) string {
	return colorize(s, white)
}
```

## File: `colors/no_colors.go`
```go
package colors

import (
	"bytes"
	"fmt"
	"io"
)

type noColors struct {
	out     io.Writer
	lastbuf bytes.Buffer
}

// Uncolored will accept and io.Writer and return a
// new io.Writer that won't include colors.
func Uncolored(w io.Writer) io.Writer {
	return &noColors{out: w}
}

func (w *noColors) Write(data []byte) (n int, err error) {
	er := bytes.NewBuffer(data)
loop:
	for {
		c1, _, err := er.ReadRune()
		if err != nil {
			break loop
		}
		if c1 != 0x1b {
			fmt.Fprint(w.out, string(c1))
			continue
		}
		c2, _, err := er.ReadRune()
		if err != nil {
			w.lastbuf.WriteRune(c1)
			break loop
		}
		if c2 != 0x5b {
			w.lastbuf.WriteRune(c1)
			w.lastbuf.WriteRune(c2)
			continue
		}

		var buf bytes.Buffer
		for {
			c, _, err := er.ReadRune()
			if err != nil {
				w.lastbuf.WriteRune(c1)
				w.lastbuf.WriteRune(c2)
				w.lastbuf.Write(buf.Bytes())
				break loop
			}
			if ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') || c == '@' {
				break
			}
			buf.Write([]byte(string(c)))
		}
	}
	return len(data) - w.lastbuf.Len(), nil
}
```

## File: `colors/writer.go`
```go
// Copyright 2014 shiena Authors. All rights reserved.
// Use of this source code is governed by a MIT-style
// license that can be found in the LICENSE file.

package colors

import "io"

type outputMode int

// DiscardNonColorEscSeq supports the divided color escape sequence.
// But non-color escape sequence is not output.
// Please use the OutputNonColorEscSeq If you want to output a non-color
// escape sequences such as ncurses. However, it does not support the divided
// color escape sequence.
const (
	_ outputMode = iota
	discardNonColorEscSeq
	outputNonColorEscSeq // unused
)

// Colored creates and initializes a new ansiColorWriter
// using io.Writer w as its initial contents.
// In the console of Windows, which change the foreground and background
// colors of the text by the escape sequence.
// In the console of other systems, which writes to w all text.
func Colored(w io.Writer) io.Writer {
	return createModeAnsiColorWriter(w, discardNonColorEscSeq)
}

// NewModeAnsiColorWriter create and initializes a new ansiColorWriter
// by specifying the outputMode.
func createModeAnsiColorWriter(w io.Writer, mode outputMode) io.Writer {
	if _, ok := w.(*ansiColorWriter); !ok {
		return &ansiColorWriter{
			w:    w,
			mode: mode,
		}
	}
	return w
}
```

## File: `features/background.feature`
```
Feature: run background
  In order to test application behavior
  As a test suite
  I need to be able to run background correctly

  Scenario: should run background steps
    Given a feature "normal.feature" file:
      """
      Feature: with background

        Background:
          Given a feature path "features/load.feature:6"

        Scenario: parse a scenario
          When I parse features
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      a feature path "features/load.feature:6"
      I parse features
      I should have 1 scenario registered
      """

  Scenario: should skip all consequent steps on failure
    Given a feature "normal.feature" file:
      """
      Feature: with background

        Background:
          Given a failing step
          And a feature path "features/load.feature:6"

        Scenario: parse a scenario
          When I parse features
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have failed
    And the following steps should be failed:
      """
      a failing step
      """
    And the following steps should be skipped:
      """
      a feature path "features/load.feature:6"
      I parse features
      I should have 1 scenario registered
      """

  Scenario: should continue undefined steps
    Given a feature "normal.feature" file:
      """
      Feature: with background

        Background:
          Given an undefined step

        Scenario: parse a scenario
          When I do undefined action
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be undefined:
      """
      an undefined step
      I do undefined action
      """
    And the following steps should be skipped:
      """
      I should have 1 scenario registered
      """
```

## File: `features/events.feature`
```
Feature: suite events
  In order to run tasks before and after important events
  As a test suite
  I need to provide a way to hook into these events

  Background:
    Given I'm listening to suite events

  Scenario: triggers before scenario event
    Given a feature path "features/load.feature:6"
    When I run feature suite
    Then there was event triggered before scenario "load features within path"

  Scenario: triggers appropriate events for a single scenario
    Given a feature path "features/load.feature:6"
    When I run feature suite
    Then these events had to be fired for a number of times:
      | BeforeSuite    | 1 |
      | BeforeScenario | 1 |
      | BeforeStep     | 3 |
      | AfterStep      | 3 |
      | AfterScenario  | 1 |
      | AfterSuite     | 1 |

  Scenario: triggers appropriate events whole feature
    Given a feature path "features/load.feature"
    When I run feature suite
    Then these events had to be fired for a number of times:
      | BeforeSuite    | 1  |
      | BeforeScenario | 6  |
      | BeforeStep     | 19 |
      | AfterStep      | 19 |
      | AfterScenario  | 6  |
      | AfterSuite     | 1  |

  Scenario: triggers appropriate events for two feature files
    Given a feature path "features/load.feature:6"
    And a feature path "features/multistep.feature:6"
    When I run feature suite
    Then these events had to be fired for a number of times:
      | BeforeSuite    | 1 |
      | BeforeScenario | 2 |
      | BeforeStep     | 7 |
      | AfterStep      | 7 |
      | AfterScenario  | 2 |
      | AfterSuite     | 1 |

  Scenario: should not trigger events on empty feature
    Given a feature "normal.feature" file:
      """
      Feature: empty

        Scenario: one

        Scenario: two
      """
    When I run feature suite
    Then these events had to be fired for a number of times:
      | BeforeSuite    | 1 |
      | BeforeScenario | 0 |
      | BeforeStep     | 0 |
      | AfterStep      | 0 |
      | AfterScenario  | 0 |
      | AfterSuite     | 1 |

  Scenario: should not trigger events on empty scenarios
    Given a feature "normal.feature" file:
      """
      Feature: half empty

        Scenario: one

        Scenario: two
          Then passing step
          And adding step state to context
          And having correct context
          And failing step

        Scenario Outline: three
          Then passing step

          Examples:
            | a |
            | 1 |
      """
    When I run feature suite
    Then these events had to be fired for a number of times:
      | BeforeSuite    | 1 |
      | BeforeScenario | 2 |
      | BeforeStep     | 5 |
      | AfterStep      | 5 |
      | AfterScenario  | 2 |
      | AfterSuite     | 1 |

    And the suite should have failed


  Scenario: should add scenario hook errors to steps
    Given a feature "normal.feature" file:
      """
      Feature: scenario hook errors

        Scenario: failing before and after scenario
          Then adding step state to context
          And passing step

        Scenario: failing before scenario
          Then adding step state to context
          And passing step

        Scenario: failing after scenario
          Then adding step state to context
          And passing step

      """
    When I run feature suite with formatter "pretty"

    Then the suite should have failed
    And the rendered output will be as follows:
    """
      Feature: scenario hook errors

        Scenario: failing before and after scenario # normal.feature:3
          Then adding step state to context         # suite_context_test.go:0 -> InitializeScenario.func17
          after scenario hook failed: failed in after scenario hook, step error: before scenario hook failed: failed in before scenario hook
          And passing step                          # suite_context_test.go:0 -> InitializeScenario.func2

        Scenario: failing before scenario   # normal.feature:7
          Then adding step state to context # suite_context_test.go:0 -> InitializeScenario.func17
          before scenario hook failed: failed in before scenario hook
          And passing step                  # suite_context_test.go:0 -> InitializeScenario.func2

        Scenario: failing after scenario    # normal.feature:11
          Then adding step state to context # suite_context_test.go:0 -> InitializeScenario.func17
          And passing step                  # suite_context_test.go:0 -> InitializeScenario.func2
          after scenario hook failed: failed in after scenario hook

      --- Failed steps:

        Scenario: failing before and after scenario # normal.feature:3
          Then adding step state to context # normal.feature:4
            Error: after scenario hook failed: failed in after scenario hook, step error: before scenario hook failed: failed in before scenario hook

        Scenario: failing before scenario # normal.feature:7
          Then adding step state to context # normal.feature:8
            Error: before scenario hook failed: failed in before scenario hook

        Scenario: failing after scenario # normal.feature:11
          And passing step # normal.feature:13
            Error: after scenario hook failed: failed in after scenario hook


      3 scenarios (3 failed)
      6 steps (1 passed, 3 failed, 2 skipped)
      0s
    """
```

## File: `features/lang.feature`
```
# language: lt
@lang
Savybė: užkrauti savybes
  Kad būtų galima paleisti savybių testus
  Kaip testavimo įrankis
  Aš turiu galėti užregistruoti savybes

  Scenarijus: savybių užkrovimas iš aplanko
    Duota savybių aplankas "features"
    Kai aš išskaitau savybes
    Tada aš turėčiau turėti 14 savybių failus:
      """
      features/background.feature
      features/events.feature
      features/formatter/cucumber.feature
      features/formatter/events.feature
      features/formatter/junit.feature
      features/formatter/pretty.feature
      features/lang.feature
      features/load.feature
      features/multistep.feature
      features/outline.feature
      features/run.feature
      features/snippets.feature
      features/tags.feature
      features/testingt.feature
      """
```

## File: `features/load.feature`
```
Feature: load features
  In order to run features
  As a test suite
  I need to be able to load features

  Scenario: load features within path
    Given a feature path "features"
    When I parse features
    Then I should have 14 feature files:
      """
      features/background.feature
      features/events.feature
      features/formatter/cucumber.feature
      features/formatter/events.feature
      features/formatter/junit.feature
      features/formatter/pretty.feature
      features/lang.feature
      features/load.feature
      features/multistep.feature
      features/outline.feature
      features/run.feature
      features/snippets.feature
      features/tags.feature
      features/testingt.feature
      """

  Scenario: load a specific feature file
    Given a feature path "features/load.feature"
    When I parse features
    Then I should have 1 feature file:
      """
      features/load.feature
      """

  Scenario Outline: loaded feature should have a number of scenarios
    Given a feature path "<feature>"
    When I parse features
    Then I should have <number> scenario registered

    Examples:
      | feature                 | number |
      | features/load.feature:3 | 0      |
      | features/load.feature:6 | 1      |
      | features/load.feature   | 6      |

  Scenario: load a number of feature files
    Given a feature path "features/load.feature"
    And a feature path "features/events.feature"
    When I parse features
    Then I should have 2 feature files:
      """
      features/events.feature
      features/load.feature
      """
```

## File: `features/multistep.feature`
```
Feature: run features with nested steps
  In order to test multisteps
  As a test suite
  I need to be able to execute multisteps

  Scenario: should run passing multistep successfully
    Given a feature "normal.feature" file:
      """
      Feature: normal feature

        Scenario: run passing multistep
          Given passing step
          Then passing multistep
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      passing step
      passing multistep
      """

  Scenario: should fail multistep
    Given a feature "failed.feature" file:
      """
      Feature: failed feature

        Scenario: run failing multistep
          Given passing step
          When failing multistep
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have failed
    And the following step should be failed:
      """
      failing multistep
      """
    And the following steps should be skipped:
      """
      I should have 1 scenario registered
      """
    And the following steps should be passed:
      """
      passing step
      """

  Scenario: should fail nested multistep
    Given a feature "failed.feature" file:
      """
      Feature: failed feature

        Scenario: run failing nested multistep
          Given failing nested multistep
          When passing step
      """
    When I run feature suite
    Then the suite should have failed
    And the following step should be failed:
      """
      failing nested multistep
      """
    And the following steps should be skipped:
      """
      passing step
      """

  Scenario: should skip steps after undefined multistep
    Given a feature "undefined.feature" file:
      """
      Feature: run undefined multistep

        Scenario: run undefined multistep
          Given passing step
          When undefined multistep
          Then passing multistep
      """
    When I run feature suite
    Then the suite should have passed
    And the following step should be passed:
      """
      passing step
      """
    And the following step should be undefined:
      """
      undefined multistep
      """
    And the following step should be skipped:
      """
      passing multistep
      """

  Scenario: should match undefined steps in a row
    Given a feature "undefined.feature" file:
      """
      Feature: undefined feature

        Scenario: parse a scenario
          Given undefined step
          When undefined multistep
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be undefined:
      """
      undefined step
      undefined multistep
      """
    And the following step should be skipped:
      """
      I should have 1 scenario registered
      """

  Scenario: should mark undefined steps after pending
    Given a feature "pending.feature" file:
      """
      Feature: pending feature

        Scenario: parse a scenario
          Given pending step
          When undefined step
          Then undefined multistep
          And I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be undefined:
      """
      undefined step
      undefined multistep
      """
    And the following step should be pending:
      """
      pending step
      """
    And the following step should be skipped:
      """
      I should have 1 scenario registered
      """

  Scenario: context passed between steps
    Given a feature "normal.feature" file:
      """
      Feature: normal feature

        Scenario: run passing multistep
          Given I return a context from a step
          Then I should see the context in the next step
      """
    When I run feature suite
    Then the suite should have passed

  Scenario: context passed between steps
    Given a feature "normal.feature" file:
      """
      Feature: normal feature

      Scenario: run passing multistep
        Given I can see contexts passed in multisteps
      """
    When I run feature suite
    Then the suite should have passed

  Scenario: should run passing multistep using keyword function successfully
    Given a feature "normal.feature" file:
      """
      Feature: normal feature

        Scenario: run passing multistep
          Given passing step
          Then passing multistep using 'then' function
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      passing step
      passing multistep using 'then' function
      """

  Scenario: should identify undefined multistep using keyword function
    Given a feature "normal.feature" file:
      """
      Feature: normal feature

        Scenario: run passing multistep
          Given passing step
          Then undefined multistep using 'then' function
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      passing step
      """
    And the following step should be undefined:
      """
      undefined multistep using 'then' function
      """
```

## File: `features/outline.feature`
```
Feature: run outline
  In order to test application behavior
  As a test suite
  I need to be able to run outline scenarios

  Scenario: should run a normal outline
    Given a feature "normal.feature" file:
      """
      Feature: outline

        Background:
          Given passing step

        Scenario Outline: parse a scenario
          Given a feature path "<path>"
          When I parse features
          Then I should have <num> scenario registered

          Examples:
            | path                    | num |
            | features/load.feature:6 | 1   |
            | features/load.feature:3 | 0   |
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      a passing step
      I parse features
      a feature path "features/load.feature:6"
      a feature path "features/load.feature:3"
      I should have 1 scenario registered
      I should have 0 scenario registered
      """

  Scenario: should continue through examples on failure
    Given a feature "normal.feature" file:
      """
      Feature: outline

        Background:
          Given passing step

        Scenario Outline: parse a scenario
          Given a feature path "<path>"
          When I parse features
          Then I should have <num> scenario registered

          Examples:
            | path                    | num |
            | features/load.feature:6 | 5   |
            | features/load.feature:3 | 0   |
      """
    When I run feature suite
    Then the suite should have failed
    And the following steps should be passed:
      """
      a passing step
      I parse features
      a feature path "features/load.feature:6"
      a feature path "features/load.feature:3"
      I should have 0 scenario registered
      """
    And the following steps should be failed:
      """
      I should have 5 scenario registered
      """

  Scenario: should skip examples on background failure
    Given a feature "normal.feature" file:
      """
      Feature: outline

        Background:
          Given a failing step

        Scenario Outline: parse a scenario
          Given a feature path "<path>"
          When I parse features
          Then I should have <num> scenario registered

          Examples:
            | path                    | num |
            | features/load.feature:6 | 1   |
            | features/load.feature:3 | 0   |
      """
    When I run feature suite
    Then the suite should have failed
    And the following steps should be skipped:
      """
      I parse features
      a feature path "features/load.feature:6"
      a feature path "features/load.feature:3"
      I should have 0 scenario registered
      I should have 1 scenario registered
      """
    And the following steps should be failed:
      """
      a failing step
      """

  Scenario: should translate step table body
    Given a feature "normal.feature" file:
      """
      Feature: outline

        Background:
          Given I'm listening to suite events

        Scenario Outline: run with events
          Given a feature path "<path>"
          When I run feature suite
          Then these events had to be fired for a number of times:
            | BeforeScenario | <scen> |
            | BeforeStep     | <step> |

          Examples:
            | path                    | scen | step |
            | features/load.feature:6 | 1    | 3    |
            | features/load.feature   | 6    | 19   |
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      I'm listening to suite events
      I run feature suite
      a feature path "features/load.feature:6"
      a feature path "features/load.feature"
      """

  Scenario Outline: should translate step doc string argument
    Given a feature "normal.feature" file:
      """
      Feature: scenario events

        Background:
          Given I'm listening to suite events

        Scenario: run with events
          Given a feature path "<path>"
          When I run feature suite
          Then these events had to be fired for a number of times:
            | BeforeScenario | <scen> |
      """
    When I run feature suite
    Then the suite should have passed

    Examples:
      | path                    | scen |
      | features/load.feature:6 | 1    |
      | features/load.feature   | 6    |

```

## File: `features/run.feature`
```
Feature: run features
  In order to test application behavior
  As a test suite
  I need to be able to run features

  Scenario: should run a normal feature
    Given a feature "normal.feature" file:
      """
      Feature: normal feature

        Scenario: parse a scenario
          Given a feature path "features/load.feature:6"
          When I parse features
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      a feature path "features/load.feature:6"
      I parse features
      I should have 1 scenario registered
      """

  Scenario: should skip steps after failure
    Given a feature "failed.feature" file:
      """
      Feature: failed feature

        Scenario: parse a scenario
          Given a failing step
          When I parse features
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have failed
    And the following step should be failed:
      """
      a failing step
      """
    And the following steps should be skipped:
      """
      I parse features
      I should have 1 scenario registered
      """

  Scenario: should skip all scenarios if background fails
    Given a feature "failed.feature" file:
      """
      Feature: failed feature

        Background:
          Given a failing step

        Scenario: parse a scenario
          Given a feature path "features/load.feature:6"
          When I parse features
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have failed
    And the following step should be failed:
      """
      a failing step
      """
    And the following steps should be skipped:
      """
      a feature path "features/load.feature:6"
      I parse features
      I should have 1 scenario registered
      """

  Scenario: should skip steps after undefined
    Given a feature "undefined.feature" file:
      """
      Feature: undefined feature

        Scenario: parse a scenario
          Given a feature path "features/load.feature:6"
          When undefined action
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following step should be passed:
      """
      a feature path "features/load.feature:6"
      """
    And the following step should be undefined:
      """
      undefined action
      """
    And the following step should be skipped:
      """
      I should have 1 scenario registered
      """

  Scenario: should match undefined steps in a row
    Given a feature "undefined.feature" file:
      """
      Feature: undefined feature

        Scenario: parse a scenario
          Given undefined step
          When undefined action
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be undefined:
      """
      undefined step
      undefined action
      """
    And the following step should be skipped:
      """
      I should have 1 scenario registered
      """

  Scenario: should skip steps on pending
    Given a feature "pending.feature" file:
      """
      Feature: pending feature

        Scenario: parse a scenario
          Given undefined step
          When pending step
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following step should be undefined:
      """
      undefined step
      """
    And the following step should be skipped:
      """
      pending step
      I should have 1 scenario registered
      """

  Scenario: should handle pending step
    Given a feature "pending.feature" file:
      """
      Feature: pending feature

        Scenario: parse a scenario
          Given a feature path "features/load.feature:6"
          When pending step
          Then I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following step should be passed:
      """
      a feature path "features/load.feature:6"
      """
    And the following step should be pending:
      """
      pending step
      """
    And the following step should be skipped:
      """
      I should have 1 scenario registered
      """

  Scenario: should mark undefined steps after pending
    Given a feature "pending.feature" file:
      """
      Feature: pending feature

        Scenario: parse a scenario
          Given pending step
          When undefined
          Then undefined 2
          And I should have 1 scenario registered
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be undefined:
      """
      undefined
      undefined 2
      """
    And the following step should be pending:
      """
      pending step
      """
    And the following step should be skipped:
      """
      I should have 1 scenario registered
      """

  Scenario: should fail suite if undefined steps follow after the failure
    Given a feature "failed.feature" file:
      """
      Feature: failed feature

        Scenario: parse a scenario
          Given a failing step
          When an undefined step
          Then another undefined step
      """
    When I run feature suite
    Then the following step should be failed:
      """
      a failing step
      """
    And the following steps should be undefined:
      """
      an undefined step
      another undefined step
      """
    And the suite should have failed

  Scenario: should fail suite and skip pending step after failed step
    Given a feature "failed.feature" file:
      """
      Feature: failed feature

        Scenario: parse a scenario
          Given a failing step
          When pending step
          Then another undefined step
      """
    When I run feature suite
    Then the following step should be failed:
      """
      a failing step
      """
    And the following steps should be skipped:
      """
      pending step
      """
    And the following steps should be undefined:
      """
      another undefined step
      """
    And the suite should have failed

  Scenario: should fail suite and skip next step after failed step
    Given a feature "failed.feature" file:
      """
      Feature: failed feature

        Scenario: parse a scenario
          Given a failing step
          When a failing step
          Then another undefined step
      """
    When I run feature suite
    Then the following step should be failed:
      """
      a failing step
      """
    And the following steps should be skipped:
      """
      a failing step
      """
    And the following steps should be undefined:
      """
      another undefined step
      """
    And the suite should have failed

  Scenario: should be able to convert a Doc String to a `*godog.DocString` argument
    Given call func(*godog.DocString) with:
    """
    text
    """

  Scenario: should be able to convert a Doc String to a `string` argument
    Given call func(string) with:
    """
    text
    """

```

## File: `features/snippets.feature`
```
Feature: undefined step snippets
  In order to implement step definitions faster
  As a test suite user
  I need to be able to get undefined step snippets

  Scenario: should generate snippets
    Given a feature "undefined.feature" file:
      """
      Feature: undefined steps

        Scenario: get version number from api
          When I send "GET" request to "/version"
          Then the response code should be 200
      """
    When I run feature suite
    Then the following steps should be undefined:
      """
      I send "GET" request to "/version"
      the response code should be 200
      """
    And the undefined step snippets should be:
      """
      func iSendRequestTo(arg1, arg2 string) error {
              return godog.ErrPending
      }

      func theResponseCodeShouldBe(arg1 int) error {
              return godog.ErrPending
      }

      func InitializeScenario(ctx *godog.ScenarioContext) {
              ctx.Step(`^I send "([^"]*)" request to "([^"]*)"$`, iSendRequestTo)
              ctx.Step(`^the response code should be (\d+)$`, theResponseCodeShouldBe)
      }
      """

  Scenario: should generate snippets with more arguments
    Given a feature "undefined.feature" file:
      """
      Feature: undefined steps

        Scenario: get version number from api
          When I send "GET" request to "/version" with:
            | col1 | val1 |
            | col2 | val2 |
          Then the response code should be 200 and header "X-Powered-By" should be "godog"
          And the response body should be:
          \"\"\"
          Hello World
          \"\"\"
      """
    When I run feature suite
    Then the undefined step snippets should be:
      """
      func iSendRequestToWith(arg1, arg2 string, arg3 *godog.Table) error {
              return godog.ErrPending
      }

      func theResponseBodyShouldBe(arg1 *godog.DocString) error {
              return godog.ErrPending
      }

      func theResponseCodeShouldBeAndHeaderShouldBe(arg1 int, arg2, arg3 string) error {
              return godog.ErrPending
      }

      func InitializeScenario(ctx *godog.ScenarioContext) {
              ctx.Step(`^I send "([^"]*)" request to "([^"]*)" with:$`, iSendRequestToWith)
              ctx.Step(`^the response body should be:$`, theResponseBodyShouldBe)
              ctx.Step(`^the response code should be (\d+) and header "([^"]*)" should be "([^"]*)"$`, theResponseCodeShouldBeAndHeaderShouldBe)
      }
      """

  Scenario: should handle escaped symbols
    Given a feature "undefined.feature" file:
      """
      Feature: undefined steps

        Scenario: get version number from api
          When I pull from github.com
          Then the project should be there
      """
    When I run feature suite
    Then the following steps should be undefined:
      """
      I pull from github.com
      the project should be there
      """
    And the undefined step snippets should be:
      """
      func iPullFromGithubcom() error {
              return godog.ErrPending
      }

      func theProjectShouldBeThere() error {
              return godog.ErrPending
      }

      func InitializeScenario(ctx *godog.ScenarioContext) {
              ctx.Step(`^I pull from github\.com$`, iPullFromGithubcom)
              ctx.Step(`^the project should be there$`, theProjectShouldBeThere)
      }
      """

  Scenario: should handle string argument followed by comma
    Given a feature "undefined.feature" file:
      """
      Feature: undefined

        Scenario: add item to basket
          Given there is a "Sith Lord Lightsaber", which costs £5
          When I add the "Sith Lord Lightsaber" to the basket
      """
    When I run feature suite
    And the undefined step snippets should be:
      """
      func iAddTheToTheBasket(arg1 string) error {
              return godog.ErrPending
      }

      func thereIsAWhichCosts(arg1 string, arg2 int) error {
              return godog.ErrPending
      }

      func InitializeScenario(ctx *godog.ScenarioContext) {
              ctx.Step(`^I add the "([^"]*)" to the basket$`, iAddTheToTheBasket)
              ctx.Step(`^there is a "([^"]*)", which costs £(\d+)$`, thereIsAWhichCosts)
      }
      """

  Scenario: should handle arguments in the beggining or end of the step
    Given a feature "undefined.feature" file:
      """
      Feature: undefined

        Scenario: add item to basket
          Given "Sith Lord Lightsaber", which costs £5
          And 12 godogs
      """
    When I run feature suite
    And the undefined step snippets should be:
      """
      func godogs(arg1 int) error {
              return godog.ErrPending
      }

      func whichCosts(arg1 string, arg2 int) error {
              return godog.ErrPending
      }

      func InitializeScenario(ctx *godog.ScenarioContext) {
              ctx.Step(`^(\d+) godogs$`, godogs)
              ctx.Step(`^"([^"]*)", which costs £(\d+)$`, whichCosts)
      }
      """
```

## File: `features/tags.feature`
```
Feature: tag filters
  In order to test application behavior
  As a test suite
  I need to be able to filter features and scenarios by tags

  Scenario: should filter outline examples by tags
    Given a feature "normal.feature" file:
      """
      Feature: outline

        Background:
          Given passing step
          And passing step without return

        Scenario Outline: parse a scenario
          Given a feature path "<path>"
          When I parse features
          Then I should have <num> scenario registered

          Examples:
            | path                    | num |
            | features/load.feature:3 | 0   |

          @used
          Examples:
            | path                    | num |
            | features/load.feature:6 | 1   |
      """
    When I run feature suite with tags "@used"
    Then the suite should have passed
    And the following steps should be passed:
      """
      I parse features
      a feature path "features/load.feature:6"
      I should have 1 scenario registered
      """
    And I should have 1 scenario registered

  Scenario: should filter scenarios by X tag
    Given a feature "normal.feature" file:
      """
      Feature: tagged

        @x
        Scenario: one
          Given a feature path "one"

        @x
        Scenario: two
          Given a feature path "two"

        @x @y
        Scenario: three
          Given a feature path "three"

        @y
        Scenario: four
          Given a feature path "four"
      """
    When I run feature suite with tags "@x"
    Then the suite should have passed
    And I should have 3 scenario registered
    And the following steps should be passed:
      """
      a feature path "one"
      a feature path "two"
      a feature path "three"
      """

  Scenario: should filter scenarios by X tag not having Y
    Given a feature "normal.feature" file:
      """
      Feature: tagged

        @x
        Scenario: one
          Given a feature path "one"

        @x
        Scenario: two
          Given a feature path "two"

        @x @y
        Scenario: three
          Given a feature path "three"

        @y @z
        Scenario: four
          Given a feature path "four"
      """
    When I run feature suite with tags "@x && ~@y"
    Then the suite should have passed
    And I should have 2 scenario registered
    And the following steps should be passed:
      """
      a feature path "one"
      a feature path "two"
      """

  Scenario: should filter scenarios having Y and Z tags
    Given a feature "normal.feature" file:
      """
      Feature: tagged

        @x
        Scenario: one
          Given a feature path "one"

        @x
        Scenario: two
          Given a feature path "two"

        @x @y
        Scenario: three
          Given a feature path "three"

        @y @z
        Scenario: four
          Given a feature path "four"
      """
    When I run feature suite with tags "@y && @z"
    Then the suite should have passed
    And I should have 1 scenario registered
    And the following steps should be passed:
      """
      a feature path "four"
      """
```

## File: `features/testingt.feature`
```
Feature: providing testingT compatibility
  In order to test application behavior using standard go assertion techniques
  As a test suite
  I need to be able to provide a testing.T compatible interface

  Scenario Outline: should fail test with no message if <op> called on testing T
    Given a feature "failed.feature" file:
      """
      Feature: failed feature

        Scenario: fail a scenario
          Given passing step
          When my step fails the test by calling <op> on testing T
      """
    When I run feature suite
    Then the suite should have failed
    And the following steps should be passed:
      """
      passing step
      """
    And the following step should be failed:
      """
      my step fails the test by calling <op> on testing T
      """
    Examples:
      | op      |
      | Fail    |
      | FailNow |

  Scenario Outline: should fail test with message if <op> called on T
    Given a feature "failed.feature" file:
      """
      Feature: failed feature

        Scenario: fail a scenario
          Given passing step
          When my step fails the test by calling <op> on testing T with message "an unformatted message"
      """
    When I run feature suite
    Then the suite should have failed
    And the following steps should be passed:
      """
      passing step
      """
    And the following step should be failed:
      """
      my step fails the test by calling <op> on testing T with message "an unformatted message"
      """
    Examples:
      | op    |
      | Error |
      | Fatal |


  Scenario Outline: should fail test with formatted message if <op> called on T
    Given a feature "failed.feature" file:
      """
      Feature: failed feature

        Scenario: fail a scenario
          Given passing step
          When my step fails the test by calling <op> on testing T with message "a formatted message %s" and argument "arg1"
      """
    When I run feature suite
    Then the suite should have failed
    And the following steps should be passed:
      """
      passing step
      """
    And the following step should be failed:
      """
      my step fails the test by calling <op> on testing T with message "a formatted message %s" and argument "arg1"
      """
    Examples:
      | op     |
      | Errorf |
      | Fatalf |

  Scenario: should pass test when testify assertions pass
    Given a feature "testify.feature" file:
      """
      Feature: passed feature

        Scenario: pass a scenario
          Given passing step
          When my step calls testify's assert.Equal with expected "exp" and actual "exp"
          When my step calls testify's require.Equal with expected "exp" and actual "exp"
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      passing step
      my step calls testify's assert.Equal with expected "exp" and actual "exp"
      my step calls testify's require.Equal with expected "exp" and actual "exp"
      """

  Scenario: should fail test when testify assertions do not pass
    Given a feature "testify.feature" file:
      """
      Feature: failed feature

        Scenario: fail a scenario
          Given passing step
          When my step calls testify's assert.Equal with expected "exp" and actual "not"
          And my step calls testify's assert.Equal with expected "exp2" and actual "not"
      """
    When I run feature suite
    Then the suite should have failed
    And the following steps should be passed:
      """
      passing step
      """
    And the following steps should be failed:
      """
      my step calls testify's assert.Equal with expected "exp" and actual "not"
      """
    And the following steps should be skipped:
      """
      my step calls testify's assert.Equal with expected "exp2" and actual "not"
      """

  Scenario: should fail test when multiple testify assertions are used in a step
    Given a feature "testify.feature" file:
      """
      Feature: failed feature

        Scenario: fail a scenario
          Given passing step
          When my step calls testify's assert.Equal 3 times
      """
    When I run feature suite
    Then the suite should have failed
    And the following steps should be passed:
      """
      passing step
      """
    And the following steps should be failed:
      """
      my step calls testify's assert.Equal 3 times
      """

  Scenario: should pass test when multiple testify assertions are used successfully in a step
    Given a feature "testify.feature" file:
      """
      Feature: passed feature

        Scenario: pass a scenario
          Given passing step
          When my step calls testify's assert.Equal 3 times with match
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      passing step
      my step calls testify's assert.Equal 3 times with match
      """

  Scenario Outline: should skip test when <op> is called on the testing.T
    Given a feature "testify.feature" file:
      """
      Feature: skipped feature

        Scenario: skip a scenario
          Given passing step
          When my step skips the test by calling <op> on testing T
      """
    When I run feature suite
    Then the suite should have passed
    And the following steps should be passed:
      """
      passing step
      """
    And the following steps should be skipped:
      """
      my step skips the test by calling <op> on testing T
      """
    Examples:
      | op      |
      | Skip    |
      | SkipNow |

  Scenario: should log when Logf/Log called on testing.T
    When my step calls Logf on testing T with message "format this %s" and argument "formatparam1"
    And my step calls Log on testing T with message "log this message"
    Then the logged messages should include "format this formatparam1"
    And the logged messages should include "log this message"

  Scenario: should log when godog.Logf/Log called
    When my step calls godog.Logf with message "format this %s" and argument "formatparam1"
    And my step calls godog.Log with message "log this message"
    Then the logged messages should include "format this formatparam1"
    And the logged messages should include "log this message"
```

## File: `features/formatter/cucumber.feature`
```
Feature: cucumber json formatter
  In order to support tools that import cucumber json output
  I need to be able to support cucumber json formatted output

  Scenario: Support of Feature Plus Scenario Node
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
            simple feature description
        Scenario: simple scenario
            simple scenario description
    """
    When I run feature suite with formatter "cucumber"
    Then the rendered json will be as follows:
      """ application/json
        [
          {
            "uri": "features/simple.feature",
            "id": "simple-feature",
            "keyword": "Feature",
            "name": "simple feature",
            "description": "        simple feature description",
            "line": 1,
            "elements": [
              {
                "id": "simple-feature;simple-scenario",
                "keyword": "Scenario",
                "name": "simple scenario",
                "description": "        simple scenario description",
                "line": 3,
                "type": "scenario"
              }
            ]
          }
        ]
      """

  Scenario: Support of Feature Plus Scenario Node With Tags
    Given a feature "features/simple.feature" file:
    """
        @TAG1
        Feature: simple feature
            simple feature description
        @TAG2 @TAG3
        Scenario: simple scenario
            simple scenario description
    """
    When I run feature suite with formatter "cucumber"
    Then the rendered json will be as follows:
      """ application/json
        [
          {
            "uri": "features/simple.feature",
            "id": "simple-feature",
            "keyword": "Feature",
            "name": "simple feature",
            "description": "        simple feature description",
            "line": 2,
            "tags": [
              {
                "name": "@TAG1",
                "line": 1
              }
            ],
            "elements": [
              {
                "id": "simple-feature;simple-scenario",
                "keyword": "Scenario",
                "name": "simple scenario",
                "description": "        simple scenario description",
                "line": 5,
                "type": "scenario",
                "tags": [
                  {
                    "name": "@TAG1",
                    "line": 1
                  },
                  {
                    "name": "@TAG2",
                    "line": 4
                  },
                  {
                    "name": "@TAG3",
                    "line": 4
                  }
                ]
              }
            ]
          }
      ]
      """
  Scenario: Support of Feature Plus Scenario Outline
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
            simple feature description

        Scenario Outline: simple scenario
            simple scenario description

        Examples: simple examples
        | status |
        | pass   |
        | fail   |
    """
    When I run feature suite with formatter "cucumber"
    Then the rendered json will be as follows:
    """
      [
        {
          "uri": "features/simple.feature",
          "id": "simple-feature",
          "keyword": "Feature",
          "name": "simple feature",
          "description": "        simple feature description",
          "line": 1,
          "elements": [
            {
              "id": "simple-feature;simple-scenario;simple-examples;2",
              "keyword": "Scenario Outline",
              "name": "simple scenario",
              "description": "        simple scenario description",
              "line": 9,
              "type": "scenario"
            },
            {
              "id": "simple-feature;simple-scenario;simple-examples;3",
              "keyword": "Scenario Outline",
              "name": "simple scenario",
              "description": "        simple scenario description",
              "line": 10,
              "type": "scenario"
            }
          ]
        }
      ]
    """

  Scenario: Support of Feature Plus Scenario Outline With Tags
    Given a feature "features/simple.feature" file:
    """
        @TAG1
        Feature: simple feature
            simple feature description

        @TAG2
        Scenario Outline: simple scenario
            simple scenario description

        @TAG3
        Examples: simple examples
        | status |
        | pass   |
        | fail   |
    """
    When I run feature suite with formatter "cucumber"
    Then the rendered json will be as follows:
    """
        [
          {
            "uri": "features/simple.feature",
            "id": "simple-feature",
            "keyword": "Feature",
            "name": "simple feature",
            "description": "        simple feature description",
            "line": 2,
            "tags": [
              {
                "name": "@TAG1",
                "line": 1
              }
            ],
            "elements": [
              {
                "id": "simple-feature;simple-scenario;simple-examples;2",
                "keyword": "Scenario Outline",
                "name": "simple scenario",
                "description": "        simple scenario description",
                "line": 12,
                "type": "scenario",
                "tags": [
                  {
                    "name": "@TAG1",
                    "line": 1
                  },
                  {
                    "name": "@TAG2",
                    "line": 5
                  },
                  {
                    "name": "@TAG3",
                    "line": 9
                  }
                ]
              },
              {
                "id": "simple-feature;simple-scenario;simple-examples;3",
                "keyword": "Scenario Outline",
                "name": "simple scenario",
                "description": "        simple scenario description",
                "line": 13,
                "type": "scenario",
                "tags": [
                  {
                    "name": "@TAG1",
                    "line": 1
                  },
                  {
                    "name": "@TAG2",
                    "line": 5
                  },
                  {
                    "name": "@TAG3",
                    "line": 9
                  }
                ]
              }
            ]
          }
        ]
    """
  Scenario: Support of Feature Plus Scenario With Steps
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
            simple feature description

        Scenario: simple scenario
            simple scenario description

        Given passing step
        Then a failing step

    """
    When I run feature suite with formatter "cucumber"
    Then the rendered json will be as follows:
    """
      [
        {
          "uri": "features/simple.feature",
          "id": "simple-feature",
          "keyword": "Feature",
          "name": "simple feature",
          "description": "        simple feature description",
          "line": 1,
          "elements": [
            {
              "id": "simple-feature;simple-scenario",
              "keyword": "Scenario",
              "name": "simple scenario",
              "description": "        simple scenario description",
              "line": 4,
              "type": "scenario",
              "steps": [
                {
                  "keyword": "Given ",
                  "name": "passing step",
                  "line": 7,
                  "match": {
                    "location": "suite_context.go:64"
                  },
                  "result": {
                    "status": "passed",
                    "duration": 0
                  }
                },
                {
                  "keyword": "Then ",
                  "name": "a failing step",
                  "line": 8,
                  "match": {
                    "location": "suite_context.go:47"
                  },
                  "result": {
                    "status": "failed",
                    "error_message": "intentional failure",
                    "duration": 0
                  }
                }
              ]
            }
          ]
        }
      ]
    """
  Scenario: Support of Feature Plus Scenario Outline With Steps
    Given a feature "features/simple.feature" file:
    """
      Feature: simple feature
        simple feature description

        Scenario Outline: simple scenario
        simple scenario description

          Given <status> step

        Examples: simple examples
        | status |
        | passing |
        | failing |

    """
    When I run feature suite with formatter "cucumber"
    Then the rendered json will be as follows:
    """
      [
        {
          "uri": "features/simple.feature",
          "id": "simple-feature",
          "keyword": "Feature",
          "name": "simple feature",
          "description": "    simple feature description",
          "line": 1,
          "elements": [
            {
              "id": "simple-feature;simple-scenario;simple-examples;2",
              "keyword": "Scenario Outline",
              "name": "simple scenario",
              "description": "    simple scenario description",
              "line": 11,
              "type": "scenario",
              "steps": [
                {
                  "keyword": "Given ",
                  "name": "passing step",
                  "line": 7,
                  "match": {
                    "location": "suite_context.go:64"
                  },
                  "result": {
                    "status": "passed",
                    "duration": 0
                  }
                }
              ]
            },
            {
              "id": "simple-feature;simple-scenario;simple-examples;3",
              "keyword": "Scenario Outline",
              "name": "simple scenario",
              "description": "    simple scenario description",
              "line": 12,
              "type": "scenario",
              "steps": [
                {
                  "keyword": "Given ",
                  "name": "failing step",
                  "line": 7,
                  "match": {
                    "location": "suite_context.go:47"
                  },
                  "result": {
                    "status": "failed",
                    "error_message": "intentional failure",
                    "duration": 0
                  }
                }
              ]
            }
          ]
        }
      ]
    """

  # Currently godog only supports comments on Feature and not
  # scenario and steps.
  Scenario: Support of Comments
    Given a feature "features/simple.feature" file:
    """
        #Feature comment
        Feature: simple feature
          simple description

          Scenario: simple scenario
          simple feature description
    """
    When I run feature suite with formatter "cucumber"
    Then the rendered json will be as follows:
    """
        [
          {
            "uri": "features/simple.feature",
            "id": "simple-feature",
            "keyword": "Feature",
            "name": "simple feature",
            "description": "      simple description",
            "line": 2,
            "comments": [
              {
                "value": "#Feature comment",
                "line": 1
              }
            ],
            "elements": [
              {
                "id": "simple-feature;simple-scenario",
                "keyword": "Scenario",
                "name": "simple scenario",
                "description": "      simple feature description",
                "line": 5,
                "type": "scenario"
              }
            ]
          }
        ]
    """
  Scenario: Support of Docstrings
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
          simple description

          Scenario: simple scenario
          simple feature description

          Given passing step
          \"\"\" content type
          step doc string
          \"\"\"
    """
    When I run feature suite with formatter "cucumber"
    Then the rendered json will be as follows:
    """
        [
      {
        "uri": "features/simple.feature",
        "id": "simple-feature",
        "keyword": "Feature",
        "name": "simple feature",
        "description": "      simple description",
        "line": 1,
        "elements": [
          {
            "id": "simple-feature;simple-scenario",
            "keyword": "Scenario",
            "name": "simple scenario",
            "description": "      simple feature description",
            "line": 4,
            "type": "scenario",
            "steps": [
              {
                "keyword": "Given ",
                "name": "passing step",
                "line": 7,
                "doc_string": {
                  "value": "step doc string",
                  "content_type": "content type",
                  "line": 8
                },
                "match": {
                  "location": "suite_context.go:64"
                },
                "result": {
                  "status": "passed",
                  "duration": 0
                }
              }
            ]
          }
        ]
      }
    ]
    """
  Scenario: Support of Undefined, Pending and Skipped status
    Given a feature "features/simple.feature" file:
    """
      Feature: simple feature
      simple feature description

      Scenario: simple scenario
      simple scenario description

        Given passing step
        And pending step
        And undefined
        And passing step

    """
    When I run feature suite with formatter "cucumber"
    Then the rendered json will be as follows:
    """
      [
        {
          "uri": "features/simple.feature",
          "id": "simple-feature",
          "keyword": "Feature",
          "name": "simple feature",
          "description": "  simple feature description",
          "line": 1,
          "elements": [
            {
              "id": "simple-feature;simple-scenario",
              "keyword": "Scenario",
              "name": "simple scenario",
              "description": "  simple scenario description",
              "line": 4,
              "type": "scenario",
              "steps": [
                {
                  "keyword": "Given ",
                  "name": "passing step",
                  "line": 7,
                  "match": {
                    "location": "suite_context.go:64"
                  },
                  "result": {
                    "status": "passed",
                    "duration": 0
                  }
                },
                {
                  "keyword": "And ",
                  "name": "pending step",
                  "line": 8,
                  "match": {
                    "location": "features/simple.feature:8"
                  },
                  "result": {
                    "status": "pending"
                  }
                },
                {
                  "keyword": "And ",
                  "name": "undefined",
                  "line": 9,
                  "match": {
                    "location": "features/simple.feature:9"
                  },
                  "result": {
                    "status": "undefined"
                  }
                },
                {
                  "keyword": "And ",
                  "name": "passing step",
                  "line": 10,
                  "match": {
                    "location": "suite_context.go:64"
                  },
                  "result": {
                    "status": "skipped"
                  }
                }
              ]
            }
          ]
        }
      ]
    """


```

## File: `features/formatter/events.feature`
```
Feature: event stream formatter
  In order to have universal cucumber formatter
  As a test suite
  I need to be able to support event stream formatter

  Scenario: should fire only suite events without any scenario
    Given a feature path "features/load.feature:4"
    When I run feature suite with formatter "events"
    Then the following events should be fired:
      """
        TestRunStarted
        TestRunFinished
      """

  Scenario: should process simple scenario
    Given a feature path "features/load.feature:27"
    When I run feature suite with formatter "events"
    Then the following events should be fired:
      """
        TestRunStarted
        TestSource
        TestCaseStarted
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        TestCaseFinished
        TestRunFinished
      """

  Scenario: should process outline scenario
    Given a feature path "features/load.feature:35"
    When I run feature suite with formatter "events"
    Then the following events should be fired:
      """
        TestRunStarted
        TestSource
        TestCaseStarted
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        TestCaseFinished
        TestCaseStarted
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        TestCaseFinished
        TestCaseStarted
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        StepDefinitionFound
        TestStepStarted
        TestStepFinished
        TestCaseFinished
        TestRunFinished
      """
```

## File: `features/formatter/junit.feature`
```
Feature: JUnit XML formatter
  In order to support tools that import JUnit XML output
  I need to be able to support junit formatted output

  Scenario: Support of Feature Plus Scenario Node
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
            simple feature description
        Scenario: simple scenario
            simple scenario description
    """
    When I run feature suite with formatter "junit"
    Then the rendered xml will be as follows:
    """ application/xml
      <?xml version="1.0" encoding="UTF-8"?>
      <testsuites name="godog" tests="1" skipped="0" failures="0" errors="0" time="0">
        <testsuite name="simple feature" tests="1" skipped="0" failures="0" errors="0" time="0">
          <testcase name="simple scenario" status="" time="0"></testcase>
        </testsuite>
      </testsuites>
    """

  Scenario: Support of Feature Plus Scenario Node With Tags
    Given a feature "features/simple.feature" file:
    """
        @TAG1
        Feature: simple feature
            simple feature description
        @TAG2 @TAG3
        Scenario: simple scenario
            simple scenario description
    """
    When I run feature suite with formatter "junit"
    Then the rendered xml will be as follows:
    """ application/xml
      <?xml version="1.0" encoding="UTF-8"?>
      <testsuites name="godog" tests="1" skipped="0" failures="0" errors="0" time="0">
        <testsuite name="simple feature" tests="1" skipped="0" failures="0" errors="0" time="0">
          <testcase name="simple scenario" status="" time="0"></testcase>
        </testsuite>
      </testsuites>
    """
  Scenario: Support of Feature Plus Scenario Outline
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
            simple feature description

        Scenario Outline: simple scenario
            simple scenario description

        Examples: simple examples
        | status |
        | pass   |
        | fail   |
    """
    When I run feature suite with formatter "junit"
    Then the rendered xml will be as follows:
    """ application/xml
      <?xml version="1.0" encoding="UTF-8"?>
      <testsuites name="godog" tests="2" skipped="0" failures="0" errors="0" time="0">
        <testsuite name="simple feature" tests="2" skipped="0" failures="0" errors="0" time="0">
          <testcase name="simple scenario #1" status="" time="0"></testcase>
          <testcase name="simple scenario #2" status="" time="0"></testcase>
        </testsuite>
      </testsuites>
    """

  Scenario: Support of Feature Plus Scenario Outline With Tags
    Given a feature "features/simple.feature" file:
    """
        @TAG1
        Feature: simple feature
            simple feature description

        @TAG2
        Scenario Outline: simple scenario
            simple scenario description

        @TAG3
        Examples: simple examples
        | status |
        | pass   |
        | fail   |
    """
    When I run feature suite with formatter "junit"
    Then the rendered xml will be as follows:
    """ application/xml
      <?xml version="1.0" encoding="UTF-8"?>
      <testsuites name="godog" tests="2" skipped="0" failures="0" errors="0" time="0">
        <testsuite name="simple feature" tests="2" skipped="0" failures="0" errors="0" time="0">
          <testcase name="simple scenario #1" status="" time="0"></testcase>
          <testcase name="simple scenario #2" status="" time="0"></testcase>
        </testsuite>
      </testsuites>
    """
  Scenario: Support of Feature Plus Scenario With Steps
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
            simple feature description

        Scenario: simple scenario
            simple scenario description

        Given passing step
        Then a failing step

    """
    When I run feature suite with formatter "junit"
    Then the rendered xml will be as follows:
    """ application/xml
      <?xml version="1.0" encoding="UTF-8"?>
      <testsuites name="godog" tests="1" skipped="0" failures="1" errors="0" time="0">
        <testsuite name="simple feature" tests="1" skipped="0" failures="1" errors="0" time="0">
          <testcase name="simple scenario" status="failed" time="0">
            <failure message="Step a failing step: intentional failure"></failure>
          </testcase>
        </testsuite>
      </testsuites>
    """
  Scenario: Support of Feature Plus Scenario Outline With Steps
    Given a feature "features/simple.feature" file:
    """
      Feature: simple feature
        simple feature description

        Scenario Outline: simple scenario
        simple scenario description

          Given <status> step

        Examples: simple examples
        | status |
        | passing |
        | failing |

    """
    When I run feature suite with formatter "junit"
    Then the rendered xml will be as follows:
    """ application/xml
      <?xml version="1.0" encoding="UTF-8"?>
      <testsuites name="godog" tests="2" skipped="0" failures="1" errors="0" time="0">
        <testsuite name="simple feature" tests="2" skipped="0" failures="1" errors="0" time="0">
          <testcase name="simple scenario #1" status="passed" time="0"></testcase>
          <testcase name="simple scenario #2" status="failed" time="0">
            <failure message="Step failing step: intentional failure"></failure>
          </testcase>
        </testsuite>
      </testsuites>
    """

  # Currently godog only supports comments on Feature and not
  # scenario and steps.
  Scenario: Support of Comments
    Given a feature "features/simple.feature" file:
    """
        #Feature comment
        Feature: simple feature
          simple description

          Scenario: simple scenario
          simple feature description
    """
    When I run feature suite with formatter "junit"
    Then the rendered xml will be as follows:
    """ application/xml
      <?xml version="1.0" encoding="UTF-8"?>
      <testsuites name="godog" tests="1" skipped="0" failures="0" errors="0" time="0">
        <testsuite name="simple feature" tests="1" skipped="0" failures="0" errors="0" time="0">
          <testcase name="simple scenario" status="" time="0"></testcase>
        </testsuite>
      </testsuites>
    """
  Scenario: Support of Docstrings
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
          simple description

          Scenario: simple scenario
          simple feature description

          Given passing step
          \"\"\" content type
          step doc string
          \"\"\"
    """
    When I run feature suite with formatter "junit"
    Then the rendered xml will be as follows:
    """ application/xml
      <?xml version="1.0" encoding="UTF-8"?>
      <testsuites name="godog" tests="1" skipped="0" failures="0" errors="0" time="0">
        <testsuite name="simple feature" tests="1" skipped="0" failures="0" errors="0" time="0">
          <testcase name="simple scenario" status="passed" time="0"></testcase>
        </testsuite>
      </testsuites>
    """
  Scenario: Support of Undefined, Pending and Skipped status
    Given a feature "features/simple.feature" file:
    """
      Feature: simple feature
      simple feature description

      Scenario: simple scenario
      simple scenario description

        Given passing step
        And pending step
        And undefined
        And passing step

    """
    When I run feature suite with formatter "junit"
    Then the rendered xml will be as follows:
    """ application/xml
      <?xml version="1.0" encoding="UTF-8"?>
      <testsuites name="godog" tests="1" skipped="0" failures="0" errors="1" time="0">
        <testsuite name="simple feature" tests="1" skipped="0" failures="0" errors="1" time="0">
          <testcase name="simple scenario" status="undefined" time="0">
            <error message="Step pending step: TODO: write pending definition" type="pending"></error>
            <error message="Step undefined" type="undefined"></error>
            <error message="Step passing step" type="skipped"></error>
          </testcase>
        </testsuite>
      </testsuites>
    """
```

## File: `features/formatter/pretty.feature`
```
Feature: pretty formatter
  In order to support tools that import pretty output
  I need to be able to support pretty formatted output

  Scenario: Support of Feature Plus Scenario Node
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
            simple feature description
        Scenario: simple scenario
            simple scenario description
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature
        simple feature description

        Scenario: simple scenario # features/simple.feature:3

      1 scenarios (1 undefined)
      No steps
      0s
    """

  Scenario: Support of Feature Plus Scenario Node With Tags
    Given a feature "features/simple.feature" file:
    """
        @TAG1
        Feature: simple feature
            simple feature description
        @TAG2 @TAG3
        Scenario: simple scenario
            simple scenario description
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature
        simple feature description

        Scenario: simple scenario # features/simple.feature:5

      1 scenarios (1 undefined)
      No steps
      0s
    """

  Scenario: Support of Feature Plus Scenario Outline
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
            simple feature description

        Scenario Outline: simple scenario
            simple scenario description

        Examples: simple examples
        | status |
        | pass   |
        | fail   |
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature
        simple feature description

        Scenario Outline: simple scenario # features/simple.feature:4

          Examples: simple examples
            | status |
            | pass   |
            | fail   |

      2 scenarios (2 undefined)
      No steps
      0s
    """

  Scenario: Support of Feature Plus Scenario Outline With Tags
    Given a feature "features/simple.feature" file:
    """
        @TAG1
        Feature: simple feature
            simple feature description

        @TAG2
        Scenario Outline: simple scenario
            simple scenario description

        @TAG3
        Examples: simple examples
        | status |
        | pass   |
        | fail   |
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature
        simple feature description

        Scenario Outline: simple scenario # features/simple.feature:6

          Examples: simple examples
            | status |
            | pass   |
            | fail   |

      2 scenarios (2 undefined)
      No steps
      0s
    """

  Scenario: Support of Feature Plus Scenario With Steps
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
            simple feature description

        Scenario: simple scenario
            simple scenario description

        Given passing step
        Then a failing step

    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature
        simple feature description

        Scenario: simple scenario # features/simple.feature:4
          Given passing step      # suite_context.go:0 -> SuiteContext.func2
          Then a failing step     # suite_context.go:0 -> *suiteContext
          intentional failure

      --- Failed steps:

        Scenario: simple scenario # features/simple.feature:4
          Then a failing step # features/simple.feature:8
            Error: intentional failure


      1 scenarios (1 failed)
      2 steps (1 passed, 1 failed)
      0s
    """

  Scenario: Support of Feature Plus Scenario Outline With Steps
    Given a feature "features/simple.feature" file:
    """
      Feature: simple feature
        simple feature description

        Scenario Outline: simple scenario
        simple scenario description

          Given <status> step

        Examples: simple examples
        | status |
        | passing |
        | failing |

    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature
        simple feature description

        Scenario Outline: simple scenario # features/simple.feature:4
          Given <status> step             # suite_context.go:0 -> SuiteContext.func2

          Examples: simple examples
            | status  |
            | passing |
            | failing |
              intentional failure

      --- Failed steps:

        Scenario Outline: simple scenario # features/simple.feature:4
          Given failing step # features/simple.feature:7
            Error: intentional failure


      2 scenarios (1 passed, 1 failed)
      2 steps (1 passed, 1 failed)
      0s
    """

  # Currently godog only supports comments on Feature and not
  # scenario and steps.
  Scenario: Support of Comments
    Given a feature "features/simple.feature" file:
    """
        #Feature comment
        Feature: simple feature
          simple description

          Scenario: simple scenario
          simple feature description
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature
        simple description

        Scenario: simple scenario # features/simple.feature:5

      1 scenarios (1 undefined)
      No steps
      0s
    """

  Scenario: Support of Docstrings
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature
          simple description

          Scenario: simple scenario
          simple feature description

          Given passing step
          \"\"\" content type
          step doc string
          \"\"\"
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature
        simple description

        Scenario: simple scenario # features/simple.feature:4
          Given passing step      # suite_context.go:0 -> SuiteContext.func2
            \"\"\"  content type
            step doc string
            \"\"\"

      1 scenarios (1 passed)
      1 steps (1 passed)
      0s
    """

  Scenario: Support of Undefined, Pending and Skipped status
    Given a feature "features/simple.feature" file:
    """
      Feature: simple feature
      simple feature description

      Scenario: simple scenario
      simple scenario description

        Given passing step
        And pending step
        And undefined doc string
        \"\"\"
        abc
        \"\"\"
        And undefined table
        | a | b | c |
        | 1 | 2 | 3 |
        And passing step

    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature
        simple feature description

        Scenario: simple scenario  # features/simple.feature:4
          Given passing step       # suite_context.go:0 -> SuiteContext.func2
          And pending step         # suite_context.go:0 -> SuiteContext.func1
            TODO: write pending definition
          And undefined doc string
          \"\"\"
          abc
          \"\"\"
          And undefined table
          | a | b | c |
          | 1 | 2 | 3 |
          And passing step         # suite_context.go:0 -> SuiteContext.func2

      1 scenarios (1 pending, 1 undefined)
      5 steps (1 passed, 1 pending, 2 undefined, 1 skipped)
      0s

      You can implement step definitions for undefined steps with these snippets:

      func undefinedDocString(arg1 *godog.DocString) error {
        return godog.ErrPending
      }

      func undefinedTable(arg1 *godog.Table) error {
        return godog.ErrPending
      }

      func InitializeScenario(ctx *godog.ScenarioContext) {
        ctx.Step(`^undefined doc string$`, undefinedDocString)
        ctx.Step(`^undefined table$`, undefinedTable)
      }
    """

  # Ensure s will not break when injecting data from BeforeStep
  Scenario: Support data injection in BeforeStep
    Given a feature "features/inject.feature" file:
    """
      Feature: inject long value

      Scenario: test scenario
        Given Ignore I save some value X under key Y
        And I allow variable injection
        When Ignore I use value {{Y}}
        Then Ignore Godog rendering should not break
        And Ignore test
          | key | val |
          | 1   | 2   |
          | 3   | 4   |
        And I disable variable injection
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: inject long value

        Scenario: test scenario                        # features/inject.feature:3
          Given Ignore I save some value X under key Y # suite_context.go:0 -> SuiteContext.func12
          And I allow variable injection               # suite_context.go:0 -> *suiteContext
          When Ignore I use value someverylonginjectionsoweacanbesureitsurpasstheinitiallongeststeplenghtanditwillhelptestsmethodsafety # suite_context.go:0 -> SuiteContext.func12
          Then Ignore Godog rendering should not break # suite_context.go:0 -> SuiteContext.func12
          And Ignore test                              # suite_context.go:0 -> SuiteContext.func12
            | key | val |
            | 1   | 2   |
            | 3   | 4   |
          And I disable variable injection             # suite_context.go:0 -> *suiteContext

      1 scenarios (1 passed)
      6 steps (6 passed)
      0s
    """

  Scenario: Should scenarios identified with path:line and preserve the order.
    Given a feature path "features/load.feature:6"
    And a feature path "features/multistep.feature:6"
    And a feature path "features/load.feature:27"
    And a feature path "features/multistep.feature:23"
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
    Feature: load features
      In order to run features
      As a test suite
      I need to be able to load features

      Scenario: load features within path    # features/load.feature:6
        Given a feature path "features"      # suite_context_test.go:0 -> *godogFeaturesScenario
        When I parse features                # suite_context_test.go:0 -> *godogFeaturesScenario
        Then I should have 14 feature files: # suite_context_test.go:0 -> *godogFeaturesScenario
          \"\"\"
          features/background.feature
          features/events.feature
          features/formatter/cucumber.feature
          features/formatter/events.feature
          features/formatter/junit.feature
          features/formatter/pretty.feature
          features/lang.feature
          features/load.feature
          features/multistep.feature
          features/outline.feature
          features/run.feature
          features/snippets.feature
          features/tags.feature
          features/testingt.feature
          \"\"\"

    Feature: run features with nested steps
      In order to test multisteps
      As a test suite
      I need to be able to execute multisteps

      Scenario: should run passing multistep successfully # features/multistep.feature:6
        Given a feature "normal.feature" file:            # suite_context_test.go:0 -> *godogFeaturesScenario
          \"\"\"
          Feature: normal feature

            Scenario: run passing multistep
              Given passing step
              Then passing multistep
          \"\"\"
        When I run feature suite                          # suite_context_test.go:0 -> *godogFeaturesScenario
        Then the suite should have passed                 # suite_context_test.go:0 -> *godogFeaturesScenario
        And the following steps should be passed:         # suite_context_test.go:0 -> *godogFeaturesScenario
          \"\"\"
          passing step
          passing multistep
          \"\"\"

    Feature: load features
      In order to run features
      As a test suite
      I need to be able to load features

      Scenario: load a specific feature file         # features/load.feature:27
        Given a feature path "features/load.feature" # suite_context_test.go:0 -> *godogFeaturesScenario
        When I parse features                        # suite_context_test.go:0 -> *godogFeaturesScenario
        Then I should have 1 feature file:           # suite_context_test.go:0 -> *godogFeaturesScenario
          \"\"\"
          features/load.feature
          \"\"\"

    Feature: run features with nested steps
      In order to test multisteps
      As a test suite
      I need to be able to execute multisteps

      Scenario: should fail multistep              # features/multistep.feature:23
        Given a feature "failed.feature" file:     # suite_context_test.go:0 -> *godogFeaturesScenario
          \"\"\"
          Feature: failed feature

            Scenario: run failing multistep
              Given passing step
              When failing multistep
              Then I should have 1 scenario registered
          \"\"\"
        When I run feature suite                   # suite_context_test.go:0 -> *godogFeaturesScenario
        Then the suite should have failed          # suite_context_test.go:0 -> *godogFeaturesScenario
        And the following step should be failed:   # suite_context_test.go:0 -> *godogFeaturesScenario
          \"\"\"
          failing multistep
          \"\"\"
        And the following steps should be skipped: # suite_context_test.go:0 -> *godogFeaturesScenario
          \"\"\"
          I should have 1 scenario registered
          \"\"\"
        And the following steps should be passed:  # suite_context_test.go:0 -> *godogFeaturesScenario
          \"\"\"
          passing step
          \"\"\"

    4 scenarios (4 passed)
    16 steps (16 passed)
    0s
    """

  Scenario: Support of Feature Plus Rule
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature with a rule
            simple feature description
         Rule: simple rule
             simple rule description
         Example: simple scenario
            simple scenario description
          Given passing step
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature with a rule
        simple feature description

        Example: simple scenario # features/simple.feature:5
          Given passing step     # suite_context.go:0 -> SuiteContext.func2

      1 scenarios (1 passed)
      1 steps (1 passed)
      0s
    """

  Scenario: Support of Feature Plus Rule with Background
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature with a rule with Background
            simple feature description
         Rule: simple rule
             simple rule description
         Background:
             Given passing step
         Example: simple scenario
            simple scenario description
          Given passing step
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature with a rule with Background
        simple feature description

        Background:
          Given passing step     # suite_context.go:0 -> SuiteContext.func2

        Example: simple scenario # features/simple.feature:7
          Given passing step     # suite_context.go:0 -> SuiteContext.func2

      1 scenarios (1 passed)
      2 steps (2 passed)
      0s
    """

  Scenario: Support of Feature Plus Rule with Scenario Outline
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature with a rule with Scenario Outline
            simple feature description
         Rule: simple rule
             simple rule description
         Scenario Outline: simple scenario
             simple scenario description

              Given <status> step

          Examples: simple examples
          | status |
          | passing |
          | failing |
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature with a rule with Scenario Outline
        simple feature description

        Scenario Outline: simple scenario # features/simple.feature:5
          Given <status> step             # suite_context.go:0 -> SuiteContext.func2

          Examples: simple examples
            | status  |
            | passing |
            | failing |
              intentional failure

      --- Failed steps:

        Scenario Outline: simple scenario # features/simple.feature:5
          Given failing step # features/simple.feature:8
          Error: intentional failure


      2 scenarios (1 passed, 1 failed)
      2 steps (1 passed, 1 failed)
      0s
    """

  Scenario: Use 'given' keyword on a declared 'when' step
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature with a rule
            simple feature description
         Rule: simple rule
             simple rule description
         Example: simple scenario
            simple scenario description
          Given a when step
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature with a rule
        simple feature description

        Example: simple scenario # features/simple.feature:5
          Given a when step

      1 scenarios (1 undefined)
      1 steps (1 undefined)
      0s

      You can implement step definitions for undefined steps with these snippets:

      func aWhenStep() error {
        return godog.ErrPending
      }

      func InitializeScenario(ctx *godog.ScenarioContext) {
        ctx.Step(`^a when step$`, aWhenStep)
      }
    """

  Scenario: Use 'when' keyword on a declared 'then' step
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature with a rule
            simple feature description
         Rule: simple rule
             simple rule description
         Example: simple scenario
            simple scenario description
          When a then step
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature with a rule
        simple feature description

        Example: simple scenario # features/simple.feature:5
          When a then step

      1 scenarios (1 undefined)
      1 steps (1 undefined)
      0s

      You can implement step definitions for undefined steps with these snippets:

      func aThenStep() error {
        return godog.ErrPending
      }

      func InitializeScenario(ctx *godog.ScenarioContext) {
        ctx.Step(`^a then step$`, aThenStep)
      }
    """

  Scenario: Use 'then' keyword on a declared 'given' step
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature with a rule
            simple feature description
         Rule: simple rule
             simple rule description
         Example: simple scenario
            simple scenario description
          Then a given step
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature with a rule
        simple feature description

        Example: simple scenario # features/simple.feature:5
          Then a given step

      1 scenarios (1 undefined)
      1 steps (1 undefined)
      0s

      You can implement step definitions for undefined steps with these snippets:

      func aGivenStep() error {
        return godog.ErrPending
      }

      func InitializeScenario(ctx *godog.ScenarioContext) {
        ctx.Step(`^a given step$`, aGivenStep)
      }
    """

  Scenario: Match keyword functions correctly
    Given a feature "features/simple.feature" file:
    """
        Feature: simple feature with a rule
            simple feature description
         Rule: simple rule
             simple rule description
         Example: simple scenario
            simple scenario description
          Given a given step
          When a when step
          Then a then step
          And a then step
    """
    When I run feature suite with formatter "pretty"
    Then the rendered output will be as follows:
    """
      Feature: simple feature with a rule
        simple feature description

	    Example: simple scenario # features/simple.feature:5
	      Given a given step     # suite_context_test.go:0 -> InitializeScenario.func3
	      When a when step       # suite_context_test.go:0 -> InitializeScenario.func4
	      Then a then step       # suite_context_test.go:0 -> InitializeScenario.func5
	      And a then step        # suite_context_test.go:0 -> InitializeScenario.func5

      1 scenarios (1 passed)
      4 steps (4 passed)
      0s
    """
```

## File: `formatters/fmt.go`
```go
package formatters

import (
	"io"
	"regexp"

	messages "github.com/cucumber/messages/go/v21"
)

type registeredFormatter struct {
	name        string
	description string
	fmt         FormatterFunc
}

var registeredFormatters []*registeredFormatter

// FindFmt searches available formatters registered
// and returns FormaterFunc matched by given
// format name or nil otherwise
func FindFmt(name string) FormatterFunc {
	for _, el := range registeredFormatters {
		if el.name == name {
			return el.fmt
		}
	}

	return nil
}

// Format registers a feature suite output
// formatter by given name, description and
// FormatterFunc constructor function, to initialize
// formatter with the output recorder.
func Format(name, description string, f FormatterFunc) {
	registeredFormatters = append(registeredFormatters, &registeredFormatter{
		name:        name,
		fmt:         f,
		description: description,
	})
}

// AvailableFormatters gives a map of all
// formatters registered with their name as key
// and description as value
func AvailableFormatters() map[string]string {
	fmts := make(map[string]string, len(registeredFormatters))

	for _, f := range registeredFormatters {
		fmts[f.name] = f.description
	}

	return fmts
}

// Formatter is an interface for feature runner
// output summary presentation.
//
// New formatters may be created to represent
// suite results in different ways. These new
// formatters needs to be registered with a
// godog.Format function call
type Formatter interface {
	TestRunStarted()
	Feature(*messages.GherkinDocument, string, []byte)
	Pickle(*messages.Pickle)
	Defined(*messages.Pickle, *messages.PickleStep, *StepDefinition)
	Failed(*messages.Pickle, *messages.PickleStep, *StepDefinition, error)
	Passed(*messages.Pickle, *messages.PickleStep, *StepDefinition)
	Skipped(*messages.Pickle, *messages.PickleStep, *StepDefinition)
	Undefined(*messages.Pickle, *messages.PickleStep, *StepDefinition)
	Pending(*messages.Pickle, *messages.PickleStep, *StepDefinition)
	Ambiguous(*messages.Pickle, *messages.PickleStep, *StepDefinition, error)
	Summary()
}

// FlushFormatter is a `Formatter` but can be flushed.
type FlushFormatter interface {
	Formatter
	Flush()
}

// FormatterFunc builds a formatter with given
// suite name and io.Writer to record output
type FormatterFunc func(string, io.Writer) Formatter

// StepDefinition is a registered step definition
// contains a StepHandler and regexp which
// is used to match a step. Args which
// were matched by last executed step
//
// This structure is passed to the formatter
// when step is matched and is either failed
// or successful
type StepDefinition struct {
	Expr    *regexp.Regexp
	Handler interface{}
	Keyword Keyword
}

type Keyword int64

const (
	Given Keyword = iota
	When
	Then
	None
)
```

## File: `formatters/fmt_test.go`
```go
package formatters_test

import (
	"io"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/cucumber/godog"
)

func Test_FindFmt(t *testing.T) {
	cases := map[string]bool{
		"cucumber": true,
		"events":   true,
		"junit":    true,
		"pretty":   true,
		"progress": true,
		"unknown":  false,
		"undef":    false,
	}

	for name, expected := range cases {
		t.Run(
			name,
			func(t *testing.T) {
				actual := godog.FindFmt(name)

				if expected {
					assert.NotNilf(t, actual, "expected %s formatter should be available", name)
				} else {
					assert.Nilf(t, actual, "expected %s formatter should be available", name)
				}
			},
		)
	}
}

func Test_AvailableFormatters(t *testing.T) {
	expected := map[string]string{
		"cucumber": "Produces cucumber JSON format output.",
		"events":   "Produces JSON event stream, based on spec: 0.1.0.",
		"junit":    "Prints junit compatible xml to stdout",
		"pretty":   "Prints every feature with runtime statuses.",
		"progress": "Prints a character per step.",
	}

	actual := godog.AvailableFormatters()
	assert.Equal(t, expected, actual)
}

func Test_Format(t *testing.T) {
	actual := godog.FindFmt("Test_Format")
	require.Nil(t, actual)

	godog.Format("Test_Format", "...", testFormatterFunc)
	actual = godog.FindFmt("Test_Format")

	assert.NotNil(t, actual)
}

func testFormatterFunc(suiteName string, out io.Writer) godog.Formatter {
	return nil
}
```

## File: `internal/builder/ast.go`
```go
package builder

import "go/ast"

func astContexts(f *ast.File, selectName string) []string {
	var contexts []string
	for _, d := range f.Decls {
		switch fun := d.(type) {
		case *ast.FuncDecl:
			for _, param := range fun.Type.Params.List {
				switch expr := param.Type.(type) {
				case *ast.StarExpr:
					switch x := expr.X.(type) {
					case *ast.Ident:
						if x.Name == selectName {
							contexts = append(contexts, fun.Name.Name)
						}
					case *ast.SelectorExpr:
						switch t := x.X.(type) {
						case *ast.Ident:
							if t.Name == "godog" && x.Sel.Name == selectName {
								contexts = append(contexts, fun.Name.Name)
							}
						}
					}
				}
			}
		}
	}
	return contexts
}
```

## File: `internal/builder/ast_test.go`
```go
package builder

import (
	"go/parser"
	"go/token"
	"testing"
)

var astContextSrc = `package main

import (
	"github.com/cucumber/godog"
)

func MyContext(s *godog.Suite) {
}`

var astTwoContextSrc = `package lib

import (
	"github.com/cucumber/godog"
)

func ApiContext(s *godog.Suite) {
}

func DBContext(s *godog.Suite) {
}`

func astContextParse(src string, t *testing.T) []string {
	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, "", []byte(src), 0)
	if err != nil {
		t.Fatalf("unexpected error while parsing ast: %v", err)
	}

	return astContexts(f, "Suite")
}

func TestShouldGetSingleContextFromSource(t *testing.T) {
	actual := astContextParse(astContextSrc, t)
	expect := []string{"MyContext"}

	if len(actual) != len(expect) {
		t.Fatalf("number of found contexts do not match, expected %d, but got %d", len(expect), len(actual))
	}

	for i, c := range expect {
		if c != actual[i] {
			t.Fatalf("expected context '%s' at pos %d, but got: '%s'", c, i, actual[i])
		}
	}
}

func TestShouldGetTwoContextsFromSource(t *testing.T) {
	actual := astContextParse(astTwoContextSrc, t)
	expect := []string{"ApiContext", "DBContext"}

	if len(actual) != len(expect) {
		t.Fatalf("number of found contexts do not match, expected %d, but got %d", len(expect), len(actual))
	}

	for i, c := range expect {
		if c != actual[i] {
			t.Fatalf("expected context '%s' at pos %d, but got: '%s'", c, i, actual[i])
		}
	}
}

func TestShouldNotFindAnyContextsInEmptyFile(t *testing.T) {
	actual := astContextParse(`package main`, t)

	if len(actual) != 0 {
		t.Fatalf("expected no contexts to be found, but there was some: %v", actual)
	}
}
```

## File: `internal/builder/builder.go`
```go
package builder

import (
	"bytes"
	"encoding/json"
	"fmt"
	"go/build"
	"go/parser"
	"go/token"
	"io/ioutil"
	"os"
	"os/exec"
	"path"
	"path/filepath"
	"strings"
	"text/template"
	"time"
	"unicode"
)

var (
	tooldir         = findToolDir()
	compiler        = filepath.Join(tooldir, "compile")
	linker          = filepath.Join(tooldir, "link")
	gopaths         = filepath.SplitList(build.Default.GOPATH)
	godogImportPath = "github.com/cucumber/godog"

	// godep
	runnerTemplate = template.Must(template.New("testmain").Parse(`package main

import (
	"github.com/cucumber/godog"
	{{if or .TestSuiteContexts .ScenarioContexts}}_test "{{.ImportPath}}"{{end}}
	{{if or .XTestSuiteContexts .XScenarioContexts}}_xtest "{{.ImportPath}}_test"{{end}}
	{{if or .XTestSuiteContexts .XScenarioContexts}}"testing/internal/testdeps"{{end}}
	"os"
)

{{if or .XTestSuiteContexts .XScenarioContexts}}
func init() {
	testdeps.ImportPath = "{{.ImportPath}}"
}
{{end}}

func main() {
	status := godog.TestSuite{
		Name: "{{ .Name }}",
		TestSuiteInitializer: func (ctx *godog.TestSuiteContext) {
			os.Setenv("GODOG_TESTED_PACKAGE", "{{.ImportPath}}")
			{{range .TestSuiteContexts}}
			_test.{{ . }}(ctx)
			{{end}}
			{{range .XTestSuiteContexts}}
			_xtest.{{ . }}(ctx)
			{{end}}
		},
		ScenarioInitializer: func (ctx *godog.ScenarioContext) {
			{{range .ScenarioContexts}}
			_test.{{ . }}(ctx)
			{{end}}
			{{range .XScenarioContexts}}
			_xtest.{{ . }}(ctx)
			{{end}}
		},
	}.Run()

	os.Exit(status)
}`))

	// temp file for import
	tempFileTemplate = template.Must(template.New("temp").Parse(`package {{.Name}}

import "github.com/cucumber/godog"

var _ = godog.Version
`))
)

// Build creates a test package like go test command at given target path.
// If there are no go files in tested directory, then
// it simply builds a godog executable to scan features.
//
// If there are go test files, it first builds a test
// package with standard go test command.
//
// Finally it generates godog suite executable which
// registers exported godog contexts from the test files
// of tested package.
//
// Returns the path to generated executable
func Build(bin string) error {
	abs, err := filepath.Abs(".")
	if err != nil {
		return err
	}

	// we allow package to be nil, if godog is run only when
	// there is a feature file in empty directory
	pkg := importPackage(abs)
	src, err := buildTestMain(pkg)
	if err != nil {
		return err
	}

	// may need to produce temp file for godog dependency
	srcTemp, err := buildTempFile(pkg)
	if err != nil {
		return err
	}

	if srcTemp != nil {
		// @TODO: in case of modules we cannot build it our selves, we need to have this hacky option
		pathTemp := filepath.Join(abs, "godog_dependency_file_test.go")
		err = ioutil.WriteFile(pathTemp, srcTemp, 0644)
		if err != nil {
			return err
		}
		defer os.Remove(pathTemp)
	}

	workdir := ""
	testdir := workdir

	// build and compile the tested package.
	// generated test executable will be removed
	// since we do not need it for godog suite.
	// we also print back the temp WORK directory
	// go has built. We will reuse it for our suite workdir.
	temp := fmt.Sprintf(filepath.Join("%s", "temp-%d.test"), os.TempDir(), time.Now().UnixNano())
	if os.Getenv("GO111MODULE") != "off" {
		modTidyOutput, err := exec.Command("go", "mod", "tidy").CombinedOutput()
		if err != nil {
			return fmt.Errorf("failed to tidy modules in tested package: %s, reason: %v, output: %s", abs, err, string(modTidyOutput))
		}
	}
	testOutput, err := exec.Command("go", "test", "-c", "-work", "-o", temp).CombinedOutput()
	if err != nil {
		return fmt.Errorf("failed to compile tested package: %s, reason: %v, output: %s", abs, err, string(testOutput))
	}
	defer os.Remove(temp)

	// extract go-build temporary directory as our workdir
	linesOut := strings.Split(strings.TrimSpace(string(testOutput)), "\n")
	// it may have some compilation warnings, in the output, but these are not
	// considered to be errors, since command exit status is 0
	for _, ln := range linesOut {
		if !strings.HasPrefix(ln, "WORK=") {
			continue
		}
		workdir = strings.Replace(ln, "WORK=", "", 1)
		break
	}

	if strings.Contains(string(testOutput), "[no test files]") {
		return fmt.Errorf("incorrect project structure: no test files found")
	}

	// may not locate it in output
	if workdir == testdir {
		return fmt.Errorf("expected WORK dir path to be present in output: %s", string(testOutput))
	}

	// check whether workdir exists
	stats, err := os.Stat(workdir)
	if os.IsNotExist(err) {
		return fmt.Errorf("expected WORK dir: %s to be available", workdir)
	}

	if !stats.IsDir() {
		return fmt.Errorf("expected WORK dir: %s to be directory", workdir)
	}
	testdir = filepath.Join(workdir, "b001")
	defer os.RemoveAll(workdir)

	// replace _testmain.go file with our own
	testmain := filepath.Join(testdir, "_testmain.go")
	err = ioutil.WriteFile(testmain, src, 0644)
	if err != nil {
		return err
	}

	// godog package may be vendored and may need importmap
	vendored := maybeVendoredGodog()

	// compile godog testmain package archive
	// we do not depend on CGO so a lot of checks are not necessary
	linkerCfg := filepath.Join(testdir, "importcfg.link")
	compilerCfg := linkerCfg

	if vendored != nil {
		data, err := ioutil.ReadFile(linkerCfg)
		if err != nil {
			return err
		}

		data = append(data, []byte(fmt.Sprintf("importmap %s=%s\n", godogImportPath, vendored.ImportPath))...)
		compilerCfg = filepath.Join(testdir, "importcfg")

		err = ioutil.WriteFile(compilerCfg, data, 0644)
		if err != nil {
			return err
		}
	}

	testMainPkgOut := filepath.Join(testdir, "main.a")
	args := []string{
		"-o", testMainPkgOut,
		"-importcfg", compilerCfg,
		"-p", "main",
		"-complete",
	}

	if err := filterImportCfg(compilerCfg); err != nil {
		return err
	}

	args = append(args, "-pack", testmain)
	cmd := exec.Command(compiler, args...)
	cmd.Env = os.Environ()
	out, err := cmd.CombinedOutput()
	if err != nil {
		return fmt.Errorf("failed to compile testmain package: %v - output: %s", err, string(out))
	}

	// link test suite executable
	args = []string{
		"-o", bin,
		"-importcfg", linkerCfg,
		"-buildmode=exe",
	}
	args = append(args, testMainPkgOut)
	cmd = exec.Command(linker, args...)
	cmd.Env = os.Environ()

	out, err = cmd.CombinedOutput()
	if err != nil {
		msg := `failed to link test executable:
	reason: %s
	command: %s`
		return fmt.Errorf(msg, string(out), linker+" '"+strings.Join(args, "' '")+"'")
	}

	return nil
}

// filterImportCfg strips unsupported lines from imports configuration.
func filterImportCfg(path string) error {
	orig, err := os.ReadFile(path)
	if err != nil {
		return fmt.Errorf("failed to read %s: %w", path, err)
	}

	res := ""
	for _, l := range strings.Split(string(orig), "\n") {
		if !strings.HasPrefix(l, "modinfo") {
			res += l + "\n"
		}
	}
	err = ioutil.WriteFile(path, []byte(res), 0600)
	if err != nil {
		return fmt.Errorf("failed to write %s: %w", path, err)
	}

	return nil
}

func maybeVendoredGodog() *build.Package {
	dir, err := filepath.Abs(".")
	if err != nil {
		return nil
	}

	for _, gopath := range gopaths {
		gopath = filepath.Join(gopath, "src")
		for strings.HasPrefix(dir, gopath) && dir != gopath {
			pkg, err := build.ImportDir(filepath.Join(dir, "vendor", godogImportPath), 0)
			if err != nil {
				dir = filepath.Dir(dir)
				continue
			}
			return pkg
		}
	}
	return nil
}

func normaliseLocalImportPath(dir string) string {
	return path.Join("_", strings.Map(makeImportValid, filepath.ToSlash(dir)))
}
func importPackage(dir string) *build.Package {
	pkg, _ := build.ImportDir(dir, 0)

	// normalize import path for local import packages
	// taken from go source code
	// see: https://github.com/golang/go/blob/go1.7rc5/src/cmd/go/pkg.go#L279
	if pkg != nil && pkg.ImportPath == "." {
		pkg.ImportPath = normaliseLocalImportPath(dir)
	}

	return pkg
}

// from go src
func makeImportValid(r rune) rune {
	// Should match Go spec, compilers, and ../../go/parser/parser.go:/isValidImport.
	const illegalChars = `!"#$%&'()*,:;<=>?[\]^{|}` + "`\uFFFD"
	if !unicode.IsGraphic(r) || unicode.IsSpace(r) || strings.ContainsRune(illegalChars, r) {
		return '_'
	}
	return r
}

// build temporary file content if godog
// package is not present in currently tested package
func buildTempFile(pkg *build.Package) ([]byte, error) {
	shouldBuild := true
	var name string
	if pkg != nil {
		name = pkg.Name
		all := pkg.Imports
		all = append(all, pkg.TestImports...)
		all = append(all, pkg.XTestImports...)
		for _, imp := range all {
			if imp == godogImportPath {
				shouldBuild = false
				break
			}
		}

		// maybe we are testing the godog package on it's own
		if name == "godog" {
			if parseImport(pkg.ImportPath, pkg.Root) == godogImportPath {
				shouldBuild = false
			}
		}
	}

	if name == "" {
		name = "main"
	}

	if !shouldBuild {
		return nil, nil
	}

	data := struct{ Name string }{name}
	var buf bytes.Buffer
	if err := tempFileTemplate.Execute(&buf, data); err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

// buildTestMain if given package is valid
// it scans test files for contexts
// and produces a testmain source code.
func buildTestMain(pkg *build.Package) ([]byte, error) {
	var (
		ctxs, xctxs contexts
		err         error
		name        = "main"
		importPath  string
	)

	if nil != pkg {
		if ctxs, err = processPackageTestFiles(pkg.TestGoFiles); err != nil {
			return nil, err
		}

		if xctxs, err = processPackageTestFiles(pkg.XTestGoFiles); err != nil {
			return nil, err
		}

		importPath = parseImport(pkg.ImportPath, pkg.Root)
		name = pkg.Name
	} else {
		name = "main"
	}

	data := struct {
		Name               string
		ImportPath         string
		TestSuiteContexts  []string
		ScenarioContexts   []string
		XTestSuiteContexts []string
		XScenarioContexts  []string
	}{
		Name:               name,
		ImportPath:         importPath,
		TestSuiteContexts:  ctxs.testSuiteCtxs,
		ScenarioContexts:   ctxs.scenarioCtxs,
		XTestSuiteContexts: xctxs.testSuiteCtxs,
		XScenarioContexts:  xctxs.scenarioCtxs,
	}

	var buf bytes.Buffer
	if err = runnerTemplate.Execute(&buf, data); err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

// parseImport parses the import path to deal with go module.
func parseImport(rawPath, rootPath string) string {
	// with go > 1.11 and go module enabled out of the GOPATH,
	// the import path begins with an underscore and the GOPATH is unknown on build.
	if rootPath != "" {
		// go < 1.11 or it's a module inside the GOPATH
		return rawPath
	}
	// for module support, query the module import path
	cmd := exec.Command("go", "list", "-m", "-json")
	out, err := cmd.StdoutPipe()
	if err != nil {
		// Unable to read stdout
		return rawPath
	}
	if cmd.Start() != nil {
		// Does not using modules
		return rawPath
	}
	var mod struct {
		Dir  string `json:"Dir"`
		Path string `json:"Path"`
	}
	if json.NewDecoder(out).Decode(&mod) != nil {
		// Unexpected result
		return rawPath
	}
	if cmd.Wait() != nil {
		return rawPath
	}
	// Concatenates the module path with the current sub-folders if needed
	return mod.Path + filepath.ToSlash(strings.TrimPrefix(rawPath, normaliseLocalImportPath(mod.Dir)))
}

type contexts struct {
	deprecatedFeatureCtxs []string
	testSuiteCtxs         []string
	scenarioCtxs          []string
}

func (ctxs contexts) validate() error {
	var allCtxs []string
	allCtxs = append(allCtxs, ctxs.deprecatedFeatureCtxs...)
	allCtxs = append(allCtxs, ctxs.testSuiteCtxs...)
	allCtxs = append(allCtxs, ctxs.scenarioCtxs...)

	var failed []string
	for _, ctx := range allCtxs {
		runes := []rune(ctx)
		if unicode.IsLower(runes[0]) {
			expected := append([]rune{unicode.ToUpper(runes[0])}, runes[1:]...)
			failed = append(failed, fmt.Sprintf("%s - should be: %s", ctx, string(expected)))
		}
	}

	if len(failed) > 0 {
		return fmt.Errorf("godog contexts must be exported:\n\t%s", strings.Join(failed, "\n\t"))
	}

	return nil
}

// processPackageTestFiles runs through ast of each test
// file pack and looks for godog suite contexts to register
// on run
func processPackageTestFiles(packs ...[]string) (ctxs contexts, _ error) {
	fset := token.NewFileSet()
	for _, pack := range packs {
		for _, testFile := range pack {
			node, err := parser.ParseFile(fset, testFile, nil, 0)
			if err != nil {
				return ctxs, err
			}

			ctxs.testSuiteCtxs = append(ctxs.testSuiteCtxs, astContexts(node, "TestSuiteContext")...)
			ctxs.scenarioCtxs = append(ctxs.scenarioCtxs, astContexts(node, "ScenarioContext")...)
		}
	}

	return ctxs, ctxs.validate()
}

func findToolDir() string {
	if out, err := exec.Command("go", "env", "GOTOOLDIR").Output(); err != nil {
		return filepath.Clean(strings.TrimSpace(string(out)))
	}
	return filepath.Clean(build.ToolDir)
}
```

## File: `internal/builder/builder_go112_test.go`
```go
//go:build go1.12 && !go1.13
// +build go1.12,!go1.13

package builder_test

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/require"
)

func testWithVendoredGodogAndMod(t *testing.T) {
	builderTC := builderTestCase{}

	gopath := filepath.Join(os.TempDir(), t.Name(), "_gpc")
	defer os.RemoveAll(gopath)

	builderTC.dir = filepath.Join(gopath, "src", "godogs")
	builderTC.files = map[string]string{
		"godogs.feature": builderFeatureFile,
		"godogs.go":      builderMainCodeFile,
		"godogs_test.go": builderTestFile,
		"go.mod":         builderModFile,
	}

	pkg := filepath.Join(builderTC.dir, "vendor", "github.com", "cucumber")
	err := os.MkdirAll(pkg, 0755)
	require.Nil(t, err)

	wd, err := os.Getwd()
	require.Nil(t, err)

	// symlink godog package
	err = os.Symlink(wd, filepath.Join(pkg, "godog"))
	require.Nil(t, err)

	builderTC.testCmdEnv = append(envVarsWithoutGopath(), "GOPATH="+gopath)
	builderTC.run(t)
}
```

## File: `internal/builder/builder_go113_test.go`
```go
//go:build go1.13
// +build go1.13

package builder_test

import (
	"os"
	"os/exec"
	"path/filepath"
	"testing"
)

func testWithVendoredGodogAndMod(t *testing.T) {
	builderTC := builderTestCase{}

	gopath := filepath.Join(os.TempDir(), t.Name(), "_gpc")
	defer os.RemoveAll(gopath)

	builderTC.dir = filepath.Join(gopath, "src", "godogs")
	builderTC.files = map[string]string{
		"godogs.feature": builderFeatureFile,
		"godogs.go":      builderMainCodeFile,
		"godogs_test.go": builderTestFile,
		"go.mod":         builderModFile,
	}

	builderTC.goModCmds = make([]*exec.Cmd, 2)
	builderTC.goModCmds[0] = exec.Command("go", "mod", "tidy")
	builderTC.goModCmds[1] = exec.Command("go", "mod", "vendor")
	builderTC.testCmdEnv = append(envVarsWithoutGopath(), "GOPATH="+gopath)

	builderTC.run(t)
}
```

## File: `internal/builder/builder_go_module_test.go`
```go
package builder_test

import (
	"os"
	"os/exec"
	"path/filepath"
	"testing"
)

func testOutsideGopathAndHavingOnlyFeature(t *testing.T) {
	builderTC := builderTestCase{}

	builderTC.dir = filepath.Join(os.TempDir(), t.Name(), "godogs")
	builderTC.files = map[string]string{
		"godogs.feature": builderFeatureFile,
	}

	builderTC.goModCmds = make([]*exec.Cmd, 2)
	builderTC.goModCmds[0] = exec.Command("go", "mod", "init", "godogs")

	builderTC.goModCmds[1] = exec.Command("go", "mod", "tidy")

	builderTC.run(t)
}

func testOutsideGopath(t *testing.T) {
	builderTC := builderTestCase{}

	builderTC.dir = filepath.Join(os.TempDir(), t.Name(), "godogs")
	builderTC.files = map[string]string{
		"godogs.feature": builderFeatureFile,
		"godogs.go":      builderMainCodeFile,
		"godogs_test.go": builderTestFile,
	}

	builderTC.goModCmds = make([]*exec.Cmd, 1)
	builderTC.goModCmds[0] = exec.Command("go", "mod", "init", "godogs")

	builderTC.run(t)
}

func testOutsideGopathWithXTest(t *testing.T) {
	builderTC := builderTestCase{}

	builderTC.dir = filepath.Join(os.TempDir(), t.Name(), "godogs")
	builderTC.files = map[string]string{
		"godogs.feature": builderFeatureFile,
		"godogs.go":      builderMainCodeFile,
		"godogs_test.go": builderXTestFile,
	}

	builderTC.goModCmds = make([]*exec.Cmd, 1)
	builderTC.goModCmds[0] = exec.Command("go", "mod", "init", "godogs")

	builderTC.run(t)
}

func testInsideGopath(t *testing.T) {
	builderTC := builderTestCase{}

	gopath := filepath.Join(os.TempDir(), t.Name(), "_gp")
	defer os.RemoveAll(gopath)

	builderTC.dir = filepath.Join(gopath, "src", "godogs")
	builderTC.files = map[string]string{
		"godogs.feature": builderFeatureFile,
		"godogs.go":      builderMainCodeFile,
		"godogs_test.go": builderTestFile,
	}

	builderTC.goModCmds = make([]*exec.Cmd, 1)
	builderTC.goModCmds[0] = exec.Command("go", "mod", "init", "godogs")
	builderTC.goModCmds[0].Env = os.Environ()
	builderTC.goModCmds[0].Env = append(builderTC.goModCmds[0].Env, "GOPATH="+gopath)
	builderTC.goModCmds[0].Env = append(builderTC.goModCmds[0].Env, "GO111MODULE=on")

	builderTC.run(t)
}
```

## File: `internal/builder/builder_test.go`
```go
package builder_test

import (
	"bytes"
	"go/build"
	"io/ioutil"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"testing"

	"github.com/stretchr/testify/require"

	"github.com/cucumber/godog"
	"github.com/cucumber/godog/internal/builder"
)

func InitializeScenario(ctx *godog.ScenarioContext) {}

func Test_GodogBuild(t *testing.T) {
	t.Run("WithSourceNotInGoPath", testWithSourceNotInGoPath)
	t.Run("WithoutSourceNotInGoPath", testWithoutSourceNotInGoPath)
	t.Run("WithoutTestSourceNotInGoPath", testWithoutTestSourceNotInGoPath)
	t.Run("WithinGopath", testWithinGopath)
	t.Run("WithVendoredGodogWithoutModule", testWithVendoredGodogWithoutModule)
	t.Run("WithVendoredGodogAndMod", testWithVendoredGodogAndMod)
	t.Run("WithIncorrectProjectStructure", testWithIncorrectProjectStructure)

	t.Run("WithModule", func(t *testing.T) {
		t.Run("OutsideGopathAndHavingOnlyFeature", testOutsideGopathAndHavingOnlyFeature)
		t.Run("OutsideGopath", testOutsideGopath)
		t.Run("OutsideGopathWithXTest", testOutsideGopathWithXTest)
		t.Run("InsideGopath", testInsideGopath)
	})
}

var builderFeatureFile = `Feature: eat godogs
  In order to be happy
  As a hungry gopher
  I need to be able to eat godogs

  Scenario: Eat 5 out of 12
    Given there are 12 godogs
    When I eat 5
    Then there should be 7 remaining
`

var builderTestFile = `package godogs

import (
	"fmt"

	"github.com/cucumber/godog"
)

func thereAreGodogs(available int) error {
	Godogs = available
	return nil
}

func iEat(num int) error {
	if Godogs < num {
		return fmt.Errorf("you cannot eat %d godogs, there are %d available", num, Godogs)
	}
	Godogs -= num
	return nil
}

func thereShouldBeRemaining(remaining int) error {
	if Godogs != remaining {
		return fmt.Errorf("expected %d godogs to be remaining, but there is %d", remaining, Godogs)
	}
	return nil
}


func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Step("^there are (\\d+) godogs$", thereAreGodogs)
	ctx.Step("^I eat (\\d+)$", iEat)
	ctx.Step("^there should be (\\d+) remaining$", thereShouldBeRemaining)

	ctx.BeforeScenario(func(*godog.Scenario) {
		Godogs = 0 // clean the state before every scenario
	})
}
`

var builderXTestFile = `package godogs_test

import (
	"fmt"

	"github.com/cucumber/godog"

	"godogs"
)

func thereAreGodogs(available int) error {
	godogs.Godogs = available
	return nil
}

func iEat(num int) error {
	if godogs.Godogs < num {
		return fmt.Errorf("you cannot eat %d godogs, there are %d available", num, godogs.Godogs)
	}
	godogs.Godogs -= num
	return nil
}

func thereShouldBeRemaining(remaining int) error {
	if godogs.Godogs != remaining {
		return fmt.Errorf("expected %d godogs to be remaining, but there is %d", remaining, godogs.Godogs)
	}
	return nil
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Step("^there are (\\d+) godogs$", thereAreGodogs)
	ctx.Step("^I eat (\\d+)$", iEat)
	ctx.Step("^there should be (\\d+) remaining$", thereShouldBeRemaining)

	ctx.BeforeScenario(func(*godog.Scenario) {
		godogs.Godogs = 0 // clean the state before every scenario
	})
}
`

var builderMainCodeFile = `package godogs

// Godogs available to eat
var Godogs int

func main() {
}
`

var emptyBuilderTestFile = `package godogs

import "github.com/cucumber/godog"
 
func InitializeScenario(ctx *godog.ScenarioContext) {}
`

var builderModFile = `module godogs`

func buildTestPackage(dir string, files map[string]string) error {
	if err := os.MkdirAll(dir, 0755); err != nil {
		return err
	}

	for name, content := range files {
		if err := ioutil.WriteFile(filepath.Join(dir, name), []byte(content), 0644); err != nil {
			return err
		}
	}

	return nil
}

func buildTestCommand(t *testing.T, wd, featureFile string) *exec.Cmd {
	testBin := filepath.Join(wd, "godog.test")
	testBin, err := filepath.Abs(testBin)
	require.Nil(t, err)

	if build.Default.GOOS == "windows" {
		testBin += ".exe"
	}

	err = builder.Build(testBin)
	require.Nil(t, err)

	featureFilePath := filepath.Join(wd, featureFile)
	return exec.Command(testBin, featureFilePath)
}

func envVarsWithoutGopath() []string {
	var env []string

	for _, def := range os.Environ() {
		if strings.Index(def, "GOPATH=") == 0 {
			continue
		}

		env = append(env, def)
	}

	return env
}

func testWithSourceNotInGoPath(t *testing.T) {
	dir := filepath.Join(os.TempDir(), t.Name(), "godogs")
	files := map[string]string{
		"godogs.feature": builderFeatureFile,
		"godogs.go":      builderMainCodeFile,
		"godogs_test.go": builderTestFile,
		"go.mod":         builderModFile,
	}

	err := buildTestPackage(dir, files)
	defer os.RemoveAll(dir)
	require.Nil(t, err)

	prevDir, err := os.Getwd()
	require.Nil(t, err)

	err = os.Chdir(dir)
	require.Nil(t, err)
	defer os.Chdir(prevDir)

	testCmd := buildTestCommand(t, "", "godogs.feature")
	testCmd.Env = os.Environ()

	var stdout, stderr bytes.Buffer
	testCmd.Stdout = &stdout
	testCmd.Stderr = &stderr

	err = testCmd.Run()
	require.Nil(t, err, "stdout:\n%s\nstderr:\n%s", stdout.String(), stderr.String())
}

func testWithoutSourceNotInGoPath(t *testing.T) {
	builderTC := builderTestCase{}

	builderTC.dir = filepath.Join(os.TempDir(), t.Name(), "godogs")
	builderTC.files = map[string]string{
		"godogs.feature": builderFeatureFile,
		"go.mod":         builderModFile,
	}

	builderTC.run(t)
}

func testWithoutTestSourceNotInGoPath(t *testing.T) {
	builderTC := builderTestCase{}

	builderTC.dir = filepath.Join(os.TempDir(), t.Name(), "godogs")
	builderTC.files = map[string]string{
		"godogs.feature": builderFeatureFile,
		"godogs.go":      builderMainCodeFile,
		"go.mod":         builderModFile,
	}

	builderTC.run(t)
}

func testWithIncorrectProjectStructure(t *testing.T) {
	dir := filepath.Join(os.TempDir(), t.Name(), "godogs")
	files := map[string]string{
		"godogs.go": emptyBuilderTestFile,
		"go.mod":    builderModFile,
	}

	err := buildTestPackage(dir, files)
	defer os.RemoveAll(dir)
	require.Nil(t, err)

	prevDir, err := os.Getwd()
	require.Nil(t, err)
	err = os.Chdir(dir)
	require.Nil(t, err)
	defer os.Chdir(prevDir)

	testBin, err := filepath.Abs(filepath.Join(dir, "godog.test"))
	require.Nil(t, err)

	if build.Default.GOOS == "windows" {
		testBin += ".exe"
	}

	// call the builder - we should get an error
	err = builder.Build(testBin)
	// check that we even got an error at all
	require.NotNil(t, err)
	// now check the details of the error message
	require.EqualError(t, err, "incorrect project structure: no test files found")
}

func testWithinGopath(t *testing.T) {
	builderTC := builderTestCase{}

	gopath := filepath.Join(os.TempDir(), t.Name(), "_gp")
	defer os.RemoveAll(gopath)

	builderTC.dir = filepath.Join(gopath, "src", "godogs")
	builderTC.files = map[string]string{
		"godogs.feature": builderFeatureFile,
		"godogs.go":      builderMainCodeFile,
		"godogs_test.go": builderTestFile,
		"go.mod":         builderModFile,
	}

	pkg := filepath.Join(gopath, "src", "github.com", "cucumber")
	err := os.MkdirAll(pkg, 0755)
	require.Nil(t, err)

	wd, err := os.Getwd()
	require.Nil(t, err)

	// symlink godog package
	err = os.Symlink(wd, filepath.Join(pkg, "godog"))
	require.Nil(t, err)

	builderTC.testCmdEnv = []string{"GOPATH=" + gopath}
	builderTC.run(t)
}

func testWithVendoredGodogWithoutModule(t *testing.T) {
	builderTC := builderTestCase{}

	gopath := filepath.Join(os.TempDir(), t.Name(), "_gp")
	defer os.RemoveAll(gopath)

	builderTC.dir = filepath.Join(gopath, "src", "godogs")
	builderTC.files = map[string]string{
		"godogs.feature": builderFeatureFile,
	}

	pkg := filepath.Join(builderTC.dir, "vendor", "github.com", "cucumber")
	err := os.MkdirAll(pkg, 0755)
	require.Nil(t, err)

	wd, err := os.Getwd()
	require.Nil(t, err)

	// symlink godog package
	err = os.Symlink(wd, filepath.Join(pkg, "godog"))
	require.Nil(t, err)

	builderTC.testCmdEnv = append(envVarsWithoutGopath(), "GOPATH="+gopath)
	builderTC.run(t)
}

type builderTestCase struct {
	dir        string
	files      map[string]string
	goModCmds  []*exec.Cmd
	testCmdEnv []string
}

func (bt builderTestCase) run(t *testing.T) {
	err := buildTestPackage(bt.dir, bt.files)
	defer os.RemoveAll(bt.dir)
	require.Nil(t, err)

	for _, c := range bt.goModCmds {
		c.Dir = bt.dir
		out, err := c.CombinedOutput()
		require.Nil(t, err, "%s", string(out))
	}

	testCmd := buildTestCommand(t, bt.dir, "godogs.feature")
	testCmd.Env = append(os.Environ(), bt.testCmdEnv...)

	var stdout, stderr bytes.Buffer
	testCmd.Stdout = &stdout
	testCmd.Stderr = &stderr

	err = testCmd.Run()
	require.Nil(t, err, "stdout:\n%s\nstderr:\n%s", stdout.String(), stderr.String())
}
```

## File: `internal/flags/flags.go`
```go
package flags

import (
	"github.com/spf13/pflag"
)

// BindRunCmdFlags is an internal func to bind run subcommand flags.
func BindRunCmdFlags(prefix string, flagSet *pflag.FlagSet, opts *Options) {
	if opts.Concurrency == 0 {
		opts.Concurrency = 1
	}

	if opts.Format == "" {
		opts.Format = "pretty"
	}

	flagSet.BoolVar(&opts.NoColors, prefix+"no-colors", opts.NoColors, "disable ansi colors")
	flagSet.IntVarP(&opts.Concurrency, prefix+"concurrency", "c", opts.Concurrency, "run the test suite with concurrency")
	flagSet.StringVarP(&opts.Tags, prefix+"tags", "t", opts.Tags, `filter scenarios by tags, expression can be:
  "@wip"           run all scenarios with wip tag
  "~@wip"          exclude all scenarios with wip tag
  "@wip && ~@new"  run wip scenarios, but exclude new
  "@wip,@undone"   run wip or undone scenarios`)
	flagSet.StringVarP(&opts.Format, prefix+"format", "f", opts.Format, `will write a report according to the selected formatter

usage:
  -f <formatter>
  will use the formatter and write the report on stdout
  -f <formatter>:<file_path>
  will use the formatter and write the report to the file path

built-in formatters are:
  progress  prints a character per step
  cucumber  produces a Cucumber JSON report
  events    produces JSON event stream, based on spec: 0.1.0
  junit     produces JUnit compatible XML report
  pretty    prints every feature with runtime statuses
 `)

	flagSet.BoolVarP(&opts.ShowStepDefinitions, prefix+"definitions", "d", opts.ShowStepDefinitions, "print all available step definitions")
	flagSet.BoolVar(&opts.StopOnFailure, prefix+"stop-on-failure", opts.StopOnFailure, "stop processing on first failed scenario")
	flagSet.BoolVar(&opts.Strict, prefix+"strict", opts.Strict, "fail suite when there are pending or undefined or ambiguous steps")

	flagSet.Int64Var(&opts.Randomize, prefix+"random", opts.Randomize, `randomly shuffle the scenario execution order
  --random
specify SEED to reproduce the shuffling from a previous run
  --random=5738`)
	flagSet.Lookup(prefix + "random").NoOptDefVal = "-1"
}
```

## File: `internal/flags/flags_test.go`
```go
package flags_test

import (
	"testing"

	"github.com/spf13/pflag"
	"github.com/stretchr/testify/assert"

	"github.com/cucumber/godog/internal/flags"
)

func Test_BindFlagsShouldRespectFlagDefaults(t *testing.T) {
	opts := flags.Options{}
	flagSet := pflag.FlagSet{}

	flags.BindRunCmdFlags("optDefaults.", &flagSet, &opts)

	flagSet.Parse([]string{})

	assert.Equal(t, "pretty", opts.Format)
	assert.Equal(t, "", opts.Tags)
	assert.Equal(t, 1, opts.Concurrency)
	assert.False(t, opts.ShowStepDefinitions)
	assert.False(t, opts.StopOnFailure)
	assert.False(t, opts.Strict)
	assert.False(t, opts.NoColors)
	assert.Equal(t, int64(0), opts.Randomize)
}

func Test_BindFlagsShouldRespectFlagOverrides(t *testing.T) {
	opts := flags.Options{
		Format:              "progress",
		Tags:                "test",
		Concurrency:         2,
		ShowStepDefinitions: true,
		StopOnFailure:       true,
		Strict:              true,
		NoColors:            true,
		Randomize:           11,
	}
	flagSet := pflag.FlagSet{}

	flags.BindRunCmdFlags("optOverrides.", &flagSet, &opts)

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

	assert.Equal(t, "junit", opts.Format)
	assert.Equal(t, "test2", opts.Tags)
	assert.Equal(t, 3, opts.Concurrency)
	assert.False(t, opts.ShowStepDefinitions)
	assert.False(t, opts.StopOnFailure)
	assert.False(t, opts.Strict)
	assert.False(t, opts.NoColors)
	assert.Equal(t, int64(2), opts.Randomize)
}
```

## File: `internal/flags/options.go`
```go
package flags

import (
	"context"
	"io"
	"io/fs"
	"testing"
)

// Options are suite run options
// flags are mapped to these options.
//
// It can also be used together with godog.RunWithOptions
// to run test suite from go source directly
//
// See the flags for more details
type Options struct {
	// Print step definitions found and exit
	ShowStepDefinitions bool

	// Randomize, if not `0`, will be used to run scenarios in a random order.
	//
	// Randomizing scenario order is especially helpful for detecting
	// situations where you have state leaking between scenarios, which can
	// cause flickering or fragile tests.
	//
	// The default value of `0` means "do not randomize".
	//
	// The magic value of `-1` means "pick a random seed for me", and godog will
	// assign a seed on it's own during the `RunWithOptions` phase, similar to if
	// you specified `--random` on the command line.
	//
	// Any other value will be used as the random seed for shuffling. Re-using the
	// same seed will allow you to reproduce the shuffle order of a previous run
	// to isolate an error condition.
	Randomize int64

	// Stops on the first failure
	StopOnFailure bool

	// Fail suite when there are pending or undefined or ambiguous steps
	Strict bool

	// Forces ansi color stripping
	NoColors bool

	// Various filters for scenarios parsed
	// from feature files
	Tags string

	// Dialect to be used to parse feature files. If not set, default to "en".
	Dialect string

	// The formatter name
	Format string

	// Concurrency rate, not all formatters accepts this
	Concurrency int

	// All feature file paths
	Paths []string

	// Where it should print formatter output
	Output io.Writer

	// DefaultContext is used as initial context instead of context.Background().
	DefaultContext context.Context

	// TestingT runs scenarios as subtests.
	TestingT *testing.T

	// FeatureContents allows passing in each feature manually
	// where the contents of each feature is stored as a byte slice
	// in a map entry
	FeatureContents []Feature

	// FS allows passing in an `fs.FS` to read features from, such as an `embed.FS`
	// or os.DirFS(string).
	FS fs.FS

	// ShowHelp enables suite to show CLI flags usage help and exit.
	ShowHelp bool
}

type Feature struct {
	Name     string
	Contents []byte
}
```

## File: `internal/formatters/fmt.go`
```go
package formatters

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"runtime"
	"strconv"
	"strings"

	messages "github.com/cucumber/messages/go/v21"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/utils"
)

var (
	red    = colors.Red
	redb   = colors.Bold(colors.Red)
	green  = colors.Green
	blackb = colors.Bold(colors.Black)
	yellow = colors.Yellow
	cyan   = colors.Cyan
	cyanb  = colors.Bold(colors.Cyan)
	whiteb = colors.Bold(colors.White)
)

// repeats a space n times
var s = utils.S

var (
	passed    = models.Passed
	failed    = models.Failed
	skipped   = models.Skipped
	undefined = models.Undefined
	pending   = models.Pending
	ambiguous = models.Ambiguous
)

type sortFeaturesByName []*models.Feature

func (s sortFeaturesByName) Len() int           { return len(s) }
func (s sortFeaturesByName) Less(i, j int) bool { return s[i].Feature.Name < s[j].Feature.Name }
func (s sortFeaturesByName) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }

type sortPicklesByID []*messages.Pickle

func (s sortPicklesByID) Len() int { return len(s) }
func (s sortPicklesByID) Less(i, j int) bool {
	iID := mustConvertStringToInt(s[i].Id)
	jID := mustConvertStringToInt(s[j].Id)
	return iID < jID
}
func (s sortPicklesByID) Swap(i, j int) { s[i], s[j] = s[j], s[i] }

type sortPickleStepResultsByPickleStepID []models.PickleStepResult

func (s sortPickleStepResultsByPickleStepID) Len() int { return len(s) }
func (s sortPickleStepResultsByPickleStepID) Less(i, j int) bool {
	iID := mustConvertStringToInt(s[i].PickleStepID)
	jID := mustConvertStringToInt(s[j].PickleStepID)
	return iID < jID
}
func (s sortPickleStepResultsByPickleStepID) Swap(i, j int) { s[i], s[j] = s[j], s[i] }

func mustConvertStringToInt(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}

	return i
}

// DefinitionID ...
func DefinitionID(sd *models.StepDefinition) string {
	ptr := sd.HandlerValue.Pointer()
	f := runtime.FuncForPC(ptr)
	dir := filepath.Dir(sd.File)
	fn := strings.Replace(f.Name(), dir, "", -1)
	var parts []string
	for _, gr := range matchFuncDefRef.FindAllStringSubmatch(fn, -1) {
		parts = append(parts, strings.Trim(gr[1], "_."))
	}
	if len(parts) > 0 {
		// case when suite is a structure with methods
		fn = strings.Join(parts, ".")
	} else {
		// case when steps are just plain funcs
		fn = strings.Trim(fn, "_.")
	}

	if pkg := os.Getenv("GODOG_TESTED_PACKAGE"); len(pkg) > 0 {
		fn = strings.Replace(fn, pkg, "", 1)
		fn = strings.TrimLeft(fn, ".")
		fn = strings.Replace(fn, "..", ".", -1)
	}

	return fmt.Sprintf("%s:%d -> %s", filepath.Base(sd.File), sd.Line, fn)
}

var matchFuncDefRef = regexp.MustCompile(`\(([^\)]+)\)`)
```

## File: `internal/formatters/fmt_base.go`
```go
package formatters

import (
	"bytes"
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
	"strings"
	"sync"
	"unicode"

	messages "github.com/cucumber/messages/go/v21"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/formatters"
	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/storage"
	"github.com/cucumber/godog/internal/utils"
)

// BaseFormatterFunc implements the FormatterFunc for the base formatter.
func BaseFormatterFunc(suite string, out io.Writer) formatters.Formatter {
	return NewBase(suite, out)
}

// NewBase creates a new base formatter.
func NewBase(suite string, out io.Writer) *Base {
	return &Base{
		suiteName: suite,
		indent:    2,
		out:       out,
		Lock:      new(sync.Mutex),
	}
}

// Base is a base formatter.
type Base struct {
	suiteName string
	out       io.Writer
	indent    int

	Storage *storage.Storage
	Lock    *sync.Mutex
}

// SetStorage assigns gherkin data storage.
func (f *Base) SetStorage(st *storage.Storage) {
	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.Storage = st
}

// TestRunStarted is triggered on test start.
func (f *Base) TestRunStarted() {}

// Feature receives gherkin document.
func (f *Base) Feature(*messages.GherkinDocument, string, []byte) {}

// Pickle receives scenario.
func (f *Base) Pickle(*messages.Pickle) {}

// Defined receives step definition.
func (f *Base) Defined(*messages.Pickle, *messages.PickleStep, *formatters.StepDefinition) {
}

// Passed captures passed step.
func (f *Base) Passed(*messages.Pickle, *messages.PickleStep, *formatters.StepDefinition) {}

// Skipped captures skipped step.
func (f *Base) Skipped(*messages.Pickle, *messages.PickleStep, *formatters.StepDefinition) {
}

// Undefined captures undefined step.
func (f *Base) Undefined(*messages.Pickle, *messages.PickleStep, *formatters.StepDefinition) {
}

// Failed captures failed step.
func (f *Base) Failed(*messages.Pickle, *messages.PickleStep, *formatters.StepDefinition, error) {
}

// Pending captures pending step.
func (f *Base) Pending(*messages.Pickle, *messages.PickleStep, *formatters.StepDefinition) {
}

// Ambiguous captures ambiguous step.
func (f *Base) Ambiguous(*messages.Pickle, *messages.PickleStep, *formatters.StepDefinition, error) {
}

// Summary renders summary information.
func (f *Base) Summary() {
	var totalSc, passedSc, undefinedSc int
	var totalSt, passedSt, failedSt, skippedSt, pendingSt, undefinedSt, ambiguousSt int

	pickleResults := f.Storage.MustGetPickleResults()
	for _, pr := range pickleResults {
		var prStatus models.StepResultStatus
		totalSc++

		pickleStepResults := f.Storage.MustGetPickleStepResultsByPickleID(pr.PickleID)

		if len(pickleStepResults) == 0 {
			prStatus = undefined
		}

		for _, sr := range pickleStepResults {
			totalSt++

			switch sr.Status {
			case passed:
				passedSt++
			case failed:
				prStatus = failed
				failedSt++
			case ambiguous:
				prStatus = ambiguous
				ambiguousSt++
			case skipped:
				skippedSt++
			case undefined:
				prStatus = undefined
				undefinedSt++
			case pending:
				prStatus = pending
				pendingSt++
			}
		}

		if prStatus == passed {
			passedSc++
		} else if prStatus == undefined {
			undefinedSc++
		}
	}

	var steps, parts, scenarios []string
	if passedSt > 0 {
		steps = append(steps, green(fmt.Sprintf("%d passed", passedSt)))
	}
	if failedSt > 0 {
		parts = append(parts, red(fmt.Sprintf("%d failed", failedSt)))
		steps = append(steps, red(fmt.Sprintf("%d failed", failedSt)))
	}
	if pendingSt > 0 {
		parts = append(parts, yellow(fmt.Sprintf("%d pending", pendingSt)))
		steps = append(steps, yellow(fmt.Sprintf("%d pending", pendingSt)))
	}
	if ambiguousSt > 0 {
		parts = append(parts, yellow(fmt.Sprintf("%d ambiguous", ambiguousSt)))
		steps = append(steps, yellow(fmt.Sprintf("%d ambiguous", ambiguousSt)))
	}
	if undefinedSt > 0 {
		parts = append(parts, yellow(fmt.Sprintf("%d undefined", undefinedSc)))
		steps = append(steps, yellow(fmt.Sprintf("%d undefined", undefinedSt)))
	} else if undefinedSc > 0 {
		// there may be some scenarios without steps
		parts = append(parts, yellow(fmt.Sprintf("%d undefined", undefinedSc)))
	}
	if skippedSt > 0 {
		steps = append(steps, cyan(fmt.Sprintf("%d skipped", skippedSt)))
	}
	if passedSc > 0 {
		scenarios = append(scenarios, green(fmt.Sprintf("%d passed", passedSc)))
	}
	scenarios = append(scenarios, parts...)

	testRunStartedAt := f.Storage.MustGetTestRunStarted().StartedAt
	elapsed := utils.TimeNowFunc().Sub(testRunStartedAt)

	fmt.Fprintln(f.out, "")

	if totalSc == 0 {
		fmt.Fprintln(f.out, "No scenarios")
	} else {
		fmt.Fprintf(f.out, "%d scenarios (%s)\n", totalSc, strings.Join(scenarios, ", "))
	}

	if totalSt == 0 {
		fmt.Fprintln(f.out, "No steps")
	} else {
		fmt.Fprintf(f.out, "%d steps (%s)\n", totalSt, strings.Join(steps, ", "))
	}

	elapsedString := elapsed.String()
	if elapsed.Nanoseconds() == 0 {
		// go 1.5 and 1.6 prints 0 instead of 0s, if duration is zero.
		elapsedString = "0s"
	}
	fmt.Fprintln(f.out, elapsedString)

	// prints used randomization seed
	seed, err := strconv.ParseInt(os.Getenv("GODOG_SEED"), 10, 64)
	if err == nil && seed != 0 {
		fmt.Fprintln(f.out, "")
		fmt.Fprintln(f.out, "Randomized with seed:", colors.Yellow(seed))
	}

	if text := f.Snippets(); text != "" {
		fmt.Fprintln(f.out, "")
		fmt.Fprintln(f.out, yellow("You can implement step definitions for undefined steps with these snippets:"))
		fmt.Fprintln(f.out, yellow(text))
	}
}

// Snippets returns code suggestions for undefined steps.
func (f *Base) Snippets() string {
	undefinedStepResults := f.Storage.MustGetPickleStepResultsByStatus(undefined)
	if len(undefinedStepResults) == 0 {
		return ""
	}

	var index int
	var snips []undefinedSnippet
	// build snippets
	for _, u := range undefinedStepResults {
		pickleStep := f.Storage.MustGetPickleStep(u.PickleStepID)

		steps := []string{pickleStep.Text}
		arg := pickleStep.Argument
		if u.Def != nil {
			steps = u.Def.Undefined
			arg = nil
		}
		for _, step := range steps {
			expr := snippetExprCleanup.ReplaceAllString(step, "\\$1")
			expr = snippetNumbers.ReplaceAllString(expr, "(\\d+)")
			expr = snippetExprQuoted.ReplaceAllString(expr, "$1\"([^\"]*)\"$2")
			expr = "^" + strings.TrimSpace(expr) + "$"

			name := snippetNumbers.ReplaceAllString(step, " ")
			name = snippetExprQuoted.ReplaceAllString(name, " ")
			name = strings.TrimSpace(snippetMethodName.ReplaceAllString(name, ""))
			var words []string
			for i, w := range strings.Split(name, " ") {
				switch {
				case i != 0:
					w = strings.Title(w)
				case len(w) > 0:
					w = string(unicode.ToLower(rune(w[0]))) + w[1:]
				}
				words = append(words, w)
			}
			name = strings.Join(words, "")
			if len(name) == 0 {
				index++
				name = fmt.Sprintf("StepDefinitioninition%d", index)
			}

			var found bool
			for _, snip := range snips {
				if snip.Expr == expr {
					found = true
					break
				}
			}
			if !found {
				snips = append(snips, undefinedSnippet{Method: name, Expr: expr, argument: arg})
			}
		}
	}

	sort.Sort(snippetSortByMethod(snips))

	var buf bytes.Buffer
	if err := undefinedSnippetsTpl.Execute(&buf, snips); err != nil {
		panic(err)
	}
	// there may be trailing spaces
	return strings.Replace(buf.String(), " \n", "\n", -1)
}
```

## File: `internal/formatters/fmt_base_test.go`
```go
package formatters_test

import (
	"bytes"
	"context"
	"errors"
	"fmt"
	"testing"

	"github.com/cucumber/godog"
	"github.com/cucumber/godog/internal/flags"
	"github.com/stretchr/testify/assert"
)

func TestBase_Summary(t *testing.T) {
	var features []flags.Feature

	features = append(features,
		flags.Feature{Name: "f1", Contents: []byte(`
Feature: f1

Scenario: f1s1
When step passed f1s1:1
Then step failed f1s1:2
`)},
		flags.Feature{Name: "f2", Contents: []byte(`
Feature: f2

Scenario: f2s1
When step passed f2s1:1
Then step passed f2s1:2

Scenario: f2s2
When step failed f2s2:1
Then step passed f2s2:2

Scenario: f2s3
When step passed f2s3:1
Then step skipped f2s3:2
And step passed f2s3:3
And step failed f2s3:4

Scenario: f2s4
When step passed f2s4:1
Then something unknown happens f2s4:2
And step passed f2s4:3
`)},
	)

	out := bytes.NewBuffer(nil)
	suite := godog.TestSuite{
		ScenarioInitializer: func(sc *godog.ScenarioContext) {
			sc.After(func(ctx context.Context, sc *godog.Scenario, err error) (context.Context, error) {
				if err != nil {
					_, _ = out.WriteString(fmt.Sprintf("scenario %q ended with error %q\n", sc.Name, err.Error()))
				} else {
					_, _ = out.WriteString(fmt.Sprintf("scenario %q passed\n", sc.Name))
				}

				return ctx, nil
			})
			sc.StepContext().After(func(ctx context.Context, st *godog.Step, status godog.StepResultStatus, err error) (context.Context, error) {
				_, _ = out.WriteString(fmt.Sprintf("step %q finished with status %s\n", st.Text, status.String()))
				return ctx, nil
			})
			sc.Step("failed (.+)", func(s string) error {
				_, _ = out.WriteString(fmt.Sprintf("\nstep invoked: %q, failed\n", s))
				return errors.New("failed")
			})
			sc.Step("skipped (.+)", func(s string) error {
				_, _ = out.WriteString(fmt.Sprintf("\nstep invoked: %q, skipped\n", s))
				return godog.ErrSkip
			})
			sc.Step("passed (.+)", func(s string) {
				_, _ = out.WriteString(fmt.Sprintf("\nstep invoked: %q, passed\n", s))
			})
		},
		Options: &godog.Options{
			Output:          out,
			NoColors:        true,
			Strict:          true,
			Format:          "progress",
			FeatureContents: features,
		},
	}

	assert.Equal(t, 1, suite.Run())
	assert.Equal(t, `
step invoked: "f1s1:1", passed
step "step passed f1s1:1" finished with status passed
.
step invoked: "f1s1:2", failed
step "step failed f1s1:2" finished with status failed
scenario "f1s1" ended with error "failed"
F
step invoked: "f2s1:1", passed
step "step passed f2s1:1" finished with status passed
.
step invoked: "f2s1:2", passed
step "step passed f2s1:2" finished with status passed
scenario "f2s1" passed
.
step invoked: "f2s2:1", failed
step "step failed f2s2:1" finished with status failed
scenario "f2s2" ended with error "failed"
F-step "step passed f2s2:2" finished with status skipped

step invoked: "f2s3:1", passed
step "step passed f2s3:1" finished with status passed
.
step invoked: "f2s3:2", skipped
step "step skipped f2s3:2" finished with status skipped
--step "step passed f2s3:3" finished with status skipped
-step "step failed f2s3:4" finished with status skipped
scenario "f2s3" passed

step invoked: "f2s4:1", passed
step "step passed f2s4:1" finished with status passed
.Ustep "something unknown happens f2s4:2" finished with status undefined
scenario "f2s4" ended with error "step is undefined: something unknown happens f2s4:2"
-step "step passed f2s4:3" finished with status skipped
 13


--- Failed steps:

  Scenario: f1s1 # f1:4
    Then step failed f1s1:2 # f1:6
      Error: failed

  Scenario: f2s2 # f2:8
    When step failed f2s2:1 # f2:9
      Error: failed


5 scenarios (2 passed, 2 failed, 1 undefined)
13 steps (5 passed, 2 failed, 1 undefined, 5 skipped)
0s

You can implement step definitions for undefined steps with these snippets:

func somethingUnknownHappensFS(arg1, arg2, arg3 int) error {
	return godog.ErrPending
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Step(`+"`"+`^something unknown happens f(\d+)s(\d+):(\d+)$`+"`"+`, somethingUnknownHappensFS)
}

`, out.String())
}
```

## File: `internal/formatters/fmt_color_tag_test.go`
```go
package formatters_test

import (
	"bytes"
	"fmt"
	"io"
	"strings"
	"testing"

	"github.com/cucumber/godog/colors"
)

type csiState int

const (
	outsideCsiCode csiState = iota
	firstCsiCode
	secondCsiCode
)

type tagColorWriter struct {
	w             io.Writer
	state         csiState
	paramStartBuf bytes.Buffer
	paramBuf      bytes.Buffer
	tag           string
}

const (
	firstCsiChar   byte = '\x1b'
	secondeCsiChar byte = '['
	separatorChar  byte = ';'
	sgrCode        byte = 'm'
)

const (
	ansiReset        = "0"
	ansiIntensityOn  = "1"
	ansiIntensityOff = "21"
	ansiUnderlineOn  = "4"
	ansiUnderlineOff = "24"
	ansiBlinkOn      = "5"
	ansiBlinkOff     = "25"

	ansiForegroundBlack   = "30"
	ansiForegroundRed     = "31"
	ansiForegroundGreen   = "32"
	ansiForegroundYellow  = "33"
	ansiForegroundBlue    = "34"
	ansiForegroundMagenta = "35"
	ansiForegroundCyan    = "36"
	ansiForegroundWhite   = "37"
	ansiForegroundDefault = "39"
)

var colorMap = map[string]string{
	ansiForegroundBlack:   "black",
	ansiForegroundRed:     "red",
	ansiForegroundGreen:   "green",
	ansiForegroundYellow:  "yellow",
	ansiForegroundBlue:    "blue",
	ansiForegroundMagenta: "magenta",
	ansiForegroundCyan:    "cyan",
	ansiForegroundWhite:   "white",
	ansiForegroundDefault: "",
}

func (cw *tagColorWriter) resetBuffer() (int, error) {
	return cw.flushTo(nil)
}

func (cw *tagColorWriter) flushTo(w io.Writer) (int, error) {
	var n1, n2 int
	var err error

	startBytes := cw.paramStartBuf.Bytes()
	cw.paramStartBuf.Reset()
	if w != nil {
		n1, err = cw.w.Write(startBytes)
		if err != nil {
			return n1, err
		}
	} else {
		n1 = len(startBytes)
	}
	paramBytes := cw.paramBuf.Bytes()
	cw.paramBuf.Reset()
	if w != nil {
		n2, err = cw.w.Write(paramBytes)
		if err != nil {
			return n1 + n2, err
		}
	} else {
		n2 = len(paramBytes)
	}
	return n1 + n2, nil
}

func isParameterChar(b byte) bool {
	return ('0' <= b && b <= '9') || b == separatorChar
}

func (cw *tagColorWriter) Write(p []byte) (int, error) {
	r, nw, first, last := 0, 0, 0, 0

	var err error
	for i, ch := range p {
		switch cw.state {
		case outsideCsiCode:
			if ch == firstCsiChar {
				cw.paramStartBuf.WriteByte(ch)
				cw.state = firstCsiCode
			}
		case firstCsiCode:
			switch ch {
			case firstCsiChar:
				cw.paramStartBuf.WriteByte(ch)
			case secondeCsiChar:
				cw.paramStartBuf.WriteByte(ch)
				cw.state = secondCsiCode
				last = i - 1
			default:
				cw.resetBuffer()
				cw.state = outsideCsiCode
			}
		case secondCsiCode:
			if isParameterChar(ch) {
				cw.paramBuf.WriteByte(ch)
			} else {
				nw, err = cw.w.Write(p[first:last])
				r += nw
				if err != nil {
					return r, err
				}
				first = i + 1
				if ch == sgrCode {
					cw.changeColor()
				}
				n, _ := cw.resetBuffer()
				// Add one more to the size of the buffer for the last ch
				r += n + 1

				cw.state = outsideCsiCode
			}
		default:
			cw.state = outsideCsiCode
		}
	}

	if cw.state == outsideCsiCode {
		nw, err = cw.w.Write(p[first:])
		r += nw
	}

	return r, err
}

func (cw *tagColorWriter) changeColor() {
	strParam := cw.paramBuf.String()
	if len(strParam) <= 0 {
		strParam = "0"
	}
	csiParam := strings.Split(strParam, string(separatorChar))
	for _, p := range csiParam {
		c, ok := colorMap[p]
		switch {
		case !ok:
			switch p {
			case ansiReset:
				fmt.Fprint(cw.w, "</"+cw.tag+">")
				cw.tag = ""
			case ansiIntensityOn:
				cw.tag = "bold-" + cw.tag
			case ansiIntensityOff:
			case ansiUnderlineOn:
			case ansiUnderlineOff:
			case ansiBlinkOn:
			case ansiBlinkOff:
			default:
				// unknown code
			}
		default:
			cw.tag += c
			fmt.Fprint(cw.w, "<"+cw.tag+">")
		}
	}
}

func TestTagColorWriter(t *testing.T) {
	var buf bytes.Buffer
	w := &tagColorWriter{w: &buf}

	s := fmt.Sprintf("text %s then %s", colors.Red("in red"), colors.Yellow("yel"))
	fmt.Fprint(w, s)

	expected := "text <red>in red</red> then <yellow>yel</yellow>"
	if buf.String() != expected {
		t.Fatalf("expected `%s` but got `%s`", expected, buf.String())
	}
}

func TestTagBoldColorWriter(t *testing.T) {
	var buf bytes.Buffer
	w := &tagColorWriter{w: &buf}

	s := fmt.Sprintf(
		"text %s then %s",
		colors.Bold(colors.Red)("in red"),
		colors.Bold(colors.Yellow)("yel"),
	)
	fmt.Fprint(w, s)

	expected := "text <bold-red>in red</bold-red> then <bold-yellow>yel</bold-yellow>"
	if buf.String() != expected {
		t.Fatalf("expected `%s` but got `%s`", expected, buf.String())
	}
}
```

## File: `internal/formatters/fmt_cucumber.go`
```go
package formatters

/*
   The specification for the formatting originated from https://www.relishapp.com/cucumber/cucumber/brain/knowledge/docs_legacy/formatters/json-output-formatter.
   I found that documentation was misleading or out dated.  To validate formatting I create a ruby cucumber test harness and ran the
   same feature files through godog and the ruby cucumber.

   The docstrings in the cucumber.feature represent the cucumber output for those same feature definitions.

   I did note that comments in ruby could be at just about any level in particular Feature, Scenario and Step.  In godog I
   could only find comments under the Feature data structure.
*/

import (
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"sort"
	"strings"

	"github.com/cucumber/godog/formatters"
	"github.com/cucumber/godog/internal/models"
	messages "github.com/cucumber/messages/go/v21"
)

func init() {
	formatters.Format("cucumber", "Produces cucumber JSON format output.", CucumberFormatterFunc)
}

// CucumberFormatterFunc implements the FormatterFunc for the cucumber formatter
func CucumberFormatterFunc(suite string, out io.Writer) formatters.Formatter {
	return &Cuke{Base: NewBase(suite, out)}
}

// Cuke ...
type Cuke struct {
	*Base
}

// Summary renders test result as Cucumber JSON.
func (f *Cuke) Summary() {
	features := f.Storage.MustGetFeatures()

	res := f.buildCukeFeatures(features)

	dat, err := json.MarshalIndent(res, "", "    ")
	if err != nil {
		panic(err)
	}

	fmt.Fprintf(f.out, "%s\n", string(dat))
}

func (f *Cuke) buildCukeFeatures(features []*models.Feature) (res []CukeFeatureJSON) {
	sort.Sort(sortFeaturesByName(features))

	res = make([]CukeFeatureJSON, len(features))

	for idx, feat := range features {
		cukeFeature := buildCukeFeature(feat)

		pickles := f.Storage.MustGetPickles(feat.Uri)
		sort.Sort(sortPicklesByID(pickles))

		cukeFeature.Elements = f.buildCukeElements(pickles)

		for jdx, elem := range cukeFeature.Elements {
			elem.ID = cukeFeature.ID + ";" + makeCukeID(elem.Name) + elem.ID
			elem.Tags = append(cukeFeature.Tags, elem.Tags...)
			cukeFeature.Elements[jdx] = elem
		}

		res[idx] = cukeFeature
	}

	return res
}

func (f *Cuke) buildCukeElements(pickles []*messages.Pickle) (res []cukeElement) {
	res = make([]cukeElement, len(pickles))

	for idx, pickle := range pickles {
		pickleResult := f.Storage.MustGetPickleResult(pickle.Id)
		pickleStepResults := f.Storage.MustGetPickleStepResultsByPickleID(pickle.Id)

		cukeElement := f.buildCukeElement(pickle)

		stepStartedAt := pickleResult.StartedAt

		cukeElement.Steps = make([]cukeStep, len(pickleStepResults))
		sort.Sort(sortPickleStepResultsByPickleStepID(pickleStepResults))

		for jdx, stepResult := range pickleStepResults {
			cukeStep := f.buildCukeStep(pickle, stepResult)

			stepResultFinishedAt := stepResult.FinishedAt
			d := int(stepResultFinishedAt.Sub(stepStartedAt).Nanoseconds())
			stepStartedAt = stepResultFinishedAt

			cukeStep.Result.Duration = &d
			if stepResult.Status == undefined ||
				stepResult.Status == pending ||
				stepResult.Status == skipped ||
				stepResult.Status == ambiguous {
				cukeStep.Result.Duration = nil
			}

			cukeElement.Steps[jdx] = cukeStep
		}

		res[idx] = cukeElement
	}

	return res
}

type cukeComment struct {
	Value string `json:"value"`
	Line  int    `json:"line"`
}

type cukeDocstring struct {
	Value       string `json:"value"`
	ContentType string `json:"content_type"`
	Line        int    `json:"line"`
}

type cukeTag struct {
	Name string `json:"name"`
	Line int    `json:"line"`
}

type cukeResult struct {
	Status   string `json:"status"`
	Error    string `json:"error_message,omitempty"`
	Duration *int   `json:"duration,omitempty"`
}

type cukeMatch struct {
	Location string `json:"location"`
}

type cukeEmbedding struct {
	Name     string `json:"name"`
	MimeType string `json:"mime_type"`
	Data     string `json:"data"`
}

type cukeStep struct {
	Keyword    string              `json:"keyword"`
	Name       string              `json:"name"`
	Line       int                 `json:"line"`
	Docstring  *cukeDocstring      `json:"doc_string,omitempty"`
	Match      cukeMatch           `json:"match"`
	Result     cukeResult          `json:"result"`
	DataTable  []*cukeDataTableRow `json:"rows,omitempty"`
	Embeddings []cukeEmbedding     `json:"embeddings,omitempty"`
}

type cukeDataTableRow struct {
	Cells []string `json:"cells"`
}

type cukeElement struct {
	ID          string     `json:"id"`
	Keyword     string     `json:"keyword"`
	Name        string     `json:"name"`
	Description string     `json:"description"`
	Line        int        `json:"line"`
	Type        string     `json:"type"`
	Tags        []cukeTag  `json:"tags,omitempty"`
	Steps       []cukeStep `json:"steps,omitempty"`
}

// CukeFeatureJSON ...
type CukeFeatureJSON struct {
	URI         string        `json:"uri"`
	ID          string        `json:"id"`
	Keyword     string        `json:"keyword"`
	Name        string        `json:"name"`
	Description string        `json:"description"`
	Line        int           `json:"line"`
	Comments    []cukeComment `json:"comments,omitempty"`
	Tags        []cukeTag     `json:"tags,omitempty"`
	Elements    []cukeElement `json:"elements,omitempty"`
}

func buildCukeFeature(feat *models.Feature) CukeFeatureJSON {
	cukeFeature := CukeFeatureJSON{
		URI:         feat.Uri,
		ID:          makeCukeID(feat.Feature.Name),
		Keyword:     feat.Feature.Keyword,
		Name:        feat.Feature.Name,
		Description: feat.Feature.Description,
		Line:        int(feat.Feature.Location.Line),
		Comments:    make([]cukeComment, len(feat.Comments)),
		Tags:        make([]cukeTag, len(feat.Feature.Tags)),
	}

	for idx, element := range feat.Feature.Tags {
		cukeFeature.Tags[idx].Line = int(element.Location.Line)
		cukeFeature.Tags[idx].Name = element.Name
	}

	for idx, comment := range feat.Comments {
		cukeFeature.Comments[idx].Value = strings.TrimSpace(comment.Text)
		cukeFeature.Comments[idx].Line = int(comment.Location.Line)
	}

	return cukeFeature
}

func (f *Cuke) buildCukeElement(pickle *messages.Pickle) (cukeElement cukeElement) {
	feature := f.Storage.MustGetFeature(pickle.Uri)
	scenario := feature.FindScenario(pickle.AstNodeIds[0])

	cukeElement.Name = pickle.Name
	cukeElement.Line = int(scenario.Location.Line)
	cukeElement.Description = scenario.Description
	cukeElement.Keyword = scenario.Keyword
	cukeElement.Type = "scenario"

	cukeElement.Tags = make([]cukeTag, len(scenario.Tags))
	for idx, element := range scenario.Tags {
		cukeElement.Tags[idx].Line = int(element.Location.Line)
		cukeElement.Tags[idx].Name = element.Name
	}

	if len(pickle.AstNodeIds) == 1 {
		return
	}

	example, _ := feature.FindExample(pickle.AstNodeIds[1])

	for _, tag := range example.Tags {
		tag := cukeTag{Line: int(tag.Location.Line), Name: tag.Name}
		cukeElement.Tags = append(cukeElement.Tags, tag)
	}

	examples := scenario.Examples
	if len(examples) > 0 {
		rowID := pickle.AstNodeIds[1]

		for _, example := range examples {
			for idx, row := range example.TableBody {
				if rowID == row.Id {
					cukeElement.ID += fmt.Sprintf(";%s;%d", makeCukeID(example.Name), idx+2)
					cukeElement.Line = int(row.Location.Line)
				}
			}
		}
	}

	return cukeElement
}

func (f *Cuke) buildCukeStep(pickle *messages.Pickle, stepResult models.PickleStepResult) (cukeStep cukeStep) {
	feature := f.Storage.MustGetFeature(pickle.Uri)
	pickleStep := f.Storage.MustGetPickleStep(stepResult.PickleStepID)
	step := feature.FindStep(pickleStep.AstNodeIds[0])

	line := step.Location.Line

	cukeStep.Name = pickleStep.Text
	cukeStep.Line = int(line)
	cukeStep.Keyword = step.Keyword

	arg := pickleStep.Argument

	if arg != nil {
		if arg.DocString != nil && step.DocString != nil {
			cukeStep.Docstring = &cukeDocstring{}
			cukeStep.Docstring.ContentType = strings.TrimSpace(arg.DocString.MediaType)
			if step.Location != nil {
				cukeStep.Docstring.Line = int(step.DocString.Location.Line)
			}
			cukeStep.Docstring.Value = arg.DocString.Content
		}

		if arg.DataTable != nil {
			cukeStep.DataTable = make([]*cukeDataTableRow, len(arg.DataTable.Rows))
			for i, row := range arg.DataTable.Rows {
				cells := make([]string, len(row.Cells))
				for j, cell := range row.Cells {
					cells[j] = cell.Value
				}
				cukeStep.DataTable[i] = &cukeDataTableRow{Cells: cells}
			}
		}
	}

	if stepResult.Def != nil {
		cukeStep.Match.Location = strings.Split(DefinitionID(stepResult.Def), " ")[0]
	}

	cukeStep.Result.Status = stepResult.Status.String()
	if stepResult.Err != nil {
		cukeStep.Result.Error = stepResult.Err.Error()
	}

	if stepResult.Status == undefined || stepResult.Status == pending || stepResult.Status == ambiguous {
		cukeStep.Match.Location = fmt.Sprintf("%s:%d", pickle.Uri, step.Location.Line)
	}

	if stepResult.Attachments != nil {
		attachments := []cukeEmbedding{}

		for _, a := range stepResult.Attachments {
			attachments = append(attachments, cukeEmbedding{
				Name:     a.Name,
				Data:     base64.StdEncoding.EncodeToString(a.Data),
				MimeType: a.MimeType,
			})
		}

		if len(attachments) > 0 {
			cukeStep.Embeddings = attachments
		}
	}
	return cukeStep
}

func makeCukeID(name string) string {
	return strings.Replace(strings.ToLower(name), " ", "-", -1)
}
```

## File: `internal/formatters/fmt_events.go`
```go
package formatters

import (
	"encoding/json"
	"fmt"
	"io"

	"github.com/cucumber/godog/formatters"
	"github.com/cucumber/godog/internal/utils"
	messages "github.com/cucumber/messages/go/v21"
)

const nanoSec = 1000000
const spec = "0.1.0"

func init() {
	formatters.Format("events", fmt.Sprintf("Produces JSON event stream, based on spec: %s.", spec), EventsFormatterFunc)
}

// EventsFormatterFunc implements the FormatterFunc for the events formatter
func EventsFormatterFunc(suite string, out io.Writer) formatters.Formatter {
	return &Events{Base: NewBase(suite, out)}
}

// Events - Events formatter
type Events struct {
	*Base
}

func (f *Events) event(ev interface{}) {
	data, err := json.Marshal(ev)
	if err != nil {
		panic(fmt.Sprintf("failed to marshal stream event: %+v - %v", ev, err))
	}
	fmt.Fprintln(f.out, string(data))
}

// Pickle receives scenario.
func (f *Events) Pickle(pickle *messages.Pickle) {
	f.Base.Pickle(pickle)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.event(&struct {
		Event     string `json:"event"`
		Location  string `json:"location"`
		Timestamp int64  `json:"timestamp"`
	}{
		"TestCaseStarted",
		f.scenarioLocation(pickle),
		utils.TimeNowFunc().UnixNano() / nanoSec,
	})

	if len(pickle.Steps) == 0 {
		// @TODO: is status undefined or passed? when there are no steps
		// for this scenario
		f.event(&struct {
			Event     string `json:"event"`
			Location  string `json:"location"`
			Timestamp int64  `json:"timestamp"`
			Status    string `json:"status"`
		}{
			"TestCaseFinished",
			f.scenarioLocation(pickle),
			utils.TimeNowFunc().UnixNano() / nanoSec,
			"undefined",
		})
	}
}

// TestRunStarted is triggered on test start.
func (f *Events) TestRunStarted() {
	f.Base.TestRunStarted()

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.event(&struct {
		Event     string `json:"event"`
		Version   string `json:"version"`
		Timestamp int64  `json:"timestamp"`
		Suite     string `json:"suite"`
	}{
		"TestRunStarted",
		spec,
		utils.TimeNowFunc().UnixNano() / nanoSec,
		f.suiteName,
	})
}

// Feature receives gherkin document.
func (f *Events) Feature(ft *messages.GherkinDocument, p string, c []byte) {
	f.Base.Feature(ft, p, c)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.event(&struct {
		Event    string `json:"event"`
		Location string `json:"location"`
		Source   string `json:"source"`
	}{
		"TestSource",
		fmt.Sprintf("%s:%d", p, ft.Feature.Location.Line),
		string(c),
	})
}

// Summary pushes summary information to JSON stream.
func (f *Events) Summary() {
	// @TODO: determine status
	status := passed

	f.Storage.MustGetPickleStepResultsByStatus(failed)

	if len(f.Storage.MustGetPickleStepResultsByStatus(failed)) > 0 {
		status = failed
	} else if len(f.Storage.MustGetPickleStepResultsByStatus(passed)) == 0 {
		if len(f.Storage.MustGetPickleStepResultsByStatus(undefined)) > len(f.Storage.MustGetPickleStepResultsByStatus(pending)) {
			status = undefined
		} else {
			status = pending
		}
	}

	snips := f.Snippets()
	if len(snips) > 0 {
		snips = "You can implement step definitions for undefined steps with these snippets:\n" + snips
	}

	f.event(&struct {
		Event     string `json:"event"`
		Status    string `json:"status"`
		Timestamp int64  `json:"timestamp"`
		Snippets  string `json:"snippets"`
		Memory    string `json:"memory"`
	}{
		"TestRunFinished",
		status.String(),
		utils.TimeNowFunc().UnixNano() / nanoSec,
		snips,
		"", // @TODO not sure that could be correctly implemented
	})
}

func (f *Events) step(pickle *messages.Pickle, pickleStep *messages.PickleStep) {
	feature := f.Storage.MustGetFeature(pickle.Uri)
	pickleStepResult := f.Storage.MustGetPickleStepResult(pickleStep.Id)
	step := feature.FindStep(pickleStep.AstNodeIds[0])

	var errMsg string
	if pickleStepResult.Err != nil {
		errMsg = pickleStepResult.Err.Error()
	}

	if pickleStepResult.Attachments != nil {
		for _, attachment := range pickleStepResult.Attachments {

			f.event(&struct {
				Event           string `json:"event"`
				Location        string `json:"location"`
				Timestamp       int64  `json:"timestamp"`
				ContentEncoding string `json:"contentEncoding"`
				FileName        string `json:"fileName"`
				MimeType        string `json:"mimeType"`
				Body            string `json:"body"`
			}{
				"Attachment",
				fmt.Sprintf("%s:%d", pickle.Uri, step.Location.Line),
				utils.TimeNowFunc().UnixNano() / nanoSec,
				messages.AttachmentContentEncoding_BASE64.String(),
				attachment.Name,
				attachment.MimeType,
				string(attachment.Data),
			})

		}
	}

	f.event(&struct {
		Event     string `json:"event"`
		Location  string `json:"location"`
		Timestamp int64  `json:"timestamp"`
		Status    string `json:"status"`
		Summary   string `json:"summary,omitempty"`
	}{
		"TestStepFinished",
		fmt.Sprintf("%s:%d", pickle.Uri, step.Location.Line),
		utils.TimeNowFunc().UnixNano() / nanoSec,
		pickleStepResult.Status.String(),
		errMsg,
	})

	if isLastStep(pickle, pickleStep) {
		var status string

		pickleStepResults := f.Storage.MustGetPickleStepResultsByPickleID(pickle.Id)
		for _, stepResult := range pickleStepResults {
			switch stepResult.Status {
			case passed, failed, undefined, pending, ambiguous:
				status = stepResult.Status.String()
			}
		}

		f.event(&struct {
			Event     string `json:"event"`
			Location  string `json:"location"`
			Timestamp int64  `json:"timestamp"`
			Status    string `json:"status"`
		}{
			"TestCaseFinished",
			f.scenarioLocation(pickle),
			utils.TimeNowFunc().UnixNano() / nanoSec,
			status,
		})
	}
}

// Defined receives step definition.
func (f *Events) Defined(pickle *messages.Pickle, pickleStep *messages.PickleStep, def *formatters.StepDefinition) {
	f.Base.Defined(pickle, pickleStep, def)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	feature := f.Storage.MustGetFeature(pickle.Uri)
	step := feature.FindStep(pickleStep.AstNodeIds[0])

	if def != nil {
		matchedDef := f.Storage.MustGetStepDefintionMatch(pickleStep.AstNodeIds[0])

		m := def.Expr.FindStringSubmatchIndex(pickleStep.Text)[2:]
		var args [][2]int
		for i := 0; i < len(m)/2; i++ {
			pair := m[i : i*2+2]
			var idxs [2]int
			idxs[0] = pair[0]
			idxs[1] = pair[1]
			args = append(args, idxs)
		}

		if len(args) == 0 {
			args = make([][2]int, 0)
		}

		f.event(&struct {
			Event    string   `json:"event"`
			Location string   `json:"location"`
			DefID    string   `json:"definition_id"`
			Args     [][2]int `json:"arguments"`
		}{
			"StepDefinitionFound",
			fmt.Sprintf("%s:%d", pickle.Uri, step.Location.Line),
			DefinitionID(matchedDef),
			args,
		})
	}

	f.event(&struct {
		Event     string `json:"event"`
		Location  string `json:"location"`
		Timestamp int64  `json:"timestamp"`
	}{
		"TestStepStarted",
		fmt.Sprintf("%s:%d", pickle.Uri, step.Location.Line),
		utils.TimeNowFunc().UnixNano() / nanoSec,
	})
}

// Passed captures passed step.
func (f *Events) Passed(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Passed(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(pickle, step)
}

// Skipped captures skipped step.
func (f *Events) Skipped(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Skipped(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(pickle, step)
}

// Undefined captures undefined step.
func (f *Events) Undefined(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Undefined(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(pickle, step)
}

// Failed captures failed step.
func (f *Events) Failed(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition, err error) {
	f.Base.Failed(pickle, step, match, err)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(pickle, step)
}

// Pending captures pending step.
func (f *Events) Pending(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Pending(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(pickle, step)
}

// Ambiguous captures ambiguous step.
func (f *Events) Ambiguous(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition, err error) {
	f.Base.Ambiguous(pickle, step, match, err)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(pickle, step)
}

func (f *Events) scenarioLocation(pickle *messages.Pickle) string {
	feature := f.Storage.MustGetFeature(pickle.Uri)
	scenario := feature.FindScenario(pickle.AstNodeIds[0])

	line := scenario.Location.Line
	if len(pickle.AstNodeIds) == 2 {
		_, row := feature.FindExample(pickle.AstNodeIds[1])
		line = row.Location.Line
	}

	return fmt.Sprintf("%s:%d", pickle.Uri, line)
}

func isLastStep(pickle *messages.Pickle, step *messages.PickleStep) bool {
	return pickle.Steps[len(pickle.Steps)-1].Id == step.Id
}
```

## File: `internal/formatters/fmt_flushwrap.go`
```go
package formatters

import (
	"sync"

	"github.com/cucumber/godog/formatters"
	messages "github.com/cucumber/messages/go/v21"
)

// WrapOnFlush wrap a `formatters.Formatter` in a `formatters.FlushFormatter`, which only
// executes when `Flush` is called
func WrapOnFlush(fmt formatters.Formatter) formatters.FlushFormatter {
	return &onFlushFormatter{
		fmt: fmt,
		fns: make([]func(), 0),
		mu:  &sync.Mutex{},
	}
}

type onFlushFormatter struct {
	fmt formatters.Formatter
	fns []func()
	mu  *sync.Mutex
}

func (o *onFlushFormatter) Pickle(pickle *messages.Pickle) {
	o.fns = append(o.fns, func() {
		o.fmt.Pickle(pickle)
	})
}

func (o *onFlushFormatter) Passed(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition) {
	o.fns = append(o.fns, func() {
		o.fmt.Passed(pickle, step, definition)
	})
}

// Ambiguous implements formatters.Formatter.
func (o *onFlushFormatter) Ambiguous(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition, err error) {
	o.fns = append(o.fns, func() {
		o.fmt.Ambiguous(pickle, step, definition, err)
	})
}

// Defined implements formatters.Formatter.
func (o *onFlushFormatter) Defined(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition) {
	o.fns = append(o.fns, func() {
		o.fmt.Defined(pickle, step, definition)
	})
}

// Failed implements formatters.Formatter.
func (o *onFlushFormatter) Failed(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition, err error) {
	o.fns = append(o.fns, func() {
		o.fmt.Failed(pickle, step, definition, err)
	})
}

// Feature implements formatters.Formatter.
func (o *onFlushFormatter) Feature(pickle *messages.GherkinDocument, p string, c []byte) {
	o.fns = append(o.fns, func() {
		o.fmt.Feature(pickle, p, c)
	})
}

// Pending implements formatters.Formatter.
func (o *onFlushFormatter) Pending(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition) {
	o.fns = append(o.fns, func() {
		o.fmt.Pending(pickle, step, definition)
	})
}

// Skipped implements formatters.Formatter.
func (o *onFlushFormatter) Skipped(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition) {
	o.fns = append(o.fns, func() {
		o.fmt.Skipped(pickle, step, definition)
	})
}

// Summary implements formatters.Formatter.
func (o *onFlushFormatter) Summary() {
	o.fns = append(o.fns, func() {
		o.fmt.Summary()
	})
}

// TestRunStarted implements formatters.Formatter.
func (o *onFlushFormatter) TestRunStarted() {
	o.fns = append(o.fns, func() {
		o.fmt.TestRunStarted()
	})
}

// Undefined implements formatters.Formatter.
func (o *onFlushFormatter) Undefined(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition) {
	o.fns = append(o.fns, func() {
		o.fmt.Undefined(pickle, step, definition)
	})
}

// Flush the logs.
func (o *onFlushFormatter) Flush() {
	o.mu.Lock()
	defer o.mu.Unlock()
	for _, fn := range o.fns {
		fn()
	}
}
```

## File: `internal/formatters/fmt_flushwrap_test.go`
```go
package formatters

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

var flushMock = DummyFormatter{}

func TestFlushWrapOnFormatter(t *testing.T) {
	flushMock.tt = t

	fmt := WrapOnFlush(&flushMock)

	fmt.Feature(document, str, byt)
	fmt.TestRunStarted()
	fmt.Pickle(pickle)
	fmt.Defined(pickle, step, definition)
	fmt.Passed(pickle, step, definition)
	fmt.Skipped(pickle, step, definition)
	fmt.Undefined(pickle, step, definition)
	fmt.Failed(pickle, step, definition, err)
	fmt.Pending(pickle, step, definition)
	fmt.Ambiguous(pickle, step, definition, err)
	fmt.Summary()

	assert.Equal(t, 0, flushMock.CountFeature)
	assert.Equal(t, 0, flushMock.CountTestRunStarted)
	assert.Equal(t, 0, flushMock.CountPickle)
	assert.Equal(t, 0, flushMock.CountDefined)
	assert.Equal(t, 0, flushMock.CountPassed)
	assert.Equal(t, 0, flushMock.CountSkipped)
	assert.Equal(t, 0, flushMock.CountUndefined)
	assert.Equal(t, 0, flushMock.CountFailed)
	assert.Equal(t, 0, flushMock.CountPending)
	assert.Equal(t, 0, flushMock.CountAmbiguous)
	assert.Equal(t, 0, flushMock.CountSummary)

	fmt.Flush()

	assert.Equal(t, 1, flushMock.CountFeature)
	assert.Equal(t, 1, flushMock.CountTestRunStarted)
	assert.Equal(t, 1, flushMock.CountPickle)
	assert.Equal(t, 1, flushMock.CountDefined)
	assert.Equal(t, 1, flushMock.CountPassed)
	assert.Equal(t, 1, flushMock.CountSkipped)
	assert.Equal(t, 1, flushMock.CountUndefined)
	assert.Equal(t, 1, flushMock.CountFailed)
	assert.Equal(t, 1, flushMock.CountPending)
	assert.Equal(t, 1, flushMock.CountAmbiguous)
	assert.Equal(t, 1, flushMock.CountSummary)
}
```

## File: `internal/formatters/fmt_junit.go`
```go
package formatters

import (
	"encoding/xml"
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
	"time"

	"github.com/cucumber/godog/formatters"
	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/utils"
)

func init() {
	formatters.Format("junit", "Prints junit compatible xml to stdout", JUnitFormatterFunc)
}

// JUnitFormatterFunc implements the FormatterFunc for the junit formatter
func JUnitFormatterFunc(suite string, out io.Writer) formatters.Formatter {
	return &JUnit{Base: NewBase(suite, out)}
}

// JUnit renders test results in JUnit format.
type JUnit struct {
	*Base
}

// Summary renders summary information.
func (f *JUnit) Summary() {
	suite := f.buildJUNITPackageSuite()

	_, err := io.WriteString(f.out, xml.Header)
	if err != nil {
		fmt.Fprintln(os.Stderr, "failed to write junit string:", err)
	}

	enc := xml.NewEncoder(f.out)
	enc.Indent("", s(2))
	if err = enc.Encode(suite); err != nil {
		fmt.Fprintln(os.Stderr, "failed to write junit xml:", err)
	}
}

func junitTimeDuration(from, to time.Time) string {
	return strconv.FormatFloat(to.Sub(from).Seconds(), 'f', -1, 64)
}

// getPickleResult deals with the fact that if there's no result due to 'StopOnFirstFailure' being
// set, MustGetPickleResult panics.
func (f *JUnit) getPickleResult(pickleID string) (res *models.PickleResult) {
	defer func() {
		if r := recover(); r != nil {
			res = nil
		}
	}()
	pr := f.Storage.MustGetPickleResult(pickleID)
	res = &pr
	return
}

func (f *JUnit) getPickleStepResult(stepID string) (res *models.PickleStepResult) {
	defer func() {
		if r := recover(); r != nil {
			res = nil
		}
	}()
	psr := f.Storage.MustGetPickleStepResult(stepID)
	res = &psr
	return
}

func (f *JUnit) getPickleStepResultsByPickleID(pickleID string) (res []models.PickleStepResult) {
	defer func() {
		if r := recover(); r != nil {
			res = nil
		}
	}()
	res = f.Storage.MustGetPickleStepResultsByPickleID(pickleID)
	return
}

func (f *JUnit) buildJUNITPackageSuite() JunitPackageSuite {
	features := f.Storage.MustGetFeatures()
	sort.Sort(sortFeaturesByName(features))

	testRunStartedAt := f.Storage.MustGetTestRunStarted().StartedAt

	suite := JunitPackageSuite{
		Name:       f.suiteName,
		TestSuites: make([]*junitTestSuite, len(features)),
		Time:       junitTimeDuration(testRunStartedAt, utils.TimeNowFunc()),
	}

	for idx, feature := range features {
		pickles := f.Storage.MustGetPickles(feature.Uri)
		sort.Sort(sortPicklesByID(pickles))

		ts := junitTestSuite{
			Name:      feature.Feature.Name,
			TestCases: make([]*junitTestCase, len(pickles)),
		}

		var testcaseNames = make(map[string]int)
		for _, pickle := range pickles {
			testcaseNames[pickle.Name] = testcaseNames[pickle.Name] + 1
		}

		firstPickleStartedAt := testRunStartedAt
		lastPickleFinishedAt := testRunStartedAt

		var outlineNo = make(map[string]int)
		for idx, pickle := range pickles {
			tc := junitTestCase{}
			tc.Name = pickle.Name
			if testcaseNames[tc.Name] > 1 {
				outlineNo[tc.Name] = outlineNo[tc.Name] + 1
				tc.Name += fmt.Sprintf(" #%d", outlineNo[tc.Name])
			}

			pickleResult := f.getPickleResult(pickle.Id)
			if pickleResult == nil {
				tc.Status = skipped.String()
			} else {
				if idx == 0 {
					firstPickleStartedAt = pickleResult.StartedAt
				}
				lastPickleFinishedAt = pickleResult.StartedAt
			}

			if len(pickle.Steps) > 0 {
				lastStep := pickle.Steps[len(pickle.Steps)-1]
				if lastPickleStepResult := f.getPickleStepResult(lastStep.Id); lastPickleStepResult != nil {
					lastPickleFinishedAt = lastPickleStepResult.FinishedAt
				}
			}

			if pickleResult != nil {
				tc.Time = junitTimeDuration(pickleResult.StartedAt, lastPickleFinishedAt)
			}

			ts.Tests++
			suite.Tests++

			pickleStepResults := f.getPickleStepResultsByPickleID(pickle.Id)
			for _, stepResult := range pickleStepResults {
				pickleStep := f.Storage.MustGetPickleStep(stepResult.PickleStepID)

				switch stepResult.Status {
				case passed:
					tc.Status = passed.String()
				case failed:
					tc.Status = failed.String()
					tc.Failure = &junitFailure{
						Message: fmt.Sprintf("Step %s: %s", pickleStep.Text, stepResult.Err),
					}
				case ambiguous:
					tc.Status = ambiguous.String()
					tc.Error = append(tc.Error, &junitError{
						Type:    "ambiguous",
						Message: fmt.Sprintf("Step %s", pickleStep.Text),
					})
				case skipped:
					tc.Error = append(tc.Error, &junitError{
						Type:    "skipped",
						Message: fmt.Sprintf("Step %s", pickleStep.Text),
					})
				case undefined:
					tc.Status = undefined.String()
					tc.Error = append(tc.Error, &junitError{
						Type:    "undefined",
						Message: fmt.Sprintf("Step %s", pickleStep.Text),
					})
				case pending:
					tc.Status = pending.String()
					tc.Error = append(tc.Error, &junitError{
						Type:    "pending",
						Message: fmt.Sprintf("Step %s: TODO: write pending definition", pickleStep.Text),
					})
				}
			}

			switch tc.Status {
			case failed.String():
				ts.Failures++
				suite.Failures++
			case undefined.String(), pending.String():
				ts.Errors++
				suite.Errors++
			}

			ts.TestCases[idx] = &tc
		}

		ts.Time = junitTimeDuration(firstPickleStartedAt, lastPickleFinishedAt)

		suite.TestSuites[idx] = &ts
	}

	return suite
}

type junitFailure struct {
	Message string `xml:"message,attr"`
	Type    string `xml:"type,attr,omitempty"`
}

type junitError struct {
	XMLName xml.Name `xml:"error,omitempty"`
	Message string   `xml:"message,attr"`
	Type    string   `xml:"type,attr"`
}

type junitTestCase struct {
	XMLName xml.Name      `xml:"testcase"`
	Name    string        `xml:"name,attr"`
	Status  string        `xml:"status,attr"`
	Time    string        `xml:"time,attr"`
	Failure *junitFailure `xml:"failure,omitempty"`
	Error   []*junitError
}

type junitTestSuite struct {
	XMLName   xml.Name `xml:"testsuite"`
	Name      string   `xml:"name,attr"`
	Tests     int      `xml:"tests,attr"`
	Skipped   int      `xml:"skipped,attr"`
	Failures  int      `xml:"failures,attr"`
	Errors    int      `xml:"errors,attr"`
	Time      string   `xml:"time,attr"`
	TestCases []*junitTestCase
}

// JunitPackageSuite ...
type JunitPackageSuite struct {
	XMLName    xml.Name `xml:"testsuites"`
	Name       string   `xml:"name,attr"`
	Tests      int      `xml:"tests,attr"`
	Skipped    int      `xml:"skipped,attr"`
	Failures   int      `xml:"failures,attr"`
	Errors     int      `xml:"errors,attr"`
	Time       string   `xml:"time,attr"`
	TestSuites []*junitTestSuite
}
```

## File: `internal/formatters/fmt_junit_test.go`
```go
package formatters_test

import (
	"bytes"
	"encoding/xml"
	"fmt"
	"testing"

	"github.com/cucumber/godog"
)

func Test_JUnitFormatter_StopOnFirstFailure(t *testing.T) {
	featureFile := "formatter-tests/features/stop_on_first_failure.feature"

	// First, verify the normal output (without StopOnFirstFailure)
	var normalBuf bytes.Buffer
	normalOpts := godog.Options{
		Format: "junit",
		Paths:  []string{featureFile},
		Output: &normalBuf,
		Strict: true,
	}

	normalSuite := godog.TestSuite{
		Name: "Normal Run",
		ScenarioInitializer: func(sc *godog.ScenarioContext) {
			setupStopOnFailureSteps(sc)
		},
		Options: &normalOpts,
	}
	if status := normalSuite.Run(); status != 1 {
		t.Fatalf("Expected suite to have status 1, but got %d", status)
	}

	// Parse the XML output
	var normalResult JunitPackageSuite
	err := xml.Unmarshal(normalBuf.Bytes(), &normalResult)
	if err != nil {
		t.Fatalf("Failed to parse XML output: %v", err)
	}

	// Now run with StopOnFirstFailure
	var stopBuf bytes.Buffer
	stopOpts := godog.Options{
		Format:        "junit",
		Paths:         []string{featureFile},
		Output:        &stopBuf,
		Strict:        true,
		StopOnFailure: true,
	}

	stopSuite := godog.TestSuite{
		Name: "Stop On First Failure",
		ScenarioInitializer: func(sc *godog.ScenarioContext) {
			setupStopOnFailureSteps(sc)
		},
		Options: &stopOpts,
	}
	if status := stopSuite.Run(); status != 1 {
		t.Fatalf("Expected suite to have status 1, but got %d", status)
	}

	// Parse the XML output
	var stopResult JunitPackageSuite
	err = xml.Unmarshal(stopBuf.Bytes(), &stopResult)
	if err != nil {
		t.Fatalf("Failed to parse XML output: %v", err)
	}

	// Verify the second test case is marked as skipped when StopOnFirstFailure is enabled
	if len(stopResult.TestSuites) == 0 || len(stopResult.TestSuites[0].TestCases) < 2 {
		t.Fatal("Expected at least 2 test cases in the results")
	}

	// In a normal run, second test case should not be skipped
	if normalResult.TestSuites[0].TestCases[1].Status == "skipped" {
		t.Errorf("In normal run, second test case should not be skipped")
	}

	// In stop on failure run, second test case should be skipped
	if stopResult.TestSuites[0].TestCases[1].Status != "skipped" {
		t.Errorf("In stop on failure run, second test case should be skipped, but got %s",
			stopResult.TestSuites[0].TestCases[1].Status)
	}
}

// setupStopOnFailureSteps registers the step definitions for the stop-on-failure test
func setupStopOnFailureSteps(sc *godog.ScenarioContext) {
	sc.Step(`^a passing step$`, func() error {
		return nil
	})
	sc.Step(`^a failing step$`, func() error {
		return fmt.Errorf("step failed")
	})
}

// JunitPackageSuite represents the JUnit XML structure for test suites
type JunitPackageSuite struct {
	XMLName    xml.Name          `xml:"testsuites"`
	Name       string            `xml:"name,attr"`
	Tests      int               `xml:"tests,attr"`
	Skipped    int               `xml:"skipped,attr"`
	Failures   int               `xml:"failures,attr"`
	Errors     int               `xml:"errors,attr"`
	Time       string            `xml:"time,attr"`
	TestSuites []*JunitTestSuite `xml:"testsuite"`
}

type JunitTestSuite struct {
	XMLName   xml.Name         `xml:"testsuite"`
	Name      string           `xml:"name,attr"`
	Tests     int              `xml:"tests,attr"`
	Skipped   int              `xml:"skipped,attr"`
	Failures  int              `xml:"failures,attr"`
	Errors    int              `xml:"errors,attr"`
	Time      string           `xml:"time,attr"`
	TestCases []*JunitTestCase `xml:"testcase"`
}

type JunitTestCase struct {
	XMLName xml.Name      `xml:"testcase"`
	Name    string        `xml:"name,attr"`
	Status  string        `xml:"status,attr"`
	Time    string        `xml:"time,attr"`
	Failure *JunitFailure `xml:"failure,omitempty"`
	Error   []*JunitError `xml:"error,omitempty"`
}

type JunitFailure struct {
	Message string `xml:"message,attr"`
	Type    string `xml:"type,attr,omitempty"`
}

type JunitError struct {
	XMLName xml.Name `xml:"error,omitempty"`
	Message string   `xml:"message,attr"`
	Type    string   `xml:"type,attr"`
}
```

## File: `internal/formatters/fmt_multi.go`
```go
package formatters

import (
	"io"

	"github.com/cucumber/godog/formatters"
	"github.com/cucumber/godog/internal/storage"
	messages "github.com/cucumber/messages/go/v21"
)

// MultiFormatter passes test progress to multiple formatters.
type MultiFormatter struct {
	formatters []formatter
	repeater   repeater
}

type formatter struct {
	fmt formatters.FormatterFunc
	out io.Writer
}

type repeater []formatters.Formatter

type storageFormatter interface {
	SetStorage(s *storage.Storage)
}

// SetStorage passes storage to all added formatters.
func (r repeater) SetStorage(s *storage.Storage) {
	for _, f := range r {
		if ss, ok := f.(storageFormatter); ok {
			ss.SetStorage(s)
		}
	}
}

// TestRunStarted triggers TestRunStarted for all added formatters.
func (r repeater) TestRunStarted() {
	for _, f := range r {
		f.TestRunStarted()
	}
}

// Feature triggers Feature for all added formatters.
func (r repeater) Feature(document *messages.GherkinDocument, s string, bytes []byte) {
	for _, f := range r {
		f.Feature(document, s, bytes)
	}
}

// Pickle triggers Pickle for all added formatters.
func (r repeater) Pickle(pickle *messages.Pickle) {
	for _, f := range r {
		f.Pickle(pickle)
	}
}

// Defined triggers Defined for all added formatters.
func (r repeater) Defined(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition) {
	for _, f := range r {
		f.Defined(pickle, step, definition)
	}
}

// Failed triggers Failed for all added formatters.
func (r repeater) Failed(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition, err error) {
	for _, f := range r {
		f.Failed(pickle, step, definition, err)
	}
}

// Passed triggers Passed for all added formatters.
func (r repeater) Passed(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition) {
	for _, f := range r {
		f.Passed(pickle, step, definition)
	}
}

// Skipped triggers Skipped for all added formatters.
func (r repeater) Skipped(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition) {
	for _, f := range r {
		f.Skipped(pickle, step, definition)
	}
}

// Undefined triggers Undefined for all added formatters.
func (r repeater) Undefined(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition) {
	for _, f := range r {
		f.Undefined(pickle, step, definition)
	}
}

// Pending triggers Pending for all added formatters.
func (r repeater) Pending(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition) {
	for _, f := range r {
		f.Pending(pickle, step, definition)
	}
}

// Ambiguous triggers Ambiguous for all added formatters.
func (r repeater) Ambiguous(pickle *messages.Pickle, step *messages.PickleStep, definition *formatters.StepDefinition, err error) {
	for _, f := range r {
		f.Ambiguous(pickle, step, definition, err)
	}
}

// Summary triggers Summary for all added formatters.
func (r repeater) Summary() {
	for _, f := range r {
		f.Summary()
	}
}

// Add adds formatter with output writer.
func (m *MultiFormatter) Add(name string, out io.Writer) {
	f := formatters.FindFmt(name)
	if f == nil {
		panic("formatter not found: " + name)
	}

	m.formatters = append(m.formatters, formatter{
		fmt: f,
		out: out,
	})
}

// FormatterFunc implements the FormatterFunc for the multi formatter.
func (m *MultiFormatter) FormatterFunc(suite string, out io.Writer) formatters.Formatter {
	for _, f := range m.formatters {
		out := out
		if f.out != nil {
			out = f.out
		}

		m.repeater = append(m.repeater, f.fmt(suite, out))
	}

	return m.repeater
}
```

## File: `internal/formatters/fmt_multi_test.go`
```go
package formatters

import (
	"errors"
	"testing"

	"github.com/cucumber/godog/formatters"
	messages "github.com/cucumber/messages/go/v21"
	"github.com/stretchr/testify/assert"
)

var (
	mock = DummyFormatter{}
	base = BaseFormatter{}

	document   = &messages.GherkinDocument{}
	str        = "theString"
	byt        = []byte("bytes")
	pickle     = &messages.Pickle{}
	step       = &messages.PickleStep{}
	definition = &formatters.StepDefinition{}
	err        = errors.New("expected")
)

// TestRepeater tests the delegation of the repeater functions.
func TestRepeater(t *testing.T) {
	mock.tt = t
	f := make(repeater, 0)
	f = append(f, &mock)
	f = append(f, &mock)
	f = append(f, &base)

	f.Feature(document, str, byt)
	f.TestRunStarted()
	f.Pickle(pickle)
	f.Defined(pickle, step, definition)
	f.Passed(pickle, step, definition)
	f.Skipped(pickle, step, definition)
	f.Undefined(pickle, step, definition)
	f.Failed(pickle, step, definition, err)
	f.Pending(pickle, step, definition)
	f.Ambiguous(pickle, step, definition, err)

	assert.Equal(t, 2, mock.CountFeature)
	assert.Equal(t, 2, mock.CountTestRunStarted)
	assert.Equal(t, 2, mock.CountPickle)
	assert.Equal(t, 2, mock.CountDefined)
	assert.Equal(t, 2, mock.CountPassed)
	assert.Equal(t, 2, mock.CountSkipped)
	assert.Equal(t, 2, mock.CountUndefined)
	assert.Equal(t, 2, mock.CountFailed)
	assert.Equal(t, 2, mock.CountPending)
	assert.Equal(t, 2, mock.CountAmbiguous)
}

type BaseFormatter struct {
	*Base
}

type DummyFormatter struct {
	*Base

	tt                  *testing.T
	CountFeature        int
	CountTestRunStarted int
	CountPickle         int
	CountDefined        int
	CountPassed         int
	CountSkipped        int
	CountUndefined      int
	CountFailed         int
	CountPending        int
	CountAmbiguous      int
	CountSummary        int
}

// SetStorage assigns gherkin data storage.
// func (f *DummyFormatter) SetStorage(st *storage.Storage) {
// }

// TestRunStarted is triggered on test start.
func (f *DummyFormatter) TestRunStarted() {
	f.CountTestRunStarted++
}

// Feature receives gherkin document.
func (f *DummyFormatter) Feature(d *messages.GherkinDocument, s string, b []byte) {
	assert.Equal(f.tt, document, d)
	assert.Equal(f.tt, str, s)
	assert.Equal(f.tt, byt, b)
	f.CountFeature++
}

// Pickle receives scenario.
func (f *DummyFormatter) Pickle(p *messages.Pickle) {
	assert.Equal(f.tt, pickle, p)
	f.CountPickle++
}

// Defined receives step definition.
func (f *DummyFormatter) Defined(p *messages.Pickle, s *messages.PickleStep, d *formatters.StepDefinition) {
	assert.Equal(f.tt, pickle, p)
	assert.Equal(f.tt, s, step)
	assert.Equal(f.tt, d, definition)
	f.CountDefined++
}

// Passed captures passed step.
func (f *DummyFormatter) Passed(p *messages.Pickle, s *messages.PickleStep, d *formatters.StepDefinition) {
	assert.Equal(f.tt, pickle, p)
	assert.Equal(f.tt, s, step)
	assert.Equal(f.tt, d, definition)
	f.CountPassed++
}

// Skipped captures skipped step.
func (f *DummyFormatter) Skipped(p *messages.Pickle, s *messages.PickleStep, d *formatters.StepDefinition) {
	assert.Equal(f.tt, pickle, p)
	assert.Equal(f.tt, s, step)
	assert.Equal(f.tt, d, definition)

	f.CountSkipped++
}

// Undefined captures undefined step.
func (f *DummyFormatter) Undefined(p *messages.Pickle, s *messages.PickleStep, d *formatters.StepDefinition) {
	assert.Equal(f.tt, pickle, p)
	assert.Equal(f.tt, s, step)
	assert.Equal(f.tt, d, definition)

	f.CountUndefined++
}

// Failed captures failed step.
func (f *DummyFormatter) Failed(p *messages.Pickle, s *messages.PickleStep, d *formatters.StepDefinition, e error) {
	assert.Equal(f.tt, pickle, p)
	assert.Equal(f.tt, s, step)
	assert.Equal(f.tt, d, definition)
	assert.Equal(f.tt, err, e)

	f.CountFailed++
}

// Pending captures pending step.
func (f *DummyFormatter) Pending(p *messages.Pickle, s *messages.PickleStep, d *formatters.StepDefinition) {
	assert.Equal(f.tt, pickle, p)
	assert.Equal(f.tt, s, step)
	assert.Equal(f.tt, d, definition)

	f.CountPending++
}

// Ambiguous captures ambiguous step.
func (f *DummyFormatter) Ambiguous(p *messages.Pickle, s *messages.PickleStep, d *formatters.StepDefinition, e error) {
	assert.Equal(f.tt, pickle, p)
	assert.Equal(f.tt, s, step)
	assert.Equal(f.tt, d, definition)
	f.CountAmbiguous++
}

// Pickle receives scenario.
func (f *DummyFormatter) Summary() {
	f.CountSummary++
}
```

## File: `internal/formatters/fmt_output_test.go`
```go
package formatters_test

import (
	"bytes"
	"context"
	"fmt"
	"os"
	"path"
	"path/filepath"
	"regexp"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/cucumber/godog"
)

const fmtOutputTestsFeatureDir = "formatter-tests/features"

var tT *testing.T

func Test_FmtOutput(t *testing.T) {
	tT = t
	pkg := os.Getenv("GODOG_TESTED_PACKAGE")
	os.Setenv("GODOG_TESTED_PACKAGE", "github.com/cucumber/godog")

	featureFiles, err := listFmtOutputTestsFeatureFiles()
	require.Nil(t, err)
	formatters := []string{"cucumber", "events", "junit", "pretty", "progress", "junit,pretty"}
	for _, fmtName := range formatters {
		for _, featureFile := range featureFiles {
			testName := fmt.Sprintf("%s/%s", fmtName, featureFile)
			featureFilePath := fmt.Sprintf("%s/%s", fmtOutputTestsFeatureDir, featureFile)
			t.Run(testName, fmtOutputTest(fmtName, testName, featureFilePath))
		}
	}

	os.Setenv("GODOG_TESTED_PACKAGE", pkg)
}

func listFmtOutputTestsFeatureFiles() (featureFiles []string, err error) {
	err = filepath.Walk(fmtOutputTestsFeatureDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if !info.IsDir() {
			featureFiles = append(featureFiles, info.Name())
			return nil
		}

		if info.Name() == "features" {
			return nil
		}

		return filepath.SkipDir
	})

	return
}

func fmtOutputTest(fmtName, testName, featureFilePath string) func(*testing.T) {
	fmtOutputScenarioInitializer := func(ctx *godog.ScenarioContext) {
		stepIndex := 0
		ctx.Before(func(ctx context.Context, sc *godog.Scenario) (context.Context, error) {
			if strings.Contains(sc.Name, "attachment") {
				att := godog.Attachments(ctx)
				attCount := len(att)
				if attCount != 0 {
					assert.FailNowf(tT, "Unexpected attachments: "+sc.Name, "should have been empty, found %d", attCount)
				}

				ctx = godog.Attach(ctx,
					godog.Attachment{Body: []byte("BeforeScenarioAttachment"), FileName: "Before Scenario Attachment 1", MediaType: "text/plain"},
				)
			}
			return ctx, nil
		})

		ctx.After(func(ctx context.Context, sc *godog.Scenario, err error) (context.Context, error) {

			if strings.Contains(sc.Name, "attachment") {
				att := godog.Attachments(ctx)
				attCount := len(att)
				if attCount != 4 {
					assert.FailNow(tT, "Unexpected attachments: "+sc.Name, "expected 4, found %d", attCount)
				}
				ctx = godog.Attach(ctx,
					godog.Attachment{Body: []byte("AfterScenarioAttachment"), FileName: "After Scenario Attachment 2", MediaType: "text/plain"},
				)
			}
			return ctx, nil
		})

		ctx.StepContext().Before(func(ctx context.Context, st *godog.Step) (context.Context, error) {
			stepIndex++

			if strings.Contains(st.Text, "attachment") {
				att := godog.Attachments(ctx)
				attCount := len(att)

				// 1 for before scenario ONLY if this is the 1st step
				expectedAttCount := 0
				if stepIndex == 1 {
					expectedAttCount = 1
				}

				if attCount != expectedAttCount {
					assert.FailNow(tT, "Unexpected attachments: "+st.Text, "expected 1, found %d\n%+v", attCount, att)
				}
				ctx = godog.Attach(ctx,
					godog.Attachment{Body: []byte("BeforeStepAttachment"), FileName: "Before Step Attachment 3", MediaType: "text/plain"},
				)
			}
			return ctx, nil
		})
		ctx.StepContext().After(func(ctx context.Context, st *godog.Step, status godog.StepResultStatus, err error) (context.Context, error) {

			if strings.Contains(st.Text, "attachment") {
				att := godog.Attachments(ctx)
				attCount := len(att)

				// 1 for before scenario ONLY if this is the 1st step
				// 1 for before before step
				// 2 from from step
				expectedAttCount := 3
				if stepIndex == 1 {
					expectedAttCount = 4
				}

				if attCount != expectedAttCount {
					// 1 from before scenario, 1 from before step, 1 from step
					assert.FailNow(tT, "Unexpected attachments: "+st.Text, "expected 4, found %d", attCount)
				}
				ctx = godog.Attach(ctx,
					godog.Attachment{Body: []byte("AfterStepAttachment"), FileName: "After Step Attachment 4", MediaType: "text/plain"},
				)
			}
			return ctx, nil
		})

		ctx.Step(`^(?:a )?failing step`, failingStepDef)
		ctx.Step(`^(?:a )?pending step$`, pendingStepDef)
		ctx.Step(`^(?:a )?passing step$`, passingStepDef)
		ctx.Step(`^ambiguous step.*$`, ambiguousStepDef)
		ctx.Step(`^ambiguous step$`, ambiguousStepDef)
		ctx.Step(`^odd (\d+) and even (\d+) number$`, oddEvenStepDef)
		ctx.Step(`^(?:a )?a step with a single attachment call for multiple attachments$`, stepWithSingleAttachmentCall)
		ctx.Step(`^(?:a )?a step with multiple attachment calls$`, stepWithMultipleAttachmentCalls)
	}

	return func(t *testing.T) {
		fmt.Printf("fmt_output_test for format %10s : sample file %v\n", fmtName, featureFilePath)
		expectOutputPath := strings.Replace(featureFilePath, "features", fmtName, 1)
		expectOutputPath = strings.TrimSuffix(expectOutputPath, path.Ext(expectOutputPath))
		if _, err := os.Stat(expectOutputPath); err != nil {
			// the test author needs to write an "expected output" file for any formats they want the test feature to be verified against
			t.Skipf("Skipping test for feature '%v' for format '%v', because no 'expected output' file %q", featureFilePath, fmtName, expectOutputPath)
		}

		expectedOutput, err := os.ReadFile(expectOutputPath)
		require.NoError(t, err)

		var buf bytes.Buffer
		out := &tagColorWriter{w: &buf}

		opts := godog.Options{
			Format: fmtName,
			Paths:  []string{featureFilePath},
			Output: out,
			Strict: true,
		}

		godog.TestSuite{
			Name:                fmtName,
			ScenarioInitializer: fmtOutputScenarioInitializer,
			Options:             &opts,
		}.Run()

		// normalise on unix line ending so expected vs actual works cross platform
		expected := normalise(string(expectedOutput))
		actual := normalise(buf.String())

		assert.Equalf(t, expected, actual, "path: %s", expectOutputPath)

		// display as a side by side listing as the output of the assert is all one line with embedded newlines and useless
		if expected != actual {
			fmt.Printf("Error: fmt: %s, path: %s\n", fmtName, expectOutputPath)
			compareLists(expected, actual)
		}
	}
}

func normalise(s string) string {

	m := regexp.MustCompile("fmt_output_test.go:[0-9]+")
	normalised := m.ReplaceAllString(s, "fmt_output_test.go:XXX")
	normalised = strings.Replace(normalised, "\r\n", "\n", -1)
	normalised = strings.Replace(normalised, "\\r\\n", "\\n", -1)

	return normalised
}

func passingStepDef() error {
	return nil
}

func ambiguousStepDef() error {
	return nil
}

func oddEvenStepDef(odd, even int) error {
	return oddOrEven(odd, even)
}

func oddOrEven(odd, even int) error {
	if odd%2 == 0 {
		return fmt.Errorf("%d is not odd", odd)
	}
	if even%2 != 0 {
		return fmt.Errorf("%d is not even", even)
	}
	return nil
}

func pendingStepDef() error { return godog.ErrPending }

func failingStepDef() error { return fmt.Errorf("step failed") }

func stepWithSingleAttachmentCall(ctx context.Context) (context.Context, error) {
	aCount := len(godog.Attachments(ctx))
	if aCount != 2 {
		// 1 from before scenario, 1 from before step
		assert.FailNowf(tT, "Unexpected Attachments found", "should have been 2, but found %v", aCount)
	}

	ctx = godog.Attach(ctx,
		godog.Attachment{Body: []byte("TheData1"), FileName: "TheFilename1", MediaType: "text/plain"},
		godog.Attachment{Body: []byte("TheData2"), FileName: "TheFilename2", MediaType: "text/plain"},
	)

	return ctx, nil
}
func stepWithMultipleAttachmentCalls(ctx context.Context) (context.Context, error) {
	aCount := len(godog.Attachments(ctx))
	if aCount != 1 {
		assert.FailNowf(tT, "Unexpected Attachments found", "Expected 1 Attachment, but found %v", aCount)
	}

	ctx = godog.Attach(ctx,
		godog.Attachment{Body: []byte("TheData1"), FileName: "TheFilename3", MediaType: "text/plain"},
	)
	ctx = godog.Attach(ctx,
		godog.Attachment{Body: []byte("TheData2"), FileName: "TheFilename4", MediaType: "text/plain"},
	)

	return ctx, nil
}

// wrapString wraps a string into chunks of the given width.
func wrapString(s string, width int) []string {
	var result []string
	for len(s) > width {
		result = append(result, s[:width])
		s = s[width:]
	}
	result = append(result, s)
	return result
}

// compareLists compares two lists of strings and prints them with wrapped text.
func compareLists(expected, actual string) {
	list1 := strings.Split(expected, "\n")
	list2 := strings.Split(actual, "\n")

	// Get the length of the longer list
	maxLength := len(list1)
	if len(list2) > maxLength {
		maxLength = len(list2)
	}

	colWid := 60
	fmtTitle := fmt.Sprintf("%%4s: %%-%ds | %%-%ds\n", colWid+2, colWid+2)
	fmtData := fmt.Sprintf("%%4d: %%-%ds | %%-%ds   %%s\n", colWid+2, colWid+2)

	fmt.Printf(fmtTitle, "#", "expected", "actual")

	for i := 0; i < maxLength; i++ {
		var val1, val2 string

		// Get the value from list1 if it exists
		if i < len(list1) {
			val1 = list1[i]
		} else {
			val1 = "N/A"
		}

		// Get the value from list2 if it exists
		if i < len(list2) {
			val2 = list2[i]
		} else {
			val2 = "N/A"
		}

		// Wrap both strings into slices of strings with fixed width
		wrapped1 := wrapString(val1, colWid)
		wrapped2 := wrapString(val2, colWid)

		// Find the number of wrapped lines needed for the current pair
		maxWrappedLines := len(wrapped1)
		if len(wrapped2) > maxWrappedLines {
			maxWrappedLines = len(wrapped2)
		}

		// Print the wrapped lines with alignment
		for j := 0; j < maxWrappedLines; j++ {
			var line1, line2 string

			// Get the wrapped line or use an empty string if it doesn't exist
			if j < len(wrapped1) {
				line1 = wrapped1[j]
			} else {
				line1 = ""
			}

			if j < len(wrapped2) {
				line2 = wrapped2[j]
			} else {
				line2 = ""
			}

			status := "same"
			// if val1 != val2 {
			if line1 != line2 {
				status = "different"
			}

			delim := "¬"
			// Print the wrapped lines with fixed-width column
			fmt.Printf(fmtData, i+1, delim+line1+delim, delim+line2+delim, status)
		}
	}
}
```

## File: `internal/formatters/fmt_pretty.go`
```go
package formatters

import (
	"fmt"
	"io"
	"regexp"
	"sort"
	"strings"
	"unicode/utf8"

	messages "github.com/cucumber/messages/go/v21"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/formatters"
	"github.com/cucumber/godog/internal/models"
)

func init() {
	formatters.Format("pretty", "Prints every feature with runtime statuses.", PrettyFormatterFunc)
}

// PrettyFormatterFunc implements the FormatterFunc for the pretty formatter
func PrettyFormatterFunc(suite string, out io.Writer) formatters.Formatter {
	return &Pretty{Base: NewBase(suite, out)}
}

var outlinePlaceholderRegexp = regexp.MustCompile("<[^>]+>")

// Pretty is a formatter for readable output.
type Pretty struct {
	*Base
	firstFeature *bool
}

// TestRunStarted is triggered on test start.
func (f *Pretty) TestRunStarted() {
	f.Base.TestRunStarted()

	f.Lock.Lock()
	defer f.Lock.Unlock()

	firstFeature := true
	f.firstFeature = &firstFeature
}

// Feature receives gherkin document.
func (f *Pretty) Feature(gd *messages.GherkinDocument, p string, c []byte) {
	f.Lock.Lock()
	if !*f.firstFeature {
		fmt.Fprintln(f.out, "")
	}

	*f.firstFeature = false
	f.Lock.Unlock()

	f.Base.Feature(gd, p, c)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.printFeature(gd.Feature)
}

// Pickle takes a gherkin node for formatting.
func (f *Pretty) Pickle(pickle *messages.Pickle) {
	f.Base.Pickle(pickle)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	if len(pickle.Steps) == 0 {
		f.printUndefinedPickle(pickle)
		return
	}
}

// Passed captures passed step.
func (f *Pretty) Passed(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Passed(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.printStep(pickle, step)
}

// Skipped captures skipped step.
func (f *Pretty) Skipped(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Skipped(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.printStep(pickle, step)
}

// Undefined captures undefined step.
func (f *Pretty) Undefined(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Undefined(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.printStep(pickle, step)
}

// Failed captures failed step.
func (f *Pretty) Failed(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition, err error) {
	f.Base.Failed(pickle, step, match, err)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.printStep(pickle, step)
}

// Failed captures failed step.
func (f *Pretty) Ambiguous(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition, err error) {
	f.Base.Ambiguous(pickle, step, match, err)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.printStep(pickle, step)
}

// Pending captures pending step.
func (f *Pretty) Pending(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Pending(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.printStep(pickle, step)
}

func (f *Pretty) printFeature(feature *messages.Feature) {
	fmt.Fprintln(f.out, keywordAndName(feature.Keyword, feature.Name))
	if strings.TrimSpace(feature.Description) != "" {
		for _, line := range strings.Split(feature.Description, "\n") {
			fmt.Fprintln(f.out, s(f.indent)+strings.TrimSpace(line))
		}
	}
}

func keywordAndName(keyword, name string) string {
	title := whiteb(keyword + ":")
	if len(name) > 0 {
		title += " " + name
	}
	return title
}

func (f *Pretty) scenarioLengths(pickle *messages.Pickle) (scenarioHeaderLength int, maxLength int) {
	feature := f.Storage.MustGetFeature(pickle.Uri)
	astScenario := feature.FindScenario(pickle.AstNodeIds[0])
	astBackground := feature.FindBackground(pickle.AstNodeIds[0])

	scenarioHeaderLength = f.lengthPickle(astScenario.Keyword, astScenario.Name)
	maxLength = f.longestStep(astScenario.Steps, scenarioHeaderLength)

	if astBackground != nil {
		maxLength = f.longestStep(astBackground.Steps, maxLength)
	}

	return scenarioHeaderLength, maxLength
}

func (f *Pretty) printScenarioHeader(pickle *messages.Pickle, astScenario *messages.Scenario, spaceFilling int) {
	feature := f.Storage.MustGetFeature(pickle.Uri)
	text := s(f.indent) + keywordAndName(astScenario.Keyword, astScenario.Name)
	text += s(spaceFilling) + line(feature.Uri, astScenario.Location)
	fmt.Fprintln(f.out, "\n"+text)
}

func (f *Pretty) printUndefinedPickle(pickle *messages.Pickle) {
	feature := f.Storage.MustGetFeature(pickle.Uri)
	astScenario := feature.FindScenario(pickle.AstNodeIds[0])
	astBackground := feature.FindBackground(pickle.AstNodeIds[0])

	scenarioHeaderLength, maxLength := f.scenarioLengths(pickle)

	if astBackground != nil {
		fmt.Fprintln(f.out, "\n"+s(f.indent)+keywordAndName(astBackground.Keyword, astBackground.Name))
		for _, step := range astBackground.Steps {
			text := s(f.indent*2) + cyan(strings.TrimSpace(step.Keyword)) + " " + cyan(step.Text)
			fmt.Fprintln(f.out, text)
		}
	}

	//  do not print scenario headers and examples multiple times
	if len(astScenario.Examples) > 0 {
		exampleTable, exampleRow := feature.FindExample(pickle.AstNodeIds[1])
		firstExampleRow := exampleTable.TableBody[0].Id == exampleRow.Id
		firstExamplesTable := astScenario.Examples[0].Location.Line == exampleTable.Location.Line

		if !(firstExamplesTable && firstExampleRow) {
			return
		}
	}

	f.printScenarioHeader(pickle, astScenario, maxLength-scenarioHeaderLength)

	for _, examples := range astScenario.Examples {
		max := longestExampleRow(examples, cyan, cyan)

		fmt.Fprintln(f.out, "")
		fmt.Fprintln(f.out, s(f.indent*2)+keywordAndName(examples.Keyword, examples.Name))

		f.printTableHeader(examples.TableHeader, max)

		for _, row := range examples.TableBody {
			f.printTableRow(row, max, cyan)
		}
	}
}

// Summary renders summary information.
func (f *Pretty) Summary() {
	failedStepResults := f.Storage.MustGetPickleStepResultsByStatus(failed)
	if len(failedStepResults) > 0 {
		fmt.Fprintln(f.out, "\n--- "+red("Failed steps:")+"\n")

		sort.Sort(sortPickleStepResultsByPickleStepID(failedStepResults))

		for _, fail := range failedStepResults {
			pickle := f.Storage.MustGetPickle(fail.PickleID)
			pickleStep := f.Storage.MustGetPickleStep(fail.PickleStepID)
			feature := f.Storage.MustGetFeature(pickle.Uri)

			astScenario := feature.FindScenario(pickle.AstNodeIds[0])
			scenarioDesc := fmt.Sprintf("%s: %s", astScenario.Keyword, pickle.Name)

			astStep := feature.FindStep(pickleStep.AstNodeIds[0])
			stepDesc := strings.TrimSpace(astStep.Keyword) + " " + pickleStep.Text

			fmt.Fprintln(f.out, s(f.indent)+red(scenarioDesc)+line(feature.Uri, astScenario.Location))
			fmt.Fprintln(f.out, s(f.indent*2)+red(stepDesc)+line(feature.Uri, astStep.Location))
			fmt.Fprintln(f.out, s(f.indent*3)+red("Error: ")+redb(fmt.Sprintf("%+v", fail.Err))+"\n")
		}
	}

	f.Base.Summary()
}

func (f *Pretty) printOutlineExample(pickle *messages.Pickle, step *messages.PickleStep, backgroundSteps int) {
	var errorMsg string
	var clr = green

	feature := f.Storage.MustGetFeature(pickle.Uri)
	astScenario := feature.FindScenario(pickle.AstNodeIds[0])
	scenarioHeaderLength, maxLength := f.scenarioLengths(pickle)

	exampleTable, exampleRow := feature.FindExample(pickle.AstNodeIds[1])
	printExampleHeader := exampleTable.TableBody[0].Id == exampleRow.Id
	firstExamplesTable := astScenario.Examples[0].Location.Line == exampleTable.Location.Line

	pickleStepResults := f.Storage.MustGetPickleStepResultsByPickleIDUntilStep(pickle.Id, step.Id)

	firstExecutedScenarioStep := len(pickleStepResults) == backgroundSteps+1
	if firstExamplesTable && printExampleHeader && firstExecutedScenarioStep {
		f.printScenarioHeader(pickle, astScenario, maxLength-scenarioHeaderLength)
	}

	if len(exampleTable.TableBody) == 0 {
		// do not print empty examples
		return
	}

	lastStep := len(pickleStepResults) == len(pickle.Steps)
	if !lastStep {
		// do not print examples unless all steps has finished
		return
	}

	for _, result := range pickleStepResults {
		// determine example row status
		switch {
		case result.Status == failed:
			errorMsg = result.Err.Error()
			clr = result.Status.Color()
		case result.Status == ambiguous:
			errorMsg = result.Err.Error()
			clr = result.Status.Color()
		case result.Status == undefined || result.Status == pending:
			clr = result.Status.Color()
		case result.Status == skipped && clr == nil:
			clr = cyan
		}

		if firstExamplesTable && printExampleHeader {
			// in first example, we need to print steps

			pickleStep := f.Storage.MustGetPickleStep(result.PickleStepID)
			astStep := feature.FindStep(pickleStep.AstNodeIds[0])

			var text = ""
			if result.Def != nil {
				if m := outlinePlaceholderRegexp.FindAllStringIndex(astStep.Text, -1); len(m) > 0 {
					var pos int
					for i := 0; i < len(m); i++ {
						pair := m[i]
						text += cyan(astStep.Text[pos:pair[0]])
						text += cyanb(astStep.Text[pair[0]:pair[1]])
						pos = pair[1]
					}
					text += cyan(astStep.Text[pos:len(astStep.Text)])
				} else {
					text = cyan(astStep.Text)
				}

				_, maxLength := f.scenarioLengths(pickle)
				stepLength := f.lengthPickleStep(astStep.Keyword, astStep.Text)

				text += s(maxLength - stepLength)
				text += " " + blackb("# "+DefinitionID(result.Def))
			}

			// print the step outline
			fmt.Fprintln(f.out, s(f.indent*2)+cyan(strings.TrimSpace(astStep.Keyword))+" "+text)

			if pickleStep.Argument != nil {
				if table := pickleStep.Argument.DataTable; table != nil {
					f.printTable(table, cyan)
				}

				if docString := astStep.DocString; docString != nil {
					f.printDocString(docString)
				}
			}
		}
	}

	max := longestExampleRow(exampleTable, clr, cyan)

	// an example table header
	if printExampleHeader {
		fmt.Fprintln(f.out, "")
		fmt.Fprintln(f.out, s(f.indent*2)+keywordAndName(exampleTable.Keyword, exampleTable.Name))

		f.printTableHeader(exampleTable.TableHeader, max)
	}

	f.printTableRow(exampleRow, max, clr)

	if errorMsg != "" {
		fmt.Fprintln(f.out, s(f.indent*4)+redb(errorMsg))
	}
}

func (f *Pretty) printTableRow(row *messages.TableRow, max []int, clr colors.ColorFunc) {
	cells := make([]string, len(row.Cells))

	for i, cell := range row.Cells {
		val := clr(cell.Value)
		ln := utf8.RuneCountInString(val)
		cells[i] = val + s(max[i]-ln)
	}

	fmt.Fprintln(f.out, s(f.indent*3)+"| "+strings.Join(cells, " | ")+" |")
}

func (f *Pretty) printTableHeader(row *messages.TableRow, max []int) {
	f.printTableRow(row, max, cyan)
}

func isFirstScenarioInRule(rule *messages.Rule, scenario *messages.Scenario) bool {
	if rule == nil || scenario == nil {
		return false
	}
	var firstScenario *messages.Scenario
	for _, c := range rule.Children {
		if c.Scenario != nil {
			firstScenario = c.Scenario
			break
		}
	}
	return firstScenario != nil && firstScenario.Id == scenario.Id
}

func isFirstPickleAndNoRule(feature *models.Feature, pickle *messages.Pickle, rule *messages.Rule) bool {
	if rule != nil {
		return false
	}
	return feature.Pickles[0].Id == pickle.Id
}

func (f *Pretty) printStep(pickle *messages.Pickle, pickleStep *messages.PickleStep) {
	feature := f.Storage.MustGetFeature(pickle.Uri)
	astBackground := feature.FindBackground(pickle.AstNodeIds[0])
	astScenario := feature.FindScenario(pickle.AstNodeIds[0])
	astRule := feature.FindRule(pickle.AstNodeIds[0])
	astStep := feature.FindStep(pickleStep.AstNodeIds[0])

	var astBackgroundStep bool
	var firstExecutedBackgroundStep bool
	var backgroundSteps int

	if astBackground != nil {
		backgroundSteps = len(astBackground.Steps)

		for idx, step := range astBackground.Steps {
			if step.Id == pickleStep.AstNodeIds[0] {
				astBackgroundStep = true
				firstExecutedBackgroundStep = idx == 0
				break
			}
		}
	}

	firstPickle := isFirstPickleAndNoRule(feature, pickle, astRule) || isFirstScenarioInRule(astRule, astScenario)

	if astBackgroundStep && !firstPickle {
		return
	}

	if astBackgroundStep && firstExecutedBackgroundStep {
		fmt.Fprintln(f.out, "\n"+s(f.indent)+keywordAndName(astBackground.Keyword, astBackground.Name))
	}

	if !astBackgroundStep && len(astScenario.Examples) > 0 {
		f.printOutlineExample(pickle, pickleStep, backgroundSteps)
		return
	}

	scenarioHeaderLength, maxLength := f.scenarioLengths(pickle)
	stepLength := f.lengthPickleStep(astStep.Keyword, pickleStep.Text)

	firstExecutedScenarioStep := astScenario.Steps[0].Id == pickleStep.AstNodeIds[0]
	if !astBackgroundStep && firstExecutedScenarioStep {
		f.printScenarioHeader(pickle, astScenario, maxLength-scenarioHeaderLength)
	}

	pickleStepResult := f.Storage.MustGetPickleStepResult(pickleStep.Id)
	text := s(f.indent*2) + pickleStepResult.Status.Color()(strings.TrimSpace(astStep.Keyword)) + " " + pickleStepResult.Status.Color()(pickleStep.Text)
	if pickleStepResult.Def != nil {
		text += s(maxLength - stepLength + 1)
		text += blackb("# " + DefinitionID(pickleStepResult.Def))
	}
	fmt.Fprintln(f.out, text)

	if pickleStep.Argument != nil {
		if table := pickleStep.Argument.DataTable; table != nil {
			f.printTable(table, cyan)
		}

		if docString := astStep.DocString; docString != nil {
			f.printDocString(docString)
		}
	}

	if pickleStepResult.Err != nil {
		fmt.Fprintln(f.out, s(f.indent*2)+redb(fmt.Sprintf("%+v", pickleStepResult.Err)))
	}

	if pickleStepResult.Status == pending {
		fmt.Fprintln(f.out, s(f.indent*3)+yellow("TODO: write pending definition"))
	}
}

func (f *Pretty) printDocString(docString *messages.DocString) {
	var ct string

	if len(docString.MediaType) > 0 {
		ct = " " + cyan(docString.MediaType)
	}

	fmt.Fprintln(f.out, s(f.indent*3)+cyan(docString.Delimiter)+ct)

	for _, ln := range strings.Split(docString.Content, "\n") {
		fmt.Fprintln(f.out, s(f.indent*3)+cyan(ln))
	}

	fmt.Fprintln(f.out, s(f.indent*3)+cyan(docString.Delimiter))
}

// print table with aligned table cells
// @TODO: need to make example header cells bold
func (f *Pretty) printTable(t *messages.PickleTable, c colors.ColorFunc) {
	maxColLengths := maxColLengths(t, c)
	var cols = make([]string, len(t.Rows[0].Cells))

	for _, row := range t.Rows {
		for i, cell := range row.Cells {
			val := c(cell.Value)
			colLength := utf8.RuneCountInString(val)
			cols[i] = val + s(maxColLengths[i]-colLength)
		}

		fmt.Fprintln(f.out, s(f.indent*3)+"| "+strings.Join(cols, " | ")+" |")
	}
}

// longest gives a list of longest columns of all rows in Table
func maxColLengths(t *messages.PickleTable, clrs ...colors.ColorFunc) []int {
	if t == nil {
		return []int{}
	}

	longest := make([]int, len(t.Rows[0].Cells))
	for _, row := range t.Rows {
		for i, cell := range row.Cells {
			for _, c := range clrs {
				ln := utf8.RuneCountInString(c(cell.Value))
				if longest[i] < ln {
					longest[i] = ln
				}
			}

			ln := utf8.RuneCountInString(cell.Value)
			if longest[i] < ln {
				longest[i] = ln
			}
		}
	}

	return longest
}

func longestExampleRow(t *messages.Examples, clrs ...colors.ColorFunc) []int {
	if t == nil {
		return []int{}
	}

	longest := make([]int, len(t.TableHeader.Cells))
	for i, cell := range t.TableHeader.Cells {
		for _, c := range clrs {
			ln := utf8.RuneCountInString(c(cell.Value))
			if longest[i] < ln {
				longest[i] = ln
			}
		}

		ln := utf8.RuneCountInString(cell.Value)
		if longest[i] < ln {
			longest[i] = ln
		}
	}

	for _, row := range t.TableBody {
		for i, cell := range row.Cells {
			for _, c := range clrs {
				ln := utf8.RuneCountInString(c(cell.Value))
				if longest[i] < ln {
					longest[i] = ln
				}
			}

			ln := utf8.RuneCountInString(cell.Value)
			if longest[i] < ln {
				longest[i] = ln
			}
		}
	}

	return longest
}

func (f *Pretty) longestStep(steps []*messages.Step, pickleLength int) int {
	max := pickleLength

	for _, step := range steps {
		length := f.lengthPickleStep(step.Keyword, step.Text)
		if length > max {
			max = length
		}
	}

	return max
}

// a line number representation in feature file
func line(path string, loc *messages.Location) string {
	// Path can contain a line number already.
	// This line number has to be trimmed to avoid duplication.
	path = strings.TrimSuffix(path, fmt.Sprintf(":%d", loc.Line))
	return " " + blackb(fmt.Sprintf("# %s:%d", path, loc.Line))
}

func (f *Pretty) lengthPickleStep(keyword, text string) int {
	return f.indent*2 + utf8.RuneCountInString(strings.TrimSpace(keyword)+" "+text)
}

func (f *Pretty) lengthPickle(keyword, name string) int {
	return f.indent + utf8.RuneCountInString(strings.TrimSpace(keyword)+": "+name)
}
```

## File: `internal/formatters/fmt_progress.go`
```go
package formatters

import (
	"fmt"
	"io"
	"math"
	"sort"
	"strings"

	"github.com/cucumber/godog/formatters"
	messages "github.com/cucumber/messages/go/v21"
)

func init() {
	formatters.Format("progress", "Prints a character per step.", ProgressFormatterFunc)
}

// ProgressFormatterFunc implements the FormatterFunc for the progress formatter.
func ProgressFormatterFunc(suite string, out io.Writer) formatters.Formatter {
	return NewProgress(suite, out)
}

// NewProgress creates a new progress formatter.
func NewProgress(suite string, out io.Writer) *Progress {
	steps := 0
	return &Progress{
		Base:        NewBase(suite, out),
		StepsPerRow: 70,
		Steps:       &steps,
	}
}

// Progress is a minimalistic formatter.
type Progress struct {
	*Base
	StepsPerRow int
	Steps       *int
}

// Summary renders summary information.
func (f *Progress) Summary() {
	left := math.Mod(float64(*f.Steps), float64(f.StepsPerRow))
	if left != 0 {
		if *f.Steps > f.StepsPerRow {
			fmt.Fprintf(f.out, s(f.StepsPerRow-int(left))+fmt.Sprintf(" %d\n", *f.Steps))
		} else {
			fmt.Fprintf(f.out, " %d\n", *f.Steps)
		}
	}

	var failedStepsOutput []string

	failedSteps := f.Storage.MustGetPickleStepResultsByStatus(failed)
	sort.Sort(sortPickleStepResultsByPickleStepID(failedSteps))

	for _, sr := range failedSteps {
		if sr.Status == failed {
			pickle := f.Storage.MustGetPickle(sr.PickleID)
			pickleStep := f.Storage.MustGetPickleStep(sr.PickleStepID)
			feature := f.Storage.MustGetFeature(pickle.Uri)

			sc := feature.FindScenario(pickle.AstNodeIds[0])
			scenarioDesc := fmt.Sprintf("%s: %s", sc.Keyword, pickle.Name)
			scenarioLine := fmt.Sprintf("%s:%d", pickle.Uri, sc.Location.Line)

			step := feature.FindStep(pickleStep.AstNodeIds[0])
			stepDesc := strings.TrimSpace(step.Keyword) + " " + pickleStep.Text
			stepLine := fmt.Sprintf("%s:%d", pickle.Uri, step.Location.Line)

			failedStepsOutput = append(
				failedStepsOutput,
				s(2)+red(scenarioDesc)+blackb(" # "+scenarioLine),
				s(4)+red(stepDesc)+blackb(" # "+stepLine),
				s(6)+red("Error: ")+redb(fmt.Sprintf("%+v", sr.Err)),
				"",
			)
		}
	}

	if len(failedStepsOutput) > 0 {
		fmt.Fprintln(f.out, "\n\n--- "+red("Failed steps:")+"\n")
		fmt.Fprint(f.out, strings.Join(failedStepsOutput, "\n"))
	}
	fmt.Fprintln(f.out, "")

	f.Base.Summary()
}

func (f *Progress) step(pickleStepID string) {
	pickleStepResult := f.Storage.MustGetPickleStepResult(pickleStepID)

	switch pickleStepResult.Status {
	case passed:
		fmt.Fprint(f.out, green("."))
	case skipped:
		fmt.Fprint(f.out, cyan("-"))
	case failed:
		fmt.Fprint(f.out, red("F"))
	case undefined:
		fmt.Fprint(f.out, yellow("U"))
	case ambiguous:
		fmt.Fprint(f.out, yellow("A"))
	case pending:
		fmt.Fprint(f.out, yellow("P"))
	}

	*f.Steps++

	if math.Mod(float64(*f.Steps), float64(f.StepsPerRow)) == 0 {
		fmt.Fprintf(f.out, " %d\n", *f.Steps)
	}
}

// Passed captures passed step.
func (f *Progress) Passed(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Passed(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(step.Id)
}

// Skipped captures skipped step.
func (f *Progress) Skipped(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Skipped(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(step.Id)
}

// Undefined captures undefined step.
func (f *Progress) Undefined(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Undefined(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(step.Id)
}

// Failed captures failed step.
func (f *Progress) Failed(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition, err error) {
	f.Base.Failed(pickle, step, match, err)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(step.Id)
}

// Ambiguous steps.
func (f *Progress) Ambiguous(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition, err error) {
	f.Base.Ambiguous(pickle, step, match, err)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(step.Id)
}

// Pending captures pending step.
func (f *Progress) Pending(pickle *messages.Pickle, step *messages.PickleStep, match *formatters.StepDefinition) {
	f.Base.Pending(pickle, step, match)

	f.Lock.Lock()
	defer f.Lock.Unlock()

	f.step(step.Id)
}
```

## File: `internal/formatters/undefined_snippets_gen.go`
```go
package formatters

import (
	"fmt"
	"reflect"
	"regexp"
	"strings"
	"text/template"

	messages "github.com/cucumber/messages/go/v21"
)

// some snippet formatting regexps
var snippetExprCleanup = regexp.MustCompile(`([\/\[\]\(\)\\^\$\.\|\?\*\+\'])`)
var snippetExprQuoted = regexp.MustCompile(`(\W|^)"(?:[^"]*)"(\W|$)`)
var snippetMethodName = regexp.MustCompile(`[^a-zA-Z\_\ ]`)
var snippetNumbers = regexp.MustCompile(`(\d+)`)

var snippetHelperFuncs = template.FuncMap{
	"backticked": func(s string) string {
		return "`" + s + "`"
	},
}

var undefinedSnippetsTpl = template.Must(template.New("snippets").Funcs(snippetHelperFuncs).Parse(`
{{ range . }}func {{ .Method }}({{ .Args }}) error {
	return godog.ErrPending
}

{{end}}func InitializeScenario(ctx *godog.ScenarioContext) { {{ range . }}
	ctx.Step({{ backticked .Expr }}, {{ .Method }}){{end}}
}
`))

type undefinedSnippet struct {
	Method   string
	Expr     string
	argument *messages.PickleStepArgument
}

func (s undefinedSnippet) Args() (ret string) {
	var (
		args      []string
		pos       int
		breakLoop bool
	)

	for !breakLoop {
		part := s.Expr[pos:]
		ipos := strings.Index(part, "(\\d+)")
		spos := strings.Index(part, "\"([^\"]*)\"")

		switch {
		case spos == -1 && ipos == -1:
			breakLoop = true
		case spos == -1:
			pos += ipos + len("(\\d+)")
			args = append(args, reflect.Int.String())
		case ipos == -1:
			pos += spos + len("\"([^\"]*)\"")
			args = append(args, reflect.String.String())
		case ipos < spos:
			pos += ipos + len("(\\d+)")
			args = append(args, reflect.Int.String())
		case spos < ipos:
			pos += spos + len("\"([^\"]*)\"")
			args = append(args, reflect.String.String())
		}
	}

	if s.argument != nil {
		if s.argument.DocString != nil {
			args = append(args, "*godog.DocString")
		}

		if s.argument.DataTable != nil {
			args = append(args, "*godog.Table")
		}
	}

	var last string

	for i, arg := range args {
		if last == "" || last == arg {
			ret += fmt.Sprintf("arg%d, ", i+1)
		} else {
			ret = strings.TrimRight(ret, ", ") + fmt.Sprintf(" %s, arg%d, ", last, i+1)
		}

		last = arg
	}

	return strings.TrimSpace(strings.TrimRight(ret, ", ") + " " + last)
}

type snippetSortByMethod []undefinedSnippet

func (s snippetSortByMethod) Len() int {
	return len(s)
}

func (s snippetSortByMethod) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s snippetSortByMethod) Less(i, j int) bool {
	return s[i].Method < s[j].Method
}
```

## File: `internal/formatters/utils_test.go`
```go
package formatters

import (
	"testing"
	"time"

	"github.com/cucumber/godog/internal/utils"
)

// this zeroes the time throughout whole test suite
// and makes it easier to assert output
// activated only when godog tests are being run
func init() {
	utils.TimeNowFunc = func() time.Time {
		return time.Time{}
	}
}

func TestTimeNowFunc(t *testing.T) {
	now := utils.TimeNowFunc()
	if !now.IsZero() {
		t.Fatalf("expected zeroed time, but got: %s", now.Format(time.RFC3339))
	}
}
```

## File: `internal/formatters/formatter-tests/cucumber/empty`
```
[]
```

## File: `internal/formatters/formatter-tests/cucumber/empty_with_description`
```
[]
```

## File: `internal/formatters/formatter-tests/cucumber/empty_with_single_scenario_without_steps`
```
[
    {
        "uri": "formatter-tests/features/empty_with_single_scenario_without_steps.feature",
        "id": "empty-feature",
        "keyword": "Feature",
        "name": "empty feature",
        "description": "",
        "line": 1,
        "elements": [
            {
                "id": "empty-feature;without-steps",
                "keyword": "Scenario",
                "name": "without steps",
                "description": "",
                "line": 3,
                "type": "scenario"
            }
        ]
    }
]
```

## File: `internal/formatters/formatter-tests/cucumber/empty_with_single_scenario_without_steps_and_description`
```
[
    {
        "uri": "formatter-tests/features/empty_with_single_scenario_without_steps_and_description.feature",
        "id": "empty-feature",
        "keyword": "Feature",
        "name": "empty feature",
        "description": "  describes\n  an empty\n  feature",
        "line": 1,
        "elements": [
            {
                "id": "empty-feature;without-steps",
                "keyword": "Scenario",
                "name": "without steps",
                "description": "",
                "line": 6,
                "type": "scenario"
            }
        ]
    }
]
```

## File: `internal/formatters/formatter-tests/cucumber/scenario_outline`
```
[
    {
        "uri": "formatter-tests/features/scenario_outline.feature",
        "id": "outline",
        "keyword": "Feature",
        "name": "outline",
        "description": "",
        "line": 2,
        "tags": [
            {
                "name": "@outline",
                "line": 1
            },
            {
                "name": "@tag",
                "line": 1
            }
        ],
        "elements": [
            {
                "id": "outline;outline;tagged;2",
                "keyword": "Scenario Outline",
                "name": "outline",
                "description": "",
                "line": 13,
                "type": "scenario",
                "tags": [
                    {
                        "name": "@outline",
                        "line": 1
                    },
                    {
                        "name": "@tag",
                        "line": 1
                    },
                    {
                        "name": "@scenario",
                        "line": 4
                    },
                    {
                        "name": "@tagged",
                        "line": 10
                    }
                ],
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "passing step",
                        "line": 6,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "When ",
                        "name": "passing step",
                        "line": 7,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "odd 1 and even 2 number",
                        "line": 8,
                        "match": {
                            "location": "fmt_output_test.go:103"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    }
                ]
            },
            {
                "id": "outline;outline;tagged;3",
                "keyword": "Scenario Outline",
                "name": "outline",
                "description": "",
                "line": 14,
                "type": "scenario",
                "tags": [
                    {
                        "name": "@outline",
                        "line": 1
                    },
                    {
                        "name": "@tag",
                        "line": 1
                    },
                    {
                        "name": "@scenario",
                        "line": 4
                    },
                    {
                        "name": "@tagged",
                        "line": 10
                    }
                ],
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "passing step",
                        "line": 6,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "When ",
                        "name": "passing step",
                        "line": 7,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "odd 2 and even 0 number",
                        "line": 8,
                        "match": {
                            "location": "fmt_output_test.go:103"
                        },
                        "result": {
                            "status": "failed",
                            "error_message": "2 is not odd",
                            "duration": 0
                        }
                    }
                ]
            },
            {
                "id": "outline;outline;tagged;4",
                "keyword": "Scenario Outline",
                "name": "outline",
                "description": "",
                "line": 15,
                "type": "scenario",
                "tags": [
                    {
                        "name": "@outline",
                        "line": 1
                    },
                    {
                        "name": "@tag",
                        "line": 1
                    },
                    {
                        "name": "@scenario",
                        "line": 4
                    },
                    {
                        "name": "@tagged",
                        "line": 10
                    }
                ],
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "passing step",
                        "line": 6,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "When ",
                        "name": "passing step",
                        "line": 7,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "odd 3 and even 11 number",
                        "line": 8,
                        "match": {
                            "location": "fmt_output_test.go:103"
                        },
                        "result": {
                            "status": "failed",
                            "error_message": "11 is not even",
                            "duration": 0
                        }
                    }
                ]
            },
            {
                "id": "outline;outline;;2",
                "keyword": "Scenario Outline",
                "name": "outline",
                "description": "",
                "line": 20,
                "type": "scenario",
                "tags": [
                    {
                        "name": "@outline",
                        "line": 1
                    },
                    {
                        "name": "@tag",
                        "line": 1
                    },
                    {
                        "name": "@scenario",
                        "line": 4
                    },
                    {
                        "name": "@tag2",
                        "line": 17
                    }
                ],
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "passing step",
                        "line": 6,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "When ",
                        "name": "passing step",
                        "line": 7,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "odd 1 and even 14 number",
                        "line": 8,
                        "match": {
                            "location": "fmt_output_test.go:103"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    }
                ]
            },
            {
                "id": "outline;outline;;3",
                "keyword": "Scenario Outline",
                "name": "outline",
                "description": "",
                "line": 21,
                "type": "scenario",
                "tags": [
                    {
                        "name": "@outline",
                        "line": 1
                    },
                    {
                        "name": "@tag",
                        "line": 1
                    },
                    {
                        "name": "@scenario",
                        "line": 4
                    },
                    {
                        "name": "@tag2",
                        "line": 17
                    }
                ],
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "passing step",
                        "line": 6,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "When ",
                        "name": "passing step",
                        "line": 7,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "odd 3 and even 9 number",
                        "line": 8,
                        "match": {
                            "location": "fmt_output_test.go:103"
                        },
                        "result": {
                            "status": "failed",
                            "error_message": "9 is not even",
                            "duration": 0
                        }
                    }
                ]
            }
        ]
    }
]
```

## File: `internal/formatters/formatter-tests/cucumber/scenario_with_attachment`
```
[
    {
        "uri": "formatter-tests/features/scenario_with_attachment.feature",
        "id": "feature-with-attachment",
        "keyword": "Feature",
        "name": "feature with attachment",
        "description": "  describes\n  an attachment\n  feature",
        "line": 1,
        "elements": [
            {
                "id": "feature-with-attachment;scenario-with-attachment",
                "keyword": "Scenario",
                "name": "scenario with attachment",
                "description": "",
                "line": 6,
                "type": "scenario",
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "a step with a single attachment call for multiple attachments",
                        "line": 7,
                        "match": {
                            "location": "fmt_output_test.go:119"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        },
                        "embeddings": [
                            {
                                "name": "Before Scenario Attachment 1",
                                "mime_type": "text/plain",
                                "data": "QmVmb3JlU2NlbmFyaW9BdHRhY2htZW50"
                            },
                            {
                                "name": "Before Step Attachment 3",
                                "mime_type": "text/plain",
                                "data": "QmVmb3JlU3RlcEF0dGFjaG1lbnQ="
                            },
                            {
                                "name": "TheFilename1",
                                "mime_type": "text/plain",
                                "data": "VGhlRGF0YTE="
                            },
                            {
                                "name": "TheFilename2",
                                "mime_type": "text/plain",
                                "data": "VGhlRGF0YTI="
                            },
                            {
                                "name": "After Step Attachment 4",
                                "mime_type": "text/plain",
                                "data": "QWZ0ZXJTdGVwQXR0YWNobWVudA=="
                            }
                        ]
                    },
                    {
                        "keyword": "And ",
                        "name": "a step with multiple attachment calls",
                        "line": 8,
                        "match": {
                            "location": "fmt_output_test.go:119"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        },
                        "embeddings": [
                            {
                                "name": "Before Step Attachment 3",
                                "mime_type": "text/plain",
                                "data": "QmVmb3JlU3RlcEF0dGFjaG1lbnQ="
                            },
                            {
                                "name": "TheFilename3",
                                "mime_type": "text/plain",
                                "data": "VGhlRGF0YTE="
                            },
                            {
                                "name": "TheFilename4",
                                "mime_type": "text/plain",
                                "data": "VGhlRGF0YTI="
                            },
                            {
                                "name": "After Step Attachment 4",
                                "mime_type": "text/plain",
                                "data": "QWZ0ZXJTdGVwQXR0YWNobWVudA=="
                            },
                            {
                                "name": "After Scenario Attachment 2",
                                "mime_type": "text/plain",
                                "data": "QWZ0ZXJTY2VuYXJpb0F0dGFjaG1lbnQ="
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
```

## File: `internal/formatters/formatter-tests/cucumber/scenario_with_background`
```
[
    {
        "uri": "formatter-tests/features/scenario_with_background.feature",
        "id": "single-scenario-with-background",
        "keyword": "Feature",
        "name": "single scenario with background",
        "description": "",
        "line": 1,
        "elements": [
            {
                "id": "single-scenario-with-background;scenario",
                "keyword": "Scenario",
                "name": "scenario",
                "description": "",
                "line": 7,
                "type": "scenario",
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "passing step",
                        "line": 4,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "And ",
                        "name": "passing step",
                        "line": 5,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "When ",
                        "name": "passing step",
                        "line": 8,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "passing step",
                        "line": 9,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    }
                ]
            }
        ]
    }
]
```

## File: `internal/formatters/formatter-tests/cucumber/scenario_without_steps_with_background`
```
[
    {
        "uri": "formatter-tests/features/scenario_without_steps_with_background.feature",
        "id": "empty-feature",
        "keyword": "Feature",
        "name": "empty feature",
        "description": "",
        "line": 1,
        "elements": [
            {
                "id": "empty-feature;without-steps",
                "keyword": "Scenario",
                "name": "without steps",
                "description": "",
                "line": 6,
                "type": "scenario"
            }
        ]
    }
]
```

## File: `internal/formatters/formatter-tests/cucumber/single_scenario_with_passing_step`
```
[
    {
        "uri": "formatter-tests/features/single_scenario_with_passing_step.feature",
        "id": "single-passing-scenario",
        "keyword": "Feature",
        "name": "single passing scenario",
        "description": "  describes\n  a single scenario\n  feature",
        "line": 1,
        "elements": [
            {
                "id": "single-passing-scenario;one-step-passing",
                "keyword": "Scenario",
                "name": "one step passing",
                "description": "",
                "line": 6,
                "type": "scenario",
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "a passing step",
                        "line": 7,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    }
                ]
            }
        ]
    }
]
```

## File: `internal/formatters/formatter-tests/cucumber/some_scenarios_including_failing`
```
[
    {
        "uri": "formatter-tests/features/some_scenarios_including_failing.feature",
        "id": "some-scenarios",
        "keyword": "Feature",
        "name": "some scenarios",
        "description": "",
        "line": 1,
        "elements": [
            {
                "id": "some-scenarios;failing",
                "keyword": "Scenario",
                "name": "failing",
                "description": "",
                "line": 3,
                "type": "scenario",
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "passing step",
                        "line": 4,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "When ",
                        "name": "failing step",
                        "line": 5,
                        "match": {
                            "location": "fmt_output_test.go:117"
                        },
                        "result": {
                            "status": "failed",
                            "error_message": "step failed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "passing step",
                        "line": 6,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "skipped"
                        }
                    }
                ]
            },
            {
                "id": "some-scenarios;pending",
                "keyword": "Scenario",
                "name": "pending",
                "description": "",
                "line": 8,
                "type": "scenario",
                "steps": [
                    {
                        "keyword": "When ",
                        "name": "pending step",
                        "line": 9,
                        "match": {
                            "location": "formatter-tests/features/some_scenarios_including_failing.feature:9"
                        },
                        "result": {
                            "status": "pending"
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "passing step",
                        "line": 10,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "skipped"
                        }
                    }
                ]
            },
            {
                "id": "some-scenarios;undefined",
                "keyword": "Scenario",
                "name": "undefined",
                "description": "",
                "line": 12,
                "type": "scenario",
                "steps": [
                    {
                        "keyword": "When ",
                        "name": "undefined",
                        "line": 13,
                        "match": {
                            "location": "formatter-tests/features/some_scenarios_including_failing.feature:13"
                        },
                        "result": {
                            "status": "undefined"
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "passing step",
                        "line": 14,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "skipped"
                        }
                    }
                ]
            },
            {
                "id": "some-scenarios;ambiguous",
                "keyword": "Scenario",
                "name": "ambiguous",
                "description": "",
                "line": 16,
                "type": "scenario",
                "steps": [
                    {
                        "keyword": "When ",
                        "name": "ambiguous step",
                        "line": 17,
                        "match": {
                            "location": "formatter-tests/features/some_scenarios_including_failing.feature:17"
                        },
                        "result": {
                            "status": "ambiguous",
                            "error_message": "ambiguous step definition, step text: ambiguous step\n    matches:\n        ^ambiguous step.*$\n        ^ambiguous step$"
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "passing step",
                        "line": 18,
                        "match": {
                            "location": "fmt_output_test.go:XXX"
                        },
                        "result": {
                            "status": "skipped"
                        }
                    }
                ]
            }
        ]
    }
]
```

## File: `internal/formatters/formatter-tests/cucumber/two_scenarios_with_background_fail`
```
[
    {
        "uri": "formatter-tests/features/two_scenarios_with_background_fail.feature",
        "id": "two-scenarios-with-background-fail",
        "keyword": "Feature",
        "name": "two scenarios with background fail",
        "description": "",
        "line": 1,
        "elements": [
            {
                "id": "two-scenarios-with-background-fail;one",
                "keyword": "Scenario",
                "name": "one",
                "description": "",
                "line": 7,
                "type": "scenario",
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "passing step",
                        "line": 4,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "And ",
                        "name": "failing step",
                        "line": 5,
                        "match": {
                            "location": "fmt_output_test.go:117"
                        },
                        "result": {
                            "status": "failed",
                            "error_message": "step failed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "When ",
                        "name": "passing step",
                        "line": 8,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "skipped"
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "passing step",
                        "line": 9,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "skipped"
                        }
                    }
                ]
            },
            {
                "id": "two-scenarios-with-background-fail;two",
                "keyword": "Scenario",
                "name": "two",
                "description": "",
                "line": 11,
                "type": "scenario",
                "steps": [
                    {
                        "keyword": "Given ",
                        "name": "passing step",
                        "line": 4,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "passed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "And ",
                        "name": "failing step",
                        "line": 5,
                        "match": {
                            "location": "fmt_output_test.go:117"
                        },
                        "result": {
                            "status": "failed",
                            "error_message": "step failed",
                            "duration": 0
                        }
                    },
                    {
                        "keyword": "Then ",
                        "name": "passing step",
                        "line": 12,
                        "match": {
                            "location": "fmt_output_test.go:101"
                        },
                        "result": {
                            "status": "skipped"
                        }
                    }
                ]
            }
        ]
    }
]
```

## File: `internal/formatters/formatter-tests/cucumber/with_few_empty_scenarios`
```
[
    {
        "uri": "formatter-tests/features/with_few_empty_scenarios.feature",
        "id": "few-empty-scenarios",
        "keyword": "Feature",
        "name": "few empty scenarios",
        "description": "",
        "line": 1,
        "elements": [
            {
                "id": "few-empty-scenarios;one",
                "keyword": "Scenario",
                "name": "one",
                "description": "",
                "line": 3,
                "type": "scenario"
            },
            {
                "id": "few-empty-scenarios;two;first-group;2",
                "keyword": "Scenario Outline",
                "name": "two",
                "description": "",
                "line": 9,
                "type": "scenario"
            },
            {
                "id": "few-empty-scenarios;two;first-group;3",
                "keyword": "Scenario Outline",
                "name": "two",
                "description": "",
                "line": 10,
                "type": "scenario"
            },
            {
                "id": "few-empty-scenarios;two;second-group;2",
                "keyword": "Scenario Outline",
                "name": "two",
                "description": "",
                "line": 14,
                "type": "scenario"
            },
            {
                "id": "few-empty-scenarios;three",
                "keyword": "Scenario",
                "name": "three",
                "description": "",
                "line": 16,
                "type": "scenario"
            }
        ]
    }
]
```

## File: `internal/formatters/formatter-tests/events/empty`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestRunFinished","status":"pending","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/events/empty_with_description`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestRunFinished","status":"pending","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/events/empty_with_single_scenario_without_steps`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestSource","location":"formatter-tests/features/empty_with_single_scenario_without_steps.feature:1","source":"Feature: empty feature\n\n  Scenario: without steps\n"}
{"event":"TestCaseStarted","location":"formatter-tests/features/empty_with_single_scenario_without_steps.feature:3","timestamp":-6795364578871}
{"event":"TestCaseFinished","location":"formatter-tests/features/empty_with_single_scenario_without_steps.feature:3","timestamp":-6795364578871,"status":"undefined"}
{"event":"TestRunFinished","status":"pending","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/events/empty_with_single_scenario_without_steps_and_description`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestSource","location":"formatter-tests/features/empty_with_single_scenario_without_steps_and_description.feature:1","source":"Feature: empty feature\n  describes\n  an empty\n  feature\n\n  Scenario: without steps\n"}
{"event":"TestCaseStarted","location":"formatter-tests/features/empty_with_single_scenario_without_steps_and_description.feature:6","timestamp":-6795364578871}
{"event":"TestCaseFinished","location":"formatter-tests/features/empty_with_single_scenario_without_steps_and_description.feature:6","timestamp":-6795364578871,"status":"undefined"}
{"event":"TestRunFinished","status":"pending","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/events/scenario_outline`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestSource","location":"formatter-tests/features/scenario_outline.feature:2","source":"@outline @tag\nFeature: outline\n\n  @scenario\n  Scenario Outline: outline\n    Given passing step\n    When passing step\n    Then odd \u003codd\u003e and even \u003ceven\u003e number\n\n    @tagged\n    Examples: tagged\n      | odd | even |\n      | 1   | 2    |\n      | 2   | 0    |\n      | 3   | 11   |\n\n    @tag2\n    Examples:\n      | odd | even |\n      | 1   | 14   |\n      | 3   | 9    |\n"}
{"event":"TestCaseStarted","location":"formatter-tests/features/scenario_outline.feature:13","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:6","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:6","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:6","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:7","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:7","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:7","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:8","definition_id":"fmt_output_test.go:103 -\u003e github.com/cucumber/godog/internal/formatters_test.oddEvenStepDef","arguments":[[4,5],[5,15]]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:8","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:8","timestamp":-6795364578871,"status":"passed"}
{"event":"TestCaseFinished","location":"formatter-tests/features/scenario_outline.feature:13","timestamp":-6795364578871,"status":"passed"}
{"event":"TestCaseStarted","location":"formatter-tests/features/scenario_outline.feature:14","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:6","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:6","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:6","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:7","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:7","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:7","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:8","definition_id":"fmt_output_test.go:103 -\u003e github.com/cucumber/godog/internal/formatters_test.oddEvenStepDef","arguments":[[4,5],[5,15]]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:8","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:8","timestamp":-6795364578871,"status":"failed","summary":"2 is not odd"}
{"event":"TestCaseFinished","location":"formatter-tests/features/scenario_outline.feature:14","timestamp":-6795364578871,"status":"failed"}
{"event":"TestCaseStarted","location":"formatter-tests/features/scenario_outline.feature:15","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:6","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:6","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:6","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:7","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:7","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:7","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:8","definition_id":"fmt_output_test.go:103 -\u003e github.com/cucumber/godog/internal/formatters_test.oddEvenStepDef","arguments":[[4,5],[5,15]]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:8","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:8","timestamp":-6795364578871,"status":"failed","summary":"11 is not even"}
{"event":"TestCaseFinished","location":"formatter-tests/features/scenario_outline.feature:15","timestamp":-6795364578871,"status":"failed"}
{"event":"TestCaseStarted","location":"formatter-tests/features/scenario_outline.feature:20","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:6","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:6","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:6","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:7","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:7","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:7","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:8","definition_id":"fmt_output_test.go:103 -\u003e github.com/cucumber/godog/internal/formatters_test.oddEvenStepDef","arguments":[[4,5],[5,15]]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:8","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:8","timestamp":-6795364578871,"status":"passed"}
{"event":"TestCaseFinished","location":"formatter-tests/features/scenario_outline.feature:20","timestamp":-6795364578871,"status":"passed"}
{"event":"TestCaseStarted","location":"formatter-tests/features/scenario_outline.feature:21","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:6","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:6","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:6","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:7","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:7","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:7","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_outline.feature:8","definition_id":"fmt_output_test.go:103 -\u003e github.com/cucumber/godog/internal/formatters_test.oddEvenStepDef","arguments":[[4,5],[5,15]]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_outline.feature:8","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_outline.feature:8","timestamp":-6795364578871,"status":"failed","summary":"9 is not even"}
{"event":"TestCaseFinished","location":"formatter-tests/features/scenario_outline.feature:21","timestamp":-6795364578871,"status":"failed"}
{"event":"TestRunFinished","status":"failed","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/events/scenario_with_attachment`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestSource","location":"formatter-tests/features/scenario_with_attachment.feature:1","source":"Feature: feature with attachment\n  describes\n  an attachment\n  feature\n\n  Scenario: scenario with attachment\n    Given a step with a single attachment call for multiple attachments\n    And a step with multiple attachment calls\n"}
{"event":"TestCaseStarted","location":"formatter-tests/features/scenario_with_attachment.feature:6","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_with_attachment.feature:7","definition_id":"fmt_output_test.go:XXX -\u003e github.com/cucumber/godog/internal/formatters_test.stepWithSingleAttachmentCall","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_with_attachment.feature:7","timestamp":-6795364578871}
{"event":"Attachment","location":"formatter-tests/features/scenario_with_attachment.feature:7","timestamp":-6795364578871,"contentEncoding":"BASE64","fileName":"Before Scenario Attachment 1","mimeType":"text/plain","body":"BeforeScenarioAttachment"}
{"event":"Attachment","location":"formatter-tests/features/scenario_with_attachment.feature:7","timestamp":-6795364578871,"contentEncoding":"BASE64","fileName":"Before Step Attachment 3","mimeType":"text/plain","body":"BeforeStepAttachment"}
{"event":"Attachment","location":"formatter-tests/features/scenario_with_attachment.feature:7","timestamp":-6795364578871,"contentEncoding":"BASE64","fileName":"TheFilename1","mimeType":"text/plain","body":"TheData1"}
{"event":"Attachment","location":"formatter-tests/features/scenario_with_attachment.feature:7","timestamp":-6795364578871,"contentEncoding":"BASE64","fileName":"TheFilename2","mimeType":"text/plain","body":"TheData2"}
{"event":"Attachment","location":"formatter-tests/features/scenario_with_attachment.feature:7","timestamp":-6795364578871,"contentEncoding":"BASE64","fileName":"After Step Attachment 4","mimeType":"text/plain","body":"AfterStepAttachment"}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_with_attachment.feature:7","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_with_attachment.feature:8","definition_id":"fmt_output_test.go:XXX -\u003e github.com/cucumber/godog/internal/formatters_test.stepWithMultipleAttachmentCalls","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_with_attachment.feature:8","timestamp":-6795364578871}
{"event":"Attachment","location":"formatter-tests/features/scenario_with_attachment.feature:8","timestamp":-6795364578871,"contentEncoding":"BASE64","fileName":"Before Step Attachment 3","mimeType":"text/plain","body":"BeforeStepAttachment"}
{"event":"Attachment","location":"formatter-tests/features/scenario_with_attachment.feature:8","timestamp":-6795364578871,"contentEncoding":"BASE64","fileName":"TheFilename3","mimeType":"text/plain","body":"TheData1"}
{"event":"Attachment","location":"formatter-tests/features/scenario_with_attachment.feature:8","timestamp":-6795364578871,"contentEncoding":"BASE64","fileName":"TheFilename4","mimeType":"text/plain","body":"TheData2"}
{"event":"Attachment","location":"formatter-tests/features/scenario_with_attachment.feature:8","timestamp":-6795364578871,"contentEncoding":"BASE64","fileName":"After Step Attachment 4","mimeType":"text/plain","body":"AfterStepAttachment"}
{"event":"Attachment","location":"formatter-tests/features/scenario_with_attachment.feature:8","timestamp":-6795364578871,"contentEncoding":"BASE64","fileName":"After Scenario Attachment 2","mimeType":"text/plain","body":"AfterScenarioAttachment"}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_with_attachment.feature:8","timestamp":-6795364578871,"status":"passed"}
{"event":"TestCaseFinished","location":"formatter-tests/features/scenario_with_attachment.feature:6","timestamp":-6795364578871,"status":"passed"}
{"event":"TestRunFinished","status":"passed","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/events/scenario_with_background`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestSource","location":"formatter-tests/features/scenario_with_background.feature:1","source":"Feature: single scenario with background\n\n  Background: named\n    Given passing step\n    And passing step\n\n  Scenario: scenario\n    When passing step\n    Then passing step\n"}
{"event":"TestCaseStarted","location":"formatter-tests/features/scenario_with_background.feature:7","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_with_background.feature:4","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_with_background.feature:4","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_with_background.feature:4","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_with_background.feature:5","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_with_background.feature:5","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_with_background.feature:5","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_with_background.feature:8","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_with_background.feature:8","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_with_background.feature:8","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/scenario_with_background.feature:9","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/scenario_with_background.feature:9","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/scenario_with_background.feature:9","timestamp":-6795364578871,"status":"passed"}
{"event":"TestCaseFinished","location":"formatter-tests/features/scenario_with_background.feature:7","timestamp":-6795364578871,"status":"passed"}
{"event":"TestRunFinished","status":"passed","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/events/scenario_without_steps_with_background`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestSource","location":"formatter-tests/features/scenario_without_steps_with_background.feature:1","source":"Feature: empty feature\n\n  Background:\n    Given passing step\n\n  Scenario: without steps\n"}
{"event":"TestCaseStarted","location":"formatter-tests/features/scenario_without_steps_with_background.feature:6","timestamp":-6795364578871}
{"event":"TestCaseFinished","location":"formatter-tests/features/scenario_without_steps_with_background.feature:6","timestamp":-6795364578871,"status":"undefined"}
{"event":"TestRunFinished","status":"pending","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/events/single_scenario_with_passing_step`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestSource","location":"formatter-tests/features/single_scenario_with_passing_step.feature:1","source":"Feature: single passing scenario\n  describes\n  a single scenario\n  feature\n\n  Scenario: one step passing\n    Given a passing step\n"}
{"event":"TestCaseStarted","location":"formatter-tests/features/single_scenario_with_passing_step.feature:6","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/single_scenario_with_passing_step.feature:7","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/single_scenario_with_passing_step.feature:7","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/single_scenario_with_passing_step.feature:7","timestamp":-6795364578871,"status":"passed"}
{"event":"TestCaseFinished","location":"formatter-tests/features/single_scenario_with_passing_step.feature:6","timestamp":-6795364578871,"status":"passed"}
{"event":"TestRunFinished","status":"passed","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/events/some_scenarios_including_failing`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestSource","location":"formatter-tests/features/some_scenarios_including_failing.feature:1","source":"Feature: some scenarios\n\n  Scenario: failing\n    Given passing step\n    When failing step\n    Then passing step\n\n  Scenario: pending\n    When pending step\n    Then passing step\n\n  Scenario: undefined\n    When undefined\n    Then passing step\n\n  Scenario: ambiguous\n    When ambiguous step\n    Then passing step\n"}
{"event":"TestCaseStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:3","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/some_scenarios_including_failing.feature:4","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:4","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:4","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/some_scenarios_including_failing.feature:5","definition_id":"fmt_output_test.go:117 -\u003e github.com/cucumber/godog/internal/formatters_test.failingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:5","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:5","timestamp":-6795364578871,"status":"failed","summary":"step failed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/some_scenarios_including_failing.feature:6","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:6","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:6","timestamp":-6795364578871,"status":"skipped"}
{"event":"TestCaseFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:3","timestamp":-6795364578871,"status":"failed"}
{"event":"TestCaseStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:8","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/some_scenarios_including_failing.feature:9","definition_id":"fmt_output_test.go:115 -\u003e github.com/cucumber/godog/internal/formatters_test.pendingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:9","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:9","timestamp":-6795364578871,"status":"pending"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/some_scenarios_including_failing.feature:10","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:10","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:10","timestamp":-6795364578871,"status":"skipped"}
{"event":"TestCaseFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:8","timestamp":-6795364578871,"status":"pending"}
{"event":"TestCaseStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:12","timestamp":-6795364578871}
{"event":"TestStepStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:13","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:13","timestamp":-6795364578871,"status":"undefined"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/some_scenarios_including_failing.feature:14","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:14","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:14","timestamp":-6795364578871,"status":"skipped"}
{"event":"TestCaseFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:12","timestamp":-6795364578871,"status":"undefined"}
{"event":"TestCaseStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:16","timestamp":-6795364578871}
{"event":"TestStepStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:17","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:17","timestamp":-6795364578871,"status":"ambiguous","summary":"ambiguous step definition, step text: ambiguous step\n    matches:\n        ^ambiguous step.*$\n        ^ambiguous step$"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/some_scenarios_including_failing.feature:18","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/some_scenarios_including_failing.feature:18","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:18","timestamp":-6795364578871,"status":"skipped"}
{"event":"TestCaseFinished","location":"formatter-tests/features/some_scenarios_including_failing.feature:16","timestamp":-6795364578871,"status":"ambiguous"}
{"event":"TestRunFinished","status":"failed","timestamp":-6795364578871,"snippets":"You can implement step definitions for undefined steps with these snippets:\n\nfunc undefined() error {\n\treturn godog.ErrPending\n}\n\nfunc InitializeScenario(ctx *godog.ScenarioContext) {\n\tctx.Step(`^undefined$`, undefined)\n}\n","memory":""}
```

## File: `internal/formatters/formatter-tests/events/two_scenarios_with_background_fail`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestSource","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:1","source":"Feature: two scenarios with background fail\n\n  Background:\n    Given passing step\n    And failing step\n\n  Scenario: one\n    When passing step\n    Then passing step\n\n  Scenario: two\n    Then passing step\n"}
{"event":"TestCaseStarted","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:7","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:4","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:4","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:4","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:5","definition_id":"fmt_output_test.go:117 -\u003e github.com/cucumber/godog/internal/formatters_test.failingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:5","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:5","timestamp":-6795364578871,"status":"failed","summary":"step failed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:8","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:8","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:8","timestamp":-6795364578871,"status":"skipped"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:9","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:9","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:9","timestamp":-6795364578871,"status":"skipped"}
{"event":"TestCaseFinished","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:7","timestamp":-6795364578871,"status":"failed"}
{"event":"TestCaseStarted","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:11","timestamp":-6795364578871}
{"event":"StepDefinitionFound","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:4","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:4","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:4","timestamp":-6795364578871,"status":"passed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:5","definition_id":"fmt_output_test.go:117 -\u003e github.com/cucumber/godog/internal/formatters_test.failingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:5","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:5","timestamp":-6795364578871,"status":"failed","summary":"step failed"}
{"event":"StepDefinitionFound","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:12","definition_id":"fmt_output_test.go:101 -\u003e github.com/cucumber/godog/internal/formatters_test.passingStepDef","arguments":[]}
{"event":"TestStepStarted","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:12","timestamp":-6795364578871}
{"event":"TestStepFinished","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:12","timestamp":-6795364578871,"status":"skipped"}
{"event":"TestCaseFinished","location":"formatter-tests/features/two_scenarios_with_background_fail.feature:11","timestamp":-6795364578871,"status":"failed"}
{"event":"TestRunFinished","status":"failed","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/events/with_few_empty_scenarios`
```
{"event":"TestRunStarted","version":"0.1.0","timestamp":-6795364578871,"suite":"events"}
{"event":"TestSource","location":"formatter-tests/features/with_few_empty_scenarios.feature:1","source":"Feature: few empty scenarios\n\n  Scenario: one\n\n  Scenario Outline: two\n\n    Examples: first group\n      | one | two |\n      | 1   | 2   |\n      | 4   | 7   |\n\n    Examples: second group\n      | one | two |\n      | 5   | 9   |\n\n  Scenario: three\n"}
{"event":"TestCaseStarted","location":"formatter-tests/features/with_few_empty_scenarios.feature:3","timestamp":-6795364578871}
{"event":"TestCaseFinished","location":"formatter-tests/features/with_few_empty_scenarios.feature:3","timestamp":-6795364578871,"status":"undefined"}
{"event":"TestCaseStarted","location":"formatter-tests/features/with_few_empty_scenarios.feature:9","timestamp":-6795364578871}
{"event":"TestCaseFinished","location":"formatter-tests/features/with_few_empty_scenarios.feature:9","timestamp":-6795364578871,"status":"undefined"}
{"event":"TestCaseStarted","location":"formatter-tests/features/with_few_empty_scenarios.feature:10","timestamp":-6795364578871}
{"event":"TestCaseFinished","location":"formatter-tests/features/with_few_empty_scenarios.feature:10","timestamp":-6795364578871,"status":"undefined"}
{"event":"TestCaseStarted","location":"formatter-tests/features/with_few_empty_scenarios.feature:14","timestamp":-6795364578871}
{"event":"TestCaseFinished","location":"formatter-tests/features/with_few_empty_scenarios.feature:14","timestamp":-6795364578871,"status":"undefined"}
{"event":"TestCaseStarted","location":"formatter-tests/features/with_few_empty_scenarios.feature:16","timestamp":-6795364578871}
{"event":"TestCaseFinished","location":"formatter-tests/features/with_few_empty_scenarios.feature:16","timestamp":-6795364578871,"status":"undefined"}
{"event":"TestRunFinished","status":"pending","timestamp":-6795364578871,"snippets":"","memory":""}
```

## File: `internal/formatters/formatter-tests/features/empty.feature`
```
Feature: empty feature
```

## File: `internal/formatters/formatter-tests/features/empty_with_description.feature`
```
Feature: empty feature
  describes
  an empty
  feature
```

## File: `internal/formatters/formatter-tests/features/empty_with_single_scenario_without_steps.feature`
```
Feature: empty feature

  Scenario: without steps
```

## File: `internal/formatters/formatter-tests/features/empty_with_single_scenario_without_steps_and_description.feature`
```
Feature: empty feature
  describes
  an empty
  feature

  Scenario: without steps
```

## File: `internal/formatters/formatter-tests/features/rules_with_examples_with_backgrounds.feature`
```
Feature: rules with examples with backgrounds

  Rule: first rule

    Background: for first rule
      Given passing step
      And passing step

    Example: rule 1 example 1
      When passing step
      Then passing step

    Example: rule 1 example 2
      When passing step
      Then passing step


  Rule: second rule

    Background: for second rule
      Given passing step
      And passing step

    Example: rule 1 example 1
      When passing step
      Then passing step

    Example: rule 2 example 2
      When passing step
      Then passing step
```

## File: `internal/formatters/formatter-tests/features/scenario_outline.feature`
```
@outline @tag
Feature: outline

  @scenario
  Scenario Outline: outline
    Given passing step
    When passing step
    Then odd <odd> and even <even> number

    @tagged
    Examples: tagged
      | odd | even |
      | 1   | 2    |
      | 2   | 0    |
      | 3   | 11   |

    @tag2
    Examples:
      | odd | even |
      | 1   | 14   |
      | 3   | 9    |
```

## File: `internal/formatters/formatter-tests/features/scenario_with_attachment.feature`
```
Feature: feature with attachment
  describes
  an attachment
  feature

  Scenario: scenario with attachment
    Given a step with a single attachment call for multiple attachments
    And a step with multiple attachment calls
```

## File: `internal/formatters/formatter-tests/features/scenario_with_background.feature`
```
Feature: single scenario with background

  Background: named
    Given passing step
    And passing step

  Scenario: scenario
    When passing step
    Then passing step
```

## File: `internal/formatters/formatter-tests/features/scenario_without_steps_with_background.feature`
```
Feature: empty feature

  Background:
    Given passing step

  Scenario: without steps
```

## File: `internal/formatters/formatter-tests/features/single_scenario_with_passing_step.feature`
```
Feature: single passing scenario
  describes
  a single scenario
  feature

  Scenario: one step passing
    Given a passing step
```

## File: `internal/formatters/formatter-tests/features/some_scenarios_including_failing.feature`
```
Feature: some scenarios

  Scenario: failing
    Given passing step
    When failing step
    Then passing step

  Scenario: pending
    When pending step
    Then passing step

  Scenario: undefined
    When undefined
    Then passing step

  Scenario: ambiguous
    When ambiguous step
    Then passing step
```

## File: `internal/formatters/formatter-tests/features/stop_on_first_failure.feature`
```
Feature: Stop on first failure

  Scenario: First scenario - should run and fail
    Given a passing step
    When a failing step
    Then a passing step

  Scenario: Second scenario - should be skipped
    Given a passing step
    Then a passing step 
```

## File: `internal/formatters/formatter-tests/features/two_scenarios_with_background_fail.feature`
```
Feature: two scenarios with background fail

  Background:
    Given passing step
    And failing step

  Scenario: one
    When passing step
    Then passing step

  Scenario: two
    Then passing step
```

## File: `internal/formatters/formatter-tests/features/with_few_empty_scenarios.feature`
```
Feature: few empty scenarios

  Scenario: one

  Scenario Outline: two

    Examples: first group
      | one | two |
      | 1   | 2   |
      | 4   | 7   |

    Examples: second group
      | one | two |
      | 5   | 9   |

  Scenario: three
```

## File: `internal/formatters/formatter-tests/junit/empty`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="0" skipped="0" failures="0" errors="0" time="0"></testsuites>
```

## File: `internal/formatters/formatter-tests/junit/empty_with_description`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="0" skipped="0" failures="0" errors="0" time="0"></testsuites>
```

## File: `internal/formatters/formatter-tests/junit/empty_with_single_scenario_without_steps`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="1" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="empty feature" tests="1" skipped="0" failures="0" errors="0" time="0">
    <testcase name="without steps" status="" time="0"></testcase>
  </testsuite>
</testsuites>
```

## File: `internal/formatters/formatter-tests/junit/empty_with_single_scenario_without_steps_and_description`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="1" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="empty feature" tests="1" skipped="0" failures="0" errors="0" time="0">
    <testcase name="without steps" status="" time="0"></testcase>
  </testsuite>
</testsuites>
```

## File: `internal/formatters/formatter-tests/junit/scenario_outline`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="5" skipped="0" failures="3" errors="0" time="0">
  <testsuite name="outline" tests="5" skipped="0" failures="3" errors="0" time="0">
    <testcase name="outline #1" status="passed" time="0"></testcase>
    <testcase name="outline #2" status="failed" time="0">
      <failure message="Step odd 2 and even 0 number: 2 is not odd"></failure>
    </testcase>
    <testcase name="outline #3" status="failed" time="0">
      <failure message="Step odd 3 and even 11 number: 11 is not even"></failure>
    </testcase>
    <testcase name="outline #4" status="passed" time="0"></testcase>
    <testcase name="outline #5" status="failed" time="0">
      <failure message="Step odd 3 and even 9 number: 9 is not even"></failure>
    </testcase>
  </testsuite>
</testsuites>
```

## File: `internal/formatters/formatter-tests/junit/scenario_with_background`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="1" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="single scenario with background" tests="1" skipped="0" failures="0" errors="0" time="0">
    <testcase name="scenario" status="passed" time="0"></testcase>
  </testsuite>
</testsuites>
```

## File: `internal/formatters/formatter-tests/junit/scenario_without_steps_with_background`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="1" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="empty feature" tests="1" skipped="0" failures="0" errors="0" time="0">
    <testcase name="without steps" status="" time="0"></testcase>
  </testsuite>
</testsuites>
```

## File: `internal/formatters/formatter-tests/junit/single_scenario_with_passing_step`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="1" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="single passing scenario" tests="1" skipped="0" failures="0" errors="0" time="0">
    <testcase name="one step passing" status="passed" time="0"></testcase>
  </testsuite>
</testsuites>
```

## File: `internal/formatters/formatter-tests/junit/some_scenarios_including_failing`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="4" skipped="0" failures="1" errors="2" time="0">
  <testsuite name="some scenarios" tests="4" skipped="0" failures="1" errors="2" time="0">
    <testcase name="failing" status="failed" time="0">
      <failure message="Step failing step: step failed"></failure>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
    <testcase name="pending" status="pending" time="0">
      <error message="Step pending step: TODO: write pending definition" type="pending"></error>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
    <testcase name="undefined" status="undefined" time="0">
      <error message="Step undefined" type="undefined"></error>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
    <testcase name="ambiguous" status="ambiguous" time="0">
      <error message="Step ambiguous step" type="ambiguous"></error>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
  </testsuite>
</testsuites>
```

## File: `internal/formatters/formatter-tests/junit/stop_on_first_failure`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="2" skipped="0" failures="1" errors="0" time="0">
  <testsuite name="Stop on first failure" tests="2" skipped="0" failures="1" errors="0" time="0">
    <testcase name="First scenario - should run and fail" status="failed" time="0">
      <failure message="Step a failing step: step failed"></failure>
      <error message="Step a passing step" type="skipped"></error>
    </testcase>
    <testcase name="Second scenario - should be skipped" status="passed" time="0"></testcase>
  </testsuite>
</testsuites>
```

## File: `internal/formatters/formatter-tests/junit/two_scenarios_with_background_fail`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="2" skipped="0" failures="2" errors="0" time="0">
  <testsuite name="two scenarios with background fail" tests="2" skipped="0" failures="2" errors="0" time="0">
    <testcase name="one" status="failed" time="0">
      <failure message="Step failing step: step failed"></failure>
      <error message="Step passing step" type="skipped"></error>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
    <testcase name="two" status="failed" time="0">
      <failure message="Step failing step: step failed"></failure>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
  </testsuite>
</testsuites>
```

## File: `internal/formatters/formatter-tests/junit/with_few_empty_scenarios`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit" tests="5" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="few empty scenarios" tests="5" skipped="0" failures="0" errors="0" time="0">
    <testcase name="one" status="" time="0"></testcase>
    <testcase name="two #1" status="" time="0"></testcase>
    <testcase name="two #2" status="" time="0"></testcase>
    <testcase name="two #3" status="" time="0"></testcase>
    <testcase name="three" status="" time="0"></testcase>
  </testsuite>
</testsuites>
```

## File: `internal/formatters/formatter-tests/junit,pretty/empty`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="0" skipped="0" failures="0" errors="0" time="0"></testsuites>
No scenarios
No steps
0s
```

## File: `internal/formatters/formatter-tests/junit,pretty/empty_with_description`
```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="0" skipped="0" failures="0" errors="0" time="0"></testsuites>
No scenarios
No steps
0s
```

## File: `internal/formatters/formatter-tests/junit,pretty/empty_with_single_scenario_without_steps`
```
<bold-white>Feature:</bold-white> empty feature

  <bold-white>Scenario:</bold-white> without steps <bold-black># formatter-tests/features/empty_with_single_scenario_without_steps.feature:3</bold-black>
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="1" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="empty feature" tests="1" skipped="0" failures="0" errors="0" time="0">
    <testcase name="without steps" status="" time="0"></testcase>
  </testsuite>
</testsuites>
1 scenarios (<yellow>1 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/junit,pretty/empty_with_single_scenario_without_steps_and_description`
```
<bold-white>Feature:</bold-white> empty feature
  describes
  an empty
  feature

  <bold-white>Scenario:</bold-white> without steps <bold-black># formatter-tests/features/empty_with_single_scenario_without_steps_and_description.feature:6</bold-black>
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="1" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="empty feature" tests="1" skipped="0" failures="0" errors="0" time="0">
    <testcase name="without steps" status="" time="0"></testcase>
  </testsuite>
</testsuites>
1 scenarios (<yellow>1 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/junit,pretty/scenario_outline`
```
<bold-white>Feature:</bold-white> outline

  <bold-white>Scenario Outline:</bold-white> outline               <bold-black># formatter-tests/features/scenario_outline.feature:5</bold-black>
    <cyan>Given</cyan> <cyan>passing step</cyan>                    <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <cyan>When</cyan> <cyan>passing step</cyan>                     <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <cyan>Then</cyan> <cyan>odd </cyan><bold-cyan><odd></bold-cyan><cyan> and even </cyan><bold-cyan><even></bold-cyan><cyan> number</cyan> <bold-black># fmt_output_test.go:103 -> github.com/cucumber/godog/internal/formatters_test.oddEvenStepDef</bold-black>

    <bold-white>Examples:</bold-white> tagged
      | <cyan>odd</cyan> | <cyan>even</cyan> |
      | <green>1</green>   | <green>2</green>    |
      | <red>2</red>   | <red>0</red>    |
        <bold-red>2 is not odd</bold-red>
      | <red>3</red>   | <red>11</red>   |
        <bold-red>11 is not even</bold-red>

    <bold-white>Examples:</bold-white>
      | <cyan>odd</cyan> | <cyan>even</cyan> |
      | <green>1</green>   | <green>14</green>   |
      | <red>3</red>   | <red>9</red>    |
        <bold-red>9 is not even</bold-red>
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="5" skipped="0" failures="3" errors="0" time="0">
  <testsuite name="outline" tests="5" skipped="0" failures="3" errors="0" time="0">
    <testcase name="outline #1" status="passed" time="0"></testcase>
    <testcase name="outline #2" status="failed" time="0">
      <failure message="Step odd 2 and even 0 number: 2 is not odd"></failure>
    </testcase>
    <testcase name="outline #3" status="failed" time="0">
      <failure message="Step odd 3 and even 11 number: 11 is not even"></failure>
    </testcase>
    <testcase name="outline #4" status="passed" time="0"></testcase>
    <testcase name="outline #5" status="failed" time="0">
      <failure message="Step odd 3 and even 9 number: 9 is not even"></failure>
    </testcase>
  </testsuite>
</testsuites>
--- <red>Failed steps:</red>

  <red>Scenario Outline: outline</red> <bold-black># formatter-tests/features/scenario_outline.feature:5</bold-black>
    <red>Then odd 2 and even 0 number</red> <bold-black># formatter-tests/features/scenario_outline.feature:8</bold-black>
      <red>Error: </red><bold-red>2 is not odd</bold-red>

  <red>Scenario Outline: outline</red> <bold-black># formatter-tests/features/scenario_outline.feature:5</bold-black>
    <red>Then odd 3 and even 11 number</red> <bold-black># formatter-tests/features/scenario_outline.feature:8</bold-black>
      <red>Error: </red><bold-red>11 is not even</bold-red>

  <red>Scenario Outline: outline</red> <bold-black># formatter-tests/features/scenario_outline.feature:5</bold-black>
    <red>Then odd 3 and even 9 number</red> <bold-black># formatter-tests/features/scenario_outline.feature:8</bold-black>
      <red>Error: </red><bold-red>9 is not even</bold-red>


5 scenarios (<green>2 passed</green>, <red>3 failed</red>)
15 steps (<green>12 passed</green>, <red>3 failed</red>)
0s
```

## File: `internal/formatters/formatter-tests/junit,pretty/scenario_with_background`
```
<bold-white>Feature:</bold-white> single scenario with background

  <bold-white>Background:</bold-white> named
    <green>Given</green> <green>passing step</green> <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>And</green> <green>passing step</green>   <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> scenario   <bold-black># formatter-tests/features/scenario_with_background.feature:7</bold-black>
    <green>When</green> <green>passing step</green>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>Then</green> <green>passing step</green>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="1" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="single scenario with background" tests="1" skipped="0" failures="0" errors="0" time="0">
    <testcase name="scenario" status="passed" time="0"></testcase>
  </testsuite>
</testsuites>
1 scenarios (<green>1 passed</green>)
4 steps (<green>4 passed</green>)
0s
```

## File: `internal/formatters/formatter-tests/junit,pretty/scenario_without_steps_with_background`
```
<bold-white>Feature:</bold-white> empty feature

  <bold-white>Background:</bold-white>
    <cyan>Given</cyan> <cyan>passing step</cyan>

  <bold-white>Scenario:</bold-white> without steps <bold-black># formatter-tests/features/scenario_without_steps_with_background.feature:6</bold-black>
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="1" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="empty feature" tests="1" skipped="0" failures="0" errors="0" time="0">
    <testcase name="without steps" status="" time="0"></testcase>
  </testsuite>
</testsuites>
1 scenarios (<yellow>1 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/junit,pretty/single_scenario_with_passing_step`
```
<bold-white>Feature:</bold-white> single passing scenario
  describes
  a single scenario
  feature

  <bold-white>Scenario:</bold-white> one step passing <bold-black># formatter-tests/features/single_scenario_with_passing_step.feature:6</bold-black>
    <green>Given</green> <green>a passing step</green>     <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="1" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="single passing scenario" tests="1" skipped="0" failures="0" errors="0" time="0">
    <testcase name="one step passing" status="passed" time="0"></testcase>
  </testsuite>
</testsuites>
1 scenarios (<green>1 passed</green>)
1 steps (<green>1 passed</green>)
0s
```

## File: `internal/formatters/formatter-tests/junit,pretty/some_scenarios_including_failing`
```
<bold-white>Feature:</bold-white> some scenarios

  <bold-white>Scenario:</bold-white> failing    <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:3</bold-black>
    <green>Given</green> <green>passing step</green> <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <red>When</red> <red>failing step</red>  <bold-black># fmt_output_test.go:117 -> github.com/cucumber/godog/internal/formatters_test.failingStepDef</bold-black>
    <bold-red>step failed</bold-red>
    <cyan>Then</cyan> <cyan>passing step</cyan>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> pending   <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:8</bold-black>
    <yellow>When</yellow> <yellow>pending step</yellow> <bold-black># fmt_output_test.go:115 -> github.com/cucumber/godog/internal/formatters_test.pendingStepDef</bold-black>
      <yellow>TODO: write pending definition</yellow>
    <cyan>Then</cyan> <cyan>passing step</cyan> <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> undefined <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:12</bold-black>
    <yellow>When</yellow> <yellow>undefined</yellow>
    <cyan>Then</cyan> <cyan>passing step</cyan> <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> ambiguous   <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:16</bold-black>
    <yellow>When</yellow> <yellow>ambiguous step</yellow>
    <bold-red>ambiguous step definition, step text: ambiguous step
    matches:
        ^ambiguous step.*$
        ^ambiguous step$</bold-red>
    <cyan>Then</cyan> <cyan>passing step</cyan>   <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="4" skipped="0" failures="1" errors="2" time="0">
  <testsuite name="some scenarios" tests="4" skipped="0" failures="1" errors="2" time="0">
    <testcase name="failing" status="failed" time="0">
      <failure message="Step failing step: step failed"></failure>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
    <testcase name="pending" status="pending" time="0">
      <error message="Step pending step: TODO: write pending definition" type="pending"></error>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
    <testcase name="undefined" status="undefined" time="0">
      <error message="Step undefined" type="undefined"></error>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
    <testcase name="ambiguous" status="ambiguous" time="0">
      <error message="Step ambiguous step" type="ambiguous"></error>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
  </testsuite>
</testsuites>
--- <red>Failed steps:</red>

  <red>Scenario: failing</red> <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:3</bold-black>
    <red>When failing step</red> <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>


4 scenarios (<red>1 failed</red>, <yellow>1 pending</yellow>, <yellow>1 ambiguous</yellow>, <yellow>1 undefined</yellow>)
9 steps (<green>1 passed</green>, <red>1 failed</red>, <yellow>1 pending</yellow>, <yellow>1 ambiguous</yellow>, <yellow>1 undefined</yellow>, <cyan>4 skipped</cyan>)
0s

<yellow>You can implement step definitions for undefined steps with these snippets:</yellow>
<yellow>
func undefined() error {
	return godog.ErrPending
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Step(`^undefined$`, undefined)
}
</yellow>
```

## File: `internal/formatters/formatter-tests/junit,pretty/stop_on_first_failure`
```
<bold-white>Feature:</bold-white> Stop on first failure

  <bold-white>Scenario:</bold-white> First scenario - should run and fail <bold-black># formatter-tests/features/stop_on_first_failure.feature:3</bold-black>
    <green>Given</green> <green>a passing step</green>                         <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <red>When</red> <red>a failing step</red>                          <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.failingStepDef</bold-black>
    <bold-red>step failed</bold-red>
    <cyan>Then</cyan> <cyan>a passing step</cyan>                          <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> Second scenario - should be skipped <bold-black># formatter-tests/features/stop_on_first_failure.feature:8</bold-black>
    <green>Given</green> <green>a passing step</green>                        <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>Then</green> <green>a passing step</green>                         <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="2" skipped="0" failures="1" errors="0" time="0">
  <testsuite name="Stop on first failure" tests="2" skipped="0" failures="1" errors="0" time="0">
    <testcase name="First scenario - should run and fail" status="failed" time="0">
      <failure message="Step a failing step: step failed"></failure>
      <error message="Step a passing step" type="skipped"></error>
    </testcase>
    <testcase name="Second scenario - should be skipped" status="passed" time="0"></testcase>
  </testsuite>
</testsuites>
--- <red>Failed steps:</red>

  <red>Scenario: First scenario - should run and fail</red> <bold-black># formatter-tests/features/stop_on_first_failure.feature:3</bold-black>
    <red>When a failing step</red> <bold-black># formatter-tests/features/stop_on_first_failure.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>


2 scenarios (<green>1 passed</green>, <red>1 failed</red>)
5 steps (<green>3 passed</green>, <red>1 failed</red>, <cyan>1 skipped</cyan>)
0s
```

## File: `internal/formatters/formatter-tests/junit,pretty/two_scenarios_with_background_fail`
```
<bold-white>Feature:</bold-white> two scenarios with background fail

  <bold-white>Background:</bold-white>
    <green>Given</green> <green>passing step</green> <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <red>And</red> <red>failing step</red>   <bold-black># fmt_output_test.go:117 -> github.com/cucumber/godog/internal/formatters_test.failingStepDef</bold-black>
    <bold-red>step failed</bold-red>

  <bold-white>Scenario:</bold-white> one        <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:7</bold-black>
    <cyan>When</cyan> <cyan>passing step</cyan>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <cyan>Then</cyan> <cyan>passing step</cyan>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> two        <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:11</bold-black>
    <cyan>Then</cyan> <cyan>passing step</cyan>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="2" skipped="0" failures="2" errors="0" time="0">
  <testsuite name="two scenarios with background fail" tests="2" skipped="0" failures="2" errors="0" time="0">
    <testcase name="one" status="failed" time="0">
      <failure message="Step failing step: step failed"></failure>
      <error message="Step passing step" type="skipped"></error>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
    <testcase name="two" status="failed" time="0">
      <failure message="Step failing step: step failed"></failure>
      <error message="Step passing step" type="skipped"></error>
    </testcase>
  </testsuite>
</testsuites>
--- <red>Failed steps:</red>

  <red>Scenario: one</red> <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:7</bold-black>
    <red>And failing step</red> <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>

  <red>Scenario: two</red> <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:11</bold-black>
    <red>And failing step</red> <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>


2 scenarios (<red>2 failed</red>)
7 steps (<green>2 passed</green>, <red>2 failed</red>, <cyan>3 skipped</cyan>)
0s
```

## File: `internal/formatters/formatter-tests/junit,pretty/with_few_empty_scenarios`
```
<bold-white>Feature:</bold-white> few empty scenarios

  <bold-white>Scenario:</bold-white> one <bold-black># formatter-tests/features/with_few_empty_scenarios.feature:3</bold-black>

  <bold-white>Scenario Outline:</bold-white> two <bold-black># formatter-tests/features/with_few_empty_scenarios.feature:5</bold-black>

    <bold-white>Examples:</bold-white> first group
      | <cyan>one</cyan> | <cyan>two</cyan> |
      | <cyan>1</cyan>   | <cyan>2</cyan>   |
      | <cyan>4</cyan>   | <cyan>7</cyan>   |

    <bold-white>Examples:</bold-white> second group
      | <cyan>one</cyan> | <cyan>two</cyan> |
      | <cyan>5</cyan>   | <cyan>9</cyan>   |

  <bold-white>Scenario:</bold-white> three <bold-black># formatter-tests/features/with_few_empty_scenarios.feature:16</bold-black>
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="junit,pretty" tests="5" skipped="0" failures="0" errors="0" time="0">
  <testsuite name="few empty scenarios" tests="5" skipped="0" failures="0" errors="0" time="0">
    <testcase name="one" status="" time="0"></testcase>
    <testcase name="two #1" status="" time="0"></testcase>
    <testcase name="two #2" status="" time="0"></testcase>
    <testcase name="two #3" status="" time="0"></testcase>
    <testcase name="three" status="" time="0"></testcase>
  </testsuite>
</testsuites>
5 scenarios (<yellow>5 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/pretty/empty`
```

No scenarios
No steps
0s
```

## File: `internal/formatters/formatter-tests/pretty/empty_with_description`
```

No scenarios
No steps
0s
```

## File: `internal/formatters/formatter-tests/pretty/empty_with_single_scenario_without_steps`
```
<bold-white>Feature:</bold-white> empty feature

  <bold-white>Scenario:</bold-white> without steps <bold-black># formatter-tests/features/empty_with_single_scenario_without_steps.feature:3</bold-black>

1 scenarios (<yellow>1 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/pretty/empty_with_single_scenario_without_steps_and_description`
```
<bold-white>Feature:</bold-white> empty feature
  describes
  an empty
  feature

  <bold-white>Scenario:</bold-white> without steps <bold-black># formatter-tests/features/empty_with_single_scenario_without_steps_and_description.feature:6</bold-black>

1 scenarios (<yellow>1 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/pretty/rules_with_examples_with_backgrounds`
```
<bold-white>Feature:</bold-white> rules with examples with backgrounds

  <bold-white>Background:</bold-white> for first rule
    <green>Given</green> <green>passing step</green>      <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>And</green> <green>passing step</green>        <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Example:</bold-white> rule 1 example 1 <bold-black># formatter-tests/features/rules_with_examples_with_backgrounds.feature:9</bold-black>
    <green>When</green> <green>passing step</green>       <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>Then</green> <green>passing step</green>       <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Example:</bold-white> rule 1 example 2 <bold-black># formatter-tests/features/rules_with_examples_with_backgrounds.feature:13</bold-black>
    <green>When</green> <green>passing step</green>       <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>Then</green> <green>passing step</green>       <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Background:</bold-white> for second rule
    <green>Given</green> <green>passing step</green>      <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>And</green> <green>passing step</green>        <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Example:</bold-white> rule 1 example 1 <bold-black># formatter-tests/features/rules_with_examples_with_backgrounds.feature:24</bold-black>
    <green>When</green> <green>passing step</green>       <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>Then</green> <green>passing step</green>       <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Example:</bold-white> rule 2 example 2 <bold-black># formatter-tests/features/rules_with_examples_with_backgrounds.feature:28</bold-black>
    <green>When</green> <green>passing step</green>       <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>Then</green> <green>passing step</green>       <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

4 scenarios (<green>4 passed</green>)
16 steps (<green>16 passed</green>)
0s
```

## File: `internal/formatters/formatter-tests/pretty/scenario_outline`
```
<bold-white>Feature:</bold-white> outline

  <bold-white>Scenario Outline:</bold-white> outline               <bold-black># formatter-tests/features/scenario_outline.feature:5</bold-black>
    <cyan>Given</cyan> <cyan>passing step</cyan>                    <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <cyan>When</cyan> <cyan>passing step</cyan>                     <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <cyan>Then</cyan> <cyan>odd </cyan><bold-cyan><odd></bold-cyan><cyan> and even </cyan><bold-cyan><even></bold-cyan><cyan> number</cyan> <bold-black># fmt_output_test.go:103 -> github.com/cucumber/godog/internal/formatters_test.oddEvenStepDef</bold-black>

    <bold-white>Examples:</bold-white> tagged
      | <cyan>odd</cyan> | <cyan>even</cyan> |
      | <green>1</green>   | <green>2</green>    |
      | <red>2</red>   | <red>0</red>    |
        <bold-red>2 is not odd</bold-red>
      | <red>3</red>   | <red>11</red>   |
        <bold-red>11 is not even</bold-red>

    <bold-white>Examples:</bold-white>
      | <cyan>odd</cyan> | <cyan>even</cyan> |
      | <green>1</green>   | <green>14</green>   |
      | <red>3</red>   | <red>9</red>    |
        <bold-red>9 is not even</bold-red>

--- <red>Failed steps:</red>

  <red>Scenario Outline: outline</red> <bold-black># formatter-tests/features/scenario_outline.feature:5</bold-black>
    <red>Then odd 2 and even 0 number</red> <bold-black># formatter-tests/features/scenario_outline.feature:8</bold-black>
      <red>Error: </red><bold-red>2 is not odd</bold-red>

  <red>Scenario Outline: outline</red> <bold-black># formatter-tests/features/scenario_outline.feature:5</bold-black>
    <red>Then odd 3 and even 11 number</red> <bold-black># formatter-tests/features/scenario_outline.feature:8</bold-black>
      <red>Error: </red><bold-red>11 is not even</bold-red>

  <red>Scenario Outline: outline</red> <bold-black># formatter-tests/features/scenario_outline.feature:5</bold-black>
    <red>Then odd 3 and even 9 number</red> <bold-black># formatter-tests/features/scenario_outline.feature:8</bold-black>
      <red>Error: </red><bold-red>9 is not even</bold-red>


5 scenarios (<green>2 passed</green>, <red>3 failed</red>)
15 steps (<green>12 passed</green>, <red>3 failed</red>)
0s
```

## File: `internal/formatters/formatter-tests/pretty/scenario_with_background`
```
<bold-white>Feature:</bold-white> single scenario with background

  <bold-white>Background:</bold-white> named
    <green>Given</green> <green>passing step</green> <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>And</green> <green>passing step</green>   <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> scenario   <bold-black># formatter-tests/features/scenario_with_background.feature:7</bold-black>
    <green>When</green> <green>passing step</green>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>Then</green> <green>passing step</green>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

1 scenarios (<green>1 passed</green>)
4 steps (<green>4 passed</green>)
0s
```

## File: `internal/formatters/formatter-tests/pretty/scenario_without_steps_with_background`
```
<bold-white>Feature:</bold-white> empty feature

  <bold-white>Background:</bold-white>
    <cyan>Given</cyan> <cyan>passing step</cyan>

  <bold-white>Scenario:</bold-white> without steps <bold-black># formatter-tests/features/scenario_without_steps_with_background.feature:6</bold-black>

1 scenarios (<yellow>1 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/pretty/single_scenario_with_passing_step`
```
<bold-white>Feature:</bold-white> single passing scenario
  describes
  a single scenario
  feature

  <bold-white>Scenario:</bold-white> one step passing <bold-black># formatter-tests/features/single_scenario_with_passing_step.feature:6</bold-black>
    <green>Given</green> <green>a passing step</green>     <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

1 scenarios (<green>1 passed</green>)
1 steps (<green>1 passed</green>)
0s
```

## File: `internal/formatters/formatter-tests/pretty/some_scenarios_including_failing`
```
<bold-white>Feature:</bold-white> some scenarios

  <bold-white>Scenario:</bold-white> failing    <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:3</bold-black>
    <green>Given</green> <green>passing step</green> <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <red>When</red> <red>failing step</red>  <bold-black># fmt_output_test.go:117 -> github.com/cucumber/godog/internal/formatters_test.failingStepDef</bold-black>
    <bold-red>step failed</bold-red>
    <cyan>Then</cyan> <cyan>passing step</cyan>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> pending   <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:8</bold-black>
    <yellow>When</yellow> <yellow>pending step</yellow> <bold-black># fmt_output_test.go:115 -> github.com/cucumber/godog/internal/formatters_test.pendingStepDef</bold-black>
      <yellow>TODO: write pending definition</yellow>
    <cyan>Then</cyan> <cyan>passing step</cyan> <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> undefined <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:12</bold-black>
    <yellow>When</yellow> <yellow>undefined</yellow>
    <cyan>Then</cyan> <cyan>passing step</cyan> <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> ambiguous   <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:16</bold-black>
    <yellow>When</yellow> <yellow>ambiguous step</yellow>
    <bold-red>ambiguous step definition, step text: ambiguous step
    matches:
        ^ambiguous step.*$
        ^ambiguous step$</bold-red>
    <cyan>Then</cyan> <cyan>passing step</cyan>   <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

--- <red>Failed steps:</red>

  <red>Scenario: failing</red> <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:3</bold-black>
    <red>When failing step</red> <bold-black># formatter-tests/features/some_scenarios_including_failing.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>


4 scenarios (<red>1 failed</red>, <yellow>1 pending</yellow>, <yellow>1 ambiguous</yellow>, <yellow>1 undefined</yellow>)
9 steps (<green>1 passed</green>, <red>1 failed</red>, <yellow>1 pending</yellow>, <yellow>1 ambiguous</yellow>, <yellow>1 undefined</yellow>, <cyan>4 skipped</cyan>)
0s

<yellow>You can implement step definitions for undefined steps with these snippets:</yellow>
<yellow>
func undefined() error {
	return godog.ErrPending
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Step(`^undefined$`, undefined)
}
</yellow>
```

## File: `internal/formatters/formatter-tests/pretty/stop_on_first_failure`
```
<bold-white>Feature:</bold-white> Stop on first failure

  <bold-white>Scenario:</bold-white> First scenario - should run and fail <bold-black># formatter-tests/features/stop_on_first_failure.feature:3</bold-black>
    <green>Given</green> <green>a passing step</green>                         <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <red>When</red> <red>a failing step</red>                          <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.failingStepDef</bold-black>
    <bold-red>step failed</bold-red>
    <cyan>Then</cyan> <cyan>a passing step</cyan>                          <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> Second scenario - should be skipped <bold-black># formatter-tests/features/stop_on_first_failure.feature:8</bold-black>
    <green>Given</green> <green>a passing step</green>                        <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <green>Then</green> <green>a passing step</green>                         <bold-black># fmt_output_test.go:XXX -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

--- <red>Failed steps:</red>

  <red>Scenario: First scenario - should run and fail</red> <bold-black># formatter-tests/features/stop_on_first_failure.feature:3</bold-black>
    <red>When a failing step</red> <bold-black># formatter-tests/features/stop_on_first_failure.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>


2 scenarios (<green>1 passed</green>, <red>1 failed</red>)
5 steps (<green>3 passed</green>, <red>1 failed</red>, <cyan>1 skipped</cyan>)
0s
```

## File: `internal/formatters/formatter-tests/pretty/two_scenarios_with_background_fail`
```
<bold-white>Feature:</bold-white> two scenarios with background fail

  <bold-white>Background:</bold-white>
    <green>Given</green> <green>passing step</green> <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <red>And</red> <red>failing step</red>   <bold-black># fmt_output_test.go:117 -> github.com/cucumber/godog/internal/formatters_test.failingStepDef</bold-black>
    <bold-red>step failed</bold-red>

  <bold-white>Scenario:</bold-white> one        <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:7</bold-black>
    <cyan>When</cyan> <cyan>passing step</cyan>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>
    <cyan>Then</cyan> <cyan>passing step</cyan>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

  <bold-white>Scenario:</bold-white> two        <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:11</bold-black>
    <cyan>Then</cyan> <cyan>passing step</cyan>  <bold-black># fmt_output_test.go:101 -> github.com/cucumber/godog/internal/formatters_test.passingStepDef</bold-black>

--- <red>Failed steps:</red>

  <red>Scenario: one</red> <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:7</bold-black>
    <red>And failing step</red> <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>

  <red>Scenario: two</red> <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:11</bold-black>
    <red>And failing step</red> <bold-black># formatter-tests/features/two_scenarios_with_background_fail.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>


2 scenarios (<red>2 failed</red>)
7 steps (<green>2 passed</green>, <red>2 failed</red>, <cyan>3 skipped</cyan>)
0s
```

## File: `internal/formatters/formatter-tests/pretty/with_few_empty_scenarios`
```
<bold-white>Feature:</bold-white> few empty scenarios

  <bold-white>Scenario:</bold-white> one <bold-black># formatter-tests/features/with_few_empty_scenarios.feature:3</bold-black>

  <bold-white>Scenario Outline:</bold-white> two <bold-black># formatter-tests/features/with_few_empty_scenarios.feature:5</bold-black>

    <bold-white>Examples:</bold-white> first group
      | <cyan>one</cyan> | <cyan>two</cyan> |
      | <cyan>1</cyan>   | <cyan>2</cyan>   |
      | <cyan>4</cyan>   | <cyan>7</cyan>   |

    <bold-white>Examples:</bold-white> second group
      | <cyan>one</cyan> | <cyan>two</cyan> |
      | <cyan>5</cyan>   | <cyan>9</cyan>   |

  <bold-white>Scenario:</bold-white> three <bold-black># formatter-tests/features/with_few_empty_scenarios.feature:16</bold-black>

5 scenarios (<yellow>5 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/progress/empty`
```


No scenarios
No steps
0s
```

## File: `internal/formatters/formatter-tests/progress/empty_with_description`
```


No scenarios
No steps
0s
```

## File: `internal/formatters/formatter-tests/progress/empty_with_single_scenario_without_steps`
```


1 scenarios (<yellow>1 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/progress/empty_with_single_scenario_without_steps_and_description`
```


1 scenarios (<yellow>1 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/progress/scenario_outline`
```
<green>.</green><green>.</green><green>.</green><green>.</green><green>.</green><red>F</red><green>.</green><green>.</green><red>F</red><green>.</green><green>.</green><green>.</green><green>.</green><green>.</green><red>F</red> 15


--- <red>Failed steps:</red>

  <red>Scenario Outline: outline</red><bold-black> # formatter-tests/features/scenario_outline.feature:5</bold-black>
    <red>Then odd 2 and even 0 number</red><bold-black> # formatter-tests/features/scenario_outline.feature:8</bold-black>
      <red>Error: </red><bold-red>2 is not odd</bold-red>

  <red>Scenario Outline: outline</red><bold-black> # formatter-tests/features/scenario_outline.feature:5</bold-black>
    <red>Then odd 3 and even 11 number</red><bold-black> # formatter-tests/features/scenario_outline.feature:8</bold-black>
      <red>Error: </red><bold-red>11 is not even</bold-red>

  <red>Scenario Outline: outline</red><bold-black> # formatter-tests/features/scenario_outline.feature:5</bold-black>
    <red>Then odd 3 and even 9 number</red><bold-black> # formatter-tests/features/scenario_outline.feature:8</bold-black>
      <red>Error: </red><bold-red>9 is not even</bold-red>


5 scenarios (<green>2 passed</green>, <red>3 failed</red>)
15 steps (<green>12 passed</green>, <red>3 failed</red>)
0s
```

## File: `internal/formatters/formatter-tests/progress/scenario_with_background`
```
<green>.</green><green>.</green><green>.</green><green>.</green> 4


1 scenarios (<green>1 passed</green>)
4 steps (<green>4 passed</green>)
0s
```

## File: `internal/formatters/formatter-tests/progress/scenario_without_steps_with_background`
```


1 scenarios (<yellow>1 undefined</yellow>)
No steps
0s
```

## File: `internal/formatters/formatter-tests/progress/single_scenario_with_passing_step`
```
<green>.</green> 1


1 scenarios (<green>1 passed</green>)
1 steps (<green>1 passed</green>)
0s
```

## File: `internal/formatters/formatter-tests/progress/some_scenarions_including_failing`
```
<green>.</green><red>F</red><cyan>-</cyan><yellow>P</yellow><cyan>-</cyan><yellow>U</yellow><cyan>-</cyan><yellow>A</yellow><cyan>-</cyan> 9


--- <red>Failed steps:</red>

  <red>Scenario: failing</red><bold-black> # formatter-tests/features/some_scenarios_including_failing.feature:3</bold-black>
    <red>When failing step</red><bold-black> # formatter-tests/features/some_scenarios_including_failing.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>


4 scenarios (<red>1 failed</red>, <yellow>1 pending</yellow>, <yellow>1 ambiguous</yellow>, <yellow>1 undefined</yellow>)
9 steps (<green>1 passed</green>, <red>1 failed</red>, <yellow>1 pending</yellow>, <yellow>1 ambiguous</yellow>, <yellow>1 undefined</yellow>, <cyan>4 skipped</cyan>)
0s

<yellow>You can implement step definitions for undefined steps with these snippets:</yellow>
<yellow>
func undefined() error {
	return godog.ErrPending
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Step(`^undefined$`, undefined)
}
</yellow>
```

## File: `internal/formatters/formatter-tests/progress/two_scenarios_with_background_fail`
```
<green>.</green><red>F</red><cyan>-</cyan><cyan>-</cyan><green>.</green><red>F</red><cyan>-</cyan> 7


--- <red>Failed steps:</red>

  <red>Scenario: one</red><bold-black> # formatter-tests/features/two_scenarios_with_background_fail.feature:7</bold-black>
    <red>And failing step</red><bold-black> # formatter-tests/features/two_scenarios_with_background_fail.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>

  <red>Scenario: two</red><bold-black> # formatter-tests/features/two_scenarios_with_background_fail.feature:11</bold-black>
    <red>And failing step</red><bold-black> # formatter-tests/features/two_scenarios_with_background_fail.feature:5</bold-black>
      <red>Error: </red><bold-red>step failed</bold-red>


2 scenarios (<red>2 failed</red>)
7 steps (<green>2 passed</green>, <red>2 failed</red>, <cyan>3 skipped</cyan>)
0s
```

## File: `internal/formatters/formatter-tests/progress/with_few_empty_scenarios`
```


5 scenarios (<yellow>5 undefined</yellow>)
No steps
0s
```

## File: `internal/models/feature.go`
```go
package models

import (
	messages "github.com/cucumber/messages/go/v21"
)

// Feature is an internal object to group together
// the parsed gherkin document, the pickles and the
// raw content.
type Feature struct {
	*messages.GherkinDocument
	Pickles []*messages.Pickle
	Content []byte
}

// FindRule returns the rule to which the given scenario belongs
func (f Feature) FindRule(astScenarioID string) *messages.Rule {
	for _, child := range f.GherkinDocument.Feature.Children {
		if ru := child.Rule; ru != nil {
			if rc := child.Rule; rc != nil {
				for _, rcc := range rc.Children {
					if sc := rcc.Scenario; sc != nil && sc.Id == astScenarioID {
						return ru
					}
				}
			}
		}
	}
	return nil
}

// FindScenario returns the scenario in the feature or in a rule in the feature
func (f Feature) FindScenario(astScenarioID string) *messages.Scenario {
	for _, child := range f.GherkinDocument.Feature.Children {
		if sc := child.Scenario; sc != nil && sc.Id == astScenarioID {
			return sc
		}
		if rc := child.Rule; rc != nil {
			for _, rcc := range rc.Children {
				if sc := rcc.Scenario; sc != nil && sc.Id == astScenarioID {
					return sc
				}
			}
		}
	}

	return nil
}

// FindBackground ...
func (f Feature) FindBackground(astScenarioID string) *messages.Background {
	var bg *messages.Background

	for _, child := range f.GherkinDocument.Feature.Children {
		if tmp := child.Background; tmp != nil {
			bg = tmp
		}

		if sc := child.Scenario; sc != nil && sc.Id == astScenarioID {
			return bg
		}

		if ru := child.Rule; ru != nil {
			for _, rc := range ru.Children {
				if tmp := rc.Background; tmp != nil {
					bg = tmp
				}

				if sc := rc.Scenario; sc != nil && sc.Id == astScenarioID {
					return bg
				}
			}
		}
	}

	return nil
}

// FindExample ...
func (f Feature) FindExample(exampleAstID string) (*messages.Examples, *messages.TableRow) {
	for _, child := range f.GherkinDocument.Feature.Children {
		if sc := child.Scenario; sc != nil {
			for _, example := range sc.Examples {
				for _, row := range example.TableBody {
					if row.Id == exampleAstID {
						return example, row
					}
				}
			}
		}
		if ru := child.Rule; ru != nil {
			for _, rc := range ru.Children {
				if sc := rc.Scenario; sc != nil {
					for _, example := range sc.Examples {
						for _, row := range example.TableBody {
							if row.Id == exampleAstID {
								return example, row
							}
						}
					}
				}
			}
		}
	}

	return nil, nil
}

// FindStep ...
func (f Feature) FindStep(astStepID string) *messages.Step {
	for _, child := range f.GherkinDocument.Feature.Children {

		if ru := child.Rule; ru != nil {
			for _, ch := range ru.Children {
				if sc := ch.Scenario; sc != nil {
					for _, step := range sc.Steps {
						if step.Id == astStepID {
							return step
						}
					}
				}

				if bg := ch.Background; bg != nil {
					for _, step := range bg.Steps {
						if step.Id == astStepID {
							return step
						}
					}
				}
			}
		}

		if sc := child.Scenario; sc != nil {
			for _, step := range sc.Steps {
				if step.Id == astStepID {
					return step
				}
			}
		}

		if bg := child.Background; bg != nil {
			for _, step := range bg.Steps {
				if step.Id == astStepID {
					return step
				}
			}
		}
	}

	return nil
}
```

## File: `internal/models/feature_test.go`
```go
package models_test

import (
	"testing"

	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/testutils"
	"github.com/stretchr/testify/assert"
)

func Test_Find(t *testing.T) {
	ft := testutils.BuildTestFeature(t)

	t.Run("scenario", func(t *testing.T) {
		sc := ft.FindScenario(ft.Pickles[0].AstNodeIds[0])
		assert.NotNilf(t, sc, "expected scenario to not be nil")
	})

	t.Run("background", func(t *testing.T) {
		bg := ft.FindBackground(ft.Pickles[0].AstNodeIds[0])
		assert.NotNilf(t, bg, "expected background to not be nil")
	})

	t.Run("example", func(t *testing.T) {
		example, row := ft.FindExample(ft.Pickles[1].AstNodeIds[1])
		assert.NotNilf(t, example, "expected example to not be nil")
		assert.NotNilf(t, row, "expected table row to not be nil")
	})

	t.Run("step", func(t *testing.T) {
		for _, ps := range ft.Pickles[0].Steps {
			step := ft.FindStep(ps.AstNodeIds[0])
			assert.NotNilf(t, step, "expected step to not be nil")
		}
	})

	t.Run("rule", func(t *testing.T) {
		sc := ft.FindRule(ft.Pickles[0].AstNodeIds[0])
		assert.Nilf(t, sc, "expected rule to be nil")
	})
}

func Test_FindInRule(t *testing.T) {

	ft := testutils.BuildTestFeatureWithRules(t)

	t.Run("rule", func(t *testing.T) {
		sc := ft.FindRule(ft.Pickles[0].AstNodeIds[0])
		assert.NotNilf(t, sc, "expected rule to not be nil")
	})

	t.Run("scenario", func(t *testing.T) {
		sc := ft.FindScenario(ft.Pickles[0].AstNodeIds[0])
		assert.NotNilf(t, sc, "expected scenario to not be nil")
	})

	t.Run("background", func(t *testing.T) {
		bg := ft.FindBackground(ft.Pickles[0].AstNodeIds[0])
		assert.NotNilf(t, bg, "expected background to not be nil")
	})

	t.Run("example", func(t *testing.T) {
		example, row := ft.FindExample(ft.Pickles[1].AstNodeIds[1])
		assert.NotNilf(t, example, "expected example to not be nil")
		assert.NotNilf(t, row, "expected table row to not be nil")
	})

	t.Run("step", func(t *testing.T) {
		for _, ps := range ft.Pickles[0].Steps {
			step := ft.FindStep(ps.AstNodeIds[0])
			assert.NotNilf(t, step, "expected step to not be nil")
		}
	})
}

func Test_NotFind(t *testing.T) {
	testCases := []struct {
		Feature models.Feature
	}{
		{testutils.BuildTestFeature(t)},
		{testutils.BuildTestFeatureWithRules(t)},
	}

	for _, tc := range testCases {

		ft := tc.Feature
		t.Run("scenario", func(t *testing.T) {
			sc := ft.FindScenario("-")
			assert.Nilf(t, sc, "expected scenario to be nil")
		})

		t.Run("background", func(t *testing.T) {
			bg := ft.FindBackground("-")
			assert.Nilf(t, bg, "expected background to be nil")
		})

		t.Run("example", func(t *testing.T) {
			example, row := ft.FindExample("-")
			assert.Nilf(t, example, "expected example to be nil")
			assert.Nilf(t, row, "expected table row to be nil")
		})

		t.Run("step", func(t *testing.T) {
			step := ft.FindStep("-")
			assert.Nilf(t, step, "expected step to be nil")
		})
	}
}
```

## File: `internal/models/results.go`
```go
package models

import (
	"time"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/internal/utils"
)

// TestRunStarted ...
type TestRunStarted struct {
	StartedAt time.Time
}

// PickleResult ...
type PickleResult struct {
	PickleID  string
	StartedAt time.Time
}

// PickleAttachment ...
type PickleAttachment struct {
	Name     string
	MimeType string
	Data     []byte
}

// PickleStepResult ...
type PickleStepResult struct {
	Status     StepResultStatus
	FinishedAt time.Time
	Err        error

	PickleID     string
	PickleStepID string

	Def *StepDefinition

	Attachments []PickleAttachment
}

// NewStepResult ...
func NewStepResult(
	status StepResultStatus,
	pickleID, pickleStepID string,
	match *StepDefinition,
	attachments []PickleAttachment,
	err error,
) PickleStepResult {
	return PickleStepResult{
		Status:       status,
		FinishedAt:   utils.TimeNowFunc(),
		Err:          err,
		PickleID:     pickleID,
		PickleStepID: pickleStepID,
		Def:          match,
		Attachments:  attachments,
	}
}

// StepResultStatus ...
type StepResultStatus int

const (
	// Passed ...
	Passed StepResultStatus = iota
	// Failed ...
	Failed
	// Skipped ...
	Skipped
	// Undefined ...
	Undefined
	// Pending ...
	Pending
	// Ambiguous ...
	Ambiguous
)

// Color ...
func (st StepResultStatus) Color() colors.ColorFunc {
	switch st {
	case Passed:
		return colors.Green
	case Failed:
		return colors.Red
	case Skipped:
		return colors.Cyan
	default:
		return colors.Yellow
	}
}

// String ...
func (st StepResultStatus) String() string {
	switch st {
	case Passed:
		return "passed"
	case Failed:
		return "failed"
	case Skipped:
		return "skipped"
	case Undefined:
		return "undefined"
	case Pending:
		return "pending"
	case Ambiguous:
		return "ambiguous"
	default:
		return "unknown"
	}
}
```

## File: `internal/models/results_test.go`
```go
package models_test

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/cucumber/godog/colors"
	"github.com/cucumber/godog/internal/models"
)

type stepResultStatusTestCase struct {
	st  models.StepResultStatus
	str string
	clr colors.ColorFunc
}

var stepResultStatusTestCases = []stepResultStatusTestCase{
	{st: models.Passed, str: "passed", clr: colors.Green},
	{st: models.Failed, str: "failed", clr: colors.Red},
	{st: models.Skipped, str: "skipped", clr: colors.Cyan},
	{st: models.Undefined, str: "undefined", clr: colors.Yellow},
	{st: models.Pending, str: "pending", clr: colors.Yellow},
	{st: models.Ambiguous, str: "ambiguous", clr: colors.Yellow},
	{st: -1, str: "unknown", clr: colors.Yellow},
}

func Test_StepResultStatus(t *testing.T) {
	for _, tc := range stepResultStatusTestCases {
		t.Run(tc.str, func(t *testing.T) {
			assert.Equal(t, tc.str, tc.st.String())
			assert.Equal(t, tc.clr(tc.str), tc.st.Color()(tc.str))
		})
	}
}

func Test_NewStepResuklt(t *testing.T) {
	status := models.StepResultStatus(123)
	pickleID := "pickleId"
	pickleStepID := "pickleStepID"
	match := &models.StepDefinition{}
	attachments := make([]models.PickleAttachment, 0)
	err := fmt.Errorf("intentional")

	results := models.NewStepResult(status, pickleID, pickleStepID, match, attachments, err)

	assert.Equal(t, status, results.Status)
	assert.Equal(t, pickleID, results.PickleID)
	assert.Equal(t, pickleStepID, results.PickleStepID)
	assert.Equal(t, match, results.Def)
	assert.Equal(t, attachments, results.Attachments)
	assert.Equal(t, err, results.Err)
}
```

## File: `internal/models/stepdef.go`
```go
package models

import (
	"context"
	"errors"
	"fmt"
	"reflect"
	"strconv"

	messages "github.com/cucumber/messages/go/v21"

	"github.com/cucumber/godog/formatters"
)

var typeOfBytes = reflect.TypeOf([]byte(nil))

// matchable errors
var (
	ErrUnmatchedStepArgumentNumber = errors.New("func expected more arguments than given")
	ErrCannotConvert               = errors.New("cannot convert argument")
	ErrUnsupportedParameterType    = errors.New("func has unsupported parameter type")
)

// StepDefinition ...
type StepDefinition struct {
	formatters.StepDefinition

	Args         []interface{}
	HandlerValue reflect.Value
	File         string
	Line         int

	// multistep related
	Nested    bool
	Undefined []string
}

var typeOfContext = reflect.TypeOf((*context.Context)(nil)).Elem()

// Run a step with the matched arguments using reflect
// Returns one of ...
// (context, error)
// (context, godog.Steps)
func (sd *StepDefinition) Run(ctx context.Context) (context.Context, interface{}) {
	var values []reflect.Value

	typ := sd.HandlerValue.Type()
	numIn := typ.NumIn()
	hasCtxIn := numIn > 0 && typ.In(0).Implements(typeOfContext)
	ctxOffset := 0

	if hasCtxIn {
		values = append(values, reflect.ValueOf(ctx))
		ctxOffset = 1
		numIn--
	}

	if len(sd.Args) < numIn {
		return ctx, fmt.Errorf("%w: expected %d arguments, matched %d from step", ErrUnmatchedStepArgumentNumber, numIn, len(sd.Args))
	}

	for i := 0; i < numIn; i++ {
		param := typ.In(i + ctxOffset)
		switch param.Kind() {
		case reflect.Int:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseInt(s, 10, 0)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to int: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(int(v)))
		case reflect.Int64:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseInt(s, 10, 64)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to int64: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(v))
		case reflect.Int32:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseInt(s, 10, 32)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to int32: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(int32(v)))
		case reflect.Int16:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseInt(s, 10, 16)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to int16: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(int16(v)))
		case reflect.Int8:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseInt(s, 10, 8)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to int8: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(int8(v)))
		case reflect.Uint:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseUint(s, 10, 0)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to uint: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(uint(v)))
		case reflect.Uint64:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseUint(s, 10, 64)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to uint64: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(v))
		case reflect.Uint32:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseUint(s, 10, 32)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to uint32: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(uint32(v)))
		case reflect.Uint16:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseUint(s, 10, 16)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to uint16: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(uint16(v)))
		case reflect.Uint8:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseUint(s, 10, 8)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to uint8: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(uint8(v)))
		case reflect.String:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			values = append(values, reflect.ValueOf(s))
		case reflect.Float64:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseFloat(s, 64)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to float64: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(v))
		case reflect.Float32:
			s, err := sd.shouldBeString(i)
			if err != nil {
				return ctx, err
			}
			v, err := strconv.ParseFloat(s, 32)
			if err != nil {
				return ctx, fmt.Errorf(`%w %d: "%s" to float32: %s`, ErrCannotConvert, i, s, err)
			}
			values = append(values, reflect.ValueOf(float32(v)))
		case reflect.Ptr:
			arg := sd.Args[i]
			switch param.Elem().String() {
			case "messages.PickleDocString":
				if v, ok := arg.(*messages.PickleStepArgument); ok {
					values = append(values, reflect.ValueOf(v.DocString))
					break
				}

				if v, ok := arg.(*messages.PickleDocString); ok {
					values = append(values, reflect.ValueOf(v))
					break
				}

				return ctx, fmt.Errorf(`%w %d: "%v" of type "%T" to *messages.PickleDocString`, ErrCannotConvert, i, arg, arg)
			case "messages.PickleTable":
				if v, ok := arg.(*messages.PickleStepArgument); ok {
					values = append(values, reflect.ValueOf(v.DataTable))
					break
				}

				if v, ok := arg.(*messages.PickleTable); ok {
					values = append(values, reflect.ValueOf(v))
					break
				}

				return ctx, fmt.Errorf(`%w %d: "%v" of type "%T" to *messages.PickleTable`, ErrCannotConvert, i, arg, arg)
			default:
				// the error here is that the declared function has an unsupported param type - really this ought to be trapped at registration ti,e
				return ctx, fmt.Errorf("%w: the data type of parameter %d type *%s is not supported", ErrUnsupportedParameterType, i, param.Elem().String())
			}
		case reflect.Slice:
			switch param {
			case typeOfBytes:
				s, err := sd.shouldBeString(i)
				if err != nil {
					return ctx, err
				}
				values = append(values, reflect.ValueOf([]byte(s)))
			default:
				// the problem is the function decl is not using a support slice type as the param
				return ctx, fmt.Errorf("%w: the slice parameter %d type []%s is not supported", ErrUnsupportedParameterType, i, param.Elem().Kind())
			}
		case reflect.Struct:
			return ctx, fmt.Errorf("%w: the struct parameter %d type %s is not supported", ErrUnsupportedParameterType, i, param.String())
		default:
			return ctx, fmt.Errorf("%w: the parameter %d type %s is not supported", ErrUnsupportedParameterType, i, param.Kind())
		}
	}

	res := sd.HandlerValue.Call(values)
	if len(res) == 0 {
		return ctx, nil
	}

	// Note that the step fn return types were validated at Initialise in test_context.go stepWithKeyword()

	// single return value may be one of ...
	// error
	// context.Context
	// godog.Steps
	result0 := res[0].Interface()
	if len(res) == 1 {

		// if the single return value is a context then just return it
		if ctx, ok := result0.(context.Context); ok {
			return ctx, nil
		}

		// return type is presumably one of nil, "error" or "Steps" so place it into second return position
		return ctx, result0
	}

	// multi-value value return must be
	//  (context, error) and the context value must not be nil
	if ctx, ok := result0.(context.Context); ok {
		return ctx, res[1].Interface()
	}

	result1 := res[1].Interface()
	errMsg := ""
	if result1 != nil {
		errMsg = fmt.Sprintf(", step def also returned an error: %v", result1)
	}

	text := sd.StepDefinition.Expr.String()

	if result0 == nil {
		panic(fmt.Sprintf("step definition '%v' with return type (context.Context, error) must not return <nil> for the context.Context value%s", text, errMsg))
	}

	panic(fmt.Errorf("step definition '%v' has return type (context.Context, error), but found %v rather than a context.Context value%s", text, result0, errMsg))
}

func (sd *StepDefinition) shouldBeString(idx int) (string, error) {
	arg := sd.Args[idx]
	switch arg := arg.(type) {
	case string:
		return arg, nil
	case *messages.PickleStepArgument:
		if arg.DocString == nil {
			return "", fmt.Errorf(`%w %d: "%v" of type "%T": DocString is not set`, ErrCannotConvert, idx, arg, arg)
		}
		return arg.DocString.Content, nil
	case *messages.PickleDocString:
		return arg.Content, nil
	default:
		return "", fmt.Errorf(`%w %d: "%v" of type "%T" to string`, ErrCannotConvert, idx, arg, arg)
	}
}

// GetInternalStepDefinition ...
func (sd *StepDefinition) GetInternalStepDefinition() *formatters.StepDefinition {
	if sd == nil {
		return nil
	}

	return &sd.StepDefinition
}
```

## File: `internal/models/stepdef_test.go`
```go
package models_test

import (
	"context"
	"errors"
	"fmt"
	"reflect"
	"regexp"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/cucumber/godog"
	"github.com/cucumber/godog/formatters"
	"github.com/cucumber/godog/internal/models"
	messages "github.com/cucumber/messages/go/v21"
)

type ctxKey string

func TestShouldSupportVoidHandlerReturn(t *testing.T) {
	wasCalled := false
	initialCtx := context.WithValue(context.Background(), ctxKey("original"), 123)

	fn := func(ctx context.Context) {
		wasCalled = true
		assert.Equal(t, 123, ctx.Value(ctxKey("original")))
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{}

	ctx, err := def.Run(initialCtx)
	assert.True(t, wasCalled)
	// ctx is passed thru
	assert.Equal(t, initialCtx, ctx)
	assert.Nil(t, err)

}

func TestShouldSupportNilContextReturn(t *testing.T) {
	initialCtx := context.WithValue(context.Background(), ctxKey("original"), 123)

	wasCalled := false
	fn := func(ctx context.Context) context.Context {
		wasCalled = true
		assert.Equal(t, 123, ctx.Value(ctxKey("original")))

		// nil context is permitted if is single return value
		return nil
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{}
	ctx, err := def.Run(initialCtx)
	assert.True(t, wasCalled)
	// original context is substituted for a nil return value
	//  << JL : IS THIS A BUG? TWO ARG API DOESN'T ALLOW THIS
	assert.Equal(t, initialCtx, ctx)
	assert.Nil(t, err)
}

func TestShouldSupportNilErrorReturn(t *testing.T) {
	initialCtx := context.WithValue(context.Background(), ctxKey("original"), 123)

	wasCalled := false
	fn := func(ctx context.Context) error {
		wasCalled = true
		assert.Equal(t, 123, ctx.Value(ctxKey("original")))

		// nil error is permitted
		return nil
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{}
	ctx, err := def.Run(initialCtx)
	assert.True(t, wasCalled)
	// original context is passed thru if method doesn't return context.
	assert.Equal(t, initialCtx, ctx)
	assert.Nil(t, err)
}

func TestShouldSupportContextReturn(t *testing.T) {
	ctx := context.WithValue(context.Background(), ctxKey("original"), 123)

	fn := func(ctx context.Context) context.Context {
		assert.Equal(t, 123, ctx.Value(ctxKey("original")))

		return context.WithValue(ctx, ctxKey("updated"), 321)
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{}
	ctx, err := def.Run(ctx)
	assert.Nil(t, err)
	// converys the context
	assert.Equal(t, 123, ctx.Value(ctxKey("original")))
	assert.Equal(t, 321, ctx.Value(ctxKey("updated")))
}

func TestShouldSupportErrorReturn(t *testing.T) {
	ctx := context.WithValue(context.Background(), ctxKey("original"), 123)
	expectedErr := fmt.Errorf("expected error")

	fn := func(ctx context.Context) error {
		assert.Equal(t, 123, ctx.Value(ctxKey("original")))

		return expectedErr
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{}
	ctx, err := def.Run(ctx)
	// conveys the returned error
	assert.Equal(t, expectedErr, err)
	assert.Equal(t, 123, ctx.Value(ctxKey("original")))
}

func TestShouldSupportContextAndErrorReturn(t *testing.T) {

	ctx := context.WithValue(context.Background(), ctxKey("original"), 123)
	expectedErr := fmt.Errorf("expected error")

	fn := func(ctx context.Context) (context.Context, error) {
		assert.Equal(t, 123, ctx.Value(ctxKey("original")))

		return context.WithValue(ctx, ctxKey("updated"), 321), expectedErr
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{}
	ctx, err := def.Run(ctx)
	// conveys error and context
	assert.Equal(t, expectedErr, err)
	assert.Equal(t, 123, ctx.Value(ctxKey("original")))
	assert.Equal(t, 321, ctx.Value(ctxKey("updated")))
}

func TestShouldSupportContextAndNilErrorReturn(t *testing.T) {

	ctx := context.WithValue(context.Background(), ctxKey("original"), 123)

	fn := func(ctx context.Context) (context.Context, error) {
		assert.Equal(t, 123, ctx.Value(ctxKey("original")))

		return context.WithValue(ctx, ctxKey("updated"), 321), nil
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{}
	ctx, err := def.Run(ctx)
	// conveys nil error and context
	assert.Nil(t, err)
	assert.Equal(t, 123, ctx.Value(ctxKey("original")))
	assert.Equal(t, 321, ctx.Value(ctxKey("updated")))
}

func TestShouldRejectNilContextWhenMultiValueReturn(t *testing.T) {

	ctx := context.WithValue(context.Background(), ctxKey("original"), 123)

	fn := func(ctx context.Context) (context.Context, error) {
		assert.Equal(t, 123, ctx.Value(ctxKey("original")))

		// nil context is illegal.
		return nil, fmt.Errorf("expected error")
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
			Expr:    regexp.MustCompile("some regex string"),
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{}

	defer func() {
		if e := recover(); e != nil {
			pe := e.(string)
			assert.Equal(t, "step definition 'some regex string' with return type (context.Context, error) must not return <nil> for the context.Context value, step def also returned an error: expected error", pe)
		}
	}()

	def.Run(ctx)

	assert.Fail(t, "should not get here")
}

func TestArgumentCountChecks(t *testing.T) {

	wasCalled := false
	fn := func(a int, b int) {
		wasCalled = true
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{"1"}
	_, err := def.Run(context.Background())
	assert.False(t, wasCalled)
	assert.Equal(t, `func expected more arguments than given: expected 2 arguments, matched 1 from step`, err.(error).Error())
	assert.True(t, errors.Is(err.(error), models.ErrUnmatchedStepArgumentNumber))

	// FIXME - extra args are ignored - but should be reported at runtime
	def.Args = []interface{}{"1", "2", "IGNORED-EXTRA-ARG"}
	_, err = def.Run(context.Background())
	assert.True(t, wasCalled)
	assert.Nil(t, err)
}

func TestArgumentCountChecksWithContext(t *testing.T) {
	wasCalled := false
	fn := func(ctx context.Context, a int, b int) {
		wasCalled = true
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{"1"}
	_, err := def.Run(context.Background())
	assert.False(t, wasCalled)
	assert.Equal(t, `func expected more arguments than given: expected 2 arguments, matched 1 from step`, err.(error).Error())
	assert.True(t, errors.Is(err.(error), models.ErrUnmatchedStepArgumentNumber))
}

func TestShouldSupportIntTypes(t *testing.T) {
	var aActual int64
	var bActual int32
	var cActual int16
	var dActual int8

	fn := func(a int64, b int32, c int16, d int8) {
		aActual = a
		bActual = b
		cActual = c
		dActual = d
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{"1", "2", "3", "4"}
	_, err := def.Run(context.Background())
	assert.Nil(t, err)
	assert.Equal(t, int64(1), aActual)
	assert.Equal(t, int32(2), bActual)
	assert.Equal(t, int16(3), cActual)
	assert.Equal(t, int8(4), dActual)

	// 128 doesn't fit in signed 8bit int
	def.Args = []interface{}{"1", "2", "3", "128"}
	_, err = def.Run(context.Background())
	assert.Equal(t, `cannot convert argument 3: "128" to int8: strconv.ParseInt: parsing "128": value out of range`, err.(error).Error())

	def.Args = []interface{}{"1", "2", "99999", "4"}
	_, err = def.Run(context.Background())
	assert.Equal(t, `cannot convert argument 2: "99999" to int16: strconv.ParseInt: parsing "99999": value out of range`, err.(error).Error())

	def.Args = []interface{}{"1", strings.Repeat("2", 32), "3", "4"}
	_, err = def.Run(context.Background())
	assert.Equal(t, `cannot convert argument 1: "22222222222222222222222222222222" to int32: strconv.ParseInt: parsing "22222222222222222222222222222222": value out of range`, err.(error).Error())

	def.Args = []interface{}{strings.Repeat("1", 32), "2", "3", "4"}
	_, err = def.Run(context.Background())
	assert.Equal(t, `cannot convert argument 0: "11111111111111111111111111111111" to int64: strconv.ParseInt: parsing "11111111111111111111111111111111": value out of range`, err.(error).Error())
}

func TestShouldSupportUintTypes(t *testing.T) {
	var aActual uint64
	var bActual uint32
	var cActual uint16
	var dActual uint8

	fn := func(a uint64, b uint32, c uint16, d uint8) {
		aActual = a
		bActual = b
		cActual = c
		dActual = d
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{"1", "2", "3", "4"}
	_, err := def.Run(context.Background())
	assert.Nil(t, err)
	assert.Equal(t, uint64(1), aActual)
	assert.Equal(t, uint32(2), bActual)
	assert.Equal(t, uint16(3), cActual)
	assert.Equal(t, uint8(4), dActual)

	// 256 doesn't fit in uint8
	def.Args = []interface{}{"1", "2", "3", "256"}
	_, err = def.Run(context.Background())
	assert.Equal(t, `cannot convert argument 3: "256" to uint8: strconv.ParseUint: parsing "256": value out of range`, err.(error).Error())

	// 65536 doesn't fit in uint16
	def.Args = []interface{}{"1", "2", "65536", "4"}
	_, err = def.Run(context.Background())
	assert.Equal(t, `cannot convert argument 2: "65536" to uint16: strconv.ParseUint: parsing "65536": value out of range`, err.(error).Error())

	// 4294967296 too large for uint32
	def.Args = []interface{}{"1", "4294967296", "3", "4"}
	_, err = def.Run(context.Background())
	assert.Equal(t, `cannot convert argument 1: "4294967296" to uint32: strconv.ParseUint: parsing "4294967296": value out of range`, err.(error).Error())

	// 18446744073709551616 too large for uint64
	def.Args = []interface{}{"18446744073709551616", "2", "3", "4"}
	_, err = def.Run(context.Background())
	assert.Equal(t, `cannot convert argument 0: "18446744073709551616" to uint64: strconv.ParseUint: parsing "18446744073709551616": value out of range`, err.(error).Error())
}

func TestShouldSupportFloatTypes(t *testing.T) {
	var aActual float64
	var bActual float32
	fn := func(a float64, b float32) {
		aActual = a
		bActual = b
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
	}

	def.Args = []interface{}{"1.1", "2.2"}
	_, err := def.Run(context.Background())
	assert.Nil(t, err)
	assert.Equal(t, float64(1.1), aActual)
	assert.Equal(t, float32(2.2), bActual)

	def.Args = []interface{}{"1.1", strings.Repeat("2", 65) + ".22"}
	_, err = def.Run(context.Background())
	assert.Equal(t, `cannot convert argument 1: "22222222222222222222222222222222222222222222222222222222222222222.22" to float32: strconv.ParseFloat: parsing "22222222222222222222222222222222222222222222222222222222222222222.22": value out of range`, err.(error).Error())
}

func TestShouldSupportGherkinDocstring(t *testing.T) {
	var actualDocString *messages.PickleDocString
	fnDocstring := func(a *messages.PickleDocString) {
		actualDocString = a
	}

	expectedDocString := &messages.PickleDocString{Content: "hello"}
	defDocstring := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fnDocstring,
		},
		HandlerValue: reflect.ValueOf(fnDocstring),
		Args:         []interface{}{expectedDocString},
	}

	_, err := defDocstring.Run(context.Background())
	assert.Nil(t, err)
	assert.Equal(t, expectedDocString, actualDocString)
}

func TestShouldSupportGherkinTable(t *testing.T) {

	var actualTable *messages.PickleTable
	fnTable := func(a *messages.PickleTable) {
		actualTable = a
	}

	expectedTable := &messages.PickleTable{}
	defTable := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fnTable,
		},
		HandlerValue: reflect.ValueOf(fnTable),
		Args:         []interface{}{expectedTable},
	}

	_, err := defTable.Run(context.Background())
	assert.Nil(t, err)
	assert.Equal(t, expectedTable, actualTable)
}

func TestShouldSupportOnlyByteSlice(t *testing.T) {
	var aActual []byte
	fn1 := func(a []byte) {
		aActual = a
	}
	fn2 := func(a []string) {
		assert.Fail(t, "fn2 should not be called")
	}

	def1 := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn1,
		},
		HandlerValue: reflect.ValueOf(fn1),
		Args:         []interface{}{"str"},
	}

	def2 := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn2,
		},
		HandlerValue: reflect.ValueOf(fn2),
		Args:         []interface{}{[]string{}},
	}

	_, err := def1.Run(context.Background())
	assert.Nil(t, err)
	assert.Equal(t, []byte{'s', 't', 'r'}, aActual)

	_, err = def2.Run(context.Background())
	assert.Equal(t, `func has unsupported parameter type: the slice parameter 0 type []string is not supported`, err.(error).Error())
	assert.True(t, errors.Is(err.(error), models.ErrUnsupportedParameterType))
}

// this test is superficial compared to the ones above where the actual error messages the user woudl see are verified
func TestStepDefinition_Run_StepArgsShouldBeString(t *testing.T) {
	test := func(t *testing.T, fn interface{}, expectedError string) {
		def := &models.StepDefinition{
			StepDefinition: formatters.StepDefinition{
				Handler: fn,
			},
			HandlerValue: reflect.ValueOf(fn),
		}

		// some value that is not a string
		def.Args = []interface{}{12}

		_, res := def.Run(context.Background())
		if res == nil {
			t.Fatalf("expected a string convertion error, but got none")
		}

		err, ok := res.(error)
		if !ok {
			t.Fatalf("expected a string convertion error, but got %T instead", res)
		}

		if !errors.Is(err, models.ErrCannotConvert) {
			t.Fatalf("expected a string convertion error, but got '%v' instead", err)
		}

		assert.Equal(t, expectedError, err.Error())
	}

	// Ensure step type error if step argument is not a string
	// for all supported types.
	const toStringError = `cannot convert argument 0: "12" of type "int" to string`
	shouldNotBeCalled := func() { assert.Fail(t, "shound not be called") }
	test(t, func(a int) { shouldNotBeCalled() }, toStringError)
	test(t, func(a int64) { shouldNotBeCalled() }, toStringError)
	test(t, func(a int32) { shouldNotBeCalled() }, toStringError)
	test(t, func(a int16) { shouldNotBeCalled() }, toStringError)
	test(t, func(a int8) { shouldNotBeCalled() }, toStringError)
	test(t, func(a string) { shouldNotBeCalled() }, toStringError)
	test(t, func(a float64) { shouldNotBeCalled() }, toStringError)
	test(t, func(a float32) { shouldNotBeCalled() }, toStringError)
	test(t, func(a *godog.Table) { shouldNotBeCalled() }, `cannot convert argument 0: "12" of type "int" to *messages.PickleTable`)
	test(t, func(a *godog.DocString) { shouldNotBeCalled() }, `cannot convert argument 0: "12" of type "int" to *messages.PickleDocString`)
	test(t, func(a []byte) { shouldNotBeCalled() }, toStringError)

}

func TestStepDefinition_Run_InvalidHandlerParamConversion(t *testing.T) {
	test := func(t *testing.T, fn interface{}, expectedError string) {
		def := &models.StepDefinition{
			StepDefinition: formatters.StepDefinition{
				Handler: fn,
			},
			HandlerValue: reflect.ValueOf(fn),
		}

		def.Args = []interface{}{12}

		_, res := def.Run(context.Background())
		if res == nil {
			t.Fatalf("expected an unsupported argument type error, but got none")
		}

		err, ok := res.(error)
		if !ok {
			t.Fatalf("expected an unsupported argument type error, but got %T instead", res)
		}

		if !errors.Is(err, models.ErrUnsupportedParameterType) {
			// FIXME JL - check logic as the error message was wrong
			t.Fatalf("expected an unsupported argument type error, but got '%v' instead", err)
		}

		assert.Equal(t, expectedError, err.Error())
	}

	shouldNotBeCalled := func() { assert.Fail(t, "shound not be called") }

	// Lists some unsupported argument types for step handler.

	// Pointers should work only for godog.Table/godog.DocString
	test(t, func(a *int) { shouldNotBeCalled() }, "func has unsupported parameter type: the data type of parameter 0 type *int is not supported")
	test(t, func(a *int64) { shouldNotBeCalled() }, "func has unsupported parameter type: the data type of parameter 0 type *int64 is not supported")
	test(t, func(a *int32) { shouldNotBeCalled() }, "func has unsupported parameter type: the data type of parameter 0 type *int32 is not supported")
	test(t, func(a *int16) { shouldNotBeCalled() }, "func has unsupported parameter type: the data type of parameter 0 type *int16 is not supported")
	test(t, func(a *int8) { shouldNotBeCalled() }, "func has unsupported parameter type: the data type of parameter 0 type *int8 is not supported")
	test(t, func(a *string) { shouldNotBeCalled() }, "func has unsupported parameter type: the data type of parameter 0 type *string is not supported")
	test(t, func(a *float64) { shouldNotBeCalled() }, "func has unsupported parameter type: the data type of parameter 0 type *float64 is not supported")
	test(t, func(a *float32) { shouldNotBeCalled() }, "func has unsupported parameter type: the data type of parameter 0 type *float32 is not supported")

	// I cannot pass structures
	test(t, func(a godog.Table) { shouldNotBeCalled() }, "func has unsupported parameter type: the struct parameter 0 type messages.PickleTable is not supported")
	test(t, func(a godog.DocString) { shouldNotBeCalled() }, "func has unsupported parameter type: the struct parameter 0 type messages.PickleDocString is not supported")
	test(t, func(a testStruct) { shouldNotBeCalled() }, "func has unsupported parameter type: the struct parameter 0 type models_test.testStruct is not supported")

	// // I cannot use maps
	test(t, func(a map[string]interface{ body() }) { shouldNotBeCalled() }, "func has unsupported parameter type: the parameter 0 type map is not supported")
	test(t, func(a map[string]int) { shouldNotBeCalled() }, "func has unsupported parameter type: the parameter 0 type map is not supported")

	// // Slice works only for byte
	test(t, func(a []int) { shouldNotBeCalled() }, "func has unsupported parameter type: the slice parameter 0 type []int is not supported")
	test(t, func(a []string) { shouldNotBeCalled() }, "func has unsupported parameter type: the slice parameter 0 type []string is not supported")
	test(t, func(a []bool) { shouldNotBeCalled() }, "func has unsupported parameter type: the slice parameter 0 type []bool is not supported")

	// // I cannot use bool
	test(t, func(a bool) { shouldNotBeCalled() }, "func has unsupported parameter type: the parameter 0 type bool is not supported")

}

func TestStepDefinition_Run_StringConversionToFunctionType(t *testing.T) {
	test := func(t *testing.T, fn interface{}, args []interface{}, expectedError string) {
		def := &models.StepDefinition{
			StepDefinition: formatters.StepDefinition{
				Handler: fn,
			},
			HandlerValue: reflect.ValueOf(fn),
			Args:         args,
		}

		_, res := def.Run(context.Background())
		if res == nil {
			t.Fatalf("expected a cannot convert argument type error, but got none")
		}

		err, ok := res.(error)
		if !ok {
			t.Fatalf("expected a cannot convert argument type error, but got %T instead", res)
		}

		if !errors.Is(err, models.ErrCannotConvert) {
			t.Fatalf("expected a cannot convert argument type error, but got '%v' instead", err)
		}

		assert.Equal(t, expectedError, err.Error())
	}

	shouldNotBeCalled := func() { assert.Fail(t, "shound not be called") }

	// Lists some unsupported argument types for step handler.

	// Cannot convert invalid int
	test(t, func(a int) { shouldNotBeCalled() }, []interface{}{"a"}, `cannot convert argument 0: "a" to int: strconv.ParseInt: parsing "a": invalid syntax`)
	test(t, func(a int64) { shouldNotBeCalled() }, []interface{}{"a"}, `cannot convert argument 0: "a" to int64: strconv.ParseInt: parsing "a": invalid syntax`)
	test(t, func(a int32) { shouldNotBeCalled() }, []interface{}{"a"}, `cannot convert argument 0: "a" to int32: strconv.ParseInt: parsing "a": invalid syntax`)
	test(t, func(a int16) { shouldNotBeCalled() }, []interface{}{"a"}, `cannot convert argument 0: "a" to int16: strconv.ParseInt: parsing "a": invalid syntax`)
	test(t, func(a int8) { shouldNotBeCalled() }, []interface{}{"a"}, `cannot convert argument 0: "a" to int8: strconv.ParseInt: parsing "a": invalid syntax`)

	// Cannot convert invalid float
	test(t, func(a float32) { shouldNotBeCalled() }, []interface{}{"a"}, `cannot convert argument 0: "a" to float32: strconv.ParseFloat: parsing "a": invalid syntax`)
	test(t, func(a float64) { shouldNotBeCalled() }, []interface{}{"a"}, `cannot convert argument 0: "a" to float64: strconv.ParseFloat: parsing "a": invalid syntax`)

	// Cannot convert to DataArg
	test(t, func(a *godog.Table) { shouldNotBeCalled() }, []interface{}{"194"}, `cannot convert argument 0: "194" of type "string" to *messages.PickleTable`)

	// Cannot convert to DocString ?
	test(t, func(a *godog.DocString) { shouldNotBeCalled() }, []interface{}{"194"}, `cannot convert argument 0: "194" of type "string" to *messages.PickleDocString`)

}

// @TODO maybe we should support duration
// fn2 := func(err time.Duration) error { return nil }
// def = &models.StepDefinition{Handler: fn2, HandlerValue: reflect.ValueOf(fn2)}

// def.Args = []interface{}{"1"}
// if _, err := def.Run(context.Background()); err == nil {
// 	t.Fatalf("expected an error due to wrong argument type, but got none")
// }

type testStruct struct {
	_ string
}

func TestShouldSupportDocStringToStringConversion(t *testing.T) {
	var aActual string
	fn := func(a string) {
		aActual = a
	}

	def := &models.StepDefinition{
		StepDefinition: formatters.StepDefinition{
			Handler: fn,
		},
		HandlerValue: reflect.ValueOf(fn),
		Args: []interface{}{&messages.PickleDocString{
			Content: "hello",
		}},
	}

	_, err := def.Run(context.Background())
	assert.Nil(t, err)
	assert.Equal(t, "hello", aActual)
}
```

## File: `internal/parser/parser.go`
```go
package parser

import (
	"bytes"
	"fmt"
	"io"
	"io/fs"
	"os"
	"regexp"
	"strconv"
	"strings"

	gherkin "github.com/cucumber/gherkin/go/v26"
	messages "github.com/cucumber/messages/go/v21"

	"github.com/cucumber/godog/internal/flags"
	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/tags"
)

var pathLineRe = regexp.MustCompile(`:([\d]+)$`)

// ExtractFeaturePathLine ...
func ExtractFeaturePathLine(p string) (string, int) {
	line := -1
	retPath := p
	if m := pathLineRe.FindStringSubmatch(p); len(m) > 0 {
		if i, err := strconv.Atoi(m[1]); err == nil {
			line = i
			retPath = p[:strings.LastIndexByte(p, ':')]
		}
	}
	return retPath, line
}

func parseFeatureFile(fsys fs.FS, path, dialect string, newIDFunc func() string) (*models.Feature, error) {
	reader, err := fsys.Open(path)
	if err != nil {
		return nil, err
	}

	defer reader.Close()

	var buf bytes.Buffer
	gherkinDocument, err := gherkin.ParseGherkinDocumentForLanguage(io.TeeReader(reader, &buf), dialect, newIDFunc)
	if err != nil {
		return nil, fmt.Errorf("%s - %v", path, err)
	}

	gherkinDocument.Uri = path
	pickles := gherkin.Pickles(*gherkinDocument, path, newIDFunc)

	f := models.Feature{GherkinDocument: gherkinDocument, Pickles: pickles, Content: buf.Bytes()}
	return &f, nil
}

func parseBytes(path string, feature []byte, dialect string, newIDFunc func() string) (*models.Feature, error) {
	reader := bytes.NewReader(feature)

	var buf bytes.Buffer
	gherkinDocument, err := gherkin.ParseGherkinDocumentForLanguage(io.TeeReader(reader, &buf), dialect, newIDFunc)
	if err != nil {
		return nil, fmt.Errorf("%s - %v", path, err)
	}

	gherkinDocument.Uri = path
	pickles := gherkin.Pickles(*gherkinDocument, path, newIDFunc)

	f := models.Feature{GherkinDocument: gherkinDocument, Pickles: pickles, Content: buf.Bytes()}
	return &f, nil
}

func parseFeatureDir(fsys fs.FS, dir, dialect string, newIDFunc func() string) ([]*models.Feature, error) {
	var features []*models.Feature
	return features, fs.WalkDir(fsys, dir, func(p string, f fs.DirEntry, err error) error {
		if err != nil {
			return err
		}

		if f.IsDir() {
			return nil
		}

		if !strings.HasSuffix(p, ".feature") {
			return nil
		}

		feat, err := parseFeatureFile(fsys, p, dialect, newIDFunc)
		if err != nil {
			return err
		}

		features = append(features, feat)
		return nil
	})
}

func parsePath(fsys fs.FS, path, dialect string, newIDFunc func() string) ([]*models.Feature, error) {
	var features []*models.Feature

	path, line := ExtractFeaturePathLine(path)

	fi, err := func() (fs.FileInfo, error) {
		file, err := fsys.Open(path)
		if err != nil {
			return nil, err
		}
		defer file.Close()

		return file.Stat()
	}()
	if err != nil {
		return features, err
	}

	if fi.IsDir() {
		return parseFeatureDir(fsys, path, dialect, newIDFunc)
	}

	ft, err := parseFeatureFile(fsys, path, dialect, newIDFunc)
	if err != nil {
		return features, err
	}

	// filter scenario by line number
	var pickles []*messages.Pickle

	if line != -1 {
		ft.Uri += ":" + strconv.Itoa(line)
	}

	for _, pickle := range ft.Pickles {
		sc := ft.FindScenario(pickle.AstNodeIds[0])

		if line == -1 || int64(line) == sc.Location.Line {
			if line != -1 {
				pickle.Uri += ":" + strconv.Itoa(line)
			}

			pickles = append(pickles, pickle)
		}
	}
	ft.Pickles = pickles

	return append(features, ft), nil
}

// ParseFeatures ...
func ParseFeatures(fsys fs.FS, filter, dialect string, paths []string) ([]*models.Feature, error) {
	var order int

	if dialect == "" {
		dialect = gherkin.DefaultDialect
	}

	featureIdxs := make(map[string]int)
	uniqueFeatureURI := make(map[string]*models.Feature)
	newIDFunc := (&messages.Incrementing{}).NewId
	for _, path := range paths {
		feats, err := parsePath(fsys, path, dialect, newIDFunc)

		switch {
		case os.IsNotExist(err):
			return nil, fmt.Errorf(`feature path "%s" is not available`, path)
		case os.IsPermission(err):
			return nil, fmt.Errorf(`feature path "%s" is not accessible`, path)
		case err != nil:
			return nil, err
		}

		for _, ft := range feats {
			if _, duplicate := uniqueFeatureURI[ft.Uri]; duplicate {
				continue
			}

			uniqueFeatureURI[ft.Uri] = ft
			featureIdxs[ft.Uri] = order

			order++
		}
	}

	var features = make([]*models.Feature, len(uniqueFeatureURI))
	for uri, feature := range uniqueFeatureURI {
		idx := featureIdxs[uri]
		features[idx] = feature
	}

	features = filterFeatures(filter, features)

	return features, nil
}

type FeatureContent = flags.Feature

func ParseFromBytes(filter, dialect string, featuresInputs []FeatureContent) ([]*models.Feature, error) {
	var order int

	if dialect == "" {
		dialect = gherkin.DefaultDialect
	}

	featureIdxs := make(map[string]int)
	uniqueFeatureURI := make(map[string]*models.Feature)
	newIDFunc := (&messages.Incrementing{}).NewId
	for _, f := range featuresInputs {
		ft, err := parseBytes(f.Name, f.Contents, dialect, newIDFunc)
		if err != nil {
			return nil, err
		}

		if _, duplicate := uniqueFeatureURI[ft.Uri]; duplicate {
			continue
		}

		uniqueFeatureURI[ft.Uri] = ft
		featureIdxs[ft.Uri] = order

		order++
	}

	var features = make([]*models.Feature, len(uniqueFeatureURI))
	for uri, feature := range uniqueFeatureURI {
		idx := featureIdxs[uri]
		features[idx] = feature
	}

	features = filterFeatures(filter, features)

	return features, nil
}

func filterFeatures(filter string, features []*models.Feature) (result []*models.Feature) {
	for _, ft := range features {
		ft.Pickles = tags.ApplyTagFilter(filter, ft.Pickles)

		if ft.Feature != nil && len(ft.Pickles) > 0 {
			result = append(result, ft)
		}
	}

	return
}
```

## File: `internal/parser/parser_test.go`
```go
package parser_test

import (
	"errors"
	"io/fs"
	"path/filepath"
	"testing"
	"testing/fstest"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/cucumber/godog/internal/parser"
)

func Test_FeatureFilePathParser(t *testing.T) {
	type Case struct {
		input string
		path  string
		line  int
	}

	cases := []Case{
		{"/home/test.feature", "/home/test.feature", -1},
		{"/home/test.feature:21", "/home/test.feature", 21},
		{"test.feature", "test.feature", -1},
		{"test.feature:2", "test.feature", 2},
		{"", "", -1},
		{"/c:/home/test.feature", "/c:/home/test.feature", -1},
		{"/c:/home/test.feature:3", "/c:/home/test.feature", 3},
		{"D:\\home\\test.feature:3", "D:\\home\\test.feature", 3},
	}

	for _, c := range cases {
		p, ln := parser.ExtractFeaturePathLine(c.input)
		assert.Equal(t, p, c.path)
		assert.Equal(t, ln, c.line)
	}
}

func Test_ParseFromBytes_FromMultipleFeatures_DuplicateNames(t *testing.T) {
	eatGodogContents := `
Feature: eat godogs
  In order to be happy
  As a hungry gopher
  I need to be able to eat godogs

  Scenario: Eat 5 out of 12
    Given there are 12 godogs
    When I eat 5
    Then there should be 7 remaining`
	input := []parser.FeatureContent{
		{Name: "MyCoolDuplicatedFeature", Contents: []byte(eatGodogContents)},
		{Name: "MyCoolDuplicatedFeature", Contents: []byte(eatGodogContents)},
	}

	featureFromBytes, err := parser.ParseFromBytes("", "", input)
	require.NoError(t, err)
	require.Len(t, featureFromBytes, 1)
}

func Test_ParseFromBytes_FromMultipleFeatures(t *testing.T) {
	featureFileName := "godogs.feature"
	eatGodogContents := `
Feature: eat godogs
  In order to be happy
  As a hungry gopher
  I need to be able to eat godogs

  Scenario: Eat 5 out of 12
    Given there are 12 godogs
    When I eat 5
    Then there should be 7 remaining`

	baseDir := "base"
	fsys := fstest.MapFS{
		filepath.Join(baseDir, featureFileName): {
			Data: []byte(eatGodogContents),
			Mode: fs.FileMode(0644),
		},
	}

	featureFromFile, err := parser.ParseFeatures(fsys, "", "", []string{baseDir})
	require.NoError(t, err)
	require.Len(t, featureFromFile, 1)

	input := []parser.FeatureContent{
		{Name: filepath.Join(baseDir, featureFileName), Contents: []byte(eatGodogContents)},
	}

	featureFromBytes, err := parser.ParseFromBytes("", "", input)
	require.NoError(t, err)
	require.Len(t, featureFromBytes, 1)

	assert.Equal(t, featureFromFile, featureFromBytes)
}

func Test_ParseFeatures_FromMultiplePaths(t *testing.T) {
	const (
		defaultFeatureFile     = "godogs.feature"
		defaultFeatureContents = `Feature: eat godogs
  In order to be happy
  As a hungry gopher
  I need to be able to eat godogs

  Scenario: Eat 5 out of 12
    Given there are 12 godogs
    When I eat 5
		Then there should be 7 remaining`
	)

	tests := map[string]struct {
		fsys  fs.FS
		paths []string

		expFeatures int
		expError    error
	}{
		"feature directories can be parsed": {
			paths: []string{"base/a", "base/b"},
			fsys: fstest.MapFS{
				filepath.Join("base/a", defaultFeatureFile): {
					Data: []byte(defaultFeatureContents),
				},
				filepath.Join("base/b", defaultFeatureFile): {
					Data: []byte(defaultFeatureContents),
				},
			},
			expFeatures: 2,
		},
		"path not found errors": {
			fsys:     fstest.MapFS{},
			paths:    []string{"base/a", "base/b"},
			expError: errors.New(`feature path "base/a" is not available`),
		},
		"feature files can be parsed": {
			paths: []string{
				filepath.Join("base/a/", defaultFeatureFile),
				filepath.Join("base/b/", defaultFeatureFile),
			},
			fsys: fstest.MapFS{
				filepath.Join("base/a", defaultFeatureFile): {
					Data: []byte(defaultFeatureContents),
				},
				filepath.Join("base/b", defaultFeatureFile): {
					Data: []byte(defaultFeatureContents),
				},
			},
			expFeatures: 2,
		},
	}

	for name, test := range tests {
		test := test
		t.Run(name, func(t *testing.T) {
			t.Parallel()

			features, err := parser.ParseFeatures(test.fsys, "", "", test.paths)
			if test.expError != nil {
				require.Error(t, err)
				require.EqualError(t, err, test.expError.Error())
				return
			}

			assert.Nil(t, err)
			assert.Len(t, features, test.expFeatures)

			pickleIDs := map[string]bool{}
			for _, f := range features {
				for _, p := range f.Pickles {
					if pickleIDs[p.Id] {
						assert.Failf(t, "found duplicate pickle ID", "Pickle ID %s was already used", p.Id)
					}

					pickleIDs[p.Id] = true
				}
			}
		})
	}
}

func Test_ParseFeatures_Localisation(t *testing.T) {
	tests := map[string]struct {
		dialect  string
		contents string
	}{
		"english": {
			dialect: "en",
			contents: `
Feature: dummy
  Rule: dummy
    Background: dummy
      Given dummy
      When dummy
      Then dummy
    Scenario: dummy
      Given dummy
      When dummy
      Then dummy
      And dummy
      But dummy
    Example: dummy
      Given dummy
      When dummy
      Then dummy
    Scenario Outline: dummy
      Given dummy
      When dummy
      Then dummy
      `,
		},
		"afrikaans": {
			dialect: "af",
			contents: `
Funksie: dummy
  Regel: dummy
    Agtergrond: dummy
      Gegewe dummy
      Wanneer dummy
      Dan dummy
    Voorbeeld: dummy
      Gegewe dummy
      Wanneer dummy
      Dan dummy
      En dummy
      Maar dummy
    Voorbeelde: dummy
      Gegewe dummy
      Wanneer dummy
      Dan dummy
    Situasie Uiteensetting: dummy
      Gegewe dummy
      Wanneer dummy
      Dan dummy
      `,
		},
		"arabic": {
			dialect: "ar",
			contents: `
خاصية: dummy
  Rule: dummy
    الخلفية: dummy
      بفرض  dummy
      متى  dummy
      اذاً  dummy
    مثال: dummy
      بفرض  dummy
      متى  dummy
      اذاً  dummy
      و dummy
      لكن dummy
    امثلة: dummy
      بفرض  dummy
      متى  dummy
      اذاً  dummy
    سيناريو مخطط: dummy
      بفرض  dummy
      متى  dummy
      اذاً  dummy
      `,
		},
		"chinese simplified": {
			dialect: "zh-CN",
			contents: `
功能: dummy
  规则: dummy
    背景: dummy
      假如 dummy
      当 dummy
      那么 dummy
    场景: dummy
      假如 dummy
      当 dummy
      那么 dummy
      而且 dummy
      但是 dummy
    例子: dummy
      假如 dummy
      当 dummy
      那么 dummy
    场景大纲: dummy
      假如 dummy
      当 dummy
      那么 dummy
      `,
		},
	}

	featureFileName := "godogs.feature"
	baseDir := "base"

	for name, test := range tests {
		test := test
		t.Run(name, func(t *testing.T) {
			t.Parallel()

			fsys := fstest.MapFS{
				filepath.Join(baseDir, featureFileName): {
					Data: []byte(test.contents),
					Mode: fs.FileMode(0o644),
				},
			}

			featureTestDialect, err := parser.ParseFeatures(fsys, "", test.dialect, []string{baseDir})
			require.NoError(t, err)
			require.Len(t, featureTestDialect, 1)
		})
	}
}
```

## File: `internal/vault/fs.go`
```go
package storage

import (
	"io/fs"
	"os"
)

// FS is a wrapper that falls back to `os`.
type FS struct {
	FS fs.FS
}

// Open a file in the provided `fs.FS`. If none provided,
// open via `os.Open`
func (f FS) Open(name string) (fs.File, error) {
	if f.FS == nil {
		return os.Open(name)
	}

	return f.FS.Open(name)
}
```

## File: `internal/vault/fs_test.go`
```go
package storage_test

import (
	"errors"
	"io/fs"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
	"testing"
	"testing/fstest"

	"github.com/cucumber/godog/internal/storage"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestStorage_Open_FS(t *testing.T) {
	tests := map[string]struct {
		fs fs.FS

		expData  []byte
		expError error
	}{
		"normal open": {
			fs: fstest.MapFS{
				"testfile": {
					Data: []byte("hello worlds"),
				},
			},
			expData: []byte("hello worlds"),
		},
		"file not found": {
			fs:       fstest.MapFS{},
			expError: errors.New("open testfile: file does not exist"),
		},
		"nil fs falls back on os": {
			expError: errors.New("open testfile: no such file or directory"),
		},
	}

	for name, test := range tests {
		test := test
		t.Run(name, func(t *testing.T) {
			t.Parallel()

			f, err := (storage.FS{FS: test.fs}).Open("testfile")
			if test.expError != nil {
				assert.Error(t, err)
				assert.EqualError(t, err, test.expError.Error())
				return
			}

			assert.NoError(t, err)

			bb := make([]byte, len(test.expData))
			_, _ = f.Read(bb)
			assert.Equal(t, test.expData, bb)
		})
	}
}

func TestStorage_Open_OS(t *testing.T) {
	tests := map[string]struct {
		files    map[string][]byte
		expData  []byte
		expError error
	}{
		"normal open": {
			files: map[string][]byte{
				"testfile": []byte("hello worlds"),
			},
			expData: []byte("hello worlds"),
		},
		"nil fs falls back on os": {
			expError: errors.New("open %baseDir%/testfile: no such file or directory"),
		},
	}

	for name, test := range tests {
		test := test
		t.Run(name, func(t *testing.T) {
			t.Parallel()

			baseDir := filepath.Join(os.TempDir(), t.Name(), "godogs")
			err := os.MkdirAll(baseDir+"/a", 0755)
			defer os.RemoveAll(baseDir)

			require.Nil(t, err)

			for name, data := range test.files {
				err := ioutil.WriteFile(filepath.Join(baseDir, name), data, 0644)
				require.NoError(t, err)
			}

			f, err := (storage.FS{}).Open(filepath.Join(baseDir, "testfile"))
			if test.expError != nil {
				assert.Error(t, err)
				assert.EqualError(t, err, strings.ReplaceAll(test.expError.Error(), "%baseDir%", baseDir))
				return
			}

			assert.NoError(t, err)

			bb := make([]byte, len(test.expData))
			_, _ = f.Read(bb)
			assert.Equal(t, test.expData, bb)
		})
	}
}
```

## File: `internal/vault/storage.go`
```go
package storage

import (
	"fmt"
	"sync"

	messages "github.com/cucumber/messages/go/v21"
	"github.com/hashicorp/go-memdb"

	"github.com/cucumber/godog/internal/models"
)

const (
	writeMode bool = true
	readMode  bool = false

	tableFeature         string = "feature"
	tableFeatureIndexURI string = "id"

	tablePickle         string = "pickle"
	tablePickleIndexID  string = "id"
	tablePickleIndexURI string = "uri"

	tablePickleStep        string = "pickle_step"
	tablePickleStepIndexID string = "id"

	tablePickleResult              string = "pickle_result"
	tablePickleResultIndexPickleID string = "id"

	tablePickleStepResult                  string = "pickle_step_result"
	tablePickleStepResultIndexPickleStepID string = "id"
	tablePickleStepResultIndexPickleID     string = "pickle_id"
	tablePickleStepResultIndexStatus       string = "status"

	tableStepDefintionMatch            string = "step_defintion_match"
	tableStepDefintionMatchIndexStepID string = "id"
)

// Storage is a thread safe in-mem storage
type Storage struct {
	db *memdb.MemDB

	testRunStarted     models.TestRunStarted
	testRunStartedLock *sync.Mutex
}

// NewStorage will create an in-mem storage that
// is used across concurrent runners and formatters
func NewStorage() *Storage {
	schema := memdb.DBSchema{
		Tables: map[string]*memdb.TableSchema{
			tableFeature: {
				Name: tableFeature,
				Indexes: map[string]*memdb.IndexSchema{
					tableFeatureIndexURI: {
						Name:    tableFeatureIndexURI,
						Unique:  true,
						Indexer: &memdb.StringFieldIndex{Field: "Uri"},
					},
				},
			},
			tablePickle: {
				Name: tablePickle,
				Indexes: map[string]*memdb.IndexSchema{
					tablePickleIndexID: {
						Name:    tablePickleIndexID,
						Unique:  true,
						Indexer: &memdb.StringFieldIndex{Field: "Id"},
					},
					tablePickleIndexURI: {
						Name:    tablePickleIndexURI,
						Unique:  false,
						Indexer: &memdb.StringFieldIndex{Field: "Uri"},
					},
				},
			},
			tablePickleStep: {
				Name: tablePickleStep,
				Indexes: map[string]*memdb.IndexSchema{
					tablePickleStepIndexID: {
						Name:    tablePickleStepIndexID,
						Unique:  true,
						Indexer: &memdb.StringFieldIndex{Field: "Id"},
					},
				},
			},
			tablePickleResult: {
				Name: tablePickleResult,
				Indexes: map[string]*memdb.IndexSchema{
					tablePickleResultIndexPickleID: {
						Name:    tablePickleResultIndexPickleID,
						Unique:  true,
						Indexer: &memdb.StringFieldIndex{Field: "PickleID"},
					},
				},
			},
			tablePickleStepResult: {
				Name: tablePickleStepResult,
				Indexes: map[string]*memdb.IndexSchema{
					tablePickleStepResultIndexPickleStepID: {
						Name:    tablePickleStepResultIndexPickleStepID,
						Unique:  true,
						Indexer: &memdb.StringFieldIndex{Field: "PickleStepID"},
					},
					tablePickleStepResultIndexPickleID: {
						Name:    tablePickleStepResultIndexPickleID,
						Unique:  false,
						Indexer: &memdb.StringFieldIndex{Field: "PickleID"},
					},
					tablePickleStepResultIndexStatus: {
						Name:    tablePickleStepResultIndexStatus,
						Unique:  false,
						Indexer: &memdb.IntFieldIndex{Field: "Status"},
					},
				},
			},
			tableStepDefintionMatch: {
				Name: tableStepDefintionMatch,
				Indexes: map[string]*memdb.IndexSchema{
					tableStepDefintionMatchIndexStepID: {
						Name:    tableStepDefintionMatchIndexStepID,
						Unique:  true,
						Indexer: &memdb.StringFieldIndex{Field: "StepID"},
					},
				},
			},
		},
	}

	db, err := memdb.NewMemDB(&schema)
	if err != nil {
		panic(err)
	}

	return &Storage{db: db, testRunStartedLock: new(sync.Mutex)}
}

// MustInsertPickle will insert a pickle and it's steps,
// will panic on error.
func (s *Storage) MustInsertPickle(p *messages.Pickle) {
	txn := s.db.Txn(writeMode)

	if err := txn.Insert(tablePickle, p); err != nil {
		panic(err)
	}

	for _, step := range p.Steps {
		if err := txn.Insert(tablePickleStep, step); err != nil {
			panic(err)
		}
	}

	txn.Commit()
}

// MustGetPickle will retrieve a pickle by id and panic on error.
func (s *Storage) MustGetPickle(id string) *messages.Pickle {
	v := s.mustFirst(tablePickle, tablePickleIndexID, id)
	return v.(*messages.Pickle)
}

// MustGetPickles will retrieve pickles by URI and panic on error.
func (s *Storage) MustGetPickles(uri string) (ps []*messages.Pickle) {
	it := s.mustGet(tablePickle, tablePickleIndexURI, uri)
	for v := it.Next(); v != nil; v = it.Next() {
		ps = append(ps, v.(*messages.Pickle))
	}

	return
}

// MustGetPickleStep will retrieve a pickle step and panic on error.
func (s *Storage) MustGetPickleStep(id string) *messages.PickleStep {
	v := s.mustFirst(tablePickleStep, tablePickleStepIndexID, id)
	return v.(*messages.PickleStep)
}

// MustInsertTestRunStarted will set the test run started event and panic on error.
func (s *Storage) MustInsertTestRunStarted(trs models.TestRunStarted) {
	s.testRunStartedLock.Lock()
	defer s.testRunStartedLock.Unlock()

	s.testRunStarted = trs
}

// MustGetTestRunStarted will retrieve the test run started event and panic on error.
func (s *Storage) MustGetTestRunStarted() models.TestRunStarted {
	s.testRunStartedLock.Lock()
	defer s.testRunStartedLock.Unlock()

	return s.testRunStarted
}

// MustInsertPickleResult will instert a pickle result and panic on error.
func (s *Storage) MustInsertPickleResult(pr models.PickleResult) {
	s.mustInsert(tablePickleResult, pr)
}

// MustInsertPickleStepResult will insert a pickle step result and panic on error.
func (s *Storage) MustInsertPickleStepResult(psr models.PickleStepResult) {
	s.mustInsert(tablePickleStepResult, psr)
}

// MustGetPickleResult will retrieve a pickle result by id and panic on error.
func (s *Storage) MustGetPickleResult(id string) models.PickleResult {
	v := s.mustFirst(tablePickleResult, tablePickleResultIndexPickleID, id)
	return v.(models.PickleResult)
}

// MustGetPickleResults will retrieve all pickle results and panic on error.
func (s *Storage) MustGetPickleResults() (prs []models.PickleResult) {
	it := s.mustGet(tablePickleResult, tablePickleResultIndexPickleID)
	for v := it.Next(); v != nil; v = it.Next() {
		prs = append(prs, v.(models.PickleResult))
	}

	return prs
}

// MustGetPickleStepResult will retrieve a pickle strep result by id and panic on error.
func (s *Storage) MustGetPickleStepResult(id string) models.PickleStepResult {
	v := s.mustFirst(tablePickleStepResult, tablePickleStepResultIndexPickleStepID, id)
	return v.(models.PickleStepResult)
}

// MustGetPickleStepResultsByPickleID will retrieve pickle step results by pickle id and panic on error.
func (s *Storage) MustGetPickleStepResultsByPickleID(pickleID string) (psrs []models.PickleStepResult) {
	it := s.mustGet(tablePickleStepResult, tablePickleStepResultIndexPickleID, pickleID)
	for v := it.Next(); v != nil; v = it.Next() {
		psrs = append(psrs, v.(models.PickleStepResult))
	}

	return psrs
}

// MustGetPickleStepResultsByPickleIDUntilStep will retrieve pickle step results by pickle id
// from 0..stepID for that pickle.
func (s *Storage) MustGetPickleStepResultsByPickleIDUntilStep(pickleID string, untilStepID string) (psrs []models.PickleStepResult) {
	it := s.mustGet(tablePickleStepResult, tablePickleStepResultIndexPickleID, pickleID)
	for v := it.Next(); v != nil; v = it.Next() {
		psr := v.(models.PickleStepResult)
		psrs = append(psrs, psr)
		if psr.PickleStepID == untilStepID {
			break
		}
	}

	return psrs
}

// MustGetPickleStepResultsByStatus will retrieve pickle strep results by status and panic on error.
func (s *Storage) MustGetPickleStepResultsByStatus(status models.StepResultStatus) (psrs []models.PickleStepResult) {
	it := s.mustGet(tablePickleStepResult, tablePickleStepResultIndexStatus, status)
	for v := it.Next(); v != nil; v = it.Next() {
		psrs = append(psrs, v.(models.PickleStepResult))
	}

	return psrs
}

// MustInsertFeature will insert a feature and panic on error.
func (s *Storage) MustInsertFeature(f *models.Feature) {
	s.mustInsert(tableFeature, f)
}

// MustGetFeature will retrieve a feature by URI and panic on error.
func (s *Storage) MustGetFeature(uri string) *models.Feature {
	v := s.mustFirst(tableFeature, tableFeatureIndexURI, uri)
	return v.(*models.Feature)
}

// MustGetFeatures will retrieve all features by and panic on error.
func (s *Storage) MustGetFeatures() (fs []*models.Feature) {
	it := s.mustGet(tableFeature, tableFeatureIndexURI)
	for v := it.Next(); v != nil; v = it.Next() {
		fs = append(fs, v.(*models.Feature))
	}

	return
}

type stepDefinitionMatch struct {
	StepID         string
	StepDefinition *models.StepDefinition
}

// MustInsertStepDefintionMatch will insert the matched StepDefintion for the step ID and panic on error.
func (s *Storage) MustInsertStepDefintionMatch(stepID string, match *models.StepDefinition) {
	d := stepDefinitionMatch{
		StepID:         stepID,
		StepDefinition: match,
	}

	s.mustInsert(tableStepDefintionMatch, d)
}

// MustGetStepDefintionMatch will retrieve the matched StepDefintion for the step ID and panic on error.
func (s *Storage) MustGetStepDefintionMatch(stepID string) *models.StepDefinition {
	v := s.mustFirst(tableStepDefintionMatch, tableStepDefintionMatchIndexStepID, stepID)
	return v.(stepDefinitionMatch).StepDefinition
}

func (s *Storage) mustInsert(table string, obj interface{}) {
	txn := s.db.Txn(writeMode)

	if err := txn.Insert(table, obj); err != nil {
		panic(err)
	}

	txn.Commit()
}

func (s *Storage) mustFirst(table, index string, args ...interface{}) interface{} {
	txn := s.db.Txn(readMode)
	defer txn.Abort()

	v, err := txn.First(table, index, args...)
	if err != nil {
		panic(err)
	} else if v == nil {
		err = fmt.Errorf("couldn't find index: %q in table: %q with args: %+v", index, table, args)
		panic(err)
	}

	return v
}

func (s *Storage) mustGet(table, index string, args ...interface{}) memdb.ResultIterator {
	txn := s.db.Txn(readMode)
	defer txn.Abort()

	it, err := txn.Get(table, index, args...)
	if err != nil {
		panic(err)
	}

	return it
}
```

## File: `internal/vault/storage_test.go`
```go
package storage_test

import (
	"testing"
	"time"

	messages "github.com/cucumber/messages/go/v21"
	"github.com/stretchr/testify/assert"

	"github.com/cucumber/godog/internal/models"
	"github.com/cucumber/godog/internal/storage"
	"github.com/cucumber/godog/internal/testutils"
)

func Test_MustGetPickle(t *testing.T) {
	s := storage.NewStorage()
	ft := testutils.BuildTestFeature(t)

	expected := ft.Pickles[0]
	s.MustInsertPickle(expected)

	actual := s.MustGetPickle(expected.Id)
	assert.Equal(t, expected, actual)
}

func Test_MustGetPickles(t *testing.T) {
	s := storage.NewStorage()
	ft := testutils.BuildTestFeature(t)

	expected := ft.Pickles
	for _, pickle := range expected {
		s.MustInsertPickle(pickle)
	}

	actual := s.MustGetPickles(ft.Uri)
	assert.Equal(t, expected, actual)
}

func Test_MustGetPickleStep(t *testing.T) {
	s := storage.NewStorage()
	ft := testutils.BuildTestFeature(t)

	for _, pickle := range ft.Pickles {
		s.MustInsertPickle(pickle)
	}

	for _, pickle := range ft.Pickles {
		for _, expected := range pickle.Steps {
			actual := s.MustGetPickleStep(expected.Id)
			assert.Equal(t, expected, actual)
		}
	}
}

func Test_MustGetTestRunStarted(t *testing.T) {
	s := storage.NewStorage()

	expected := models.TestRunStarted{StartedAt: time.Now()}
	s.MustInsertTestRunStarted(expected)

	actual := s.MustGetTestRunStarted()
	assert.Equal(t, expected, actual)
}

func Test_MustGetPickleResult(t *testing.T) {
	s := storage.NewStorage()

	const pickleID = "1"
	expected := models.PickleResult{PickleID: pickleID}
	s.MustInsertPickleResult(expected)

	actual := s.MustGetPickleResult(pickleID)
	assert.Equal(t, expected, actual)
}

func Test_MustGetPickleResults(t *testing.T) {
	s := storage.NewStorage()

	expected := []models.PickleResult{{PickleID: "1"}, {PickleID: "2"}}
	for _, pr := range expected {
		s.MustInsertPickleResult(pr)
	}

	actual := s.MustGetPickleResults()
	assert.Equal(t, expected, actual)
}

func Test_MustGetPickleStepResult(t *testing.T) {
	s := storage.NewStorage()

	const pickleID = "1"
	const stepID = "2"

	expected := models.PickleStepResult{
		Status:       models.Passed,
		PickleID:     pickleID,
		PickleStepID: stepID,
	}
	s.MustInsertPickleStepResult(expected)

	actual := s.MustGetPickleStepResult(stepID)
	assert.Equal(t, expected, actual)
}

func Test_MustGetPickleStepResultsByPickleID(t *testing.T) {
	s := storage.NewStorage()

	const pickleID = "p1"

	expected := []models.PickleStepResult{
		{
			Status:       models.Passed,
			PickleID:     pickleID,
			PickleStepID: "s1",
		},
		{
			Status:       models.Passed,
			PickleID:     pickleID,
			PickleStepID: "s2",
		},
	}

	for _, psr := range expected {
		s.MustInsertPickleStepResult(psr)
	}

	actual := s.MustGetPickleStepResultsByPickleID(pickleID)
	assert.Equal(t, expected, actual)
}

func Test_MustGetPickleStepResultsByPickleIDUntilStep(t *testing.T) {
	s := storage.NewStorage()

	const pickleID = "p1"
	const stepID = "s2"

	store := []models.PickleStepResult{
		{
			Status:       models.Passed,
			PickleID:     pickleID,
			PickleStepID: "s1",
		},
		{
			Status:       models.Passed,
			PickleID:     pickleID,
			PickleStepID: "s2",
		},
		{
			Status:       models.Passed,
			PickleID:     pickleID,
			PickleStepID: "s3",
		},
	}

	for _, psr := range store {
		s.MustInsertPickleStepResult(psr)
	}

	expected := store[:2]

	actual := s.MustGetPickleStepResultsByPickleIDUntilStep(pickleID, stepID)
	assert.Equal(t, expected, actual)
}

func Test_MustGetPickleStepResultsByStatus(t *testing.T) {
	s := storage.NewStorage()

	const pickleID = "p1"

	expected := []models.PickleStepResult{
		{
			Status:       models.Passed,
			PickleID:     pickleID,
			PickleStepID: "s1",
		},
	}

	testdata := []models.PickleStepResult{
		expected[0],
		{
			Status:       models.Failed,
			PickleID:     pickleID,
			PickleStepID: "s2",
		},
	}

	for _, psr := range testdata {
		s.MustInsertPickleStepResult(psr)
	}

	actual := s.MustGetPickleStepResultsByStatus(models.Passed)
	assert.Equal(t, expected, actual)
}

func Test_MustGetFeature(t *testing.T) {
	s := storage.NewStorage()

	const uri = "<uri>"

	expected := &models.Feature{GherkinDocument: &messages.GherkinDocument{Uri: uri}}
	s.MustInsertFeature(expected)

	actual := s.MustGetFeature(uri)
	assert.Equal(t, expected, actual)
}

func Test_MustGetFeatures(t *testing.T) {
	s := storage.NewStorage()

	expected := []*models.Feature{
		{GherkinDocument: &messages.GherkinDocument{Uri: "uri1"}},
		{GherkinDocument: &messages.GherkinDocument{Uri: "uri2"}},
	}

	for _, f := range expected {
		s.MustInsertFeature(f)
	}

	actual := s.MustGetFeatures()
	assert.Equal(t, expected, actual)
}

func Test_MustGetStepDefintionMatch(t *testing.T) {
	s := storage.NewStorage()

	const stepID = "<step_id>"

	expected := &models.StepDefinition{}
	s.MustInsertStepDefintionMatch(stepID, expected)

	actual := s.MustGetStepDefintionMatch(stepID)
	assert.Equal(t, expected, actual)
}
```

## File: `internal/tags/tag_filter.go`
```go
package tags

import (
	"strings"

	messages "github.com/cucumber/messages/go/v21"
)

// ApplyTagFilter will apply a filter string on the
// array of pickles and returned the filtered list.
func ApplyTagFilter(filter string, pickles []*messages.Pickle) []*messages.Pickle {
	if filter == "" {
		return pickles
	}

	var result = []*messages.Pickle{}

	for _, pickle := range pickles {
		if match(filter, pickle.Tags) {
			result = append(result, pickle)
		}
	}

	return result
}

// Based on http://behat.readthedocs.org/en/v2.5/guides/6.cli.html#gherkin-filters
func match(filter string, tags []*messages.PickleTag) (ok bool) {
	ok = true

	for _, andTags := range strings.Split(filter, "&&") {
		var okComma bool

		for _, tag := range strings.Split(andTags, ",") {
			tag = strings.TrimSpace(tag)
			tag = strings.Replace(tag, "@", "", -1)

			okComma = contains(tags, tag) || okComma

			if tag[0] == '~' {
				tag = tag[1:]
				okComma = !contains(tags, tag) || okComma
			}
		}

		ok = ok && okComma
	}

	return
}

func contains(tags []*messages.PickleTag, tag string) bool {
	for _, t := range tags {
		tagName := strings.Replace(t.Name, "@", "", -1)

		if tagName == tag {
			return true
		}
	}

	return false
}
```

## File: `internal/tags/tag_filter_test.go`
```go
package tags_test

import (
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/cucumber/godog/internal/tags"
	messages "github.com/cucumber/messages/go/v21"
)

type tag = messages.PickleTag
type pickle = messages.Pickle

type testcase struct {
	filter   string
	expected []*pickle
}

var testdata = []*pickle{p1, p2, p3}
var p1 = &pickle{Id: "one", Tags: []*tag{{Name: "@one"}, {Name: "@wip"}}}
var p2 = &pickle{Id: "two", Tags: []*tag{{Name: "@two"}, {Name: "@wip"}}}
var p3 = &pickle{Id: "three", Tags: []*tag{{Name: "@hree"}, {Name: "@wip"}}}

var testcases = []testcase{
	{filter: "", expected: testdata},

	{filter: "@one", expected: []*pickle{p1}},
	{filter: "~@one", expected: []*pickle{p2, p3}},
	{filter: "one", expected: []*pickle{p1}},
	{filter: " one ", expected: []*pickle{p1}},

	{filter: "@one,@two", expected: []*pickle{p1, p2}},
	{filter: "@one,~@two", expected: []*pickle{p1, p3}},
	{filter: " @one , @two ", expected: []*pickle{p1, p2}},

	{filter: "@one&&@two", expected: []*pickle{}},
	{filter: "@one&&~@two", expected: []*pickle{p1}},
	{filter: "@one&&@wip", expected: []*pickle{p1}},

	{filter: "@one&&@two,@wip", expected: []*pickle{p1}},
}

func Test_ApplyTagFilter(t *testing.T) {
	for _, tc := range testcases {
		t.Run("", func(t *testing.T) {
			actual := tags.ApplyTagFilter(tc.filter, testdata)
			assert.Equal(t, tc.expected, actual)
		})
	}
}
```

## File: `internal/testutils/utils.go`
```go
package testutils

import (
	"strings"
	"testing"

	gherkin "github.com/cucumber/gherkin/go/v26"
	messages "github.com/cucumber/messages/go/v21"
	"github.com/stretchr/testify/require"

	"github.com/cucumber/godog/internal/models"
)

// BuildTestFeature creates a feature for testing purpose.
//
// The created feature includes:
//   - a background
//   - one normal scenario with three steps
//   - one outline scenario with one example and three steps
func BuildTestFeature(t *testing.T) models.Feature {
	newIDFunc := (&messages.Incrementing{}).NewId

	gherkinDocument, err := gherkin.ParseGherkinDocument(strings.NewReader(featureContent), newIDFunc)
	require.NoError(t, err)

	path := t.Name()
	gherkinDocument.Uri = path
	pickles := gherkin.Pickles(*gherkinDocument, path, newIDFunc)

	ft := models.Feature{GherkinDocument: gherkinDocument, Pickles: pickles, Content: []byte(featureContent)}
	require.Len(t, ft.Pickles, 2)

	require.Len(t, ft.Pickles[0].AstNodeIds, 1)
	require.Len(t, ft.Pickles[0].Steps, 3)

	require.Len(t, ft.Pickles[1].AstNodeIds, 2)
	require.Len(t, ft.Pickles[1].Steps, 3)

	return ft
}

const featureContent = `Feature: eat godogs
In order to be happy
As a hungry gopher
I need to be able to eat godogs

Background:
  Given there are <begin> godogs

Scenario: Eat 5 out of 12
  When I eat 5
  Then there should be 7 remaining

Scenario Outline: Eat <dec> out of <beginning>
  When I eat <dec>
  Then there should be <remain> remaining

  Examples:
	| begin | dec | remain |
	| 12    | 5   | 7      |`

// BuildTestFeature creates a feature with rules for testing purpose.
//
// The created feature includes:
//   - a background
//   - one normal scenario with three steps
//   - one outline scenario with one example and three steps
func BuildTestFeatureWithRules(t *testing.T) models.Feature {
	newIDFunc := (&messages.Incrementing{}).NewId

	gherkinDocument, err := gherkin.ParseGherkinDocument(strings.NewReader(featureWithRuleContent), newIDFunc)
	require.NoError(t, err)

	path := t.Name()
	gherkinDocument.Uri = path
	pickles := gherkin.Pickles(*gherkinDocument, path, newIDFunc)

	ft := models.Feature{GherkinDocument: gherkinDocument, Pickles: pickles, Content: []byte(featureWithRuleContent)}
	require.Len(t, ft.Pickles, 2)

	require.Len(t, ft.Pickles[0].AstNodeIds, 1)
	require.Len(t, ft.Pickles[0].Steps, 3)

	require.Len(t, ft.Pickles[1].AstNodeIds, 2)
	require.Len(t, ft.Pickles[1].Steps, 3)

	return ft
}

const featureWithRuleContent = `Feature: eat godogs
In order to be happy
As a hungry gopher
I need to be able to eat godogs

Rule: eating godogs

Background:
  Given there are <begin> godogs

Scenario: Eat 5 out of 12
  When I eat 5
  Then there should be 7 remaining

Scenario Outline: Eat <dec> out of <beginning>
  When I eat <dec>
  Then there should be <remain> remaining

  Examples:
	| begin | dec | remain |
	| 12    | 5   | 7      |`
```

## File: `internal/utils/utils.go`
```go
package utils

import (
	"strings"
	"time"
)

// S repeats a space n times
func S(n int) string {
	if n < 0 {
		n = 1
	}
	return strings.Repeat(" ", n)
}

// TimeNowFunc is a utility function to simply testing
// by allowing TimeNowFunc to be defined to zero time
// to remove the time domain from tests
var TimeNowFunc = func() time.Time {
	return time.Now()
}
```

## File: `release-notes/v0.10.0.md`
```markdown
We are excited to announce the release of godog v0.10.0.

Here follows a summary of Notable Changes, the Non Backward Compatible Changes and Deprecation Notices.
The full change log is available [here](https://github.com/cucumber/godog/blob/master/CHANGELOG.md#v0100).


Notable Changes
---------------

### Context Initializers
The current Suite initializer will be removed and replaced by two new initializers, one for the Test Suite and one for the Scenarios.

The **TestSuiteContext** Initializer will be executed once for the execution of the full TestSuite.
```go
// These are the hooks that can be configured for the TestSuite.
func (ctx *TestSuiteContext) BeforeSuite(fn func())
func (ctx *TestSuiteContext) AfterSuite(fn func())
```

The **ScenarioContext** Initializer will be executed before every Scenario.
```go
// These are the hooks that can be configured for a Scenario.
func (ctx *ScenarioContext) BeforeScenario(fn func(sc *Scenario))
func (ctx *ScenarioContext) AfterScenario(fn func(sc *Scenario, err error))
func (ctx *ScenarioContext) BeforeStep(fn func(st *Step))
func (ctx *ScenarioContext) AfterStep(fn func(st *Step, err error))

// Registers a step definition for a Scenario.
func (ctx *ScenarioContext) Step(expr, stepFunc interface{})
```

### Formatter Concurrency
All builtin formatters now support concurrency.

### Scenario Concurrency
Using the new Initializers, godog will now execute scenarios concurrently instead of features.


Non Backward Compatible Changes
-------------------------------

### Hooks
`BeforeFeature` and `AfterFeature` hooks are now removed since the deprecation in [v0.9.0](./v0.9.0.md).


Deprecation Notices
-------------------

### Run and RunWithOptions
`Run` and `RunWithOptions` are now considered deprecated and will be removed in `v0.11.0`.

`godog.Run(suiteName string, initializer func(*Suite))` will be replaced by:
```go
godog.TestSuite{
	Name: suiteName,
	TestSuiteInitializer: InitializeTestSuite,
	ScenarioInitializer: InitializeScenario,
}.Run()
```

`godog.RunWithOptions(suiteName string, initializer func(*Suite), opts Options)` will be replaced by:
```go
godog.TestSuite{
	Name: suiteName,
	TestSuiteInitializer: InitializeTestSuite,
	ScenarioInitializer: InitializeScenario,
	Options: &opts,
}.Run()
```

### Suite Initializers
The `Suite` is now considered deprecated and will be removed in `v0.11.0`.

Initializers that use `*godog.Suite` like this:
```go
func FeatureContext(s *godog.Suite) {
	s.BeforeSuite(func() { Godogs = 0 })

	s.BeforeScenario(func(*messages.Pickle) {
		Godogs = 0 // clean the state before every scenario
	})

	s.Step(`^there are (\d+) godogs$`, thereAreGodogs)
	s.Step(`^I eat (\d+)$`, iEat)
	s.Step(`^there should be (\d+) remaining$`, thereShouldBeRemaining)
}
```

will be replaced by:
```go
func InitializeTestSuite(ctx *godog.TestSuiteContext) {
	ctx.BeforeSuite(func() { Godogs = 0 })
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.BeforeScenario(func(*godog.Scenario) {
		Godogs = 0 // clean the state before every scenario
	})

	ctx.Step(`^there are (\d+) godogs$`, thereAreGodogs)
	ctx.Step(`^I eat (\d+)$`, iEat)
	ctx.Step(`^there should be (\d+) remaining$`, thereShouldBeRemaining)
}
```

### SuiteContext
The `SuiteContext` is now considered deprecated and will be removed in `v0.11.0`.

### Concurrency Formatter
The `ConcurrencyFormatter` interface is now considered deprecated and will be removed in `v0.11.0`.

Full change log
---------------

See [CHANGELOG.md](https://github.com/cucumber/godog/blob/master/CHANGELOG.md#v0100).
```

## File: `release-notes/v0.11.0.md`
```markdown
We are excited to announce the release of godog v0.11.0.

Here follows a summary of Notable Changes, the Non Backward Compatible Changes and Deprecation Notices.
The full change log is available [here](https://github.com/cucumber/godog/blob/master/CHANGELOG.md#v0110-rc1).


Notable Changes
---------------

### Write test report to file
godog is now able to write the report to a file.

- `--format cucumber` will continue to write the report to `stdout`

- `--format cucumber:report.json` will instead write the report to a file named `report.json`

**Note**, godog still only support the use of one formatter.

### Executing godog from the Command Line
godog is now using [Cobra](https://pkg.go.dev/github.com/spf13/cobra) to run godog from the command line. With this update, godog has received sub-commands: (build, help, run, version)

To run tests with godog, `godog [<feature>]` has been replaced with `godog run [<feature>]`.

To build a test binary, `godog --output g.test [<feature>]`has been replaced with `godog build --output g.test [<feature>]`.

### Upload artifacts to the github release
The releases on github now include prebuilt binaries for:
- Linux for amd64 and arm64
- macOs (Darwin) for amd64

### Restructure of the codebase with internal packages
A lot of the internal code that used to be in the main godog package has been moved to internal packages.

The reason for this is mainly for decoupling to allow for simpler tests and to make the codebase easier to work with in general.

### Added official support for go1.15 and removed support for go1.12 
With the introduction of go1.15, go1.15 is now officially supported and go1.12 has been removed, this is since godog supports the 3 latest versions of golang.

Non Backward Compatible Changes
-------------------------------

### Concurrency Formatter
`ConcurrencyFormatter` is now removed since the deprecation in [v0.10.0](./v0.10.0.md).

### Run and RunWithOptions
`Run` and `RunWithOptions` are now removed since the deprecation in [v0.10.0](./v0.10.0.md).

### Suite and SuiteContext
`Suite` and `SuiteContext` are now removed since the deprecation in [v0.10.0](./v0.10.0.md).

Deprecation Notices
-------------------

### BindFlags
`BindFlags(prefix, flag.CommandLine, &opts)` has been replaced by `BindCommandLineFlags(prefix, &opts)` and will be removed in `v0.12.0`.

Using `BindCommandLineFlags(prefix, &opts)` also requires you to use `"github.com/spf13/pflag"` to parse the flags.
```go
package main

import (
	"fmt"
	"os"
	"testing"

	"github.com/cucumber/godog"
	"github.com/cucumber/godog/colors"
	"github.com/spf13/pflag"
)

var opts = godog.Options{Output: colors.Colored(os.Stdout)}

func init() {
	godog.BindCommandLineFlags("godog.", &opts)
}

func TestMain(m *testing.M) {
	pflag.Parse()
	opts.Paths = pflag.Args()
  
  // ...
```

### Executing the godog CLI
godog has received sub-commands: (build, help, run, version)

To run tests with godog, `godog [<feature>]` has been replaced with `godog run [<feature>]`.

To build a test binary, `godog --output g.test [<feature>]`has been replaced with `godog build --output g.test [<feature>]`.

Full change log
---------------

See [CHANGELOG.md](https://github.com/cucumber/godog/blob/master/CHANGELOG.md#v0110-rc1).
```

## File: `release-notes/v0.12.0.md`
```markdown
We are excited to announce the release of godog v0.12.0.

Here follows a summary of Notable Changes, the Non Backward Compatible Changes and Deprecation Notices. The full change
log is available [here](https://github.com/cucumber/godog/blob/master/CHANGELOG.md).


Notable Changes
---------------

### Output with multiple formatters

Now `godog` is able to use multiple formatters simultaneously with comma-separated formatters.

`--format pretty,junit:report.xml,cucumber:report.json` will write `pretty` format to stdout, `junit` to report.xml
and `cucumber` to report.json.

### Extensible formatters

Standard formatters are now exported with type aliases so that a custom formatter can be built on top of it.
Please check [an example](../_examples/custom-formatter).

### Contextualized hooks

Scenario and Step hooks are now passing context to allow custom state communication. Returned context should generally
be based or equal to received context. Context is also passed to steps that have it in declaration and is read from
steps that return it.

Hooks can now return error, if non nil error is returned test is failed. This enables additional flow control, for
example to check expectations after the scenario.

Scenario hooks are now named `Before` and `After`.

```go
// BeforeScenarioHook defines a hook before scenario.
type BeforeScenarioHook func (ctx context.Context, sc *Scenario) (context.Context, error)

// AfterScenarioHook defines a hook after scenario.
type AfterScenarioHook func (ctx context.Context, sc *Scenario, err error) (context.Context, error)
```

Step hooks are now also named `Before` and `After`, but they are available with `ScenarioContext.StepContext()`.

```go
// BeforeStepHook defines a hook before step.
type BeforeStepHook func (ctx context.Context, st *Step) (context.Context, error)

// AfterStepHook defines a hook after step.
type AfterStepHook func (ctx context.Context, st *Step, status StepResultStatus, err error) (context.Context, error)
```

### Step definition improvements

Now `godog` can use additional ways to declare step definition. These declarations are optional and do not break
backwards compatibility.

Error result may be omitted if the step does not fail.

```go
func iEat(arg1 int) {
    // Eat arg1.
}
```

You can have `context.Context` as first argument, test runner will pass current context to the step.

```go
func iEat(ctx context.Context, arg1 int) {
    if v, ok := ctx.Value(eatKey{}).int; ok {
        // Eat v from context.
    }
    // Eat arg1.
}
```

You can have `context.Context` in return, test runner will use returned context to pass to next hooks and steps.

```go
func iEat(ctx context.Context, arg1 int) context.Context {
    if v, ok := ctx.Value(eatKey{}).int; ok {
        // Eat v from context.
    }
    // Eat arg1.
    
    return context.WithValue(ctx, eatKey{}, 0)
}
```

If error is also needed in return, context have to be first.

```go
func iEat(ctx context.Context, arg1 int) (context.Context, error) {
    if v, ok := ctx.Value(eatKey{}).int; ok {
        // Eat v from context.
    }
    // Eat arg1.

    if arg1 == 0 {
        return errors.New("can't eat nothing")
    }
    
    return context.WithValue(ctx, eatKey{}, 0), nil
}
```

You can now use `string` instead of `*godog.DocString` in declaration.

### Getting features of test suite

`godog.TestSuite` now can `RetrieveFeatures() ([]*models.Feature, error)` to expose parsed features to the user.

### Added official support for go1.16 and go1.17

With the introduction of go1.17, go1.17 and go1.16 are now officially supported.

### Running scenarios as subtests of *testing.T

You can now assign an instance of `*testing.T` to `godog.Options.TestingT` so that scenarios will be invoked with 
`t.Run` allowing granular control with standard Go tools. 

[More info](https://github.com/cucumber/godog#running-godog-with-go-test).

Non Backward Compatible Changes
-------------------------------

### Messages library updated

Messages library is changed from `github.com/cucumber/messages-go/v10` to `github.com/cucumber/messages-go/v16`.

Deprecation Notices
-------------------

### Hooks

Scenario and step hooks were upgraded with new API to support context and errors, previous methods are now deprecated.

- `ScenarioContext.BeforeScenario`, use `ScenarioContext.Before`
- `ScenarioContext.AfterScenario`, use `ScenarioContext.After`
- `ScenarioContext.BeforeStep`, use `ScenarioContext.StepContext().Before`
- `ScenarioContext.AfterStep`, use `ScenarioContext.StepContext().After`

Full change log
---------------

See [CHANGELOG.md](https://github.com/cucumber/godog/blob/master/CHANGELOG.md).
```

## File: `release-notes/v0.9.0.md`
```markdown
We are excited to announce the release of godog v0.9.0.

Here follows a summary of Notable Changes, the Non Backward Compatible Changes and Deprecation Notices.
The full change log is available [here](https://github.com/cucumber/godog/blob/master/CHANGELOG.md#090).


Notable Changes
---------------

Most importantly, note that the gherkin core is changed to [gherkin-go](https://github.com/cucumber/gherkin-go/releases/tag/v9.2.0).



Non Backward Compatible Changes
-------------------------------

### Install godog
With the change of dependencies for godog, which relies on `go modules`, installing godog now requires go modules to be active.

If you are running `within the $GOPATH`, you would need to install godog like this:
`GO111MODULE=on go get github.com/cucumber/godog/cmd/godog@v0.9.0`
- Adding `GO111MODULE=on` will allow go get and go mod to work together as intended.
- Adding `@v0.9.0` will install v0.9.0 specifically instead of master.

If you are running `outside of the $GOPATH`, you should still specify a version.

I you encounter this error, please try adding `GO111MODULE=on`:
```
/go# go get github.com/cucumber/godog/cmd/godog
package github.com/cucumber/gherkin-go/v19: cannot find package "github.com/cucumber/gherkin-go/v19" in any of:
	/usr/local/go/src/github.com/cucumber/gherkin-go/v19 (from $GOROOT)
	/go/src/github.com/cucumber/gherkin-go/v19 (from $GOPATH)
package github.com/cucumber/messages-go/v10: cannot find package "github.com/cucumber/messages-go/v10" in any of:
	/usr/local/go/src/github.com/cucumber/messages-go/v10 (from $GOROOT)
	/go/src/github.com/cucumber/messages-go/v10 (from $GOPATH)
```


### Gherkin Core
The following types have been switched for [messages-go](https://github.com/cucumber/messages-go).

|           old           |                     new                     |
| ----------------------- | ------------------------------------------- |
| gherkin.Feature         | messages.GherkinDocument                    |
| gherkin.Scenario        | messages.Pickle                             |
| gherkin.ScenarioOutline | messages.Pickle                             |
| gherkin.Step            | messages.Pickle_PickleStep                  |
| gherkin.DocString       | messages.PickleStepArgument_PickleDocString |
| gherkin.DataTable       | messages.PickleStepArgument_PickleTable     |


### Step Defintions
- `StepDef` has been renamed to `StepDefinition`
- Steps that earlier accepted `*gherkin.DocString` or `*gherkin.DataTable` needs to be updated to use `*messages.PickleStepArgument_PickleDocString` resp. `*messages.PickleStepArgument_PickleTable`.
[Example](https://github.com/cucumber/godog/pull/240/files#diff-a5f59d298843b731ff8d2f9c670303ff).


### Hooks
The updated hooks can be found [here](https://github.com/cucumber/godog/blob/b62eb13ee70c9f0f732b694b39bde9670051bac7/suite.go#L251).
- `BeforeFeature` and `AfterFeature` hooks now accept `*messages.GherkinDocument` instead of `*gherkin.Feature`
- `BeforeScenario` and `AfterScenario` hooks now accept `*messages.Pickle` instead of `interface{}`
- `BeforeStep` and `AfterStep` hooks now accept `*messages.Pickle_PickleStep` instead `*gherkin.Step`


### Formatter
The formatter interface have recieved some updates, the updated version can be found [here](https://github.com/cucumber/godog/blob/b62eb13ee70c9f0f732b694b39bde9670051bac7/fmt.go#L100).

- `Feature` now accepts `*messages.GherkinDocument` instead of `*gherkin.Feature`
- `Node` has been renamed to `Pickle` and now accepts `*messages.Pickle` instead of `interface{}`
- `Defined`, `Failed`, `Passed`, `Skipped`, `Undefined`, `Pending` now takes `*messages.Pickle` as the first argument and `*gherkin.Step, *StepDef` have been updated to `*messages.Pickle_PickleStep, *StepDefinition`



Deprecation Notices
-------------------

### Hooks
- `BeforeFeature` and `AfterFeature` hooks are now considered deprecated and will be removed in `v0.10.0`.


Full change log
---------------

See [CHANGELOG.md](https://github.com/cucumber/godog/blob/master/CHANGELOG.md#090).

```

