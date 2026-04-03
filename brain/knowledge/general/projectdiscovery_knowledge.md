---
id: projectdiscovery-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:02.176687
---

# KNOWLEDGE EXTRACT: projectdiscovery
> **Extracted on:** 2026-03-30 17:51:10
> **Source:** projectdiscovery

---

## File: `dsl.md`
```markdown
# 📦 projectdiscovery/dsl [🔖 PENDING/APPROVE]
🔗 https://github.com/projectdiscovery/dsl


## Meta
- **Stars:** ⭐ 117 | **Forks:** 🍴 31
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
DSL engine

## README (trích đầu)
```
# DSL
DSL ease the creation of expressions by providing a set of built-in helper functions.

### What is DSL?
DSL is a library that allows to create and evaluate expressions. You can define expressions to compare, filter, or transform data, and then evaluate them against a set of data.

### Example
```go
package main

import (
	"fmt"
	"github.com/Knetic/govaluate"
	"github.com/projectdiscovery/dsl"
)

func main() {
	// Define the data to evaluate
	data := map[string]interface{}{
		"username": "johndoe",
		"email":    "johndoe@example.com",
		"password": "12345",
		"ip":       "127.0.0.1",
		"url":      "https://www.example.com",
		"date":     "2022-05-01",
	}

	// Define the expressions to evaluate
	expressions := map[string]string{
		"username_and_email_matcher": "contains(username, 'john') && contains(email, 'example.com')",
		"password_criteria":          "contains_any(password, '0123456789') && regex_any(password, '[A-Z]')",
		"sha256_username_matcher":    "sha256(username) == 'a0d95c8b32fa9b05a7d790a08e221c384b317ca05f66a7b84978d22c9838bb2a'",
		"ip_format_matcher":        "ip_format(ip, '1') == '127.0.0.1'",
		"url_valid_matcher":       "startswith(url, 'http') && contains(url, '://') && contains(url, '.') && !contains_any(url, ':@')",
	}

	for matcherName, expression := range expressions {
		compiledExpression, err := govaluate.NewEvaluableExpressionWithFunctions(expression, dsl.DefaultHelperFunctions)
		if err != nil {
			fmt.Printf("Failed to compile expresion: %v\n", expression)
		}

		result, err := compiledExpression.Evaluate(data)
		if err != nil {
			fmt.Printf("Failed to evaluate expresion: %v\n", expression)
		}

		if result == true {
			fmt.Printf("[%v] matches data\n", matcherName)
		} else {
			fmt.Printf("[%v] not matches data\n", matcherName)
		}
	}
}


```

### Default Helper functions list

| Helper function                                                       | Description                                                                                                         | Example                                                                                                                                              | Output                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `katana.md`
```markdown
# 📦 projectdiscovery/katana [🔖 PENDING/APPROVE]
🔗 https://github.com/projectdiscovery/katana


## Meta
- **Stars:** ⭐ 16326 | **Forks:** 🍴 1065
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A next-generation crawling and spidering framework.

## README (trích đầu)
```
<h1 align="center">
  <img src="https://user-images.githubusercontent.com/8293321/196779266-421c79d4-643a-4f73-9b54-3da379bbac09.png" alt="katana" width="200px">
  <br>
</h1>

<h4 align="center">A next-generation crawling and spidering framework</h4>

<p align="center">
<a href="https://goreportcard.com/report/github.com/projectdiscovery/katana"><img src="https://goreportcard.com/badge/github.com/projectdiscovery/katana"></a>
<a href="https://github.com/projectdiscovery/katana/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/projectdiscovery/katana/releases"><img src="https://img.shields.io/github/release/projectdiscovery/katana"></a>
<a href="https://twitter.com/pdiscoveryio"><img src="https://img.shields.io/twitter/follow/pdiscoveryio.svg?logo=twitter"></a>
<a href="https://discord.gg/projectdiscovery"><img src="https://img.shields.io/discord/695645237418131507.svg?logo=discord"></a>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#scope-control">Scope</a> •
  <a href="#crawler-configuration">Config</a> •
  <a href="#filters">Filters</a> •
  <a href="https://discord.gg/projectdiscovery">Join Discord</a>
</p>


# Features

