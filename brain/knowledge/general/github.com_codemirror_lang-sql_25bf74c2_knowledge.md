---
id: github.com-codemirror-lang-sql-25bf74c2-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:41.004842
---

# KNOWLEDGE EXTRACT: github.com_codemirror_lang-sql_25bf74c2
> **Extracted on:** 2026-04-01 15:40:30
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524674/github.com_codemirror_lang-sql_25bf74c2

---

## File: `.gitignore`
```
/node_modules
package-lock.json
/dist
/test/*.js
/test/*.d.ts
/test/*.d.ts.map
.tern-*
```

## File: `.npmignore`
```
/src
/test
/node_modules
.tern-*
rollup.config.js
tsconfig.json
```

## File: `CHANGELOG.md`
```markdown
## 6.10.0 (2025-09-16)

### New features

Allow `[` in `identifierQuotes` for MSSQL-style bracketed identifiers.

## 6.9.1 (2025-07-28)

### Bug fixes

Include more MSSQL keyboards and builtins in the completions.

Allow built-in special variables for a dialect to be completed.

## 6.9.0 (2025-05-30)

### New features

The new `SQLDialect.configureLanguage` method can be used to configure the language (and it's syntax node props) used by a dialect.

## 6.8.0 (2024-10-01)

### New features

The new `keywordCompletion` option can be used to define what kind of completions are generated for keywords.

## 6.7.1 (2024-08-21)

### Bug fixes

Remove single-letter words from the list of Postgres keywords, since they interfere with alias-based autocompletion.

## 6.7.0 (2024-06-24)

### New features

Dialects can now disable quoting of identifiers containing upper-case characters with the `caseInsensitiveIdentifiers` option.

## 6.6.5 (2024-06-17)

### Bug fixes

Fix a bug that broke tokenizing of `e'\n'`-style strings.

## 6.6.4 (2024-05-04)

### Bug fixes

Make statement folding leave the entire first line visible.

Fix a null dereference in schema-based autocompletion.

## 6.6.3 (2024-04-08)

### Bug fixes

Fix a bug where Postgres-style dollar-quoted strings were enabled for all dialects, and the `doubleDollarQuotedStrings` options was ignored.

## 6.6.2 (2024-03-23)

### Bug fixes

Properly support tags in PostgreSQL `4073` quoted strings.

## 6.6.1 (2024-03-04)

### Bug fixes

Fix an issue that caused completions to be missing when using the `defaultSchema` option.

## 6.6.0 (2024-02-29)

### Bug fixes

Don't tokenize identifiers after periods as anything but plain identifiers.

### New features

The `schema` option now allows nested objects to define multiple levels of completions, as well as `self` completion options for specific levels. The old format (using `tables`/`schemas`) continues to work but is deprecated.

## 6.5.5 (2023-12-28)

### Bug fixes

Make sure table and column completions with upper-case characters are quoted.

Tag comments and strings as isolating for the purpose of bidirectional text.

## 6.5.4 (2023-08-10)

### Bug fixes

Remove use of negative lookbehind in a regular expression, which recent versions of Safari still don't support.

## 6.5.3 (2023-08-05)

### Bug fixes

The PL/SQL dialect now correctly handles `q'[]'`-quoting syntax.

## 6.5.2 (2023-06-23)

### Bug fixes

Allow table names to contain multiple dots in the schema passed to `schemaCompletionSource`.

## 6.5.1 (2023-06-21)

### Bug fixes

`schemaCompletionSource` now adds quotes around non-word identifiers even if the user didn't type a starting quote.

## 6.5.0 (2023-05-16)

### New features

Dialect objects now have a public `spec` property holding their configuration.

## 6.4.1 (2023-04-13)

### Bug fixes

Fix a bug where tokenizing of block comments got confused when nested comment start/end markers appeared directly next to each other.

## 6.4.0 (2023-01-23)

### Bug fixes

Fix syntax tree node names for curly and square brackets, which had their names swapped.

### New features

The new `schemas` config option can be used to provide custom completion objects for schema completions.

## 6.3.3 (2022-11-14)

### Bug fixes

Fix tokenizing of double-`$` strings in SQL dialects that support them.

## 6.3.2 (2022-10-24)

### Bug fixes

Make sure the language object has a name.

## 6.3.1 (2022-10-17)

### Bug fixes

Fix tokenizing of `--` line comments.

## 6.3.0 (2022-08-23)

### New features

Schema-based completion now understands basic table alias syntax, and will take it into account when looking up completions.

## 6.2.0 (2022-08-14)

### New features

The new `unquotedBitLiterals` dialect option controls whether `0b01` syntax is recognized.

Dialects now allow a `treatBitsAsBytes` option to allow any characters inside quoted strings prefixed with `b`.

## 6.1.0 (2022-08-05)

### New features

The new `doubleDollarQuotedStrings` options to SQL dialects allows parsing of text delimited by `$$` as strings. Regenerate readme

## 6.0.0 (2022-06-08)

### Breaking changes

Update dependencies to 6.0.0

## 0.20.4 (2022-05-30)

### New features

Schema completion descriptions may now include dots in table names to indicate nested schemas.

## 0.20.3 (2022-05-27)

### Bug fixes

Fix a bug where the slash at the end of block comments wasn't considered part of the comment token.

## 0.20.2 (2022-05-24)

### Bug fixes

Fix an infinite recursion bug in `schemaCompletionSource`.

## 0.20.1 (2022-05-24)

### Breaking changes

The `schemaCompletion` and `keywordCompletion` exports, which returned extensions, have been replaced with `schemaCompletionSource` and `keywordCompletionSource`, which return completion sources. The old exports will remain available until the next major version.

## 0.20.0 (2022-04-20)

### Bug fixes

Fix autocompletion on columns when the table name is written with upper-case letters. Move to @lezer/highlight

## 0.19.4 (2021-10-28)

### Bug fixes

Remove duplicate keywords/types in dialect configurations.

Fix a bug that caused characters directly before a space to be tokenized incorrectly.

## 0.19.3 (2021-08-21)

### Bug fixes

Fix a bug that broke tokenization of keywords.

## 0.19.2 (2021-08-11)

## 0.19.1 (2021-08-11)

### Bug fixes

Fix incorrect versions for @lezer dependencies.

## 0.19.0 (2021-08-11)

### Breaking changes

Update dependencies to 0.19.0

## 0.18.0 (2021-03-03)

### Breaking changes

Update dependencies to 0.18.

## 0.17.2 (2021-02-01)

### Bug fixes

Fix bad syntax tree creation when the input ends with an unfinished quoted identifier.

## 0.17.1 (2021-01-06)

### New features

The package now also exports a CommonJS module.

## 0.17.0 (2020-12-29)

### Breaking changes

First numbered release.

```

## File: `LICENSE`
```
MIT License

Copyright (C) 2018-2021 by Marijn Haverbeke <marijn@haverbeke.berlin> and others

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

## File: `README.md`
```markdown
<!-- NOTE: README.md is generated from src/README.md -->

# @codemirror/lang-sql [![NPM version](https://img.shields.io/npm/v/@codemirror/lang-sql.svg)](https://www.npmjs.org/package/@codemirror/lang-sql)

[ [**WEBSITE**](https://codemirror.net/) | [**ISSUES**](https://github.com/codemirror/dev/issues) | [**FORUM**](https://discuss.codemirror.net/) | [**CHANGELOG**](https://github.com/codemirror/lang-sql/blob/main/CHANGELOG.md) ]

This package implements SQL language support for the
[CodeMirror](https://codemirror.net/) code editor.

The [project page](https://codemirror.net/) has more information, a
number of [examples](https://codemirror.net/examples/) and the
[documentation](https://codemirror.net/brain/knowledge/docs_legacy/).

This code is released under an
[MIT license](https://github.com/codemirror/lang-sql/tree/main/LICENSE).

We aim to be an inclusive, welcoming community. To make that explicit,
we have a [code of
conduct](http://contributor-covenant.org/version/1/1/0/) that applies
to communication around the project.

## Usage

```javascript
import {EditorView, basicSetup} from "codemirror"
import {sql} from "@codemirror/lang-sql"

const view = new EditorView({
  parent: document.body,
  doc: `select * from users where age > 20`,
  extensions: [basicSetup, sql()]
})
```

Use `sql({dialect: PostgreSQL})` or similar to select a specific SQL
dialect.

## API Reference

<dl>
<dt id="user-content-sql">
  <code><strong><a href="#user-content-sql">sql</a></strong>(<a id="user-content-sql^config" href="#user-content-sql^config">config</a>&#8288;?: <a href="#user-content-sqlconfig">SQLConfig</a> = {}) → <a href="https://codemirror.net/brain/knowledge/docs_legacy/ref#language.LanguageSupport">LanguageSupport</a></code></dt>

<dd><p>SQL language support for the given SQL dialect, with keyword
completion, and, if provided, schema-based completion as extra
extensions.</p>
</dd>
<dt id="user-content-sqlconfig">
  <h4>
    <code>interface</code>
    <a href="#user-content-sqlconfig">SQLConfig</a></h4>
</dt>

<dd><p>Options used to configure an SQL extension.</p>
<dl><dt id="user-content-sqlconfig.dialect">
  <code><strong><a href="#user-content-sqlconfig.dialect">dialect</a></strong>&#8288;?: <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p>The <a href="#user-content-sqldialect">dialect</a> to use. Defaults to
<a href="#user-content-standardsql"><code>StandardSQL</code></a>.</p>
</dd><dt id="user-content-sqlconfig.schema">
  <code><strong><a href="#user-content-sqlconfig.schema">schema</a></strong>&#8288;?: <a href="#user-content-sqlnamespace">SQLNamespace</a></code></dt>

<dd><p>You can use this to define the schemas, tables, and their fields
for autocompletion.</p>
</dd><dt id="user-content-sqlconfig.defaulttable">
  <code><strong><a href="#user-content-sqlconfig.defaulttable">defaultTable</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a></code></dt>

<dd><p>When given, columns from the named table can be completed
directly at the top level.</p>
</dd><dt id="user-content-sqlconfig.defaultschema">
  <code><strong><a href="#user-content-sqlconfig.defaultschema">defaultSchema</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a></code></dt>

<dd><p>When given, tables prefixed with this schema name can be
completed directly at the top level.</p>
</dd><dt id="user-content-sqlconfig.uppercasekeywords">
  <code><strong><a href="#user-content-sqlconfig.uppercasekeywords">upperCaseKeywords</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>When set to true, keyword completions will be upper-case.</p>
</dd><dt id="user-content-sqlconfig.keywordcompletion">
  <code><strong><a href="#user-content-sqlconfig.keywordcompletion">keywordCompletion</a></strong>&#8288;?: fn(<a id="user-content-sqlconfig.keywordcompletion^label" href="#user-content-sqlconfig.keywordcompletion^label">label</a>: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a>, <a id="user-content-sqlconfig.keywordcompletion^type" href="#user-content-sqlconfig.keywordcompletion^type">type</a>: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a>) → <a href="https://codemirror.net/brain/knowledge/docs_legacy/ref#autocomplete.Completion">Completion</a></code></dt>

<dd><p>Can be used to customize the completions generated for keywords.</p>
</dd></dl>

</dd>
<dt id="user-content-sqlnamespace">
  <code>type</code>
  <code><strong><a href="#user-content-sqlnamespace">SQLNamespace</a></strong> = <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Object">Object</a>&lt;<a href="#user-content-sqlnamespace">SQLNamespace</a>&gt; | {self: <a href="https://codemirror.net/brain/knowledge/docs_legacy/ref#autocomplete.Completion">Completion</a>, children: <a href="#user-content-sqlnamespace">SQLNamespace</a>} | readonly (<a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a> | <a href="https://codemirror.net/brain/knowledge/docs_legacy/ref#autocomplete.Completion">Completion</a>)[]</code>
</dt>

<dd><p>The type used to describe a level of the schema for
<a href="#user-content-sqlconfig.schema">completion</a>. Can be an array of
options (columns), an object mapping table or schema names to
deeper levels, or a <code>{self, children}</code> object that assigns a
completion option to use for its parent property, when the default option
(its name as label and type <code>&quot;type&quot;</code>) isn't suitable.</p>
</dd>
<dt id="user-content-sqldialect">
  <h4>
    <code>class</code>
    <a href="#user-content-sqldialect">SQLDialect</a></h4>
</dt>

<dd><p>Represents an SQL dialect.</p>
<dl><dt id="user-content-sqldialect.language">
  <code><strong><a href="#user-content-sqldialect.language">language</a></strong>: <a href="https://codemirror.net/brain/knowledge/docs_legacy/ref#language.LRLanguage">LRLanguage</a></code></dt>

<dd><p>The language for this dialect.</p>
</dd><dt id="user-content-sqldialect.spec">
  <code><strong><a href="#user-content-sqldialect.spec">spec</a></strong>: <a href="#user-content-sqldialectspec">SQLDialectSpec</a></code></dt>

<dd><p>The spec used to define this dialect.</p>
</dd><dt id="user-content-sqldialect.extension">
  <code><strong><a href="#user-content-sqldialect.extension">extension</a></strong>: <a href="https://codemirror.net/brain/knowledge/docs_legacy/ref#state.Extension">Extension</a></code></dt>

<dd><p>Returns the language for this dialect as an extension.</p>
</dd><dt id="user-content-sqldialect.configurelanguage">
  <code><strong><a href="#user-content-sqldialect.configurelanguage">configureLanguage</a></strong>(<a id="user-content-sqldialect.configurelanguage^options" href="#user-content-sqldialect.configurelanguage^options">options</a>: <a href="https://lezer.codemirror.net/brain/knowledge/docs_legacy/ref/#lr.ParserConfig">ParserConfig</a>, <a id="user-content-sqldialect.configurelanguage^name" href="#user-content-sqldialect.configurelanguage^name">name</a>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a>) → <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p>Reconfigure the parser used by this dialect. Returns a new
dialect object.</p>
</dd><dt id="user-content-sqldialect^define">
  <code>static <strong><a href="#user-content-sqldialect^define">define</a></strong>(<a id="user-content-sqldialect^define^spec" href="#user-content-sqldialect^define^spec">spec</a>: <a href="#user-content-sqldialectspec">SQLDialectSpec</a>) → <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p>Define a new dialect.</p>
</dd></dl>

</dd>
<dt id="user-content-sqldialectspec">
  <h4>
    <code>type</code>
    <a href="#user-content-sqldialectspec">SQLDialectSpec</a></h4>
</dt>

<dd><p>Configuration for an <a href="#user-content-sqldialect">SQL Dialect</a>.</p>
<dl><dt id="user-content-sqldialectspec.keywords">
  <code><strong><a href="#user-content-sqldialectspec.keywords">keywords</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a></code></dt>

<dd><p>A space-separated list of keywords for the dialect.</p>
</dd><dt id="user-content-sqldialectspec.builtin">
  <code><strong><a href="#user-content-sqldialectspec.builtin">builtin</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a></code></dt>

<dd><p>A space-separated string of built-in identifiers for the dialect.</p>
</dd><dt id="user-content-sqldialectspec.types">
  <code><strong><a href="#user-content-sqldialectspec.types">types</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a></code></dt>

<dd><p>A space-separated string of type names for the dialect.</p>
</dd><dt id="user-content-sqldialectspec.backslashescapes">
  <code><strong><a href="#user-content-sqldialectspec.backslashescapes">backslashEscapes</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>Controls whether regular strings allow backslash escapes.</p>
</dd><dt id="user-content-sqldialectspec.hashcomments">
  <code><strong><a href="#user-content-sqldialectspec.hashcomments">hashComments</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>Controls whether # creates a line comment.</p>
</dd><dt id="user-content-sqldialectspec.slashcomments">
  <code><strong><a href="#user-content-sqldialectspec.slashcomments">slashComments</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>Controls whether <code>//</code> creates a line comment.</p>
</dd><dt id="user-content-sqldialectspec.spaceafterdashes">
  <code><strong><a href="#user-content-sqldialectspec.spaceafterdashes">spaceAfterDashes</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>When enabled <code>--</code> comments are only recognized when there's a
space after the dashes.</p>
</dd><dt id="user-content-sqldialectspec.doubledollarquotedstrings">
  <code><strong><a href="#user-content-sqldialectspec.doubledollarquotedstrings">doubleDollarQuotedStrings</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>When enabled, things quoted with &quot;$&quot; are treated as
strings, rather than identifiers.</p>
</dd><dt id="user-content-sqldialectspec.doublequotedstrings">
  <code><strong><a href="#user-content-sqldialectspec.doublequotedstrings">doubleQuotedStrings</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>When enabled, things quoted with double quotes are treated as
strings, rather than identifiers.</p>
</dd><dt id="user-content-sqldialectspec.charsetcasts">
  <code><strong><a href="#user-content-sqldialectspec.charsetcasts">charSetCasts</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>Enables strings like <code>_utf8'str'</code> or <code>N'str'</code>.</p>
</dd><dt id="user-content-sqldialectspec.plsqlquotingmechanism">
  <code><strong><a href="#user-content-sqldialectspec.plsqlquotingmechanism">plsqlQuotingMechanism</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>Enables string quoting syntax like <code>q'[str]'</code>, as used in
PL/SQL.</p>
</dd><dt id="user-content-sqldialectspec.operatorchars">
  <code><strong><a href="#user-content-sqldialectspec.operatorchars">operatorChars</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a></code></dt>

<dd><p>The set of characters that make up operators. Defaults to
<code>&quot;*+\-%&lt;&gt;!=&amp;|~^/&quot;</code>.</p>
</dd><dt id="user-content-sqldialectspec.specialvar">
  <code><strong><a href="#user-content-sqldialectspec.specialvar">specialVar</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a></code></dt>

<dd><p>The set of characters that start a special variable name.
Defaults to <code>&quot;?&quot;</code>.</p>
</dd><dt id="user-content-sqldialectspec.identifierquotes">
  <code><strong><a href="#user-content-sqldialectspec.identifierquotes">identifierQuotes</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a></code></dt>

<dd><p>The characters that can be used to quote identifiers. Defaults
to <code>&quot;\&quot;&quot;</code>. Add <code>[</code> for MSSQL-style bracket quoted identifiers.</p>
</dd><dt id="user-content-sqldialectspec.caseinsensitiveidentifiers">
  <code><strong><a href="#user-content-sqldialectspec.caseinsensitiveidentifiers">caseInsensitiveIdentifiers</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>Controls whether identifiers are case-insensitive. Identifiers
with upper-case letters are quoted when set to false (which is
the default).</p>
</dd><dt id="user-content-sqldialectspec.unquotedbitliterals">
  <code><strong><a href="#user-content-sqldialectspec.unquotedbitliterals">unquotedBitLiterals</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>Controls whether bit values can be defined as 0b1010. Defaults
to false.</p>
</dd><dt id="user-content-sqldialectspec.treatbitsasbytes">
  <code><strong><a href="#user-content-sqldialectspec.treatbitsasbytes">treatBitsAsBytes</a></strong>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></code></dt>

<dd><p>Controls whether bit values can contain other characters than 0 and 1.
Defaults to false.</p>
</dd></dl>

</dd>
<dt id="user-content-standardsql">
  <code><strong><a href="#user-content-standardsql">StandardSQL</a></strong>: <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p>The standard SQL dialect.</p>
</dd>
<dt id="user-content-postgresql">
  <code><strong><a href="#user-content-postgresql">PostgreSQL</a></strong>: <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p>Dialect for <a href="https://www.postgresql.org">PostgreSQL</a>.</p>
</dd>
<dt id="user-content-mysql">
  <code><strong><a href="#user-content-mysql">MySQL</a></strong>: <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p><a href="https://dev.mysql.com/">MySQL</a> dialect.</p>
</dd>
<dt id="user-content-mariasql">
  <code><strong><a href="#user-content-mariasql">MariaSQL</a></strong>: <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p>Variant of <a href="#user-content-mysql"><code>MySQL</code></a> for
<a href="https://mariadb.org/">MariaDB</a>.</p>
</dd>
<dt id="user-content-mssql">
  <code><strong><a href="#user-content-mssql">MSSQL</a></strong>: <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p>SQL dialect for Microsoft <a href="https://www.microsoft.com/en-us/sql-server">SQL
Server</a>.</p>
</dd>
<dt id="user-content-sqlite">
  <code><strong><a href="#user-content-sqlite">SQLite</a></strong>: <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p><a href="https://sqlite.org/">SQLite</a> dialect.</p>
</dd>
<dt id="user-content-cassandra">
  <code><strong><a href="#user-content-cassandra">Cassandra</a></strong>: <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p>Dialect for <a href="https://cassandra.apache.org/">Cassandra</a>'s SQL-ish query language.</p>
</dd>
<dt id="user-content-plsql">
  <code><strong><a href="#user-content-plsql">PLSQL</a></strong>: <a href="#user-content-sqldialect">SQLDialect</a></code></dt>

<dd><p><a href="https://en.wikipedia.org/wiki/PL/SQL">PL/SQL</a> dialect.</p>
</dd>
<dt id="user-content-keywordcompletionsource">
  <code><strong><a href="#user-content-keywordcompletionsource">keywordCompletionSource</a></strong>(<a id="user-content-keywordcompletionsource^dialect" href="#user-content-keywordcompletionsource^dialect">dialect</a>: <a href="#user-content-sqldialect">SQLDialect</a>, <a id="user-content-keywordcompletionsource^uppercase" href="#user-content-keywordcompletionsource^uppercase">upperCase</a>&#8288;?: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a> = false, <a id="user-content-keywordcompletionsource^build" href="#user-content-keywordcompletionsource^build">build</a>&#8288;?: fn(<a id="user-content-keywordcompletionsource^build^label" href="#user-content-keywordcompletionsource^build^label">label</a>: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a>, <a id="user-content-keywordcompletionsource^build^type" href="#user-content-keywordcompletionsource^build^type">type</a>: <a href="https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/String">string</a>) → <a href="https://codemirror.net/brain/knowledge/docs_legacy/ref#autocomplete.Completion">Completion</a>) → <a href="https://codemirror.net/brain/knowledge/docs_legacy/ref#autocomplete.CompletionSource">CompletionSource</a></code></dt>

<dd><p>Returns a completion source that provides keyword completion for
the given SQL dialect.</p>
</dd>
<dt id="user-content-schemacompletionsource">
  <code><strong><a href="#user-content-schemacompletionsource">schemaCompletionSource</a></strong>(<a id="user-content-schemacompletionsource^config" href="#user-content-schemacompletionsource^config">config</a>: <a href="#user-content-sqlconfig">SQLConfig</a>) → <a href="https://codemirror.net/brain/knowledge/docs_legacy/ref#autocomplete.CompletionSource">CompletionSource</a></code></dt>

<dd><p>Returns a completion sources that provides schema-based completion
for the given configuration.</p>
</dd>
</dl>
```

## File: `package.json`
```json
{
  "name": "@codemirror/lang-sql",
  "version": "6.10.0",
  "description": "SQL language support for the CodeMirror code editor",
  "scripts": {
    "test": "cm-runtests",
    "prepare": "cm-buildhelper src/sql.ts"
  },
  "keywords": [
    "editor",
    "code"
  ],
  "author": {
    "name": "Marijn Haverbeke",
    "email": "marijn@haverbeke.berlin",
    "url": "http://marijnhaverbeke.nl"
  },
  "type": "module",
  "main": "dist/index.cjs",
  "exports": {
    "import": "./dist/index.js",
    "require": "./dist/index.cjs"
  },
  "types": "dist/index.d.ts",
  "module": "dist/index.js",
  "sideEffects": false,
  "license": "MIT",
  "dependencies": {
    "@codemirror/autocomplete": "^6.0.0",
    "@lezer/common": "^1.2.0",
    "@lezer/highlight": "^1.0.0",
    "@codemirror/language": "^6.0.0",
    "@codemirror/state": "^6.0.0",
    "@lezer/lr": "^1.0.0"
  },
  "devDependencies": {
    "@codemirror/buildhelper": "^1.0.0"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/codemirror/lang-sql.git"
  }
}
```

## File: `src/README.md`
```markdown
<!-- NOTE: README.md is generated from src/README.md -->

# @codemirror/lang-sql [![NPM version](https://img.shields.io/npm/v/@codemirror/lang-sql.svg)](https://www.npmjs.org/package/@codemirror/lang-sql)

[ [**WEBSITE**](https://codemirror.net/) | [**ISSUES**](https://github.com/codemirror/dev/issues) | [**FORUM**](https://discuss.codemirror.net/c/next/) | [**CHANGELOG**](https://github.com/codemirror/lang-sql/blob/main/CHANGELOG.md) ]

This package implements SQL language support for the
[CodeMirror](https://codemirror.net/) code editor.

The [project page](https://codemirror.net/) has more information, a
number of [examples](https://codemirror.net/examples/) and the
[documentation](https://codemirror.net/brain/knowledge/docs_legacy/).

This code is released under an
[MIT license](https://github.com/codemirror/lang-sql/tree/main/LICENSE).

We aim to be an inclusive, welcoming community. To make that explicit,
we have a [code of
conduct](http://contributor-covenant.org/version/1/1/0/) that applies
to communication around the project.

## Usage

```javascript
import {EditorView, basicSetup} from "codemirror"
import {sql} from "@codemirror/lang-sql"

const view = new EditorView({
  parent: document.body,
  doc: `select * from users where age > 20`,
  extensions: [basicSetup, sql()]
})
```

Use `sql({dialect: PostgreSQL})` or similar to select a specific SQL
dialect.

## API Reference

@sql

@SQLConfig

@SQLNamespace

@SQLDialect

@SQLDialectSpec

@StandardSQL
@PostgreSQL
@MySQL
@MariaSQL
@MSSQL
@SQLite
@Cassandra
@PLSQL

@keywordCompletionSource
@schemaCompletionSource
```

## File: `src/complete.ts`
```typescript
import {Completion, CompletionContext, CompletionSource, completeFromList, ifNotIn} from "@codemirror/autocomplete"
import {EditorState, Text} from "@codemirror/state"
import {syntaxTree} from "@codemirror/language"
import {SyntaxNode} from "@lezer/common"
import {Type, Keyword} from "./sql.grammar.terms"
import {type SQLDialect, SQLNamespace} from "./sql"

function tokenBefore(tree: SyntaxNode) {
  let cursor = tree.cursor().moveTo(tree.from, -1)
  while (/Comment/.test(cursor.name)) cursor.moveTo(cursor.from, -1)
  return cursor.node
}

function idName(doc: Text, node: SyntaxNode): string {
  let text = doc.sliceString(node.from, node.to)
  let quoted = /^([`'"\[])(.*)([`'"\]])$/.exec(text)
  return quoted ? quoted[2] : text
}

function plainID(node: SyntaxNode | null) {
  return node && (node.name == "Identifier" || node.name == "QuotedIdentifier")
}

function pathFor(doc: Text, id: SyntaxNode) {
  if (id.name == "CompositeIdentifier") {
    let path = []
    for (let ch = id.firstChild; ch; ch = ch.nextSibling)
      if (plainID(ch)) path.push(idName(doc, ch))
    return path
  }
  return [idName(doc, id)]
}

function parentsFor(doc: Text, node: SyntaxNode | null) {
  for (let path = [];;) {
    if (!node || node.name != ".") return path
    let name = tokenBefore(node)
    if (!plainID(name)) return path
    path.unshift(idName(doc, name))
    node = tokenBefore(name)
  }
}

function sourceContext(state: EditorState, startPos: number) {
  let pos = syntaxTree(state).resolveInner(startPos, -1)
  let aliases = getAliases(state.doc, pos)
  if (pos.name == "Identifier" || pos.name == "QuotedIdentifier" || pos.name == "Keyword") {
    return {from: pos.from,
            quoted: pos.name == "QuotedIdentifier" ? state.doc.sliceString(pos.from, pos.from + 1) : null,
            parents: parentsFor(state.doc, tokenBefore(pos)),
            aliases}
  } if (pos.name == ".") {
    return {from: startPos, quoted: null, parents: parentsFor(state.doc, pos), aliases}
  } else {
    return {from: startPos, quoted: null, parents: [], empty: true, aliases}
  }
}

const EndFrom = new Set("where group having order union intersect except all distinct limit offset fetch for".split(" "))

function getAliases(doc: Text, at: SyntaxNode) {
  let statement
  for (let parent: SyntaxNode | null = at; !statement; parent = parent.parent) {
    if (!parent) return null
    if (parent.name == "Statement") statement = parent
  }
  let aliases = null
  for (let scan = statement.firstChild, sawFrom = false, prevID: SyntaxNode | null = null; scan; scan = scan.nextSibling) {
    let kw = scan.name == "Keyword" ? doc.sliceString(scan.from, scan.to).toLowerCase() : null
    let alias = null
    if (!sawFrom) {
      sawFrom = kw == "from"
    } else if (kw == "as" && prevID && plainID(scan.nextSibling)) {
      alias = idName(doc, scan.nextSibling!)
    } else if (kw && EndFrom.has(kw)) {
      break
    } else if (prevID && plainID(scan)) {
      alias = idName(doc, scan)
    }
    if (alias) {
      if (!aliases) aliases = Object.create(null)
      aliases[alias] = pathFor(doc, prevID!)
    }
    prevID = /Identifier$/.test(scan.name) ? scan : null
  }
  return aliases
}

function maybeQuoteCompletions(openingQuote: string, closingQuote: string, completions: readonly Completion[]) {
  return completions.map(c => ({...c, label: c.label[0] == openingQuote ? c.label : openingQuote + c.label + closingQuote, apply: undefined}))
}

const Span = /^\w*$/, QuotedSpan = /^[`'"\[]?\w*[`'"\]]?$/

function isSelfTag(namespace: SQLNamespace): namespace is {self: Completion, children: SQLNamespace} {
  return (namespace as any).self && typeof (namespace as any).self.label == "string"
}

class CompletionLevel {
  list: Completion[] = []
  children: {[name: string]: CompletionLevel} | undefined = undefined

  constructor(readonly idQuote: string, readonly idCaseInsensitive: boolean) {}

  child(name: string) {
    let children = this.children || (this.children = Object.create(null))
    let found = children[name]
    if (found) return found
    if (name && !this.list.some(c => c.label == name)) this.list.push(nameCompletion(name, "type", this.idQuote, this.idCaseInsensitive))
    return (children[name] = new CompletionLevel(this.idQuote, this.idCaseInsensitive))
  }

  maybeChild(name: string) {
    return this.children ? this.children[name] : null
  }    

  addCompletion(option: Completion) {
    let found = this.list.findIndex(o => o.label == option.label)
    if (found > -1) this.list[found] = option
    else this.list.push(option)
  }

  addCompletions(completions: readonly (Completion | string)[]) {
    for (let option of completions)
      this.addCompletion(typeof option == "string" ? nameCompletion(option, "property", this.idQuote, this.idCaseInsensitive) : option)
  }

  addNamespace(namespace: SQLNamespace) {
    if (Array.isArray(namespace)) {
      this.addCompletions(namespace)
    } else if (isSelfTag(namespace)) {
      this.addNamespace(namespace.children)
    } else {
      this.addNamespaceObject(namespace as {[name: string]: SQLNamespace})
    }
  }

  addNamespaceObject(namespace: {[name: string]: SQLNamespace}) {
    for (let name of Object.keys(namespace)) {
      let children = namespace[name], self: Completion | null = null
      let parts = name.replace(/\\?\./g, p => p == "." ? "\0" : p).split("\0")
      let scope = this
      if (isSelfTag(children)) {
        self = children.self
        children = children.children
      }
      for (let i = 0; i < parts.length; i++) {
        if (self && i == parts.length - 1) scope.addCompletion(self)
        scope = scope.child(parts[i].replace(/\\\./g, "."))
      }
      scope.addNamespace(children)
    }
  }
}

function nameCompletion(label: string, type: string, idQuote: string, idCaseInsensitive: boolean): Completion {
  if ((new RegExp("^[a-z_][a-z_\\d]*$", idCaseInsensitive ? "i" : "")).test(label)) return {label, type}

  return {label, type, apply: idQuote + label + getClosingQuote(idQuote)}
}

function getClosingQuote(openingQuote: string) {
  return openingQuote === "[" ? "]" : openingQuote
}

// Some of this is more gnarly than it has to be because we're also
// supporting the deprecated, not-so-well-considered style of
// supplying the schema (dotted property names for schemas, separate
// `tables` and `schemas` completions).
export function completeFromSchema(schema: SQLNamespace,
                                   tables?: readonly Completion[], schemas?: readonly Completion[],
                                   defaultTableName?: string, defaultSchemaName?: string,
                                   dialect?: SQLDialect): CompletionSource {
  let idQuote = dialect?.spec.identifierQuotes?.[0] || '"'
  let top = new CompletionLevel(idQuote, !!dialect?.spec.caseInsensitiveIdentifiers)
  let defaultSchema = defaultSchemaName ? top.child(defaultSchemaName) : null
  top.addNamespace(schema)
  if (tables) (defaultSchema || top).addCompletions(tables)
  if (schemas) top.addCompletions(schemas)
  if (defaultSchema) top.addCompletions(defaultSchema.list)
  if (defaultTableName) top.addCompletions((defaultSchema || top).child(defaultTableName).list)

  return (context: CompletionContext) => {
    let {parents, from, quoted, empty, aliases} = sourceContext(context.state, context.pos)
    if (empty && !context.explicit) return null
    if (aliases && parents.length == 1) parents = aliases[parents[0]] || parents
    let level = top
    for (let name of parents) {
      while (!level.children || !level.children[name]) {
        if (level == top && defaultSchema) level = defaultSchema
        else if (level == defaultSchema && defaultTableName) level = level.child(defaultTableName)
        else return null
      }
      let next = level.maybeChild(name)
      if (!next) return null
      level = next
    }

    let options = level.list
    if (level == top && aliases)
      options = options.concat(Object.keys(aliases).map(name => ({label: name, type: "constant"})))

    if (quoted) {
      let openingQuote = quoted[0]
      let closingQuote = getClosingQuote(openingQuote)

      let quoteAfter = context.state.sliceDoc(context.pos, context.pos + 1) == closingQuote

      return {
        from,
        to: quoteAfter ? context.pos + 1 : undefined,
        options: maybeQuoteCompletions(openingQuote, closingQuote, options),
        validFor: QuotedSpan,
      }
    } else {
      return {
        from,
        options: options,
        validFor: Span
      }
    }
  }
}

function completionType(tokenType: number) {
  return tokenType == Type ? "type" : tokenType == Keyword ? "keyword" : "variable"
}

export function completeKeywords(keywords: {[name: string]: number}, upperCase: boolean,
                                 build: (name: string, type: string) => Completion) {
  let completions =  Object.keys(keywords)
    .map(keyword => build(upperCase ? keyword.toUpperCase() : keyword, completionType(keywords[keyword])))
  return ifNotIn(["QuotedIdentifier", "String", "LineComment", "BlockComment", "."],
                 completeFromList(completions))
}
```

## File: `src/sql.grammar`
```
@precedence { dot }

@top Script {
  Statement { element* Semi }*
  Statement { element+ }?
}

@skip { whitespace | LineComment | BlockComment }

element {
  String |
  Number |
  Bool |
  Null |
  Identifier |
  QuotedIdentifier |
  Bits |
  Bytes |
  Builtin |
  SpecialVar |
  CompositeIdentifier {
    Dot? (QuotedIdentifier | Identifier | SpecialVar) (!dot Dot (QuotedIdentifier | Identifier | SpecialVar))+
  } |
  Keyword |
  Type |
  Operator |
  Punctuation |
  Parens { ParenL element* ParenR } |
  Braces { BraceL element* BraceR } |
  Brackets { BracketL element* BracketR }
}

@external tokens tokens from "./tokens" {
  whitespace
  LineComment[isolate]
  BlockComment[isolate]
  String[isolate]
  Number
  Bool
  Null
  ParenL[@name="("]
  ParenR[@name=")"]
  BraceL[@name="{"]
  BraceR[@name="}"]
  BracketL[@name="["]
  BracketR[@name="]"]
  Semi[@name=";"]
  Dot[@name="."]
  Operator
  Punctuation
  SpecialVar
  Identifier
  QuotedIdentifier[isolate]
  Keyword
  Type
  Bits
  Bytes
  Builtin
}

@detectDelim
```

## File: `src/sql.grammar.d.ts`
```typescript
import {LRParser} from "@lezer/lr"
export declare const parser: LRParser
```

## File: `src/sql.grammar.terms.d.ts`
```typescript
export const whitespace: number, LineComment: number, BlockComment: number,
  String: number, Number: number, Bool: number, Null: number,
  ParenL: number, ParenR: number, BraceL: number, BraceR: number, BracketL: number, BracketR: number, Semi: number, Dot: number,
  Operator: number, Punctuation: number, SpecialVar: number, Identifier: number, QuotedIdentifier: number,
  Keyword: number, Type: number, Builtin: number, Bits: number, Bytes: number
```

## File: `src/sql.ts`
```typescript
import {continuedIndent, indentNodeProp, foldNodeProp, LRLanguage, LanguageSupport} from "@codemirror/language"
import {Extension} from "@codemirror/state"
import {Completion, CompletionSource} from "@codemirror/autocomplete"
import {styleTags, tags as t} from "@lezer/highlight"
import {ParserConfig} from "@lezer/lr"
import {parser as baseParser} from "./sql.grammar"
import {tokens, Dialect, tokensFor, SQLKeywords, SQLTypes, dialect} from "./tokens"
import {completeFromSchema, completeKeywords} from "./complete"

let parser = baseParser.configure({
  props: [
    indentNodeProp.add({
      Statement: continuedIndent()
    }),
    foldNodeProp.add({
      Statement(tree, state) { return {from: Math.min(tree.from + 100, state.doc.lineAt(tree.from).to), to: tree.to} },
      BlockComment(tree) { return {from: tree.from + 2, to: tree.to - 2} }
    }),
    styleTags({
      Keyword: t.keyword,
      Type: t.typeName,
      Builtin: t.standard(t.name),
      Bits: t.number,
      Bytes: t.string,
      Bool: t.bool,
      Null: t.null,
      Number: t.number,
      String: t.string,
      Identifier: t.name,
      QuotedIdentifier: t.special(t.string),
      SpecialVar: t.special(t.name),
      LineComment: t.lineComment,
      BlockComment: t.blockComment,
      Operator: t.operator,
      "Semi Punctuation": t.punctuation,
      "( )": t.paren,
      "{ }": t.brace,
      "[ ]": t.squareBracket
    })
  ]
})

/// Configuration for an [SQL Dialect](#lang-sql.SQLDialect).
export type SQLDialectSpec = {
  /// A space-separated list of keywords for the dialect.
  keywords?: string,
  /// A space-separated string of built-in identifiers for the dialect.
  builtin?: string,
  /// A space-separated string of type names for the dialect.
  types?: string,
  /// Controls whether regular strings allow backslash escapes.
  backslashEscapes?: boolean,
  /// Controls whether # creates a line comment.
  hashComments?: boolean,
  /// Controls whether `//` creates a line comment.
  slashComments?: boolean,
  /// When enabled `--` comments are only recognized when there's a
  /// space after the dashes.
  spaceAfterDashes?: boolean,
  /// When enabled, things quoted with "$$" are treated as
  /// strings, rather than identifiers.
  doubleDollarQuotedStrings?: boolean,
  /// When enabled, things quoted with double quotes are treated as
  /// strings, rather than identifiers.
  doubleQuotedStrings?: boolean,
  /// Enables strings like `_utf8'str'` or `N'str'`.
  charSetCasts?: boolean,
  /// Enables string quoting syntax like `q'[str]'`, as used in
  /// PL/SQL.
  plsqlQuotingMechanism?: boolean,
  /// The set of characters that make up operators. Defaults to
  /// `"*+\-%<>!=&|~^/"`.
  operatorChars?: string,
  /// The set of characters that start a special variable name.
  /// Defaults to `"?"`.
  specialVar?: string,
  /// The characters that can be used to quote identifiers. Defaults
  /// to `"\""`. Add `[` for MSSQL-style bracket quoted identifiers.
  identifierQuotes?: string
  /// Controls whether identifiers are case-insensitive. Identifiers
  /// with upper-case letters are quoted when set to false (which is
  /// the default).
  caseInsensitiveIdentifiers?: boolean,
  /// Controls whether bit values can be defined as 0b1010. Defaults
  /// to false.
  unquotedBitLiterals?: boolean,
  /// Controls whether bit values can contain other characters than 0 and 1.
  /// Defaults to false.
  treatBitsAsBytes?: boolean,
}

/// Represents an SQL dialect.
export class SQLDialect {
  private constructor(
    /// @internal
    readonly dialect: Dialect,
    /// The language for this dialect.
    readonly language: LRLanguage,
    /// The spec used to define this dialect.
    readonly spec: SQLDialectSpec
  ) {}

  /// Returns the language for this dialect as an extension.
  get extension() { return this.language.extension }

  /// Reconfigure the parser used by this dialect. Returns a new
  /// dialect object.
  configureLanguage(options: ParserConfig, name?: string) {
    return new SQLDialect(this.dialect, this.language.configure(options, name), this.spec)
  }

  /// Define a new dialect.
  static define(spec: SQLDialectSpec) {
    let d = dialect(spec, spec.keywords, spec.types, spec.builtin)
    let language = LRLanguage.define({
      name: "sql",
      parser: parser.configure({
        tokenizers: [{from: tokens, to: tokensFor(d)}]
      }),
      languageData: {
        commentTokens: {line: "--", block: {open: "/*", close: "*/"}},
        closeBrackets: {brackets: ["(", "[", "{", "'", '"', "`"]}
      }
    })
    return new SQLDialect(d, language, spec)
  }
}

/// The type used to describe a level of the schema for
/// [completion](#lang-sql.SQLConfig.schema). Can be an array of
/// options (columns), an object mapping table or schema names to
/// deeper levels, or a `{self, children}` object that assigns a
/// completion option to use for its parent property, when the default option
/// (its name as label and type `"type"`) isn't suitable.
export type SQLNamespace = {[name: string]: SQLNamespace}
  | {self: Completion, children: SQLNamespace}
  | readonly (Completion | string)[]

/// Options used to configure an SQL extension.
export interface SQLConfig {
  /// The [dialect](#lang-sql.SQLDialect) to use. Defaults to
  /// [`StandardSQL`](#lang-sql.StandardSQL).
  dialect?: SQLDialect,
  /// You can use this to define the schemas, tables, and their fields
  /// for autocompletion.
  schema?: SQLNamespace,
  /// @hide
  tables?: readonly Completion[],
  /// @hide
  schemas?: readonly Completion[],
  /// When given, columns from the named table can be completed
  /// directly at the top level.
  defaultTable?: string,
  /// When given, tables prefixed with this schema name can be
  /// completed directly at the top level.
  defaultSchema?: string,
  /// When set to true, keyword completions will be upper-case.
  upperCaseKeywords?: boolean
  /// Can be used to customize the completions generated for keywords.
  keywordCompletion?: (label: string, type: string) => Completion
}

function defaultKeyword(label: string, type: string) { return {label, type, boost: -1} }

/// Returns a completion source that provides keyword completion for
/// the given SQL dialect.
export function keywordCompletionSource(dialect: SQLDialect, upperCase = false,
                                        build?: (label: string, type: string) => Completion): CompletionSource {
  return completeKeywords(dialect.dialect.words, upperCase, build || defaultKeyword)
}

/// Returns a completion sources that provides schema-based completion
/// for the given configuration.
export function schemaCompletionSource(config: SQLConfig): CompletionSource {
  return config.schema ? completeFromSchema(config.schema, config.tables, config.schemas,
                                            config.defaultTable, config.defaultSchema,
                                            config.dialect || StandardSQL)
    : () => null
}

function schemaCompletion(config: SQLConfig): Extension {
  return config.schema ? (config.dialect || StandardSQL).language.data.of({
    autocomplete: schemaCompletionSource(config)
  }) : []
}

/// SQL language support for the given SQL dialect, with keyword
/// completion, and, if provided, schema-based completion as extra
/// extensions.
export function sql(config: SQLConfig = {}) {
  let lang = config.dialect || StandardSQL
  return new LanguageSupport(lang.language, [
    schemaCompletion(config),
    lang.language.data.of({
      autocomplete: keywordCompletionSource(lang, config.upperCaseKeywords, config.keywordCompletion)
    })
  ])
}

/// The standard SQL dialect.
export const StandardSQL = SQLDialect.define({})

/// Dialect for [PostgreSQL](https://www.postgresql.org).
export const PostgreSQL = SQLDialect.define({
  charSetCasts: true,
  doubleDollarQuotedStrings: true,
  operatorChars: "+-*/<>=~!@#%^&|`?",
  specialVar: "",
  keywords: SQLKeywords + "abort abs absent access according ada admin aggregate alias also always analyse analyze array_agg array_max_cardinality asensitive assert assignment asymmetric atomic attach attribute attributes avg backward base64 begin_frame begin_partition bernoulli bit_length blocked bom cache called cardinality catalog_name ceil ceiling chain char_length character_length character_set_catalog character_set_name character_set_schema characteristics characters checkpoint class class_origin cluster coalesce cobol collation_catalog collation_name collation_schema collect column_name columns command_function command_function_code comment comments committed concurrently condition_number configuration conflict connection_name constant constraint_catalog constraint_name constraint_schema contains content control conversion convert copy corr cost covar_pop covar_samp csv cume_dist current_catalog current_row current_schema cursor_name database datalink datatype datetime_interval_code datetime_interval_precision db debug defaults defined definer degree delimiter delimiters dense_rank depends derived detach detail dictionary disable discard dispatch dlnewcopy dlpreviouscopy dlurlcomplete dlurlcompleteonly dlurlcompletewrite dlurlpath dlurlpathonly dlurlpathwrite dlurlscheme dlurlserver dlvalue document dump dynamic_function dynamic_function_code element elsif empty enable encoding encrypted end_frame end_partition endexec enforced enum errcode error event every exclude excluding exclusive exp explain expression extension extract family file filter final first_value flag floor following force foreach fortran forward frame_row freeze fs functions fusion generated granted greatest groups handler header hex hierarchy hint id ignore ilike immediately immutable implementation implicit import include including increment indent index indexes info inherit inherits inline insensitive instance instantiable instead integrity intersection invoker isnull key_member key_type label lag last_value lead leakproof least length library like_regex link listen ln load location lock locked log logged lower mapping matched materialized max max_cardinality maxvalue member merge message message_length message_octet_length message_text min minvalue mod mode more move multiset mumps name namespace nfc nfd nfkc nfkd nil normalize normalized nothing notice notify notnull nowait nth_value ntile nullable nullif nulls number occurrences_regex octet_length octets off offset oids operator options ordering others over overlay overriding owned owner parallel parameter_mode parameter_name parameter_ordinal_position parameter_specific_catalog parameter_specific_name parameter_specific_schema parser partition pascal passing passthrough password percent percent_rank percentile_cont percentile_disc perform period permission pg_context pg_datatype_name pg_exception_context pg_exception_detail pg_exception_hint placing plans pli policy portion position position_regex power precedes preceding prepared print_strict_params procedural procedures program publication query quote raise range rank reassign recheck recovery refresh regr_avgx regr_avgy regr_count regr_intercept regr_r2 regr_slope regr_sxx regr_sxy regr_syy reindex rename repeatable replace replica requiring reset respect restart restore result_oid returned_cardinality returned_length returned_octet_length returned_sqlstate returning reverse routine_catalog routine_name routine_schema routines row_count row_number rowtype rule scale schema_name schemas scope scope_catalog scope_name scope_schema security selective self sensitive sequence sequences serializable server server_name setof share show simple skip slice snapshot source specific_name sqlcode sqlerror sqrt stable stacked standalone statement statistics stddev_pop stddev_samp stdin stdout storage strict strip structure style subclass_origin submultiset subscription substring substring_regex succeeds sum symmetric sysid system system_time table_name tables tablesample tablespace temp template ties token top_level_count transaction_active transactions_committed transactions_rolled_back transform transforms translate translate_regex trigger_catalog trigger_name trigger_schema trim trim_array truncate trusted type types uescape unbounded uncommitted unencrypted unlink unlisten unlogged unnamed untyped upper uri use_column use_variable user_defined_type_catalog user_defined_type_code user_defined_type_name user_defined_type_schema vacuum valid validate validator value_of var_pop var_samp varbinary variable_conflict variadic verbose version versioning views volatile warning whitespace width_bucket window within wrapper xmlagg xmlattributes xmlbinary xmlcast xmlcomment xmlconcat xmldeclaration xmldocument xmlelement xmlexists xmlforest xmliterate xmlnamespaces xmlparse xmlpi xmlquery xmlroot xmlschema xmlserialize xmltable xmltext xmlvalidate yes",
  types: SQLTypes + "bigint int8 bigserial serial8 varbit bool box bytea cidr circle precision float8 inet int4 json jsonb line lseg macaddr macaddr8 money numeric pg_lsn point polygon float4 int2 smallserial serial2 serial serial4 text timetz timestamptz tsquery tsvector txid_snapshot uuid xml"
})

const MySQLKeywords = "accessible algorithm analyze asensitive authors auto_increment autocommit avg avg_row_length binlog btree cache catalog_name chain change changed checkpoint checksum class_origin client_statistics coalesce code collations columns comment committed completion concurrent consistent contains contributors convert database databases day_hour day_microsecond day_minute day_second delay_key_write delayed delimiter des_key_file dev_pop dev_samp deviance directory disable discard distinctrow div dual dumpfile enable enclosed ends engine engines enum errors escaped even event events every explain extended fast field fields flush force found_rows fulltext grants handler hash high_priority hosts hour_microsecond hour_minute hour_second ignore ignore_server_ids import index index_statistics infile innodb insensitive insert_method install invoker iterate keys kill linear lines list load lock logs low_priority master master_heartbeat_period master_ssl_verify_server_cert masters max max_rows maxvalue message_text middleint migrate min min_rows minute_microsecond minute_second mod mode modify mutex mysql_errno no_write_to_binlog offline offset one online optimize optionally outfile pack_keys parser partition partitions password phase plugin plugins prev processlist profile profiles purge query quick range read_write rebuild recover regexp relaylog remove rename reorganize repair repeatable replace require resume rlike row_format rtree schedule schema_name schemas second_microsecond security sensitive separator serializable server share show slave slow snapshot soname spatial sql_big_result sql_buffer_result sql_cache sql_calc_found_rows sql_no_cache sql_small_result ssl starting starts std stddev stddev_pop stddev_samp storage straight_join subclass_origin sum suspend table_name table_statistics tables tablespace terminated triggers truncate uncommitted uninstall unlock upgrade use use_frm user_resources user_statistics utc_date utc_time utc_timestamp variables views warnings xa xor year_month zerofill"

const MySQLTypes = SQLTypes + "bool blob long longblob longtext medium mediumblob mediumint mediumtext tinyblob tinyint tinytext text bigint int1 int2 int3 int4 int8 float4 float8 varbinary varcharacter precision datetime unsigned signed"

const MySQLBuiltin = "charset clear edit ego help nopager notee nowarning pager print prompt quit rehash source status system tee"

/// [MySQL](https://dev.mysql.com/) dialect.
export const MySQL = SQLDialect.define({
  operatorChars: "*+-%<>!=&|^",
  charSetCasts: true,
  doubleQuotedStrings: true,
  unquotedBitLiterals: true,
  hashComments: true,
  spaceAfterDashes: true,
  specialVar: "@?",
  identifierQuotes: "`",
  keywords: SQLKeywords + "group_concat " + MySQLKeywords,
  types: MySQLTypes,
  builtin: MySQLBuiltin
})

/// Variant of [`MySQL`](#lang-sql.MySQL) for
/// [MariaDB](https://mariadb.org/).
export const MariaSQL = SQLDialect.define({
  operatorChars: "*+-%<>!=&|^",
  charSetCasts: true,
  doubleQuotedStrings: true,
  unquotedBitLiterals: true,
  hashComments: true,
  spaceAfterDashes: true,
  specialVar: "@?",
  identifierQuotes: "`",
  keywords: SQLKeywords + "always generated groupby_concat hard persistent shutdown soft virtual " + MySQLKeywords,
  types: MySQLTypes,
  builtin: MySQLBuiltin
})

let MSSQLBuiltin =
  // Aggregate https://msdn.microsoft.com/en-us/library/ms173454.aspx
  "approx_count_distinct approx_percentile_cont approx_percentile_disc avg checksum_agg count count_big grouping grouping_id max min product stdev stdevp sum var varp " +
  // AI https://learn.microsoft.com/en-us/sql/t-sql/functions/ai-functions-transact-sql?view=sql-server-ver17
  "ai_generate_embeddings ai_generate_chunks " +
  // Analytic https://learn.microsoft.com/en-us/sql/t-sql/functions/analytic-functions-transact-sql?view=sql-server-ver17
  "cume_dist first_value lag last_value lead percentile_cont percentile_disc percent_rank " +
  // Bit Manipulation https://learn.microsoft.com/en-us/sql/t-sql/functions/bit-manipulation-functions-overview?view=sql-server-ver17
  "left_shift right_shift bit_count get_bit set_bit " +
  // Collation Functions https://learn.microsoft.com/en-us/sql/t-sql/functions/collation-functions-collationproperty-transact-sql?view=sql-server-ver17
  "collationproperty tertiary_weights " +
  // Configuration https://learn.microsoft.com/en-us/sql/t-sql/functions/configuration-functions-transact-sql?view=sql-server-ver17
  "@@datefirst @@dbts @@langid @@language @@lock_timeout @@max_connections @@max_precision @@nestlevel @@options @@remserver @@servername @@servicename @@spid @@textsize @@version " +
  // Conversion https://learn.microsoft.com/en-us/sql/t-sql/functions/conversion-functions-transact-sql?view=sql-server-ver17
  "cast convert parse try_cast try_convert try_parse " +
  // Cryptographic https://learn.microsoft.com/en-us/sql/t-sql/functions/cryptographic-functions-transact-sql?view=sql-server-ver17
  "asymkey_id asymkeyproperty certproperty cert_id crypt_gen_random decryptbyasymkey decryptbycert decryptbykey decryptbykeyautoasymkey decryptbykeyautocert decryptbypassphrase encryptbyasymkey encryptbycert encryptbykey encryptbypassphrase hashbytes is_objectsigned key_guid key_id key_name signbyasymkey signbycert symkeyproperty verifysignedbycert verifysignedbyasymkey " +
  // Cursor https://learn.microsoft.com/en-us/sql/t-sql/functions/cursor-functions-transact-sql?view=sql-server-ver17
  "@@cursor_rows @@fetch_status cursor_status " +
  // Data type https://learn.microsoft.com/en-us/sql/t-sql/functions/data-type-functions-transact-sql?view=sql-server-ver17
  "datalength ident_current ident_incr ident_seed identity sql_variant_property " +
  // Date & time https://learn.microsoft.com/en-us/sql/t-sql/functions/date-and-time-data-types-and-functions-transact-sql?view=sql-server-ver17
  "@@datefirst current_timestamp current_timezone current_timezone_id date_bucket dateadd datediff datediff_big datefromparts datename datepart datetime2fromparts datetimefromparts datetimeoffsetfromparts datetrunc day eomonth getdate getutcdate isdate month smalldatetimefromparts switchoffset sysdatetime sysdatetimeoffset sysutcdatetime timefromparts todatetimeoffset year " +
  // Fuzzy string match https://learn.microsoft.com/en-us/sql/t-sql/functions/edit-distance-transact-sql?view=sql-server-ver17
  "edit_distance edit_distance_similarity jaro_winkler_distance jaro_winkler_similarity " +
  // Graph https://learn.microsoft.com/en-us/sql/t-sql/functions/graph-functions-transact-sql?view=sql-server-ver17
  "edge_id_from_parts graph_id_from_edge_id graph_id_from_node_id node_id_from_parts object_id_from_edge_id object_id_from_node_id " +
  // JSON https://learn.microsoft.com/en-us/sql/t-sql/functions/json-functions-transact-sql?view=sql-server-ver17
  "json isjson json_array json_contains json_modify json_object json_path_exists json_query json_value " +
  // Regular Expressions https://learn.microsoft.com/en-us/sql/t-sql/functions/regular-expressions-functions-transact-sql?view=sql-server-ver17
  "regexp_like regexp_replace regexp_substr regexp_instr regexp_count regexp_matches regexp_split_to_table " +
  // Mathematical https://learn.microsoft.com/en-us/sql/t-sql/functions/mathematical-functions-transact-sql?view=sql-server-ver17
  "abs acos asin atan atn2 ceiling cos cot degrees exp floor log log10 pi power radians rand round sign sin sqrt square tan " +
  // Logical https://learn.microsoft.com/en-us/sql/t-sql/functions/logical-functions-choose-transact-sql?view=sql-server-ver17
  "choose greatest iif least " +
  // Metadata https://learn.microsoft.com/en-us/sql/t-sql/functions/metadata-functions-transact-sql?view=sql-server-ver17
  "@@procid app_name applock_mode applock_test assemblyproperty col_length col_name columnproperty databasepropertyex db_id db_name file_id file_idex file_name filegroup_id filegroup_name filegroupproperty fileproperty filepropertyex fulltextcatalogproperty fulltextserviceproperty index_col indexkey_property indexproperty next value for object_definition object_id object_name object_schema_name objectproperty objectpropertyex original_db_name parsename schema_id schema_name scope_identity serverproperty stats_date type_id type_name typeproperty " +
  // Ranking https://learn.microsoft.com/en-us/sql/t-sql/functions/ranking-functions-transact-sql?view=sql-server-ver17
  "dense_rank ntile rank row_number " +
  // Replication https://learn.microsoft.com/en-us/sql/t-sql/functions/replication-functions-publishingservername?view=sql-server-ver17
  "publishingservername " +
  // Security https://learn.microsoft.com/en-us/sql/t-sql/functions/security-functions-transact-sql?view=sql-server-ver17
  "certenclosed certprivatekey current_user database_principal_id has_dbaccess has_perms_by_name is_member is_rolemember is_srvrolemember loginproperty original_login permissions pwdencrypt pwdcompare session_user sessionproperty suser_id suser_name suser_sid suser_sname system_user user user_id user_name " +
  // String https://learn.microsoft.com/en-us/sql/t-sql/functions/string-functions-transact-sql?view=sql-server-ver17
  "ascii char charindex concat concat_ws difference format left len lower ltrim nchar patindex quotename replace replicate reverse right rtrim soundex space str string_agg string_escape stuff substring translate trim unicode upper " +
  // System https://learn.microsoft.com/en-us/sql/t-sql/functions/system-functions-transact-sql?view=sql-server-ver17
  "$partition @@error @@identity @@pack_received @@rowcount @@trancount binary_checksum checksum compress connectionproperty context_info current_request_id current_transaction_id decompress error_line error_message error_number error_procedure error_severity error_state formatmessage get_filestream_transaction_context getansinull host_id host_name isnull isnumeric min_active_rowversion newid newsequentialid rowcount_big session_context xact_state " +
  // System Statistical https://learn.microsoft.com/en-us/sql/t-sql/functions/system-statistical-functions-transact-sql?view=sql-server-ver17
  "@@connections @@cpu_busy @@idle @@io_busy @@pack_sent @@packet_errors @@timeticks @@total_errors @@total_read @@total_write " +
  // Text & Image https://learn.microsoft.com/en-us/sql/t-sql/functions/text-and-image-functions-textptr-transact-sql?view=sql-server-ver17
  "textptr textvalid " +
  // Trigger https://learn.microsoft.com/en-us/sql/t-sql/functions/trigger-functions-transact-sql?view=sql-server-ver17
  "columns_updated eventdata trigger_nestlevel " +
  // Vectors https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-functions-transact-sql?view=sql-server-ver17
  "vector_distance vectorproperty vector_search " +
  // Relational operators https://msdn.microsoft.com/en-us/library/ms187957.aspx
  "generate_series opendatasource openjson openquery openrowset openxml predict string_split " +
  // Other
  "coalesce nullif apply catch filter force include keep keepfixed modify optimize parameterization parameters partition recompile sequence set"

/// SQL dialect for Microsoft [SQL
/// Server](https://www.microsoft.com/en-us/sql-server).
export const MSSQL = SQLDialect.define({
  keywords: SQLKeywords + 
    // Reserved Keywords https://learn.microsoft.com/en-us/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-ver17
    "add external procedure all fetch public alter file raiserror and fillfactor read any for readtext as foreign reconfigure asc freetext references authorization freetexttable replication backup from restore begin full restrict between function return break goto revert browse grant revoke bulk group right by having rollback cascade holdlock rowcount case identity rowguidcol check identity_insert rule checkpoint identitycol save close if schema clustered in securityaudit coalesce index select collate inner semantickeyphrasetable column insert semanticsimilaritydetailstable commit intersect semanticsimilaritytable compute into session_user constraint is set contains join setuser containstable key shutdown continue kill some convert left statistics create like system_user cross lineno table current load tablesample current_date merge textsize current_time national then current_timestamp nocheck to current_user nonclustered top cursor not tran database null transaction dbcc nullif trigger deallocate of truncate declare off try_convert default offsets tsequal delete on union deny open unique desc opendatasource unpivot disk openquery update distinct openrowset updatetext distributed openxml use double option user drop or values dump order varying else outer view end over waitfor errlvl percent when escape pivot where except plan while exec precision with execute primary within group exists print writetext exit proc " +
    // table hints https://learn.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql-table?view=sql-server-ver17
    "noexpand index forceseek forcescan holdlock nolock nowait paglock readcommitted readcommittedlock readpast readuncommitted repeatableread rowlock serializable snapshot spatial_window_max_cells tablock tablockx updlock xlock keepidentity keepdefaults ignore_constraints ignore_triggers",
  types: SQLTypes + "smalldatetime datetimeoffset datetime2 datetime bigint smallint smallmoney tinyint money real text nvarchar ntext varbinary image hierarchyid uniqueidentifier sql_variant xml",
  builtin: MSSQLBuiltin,
  operatorChars: "*+-%<>!=^&|/",
  specialVar: "@",
  identifierQuotes: "\"["
})

/// [SQLite](https://sqlite.org/) dialect.
export const SQLite = SQLDialect.define({
  keywords: SQLKeywords + "abort analyze attach autoincrement conflict database detach exclusive fail glob ignore index indexed instead isnull notnull offset plan pragma query raise regexp reindex rename replace temp vacuum virtual",
  types: SQLTypes + "bool blob long longblob longtext medium mediumblob mediumint mediumtext tinyblob tinyint tinytext text bigint int2 int8 unsigned signed real",
  builtin: "auth backup bail changes clone databases dbinfo dump echo eqp explain fullschema headers help import imposter indexes iotrace lint load log mode nullvalue once print prompt quit restore save scanstats separator shell show stats system tables testcase timeout timer trace vfsinfo vfslist vfsname width",
  operatorChars: "*+-%<>!=&|/~",
  identifierQuotes: "`\"",
  specialVar: "@:?$"
})

/// Dialect for [Cassandra](https://cassandra.apache.org/)'s SQL-ish query language.
export const Cassandra = SQLDialect.define({
  keywords: "add all allow alter and any apply as asc authorize batch begin by clustering columnfamily compact consistency count create custom delete desc distinct drop each_quorum exists filtering from grant if in index insert into key keyspace keyspaces level limit local_one local_quorum modify nan norecursive nosuperuser not of on one order password permission permissions primary quorum rename revoke schema select set storage superuser table three to token truncate ttl two type unlogged update use user users using values where with writetime infinity NaN",
  types: SQLTypes + "ascii bigint blob counter frozen inet list map static text timeuuid tuple uuid varint",
  slashComments: true
})

/// [PL/SQL](https://en.wikipedia.org/wiki/PL/SQL) dialect.
export const PLSQL = SQLDialect.define({
  keywords: SQLKeywords + "abort accept access add all alter and any arraylen as asc assert assign at attributes audit authorization avg base_table begin between binary_integer body by case cast char_base check close cluster clusters colauth column comment commit compress connected constant constraint crash create current currval cursor data_base database dba deallocate debugoff debugon declare default definition delay delete desc digits dispose distinct do drop else elseif elsif enable end entry exception exception_init exchange exclusive exists external fast fetch file for force form from function generic goto grant group having identified if immediate in increment index indexes indicator initial initrans insert interface intersect into is key level library like limited local lock log logging loop master maxextents maxtrans member minextents minus mislabel mode modify multiset new next no noaudit nocompress nologging noparallel not nowait number_base of off offline on online only option or order out package parallel partition pctfree pctincrease pctused pls_integer positive positiven pragma primary prior private privileges procedure public raise range raw rebuild record ref references refresh rename replace resource restrict return returning returns reverse revoke rollback row rowid rowlabel rownum rows run savepoint schema segment select separate set share snapshot some space split sql start statement storage subtype successful synonym tabauth table tables tablespace task terminate then to trigger truncate type union unique unlimited unrecoverable unusable update use using validate value values variable view views when whenever where while with work",
  builtin: "appinfo arraysize autocommit autoprint autorecovery autotrace blockterminator break btitle cmdsep colsep compatibility compute concat copycommit copytypecheck define echo editfile embedded feedback flagger flush heading headsep instance linesize lno loboffset logsource longchunksize markup native newpage numformat numwidth pagesize pause pno recsep recsepchar repfooter repheader serveroutput shiftinout show showmode spool sqlblanklines sqlcase sqlcode sqlcontinue sqlnumber sqlpluscompatibility sqlprefix sqlprompt sqlterminator suffix tab term termout timing trimout trimspool ttitle underline verify version wrap",
  types: SQLTypes + "ascii bfile bfilename bigserial bit blob dec long number nvarchar nvarchar2 serial smallint string text uid varchar2 xml",
  operatorChars: "*/+-%<>!=~",
  doubleQuotedStrings: true,
  charSetCasts: true,
  plsqlQuotingMechanism: true
})
```

## File: `src/tokens.ts`
```typescript
import {ExternalTokenizer, InputStream} from "@lezer/lr"
import {whitespace, LineComment, BlockComment, String as StringToken, Number, Bits, Bytes, Bool, Null,
        ParenL, ParenR, BraceL, BraceR, BracketL, BracketR, Semi, Dot,
        Operator, Punctuation, SpecialVar, Identifier, QuotedIdentifier,
        Keyword, Type, Builtin} from "./sql.grammar.terms"

const enum Ch {
  Newline = 10,
  Space = 32,
  DoubleQuote = 34,
  Hash = 35,
  Dollar = 36,
  SingleQuote = 39,
  ParenL = 40, ParenR = 41,
  Star = 42,
  Plus = 43,
  Comma = 44,
  Dash = 45,
  Dot = 46,
  Slash = 47,
  Colon = 58,
  Semi = 59,
  Question = 63,
  At = 64,
  BracketL = 91, BracketR = 93,
  Backslash = 92,
  Underscore = 95,
  Backtick = 96,
  BraceL = 123, BraceR = 125,

  A = 65, a = 97,
  B = 66, b = 98,
  E = 69, e = 101,
  F = 70, f = 102,
  N = 78, n = 110,
  Q = 81, q = 113,
  X = 88, x = 120,
  Z = 90, z = 122,

  _0 = 48, _1 = 49, _9 = 57,
}

function isAlpha(ch: number) {
  return ch >= Ch.A && ch <= Ch.Z || ch >= Ch.a && ch <= Ch.z || ch >= Ch._0 && ch <= Ch._9
}

function isHexDigit(ch: number) {
  return ch >= Ch._0 && ch <= Ch._9 || ch >= Ch.a && ch <= Ch.f || ch >= Ch.A && ch <= Ch.F
}

function readLiteral(input: InputStream, endQuote: number, backslashEscapes: boolean) {
  for (let escaped = false;;) {
    if (input.next < 0) return
    if (input.next == endQuote && !escaped) { input.advance(); return }
    escaped = backslashEscapes && !escaped && input.next == Ch.Backslash
    input.advance()
  }
}

function readDoubleDollarLiteral(input: InputStream, tag: string) {
  scan: for (;;) {
    if (input.next < 0) return
    if (input.next == Ch.Dollar) {
      input.advance()
      for (let i = 0; i < tag.length; i++) {
        if (input.next != tag.charCodeAt(i)) continue scan
        input.advance()
      }
      if (input.next == Ch.Dollar) {
        input.advance()
        return
      }
    } else {
      input.advance()
    }
  }
}

function readPLSQLQuotedLiteral(input: InputStream, openDelim: number) {
  let matchingDelim = "[{<(".indexOf(String.fromCharCode(openDelim))
  let closeDelim = matchingDelim < 0 ? openDelim : "]}>)".charCodeAt(matchingDelim)

  for (;;) {
    if (input.next < 0) return
    if (input.next == closeDelim && input.peek(1) == Ch.SingleQuote) {
      input.advance(2)
      return
    }
    input.advance()
  }
}

function readWord(input: InputStream): void
function readWord(input: InputStream, result: string): string
function readWord(input: InputStream, result?: string) {
  for (;;) {
    if (input.next != Ch.Underscore && !isAlpha(input.next)) break
    if (result != null) result += String.fromCharCode(input.next)
    input.advance()
  }
  return result
}

function readWordOrQuoted(input: InputStream) {
  if (input.next == Ch.SingleQuote || input.next == Ch.DoubleQuote || input.next == Ch.Backtick) {
    let quote = input.next
    input.advance()
    readLiteral(input, quote, false)
  } else {
    readWord(input)
  }
}

function readBits(input: InputStream, endQuote?: number) {
  while ((input as any).next == Ch._0 || (input as any).next == Ch._1) input.advance()
  if (endQuote && input.next == endQuote) input.advance()
}

function readNumber(input: InputStream, sawDot: boolean) {
  for (;;) {
    if (input.next == Ch.Dot) {
      if (sawDot) break
      sawDot = true
    } else if (input.next < Ch._0 || input.next > Ch._9) {
      break
    }
    input.advance()
  }
  if (input.next == Ch.E || input.next == Ch.e) {
    input.advance()
    if ((input as any).next == Ch.Plus || (input as any).next == Ch.Dash) input.advance()
    while (input.next >= Ch._0 && input.next <= Ch._9) input.advance()
  }
}

function eol(input: InputStream) {
  while (!(input.next < 0 || input.next == Ch.Newline)) input.advance()
}

function inString(ch: number, str: string) {
  for (let i = 0; i < str.length; i++) if (str.charCodeAt(i) == ch) return true
  return false
}

const Space = " \t\r\n"

function keywords(keywords: string, types: string, builtin?: string) {
  let result: {[name: string]: number} = Object.create(null)
  result["true"] = result["false"] = Bool
  result["null"] = result["unknown"] = Null
  for (let kw of keywords.split(" ")) if (kw) result[kw] = Keyword
  for (let tp of types.split(" ")) if (tp) result[tp] = Type
  for (let kw of (builtin || "").split(" ")) if (kw) result[kw] = Builtin
  return result
}

export interface Dialect {
  backslashEscapes: boolean,
  hashComments: boolean,
  spaceAfterDashes: boolean,
  slashComments: boolean,
  doubleQuotedStrings: boolean,
  doubleDollarQuotedStrings: boolean,
  unquotedBitLiterals: boolean,
  treatBitsAsBytes: boolean,
  charSetCasts: boolean,
  plsqlQuotingMechanism: boolean,
  operatorChars: string,
  specialVar: string,
  identifierQuotes: string,
  caseInsensitiveIdentifiers: boolean,
  words: {[name: string]: number}
}

export const SQLTypes = "array binary bit boolean char character clob date decimal double float int integer interval large national nchar nclob numeric object precision real smallint time timestamp varchar varying "
export const SQLKeywords = "absolute action add after all allocate alter and any are as asc assertion at authorization before begin between both breadth by call cascade cascaded case cast catalog check close collate collation column commit condition connect connection constraint constraints constructor continue corresponding count create cross cube current current_date current_default_transform_group current_transform_group_for_type current_path current_role current_time current_timestamp current_user cursor cycle data day deallocate declare default deferrable deferred delete depth deref desc describe descriptor deterministic diagnostics disconnect distinct do domain drop dynamic each else elseif end end-exec equals escape except exception exec execute exists exit external fetch first for foreign found from free full function general get global go goto grant group grouping handle having hold hour identity if immediate in indicator initially inner inout input insert intersect into is isolation join key language last lateral leading leave left level like limit local localtime localtimestamp locator loop map match method minute modifies module month names natural nesting new next no none not of old on only open option or order ordinality out outer output overlaps pad parameter partial path prepare preserve primary prior privileges procedure public read reads recursive redo ref references referencing relative release repeat resignal restrict result return returns revoke right role rollback rollup routine row rows savepoint schema scroll search second section select session session_user set sets signal similar size some space specific specifictype sql sqlexception sqlstate sqlwarning start state static system_user table temporary then timezone_hour timezone_minute to trailing transaction translation treat trigger under undo union unique unnest until update usage user using value values view when whenever where while with without work write year zone "

const defaults: Dialect = {
  backslashEscapes: false,
  hashComments: false,
  spaceAfterDashes: false,
  slashComments: false,
  doubleQuotedStrings: false,
  doubleDollarQuotedStrings: false,
  unquotedBitLiterals: false,
  treatBitsAsBytes: false,
  charSetCasts: false,
  plsqlQuotingMechanism: false,
  operatorChars: "*+\-%<>!=&|~^/",
  specialVar: "?",
  identifierQuotes: '"',
  caseInsensitiveIdentifiers: false,
  words: keywords(SQLKeywords, SQLTypes)
}

export function dialect(spec: Partial<Dialect>, kws?: string, types?: string, builtin?: string): Dialect {
  let dialect = {} as Dialect
  for (let prop in defaults)
    (dialect as any)[prop] = ((spec.hasOwnProperty(prop) ? spec : defaults) as any)[prop]
  if (kws) dialect.words = keywords(kws, types || "", builtin)
  return dialect
}

export function tokensFor(d: Dialect) {
  return new ExternalTokenizer(input => {
    let {next} = input
    input.advance()
    if (inString(next, Space)) {
      while (inString(input.next, Space)) input.advance()
      input.acceptToken(whitespace)
    } else if (next == Ch.Dollar && d.doubleDollarQuotedStrings) {
      let tag = readWord(input, "")
      if (input.next == Ch.Dollar) {
        input.advance()
        readDoubleDollarLiteral(input, tag)
        input.acceptToken(StringToken)
      }
    } else if (next == Ch.SingleQuote || next == Ch.DoubleQuote && d.doubleQuotedStrings) {
      readLiteral(input, next, d.backslashEscapes)
      input.acceptToken(StringToken)
    } else if (next == Ch.Hash && d.hashComments ||
               next == Ch.Slash && input.next == Ch.Slash && d.slashComments) {
      eol(input)
      input.acceptToken(LineComment)
    } else if (next == Ch.Dash && input.next == Ch.Dash &&
               (!d.spaceAfterDashes || input.peek(1) == Ch.Space)) {
      eol(input)
      input.acceptToken(LineComment)
    } else if (next == Ch.Slash && input.next == Ch.Star) {
      input.advance()
      for (let depth = 1;;) {
        let cur: number = input.next
        if (input.next < 0) break
        input.advance()
        if (cur == Ch.Star && (input as any).next == Ch.Slash) {
          depth--
          input.advance()
          if (!depth) break
        } else if (cur == Ch.Slash && input.next == Ch.Star) {
          depth++
          input.advance()
        }
      }
      input.acceptToken(BlockComment)
    } else if ((next == Ch.e || next == Ch.E) && input.next == Ch.SingleQuote) {
      input.advance()
      readLiteral(input, Ch.SingleQuote, true)
      input.acceptToken(StringToken)
    } else if ((next == Ch.n || next == Ch.N) && input.next == Ch.SingleQuote &&
               d.charSetCasts) {
      input.advance()
      readLiteral(input, Ch.SingleQuote, d.backslashEscapes)
      input.acceptToken(StringToken)
    } else if (next == Ch.Underscore && d.charSetCasts) {
      for (let i = 0;; i++) {
        if (input.next == Ch.SingleQuote && i > 1) {
          input.advance()
          readLiteral(input, Ch.SingleQuote, d.backslashEscapes)
          input.acceptToken(StringToken)
          break
        }
        if (!isAlpha(input.next)) break
        input.advance()
      }
    } else if (d.plsqlQuotingMechanism &&
               (next == Ch.q || next == Ch.Q) && input.next == Ch.SingleQuote &&
               input.peek(1) > 0 && !inString(input.peek(1), Space)) {
      let openDelim = input.peek(1)
      input.advance(2)
      readPLSQLQuotedLiteral(input, openDelim)
      input.acceptToken(StringToken)
    } else if (inString(next, d.identifierQuotes)) {
      const endQuote = next == Ch.BracketL ? Ch.BracketR : next
      readLiteral(input, endQuote, false)
      input.acceptToken(QuotedIdentifier)
    } else if (next == Ch.ParenL) {
      input.acceptToken(ParenL)
    } else if (next == Ch.ParenR) {
      input.acceptToken(ParenR)
    } else if (next == Ch.BraceL) {
      input.acceptToken(BraceL)
    } else if (next == Ch.BraceR) {
      input.acceptToken(BraceR)
    } else if (next == Ch.BracketL) {
      input.acceptToken(BracketL)
    } else if (next == Ch.BracketR) {
      input.acceptToken(BracketR)
    } else if (next == Ch.Semi) {
      input.acceptToken(Semi)
    } else if (d.unquotedBitLiterals && next == Ch._0 && input.next == Ch.b) {
      input.advance()
      readBits(input)
      input.acceptToken(Bits)
    } else if ((next == Ch.b || next == Ch.B) && (input.next == Ch.SingleQuote || input.next == Ch.DoubleQuote)) {
      const quoteStyle = input.next
      input.advance()
      if (d.treatBitsAsBytes) {
        readLiteral(input, quoteStyle, d.backslashEscapes)
        input.acceptToken(Bytes)
      } else {
        readBits(input, quoteStyle)
        input.acceptToken(Bits)
      }
    } else if (next == Ch._0 && (input.next == Ch.x || input.next == Ch.X) ||
               (next == Ch.x || next == Ch.X) && input.next == Ch.SingleQuote) {
      let quoted = input.next == Ch.SingleQuote
      input.advance()
      while (isHexDigit(input.next)) input.advance()
      if (quoted && input.next == Ch.SingleQuote) input.advance()
      input.acceptToken(Number)
    } else if (next == Ch.Dot && input.next >= Ch._0 && input.next <= Ch._9) {
      readNumber(input, true)
      input.acceptToken(Number)
    } else if (next == Ch.Dot) {
      input.acceptToken(Dot)
    } else if (next >= Ch._0 && next <= Ch._9) {
      readNumber(input, false)
      input.acceptToken(Number)
    } else if (inString(next, d.operatorChars)) {
      while (inString(input.next, d.operatorChars)) input.advance()
      input.acceptToken(Operator)
    } else if (inString(next, d.specialVar)) {
      if (input.next == next) input.advance()
      readWordOrQuoted(input)
      input.acceptToken(SpecialVar)
    } else if (next == Ch.Colon || next == Ch.Comma) {
      input.acceptToken(Punctuation)
    } else if (isAlpha(next)) {
      let word = readWord(input, String.fromCharCode(next))
      input.acceptToken(input.next == Ch.Dot || input.peek(-word.length - 1) == Ch.Dot
        ? Identifier : d.words[word.toLowerCase()] ?? Identifier)
    }
  })
}

export const tokens = tokensFor(defaults)
```

## File: `test/test-complete.ts`
```typescript
import {EditorState} from "@codemirror/state"
import {CompletionContext, CompletionResult, CompletionSource} from "@codemirror/autocomplete"
import {schemaCompletionSource, keywordCompletionSource, PostgreSQL, MySQL, SQLConfig, SQLDialect, MSSQL} from "@codemirror/lang-sql"
import ist from "ist"

function get(doc: string, conf: SQLConfig & {explicit?: boolean, keywords?: boolean} = {}) {
  let cur = doc.indexOf("|"), dialect = conf.dialect || PostgreSQL
  doc = doc.slice(0, cur) + doc.slice(cur + 1)
  let state = EditorState.create({
    doc,
    selection: {anchor: cur},
    extensions: [dialect, dialect.language.data.of({
      autocomplete: conf.keywords
        ? keywordCompletionSource(dialect, conf.upperCaseKeywords, conf.keywordCompletion)
        : schemaCompletionSource(Object.assign({dialect}, conf))
    })]
  })
  let result = state.languageDataAt<CompletionSource>("autocomplete", cur)[0](new CompletionContext(state, cur, !!conf.explicit))
  return result as CompletionResult | null
}

function str(result: CompletionResult | null) {
  return !result ? "" : result.options.slice()
    .sort((a, b) => (b.boost || 0) - (a.boost || 0) || (a.label < b.label ? -1 : 1))
    .map(o => o.apply || o.label)
    .join(", ")
}

let schema1 = {
  users: ["name", "id", "address"],
  products: ["name", "cost", "description"]
}

let schema2 = {
  "public.users": ["email", "id"],
  "other.users": ["name", "id"]
}

describe("SQL completion", () => {
  it("completes table names", () => {
    ist(str(get("select u|", {schema: schema1})), "products, users")
  })

  it("completes quoted table names", () => {
    ist(str(get('select "u|', {schema: schema1})), '"products", "users"')
  })

  it("completes table names under schema", () => {
    ist(str(get("select public.u|", {schema: schema2})), "users")
  })

  it("completes quoted table names under schema", () => {
    ist(str(get('select public."u|', {schema: schema2})), '"users"')
  })

  it("completes quoted table names under quoted schema", () => {
    ist(str(get('select "public"."u|', {schema: schema2})), '"users"')
  })

  it("completes column names", () => {
    ist(str(get("select users.|", {schema: schema1})), "address, id, name")
  })

  it("completes quoted column names", () => {
    ist(str(get('select users."|', {schema: schema1})), '"address", "id", "name"')
  })

  it("completes column names in quoted tables", () => {
    ist(str(get('select "users".|', {schema: schema1})), "address, id, name")
  })

  it("completes column names in tables for a specific schema", () => {
    ist(str(get("select public.users.|", {schema: schema2})), "email, id")
    ist(str(get("select other.users.|", {schema: schema2})), "id, name")
  })

  it("completes quoted column names in tables for a specific schema", () => {
    ist(str(get('select public.users."|', {schema: schema2})), '"email", "id"')
    ist(str(get('select other.users."|', {schema: schema2})), '"id", "name"')
  })

  it("completes column names in quoted tables for a specific schema", () => {
    ist(str(get('select public."users".|', {schema: schema2})), "email, id")
    ist(str(get('select other."users".|', {schema: schema2})), "id, name")
  })

  it("completes column names in quoted tables for a specific quoted schema", () => {
    ist(str(get('select "public"."users".|', {schema: schema2})), "email, id")
    ist(str(get('select "other"."users".|', {schema: schema2})), "id, name")
  })

  it("completes quoted column names in quoted tables for a specific quoted schema", () => {
    ist(str(get('select "public"."users"."|', {schema: schema2})), '"email", "id"')
    ist(str(get('select "other"."users"."|', {schema: schema2})), '"id", "name"')
  })

  it("completes column names in bracket quoted tables with MSSQL", () => {
    ist(str(get("select [public].[users].|", {schema: schema2, dialect: MSSQL})), "email, id")
    ist(str(get("select [other].[users].|", {schema: schema2, dialect: MSSQL})), "id, name")
  })

  it("completes column names of aliased tables", () => {
    ist(str(get("select u.| from users u", {schema: schema1})), "address, id, name")
    ist(str(get("select u.| from users as u", {schema: schema1})), "address, id, name")
    ist(str(get("select u.| from (SELECT * FROM something u) join users u", {schema: schema1})), "address, id, name")
    ist(str(get("select * from users u where u.|", {schema: schema1})), "address, id, name")
    ist(str(get("select * from users as u where u.|", {schema: schema1})), "address, id, name")
    ist(str(get("select * from (SELECT * FROM something u) join users u where u.|", {schema: schema1})), "address, id, name")
  })

  it("completes column names of aliased quoted tables", () => {
    ist(str(get('select u.| from "users" u', {schema: schema1})), "address, id, name")
    ist(str(get('select u.| from "users" as u', {schema: schema1})), "address, id, name")
    ist(str(get('select * from "users" u where u.|', {schema: schema1})), "address, id, name")
    ist(str(get('select * from "users" as u where u.|', {schema: schema1})), "address, id, name")
  })

  it("completes column names of aliased tables for a specific schema", () => {
    ist(str(get("select u.| from public.users u", {schema: schema2})), "email, id")
  })

  it("completes column names in aliased quoted tables for a specific schema", () => {
    ist(str(get('select u.| from public."users" u', {schema: schema2})), "email, id")
  })

  it("completes column names in aliased quoted tables for a specific quoted schema", () => {
    ist(str(get('select u.| from "public"."users" u', {schema: schema2})), "email, id")
  })

  it("completes aliased table names", () => {
    ist(str(get('select a| from a.b as ab join auto au', {schema: schema2})), "ab, au, other, public")
  })

  it("completes bracket quoted aliases with MSSQL", () => {
    ist(str(get("select u.| from public.users [u]", {schema: schema2, dialect: MSSQL})), "email, id")
    ist(str(get("select [u].| from public.users u", {schema: schema2, dialect: MSSQL})), "email, id")
  })

  it("includes closing quote in completion", () => {
    let r = get('select "u|"', {schema: schema1})
    ist(r!.to, 10)
  })

  it("keeps extra table completion properties", () => {
    let r = get("select u|", {schema: {users: ["id"]}, tables: [{label: "users", type: "keyword"}]})
    ist(r!.options[0].type, "keyword")
  })

  it("keeps extra column completion properties", () => {
    let r = get("select users.|", {schema: {users: [{label: "id", type: "keyword"}]}})
    ist(r!.options[0].type, "keyword")
  })

  it("supports a default table", () => {
    ist(str(get("select i|", {schema: schema1, defaultTable: "users"})), "address, id, name, products, users")
  })

  it("supports alternate quoting styles", () => {
    ist(str(get("select `u|", {dialect: MySQL, schema: schema1})), "`products`, `users`")
    ist(str(get("select [u|", {dialect: MSSQL, schema: schema1})), "[products], [users]")
  })

  it("doesn't complete without identifier", () => {
    ist(str(get("select |", {schema: schema1})), "")
  })

  it("does complete explicitly without identifier", () => {
    ist(str(get("select |", {schema: schema1, explicit: true})), "products, users")
  })

  it("adds identifiers for non-word completions", () => {
    ist(str(get("foo.b|", {schema: {foo: ["b c", "b-c", "bup"]}, dialect: PostgreSQL})),
        '"b c", "b-c", bup')
    ist(str(get("foo.b|", {schema: {foo: ["b c", "b-c", "bup"]}, dialect: MySQL})),
        '`b c`, `b-c`, bup')
  })

  it("adds identifiers for upper case completions", () => {
    ist(str(get("foo.c|", {schema: {foo: ["Column", "cell"]}, dialect: PostgreSQL})),
        '"Column", cell')

    const customDialect = SQLDialect.define({...PostgreSQL.spec, caseInsensitiveIdentifiers: true})
    ist(str(get("foo.c|", {schema: {foo: ["Column", "cell"]}, dialect: customDialect})),
        'Column, cell')
  })

  it("can add MSSQL-style brackets as identifier quotes", () => {
    let dialect = SQLDialect.define({...MSSQL.spec, identifierQuotes: '['})
    let config = { schema: {"Foo": ["Bar"]}, dialect: dialect }

    ist(str(get("[Foo].b|", config)), "[Bar]")
  })

  it("supports nesting more than two deep", () => {
    let s = {schema: {"one.two.three": ["four"]}}
    ist(str(get("o|", s)), "one")
    ist(str(get("one.|", s)), "two")
    ist(str(get("one.two.|", s)), "three")
    ist(str(get("one.two.three.|", s)), "four")
  })

  it("supports escaped dots in table names", () => {
    let s = {schema: {"db\\.conf": ["abc"]}}
    ist(str(get("db|", s)), '"db.conf"')
    ist(str(get('"db.conf".|', s)), "abc")
  })

  it("supports nested schema declarations", () => {
    let s = {schema: {
      public: {users: ["email", "id"]},
      other: {users: ["name", "id"]},
      plain: ["one", "two"]
    }}
    ist(str(get("pl|", s)), "other, plain, public")
    ist(str(get("plain.|", s)), "one, two")
    ist(str(get("public.u|", s)), "users")
    ist(str(get("public.users.e|", s)), "email, id")
  })

  it("supports self fields to specify table/schema completions", () => {
    let s: SQLConfig = {schema: {
      foo: {
        self: {label: "foo", type: "keyword"},
        children: {
          bar: {
            self: {label: "bar", type: "constant"},
            children: ["a", "b"]
          }
        }
      }
    }}
    ist(get("select f|", s)!.options[0].type, "keyword")
    ist(get("select foo.|", s)!.options[0].type, "constant")
    ist(get("select foo.|", s)!.options.length, 1)
  })

  it("can complete keywords", () => {
    ist(get("s|", {keywords: true})!.options.some(c => c.label == "select"))
  })

  it("can complete upper-case keywords", () => {
    ist(get("s|", {keywords: true, upperCaseKeywords: true})!.options.some(c => c.label == "SELECT"))
  })

  it("can transform keyword completions", () => {
    ist(get("s|", {keywords: true, keywordCompletion: l => ({label: l, type: "x"})})!.options.every(c => c.type == "x"))
  })
})
```

## File: `test/test-tokens.ts`
```typescript
import ist from "ist"
import {PostgreSQL, MySQL, PLSQL, SQLDialect, MSSQL} from "@codemirror/lang-sql"

const mysqlTokens = MySQL.language
const postgresqlTokens = PostgreSQL.language
const bigQueryTokens = SQLDialect.define({
  treatBitsAsBytes: true
}).language
const plsqlTokens = PLSQL.language
const mssqlTokens = MSSQL.language

describe("Parse MySQL tokens", () => {
  const parser = mysqlTokens.parser

  it("parses quoted bit-value literals", () => {
    ist(parser.parse("SELECT b'0101'"), 'Script(Statement(Keyword,Bits))')
  })

  it("parses unquoted bit-value literals", () => {
    ist(parser.parse("SELECT 0b01"), 'Script(Statement(Keyword,Bits))')
  })
})

describe("Parse PostgreSQL tokens", () => {
  const parser = postgresqlTokens.parser

  it("parses quoted bit-value literals", () => {
    ist(parser.parse("SELECT b'0101'"), 'Script(Statement(Keyword,Bits))')
  })

  it("parses quoted bit-value literals", () => {
    ist(parser.parse("SELECT B'0101'"), 'Script(Statement(Keyword,Bits))')
  })

  it("parses double dollar quoted string literals", () => {
    ist(parser.parse("SELECT $$hello$$"), 'Script(Statement(Keyword,String))')
  })

  it("parses tagged double dollar quoted string literals", () => {
    ist(parser.parse("SELECT $body$\nhello\n$body$"), 'Script(Statement(Keyword,String))')
  })
})

describe("Parse BigQuery tokens", () => {
  const parser = bigQueryTokens.parser

  it("parses quoted bytes literals in single quotes", () => {
    ist(parser.parse("SELECT b'abcd'"), 'Script(Statement(Keyword,Bytes))')
  })

  it("parses quoted bytes literals in double quotes", () => {
    ist(parser.parse('SELECT b"abcd"'), 'Script(Statement(Keyword,Bytes))')
  })

  it("parses bytes literals in single quotes", () => {
    ist(parser.parse("SELECT b'0101'"), 'Script(Statement(Keyword,Bytes))')
  })

  it("parses bytes literals in double quotes", () => {
    ist(parser.parse('SELECT b"0101"'), 'Script(Statement(Keyword,Bytes))')
  })
})

describe("Parse PL/SQL tokens", () => {
  const parser = plsqlTokens.parser

  it("parses alternative quoting mechanism - []", () => {
    ist(parser.parse("SELECT q'[foo'bar]' FROM DUAL"), 'Script(Statement(Keyword,String,Keyword,Identifier))')
  })

  it("parses alternative quoting mechanism - {}", () => {
    ist(parser.parse("SELECT q'{foo'bar}' FROM DUAL"), 'Script(Statement(Keyword,String,Keyword,Identifier))')
  })

  it("parses alternative quoting mechanism - <>", () => {
    ist(parser.parse("SELECT q'<foo'bar>' FROM DUAL"), 'Script(Statement(Keyword,String,Keyword,Identifier))')
  })

  it("parses alternative quoting mechanism - ()", () => {
    ist(parser.parse("SELECT q'(foo'bar)' FROM DUAL"), 'Script(Statement(Keyword,String,Keyword,Identifier))')
  })

  it("parses alternative quoting mechanism - custom", () => {
    ist(parser.parse("SELECT q'~foo'bar~' FROM DUAL"), 'Script(Statement(Keyword,String,Keyword,Identifier))')
  })

  it("parses alternative quoting mechanism - uppercase Q", () => {
    ist(parser.parse("SELECT Q'~foo'bar~' FROM DUAL"), 'Script(Statement(Keyword,String,Keyword,Identifier))')
  })

  it("parses alternative quoting mechanism - unclosed", () => {
    ist(parser.parse("SELECT q'~foo'bar' FROM DUAL"), 'Script(Statement(Keyword,String))')
  })
})

describe("Parse MSSQL tokens", () => {
  const parser = mssqlTokens.parser;

  it("parses brackets as QuotedIdentifier", () => {
    ist(parser.parse("SELECT * FROM [tblTest]"), "Script(Statement(Keyword,Operator,Keyword,QuotedIdentifier))")
  })
})
```

