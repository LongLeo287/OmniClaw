---
id: github.com-tieske-date-fe9c734f-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:27.793096
---

# KNOWLEDGE EXTRACT: github.com_Tieske_date_fe9c734f
> **Extracted on:** 2026-04-01 15:25:44
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524500/github.com_Tieske_date_fe9c734f

---

## File: `.busted`
```
return {
  default = {
    verbose = true,
    coverage = true,
    output = "gtest",
    ROOT = {
      "spec/",
      --"examples/vcache.lua",
    },
  },
}
```

## File: `.editorconfig`
```
root = true

[*]
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
charset = utf-8

[*.lua]
indent_style = space
indent_size = 2

[*.rockspec]
indent_style = space
indent_size = 2

[Makefile]
indent_style = tab
```

## File: `.gitignore`
```
.DS_store
luacov.*
*.rock
```

## File: `.luacheckrc`
```
unused_args     = false
redefined       = false
max_line_length = false

globals = {
--    "ngx",
}

not_globals = {
    -- deprecated Lua 5.0 functions
    "string.len",
    "table.getn",
}

include_files = {
  "**/*.lua",
  "**/*.rockspec",
  ".busted",
  ".luacheckrc",
}

files["spec/**/*.lua"] = {
    std = "+busted",
}

exclude_files = {
    -- The Github Actions Lua Environment
    ".lua",
    ".luarocks",
    ".install",
}
```

## File: `.luacov`
```
modules = {
   ["date"] = "src/date.lua",
   ["date.*"] = "src"
}
runreport = true
deletestats = false
```

## File: `LICENSE`
```
The MIT License (MIT) http://opensource.org/licenses/MIT

Copyright (c) 2013-2021 Thijs Schreijer

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
```

## File: `Makefile`
```
# additional Busted options to pass
BUSTED:=

# SCM rockspec label; scm/cvs/dev
SCM_LABEL:=$(shell cat *.rockspec | grep "local package_version" | sed "s/ //g" | sed "s/localpackage_version=//g" | sed "s/\"//g")
ROCK_REV:=$(shell cat *.rockspec | grep "local rockspec_revision" | sed "s/ //g" | sed "s/localrockspec_revision=//g" | sed "s/\"//g")
ROCK_NAME:=$(shell cat *.rockspec | grep "local package_name" | sed "s/ //g" | sed "s/localpackage_name=//g" | sed "s/\"//g")
ROCKSPEC:=${ROCK_NAME}-${SCM_LABEL}-${ROCK_REV}.rockspec
TAB=$(shell printf "\t")

# dev/test dependencies; versions can be pinned. Example: "ldoc 1.4.6"
DEV_ROCKS = "busted" "luacheck" "luacov"


target_not_specified: help
	@exit 1


help:
	@echo "Available make targets for ${ROCK_NAME}:"
	@echo ""
	@echo "install:     uses LuaRocks to install ${ROCK_NAME}"
	@echo "uninstall:   uninstalls ALL versions of ${ROCK_NAME} (using LuaRocks with"
	@echo "             the '--force' flag)"
	@echo "clean:       removes LuaCov output and packed rocks"
	@echo "test:        runs the test suite using Busted"
	@echo "testinst:    installs ${ROCK_NAME} and runs tests using the installed version"
	@echo "             (this modifies the local installation, but also tests the"
	@echo "             .rockspec file). This is best used when testing in CI."
	@echo "lint:        will validate all 'rockspec' files using LuaRocks, and the"
	@echo "             '.lua' files with LuaCheck"
	@echo "dev:         installs the development dependencies (Busted, LuaCheck, etc.)"
	@echo "help:        displays this list of make targets"
	@echo ""


install: luarocks
	luarocks make


uninstall: luarocks
	if (luarocks list --porcelain ${ROCK_NAME} | grep "^${ROCK_NAME}${TAB}" | grep -q "installed") ; then \
	  luarocks remove ${ROCK_NAME} --force; \
	fi;


# note: restore the docs to the last committed version
clean: clean_luacov clean_luarocks


.PHONY: test
test: clean_luacov dev
	busted ${BUSTED}


# test while having the code installed; also tests the rockspec, but
# this will modify the local luarocks installation/tree!!
.PHONY: testinst
testinst: clean_luacov dev uninstall install
	busted --lpath="" --cpath="" ${BUSTED}


.PHONY: lint
lint: dev
	@echo "luarocks lint ..."
	@for spec in $(shell find . -type f -name "*.rockspec") ; do \
	  (luarocks lint $$spec && echo "$$spec [OK]") || (echo "$$spec [NOK]"; exit 1); \
	done
	luacheck .


.PHONY: dev
dev: luarocks
	@for rock in $(DEV_ROCKS) ; do \
	  (luarocks list --porcelain $$rock | grep -q "installed") || (luarocks install $$rock || exit 1); \
	done;


.PHONY: clean_luarocks
clean_luarocks:
	$(RM) *.rock


.PHONY: clean_luacov
clean_luacov:
	$(RM) luacov.report.out luacov.stats.out


.PHONY: luarocks
luarocks:
	@which luarocks > /dev/null || (echo "LuaRocks was not found. Please install and/or make available in the path." && exit 1)
```

## File: `README.md`
```markdown
# LuaDate v2.2

[![Unix build](https://img.shields.io/github/actions/workflow/status/Tieske/date/unix_build.yml?branch=master&label=Unix%20build&logo=linux)](https://github.com/Tieske/date/actions/workflows/unix_build.yml)
[![Coveralls code coverage](https://img.shields.io/coveralls/github/Tieske/date?logo=coveralls)](https://coveralls.io/github/Tieske/date)
[![Lint](https://github.com/Tieske/date/workflows/Lint/badge.svg)](https://github.com/Tieske/date/actions/workflows/lint.yml)
[![SemVer](https://img.shields.io/github/v/tag/Tieske/date?color=brightgreen&label=SemVer&logo=semver&sort=semver)](CHANGELOG.md)

Lua Date and Time module for Lua 5.x.

## Features:

* Date and Time string parsing.
* Time addition and subtraction.
* Time span calculation.
* Support ISO 8601 Dates.
* Local time support.
* Lua module (not binary).
* Formats Date and Time like strftime.

## License

[MIT license](http://opensource.org/licenses/MIT).

## Documentation

Documentation is available in the `doc` folder, or [online at Github](http://tieske.github.io/date/).

## Tests

Tests are located in the `spec` directory and can be run using [busted](http://olivinelabs.com/busted/).

## Changelog:

### Releasing:
- search for "copyright" and update all occurences with proper years
- update version in:
  - `README.md` (at the top)
  - `date.lua` (at the top, and exported field `date.version`)
  - `index.html` (appr. line 20)
- update changelog below
- update rockspec
- commit as `release x.y.z` (omit trailing 0)
- tag as `version_x.y.z` (omit trailing 0)
- push commit & tags
- upload rock to luarocks

### Changes:

#### v2.2.1 released 6-Sep-2023
  - fix parsing timezone offset after a decimal number [#33](https://github.com/Tieske/date/pull/33)
  - also accept "," as a decimal separator [#31](https://github.com/Tieske/date/pull/31)
  - fix bad function call (no functional impact) [#34](https://github.com/Tieske/date/pull/34)

#### v2.2
  - add 'centuryflip' to set 2 digit year interpretation [#26](https://github.com/Tieske/date/pull/26)
#### v2.1.3
  - fix rockspec for Lua 5.4
#### v2.1.2
  - fix scientific notation [#9](https://github.com/Tieske/date/pull/9), now available for Lua 5.3
#### v2.1.1
  - fix for '>=' operator [#3](https://github.com/Tieske/date/pull/3), added test suite, added Travis CI, license MIT
#### v2.1
  - Lua 5.2 support. Global 'date' will no longer be set.
#### v2.0
  - original by Jas Latrix
```

## File: `date-dev-1.rockspec`
```
local package_name = "date"
local package_version = "dev"
local rockspec_revision = "1"
local github_account_name = "Tieske"
local github_repo_name = package_name
local git_checkout = package_version == "dev" and "master" or ("version_"..package_version)

package = package_name
version = package_version .. "-" .. rockspec_revision

source = {
  url = "git+https://github.com/"..github_account_name.."/"..github_repo_name..".git",
  branch = git_checkout
}

description = {
  summary = "Date & Time module for Lua 5.x",
  detailed = [[
    Pure Lua Date & Time module for Lua 5.x featuring date and time string
    parsing, time addition & subtraction, time span calculation, support for
    ISO 8601 dates, local time support, strftime-like formatting.
  ]],
  license = "MIT",
  homepage = "https://github.com/"..github_account_name.."/"..github_repo_name,
}

dependencies = {
  "lua >= 5.0, < 5.6"
}

build = {
  type = "builtin",
  modules = {
    date = "src/date.lua"
  },
  copy_directories = { "docs" },
}
```

## File: `docs/index.html`
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta name="generator" content=
  "HTML Tidy for Linux/x86 (vers 25 March 2009), see www.w3.org" />
  <meta http-equiv="Content-Type" content="text/html; charset=us-ascii" />

  <title>LuaDate v2</title>
  <link rel="stylesheet" href="main.css" type="text/css" />
  <meta name="generator" content="DocBook XSL Stylesheets V1.70.1" />
</head>

<body bgcolor="white" text="black" link="#0000FF" vlink="#840084" alink="#0000FF">
  <div class="article" lang="en" xml:lang="en">
    <div class="titlepage">
      <div>
        <div>
          <h2 class="title"><a name="id90891" id="id90891"></a>LuaDate v2.2.1</h2>
        </div>

        <div>
          <h3 class="subtitle"><i>Lua Date and Time module for Lua 5.x.</i></h3>
        </div>

        <div>
          <div class="author">
            <h3 class="author"><span class="firstname">Jas</span> <span class=
            "surname">Latrix</span></h3>
          </div>
        </div>

        <div>
          <p class="copyright">Copyright &copy; 2005-2006 Jas Latrix <code class=
          "email">&lt;<a href=
          "mailto:jastejada@yahoo.com">jastejada@yahoo.com</a>&gt;</code></p>

          <p class="copyright">Copyright &copy; 2013-2021 Thijs
          Schreijer</p>
        </div>

        <div>
          <div class="legalnotice">
            <a name="id349744" id="id349744"></a>Licensed under <a href="http://opensource.org/licenses/MIT">MIT license</a>.
          </div>
        </div>
      </div>
      <hr />
    </div>

    <div class="toc">
      <p><b>Table of Contents</b></p>

      <dl>
        <dt><span class="section"><a href="#intro">1. Introduction</a></span></dt>

        <dt><span class="section"><a href="#Limits">2. Limits</a></span></dt>

        <dt><span class="section"><a href="#LocalTimeSupport">3. Local time
        support</a></span></dt>

        <dt><span class="section"><a href="#ParsableDateValue">4. Parsable date
        value</a></span></dt>

        <dt><span class="section"><a href="#ParsableMonthValue">5. Parsable month
        value</a></span></dt>

        <dt><span class="section"><a href="#date">6. date</a></span></dt>

        <dd>
          <dl>
            <dt><span class="section"><a href="#date-id96473">6.1. Function(s) of
            date</a></span></dt>

            <dt><span class="section"><a href="#date-id95781">6.2. Method(s) of
            date</a></span></dt>
          </dl>
        </dd>

        <dt><span class="section"><a href="#dateObject">7. dateObject</a></span></dt>

        <dd>
          <dl>
            <dt><span class="section"><a href="#DaysAndTick">7.1. How Date and Time are
            stored in <code class="classname">dateObject</code></a></span></dt>

            <dt><span class="section"><a href="#SupportedMetaMethods">7.2. Supported
            MetaMethods</a></span></dt>

            <dt><span class="section"><a href="#dateObject-id94476">7.3. Method(s) of
            dateObject</a></span></dt>
          </dl>
        </dd>

        <dt><span class="section"><a href="#history">8. History</a></span></dt>

        <dt><span class="section"><a href="#ackno">9. Acknowledgement</a></span></dt>
      </dl>
    </div>

    <div class="section" lang="en" xml:lang="en">
      <div class="titlepage">
        <div>
          <div>
            <h2 class="title" style="clear: both"><a name="intro" id=
            "intro"></a>1.&nbsp;Introduction</h2>
          </div>
        </div>
      </div><em class="firstterm">LuaDate</em> is a Lua module for date and time
      calculation and retrieval using the Gregorian Date system.

      <p>To Load the module call <code class="code">local date = require"date"</code> in
      your script. Make sure Lua can find the source file <code class=
      "filename">date.lua</code>. No global table <code class="classname">date</code>
      will be created. Use the metamethod <a href="#date.__call">__call</a> to construct
      a <a href="#dateObject">dateObject</a> see example below:</p>
      <pre class="programlisting">
local date = require "date"
-- prints all FRIDAY the 13TH dates between year 2000 and 2010
for i = 2000, 2010 do
        -- year jan 1
        x = date(i, 1, 1)
        -- from january to december
        for j = 1, 12 do
                -- set date to 13, check if friday
                if x:setmonth(j, 13):getweekday() == 6 then
                        print(x:fmt("%A, %B %d %Y"))
                end
        end
end

--- OUTPUT ---
--&gt; Friday, October 13 2000
--&gt; Friday, April 13 2001
--&gt; Friday, July 13 2001
--&gt; Friday, September 13 2002
--&gt; Friday, December 13 2002
--&gt; Friday, June 13 2003
--&gt; Friday, February 13 2004
--&gt; Friday, August 13 2004
--&gt; Friday, May 13 2005
--&gt; Friday, January 13 2006
--&gt; Friday, October 13 2006
--&gt; Friday, April 13 2007
--&gt; Friday, July 13 2007
--&gt; Friday, June 13 2008
--&gt; Friday, February 13 2009
--&gt; Friday, March 13 2009
--&gt; Friday, November 13 2009
--&gt; Friday, August 13 2010
</pre>
    </div>

    <div class="section" lang="en" xml:lang="en">
      <div class="titlepage">
        <div>
          <div>
            <h2 class="title" style="clear: both"><a name="Limits" id=
            "Limits"></a>2.&nbsp;Limits</h2>
          </div>
        </div>
      </div>

      <div class="itemizedlist">
        <ul type="disc">
          <li>This module does not recognize leap seconds.</li>

          <li>It assumes that a day has exactly <code class="constant">24*60*60</code>
          seconds.</li>

          <li>The Lua number must be a double C data type</li>

          <li>This module supports dates that are greater than <code class="constant">Mon
          Jan 01 1000000 BCE 00:00:00</code> and less than <code class="constant">Mon Jan
          01 1000001 00:00:00</code>.</li>

          <li>see <a href="#LocalTimeSupport">Local time support</a> for local time
          limts</li>
        </ul>
      </div>
    </div>

    <div class="section" lang="en" xml:lang="en">
      <div class="titlepage">
        <div>
          <div>
            <h2 class="title" style="clear: both"><a name="LocalTimeSupport" id=
            "LocalTimeSupport"></a>3.&nbsp;Local time support</h2>
          </div>
        </div>
      </div>This module also supports local time. Local Time is;

      <div class="blockquote">
        <blockquote class="blockquote">
          Local = UTC + bias
        </blockquote>
      </div>The <span class="emphasis"><em>bias</em></span> is time zone offset plus the
      daylight savings if in effect. The <span class="emphasis"><em>bias</em></span> is
      retrieve using the Lua function <code class="code">os.date</code> and <code class=
      "code">os.time</code>. It assumes that the Lua function <code class=
      "code">os.time</code> <span class="bold"><strong>returns the number of seconds
      since the start time (called "epoch")</strong></span>. If the time value is outside
      the allowable range of times, usually <code class="constant">Jan 01 1970
      00:00:00</code> to <code class="constant">Jan 19 2038 03:14:07</code> the bias will
      be retrieve using the equivalent year inside the allowable range. Two years are
      considered to equivalent if they have the same leap year ness and starting weekday.

      <p>The function that needs local time support are <a href="#date.__call" title=
      "6.2.1.&nbsp;__call">date(true)</a> (get the current UTC time), <a href=
      "#date.__call" title="6.2.1.&nbsp;__call">date(false)</a> (get the current local
      time), <a href="#date.__call" title="6.2.1.&nbsp;__call">date(num_time)</a>,
      <a href="#dateObject.getbias" title="7.3.10.&nbsp;getbias">dateObj:getbias()</a>,
      <a href="#dateObject.fmt" title="7.3.9.&nbsp;fmt">dateObject:fmt(str)</a> (when str
      has a '%Z' or '%z'),</p>
    </div>

    <div class="section" lang="en" xml:lang="en">
      <div class="titlepage">
        <div>
          <div>
            <h2 class="title" style="clear: both"><a name="ParsableDateValue" id=
            "ParsableDateValue"></a>4.&nbsp;Parsable date value</h2>
          </div>
        </div>
      </div>Parsable date value is a lua value that can be converted to a <a href=
      "#dateObject">dateObject</a>. This value must be <code class="code">num_time</code>
      or <code class="code">tbl_date</code> or <code class="code">str_date</code> or
      <code class="code">bool_now</code> argument describe in the <a href=
      "#date">date</a> library <a href="#date.__call">__call</a> method.
    </div>

    <div class="section" lang="en" xml:lang="en">
      <div class="titlepage">
        <div>
          <div>
            <h2 class="title" style="clear: both"><a name="ParsableMonthValue" id=
            "ParsableMonthValue"></a>5.&nbsp;Parsable month value</h2>
          </div>
        </div>
      </div>If a function needs a month value it must be a string or a number. If the
      value is a <code class="constant">string</code>, it must be the name of the month
      full or abbreviated. If the value is a <code class="constant">number</code>, that
      number must be 1-12 (January-December). see table below

      <div class="table">
        <a name="monthtable" id="monthtable"></a>

        <p class="title"><b>Table&nbsp;1.&nbsp;</b></p>

        <div class="table-contents">
          <table border="1">
            <colgroup>
              <col />
              <col />
              <col />
            </colgroup>

            <thead>
              <tr>
                <th>Index</th>

                <th>Abbreviation</th>

                <th>Full Name</th>
              </tr>
            </thead>

            <tbody>
              <tr>
                <td>1</td>

                <td>Jan</td>

                <td>January</td>
              </tr>

              <tr>
                <td>2</td>

                <td>Feb</td>

                <td>February</td>
              </tr>

              <tr>
                <td>3</td>

                <td>Mar</td>

                <td>March</td>
              </tr>

              <tr>
                <td>4</td>

                <td>Apr</td>

                <td>April</td>
              </tr>

              <tr>
                <td>5</td>

                <td>May</td>

                <td>May</td>
              </tr>

              <tr>
                <td>6</td>

                <td>Jun</td>

                <td>June</td>
              </tr>

              <tr>
                <td>7</td>

                <td>Jul</td>

                <td>July</td>
              </tr>

              <tr>
                <td>8</td>

                <td>Aug</td>

                <td>August</td>
              </tr>

              <tr>
                <td>9</td>

                <td>Sep</td>

                <td>September</td>
              </tr>

              <tr>
                <td>10</td>

                <td>Oct</td>

                <td>October</td>
              </tr>

              <tr>
                <td>11</td>

                <td>Nov</td>

                <td>November</td>
              </tr>

              <tr>
                <td>12</td>

                <td>Dec</td>

                <td>December</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div><br class="table-break" />

      <p>If the value does not represent month, that is equivalent to passing a nil
      value.</p>
    </div>

    <div class="section" lang="en" xml:lang="en">
      <div class="titlepage">
        <div>
          <div>
            <h2 class="title" style="clear: both"><a name="date" id=
            "date"></a>6.&nbsp;date</h2>
          </div>
        </div>
      </div>The date module.

      <div class="section" lang="en" xml:lang="en">
        <div class="titlepage">
          <div>
            <div>
              <h3 class="title"><a name="date-id96473" id=
              "date-id96473"></a>6.1.&nbsp;Function(s) of date</h3>
            </div>
          </div>
        </div>

        <div class="variablelist">
          <dl>
            <dd><a href="#date.diff">diff</a> | <a href="#date.epoch">epoch</a> |
            <a href="#date.isleapyear">isleapyear</a> <sub>3</sub></dd>
          </dl>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="date.diff" id=
                "date.diff"></a>6.1.1.&nbsp;diff</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id352312" id="id352312"></a>Subtract the date
          and time value of two <a href="#dateObject">dateObject</a> and returns the
          resulting <a href="#dateObject">dateObject</a>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
