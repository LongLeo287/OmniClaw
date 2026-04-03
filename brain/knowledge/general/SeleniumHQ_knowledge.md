---
id: seleniumhq-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:11.416859
---

# KNOWLEDGE EXTRACT: SeleniumHQ
> **Extracted on:** 2026-03-30 17:53:11
> **Source:** SeleniumHQ

---

## File: `selenium.md`
```markdown
# 📦 SeleniumHQ/selenium [🔖 PENDING/APPROVE]
🔗 https://github.com/SeleniumHQ/selenium
🌐 https://selenium.dev

## Meta
- **Stars:** ⭐ 34183 | **Forks:** 🍴 8667
- **Language:** Java | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A browser automation framework and ecosystem.

## README (trích đầu)
```
<h1 align="center">
  <br/>
  <a href="https://selenium.dev"><img src="common/images/selenium_logo_mark_green.svg" alt="Selenium" width="100"></a>
  <br/>
  Selenium
  <br/>
</h1>

<h3 align="center">Automates browsers. That's it!</h3>

<p align="center">
  <a href="#contributing">Contributing</a> •
  <a href="#installing">Installing</a> •
  <a href="#building">Building</a> •
  <a href="#developing">Developing</a> •
  <a href="#testing">Testing</a> •
  <a href="#documenting">Documenting</a> •
  <a href="#releasing">Releasing</a>
</p>

<br>

Selenium is an umbrella project encapsulating a variety of tools and
libraries enabling web browser automation. Selenium specifically
provides an infrastructure for the [W3C WebDriver specification](https://w3c.github.io/webdriver/)
— a platform and language-neutral coding interface compatible with all
major web browsers.

The project is made possible by volunteer contributors who've
generously donated thousands of hours in code development and upkeep.

This README is for developers interested in contributing to the project.
For people looking to get started using Selenium, please check out
our [User Manual](https://selenium.dev/documentation/) for detailed examples and descriptions, and if you
get stuck, there are several ways to [Get Help](https://www.selenium.dev/support/).

[![CI](https://github.com/SeleniumHQ/selenium/actions/workflows/ci.yml/badge.svg)](https://github.com/SeleniumHQ/selenium/actions/workflows/ci.yml)
[![CI - RBE](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-rbe.yml/badge.svg)](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-rbe.yml)
[![Releases downloads](https://img.shields.io/github/downloads/SeleniumHQ/selenium/total.svg)](https://github.com/SeleniumHQ/selenium/releases)

## Contributing

Please read [CONTRIBUTING.md](https://github.com/SeleniumHQ/selenium/blob/trunk/CONTRIBUTING.md)
before submitting your pull requests.

## Installing

These are the requirements to create your own local dev environment to contribute to Selenium.

### All Platforms

* [Bazelisk](https://github.com/bazelbuild/bazelisk), a Bazel wrapper that automatically downloads
  the version of Bazel specified in `.bazelversion` file and transparently passes through all
  command-line arguments to the real Bazel binary.
* Java JDK version 17 or greater (e.g., [Java 17 Temurin](https://adoptium.net/temurin/releases/?version=17))
  * Set `JAVA_HOME` environment variable to location of Java executable (the JDK not the JRE)
  * To test this, try running the command `javac`. This command won't exist if you only have the JRE
  installed. If you're met with a list of command-line options, you're referencing the JDK properly.

### MacOS

  * Xcode including the command-line tools. Install the latest version using: `xcode-select --install`
  * Rosetta for Apple Silicon Macs. Add `build --host_platform=//:rosetta` to the `.bazelrc.local` file. We are working
  to make sure this isn't required in the
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

