---
id: codemirror-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:08.123798
---

# KNOWLEDGE EXTRACT: codemirror
> **Extracted on:** 2026-03-30 17:34:53
> **Source:** codemirror

---

## File: `lang-sql.md`
```markdown
# 📦 codemirror/lang-sql [🔖 PENDING/APPROVE]
🔗 https://github.com/codemirror/lang-sql
🌐 https://codemirror.net

## Meta
- **Stars:** ⭐ 97 | **Forks:** 🍴 46
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-16
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
SQL language support for the CodeMirror code editor

## README (trích đầu)
```
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

<dd><p>When given, columns from the named 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

