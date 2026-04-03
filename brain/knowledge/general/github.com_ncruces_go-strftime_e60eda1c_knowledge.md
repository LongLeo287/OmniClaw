---
id: github.com-ncruces-go-strftime-e60eda1c-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:01.937744
---

# KNOWLEDGE EXTRACT: github.com_ncruces_go-strftime_e60eda1c
> **Extracted on:** 2026-04-01 17:06:07
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525499/github.com_ncruces_go-strftime_e60eda1c

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
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2022 Nuno Cruces

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
# `strftime`/`strptime` compatible time formatting and parsing for Go

[![Go Reference](https://pkg.go.dev/badge/image)](https://pkg.go.dev/github.com/ncruces/go-strftime)
[![Go Report](https://goreportcard.com/badge/github.com/ncruces/go-strftime)](https://goreportcard.com/report/github.com/ncruces/go-strftime)
[![Go Coverage](https://github.com/ncruces/go-strftime/wiki/coverage.svg)](https://raw.githack.com/wiki/ncruces/go-strftime/coverage.html)
```

## File: `bench_test.go`
```go
package strftime_test

import (
	"testing"
	"time"

	"github.com/ncruces/go-strftime"
)

const benchfmt = `%A %a %B %b %d %H %I %M %m %p %S %Y %y %Z`

func BenchmarkFormat(b *testing.B) {
	var t time.Time
	for i := 0; i < b.N; i++ {
		strftime.Format(benchfmt, t)
	}
}

func BenchmarkAppendFormat(b *testing.B) {
	var d []byte
	var t time.Time
	for i := 0; i < b.N; i++ {
		d = strftime.AppendFormat(d[:0], benchfmt, t)
	}
}
```

## File: `example_test.go`
```go
package strftime_test

import (
	"fmt"
	"os"

	strftime "github.com/ncruces/go-strftime"
)

func ExampleLayout() {
	layout, err := strftime.Layout("%Y-%m-%d %H:%M:%S")
	if err != nil {
		fmt.Fprint(os.Stderr, err)
	} else {
		fmt.Printf("%q", layout)
	}
	// Output:
	// "2006-01-02 15:04:05"
}
```

## File: `external_test.go`
```go
// These tests were adapted from 3rd party sources.

package strftime_test

import (
	"testing"
	"time"

	"github.com/ncruces/go-strftime"
)

func TestFormat_rubydoc(t *testing.T) {
	// https://ruby-doc.org/stdlib-2.6.1/libdoc/date/rdoc/DateTime.html#method-i-strftime
	reference := time.Date(2007, 11, 19, 8, 37, 48, 0, time.FixedZone("", -6*3600))
	tests := []struct {
		format string
		time   string
	}{
		{"Printed on %m/%d/%Y", "Printed on 11/19/2007"},
		{"at %I:%M%p", "at 08:37AM"},
		// Various ISO 8601 formats:
		{"%Y%m%d", "20071119"},                           // Calendar date (basic)
		{"%F", "2007-11-19"},                             // Calendar date (extended)
		{"%Y-%m", "2007-11"},                             // Calendar date, reduced accuracy, specific month
		{"%Y", "2007"},                                   // Calendar date, reduced accuracy, specific year
		{"%C", "20"},                                     // Calendar date, reduced accuracy, specific century
		{"%Y%j", "2007323"},                              // Ordinal date (basic)
		{"%Y-%j", "2007-323"},                            // Ordinal date (extended)
		{"%GW%V%u", "2007W471"},                          // Week date (basic)
		{"%G-W%V-%u", "2007-W47-1"},                      // Week date (extended)
		{"%GW%V", "2007W47"},                             // Week date, reduced accuracy, specific week (basic)
		{"%G-W%V", "2007-W47"},                           // Week date, reduced accuracy, specific week (extended)
		{"%H%M%S", "083748"},                             // Local time (basic)
		{"%T", "08:37:48"},                               // Local time (extended)
		{"%H%M", "0837"},                                 // Local time, reduced accuracy, specific minute (basic)
		{"%H:%M", "08:37"},                               // Local time, reduced accuracy, specific minute (extended)
		{"%H", "08"},                                     // Local time, reduced accuracy, specific hour
		{"%H%M%S,%L", "083748,000"},                      // Local time with decimal fraction, comma as decimal sign (basic)
		{"%T,%L", "08:37:48,000"},                        // Local time with decimal fraction, comma as decimal sign (extended)
		{"%H%M%S.%L", "083748.000"},                      // Local time with decimal fraction, full stop as decimal sign (basic)
		{"%T.%L", "08:37:48.000"},                        // Local time with decimal fraction, full stop as decimal sign (extended)
		{"%H%M%S%z", "083748-0600"},                      // Local time and the difference from UTC (basic)
		{"%T%:z", "08:37:48-06:00"},                      // Local time and the difference from UTC (extended)
		{"%Y%m%dT%H%M%S%z", "20071119T083748-0600"},      // Date and time of day for calendar date (basic)
		{"%FT%T%:z", "2007-11-19T08:37:48-06:00"},        // Date and time of day for calendar date (extended)
		{"%Y%jT%H%M%S%z", "2007323T083748-0600"},         // Date and time of day for ordinal date (basic)
		{"%Y-%jT%T%:z", "2007-323T08:37:48-06:00"},       // Date and time of day for ordinal date (extended)
		{"%GW%V%uT%H%M%S%z", "2007W471T083748-0600"},     // Date and time of day for week date (basic)
		{"%G-W%V-%uT%T%:z", "2007-W47-1T08:37:48-06:00"}, // Date and time of day for week date (extended)
		{"%Y%m%dT%H%M", "20071119T0837"},                 // Calendar date and local time (basic)
		{"%FT%R", "2007-11-19T08:37"},                    // Calendar date and local time (extended)
		{"%Y%jT%H%MZ", "2007323T0837Z"},                  // Ordinal date and UTC of day (basic)
		{"%Y-%jT%RZ", "2007-323T08:37Z"},                 // Ordinal date and UTC of day (extended)
		{"%GW%V%uT%H%M%z", "2007W471T0837-0600"},         // Week date and local time and difference from UTC (basic)
		{"%G-W%V-%uT%R%:z", "2007-W47-1T08:37-06:00"},    // Week date and local time and difference from UTC (extended)
	}

	for _, test := range tests {
		if got := strftime.Format(test.format, reference); got != test.time {
			t.Errorf("Format(%q) = %q, want %q", test.format, got, test.time)
		}
	}
}

func TestFormat_tebeka(t *testing.T) {
	// github.com/tebeka/strftime
	// github.com/hhkbp2/go-strftime
	reference := time.Date(2009, time.November, 10, 23, 1, 2, 3, time.UTC)
	tests := []struct {
		format string
		time   string
	}{
		{"%a", "Tue"},
		{"%A", "Tuesday"},
		{"%b", "Nov"},
		{"%B", "November"},
		{"%c", "Tue Nov 10 23:01:02 2009"}, // we use a different format
		{"%d", "10"},
		{"%H", "23"},
		{"%I", "11"},
		{"%j", "314"},
		{"%m", "11"},
		{"%M", "01"},
		{"%p", "PM"},
		{"%S", "02"},
		{"%U", "45"},
		{"%w", "2"},
		{"%W", "45"},
		{"%x", "11/10/09"},
		{"%X", "23:01:02"},
		{"%y", "09"},
		{"%Y", "2009"},
		{"%Z", "UTC"},
		{"%L", "000"},       // we use a different specifier
		{"%f", "000000"},    // we use a different specifier
		{"%N", "000000003"}, // we use a different specifier

		// Escape
		{"%%%Y", "%2009"},
		{"%3%%", "%3%"},
		{"%3%L", "%3000"},     // we use a different specifier
		{"%3xy%L", "%3xy000"}, // we use a different specifier

		// Embedded
		{"/path/%Y/%m/report", "/path/2009/11/report"},

		// Empty
		{"", ""},
	}

	for _, test := range tests {
		if got := strftime.Format(test.format, reference); got != test.time {
			t.Errorf("Format(%q) = %q, want %q", test.format, got, test.time)
		}
	}
}

func TestFormat_fastly(t *testing.T) {
	// github.com/fastly/go-utils/strftime
	timezone, err := time.LoadLocation("MST")
	if err != nil {
		t.Skip("could not load timezone:", err)
	}

	reference := time.Unix(1136239445, 0).In(timezone)

	tests := []struct {
		format string
		time   string
	}{
		{"", ``},

		// invalid formats
		{"%", `%`},
		{"%^", `%^`},
		{"%^ ", `%^ `},
		{"%^ x", `%^ x`},
		{"x%^ x", `x%^ x`},

		// supported locale-invariant formats
		{"%a", `Mon`},
		{"%A", `Monday`},
		{"%b", `Jan`},
		{"%B", `January`},
		{"%C", `20`},
		{"%d", `02`},
		{"%D", `01/02/06`},
		{"%e", ` 2`},
		{"%F", `2006-01-02`},
		{"%G", `2006`},
		{"%g", `06`},
		{"%h", `Jan`},
		{"%H", `15`},
		{"%I", `03`},
		{"%j", `002`},
		{"%k", `15`},
		{"%l", ` 3`},
		{"%m", `01`},
		{"%M", `04`},
		{"%n", "\n"},
		{"%p", `PM`},
		{"%r", `03:04:05 PM`},
		{"%R", `15:04`},
		{"%s", `1136239445`},
		{"%S", `05`},
		{"%t", "\t"},
		{"%T", `15:04:05`},
		{"%u", `1`},
		{"%U", `01`},
		{"%V", `01`},
		{"%w", `1`},
		{"%W", `01`},
		{"%x", `01/02/06`},
		{"%X", `15:04:05`},
		{"%y", `06`},
		{"%Y", `2006`},
		{"%z", `-0700`},
		{"%Z", `MST`},
		{"%%", `%`},

		// supported locale-varying formats
		{"%c", `Mon Jan  2 15:04:05 2006`},
		{"%E", `%E`},
		{"%EF", `%EF`},
		{"%O", `%O`},
		{"%OF", `%OF`},
		{"%P", `pm`},
		{"%+", `Mon Jan  2 15:04:05 MST 2006`},
		{
			"%a|%A|%b|%B|%c|%C|%d|%D|%e|%E|%EF|%F|%G|%g|%h|%H|%I|%j|%k|%l|%m|%M|%O|%OF|%p|%P|%r|%R|%s|%S|%t|%T|%u|%U|%V|%w|%W|%x|%X|%y|%Y|%z|%Z|%%",
			`Mon|Monday|Jan|January|Mon Jan  2 15:04:05 2006|20|02|01/02/06| 2|%E|%EF|2006-01-02|2006|06|Jan|15|03|002|15| 3|01|04|%O|%OF|PM|pm|03:04:05 PM|15:04|1136239445|05|	|15:04:05|1|01|01|1|01|01/02/06|15:04:05|06|2006|-0700|MST|%`,
		},
	}

	for _, test := range tests {
		if got := strftime.Format(test.format, reference); got != test.time {
			t.Errorf("Format(%q) = %q, want %q", test.format, got, test.time)
		}
	}
}

func TestFormat_jehiah(t *testing.T) {
	// github.com/jehiah/go-strftime
	reference := time.Unix(1340244776, 0).UTC()
	tests := []struct {
		format string
		time   string
	}{
		{"%Y-%m-%d %H:%M:%S", "2012-06-21 02:12:56"},
		{"aaabbb0123456789%Y", "aaabbb01234567892012"},
		{"%H:%M:%S.%L", "02:12:56.000"}, // jehiah disagrees with Ruby on this one
		{"%0%1%%%2", "%0%1%%2"},
	}

	for _, test := range tests {
		if got := strftime.Format(test.format, reference); got != test.time {
			t.Errorf("Format(%q) = %q, want %q", test.format, got, test.time)
		}
	}
}

func TestFormat_lestrrat(t *testing.T) {
	// github.com/lestrrat-go/strftime
	reference := time.Unix(1136239445, 123456789).UTC()
	tests := []struct {
		format string
		time   string
	}{
		{
			`%A %a %B %b %C %c %D %d %e %F %H %h %I %j %k %l %M %m %n %p %R %r %S %T %t %U %u %V %v %W %w %X %x %Y %y %Z %z`,
			"Monday Mon January Jan 20 Mon Jan  2 22:04:05 2006 01/02/06 02  2 2006-01-02 22 Jan 10 002 22 10 04 01 \n PM 22:04 10:04:05 PM 05 22:04:05 \t 01 1 01  2-Jan-2006 01 1 22:04:05 01/02/06 2006 06 UTC +0000",
		},
	}

	for _, test := range tests {
		if got := strftime.Format(test.format, reference); got != test.time {
			t.Errorf("Format(%q) = %q, want %q", test.format, got, test.time)
		}
	}
}
```

## File: `fuzz_test.go`
```go
//go:build go1.18

package strftime_test

import (
	"strings"
	"testing"

	"github.com/ncruces/go-strftime"
)

func FuzzFormat(f *testing.F) {
	for _, test := range timeTests {
		f.Add(test.format)
	}

	f.Fuzz(func(t *testing.T, format string) {
		str := strftime.Format(format, reference)
		if str == "" && format != "" {
			t.Errorf("Format(%q) = %q", format, str)
		}
		if str != format && !strings.Contains(format, "%") {
			t.Errorf("Format(%q) = %q", format, str)
		}
	})
}

func FuzzParse(f *testing.F) {
	for _, test := range timeTests {
		f.Add(test.format, strftime.Format(test.format, reference))
	}

	f.Fuzz(func(t *testing.T, format, value string) {
		parsed, err := strftime.Parse(format, value)
		if err != nil && !parsed.IsZero() {
			t.Errorf("Parse(%q, %q) = (%v, %v)", format, value, parsed, err)
		}
	})
}

func FuzzLayout(f *testing.F) {
	for _, test := range timeTests {
		f.Add(test.format)
	}

	f.Fuzz(func(t *testing.T, format string) {
		layout, err := strftime.Layout(format)
		if err != nil && layout != "" {
			t.Errorf("Layout(%q) = %v", format, err)
		}
		if err == nil && layout == "" && format != "" {
			t.Errorf("Layout(%q) = (%q, %v)", format, layout, err)
		}
	})
}

func FuzzUTS35(f *testing.F) {
	for _, test := range timeTests {
		f.Add(test.format)
	}

	f.Fuzz(func(t *testing.T, format string) {
		pattern, err := strftime.UTS35(format)
		if err != nil && pattern != "" {
			t.Errorf("UTS35(%q) = %v", format, err)
		}
		if err == nil && pattern == "" && format != "" {
			t.Errorf("UTS35(%q) = (%q, %v)", format, pattern, err)
		}
	})
}
```

## File: `go.mod`
```
module github.com/ncruces/go-strftime

go 1.17
```

## File: `parser.go`
```go
package strftime

import "unicode/utf8"

type parser struct {
	format  func(spec, flag byte) error
	literal func(byte) error
}

func (p *parser) parse(fmt string) error {
	const (
		initial = iota
		percent
		flagged
		modified
	)

	var flag, modifier byte
	var err error
	state := initial
	start := 0
	for i, b := range []byte(fmt) {
		switch state {
		default:
			if b == '%' {
				state = percent
				start = i
				continue
			}
			err = p.literal(b)

		case percent:
			if b == '-' || b == ':' {
				state = flagged
				flag = b
				continue
			}
			if b == 'E' || b == 'O' {
				state = modified
				modifier = b
				flag = 0
				continue
			}
			err = p.format(b, 0)
			state = initial

		case flagged:
			if b == 'E' || b == 'O' {
				state = modified
				modifier = b
				continue
			}
			err = p.format(b, flag)
			state = initial

		case modified:
			if okModifier(modifier, b) {
				err = p.format(b, flag)
			} else {
				err = p.literals(fmt[start : i+1])
			}
			state = initial
		}

		if err != nil {
			if err, ok := err.(formatError); ok {
				err.setDirective(fmt, start, i)
				return err
			}
			return err
		}
	}

	if state != initial {
		return p.literals(fmt[start:])
	}
	return nil
}

func (p *parser) literals(literal string) error {
	for _, b := range []byte(literal) {
		if err := p.literal(b); err != nil {
			return err
		}
	}
	return nil
}

type literalErr string

func (e literalErr) Error() string {
	return "strftime: unsupported literal: " + string(e)
}

type formatError struct {
	message   string
	directive string
}

func (e formatError) Error() string {
	return "strftime: unsupported directive: " + e.directive + " " + e.message
}

func (e *formatError) setDirective(str string, i, j int) {
	_, n := utf8.DecodeRuneInString(str[j:])
	e.directive = str[i : j+n]
}
```

## File: `parser_test.go`
```go
package strftime

import (
	"errors"
	"testing"
)

func Test_parser_literals(t *testing.T) {
	var noliterals parser
	noliterals.format = func(spec, flag byte) error { return nil }
	noliterals.literal = func(b byte) error { return errors.New("no literals") }

	for _, tt := range []string{"%+", "%c"} {
		if err := noliterals.parse(tt); err != nil {
			t.Errorf("noliterals.parse(%q) = %v", tt, err)
		}
	}

	for _, tt := range []string{"%-", "abc"} {
		if err := noliterals.parse(tt); err == nil {
			t.Errorf("noliterals.parse(%q) = %v", tt, err)
		}
	}
}

func Test_validModifier(t *testing.T) {
	for _, tt := range []string{"Ed", "Oc", "Yy"} {
		if okModifier(tt[0], tt[1]) {
			t.Errorf("okModifier(%q, %q)", tt[0], tt[1])
		}
	}

	for _, tt := range []string{"Ey", "Oy"} {
		if !okModifier(tt[0], tt[1]) {
			t.Errorf("not okModifier(%q, %q)", tt[0], tt[1])
		}
	}
}
```

## File: `pkg.go`
```go
/*
Package strftime provides strftime/strptime compatible time formatting and parsing.

The following formatting specifiers are available:

	Date (Year, Month, Day):
	  %Y - Year with century (can be negative, 4 digits at least)
	          -0001, 0000, 1995, 2009, 14292, etc.
	  %C - year / 100 (round down, 20 in 2009)
	  %y - year % 100 (00..99)

	  %m - Month of the year, zero-padded (01..12)
	          %-m  no-padded (1..12)
	  %B - Full month name (January)
	  %b - Abbreviated month name (Jan)
	  %h - Equivalent to %b

	  %d - Day of the month, zero-padded  (01..31)
	          %-d  no-padded (1..31)
	  %e - Day of the month, blank-padded ( 1..31)

	  %j - Day of the year (001..366)
	          %-j  no-padded (1..366)

	Time (Hour, Minute, Second, Subsecond):
	  %H - Hour of the day, 24-hour clock, zero-padded  (00..23)
	          %-H  no-padded (0..23)
	  %k - Hour of the day, 24-hour clock, blank-padded ( 0..23)
	  %I - Hour of the day, 12-hour clock, zero-padded  (01..12)
	          %-I  no-padded (1..12)
	  %l - Hour of the day, 12-hour clock, blank-padded ( 1..12)
	  %P - Meridian indicator, lowercase (am or pm)
	  %p - Meridian indicator, uppercase (AM or PM)

	  %M - Minute of the hour (00..59)
	          %-M  no-padded (0..59)

	  %S - Second of the minute (00..60)
	          %-S  no-padded (0..60)

	  %L - Millisecond of the second (000..999)
	  %f - Microsecond of the second (000000..999999)
	  %N - Nanosecond  of the second (000000000..999999999)

	Time zone:
	  %z - Time zone as hour and minute offset from UTC (e.g. +0900)
	          %:z - hour and minute offset from UTC with a colon (e.g. +09:00)
	  %Z - Time zone abbreviation (e.g. MST)

	Weekday:
	  %A - Full weekday name (Sunday)
	  %a - Abbreviated weekday name (Sun)
	  %u - Day of the week (Monday is 1, 1..7)
	  %w - Day of the week (Sunday is 0, 0..6)

	ISO 8601 week-based year and week number:
	Week 1 of YYYY starts with a Monday and includes YYYY-01-04.
	The days in the year before the first week are in the last week of
	the previous year.
	  %G - Week-based year
	  %g - Last 2 digits of the week-based year (00..99)
	  %V - Week number of the week-based year (01..53)
	          %-V  no-padded (1..53)

	Week number:
	Week 1 of YYYY starts with a Sunday or Monday (according to %U or %W).
	The days in the year before the first week are in week 0.
	  %U - Week number of the year.  The week starts with Sunday.  (00..53)
	          %-U  no-padded (0..53)
	  %W - Week number of the year.  The week starts with Monday.  (00..53)
	          %-W  no-padded (0..53)

	Seconds since the Unix Epoch:
	  %s - Number of seconds since 1970-01-01 00:00:00 UTC.
	  %Q - Number of milliseconds since 1970-01-01 00:00:00 UTC.

	Literal string:
	  %n - Newline character (\n)
	  %t - Tab character (\t)
	  %% - Literal % character

	Combination:
	  %c - date and time (%a %b %e %T %Y)
	  %D - Date (%m/%d/%y)
	  %F - ISO 8601 date format (%Y-%m-%d)
	  %v - VMS date (%e-%b-%Y)
	  %x - Same as %D
	  %X - Same as %T
	  %r - 12-hour time (%I:%M:%S %p)
	  %R - 24-hour time (%H:%M)
	  %T - 24-hour time (%H:%M:%S)
	  %+ - date(1) (%a %b %e %H:%M:%S %Z %Y)

The modifiers “E” and “O” are ignored.
*/
package strftime
```

## File: `reference_test.go`
```go
//go:build reference

package strftime_test

import (
	"bytes"
	"context"
	"fmt"
	"os/exec"
	"strings"
	"testing"
	"time"

	"github.com/ncruces/go-strftime"
)

func TestFormat_ruby(t *testing.T) {
	if testing.Short() {
		t.SkipNow()
	}

	exe, err := exec.LookPath("ruby")
	if err != nil {
		t.Skip(err)
	}

	ref := reference.Format(time.RFC3339Nano)
	ctx, cancel := context.WithCancel(context.Background())
	t.Cleanup(cancel)

	ruby := func(format string) func(t *testing.T) {
		return func(t *testing.T) {
			script := fmt.Sprintf("print(DateTime.parse(%q).strftime(%q))", ref, format)
			cmd := exec.CommandContext(ctx, exe, "-e", "require 'date'", "-e", script)
			t.Parallel()

			want, err := cmd.CombinedOutput()
			if err != nil {
				t.Error(err)
			}

			if got := strftime.Format(format, reference); got != string(want) {
				t.Errorf("Format(%q) = %q, ruby wants %q", format, got, string(want))
			}
		}
	}

	for _, test := range timeTests {
		t.Run("", ruby(test.format))
	}
}

func TestFormat_osascript(t *testing.T) {
	if testing.Short() {
		t.SkipNow()
	}

	exe, err := exec.LookPath("osascript")
	if err != nil {
		t.Skip(err)
	}

	zone, _ := reference.Zone()
	unix := float64(reference.UnixNano()) / 1e9
	ctx, cancel := context.WithCancel(context.Background())
	t.Cleanup(cancel)

	osascript := func(pattern, format string) func(t *testing.T) {
		return func(t *testing.T) {
			script := fmt.Sprintf(`
				ObjC.import('Cocoa')
				var fmt = $.NSDateFormatter.alloc.init
				fmt.dateFormat = %q
				fmt.timeZone = $.NSTimeZone.timeZoneWithName(%q)
				fmt.locale = $.NSLocale.localeWithLocaleIdentifier("en_US_POSIX");
				fmt.stringFromDate($.NSDate.dateWithTimeIntervalSince1970(%g))
			`, pattern, zone, unix)
			cmd := exec.CommandContext(ctx, exe, "-l", "JavaScript")
			cmd.Stdin = strings.NewReader(script)
			t.Parallel()

			want, err := cmd.CombinedOutput()
			if err != nil {
				t.Error(err)
			}
			want = bytes.TrimSuffix(want, []byte("\n"))

			if got := strftime.Format(format, reference); got != string(want) {
				t.Errorf("Format(%q) = %q, osascript wants %q", format, got, string(want))
			}
		}
	}

	for _, test := range timeTests {
		if test.uts35 != "" {
			t.Run("", osascript(test.uts35, test.format))
		}
	}
}
```

## File: `specifiers.go`
```go
package strftime

import "strings"

// https://strftime.org/
func goLayout(spec, flag byte, parsing bool) string {
	switch spec {
	default:
		return ""

	case 'B':
		return "January"
	case 'b', 'h':
		return "Jan"
	case 'm':
		if flag == '-' || parsing {
			return "1"
		}
		return "01"
	case 'A':
		return "Monday"
	case 'a':
		return "Mon"
	case 'e':
		return "_2"
	case 'd':
		if flag == '-' || parsing {
			return "2"
		}
		return "02"
	case 'j':
		if flag == '-' {
			if parsing {
				return "__2"
			}
			return ""
		}
		return "002"
	case 'I':
		if flag == '-' || parsing {
			return "3"
		}
		return "03"
	case 'H':
		if flag == '-' && !parsing {
			return ""
		}
		return "15"
	case 'M':
		if flag == '-' || parsing {
			return "4"
		}
		return "04"
	case 'S':
		if flag == '-' || parsing {
			return "5"
		}
		return "05"
	case 'y':
		return "06"
	case 'Y':
		return "2006"
	case 'p':
		return "PM"
	case 'P':
		return "pm"
	case 'Z':
		return "MST"
	case 'z':
		if flag == ':' {
			if parsing {
				return "Z07:00"
			}
			return "-07:00"
		}
		if parsing {
			return "Z0700"
		}
		return "-0700"

	case '+':
		if parsing {
			return "Mon Jan _2 15:4:5 MST 2006"
		}
		return "Mon Jan _2 15:04:05 MST 2006"
	case 'c':
		if parsing {
			return "Mon Jan _2 15:4:5 2006"
		}
		return "Mon Jan _2 15:04:05 2006"
	case 'v':
		return "_2-Jan-2006"
	case 'F':
		if parsing {
			return "2006-1-2"
		}
		return "2006-01-02"
	case 'D', 'x':
		if parsing {
			return "1/2/06"
		}
		return "01/02/06"
	case 'r':
		if parsing {
			return "3:4:5 PM"
		}
		return "03:04:05 PM"
	case 'T', 'X':
		if parsing {
			return "15:4:5"
		}
		return "15:04:05"
	case 'R':
		if parsing {
			return "15:4"
		}
		return "15:04"

	case '%':
		return "%"
	case 't':
		return "\t"
	case 'n':
		return "\n"
	}
}

// https://nsdateformatter.com/
func uts35Pattern(spec, flag byte) string {
	switch spec {
	default:
		return ""

	case 'B':
		return "MMMM"
	case 'b', 'h':
		return "MMM"
	case 'm':
		if flag == '-' {
			return "M"
		}
		return "MM"
	case 'A':
		return "EEEE"
	case 'a':
		return "E"
	case 'd':
		if flag == '-' {
			return "d"
		}
		return "dd"
	case 'j':
		if flag == '-' {
			return "D"
		}
		return "DDD"
	case 'I':
		if flag == '-' {
			return "h"
		}
		return "hh"
	case 'H':
		if flag == '-' {
			return "H"
		}
		return "HH"
	case 'M':
		if flag == '-' {
			return "m"
		}
		return "mm"
	case 'S':
		if flag == '-' {
			return "s"
		}
		return "ss"
	case 'y':
		return "yy"
	case 'Y':
		return "yyyy"
	case 'g':
		return "YY"
	case 'G':
		return "YYYY"
	case 'V':
		if flag == '-' {
			return "w"
		}
		return "ww"
	case 'p':
		return "a"
	case 'Z':
		return "zzz"
	case 'z':
		if flag == ':' {
			return "xxx"
		}
		return "xx"
	case 'L':
		return "SSS"
	case 'f':
		return "SSSSSS"
	case 'N':
		return "SSSSSSSSS"

	case '+':
		return "E MMM d HH:mm:ss zzz yyyy"
	case 'c':
		return "E MMM d HH:mm:ss yyyy"
	case 'v':
		return "d-MMM-yyyy"
	case 'F':
		return "yyyy-MM-dd"
	case 'D', 'x':
		return "MM/dd/yy"
	case 'r':
		return "hh:mm:ss a"
	case 'T', 'X':
		return "HH:mm:ss"
	case 'R':
		return "HH:mm"

	case '%':
		return "%"
	case 't':
		return "\t"
	case 'n':
		return "\n"
	}
}

// http://man.he.net/man3/strftime
func okModifier(mod, spec byte) bool {
	if mod == 'E' {
		return strings.Contains("cCxXyY", string(spec))
	}
	if mod == 'O' {
		return strings.Contains("deHImMSuUVwWy", string(spec))
	}
	return false
}
```

## File: `strftime.go`
```go
package strftime

import (
	"bytes"
	"strconv"
	"time"
)

// Format returns a textual representation of the time value
// formatted according to the strftime format specification.
func Format(fmt string, t time.Time) string {
	buf := buffer(fmt)
	return string(AppendFormat(buf, fmt, t))
}

// AppendFormat is like Format, but appends the textual representation
// to dst and returns the extended buffer.
func AppendFormat(dst []byte, fmt string, t time.Time) []byte {
	var parser parser

	parser.literal = func(b byte) error {
		dst = append(dst, b)
		return nil
	}

	parser.format = func(spec, flag byte) error {
		switch spec {
		case 'A':
			dst = append(dst, t.Weekday().String()...)
			return nil
		case 'a':
			dst = append(dst, t.Weekday().String()[:3]...)
			return nil
		case 'B':
			dst = append(dst, t.Month().String()...)
			return nil
		case 'b', 'h':
			dst = append(dst, t.Month().String()[:3]...)
			return nil
		case 'm':
			dst = appendInt2(dst, int(t.Month()), flag)
			return nil
		case 'd':
			dst = appendInt2(dst, int(t.Day()), flag)
			return nil
		case 'e':
			dst = appendInt2(dst, int(t.Day()), ' ')
			return nil
		case 'I':
			dst = append12Hour(dst, t, flag)
			return nil
		case 'l':
			dst = append12Hour(dst, t, ' ')
			return nil
		case 'H':
			dst = appendInt2(dst, t.Hour(), flag)
			return nil
		case 'k':
			dst = appendInt2(dst, t.Hour(), ' ')
			return nil
		case 'M':
			dst = appendInt2(dst, t.Minute(), flag)
			return nil
		case 'S':
			dst = appendInt2(dst, t.Second(), flag)
			return nil
		case 'L':
			dst = append(dst, t.Format(".000")[1:]...)
			return nil
		case 'f':
			dst = append(dst, t.Format(".000000")[1:]...)
			return nil
		case 'N':
			dst = append(dst, t.Format(".000000000")[1:]...)
			return nil
		case 'y':
			dst = t.AppendFormat(dst, "06")
			return nil
		case 'Y':
			dst = t.AppendFormat(dst, "2006")
			return nil
		case 'C':
			dst = t.AppendFormat(dst, "2006")
			dst = dst[:len(dst)-2]
			return nil
		case 'U':
			dst = appendWeekNumber(dst, t, flag, true)
			return nil
		case 'W':
			dst = appendWeekNumber(dst, t, flag, false)
			return nil
		case 'V':
			_, w := t.ISOWeek()
			dst = appendInt2(dst, w, flag)
			return nil
		case 'g':
			y, _ := t.ISOWeek()
			dst = year(y).AppendFormat(dst, "06")
			return nil
		case 'G':
			y, _ := t.ISOWeek()
			dst = year(y).AppendFormat(dst, "2006")
			return nil
		case 's':
			dst = strconv.AppendInt(dst, t.Unix(), 10)
			return nil
		case 'Q':
			dst = strconv.AppendInt(dst, t.UnixMilli(), 10)
			return nil
		case 'w':
			w := t.Weekday()
			dst = appendInt1(dst, int(w))
			return nil
		case 'u':
			if w := t.Weekday(); w == 0 {
				dst = append(dst, '7')
			} else {
				dst = appendInt1(dst, int(w))
			}
			return nil
		case 'j':
			if flag == '-' {
				dst = strconv.AppendInt(dst, int64(t.YearDay()), 10)
			} else {
				dst = t.AppendFormat(dst, "002")
			}
			return nil
		}

		if layout := goLayout(spec, flag, false); layout != "" {
			dst = t.AppendFormat(dst, layout)
			return nil
		}

		dst = append(dst, '%')
		if flag != 0 {
			dst = append(dst, flag)
		}
		dst = append(dst, spec)
		return nil
	}

	parser.parse(fmt)
	return dst
}

// Parse converts a textual representation of time to the time value it represents
// according to the strptime format specification.
//
// The following specifiers are not supported for parsing:
//
//	%g %k %l %s %u %w %C %G %Q %U %V %W
//
// You must also avoid digits and these letter sequences
// in fmt literals:
//
//	Jan Mon MST PM pm
func Parse(fmt, value string) (time.Time, error) {
	pattern, err := layout(fmt, true)
	if err != nil {
		return time.Time{}, err
	}
	return time.Parse(pattern, value)
}

// Layout converts a strftime format specification
// to a Go time pattern specification.
//
// The following specifiers are not supported by Go patterns:
//
//	%f %g %k %l %s %u %w %C %G %L %N %Q %U %V %W
//
// You must also avoid digits and these letter sequences
// in fmt literals:
//
//	Jan Mon MST PM pm
func Layout(fmt string) (string, error) {
	return layout(fmt, false)
}

func layout(fmt string, parsing bool) (string, error) {
	dst := buffer(fmt)
	var parser parser

	parser.literal = func(b byte) error {
		if '0' <= b && b <= '9' {
			return literalErr(b)
		}
		dst = append(dst, b)
		if b == 'M' || b == 'T' || b == 'm' || b == 'n' {
			switch {
			case bytes.HasSuffix(dst, []byte("Jan")):
				return literalErr("Jan")
			case bytes.HasSuffix(dst, []byte("Mon")):
				return literalErr("Mon")
			case bytes.HasSuffix(dst, []byte("MST")):
				return literalErr("MST")
			case bytes.HasSuffix(dst, []byte("PM")):
				return literalErr("PM")
			case bytes.HasSuffix(dst, []byte("pm")):
				return literalErr("pm")
			}
		}
		return nil
	}

	parser.format = func(spec, flag byte) error {
		if layout := goLayout(spec, flag, parsing); layout != "" {
			dst = append(dst, layout...)
			return nil
		}

		switch spec {
		default:
			return formatError{}

		case 'L', 'f', 'N':
			if bytes.HasSuffix(dst, []byte(".")) || bytes.HasSuffix(dst, []byte(",")) {
				switch spec {
				default:
					dst = append(dst, "000"...)
				case 'f':
					dst = append(dst, "000000"...)
				case 'N':
					dst = append(dst, "000000000"...)
				}
				return nil
			}
			return formatError{message: "must follow '.' or ','"}
		}
	}

	if err := parser.parse(fmt); err != nil {
		return "", err
	}
	return string(dst), nil
}

// UTS35 converts a strftime format specification
// to a Unicode Technical Standard #35 Date Format Pattern.
//
// The following specifiers are not supported by UTS35:
//
//	%e %k %l %u %w %C %P %U %W
func UTS35(fmt string) (string, error) {
	const quote = '\''
	var quoted bool
	dst := buffer(fmt)

	var parser parser

	parser.literal = func(b byte) error {
		if b == quote {
			dst = append(dst, quote, quote)
			return nil
		}
		if !quoted && ('a' <= b && b <= 'z' || 'A' <= b && b <= 'Z') {
			dst = append(dst, quote)
			quoted = true
		}
		dst = append(dst, b)
		return nil
	}

	parser.format = func(spec, flag byte) error {
		if quoted {
			dst = append(dst, quote)
			quoted = false
		}
		if pattern := uts35Pattern(spec, flag); pattern != "" {
			dst = append(dst, pattern...)
			return nil
		}
		return formatError{}
	}

	if err := parser.parse(fmt); err != nil {
		return "", err
	}
	if quoted {
		dst = append(dst, quote)
	}
	return string(dst), nil
}

func buffer(format string) (buf []byte) {
	const bufSize = 64
	max := len(format) + 10
	if max < bufSize {
		var b [bufSize]byte
		buf = b[:0]
	} else {
		buf = make([]byte, 0, max)
	}
	return
}

func year(y int) time.Time {
	return time.Date(y, time.January, 1, 0, 0, 0, 0, time.UTC)
}

func appendWeekNumber(dst []byte, t time.Time, flag byte, sunday bool) []byte {
	offset := int(t.Weekday())
	if sunday {
		offset = 6 - offset
	} else if offset != 0 {
		offset = 7 - offset
	}
	return appendInt2(dst, (t.YearDay()+offset)/7, flag)
}

func append12Hour(dst []byte, t time.Time, flag byte) []byte {
	h := t.Hour()
	if h == 0 {
		h = 12
	} else if h > 12 {
		h -= 12
	}
	return appendInt2(dst, h, flag)
}

func appendInt1(dst []byte, i int) []byte {
	return append(dst, byte('0'+i))
}

func appendInt2(dst []byte, i int, flag byte) []byte {
	if flag == 0 || i >= 10 {
		return append(dst, smallsString[i*2:i*2+2]...)
	}
	if flag == ' ' {
		dst = append(dst, flag)
	}
	return appendInt1(dst, i)
}

const smallsString = "" +
	"00010203040506070809" +
	"10111213141516171819" +
	"20212223242526272829" +
	"30313233343536373839" +
	"40414243444546474849" +
	"50515253545556575859" +
	"60616263646566676869" +
	"70717273747576777879" +
	"80818283848586878889" +
	"90919293949596979899"
```

## File: `strftime_test.go`
```go
package strftime_test

import (
	"net/http"
	"testing"
	"time"

	"github.com/ncruces/go-strftime"
)

var reference = time.Date(2009, 8, 7, 6, 5, 4, 300000000, time.UTC)

var timeTests = []struct {
	format string
	layout string
	uts35  string
	time   string
}{
	// Date and time formats
	{"%c", time.ANSIC, "E MMM d HH:mm:ss yyyy", "Fri Aug  7 06:05:04 2009"},
	{"%+", time.UnixDate, "E MMM d HH:mm:ss zzz yyyy", "Fri Aug  7 06:05:04 UTC 2009"},
	{"%FT%TZ", time.RFC3339[:20], "yyyy-MM-dd'T'HH:mm:ss'Z'", "2009-08-07T06:05:04Z"},
	{"%a %b %e %T %Y", time.ANSIC, "", "Fri Aug  7 06:05:04 2009"},
	{"%a %b %e %T %Z %Y", time.UnixDate, "", "Fri Aug  7 06:05:04 UTC 2009"},
	{"%a %b %d %T %z %Y", time.RubyDate, "E MMM dd HH:mm:ss xx yyyy", "Fri Aug 07 06:05:04 +0000 2009"},
	{"%a %h %d %T %z %Y", time.RubyDate, "E MMM dd HH:mm:ss xx yyyy", "Fri Aug 07 06:05:04 +0000 2009"},
	{"%a, %d %b %Y %T %Z", time.RFC1123, "E, dd MMM yyyy HH:mm:ss zzz", "Fri, 07 Aug 2009 06:05:04 UTC"},
	{"%a, %d %b %Y %T GMT", http.TimeFormat, "E, dd MMM yyyy HH:mm:ss 'GMT'", "Fri, 07 Aug 2009 06:05:04 GMT"},
	{"%Y-%m-%dT%H:%M:%SZ", time.RFC3339[:20], "yyyy-MM-dd'T'HH:mm:ss'Z'", "2009-08-07T06:05:04Z"},
	// Date formats
	{"%v", "_2-Jan-2006", "d-MMM-yyyy", " 7-Aug-2009"},
	{"%F", "2006-01-02", "yyyy-MM-dd", "2009-08-07"},
	{"%D", "01/02/06", "MM/dd/yy", "08/07/09"},
	{"%x", "01/02/06", "MM/dd/yy", "08/07/09"},
	{"%e-%b-%Y", "_2-Jan-2006", "", " 7-Aug-2009"},
	{"%Y-%m-%d", "2006-01-02", "yyyy-MM-dd", "2009-08-07"},
	{"%m/%d/%y", "01/02/06", "MM/dd/yy", "08/07/09"},
	// Time formats
	{"%R", "15:04", "HH:mm", "06:05"},
	{"%T", "15:04:05", "HH:mm:ss", "06:05:04"},
	{"%X", "15:04:05", "HH:mm:ss", "06:05:04"},
	{"%r", "03:04:05 PM", "hh:mm:ss a", "06:05:04 AM"},
	{"%H:%M", "15:04", "HH:mm", "06:05"},
	{"%H:%M:%S", "15:04:05", "HH:mm:ss", "06:05:04"},
	{"%I:%M:%S %p", "03:04:05 PM", "hh:mm:ss a", "06:05:04 AM"},
	// Misc
	{"%g", "", "YY", "09"},
	{"%-EC", "", "", "20"},
	{"%-Od", "2", "d", "7"},
	{"%Ey", "06", "yy", "09"},
	{"%Oy", "06", "yy", "09"},
	{"%:z", "-07:00", "xxx", "+00:00"},
	{"%V/%G", "", "ww/YYYY", "32/2009"},
	{"%-V/%G", "", "w/YYYY", "32/2009"},
	{"%Cth Century Fox", "", "", "20th Century Fox"},
	{"%-d-%-m-%Y", "2-1-2006", "d-M-yyyy", "7-8-2009"},
	{"%-Hh%-Mm%-Ss", "", "H'h'm'm's's'", "6h5m4s"},
	{"%-I o'clock", "3 o'clock", "h 'o''clock'", "6 o'clock"},
	{"%-M past %-I %p", "4 past 3 PM", "m 'past 'h a", "5 past 6 AM"},
	{"%fμs since %T", "", "SSSSSSμ's since 'HH:mm:ss", "300000μs since 06:05:04"},
	{"%Nns since %T", "", "SSSSSSSSS'ns since 'HH:mm:ss", "300000000ns since 06:05:04"},
	{"%-S.%Ls since %R", "5.000s since 15:04", "s.SSS's since 'HH:mm", "4.300s since 06:05"},
	{"%-S,%fs since %R", "5,000000s since 15:04", "s,SSSSSS's since 'HH:mm", "4,300000s since 06:05"},
	{"%-S.%Ns since %R", "5.000000000s since 15:04", "s.SSSSSSSSS's since 'HH:mm", "4.300000000s since 06:05"},
	{"%-B, is month #%-m of the year", "January, is month #1 of the year", "MMMM, 'is month #'M 'of the year'", "August, is month #8 of the year"},
	{"%-d-%b-%Y is day %j of the year", "2-Jan-2006 is day 002 of the year", "d-MMM-yyyy 'is day 'DDD 'of the year'", "7-Aug-2009 is day 219 of the year"},
	{"%-d-%b-%Y is day %-j of the year", "", "d-MMM-yyyy 'is day 'D 'of the year'", "7-Aug-2009 is day 219 of the year"},
	{"%-A, is day #%u of the week", "", "", "Friday, is day #5 of the week"},
	// Parsing
	{"", "", "", ""},
	{"%", "%", "%", "%"},
	{"%%", "%", "%", "%"},
	{"%-", "%-", "%-", "%-"},
	{"%n", "\n", "\n", "\n"},
	{"%t", "\t", "\t", "\t"},
	{"%q", "", "", "%q"},
	{"%-q", "", "", "%-q"},
	{"'", "'", "''", "'"},
	{"0", "", "0", "0"},
	{"9", "", "9", "9"},
	{"100%", "", "100%", "100%"},
	{"Monday", "", "'Monday'", "Monday"},
	{"January", "", "'January'", "January"},
	{"MST", "", "'MST'", "MST"},
	{"AM", "AM", "'AM'", "AM"},
	{"am", "am", "'am'", "am"},
	{"PM", "", "'PM'", "PM"},
	{"pm", "", "'pm'", "pm"},
}

func TestFormat(t *testing.T) {
	for _, test := range timeTests {
		if got := strftime.Format(test.format, reference); got != test.time {
			t.Errorf("Format(%q) = %q, want %q", test.format, got, test.time)
		}
	}
}

func TestFormat_Unix(t *testing.T) {
	tm := time.Unix(123456, 789*int64(time.Millisecond))

	if got := strftime.Format("%s", tm); got != "123456" {
		t.Errorf("Format(%q) = %q, want %q", "%s", got, "123456")
	}

	if got := strftime.Format("%Q", tm); got != "123456789" {
		t.Errorf("Format(%q) = %q, want %q", "%Q", got, "123456789")
	}
}

func TestFormat_Hour(t *testing.T) {
	hours := []struct{ hour12, hour24 string }{
		0:  {"12", " 0"},
		1:  {" 1", " 1"},
		2:  {" 2", " 2"},
		3:  {" 3", " 3"},
		4:  {" 4", " 4"},
		5:  {" 5", " 5"},
		6:  {" 6", " 6"},
		7:  {" 7", " 7"},
		8:  {" 8", " 8"},
		9:  {" 9", " 9"},
		10: {"10", "10"},
		11: {"11", "11"},
		12: {"12", "12"},
		13: {" 1", "13"},
		14: {" 2", "14"},
		15: {" 3", "15"},
		16: {" 4", "16"},
		17: {" 5", "17"},
		18: {" 6", "18"},
		19: {" 7", "19"},
		20: {" 8", "20"},
		21: {" 9", "21"},
		22: {"10", "22"},
		23: {"11", "23"},
	}

	for h := 0; h < len(hours); h++ {
		base := reference.Add(time.Duration(h) * time.Hour)
		want := hours[base.Hour()]
		if got := strftime.Format("%l", base); got != want.hour12 {
			t.Errorf("Format(%q) = %q, want %q", "%l", got, want.hour12)
		}
		if got := strftime.Format("%k", base); got != want.hour24 {
			t.Errorf("Format(%q) = %q, want %q", "%k", got, want.hour24)
		}
	}
}

func TestFormat_Weekday(t *testing.T) {
	weekdays := []struct{ sunday0, sunday7 string }{
		time.Sunday:    {"0", "7"},
		time.Monday:    {"1", "1"},
		time.Tuesday:   {"2", "2"},
		time.Wednesday: {"3", "3"},
		time.Thursday:  {"4", "4"},
		time.Friday:    {"5", "5"},
		time.Saturday:  {"6", "6"},
	}

	for d := 0; d < len(weekdays); d++ {
		base := reference.AddDate(0, 0, d)
		want := weekdays[base.Weekday()]
		if got := strftime.Format("%w", base); got != want.sunday0 {
			t.Errorf("Format(%q) = %q, want %q", "%w", got, want.sunday0)
		}
		if got := strftime.Format("%u", base); got != want.sunday7 {
			t.Errorf("Format(%q) = %q, want %q", "%u", got, want.sunday7)
		}
	}
}

func TestFormat_WeekNumber(t *testing.T) {
	for y := 2000; y < 2020; y++ {
		sunday := "00"
		monday := "00"
		for d := 1; d < 8; d++ {
			base := time.Date(y, time.January, d, 0, 0, 0, 0, time.UTC)

			switch base.Weekday() {
			case time.Sunday:
				sunday = "01"
			case time.Monday:
				monday = "01"
			}

			if got := strftime.Format("%U", base); got != sunday {
				t.Errorf("Format(%q, %d) = %q, want %q", "%U", base.Unix(), got, sunday)
			}
			if got := strftime.Format("%W", base); got != monday {
				t.Errorf("Format(%q, %d) = %q, want %q", "%W", base.Unix(), got, monday)
			}
		}
	}
}

func TestParse(t *testing.T) {
	for _, test := range timeTests {
		if got, err := strftime.Parse(test.format, test.time); err != nil && test.layout != "" {
			t.Errorf("Parse(%q) = %v", test.format, err)
		} else if err != nil && !got.IsZero() {
			t.Errorf("Parse(%q) = %v", test.format, got)
		} else if then := strftime.Format(test.format, got); err == nil && then != test.time {
			t.Errorf("Parse(%q) = %q, want %q", test.format, got, test.time)
		} else if err != nil {
			t.Logf("Parse(%q) = %v", test.format, err)
		}
	}
}

func TestParse_Error(t *testing.T) {
	if got, err := strftime.Parse("%C", ""); err == nil || !got.IsZero() {
		t.Errorf("Parse(%q) = %v", "%C", got)
	}
}

func TestParse_Table(t *testing.T) {
	var parseTests = []struct {
		format string
		time   string
	}{
		{"%FT%T%:z", "2009-08-07T06:05:04.300Z"},
		{"%FT%T%:z", "2009-8-7T6:5:4.3Z"},
		{"%r %D", "06:05:04.3 AM 08/07/09"},
		{"%r %D", "6:5:4.3 AM 8/7/09"},
	}

	for _, test := range parseTests {
		if got, err := strftime.Parse(test.format, test.time); err != nil {
			t.Errorf("Parse(%q) = %v", test.format, err)
		} else if got != reference {
			t.Errorf("Parse(%q) = %q, want %q", test.format, got, test.time)
		}
	}
}

func TestLayout(t *testing.T) {
	for _, test := range timeTests {
		if got, err := strftime.Layout(test.format); err != nil && test.layout != "" {
			t.Errorf("Layout(%q) = %v", test.format, err)
		} else if got != test.layout {
			t.Errorf("Layout(%q) = %q, want %q", test.format, got, test.layout)
		} else if err != nil {
			t.Logf("Layout(%q) = %v", test.format, err)
		}
	}
}

func TestLayout_Format(t *testing.T) {
	for _, test := range timeTests {
		if test.layout == "" {
			continue
		}
		if got := reference.Format(test.layout); got != test.time {
			t.Errorf("Format(%q) = %q, want %q", test.layout, got, test.time)
		}
	}
}

func TestUTS35(t *testing.T) {
	for _, test := range timeTests {
		if got, err := strftime.UTS35(test.format); err != nil && test.uts35 != "" {
			t.Errorf("UTS35(%q) = %v", test.format, err)
		} else if got != test.uts35 {
			t.Errorf("UTS35(%q) = %q, want %q", test.format, got, test.uts35)
		} else if err != nil {
			t.Logf("UTS35(%q) = %v", test.format, err)
		}
	}
}
```

