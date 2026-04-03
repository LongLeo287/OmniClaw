---
id: github.com-mpalmer-action-validator-b3890919-knowl
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:01.098739
---

# KNOWLEDGE EXTRACT: github.com_mpalmer_action-validator_b3890919
> **Extracted on:** 2026-04-01 08:47:45
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519798/github.com_mpalmer_action-validator_b3890919

---

## File: `.editorconfig`
```
root = true

[*]
end_of_line = lf
insert_final_newline = true
charset = utf-8
trim_trailing_whitespace = true

[*.yml]
indent_style = space
indent_size = 2

[{install,list-all}]
indent_style = tab
indent_size = 3
```

## File: `.gitignore`
```
/node_modules
/target
**/*.rs.bk
```

## File: `.gitmodules`
```
[submodule "src/schemastore"]
	path = src/schemastore
	url = https://github.com/SchemaStore/schemastore
```

## File: `.nvmrc`
```
lts/hydrogen
```

## File: `.pre-commit-hooks.yaml`
```yaml
- id: action-validator
  name: Validate GitHub Actions workflows
  description: "Validate GitHub Actions workflows"
  entry: action-validator
  language: rust
  files: '.github/workflows/.*\.ya?ml'
```

## File: `.prettierignore`
```
# Ignore everything
*

# But not JavaScript files in the packages directory
!packages/**/*.mjs
!packages/**/*.js
```

## File: `.prettierrc.json`
```json
{}
```

## File: `.tool-versions`
```
rust 1.56.1
shellcheck 0.7.2
shfmt 3.3.0
action-validator 0.1.0
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Code of Conduct

As contributors and maintainers of this project, and in the interest of
fostering an open and welcoming community, we pledge to respect all people who
contribute through reporting issues, posting feature requests, updating
documentation, submitting pull requests or patches, and other activities.

We are committed to making participation in this project a harassment-free
experience for everyone, regardless of level of experience, gender, gender
identity and expression, sexual orientation, disability, personal appearance,
body size, race, ethnicity, age, religion, or nationality.

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery
* Personal attacks
* Trolling or insulting/derogatory comments
* Public or private harassment
* Publishing other's private information, such as physical or electronic
  addresses, without explicit permission
* Other unethical or unprofessional conduct

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

By adopting this Code of Conduct, project maintainers commit themselves to
fairly and consistently applying these principles to every aspect of managing
this project. Project maintainers who do not follow or enforce the Code of
Conduct may be permanently removed from the project team.

This code of conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community.

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting a project maintainer at mpalmer@hezmatt.org. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. Maintainers are
obligated to maintain confidentiality with regard to the reporter of an
incident.

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 1.3.0, available at
[http://contributor-covenant.org/version/1/3/0/][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/3/0/
```