date.<span class="bold"><strong>diff</strong></span>(<em class=
"parameter"><code>var_date1</code></em>, <em class=
"parameter"><code>var_date2</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>var_date1</em></span></span></dt>

                    <dd>Required. a <a href="#dateObject">dateObject</a> or <a href=
                    "#ParsableDateValue">parsable date value</a></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>var_date2</em></span></span></dt>

                    <dd>Required. a <a href="#dateObject">dateObject</a> or <a href=
                    "#ParsableDateValue">parsable date value</a></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>The resulting <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
-- get the days between two dates
d = date.diff("Jan 7 1563", date(1563, 1, 2))
assert(d:spandays()==5)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="date.epoch" id=
                "date.epoch"></a>6.1.2.&nbsp;epoch</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id352466" id="id352466"></a>Returns <a href=
          "#dateObject">dateObject</a> whose date and time value is the Operating System
          epoch.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
date.<span class="bold"><strong>epoch</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>The resulting <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
assert(date.epoch()==date("jan 1 1970"))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="date.getcenturyflip" id=
                "date.getcenturyflip"></a>6.1.3.&nbsp;getcenturyflip</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id352557" id="id352557"></a>Returns the current
          global setting for centuryflip.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
local centuryflip = date.<span class="bold"><strong>getcenturyflip</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>none</em></span></span></dt>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>The currrent global centuryflip value.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>centuryflip is a global setting and hence should only be set
              by an application, never by a library.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
local centuryflip = date.getcenturyflip()
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="date.isleapyear" id=
                "date.isleapyear"></a>6.1.4.&nbsp;isleapyear</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id352556" id="id352556"></a>Check if a number
          or <a href="#dateObject">dateObject</a> is a leapyear.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
date.<span class="bold"><strong>isleapyear</strong></span>(<em class=
"parameter"><code>var_year</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>var_year</em></span></span></dt>

                    <dd>a number or <a href="#dateObject">dateObject</a> or <a href=
                    "#ParsableDateValue">parsable date value</a></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd><code class="classname">true</code> if <code class=
              "varname">var_year</code> leap year. <code class="classname">false</code>
              if <code class="varname">var_year</code> not leap year.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>A leap year in the Gregorian calendar is defined as a year that is
              evenly divisible by four, except if it is divisible by 100; however, years
              that are divisible by 400 are leap years.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1776, 1, 1)
assert(date.isleapyear(d))
assert(date.isleapyear(d:getyear()))
assert(date.isleapyear(1776))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="date.setcenturyflip" id=
                "date.setcenturyflip"></a>6.1.5.&nbsp;setcenturyflip</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id352555" id="id352555"></a>Sets the global
          value for centuryflip. Century flip determines how 2-digit years are
          interpreted when parsing string values. Any value smaller than centuryflip
          will be considered 20xx, and values greater or equal will become 19xx.

          <div>The default value is 0, so all 2 digit years are considered 19xx.</div>
          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
date.<span class="bold"><strong>setcenturyflip</strong></span>(<em class=
"parameter"><code>century_flip</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>century_flip</em></span></span></dt>

                    <dd>a number from 0 to 100</a></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>Nothing.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>centuryflip is a global setting and hence should only be set
              by an application, never by a library.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
date.setcenturyflip(0)
assert(date("01-01-00")==date(1900,01,01))
assert(date("01-01-50")==date(1950,01,01))
assert(date("01-01-99")==date(1999,01,01))
date.setcenturyflip(100)
assert(date("01-01-00")==date(2000,01,01))
assert(date("01-01-50")==date(2050,01,01))
assert(date("01-01-99")==date(2099,01,01))
date.setcenturyflip(50)
assert(date("01-01-00")==date(2000,01,01))
assert(date("01-01-49")==date(2049,01,01))
assert(date("01-01-50")==date(1950,01,01))
assert(date("01-01-99")==date(1999,01,01))
</pre>
              </dd>
            </dl>
          </div>
        </div>

      </div>

      <div class="section" lang="en" xml:lang="en">
        <div class="titlepage">
          <div>
            <div>
              <h3 class="title"><a name="date-id95781" id=
              "date-id95781"></a>6.2.&nbsp;Method(s) of date</h3>
            </div>
          </div>
        </div>

        <div class="variablelist">
          <dl>
            <dd><a href="#date.__call">__call</a> <sub>1</sub></dd>
          </dl>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="date.__call" id=
                "date.__call"></a>6.2.1.&nbsp;__call</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id352700" id="id352700"></a> Construct a
          <a href="#dateObject">dateObject</a>. It has 3 method of constructing a date
          object.

          <div class="itemizedlist">
            <ul type="disc">
              <li>3 or more arguments - <em class="parameter"><code>int_year, var_month,
              int_day, num_hour, num_min, num_sec, int_ticks</code></em></li>

              <li>1 argument - <em class="parameter"><code>num_time</code></em> or
              <em class="parameter"><code>tbl_date</code></em> or <em class=
              "parameter"><code>str_date</code></em> or <em class=
              "parameter"><code>bool_now</code></em></li>

              <li>no argument - same as <code class="varname">date(<code class=
              "classname">false</code>)</code></li>
            </ul>
          </div>This is a metamethod of <a href="#date">date</a>. Remember <code class=
          "function">date:__call(...)</code> is the same as <code class=
          "function">date(...)</code>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
date(<em class="parameter"><code>num_time</code></em>)
</pre>
                <pre class="programlisting">
date(<em class="parameter"><code>tbl_date</code></em>)
</pre>
                <pre class="programlisting">
date(<em class="parameter"><code>str_date</code></em>)
</pre>
                <pre class="programlisting">
date(<em class="parameter"><code>bool_now</code></em>)
</pre>
                <pre class="programlisting">
date(<em class="parameter"><code>int_year</code></em>, <em class=
"parameter"><code>var_month</code></em>, <em class=
"parameter"><code>int_day</code></em>, [<em class=
"parameter"><code>num_hour</code></em>], [<em class=
"parameter"><code>num_min</code></em>], [<em class=
"parameter"><code>num_sec</code></em>], [<em class=
"parameter"><code>int_ticks</code></em>])
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist"></div>

                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>num_time</em></span></span></dt>

                    <dd>Required <code class="classname">number</code> value. Represents
                    the number of seconds in Universal Coordinated Time between the
                    specified value and the System epoch.</dd>
                  </dl>
                </div>

                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>tbl_date</em></span></span></dt>

                    <dd>
                      Required <code class="classname">table</code> value. The
                      constructor will look for the value of this key:

                      <div class="itemizedlist">
                        <ul type="disc">
                          <li><em class="parameter"><code>year</code></em> - an integer,
                          the full year, for example, 1969. Required if month and day is
                          given</li>

                          <li><em class="parameter"><code>month</code></em> - a <a href=
                          "#ParsableMonthValue">parsable month value</a>. Required if
                          year and day is given</li>

                          <li><em class="parameter"><code>day</code></em> - an integer,
                          the day of month from 1 to 31. Required if year and month is
                          given</li>

                          <li><em class="parameter"><code>hour</code></em> - a number,
                          hours value, from 0 to 23, indicating the number of hours since
                          midnight. (default = 0)</li>

                          <li><em class="parameter"><code>min</code></em> - a number,
                          minutes value, from 0 to 59. (default = 0)</li>

                          <li><em class="parameter"><code>sec</code></em> - a number,
                          seconds value, from 0 to 59. (default = 0)</li>
                        </ul>
                      </div>Time <em class="parameter"><code>(hour or min or sec or
                      msec)</code></em> must be supplied if date <em class=
                      "parameter"><code>(year and month and day)</code></em> is not
                      given, vice versa.
                    </dd>
                  </dl>
                </div>

                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>str_date</em></span></span></dt>

                    <dd>
                      Required <code class="classname">string</code> value. It must have
                      number/words representing date and/or time. Use commas and spaces
                      as delimiters. Strings enclosed by parenthesis is treated as a
                      comment and is ignored, these parentheses may be nested. The stated
                      day of the week is ignored whether its correct or not. A string
                      containing an invalid date is an error. For example, a string
                      containing two years or two months is an error. Time must be
                      supplied if date is not given, vice versa.

                      <p><b>Time Format.&nbsp;</b> Hours, minutes, and seconds are
                      separated by colons, although all need not be specified. "10:",
                      "10:11", and "10:11:12" are all valid. If the 24-hour clock is
                      used, it is an error to specify "PM" for times later than 12 noon.
                      For example, "23:15 PM" is an error.</p>

                      <p><b>Time Zone Format.&nbsp;</b> First character is a sign "+"
                      (east of UTC) or "-" (west of UTC). Hours and minutes offset are
                      separated by colons:</p>
                      <pre class="programlisting">
assert( date("Jul 27 2006 03:56:28 +2:00") == date(2006,07,27,1,56,28))
</pre>

                      <p>Another format is <code class="constant">[sign][number]</code>
                      If <code class="constant">[number]</code> is less than 24, it is
                      the offset in hours e.g. "-10" = -10 hours. Otherwise it is the
                      offset in houndred hours e.g. "+75" = "+115" = +1.25 hours.</p>
                      <pre class="programlisting">
assert(date("Jul 27 2006 -75 ") == date(2006,07,27,1,15,0))
assert(date("Jul 27 2006 -115") == date(2006,07,27,1,15,0))
assert(date("Jul 27 2006 +10 ") == date(2006,07,26,14,0,0))
assert(date("Jul 27 2006 +2  ") == date(2006,07,26,22,0,0))
</pre>

                      <p>Standard timezone GMT, UTC, EST, EDT, CST, CDT, MST, MDT, PST,
                      PDT are supported.</p>
                      <pre class="programlisting">
assert(date("Jul 27 2006 GMT") == date(2006,07,27,0,0,0))
assert(date("Jul 27 2006 UTC") == date(2006,07,27,0,0,0))
assert(date("Jul 27 2006 EST") == date(2006,07,27,5,0,0))
assert(date("Jul 27 2006 EDT") == date(2006,07,27,4,0,0))
assert(date("Jul 27 2006 CST") == date(2006,07,27,6,0,0))
assert(date("Jul 27 2006 CDT") == date(2006,07,27,5,0,0))
assert(date("Jul 27 2006 MST") == date(2006,07,27,7,0,0))
assert(date("Jul 27 2006 MDT") == date(2006,07,27,6,0,0))
assert(date("Jul 27 2006 PST") == date(2006,07,27,8,0,0))
assert(date("Jul 27 2006 PDT") == date(2006,07,27,7,0,0))
</pre>

                      <p><b>Date Format.&nbsp;</b> Short dates can use either a "/" or
                      "-" date separator, but must follow the month/day/year format. 2
                      digit years are interpreted according to the global
                      <a href="#date.setcenturyflip">centuryflip setting</a>.</p>
                      <pre class="programlisting">
assert(date("02-03-04")==date(1904,02,03))
assert(date("12/25/98")==date(1998,12,25))
</pre>

                      <p>Long dates of the form "July 10 1995" can be given with the
                      year, month, and day in any order, and the year in 2-digit or
                      4-digit form. If you use the 2-digit form, the year must be greater
                      than or equal to 70.</p>
                      <pre class="programlisting">
assert(date("Feb-03-04")==date(1904,02,03))
assert(date("December 25 1998")==date(1998,12,25))
</pre>

                      <p>Follow the year with BC or BCE to indicate that the year is
                      before common era.</p>
                      <pre class="programlisting">
assert(date("Feb 3 0003 BC")==date(-2,02,03))
assert(date("December 25 0001 BC")==date(0,12,25))
</pre>

                      <p><b>Supported ISO 8601 Formats.&nbsp;</b></p>

                      <div class="variablelist">
                        <dl>
                          <dt><span class="term"><code class=
                          "constant">YYYY-MM-DD</code></span></dt>

                          <dd>
                            where YYYY is the year, MM is the month of the year, and DD
                            is the day of the month.
                            <pre class="programlisting">
assert(date("2000-12-31")==date(2000,12,31))
assert(date(" 20001231 ")==date(2000,12,31)) -- Compact version
</pre>
                          </dd>

                          <dt><span class="term"><code class=
                          "constant">YYYY-DDD</code></span></dt>

                          <dd>
                            where YYYY is the year, DDD is the day of the year.
                            <pre class="programlisting">
assert(date("1995-035")==date(1995,02,04))
assert(date("1995035 ")==date(1995,02,04)) -- Compact version
</pre>
                          </dd>

                          <dt><span class="term"><code class=
                          "constant">YYYY-WDD-D</code></span></dt>

                          <dd>
                            where YYYY is the year, DD is the week of the year, D is the
                            day of the week.
                            <pre class="programlisting">
assert(date("1997-W01-1")==date(1996,12,30))
assert(date("  1997W017")==date(1997,01,05)) -- Compact version
</pre>
                          </dd>

                          <dt><span class="term"><code class="constant"><span class=
                          "emphasis"><em>DATE</em></span> HH:MM:SS.SSS</code></span></dt>

                          <dd>
                            Where <span class="emphasis"><em>DATE</em></span> is the date
                            format discuss above, HH is the hour, MM is the miute, SS.SSS
                            is the seconds (fraction is optional).
                            <pre class="programlisting">
assert(date("1995-02-04 24:00:51.536")==date(1995,2,5,0,0,51.536))
assert(date("1976-W01-1 12:12:12.123")==date(1975,12,29,12,12,12.123))
assert(date("1995-035 23:59:59.99999")==date(1995,02,04,23,59,59.99999))
-- Compact version separated by latin capital letter T
assert(date("  19950205T000051.536  ")==date(1995,2,5,0,0,51.536))
assert(date("  1976W011T121212.123  ")==date(1975,12,29,12,12,12.123))
assert(date(" 1995035T235959.99999  ")==date(1995,02,04,23,59,59.99999))
</pre>
                          </dd>

                          <dt><span class="term"><code class="constant"><span class=
                          "emphasis"><em>DATE</em></span> <span class=
                          "emphasis"><em>TIME</em></span> +HH:MM</code>, <code class=
                          "constant"><span class="emphasis"><em>DATE</em></span>
                          <span class="emphasis"><em>TIME</em></span> -HHMM</code>,
                          <code class="constant"><span class=
                          "emphasis"><em>DATE</em></span> <span class=
                          "emphasis"><em>TIME</em></span> Z</code>,</span></dt>

                          <dd>
                            Where <span class="emphasis"><em>DATE</em></span> and
                            <span class="emphasis"><em>TIME</em></span> is the dateand
                            time format discuss above. First character is a sign "+"
                            (east of UTC) or "-" (west of UTC). HH and MM is Hours and
                            minutes offset. The Z stands for the zero offset.
                            <pre class="programlisting">
assert(date("1976-W01-1 12:00Z     ")==date(1975,12,29,12))
assert(date("1976-W01-1 13:00+01:00")==date(1975,12,29,12))
assert(date("1976-W01-1 0700-0500  ")==date(1975,12,29,12))
</pre>
                          </dd>
                        </dl>
                      </div>
                    </dd>
                  </dl>
                </div>

                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>bool_now</em></span></span></dt>

                    <dd>Required <code class="classname">boolean</code> value. if
                    <code class="varname">bool_now</code> is <code class=
                    "classname">false</code> it returns the current local date and time.
                    if <code class="varname">bool_now</code> is <code class=
                    "classname">true</code> it returns the current UTC date and
                    time.</dd>
                  </dl>
                </div>

                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>int_year</em></span></span></dt>

                    <dd>Required <code class="classname">interger</code> value. The year
                    value.</dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>var_month</em></span></span></dt>

                    <dd>Required. A <a href="#ParsableMonthValue">parsable month
                    value</a>.</dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>int_day</em></span></span></dt>

                    <dd>Required <code class="classname">interger</code> value. The day
                    of month.</dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>num_hour</em></span></span></dt>

                    <dd>Optional <code class="classname">number</code> value. Equal to
                    the hours value. The default value is <code class=
                    "literal">0</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>num_min</em></span></span></dt>

                    <dd>Optional <code class="classname">number</code> value. Equal to
                    the minutes value. The default value is <code class=
                    "literal">0</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>num_sec</em></span></span></dt>

                    <dd>Optional <code class="classname">number</code> value. Equal to
                    the seconds value. The default value is <code class=
                    "literal">0</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>int_ticks</em></span></span></dt>

                    <dd>Optional <code class="classname">interger</code> value. Equal to
                    the ticks value. The default value is <code class=
                    "literal">0</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>the new <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2006, 8, 13)   assert(a == date("Sun Aug 13 2006"))
b = date("Jun 13 1999") assert(b == date(1999, 6, 13))
c = date(1234483200)    assert(c == date("Feb 13 2009"))
d = date({year=2009, month=11, day=13, min=6})
        assert(d == date("Nov 13 2009 00:06:00"))
e = date() assert(e)
</pre>
              </dd>
            </dl>
          </div>
        </div>
      </div>
    </div>

    <div class="section" lang="en" xml:lang="en">
      <div class="titlepage">
        <div>
          <div>
            <h2 class="title" style="clear: both"><a name="dateObject" id=
            "dateObject"></a>7.&nbsp;dateObject</h2>
          </div>
        </div>
      </div><em class="firstterm">dateObject</em> is a table containing date and time
      value. It has a metatable for manipulation and retrieval of dates and times. Use
      the <a href="#date.__call">__call</a> method of <a href="#date">date</a> to
      construct a dateObject.

      <div class="section" lang="en" xml:lang="en">
        <div class="titlepage">
          <div>
            <div>
              <h3 class="title"><a name="DaysAndTick" id="DaysAndTick"></a>7.1.&nbsp;How
              Date and Time are stored in <code class="classname">dateObject</code></h3>
            </div>
          </div>
        </div>Time is stored in <code class="classname">dateObject</code> as Ticks or Day
        Fraction. Date is stored in <code class="classname">dateObject</code> as Day
        Number. Ticks is time unit per seconds. For example, if the tick unit is 1000000.
        0.25 seconds is equivalent to 250000 ticks (0.25*1000000). Day number, is the
        number days since the epoch, which is January 1, 0001 AD. Example.
        <pre class="programlisting">
dobj = date("15:49:59.3669")
</pre>If the tick unit is 1000000, <code class="varname">dobj</code> store this time as
56999366900 ticks and 0 days.
        <pre class="programlisting">
((((15*60)+49)*60)+59.3669)*1000000 == 56999366900
</pre>Example Date and Time:
        <pre class="programlisting">
dobj = date("Jan-5-0001 10:30:15")
</pre>If the tick unit is 1000000, <code class="varname">dobj</code> store this date and
time as 37815000000 ticks and 4 days. 4 days becuase:

        <table id="id354830">
          <tr>
            <th>Day#</th>

            <th>Date</th>
          </tr>

          <tr>
            <td>0</td>

            <td>Jan 1 0001</td>
          </tr>

          <tr>
            <td>1</td>

            <td>Jan 2 0001</td>
          </tr>

          <tr>
            <td>2</td>

            <td>Jan 3 0001</td>
          </tr>

          <tr>
            <td>3</td>

            <td>Jan 4 0001</td>
          </tr>

          <tr>
            <td><span class="bold"><strong>4</strong></span></td>

            <td><span class="bold"><strong>Jan 5 0001</strong></span></td>
          </tr>

          <tr>
            <td>5</td>

            <td>Jan 6 0001</td>
          </tr>

          <tr>
            <td>...</td>

            <td>...</td>
          </tr>
        </table>

        <p>The default tick unit is 1000000 (micro-second-ticks)</p>
      </div>

      <div class="section" lang="en" xml:lang="en">
        <div class="titlepage">
          <div>
            <div>
              <h3 class="title"><a name="SupportedMetaMethods" id=
              "SupportedMetaMethods"></a>7.2.&nbsp;Supported MetaMethods</h3>
            </div>
          </div>
        </div>

        <div class="variablelist">
          <dl>
            <dt><span class="term">The <code class="varname">a &lt; b</code>
            operation.</span></dt>

            <dd>Returns <code class="constant">true</code> if date value of a is smaller/older
            than date value of b. <code class="varname">a &gt; b</code> is equivalent to
            <code class="varname">b &lt; a</code>.</dd>

            <dt><span class="term">The <code class="varname">a &lt;= b</code>
            operation.</span></dt>

            <dd>Returns <code class="constant">true</code> if date value of a is smaller/older
            than or equal to the date value of b. <code class="varname">a &gt;= b</code>
            is equivalent to <code class="varname">b &lt;= a</code>.</dd>

            <dt><span class="term">The <code class="varname">a == b</code>
            operation.</span></dt>

            <dd>Returns <code class="constant">true</code> if date value of a is equal
            equal to the date value of b. <code class="varname">a ~= b</code> is
            equivalent to <code class="varname">not (a == b)</code>.</dd>

            <dt><span class="term">The <code class="varname">a .. b</code>
            operation.</span></dt>

            <dd>Equivalent to <code class="varname">tostring(a) ..
            tostring(b)</code>.</dd>

            <dt><span class="term">The <code class="varname">a - b</code>
            operation.</span></dt>

            <dd>Subtract the date and time value of <code class="varname">b</code> from
            date and time value of <code class="varname">a</code>.</dd>

            <dt><span class="term">The <code class="varname">a + b</code>
            operation.</span></dt>

            <dd>Add the date and time value of <code class="varname">b</code> to date and
            time value of <code class="varname">a</code>.</dd>
          </dl>
        </div><code class="varname">a</code> and <code class="varname">b</code> must be a
        parsable date value or an error rises
        <pre class="programlisting">
a = date(1521,5,2)
b = a:copy():addseconds(0.001)

assert((a - b):spanseconds() == -0.001)
assert((a + b) == (b + a))
assert(a == (b - date("00:00:00.001")) )
assert(b == (a + date("00:00:00.001")) )

b:addseconds(-0.01)

assert(a &gt;  b and b &lt;  a)
assert(a &gt;= b and b &lt;= a)
assert(a ~= b and (not(a == b)))

a = b:copy()

assert(not (a &gt;  b and b &lt;  a))
assert(a &gt;= b and b &lt;= a)
assert(a == b and (not(a ~= b)))

assert((a .. 565369) == (b .. 565369))
assert((a .. "????") == (b .. "????"))

</pre>
      </div>

      <div class="section" lang="en" xml:lang="en">
        <div class="titlepage">
          <div>
            <div>
              <h3 class="title"><a name="dateObject-id94476" id=
              "dateObject-id94476"></a>7.3.&nbsp;Method(s) of dateObject</h3>
            </div>
          </div>
        </div>

        <div class="variablelist">
          <dl>
            <dd><a href="#dateObject.adddays">adddays</a> | <a href=
            "#dateObject.addhours">addhours</a> | <a href=
            "#dateObject.addminutes">addminutes</a> | <a href=
            "#dateObject.addmonths">addmonths</a> | <a href=
            "#dateObject.addseconds">addseconds</a> | <a href=
            "#dateObject.addticks">addticks</a> | <a href=
            "#dateObject.addyears">addyears</a> | <a href="#dateObject.copy">copy</a> |
            <a href="#dateObject.fmt">fmt</a> | <a href="#dateObject.getbias">getbias</a>
            | <a href="#dateObject.getclockhour">getclockhour</a> | <a href=
            "#dateObject.getdate">getdate</a> | <a href="#dateObject.getday">getday</a> |
            <a href="#dateObject.getfracsec">getfracsec</a> | <a href=
            "#dateObject.gethours">gethours</a> | <a href=
            "#dateObject.getisoweekday">getisoweekday</a> | <a href=
            "#dateObject.getisoweeknumber">getisoweeknumber</a> | <a href=
            "#dateObject.getisoyear">getisoyear</a> | <a href=
            "#dateObject.getminutes">getminutes</a> | <a href=
            "#dateObject.getmonth">getmonth</a> | <a href=
            "#dateObject.getseconds">getseconds</a> | <a href=
            "#dateObject.getticks">getticks</a> | <a href=
            "#dateObject.gettime">gettime</a> | <a href=
            "#dateObject.getweekday">getweekday</a> | <a href=
            "#dateObject.getweeknumber">getweeknumber</a> | <a href=
            "#dateObject.getyear">getyear</a> | <a href=
            "#dateObject.getyearday">getyearday</a> | <a href=
            "#dateObject.setday">setday</a> | <a href="#dateObject.sethours">sethours</a>
            | <a href="#dateObject.setisoweekday">setisoweekday</a> | <a href=
            "#dateObject.setisoweeknumber">setisoweeknumber</a> | <a href=
            "#dateObject.setisoyear">setisoyear</a> | <a href=
            "#dateObject.setminutes">setminutes</a> | <a href=
            "#dateObject.setmonth">setmonth</a> | <a href=
            "#dateObject.setseconds">setseconds</a> | <a href=
            "#dateObject.setticks">setticks</a> | <a href=
            "#dateObject.setyear">setyear</a> | <a href=
            "#dateObject.spandays">spandays</a> | <a href=
            "#dateObject.spanhours">spanhours</a> | <a href=
            "#dateObject.spanminutes">spanminutes</a> | <a href=
            "#dateObject.spanseconds">spanseconds</a> | <a href=
            "#dateObject.spanticks">spanticks</a> | <a href=
            "#dateObject.tolocal">tolocal</a> | <a href="#dateObject.toutc">toutc</a>
            <sub>44</sub></dd>
          </dl>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.adddays" id=
                "dateObject.adddays"></a>7.3.1.&nbsp;adddays</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id355399" id="id355399"></a>Add days in
          <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>adddays</strong></span>(<em class=
"parameter"><code>int_days</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>int_days</em></span></span></dt>

                    <dd>Required <code class="classname">integer</code> value. Days to
                    add.</dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the adjusted <a href=
                    "#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>If the value is negative, the adjusted dateObject will be earlier.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2000,12,30)
b = date(a):adddays(3)
c = date.diff(b,a)
assert(c:spandays() == 3)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.addhours" id=
                "dateObject.addhours"></a>7.3.2.&nbsp;addhours</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id355527" id="id355527"></a>Add hours in
          <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>addhours</strong></span>(<em class=
"parameter"><code>num_hours</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>num_hours</em></span></span></dt>

                    <dd>Required <code class="classname">number</code> value. Hours to
                    add.</dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the adjusted <a href=
                    "#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>If the value is negative, the adjusted dateObject will be earlier.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2000,12,30)
b = date(a):addhours(3)
c = date.diff(b,a)
assert(c:spanhours() == 3)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.addminutes" id=
                "dateObject.addminutes"></a>7.3.3.&nbsp;addminutes</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id355655" id="id355655"></a>Add minutes in
          <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>addminutes</strong></span>(<em class=
"parameter"><code>num_minutes</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>num_minutes</em></span></span></dt>

                    <dd>Required <code class="classname">number</code> value. Minutes to
                    add.</dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the adjusted <a href=
                    "#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>If the value is negative, the adjusted dateObject will be earlier.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2000,12,30)
b = date(a):addminutes(3)
c = date.diff(b,a)
assert(c:spanminutes() == 3)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.addmonths" id=
                "dateObject.addmonths"></a>7.3.4.&nbsp;addmonths</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id355783" id="id355783"></a>Add months in
          <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>addmonths</strong></span>(<em class=
"parameter"><code>int_months</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>int_months</em></span></span></dt>

                    <dd>Required <code class="classname">integer</code> value. Months to
                    add.</dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the adjusted <a href=
                    "#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>If the value is negative, the adjusted dateObject will be earlier.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2000,12,28):addmonths(3)
assert(a:getmonth() == 3)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.addseconds" id=
                "dateObject.addseconds"></a>7.3.5.&nbsp;addseconds</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id355910" id="id355910"></a>Add seconds in
          <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>addseconds</strong></span>(<em class=
"parameter"><code>num_sec</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>num_sec</em></span></span></dt>

                    <dd>Required <code class="classname">number</code> value. Seconds to
                    add.</dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the adjusted <a href=
                    "#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>If the value is negative, the adjusted dateObject will be earlier.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2000,12,30)
b = date(a):addseconds(3)
c = date.diff(b,a)
assert(c:spanseconds() == 3)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.addticks" id=
                "dateObject.addticks"></a>7.3.6.&nbsp;addticks</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id356038" id="id356038"></a>Add ticks in
          <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>addticks</strong></span>(<em class=
"parameter"><code>num_ticks</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>num_ticks</em></span></span></dt>

                    <dd>Required <code class="classname">number</code> value. Ticks to
                    add.</dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the adjusted <a href=
                    "#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>If the value is negative, the adjusted dateObject will be earlier. For
              discussion about ticks see <a href="#DaysAndTick" title=
              "7.1.&nbsp;How Date and Time are stored in dateObject">Section&nbsp;7.1,
              &ldquo;How Date and Time are stored in <code class=
              "classname">dateObject</code>&rdquo;</a>.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2000,12,30)
b = date(a):addticks(3)
c = date.diff(b,a)
assert(c:spanticks() == 3)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.addyears" id=
                "dateObject.addyears"></a>7.3.7.&nbsp;addyears</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id356171" id="id356171"></a>Add years in
          <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>addyears</strong></span>(<em class=
"parameter"><code>int_years</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>int_years</em></span></span></dt>

                    <dd>Required <code class="classname">integer</code> value. Years to
                    add.</dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the adjusted <a href=
                    "#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>If the value is negative, the adjusted dateObject will be earlier.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2000,12,30):addyears(3)
assert(a:getyear() == (2000+3))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.copy" id=
                "dateObject.copy"></a>7.3.8.&nbsp;copy</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id356299" id="id356299"></a>Returns a new date
          object having the same date and time value of <a href=
          "#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>copy</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2000,12,30)
b = a:copy()
assert(a==b)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.fmt" id=
                "dateObject.fmt"></a>7.3.9.&nbsp;fmt</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id356352" id="id356352"></a>Returns a
          formatted version of <a href="#dateObject">dateObject</a>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>fmt</strong></span>(<em class=
"parameter"><code>str_code</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>str_code</em></span></span></dt>

                    <dd>
                      <code class="classname">string</code> value. The format string
                      follows the same rules as the strftime standard C function.

                      <div class="table">
                        <a name="fmtspec" id="fmtspec"></a>

                        <p class="title"><b>Table&nbsp;3.&nbsp;Format Spec</b></p>

                        <div class="table-contents">
                          <table summary="Format Spec" border="1">
                            <colgroup>
                              <col />
                              <col />
                            </colgroup>

                            <thead>
                              <tr>
                                <th>Spec</th>

                                <th>Description</th>
                              </tr>
                            </thead>

                            <tbody>
                              <tr>
                                <td>'%a'</td>

                                <td>Abbreviated weekday name (Sun)</td>
                              </tr>

                              <tr>
                                <td>'%A'</td>

                                <td>Full weekday name (Sunday)</td>
                              </tr>

                              <tr>
                                <td>'%b'</td>

                                <td>Abbreviated month name (Dec)</td>
                              </tr>

                              <tr>
                                <td>'%B'</td>

                                <td>Full month name (December)</td>
                              </tr>

                              <tr>
                                <td>'%C'</td>

                                <td>Year/100 (19, 20, 30)</td>
                              </tr>

                              <tr>
                                <td>'%d'</td>

                                <td>The day of the month as a number (range 1 - 31)</td>
                              </tr>

                              <tr>
                                <td>'%g'</td>

                                <td>year for ISO 8601 week, from 00 (79)</td>
                              </tr>

                              <tr>
                                <td>'%G'</td>

                                <td>year for ISO 8601 week, from 0000 (1979)</td>
                              </tr>

                              <tr>
                                <td>'%h'</td>

                                <td>same as %b</td>
                              </tr>

                              <tr>
                                <td>'%H'</td>

                                <td>hour of the 24-hour day, from 00 (06)</td>
                              </tr>

                              <tr>
                                <td>'%I'</td>

                                <td>The hour as a number using a 12-hour clock (01 -
                                12)</td>
                              </tr>

                              <tr>
                                <td>'%j'</td>

                                <td>The day of the year as a number (001 - 366)</td>
                              </tr>

                              <tr>
                                <td>'%m'</td>

                                <td>Month of the year, from 01 to 12</td>
                              </tr>

                              <tr>
                                <td>'%M'</td>

                                <td>Minutes after the hour 55</td>
                              </tr>

                              <tr>
                                <td>'%p'</td>

                                <td>AM/PM indicator (AM)</td>
                              </tr>

                              <tr>
                                <td>'%S'</td>

                                <td>The second as a number (59, 20 , 01)</td>
                              </tr>

                              <tr>
                                <td>'%u'</td>

                                <td>ISO 8601 day of the week, to 7 for Sunday (7, 1)</td>
                              </tr>

                              <tr>
                                <td>'%U'</td>

                                <td>Sunday week of the year, from 00 (48)</td>
                              </tr>

                              <tr>
                                <td>'%V'</td>

                                <td>ISO 8601 week of the year, from 01 (48)</td>
                              </tr>

                              <tr>
                                <td>'%w'</td>

                                <td>The day of the week as a decimal, Sunday being 0</td>
                              </tr>

                              <tr>
                                <td>'%W'</td>

                                <td>Monday week of the year, from 00 (48)</td>
                              </tr>

                              <tr>
                                <td>'%y'</td>

                                <td>The year as a number without a century (range 00 to
                                99)</td>
                              </tr>

                              <tr>
                                <td>'%Y'</td>

                                <td>Year with century (2000, 1914, 0325, 0001)</td>
                              </tr>

                              <tr>
                                <td>'%z'</td>

                                <td>Time zone offset, the date object is assumed local
                                time (+1000, -0230)</td>
                              </tr>

                              <tr>
                                <td>'%Z'</td>

                                <td>Time zone name, the date object is assumed local
                                time</td>
                              </tr>

                              <tr>
                                <td>'%\b'</td>

                                <td>Year, if year is in BCE, prints the BCE Year
                                representation, otherwise result is similar to "%Y" (1
                                BCE, 40 BCE) #</td>
                              </tr>

                              <tr>
                                <td>'%\f'</td>

                                <td>Seconds including fraction (59.998, 01.123) #</td>
                              </tr>

                              <tr>
                                <td>'%%'</td>

                                <td>percent character %</td>
                              </tr>

                              <tr>
                                <td>'%r'</td>

                                <td>12-hour time, from 01:00:00 AM (06:55:15 AM); same as
                                "%I:%M:%S %p"</td>
                              </tr>

                              <tr>
                                <td>'%R'</td>

                                <td>hour:minute, from 01:00 (06:55); same as "%I:%M"</td>
                              </tr>

                              <tr>
                                <td>'%T'</td>

                                <td>24-hour time, from 00:00:00 (06:55:15); same as
                                "%H:%M:%S"</td>
                              </tr>

                              <tr>
                                <td>'%D'</td>

                                <td>month/day/year from 01/01/00 (12/02/79); same as
                                "%m/%d/%y"</td>
                              </tr>

                              <tr>
                                <td>'%F'</td>

                                <td>year-month-day (1979-12-02); same as "%Y-%m-%d"</td>
                              </tr>

                              <tr>
                                <td>'%c'</td>

                                <td>The preferred date and time representation; same as
                                "%x %X"</td>
                              </tr>

                              <tr>
                                <td>'%x'</td>

                                <td>The preferred date representation, same as "%a %b %d
                                %\b"</td>
                              </tr>

                              <tr>
                                <td>'%X'</td>

                                <td>The preferred time representation, same as
                                "%H:%M:%\f"</td>
                              </tr>

                              <tr>
                                <td>'${iso}'</td>

                                <td>Iso format, same as "%Y-%m-%dT%T"</td>
                              </tr>

                              <tr>
                                <td>'${http}'</td>

                                <td>http format, same as "%a, %d %b %Y %T GMT"</td>
                              </tr>

                              <tr>
                                <td>'${ctime}'</td>

                                <td>ctime format, same as "%a %b %d %T GMT %Y"</td>
                              </tr>

                              <tr>
                                <td>'${rfc850}'</td>

                                <td>RFC850 format, same as "%A, %d-%b-%y %T GMT"</td>
                              </tr>

                              <tr>
                                <td>'${rfc1123}'</td>

                                <td>RFC1123 format, same as "%a, %d %b %Y %T GMT"</td>
                              </tr>

                              <tr>
                                <td>'${asctime}'</td>

                                <td>asctime format, same as "%a %b %d %T %Y"</td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div><br class="table-break" />
                    </dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>Only English names are supported</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1582,10,5)
assert(d:fmt('%D') == d:fmt("%m/%d/%y"))        -- month/day/year from 01/01/00 (12/02/79)
assert(d:fmt('%F') == d:fmt("%Y-%m-%d"))        -- year-month-day (1979-12-02)
assert(d:fmt('%h') == d:fmt("%b"))                      -- same as %b (Dec)
assert(d:fmt('%r') == d:fmt("%I:%M:%S %p"))     -- 12-hour time, from 01:00:00 AM (06:55:15 AM)
assert(d:fmt('%T') == d:fmt("%H:%M:%S"))        -- 24-hour time, from 00:00:00 (06:55:15)
assert(d:fmt('%a %A %b %B') == "Tue Tuesday Oct October")
assert(d:fmt('%C %d') == "15 05", d:fmt('%C %d'))

print(d:fmt[[
${iso} -- iso
${http} -- http
${ctime} -- ctime
${rfc850} -- rfc850
${rfc1123} -- rfc1123
${asctime} -- asctime
]])
</pre>
              </dd>

              <dt><span class="term"><span class="bold"><strong>Example</strong></span>
              (Prints the current date and time)</span></dt>

              <dd>
                <pre class="programlisting">
-- Prints the current date and time, including time zone
d = date(false);
print(d:fmt("Today is %c GMT%z"))
--&gt; "Today is Tue Oct 31 2000 01:58:14 GMT-0330"

-- Prints the current date and time in ISO format including time zone
d = date(false);
print(d:fmt("Today is ${iso}%z"))
--&gt; "Today is 2000-10-31T01:58:14-0330"

-- Prints the current date and time in ISO format, indicates UTC
d = date(true);
print(d:fmt("Today is ${iso}Z"))
--&gt; "Today is 2000-10-31T05:28:14Z"
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getbias" id=
                "dateObject.getbias"></a>7.3.10.&nbsp;getbias</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id356866" id="id356866"></a> Assuming <a href=
          "#dateObject">dateObject</a> is a local time. Returns the time zone offset.
          Returns nil on failure.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getbias</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2^16)
print(a:getbias())
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getclockhour" id=
                "dateObject.getclockhour"></a>7.3.11.&nbsp;getclockhour</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id356921" id="id356921"></a>Returns the hours
          value using a 12-hour clock in a <a href="#dateObject">dateObject</a>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getclockhour</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date("10:59:59 pm")
assert(a:getclockhour()==10)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getdate" id=
                "dateObject.getdate"></a>7.3.12.&nbsp;getdate</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id356976" id="id356976"></a>Returns the
          <em class="parameter"><code>year</code></em>, <em class=
          "parameter"><code>month</code></em>, and <em class=
          "parameter"><code>day</code></em> value in a <a href=
          "#dateObject">dateObject</a>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getdate</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(1970, 1, 1)
y, m, d = a:getdate()
assert(y == 1970 and m == 1 and d == 1)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getday" id=
                "dateObject.getday"></a>7.3.13.&nbsp;getday</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357044" id="id357044"></a>Returns the day of
          month value in a <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getday</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1966, 'sep', 6)
assert(d:getday() == 6)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getfracsec" id=
                "dateObject.getfracsec"></a>7.3.14.&nbsp;getfracsec</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357097" id="id357097"></a>Returns the
          seconds after the minute (fractional) value in a <a href=
          "#dateObject">dateObject</a>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getfracsec</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date("Wed Apr 04 2181 11:51:06.996 UTC")
assert(d:getfracsec() == 6.996)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.gethours" id=
                "dateObject.gethours"></a>7.3.15.&nbsp;gethours</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357152" id="id357152"></a>Returns the hours
          value in a <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>gethours</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date("Wed Apr 04 2181 11:51:06 UTC")
assert(d:gethours() == 11)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getisoweekday" id=
                "dateObject.getisoweekday"></a>7.3.16.&nbsp;getisoweekday</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357205" id="id357205"></a>Returns the day of
          week (sunday=7, monday=1, ...saturday=6) in a <a href=
          "#dateObject">dateObject</a>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getisoweekday</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1970, 1, 1)
assert(d:getisoweekday() == 4)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getisoweeknumber" id=
                "dateObject.getisoweeknumber"></a>7.3.17.&nbsp;getisoweeknumber</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357261" id="id357261"></a>Returns the ISO
          8601 week number (01 to 53) in a <a href="#dateObject">dateObject</a>. Using
          the Year-WeekOfYear-DayOfWeek date system

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getisoweeknumber</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1975, 12, 29)
assert(d:getisoweeknumber() == 1)
assert(d:getisoyear() == 1976)
assert(d:getisoweekday() == 1)
d = date(1977, 1, 2)
assert(d:getisoweeknumber() == 53)
assert(d:getisoyear() == 1976)
assert(d:getisoweekday() == 7)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getisoyear" id=
                "dateObject.getisoyear"></a>7.3.18.&nbsp;getisoyear</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357320" id="id357320"></a>Returns the ISO
          8601 year in a <a href="#dateObject">dateObject</a>. Using the
          Year-WeekOfYear-DayOfWeek date system

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getisoyear</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1996, 12, 30)
assert(d:getisoyear() == 1997)
d = date(1997, 01, 05)
assert(d:getisoyear() == 1997)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getminutes" id=
                "dateObject.getminutes"></a>7.3.19.&nbsp;getminutes</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357377" id="id357377"></a>Returns the
          minutes after the hour value in a <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getminutes</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date("Wed Apr 04 2181 11:51:06 UTC")
assert(d:getminutes() == 51)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getmonth" id=
                "dateObject.getmonth"></a>7.3.20.&nbsp;getmonth</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357430" id="id357430"></a>Returns the month
          value in a <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getmonth</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1966, 'sep', 6)
assert(d:getmonth() == 9)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getseconds" id=
                "dateObject.getseconds"></a>7.3.21.&nbsp;getseconds</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357483" id="id357483"></a>Returns the
          seconds after the minute value in a <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getseconds</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date("Wed Apr 04 2181 11:51:06.123 UTC")
assert(d:getseconds() == 6)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getticks" id=
                "dateObject.getticks"></a>7.3.22.&nbsp;getticks</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357537" id="id357537"></a>Returns the ticks
          after the seconds value in a <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getticks</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>For discussion about ticks see <a href="#DaysAndTick" title=
              "7.1.&nbsp;How Date and Time are stored in dateObject">Section&nbsp;7.1,
              &ldquo;How Date and Time are stored in <code class=
              "classname">dateObject</code>&rdquo;</a>.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date("Wed Apr 04 2181 11:51:06.123 UTC")
assert(d:getticks() == 123000)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.gettime" id=
                "dateObject.gettime"></a>7.3.23.&nbsp;gettime</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357607" id="id357607"></a>Returns the
          <em class="parameter"><code>hours</code></em>, <em class=
          "parameter"><code>minutes</code></em>, <em class=
          "parameter"><code>seconds</code></em> and <em class=
          "parameter"><code>ticks</code></em> value in a <a href=
          "#dateObject">dateObject</a>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>gettime</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date({hour=5,sec=.5,min=59})
h, m, s, t = a:gettime()
assert(t == 500000 and s == 0 and m == 59 and h == 5, tostring(a))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getweekday" id=
                "dateObject.getweekday"></a>7.3.24.&nbsp;getweekday</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357677" id="id357677"></a>Returns the day of
          week (sunday=1, monday=2, ...saturday=7) in a <a href=
          "#dateObject">dateObject</a>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getweekday</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1970, 1, 1)
