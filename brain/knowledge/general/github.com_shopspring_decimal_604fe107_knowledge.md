---
id: github.com-shopspring-decimal-604fe107-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:21.867294
---

# KNOWLEDGE EXTRACT: github.com_shopspring_decimal_604fe107
> **Extracted on:** 2026-04-01 08:37:08
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519652/github.com_shopspring_decimal_604fe107

---

## File: `.gitignore`
```
.git
*.swp

# IntelliJ
.idea/
*.iml

# VS code
*.code-workspace
.vscode/

mise.toml
```

## File: `CHANGELOG.md`
```markdown
## Decimal v1.4.0
#### BREAKING
- Drop support for Go version older than 1.10 [#361](https://github.com/shopspring/decimal/pull/361)

#### FEATURES
- Add implementation of natural logarithm [#339](https://github.com/shopspring/decimal/pull/339) [#357](https://github.com/shopspring/decimal/pull/357)
- Add improved implementation of power operation [#358](https://github.com/shopspring/decimal/pull/358)
- Add Compare method which forwards calls to Cmp [#346](https://github.com/shopspring/decimal/pull/346)
- Add NewFromBigRat constructor [#288](https://github.com/shopspring/decimal/pull/288)
- Add NewFromUint64 constructor [#352](https://github.com/shopspring/decimal/pull/352)

#### ENHANCEMENTS
- Migrate to Github Actions [#245](https://github.com/shopspring/decimal/pull/245) [#340](https://github.com/shopspring/decimal/pull/340)
- Fix examples for RoundDown, RoundFloor, RoundUp, and RoundCeil [#285](https://github.com/shopspring/decimal/pull/285) [#328](https://github.com/shopspring/decimal/pull/328) [#341](https://github.com/shopspring/decimal/pull/341)
- Use Godoc standard to mark deprecated Equals and StringScaled methods [#342](https://github.com/shopspring/decimal/pull/342)
- Removed unnecessary min function for RescalePair method [#265](https://github.com/shopspring/decimal/pull/265)
- Avoid reallocation of initial slice in MarshalBinary (GobEncode) [#355](https://github.com/shopspring/decimal/pull/355)
- Optimize NumDigits method [#301](https://github.com/shopspring/decimal/pull/301) [#356](https://github.com/shopspring/decimal/pull/356)
- Optimize BigInt method [#359](https://github.com/shopspring/decimal/pull/359)
- Support scanning uint64 [#131](https://github.com/shopspring/decimal/pull/131) [#364](https://github.com/shopspring/decimal/pull/364)
- Add docs section with alternative libraries [#363](https://github.com/shopspring/decimal/pull/363)

#### BUGFIXES
- Fix incorrect calculation of decimal modulo [#258](https://github.com/shopspring/decimal/pull/258) [#317](https://github.com/shopspring/decimal/pull/317)
- Allocate new(big.Int) in Copy method to deeply clone it [#278](https://github.com/shopspring/decimal/pull/278)
- Fix overflow edge case in QuoRem method [#322](https://github.com/shopspring/decimal/pull/322)

## Decimal v1.3.1

#### ENHANCEMENTS
- Reduce memory allocation in case of initialization from big.Int [#252](https://github.com/shopspring/decimal/pull/252)

#### BUGFIXES
- Fix binary marshalling of decimal zero value  [#253](https://github.com/shopspring/decimal/pull/253)

## Decimal v1.3.0

#### FEATURES
- Add NewFromFormattedString initializer [#184](https://github.com/shopspring/decimal/pull/184)
- Add NewNullDecimal initializer [#234](https://github.com/shopspring/decimal/pull/234)
- Add implementation of natural exponent function (Taylor, Hull-Abraham) [#229](https://github.com/shopspring/decimal/pull/229)
- Add RoundUp, RoundDown, RoundCeil, RoundFloor methods [#196](https://github.com/shopspring/decimal/pull/196) [#202](https://github.com/shopspring/decimal/pull/202) [#220](https://github.com/shopspring/decimal/pull/220)
- Add XML support for NullDecimal [#192](https://github.com/shopspring/decimal/pull/192)
- Add IsInteger method [#179](https://github.com/shopspring/decimal/pull/179)
- Add Copy helper method [#123](https://github.com/shopspring/decimal/pull/123)
- Add InexactFloat64 helper method [#205](https://github.com/shopspring/decimal/pull/205)
- Add CoefficientInt64 helper method [#244](https://github.com/shopspring/decimal/pull/244)

#### ENHANCEMENTS
- Performance optimization of NewFromString init method [#198](https://github.com/shopspring/decimal/pull/198)
- Performance optimization of Abs and Round methods [#240](https://github.com/shopspring/decimal/pull/240)
- Additional tests (CI) for ppc64le architecture [#188](https://github.com/shopspring/decimal/pull/188)

#### BUGFIXES
- Fix rounding in FormatFloat fallback path (roundShortest method, fix taken from Go main repository) [#161](https://github.com/shopspring/decimal/pull/161)
- Add slice range checks to UnmarshalBinary method [#232](https://github.com/shopspring/decimal/pull/232)

## Decimal v1.2.0

#### BREAKING
- Drop support for Go version older than 1.7 [#172](https://github.com/shopspring/decimal/pull/172)

#### FEATURES
- Add NewFromInt and NewFromInt32 initializers [#72](https://github.com/shopspring/decimal/pull/72)
- Add support for Go modules [#157](https://github.com/shopspring/decimal/pull/157)
- Add BigInt, BigFloat helper methods [#171](https://github.com/shopspring/decimal/pull/171)

#### ENHANCEMENTS
- Memory usage optimization [#160](https://github.com/shopspring/decimal/pull/160)
- Updated travis CI golang versions [#156](https://github.com/shopspring/decimal/pull/156)
- Update documentation [#173](https://github.com/shopspring/decimal/pull/173)
- Improve code quality [#174](https://github.com/shopspring/decimal/pull/174)

#### BUGFIXES
- Revert remove insignificant digits [#159](https://github.com/shopspring/decimal/pull/159)
- Remove 15 interval for RoundCash [#166](https://github.com/shopspring/decimal/pull/166)
```

## File: `LICENSE`
```
The MIT License (MIT)

Copyright (c) 2015 Spring, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

- Based on https://github.com/oguzbilgic/fpd, which has the following license:
"""
The MIT License (MIT)

Copyright (c) 2013 Oguz Bilgic

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
```

## File: `README.md`
```markdown
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
numbers such as `0.1` exactly.

Consider this code: http://play.golang.org/p/TQBd4yJe6B You might expect that
it prints out `10`, but it actually prints `9.999999999999831`. Over time,
these small errors can really add up!

#### Why don't you just use big.Rat?

big.Rat is fine for representing rational numbers, but Decimal is better for
representing money. Why? Here's a (contrived) example:

Let's say you use big.Rat, and you have two numbers, x and y, both
representing 1/3, and you have `z = 1 - x - y = 1/3`. If you print each one
out, the string output has to stop somewhere (let's say it stops at 3 decimal
digits, for simplicity), so you'll get 0.333, 0.333, and 0.333. But where did
the other 0.001 go?

Here's the above example as code: http://play.golang.org/p/lCZZs0w9KE

With Decimal, the strings being printed out represent the number exactly. So,
if you have `x = y = 1/3` (with precision 3), they will actually be equal to
0.333, and when you do `z = 1 - x - y`, `z` will be equal to .334. No money is
unaccounted for!

You still have to be careful. If you want to split a number `N` 3 ways, you
can't just send `N/3` to three different people. You have to pick one to send
`N - (2/3*N)` to. That person will receive the fraction of a penny remainder.

But, it is much easier to be careful with Decimal than with big.Rat.

#### Why isn't the API similar to big.Int's?

big.Int's API is built to reduce the number of memory allocations for maximal
performance. This makes sense for its use-case, but the trade-off is that the
API is awkward and easy to misuse.

For example, to add two big.Ints, you do: `z := new(big.Int).Add(x, y)`. A
developer unfamiliar with this API might try to do `z := a.Add(a, b)`. This
modifies `a` and sets `z` as an alias for `a`, which they might not expect. It
also modifies any other aliases to `a`.

Here's an example of the subtle bugs you can introduce with big.Int's API:
https://play.golang.org/p/x2R_78pa8r

In contrast, it's difficult to make such mistakes with decimal. Decimals
behave like other go numbers types: even though `a = b` will not deep copy
`b` into `a`, it is impossible to modify a Decimal, since all Decimal methods
return new Decimals and do not modify the originals. The downside is that
this causes extra allocations, so Decimal is less performant.  My assumption
is that if you're using Decimals, you probably care more about correctness
than performance.

## License

The MIT License (MIT)

This is a heavily modified fork of [fpd.Decimal](https://github.com/oguzbilgic/fpd), which was also released under the MIT License.
```

## File: `const.go`
```go
package decimal

import (
	"strings"
)

const (
	strLn10 = "2.302585092994045684017991454684364207601101488628772976033327900967572609677352480235997205089598298341967784042286248633409525465082806756666287369098781689482907208325554680843799894826233198528393505308965377732628846163366222287698219886746543667474404243274365155048934314939391479619404400222105101714174800368808401264708068556774321622835522011480466371565912137345074785694768346361679210180644507064800027750268491674655058685693567342067058113642922455440575892572420824131469568901675894025677631135691929203337658714166023010570308963457207544037084746994016826928280848118428931484852494864487192780967627127577539702766860595249671667418348570442250719796500471495105049221477656763693866297697952211071826454973477266242570942932258279850258550978526538320760672631716430950599508780752371033310119785754733154142180842754386359177811705430982748238504564801909561029929182431823752535770975053956518769751037497088869218020518933950723853920514463419726528728696511086257149219884997874887377134568620916705849807828059751193854445009978131146915934666241071846692310107598438319191292230792503747298650929009880391941702654416816335727555703151596113564846546190897042819763365836983716328982174407366009162177850541779276367731145041782137660111010731042397832521894898817597921798666394319523936855916447118246753245630912528778330963604262982153040874560927760726641354787576616262926568298704957954913954918049209069438580790032763017941503117866862092408537949861264933479354871737451675809537088281067452440105892444976479686075120275724181874989395971643105518848195288330746699317814634930000321200327765654130472621883970596794457943468343218395304414844803701305753674262153675579814770458031413637793236291560128185336498466942261465206459942072917119370602444929358037007718981097362533224548366988505528285966192805098447175198503666680874970496982273220244823343097169111136813588418696549323714996941979687803008850408979618598756579894836445212043698216415292987811742973332588607915912510967187510929248475023930572665446276200923068791518135803477701295593646298412366497023355174586195564772461857717369368404676577047874319780573853271810933883496338813069945569399346101090745616033312247949360455361849123333063704751724871276379140924398331810164737823379692265637682071706935846394531616949411701841938119405416449466111274712819705817783293841742231409930022911502362192186723337268385688273533371925103412930705632544426611429765388301822384091026198582888433587455960453004548370789052578473166283701953392231047527564998119228742789713715713228319641003422124210082180679525276689858180956119208391760721080919923461516952599099473782780648128058792731993893453415320185969711021407542282796298237068941764740642225757212455392526179373652434440560595336591539160312524480149313234572453879524389036839236450507881731359711238145323701508413491122324390927681724749607955799151363982881058285740538000653371655553014196332241918087621018204919492651483892"
)

var (
	ln10 = newConstApproximation(strLn10)
)

type constApproximation struct {
	exact          Decimal
	approximations []Decimal
}

func newConstApproximation(value string) constApproximation {
	parts := strings.Split(value, ".")
	coeff, fractional := parts[0], parts[1]

	coeffLen := len(coeff)
	maxPrecision := len(fractional)

	var approximations []Decimal
	for p := 1; p < maxPrecision; p *= 2 {
		r := RequireFromString(value[:coeffLen+p])
		approximations = append(approximations, r)
	}

	return constApproximation{
		RequireFromString(value),
		approximations,
	}
}

// Returns the smallest approximation available that's at least as precise
// as the passed precision (places after decimal point), i.e. Floor[ log2(precision) ] + 1
func (c constApproximation) withPrecision(precision int32) Decimal {
	i := 0

	if precision >= 1 {
		i++
	}

	for precision >= 16 {
		precision /= 16
		i += 4
	}

	for precision >= 2 {
		precision /= 2
		i++
	}

	if i >= len(c.approximations) {
		return c.exact
	}

	return c.approximations[i]
}
```

## File: `const_test.go`
```go
package decimal

import "testing"

func TestConstApproximation(t *testing.T) {
	for _, testCase := range []struct {
		Const                 string
		Precision             int32
		ExpectedApproximation string
	}{
		{"2.3025850929940456840179914546", 0, "2"},
		{"2.3025850929940456840179914546", 1, "2.3"},
		{"2.3025850929940456840179914546", 3, "2.302"},
		{"2.3025850929940456840179914546", 5, "2.302585"},
		{"2.3025850929940456840179914546", 10, "2.302585092994045"},
		{"2.3025850929940456840179914546", 100, "2.3025850929940456840179914546"},
		{"2.3025850929940456840179914546", -1, "2"},
		{"2.3025850929940456840179914546", -5, "2"},
		{"3.14159265359", 0, "3"},
		{"3.14159265359", 1, "3.1"},
		{"3.14159265359", 2, "3.141"},
		{"3.14159265359", 4, "3.1415926"},
		{"3.14159265359", 13, "3.14159265359"},
	} {
		ca := newConstApproximation(testCase.Const)
		expected, _ := NewFromString(testCase.ExpectedApproximation)

		approximation := ca.withPrecision(testCase.Precision)

		if approximation.Cmp(expected) != 0 {
			t.Errorf("expected approximation %s, got %s - for const with %s precision %d", testCase.ExpectedApproximation, approximation.String(), testCase.Const, testCase.Precision)
		}
	}
}
```

## File: `decimal-go.go`
```go
// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Multiprecision decimal numbers.
// For floating-point formatting only; not general purpose.
// Only operations are assign and (binary) left/right shift.
// Can do binary floating point in multiprecision decimal precisely
// because 2 divides 10; cannot do decimal floating point
// in multiprecision binary precisely.

package decimal

type decimal struct {
	d     [800]byte // digits, big-endian representation
	nd    int       // number of digits used
	dp    int       // decimal point
	neg   bool      // negative flag
	trunc bool      // discarded nonzero digits beyond d[:nd]
}

func (a *decimal) String() string {
	n := 10 + a.nd
	if a.dp > 0 {
		n += a.dp
	}
	if a.dp < 0 {
		n += -a.dp
	}

	buf := make([]byte, n)
	w := 0
	switch {
	case a.nd == 0:
		return "0"

	case a.dp <= 0:
		// zeros fill space between decimal point and digits
		buf[w] = '0'
		w++
		buf[w] = '.'
		w++
		w += digitZero(buf[w : w+-a.dp])
		w += copy(buf[w:], a.d[0:a.nd])

	case a.dp < a.nd:
		// decimal point in middle of digits
		w += copy(buf[w:], a.d[0:a.dp])
		buf[w] = '.'
		w++
		w += copy(buf[w:], a.d[a.dp:a.nd])

	default:
		// zeros fill space between digits and decimal point
		w += copy(buf[w:], a.d[0:a.nd])
		w += digitZero(buf[w : w+a.dp-a.nd])
	}
	return string(buf[0:w])
}

func digitZero(dst []byte) int {
	for i := range dst {
		dst[i] = '0'
	}
	return len(dst)
}

// trim trailing zeros from number.
// (They are meaningless; the decimal point is tracked
// independent of the number of digits.)
func trim(a *decimal) {
	for a.nd > 0 && a.d[a.nd-1] == '0' {
		a.nd--
	}
	if a.nd == 0 {
		a.dp = 0
	}
}

// Assign v to a.
func (a *decimal) Assign(v uint64) {
	var buf [24]byte

	// Write reversed decimal in buf.
	n := 0
	for v > 0 {
		v1 := v / 10
		v -= 10 * v1
		buf[n] = byte(v + '0')
		n++
		v = v1
	}

	// Reverse again to produce forward decimal in a.d.
	a.nd = 0
	for n--; n >= 0; n-- {
		a.d[a.nd] = buf[n]
		a.nd++
	}
	a.dp = a.nd
	trim(a)
}

// Maximum shift that we can do in one pass without overflow.
// A uint has 32 or 64 bits, and we have to be able to accommodate 9<<k.
const uintSize = 32 << (^uint(0) >> 63)
const maxShift = uintSize - 4

// Binary shift right (/ 2) by k bits.  k <= maxShift to avoid overflow.
func rightShift(a *decimal, k uint) {
	r := 0 // read pointer
	w := 0 // write pointer

	// Pick up enough leading digits to cover first shift.
	var n uint
	for ; n>>k == 0; r++ {
		if r >= a.nd {
			if n == 0 {
				// a == 0; shouldn't get here, but handle anyway.
				a.nd = 0
				return
			}
			for n>>k == 0 {
				n = n * 10
				r++
			}
			break
		}
		c := uint(a.d[r])
		n = n*10 + c - '0'
	}
	a.dp -= r - 1

	var mask uint = (1 << k) - 1

	// Pick up a digit, put down a digit.
	for ; r < a.nd; r++ {
		c := uint(a.d[r])
		dig := n >> k
		n &= mask
		a.d[w] = byte(dig + '0')
		w++
		n = n*10 + c - '0'
	}

	// Put down extra digits.
	for n > 0 {
		dig := n >> k
		n &= mask
		if w < len(a.d) {
			a.d[w] = byte(dig + '0')
			w++
		} else if dig > 0 {
			a.trunc = true
		}
		n = n * 10
	}

	a.nd = w
	trim(a)
}

// Cheat sheet for left shift: table indexed by shift count giving
// number of new digits that will be introduced by that shift.
//
// For example, leftcheats[4] = {2, "625"}.  That means that
// if we are shifting by 4 (multiplying by 16), it will add 2 digits
// when the string prefix is "625" through "999", and one fewer digit
// if the string prefix is "000" through "624".
//
// Credit for this trick goes to Ken.

type leftCheat struct {
	delta  int    // number of new digits
	cutoff string // minus one digit if original < a.
}

var leftcheats = []leftCheat{
	// Leading digits of 1/2^i = 5^i.
	// 5^23 is not an exact 64-bit floating point number,
	// so have to use bc for the math.
	// Go up to 60 to be large enough for 32bit and 64bit platforms.
	/*
		seq 60 | sed 's/^/5^/' | bc |
		awk 'BEGIN{ print "\t{ 0, \"\" }," }
		{
			log2 = log(2)/log(10)
			printf("\t{ %d, \"%s\" },\t// * %d\n",
				int(log2*NR+1), $0, 2**NR)
		}'
	*/
	{0, ""},
	{1, "5"},                                           // * 2
	{1, "25"},                                          // * 4
	{1, "125"},                                         // * 8
	{2, "625"},                                         // * 16
	{2, "3125"},                                        // * 32
	{2, "15625"},                                       // * 64
	{3, "78125"},                                       // * 128
	{3, "390625"},                                      // * 256
	{3, "1953125"},                                     // * 512
	{4, "9765625"},                                     // * 1024
	{4, "48828125"},                                    // * 2048
	{4, "244140625"},                                   // * 4096
	{4, "1220703125"},                                  // * 8192
	{5, "6103515625"},                                  // * 16384
	{5, "30517578125"},                                 // * 32768
	{5, "152587890625"},                                // * 65536
	{6, "762939453125"},                                // * 131072
	{6, "3814697265625"},                               // * 262144
	{6, "19073486328125"},                              // * 524288
	{7, "95367431640625"},                              // * 1048576
	{7, "476837158203125"},                             // * 2097152
	{7, "2384185791015625"},                            // * 4194304
	{7, "11920928955078125"},                           // * 8388608
	{8, "59604644775390625"},                           // * 16777216
	{8, "298023223876953125"},                          // * 33554432
	{8, "1490116119384765625"},                         // * 67108864
	{9, "7450580596923828125"},                         // * 134217728
	{9, "37252902984619140625"},                        // * 268435456
	{9, "186264514923095703125"},                       // * 536870912
	{10, "931322574615478515625"},                      // * 1073741824
	{10, "4656612873077392578125"},                     // * 2147483648
	{10, "23283064365386962890625"},                    // * 4294967296
	{10, "116415321826934814453125"},                   // * 8589934592
	{11, "582076609134674072265625"},                   // * 17179869184
	{11, "2910383045673370361328125"},                  // * 34359738368
	{11, "14551915228366851806640625"},                 // * 68719476736
	{12, "72759576141834259033203125"},                 // * 137438953472
	{12, "363797880709171295166015625"},                // * 274877906944
	{12, "1818989403545856475830078125"},               // * 549755813888
	{13, "9094947017729282379150390625"},               // * 1099511627776
	{13, "45474735088646411895751953125"},              // * 2199023255552
	{13, "227373675443232059478759765625"},             // * 4398046511104
	{13, "1136868377216160297393798828125"},            // * 8796093022208
	{14, "5684341886080801486968994140625"},            // * 17592186044416
	{14, "28421709430404007434844970703125"},           // * 35184372088832
	{14, "142108547152020037174224853515625"},          // * 70368744177664
	{15, "710542735760100185871124267578125"},          // * 140737488355328
	{15, "3552713678800500929355621337890625"},         // * 281474976710656
	{15, "17763568394002504646778106689453125"},        // * 562949953421312
	{16, "88817841970012523233890533447265625"},        // * 1125899906842624
	{16, "444089209850062616169452667236328125"},       // * 2251799813685248
	{16, "2220446049250313080847263336181640625"},      // * 4503599627370496
	{16, "11102230246251565404236316680908203125"},     // * 9007199254740992
	{17, "55511151231257827021181583404541015625"},     // * 18014398509481984
	{17, "277555756156289135105907917022705078125"},    // * 36028797018963968
	{17, "1387778780781445675529539585113525390625"},   // * 72057594037927936
	{18, "6938893903907228377647697925567626953125"},   // * 144115188075855872
	{18, "34694469519536141888238489627838134765625"},  // * 288230376151711744
	{18, "173472347597680709441192448139190673828125"}, // * 576460752303423488
	{19, "867361737988403547205962240695953369140625"}, // * 1152921504606846976
}

// Is the leading prefix of b lexicographically less than s?
func prefixIsLessThan(b []byte, s string) bool {
	for i := 0; i < len(s); i++ {
		if i >= len(b) {
			return true
		}
		if b[i] != s[i] {
			return b[i] < s[i]
		}
	}
	return false
}

// Binary shift left (* 2) by k bits.  k <= maxShift to avoid overflow.
func leftShift(a *decimal, k uint) {
	delta := leftcheats[k].delta
	if prefixIsLessThan(a.d[0:a.nd], leftcheats[k].cutoff) {
		delta--
	}

	r := a.nd         // read index
	w := a.nd + delta // write index

	// Pick up a digit, put down a digit.
	var n uint
	for r--; r >= 0; r-- {
		n += (uint(a.d[r]) - '0') << k
		quo := n / 10
		rem := n - 10*quo
		w--
		if w < len(a.d) {
			a.d[w] = byte(rem + '0')
		} else if rem != 0 {
			a.trunc = true
		}
		n = quo
	}

	// Put down extra digits.
	for n > 0 {
		quo := n / 10
		rem := n - 10*quo
		w--
		if w < len(a.d) {
			a.d[w] = byte(rem + '0')
		} else if rem != 0 {
			a.trunc = true
		}
		n = quo
	}

	a.nd += delta
	if a.nd >= len(a.d) {
		a.nd = len(a.d)
	}
	a.dp += delta
	trim(a)
}

// Binary shift left (k > 0) or right (k < 0).
func (a *decimal) Shift(k int) {
	switch {
	case a.nd == 0:
		// nothing to do: a == 0
	case k > 0:
		for k > maxShift {
			leftShift(a, maxShift)
			k -= maxShift
		}
		leftShift(a, uint(k))
	case k < 0:
		for k < -maxShift {
			rightShift(a, maxShift)
			k += maxShift
		}
		rightShift(a, uint(-k))
	}
}

// If we chop a at nd digits, should we round up?
func shouldRoundUp(a *decimal, nd int) bool {
	if nd < 0 || nd >= a.nd {
		return false
	}
	if a.d[nd] == '5' && nd+1 == a.nd { // exactly halfway - round to even
		// if we truncated, a little higher than what's recorded - always round up
		if a.trunc {
			return true
		}
		return nd > 0 && (a.d[nd-1]-'0')%2 != 0
	}
	// not halfway - digit tells all
	return a.d[nd] >= '5'
}

// Round a to nd digits (or fewer).
// If nd is zero, it means we're rounding
// just to the left of the digits, as in
// 0.09 -> 0.1.
func (a *decimal) Round(nd int) {
	if nd < 0 || nd >= a.nd {
		return
	}
	if shouldRoundUp(a, nd) {
		a.RoundUp(nd)
	} else {
		a.RoundDown(nd)
	}
}

// Round a down to nd digits (or fewer).
func (a *decimal) RoundDown(nd int) {
	if nd < 0 || nd >= a.nd {
		return
	}
	a.nd = nd
	trim(a)
}

// Round a up to nd digits (or fewer).
func (a *decimal) RoundUp(nd int) {
	if nd < 0 || nd >= a.nd {
		return
	}

	// round up
	for i := nd - 1; i >= 0; i-- {
		c := a.d[i]
		if c < '9' { // can stop after this digit
			a.d[i]++
			a.nd = i + 1
			return
		}
	}

	// Number is all 9s.
	// Change to single 1 with adjusted decimal point.
	a.d[0] = '1'
	a.nd = 1
	a.dp++
}

// Extract integer part, rounded appropriately.
// No guarantees about overflow.
func (a *decimal) RoundedInteger() uint64 {
	if a.dp > 20 {
		return 0xFFFFFFFFFFFFFFFF
	}
	var i int
	n := uint64(0)
	for i = 0; i < a.dp && i < a.nd; i++ {
		n = n*10 + uint64(a.d[i]-'0')
	}
	for ; i < a.dp; i++ {
		n *= 10
	}
	if shouldRoundUp(a, a.dp) {
		n++
	}
	return n
}
```

