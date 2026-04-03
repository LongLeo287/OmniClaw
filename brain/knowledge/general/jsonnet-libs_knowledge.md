---
id: jsonnet-libs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.654163
---

# KNOWLEDGE EXTRACT: jsonnet-libs
> **Extracted on:** 2026-03-30 17:38:13
> **Source:** jsonnet-libs

---

## File: `docsonnet.md`
```markdown
# 📦 jsonnet-libs/docsonnet [🔖 PENDING/APPROVE]
🔗 https://github.com/jsonnet-libs/docsonnet


## Meta
- **Stars:** ⭐ 69 | **Forks:** 🍴 17
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Experimental Jsonnet docs generator

## README (trích đầu)
```
# `docsonnet`

This repository contains an experimental Jsonnet docs generator, consisting of multiple parts:

- **Docsonnet**, a **data model** for logically describing the structure of public
  facing Jsonnet API's.
- `doc-util`, A **Jsonnet extension** that allows to write Docsonnet directly
  alongside your Jsonnet. Currently implemented as a library, might become
  language sugar at some point
- `docsonnet`: A **CLI application** and Go library for parsing Docsonnet and
  transforming it to e.g. **Markdown** pages

## Example

To make use of Docsonnet, use `doc-util` to annotate your Jsonnet like so:

```jsonnet
{
    // package declaration
    '#': d.pkg(
      name='url',
      url='github.com/jsonnet-libs/xtd/url/main.libsonet',
      help='`url` implements URL escaping and query building',
    ),

    // function description
    '#encodeQuery': d.fn(
      '`encodeQuery` takes an query parameters and returns them as an escaped `key=value` string',
      [d.arg('params', d.T.object)]),
    encodeQuery(params)::
      local fmtParam(p) = '%s=%s' % [self.escapeString(p), self.escapeString(params[p])];
      std.join('&', std.map(fmtParam, std.objectFields(params))),
}
```

### Packages

Jsonnet itself does not know traditional packages, classes or similar.

For documentation and distribution purposes however, it seems reasonable to introduce a concept of **loose packages**, defined as a single importable file, holding all of your **public API**.

As an example, a hypothetical `url` library could define its package like above example does.

Packages are defined by including assigning a `d.pkg` call to a key literally named `#` (hash). All fields, including nested packages, of the same object having the `#` key belong to that package.

### Functions

Most common part of an API will be functions. These are annotated in a similar fashion:

```jsonnet
{
    "#myFunc": d.fn("myFunc greets you", [d.arg("who", d.T.string)])
    myFunc(who):: "hello %s!" % who
}
```

Along the actual function definition, a _docsonnet_ key is added, with the functions name prefixed by the familiar `#` as its name.
Above example defines `myFunc` as a function, that greets the user and takes a single argument of type `string`.

### Objects

Sometimes you might want to group functions of a similar kind, by nesting them into plain Jsonnet objects.

Such an object might need a description as well, so you can also annotate it:

```jsonnet
{
    "#myObj": d.obj("myObj holds my functions")
    myObj:: {
        "#myFunc": d.fn("myFunc greets you", [d.arg("who", d.T.string)])
        myFunc(who):: "hello %s!" % who
    }
}
```

Again, the naming rule `#` joined with the fields name must be followed, so the `docsonnet` utility can automatically join together the contents of your object with its annotated description.


## Usage

Once you have a Jsonnet library annotated with `doc-util`, you can generate the docs using one of three ways:

- [Jsonnet renderer](#jsonnet-renderer)
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

