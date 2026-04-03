---
id: github.com-jsonnet-libs-docsonnet-5e0f8c6f-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:16.849258
---

# KNOWLEDGE EXTRACT: github.com_jsonnet-libs_docsonnet_5e0f8c6f
> **Extracted on:** 2026-04-01 09:44:33
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520408/github.com_jsonnet-libs_docsonnet_5e0f8c6f

---

## File: `.gitignore`
```
dist
docsonnet
```

## File: `.goreleaser.yaml`
```yaml
project_name: docsonnet
before:
  hooks:
    - go mod tidy
builds:
  - binary: docsonnet
    env:
      - CGO_ENABLED=0
    goos:
      - linux
      - darwin
    goarch:
      - amd64
      - arm64
checksum:
  name_template: 'checksums.txt'
dockers:
- image_templates:
  - "ghcr.io/jsonnet-libs/docsonnet:{{ .Version }}-amd64"
  use: buildx
  dockerfile: Dockerfile
  build_flag_templates:
  - "--platform=linux/amd64"
- image_templates:
  - "ghcr.io/jsonnet-libs/docsonnet:{{ .Version }}-arm64v8"
  use: buildx
  goarch: arm64
  dockerfile: Dockerfile
  build_flag_templates:
  - "--platform=linux/arm64/v8"
docker_manifests:
- name_template: ghcr.io/jsonnet-libs/docsonnet:{{ .Version }}
  image_templates:
  - ghcr.io/jsonnet-libs/docsonnet:{{ .Version }}-amd64
  - ghcr.io/jsonnet-libs/docsonnet:{{ .Version }}-arm64v8
```

## File: `Dockerfile`
```
FROM alpine:3.12
ENTRYPOINT ["/usr/bin/docsonnet"]
COPY docsonnet /usr/bin/docsonnet
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "{}"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2018 grafana, sh0rez

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

## File: `Makefile`
```
.PHONY: build release docs

build:
	goreleaser build --rm-dist --snapshot

release:
	goreleaser release --rm-dist

docs:
	cd doc-util && \
	jsonnet -S -c -m . \
		-e "(import './main.libsonnet').render(import './main.libsonnet')"