## File: `decimal.go`
```go
// Package decimal implements an arbitrary precision fixed-point decimal.
//
// The zero-value of a Decimal is 0, as you would expect.
//
// The best way to create a new Decimal is to use decimal.NewFromString, ex:
//
//	n, err := decimal.NewFromString("-123.4567")
//	n.String() // output: "-123.4567"
//
// To use Decimal as part of a struct:
//
//	type StructName struct {
//	    Number Decimal
//	}
//
// Note: This can "only" represent numbers with a maximum of 2^31 digits after the decimal point.
package decimal

import (
	"database/sql/driver"
	"encoding/binary"
	"fmt"
	"math"
	"math/big"
	"regexp"
	"strconv"
	"strings"
)

// DivisionPrecision is the number of decimal places in the result when it
// doesn't divide exactly.
//
// Example:
//
//	d1 := decimal.NewFromFloat(2).Div(decimal.NewFromFloat(3))
//	d1.String() // output: "0.6666666666666667"
//	d2 := decimal.NewFromFloat(2).Div(decimal.NewFromFloat(30000))
//	d2.String() // output: "0.0000666666666667"
//	d3 := decimal.NewFromFloat(20000).Div(decimal.NewFromFloat(3))
//	d3.String() // output: "6666.6666666666666667"
//	decimal.DivisionPrecision = 3
//	d4 := decimal.NewFromFloat(2).Div(decimal.NewFromFloat(3))
//	d4.String() // output: "0.667"
var DivisionPrecision = 16

// PowPrecisionNegativeExponent specifies the maximum precision of the result (digits after decimal point)
// when calculating decimal power. Only used for cases where the exponent is a negative number.
// This constant applies to Pow, PowInt32 and PowBigInt methods, PowWithPrecision method is not constrained by it.
//
// Example:
//
//	d1, err := decimal.NewFromFloat(15.2).PowInt32(-2)
//	d1.String() // output: "0.0043282548476454"
//
//	decimal.PowPrecisionNegativeExponent = 24
//	d2, err := decimal.NewFromFloat(15.2).PowInt32(-2)
//	d2.String() // output: "0.004328254847645429362881"
var PowPrecisionNegativeExponent = 16

// MarshalJSONWithoutQuotes should be set to true if you want the decimal to
// be JSON marshaled as a number, instead of as a string.
// WARNING: this is dangerous for decimals with many digits, since many JSON
// unmarshallers (ex: Javascript's) will unmarshal JSON numbers to IEEE 754
// double-precision floating point numbers, which means you can potentially
// silently lose precision.
var MarshalJSONWithoutQuotes = false

// TrimTrailingZeros specifies whether trailing zeroes should be trimmed from a string representation of decimal.
// If set to true, trailing zeroes will be truncated (2.00 -> 2, 3.11 -> 3.11, 13.000 -> 13),
// otherwise trailing zeroes will be preserved (2.00 -> 2.00, 3.11 -> 3.11, 13.000 -> 13.000).
// Setting this value to false can be useful for APIs where exact decimal string representation matters.
var TrimTrailingZeros = true

// UseScientificNotation specifies whether scientific notation should be used when a decimal is turned
// into a string that has a "negative" precision.
//
// For example, 1200 rounded to the nearest 100 cannot accurately be shown as "1200" because the last two
// digits are unknown. With this set to true, that number would be expressed as "1.2E3" instead.
var UseScientificNotation = false

// ExpMaxIterations specifies the maximum number of iterations needed to calculate
// precise natural exponent value using ExpHullAbrham method.
var ExpMaxIterations = 1000

// Zero constant, to make computations faster.
// Zero should never be compared with == or != directly, please use decimal.Equal or decimal.Cmp instead.
var Zero = Decimal{}

var zeroInt = big.NewInt(0)
var oneInt = big.NewInt(1)
var twoInt = big.NewInt(2)
var fourInt = big.NewInt(4)
var fiveInt = big.NewInt(5)
var tenInt = big.NewInt(10)
var twentyInt = big.NewInt(20)

var factorials = []Decimal{New(1, 0)}

// Decimal represents a fixed-point decimal. It is immutable.
// number = value * 10 ^ exp
type Decimal struct {
	value *big.Int

	// NOTE(vadim): this must be an int32, because we cast it to float64 during
	// calculations. If exp is 64 bit, we might lose precision.
	// If we cared about being able to represent every possible decimal, we
	// could make exp a *big.Int but it would hurt performance and numbers
	// like that are unrealistic.
	exp int32
}

func (d Decimal) getValue() *big.Int {
	if d.value == nil {
		return zeroInt
	}
	return d.value
}

// New returns a new fixed-point decimal, value * 10 ^ exp.
func New(value int64, exp int32) Decimal {
	return Decimal{
		value: big.NewInt(value),
		exp:   exp,
	}
}

// NewFromInt converts an int64 to Decimal.
//
// Example:
//
//	NewFromInt(123).String() // output: "123"
//	NewFromInt(-10).String() // output: "-10"
func NewFromInt(value int64) Decimal {
	return Decimal{
		value: big.NewInt(value),
		exp:   0,
	}
}

// NewFromInt32 converts an int32 to Decimal.
//
// Example:
//
//	NewFromInt(123).String() // output: "123"
//	NewFromInt(-10).String() // output: "-10"
func NewFromInt32(value int32) Decimal {
	return Decimal{
		value: big.NewInt(int64(value)),
		exp:   0,
	}
}

// NewFromUint64 converts an uint64 to Decimal.
//
// Example:
//
//	NewFromUint64(123).String() // output: "123"
func NewFromUint64(value uint64) Decimal {
	return Decimal{
		value: new(big.Int).SetUint64(value),
		exp:   0,
	}
}

// NewFromBigInt returns a new Decimal from a big.Int, value * 10 ^ exp
func NewFromBigInt(value *big.Int, exp int32) Decimal {
	return Decimal{
		value: new(big.Int).Set(value),
		exp:   exp,
	}
}

// NewFromBigRat returns a new Decimal from a big.Rat. The numerator and
// denominator are divided and rounded to the given precision.
//
// Example:
//
//	d1 := NewFromBigRat(big.NewRat(0, 1), 0)    // output: "0"
//	d2 := NewFromBigRat(big.NewRat(4, 5), 1)    // output: "0.8"
//	d3 := NewFromBigRat(big.NewRat(1000, 3), 3) // output: "333.333"
//	d4 := NewFromBigRat(big.NewRat(2, 7), 4)    // output: "0.2857"
func NewFromBigRat(value *big.Rat, precision int32) Decimal {
	return Decimal{
		value: new(big.Int).Set(value.Num()),
		exp:   0,
	}.DivRound(Decimal{
		value: new(big.Int).Set(value.Denom()),
		exp:   0,
	}, precision)
}

// NewFromString returns a new Decimal from a string representation.
// Trailing zeroes are not trimmed.
//
// Example:
//
//	d, err := NewFromString("-123.45")
//	d2, err := NewFromString(".0001")
//	d3, err := NewFromString("1.47000")
func NewFromString(value string) (Decimal, error) {
	originalInput := value
	var intString string
	var exp int64

	// Check if number is using scientific notation and find dots
	eIndex := -1
	pIndex := -1
	for i, r := range value {
		if r == 'E' || r == 'e' {
			if eIndex > -1 {
				return Decimal{}, fmt.Errorf("can't convert %s to decimal: multiple 'E' characters found", value)
			}
			eIndex = i
			continue
		}

		if r == '.' {
			if pIndex > -1 {
				return Decimal{}, fmt.Errorf("can't convert %s to decimal: too many .s", value)
			}
			pIndex = i
		}
	}

	if eIndex != -1 {
		expInt, err := strconv.ParseInt(value[eIndex+1:], 10, 32)
		if err != nil {
			if e, ok := err.(*strconv.NumError); ok && e.Err == strconv.ErrRange {
				return Decimal{}, fmt.Errorf("can't convert %s to decimal: fractional part too long", value)
			}
			return Decimal{}, fmt.Errorf("can't convert %s to decimal: exponent is not numeric", value)
		}
		value = value[:eIndex]
		exp = expInt
	}

	if pIndex == -1 {
		// There is no decimal point, we can just parse the original string as
		// an int
		intString = value
	} else {
		if pIndex+1 < len(value) {
			intString = value[:pIndex] + value[pIndex+1:]
		} else {
			intString = value[:pIndex]
		}
		expInt := -len(value[pIndex+1:])
		exp += int64(expInt)
	}

	var dValue *big.Int
	// strconv.ParseInt is faster than new(big.Int).SetString so this is just a shortcut for strings we know won't overflow
	if len(intString) <= 18 {
		parsed64, err := strconv.ParseInt(intString, 10, 64)
		if err != nil {
			return Decimal{}, fmt.Errorf("can't convert %s to decimal", value)
		}
		dValue = big.NewInt(parsed64)
	} else {
		dValue = new(big.Int)
		_, ok := dValue.SetString(intString, 10)
		if !ok {
			return Decimal{}, fmt.Errorf("can't convert %s to decimal", value)
		}
	}

	if exp < math.MinInt32 || exp > math.MaxInt32 {
		// NOTE(vadim): I doubt a string could realistically be this long
		return Decimal{}, fmt.Errorf("can't convert %s to decimal: fractional part too long", originalInput)
	}

	return Decimal{
		value: dValue,
		exp:   int32(exp),
	}, nil
}

// NewFromFormattedString returns a new Decimal from a formatted string representation.
// The second argument - replRegexp, is a regular expression that is used to find characters that should be
// removed from given decimal string representation. All matched characters will be replaced with an empty string.
//
// Example:
//
//	r := regexp.MustCompile("[$,]")
//	d1, err := NewFromFormattedString("$5,125.99", r)
//
//	r2 := regexp.MustCompile("[_]")
//	d2, err := NewFromFormattedString("1_000_000", r2)
//
//	r3 := regexp.MustCompile("[USD\\s]")
//	d3, err := NewFromFormattedString("5000 USD", r3)
func NewFromFormattedString(value string, replRegexp *regexp.Regexp) (Decimal, error) {
	parsedValue := replRegexp.ReplaceAllString(value, "")
	d, err := NewFromString(parsedValue)
	if err != nil {
		return Decimal{}, err
	}
	return d, nil
}

// RequireFromString returns a new Decimal from a string representation
// or panics if NewFromString had returned an error.
//
// Example:
//
//	d := RequireFromString("-123.45")
//	d2 := RequireFromString(".0001")
func RequireFromString(value string) Decimal {
	dec, err := NewFromString(value)
	if err != nil {
		panic(err)
	}
	return dec
}

// NewFromFloat converts a float64 to Decimal.
//
// The converted number will contain the number of significant digits that can be
// represented in a float with reliable roundtrip.
// This is typically 15 digits, but may be more in some cases.
// See https://www.exploringbinary.com/decimal-precision-of-binary-floating-point-numbers/ for more information.
//
// For slightly faster conversion, use NewFromFloatWithExponent where you can specify the precision in absolute terms.
//
// NOTE: this will panic on NaN, +/-inf
func NewFromFloat(value float64) Decimal {
	if value == 0 {
		return New(0, 0)
	}
	return newFromFloat(value, math.Float64bits(value), &float64info)
}

// NewFromFloat32 converts a float32 to Decimal.
//
// The converted number will contain the number of significant digits that can be
// represented in a float with reliable roundtrip.
// This is typically 6-8 digits depending on the input.
// See https://www.exploringbinary.com/decimal-precision-of-binary-floating-point-numbers/ for more information.
//
// For slightly faster conversion, use NewFromFloatWithExponent where you can specify the precision in absolute terms.
//
// NOTE: this will panic on NaN, +/-inf
func NewFromFloat32(value float32) Decimal {
	if value == 0 {
		return New(0, 0)
	}
	// XOR is workaround for https://github.com/golang/go/issues/26285
	a := math.Float32bits(value) ^ 0x80808080
	return newFromFloat(float64(value), uint64(a)^0x80808080, &float32info)
}

func newFromFloat(val float64, bits uint64, flt *floatInfo) Decimal {
	if math.IsNaN(val) || math.IsInf(val, 0) {
		panic(fmt.Sprintf("Cannot create a Decimal from %v", val))
	}
	exp := int(bits>>flt.mantbits) & (1<<flt.expbits - 1)
	mant := bits & (uint64(1)<<flt.mantbits - 1)

	switch exp {
	case 0:
		// denormalized
		exp++

	default:
		// add implicit top bit
		mant |= uint64(1) << flt.mantbits
	}
	exp += flt.bias

	var d decimal
	d.Assign(mant)
	d.Shift(exp - int(flt.mantbits))
	d.neg = bits>>(flt.expbits+flt.mantbits) != 0

	roundShortest(&d, mant, exp, flt)
	// If less than 19 digits, we can do calculation in an int64.
	if d.nd < 19 {
		tmp := int64(0)
		m := int64(1)
		for i := d.nd - 1; i >= 0; i-- {
			tmp += m * int64(d.d[i]-'0')
			m *= 10
		}
		if d.neg {
			tmp *= -1
		}
		return Decimal{value: big.NewInt(tmp), exp: int32(d.dp) - int32(d.nd)}
	}
	dValue := new(big.Int)
	dValue, ok := dValue.SetString(string(d.d[:d.nd]), 10)
	if ok {
		return Decimal{value: dValue, exp: int32(d.dp) - int32(d.nd)}
	}

	return NewFromFloatWithExponent(val, int32(d.dp)-int32(d.nd))
}

// NewFromFloatWithExponent converts a float64 to Decimal, with an arbitrary
// number of fractional digits.
//
// Example:
//
//	NewFromFloatWithExponent(123.456, -2).String() // output: "123.46"
func NewFromFloatWithExponent(value float64, exp int32) Decimal {
	if math.IsNaN(value) || math.IsInf(value, 0) {
		panic(fmt.Sprintf("Cannot create a Decimal from %v", value))
	}

	bits := math.Float64bits(value)
	mant := bits & (1<<52 - 1)
	exp2 := int32((bits >> 52) & (1<<11 - 1))
	sign := bits >> 63

	if exp2 == 0 {
		// specials
		if mant == 0 {
			return Decimal{}
		}
		// subnormal
		exp2++
	} else {
		// normal
		mant |= 1 << 52
	}

	exp2 -= 1023 + 52

	// normalizing base-2 values
	for mant&1 == 0 {
		mant = mant >> 1
		exp2++
	}

	// maximum number of fractional base-10 digits to represent 2^N exactly cannot be more than -N if N<0
	if exp < 0 && exp < exp2 {
		if exp2 < 0 {
			exp = exp2
		} else {
			exp = 0
		}
	}

	// representing 10^M * 2^N as 5^M * 2^(M+N)
	exp2 -= exp

	temp := big.NewInt(1)
	dMant := big.NewInt(int64(mant))

	// applying 5^M
	if exp > 0 {
		temp = temp.SetInt64(int64(exp))
		temp = temp.Exp(fiveInt, temp, nil)
	} else if exp < 0 {
		temp = temp.SetInt64(-int64(exp))
		temp = temp.Exp(fiveInt, temp, nil)
		dMant = dMant.Mul(dMant, temp)
		temp = temp.SetUint64(1)
	}

	// applying 2^(M+N)
	if exp2 > 0 {
		dMant = dMant.Lsh(dMant, uint(exp2))
	} else if exp2 < 0 {
		temp = temp.Lsh(temp, uint(-exp2))
	}

	// rounding and downscaling
	if exp > 0 || exp2 < 0 {
		halfDown := new(big.Int).Rsh(temp, 1)
		dMant = dMant.Add(dMant, halfDown)
		dMant = dMant.Quo(dMant, temp)
	}

	if sign == 1 {
		dMant = dMant.Neg(dMant)
	}

	return Decimal{
		value: dMant,
		exp:   exp,
	}
}

// Copy returns a copy of decimal with the same value and exponent, but a different pointer to value.
func (d Decimal) Copy() Decimal {
	return Decimal{
		value: new(big.Int).Set(d.getValue()),
		exp:   d.exp,
	}
}

// rescale returns a rescaled version of the decimal. Returned
// decimal may be less precise if the given exponent is bigger
// than the initial exponent of the Decimal.
// NOTE: this will truncate, NOT round
//
// Example:
//
//	d := New(12345, -4)
//	d2 := d.rescale(-1)
//	d3 := d2.rescale(-4)
//	println(d1)
//	println(d2)
//	println(d3)
//
// Output:
//
//	1.2345
//	1.2
//	1.2000
func (d Decimal) rescale(exp int32) Decimal {
	if d.exp == exp {
		return Decimal{
			new(big.Int).Set(d.getValue()),
			d.exp,
		}
	}

	// NOTE(vadim): must convert exps to float64 before - to prevent overflow
	diff := math.Abs(float64(exp) - float64(d.exp))
	value := new(big.Int).Set(d.getValue())

	expScale := new(big.Int).Exp(tenInt, big.NewInt(int64(diff)), nil)
	if exp > d.exp {
		value = value.Quo(value, expScale)
	} else if exp < d.exp {
		value = value.Mul(value, expScale)
	}

	return Decimal{
		value: value,
		exp:   exp,
	}
}

// Abs returns the absolute value of the decimal.
func (d Decimal) Abs() Decimal {
	if !d.IsNegative() {
		return d
	}
	d2Value := new(big.Int).Abs(d.getValue())
	return Decimal{
		value: d2Value,
		exp:   d.exp,
	}
}

// Add returns d + d2.
func (d Decimal) Add(d2 Decimal) Decimal {
	rd, rd2 := RescalePair(d, d2)

	d3Value := new(big.Int).Add(rd.getValue(), rd2.getValue())
	return Decimal{
		value: d3Value,
		exp:   rd.exp,
	}
}

// Sub returns d - d2.
func (d Decimal) Sub(d2 Decimal) Decimal {
	rd, rd2 := RescalePair(d, d2)

	d3Value := new(big.Int).Sub(rd.getValue(), rd2.getValue())
	return Decimal{
		value: d3Value,
		exp:   rd.exp,
	}
}

// Neg returns -d.
func (d Decimal) Neg() Decimal {
	val := new(big.Int).Neg(d.getValue())
	return Decimal{
		value: val,
		exp:   d.exp,
	}
}

// Mul returns d * d2.
func (d Decimal) Mul(d2 Decimal) Decimal {
	expInt64 := int64(d.exp) + int64(d2.exp)
	if expInt64 > math.MaxInt32 || expInt64 < math.MinInt32 {
		// NOTE(vadim): better to panic than give incorrect results, as
		// Decimals are usually used for money
		panic(fmt.Sprintf("exponent %v overflows an int32!", expInt64))
	}

	d3Value := new(big.Int).Mul(d.getValue(), d2.getValue())
	return Decimal{
		value: d3Value,
		exp:   int32(expInt64),
	}
}

// Shift shifts the decimal in base 10.
// It shifts left when shift is positive and right if shift is negative.
// In simpler terms, the given value for shift is added to the exponent
// of the decimal.
func (d Decimal) Shift(shift int32) Decimal {
	return Decimal{
		value: new(big.Int).Set(d.getValue()),
		exp:   d.exp + shift,
	}
}

// Div returns d / d2. If it doesn't divide exactly, the result will have
// DivisionPrecision digits after the decimal point.
func (d Decimal) Div(d2 Decimal) Decimal {
	return d.DivRound(d2, int32(DivisionPrecision))
}

// QuoRem does division with remainder
// d.QuoRem(d2,precision) returns quotient q and remainder r such that
//
//	d = d2 * q + r, q an integer multiple of 10^(-precision)
//	0 <= r < abs(d2) * 10 ^(-precision) if d>=0
//	0 >= r > -abs(d2) * 10 ^(-precision) if d<0
//
// Note that precision<0 is allowed as input.
func (d Decimal) QuoRem(d2 Decimal, precision int32) (Decimal, Decimal) {
	if d2.getValue().Sign() == 0 {
		panic("decimal division by 0")
	}
	scale := -precision
	e := int64(d.exp) - int64(d2.exp) - int64(scale)
	if e > math.MaxInt32 || e < math.MinInt32 {
		panic("overflow in decimal QuoRem")
	}
	var aa, bb, expo big.Int
	var scalerest int32
	// d = a 10^ea
	// d2 = b 10^eb
	if e < 0 {
		aa = *d.getValue()
		expo.SetInt64(-e)
		bb.Exp(tenInt, &expo, nil)
		bb.Mul(d2.getValue(), &bb)
		scalerest = d.exp
		// now aa = a
		//     bb = b 10^(scale + eb - ea)
	} else {
		expo.SetInt64(e)
		aa.Exp(tenInt, &expo, nil)
		aa.Mul(d.getValue(), &aa)
		bb = *d2.getValue()
		scalerest = scale + d2.exp
		// now aa = a ^ (ea - eb - scale)
		//     bb = b
	}
	var q, r big.Int
	q.QuoRem(&aa, &bb, &r)
	dq := Decimal{value: &q, exp: scale}
	dr := Decimal{value: &r, exp: scalerest}
	return dq, dr
}

// DivRound divides and rounds to a given precision
// i.e. to an integer multiple of 10^(-precision)
//
//	for a positive quotient digit 5 is rounded up, away from 0
//	if the quotient is negative then digit 5 is rounded down, away from 0
//
// Note that precision<0 is allowed as input.
func (d Decimal) DivRound(d2 Decimal, precision int32) Decimal {
	// QuoRem already checks initialization
	q, r := d.QuoRem(d2, precision)
	// the actual rounding decision is based on comparing r*10^precision and d2/2
	// instead compare 2 r 10 ^precision and d2
	var rv2 big.Int
	rv2.Abs(r.getValue())
	rv2.Lsh(&rv2, 1)
	// now rv2 = abs(r.value) * 2
	r2 := Decimal{value: &rv2, exp: r.exp + precision}
	// r2 is now 2 * r * 10 ^ precision
	var c = r2.Cmp(d2.Abs())

	if c < 0 {
		return q
	}

	if d.getValue().Sign()*d2.getValue().Sign() < 0 {
		return q.Sub(New(1, -precision))
	}

	return q.Add(New(1, -precision))
}

// Mod returns d % d2.
func (d Decimal) Mod(d2 Decimal) Decimal {
	_, r := d.QuoRem(d2, 0)
	return r
}

// Pow returns d to the power of d2.
// When exponent is negative the returned decimal will have maximum precision of PowPrecisionNegativeExponent places after decimal point.
//
// Pow returns 0 (zero-value of Decimal) instead of error for power operation edge cases, to handle those edge cases use PowWithPrecision
// Edge cases not handled by Pow:
//   - 0 ** 0 => undefined value
//   - 0 ** y, where y < 0 => infinity
//   - x ** y, where x < 0 and y is non-integer decimal => imaginary value
//
// Example:
//
//	d1 := decimal.NewFromFloat(4.0)
//	d2 := decimal.NewFromFloat(4.0)
//	res1 := d1.Pow(d2)
//	res1.String() // output: "256"
//
//	d3 := decimal.NewFromFloat(5.0)
//	d4 := decimal.NewFromFloat(5.73)
//	res2 := d3.Pow(d4)
//	res2.String() // output: "10118.08037125"
func (d Decimal) Pow(d2 Decimal) Decimal {
	baseSign := d.Sign()
	expSign := d2.Sign()

	if baseSign == 0 {
		if expSign == 0 {
			return Decimal{}
		}
		if expSign == 1 {
			return Decimal{zeroInt, 0}
		}
		if expSign == -1 {
			return Decimal{}
		}
	}

	if expSign == 0 {
		return Decimal{oneInt, 0}
	}

	// TODO: optimize extraction of fractional part
	one := Decimal{oneInt, 0}
	expIntPart, expFracPart := d2.QuoRem(one, 0)

	if baseSign == -1 && !expFracPart.IsZero() {
		return Decimal{}
	}

	intPartPow, _ := d.PowBigInt(expIntPart.getValue())

	// if exponent is an integer we don't need to calculate d1**frac(d2)
	if expFracPart.getValue().Sign() == 0 {
		return intPartPow
	}

	// TODO: optimize NumDigits for more performant precision adjustment
	digitsBase := d.NumDigits()
	digitsExponent := d2.NumDigits()

	precision := digitsBase

	if digitsExponent > precision {
		precision += digitsExponent
	}

	precision += 6

	// Calculate x ** frac(y), where
	// x ** frac(y) = exp(ln(x ** frac(y)) = exp(ln(x) * frac(y))
	fracPartPow, err := d.Abs().Ln(-d.exp + int32(precision))
	if err != nil {
		return Decimal{}
	}

	fracPartPow = fracPartPow.Mul(expFracPart)

	fracPartPow, err = fracPartPow.ExpTaylor(-d.exp + int32(precision))
	if err != nil {
		return Decimal{}
	}

	// Join integer and fractional part,
	// base ** (expBase + expFrac) = base ** expBase * base ** expFrac
	res := intPartPow.Mul(fracPartPow)

	return res
}

// PowWithPrecision returns d to the power of d2.
// Precision parameter specifies minimum precision of the result (digits after decimal point).
// Returned decimal is not rounded to 'precision' places after decimal point.
//
// PowWithPrecision returns error when:
//   - 0 ** 0 => undefined value
//   - 0 ** y, where y < 0 => infinity
//   - x ** y, where x < 0 and y is non-integer decimal => imaginary value
//
// Example:
//
//	d1 := decimal.NewFromFloat(4.0)
//	d2 := decimal.NewFromFloat(4.0)
//	res1, err := d1.PowWithPrecision(d2, 2)
//	res1.String() // output: "256"
//
//	d3 := decimal.NewFromFloat(5.0)
//	d4 := decimal.NewFromFloat(5.73)
//	res2, err := d3.PowWithPrecision(d4, 5)
//	res2.String() // output: "10118.080371595015625"
//
//	d5 := decimal.NewFromFloat(-3.0)
//	d6 := decimal.NewFromFloat(-6.0)
//	res3, err := d5.PowWithPrecision(d6, 10)
//	res3.String() // output: "0.0013717421"
func (d Decimal) PowWithPrecision(d2 Decimal, precision int32) (Decimal, error) {
	baseSign := d.Sign()
	expSign := d2.Sign()

	if baseSign == 0 {
		if expSign == 0 {
			return Decimal{}, fmt.Errorf("cannot represent undefined value of 0**0")
		}
		if expSign == 1 {
			return Decimal{zeroInt, 0}, nil
		}
		if expSign == -1 {
			return Decimal{}, fmt.Errorf("cannot represent infinity value of 0 ** y, where y < 0")
		}
	}

	if expSign == 0 {
		return Decimal{oneInt, 0}, nil
	}

	// TODO: optimize extraction of fractional part
	one := Decimal{oneInt, 0}
	expIntPart, expFracPart := d2.QuoRem(one, 0)

	if baseSign == -1 && !expFracPart.IsZero() {
		return Decimal{}, fmt.Errorf("cannot represent imaginary value of x ** y, where x < 0 and y is non-integer decimal")
	}

	intPartPow, _ := d.powBigIntWithPrecision(expIntPart.getValue(), precision)

	// if exponent is an integer we don't need to calculate d1**frac(d2)
	if expFracPart.getValue().Sign() == 0 {
		return intPartPow, nil
	}

	// TODO: optimize NumDigits for more performant precision adjustment
	digitsBase := d.NumDigits()
	digitsExponent := d2.NumDigits()

	if int32(digitsBase) > precision {
		precision = int32(digitsBase)
	}
	if int32(digitsExponent) > precision {
		precision += int32(digitsExponent)
	}
	// increase precision by 10 to compensate for errors in further calculations
	precision += 10

	// Calculate x ** frac(y), where
	// x ** frac(y) = exp(ln(x ** frac(y)) = exp(ln(x) * frac(y))
	fracPartPow, err := d.Abs().Ln(precision)
	if err != nil {
		return Decimal{}, err
	}

	fracPartPow = fracPartPow.Mul(expFracPart)

	fracPartPow, err = fracPartPow.ExpTaylor(precision)
	if err != nil {
		return Decimal{}, err
	}

	// Join integer and fractional part,
	// base ** (expBase + expFrac) = base ** expBase * base ** expFrac
	res := intPartPow.Mul(fracPartPow)

	return res, nil
}

// PowInt32 returns d to the power of exp, where exp is int32.
// Only returns error when d and exp is 0, thus result is undefined.
//
// When exponent is negative the returned decimal will have maximum precision of PowPrecisionNegativeExponent places after decimal point.
//
// Example:
//
//	d1, err := decimal.NewFromFloat(4.0).PowInt32(4)
//	d1.String() // output: "256"
//
//	d2, err := decimal.NewFromFloat(3.13).PowInt32(5)
//	d2.String() // output: "300.4150512793"
func (d Decimal) PowInt32(exp int32) (Decimal, error) {
	if d.IsZero() && exp == 0 {
		return Decimal{}, fmt.Errorf("cannot represent undefined value of 0**0")
	}

	isExpNeg := exp < 0
	exp = abs(exp)

	n, result := d, New(1, 0)

	for exp > 0 {
		if exp%2 == 1 {
			result = result.Mul(n)
		}
		exp /= 2

		if exp > 0 {
			n = n.Mul(n)
		}
	}

	if isExpNeg {
		return New(1, 0).DivRound(result, int32(PowPrecisionNegativeExponent)), nil
	}

	return result, nil
}

// PowBigInt returns d to the power of exp, where exp is big.Int.
// Only returns error when d and exp is 0, thus result is undefined.
//
// When exponent is negative the returned decimal will have maximum precision of PowPrecisionNegativeExponent places after decimal point.
//
// Example:
//
//	d1, err := decimal.NewFromFloat(3.0).PowBigInt(big.NewInt(3))
//	d1.String() // output: "27"
//
//	d2, err := decimal.NewFromFloat(629.25).PowBigInt(big.NewInt(5))
//	d2.String() // output: "98654323103449.5673828125"
func (d Decimal) PowBigInt(exp *big.Int) (Decimal, error) {
	return d.powBigIntWithPrecision(exp, int32(PowPrecisionNegativeExponent))
}

func (d Decimal) powBigIntWithPrecision(exp *big.Int, precision int32) (Decimal, error) {
	if d.IsZero() && exp.Sign() == 0 {
		return Decimal{}, fmt.Errorf("cannot represent undefined value of 0**0")
	}

	tmpExp := new(big.Int).Set(exp)
	isExpNeg := exp.Sign() < 0

	if isExpNeg {
		tmpExp.Abs(tmpExp)
	}

	n, result := d, New(1, 0)

	for tmpExp.Sign() > 0 {
		if tmpExp.Bit(0) == 1 {
			result = result.Mul(n)
		}
		tmpExp.Rsh(tmpExp, 1)

		if tmpExp.Sign() > 0 {
			n = n.Mul(n)
		}
	}

	if isExpNeg {
		return New(1, 0).DivRound(result, precision), nil
	}

	return result, nil
}

// ExpHullAbrham calculates the natural exponent of decimal (e to the power of d) using Hull-Abraham algorithm.
// OverallPrecision argument specifies the overall precision of the result (integer part + decimal part).
//
// ExpHullAbrham is faster than ExpTaylor for small precision values, but it is much slower for large precision values.
//
// Example:
//
//	NewFromFloat(26.1).ExpHullAbrham(2).String()    // output: "220000000000"
//	NewFromFloat(26.1).ExpHullAbrham(20).String()   // output: "216314672147.05767284"
func (d Decimal) ExpHullAbrham(overallPrecision uint32) (Decimal, error) {
	// Algorithm based on Variable precision exponential function.
	// ACM Transactions on Mathematical Software by T. E. Hull & A. Abrham.
	if d.IsZero() {
		return Decimal{oneInt, 0}, nil
	}

	currentPrecision := overallPrecision

	// Algorithm does not work if currentPrecision * 23 < |x|.
	// Precision is automatically increased in such cases, so the value can be calculated precisely.
	// If newly calculated precision is higher than ExpMaxIterations the currentPrecision will not be changed.
	f := d.Abs().InexactFloat64()
	if ncp := f / 23; ncp > float64(currentPrecision) && ncp < float64(ExpMaxIterations) {
		currentPrecision = uint32(math.Ceil(ncp))
	}

	// fail if abs(d) beyond an over/underflow threshold
	overflowThreshold := New(23*int64(currentPrecision), 0)
	if d.Abs().Cmp(overflowThreshold) > 0 {
		return Decimal{}, fmt.Errorf("over/underflow threshold, exp(x) cannot be calculated precisely")
	}

	// Return 1 if abs(d) small enough; this also avoids later over/underflow
	overflowThreshold2 := New(9, -int32(currentPrecision)-1)
	if d.Abs().Cmp(overflowThreshold2) <= 0 {
		return Decimal{oneInt, d.exp}, nil
	}

	// t is the smallest integer >= 0 such that the corresponding abs(d/k) < 1
	t := d.exp + int32(d.NumDigits()) // Add d.NumDigits because the paper assumes that d.value [0.1, 1)

	if t < 0 {
		t = 0
	}

	k := New(1, t)                                          // reduction factor
	r := Decimal{new(big.Int).Set(d.getValue()), d.exp - t} // reduced argument
	p := int32(currentPrecision) + t + 2                    // precision for calculating the sum

	// Determine n, the number of therms for calculating sum
	// use first Newton step (1.435p - 1.182) / log10(p/abs(r))
	// for solving appropriate equation, along with directed
	// roundings and simple rational bound for log10(p/abs(r))
	rf := r.Abs().InexactFloat64()
	pf := float64(p)
	nf := math.Ceil((1.453*pf - 1.182) / math.Log10(pf/rf))
	if nf > float64(ExpMaxIterations) || math.IsNaN(nf) {
		return Decimal{}, fmt.Errorf("exact value cannot be calculated in <=ExpMaxIterations iterations")
	}
	n := int64(nf)

	tmp := New(0, 0)
	sum := New(1, 0)
	one := New(1, 0)
	for i := n - 1; i > 0; i-- {
		tmp.value.SetInt64(i)
		sum = sum.Mul(r.DivRound(tmp, p))
		sum = sum.Add(one)
	}

	ki := k.IntPart()
	res := New(1, 0)
	for i := ki; i > 0; i-- {
		res = res.Mul(sum)
	}

	resNumDigits := int32(res.NumDigits())

	var roundDigits int32
	if resNumDigits > abs(res.exp) {
		roundDigits = int32(currentPrecision) - resNumDigits - res.exp
	} else {
		roundDigits = int32(currentPrecision)
	}

	res = res.Round(roundDigits)

	return res, nil
}

// ExpTaylor calculates the natural exponent of decimal (e to the power of d) using Taylor series expansion.
// Precision argument specifies how precise the result must be (number of digits after decimal point).
// Negative precision is allowed.
//
// ExpTaylor is much faster for large precision values than ExpHullAbrham.
//
// Example:
//
//	d, err := NewFromFloat(26.1).ExpTaylor(2).String()
//	d.String()  // output: "216314672147.06"
//
//	NewFromFloat(26.1).ExpTaylor(20).String()
//	d.String()  // output: "216314672147.05767284062928674083"
//
//	NewFromFloat(26.1).ExpTaylor(-10).String()
//	d.String()  // output: "220000000000"
func (d Decimal) ExpTaylor(precision int32) (Decimal, error) {
	// Note(mwoss): Implementation can be optimized by exclusively using big.Int API only
	if d.IsZero() {
		return Decimal{oneInt, 0}.Round(precision), nil
	}

	var epsilon Decimal
	var divPrecision int32
	if precision < 0 {
		epsilon = New(1, -1)
		divPrecision = 8
	} else {
		epsilon = New(1, -precision-1)
		divPrecision = precision + 1
	}

	decAbs := d.Abs()
	pow := d.Abs()
	factorial := New(1, 0)

	result := New(1, 0)

	for i := int64(1); ; {
		step := pow.DivRound(factorial, divPrecision)
		result = result.Add(step)

		// Stop Taylor series when current step is smaller than epsilon
		if step.Cmp(epsilon) < 0 {
			break
		}

		pow = pow.Mul(decAbs)

		i++

		// Calculate next factorial number or retrieve cached value
		if len(factorials) >= int(i) && !factorials[i-1].IsZero() {
			factorial = factorials[i-1]
		} else {
			// To avoid any race conditions, firstly the zero value is appended to a slice to create
			// a spot for newly calculated factorial. After that, the zero value is replaced by calculated
			// factorial using the index notation.
			factorial = factorials[i-2].Mul(New(i, 0))
			factorials = append(factorials, Zero)
			factorials[i-1] = factorial
		}
	}

	if d.Sign() < 0 {
		result = New(1, 0).DivRound(result, precision+1)
	}

	result = result.Round(precision)
	return result, nil
}

// Ln calculates natural logarithm of d.
// Precision argument specifies how precise the result must be (number of digits after decimal point).
// Negative precision is allowed.
//
// Example:
//
//	d1, err := NewFromFloat(13.3).Ln(2)
//	d1.String()  // output: "2.59"
//
//	d2, err := NewFromFloat(579.161).Ln(10)
//	d2.String()  // output: "6.3615805046"
func (d Decimal) Ln(precision int32) (Decimal, error) {
	// Algorithm based on The Use of Iteration Methods for Approximating the Natural Logarithm,
	// James F. Epperson, The American Mathematical Monthly, Vol. 96, No. 9, November 1989, pp. 831-835.
	if d.IsNegative() {
		return Decimal{}, fmt.Errorf("cannot calculate natural logarithm for negative decimals")
	}

	if d.IsZero() {
		return Decimal{}, fmt.Errorf("cannot represent natural logarithm of 0, result: -infinity")
	}

	calcPrecision := precision + 2
	z := d.Copy()

	var comp1, comp3, comp2, comp4, reduceAdjust Decimal
	comp1 = z.Sub(Decimal{oneInt, 0})
	comp3 = Decimal{oneInt, -1}

	// for decimal in range [0.9, 1.1] where ln(d) is close to 0
	usePowerSeries := false

	if comp1.Abs().Cmp(comp3) <= 0 {
		usePowerSeries = true
	} else {
		// reduce input decimal to range [0.1, 1)
		expDelta := int32(z.NumDigits()) + z.exp
		z.exp -= expDelta

		// Input decimal was reduced by factor of 10^expDelta, thus we will need to add
		// ln(10^expDelta) = expDelta * ln(10)
		// to the result to compensate that
		ln10 := ln10.withPrecision(calcPrecision)
		reduceAdjust = NewFromInt32(expDelta)
		reduceAdjust = reduceAdjust.Mul(ln10)

		comp1 = z.Sub(Decimal{oneInt, 0})

		if comp1.Abs().Cmp(comp3) <= 0 {
			usePowerSeries = true
		} else {
			// initial estimate using floats
			zFloat := z.InexactFloat64()
			comp1 = NewFromFloat(math.Log(zFloat))
		}
	}

	epsilon := Decimal{oneInt, -calcPrecision}

	if usePowerSeries {
		// Power Series - https://en.wikipedia.org/wiki/Logarithm#Power_series
		// Calculating n-th term of formula: ln(z+1) = 2 sum [ 1 / (2n+1) * (z / (z+2))^(2n+1) ]
		// until the difference between current and next term is smaller than epsilon.
		// Coverage quite fast for decimals close to 1.0

		// z + 2
		comp2 = comp1.Add(Decimal{twoInt, 0})
		// z / (z + 2)
		comp3 = comp1.DivRound(comp2, calcPrecision)
		// 2 * (z / (z + 2))
		comp1 = comp3.Add(comp3)
		comp2 = comp1.Copy()

		for n := 1; ; n++ {
			// 2 * (z / (z+2))^(2n+1)
			comp2 = comp2.Mul(comp3).Mul(comp3)

			// 1 / (2n+1) * 2 * (z / (z+2))^(2n+1)
			comp4 = NewFromInt(int64(2*n + 1))
			comp4 = comp2.DivRound(comp4, calcPrecision)

			// comp1 = 2 sum [ 1 / (2n+1) * (z / (z+2))^(2n+1) ]
			comp1 = comp1.Add(comp4)

			if comp4.Abs().Cmp(epsilon) <= 0 {
				break
			}
		}
	} else {
		// Halley's Iteration.
		// Calculating n-th term of formula: a_(n+1) = a_n - 2 * (exp(a_n) - z) / (exp(a_n) + z),
		// until the difference between current and next term is smaller than epsilon
		var prevStep Decimal
		maxIters := calcPrecision*2 + 10

		for i := int32(0); i < maxIters; i++ {
			// exp(a_n)
			comp3, _ = comp1.ExpTaylor(calcPrecision)
			// exp(a_n) - z
			comp2 = comp3.Sub(z)
			// 2 * (exp(a_n) - z)
			comp2 = comp2.Add(comp2)
			// exp(a_n) + z
			comp4 = comp3.Add(z)
			// 2 * (exp(a_n) - z) / (exp(a_n) + z)
			comp3 = comp2.DivRound(comp4, calcPrecision)
			// comp1 = a_(n+1) = a_n - 2 * (exp(a_n) - z) / (exp(a_n) + z)
			comp1 = comp1.Sub(comp3)

			if prevStep.Add(comp3).IsZero() {
				// If iteration steps oscillate we should return early and prevent an infinity loop
				// NOTE(mwoss): This should be quite a rare case, returning error is not necessary
				break
			}

			if comp3.Abs().Cmp(epsilon) <= 0 {
				break
			}

			prevStep = comp3
		}
	}

	comp1 = comp1.Add(reduceAdjust)

	return comp1.Round(precision), nil
}

// NumDigits returns the number of digits of the decimal coefficient (d.Value)
func (d Decimal) NumDigits() int {
	v := d.getValue()
	if v.IsInt64() {
		i64 := v.Int64()
		// restrict fast path to integers with exact conversion to float64
		if i64 <= (1<<53) && i64 >= -(1<<53) {
			if i64 == 0 {
				return 1
			}
			return int(math.Log10(math.Abs(float64(i64)))) + 1
		}
	}

	estimatedNumDigits := int(float64(v.BitLen()) / math.Log2(10))

	// estimatedNumDigits (lg10) may be off by 1, need to verify
	digitsBigInt := big.NewInt(int64(estimatedNumDigits))
	errorCorrectionUnit := digitsBigInt.Exp(tenInt, digitsBigInt, nil)

	if v.CmpAbs(errorCorrectionUnit) >= 0 {
		return estimatedNumDigits + 1
	}

	return estimatedNumDigits
}

// IsInteger returns true when decimal can be represented as an integer value, otherwise, it returns false.
func (d Decimal) IsInteger() bool {
	// The most typical case, all decimal with exponent higher or equal 0 can be represented as integer
	if d.exp >= 0 {
		return true
	}
	// When the exponent is negative we have to check every number after the decimal place
	// If all of them are zeroes, we are sure that given decimal can be represented as an integer
	var r big.Int
	q := new(big.Int).Set(d.getValue())
	for z := abs(d.exp); z > 0; z-- {
		q.QuoRem(q, tenInt, &r)
		if r.Cmp(zeroInt) != 0 {
			return false
		}
	}
	return true
}

// Abs calculates absolute value of any int32. Used for calculating absolute value of decimal's exponent.
func abs(n int32) int32 {
	if n < 0 {
		return -n
	}
	return n
}

// Cmp compares the numbers represented by d and d2 and returns:
//
//	-1 if d <  d2
//	 0 if d == d2
//	+1 if d >  d2
func (d Decimal) Cmp(d2 Decimal) int {
	if d.exp == d2.exp {
		return d.getValue().Cmp(d2.getValue())
	}

	rd, rd2 := RescalePair(d, d2)

	return rd.getValue().Cmp(rd2.getValue())
}

// Compare compares the numbers represented by d and d2 and returns:
//
//	-1 if d <  d2
//	 0 if d == d2
//	+1 if d >  d2
func (d Decimal) Compare(d2 Decimal) int {
	return d.Cmp(d2)
}

// Equal returns whether the numbers represented by d and d2 are equal.
func (d Decimal) Equal(d2 Decimal) bool {
	return d.Cmp(d2) == 0
}

// Deprecated: Equals is deprecated, please use Equal method instead.
func (d Decimal) Equals(d2 Decimal) bool {
	return d.Equal(d2)
}

// GreaterThan (GT) returns true when d is greater than d2.
func (d Decimal) GreaterThan(d2 Decimal) bool {
	return d.Cmp(d2) == 1
}

// GreaterThanOrEqual (GTE) returns true when d is greater than or equal to d2.
func (d Decimal) GreaterThanOrEqual(d2 Decimal) bool {
	cmp := d.Cmp(d2)
	return cmp == 1 || cmp == 0
}

// LessThan (LT) returns true when d is less than d2.
func (d Decimal) LessThan(d2 Decimal) bool {
	return d.Cmp(d2) == -1
}

// LessThanOrEqual (LTE) returns true when d is less than or equal to d2.
func (d Decimal) LessThanOrEqual(d2 Decimal) bool {
	cmp := d.Cmp(d2)
	return cmp == -1 || cmp == 0
}

// Sign returns:
//
//	-1 if d <  0
//	 0 if d == 0
//	+1 if d >  0
func (d Decimal) Sign() int {
	return d.getValue().Sign()
}

// IsPositive return
//
//	true if d > 0
//	false if d == 0
//	false if d < 0
func (d Decimal) IsPositive() bool {
	return d.Sign() == 1
}

// IsNegative return
//
//	true if d < 0
//	false if d == 0
//	false if d > 0
func (d Decimal) IsNegative() bool {
	return d.Sign() == -1
}

// IsZero return
//
//	true if d == 0
//	false if d > 0
//	false if d < 0
func (d Decimal) IsZero() bool {
	return d.Sign() == 0
}

// Exponent returns the exponent, or scale component of the decimal.
func (d Decimal) Exponent() int32 {
	return d.exp
}

// Coefficient returns the coefficient of the decimal. It is scaled by 10^Exponent()
func (d Decimal) Coefficient() *big.Int {
	// we copy the coefficient so that mutating the result does not mutate the Decimal.
	return new(big.Int).Set(d.getValue())
}

// CoefficientInt64 returns the coefficient of the decimal as int64. It is scaled by 10^Exponent()
// If coefficient cannot be represented in an int64, the result will be undefined.
func (d Decimal) CoefficientInt64() int64 {
	return d.getValue().Int64()
}

// IntPart returns the integer component of the decimal.
func (d Decimal) IntPart() int64 {
	scaledD := d.rescale(0)
	return scaledD.getValue().Int64()
}

// BigInt returns integer component of the decimal as a BigInt.
func (d Decimal) BigInt() *big.Int {
	scaledD := d.rescale(0)
	return scaledD.getValue()
}

// BigFloat returns decimal as BigFloat.
// Be aware that casting decimal to BigFloat might cause a loss of precision.
func (d Decimal) BigFloat() *big.Float {
	f := &big.Float{}
	f.SetString(d.String())
	return f
}

// Rat returns a rational number representation of the decimal.
func (d Decimal) Rat() *big.Rat {
	if d.exp <= 0 {
		// NOTE(vadim): must negate after casting to prevent int32 overflow
		denom := new(big.Int).Exp(tenInt, big.NewInt(-int64(d.exp)), nil)
		return new(big.Rat).SetFrac(d.getValue(), denom)
	}

	mul := new(big.Int).Exp(tenInt, big.NewInt(int64(d.exp)), nil)
	num := new(big.Int).Mul(d.getValue(), mul)
	return new(big.Rat).SetFrac(num, oneInt)
}

// Float64 returns the nearest float64 value for d and a bool indicating
// whether f represents d exactly.
// For more details, see the documentation for big.Rat.Float64
func (d Decimal) Float64() (f float64, exact bool) {
	return d.Rat().Float64()
}

// InexactFloat64 returns the nearest float64 value for d.
// It doesn't indicate if the returned value represents d exactly.
func (d Decimal) InexactFloat64() float64 {
	f, _ := d.Float64()
	return f
}

// String returns the string representation of the decimal
// with the fixed point.
//
// Example:
//
//	d := New(-12345, -3)
//	println(d.String())
//
// Output:
//
//	-12.345
func (d Decimal) String() string {
	return d.string(TrimTrailingZeros, UseScientificNotation)
}

// StringFixed returns a rounded fixed-point string with places digits after
// the decimal point.
//
// Example:
//
//	NewFromFloat(0).StringFixed(2) // output: "0.00"
//	NewFromFloat(0).StringFixed(0) // output: "0"
//	NewFromFloat(5.45).StringFixed(0) // output: "5"
//	NewFromFloat(5.45).StringFixed(1) // output: "5.5"
//	NewFromFloat(5.45).StringFixed(2) // output: "5.45"
//	NewFromFloat(5.45).StringFixed(3) // output: "5.450"
//	NewFromFloat(545).StringFixed(-1) // output: "540"
//
// Regardless of the UseScientificNotation option, the returned string will never be in scientific notation.
func (d Decimal) StringFixed(places int32) string {
	rounded := d.Round(places)
	return rounded.string(false, false)
}

// StringFixedBank returns a banker rounded fixed-point string with places digits
// after the decimal point.
//
// Example:
//
//	NewFromFloat(0).StringFixedBank(2) // output: "0.00"
//	NewFromFloat(0).StringFixedBank(0) // output: "0"
//	NewFromFloat(5.45).StringFixedBank(0) // output: "5"
//	NewFromFloat(5.45).StringFixedBank(1) // output: "5.4"
//	NewFromFloat(5.45).StringFixedBank(2) // output: "5.45"
//	NewFromFloat(5.45).StringFixedBank(3) // output: "5.450"
//	NewFromFloat(545).StringFixedBank(-1) // output: "540"
//
// Regardless of the UseScientificNotation option, the returned string will never be in scientific notation.
func (d Decimal) StringFixedBank(places int32) string {
	rounded := d.RoundBank(places)
	return rounded.string(false, false)
}

// StringFixedCash returns a Swedish/Cash rounded fixed-point string. For
// more details see the documentation at function RoundCash.
//
// Regardless of the UseScientificNotation option, the returned string will never be in scientific notation.
func (d Decimal) StringFixedCash(interval uint8) string {
	rounded := d.RoundCash(interval)
	return rounded.string(false, false)
}

// Round rounds the decimal to places decimal places.
// If places < 0, it will round the integer part to the nearest 10^(-places).
//
// Example:
//
//	NewFromFloat(5.45).Round(1).String() // output: "5.5"
//	NewFromFloat(545).Round(-1).String() // output: "550" (with UseScientificNotation false, "5.5E2" if true)
func (d Decimal) Round(places int32) Decimal {
	if d.exp == -places {
		return d
	}
	// truncate to places + 1
	ret := d.rescale(-places - 1)

	// add sign(d) * 0.5
	if ret.value.Sign() < 0 {
		ret.value.Sub(ret.value, fiveInt)
	} else {
		ret.value.Add(ret.value, fiveInt)
	}

	// floor for positive numbers, ceil for negative numbers
	_, m := ret.value.DivMod(ret.value, tenInt, new(big.Int))
	ret.exp++
	if ret.value.Sign() < 0 && m.Cmp(zeroInt) != 0 {
		ret.value.Add(ret.value, oneInt)
	}

	return ret
}

// RoundCeil rounds the decimal towards +infinity.
//
// Example:
//
//	NewFromFloat(545).RoundCeil(-2).String()   // output: "600"
//	NewFromFloat(500).RoundCeil(-2).String()   // output: "500"
//	NewFromFloat(1.1001).RoundCeil(2).String() // output: "1.11"
//	NewFromFloat(-1.454).RoundCeil(1).String() // output: "-1.4"
func (d Decimal) RoundCeil(places int32) Decimal {
	if d.exp >= -places {
		return d
	}

	rescaled := d.rescale(-places)
	if d.Equal(rescaled) {
		return d
	}

	if d.getValue().Sign() > 0 {
		rescaled.value = new(big.Int).Add(rescaled.getValue(), oneInt)
	}

	return rescaled
}

// RoundFloor rounds the decimal towards -infinity.
//
// Example:
//
//	NewFromFloat(545).RoundFloor(-2).String()   // output: "500"
//	NewFromFloat(-500).RoundFloor(-2).String()   // output: "-500"
//	NewFromFloat(1.1001).RoundFloor(2).String() // output: "1.1"
//	NewFromFloat(-1.454).RoundFloor(1).String() // output: "-1.5"
func (d Decimal) RoundFloor(places int32) Decimal {
	if d.exp >= -places {
		return d
	}

	rescaled := d.rescale(-places)
	if d.Equal(rescaled) {
		return d
	}

	if d.getValue().Sign() < 0 {
		rescaled.value = new(big.Int).Sub(rescaled.getValue(), oneInt)
	}

	return rescaled
}

// RoundUp rounds the decimal away from zero.
//
// Example:
//
//	NewFromFloat(545).RoundUp(-2).String()   // output: "600"
//	NewFromFloat(500).RoundUp(-2).String()   // output: "500"
//	NewFromFloat(1.1001).RoundUp(2).String() // output: "1.11"
//	NewFromFloat(-1.454).RoundUp(1).String() // output: "-1.5"
func (d Decimal) RoundUp(places int32) Decimal {
	if d.exp >= -places {
		return d
	}

	rescaled := d.rescale(-places)
	if d.Equal(rescaled) {
		return d
	}

	if d.getValue().Sign() > 0 {
		rescaled.value = new(big.Int).Add(rescaled.getValue(), oneInt)
	} else if d.getValue().Sign() < 0 {
		rescaled.value = new(big.Int).Sub(rescaled.getValue(), oneInt)
	}

	return rescaled
}

// RoundDown rounds the decimal towards zero.
//
// Example:
//
//	NewFromFloat(545).RoundDown(-2).String()   // output: "500"
//	NewFromFloat(-500).RoundDown(-2).String()   // output: "-500"
//	NewFromFloat(1.1001).RoundDown(2).String() // output: "1.1"
//	NewFromFloat(-1.454).RoundDown(1).String() // output: "-1.4"
func (d Decimal) RoundDown(places int32) Decimal {
	if d.exp >= -places {
		return d
	}

	rescaled := d.rescale(-places)
	if d.Equal(rescaled) {
		return d
	}
	return rescaled
}

// RoundBank rounds the decimal to places decimal places.
// If the final digit to round is equidistant from the nearest two integers the
// rounded value is taken as the even number
//
// If places < 0, it will round the integer part to the nearest 10^(-places).
//
// Examples:
//
//	NewFromFloat(5.45).RoundBank(1).String() // output: "5.4"
//	NewFromFloat(545).RoundBank(-1).String() // output: "540"
//	NewFromFloat(5.46).RoundBank(1).String() // output: "5.5"
//	NewFromFloat(546).RoundBank(-1).String() // output: "550"
//	NewFromFloat(5.55).RoundBank(1).String() // output: "5.6"
//	NewFromFloat(555).RoundBank(-1).String() // output: "560"
func (d Decimal) RoundBank(places int32) Decimal {

	round := d.Round(places)
	remainder := d.Sub(round).Abs()

	half := New(5, -places-1)
	if remainder.Cmp(half) == 0 && round.getValue().Bit(0) != 0 {
		if round.getValue().Sign() < 0 {
			round.value = new(big.Int).Add(round.getValue(), oneInt)
		} else {
			round.value = new(big.Int).Sub(round.getValue(), oneInt)
		}
	}

	return round
}

// RoundCash aka Cash/Penny/öre rounding rounds decimal to a specific
// interval. The amount payable for a cash transaction is rounded to the nearest
// multiple of the minimum currency unit available. The following intervals are
// available: 5, 10, 25, 50 and 100; any other number throws a panic.
//
//	  5:   5 cent rounding 3.43 => 3.45
//	 10:  10 cent rounding 3.45 => 3.50 (5 gets rounded up)
//	 25:  25 cent rounding 3.41 => 3.50
//	 50:  50 cent rounding 3.75 => 4.00
//	100: 100 cent rounding 3.50 => 4.00
//
// For more details: https://en.wikipedia.org/wiki/Cash_rounding
func (d Decimal) RoundCash(interval uint8) Decimal {
	var iVal *big.Int
	switch interval {
	case 5:
		iVal = twentyInt
	case 10:
		iVal = tenInt
	case 25:
		iVal = fourInt
	case 50:
		iVal = twoInt
	case 100:
		iVal = oneInt
	default:
		panic(fmt.Sprintf("Decimal does not support this Cash rounding interval `%d`. Supported: 5, 10, 25, 50, 100", interval))
	}
	dVal := Decimal{
		value: iVal,
	}

	// TODO: optimize those calculations to reduce the high allocations (~29 allocs).
	return d.Mul(dVal).Round(0).Div(dVal).Truncate(2)
}

// Floor returns the nearest integer value less than or equal to d.
func (d Decimal) Floor() Decimal {
	if d.exp >= 0 {
		return d
	}

	exp := big.NewInt(10)

	// NOTE(vadim): must negate after casting to prevent int32 overflow
	exp.Exp(exp, big.NewInt(-int64(d.exp)), nil)

	z := new(big.Int).Div(d.getValue(), exp)
	return Decimal{value: z, exp: 0}
}

// Ceil returns the nearest integer value greater than or equal to d.
func (d Decimal) Ceil() Decimal {
	if d.exp >= 0 {
		return d
	}

	exp := big.NewInt(10)

	// NOTE(vadim): must negate after casting to prevent int32 overflow
	exp.Exp(exp, big.NewInt(-int64(d.exp)), nil)

	z, m := new(big.Int).DivMod(d.getValue(), exp, new(big.Int))
	if m.Cmp(zeroInt) != 0 {
		z.Add(z, oneInt)
	}
	return Decimal{value: z, exp: 0}
}

// Truncate truncates off digits from the number, without rounding.
//
// NOTE: precision is the last digit that will not be truncated (must be >= 0).
//
// Example:
//
//	decimal.NewFromString("123.456").Truncate(2).String() // "123.45"
func (d Decimal) Truncate(precision int32) Decimal {
	if precision >= 0 && -precision > d.exp {
		return d.rescale(-precision)
	}
	return d
}

// UnmarshalJSON implements the json.Unmarshaler interface.
func (d *Decimal) UnmarshalJSON(decimalBytes []byte) error {
	if string(decimalBytes) == "null" {
		return nil
	}

	decimal, err := NewFromString(unquoteIfQuoted(string(decimalBytes)))
	*d = decimal
	if err != nil {
		return fmt.Errorf("error decoding string '%s': %s", string(decimalBytes), err)
	}
	return nil
}

// MarshalJSON implements the json.Marshaler interface.
func (d Decimal) MarshalJSON() ([]byte, error) {
	var str string
	if MarshalJSONWithoutQuotes {
		str = d.String()
	} else {
		str = "\"" + d.String() + "\""
	}
	return []byte(str), nil
}

// UnmarshalBinary implements the encoding.BinaryUnmarshaler interface. As a string representation
// is already used when encoding to text, this method stores that string as []byte
func (d *Decimal) UnmarshalBinary(data []byte) error {
	// Verify we have at least 4 bytes for the exponent. The GOB encoded value
	// may be empty.
	if len(data) < 4 {
		return fmt.Errorf("error decoding binary %v: expected at least 4 bytes, got %d", data, len(data))
	}

	// Extract the exponent
	d.exp = int32(binary.BigEndian.Uint32(data[:4]))

	// Extract the value
	d.value = new(big.Int)
	if err := d.value.GobDecode(data[4:]); err != nil {
		return fmt.Errorf("error decoding binary %v: %s", data, err)
	}

	return nil
}

// MarshalBinary implements the encoding.BinaryMarshaler interface.
func (d Decimal) MarshalBinary() (data []byte, err error) {
	// exp is written first, but encode value first to know output size
	var valueData []byte
	if valueData, err = d.getValue().GobEncode(); err != nil {
		return nil, err
	}

	// Write the exponent in front, since it's a fixed size
	expData := make([]byte, 4, len(valueData)+4)
	binary.BigEndian.PutUint32(expData, uint32(d.exp))

	// Return the byte array
	return append(expData, valueData...), nil
}

// Scan implements the sql.Scanner interface for database deserialization.
func (d *Decimal) Scan(value interface{}) error {
	// first try to see if the data is stored in database as a Numeric datatype
	switch v := value.(type) {

	case float32:
		*d = NewFromFloat(float64(v))
		return nil

	case float64:
		// numeric in sqlite3 sends us float64
		*d = NewFromFloat(v)
		return nil

	case int64:
		// at least in sqlite3 when the value is 0 in db, the data is sent
		// to us as an int64 instead of a float64 ...
		*d = New(v, 0)
		return nil

	case uint64:
		// while clickhouse may send 0 in db as uint64
		*d = NewFromUint64(v)
		return nil

	case string:
		var err error
		*d, err = NewFromString(unquoteIfQuoted(v))
		return err

	case []byte:
		var err error
		*d, err = NewFromString(unquoteIfQuoted(string(v)))
		return err

	default:
		return fmt.Errorf("could not convert value '%+v' to any known type", value)
	}
}

// Value implements the driver.Valuer interface for database serialization.
func (d Decimal) Value() (driver.Value, error) {
	return d.String(), nil
}

// UnmarshalText implements the encoding.TextUnmarshaler interface for XML
// deserialization.
func (d *Decimal) UnmarshalText(text []byte) error {
	str := string(text)

	dec, err := NewFromString(str)
	*d = dec
	if err != nil {
		return fmt.Errorf("error decoding string '%s': %s", str, err)
	}

	return nil
}

// MarshalText implements the encoding.TextMarshaler interface for XML
// serialization.
func (d Decimal) MarshalText() (text []byte, err error) {
	return []byte(d.String()), nil
}

// GobEncode implements the gob.GobEncoder interface for gob serialization.
func (d Decimal) GobEncode() ([]byte, error) {
	return d.MarshalBinary()
}

// GobDecode implements the gob.GobDecoder interface for gob serialization.
func (d *Decimal) GobDecode(data []byte) error {
	return d.UnmarshalBinary(data)
}

// DecodeSpanner decodes a Spanner value into a Decimal
func (d *Decimal) DecodeSpanner(val interface{}) error {
	return d.Scan(val)
}

// EncodeSpanner encodes a Decimal into a Spanner value
func (d Decimal) EncodeSpanner() (interface{}, error) {
	return d.String(), nil
}

// StringScaled first scales the decimal then calls .String() on it.
//
// Deprecated: buggy and unintuitive. Use StringFixed instead.
func (d Decimal) StringScaled(exp int32) string {
	return d.rescale(exp).String()
}

func (d Decimal) string(trimTrailingZeros, useScientificNotation bool) string {
	if d.exp == 0 {
		return d.rescale(0).getValue().String()
	}
	if d.exp >= 0 {
		if useScientificNotation {
			return d.ScientificNotationString()
		} else {
			return d.rescale(0).value.String()
		}
	}

	abs := new(big.Int).Abs(d.getValue())
	str := abs.String()

	var intPart, fractionalPart string

	// NOTE(vadim): this cast to int will cause bugs if d.exp == INT_MIN
	// and you are on a 32-bit machine. Won't fix this super-edge case.
	dExpInt := int(d.exp)
	if len(str) > -dExpInt {
		intPart = str[:len(str)+dExpInt]
		fractionalPart = str[len(str)+dExpInt:]
	} else {
		intPart = "0"

		num0s := -dExpInt - len(str)
		fractionalPart = strings.Repeat("0", num0s) + str
	}

	if trimTrailingZeros {
		i := len(fractionalPart) - 1
		for ; i >= 0; i-- {
			if fractionalPart[i] != '0' {
				break
			}
		}
		fractionalPart = fractionalPart[:i+1]
	}

	number := intPart
	if len(fractionalPart) > 0 {
		number += "." + fractionalPart
	}

	if d.getValue().Sign() < 0 {
		return "-" + number
	}

	return number
}

// ScientificNotationString serializes the decimal into standard scientific notation.
//
// The notation is normalized to have one non-zero digit followed by a decimal point and
// the remaining significant digits followed by "E" and the base-10 exponent.
//
// A zero, which has no significant digits, is simply serialized to "0".
func (d Decimal) ScientificNotationString() string {
	exp := int(d.exp)
	intStr := new(big.Int).Abs(d.getValue()).String()
	if intStr == "0" {
		return intStr
	}
	first := intStr[0]
	var remaining string
	if len(intStr) > 1 {
		remaining = "." + intStr[1:]
		exp = exp + len(intStr) - 1
	}
	number := string(first) + remaining + "E" + strconv.Itoa(exp)
	if d.value.Sign() < 0 {
		return "-" + number
	}
	return number
}

// Min returns the smallest Decimal that was passed in the arguments.
//
// To call this function with an array, you must do:
//
//	Min(arr[0], arr[1:]...)
//
// This makes it harder to accidentally call Min with 0 arguments.
func Min(first Decimal, rest ...Decimal) Decimal {
	ans := first
	for _, item := range rest {
		if item.Cmp(ans) < 0 {
			ans = item
		}
	}
	return ans
}

// Max returns the largest Decimal that was passed in the arguments.
//
// To call this function with an array, you must do:
//
//	Max(arr[0], arr[1:]...)
//
// This makes it harder to accidentally call Max with 0 arguments.
func Max(first Decimal, rest ...Decimal) Decimal {
	ans := first
	for _, item := range rest {
		if item.Cmp(ans) > 0 {
			ans = item
		}
	}
	return ans
}

// Sum returns the combined total of the provided first and rest Decimals
func Sum(first Decimal, rest ...Decimal) Decimal {
	total := first
	for _, item := range rest {
		total = total.Add(item)
	}

	return total
}

// Avg returns the average value of the provided first and rest Decimals
func Avg(first Decimal, rest ...Decimal) Decimal {
	count := New(int64(len(rest)+1), 0)
	sum := Sum(first, rest...)
	return sum.Div(count)
}

// RescalePair rescales two decimals to common exponential value (minimal exp of both decimals)
func RescalePair(d1 Decimal, d2 Decimal) (Decimal, Decimal) {
	if d1.exp < d2.exp {
		return d1, d2.rescale(d1.exp)
	} else if d1.exp > d2.exp {
		return d1.rescale(d2.exp), d2
	}

	return d1, d2
}

func unquoteIfQuoted(value string) string {
	// If the amount is quoted, strip the quotes
	if len(value) > 2 && value[0] == '"' && value[len(value)-1] == '"' {
		return value[1 : len(value)-1]
	}

	return value
}

// NullDecimal represents a nullable decimal with compatibility for
// scanning null values from the database.
type NullDecimal struct {
	Decimal Decimal
	Valid   bool
}

func NewNullDecimal(d Decimal) NullDecimal {
	return NullDecimal{
		Decimal: d,
		Valid:   true,
	}
}

// Scan implements the sql.Scanner interface for database deserialization.
func (d *NullDecimal) Scan(value interface{}) error {
	if value == nil {
		d.Valid = false
		return nil
	}
	d.Valid = true
	return d.Decimal.Scan(value)
}

// Value implements the driver.Valuer interface for database serialization.
func (d NullDecimal) Value() (driver.Value, error) {
	if !d.Valid {
		return nil, nil
	}
	return d.Decimal.Value()
}

// UnmarshalJSON implements the json.Unmarshaler interface.
func (d *NullDecimal) UnmarshalJSON(decimalBytes []byte) error {
	if string(decimalBytes) == "null" {
		d.Valid = false
		return nil
	}
	d.Valid = true
	return d.Decimal.UnmarshalJSON(decimalBytes)
}

// MarshalJSON implements the json.Marshaler interface.
func (d NullDecimal) MarshalJSON() ([]byte, error) {
	if !d.Valid {
		return []byte("null"), nil
	}
	return d.Decimal.MarshalJSON()
}

// UnmarshalText implements the encoding.TextUnmarshaler interface for XML
// deserialization
func (d *NullDecimal) UnmarshalText(text []byte) error {
	str := string(text)

	// check for empty XML or XML without body e.g., <tag></tag>
	if str == "" {
		d.Valid = false
		return nil
	}
	if err := d.Decimal.UnmarshalText(text); err != nil {
		d.Valid = false
		return err
	}
	d.Valid = true
	return nil
}

// MarshalText implements the encoding.TextMarshaler interface for XML
// serialization.
func (d NullDecimal) MarshalText() (text []byte, err error) {
	if !d.Valid {
		return []byte{}, nil
	}
	return d.Decimal.MarshalText()
}

// DecodeSpanner decodes a Spanner value into a Decimal
func (d *NullDecimal) DecodeSpanner(value interface{}) error {
	switch t := value.(type) {
	case nil:
		d.Valid = false
		return nil
	case *string:
		if t == nil {
			d.Valid = false
			return nil
		}
		value = *t
	}
	d.Valid = true

	return d.Decimal.Scan(value)
}

// EncodeSpanner encodes a Decimal into a Spanner value
func (d NullDecimal) EncodeSpanner() (interface{}, error) {
	if !d.Valid {
		return nil, nil
	}
	return d.Decimal.String(), nil
}

// Trig functions

// Atan returns the arctangent, in radians, of x.
func (d Decimal) Atan() Decimal {
	if d.Equal(NewFromFloat(0.0)) {
		return d
	}
	if d.GreaterThan(NewFromFloat(0.0)) {
		return d.satan()
	}
	return d.Neg().satan().Neg()
}

func (d Decimal) xatan() Decimal {
	P0 := NewFromFloat(-8.750608600031904122785e-01)
	P1 := NewFromFloat(-1.615753718733365076637e+01)
	P2 := NewFromFloat(-7.500855792314704667340e+01)
	P3 := NewFromFloat(-1.228866684490136173410e+02)
	P4 := NewFromFloat(-6.485021904942025371773e+01)
	Q0 := NewFromFloat(2.485846490142306297962e+01)
	Q1 := NewFromFloat(1.650270098316988542046e+02)
	Q2 := NewFromFloat(4.328810604912902668951e+02)
	Q3 := NewFromFloat(4.853903996359136964868e+02)
	Q4 := NewFromFloat(1.945506571482613964425e+02)
	z := d.Mul(d)
	b1 := P0.Mul(z).Add(P1).Mul(z).Add(P2).Mul(z).Add(P3).Mul(z).Add(P4).Mul(z)
	b2 := z.Add(Q0).Mul(z).Add(Q1).Mul(z).Add(Q2).Mul(z).Add(Q3).Mul(z).Add(Q4)
	z = b1.Div(b2)
	z = d.Mul(z).Add(d)
	return z
}

// satan reduces its argument (known to be positive)
// to the range [0, 0.66] and calls xatan.
func (d Decimal) satan() Decimal {
	Morebits := NewFromFloat(6.123233995736765886130e-17) // pi/2 = PIO2 + Morebits
	Tan3pio8 := NewFromFloat(2.41421356237309504880)      // tan(3*pi/8)
	pi := NewFromFloat(3.14159265358979323846264338327950288419716939937510582097494459)

	if d.LessThanOrEqual(NewFromFloat(0.66)) {
		return d.xatan()
	}
	if d.GreaterThan(Tan3pio8) {
		return pi.Div(NewFromFloat(2.0)).Sub(NewFromFloat(1.0).Div(d).xatan()).Add(Morebits)
	}
	return pi.Div(NewFromFloat(4.0)).Add((d.Sub(NewFromFloat(1.0)).Div(d.Add(NewFromFloat(1.0)))).xatan()).Add(NewFromFloat(0.5).Mul(Morebits))
}

// sin coefficients
var _sin = [...]Decimal{
	NewFromFloat(1.58962301576546568060e-10), // 0x3de5d8fd1fd19ccd
	NewFromFloat(-2.50507477628578072866e-8), // 0xbe5ae5e5a9291f5d
	NewFromFloat(2.75573136213857245213e-6),  // 0x3ec71de3567d48a1
	NewFromFloat(-1.98412698295895385996e-4), // 0xbf2a01a019bfdf03
	NewFromFloat(8.33333333332211858878e-3),  // 0x3f8111111110f7d0
	NewFromFloat(-1.66666666666666307295e-1), // 0xbfc5555555555548
}

// Sin returns the sine of the radian argument x.
func (d Decimal) Sin() Decimal {
	PI4A := NewFromFloat(7.85398125648498535156e-1)                             // 0x3fe921fb40000000, Pi/4 split into three parts
	PI4B := NewFromFloat(3.77489470793079817668e-8)                             // 0x3e64442d00000000,
	PI4C := NewFromFloat(2.69515142907905952645e-15)                            // 0x3ce8469898cc5170,
	M4PI := NewFromFloat(1.273239544735162542821171882678754627704620361328125) // 4/pi

	if d.Equal(NewFromFloat(0.0)) {
		return d
	}
	// make argument positive but save the sign
	sign := false
	if d.LessThan(NewFromFloat(0.0)) {
		d = d.Neg()
		sign = true
	}

	j := d.Mul(M4PI).IntPart()    // integer part of x/(Pi/4), as integer for tests on the phase angle
	y := NewFromFloat(float64(j)) // integer part of x/(Pi/4), as float

	// map zeros to origin
	if j&1 == 1 {
		j++
		y = y.Add(NewFromFloat(1.0))
	}
	j &= 7 // octant modulo 2Pi radians (360 degrees)
	// reflect in x axis
	if j > 3 {
		sign = !sign
		j -= 4
	}
	z := d.Sub(y.Mul(PI4A)).Sub(y.Mul(PI4B)).Sub(y.Mul(PI4C)) // Extended precision modular arithmetic
	zz := z.Mul(z)

	if j == 1 || j == 2 {
		w := zz.Mul(zz).Mul(_cos[0].Mul(zz).Add(_cos[1]).Mul(zz).Add(_cos[2]).Mul(zz).Add(_cos[3]).Mul(zz).Add(_cos[4]).Mul(zz).Add(_cos[5]))
		y = NewFromFloat(1.0).Sub(NewFromFloat(0.5).Mul(zz)).Add(w)
	} else {
		y = z.Add(z.Mul(zz).Mul(_sin[0].Mul(zz).Add(_sin[1]).Mul(zz).Add(_sin[2]).Mul(zz).Add(_sin[3]).Mul(zz).Add(_sin[4]).Mul(zz).Add(_sin[5])))
	}
	if sign {
		y = y.Neg()
	}
	return y
}

// cos coefficients
var _cos = [...]Decimal{
	NewFromFloat(-1.13585365213876817300e-11), // 0xbda8fa49a0861a9b
	NewFromFloat(2.08757008419747316778e-9),   // 0x3e21ee9d7b4e3f05
	NewFromFloat(-2.75573141792967388112e-7),  // 0xbe927e4f7eac4bc6
	NewFromFloat(2.48015872888517045348e-5),   // 0x3efa01a019c844f5
	NewFromFloat(-1.38888888888730564116e-3),  // 0xbf56c16c16c14f91
	NewFromFloat(4.16666666666665929218e-2),   // 0x3fa555555555554b
}

// Cos returns the cosine of the radian argument x.
func (d Decimal) Cos() Decimal {

	PI4A := NewFromFloat(7.85398125648498535156e-1)                             // 0x3fe921fb40000000, Pi/4 split into three parts
	PI4B := NewFromFloat(3.77489470793079817668e-8)                             // 0x3e64442d00000000,
	PI4C := NewFromFloat(2.69515142907905952645e-15)                            // 0x3ce8469898cc5170,
	M4PI := NewFromFloat(1.273239544735162542821171882678754627704620361328125) // 4/pi

	// make argument positive
	sign := false
	if d.LessThan(NewFromFloat(0.0)) {
		d = d.Neg()
	}

	j := d.Mul(M4PI).IntPart()    // integer part of x/(Pi/4), as integer for tests on the phase angle
	y := NewFromFloat(float64(j)) // integer part of x/(Pi/4), as float

	// map zeros to origin
	if j&1 == 1 {
		j++
		y = y.Add(NewFromFloat(1.0))
	}
	j &= 7 // octant modulo 2Pi radians (360 degrees)
	// reflect in x axis
	if j > 3 {
		sign = !sign
		j -= 4
	}
	if j > 1 {
		sign = !sign
	}

	z := d.Sub(y.Mul(PI4A)).Sub(y.Mul(PI4B)).Sub(y.Mul(PI4C)) // Extended precision modular arithmetic
	zz := z.Mul(z)

	if j == 1 || j == 2 {
		y = z.Add(z.Mul(zz).Mul(_sin[0].Mul(zz).Add(_sin[1]).Mul(zz).Add(_sin[2]).Mul(zz).Add(_sin[3]).Mul(zz).Add(_sin[4]).Mul(zz).Add(_sin[5])))
	} else {
		w := zz.Mul(zz).Mul(_cos[0].Mul(zz).Add(_cos[1]).Mul(zz).Add(_cos[2]).Mul(zz).Add(_cos[3]).Mul(zz).Add(_cos[4]).Mul(zz).Add(_cos[5]))
		y = NewFromFloat(1.0).Sub(NewFromFloat(0.5).Mul(zz)).Add(w)
	}
	if sign {
		y = y.Neg()
	}
	return y
}

var _tanP = [...]Decimal{
	NewFromFloat(-1.30936939181383777646e+4), // 0xc0c992d8d24f3f38
	NewFromFloat(1.15351664838587416140e+6),  // 0x413199eca5fc9ddd
	NewFromFloat(-1.79565251976484877988e+7), // 0xc1711fead3299176
}
var _tanQ = [...]Decimal{
	NewFromFloat(1.00000000000000000000e+0),
	NewFromFloat(1.36812963470692954678e+4),  //0x40cab8a5eeb36572
	NewFromFloat(-1.32089234440210967447e+6), //0xc13427bc582abc96
	NewFromFloat(2.50083801823357915839e+7),  //0x4177d98fc2ead8ef
	NewFromFloat(-5.38695755929454629881e+7), //0xc189afe03cbe5a31
}

// Tan returns the tangent of the radian argument x.
func (d Decimal) Tan() Decimal {

	PI4A := NewFromFloat(7.85398125648498535156e-1)                             // 0x3fe921fb40000000, Pi/4 split into three parts
	PI4B := NewFromFloat(3.77489470793079817668e-8)                             // 0x3e64442d00000000,
	PI4C := NewFromFloat(2.69515142907905952645e-15)                            // 0x3ce8469898cc5170,
	M4PI := NewFromFloat(1.273239544735162542821171882678754627704620361328125) // 4/pi

	if d.Equal(NewFromFloat(0.0)) {
		return d
	}

	// make argument positive but save the sign
	sign := false
	if d.LessThan(NewFromFloat(0.0)) {
		d = d.Neg()
		sign = true
	}

	j := d.Mul(M4PI).IntPart()    // integer part of x/(Pi/4), as integer for tests on the phase angle
	y := NewFromFloat(float64(j)) // integer part of x/(Pi/4), as float

	// map zeros to origin
	if j&1 == 1 {
		j++
		y = y.Add(NewFromFloat(1.0))
	}

	z := d.Sub(y.Mul(PI4A)).Sub(y.Mul(PI4B)).Sub(y.Mul(PI4C)) // Extended precision modular arithmetic
	zz := z.Mul(z)

	if zz.GreaterThan(NewFromFloat(1e-14)) {
		w := zz.Mul(_tanP[0].Mul(zz).Add(_tanP[1]).Mul(zz).Add(_tanP[2]))
		x := zz.Add(_tanQ[1]).Mul(zz).Add(_tanQ[2]).Mul(zz).Add(_tanQ[3]).Mul(zz).Add(_tanQ[4])
		y = z.Add(z.Mul(w.Div(x)))
	} else {
		y = z
	}
	if j&2 == 2 {
		y = NewFromFloat(-1.0).Div(y)
	}
	if sign {
		y = y.Neg()
	}
	return y
}
```

