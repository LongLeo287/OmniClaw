---
id: metube-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:07.750122
---

# KNOWLEDGE EXTRACT: metube
> **Extracted on:** 2026-03-30 17:42:47
> **Source:** metube

---

## File: `.dockerignore`
```
.git
.venv
ui/.angular
ui/node_modules
```

## File: `.editorconfig`
```
# Editor configuration, see https://editorconfig.org
root = true

[*]
charset = utf-8
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
max_line_length = off
trim_trailing_whitespace = false

[*.py]
indent_size = 4
```

## File: `.gitignore`
```
# compiled output
/ui/dist
/ui/tmp
/ui/out-tsc
# Only exists if Bazel was run
/ui/bazel-out

# dependencies
/ui/node_modules
/ui/package-lock.json

# profiling files
chrome-profiler-events*.json
speed-measure-plugin*.json

# IDEs and editors
/ui/.idea
.project
.classpath
.c9/
*.launch
.settings/
*.sublime-workspace

# IDE - VSCode
.vscode/*
#!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history/*

# misc
/ui/.sass-cache
/ui/.angular
/ui/connect.lock
/ui/coverage
/ui/libpeerconnection.log
npm-debug.log
yarn-error.log
testem.log
/ui/typings

# System Files
.DS_Store
Thumbs.db

# MeTube runtime databases
queue*
completed*
pending*

__pycache__
.venv
```

## File: `docker-entrypoint.sh`
```bash
#!/bin/sh

PUID="${UID:-$PUID}"
PGID="${GID:-$PGID}"

echo "Setting umask to ${UMASK}"
umask ${UMASK}
echo "Creating download directory (${DOWNLOAD_DIR}), state directory (${STATE_DIR}), and temp dir (${TEMP_DIR})"
mkdir -p "${DOWNLOAD_DIR}" "${STATE_DIR}" "${TEMP_DIR}"

if [ `id -u` -eq 0 ] && [ `id -g` -eq 0 ]; then
    if [ "${PUID}" -eq 0 ]; then
        echo "Warning: it is not recommended to run as root user, please check your setting of the PUID/PGID (or legacy UID/GID) environment variables"
    fi
    if [ "${CHOWN_DIRS:-true}" != "false" ]; then
        echo "Changing ownership of download and state directories to ${PUID}:${PGID}"
        chown -R "${PUID}":"${PGID}" /app "${DOWNLOAD_DIR}" "${STATE_DIR}" "${TEMP_DIR}"
    fi
    echo "Starting BgUtils POT Provider"
    gosu "${PUID}":"${PGID}" bgutil-pot server >/tmp/bgutil-pot.log 2>&1 &
    echo "Running MeTube as user ${PUID}:${PGID}"
    exec gosu "${PUID}":"${PGID}" python3 app/main.py
else
    echo "User set by docker; running MeTube as `id -u`:`id -g`"
    echo "Starting BgUtils POT Provider"
    bgutil-pot server >/tmp/bgutil-pot.log 2>&1 &
    exec python3 app/main.py
fi
```

## File: `Dockerfile`
```
FROM node:lts-alpine AS builder

WORKDIR /metube
COPY ui ./
RUN corepack enable && corepack prepare pnpm --activate
RUN CI=true pnpm install && pnpm run build


FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock docker-entrypoint.sh ./

# Use sed to strip carriage-return characters from the entrypoint script (in case building on Windows)
# Install dependencies
RUN sed -i 's/\r$//g' docker-entrypoint.sh && \
    chmod +x docker-entrypoint.sh && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
      ca-certificates \
      ffmpeg \
      unzip \
      aria2 \
      coreutils \
      gosu \
      curl \
      tini \
      file \
      gdbmtool \
      sqlite3 \
      build-essential && \
    curl -LsSf https://astral.sh/uv/install.sh | UV_INSTALL_DIR=/usr/local/bin sh && \
    UV_PROJECT_ENVIRONMENT=/usr/local uv sync --frozen --no-dev --compile-bytecode && \
    uv cache clean && \
    rm -f /usr/local/bin/uv /usr/local/bin/uvx /usr/local/bin/uvw && \
    curl -fsSL https://deno.land/install.sh | DENO_INSTALL=/usr/local sh -s -- -y && \
    apt-get purge -y --auto-remove build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /.cache && chmod 777 /.cache

ARG TARGETARCH

RUN BGUTIL_TAG="$(curl -Ls -o /dev/null -w '%{url_effective}' https://github.com/jim60105/bgutil-ytdlp-pot-provider-rs/releases/latest | sed 's#.*/tag/##')" && \
    case "$TARGETARCH" in \
      amd64) BGUTIL_ARCH="x86_64" ;; \
      arm64) BGUTIL_ARCH="aarch64" ;; \
      *) echo "Unsupported TARGETARCH: $TARGETARCH" >&2; exit 1 ;; \
    esac && \
    curl -L -o /usr/local/bin/bgutil-pot \
      "https://github.com/jim60105/bgutil-ytdlp-pot-provider-rs/releases/download/${BGUTIL_TAG}/bgutil-pot-linux-${BGUTIL_ARCH}" && \
    chmod +x /usr/local/bin/bgutil-pot && \
    PLUGIN_DIR="$(python3 -c 'import site; print(site.getsitepackages()[0])')" && \
    curl -L -o /tmp/bgutil-ytdlp-pot-provider-rs.zip \
      "https://github.com/jim60105/bgutil-ytdlp-pot-provider-rs/releases/download/${BGUTIL_TAG}/bgutil-ytdlp-pot-provider-rs.zip" && \
    unzip -q /tmp/bgutil-ytdlp-pot-provider-rs.zip -d "${PLUGIN_DIR}" && \
    rm /tmp/bgutil-ytdlp-pot-provider-rs.zip

COPY app ./app
COPY --from=builder /metube/dist/metube ./ui/dist/metube

ENV PUID=1000
ENV PGID=1000
ENV UMASK=022

ENV DOWNLOAD_DIR /downloads
ENV STATE_DIR /downloads/.metube
ENV TEMP_DIR /downloads
VOLUME /downloads
EXPOSE 8081

# Add build-time argument for version
ARG VERSION=dev
ENV METUBE_VERSION=$VERSION

ENTRYPOINT ["/usr/bin/tini", "-g", "--", "./docker-entrypoint.sh"]
```

## File: `LICENSE`
```
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU Affero General Public License is a free, copyleft license for
software and other kinds of works, specifically designed to ensure
cooperation with the community in the case of network server software.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
our General Public Licenses are intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  Developers that use our General Public Licenses protect your rights
with two steps: (1) assert copyright on the software, and (2) offer
you this License which gives you legal permission to copy, distribute
and/or modify the software.

  A secondary benefit of defending all users' freedom is that
improvements made in alternate versions of the program, if they
receive widespread use, become available for other developers to
incorporate.  Many developers of free software are heartened and
encouraged by the resulting cooperation.  However, in the case of
software used on network servers, this result may fail to come about.
The GNU General Public License permits making a modified version and
letting the public access it on a server without ever releasing its
source code to the public.

  The GNU Affero General Public License is designed specifically to
ensure that, in such cases, the modified source code becomes available
to the community.  It requires the operator of a network server to
provide the source code of the modified version running there to the
users of that server.  Therefore, public use of a modified version, on
a publicly accessible server, gives the public access to the source
code of the modified version.

  An older license, called the Affero General Public License and
published by Affero, was designed to accomplish similar goals.  This is
a different license, not a version of the Affero GPL, but Affero has
released a new version of the Affero GPL which permits relicensing under
this license.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU Affero General Public License.

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

  13. Remote Network Interaction; Use with the GNU General Public License.

  Notwithstanding any other provision of this License, if you modify the
Program, your modified version must prominently offer all users
interacting with it remotely through a computer network (if your version
supports such interaction) an opportunity to receive the Corresponding
Source of your version by providing access to the Corresponding Source
from a network server at no charge, through some standard or customary
means of facilitating copying of software.  This Corresponding Source
shall include the Corresponding Source for any work covered by version 3
of the GNU General Public License that is incorporated pursuant to the
following paragraph.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the work with which it is combined will remain governed by version
3 of the GNU General Public License.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU Affero General Public License from time to time.  Such new versions
will be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU Affero General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU Affero General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU Affero General Public License can be used, that proxy's
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
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If your software can interact with users remotely through a computer
network, you should also make sure that it provides a way for users to
get its source.  For example, if your program is a web application, its
interface could display a "Source" link that leads users to an archive
of the code.  There are many ways you could offer source, and different
solutions will be better for different programs; see section 13 for the
specific requirements.

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU AGPL, see
<https://www.gnu.org/licenses/>.
```

## File: `pyproject.toml`
```
[project]
name = "metube"
version = "0.1.0"
description = "Web GUI for youtube-dl (using yt-dlp) with playlist support"
requires-python = ">=3.13"
dependencies = [
    "aiohttp",
    "python-socketio>=5.0,<6.0",
    "yt-dlp[default,curl-cffi,deno]",
    "mutagen",
    "curl-cffi",
    "watchfiles",
]

[dependency-groups]
dev = [
    "pylint",
]
```

## File: `README.md`
```markdown
# MeTube

![Build Status](https://github.com/alexta69/metube/actions/workflows/main.yml/badge.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/alexta69/metube.svg)

Web GUI for youtube-dl (using the [yt-dlp](https://github.com/yt-dlp/yt-dlp) fork) with playlist support. Allows you to download videos from YouTube and [dozens of other sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

![screenshot1](https://github.com/alexta69/metube/raw/master/screenshot.gif)

## 🐳 Run using Docker

```bash
docker run -d -p 8081:8081 -v /path/to/downloads:/downloads ghcr.io/alexta69/metube
```

## 🐳 Run using docker-compose

```yaml
services:
  metube:
    image: ghcr.io/alexta69/metube
    container_name: metube
    restart: unless-stopped
    ports:
      - "8081:8081"
    volumes:
      - /path/to/downloads:/downloads
```

## ⚙️ Configuration via environment variables

Certain values can be set via environment variables, using the `-e` parameter on the docker command line, or the `environment:` section in docker-compose.

### ⬇️ Download Behavior

* __MAX_CONCURRENT_DOWNLOADS__: Maximum number of simultaneous downloads allowed. For example, if set to `5`, then at most five downloads will run concurrently, and any additional downloads will wait until one of the active downloads completes. Defaults to `3`. 
* __DELETE_FILE_ON_TRASHCAN__: if `true`, downloaded files are deleted on the server, when they are trashed from the "Completed" section of the UI. Defaults to `false`.
* __DEFAULT_OPTION_PLAYLIST_ITEM_LIMIT__: Maximum number of playlist items that can be downloaded. Defaults to `0` (no limit).
* __CLEAR_COMPLETED_AFTER__: Number of seconds after which completed (and failed) downloads are automatically removed from the "Completed" list. Defaults to `0` (disabled).

### 📁 Storage & Directories

* __DOWNLOAD_DIR__: Path to where the downloads will be saved. Defaults to `/downloads` in the Docker image, and `.` otherwise.
* __AUDIO_DOWNLOAD_DIR__: Path to where audio-only downloads will be saved, if you wish to separate them from the video downloads. Defaults to the value of `DOWNLOAD_DIR`.
* __CUSTOM_DIRS__: Whether to enable downloading videos into custom directories within the __DOWNLOAD_DIR__ (or __AUDIO_DOWNLOAD_DIR__). When enabled, a dropdown appears next to the Add button to specify the download directory. Defaults to `true`.
* __CREATE_CUSTOM_DIRS__: Whether to support automatically creating directories within the __DOWNLOAD_DIR__ (or __AUDIO_DOWNLOAD_DIR__) if they do not exist. When enabled, the download directory selector supports free-text input, and the specified directory will be created recursively. Defaults to `true`.
* __CUSTOM_DIRS_EXCLUDE_REGEX__: Regular expression to exclude some custom directories from the dropdown. Empty regex disables exclusion. Defaults to `(^|/)[.@].*$`, which means directories starting with `.` or `@`.
* __DOWNLOAD_DIRS_INDEXABLE__: If `true`, the download directories (__DOWNLOAD_DIR__ and __AUDIO_DOWNLOAD_DIR__) are indexable on the web server. Defaults to `false`.
* __STATE_DIR__: Path to where the queue persistence files will be saved. Defaults to `/downloads/.metube` in the Docker image, and `.` otherwise.
* __TEMP_DIR__: Path where intermediary download files will be saved. Defaults to `/downloads` in the Docker image, and `.` otherwise.
  * Set this to an SSD or RAM filesystem (e.g., `tmpfs`) for better performance.
  * __Note__: Using a RAM filesystem may prevent downloads from being resumed.
* __CHOWN_DIRS__: If `false`, ownership of `DOWNLOAD_DIR`, `STATE_DIR`, and `TEMP_DIR` (and their contents) will not be set on container start. Ensure user under which MeTube runs has necessary access to these directories already. Defaults to `true`.

### 📝 File Naming & yt-dlp

* __OUTPUT_TEMPLATE__: The template for the filenames of the downloaded videos, formatted according to [this spec](https://github.com/yt-dlp/yt-dlp/blob/master/README.md#output-template). Defaults to `%(title)s.%(ext)s`.
* __OUTPUT_TEMPLATE_CHAPTER__: The template for the filenames of the downloaded videos when split into chapters via postprocessors. Defaults to `%(title)s - %(section_number)s %(section_title)s.%(ext)s`.
* __OUTPUT_TEMPLATE_PLAYLIST__: The template for the filenames of the downloaded videos when downloaded as a playlist. Defaults to `%(playlist_title)s/%(title)s.%(ext)s`. Set to empty to use `OUTPUT_TEMPLATE` instead.
* __OUTPUT_TEMPLATE_CHANNEL__: The template for the filenames of the downloaded videos when downloaded as a channel. Defaults to `%(channel)s/%(title)s.%(ext)s`. Set to empty to use `OUTPUT_TEMPLATE` instead.
* __YTDL_OPTIONS__: Additional options to pass to yt-dlp in JSON format. [See available options here](https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L222). They roughly correspond to command-line options, though some do not have exact equivalents here. For example, `--recode-video` has to be specified via `postprocessors`. Also note that dashes are replaced with underscores. You may find [this script](https://github.com/yt-dlp/yt-dlp/blob/master/devscripts/cli_to_api.py) helpful for converting from command-line options to `YTDL_OPTIONS`.
* __YTDL_OPTIONS_FILE__: A path to a JSON file that will be loaded and used for populating `YTDL_OPTIONS` above. Please note that if both `YTDL_OPTIONS_FILE` and `YTDL_OPTIONS` are specified, the options in `YTDL_OPTIONS` take precedence. The file will be monitored for changes and reloaded automatically when changes are detected.

### 🌐 Web Server & URLs

* __HOST__: The host address the web server will bind to. Defaults to `0.0.0.0` (all interfaces).
* __PORT__: The port number the web server will listen on. Defaults to `8081`.
* __URL_PREFIX__: Base path for the web server (for use when hosting behind a reverse proxy). Defaults to `/`.
* __PUBLIC_HOST_URL__: Base URL for the download links shown in the UI for completed files. By default, MeTube serves them under its own URL. If your download directory is accessible on another URL and you want the download links to be based there, use this variable to set it.
* __PUBLIC_HOST_AUDIO_URL__: Same as PUBLIC_HOST_URL but for audio downloads.
* __HTTPS__: Use `https` instead of `http` (__CERTFILE__ and __KEYFILE__ required). Defaults to `false`.
* __CERTFILE__: HTTPS certificate file path.
* __KEYFILE__: HTTPS key file path.
* __ROBOTS_TXT__: A path to a `robots.txt` file mounted in the container.

### 🏠 Basic Setup

* __PUID__: User under which MeTube will run. Defaults to `1000` (legacy `UID` also supported).
* __PGID__: Group under which MeTube will run. Defaults to `1000` (legacy `GID` also supported).
* __UMASK__: Umask value used by MeTube. Defaults to `022`.
* __DEFAULT_THEME__: Default theme to use for the UI, can be set to `light`, `dark`, or `auto`. Defaults to `auto`.
* __LOGLEVEL__: Log level, can be set to `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`, or `NONE`. Defaults to `INFO`. 
* __ENABLE_ACCESSLOG__: Whether to enable access log. Defaults to `false`.

The project's Wiki contains examples of useful configurations contributed by users of MeTube:
* [YTDL_OPTIONS Cookbook](https://github.com/alexta69/metube/wiki/YTDL_OPTIONS-Cookbook)
* [OUTPUT_TEMPLATE Cookbook](https://github.com/alexta69/metube/wiki/OUTPUT_TEMPLATE-Cookbook)

## 🍪 Using browser cookies

In case you need to use your browser's cookies with MeTube, for example to download restricted or private videos:

* Install in your browser an extension to extract cookies:
  * [Firefox](https://addons.mozilla.org/en-US/firefox/addon/export-cookies-txt/)
  * [Chrome](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
* Extract the cookies you need with the extension and save/export them as `cookies.txt`.
* In MeTube, open **Advanced Options** and use the **Upload Cookies** button to upload the file.
* After upload, the cookie indicator should show as active.
* Use **Delete Cookies** in the same section to remove uploaded cookies.

## 🔌 Browser extensions

Browser extensions allow right-clicking videos and sending them directly to MeTube. Please note that if you're on an HTTPS page, your MeTube instance must be behind an HTTPS reverse proxy (see below) for the extensions to work.

__Chrome:__ contributed by [Rpsl](https://github.com/rpsl). You can install it from [Google Chrome Webstore](https://chrome.google.com/webstore/detail/metube-downloader/fbmkmdnlhacefjljljlbhkodfmfkijdh) or use developer mode and install [from sources](https://github.com/Rpsl/metube-browser-extension).

__Firefox:__ contributed by [nanocortex](https://github.com/nanocortex). You can install it from [Firefox Addons](https://addons.mozilla.org/en-US/firefox/addon/metube-downloader) or get sources from [here](https://github.com/nanocortex/metube-firefox-addon).

## 📱 iOS Shortcut

[rithask](https://github.com/rithask) created an iOS shortcut to send URLs to MeTube from Safari. Enter the MeTube instance address when prompted which will be saved for later use. You can run the shortcut from Safari’s share menu. The shortcut can be downloaded from [this iCloud link](https://www.icloud.com/shortcuts/66627a9f334c467baabdb2769763a1a6).

## 📱 iOS Compatibility

iOS has strict requirements for video files, requiring h264 or h265 video codec and aac audio codec in MP4 container. This can sometimes be a lower quality than the best quality available. To accommodate iOS requirements, when downloading a MP4 format you can choose "Best (iOS)" to get the best quality formats as compatible as possible with iOS requirements.

To force all downloads to be converted to an iOS-compatible codec, insert this as an environment variable: 

```yaml
  environment:
    - 'YTDL_OPTIONS={"format": "best", "exec": "ffmpeg -i %(filepath)q -c:v libx264 -c:a aac %(filepath)q.h264.mp4"}'
```

## 🔖 Bookmarklet

[kushfest](https://github.com/kushfest) has created a Chrome bookmarklet for sending the currently open webpage to MeTube. Please note that if you're on an HTTPS page, your MeTube instance must be configured with `HTTPS` as `true` in the environment, or be behind an HTTPS reverse proxy (see below) for the bookmarklet to work.

GitHub doesn't allow embedding JavaScript as a link, so the bookmarklet has to be created manually by copying the following code to a new bookmark you create on your bookmarks bar. Change the hostname in the URL below to point to your MeTube instance.

```javascript
javascript:!function(){xhr=new XMLHttpRequest();xhr.open("POST","https://metube.domain.com/add");xhr.withCredentials=true;xhr.send(JSON.stringify({"url":document.location.href,"quality":"best"}));xhr.onload=function(){if(xhr.status==200){alert("Sent to metube!")}else{alert("Send to metube failed. Check the javascript console for clues.")}}}();
```

[shoonya75](https://github.com/shoonya75) has contributed a Firefox version:

```javascript
javascript:(function(){xhr=new XMLHttpRequest();xhr.open("POST","https://metube.domain.com/add");xhr.send(JSON.stringify({"url":document.location.href,"quality":"best"}));xhr.onload=function(){if(xhr.status==200){alert("Sent to metube!")}else{alert("Send to metube failed. Check the javascript console for clues.")}}})();
```

The above bookmarklets use `alert()` as a success/failure notification. The following will show a toast message instead:

Chrome:

```javascript
javascript:!function(){function notify(msg) {var sc = document.scrollingElement.scrollTop; var text = document.createElement('span');text.innerHTML=msg;var ts = text.style;ts.all = 'revert';ts.color = '#000';ts.fontFamily = 'Verdana, sans-serif';ts.fontSize = '15px';ts.backgroundColor = 'white';ts.padding = '15px';ts.border = '1px solid gainsboro';ts.boxShadow = '3px 3px 10px';ts.zIndex = '100';document.body.appendChild(text);ts.position = 'absolute'; ts.top = 50 + sc + 'px'; ts.left = (window.innerWidth / 2)-(text.offsetWidth / 2) + 'px'; setTimeout(function () { text.style.visibility = "hidden"; }, 1500);}xhr=new XMLHttpRequest();xhr.open("POST","https://metube.domain.com/add");xhr.send(JSON.stringify({"url":document.location.href,"quality":"best"}));xhr.onload=function() { if(xhr.status==200){notify("Sent to metube!")}else {notify("Send to metube failed. Check the javascript console for clues.")}}}();
```

Firefox:

```javascript
javascript:(function(){function notify(msg) {var sc = document.scrollingElement.scrollTop; var text = document.createElement('span');text.innerHTML=msg;var ts = text.style;ts.all = 'revert';ts.color = '#000';ts.fontFamily = 'Verdana, sans-serif';ts.fontSize = '15px';ts.backgroundColor = 'white';ts.padding = '15px';ts.border = '1px solid gainsboro';ts.boxShadow = '3px 3px 10px';ts.zIndex = '100';document.body.appendChild(text);ts.position = 'absolute'; ts.top = 50 + sc + 'px'; ts.left = (window.innerWidth / 2)-(text.offsetWidth / 2) + 'px'; setTimeout(function () { text.style.visibility = "hidden"; }, 1500);}xhr=new XMLHttpRequest();xhr.open("POST","https://metube.domain.com/add");xhr.send(JSON.stringify({"url":document.location.href,"quality":"best"}));xhr.onload=function() { if(xhr.status==200){notify("Sent to metube!")}else {notify("Send to metube failed. Check the javascript console for clues.")}}})();
```

## ⚡ Raycast extension

[dotvhs](https://github.com/dotvhs) has created an [extension for Raycast](https://www.raycast.com/dot/metube) that allows adding videos to MeTube directly from Raycast.

## 🔒 HTTPS support, and running behind a reverse proxy

It's possible to configure MeTube to listen in HTTPS mode. `docker-compose` example:

```yaml
services:
  metube:
    image: ghcr.io/alexta69/metube
    container_name: metube
    restart: unless-stopped
    ports:
      - "8081:8081"
    volumes:
      - /path/to/downloads:/downloads
      - /path/to/ssl/crt:/ssl/crt.pem
      - /path/to/ssl/key:/ssl/key.pem
    environment:
      - HTTPS=true
      - CERTFILE=/ssl/crt.pem
      - KEYFILE=/ssl/key.pem
```

It's also possible to run MeTube behind a reverse proxy, in order to support authentication. HTTPS support can also be added in this way.

When running behind a reverse proxy which remaps the URL (i.e. serves MeTube under a subdirectory and not under root), don't forget to set the URL_PREFIX environment variable to the correct value.

If you're using the [linuxserver/swag](https://docs.linuxserver.io/general/swag) image for your reverse proxying needs (which I can heartily recommend), it already includes ready snippets for proxying MeTube both in [subfolder](https://github.com/linuxserver/reverse-proxy-confs/blob/master/metube.subfolder.conf.sample) and [subdomain](https://github.com/linuxserver/reverse-proxy-confs/blob/master/metube.subdomain.conf.sample) modes under the `nginx/proxy-confs` directory in the configuration volume. It also includes Authelia which can be used for authentication.

### 🌐 NGINX

```nginx
location /metube/ {
        proxy_pass http://metube:8081;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
}
```

Note: the extra `proxy_set_header` directives are there to make WebSocket work.

### 🌐 Apache

Contributed by [PIE-yt](https://github.com/PIE-yt). Source [here](https://gist.github.com/PIE-yt/29e7116588379032427f5bd446b2cac4).

```apache
# For putting in your Apache sites site.conf
# Serves MeTube under a /metube/ subdir (http://yourdomain.com/metube/)
<Location /metube/>
    ProxyPass http://localhost:8081/ retry=0 timeout=30
    ProxyPassReverse http://localhost:8081/
</Location>

<Location /metube/socket.io>
    RewriteEngine On
    RewriteCond %{QUERY_STRING} transport=websocket    [NC]
    RewriteRule /(.*) ws://localhost:8081/socket.io/$1 [P,L]
    ProxyPass http://localhost:8081/socket.io retry=0 timeout=30
    ProxyPassReverse http://localhost:8081/socket.io
</Location>
```

### 🌐 Caddy

The following example Caddyfile gets a reverse proxy going behind [caddy](https://caddyserver.com).

```caddyfile
example.com {
  route /metube/* {
    uri strip_prefix metube
    reverse_proxy metube:8081
  }
}
```

## 🔄 Updating yt-dlp

The engine which powers the actual video downloads in MeTube is [yt-dlp](https://github.com/yt-dlp/yt-dlp). Since video sites regularly change their layouts, frequent updates of yt-dlp are required to keep up.

There's an automatic nightly build of MeTube which looks for a new version of yt-dlp, and if one exists, the build pulls it and publishes an updated docker image. Therefore, in order to keep up with the changes, it's recommended that you update your MeTube container regularly with the latest image.

I recommend installing and setting up [watchtower](https://github.com/nicholas-fedor/watchtower) for this purpose.

## 🔧 Troubleshooting and submitting issues

Before asking a question or submitting an issue for MeTube, please remember that MeTube is only a UI for [yt-dlp](https://github.com/yt-dlp/yt-dlp). Any issues you might be experiencing with authentication to video websites, postprocessing, permissions, other `YTDL_OPTIONS` configurations which seem not to work, or anything else that concerns the workings of the underlying yt-dlp library, need not be opened on the MeTube project. In order to debug and troubleshoot them, it's advised to try using the yt-dlp binary directly first, bypassing the UI, and once that is working, importing the options that worked for you into `YTDL_OPTIONS`.

In order to test with the yt-dlp command directly, you can either download it and run it locally, or for a better simulation of its actual conditions, you can run it within the MeTube container itself. Assuming your MeTube container is called `metube`, run the following on your Docker host to get a shell inside the container:

```bash
docker exec -ti metube sh
cd /downloads
```

Once there, you can use the yt-dlp command freely.

## 💡 Submitting feature requests

MeTube development relies on code contributions by the community. The program as it currently stands fits my own use cases, and is therefore feature-complete as far as I'm concerned. If your use cases are different and require additional features, please feel free to submit PRs that implement those features. It's advisable to create an issue first to discuss the planned implementation, because in an effort to reduce bloat, some PRs may not be accepted. However, note that opening a feature request when you don't intend to implement the feature will rarely result in the request being fulfilled.

## 🛠️ Building and running locally

Make sure you have Node.js 22+ and Python 3.13 installed.

```bash
# install Angular and build the UI
cd ui
curl -fsSL https://get.pnpm.io/install.sh | sh -
pnpm install
pnpm run build
# install python dependencies
cd ..
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
# run
uv run python3 app/main.py
```

A Docker image can be built locally (it will build the UI too):

```bash
docker build -t metube .
```

Note that if you're running the server in VSCode, your downloads will go to your user's Downloads folder (this is configured via the environment in `.vscode/launch.json`).
```

## File: `uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.13"

[[package]]
name = "aiohappyeyeballs"
version = "2.6.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/26/30/f84a107a9c4331c14b2b586036f40965c128aa4fee4dda5d3d51cb14ad54/aiohappyeyeballs-2.6.1.tar.gz", hash = "sha256:c3f9d0113123803ccadfdf3f0faa505bc78e6a72d1cc4806cbd719826e943558", size = 22760, upload-time = "2025-03-12T01:42:48.764Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0f/15/5bf3b99495fb160b63f95972b81750f18f7f4e02ad051373b669d17d44f2/aiohappyeyeballs-2.6.1-py3-none-any.whl", hash = "sha256:f349ba8f4b75cb25c99c5c2d84e997e485204d2902a9597802b0371f09331fb8", size = 15265, upload-time = "2025-03-12T01:42:47.083Z" },
]

[[package]]
name = "aiohttp"
version = "3.13.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "aiohappyeyeballs" },
    { name = "aiosignal" },
    { name = "attrs" },
    { name = "frozenlist" },
    { name = "multidict" },
    { name = "propcache" },
    { name = "yarl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/50/42/32cf8e7704ceb4481406eb87161349abb46a57fee3f008ba9cb610968646/aiohttp-3.13.3.tar.gz", hash = "sha256:a949eee43d3782f2daae4f4a2819b2cb9b0c5d3b7f7a927067cc84dafdbb9f88", size = 7844556, upload-time = "2026-01-03T17:33:05.204Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/97/8a/12ca489246ca1faaf5432844adbfce7ff2cc4997733e0af120869345643a/aiohttp-3.13.3-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:5dff64413671b0d3e7d5918ea490bdccb97a4ad29b3f311ed423200b2203e01c", size = 734190, upload-time = "2026-01-03T17:30:45.832Z" },
    { url = "https://files.pythonhosted.org/packages/32/08/de43984c74ed1fca5c014808963cc83cb00d7bb06af228f132d33862ca76/aiohttp-3.13.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:87b9aab6d6ed88235aa2970294f496ff1a1f9adcd724d800e9b952395a80ffd9", size = 491783, upload-time = "2026-01-03T17:30:47.466Z" },
    { url = "https://files.pythonhosted.org/packages/17/f8/8dd2cf6112a5a76f81f81a5130c57ca829d101ad583ce57f889179accdda/aiohttp-3.13.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:425c126c0dc43861e22cb1c14ba4c8e45d09516d0a3ae0a3f7494b79f5f233a3", size = 490704, upload-time = "2026-01-03T17:30:49.373Z" },
    { url = "https://files.pythonhosted.org/packages/6d/40/a46b03ca03936f832bc7eaa47cfbb1ad012ba1be4790122ee4f4f8cba074/aiohttp-3.13.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7f9120f7093c2a32d9647abcaf21e6ad275b4fbec5b55969f978b1a97c7c86bf", size = 1720652, upload-time = "2026-01-03T17:30:50.974Z" },
    { url = "https://files.pythonhosted.org/packages/f7/7e/917fe18e3607af92657e4285498f500dca797ff8c918bd7d90b05abf6c2a/aiohttp-3.13.3-cp313-cp313-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:697753042d57f4bf7122cab985bf15d0cef23c770864580f5af4f52023a56bd6", size = 1692014, upload-time = "2026-01-03T17:30:52.729Z" },
    { url = "https://files.pythonhosted.org/packages/71/b6/cefa4cbc00d315d68973b671cf105b21a609c12b82d52e5d0c9ae61d2a09/aiohttp-3.13.3-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:6de499a1a44e7de70735d0b39f67c8f25eb3d91eb3103be99ca0fa882cdd987d", size = 1759777, upload-time = "2026-01-03T17:30:54.537Z" },
    { url = "https://files.pythonhosted.org/packages/fb/e3/e06ee07b45e59e6d81498b591fc589629be1553abb2a82ce33efe2a7b068/aiohttp-3.13.3-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:37239e9f9a7ea9ac5bf6b92b0260b01f8a22281996da609206a84df860bc1261", size = 1861276, upload-time = "2026-01-03T17:30:56.512Z" },
    { url = "https://files.pythonhosted.org/packages/7c/24/75d274228acf35ceeb2850b8ce04de9dd7355ff7a0b49d607ee60c29c518/aiohttp-3.13.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f76c1e3fe7d7c8afad7ed193f89a292e1999608170dcc9751a7462a87dfd5bc0", size = 1743131, upload-time = "2026-01-03T17:30:58.256Z" },
    { url = "https://files.pythonhosted.org/packages/04/98/3d21dde21889b17ca2eea54fdcff21b27b93f45b7bb94ca029c31ab59dc3/aiohttp-3.13.3-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:fc290605db2a917f6e81b0e1e0796469871f5af381ce15c604a3c5c7e51cb730", size = 1556863, upload-time = "2026-01-03T17:31:00.445Z" },
    { url = "https://files.pythonhosted.org/packages/9e/84/da0c3ab1192eaf64782b03971ab4055b475d0db07b17eff925e8c93b3aa5/aiohttp-3.13.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:4021b51936308aeea0367b8f006dc999ca02bc118a0cc78c303f50a2ff6afb91", size = 1682793, upload-time = "2026-01-03T17:31:03.024Z" },
    { url = "https://files.pythonhosted.org/packages/ff/0f/5802ada182f575afa02cbd0ec5180d7e13a402afb7c2c03a9aa5e5d49060/aiohttp-3.13.3-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:49a03727c1bba9a97d3e93c9f93ca03a57300f484b6e935463099841261195d3", size = 1716676, upload-time = "2026-01-03T17:31:04.842Z" },
    { url = "https://files.pythonhosted.org/packages/3f/8c/714d53bd8b5a4560667f7bbbb06b20c2382f9c7847d198370ec6526af39c/aiohttp-3.13.3-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:3d9908a48eb7416dc1f4524e69f1d32e5d90e3981e4e37eb0aa1cd18f9cfa2a4", size = 1733217, upload-time = "2026-01-03T17:31:06.868Z" },
    { url = "https://files.pythonhosted.org/packages/7d/79/e2176f46d2e963facea939f5be2d26368ce543622be6f00a12844d3c991f/aiohttp-3.13.3-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:2712039939ec963c237286113c68dbad80a82a4281543f3abf766d9d73228998", size = 1552303, upload-time = "2026-01-03T17:31:08.958Z" },
    { url = "https://files.pythonhosted.org/packages/ab/6a/28ed4dea1759916090587d1fe57087b03e6c784a642b85ef48217b0277ae/aiohttp-3.13.3-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:7bfdc049127717581866fa4708791220970ce291c23e28ccf3922c700740fdc0", size = 1763673, upload-time = "2026-01-03T17:31:10.676Z" },
    { url = "https://files.pythonhosted.org/packages/e8/35/4a3daeb8b9fab49240d21c04d50732313295e4bd813a465d840236dd0ce1/aiohttp-3.13.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:8057c98e0c8472d8846b9c79f56766bcc57e3e8ac7bfd510482332366c56c591", size = 1721120, upload-time = "2026-01-03T17:31:12.575Z" },
    { url = "https://files.pythonhosted.org/packages/bc/9f/d643bb3c5fb99547323e635e251c609fbbc660d983144cfebec529e09264/aiohttp-3.13.3-cp313-cp313-win32.whl", hash = "sha256:1449ceddcdbcf2e0446957863af03ebaaa03f94c090f945411b61269e2cb5daf", size = 427383, upload-time = "2026-01-03T17:31:14.382Z" },
    { url = "https://files.pythonhosted.org/packages/4e/f1/ab0395f8a79933577cdd996dd2f9aa6014af9535f65dddcf88204682fe62/aiohttp-3.13.3-cp313-cp313-win_amd64.whl", hash = "sha256:693781c45a4033d31d4187d2436f5ac701e7bbfe5df40d917736108c1cc7436e", size = 453899, upload-time = "2026-01-03T17:31:15.958Z" },
    { url = "https://files.pythonhosted.org/packages/99/36/5b6514a9f5d66f4e2597e40dea2e3db271e023eb7a5d22defe96ba560996/aiohttp-3.13.3-cp314-cp314-macosx_10_13_universal2.whl", hash = "sha256:ea37047c6b367fd4bd632bff8077449b8fa034b69e812a18e0132a00fae6e808", size = 737238, upload-time = "2026-01-03T17:31:17.909Z" },
    { url = "https://files.pythonhosted.org/packages/f7/49/459327f0d5bcd8c6c9ca69e60fdeebc3622861e696490d8674a6d0cb90a6/aiohttp-3.13.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:6fc0e2337d1a4c3e6acafda6a78a39d4c14caea625124817420abceed36e2415", size = 492292, upload-time = "2026-01-03T17:31:19.919Z" },
    { url = "https://files.pythonhosted.org/packages/e8/0b/b97660c5fd05d3495b4eb27f2d0ef18dc1dc4eff7511a9bf371397ff0264/aiohttp-3.13.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c685f2d80bb67ca8c3837823ad76196b3694b0159d232206d1e461d3d434666f", size = 493021, upload-time = "2026-01-03T17:31:21.636Z" },
    { url = "https://files.pythonhosted.org/packages/54/d4/438efabdf74e30aeceb890c3290bbaa449780583b1270b00661126b8aae4/aiohttp-3.13.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:48e377758516d262bde50c2584fc6c578af272559c409eecbdd2bae1601184d6", size = 1717263, upload-time = "2026-01-03T17:31:23.296Z" },
    { url = "https://files.pythonhosted.org/packages/71/f2/7bddc7fd612367d1459c5bcf598a9e8f7092d6580d98de0e057eb42697ad/aiohttp-3.13.3-cp314-cp314-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:34749271508078b261c4abb1767d42b8d0c0cc9449c73a4df494777dc55f0687", size = 1669107, upload-time = "2026-01-03T17:31:25.334Z" },
    { url = "https://files.pythonhosted.org/packages/00/5a/1aeaecca40e22560f97610a329e0e5efef5e0b5afdf9f857f0d93839ab2e/aiohttp-3.13.3-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:82611aeec80eb144416956ec85b6ca45a64d76429c1ed46ae1b5f86c6e0c9a26", size = 1760196, upload-time = "2026-01-03T17:31:27.394Z" },
    { url = "https://files.pythonhosted.org/packages/f8/f8/0ff6992bea7bd560fc510ea1c815f87eedd745fe035589c71ce05612a19a/aiohttp-3.13.3-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:2fff83cfc93f18f215896e3a190e8e5cb413ce01553901aca925176e7568963a", size = 1843591, upload-time = "2026-01-03T17:31:29.238Z" },
    { url = "https://files.pythonhosted.org/packages/e3/d1/e30e537a15f53485b61f5be525f2157da719819e8377298502aebac45536/aiohttp-3.13.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:bbe7d4cecacb439e2e2a8a1a7b935c25b812af7a5fd26503a66dadf428e79ec1", size = 1720277, upload-time = "2026-01-03T17:31:31.053Z" },
    { url = "https://files.pythonhosted.org/packages/84/45/23f4c451d8192f553d38d838831ebbc156907ea6e05557f39563101b7717/aiohttp-3.13.3-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:b928f30fe49574253644b1ca44b1b8adbd903aa0da4b9054a6c20fc7f4092a25", size = 1548575, upload-time = "2026-01-03T17:31:32.87Z" },
    { url = "https://files.pythonhosted.org/packages/6a/ed/0a42b127a43712eda7807e7892c083eadfaf8429ca8fb619662a530a3aab/aiohttp-3.13.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7b5e8fe4de30df199155baaf64f2fcd604f4c678ed20910db8e2c66dc4b11603", size = 1679455, upload-time = "2026-01-03T17:31:34.76Z" },
    { url = "https://files.pythonhosted.org/packages/2e/b5/c05f0c2b4b4fe2c9d55e73b6d3ed4fd6c9dc2684b1d81cbdf77e7fad9adb/aiohttp-3.13.3-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:8542f41a62bcc58fc7f11cf7c90e0ec324ce44950003feb70640fc2a9092c32a", size = 1687417, upload-time = "2026-01-03T17:31:36.699Z" },
    { url = "https://files.pythonhosted.org/packages/c9/6b/915bc5dad66aef602b9e459b5a973529304d4e89ca86999d9d75d80cbd0b/aiohttp-3.13.3-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:5e1d8c8b8f1d91cd08d8f4a3c2b067bfca6ec043d3ff36de0f3a715feeedf926", size = 1729968, upload-time = "2026-01-03T17:31:38.622Z" },
    { url = "https://files.pythonhosted.org/packages/11/3b/e84581290a9520024a08640b63d07673057aec5ca548177a82026187ba73/aiohttp-3.13.3-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:90455115e5da1c3c51ab619ac57f877da8fd6d73c05aacd125c5ae9819582aba", size = 1545690, upload-time = "2026-01-03T17:31:40.57Z" },
    { url = "https://files.pythonhosted.org/packages/f5/04/0c3655a566c43fd647c81b895dfe361b9f9ad6d58c19309d45cff52d6c3b/aiohttp-3.13.3-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:042e9e0bcb5fba81886c8b4fbb9a09d6b8a00245fd8d88e4d989c1f96c74164c", size = 1746390, upload-time = "2026-01-03T17:31:42.857Z" },
    { url = "https://files.pythonhosted.org/packages/1f/53/71165b26978f719c3419381514c9690bd5980e764a09440a10bb816ea4ab/aiohttp-3.13.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:2eb752b102b12a76ca02dff751a801f028b4ffbbc478840b473597fc91a9ed43", size = 1702188, upload-time = "2026-01-03T17:31:44.984Z" },
    { url = "https://files.pythonhosted.org/packages/29/a7/cbe6c9e8e136314fa1980da388a59d2f35f35395948a08b6747baebb6aa6/aiohttp-3.13.3-cp314-cp314-win32.whl", hash = "sha256:b556c85915d8efaed322bf1bdae9486aa0f3f764195a0fb6ee962e5c71ef5ce1", size = 433126, upload-time = "2026-01-03T17:31:47.463Z" },
    { url = "https://files.pythonhosted.org/packages/de/56/982704adea7d3b16614fc5936014e9af85c0e34b58f9046655817f04306e/aiohttp-3.13.3-cp314-cp314-win_amd64.whl", hash = "sha256:9bf9f7a65e7aa20dd764151fb3d616c81088f91f8df39c3893a536e279b4b984", size = 459128, upload-time = "2026-01-03T17:31:49.2Z" },
    { url = "https://files.pythonhosted.org/packages/6c/2a/3c79b638a9c3d4658d345339d22070241ea341ed4e07b5ac60fb0f418003/aiohttp-3.13.3-cp314-cp314t-macosx_10_13_universal2.whl", hash = "sha256:05861afbbec40650d8a07ea324367cb93e9e8cc7762e04dd4405df99fa65159c", size = 769512, upload-time = "2026-01-03T17:31:51.134Z" },
    { url = "https://files.pythonhosted.org/packages/29/b9/3e5014d46c0ab0db8707e0ac2711ed28c4da0218c358a4e7c17bae0d8722/aiohttp-3.13.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:2fc82186fadc4a8316768d61f3722c230e2c1dcab4200d52d2ebdf2482e47592", size = 506444, upload-time = "2026-01-03T17:31:52.85Z" },
    { url = "https://files.pythonhosted.org/packages/90/03/c1d4ef9a054e151cd7839cdc497f2638f00b93cbe8043983986630d7a80c/aiohttp-3.13.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:0add0900ff220d1d5c5ebbf99ed88b0c1bbf87aa7e4262300ed1376a6b13414f", size = 510798, upload-time = "2026-01-03T17:31:54.91Z" },
    { url = "https://files.pythonhosted.org/packages/ea/76/8c1e5abbfe8e127c893fe7ead569148a4d5a799f7cf958d8c09f3eedf097/aiohttp-3.13.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:568f416a4072fbfae453dcf9a99194bbb8bdeab718e08ee13dfa2ba0e4bebf29", size = 1868835, upload-time = "2026-01-03T17:31:56.733Z" },
    { url = "https://files.pythonhosted.org/packages/8e/ac/984c5a6f74c363b01ff97adc96a3976d9c98940b8969a1881575b279ac5d/aiohttp-3.13.3-cp314-cp314t-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:add1da70de90a2569c5e15249ff76a631ccacfe198375eead4aadf3b8dc849dc", size = 1720486, upload-time = "2026-01-03T17:31:58.65Z" },
    { url = "https://files.pythonhosted.org/packages/b2/9a/b7039c5f099c4eb632138728828b33428585031a1e658d693d41d07d89d1/aiohttp-3.13.3-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:10b47b7ba335d2e9b1239fa571131a87e2d8ec96b333e68b2a305e7a98b0bae2", size = 1847951, upload-time = "2026-01-03T17:32:00.989Z" },
    { url = "https://files.pythonhosted.org/packages/3c/02/3bec2b9a1ba3c19ff89a43a19324202b8eb187ca1e928d8bdac9bbdddebd/aiohttp-3.13.3-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:3dd4dce1c718e38081c8f35f323209d4c1df7d4db4bab1b5c88a6b4d12b74587", size = 1941001, upload-time = "2026-01-03T17:32:03.122Z" },
    { url = "https://files.pythonhosted.org/packages/37/df/d879401cedeef27ac4717f6426c8c36c3091c6e9f08a9178cc87549c537f/aiohttp-3.13.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:34bac00a67a812570d4a460447e1e9e06fae622946955f939051e7cc895cfab8", size = 1797246, upload-time = "2026-01-03T17:32:05.255Z" },
    { url = "https://files.pythonhosted.org/packages/8d/15/be122de1f67e6953add23335c8ece6d314ab67c8bebb3f181063010795a7/aiohttp-3.13.3-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:a19884d2ee70b06d9204b2727a7b9f983d0c684c650254679e716b0b77920632", size = 1627131, upload-time = "2026-01-03T17:32:07.607Z" },
    { url = "https://files.pythonhosted.org/packages/12/12/70eedcac9134cfa3219ab7af31ea56bc877395b1ac30d65b1bc4b27d0438/aiohttp-3.13.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:5f8ca7f2bb6ba8348a3614c7918cc4bb73268c5ac2a207576b7afea19d3d9f64", size = 1795196, upload-time = "2026-01-03T17:32:09.59Z" },
    { url = "https://files.pythonhosted.org/packages/32/11/b30e1b1cd1f3054af86ebe60df96989c6a414dd87e27ad16950eee420bea/aiohttp-3.13.3-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:b0d95340658b9d2f11d9697f59b3814a9d3bb4b7a7c20b131df4bcef464037c0", size = 1782841, upload-time = "2026-01-03T17:32:11.445Z" },
    { url = "https://files.pythonhosted.org/packages/88/0d/d98a9367b38912384a17e287850f5695c528cff0f14f791ce8ee2e4f7796/aiohttp-3.13.3-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:a1e53262fd202e4b40b70c3aff944a8155059beedc8a89bba9dc1f9ef06a1b56", size = 1795193, upload-time = "2026-01-03T17:32:13.705Z" },
    { url = "https://files.pythonhosted.org/packages/43/a5/a2dfd1f5ff5581632c7f6a30e1744deda03808974f94f6534241ef60c751/aiohttp-3.13.3-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:d60ac9663f44168038586cab2157e122e46bdef09e9368b37f2d82d354c23f72", size = 1621979, upload-time = "2026-01-03T17:32:15.965Z" },
    { url = "https://files.pythonhosted.org/packages/fa/f0/12973c382ae7c1cccbc4417e129c5bf54c374dfb85af70893646e1f0e749/aiohttp-3.13.3-cp314-cp314t-musllinux_1_2_s390x.whl", hash = "sha256:90751b8eed69435bac9ff4e3d2f6b3af1f57e37ecb0fbeee59c0174c9e2d41df", size = 1822193, upload-time = "2026-01-03T17:32:18.219Z" },
    { url = "https://files.pythonhosted.org/packages/3c/5f/24155e30ba7f8c96918af1350eb0663e2430aad9e001c0489d89cd708ab1/aiohttp-3.13.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:fc353029f176fd2b3ec6cfc71be166aba1936fe5d73dd1992ce289ca6647a9aa", size = 1769801, upload-time = "2026-01-03T17:32:20.25Z" },
    { url = "https://files.pythonhosted.org/packages/eb/f8/7314031ff5c10e6ece114da79b338ec17eeff3a079e53151f7e9f43c4723/aiohttp-3.13.3-cp314-cp314t-win32.whl", hash = "sha256:2e41b18a58da1e474a057b3d35248d8320029f61d70a37629535b16a0c8f3767", size = 466523, upload-time = "2026-01-03T17:32:22.215Z" },
    { url = "https://files.pythonhosted.org/packages/b4/63/278a98c715ae467624eafe375542d8ba9b4383a016df8fdefe0ae28382a7/aiohttp-3.13.3-cp314-cp314t-win_amd64.whl", hash = "sha256:44531a36aa2264a1860089ffd4dce7baf875ee5a6079d5fb42e261c704ef7344", size = 499694, upload-time = "2026-01-03T17:32:24.546Z" },
]

[[package]]
name = "aiosignal"
version = "1.4.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "frozenlist" },
]
sdist = { url = "https://files.pythonhosted.org/packages/61/62/06741b579156360248d1ec624842ad0edf697050bbaf7c3e46394e106ad1/aiosignal-1.4.0.tar.gz", hash = "sha256:f47eecd9468083c2029cc99945502cb7708b082c232f9aca65da147157b251c7", size = 25007, upload-time = "2025-07-03T22:54:43.528Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fb/76/641ae371508676492379f16e2fa48f4e2c11741bd63c48be4b12a6b09cba/aiosignal-1.4.0-py3-none-any.whl", hash = "sha256:053243f8b92b990551949e63930a839ff0cf0b0ebbe0597b0f3fb19e1a0fe82e", size = 7490, upload-time = "2025-07-03T22:54:42.156Z" },
]

[[package]]
name = "anyio"
version = "4.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/f0/5eb65b2bb0d09ac6776f2eb54adee6abe8228ea05b20a5ad0e4945de8aac/anyio-4.12.1.tar.gz", hash = "sha256:41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703", size = 228685, upload-time = "2026-01-06T11:45:21.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/0e/27be9fdef66e72d64c0cdc3cc2823101b80585f8119b5c112c2e8f5f7dab/anyio-4.12.1-py3-none-any.whl", hash = "sha256:d405828884fc140aa80a3c667b8beed277f1dfedec42ba031bd6ac3db606ab6c", size = 113592, upload-time = "2026-01-06T11:45:19.497Z" },
]

[[package]]
name = "astroid"
version = "4.0.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/07/63/0adf26577da5eff6eb7a177876c1cfa213856be9926a000f65c4add9692b/astroid-4.0.4.tar.gz", hash = "sha256:986fed8bcf79fb82c78b18a53352a0b287a73817d6dbcfba3162da36667c49a0", size = 406358, upload-time = "2026-02-07T23:35:07.509Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b0/cf/1c5f42b110e57bc5502eb80dbc3b03d256926062519224835ef08134f1f9/astroid-4.0.4-py3-none-any.whl", hash = "sha256:52f39653876c7dec3e3afd4c2696920e05c83832b9737afc21928f2d2eb7a753", size = 276445, upload-time = "2026-02-07T23:35:05.344Z" },
]

[[package]]
name = "attrs"
version = "25.4.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6b/5c/685e6633917e101e5dcb62b9dd76946cbb57c26e133bae9e0cd36033c0a9/attrs-25.4.0.tar.gz", hash = "sha256:16d5969b87f0859ef33a48b35d55ac1be6e42ae49d5e853b597db70c35c57e11", size = 934251, upload-time = "2025-10-06T13:54:44.725Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3a/2a/7cc015f5b9f5db42b7d48157e23356022889fc354a2813c15934b7cb5c0e/attrs-25.4.0-py3-none-any.whl", hash = "sha256:adcf7e2a1fb3b36ac48d97835bb6d8ade15b8dcce26aba8bf1d14847b57a3373", size = 67615, upload-time = "2025-10-06T13:54:43.17Z" },
]

[[package]]
name = "bidict"
version = "0.23.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/9a/6e/026678aa5a830e07cd9498a05d3e7e650a4f56a42f267a53d22bcda1bdc9/bidict-0.23.1.tar.gz", hash = "sha256:03069d763bc387bbd20e7d49914e75fc4132a41937fa3405417e1a5a2d006d71", size = 29093, upload-time = "2024-02-18T19:09:05.748Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/99/37/e8730c3587a65eb5645d4aba2d27aae48e8003614d6aaf15dda67f702f1f/bidict-0.23.1-py3-none-any.whl", hash = "sha256:5dae8d4d79b552a71cbabc7deb25dfe8ce710b17ff41711e13010ead2abfc3e5", size = 32764, upload-time = "2024-02-18T19:09:04.156Z" },
]

[[package]]
name = "brotli"
version = "1.2.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f7/16/c92ca344d646e71a43b8bb353f0a6490d7f6e06210f8554c8f874e454285/brotli-1.2.0.tar.gz", hash = "sha256:e310f77e41941c13340a95976fe66a8a95b01e783d430eeaf7a2f87e0a57dd0a", size = 7388632, upload-time = "2025-11-05T18:39:42.86Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6c/d4/4ad5432ac98c73096159d9ce7ffeb82d151c2ac84adcc6168e476bb54674/brotli-1.2.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:9e5825ba2c9998375530504578fd4d5d1059d09621a02065d1b6bfc41a8e05ab", size = 861523, upload-time = "2025-11-05T18:38:34.67Z" },
    { url = "https://files.pythonhosted.org/packages/91/9f/9cc5bd03ee68a85dc4bc89114f7067c056a3c14b3d95f171918c088bf88d/brotli-1.2.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:0cf8c3b8ba93d496b2fae778039e2f5ecc7cff99df84df337ca31d8f2252896c", size = 444289, upload-time = "2025-11-05T18:38:35.6Z" },
    { url = "https://files.pythonhosted.org/packages/2e/b6/fe84227c56a865d16a6614e2c4722864b380cb14b13f3e6bef441e73a85a/brotli-1.2.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c8565e3cdc1808b1a34714b553b262c5de5fbda202285782173ec137fd13709f", size = 1528076, upload-time = "2025-11-05T18:38:36.639Z" },
    { url = "https://files.pythonhosted.org/packages/55/de/de4ae0aaca06c790371cf6e7ee93a024f6b4bb0568727da8c3de112e726c/brotli-1.2.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:26e8d3ecb0ee458a9804f47f21b74845cc823fd1bb19f02272be70774f56e2a6", size = 1626880, upload-time = "2025-11-05T18:38:37.623Z" },
    { url = "https://files.pythonhosted.org/packages/5f/16/a1b22cbea436642e071adcaf8d4b350a2ad02f5e0ad0da879a1be16188a0/brotli-1.2.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:67a91c5187e1eec76a61625c77a6c8c785650f5b576ca732bd33ef58b0dff49c", size = 1419737, upload-time = "2025-11-05T18:38:38.729Z" },
    { url = "https://files.pythonhosted.org/packages/46/63/c968a97cbb3bdbf7f974ef5a6ab467a2879b82afbc5ffb65b8acbb744f95/brotli-1.2.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:4ecdb3b6dc36e6d6e14d3a1bdc6c1057c8cbf80db04031d566eb6080ce283a48", size = 1484440, upload-time = "2025-11-05T18:38:39.916Z" },
    { url = "https://files.pythonhosted.org/packages/06/9d/102c67ea5c9fc171f423e8399e585dabea29b5bc79b05572891e70013cdd/brotli-1.2.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:3e1b35d56856f3ed326b140d3c6d9db91740f22e14b06e840fe4bb1923439a18", size = 1593313, upload-time = "2025-11-05T18:38:41.24Z" },
    { url = "https://files.pythonhosted.org/packages/9e/4a/9526d14fa6b87bc827ba1755a8440e214ff90de03095cacd78a64abe2b7d/brotli-1.2.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:54a50a9dad16b32136b2241ddea9e4df159b41247b2ce6aac0b3276a66a8f1e5", size = 1487945, upload-time = "2025-11-05T18:38:42.277Z" },
    { url = "https://files.pythonhosted.org/packages/5b/e8/3fe1ffed70cbef83c5236166acaed7bb9c766509b157854c80e2f766b38c/brotli-1.2.0-cp313-cp313-win32.whl", hash = "sha256:1b1d6a4efedd53671c793be6dd760fcf2107da3a52331ad9ea429edf0902f27a", size = 334368, upload-time = "2025-11-05T18:38:43.345Z" },
    { url = "https://files.pythonhosted.org/packages/ff/91/e739587be970a113b37b821eae8097aac5a48e5f0eca438c22e4c7dd8648/brotli-1.2.0-cp313-cp313-win_amd64.whl", hash = "sha256:b63daa43d82f0cdabf98dee215b375b4058cce72871fd07934f179885aad16e8", size = 369116, upload-time = "2025-11-05T18:38:44.609Z" },
    { url = "https://files.pythonhosted.org/packages/17/e1/298c2ddf786bb7347a1cd71d63a347a79e5712a7c0cba9e3c3458ebd976f/brotli-1.2.0-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:6c12dad5cd04530323e723787ff762bac749a7b256a5bece32b2243dd5c27b21", size = 863080, upload-time = "2025-11-05T18:38:45.503Z" },
    { url = "https://files.pythonhosted.org/packages/84/0c/aac98e286ba66868b2b3b50338ffbd85a35c7122e9531a73a37a29763d38/brotli-1.2.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:3219bd9e69868e57183316ee19c84e03e8f8b5a1d1f2667e1aa8c2f91cb061ac", size = 445453, upload-time = "2025-11-05T18:38:46.433Z" },
    { url = "https://files.pythonhosted.org/packages/ec/f1/0ca1f3f99ae300372635ab3fe2f7a79fa335fee3d874fa7f9e68575e0e62/brotli-1.2.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:963a08f3bebd8b75ac57661045402da15991468a621f014be54e50f53a58d19e", size = 1528168, upload-time = "2025-11-05T18:38:47.371Z" },
    { url = "https://files.pythonhosted.org/packages/d6/a6/2ebfc8f766d46df8d3e65b880a2e220732395e6d7dc312c1e1244b0f074a/brotli-1.2.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:9322b9f8656782414b37e6af884146869d46ab85158201d82bab9abbcb971dc7", size = 1627098, upload-time = "2025-11-05T18:38:48.385Z" },
    { url = "https://files.pythonhosted.org/packages/f3/2f/0976d5b097ff8a22163b10617f76b2557f15f0f39d6a0fe1f02b1a53e92b/brotli-1.2.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:cf9cba6f5b78a2071ec6fb1e7bd39acf35071d90a81231d67e92d637776a6a63", size = 1419861, upload-time = "2025-11-05T18:38:49.372Z" },
    { url = "https://files.pythonhosted.org/packages/9c/97/d76df7176a2ce7616ff94c1fb72d307c9a30d2189fe877f3dd99af00ea5a/brotli-1.2.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7547369c4392b47d30a3467fe8c3330b4f2e0f7730e45e3103d7d636678a808b", size = 1484594, upload-time = "2025-11-05T18:38:50.655Z" },
    { url = "https://files.pythonhosted.org/packages/d3/93/14cf0b1216f43df5609f5b272050b0abd219e0b54ea80b47cef9867b45e7/brotli-1.2.0-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:fc1530af5c3c275b8524f2e24841cbe2599d74462455e9bae5109e9ff42e9361", size = 1593455, upload-time = "2025-11-05T18:38:51.624Z" },
    { url = "https://files.pythonhosted.org/packages/b3/73/3183c9e41ca755713bdf2cc1d0810df742c09484e2e1ddd693bee53877c1/brotli-1.2.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:d2d085ded05278d1c7f65560aae97b3160aeb2ea2c0b3e26204856beccb60888", size = 1488164, upload-time = "2025-11-05T18:38:53.079Z" },
    { url = "https://files.pythonhosted.org/packages/64/6a/0c78d8f3a582859236482fd9fa86a65a60328a00983006bcf6d83b7b2253/brotli-1.2.0-cp314-cp314-win32.whl", hash = "sha256:832c115a020e463c2f67664560449a7bea26b0c1fdd690352addad6d0a08714d", size = 339280, upload-time = "2025-11-05T18:38:54.02Z" },
    { url = "https://files.pythonhosted.org/packages/f5/10/56978295c14794b2c12007b07f3e41ba26acda9257457d7085b0bb3bb90c/brotli-1.2.0-cp314-cp314-win_amd64.whl", hash = "sha256:e7c0af964e0b4e3412a0ebf341ea26ec767fa0b4cf81abb5e897c9338b5ad6a3", size = 375639, upload-time = "2025-11-05T18:38:55.67Z" },
]

[[package]]
name = "brotlicffi"
version = "1.2.0.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "cffi" },
]
sdist = { url = "https://files.pythonhosted.org/packages/8a/b6/017dc5f852ed9b8735af77774509271acbf1de02d238377667145fcee01d/brotlicffi-1.2.0.1.tar.gz", hash = "sha256:c20d5c596278307ad06414a6d95a892377ea274a5c6b790c2548c009385d621c", size = 478156, upload-time = "2026-03-05T19:54:11.547Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ef/f9/dfa56316837fa798eac19358351e974de8e1e2ca9475af4cb90293cd6576/brotlicffi-1.2.0.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:2c85e65913cf2b79c57a3fdd05b98d9731d9255dc0cb696b09376cc091b9cddd", size = 433046, upload-time = "2026-03-05T19:53:46.209Z" },
    { url = "https://files.pythonhosted.org/packages/4a/f5/f8f492158c76b0d940388801f04f747028971ad5774287bded5f1e53f08d/brotlicffi-1.2.0.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:535f2d05d0273408abc13fc0eebb467afac17b0ad85090c8913690d40207dac5", size = 1541126, upload-time = "2026-03-05T19:53:48.248Z" },
    { url = "https://files.pythonhosted.org/packages/3b/e1/ff87af10ac419600c63e9287a0649c673673ae6b4f2bcf48e96cb2f89f60/brotlicffi-1.2.0.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ce17eb798ca59ecec67a9bb3fd7a4304e120d1cd02953ce522d959b9a84d58ac", size = 1541983, upload-time = "2026-03-05T19:53:50.317Z" },
    { url = "https://files.pythonhosted.org/packages/47/c0/80ecd9bd45776109fab14040e478bf63e456967c9ddee2353d8330ed8de1/brotlicffi-1.2.0.1-cp314-cp314t-win32.whl", hash = "sha256:3c9544f83cb715d95d7eab3af4adbbef8b2093ad6382288a83b3a25feb1a57ec", size = 349047, upload-time = "2026-03-05T19:53:52.215Z" },
    { url = "https://files.pythonhosted.org/packages/ab/98/13e5b250236a281b6cd9e92a01ee1ae231029fa78faee932ef3766e1cb24/brotlicffi-1.2.0.1-cp314-cp314t-win_amd64.whl", hash = "sha256:625f8115d32ae9c0740d01ea51518437c3fbaa3e78d41cb18459f6f7ac326000", size = 385652, upload-time = "2026-03-05T19:53:53.892Z" },
    { url = "https://files.pythonhosted.org/packages/9a/9f/b98dcd4af47994cee97aebac866996a006a2e5fc1fd1e2b82a8ad95cf09c/brotlicffi-1.2.0.1-cp38-abi3-macosx_11_0_arm64.whl", hash = "sha256:91ba5f0ccc040f6ff8f7efaf839f797723d03ed46acb8ae9408f99ffd2572cf4", size = 432608, upload-time = "2026-03-05T19:53:56.736Z" },
    { url = "https://files.pythonhosted.org/packages/b1/7a/ac4ee56595a061e3718a6d1ea7e921f4df156894acffb28ed88a1fd52022/brotlicffi-1.2.0.1-cp38-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:be9a670c6811af30a4bd42d7116dc5895d3b41beaa8ed8a89050447a0181f5ce", size = 1534257, upload-time = "2026-03-05T19:53:58.667Z" },
    { url = "https://files.pythonhosted.org/packages/99/39/e7410db7f6f56de57744ea52a115084ceb2735f4d44973f349bb92136586/brotlicffi-1.2.0.1-cp38-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6f3314a3476f59e5443f9f72a6dff16edc0c3463c9b318feaef04ae3e4683f5a", size = 1536838, upload-time = "2026-03-05T19:54:00.705Z" },
    { url = "https://files.pythonhosted.org/packages/a6/75/6e7977d1935fc3fbb201cbd619be8f2c7aea25d40a096967132854b34708/brotlicffi-1.2.0.1-cp38-abi3-win32.whl", hash = "sha256:82ea52e2b5d3145b6c406ebd3efb0d55db718b7ad996bd70c62cec0439de1187", size = 343337, upload-time = "2026-03-05T19:54:02.446Z" },
    { url = "https://files.pythonhosted.org/packages/d8/ef/e7e485ce5e4ba3843a0a92feb767c7b6098fd6e65ce752918074d175ae71/brotlicffi-1.2.0.1-cp38-abi3-win_amd64.whl", hash = "sha256:da2e82a08e7778b8bc539d27ca03cdd684113e81394bfaaad8d0dfc6a17ddede", size = 379026, upload-time = "2026-03-05T19:54:04.322Z" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "cffi"
version = "2.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pycparser", marker = "implementation_name != 'PyPy'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/eb/56/b1ba7935a17738ae8453301356628e8147c79dbb825bcbc73dc7401f9846/cffi-2.0.0.tar.gz", hash = "sha256:44d1b5909021139fe36001ae048dbdde8214afa20200eda0f64c068cac5d5529", size = 523588, upload-time = "2025-09-08T23:24:04.541Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4b/8d/a0a47a0c9e413a658623d014e91e74a50cdd2c423f7ccfd44086ef767f90/cffi-2.0.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:00bdf7acc5f795150faa6957054fbbca2439db2f775ce831222b66f192f03beb", size = 185230, upload-time = "2025-09-08T23:23:00.879Z" },
    { url = "https://files.pythonhosted.org/packages/4a/d2/a6c0296814556c68ee32009d9c2ad4f85f2707cdecfd7727951ec228005d/cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:45d5e886156860dc35862657e1494b9bae8dfa63bf56796f2fb56e1679fc0bca", size = 181043, upload-time = "2025-09-08T23:23:02.231Z" },
    { url = "https://files.pythonhosted.org/packages/b0/1e/d22cc63332bd59b06481ceaac49d6c507598642e2230f201649058a7e704/cffi-2.0.0-cp313-cp313-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:07b271772c100085dd28b74fa0cd81c8fb1a3ba18b21e03d7c27f3436a10606b", size = 212446, upload-time = "2025-09-08T23:23:03.472Z" },
    { url = "https://files.pythonhosted.org/packages/a9/f5/a2c23eb03b61a0b8747f211eb716446c826ad66818ddc7810cc2cc19b3f2/cffi-2.0.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:d48a880098c96020b02d5a1f7d9251308510ce8858940e6fa99ece33f610838b", size = 220101, upload-time = "2025-09-08T23:23:04.792Z" },
    { url = "https://files.pythonhosted.org/packages/f2/7f/e6647792fc5850d634695bc0e6ab4111ae88e89981d35ac269956605feba/cffi-2.0.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:f93fd8e5c8c0a4aa1f424d6173f14a892044054871c771f8566e4008eaa359d2", size = 207948, upload-time = "2025-09-08T23:23:06.127Z" },
    { url = "https://files.pythonhosted.org/packages/cb/1e/a5a1bd6f1fb30f22573f76533de12a00bf274abcdc55c8edab639078abb6/cffi-2.0.0-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:dd4f05f54a52fb558f1ba9f528228066954fee3ebe629fc1660d874d040ae5a3", size = 206422, upload-time = "2025-09-08T23:23:07.753Z" },
    { url = "https://files.pythonhosted.org/packages/98/df/0a1755e750013a2081e863e7cd37e0cdd02664372c754e5560099eb7aa44/cffi-2.0.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:c8d3b5532fc71b7a77c09192b4a5a200ea992702734a2e9279a37f2478236f26", size = 219499, upload-time = "2025-09-08T23:23:09.648Z" },
    { url = "https://files.pythonhosted.org/packages/50/e1/a969e687fcf9ea58e6e2a928ad5e2dd88cc12f6f0ab477e9971f2309b57c/cffi-2.0.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d9b29c1f0ae438d5ee9acb31cadee00a58c46cc9c0b2f9038c6b0b3470877a8c", size = 222928, upload-time = "2025-09-08T23:23:10.928Z" },
    { url = "https://files.pythonhosted.org/packages/36/54/0362578dd2c9e557a28ac77698ed67323ed5b9775ca9d3fe73fe191bb5d8/cffi-2.0.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6d50360be4546678fc1b79ffe7a66265e28667840010348dd69a314145807a1b", size = 221302, upload-time = "2025-09-08T23:23:12.42Z" },
    { url = "https://files.pythonhosted.org/packages/eb/6d/bf9bda840d5f1dfdbf0feca87fbdb64a918a69bca42cfa0ba7b137c48cb8/cffi-2.0.0-cp313-cp313-win32.whl", hash = "sha256:74a03b9698e198d47562765773b4a8309919089150a0bb17d829ad7b44b60d27", size = 172909, upload-time = "2025-09-08T23:23:14.32Z" },
    { url = "https://files.pythonhosted.org/packages/37/18/6519e1ee6f5a1e579e04b9ddb6f1676c17368a7aba48299c3759bbc3c8b3/cffi-2.0.0-cp313-cp313-win_amd64.whl", hash = "sha256:19f705ada2530c1167abacb171925dd886168931e0a7b78f5bffcae5c6b5be75", size = 183402, upload-time = "2025-09-08T23:23:15.535Z" },
    { url = "https://files.pythonhosted.org/packages/cb/0e/02ceeec9a7d6ee63bb596121c2c8e9b3a9e150936f4fbef6ca1943e6137c/cffi-2.0.0-cp313-cp313-win_arm64.whl", hash = "sha256:256f80b80ca3853f90c21b23ee78cd008713787b1b1e93eae9f3d6a7134abd91", size = 177780, upload-time = "2025-09-08T23:23:16.761Z" },
    { url = "https://files.pythonhosted.org/packages/92/c4/3ce07396253a83250ee98564f8d7e9789fab8e58858f35d07a9a2c78de9f/cffi-2.0.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:fc33c5141b55ed366cfaad382df24fe7dcbc686de5be719b207bb248e3053dc5", size = 185320, upload-time = "2025-09-08T23:23:18.087Z" },
    { url = "https://files.pythonhosted.org/packages/59/dd/27e9fa567a23931c838c6b02d0764611c62290062a6d4e8ff7863daf9730/cffi-2.0.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c654de545946e0db659b3400168c9ad31b5d29593291482c43e3564effbcee13", size = 181487, upload-time = "2025-09-08T23:23:19.622Z" },
    { url = "https://files.pythonhosted.org/packages/d6/43/0e822876f87ea8a4ef95442c3d766a06a51fc5298823f884ef87aaad168c/cffi-2.0.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:24b6f81f1983e6df8db3adc38562c83f7d4a0c36162885ec7f7b77c7dcbec97b", size = 220049, upload-time = "2025-09-08T23:23:20.853Z" },
    { url = "https://files.pythonhosted.org/packages/b4/89/76799151d9c2d2d1ead63c2429da9ea9d7aac304603de0c6e8764e6e8e70/cffi-2.0.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:12873ca6cb9b0f0d3a0da705d6086fe911591737a59f28b7936bdfed27c0d47c", size = 207793, upload-time = "2025-09-08T23:23:22.08Z" },
    { url = "https://files.pythonhosted.org/packages/bb/dd/3465b14bb9e24ee24cb88c9e3730f6de63111fffe513492bf8c808a3547e/cffi-2.0.0-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:d9b97165e8aed9272a6bb17c01e3cc5871a594a446ebedc996e2397a1c1ea8ef", size = 206300, upload-time = "2025-09-08T23:23:23.314Z" },
    { url = "https://files.pythonhosted.org/packages/47/d9/d83e293854571c877a92da46fdec39158f8d7e68da75bf73581225d28e90/cffi-2.0.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:afb8db5439b81cf9c9d0c80404b60c3cc9c3add93e114dcae767f1477cb53775", size = 219244, upload-time = "2025-09-08T23:23:24.541Z" },
    { url = "https://files.pythonhosted.org/packages/2b/0f/1f177e3683aead2bb00f7679a16451d302c436b5cbf2505f0ea8146ef59e/cffi-2.0.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:737fe7d37e1a1bffe70bd5754ea763a62a066dc5913ca57e957824b72a85e205", size = 222828, upload-time = "2025-09-08T23:23:26.143Z" },
    { url = "https://files.pythonhosted.org/packages/c6/0f/cafacebd4b040e3119dcb32fed8bdef8dfe94da653155f9d0b9dc660166e/cffi-2.0.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:38100abb9d1b1435bc4cc340bb4489635dc2f0da7456590877030c9b3d40b0c1", size = 220926, upload-time = "2025-09-08T23:23:27.873Z" },
    { url = "https://files.pythonhosted.org/packages/3e/aa/df335faa45b395396fcbc03de2dfcab242cd61a9900e914fe682a59170b1/cffi-2.0.0-cp314-cp314-win32.whl", hash = "sha256:087067fa8953339c723661eda6b54bc98c5625757ea62e95eb4898ad5e776e9f", size = 175328, upload-time = "2025-09-08T23:23:44.61Z" },
    { url = "https://files.pythonhosted.org/packages/bb/92/882c2d30831744296ce713f0feb4c1cd30f346ef747b530b5318715cc367/cffi-2.0.0-cp314-cp314-win_amd64.whl", hash = "sha256:203a48d1fb583fc7d78a4c6655692963b860a417c0528492a6bc21f1aaefab25", size = 185650, upload-time = "2025-09-08T23:23:45.848Z" },
    { url = "https://files.pythonhosted.org/packages/9f/2c/98ece204b9d35a7366b5b2c6539c350313ca13932143e79dc133ba757104/cffi-2.0.0-cp314-cp314-win_arm64.whl", hash = "sha256:dbd5c7a25a7cb98f5ca55d258b103a2054f859a46ae11aaf23134f9cc0d356ad", size = 180687, upload-time = "2025-09-08T23:23:47.105Z" },
    { url = "https://files.pythonhosted.org/packages/3e/61/c768e4d548bfa607abcda77423448df8c471f25dbe64fb2ef6d555eae006/cffi-2.0.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:9a67fc9e8eb39039280526379fb3a70023d77caec1852002b4da7e8b270c4dd9", size = 188773, upload-time = "2025-09-08T23:23:29.347Z" },
    { url = "https://files.pythonhosted.org/packages/2c/ea/5f76bce7cf6fcd0ab1a1058b5af899bfbef198bea4d5686da88471ea0336/cffi-2.0.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7a66c7204d8869299919db4d5069a82f1561581af12b11b3c9f48c584eb8743d", size = 185013, upload-time = "2025-09-08T23:23:30.63Z" },
    { url = "https://files.pythonhosted.org/packages/be/b4/c56878d0d1755cf9caa54ba71e5d049479c52f9e4afc230f06822162ab2f/cffi-2.0.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:7cc09976e8b56f8cebd752f7113ad07752461f48a58cbba644139015ac24954c", size = 221593, upload-time = "2025-09-08T23:23:31.91Z" },
    { url = "https://files.pythonhosted.org/packages/e0/0d/eb704606dfe8033e7128df5e90fee946bbcb64a04fcdaa97321309004000/cffi-2.0.0-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:92b68146a71df78564e4ef48af17551a5ddd142e5190cdf2c5624d0c3ff5b2e8", size = 209354, upload-time = "2025-09-08T23:23:33.214Z" },
    { url = "https://files.pythonhosted.org/packages/d8/19/3c435d727b368ca475fb8742ab97c9cb13a0de600ce86f62eab7fa3eea60/cffi-2.0.0-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:b1e74d11748e7e98e2f426ab176d4ed720a64412b6a15054378afdb71e0f37dc", size = 208480, upload-time = "2025-09-08T23:23:34.495Z" },
    { url = "https://files.pythonhosted.org/packages/d0/44/681604464ed9541673e486521497406fadcc15b5217c3e326b061696899a/cffi-2.0.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:28a3a209b96630bca57cce802da70c266eb08c6e97e5afd61a75611ee6c64592", size = 221584, upload-time = "2025-09-08T23:23:36.096Z" },
    { url = "https://files.pythonhosted.org/packages/25/8e/342a504ff018a2825d395d44d63a767dd8ebc927ebda557fecdaca3ac33a/cffi-2.0.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:7553fb2090d71822f02c629afe6042c299edf91ba1bf94951165613553984512", size = 224443, upload-time = "2025-09-08T23:23:37.328Z" },
    { url = "https://files.pythonhosted.org/packages/e1/5e/b666bacbbc60fbf415ba9988324a132c9a7a0448a9a8f125074671c0f2c3/cffi-2.0.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:6c6c373cfc5c83a975506110d17457138c8c63016b563cc9ed6e056a82f13ce4", size = 223437, upload-time = "2025-09-08T23:23:38.945Z" },
    { url = "https://files.pythonhosted.org/packages/a0/1d/ec1a60bd1a10daa292d3cd6bb0b359a81607154fb8165f3ec95fe003b85c/cffi-2.0.0-cp314-cp314t-win32.whl", hash = "sha256:1fc9ea04857caf665289b7a75923f2c6ed559b8298a1b8c49e59f7dd95c8481e", size = 180487, upload-time = "2025-09-08T23:23:40.423Z" },
    { url = "https://files.pythonhosted.org/packages/bf/41/4c1168c74fac325c0c8156f04b6749c8b6a8f405bbf91413ba088359f60d/cffi-2.0.0-cp314-cp314t-win_amd64.whl", hash = "sha256:d68b6cef7827e8641e8ef16f4494edda8b36104d79773a334beaa1e3521430f6", size = 191726, upload-time = "2025-09-08T23:23:41.742Z" },
    { url = "https://files.pythonhosted.org/packages/ae/3a/dbeec9d1ee0844c679f6bb5d6ad4e9f198b1224f4e7a32825f47f6192b0c/cffi-2.0.0-cp314-cp314t-win_arm64.whl", hash = "sha256:0a1527a803f0a659de1af2e1fd700213caba79377e27e4693648c2923da066f9", size = 184195, upload-time = "2025-09-08T23:23:43.004Z" },
]

[[package]]
name = "charset-normalizer"
version = "3.4.5"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1d/35/02daf95b9cd686320bb622eb148792655c9412dbb9b67abb5694e5910a24/charset_normalizer-3.4.5.tar.gz", hash = "sha256:95adae7b6c42a6c5b5b559b1a99149f090a57128155daeea91732c8d970d8644", size = 134804, upload-time = "2026-03-06T06:03:19.46Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f5/48/9f34ec4bb24aa3fdba1890c1bddb97c8a4be1bd84ef5c42ac2352563ad05/charset_normalizer-3.4.5-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:ac59c15e3f1465f722607800c68713f9fbc2f672b9eb649fe831da4019ae9b23", size = 280788, upload-time = "2026-03-06T06:01:37.126Z" },
    { url = "https://files.pythonhosted.org/packages/0e/09/6003e7ffeb90cc0560da893e3208396a44c210c5ee42efff539639def59b/charset_normalizer-3.4.5-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:165c7b21d19365464e8f70e5ce5e12524c58b48c78c1f5a57524603c1ab003f8", size = 188890, upload-time = "2026-03-06T06:01:38.73Z" },
    { url = "https://files.pythonhosted.org/packages/42/1e/02706edf19e390680daa694d17e2b8eab4b5f7ac285e2a51168b4b22ee6b/charset_normalizer-3.4.5-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:28269983f25a4da0425743d0d257a2d6921ea7d9b83599d4039486ec5b9f911d", size = 206136, upload-time = "2026-03-06T06:01:40.016Z" },
    { url = "https://files.pythonhosted.org/packages/c7/87/942c3def1b37baf3cf786bad01249190f3ca3d5e63a84f831e704977de1f/charset_normalizer-3.4.5-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d27ce22ec453564770d29d03a9506d449efbb9fa13c00842262b2f6801c48cce", size = 202551, upload-time = "2026-03-06T06:01:41.522Z" },
    { url = "https://files.pythonhosted.org/packages/94/0a/af49691938dfe175d71b8a929bd7e4ace2809c0c5134e28bc535660d5262/charset_normalizer-3.4.5-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0625665e4ebdddb553ab185de5db7054393af8879fb0c87bd5690d14379d6819", size = 195572, upload-time = "2026-03-06T06:01:43.208Z" },
    { url = "https://files.pythonhosted.org/packages/20/ea/dfb1792a8050a8e694cfbde1570ff97ff74e48afd874152d38163d1df9ae/charset_normalizer-3.4.5-cp313-cp313-manylinux_2_31_armv7l.whl", hash = "sha256:c23eb3263356d94858655b3e63f85ac5d50970c6e8febcdde7830209139cc37d", size = 184438, upload-time = "2026-03-06T06:01:44.755Z" },
    { url = "https://files.pythonhosted.org/packages/72/12/c281e2067466e3ddd0595bfaea58a6946765ace5c72dfa3edc2f5f118026/charset_normalizer-3.4.5-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e6302ca4ae283deb0af68d2fbf467474b8b6aedcd3dab4db187e07f94c109763", size = 193035, upload-time = "2026-03-06T06:01:46.051Z" },
    { url = "https://files.pythonhosted.org/packages/ba/4f/3792c056e7708e10464bad0438a44708886fb8f92e3c3d29ec5e2d964d42/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e51ae7d81c825761d941962450f50d041db028b7278e7b08930b4541b3e45cb9", size = 191340, upload-time = "2026-03-06T06:01:47.547Z" },
    { url = "https://files.pythonhosted.org/packages/e7/86/80ddba897127b5c7a9bccc481b0cd36c8fefa485d113262f0fe4332f0bf4/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:597d10dec876923e5c59e48dbd366e852eacb2b806029491d307daea6b917d7c", size = 185464, upload-time = "2026-03-06T06:01:48.764Z" },
    { url = "https://files.pythonhosted.org/packages/4d/00/b5eff85ba198faacab83e0e4b6f0648155f072278e3b392a82478f8b988b/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:5cffde4032a197bd3b42fd0b9509ec60fb70918d6970e4cc773f20fc9180ca67", size = 208014, upload-time = "2026-03-06T06:01:50.371Z" },
    { url = "https://files.pythonhosted.org/packages/c8/11/d36f70be01597fd30850dde8a1269ebc8efadd23ba5785808454f2389bde/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:2da4eedcb6338e2321e831a0165759c0c620e37f8cd044a263ff67493be8ffb3", size = 193297, upload-time = "2026-03-06T06:01:51.933Z" },
    { url = "https://files.pythonhosted.org/packages/1a/1d/259eb0a53d4910536c7c2abb9cb25f4153548efb42800c6a9456764649c0/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:65a126fb4b070d05340a84fc709dd9e7c75d9b063b610ece8a60197a291d0adf", size = 204321, upload-time = "2026-03-06T06:01:53.887Z" },
    { url = "https://files.pythonhosted.org/packages/84/31/faa6c5b9d3688715e1ed1bb9d124c384fe2fc1633a409e503ffe1c6398c1/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:c7a80a9242963416bd81f99349d5f3fce1843c303bd404f204918b6d75a75fd6", size = 197509, upload-time = "2026-03-06T06:01:56.439Z" },
    { url = "https://files.pythonhosted.org/packages/fd/a5/c7d9dd1503ffc08950b3260f5d39ec2366dd08254f0900ecbcf3a6197c7c/charset_normalizer-3.4.5-cp313-cp313-win32.whl", hash = "sha256:f1d725b754e967e648046f00c4facc42d414840f5ccc670c5670f59f83693e4f", size = 132284, upload-time = "2026-03-06T06:01:57.812Z" },
    { url = "https://files.pythonhosted.org/packages/b9/0f/57072b253af40c8aa6636e6de7d75985624c1eb392815b2f934199340a89/charset_normalizer-3.4.5-cp313-cp313-win_amd64.whl", hash = "sha256:e37bd100d2c5d3ba35db9c7c5ba5a9228cbcffe5c4778dc824b164e5257813d7", size = 142630, upload-time = "2026-03-06T06:01:59.062Z" },
    { url = "https://files.pythonhosted.org/packages/31/41/1c4b7cc9f13bd9d369ce3bc993e13d374ce25fa38a2663644283ecf422c1/charset_normalizer-3.4.5-cp313-cp313-win_arm64.whl", hash = "sha256:93b3b2cc5cf1b8743660ce77a4f45f3f6d1172068207c1defc779a36eea6bb36", size = 133254, upload-time = "2026-03-06T06:02:00.281Z" },
    { url = "https://files.pythonhosted.org/packages/43/be/0f0fd9bb4a7fa4fb5067fb7d9ac693d4e928d306f80a0d02bde43a7c4aee/charset_normalizer-3.4.5-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:8197abe5ca1ffb7d91e78360f915eef5addff270f8a71c1fc5be24a56f3e4873", size = 280232, upload-time = "2026-03-06T06:02:01.508Z" },
    { url = "https://files.pythonhosted.org/packages/28/02/983b5445e4bef49cd8c9da73a8e029f0825f39b74a06d201bfaa2e55142a/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a2aecdb364b8a1802afdc7f9327d55dad5366bc97d8502d0f5854e50712dbc5f", size = 189688, upload-time = "2026-03-06T06:02:02.857Z" },
    { url = "https://files.pythonhosted.org/packages/d0/88/152745c5166437687028027dc080e2daed6fe11cfa95a22f4602591c42db/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:a66aa5022bf81ab4b1bebfb009db4fd68e0c6d4307a1ce5ef6a26e5878dfc9e4", size = 206833, upload-time = "2026-03-06T06:02:05.127Z" },
    { url = "https://files.pythonhosted.org/packages/cb/0f/ebc15c8b02af2f19be9678d6eed115feeeccc45ce1f4b098d986c13e8769/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d77f97e515688bd615c1d1f795d540f32542d514242067adcb8ef532504cb9ee", size = 202879, upload-time = "2026-03-06T06:02:06.446Z" },
    { url = "https://files.pythonhosted.org/packages/38/9c/71336bff6934418dc8d1e8a1644176ac9088068bc571da612767619c97b3/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01a1ed54b953303ca7e310fafe0fe347aab348bd81834a0bcd602eb538f89d66", size = 195764, upload-time = "2026-03-06T06:02:08.763Z" },
    { url = "https://files.pythonhosted.org/packages/b7/95/ce92fde4f98615661871bc282a856cf9b8a15f686ba0af012984660d480b/charset_normalizer-3.4.5-cp314-cp314-manylinux_2_31_armv7l.whl", hash = "sha256:b2d37d78297b39a9eb9eb92c0f6df98c706467282055419df141389b23f93362", size = 183728, upload-time = "2026-03-06T06:02:10.137Z" },
    { url = "https://files.pythonhosted.org/packages/1c/e7/f5b4588d94e747ce45ae680f0f242bc2d98dbd4eccfab73e6160b6893893/charset_normalizer-3.4.5-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e71bbb595973622b817c042bd943c3f3667e9c9983ce3d205f973f486fec98a7", size = 192937, upload-time = "2026-03-06T06:02:11.663Z" },
    { url = "https://files.pythonhosted.org/packages/f9/29/9d94ed6b929bf9f48bf6ede6e7474576499f07c4c5e878fb186083622716/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:4cd966c2559f501c6fd69294d082c2934c8dd4719deb32c22961a5ac6db0df1d", size = 192040, upload-time = "2026-03-06T06:02:13.489Z" },
    { url = "https://files.pythonhosted.org/packages/15/d2/1a093a1cf827957f9445f2fe7298bcc16f8fc5e05c1ed2ad1af0b239035e/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:d5e52d127045d6ae01a1e821acfad2f3a1866c54d0e837828538fabe8d9d1bd6", size = 184107, upload-time = "2026-03-06T06:02:14.83Z" },
    { url = "https://files.pythonhosted.org/packages/0f/7d/82068ce16bd36135df7b97f6333c5d808b94e01d4599a682e2337ed5fd14/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:30a2b1a48478c3428d047ed9690d57c23038dac838a87ad624c85c0a78ebeb39", size = 208310, upload-time = "2026-03-06T06:02:16.165Z" },
    { url = "https://files.pythonhosted.org/packages/84/4e/4dfb52307bb6af4a5c9e73e482d171b81d36f522b21ccd28a49656baa680/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:d8ed79b8f6372ca4254955005830fd61c1ccdd8c0fac6603e2c145c61dd95db6", size = 192918, upload-time = "2026-03-06T06:02:18.144Z" },
    { url = "https://files.pythonhosted.org/packages/08/a4/159ff7da662cf7201502ca89980b8f06acf3e887b278956646a8aeb178ab/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:c5af897b45fa606b12464ccbe0014bbf8c09191e0a66aab6aa9d5cf6e77e0c94", size = 204615, upload-time = "2026-03-06T06:02:19.821Z" },
    { url = "https://files.pythonhosted.org/packages/d6/62/0dd6172203cb6b429ffffc9935001fde42e5250d57f07b0c28c6046deb6b/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:1088345bcc93c58d8d8f3d783eca4a6e7a7752bbff26c3eee7e73c597c191c2e", size = 197784, upload-time = "2026-03-06T06:02:21.86Z" },
    { url = "https://files.pythonhosted.org/packages/c7/5e/1aab5cb737039b9c59e63627dc8bbc0d02562a14f831cc450e5f91d84ce1/charset_normalizer-3.4.5-cp314-cp314-win32.whl", hash = "sha256:ee57b926940ba00bca7ba7041e665cc956e55ef482f851b9b65acb20d867e7a2", size = 133009, upload-time = "2026-03-06T06:02:23.289Z" },
    { url = "https://files.pythonhosted.org/packages/40/65/e7c6c77d7aaa4c0d7974f2e403e17f0ed2cb0fc135f77d686b916bf1eead/charset_normalizer-3.4.5-cp314-cp314-win_amd64.whl", hash = "sha256:4481e6da1830c8a1cc0b746b47f603b653dadb690bcd851d039ffaefe70533aa", size = 143511, upload-time = "2026-03-06T06:02:26.195Z" },
    { url = "https://files.pythonhosted.org/packages/ba/91/52b0841c71f152f563b8e072896c14e3d83b195c188b338d3cc2e582d1d4/charset_normalizer-3.4.5-cp314-cp314-win_arm64.whl", hash = "sha256:97ab7787092eb9b50fb47fa04f24c75b768a606af1bcba1957f07f128a7219e4", size = 133775, upload-time = "2026-03-06T06:02:27.473Z" },
    { url = "https://files.pythonhosted.org/packages/c5/60/3a621758945513adfd4db86827a5bafcc615f913dbd0b4c2ed64a65731be/charset_normalizer-3.4.5-py3-none-any.whl", hash = "sha256:9db5e3fcdcee89a78c04dffb3fe33c79f77bd741a624946db2591c81b2fc85b0", size = 55455, upload-time = "2026-03-06T06:03:17.827Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "curl-cffi"
version = "0.14.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "cffi" },
]
sdist = { url = "https://files.pythonhosted.org/packages/9b/c9/0067d9a25ed4592b022d4558157fcdb6e123516083700786d38091688767/curl_cffi-0.14.0.tar.gz", hash = "sha256:5ffbc82e59f05008ec08ea432f0e535418823cda44178ee518906a54f27a5f0f", size = 162633, upload-time = "2025-12-16T03:25:07.931Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/aa/f0/0f21e9688eaac85e705537b3a87a5588d0cefb2f09d83e83e0e8be93aa99/curl_cffi-0.14.0-cp39-abi3-macosx_14_0_arm64.whl", hash = "sha256:e35e89c6a69872f9749d6d5fda642ed4fc159619329e99d577d0104c9aad5893", size = 3087277, upload-time = "2025-12-16T03:24:49.607Z" },
    { url = "https://files.pythonhosted.org/packages/ba/a3/0419bd48fce5b145cb6a2344c6ac17efa588f5b0061f212c88e0723da026/curl_cffi-0.14.0-cp39-abi3-macosx_15_0_x86_64.whl", hash = "sha256:5945478cd28ad7dfb5c54473bcfb6743ee1d66554d57951fdf8fc0e7d8cf4e45", size = 5804650, upload-time = "2025-12-16T03:24:51.518Z" },
    { url = "https://files.pythonhosted.org/packages/e2/07/a238dd062b7841b8caa2fa8a359eb997147ff3161288f0dd46654d898b4d/curl_cffi-0.14.0-cp39-abi3-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c42e8fa3c667db9ccd2e696ee47adcd3cd5b0838d7282f3fc45f6c0ef3cfdfa7", size = 8231918, upload-time = "2025-12-16T03:24:52.862Z" },
    { url = "https://files.pythonhosted.org/packages/7c/d2/ce907c9b37b5caf76ac08db40cc4ce3d9f94c5500db68a195af3513eacbc/curl_cffi-0.14.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:060fe2c99c41d3cb7f894de318ddf4b0301b08dca70453d769bd4e74b36b8483", size = 8654624, upload-time = "2025-12-16T03:24:54.579Z" },
    { url = "https://files.pythonhosted.org/packages/f2/ae/6256995b18c75e6ef76b30753a5109e786813aa79088b27c8eabb1ef85c9/curl_cffi-0.14.0-cp39-abi3-manylinux_2_28_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:b158c41a25388690dd0d40b5bc38d1e0f512135f17fdb8029868cbc1993d2e5b", size = 8010654, upload-time = "2025-12-16T03:24:56.507Z" },
    { url = "https://files.pythonhosted.org/packages/fb/10/ff64249e516b103cb762e0a9dca3ee0f04cf25e2a1d5d9838e0f1273d071/curl_cffi-0.14.0-cp39-abi3-manylinux_2_28_i686.whl", hash = "sha256:1439fbef3500fb723333c826adf0efb0e2e5065a703fb5eccce637a2250db34a", size = 7781969, upload-time = "2025-12-16T03:24:57.885Z" },
    { url = "https://files.pythonhosted.org/packages/51/76/d6f7bb76c2d12811aa7ff16f5e17b678abdd1b357b9a8ac56310ceccabd5/curl_cffi-0.14.0-cp39-abi3-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e7176f2c2d22b542e3cf261072a81deb018cfa7688930f95dddef215caddb469", size = 7969133, upload-time = "2025-12-16T03:24:59.261Z" },
    { url = "https://files.pythonhosted.org/packages/23/7c/cca39c0ed4e1772613d3cba13091c0e9d3b89365e84b9bf9838259a3cd8f/curl_cffi-0.14.0-cp39-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:03f21ade2d72978c2bb8670e9b6de5260e2755092b02d94b70b906813662998d", size = 9080167, upload-time = "2025-12-16T03:25:00.946Z" },
    { url = "https://files.pythonhosted.org/packages/75/03/a942d7119d3e8911094d157598ae0169b1c6ca1bd3f27d7991b279bcc45b/curl_cffi-0.14.0-cp39-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:58ebf02de64ee5c95613209ddacb014c2d2f86298d7080c0a1c12ed876ee0690", size = 9520464, upload-time = "2025-12-16T03:25:02.922Z" },
    { url = "https://files.pythonhosted.org/packages/a2/77/78900e9b0833066d2274bda75cba426fdb4cef7fbf6a4f6a6ca447607bec/curl_cffi-0.14.0-cp39-abi3-win_amd64.whl", hash = "sha256:6e503f9a103f6ae7acfb3890c843b53ec030785a22ae7682a22cc43afb94123e", size = 1677416, upload-time = "2025-12-16T03:25:04.902Z" },
    { url = "https://files.pythonhosted.org/packages/5c/7c/d2ba86b0b3e1e2830bd94163d047de122c69a8df03c5c7c36326c456ad82/curl_cffi-0.14.0-cp39-abi3-win_arm64.whl", hash = "sha256:2eed50a969201605c863c4c31269dfc3e0da52916086ac54553cfa353022425c", size = 1425067, upload-time = "2025-12-16T03:25:06.454Z" },
]

[[package]]
name = "deno"
version = "2.7.5"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/31/8bbaf3fb6a41929ae161be0b2a79b2747b5e5490811573ef60af7e3aeac3/deno-2.7.5.tar.gz", hash = "sha256:50635e0462697fa6e79d90bcacbe98e19f785e604c0e5061754de89b3668af83", size = 8166, upload-time = "2026-03-11T12:48:44.286Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/68/15/47c4b8da4e1b312ab14a2517e3f484c4d67a879cb5099cb6c33b8ce00c8c/deno-2.7.5-py3-none-macosx_10_12_x86_64.whl", hash = "sha256:29cb89cdaea5f36133841fb4da058b1c6cb70d117ebfc7a24c717747b58e8503", size = 46641593, upload-time = "2026-03-11T12:48:16.589Z" },
    { url = "https://files.pythonhosted.org/packages/1c/3a/c3f8842b7499ff3faeb7508711a82b736d3a4c6e0ffb359191386bcf539d/deno-2.7.5-py3-none-macosx_11_0_arm64.whl", hash = "sha256:6456980341e97e4eb88e0c560fa57cd1b5f732e0eaadccc6c47d5ada73a71ff3", size = 43537874, upload-time = "2026-03-11T12:48:21.958Z" },
    { url = "https://files.pythonhosted.org/packages/71/a2/53a013ba3509648582748678d5c6980210a45e0913934f91bfe1ec237e07/deno-2.7.5-py3-none-manylinux_2_27_aarch64.whl", hash = "sha256:fdc1e647a06ef792643237c030f45295692b0abc05d5bc9894fb11fd70876953", size = 47265090, upload-time = "2026-03-11T12:48:26.819Z" },
    { url = "https://files.pythonhosted.org/packages/3e/85/88c76daa72575f7229bb94191f15f4771f0614227bf8467bfe06e051f4ab/deno-2.7.5-py3-none-manylinux_2_27_x86_64.whl", hash = "sha256:c15e6b8ccf5f0808cd5ba243ea4eea7d8d78f6fdff228f5c6c85b96ba286bd3c", size = 49262188, upload-time = "2026-03-11T12:48:32.125Z" },
    { url = "https://files.pythonhosted.org/packages/42/5e/501a92ef93d6d46ed8a1a8c03cff8bcbccbc06c1f59b163113ff09cd23cf/deno-2.7.5-py3-none-win_amd64.whl", hash = "sha256:3e3d06006ee39901dd23068c4a501a4a524fb71c323e22503b1b2ddf236da463", size = 48481169, upload-time = "2026-03-11T12:48:38.684Z" },
]

[[package]]
name = "dill"
version = "0.4.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/81/e1/56027a71e31b02ddc53c7d65b01e68edf64dea2932122fe7746a516f75d5/dill-0.4.1.tar.gz", hash = "sha256:423092df4182177d4d8ba8290c8a5b640c66ab35ec7da59ccfa00f6fa3eea5fa", size = 187315, upload-time = "2026-01-19T02:36:56.85Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1e/77/dc8c558f7593132cf8fefec57c4f60c83b16941c574ac5f619abb3ae7933/dill-0.4.1-py3-none-any.whl", hash = "sha256:1e1ce33e978ae97fcfcff5638477032b801c46c7c65cf717f95fbc2248f79a9d", size = 120019, upload-time = "2026-01-19T02:36:55.663Z" },
]

[[package]]
name = "frozenlist"
version = "1.8.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/2d/f5/c831fac6cc817d26fd54c7eaccd04ef7e0288806943f7cc5bbf69f3ac1f0/frozenlist-1.8.0.tar.gz", hash = "sha256:3ede829ed8d842f6cd48fc7081d7a41001a56f1f38603f9d49bf3020d59a31ad", size = 45875, upload-time = "2025-10-06T05:38:17.865Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2d/40/0832c31a37d60f60ed79e9dfb5a92e1e2af4f40a16a29abcc7992af9edff/frozenlist-1.8.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:8d92f1a84bb12d9e56f818b3a746f3efba93c1b63c8387a73dde655e1e42282a", size = 85717, upload-time = "2025-10-06T05:36:27.341Z" },
    { url = "https://files.pythonhosted.org/packages/30/ba/b0b3de23f40bc55a7057bd38434e25c34fa48e17f20ee273bbde5e0650f3/frozenlist-1.8.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:96153e77a591c8adc2ee805756c61f59fef4cf4073a9275ee86fe8cba41241f7", size = 49651, upload-time = "2025-10-06T05:36:28.855Z" },
    { url = "https://files.pythonhosted.org/packages/0c/ab/6e5080ee374f875296c4243c381bbdef97a9ac39c6e3ce1d5f7d42cb78d6/frozenlist-1.8.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f21f00a91358803399890ab167098c131ec2ddd5f8f5fd5fe9c9f2c6fcd91e40", size = 49417, upload-time = "2025-10-06T05:36:29.877Z" },
    { url = "https://files.pythonhosted.org/packages/d5/4e/e4691508f9477ce67da2015d8c00acd751e6287739123113a9fca6f1604e/frozenlist-1.8.0-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:fb30f9626572a76dfe4293c7194a09fb1fe93ba94c7d4f720dfae3b646b45027", size = 234391, upload-time = "2025-10-06T05:36:31.301Z" },
    { url = "https://files.pythonhosted.org/packages/40/76/c202df58e3acdf12969a7895fd6f3bc016c642e6726aa63bd3025e0fc71c/frozenlist-1.8.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:eaa352d7047a31d87dafcacbabe89df0aa506abb5b1b85a2fb91bc3faa02d822", size = 233048, upload-time = "2025-10-06T05:36:32.531Z" },
    { url = "https://files.pythonhosted.org/packages/f9/c0/8746afb90f17b73ca5979c7a3958116e105ff796e718575175319b5bb4ce/frozenlist-1.8.0-cp313-cp313-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:03ae967b4e297f58f8c774c7eabcce57fe3c2434817d4385c50661845a058121", size = 226549, upload-time = "2025-10-06T05:36:33.706Z" },
    { url = "https://files.pythonhosted.org/packages/7e/eb/4c7eefc718ff72f9b6c4893291abaae5fbc0c82226a32dcd8ef4f7a5dbef/frozenlist-1.8.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:f6292f1de555ffcc675941d65fffffb0a5bcd992905015f85d0592201793e0e5", size = 239833, upload-time = "2025-10-06T05:36:34.947Z" },
    { url = "https://files.pythonhosted.org/packages/c2/4e/e5c02187cf704224f8b21bee886f3d713ca379535f16893233b9d672ea71/frozenlist-1.8.0-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:29548f9b5b5e3460ce7378144c3010363d8035cea44bc0bf02d57f5a685e084e", size = 245363, upload-time = "2025-10-06T05:36:36.534Z" },
    { url = "https://files.pythonhosted.org/packages/1f/96/cb85ec608464472e82ad37a17f844889c36100eed57bea094518bf270692/frozenlist-1.8.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:ec3cc8c5d4084591b4237c0a272cc4f50a5b03396a47d9caaf76f5d7b38a4f11", size = 229314, upload-time = "2025-10-06T05:36:38.582Z" },
    { url = "https://files.pythonhosted.org/packages/5d/6f/4ae69c550e4cee66b57887daeebe006fe985917c01d0fff9caab9883f6d0/frozenlist-1.8.0-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:517279f58009d0b1f2e7c1b130b377a349405da3f7621ed6bfae50b10adf20c1", size = 243365, upload-time = "2025-10-06T05:36:40.152Z" },
    { url = "https://files.pythonhosted.org/packages/7a/58/afd56de246cf11780a40a2c28dc7cbabbf06337cc8ddb1c780a2d97e88d8/frozenlist-1.8.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:db1e72ede2d0d7ccb213f218df6a078a9c09a7de257c2fe8fcef16d5925230b1", size = 237763, upload-time = "2025-10-06T05:36:41.355Z" },
    { url = "https://files.pythonhosted.org/packages/cb/36/cdfaf6ed42e2644740d4a10452d8e97fa1c062e2a8006e4b09f1b5fd7d63/frozenlist-1.8.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:b4dec9482a65c54a5044486847b8a66bf10c9cb4926d42927ec4e8fd5db7fed8", size = 240110, upload-time = "2025-10-06T05:36:42.716Z" },
    { url = "https://files.pythonhosted.org/packages/03/a8/9ea226fbefad669f11b52e864c55f0bd57d3c8d7eb07e9f2e9a0b39502e1/frozenlist-1.8.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:21900c48ae04d13d416f0e1e0c4d81f7931f73a9dfa0b7a8746fb2fe7dd970ed", size = 233717, upload-time = "2025-10-06T05:36:44.251Z" },
    { url = "https://files.pythonhosted.org/packages/1e/0b/1b5531611e83ba7d13ccc9988967ea1b51186af64c42b7a7af465dcc9568/frozenlist-1.8.0-cp313-cp313-win32.whl", hash = "sha256:8b7b94a067d1c504ee0b16def57ad5738701e4ba10cec90529f13fa03c833496", size = 39628, upload-time = "2025-10-06T05:36:45.423Z" },
    { url = "https://files.pythonhosted.org/packages/d8/cf/174c91dbc9cc49bc7b7aab74d8b734e974d1faa8f191c74af9b7e80848e6/frozenlist-1.8.0-cp313-cp313-win_amd64.whl", hash = "sha256:878be833caa6a3821caf85eb39c5ba92d28e85df26d57afb06b35b2efd937231", size = 43882, upload-time = "2025-10-06T05:36:46.796Z" },
    { url = "https://files.pythonhosted.org/packages/c1/17/502cd212cbfa96eb1388614fe39a3fc9ab87dbbe042b66f97acb57474834/frozenlist-1.8.0-cp313-cp313-win_arm64.whl", hash = "sha256:44389d135b3ff43ba8cc89ff7f51f5a0bb6b63d829c8300f79a2fe4fe61bcc62", size = 39676, upload-time = "2025-10-06T05:36:47.8Z" },
    { url = "https://files.pythonhosted.org/packages/d2/5c/3bbfaa920dfab09e76946a5d2833a7cbdf7b9b4a91c714666ac4855b88b4/frozenlist-1.8.0-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:e25ac20a2ef37e91c1b39938b591457666a0fa835c7783c3a8f33ea42870db94", size = 89235, upload-time = "2025-10-06T05:36:48.78Z" },
    { url = "https://files.pythonhosted.org/packages/d2/d6/f03961ef72166cec1687e84e8925838442b615bd0b8854b54923ce5b7b8a/frozenlist-1.8.0-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:07cdca25a91a4386d2e76ad992916a85038a9b97561bf7a3fd12d5d9ce31870c", size = 50742, upload-time = "2025-10-06T05:36:49.837Z" },
    { url = "https://files.pythonhosted.org/packages/1e/bb/a6d12b7ba4c3337667d0e421f7181c82dda448ce4e7ad7ecd249a16fa806/frozenlist-1.8.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:4e0c11f2cc6717e0a741f84a527c52616140741cd812a50422f83dc31749fb52", size = 51725, upload-time = "2025-10-06T05:36:50.851Z" },
    { url = "https://files.pythonhosted.org/packages/bc/71/d1fed0ffe2c2ccd70b43714c6cab0f4188f09f8a67a7914a6b46ee30f274/frozenlist-1.8.0-cp313-cp313t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:b3210649ee28062ea6099cfda39e147fa1bc039583c8ee4481cb7811e2448c51", size = 284533, upload-time = "2025-10-06T05:36:51.898Z" },
    { url = "https://files.pythonhosted.org/packages/c9/1f/fb1685a7b009d89f9bf78a42d94461bc06581f6e718c39344754a5d9bada/frozenlist-1.8.0-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:581ef5194c48035a7de2aefc72ac6539823bb71508189e5de01d60c9dcd5fa65", size = 292506, upload-time = "2025-10-06T05:36:53.101Z" },
    { url = "https://files.pythonhosted.org/packages/e6/3b/b991fe1612703f7e0d05c0cf734c1b77aaf7c7d321df4572e8d36e7048c8/frozenlist-1.8.0-cp313-cp313t-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:3ef2d026f16a2b1866e1d86fc4e1291e1ed8a387b2c333809419a2f8b3a77b82", size = 274161, upload-time = "2025-10-06T05:36:54.309Z" },
    { url = "https://files.pythonhosted.org/packages/ca/ec/c5c618767bcdf66e88945ec0157d7f6c4a1322f1473392319b7a2501ded7/frozenlist-1.8.0-cp313-cp313t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:5500ef82073f599ac84d888e3a8c1f77ac831183244bfd7f11eaa0289fb30714", size = 294676, upload-time = "2025-10-06T05:36:55.566Z" },
    { url = "https://files.pythonhosted.org/packages/7c/ce/3934758637d8f8a88d11f0585d6495ef54b2044ed6ec84492a91fa3b27aa/frozenlist-1.8.0-cp313-cp313t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:50066c3997d0091c411a66e710f4e11752251e6d2d73d70d8d5d4c76442a199d", size = 300638, upload-time = "2025-10-06T05:36:56.758Z" },
    { url = "https://files.pythonhosted.org/packages/fc/4f/a7e4d0d467298f42de4b41cbc7ddaf19d3cfeabaf9ff97c20c6c7ee409f9/frozenlist-1.8.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:5c1c8e78426e59b3f8005e9b19f6ff46e5845895adbde20ece9218319eca6506", size = 283067, upload-time = "2025-10-06T05:36:57.965Z" },
    { url = "https://files.pythonhosted.org/packages/dc/48/c7b163063d55a83772b268e6d1affb960771b0e203b632cfe09522d67ea5/frozenlist-1.8.0-cp313-cp313t-musllinux_1_2_armv7l.whl", hash = "sha256:eefdba20de0d938cec6a89bd4d70f346a03108a19b9df4248d3cf0d88f1b0f51", size = 292101, upload-time = "2025-10-06T05:36:59.237Z" },
    { url = "https://files.pythonhosted.org/packages/9f/d0/2366d3c4ecdc2fd391e0afa6e11500bfba0ea772764d631bbf82f0136c9d/frozenlist-1.8.0-cp313-cp313t-musllinux_1_2_ppc64le.whl", hash = "sha256:cf253e0e1c3ceb4aaff6df637ce033ff6535fb8c70a764a8f46aafd3d6ab798e", size = 289901, upload-time = "2025-10-06T05:37:00.811Z" },
    { url = "https://files.pythonhosted.org/packages/b8/94/daff920e82c1b70e3618a2ac39fbc01ae3e2ff6124e80739ce5d71c9b920/frozenlist-1.8.0-cp313-cp313t-musllinux_1_2_s390x.whl", hash = "sha256:032efa2674356903cd0261c4317a561a6850f3ac864a63fc1583147fb05a79b0", size = 289395, upload-time = "2025-10-06T05:37:02.115Z" },
    { url = "https://files.pythonhosted.org/packages/e3/20/bba307ab4235a09fdcd3cc5508dbabd17c4634a1af4b96e0f69bfe551ebd/frozenlist-1.8.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:6da155091429aeba16851ecb10a9104a108bcd32f6c1642867eadaee401c1c41", size = 283659, upload-time = "2025-10-06T05:37:03.711Z" },
    { url = "https://files.pythonhosted.org/packages/fd/00/04ca1c3a7a124b6de4f8a9a17cc2fcad138b4608e7a3fc5877804b8715d7/frozenlist-1.8.0-cp313-cp313t-win32.whl", hash = "sha256:0f96534f8bfebc1a394209427d0f8a63d343c9779cda6fc25e8e121b5fd8555b", size = 43492, upload-time = "2025-10-06T05:37:04.915Z" },
    { url = "https://files.pythonhosted.org/packages/59/5e/c69f733a86a94ab10f68e496dc6b7e8bc078ebb415281d5698313e3af3a1/frozenlist-1.8.0-cp313-cp313t-win_amd64.whl", hash = "sha256:5d63a068f978fc69421fb0e6eb91a9603187527c86b7cd3f534a5b77a592b888", size = 48034, upload-time = "2025-10-06T05:37:06.343Z" },
    { url = "https://files.pythonhosted.org/packages/16/6c/be9d79775d8abe79b05fa6d23da99ad6e7763a1d080fbae7290b286093fd/frozenlist-1.8.0-cp313-cp313t-win_arm64.whl", hash = "sha256:bf0a7e10b077bf5fb9380ad3ae8ce20ef919a6ad93b4552896419ac7e1d8e042", size = 41749, upload-time = "2025-10-06T05:37:07.431Z" },
    { url = "https://files.pythonhosted.org/packages/f1/c8/85da824b7e7b9b6e7f7705b2ecaf9591ba6f79c1177f324c2735e41d36a2/frozenlist-1.8.0-cp314-cp314-macosx_10_13_universal2.whl", hash = "sha256:cee686f1f4cadeb2136007ddedd0aaf928ab95216e7691c63e50a8ec066336d0", size = 86127, upload-time = "2025-10-06T05:37:08.438Z" },
    { url = "https://files.pythonhosted.org/packages/8e/e8/a1185e236ec66c20afd72399522f142c3724c785789255202d27ae992818/frozenlist-1.8.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:119fb2a1bd47307e899c2fac7f28e85b9a543864df47aa7ec9d3c1b4545f096f", size = 49698, upload-time = "2025-10-06T05:37:09.48Z" },
    { url = "https://files.pythonhosted.org/packages/a1/93/72b1736d68f03fda5fdf0f2180fb6caaae3894f1b854d006ac61ecc727ee/frozenlist-1.8.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:4970ece02dbc8c3a92fcc5228e36a3e933a01a999f7094ff7c23fbd2beeaa67c", size = 49749, upload-time = "2025-10-06T05:37:10.569Z" },
    { url = "https://files.pythonhosted.org/packages/a7/b2/fabede9fafd976b991e9f1b9c8c873ed86f202889b864756f240ce6dd855/frozenlist-1.8.0-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:cba69cb73723c3f329622e34bdbf5ce1f80c21c290ff04256cff1cd3c2036ed2", size = 231298, upload-time = "2025-10-06T05:37:11.993Z" },
    { url = "https://files.pythonhosted.org/packages/3a/3b/d9b1e0b0eed36e70477ffb8360c49c85c8ca8ef9700a4e6711f39a6e8b45/frozenlist-1.8.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:778a11b15673f6f1df23d9586f83c4846c471a8af693a22e066508b77d201ec8", size = 232015, upload-time = "2025-10-06T05:37:13.194Z" },
    { url = "https://files.pythonhosted.org/packages/dc/94/be719d2766c1138148564a3960fc2c06eb688da592bdc25adcf856101be7/frozenlist-1.8.0-cp314-cp314-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:0325024fe97f94c41c08872db482cf8ac4800d80e79222c6b0b7b162d5b13686", size = 225038, upload-time = "2025-10-06T05:37:14.577Z" },
    { url = "https://files.pythonhosted.org/packages/e4/09/6712b6c5465f083f52f50cf74167b92d4ea2f50e46a9eea0523d658454ae/frozenlist-1.8.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:97260ff46b207a82a7567b581ab4190bd4dfa09f4db8a8b49d1a958f6aa4940e", size = 240130, upload-time = "2025-10-06T05:37:15.781Z" },
    { url = "https://files.pythonhosted.org/packages/f8/d4/cd065cdcf21550b54f3ce6a22e143ac9e4836ca42a0de1022da8498eac89/frozenlist-1.8.0-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:54b2077180eb7f83dd52c40b2750d0a9f175e06a42e3213ce047219de902717a", size = 242845, upload-time = "2025-10-06T05:37:17.037Z" },
    { url = "https://files.pythonhosted.org/packages/62/c3/f57a5c8c70cd1ead3d5d5f776f89d33110b1addae0ab010ad774d9a44fb9/frozenlist-1.8.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:2f05983daecab868a31e1da44462873306d3cbfd76d1f0b5b69c473d21dbb128", size = 229131, upload-time = "2025-10-06T05:37:18.221Z" },
    { url = "https://files.pythonhosted.org/packages/6c/52/232476fe9cb64f0742f3fde2b7d26c1dac18b6d62071c74d4ded55e0ef94/frozenlist-1.8.0-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:33f48f51a446114bc5d251fb2954ab0164d5be02ad3382abcbfe07e2531d650f", size = 240542, upload-time = "2025-10-06T05:37:19.771Z" },
    { url = "https://files.pythonhosted.org/packages/5f/85/07bf3f5d0fb5414aee5f47d33c6f5c77bfe49aac680bfece33d4fdf6a246/frozenlist-1.8.0-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:154e55ec0655291b5dd1b8731c637ecdb50975a2ae70c606d100750a540082f7", size = 237308, upload-time = "2025-10-06T05:37:20.969Z" },
    { url = "https://files.pythonhosted.org/packages/11/99/ae3a33d5befd41ac0ca2cc7fd3aa707c9c324de2e89db0e0f45db9a64c26/frozenlist-1.8.0-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:4314debad13beb564b708b4a496020e5306c7333fa9a3ab90374169a20ffab30", size = 238210, upload-time = "2025-10-06T05:37:22.252Z" },
    { url = "https://files.pythonhosted.org/packages/b2/60/b1d2da22f4970e7a155f0adde9b1435712ece01b3cd45ba63702aea33938/frozenlist-1.8.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:073f8bf8becba60aa931eb3bc420b217bb7d5b8f4750e6f8b3be7f3da85d38b7", size = 231972, upload-time = "2025-10-06T05:37:23.5Z" },
    { url = "https://files.pythonhosted.org/packages/3f/ab/945b2f32de889993b9c9133216c068b7fcf257d8595a0ac420ac8677cab0/frozenlist-1.8.0-cp314-cp314-win32.whl", hash = "sha256:bac9c42ba2ac65ddc115d930c78d24ab8d4f465fd3fc473cdedfccadb9429806", size = 40536, upload-time = "2025-10-06T05:37:25.581Z" },
    { url = "https://files.pythonhosted.org/packages/59/ad/9caa9b9c836d9ad6f067157a531ac48b7d36499f5036d4141ce78c230b1b/frozenlist-1.8.0-cp314-cp314-win_amd64.whl", hash = "sha256:3e0761f4d1a44f1d1a47996511752cf3dcec5bbdd9cc2b4fe595caf97754b7a0", size = 44330, upload-time = "2025-10-06T05:37:26.928Z" },
    { url = "https://files.pythonhosted.org/packages/82/13/e6950121764f2676f43534c555249f57030150260aee9dcf7d64efda11dd/frozenlist-1.8.0-cp314-cp314-win_arm64.whl", hash = "sha256:d1eaff1d00c7751b7c6662e9c5ba6eb2c17a2306ba5e2a37f24ddf3cc953402b", size = 40627, upload-time = "2025-10-06T05:37:28.075Z" },
    { url = "https://files.pythonhosted.org/packages/c0/c7/43200656ecc4e02d3f8bc248df68256cd9572b3f0017f0a0c4e93440ae23/frozenlist-1.8.0-cp314-cp314t-macosx_10_13_universal2.whl", hash = "sha256:d3bb933317c52d7ea5004a1c442eef86f426886fba134ef8cf4226ea6ee1821d", size = 89238, upload-time = "2025-10-06T05:37:29.373Z" },
    { url = "https://files.pythonhosted.org/packages/d1/29/55c5f0689b9c0fb765055629f472c0de484dcaf0acee2f7707266ae3583c/frozenlist-1.8.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:8009897cdef112072f93a0efdce29cd819e717fd2f649ee3016efd3cd885a7ed", size = 50738, upload-time = "2025-10-06T05:37:30.792Z" },
    { url = "https://files.pythonhosted.org/packages/ba/7d/b7282a445956506fa11da8c2db7d276adcbf2b17d8bb8407a47685263f90/frozenlist-1.8.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:2c5dcbbc55383e5883246d11fd179782a9d07a986c40f49abe89ddf865913930", size = 51739, upload-time = "2025-10-06T05:37:32.127Z" },
    { url = "https://files.pythonhosted.org/packages/62/1c/3d8622e60d0b767a5510d1d3cf21065b9db874696a51ea6d7a43180a259c/frozenlist-1.8.0-cp314-cp314t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:39ecbc32f1390387d2aa4f5a995e465e9e2f79ba3adcac92d68e3e0afae6657c", size = 284186, upload-time = "2025-10-06T05:37:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/2d/14/aa36d5f85a89679a85a1d44cd7a6657e0b1c75f61e7cad987b203d2daca8/frozenlist-1.8.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:92db2bf818d5cc8d9c1f1fc56b897662e24ea5adb36ad1f1d82875bd64e03c24", size = 292196, upload-time = "2025-10-06T05:37:36.107Z" },
    { url = "https://files.pythonhosted.org/packages/05/23/6bde59eb55abd407d34f77d39a5126fb7b4f109a3f611d3929f14b700c66/frozenlist-1.8.0-cp314-cp314t-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:2dc43a022e555de94c3b68a4ef0b11c4f747d12c024a520c7101709a2144fb37", size = 273830, upload-time = "2025-10-06T05:37:37.663Z" },
    { url = "https://files.pythonhosted.org/packages/d2/3f/22cff331bfad7a8afa616289000ba793347fcd7bc275f3b28ecea2a27909/frozenlist-1.8.0-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:cb89a7f2de3602cfed448095bab3f178399646ab7c61454315089787df07733a", size = 294289, upload-time = "2025-10-06T05:37:39.261Z" },
    { url = "https://files.pythonhosted.org/packages/a4/89/5b057c799de4838b6c69aa82b79705f2027615e01be996d2486a69ca99c4/frozenlist-1.8.0-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:33139dc858c580ea50e7e60a1b0ea003efa1fd42e6ec7fdbad78fff65fad2fd2", size = 300318, upload-time = "2025-10-06T05:37:43.213Z" },
    { url = "https://files.pythonhosted.org/packages/30/de/2c22ab3eb2a8af6d69dc799e48455813bab3690c760de58e1bf43b36da3e/frozenlist-1.8.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:168c0969a329b416119507ba30b9ea13688fafffac1b7822802537569a1cb0ef", size = 282814, upload-time = "2025-10-06T05:37:45.337Z" },
    { url = "https://files.pythonhosted.org/packages/59/f7/970141a6a8dbd7f556d94977858cfb36fa9b66e0892c6dd780d2219d8cd8/frozenlist-1.8.0-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:28bd570e8e189d7f7b001966435f9dac6718324b5be2990ac496cf1ea9ddb7fe", size = 291762, upload-time = "2025-10-06T05:37:46.657Z" },
    { url = "https://files.pythonhosted.org/packages/c1/15/ca1adae83a719f82df9116d66f5bb28bb95557b3951903d39135620ef157/frozenlist-1.8.0-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:b2a095d45c5d46e5e79ba1e5b9cb787f541a8dee0433836cea4b96a2c439dcd8", size = 289470, upload-time = "2025-10-06T05:37:47.946Z" },
    { url = "https://files.pythonhosted.org/packages/ac/83/dca6dc53bf657d371fbc88ddeb21b79891e747189c5de990b9dfff2ccba1/frozenlist-1.8.0-cp314-cp314t-musllinux_1_2_s390x.whl", hash = "sha256:eab8145831a0d56ec9c4139b6c3e594c7a83c2c8be25d5bcf2d86136a532287a", size = 289042, upload-time = "2025-10-06T05:37:49.499Z" },
    { url = "https://files.pythonhosted.org/packages/96/52/abddd34ca99be142f354398700536c5bd315880ed0a213812bc491cff5e4/frozenlist-1.8.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:974b28cf63cc99dfb2188d8d222bc6843656188164848c4f679e63dae4b0708e", size = 283148, upload-time = "2025-10-06T05:37:50.745Z" },
    { url = "https://files.pythonhosted.org/packages/af/d3/76bd4ed4317e7119c2b7f57c3f6934aba26d277acc6309f873341640e21f/frozenlist-1.8.0-cp314-cp314t-win32.whl", hash = "sha256:342c97bf697ac5480c0a7ec73cd700ecfa5a8a40ac923bd035484616efecc2df", size = 44676, upload-time = "2025-10-06T05:37:52.222Z" },
    { url = "https://files.pythonhosted.org/packages/89/76/c615883b7b521ead2944bb3480398cbb07e12b7b4e4d073d3752eb721558/frozenlist-1.8.0-cp314-cp314t-win_amd64.whl", hash = "sha256:06be8f67f39c8b1dc671f5d83aaefd3358ae5cdcf8314552c57e7ed3e6475bdd", size = 49451, upload-time = "2025-10-06T05:37:53.425Z" },
    { url = "https://files.pythonhosted.org/packages/e0/a3/5982da14e113d07b325230f95060e2169f5311b1017ea8af2a29b374c289/frozenlist-1.8.0-cp314-cp314t-win_arm64.whl", hash = "sha256:102e6314ca4da683dca92e3b1355490fed5f313b768500084fbe6371fddfdb79", size = 42507, upload-time = "2025-10-06T05:37:54.513Z" },
    { url = "https://files.pythonhosted.org/packages/9a/9a/e35b4a917281c0b8419d4207f4334c8e8c5dbf4f3f5f9ada73958d937dcc/frozenlist-1.8.0-py3-none-any.whl", hash = "sha256:0c18a16eab41e82c295618a77502e17b195883241c563b00f0aa5106fc4eaa0d", size = 13409, upload-time = "2025-10-06T05:38:16.721Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "isort"
version = "8.0.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ef/7c/ec4ab396d31b3b395e2e999c8f46dec78c5e29209fac49d1f4dace04041d/isort-8.0.1.tar.gz", hash = "sha256:171ac4ff559cdc060bcfff550bc8404a486fee0caab245679c2abe7cb253c78d", size = 769592, upload-time = "2026-02-28T10:08:20.685Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3e/95/c7c34aa53c16353c56d0b802fba48d5f5caa2cdee7958acbcb795c830416/isort-8.0.1-py3-none-any.whl", hash = "sha256:28b89bc70f751b559aeca209e6120393d43fbe2490de0559662be7a9787e3d75", size = 89733, upload-time = "2026-02-28T10:08:19.466Z" },
]

[[package]]
name = "mccabe"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/e7/ff/0ffefdcac38932a54d2b5eed4e0ba8a408f215002cd178ad1df0f2806ff8/mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325", size = 9658, upload-time = "2022-01-24T01:14:51.113Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/27/1a/1f68f9ba0c207934b35b86a8ca3aad8395a3d6dd7921c0686e23853ff5a9/mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e", size = 7350, upload-time = "2022-01-24T01:14:49.62Z" },
]

[[package]]
name = "metube"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "aiohttp" },
    { name = "curl-cffi" },
    { name = "mutagen" },
    { name = "python-socketio" },
    { name = "watchfiles" },
    { name = "yt-dlp", extra = ["curl-cffi", "default", "deno"] },
]

[package.dev-dependencies]
dev = [
    { name = "pylint" },
]

[package.metadata]
requires-dist = [
    { name = "aiohttp" },
    { name = "curl-cffi" },
    { name = "mutagen" },
    { name = "python-socketio", specifier = ">=5.0,<6.0" },
    { name = "watchfiles" },
    { name = "yt-dlp", extras = ["default", "curl-cffi", "deno"] },
]

[package.metadata.requires-dev]
dev = [{ name = "pylint" }]

[[package]]
name = "multidict"
version = "6.7.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1a/c2/c2d94cbe6ac1753f3fc980da97b3d930efe1da3af3c9f5125354436c073d/multidict-6.7.1.tar.gz", hash = "sha256:ec6652a1bee61c53a3e5776b6049172c53b6aaba34f18c9ad04f82712bac623d", size = 102010, upload-time = "2026-01-26T02:46:45.979Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f2/22/929c141d6c0dba87d3e1d38fbdf1ba8baba86b7776469f2bc2d3227a1e67/multidict-6.7.1-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:2b41f5fed0ed563624f1c17630cb9941cf2309d4df00e494b551b5f3e3d67a23", size = 76174, upload-time = "2026-01-26T02:44:18.509Z" },
    { url = "https://files.pythonhosted.org/packages/c7/75/bc704ae15fee974f8fccd871305e254754167dce5f9e42d88a2def741a1d/multidict-6.7.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:84e61e3af5463c19b67ced91f6c634effb89ef8bfc5ca0267f954451ed4bb6a2", size = 45116, upload-time = "2026-01-26T02:44:19.745Z" },
    { url = "https://files.pythonhosted.org/packages/79/76/55cd7186f498ed080a18440c9013011eb548f77ae1b297206d030eb1180a/multidict-6.7.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:935434b9853c7c112eee7ac891bc4cb86455aa631269ae35442cb316790c1445", size = 43524, upload-time = "2026-01-26T02:44:21.571Z" },
    { url = "https://files.pythonhosted.org/packages/e9/3c/414842ef8d5a1628d68edee29ba0e5bcf235dbfb3ccd3ea303a7fe8c72ff/multidict-6.7.1-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:432feb25a1cb67fe82a9680b4d65fb542e4635cb3166cd9c01560651ad60f177", size = 249368, upload-time = "2026-01-26T02:44:22.803Z" },
    { url = "https://files.pythonhosted.org/packages/f6/32/befed7f74c458b4a525e60519fe8d87eef72bb1e99924fa2b0f9d97a221e/multidict-6.7.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:e82d14e3c948952a1a85503817e038cba5905a3352de76b9a465075d072fba23", size = 256952, upload-time = "2026-01-26T02:44:24.306Z" },
    { url = "https://files.pythonhosted.org/packages/03/d6/c878a44ba877f366630c860fdf74bfb203c33778f12b6ac274936853c451/multidict-6.7.1-cp313-cp313-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:4cfb48c6ea66c83bcaaf7e4dfa7ec1b6bbcf751b7db85a328902796dfde4c060", size = 240317, upload-time = "2026-01-26T02:44:25.772Z" },
    { url = "https://files.pythonhosted.org/packages/68/49/57421b4d7ad2e9e60e25922b08ceb37e077b90444bde6ead629095327a6f/multidict-6.7.1-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:1d540e51b7e8e170174555edecddbd5538105443754539193e3e1061864d444d", size = 267132, upload-time = "2026-01-26T02:44:27.648Z" },
    { url = "https://files.pythonhosted.org/packages/b7/fe/ec0edd52ddbcea2a2e89e174f0206444a61440b40f39704e64dc807a70bd/multidict-6.7.1-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:273d23f4b40f3dce4d6c8a821c741a86dec62cded82e1175ba3d99be128147ed", size = 268140, upload-time = "2026-01-26T02:44:29.588Z" },
    { url = "https://files.pythonhosted.org/packages/b0/73/6e1b01cbeb458807aa0831742232dbdd1fa92bfa33f52a3f176b4ff3dc11/multidict-6.7.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9d624335fd4fa1c08a53f8b4be7676ebde19cd092b3895c421045ca87895b429", size = 254277, upload-time = "2026-01-26T02:44:30.902Z" },
    { url = "https://files.pythonhosted.org/packages/6a/b2/5fb8c124d7561a4974c342bc8c778b471ebbeb3cc17df696f034a7e9afe7/multidict-6.7.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:12fad252f8b267cc75b66e8fc51b3079604e8d43a75428ffe193cd9e2195dfd6", size = 252291, upload-time = "2026-01-26T02:44:32.31Z" },
    { url = "https://files.pythonhosted.org/packages/5a/96/51d4e4e06bcce92577fcd488e22600bd38e4fd59c20cb49434d054903bd2/multidict-6.7.1-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:03ede2a6ffbe8ef936b92cb4529f27f42be7f56afcdab5ab739cd5f27fb1cbf9", size = 250156, upload-time = "2026-01-26T02:44:33.734Z" },
    { url = "https://files.pythonhosted.org/packages/db/6b/420e173eec5fba721a50e2a9f89eda89d9c98fded1124f8d5c675f7a0c0f/multidict-6.7.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:90efbcf47dbe33dcf643a1e400d67d59abeac5db07dc3f27d6bdeae497a2198c", size = 249742, upload-time = "2026-01-26T02:44:35.222Z" },
    { url = "https://files.pythonhosted.org/packages/44/a3/ec5b5bd98f306bc2aa297b8c6f11a46714a56b1e6ef5ebda50a4f5d7c5fb/multidict-6.7.1-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:5c4b9bfc148f5a91be9244d6264c53035c8a0dcd2f51f1c3c6e30e30ebaa1c84", size = 262221, upload-time = "2026-01-26T02:44:36.604Z" },
    { url = "https://files.pythonhosted.org/packages/cd/f7/e8c0d0da0cd1e28d10e624604e1a36bcc3353aaebdfdc3a43c72bc683a12/multidict-6.7.1-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:401c5a650f3add2472d1d288c26deebc540f99e2fb83e9525007a74cd2116f1d", size = 258664, upload-time = "2026-01-26T02:44:38.008Z" },
    { url = "https://files.pythonhosted.org/packages/52/da/151a44e8016dd33feed44f730bd856a66257c1ee7aed4f44b649fb7edeb3/multidict-6.7.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:97891f3b1b3ffbded884e2916cacf3c6fc87b66bb0dde46f7357404750559f33", size = 249490, upload-time = "2026-01-26T02:44:39.386Z" },
    { url = "https://files.pythonhosted.org/packages/87/af/a3b86bf9630b732897f6fc3f4c4714b90aa4361983ccbdcd6c0339b21b0c/multidict-6.7.1-cp313-cp313-win32.whl", hash = "sha256:e1c5988359516095535c4301af38d8a8838534158f649c05dd1050222321bcb3", size = 41695, upload-time = "2026-01-26T02:44:41.318Z" },
    { url = "https://files.pythonhosted.org/packages/b2/35/e994121b0e90e46134673422dd564623f93304614f5d11886b1b3e06f503/multidict-6.7.1-cp313-cp313-win_amd64.whl", hash = "sha256:960c83bf01a95b12b08fd54324a4eb1d5b52c88932b5cba5d6e712bb3ed12eb5", size = 45884, upload-time = "2026-01-26T02:44:42.488Z" },
    { url = "https://files.pythonhosted.org/packages/ca/61/42d3e5dbf661242a69c97ea363f2d7b46c567da8eadef8890022be6e2ab0/multidict-6.7.1-cp313-cp313-win_arm64.whl", hash = "sha256:563fe25c678aaba333d5399408f5ec3c383ca5b663e7f774dd179a520b8144df", size = 43122, upload-time = "2026-01-26T02:44:43.664Z" },
    { url = "https://files.pythonhosted.org/packages/6d/b3/e6b21c6c4f314bb956016b0b3ef2162590a529b84cb831c257519e7fde44/multidict-6.7.1-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:c76c4bec1538375dad9d452d246ca5368ad6e1c9039dadcf007ae59c70619ea1", size = 83175, upload-time = "2026-01-26T02:44:44.894Z" },
    { url = "https://files.pythonhosted.org/packages/fb/76/23ecd2abfe0957b234f6c960f4ade497f55f2c16aeb684d4ecdbf1c95791/multidict-6.7.1-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:57b46b24b5d5ebcc978da4ec23a819a9402b4228b8a90d9c656422b4bdd8a963", size = 48460, upload-time = "2026-01-26T02:44:46.106Z" },
    { url = "https://files.pythonhosted.org/packages/c4/57/a0ed92b23f3a042c36bc4227b72b97eca803f5f1801c1ab77c8a212d455e/multidict-6.7.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:e954b24433c768ce78ab7929e84ccf3422e46deb45a4dc9f93438f8217fa2d34", size = 46930, upload-time = "2026-01-26T02:44:47.278Z" },
    { url = "https://files.pythonhosted.org/packages/b5/66/02ec7ace29162e447f6382c495dc95826bf931d3818799bbef11e8f7df1a/multidict-6.7.1-cp313-cp313t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:3bd231490fa7217cc832528e1cd8752a96f0125ddd2b5749390f7c3ec8721b65", size = 242582, upload-time = "2026-01-26T02:44:48.604Z" },
    { url = "https://files.pythonhosted.org/packages/58/18/64f5a795e7677670e872673aca234162514696274597b3708b2c0d276cce/multidict-6.7.1-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:253282d70d67885a15c8a7716f3a73edf2d635793ceda8173b9ecc21f2fb8292", size = 250031, upload-time = "2026-01-26T02:44:50.544Z" },
    { url = "https://files.pythonhosted.org/packages/c8/ed/e192291dbbe51a8290c5686f482084d31bcd9d09af24f63358c3d42fd284/multidict-6.7.1-cp313-cp313t-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:0b4c48648d7649c9335cf1927a8b87fa692de3dcb15faa676c6a6f1f1aabda43", size = 228596, upload-time = "2026-01-26T02:44:51.951Z" },
    { url = "https://files.pythonhosted.org/packages/1e/7e/3562a15a60cf747397e7f2180b0a11dc0c38d9175a650e75fa1b4d325e15/multidict-6.7.1-cp313-cp313t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:98bc624954ec4d2c7cb074b8eefc2b5d0ce7d482e410df446414355d158fe4ca", size = 257492, upload-time = "2026-01-26T02:44:53.902Z" },
    { url = "https://files.pythonhosted.org/packages/24/02/7d0f9eae92b5249bb50ac1595b295f10e263dd0078ebb55115c31e0eaccd/multidict-6.7.1-cp313-cp313t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:1b99af4d9eec0b49927b4402bcbb58dea89d3e0db8806a4086117019939ad3dd", size = 255899, upload-time = "2026-01-26T02:44:55.316Z" },
    { url = "https://files.pythonhosted.org/packages/00/e3/9b60ed9e23e64c73a5cde95269ef1330678e9c6e34dd4eb6b431b85b5a10/multidict-6.7.1-cp313-cp313t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6aac4f16b472d5b7dc6f66a0d49dd57b0e0902090be16594dc9ebfd3d17c47e7", size = 247970, upload-time = "2026-01-26T02:44:56.783Z" },
    { url = "https://files.pythonhosted.org/packages/3e/06/538e58a63ed5cfb0bd4517e346b91da32fde409d839720f664e9a4ae4f9d/multidict-6.7.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:21f830fe223215dffd51f538e78c172ed7c7f60c9b96a2bf05c4848ad49921c3", size = 245060, upload-time = "2026-01-26T02:44:58.195Z" },
    { url = "https://files.pythonhosted.org/packages/b2/2f/d743a3045a97c895d401e9bd29aaa09b94f5cbdf1bd561609e5a6c431c70/multidict-6.7.1-cp313-cp313t-musllinux_1_2_armv7l.whl", hash = "sha256:f5dd81c45b05518b9aa4da4aa74e1c93d715efa234fd3e8a179df611cc85e5f4", size = 235888, upload-time = "2026-01-26T02:44:59.57Z" },
    { url = "https://files.pythonhosted.org/packages/38/83/5a325cac191ab28b63c52f14f1131f3b0a55ba3b9aa65a6d0bf2a9b921a0/multidict-6.7.1-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:eb304767bca2bb92fb9c5bd33cedc95baee5bb5f6c88e63706533a1c06ad08c8", size = 243554, upload-time = "2026-01-26T02:45:01.054Z" },
    { url = "https://files.pythonhosted.org/packages/20/1f/9d2327086bd15da2725ef6aae624208e2ef828ed99892b17f60c344e57ed/multidict-6.7.1-cp313-cp313t-musllinux_1_2_ppc64le.whl", hash = "sha256:c9035dde0f916702850ef66460bc4239d89d08df4d02023a5926e7446724212c", size = 252341, upload-time = "2026-01-26T02:45:02.484Z" },
    { url = "https://files.pythonhosted.org/packages/e8/2c/2a1aa0280cf579d0f6eed8ee5211c4f1730bd7e06c636ba2ee6aafda302e/multidict-6.7.1-cp313-cp313t-musllinux_1_2_s390x.whl", hash = "sha256:af959b9beeb66c822380f222f0e0a1889331597e81f1ded7f374f3ecb0fd6c52", size = 246391, upload-time = "2026-01-26T02:45:03.862Z" },
    { url = "https://files.pythonhosted.org/packages/e5/03/7ca022ffc36c5a3f6e03b179a5ceb829be9da5783e6fe395f347c0794680/multidict-6.7.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:41f2952231456154ee479651491e94118229844dd7226541788be783be2b5108", size = 243422, upload-time = "2026-01-26T02:45:05.296Z" },
    { url = "https://files.pythonhosted.org/packages/dc/1d/b31650eab6c5778aceed46ba735bd97f7c7d2f54b319fa916c0f96e7805b/multidict-6.7.1-cp313-cp313t-win32.whl", hash = "sha256:df9f19c28adcb40b6aae30bbaa1478c389efd50c28d541d76760199fc1037c32", size = 47770, upload-time = "2026-01-26T02:45:06.754Z" },
    { url = "https://files.pythonhosted.org/packages/ac/5b/2d2d1d522e51285bd61b1e20df8f47ae1a9d80839db0b24ea783b3832832/multidict-6.7.1-cp313-cp313t-win_amd64.whl", hash = "sha256:d54ecf9f301853f2c5e802da559604b3e95bb7a3b01a9c295c6ee591b9882de8", size = 53109, upload-time = "2026-01-26T02:45:08.044Z" },
    { url = "https://files.pythonhosted.org/packages/3d/a3/cc409ba012c83ca024a308516703cf339bdc4b696195644a7215a5164a24/multidict-6.7.1-cp313-cp313t-win_arm64.whl", hash = "sha256:5a37ca18e360377cfda1d62f5f382ff41f2b8c4ccb329ed974cc2e1643440118", size = 45573, upload-time = "2026-01-26T02:45:09.349Z" },
    { url = "https://files.pythonhosted.org/packages/91/cc/db74228a8be41884a567e88a62fd589a913708fcf180d029898c17a9a371/multidict-6.7.1-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:8f333ec9c5eb1b7105e3b84b53141e66ca05a19a605368c55450b6ba208cb9ee", size = 75190, upload-time = "2026-01-26T02:45:10.651Z" },
    { url = "https://files.pythonhosted.org/packages/d5/22/492f2246bb5b534abd44804292e81eeaf835388901f0c574bac4eeec73c5/multidict-6.7.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:a407f13c188f804c759fc6a9f88286a565c242a76b27626594c133b82883b5c2", size = 44486, upload-time = "2026-01-26T02:45:11.938Z" },
    { url = "https://files.pythonhosted.org/packages/f1/4f/733c48f270565d78b4544f2baddc2fb2a245e5a8640254b12c36ac7ac68e/multidict-6.7.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:0e161ddf326db5577c3a4cc2d8648f81456e8a20d40415541587a71620d7a7d1", size = 43219, upload-time = "2026-01-26T02:45:14.346Z" },
    { url = "https://files.pythonhosted.org/packages/24/bb/2c0c2287963f4259c85e8bcbba9182ced8d7fca65c780c38e99e61629d11/multidict-6.7.1-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:1e3a8bb24342a8201d178c3b4984c26ba81a577c80d4d525727427460a50c22d", size = 245132, upload-time = "2026-01-26T02:45:15.712Z" },
    { url = "https://files.pythonhosted.org/packages/a7/f9/44d4b3064c65079d2467888794dea218d1601898ac50222ab8a9a8094460/multidict-6.7.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:97231140a50f5d447d3164f994b86a0bed7cd016e2682f8650d6a9158e14fd31", size = 252420, upload-time = "2026-01-26T02:45:17.293Z" },
    { url = "https://files.pythonhosted.org/packages/8b/13/78f7275e73fa17b24c9a51b0bd9d73ba64bb32d0ed51b02a746eb876abe7/multidict-6.7.1-cp314-cp314-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:6b10359683bd8806a200fd2909e7c8ca3a7b24ec1d8132e483d58e791d881048", size = 233510, upload-time = "2026-01-26T02:45:19.356Z" },
    { url = "https://files.pythonhosted.org/packages/4b/25/8167187f62ae3cbd52da7893f58cb036b47ea3fb67138787c76800158982/multidict-6.7.1-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:283ddac99f7ac25a4acadbf004cb5ae34480bbeb063520f70ce397b281859362", size = 264094, upload-time = "2026-01-26T02:45:20.834Z" },
    { url = "https://files.pythonhosted.org/packages/a1/e7/69a3a83b7b030cf283fb06ce074a05a02322359783424d7edf0f15fe5022/multidict-6.7.1-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:538cec1e18c067d0e6103aa9a74f9e832904c957adc260e61cd9d8cf0c3b3d37", size = 260786, upload-time = "2026-01-26T02:45:22.818Z" },
    { url = "https://files.pythonhosted.org/packages/fe/3b/8ec5074bcfc450fe84273713b4b0a0dd47c0249358f5d82eb8104ffe2520/multidict-6.7.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7eee46ccb30ff48a1e35bb818cc90846c6be2b68240e42a78599166722cea709", size = 248483, upload-time = "2026-01-26T02:45:24.368Z" },
    { url = "https://files.pythonhosted.org/packages/48/5a/d5a99e3acbca0e29c5d9cba8f92ceb15dce78bab963b308ae692981e3a5d/multidict-6.7.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:fa263a02f4f2dd2d11a7b1bb4362aa7cb1049f84a9235d31adf63f30143469a0", size = 248403, upload-time = "2026-01-26T02:45:25.982Z" },
    { url = "https://files.pythonhosted.org/packages/35/48/e58cd31f6c7d5102f2a4bf89f96b9cf7e00b6c6f3d04ecc44417c00a5a3c/multidict-6.7.1-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:2e1425e2f99ec5bd36c15a01b690a1a2456209c5deed58f95469ffb46039ccbb", size = 240315, upload-time = "2026-01-26T02:45:27.487Z" },
    { url = "https://files.pythonhosted.org/packages/94/33/1cd210229559cb90b6786c30676bb0c58249ff42f942765f88793b41fdce/multidict-6.7.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:497394b3239fc6f0e13a78a3e1b61296e72bf1c5f94b4c4eb80b265c37a131cd", size = 245528, upload-time = "2026-01-26T02:45:28.991Z" },
    { url = "https://files.pythonhosted.org/packages/64/f2/6e1107d226278c876c783056b7db43d800bb64c6131cec9c8dfb6903698e/multidict-6.7.1-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:233b398c29d3f1b9676b4b6f75c518a06fcb2ea0b925119fb2c1bc35c05e1601", size = 258784, upload-time = "2026-01-26T02:45:30.503Z" },
    { url = "https://files.pythonhosted.org/packages/4d/c1/11f664f14d525e4a1b5327a82d4de61a1db604ab34c6603bb3c2cc63ad34/multidict-6.7.1-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:93b1818e4a6e0930454f0f2af7dfce69307ca03cdcfb3739bf4d91241967b6c1", size = 251980, upload-time = "2026-01-26T02:45:32.603Z" },
    { url = "https://files.pythonhosted.org/packages/e1/9f/75a9ac888121d0c5bbd4ecf4eead45668b1766f6baabfb3b7f66a410e231/multidict-6.7.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:f33dc2a3abe9249ea5d8360f969ec7f4142e7ac45ee7014d8f8d5acddf178b7b", size = 243602, upload-time = "2026-01-26T02:45:34.043Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e7/50bf7b004cc8525d80dbbbedfdc7aed3e4c323810890be4413e589074032/multidict-6.7.1-cp314-cp314-win32.whl", hash = "sha256:3ab8b9d8b75aef9df299595d5388b14530839f6422333357af1339443cff777d", size = 40930, upload-time = "2026-01-26T02:45:36.278Z" },
    { url = "https://files.pythonhosted.org/packages/e0/bf/52f25716bbe93745595800f36fb17b73711f14da59ed0bb2eba141bc9f0f/multidict-6.7.1-cp314-cp314-win_amd64.whl", hash = "sha256:5e01429a929600e7dab7b166062d9bb54a5eed752384c7384c968c2afab8f50f", size = 45074, upload-time = "2026-01-26T02:45:37.546Z" },
    { url = "https://files.pythonhosted.org/packages/97/ab/22803b03285fa3a525f48217963da3a65ae40f6a1b6f6cf2768879e208f9/multidict-6.7.1-cp314-cp314-win_arm64.whl", hash = "sha256:4885cb0e817aef5d00a2e8451d4665c1808378dc27c2705f1bf4ef8505c0d2e5", size = 42471, upload-time = "2026-01-26T02:45:38.889Z" },
    { url = "https://files.pythonhosted.org/packages/e0/6d/f9293baa6146ba9507e360ea0292b6422b016907c393e2f63fc40ab7b7b5/multidict-6.7.1-cp314-cp314t-macosx_10_15_universal2.whl", hash = "sha256:0458c978acd8e6ea53c81eefaddbbee9c6c5e591f41b3f5e8e194780fe026581", size = 82401, upload-time = "2026-01-26T02:45:40.254Z" },
    { url = "https://files.pythonhosted.org/packages/7a/68/53b5494738d83558d87c3c71a486504d8373421c3e0dbb6d0db48ad42ee0/multidict-6.7.1-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:c0abd12629b0af3cf590982c0b413b1e7395cd4ec026f30986818ab95bfaa94a", size = 48143, upload-time = "2026-01-26T02:45:41.635Z" },
    { url = "https://files.pythonhosted.org/packages/37/e8/5284c53310dcdc99ce5d66563f6e5773531a9b9fe9ec7a615e9bc306b05f/multidict-6.7.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:14525a5f61d7d0c94b368a42cff4c9a4e7ba2d52e2672a7b23d84dc86fb02b0c", size = 46507, upload-time = "2026-01-26T02:45:42.99Z" },
    { url = "https://files.pythonhosted.org/packages/e4/fc/6800d0e5b3875568b4083ecf5f310dcf91d86d52573160834fb4bfcf5e4f/multidict-6.7.1-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:17307b22c217b4cf05033dabefe68255a534d637c6c9b0cc8382718f87be4262", size = 239358, upload-time = "2026-01-26T02:45:44.376Z" },
    { url = "https://files.pythonhosted.org/packages/41/75/4ad0973179361cdf3a113905e6e088173198349131be2b390f9fa4da5fc6/multidict-6.7.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7a7e590ff876a3eaf1c02a4dfe0724b6e69a9e9de6d8f556816f29c496046e59", size = 246884, upload-time = "2026-01-26T02:45:47.167Z" },
    { url = "https://files.pythonhosted.org/packages/c3/9c/095bb28b5da139bd41fb9a5d5caff412584f377914bd8787c2aa98717130/multidict-6.7.1-cp314-cp314t-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:5fa6a95dfee63893d80a34758cd0e0c118a30b8dcb46372bf75106c591b77889", size = 225878, upload-time = "2026-01-26T02:45:48.698Z" },
    { url = "https://files.pythonhosted.org/packages/07/d0/c0a72000243756e8f5a277b6b514fa005f2c73d481b7d9e47cd4568aa2e4/multidict-6.7.1-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:a0543217a6a017692aa6ae5cc39adb75e587af0f3a82288b1492eb73dd6cc2a4", size = 253542, upload-time = "2026-01-26T02:45:50.164Z" },
    { url = "https://files.pythonhosted.org/packages/c0/6b/f69da15289e384ecf2a68837ec8b5ad8c33e973aa18b266f50fe55f24b8c/multidict-6.7.1-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:f99fe611c312b3c1c0ace793f92464d8cd263cc3b26b5721950d977b006b6c4d", size = 252403, upload-time = "2026-01-26T02:45:51.779Z" },
    { url = "https://files.pythonhosted.org/packages/a2/76/b9669547afa5a1a25cd93eaca91c0da1c095b06b6d2d8ec25b713588d3a1/multidict-6.7.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9004d8386d133b7e6135679424c91b0b854d2d164af6ea3f289f8f2761064609", size = 244889, upload-time = "2026-01-26T02:45:53.27Z" },
    { url = "https://files.pythonhosted.org/packages/7e/a9/a50d2669e506dad33cfc45b5d574a205587b7b8a5f426f2fbb2e90882588/multidict-6.7.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:e628ef0e6859ffd8273c69412a2465c4be4a9517d07261b33334b5ec6f3c7489", size = 241982, upload-time = "2026-01-26T02:45:54.919Z" },
    { url = "https://files.pythonhosted.org/packages/c5/bb/1609558ad8b456b4827d3c5a5b775c93b87878fd3117ed3db3423dfbce1b/multidict-6.7.1-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:841189848ba629c3552035a6a7f5bf3b02eb304e9fea7492ca220a8eda6b0e5c", size = 232415, upload-time = "2026-01-26T02:45:56.981Z" },
    { url = "https://files.pythonhosted.org/packages/d8/59/6f61039d2aa9261871e03ab9dc058a550d240f25859b05b67fd70f80d4b3/multidict-6.7.1-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:ce1bbd7d780bb5a0da032e095c951f7014d6b0a205f8318308140f1a6aba159e", size = 240337, upload-time = "2026-01-26T02:45:58.698Z" },
    { url = "https://files.pythonhosted.org/packages/a1/29/fdc6a43c203890dc2ae9249971ecd0c41deaedfe00d25cb6564b2edd99eb/multidict-6.7.1-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:b26684587228afed0d50cf804cc71062cc9c1cdf55051c4c6345d372947b268c", size = 248788, upload-time = "2026-01-26T02:46:00.862Z" },
    { url = "https://files.pythonhosted.org/packages/a9/14/a153a06101323e4cf086ecee3faadba52ff71633d471f9685c42e3736163/multidict-6.7.1-cp314-cp314t-musllinux_1_2_s390x.whl", hash = "sha256:9f9af11306994335398293f9958071019e3ab95e9a707dc1383a35613f6abcb9", size = 242842, upload-time = "2026-01-26T02:46:02.824Z" },
    { url = "https://files.pythonhosted.org/packages/41/5f/604ae839e64a4a6efc80db94465348d3b328ee955e37acb24badbcd24d83/multidict-6.7.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:b4938326284c4f1224178a560987b6cf8b4d38458b113d9b8c1db1a836e640a2", size = 240237, upload-time = "2026-01-26T02:46:05.898Z" },
    { url = "https://files.pythonhosted.org/packages/5f/60/c3a5187bf66f6fb546ff4ab8fb5a077cbdd832d7b1908d4365c7f74a1917/multidict-6.7.1-cp314-cp314t-win32.whl", hash = "sha256:98655c737850c064a65e006a3df7c997cd3b220be4ec8fe26215760b9697d4d7", size = 48008, upload-time = "2026-01-26T02:46:07.468Z" },
    { url = "https://files.pythonhosted.org/packages/0c/f7/addf1087b860ac60e6f382240f64fb99f8bfb532bb06f7c542b83c29ca61/multidict-6.7.1-cp314-cp314t-win_amd64.whl", hash = "sha256:497bde6223c212ba11d462853cfa4f0ae6ef97465033e7dc9940cdb3ab5b48e5", size = 53542, upload-time = "2026-01-26T02:46:08.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/81/4629d0aa32302ef7b2ec65c75a728cc5ff4fa410c50096174c1632e70b3e/multidict-6.7.1-cp314-cp314t-win_arm64.whl", hash = "sha256:2bbd113e0d4af5db41d5ebfe9ccaff89de2120578164f86a5d17d5a576d1e5b2", size = 44719, upload-time = "2026-01-26T02:46:11.146Z" },
    { url = "https://files.pythonhosted.org/packages/81/08/7036c080d7117f28a4af526d794aab6a84463126db031b007717c1a6676e/multidict-6.7.1-py3-none-any.whl", hash = "sha256:55d97cc6dae627efa6a6e548885712d4864b81110ac76fa4e534c03819fa4a56", size = 12319, upload-time = "2026-01-26T02:46:44.004Z" },
]

[[package]]
name = "mutagen"
version = "1.47.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/81/e6/64bc71b74eef4b68e61eb921dcf72dabd9e4ec4af1e11891bbd312ccbb77/mutagen-1.47.0.tar.gz", hash = "sha256:719fadef0a978c31b4cf3c956261b3c58b6948b32023078a2117b1de09f0fc99", size = 1274186, upload-time = "2023-09-03T16:33:33.411Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b0/7a/620f945b96be1f6ee357d211d5bf74ab1b7fe72a9f1525aafbfe3aee6875/mutagen-1.47.0-py3-none-any.whl", hash = "sha256:edd96f50c5907a9539d8e5bba7245f62c9f520aef333d13392a79a4f70aca719", size = 194391, upload-time = "2023-09-03T16:33:29.955Z" },
]

[[package]]
name = "platformdirs"
version = "4.9.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/19/56/8d4c30c8a1d07013911a8fdbd8f89440ef9f08d07a1b50ab8ca8be5a20f9/platformdirs-4.9.4.tar.gz", hash = "sha256:1ec356301b7dc906d83f371c8f487070e99d3ccf9e501686456394622a01a934", size = 28737, upload-time = "2026-03-05T18:34:13.271Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/63/d7/97f7e3a6abb67d8080dd406fd4df842c2be0efaf712d1c899c32a075027c/platformdirs-4.9.4-py3-none-any.whl", hash = "sha256:68a9a4619a666ea6439f2ff250c12a853cd1cbd5158d258bd824a7df6be2f868", size = 21216, upload-time = "2026-03-05T18:34:12.172Z" },
]

[[package]]
name = "propcache"
version = "0.4.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/9e/da/e9fc233cf63743258bff22b3dfa7ea5baef7b5bc324af47a0ad89b8ffc6f/propcache-0.4.1.tar.gz", hash = "sha256:f48107a8c637e80362555f37ecf49abe20370e557cc4ab374f04ec4423c97c3d", size = 46442, upload-time = "2025-10-08T19:49:02.291Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/bf/df/6d9c1b6ac12b003837dde8a10231a7344512186e87b36e855bef32241942/propcache-0.4.1-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:43eedf29202c08550aac1d14e0ee619b0430aaef78f85864c1a892294fbc28cf", size = 77750, upload-time = "2025-10-08T19:47:07.648Z" },
    { url = "https://files.pythonhosted.org/packages/8b/e8/677a0025e8a2acf07d3418a2e7ba529c9c33caf09d3c1f25513023c1db56/propcache-0.4.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:d62cdfcfd89ccb8de04e0eda998535c406bf5e060ffd56be6c586cbcc05b3311", size = 44780, upload-time = "2025-10-08T19:47:08.851Z" },
    { url = "https://files.pythonhosted.org/packages/89/a4/92380f7ca60f99ebae761936bc48a72a639e8a47b29050615eef757cb2a7/propcache-0.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:cae65ad55793da34db5f54e4029b89d3b9b9490d8abe1b4c7ab5d4b8ec7ebf74", size = 46308, upload-time = "2025-10-08T19:47:09.982Z" },
    { url = "https://files.pythonhosted.org/packages/2d/48/c5ac64dee5262044348d1d78a5f85dd1a57464a60d30daee946699963eb3/propcache-0.4.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:333ddb9031d2704a301ee3e506dc46b1fe5f294ec198ed6435ad5b6a085facfe", size = 208182, upload-time = "2025-10-08T19:47:11.319Z" },
    { url = "https://files.pythonhosted.org/packages/c6/0c/cd762dd011a9287389a6a3eb43aa30207bde253610cca06824aeabfe9653/propcache-0.4.1-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:fd0858c20f078a32cf55f7e81473d96dcf3b93fd2ccdb3d40fdf54b8573df3af", size = 211215, upload-time = "2025-10-08T19:47:13.146Z" },
    { url = "https://files.pythonhosted.org/packages/30/3e/49861e90233ba36890ae0ca4c660e95df565b2cd15d4a68556ab5865974e/propcache-0.4.1-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:678ae89ebc632c5c204c794f8dab2837c5f159aeb59e6ed0539500400577298c", size = 218112, upload-time = "2025-10-08T19:47:14.913Z" },
    { url = "https://files.pythonhosted.org/packages/f1/8b/544bc867e24e1bd48f3118cecd3b05c694e160a168478fa28770f22fd094/propcache-0.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d472aeb4fbf9865e0c6d622d7f4d54a4e101a89715d8904282bb5f9a2f476c3f", size = 204442, upload-time = "2025-10-08T19:47:16.277Z" },
    { url = "https://files.pythonhosted.org/packages/50/a6/4282772fd016a76d3e5c0df58380a5ea64900afd836cec2c2f662d1b9bb3/propcache-0.4.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:4d3df5fa7e36b3225954fba85589da77a0fe6a53e3976de39caf04a0db4c36f1", size = 199398, upload-time = "2025-10-08T19:47:17.962Z" },
    { url = "https://files.pythonhosted.org/packages/3e/ec/d8a7cd406ee1ddb705db2139f8a10a8a427100347bd698e7014351c7af09/propcache-0.4.1-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:ee17f18d2498f2673e432faaa71698032b0127ebf23ae5974eeaf806c279df24", size = 196920, upload-time = "2025-10-08T19:47:19.355Z" },
    { url = "https://files.pythonhosted.org/packages/f6/6c/f38ab64af3764f431e359f8baf9e0a21013e24329e8b85d2da32e8ed07ca/propcache-0.4.1-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:580e97762b950f993ae618e167e7be9256b8353c2dcd8b99ec100eb50f5286aa", size = 203748, upload-time = "2025-10-08T19:47:21.338Z" },
    { url = "https://files.pythonhosted.org/packages/d6/e3/fa846bd70f6534d647886621388f0a265254d30e3ce47e5c8e6e27dbf153/propcache-0.4.1-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:501d20b891688eb8e7aa903021f0b72d5a55db40ffaab27edefd1027caaafa61", size = 205877, upload-time = "2025-10-08T19:47:23.059Z" },
    { url = "https://files.pythonhosted.org/packages/e2/39/8163fc6f3133fea7b5f2827e8eba2029a0277ab2c5beee6c1db7b10fc23d/propcache-0.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:9a0bd56e5b100aef69bd8562b74b46254e7c8812918d3baa700c8a8009b0af66", size = 199437, upload-time = "2025-10-08T19:47:24.445Z" },
    { url = "https://files.pythonhosted.org/packages/93/89/caa9089970ca49c7c01662bd0eeedfe85494e863e8043565aeb6472ce8fe/propcache-0.4.1-cp313-cp313-win32.whl", hash = "sha256:bcc9aaa5d80322bc2fb24bb7accb4a30f81e90ab8d6ba187aec0744bc302ad81", size = 37586, upload-time = "2025-10-08T19:47:25.736Z" },
    { url = "https://files.pythonhosted.org/packages/f5/ab/f76ec3c3627c883215b5c8080debb4394ef5a7a29be811f786415fc1e6fd/propcache-0.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:381914df18634f5494334d201e98245c0596067504b9372d8cf93f4bb23e025e", size = 40790, upload-time = "2025-10-08T19:47:26.847Z" },
    { url = "https://files.pythonhosted.org/packages/59/1b/e71ae98235f8e2ba5004d8cb19765a74877abf189bc53fc0c80d799e56c3/propcache-0.4.1-cp313-cp313-win_arm64.whl", hash = "sha256:8873eb4460fd55333ea49b7d189749ecf6e55bf85080f11b1c4530ed3034cba1", size = 37158, upload-time = "2025-10-08T19:47:27.961Z" },
    { url = "https://files.pythonhosted.org/packages/83/ce/a31bbdfc24ee0dcbba458c8175ed26089cf109a55bbe7b7640ed2470cfe9/propcache-0.4.1-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:92d1935ee1f8d7442da9c0c4fa7ac20d07e94064184811b685f5c4fada64553b", size = 81451, upload-time = "2025-10-08T19:47:29.445Z" },
    { url = "https://files.pythonhosted.org/packages/25/9c/442a45a470a68456e710d96cacd3573ef26a1d0a60067e6a7d5e655621ed/propcache-0.4.1-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:473c61b39e1460d386479b9b2f337da492042447c9b685f28be4f74d3529e566", size = 46374, upload-time = "2025-10-08T19:47:30.579Z" },
    { url = "https://files.pythonhosted.org/packages/f4/bf/b1d5e21dbc3b2e889ea4327044fb16312a736d97640fb8b6aa3f9c7b3b65/propcache-0.4.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:c0ef0aaafc66fbd87842a3fe3902fd889825646bc21149eafe47be6072725835", size = 48396, upload-time = "2025-10-08T19:47:31.79Z" },
    { url = "https://files.pythonhosted.org/packages/f4/04/5b4c54a103d480e978d3c8a76073502b18db0c4bc17ab91b3cb5092ad949/propcache-0.4.1-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f95393b4d66bfae908c3ca8d169d5f79cd65636ae15b5e7a4f6e67af675adb0e", size = 275950, upload-time = "2025-10-08T19:47:33.481Z" },
    { url = "https://files.pythonhosted.org/packages/b4/c1/86f846827fb969c4b78b0af79bba1d1ea2156492e1b83dea8b8a6ae27395/propcache-0.4.1-cp313-cp313t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:c07fda85708bc48578467e85099645167a955ba093be0a2dcba962195676e859", size = 273856, upload-time = "2025-10-08T19:47:34.906Z" },
    { url = "https://files.pythonhosted.org/packages/36/1d/fc272a63c8d3bbad6878c336c7a7dea15e8f2d23a544bda43205dfa83ada/propcache-0.4.1-cp313-cp313t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:af223b406d6d000830c6f65f1e6431783fc3f713ba3e6cc8c024d5ee96170a4b", size = 280420, upload-time = "2025-10-08T19:47:36.338Z" },
    { url = "https://files.pythonhosted.org/packages/07/0c/01f2219d39f7e53d52e5173bcb09c976609ba30209912a0680adfb8c593a/propcache-0.4.1-cp313-cp313t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a78372c932c90ee474559c5ddfffd718238e8673c340dc21fe45c5b8b54559a0", size = 263254, upload-time = "2025-10-08T19:47:37.692Z" },
    { url = "https://files.pythonhosted.org/packages/2d/18/cd28081658ce597898f0c4d174d4d0f3c5b6d4dc27ffafeef835c95eb359/propcache-0.4.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:564d9f0d4d9509e1a870c920a89b2fec951b44bf5ba7d537a9e7c1ccec2c18af", size = 261205, upload-time = "2025-10-08T19:47:39.659Z" },
    { url = "https://files.pythonhosted.org/packages/7a/71/1f9e22eb8b8316701c2a19fa1f388c8a3185082607da8e406a803c9b954e/propcache-0.4.1-cp313-cp313t-musllinux_1_2_armv7l.whl", hash = "sha256:17612831fda0138059cc5546f4d12a2aacfb9e47068c06af35c400ba58ba7393", size = 247873, upload-time = "2025-10-08T19:47:41.084Z" },
    { url = "https://files.pythonhosted.org/packages/4a/65/3d4b61f36af2b4eddba9def857959f1016a51066b4f1ce348e0cf7881f58/propcache-0.4.1-cp313-cp313t-musllinux_1_2_ppc64le.whl", hash = "sha256:41a89040cb10bd345b3c1a873b2bf36413d48da1def52f268a055f7398514874", size = 262739, upload-time = "2025-10-08T19:47:42.51Z" },
    { url = "https://files.pythonhosted.org/packages/2a/42/26746ab087faa77c1c68079b228810436ccd9a5ce9ac85e2b7307195fd06/propcache-0.4.1-cp313-cp313t-musllinux_1_2_s390x.whl", hash = "sha256:e35b88984e7fa64aacecea39236cee32dd9bd8c55f57ba8a75cf2399553f9bd7", size = 263514, upload-time = "2025-10-08T19:47:43.927Z" },
    { url = "https://files.pythonhosted.org/packages/94/13/630690fe201f5502d2403dd3cfd451ed8858fe3c738ee88d095ad2ff407b/propcache-0.4.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:6f8b465489f927b0df505cbe26ffbeed4d6d8a2bbc61ce90eb074ff129ef0ab1", size = 257781, upload-time = "2025-10-08T19:47:45.448Z" },
    { url = "https://files.pythonhosted.org/packages/92/f7/1d4ec5841505f423469efbfc381d64b7b467438cd5a4bbcbb063f3b73d27/propcache-0.4.1-cp313-cp313t-win32.whl", hash = "sha256:2ad890caa1d928c7c2965b48f3a3815c853180831d0e5503d35cf00c472f4717", size = 41396, upload-time = "2025-10-08T19:47:47.202Z" },
    { url = "https://files.pythonhosted.org/packages/48/f0/615c30622316496d2cbbc29f5985f7777d3ada70f23370608c1d3e081c1f/propcache-0.4.1-cp313-cp313t-win_amd64.whl", hash = "sha256:f7ee0e597f495cf415bcbd3da3caa3bd7e816b74d0d52b8145954c5e6fd3ff37", size = 44897, upload-time = "2025-10-08T19:47:48.336Z" },
    { url = "https://files.pythonhosted.org/packages/fd/ca/6002e46eccbe0e33dcd4069ef32f7f1c9e243736e07adca37ae8c4830ec3/propcache-0.4.1-cp313-cp313t-win_arm64.whl", hash = "sha256:929d7cbe1f01bb7baffb33dc14eb5691c95831450a26354cd210a8155170c93a", size = 39789, upload-time = "2025-10-08T19:47:49.876Z" },
    { url = "https://files.pythonhosted.org/packages/8e/5c/bca52d654a896f831b8256683457ceddd490ec18d9ec50e97dfd8fc726a8/propcache-0.4.1-cp314-cp314-macosx_10_13_universal2.whl", hash = "sha256:3f7124c9d820ba5548d431afb4632301acf965db49e666aa21c305cbe8c6de12", size = 78152, upload-time = "2025-10-08T19:47:51.051Z" },
    { url = "https://files.pythonhosted.org/packages/65/9b/03b04e7d82a5f54fb16113d839f5ea1ede58a61e90edf515f6577c66fa8f/propcache-0.4.1-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:c0d4b719b7da33599dfe3b22d3db1ef789210a0597bc650b7cee9c77c2be8c5c", size = 44869, upload-time = "2025-10-08T19:47:52.594Z" },
    { url = "https://files.pythonhosted.org/packages/b2/fa/89a8ef0468d5833a23fff277b143d0573897cf75bd56670a6d28126c7d68/propcache-0.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:9f302f4783709a78240ebc311b793f123328716a60911d667e0c036bc5dcbded", size = 46596, upload-time = "2025-10-08T19:47:54.073Z" },
    { url = "https://files.pythonhosted.org/packages/86/bd/47816020d337f4a746edc42fe8d53669965138f39ee117414c7d7a340cfe/propcache-0.4.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c80ee5802e3fb9ea37938e7eecc307fb984837091d5fd262bb37238b1ae97641", size = 206981, upload-time = "2025-10-08T19:47:55.715Z" },
    { url = "https://files.pythonhosted.org/packages/df/f6/c5fa1357cc9748510ee55f37173eb31bfde6d94e98ccd9e6f033f2fc06e1/propcache-0.4.1-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:ed5a841e8bb29a55fb8159ed526b26adc5bdd7e8bd7bf793ce647cb08656cdf4", size = 211490, upload-time = "2025-10-08T19:47:57.499Z" },
    { url = "https://files.pythonhosted.org/packages/80/1e/e5889652a7c4a3846683401a48f0f2e5083ce0ec1a8a5221d8058fbd1adf/propcache-0.4.1-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:55c72fd6ea2da4c318e74ffdf93c4fe4e926051133657459131a95c846d16d44", size = 215371, upload-time = "2025-10-08T19:47:59.317Z" },
    { url = "https://files.pythonhosted.org/packages/b2/f2/889ad4b2408f72fe1a4f6a19491177b30ea7bf1a0fd5f17050ca08cfc882/propcache-0.4.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8326e144341460402713f91df60ade3c999d601e7eb5ff8f6f7862d54de0610d", size = 201424, upload-time = "2025-10-08T19:48:00.67Z" },
    { url = "https://files.pythonhosted.org/packages/27/73/033d63069b57b0812c8bd19f311faebeceb6ba31b8f32b73432d12a0b826/propcache-0.4.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:060b16ae65bc098da7f6d25bf359f1f31f688384858204fe5d652979e0015e5b", size = 197566, upload-time = "2025-10-08T19:48:02.604Z" },
    { url = "https://files.pythonhosted.org/packages/dc/89/ce24f3dc182630b4e07aa6d15f0ff4b14ed4b9955fae95a0b54c58d66c05/propcache-0.4.1-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:89eb3fa9524f7bec9de6e83cf3faed9d79bffa560672c118a96a171a6f55831e", size = 193130, upload-time = "2025-10-08T19:48:04.499Z" },
    { url = "https://files.pythonhosted.org/packages/a9/24/ef0d5fd1a811fb5c609278d0209c9f10c35f20581fcc16f818da959fc5b4/propcache-0.4.1-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:dee69d7015dc235f526fe80a9c90d65eb0039103fe565776250881731f06349f", size = 202625, upload-time = "2025-10-08T19:48:06.213Z" },
    { url = "https://files.pythonhosted.org/packages/f5/02/98ec20ff5546f68d673df2f7a69e8c0d076b5abd05ca882dc7ee3a83653d/propcache-0.4.1-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:5558992a00dfd54ccbc64a32726a3357ec93825a418a401f5cc67df0ac5d9e49", size = 204209, upload-time = "2025-10-08T19:48:08.432Z" },
    { url = "https://files.pythonhosted.org/packages/a0/87/492694f76759b15f0467a2a93ab68d32859672b646aa8a04ce4864e7932d/propcache-0.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:c9b822a577f560fbd9554812526831712c1436d2c046cedee4c3796d3543b144", size = 197797, upload-time = "2025-10-08T19:48:09.968Z" },
    { url = "https://files.pythonhosted.org/packages/ee/36/66367de3575db1d2d3f3d177432bd14ee577a39d3f5d1b3d5df8afe3b6e2/propcache-0.4.1-cp314-cp314-win32.whl", hash = "sha256:ab4c29b49d560fe48b696cdcb127dd36e0bc2472548f3bf56cc5cb3da2b2984f", size = 38140, upload-time = "2025-10-08T19:48:11.232Z" },
    { url = "https://files.pythonhosted.org/packages/0c/2a/a758b47de253636e1b8aef181c0b4f4f204bf0dd964914fb2af90a95b49b/propcache-0.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:5a103c3eb905fcea0ab98be99c3a9a5ab2de60228aa5aceedc614c0281cf6153", size = 41257, upload-time = "2025-10-08T19:48:12.707Z" },
    { url = "https://files.pythonhosted.org/packages/34/5e/63bd5896c3fec12edcbd6f12508d4890d23c265df28c74b175e1ef9f4f3b/propcache-0.4.1-cp314-cp314-win_arm64.whl", hash = "sha256:74c1fb26515153e482e00177a1ad654721bf9207da8a494a0c05e797ad27b992", size = 38097, upload-time = "2025-10-08T19:48:13.923Z" },
    { url = "https://files.pythonhosted.org/packages/99/85/9ff785d787ccf9bbb3f3106f79884a130951436f58392000231b4c737c80/propcache-0.4.1-cp314-cp314t-macosx_10_13_universal2.whl", hash = "sha256:824e908bce90fb2743bd6b59db36eb4f45cd350a39637c9f73b1c1ea66f5b75f", size = 81455, upload-time = "2025-10-08T19:48:15.16Z" },
    { url = "https://files.pythonhosted.org/packages/90/85/2431c10c8e7ddb1445c1f7c4b54d886e8ad20e3c6307e7218f05922cad67/propcache-0.4.1-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:c2b5e7db5328427c57c8e8831abda175421b709672f6cfc3d630c3b7e2146393", size = 46372, upload-time = "2025-10-08T19:48:16.424Z" },
    { url = "https://files.pythonhosted.org/packages/01/20/b0972d902472da9bcb683fa595099911f4d2e86e5683bcc45de60dd05dc3/propcache-0.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:6f6ff873ed40292cd4969ef5310179afd5db59fdf055897e282485043fc80ad0", size = 48411, upload-time = "2025-10-08T19:48:17.577Z" },
    { url = "https://files.pythonhosted.org/packages/e2/e3/7dc89f4f21e8f99bad3d5ddb3a3389afcf9da4ac69e3deb2dcdc96e74169/propcache-0.4.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:49a2dc67c154db2c1463013594c458881a069fcf98940e61a0569016a583020a", size = 275712, upload-time = "2025-10-08T19:48:18.901Z" },
    { url = "https://files.pythonhosted.org/packages/20/67/89800c8352489b21a8047c773067644e3897f02ecbbd610f4d46b7f08612/propcache-0.4.1-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:005f08e6a0529984491e37d8dbc3dd86f84bd78a8ceb5fa9a021f4c48d4984be", size = 273557, upload-time = "2025-10-08T19:48:20.762Z" },
    { url = "https://files.pythonhosted.org/packages/e2/a1/b52b055c766a54ce6d9c16d9aca0cad8059acd9637cdf8aa0222f4a026ef/propcache-0.4.1-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5c3310452e0d31390da9035c348633b43d7e7feb2e37be252be6da45abd1abcc", size = 280015, upload-time = "2025-10-08T19:48:22.592Z" },
    { url = "https://files.pythonhosted.org/packages/48/c8/33cee30bd890672c63743049f3c9e4be087e6780906bfc3ec58528be59c1/propcache-0.4.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4c3c70630930447f9ef1caac7728c8ad1c56bc5015338b20fed0d08ea2480b3a", size = 262880, upload-time = "2025-10-08T19:48:23.947Z" },
    { url = "https://files.pythonhosted.org/packages/0c/b1/8f08a143b204b418285c88b83d00edbd61afbc2c6415ffafc8905da7038b/propcache-0.4.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:8e57061305815dfc910a3634dcf584f08168a8836e6999983569f51a8544cd89", size = 260938, upload-time = "2025-10-08T19:48:25.656Z" },
    { url = "https://files.pythonhosted.org/packages/cf/12/96e4664c82ca2f31e1c8dff86afb867348979eb78d3cb8546a680287a1e9/propcache-0.4.1-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:521a463429ef54143092c11a77e04056dd00636f72e8c45b70aaa3140d639726", size = 247641, upload-time = "2025-10-08T19:48:27.207Z" },
    { url = "https://files.pythonhosted.org/packages/18/ed/e7a9cfca28133386ba52278136d42209d3125db08d0a6395f0cba0c0285c/propcache-0.4.1-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:120c964da3fdc75e3731aa392527136d4ad35868cc556fd09bb6d09172d9a367", size = 262510, upload-time = "2025-10-08T19:48:28.65Z" },
    { url = "https://files.pythonhosted.org/packages/f5/76/16d8bf65e8845dd62b4e2b57444ab81f07f40caa5652b8969b87ddcf2ef6/propcache-0.4.1-cp314-cp314t-musllinux_1_2_s390x.whl", hash = "sha256:d8f353eb14ee3441ee844ade4277d560cdd68288838673273b978e3d6d2c8f36", size = 263161, upload-time = "2025-10-08T19:48:30.133Z" },
    { url = "https://files.pythonhosted.org/packages/e7/70/c99e9edb5d91d5ad8a49fa3c1e8285ba64f1476782fed10ab251ff413ba1/propcache-0.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:ab2943be7c652f09638800905ee1bab2c544e537edb57d527997a24c13dc1455", size = 257393, upload-time = "2025-10-08T19:48:31.567Z" },
    { url = "https://files.pythonhosted.org/packages/08/02/87b25304249a35c0915d236575bc3574a323f60b47939a2262b77632a3ee/propcache-0.4.1-cp314-cp314t-win32.whl", hash = "sha256:05674a162469f31358c30bcaa8883cb7829fa3110bf9c0991fe27d7896c42d85", size = 42546, upload-time = "2025-10-08T19:48:32.872Z" },
    { url = "https://files.pythonhosted.org/packages/cb/ef/3c6ecf8b317aa982f309835e8f96987466123c6e596646d4e6a1dfcd080f/propcache-0.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:990f6b3e2a27d683cb7602ed6c86f15ee6b43b1194736f9baaeb93d0016633b1", size = 46259, upload-time = "2025-10-08T19:48:34.226Z" },
    { url = "https://files.pythonhosted.org/packages/c4/2d/346e946d4951f37eca1e4f55be0f0174c52cd70720f84029b02f296f4a38/propcache-0.4.1-cp314-cp314t-win_arm64.whl", hash = "sha256:ecef2343af4cc68e05131e45024ba34f6095821988a9d0a02aa7c73fcc448aa9", size = 40428, upload-time = "2025-10-08T19:48:35.441Z" },
    { url = "https://files.pythonhosted.org/packages/5b/5a/bc7b4a4ef808fa59a816c17b20c4bef6884daebbdf627ff2a161da67da19/propcache-0.4.1-py3-none-any.whl", hash = "sha256:af2a6052aeb6cf17d3e46ee169099044fd8224cbaf75c76a2ef596e8163e2237", size = 13305, upload-time = "2025-10-08T19:49:00.792Z" },
]

[[package]]
name = "pycparser"
version = "3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1b/7d/92392ff7815c21062bea51aa7b87d45576f649f16458d78b7cf94b9ab2e6/pycparser-3.0.tar.gz", hash = "sha256:600f49d217304a5902ac3c37e1281c9fe94e4d0489de643a9504c5cdfdfc6b29", size = 103492, upload-time = "2026-01-21T14:26:51.89Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0c/c3/44f3fbbfa403ea2a7c779186dc20772604442dde72947e7d01069cbe98e3/pycparser-3.0-py3-none-any.whl", hash = "sha256:b727414169a36b7d524c1c3e31839a521725078d7b2ff038656844266160a992", size = 48172, upload-time = "2026-01-21T14:26:50.693Z" },
]

[[package]]
name = "pycryptodomex"
version = "3.23.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c9/85/e24bf90972a30b0fcd16c73009add1d7d7cd9140c2498a68252028899e41/pycryptodomex-3.23.0.tar.gz", hash = "sha256:71909758f010c82bc99b0abf4ea12012c98962fbf0583c2164f8b84533c2e4da", size = 4922157, upload-time = "2025-05-17T17:23:41.434Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2e/00/10edb04777069a42490a38c137099d4b17ba6e36a4e6e28bdc7470e9e853/pycryptodomex-3.23.0-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:7b37e08e3871efe2187bc1fd9320cc81d87caf19816c648f24443483005ff886", size = 2498764, upload-time = "2025-05-17T17:22:21.453Z" },
    { url = "https://files.pythonhosted.org/packages/6b/3f/2872a9c2d3a27eac094f9ceaa5a8a483b774ae69018040ea3240d5b11154/pycryptodomex-3.23.0-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:91979028227543010d7b2ba2471cf1d1e398b3f183cb105ac584df0c36dac28d", size = 1643012, upload-time = "2025-05-17T17:22:23.702Z" },
    { url = "https://files.pythonhosted.org/packages/70/af/774c2e2b4f6570fbf6a4972161adbb183aeeaa1863bde31e8706f123bf92/pycryptodomex-3.23.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:6b8962204c47464d5c1c4038abeadd4514a133b28748bcd9fa5b6d62e3cec6fa", size = 2187643, upload-time = "2025-05-17T17:22:26.37Z" },
    { url = "https://files.pythonhosted.org/packages/de/a3/71065b24cb889d537954cedc3ae5466af00a2cabcff8e29b73be047e9a19/pycryptodomex-3.23.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a33986a0066860f7fcf7c7bd2bc804fa90e434183645595ae7b33d01f3c91ed8", size = 2273762, upload-time = "2025-05-17T17:22:28.313Z" },
    { url = "https://files.pythonhosted.org/packages/c9/0b/ff6f43b7fbef4d302c8b981fe58467b8871902cdc3eb28896b52421422cc/pycryptodomex-3.23.0-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c7947ab8d589e3178da3d7cdeabe14f841b391e17046954f2fbcd941705762b5", size = 2313012, upload-time = "2025-05-17T17:22:30.57Z" },
    { url = "https://files.pythonhosted.org/packages/02/de/9d4772c0506ab6da10b41159493657105d3f8bb5c53615d19452afc6b315/pycryptodomex-3.23.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:c25e30a20e1b426e1f0fa00131c516f16e474204eee1139d1603e132acffc314", size = 2186856, upload-time = "2025-05-17T17:22:32.819Z" },
    { url = "https://files.pythonhosted.org/packages/28/ad/8b30efcd6341707a234e5eba5493700a17852ca1ac7a75daa7945fcf6427/pycryptodomex-3.23.0-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:da4fa650cef02db88c2b98acc5434461e027dce0ae8c22dd5a69013eaf510006", size = 2347523, upload-time = "2025-05-17T17:22:35.386Z" },
    { url = "https://files.pythonhosted.org/packages/0f/02/16868e9f655b7670dbb0ac4f2844145cbc42251f916fc35c414ad2359849/pycryptodomex-3.23.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:58b851b9effd0d072d4ca2e4542bf2a4abcf13c82a29fd2c93ce27ee2a2e9462", size = 2272825, upload-time = "2025-05-17T17:22:37.632Z" },
    { url = "https://files.pythonhosted.org/packages/ca/18/4ca89ac737230b52ac8ffaca42f9c6f1fd07c81a6cd821e91af79db60632/pycryptodomex-3.23.0-cp313-cp313t-win32.whl", hash = "sha256:a9d446e844f08299236780f2efa9898c818fe7e02f17263866b8550c7d5fb328", size = 1772078, upload-time = "2025-05-17T17:22:40Z" },
    { url = "https://files.pythonhosted.org/packages/73/34/13e01c322db027682e00986873eca803f11c56ade9ba5bbf3225841ea2d4/pycryptodomex-3.23.0-cp313-cp313t-win_amd64.whl", hash = "sha256:bc65bdd9fc8de7a35a74cab1c898cab391a4add33a8fe740bda00f5976ca4708", size = 1803656, upload-time = "2025-05-17T17:22:42.139Z" },
    { url = "https://files.pythonhosted.org/packages/54/68/9504c8796b1805d58f4425002bcca20f12880e6fa4dc2fc9a668705c7a08/pycryptodomex-3.23.0-cp313-cp313t-win_arm64.whl", hash = "sha256:c885da45e70139464f082018ac527fdaad26f1657a99ee13eecdce0f0ca24ab4", size = 1707172, upload-time = "2025-05-17T17:22:44.704Z" },
    { url = "https://files.pythonhosted.org/packages/dd/9c/1a8f35daa39784ed8adf93a694e7e5dc15c23c741bbda06e1d45f8979e9e/pycryptodomex-3.23.0-cp37-abi3-macosx_10_9_universal2.whl", hash = "sha256:06698f957fe1ab229a99ba2defeeae1c09af185baa909a31a5d1f9d42b1aaed6", size = 2499240, upload-time = "2025-05-17T17:22:46.953Z" },
    { url = "https://files.pythonhosted.org/packages/7a/62/f5221a191a97157d240cf6643747558759126c76ee92f29a3f4aee3197a5/pycryptodomex-3.23.0-cp37-abi3-macosx_10_9_x86_64.whl", hash = "sha256:b2c2537863eccef2d41061e82a881dcabb04944c5c06c5aa7110b577cc487545", size = 1644042, upload-time = "2025-05-17T17:22:49.098Z" },
    { url = "https://files.pythonhosted.org/packages/8c/fd/5a054543c8988d4ed7b612721d7e78a4b9bf36bc3c5ad45ef45c22d0060e/pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:43c446e2ba8df8889e0e16f02211c25b4934898384c1ec1ec04d7889c0333587", size = 2186227, upload-time = "2025-05-17T17:22:51.139Z" },
    { url = "https://files.pythonhosted.org/packages/c8/a9/8862616a85cf450d2822dbd4fff1fcaba90877907a6ff5bc2672cafe42f8/pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f489c4765093fb60e2edafdf223397bc716491b2b69fe74367b70d6999257a5c", size = 2272578, upload-time = "2025-05-17T17:22:53.676Z" },
    { url = "https://files.pythonhosted.org/packages/46/9f/bda9c49a7c1842820de674ab36c79f4fbeeee03f8ff0e4f3546c3889076b/pycryptodomex-3.23.0-cp37-abi3-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:bdc69d0d3d989a1029df0eed67cc5e8e5d968f3724f4519bd03e0ec68df7543c", size = 2312166, upload-time = "2025-05-17T17:22:56.585Z" },
    { url = "https://files.pythonhosted.org/packages/03/cc/870b9bf8ca92866ca0186534801cf8d20554ad2a76ca959538041b7a7cf4/pycryptodomex-3.23.0-cp37-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:6bbcb1dd0f646484939e142462d9e532482bc74475cecf9c4903d4e1cd21f003", size = 2185467, upload-time = "2025-05-17T17:22:59.237Z" },
    { url = "https://files.pythonhosted.org/packages/96/e3/ce9348236d8e669fea5dd82a90e86be48b9c341210f44e25443162aba187/pycryptodomex-3.23.0-cp37-abi3-musllinux_1_2_i686.whl", hash = "sha256:8a4fcd42ccb04c31268d1efeecfccfd1249612b4de6374205376b8f280321744", size = 2346104, upload-time = "2025-05-17T17:23:02.112Z" },
    { url = "https://files.pythonhosted.org/packages/a5/e9/e869bcee87beb89040263c416a8a50204f7f7a83ac11897646c9e71e0daf/pycryptodomex-3.23.0-cp37-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:55ccbe27f049743a4caf4f4221b166560d3438d0b1e5ab929e07ae1702a4d6fd", size = 2271038, upload-time = "2025-05-17T17:23:04.872Z" },
    { url = "https://files.pythonhosted.org/packages/8d/67/09ee8500dd22614af5fbaa51a4aee6e342b5fa8aecf0a6cb9cbf52fa6d45/pycryptodomex-3.23.0-cp37-abi3-win32.whl", hash = "sha256:189afbc87f0b9f158386bf051f720e20fa6145975f1e76369303d0f31d1a8d7c", size = 1771969, upload-time = "2025-05-17T17:23:07.115Z" },
    { url = "https://files.pythonhosted.org/packages/69/96/11f36f71a865dd6df03716d33bd07a67e9d20f6b8d39820470b766af323c/pycryptodomex-3.23.0-cp37-abi3-win_amd64.whl", hash = "sha256:52e5ca58c3a0b0bd5e100a9fbc8015059b05cffc6c66ce9d98b4b45e023443b9", size = 1803124, upload-time = "2025-05-17T17:23:09.267Z" },
    { url = "https://files.pythonhosted.org/packages/f9/93/45c1cdcbeb182ccd2e144c693eaa097763b08b38cded279f0053ed53c553/pycryptodomex-3.23.0-cp37-abi3-win_arm64.whl", hash = "sha256:02d87b80778c171445d67e23d1caef279bf4b25c3597050ccd2e13970b57fd51", size = 1707161, upload-time = "2025-05-17T17:23:11.414Z" },
]

[[package]]
name = "pylint"
version = "4.0.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "astroid" },
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "dill" },
    { name = "isort" },
    { name = "mccabe" },
    { name = "platformdirs" },
    { name = "tomlkit" },
]
sdist = { url = "https://files.pythonhosted.org/packages/e4/b6/74d9a8a68b8067efce8d07707fe6a236324ee1e7808d2eb3646ec8517c7d/pylint-4.0.5.tar.gz", hash = "sha256:8cd6a618df75deb013bd7eb98327a95f02a6fb839205a6bbf5456ef96afb317c", size = 1572474, upload-time = "2026-02-20T09:07:33.621Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d5/6f/9ac2548e290764781f9e7e2aaf0685b086379dabfb29ca38536985471eaf/pylint-4.0.5-py3-none-any.whl", hash = "sha256:00f51c9b14a3b3ae08cff6b2cdd43f28165c78b165b628692e428fb1f8dc2cf2", size = 536694, upload-time = "2026-02-20T09:07:31.028Z" },
]

[[package]]
name = "python-engineio"
version = "4.13.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "simple-websocket" },
]
sdist = { url = "https://files.pythonhosted.org/packages/34/12/bdef9dbeedbe2cdeba2a2056ad27b1fb081557d34b69a97f574843462cae/python_engineio-4.13.1.tar.gz", hash = "sha256:0a853fcef52f5b345425d8c2b921ac85023a04dfcf75d7b74696c61e940fd066", size = 92348, upload-time = "2026-02-06T23:38:06.12Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/aa/54/0cce26da03a981f949bb8449c9778537f75f5917c172e1d2992ff25cb57d/python_engineio-4.13.1-py3-none-any.whl", hash = "sha256:f32ad10589859c11053ad7d9bb3c9695cdf862113bfb0d20bc4d890198287399", size = 59847, upload-time = "2026-02-06T23:38:04.861Z" },
]

[[package]]
name = "python-socketio"
version = "5.16.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "bidict" },
    { name = "python-engineio" },
]
sdist = { url = "https://files.pythonhosted.org/packages/59/81/cf8284f45e32efa18d3848ed82cdd4dcc1b657b082458fbe01ad3e1f2f8d/python_socketio-5.16.1.tar.gz", hash = "sha256:f863f98eacce81ceea2e742f6388e10ca3cdd0764be21d30d5196470edf5ea89", size = 128508, upload-time = "2026-02-06T23:42:07Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/07/c7/deb8c5e604404dbf10a3808a858946ca3547692ff6316b698945bb72177e/python_socketio-5.16.1-py3-none-any.whl", hash = "sha256:a3eb1702e92aa2f2b5d3ba00261b61f062cce51f1cfb6900bf3ab4d1934d2d35", size = 82054, upload-time = "2026-02-06T23:42:05.772Z" },
]

[[package]]
name = "requests"
version = "2.32.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c9/74/b3ff8e6c8446842c3f5c837e9c3dfcfe2018ea6ecef224c710c85ef728f4/requests-2.32.5.tar.gz", hash = "sha256:dbba0bac56e100853db0ea71b82b4dfd5fe2bf6d3754a8893c3af500cec7d7cf", size = 134517, upload-time = "2025-08-18T20:46:02.573Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1e/db/4254e3eabe8020b458f1a747140d32277ec7a271daf1d235b70dc0b4e6e3/requests-2.32.5-py3-none-any.whl", hash = "sha256:2462f94637a34fd532264295e186976db0f5d453d1cdd31473c85a6a161affb6", size = 64738, upload-time = "2025-08-18T20:46:00.542Z" },
]

[[package]]
name = "simple-websocket"
version = "1.1.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "wsproto" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b0/d4/bfa032f961103eba93de583b161f0e6a5b63cebb8f2c7d0c6e6efe1e3d2e/simple_websocket-1.1.0.tar.gz", hash = "sha256:7939234e7aa067c534abdab3a9ed933ec9ce4691b0713c78acb195560aa52ae4", size = 17300, upload-time = "2024-10-10T22:39:31.412Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/52/59/0782e51887ac6b07ffd1570e0364cf901ebc36345fea669969d2084baebb/simple_websocket-1.1.0-py3-none-any.whl", hash = "sha256:4af6069630a38ed6c561010f0e11a5bc0d4ca569b36306eb257cd9a192497c8c", size = 13842, upload-time = "2024-10-10T22:39:29.645Z" },
]

[[package]]
name = "tomlkit"
version = "0.14.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c3/af/14b24e41977adb296d6bd1fb59402cf7d60ce364f90c890bd2ec65c43b5a/tomlkit-0.14.0.tar.gz", hash = "sha256:cf00efca415dbd57575befb1f6634c4f42d2d87dbba376128adb42c121b87064", size = 187167, upload-time = "2026-01-13T01:14:53.304Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b5/11/87d6d29fb5d237229d67973a6c9e06e048f01cf4994dee194ab0ea841814/tomlkit-0.14.0-py3-none-any.whl", hash = "sha256:592064ed85b40fa213469f81ac584f67a4f2992509a7c3ea2d632208623a3680", size = 39310, upload-time = "2026-01-13T01:14:51.965Z" },
]

[[package]]
name = "urllib3"
version = "2.6.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/24/5f1b3bdffd70275f6661c76461e25f024d5a38a46f04aaca912426a2b1d3/urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed", size = 435556, upload-time = "2026-01-07T16:24:43.925Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/39/08/aaaad47bc4e9dc8c725e68f9d04865dbcb2052843ff09c97b08904852d84/urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4", size = 131584, upload-time = "2026-01-07T16:24:42.685Z" },
]

[[package]]
name = "watchfiles"
version = "1.1.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c2/c9/8869df9b2a2d6c59d79220a4db37679e74f807c559ffe5265e08b227a210/watchfiles-1.1.1.tar.gz", hash = "sha256:a173cb5c16c4f40ab19cecf48a534c409f7ea983ab8fed0741304a1c0a31b3f2", size = 94440, upload-time = "2025-10-14T15:06:21.08Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/bb/f4/f750b29225fe77139f7ae5de89d4949f5a99f934c65a1f1c0b248f26f747/watchfiles-1.1.1-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:130e4876309e8686a5e37dba7d5e9bc77e6ed908266996ca26572437a5271e18", size = 404321, upload-time = "2025-10-14T15:05:02.063Z" },
    { url = "https://files.pythonhosted.org/packages/2b/f9/f07a295cde762644aa4c4bb0f88921d2d141af45e735b965fb2e87858328/watchfiles-1.1.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:5f3bde70f157f84ece3765b42b4a52c6ac1a50334903c6eaf765362f6ccca88a", size = 391783, upload-time = "2025-10-14T15:05:03.052Z" },
    { url = "https://files.pythonhosted.org/packages/bc/11/fc2502457e0bea39a5c958d86d2cb69e407a4d00b85735ca724bfa6e0d1a/watchfiles-1.1.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:14e0b1fe858430fc0251737ef3824c54027bedb8c37c38114488b8e131cf8219", size = 449279, upload-time = "2025-10-14T15:05:04.004Z" },
    { url = "https://files.pythonhosted.org/packages/e3/1f/d66bc15ea0b728df3ed96a539c777acfcad0eb78555ad9efcaa1274688f0/watchfiles-1.1.1-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:f27db948078f3823a6bb3b465180db8ebecf26dd5dae6f6180bd87383b6b4428", size = 459405, upload-time = "2025-10-14T15:05:04.942Z" },
    { url = "https://files.pythonhosted.org/packages/be/90/9f4a65c0aec3ccf032703e6db02d89a157462fbb2cf20dd415128251cac0/watchfiles-1.1.1-cp313-cp313-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:059098c3a429f62fc98e8ec62b982230ef2c8df68c79e826e37b895bc359a9c0", size = 488976, upload-time = "2025-10-14T15:05:05.905Z" },
    { url = "https://files.pythonhosted.org/packages/37/57/ee347af605d867f712be7029bb94c8c071732a4b44792e3176fa3c612d39/watchfiles-1.1.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:bfb5862016acc9b869bb57284e6cb35fdf8e22fe59f7548858e2f971d045f150", size = 595506, upload-time = "2025-10-14T15:05:06.906Z" },
    { url = "https://files.pythonhosted.org/packages/a8/78/cc5ab0b86c122047f75e8fc471c67a04dee395daf847d3e59381996c8707/watchfiles-1.1.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:319b27255aacd9923b8a276bb14d21a5f7ff82564c744235fc5eae58d95422ae", size = 474936, upload-time = "2025-10-14T15:05:07.906Z" },
    { url = "https://files.pythonhosted.org/packages/62/da/def65b170a3815af7bd40a3e7010bf6ab53089ef1b75d05dd5385b87cf08/watchfiles-1.1.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c755367e51db90e75b19454b680903631d41f9e3607fbd941d296a020c2d752d", size = 456147, upload-time = "2025-10-14T15:05:09.138Z" },
    { url = "https://files.pythonhosted.org/packages/57/99/da6573ba71166e82d288d4df0839128004c67d2778d3b566c138695f5c0b/watchfiles-1.1.1-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:c22c776292a23bfc7237a98f791b9ad3144b02116ff10d820829ce62dff46d0b", size = 630007, upload-time = "2025-10-14T15:05:10.117Z" },
    { url = "https://files.pythonhosted.org/packages/a8/51/7439c4dd39511368849eb1e53279cd3454b4a4dbace80bab88feeb83c6b5/watchfiles-1.1.1-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:3a476189be23c3686bc2f4321dd501cb329c0a0469e77b7b534ee10129ae6374", size = 622280, upload-time = "2025-10-14T15:05:11.146Z" },
    { url = "https://files.pythonhosted.org/packages/95/9c/8ed97d4bba5db6fdcdb2b298d3898f2dd5c20f6b73aee04eabe56c59677e/watchfiles-1.1.1-cp313-cp313-win32.whl", hash = "sha256:bf0a91bfb5574a2f7fc223cf95eeea79abfefa404bf1ea5e339c0c1560ae99a0", size = 272056, upload-time = "2025-10-14T15:05:12.156Z" },
    { url = "https://files.pythonhosted.org/packages/1f/f3/c14e28429f744a260d8ceae18bf58c1d5fa56b50d006a7a9f80e1882cb0d/watchfiles-1.1.1-cp313-cp313-win_amd64.whl", hash = "sha256:52e06553899e11e8074503c8e716d574adeeb7e68913115c4b3653c53f9bae42", size = 288162, upload-time = "2025-10-14T15:05:13.208Z" },
    { url = "https://files.pythonhosted.org/packages/dc/61/fe0e56c40d5cd29523e398d31153218718c5786b5e636d9ae8ae79453d27/watchfiles-1.1.1-cp313-cp313-win_arm64.whl", hash = "sha256:ac3cc5759570cd02662b15fbcd9d917f7ecd47efe0d6b40474eafd246f91ea18", size = 277909, upload-time = "2025-10-14T15:05:14.49Z" },
    { url = "https://files.pythonhosted.org/packages/79/42/e0a7d749626f1e28c7108a99fb9bf524b501bbbeb9b261ceecde644d5a07/watchfiles-1.1.1-cp313-cp313t-macosx_10_12_x86_64.whl", hash = "sha256:563b116874a9a7ce6f96f87cd0b94f7faf92d08d0021e837796f0a14318ef8da", size = 403389, upload-time = "2025-10-14T15:05:15.777Z" },
    { url = "https://files.pythonhosted.org/packages/15/49/08732f90ce0fbbc13913f9f215c689cfc9ced345fb1bcd8829a50007cc8d/watchfiles-1.1.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:3ad9fe1dae4ab4212d8c91e80b832425e24f421703b5a42ef2e4a1e215aff051", size = 389964, upload-time = "2025-10-14T15:05:16.85Z" },
    { url = "https://files.pythonhosted.org/packages/27/0d/7c315d4bd5f2538910491a0393c56bf70d333d51bc5b34bee8e68e8cea19/watchfiles-1.1.1-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ce70f96a46b894b36eba678f153f052967a0d06d5b5a19b336ab0dbbd029f73e", size = 448114, upload-time = "2025-10-14T15:05:17.876Z" },
    { url = "https://files.pythonhosted.org/packages/c3/24/9e096de47a4d11bc4df41e9d1e61776393eac4cb6eb11b3e23315b78b2cc/watchfiles-1.1.1-cp313-cp313t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:cb467c999c2eff23a6417e58d75e5828716f42ed8289fe6b77a7e5a91036ca70", size = 460264, upload-time = "2025-10-14T15:05:18.962Z" },
    { url = "https://files.pythonhosted.org/packages/cc/0f/e8dea6375f1d3ba5fcb0b3583e2b493e77379834c74fd5a22d66d85d6540/watchfiles-1.1.1-cp313-cp313t-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:836398932192dae4146c8f6f737d74baeac8b70ce14831a239bdb1ca882fc261", size = 487877, upload-time = "2025-10-14T15:05:20.094Z" },
    { url = "https://files.pythonhosted.org/packages/ac/5b/df24cfc6424a12deb41503b64d42fbea6b8cb357ec62ca84a5a3476f654a/watchfiles-1.1.1-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:743185e7372b7bc7c389e1badcc606931a827112fbbd37f14c537320fca08620", size = 595176, upload-time = "2025-10-14T15:05:21.134Z" },
    { url = "https://files.pythonhosted.org/packages/8f/b5/853b6757f7347de4e9b37e8cc3289283fb983cba1ab4d2d7144694871d9c/watchfiles-1.1.1-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:afaeff7696e0ad9f02cbb8f56365ff4686ab205fcf9c4c5b6fdfaaa16549dd04", size = 473577, upload-time = "2025-10-14T15:05:22.306Z" },
    { url = "https://files.pythonhosted.org/packages/e1/f7/0a4467be0a56e80447c8529c9fce5b38eab4f513cb3d9bf82e7392a5696b/watchfiles-1.1.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3f7eb7da0eb23aa2ba036d4f616d46906013a68caf61b7fdbe42fc8b25132e77", size = 455425, upload-time = "2025-10-14T15:05:23.348Z" },
    { url = "https://files.pythonhosted.org/packages/8e/e0/82583485ea00137ddf69bc84a2db88bd92ab4a6e3c405e5fb878ead8d0e7/watchfiles-1.1.1-cp313-cp313t-musllinux_1_1_aarch64.whl", hash = "sha256:831a62658609f0e5c64178211c942ace999517f5770fe9436be4c2faeba0c0ef", size = 628826, upload-time = "2025-10-14T15:05:24.398Z" },
    { url = "https://files.pythonhosted.org/packages/28/9a/a785356fccf9fae84c0cc90570f11702ae9571036fb25932f1242c82191c/watchfiles-1.1.1-cp313-cp313t-musllinux_1_1_x86_64.whl", hash = "sha256:f9a2ae5c91cecc9edd47e041a930490c31c3afb1f5e6d71de3dc671bfaca02bf", size = 622208, upload-time = "2025-10-14T15:05:25.45Z" },
    { url = "https://files.pythonhosted.org/packages/c3/f4/0872229324ef69b2c3edec35e84bd57a1289e7d3fe74588048ed8947a323/watchfiles-1.1.1-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:d1715143123baeeaeadec0528bb7441103979a1d5f6fd0e1f915383fea7ea6d5", size = 404315, upload-time = "2025-10-14T15:05:26.501Z" },
    { url = "https://files.pythonhosted.org/packages/7b/22/16d5331eaed1cb107b873f6ae1b69e9ced582fcf0c59a50cd84f403b1c32/watchfiles-1.1.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:39574d6370c4579d7f5d0ad940ce5b20db0e4117444e39b6d8f99db5676c52fd", size = 390869, upload-time = "2025-10-14T15:05:27.649Z" },
    { url = "https://files.pythonhosted.org/packages/b2/7e/5643bfff5acb6539b18483128fdc0ef2cccc94a5b8fbda130c823e8ed636/watchfiles-1.1.1-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:7365b92c2e69ee952902e8f70f3ba6360d0d596d9299d55d7d386df84b6941fb", size = 449919, upload-time = "2025-10-14T15:05:28.701Z" },
    { url = "https://files.pythonhosted.org/packages/51/2e/c410993ba5025a9f9357c376f48976ef0e1b1aefb73b97a5ae01a5972755/watchfiles-1.1.1-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:bfff9740c69c0e4ed32416f013f3c45e2ae42ccedd1167ef2d805c000b6c71a5", size = 460845, upload-time = "2025-10-14T15:05:30.064Z" },
    { url = "https://files.pythonhosted.org/packages/8e/a4/2df3b404469122e8680f0fcd06079317e48db58a2da2950fb45020947734/watchfiles-1.1.1-cp314-cp314-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b27cf2eb1dda37b2089e3907d8ea92922b673c0c427886d4edc6b94d8dfe5db3", size = 489027, upload-time = "2025-10-14T15:05:31.064Z" },
    { url = "https://files.pythonhosted.org/packages/ea/84/4587ba5b1f267167ee715b7f66e6382cca6938e0a4b870adad93e44747e6/watchfiles-1.1.1-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:526e86aced14a65a5b0ec50827c745597c782ff46b571dbfe46192ab9e0b3c33", size = 595615, upload-time = "2025-10-14T15:05:32.074Z" },
    { url = "https://files.pythonhosted.org/packages/6a/0f/c6988c91d06e93cd0bb3d4a808bcf32375ca1904609835c3031799e3ecae/watchfiles-1.1.1-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:04e78dd0b6352db95507fd8cb46f39d185cf8c74e4cf1e4fbad1d3df96faf510", size = 474836, upload-time = "2025-10-14T15:05:33.209Z" },
    { url = "https://files.pythonhosted.org/packages/b4/36/ded8aebea91919485b7bbabbd14f5f359326cb5ec218cd67074d1e426d74/watchfiles-1.1.1-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5c85794a4cfa094714fb9c08d4a218375b2b95b8ed1666e8677c349906246c05", size = 455099, upload-time = "2025-10-14T15:05:34.189Z" },
    { url = "https://files.pythonhosted.org/packages/98/e0/8c9bdba88af756a2fce230dd365fab2baf927ba42cd47521ee7498fd5211/watchfiles-1.1.1-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:74d5012b7630714b66be7b7b7a78855ef7ad58e8650c73afc4c076a1f480a8d6", size = 630626, upload-time = "2025-10-14T15:05:35.216Z" },
    { url = "https://files.pythonhosted.org/packages/2a/84/a95db05354bf2d19e438520d92a8ca475e578c647f78f53197f5a2f17aaf/watchfiles-1.1.1-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:8fbe85cb3201c7d380d3d0b90e63d520f15d6afe217165d7f98c9c649654db81", size = 622519, upload-time = "2025-10-14T15:05:36.259Z" },
    { url = "https://files.pythonhosted.org/packages/1d/ce/d8acdc8de545de995c339be67711e474c77d643555a9bb74a9334252bd55/watchfiles-1.1.1-cp314-cp314-win32.whl", hash = "sha256:3fa0b59c92278b5a7800d3ee7733da9d096d4aabcfabb9a928918bd276ef9b9b", size = 272078, upload-time = "2025-10-14T15:05:37.63Z" },
    { url = "https://files.pythonhosted.org/packages/c4/c9/a74487f72d0451524be827e8edec251da0cc1fcf111646a511ae752e1a3d/watchfiles-1.1.1-cp314-cp314-win_amd64.whl", hash = "sha256:c2047d0b6cea13b3316bdbafbfa0c4228ae593d995030fda39089d36e64fc03a", size = 287664, upload-time = "2025-10-14T15:05:38.95Z" },
    { url = "https://files.pythonhosted.org/packages/df/b8/8ac000702cdd496cdce998c6f4ee0ca1f15977bba51bdf07d872ebdfc34c/watchfiles-1.1.1-cp314-cp314-win_arm64.whl", hash = "sha256:842178b126593addc05acf6fce960d28bc5fae7afbaa2c6c1b3a7b9460e5be02", size = 277154, upload-time = "2025-10-14T15:05:39.954Z" },
    { url = "https://files.pythonhosted.org/packages/47/a8/e3af2184707c29f0f14b1963c0aace6529f9d1b8582d5b99f31bbf42f59e/watchfiles-1.1.1-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:88863fbbc1a7312972f1c511f202eb30866370ebb8493aef2812b9ff28156a21", size = 403820, upload-time = "2025-10-14T15:05:40.932Z" },
    { url = "https://files.pythonhosted.org/packages/c0/ec/e47e307c2f4bd75f9f9e8afbe3876679b18e1bcec449beca132a1c5ffb2d/watchfiles-1.1.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:55c7475190662e202c08c6c0f4d9e345a29367438cf8e8037f3155e10a88d5a5", size = 390510, upload-time = "2025-10-14T15:05:41.945Z" },
    { url = "https://files.pythonhosted.org/packages/d5/a0/ad235642118090f66e7b2f18fd5c42082418404a79205cdfca50b6309c13/watchfiles-1.1.1-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3f53fa183d53a1d7a8852277c92b967ae99c2d4dcee2bfacff8868e6e30b15f7", size = 448408, upload-time = "2025-10-14T15:05:43.385Z" },
    { url = "https://files.pythonhosted.org/packages/df/85/97fa10fd5ff3332ae17e7e40e20784e419e28521549780869f1413742e9d/watchfiles-1.1.1-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:6aae418a8b323732fa89721d86f39ec8f092fc2af67f4217a2b07fd3e93c6101", size = 458968, upload-time = "2025-10-14T15:05:44.404Z" },
    { url = "https://files.pythonhosted.org/packages/47/c2/9059c2e8966ea5ce678166617a7f75ecba6164375f3b288e50a40dc6d489/watchfiles-1.1.1-cp314-cp314t-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f096076119da54a6080e8920cbdaac3dbee667eb91dcc5e5b78840b87415bd44", size = 488096, upload-time = "2025-10-14T15:05:45.398Z" },
    { url = "https://files.pythonhosted.org/packages/94/44/d90a9ec8ac309bc26db808a13e7bfc0e4e78b6fc051078a554e132e80160/watchfiles-1.1.1-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:00485f441d183717038ed2e887a7c868154f216877653121068107b227a2f64c", size = 596040, upload-time = "2025-10-14T15:05:46.502Z" },
    { url = "https://files.pythonhosted.org/packages/95/68/4e3479b20ca305cfc561db3ed207a8a1c745ee32bf24f2026a129d0ddb6e/watchfiles-1.1.1-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:a55f3e9e493158d7bfdb60a1165035f1cf7d320914e7b7ea83fe22c6023b58fc", size = 473847, upload-time = "2025-10-14T15:05:47.484Z" },
    { url = "https://files.pythonhosted.org/packages/4f/55/2af26693fd15165c4ff7857e38330e1b61ab8c37d15dc79118cdba115b7a/watchfiles-1.1.1-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8c91ed27800188c2ae96d16e3149f199d62f86c7af5f5f4d2c61a3ed8cd3666c", size = 455072, upload-time = "2025-10-14T15:05:48.928Z" },
    { url = "https://files.pythonhosted.org/packages/66/1d/d0d200b10c9311ec25d2273f8aad8c3ef7cc7ea11808022501811208a750/watchfiles-1.1.1-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:311ff15a0bae3714ffb603e6ba6dbfba4065ab60865d15a6ec544133bdb21099", size = 629104, upload-time = "2025-10-14T15:05:49.908Z" },
    { url = "https://files.pythonhosted.org/packages/e3/bd/fa9bb053192491b3867ba07d2343d9f2252e00811567d30ae8d0f78136fe/watchfiles-1.1.1-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:a916a2932da8f8ab582f242c065f5c81bed3462849ca79ee357dd9551b0e9b01", size = 622112, upload-time = "2025-10-14T15:05:50.941Z" },
]

[[package]]
name = "websockets"
version = "16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/04/24/4b2031d72e840ce4c1ccb255f693b15c334757fc50023e4db9537080b8c4/websockets-16.0.tar.gz", hash = "sha256:5f6261a5e56e8d5c42a4497b364ea24d94d9563e8fbd44e78ac40879c60179b5", size = 179346, upload-time = "2026-01-10T09:23:47.181Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cc/9c/baa8456050d1c1b08dd0ec7346026668cbc6f145ab4e314d707bb845bf0d/websockets-16.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:878b336ac47938b474c8f982ac2f7266a540adc3fa4ad74ae96fea9823a02cc9", size = 177364, upload-time = "2026-01-10T09:22:59.333Z" },
    { url = "https://files.pythonhosted.org/packages/7e/0c/8811fc53e9bcff68fe7de2bcbe75116a8d959ac699a3200f4847a8925210/websockets-16.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:52a0fec0e6c8d9a784c2c78276a48a2bdf099e4ccc2a4cad53b27718dbfd0230", size = 175039, upload-time = "2026-01-10T09:23:01.171Z" },
    { url = "https://files.pythonhosted.org/packages/aa/82/39a5f910cb99ec0b59e482971238c845af9220d3ab9fa76dd9162cda9d62/websockets-16.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:e6578ed5b6981005df1860a56e3617f14a6c307e6a71b4fff8c48fdc50f3ed2c", size = 175323, upload-time = "2026-01-10T09:23:02.341Z" },
    { url = "https://files.pythonhosted.org/packages/bd/28/0a25ee5342eb5d5f297d992a77e56892ecb65e7854c7898fb7d35e9b33bd/websockets-16.0-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:95724e638f0f9c350bb1c2b0a7ad0e83d9cc0c9259f3ea94e40d7b02a2179ae5", size = 184975, upload-time = "2026-01-10T09:23:03.756Z" },
    { url = "https://files.pythonhosted.org/packages/f9/66/27ea52741752f5107c2e41fda05e8395a682a1e11c4e592a809a90c6a506/websockets-16.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c0204dc62a89dc9d50d682412c10b3542d748260d743500a85c13cd1ee4bde82", size = 186203, upload-time = "2026-01-10T09:23:05.01Z" },
    { url = "https://files.pythonhosted.org/packages/37/e5/8e32857371406a757816a2b471939d51c463509be73fa538216ea52b792a/websockets-16.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:52ac480f44d32970d66763115edea932f1c5b1312de36df06d6b219f6741eed8", size = 185653, upload-time = "2026-01-10T09:23:06.301Z" },
    { url = "https://files.pythonhosted.org/packages/9b/67/f926bac29882894669368dc73f4da900fcdf47955d0a0185d60103df5737/websockets-16.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6e5a82b677f8f6f59e8dfc34ec06ca6b5b48bc4fcda346acd093694cc2c24d8f", size = 184920, upload-time = "2026-01-10T09:23:07.492Z" },
    { url = "https://files.pythonhosted.org/packages/3c/a1/3d6ccdcd125b0a42a311bcd15a7f705d688f73b2a22d8cf1c0875d35d34a/websockets-16.0-cp313-cp313-win32.whl", hash = "sha256:abf050a199613f64c886ea10f38b47770a65154dc37181bfaff70c160f45315a", size = 178255, upload-time = "2026-01-10T09:23:09.245Z" },
    { url = "https://files.pythonhosted.org/packages/6b/ae/90366304d7c2ce80f9b826096a9e9048b4bb760e44d3b873bb272cba696b/websockets-16.0-cp313-cp313-win_amd64.whl", hash = "sha256:3425ac5cf448801335d6fdc7ae1eb22072055417a96cc6b31b3861f455fbc156", size = 178689, upload-time = "2026-01-10T09:23:10.483Z" },
    { url = "https://files.pythonhosted.org/packages/f3/1d/e88022630271f5bd349ed82417136281931e558d628dd52c4d8621b4a0b2/websockets-16.0-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:8cc451a50f2aee53042ac52d2d053d08bf89bcb31ae799cb4487587661c038a0", size = 177406, upload-time = "2026-01-10T09:23:12.178Z" },
    { url = "https://files.pythonhosted.org/packages/f2/78/e63be1bf0724eeb4616efb1ae1c9044f7c3953b7957799abb5915bffd38e/websockets-16.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:daa3b6ff70a9241cf6c7fc9e949d41232d9d7d26fd3522b1ad2b4d62487e9904", size = 175085, upload-time = "2026-01-10T09:23:13.511Z" },
    { url = "https://files.pythonhosted.org/packages/bb/f4/d3c9220d818ee955ae390cf319a7c7a467beceb24f05ee7aaaa2414345ba/websockets-16.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:fd3cb4adb94a2a6e2b7c0d8d05cb94e6f1c81a0cf9dc2694fb65c7e8d94c42e4", size = 175328, upload-time = "2026-01-10T09:23:14.727Z" },
    { url = "https://files.pythonhosted.org/packages/63/bc/d3e208028de777087e6fb2b122051a6ff7bbcca0d6df9d9c2bf1dd869ae9/websockets-16.0-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:781caf5e8eee67f663126490c2f96f40906594cb86b408a703630f95550a8c3e", size = 185044, upload-time = "2026-01-10T09:23:15.939Z" },
    { url = "https://files.pythonhosted.org/packages/ad/6e/9a0927ac24bd33a0a9af834d89e0abc7cfd8e13bed17a86407a66773cc0e/websockets-16.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:caab51a72c51973ca21fa8a18bd8165e1a0183f1ac7066a182ff27107b71e1a4", size = 186279, upload-time = "2026-01-10T09:23:17.148Z" },
    { url = "https://files.pythonhosted.org/packages/b9/ca/bf1c68440d7a868180e11be653c85959502efd3a709323230314fda6e0b3/websockets-16.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:19c4dc84098e523fd63711e563077d39e90ec6702aff4b5d9e344a60cb3c0cb1", size = 185711, upload-time = "2026-01-10T09:23:18.372Z" },
    { url = "https://files.pythonhosted.org/packages/c4/f8/fdc34643a989561f217bb477cbc47a3a07212cbda91c0e4389c43c296ebf/websockets-16.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:a5e18a238a2b2249c9a9235466b90e96ae4795672598a58772dd806edc7ac6d3", size = 184982, upload-time = "2026-01-10T09:23:19.652Z" },
    { url = "https://files.pythonhosted.org/packages/dd/d1/574fa27e233764dbac9c52730d63fcf2823b16f0856b3329fc6268d6ae4f/websockets-16.0-cp314-cp314-win32.whl", hash = "sha256:a069d734c4a043182729edd3e9f247c3b2a4035415a9172fd0f1b71658a320a8", size = 177915, upload-time = "2026-01-10T09:23:21.458Z" },
    { url = "https://files.pythonhosted.org/packages/8a/f1/ae6b937bf3126b5134ce1f482365fde31a357c784ac51852978768b5eff4/websockets-16.0-cp314-cp314-win_amd64.whl", hash = "sha256:c0ee0e63f23914732c6d7e0cce24915c48f3f1512ec1d079ed01fc629dab269d", size = 178381, upload-time = "2026-01-10T09:23:22.715Z" },
    { url = "https://files.pythonhosted.org/packages/06/9b/f791d1db48403e1f0a27577a6beb37afae94254a8c6f08be4a23e4930bc0/websockets-16.0-cp314-cp314t-macosx_10_15_universal2.whl", hash = "sha256:a35539cacc3febb22b8f4d4a99cc79b104226a756aa7400adc722e83b0d03244", size = 177737, upload-time = "2026-01-10T09:23:24.523Z" },
    { url = "https://files.pythonhosted.org/packages/bd/40/53ad02341fa33b3ce489023f635367a4ac98b73570102ad2cdd770dacc9a/websockets-16.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:b784ca5de850f4ce93ec85d3269d24d4c82f22b7212023c974c401d4980ebc5e", size = 175268, upload-time = "2026-01-10T09:23:25.781Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/6158d4e459b984f949dcbbb0c5d270154c7618e11c01029b9bbd1bb4c4f9/websockets-16.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:569d01a4e7fba956c5ae4fc988f0d4e187900f5497ce46339c996dbf24f17641", size = 175486, upload-time = "2026-01-10T09:23:27.033Z" },
    { url = "https://files.pythonhosted.org/packages/e5/2d/7583b30208b639c8090206f95073646c2c9ffd66f44df967981a64f849ad/websockets-16.0-cp314-cp314t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:50f23cdd8343b984957e4077839841146f67a3d31ab0d00e6b824e74c5b2f6e8", size = 185331, upload-time = "2026-01-10T09:23:28.259Z" },
    { url = "https://files.pythonhosted.org/packages/45/b0/cce3784eb519b7b5ad680d14b9673a31ab8dcb7aad8b64d81709d2430aa8/websockets-16.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:152284a83a00c59b759697b7f9e9cddf4e3c7861dd0d964b472b70f78f89e80e", size = 186501, upload-time = "2026-01-10T09:23:29.449Z" },
    { url = "https://files.pythonhosted.org/packages/19/60/b8ebe4c7e89fb5f6cdf080623c9d92789a53636950f7abacfc33fe2b3135/websockets-16.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:bc59589ab64b0022385f429b94697348a6a234e8ce22544e3681b2e9331b5944", size = 186062, upload-time = "2026-01-10T09:23:31.368Z" },
    { url = "https://files.pythonhosted.org/packages/88/a8/a080593f89b0138b6cba1b28f8df5673b5506f72879322288b031337c0b8/websockets-16.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:32da954ffa2814258030e5a57bc73a3635463238e797c7375dc8091327434206", size = 185356, upload-time = "2026-01-10T09:23:32.627Z" },
    { url = "https://files.pythonhosted.org/packages/c2/b6/b9afed2afadddaf5ebb2afa801abf4b0868f42f8539bfe4b071b5266c9fe/websockets-16.0-cp314-cp314t-win32.whl", hash = "sha256:5a4b4cc550cb665dd8a47f868c8d04c8230f857363ad3c9caf7a0c3bf8c61ca6", size = 178085, upload-time = "2026-01-10T09:23:33.816Z" },
    { url = "https://files.pythonhosted.org/packages/9f/3e/28135a24e384493fa804216b79a6a6759a38cc4ff59118787b9fb693df93/websockets-16.0-cp314-cp314t-win_amd64.whl", hash = "sha256:b14dc141ed6d2dde437cddb216004bcac6a1df0935d79656387bd41632ba0bbd", size = 178531, upload-time = "2026-01-10T09:23:35.016Z" },
    { url = "https://files.pythonhosted.org/packages/6f/28/258ebab549c2bf3e64d2b0217b973467394a9cea8c42f70418ca2c5d0d2e/websockets-16.0-py3-none-any.whl", hash = "sha256:1637db62fad1dc833276dded54215f2c7fa46912301a24bd94d45d46a011ceec", size = 171598, upload-time = "2026-01-10T09:23:45.395Z" },
]

[[package]]
name = "wsproto"
version = "1.3.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c7/79/12135bdf8b9c9367b8701c2c19a14c913c120b882d50b014ca0d38083c2c/wsproto-1.3.2.tar.gz", hash = "sha256:b86885dcf294e15204919950f666e06ffc6c7c114ca900b060d6e16293528294", size = 50116, upload-time = "2025-11-20T18:18:01.871Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a4/f5/10b68b7b1544245097b2a1b8238f66f2fc6dcaeb24ba5d917f52bd2eed4f/wsproto-1.3.2-py3-none-any.whl", hash = "sha256:61eea322cdf56e8cc904bd3ad7573359a242ba65688716b0710a5eb12beab584", size = 24405, upload-time = "2025-11-20T18:18:00.454Z" },
]

[[package]]
name = "yarl"
version = "1.23.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "idna" },
    { name = "multidict" },
    { name = "propcache" },
]
sdist = { url = "https://files.pythonhosted.org/packages/23/6e/beb1beec874a72f23815c1434518bfc4ed2175065173fb138c3705f658d4/yarl-1.23.0.tar.gz", hash = "sha256:53b1ea6ca88ebd4420379c330aea57e258408dd0df9af0992e5de2078dc9f5d5", size = 194676, upload-time = "2026-03-01T22:07:53.373Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/4b/a0a6e5d0ee8a2f3a373ddef8a4097d74ac901ac363eea1440464ccbe0898/yarl-1.23.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:16c6994ac35c3e74fb0ae93323bf8b9c2a9088d55946109489667c510a7d010e", size = 123796, upload-time = "2026-03-01T22:05:41.412Z" },
    { url = "https://files.pythonhosted.org/packages/67/b6/8925d68af039b835ae876db5838e82e76ec87b9782ecc97e192b809c4831/yarl-1.23.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:4a42e651629dafb64fd5b0286a3580613702b5809ad3f24934ea87595804f2c5", size = 86547, upload-time = "2026-03-01T22:05:42.841Z" },
    { url = "https://files.pythonhosted.org/packages/ae/50/06d511cc4b8e0360d3c94af051a768e84b755c5eb031b12adaaab6dec6e5/yarl-1.23.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:7c6b9461a2a8b47c65eef63bb1c76a4f1c119618ffa99ea79bc5bb1e46c5821b", size = 85854, upload-time = "2026-03-01T22:05:44.85Z" },
    { url = "https://files.pythonhosted.org/packages/c4/f4/4e30b250927ffdab4db70da08b9b8d2194d7c7b400167b8fbeca1e4701ca/yarl-1.23.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2569b67d616eab450d262ca7cb9f9e19d2f718c70a8b88712859359d0ab17035", size = 98351, upload-time = "2026-03-01T22:05:46.836Z" },
    { url = "https://files.pythonhosted.org/packages/86/fc/4118c5671ea948208bdb1492d8b76bdf1453d3e73df051f939f563e7dcc5/yarl-1.23.0-cp313-cp313-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:e9d9a4d06d3481eab79803beb4d9bd6f6a8e781ec078ac70d7ef2dcc29d1bea5", size = 92711, upload-time = "2026-03-01T22:05:48.316Z" },
    { url = "https://files.pythonhosted.org/packages/56/11/1ed91d42bd9e73c13dc9e7eb0dd92298d75e7ac4dd7f046ad0c472e231cd/yarl-1.23.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:f514f6474e04179d3d33175ed3f3e31434d3130d42ec153540d5b157deefd735", size = 106014, upload-time = "2026-03-01T22:05:50.028Z" },
    { url = "https://files.pythonhosted.org/packages/ce/c9/74e44e056a23fbc33aca71779ef450ca648a5bc472bdad7a82339918f818/yarl-1.23.0-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:fda207c815b253e34f7e1909840fd14299567b1c0eb4908f8c2ce01a41265401", size = 105557, upload-time = "2026-03-01T22:05:51.416Z" },
    { url = "https://files.pythonhosted.org/packages/66/fe/b1e10b08d287f518994f1e2ff9b6d26f0adeecd8dd7d533b01bab29a3eda/yarl-1.23.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:34b6cf500e61c90f305094911f9acc9c86da1a05a7a3f5be9f68817043f486e4", size = 101559, upload-time = "2026-03-01T22:05:52.872Z" },
    { url = "https://files.pythonhosted.org/packages/72/59/c5b8d94b14e3d3c2a9c20cb100119fd534ab5a14b93673ab4cc4a4141ea5/yarl-1.23.0-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:d7504f2b476d21653e4d143f44a175f7f751cd41233525312696c76aa3dbb23f", size = 100502, upload-time = "2026-03-01T22:05:54.954Z" },
    { url = "https://files.pythonhosted.org/packages/77/4f/96976cb54cbfc5c9fd73ed4c51804f92f209481d1fb190981c0f8a07a1d7/yarl-1.23.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:578110dd426f0d209d1509244e6d4a3f1a3e9077655d98c5f22583d63252a08a", size = 98027, upload-time = "2026-03-01T22:05:56.409Z" },
    { url = "https://files.pythonhosted.org/packages/63/6e/904c4f476471afdbad6b7e5b70362fb5810e35cd7466529a97322b6f5556/yarl-1.23.0-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:609d3614d78d74ebe35f54953c5bbd2ac647a7ddb9c30a5d877580f5e86b22f2", size = 95369, upload-time = "2026-03-01T22:05:58.141Z" },
    { url = "https://files.pythonhosted.org/packages/9d/40/acfcdb3b5f9d68ef499e39e04d25e141fe90661f9d54114556cf83be8353/yarl-1.23.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:4966242ec68afc74c122f8459abd597afd7d8a60dc93d695c1334c5fd25f762f", size = 105565, upload-time = "2026-03-01T22:06:00.286Z" },
    { url = "https://files.pythonhosted.org/packages/5e/c6/31e28f3a6ba2869c43d124f37ea5260cac9c9281df803c354b31f4dd1f3c/yarl-1.23.0-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:e0fd068364a6759bc794459f0a735ab151d11304346332489c7972bacbe9e72b", size = 99813, upload-time = "2026-03-01T22:06:01.712Z" },
    { url = "https://files.pythonhosted.org/packages/08/1f/6f65f59e72d54aa467119b63fc0b0b1762eff0232db1f4720cd89e2f4a17/yarl-1.23.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:39004f0ad156da43e86aa71f44e033de68a44e5a31fc53507b36dd253970054a", size = 105632, upload-time = "2026-03-01T22:06:03.188Z" },
    { url = "https://files.pythonhosted.org/packages/a3/c4/18b178a69935f9e7a338127d5b77d868fdc0f0e49becd286d51b3a18c61d/yarl-1.23.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:e5723c01a56c5028c807c701aa66722916d2747ad737a046853f6c46f4875543", size = 101895, upload-time = "2026-03-01T22:06:04.651Z" },
    { url = "https://files.pythonhosted.org/packages/8f/54/f5b870b5505663911dba950a8e4776a0dbd51c9c54c0ae88e823e4b874a0/yarl-1.23.0-cp313-cp313-win32.whl", hash = "sha256:1b6b572edd95b4fa8df75de10b04bc81acc87c1c7d16bcdd2035b09d30acc957", size = 82356, upload-time = "2026-03-01T22:06:06.04Z" },
    { url = "https://files.pythonhosted.org/packages/7a/84/266e8da36879c6edcd37b02b547e2d9ecdfea776be49598e75696e3316e1/yarl-1.23.0-cp313-cp313-win_amd64.whl", hash = "sha256:baaf55442359053c7d62f6f8413a62adba3205119bcb6f49594894d8be47e5e3", size = 87515, upload-time = "2026-03-01T22:06:08.107Z" },
    { url = "https://files.pythonhosted.org/packages/00/fd/7e1c66efad35e1649114fa13f17485f62881ad58edeeb7f49f8c5e748bf9/yarl-1.23.0-cp313-cp313-win_arm64.whl", hash = "sha256:fb4948814a2a98e3912505f09c9e7493b1506226afb1f881825368d6fb776ee3", size = 81785, upload-time = "2026-03-01T22:06:10.181Z" },
    { url = "https://files.pythonhosted.org/packages/9c/fc/119dd07004f17ea43bb91e3ece6587759edd7519d6b086d16bfbd3319982/yarl-1.23.0-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:aecfed0b41aa72b7881712c65cf764e39ce2ec352324f5e0837c7048d9e6daaa", size = 130719, upload-time = "2026-03-01T22:06:11.708Z" },
    { url = "https://files.pythonhosted.org/packages/e6/0d/9f2348502fbb3af409e8f47730282cd6bc80dec6630c1e06374d882d6eb2/yarl-1.23.0-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:a41bcf68efd19073376eb8cf948b8d9be0af26256403e512bb18f3966f1f9120", size = 89690, upload-time = "2026-03-01T22:06:13.429Z" },
    { url = "https://files.pythonhosted.org/packages/50/93/e88f3c80971b42cfc83f50a51b9d165a1dbf154b97005f2994a79f212a07/yarl-1.23.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:cde9a2ecd91668bcb7f077c4966d8ceddb60af01b52e6e3e2680e4cf00ad1a59", size = 89851, upload-time = "2026-03-01T22:06:15.53Z" },
    { url = "https://files.pythonhosted.org/packages/1c/07/61c9dd8ba8f86473263b4036f70fb594c09e99c0d9737a799dfd8bc85651/yarl-1.23.0-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5023346c4ee7992febc0068e7593de5fa2bf611848c08404b35ebbb76b1b0512", size = 95874, upload-time = "2026-03-01T22:06:17.553Z" },
    { url = "https://files.pythonhosted.org/packages/9e/e9/f9ff8ceefba599eac6abddcfb0b3bee9b9e636e96dbf54342a8577252379/yarl-1.23.0-cp313-cp313t-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:d1009abedb49ae95b136a8904a3f71b342f849ffeced2d3747bf29caeda218c4", size = 88710, upload-time = "2026-03-01T22:06:19.004Z" },
    { url = "https://files.pythonhosted.org/packages/eb/78/0231bfcc5d4c8eec220bc2f9ef82cb4566192ea867a7c5b4148f44f6cbcd/yarl-1.23.0-cp313-cp313t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:a8d00f29b42f534cc8aa3931cfe773b13b23e561e10d2b26f27a8d309b0e82a1", size = 101033, upload-time = "2026-03-01T22:06:21.203Z" },
    { url = "https://files.pythonhosted.org/packages/cd/9b/30ea5239a61786f18fd25797151a17fbb3be176977187a48d541b5447dd4/yarl-1.23.0-cp313-cp313t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:95451e6ce06c3e104556d73b559f5da6c34a069b6b62946d3ad66afcd51642ea", size = 100817, upload-time = "2026-03-01T22:06:22.738Z" },
    { url = "https://files.pythonhosted.org/packages/62/e2/a4980481071791bc83bce2b7a1a1f7adcabfa366007518b4b845e92eeee3/yarl-1.23.0-cp313-cp313t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:531ef597132086b6cf96faa7c6c1dcd0361dd5f1694e5cc30375907b9b7d3ea9", size = 97482, upload-time = "2026-03-01T22:06:24.21Z" },
    { url = "https://files.pythonhosted.org/packages/e5/1e/304a00cf5f6100414c4b5a01fc7ff9ee724b62158a08df2f8170dfc72a2d/yarl-1.23.0-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:88f9fb0116fbfcefcab70f85cf4b74a2b6ce5d199c41345296f49d974ddb4123", size = 95949, upload-time = "2026-03-01T22:06:25.697Z" },
    { url = "https://files.pythonhosted.org/packages/68/03/093f4055ed4cae649ac53bca3d180bd37102e9e11d048588e9ab0c0108d0/yarl-1.23.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:e7b0460976dc75cb87ad9cc1f9899a4b97751e7d4e77ab840fc9b6d377b8fd24", size = 95839, upload-time = "2026-03-01T22:06:27.309Z" },
    { url = "https://files.pythonhosted.org/packages/b9/28/4c75ebb108f322aa8f917ae10a8ffa4f07cae10a8a627b64e578617df6a0/yarl-1.23.0-cp313-cp313t-musllinux_1_2_armv7l.whl", hash = "sha256:115136c4a426f9da976187d238e84139ff6b51a20839aa6e3720cd1026d768de", size = 90696, upload-time = "2026-03-01T22:06:29.048Z" },
    { url = "https://files.pythonhosted.org/packages/23/9c/42c2e2dd91c1a570402f51bdf066bfdb1241c2240ba001967bad778e77b7/yarl-1.23.0-cp313-cp313t-musllinux_1_2_ppc64le.whl", hash = "sha256:ead11956716a940c1abc816b7df3fa2b84d06eaed8832ca32f5c5e058c65506b", size = 100865, upload-time = "2026-03-01T22:06:30.525Z" },
    { url = "https://files.pythonhosted.org/packages/74/05/1bcd60a8a0a914d462c305137246b6f9d167628d73568505fce3f1cb2e65/yarl-1.23.0-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:fe8f8f5e70e6dbdfca9882cd9deaac058729bcf323cf7a58660901e55c9c94f6", size = 96234, upload-time = "2026-03-01T22:06:32.692Z" },
    { url = "https://files.pythonhosted.org/packages/90/b2/f52381aac396d6778ce516b7bc149c79e65bfc068b5de2857ab69eeea3b7/yarl-1.23.0-cp313-cp313t-musllinux_1_2_s390x.whl", hash = "sha256:a0e317df055958a0c1e79e5d2aa5a5eaa4a6d05a20d4b0c9c3f48918139c9fc6", size = 100295, upload-time = "2026-03-01T22:06:34.268Z" },
    { url = "https://files.pythonhosted.org/packages/e5/e8/638bae5bbf1113a659b2435d8895474598afe38b4a837103764f603aba56/yarl-1.23.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:6f0fd84de0c957b2d280143522c4f91a73aada1923caee763e24a2b3fda9f8a5", size = 97784, upload-time = "2026-03-01T22:06:35.864Z" },
    { url = "https://files.pythonhosted.org/packages/80/25/a3892b46182c586c202629fc2159aa13975d3741d52ebd7347fd501d48d5/yarl-1.23.0-cp313-cp313t-win32.whl", hash = "sha256:93a784271881035ab4406a172edb0faecb6e7d00f4b53dc2f55919d6c9688595", size = 88313, upload-time = "2026-03-01T22:06:37.39Z" },
    { url = "https://files.pythonhosted.org/packages/43/68/8c5b36aa5178900b37387937bc2c2fe0e9505537f713495472dcf6f6fccc/yarl-1.23.0-cp313-cp313t-win_amd64.whl", hash = "sha256:dd00607bffbf30250fe108065f07453ec124dbf223420f57f5e749b04295e090", size = 94932, upload-time = "2026-03-01T22:06:39.579Z" },
    { url = "https://files.pythonhosted.org/packages/c6/cc/d79ba8292f51f81f4dc533a8ccfb9fc6992cabf0998ed3245de7589dc07c/yarl-1.23.0-cp313-cp313t-win_arm64.whl", hash = "sha256:ac09d42f48f80c9ee1635b2fcaa819496a44502737660d3c0f2ade7526d29144", size = 84786, upload-time = "2026-03-01T22:06:41.988Z" },
    { url = "https://files.pythonhosted.org/packages/90/98/b85a038d65d1b92c3903ab89444f48d3cee490a883477b716d7a24b1a78c/yarl-1.23.0-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:21d1b7305a71a15b4794b5ff22e8eef96ff4a6d7f9657155e5aa419444b28912", size = 124455, upload-time = "2026-03-01T22:06:43.615Z" },
    { url = "https://files.pythonhosted.org/packages/39/54/bc2b45559f86543d163b6e294417a107bb87557609007c007ad889afec18/yarl-1.23.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:85610b4f27f69984932a7abbe52703688de3724d9f72bceb1cca667deff27474", size = 86752, upload-time = "2026-03-01T22:06:45.425Z" },
    { url = "https://files.pythonhosted.org/packages/24/f9/e8242b68362bffe6fb536c8db5076861466fc780f0f1b479fc4ffbebb128/yarl-1.23.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:23f371bd662cf44a7630d4d113101eafc0cfa7518a2760d20760b26021454719", size = 86291, upload-time = "2026-03-01T22:06:46.974Z" },
    { url = "https://files.pythonhosted.org/packages/ea/d8/d1cb2378c81dd729e98c716582b1ccb08357e8488e4c24714658cc6630e8/yarl-1.23.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c4a80f77dc1acaaa61f0934176fccca7096d9b1ff08c8ba9cddf5ae034a24319", size = 99026, upload-time = "2026-03-01T22:06:48.459Z" },
    { url = "https://files.pythonhosted.org/packages/0a/ff/7196790538f31debe3341283b5b0707e7feb947620fc5e8236ef28d44f72/yarl-1.23.0-cp314-cp314-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:bd654fad46d8d9e823afbb4f87c79160b5a374ed1ff5bde24e542e6ba8f41434", size = 92355, upload-time = "2026-03-01T22:06:50.306Z" },
    { url = "https://files.pythonhosted.org/packages/c1/56/25d58c3eddde825890a5fe6aa1866228377354a3c39262235234ab5f616b/yarl-1.23.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:682bae25f0a0dd23a056739f23a134db9f52a63e2afd6bfb37ddc76292bbd723", size = 106417, upload-time = "2026-03-01T22:06:52.1Z" },
    { url = "https://files.pythonhosted.org/packages/51/8a/882c0e7bc8277eb895b31bce0138f51a1ba551fc2e1ec6753ffc1e7c1377/yarl-1.23.0-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a82836cab5f197a0514235aaf7ffccdc886ccdaa2324bc0aafdd4ae898103039", size = 106422, upload-time = "2026-03-01T22:06:54.424Z" },
    { url = "https://files.pythonhosted.org/packages/42/2b/fef67d616931055bf3d6764885990a3ac647d68734a2d6a9e1d13de437a2/yarl-1.23.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1c57676bdedc94cd3bc37724cf6f8cd2779f02f6aba48de45feca073e714fe52", size = 101915, upload-time = "2026-03-01T22:06:55.895Z" },
    { url = "https://files.pythonhosted.org/packages/18/6a/530e16aebce27c5937920f3431c628a29a4b6b430fab3fd1c117b26ff3f6/yarl-1.23.0-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:c7f8dc16c498ff06497c015642333219871effba93e4a2e8604a06264aca5c5c", size = 100690, upload-time = "2026-03-01T22:06:58.21Z" },
    { url = "https://files.pythonhosted.org/packages/88/08/93749219179a45e27b036e03260fda05190b911de8e18225c294ac95bbc9/yarl-1.23.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:5ee586fb17ff8f90c91cf73c6108a434b02d69925f44f5f8e0d7f2f260607eae", size = 98750, upload-time = "2026-03-01T22:06:59.794Z" },
    { url = "https://files.pythonhosted.org/packages/d9/cf/ea424a004969f5d81a362110a6ac1496d79efdc6d50c2c4b2e3ea0fc2519/yarl-1.23.0-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:17235362f580149742739cc3828b80e24029d08cbb9c4bda0242c7b5bc610a8e", size = 94685, upload-time = "2026-03-01T22:07:01.375Z" },
    { url = "https://files.pythonhosted.org/packages/e2/b7/14341481fe568e2b0408bcf1484c652accafe06a0ade9387b5d3fd9df446/yarl-1.23.0-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:0793e2bd0cf14234983bbb371591e6bea9e876ddf6896cdcc93450996b0b5c85", size = 106009, upload-time = "2026-03-01T22:07:03.151Z" },
    { url = "https://files.pythonhosted.org/packages/0a/e6/5c744a9b54f4e8007ad35bce96fbc9218338e84812d36f3390cea616881a/yarl-1.23.0-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:3650dc2480f94f7116c364096bc84b1d602f44224ef7d5c7208425915c0475dd", size = 100033, upload-time = "2026-03-01T22:07:04.701Z" },
    { url = "https://files.pythonhosted.org/packages/0c/23/e3bfc188d0b400f025bc49d99793d02c9abe15752138dcc27e4eaf0c4a9e/yarl-1.23.0-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:f40e782d49630ad384db66d4d8b73ff4f1b8955dc12e26b09a3e3af064b3b9d6", size = 106483, upload-time = "2026-03-01T22:07:06.231Z" },
    { url = "https://files.pythonhosted.org/packages/72/42/f0505f949a90b3f8b7a363d6cbdf398f6e6c58946d85c6d3a3bc70595b26/yarl-1.23.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:94f8575fbdf81749008d980c17796097e645574a3b8c28ee313931068dad14fe", size = 102175, upload-time = "2026-03-01T22:07:08.4Z" },
    { url = "https://files.pythonhosted.org/packages/aa/65/b39290f1d892a9dd671d1c722014ca062a9c35d60885d57e5375db0404b5/yarl-1.23.0-cp314-cp314-win32.whl", hash = "sha256:c8aa34a5c864db1087d911a0b902d60d203ea3607d91f615acd3f3108ac32169", size = 83871, upload-time = "2026-03-01T22:07:09.968Z" },
    { url = "https://files.pythonhosted.org/packages/a9/5b/9b92f54c784c26e2a422e55a8d2607ab15b7ea3349e28359282f84f01d43/yarl-1.23.0-cp314-cp314-win_amd64.whl", hash = "sha256:63e92247f383c85ab00dd0091e8c3fa331a96e865459f5ee80353c70a4a42d70", size = 89093, upload-time = "2026-03-01T22:07:11.501Z" },
    { url = "https://files.pythonhosted.org/packages/e0/7d/8a84dc9381fd4412d5e7ff04926f9865f6372b4c2fd91e10092e65d29eb8/yarl-1.23.0-cp314-cp314-win_arm64.whl", hash = "sha256:70efd20be968c76ece7baa8dafe04c5be06abc57f754d6f36f3741f7aa7a208e", size = 83384, upload-time = "2026-03-01T22:07:13.069Z" },
    { url = "https://files.pythonhosted.org/packages/dd/8d/d2fad34b1c08aa161b74394183daa7d800141aaaee207317e82c790b418d/yarl-1.23.0-cp314-cp314t-macosx_10_15_universal2.whl", hash = "sha256:9a18d6f9359e45722c064c97464ec883eb0e0366d33eda61cb19a244bf222679", size = 131019, upload-time = "2026-03-01T22:07:14.903Z" },
    { url = "https://files.pythonhosted.org/packages/19/ff/33009a39d3ccf4b94d7d7880dfe17fb5816c5a4fe0096d9b56abceea9ac7/yarl-1.23.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:2803ed8b21ca47a43da80a6fd1ed3019d30061f7061daa35ac54f63933409412", size = 89894, upload-time = "2026-03-01T22:07:17.372Z" },
    { url = "https://files.pythonhosted.org/packages/0c/f1/dab7ac5e7306fb79c0190766a3c00b4cb8d09a1f390ded68c85a5934faf5/yarl-1.23.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:394906945aa8b19fc14a61cf69743a868bb8c465efe85eee687109cc540b98f4", size = 89979, upload-time = "2026-03-01T22:07:19.361Z" },
    { url = "https://files.pythonhosted.org/packages/aa/b1/08e95f3caee1fad6e65017b9f26c1d79877b502622d60e517de01e72f95d/yarl-1.23.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:71d006bee8397a4a89f469b8deb22469fe7508132d3c17fa6ed871e79832691c", size = 95943, upload-time = "2026-03-01T22:07:21.266Z" },
    { url = "https://files.pythonhosted.org/packages/c0/cc/6409f9018864a6aa186c61175b977131f373f1988e198e031236916e87e4/yarl-1.23.0-cp314-cp314t-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:62694e275c93d54f7ccedcfef57d42761b2aad5234b6be1f3e3026cae4001cd4", size = 88786, upload-time = "2026-03-01T22:07:23.129Z" },
    { url = "https://files.pythonhosted.org/packages/76/40/cc22d1d7714b717fde2006fad2ced5efe5580606cb059ae42117542122f3/yarl-1.23.0-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:a31de1613658308efdb21ada98cbc86a97c181aa050ba22a808120bb5be3ab94", size = 101307, upload-time = "2026-03-01T22:07:24.689Z" },
    { url = "https://files.pythonhosted.org/packages/8f/0d/476c38e85ddb4c6ec6b20b815bdd779aa386a013f3d8b85516feee55c8dc/yarl-1.23.0-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:fb1e8b8d66c278b21d13b0a7ca22c41dd757a7c209c6b12c313e445c31dd3b28", size = 100904, upload-time = "2026-03-01T22:07:26.287Z" },
    { url = "https://files.pythonhosted.org/packages/72/32/0abe4a76d59adf2081dcb0397168553ece4616ada1c54d1c49d8936c74f8/yarl-1.23.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:50f9d8d531dfb767c565f348f33dd5139a6c43f5cbdf3f67da40d54241df93f6", size = 97728, upload-time = "2026-03-01T22:07:27.906Z" },
    { url = "https://files.pythonhosted.org/packages/b7/35/7b30f4810fba112f60f5a43237545867504e15b1c7647a785fbaf588fac2/yarl-1.23.0-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:575aa4405a656e61a540f4a80eaa5260f2a38fff7bfdc4b5f611840d76e9e277", size = 95964, upload-time = "2026-03-01T22:07:30.198Z" },
    { url = "https://files.pythonhosted.org/packages/2d/86/ed7a73ab85ef00e8bb70b0cb5421d8a2a625b81a333941a469a6f4022828/yarl-1.23.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:041b1a4cefacf65840b4e295c6985f334ba83c30607441ae3cf206a0eed1a2e4", size = 95882, upload-time = "2026-03-01T22:07:32.132Z" },
    { url = "https://files.pythonhosted.org/packages/19/90/d56967f61a29d8498efb7afb651e0b2b422a1e9b47b0ab5f4e40a19b699b/yarl-1.23.0-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:d38c1e8231722c4ce40d7593f28d92b5fc72f3e9774fe73d7e800ec32299f63a", size = 90797, upload-time = "2026-03-01T22:07:34.404Z" },
    { url = "https://files.pythonhosted.org/packages/72/00/8b8f76909259f56647adb1011d7ed8b321bcf97e464515c65016a47ecdf0/yarl-1.23.0-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:d53834e23c015ee83a99377db6e5e37d8484f333edb03bd15b4bc312cc7254fb", size = 101023, upload-time = "2026-03-01T22:07:35.953Z" },
    { url = "https://files.pythonhosted.org/packages/ac/e2/cab11b126fb7d440281b7df8e9ddbe4851e70a4dde47a202b6642586b8d9/yarl-1.23.0-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:2e27c8841126e017dd2a054a95771569e6070b9ee1b133366d8b31beb5018a41", size = 96227, upload-time = "2026-03-01T22:07:37.594Z" },
    { url = "https://files.pythonhosted.org/packages/c2/9b/2c893e16bfc50e6b2edf76c1a9eb6cb0c744346197e74c65e99ad8d634d0/yarl-1.23.0-cp314-cp314t-musllinux_1_2_s390x.whl", hash = "sha256:76855800ac56f878847a09ce6dba727c93ca2d89c9e9d63002d26b916810b0a2", size = 100302, upload-time = "2026-03-01T22:07:39.334Z" },
    { url = "https://files.pythonhosted.org/packages/28/ec/5498c4e3a6d5f1003beb23405671c2eb9cdbf3067d1c80f15eeafe301010/yarl-1.23.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:e09fd068c2e169a7070d83d3bde728a4d48de0549f975290be3c108c02e499b4", size = 98202, upload-time = "2026-03-01T22:07:41.717Z" },
    { url = "https://files.pythonhosted.org/packages/fe/c3/cd737e2d45e70717907f83e146f6949f20cc23cd4bf7b2688727763aa458/yarl-1.23.0-cp314-cp314t-win32.whl", hash = "sha256:73309162a6a571d4cbd3b6a1dcc703c7311843ae0d1578df6f09be4e98df38d4", size = 90558, upload-time = "2026-03-01T22:07:43.433Z" },
    { url = "https://files.pythonhosted.org/packages/e1/19/3774d162f6732d1cfb0b47b4140a942a35ca82bb19b6db1f80e9e7bdc8f8/yarl-1.23.0-cp314-cp314t-win_amd64.whl", hash = "sha256:4503053d296bc6e4cbd1fad61cf3b6e33b939886c4f249ba7c78b602214fabe2", size = 97610, upload-time = "2026-03-01T22:07:45.773Z" },
    { url = "https://files.pythonhosted.org/packages/51/47/3fa2286c3cb162c71cdb34c4224d5745a1ceceb391b2bd9b19b668a8d724/yarl-1.23.0-cp314-cp314t-win_arm64.whl", hash = "sha256:44bb7bef4ea409384e3f8bc36c063d77ea1b8d4a5b2706956c0d6695f07dcc25", size = 86041, upload-time = "2026-03-01T22:07:49.026Z" },
    { url = "https://files.pythonhosted.org/packages/69/68/c8739671f5699c7dc470580a4f821ef37c32c4cb0b047ce223a7f115757f/yarl-1.23.0-py3-none-any.whl", hash = "sha256:a2df6afe50dea8ae15fa34c9f824a3ee958d785fd5d089063d960bae1daa0a3f", size = 48288, upload-time = "2026-03-01T22:07:51.388Z" },
]

[[package]]
name = "yt-dlp"
version = "2026.3.13"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/34/69/59253e5627f583939e742a592f56dc7d7f30d164473e58f055e1fccdc02b/yt_dlp-2026.3.13.tar.gz", hash = "sha256:fb43659db684a3db6ff2f5c92e0f1641262f6ecc71dbb64fefe84177aaba9e36", size = 3117911, upload-time = "2026-03-13T09:02:22.711Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f0/ef/52ed7ed10d2e1a22badf74b520b617c48b0a725a981620393245ac842bf9/yt_dlp-2026.3.13-py3-none-any.whl", hash = "sha256:e22e7716f94c08e76b29c0172a3fe0c01d8cabab9bce7f528ad440d70a0d213c", size = 3315062, upload-time = "2026-03-13T09:02:20.357Z" },
]

[package.optional-dependencies]
curl-cffi = [
    { name = "curl-cffi", marker = "implementation_name == 'cpython'" },
]
default = [
    { name = "brotli", marker = "implementation_name == 'cpython'" },
    { name = "brotlicffi", marker = "implementation_name != 'cpython'" },
    { name = "certifi" },
    { name = "mutagen" },
    { name = "pycryptodomex" },
    { name = "requests" },
    { name = "urllib3" },
    { name = "websockets" },
    { name = "yt-dlp-ejs" },
]
deno = [
    { name = "deno" },
]

[[package]]
name = "yt-dlp-ejs"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/63/39/57bc2dedbcd4c921fa740fc99f83ada045a219a0e9bb3283b9ab2102e840/yt_dlp_ejs-0.7.0.tar.gz", hash = "sha256:ecac13eb9ff948da84b39f1030fa03422abaf32dc58a0edd78f5dbcc03843556", size = 95961, upload-time = "2026-03-13T07:34:43.612Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/59/f6/54fe93b9db02b7727043fb48816504f09066ca6d7f7d6145cd9d713a1047/yt_dlp_ejs-0.7.0-py3-none-any.whl", hash = "sha256:967e9cbe114ddfd046ff4668af18b1827b4597e2e47a83deea668a355828c798", size = 53444, upload-time = "2026-03-13T07:34:42.195Z" },
]
```

## File: `app/dl_formats.py`
```python
import copy

AUDIO_FORMATS = ("m4a", "mp3", "opus", "wav", "flac")
CAPTION_MODES = ("auto_only", "manual_only", "prefer_manual", "prefer_auto")

CODEC_FILTER_MAP = {
    'h264': "[vcodec~='^(h264|avc)']",
    'h265': "[vcodec~='^(h265|hevc)']",
    'av1':  "[vcodec~='^av0?1']",
    'vp9':  "[vcodec~='^vp0?9']",
}


def _normalize_caption_mode(mode: str) -> str:
    mode = (mode or "").strip()
    return mode if mode in CAPTION_MODES else "prefer_manual"


def _normalize_subtitle_language(language: str) -> str:
    language = (language or "").strip()
    return language or "en"


def get_format(download_type: str, codec: str, format: str, quality: str) -> str:
    """
    Returns yt-dlp format selector.

    Args:
      download_type (str): selected content type (video, audio, captions, thumbnail)
      codec (str): selected video codec (auto, h264, h265, av1, vp9)
      format (str): selected output format/profile for type
      quality (str): selected quality

    Raises:
      Exception: unknown type/format

    Returns:
      str: yt-dlp format selector
    """
    download_type = (download_type or "video").strip().lower()
    format = (format or "any").strip().lower()
    codec = (codec or "auto").strip().lower()
    quality = (quality or "best").strip().lower()

    if format.startswith("custom:"):
        return format[7:]

    if download_type == "thumbnail":
        return "bestaudio/best"

    if download_type == "captions":
        return "bestaudio/best"

    if download_type == "audio":
        if format not in AUDIO_FORMATS:
            raise Exception(f"Unknown audio format {format}")
        return f"bestaudio[ext={format}]/bestaudio/best"

    if download_type == "video":
        if format not in ("any", "mp4", "ios"):
            raise Exception(f"Unknown video format {format}")
        vfmt, afmt = ("[ext=mp4]", "[ext=m4a]") if format in ("mp4", "ios") else ("", "")
        vres = f"[height<={quality}]" if quality not in ("best", "worst") else ""
        vcombo = vres + vfmt
        codec_filter = CODEC_FILTER_MAP.get(codec, "")

        if format == "ios":
            return f"bestvideo[vcodec~='^((he|a)vc|h26[45])']{vres}+bestaudio[acodec=aac]/bestvideo[vcodec~='^((he|a)vc|h26[45])']{vres}+bestaudio{afmt}/bestvideo{vcombo}+bestaudio{afmt}/best{vcombo}"

        if codec_filter:
            return f"bestvideo{codec_filter}{vcombo}+bestaudio{afmt}/bestvideo{vcombo}+bestaudio{afmt}/best{vcombo}"
        return f"bestvideo{vcombo}+bestaudio{afmt}/best{vcombo}"

    raise Exception(f"Unknown download_type {download_type}")


def get_opts(
    download_type: str,
    codec: str,
    format: str,
    quality: str,
    ytdl_opts: dict,
    subtitle_language: str = "en",
    subtitle_mode: str = "prefer_manual",
) -> dict:
    """
    Returns extra yt-dlp options/postprocessors.

    Args:
      download_type (str): selected content type
      codec (str): selected codec (unused currently, kept for API consistency)
      format (str): selected format/profile
      quality (str): selected quality
      ytdl_opts (dict): current options selected

    Returns:
      dict: extended options
    """
    del codec  # kept for parity with get_format signature

    download_type = (download_type or "video").strip().lower()
    format = (format or "any").strip().lower()
    opts = copy.deepcopy(ytdl_opts)

    postprocessors = []

    if download_type == "audio":
        postprocessors.append(
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": format,
                "preferredquality": 0 if quality == "best" else quality,
            }
        )

        if format not in ("wav") and "writethumbnail" not in opts:
            opts["writethumbnail"] = True
            postprocessors.append(
                {
                    "key": "FFmpegThumbnailsConvertor",
                    "format": "jpg",
                    "when": "before_dl",
                }
            )
            postprocessors.append({"key": "FFmpegMetadata"})
            postprocessors.append({"key": "EmbedThumbnail"})

    if download_type == "thumbnail":
        opts["skip_download"] = True
        opts["writethumbnail"] = True
        postprocessors.append(
            {"key": "FFmpegThumbnailsConvertor", "format": "jpg", "when": "before_dl"}
        )

    if download_type == "captions":
        mode = _normalize_caption_mode(subtitle_mode)
        language = _normalize_subtitle_language(subtitle_language)
        opts["skip_download"] = True
        requested_subtitle_format = (format or "srt").lower()
        if requested_subtitle_format == "txt":
            requested_subtitle_format = "srt"
        opts["subtitlesformat"] = requested_subtitle_format
        if mode == "manual_only":
            opts["writesubtitles"] = True
            opts["writeautomaticsub"] = False
            opts["subtitleslangs"] = [language]
        elif mode == "auto_only":
            opts["writesubtitles"] = False
            opts["writeautomaticsub"] = True
            # `-orig` captures common YouTube auto-sub tags. The plain language
            # fallback keeps behavior useful across other extractors.
            opts["subtitleslangs"] = [f"{language}-orig", language]
        elif mode == "prefer_auto":
            opts["writesubtitles"] = True
            opts["writeautomaticsub"] = True
            opts["subtitleslangs"] = [f"{language}-orig", language]
        else:
            opts["writesubtitles"] = True
            opts["writeautomaticsub"] = True
            opts["subtitleslangs"] = [language, f"{language}-orig"]

    opts["postprocessors"] = postprocessors + (
        opts["postprocessors"] if "postprocessors" in opts else []
    )
    return opts
```

## File: `app/main.py`
```python
#!/usr/bin/env python3
# pylint: disable=no-member,method-hidden

import os
import sys
import asyncio
from pathlib import Path
from aiohttp import web
from aiohttp.log import access_logger
import ssl
import socket
import socketio
import logging
import json
import pathlib
import re
from watchfiles import DefaultFilter, Change, awatch

from ytdl import DownloadQueueNotifier, DownloadQueue
from yt_dlp.version import __version__ as yt_dlp_version

log = logging.getLogger('main')

def parseLogLevel(logLevel):
    match logLevel:
        case 'DEBUG':
            return logging.DEBUG
        case 'INFO':
            return logging.INFO
        case 'WARNING':
            return logging.WARNING
        case 'ERROR':
            return logging.ERROR
        case 'CRITICAL':
            return logging.CRITICAL
        case _:
            return None

# Configure logging before Config() uses it so early messages are not dropped.
# Only configure if no handlers are set (avoid clobbering hosting app settings).
if not logging.getLogger().hasHandlers():
    logging.basicConfig(level=parseLogLevel(os.environ.get('LOGLEVEL', 'INFO')) or logging.INFO)

class Config:
    _DEFAULTS = {
        'DOWNLOAD_DIR': '.',
        'AUDIO_DOWNLOAD_DIR': '%%DOWNLOAD_DIR',
        'TEMP_DIR': '%%DOWNLOAD_DIR',
        'DOWNLOAD_DIRS_INDEXABLE': 'false',
        'CUSTOM_DIRS': 'true',
        'CREATE_CUSTOM_DIRS': 'true',
        'CUSTOM_DIRS_EXCLUDE_REGEX': r'(^|/)[.@].*$',
        'DELETE_FILE_ON_TRASHCAN': 'false',
        'STATE_DIR': '.',
        'URL_PREFIX': '',
        'PUBLIC_HOST_URL': 'download/',
        'PUBLIC_HOST_AUDIO_URL': 'audio_download/',
        'OUTPUT_TEMPLATE': '%(title)s.%(ext)s',
        'OUTPUT_TEMPLATE_CHAPTER': '%(title)s - %(section_number)02d - %(section_title)s.%(ext)s',
        'OUTPUT_TEMPLATE_PLAYLIST': '%(playlist_title)s/%(title)s.%(ext)s',
        'OUTPUT_TEMPLATE_CHANNEL': '%(channel)s/%(title)s.%(ext)s',
        'DEFAULT_OPTION_PLAYLIST_ITEM_LIMIT' : '0',
        'CLEAR_COMPLETED_AFTER': '0',
        'YTDL_OPTIONS': '{}',
        'YTDL_OPTIONS_FILE': '',
        'ROBOTS_TXT': '',
        'HOST': '0.0.0.0',
        'PORT': '8081',
        'HTTPS': 'false',
        'CERTFILE': '',
        'KEYFILE': '',
        'BASE_DIR': '',
        'DEFAULT_THEME': 'auto',
        'MAX_CONCURRENT_DOWNLOADS': 3,
        'LOGLEVEL': 'INFO',
        'ENABLE_ACCESSLOG': 'false',
    }

    _BOOLEAN = ('DOWNLOAD_DIRS_INDEXABLE', 'CUSTOM_DIRS', 'CREATE_CUSTOM_DIRS', 'DELETE_FILE_ON_TRASHCAN', 'HTTPS', 'ENABLE_ACCESSLOG')

    def __init__(self):
        for k, v in self._DEFAULTS.items():
            setattr(self, k, os.environ.get(k, v))

        for k, v in self.__dict__.items():
            if isinstance(v, str) and v.startswith('%%'):
                setattr(self, k, getattr(self, v[2:]))
            if k in self._BOOLEAN:
                if v not in ('true', 'false', 'True', 'False', 'on', 'off', '1', '0'):
                    log.error(f'Environment variable "{k}" is set to a non-boolean value "{v}"')
                    sys.exit(1)
                setattr(self, k, v in ('true', 'True', 'on', '1'))

        if not self.URL_PREFIX.endswith('/'):
            self.URL_PREFIX += '/'

        # Convert relative addresses to absolute addresses to prevent the failure of file address comparison
        if self.YTDL_OPTIONS_FILE and self.YTDL_OPTIONS_FILE.startswith('.'):
            self.YTDL_OPTIONS_FILE = str(Path(self.YTDL_OPTIONS_FILE).resolve())

        self._runtime_overrides = {}

        success,_ = self.load_ytdl_options()
        if not success:
            sys.exit(1)

    def set_runtime_override(self, key, value):
        self._runtime_overrides[key] = value
        self.YTDL_OPTIONS[key] = value

    def remove_runtime_override(self, key):
        self._runtime_overrides.pop(key, None)
        self.YTDL_OPTIONS.pop(key, None)

    def _apply_runtime_overrides(self):
        self.YTDL_OPTIONS.update(self._runtime_overrides)

    # Keys sent to the browser. Sensitive or server-only keys (YTDL_OPTIONS,
    # paths, TLS config, etc.) are intentionally excluded.
    _FRONTEND_KEYS = (
        'CUSTOM_DIRS',
        'CREATE_CUSTOM_DIRS',
        'OUTPUT_TEMPLATE_CHAPTER',
        'PUBLIC_HOST_URL',
        'PUBLIC_HOST_AUDIO_URL',
        'DEFAULT_OPTION_PLAYLIST_ITEM_LIMIT',
    )

    def frontend_safe(self) -> dict:
        """Return only the config keys that are safe to expose to browser clients.

        Sensitive or server-only keys (YTDL_OPTIONS, file-system paths, TLS
        settings, etc.) are intentionally excluded.
        """
        return {k: getattr(self, k) for k in self._FRONTEND_KEYS}

    def load_ytdl_options(self) -> tuple[bool, str]:
        try:
            self.YTDL_OPTIONS = json.loads(os.environ.get('YTDL_OPTIONS', '{}'))
            assert isinstance(self.YTDL_OPTIONS, dict)
        except (json.decoder.JSONDecodeError, AssertionError):
            msg = 'Environment variable YTDL_OPTIONS is invalid'
            log.error(msg)
            return (False, msg)

        if not self.YTDL_OPTIONS_FILE:
            self._apply_runtime_overrides()
            return (True, '')

        log.info(f'Loading yt-dlp custom options from "{self.YTDL_OPTIONS_FILE}"')
        if not os.path.exists(self.YTDL_OPTIONS_FILE):
            msg = f'File "{self.YTDL_OPTIONS_FILE}" not found'
            log.error(msg)
            return (False, msg)
        try:
            with open(self.YTDL_OPTIONS_FILE) as json_data:
                opts = json.load(json_data)
            assert isinstance(opts, dict)
        except (json.decoder.JSONDecodeError, AssertionError):
            msg = 'YTDL_OPTIONS_FILE contents is invalid'
            log.error(msg)
            return (False, msg)

        self.YTDL_OPTIONS.update(opts)
        self._apply_runtime_overrides()
        return (True, '')

config = Config()
# Align root logger level with Config (keeps a single source of truth).
# This re-applies the log level after Config loads, in case LOGLEVEL was
# overridden by config file settings or differs from the environment variable.
logging.getLogger().setLevel(parseLogLevel(str(config.LOGLEVEL)) or logging.INFO)

class ObjectSerializer(json.JSONEncoder):
    def default(self, obj):
        # First try to use __dict__ for custom objects
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        # Convert iterables (generators, dict_items, etc.) to lists
        # Exclude strings and bytes which are also iterable
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
            try:
                return list(obj)
            except:
                pass
        # Fall back to default behavior
        return json.JSONEncoder.default(self, obj)

serializer = ObjectSerializer()
app = web.Application()
sio = socketio.AsyncServer(cors_allowed_origins='*')
sio.attach(app, socketio_path=config.URL_PREFIX + 'socket.io')
routes = web.RouteTableDef()
VALID_SUBTITLE_FORMATS = {'srt', 'txt', 'vtt', 'ttml', 'sbv', 'scc', 'dfxp'}
VALID_SUBTITLE_MODES = {'auto_only', 'manual_only', 'prefer_manual', 'prefer_auto'}
SUBTITLE_LANGUAGE_RE = re.compile(r'^[A-Za-z0-9][A-Za-z0-9-]{0,34}$')
VALID_DOWNLOAD_TYPES = {'video', 'audio', 'captions', 'thumbnail'}
VALID_VIDEO_CODECS = {'auto', 'h264', 'h265', 'av1', 'vp9'}
VALID_VIDEO_FORMATS = {'any', 'mp4', 'ios'}
VALID_AUDIO_FORMATS = {'m4a', 'mp3', 'opus', 'wav', 'flac'}
VALID_THUMBNAIL_FORMATS = {'jpg'}


def _migrate_legacy_request(post: dict) -> dict:
    """
    BACKWARD COMPATIBILITY: Translate old API request schema into the new one.

    Old API:
      format (any/mp4/m4a/mp3/opus/wav/flac/thumbnail/captions)
      quality
      video_codec
      subtitle_format (only when format=captions)

    New API:
      download_type (video/audio/captions/thumbnail)
      codec
      format
      quality
    """
    if "download_type" in post:
        return post

    old_format = str(post.get("format") or "any").strip().lower()
    old_quality = str(post.get("quality") or "best").strip().lower()
    old_video_codec = str(post.get("video_codec") or "auto").strip().lower()

    if old_format in VALID_AUDIO_FORMATS:
        post["download_type"] = "audio"
        post["codec"] = "auto"
        post["format"] = old_format
    elif old_format == "thumbnail":
        post["download_type"] = "thumbnail"
        post["codec"] = "auto"
        post["format"] = "jpg"
        post["quality"] = "best"
    elif old_format == "captions":
        post["download_type"] = "captions"
        post["codec"] = "auto"
        post["format"] = str(post.get("subtitle_format") or "srt").strip().lower()
        post["quality"] = "best"
    else:
        # old_format is usually any/mp4 (legacy video path)
        post["download_type"] = "video"
        post["codec"] = old_video_codec
        if old_quality == "best_ios":
            post["format"] = "ios"
            post["quality"] = "best"
        elif old_quality == "audio":
            # Legacy "audio only" under video format maps to m4a audio.
            post["download_type"] = "audio"
            post["codec"] = "auto"
            post["format"] = "m4a"
            post["quality"] = "best"
        else:
            post["format"] = old_format
            post["quality"] = old_quality

    return post

class Notifier(DownloadQueueNotifier):
    async def added(self, dl):
        log.info(f"Notifier: Download added - {dl.title}")
        await sio.emit('added', serializer.encode(dl))

    async def updated(self, dl):
        log.debug(f"Notifier: Download updated - {dl.title}")
        await sio.emit('updated', serializer.encode(dl))

    async def completed(self, dl):
        log.info(f"Notifier: Download completed - {dl.title}")
        await sio.emit('completed', serializer.encode(dl))

    async def canceled(self, id):
        log.info(f"Notifier: Download canceled - {id}")
        await sio.emit('canceled', serializer.encode(id))

    async def cleared(self, id):
        log.info(f"Notifier: Download cleared - {id}")
        await sio.emit('cleared', serializer.encode(id))

dqueue = DownloadQueue(config, Notifier())
app.on_startup.append(lambda app: dqueue.initialize())

class FileOpsFilter(DefaultFilter):
    def __call__(self, change_type: int, path: str) -> bool:
        # Check if this path matches our YTDL_OPTIONS_FILE
        if path != config.YTDL_OPTIONS_FILE:
            return False

        # For existing files, use samefile comparison to handle symlinks correctly
        if os.path.exists(config.YTDL_OPTIONS_FILE):
            try:
                if not os.path.samefile(path, config.YTDL_OPTIONS_FILE):
                    return False
            except (OSError, IOError):
                # If samefile fails, fall back to string comparison
                if path != config.YTDL_OPTIONS_FILE:
                    return False

        # Accept all change types for our file: modified, added, deleted
        return change_type in (Change.modified, Change.added, Change.deleted)

def get_options_update_time(success=True, msg=''):
    result = {
        'success': success,
        'msg': msg,
        'update_time': None
    }

    # Only try to get file modification time if YTDL_OPTIONS_FILE is set and file exists
    if config.YTDL_OPTIONS_FILE and os.path.exists(config.YTDL_OPTIONS_FILE):
        try:
            result['update_time'] = os.path.getmtime(config.YTDL_OPTIONS_FILE)
        except (OSError, IOError) as e:
            log.warning(f"Could not get modification time for {config.YTDL_OPTIONS_FILE}: {e}")
            result['update_time'] = None

    return result

async def watch_files():
    async def _watch_files():
        async for changes in awatch(config.YTDL_OPTIONS_FILE, watch_filter=FileOpsFilter()):
            success, msg = config.load_ytdl_options()
            result = get_options_update_time(success, msg)
            await sio.emit('ytdl_options_changed', serializer.encode(result))

    log.info(f'Starting Watch File: {config.YTDL_OPTIONS_FILE}')
    asyncio.create_task(_watch_files())

if config.YTDL_OPTIONS_FILE:
    app.on_startup.append(lambda app: watch_files())

@routes.post(config.URL_PREFIX + 'add')
async def add(request):
    log.info("Received request to add download")
    post = await request.json()
    post = _migrate_legacy_request(post)
    log.info(f"Request data: {post}")
    url = post.get('url')
    download_type = post.get('download_type')
    codec = post.get('codec')
    format = post.get('format')
    quality = post.get('quality')
    if not url or not quality or not download_type:
        log.error("Bad request: missing 'url', 'download_type', or 'quality'")
        raise web.HTTPBadRequest()
    folder = post.get('folder')
    custom_name_prefix = post.get('custom_name_prefix')
    playlist_item_limit = post.get('playlist_item_limit')
    auto_start = post.get('auto_start')
    split_by_chapters = post.get('split_by_chapters')
    chapter_template = post.get('chapter_template')
    subtitle_language = post.get('subtitle_language')
    subtitle_mode = post.get('subtitle_mode')

    if custom_name_prefix is None:
        custom_name_prefix = ''
    if custom_name_prefix and ('..' in custom_name_prefix or custom_name_prefix.startswith('/') or custom_name_prefix.startswith('\\')):
        raise web.HTTPBadRequest(reason='custom_name_prefix must not contain ".." or start with a path separator')
    if auto_start is None:
        auto_start = True
    if playlist_item_limit is None:
        playlist_item_limit = config.DEFAULT_OPTION_PLAYLIST_ITEM_LIMIT
    if split_by_chapters is None:
        split_by_chapters = False
    if chapter_template is None:
        chapter_template = config.OUTPUT_TEMPLATE_CHAPTER
    if subtitle_language is None:
        subtitle_language = 'en'
    if subtitle_mode is None:
        subtitle_mode = 'prefer_manual'
    download_type = str(download_type).strip().lower()
    codec = str(codec or 'auto').strip().lower()
    format = str(format or '').strip().lower()
    quality = str(quality).strip().lower()
    subtitle_language = str(subtitle_language).strip()
    subtitle_mode = str(subtitle_mode).strip()

    if chapter_template and ('..' in chapter_template or chapter_template.startswith('/') or chapter_template.startswith('\\')):
        raise web.HTTPBadRequest(reason='chapter_template must not contain ".." or start with a path separator')
    if not SUBTITLE_LANGUAGE_RE.fullmatch(subtitle_language):
        raise web.HTTPBadRequest(reason='subtitle_language must match pattern [A-Za-z0-9-] and be at most 35 characters')
    if subtitle_mode not in VALID_SUBTITLE_MODES:
        raise web.HTTPBadRequest(reason=f'subtitle_mode must be one of {sorted(VALID_SUBTITLE_MODES)}')

    if download_type not in VALID_DOWNLOAD_TYPES:
        raise web.HTTPBadRequest(reason=f'download_type must be one of {sorted(VALID_DOWNLOAD_TYPES)}')
    if codec not in VALID_VIDEO_CODECS:
        raise web.HTTPBadRequest(reason=f'codec must be one of {sorted(VALID_VIDEO_CODECS)}')

    if download_type == 'video':
        if format not in VALID_VIDEO_FORMATS:
            raise web.HTTPBadRequest(reason=f'format must be one of {sorted(VALID_VIDEO_FORMATS)} for video')
        if quality not in {'best', 'worst', '2160', '1440', '1080', '720', '480', '360', '240'}:
            raise web.HTTPBadRequest(reason="quality must be one of ['best', '2160', '1440', '1080', '720', '480', '360', '240', 'worst'] for video")
    elif download_type == 'audio':
        if format not in VALID_AUDIO_FORMATS:
            raise web.HTTPBadRequest(reason=f'format must be one of {sorted(VALID_AUDIO_FORMATS)} for audio')
        allowed_audio_qualities = {'best'}
        if format == 'mp3':
            allowed_audio_qualities |= {'320', '192', '128'}
        elif format == 'm4a':
            allowed_audio_qualities |= {'192', '128'}
        if quality not in allowed_audio_qualities:
            raise web.HTTPBadRequest(reason=f'quality must be one of {sorted(allowed_audio_qualities)} for format {format}')
        codec = 'auto'
    elif download_type == 'captions':
        if format not in VALID_SUBTITLE_FORMATS:
            raise web.HTTPBadRequest(reason=f'format must be one of {sorted(VALID_SUBTITLE_FORMATS)} for captions')
        quality = 'best'
        codec = 'auto'
    elif download_type == 'thumbnail':
        if format not in VALID_THUMBNAIL_FORMATS:
            raise web.HTTPBadRequest(reason=f'format must be one of {sorted(VALID_THUMBNAIL_FORMATS)} for thumbnail')
        quality = 'best'
        codec = 'auto'

    playlist_item_limit = int(playlist_item_limit)

    status = await dqueue.add(
        url,
        download_type,
        codec,
        format,
        quality,
        folder,
        custom_name_prefix,
        playlist_item_limit,
        auto_start,
        split_by_chapters,
        chapter_template,
        subtitle_language,
        subtitle_mode,
    )
    return web.Response(text=serializer.encode(status))

@routes.post(config.URL_PREFIX + 'cancel-add')
async def cancel_add(request):
    dqueue.cancel_add()
    return web.Response(text=serializer.encode({'status': 'ok'}), content_type='application/json')

@routes.post(config.URL_PREFIX + 'delete')
async def delete(request):
    post = await request.json()
    ids = post.get('ids')
    where = post.get('where')
    if not ids or where not in ['queue', 'done']:
        log.error("Bad request: missing 'ids' or incorrect 'where' value")
        raise web.HTTPBadRequest()
    status = await (dqueue.cancel(ids) if where == 'queue' else dqueue.clear(ids))
    log.info(f"Download delete request processed for ids: {ids}, where: {where}")
    return web.Response(text=serializer.encode(status))

@routes.post(config.URL_PREFIX + 'start')
async def start(request):
    post = await request.json()
    ids = post.get('ids')
    log.info(f"Received request to start pending downloads for ids: {ids}")
    status = await dqueue.start_pending(ids)
    return web.Response(text=serializer.encode(status))


COOKIES_PATH = os.path.join(config.STATE_DIR, 'cookies.txt')

@routes.post(config.URL_PREFIX + 'upload-cookies')
async def upload_cookies(request):
    reader = await request.multipart()
    field = await reader.next()
    if field is None or field.name != 'cookies':
        return web.Response(status=400, text=serializer.encode({'status': 'error', 'msg': 'No cookies file provided'}))
    size = 0
    with open(COOKIES_PATH, 'wb') as f:
        while True:
            chunk = await field.read_chunk()
            if not chunk:
                break
            size += len(chunk)
            if size > 1_000_000:  # 1MB limit
                os.remove(COOKIES_PATH)
                return web.Response(status=400, text=serializer.encode({'status': 'error', 'msg': 'Cookie file too large (max 1MB)'}))
            f.write(chunk)
    config.set_runtime_override('cookiefile', COOKIES_PATH)
    log.info(f'Cookies file uploaded ({size} bytes)')
    return web.Response(text=serializer.encode({'status': 'ok', 'msg': f'Cookies uploaded ({size} bytes)'}))

@routes.post(config.URL_PREFIX + 'delete-cookies')
async def delete_cookies(request):
    has_uploaded_cookies = os.path.exists(COOKIES_PATH)
    configured_cookiefile = config.YTDL_OPTIONS.get('cookiefile')
    has_manual_cookiefile = isinstance(configured_cookiefile, str) and configured_cookiefile and configured_cookiefile != COOKIES_PATH

    if not has_uploaded_cookies:
        if has_manual_cookiefile:
            return web.Response(
                status=400,
                text=serializer.encode({
                    'status': 'error',
                    'msg': 'Cookies are configured manually via YTDL_OPTIONS (cookiefile). Remove or change that setting manually; UI delete only removes uploaded cookies.'
                })
            )
        return web.Response(status=400, text=serializer.encode({'status': 'error', 'msg': 'No uploaded cookies to delete'}))

    os.remove(COOKIES_PATH)
    config.remove_runtime_override('cookiefile')
    success, msg = config.load_ytdl_options()
    if not success:
        log.error(f'Cookies file deleted, but failed to reload YTDL_OPTIONS: {msg}')
        return web.Response(status=500, text=serializer.encode({'status': 'error', 'msg': f'Cookies file deleted, but failed to reload YTDL_OPTIONS: {msg}'}))

    log.info('Cookies file deleted')
    return web.Response(text=serializer.encode({'status': 'ok'}))

@routes.get(config.URL_PREFIX + 'cookie-status')
async def cookie_status(request):
    configured_cookiefile = config.YTDL_OPTIONS.get('cookiefile')
    has_configured_cookies = isinstance(configured_cookiefile, str) and os.path.exists(configured_cookiefile)
    has_uploaded_cookies = os.path.exists(COOKIES_PATH)
    exists = has_uploaded_cookies or has_configured_cookies
    return web.Response(text=serializer.encode({'status': 'ok', 'has_cookies': exists}))

@routes.get(config.URL_PREFIX + 'history')
async def history(request):
    history = { 'done': [], 'queue': [], 'pending': []}

    for _, v in dqueue.queue.saved_items():
        history['queue'].append(v)
    for _, v in dqueue.done.saved_items():
        history['done'].append(v)
    for _, v in dqueue.pending.saved_items():
        history['pending'].append(v)

    log.info("Sending download history")
    return web.Response(text=serializer.encode(history))

@sio.event
async def connect(sid, environ):
    log.info(f"Client connected: {sid}")
    await sio.emit('all', serializer.encode(dqueue.get()), to=sid)
    await sio.emit('configuration', serializer.encode(config.frontend_safe()), to=sid)
    if config.CUSTOM_DIRS:
        await sio.emit('custom_dirs', serializer.encode(get_custom_dirs()), to=sid)
    if config.YTDL_OPTIONS_FILE:
        await sio.emit('ytdl_options_changed', serializer.encode(get_options_update_time()), to=sid)

def get_custom_dirs():
    def recursive_dirs(base):
        path = pathlib.Path(base)

        # Converts PosixPath object to string, and remove base/ prefix
        def convert(p):
            s = str(p)
            if s.startswith(base):
                s = s[len(base):]

            if s.startswith('/'):
                s = s[1:]

            return s

        # Include only directories which do not match the exclude filter
        def include_dir(d):
            if len(config.CUSTOM_DIRS_EXCLUDE_REGEX) == 0:
                return True
            else:
                return re.search(config.CUSTOM_DIRS_EXCLUDE_REGEX, d) is None

        # Recursively lists all subdirectories of DOWNLOAD_DIR.
        # Always include '' (the base directory itself) even when the
        # directory is empty or does not yet exist.
        dirs = list(filter(include_dir, map(convert, path.glob('**/'))))
        if '' not in dirs:
            dirs.insert(0, '')

        return dirs

    download_dir = recursive_dirs(config.DOWNLOAD_DIR)

    audio_download_dir = download_dir
    if config.DOWNLOAD_DIR != config.AUDIO_DOWNLOAD_DIR:
        audio_download_dir = recursive_dirs(config.AUDIO_DOWNLOAD_DIR)

    return {
        "download_dir": download_dir,
        "audio_download_dir": audio_download_dir
    }

@routes.get(config.URL_PREFIX)
def index(request):
    response = web.FileResponse(os.path.join(config.BASE_DIR, 'ui/dist/metube/browser/index.html'))
    if 'metube_theme' not in request.cookies:
        response.set_cookie('metube_theme', config.DEFAULT_THEME)
    return response

@routes.get(config.URL_PREFIX + 'robots.txt')
def robots(request):
    if config.ROBOTS_TXT:
        response = web.FileResponse(os.path.join(config.BASE_DIR, config.ROBOTS_TXT))
    else:
        response = web.Response(
            text="User-agent: *\nDisallow: /download/\nDisallow: /audio_download/\n"
        )
    return response

@routes.get(config.URL_PREFIX + 'version')
def version(request):
    return web.json_response({
        "yt-dlp": yt_dlp_version,
        "version": os.getenv("METUBE_VERSION", "dev")
    })

if config.URL_PREFIX != '/':
    @routes.get('/')
    def index_redirect_root(request):
        return web.HTTPFound(config.URL_PREFIX)

    @routes.get(config.URL_PREFIX[:-1])
    def index_redirect_dir(request):
        return web.HTTPFound(config.URL_PREFIX)

routes.static(config.URL_PREFIX + 'download/', config.DOWNLOAD_DIR, show_index=config.DOWNLOAD_DIRS_INDEXABLE)
routes.static(config.URL_PREFIX + 'audio_download/', config.AUDIO_DOWNLOAD_DIR, show_index=config.DOWNLOAD_DIRS_INDEXABLE)
routes.static(config.URL_PREFIX, os.path.join(config.BASE_DIR, 'ui/dist/metube/browser'))
try:
    app.add_routes(routes)
except ValueError as e:
    if 'ui/dist/metube/browser' in str(e):
        raise RuntimeError('Could not find the frontend UI static assets. Please run `node_modules/.bin/ng build` inside the ui folder') from e
    raise e

# https://github.com/aio-libs/aiohttp/pull/4615 waiting for release
# @routes.options(config.URL_PREFIX + 'add')
async def add_cors(request):
    return web.Response(text=serializer.encode({"status": "ok"}))

app.router.add_route('OPTIONS', config.URL_PREFIX + 'add', add_cors)
app.router.add_route('OPTIONS', config.URL_PREFIX + 'cancel-add', add_cors)
app.router.add_route('OPTIONS', config.URL_PREFIX + 'upload-cookies', add_cors)
app.router.add_route('OPTIONS', config.URL_PREFIX + 'delete-cookies', add_cors)

async def on_prepare(request, response):
    if 'Origin' in request.headers:
        response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

app.on_response_prepare.append(on_prepare)

def supports_reuse_port():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        sock.close()
        return True
    except (AttributeError, OSError):
        return False

def isAccessLogEnabled():
    if config.ENABLE_ACCESSLOG:
        return access_logger
    else:
        return None

if __name__ == '__main__':
    logging.getLogger().setLevel(parseLogLevel(config.LOGLEVEL) or logging.INFO)
    log.info(f"Listening on {config.HOST}:{config.PORT}")


    # Auto-detect cookie file on startup
    if os.path.exists(COOKIES_PATH):
        config.set_runtime_override('cookiefile', COOKIES_PATH)
        log.info(f'Cookie file detected at {COOKIES_PATH}')

    if config.HTTPS:
        ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_context.load_cert_chain(certfile=config.CERTFILE, keyfile=config.KEYFILE)
        web.run_app(app, host=config.HOST, port=int(config.PORT), reuse_port=supports_reuse_port(), ssl_context=ssl_context, access_log=isAccessLogEnabled())
    else:
        web.run_app(app, host=config.HOST, port=int(config.PORT), reuse_port=supports_reuse_port(), access_log=isAccessLogEnabled())
```

## File: `app/ytdl.py`
```python
import os
import shutil
import yt_dlp
from collections import OrderedDict
import shelve
import time
import asyncio
import multiprocessing
import logging
import re
import types
import dbm
import subprocess
from typing import Any
from functools import lru_cache

import yt_dlp.networking.impersonate
from yt_dlp.utils import STR_FORMAT_RE_TMPL, STR_FORMAT_TYPES
from dl_formats import get_format, get_opts, AUDIO_FORMATS
from datetime import datetime

log = logging.getLogger('ytdl')


@lru_cache(maxsize=None)
def _compile_outtmpl_pattern(field: str) -> re.Pattern:
    """Compile a regex pattern to match a specific field in an output template, including optional format specifiers."""
    conversion_types = f"[{re.escape(STR_FORMAT_TYPES)}]"
    return re.compile(STR_FORMAT_RE_TMPL.format(re.escape(field), conversion_types))


# Characters that are invalid in Windows/NTFS path components. These are pre-
# sanitised when substituting playlist/channel titles into output templates so
# that downloads do not fail on NTFS-mounted volumes or Windows Docker hosts.
_WINDOWS_INVALID_PATH_CHARS = re.compile(r'[\\:*?"<>|]')


def _sanitize_path_component(value: Any) -> Any:
    """Replace characters that are invalid in Windows path components with '_'.

    Non-string values (int, float, None, …) are passed through unchanged so
    that ``_outtmpl_substitute_field`` can still coerce them with format specs
    (e.g. ``%(playlist_index)02d``).  Only string values are sanitised because
    Windows-invalid characters are only a concern for human-readable strings
    (titles, channel names, etc.) that may end up as directory names.
    """
    if not isinstance(value, str):
        return value
    return _WINDOWS_INVALID_PATH_CHARS.sub('_', value)


def _outtmpl_substitute_field(template: str, field: str, value: Any) -> str:
    """Substitute a single field in an output template, applying any format specifiers to the value."""
    pattern = _compile_outtmpl_pattern(field)

    def replacement(match: re.Match) -> str:
        if match.group("has_key") is None:
            return match.group(0)

        prefix = match.group("prefix") or ""
        format_spec = match.group("format")

        if not format_spec:
            return f"{prefix}{value}"

        conversion_type = format_spec[-1]
        try:
            if conversion_type in "diouxX":
                coerced_value = int(value)
            elif conversion_type in "eEfFgG":
                coerced_value = float(value)
            else:
                coerced_value = value

            return f"{prefix}{('%' + format_spec) % coerced_value}"
        except (ValueError, TypeError):
            return f"{prefix}{value}"

    return pattern.sub(replacement, template)

def _convert_generators_to_lists(obj):
    """Recursively convert generators to lists in a dictionary to make it pickleable."""
    if isinstance(obj, types.GeneratorType):
        return list(obj)
    elif isinstance(obj, dict):
        return {k: _convert_generators_to_lists(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return type(obj)(_convert_generators_to_lists(item) for item in obj)
    else:
        return obj


def _convert_srt_to_txt_file(subtitle_path: str):
    """Convert an SRT subtitle file into plain text by stripping cue numbers/timestamps."""
    txt_path = os.path.splitext(subtitle_path)[0] + ".txt"
    try:
        with open(subtitle_path, "r", encoding="utf-8", errors="replace") as infile:
            content = infile.read()

        # Normalize newlines so cue splitting is consistent across platforms.
        content = content.replace("\r\n", "\n").replace("\r", "\n")
        cues = []
        for block in re.split(r"\n{2,}", content):
            lines = [line.strip() for line in block.split("\n") if line.strip()]
            if not lines:
                continue
            if re.fullmatch(r"\d+", lines[0]):
                lines = lines[1:]
            if lines and "-->" in lines[0]:
                lines = lines[1:]

            text_lines = []
            for line in lines:
                if "-->" in line:
                    continue
                clean_line = re.sub(r"<[^>]+>", "", line).strip()
                if clean_line:
                    text_lines.append(clean_line)
            if text_lines:
                cues.append(" ".join(text_lines))

        with open(txt_path, "w", encoding="utf-8") as outfile:
            if cues:
                outfile.write("\n".join(cues))
                outfile.write("\n")
        return txt_path
    except OSError as exc:
        log.warning(f"Failed to convert subtitle file {subtitle_path} to txt: {exc}")
        return None

class DownloadQueueNotifier:
    async def added(self, dl):
        raise NotImplementedError

    async def updated(self, dl):
        raise NotImplementedError

    async def completed(self, dl):
        raise NotImplementedError

    async def canceled(self, id):
        raise NotImplementedError

    async def cleared(self, id):
        raise NotImplementedError

class DownloadInfo:
    def __init__(
        self,
        id,
        title,
        url,
        quality,
        download_type,
        codec,
        format,
        folder,
        custom_name_prefix,
        error,
        entry,
        playlist_item_limit,
        split_by_chapters,
        chapter_template,
        subtitle_language="en",
        subtitle_mode="prefer_manual",
    ):
        self.id = id if len(custom_name_prefix) == 0 else f'{custom_name_prefix}.{id}'
        self.title = title if len(custom_name_prefix) == 0 else f'{custom_name_prefix}.{title}'
        self.url = url
        self.quality = quality
        self.download_type = download_type
        self.codec = codec
        self.format = format
        self.folder = folder
        self.custom_name_prefix = custom_name_prefix
        self.msg = self.percent = self.speed = self.eta = None
        self.status = "pending"
        self.size = None
        self.timestamp = time.time_ns()
        self.error = error
        # Convert generators to lists to make entry pickleable
        self.entry = _convert_generators_to_lists(entry) if entry is not None else None
        self.playlist_item_limit = playlist_item_limit
        self.split_by_chapters = split_by_chapters
        self.chapter_template = chapter_template
        self.subtitle_language = subtitle_language
        self.subtitle_mode = subtitle_mode
        self.subtitle_files = []

    def __setstate__(self, state):
        """BACKWARD COMPATIBILITY: migrate old DownloadInfo from persistent queue files."""
        self.__dict__.update(state)
        if 'download_type' not in state:
            old_format = state.get('format', 'any')
            old_video_codec = state.get('video_codec', 'auto')
            old_quality = state.get('quality', 'best')
            old_subtitle_format = state.get('subtitle_format', 'srt')

            if old_format in AUDIO_FORMATS:
                self.download_type = 'audio'
                self.codec = 'auto'
            elif old_format == 'thumbnail':
                self.download_type = 'thumbnail'
                self.codec = 'auto'
                self.format = 'jpg'
            elif old_format == 'captions':
                self.download_type = 'captions'
                self.codec = 'auto'
                self.format = old_subtitle_format
            else:
                self.download_type = 'video'
                self.codec = old_video_codec
                if old_quality == 'best_ios':
                    self.format = 'ios'
                    self.quality = 'best'
                elif old_quality == 'audio':
                    self.download_type = 'audio'
                    self.codec = 'auto'
                    self.format = 'm4a'
                    self.quality = 'best'
            self.__dict__.pop('video_codec', None)
            self.__dict__.pop('subtitle_format', None)

        if not getattr(self, "codec", None):
            self.codec = "auto"
        if not hasattr(self, "subtitle_files"):
            self.subtitle_files = []

class Download:
    manager = None

    def __init__(self, download_dir, temp_dir, output_template, output_template_chapter, quality, format, ytdl_opts, info):
        self.download_dir = download_dir
        self.temp_dir = temp_dir
        self.output_template = output_template
        self.output_template_chapter = output_template_chapter
        self.info = info
        self.format = get_format(
            getattr(info, 'download_type', 'video'),
            getattr(info, 'codec', 'auto'),
            format,
            quality,
        )
        self.ytdl_opts = get_opts(
            getattr(info, 'download_type', 'video'),
            getattr(info, 'codec', 'auto'),
            format,
            quality,
            ytdl_opts,
            subtitle_language=getattr(info, 'subtitle_language', 'en'),
            subtitle_mode=getattr(info, 'subtitle_mode', 'prefer_manual'),
        )
        if "impersonate" in self.ytdl_opts:
            self.ytdl_opts["impersonate"] = yt_dlp.networking.impersonate.ImpersonateTarget.from_str(self.ytdl_opts["impersonate"])
        self.canceled = False
        self.tmpfilename = None
        self.status_queue = None
        self.proc = None
        self.loop = None
        self.notifier = None

    def _download(self):
        log.info(f"Starting download for: {self.info.title} ({self.info.url})")
        try:
            debug_logging = logging.getLogger().isEnabledFor(logging.DEBUG)
            def put_status(st):
                self.status_queue.put({k: v for k, v in st.items() if k in (
                    'tmpfilename',
                    'filename',
                    'status',
                    'msg',
                    'total_bytes',
                    'total_bytes_estimate',
                    'downloaded_bytes',
                    'speed',
                    'eta',
                )})

            def put_status_postprocessor(d):
                if d['postprocessor'] == 'MoveFiles' and d['status'] == 'finished':
                    filepath = d['info_dict']['filepath']
                    if '__finaldir' in d['info_dict']:
                        finaldir = d['info_dict']['__finaldir']
                        filename = os.path.join(finaldir, os.path.basename(filepath))
                    else:
                        filename = filepath
                    self.status_queue.put({'status': 'finished', 'filename': filename})
                    # For captions-only downloads, yt-dlp may still report a media-like
                    # filepath in MoveFiles. Capture subtitle outputs explicitly so the
                    # UI can link to real caption files.
                    if getattr(self.info, 'download_type', '') == 'captions':
                        requested_subtitles = d.get('info_dict', {}).get('requested_subtitles', {}) or {}
                        for subtitle in requested_subtitles.values():
                            if isinstance(subtitle, dict) and subtitle.get('filepath'):
                                self.status_queue.put({'subtitle_file': subtitle['filepath']})

                # Capture all chapter files when SplitChapters finishes
                elif d.get('postprocessor') == 'SplitChapters' and d.get('status') == 'finished':
                    chapters = d.get('info_dict', {}).get('chapters', [])
                    if chapters:
                        for chapter in chapters:
                            if isinstance(chapter, dict) and 'filepath' in chapter:
                                log.info(f"Captured chapter file: {chapter['filepath']}")
                                self.status_queue.put({'chapter_file': chapter['filepath']})
                    else:
                        log.warning("SplitChapters finished but no chapter files found in info_dict")

            ytdl_params = {
                'quiet': not debug_logging,
                'verbose': debug_logging,
                'no_color': True,
                'paths': {"home": self.download_dir, "temp": self.temp_dir},
                'outtmpl': { "default": self.output_template, "chapter": self.output_template_chapter },
                'format': self.format,
                'socket_timeout': 30,
                'ignore_no_formats_error': True,
                'progress_hooks': [put_status],
                'postprocessor_hooks': [put_status_postprocessor],
                **self.ytdl_opts,
            }

            # Add chapter splitting options if enabled
            if self.info.split_by_chapters:
                ytdl_params['outtmpl']['chapter'] = self.info.chapter_template
                if 'postprocessors' not in ytdl_params:
                    ytdl_params['postprocessors'] = []
                ytdl_params['postprocessors'].append({
                    'key': 'FFmpegSplitChapters',
                    'force_keyframes': False
                })

            ret = yt_dlp.YoutubeDL(params=ytdl_params).download([self.info.url])
            self.status_queue.put({'status': 'finished' if ret == 0 else 'error'})
            log.info(f"Finished download for: {self.info.title}")
        except yt_dlp.utils.YoutubeDLError as exc:
            log.error(f"Download error for {self.info.title}: {str(exc)}")
            self.status_queue.put({'status': 'error', 'msg': str(exc)})

    async def start(self, notifier):
        log.info(f"Preparing download for: {self.info.title}")
        if Download.manager is None:
            Download.manager = multiprocessing.Manager()
        self.status_queue = Download.manager.Queue()
        self.proc = multiprocessing.Process(target=self._download)
        self.proc.start()
        self.loop = asyncio.get_running_loop()
        self.notifier = notifier
        self.info.status = 'preparing'
        await self.notifier.updated(self.info)
        self.status_task = asyncio.create_task(self.update_status())
        await self.loop.run_in_executor(None, self.proc.join)
        # Signal update_status to stop and wait for it to finish
        # so that all status updates (including MoveFiles with correct
        # file size) are processed before _post_download_cleanup runs.
        if self.status_queue is not None:
            self.status_queue.put(None)
        await self.status_task

    def cancel(self):
        log.info(f"Cancelling download: {self.info.title}")
        if self.running():
            try:
                self.proc.kill()
            except Exception as e:
                log.error(f"Error killing process for {self.info.title}: {e}")
        self.canceled = True
        if self.status_queue is not None:
            self.status_queue.put(None)

    def close(self):
        log.info(f"Closing download process for: {self.info.title}")
        if self.started():
            self.proc.close()

    def running(self):
        try:
            return self.proc is not None and self.proc.is_alive()
        except ValueError:
            return False

    def started(self):
        return self.proc is not None

    async def update_status(self):
        while True:
            status = await self.loop.run_in_executor(None, self.status_queue.get)
            if status is None:
                log.info(f"Status update finished for: {self.info.title}")
                return
            if self.canceled:
                log.info(f"Download {self.info.title} is canceled; stopping status updates.")
                return
            self.tmpfilename = status.get('tmpfilename')
            if 'filename' in status:
                fileName = status.get('filename')
                rel_name = os.path.relpath(fileName, self.download_dir)
                # For captions mode, ignore media-like placeholders and let subtitle_file
                # statuses define the final file shown in the UI.
                if getattr(self.info, 'download_type', '') == 'captions':
                    requested_subtitle_format = str(getattr(self.info, 'format', '')).lower()
                    allowed_caption_exts = ('.txt',) if requested_subtitle_format == 'txt' else ('.vtt', '.srt', '.sbv', '.scc', '.ttml', '.dfxp')
                    if not rel_name.lower().endswith(allowed_caption_exts):
                        continue
                self.info.filename = rel_name
                self.info.size = os.path.getsize(fileName) if os.path.exists(fileName) else None
                if getattr(self.info, 'download_type', '') == 'thumbnail':
                    self.info.filename = re.sub(r'\.webm$', '.jpg', self.info.filename)

            # Handle chapter files
            log.debug(f"Update status for {self.info.title}: {status}")
            if 'chapter_file' in status:
                chapter_file = status.get('chapter_file')
                if not hasattr(self.info, 'chapter_files'):
                    self.info.chapter_files = []
                rel_path = os.path.relpath(chapter_file, self.download_dir)
                file_size = os.path.getsize(chapter_file) if os.path.exists(chapter_file) else None
                #Postprocessor hook called multiple times with chapters. Only insert if not already present.
                existing = next((cf for cf in self.info.chapter_files if cf['filename'] == rel_path), None)
                if not existing:
                    self.info.chapter_files.append({'filename': rel_path, 'size': file_size})
                # Skip the rest of status processing for chapter files
                continue

            if 'subtitle_file' in status:
                subtitle_file = status.get('subtitle_file')
                if not subtitle_file:
                    continue
                subtitle_output_file = subtitle_file

                # txt mode is derived from SRT by stripping cue metadata.
                if getattr(self.info, 'download_type', '') == 'captions' and str(getattr(self.info, 'format', '')).lower() == 'txt':
                    converted_txt = _convert_srt_to_txt_file(subtitle_file)
                    if converted_txt:
                        subtitle_output_file = converted_txt
                        if converted_txt != subtitle_file:
                            try:
                                os.remove(subtitle_file)
                            except OSError as exc:
                                log.debug(f"Could not remove temporary SRT file {subtitle_file}: {exc}")

                rel_path = os.path.relpath(subtitle_output_file, self.download_dir)
                file_size = os.path.getsize(subtitle_output_file) if os.path.exists(subtitle_output_file) else None
                existing = next((sf for sf in self.info.subtitle_files if sf['filename'] == rel_path), None)
                if not existing:
                    self.info.subtitle_files.append({'filename': rel_path, 'size': file_size})
                # Prefer first subtitle file as the primary result link in captions mode.
                if getattr(self.info, 'download_type', '') == 'captions' and (
                    not getattr(self.info, 'filename', None) or
                    str(getattr(self.info, 'format', '')).lower() == 'txt'
                ):
                    self.info.filename = rel_path
                    self.info.size = file_size
                continue

            self.info.status = status['status']
            self.info.msg = status.get('msg')
            if 'downloaded_bytes' in status:
                total = status.get('total_bytes') or status.get('total_bytes_estimate')
                if total:
                    self.info.percent = status['downloaded_bytes'] / total * 100
            self.info.speed = status.get('speed')
            self.info.eta = status.get('eta')
            log.debug(f"Updating status for {self.info.title}: {status}")
            await self.notifier.updated(self.info)

class PersistentQueue:
    def __init__(self, name, path):
        self.identifier = name
        pdir = os.path.dirname(path)
        if not os.path.isdir(pdir):
            os.mkdir(pdir)
        with shelve.open(path, 'c'):
            pass

        self.path = path
        self.repair()
        self.dict = OrderedDict()

    def load(self):
        for k, v in self.saved_items():
            self.dict[k] = Download(None, None, None, None, getattr(v, 'quality', 'best'), getattr(v, 'format', 'any'), {}, v)

    def exists(self, key):
        return key in self.dict

    def get(self, key):
        return self.dict[key]

    def items(self):
        return self.dict.items()

    def saved_items(self):
        with shelve.open(self.path, 'r') as shelf:
            return sorted(shelf.items(), key=lambda item: item[1].timestamp)

    def put(self, value):
        key = value.info.url
        self.dict[key] = value
        with shelve.open(self.path, 'w') as shelf:
            shelf[key] = value.info

    def delete(self, key):
        if key in self.dict:
            del self.dict[key]
            with shelve.open(self.path, 'w') as shelf:
                shelf.pop(key, None)

    def next(self):
        k, v = next(iter(self.dict.items()))
        return k, v

    def empty(self):
        return not bool(self.dict)

    def repair(self):
        # check DB format
        type_check = subprocess.run(
            ["file", self.path],
            capture_output=True,
            text=True
        )
        db_type = type_check.stdout.lower()

        # create backup (<queue>.old)
        try:
            shutil.copy2(self.path, f"{self.path}.old")
        except Exception as e:
            # if we cannot backup then its not safe to attempt a repair
            #  since it could be due to a filesystem error
            log.debug(f"PersistentQueue:{self.identifier} backup failed, skipping repair")
            return

        if "gnu dbm" in db_type:
            # perform gdbm repair
            log_prefix = f"PersistentQueue:{self.identifier} repair (dbm/file)"
            log.debug(f"{log_prefix} started")
            try:
                result = subprocess.run(
                    ["gdbmtool", self.path],
                    input="recover verbose summary\n",
                    text=True,
                    capture_output=True,
                    timeout=60
                )
                log.debug(f"{log_prefix} {result.stdout}")
                if result.stderr:
                    log.debug(f"{log_prefix} failed: {result.stderr}")
            except FileNotFoundError:
                log.debug(f"{log_prefix} failed: 'gdbmtool' was not found")

            # perform null key cleanup
            log_prefix = f"PersistentQueue:{self.identifier} repair (null keys)"
            log.debug(f"{log_prefix} started")
            deleted = 0
            try:
                with dbm.open(self.path, "w") as db:
                    for key in list(db.keys()):
                        if len(key) > 0 and all(b == 0x00 for b in key):
                            log.debug(f"{log_prefix} deleting key of length {len(key)} (all NUL bytes)")
                            del db[key]
                            deleted += 1
                log.debug(f"{log_prefix} done - deleted {deleted} key(s)")
            except dbm.error:
                log.debug(f"{log_prefix} failed: db type is dbm.gnu, but the module is not available (dbm.error; module support may be missing or the file may be corrupted)")

        elif "sqlite" in db_type:
            # perform sqlite3 recovery
            log_prefix = f"PersistentQueue:{self.identifier} repair (sqlite3/file)"
            log.debug(f"{log_prefix} started")
            try:
                result = subprocess.run(
                    f"sqlite3 {self.path} '.recover' | sqlite3 {self.path}.tmp",
                    capture_output=True,
                    text=True,
                    shell=True,
                    timeout=60
                )
                if result.stderr:
                    log.debug(f"{log_prefix} failed: {result.stderr}")
                else:
                    shutil.move(f"{self.path}.tmp", self.path)
                    log.debug(f"{log_prefix}{result.stdout or " was successful, no output"}")
            except FileNotFoundError:
                log.debug(f"{log_prefix} failed: 'sqlite3' was not found")

class DownloadQueue:
    def __init__(self, config, notifier):
        self.config = config
        self.notifier = notifier
        self.queue = PersistentQueue("queue", self.config.STATE_DIR + '/queue')
        self.done = PersistentQueue("completed", self.config.STATE_DIR + '/completed')
        self.pending = PersistentQueue("pending", self.config.STATE_DIR + '/pending')
        self.active_downloads = set()
        self.semaphore = asyncio.Semaphore(int(self.config.MAX_CONCURRENT_DOWNLOADS))
        self.done.load()
        self._add_generation = 0
        self._canceled_urls = set()  # URLs canceled during current playlist add

    def cancel_add(self):
        self._add_generation += 1
        log.info('Playlist add operation canceled by user')

    async def __import_queue(self):
        for k, v in self.queue.saved_items():
            await self.__add_download(v, True)

    async def __import_pending(self):
        for k, v in self.pending.saved_items():
            await self.__add_download(v, False)

    async def initialize(self):
        log.info("Initializing DownloadQueue")
        asyncio.create_task(self.__import_queue())
        asyncio.create_task(self.__import_pending())

    async def __start_download(self, download):
        if download.canceled:
            log.info(f"Download {download.info.title} was canceled, skipping start.")
            return
        async with self.semaphore:
            if download.canceled:
                log.info(f"Download {download.info.title} was canceled, skipping start.")
                return
            await download.start(self.notifier)
            self._post_download_cleanup(download)

    def _post_download_cleanup(self, download):
        if download.info.status != 'finished':
            if download.tmpfilename and os.path.isfile(download.tmpfilename):
                try:
                    os.remove(download.tmpfilename)
                except:
                    pass
            download.info.status = 'error'
        download.close()
        if self.queue.exists(download.info.url):
            self.queue.delete(download.info.url)
            if download.canceled:
                asyncio.create_task(self.notifier.canceled(download.info.url))
            else:
                self.done.put(download)
                asyncio.create_task(self.notifier.completed(download.info))
                try:
                    clear_after = int(self.config.CLEAR_COMPLETED_AFTER)
                except ValueError:
                    log.error(f'CLEAR_COMPLETED_AFTER is set to an invalid value "{self.config.CLEAR_COMPLETED_AFTER}", expected an integer number of seconds')
                    clear_after = 0
                if clear_after > 0:
                    task = asyncio.create_task(self.__auto_clear_after_delay(download.info.url, clear_after))
                    task.add_done_callback(lambda t: log.error(f'Auto-clear task failed: {t.exception()}') if not t.cancelled() and t.exception() else None)

    async def __auto_clear_after_delay(self, url, delay_seconds):
        await asyncio.sleep(delay_seconds)
        if self.done.exists(url):
            log.debug(f'Auto-clearing completed download: {url}')
            await self.clear([url])

    def __extract_info(self, url):
        debug_logging = logging.getLogger().isEnabledFor(logging.DEBUG)
        return yt_dlp.YoutubeDL(params={
            'quiet': not debug_logging,
            'verbose': debug_logging,
            'no_color': True,
            'extract_flat': True,
            'ignore_no_formats_error': True,
            'noplaylist': True,
            'paths': {"home": self.config.DOWNLOAD_DIR, "temp": self.config.TEMP_DIR},
            **self.config.YTDL_OPTIONS,
            **({'impersonate': yt_dlp.networking.impersonate.ImpersonateTarget.from_str(self.config.YTDL_OPTIONS['impersonate'])} if 'impersonate' in self.config.YTDL_OPTIONS else {}),
        }).extract_info(url, download=False)

    def __calc_download_path(self, download_type, folder):
        base_directory = self.config.AUDIO_DOWNLOAD_DIR if download_type == 'audio' else self.config.DOWNLOAD_DIR
        if folder:
            if not self.config.CUSTOM_DIRS:
                return None, {'status': 'error', 'msg': 'A folder for the download was specified but CUSTOM_DIRS is not true in the configuration.'}
            dldirectory = os.path.realpath(os.path.join(base_directory, folder))
            real_base_directory = os.path.realpath(base_directory)
            if not dldirectory.startswith(real_base_directory):
                return None, {'status': 'error', 'msg': f'Folder "{folder}" must resolve inside the base download directory "{real_base_directory}"'}
            if not os.path.isdir(dldirectory):
                if not self.config.CREATE_CUSTOM_DIRS:
                    return None, {'status': 'error', 'msg': f'Folder "{folder}" for download does not exist inside base directory "{real_base_directory}", and CREATE_CUSTOM_DIRS is not true in the configuration.'}
                os.makedirs(dldirectory, exist_ok=True)
        else:
            dldirectory = base_directory
        return dldirectory, None

    async def __add_download(self, dl, auto_start):
        dldirectory, error_message = self.__calc_download_path(dl.download_type, dl.folder)
        if error_message is not None:
            return error_message
        output = self.config.OUTPUT_TEMPLATE if len(dl.custom_name_prefix) == 0 else f'{dl.custom_name_prefix}.{self.config.OUTPUT_TEMPLATE}'
        output_chapter = self.config.OUTPUT_TEMPLATE_CHAPTER
        entry = getattr(dl, 'entry', None)
        if entry is not None and entry.get('playlist_index') is not None:
            if len(self.config.OUTPUT_TEMPLATE_PLAYLIST):
                output = self.config.OUTPUT_TEMPLATE_PLAYLIST
            for property, value in entry.items():
                if property.startswith("playlist"):
                    output = _outtmpl_substitute_field(output, property, _sanitize_path_component(value))
        if entry is not None and entry.get('channel_index') is not None:
            if len(self.config.OUTPUT_TEMPLATE_CHANNEL):
                output = self.config.OUTPUT_TEMPLATE_CHANNEL
            for property, value in entry.items():
                if property.startswith("channel"):
                    output = _outtmpl_substitute_field(output, property, _sanitize_path_component(value))
        ytdl_options = dict(self.config.YTDL_OPTIONS)
        playlist_item_limit = getattr(dl, 'playlist_item_limit', 0)
        if playlist_item_limit > 0:
            log.info(f'playlist limit is set. Processing only first {playlist_item_limit} entries')
            ytdl_options['playlistend'] = playlist_item_limit
        download = Download(dldirectory, self.config.TEMP_DIR, output, output_chapter, dl.quality, dl.format, ytdl_options, dl)
        if auto_start is True:
            self.queue.put(download)
            asyncio.create_task(self.__start_download(download))
        else:
            self.pending.put(download)
        await self.notifier.added(dl)

    async def __add_entry(
        self,
        entry,
        download_type,
        codec,
        format,
        quality,
        folder,
        custom_name_prefix,
        playlist_item_limit,
        auto_start,
        split_by_chapters,
        chapter_template,
        subtitle_language,
        subtitle_mode,
        already,
        _add_gen=None,
    ):
        if not entry:
            return {'status': 'error', 'msg': "Invalid/empty data was given."}

        error = None
        if "live_status" in entry and "release_timestamp" in entry and entry.get("live_status") == "is_upcoming":
            dt_ts = datetime.fromtimestamp(entry.get("release_timestamp")).strftime('%Y-%m-%d %H:%M:%S %z')
            error = f"Live stream is scheduled to start at {dt_ts}"
        else:
            if "msg" in entry:
                error = entry["msg"]

        etype = entry.get('_type') or 'video'

        if etype.startswith('url'):
            log.debug('Processing as a url')
            return await self.add(
                entry['url'],
                download_type,
                codec,
                format,
                quality,
                folder,
                custom_name_prefix,
                playlist_item_limit,
                auto_start,
                split_by_chapters,
                chapter_template,
                subtitle_language,
                subtitle_mode,
                already,
                _add_gen,
            )
        elif etype == 'playlist' or etype == 'channel':
            log.debug(f'Processing as a {etype}')
            entries = entry['entries']
            # Convert generator to list if needed (for len() and slicing operations)
            if isinstance(entries, types.GeneratorType):
                entries = list(entries)
            log.info(f'{etype} detected with {len(entries)} entries')
            index_digits = len(str(len(entries)))
            results = []
            if playlist_item_limit > 0:
                log.info(f'Item limit is set. Processing only first {playlist_item_limit} entries')
                entries = entries[:playlist_item_limit]
            for index, etr in enumerate(entries, start=1):
                if _add_gen is not None and self._add_generation != _add_gen:
                    log.info(f'Playlist add canceled after processing {len(already)} entries')
                    return {'status': 'ok', 'msg': f'Canceled - added {len(already)} items before cancel'}
                etr["_type"] = "video"
                etr[etype] = entry.get("id") or entry.get("channel_id") or entry.get("channel")
                etr[f"{etype}_index"] = '{{0:0{0:d}d}}'.format(index_digits).format(index)
                for property in ("id", "title", "uploader", "uploader_id"):
                    if property in entry:
                        etr[f"{etype}_{property}"] = entry[property]
                results.append(
                    await self.__add_entry(
                        etr,
                        download_type,
                        codec,
                        format,
                        quality,
                        folder,
                        custom_name_prefix,
                        playlist_item_limit,
                        auto_start,
                        split_by_chapters,
                        chapter_template,
                        subtitle_language,
                        subtitle_mode,
                        already,
                        _add_gen,
                    )
                )
            if any(res['status'] == 'error' for res in results):
                return {'status': 'error', 'msg': ', '.join(res['msg'] for res in results if res['status'] == 'error' and 'msg' in res)}
            return {'status': 'ok'}
        elif etype == 'video' or (etype.startswith('url') and 'id' in entry and 'title' in entry):
            log.debug('Processing as a video')
            key = entry.get('webpage_url') or entry['url']
            if key in self._canceled_urls:
                log.info(f'Skipping canceled URL: {entry.get("title") or key}')
                return {'status': 'ok'}
            if not self.queue.exists(key):
                dl = DownloadInfo(
                    id=entry['id'],
                    title=entry.get('title') or entry['id'],
                    url=key,
                    quality=quality,
                    download_type=download_type,
                    codec=codec,
                    format=format,
                    folder=folder,
                    custom_name_prefix=custom_name_prefix,
                    error=error,
                    entry=entry,
                    playlist_item_limit=playlist_item_limit,
                    split_by_chapters=split_by_chapters,
                    chapter_template=chapter_template,
                    subtitle_language=subtitle_language,
                    subtitle_mode=subtitle_mode,
                )
                await self.__add_download(dl, auto_start)
            return {'status': 'ok'}
        return {'status': 'error', 'msg': f'Unsupported resource "{etype}"'}

    async def add(
        self,
        url,
        download_type,
        codec,
        format,
        quality,
        folder,
        custom_name_prefix,
        playlist_item_limit,
        auto_start=True,
        split_by_chapters=False,
        chapter_template=None,
        subtitle_language="en",
        subtitle_mode="prefer_manual",
        already=None,
        _add_gen=None,
    ):
        log.info(
            f'adding {url}: {download_type=} {codec=} {format=} {quality=} {already=} {folder=} {custom_name_prefix=} '
            f'{playlist_item_limit=} {auto_start=} {split_by_chapters=} {chapter_template=} '
            f'{subtitle_language=} {subtitle_mode=}'
        )
        if already is None:
            _add_gen = self._add_generation
            self._canceled_urls.clear()
        already = set() if already is None else already
        if url in already:
            log.info('recursion detected, skipping')
            return {'status': 'ok'}
        else:
            already.add(url)
        try:
            entry = await asyncio.get_running_loop().run_in_executor(None, self.__extract_info, url)
        except yt_dlp.utils.YoutubeDLError as exc:
            return {'status': 'error', 'msg': str(exc)}
        return await self.__add_entry(
            entry,
            download_type,
            codec,
            format,
            quality,
            folder,
            custom_name_prefix,
            playlist_item_limit,
            auto_start,
            split_by_chapters,
            chapter_template,
            subtitle_language,
            subtitle_mode,
            already,
            _add_gen,
        )

    async def start_pending(self, ids):
        for id in ids:
            if not self.pending.exists(id):
                log.warn(f'requested start for non-existent download {id}')
                continue
            dl = self.pending.get(id)
            self.queue.put(dl)
            self.pending.delete(id)
            asyncio.create_task(self.__start_download(dl))
        return {'status': 'ok'}

    async def cancel(self, ids):
        for id in ids:
            # Track URL so playlist add loop won't re-queue it
            self._canceled_urls.add(id)
            if self.pending.exists(id):
                self.pending.delete(id)
                await self.notifier.canceled(id)
                continue
            if not self.queue.exists(id):
                log.warn(f'requested cancel for non-existent download {id}')
                continue
            if self.queue.get(id).started():
                self.queue.get(id).cancel()
            else:
                self.queue.delete(id)
                await self.notifier.canceled(id)
        return {'status': 'ok'}

    async def clear(self, ids):
        for id in ids:
            if not self.done.exists(id):
                log.warn(f'requested delete for non-existent download {id}')
                continue
            if self.config.DELETE_FILE_ON_TRASHCAN:
                dl = self.done.get(id)
                try:
                    dldirectory, _ = self.__calc_download_path(dl.info.download_type, dl.info.folder)
                    os.remove(os.path.join(dldirectory, dl.info.filename))
                except Exception as e:
                    log.warn(f'deleting file for download {id} failed with error message {e!r}')
            self.done.delete(id)
            await self.notifier.cleared(id)
        return {'status': 'ok'}

    def get(self):
        return (list((k, v.info) for k, v in self.queue.items()) +
                list((k, v.info) for k, v in self.pending.items()),
                list((k, v.info) for k, v in self.done.items()))
```

## File: `ui/.editorconfig`
```
# Editor configuration, see https://editorconfig.org
root = true

[*]
charset = utf-8
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true

[*.ts]
quote_type = single

[*.md]
max_line_length = off
trim_trailing_whitespace = false
```

## File: `ui/angular.json`
```json
{
  "$schema": "./node_modules/@angular/cli/lib/config/schema.json",
  "version": 1,
  "newProjectRoot": "projects",
  "projects": {
    "metube": {
      "projectType": "application",
      "schematics": {
        "@schematics/angular:component": {
          "style": "sass"
        }
      },
      "root": "",
      "sourceRoot": "src",
      "prefix": "app",
      "architect": {
        "build": {
          "builder": "@angular/build:application",
          "options": {
            "outputPath": {
              "base": "dist/metube"
            },
            "index": "src/index.html",
            "tsConfig": "tsconfig.app.json",
            "assets": [
              "src/favicon.ico",
              "src/assets",
              "src/manifest.webmanifest",
              "src/custom-service-worker.js"
            ],
            "styles": [
              "node_modules/bootstrap/dist/css/bootstrap.min.css",
              "node_modules/@ng-select/ng-select/themes/default.theme.css",
              "src/styles.sass"
            ],
            "scripts": [
              "node_modules/bootstrap/dist/js/bootstrap.bundle.min.js"
            ],
            "serviceWorker": "ngsw-config.json",
            "browser": "src/main.ts",
            "polyfills": [
              "zone.js",
              "@angular/localize/init"
            ]
          },
          "configurations": {
            "production": {
              "outputHashing": "all",
              "sourceMap": false,
              "namedChunks": false,
              "extractLicenses": true,
              "budgets": [
                {
                  "type": "initial",
                  "maximumWarning": "2mb",
                  "maximumError": "5mb"
                },
                {
                  "type": "anyComponentStyle",
                  "maximumWarning": "6kb",
                  "maximumError": "10kb"
                }
              ]
            },
            "development": {
              "optimization": false,
              "extractLicenses": false,
              "sourceMap": true
            }
          },
          "defaultConfiguration": "production"
        },
        "serve": {
          "builder": "@angular/build:dev-server",
          "configurations": {
            "production": {
              "buildTarget": "metube:build:production"
            },
             "development": {
              "buildTarget": "metube:build:development",
              "proxyConfig": "proxy.conf.json"
            }
          },
           "defaultConfiguration": "development"
        },
        "test": {
          "builder": "@angular/build:unit-test"
        },
       "lint": {
          "builder": "@angular-eslint/builder:lint",
          "options": {
            "lintFilePatterns": [
              "src/**/*.ts",
              "src/**/*.html"
            ]
          }
        }
      }
    }
  },
  "cli": {
    "analytics": false,
    "packageManager": "pnpm"
  },
  "schematics": {
    "@schematics/angular:component": {
      "type": "component"
    },
    "@schematics/angular:directive": {
      "type": "directive"
    },
    "@schematics/angular:service": {
      "type": "service"
    },
    "@schematics/angular:guard": {
      "typeSeparator": "."
    },
    "@schematics/angular:interceptor": {
      "typeSeparator": "."
    },
    "@schematics/angular:module": {
      "typeSeparator": "."
    },
    "@schematics/angular:pipe": {
      "typeSeparator": "."
    },
    "@schematics/angular:resolver": {
      "typeSeparator": "."
    }
  }
}
```

## File: `ui/eslint.config.js`
```javascript
// @ts-check
const eslint = require("@eslint/js");
const { defineConfig } = require("eslint/config");
const tseslint = require("typescript-eslint");
const angular = require("angular-eslint");

module.exports = defineConfig([
  {
    files: ["**/*.ts"],
    extends: [
      eslint.configs.recommended,
      tseslint.configs.recommended,
      tseslint.configs.stylistic,
      angular.configs.tsRecommended,
    ],
    processor: angular.processInlineTemplates,
    rules: {
      "@angular-eslint/directive-selector": [
        "error",
        {
          type: "attribute",
          prefix: "app",
          style: "camelCase",
        },
      ],
      "@angular-eslint/component-selector": [
        "error",
        {
          type: "element",
          prefix: "app",
          style: "kebab-case",
        },
      ],
    },
  },
  {
    files: ["**/*.html"],
    extends: [
      angular.configs.templateRecommended,
      angular.configs.templateAccessibility,
    ],
    rules: {},
  }
]);
```

## File: `ui/ngsw-config.json`
```json
{
  "$schema": "./node_modules/@angular/service-worker/config/schema.json",
  "index": "/index.html",
  "assetGroups": [
    {
      "name": "app",
      "installMode": "prefetch",
      "resources": {
        "files": [
          "/favicon.ico",
          "/manifest.webmanifest",
          "/*.css",
          "/*.js"
        ]
      }
    },
    {
      "name": "assets",
      "installMode": "lazy",
      "updateMode": "prefetch",
      "resources": {
        "files": [
          "/assets/**",
          "/*.(svg|cur|jpg|jpeg|png|apng|webp|avif|gif|otf|ttf|woff|woff2)"
        ]
      }
    }
  ]
}
```

## File: `ui/package.json`
```json
{
  "name": "metube",
  "version": "0.0.0",
  "scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "build:watch": "ng build --watch",
    "test": "ng test",
    "lint": "ng lint"
  },
  "prettier": {
    "printWidth": 100,
    "singleQuote": true,
    "overrides": [
      {
        "files": "*.html",
        "options": {
          "parser": "angular"
        }
      }
    ]
  },
  "private": true,
  "dependencies": {
    "@angular/animations": "^21.2.4",
    "@angular/common": "^21.2.4",
    "@angular/compiler": "^21.2.4",
    "@angular/core": "^21.2.4",
    "@angular/forms": "^21.2.4",
    "@angular/platform-browser": "^21.2.4",
    "@angular/platform-browser-dynamic": "^21.2.4",
    "@angular/service-worker": "^21.2.4",
    "@fortawesome/angular-fontawesome": "~4.0.0",
    "@fortawesome/fontawesome-svg-core": "^7.2.0",
    "@fortawesome/free-brands-svg-icons": "^7.2.0",
    "@fortawesome/free-regular-svg-icons": "^7.2.0",
    "@fortawesome/free-solid-svg-icons": "^7.2.0",
    "@ng-bootstrap/ng-bootstrap": "^20.0.0",
    "@ng-select/ng-select": "^21.5.2",
    "@popperjs/core": "^2.11.8",
    "bootstrap": "^5.3.8",
    "ngx-cookie-service": "^21.1.0",
    "ngx-socket-io": "~4.10.0",
    "rxjs": "~7.8.2",
    "tslib": "^2.8.1",
    "zone.js": "0.15.0"
  },
  "devDependencies": {
    "@angular-eslint/builder": "21.1.0",
    "@angular/build": "^21.2.2",
    "@angular/cli": "^21.2.2",
    "@angular/compiler-cli": "^21.2.4",
    "@angular/localize": "^21.2.4",
    "@eslint/js": "^9.39.4",
    "angular-eslint": "21.1.0",
    "eslint": "^9.39.4",
    "jsdom": "^27.4.0",
    "typescript": "~5.9.3",
    "typescript-eslint": "8.47.0",
    "vitest": "^4.1.0"
  }
}
```

## File: `ui/tsconfig.app.json`
```json
/* To learn more about this file see: https://angular.io/config/tsconfig. */
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./out-tsc/app",
    "types": [
      "@angular/localize"
    ]
  },
  "include": [
    "src/**/*.ts"
  ],
    "exclude": [
    "src/**/*.spec.ts"
  ]
}
```

## File: `ui/tsconfig.json`
```json
/* To learn more about this file see: https://angular.io/config/tsconfig. */
{
  "compileOnSave": false,
  "compilerOptions": {
    "strict": true,
    "noImplicitOverride": true,
    "noPropertyAccessFromIndexSignature": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "skipLibCheck": true,
    "isolatedModules": true,
    "experimentalDecorators": true,
    "importHelpers": true,
    "target": "ES2022",
    "module": "preserve"
  },
  "angularCompilerOptions": {
    "strictInjectionParameters": true,
    "strictInputAccessModifiers": true,
    "strictTemplates": true
  },
  "files": [],
  "references": [
    {
      "path": "./tsconfig.app.json"
    },
    {
      "path": "./tsconfig.spec.json"
    }
  ]
}
```

## File: `ui/tsconfig.spec.json`
```json
/* To learn more about this file see: https://angular.io/config/tsconfig. */
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./out-tsc/spec",
    "types": [
      "vitest/globals"
    ]
  },
  "include": [
    "src/**/*.spec.ts",
    "src/**/*.d.ts"
  ]
}
```

## File: `ui/src/custom-service-worker.js`
```javascript
/* RegExp pattern to match URLs in the shared target text (apps often share additional text, not only URLs) */
const URL_PATTERN = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/gi;

self.addEventListener("fetch", (event) => {
  if (event.request.method === "GET") {
    const url = new URL(event.request.url);

    if (url.pathname.endsWith("/share-target")) {
      const urlRegExp = new RegExp(URL_PATTERN);
      const sharedText = url.searchParams.get("text");
      const matches = [...sharedText.matchAll(urlRegExp)].map((m) => m[0]);
      const basePath = url.pathname.split("/").slice(0, -1).join("/");

      event.respondWith(
        (async () => {
          await Promise.all(
            matches.map((url) => {
              return fetch(`${basePath}/add`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  url,
                  quality: "best",
                  format: "any",
                  auto_start: true,
                }),
              });
            })
          );
          return Response.redirect(basePath || "/", 303);
        })()
      );
    }
  }
});

importScripts("./ngsw-worker.js");
```

## File: `ui/src/index.html`
```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>MeTube</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="apple-touch-icon" sizes="180x180" href="assets/icons/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/icons/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="assets/icons/favicon-16x16.png">
  <link rel="mask-icon" href="assets/icons/safari-pinned-tab.svg" color="#5bbad5">
  <meta name="msapplication-config" content="assets/icons/browserconfig.xml">
  <link rel="shortcut icon" href="favicon.ico">
  <meta name="msapplication-TileColor" content="#da532c">
  <link rel="manifest" href="manifest.webmanifest" crossorigin="use-credentials">
  <meta name="theme-color" content="#212529">
</head>
<body>
  <app-root></app-root>
  <noscript>Please enable JavaScript to continue using this application.</noscript>
</body>
</html>
```

## File: `ui/src/main.ts`
```typescript
/// <reference types="@angular/localize" />

import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { App } from './app/app';


bootstrapApplication(App, appConfig)
  .catch((err) => console.error(err));
```

## File: `ui/src/manifest.webmanifest`
```
{
  "name": "MeTube",
  "short_name": "MeTube",
  "theme_color": "#212529",
  "background_color": "#fafafa",
  "display": "standalone",
  "scope": "./",
  "start_url": "./?utm_source=homescreen",
  "icons": [
    {
      "src": "assets/icons/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "assets/icons/android-chrome-384x384.png",
      "sizes": "384x384",
      "type": "image/png"
    }
  ],
  "share_target": {
    "action": "./share-target",
    "method": "GET",
    "params": {
      "text": "text"
    }
  }
}
```

## File: `ui/src/styles.sass`
```
/* You can add global styles to this file, and also import other style files */

.navbar
    background-color: var(--bs-dark) !important

    [data-bs-theme="dark"] &
        background-color: var(--bs-dark-bg-subtle) !important
```

## File: `ui/src/app/app.config.ts`
```typescript
import { ApplicationConfig, provideBrowserGlobalErrorListeners, isDevMode, provideZonelessChangeDetection, provideZoneChangeDetection } from '@angular/core';
import { provideServiceWorker } from '@angular/service-worker';
import { provideHttpClient, withInterceptorsFromDi } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideServiceWorker('custom-service-worker.js', {
            enabled: !isDevMode(),
            // Register the ServiceWorker as soon as the application is stable
            // or after 30 seconds (whichever comes first).
            registrationStrategy: 'registerWhenStable:30000'
          }),
    provideHttpClient(withInterceptorsFromDi()),
  ]
};
```

## File: `ui/src/app/app.html`
```html
<nav class="navbar navbar-expand-md navbar-dark">
  <div class="container-fluid">
    <a class="navbar-brand d-flex align-items-center" href="#">
      <img src="assets/icons/android-chrome-192x192.png" alt="MeTube Logo" height="32" class="me-2">
      MeTube
    </a>
    <div class="download-metrics">
      @if (activeDownloads > 0) {
        <div class="metric">
          <fa-icon [icon]="faDownload" class="text-primary" />
          <span>{{activeDownloads}} downloading</span>
        </div>
      }
      @if (queuedDownloads > 0) {
        <div class="metric">
          <fa-icon [icon]="faClock" class="text-warning" />
          <span>{{queuedDownloads}} queued</span>
        </div>
      }
      @if (completedDownloads > 0) {
        <div class="metric">
          <fa-icon [icon]="faCheck" class="text-success" />
          <span>{{completedDownloads}} completed</span>
        </div>
      }
      @if (failedDownloads > 0) {
        <div class="metric">
          <fa-icon [icon]="faTimesCircle" class="text-danger" />
          <span>{{failedDownloads}} failed</span>
        </div>
      }
      @if ((totalSpeed | speed) !== '') {
        <div class="metric">
          <fa-icon [icon]="faTachometerAlt" class="text-info" />
          <span>{{totalSpeed | speed }}</span>
        </div>
      }
    </div>
    <!--
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsDefault" aria-controls="navbarsDefault" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarsDefault">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
      </ul>
    </div>
    -->
    <div class="navbar-nav ms-auto">
      <div class="nav-item dropdown">
        <button class="btn btn-link nav-link py-2 px-0 px-sm-2 dropdown-toggle d-flex align-items-center"
          id="theme-select"
          type="button"
          aria-expanded="false"
          data-bs-toggle="dropdown"
          data-bs-display="static">
          @if(activeTheme){
          <fa-icon [icon]="activeTheme.icon" />
          }
        </button>
        <ul class="dropdown-menu dropdown-menu-end position-absolute" aria-labelledby="theme-select">
          @for (theme of themes; track theme) {
            <li>
              <button type="button" class="dropdown-item d-flex align-items-center"
              [class.active]="activeTheme === theme"
              (click)="themeChanged(theme)">
                <span class="me-2 opacity-50">
                  <fa-icon [icon]="theme.icon" />
                </span>
                {{ theme.displayName }}
                <span class="ms-auto"
                [class.d-none]="activeTheme !== theme">
                <fa-icon [icon]="faCheck" />
                </span>
              </button>
            </li>
          }
        </ul>
      </div>
    </div>
  </div>
</nav>

<main role="main" class="container container-xl">
  <form #f="ngForm">
    <div class="container add-url-box">
      <!-- Main URL Input with Download Button -->
      <div class="row mb-4">
        <div class="col">
          <div class="input-group input-group-lg shadow-sm">
            <input type="text"
              autocomplete="off"
              spellcheck="false"
              class="form-control form-control-lg"
              placeholder="Enter video, channel, or playlist URL"
              name="addUrl"
              [(ngModel)]="addUrl"
              [disabled]="addInProgress || downloads.loading">
            @if (addInProgress && cancelRequested) {
              <button class="btn btn-warning btn-lg px-3" type="button" disabled>
                <span class="spinner-border spinner-border-sm me-1" role="status"></span>
                Canceling...
              </button>
            } @else if (addInProgress) {
              <button class="btn btn-secondary btn-lg px-3 add-progress-btn" type="button" disabled>
                <span class="spinner-border spinner-border-sm me-2" role="status"></span>
                Adding...
              </button>
              <button class="btn btn-outline-danger btn-lg px-3 add-cancel-btn"
                type="button"
                (click)="cancelAdding()"
                aria-label="Cancel adding URL"
                title="Cancel adding URL">
                <fa-icon [icon]="faTimesCircle" class="me-1" /> Cancel
              </button>
            } @else {
              <button class="btn btn-primary btn-lg px-4" type="submit"
                (click)="addDownload()"
                [disabled]="downloads.loading">
                Download
              </button>
            }
          </div>
        </div>
      </div>

      <!-- Options Row -->
      <div class="row mb-3 g-3">
        @if (downloadType === 'video') {
          <div class="col-md-3">
            <div class="input-group">
              <span class="input-group-text">Type</span>
              <select class="form-select"
                name="downloadType"
                [(ngModel)]="downloadType"
                (change)="downloadTypeChanged()"
                [disabled]="addInProgress || downloads.loading">
                @for (type of downloadTypes; track type.id) {
                  <option [ngValue]="type.id">{{ type.text }}</option>
                }
              </select>
            </div>
          </div>
          <div class="col-md-3">
            <div class="input-group">
              <span class="input-group-text">Codec</span>
              <select class="form-select"
                name="codec"
                [(ngModel)]="codec"
                (change)="codecChanged()"
                [disabled]="addInProgress || downloads.loading">
                @for (vc of videoCodecs; track vc.id) {
                  <option [ngValue]="vc.id">{{ vc.text }}</option>
                }
              </select>
            </div>
          </div>
          <div class="col-md-3">
            <div class="input-group">
              <span class="input-group-text">Format</span>
              <select class="form-select"
                name="format"
                [(ngModel)]="format"
                (change)="formatChanged()"
                [disabled]="addInProgress || downloads.loading">
                @for (f of getFormatOptions(); track f.id) {
                  <option [ngValue]="f.id">{{ f.text }}</option>
                }
              </select>
            </div>
          </div>
          <div class="col-md-3">
            <div class="input-group">
              <span class="input-group-text">Quality</span>
              <select class="form-select"
                name="quality"
                [(ngModel)]="quality"
                (change)="qualityChanged()"
                [disabled]="addInProgress || downloads.loading || !showQualitySelector()">
                @for (q of qualities; track q.id) {
                  <option [ngValue]="q.id">{{ q.text }}</option>
                }
              </select>
            </div>
          </div>
        } @else if (downloadType === 'audio') {
          <div class="col-md-4">
            <div class="input-group">
              <span class="input-group-text">Type</span>
              <select class="form-select"
                name="downloadType"
                [(ngModel)]="downloadType"
                (change)="downloadTypeChanged()"
                [disabled]="addInProgress || downloads.loading">
                @for (type of downloadTypes; track type.id) {
                  <option [ngValue]="type.id">{{ type.text }}</option>
                }
              </select>
            </div>
          </div>
          <div class="col-md-4">
            <div class="input-group">
              <span class="input-group-text">Format</span>
              <select class="form-select"
                name="format"
                [(ngModel)]="format"
                (change)="formatChanged()"
                [disabled]="addInProgress || downloads.loading">
                @for (f of getFormatOptions(); track f.id) {
                  <option [ngValue]="f.id">{{ f.text }}</option>
                }
              </select>
            </div>
          </div>
          <div class="col-md-4">
            <div class="input-group">
              <span class="input-group-text">Quality</span>
              <select class="form-select"
                name="quality"
                [(ngModel)]="quality"
                (change)="qualityChanged()"
                [disabled]="addInProgress || downloads.loading">
                @for (q of qualities; track q.id) {
                  <option [ngValue]="q.id">{{ q.text }}</option>
                }
              </select>
            </div>
          </div>
        } @else if (downloadType === 'captions') {
          <div class="col-md-3">
            <div class="input-group">
              <span class="input-group-text">Type</span>
              <select class="form-select"
                name="downloadType"
                [(ngModel)]="downloadType"
                (change)="downloadTypeChanged()"
                [disabled]="addInProgress || downloads.loading">
                @for (type of downloadTypes; track type.id) {
                  <option [ngValue]="type.id">{{ type.text }}</option>
                }
              </select>
            </div>
          </div>
          <div class="col-md-3">
            <div class="input-group">
              <span class="input-group-text">Format</span>
              <select class="form-select"
                name="format"
                [(ngModel)]="format"
                (change)="formatChanged()"
                [disabled]="addInProgress || downloads.loading"
                ngbTooltip="Subtitle output format for captions mode">
                @for (f of getFormatOptions(); track f.id) {
                  <option [ngValue]="f.id">{{ f.text }}</option>
                }
              </select>
            </div>
          </div>
          <div class="col-md-3">
            <div class="input-group">
              <span class="input-group-text">Language</span>
              <input class="form-control"
                type="text"
                list="subtitleLanguageOptions"
                name="subtitleLanguage"
                [(ngModel)]="subtitleLanguage"
                (change)="subtitleLanguageChanged()"
                [disabled]="addInProgress || downloads.loading"
                placeholder="e.g. en, es, zh-Hans"
                ngbTooltip="Subtitle language (you can type any language code)">
              <datalist id="subtitleLanguageOptions">
                @for (lang of subtitleLanguages; track lang.id) {
                  <option [value]="lang.id">{{ lang.text }}</option>
                }
              </datalist>
            </div>
          </div>
          <div class="col-md-3">
            <div class="input-group">
              <span class="input-group-text">Subtitle Source</span>
              <select class="form-select"
                name="subtitleMode"
                [(ngModel)]="subtitleMode"
                (change)="subtitleModeChanged()"
                [disabled]="addInProgress || downloads.loading"
                ngbTooltip="Choose manual, auto, or fallback preference for captions mode">
                @for (mode of subtitleModes; track mode.id) {
                  <option [ngValue]="mode.id">{{ mode.text }}</option>
                }
              </select>
            </div>
          </div>
        } @else {
          <div class="col-md-6">
            <div class="input-group">
              <span class="input-group-text">Type</span>
              <select class="form-select"
                name="downloadType"
                [(ngModel)]="downloadType"
                (change)="downloadTypeChanged()"
                [disabled]="addInProgress || downloads.loading">
                @for (type of downloadTypes; track type.id) {
                  <option [ngValue]="type.id">{{ type.text }}</option>
                }
              </select>
            </div>
          </div>
          <div class="col-md-6">
            <div class="input-group">
              <span class="input-group-text">Format</span>
              <input class="form-control" value="JPG" disabled>
            </div>
          </div>
        }
      </div>

      <div class="row mb-3 g-3">
        <div class="col-12 text-start">
          <button type="button"
            class="btn btn-link p-0 text-decoration-none"
            (click)="toggleAdvanced()"
            [attr.aria-expanded]="isAdvancedOpen"
            aria-controls="advancedOptions">
            Advanced Options
            <fa-icon
              [icon]="isAdvancedOpen ? faChevronDown : faChevronRight"
              class="ms-1" />
          </button>
        </div>
      </div>

      <!-- Advanced Options Panel -->
      <div class="row">
        <div class="col-12">
          <div class="collapse show" id="advancedOptions" [ngbCollapse]="!isAdvancedOpen">
            <div class="py-2">
              <!-- Advanced Settings -->
              <div class="row g-3 mb-2">
                <div class="col-md-6">
                  <div class="input-group">
                    <span class="input-group-text">Auto Start</span>
                    <select class="form-select"
                      name="autoStart"
                      [(ngModel)]="autoStart"
                      (change)="autoStartChanged()"
                      [disabled]="addInProgress || downloads.loading"
                      ngbTooltip="Automatically start downloads when added">
                      <option [ngValue]="true">Yes</option>
                      <option [ngValue]="false">No</option>
                    </select>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="input-group">
                    <span class="input-group-text">Download Folder</span>
                    @if (customDirs$ | async; as customDirs) {
                    <ng-select [items]="customDirs"
                      placeholder="Default"
                      [addTag]="allowCustomDir.bind(this)"
                      addTagText="Create directory"
                      bindLabel="folder"
                      [(ngModel)]="folder"
                      [disabled]="addInProgress || downloads.loading"
                      [virtualScroll]="true"
                      [clearable]="true"
                      [loading]="downloads.loading"
                      [searchable]="true"
                      [closeOnSelect]="true"
                      ngbTooltip="Choose where to save downloads. Type to create a new folder." />
                  }
                  </div>

                </div>
                <div class="col-md-6">
                  <div class="input-group">
                    <span class="input-group-text">Custom Name Prefix</span>
                    <input type="text"
                      class="form-control"
                      placeholder="Default"
                      name="customNamePrefix"
                      [(ngModel)]="customNamePrefix"
                      [disabled]="addInProgress || downloads.loading"
                      ngbTooltip="Add a prefix to downloaded filenames">
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="input-group">
                    <span class="input-group-text">Items Limit</span>
                    <input type="number"
                      min="0"
                      class="form-control"
                      placeholder="Default"
                      name="playlistItemLimit"
                      (keydown)="isNumber($event)"
                      [(ngModel)]="playlistItemLimit"
                      [disabled]="addInProgress || downloads.loading"
                      ngbTooltip="Maximum number of items to download from a playlist or channel (0 = no limit)">
                  </div>
                </div>
                <div class="col-12">
                  <div class="row g-2 align-items-center">
                    <div class="col-auto">
                      <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" role="switch" id="checkbox-split-chapters"
                          name="splitByChapters" [(ngModel)]="splitByChapters" (change)="splitByChaptersChanged()"
                          [disabled]="addInProgress || downloads.loading"
                          ngbTooltip="Split video into separate files by chapters">
                        <label class="form-check-label" for="checkbox-split-chapters">Split by chapters</label>
                      </div>
                    </div>
                    @if (splitByChapters) {
                    <div class="col">
                      <div class="input-group">
                        <span class="input-group-text">Template</span>
                        <input type="text" class="form-control" name="chapterTemplate" [(ngModel)]="chapterTemplate"
                          (change)="chapterTemplateChanged()" [disabled]="addInProgress || downloads.loading"
                          ngbTooltip="Output template for chapter files">
                      </div>
                    </div>
                    }
                  </div>
                </div>
              </div>

              <!-- Advanced Actions -->
              <div class="row">
                <div class="col-12">
                  <hr class="my-3">
                  <div class="row g-3">
                    <div class="col-md-4">
                      <div class="action-group-label">Cookies</div>
                      <input type="file" id="cookie-upload" class="d-none" accept=".txt"
                        (change)="onCookieFileSelect($event)"
                        [disabled]="cookieUploadInProgress || addInProgress">
                      <div class="btn-group w-100" role="group">
                        <label class="btn mb-0"
                          [class]="hasCookies ? 'btn cookie-active-btn mb-0' : 'btn cookie-btn mb-0'"
                          [class.disabled]="cookieUploadInProgress || addInProgress"
                          for="cookie-upload"
                          ngbTooltip="Upload a cookies.txt file for authenticated downloads">
                          @if (cookieUploadInProgress) {
                            <span class="spinner-border spinner-border-sm me-2" role="status"></span>
                          } @else {
                            <fa-icon [icon]="faUpload" class="me-2" />
                          }
                          {{ hasCookies ? 'Replace Cookies' : 'Upload Cookies' }}
                        </label>
                        @if (hasCookies) {
                          <button type="button" class="btn btn-outline-danger"
                            (click)="deleteCookies()"
                            [disabled]="cookieUploadInProgress || addInProgress"
                            ngbTooltip="Remove uploaded cookies">
                            <fa-icon [icon]="faTrashAlt" />
                          </button>
                        }
                      </div>
                      <div class="cookie-status" [class.active]="hasCookies">
                        @if (hasCookies) {
                          <fa-icon [icon]="faCheckCircle" class="me-1" />
                          Cookies active
                        } @else {
                          No cookies configured
                        }
                      </div>
                    </div>
                    <div class="col-md-8">
                      <div class="action-group-label">Bulk Actions</div>
                      <div class="row g-2">
                        <div class="col-4">
                          <button type="button"
                            class="btn btn-secondary w-100"
                            (click)="openBatchImportModal()">
                            <fa-icon [icon]="faFileImport" class="me-2" />
                            Import URLs
                          </button>
                        </div>
                        <div class="col-4">
                          <button type="button"
                            class="btn btn-secondary w-100"
                            (click)="exportBatchUrls('all')">
                            <fa-icon [icon]="faFileExport" class="me-2" />
                            Export URLs
                          </button>
                        </div>
                        <div class="col-4">
                          <button type="button"
                            class="btn btn-secondary w-100"
                            (click)="copyBatchUrls('all')">
                            <fa-icon [icon]="faCopy" class="me-2" />
                            Copy URLs
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </form>

  <!-- Batch Import Modal -->
  <div class="modal fade" tabindex="-1" role="dialog"
  [class.show]="batchImportModalOpen"
  [style.display]="batchImportModalOpen ? 'block' : 'none'">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Batch Import URLs</h5>
          <button type="button" class="btn-close" aria-label="Close" (click)="closeBatchImportModal()"></button>
        </div>
        <div class="modal-body">
          <textarea [(ngModel)]="batchImportText" class="form-control" rows="6"
          placeholder="Paste one video URL per line"></textarea>
          <div class="mt-2">
            @if (batchImportStatus) {
              <small>{{ batchImportStatus }}</small>
            }
          </div>
        </div>
        <div class="modal-footer">
          @if (importInProgress) {
            <button type="button" class="btn btn-danger me-auto" (click)="cancelBatchImport()">
              Cancel Import
            </button>
          }
          <button type="button" class="btn btn-secondary" (click)="closeBatchImportModal()">Close</button>
          <button type="button" class="btn btn-primary" (click)="startBatchImport()" [disabled]="importInProgress">
            Import URLs
          </button>
        </div>
      </div>
    </div>
  </div>


  @if (downloads.loading) {
    <div class="alert alert-info" role="alert">
      Connecting to server...
    </div>
  }
  <div class="metube-section-header">Downloading</div>
  <div class="px-2 py-3 border-bottom">
    <button type="button" class="btn btn-link text-decoration-none px-0 me-4" disabled #queueDelSelected (click)="delSelectedDownloads('queue')"><fa-icon [icon]="faTrashAlt" />&nbsp; Cancel selected</button>
    <button type="button" class="btn btn-link text-decoration-none px-0 me-4" disabled #queueDownloadSelected (click)="startSelectedDownloads('queue')"><fa-icon [icon]="faDownload" />&nbsp; Download selected</button>
  </div>
  <div class="overflow-auto">
    <table class="table">
      <thead>
        <tr>
          <th scope="col" style="width: 1rem;">
            <app-master-checkbox #queueMasterCheckboxRef [id]="'queue'" [list]="downloads.queue" (changed)="queueSelectionChanged($event)" />
          </th>
          <th scope="col">Video</th>
          <th scope="col" style="width: 8rem;">Speed</th>
          <th scope="col" style="width: 7rem;">ETA</th>
          <th scope="col" style="width: 6rem;"></th>
        </tr>
      </thead>
      <tbody>
        @for (download of downloads.queue | keyvalue: asIsOrder; track download.value.id) {
          <tr [class.disabled]='download.value.deleting'>
            <td>
              <app-slave-checkbox [id]="download.key" [master]="queueMasterCheckboxRef" [checkable]="download.value" />
            </td>
            <td title="{{ download.value.filename }}">
              <div class="d-flex flex-column flex-sm-row align-items-center row-gap-2 column-gap-3">
                <div>{{ download.value.title }} </div>
                <ngb-progressbar height="1.5rem" [showValue]="download.value.status !== 'preparing'" [striped]="download.value.status === 'preparing'" [animated]="download.value.status === 'preparing'" type="success"
                [value]="download.value.status === 'preparing' ? 100 : download.value.percent" class="download-progressbar" />
              </div>
            </td>
            <td>{{ download.value.speed | speed }}</td>
            <td>{{ download.value.eta | eta }}</td>
            <td>
              <div class="d-flex">
                @if (download.value.status === 'pending') {
                  <button type="button" class="btn btn-link" (click)="downloadItemByKey(download.key)"><fa-icon [icon]="faDownload" /></button>
                }
                <button type="button" class="btn btn-link" (click)="delDownload('queue', download.key)"><fa-icon [icon]="faTrashAlt" /></button>
                <a href="{{download.value.url}}" target="_blank" class="btn btn-link"><fa-icon [icon]="faExternalLinkAlt" /></a>
              </div>
            </td>
          </tr>
        }
      </tbody>
    </table>
  </div>

  <div class="metube-section-header">Completed</div>
  <div class="px-2 py-3 border-bottom">
    <button type="button" class="btn btn-link text-decoration-none px-0 me-4" (click)="toggleSortOrder()" ngbTooltip="{{ sortAscending ? 'Oldest first' : 'Newest first' }}"><fa-icon [icon]="sortAscending ? faSortAmountUp : faSortAmountDown" />&nbsp; {{ sortAscending ? 'Oldest first' : 'Newest first' }}</button>
    <button type="button" class="btn btn-link text-decoration-none px-0 me-4" disabled #doneDelSelected (click)="delSelectedDownloads('done')"><fa-icon [icon]="faTrashAlt" />&nbsp; Clear selected</button>
    <button type="button" class="btn btn-link text-decoration-none px-0 me-4" disabled #doneClearCompleted (click)="clearCompletedDownloads()"><fa-icon [icon]="faCheckCircle" />&nbsp; Clear completed</button>
    <button type="button" class="btn btn-link text-decoration-none px-0 me-4" disabled #doneClearFailed (click)="clearFailedDownloads()"><fa-icon [icon]="faTimesCircle" />&nbsp; Clear failed</button>
    <button type="button" class="btn btn-link text-decoration-none px-0 me-4" disabled #doneRetryFailed (click)="retryFailedDownloads()"><fa-icon [icon]="faRedoAlt" />&nbsp; Retry failed</button>
    <button type="button" class="btn btn-link text-decoration-none px-0 me-4" disabled #doneDownloadSelected (click)="downloadSelectedFiles()"><fa-icon [icon]="faDownload" />&nbsp; Download Selected</button>
  </div>
  <div class="overflow-auto">
    <table class="table">
      <thead>
        <tr>
          <th scope="col" style="width: 1rem;">
            <app-master-checkbox #doneMasterCheckboxRef [id]="'done'" [list]="downloads.done" (changed)="doneSelectionChanged($event)" />
          </th>
          <th scope="col">Video</th>
          <th scope="col">Type</th>
          <th scope="col">Quality</th>
          <th scope="col">Codec / Format</th>
          <th scope="col">File Size</th>
          <th scope="col">Downloaded</th>
          <th scope="col" style="width: 8rem;"></th>
        </tr>
      </thead>
      <tbody>
        @for (entry of cachedSortedDone; track entry[1].id) {
          <tr [class.disabled]='entry[1].deleting'>
            <td>
              <app-slave-checkbox [id]="entry[0]" [master]="doneMasterCheckboxRef" [checkable]="entry[1]" />
            </td>
            <td>
              <div style="display: inline-block; width: 1.5rem;">
                @if (entry[1].status === 'finished') {
                  <fa-icon [icon]="faCheckCircle" class="text-success" />
                }
                @if (entry[1].status === 'error') {
                  <button type="button" class="btn btn-link p-0"
                    (click)="toggleErrorDetail(entry[0])"
                    [attr.aria-label]="'Toggle error details for ' + entry[1].title"
                    [attr.aria-expanded]="isErrorExpanded(entry[0])">
                    <fa-icon [icon]="faTimesCircle" class="text-danger" />
                  </button>
                }
              </div>
              <span ngbTooltip="{{buildResultItemTooltip(entry[1])}}">@if (!!entry[1].filename) {
                <a href="{{buildDownloadLink(entry[1])}}" target="_blank">{{ entry[1].title }}</a>
              } @else {
                @if (entry[1].status === 'error') {
                  <button type="button" class="btn btn-link p-0 text-start align-baseline" (click)="toggleErrorDetail(entry[0])">
                    {{entry[1].title}}
                    @if (!isErrorExpanded(entry[0])) {
                      <small class="text-danger ms-2">
                        <fa-icon [icon]="faChevronRight" size="xs" class="me-1" />Click for details
                      </small>
                    }
                  </button>
                } @else {
                  <span>{{entry[1].title}}</span>
                }
              }</span>
              @if (entry[1].status === 'error' && isErrorExpanded(entry[0])) {
                <div class="alert alert-danger py-2 px-3 mt-2 mb-0 small" style="border-left: 4px solid var(--bs-danger);">
                  <div class="d-flex justify-content-between align-items-start">
                    <div class="flex-grow-1">
                      @if (entry[1].msg) {
                        <div class="mb-1"><strong>Message:</strong> {{entry[1].msg}}</div>
                      }
                      @if (entry[1].error) {
                        <div class="mb-1"><strong>Error:</strong> {{entry[1].error}}</div>
                      }
                      <div class="text-muted" style="word-break: break-all;"><strong>URL:</strong> {{entry[1].url}}</div>
                    </div>
                    <button type="button" class="btn btn-sm btn-outline-danger ms-2 flex-shrink-0"
                      (click)="copyErrorMessage(entry[0], entry[1]); $event.stopPropagation()"
                      ngbTooltip="Copy error details to clipboard">
                      @if (lastCopiedErrorId === entry[0]) {
                        <span class="text-success">Copied!</span>
                      } @else {
                        <fa-icon [icon]="faCopy" />
                      }
                    </button>
                  </div>
                </div>
              }
            </td>
            <td class="text-nowrap">
              {{ downloadTypeLabel(entry[1]) }}
            </td>
            <td class="text-nowrap">
              {{ formatQualityLabel(entry[1]) }}
            </td>
            <td class="text-nowrap">
              {{ formatCodecLabel(entry[1]) }}
            </td>
            <td>
              @if (entry[1].size) {
                <span>{{ entry[1].size | fileSize }}</span>
              }
            </td>
            <td class="text-nowrap">
              @if (entry[1].timestamp) {
                <span>{{ entry[1].timestamp / 1000000 | date:'yyyy-MM-dd HH:mm' }}</span>
              }
            </td>
            <td>
              <div class="d-flex">
                @if (entry[1].status === 'error') {
                  <button type="button" class="btn btn-link" (click)="retryDownload(entry[0], entry[1])"><fa-icon [icon]="faRedoAlt" /></button>
                }
                @if (entry[1].filename) {
                  <a href="{{buildDownloadLink(entry[1])}}" download class="btn btn-link"><fa-icon [icon]="faDownload" /></a>
                }
                <a href="{{entry[1].url}}" target="_blank" class="btn btn-link"><fa-icon [icon]="faExternalLinkAlt" /></a>
                <button type="button" class="btn btn-link" (click)="delDownload('done', entry[0])"><fa-icon [icon]="faTrashAlt" /></button>
              </div>
            </td>
          </tr>
        @if (entry[1].chapter_files && entry[1].chapter_files.length > 0) {
          @for (chapterFile of entry[1].chapter_files; track chapterFile.filename) {
            <tr [class.disabled]='entry[1].deleting'>
              <td></td>
              <td>
                <div style="padding-left: 2rem;">
              <fa-icon [icon]="faCheckCircle" class="text-success me-2" />
              <a href="{{buildChapterDownloadLink(entry[1], chapterFile.filename)}}" target="_blank">{{
                getChapterFileName(chapterFile.filename) }}</a>
            </div>
          </td>
          <td></td>
          <td></td>
          <td></td>
          <td>
            @if (chapterFile.size) {
            <span>{{ chapterFile.size | fileSize }}</span>
            }
          </td>
          <td></td>
          <td>
            <div class="d-flex">
              <a href="{{buildChapterDownloadLink(entry[1], chapterFile.filename)}}" download
                class="btn btn-link"><fa-icon [icon]="faDownload" /></a>
            </div>
          </td>
        </tr>
        }
      }
    }
      </tbody>
    </table>
  </div>
</main><!-- /.container -->

<footer class="footer navbar-dark bg-dark py-3 mt-5">
  <div class="container text-center">
    @if (ytDlpVersion && metubeVersion) {
      <div class="footer-content">
        <div class="version-item">
          <span class="version-label">yt-dlp</span>
          <span class="version-value">{{ytDlpVersion}}</span>
        </div>
        <div class="version-separator"></div>
        <div class="version-item">
          <span class="version-label">MeTube</span>
          <span class="version-value">{{metubeVersion}}</span>
        </div>
        <div class="version-separator"></div>
        @if (ytDlpOptionsUpdateTime) {
          <div class="version-item">
            <span class="version-label">yt-dlp-options</span>
            <span class="version-value">{{ytDlpOptionsUpdateTime}}</span>
          </div>
        }
        @if (ytDlpOptionsUpdateTime) {
          <div class="version-separator"></div>
        }
        <a href="https://github.com/alexta69/metube" target="_blank" class="github-link">
          <fa-icon [icon]="faGithub" />
          <span>GitHub</span>
        </a>
      </div>
    }
  </div>
</footer>
```

## File: `ui/src/app/app.sass`
```
.button-toggle-theme:focus, .button-toggle-theme:active
    box-shadow: none
    outline: 0px

.add-url-box
    max-width: 960px
    margin: 4rem auto

.add-url-component
    margin: 0.5rem auto

.add-url-group
    width: 100%

button.add-url
    width: 100%

.folder-dropdown-menu
    width: 500px
    max-width: calc(100vw - 3rem)

.folder-dropdown-menu .input-group
    display: flex
    padding-left: 5px
    padding-right: 5px

.metube-section-header
    font-size: 1.8rem
    font-weight: 300
    position: relative
    background: var(--bs-secondary-bg)
    padding: 0.5rem 0
    margin-top: 3.5rem

.metube-section-header:before
    content: ""
    position: absolute
    top: 0
    bottom: 0
    left: -9999px
    right: 0
    border-left: 9999px solid var(--bs-secondary-bg)
    box-shadow: 9999px 0 0 var(--bs-secondary-bg)

button:hover
    text-decoration: none

th
    border-top: 0
    border-bottom-width: 3px !important
    vertical-align: middle !important
    white-space: nowrap

td
    vertical-align: middle

.disabled
    opacity: 0.5
    pointer-events: none

.form-switch
  input
    margin-top: 5px

.download-progressbar
    width: 12rem
    margin-left: auto

.batch-panel
  margin-top: 15px
  border: 1px solid #ccc
  border-radius: 8px
  padding: 15px
  background-color: #fff
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1)

.batch-panel-header
  border-bottom: 1px solid #eee
  padding-bottom: 8px
  margin-bottom: 15px
  h4
    font-size: 1.5rem
    margin: 0

.batch-panel-body
  textarea.form-control
    resize: vertical

.batch-status
  font-size: 0.9rem
  color: #555

.d-flex.my-3
  margin-top: 1rem
  margin-bottom: 1rem

.modal.fade.show
  background-color: rgba(0, 0, 0, 0.5)

.modal-header
  border-bottom: 1px solid #eee

.modal-body
  textarea.form-control
    resize: vertical

.add-url
  display: inline-flex
  align-items: center
  justify-content: center

  .spinner-border
    margin-right: 0.5rem

.add-progress-btn
  min-width: 9.5rem
  cursor: default

.add-cancel-btn
  min-width: 3.25rem

::ng-deep .ng-select
    flex: 1
    .ng-select-container
        min-height: 38px
    .ng-value
        white-space: nowrap
        overflow: visible
    .ng-dropdown-panel
        .ng-dropdown-panel-items
            max-height: 300px
            .ng-option
                white-space: nowrap
                overflow: visible
                text-overflow: ellipsis

:host
  display: flex
  flex-direction: column
  min-height: 100vh

main
  flex-grow: 1

.footer
  width: 100%
  padding: 10px 0
  background: linear-gradient(to bottom, rgba(0,0,0,0.2), rgba(0,0,0,0.1))

  .footer-content
    display: flex
    justify-content: center
    align-items: center
    gap: 20px
    color: #fff
    font-size: 0.9rem

    .version-item
      display: flex
      align-items: center
      gap: 8px

      .version-label
        font-size: 0.75rem
        text-transform: uppercase
        letter-spacing: 0.5px
        opacity: 0.7

      .version-value
        font-family: monospace
        font-size: 0.85rem
        padding: 2px 6px
        background: rgba(255,255,255,0.1)
        border-radius: 4px

    .version-separator
      width: 1px
      height: 16px
      background: rgba(255,255,255,0.2)
      margin: 0 4px

    .github-link
      display: flex
      align-items: center
      gap: 6px
      color: #fff
      text-decoration: none
      font-size: 0.85rem
      padding: 2px 8px
      border-radius: 4px
      transition: background-color 0.2s ease

      &:hover
        background: rgba(255,255,255,0.1)
        color: #fff
        text-decoration: none

      i
        font-size: 1rem

.download-metrics
  display: flex
  align-items: center
  gap: 16px
  margin-left: 24px

  .metric
    display: flex
    align-items: center
    gap: 6px
    font-size: 0.9rem
    color: #adb5bd

    fa-icon
      font-size: 1rem

    span
      white-space: nowrap

.cookie-btn
  flex: 1 1 auto
  background-color: var(--bs-secondary-bg)
  border-color: var(--bs-border-color)
  color: var(--bs-emphasis-color)

  &:hover
    background-color: var(--bs-tertiary-bg)
    border-color: var(--bs-secondary)
    color: var(--bs-emphasis-color)

  &.disabled
    opacity: 0.65
    pointer-events: none

.cookie-active-btn
  flex: 1 1 auto
  background-color: var(--bs-success-bg-subtle)
  border-color: var(--bs-success-border-subtle)
  color: var(--bs-success-text-emphasis)

  &:hover
    background-color: var(--bs-success-bg-subtle)
    border-color: var(--bs-success)
    color: var(--bs-success-text-emphasis)

  &.disabled
    opacity: 0.65
    pointer-events: none

.action-group-label
  font-size: 0.7rem
  text-transform: uppercase
  letter-spacing: 0.05em
  color: var(--bs-secondary-color)
  margin-bottom: 0.4rem

.cookie-status
  font-size: 0.8rem
  margin-top: 0.35rem
  color: var(--bs-secondary-color)

  &.active
    color: var(--bs-success-text-emphasis)
```

## File: `ui/src/app/app.spec.ts`
```typescript
import { TestBed } from '@angular/core/testing';
import { App } from './app';

vi.hoisted(() => {
  Object.defineProperty(window, "matchMedia", {
    writable: true,
    enumerable: true,
    value: vi.fn().mockImplementation((query) => ({
      matches: false,
      media: query,
      onchange: null,
      addEventListener: vi.fn(),
      removeEventListener: vi.fn(),
      dispatchEvent: vi.fn(),
 })),
 });
});


describe('App', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(App);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

});
```

## File: `ui/src/app/app.ts`
```typescript
import { AsyncPipe, DatePipe, KeyValuePipe } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { AfterViewInit, Component, ElementRef, viewChild, inject, OnInit } from '@angular/core';
import { Observable, map, distinctUntilChanged } from 'rxjs';
import { FormsModule } from '@angular/forms';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NgSelectModule } from '@ng-select/ng-select';  
import { faTrashAlt, faCheckCircle, faTimesCircle, faRedoAlt, faSun, faMoon, faCheck, faCircleHalfStroke, faDownload, faExternalLinkAlt, faFileImport, faFileExport, faCopy, faClock, faTachometerAlt, faSortAmountDown, faSortAmountUp, faChevronRight, faChevronDown, faUpload } from '@fortawesome/free-solid-svg-icons';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import { CookieService } from 'ngx-cookie-service';
import { DownloadsService } from './services/downloads.service';
import { Themes } from './theme';
import {
  Download,
  Status,
  Theme,
  Quality,
  Option,
  AudioFormatOption,
  DOWNLOAD_TYPES,
  VIDEO_CODECS,
  VIDEO_FORMATS,
  VIDEO_QUALITIES,
  AUDIO_FORMATS,
  CAPTION_FORMATS,
  THUMBNAIL_FORMATS,
  State,
} from './interfaces';
import { EtaPipe, SpeedPipe, FileSizePipe } from './pipes';
import { MasterCheckboxComponent , SlaveCheckboxComponent} from './components/';

@Component({
  selector: 'app-root',
  imports: [
        FormsModule,
        KeyValuePipe,
        AsyncPipe,
        DatePipe,
        FontAwesomeModule,
        NgbModule,
        NgSelectModule,
        EtaPipe,
        SpeedPipe,
        FileSizePipe,
        MasterCheckboxComponent,
        SlaveCheckboxComponent,
  ],
  templateUrl: './app.html',
  styleUrl: './app.sass',
})
export class App implements AfterViewInit, OnInit {
  downloads = inject(DownloadsService);
  private cookieService = inject(CookieService);
  private http = inject(HttpClient);

  addUrl!: string;
  downloadTypes: Option[] = DOWNLOAD_TYPES;
  videoCodecs: Option[] = VIDEO_CODECS;
  videoFormats: Option[] = VIDEO_FORMATS;
  audioFormats: AudioFormatOption[] = AUDIO_FORMATS;
  captionFormats: Option[] = CAPTION_FORMATS;
  thumbnailFormats: Option[] = THUMBNAIL_FORMATS;
  qualities!: Quality[];
  downloadType: string;
  codec: string;
  quality: string;
  format: string;
  folder!: string;
  customNamePrefix!: string;
  autoStart: boolean;
  playlistItemLimit!: number;
  splitByChapters: boolean;
  chapterTemplate: string;
  subtitleLanguage: string;
  subtitleMode: string;
  addInProgress = false;
  cancelRequested = false;
  hasCookies = false;
  cookieUploadInProgress = false;
  themes: Theme[] = Themes;
  activeTheme: Theme | undefined;
  customDirs$!: Observable<string[]>;
  showBatchPanel = false; 
  batchImportModalOpen = false;
  batchImportText = '';
  batchImportStatus = '';
  importInProgress = false;
  cancelImportFlag = false;
  ytDlpOptionsUpdateTime: string | null = null;
  ytDlpVersion: string | null = null;
  metubeVersion: string | null = null;
  isAdvancedOpen = false;
  sortAscending = false;
  expandedErrors: Set<string> = new Set<string>();
  cachedSortedDone: [string, Download][] = [];
  lastCopiedErrorId: string | null = null;
  private previousDownloadType = 'video';
  private selectionsByType: Record<string, {
    codec: string;
    format: string;
    quality: string;
    subtitleLanguage: string;
    subtitleMode: string;
  }> = {};
  private readonly selectionCookiePrefix = 'metube_selection_';

  // Download metrics
  activeDownloads = 0;
  queuedDownloads = 0;
  completedDownloads = 0;
  failedDownloads = 0;
  totalSpeed = 0;

  readonly queueMasterCheckbox = viewChild<MasterCheckboxComponent>('queueMasterCheckboxRef');
  readonly queueDelSelected = viewChild.required<ElementRef>('queueDelSelected');
  readonly queueDownloadSelected = viewChild.required<ElementRef>('queueDownloadSelected');
  readonly doneMasterCheckbox = viewChild<MasterCheckboxComponent>('doneMasterCheckboxRef');
  readonly doneDelSelected = viewChild.required<ElementRef>('doneDelSelected');
  readonly doneClearCompleted = viewChild.required<ElementRef>('doneClearCompleted');
  readonly doneClearFailed = viewChild.required<ElementRef>('doneClearFailed');
  readonly doneRetryFailed = viewChild.required<ElementRef>('doneRetryFailed');
  readonly doneDownloadSelected = viewChild.required<ElementRef>('doneDownloadSelected');

  faTrashAlt = faTrashAlt;
  faCheckCircle = faCheckCircle;
  faTimesCircle = faTimesCircle;
  faRedoAlt = faRedoAlt;
  faSun = faSun;
  faMoon = faMoon;
  faCheck = faCheck;
  faCircleHalfStroke = faCircleHalfStroke;
  faDownload = faDownload;
  faExternalLinkAlt = faExternalLinkAlt;
  faFileImport = faFileImport;
  faFileExport = faFileExport;
  faCopy = faCopy;
  faGithub = faGithub;
  faClock = faClock;
  faTachometerAlt = faTachometerAlt;
  faSortAmountDown = faSortAmountDown;
  faSortAmountUp = faSortAmountUp;
  faChevronRight = faChevronRight;
  faChevronDown = faChevronDown;
  faUpload = faUpload;
  subtitleLanguages = [
    { id: 'en', text: 'English' },
    { id: 'ar', text: 'Arabic' },
    { id: 'bn', text: 'Bengali' },
    { id: 'bg', text: 'Bulgarian' },
    { id: 'ca', text: 'Catalan' },
    { id: 'cs', text: 'Czech' },
    { id: 'da', text: 'Danish' },
    { id: 'nl', text: 'Dutch' },
    { id: 'es', text: 'Spanish' },
    { id: 'et', text: 'Estonian' },
    { id: 'fi', text: 'Finnish' },
    { id: 'fr', text: 'French' },
    { id: 'de', text: 'German' },
    { id: 'el', text: 'Greek' },
    { id: 'he', text: 'Hebrew' },
    { id: 'hi', text: 'Hindi' },
    { id: 'hu', text: 'Hungarian' },
    { id: 'id', text: 'Indonesian' },
    { id: 'it', text: 'Italian' },
    { id: 'lt', text: 'Lithuanian' },
    { id: 'lv', text: 'Latvian' },
    { id: 'ms', text: 'Malay' },
    { id: 'no', text: 'Norwegian' },
    { id: 'pl', text: 'Polish' },
    { id: 'pt', text: 'Portuguese' },
    { id: 'pt-BR', text: 'Portuguese (Brazil)' },
    { id: 'ro', text: 'Romanian' },
    { id: 'ru', text: 'Russian' },
    { id: 'sk', text: 'Slovak' },
    { id: 'sl', text: 'Slovenian' },
    { id: 'sr', text: 'Serbian' },
    { id: 'sv', text: 'Swedish' },
    { id: 'ta', text: 'Tamil' },
    { id: 'te', text: 'Telugu' },
    { id: 'th', text: 'Thai' },
    { id: 'tr', text: 'Turkish' },
    { id: 'uk', text: 'Ukrainian' },
    { id: 'ur', text: 'Urdu' },
    { id: 'vi', text: 'Vietnamese' },
    { id: 'ja', text: 'Japanese' },
    { id: 'ko', text: 'Korean' },
    { id: 'zh-Hans', text: 'Chinese (Simplified)' },
    { id: 'zh-Hant', text: 'Chinese (Traditional)' },
  ];
  subtitleModes = [
    { id: 'prefer_manual', text: 'Prefer Manual' },
    { id: 'prefer_auto', text: 'Prefer Auto' },
    { id: 'manual_only', text: 'Manual Only' },
    { id: 'auto_only', text: 'Auto Only' },
  ];
  constructor() {
    this.downloadType = this.cookieService.get('metube_download_type') || 'video';
    this.codec = this.cookieService.get('metube_codec') || 'auto';
    this.format = this.cookieService.get('metube_format') || 'any';
    this.quality = this.cookieService.get('metube_quality') || 'best';
    this.autoStart = this.cookieService.get('metube_auto_start') !== 'false';
    this.splitByChapters = this.cookieService.get('metube_split_chapters') === 'true';
    // Will be set from backend configuration, use empty string as placeholder
    this.chapterTemplate = this.cookieService.get('metube_chapter_template') || '';
    this.subtitleLanguage = this.cookieService.get('metube_subtitle_language') || 'en';
    this.subtitleMode = this.cookieService.get('metube_subtitle_mode') || 'prefer_manual';
    const allowedDownloadTypes = new Set(this.downloadTypes.map(t => t.id));
    const allowedVideoCodecs = new Set(this.videoCodecs.map(c => c.id));
    if (!allowedDownloadTypes.has(this.downloadType)) {
      this.downloadType = 'video';
    }
    if (!allowedVideoCodecs.has(this.codec)) {
      this.codec = 'auto';
    }
    const allowedSubtitleModes = new Set(this.subtitleModes.map(mode => mode.id));
    if (!allowedSubtitleModes.has(this.subtitleMode)) {
      this.subtitleMode = 'prefer_manual';
    }
    this.loadSavedSelections();
    this.restoreSelection(this.downloadType);
    this.normalizeSelectionsForType();
    this.setQualities();
    this.previousDownloadType = this.downloadType;
    this.saveSelection(this.downloadType);
    this.sortAscending = this.cookieService.get('metube_sort_ascending') === 'true';

    this.activeTheme = this.getPreferredTheme(this.cookieService);

    // Subscribe to download updates
    this.downloads.queueChanged.subscribe(() => {
      this.updateMetrics();
    });
    this.downloads.doneChanged.subscribe(() => {
      this.updateMetrics();
      this.rebuildSortedDone();
    });
    // Subscribe to real-time updates
    this.downloads.updated.subscribe(() => {
      this.updateMetrics();
    });
  }

  ngOnInit() {
    this.downloads.getCookieStatus().subscribe(data => {
      this.hasCookies = !!(data && typeof data === 'object' && 'has_cookies' in data && data.has_cookies);
    });
    this.getConfiguration();
    this.getYtdlOptionsUpdateTime();
    this.customDirs$ = this.getMatchingCustomDir();
    this.setTheme(this.activeTheme!);

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
      if (this.activeTheme && this.activeTheme.id === 'auto') {
         this.setTheme(this.activeTheme);
      }
    });
  }

  ngAfterViewInit() {
    this.downloads.queueChanged.subscribe(() => {
      this.queueMasterCheckbox()?.selectionChanged();
    });
    this.downloads.doneChanged.subscribe(() => {
      this.doneMasterCheckbox()?.selectionChanged();
      let completed = 0, failed = 0;
      this.downloads.done.forEach(dl => {
        if (dl.status === 'finished')
          completed++;
        else if (dl.status === 'error')
          failed++;
      });
      this.doneClearCompleted().nativeElement.disabled = completed === 0;
      this.doneClearFailed().nativeElement.disabled = failed === 0;
      this.doneRetryFailed().nativeElement.disabled = failed === 0;
    });
    this.fetchVersionInfo();
  }

  // workaround to allow fetching of Map values in the order they were inserted
  //  https://github.com/angular/angular/issues/31420
    
   
      
  asIsOrder() {
    return 1;
  }

  qualityChanged() {
    this.cookieService.set('metube_quality', this.quality, { expires: 3650 });
    this.saveSelection(this.downloadType);
    // Re-trigger custom directory change
    this.downloads.customDirsChanged.next(this.downloads.customDirs);
  }

  downloadTypeChanged() {
    this.saveSelection(this.previousDownloadType);
    this.restoreSelection(this.downloadType);
    this.cookieService.set('metube_download_type', this.downloadType, { expires: 3650 });
    this.normalizeSelectionsForType(false);
    this.setQualities();
    this.saveSelection(this.downloadType);
    this.previousDownloadType = this.downloadType;
    this.downloads.customDirsChanged.next(this.downloads.customDirs);
  }

  codecChanged() {
    this.cookieService.set('metube_codec', this.codec, { expires: 3650 });
    this.saveSelection(this.downloadType);
  }

  showAdvanced() {
    return this.downloads.configuration['CUSTOM_DIRS'];
  }

  allowCustomDir(tag: string) {
    if (this.downloads.configuration['CREATE_CUSTOM_DIRS']) {
      return tag;
    }
    return false;
  }

  isAudioType() {
    return this.downloadType === 'audio';
  }

  getMatchingCustomDir() : Observable<string[]> {
    return this.downloads.customDirsChanged.asObservable().pipe(
       // eslint-disable-next-line @typescript-eslint/no-explicit-any
      map((output: any) => {
        // Keep logic consistent with app/ytdl.py
        if (this.isAudioType()) {
          console.debug("Showing audio-specific download directories");
          return output["audio_download_dir"];
        } else {
          console.debug("Showing default download directories");
          return output["download_dir"];
        }
      }),
      distinctUntilChanged((prev, curr) => JSON.stringify(prev) === JSON.stringify(curr))
    );
  }

  getYtdlOptionsUpdateTime() {
    this.downloads.ytdlOptionsChanged.subscribe({
       // eslint-disable-next-line @typescript-eslint/no-explicit-any
      next: (data:any) => {
        if (data['success']){
          const date = new Date(data['update_time'] * 1000);
          this.ytDlpOptionsUpdateTime=date.toLocaleString();
        }else{
          alert("Error reload yt-dlp options: "+data['msg']);
        }
      }
    });
  }
  getConfiguration() {
    this.downloads.configurationChanged.subscribe({
       // eslint-disable-next-line @typescript-eslint/no-explicit-any
      next: (config: any) => {
        const playlistItemLimit = config['DEFAULT_OPTION_PLAYLIST_ITEM_LIMIT'];
        if (playlistItemLimit !== '0') {
          this.playlistItemLimit = playlistItemLimit;
        }
        // Set chapter template from backend config if not already set by cookie
        if (!this.chapterTemplate) {
          this.chapterTemplate = config['OUTPUT_TEMPLATE_CHAPTER'];
        }
      }
    });
  }

  getPreferredTheme(cookieService: CookieService) {
    let theme = 'auto';
    if (cookieService.check('metube_theme')) {
      theme = cookieService.get('metube_theme');
    }

    return this.themes.find(x => x.id === theme) ?? this.themes.find(x => x.id === 'auto');
  }

  themeChanged(theme: Theme) {
    this.cookieService.set('metube_theme', theme.id, { expires: 3650 });
    this.setTheme(theme);
  }

  setTheme(theme: Theme) {
    this.activeTheme = theme;
    if (theme.id === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.documentElement.setAttribute('data-bs-theme', 'dark');
    } else {
      document.documentElement.setAttribute('data-bs-theme', theme.id);
    }
  }

  formatChanged() {
    this.cookieService.set('metube_format', this.format, { expires: 3650 });
    this.setQualities();
    this.saveSelection(this.downloadType);
    // Re-trigger custom directory change
    this.downloads.customDirsChanged.next(this.downloads.customDirs);
  }

  autoStartChanged() {
    this.cookieService.set('metube_auto_start', this.autoStart ? 'true' : 'false', { expires: 3650 });
  }

  splitByChaptersChanged() {
    this.cookieService.set('metube_split_chapters', this.splitByChapters ? 'true' : 'false', { expires: 3650 });
  }

  chapterTemplateChanged() {
    // Restore default if template is cleared - get from configuration
    if (!this.chapterTemplate || this.chapterTemplate.trim() === '') {
      this.chapterTemplate = this.downloads.configuration['OUTPUT_TEMPLATE_CHAPTER'];
    }
    this.cookieService.set('metube_chapter_template', this.chapterTemplate, { expires: 3650 });
  }

  subtitleLanguageChanged() {
    this.cookieService.set('metube_subtitle_language', this.subtitleLanguage, { expires: 3650 });
    this.saveSelection(this.downloadType);
  }

  subtitleModeChanged() {
    this.cookieService.set('metube_subtitle_mode', this.subtitleMode, { expires: 3650 });
    this.saveSelection(this.downloadType);
  }

  isVideoType() {
    return this.downloadType === 'video';
  }

  formatQualityLabel(download: Download): string {
    if (download.download_type === 'captions' || download.download_type === 'thumbnail') {
      return '-';
    }
    const q = download.quality;
    if (!q) return '';
    if (/^\d+$/.test(q) && download.download_type === 'audio') return `${q} kbps`;
    if (/^\d+$/.test(q)) return `${q}p`;
    return q.charAt(0).toUpperCase() + q.slice(1);
  }

  downloadTypeLabel(download: Download): string {
    const type = download.download_type || 'video';
    return type.charAt(0).toUpperCase() + type.slice(1);
  }

  formatCodecLabel(download: Download): string {
    if (download.download_type !== 'video') {
      const format = (download.format || '').toUpperCase();
      return format || '-';
    }
    const codec = download.codec;
    if (!codec || codec === 'auto') return 'Auto';
    return this.videoCodecs.find(c => c.id === codec)?.text ?? codec;
  }

  queueSelectionChanged(checked: number) {
    this.queueDelSelected().nativeElement.disabled = checked == 0;
    this.queueDownloadSelected().nativeElement.disabled = checked == 0;
  }

  doneSelectionChanged(checked: number) {
    this.doneDelSelected().nativeElement.disabled = checked == 0;
    this.doneDownloadSelected().nativeElement.disabled = checked == 0;
  }

  setQualities() {
    if (this.downloadType === 'video') {
      this.qualities = this.format === 'ios'
        ? [{ id: 'best', text: 'Best' }]
        : VIDEO_QUALITIES;
    } else if (this.downloadType === 'audio') {
      const selectedFormat = this.audioFormats.find(el => el.id === this.format);
      this.qualities = selectedFormat ? selectedFormat.qualities : [{ id: 'best', text: 'Best' }];
    } else {
      this.qualities = [{ id: 'best', text: 'Best' }];
    }
    const exists = this.qualities.find(el => el.id === this.quality);
    this.quality = exists ? this.quality : 'best';
  }

  showCodecSelector() {
    return this.downloadType === 'video';
  }

  showFormatSelector() {
    return this.downloadType !== 'thumbnail';
  }

  showQualitySelector() {
    if (this.downloadType === 'video') {
      return this.format !== 'ios';
    }
    return this.downloadType === 'audio';
  }

  getFormatOptions() {
    if (this.downloadType === 'video') {
      return this.videoFormats;
    }
    if (this.downloadType === 'audio') {
      return this.audioFormats;
    }
    if (this.downloadType === 'captions') {
      return this.captionFormats;
    }
    return this.thumbnailFormats;
  }

  private normalizeSelectionsForType(resetForTypeChange = false) {
    if (this.downloadType === 'video') {
      const allowedFormats = new Set(this.videoFormats.map(f => f.id));
      if (resetForTypeChange || !allowedFormats.has(this.format)) {
        this.format = 'any';
      }
      const allowedCodecs = new Set(this.videoCodecs.map(c => c.id));
      if (resetForTypeChange || !allowedCodecs.has(this.codec)) {
        this.codec = 'auto';
      }
    } else if (this.downloadType === 'audio') {
      const allowedFormats = new Set(this.audioFormats.map(f => f.id));
      if (resetForTypeChange || !allowedFormats.has(this.format)) {
        this.format = this.audioFormats[0].id;
      }
    } else if (this.downloadType === 'captions') {
      const allowedFormats = new Set(this.captionFormats.map(f => f.id));
      if (resetForTypeChange || !allowedFormats.has(this.format)) {
        this.format = 'srt';
      }
      this.quality = 'best';
    } else {
      this.format = 'jpg';
      this.quality = 'best';
    }
    this.cookieService.set('metube_format', this.format, { expires: 3650 });
    this.cookieService.set('metube_codec', this.codec, { expires: 3650 });
  }

  private saveSelection(type: string) {
    if (!type) return;
    const selection = {
      codec: this.codec,
      format: this.format,
      quality: this.quality,
      subtitleLanguage: this.subtitleLanguage,
      subtitleMode: this.subtitleMode,
    };
    this.selectionsByType[type] = selection;
    this.cookieService.set(
      this.selectionCookiePrefix + type,
      JSON.stringify(selection),
      { expires: 3650 }
    );
  }

  private restoreSelection(type: string) {
    const saved = this.selectionsByType[type];
    if (!saved) return;
    this.codec = saved.codec;
    this.format = saved.format;
    this.quality = saved.quality;
    this.subtitleLanguage = saved.subtitleLanguage;
    this.subtitleMode = saved.subtitleMode;
  }

  private loadSavedSelections() {
    for (const type of this.downloadTypes.map(t => t.id)) {
      const key = this.selectionCookiePrefix + type;
      if (!this.cookieService.check(key)) continue;
      try {
        const raw = this.cookieService.get(key);
        const parsed = JSON.parse(raw);
        if (parsed && typeof parsed === 'object') {
          this.selectionsByType[type] = {
            codec: String(parsed.codec ?? 'auto'),
            format: String(parsed.format ?? ''),
            quality: String(parsed.quality ?? 'best'),
            subtitleLanguage: String(parsed.subtitleLanguage ?? 'en'),
            subtitleMode: String(parsed.subtitleMode ?? 'prefer_manual'),
          };
        }
      } catch {
        // Ignore malformed cookie values.
      }
    }
  }

  addDownload(
    url?: string,
    downloadType?: string,
    codec?: string,
    quality?: string,
    format?: string,
    folder?: string,
    customNamePrefix?: string,
    playlistItemLimit?: number,
    autoStart?: boolean,
    splitByChapters?: boolean,
    chapterTemplate?: string,
    subtitleLanguage?: string,
    subtitleMode?: string,
  ) {
    url = url ?? this.addUrl
    downloadType = downloadType ?? this.downloadType
    codec = codec ?? this.codec
    quality = quality ?? this.quality
    format = format ?? this.format
    folder = folder ?? this.folder
    customNamePrefix = customNamePrefix ?? this.customNamePrefix
    playlistItemLimit = playlistItemLimit ?? this.playlistItemLimit
    autoStart = autoStart ?? this.autoStart
    splitByChapters = splitByChapters ?? this.splitByChapters
    chapterTemplate = chapterTemplate ?? this.chapterTemplate
    subtitleLanguage = subtitleLanguage ?? this.subtitleLanguage
    subtitleMode = subtitleMode ?? this.subtitleMode

    // Validate chapter template if chapter splitting is enabled
    if (splitByChapters && !chapterTemplate.includes('%(section_number)')) {
      alert('Chapter template must include %(section_number)');
      return;
    }

    console.debug('Downloading: url=' + url + ' downloadType=' + downloadType + ' codec=' + codec + ' quality=' + quality + ' format=' + format + ' folder=' + folder + ' customNamePrefix=' + customNamePrefix + ' playlistItemLimit=' + playlistItemLimit + ' autoStart=' + autoStart + ' splitByChapters=' + splitByChapters + ' chapterTemplate=' + chapterTemplate + ' subtitleLanguage=' + subtitleLanguage + ' subtitleMode=' + subtitleMode);
    this.addInProgress = true;
    this.cancelRequested = false;
    this.downloads.add(url, downloadType, codec, quality, format, folder, customNamePrefix, playlistItemLimit, autoStart, splitByChapters, chapterTemplate, subtitleLanguage, subtitleMode).subscribe((status: Status) => {
      if (status.status === 'error' && !this.cancelRequested) {
        alert(`Error adding URL: ${status.msg}`);
      } else if (status.status !== 'error') {
        this.addUrl = '';
      }
      this.addInProgress = false;
      this.cancelRequested = false;
    });
  }

  cancelAdding() {
    this.cancelRequested = true;
    this.downloads.cancelAdd().subscribe({
      error: (err) => {
        console.error('Failed to cancel adding:', err?.message || err);
      }
    });
  }

  downloadItemByKey(id: string) {
    this.downloads.startById([id]).subscribe();
  }

  retryDownload(key: string, download: Download) {
    this.addDownload(
      download.url,
      download.download_type,
      download.codec,
      download.quality,
      download.format,
      download.folder,
      download.custom_name_prefix,
      download.playlist_item_limit,
      true,
      download.split_by_chapters,
      download.chapter_template,
      download.subtitle_language,
      download.subtitle_mode,
    );
    this.downloads.delById('done', [key]).subscribe();
  }

  delDownload(where: State, id: string) {
    this.downloads.delById(where, [id]).subscribe();
  }

  startSelectedDownloads(where: State){
    this.downloads.startByFilter(where, dl => !!dl.checked).subscribe();
  }

  delSelectedDownloads(where: State) {
    this.downloads.delByFilter(where, dl => !!dl.checked).subscribe();
  }

  clearCompletedDownloads() {
    this.downloads.delByFilter('done', dl => dl.status === 'finished').subscribe();
  }

  clearFailedDownloads() {
    this.downloads.delByFilter('done', dl => dl.status === 'error').subscribe();
  }

  retryFailedDownloads() {
    this.downloads.done.forEach((dl, key) => {
      if (dl.status === 'error') {
        this.retryDownload(key, dl);
      }
    });
  }

  downloadSelectedFiles() {
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    this.downloads.done.forEach((dl, _) => {
      if (dl.status === 'finished' && dl.checked) {
        const link = document.createElement('a');
        link.href = this.buildDownloadLink(dl);
        link.setAttribute('download', dl.filename);
        link.setAttribute('target', '_self');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }
    });
  }

  buildDownloadLink(download: Download) {
    let baseDir = this.downloads.configuration["PUBLIC_HOST_URL"];
    if (download.download_type === 'audio' || download.filename.endsWith('.mp3')) {
      baseDir = this.downloads.configuration["PUBLIC_HOST_AUDIO_URL"];
    }

    if (download.folder) {
      baseDir += download.folder + '/';
    }

    return baseDir + encodeURIComponent(download.filename);
  }

  buildResultItemTooltip(download: Download) {
    const parts = [];
    if (download.msg) {
      parts.push(download.msg);
    }
    if (download.error) {
      parts.push(download.error);
    }
    return parts.join(' | ');
  }

  buildChapterDownloadLink(download: Download, chapterFilename: string) {
    let baseDir = this.downloads.configuration["PUBLIC_HOST_URL"];
    if (download.download_type === 'audio' || chapterFilename.endsWith('.mp3')) {
      baseDir = this.downloads.configuration["PUBLIC_HOST_AUDIO_URL"];
    }

    if (download.folder) {
      baseDir += download.folder + '/';
    }

    return baseDir + encodeURIComponent(chapterFilename);
  }

  getChapterFileName(filepath: string) {
    // Extract just the filename from the path
    const parts = filepath.split('/');
    return parts[parts.length - 1];
  }

  isNumber(event: KeyboardEvent) {
    const charCode = +event.code || event.keyCode;
    if (charCode > 31 && (charCode  < 48 || charCode > 57)) {
      event.preventDefault();
    }
  }

  // Toggle inline batch panel (if you want to use an inline panel for export; not used for import modal)
  toggleBatchPanel(): void {
    this.showBatchPanel = !this.showBatchPanel;
  }

  // Open the Batch Import modal
  openBatchImportModal(): void {
    this.batchImportModalOpen = true;
    this.batchImportText = '';
    this.batchImportStatus = '';
    this.importInProgress = false;
    this.cancelImportFlag = false;
  }

  // Close the Batch Import modal
  closeBatchImportModal(): void {
    this.batchImportModalOpen = false;
  }

  // Start importing URLs from the batch modal textarea
  startBatchImport(): void {
    const urls = this.batchImportText
      .split(/\r?\n/)
      .map(url => url.trim())
      .filter(url => url.length > 0);
    if (urls.length === 0) {
      alert('No valid URLs found.');
      return;
    }
    this.importInProgress = true;
    this.cancelImportFlag = false;
    this.batchImportStatus = `Starting to import ${urls.length} URLs...`;
    let index = 0;
    const delayBetween = 1000;
    const processNext = () => {
      if (this.cancelImportFlag) {
        this.batchImportStatus = `Import cancelled after ${index} of ${urls.length} URLs.`;
        this.importInProgress = false;
        return;
      }
      if (index >= urls.length) {
        this.batchImportStatus = `Finished importing ${urls.length} URLs.`;
        this.importInProgress = false;
        return;
      }
      const url = urls[index];
      this.batchImportStatus = `Importing URL ${index + 1} of ${urls.length}: ${url}`;
      // Pass current selection options to backend
      this.downloads.add(url, this.downloadType, this.codec, this.quality, this.format, this.folder, this.customNamePrefix,
        this.playlistItemLimit, this.autoStart, this.splitByChapters, this.chapterTemplate,
        this.subtitleLanguage, this.subtitleMode)
        .subscribe({
          next: (status: Status) => {
            if (status.status === 'error') {
              alert(`Error adding URL ${url}: ${status.msg}`);
            }
            index++;
            setTimeout(processNext, delayBetween);
          },
          error: (err) => {
            console.error(`Error importing URL ${url}:`, err);
            index++;
            setTimeout(processNext, delayBetween);
          }
        });
    };
    processNext();
  }

  // Cancel the batch import process
  cancelBatchImport(): void {
    if (this.importInProgress) {
      this.cancelImportFlag = true;
      this.batchImportStatus += ' Cancelling...';
    }
  }

  // Export URLs based on filter: 'pending', 'completed', 'failed', or 'all'
  exportBatchUrls(filter: 'pending' | 'completed' | 'failed' | 'all'): void {
    let urls: string[];
    if (filter === 'pending') {
      urls = Array.from(this.downloads.queue.values()).map(dl => dl.url);
    } else if (filter === 'completed') {
      // Only finished downloads in the "done" Map
      urls = Array.from(this.downloads.done.values()).filter(dl => dl.status === 'finished').map(dl => dl.url);
    } else if (filter === 'failed') {
      // Only error downloads from the "done" Map
      urls = Array.from(this.downloads.done.values()).filter(dl => dl.status === 'error').map(dl => dl.url);
    } else {
      // All: pending + both finished and error in done
      urls = [
        ...Array.from(this.downloads.queue.values()).map(dl => dl.url),
        ...Array.from(this.downloads.done.values()).map(dl => dl.url)
      ];
    }
    if (!urls.length) {
      alert('No URLs found for the selected filter.');
      return;
    }
    const content = urls.join('\n');
    const blob = new Blob([content], { type: 'text/plain' });
    const downloadUrl = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = downloadUrl;
    a.download = 'metube_urls.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(downloadUrl);
  }

  // Copy URLs to clipboard based on filter: 'pending', 'completed', 'failed', or 'all'
  copyBatchUrls(filter: 'pending' | 'completed' | 'failed' | 'all'): void {
    let urls: string[];
    if (filter === 'pending') {
      urls = Array.from(this.downloads.queue.values()).map(dl => dl.url);
    } else if (filter === 'completed') {
      urls = Array.from(this.downloads.done.values()).filter(dl => dl.status === 'finished').map(dl => dl.url);
    } else if (filter === 'failed') {
      urls = Array.from(this.downloads.done.values()).filter(dl => dl.status === 'error').map(dl => dl.url);
    } else {
      urls = [
        ...Array.from(this.downloads.queue.values()).map(dl => dl.url),
        ...Array.from(this.downloads.done.values()).map(dl => dl.url)
      ];
    }
    if (!urls.length) {
      alert('No URLs found for the selected filter.');
      return;
    }
    const content = urls.join('\n');
    navigator.clipboard.writeText(content)
      .then(() => alert('URLs copied to clipboard.'))
      .catch(() => alert('Failed to copy URLs.'));
  }

  fetchVersionInfo(): void {
    // eslint-disable-next-line no-useless-escape    
    const baseUrl = `${window.location.origin}${window.location.pathname.replace(/\/[^\/]*$/, '/')}`;
    const versionUrl = `${baseUrl}version`;
    this.http.get<{ 'yt-dlp': string, version: string }>(versionUrl)
      .subscribe({
        next: (data) => {
          this.ytDlpVersion = data['yt-dlp'];
          this.metubeVersion = data.version;
        },
        error: () => {
          this.ytDlpVersion = null;
          this.metubeVersion = null;
        }
      });
  }

  toggleAdvanced() {
    this.isAdvancedOpen = !this.isAdvancedOpen;
  }

  toggleSortOrder() {
    this.sortAscending = !this.sortAscending;
    this.cookieService.set('metube_sort_ascending', this.sortAscending ? 'true' : 'false', { expires: 3650 });
    this.rebuildSortedDone();
  }

  private rebuildSortedDone() {
    const result: [string, Download][] = [];
    this.downloads.done.forEach((dl, key) => {
      result.push([key, dl]);
    });
    if (!this.sortAscending) {
      result.reverse();
    }
    this.cachedSortedDone = result;
  }

  toggleErrorDetail(id: string) {
    if (this.expandedErrors.has(id)) this.expandedErrors.delete(id);
    else this.expandedErrors.add(id);
  }

  copyErrorMessage(id: string, download: Download) {
    const parts: string[] = [];
    if (download.title) parts.push(`Title: ${download.title}`);
    if (download.url) parts.push(`URL: ${download.url}`);
    if (download.msg) parts.push(`Message: ${download.msg}`);
    if (download.error) parts.push(`Error: ${download.error}`);
    const text = parts.join('\n');
    if (!text.trim()) return;
    const done = () => {
      this.lastCopiedErrorId = id;
      setTimeout(() => { this.lastCopiedErrorId = null; }, 1500);
    };
    const fail = (err?: unknown) => {
      console.error('Clipboard write failed:', err);
      alert('Failed to copy to clipboard. Your browser may require HTTPS for clipboard access.');
    };
    if (navigator.clipboard?.writeText) {
      navigator.clipboard.writeText(text).then(done).catch(fail);
    } else {
      try {
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.setAttribute('readonly', '');
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        done();
      } catch (e) {
        fail(e);
      }
    }
  }

  isErrorExpanded(id: string): boolean {
    return this.expandedErrors.has(id);
  }

  onCookieFileSelect(event: Event) {
    const input = event.target as HTMLInputElement;
    if (!input.files?.length) return;
    this.cookieUploadInProgress = true;
    this.downloads.uploadCookies(input.files[0]).subscribe({
      next: (response) => {
        if (response?.status === 'ok') {
          this.hasCookies = true;
        } else {
          this.refreshCookieStatus();
          alert(`Error uploading cookies: ${this.formatErrorMessage(response?.msg)}`);
        }
        this.cookieUploadInProgress = false;
        input.value = '';
      },
      error: () => {
        this.refreshCookieStatus();
        this.cookieUploadInProgress = false;
        input.value = '';
        alert('Error uploading cookies.');
      }
    });
  }

  private formatErrorMessage(error: unknown): string {
    if (typeof error === 'string') {
      return error;
    }
    if (error && typeof error === 'object') {
      const obj = error as Record<string, unknown>;
      for (const key of ['msg', 'reason', 'error', 'detail']) {
        const value = obj[key];
        if (typeof value === 'string' && value.trim()) {
          return value;
        }
      }
      try {
        return JSON.stringify(error);
      } catch {
        return 'Unknown error';
      }
    }
    return 'Unknown error';
  }

  deleteCookies() {
    this.downloads.deleteCookies().subscribe({
      next: (response) => {
        if (response?.status === 'ok') {
          this.refreshCookieStatus();
          return;
        }
        this.refreshCookieStatus();
        alert(`Error deleting cookies: ${this.formatErrorMessage(response?.msg)}`);
      },
      error: () => {
        this.refreshCookieStatus();
        alert('Error deleting cookies.');
      }
    });
  }

  private refreshCookieStatus() {
    this.downloads.getCookieStatus().subscribe(data => {
      this.hasCookies = !!(data && typeof data === 'object' && 'has_cookies' in data && data.has_cookies);
    });
  }

  private updateMetrics() {
    this.activeDownloads = Array.from(this.downloads.queue.values()).filter(d => d.status === 'downloading' || d.status === 'preparing').length;
    this.queuedDownloads = Array.from(this.downloads.queue.values()).filter(d => d.status === 'pending').length;
    this.completedDownloads = Array.from(this.downloads.done.values()).filter(d => d.status === 'finished').length;
    this.failedDownloads = Array.from(this.downloads.done.values()).filter(d => d.status === 'error').length;
    
    // Calculate total speed from downloading items
    const downloadingItems = Array.from(this.downloads.queue.values())
      .filter(d => d.status === 'downloading');
    
    this.totalSpeed = downloadingItems.reduce((total, item) => total + (item.speed || 0), 0);
  }
}
```

## File: `ui/src/app/theme.ts`
```typescript
import { faCircleHalfStroke, faMoon, faSun  } from "@fortawesome/free-solid-svg-icons";
import { Theme } from "./interfaces/theme";


export const Themes: Theme[] = [
  {
    id: 'light',
    displayName: 'Light',
    icon: faSun,
  },
  {
    id: 'dark',
    displayName: 'Dark',
    icon: faMoon,
  },
  {
    id: 'auto',
    displayName: 'Auto',
    icon: faCircleHalfStroke,
  },
];
```

## File: `ui/src/app/components/index.ts`
```typescript
export { MasterCheckboxComponent } from './master-checkbox.component';
export { SlaveCheckboxComponent } from './slave-checkbox.component';
```

## File: `ui/src/app/components/master-checkbox.component.ts`
```typescript
import { Component, ElementRef, viewChild, output, input } from "@angular/core";
import { Checkable } from "../interfaces";
import { FormsModule } from "@angular/forms";

@Component({
    selector: 'app-master-checkbox',
    template: `
  <div class="form-check">
    <input type="checkbox" class="form-check-input" id="{{id()}}-select-all" #masterCheckbox [(ngModel)]="selected" (change)="clicked()">
    <label class="form-check-label" for="{{id()}}-select-all"></label>
  </div>
`,
imports: [
  FormsModule
]
})
export class MasterCheckboxComponent {
  readonly id = input.required<string>();
  readonly list = input.required<Map<string, Checkable>>();
  readonly changed = output<number>();

  readonly masterCheckbox = viewChild.required<ElementRef>('masterCheckbox');
  selected!: boolean;

  clicked() {
    this.list().forEach(item => item.checked = this.selected);
    this.selectionChanged();
  }

  selectionChanged() {
    const masterCheckbox = this.masterCheckbox();
    if (!masterCheckbox)
      return;
    let checked = 0;
    this.list().forEach(item => { if(item.checked) checked++ });
    this.selected = checked > 0 && checked == this.list().size;
    masterCheckbox.nativeElement.indeterminate = checked > 0 && checked < this.list().size;
    this.changed.emit(checked);
  }
}
```

## File: `ui/src/app/components/slave-checkbox.component.ts`
```typescript
import { Component, input } from '@angular/core';
import { MasterCheckboxComponent } from './master-checkbox.component';
import { Checkable } from '../interfaces';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-slave-checkbox',
    template: `
  <div class="form-check">
    <input type="checkbox" class="form-check-input" id="{{master().id()}}-{{id()}}-select" [(ngModel)]="checkable().checked" (change)="master().selectionChanged()">
    <label class="form-check-label" for="{{master().id()}}-{{id()}}-select"></label>
  </div>
`,
imports: [  
  FormsModule
]
})
export class SlaveCheckboxComponent {
  readonly id = input.required<string>();
  readonly master = input.required<MasterCheckboxComponent>();
  readonly checkable = input.required<Checkable>();
}
```

## File: `ui/src/app/interfaces/checkable.ts`
```typescript
export interface Checkable {
  checked: boolean;
}
```

## File: `ui/src/app/interfaces/download.ts`
```typescript

export interface Download {
  id: string;
  title: string;
  url: string;
  download_type: string;
  codec?: string;
  quality: string;
  format: string;
  folder: string;
  custom_name_prefix: string;
  playlist_item_limit: number;
  split_by_chapters?: boolean;
  chapter_template?: string;
  subtitle_language?: string;
  subtitle_mode?: string;
  status: string;
  msg: string;
  percent: number;
  speed: number;
  eta: number;
  filename: string;
  checked: boolean;
  timestamp?: number;
  size?: number;
  error?: string;
  deleting?: boolean;
  chapter_files?: { filename: string, size: number }[];
}
```

## File: `ui/src/app/interfaces/format.ts`
```typescript
import { Quality } from "./quality";

export interface Format {
  id: string;
  text: string;
  qualities: Quality[];
}
```

## File: `ui/src/app/interfaces/formats.ts`
```typescript
import { Quality } from "./quality";

export interface Option {
  id: string;
  text: string;
}

export interface AudioFormatOption extends Option {
  qualities: Quality[];
}

export const DOWNLOAD_TYPES: Option[] = [
  { id: "video", text: "Video" },
  { id: "audio", text: "Audio" },
  { id: "captions", text: "Captions" },
  { id: "thumbnail", text: "Thumbnail" },
];

export const VIDEO_CODECS: Option[] = [
  { id: "auto", text: "Auto" },
  { id: "h264", text: "H.264" },
  { id: "h265", text: "H.265 (HEVC)" },
  { id: "av1", text: "AV1" },
  { id: "vp9", text: "VP9" },
];

export const VIDEO_FORMATS: Option[] = [
  { id: "any", text: "Auto" },
  { id: "mp4", text: "MP4" },
  { id: "ios", text: "iOS Compatible" },
];

export const VIDEO_QUALITIES: Quality[] = [
  { id: "best", text: "Best" },
  { id: "2160", text: "2160p" },
  { id: "1440", text: "1440p" },
  { id: "1080", text: "1080p" },
  { id: "720", text: "720p" },
  { id: "480", text: "480p" },
  { id: "360", text: "360p" },
  { id: "240", text: "240p" },
  { id: "worst", text: "Worst" },
];

export const AUDIO_FORMATS: AudioFormatOption[] = [
  {
    id: "m4a",
    text: "M4A",
    qualities: [
      { id: "best", text: "Best" },
      { id: "192", text: "192 kbps" },
      { id: "128", text: "128 kbps" },
    ],
  },
  {
    id: "mp3",
    text: "MP3",
    qualities: [
      { id: "best", text: "Best" },
      { id: "320", text: "320 kbps" },
      { id: "192", text: "192 kbps" },
      { id: "128", text: "128 kbps" },
    ],
  },
  { id: "opus", text: "OPUS", qualities: [{ id: "best", text: "Best" }] },
  { id: "wav", text: "WAV", qualities: [{ id: "best", text: "Best" }] },
  { id: "flac", text: "FLAC", qualities: [{ id: "best", text: "Best" }] },
];

export const CAPTION_FORMATS: Option[] = [
  { id: "srt", text: "SRT" },
  { id: "txt", text: "TXT (Text only)" },
  { id: "vtt", text: "VTT" },
  { id: "ttml", text: "TTML" },
];

export const THUMBNAIL_FORMATS: Option[] = [{ id: "jpg", text: "JPG" }];
```

## File: `ui/src/app/interfaces/index.ts`
```typescript
export * from './theme';
export * from './status';
export * from './quality';
export * from './state';    
export * from './download'; 
export * from './checkable';
export * from './format';
export * from './formats';

```

## File: `ui/src/app/interfaces/quality.ts`
```typescript

export interface Quality {
  id: string;
  text: string;
}
```

## File: `ui/src/app/interfaces/state.ts`
```typescript
export type State =  'queue' | 'done';
```

## File: `ui/src/app/interfaces/status.ts`
```typescript
export interface Status {
  status: string;
  msg?: string;
}
```

## File: `ui/src/app/interfaces/theme.ts`
```typescript
import { IconDefinition } from "@fortawesome/fontawesome-svg-core";

export interface Theme {
  id: string;
  displayName: string;
  icon: IconDefinition;
}
```

## File: `ui/src/app/pipes/eta.pipe.ts`
```typescript
import { Pipe, PipeTransform } from "@angular/core";

@Pipe({
    name: 'eta',
})
export class EtaPipe implements PipeTransform {
  transform(value: number): string | null {
    if (value === null) {
      return null;
    }
    if (value < 60) {
      return `${Math.round(value)}s`;
    }
    if (value < 3600) {
      return `${Math.floor(value/60)}m ${Math.round(value%60)}s`;
    }
    const hours = Math.floor(value/3600)
    const minutes = value % 3600
    return `${hours}h ${Math.floor(minutes/60)}m ${Math.round(minutes%60)}s`;
  }
}
```

## File: `ui/src/app/pipes/file-size.pipe.ts`
```typescript
import { Pipe, PipeTransform } from "@angular/core";

@Pipe({
    name: 'fileSize',
})
export class FileSizePipe implements PipeTransform {
  transform(value: number): string {
      if (isNaN(value) || value === 0) return '0 Bytes';

      const units = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
      const unitIndex = Math.floor(Math.log(value) / Math.log(1000)); // Use 1000 for common units

      const unitValue = value / Math.pow(1000, unitIndex);
      return `${unitValue.toFixed(2)} ${units[unitIndex]}`;
  }
}
```

## File: `ui/src/app/pipes/index.ts`
```typescript
export { EtaPipe } from './eta.pipe';
export { SpeedPipe } from './speed.pipe';
export { FileSizePipe } from './file-size.pipe';
```

## File: `ui/src/app/pipes/speed.pipe.ts`
```typescript
import { Pipe, PipeTransform } from "@angular/core";
import { BehaviorSubject, throttleTime } from "rxjs";

@Pipe({
    name: 'speed',
    pure: false // Make the pipe impure so it can handle async updates
})
export class SpeedPipe implements PipeTransform {
  private speedSubject = new BehaviorSubject<number>(0);
  private formattedSpeed = '';

  constructor() {
    // Throttle updates to once per second
    this.speedSubject.pipe(
      throttleTime(1000)
    ).subscribe(speed => {
      // If speed is invalid or 0, return empty string
      if (speed === null || speed === undefined || isNaN(speed) || speed <= 0) {
        this.formattedSpeed = '';
        return;
      }
      
      const k = 1024;
      const dm = 2;
      const sizes = ['B/s', 'KB/s', 'MB/s', 'GB/s', 'TB/s', 'PB/s', 'EB/s', 'ZB/s', 'YB/s'];
      const i = Math.floor(Math.log(speed) / Math.log(k));
      this.formattedSpeed = parseFloat((speed / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    });
  }

  transform(value: number): string {
    // If speed is invalid or 0, return empty string
    if (value === null || value === undefined || isNaN(value) || value <= 0) {
      return '';
    }
    
    // Update the speed subject
    this.speedSubject.next(value);
    
    // Return the last formatted speed
    return this.formattedSpeed;
  }
}
```

## File: `ui/src/app/services/downloads.service.ts`
```typescript
import { inject, Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { of, Subject } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { MeTubeSocket } from './metube-socket.service';
import { Download, Status, State } from '../interfaces';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
@Injectable({
  providedIn: 'root'
})
export class DownloadsService {
  private http = inject(HttpClient);
  private socket = inject(MeTubeSocket);
  loading = true;
  queue = new Map<string, Download>();
  done = new Map<string, Download>();
  queueChanged = new Subject();
  doneChanged = new Subject();
  customDirsChanged = new Subject();
  ytdlOptionsChanged = new Subject();
  configurationChanged = new Subject();
  updated = new Subject();

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  configuration: any = {};
  customDirs = {};

  constructor() {
    this.socket.fromEvent('all')
    .pipe(takeUntilDestroyed())
    .subscribe((strdata: string) => {
      this.loading = false;
      const data: [[[string, Download]], [[string, Download]]] = JSON.parse(strdata);
      this.queue.clear();
      data[0].forEach(entry => this.queue.set(...entry));
      this.done.clear();
      data[1].forEach(entry => this.done.set(...entry));
      this.queueChanged.next(null);
      this.doneChanged.next(null);
    });
    this.socket.fromEvent('added')
    .pipe(takeUntilDestroyed())
    .subscribe((strdata: string) => {
      const data: Download = JSON.parse(strdata);
      this.queue.set(data.url, data);
      this.queueChanged.next(null);
    });
    this.socket.fromEvent('updated')
    .pipe(takeUntilDestroyed())
    .subscribe((strdata: string) => {
      const data: Download = JSON.parse(strdata);
      const dl: Download | undefined  = this.queue.get(data.url);
      data.checked = !!dl?.checked;
      data.deleting = !!dl?.deleting;
      this.queue.set(data.url, data);
      this.updated.next(null);
    });
    this.socket.fromEvent('completed')
    .pipe(takeUntilDestroyed())
    .subscribe((strdata: string) => {
      const data: Download = JSON.parse(strdata);
      this.queue.delete(data.url);
      this.done.set(data.url, data);
      this.queueChanged.next(null);
      this.doneChanged.next(null);
    });
    this.socket.fromEvent('canceled')
    .pipe(takeUntilDestroyed())
    .subscribe((strdata: string) => {
      const data: string = JSON.parse(strdata);
      this.queue.delete(data);
      this.queueChanged.next(null);
    });
    this.socket.fromEvent('cleared')
    .pipe(takeUntilDestroyed())
    .subscribe((strdata: string) => {
      const data: string = JSON.parse(strdata);
      this.done.delete(data);
      this.doneChanged.next(null);
    });
    this.socket.fromEvent('configuration')
    .pipe(takeUntilDestroyed())
    .subscribe((strdata: string) => {
      const data = JSON.parse(strdata);
      console.debug("got configuration:", data);
      this.configuration = data;
      this.configurationChanged.next(data);
    });
    this.socket.fromEvent('custom_dirs')
    .pipe(takeUntilDestroyed())
    .subscribe((strdata: string) => {
      const data = JSON.parse(strdata);
      console.debug("got custom_dirs:", data);
      this.customDirs = data;
      this.customDirsChanged.next(data);
    });
    this.socket.fromEvent('ytdl_options_changed')
    .pipe(takeUntilDestroyed())
    .subscribe((strdata: string) => {
      const data = JSON.parse(strdata);
      this.ytdlOptionsChanged.next(data);
    });
  }

  handleHTTPError(error: HttpErrorResponse) {
    const msg = error.error instanceof ErrorEvent ? error.error.message : error.error;
    return of({status: 'error', msg: msg})
  }

  public add(
    url: string,
    downloadType: string,
    codec: string,
    quality: string,
    format: string,
    folder: string,
    customNamePrefix: string,
    playlistItemLimit: number,
    autoStart: boolean,
    splitByChapters: boolean,
    chapterTemplate: string,
    subtitleLanguage: string,
    subtitleMode: string,
  ) {
    return this.http.post<Status>('add', {
      url: url,
      download_type: downloadType,
      codec: codec,
      quality: quality,
      format: format,
      folder: folder,
      custom_name_prefix: customNamePrefix,
      playlist_item_limit: playlistItemLimit,
      auto_start: autoStart,
      split_by_chapters: splitByChapters,
      chapter_template: chapterTemplate,
      subtitle_language: subtitleLanguage,
      subtitle_mode: subtitleMode,
    }).pipe(
      catchError(this.handleHTTPError)
    );
  }

  public startById(ids: string[]) {
    return this.http.post('start', {ids: ids});
  }

  public delById(where: State, ids: string[]) {
    const map = this[where];
    if (map) {
      for (const id of ids) {
        const obj = map.get(id);
        if (obj) {
          obj.deleting = true;
        }
      }
    }
    return this.http.post('delete', {where: where, ids: ids});
  }

  public startByFilter(where: State, filter: (dl: Download) => boolean) {
    const ids: string[] = [];
    this[where].forEach((dl: Download) => { if (filter(dl)) ids.push(dl.url) });
    return this.startById(ids);
  }

  public delByFilter(where: State, filter: (dl: Download) => boolean) {
    const ids: string[] = [];
    this[where].forEach((dl: Download) => { if (filter(dl)) ids.push(dl.url) });
    return this.delById(where, ids);
  }
  public addDownloadByUrl(url: string): Promise<{
    response: Status} | {
    status: string;
    msg?: string;
  }> {
    const defaultDownloadType = 'video';
    const defaultCodec = 'auto';
    const defaultQuality = 'best';
    const defaultFormat = 'mp4';
    const defaultFolder = ''; 
    const defaultCustomNamePrefix = '';
    const defaultPlaylistItemLimit = 0;
    const defaultAutoStart = true;
    const defaultSplitByChapters = false;
    const defaultChapterTemplate = this.configuration['OUTPUT_TEMPLATE_CHAPTER'];
    const defaultSubtitleLanguage = 'en';
    const defaultSubtitleMode = 'prefer_manual';

    return new Promise((resolve, reject) => {
      this.add(
        url,
        defaultDownloadType,
        defaultCodec,
        defaultQuality,
        defaultFormat,
        defaultFolder,
        defaultCustomNamePrefix,
        defaultPlaylistItemLimit,
        defaultAutoStart,
        defaultSplitByChapters,
        defaultChapterTemplate,
        defaultSubtitleLanguage,
        defaultSubtitleMode,
      )
        .subscribe({
          next: (response) => resolve(response),
          error: (error) => reject(error)
        });
    });
  }
  public exportQueueUrls(): string[] {
    return Array.from(this.queue.values()).map(download => download.url);
  }
  public cancelAdd() {
    return this.http.post<Status>('cancel-add', {}).pipe(
      catchError(this.handleHTTPError)
    );
  }

  uploadCookies(file: File) {
    const formData = new FormData();
    formData.append('cookies', file);
    return this.http.post<{ status: string; msg?: string }>('upload-cookies', formData).pipe(
      catchError(this.handleHTTPError)
    );
  }

  deleteCookies() {
    return this.http.post<{ status: string; msg?: string }>('delete-cookies', {}).pipe(
      catchError(this.handleHTTPError)
    );
  }

  getCookieStatus() {
    return this.http.get<{ status: string; has_cookies: boolean }>('cookie-status').pipe(
      catchError(this.handleHTTPError)
    );
  }
}
```

## File: `ui/src/app/services/index.ts`
```typescript
export { DownloadsService } from './downloads.service';
export { SpeedService } from './speed.service';
export { MeTubeSocket } from './metube-socket.service';
```

## File: `ui/src/app/services/metube-socket.service.ts`
```typescript
import { Injectable, inject } from '@angular/core';
import { ApplicationRef } from '@angular/core';
import { Socket } from 'ngx-socket-io';

@Injectable(
  { providedIn: 'root' }
)
export class MeTubeSocket extends Socket {

  constructor() {
    const appRef = inject(ApplicationRef);

    const path =
      document.location.pathname.replace(/share-target/, '') + 'socket.io';
    super({ url: '', options: { path } }, appRef);
  }
}
```

## File: `ui/src/app/services/speed.service.ts`
```typescript
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, interval } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SpeedService {
  private speedBuffer = new BehaviorSubject<number[]>([]);
  private readonly BUFFER_SIZE = 10; // Keep last 10 measurements (1 second at 100ms intervals)

  // Observable that emits the mean speed every second
  public meanSpeed$: Observable<number>;

  constructor() {
    // Calculate mean speed every second
    this.meanSpeed$ = interval(1000).pipe(
      map(() => {
        const speeds = this.speedBuffer.value;
        if (speeds.length === 0) return 0;
        return speeds.reduce((sum, speed) => sum + speed, 0) / speeds.length;
      })
    );
  }

  // Add a new speed measurement
  public addSpeedMeasurement(speed: number) {
    const currentBuffer = this.speedBuffer.value;
    const newBuffer = [...currentBuffer, speed].slice(-this.BUFFER_SIZE);
    this.speedBuffer.next(newBuffer);
  }

  // Get the current mean speed
  public getCurrentMeanSpeed(): number {
    const speeds = this.speedBuffer.value;
    if (speeds.length === 0) return 0;
    return speeds.reduce((sum, speed) => sum + speed, 0) / speeds.length;
  }
} 
```

## File: `ui/src/assets/icons/browserconfig.xml`
```xml
<?xml version="1.0" encoding="utf-8"?>
<browserconfig>
    <msapplication>
        <tile>
            <square150x150logo src="favicon/mstile-150x150.png"/>
            <TileColor>#da532c</TileColor>
        </tile>
    </msapplication>
</browserconfig>
```