assert(d:getweekday() == 5)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getweeknumber" id=
                "dateObject.getweeknumber"></a>7.3.25.&nbsp;getweeknumber</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357732" id="id357732"></a>Returns the week
          number value in a <a href="#dateObject">dateObject</a>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getweeknumber</strong></span>([<em class=
"parameter"><code>int_wdaybase</code></em>])
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>int_wdaybase</em></span></span></dt>

                    <dd>Optional <code class="classname">integer</code> value. The
                    starting day of week (1 for sunday, 2 for monday, ... 7 for
                    saturday). If omitted the starting day of week is sunday.</dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date("12/31/1972")
b,c = a:getweeknumber(), a:getweeknumber(2)
assert(b==53 and c==52)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getyear" id=
                "dateObject.getyear"></a>7.3.26.&nbsp;getyear</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357817" id="id357817"></a>Returns the year
          value in a <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getyear</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1965, 'jan', 0)
assert(d:getyear() == 1964)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.getyearday" id=
                "dateObject.getyearday"></a>7.3.27.&nbsp;getyearday</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357870" id="id357870"></a>Returns the day of
          year (1-366) in a <a href="#dateObject">dateObject</a>.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>getyearday</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(2181, 1, 12)
assert(d:getyearday() == 12)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.setday" id=
                "dateObject.setday"></a>7.3.28.&nbsp;setday</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id357925" id="id357925"></a>Sets the day of
          month value in <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>setday</strong></span>(<em class=
"parameter"><code>int_mday</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>int_mday</em></span></span></dt>

                    <dd><code class="classname">integer</code> value. A numeric value
                    equal to the day of month. The default value is <code class=
                    "literal">the current day of month</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1966, 'july', 6)