## File: `decimal_bench_test.go`
```go
package decimal

import (
	"fmt"
	"math"
	"math/big"
	"math/rand"
	"sort"
	"strconv"
	"testing"
)

type DecimalSlice []Decimal

func (p DecimalSlice) Len() int           { return len(p) }
func (p DecimalSlice) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func (p DecimalSlice) Less(i, j int) bool { return p[i].Cmp(p[j]) < 0 }

func BenchmarkNewFromFloatWithExponent(b *testing.B) {
	rng := rand.New(rand.NewSource(0xdead1337))
	in := make([]float64, b.N)
	for i := range in {
		in[i] = rng.NormFloat64() * 10e20
	}
	b.ReportAllocs()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		in := rng.NormFloat64() * 10e20
		_ = NewFromFloatWithExponent(in, math.MinInt32)
	}
}

func BenchmarkNewFromFloat(b *testing.B) {
	rng := rand.New(rand.NewSource(0xdead1337))
	in := make([]float64, b.N)
	for i := range in {
		in[i] = rng.NormFloat64() * 10e20
	}
	b.ReportAllocs()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		_ = NewFromFloat(in[i])
	}
}

func BenchmarkNewFromStringFloat(b *testing.B) {
	rng := rand.New(rand.NewSource(0xdead1337))
	in := make([]float64, b.N)
	for i := range in {
		in[i] = rng.NormFloat64() * 10e20
	}
	b.ReportAllocs()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		in := strconv.FormatFloat(in[i], 'f', -1, 64)
		_, _ = NewFromString(in)
	}
}

func Benchmark_FloorFast(b *testing.B) {
	input := New(200, 2)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		input.Floor()
	}
}

func Benchmark_FloorRegular(b *testing.B) {
	input := New(200, -2)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		input.Floor()
	}
}

func Benchmark_DivideOriginal(b *testing.B) {
	tcs := createDivTestCases()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		for _, tc := range tcs {
			d := tc.d
			if sign(tc.d2) == 0 {
				continue
			}
			d2 := tc.d2
			prec := tc.prec
			a := d.DivOld(d2, int(prec))
			if sign(a) > 2 {
				panic("dummy panic")
			}
		}
	}
}

func Benchmark_DivideNew(b *testing.B) {
	tcs := createDivTestCases()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		for _, tc := range tcs {
			d := tc.d
			if sign(tc.d2) == 0 {
				continue
			}
			d2 := tc.d2
			prec := tc.prec
			a := d.DivRound(d2, prec)
			if sign(a) > 2 {
				panic("dummy panic")
			}
		}
	}
}

func BenchmarkDecimal_RoundCash_Five(b *testing.B) {
	const want = "3.50"
	for i := 0; i < b.N; i++ {
		val := New(3478, -3)
		if have := val.StringFixedCash(5); have != want {
			b.Fatalf("\nHave: %q\nWant: %q", have, want)
		}
	}
}

func numDigits(b *testing.B, want int, val Decimal) {
	b.Helper()
	for i := 0; i < b.N; i++ {
		if have := val.NumDigits(); have != want {
			b.Fatalf("\nHave: %d\nWant: %d", have, want)
		}
	}
}

func BenchmarkDecimal_NumDigits10(b *testing.B) {
	numDigits(b, 10, New(3478512345, -3))
}

func BenchmarkDecimal_NumDigits100(b *testing.B) {
	s := make([]byte, 102)
	for i := range s {
		s[i] = byte('0' + i%10)
	}
	s[0] = '-'
	s[100] = '.'
	d, err := NewFromString(string(s))
	if err != nil {
		b.Log(d)
		b.Error(err)
	}
	numDigits(b, 100, d)
}

func Benchmark_Cmp(b *testing.B) {
	decimals := DecimalSlice([]Decimal{})
	for i := 0; i < 1000000; i++ {
		decimals = append(decimals, New(int64(i), 0))
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		sort.Sort(decimals)
	}
}

func BenchmarkDecimal_Add_different_precision(b *testing.B) {
	d1 := NewFromFloat(1000.123)
	d2 := NewFromFloat(500).Mul(NewFromFloat(0.12))

	b.ReportAllocs()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		d1.Add(d2)
	}
}

func BenchmarkDecimal_Sub_different_precision(b *testing.B) {
	d1 := NewFromFloat(1000.123)
	d2 := NewFromFloat(500).Mul(NewFromFloat(0.12))

	b.ReportAllocs()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		d1.Sub(d2)
	}
}

func BenchmarkDecimal_Add_same_precision(b *testing.B) {
	d1 := NewFromFloat(1000.123)
	d2 := NewFromFloat(500.123)

	b.ReportAllocs()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		d1.Add(d2)
	}
}

func BenchmarkDecimal_Sub_same_precision(b *testing.B) {
	d1 := NewFromFloat(1000.123)
	d2 := NewFromFloat(500.123)

	b.ReportAllocs()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		d1.Add(d2)
	}
}

func BenchmarkDecimal_IsInteger(b *testing.B) {
	d := RequireFromString("12.000")

	b.ReportAllocs()
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		d.IsInteger()
	}
}

func BenchmarkDecimal_Pow(b *testing.B) {
	d1 := RequireFromString("5.2")
	d2 := RequireFromString("6.3")

	for i := 0; i < b.N; i++ {
		d1.Pow(d2)
	}
}

func BenchmarkDecimal_PowWithPrecision(b *testing.B) {
	d1 := RequireFromString("5.2")
	d2 := RequireFromString("6.3")

	for i := 0; i < b.N; i++ {
		_, _ = d1.PowWithPrecision(d2, 8)
	}
}
func BenchmarkDecimal_PowInt32(b *testing.B) {
	d1 := RequireFromString("5.2")
	d2 := int32(10)

	for i := 0; i < b.N; i++ {
		_, _ = d1.PowInt32(d2)
	}
}

func BenchmarkDecimal_PowBigInt(b *testing.B) {
	d1 := RequireFromString("5.2")
	d2 := big.NewInt(10)

	for i := 0; i < b.N; i++ {
		_, _ = d1.PowBigInt(d2)
	}
}

func BenchmarkDecimal_NewFromString(b *testing.B) {
	count := 72
	prices := make([]string, 0, count)
	for i := 1; i <= count; i++ {
		prices = append(prices, fmt.Sprintf("%d.%d", i*100, i))
	}

	b.ReportAllocs()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		for _, p := range prices {
			d, err := NewFromString(p)
			if err != nil {
				b.Log(d)
				b.Error(err)
			}
		}
	}
}

func BenchmarkDecimal_NewFromString_large_number(b *testing.B) {
	count := 72
	prices := make([]string, 0, count)
	for i := 1; i <= count; i++ {
		prices = append(prices, "9323372036854775807.9223372036854775807")
	}

	b.ReportAllocs()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		for _, p := range prices {
			d, err := NewFromString(p)
			if err != nil {
				b.Log(d)
				b.Error(err)
			}
		}
	}
}

func BenchmarkDecimal_ExpHullAbraham(b *testing.B) {
	b.ResetTimer()

	d := RequireFromString("30.412346346346")

	b.ReportAllocs()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_, _ = d.ExpHullAbrham(10)
	}
}

func BenchmarkDecimal_ExpTaylor(b *testing.B) {
	b.ResetTimer()

	d := RequireFromString("30.412346346346")

	b.ReportAllocs()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_, _ = d.ExpTaylor(10)
	}
}

func BenchmarkDecimal_UnmarshalJSON(b *testing.B) {
	b.ResetTimer()

	bstr := []byte("1234.56789")

	b.ReportAllocs()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_ = (&Decimal{}).UnmarshalJSON(bstr)
	}
}
```