## File: `CONTRIBUTING.md`
```markdown
# Overview

* If you have found a discrepancy in documented and observed behaviour, that
  is a bug. Feel free to [report it as an
  issue](https://github.com/mpalmer/action-validator/issues), providing
  sufficient detail to reproduce the problem.

* If you would like to add new behaviour, please submit a well-tested and
  well-documented [pull
  request](https://github.com/mpalmer/action-validator/pulls).

* At all times, abide by the Code of Conduct (CODE_OF_CONDUCT.md).

---

# Environment Setup

## Install Rust
Firstly, you'll need a Rust toolchain to make any changes to the core functionality of this project. We recommend [using `rustup`](https://www.rust-lang.org/tools/install), because that's what the Rust core team recommend.

To confirm that rust is installed, run the `cargo` command. If you don't receive the help docs output, you may need to add rust to your shell rc file.

## Git Submodule Setup
This repository uses [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules). Specifically for the use of [schemastore](https://github.com/SchemaStore/schemastore).

To setup the git submodule after cloning this repo to your local, you'll want to run the following commands:
1. `git submodule init`
2. `git submodule update`

It should look similar to the output below.

```bash
❯ git submodule init
Submodule 'src/schemastore' (https://github.com/SchemaStore/schemastore) registered for path 'src
/schemastore'
❯ git submodule update
Cloning into '/Users/someuser/action-validator/src/schemastore'...
Submodule path 'src/schemastore': checked out 'd3e6ab7727380b214acbab05570fb09a3e5d2dfc'
```

At this point, you should be all set to `cargo run`!

## Node/WASM Setup
If you plan to work on the WASM/Node bindings, you'll also need to install Node. We recommend using [NVM](https://github.com/nvm-sh/nvm) to install the Node version listed in `.nvmrc`.

Once Node is installed, run `npm install` at the root of the repository.

You should now be all set to run `npm build`, to build the Node/WASM bindings. Once built, run `npx action-validator` to run the CLI via the Node/WASM bindings.

# Running the Validator Locally

## `cargo run [FILE] -- [OPTIONS]`
`cargo run` will create a _debug_ executable and run the project. If this is your first time running the command, cargo will compile the development binary with `cargo build`. This will install all of the dependencies and create the debug binary `action-validator` in the `/target/debug/` directory. `cargo run` will then invoke this binary after creation.

One caveat if you're running with `cargo run`: if you want to supply the program with options, you need to use the `--` operator between `cargo run` and your provided options. This let's cargo know which flags are meant for cargo, and which are meant for the executable.

## `cargo build` && `./target/debug/action-validator [OPTIONS]`
As discussed in the prior section, `cargo build` install dependencies (if they're not cached) and build the development binary. This binary can then be invoked directly by running `./target/debug/action-validator`. This does **not** require the use of the `--` operator in between the binary and any provided options.

## Try It Yourself!

Run the command `cargo run -- --help`. You should see an output similar to the following.
```bash
❯ cargo run -- --help
    Finished dev [unoptimized + debuginfo] target(s) in 0.05s
     Running `target/debug/action-validator --help`
A validator for GitHub Action and Workflow YAML files

Usage: action-validator [OPTIONS] [path_to_action_yaml]...

Arguments:
  [path_to_action_yaml]...  Input file

Options:
  -v, --verbose  Be more verbose
  -h, --help     Print help information
  -V, --version  Print version information
```

# Writing Tests

All tests live in the `tests` directory. Currently, this project implements snapshot testing,
but that's not to say you couldn't write unit or integration tests with the current structure.
To run the tests, simply run `cargo test` from the root directory. If you want to test a specific
feature, you can add the `-F {feature}` flag (e.g. `cargo test -F remote-checks`).

## Unit/Integration Tests
As of this writing, there are no unit or integration tests. If you are looking to write some, please
follow the directions in [this guide](https://doc.rust-lang.org/book/ch11-01-writing-tests.html).

## Snapshot Tests
A snapshot test is performed when we execute the cli and capture `stdout`, `stderr`, and/or an exit code.
When the tests are run, the results of the test must exactly match those of the previous run. For this project,
the snapshot tests are named in the format `{next_id}_{whats_being_tested}` (e.g. `011_remote_checks_failure`).

If you have made changes which will change the output of the program and cause snapshots to fail, you can run
`cargo test -F test-save-snapshots`. This feature causes the executed command to save the `stdout`, `stderr`, and/or
exit code to the specified testing directory.

If you are writing a net new test, you will need to create the test directory with your workflow or action file, and a
`test.json` file. Once you're done, you can save the results to that directy by running
`cargo test -F test-save-snapshots`.

The `test.json` file contains the test configuration. It can usually be left empty (i.e. `{}`).

```jsonc
// Example test.json
{
  "targets": {
    "node": false,
    "native": true
  },
  "cli_args": [
    "--rootdir",
    "tests/fixtures/011_subdir_globs/subdir",
    "tests/fixtures/011_subdir_globs/subdir/glob.yml"
  ]
}
```

# Testing Node/WASM Bindings

To test against the Node/WASM bindings, you can run `npm test`, or `npm test:dev` (to skip optimisations).
Note that Node support is considered experimental, and does not have one to one feature parity with the native binary yet.
As such, some tests may fail, even on `main`.
```

## File: `Cargo.toml`
```
[package]
name = "action-validator"
description = "Validator for GitHub action and workflow YAML files"
license = "GPL-3.0-only"
homepage = "https://github.com/mpalmer/action-validator"
repository = "https://github.com/mpalmer/action-validator"
include = [
	"/LICENCE",
	"/src/*.rs",
	"/src/**/*.rs",
	"/src/schemastore/src/schemas/json/github-workflow.json",
	"/src/schemastore/src/schemas/json/github-action.json"
]
version = "0.0.0-git"
authors = ["Matt Palmer <matt@hezmatt.org>"]
edition = "2021"
# If this is changed, .github/workflows/qa.yml build matrix needs updating as well
rust-version = "1.84.0"

[lib]
crate-type = ["cdylib", "rlib"]

[features]
default = ["assert_cmd"]
js = ["console_error_panic_hook", "valico/js"]
test-save-snapshots = []
test-js = []

[dependencies]
clap = { version = "4.0", features = ["derive"] }
glob = "0.3"
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
serde_yaml = "0.9.17"
valico = "4.0"

wasm-bindgen = "0.2.84"

# The `console_error_panic_hook` crate provides better debugging of panics by
# logging them with `console.error`. This is great for development, but requires
# all the `std::fmt` and `std::panicking` infrastructure, so isn't great for
# code size when deploying.
console_error_panic_hook = { version = "0.1.7", optional = true }

serde-wasm-bindgen = "0.4.5"
js-sys = "0.3.77"
is-terminal = "0.4.7"
assert_cmd = { version = "2.1.1", optional = true }

[dev-dependencies]
wasm-bindgen-test = "0.3.34"
fixtures = "2.5.0"

[profile.release]
# Tell `rustc` to optimize for small code size.
opt-level = "s"
```

## File: `LICENCE`
```
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

## File: `README.md`
```markdown
The `action-validator` is a standalone tool designed to "lint" the YAML files
used to define GitHub Actions and Workflows. It ensures that they are well-formed,
by checking them against published JSON schemas, and it makes sure that any
globs used in `paths` / `paths-ignore` match at least one file in the repo.

The intended use case for `action-validator` is in Git pre-commit hooks and
similar situations.


# Funding Development

I am currently experimenting with ways to fund development of new features in `action-validator`.
You can find more details of this approach at [the `action-validator` code fund page](https://hezmatt.org/~mpalmer/code-fund.html).


# Installation

We have many ways to install `action-validator`.

## Pre-built binaries

The [GitHub releases](https://github.com/mpalmer/action-validator/releases)
have some pre-built binaries -- just download and put them in your path. If a
binary for your platform isn't available, let me know and I'll see what I can
figure out.


## Using cargo

If you've got a Rust toolchain installed, running `cargo install action-validator` should give you the latest release.


## Using asdf

If you're a proponent of the [asdf tool](https://asdf-vm.com/), then you can
use that to install and manage `action-validator`:

```shell
asdf plugin add action-validator
# or
asdf plugin add action-validator https://github.com/mpalmer/action-validator.git
```

Install/configure action-validator:

```shell
# Show all installable versions
asdf list-all action-validator

# Install specific version
asdf install action-validator latest

# Set a version globally (on your ~/.tool-versions file)
asdf set -u action-validator latest

# Now action-validator commands are available
action-validator --help
```


# Using mise

If you are a passionate user of [mise](https://github.com/jdx/mise), then you can use that to install and manage `action-validator`:

No need to declare the plugin, it's already known by mise.

Install/configure action-validator:

```shell
# Show all installable versions
mise ls-remote action-validator

# Install specific version
mise install action-validator@latest

# Set a version globally (on your ~/.tool-versions or .mise.toml file)
mise use -g action-validator@latest

# Now action-validator commands are available
action-validator --help
```


## Using NPM

Node users can install the latest version using NPM:

> ℹ️ The `@action-validator/core` package can be used directly within Node.js applications.

```sh
npm install -g @action-validator/core @action-validator/cli --save-dev
```

## Building from the repo

If you want to build locally, you'll need to:

1. Checkout the git repository somewhere;

1. Grab the `SchemaStore` submodule, by running `git submodule init && git submodule update`;

1. Install a [Rust](https://rust-lang.org) toolchain; and then

1. run `cargo build`.


# Usage

Couldn't be simpler: just pass a file to the program:

```shell
action-validator .github/workflows/build.yml
```

Use `action-validator -h` to see additional options.


## In a GitHub Action

The action-validator can be run in a Github action itself, as a pull request job. See the `actions` job in the [QA workflow](https://github.com/mpalmer/action-validator/tree/main/.github/workflows/qa.yml), in this repository, as an example of how to use action-validator + asdf in a GitHub workflow.
This may seem a little redundant (after all, an action has to be valid in order for GitHub to run it), but this job will make sure that all your *other* actions are also valid.

Alternatively, use the [composite action](./action.yml) from this repository by adding this step to your job:

```yml
      - name: action-validator
        uses: mpalmer/action-validator@main # please lock to the latest SHA for secure use
        with:
          version: latest # also lock this to a semver without the v prefix for secure use and stability
```

## Using pre-commit

Update your .pre-commit-config.yaml:

```yaml
repos:
- repo: https://github.com/mpalmer/action-validator
  rev: v<version>
  hooks:
    - id: action-validator
```

## Pre-commit hook example

Create an executable file in the .git/hooks directory of the target repository:
`touch .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit` and paste the following example code:

```bash
#!/bin/bash
if ! command -v action-validator >/dev/null; then
  echo "action-validator is not installed."
  echo "Installation instructions: https://github.com/mpalmer/action-validator"
  exit 1
fi
echo "Running pre-commit hook for GitHub Actions: https://github.com/mpalmer/action-validator"
scan_count=0
for action in $(git diff --cached --name-only --diff-filter=ACM | grep -E '^\.github/(workflows|actions)/.*\.ya?ml$'); do
  if action-validator "$action"; then
    echo "✅ $action"
  else
    echo "❌ $action"
    exit 1
  fi
  scan_count=$((scan_count+1))
done
echo "action-validator scanned $scan_count GitHub Actions and found no errors!"
```

This script will run on every commit to the target repository, whether the github action yaml files are being committed, or not and prevent any commit if there are linting errors.

```
# All action-validator linting errors must be resolved before any commit will succeed.
$ echo "" >> README.md && git add README.md && git commit -m "Update read-me"
Running pre-commit hook for GitHub Actions: https://github.com/mpalmer/action-validator
Validation failed: ValidationState {
    errors: [
        Properties {
            path: "",
            detail: "Additional property 'aname' is not allowed",
        },
    ],
    missing: [],
    replacement: None,
}
❌ .github/workflows/ci.yaml
Fatal error validating .github/workflows/ci.yaml: validation failed


# Fix error and try again
$ echo "" >> README.md && git add README.md && git commit -m "Update read-me"
Running pre-commit hook for GitHub Actions: https://github.com/mpalmer/action-validator
✅ .github/workflows/ci.yaml
✅ .github/workflows/release.yml
action-validator scanned 2 GitHub Actions found no errors!
[main c34fda3] Update read-me
 1 file changed, 2 insertions(+)
```

## NPM

Provided you have followed the [installation instructions for NPM](#using-npm), you can run the action
validator CLI as follows

```sh
npx action-validator <path_to_action_yaml>
```

Or, if you've installed the package globally:

```sh
action-validator <path_to_action_yaml>
```

The CLI distributed via NPM supports all the same options as the native binary.

## Node API

The Node API can be used to validate action and workflow files from Node.js as follows:

```ts
import { readFileSync } from "fs";
import { validateAction, validateWorkflow } from "@action-validator/core";

// Validate Action
const actionSource = readFileSync("action.yml", "utf8");
const state = validator.validateAction(actionSource);
const isValid = state.errors.length === 0;

// Validate Workflow
const workflowSource = readFileSync("workflow.yml", "utf8");
const state = validator.validateWorkflow(workflowSource);
const isValid = state.errors.length === 0;
```

# Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md).


# Licence

Unless otherwise stated, everything in this repo is covered by the following
copyright notice:

    Copyright (C) 2021  Matt Palmer <matt@hezmatt.org>

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License version 3, as
    published by the Free Software Foundation.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
```

## File: `action.yml`
```yaml
name: action-validator
description: Downloads, caches, and runs action-validator with verbose output on files tracked by Git.
inputs:
  version:
    description: action-validator version in semver format without the 'v' prefix
    required: false
    default: "latest"
  patterns:
    description: 'Newline-separated list of git ls-files patterns'
    required: false
    default: |
      :(glob).github/**/action.yml
      :(glob).github/**/action.yaml
      .github/workflows/*.yml
      .github/workflows/*.yaml
branding:
  icon: check
  color: green
runs:
  using: "composite"
  steps:
    - name: Convert architecture
      id: arch
      shell: sh
      env:
        runner_arch: ${{ runner.arch }} # Possible values are X86, X64, ARM, or ARM64.
      run: |
        case "$runner_arch" in
          X64) echo "arch=amd64" >> "$GITHUB_OUTPUT" ;;
          ARM64) echo "arch=arm64" >> "$GITHUB_OUTPUT" ;;
          *) echo "Unsupported architecture: $runner_arch" >&2; exit 1 ;;
        esac
    - name: Convert OS
      id: os
      shell: sh
      env:
        runner_os: ${{ runner.os }} # Possible values are Linux, Windows, or macOS.
      run: |
        case "$runner_os" in
          Linux) echo "os=linux" >> "$GITHUB_OUTPUT" ;;
          macOS) echo "os=darwin" >> "$GITHUB_OUTPUT" ;;
          *) echo "Unsupported OS: $runner_os" >&2; exit 1 ;;
        esac
    - name: Resolve version
      id: resolve
      shell: bash
      env:
        GH_TOKEN: ${{ github.token }}
        version: ${{ inputs.version }}
      run: |
        if [[ "$version" = "latest" ]]; then
          tag="$(gh release view --repo mpalmer/action-validator --json tagName -q .tagName)"
          version="${tag#v}"
        fi
        echo "version=$version" >> "$GITHUB_OUTPUT"
    - name: Cache
      id: cache
      uses: actions/cache@v4
      with:
        path: /usr/local/bin/action-validator
        key: action-validator_v${{ steps.resolve.outputs.version }}_${{ steps.os.outputs.os }}_${{ steps.arch.outputs.arch }}
    - if: steps.cache.outputs.cache-hit != 'true'
      name: Install
      shell: sh
      env:
        GH_TOKEN: ${{ github.token }}
        version: ${{ steps.resolve.outputs.version }}
        os: ${{ steps.os.outputs.os }}
        arch: ${{ steps.arch.outputs.arch }}
        output: /usr/local/bin/action-validator
      run: |
        printf 'gh release download "v%s" --repo mpalmer/action-validator --pattern "action-validator_%s_%s" --output "%s"\n' "$version" "$os" "$arch" "$output"
        gh release download "v$version" --repo mpalmer/action-validator --pattern "action-validator_${os}_$arch" --output "$output"
        chmod +x "$output"
    - name: Run
      shell: sh
      env:
        patterns: ${{ inputs.patterns }}
      run: |
        printf '%s\n' "$patterns" | xargs -I{} git ls-files -z -- {} | sort --zero-terminated --unique | xargs -0 action-validator --verbose
```

## File: `build.rs`
```rust
fn main() {
    println!("cargo:rerun-if-changed=tests/fixtures");
}
```

## File: `package.json`
```json
{
  "name": "@action-validator/root",
  "private": true,
  "version": "0.0.0-git",
  "license": "GPL-3.0-only",
  "workspaces": ["packages/*"],
  "scripts": {
    "build": "./scripts/build-wasm.sh",
    "build:dev": "WASM_PACK_BUILD_FLAGS='--no-opt' ./scripts/build-wasm.sh",
    "test": "./scripts/test-wasm.sh",
    "test:dev": "WASM_PACK_BUILD_FLAGS='--no-opt' ./scripts/test-wasm.sh",
    "lint": "prettier --check .",
    "format": "prettier --write ."
  },
  "devDependencies": {
    "chalk": "5.2.0",
    "diff": "5.1.0",
    "prettier": "2.8.4",
    "wasm-pack": "0.13.1"
  }
}
```

## File: `packages/cli/.gitignore`
```
/node_modules
```

## File: `packages/cli/cli.mjs`
```
#!/usr/bin/env node
// @ts-check

import * as actionValidator from "@action-validator/core";

actionValidator.main(process.argv.slice(1));
```

## File: `packages/cli/package.json`
```json
{
  "name": "@action-validator/cli",
  "collaborators": [
    "Matt Palmer <matt@hezmatt.org>",
    "Ben Heidemann <ben@heidemann.co.uk>"
  ],
  "description": "Validator for GitHub action and workflow YAML files",
  "version": "0.0.0-git",
  "license": "GPL-3.0-only",
  "repository": {
    "type": "git",
    "url": "https://github.com/mpalmer/action-validator"
  },
  "files": [
    "cli.mjs"
  ],
  "main": "cli.js",
  "homepage": "https://github.com/mpalmer/action-validator",
  "bin": {
    "action-validator": "./cli.mjs"
  },
  "scripts": {
    "build": "npx wasm-pack build --out-dir target/wasm-pack/build --no-typescript --target nodejs --features js && cp target/wasm-pack/build/action_validator_bg.wasm dist/ && cp target/wasm-pack/build/action_validator.js dist/ && cp target/wasm-pack/build/action_validator.js dist/",
    "test": "node test/run.mjs",
    "lint": "prettier --check .",
    "format": "prettier --write ."
  },
  "dependencies": {},
  "devDependencies": {
    "@action-validator/core": "file:../core"
  },
  "peerDependencies": {
    "@action-validator/core": "0.0.0-git"
  }
}
```

## File: `packages/core/.gitignore`
```
/node_modules
/snippets
action_validator_bg.wasm
action_validator.js
```

## File: `packages/core/action_validator.d.ts`
```typescript
export type ParseErrorLocation = {
  index: number;
  line: number;
  column: number;
};

export type ValidationError =
  | {
      code: string;
      detail?: string;
      path: string;
      title: string;
      states?: Omit<ValidationState, "actionType">[];
    }
  | {
      code: string;
      detail: string;
      title: string;
      location?: ParseErrorLocation;
    };

export type ValidationState = {
  actionType: "action" | "workflow";
  errors: ValidationError[];
};

export function main(args: string[]): never;
export function validateAction(src: string): ValidationState;
export function validateWorkflow(src: string): ValidationState;
```

## File: `packages/core/package.json`
```json
{
  "name": "@action-validator/core",
  "collaborators": [
    "Matt Palmer <matt@hezmatt.org>",
    "Ben Heidemann <ben@heidemann.co.uk>"
  ],
  "description": "Validator for GitHub action and workflow YAML files",
  "version": "0.0.0-git",
  "license": "GPL-3.0-only",
  "repository": {
    "type": "git",
    "url": "https://github.com/mpalmer/action-validator"
  },
  "files": [
    "action_validator_bg.wasm",
    "action_validator.js",
    "action_validator.d.ts"
  ],
  "main": "action_validator.js",
  "homepage": "https://github.com/mpalmer/action-validator",
  "types": "action_validator.d.ts",
  "scripts": {
    "build": "npx wasm-pack build --out-dir target/wasm-pack/build --no-typescript --target nodejs --features js && cp target/wasm-pack/build/action_validator_bg.wasm dist/ && cp target/wasm-pack/build/action_validator.js dist/ && cp target/wasm-pack/build/action_validator.js dist/",
    "test": "node test/run.mjs",
    "lint": "prettier --check .",
    "format": "prettier --write ."
  },
  "dependencies": {
    "fast-glob": "^3.3.3"
  }
}
```

## File: `scripts/build-wasm.sh`
```bash
#!/usr/bin/env bash

set -euo pipefail

# [SC2086] Intenitonally omitting double quotes to allow word splitting of WASM_PACK_BUILD_FLAGS
# shellcheck disable=SC2086
npx wasm-pack build ${WASM_PACK_BUILD_FLAGS:-} --out-dir target/wasm-pack/build --no-typescript --target nodejs --no-default-features --features js
rm -rf packages/core/snippets
cp -R target/wasm-pack/build/snippets packages/core/snippets
cp target/wasm-pack/build/action_validator_bg.wasm packages/core/
cp target/wasm-pack/build/action_validator.js packages/core/
```

## File: `scripts/test-wasm.sh`
```bash
#!/usr/bin/env bash

set -euo pipefail

cargo test -F test-js
```

## File: `src/config.rs`
```rust
use clap::Parser;
use serde::Serialize;
use std::path::PathBuf;

#[derive(Parser, Debug)]
#[command(
    name = "action-validator",
    about = "A validator for GitHub Action and Workflow YAML files",
    version
)]
pub struct CliConfig {
    /// Be more verbose
    #[arg(short, long)]
    pub verbose: bool,

    #[arg(
        long,
        help = "Use specified dir as root of glob matching, rather than the current directory"
    )]
    pub rootdir: Option<PathBuf>,

    /// Input file
    #[arg(name = "path_to_action_yaml")]
    pub src: Vec<PathBuf>,
}

#[derive(Serialize, Copy, Clone, Debug)]
pub enum ActionType {
    #[serde(rename = "action")]
    Action,
    #[serde(rename = "workflow")]
    Workflow,
}

pub struct JsConfig<'a> {
    pub action_type: ActionType,
    pub src: &'a str,
    pub verbose: bool,
}

pub struct RunConfig<'a> {
    pub file_path: Option<&'a str>,
    pub file_name: Option<&'a str>,
    pub action_type: ActionType,
    pub src: &'a str,
    pub verbose: bool,
    pub rootdir: Option<PathBuf>,
}

impl<'a> From<&JsConfig<'a>> for RunConfig<'a> {
    fn from(config: &JsConfig<'a>) -> Self {
        RunConfig {
            file_path: None,
            file_name: None,
            action_type: config.action_type,
            src: config.src,
            verbose: config.verbose,
            rootdir: None,
        }
    }
}
```

## File: `src/lib.rs`
```rust
mod config;
mod schemas;
mod system;
mod utils;
mod validation_error;
mod validation_state;

use config::{ActionType, RunConfig};
use std::path::PathBuf;
use validation_error::ValidationError;
use validation_state::ValidationState;

pub use crate::config::CliConfig;
use crate::schemas::{validate_as_action, validate_as_workflow};

#[cfg(feature = "js")]
mod js {
    use super::cli;
    use crate::config::CliConfig;
    use crate::system;
    use crate::{
        config::{ActionType, JsConfig},
        utils::set_panic_hook,
    };
    use clap::Parser as _;
    use js_sys::Array;
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(js_name = main)]
    pub fn main(args: Array) -> JsValue {
        set_panic_hook();

        let rust_args: Vec<String> = args
            .iter()
            .map(|arg| arg.as_string().unwrap_or_default())
            .collect();

        let config = match CliConfig::try_parse_from(rust_args) {
            Ok(config) => config,
            Err(error) => {
                let error_text = if system::process::stdout::is_tty() {
                    format!("{}", error.render().ansi())
                } else {
                    error.render().to_string()
                };
                system::console::error(&error_text);
                system::process::exit(error.exit_code());
            }
        };

        if matches!(cli::run(&config), cli::RunResult::Failure) {
            system::process::exit(1);
        }

        system::process::exit(0);
    }

    #[wasm_bindgen(js_name = validateAction)]
    pub fn validate_action(src: &str) -> JsValue {
        set_panic_hook();

        let config = JsConfig {
            action_type: ActionType::Action,
            src,
            verbose: false,
        };

        run(&config)
    }

    #[wasm_bindgen(js_name = validateWorkflow)]
    pub fn validate_workflow(src: &str) -> JsValue {
        set_panic_hook();

        let config = JsConfig {
            action_type: ActionType::Workflow,
            src,
            verbose: false,
        };

        run(&config)
    }

    fn run(config: &JsConfig) -> JsValue {
        let run_config = config.into();
        let state = crate::run(&run_config);
        serde_wasm_bindgen::to_value(&state).unwrap()
    }
}

pub mod cli {
    use crate::{
        config::{ActionType, RunConfig},
        system, CliConfig,
    };

    pub enum RunResult {
        Success,
        Failure,
    }

    pub fn run(config: &CliConfig) -> RunResult {
        let mut success = true;

        for path in &config.src {
            let file_name = match path.file_name() {
                Some(file_name) => file_name.to_str(),
                None => {
                    eprintln!("Unable to derive file name from src!");
                    success = false;
                    continue;
                }
            };

            let src = &match system::fs::read_to_string(path) {
                Ok(src) => src,
                Err(err) => {
                    system::console::error(&format!(
                        "Unable to read file {}: {err}",
                        path.display()
                    ));
                    success = false;
                    continue;
                }
            };

            let config = RunConfig {
                file_path: Some(path.to_str().unwrap()),
                file_name,
                action_type: match file_name {
                    Some("action.yml") | Some("action.yaml") => ActionType::Action,
                    _ => ActionType::Workflow,
                },
                src,
                verbose: config.verbose,
                rootdir: config.rootdir.clone(),
            };

            let state = crate::run(&config);

            if !state.is_valid() {
                let fmt_state = format!("{state:#?}");
                let path = state.file_path.unwrap_or("file".into());
                system::console::log(&format!("Fatal error validating {path}"));
                system::console::error(&format!("Validation failed: {fmt_state}"));
                success = false;
            }
        }

        if success {
            RunResult::Success
        } else {
            RunResult::Failure
        }
    }
}

fn run(config: &RunConfig) -> ValidationState {
    let file_name = config.file_name.unwrap_or("file");
    let doc = serde_yaml::from_str(config.src);

    let mut state = match doc {
        Err(err) => ValidationState {
            action_type: Some(config.action_type),
            file_path: Some(file_name.to_string()),
            errors: vec![err.into()],
        },
        Ok(doc) => match config.action_type {
            ActionType::Action => {
                if config.verbose {
                    system::console::log(&format!("Treating {file_name} as an Action definition"));
                }
                validate_as_action(&doc)
            }
            ActionType::Workflow => {
                if config.verbose {
                    system::console::log(&format!("Treating {file_name} as a Workflow definition"));
                }
                // TODO: Re-enable path and job validation
                let mut state = validate_as_workflow(&doc);

                validate_paths(&doc, config.rootdir.as_ref(), &mut state);
                validate_job_needs(&doc, &mut state);

                state
            }
        },
    };

    state.action_type = Some(config.action_type);
    state.file_path = config.file_path.map(|file_name| file_name.to_string());

    state
}

fn validate_paths(doc: &serde_json::Value, rootdir: Option<&PathBuf>, state: &mut ValidationState) {
    validate_globs(
        &doc["on"]["push"]["paths"],
        "/on/push/paths",
        rootdir,
        state,
    );
    validate_globs(
        &doc["on"]["push"]["paths-ignore"],
        "/on/push/paths-ignore",
        rootdir,
        state,
    );
    validate_globs(
        &doc["on"]["pull_request"]["paths"],
        "/on/pull_request/paths",
        rootdir,
        state,
    );
    validate_globs(
        &doc["on"]["pull_request"]["paths-ignore"],
        "/on/pull_request/paths-ignore",
        rootdir,
        state,
    );
}

fn validate_globs(
    globs: &serde_json::Value,
    path: &str,
    rootdir: Option<&PathBuf>,
    state: &mut ValidationState,
) {
    if globs.is_null() {
        return;
    }

    if let Some(globs) = globs.as_array() {
        for g in globs {
            let glob = g.as_str().expect("glob to be a string");
            let pattern = if glob.starts_with('!') {
                glob.chars().skip(1).collect()
            } else {
                glob.to_string()
            };

            let pattern = if let Some(rootdir) = rootdir {
                rootdir.join(pattern).display().to_string()
            } else {
                pattern
            };

            match system::glob::glob_count_matches(&pattern) {
                Ok(count) => {
                    if count == 0 {
                        state.errors.push(ValidationError::NoFilesMatchingGlob {
                            code: "glob_not_matched".into(),
                            path: path.into(),
                            title: "Glob does not match any files".into(),
                            detail: Some(format!("Glob {g} in {path} does not match any files")),
                        });
                    }
                }
                Err(e) => {
                    state.errors.push(ValidationError::InvalidGlob {
                        code: "invalid_glob".into(),
                        path: path.into(),
                        title: "Glob does not match any files".into(),
                        detail: Some(format!("Glob {g} in {path} is invalid: {e}")),
                    });
                }
            };
        }
    } else {
        unreachable!(
            "validate_globs called on globs object with invalid type: must be array or null"
        )
    }
}

fn validate_job_needs(doc: &serde_json::Value, state: &mut ValidationState) {
    fn is_invalid_dependency(
        jobs: &serde_json::Map<String, serde_json::Value>,
        need_str: &str,
    ) -> bool {
        !jobs.contains_key(need_str)
    }

    fn handle_unresolved_job(job_name: &String, needs_str: &str, state: &mut ValidationState) {
        state.errors.push(ValidationError::UnresolvedJob {
            code: "unresolved_job".into(),
            path: format!("/jobs/{job_name}/needs"),
            title: "Unresolved job".into(),
            detail: Some(format!("unresolved job {needs_str}")),
        });
    }

    if let Some(jobs) = doc["jobs"].as_object() {
        for (job_name, job) in jobs.iter() {
            let needs = &job["needs"];
            if let Some(needs_str) = needs.as_str() {
                if is_invalid_dependency(jobs, needs_str) {
                    handle_unresolved_job(job_name, needs_str, state);
                }
            } else if let Some(needs_array) = needs.as_array() {
                for needs_str in needs_array
                    .iter()
                    .filter_map(|v| v.as_str())
                    .filter(|needs_str| is_invalid_dependency(jobs, needs_str))
                {
                    handle_unresolved_job(job_name, needs_str, state);
                }
            }
        }
    }
}
```

## File: `src/main.rs`
```rust
#[cfg(feature = "js")]
fn main() {}

#[cfg(not(feature = "js"))]
fn main() {
    use action_validator::CliConfig;
    use clap::Parser;
    use std::process;

    let config = CliConfig::parse();

    if matches!(
        action_validator::cli::run(&config),
        action_validator::cli::RunResult::Failure
    ) {
        process::exit(1);
    }
}
```

## File: `src/schemas.rs`
```rust
use serde_json::Value;

use crate::validation_state::ValidationState;

pub fn validate_as_action(doc: &Value) -> ValidationState {
    validate_with_schema(
        doc,
        include_bytes!("schemastore/src/schemas/json/github-action.json"),
    )
}

pub fn validate_as_workflow(doc: &Value) -> ValidationState {
    validate_with_schema(
        doc,
        include_bytes!("schemastore/src/schemas/json/github-workflow.json"),
    )
}

fn validate_with_schema(doc: &Value, schema: &[u8]) -> ValidationState {
    let schema_json: serde_json::Value =
        serde_json::from_str(String::from_utf8_lossy(schema).as_ref()).unwrap();

    let mut scope = valico::json_schema::Scope::new();
    let validator = scope.compile_and_return(schema_json, false).unwrap();

    validator.validate(doc).into()
}
```

## File: `src/utils.rs`
```rust
#[cfg(feature = "js")]
pub fn set_panic_hook() {
    // When the `console_error_panic_hook` feature is enabled, we can call the
    // `set_panic_hook` function at least once during initialization, and then
    // we will get better error messages if our code ever panics.
    //
    // For more details see
    // https://github.com/rustwasm/console_error_panic_hook#readme
    #[cfg(feature = "console_error_panic_hook")]
    console_error_panic_hook::set_once();
}
```

## File: `src/validation_error.rs`
```rust
use serde::Serialize;
use valico::common::error::ValicoError;

use crate::validation_state::ValidationState;

type BoxedValicoError = Box<dyn ValicoError>;

#[derive(Serialize, Debug)]
pub struct ParseErrorLocation {
    pub index: usize,
    pub line: usize,
    pub column: usize,
}

impl From<serde_yaml::Location> for ParseErrorLocation {
    fn from(location: serde_yaml::Location) -> Self {
        ParseErrorLocation {
            index: location.index(),
            line: location.line(),
            column: location.column(),
        }
    }
}

macro_rules! validation_errors {
    ($( $name:ident $( { $($fields:tt)* } )? ),*) => {
        #[derive(Serialize, Debug)]
        #[serde(untagged)]
        #[allow(dead_code)] // JS doesn't instantiate some of the validation errors at present
        pub enum ValidationError {
            $(
                $name {
                    code: String,
                    detail: Option<String>,
                    path: String,
                    title: String,
                    $( $($fields)* )?
                },
            )*
        }
    };
}

validation_errors!(
    // Schema Validation Errors
    WrongType,
    MultipleOf,
    Maximum,
    Minimum,
    MaxLength,
    MinLength,
    Pattern,
    MaxItems,
    MinItems,
    UniqueItems,
    Items,
    MaxProperties,
    MinProperties,
    Required,
    Properties,
    Enum,
    AnyOf { states: Vec<ValidationState> },
    OneOf { states: Vec<ValidationState> },
    Const,
    Contains,
    ContainsMinMax,
    Not,
    DivergentDefaults,
    Format,
    Unevaluated,
    Unknown,
    // Other Validation Errors
    UnresolvedJob,
    InvalidGlob,
    NoFilesMatchingGlob,
    // Other Errors
    Parse { location: Option<ParseErrorLocation> }
);

macro_rules! impl_from_valico_error {
    ($($err:ident => $name:ident $( { $($fields:tt)* } )? ),*) => {
        impl From<&BoxedValicoError> for ValidationError {
            fn from(err: &BoxedValicoError) -> Self {
                if false {
                    unreachable!()
                }
                $(
                    else if let Some($err) = err.downcast_ref::<valico::json_schema::errors::$name>() {
                        ValidationError::$name {
                            code: $err.get_code().into(),
                            path: $err.get_path().into(),
                            title: $err.get_title().into(),
                            detail: $err.get_detail().map(|s| s.into()),
                            $( $($fields)* )?
                        }
                    }
                )*
                else {
                    ValidationError::Unknown {
                        code: err.get_code().into(),
                        path: err.get_path().into(),
                        title: err.get_title().into(),
                        detail: err.get_detail().map(|s| s.into()),
                    }
                }
            }
        }
    };
}

impl_from_valico_error!(
    err => WrongType,
    err => MultipleOf,
    err => Maximum,
    err => Minimum,
    err => MaxLength,
    err => MinLength,
    err => Pattern,
    err => MaxItems,
    err => MinItems,
    err => UniqueItems,
    err => Items,
    err => MaxProperties,
    err => MinProperties,
    err => Required,
    err => Properties,
    err => Enum,
    err => AnyOf { states: err.states.iter().map(ValidationState::from).collect() },
    err => OneOf { states: err.states.iter().map(ValidationState::from).collect() },
    err => Const,
    err => Contains,
    err => ContainsMinMax,
    err => Not,
    err => DivergentDefaults,
    err => Format,
    err => Unevaluated
);

impl From<serde_yaml::Error> for ValidationError {
    fn from(err: serde_yaml::Error) -> Self {
        ValidationError::Parse {
            code: "parse_error".into(),
            detail: Some(err.to_string()),
            location: err.location().map(ParseErrorLocation::from),
            path: "".into(),
            title: "Parse Error".into(),
        }
    }
}
```

## File: `src/validation_state.rs`
```rust
use serde::Serialize;

use crate::{config::ActionType, validation_error::ValidationError};

#[derive(Serialize, Debug)]
pub struct ValidationState {
    #[serde(rename = "actionType")]
    pub action_type: Option<ActionType>,
    #[serde(rename = "filePath")]
    pub file_path: Option<String>,
    pub errors: Vec<ValidationError>,
}

impl ValidationState {
    #[allow(dead_code)]
    pub fn is_valid(&self) -> bool {
        self.errors.is_empty()
    }
}

impl From<valico::json_schema::ValidationState> for ValidationState {
    fn from(state: valico::json_schema::ValidationState) -> Self {
        ValidationState {
            file_path: None,
            action_type: None,
            errors: state.errors.iter().map(|err| err.into()).collect(),
        }
    }
}

impl From<&valico::json_schema::ValidationState> for ValidationState {
    fn from(state: &valico::json_schema::ValidationState) -> Self {
        ValidationState {
            file_path: None,
            action_type: None,
            errors: state.errors.iter().map(|err| err.into()).collect(),
        }
    }
}
```

## File: `src/js/system.js`
```javascript
const console = require('node:console');
const fs = require('node:fs');
const process = require('node:process');
const fg = require('fast-glob');

module.exports.console = console;
module.exports.fs = fs;
module.exports.process = process;
module.exports.fg = fg;
```

## File: `src/system/console.rs`
```rust
// The below functions have duplicate implementations for WASM and non-WASM targets.
// Each target might not use all of the functions, but they are all defined for both targets
// for simplicity.
#![allow(dead_code)]

#[cfg(feature = "js")]
mod js_console {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(module = "/src/js/system.js")]
    extern "C" {
        #[wasm_bindgen(js_namespace = console, js_name = log)]
        pub fn log(s: &str);

        #[wasm_bindgen(js_namespace = console, js_name = error)]
        pub fn error(s: &str);

        #[wasm_bindgen(js_namespace = console, js_name = warn)]
        pub fn warn(s: &str);
    }
}

#[cfg(feature = "js")]
pub fn log(s: &str) {
    js_console::log(s);
}

#[cfg(not(feature = "js"))]
pub fn log(s: &str) {
    println!("{s}");
}

#[cfg(feature = "js")]
pub fn error(s: &str) {
    js_console::error(s);
}

#[cfg(not(feature = "js"))]
pub fn error(s: &str) {
    eprintln!("{s}");
}

#[cfg(feature = "js")]
pub fn warn(s: &str) {
    js_console::warn(s);
}

#[cfg(not(feature = "js"))]
pub fn warn(s: &str) {
    eprintln!("{s}");
}
```

## File: `src/system/fs.rs`
```rust
// The below functions have duplicate implementations for WASM and non-WASM targets.
// Each target might not use all of the functions, but they are all defined for both targets
// for simplicity.
#![allow(dead_code)]

use std::path::Path;

#[cfg(feature = "js")]
mod js_fs {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(module = "/src/js/system.js")]
    extern "C" {
        #[wasm_bindgen(catch, js_namespace = fs, js_name = readFileSync)]
        pub fn read_file_sync(path: &str, encoding: &str) -> Result<String, js_sys::Error>;
    }
}

#[cfg(feature = "js")]
pub fn read_to_string<P>(path: P) -> Result<String, String>
where
    P: AsRef<Path>,
{
    js_fs::read_file_sync(path.as_ref().to_string_lossy().as_ref(), "utf8")
        .map_err(|e| format!("{}", e.to_string()))
}

#[cfg(not(feature = "js"))]
pub fn read_to_string<P>(path: P) -> Result<String, String>
where
    P: AsRef<Path>,
{
    std::fs::read_to_string(path).map_err(|e| e.to_string())
}
```

## File: `src/system/glob.rs`
```rust
// The below functions have duplicate implementations for WASM and non-WASM targets.
// Each target might not use all of the functions, but they are all defined for both targets
// for simplicity.
#![allow(dead_code)]

#[cfg(feature = "js")]
mod js_fg {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(module = "/src/js/system.js")]
    extern "C" {
        #[wasm_bindgen(js_name = String)]
        type Entry;

        #[wasm_bindgen(catch, js_namespace = fg, js_name = globSync)]
        pub fn glob_sync(pattern: &str) -> Result<Vec<js_sys::Object>, js_sys::Error>;
    }
}

#[cfg(feature = "js")]
pub fn glob_count_matches(pattern: &str) -> Result<usize, String> {
    js_fg::glob_sync(pattern)
        .map(|entries| entries.len())
        .map_err(|e| format!("{}", e.to_string()))
}

#[cfg(not(feature = "js"))]
pub fn glob_count_matches(pattern: &str) -> Result<usize, String> {
    use glob::glob;
    glob(pattern)
        .map(|paths| paths.count())
        .map_err(|e| e.to_string())
}
```

## File: `src/system/mod.rs`
```rust
pub mod console;
pub mod fs;
pub mod glob;
pub mod process;
```

## File: `src/system/process.rs`
```rust
// The below functions have duplicate implementations for WASM and non-WASM targets.
// Each target might not use all of the functions, but they are all defined for both targets
// for simplicity.
#![allow(dead_code)]

#[cfg(feature = "js")]
mod js_process {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(module = "/src/js/system.js")]
    extern "C" {
        #[wasm_bindgen(js_namespace = process, js_name = exit)]
        pub fn exit(code: i32) -> JsValue;

        #[wasm_bindgen(thread_local_v2, js_namespace = ["process", "stdout"], js_name = isTTY)]
        pub static STDOUT_IS_TTY: bool;
    }
}

#[cfg(feature = "js")]
pub fn exit(code: i32) -> ! {
    js_process::exit(code);
    unreachable!();
}

#[cfg(not(feature = "js"))]
pub fn exit(code: i32) -> ! {
    std::process::exit(code);
}

pub mod stdout {
    #[cfg(feature = "js")]
    pub fn is_tty() -> bool {
        use super::js_process;
        js_process::STDOUT_IS_TTY.with(bool::clone)
    }
}
```

## File: `tests/snapshot_tests.rs`
```rust
use fixtures::fixtures;
use std::env::current_dir;
use std::fs::File;
use std::io::BufReader;
use std::path::{Path, PathBuf};
use std::process::Command;
use std::{ffi::OsStr, fs};

static REPO_DIR_WILDCARD: &str = "{{repo}}";

#[derive(Debug, serde::Deserialize)]
struct SnapshotTestConfig {
    cli_args: Option<Vec<String>>,
}

#[derive(Debug)]
struct SnapshotTest {
    config: SnapshotTestConfig,
    current_dir: PathBuf,
    test_dir: PathBuf,
}

impl SnapshotTest {
    fn new(test_dir: &Path) -> Self {
        let test_config_file = test_dir.join("test.json");

        let config: SnapshotTestConfig = serde_json::from_reader(BufReader::new(
            File::open(&test_config_file).expect(&format!(
                "missing test conifg file ({})",
                test_config_file.to_string_lossy(),
            )),
        ))
        .expect(&format!(
            "invalid test config file ({})",
            test_config_file.to_string_lossy(),
        ));

        SnapshotTest {
            config,
            current_dir: current_dir().unwrap(),
            test_dir: test_dir.to_path_buf(),
        }
    }

    fn build_command(&self) -> Command {
        #[cfg(not(feature = "test-js"))]
        {
            Command::new(assert_cmd::cargo::cargo_bin!())
        }

        #[cfg(feature = "test-js")]
        {
            let mut cmd = Command::new("node");
            cmd.arg("packages/cli/cli.mjs");
            cmd
        }
    }

    fn execute(self) {
        use std::ffi::OsString;

        let pwd = self.current_dir.to_str().unwrap();

        let cli_args: Vec<_> = if let Some(cli_args) = &self.config.cli_args {
            cli_args.iter().map(OsString::from).collect()
        } else {
            fs::read_dir(&self.test_dir)
                .unwrap()
                .filter_map(Result::ok)
                .filter(|f| f.path().extension() == Some(OsStr::new("yml")))
                .map(|f| f.path().into_os_string())
                .collect()
        };

        #[cfg(not(feature = "test-save-snapshots"))]
        {
            use assert_cmd::assert::OutputAssertExt as _;

            let stderr = fs::read_to_string(self.test_dir.join("stderr"))
                .unwrap_or(String::from(""))
                .replace(REPO_DIR_WILDCARD, pwd);

            let stdout = fs::read_to_string(self.test_dir.join("stdout"))
                .unwrap_or(String::from(""))
                .replace(REPO_DIR_WILDCARD, pwd);

            let exitcode: i32 = fs::read_to_string(self.test_dir.join("exitcode"))
                .map(|s| {
                    s.strip_suffix("\n")
                        .unwrap_or(s.as_str())
                        .parse::<i32>()
                        .unwrap_or(0)
                })
                .unwrap_or(0);

            self.build_command()
                .args(&cli_args)
                .assert()
                .stdout(stdout)
                .stderr(stderr)
                .code(exitcode);
        }

        #[cfg(feature = "test-save-snapshots")]
        {
            use assert_cmd::output::OutputOkExt as _;
            use std::io::prelude::*;

            let result = self
                .build_command()
                .args(&cli_args)
                .ok()
                .unwrap_or_else(|e| e.as_output().unwrap().to_owned());

            if !result.stdout.is_empty() {
                File::create(self.test_dir.join("stdout"))
                    .unwrap()
                    .write_all(
                        String::from_utf8(result.stdout)
                            .unwrap()
                            .replace(pwd, REPO_DIR_WILDCARD)
                            .as_bytes(),
                    )
                    .unwrap();
            }
            if !result.stderr.is_empty() {
                File::create(self.test_dir.join("stderr"))
                    .unwrap()
                    .write_all(
                        String::from_utf8(result.stderr)
                            .unwrap()
                            .replace(pwd, REPO_DIR_WILDCARD)
                            .as_bytes(),
                    )
                    .unwrap();
            }
            if let Some(exitcode) = result.status.code() {
                if exitcode > 0 {
                    File::create(self.test_dir.join("exitcode"))
                        .unwrap()
                        .write_all(exitcode.to_string().as_bytes())
                        .unwrap();
                }
            }
        }
    }
}

#[fixtures(["tests/fixtures/*"])]
#[cfg_attr(
    feature = "test-js",
    fixtures::ignore(
        paths = "tests/fixtures/013_rejects_gitignore_extended_glob_syntax",
        reason = "The WASM implementation of action validator currently (incorrectly) accepts extended gitignore syntax"
    )
)]
#[test]
fn snapshot(dir: &Path) {
    SnapshotTest::new(dir).execute();
}
```

## File: `tests/fixtures/001_basic_workflow/test.json`
```json
{}
```

## File: `tests/fixtures/001_basic_workflow/test.yml`
```yaml
name: Test

on:
  push:
  pull_request:
    branches:
      - main

defaults:
  run:
    shell: bash

jobs:
  check:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup Rust
        uses: actions-rs/toolchain@v1
        with:
          toolchain: stable
          override: true
          default: true

      - name: Check Formatting
        uses: actions-rs/cargo@v1
        with:
          command: fmt
          args: -- --check

      - name: Check with Clippy
        uses: actions-rs/clippy-check@v1
        with:
          args: -- -Dwarnings
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Shellcheck
        uses: ludeeus/action-shellcheck@master

      - name: Install shfmt
        uses: mfinelli/setup-shfmt@master

      - name: Run shfmt
        run: shfmt -d bin/*


  build:
    strategy:
      matrix:
        rust-toolchain:
          - stable
          - nightly
        os:
          - ubuntu-latest
          - macos-latest
          - windows-latest

    runs-on: ${{ matrix.os }}

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup Rust
        uses: actions-rs/toolchain@v1
        with:
          toolchain: ${{ matrix.rust-toolchain }}
          override: true
          default: true

      - name: Build
        uses: actions-rs/cargo@v1
        with:
          command: build
          args: --release --all-features
```

## File: `tests/fixtures/002_basic_action/action.yml`
```yaml
name: 'Build something'
description: |
  Build something repeatable.

inputs:
  role:
    description: |
      The role of what's being built.
    required: true

runs:
  using: "composite"
  steps:
    - name: "setup"
      shell: bash
      run: |
        ./setup

    - name: "test"
      shell: bash
      run: |
        ./test

    - name: "build"
      shell: bash
      run: |
        ./build ${{ inputs.role }}
```

## File: `tests/fixtures/002_basic_action/test.json`
```json
{}
```

## File: `tests/fixtures/003_successful_globs/excluded_path.json`
```json
{}
```

## File: `tests/fixtures/003_successful_globs/glob.yml`
```yaml
name: Test

on:
  push:
    paths:
      - tests/fixtures/003_successful_globs/*
      - '!tests/fixtures/003_successful_globs/*.json'

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1
```

## File: `tests/fixtures/003_successful_globs/test.json`
```json
{}
```

## File: `tests/fixtures/004_failing_globs/exitcode`
```
1
```

## File: `tests/fixtures/004_failing_globs/glob.yml`
```yaml
name: Bad globs, no biscuit

on:
  push:
    paths:
      - tests/fixtures/004_failing_globs/*.txt

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1
```

## File: `tests/fixtures/004_failing_globs/stderr`
```
Validation failed: ValidationState {
    action_type: Some(
        Workflow,
    ),
    file_path: Some(
        "{{repo}}/tests/fixtures/004_failing_globs/glob.yml",
    ),
    errors: [
        NoFilesMatchingGlob {
            code: "glob_not_matched",
            detail: Some(
                "Glob \"tests/fixtures/004_failing_globs/*.txt\" in /on/push/paths does not match any files",
            ),
            path: "/on/push/paths",
            title: "Glob does not match any files",
        },
    ],
}
```

## File: `tests/fixtures/004_failing_globs/stdout`
```
Fatal error validating {{repo}}/tests/fixtures/004_failing_globs/glob.yml
```

## File: `tests/fixtures/004_failing_globs/test.json`
```json
{}
```

## File: `tests/fixtures/004a_failing_negative_glob/exitcode`
```
1
```

## File: `tests/fixtures/004a_failing_negative_glob/glob.yml`
```yaml
name: Bad globs, no biscuit

on:
  push:
    paths:
      - '!tests/fixtures/004a_failing_negative_glob/*.txt'

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1
```

## File: `tests/fixtures/004a_failing_negative_glob/stderr`
```
Validation failed: ValidationState {
    action_type: Some(
        Workflow,
    ),
    file_path: Some(
        "{{repo}}/tests/fixtures/004a_failing_negative_glob/glob.yml",
    ),
    errors: [
        NoFilesMatchingGlob {
            code: "glob_not_matched",
            detail: Some(
                "Glob \"!tests/fixtures/004a_failing_negative_glob/*.txt\" in /on/push/paths does not match any files",
            ),
            path: "/on/push/paths",
            title: "Glob does not match any files",
        },
    ],
}
```

## File: `tests/fixtures/004a_failing_negative_glob/stdout`
```
Fatal error validating {{repo}}/tests/fixtures/004a_failing_negative_glob/glob.yml
```

## File: `tests/fixtures/004a_failing_negative_glob/test.json`
```json
{}
```

## File: `tests/fixtures/005_conditional_step_in_action/action.yml`
```yaml
name: 'Build something conditionally'
description: |
  Build something repeatable.

inputs:
  role:
    description: |
      The role of what's being built.
    required: true

runs:
  using: "composite"
  steps:
    - name: "setup"
      shell: bash
      run: |
        ./setup

    - name: "test"
      shell: bash
      if: ${{ inputs.role }} == 'tester'
      run: |
        ./test

    - name: "build"
      shell: bash
      run: |
        ./build ${{ inputs.role }}
```

## File: `tests/fixtures/005_conditional_step_in_action/test.json`
```json
{}
```

## File: `tests/fixtures/006_workflow_dispatch_inputs_options/test.json`
```json
{}
```

## File: `tests/fixtures/006_workflow_dispatch_inputs_options/test.yml`
```yaml
name: Test

'on':
  workflow_dispatch:
    inputs:
      ApplicationName:
        description: 'Application name'
        required: true
        type: choice
        options:
          - SomeName
          - SomeOtherName
          - YetMoarNames
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Build
        uses: actions/build@v1
```

## File: `tests/fixtures/007_funky_syntax/exitcode`
```
1
```

## File: `tests/fixtures/007_funky_syntax/rust-check.yml`
```yaml
# From https://github.com/umccr/reusable-github-actions/blob/45fa579dfaceeec903d1b01396c552fc1b72ace9/.github/workflows/rust-check.yaml,
# re: https://github.com/mpalmer/action-validator/issues/14
on:
  workflow_call:
    inputs:
      rust-version:
        type: string
        required: false
        default: nightly

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Check out
        uses: actions/checkout@v3
      - name: Install Rust
        uses: actions-rs/toolchain@v1
        with:
          profile: minimal
          toolchain: ${{ inputs.rust-version }}
          override: true
          components: rustfmt, clippy
      - name: Set up cargo cache
        uses: actions/cache@v3
        continue-on-error: false
        with:
          path: |
            ~/.cargo/bin/
            ~/.cargo/registry/index/
            ~/.cargo/registry/cache/
            ~/.cargo/git/db/
            target/
          key: ${{ runner.os }}-cargo-${{ hashFiles('**/Cargo.toml') }}

      - name: Format
        uses: actions-rs/cargo@v1
          with:
            command: fmt
            args: --all -- --check
      - name: Clippy
        uses: actions-rs/cargo@v1
          with:
            command: clippy
            args: -- -D warnings
      - name: Install
        uses: actions-rs/cargo@v1
          with:
            command: install
            args: cargo-deny cargo-outdated cargo-udeps cargo-audit cargo-pants
      - name: Check
        run: |
          #cargo deny check
          cargo outdated
          #cargo udeps
          #cargo audit
          cargo pants
```

## File: `tests/fixtures/007_funky_syntax/stderr`
```
Validation failed: ValidationState {
    action_type: Some(
        Workflow,
    ),
    file_path: Some(
        "{{repo}}/tests/fixtures/007_funky_syntax/rust-check.yml",
    ),
    errors: [
        Parse {
            code: "parse_error",
            detail: Some(
                "mapping values are not allowed in this context at line 38 column 15",
            ),
            path: "",
            title: "Parse Error",
            location: Some(
                ParseErrorLocation {
                    index: 1069,
                    line: 38,
                    column: 15,
                },
            ),
        },
    ],
}
```

## File: `tests/fixtures/007_funky_syntax/stdout`
```
Fatal error validating {{repo}}/tests/fixtures/007_funky_syntax/rust-check.yml
```

## File: `tests/fixtures/007_funky_syntax/test.json`
```json
{}
```

## File: `tests/fixtures/008_job_dependencies/exitcode`
```
1
```

## File: `tests/fixtures/008_job_dependencies/stderr`
```
Validation failed: ValidationState {
    action_type: Some(
        Workflow,
    ),
    file_path: Some(
        "{{repo}}/tests/fixtures/008_job_dependencies/test.yml",
    ),
    errors: [
        UnresolvedJob {
            code: "unresolved_job",
            detail: Some(
                "unresolved job asdf",
            ),
            path: "/jobs/build/needs",
            title: "Unresolved job",
        },
    ],
}
```

## File: `tests/fixtures/008_job_dependencies/stdout`
```
Fatal error validating {{repo}}/tests/fixtures/008_job_dependencies/test.yml
```

## File: `tests/fixtures/008_job_dependencies/test.json`
```json
{}
```

## File: `tests/fixtures/008_job_dependencies/test.yml`
```yaml
name: Test

on:
  push:
  pull_request:
    branches:
      - main

jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - run: echo "setup"
  check:
    runs-on: ubuntu-latest
    needs: setup
    steps:
      - run: echo "check"
  build:
    runs-on: ubuntu-latest
    needs:
      - check
      - asdf
    steps:
      - run: echo "build"
```

## File: `tests/fixtures/009_multi_file/exitcode`
```
1
```

## File: `tests/fixtures/009_multi_file/stderr`
```
Validation failed: ValidationState {
    action_type: Some(
        Workflow,
    ),
    file_path: Some(
        "{{repo}}/tests/fixtures/009_multi_file/xinvalid.yml",
    ),
    errors: [
        Parse {
            code: "parse_error",
            detail: Some(
                "mapping values are not allowed in this context at line 36 column 15",
            ),
            path: "",
            title: "Parse Error",
            location: Some(
                ParseErrorLocation {
                    index: 872,
                    line: 36,
                    column: 15,
                },
            ),
        },
    ],
}
```

## File: `tests/fixtures/009_multi_file/stdout`
```
Fatal error validating {{repo}}/tests/fixtures/009_multi_file/xinvalid.yml
```

## File: `tests/fixtures/009_multi_file/test.json`
```json
{}
```

## File: `tests/fixtures/009_multi_file/valid.yml`
```yaml
on:
  workflow_call:
    inputs:
      rust-version:
        type: string
        required: false
        default: nightly

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Check out
        uses: actions/checkout@v3
      - name: Install Rust
        uses: actions-rs/toolchain@v1
        with:
          profile: minimal
          toolchain: ${{ inputs.rust-version }}
          override: true
          components: rustfmt, clippy
      - name: Set up cargo cache
        uses: actions/cache@v3
        continue-on-error: false
        with:
          path: |
            ~/.cargo/bin/
            ~/.cargo/registry/index/
            ~/.cargo/registry/cache/
            ~/.cargo/git/db/
            target/
          key: ${{ runner.os }}-cargo-${{ hashFiles('**/Cargo.toml') }}

      - name: Format
        uses: actions-rs/cargo@v1
        with:
          command: fmt
          args: --all -- --check
      - name: Clippy
        uses: actions-rs/cargo@v1
        with:
          command: clippy
          args: -- -D warnings
      - name: Install
        uses: actions-rs/cargo@v1
        with:
          command: install
          args: cargo-deny cargo-outdated cargo-udeps cargo-audit cargo-pants
      - name: Check
        run: |
          #cargo deny check
          cargo outdated
          #cargo udeps
          #cargo audit
          cargo pants
```

## File: `tests/fixtures/009_multi_file/xinvalid.yml`
```yaml
on:
  workflow_call:
    inputs:
      rust-version:
        type: string
        required: false
        default: nightly

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Check out
        uses: actions/checkout@v3
      - name: Install Rust
        uses: actions-rs/toolchain@v1
        with:
          profile: minimal
          toolchain: ${{ inputs.rust-version }}
          override: true
          components: rustfmt, clippy
      - name: Set up cargo cache
        uses: actions/cache@v3
        continue-on-error: false
        with:
          path: |
            ~/.cargo/bin/
            ~/.cargo/registry/index/
            ~/.cargo/registry/cache/
            ~/.cargo/git/db/
            target/
          key: ${{ runner.os }}-cargo-${{ hashFiles('**/Cargo.toml') }}

      - name: Format
        uses: actions-rs/cargo@v1
          with:
            command: fmt
            args: --all -- --check
      - name: Clippy
        uses: actions-rs/cargo@v1
          with:
            command: clippy
            args: -- -D warnings
      - name: Install
        uses: actions-rs/cargo@v1
          with:
            command: install
            args: cargo-deny cargo-outdated cargo-udeps cargo-audit cargo-pants
      - name: Check
        run: |
          #cargo deny check
          cargo outdated
          #cargo udeps
          #cargo audit
          cargo pants
```

## File: `tests/fixtures/010_missing_shell_in_action/action.yml`
```yaml
name: 'missing shell'
description: ''

runs:
  using: "composite"
  steps:
    - name: "say hello"
      run: |
        echo "Hello world"
```

## File: `tests/fixtures/010_missing_shell_in_action/exitcode`
```
1
```

## File: `tests/fixtures/010_missing_shell_in_action/stderr`
```
Validation failed: ValidationState {
    action_type: Some(
        Action,
    ),
    file_path: Some(
        "{{repo}}/tests/fixtures/010_missing_shell_in_action/action.yml",
    ),
    errors: [
        OneOf {
            code: "one_of",
            detail: None,
            path: "/runs",
            title: "OneOf conditions are not met",
            states: [
                ValidationState {
                    action_type: None,
                    file_path: None,
                    errors: [
                        Properties {
                            code: "properties",
                            detail: Some(
                                "Additional property 'steps' is not allowed",
                            ),
                            path: "/runs",
                            title: "Property conditions are not met",
                        },
                        Enum {
                            code: "enum",
                            detail: None,
                            path: "/runs/using",
                            title: "Enum conditions are not met",
                        },
                        Required {
                            code: "required",
                            detail: None,
                            path: "/runs/main",
                            title: "This property is required",
                        },
                    ],
                },
                ValidationState {
                    action_type: None,
                    file_path: None,
                    errors: [
                        OneOf {
                            code: "one_of",
                            detail: None,
                            path: "/runs/steps/0",
                            title: "OneOf conditions are not met",
                            states: [
                                ValidationState {
                                    action_type: None,
                                    file_path: None,
                                    errors: [
                                        Required {
                                            code: "required",
                                            detail: None,
                                            path: "/runs/steps/0/shell",
                                            title: "This property is required",
                                        },
                                    ],
                                },
                                ValidationState {
                                    action_type: None,
                                    file_path: None,
                                    errors: [
                                        Required {
                                            code: "required",
                                            detail: None,
                                            path: "/runs/steps/0/uses",
                                            title: "This property is required",
                                        },
                                    ],
                                },
                            ],
                        },
                    ],
                },
                ValidationState {
                    action_type: None,
                    file_path: None,
                    errors: [
                        Properties {
                            code: "properties",
                            detail: Some(
                                "Additional property 'steps' is not allowed",
                            ),
                            path: "/runs",
                            title: "Property conditions are not met",
                        },
                        Const {
                            code: "const",
                            detail: None,
                            path: "/runs/using",
                            title: "Const condition is not met",
                        },
                        Required {
                            code: "required",
                            detail: None,
                            path: "/runs/image",
                            title: "This property is required",
                        },
                    ],
                },
            ],
        },
    ],
}
```

## File: `tests/fixtures/010_missing_shell_in_action/stdout`
```
Fatal error validating {{repo}}/tests/fixtures/010_missing_shell_in_action/action.yml
```

## File: `tests/fixtures/010_missing_shell_in_action/test.json`
```json
{}
```

## File: `tests/fixtures/011_subdir_globs/test.json`
```json
{
  "cli_args": ["--rootdir", "tests/fixtures/011_subdir_globs/subdir", "tests/fixtures/011_subdir_globs/subdir/glob.yml"]
}
```

## File: `tests/fixtures/011_subdir_globs/subdir/glob.yml`
```yaml
name: Test

on:
  push:
    paths:
      - g*.yml
      - '!*.json'

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1
```

## File: `tests/fixtures/012_github_glob_syntax/glob.yml`
```yaml
name: Test

on:
  push:
    # See https://chatgpt.com/c/68f9f77c-6c40-832c-8197-5d5698de0d6e
    # Currently supported:
    #  - "*" ✅
    #  - "**" ✅
    #  - "?" ✅
    #  - "+" 🚫
    #  - "[]" ✅
    #  - "!" ✅
    paths:
      - tests/fixtures/012_github_glob_syntax/subdir/artefact.*
      - tests/fixtures/012_github_glob_syntax/**/artefact.a
      - tests/fixtures/012_github_glob_syntax/subdir/artefact.?
      # - tests/fixtures/012_github_glob_syntax/subdir/artefact+
      - tests/fixtures/012_github_glob_syntax/subdir/artefact.[bc]
      - tests/fixtures/012_github_glob_syntax/subdir/[0-9]00
      - '!tests/fixtures/012_github_glob_syntax/subdir/ignore'

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1
```

## File: `tests/fixtures/012_github_glob_syntax/test.json`
```json
{}
```

## File: `tests/fixtures/012_github_glob_syntax/subdir/artefact.a`
```
{}
```

## File: `tests/fixtures/013_rejects_gitignore_extended_glob_syntax/exitcode`
```
1
```

## File: `tests/fixtures/013_rejects_gitignore_extended_glob_syntax/glob.yml`
```yaml
name: Test

on:
  push:
    paths:
      # The {} syntax is not supported by GitHub actions.
      - tests/fixtures/013_rejects_gitignore_extended_glob_syntax/subdir/asset.{js,jsx}

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1
```

## File: `tests/fixtures/013_rejects_gitignore_extended_glob_syntax/stderr`
```
Validation failed: ValidationState {
    action_type: Some(
        Workflow,
    ),
    file_path: Some(
        "{{repo}}/tests/fixtures/013_rejects_gitignore_extended_glob_syntax/glob.yml",
    ),
    errors: [
        NoFilesMatchingGlob {
            code: "glob_not_matched",
            detail: Some(
                "Glob \"tests/fixtures/013_rejects_gitignore_extended_glob_syntax/subdir/asset.{js,jsx}\" in /on/push/paths does not match any files",
            ),
            path: "/on/push/paths",
            title: "Glob does not match any files",
        },
    ],
}
```

## File: `tests/fixtures/013_rejects_gitignore_extended_glob_syntax/stdout`
```
Fatal error validating {{repo}}/tests/fixtures/013_rejects_gitignore_extended_glob_syntax/glob.yml
```

## File: `tests/fixtures/013_rejects_gitignore_extended_glob_syntax/test.json`
```json
{}
```

