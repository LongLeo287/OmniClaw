---
id: shopspring-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.303053
---

# KNOWLEDGE EXTRACT: shopspring
> **Extracted on:** 2026-03-30 17:53:20
> **Source:** shopspring

---

## File: `decimal.md`
```markdown
# 📦 shopspring/decimal [🔖 PENDING/APPROVE]
🔗 https://github.com/shopspring/decimal


## Meta
- **Stars:** ⭐ 7285 | **Forks:** 🍴 650
- **Language:** Go | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Arbitrary-precision fixed-point decimal numbers in Go

## README (trích đầu)
```
# decimal

[![ci](https://github.com/shopspring/decimal/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/shopspring/decimal/actions/workflows/ci.yml)
[![GoDoc](https://godoc.org/github.com/shopspring/decimal?status.svg)](https://godoc.org/github.com/shopspring/decimal) 
[![Go Report Card](https://goreportcard.com/badge/github.com/shopspring/decimal)](https://goreportcard.com/report/github.com/shopspring/decimal)

Arbitrary-precision fixed-point decimal numbers in go.

_Note:_ Decimal library can "only" represent numbers with a maximum of 2^31 digits after the decimal point.

## Features

 * The zero-value is 0, and is safe to use without initialization
 * Addition, subtraction, multiplication with no loss of precision
 * Division with specified precision
 * Database/sql serialization/deserialization
 * JSON and XML serialization/deserialization

## Install

Run `go get github.com/shopspring/decimal`

## Requirements 

Decimal library requires Go version `>=1.10`

## Documentation

http://godoc.org/github.com/shopspring/decimal


## Usage

```go
package main

import (
	"fmt"
	"github.com/shopspring/decimal"
)

func main() {
	price, err := decimal.NewFromString("136.02")
	if err != nil {
		panic(err)
	}

	quantity := decimal.NewFromInt(3)

	fee, _ := decimal.NewFromString(".035")
	taxRate, _ := decimal.NewFromString(".08875")

	subtotal := price.Mul(quantity)

	preTax := subtotal.Mul(fee.Add(decimal.NewFromFloat(1)))

	total := preTax.Mul(taxRate.Add(decimal.NewFromFloat(1)))

	fmt.Println("Subtotal:", subtotal)                      // Subtotal: 408.06
	fmt.Println("Pre-tax:", preTax)                         // Pre-tax: 422.3421
	fmt.Println("Taxes:", total.Sub(preTax))                // Taxes: 37.482861375
	fmt.Println("Total:", total)                            // Total: 459.824961375
	fmt.Println("Tax rate:", total.Sub(preTax).Div(preTax)) // Tax rate: 0.08875
}
```

## Alternative libraries

When working with decimal numbers, you might face problems this library is not perfectly suited for. 
Fortunately, thanks to the wonderful community we have a dozen other libraries that you can choose from.  
Explore other alternatives to find the one that best fits your needs :)  

* [cockroachdb/apd](https://github.com/cockroachdb/apd) - arbitrary precision, mutable and rich API similar to `big.Int`, more performant than this library 
* [alpacahq/alpacadecimal](https://github.com/alpacahq/alpacadecimal) - high performance, low precision (12 digits), fully compatible API with this library 
* [govalues/decimal](https://github.com/govalues/decimal) - high performance, zero-allocation, low precision (19 digits)
* [greatcloak/decimal](https://github.com/greatcloak/decimal) - fork focusing on billing and e-commerce web application related use cases, includes out-of-the-box BSON marshaling support

## FAQ

#### Why don't you just use float64?

Because float64 (or any binary floating point type, actually) can't represent
numbers such as `0.1`
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