## File: `decimal_go124_test.go`
```go
//go:build go1.24
// +build go1.24

package decimal

import (
	"encoding/json"
	"testing"
)

// `omitzero` is supported by encoding/json starting in Go 1.24.
// Keep this test in a go1.24-gated file so older CI jobs skip it.
func TestJSONOmitZeroTag(t *testing.T) {
	type Nested struct {
		Amount Decimal `json:"amount,omitzero"`
	}

	type Parent struct {
		Nested Nested `json:"nested,omitzero"`
	}

	tests := []struct {
		name     string
		parent   Parent
		expected string
	}{
		{
			name: "Decimal{} empty value",
			parent: Parent{
				Nested: Nested{
					Amount: Decimal{},
				},
			},
			expected: "{}",
		},
		{
			name: "Zero constant",
			parent: Parent{
				Nested: Nested{
					Amount: Zero,
				},
			},
			expected: "{}",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			b, err := json.Marshal(tt.parent)
			if err != nil {
				t.Fatal(err)
			}
			if string(b) != tt.expected {
				t.Errorf("expected %s, got %s", tt.expected, string(b))
			}
		})
	}
}
```

## File: `decimal_test.go`
```go
package decimal

import (
	"database/sql/driver"
	"encoding/json"
	"encoding/xml"
	"fmt"
	"math"
	"math/big"
	"math/rand"
	"reflect"
	"regexp"
	"strconv"
	"strings"
	"testing"
	"testing/quick"
	"time"
)

type testEnt struct {
	float   float64
	short   string
	exact   string
	inexact string
}

var testTable = []*testEnt{
	{3.141592653589793, "3.141592653589793", "", "3.14159265358979300000000000000000000000000000000000004"},
	{3, "3", "", "3.0000000000000000000000002"},
	{1234567890123456, "1234567890123456", "", "1234567890123456.00000000000000002"},
	{1234567890123456000, "1234567890123456000", "", "1234567890123456000.0000000000000008"},
	{1234.567890123456, "1234.567890123456", "", "1234.5678901234560000000000000009"},
	{.1234567890123456, "0.1234567890123456", "", "0.12345678901234560000000000006"},
	{0, "0", "", "0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"},
	{.1111111111111110, "0.111111111111111", "", "0.111111111111111000000000000000009"},
	{.1111111111111111, "0.1111111111111111", "", "0.111111111111111100000000000000000000023423545644534234"},
	{.1111111111111119, "0.1111111111111119", "", "0.111111111111111900000000000000000000000000000000000134123984192834"},
	{.000000000000000001, "0.000000000000000001", "", "0.00000000000000000100000000000000000000000000000000012341234"},
	{.000000000000000002, "0.000000000000000002", "", "0.0000000000000000020000000000000000000012341234123"},
	{.000000000000000003, "0.000000000000000003", "", "0.00000000000000000299999999999999999999999900000000000123412341234"},
	{.000000000000000005, "0.000000000000000005", "", "0.00000000000000000500000000000000000023412341234"},
	{.000000000000000008, "0.000000000000000008", "", "0.0000000000000000080000000000000000001241234432"},
	{.1000000000000001, "0.1000000000000001", "", "0.10000000000000010000000000000012341234"},
	{.1000000000000002, "0.1000000000000002", "", "0.10000000000000020000000000001234123412"},
	{.1000000000000003, "0.1000000000000003", "", "0.1000000000000003000000000000001234123412"},
	{.1000000000000005, "0.1000000000000005", "", "0.1000000000000005000000000000000006441234"},
	{.1000000000000008, "0.1000000000000008", "", "0.100000000000000800000000000000000009999999999999999999999999999"},
	{1e25, "10000000000000000000000000", "", ""},
	{1.5e14, "150000000000000", "", ""},
	{1.5e15, "1500000000000000", "", ""},
	{1.5e16, "15000000000000000", "", ""},
	{1.0001e25, "10001000000000000000000000", "", ""},
	{1.0001000000000000033e25, "10001000000000000000000000", "", ""},
	{2e25, "20000000000000000000000000", "", ""},
	{4e25, "40000000000000000000000000", "", ""},
	{8e25, "80000000000000000000000000", "", ""},
	{1e250, "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", "", ""},
	{2e250, "20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", "", ""},
	{math.MaxInt64, strconv.FormatFloat(float64(math.MaxInt64), 'f', -1, 64), "", strconv.FormatInt(math.MaxInt64, 10)},
	{1.29067116156722e-309, "0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000129067116156722", "", "0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001290671161567218558822290567835270536800098852722416870074139002112543896676308448335063375297788379444685193974290737962187240854947838776604607190387984577130572928111657710645015086812756013489109884753559084166516937690932698276436869274093950997935137476803610007959500457935217950764794724766740819156974617155861568214427828145972181876775307023388139991104942469299524961281641158436752347582767153796914843896176260096039358494077706152272661453132497761307744086665088096215425146090058519888494342944692629602847826300550628670375451325582843627504604013541465361435761965354140678551369499812124085312128659002910905639984075064968459581691226705666561364681985266583563078466180095375402399087817404368974165082030458595596655868575908243656158447265625000000000000000000000000000000000000004440000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"},
	// go Issue 29491.
	{498484681984085570, "498484681984085570", "", ""},
	{5.8339553793802237e+23, "583395537938022370000000", "", ""},
}

var testTableScientificNotation = map[string]string{
	"1e9":        "1000000000",
	"2.41E-3":    "0.00241",
	"24.2E-4":    "0.00242",
	"243E-5":     "0.00243",
	"1e-5":       "0.00001",
	"245E3":      "245000",
	"1.2345E-1":  "0.12345",
	"0e5":        "0",
	"0e-5":       "0",
	"0.e0":       "0",
	".0e0":       "0",
	"123.456e0":  "123.456",
	"123.456e2":  "12345.6",
	"123.456e10": "1234560000000",
}

var testMalformedDecimalStrings = map[string]error{
	"1ee10":     fmt.Errorf("can't convert %s to decimal: multiple 'E' characters found", "1ee10"),
	"123.45.66": fmt.Errorf("can't convert %s to decimal: too many .s", "123.45.66"),
}

func init() {
	for _, s := range testTable {
		s.exact = strconv.FormatFloat(s.float, 'f', 1500, 64)
		if strings.ContainsRune(s.exact, '.') {
			s.exact = strings.TrimRight(s.exact, "0")
			s.exact = strings.TrimRight(s.exact, ".")
		}
	}

	// add negatives
	withNeg := testTable[:]
	for _, s := range testTable {
		if s.float > 0 && s.short != "0" && s.exact != "0" {
			withNeg = append(withNeg, &testEnt{-s.float, "-" + s.short, "-" + s.exact, "-" + s.inexact})
		}
	}
	testTable = withNeg

	for e, s := range testTableScientificNotation {
		if string(e[0]) != "-" && s != "0" {
			testTableScientificNotation["-"+e] = "-" + s
		}
	}
}

func TestNewFromFloat(t *testing.T) {
	for _, x := range testTable {
		s := x.short
		d := NewFromFloat(x.float)
		if d.String() != s {
			t.Errorf("expected %s, got %s (float: %v) (%s, %d)",
				s, d.String(), x.float,
				d.value.String(), d.exp)
		}
	}

	shouldPanicOn := []float64{
		math.NaN(),
		math.Inf(1),
		math.Inf(-1),
	}

	for _, n := range shouldPanicOn {
		var d Decimal
		if !didPanic(func() { d = NewFromFloat(n) }) {
			t.Fatalf("Expected panic when creating a Decimal from %v, got %v instead", n, d.String())
		}
	}
}

func TestNewFromFloatRandom(t *testing.T) {
	n := 0
	rng := rand.New(rand.NewSource(0xdead1337))
	for {
		n++
		if n == 10 {
			break
		}
		in := (rng.Float64() - 0.5) * math.MaxFloat64 * 2
		want, err := NewFromString(strconv.FormatFloat(in, 'f', -1, 64))
		if err != nil {
			t.Error(err)
			continue
		}
		got := NewFromFloat(in)
		if !want.Equal(got) {
			t.Errorf("in: %v, expected %s (%s, %d), got %s (%s, %d) ",
				in, want.String(), want.value.String(), want.exp,
				got.String(), got.value.String(), got.exp)
		}
	}
}

func TestNewFromFloatQuick(t *testing.T) {
	err := quick.Check(func(f float64) bool {
		want, werr := NewFromString(strconv.FormatFloat(f, 'f', -1, 64))
		if werr != nil {
			return true
		}
		got := NewFromFloat(f)
		return got.Equal(want)
	}, &quick.Config{})
	if err != nil {
		t.Error(err)
	}
}

func TestNewFromFloat32Random(t *testing.T) {
	n := 0
	rng := rand.New(rand.NewSource(0xdead1337))
	for {
		n++
		if n == 10 {
			break
		}
		in := float32((rng.Float64() - 0.5) * math.MaxFloat32 * 2)
		want, err := NewFromString(strconv.FormatFloat(float64(in), 'f', -1, 32))
		if err != nil {
			t.Error(err)
			continue
		}
		got := NewFromFloat32(in)
		if !want.Equal(got) {
			t.Errorf("in: %v, expected %s (%s, %d), got %s (%s, %d) ",
				in, want.String(), want.value.String(), want.exp,
				got.String(), got.value.String(), got.exp)
		}
	}
}

func TestNewFromFloat32Quick(t *testing.T) {
	err := quick.Check(func(f float32) bool {
		want, werr := NewFromString(strconv.FormatFloat(float64(f), 'f', -1, 32))
		if werr != nil {
			return true
		}
		got := NewFromFloat32(f)
		return got.Equal(want)
	}, &quick.Config{})
	if err != nil {
		t.Error(err)
	}
}

func TestNewFromString(t *testing.T) {
	for _, x := range testTable {
		s := x.short
		d, err := NewFromString(s)
		if err != nil {
			t.Errorf("error while parsing %s", s)
		} else if d.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, d.String(),
				d.value.String(), d.exp)
		}
	}

	for _, x := range testTable {
		s := x.exact
		d, err := NewFromString(s)
		if err != nil {
			t.Errorf("error while parsing %s", s)
		} else if d.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, d.String(),
				d.value.String(), d.exp)
		}
	}

	for e, s := range testTableScientificNotation {
		d, err := NewFromString(e)
		if err != nil {
			t.Errorf("error while parsing %s", e)
		} else if d.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, d.String(),
				d.value.String(), d.exp)
		}
	}

	for s, e := range testMalformedDecimalStrings {
		_, err := NewFromString(s)
		if err == nil {
			t.Errorf("expected an error, got nil %s", s)
		} else if err.Error() != e.Error() {
			t.Errorf("expected %v error, got %v", e, err)
		}
	}
}

func TestNewFromFormattedString(t *testing.T) {
	for _, testCase := range []struct {
		Formatted string
		Expected  string
		ReplRegex *regexp.Regexp
	}{
		{"$10.99", "10.99", regexp.MustCompile("[$]")},
		{"$ 12.1", "12.1", regexp.MustCompile("[$\\s]")},
		{"$61,690.99", "61690.99", regexp.MustCompile("[$,]")},
		{"1_000_000.00", "1000000.00", regexp.MustCompile("[_]")},
		{"41,410.00", "41410.00", regexp.MustCompile("[,]")},
		{"5200 USD", "5200", regexp.MustCompile("[USD\\s]")},
	} {
		dFormatted, err := NewFromFormattedString(testCase.Formatted, testCase.ReplRegex)
		if err != nil {
			t.Fatal(err)
		}

		dExact, err := NewFromString(testCase.Expected)
		if err != nil {
			t.Fatal(err)
		}

		if !dFormatted.Equal(dExact) {
			t.Errorf("expect %s, got %s", dExact, dFormatted)
		}
	}
}

func TestFloat64(t *testing.T) {
	for _, x := range testTable {
		if x.inexact == "" || x.inexact == "-" {
			continue
		}
		s := x.exact
		d, err := NewFromString(s)
		if err != nil {
			t.Errorf("error while parsing %s", s)
		} else if f, exact := d.Float64(); !exact || f != x.float {
			t.Errorf("cannot represent exactly %s", s)
		}
		s = x.inexact
		d, err = NewFromString(s)
		if err != nil {
			t.Errorf("error while parsing %s", s)
		} else if f, exact := d.Float64(); exact || f != x.float {
			t.Errorf("%s should be represented inexactly", s)
		}
	}
}

func TestNewFromStringErrs(t *testing.T) {
	tests := []string{
		"",
		"qwert",
		"-",
		".",
		"-.",
		".-",
		"234-.56",
		"234-56",
		"2-",
		"..",
		"2..",
		"..2",
		".5.2",
		"8..2",
		"8.1.",
		"1e",
		"1-e",
		"1e9e",
		"1ee9",
		"1ee",
		"1eE",
		"1e-",
		"1e-.",
		"1e1.2",
		"123.456e1.3",
		"1e-1.2",
		"123.456e-1.3",
		"123.456Easdf",
		"123.456e" + strconv.FormatInt(math.MinInt64, 10),
		"123.456e" + strconv.FormatInt(math.MinInt32, 10),
		"512.99 USD",
		"$99.99",
		"51,850.00",
		"20_000_000.00",
		"$20_000_000.00",
	}

	for _, s := range tests {
		_, err := NewFromString(s)

		if err == nil {
			t.Errorf("error expected when parsing %s", s)
		}
	}
}

func TestNewFromStringDeepEquals(t *testing.T) {
	type StrCmp struct {
		str1     string
		str2     string
		expected bool
	}
	tests := []StrCmp{
		{"1", "1", true},
		{"1.0", "1.0", true},
		{"10", "10.0", false},
		{"1.1", "1.10", false},
		{"1.001", "1.01", false},
	}

	for _, cmp := range tests {
		d1, err1 := NewFromString(cmp.str1)
		d2, err2 := NewFromString(cmp.str2)

		if err1 != nil || err2 != nil {
			t.Errorf("error parsing strings to decimals")
		}

		if reflect.DeepEqual(d1, d2) != cmp.expected {
			t.Errorf("comparison result is different from expected results for %s and %s",
				cmp.str1, cmp.str2)
		}
	}
}

func TestRequireFromString(t *testing.T) {
	s := "1.23"
	defer func() {
		err := recover()
		if err != nil {
			t.Errorf("error while parsing %s", s)
		}
	}()

	d := RequireFromString(s)
	if d.String() != s {
		t.Errorf("expected %s, got %s (%s, %d)",
			s, d.String(),
			d.value.String(), d.exp)
	}
}

func TestRequireFromStringErrs(t *testing.T) {
	s := "qwert"
	var d Decimal
	var err interface{}

	func(d Decimal) {
		defer func() {
			err = recover()
		}()

		RequireFromString(s)
	}(d)

	if err == nil {
		t.Errorf("panic expected when parsing %s", s)
	}
}

func TestNewFromFloatWithExponent(t *testing.T) {
	type Inp struct {
		float float64
		exp   int32
	}
	// some tests are taken from here https://www.cockroachlabs.com/blog/rounding-implementations-in-go/
	tests := map[Inp]string{
		Inp{123.4, -3}:                 "123.4",
		Inp{123.4, -1}:                 "123.4",
		Inp{123.412345, 1}:             "120",
		Inp{123.412345, 0}:             "123",
		Inp{123.412345, -5}:            "123.41235",
		Inp{123.412345, -6}:            "123.412345",
		Inp{123.412345, -7}:            "123.412345",
		Inp{123.412345, -28}:           "123.4123450000000019599610823207",
		Inp{1230000000, 3}:             "1230000000",
		Inp{123.9999999999999999, -7}:  "124",
		Inp{123.8989898999999999, -7}:  "123.8989899",
		Inp{0.49999999999999994, 0}:    "0",
		Inp{0.5, 0}:                    "1",
		Inp{0., -1000}:                 "0",
		Inp{0.5000000000000001, 0}:     "1",
		Inp{1.390671161567e-309, 0}:    "0",
		Inp{4.503599627370497e+15, 0}:  "4503599627370497",
		Inp{4.503599627370497e+60, 0}:  "4503599627370497110902645731364739935039854989106233267453952",
		Inp{4.503599627370497e+60, 1}:  "4503599627370497110902645731364739935039854989106233267453950",
		Inp{4.503599627370497e+60, -1}: "4503599627370497110902645731364739935039854989106233267453952",
		Inp{50, 2}:                     "100",
		Inp{49, 2}:                     "0",
		Inp{50, 3}:                     "0",
		// subnormals
		Inp{1.390671161567e-309, -2000}: "0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001390671161567000864431395448332752540137009987788957394095829635554502771758698872408926974382819387852542087331897381878220271350970912568035007740861074263206736245957501456549756342151614772544950978154339064833880234531754156635411349342950306987480369774780312897442981323940546749863054846093718407237782253156822124910364044261653195961209878120072488178603782495270845071470243842997312255994555557251870400944414666445871039673491570643357351279578519863428540219295076767898526278029257129758694673164251056158277568765100904638511604478844087596428177947970563689475826736810456067108202083804368114484417399279328807983736233036662284338182105684628835292230438999173947056675615385756827890872955322265625",
		Inp{1.390671161567e-309, -862}:  "0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000013906711615670008644313954483327525401370099877889573940958296355545027717586988724089269743828193878525420873318973818782202713509709125680350077408610742632067362459575014565497563421516147725449509781543390648338802345317541566354113493429503069874803697747803128974429813239405467498630548460937184072377822531568221249103640442616531959612098781200724881786037824952708450714702438429973122559945555572518704009444146664458710396734915706433573512795785198634285402192950767678985262780292571297586946731642510561582775687651009046385116044788440876",
		Inp{1.390671161567e-309, -863}:  "0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000013906711615670008644313954483327525401370099877889573940958296355545027717586988724089269743828193878525420873318973818782202713509709125680350077408610742632067362459575014565497563421516147725449509781543390648338802345317541566354113493429503069874803697747803128974429813239405467498630548460937184072377822531568221249103640442616531959612098781200724881786037824952708450714702438429973122559945555572518704009444146664458710396734915706433573512795785198634285402192950767678985262780292571297586946731642510561582775687651009046385116044788440876",
	}

	// add negatives
	for p, s := range tests {
		if p.float > 0 {
			if s != "0" {
				tests[Inp{-p.float, p.exp}] = "-" + s
			} else {
				tests[Inp{-p.float, p.exp}] = "0"
			}
		}
	}

	for input, s := range tests {
		d := NewFromFloatWithExponent(input.float, input.exp)
		if d.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, d.String(),
				d.value.String(), d.exp)
		}
	}

	shouldPanicOn := []float64{
		math.NaN(),
		math.Inf(1),
		math.Inf(-1),
	}

	for _, n := range shouldPanicOn {
		var d Decimal
		if !didPanic(func() { d = NewFromFloatWithExponent(n, 0) }) {
			t.Fatalf("Expected panic when creating a Decimal from %v, got %v instead", n, d.String())
		}
	}
}

func TestNewFromInt(t *testing.T) {
	tests := map[int64]string{
		0:                    "0",
		1:                    "1",
		323412345:            "323412345",
		9223372036854775807:  "9223372036854775807",
		-9223372036854775808: "-9223372036854775808",
	}

	// add negatives
	for p, s := range tests {
		if p > 0 {
			tests[-p] = "-" + s
		}
	}

	for input, s := range tests {
		d := NewFromInt(input)
		if d.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, d.String(),
				d.value.String(), d.exp)
		}
	}
}

func TestNewFromInt32(t *testing.T) {
	tests := map[int32]string{
		0:           "0",
		1:           "1",
		323412345:   "323412345",
		2147483647:  "2147483647",
		-2147483648: "-2147483648",
	}

	// add negatives
	for p, s := range tests {
		if p > 0 {
			tests[-p] = "-" + s
		}
	}

	for input, s := range tests {
		d := NewFromInt32(input)
		if d.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, d.String(),
				d.value.String(), d.exp)
		}
	}
}

func TestNewFromUint64(t *testing.T) {
	tests := map[uint64]string{
		0:                    "0",
		1:                    "1",
		323412345:            "323412345",
		9223372036854775807:  "9223372036854775807",
		18446744073709551615: "18446744073709551615",
	}

	for input, s := range tests {
		d := NewFromUint64(input)
		if d.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, d.String(),
				d.value.String(), d.exp)
		}
	}
}

func TestNewFromBigIntWithExponent(t *testing.T) {
	type Inp struct {
		val *big.Int
		exp int32
	}
	tests := map[Inp]string{
		Inp{big.NewInt(123412345), -3}: "123412.345",
		Inp{big.NewInt(2234), -1}:      "223.4",
		Inp{big.NewInt(323412345), 1}:  "3234123450",
		Inp{big.NewInt(423412345), 0}:  "423412345",
		Inp{big.NewInt(52341235), -5}:  "523.41235",
		Inp{big.NewInt(623412345), -6}: "623.412345",
		Inp{big.NewInt(723412345), -7}: "72.3412345",
	}

	// add negatives
	for p, s := range tests {
		if p.val.Cmp(zeroInt) > 0 {
			tests[Inp{p.val.Neg(p.val), p.exp}] = "-" + s
		}
	}

	for input, s := range tests {
		d := NewFromBigInt(input.val, input.exp)
		if d.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, d.String(),
				d.value.String(), d.exp)
		}
	}
}

func TestNewFromBigRat(t *testing.T) {
	mustParseRat := func(val string) *big.Rat {
		num, _ := new(big.Rat).SetString(val)
		return num
	}

	type Inp struct {
		val  *big.Rat
		prec int32
	}

	tests := map[Inp]string{
		Inp{big.NewRat(0, 1), 16}:                                                     "0",
		Inp{big.NewRat(4, 5), 16}:                                                     "0.8",
		Inp{big.NewRat(10, 2), 16}:                                                    "5",
		Inp{big.NewRat(1023427554493, 43432632), 16}:                                  "23563.5628642767953828", // rounded
		Inp{big.NewRat(1, 434324545566634), 16}:                                       "0.0000000000000023",
		Inp{big.NewRat(1, 3), 16}:                                                     "0.3333333333333333",
		Inp{big.NewRat(2, 3), 2}:                                                      "0.67",               // rounded
		Inp{big.NewRat(2, 3), 16}:                                                     "0.6666666666666667", // rounded
		Inp{big.NewRat(10000, 3), 16}:                                                 "3333.3333333333333333",
		Inp{mustParseRat("30702832066636633479"), 16}:                                 "30702832066636633479",
		Inp{mustParseRat("487028320159896636679.1827512895753"), 16}:                  "487028320159896636679.1827512895753",
		Inp{mustParseRat("127028320612589896636633479.173582751289575278357832"), -2}: "127028320612589896636633500",                  // rounded
		Inp{mustParseRat("127028320612589896636633479.173582751289575278357832"), 16}: "127028320612589896636633479.1735827512895753", // rounded
		Inp{mustParseRat("127028320612589896636633479.173582751289575278357832"), 32}: "127028320612589896636633479.173582751289575278357832",
	}

	// add negatives
	for p, s := range tests {
		if p.val.Cmp(new(big.Rat)) > 0 {
			tests[Inp{p.val.Neg(p.val), p.prec}] = "-" + s
		}
	}

	for input, s := range tests {
		d := NewFromBigRat(input.val, input.prec)
		if d.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, d.String(),
				d.value.String(), d.exp)
		}
	}
}

func TestCopy(t *testing.T) {
	origin := New(1, 0)
	cpy := origin.Copy()

	if origin.value == cpy.value {
		t.Error("expecting copy and origin to have different value pointers")
	}

	if cpy.Cmp(origin) != 0 {
		t.Error("expecting copy and origin to be equals, but they are not")
	}

	//change value
	cpy = cpy.Add(New(1, 0))

	if cpy.Cmp(origin) == 0 {
		t.Error("expecting copy and origin to have different values, but they are equal")
	}
}

func TestJSON(t *testing.T) {
	for _, x := range testTable {
		s := x.short
		var doc struct {
			Amount Decimal `json:"amount"`
		}
		docStr := `{"amount":"` + s + `"}`
		docStrNumber := `{"amount":` + s + `}`
		err := json.Unmarshal([]byte(docStr), &doc)
		if err != nil {
			t.Errorf("error unmarshaling %s: %v", docStr, err)
		} else if doc.Amount.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, doc.Amount.String(),
				doc.Amount.value.String(), doc.Amount.exp)
		}

		out, err := json.Marshal(&doc)
		if err != nil {
			t.Errorf("error marshaling %+v: %v", doc, err)
		} else if string(out) != docStr {
			t.Errorf("expected %s, got %s", docStr, string(out))
		}

		// make sure unquoted marshalling works too
		MarshalJSONWithoutQuotes = true
		out, err = json.Marshal(&doc)
		if err != nil {
			t.Errorf("error marshaling %+v: %v", doc, err)
		} else if string(out) != docStrNumber {
			t.Errorf("expected %s, got %s", docStrNumber, string(out))
		}
		MarshalJSONWithoutQuotes = false
	}
}

func TestUnmarshalJSONNull(t *testing.T) {
	var doc struct {
		Amount Decimal `json:"amount"`
	}
	docStr := `{"amount": null}`
	err := json.Unmarshal([]byte(docStr), &doc)
	if err != nil {
		t.Errorf("error unmarshaling %s: %v", docStr, err)
	} else if !doc.Amount.Equal(Zero) {
		t.Errorf("expected Zero, got %s (%s, %d)",
			doc.Amount.String(),
			doc.Amount.value.String(), doc.Amount.exp)
	}
}

func TestBadJSON(t *testing.T) {
	for _, testCase := range []string{
		"]o_o[",
		"{",
		`{"amount":""`,
		`{"amount":""}`,
		`{"amount":"nope"}`,
		`0.333`,
	} {
		var doc struct {
			Amount Decimal `json:"amount"`
		}
		err := json.Unmarshal([]byte(testCase), &doc)
		if err == nil {
			t.Errorf("expected error, got %+v", doc)
		}
	}
}

func TestNullDecimalJSON(t *testing.T) {
	for _, x := range testTable {
		s := x.short
		var doc struct {
			Amount NullDecimal `json:"amount"`
		}
		docStr := `{"amount":"` + s + `"}`
		docStrNumber := `{"amount":` + s + `}`
		err := json.Unmarshal([]byte(docStr), &doc)
		if err != nil {
			t.Errorf("error unmarshaling %s: %v", docStr, err)
		} else {
			if !doc.Amount.Valid {
				t.Errorf("expected %s to be valid (not NULL), got Valid = false", s)
			}
			if doc.Amount.Decimal.String() != s {
				t.Errorf("expected %s, got %s (%s, %d)",
					s, doc.Amount.Decimal.String(),
					doc.Amount.Decimal.value.String(), doc.Amount.Decimal.exp)
			}
		}

		out, err := json.Marshal(&doc)
		if err != nil {
			t.Errorf("error marshaling %+v: %v", doc, err)
		} else if string(out) != docStr {
			t.Errorf("expected %s, got %s", docStr, string(out))
		}

		// make sure unquoted marshalling works too
		MarshalJSONWithoutQuotes = true
		out, err = json.Marshal(&doc)
		if err != nil {
			t.Errorf("error marshaling %+v: %v", doc, err)
		} else if string(out) != docStrNumber {
			t.Errorf("expected %s, got %s", docStrNumber, string(out))
		}
		MarshalJSONWithoutQuotes = false
	}

	var doc struct {
		Amount NullDecimal `json:"amount"`
	}
	docStr := `{"amount": null}`
	err := json.Unmarshal([]byte(docStr), &doc)
	if err != nil {
		t.Errorf("error unmarshaling %s: %v", docStr, err)
	} else if doc.Amount.Valid {
		t.Errorf("expected null value to have Valid = false, got Valid = true and Decimal = %s (%s, %d)",
			doc.Amount.Decimal.String(),
			doc.Amount.Decimal.value.String(), doc.Amount.Decimal.exp)
	}

	expected := `{"amount":null}`
	out, err := json.Marshal(&doc)
	if err != nil {
		t.Errorf("error marshaling %+v: %v", doc, err)
	} else if string(out) != expected {
		t.Errorf("expected %s, got %s", expected, string(out))
	}

	// make sure unquoted marshalling works too
	MarshalJSONWithoutQuotes = true
	expectedUnquoted := `{"amount":null}`
	out, err = json.Marshal(&doc)
	if err != nil {
		t.Errorf("error marshaling %+v: %v", doc, err)
	} else if string(out) != expectedUnquoted {
		t.Errorf("expected %s, got %s", expectedUnquoted, string(out))
	}
	MarshalJSONWithoutQuotes = false
}

func TestNullDecimalBadJSON(t *testing.T) {
	for _, testCase := range []string{
		"]o_o[",
		"{",
		`{"amount":""`,
		`{"amount":""}`,
		`{"amount":"nope"}`,
		`{"amount":nope}`,
		`0.333`,
	} {
		var doc struct {
			Amount NullDecimal `json:"amount"`
		}
		err := json.Unmarshal([]byte(testCase), &doc)
		if err == nil {
			t.Errorf("expected error, got %+v", doc)
		}
	}
}

func TestXML(t *testing.T) {
	for _, x := range testTable {
		s := x.short
		var doc struct {
			XMLName xml.Name `xml:"account"`
			Amount  Decimal  `xml:"amount"`
		}
		docStr := `<account><amount>` + s + `</amount></account>`
		err := xml.Unmarshal([]byte(docStr), &doc)
		if err != nil {
			t.Errorf("error unmarshaling %s: %v", docStr, err)
		} else if doc.Amount.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, doc.Amount.String(),
				doc.Amount.value.String(), doc.Amount.exp)
		}

		out, err := xml.Marshal(&doc)
		if err != nil {
			t.Errorf("error marshaling %+v: %v", doc, err)
		} else if string(out) != docStr {
			t.Errorf("expected %s, got %s", docStr, string(out))
		}
	}
}

func TestBadXML(t *testing.T) {
	for _, testCase := range []string{
		"o_o",
		"<abc",
		"<account><amount>7",
		`<html><body></body></html>`,
		`<account><amount></amount></account>`,
		`<account><amount>nope</amount></account>`,
		`0.333`,
	} {
		var doc struct {
			XMLName xml.Name `xml:"account"`
			Amount  Decimal  `xml:"amount"`
		}
		err := xml.Unmarshal([]byte(testCase), &doc)
		if err == nil {
			t.Errorf("expected error, got %+v", doc)
		}
	}
}

func TestNullDecimalXML(t *testing.T) {
	// test valid values
	for _, x := range testTable {
		s := x.short
		var doc struct {
			XMLName xml.Name    `xml:"account"`
			Amount  NullDecimal `xml:"amount"`
		}
		docStr := `<account><amount>` + s + `</amount></account>`
		err := xml.Unmarshal([]byte(docStr), &doc)
		if err != nil {
			t.Errorf("error unmarshaling %s: %v", docStr, err)
		} else if doc.Amount.Decimal.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, doc.Amount.Decimal.String(),
				doc.Amount.Decimal.value.String(), doc.Amount.Decimal.exp)
		}

		out, err := xml.Marshal(&doc)
		if err != nil {
			t.Errorf("error marshaling %+v: %v", doc, err)
		} else if string(out) != docStr {
			t.Errorf("expected %s, got %s", docStr, string(out))
		}
	}

	var doc struct {
		XMLName xml.Name    `xml:"account"`
		Amount  NullDecimal `xml:"amount"`
	}

	// test for XML with empty body
	docStr := `<account><amount></amount></account>`
	err := xml.Unmarshal([]byte(docStr), &doc)
	if err != nil {
		t.Errorf("error unmarshaling: %s: %v", docStr, err)
	} else if doc.Amount.Valid {
		t.Errorf("expected null value to have Valid = false, got Valid = true and Decimal = %s (%s, %d)",
			doc.Amount.Decimal.String(),
			doc.Amount.Decimal.value.String(), doc.Amount.Decimal.exp)
	}

	expected := `<account><amount></amount></account>`
	out, err := xml.Marshal(&doc)
	if err != nil {
		t.Errorf("error marshaling %+v: %v", doc, err)
	} else if string(out) != expected {
		t.Errorf("expected %s, got %s", expected, string(out))
	}

	// test for empty XML
	docStr = `<account></account>`
	err = xml.Unmarshal([]byte(docStr), &doc)
	if err != nil {
		t.Errorf("error unmarshaling: %s: %v", docStr, err)
	} else if doc.Amount.Valid {
		t.Errorf("expected null value to have Valid = false, got Valid = true and Decimal = %s (%s, %d)",
			doc.Amount.Decimal.String(),
			doc.Amount.Decimal.value.String(), doc.Amount.Decimal.exp)
	}

	expected = `<account><amount></amount></account>`
	out, err = xml.Marshal(&doc)
	if err != nil {
		t.Errorf("error marshaling %+v: %v", doc, err)
	} else if string(out) != expected {
		t.Errorf("expected %s, got %s", expected, string(out))
	}
}

func TestNullDecimalBadXML(t *testing.T) {
	for _, testCase := range []string{
		"o_o",
		"<abc",
		"<account><amount>7",
		`<html><body></body></html>`,
		`<account><amount>nope</amount></account>`,
		`0.333`,
	} {
		var doc struct {
			XMLName xml.Name    `xml:"account"`
			Amount  NullDecimal `xml:"amount"`
		}
		err := xml.Unmarshal([]byte(testCase), &doc)
		if err == nil {
			t.Errorf("expected error, got %+v", doc)
		}
	}
}

func TestDecimal_rescale(t *testing.T) {
	type Inp struct {
		int     int64
		exp     int32
		rescale int32
	}
	tests := map[Inp]string{
		Inp{1234, -3, -5}: "1.234",
		Inp{1234, -3, 0}:  "1",
		Inp{1234, 3, 0}:   "1234000",
		Inp{1234, -4, -4}: "0.1234",
	}

	// add negatives
	for p, s := range tests {
		if p.int > 0 {
			tests[Inp{-p.int, p.exp, p.rescale}] = "-" + s
		}
	}

	for input, s := range tests {
		d := New(input.int, input.exp).rescale(input.rescale)

		if d.String() != s {
			t.Errorf("expected %s, got %s (%s, %d)",
				s, d.String(),
				d.value.String(), d.exp)
		}

		// test StringScaled
		s2 := New(input.int, input.exp).StringScaled(input.rescale)
		if s2 != s {
			t.Errorf("expected %s, got %s", s, s2)
		}
	}
}

func TestDecimal_Floor(t *testing.T) {
	assertFloor := func(input, expected Decimal) {
		got := input.Floor()
		if !got.Equal(expected) {
			t.Errorf("Floor(%s): got %s, expected %s", input, got, expected)
		}
	}
	type testDataString struct {
		input    string
		expected string
	}
	testsWithStrings := []testDataString{
		{"1.999", "1"},
		{"1", "1"},
		{"1.01", "1"},
		{"0", "0"},
		{"0.9", "0"},
		{"0.1", "0"},
		{"-0.9", "-1"},
		{"-0.1", "-1"},
		{"-1.00", "-1"},
		{"-1.01", "-2"},
		{"-1.999", "-2"},
	}
	for _, test := range testsWithStrings {
		expected, _ := NewFromString(test.expected)
		input, _ := NewFromString(test.input)
		assertFloor(input, expected)
	}

	type testDataDecimal struct {
		input    Decimal
		expected string
	}
	testsWithDecimals := []testDataDecimal{
		{New(100, -1), "10"},
		{New(10, 0), "10"},
		{New(1, 1), "10"},
		{New(1999, -3), "1"},
		{New(101, -2), "1"},
		{New(1, 0), "1"},
		{New(0, 0), "0"},
		{New(9, -1), "0"},
		{New(1, -1), "0"},
		{New(-1, -1), "-1"},
		{New(-9, -1), "-1"},
		{New(-1, 0), "-1"},
		{New(-101, -2), "-2"},
		{New(-1999, -3), "-2"},
	}
	for _, test := range testsWithDecimals {
		expected, _ := NewFromString(test.expected)
		assertFloor(test.input, expected)
	}
}

func TestDecimal_Ceil(t *testing.T) {
	assertCeil := func(input, expected Decimal) {
		got := input.Ceil()
		if !got.Equal(expected) {
			t.Errorf("Ceil(%s): got %s, expected %s", input, got, expected)
		}
	}
	type testDataString struct {
		input    string
		expected string
	}
	testsWithStrings := []testDataString{
		{"1.999", "2"},
		{"1", "1"},
		{"1.01", "2"},
		{"0", "0"},
		{"0.9", "1"},
		{"0.1", "1"},
		{"-0.9", "0"},
		{"-0.1", "0"},
		{"-1.00", "-1"},
		{"-1.01", "-1"},
		{"-1.999", "-1"},
	}
	for _, test := range testsWithStrings {
		expected, _ := NewFromString(test.expected)
		input, _ := NewFromString(test.input)
		assertCeil(input, expected)
	}

	type testDataDecimal struct {
		input    Decimal
		expected string
	}
	testsWithDecimals := []testDataDecimal{
		{New(100, -1), "10"},
		{New(10, 0), "10"},
		{New(1, 1), "10"},
		{New(1999, -3), "2"},
		{New(101, -2), "2"},
		{New(1, 0), "1"},
		{New(0, 0), "0"},
		{New(9, -1), "1"},
		{New(1, -1), "1"},
		{New(-1, -1), "0"},
		{New(-9, -1), "0"},
		{New(-1, 0), "-1"},
		{New(-101, -2), "-1"},
		{New(-1999, -3), "-1"},
	}
	for _, test := range testsWithDecimals {
		expected, _ := NewFromString(test.expected)
		assertCeil(test.input, expected)
	}
}

func TestDecimal_RoundAndStringFixed(t *testing.T) {
	type testData struct {
		input         string
		places        int32
		expected      string
		expectedFixed string
	}
	tests := []testData{
		{"1.454", 0, "1", ""},
		{"1.454", 1, "1.5", ""},
		{"1.454", 2, "1.45", ""},
		{"1.454", 3, "1.454", ""},
		{"1.454", 4, "1.454", "1.4540"},
		{"1.454", 5, "1.454", "1.45400"},
		{"1.554", 0, "2", ""},
		{"1.554", 1, "1.6", ""},
		{"1.554", 2, "1.55", ""},
		{"0.554", 0, "1", ""},
		{"0.454", 0, "0", ""},
		{"0.454", 5, "0.454", "0.45400"},
		{"0", 0, "0", ""},
		{"0", 1, "0", "0.0"},
		{"0", 2, "0", "0.00"},
		{"0", -1, "0", ""},
		{"5", 2, "5", "5.00"},
		{"5", 1, "5", "5.0"},
		{"5", 0, "5", ""},
		{"500", 2, "500", "500.00"},
		{"545", -1, "550", ""},
		{"545", -2, "500", ""},
		{"545", -3, "1000", ""},
		{"545", -4, "0", ""},
		{"499", -3, "0", ""},
		{"499", -4, "0", ""},
	}

	// add negative number tests
	for _, test := range tests {
		expected := test.expected
		if expected != "0" {
			expected = "-" + expected
		}
		expectedStr := test.expectedFixed
		if strings.ContainsAny(expectedStr, "123456789") && expectedStr != "" {
			expectedStr = "-" + expectedStr
		}
		tests = append(tests,
			testData{"-" + test.input, test.places, expected, expectedStr})
	}

	for _, test := range tests {
		d, err := NewFromString(test.input)
		if err != nil {
			t.Fatal(err)
		}

		// test Round
		expected, err := NewFromString(test.expected)
		if err != nil {
			t.Fatal(err)
		}
		got := d.Round(test.places)
		if !got.Equal(expected) {
			t.Errorf("Rounding %s to %d places, got %s, expected %s",
				d, test.places, got, expected)
		}

		// test StringFixed
		if test.expectedFixed == "" {
			test.expectedFixed = test.expected
		}
		gotStr := d.StringFixed(test.places)
		if gotStr != test.expectedFixed {
			t.Errorf("(%s).StringFixed(%d): got %s, expected %s",
				d, test.places, gotStr, test.expectedFixed)
		}
	}
}

func TestDecimal_RoundCeilAndStringFixed(t *testing.T) {
	type testData struct {
		input         string
		places        int32
		expected      string
		expectedFixed string
	}
	tests := []testData{
		{"1.454", 0, "2", ""},
		{"1.454", 1, "1.5", ""},
		{"1.454", 2, "1.46", ""},
		{"1.454", 3, "1.454", ""},
		{"1.454", 4, "1.454", "1.4540"},
		{"1.454", 5, "1.454", "1.45400"},
		{"1.554", 0, "2", ""},
		{"1.554", 1, "1.6", ""},
		{"1.554", 2, "1.56", ""},
		{"0.554", 0, "1", ""},
		{"0.454", 0, "1", ""},
		{"0.454", 5, "0.454", "0.45400"},
		{"0", 0, "0", ""},
		{"0", 1, "0", "0.0"},
		{"0", 2, "0", "0.00"},
		{"0", -1, "0", ""},
		{"5", 2, "5", "5.00"},
		{"5", 1, "5", "5.0"},
		{"5", 0, "5", ""},
		{"500", 2, "500", "500.00"},
		{"500", -2, "500", ""},
		{"545", -1, "550", ""},
		{"545", -2, "600", ""},
		{"545", -3, "1000", ""},
		{"545", -4, "10000", ""},
		{"499", -3, "1000", ""},
		{"499", -4, "10000", ""},
		{"1.1001", 2, "1.11", ""},
		{"-1.1001", 2, "-1.10", ""},
		{"-1.454", 0, "-1", ""},
		{"-1.454", 1, "-1.4", ""},
		{"-1.454", 2, "-1.45", ""},
		{"-1.454", 3, "-1.454", ""},
		{"-1.454", 4, "-1.454", "-1.4540"},
		{"-1.454", 5, "-1.454", "-1.45400"},
		{"-1.554", 0, "-1", ""},
		{"-1.554", 1, "-1.5", ""},
		{"-1.554", 2, "-1.55", ""},
		{"-0.554", 0, "0", ""},
		{"-0.454", 0, "0", ""},
		{"-0.454", 5, "-0.454", "-0.45400"},
		{"-5", 2, "-5", "-5.00"},
		{"-5", 1, "-5", "-5.0"},
		{"-5", 0, "-5", ""},
		{"-500", 2, "-500", "-500.00"},
		{"-500", -2, "-500", ""},
		{"-545", -1, "-540", ""},
		{"-545", -2, "-500", ""},
		{"-545", -3, "0", ""},
		{"-545", -4, "0", ""},
		{"-499", -3, "0", ""},
		{"-499", -4, "0", ""},
	}

	for _, test := range tests {
		d, err := NewFromString(test.input)
		if err != nil {
			t.Fatal(err)
		}

		// test Round
		expected, err := NewFromString(test.expected)
		if err != nil {
			t.Fatal(err)
		}
		got := d.RoundCeil(test.places)
		if !got.Equal(expected) {
			t.Errorf("Rounding ceil %s to %d places, got %s, expected %s",
				d, test.places, got, expected)
		}

		// test StringFixed
		if test.expectedFixed == "" {
			test.expectedFixed = test.expected
		}
		gotStr := got.StringFixed(test.places)
		if gotStr != test.expectedFixed {
			t.Errorf("(%s).StringFixed(%d): got %s, expected %s",
				d, test.places, gotStr, test.expectedFixed)
		}
	}
}

func TestDecimal_RoundFloorAndStringFixed(t *testing.T) {
	type testData struct {
		input         string
		places        int32
		expected      string
		expectedFixed string
	}
	tests := []testData{
		{"1.454", 0, "1", ""},
		{"1.454", 1, "1.4", ""},
		{"1.454", 2, "1.45", ""},
		{"1.454", 3, "1.454", ""},
		{"1.454", 4, "1.454", "1.4540"},
		{"1.454", 5, "1.454", "1.45400"},
		{"1.554", 0, "1", ""},
		{"1.554", 1, "1.5", ""},
		{"1.554", 2, "1.55", ""},
		{"0.554", 0, "0", ""},
		{"0.454", 0, "0", ""},
		{"0.454", 5, "0.454", "0.45400"},
		{"0", 0, "0", ""},
		{"0", 1, "0", "0.0"},
		{"0", 2, "0", "0.00"},
		{"0", -1, "0", ""},
		{"5", 2, "5", "5.00"},
		{"5", 1, "5", "5.0"},
		{"5", 0, "5", ""},
		{"500", 2, "500", "500.00"},
		{"500", -2, "500", ""},
		{"545", -1, "540", ""},
		{"545", -2, "500", ""},
		{"545", -3, "0", ""},
		{"545", -4, "0", ""},
		{"499", -3, "0", ""},
		{"499", -4, "0", ""},
		{"1.1001", 2, "1.10", ""},
		{"-1.1001", 2, "-1.11", ""},
		{"-1.454", 0, "-2", ""},
		{"-1.454", 1, "-1.5", ""},
		{"-1.454", 2, "-1.46", ""},
		{"-1.454", 3, "-1.454", ""},
		{"-1.454", 4, "-1.454", "-1.4540"},
		{"-1.454", 5, "-1.454", "-1.45400"},
		{"-1.554", 0, "-2", ""},
		{"-1.554", 1, "-1.6", ""},
		{"-1.554", 2, "-1.56", ""},
		{"-0.554", 0, "-1", ""},
		{"-0.454", 0, "-1", ""},
		{"-0.454", 5, "-0.454", "-0.45400"},
		{"-5", 2, "-5", "-5.00"},
		{"-5", 1, "-5", "-5.0"},
		{"-5", 0, "-5", ""},
		{"-500", 2, "-500", "-500.00"},
		{"-500", -2, "-500", ""},
		{"-545", -1, "-550", ""},
		{"-545", -2, "-600", ""},
		{"-545", -3, "-1000", ""},
		{"-545", -4, "-10000", ""},
		{"-499", -3, "-1000", ""},
		{"-499", -4, "-10000", ""},
	}

	for _, test := range tests {
		d, err := NewFromString(test.input)
		if err != nil {
			t.Fatal(err)
		}

		// test Round
		expected, err := NewFromString(test.expected)
		if err != nil {
			t.Fatal(err)
		}
		got := d.RoundFloor(test.places)
		if !got.Equal(expected) {
			t.Errorf("Rounding floor %s to %d places, got %s, expected %s",
				d, test.places, got, expected)
		}

		// test StringFixed
		if test.expectedFixed == "" {
			test.expectedFixed = test.expected
		}
		gotStr := got.StringFixed(test.places)
		if gotStr != test.expectedFixed {
			t.Errorf("(%s).StringFixed(%d): got %s, expected %s",
				d, test.places, gotStr, test.expectedFixed)
		}
	}
}

func TestDecimal_RoundUpAndStringFixed(t *testing.T) {
	type testData struct {
		input         string
		places        int32
		expected      string
		expectedFixed string
	}
	tests := []testData{
		{"1.454", 0, "2", ""},
		{"1.454", 1, "1.5", ""},
		{"1.454", 2, "1.46", ""},
		{"1.454", 3, "1.454", ""},
		{"1.454", 4, "1.454", "1.4540"},
		{"1.454", 5, "1.454", "1.45400"},
		{"1.554", 0, "2", ""},
		{"1.554", 1, "1.6", ""},
		{"1.554", 2, "1.56", ""},
		{"0.554", 0, "1", ""},
		{"0.454", 0, "1", ""},
		{"0.454", 5, "0.454", "0.45400"},
		{"0", 0, "0", ""},
		{"0", 1, "0", "0.0"},
		{"0", 2, "0", "0.00"},
		{"0", -1, "0", ""},
		{"5", 2, "5", "5.00"},
		{"5", 1, "5", "5.0"},
		{"5", 0, "5", ""},
		{"500", 2, "500", "500.00"},
		{"500", -2, "500", ""},
		{"545", -1, "550", ""},
		{"545", -2, "600", ""},
		{"545", -3, "1000", ""},
		{"545", -4, "10000", ""},
		{"499", -3, "1000", ""},
		{"499", -4, "10000", ""},
		{"1.1001", 2, "1.11", ""},
		{"-1.1001", 2, "-1.11", ""},
		{"-1.454", 0, "-2", ""},
		{"-1.454", 1, "-1.5", ""},
		{"-1.454", 2, "-1.46", ""},
		{"-1.454", 3, "-1.454", ""},
		{"-1.454", 4, "-1.454", "-1.4540"},
		{"-1.454", 5, "-1.454", "-1.45400"},
		{"-1.554", 0, "-2", ""},
		{"-1.554", 1, "-1.6", ""},
		{"-1.554", 2, "-1.56", ""},
		{"-0.554", 0, "-1", ""},
		{"-0.454", 0, "-1", ""},
		{"-0.454", 5, "-0.454", "-0.45400"},
		{"-5", 2, "-5", "-5.00"},
		{"-5", 1, "-5", "-5.0"},
		{"-5", 0, "-5", ""},
		{"-500", 2, "-500", "-500.00"},
		{"-500", -2, "-500", ""},
		{"-545", -1, "-550", ""},
		{"-545", -2, "-600", ""},
		{"-545", -3, "-1000", ""},
		{"-545", -4, "-10000", ""},
		{"-499", -3, "-1000", ""},
		{"-499", -4, "-10000", ""},
	}

	for _, test := range tests {
		d, err := NewFromString(test.input)
		if err != nil {
			t.Fatal(err)
		}

		// test Round
		expected, err := NewFromString(test.expected)
		if err != nil {
			t.Fatal(err)
		}
		got := d.RoundUp(test.places)
		if !got.Equal(expected) {
			t.Errorf("Rounding up %s to %d places, got %s, expected %s",
				d, test.places, got, expected)
		}

		// test StringFixed
		if test.expectedFixed == "" {
			test.expectedFixed = test.expected
		}
		gotStr := got.StringFixed(test.places)
		if gotStr != test.expectedFixed {
			t.Errorf("(%s).StringFixed(%d): got %s, expected %s",
				d, test.places, gotStr, test.expectedFixed)
		}
	}
}

func TestDecimal_RoundDownAndStringFixed(t *testing.T) {
	type testData struct {
		input         string
		places        int32
		expected      string
		expectedFixed string
	}
	tests := []testData{
		{"1.454", 0, "1", ""},
		{"1.454", 1, "1.4", ""},
		{"1.454", 2, "1.45", ""},
		{"1.454", 3, "1.454", ""},
		{"1.454", 4, "1.454", "1.4540"},
		{"1.454", 5, "1.454", "1.45400"},
		{"1.554", 0, "1", ""},
		{"1.554", 1, "1.5", ""},
		{"1.554", 2, "1.55", ""},
		{"0.554", 0, "0", ""},
		{"0.454", 0, "0", ""},
		{"0.454", 5, "0.454", "0.45400"},
		{"0", 0, "0", ""},
		{"0", 1, "0", "0.0"},
		{"0", 2, "0", "0.00"},
		{"0", -1, "0", ""},
		{"5", 2, "5", "5.00"},
		{"5", 1, "5", "5.0"},
		{"5", 0, "5", ""},
		{"500", 2, "500", "500.00"},
		{"500", -2, "500", ""},
		{"545", -1, "540", ""},
		{"545", -2, "500", ""},
		{"545", -3, "0", ""},
		{"545", -4, "0", ""},
		{"499", -3, "0", ""},
		{"499", -4, "0", ""},
		{"1.1001", 2, "1.10", ""},
		{"-1.1001", 2, "-1.10", ""},
		{"-1.454", 0, "-1", ""},
		{"-1.454", 1, "-1.4", ""},
		{"-1.454", 2, "-1.45", ""},
		{"-1.454", 3, "-1.454", ""},
		{"-1.454", 4, "-1.454", "-1.4540"},
		{"-1.454", 5, "-1.454", "-1.45400"},
		{"-1.554", 0, "-1", ""},
		{"-1.554", 1, "-1.5", ""},
		{"-1.554", 2, "-1.55", ""},
		{"-0.554", 0, "0", ""},
		{"-0.454", 0, "0", ""},
		{"-0.454", 5, "-0.454", "-0.45400"},
		{"-5", 2, "-5", "-5.00"},
		{"-5", 1, "-5", "-5.0"},
		{"-5", 0, "-5", ""},
		{"-500", 2, "-500", "-500.00"},
		{"-500", -2, "-500", ""},
		{"-545", -1, "-540", ""},
		{"-545", -2, "-500", ""},
		{"-545", -3, "0", ""},
		{"-545", -4, "0", ""},
		{"-499", -3, "0", ""},
		{"-499", -4, "0", ""},
	}

	for _, test := range tests {
		d, err := NewFromString(test.input)
		if err != nil {
			t.Fatal(err)
		}

		// test Round
		expected, err := NewFromString(test.expected)
		if err != nil {
			t.Fatal(err)
		}
		got := d.RoundDown(test.places)
		if !got.Equal(expected) {
			t.Errorf("Rounding down %s to %d places, got %s, expected %s",
				d, test.places, got, expected)
		}

		// test StringFixed
		if test.expectedFixed == "" {
			test.expectedFixed = test.expected
		}
		gotStr := got.StringFixed(test.places)
		if gotStr != test.expectedFixed {
			t.Errorf("(%s).StringFixed(%d): got %s, expected %s",
				d, test.places, gotStr, test.expectedFixed)
		}
	}
}

func TestDecimal_BankRoundAndStringFixed(t *testing.T) {
	type testData struct {
		input         string
		places        int32
		expected      string
		expectedFixed string
	}
	tests := []testData{
		{"1.454", 0, "1", ""},
		{"1.454", 1, "1.5", ""},
		{"1.454", 2, "1.45", ""},
		{"1.454", 3, "1.454", ""},
		{"1.454", 4, "1.454", "1.4540"},
		{"1.454", 5, "1.454", "1.45400"},
		{"1.554", 0, "2", ""},
		{"1.554", 1, "1.6", ""},
		{"1.554", 2, "1.55", ""},
		{"0.554", 0, "1", ""},
		{"0.454", 0, "0", ""},
		{"0.454", 5, "0.454", "0.45400"},
		{"0", 0, "0", ""},
		{"0", 1, "0", "0.0"},
		{"0", 2, "0", "0.00"},
		{"0", -1, "0", ""},
		{"5", 2, "5", "5.00"},
		{"5", 1, "5", "5.0"},
		{"5", 0, "5", ""},
		{"500", 2, "500", "500.00"},
		{"545", -2, "500", ""},
		{"545", -3, "1000", ""},
		{"545", -4, "0", ""},
		{"499", -3, "0", ""},
		{"499", -4, "0", ""},
		{"1.45", 1, "1.4", ""},
		{"1.55", 1, "1.6", ""},
		{"1.65", 1, "1.6", ""},
		{"545", -1, "540", ""},
		{"565", -1, "560", ""},
		{"555", -1, "560", ""},
	}

	// add negative number tests
	for _, test := range tests {
		expected := test.expected
		if expected != "0" {
			expected = "-" + expected
		}
		expectedStr := test.expectedFixed
		if strings.ContainsAny(expectedStr, "123456789") && expectedStr != "" {
			expectedStr = "-" + expectedStr
		}
		tests = append(tests,
			testData{"-" + test.input, test.places, expected, expectedStr})
	}

	for _, test := range tests {
		d, err := NewFromString(test.input)
		if err != nil {
			panic(err)
		}

		// test Round
		expected, err := NewFromString(test.expected)
		if err != nil {
			panic(err)
		}
		got := d.RoundBank(test.places)
		if !got.Equal(expected) {
			t.Errorf("Bank Rounding %s to %d places, got %s, expected %s",
				d, test.places, got, expected)
		}

		// test StringFixed
		if test.expectedFixed == "" {
			test.expectedFixed = test.expected
		}
		gotStr := d.StringFixedBank(test.places)
		if gotStr != test.expectedFixed {
			t.Errorf("(%s).StringFixed(%d): got %s, expected %s",
				d, test.places, gotStr, test.expectedFixed)
		}
	}
}

func TestDecimal_Uninitialized(t *testing.T) {
	a := Decimal{}
	b := Decimal{}

	decs := []Decimal{
		a,
		a.rescale(10),
		a.Abs(),
		a.Add(b),
		a.Sub(b),
		a.Mul(b),
		a.Shift(0),
		a.Div(New(1, -1)),
		a.Round(2),
		a.Floor(),
		a.Ceil(),
		a.Truncate(2),
	}

	for _, d := range decs {
		if d.String() != "0" {
			t.Errorf("expected 0, got %s", d.String())
		}
		if d.StringFixed(3) != "0.000" {
			t.Errorf("expected 0, got %s", d.StringFixed(3))
		}
		if d.StringScaled(-2) != "0" {
			t.Errorf("expected 0, got %s", d.StringScaled(-2))
		}
	}

	if a.Cmp(b) != 0 {
		t.Errorf("a != b")
	}
	if a.Sign() != 0 {
		t.Errorf("a.Sign() != 0")
	}
	if a.Exponent() != 0 {
		t.Errorf("a.Exponent() != 0")
	}
	if a.IntPart() != 0 {
		t.Errorf("a.IntPar() != 0")
	}
	f, _ := a.Float64()
	if f != 0 {
		t.Errorf("a.Float64() != 0")
	}
	if a.Rat().RatString() != "0" {
		t.Errorf("a.Rat() != 0, got %s", a.Rat().RatString())
	}
}

func TestDecimal_Add(t *testing.T) {
	type Inp struct {
		a string
		b string
	}

	inputs := map[Inp]string{
		Inp{"2", "3"}:                     "5",
		Inp{"2454495034", "3451204593"}:   "5905699627",
		Inp{"24544.95034", ".3451204593"}: "24545.2954604593",
		Inp{".1", ".1"}:                   "0.2",
		Inp{".1", "-.1"}:                  "0",
		Inp{"0", "1.001"}:                 "1.001",
	}

	for inp, res := range inputs {
		a, err := NewFromString(inp.a)
		if err != nil {
			t.FailNow()
		}
		b, err := NewFromString(inp.b)
		if err != nil {
			t.FailNow()
		}
		c := a.Add(b)
		if c.String() != res {
			t.Errorf("expected %s, got %s", res, c.String())
		}
	}
}

func TestDecimal_Sub(t *testing.T) {
	type Inp struct {
		a string
		b string
	}

	inputs := map[Inp]string{
		Inp{"2", "3"}:                     "-1",
		Inp{"12", "3"}:                    "9",
		Inp{"-2", "9"}:                    "-11",
		Inp{"2454495034", "3451204593"}:   "-996709559",
		Inp{"24544.95034", ".3451204593"}: "24544.6052195407",
		Inp{".1", "-.1"}:                  "0.2",
		Inp{".1", ".1"}:                   "0",
		Inp{"0", "1.001"}:                 "-1.001",
		Inp{"1.001", "0"}:                 "1.001",
		Inp{"2.3", ".3"}:                  "2",
	}

	for inp, res := range inputs {
		a, err := NewFromString(inp.a)
		if err != nil {
			t.FailNow()
		}
		b, err := NewFromString(inp.b)
		if err != nil {
			t.FailNow()
		}
		c := a.Sub(b)
		if c.String() != res {
			t.Errorf("expected %s, got %s", res, c.String())
		}
	}
}

func TestDecimal_Neg(t *testing.T) {
	inputs := map[string]string{
		"0":     "0",
		"10":    "-10",
		"5.56":  "-5.56",
		"-10":   "10",
		"-5.56": "5.56",
	}

	for inp, res := range inputs {
		a, err := NewFromString(inp)
		if err != nil {
			t.FailNow()
		}
		b := a.Neg()
		if b.String() != res {
			t.Errorf("expected %s, got %s", res, b.String())
		}
	}
}

func TestDecimal_NegFromEmpty(t *testing.T) {
	a := Decimal{}
	b := a.Neg()
	if b.String() != "0" {
		t.Errorf("expected %s, got %s", "0", b)
	}
}

func TestDecimal_Mul(t *testing.T) {
	type Inp struct {
		a string
		b string
	}

	inputs := map[Inp]string{
		Inp{"2", "3"}:                     "6",
		Inp{"2454495034", "3451204593"}:   "8470964534836491162",
		Inp{"24544.95034", ".3451204593"}: "8470.964534836491162",
		Inp{".1", ".1"}:                   "0.01",
		Inp{"0", "1.001"}:                 "0",
	}

	for inp, res := range inputs {
		a, err := NewFromString(inp.a)
		if err != nil {
			t.FailNow()
		}
		b, err := NewFromString(inp.b)
		if err != nil {
			t.FailNow()
		}
		c := a.Mul(b)
		if c.String() != res {
			t.Errorf("expected %s, got %s", res, c.String())
		}
	}

	// positive scale
	c := New(1234, 5).Mul(New(45, -1))
	if c.String() != "555300000" {
		t.Errorf("Expected %s, got %s", "555300000", c.String())
	}
}

func TestDecimal_Shift(t *testing.T) {
	type Inp struct {
		a string
		b int32
	}

	inputs := map[Inp]string{
		Inp{"6", 3}:                         "6000",
		Inp{"10", -2}:                       "0.1",
		Inp{"2.2", 1}:                       "22",
		Inp{"-2.2", -1}:                     "-0.22",
		Inp{"12.88", 5}:                     "1288000",
		Inp{"-10234274355545544493", -3}:    "-10234274355545544.493",
		Inp{"-4612301402398.4753343454", 5}: "-461230140239847533.43454",
	}

	for inp, expectedStr := range inputs {
		num, _ := NewFromString(inp.a)

		got := num.Shift(inp.b)
		expected, _ := NewFromString(expectedStr)
		if !got.Equal(expected) {
			t.Errorf("expected %v when shifting %v by %v, got %v",
				expected, num, inp.b, got)
		}
	}
}

func TestDecimal_Div(t *testing.T) {
	type Inp struct {
		a string
		b string
	}

	inputs := map[Inp]string{
		Inp{"6", "3"}:                            "2",
		Inp{"10", "2"}:                           "5",
		Inp{"2.2", "1.1"}:                        "2",
		Inp{"-2.2", "-1.1"}:                      "2",
		Inp{"12.88", "5.6"}:                      "2.3",
		Inp{"1023427554493", "43432632"}:         "23563.5628642767953828", // rounded
		Inp{"1", "434324545566634"}:              "0.0000000000000023",
		Inp{"1", "3"}:                            "0.3333333333333333",
		Inp{"2", "3"}:                            "0.6666666666666667", // rounded
		Inp{"10000", "3"}:                        "3333.3333333333333333",
		Inp{"10234274355545544493", "-3"}:        "-3411424785181848164.3333333333333333",
		Inp{"-4612301402398.4753343454", "23.5"}: "-196268144782.9138440146978723",
	}

	for inp, expectedStr := range inputs {
		num, err := NewFromString(inp.a)
		if err != nil {
			t.FailNow()
		}
		denom, err := NewFromString(inp.b)
		if err != nil {
			t.FailNow()
		}
		got := num.Div(denom)
		expected, _ := NewFromString(expectedStr)
		if !got.Equal(expected) {
			t.Errorf("expected %v when dividing %v by %v, got %v",
				expected, num, denom, got)
		}
		got2 := num.DivRound(denom, int32(DivisionPrecision))
		if !got2.Equal(expected) {
			t.Errorf("expected %v on DivRound (%v,%v), got %v", expected, num, denom, got2)
		}
	}

	type Inp2 struct {
		n    int64
		exp  int32
		n2   int64
		exp2 int32
	}

	// test code path where exp > 0
	inputs2 := map[Inp2]string{
		Inp2{124, 10, 3, 1}: "41333333333.3333333333333333",
		Inp2{124, 10, 3, 0}: "413333333333.3333333333333333",
		Inp2{124, 10, 6, 1}: "20666666666.6666666666666667",
		Inp2{124, 10, 6, 0}: "206666666666.6666666666666667",
		Inp2{10, 10, 10, 1}: "1000000000",
	}

	for inp, expectedAbs := range inputs2 {
		for i := -1; i <= 1; i += 2 {
			for j := -1; j <= 1; j += 2 {
				n := inp.n * int64(i)
				n2 := inp.n2 * int64(j)
				num := New(n, inp.exp)
				denom := New(n2, inp.exp2)
				expected := expectedAbs
				if i != j {
					expected = "-" + expectedAbs
				}
				got := num.Div(denom)
				if got.String() != expected {
					t.Errorf("expected %s when dividing %v by %v, got %v",
						expected, num, denom, got)
				}
			}
		}
	}
}

func TestDecimal_QuoRem(t *testing.T) {
	type Inp4 struct {
		d   string
		d2  string
		exp int32
		q   string
		r   string
	}
	cases := []Inp4{
		{"10", "1", 0, "10", "0"},
		{"1", "10", 0, "0", "1"},
		{"1", "4", 2, "0.25", "0"},
		{"1", "8", 2, "0.12", "0.04"},
		{"10", "3", 1, "3.3", "0.1"},
		{"100", "3", 1, "33.3", "0.1"},
		{"1000", "10", -3, "0", "1000"},
		{"1e-3", "2e-5", 0, "50", "0"},
		{"1e-3", "2e-3", 1, "0.5", "0"},
		{"4e-3", "0.8", 4, "5e-3", "0"},
		{"4.1e-3", "0.8", 3, "5e-3", "1e-4"},
		{"-4", "-3", 0, "1", "-1"},
		{"-4", "3", 0, "-1", "-1"},
	}

	for _, inp4 := range cases {
		d, _ := NewFromString(inp4.d)
		d2, _ := NewFromString(inp4.d2)
		prec := inp4.exp
		q, r := d.QuoRem(d2, prec)
		expectedQ, _ := NewFromString(inp4.q)
		expectedR, _ := NewFromString(inp4.r)
		if !q.Equal(expectedQ) || !r.Equal(expectedR) {
			t.Errorf("bad QuoRem division %s , %s , %d got %v, %v expected %s , %s",
				inp4.d, inp4.d2, prec, q, r, inp4.q, inp4.r)
		}
		if !d.Equal(d2.Mul(q).Add(r)) {
			t.Errorf("not fitting: d=%v, d2= %v, prec=%d, q=%v, r=%v",
				d, d2, prec, q, r)
		}
		if !q.Equal(q.Truncate(prec)) {
			t.Errorf("quotient wrong precision: d=%v, d2= %v, prec=%d, q=%v, r=%v",
				d, d2, prec, q, r)
		}
		if r.Abs().Cmp(d2.Abs().Mul(New(1, -prec))) >= 0 {
			t.Errorf("remainder too large: d=%v, d2= %v, prec=%d, q=%v, r=%v",
				d, d2, prec, q, r)
		}
		if r.Sign()*d.Sign() < 0 {
			t.Errorf("signum of divisor and rest do not match: d=%v, d2= %v, prec=%d, q=%v, r=%v",
				d, d2, prec, q, r)
		}
	}
}

type DivTestCase struct {
	d    Decimal
	d2   Decimal
	prec int32
}

func createDivTestCases() []DivTestCase {
	res := make([]DivTestCase, 0)
	var n int32 = 5
	a := []int{1, 2, 3, 6, 7, 10, 100, 14, 5, 400, 0, 1000000, 1000000 + 1, 1000000 - 1}
	for s := -1; s < 2; s = s + 2 { // 2
		for s2 := -1; s2 < 2; s2 = s2 + 2 { // 2
			for e1 := -n; e1 <= n; e1++ { // 2n+1
				for e2 := -n; e2 <= n; e2++ { // 2n+1
					var prec int32
					for prec = -n; prec <= n; prec++ { // 2n+1
						for _, v1 := range a { // 11
							for _, v2 := range a { // 11, even if 0 is skipped
								sign1 := New(int64(s), 0)
								sign2 := New(int64(s2), 0)
								d := sign1.Mul(New(int64(v1), e1))
								d2 := sign2.Mul(New(int64(v2), e2))
								res = append(res, DivTestCase{d, d2, prec})
							}
						}
					}
				}
			}
		}
	}
	return res
}

func TestDecimal_QuoRem2(t *testing.T) {
	for _, tc := range createDivTestCases() {
		d := tc.d
		if sign(tc.d2) == 0 {
			continue
		}
		d2 := tc.d2
		prec := tc.prec
		q, r := d.QuoRem(d2, prec)
		// rule 1: d = d2*q +r
		if !d.Equal(d2.Mul(q).Add(r)) {
			t.Errorf("not fitting, d=%v, d2=%v, prec=%d, q=%v, r=%v",
				d, d2, prec, q, r)
		}
		// rule 2: q is integral multiple of 10^(-prec)
		if !q.Equal(q.Truncate(prec)) {
			t.Errorf("quotient wrong precision, d=%v, d2=%v, prec=%d, q=%v, r=%v",
				d, d2, prec, q, r)
		}
		// rule 3: abs(r)<abs(d) * 10^(-prec)
		if r.Abs().Cmp(d2.Abs().Mul(New(1, -prec))) >= 0 {
			t.Errorf("remainder too large, d=%v, d2=%v, prec=%d, q=%v, r=%v",
				d, d2, prec, q, r)
		}
		// rule 4: r and d have the same sign
		if r.Sign()*d.Sign() < 0 {
			t.Errorf("signum of divisor and rest do not match, "+
				"d=%v, d2=%v, prec=%d, q=%v, r=%v",
				d, d2, prec, q, r)
		}
	}
}

// this is the old Div method from decimal
// Div returns d / d2. If it doesn't divide exactly, the result will have
// DivisionPrecision digits after the decimal point.
func (d Decimal) DivOld(d2 Decimal, prec int) Decimal {
	// NOTE(vadim): division is hard, use Rat to do it
	ratNum := d.Rat()
	ratDenom := d2.Rat()

	quoRat := big.NewRat(0, 1).Quo(ratNum, ratDenom)

	// HACK(vadim): converting from Rat to Decimal inefficiently for now
	ret, err := NewFromString(quoRat.FloatString(prec))
	if err != nil {
		panic(err) // this should never happen
	}
	return ret
}

func sign(d Decimal) int {
	return d.Sign()
}

// rules for rounded divide, rounded to integer
// rounded_divide(d,d2) = q
// sign q * sign (d/d2) >= 0
// for d and d2 >0 :
// q is already rounded
// q = d/d2 + r , with r > -0.5 and r <= 0.5
// thus q-d/d2 = r, with r > -0.5 and r <= 0.5
// and d2 q -d = r d2 with r d2 > -d2/2 and r d2 <= d2/2
// and 2 (d2 q -d) = x with x > -d2 and x <= d2
// if we factor in precision then x > -d2 * 10^(-precision) and x <= d2 * 10(-precision)

func TestDecimal_DivRound(t *testing.T) {
	cases := []struct {
		d      string
		d2     string
		prec   int32
		result string
	}{
		{"2", "2", 0, "1"},
		{"1", "2", 0, "1"},
		{"-1", "2", 0, "-1"},
		{"-1", "-2", 0, "1"},
		{"1", "-2", 0, "-1"},
		{"1", "-20", 1, "-0.1"},
		{"1", "-20", 2, "-0.05"},
		{"1", "20.0000000000000000001", 1, "0"},
		{"1", "19.9999999999999999999", 1, "0.1"},
	}
	for _, s := range cases {
		d, _ := NewFromString(s.d)
		d2, _ := NewFromString(s.d2)
		result, _ := NewFromString(s.result)
		prec := s.prec
		q := d.DivRound(d2, prec)
		if sign(q)*sign(d)*sign(d2) < 0 {
			t.Errorf("sign of quotient wrong, got: %v/%v is about %v", d, d2, q)
		}
		x := q.Mul(d2).Abs().Sub(d.Abs()).Mul(New(2, 0))
		if x.Cmp(d2.Abs().Mul(New(1, -prec))) > 0 {
			t.Errorf("wrong rounding, got: %v/%v prec=%d is about %v", d, d2, prec, q)
		}
		if x.Cmp(d2.Abs().Mul(New(-1, -prec))) <= 0 {
			t.Errorf("wrong rounding, got: %v/%v prec=%d is about %v", d, d2, prec, q)
		}
		if !q.Equal(result) {
			t.Errorf("rounded division wrong %s / %s scale %d = %s, got %v", s.d, s.d2, prec, s.result, q)
		}
	}
}

func TestDecimal_DivRound2(t *testing.T) {
	for _, tc := range createDivTestCases() {
		d := tc.d
		if sign(tc.d2) == 0 {
			continue
		}
		d2 := tc.d2
		prec := tc.prec
		q := d.DivRound(d2, prec)
		if sign(q)*sign(d)*sign(d2) < 0 {
			t.Errorf("sign of quotient wrong, got: %v/%v is about %v", d, d2, q)
		}
		x := q.Mul(d2).Abs().Sub(d.Abs()).Mul(New(2, 0))
		if x.Cmp(d2.Abs().Mul(New(1, -prec))) > 0 {
			t.Errorf("wrong rounding, got: %v/%v prec=%d is about %v", d, d2, prec, q)
		}
		if x.Cmp(d2.Abs().Mul(New(-1, -prec))) <= 0 {
			t.Errorf("wrong rounding, got: %v/%v prec=%d is about %v", d, d2, prec, q)
		}
	}
}

func TestDecimal_RoundCash(t *testing.T) {
	tests := []struct {
		d        string
		interval uint8
		result   string
	}{
		{"3.44", 5, "3.45"},
		{"3.43", 5, "3.45"},
		{"3.42", 5, "3.40"},
		{"3.425", 5, "3.45"},
		{"3.47", 5, "3.45"},
		{"3.478", 5, "3.50"},
		{"3.48", 5, "3.50"},
		{"348", 5, "348"},

		{"3.23", 10, "3.20"},
		{"3.33", 10, "3.30"},
		{"3.53", 10, "3.50"},
		{"3.949", 10, "3.90"},
		{"3.95", 10, "4.00"},
		{"395", 10, "395"},

		{"3.23", 25, "3.25"},
		{"3.33", 25, "3.25"},
		{"3.53", 25, "3.50"},
		{"3.93", 25, "4.00"},
		{"3.41", 25, "3.50"},

		{"3.249", 50, "3.00"},
		{"3.33", 50, "3.50"},
		{"3.749999999", 50, "3.50"},
		{"3.75", 50, "4.00"},
		{"3.93", 50, "4.00"},
		{"393", 50, "393"},

		{"3.249", 100, "3.00"},
		{"3.49999", 100, "3.00"},
		{"3.50", 100, "4.00"},
		{"3.75", 100, "4.00"},
		{"3.93", 100, "4.00"},
		{"393", 100, "393"},
	}
	for i, test := range tests {
		d, _ := NewFromString(test.d)
		haveRounded := d.RoundCash(test.interval)
		result, _ := NewFromString(test.result)

		if !haveRounded.Equal(result) {
			t.Errorf("Index %d: Cash rounding for %q interval %d want %q, have %q", i, test.d, test.interval, test.result, haveRounded)
		}
	}
}

func TestDecimal_RoundCash_Panic(t *testing.T) {
	defer func() {
		if r := recover(); r != nil {
			if have, ok := r.(string); ok {
				const want = "Decimal does not support this Cash rounding interval `231`. Supported: 5, 10, 25, 50, 100"
				if want != have {
					t.Errorf("\nWant: %q\nHave: %q", want, have)
				}
			} else {
				t.Errorf("Panic should contain an error string but got:\n%+v", r)
			}
		} else {
			t.Error("Expecting a panic but got nothing")
		}
	}()
	d, _ := NewFromString("1")
	d.RoundCash(231)
}

func TestDecimal_Mod(t *testing.T) {
	type Inp struct {
		a string
		b string
	}

	inputs := map[Inp]string{
		Inp{"3", "2"}:                           "1",
		Inp{"3451204593", "2454495034"}:         "996709559",
		Inp{"9999999999", "1275"}:               "324",
		Inp{"9999999999.9999998", "1275.49"}:    "239.2399998",
		Inp{"24544.95034", "0.3451204593"}:      "0.3283950433",
		Inp{"0.499999999999999999", "0.25"}:     "0.249999999999999999",
		Inp{"0.989512958912895912", "0.000001"}: "0.000000958912895912",
		Inp{"0.1", "0.1"}:                       "0",
		Inp{"0", "1.001"}:                       "0",
		Inp{"-7.5", "2"}:                        "-1.5",
		Inp{"7.5", "-2"}:                        "1.5",
		Inp{"-7.5", "-2"}:                       "-1.5",
		Inp{"41", "21"}:                         "20",
		Inp{"400000000001", "200000000001"}:     "200000000000",
	}

	for inp, res := range inputs {
		a, err := NewFromString(inp.a)
		if err != nil {
			t.FailNow()
		}
		b, err := NewFromString(inp.b)
		if err != nil {
			t.FailNow()
		}
		c := a.Mod(b)
		if c.String() != res {
			t.Errorf("expected %s, got %s", res, c.String())
		}
	}
}

func TestDecimal_Overflow(t *testing.T) {
	if !didPanic(func() { New(1, math.MinInt32).Mul(New(1, math.MinInt32)) }) {
		t.Fatalf("should have gotten an overflow panic")
	}
	if !didPanic(func() { New(1, math.MaxInt32).Mul(New(1, math.MaxInt32)) }) {
		t.Fatalf("should have gotten an overflow panic")
	}
}

func TestDecimal_ExtremeValues(t *testing.T) {
	// NOTE(vadim): this test takes pretty much forever
	if testing.Short() {
		t.Skip()
	}

	// NOTE(vadim): Seriously, the numbers involved are so large that this
	// test will take way too long, so mark it as success if it takes over
	// 1 second. The way this test typically fails (integer overflow) is that
	// a wrong result appears quickly, so if it takes a long time then it is
	// probably working properly.
	// Why even bother testing this? Completeness, I guess. -Vadim
	const timeLimit = 1 * time.Second
	test := func(f func()) {
		c := make(chan bool)
		go func() {
			f()
			close(c)
		}()
		select {
		case <-c:
		case <-time.After(timeLimit):
		}
	}

	test(func() {
		got := New(123, math.MinInt32).Floor()
		if !got.Equal(NewFromFloat(0)) {
			t.Errorf("Error: got %s, expected 0", got)
		}
	})
	test(func() {
		got := New(123, math.MinInt32).Ceil()
		if !got.Equal(NewFromFloat(1)) {
			t.Errorf("Error: got %s, expected 1", got)
		}
	})
	test(func() {
		got := New(123, math.MinInt32).Rat().FloatString(10)
		expected := "0.0000000000"
		if got != expected {
			t.Errorf("Error: got %s, expected %s", got, expected)
		}
	})
}

func TestIntPart(t *testing.T) {
	for _, testCase := range []struct {
		Dec     string
		IntPart int64
	}{
		{"0.01", 0},
		{"12.1", 12},
		{"9999.999", 9999},
		{"-32768.01234", -32768},
	} {
		d, err := NewFromString(testCase.Dec)
		if err != nil {
			t.Fatal(err)
		}
		if d.IntPart() != testCase.IntPart {
			t.Errorf("expect %d, got %d", testCase.IntPart, d.IntPart())
		}
	}
}

func TestBigInt(t *testing.T) {
	testCases := []struct {
		Dec       string
		BigIntRep string
	}{
		{"0.0", "0"},
		{"0.00000", "0"},
		{"0.01", "0"},
		{"12.1", "12"},
		{"9999.999", "9999"},
		{"-32768.01234", "-32768"},
		{"-572372.0000000001", "-572372"},
	}

	for _, testCase := range testCases {
		d, err := NewFromString(testCase.Dec)
		if err != nil {
			t.Fatal(err)
		}
		if d.BigInt().String() != testCase.BigIntRep {
			t.Errorf("expect %s, got %s", testCase.BigIntRep, d.BigInt())
		}
	}
}

func TestBigFloat(t *testing.T) {
	testCases := []struct {
		Dec         string
		BigFloatRep string
	}{
		{"0.0", "0"},
		{"0.00000", "0"},
		{"0.01", "0.01"},
		{"12.1", "12.1"},
		{"9999.999", "9999.999"},
		{"-32768.01234", "-32768.01234"},
		{"-572372.0000000001", "-572372"},
		{"512.012345123451234512345", "512.0123451"},
		{"1.010101010101010101010101010101", "1.01010101"},
		{"55555555.555555555555555555555", "55555555.56"},
	}

	for _, testCase := range testCases {
		d, err := NewFromString(testCase.Dec)
		if err != nil {
			t.Fatal(err)
		}
		if d.BigFloat().String() != testCase.BigFloatRep {
			t.Errorf("expect %s, got %s", testCase.BigFloatRep, d.BigFloat())
		}
	}
}

func TestDecimal_Min(t *testing.T) {
	// the first element in the array is the expected answer, rest are inputs
	testCases := [][]float64{
		{0, 0},
		{1, 1},
		{-1, -1},
		{1, 1, 2},
		{-2, 1, 2, -2},
		{-3, 0, 2, -2, -3},
	}

	for _, test := range testCases {
		expected, input := test[0], test[1:]
		expectedDecimal := NewFromFloat(expected)
		decimalInput := []Decimal{}
		for _, inp := range input {
			d := NewFromFloat(inp)
			decimalInput = append(decimalInput, d)
		}
		got := Min(decimalInput[0], decimalInput[1:]...)
		if !got.Equal(expectedDecimal) {
			t.Errorf("Expected %v, got %v, input=%+v", expectedDecimal, got,
				decimalInput)
		}
	}
}

func TestDecimal_Max(t *testing.T) {
	// the first element in the array is the expected answer, rest are inputs
	testCases := [][]float64{
		{0, 0},
		{1, 1},
		{-1, -1},
		{2, 1, 2},
		{2, 1, 2, -2},
		{3, 0, 3, -2},
		{-2, -3, -2},
	}

	for _, test := range testCases {
		expected, input := test[0], test[1:]
		expectedDecimal := NewFromFloat(expected)
		decimalInput := []Decimal{}
		for _, inp := range input {
			d := NewFromFloat(inp)
			decimalInput = append(decimalInput, d)
		}
		got := Max(decimalInput[0], decimalInput[1:]...)
		if !got.Equal(expectedDecimal) {
			t.Errorf("Expected %v, got %v, input=%+v", expectedDecimal, got,
				decimalInput)
		}
	}
}

func scanHelper(t *testing.T, dbval interface{}, expected Decimal) {
	t.Helper()

	a := Decimal{}
	if err := a.Scan(dbval); err != nil {
		// Scan failed... no need to test result value
		t.Errorf("a.Scan(%v) failed with message: %s", dbval, err)
	} else if !a.Equal(expected) {
		// Scan succeeded... test resulting values
		t.Errorf("%s does not equal to %s", a, expected)
	}
}

func TestDecimal_Scan(t *testing.T) {
	// test the Scan method that implements the sql.Scanner interface
	// check different types received from various database drivers

	dbvalue := 54.33
	expected := NewFromFloat(dbvalue)
	scanHelper(t, dbvalue, expected)

	// apparently MySQL 5.7.16 and returns these as float32 so we need
	// to handle these as well
	dbvalueFloat32 := float32(54.33)
	expected = NewFromFloat(float64(dbvalueFloat32))
	scanHelper(t, dbvalueFloat32, expected)

	// at least SQLite returns an int64 when 0 is stored in the db
	// and you specified a numeric format on the schema
	dbvalueInt := int64(0)
	expected = New(dbvalueInt, 0)
	scanHelper(t, dbvalueInt, expected)

	// also test uint64
	dbvalueUint64 := uint64(2)
	expected = New(2, 0)
	scanHelper(t, dbvalueUint64, expected)

	// in case you specified a varchar in your SQL schema,
	// the database driver may return either []byte or string
	valueStr := "535.666"
	dbvalueStr := []byte(valueStr)
	expected, err := NewFromString(valueStr)
	if err != nil {
		t.Fatal(err)
	}
	scanHelper(t, dbvalueStr, expected)
	scanHelper(t, valueStr, expected)

	type foo struct{}
	a := Decimal{}
	err = a.Scan(foo{})
	if err == nil {
		t.Errorf("a.Scan(Foo{}) should have thrown an error but did not")
	}
}

func TestDecimal_Value(t *testing.T) {
	// Make sure this does implement the database/sql's driver.Valuer interface
	var d Decimal
	if _, ok := interface{}(d).(driver.Valuer); !ok {
		t.Error("Decimal does not implement driver.Valuer")
	}

	// check that normal case is handled appropriately
	a := New(1234, -2)
	expected := "12.34"
	value, err := a.Value()
	if err != nil {
		t.Errorf("Decimal(12.34).Value() failed with message: %s", err)
	} else if value.(string) != expected {
		t.Errorf("%s does not equal to %s", a, expected)
	}
}

func decodeSpannerHelper(t *testing.T, dbval interface{}, expected Decimal) {
	t.Helper()

	a := Decimal{}
	if err := a.DecodeSpanner(dbval); err != nil {
		// DecodeSpanner failed... no need to test result value
		t.Errorf("a.DecodeSpanner(%v) failed with message: %s", dbval, err)
	} else if !a.Equal(expected) {
		// DecodeSpanner succeeded... test resulting values
		t.Errorf("%s does not equal to %s", a, expected)
	}
}

type spannerDecoder interface {
	DecodeSpanner(input interface{}) error
}

func TestDecimal_DecodeSpanner(t *testing.T) {
	// test the DecodeSpanner method that implements spanner.Decoder interface
	if _, ok := interface{}(new(Decimal)).(spannerDecoder); !ok {
		t.Error("Decimal does not implement spanner.Decoder")
	}

	dbvalue := 54.33
	expected := NewFromFloat(dbvalue)
	decodeSpannerHelper(t, dbvalue, expected)

	// also test uint64
	dbvalueUint64 := uint64(2)
	expected = New(2, 0)
	decodeSpannerHelper(t, dbvalueUint64, expected)

	// ensure we can handle the return of either []byte or string
	valueStr := "535.666"
	dbvalueStr := []byte(valueStr)
	expected, err := NewFromString(valueStr)
	if err != nil {
		t.Fatal(err)
	}
	decodeSpannerHelper(t, dbvalueStr, expected)
	decodeSpannerHelper(t, valueStr, expected)

	type foo struct{}
	a := Decimal{}
	err = a.DecodeSpanner(foo{})
	if err == nil {
		t.Errorf("a.DecodeSpanner(Foo{}) should have thrown an error but did not")
	}
}

type spannerEncoder interface {
	EncodeSpanner() (interface{}, error)
}

func TestDecimal_EncodeSpanner(t *testing.T) {
	// Make sure this does implement the spanner.Encoder interface
	if _, ok := interface{}(Decimal{}).(spannerEncoder); !ok {
		t.Error("Decimal does not implement spanner.Encoder")
	}

	// check that normal case is handled appropriately
	a := New(1234, -2)
	expected := "12.34"
	value, err := a.Value()
	if err != nil {
		t.Errorf("Decimal(12.34).Value() failed with message: %s", err)
	} else if got := value.(string); got != expected {
		t.Errorf("%s does not equal to %s", a, expected)
	}
}

// old tests after this line

func TestDecimal_Scale(t *testing.T) {
	a := New(1234, -3)
	if a.Exponent() != -3 {
		t.Errorf("error")
	}
}

func TestDecimal_Abs1(t *testing.T) {
	a := New(-1234, -4)
	b := New(1234, -4)

	c := a.Abs()
	if c.Cmp(b) != 0 {
		t.Errorf("error")
	}
}

func TestDecimal_Abs2(t *testing.T) {
	a := New(-1234, -4)
	b := New(1234, -4)

	c := b.Abs()
	if c.Cmp(a) == 0 {
		t.Errorf("error")
	}
}

func TestDecimal_Equalities(t *testing.T) {
	a := New(1234, 3)
	b := New(1234, 3)
	c := New(1234, 4)

	if !a.Equal(b) {
		t.Errorf("%q should equal %q", a, b)
	}
	if a.Equal(c) {
		t.Errorf("%q should not equal %q", a, c)
	}

	// note, this block should be deprecated, here for backwards compatibility
	if !a.Equals(b) {
		t.Errorf("%q should equal %q", a, b)
	}

	if !c.GreaterThan(b) {
		t.Errorf("%q should be greater than  %q", c, b)
	}
	if b.GreaterThan(c) {
		t.Errorf("%q should not be greater than  %q", b, c)
	}
	if !a.GreaterThanOrEqual(b) {
		t.Errorf("%q should be greater or equal %q", a, b)
	}
	if !c.GreaterThanOrEqual(b) {
		t.Errorf("%q should be greater or equal %q", c, b)
	}
	if b.GreaterThanOrEqual(c) {
		t.Errorf("%q should not be greater or equal %q", b, c)
	}
	if !b.LessThan(c) {
		t.Errorf("%q should be less than %q", a, b)
	}
	if c.LessThan(b) {
		t.Errorf("%q should not be less than  %q", a, b)
	}
	if !a.LessThanOrEqual(b) {
		t.Errorf("%q should be less than or equal %q", a, b)
	}
	if !b.LessThanOrEqual(c) {
		t.Errorf("%q should be less than or equal  %q", a, b)
	}
	if c.LessThanOrEqual(b) {
		t.Errorf("%q should not be less than or equal %q", a, b)
	}
}

func TestDecimal_ScalesNotEqual(t *testing.T) {
	a := New(1234, 2)
	b := New(1234, 3)
	if a.Equal(b) {
		t.Errorf("%q should not equal %q", a, b)
	}
}

func TestDecimal_Cmp1(t *testing.T) {
	a := New(123, 3)
	b := New(-1234, 2)

	if a.Cmp(b) != 1 {
		t.Errorf("Error")
	}
}

func TestDecimal_Cmp2(t *testing.T) {
	a := New(123, 3)
	b := New(1234, 2)

	if a.Cmp(b) != -1 {
		t.Errorf("Error")
	}
}

func TestDecimal_Pow(t *testing.T) {
	for _, testCase := range []struct {
		Base     string
		Exponent string
		Expected string
	}{
		{"0.0", "1.0", "0.0"},
		{"0.0", "5.7", "0.0"},
		{"0.0", "-3.2", "0.0"},
		{"3.13", "0.0", "1.0"},
		{"-591.5", "0.0", "1.0"},
		{"3.0", "3.0", "27.0"},
		{"3.0", "10.0", "59049.0"},
		{"3.13", "5.0", "300.4150512793"},
		{"4.0", "2.0", "16.0"},
		{"4.0", "-2.0", "0.0625"},
		{"629.25", "5.0", "98654323103449.5673828125"},
		{"5.0", "5.73", "10118.08037159375"},
		{"962.0", "3.2791", "6055212360.0000044205714144"},
		{"5.69169126", "5.18515912", "8242.26344757948412597909547972726268869189399260047793106028930864"},
		{"13.1337", "3.5196719618391835", "8636.856220644773844815693636723928750940666269885"},
		{"67762386.283696923", "4.85917691669163916681738", "112761146905370140621385730157437443321.91755738117317148674362233906499698561022574811238435007575701773212242750262081945556470501"},
		{"-3.0", "6.0", "729"},
		{"-13.757", "5.0", "-492740.983929899460557"},
		{"3.0", "-6.0", "0.0013717421124829"},
		{"13.757", "-5.0", "0.000002029463821"},
		{"66.12", "-7.61313", "0.000000000000013854086588876805036"},
		{"6696871.12", "-2.61313", "0.000000000000000001455988684546983"},
		{"-3.0", "-6.0", "0.0013717421124829"},
		{"-13.757", "-5.0", "-0.000002029463821"},
	} {
		base, _ := NewFromString(testCase.Base)
		exp, _ := NewFromString(testCase.Exponent)
		expected, _ := NewFromString(testCase.Expected)

		result := base.Pow(exp)

		if result.Cmp(expected) != 0 {
			t.Errorf("expected %s, got %s, for %s^%s", testCase.Expected, result.String(), testCase.Base, testCase.Exponent)
		}
	}
}

func TestDecimal_PowWithPrecision(t *testing.T) {
	for _, testCase := range []struct {
		Base      string
		Exponent  string
		Precision int32
		Expected  string
	}{
		{"0.0", "1.0", 2, "0.0"},
		{"0.0", "5.7", 2, "0.0"},
		{"0.0", "-3.2", 2, "0.0"},
		{"3.13", "0.0", 2, "1.0"},
		{"-591.5", "0.0", 2, "1.0"},
		{"3.0", "3.0", 2, "27.0"},
		{"3.0", "10.0", 2, "59049.0"},
		{"3.13", "5.0", 5, "300.4150512793"},
		{"4.0", "2.0", 2, "16.0"},
		{"4.0", "-2.0", 2, "0.06"},
		{"4.0", "-2.0", 4, "0.0625"},
		{"629.25", "5.0", 6, "98654323103449.5673828125"},
		{"5.0", "5.73", 20, "10118.080371595019317118681359884375"},
		{"962.0", "3.2791", 15, "6055212360.000004406551603058195732"},
		{"5.69169126", "5.18515912", 4, "8242.26344757948412587366859330429895955552280978668983459852256"},
		{"13.1337", "3.5196719618391835", 8, "8636.85622064477384481569363672392591908386390769375"},
		{"67762386.283696923", "4.85917691669163916681738", 10, "112761146905370140621385730157437443321.917557381173174638304347353880676293576708009282115993465286373470882947470198597518762"},
		{"-3.0", "6.0", 2, "729"},
		{"-13.757", "5.0", 4, "-492740.983929899460557"},
		{"3.0", "-6.0", 10, "0.0013717421"},
		{"13.757", "-5.0", 20, "0.00000202946382098037"},
		{"66.12", "-7.61313", 20, "0.00000000000001385381563049821591633907104023700216"},
		{"6696871.12", "-2.61313", 24, "0.0000000000000000014558252733872790626400278983397459207418"},
		{"-3.0", "-6.0", 8, "0.00137174"},
		{"-13.757", "-5.0", 16, "-0.000002029463821"},
	} {
		base, _ := NewFromString(testCase.Base)
		exp, _ := NewFromString(testCase.Exponent)
		expected, _ := NewFromString(testCase.Expected)

		result, _ := base.PowWithPrecision(exp, testCase.Precision)

		if result.Cmp(expected) != 0 {
			t.Errorf("expected %s, got %s, for %s^%s", testCase.Expected, result.String(), testCase.Base, testCase.Exponent)
		}
	}
}

func TestDecimal_PowWithPrecision_Infinity(t *testing.T) {
	for _, testCase := range []struct {
		Base     string
		Exponent string
	}{
		{"0.0", "0.0"},
		{"0.0", "-2.0"},
		{"0.0", "-4.6"},
		{"-66.12", "7.61313"},      // Imaginary value
		{"-5696871.12", "5.61313"}, // Imaginary value
	} {
		base, _ := NewFromString(testCase.Base)
		exp, _ := NewFromString(testCase.Exponent)

		_, err := base.PowWithPrecision(exp, 5)

		if err == nil {
			t.Errorf("lool it should be error")
		}
	}
}

func TestDecimal_PowWithPrecision_UndefinedResult(t *testing.T) {
	base := RequireFromString("0")
	exponent := RequireFromString("0")

	_, err := base.PowWithPrecision(exponent, 4)

	if err == nil {
		t.Errorf("expected error, cannot be represent undefined value of 0**0")
	}
}

func TestDecimal_PowWithPrecision_InfinityResult(t *testing.T) {
	for _, testCase := range []struct {
		Base     string
		Exponent string
	}{
		{"0.0", "-2.0"},
		{"0.0", "-4.6"},
		{"0.0", "-9239.671333"},
	} {
		base, _ := NewFromString(testCase.Base)
		exp, _ := NewFromString(testCase.Exponent)

		_, err := base.PowWithPrecision(exp, 4)

		if err == nil {
			t.Errorf("expected error, cannot represent infinity value of 0 ** y, where y < 0")
		}
	}
}

func TestDecimal_PowWithPrecision_ImaginaryResult(t *testing.T) {
	for _, testCase := range []struct {
		Base     string
		Exponent string
	}{
		{"-0.2261", "106.12"},
		{"-66.12", "7.61313"},
		{"-5696871.12", "5.61313"},
	} {
		base, _ := NewFromString(testCase.Base)
		exp, _ := NewFromString(testCase.Exponent)

		_, err := base.PowWithPrecision(exp, 4)

		if err == nil {
			t.Errorf("expected error, cannot represent imaginary value of x ** y, where x < 0 and y is non-integer decimal")
		}
	}
}

func TestDecimal_PowInt32(t *testing.T) {
	for _, testCase := range []struct {
		Decimal  string
		Exponent int32
		Expected string
	}{
		{"0.0", 1, "0.0"},
		{"3.13", 0, "1.0"},
		{"-591.5", 0, "1.0"},
		{"3.0", 3, "27.0"},
		{"3.0", 10, "59049.0"},
		{"3.13", 5, "300.4150512793"},
		{"629.25", 5, "98654323103449.5673828125"},
		{"-3.0", 6, "729"},
		{"-13.757", 5, "-492740.983929899460557"},
		{"3.0", -6, "0.0013717421124829"},
		{"-13.757", -5, "-0.000002029463821"},
	} {
		base, _ := NewFromString(testCase.Decimal)
		expected, _ := NewFromString(testCase.Expected)

		result, _ := base.PowInt32(testCase.Exponent)

		if result.Cmp(expected) != 0 {
			t.Errorf("expected %s, got %s, for %s**%d", testCase.Expected, result.String(), testCase.Decimal, testCase.Exponent)
		}
	}
}

func TestDecimal_PowInt32_UndefinedResult(t *testing.T) {
	base := RequireFromString("0")

	_, err := base.PowInt32(0)

	if err == nil {
		t.Errorf("expected error, cannot be represent undefined value of 0**0")
	}
}

func TestDecimal_PowBigInt(t *testing.T) {
	for _, testCase := range []struct {
		Decimal  string
		Exponent *big.Int
		Expected string
	}{
		{"3.13", big.NewInt(0), "1.0"},
		{"-591.5", big.NewInt(0), "1.0"},
		{"3.0", big.NewInt(3), "27.0"},
		{"3.0", big.NewInt(10), "59049.0"},
		{"3.13", big.NewInt(5), "300.4150512793"},
		{"629.25", big.NewInt(5), "98654323103449.5673828125"},
		{"-3.0", big.NewInt(6), "729"},
		{"-13.757", big.NewInt(5), "-492740.983929899460557"},
		{"3.0", big.NewInt(-6), "0.0013717421124829"},
		{"-13.757", big.NewInt(-5), "-0.000002029463821"},
	} {
		base, _ := NewFromString(testCase.Decimal)
		expected, _ := NewFromString(testCase.Expected)

		result, _ := base.PowBigInt(testCase.Exponent)

		if result.Cmp(expected) != 0 {
			t.Errorf("expected %s, got %s, for %s**%d", testCase.Expected, result.String(), testCase.Decimal, testCase.Exponent)
		}
	}
}

func TestDecimal_PowBigInt_UndefinedResult(t *testing.T) {
	base := RequireFromString("0")

	_, err := base.PowBigInt(big.NewInt(0))

	if err == nil {
		t.Errorf("expected error, undefined value of 0**0 cannot be represented")
	}
}

func TestDecimal_IsInteger(t *testing.T) {
	for _, testCase := range []struct {
		Dec       string
		IsInteger bool
	}{
		{"0", true},
		{"0.0000", true},
		{"0.01", false},
		{"0.01010101010000", false},
		{"12.0", true},
		{"12.00000000000000", true},
		{"12.10000", false},
		{"9999.0000", true},
		{"99999999.000000000", true},
		{"-656323444.0000000000000", true},
		{"-32768.01234", false},
		{"-32768.0123423562623600000", false},
	} {
		d, err := NewFromString(testCase.Dec)
		if err != nil {
			t.Fatal(err)
		}
		if d.IsInteger() != testCase.IsInteger {
			t.Errorf("expect %t, got %t, for %s", testCase.IsInteger, d.IsInteger(), testCase.Dec)
		}
	}
}

func TestDecimal_ExpHullAbrham(t *testing.T) {
	for _, testCase := range []struct {
		Dec              string
		OverallPrecision uint32
		ExpectedDec      string
	}{
		{"0", 1, "1"},
		{"0.00", 5, "1"},
		{"0.5", 5, "1.6487"},
		{"0.569297", 10, "1.767024397"},
		{"0.569297", 16, "1.76702439654095"},
		{"0.569297", 20, "1.7670243965409496521"},
		{"1.0", 0, "3"},
		{"1.0", 1, "3"},
		{"1.0", 5, "2.7183"},
		{"1.0", 10, "2.718281828"},
		{"3.0", 0, "20"},
		{"3.0", 2, "20"},
		{"5.26", 0, "200"},
		{"5.26", 2, "190"},
		{"5.26", 10, "192.4814913"},
		{"5.2663117716", 2, "190"},
		{"5.2663117716", 10, "193.7002327"},
		{"26.1", 2, "220000000000"},
		{"26.1", 10, "216314672100"},
		{"26.1", 20, "216314672147.05767284"},
		{"50.1591", 10, "6078834887000000000000"},
		{"50.1591", 30, "6078834886623434464595.07937141"},
		{"-0.5", 5, "0.60653"},
		{"-0.569297", 10, "0.5659231429"},
		{"-0.569297", 16, "0.565923142859576"},
		{"-0.569297", 20, "0.56592314285957604443"},
		{"-1.0", 1, "0.4"},
		{"-1.0", 5, "0.36788"},
		{"-3.0", 1, "0"},
		{"-3.0", 2, "0.05"},
		{"-3.0", 10, "0.0497870684"},
		{"-5.26", 2, "0.01"},
		{"-5.26", 10, "0.0051953047"},
		{"-5.2663117716", 2, "0.01"},
		{"-5.2663117716", 10, "0.0051626164"},
		{"-26.1", 2, "0"},
		{"-26.1", 15, "0.000000000004623"},
		{"-50.1591", 10, "0"},
		{"-50.1591", 30, "0.000000000000000000000164505208"},
	} {
		d, _ := NewFromString(testCase.Dec)
		expected, _ := NewFromString(testCase.ExpectedDec)

		exp, err := d.ExpHullAbrham(testCase.OverallPrecision)
		if err != nil {
			t.Fatal(err)
		}

		if exp.Cmp(expected) != 0 {
			t.Errorf("expected %s, got %s, for decimal %s", testCase.ExpectedDec, exp.String(), testCase.Dec)
		}

	}
}

func TestDecimal_ExpTaylor(t *testing.T) {
	for _, testCase := range []struct {
		Dec         string
		Precision   int32
		ExpectedDec string
	}{
		{"0", 1, "1"},
		{"0.00", 5, "1"},
		{"0", -1, "0"},
		{"0.5", 5, "1.64872"},
		{"0.569297", 10, "1.7670243965"},
		{"0.569297", 16, "1.7670243965409497"},
		{"0.569297", 20, "1.76702439654094965215"},
		{"1.0", 0, "3"},
		{"1.0", 1, "2.7"},
		{"1.0", 5, "2.71828"},
		{"1.0", -1, "0"},
		{"1.0", -5, "0"},
		{"3.0", 1, "20.1"},
		{"3.0", 2, "20.09"},
		{"5.26", 0, "192"},
		{"5.26", 2, "192.48"},
		{"5.26", 10, "192.4814912972"},
		{"5.26", -2, "200"},
		{"5.2663117716", 2, "193.70"},
		{"5.2663117716", 10, "193.7002326701"},
		{"26.1", 2, "216314672147.06"},
		{"26.1", 20, "216314672147.05767284062928674083"},
		{"26.1", -2, "216314672100"},
		{"26.1", -10, "220000000000"},
		{"50.1591", 10, "6078834886623434464595.0793714061"},
		{"-0.5", 5, "0.60653"},
		{"-0.569297", 10, "0.5659231429"},
		{"-0.569297", 16, "0.565923142859576"},
		{"-0.569297", 20, "0.56592314285957604443"},
		{"-1.0", 1, "0.4"},
		{"-1.0", 5, "0.36788"},
		{"-1.0", -1, "0"},
		{"-1.0", -5, "0"},
		{"-3.0", 1, "0.1"},
		{"-3.0", 2, "0.05"},
		{"-3.0", 10, "0.0497870684"},
		{"-5.26", 2, "0.01"},
		{"-5.26", 10, "0.0051953047"},
		{"-5.26", -2, "0"},
		{"-5.2663117716", 2, "0.01"},
		{"-5.2663117716", 10, "0.0051626164"},
		{"-26.1", 2, "0"},
		{"-26.1", 15, "0.000000000004623"},
		{"-26.1", -2, "0"},
		{"-26.1", -10, "0"},
		{"-50.1591", 10, "0"},
		{"-50.1591", 30, "0.000000000000000000000164505208"},
	} {
		d, _ := NewFromString(testCase.Dec)
		expected, _ := NewFromString(testCase.ExpectedDec)

		exp, err := d.ExpTaylor(testCase.Precision)
		if err != nil {
			t.Fatal(err)
		}

		if exp.Cmp(expected) != 0 {
			t.Errorf("expected %s, got %s", testCase.ExpectedDec, exp.String())
		}
	}
}

func TestDecimal_Ln(t *testing.T) {
	for _, testCase := range []struct {
		Dec       string
		Precision int32
		Expected  string
	}{
		{"0.1", 25, "-2.3025850929940456840179915"},
		{"0.01", 25, "-4.6051701859880913680359829"},
		{"0.001", 25, "-6.9077552789821370520539744"},
		{"0.00000001", 25, "-18.4206807439523654721439316"},
		{"1.0", 10, "0.0"},
		{"1.01", 25, "0.0099503308531680828482154"},
		{"1.001", 25, "0.0009995003330835331668094"},
		{"1.0001", 25, "0.0000999950003333083353332"},
		{"1.1", 25, "0.0953101798043248600439521"},
		{"1.13", 25, "0.1222176327242492005461486"},
		{"3.13", 10, "1.1410330046"},
		{"3.13", 25, "1.1410330045520618486427824"},
		{"3.13", 50, "1.14103300455206184864278239988848193837089629107972"},
		{"3.13", 100, "1.1410330045520618486427823998884819383708962910797239760817078430268177216960996098918971117211892839"},
		{"5.71", 25, "1.7422190236679188486939833"},
		{"5.7185108151957193571930205", 50, "1.74370842450178929149992165925283704012576949094645"},
		{"839101.0351", 25, "13.6400864014410013994397240"},
		{"839101.0351094726488848490572028502", 50, "13.64008640145229044389152437468283605382056561604272"},
		{"5023583755703750094849.03519358513093500275017501750602739169823", 25, "49.9684305274348922267409953"},
		{"5023583755703750094849.03519358513093500275017501750602739169823", -1, "50.0"},
		{"66.12", 18, "4.191471272952823429"},
	} {
		d, _ := NewFromString(testCase.Dec)
		expected, _ := NewFromString(testCase.Expected)

		ln, err := d.Ln(testCase.Precision)
		if err != nil {
			t.Fatal(err)
		}

		if ln.Cmp(expected) != 0 {
			t.Errorf("expected %s, got %s, for decimal %s", testCase.Expected, ln.String(), testCase.Dec)
		}
	}
}

func TestDecimal_LnZero(t *testing.T) {
	d := New(0, 0)

	_, err := d.Ln(5)

	if err == nil {
		t.Errorf("expected error, natural logarithm of 0 cannot be represented (-infinity)")
	}
}

func TestDecimal_LnNegative(t *testing.T) {
	d := New(-20, 2)

	_, err := d.Ln(5)

	if err == nil {
		t.Errorf("expected error, natural logarithm cannot be calculated for nagative decimals")
	}
}

func TestDecimal_NumDigits(t *testing.T) {
	for _, testCase := range []struct {
		Dec               string
		ExpectedNumDigits int
	}{
		{"0", 1},
		{"0.00", 1},
		{"1.0", 2},
		{"3.0", 2},
		{"5.26", 3},
		{"5.2663117716", 11},
		{"3164836416948884.2162426426426267863", 35},
		{"26.1", 3},
		{"529.1591", 7},
		{"-1.0", 2},
		{"-3.0", 2},
		{"-5.26", 3},
		{"-5.2663117716", 11},
		{"-26.1", 3},
		{"", 1},
	} {
		d, _ := NewFromString(testCase.Dec)

		nums := d.NumDigits()
		if nums != testCase.ExpectedNumDigits {
			t.Errorf("expected %d digits for decimal %s, got %d", testCase.ExpectedNumDigits, testCase.Dec, nums)
		}
	}
}

func TestDecimal_Sign(t *testing.T) {
	if Zero.Sign() != 0 {
		t.Errorf("%q should have sign 0", Zero)
	}

	one := New(1, 0)
	if one.Sign() != 1 {
		t.Errorf("%q should have sign 1", one)
	}

	mone := New(-1, 0)
	if mone.Sign() != -1 {
		t.Errorf("%q should have sign -1", mone)
	}
}

func didPanic(f func()) bool {
	ret := false
	func() {

		defer func() {
			if message := recover(); message != nil {
				ret = true
			}
		}()

		// call the target function
		f()

	}()

	return ret

}

func TestDecimal_Coefficient(t *testing.T) {
	d := New(123, 0)
	co := d.Coefficient()
	if co.Int64() != 123 {
		t.Error("Coefficient should be 123; Got:", co)
	}
	co.Set(big.NewInt(0))
	if d.IntPart() != 123 {
		t.Error("Modifying coefficient modified Decimal; Got:", d)
	}
}

func TestDecimal_CoefficientInt64(t *testing.T) {
	type Inp struct {
		Dec         string
		Coefficient int64
	}

	testCases := []Inp{
		{"1", 1},
		{"1.111", 1111},
		{"1.000000", 1000000},
		{"1.121215125511", 1121215125511},
		{"100000000000000000", 100000000000000000},
		{"9223372036854775807", 9223372036854775807},
		{"10000000000000000000", -8446744073709551616}, // undefined value
	}

	// add negative cases
	for _, tc := range testCases {
		testCases = append(testCases, Inp{"-" + tc.Dec, -tc.Coefficient})
	}

	for _, tc := range testCases {
		d := RequireFromString(tc.Dec)
		coefficient := d.CoefficientInt64()
		if coefficient != tc.Coefficient {
			t.Errorf("expect coefficient %d, got %d, for decimal %s", tc.Coefficient, coefficient, tc.Dec)
		}
	}
}

func TestNullDecimal_Scan(t *testing.T) {
	// test the Scan method that implements the
	// sql.Scanner interface
	// check for the for different type of values
	// that are possible to be received from the database
	// drivers

	// in normal operations the db driver (sqlite at least)
	// will return an int64 if you specified a numeric format

	// Make sure handles nil values
	a := NullDecimal{}
	var dbvaluePtr interface{}
	err := a.Scan(dbvaluePtr)
	if err != nil {
		// Scan failed... no need to test result value
		t.Errorf("a.Scan(nil) failed with message: %s", err)
	} else {
		if a.Valid {
			t.Errorf("%s is not null", a.Decimal)
		}
	}

	dbvalue := 54.33
	expected := NewFromFloat(dbvalue)

	err = a.Scan(dbvalue)
	if err != nil {
		// Scan failed... no need to test result value
		t.Errorf("a.Scan(54.33) failed with message: %s", err)

	} else {
		// Scan succeeded... test resulting values
		if !a.Valid {
			t.Errorf("%s is null", a.Decimal)
		} else if !a.Decimal.Equals(expected) {
			t.Errorf("%s does not equal to %s", a.Decimal, expected)
		}
	}

	// at least SQLite returns an int64 when 0 is stored in the db
	// and you specified a numeric format on the schema
	dbvalueInt := int64(0)
	expected = New(dbvalueInt, 0)

	err = a.Scan(dbvalueInt)
	if err != nil {
		// Scan failed... no need to test result value
		t.Errorf("a.Scan(0) failed with message: %s", err)

	} else {
		// Scan succeeded... test resulting values
		if !a.Valid {
			t.Errorf("%s is null", a.Decimal)
		} else if !a.Decimal.Equals(expected) {
			t.Errorf("%v does not equal %v", a, expected)
		}
	}

	// in case you specified a varchar in your SQL schema,
	// the database driver will return byte slice []byte
	valueStr := "535.666"
	dbvalueStr := []byte(valueStr)
	expected, err = NewFromString(valueStr)
	if err != nil {
		t.Fatal(err)
	}

	err = a.Scan(dbvalueStr)
	if err != nil {
		// Scan failed... no need to test result value
		t.Errorf("a.Scan('535.666') failed with message: %s", err)

	} else {
		// Scan succeeded... test resulting values
		if !a.Valid {
			t.Errorf("%s is null", a.Decimal)
		} else if !a.Decimal.Equals(expected) {
			t.Errorf("%v does not equal %v", a, expected)
		}
	}

	// lib/pq can also return strings
	expected, err = NewFromString(valueStr)
	if err != nil {
		t.Fatal(err)
	}

	err = a.Scan(valueStr)
	if err != nil {
		// Scan failed... no need to test result value
		t.Errorf("a.Scan('535.666') failed with message: %s", err)
	} else {
		// Scan succeeded... test resulting values
		if !a.Valid {
			t.Errorf("%s is null", a.Decimal)
		} else if !a.Decimal.Equals(expected) {
			t.Errorf("%v does not equal %v", a, expected)
		}
	}
}

func TestNullDecimal_Value(t *testing.T) {
	// Make sure this does implement the database/sql's driver.Valuer interface
	var nullDecimal NullDecimal
	if _, ok := interface{}(nullDecimal).(driver.Valuer); !ok {
		t.Error("NullDecimal does not implement driver.Valuer")
	}

	// check that null is handled appropriately
	value, err := nullDecimal.Value()
	if err != nil {
		t.Errorf("NullDecimal{}.Valid() failed with message: %s", err)
	} else if value != nil {
		t.Errorf("%v is not nil", value)
	}

	// check that normal case is handled appropriately
	a := NullDecimal{Decimal: New(1234, -2), Valid: true}
	expected := "12.34"
	value, err = a.Value()
	if err != nil {
		t.Errorf("NullDecimal(12.34).Value() failed with message: %s", err)
	} else if value.(string) != expected {
		t.Errorf("%v does not equal %v", a, expected)
	}
}

func TestNullDecimal_DecodeSpanner(t *testing.T) {
	// test the DecodeSpanner method that implements the
	// spanner.Decoder interface
	if _, ok := interface{}(new(NullDecimal)).(spannerDecoder); !ok {
		t.Error("NullDecimal does not implement spanner.Decoder")
	}

	// Make sure handles nil value
	a := NullDecimal{}
	var dbvaluePtr interface{}
	err := a.DecodeSpanner(dbvaluePtr)
	if err != nil {
		// DecodeSpanner failed... no need to test result value
		t.Errorf("a.DecodeSpanner(nil) failed with message: %s", err)
	} else {
		if a.Valid {
			t.Errorf("%s is not null", a.Decimal)
		}
	}

	// Make sure handles nil *string
	dbvaluePtr = (*string)(nil)
	if err := a.DecodeSpanner(dbvaluePtr); err != nil {
		// DecodeSpanner failed... no need to test result value
		t.Errorf("a.DecodeSpanner((*string)(nil)) failed with message: %s", err)
	} else {
		if a.Valid {
			t.Errorf("%s is not null", a.Decimal)
		}
	}

	valueStr := "535.666"
	expected, err := NewFromString(valueStr)
	if err != nil {
		t.Fatal(err)
	}

	// Handle string
	err = a.DecodeSpanner(valueStr)
	if err != nil {
		// DecodeSpanner failed... no need to test result value
		t.Errorf("a.DecodeSpanner('535.666') failed with message: %s", err)
	} else {
		// DecodeSpanner succeeded... test resulting values
		if !a.Valid {
			t.Errorf("%s is null", a.Decimal)
		} else if !a.Decimal.Equals(expected) {
			t.Errorf("%v does not equal %v", a, expected)
		}
	}

	// handle *string
	err = a.DecodeSpanner(&valueStr)
	if err != nil {
		// DecodeSpanner failed... no need to test result value
		t.Errorf("a.DecodeSpanner('535.666') failed with message: %s", err)
	} else {
		// DecodeSpanner succeeded... test resulting values
		if !a.Valid {
			t.Errorf("%s is null", a.Decimal)
		} else if !a.Decimal.Equals(expected) {
			t.Errorf("%v does not equal %v", a, expected)
		}
	}
}

func TestNullDecimal_EncodeSpanner(t *testing.T) {
	// Make sure this does implement the spanner.Encoder interface
	var nullDecimal NullDecimal
	if _, ok := interface{}(nullDecimal).(spannerEncoder); !ok {
		t.Error("NullDecimal does not implement spanner.Encoder")
	}

	// check that null is handled appropriately
	value, err := nullDecimal.EncodeSpanner()
	if err != nil {
		t.Errorf("NullDecimal{}.Valid() failed with message: %s", err)
	} else if value != nil {
		t.Errorf("%v is not nil", value)
	}

	// check that normal case is handled appropriately
	a := NullDecimal{Decimal: New(1234, -2), Valid: true}
	expected := "12.34"
	value, err = a.EncodeSpanner()
	if err != nil {
		t.Errorf("NullDecimal(12.34).EncodeSpanner() failed with message: %s", err)
	} else if value.(string) != expected {
		t.Errorf("%v does not equal %v", a, expected)
	}
}

func TestBinary(t *testing.T) {
	for _, y := range testTable {
		x := y.float

		// Create the decimal
		d1 := NewFromFloat(x)

		// Encode to binary
		b, err := d1.MarshalBinary()
		if err != nil {
			t.Errorf("error marshalling %v to binary: %v", d1, err)
		}

		// Restore from binary
		var d2 Decimal
		err = (&d2).UnmarshalBinary(b)
		if err != nil {
			t.Errorf("error unmarshalling from binary: %v", err)
		}

		// The restored decimal should equal the original
		if !d1.Equals(d2) {
			t.Errorf("expected %v when restoring, got %v", d1, d2)
		}
	}
}

func TestBinary_Zero(t *testing.T) {
	var d1 Decimal

	b, err := d1.MarshalBinary()
	if err != nil {
		t.Fatalf("error marshalling %v to binary: %v", d1, err)
	}

	var d2 Decimal
	err = (&d2).UnmarshalBinary(b)
	if err != nil {
		t.Errorf("error unmarshalling from binary: %v", err)
	}

	if !d1.Equals(d2) {
		t.Errorf("expected %v when restoring, got %v", d1, d2)
	}
}

func TestBinary_DataTooShort(t *testing.T) {
	var d Decimal

	err := d.UnmarshalBinary(nil) // nil slice has length 0
	if err == nil {
		t.Fatalf("expected error, got %v", d)
	}
}

func TestBinary_InvalidValue(t *testing.T) {
	var d Decimal

	err := d.UnmarshalBinary([]byte{0, 0, 0, 0, 'x'}) // valid exponent, invalid value
	if err == nil {
		t.Fatalf("expected error, got %v", d)
	}
}

func slicesEqual(a, b []byte) bool {
	for i, val := range a {
		if b[i] != val {
			return false
		}
	}
	return true
}

func TestGobEncode(t *testing.T) {
	for _, y := range testTable {
		x := y.float
		d1 := NewFromFloat(x)

		b1, err := d1.GobEncode()
		if err != nil {
			t.Errorf("error encoding %v to binary: %v", d1, err)
		}

		d2 := NewFromFloat(x)

		b2, err := d2.GobEncode()
		if err != nil {
			t.Errorf("error encoding %v to binary: %v", d2, err)
		}

		if !slicesEqual(b1, b2) {
			t.Errorf("something about the gobencode is not working properly \n%v\n%v", b1, b2)
		}

		var d3 Decimal
		err = d3.GobDecode(b1)
		if err != nil {
			t.Errorf("Error gobdecoding %v, got %v", b1, d3)
		}
		var d4 Decimal
		err = d4.GobDecode(b2)
		if err != nil {
			t.Errorf("Error gobdecoding %v, got %v", b2, d4)
		}

		eq := d3.Equal(d4)
		if eq != true {
			t.Errorf("Encoding then decoding mutated Decimal")
		}

		eq = d1.Equal(d3)
		if eq != true {
			t.Errorf("Error gobencoding/decoding %v, got %v", d1, d3)
		}
	}
}

func TestSum(t *testing.T) {
	vals := make([]Decimal, 10)
	var i = int64(0)

	for key := range vals {
		vals[key] = New(i, 0)
		i++
	}

	sum := Sum(vals[0], vals[1:]...)
	if !sum.Equal(New(45, 0)) {
		t.Errorf("Failed to calculate sum, expected %s got %s", New(45, 0), sum)
	}
}

func TestAvg(t *testing.T) {
	vals := make([]Decimal, 10)
	var i = int64(0)

	for key := range vals {
		vals[key] = New(i, 0)
		i++
	}

	avg := Avg(vals[0], vals[1:]...)
	if !avg.Equal(NewFromFloat(4.5)) {
		t.Errorf("Failed to calculate average, expected %s got %s", NewFromFloat(4.5).String(), avg.String())
	}
}

func TestRoundBankAnomaly(t *testing.T) {
	a := New(25, -1)
	b := New(250, -2)

	if !a.Equal(b) {
		t.Errorf("Expected %s to equal %s", a, b)
	}

	expected := New(2, 0)

	aRounded := a.RoundBank(0)
	if !aRounded.Equal(expected) {
		t.Errorf("Expected bank rounding %s to equal %s, but it was %s", a, expected, aRounded)
	}

	bRounded := b.RoundBank(0)
	if !bRounded.Equal(expected) {
		t.Errorf("Expected bank rounding %s to equal %s, but it was %s", b, expected, bRounded)
	}
}

// Trig tests

// For Atan
func TestAtan(t *testing.T) {
	inps := []string{
		"-2.91919191919191919",
		"-1.0",
		"-0.25",
		"0.0",
		"0.33",
		"1.0",
		"5.0",
		"10",
		"11000020.2407442310156021090304691671842603586882014729198302312846062338790031898128063403419218957424",
	}
	sols := []string{
		"-1.24076438822058001027437062753106",
		"-0.78539816339744833061616997868383",
		"-0.24497866312686415",
		"0.0",
		"0.318747560420644443",
		"0.78539816339744833061616997868383",
		"1.37340076694501580123233995736766",
		"1.47112767430373453123233995736766",
		"1.57079623588597296123259450235374",
	}
	for i, inp := range inps {
		d, err := NewFromString(inp)
		if err != nil {
			t.FailNow()
		}
		s, err := NewFromString(sols[i])
		if err != nil {
			t.FailNow()
		}
		a := d.Atan()
		if !a.Equal(s) {
			t.Errorf("expected %s, got %s", s, a)
		}
	}
}

// For Sin
func TestSin(t *testing.T) {
	inps := []string{
		"-2.91919191919191919",
		"-1.0",
		"-0.25",
		"0.0",
		"0.33",
		"1.0",
		"5.0",
		"10",
		"11000020.2407442310156021090304691671842603586882014729198302312846062338790031898128063403419218957424",
	}
	sols := []string{"-0.22057186252002995641471297726318877448242875710373383657841216606788849153474483300147427943530288911869356126149550184271061369789963810497434594683859566879253561990821788142048867910104964466745284318577343435957806286762494529983369776697504436326725441516925396488258485248699247367113416543705253919473126183478178486954138205996912770183192357029798618739277146694040778731661407420114923656224752540889120768",
		"-0.841470984807896544828551915928318375739843472469519282898610111931110319333748010828751784005573402229699531838022117989945539661588502120624574802425114599802714611508860519655182175315926637327774878594985045816542706701485174683683726979309922117859910272413672784175028365607893544855897795184024100973080880074046886009375162838756876336134083638363801171409953672944184918309063800980214873465660723218405962257950683415203634506166523593278",
		"-0.2474039592545229296662577977006816864013671875",
		"0",
		"0.3240430283948683457891331120415701894104386268737728",
		"0.841470984807896544828551915928318375739843472469519282898610111931110319333748010828751784005573402229699531838022117989945539661588502120624574802425114599802714611508860519655182175315926637327774878594985045816542706701485174683683726979309922117859910272413672784175028365607893544855897795184024100973080880074046886009375162838756876336134083638363801171409953672944184918309063800980214873465660723218405962257950683415203634506166523593278",
		"-0.958924274663138409032065951037351417114444405831206421994322505831797734568720303321152847999323782235893449831846516332891972309733806145798957570823292783131379570446989311599459252931842975162373777189193072018951049969744350662993214861042908755303566670204873618202680865638534865944483058650517380292320436016362659617294570185140789829574277032406195741535138712427510938542219940873171248862329526140744770994303733112530324791184417282382",
		"-0.54402111088937016772477554483765124109312606762621462357463994520238396180161585438877562935656067241573063207614488370477645194661241525080677431257416988398683714890165970942834453391033857378247849486306346743023618509617104937236345831462093934032592562972419977883837745736210439651143668255744843041350221801750331646628192115694352540293150183983357476391787825596543270240461102629075832777618592034309799936",
		"-0.564291758480422881634770440632390475980828840253516895637281099241819037882007239070203007530085741820184955492382572029153491807930868879341091067301689987699567034024159005627332722089169680203292567574310010066799858914647295684974242359142300929248173166551428537696685165964880390889406578530338963341989826231514301546476672476399906348023294571001061677668735117509440368611093448917120819545826797975989350435900286332895885871219875665471968941335407351099209738417818747252638912592184093301853338763294381446907254104878969784040526201729163408095795934201105630182851806342356035203279670146684553491616847294749721014579109870396804713831114709372638323643327823671187472335866664108658093206409882794958673673978956925250261545083579947618620746006004554405785185537391110314728988164693223775249484198058394348289545771967707968288542718255197272633789792059019367104377340604030147471453833808674013259696102003732963091159662478879760121731138091114134586544668859915547568540172541576138084166990547345181184322550297604278946942918844039406876827936831612756344331500301118652183156052728447906384772901595431751550607818380262138322673253023464533931883787069611052589166000316238423939491520880451263927981787175602294299295744",
	}
	for i, inp := range inps {
		d, err := NewFromString(inp)
		if err != nil {
			t.FailNow()
		}
		s, err := NewFromString(sols[i])
		if err != nil {
			t.FailNow()
		}
		a := d.Sin()
		if !a.Equal(s) {
			t.Errorf("expected %s, got %s", s, a)
		}
	}
}

// For Cos
func TestCos(t *testing.T) {
	inps := []string{
		"-2.91919191919191919",
		"-1.0",
		"-0.25",
		"0.0",
		"0.33",
		"1.0",
		"5.0",
		"10",
		"11000020.2407442310156021090304691671842603586882014729198302312846062338790031898128063403419218957424",
	}
	sols := []string{
		"-0.975370726167463467746508538219884948528729295145689640359666742268127382748782064668565276308334226452812521220478854320025773591423493734486361306323829818426063430805234608660356853863442937297855742231573288105774823103008774355455799906250461848079705023428527473474556899228935370709945979509634251305018978306493011197513482210179171510947538040406781879762352211326273272515279567525396877609653501706919545667682725671944948392322552266752",
		"0.54030230586813965874561515067176071767603141150991567490927772778673118786033739102174242337864109186439207498973007363884202112942385976796862442063752663646870430360736682397798633852405003167527051283327366631405990604840629657123985368031838052877290142895506386796217551784101265975360960112885444847880134909594560331781699767647860744559228420471946006511861233129745921297270844542687374552066388998112901504",
		"0.968912421710644784099084544806854121387004852294921875",
		"1",
		"0.9460423435283869715490383692051286742343482760977712222",
		"0.54030230586813965874561515067176071767603141150991567490927772778673118786033739102174242337864109186439207498973007363884202112942385976796862442063752663646870430360736682397798633852405003167527051283327366631405990604840629657123985368031838052877290142895506386796217551784101265975360960112885444847880134909594560331781699767647860744559228420471946006511861233129745921297270844542687374552066388998112901504",
		"0.28366218546322646623291670213892426815646045792775066552057877370468842342090306560693620285882975471913545189522117672866861003904575909174769890684057564495184019705963607555427518763375472432216131070235796577209064861003009894615394882021220247535890708789312783718414424224334988974848162884228012265684775651099758365989567444515619764427493598258393280941942356912304265535918025036942025858493361644535438208",
		"-0.839071529076452222947082170022504835457755803801719612447629165523199043803440231769716865070163209041973184176293170330332317060558438085478980463542480791358920580076809381102480339018809694514100495572097422057215638383077242523713704127605770444906854175870243452753002238589530499630034663296166308443155999957196346563161387705205277189957388653461251461388391745795979375660087266037741360406956289962327970672363315696841378765492754546688",
		"-0.82557544253149396284458404188071504476091346830440347376462206521981928020803354950315062147200396866217255527509254080721982393941347365824137698491042935894213870423296625749297033966815252917361266452901192457318047750698424190124169875103436588397415032138037063155981648677895645409699825582226442363080800781881653440538927704569142007751338851079530521979429507520541625303794665680584709171813053216867014700596866196844144286737568957809383224972108999354839705480223052622003994027222120126949093911643497423100187973906980635670000034664323357488815820848035808846624518774608931622703631130673844138378087837990739103263093532314835289302930152150130664948083902949999427848344301686172490282395687167681679607401220592559832932068966455384902377056623736013617949634746332323529256184776892339963173795176200590119077305668901887229709592836744082027738666294887303249770621722032438202753270710379312736193201366287952361100525126056993039858894987153270630277483613793395809214871734783742285495171911648254647287555645360520115341268930844095156502348405343740866836850201634640011708462641462047870611041595707018966032206807675586825362640000739202116391403514629284000986232673698892843586989003952425039512325844566790376383098534975022847888104706525937115931692008959513984157709954859352131323440787667052399474107219968",
	}
	for i, inp := range inps {
		d, err := NewFromString(inp)
		if err != nil {
			t.FailNow()
		}
		s, err := NewFromString(sols[i])
		if err != nil {
			t.FailNow()
		}
		a := d.Cos()
		if !a.Equal(s) {
			t.Errorf("expected %s, got %s", s, a)
		}
	}
}

// For Tan
func TestTan(t *testing.T) {
	inps := []string{
		"-2.91919191919191919",
		"-1.0",
		"-0.25",
		"0.0",
		"0.33",
		"1.0",
		"5.0",
		"10",
		"11000020.2407442310156021090304691671842603586882014729198302312846062338790031898128063403419218957424",
	}
	sols := []string{
		"0.2261415650505790298980791606748881031998682652",
		"-1.5574077246549025",
		"-0.255341921221036275",
		"0.0",
		"0.342524867530038963",
		"1.5574077246549025",
		"-3.3805150062465829",
		"0.6483608274590872485524085572681343280321117494",
		"0.68351325561491170753499935023939368502774607234006019034769919811202010905597996164029250820702097041244539696",
	}
	for i, inp := range inps {
		d, err := NewFromString(inp)
		if err != nil {
			t.FailNow()
		}
		s, err := NewFromString(sols[i])
		if err != nil {
			t.FailNow()
		}
		a := d.Tan()
		if !a.Equal(s) {
			t.Errorf("expected %s, got %s", s, a)
		}
	}
}

func TestNewNullDecimal(t *testing.T) {
	d := NewFromInt(1)
	nd := NewNullDecimal(d)

	if !nd.Valid {
		t.Errorf("expected NullDecimal to be valid")
	}
	if nd.Decimal != d {
		t.Errorf("expected NullDecimal to hold the provided Decimal")
	}
}

func TestDecimal_String(t *testing.T) {
	type testData struct {
		input    string
		expected string
	}

	tests := []testData{
		{"1.22", "1.22"},
		{"1.00", "1"},
		{"153.192", "153.192"},
		{"999.999", "999.999"},
		{"0.0000000001", "0.0000000001"},
		{"0.0000000000", "0"},
	}

	for _, test := range tests {
		d, err := NewFromString(test.input)
		if err != nil {
			t.Fatal(err)
		} else if d.String() != test.expected {
			t.Errorf("expected %s, got %s", test.expected, d.String())
		}
	}
}

func TestDecimal_StringWithTrailing(t *testing.T) {
	type testData struct {
		input    string
		expected string
	}

	defer func() {
		TrimTrailingZeros = true
	}()

	TrimTrailingZeros = false
	tests := []testData{
		{"1.00", "1.00"},
		{"0.00", "0.00"},
		{"129.123000", "129.123000"},
		{"1.0000E3", "1000.0"}, // 1000 to the nearest tenth
		{"10000E-1", "1000.0"}, // 1000 to the nearest tenth
	}

	for _, test := range tests {
		d, err := NewFromString(test.input)
		if err != nil {
			t.Fatal(err)
		} else if d.String() != test.expected {
			x := d.String()
			fmt.Println(x)
			t.Errorf("expected %s, got %s", test.expected, d.String())
		}
	}
}

func TestDecimal_StringWithScientificNotationWhenNeeded(t *testing.T) {
	type testData struct {
		input    string
		expected string
	}

	defer func() {
		UseScientificNotation = false
	}()
	UseScientificNotation = true

	tests := []testData{
		{"1.0E3", "1.0E3"},   // 1000 to the nearest hundred
		{"1.00E3", "1.00E3"}, // 1000 to the nearest ten
		{"1.000E3", "1000"},  // 1000 to the nearest one
		{"1E3", "1E3"},       // 1000 to the nearest thousand
		{"-1E3", "-1E3"},     // -1000 to the nearest thousand
	}

	for _, test := range tests {
		d, err := NewFromString(test.input)
		if err != nil {
			t.Fatal(err)
		} else if d.String() != test.expected {
			x := d.String()
			fmt.Println(x)
			t.Errorf("expected %s, got %s", test.expected, d.String())
		}
	}
}

func TestDecimal_ScientificNotation(t *testing.T) {
	type testData struct {
		input    string
		expected string
	}

	tests := []testData{
		{"1", "1E0"},
		{"1.0", "1.0E0"},
		{"10", "1.0E1"},
		{"123", "1.23E2"},
		{"1234", "1.234E3"},
		{"-1", "-1E0"},
		{"-10", "-1.0E1"},
		{"-123", "-1.23E2"},
		{"-1234", "-1.234E3"},
		{"0.1", "1E-1"},
		{"0.01", "1E-2"},
		{"0.123", "1.23E-1"},
		{"1.23", "1.23E0"},
		{"-0.1", "-1E-1"},
		{"-0.01", "-1E-2"},
		{"-0.010", "-1.0E-2"},
		{"-0.123", "-1.23E-1"},
		{"-1.23", "-1.23E0"},
		{"1E6", "1E6"},
		{"1e6", "1E6"},
		{"1.23E6", "1.23E6"},
		{"-1E6", "-1E6"},
		{"1E-6", "1E-6"},
		{"1.23E-6", "1.23E-6"},
		{"-1E-6", "-1E-6"},
		{"-1.0E-6", "-1.0E-6"},
		{"12345600", "1.2345600E7"},
		{"123456E2", "1.23456E7"},
		{"0", "0"},
		{"0E1", "0"},
		{"-0", "0"},
		{"-0.000", "0"},
	}

	for _, test := range tests {
		d, err := NewFromString(test.input)
		if err != nil {
			t.Fatal(err)
		} else if d.ScientificNotationString() != test.expected {
			t.Errorf("expected %s, got %s", test.expected, d.ScientificNotationString())
		}
	}
}

func ExampleNewFromFloat32() {
	fmt.Println(NewFromFloat32(123.123123123123).String())
	fmt.Println(NewFromFloat32(.123123123123123).String())
	fmt.Println(NewFromFloat32(-1e13).String())
	// OUTPUT:
	//123.12312
	//0.123123124
	//-10000000000000
}

func ExampleNewFromFloat() {
	fmt.Println(NewFromFloat(123.123123123123).String())
	fmt.Println(NewFromFloat(.123123123123123).String())
	fmt.Println(NewFromFloat(-1e13).String())
	// OUTPUT:
	//123.123123123123
	//0.123123123123123
	//-10000000000000
}
```

## File: `go.mod`
```
module github.com/shopspring/decimal

go 1.10
```

## File: `rounding.go`
```go
// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Multiprecision decimal numbers.
// For floating-point formatting only; not general purpose.
// Only operations are assign and (binary) left/right shift.
// Can do binary floating point in multiprecision decimal precisely
// because 2 divides 10; cannot do decimal floating point
// in multiprecision binary precisely.

package decimal

type floatInfo struct {
	mantbits uint
	expbits  uint
	bias     int
}

var float32info = floatInfo{23, 8, -127}
var float64info = floatInfo{52, 11, -1023}

// roundShortest rounds d (= mant * 2^exp) to the shortest number of digits
// that will let the original floating point value be precisely reconstructed.
func roundShortest(d *decimal, mant uint64, exp int, flt *floatInfo) {
	// If mantissa is zero, the number is zero; stop now.
	if mant == 0 {
		d.nd = 0
		return
	}

	// Compute upper and lower such that any decimal number
	// between upper and lower (possibly inclusive)
	// will round to the original floating point number.

	// We may see at once that the number is already shortest.
	//
	// Suppose d is not denormal, so that 2^exp <= d < 10^dp.
	// The closest shorter number is at least 10^(dp-nd) away.
	// The lower/upper bounds computed below are at distance
	// at most 2^(exp-mantbits).
	//
	// So the number is already shortest if 10^(dp-nd) > 2^(exp-mantbits),
	// or equivalently log2(10)*(dp-nd) > exp-mantbits.
	// It is true if 332/100*(dp-nd) >= exp-mantbits (log2(10) > 3.32).
	minexp := flt.bias + 1 // minimum possible exponent
	if exp > minexp && 332*(d.dp-d.nd) >= 100*(exp-int(flt.mantbits)) {
		// The number is already shortest.
		return
	}

	// d = mant << (exp - mantbits)
	// Next highest floating point number is mant+1 << exp-mantbits.
	// Our upper bound is halfway between, mant*2+1 << exp-mantbits-1.
	upper := new(decimal)
	upper.Assign(mant*2 + 1)
	upper.Shift(exp - int(flt.mantbits) - 1)

	// d = mant << (exp - mantbits)
	// Next lowest floating point number is mant-1 << exp-mantbits,
	// unless mant-1 drops the significant bit and exp is not the minimum exp,
	// in which case the next lowest is mant*2-1 << exp-mantbits-1.
	// Either way, call it mantlo << explo-mantbits.
	// Our lower bound is halfway between, mantlo*2+1 << explo-mantbits-1.
	var mantlo uint64
	var explo int
	if mant > 1<<flt.mantbits || exp == minexp {
		mantlo = mant - 1
		explo = exp
	} else {
		mantlo = mant*2 - 1
		explo = exp - 1
	}
	lower := new(decimal)
	lower.Assign(mantlo*2 + 1)
	lower.Shift(explo - int(flt.mantbits) - 1)

	// The upper and lower bounds are possible outputs only if
	// the original mantissa is even, so that IEEE round-to-even
	// would round to the original mantissa and not the neighbors.
	inclusive := mant%2 == 0

	// As we walk the digits we want to know whether rounding up would fall
	// within the upper bound. This is tracked by upperdelta:
	//
	// If upperdelta == 0, the digits of d and upper are the same so far.
	//
	// If upperdelta == 1, we saw a difference of 1 between d and upper on a
	// previous digit and subsequently only 9s for d and 0s for upper.
	// (Thus rounding up may fall outside the bound, if it is exclusive.)
	//
	// If upperdelta == 2, then the difference is greater than 1
	// and we know that rounding up falls within the bound.
	var upperdelta uint8

	// Now we can figure out the minimum number of digits required.
	// Walk along until d has distinguished itself from upper and lower.
	for ui := 0; ; ui++ {
		// lower, d, and upper may have the decimal points at different
		// places. In this case upper is the longest, so we iterate from
		// ui==0 and start li and mi at (possibly) -1.
		mi := ui - upper.dp + d.dp
		if mi >= d.nd {
			break
		}
		li := ui - upper.dp + lower.dp
		l := byte('0') // lower digit
		if li >= 0 && li < lower.nd {
			l = lower.d[li]
		}
		m := byte('0') // middle digit
		if mi >= 0 {
			m = d.d[mi]
		}
		u := byte('0') // upper digit
		if ui < upper.nd {
			u = upper.d[ui]
		}

		// Okay to round down (truncate) if lower has a different digit
		// or if lower is inclusive and is exactly the result of rounding
		// down (i.e., and we have reached the final digit of lower).
		okdown := l != m || inclusive && li+1 == lower.nd

		switch {
		case upperdelta == 0 && m+1 < u:
			// Example:
			// m = 12345xxx
			// u = 12347xxx
			upperdelta = 2
		case upperdelta == 0 && m != u:
			// Example:
			// m = 12345xxx
			// u = 12346xxx
			upperdelta = 1
		case upperdelta == 1 && (m != '9' || u != '0'):
			// Example:
			// m = 1234598x
			// u = 1234600x
			upperdelta = 2
		}
		// Okay to round up if upper has a different digit and either upper
		// is inclusive or upper is bigger than the result of rounding up.
		okup := upperdelta > 0 && (inclusive || upperdelta > 1 || ui+1 < upper.nd)

		// If it's okay to do either, then round to the nearest one.
		// If it's okay to do only one, do it.
		switch {
		case okdown && okup:
			d.Round(mi + 1)
			return
		case okdown:
			d.RoundDown(mi + 1)
			return
		case okup:
			d.RoundUp(mi + 1)
			return
		}
	}
}
```