d:setday(1)
assert(d == date("1966 july 1"))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.sethours" id=
                "dateObject.sethours"></a>7.3.29.&nbsp;sethours</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id358043" id="id358043"></a>Sets the hour
          value in <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>sethours</strong></span>(<em class=
"parameter"><code>num_hour</code></em>, <em class=
"parameter"><code>num_min</code></em>, <em class=
"parameter"><code>num_sec</code></em>, <em class="parameter"><code>num_ticks</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>num_hour</em></span></span></dt>

                    <dd><code class="classname">number</code> value. The hours value. The
                    default value is <code class="literal">the current hours
                    value</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>num_min</em></span></span></dt>

                    <dd><code class="classname">number</code> value. The minutes after
                    the hours value. The default value is <code class="literal">the
                    current minutes value</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>num_sec</em></span></span></dt>

                    <dd><code class="classname">number</code> value. The seconds after
                    the minute value. The default value is <code class="literal">the
                    current seconds value</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>num_ticks</em></span></span></dt>

                    <dd><code class="classname">number</code> value. The ticks after the
                    second value. The default value is <code class="literal">the current
                    ticks value</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1984, 12, 3, 4, 39, 54)
d:sethours(1, 1, 1)
assert(d == date("1984 DEc 3 1:1:1"))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.setisoweekday" id=
                "dateObject.setisoweekday"></a>7.3.30.&nbsp;setisoweekday</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id358218" id="id358218"></a>Sets the ISO 8601
          week number value in <a href="#dateObject">dateObject</a>. Using the
          Year-WeekOfYear-DayOfWeek date system

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>setisoweekday</strong></span>(<em class=
"parameter"><code>int_wday</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>int_wday</em></span></span></dt>

                    <dd><code class="classname">integer</code> value. The day the week.
                    The default value is <code class="literal">the current week
                    day</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date.isodate(1999, 52, 1)
d:setisoweekday(7)
assert(d == date(2000, 1, 02))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.setisoweeknumber" id=
                "dateObject.setisoweeknumber"></a>7.3.31.&nbsp;setisoweeknumber</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id358339" id="id358339"></a>Sets the ISO 8601
          week number value in <a href="#dateObject">dateObject</a>. Using the
          Year-WeekOfYear-DayOfWeek date system

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>setisoweeknumber</strong></span>(<em class=
"parameter"><code>int_week</code></em>, <em class="parameter"><code>int_wday</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>int_week</em></span></span></dt>

                    <dd><code class="classname">integer</code> value. The week value.
                    The default value is <code class="literal">the current
                    week</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>int_wday</em></span></span></dt>

                    <dd><code class="classname">integer</code> value. The day of the week.
                    The default value is <code class="literal">the current week
                    day</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1999, 12, 27)
d:setisoweeknumber(51, 7)
assert(d == date(1999, 12, 26))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.setisoyear" id=
                "dateObject.setisoyear"></a>7.3.32.&nbsp;setisoyear</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id358479" id="id358479"></a>Sets the ISO 8601
          year value in <a href="#dateObject">dateObject</a>. Using the
          Year-WeekOfYear-DayOfWeek date system

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>setisoyear</strong></span>(<em class=
"parameter"><code>int_year</code></em>, <em class=
"parameter"><code>int_week</code></em>, <em class="parameter"><code>int_wday</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>int_year</em></span></span></dt>

                    <dd><code class="classname">integer</code> value. The year value. The
                    default value is <code class="literal">the current year</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>int_week</em></span></span></dt>

                    <dd><code class="classname">integer</code> value. The week value.
                    The default value is <code class="literal">the current
                    week</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>int_wday</em></span></span></dt>

                    <dd><code class="classname">integer</code> value. The day of the week.
                    The default value is <code class="literal">the current week
                    day</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1999, 12, 27)
d:setisoyear(2000, 1)
assert(d == date.isodate(2000,1,1))
assert(d:getyear() == 2000)
assert(d:getday() == 3)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.setminutes" id=
                "dateObject.setminutes"></a>7.3.33.&nbsp;setminutes</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id358637" id="id358637"></a>Sets the minutes
          value in <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>setminutes</strong></span>(<em class=
"parameter"><code>num_min</code></em>, <em class=
"parameter"><code>num_sec</code></em>, <em class="parameter"><code>num_ticks</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>num_min</em></span></span></dt>

                    <dd><code class="classname">number</code> value. The minutes after
                    the value. The default value is <code class="literal">the current
                    minutes value</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>num_sec</em></span></span></dt>

                    <dd><code class="classname">number</code> value. The seconds after
                    the minute value. The default value is <code class="literal">the
                    current seconds value</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>num_ticks</em></span></span></dt>

                    <dd><code class="classname">number</code> value. The ticks after the
                    second value. The default value is <code class="literal">the current
                    ticks value</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1984, 12, 3, 4, 39, 54)
d:setminutes(59, 59, 500)
assert(d == date(1984, 12, 3, 4, 59, 59, 500))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.setmonth" id=
                "dateObject.setmonth"></a>7.3.34.&nbsp;setmonth</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id358794" id="id358794"></a>Sets the month
          value in <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>setmonth</strong></span>(<em class=
"parameter"><code>var_month</code></em>, <em class=
"parameter"><code>int_mday</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>var_month</em></span></span></dt>

                    <dd><a href="#ParsableMonthValue">parsable month value</a>. The
                    default value is <code class="literal">the current month</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>int_mday</em></span></span></dt>

                    <dd><code class="classname">integer</code> value. The day of month.
                    The default value is <code class="literal">the current day of
                    month</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1966, 'july', 6)
d:setmonth(1)
assert(d == date("6 jan 1966"))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.setseconds" id=
                "dateObject.setseconds"></a>7.3.35.&nbsp;setseconds</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id358931" id="id358931"></a>Sets the seconds
          after the minute value in <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>setseconds</strong></span>(<em class=
"parameter"><code>num_sec</code></em>, <em class="parameter"><code>num_ticks</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>num_sec</em></span></span></dt>

                    <dd><code class="classname">number</code> value. The seconds after
                    the minute value. The default value is <code class="literal">the
                    current seconds value</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>num_ticks</em></span></span></dt>

                    <dd><code class="classname">number</code> value. The ticks after the
                    second value. The default value is <code class="literal">the current
                    ticks value</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1984, 12, 3, 4, 39, 54)
d:setseconds(59, date.ticks())
assert(d == date(1984, 12, 3, 4, 40))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.setticks" id=
                "dateObject.setticks"></a>7.3.36.&nbsp;setticks</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id359069" id="id359069"></a>Sets the ticks
          after the second value in <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>setticks</strong></span>(<em class=
"parameter"><code>num_ticks</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>num_ticks</em></span></span></dt>

                    <dd><code class="classname">number</code> value. The ticks after the
                    second value. The default value is <code class="literal">the current
                    ticks value</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1984, 12, 3, 4, 39, 54)
d:setticks(444)
assert(d == date(1984, 12, 3, 4, 39, 54, 444))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.setyear" id=
                "dateObject.setyear"></a>7.3.37.&nbsp;setyear</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id359188" id="id359188"></a>Sets the year
          value in <a href="#dateObject">dateObject</a>

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>setyear</strong></span>(<em class=
"parameter"><code>int_year</code></em>, <em class=
"parameter"><code>var_month</code></em>, <em class=
"parameter"><code>int_mday</code></em>)
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Arguments</strong></span></span></dt>

              <dd>
                <div class="variablelist">
                  <dl>
                    <dt><span class="term"><span class=
                    "emphasis"><em>int_year</em></span></span></dt>

                    <dd><code class="classname">integer</code> value. The year value. The
                    default value is <code class="literal">the current year</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>var_month</em></span></span></dt>

                    <dd>The month value. The default value is <code class="literal">the
                    current month</code></dd>

                    <dt><span class="term"><span class=
                    "emphasis"><em>int_mday</em></span></span></dt>

                    <dd><code class="classname">integer</code> value. The day of month.
                    The default value is <code class="literal">the current day of
                    month</code></dd>
                  </dl>
                </div>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Returns</strong></span></span></dt>

              <dd>
                <table class="simplelist" border="0" summary="Simple list">
                  <tr>
                    <td><span class="emphasis"><em>Success</em></span></td>

                    <td>reference to the <a href="#dateObject">dateObject</a></td>
                  </tr>

                  <tr>
                    <td><span class="emphasis"><em>Failure</em></span></td>

                    <td>nil.</td>
                  </tr>
                </table>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
d = date(1966, 'july', 6)
d:setyear(2000)
assert(d == date("jul 6 2000"))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.spandays" id=
                "dateObject.spandays"></a>7.3.38.&nbsp;spandays</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id359339" id="id359339"></a>Returns how many
          days the <a href="#dateObject">dateObject</a> has

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>spandays</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2181, "aPr", 4, 6, 30, 30, 15000)
b = date(a):adddays(2)
c = date.diff(b, a)
assert(c:spandays() == (2))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.spanhours" id=
                "dateObject.spanhours"></a>7.3.39.&nbsp;spanhours</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id359393" id="id359393"></a>Returns how many
          hours the <a href="#dateObject">dateObject</a> has

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>spanhours</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2181, "aPr", 4, 6, 30, 30, 15000)
b = date(a):adddays(2)
c = date.diff(b, a)
assert(c:spanhours() == (2*24))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.spanminutes" id=
                "dateObject.spanminutes"></a>7.3.40.&nbsp;spanminutes</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id359446" id="id359446"></a>Returns how many
          minutes the <a href="#dateObject">dateObject</a> has

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>spanminutes</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2181, "aPr", 4, 6, 30, 30, 15000)
b = date(a):adddays(2)
c = date.diff(b, a)
assert(c:spanminutes() == (2*24*60))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.spanseconds" id=
                "dateObject.spanseconds"></a>7.3.41.&nbsp;spanseconds</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id359500" id="id359500"></a>Returns how many
          seconds the <a href="#dateObject">dateObject</a> has

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>spanseconds</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2181, "aPr", 4, 6, 30, 30, 15000)
b = date(a):adddays(2)
c = date.diff(b, a)
assert(c:spanseconds() == (2*24*60*60))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.spanticks" id=
                "dateObject.spanticks"></a>7.3.42.&nbsp;spanticks</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id359556" id="id359556"></a>Returns how many
          ticks the <a href="#dateObject">dateObject</a> has

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>spanticks</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Remarks</strong></span></span></dt>

              <dd>For discussion about ticks see <a href="#DaysAndTick" title=
              "7.1.&nbsp;How Date and Time are stored in dateObject">Section&nbsp;7.1,
              &ldquo;How Date and Time are stored in <code class=
              "classname">dateObject</code>&rdquo;</a>.</dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2181, "aPr", 4, 6, 30, 30, 15000)