![image](https://user-images.githubusercontent.com/8293321/199371558-daba03b6-bf9c-4883-8506-76497c6c3a44.png)

 - Fast And fully configurable web crawling
 - **Standard** and **Headless** mode
 - **JavaScript** parsing / crawling
 - Customizable **automatic form filling**
 - **Scope control** - Preconfigured field / Regex 
 - **Customizable output** - Preconfigured fields
 - INPUT - **STDIN**, **URL** and **LIST**
 - OUTPUT - **STDOUT**, **FILE** and **JSON**


## Installation

katana requires Go 1.25+ to install successfully. If you encounter any installation issues, we recommend trying with the latest available version of Go, as the minimum required version may have changed. Run the command below or download a pre-compiled binary from the [release page](https://github.com/projectdiscovery/katana/releases).

```console
CGO_ENABLED=1 go install github.com/projectdiscovery/katana/cmd/katana@latest
```

**More options to install / run katana-**

<details>
  <summary>Docker</summary>

> To install / update docker to latest tag -

```sh
docker pull projectdiscovery/katana:latest
```

> To run katana in standard mode using docker -


```sh
docker run projectdiscovery/katana:latest -u https://tesla.com
```

> To run katana in headless mode using docker -

```sh
docker run projectdiscovery/katana:latest -u https://tesla.com -system-chrome -headless
```

</details>

<details>
  <summary>Ubuntu</summary>

> It's recommended to install the following prerequisites -

```sh
sudo apt update
sudo snap refresh
sudo apt install zip curl wget git
sudo snap install golang --classic
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key ad
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `nuclei.md`
```markdown
# 📦 projectdiscovery/nuclei [🔖 PENDING/APPROVE]
🔗 https://github.com/projectdiscovery/nuclei
🌐 https://docs.projectdiscovery.io/tools/nuclei

## Meta
- **Stars:** ⭐ 27631 | **Forks:** 🍴 3323
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Nuclei is a fast, customizable vulnerability scanner powered by the global security community and built on a simple YAML-based DSL, enabling collaboration to tackle trending vulnerabilities on the internet. It helps you find vulnerabilities in your applications, APIs, networks, DNS, and cloud configurations.

## README (trích đầu)
```
![nuclei](/static/nuclei-cover-image.png)

<div align="center">
  
  <a href="https://github.com/projectdiscovery/nuclei/blob/main/README.md">`English`</a> •
  <a href="https://github.com/projectdiscovery/nuclei/blob/main/README_CN.md">`中文`</a> •
  <a href="https://github.com/projectdiscovery/nuclei/blob/main/README_KR.md">`Korean`</a> •
  <a href="https://github.com/projectdiscovery/nuclei/blob/main/README_ID.md">`Indonesia`</a> •
  <a href="https://github.com/projectdiscovery/nuclei/blob/main/README_ES.md">`Spanish`</a> •
  <a href="https://github.com/projectdiscovery/nuclei/blob/main/README_JP.md">`日本語`</a> •
  <a href="https://github.com/projectdiscovery/nuclei/blob/main/README_PT-BR.md">`Portuguese`</a> •
  <a href="https://github.com/projectdiscovery/nuclei/blob/main/README_TR.md">`Türkçe`</a>
  
</div>

<p align="center">

<a href="https://docs.projectdiscovery.io/tools/nuclei/overview?utm_source=github&utm_medium=web&utm_campaign=nuclei_readme"><img src="https://img.shields.io/badge/Documentation-%23000000.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1ib29rLW9wZW4iPjxwYXRoIGQ9Ik0xMiA3djE0Ii8+PHBhdGggZD0iTTMgMThhMSAxIDAgMCAxLTEtMVY0YTEgMSAwIDAgMSAxLTFoNWE0IDQgMCAwIDEgNCA0IDQgNCAwIDAgMSA0LTRoNWExIDEgMCAwIDEgMSAxdjEzYTEgMSAwIDAgMS0xIDFoLTZhMyAzIDAgMCAwLTMgMyAzIDMgMCAwIDAtMy0zeiIvPjwvc3ZnPg==&logoColor=white"></a>
&nbsp;&nbsp;
<a href="https://github.com/projectdiscovery/nuclei-templates"><img src="https://img.shields.io/badge/Templates Library-%23000000.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLXNoaWVsZCI+PHBhdGggZD0iTTIwIDEzYzAgNS0zLjUgNy41LTcuNjYgOC45NWExIDEgMCAwIDEtLjY3LS4wMUM3LjUgMjAuNSA0IDE4IDQgMTNWNmExIDEgMCAwIDEgMS0xYzIgMCA0LjUtMS4yIDYuMjQtMi43MmExLjE3IDEuMTcgMCAwIDEgMS41MiAwQzE0LjUxIDMuODEgMTcgNSAxOSA1YTEgMSAwIDAgMSAxIDF6Ii8+PC9zdmc+&logoColor=white"></a>
&nbsp;&nbsp;
<a href="https://discord.gg/projectdiscovery?utm_source=github&utm_medium=web&utm_campaign=nuclei_readme"><img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white"></a>

<hr>

</p>

<br>

**Nuclei is a modern, high-performance vulnerability scanner that leverages simple YAML-based templates. It empowers you to design custom vulnerability detection scenarios that mimic real-world conditions, leading to zero false positives.**

- Simple YAML format for creating and customizing vulnerability templates.
- Contributed by thousands of security professionals to tackle trending vulnerab
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