```

## File: `README.md`
```markdown
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
- [docsonnet binary](#docsonnet-binary)
- [docsonnet docker image](#docsonnet-docker-image)

### Jsonnet renderer

The docs can be rendered using Jsonnet with the
[render](https://github.com/jsonnet-libs/docsonnet/tree/master/doc-util#fn-render) function.

In your library source, add a file `docs.jsonnet` (assuming your library entrypoint is `main.libsonnet`) with the
following contents:

```jsonnet
local d = import 'github.com/jsonnet-libs/docsonnet/doc-util/main.libsonnet';
d.render(import 'main.libsonnet')
```

Then, you can render the markdown to the `docs/` folder using the following command:

```
jsonnet -J vendor -S -c -m docs/ docs.jsonnet
```

Note that this requires `doc-util` to be installed to `vendor/` to work properly.

### docsonnet binary

Alternatively, the docs can be rendered using the `docsonnet` go binary. The `docsonnet` binary embeds the `doc-util`
library, avoiding the need to have `doc-util` installed.

You can install the `docsonnet` binary using `go install`:

```
go install github.com/jsonnet-libs/docsonnet@master
```

Once the binary is installed, you can generate the docs by passing it the main entrypoint to your Jsonnet library:

```
docsonnet main.libsonnet
```

> **Note**
>
> Linters like [jsonnet-lint](https://pkg.go.dev/github.com/google/go-jsonnet/linter) or `tk lint` require the imports to be resolvable, so you should add `doc-util` to `vendor/` when using these linters.

### docsonnet docker image

You can also use the [docker image](https://hub.docker.com/r/jsonnetlibs/docsonnet) which contains the `docsonnet`
binary if you do not wish to set up go or install the binary locally:

```
docker run --rm -v "$(pwd):/src" -v "$(pwd)/docs:/docs" jsonnetlibs/docsonnet /src/main.libsonnet
```


## FAQ

#### What's wrong with comments? Why not parse regular comments?

I had some attempts on this, especially because it feels more natural. However, the language properties of Jsonnet make this quite challenging:

- AST parsing is insufficient:
  https://github.com/grafana/tanka/issues/223#issuecomment-590569198. Just by
  parsing the syntax tree of Jsonnet, we only receive a representation of the
  file contents, not the logical ones a human might infer
- No effective view on things: Jsonnet is a lazily evaluated, highly dynamic
  language. Just by looking at a single file, we might not even see what ends up
  at the user when importing the library, because during evaluation things can
  be heavily overwritten.

Because of that, we would need to perform a slimmed down evaluation on the AST before getting our information out of it. This is a lot of work, especially when we can just use the real Jsonnet compiler to do this for us. That's docsonnet.

#### But docsonnet is ugly. And verbose

I know. Think of docsonnet as a proof of concept and a technology preview. Only _what_ you specify is a fixed thing, not the way you do.

Of course nobody wants these ugly function calls as docs. But they are incredibly powerful, because we can use Jsonnet merging and patching on the generated docsonnet fields, and the Jsonnet compiler handles that for us.

In case this idea works out well, we might very well consider adding docsonnet as language sugar to Jsonnet, which might look like this:

```jsonnet
{
    ## myFunc greets you
    ## @params:
    ##   who: string
    myFunc(who):: "hello %s!" % who
}
```

Note the double hash `##` as a special indicator for the compiler, so it can desugar above to:

```jsonnet
{
    "#myFunc": d.fn("myFunc greets you", [d.arg("who", d.T.string)])
    myFunc(who):: "hello %s!" % who
}
```

This will all happen transparently, without any user interaction

#### What else can it do?

Because the Docsonnet gives you the missing logical representation of your Jsonnet library, it enables straight forward implementation of other language tooling, such as **code-completion**.

Instead of inferring what fields are available for a library, we can _just_ look at its docsonnet and provide the fields specified there, along with nice descriptions and argument types.
```

## File: `go.mod`
```
module github.com/jsonnet-libs/docsonnet

go 1.19

require (
	github.com/go-clix/cli v0.1.2-0.20200502172020-b8f4629e879a
	github.com/google/go-cmp v0.4.0
	github.com/google/go-jsonnet v0.18.0
	github.com/markbates/pkger v0.15.1
	github.com/stretchr/testify v1.4.0
	gopkg.in/yaml.v2 v2.2.7
)

require (
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/gobuffalo/here v0.6.0 // indirect
	github.com/hashicorp/errwrap v1.0.0 // indirect
	github.com/hashicorp/go-multierror v1.0.0 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	github.com/posener/complete v1.2.3 // indirect
	github.com/spf13/pflag v1.0.5 // indirect
	sigs.k8s.io/yaml v1.1.0 // indirect
)
```

## File: `go.sum`
```
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/fatih/color v1.10.0/go.mod h1:ELkj/draVOlAH/xkhN6mQ50Qd0MPOk5AAr3maGEBuJM=
github.com/go-clix/cli v0.1.2-0.20200502172020-b8f4629e879a h1:nh+UOawbjKgiUAJAgi8JHctNebEu6mjwDXsv8Xdln8w=
github.com/go-clix/cli v0.1.2-0.20200502172020-b8f4629e879a/go.mod h1:dYJevXraB9mXZFhz5clyQestG0qGcmT5rRC/P9etoRQ=
github.com/gobuffalo/here v0.6.0 h1:hYrd0a6gDmWxBM4TnrGw8mQg24iSVoIkHEk7FodQcBI=
github.com/gobuffalo/here v0.6.0/go.mod h1:wAG085dHOYqUpf+Ap+WOdrPTp5IYcDAs/x7PLa8Y5fM=
github.com/google/go-cmp v0.4.0 h1:xsAVV57WRhGj6kEIi8ReJzQlHHqcBYCElAvkovg3B/4=
github.com/google/go-cmp v0.4.0/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-jsonnet v0.18.0 h1:/6pTy6g+Jh1a1I2UMoAODkqELFiVIdOxbNwv0DDzoOg=
github.com/google/go-jsonnet v0.18.0/go.mod h1:C3fTzyVJDslXdiTqw/bTFk7vSGyCtH3MGRbDfvEwGd0=
github.com/hashicorp/errwrap v1.0.0 h1:hLrqtEDnRye3+sgx6z4qVLNuviH3MR5aQ0ykNJa/UYA=
github.com/hashicorp/errwrap v1.0.0/go.mod h1:YH+1FKiLXxHSkmPseP+kNlulaMuP3n2brvKWEqk/Jc4=
github.com/hashicorp/go-multierror v1.0.0 h1:iVjPR7a6H0tWELX5NxNe7bYopibicUzc7uPribsnS6o=
github.com/hashicorp/go-multierror v1.0.0/go.mod h1:dHtQlpGsu+cZNNAkkCN/P3hoUDHhCYQXV3UM06sGGrk=
github.com/kr/pretty v0.1.0 h1:L/CwN0zerZDmRFUapSPitk6f+Q3+0za1rQkzVuMiMFI=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/markbates/pkger v0.15.1 h1:3MPelV53RnGSW07izx5xGxl4e/sdRD6zqseIk0rMASY=
github.com/markbates/pkger v0.15.1/go.mod h1:0JoVlrol20BSywW79rN3kdFFsE5xYM+rSCQDXbLhiuI=
github.com/mattn/go-colorable v0.1.8/go.mod h1:u6P/XSegPjTcexA+o6vUJrdnUu04hMope9wVRipJSqc=
github.com/mattn/go-isatty v0.0.12/go.mod h1:cbi8OIDigv2wuxKPP5vlRcQ1OAZbq2CE4Kysco4FUpU=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/posener/complete v1.2.3 h1:NP0eAhjcjImqslEwo/1hq7gpajME0fTLTezBKDqfXqo=
github.com/posener/complete v1.2.3/go.mod h1:WZIdtGGp+qx0sLrYKtIRAruyNpv6hFCicSgv7Sy7s/s=
github.com/sergi/go-diff v1.1.0 h1:we8PVUC3FE2uYfodKH/nBHMSetSfHDR6scGdBi+erh0=
github.com/sergi/go-diff v1.1.0/go.mod h1:STckp+ISIX8hZLjrqAeVduY0gWCT9IjLuqbuNXdaHfM=
github.com/spf13/pflag v1.0.5 h1:iy+VFUOCP1a+8yFto/drg2CJ5u0yRoB7fZw3DKv/JXA=
github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.4.0 h1:2E4SXV/wtOkTonXsotYi4li6zVWxYlZuYNCXe9XRJyk=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
golang.org/x/sys v0.0.0-20200116001909-b77594299b42/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200223170610-d5e6a3e2c0ae/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543 h1:E7g+9GITq07hpfrRu66IVDexMakfv52eLZ2CXBWiKr4=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15 h1:YR8cESwS4TdDjEe65xsg0ogRM/Nc3DYOhEAlW+xobZo=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.4/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.7 h1:VUgggvou5XRW9mHwD/yXxIYSMtY0zoKQf/v226p2nyo=
gopkg.in/yaml.v2 v2.2.7/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
sigs.k8s.io/yaml v1.1.0 h1:4A07+ZFc2wgJwo8YNlQpr1rVlgUDlxXHhPJciaPY5gs=
sigs.k8s.io/yaml v1.1.0/go.mod h1:UJmg0vDUVViEyp3mgSv9WPwZCDxu4rQW1olrI1uml+o=
```

## File: `load.libsonnet`
```
local lib = {
  scan(obj)::
    local aux(old, key) =
      if std.startsWith(key, '#') then
        true
      else if std.isObject(obj[key]) then
        old || $.scan(obj[key])
      else old;
    std.foldl(aux, std.objectFieldsAll(obj), false),

  load(pkg)::
    local aux(old, key) =
      if !std.isObject(pkg[key]) then
        old
      else if std.objectHasAll(pkg, '#' + key) && pkg['#' + key] == 'ignore' then
        old
      else if std.startsWith(key, '#') then
        old { [key]: pkg[key] }
      else if self.scan(pkg[key]) then
        old { [key]: $.load(pkg[key]) }
      else old;

    std.foldl(aux, std.objectFieldsAll(pkg), {}),
};


lib.load(std.extVar('main'))
```

## File: `main.go`
```go
package main

import (
	"encoding/json"
	"fmt"
	"log"

	"github.com/go-clix/cli"

	"github.com/jsonnet-libs/docsonnet/pkg/docsonnet"
	"github.com/jsonnet-libs/docsonnet/pkg/render"
)

func main() {
	log.SetFlags(0)

	root := &cli.Command{
		Use:   "docsonnet <file>",
		Short: "Utility to parse and transform Jsonnet code that uses the docsonnet extension",
		Args:  cli.ArgsExact(1),
	}

	dir := root.Flags().StringP("output", "o", "docs", "directory to write the .md files to")
	outputJSON := root.Flags().Bool("json", false, "print loaded docsonnet as JSON")
	outputRaw := root.Flags().Bool("raw", false, "don't transform, dump raw eval result")
	urlPrefix := root.Flags().String("urlPrefix", "/", "url-prefix for frontmatter")
	jpath := root.Flags().StringSliceP("jpath", "J", []string{"vendor"}, "Specify an additional library search dir (right-most wins)")

	root.Run = func(cmd *cli.Command, args []string) error {
		file := args[0]

		log.Println("Extracting from Jsonnet")
		data, err := docsonnet.Extract(file, docsonnet.Opts{JPath: *jpath})
		if err != nil {
			log.Fatalln("Extracting:", err)
		}
		if *outputRaw {
			fmt.Println(string(data))
			return nil
		}

		log.Println("Transforming to docsonnet model")
		pkg, err := docsonnet.Transform(data)
		if err != nil {
			log.Fatalln("Transforming:", err)
		}
		if *outputJSON {
			data, err := json.MarshalIndent(pkg, "", "  ")
			if err != nil {
				return err
			}
			fmt.Println(string(data))
			return nil
		}

		log.Println("Rendering markdown")
		n, err := render.To(*pkg, *dir, render.Opts{
			URLPrefix: *urlPrefix,
		})
		if err != nil {
			log.Fatalln("Rendering:", err)
		}

		log.Printf("Success! Rendered %v packages from '%s' to '%s'", n, file, *dir)
		return nil
	}

	if err := root.Execute(); err != nil {
		log.Fatalln(err)
	}
}
```

## File: `pkged.go`
```go
// Code generated by pkger; DO NOT EDIT.

// +build !skippkger

package main

import (
	"github.com/markbates/pkger"
	"github.com/markbates/pkger/pkging/mem"
)

var _ = pkger.Apply(mem.UnmarshalEmbed([]byte(`1f8b08000000000000ffec7a5d93a2baf6f75739c5ede38c80e2b4de35cc8868b733ad3d229cda350501439a403804547ad77cf7a7125eb5dfdc67ef9bf32f2fba21c92259592fbfb5b2cc9f028a77840a933f0588b220773f0312f56920a6fe73df23809238f63336fc15a5c244e80724f2fb999b3a0e08fb0792861daa9e60440949b31f4e1608937727ec094b27f28589103928167ac25702848920f4844727856cc1b39520e9bb283e996045c84bba171cdd3b190884c9bf85cfc21f3d619d39d81726599afb5563e53b94c4c244a0acf52fcf4ffcd8f363504cfed5e11f924f00a3631f6024f4049d4c11f6299b95b1ff1912a1272421f43df6fa472d064ee0c780782886fd27b64c4fd8458cab37a7ee0c444e1aba4ee6d33e9b3a7d7790fd678b447e744a772e784678229f8f6853260eb63826906dedab9ff07db9f90eb16dbb45e653a127001225a94f697f879dccef76c06794f0769c3928f6d33e4634ab3afc237f4b8b2423cd4bdf29672c1b00250167a06a7bdd418f3a6dc307a74d4f561469fca2a38fe2cc4f6307f77defe0a41e3d27c3182519026d4f10399d56f379eac45e9e21fcca10cddd0cfbed40e4296d837dd7698161a7d1dd000d1ce9a4252ba393b622c99df6d99219eec8e9a888e3d3563f09d151e835f6d979ed3b3496ba6dd7a1fe6878d28362272dba3d80eebbcdc0ef4e5e1b7fd34eb89dfa694a52c6e50e3bf02ff906246ebedb3998f4033ff5cfc708c43efbf6e9352b7f31dc77e82524d08f3fa2da913472b2ecdc575f12b616584be032f2bfbe40e2a4f42f91d3cbb949520253e70c70028706089034617b3ba44ef2d630249fa21c67888be06f205fc34ee424f442d2cc097d12f75f250dfcc4f987a6e9ef10cefc73fdbe0edd17c1bb1fb9bef7df058237e868e69133fe12427d06d30cc0b19ff9ef8ff641e47d4cd147318baff81f0e4ee74bbf1fc13e22a4383f53034d76d2a09f54f0044912c2cf28ee174e843fef19f63273ae1e7d908201eb6bcc83854607c36e1748f26e73176594a459b72bf6b32c7580dfed23b47692d6f708176627169d7e92fa3bec830ca3eca49ba218627f87110c4e56a505050ec67dffe8033fdebf3694c73c5eb4c6efd38ce5043d81e70188f411a9a261d91db12cb07cf45d04dbd78cd6ef55248c50e4578f3ec784c4e142e11dffc949e67b498ae2cc7179802b6d83692dc8b2a4f3caffd5d26b3a6b8eab3e96732429e1f9066be7291be14e40281740f99697b89994bb600fe6ce7ed5aee4cbdfa07f4c9a973e2de2cc61924af3382b3756bdf5014f14eb96e7bbdcdeea7623592723114f3f5e8c54227dd14f0bc67e654a344b01e13aa4598a62c8878a18548f76fa4ab3424f6032e9677e9454b9db49bb8c21acb7dc4d1e2340bcce5b3fcf76d2e8b47dc39bd4d931babd1f7b24ed43829d187e2629ec1ffb75761738207064f132aa84e0421a88ca07d4fcc1bcef52ba3ae3798f384ff77e9d29be431784deee7d8a9749e23bc41fec9819b01753f617f9943af0ade94e5c04e6dc053fa44b52722c3e2094fb41e280f01d2ae4c5ce1bc3b4a01524be36caad90fa204ffdbe8b3c94e66f4aab34d8d489294b91de23aa6d944d78095dcce6fba3273cfa346bce7d718e71d9d59cf4caae7be23126277f0a179d81efd9e1b73a8d5e74bed6c93df13e20eb43f239221ea7def82945fc782b7d9686c2efdfbf7bc2aedcc3bb07fe097bfdc4e0bccf4fb818b96d2500c53bc29e9e9f3908f3a9e2f630dfa1ed09143dfbc264a00c473d2162a03119ca227ffdc5d16422c8a22c7e12bf7c92078fb23c91861349f93c504692389224e9ff89f24464d880e82f8fc967e760ea73e4e225097f2f4c46a38178d3138c980893c1cd97f18dcc9a4b8ce25098485c258c85817473d3137e224f9848a228f604bd7dddfefa95389e284cc49eb0f2d8a4624f587758577158ee64288e799380900a939b9e709ba188b1b2f681309194b1a20c1459517ac292b29ec197f170301e7c19feee09f71f90d69bfedd13b4cb49b7bf7ee5714e7d4f98fc5bec893df10fae647664bea868d328fabc7ad396683a142fcb346d21a62db694be50d55a2a959d165bba459492facc91ca3243eb67ff075cafca25188321bcb43cf6a61ffeee099e9339c244f00f041afa716fc9536ae80ff0c75a7db6cd6374774b1686761b1b051819fa430ef42c5edc126868b7d08da699fd28c6b606a8866ea1a1a912880ee3b9ec259e1e4816529e5c59dc03191e40b419ddc9abbd3558eedd48c19e360e5df93ef3b6abc46dbf27b6793cfcd81e6f76d51a86a6425b1f3fdd6d37a2631ea131530b776027b6be7936f46f701dd7f3a9891baf3088ecc0927f423b1a1786ae86aebc7c766525b7b72b78d7cc790badb5ba00f23877a38d687c9b3eacd78cf61edaf226b7b7f3c0d3c785315b116bfb00bded1283427df66673c91aac24106d42435f059efe0d3aa6f2ece99bc0d6d4bd8dd427579632db5444500c177cad59bd97906a9030fe034bce025bfe39fa8ed42fe5be6f634356b05700d617de4576bed0bcdcde02680de6d8daaed8fa81a1331af56099cbd4323d6ccc989c21b4652cdbe6105aba12b8e606de692a744ce9e00ee6a2a5a99b9fe1015aa6121a7a295f4b53457b1b88f3e2004df921b7b6f398ad679912667db6a6fcbc8b972288706e1721b3879a86e937bed3d4f00e3fe460b02a1c5389176bfe4d002240e67280ddd9ed4b9a8d98dc3576b3192c38af3fa931db14ae76808ebea1400bbb3281464933aa9eb4e9d7bcc4ddaa7b103fc4df11b7b9764ce7eb8faa676d5763bef64c2c75a0812766c7f3673232664becea560ef4e993234f637b432b5d789ea151b6afc83395a7bb98dbb4c1e4b7d03cbe074b5313ae97d99230593bfa34b73535720706b45a3de7252d28f73f5353fbb575d7cc4641c39f2bcfff639b4b71fe4c180f7b2b22642e711f483c1d337be0eb30dff04c09bbf12a7123d0f587bd1525d81aac9e0d2d807ea18e2d2dcce745c86552cffffd8940eefbda2d9c174bc6437c810d56733f50431f1f3c1defdd684add59083d198b8ea686f676f904225c8e213570a307684718bbfaeaf9cceeb84d7e607791636ea83dbb6fecaae6ffa55d71bd8fe705a0866e27b6790cc1b3f465b72e6dcbd0c7c889364fded776df35ee7c47e5b3c509b55e77d4cc551c2abf16e16e7d5834fe3be0f6a1d77c7664f8d3d17f426bd61d5f424397f6b68ed9fc85a18f657b3b2f1c93cb5864f4b5ac4abc533188578aa18f23439fe6863ea520da04f62c6c746337fa7e6032725b7facf9065c9e1b6e4b9c2ed9aec3da3f06ce764556d59a8b66af6732d3e8c898d1458da1358fdf5123a7c6dfb8afa1db4646f362c96c98c9a58c2b5135e7f4427f93e7ff79d7df1a1e991f79b06be7ccc681bca1366af6ce7db2896db22db951adb33172108c372c2ee958744c1667ec3d403c9648aeb9c93d9dd967277ee812f6f4606fcfeee14267732d45c71ce7a0e031a1f1c3c5bac2004e73ff2afe331dd9d190cc795b7d627af6aa58c778363af3df69ea1ecc56892b2b81ab1f95261ee89b676b304fcab16185fdd3c21e6caad804a831cdc2bb685ad8058c4bec6dec83c539862509f7b58a86f961c7860210cf037f8dbdc5baf2078e0b4119bfd780d9600022eff9c726f3168f0cef289ccb2def0cd72ef03f3ec777543eebfedd9ae3796587e08963ceb732eebce1774615f732575e25cc6e0152f75eb4294084437b7b0f3d3dc055cc809ebe197a653c67362676657e197675e4d259bfc2a684636e711bdbf126b7065c47f1e20279bcbe6fa6d737f1466572fb78df5ddbb868df5c1fcdbea36901a2a9d2c5e20e6fa4b49d0a4b348ffb771917407a1aef39fda87abe8725918b401343b91ca5cb70c48e1468e898fb1390833d8857a4f40feee390cf559c62881d0d472d6e71df3dc38f567e1fc5eb0aaf79aceee81f32195571fcb95eb7ed7bf8db58d1d5f19da68a9699711e4afdd7b9d88ad86b55f4b72ab30986ada7f8a27f63d81259db0df53455b6cca364af4fb1849f09d6ef638937c3878f68da755acc71e3b01bb3586e42caf50eb09cf3d0f2f755ca3df348178f277ec573dcefa87c767086eff93b2a9f9dfed036edc0338f22f3affabdf547e6e3556ea98127a62fa6ff2ad6301f29e3c5598cabc65fb54f36c7fb71aea34796e7c9b77189350c2341c74ecfe88a2a5741cb4a6f06b71f161f17da7ce3e9983adb55c230a13c3bb1b35af93dcbdf8d994a2d13e7c6b7a43a4f3d402f9a528fc5472d38800867ec7b2fda3c2fd64695ebda813bdbe06e8e69209e63a216afe61fe598d095ade68c53ebd91da8dcae2df348fd7599bf18fa0a037959385bb5b67926b7466f353f06ea62d9bcb477f45efe39e738fc014dbb0e6a70317f25469636569f75cb58d97cfbc35424573f241556d63e769277f178fd955467a643d3cf65f3486a19b5795ae313a4e3bf9d3cf6a13a1b95d82a5be6a1cdd3e2526666019e18a6cc25112e8a532cecc45f3297392ebc8bb1a5dd9c9f8becc0fddaf84eb5efee99e8666f4c1fa0258f734f9f266e7ccfdfc1601530ccace6e6b973e70cc4650d98ed4dbb18aad698333234af7e8f9bd8aa2b926bce317822702e57efa8a951240c8febd8e3c69bcc8a36458d098ea988b6e9f16fabbde49e29217b6b54fbb8855634debbfa2670f9fcf3bd2b1fe2fa7b3ed6ca01b9f298dae6346f796bcf2f73b9ce791bdecabcec918d9531795e9f57f4695ef5e7fe1a34bcf0fde94cdfb7c88d37d4d58c065f1df350edd3768d88d3a16d73e651397e7d47a7794cbd8ff35cef04f3eab3782c2ef8af62a91f676d49abad5bf17ad7bb05664c1cefd2baf2196d5d571e8dc5f7cbcaca27497e94be4c949b8934f83c180e878a341adffc3765e52f4371f8cf959539e77fa9aa2c0e87525dff55c663451e0dc7d2cbaaf2cd581e8fc5f1a02915d77b7e59557e8ff4ef5695af5701af5701af5701af5701af5701af5701af5701af5701af5701af5701af5701af5701af5701af5701af5701ff97ef239d9562da6b48ae3e7eb2cc0374758c8caf6259369e2d9f2c734878a9fa918caaf21375e565e06a6ae06d2171e56378a7a9a9bd0d13e3abd8964a4d0b82c12abc8b97a2b59d8b40e23f911247de2877e5b5a684ffec610e9b6f0c4d1541bcc1edcf521b0ae49fed5c117e7eacaf1fe863e4e02cb5b7d85bac55d1d137797b4de51632be8cd9f1c6d01e72c0f845c1de8a1297adbf5d876d89d63c3edb6b75efea0f6d8992ffbc33a6b67e20d67633bcabfaeaab0ff5cff50fe691723e50480ddd0edcd9122faa329dab8f035b0b0e8e0c92ef4f7509b1bee635957c2d606b5243cfb0bf0ee18f87e6a78fc446b7c18bfdced4d496dedfefdb72abca95df82008853ea967c5143034ff3e236ad7998230b023d8bcda2d3bf11e18f4711ce651cbbd1b8b0d7e54f572e6caf7419fa98daed4f3798c9c1d07164cc96a2ad29cf9e3e2dbcd972eb6c5764c1d73ac079711fbfad370a4d99af3d323afb3666e2b9de12bb299797b6caf92fbf7dcdbe98cca15fa8a51d3c1238d714eacad3f04cbee3735932bebe1f2a3d96fb8a589fab05cc0f68d5575f39a8af9ba8ae7ee03c2dd607e80fc4e4ee3619b379b4e89858a85e9b7f8bfdd9cab4b60699cb52e098c378b10e3f2cd396653dff5ad7bbd6f5ae75bd6b5def5ad7bbd6f5ae75bd6b5def5ad7bbd6f5ae75bd6b5def5ad7bbd6f5ae75bdffa5badeefff0f0000ffff010000ffffe2d72497d44b0000`)))
```

## File: `doc-util/README.md`
```markdown
# doc-util

`doc-util` provides a Jsonnet interface for `docsonnet`,
 a Jsonnet API doc generator that uses structured data instead of comments.

## Install

```
jb install github.com/jsonnet-libs/docsonnet/doc-util@master
```

## Usage

```jsonnet
local d = import "github.com/jsonnet-libs/docsonnet/doc-util/main.libsonnet"
```


## Index

* [`fn arg(name, type, default, enums)`](#fn-arg)
* [`fn fn(help, args)`](#fn-fn)
* [`fn obj(help, fields)`](#fn-obj)
* [`fn pkg(name, url, help, filename="", version="master")`](#fn-pkg)
* [`fn render(obj)`](#fn-render)
* [`fn val(type, help, default)`](#fn-val)
* [`obj argument`](#obj-argument)
  * [`fn fromSchema(name, schema)`](#fn-argumentfromschema)
  * [`fn new(name, type, default, enums)`](#fn-argumentnew)
* [`obj func`](#obj-func)
  * [`fn new(help, args)`](#fn-funcnew)
  * [`fn withArgs(args)`](#fn-funcwithargs)
  * [`fn withHelp(help)`](#fn-funcwithhelp)
* [`obj object`](#obj-object)
  * [`fn new(help, fields)`](#fn-objectnew)
  * [`fn withFields(fields)`](#fn-objectwithfields)
* [`obj value`](#obj-value)
  * [`fn new(type, help, default)`](#fn-valuenew)
* [`obj T`](#obj-t)
* [`obj package`](#obj-package)
  * [`fn new(name, url, help, filename="", version="master")`](#fn-packagenew)
  * [`fn newSub(name, help)`](#fn-packagenewsub)

## Fields

### fn arg

```jsonnet
arg(name, type, default, enums)
```

PARAMETERS:

* **name** (`string`)
* **type** (`string`)
* **default** (`any`)
* **enums** (`array`)

`arg` is a shorthand for `argument.new`
### fn fn

```jsonnet
fn(help, args)
```

PARAMETERS:

* **help** (`string`)
* **args** (`array`)

`fn` is a shorthand for `func.new`
### fn obj

```jsonnet
obj(help, fields)
```

PARAMETERS:

* **help** (`string`)
* **fields** (`object`)

`obj` is a shorthand for `object.new`
### fn pkg

```jsonnet
pkg(name, url, help, filename="", version="master")
```

PARAMETERS:

* **name** (`string`)
* **url** (`string`)
* **help** (`string`)
* **filename** (`string`)
   - default value: `""`
* **version** (`string`)
   - default value: `"master"`

`new` is a shorthand for `package.new`
### fn render

```jsonnet
render(obj)
```

PARAMETERS:

* **obj** (`object`)

`render` converts the docstrings to human readable Markdown files.

Usage:

```jsonnet
// docs.jsonnet
d.render(import 'main.libsonnet')
```

Call with: `jsonnet -S -c -m docs/ docs.jsonnet`

### fn val

```jsonnet
val(type, help, default)
```

PARAMETERS:

* **type** (`string`)
* **help** (`string`)
* **default** (`any`)

`val` is a shorthand for `value.new`
### obj argument

Utilities for creating function arguments

#### fn argument.fromSchema

```jsonnet
argument.fromSchema(name, schema)
```

PARAMETERS:

* **name** (`string`)
* **schema** (`object`)

`fromSchema` creates a new function argument, taking a JSON `schema` to describe the type information for this argument.

Examples:

```jsonnet
[
  d.argument.fromSchema('foo', { type: 'string' }),
  d.argument.fromSchema('bar', { type: 'string', default='loo' }),
  d.argument.fromSchema('baz', { type: 'number', enum=[1,2,3] }),
]
```

#### fn argument.new

```jsonnet
argument.new(name, type, default, enums)
```

PARAMETERS:

* **name** (`string`)
* **type** (`string`)
* **default** (`any`)
* **enums** (`array`)

`new` creates a new function argument, taking the `name`, the `type`. Optionally it
can take a `default` value and `enum`-erate potential values.

Examples:

```jsonnet
[
  d.argument.new('foo', d.T.string),
  d.argument.new('bar', d.T.string, default='loo'),
  d.argument.new('baz', d.T.number, enums=[1,2,3]),
]
```

### obj func

Utilities for documenting Jsonnet methods (functions of objects)

#### fn func.new

```jsonnet
func.new(help, args)
```

PARAMETERS:

* **help** (`string`)
* **args** (`array`)

new creates a new function, optionally with description and arguments
#### fn func.withArgs

```jsonnet
func.withArgs(args)
```

PARAMETERS:

* **args** (`array`)

The `withArgs` modifier overrides the arguments of that function
#### fn func.withHelp

```jsonnet
func.withHelp(help)
```

PARAMETERS:

* **help** (`string`)

The `withHelp` modifier overrides the help text of that function
### obj object

Utilities for documenting Jsonnet objects (`{ }`).

#### fn object.new

```jsonnet
object.new(help, fields)
```

PARAMETERS:

* **help** (`string`)
* **fields** (`object`)

new creates a new object, optionally with description and fields
#### fn object.withFields

```jsonnet
object.withFields(fields)
```

PARAMETERS:

* **fields** (`object`)

The `withFields` modifier overrides the fields property of an already created object
### obj value

Utilities for documenting plain Jsonnet values (primitives)

#### fn value.new

```jsonnet
value.new(type, help, default)
```

PARAMETERS:

* **type** (`string`)
* **help** (`string`)
* **default** (`any`)

new creates a new object of given type, optionally with description and default value
### obj T

* `T.any` (`string`): `"any"` - argument of type "any"
* `T.array` (`string`): `"array"` - argument of type "array"
* `T.boolean` (`string`): `"bool"` - argument of type "boolean"
* `T.func` (`string`): `"function"` - argument of type "func"
* `T.null` (`string`): `"null"` - argument of type "null"
* `T.number` (`string`): `"number"` - argument of type "number"
* `T.object` (`string`): `"object"` - argument of type "object"
* `T.string` (`string`): `"string"` - argument of type "string"

### obj package


#### fn package.new

```jsonnet
package.new(name, url, help, filename="", version="master")
```

PARAMETERS:

* **name** (`string`)
* **url** (`string`)
* **help** (`string`)
* **filename** (`string`)
   - default value: `""`
* **version** (`string`)
   - default value: `"master"`

`new` creates a new package

Arguments:

* given `name`
* source `url` for jsonnet-bundler and the import
* `help` text
* `filename` for the import, defaults to blank for backward compatibility
* `version` for jsonnet-bundler install, defaults to `master` just like jsonnet-bundler

#### fn package.newSub

```jsonnet
package.newSub(name, help)
```

PARAMETERS:

* **name** (`string`)
* **help** (`string`)

`newSub` creates a package without the preconfigured install/usage templates.

Arguments:

* given `name`
* `help` text
```

## File: `doc-util/main.libsonnet`
```
{
  local d = self,

  '#':
    d.pkg(
      name='doc-util',
      url='github.com/jsonnet-libs/docsonnet/doc-util',
      help=|||
        `doc-util` provides a Jsonnet interface for `docsonnet`,
         a Jsonnet API doc generator that uses structured data instead of comments.
      |||,
      filename=std.thisFile,
    )
    + d.package.withUsageTemplate(
      'local d = import "%(import)s"'
    ),

  package:: {
    '#new':: d.fn(|||
      `new` creates a new package

      Arguments:

      * given `name`
      * source `url` for jsonnet-bundler and the import
      * `help` text
      * `filename` for the import, defaults to blank for backward compatibility
      * `version` for jsonnet-bundler install, defaults to `master` just like jsonnet-bundler
    |||, [
      d.arg('name', d.T.string),
      d.arg('url', d.T.string),
      d.arg('help', d.T.string),
      d.arg('filename', d.T.string, ''),
      d.arg('version', d.T.string, 'master'),
    ]),
    new(name, url, help, filename='', version='master')::
      {
        name: name,
        help:
          help
          + std.get(self, 'installTemplate', '') % self
          + std.get(self, 'usageTemplate', '') % self,
        'import':
          if filename != ''
          then url + '/' + filename
          else url,
        url: url,
        filename: filename,
        version: version,

      }
      + self.withInstallTemplate(
        'jb install %(url)s@%(version)s'
      )
      + self.withUsageTemplate(
        'local %(name)s = import "%(import)s"'
      ),

    '#newSub':: d.fn(|||
      `newSub` creates a package without the preconfigured install/usage templates.

      Arguments:

      * given `name`
      * `help` text
    |||, [
      d.arg('name', d.T.string),
      d.arg('help', d.T.string),
    ]),
    newSub(name, help)::
      {
        name: name,
        help: help,
      },

    withInstallTemplate(template):: {
      installTemplate:
        if template != null
        then
          |||

            ## Install

            ```
            %s
            ```
          ||| % template
        else '',
    },

    withUsageTemplate(template):: {
      usageTemplate:
        if template != null
        then
          |||

            ## Usage

            ```jsonnet
            %s
            ```
          ||| % template
        else '',
    },
  },

  '#pkg':: self.package['#new'] + d.func.withHelp('`new` is a shorthand for `package.new`'),
  pkg:: self.package.new,

  '#object': d.obj('Utilities for documenting Jsonnet objects (`{ }`).'),
  object:: {
    '#new': d.fn('new creates a new object, optionally with description and fields', [d.arg('help', d.T.string), d.arg('fields', d.T.object)]),
    new(help='', fields={}):: { object: {
      help: help,
      fields: fields,
    } },

    '#withFields': d.fn('The `withFields` modifier overrides the fields property of an already created object', [d.arg('fields', d.T.object)]),
    withFields(fields):: { object+: {
      fields: fields,
    } },
  },

  '#obj': self.object['#new'] + d.func.withHelp('`obj` is a shorthand for `object.new`'),
  obj:: self.object.new,

  '#func': d.obj('Utilities for documenting Jsonnet methods (functions of objects)'),
  func:: {
    '#new': d.fn('new creates a new function, optionally with description and arguments', [d.arg('help', d.T.string), d.arg('args', d.T.array)]),
    new(help='', args=[]):: { 'function': {
      help: help,
      args: args,
    } },

    '#withHelp': d.fn('The `withHelp` modifier overrides the help text of that function', [d.arg('help', d.T.string)]),
    withHelp(help):: { 'function'+: {
      help: help,
    } },

    '#withArgs': d.fn('The `withArgs` modifier overrides the arguments of that function', [d.arg('args', d.T.array)]),
    withArgs(args):: { 'function'+: {
      args: args,
    } },
  },

  '#fn': self.func['#new'] + d.func.withHelp('`fn` is a shorthand for `func.new`'),
  fn:: self.func.new,

  '#argument': d.obj('Utilities for creating function arguments'),
  argument:: {
    '#new': d.fn(|||
      `new` creates a new function argument, taking the `name`, the `type`. Optionally it
      can take a `default` value and `enum`-erate potential values.

      Examples:

      ```jsonnet
      [
        d.argument.new('foo', d.T.string),
        d.argument.new('bar', d.T.string, default='loo'),
        d.argument.new('baz', d.T.number, enums=[1,2,3]),
      ]
      ```
    |||, [
      d.arg('name', d.T.string),
      d.arg('type', d.T.string),
      d.arg('default', d.T.any),
      d.arg('enums', d.T.array),
    ]),
    new(name, type, default=null, enums=null): {
      name: name,
      type: type,
      default: default,
      enums: enums,
    },
    '#fromSchema': d.fn(|||
      `fromSchema` creates a new function argument, taking a JSON `schema` to describe the type information for this argument.

      Examples:

      ```jsonnet
      [
        d.argument.fromSchema('foo', { type: 'string' }),
        d.argument.fromSchema('bar', { type: 'string', default='loo' }),
        d.argument.fromSchema('baz', { type: 'number', enum=[1,2,3] }),
      ]
      ```
    |||, [
      d.arg('name', d.T.string),
      d.arg('schema', d.T.object),
    ]),
    fromSchema(name, schema): {
      name: name,
      schema: schema,
    },
  },
  '#arg': self.argument['#new'] + self.func.withHelp('`arg` is a shorthand for `argument.new`'),
  arg:: self.argument.new,

  '#value': d.obj('Utilities for documenting plain Jsonnet values (primitives)'),
  value:: {
    '#new': d.fn('new creates a new object of given type, optionally with description and default value', [d.arg('type', d.T.string), d.arg('help', d.T.string), d.arg('default', d.T.any)]),
    new(type, help='', default=null): { value: {
      help: help,
      type: type,
      default: default,
    } },
  },
  '#val': self.value['#new'] + self.func.withHelp('`val` is a shorthand for `value.new`'),
  val:: self.value.new,

  // T contains constants for the Jsonnet types
  T:: {
    '#string': d.val(d.T.string, 'argument of type "string"'),
    string: 'string',

    '#number': d.val(d.T.string, 'argument of type "number"'),
    number: 'number',
    int: self.number,
    integer: self.number,

    '#boolean': d.val(d.T.string, 'argument of type "boolean"'),
    boolean: 'bool',
    bool: self.boolean,

    '#object': d.val(d.T.string, 'argument of type "object"'),
    object: 'object',

    '#array': d.val(d.T.string, 'argument of type "array"'),
    array: 'array',

    '#any': d.val(d.T.string, 'argument of type "any"'),
    any: 'any',

    '#null': d.val(d.T.string, 'argument of type "null"'),
    'null': 'null',
    nil: self['null'],

    '#func': d.val(d.T.string, 'argument of type "func"'),
    func: 'function',
    'function': self.func,
  },

  '#render': d.fn(
    |||
      `render` converts the docstrings to human readable Markdown files.

      Usage:

      ```jsonnet
      // docs.jsonnet
      d.render(import 'main.libsonnet')
      ```

      Call with: `jsonnet -S -c -m docs/ docs.jsonnet`
    |||,
    args=[
      d.arg('obj', d.T.object),
    ]
  ),
  render:: (import './render.libsonnet').render,

}
```

## File: `doc-util/render.libsonnet`
```
{
  local root = self,

  render(obj):
    assert std.isObject(obj) && '#' in obj : 'error: object is not a docsonnet package';
    local package = self.package(obj);
    package.toFiles(),

  findPackages(obj, path=[]): {
    local find(obj, path, parentWasPackage=true) =
      std.foldl(
        function(acc, k)
          acc
          + (
            // If matches a package but warn if also has an object docstring
            if '#' in obj[k] && '#' + k in obj
               && !std.objectHasAll(obj[k]['#'], 'ignore')
            then std.trace(
              'warning: %s both defined as object and package' % k,
              [root.package(obj[k], path + [k], parentWasPackage)]
            )
            // If matches a package, return it
            else if '#' in obj[k]
                    && !std.objectHasAll(obj[k]['#'], 'ignore')
            then [root.package(obj[k], path + [k], parentWasPackage)]
            // If not, keep looking
            else find(obj[k], path + [k], parentWasPackage=false)
          ),
        std.filter(
          function(k)
            !std.startsWith(k, '#')
            && std.isObject(obj[k]),
          std.objectFieldsAll(obj)
        ),
        []
      ),

    packages: find(obj, path),

    hasPackages(): std.length(self.packages) > 0,

    toIndex(relativeTo=[]):
      if self.hasPackages()
      then
        std.join('\n', [
          '* ' + p.link(relativeTo)
          for p in self.packages
        ])
        + '\n'
      else '',

    toFiles():
      std.foldl(
        function(acc, p)
          acc
          + { [p.path]: p.toString() }
          + p.packages.toFiles(),
        self.packages,
        {}
      ),
  },

  package(obj, path=[], parentWasPackage=true): {
    local this = self,
    local doc = obj['#'],

    packages: root.findPackages(obj, path),
    fields: root.fields(obj),

    local pathsuffix =
      (if self.packages.hasPackages()
       then '/index.md'
       else '.md'),

    // filepath on disk
    path:
      std.join('/', path)
      + pathsuffix,

    link(relativeTo):
      local relativepath = root.util.getRelativePath(path, relativeTo);
      '[%s](%s)' % [
        std.join('.', relativepath),
        std.join('/', relativepath)
        + pathsuffix,
      ],

    toFiles():
      { 'README.md': this.toString() }
      + self.packages.toFiles(),

    toString():
      std.join(
        '\n',
        [
          '# ' + doc.name + '\n',
          std.get(doc, 'help', ''),
          '',
        ]
        + (if self.packages.hasPackages()
           then [
             '## Subpackages\n\n'
             + self.packages.toIndex(path),
           ]
           else [])
        + (if self.fields.hasFields()
           then [
             '## Index\n\n'
             + self.fields.toIndex()
             + '\n## Fields\n'
             + self.fields.toString(),
           ]
           else [])
      ),
  },

  fields(obj, path=[]): {
    values: root.findValues(obj, path),
    functions: root.findFunctions(obj, path),
    objects: root.findObjects(obj, path),

    hasFields():
      std.any([
        self.values.hasFields(),
        self.functions.hasFields(),
        self.objects.hasFields(),
      ]),

    toIndex():
      std.join('', [
        self.functions.toIndex(),
        self.objects.toIndex(),
      ]),

    toString():
      std.join('', [
        self.values.toString(),
        self.functions.toString(),
        self.objects.toString(),
      ]),
  },

  findObjects(obj, path=[]): {
    local keys =
      std.filter(
        root.util.filter('object', obj),
        std.objectFieldsAll(obj)
      ),

    local undocumentedKeys =
      std.filter(
        function(k)
          std.all([
            !std.startsWith(k, '#'),
            std.isObject(obj[k]),
            !std.objectHasAll(obj[k], 'ignore'),
            !('#' + k in obj),  // not documented in parent
            !('#' in obj[k]),  // not a sub package
          ]),
        std.objectFieldsAll(obj)
      ),

    objects:
      std.foldl(
        function(acc, k)
          acc + [
            root.obj(
              root.util.realkey(k),
              obj[k],
              obj[root.util.realkey(k)],
              path,
            ),
          ],
        keys,
        []
      )
      + std.foldl(
        function(acc, k)
          local o = root.obj(
            k,
            { object: { help: '' } },
            obj[k],
            path,
          );
          acc
          + (if o.fields.hasFields()
             then [o]
             else []),
        undocumentedKeys,
        []
      ),

    hasFields(): std.length(self.objects) > 0,

    toIndex():
      if self.hasFields()
      then
        std.join('', [
          std.join(
            '',
            [' ' for d in std.range(0, (std.length(path) * 2) - 1)]
            + ['* ', f.link]
            + ['\n']
            + (if f.fields.hasFields()
               then [f.fields.toIndex()]
               else [])
          )
          for f in self.objects
        ])
      else '',

    toString():
      if self.hasFields()
      then
        std.join('', [
          o.toString()
          for o in self.objects
        ])
      else '',
  },

  obj(name, doc, obj, path): {
    fields: root.fields(obj, path + [name]),

    path: std.join('.', path + [name]),
    fragment: root.util.fragment(std.join('', path + [name])),
    link: '[`obj %s`](#obj-%s)' % [name, self.fragment],

    toString():
      std.join(
        '\n',
        [root.util.title('obj ' + self.path, std.length(path) + 2)]
        + (if std.get(doc.object, 'help', '') != ''
           then [doc.object.help]
           else [])
        + [self.fields.toString()]
      ),
  },

  findFunctions(obj, path=[]): {
    local keys =
      std.filter(
        root.util.filter('function', obj),
        std.objectFieldsAll(obj)
      ),

    functions:
      std.foldl(
        function(acc, k)
          acc + [
            root.func(
              root.util.realkey(k),
              obj[k],
              path,
            ),
          ],
        keys,
        []
      ),

    hasFields(): std.length(self.functions) > 0,

    toIndex():
      if self.hasFields()
      then
        std.join('', [
          std.join(
            '',
            [' ' for d in std.range(0, (std.length(path) * 2) - 1)]
            + ['* ', f.link]
            + ['\n']
          )
          for f in self.functions
        ])
      else '',

    toString():
      if self.hasFields()
      then
        std.join('', [
          f.toString()
          for f in self.functions
        ])
      else '',
  },

  func(name, doc, path): {
    path: std.join('.', path + [name]),
    fragment: root.util.fragment(std.join('', path + [name])),
    link: '[`fn %s(%s)`](#fn-%s)' % [name, self.args, self.fragment],

    local getType(arg) =
      local type =
        if 'schema' in arg
        then std.get(arg.schema, 'type', '')
        else std.get(arg, 'type', '');
      if std.isArray(type)
      then std.join(',', ['`%s`' % t for t in std.set(type)])
      else '`%s`' % type,

    // Use BelRune as default can be 'null' as a value. Only supported for arg.schema, arg.default didn't support this, not sure how to support without breaking asssumptions downstream.
    local BelRune = std.char(7),
    local getDefault(arg) =
      if 'schema' in arg
      then std.get(arg.schema, 'default', BelRune)
      else
        local d = std.get(arg, 'default', BelRune);
        if d == null
        then BelRune
        else d,

    local getEnum(arg) =
      if 'schema' in arg
      then std.get(arg.schema, 'enum', [])
      else
        local d = std.get(arg, 'enums', []);
        if d == null
        then []
        else d,

    local manifest(value) =
      std.manifestJsonEx(value, '', '', ': '),

    args:
      std.join(', ', [
        local default = getDefault(arg);
        if default != BelRune
        then std.join('=', [
          arg.name,
          manifest(default),
        ])
        else arg.name
        for arg in doc['function'].args
      ]),


    args_list:
      if std.length(doc['function'].args) > 0
      then
        '\nPARAMETERS:\n\n'
        + std.join('\n', [
          '* **%s** (%s)' % [arg.name, getType(arg)]
          + (
            local default = getDefault(arg);
            if default != BelRune
            then '\n   - default value: `%s`' % manifest(default)
            else ''
          )
          + (
            local enum = getEnum(arg);
            if enum != []
            then
              '\n   - valid values: %s' %
              std.join(', ', [
                '`%s`' % manifest(item)
                for item in enum
              ])
            else ''
          )
          for arg in doc['function'].args
        ])
      else '',

    toString():
      std.join('\n', [
        root.util.title('fn ' + self.path, std.length(path) + 2),
        |||
          ```jsonnet
          %s(%s)
          ```
          %s
        ||| % [self.path, self.args, self.args_list],
        std.get(doc['function'], 'help', ''),
      ]),
  },

  findValues(obj, path=[]): {
    local keys =
      std.filter(
        root.util.filter('value', obj),
        std.objectFieldsAll(obj)
      ),

    values:
      std.foldl(
        function(acc, k)
          acc + [
            root.val(
              root.util.realkey(k),
              obj[k],
              obj[root.util.realkey(k)],
              path,
            ),
          ],
        keys,
        []
      ),

    hasFields(): std.length(self.values) > 0,

    toString():
      if self.hasFields()
      then
        std.join('\n', [
          '* ' + f.toString()
          for f in self.values
        ]) + '\n'
      else '',
  },

  val(name, doc, obj, path): {
    toString():
      std.join(' ', [
        '`%s`' % std.join('.', path + [name]),
        '(`%s`):' % doc.value.type,
        '`"%s"`' % obj,
        '-',
        std.get(doc.value, 'help', ''),
      ]),
  },

  util: {
    realkey(key):
      assert std.startsWith(key, '#') : 'Key %s not a docstring key' % key;
      key[1:],
    title(title, depth=0):
      std.join(
        '',
        ['\n']
        + ['#' for i in std.range(0, depth)]
        + [' ', title, '\n']
      ),
    fragment(title):
      std.asciiLower(
        std.strReplace(
          std.strReplace(title, '.', '')
          , ' ', '-'
        )
      ),
    filter(type, obj):
      function(k)
        std.all([
          std.startsWith(k, '#'),
          std.isObject(obj[k]),
          !std.objectHasAll(obj[k], 'ignore'),
          type in obj[k],
          root.util.realkey(k) in obj,
        ]),

    getRelativePath(path, relativeTo):
      local shortest = std.min(std.length(relativeTo), std.length(path));

      local commonIndex =
        std.foldl(
          function(acc, i) (
            if acc.stop
            then acc
            else
              acc + {
                // stop count if path diverges
                local stop = relativeTo[i] != path[i],
                stop: stop,
                count+: if stop then 0 else 1,
              }
          ),
          std.range(0, shortest - 1),
          { stop: false, count: 0 }
        ).count;

      local _relativeTo = relativeTo[commonIndex:];
      local _path = path[commonIndex:];

      // prefix for relative difference
      local prefix = ['..' for i in std.range(0, std.length(_relativeTo) - 1)];

      // return path with prefix
      prefix + _path,
  },
}
```

## File: `pkg/docsonnet/fast.go`
```go
package docsonnet

import (
	"fmt"
	"log"
	"strings"
)

// load docsonnet
//
// Data assumptions:
// - only map[string]interface{} and fields
// - fields (#...) coming first
func fastLoad(d ds) Package {
	pkg := d.Package()

	pkg.API = make(Fields)
	pkg.Sub = make(map[string]Package)

	for k, v := range d {
		if k == "#" {
			continue
		}

		n := strings.TrimPrefix(k, "#")
		f := v.(map[string]interface{})

		// is it a docstring?
		if strings.HasPrefix(k, "#") {
			pkg.API[n] = loadField(n, f, d)
			continue
		}

		// is it a package?
		if _, ok := f["#"]; ok {
			p := fastLoad(ds(f))
			pkg.Sub[p.Name] = p
			continue
		}

		// is it a regular field? check nested...
		if nested, ok := loadNested(n, f); ok && !hasDocstring(n, d) {
			pkg.API[n] = *nested
		}
	}

	return pkg
}

func hasDocstring(key string, msi map[string]interface{}) bool {
	_, ok := msi["#"+key]
	return ok
}

func loadNested(name string, msi map[string]interface{}) (*Field, bool) {
	out := Object{
		Name:   name,
		Fields: make(Fields),
	}

	for k, v := range msi {
		n := strings.TrimPrefix(k, "#")
		f := v.(map[string]interface{})

		// is it a docstring?
		if strings.HasPrefix(k, "#") {
			out.Fields[n] = loadField(n, f, msi)
			continue
		}

		// is it a regular field? check nested...
		if nested, ok := loadNested(n, f); ok && !hasDocstring(n, msi) {
			out.Fields[n] = *nested
		}
	}

	return &Field{Object: &out}, true
}

func loadField(name string, field map[string]interface{}, parent map[string]interface{}) Field {
	if ifn, ok := field["function"]; ok {
		return loadFn(name, ifn.(map[string]interface{}))
	}

	if iobj, ok := field["object"]; ok {
		return loadObj(name, iobj.(map[string]interface{}), parent)
	}

	if vobj, ok := field["value"]; ok {
		return loadValue(name, vobj.(map[string]interface{}))
	}

	panic(fmt.Sprintf("field %s lacking {function | object | value}", name))
}

func loadValue(name string, msi map[string]interface{}) Field {
	h, ok := msi["help"].(string)
	if !ok {
		h = ""
	}

	t, ok := msi["type"].(string)
	if !ok {
		panic(fmt.Sprintf("value %s lacking type information", name))
	}

	v := Value{
		Name:    name,
		Help:    h,
		Type:    Type(t),
		Default: msi["default"],
	}

	return Field{Value: &v}
}

func loadFn(name string, msi map[string]interface{}) Field {
	h, ok := msi["help"].(string)
	if !ok {
		h = ""
	}
	fn := Function{
		Name: name,
		Help: h,
	}
	if args, ok := msi["args"]; ok {
		fn.Args = loadArgs(args.([]interface{}))
	}
	return Field{Function: &fn}
}

func loadArgs(is []interface{}) []Argument {
	args := make([]Argument, len(is))
	for i := range is {
		arg := is[i].(map[string]interface{})
		args[i] = Argument{
			Name:    arg["name"].(string),
			Type:    Type(arg["type"].(string)),
			Default: arg["default"],
		}
	}
	return args
}

func fieldNames(msi map[string]interface{}) []string {
	out := make([]string, 0, len(msi))
	for k := range msi {
		out = append(out, k)
	}
	return out
}

func loadObj(name string, msi map[string]interface{}, parent map[string]interface{}) Field {
	obj := Object{
		Name:   name,
		Help:   msi["help"].(string),
		Fields: make(Fields),
	}

	// look for children in same key
	var iChilds interface{}
	var ok bool
	if iChilds, ok = parent[name]; !ok {
		fmt.Println("aborting, no", name, strings.Join(fieldNames(parent), ", "))
		return Field{Object: &obj}
	}

	childs := iChilds.(map[string]interface{})
	if nested, ok := loadNested(name, childs); ok {
		obj.Fields = nested.Object.Fields
	}

	return Field{Object: &obj}
}

type ds map[string]interface{}

func (d ds) Package() Package {
	hash, ok := d["#"]
	if !ok {
		log.Fatalln("Package declaration missing")
	}

	pkg := hash.(map[string]interface{})
	return Package{
		Help:   pkg["help"].(string),
		Name:   pkg["name"].(string),
		Import: pkg["import"].(string),
	}
}
```

## File: `pkg/docsonnet/field.go`
```go
package docsonnet

import (
	"encoding/json"
	"errors"
)

// Field represents any field of an object.
type Field struct {
	// Function value
	Function *Function `json:"function,omitempty"`
	// Object value
	Object *Object `json:"object,omitempty"`
	// Any other value
	Value *Value `json:"value,omitempty"`
}

func (o *Field) UnmarshalJSON(data []byte) error {
	type fake Field

	var f fake
	if err := json.Unmarshal(data, &f); err != nil {
		return err
	}

	switch {
	case f.Function != nil:
		o.Function = f.Function
	case f.Object != nil:
		o.Object = f.Object
	case f.Value != nil:
		o.Value = f.Value
	default:
		return errors.New("field has no value")
	}

	return nil
}

func (o Field) MarshalJSON() ([]byte, error) {
	if o.Function == nil && o.Object == nil && o.Value == nil {
		return nil, errors.New("field has no value")
	}

	type fake Field
	return json.Marshal(fake(o))
}

// Fields is a list of fields
type Fields map[string]Field

func (fPtr *Fields) UnmarshalJSON(data []byte) error {
	if *fPtr == nil {
		*fPtr = make(Fields)
	}
	f := *fPtr

	tmp := make(map[string]Field)
	if err := json.Unmarshal(data, &tmp); err != nil {
		return err
	}

	for k, v := range tmp {
		switch {
		case v.Function != nil:
			v.Function.Name = k
		case v.Object != nil:
			v.Object.Name = k
		case v.Value != nil:
			v.Value.Name = k
		}
		f[k] = v
	}

	return nil
}
```

## File: `pkg/docsonnet/field_test.go`
```go
package docsonnet

import (
	"encoding/json"
	"testing"

	"github.com/google/go-cmp/cmp"
)

func TestRemarshal(t *testing.T) {
	o := Object{
		Help: "grafana.libsonnet is the offical Jsonnet library for Grafana",
		Fields: map[string]Field{
			"new": {Function: &Function{
				Name: "new",
				Help: "new returns Grafana resources with sane defaults",
			}},
			"addConfig": {Function: &Function{
				Name: "addConfig",
				Help: "addConfig adds config entries to grafana.ini",
			}},
			"datasource": {Object: &Object{
				Name: "datasource",
				Help: "ds-util makes creating datasources easy",
				Fields: map[string]Field{
					"new": {Function: &Function{
						Name: "new",
						Help: "new creates a new datasource",
					}},
				},
			}},
		},
	}

	data, err := json.Marshal(o)
	if err != nil {
		t.Fatal(err)
	}

	var got Object
	if err := json.Unmarshal(data, &got); err != nil {
		t.Fatal(err)
	}

	if str := cmp.Diff(o, got); str != "" {
		t.Fatal(str)
	}
}
```

## File: `pkg/docsonnet/load.go`
```go
package docsonnet

import (
	"encoding/json"
	"fmt"
	"io"
	"log"

	"github.com/google/go-jsonnet"
	"github.com/markbates/pkger"
)

type Opts struct {
	JPath []string
}

// Load extracts and transforms the docsonnet data in `filename`, returning the
// top level docsonnet package.
func Load(filename string, opts Opts) (*Package, error) {
	data, err := Extract(filename, opts)
	if err != nil {
		return nil, err
	}

	return Transform([]byte(data))
}

// Extract parses the Jsonnet file at `filename`, extracting all docsonnet related
// information, exactly as they appear in Jsonnet. Keep in mind this
// representation is usually not suitable for any use, use `Transform` to
// convert it to the familiar docsonnet data model.
func Extract(filename string, opts Opts) ([]byte, error) {
	// get load.libsonnet from embedded data
	file, err := pkger.Open("/load.libsonnet")
	if err != nil {
		return nil, err
	}
	load, err := io.ReadAll(file)
	if err != nil {
		return nil, err
	}

	// setup Jsonnet vm
	vm := jsonnet.MakeVM()
	importer, err := newImporter(opts.JPath)
	if err != nil {
		return nil, err
	}
	vm.Importer(importer)

	// invoke load.libsonnet
	vm.ExtCode("main", fmt.Sprintf(`(import "%s")`, filename))

	data, err := vm.EvaluateAnonymousSnippet("load.libsonnet", string(load))
	if err != nil {
		return nil, err
	}

	return []byte(data), nil
}

// Transform converts the raw result of `Extract` to the actual docsonnet object
// model `*docsonnet.Package`.
func Transform(data []byte) (*Package, error) {
	var d ds
	if err := json.Unmarshal([]byte(data), &d); err != nil {
		log.Fatalln(err)
	}

	p := fastLoad(d)
	return &p, nil
}

// importer wraps jsonnet.FileImporter, to statically provide load.libsonnet,
// bundled with the binary
type importer struct {
	fi   jsonnet.FileImporter
	util jsonnet.Contents
}

func newImporter(paths []string) (*importer, error) {
	file, err := pkger.Open("/doc-util/main.libsonnet")
	if err != nil {
		return nil, err
	}
	load, err := io.ReadAll(file)
	if err != nil {
		return nil, err
	}

	return &importer{
		fi:   jsonnet.FileImporter{JPaths: paths},
		util: jsonnet.MakeContents(string(load)),
	}, nil
}

var docUtilPaths = []string{
	"doc-util/main.libsonnet",
	"github.com/jsonnet-libs/docsonnet/doc-util/main.libsonnet",
}

func (i *importer) Import(importedFrom, importedPath string) (contents jsonnet.Contents, foundAt string, err error) {
	for _, p := range docUtilPaths {
		if importedPath == p {
			return i.util, "<internal>", nil
		}
	}

	return i.fi.Import(importedFrom, importedPath)
}
```

## File: `pkg/docsonnet/model.go`
```go
package docsonnet

// Package represents a Jsonnet package, having an API (list of Fields) and
// perhaps subpackages
type Package struct {
	Name   string `json:"name"`
	Import string `json:"import"`
	Help   string `json:"help"`

	API Fields             `json:"api,omitempty"`
	Sub map[string]Package `json:"sub,omitempty"`
}

// Object represents a Jsonnet object, a list of key-value fields
type Object struct {
	Name string `json:"-"`
	Help string `json:"help"`

	// children
	Fields Fields `json:"fields"`
}

// Function represents a Jsonnet function, a named construct that takes
// arguments
type Function struct {
	Name string `json:"-"`
	Help string `json:"help"`

	Args []Argument `json:"args,omitempty"`
}

// Argument is a function argument, optionally also having a default value
type Argument struct {
	Type    Type        `json:"type"`
	Name    string      `json:"name"`
	Default interface{} `json:"default"`
}

// Value is a value of any other type than the special Object and Function types
type Value struct {
	Name string `json:"-"`
	Help string `json:"help"`

	Type    Type        `json:"type"`
	Default interface{} `json:"default"`
}

// Type is a Jsonnet type
type Type string

const (
	TypeString = "string"
	TypeNumber = "number"
	TypeBool   = "boolean"
	TypeObject = "object"
	TypeArray  = "array"
	TypeAny    = "any"
	TypeFunc   = "function"
)
```

## File: `pkg/md/md.go`
```go
package md

import (
	"fmt"
	"strings"

	"gopkg.in/yaml.v2"
)

type Elem interface {
	String() string
}

type JoinType struct {
	elems []Elem
	with  string
}

func (p JoinType) String() string {
	s := ""
	for _, e := range p.elems {
		s += p.with + e.String()
	}
	return strings.TrimPrefix(s, p.with)
}

func Paragraph(elems ...Elem) JoinType {
	return JoinType{elems: elems, with: " "}
}

func Doc(elems ...Elem) JoinType {
	return JoinType{elems: elems, with: "\n\n"}
}

type TextType struct {
	content string
}

func (t TextType) String() string {
	return t.content
}

func Text(text string) TextType {
	return TextType{content: text}
}

type HeadlineType struct {
	level   int
	content string
}

func (h HeadlineType) String() string {
	return strings.Repeat("#", h.level) + " " + h.content
}

func Headline(level int, content string) HeadlineType {
	return HeadlineType{
		level:   level,
		content: content,
	}
}

type SurroundType struct {
	body     Elem
	surround string
}

func (s SurroundType) String() string {
	return s.surround + s.body.String() + s.surround
}

func Bold(e Elem) SurroundType {
	return SurroundType{body: e, surround: "**"}
}

func Italic(e Elem) SurroundType {
	return SurroundType{body: e, surround: "*"}
}

func Code(e Elem) SurroundType {
	return SurroundType{body: e, surround: "`"}
}

type CodeBlockType struct {
	lang    string
	snippet string
}

func (c CodeBlockType) String() string {
	return fmt.Sprintf("```%s\n%s\n```", c.lang, c.snippet)
}

func CodeBlock(lang, snippet string) CodeBlockType {
	return CodeBlockType{lang: lang, snippet: snippet}
}

type ListType struct {
	elems []Elem
}

func (l ListType) String() string {
	s := ""
	for _, e := range l.elems {
		switch t := e.(type) {
		case ListType:
			s += "\n  " + strings.Join(strings.Split(t.String(), "\n"), "\n  ")
		default:
			s += "\n* " + t.String()
		}
	}
	return strings.TrimPrefix(s, "\n")
}

func List(elems ...Elem) ListType {
	return ListType{elems: elems}
}

type LinkType struct {
	desc Elem
	href string
}

func (l LinkType) String() string {
	return fmt.Sprintf("[%s](%s)", l.desc.String(), l.href)
}

func Link(desc Elem, href string) LinkType {
	return LinkType{
		desc: desc,
		href: href,
	}
}

type FrontmatterType struct {
	yaml string
}

func (f FrontmatterType) String() string {
	return "---\n" + f.yaml + "---"
}

func Frontmatter(data map[string]interface{}) FrontmatterType {
	d, err := yaml.Marshal(data)
	if err != nil {
		panic(err)
	}

	return FrontmatterType{yaml: string(d)}
}
```

## File: `pkg/md/md_test.go`
```go
package md

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestList(t *testing.T) {
	l := List(
		Text("foo"),
		Text("bar"),
		List(
			Text("baz"),
			Text("bing"),
		),
		Text("boing"),
	).String()

	assert.Equal(t, `* foo
* bar
  * baz
  * bing
* boing`, l)
}
```

## File: `pkg/render/fs.go`
```go
package render

import (
	"os"
	"path/filepath"

	"github.com/jsonnet-libs/docsonnet/pkg/docsonnet"
)

func To(pkg docsonnet.Package, dir string, opts Opts) (int, error) {
	if err := os.MkdirAll(dir, os.ModePerm); err != nil {
		return 0, err
	}

	data := Render(pkg, opts)

	n := 0
	for k, v := range data {
		fullpath := filepath.Join(dir, k)
		dir := filepath.Dir(fullpath)
		if err := os.MkdirAll(dir, os.ModePerm); err != nil {
			return n, err
		}
		if err := os.WriteFile(fullpath, []byte(v), 0644); err != nil {
			return n, err
		}
		n++
	}

	return n, nil
}
```

## File: `pkg/render/render.go`
```go
package render

import (
	"encoding/json"
	"fmt"
	"path"
	"sort"
	"strings"

	"github.com/google/go-jsonnet/formatter"
	"github.com/jsonnet-libs/docsonnet/pkg/docsonnet"
	"github.com/jsonnet-libs/docsonnet/pkg/md"
	"github.com/jsonnet-libs/docsonnet/pkg/slug"
)

type Opts struct {
	URLPrefix string
}

func Render(pkg docsonnet.Package, opts Opts) map[string]string {
	return render(pkg, nil, true, opts.URLPrefix)
}

func render(pkg docsonnet.Package, parents []string, root bool, urlPrefix string) map[string]string {
	link := path.Join("/", urlPrefix, strings.Join(append(parents, pkg.Name), "/"))
	if root {
		link = path.Join("/", urlPrefix)
	}
	if !strings.HasSuffix(link, "/") {
		link = link + "/"
	}

	// head
	elems := []md.Elem{
		md.Frontmatter(map[string]interface{}{
			"permalink": link,
		}),
		md.Headline(1, strings.Join(append(parents, pkg.Name), ".")),
	}
	if pkg.Import != "" {
		elems = append(elems, md.CodeBlock("jsonnet", fmt.Sprintf(`local %s = import "%s"`, pkg.Name, pkg.Import)))
	}
	elems = append(elems, md.Text(pkg.Help))

	if len(pkg.Sub) > 0 {
		keys := make([]string, 0, len(pkg.Sub))
		for _, s := range pkg.Sub {
			keys = append(keys, s.Name)
		}
		sort.Strings(keys)

		var items []md.Elem
		for _, k := range keys {
			s := pkg.Sub[k]

			link := s.Name + ".md"
			if len(s.Sub) > 0 {
				link = s.Name + "/index.md"
			}
			items = append(items, md.Link(md.Text(s.Name), link))
		}

		elems = append(elems, md.List(items...))
	}

	// fields of this package
	if len(pkg.API) > 0 {
		// index
		elems = append(elems,
			md.Headline(2, "Index"),
			md.List(renderIndex(pkg.API, "", slug.New())...),
		)

		// api
		elems = append(elems, md.Headline(2, "Fields"))
		elems = append(elems, renderApi(pkg.API, "")...)
	}

	content := md.Doc(elems...).String()
	key := strings.Join(append(parents, pkg.Name+".md"), "/")
	if len(pkg.Sub) > 0 {
		key = strings.Join(append(parents, pkg.Name+"/index.md"), "/")
	}
	if root {
		key = "README.md"
	}
	out := map[string]string{
		key: content,
	}

	if len(pkg.Sub) != 0 {
		for _, s := range pkg.Sub {
			path := append(parents, pkg.Name)
			if root {
				path = parents
			}
			got := render(s, path, false, urlPrefix)
			for k, v := range got {
				out[k] = v
			}
		}
	}

	return out
}

func renderIndex(api docsonnet.Fields, path string, s *slug.Slugger) []md.Elem {
	var elems []md.Elem
	for _, k := range sortFields(api) {
		v := api[k]
		switch {
		case v.Function != nil:
			fn := v.Function
			name := md.Text(fmt.Sprintf("fn %s(%s)", fn.Name, renderParams(fn.Args)))
			link := "#" + s.Slug("fn "+path+fn.Name)
			elems = append(elems, md.Link(md.Code(name), link))
		case v.Object != nil:
			obj := v.Object
			name := md.Text("obj " + path + obj.Name)
			link := "#" + s.Slug("obj "+path+obj.Name)
			elems = append(elems, md.Link(md.Code(name), link))
			elems = append(elems, md.List(renderIndex(obj.Fields, path+obj.Name+".", s)...))
		case v.Value != nil:
			val := v.Value
			name := md.Text(fmt.Sprintf("%s %s%s", val.Type, path, val.Name))
			link := "#" + s.Slug(name.String())
			elems = append(elems, md.Link(md.Code(name), link))
		}
	}
	return elems
}

func renderApi(api docsonnet.Fields, path string) []md.Elem {
	var elems []md.Elem

	for _, k := range sortFields(api) {
		v := api[k]
		switch {
		case v.Function != nil:
			fn := v.Function
			elems = append(elems,
				md.Headline(3, fmt.Sprintf("fn %s%s", path, fn.Name)),
				md.CodeBlock("ts", fmt.Sprintf("%s(%s)", fn.Name, renderParams(fn.Args))),
				md.Text(fn.Help),
			)
		case v.Object != nil:
			obj := v.Object
			elems = append(elems,
				md.Headline(2, fmt.Sprintf("obj %s%s", path, obj.Name)),
				md.Text(obj.Help),
			)
			elems = append(elems, renderApi(obj.Fields, path+obj.Name+".")...)

		case v.Value != nil:
			val := v.Value
			elems = append(elems,
				md.Headline(3, fmt.Sprintf("%s %s%s", val.Type, path, val.Name)),
			)

			if val.Default != nil {
				elems = append(elems, md.Paragraph(
					md.Italic(md.Text("Default value: ")),
					md.Code(md.Text(fmt.Sprint(val.Default))),
				))
			}

			elems = append(elems,
				md.Text(val.Help),
			)
		}
	}

	return elems
}

func sortFields(api docsonnet.Fields) []string {
	keys := make([]string, 0, len(api))
	for k := range api {
		keys = append(keys, k)
	}

	aFn := func(a, b string) bool {
		return api[a].Function != nil && api[b].Function == nil
	}
	aNew := func(a, b string) bool {
		a = strings.ToLower(a)
		b = strings.ToLower(b)

		return strings.HasPrefix(a, "new") && !strings.HasPrefix(b, "new")
	}

	sort.Slice(keys, func(i, j int) bool {
		a, b := keys[i], keys[j]

		if aNew(a, b) {
			return true
		} else if aNew(b, a) {
			return false
		}

		if aFn(a, b) {
			return true
		} else if aFn(b, a) {
			return false
		}

		return a < b
	})

	return keys
}

func renderParams(a []docsonnet.Argument) string {
	args := make([]string, 0, len(a))
	for _, a := range a {
		arg := a.Name
		if a.Default != nil {
			arg = fmt.Sprintf("%s=%v", arg, jsonParam(a.Default))
		}
		args = append(args, arg)
	}

	return strings.Join(args, ", ")
}

func jsonParam(i interface{}) string {

	d, err := json.Marshal(i)
	if err != nil {
		panic(err)
	}

	s, err := formatter.Format("(jsonParam)", string(d), formatter.Options{
		PadObjects:       false,
		PadArrays:        false,
		PrettyFieldNames: true,
		StringStyle:      formatter.StringStyleSingle,
	})
	if err != nil {
		panic(err)
	}

	return strings.TrimSpace(s)
}
```

## File: `pkg/render/render_test.go`
```go
package render

import (
	"testing"

	"github.com/jsonnet-libs/docsonnet/pkg/docsonnet"
	"github.com/stretchr/testify/assert"
)

func TestSortFields(t *testing.T) {
	api := docsonnet.Fields{
		"new":      dfn(),
		"newNamed": dfn(),

		"aaa": dfn(),
		"bbb": dobj(),
		"ccc": dfn(),

		"metadata": dobj(),
	}

	sorted := []string{
		"new",
		"newNamed",

		"aaa",
		"ccc",

		"bbb",
		"metadata",
	}

	res := sortFields(api)

	assert.Equal(t, sorted, res)
}

func dobj() docsonnet.Field {
	return docsonnet.Field{
		Object: &docsonnet.Object{},
	}
}

func dfn() docsonnet.Field {
	return docsonnet.Field{
		Function: &docsonnet.Function{},
	}
}
```

## File: `pkg/slug/slug.go`
```go
package slug

import (
	"regexp"
	"strconv"
	"strings"
)

type Slugger struct {
	occurences map[string]int
}

var (
	expWhitespace = regexp.MustCompile(`\s`)
	expSpecials   = regexp.MustCompile("[\u2000-\u206F\u2E00-\u2E7F\\'!\"#$%&()*+,./:;<=>?@[\\]^`{|}~’]")
)

func New() *Slugger {
	return &Slugger{
		occurences: make(map[string]int),
	}
}

func (s *Slugger) Slug(str string) string {
	str = expWhitespace.ReplaceAllString(str, "-")
	str = expSpecials.ReplaceAllString(str, "")

	old := str
	if o := s.occurences[str]; o > 0 {
		str += "-" + strconv.Itoa(o)
	}
	s.occurences[old] = s.occurences[old] + 1

	return strings.ToLower(str)
}
```

## File: `pkg/slug/slug_test.go`
```go
package slug

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSlug(t *testing.T) {

	cases := [][]struct {
		in, out string
	}{
		{
			{"foo", "foo"},
			{"foo", "foo-1"},
			{"foo bar", "foo-bar"},
		},
		{
			{"foo", "foo"},
			{"fooCamelCase", "foocamelcase"},
		},
		{
			{"foo", "foo"},
			{"foo", "foo-1"},
			// {"foo 1", "foo-1-1"}, // these are too rare for Jsonnet
			// {"foo 1", "foo-1-2"},
			{"foo", "foo-2"},
		},
		{
			{"heading with a - dash", "heading-with-a---dash"},
			{"heading with an _ underscore", "heading-with-an-_-underscore"},
			{"heading with a period.txt", "heading-with-a-periodtxt"},
			{"exchange.bind_headers(exchange, routing [, bindCallback])", "exchangebind_headersexchange-routing--bindcallback"},
		},
	}

	for _, cs := range cases {
		s := New()
		for _, c := range cs {
			assert.Equal(t, c.out, s.Slug(c.in))
		}
	}
}
```