b = date(a):adddays(2)
c = date.diff(b, a)
assert(c:spanticks() == (2*24*60*60*1000000))
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.tolocal" id=
                "dateObject.tolocal"></a>7.3.43.&nbsp;tolocal</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id359627" id="id359627"></a> Assuming <a href=
          "#dateObject">dateObject</a> is a utc time. Convert its date and time value to
          local time.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>tolocal</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2^16)
b = a:copy():tolocal();
print(a,b)
</pre>
              </dd>
            </dl>
          </div>
        </div>

        <div class="section" lang="en" xml:lang="en">
          <div class="titlepage">
            <div>
              <div>
                <h4 class="title"><a name="dateObject.toutc" id=
                "dateObject.toutc"></a>7.3.44.&nbsp;toutc</h4>
              </div>
            </div>
          </div><a class="indexterm" name="id359683" id="id359683"></a> Assuming <a href=
          "#dateObject">dateObject</a> is a local time. Convert its date and time value
          to utc time.

          <div class="variablelist">
            <dl>
              <dt><span class="term"><span class=
              "bold"><strong>Syntax</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
dateObject:<span class="bold"><strong>toutc</strong></span>()
</pre>
              </dd>

              <dt><span class="term"><span class=
              "bold"><strong>Example</strong></span></span></dt>

              <dd>
                <pre class="programlisting">
a = date(2^16)
b = a:copy():toutc();
print(a,b)
</pre>
              </dd>
            </dl>
          </div>
        </div>
      </div>
    </div>

    <div class="section" lang="en" xml:lang="en">
      <div class="titlepage">
        <div>
          <div>
            <h2 class="title" style="clear: both"><a name="history" id=
            "history"></a>8.&nbsp;History</h2>
          </div>
        </div>
      </div>

      <div class="variablelist">
        <dl>
          <dt><span class="term">v1 (2005)</span></dt>

          <dd>Binary module</dd>

          <dt><span class="term">v2 (2006)</span></dt>

          <dd>Lua module</dd>
        </dl>
      </div>
    </div>

    <div class="section" lang="en" xml:lang="en">
      <div class="titlepage">
        <div>
          <div>
            <h2 class="title" style="clear: both"><a name="ackno" id=
            "ackno"></a>9.&nbsp;Acknowledgement</h2>
          </div>
        </div>
      </div>

      <p><a href="http://alcor.concordia.ca/~gpkatch/gdate-method.html" target=
      "_top">http://alcor.concordia.ca/~gpkatch/gdate-method.html</a> - Date calculation
      algorithms is based on this site.</p>
    </div>
  </div>
</body>
</html>
```

## File: `rockspecs/date-2.1.3-1.rockspec`
```
package = "date"
version = "2.1.3-1"

description = {
   summary = "Date & Time module for Lua 5.x",
   detailed = [[
      Pure Lua Date & Time module for Lua 5.x featuring date and time string
      parsing, time addition & subtraction, time span calculation, support for
      ISO 8601 dates, local time support, strftime-like formatting.
   ]],
   license = "MIT",
   homepage = "https://github.com/Tieske/date",
}

dependencies = {
   "lua >= 5.0, < 5.5"
}

source = {
   url = "git://github.com/Tieske/date/",
   tag = "version_2.1.3",
}

build = {
   type = "builtin",
   modules = {
      date = "src/date.lua"
   },
   copy_directories = { "docs" },
}

```

## File: `rockspecs/date-2.2-2.rockspec`
```
local package_name = "date"
local package_version = "2.2"
local rockspec_revision = "2"
local github_account_name = "Tieske"
local github_repo_name = package_name
local git_checkout = package_version == "dev" and "master" or ("version_"..package_version)

package = package_name
version = package_version .. "-" .. rockspec_revision

source = {
  url = "git+https://github.com/"..github_account_name.."/"..github_repo_name..".git",
  branch = git_checkout
}

description = {
  summary = "Date & Time module for Lua 5.x",
  detailed = [[
    Pure Lua Date & Time module for Lua 5.x featuring date and time string
    parsing, time addition & subtraction, time span calculation, support for
    ISO 8601 dates, local time support, strftime-like formatting.
  ]],
  license = "MIT",
  homepage = "https://github.com/"..github_account_name.."/"..github_repo_name,
}

dependencies = {
  "lua >= 5.0, < 5.5"
}

build = {
  type = "builtin",
  modules = {
    date = "src/date.lua"
  },
  copy_directories = { "docs" },
}
```

## File: `rockspecs/date-2.2.1-1.rockspec`
```
local package_name = "date"
local package_version = "2.2.1"
local rockspec_revision = "1"
local github_account_name = "Tieske"
local github_repo_name = package_name
local git_checkout = package_version == "dev" and "master" or ("version_"..package_version)

package = package_name
version = package_version .. "-" .. rockspec_revision

source = {
  url = "git+https://github.com/"..github_account_name.."/"..github_repo_name..".git",
  branch = git_checkout
}

description = {
  summary = "Date & Time module for Lua 5.x",
  detailed = [[
    Pure Lua Date & Time module for Lua 5.x featuring date and time string
    parsing, time addition & subtraction, time span calculation, support for
    ISO 8601 dates, local time support, strftime-like formatting.
  ]],
  license = "MIT",
  homepage = "https://github.com/"..github_account_name.."/"..github_repo_name,
}

dependencies = {
  "lua >= 5.0, < 5.5"
}

build = {
  type = "builtin",
  modules = {
    date = "src/date.lua"
  },
  copy_directories = { "docs" },
}
```

## File: `rockspecs/date-2.2.1-2.rockspec`
```
local package_name = "date"
local package_version = "2.2.1"
local rockspec_revision = "2"
local github_account_name = "Tieske"
local github_repo_name = package_name
local git_checkout = package_version == "dev" and "master" or ("version_"..package_version)

package = package_name
version = package_version .. "-" .. rockspec_revision

source = {
  url = "git+https://github.com/"..github_account_name.."/"..github_repo_name..".git",
  branch = git_checkout
}

description = {
  summary = "Date & Time module for Lua 5.x",
  detailed = [[
    Pure Lua Date & Time module for Lua 5.x featuring date and time string
    parsing, time addition & subtraction, time span calculation, support for
    ISO 8601 dates, local time support, strftime-like formatting.
  ]],
  license = "MIT",
  homepage = "https://github.com/"..github_account_name.."/"..github_repo_name,
}

dependencies = {
  "lua >= 5.0, < 5.6"
}

build = {
  type = "builtin",
  modules = {
    date = "src/date.lua"
  },
  copy_directories = { "docs" },
}
```

## File: `samples/mkcalendar.lua`
```
--[[---------------------
This script makes an html calendar
Syntax: mkcalendar.lua year1 year2 year3 .. yearn > file
arg:
  year1 .. yearn - the year(s) of the calendar to generate
  file           - the name of the file to write the generated text calendar
--]]---------------------

local date = require"date"

local function makemonth(y,m)
	local t = {}
	local d = date(y,m,1)
	t.name = d:fmt("%B")
	t.year = y
	-- get back to the nearest sunday
	d:adddays(-(d:getweekday()-1))
	repeat
		local tt = {}
		table.insert(t,tt)
		repeat -- insert the week days
			table.insert(tt, d:getday())
		until d:adddays(1):getweekday() == 1
	until d:getmonth() ~= m
	return t
end

local htm_foot = '\n</html>'
local htm_head = [[
<style>
  th {background:black; color: silver; vertical-align: middle;}
  td {vertical-align: middle; text-align:center;}
  td.sun {color: red;}
  td.sat {color: blue;}
</style>
<html>
]]
local htm_yearhead = '\n<table align="left">'
local htm_monhead  = '\n<tr><th colspan = "7">%s, %s</th></tr><tr><td>sun</td><td>mon</td><td>tue</td><td>wed</td><td>thu</td><td>fri</td><td>sat</td></tr>'
local htm_monweek  = '\n<tr><td class="sun">%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td class="sat">%s</td></tr>'
local htm_yearfoot = '\n</table>'
local function makecalendar(y, iox)
	iox:write(htm_yearhead)
	for i = 1, 12 do
		local tm = makemonth(y, i)
		iox:write(string.format(htm_monhead, tm.name, tm.year))
		for k, v in ipairs(tm) do
			iox:write(string.format(htm_monweek, v[1], v[2], v[3], v[4], v[5], v[6], v[7]))
		end
	end
	iox:write(htm_yearfoot)

end

io.stdout:write(htm_head)

for k, v in ipairs(arg) do
  local y = tonumber(v)
  if y then makecalendar(y, io.stdout) end
end

io.stdout:write(htm_foot)


```

## File: `samples/mkisocal.lua`
```
--[[---------------------
This script makes an iso year-week-day calendar
Syntax: mkisocal.lua year1 year2 year3 .. yearn > file
arg:
  year1 .. yearn - the year(s) of the calendar to generate
  file           - the name of the file to write the generated text calendar
--]]---------------------

local date = require"date"

local htm_foot = [[</body></html>]]
local htm_head = [[<html><head><style>body{color:#000000;background-color:#FFFFFF;font-family:sans-serif;}th{background:#000000;color:#CCCCCC;vertical-align:middle;}td{vertical-align:top;text-align:center;font-weight:bold;}.s{color:#999999;font-size:60%;}</style></head><body>]]
local htm_yearhead = [[<table align="center" width="100%" border="1"><tr><th>Year</th><th>Week</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr>]]
local htm_yearfoot = [[</table>]]
local function makecalendar(year, iow)
	local d = date():setisoyear(year,1,1)
	iow(htm_yearhead)
	iow("<!--".. d .. "-->\n")
	while d:getisoyear() == year do
		iow(d:fmt("<tr><td>%G</td><td>%V<br/><small class='s'>%Y-%j</small></td>"))
		repeat	iow(d:fmt("<td>%u<br/><small class='s'>%b %d %Y</small></td>"))
		until	d:adddays(1):getisoweekday() == 1
		iow("</tr>\n")
	end
	iow(htm_yearfoot)

end


local out = io.write

out(htm_head)

for k, v in ipairs(arg) do
  local d = tonumber(v);
  if d then makecalendar(d, out) end
end

out(htm_foot)


```

## File: `spec/date_spec.lua`
```
local date = require("date")

describe("Testing the 'date' module", function()

  it("Tests date parsing", function()
    assert( date("Jul 27 2006 03:56:28 +2:00") == date(2006,07,27,1,56,28))
    assert(date("Jul 27 2006 -75 ") == date(2006,07,27,1,15,0))
    assert(date("Jul 27 2006 -115") == date(2006,07,27,1,15,0))
    assert(date("Jul 27 2006 +10 ") == date(2006,07,26,14,0,0))
    assert(date("Jul 27 2006 +2  ") == date(2006,07,26,22,0,0))

    -- Standard timezone GMT, UTC, EST, EDT, CST, CDT, MST, MDT, PST, PDT are supported.
    assert(date("Jul 27 2006 GMT") == date(2006,07,27,0,0,0))
    assert(date("Jul 27 2006 UTC") == date(2006,07,27,0,0,0))
    assert(date("Jul 27 2006 EST") == date(2006,07,27,5,0,0))
    assert(date("Jul 27 2006 EDT") == date(2006,07,27,4,0,0))
    assert(date("Jul 27 2006 CST") == date(2006,07,27,6,0,0))
    assert(date("Jul 27 2006 CDT") == date(2006,07,27,5,0,0))
    assert(date("Jul 27 2006 MST") == date(2006,07,27,7,0,0))
    assert(date("Jul 27 2006 MDT") == date(2006,07,27,6,0,0))
    assert(date("Jul 27 2006 PST") == date(2006,07,27,8,0,0))
    assert(date("Jul 27 2006 PDT") == date(2006,07,27,7,0,0))
    -- Date Format.  Short dates can use either a "/" or "-" date separator, but must
    -- follow the month/day/year format.
    assert(date("02-03-04")==date(1904,02,03))
    assert(date("12/25/98")==date(1998,12,25))
    -- Long dates of the form "July 10 1995" can be given with the year, month, and day
    -- in any order, and the year in 2-digit or 4-digit form. If you use the 2-digit
    -- form, the year must be greater than or equal to 70.
    assert(date("Feb-03-04")==date(1904,02,03))
    assert(date("December 25 1998")==date(1998,12,25))
    -- Follow the year with BC or BCE to indicate that the year is before common era.
    assert(date("Feb 3 0003 BC")==date(-2,02,03))
    assert(date("December 25 0001 BC")==date(0,12,25))

    -- Supported ISO 8601 Formats
    -- YYYY-MM-DD, where YYYY is the year, MM is the month of the year, and DD is the
    -- day of the month
    assert(date("2000-12-31")==date(2000,12,31))
    assert(date(" 20001231 ")==date(2000,12,31)) -- "basic format" (compact)
    -- YYYY-DDD, where YYYY is the year, DDD is the day of the year
    assert(date("1995-035")==date(1995,02,04))
    assert(date("1995035 ")==date(1995,02,04)) -- "basic format" (compact)
    -- YYYY-WDD-D, where YYYY is the year, DD is the week of the year, D is the day of
    -- the week
    assert(date("1997-W01-1")==date(1996,12,30))
    assert(date("  1997W017")==date(1997,01,05)) -- "basic format" (compact)
    -- DATE HH:MM:SS.SSS, where DATE is the date format discussed above, HH is the hour,
    -- MM is the minute, SS.SSS is the seconds (fraction is optional)
    -- These are not ISO 8601 conformant:  Space between date and time is no longer
    -- allowed (though is in RFC 3339).
    assert(date("1995-02-04 24:00:51.536")==date(1995,2,5,0,0,51.536))
    assert(date("1995-02-04 24:00:51,536")==date(1995,2,5,0,0,51.536))
    assert(date("1976-W01-1 12:12:12.123")==date(1975,12,29,12,12,12.123))
    assert(date("1995-035 23:59:59.99999")==date(1995,02,04,23,59,59.99999))
    -- "basic format" (compact), date and time separated by the Latin capital T
    assert(date("  19950205T000051.536  ")==date(1995,2,5,0,0,51.536))
    assert(date("  19950205T000051,536  ")==date(1995,2,5,0,0,51.536))
    assert(date("  1976W011T121212.123  ")==date(1975,12,29,12,12,12.123))
    assert(date(" 1995035T235959.99999  ")==date(1995,02,04,23,59,59.99999)) -- not ISO 8601 conformant day spec
    -- "extended format" (human readable), date and time separated by the Latin
    -- capital T
    assert(date("1995-02-05T00:00:51.536")==date(1995,2,5,0,0,51.536))
    assert(date("1995-02-05T00:00:51,536")==date(1995,2,5,0,0,51.536))
    assert(date("1976-W01-1T12:12:12.123")==date(1975,12,29,12,12,12.123))
    assert(date("1995-035T23:59:59.99999")==date(1995,02,04,23,59,59.99999)) -- not ISO 8601 conformant day spec
    -- DATE TIME +HH:MM, DATE TIME -HHMM, DATE TIME Z, where DATE and TIME is the date
    -- and time format discussed above
    -- First character is a sign "+" (east of UTC) or "-" (west of UTC). HH and MM are
    -- hours and minutes offset. The Z stands for the zero offset.
    assert(date("1976-W01-1 12:00Z     ")==date(1975,12,29,12))
    assert(date("1976-W01-1 13:00+01:00")==date(1975,12,29,12))
    assert(date("1976-W01-1 0700-0500  ")==date(1975,12,29,12))

    -- timezone offset with colon
    assert(date("2023-08-22T17:40:23.308574-05:00")==date(2023,08,22,22,40,23.308574000))
    -- timezone offset without colon
    assert(date("2023-08-22T17:40:23.308574-0500")==date(2023,08,22,22,40,23.308574000))
    -- timezone offset without minutes
    assert(date("2023-08-22T17:40:23.308574-05")==date(2023,08,22,22,40,23.308574000))
    -- timezone offset without colon with positive offset and non-zero minutes
    assert(date("2023-08-22T19:40:23.308574+08:45")==date(2023,08,22,10,55,23.308574000))
    -- timezone offset without colon with no decimal seconds
    assert(date("2023-08-22T19:40:23-09:30")==date(2023,08,23,5,10,23))

    local a = date(2006, 8, 13)   assert(a == date("Sun Aug 13 2006"))
    local b = date("Jun 13 1999") assert(b == date(1999, 6, 13))
    local c = date(1234483200)    assert(c == date("Feb 13 2009"))
    local d = date({year=2009, month=11, day=13, min=6})
    assert(d == date("Nov 13 2009 00:06:00"))
    local e = date()              assert(e)
  end)

  it("Tests century-flip", function()
    local old = date.getcenturyflip()
    finally(function()
      date.setcenturyflip(old)
    end)

    assert(old==0)
    assert(date("01-01-00")==date(1900,01,01))
    assert(date("01-01-50")==date(1950,01,01))
    assert(date("01-01-99")==date(1999,01,01))
    date.setcenturyflip(100)
    assert(date("01-01-00")==date(2000,01,01))
    assert(date("01-01-50")==date(2050,01,01))
    assert(date("01-01-99")==date(2099,01,01))
    date.setcenturyflip(50)
    assert(date("01-01-00")==date(2000,01,01))
    assert(date("01-01-49")==date(2049,01,01))
    assert(date("01-01-50")==date(1950,01,01))
    assert(date("01-01-99")==date(1999,01,01))
  end)

  it("Tests leap year", function()
    assert.is_true(date.isleapyear(2012))
    assert.is_true(date.isleapyear(2000))
    assert.is_false(date.isleapyear(2011))
    assert.is_false(date.isleapyear(1900))
  end)

  it("Tests date equality", function()
    local a = date("20131230 00:57:04")
    assert(a:getyear()    == 2013)
    assert(a:getmonth()   == 12)
    assert(a:getday()     == 30)
    assert(a:gethours()   == 0)
    assert(a:getminutes() == 57)
    assert(a:getseconds() == 04)
    local b = date("20131230 01:00:00")
    local c = date("20131230 00:57:04")  -- same as a
    assert(a < b)
    assert(a <= b)
    assert(not (a > b))  -- luacheck: ignore
    assert(not (a >= b)) -- luacheck: ignore
    assert(a == c)
    assert(a <= c)
    assert(a >= c)
  end)

  it("Tests metamethods", function()
    local a = date(1521,5,2)
    local b = a:copy():addseconds(0.001)

    assert((a - b):spanseconds() == -0.001)
    assert((a + b) == (b + a))
    assert(a == (b - date("00:00:00.001")) )
    assert(b == (a + date("00:00:00.001")) )

    b:addseconds(-0.01)

    assert(a >  b and b <  a)
    assert(a >= b and b <= a)
    assert(a ~= b and (not(a == b)))  -- luacheck: ignore

    a = b:copy()

    assert(not (a >  b and b <  a))
    assert(a >= b and b <= a)
    assert(a == b and (not(a ~= b)))  -- luacheck: ignore

    assert((a .. 565369) == (b .. 565369))
    assert((a .. "????") == (b .. "????"))
  end)

  it("Tests 'adddays()'", function()
    local a = date(2000,12,30)
    local b = date(a):adddays(3)
    local c = date.diff(b,a)
    assert(c:spandays() == 3)
  end)

  it("Tests 'addhours()'", function()
    local a = date(2000,12,30)
    local b = date(a):addhours(3)
    local c = date.diff(b,a)
    assert(c:spanhours() == 3)
  end)

  it("Tests 'addminutes()'", function()
    local a = date(2000,12,30)
    local b = date(a):addminutes(3)
    local c = date.diff(b,a)
    assert(c:spanminutes() == 3)
  end)

  it("Tests 'addseconds()'", function()
    local a = date(2000,12,30)
    local b = date(a):addseconds(3)
    local c = date.diff(b,a)
    assert(c:spanseconds() == 3)
  end)

  it("Tests 'addmonths()'", function()
    local a = date(2000,12,28):addmonths(3)
    assert(a:getmonth() == 3)
  end)

  it("Tests 'addticks()'", function()
    local a = date(2000,12,30)
    local b = date(a):addticks(3)
    local c = date.diff(b,a)
    assert(c:spanticks() == 3)
  end)

  it("Tests 'addyears()'", function()
    local a = date(2000,12,30):addyears(3)
    assert(a:getyear() == (2000+3))
  end)

  it("Tests 'copy()'", function()
    local a = date(2000,12,30)
    local b = a:copy()
    assert(a==b)
  end)

  it("Tests 'fmt()'", function()
    local d = date(1582,10,5)
    assert(d:fmt('%D') == d:fmt("%m/%d/%y"))        -- month/day/year from 01/01/00 (12/02/79)
    assert(d:fmt('%F') == d:fmt("%Y-%m-%d"))        -- year-month-day (1979-12-02)
    assert(d:fmt('%h') == d:fmt("%b"))                      -- same as %b (Dec)
    assert(d:fmt('%r') == d:fmt("%I:%M:%S %p"))     -- 12-hour time, from 01:00:00 AM (06:55:15 AM)
    assert(d:fmt('%T') == d:fmt("%H:%M:%S"))        -- 24-hour time, from 00:00:00 (06:55:15)
    assert(d:fmt('%a %A %b %B') == "Tue Tuesday Oct October")
    assert(d:fmt('%C %d') == "15 05", d:fmt('%C %d'))
    local d2 = date(1446747300.00008)
    assert.is.equals(d2:fmt('%\f'),"00.000080109")

  end)

  it("Tests 'getclockhour()'", function()
    local a = date("10:59:59 pm")
    assert(a:getclockhour()==10)
  end)

  it("Tests 'getdate()'", function()
    local a = date(1970, 1, 1)
    local y, m, d = a:getdate()
    assert(y == 1970 and m == 1 and d == 1)
  end)

  it("Tests 'getday()'", function()
    local d = date(1966, 'sep', 6)
    assert(d:getday() == 6)
  end)

  it("Tests 'getfracsec()'", function()
    local d = date("Wed Apr 04 2181 11:51:06.996 UTC")
    assert(d:getfracsec() == 6.996)
  end)

  it("Tests 'gethours()'", function()
    local d = date("Wed Apr 04 2181 11:51:06 UTC")
    assert(d:gethours() == 11)
  end)

  it("Tests 'getisoweekday()'", function()
    local d = date(1970, 1, 1)
    assert(d:getisoweekday() == 4)
  end)

  it("Tests 'getisoweeknumber()'", function()
    local d = date(1975, 12, 29)
    assert(d:getisoweeknumber() == 1)
    assert(d:getisoyear() == 1976)
    assert(d:getisoweekday() == 1)
    d = date(1977, 1, 2)
    assert(d:getisoweeknumber() == 53)
    assert(d:getisoyear() == 1976)
    assert(d:getisoweekday() == 7)
  end)

  it("Tests 'getisoyear()'", function()
    local d = date(1996, 12, 30)
    assert(d:getisoyear() == 1997)
    d = date(1997, 01, 05)
    assert(d:getisoyear() == 1997)
  end)

  it("Tests 'getminutes'", function()
    local d = date("Wed Apr 04 2181 11:51:06 UTC")
    assert(d:getminutes() == 51)
  end)

  it("Tests 'getmonth'", function()
    local d = date("Wed Apr 04 2181 11:51:06 UTC")
    assert(d:getmonth() == 4)
  end)

  it("Tests 'getseconds'", function()
    local d = date("Wed Apr 04 2181 11:51:06 UTC")
    assert(d:getseconds() == 6)
  end)

  it("Tests 'getticks()'", function()
    local d = date("Wed Apr 04 2181 11:51:06.123 UTC")
    assert(d:getticks() == 123000)
  end)

  it("Tests 'gettime()'", function()
    local a = date({hour=5,sec=.5,min=59})
    local h, m, s, t = a:gettime()
    assert(t == 500000 and s == 0 and m == 59 and h == 5, tostring(a))
  end)

  it("Tests 'getweekday()'", function()
    local d = date(1970, 1, 1)
    assert(d:getweekday() == 5)
  end)

  it("Tests 'getweeknumber()'", function()
    local a = date("12/31/1972")
    local b,c = a:getweeknumber(), a:getweeknumber(2)
    assert(b==53 and c==52)
  end)

  it("Tests 'getyear()'", function()
    local d = date(1965, 'jan', 0)
    assert(d:getyear() == 1964)
  end)

  it("Tests 'getyearday()'", function()
    local d = date(2181, 1, 12)
    assert(d:getyearday() == 12)
  end)

  it("Tests 'setday()'", function()
    local d = date(1966, 'july', 6)
    d:setday(1)
    assert(d == date("1966 july 1"))
  end)

  it("Tests 'sethours()'", function()
    local d = date(1984, 12, 3, 4, 39, 54)
    d:sethours(1, 1, 1)
    assert(d == date("1984 DEc 3 1:1:1"))
  end)

  it("Tests 'setisoweekday()'", function()
    local d = date.isodate(1999, 52, 1)
    d:setisoweekday(7)
    assert(d == date(2000, 1, 02))
  end)

  it("Tests 'setisoweeknumber()'", function()
    local d = date(1999, 12, 27)
    d:setisoweeknumber(51, 7)
    assert(d == date(1999, 12, 26))
  end)

  it("Tests 'setisoyear()'", function()
    local d = date(1999, 12, 27)
    d:setisoyear(2000, 1)
    assert(d == date.isodate(2000,1,1))
    assert(d:getyear() == 2000)
    assert(d:getday() == 3)
  end)

  it("Tests 'setminutes()'", function()
    local d = date(1984, 12, 3, 4, 39, 54)
    d:setminutes(59, 59, 500)
    assert(d == date(1984, 12, 3, 4, 59, 59, 500))
  end)

  it("Tests 'setmonth()'", function()
    local d = date(1966, 'july', 6)
    d:setmonth(1)
    assert(d == date("6 jan 1966"))
  end)

  it("Tests 'setseconds()'", function()
    local d = date(1984, 12, 3, 4, 39, 54)
    d:setseconds(59, date.ticks())
    assert(d == date(1984, 12, 3, 4, 40))
  end)

  it("Tests 'setticks()'", function()
    local d = date(1984, 12, 3, 4, 39, 54)
    d:setticks(444)
    assert(d == date(1984, 12, 3, 4, 39, 54, 444))
  end)

  it("Tests 'setyear()'", function()
    local d = date(1966, 'july', 6)
    d:setyear(2000)
    assert(d == date("jul 6 2000"))
  end)

  it("Tests 'spandays()'", function()
    local a = date(2181, "aPr", 4, 6, 30, 30, 15000)
    local b = date(a):adddays(2)
    local c = date.diff(b, a)
    assert(c:spandays() == (2))
  end)

  it("Tests 'spanhours()'", function()
    local a = date(2181, "aPr", 4, 6, 30, 30, 15000)
    local b = date(a):adddays(2)
    local c = date.diff(b, a)
    assert(c:spanhours() == (2*24))
  end)

  it("Tests 'spanminutes()'", function()
    local a = date(2181, "aPr", 4, 6, 30, 30, 15000)
    local b = date(a):adddays(2)
    local c = date.diff(b, a)
    assert(c:spanminutes() == (2*24*60))
  end)

  it("Tests 'spanseconds()'", function()
    local a = date(2181, "aPr", 4, 6, 30, 30, 15000)
    local b = date(a):adddays(2)
    local c = date.diff(b, a)
    assert(c:spanseconds() == (2*24*60*60))
  end)

  it("Tests 'spanticks()'", function()
    local a = date(2181, "aPr", 4, 6, 30, 30, 15000)
    local b = date(a):adddays(2)
    local c = date.diff(b, a)
    assert(c:spanticks() == (2*24*60*60*1000000))
  end)

end)
```

## File: `src/date.lua`
```
---------------------------------------------------------------------------------------
-- Module for date and time calculations
--
-- Version 2.2.1
-- Copyright (C) 2005-2006, by Jas Latrix (jastejada@yahoo.com)
-- Copyright (C) 2013-2021, by Thijs Schreijer
-- Licensed under MIT, http://opensource.org/licenses/MIT

--[[ CONSTANTS ]]--
  local HOURPERDAY  = 24
  local MINPERHOUR  = 60
  local MINPERDAY    = 1440  -- 24*60
  local SECPERMIN   = 60
  local SECPERHOUR  = 3600  -- 60*60
  local SECPERDAY   = 86400 -- 24*60*60
  local TICKSPERSEC = 1000000
  local TICKSPERDAY = 86400000000
  local TICKSPERHOUR = 3600000000
  local TICKSPERMIN = 60000000
  local DAYNUM_MAX =  365242500 -- Sat Jan 01 1000000 00:00:00
  local DAYNUM_MIN = -365242500 -- Mon Jan 01 1000000 BCE 00:00:00
  local DAYNUM_DEF =  0 -- Mon Jan 01 0001 00:00:00
  local _;
--[[ GLOBAL SETTINGS ]]--
  local centuryflip = 0 -- year >= centuryflip == 1900, < centuryflip == 2000
--[[ LOCAL ARE FASTER ]]--
  local type     = type
  local pairs    = pairs
  local error    = error
  local assert   = assert
  local tonumber = tonumber
  local tostring = tostring
  local string   = string
  local math     = math
  local os       = os
  local unpack   = unpack or table.unpack
  local setmetatable = setmetatable
  local getmetatable = getmetatable
--[[ EXTRA FUNCTIONS ]]--
  local fmt  = string.format
  local lwr  = string.lower
  local rep  = string.rep
  local len  = string.len  -- luacheck: ignore
  local sub  = string.sub
  local gsub = string.gsub
  local gmatch = string.gmatch or string.gfind
  local find = string.find
  local ostime = os.time
  local osdate = os.date
  local floor = math.floor
  local ceil  = math.ceil
  local abs   = math.abs
  -- removes the decimal part of a number
  local function fix(n) n = tonumber(n) return n and ((n > 0 and floor or ceil)(n)) end
  -- returns the modulo n % d;
  local function mod(n,d) return n - d*floor(n/d) end
  -- is `str` in string list `tbl`, `ml` is the minimun len
  local function inlist(str, tbl, ml, tn)
    local sl = len(str)
    if sl < (ml or 0) then return nil end
    str = lwr(str)
    for k, v in pairs(tbl) do
      if str == lwr(sub(v, 1, sl)) then
        if tn then tn[0] = k end
        return k
      end
    end
  end
  local function fnil() end
--[[ DATE FUNCTIONS ]]--
  local DATE_EPOCH -- to be set later
  local sl_weekdays = {
    [0]="Sunday",[1]="Monday",[2]="Tuesday",[3]="Wednesday",[4]="Thursday",[5]="Friday",[6]="Saturday",
    [7]="Sun",[8]="Mon",[9]="Tue",[10]="Wed",[11]="Thu",[12]="Fri",[13]="Sat",
  }
  local sl_meridian = {[-1]="AM", [1]="PM"}
  local sl_months = {
    [00]="January", [01]="February", [02]="March",
    [03]="April",   [04]="May",      [05]="June",
    [06]="July",    [07]="August",   [08]="September",
    [09]="October", [10]="November", [11]="December",
    [12]="Jan", [13]="Feb", [14]="Mar",
    [15]="Apr", [16]="May", [17]="Jun",
    [18]="Jul", [19]="Aug", [20]="Sep",
    [21]="Oct", [22]="Nov", [23]="Dec",
  }
  -- added the '.2'  to avoid collision, use `fix` to remove
  local sl_timezone = {
    [000]="utc",    [0.2]="gmt",
    [300]="est",    [240]="edt",
    [360]="cst",  [300.2]="cdt",
    [420]="mst",  [360.2]="mdt",
    [480]="pst",  [420.2]="pdt",
  }
  -- set the day fraction resolution
  local function setticks(t)
    TICKSPERSEC = t;
    TICKSPERDAY = SECPERDAY*TICKSPERSEC
    TICKSPERHOUR= SECPERHOUR*TICKSPERSEC
    TICKSPERMIN = SECPERMIN*TICKSPERSEC
  end
  -- is year y leap year?
  local function isleapyear(y) -- y must be int!
    return (mod(y, 4) == 0 and (mod(y, 100) ~= 0 or mod(y, 400) == 0))
  end
  -- day since year 0
  local function dayfromyear(y) -- y must be int!
    return 365*y + floor(y/4) - floor(y/100) + floor(y/400)
  end
  -- day number from date, month is zero base
  local function makedaynum(y, m, d)
    local mm = mod(mod(m,12) + 10, 12)
    return dayfromyear(y + floor(m/12) - floor(mm/10)) + floor((mm*306 + 5)/10) + d - 307
    --local yy = y + floor(m/12) - floor(mm/10)
    --return dayfromyear(yy) + floor((mm*306 + 5)/10) + (d - 1)
  end
  -- date from day number, month is zero base
  local function breakdaynum(g)
    local g = g + 306
    local y = floor((10000*g + 14780)/3652425)
    local d = g - dayfromyear(y)
    if d < 0 then y = y - 1; d = g - dayfromyear(y) end
    local mi = floor((100*d + 52)/3060)
    return (floor((mi + 2)/12) + y), mod(mi + 2,12), (d - floor((mi*306 + 5)/10) + 1)
  end
  --[[ for floats or int32 Lua Number data type
  local function breakdaynum2(g)
    local g, n = g + 306;
    local n400 = floor(g/DI400Y);n = mod(g,DI400Y);
    local n100 = floor(n/DI100Y);n = mod(n,DI100Y);
    local n004 = floor(n/DI4Y);   n = mod(n,DI4Y);
    local n001 = floor(n/365);   n = mod(n,365);
    local y = (n400*400) + (n100*100) + (n004*4) + n001  - ((n001 == 4 or n100 == 4) and 1 or 0)
    local d = g - dayfromyear(y)
    local mi = floor((100*d + 52)/3060)
    return (floor((mi + 2)/12) + y), mod(mi + 2,12), (d - floor((mi*306 + 5)/10) + 1)
  end
  ]]
  -- day fraction from time
  local function makedayfrc(h,r,s,t)
    return ((h*60 + r)*60 + s)*TICKSPERSEC + t
  end
  -- time from day fraction
  local function breakdayfrc(df)
    return
      mod(floor(df/TICKSPERHOUR),HOURPERDAY),
      mod(floor(df/TICKSPERMIN ),MINPERHOUR),
      mod(floor(df/TICKSPERSEC ),SECPERMIN),
      mod(df,TICKSPERSEC)
  end
  -- weekday sunday = 0, monday = 1 ...
  local function weekday(dn) return mod(dn + 1, 7) end
  -- yearday 0 based ...
  local function yearday(dn)
     return dn - dayfromyear((breakdaynum(dn))-1)
  end
  -- parse v as a month
  local function getmontharg(v)
    local m = tonumber(v);
    return (m and fix(m - 1)) or inlist(tostring(v) or "", sl_months, 2)
  end
  -- get daynum of isoweek one of year y
  local function isow1(y)
    local f = makedaynum(y, 0, 4) -- get the date for the 4-Jan of year `y`
    local d = weekday(f)
    d = d == 0 and 7 or d -- get the ISO day number, 1 == Monday, 7 == Sunday
    return f + (1 - d)
  end
  local function isowy(dn)
    local w1;
    local y = (breakdaynum(dn))
    if dn >= makedaynum(y, 11, 29) then
      w1 = isow1(y + 1);
      if dn < w1 then
        w1 = isow1(y);
      else
          y = y + 1;
      end
    else
      w1 = isow1(y);
      if dn < w1 then
        w1 = isow1(y-1)
        y = y - 1
      end
    end
    return floor((dn-w1)/7)+1, y
  end
  local function isoy(dn)
    local y = (breakdaynum(dn))
    return y + (((dn >= makedaynum(y, 11, 29)) and (dn >= isow1(y + 1))) and 1 or (dn < isow1(y) and -1 or 0))
  end
  local function makedaynum_isoywd(y,w,d)
    return isow1(y) + 7*w + d - 8 -- simplified: isow1(y) + ((w-1)*7) + (d-1)
  end
--[[ THE DATE MODULE ]]--
  local fmtstr  = "%x %X";
--#if not DATE_OBJECT_AFX then
  local date = {}
  setmetatable(date, date)
-- Version:  VMMMRRRR; V-Major, M-Minor, R-Revision;  e.g. 5.45.321 == 50450321
  do
    local major = 2
    local minor = 2
    local revision = 1
    date.version = major * 10000000 + minor * 10000 + revision
  end
--#end -- not DATE_OBJECT_AFX
--[[ THE DATE OBJECT ]]--
  local dobj = {}
  dobj.__index = dobj
  dobj.__metatable = dobj
  -- shout invalid arg
  local function date_error_arg() return error("invalid argument(s)",0) end
  -- create new date object
  local function date_new(dn, df)
    return setmetatable({daynum=dn, dayfrc=df}, dobj)
  end

--#if not NO_LOCAL_TIME_SUPPORT then
  -- magic year table
  local date_epoch, yt;
  local function getequivyear(y)
    assert(not yt)
    yt = {}
    local de = date_epoch:copy()
    local dw, dy
    for _ = 0, 3000 do
      de:setyear(de:getyear() + 1, 1, 1)
      dy = de:getyear()
      dw = de:getweekday() * (isleapyear(dy) and  -1 or 1)
      if not yt[dw] then yt[dw] = dy end  --print(de)
      if yt[1] and yt[2] and yt[3] and yt[4] and yt[5] and yt[6] and yt[7] and yt[-1] and yt[-2] and yt[-3] and yt[-4] and yt[-5] and yt[-6] and yt[-7] then
        getequivyear = function(y)  return yt[ (weekday(makedaynum(y, 0, 1)) + 1) * (isleapyear(y) and  -1 or 1) ]  end
        return getequivyear(y)
      end
    end
  end
  -- TimeValue from date and time
  local function totv(y,m,d,h,r,s)
    return (makedaynum(y, m, d) - DATE_EPOCH) * SECPERDAY  + ((h*60 + r)*60 + s)
  end
  -- TimeValue from TimeTable
  local function tmtotv(tm)
    return tm and totv(tm.year, tm.month - 1, tm.day, tm.hour, tm.min, tm.sec)
  end
  -- Returns the bias in seconds of utc time daynum and dayfrc
  local function getbiasutc2(self)
    local y,m,d = breakdaynum(self.daynum)
    local h,r,s = breakdayfrc(self.dayfrc)
    local tvu = totv(y,m,d,h,r,s) -- get the utc TimeValue of date and time
    local tml = osdate("*t", tvu) -- get the local TimeTable of tvu
    if (not tml) or (tml.year > (y+1) or tml.year < (y-1)) then -- failed try the magic
      y = getequivyear(y)
      tvu = totv(y,m,d,h,r,s)
      tml = osdate("*t", tvu)
    end
    local tvl = tmtotv(tml)
    if tvu and tvl then
      return tvu - tvl, tvu, tvl
    else
      return error("failed to get bias from utc time")
    end
  end
  -- Returns the bias in seconds of local time daynum and dayfrc
  local function getbiasloc2(daynum, dayfrc)
    local tvu
    -- extract date and time
    local y,m,d = breakdaynum(daynum)
    local h,r,s = breakdayfrc(dayfrc)
    -- get equivalent TimeTable
    local tml = {year=y, month=m+1, day=d, hour=h, min=r, sec=s}
    -- get equivalent TimeValue
    local tvl = tmtotv(tml)

    local function chkutc()
      tml.isdst =  nil; local tvug = ostime(tml) if tvug and (tvl == tmtotv(osdate("*t", tvug))) then tvu = tvug return end
      tml.isdst = true; local tvud = ostime(tml) if tvud and (tvl == tmtotv(osdate("*t", tvud))) then tvu = tvud return end
      tvu = tvud or tvug
    end
    chkutc()
    if not tvu then
      tml.year = getequivyear(y)
      tvl = tmtotv(tml)
      chkutc()
    end
    return ((tvu and tvl) and (tvu - tvl)) or error("failed to get bias from local time"), tvu, tvl
  end
--#end -- not NO_LOCAL_TIME_SUPPORT

--#if not DATE_OBJECT_AFX then
  -- the date parser
  local strwalker = {} -- ^Lua regular expression is not as powerful as Perl$
  strwalker.__index = strwalker
  local function newstrwalker(s)return setmetatable({s=s, i=1, e=1, c=len(s)}, strwalker) end
  function strwalker:aimchr() return "\n" .. self.s .. "\n" .. rep(".",self.e-1) .. "^" end
  function strwalker:finish() return self.i > self.c  end
  function strwalker:back()  self.i = self.e return self  end
  function strwalker:restart() self.i, self.e = 1, 1 return self end
  function strwalker:match(s)  return (find(self.s, s, self.i)) end
  function strwalker:__call(s, f)-- print("strwalker:__call "..s..self:aimchr())
    local is, ie; is, ie, self[1], self[2], self[3], self[4], self[5] = find(self.s, s, self.i)
    if is then self.e, self.i = self.i, 1+ie; if f then f(unpack(self)) end return self end
  end
  local function date_parse(str)
    local y,m,d, h,r,s,  z,  w,u, j,  e,  x,c,  dn,df
    local sw = newstrwalker(gsub(gsub(str, "(%b())", ""),"^(%s*)","")) -- remove comment, trim leading space
    --local function error_out() print(y,m,d,h,r,s) end
    local function error_dup(q) --[[error_out()]] error("duplicate value: " .. (q or "") .. sw:aimchr()) end
    local function error_syn(q) --[[error_out()]] error("syntax error: " .. (q or "") .. sw:aimchr()) end
    local function error_inv(q) --[[error_out()]] error("invalid date: " .. (q or "") .. sw:aimchr()) end
    local function sety(q) y = y and error_dup() or tonumber(q); end
    local function setm(q) m = (m or w or j) and error_dup(m or w or j) or tonumber(q) end
    local function setd(q) d = d and error_dup() or tonumber(q) end
    local function seth(q) h = h and error_dup() or tonumber(q) end
    local function setr(q) r = r and error_dup() or tonumber(q) end
    local function sets(q) s = s and error_dup() or tonumber(q) end
    local function adds(q) s = s + tonumber("."..string.sub(q,2,-1)) end
    local function setj(q) j = (m or w or j) and error_dup() or tonumber(q); end
    local function setz(q) z = (z ~= 0 and z) and error_dup() or q end
    local function setzn(zs,zn) zn = tonumber(zn); setz( ((zn<24) and (zn*60) or (mod(zn,100) + floor(zn/100) * 60))*( zs=='+' and -1 or 1) ) end
    local function setzc(zs,zh,zm) setz( ((tonumber(zh)*60) + tonumber(zm))*( zs=='+' and -1 or 1) ) end

    if not (sw("^(%d%d%d%d)",sety) and (sw("^(%-?)(%d%d)%1(%d%d)",function(_,a,b) setm(tonumber(a)); setd(tonumber(b)) end) or sw("^(%-?)[Ww](%d%d)%1(%d?)",function(_,a,b) w, u = tonumber(a), tonumber(b or 1) end) or sw("^%-?(%d%d%d)",setj) or sw("^%-?(%d%d)",function(a) setm(a);setd(1) end))
    and ((sw("^%s*[Tt]?(%d%d):?",seth) and sw("^(%d%d):?",setr) and sw("^(%d%d)",sets) and sw("^([,%.]%d+)",adds) and sw("%s*([+-])(%d%d):?(%d%d)%s*$",setzc))
      or sw:finish() or (sw"^%s*$" or sw"^%s*[Zz]%s*$" or sw("^%s-([%+%-])(%d%d):?(%d%d)%s*$",setzc) or sw("^%s*([%+%-])(%d%d)%s*$",setzn))
      )  )
    then --print(y,m,d,h,r,s,z,w,u,j)
    sw:restart(); y,m,d,h,r,s,z,w,u,j = nil,nil,nil,nil,nil,nil,nil,nil,nil,nil
      repeat -- print(sw:aimchr())
        if sw("^[tT:]?%s*(%d%d?):",seth) then --print("$Time")
          _ = sw("^%s*(%d%d?)",setr) and sw("^%s*:%s*(%d%d?)",sets) and sw("^([,%.]%d+)",adds)
        elseif sw("^(%d+)[/\\%s,-]?%s*") then --print("$Digits")
          x, c = tonumber(sw[1]), len(sw[1])
          if (x >= 70) or (m and d and (not y)) or (c > 3) then
            sety( x + ((x >= 100 or c>3) and 0 or x<centuryflip and 2000 or 1900) )
          else
            if m then setd(x) else m = x end
          end
        elseif sw("^(%a+)[/\\%s,-]?%s*") then --print("$Words")
          x = sw[1]
          if inlist(x, sl_months,   2, sw) then
            if m and (not d) and (not y) then d, m = m, false end
            setm(mod(sw[0],12)+1)
          elseif inlist(x, sl_timezone, 2, sw) then
            c = fix(sw[0]) -- ignore gmt and utc
            if c ~= 0 then setz(c) end
          elseif not inlist(x, sl_weekdays, 2, sw) then
            sw:back()
            -- am pm bce ad ce bc
            if sw("^([bB])%s*(%.?)%s*[Cc]%s*(%2)%s*[Ee]%s*(%2)%s*") or sw("^([bB])%s*(%.?)%s*[Cc]%s*(%2)%s*") then
              e = e and error_dup() or -1
            elseif sw("^([aA])%s*(%.?)%s*[Dd]%s*(%2)%s*") or sw("^([cC])%s*(%.?)%s*[Ee]%s*(%2)%s*") then
              e = e and error_dup() or 1
            elseif sw("^([PApa])%s*(%.?)%s*[Mm]?%s*(%2)%s*") then
              x = lwr(sw[1]) -- there should be hour and it must be correct
              if (not h) or (h > 12) or (h < 0) then return error_inv() end
              if x == 'a' and h == 12 then h = 0 end -- am
              if x == 'p' and h ~= 12 then h = h + 12 end -- pm
            else error_syn() end
          end
        elseif not(sw("^([+-])(%d%d?):(%d%d)",setzc) or sw("^([+-])(%d+)",setzn) or sw("^[Zz]%s*$")) then -- sw{"([+-])",{"(%d%d?):(%d%d)","(%d+)"}}
          error_syn("?")
        end
      sw("^%s*")  until sw:finish()
    --else print("$Iso(Date|Time|Zone)")
    end
    -- if date is given, it must be complete year, month & day
    if (not y and not h) or ((m and not d) or (d and not m)) or ((m and w) or (m and j) or (j and w)) then return error_inv("!") end
    -- fix month
    if m then m = m - 1 end
    -- fix year if we are on BCE
    if e and e < 0 and y > 0 then y = 1 - y end
    --  create date object
    dn = (y and ((w and makedaynum_isoywd(y,w,u)) or (j and makedaynum(y, 0, j)) or makedaynum(y, m, d))) or DAYNUM_DEF
    df = makedayfrc(h or 0, r or 0, s or 0, 0) + ((z or 0)*TICKSPERMIN)
    --print("Zone",h,r,s,z,m,d,y,df)
    return date_new(dn, df) -- no need to :normalize();
  end
  local function date_fromtable(v)
    local y, m, d = fix(v.year), getmontharg(v.month), fix(v.day)
    local h, r, s, t = tonumber(v.hour), tonumber(v.min), tonumber(v.sec), tonumber(v.ticks)
    -- atleast there is time or complete date
    if (y or m or d) and (not(y and m and d)) then return error("incomplete table")  end
    return (y or h or r or s or t) and date_new(y and makedaynum(y, m, d) or DAYNUM_DEF, makedayfrc(h or 0, r or 0, s or 0, t or 0))
  end
  local tmap = {
    ['number'] = function(v) return date_epoch:copy():addseconds(v) end,
    ['string'] = function(v) return date_parse(v) end,
    ['boolean']= function(v) return date_fromtable(osdate(v and "!*t" or "*t")) end,
    ['table']  = function(v) local ref = getmetatable(v) == dobj; return ref and v or date_fromtable(v), ref end
  }
  local function date_getdobj(v)
    local o, r = (tmap[type(v)] or fnil)(v);
    return (o and o:normalize() or error"invalid date time value"), r -- if r is true then o is a reference to a date obj
  end
--#end -- not DATE_OBJECT_AFX
  local function date_from(arg1, arg2, arg3, arg4, arg5, arg6, arg7)
    local y, m, d = fix(arg1), getmontharg(arg2), fix(arg3)
    local h, r, s, t = tonumber(arg4 or 0), tonumber(arg5 or 0), tonumber(arg6 or 0), tonumber(arg7 or 0)
    if y and m and d and h and r and s and t then
      return date_new(makedaynum(y, m, d), makedayfrc(h, r, s, t)):normalize()
    else
      return date_error_arg()
    end
  end

 --[[ THE DATE OBJECT METHODS ]]--
  function dobj:normalize()
    local dn, df = fix(self.daynum), self.dayfrc
    self.daynum, self.dayfrc = dn + floor(df/TICKSPERDAY), mod(df, TICKSPERDAY)
    return (dn >= DAYNUM_MIN and dn <= DAYNUM_MAX) and self or error("date beyond imposed limits:"..self)
  end

  function dobj:getdate()  local y, m, d = breakdaynum(self.daynum) return y, m+1, d end
  function dobj:gettime()  return breakdayfrc(self.dayfrc) end

  function dobj:getclockhour() local h = self:gethours() return h>12 and mod(h,12) or (h==0 and 12 or h) end

  function dobj:getyearday() return yearday(self.daynum) + 1 end
  function dobj:getweekday() return weekday(self.daynum) + 1 end   -- in lua weekday is sunday = 1, monday = 2 ...

  function dobj:getyear()   local r,_,_ = breakdaynum(self.daynum)  return r end
  function dobj:getmonth() local _,r,_ = breakdaynum(self.daynum)  return r+1 end-- in lua month is 1 base
  function dobj:getday()   local _,_,r = breakdaynum(self.daynum)  return r end
  function dobj:gethours()  return mod(floor(self.dayfrc/TICKSPERHOUR),HOURPERDAY) end
  function dobj:getminutes()  return mod(floor(self.dayfrc/TICKSPERMIN), MINPERHOUR) end
  function dobj:getseconds()  return mod(floor(self.dayfrc/TICKSPERSEC ),SECPERMIN)  end
  function dobj:getfracsec()  return mod(floor(self.dayfrc/TICKSPERSEC ),SECPERMIN)+(mod(self.dayfrc,TICKSPERSEC)/TICKSPERSEC) end
  function dobj:getticks(u)  local x = mod(self.dayfrc,TICKSPERSEC) return u and ((x*u)/TICKSPERSEC) or x  end

  function dobj:getweeknumber(wdb)
    local wd, yd = weekday(self.daynum), yearday(self.daynum)
    if wdb then
      wdb = tonumber(wdb)
      if wdb then
        wd = mod(wd-(wdb-1),7)-- shift the week day base
      else
        return date_error_arg()
      end
    end
    return (yd < wd and 0) or (floor(yd/7) + ((mod(yd, 7)>=wd) and 1 or 0))
  end

  function dobj:getisoweekday() return mod(weekday(self.daynum)-1,7)+1 end   -- sunday = 7, monday = 1 ...
  function dobj:getisoweeknumber() return (isowy(self.daynum)) end
  function dobj:getisoyear() return isoy(self.daynum)  end
  function dobj:getisodate()
    local w, y = isowy(self.daynum)
    return y, w, self:getisoweekday()
  end
  function dobj:setisoyear(y, w, d)
    local cy, cw, cd = self:getisodate()
    if y then cy = fix(tonumber(y))end
    if w then cw = fix(tonumber(w))end
    if d then cd = fix(tonumber(d))end
    if cy and cw and cd then
      self.daynum = makedaynum_isoywd(cy, cw, cd)
      return self:normalize()
    else
      return date_error_arg()
    end
  end

  function dobj:setisoweekday(d)    return self:setisoyear(nil, nil, d) end
  function dobj:setisoweeknumber(w,d)  return self:setisoyear(nil, w, d)  end

  function dobj:setyear(y, m, d)
    local cy, cm, cd = breakdaynum(self.daynum)
    if y then cy = fix(tonumber(y))end
    if m then cm = getmontharg(m)  end
    if d then cd = fix(tonumber(d))end
    if cy and cm and cd then
      self.daynum  = makedaynum(cy, cm, cd)
      return self:normalize()
    else
      return date_error_arg()
    end
  end

  function dobj:setmonth(m, d)return self:setyear(nil, m, d) end
  function dobj:setday(d)    return self:setyear(nil, nil, d) end

  function dobj:sethours(h, m, s, t)
    local ch,cm,cs,ck = breakdayfrc(self.dayfrc)
    ch, cm, cs, ck = tonumber(h or ch), tonumber(m or cm), tonumber(s or cs), tonumber(t or ck)
    if ch and cm and cs and ck then
      self.dayfrc = makedayfrc(ch, cm, cs, ck)
      return self:normalize()
    else
      return date_error_arg()
    end
  end

  function dobj:setminutes(m,s,t)  return self:sethours(nil,   m,   s, t) end
  function dobj:setseconds(s, t)  return self:sethours(nil, nil,   s, t) end
  function dobj:setticks(t)    return self:sethours(nil, nil, nil, t) end

  function dobj:spanticks()  return (self.daynum*TICKSPERDAY + self.dayfrc) end
  function dobj:spanseconds()  return (self.daynum*TICKSPERDAY + self.dayfrc)/TICKSPERSEC  end
  function dobj:spanminutes()  return (self.daynum*TICKSPERDAY + self.dayfrc)/TICKSPERMIN  end
  function dobj:spanhours()  return (self.daynum*TICKSPERDAY + self.dayfrc)/TICKSPERHOUR end
  function dobj:spandays()  return (self.daynum*TICKSPERDAY + self.dayfrc)/TICKSPERDAY  end

  function dobj:addyears(y, m, d)
    local cy, cm, cd = breakdaynum(self.daynum)
    if y then y = fix(tonumber(y))else y = 0 end
    if m then m = fix(tonumber(m))else m = 0 end
    if d then d = fix(tonumber(d))else d = 0 end
    if y and m and d then
      self.daynum  = makedaynum(cy+y, cm+m, cd+d)
      return self:normalize()
    else
      return date_error_arg()
    end
  end

  function dobj:addmonths(m, d)
    return self:addyears(nil, m, d)
  end

  local function dobj_adddayfrc(self,n,pt,pd)
    n = tonumber(n)
    if n then
      local x = floor(n/pd);
      self.daynum = self.daynum + x;
      self.dayfrc = self.dayfrc + (n-x*pd)*pt;
      return self:normalize()
    else
      return date_error_arg()
    end
  end
  function dobj:adddays(n)  return dobj_adddayfrc(self,n,TICKSPERDAY,1) end
  function dobj:addhours(n)  return dobj_adddayfrc(self,n,TICKSPERHOUR,HOURPERDAY) end
  function dobj:addminutes(n)  return dobj_adddayfrc(self,n,TICKSPERMIN,MINPERDAY)  end
  function dobj:addseconds(n)  return dobj_adddayfrc(self,n,TICKSPERSEC,SECPERDAY)  end
  function dobj:addticks(n)  return dobj_adddayfrc(self,n,1,TICKSPERDAY) end
  local tvspec = {
    -- Abbreviated weekday name (Sun)
    ['%a']=function(self) return sl_weekdays[weekday(self.daynum) + 7] end,
    -- Full weekday name (Sunday)
    ['%A']=function(self) return sl_weekdays[weekday(self.daynum)] end,
    -- Abbreviated month name (Dec)
    ['%b']=function(self) return sl_months[self:getmonth() - 1 + 12] end,
    -- Full month name (December)
    ['%B']=function(self) return sl_months[self:getmonth() - 1] end,
    -- Year/100 (19, 20, 30)
    ['%C']=function(self) return fmt("%.2d", fix(self:getyear()/100)) end,
    -- The day of the month as a number (range 1 - 31)
    ['%d']=function(self) return fmt("%.2d", self:getday())  end,
    -- year for ISO 8601 week, from 00 (79)
    ['%g']=function(self) return fmt("%.2d", mod(self:getisoyear() ,100)) end,
    -- year for ISO 8601 week, from 0000 (1979)
    ['%G']=function(self) return fmt("%.4d", self:getisoyear()) end,
    -- same as %b
    ['%h']=function(self) return self:fmt0("%b") end,
    -- hour of the 24-hour day, from 00 (06)
    ['%H']=function(self) return fmt("%.2d", self:gethours()) end,
    -- The  hour as a number using a 12-hour clock (01 - 12)
    ['%I']=function(self) return fmt("%.2d", self:getclockhour()) end,
    -- The day of the year as a number (001 - 366)
    ['%j']=function(self) return fmt("%.3d", self:getyearday())  end,
    -- Month of the year, from 01 to 12
    ['%m']=function(self) return fmt("%.2d", self:getmonth())  end,
    -- Minutes after the hour 55
    ['%M']=function(self) return fmt("%.2d", self:getminutes())end,
    -- AM/PM indicator (AM)
    ['%p']=function(self) return sl_meridian[self:gethours() > 11 and 1 or -1] end, --AM/PM indicator (AM)
    -- The second as a number (59, 20 , 01)
    ['%S']=function(self) return fmt("%.2d", self:getseconds())  end,
    -- ISO 8601 day of the week, to 7 for Sunday (7, 1)
    ['%u']=function(self) return self:getisoweekday() end,
    -- Sunday week of the year, from 00 (48)
    ['%U']=function(self) return fmt("%.2d", self:getweeknumber()) end,
    -- ISO 8601 week of the year, from 01 (48)
    ['%V']=function(self) return fmt("%.2d", self:getisoweeknumber()) end,
    -- The day of the week as a decimal, Sunday being 0
    ['%w']=function(self) return self:getweekday() - 1 end,
    -- Monday week of the year, from 00 (48)
    ['%W']=function(self) return fmt("%.2d", self:getweeknumber(2)) end,
    -- The year as a number without a century (range 00 to 99)
    ['%y']=function(self) return fmt("%.2d", mod(self:getyear() ,100)) end,
    -- Year with century (2000, 1914, 0325, 0001)
    ['%Y']=function(self) return fmt("%.4d", self:getyear()) end,
    -- Time zone offset, the date object is assumed local time (+1000, -0230)
    ['%z']=function(self) local b = -self:getbias(); local x = abs(b); return fmt("%s%.4d", b < 0 and "-" or "+", fix(x/60)*100 + floor(mod(x,60))) end,
    -- Time zone name, the date object is assumed local time
    ['%Z']=function(self) return self:gettzname() end,
    -- Misc --
    -- Year, if year is in BCE, prints the BCE Year representation, otherwise result is similar to "%Y" (1 BCE, 40 BCE)
    ['%\b']=function(self) local x = self:getyear() return fmt("%.4d%s", x>0 and x or (-x+1), x>0 and "" or " BCE") end,
    -- Seconds including fraction (59.998, 01.123)
    ['%\f']=function(self) local x = self:getfracsec() return fmt("%s%.9f",x >= 10 and "" or "0", x) end,
    -- percent character %
    ['%%']=function(self) return "%" end,
    -- Group Spec --
    -- 12-hour time, from 01:00:00 AM (06:55:15 AM); same as "%I:%M:%S %p"
    ['%r']=function(self) return self:fmt0("%I:%M:%S %p") end,
    -- hour:minute, from 01:00 (06:55); same as "%I:%M"
    ['%R']=function(self) return self:fmt0("%I:%M")  end,
    -- 24-hour time, from 00:00:00 (06:55:15); same as "%H:%M:%S"
    ['%T']=function(self) return self:fmt0("%H:%M:%S") end,
    -- month/day/year from 01/01/00 (12/02/79); same as "%m/%d/%y"
    ['%D']=function(self) return self:fmt0("%m/%d/%y") end,
    -- year-month-day (1979-12-02); same as "%Y-%m-%d"
    ['%F']=function(self) return self:fmt0("%Y-%m-%d") end,
    -- The preferred date and time representation;  same as "%x %X"
    ['%c']=function(self) return self:fmt0("%x %X") end,
    -- The preferred date representation, same as "%a %b %d %\b"
    ['%x']=function(self) return self:fmt0("%a %b %d %\b") end,
    -- The preferred time representation, same as "%H:%M:%\f"
    ['%X']=function(self) return self:fmt0("%H:%M:%\f") end,
    -- GroupSpec --
    -- Iso format, same as "%Y-%m-%dT%T"
    ['${iso}'] = function(self) return self:fmt0("%Y-%m-%dT%T") end,
    -- http format, same as "%a, %d %b %Y %T GMT"
    ['${http}'] = function(self) return self:fmt0("%a, %d %b %Y %T GMT") end,
    -- ctime format, same as "%a %b %d %T GMT %Y"
    ['${ctime}'] = function(self) return self:fmt0("%a %b %d %T GMT %Y") end,
    -- RFC850 format, same as "%A, %d-%b-%y %T GMT"
    ['${rfc850}'] = function(self) return self:fmt0("%A, %d-%b-%y %T GMT") end,
    -- RFC1123 format, same as "%a, %d %b %Y %T GMT"
    ['${rfc1123}'] = function(self) return self:fmt0("%a, %d %b %Y %T GMT") end,
    -- asctime format, same as "%a %b %d %T %Y"
    ['${asctime}'] = function(self) return self:fmt0("%a %b %d %T %Y") end,
  }
  function dobj:fmt0(str) return (gsub(str, "%%[%a%%\b\f]", function(x) local f = tvspec[x];return (f and f(self)) or x end)) end
  function dobj:fmt(str)
    str = str or self.fmtstr or fmtstr
    return self:fmt0((gmatch(str, "${%w+}")) and (gsub(str, "${%w+}", function(x)local f=tvspec[x];return (f and f(self)) or x end)) or str)
  end

  function dobj.__lt(a, b) if (a.daynum == b.daynum) then return (a.dayfrc < b.dayfrc) else return (a.daynum < b.daynum) end end
  function dobj.__le(a, b) if (a.daynum == b.daynum) then return (a.dayfrc <= b.dayfrc) else return (a.daynum <= b.daynum) end end
  function dobj.__eq(a, b)return (a.daynum == b.daynum) and (a.dayfrc == b.dayfrc) end
  function dobj.__sub(a,b)
    local d1, d2 = date_getdobj(a), date_getdobj(b)
    local d0 = d1 and d2 and date_new(d1.daynum - d2.daynum, d1.dayfrc - d2.dayfrc)
    return d0 and d0:normalize()
  end
  function dobj.__add(a,b)
    local d1, d2 = date_getdobj(a), date_getdobj(b)
    local d0 = d1 and d2 and date_new(d1.daynum + d2.daynum, d1.dayfrc + d2.dayfrc)
    return d0 and d0:normalize()
  end
  function dobj.__concat(a, b) return tostring(a) .. tostring(b) end
  function dobj:__tostring() return self:fmt() end

  function dobj:copy() return date_new(self.daynum, self.dayfrc) end

--[[ THE LOCAL DATE OBJECT METHODS ]]--
  function dobj:tolocal()
    local dn,df = self.daynum, self.dayfrc
    local bias  = getbiasutc2(self)
    if bias then
      -- utc = local + bias; local = utc - bias
      self.daynum = dn
      self.dayfrc = df - bias*TICKSPERSEC
      return self:normalize()
    else
      return nil
    end
  end

  function dobj:toutc()
    local dn,df = self.daynum, self.dayfrc
    local bias  = getbiasloc2(dn, df)
    if bias then
      -- utc = local + bias;
      self.daynum = dn
      self.dayfrc = df + bias*TICKSPERSEC
      return self:normalize()
    else
      return nil
    end
  end

  function dobj:getbias()  return (getbiasloc2(self.daynum, self.dayfrc))/SECPERMIN end

  function dobj:gettzname()
    local _, tvu, _ = getbiasloc2(self.daynum, self.dayfrc)
    return tvu and osdate("%Z",tvu) or ""
  end

--#if not DATE_OBJECT_AFX then
  function date.time(h, r, s, t)
    h, r, s, t = tonumber(h or 0), tonumber(r or 0), tonumber(s or 0), tonumber(t or 0)
    if h and r and s and t then
       return date_new(DAYNUM_DEF, makedayfrc(h, r, s, t))
    else
      return date_error_arg()
    end
  end

  function date:__call(arg1, ...)
    local arg_count = select("#", ...) + (arg1 == nil and 0 or 1)
    if arg_count  > 1 then return (date_from(arg1, ...))
    elseif arg_count == 0 then return (date_getdobj(false))
    else local o, r = date_getdobj(arg1);  return r and o:copy() or o end
  end

  date.diff = dobj.__sub

  function date.isleapyear(v)
    local y = fix(v);
    if not y then
      y = date_getdobj(v)
      y = y and y:getyear()
    end
    return isleapyear(y+0)
  end

  function date.epoch() return date_epoch:copy()  end

  function date.isodate(y,w,d) return date_new(makedaynum_isoywd(y + 0, w and (w+0) or 1, d and (d+0) or 1), 0)  end
  function date.setcenturyflip(y)
    if y ~= floor(y) or y < 0 or y > 100 then date_error_arg() end
    centuryflip = y
  end
  function date.getcenturyflip() return centuryflip end

-- Internal functions
  function date.fmt(str) if str then fmtstr = str end; return fmtstr end
  function date.daynummin(n)  DAYNUM_MIN = (n and n < DAYNUM_MAX) and n or DAYNUM_MIN  return n and DAYNUM_MIN or date_new(DAYNUM_MIN, 0):normalize()end
  function date.daynummax(n)  DAYNUM_MAX = (n and n > DAYNUM_MIN) and n or DAYNUM_MAX return n and DAYNUM_MAX or date_new(DAYNUM_MAX, 0):normalize()end
  function date.ticks(t) if t then setticks(t) end return TICKSPERSEC  end
--#end -- not DATE_OBJECT_AFX

  local tm = osdate("!*t", 0);
  if tm then
    date_epoch = date_new(makedaynum(tm.year, tm.month - 1, tm.day), makedayfrc(tm.hour, tm.min, tm.sec, 0))
    -- the distance from our epoch to os epoch in daynum
    DATE_EPOCH = date_epoch and date_epoch:spandays()
  else -- error will be raise only if called!
    date_epoch = setmetatable({},{__index = function() error("failed to get the epoch date") end})
  end

--#if not DATE_OBJECT_AFX then
return date
--#else
--$return date_from
--#end

```

