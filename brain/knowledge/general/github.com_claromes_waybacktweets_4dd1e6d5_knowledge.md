---
id: github.com-claromes-waybacktweets-4dd1e6d5-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:39.278187
---

# KNOWLEDGE EXTRACT: github.com_claromes_waybacktweets_4dd1e6d5
> **Extracted on:** 2026-04-01 15:36:53
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524634/github.com_claromes_waybacktweets_4dd1e6d5

---

## File: `.gitignore`
```
*.csv
*.json
*.html
*.txt

test.py

waybacktweets/__pycache__
waybacktweets/api/__pycache__
waybacktweets/config/__pycache__
waybacktweets/exceptions/__pycache__
waybacktweets/utils/__pycache__

dist
brain/knowledge/docs_legacy/_build/
!brain/knowledge/docs_legacy/_templates/**
```

## File: `.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        additional_dependencies: ["Flake8-pyproject"]
  - repo: https://github.com/PyCQA/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args:
          - --profile=black
```

## File: `CITATION.cff`
```
# This CITATION.cff file was generated with cffinit.
# Visit https://bit.ly/cffinit to generate yours today!

cff-version: 1.2.0
title: Wayback Tweets
message: >-
  If you use this software, please cite it using the
  metadata from this file.
type: software
authors:
  - given-names: Clarissa
    family-names: Mendes
    email: support@claromes.com
identifiers:
  - type: doi
    value: 10.5281/zenodo.12528447
    description: Retrieves archived tweets from Wayback Machine in HTML, CSV, and JSON.
  - type: url
    value: "https://pypi.org/project/waybacktweets/"
    description: Python Package Index.
  - type: url
    value: "https://waybacktweets.claromes.com/"
    description: Documentation.
repository-code: "https://github.com/claromes/waybacktweets"
url: "https://waybacktweets.claromes.com/"
abstract: >-
  Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data in HTML, for easy viewing of the tweets using the iframe tags, CSV, and JSON formats.
keywords:
  - Twitter
  - X
  - Tweets
  - Wayback Machine
  - OSINT
  - SOCMINT
  - Python
license: GPL-3.0
version: 1.0
date-released: "2025-05-26"
```

## File: `LICENSE.md`
```markdown
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

                            Preamble

The GNU General Public License is a free, copyleft license for
software and other kinds of works.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works. By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users. We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors. You can apply it to
your programs, too.

When we speak of free software, we are referring to freedom, not
price. Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights. Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received. You must make sure that they, too, receive
or can get the source code. And you must show them these terms so they
know their rights.

Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software. For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so. This is fundamentally incompatible with the aim of
protecting users' freedom to change the software. The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable. Therefore, we
have designed this version of the GPL to prohibit the practice for those
products. If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary. To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

0. Definitions.

"This License" refers to version 3 of the GNU General Public License.

"Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

"The Program" refers to any copyrightable work licensed under this
License. Each licensee is addressed as "you". "Licensees" and
"recipients" may be individuals or organizations.

To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy. The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

A "covered work" means either the unmodified Program or a work based
on the Program.

To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy. Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

To "convey" a work means any kind of propagation that enables other
parties to make or receive copies. Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License. If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

1. Source Code.

The "source code" for a work means the preferred form of the work
for making modifications to it. "Object code" means any non-source
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
implementation is available to the public in source code form. A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities. However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work. For example, Corresponding Source
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
conditions are met. This License explicitly affirms your unlimited
permission to run the unmodified Program. The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work. This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force. You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright. Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

Conveying under any other circumstances is permitted solely under
the conditions stated below. Sublicensing is not allowed; section 10
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
beyond what the individual works permit. Inclusion of a covered work
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
into a dwelling. In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage. For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product. A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

"Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source. The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information. But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed. Access to a
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
that they are valid under applicable law. If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it. (Additional permissions may be written to require their own
removal in certain cases when you modify the work.) You may place
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
restrictions" within the meaning of section 10. If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term. If a license document contains
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
provided under this License. Any attempt otherwise to propagate or
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
this License. If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

9. Acceptance Not Required for Having Copies.

You are not required to accept this License in order to receive or
run a copy of the Program. Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance. However,
nothing other than this License grants you permission to propagate or
modify any covered work. These actions infringe copyright if you do
not accept this License. Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

10. Automatic Licensing of Downstream Recipients.

Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License. You are not responsible
for enforcing compliance by third parties with this License.

An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations. If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License. For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

11. Patents.

A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based. The
work thus licensed is called the contributor's "contributor version".

A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version. For
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
sue for patent infringement). To "grant" such a patent license to a
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
license to downstream recipients. "Knowingly relying" means you have
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
specifically granted under this License. You may not convey a covered
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
excuse you from the conditions of this License. If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all. For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

13. Use with the GNU Affero General Public License.

Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work. The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

14. Revised Versions of this License.

The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time. Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number. If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation. If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

Later license versions may give you additional or different
permissions. However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

15. Disclaimer of Warranty.

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
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

To do so, attach the following notices to the program. It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    Wayback Tweets - Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data.
    Copyright (C) 2023  Clarissa Mendes (Claromes)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    Wayback Tweets  Copyright (C) 2023  Clarissa Mendes (Claromes)
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License. Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

The GNU General Public License does not permit incorporating your program
into proprietary programs. If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.
```

## File: `README.md`
```markdown
# Wayback Tweets

[![PyPI](https://img.shields.io/pypi/v/waybacktweets)](https://pypi.org/project/waybacktweets) [![PyPI Downloads](https://static.pepy.tech/badge/waybacktweets)](https://pepy.tech/projects/waybacktweets)

Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing (see [Field Options](https://waybacktweets.claromes.com/field_options)), and saves the data in HTML, for easy viewing of the tweets using the iframe tags, CSV, and JSON formats.

## Installation

It is compatible with Python versions 3.10 and above. [See installation options](https://waybacktweets.claromes.com/installation).

```shell
pipx install waybacktweets
```

## CLI

```shell
Usage:
  waybacktweets [OPTIONS] USERNAME
  USERNAME: The Twitter username without @

Options:
  -c, --collapse [urlkey|digest|timestamp:xx]
                                  Collapse results based on a field, or a
                                  substring of a field. XX in the timestamp
                                  value ranges from 1 to 14, comparing the
                                  first XX digits of the timestamp field. It
                                  is recommended to use from 4 onwards, to
                                  compare at least by years.
  -f, --from DATE                 Filtering by date range from this date.
                                  Format: YYYYmmdd
  -t, --to DATE                   Filtering by date range up to this date.
                                  Format: YYYYmmdd
  -l, --limit INTEGER             Query result limits.
  -rk, --resumption_key TEXT      Allows for a simple way to scroll through
                                  the results. Key to continue the query from
                                  the end of the previous query.
  -mt, --matchtype [exact|prefix|host|domain]
                                  Results matching a certain prefix, a certain
                                  host or all subdomains.
  -v, --verbose                   Shows the log.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.

Examples:
  waybacktweets jack
  waybacktweets --from 20200305 --to 20231231 --limit 300 --verbose jack

Repository:
  https://github.com/claromes/waybacktweets

Documentation:
  https://waybacktweets.claromes.com
```

## Module

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tnaM3rMWpoSHBZ4P_6iHFPjraWRQ3OGe?usp=sharing)

```python
from waybacktweets import WaybackTweets, TweetsParser, TweetsExporter

USERNAME = "jack"

api = WaybackTweets(USERNAME)
archived_tweets = api.get()

if archived_tweets:
    field_options = [
        "archived_urlkey",
        "archived_timestamp",
        "parsed_archived_timestamp",
        "archived_tweet_url",
        "parsed_archived_tweet_url",
        "original_tweet_url",
        "parsed_tweet_url",
        "available_tweet_text",
        "available_tweet_is_RT",
        "available_tweet_info",
        "archived_mimetype",
        "archived_statuscode",
        "archived_digest",
        "archived_length",
        "resumption_key",
    ]

    parser = TweetsParser(archived_tweets, USERNAME, field_options)
    parsed_tweets = parser.parse()

    exporter = TweetsExporter(parsed_tweets, USERNAME, field_options)
    exporter.save_to_csv()
    exporter.save_to_json()
    exporter.save_to_html()
```

## Web App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://waybacktweets.streamlit.app)

A prototype written in Python with the Streamlit framework and hosted on Streamlit Cloud.

Important: Starting from version 1.0, the web app will no longer receive all updates from the official package. To access all features, prefer using the package from PyPI.

## Documentation

- [Wayback Tweets documentation](https://waybacktweets.claromes.com/).
- [Wayback CDX Server API (Beta) documentation](https://archive.org/developers/wayback-cdx-server.html).

## Acknowledgements

- Tristan Lee (Bellingcat's Data Scientist) for the idea.
- Jessica Smith (Snowflake's Community Growth Specialist) and Streamlit team for the additional server resources on Streamlit Cloud.
- OSINT Community for recommending the package and the application.

## License

[GPL-3.0](LICENSE.md)
```

## File: `pyproject.toml`
```
[tool.poetry]
name = "waybacktweets"
version = "1.0"
description = "Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data."
authors = ["Claromes <support@claromes.com>"]
license = "GPLv3"
readme = "README.md"
repository = "https://github.com/claromes/waybacktweets"
keywords = [
    "Twitter",
    "X",
    "tweet",
    "Internet Archive",
    "Wayback Machine",
    "OSINT",
    "SOCMINT",
]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Natural Language :: English",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development",
    "Topic :: Utilities",
]
exclude = ["app/**", "legacy_app/**", ".streamlit/**", "assets/**", "brain/knowledge/docs_legacy/**", "build/**", ".github/**", ".git/**", ".gitignore", ".pre-commit-config.yaml", "CITATION.cff"]

[tool.poetry.urls]
"Homepage" = "https://waybacktweets.claromes.com/"
"Documentation" = "https://waybacktweets.claromes.com/"
"Issue Tracker" = "https://github.com/claromes/waybacktweets/issues"

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.30.0"
rich = "^13.6.0"
click = "^8.1.7"
pandas = "^2.2.2"

[tool.poetry.group.docs.dependencies]
sphinx = "^7.3.7"
pallets-sphinx-themes = "^2.1.3"
sphinxcontrib-mermaid = "^0.9.2"
sphinx-new-tab-link = "^0.4.0"
sphinx-click = "^6.0.0"
sphinx-autodoc-typehints = "^2.1.1"
sphinxcontrib-youtube = "^1.4.1"

[tool.poetry.group.dev.dependencies]
streamlit = "1.45.0"
black = "^24.4.2"
flake8 = "^7.0.0"
isort = "^5.13.2"
pre-commit = "^3.7.1"
flake8-pyproject = "^1.2.3"

[tool.isort]
profile = "black"

[tool.flake8]
max-line-length = 88
extend-ignore = ["E203", "E701"]

[tool.poetry.scripts]
waybacktweets = 'waybacktweets._cli:main'

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## File: `app/app.py`
```python
from datetime import datetime, timedelta

import streamlit as st
import streamlit.components.v1 as components

from waybacktweets.api.export import TweetsExporter
from waybacktweets.api.parse import TweetsParser
from waybacktweets.api.request import WaybackTweets
from waybacktweets.api.visualize import HTMLTweetsVisualizer
from waybacktweets.config import config

# ------ Initial Settings ------ #

PAGE_ICON = "assets/parthenon.png"
TITLE = "assets/waybacktweets.png"
FIELD_OPTIONS = [
    "archived_urlkey",
    "archived_timestamp",
    "parsed_archived_timestamp",
    "archived_tweet_url",
    "parsed_archived_tweet_url",
    "original_tweet_url",
    "parsed_tweet_url",
    "available_tweet_text",
    "available_tweet_is_RT",
    "available_tweet_info",
    "archived_mimetype",
    "archived_statuscode",
    "archived_digest",
    "archived_length",
]

collapse = None
matchtype = None
start_date = datetime.now() - timedelta(days=30 * 6)
end_date = datetime.now()
min_date = datetime(2006, 1, 1)

# ------ Verbose Mode Configuration ------ #

config.verbose = False

# ------ Page Configuration ------ #

st.set_page_config(
    page_title="Wayback Tweets",
    page_icon=PAGE_ICON,
    layout="centered",
    menu_items={
        "About": f"""
© 2023-{end_date.year} [Claromes](https://claromes.com). Licensed under the [GPL-3.0](https://raw.githubusercontent.com/claromes/waybacktweets/refs/heads/main/LICENSE.md). Icon by The Doodle Library. Title font by Google, licensed under the Open Font License (OFL).

---
""",  # noqa: E501
        "Report a bug": "https://github.com/claromes/waybacktweets/issues",
    },
)

# ------ Set States and Params ------ #

if "current_username" not in st.session_state:
    st.session_state.current_username = ""

if "count" not in st.session_state:
    st.session_state.count = False

if "archived_timestamp_filter" not in st.session_state:
    st.session_state.archived_timestamp_filter = (start_date, end_date)

if "username_value" not in st.session_state:
    st.session_state.username_value = ""

if "expanded_value" not in st.session_state:
    st.session_state.expanded_value = False

if "query" not in st.session_state:
    st.session_state.query = False

if "update_component" not in st.session_state:
    st.session_state.update_component = 0

if "username" not in st.query_params:
    st.query_params["username"] = ""

# ------ Add Custom CSS Style ------ #

st.html(
    """
    <style>
        header[data-testid="stHeader"] {
            opacity: 0.5;
        }
        iframe {
            border: 1px solid #dddddd;
            border-radius: 0.5rem;
        }
        div[data-testid="InputInstructions"] {
            visibility: hidden;
        }
        button[data-testid="StyledFullScreenButton"] {
            display: none;
        }
        div[class="st-emotion-cache-1v0mbdj e115fcil1"] {
            max-width: 100%;
        }
        div[data-testid="stElementToolbarButtonContainer"] {
            display: none;
        }
    </style>
    """
)

# ------ Functions ------ #


@st.cache_data(ttl=600, show_spinner=False)
def wayback_tweets(
    username,
    collapse,
    timestamp_from,
    timestamp_to,
    limit,
    matchtype,
):
    response = WaybackTweets(
        username,
        collapse,
        timestamp_from,
        timestamp_to,
        limit,
        matchtype,
    )
    archived_tweets = response.get()

    return archived_tweets


@st.cache_data(ttl=600, show_spinner=False)
def tweets_parser(archived_tweets, username, field_options):
    parser = TweetsParser(archived_tweets, username, field_options)
    parsed_tweets = parser.parse()

    return parsed_tweets


@st.cache_data(ttl=600, show_spinner=False)
def tweets_exporter(parsed_tweets, username, field_options):
    exporter = TweetsExporter(parsed_tweets, username, field_options)

    df = exporter.dataframe
    file_name = exporter.filename

    return df, file_name


# ------ Custom JavaScript ------ #


def scroll_page():
    js = f"""
    <script>
        window.parent.document.querySelector('section.main').scrollTo(700, 700);
        let update_component = {st.session_state.update_component} // Force component update to generate scroll
    </script>
    """  # noqa: E501

    components.html(js, width=0, height=0)


# ------ Query Param ------ #

if st.query_params.username != "":
    st.session_state.username_value = st.query_params.username
    st.session_state.expanded_value = True
    st.session_state.query = True

    st.session_state.update_component += 1
    scroll_page()

# ------ UI Settings ------ #

st.image(TITLE, width=None)
st.write(
    "Retrieves archived tweets CDX data in HTML, CSV, and JSON formats."  # noqa: E501
)

st.write(
    "This application is a prototype based on the Python package and does not include all available features. To explore the package, including CLI and Module usage, visit the [GitHub repository](https://github.com/claromes/waybacktweets)."  # noqa: E501
)

st.divider()

# -- Filters -- #

username = st.text_input(
    "Username",
    value=st.session_state.username_value,
    key="username",
    placeholder="Without @",
)

st.session_state.archived_timestamp_filter = st.date_input(
    "Tweets saved between",
    (start_date, end_date),
    min_date,
    end_date,
    format="YYYY/MM/DD",
    help="Using the `from` and `to` filters. Format: YYYY/MM/DD",
)
st.caption(
    ":gray[Note: Large date ranges may take longer to process and exceed the app's resource limits. Use smaller ranges for faster results.]"  # noqa: E501
)

limit = st.text_input(
    "Limit",
    key="limit",
    help="Query result limits (int)",
)

unique = st.checkbox(
    "Only unique Wayback Machine URLs",
    key="unique",
    help="Filtering by the collapse option using the `urlkey` field and the URL Match Scope `prefix`",  # noqa: E501
)
st.caption(
    ":gray[Note: As noted in the official Wayback CDX Server API documentation, retrieving unique URLs may experience slow performance at this time.]"  # noqa: E501
)


query = st.button("Go", type="primary", use_container_width=True)

if st.query_params.username == "":
    st.query_params.clear()
    st.session_state.query = query

# ------ Results ------ #

if username != st.session_state.current_username:
    st.session_state.current_username = username

if (st.session_state.query and username) or st.session_state.count:
    if unique:
        collapse = "urlkey"
        matchtype = "prefix"

    try:
        with st.spinner(f"Retrieving @{st.session_state.current_username}..."):
            wayback_tweets = wayback_tweets(
                st.session_state.current_username,
                collapse,
                st.session_state.archived_timestamp_filter[0],
                st.session_state.archived_timestamp_filter[1],
                limit,
                matchtype,
            )

        if not wayback_tweets:
            st.error("No data was saved due to an empty response.")
            st.stop()

        with st.spinner(f"Parsing @{st.session_state.current_username}..."):
            parsed_tweets = tweets_parser(
                wayback_tweets, st.session_state.current_username, FIELD_OPTIONS
            )

            df, file_name = tweets_exporter(
                parsed_tweets, st.session_state.current_username, FIELD_OPTIONS
            )

        csv_data = df.to_csv(index=False)
        json_data = df.to_json(orient="records", lines=False)
        html = HTMLTweetsVisualizer(username, json_data)
        html_content = html.generate()

        # -- Rendering -- #

        st.session_state.count = len(df)
        st.caption(f"{st.session_state.count} URLs have been captured.")

        tab1, tab2, tab3 = st.tabs(["HTML", "CSV", "JSON"])

        # -- HTML -- #
        with tab1:
            st.download_button(
                label=f"Download @{st.session_state.current_username} in HTML",
                data=html_content,
                file_name=f"{file_name}.html",
                mime="text/html",
                icon=":material/download:",
            )

            st.caption("Note: The iframes are best viewed in Firefox.")

            # -- CSV -- #
        with tab2:
            st.download_button(
                label=f"Download @{st.session_state.current_username} in CSV",
                data=csv_data,
                file_name=f"{file_name}.csv",
                mime="text/csv",
                icon=":material/download:",
            )

            st.caption("Preview:")
            st.dataframe(df, use_container_width=True)

            # -- JSON -- #
        with tab3:
            st.download_button(
                label=f"Download @{st.session_state.current_username} in JSON",
                data=json_data,
                file_name=f"{file_name}.json",
                mime="application/json",
                icon=":material/download:",
            )

            st.caption("Preview:")
            st.json(json_data, expanded=1)
    except TypeError as e:
        st.error(
            f"""
        {e}. Refresh this page and try again.

        If the problem persists [open an issue](https://github.com/claromes/waybacktweets/issues)."""  # noqa: E501
        )
        st.stop()
    except IndexError:
        st.error("Please check if you have entered a date range in the filter.")
        st.stop()
    except Exception as e:
        st.error(str(e))
        st.stop()
```

## File: `app/requirements.txt`
```
streamlit==1.45.0
waybacktweets
```

## File: `brain/knowledge/docs_legacy/Makefile`
```
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
```

## File: `brain/knowledge/docs_legacy/api.rst`
```
.. _api:

API
====

Request
---------

.. automodule:: waybacktweets.api.request

.. autoclass:: WaybackTweets
    :members:

.. _parser:

Parse
---------

.. automodule:: waybacktweets.api.parse

.. autoclass:: TweetsParser
    :members:
    :private-members:

.. autoclass:: TwitterEmbed
    :members:

.. autoclass:: JsonParser
    :members:

.. _exporter:

Export
---------

.. automodule:: waybacktweets.api.export

.. autoclass:: TweetsExporter
    :members:
    :private-members:

Visualize
-----------

.. automodule:: waybacktweets.api.visualize

.. autoclass:: HTMLTweetsVisualizer
    :members:
    :private-members:

.. _utils:

Utils
-------

.. automodule:: waybacktweets.utils.utils

.. autofunction:: check_double_status
.. autofunction:: check_pattern_tweet
.. autofunction:: check_url_scheme
.. autofunction:: clean_tweet_url
.. autofunction:: clean_wayback_machine_url
.. autofunction:: delete_tweet_pathnames
.. autofunction:: get_response
.. autofunction:: is_tweet_url
.. autofunction:: semicolon_parser
.. autofunction:: timestamp_parser


Config
------------

.. automodule:: waybacktweets.config.config
    :members:
```

## File: `brain/knowledge/docs_legacy/cli.rst`
```
CLI
================

Usage
---------

.. click:: waybacktweets._cli:main
   :prog: waybacktweets
   :nested: full

Examples
---------

``waybacktweets jack``

``waybacktweets --from 20200305 --to 20231231 --limit 300 --verbose jack``

``waybacktweets -f 20200305 -t 20231231 -l 300 -v jack``

Collapsing
------------

The Wayback Tweets command line tool recommends the use of three types of "collapse": ``urlkey``, ``digest``, and ``timestamp`` field.

- ``urlkey``: (`str`) A canonical transformation of the URL you supplied, for example, ``org,eserver,tc)/``. Such keys are useful for indexing.

- ``digest``: (`str`) The ``SHA1`` hash digest of the content, excluding the headers. It's usually a base-32-encoded string.

- ``timestamp``: (`datetime`) A 14 digit date-time representation in the ``YYYYMMDDhhmmss`` format. We recommend ``YYYYMMDD``.

However, it is possible to use it with other options. Read below text extracted from the official Wayback CDX Server API (Beta) documentation.

.. note::

   A new form of filtering is the option to "collapse" results based on a field, or a substring of a field. Collapsing is done on adjacent CDX lines where all captures after the first one that are duplicate are filtered out. This is useful for filtering out captures that are "too dense" or when looking for unique captures.

   To use collapsing, add one or more ``collapse=field`` or ``collapse=field:N`` where ``N`` is the first ``N`` characters of field to test.

   - Ex: Only show at most 1 capture per hour (compare the first 10 digits of the ``timestamp`` field). Given 2 captures ``20130226010000`` and ``20130226010800``, since first 10 digits ``2013022601`` match, the 2nd capture will be filtered out:

      http://web.archive.org/cdx/search/cdx?url=google.com&collapse=timestamp:10

      The calendar page at `web.archive.org` uses this filter by default: `http://web.archive.org/web/*/archive.org`

   - Ex: Only show unique captures by ``digest`` (note that only adjacent digest are collapsed, duplicates elsewhere in the cdx are not affected):

      http://web.archive.org/cdx/search/cdx?url=archive.org&collapse=digest

   - Ex: Only show unique urls in a prefix query (filtering out captures except first capture of a given url). This is similar to the old prefix query in wayback (note: this query may be slow at the moment):

      http://web.archive.org/cdx/search/cdx?url=archive.org&collapse=urlkey&matchType=prefix


URL Match Scope
-----------------

The CDX Server can return results matching a certain prefix, a certain host or all subdomains by using the ``matchType`` param.

The package ``waybacktweets`` uses the pathname ``/status`` followed by the wildcard '*' at the end of the URL to retrieve only tweets. However, if a value is provided for this parameter, the search will be made from the URL `twitter.com/<USERNAME>`.

Read below text extracted from the official Wayback CDX Server API (Beta) documentation.

.. note::

   For example, if given the url: archive.org/about/ and:

   - ``matchType=exact`` (default if omitted) will return results matching exactly archive.org/about/

   - ``matchType=prefix`` will return results for all results under the path archive.org/about/

      http://web.archive.org/cdx/search/cdx?url=archive.org/about/&matchType=prefix&limit=1000

   - ``matchType=host`` will return results from host archive.org

      http://web.archive.org/cdx/search/cdx?url=archive.org/about/&matchType=host&limit=1000

   - ``matchType=domain`` will return results from host archive.org and all subhosts \*.archive.org

      http://web.archive.org/cdx/search/cdx?url=archive.org/about/&matchType=domain&limit=1000

   The matchType may also be set implicitly by using wildcard '*' at end or beginning of the url:

   - If url is ends in '/\*', eg url=archive.org/\* the query is equivalent to url=archive.org/&matchType=prefix
   - If url starts with '\*.', eg url=\*.archive.org/ the query is equivalent to url=archive.org/&matchType=domain

   (Note: The domain mode is only available if the CDX is in `SURT <http://crawler.archive.org/articles/user_manual/glossary.html#surt>`_-order format.)
```

## File: `brain/knowledge/docs_legacy/conf.py`
```python
import datetime

from pallets_sphinx_themes import ProjectLink, get_version

project = "Wayback Tweets"
release, version = get_version("waybacktweets")
rst_epilog = f".. |release| replace:: v{release}"
copyright = f"2023 - {datetime.datetime.now().year}, Claromes · Icon by The Doodle Library · Title font by Google, licensed under the Open Font License · Release: v{release}"  # noqa: E501
author = "Claromes"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "pallets_sphinx_themes",
    "sphinxcontrib.mermaid",
    "sphinx_new_tab_link",
    "sphinx_click.ext",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.youtube",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
autodoc_typehints = "description"

# -- Options for HTML output -------------------------------------------------

html_theme = "flask"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_context = {
    "project_links": [
        ProjectLink("PyPI", "https://pypi.org/project/waybacktweets/"),
        ProjectLink("Source Code", "https://github.com/claromes/waybacktweets/"),
        ProjectLink(
            "License",
            "https://raw.githubusercontent.com/claromes/waybacktweets/refs/heads/main/LICENSE.md",  # noqa: E501
        ),
        ProjectLink(
            "Issue Tracker", "https://github.com/claromes/waybacktweets/issues/"
        ),
        ProjectLink("Mastodon", "https://ruby.social/@claromes"),
        ProjectLink("Bluesky", "https://bsky.app/profile/claromes.com"),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html"],
}
html_favicon = "../assets/parthenon.png"
html_logo = "../assets/parthenon.png"
html_title = f"Wayback Tweets Documentation ({version})"
html_show_sourcelink = False
```

## File: `brain/knowledge/docs_legacy/contribute.rst`
```
Contribute
================

Here are all the ways you can contribute to this project.

Testing
---------

The best way to help is by using the package, either on the command line or as a module, suggesting improvements and reporting bugs. You're very welcome to `open an issue <https://github.com/claromes/waybacktweets/issues/>`_.


Hacking
---------

If you have Python skills, contribute to the `code <https://github.com/claromes/waybacktweets/>`_.

These are the prerequisites:

- Python 3.10+
- Poetry

Install from the source, following the :ref:`installation_from_source` instructions.

Brief explanation about the code under the Wayback Tweets directory:

- ``app``: Streamlit application code
- ``assets``: Title and logo images
- ``docs``: Documentation generated with Sphinx
- ``legacy_app``: Legacy Streamlit application code
- ``waybacktweets/api``: Main package modules
- ``waybacktweets/config``: Global configuration module
- ``waybacktweets/exceptions``: Wayback Tweets Exceptions
- ``waybacktweets/utils``: Helper functions used in the package
```

## File: `brain/knowledge/docs_legacy/exceptions.rst`
```
Exceptions
================

These are the most common errors and are handled by the ``waybacktweets`` package.

ReadTimeoutError
------------------

This error occurs when a request to the web.archive.org server takes too long to respond. The server could be overloaded or there could be network issues.

The output message from the package would be: ``Connection to web.archive.org timed out.``

ConnectionError
------------------

This error is raised when the package fails to establish a new connection with web.archive.org. This could be due to network issues or the server being down.

The output message from the package would be: ``Failed to establish a new connection with web.archive.org. Max retries exceeded.``


This is the error often returned when performing experimental parsing of URLs with the mimetype ``application/json``.

The warning output message from the package would be: ``Connection error with https://web.archive.org/web/<TIMESTAMP>/https://twitter.com/<USERNAME>/status/<TWEET_ID>. Max retries exceeded. Error parsing the JSON, but the CDX data was saved.``

HTTPError
------------------

This error occurs when the Internet Archive services are temporarily offline. This could be due to maintenance or server issues.

The output message from the package would be: ``Temporarily Offline: Internet Archive services are temporarily offline. Please check Internet Archive Twitter feed (https://twitter.com/internetarchive) for the latest information.``

EmptyResponseError
---------------------

This exception raised for empty responses.

The output message from the package would be: ``No data was saved due to an empty response.``

Warning
------------------

It is possible to encounter the following warning when running the ``TweetsParser`` class (:ref:`parser`): ``<TWEET_URL> not available on the user's Twitter account, but the CDX data was saved.``

This occurs when the original tweet is no longer available on Twitter and has possibly been deleted.
```

## File: `brain/knowledge/docs_legacy/field_options.rst`
```
.. _field_options:

Field Options
================

The package performs several parses to facilitate the analysis of archived tweets and types of tweets. The fields below are available, which can be passed to the :ref:`parser` and :ref:`exporter`, in addition, the command line tool returns all these fields.

- ``archived_urlkey``: (`str`) A canonical transformation of the URL you supplied, for example, ``org,eserver,tc)/``. Such keys are useful for indexing.

- ``archived_timestamp``: (`str`) A 14 digit date-time representation in the ``YYYYMMDDhhmmss`` format.

- ``parsed_archived_timestamp``: (`str`) The ``archived_timestamp`` in human-readable format.

- ``archived_tweet_url``: (`str`) The archived URL.

- ``parsed_archived_tweet_url``: (`str`) The archived URL after parsing. It is not guaranteed that this option will be archived, it is just a facilitator, as the originally archived URL does not always exist, due to changes in URLs and web services of the social network Twitter. Check the :ref:`utils`.

- ``original_tweet_url``: (`str`) The original tweet URL.

- ``parsed_tweet_url``: (`str`) The original tweet URL after parsing. Old URLs were archived in a nested manner. The parsing applied here unnests these URLs, when necessary.  Check the :ref:`utils`.

- ``available_tweet_text``: (`str`) The tweet text extracted from the URL that is still available on the Twitter account.

- ``available_tweet_is_RT``: (`bool`) Whether the tweet from the ``available_tweet_text`` field is a retweet or not.

- ``available_tweet_info``: (`str`) Name and date of the tweet from the ``available_tweet_text`` field.

- ``archived_mimetype``: (`str`) The mimetype of the archived content, which can be one of these:

    - ``text/html``

    - ``warc/revisit``

    - ``application/json``

    - ``unk``

- ``archived_statuscode``: (`str`) The HTTP status code of the snapshot. If the mimetype is ``warc/revisit``, the value returned for the ``statuscode`` key can be blank, but the actual value is the same as that of any other entry that has the same ``digest`` as this entry. If the mimetype is ``application/json``, the value is usually empty or ``-``.

- ``archived_digest``: (`str`) The ``SHA1`` hash digest of the content, excluding the headers. It's usually a base-32-encoded string.

- ``archived_length``: (`int`) The compressed byte size of the corresponding WARC record, which includes WARC headers, HTTP headers, and content payload.

- ``resumption_key``: (`str`) Allows for a simple way to scroll through the results. Key to continue the query from the end of the previous query.
```

## File: `brain/knowledge/docs_legacy/handson.rst`
```
Hands-On Examples
====================

- **Tutorials**

   - `Wayback Tweets: Archive Tweets Retrieval <https://medium.com/@CyberRaya/wayback-tweets-archive-tweets-retrieval-582eb9be3334>`_ by CyberRaya, via Medium

   - Using Wayback Tweets to retrieve old tweets by Jey Zeta, in Spanish

      ..  youtube:: qy3wOnUxe6A
         :width: 100%


- **Notebook**

   This notebook demonstrates how to fetch, parse, and export archived tweets for a specific user using the ``waybacktweets`` library.

   .. image:: https://colab.research.google.com/assets/colab-badge.svg
      :target: https://colab.research.google.com/drive/1tnaM3rMWpoSHBZ4P_6iHFPjraWRQ3OGe?usp=sharing
      :alt: Open In Collab

```

## File: `brain/knowledge/docs_legacy/index.rst`
```
.. rst-class:: hide-header

Wayback Tweets
================

.. image:: ../assets/waybacktweets_title.png
    :alt: Wayback Tweets
    :align: center

Release: |release|

Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing (see :ref:`field_options`), and saves the data in HTML, for easy viewing of the tweets using the iframe tags, CSV, and JSON formats.

.. note::
    Intensive queries can lead to rate limiting, resulting in a temporary ban of a few minutes from web.archive.org.


User Guide
------------

.. toctree::
    :maxdepth: 2

    installation
    quickstart
    workflow
    field_options
    outputs
    exceptions
    handson
    contribute
    todo


Command-Line Interface
------------------------
.. toctree::
    :maxdepth: 2

    cli

API Reference
---------------

.. toctree::
    :maxdepth: 2

    api

Streamlit Web App
-------------------

.. toctree::
    :maxdepth: 2

    streamlit

Additional Information
-----------------------

.. toctree::
    :maxdepth: 1

.. raw:: html

    <ul>
        <li><a href="https://raw.githubusercontent.com/claromes/waybacktweets/refs/heads/main/LICENSE.md" target="_blank">GPL-3.0 license</a></li>
        <li><a href="https://github.com/claromes/waybacktweets/releases" target="_blank">Changes</a></li>
    </ul>

Indices and tables
----------------------

.. toctree::
    :maxdepth: 2

    genindex
    modindex
    search
```

## File: `brain/knowledge/docs_legacy/installation.rst`
```
Installation
================

**It is compatible with Python versions 3.10 and above.**

Using pipx
------------

    .. code-block:: shell

        pipx install waybacktweets

Using pip
------------

    .. code-block:: shell

        pip3 install waybacktweets

Using Poetry
------------

    .. code-block:: shell

        poetry add waybacktweets

.. _installation_from_source:

From source
-------------

    **Clone the repository:**

    .. code-block:: shell

        git clone git@github.com:claromes/waybacktweets.git

    **Change directory:**

    .. code-block:: shell

        cd waybacktweets

    **Install Poetry, if you haven't already:**

    .. code-block:: shell

        pip3 install poetry

    **Install the dependencies:**

    .. code-block:: shell

        poetry install

    **Install the pre-commit:**

    .. code-block:: shell

        poetry run pre-commit install

    **Run the CLI:**

    .. code-block:: shell

        poetry run waybacktweets [OPTIONS] USERNAME

    **Run the Streamlit App:**

    - Starts a new shell and activates the virtual environment:

        .. code-block:: shell

            poetry shell

    - Run the Streamlit:

        .. code-block:: shell

            streamlit run app/app.py

    **Build the docs:**

    .. code-block:: shell

        cd docs

    .. code-block:: shell

        make clean html
```

## File: `brain/knowledge/docs_legacy/make.bat`
```
@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=.
set BUILDDIR=_build

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
```

## File: `brain/knowledge/docs_legacy/outputs.rst`
```
Outputs
==========

It is possible to save the CDX data in three formats. In the command line tool, these three formats are saved automatically.

HTML
--------

This format allows for easy viewing of the archived tweets, through the use of the ``iframe`` tag. Each tweet contains four viewing options, which render when clicking on the accordion:

- ``archived_tweet_url``: (`str`) The archived URL.

- ``parsed_archived_tweet_url``: (`str`) The archived URL after parsing. It is not guaranteed that this option will be archived, it is just a facilitator, as the originally archived URL does not always exist, due to changes in URLs and web services of the social network Twitter. Check the :ref:`utils`.

- ``original_tweet_url``: (`str`) The original tweet URL.

- ``parsed_tweet_url``: (`str`) The original tweet URL after parsing. Old URLs were archived in a nested manner. The parsing applied here unnests these URLs when necessary. Refer to the :ref:`utils` for more details.

If you want to define which viewing options should be displayed in the HTML file, you need to use the package as a module and specify the desired view in the field options. See the :ref:`api` Reference and the :ref:`module` usage example.

Additionally, other fields are displayed.

.. note::

    The iframes (accordions) are best viewed in Firefox.

CSV
--------

Option to analyze the CDX data in comma-separated values.

JSON
--------

Option to analyze the data in JavaScript Object Notation.
```

## File: `brain/knowledge/docs_legacy/quickstart.rst`
```
Quickstart
================

CLI
-------------

Using Wayback Tweets as a standalone command line tool.

waybacktweets [OPTIONS] USERNAME

.. code-block:: shell

    waybacktweets --from 20150101 --to 20191231 --limit 250 jack

.. _module:

Module
-------------

Using Wayback Tweets as a Python Module. `Open in Colab <https://colab.research.google.com/drive/1tnaM3rMWpoSHBZ4P_6iHFPjraWRQ3OGe>`_.

.. code-block:: python

    from waybacktweets import WaybackTweets, TweetsParser, TweetsExporter

    USERNAME = "jack"

    api = WaybackTweets(USERNAME)
    archived_tweets = api.get()

    if archived_tweets:
        field_options = [
            "archived_urlkey",
            "archived_timestamp",
            "parsed_archived_timestamp",
            "archived_tweet_url",
            "parsed_archived_tweet_url",
            "original_tweet_url",
            "parsed_tweet_url",
            "available_tweet_text",
            "available_tweet_is_RT",
            "available_tweet_info",
            "archived_mimetype",
            "archived_statuscode",
            "archived_digest",
            "archived_length",
            "resumption_key",
        ]

        parser = TweetsParser(archived_tweets, USERNAME, field_options)
        parsed_tweets = parser.parse()

        exporter = TweetsExporter(parsed_tweets, USERNAME, field_options)
        exporter.save_to_csv()
        exporter.save_to_json()
        exporter.save_to_html()

Web App
-------------

Using Wayback Tweets as a Streamlit Web App.

`Open the application <https://waybacktweets.streamlit.app>`_, a prototype written in Python with the Streamlit framework and hosted on Streamlit Cloud.
```

## File: `brain/knowledge/docs_legacy/streamlit.rst`
```
Web App
=========

.. note::

   Starting from version 1.0, the web app will not receive all updates from the official package. To access all features, prefer the package via PyPI.

The application is a prototype hosted on Streamlit Cloud, serving as an alternative to the command line tool.

`Open the application <https://waybacktweets.streamlit.app>`_.


Filters
----------

- Filtering by date range: Using the ``from`` and ``to`` filters

- Limit: Query result limits.

- Only unique Wayback Machine URLs: Filtering by the collapse option using the ``urlkey`` field and the URL Match Scope ``prefix``


Username Query Parameter
--------------------------

An alternative way to access the application is by using the ``username`` query parameter. This allows for automatic configuration of the Username input and automatically searches. Additionally, when the ``username`` parameter is sent, the accordion with the filters will already be open.

Example URL format:

``https://waybacktweets.streamlit.app?username=<USERNAME>``


Community Comments
--------------------

.. raw:: html

   <ul>
        <li>"We're always delighted when we see our community members create tools for open source research." <a href="https://twitter.com/bellingcat/status/1728085974138122604" target="_blank">Bellingcat</a></li>
        <br>
        <li>"#myOSINTtip Clarissa Mendes launched a new tool for accessing old tweets via archive.org called the Wayback Tweets app. For those who love to look deeper at #osint tools, it is available on GitHub and uses the Wayback CDX Server API server (which is a hidden gem for accessing archive.org data!)" <a href="https://www.linkedin.com/posts/my-osint-training_myosinttip-osint-activity-7148425933324963841-0Q2n/" target="_blank">My OSINT Training</a></li>
        <br>
        <li>"Original way to find deleted tweets." <a href="https://twitter.com/henkvaness/status/1693298101765701676" target="_blank">Henk Van Ess</a></li>
        <br>
        <li>"This is an excellent tool to use now that most Twitter API-based tools have gone down with changes to the pricing structure over at X." <a href="https://osintnewsletter.com/p/22#%C2%A7osint-community" target="_blank">The OSINT Newsletter - Issue #22</a></li>
        <br>
        <li>"One of the keys to using the Wayback Machine effectively is knowing what it can and can't archive. It can, and has, archived many, many Twitter accounts... Utilize fun tools such as Wayback Tweets to do so more effectively." <a href="https://memeticwarfareweekly.substack.com/p/mww-paradise-by-the-telegram-dashboard" target="_blank">Ari Ben Am</a></li>
        <br>
        <li>"Want to see archived tweets on Wayback Machine in bulk? You can use Wayback Tweets." <a href="https://twitter.com/DailyOsint/status/1695065018662855102" target="_blank">Daily OSINT</a></li>
        <br>
        <li>"Untuk mempermudah penelusuran arsip, gunakan Wayback Tweets." <a href="https://twitter.com/gijnIndonesia/status/1685912219408805888" target="_blank">GIJN Indonesia</a></li>
        <br>
        <li>"A tool to quickly view tweets saved on archive.org." <a href="https://irinatechtips.substack.com/p/irina_tech_tips-newsletter-3-2023#%C2%A7wayback-tweets" target="_blank">Irina_Tech_Tips Newsletter #3</a></li>
        <br>
    </ul>

Legacy App
-------------

To access the legacy version of Wayback Tweets, `click here <https://waybacktweets-legacy.streamlit.app>`_. This version is no longer maintained.
```

## File: `brain/knowledge/docs_legacy/todo.rst`
```
TODO
================

.. |uncheck| raw:: html

    <input type="checkbox">

|uncheck| Unit Tests

|uncheck| JSON Parser: Create a separate function to handle JSON return, apply JsonParser (``waybacktweets/api/parse.py:110``), and avoid rate limiting

|uncheck| Download images when tweet URL has extensions like JPG or PNG

|uncheck| Implement logging system (remove print statements)

|uncheck| Mapping and parsing of other Twitter-related URLs

|uncheck| Download snapshots from https://archive.today
```

## File: `brain/knowledge/docs_legacy/workflow.rst`
```
.. _flowchart:

Workflow
================

The tool was written following a proposal not only to retrieve data from archived tweets, but also to facilitate the reading of these tweets. Therefore, a flow is defined to obtain these results in the best possible way.

Due to limitations of the Wayback CDX Server API, it is not always possible to parse the results with the mimetype ``application/json``, regardless, the data in CDX format are saved.

Use the mouse to zoom in and out the flowchart.

.. mermaid::
   :zoom:
   :align: center

   flowchart TB
      A[input Username]--> B[(Wayback Machine)]
      B--> B1[save Archived Tweets CDX data]
      B1--> |parsing| C{embed Tweet URL\nvia Twitter Publisher}
      C--> |2xx/3xx| D[return Tweet text]
      C--> |4xx| E[return None]
      E--> F{request Archived\nTweet URL}
      F--> |4xx| G[return Only CDX data]
      F--> |TODO: 2xx/3xx: application/json| J[return JSON text]
      F--> |2xx/3xx: text/html, warc/revisit, unk| K[return HTML iframe tag]
```

## File: `brain/knowledge/docs_legacy/_static/css/custom.css`
```css
body {
    font-family: Georgia, 'Times New Roman', Times, serif;
    background-color: whitesmoke;
}

a:hover {
    background-color: whitesmoke !important;
}

#cli #usage #waybacktweets h3,
#cli .admonition-title,
.sphinxsidebarwrapper li ul li ul:has(a[href="#waybacktweets"]):last-child {
    display: none;
}
```

## File: `brain/knowledge/docs_legacy/_templates/page.html`
```html
{% extends "!page.html" %}

{% block extrahead %}
{{ super() }}
    <meta name="description" content="Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data">

    <meta property="og:title" content="{{ title|e }}" />
    <meta property="og:description" content="Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data">
    <meta property="og:image" content="https://waybacktweets.claromes.com/_static/card.png" />

    <meta name="twitter:title" content="{{ title|e }}">
    <meta name="twitter:description" content="Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data">
    <meta property="twitter:image" content="https://waybacktweets.claromes.com/_static/card.png" />
{% endblock %}
```

## File: `legacy_app/legacy_app.py`
```python
import datetime
import re
from urllib.parse import unquote

import requests
import streamlit as st
import streamlit.components.v1 as components

year = datetime.datetime.now().year

st.set_page_config(
    page_title="Wayback Tweets",
    page_icon="🏛️",
    layout="centered",
    menu_items={
        "About": """
        This is the legacy application of [Wayback Tweets](https://waybacktweets.streamlit.app/).

        -------
        """,  # noqa: E501
    },
)

# https://discuss.streamlit.io/t/remove-hide-running-man-animation-on-top-of-page/21773/3
hide_streamlit_style = """
<style>
    header[data-testid="stHeader"] {
        opacity: 0.5;
    }
     iframe {
        border: 1px solid #dddddd;
        border-radius: 0.5rem;
    }
    div[data-testid="InputInstructions"] {
        visibility: hidden;
    }
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if "current_handle" not in st.session_state:
    st.session_state.current_handle = ""

if "prev_disabled" not in st.session_state:
    st.session_state.prev_disabled = False

if "next_disabled" not in st.session_state:
    st.session_state.next_disabled = False

if "next_button" not in st.session_state:
    st.session_state.next_button = False

if "prev_button" not in st.session_state:
    st.session_state.prev_button = False

if "update_component" not in st.session_state:
    st.session_state.update_component = 0

if "offset" not in st.session_state:
    st.session_state.offset = 0

if "saved_at" not in st.session_state:
    st.session_state.saved_at = (2006, year)

if "count" not in st.session_state:
    st.session_state.count = False


def scroll_into_view():
    js = f"""
    <script>
        window.parent.document.querySelector('section.main').scrollTo(0, 0);
        let update_component = {st.session_state.update_component} // Force component update to generate scroll
    </script>
    """  # noqa: E501

    components.html(js, width=0, height=0)


def clean_tweet(tweet):
    handle = st.session_state.current_handle.lower()
    tweet_lower = tweet.lower()

    pattern = re.compile(r"/status/(\d+)")
    match_lower_case = pattern.search(tweet_lower)
    match_original_case = pattern.search(tweet)

    if match_lower_case and handle in tweet_lower:
        return f"https://twitter.com/{st.session_state.current_handle}/status/{match_original_case.group(1)}"  # noqa: E501
    else:
        return tweet


def clean_link(link):
    handle = st.session_state.current_handle.lower()
    link = link.lower()

    pattern = re.compile(r"/status/(\d+)")
    match = pattern.search(link)

    if match and handle in link:
        return f"https://web.archive.org/web/{timestamp[i]}/https://twitter.com/{st.session_state.current_handle}/status/{match.group(1)}"  # noqa: E501
    else:
        return link


def pattern_tweet(tweet):
    # Reply: /status//
    # Link:  /status///
    # Twimg: /status/https://pbs

    pattern = re.compile(r'/status/"([^"]+)"')

    match = pattern.search(tweet)
    if match:
        return match.group(1).lstrip("/")
    else:
        return tweet


def pattern_tweet_id(tweet):
    # Delete sub-endpoint (/photos, /likes, /retweet...)
    pattern_username = re.compile(r"https://twitter\.com/([^/]+)/status/\d+")
    match_username = pattern_username.match(tweet)

    pattern_id = r"https://twitter.com/\w+/status/(\d+)"
    match_id = re.search(pattern_id, tweet)

    if match_id and match_username:
        tweet_id = match_id.group(1)
        username = match_username.group(1)
        return f"https://twitter.com/{username}/status/{tweet_id}"
    else:
        return tweet


def check_double_status(url_wb, url_tweet):
    if url_wb.count("/status/") == 2 and "twitter.com" not in url_tweet:
        return True

    return False


def embed(tweet):
    try:
        url = f"https://publish.twitter.com/oembed?url={clean_tweet(tweet)}"
        response = requests.get(url)

        regex = r'<blockquote class="twitter-tweet"(?: [^>]+)?><p[^>]*>(.*?)<\/p>.*?&mdash; (.*?)<\/a>'  # noqa: E501
        regex_author = r"^(.*?)\s*\("

        if response.status_code == 200 or response.status_code == 302:
            status_code = response.status_code
            html = response.json()["html"]
            author_name = response.json()["author_name"]

            matches_html = re.findall(regex, html, re.DOTALL)

            tweet_content = []
            user_info = []
            is_RT = []

            for match in matches_html:
                tweet_content_match = re.sub(r"<a[^>]*>|<\/a>", "", match[0].strip())
                tweet_content_match = tweet_content_match.replace("<br>", "\n")

                user_info_match = re.sub(r"<a[^>]*>|<\/a>", "", match[1].strip())
                user_info_match = user_info_match.replace(")", "), ")

                match_author = re.search(regex_author, user_info_match)
                author_tweet = match_author.group(1)

                if tweet_content_match:
                    tweet_content.append(tweet_content_match)
                if user_info_match:
                    user_info.append(user_info_match)

                    is_RT_match = False
                    if author_name != author_tweet:
                        is_RT_match = True

                    is_RT.append(is_RT_match)

            return status_code, tweet_content, user_info, is_RT
        else:
            return False
    except requests.exceptions.Timeout:
        st.error("Connection to web.archive.org timed out.")
    except requests.exceptions.ConnectionError:
        st.error("Failed to establish a new connection with web.archive.org.")
    except UnboundLocalError:
        st.empty()


@st.cache_data(ttl=1800, show_spinner=False)
def tweets_count(handle, saved_at):
    url = f"https://web.archive.org/cdx/search/cdx?url=https://twitter.com/{handle}/status/*&collapse=timestamp:8&output=json&from={saved_at[0]}&to={saved_at[1]}"  # noqa: E501
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 1:
                total_tweets = len(data) - 1
                return total_tweets
            else:
                return 0
    except requests.exceptions.Timeout:
        st.error("Connection to web.archive.org timed out.")
        st.stop()
    except requests.exceptions.ConnectionError:
        st.error("Failed to establish a new connection with web.archive.org.")
    except UnboundLocalError:
        st.empty()


@st.cache_data(ttl=1800, show_spinner=False)
def query_api(handle, limit, offset, saved_at):
    if not handle:
        st.warning("username, please!")
        st.stop()

    url = f"https://web.archive.org/cdx/search/cdx?url=https://twitter.com/{handle}/status/*&collapse=timestamp:8&output=json&limit={limit}&offset={offset}&from={saved_at[0]}&to={saved_at[1]}"  # noqa: E501
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200 or response.status_code == 304:
            return response.json()
    except requests.exceptions.Timeout:
        st.error("Connection to web.archive.org timed out.")
    except requests.exceptions.ConnectionError:
        st.error("Failed to establish a new connection with web.archive.org.")
    except UnboundLocalError:
        st.empty()
    except requests.exceptions.HTTPError:
        st.error(
            """
        **Temporarily Offline**

        Internet Archive services are temporarily offline. Please check Internet Archive [Twitter feed](https://twitter.com/internetarchive/) for the latest information.
        """  # noqa: E501
        )
        st.stop()


@st.cache_data(ttl=1800, show_spinner=False)
def parse_links(links):
    parsed_links = []
    timestamp = []
    tweet_links = []
    parsed_mimetype = []

    for link in links[1:]:
        tweet_remove_char = unquote(link[2]).replace("’", "")
        cleaned_tweet = pattern_tweet(tweet_remove_char).strip('"')

        url = f"https://web.archive.org/web/{link[1]}/{tweet_remove_char}"

        parsed_links.append(url)
        timestamp.append(link[1])
        tweet_links.append(cleaned_tweet)
        parsed_mimetype.append(link[3])

    return parsed_links, tweet_links, parsed_mimetype, timestamp


def attr(i):
    original_tweet = pattern_tweet_id(clean_tweet(tweet_links[i]))

    if status:
        original_tweet = pattern_tweet_id(f"https://twitter.com/{tweet_links[i]}")
    elif "://" not in tweet_links[i]:
        original_tweet = pattern_tweet_id(f"https://{tweet_links[i]}")

    st.markdown(
        f'{i+1 + st.session_state.offset}. [**archived url**]({link}) · [**original url**]({original_tweet}) · **MIME Type:** {mimetype[i]} · **Saved at:** {datetime.datetime.strptime(timestamp[i], "%Y%m%d%H%M%S")}'  # noqa: E501
    )


def display_tweet():
    if (
        mimetype[i] == "application/json"
        or mimetype[i] == "text/html"
        or mimetype[i] == "unk"
        or mimetype[i] == "warc/revisit"
    ):
        if is_RT[0] is True:
            st.info("*Retweet*")
        st.write(tweet_content[0])
        st.write(f"**{user_info[0]}**")

        st.divider()
    else:
        st.warning("MIME Type was not parsed.")

        st.divider()


def display_not_tweet():
    original_link = pattern_tweet_id(clean_tweet(tweet_links[i]))

    if status:
        original_link = pattern_tweet_id(f"https://twitter.com/{tweet_links[i]}")
    elif "://" not in tweet_links[i]:
        original_link = pattern_tweet_id(f"https://{tweet_links[i]}")

    response_html = requests.get(original_link)

    if (
        mimetype[i] == "text/html"
        or mimetype[i] == "warc/revisit"
        or mimetype[i] == "unk"
    ):
        if (
            ".jpg" in tweet_links[i] or ".png" in tweet_links[i]
        ) and response_html.status_code == 200:
            components.iframe(tweet_links[i], height=500, scrolling=True)
        elif "/status/" not in original_link:
            st.info("This isn't a status or is not available")
        elif status or f"{st.session_state.current_handle}" not in original_link:
            st.info(f"Replying to {st.session_state.current_handle}")
        else:
            components.iframe(clean_link(link), height=500, scrolling=True)

        st.divider()
    elif mimetype[i] == "application/json":
        try:
            response_json = requests.get(link)

            if response_json.status_code == 200:
                json_data = response_json.json()

                if "data" in json_data:
                    if "text" in json_data["data"]:
                        json_text = json_data["data"]["text"]
                    else:
                        json_text = json_data["data"]
                else:
                    if "text" in json_data:
                        json_text = json_data["text"]
                    else:
                        json_text = json_data

                st.code(json_text)
                st.json(json_data, expanded=False)

                st.divider()
            else:
                st.error(response_json.status_code)

                st.divider()
        except requests.exceptions.Timeout:
            st.error("Connection to web.archive.org timed out.")
            st.divider()
        except requests.exceptions.ConnectionError:
            st.error("Failed to establish a new connection with web.archive.org.")
            st.divider()
        except UnboundLocalError:
            st.empty()
    else:
        st.warning("MIME Type was not parsed.")
        st.divider()


def prev_page():
    st.session_state.offset -= tweets_per_page

    # scroll to top config
    st.session_state.update_component += 1
    scroll_into_view()


def next_page():
    st.session_state.offset += tweets_per_page

    # scroll to top config
    st.session_state.update_component += 1
    scroll_into_view()


# UI
st.title(
    "Wayback Tweets",  # noqa: E501
    anchor=False,
    help="v0.4.3",
)
st.write(
    "Display multiple archived tweets on Wayback Machine and avoid opening each link manually"  # noqa: E501
)

handle = st.text_input("Username", placeholder="jack")

st.session_state.saved_at = st.slider("Tweets saved between", 2006, year, (2006, year))

not_available = st.checkbox(
    "Original URLs not available",
    help="Due to changes in X, it is possible to find available tweets if you are logged into X",  # noqa: E501
)

query = st.button("Query", type="primary", use_container_width=True)

if handle != st.session_state.current_handle:
    st.session_state.current_handle = handle
    st.session_state.offset = 0

if query or st.session_state.count:
    tweets_per_page = 25

    st.session_state.count = tweets_count(handle, st.session_state.saved_at)

    st.caption(
        "The search optimization uses an 8-digit [collapsing strategy](https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md?ref=hackernoon.com#collapsing), refining the captures to one per day. The number of tweets per page is set to 25, and this is a fixed value due to the API rate limit."  # noqa: E501
    )
    st.write(f"**{st.session_state.count} URLs have been captured**")

    if st.session_state.count:
        if tweets_per_page > st.session_state.count:
            tweets_per_page = st.session_state.count

    try:
        progress = st.empty()
        links = query_api(
            handle, tweets_per_page, st.session_state.offset, st.session_state.saved_at
        )

        parse = parse_links(links)
        parsed_links = parse[0]
        tweet_links = parse[1]
        mimetype = parse[2]
        timestamp = parse[3]

        if links:
            st.divider()

            st.session_state.current_handle = handle

            return_none_count = 0

            start_index = st.session_state.offset
            end_index = min(st.session_state.count, start_index + tweets_per_page)

            with st.spinner("Fetching..."):
                for i in range(tweets_per_page):
                    try:
                        if tweet_links[i]:
                            link = parsed_links[i]
                            tweet = embed(tweet_links[i])

                            status = check_double_status(link, tweet_links[i])

                            if not not_available:
                                attr(i)

                                if tweet:
                                    status_code = tweet[0]
                                    tweet_content = tweet[1]
                                    user_info = tweet[2]
                                    is_RT = tweet[3]

                                    display_tweet()
                                elif not tweet:
                                    display_not_tweet()

                            if not_available:
                                if not tweet:
                                    return_none_count += 1
                                    attr(i)

                                    display_not_tweet()

                                progress.write(
                                    f"{return_none_count} URLs have been captured in the range {start_index}-{end_index}"  # noqa: E501
                                )

                            if start_index <= 0:
                                st.session_state.prev_disabled = True
                            else:
                                st.session_state.prev_disabled = False

                            if i + 1 == st.session_state.count:
                                st.session_state.next_disabled = True
                            else:
                                st.session_state.next_disabled = False
                    except IndexError:
                        if start_index <= 0:
                            st.session_state.prev_disabled = True
                        else:
                            st.session_state.prev_disabled = False

                        st.session_state.next_disabled = True

            prev, _, next = st.columns([3, 4, 3])

            prev.button(
                "Previous",
                disabled=st.session_state.prev_disabled,
                key="prev_button_key",
                on_click=prev_page,
                type="primary",
                use_container_width=True,
            )
            next.button(
                "Next",
                disabled=st.session_state.next_disabled,
                key="next_button_key",
                on_click=next_page,
                type="primary",
                use_container_width=True,
            )

        if not links:
            st.error("Unable to query the Wayback Machine API.")
    except TypeError as e:
        st.error(
            f"""
        {e}. Refresh this page and try again.
        """  # noqa: E501
        )
        st.session_state.offset = 0
```

## File: `legacy_app/requirements.txt`
```
requests==2.30.0
streamlit==1.27.0
```

## File: `waybacktweets/__init__.py`
```python
# flake8: noqa: F401

from waybacktweets.api.export import TweetsExporter
from waybacktweets.api.parse import JsonParser, TweetsParser, TwitterEmbed
from waybacktweets.api.request import WaybackTweets
from waybacktweets.api.visualize import HTMLTweetsVisualizer
```

## File: `waybacktweets/_cli.py`
```python
# flake8: noqa: E501
"""
CLI functions for retrieving archived tweets.
"""

from datetime import datetime
from importlib.metadata import version
from typing import Any, Optional

import click
from rich import print as rprint

from waybacktweets.api.export import TweetsExporter
from waybacktweets.api.parse import TweetsParser
from waybacktweets.api.request import WaybackTweets
from waybacktweets.config.config import config

PACKAGE_NAME = "waybacktweets"


class CustomCommand(click.Command):
    """
    Custom Click command that overrides the default help message.
    """

    def format_help(
        self, ctx: click.Context, formatter: click.HelpFormatter
    ) -> None:  # noqa: E501
        """
        Customize the help message shown when the command is invoked with --help.

        Args:
            ctx (click.Context): The Click context for the command.
            formatter (click.HelpFormatter): The formatter used to generate the help text.
        """  # noqa: E501
        formatter.write_heading("Usage")
        formatter.write_text(f"  {PACKAGE_NAME} [OPTIONS] USERNAME")
        formatter.write_text("  USERNAME: The Twitter username without @")

        self.format_options(ctx, formatter)
        formatter.write("\n")

        formatter.write_heading("Examples")
        formatter.write_text("  waybacktweets jack")
        formatter.write_text(
            "  waybacktweets --from 20200305 --to 20231231 --limit 300 --verbose jack"
        )
        formatter.write("\n")

        formatter.write_heading("Repository")
        formatter.write_text("  https://github.com/claromes/waybacktweets")
        formatter.write("\n")

        formatter.write_heading("Documentation")
        formatter.write_text("  https://waybacktweets.claromes.com")


def _parse_date(
    ctx: Optional[Any] = None, param: Optional[Any] = None, value: Optional[str] = None
) -> Optional[str]:
    """
    Parses a date string and returns it in the format "YYYYMMDD".

    Args:
        ctx: Necessary when used with the click package. Defaults to None.
        param: Necessary when used with the click package. Defaults to None.
        value: A date string in the "YYYYMMDD" format. Defaults to None.

    Returns:
        The input date string formatted in the "YYYYMMDD" format, or None if no date string was provided.
    """
    try:
        if value is None:
            return None

        date = datetime.strptime(value, "%Y%m%d")

        return date.strftime("%Y%m%d")
    except ValueError:
        raise click.BadParameter("Date must be in format YYYYmmdd")


@click.command(
    cls=CustomCommand, context_settings={"help_option_names": ["-h", "--help"]}, help=""
)
@click.argument("username", type=str)
@click.option(
    "-c",
    "--collapse",
    type=click.Choice(["urlkey", "digest", "timestamp:XX"], case_sensitive=False),
    default=None,
    help="Collapse results based on a field, or a substring of a field. XX in the timestamp value ranges from 1 to 14, comparing the first XX digits of the timestamp field. It is recommended to use from 4 onwards, to compare at least by years.",  # noqa: E501
)
@click.option(
    "-f",
    "--from",
    "timestamp_from",
    type=click.UNPROCESSED,
    metavar="DATE",
    callback=_parse_date,
    default=None,
    help="Filtering by date range from this date. Format: YYYYmmdd",
)
@click.option(
    "-t",
    "--to",
    "timestamp_to",
    type=click.UNPROCESSED,
    metavar="DATE",
    callback=_parse_date,
    default=None,
    help="Filtering by date range up to this date. Format: YYYYmmdd",
)
@click.option(
    "-l",
    "--limit",
    type=int,
    metavar="INTEGER",
    default=None,
    help="Query result limits.",
)
@click.option(
    "-rk",
    "--resumption_key",
    type=str,
    default=None,
    help="Allows for a simple way to scroll through the results. Key to continue the query from the end of the previous query.",  # noqa: E501
)
@click.option(
    "-mt",
    "--matchtype",
    type=click.Choice(["exact", "prefix", "host", "domain"], case_sensitive=False),
    default=None,
    help="Results matching a certain prefix, a certain host or all subdomains.",  # noqa: E501
)
@click.option(
    "-v",
    "--verbose",
    "verbose",
    is_flag=True,
    default=False,
    help="Shows the log.",
)
@click.version_option(version=version(PACKAGE_NAME), prog_name=PACKAGE_NAME)
def main(
    username: str,
    collapse: Optional[str],
    timestamp_from: Optional[str],
    timestamp_to: Optional[str],
    limit: Optional[int],
    resumption_key: Optional[str],
    matchtype: Optional[str],
    verbose: Optional[bool],
) -> None:
    """
    Handles CLI queries for archived tweets with filtering and pagination.

    Args:
        username (str): Twitter username to search (without the @ symbol).
        collapse (Optional[str]): Collapse results based on a specific field or a substring
            of a field. Possible values include 'urlkey', 'digest', or 'timestamp:XX', where
            XX is the number of digits to match in timestamps (recommended: 4 or more).
        timestamp_from (Optional[str]): Start date for filtering results (format: YYYYMMDD).
        timestamp_to (Optional[str]): End date for filtering results (format: YYYYMMDD).
        limit (Optional[int]): Maximum number of results to return.
        resumption_key (Optional[str]): Resume a previous query using this key (for pagination).
        matchtype (Optional[str]): Filter by URL match type: 'exact', 'prefix', 'host', or 'domain'.
        verbose (Optional[bool]): Print verbose logs during execution.
    """  # noqa: E501
    try:
        config.verbose = verbose

        api = WaybackTweets(
            username,
            collapse,
            timestamp_from,
            timestamp_to,
            limit,
            resumption_key,
            matchtype,
        )

        print("Retrieving...")
        archived_tweets = api.get()

        if archived_tweets:
            field_options = [
                "archived_urlkey",
                "archived_timestamp",
                "parsed_archived_timestamp",
                "archived_tweet_url",
                "parsed_archived_tweet_url",
                "original_tweet_url",
                "parsed_tweet_url",
                "available_tweet_text",
                "available_tweet_is_RT",
                "available_tweet_info",
                "archived_mimetype",
                "archived_statuscode",
                "archived_digest",
                "archived_length",
                "resumption_key",
            ]

            parser = TweetsParser(archived_tweets, username, field_options)
            parsed_tweets = parser.parse(print_progress=True)

            exporter = TweetsExporter(parsed_tweets, username, field_options)

            exporter.save_to_csv()
            exporter.save_to_json()
            exporter.save_to_html()
    except Exception as e:
        rprint(f"[red]{e}")
```

## File: `waybacktweets/api/export.py`
```python
"""
Exports the parsed archived tweets.
"""

import datetime
import re
from typing import Any, Dict, List, Optional

import pandas as pd

from waybacktweets.api.visualize import HTMLTweetsVisualizer


class TweetsExporter:
    """
    Class responsible for exporting parsed archived tweets.

    Args:
        data (Dict[str, List[Any]]): The parsed archived tweets data.
        username (str): The username associated with the tweets.
        field_options (List[str]): The fields to be included in the exported data. For more details on each option, visit :ref:`field_options`.
    """  # noqa: E501

    def __init__(
        self, data: Dict[str, List[Any]], username: str, field_options: List[str]
    ):
        self.data = data
        self.username = username
        self.field_options = field_options
        self.formatted_datetime = self._datetime_now()
        self.filename = f"{self.username}_tweets_{self.formatted_datetime}"
        self.dataframe = self._create_dataframe()

    @staticmethod
    def _datetime_now() -> str:
        """
        Returns the current datetime, formatted as a string.

        Returns:
            The current datetime.
        """
        now = datetime.datetime.now()
        formatted_now = now.strftime("%Y%m%d%H%M%S")
        formatted_now = re.sub(r"\W+", "", formatted_now)

        return formatted_now

    @staticmethod
    def _transpose_matrix(
        data: Dict[str, List[Any]], fill_value: Optional[Any] = None
    ) -> List[List[Any]]:
        """
        Transposes a matrix, filling in missing values with a specified fill value if needed.

        Args:
            data (Dict[str, List[Any]]): The matrix to be transposed.
            fill_value (Optional[Any]): The value to fill in missing values with.

        Returns:
            The transposed matrix.
        """  # noqa: E501
        max_length = max(len(sublist) for sublist in data.values())

        filled_data = {
            key: value + [fill_value] * (max_length - len(value))
            for key, value in data.items()
        }

        data_transposed = [list(row) for row in zip(*filled_data.values())]

        return data_transposed

    def _create_dataframe(self) -> pd.DataFrame:
        """
        Creates a DataFrame from the transposed data.

        Returns:
            The DataFrame representation of the data.
        """
        data_transposed = self._transpose_matrix(self.data)

        df = pd.DataFrame(data_transposed, columns=self.field_options)

        return df

    def save_to_csv(self) -> None:
        """
        Saves the DataFrame to a CSV file.
        """
        csv_file_path = f"{self.filename}.csv"
        self.dataframe.to_csv(csv_file_path, index=False)

        print(f"Saved to {csv_file_path}")

    def generate_json(self) -> str:
        """
        Generates JSON data from the DataFrame (without saving to a file).

        Returns:
            The JSON-formatted string of the DataFrame.
        """

        json_data = self.dataframe.to_json(orient="records", lines=False)
        return json_data

    def save_to_json(self) -> None:
        """
        Saves the DataFrame to a JSON file.
        """
        json_path = f"{self.filename}.json"
        self.dataframe.to_json(json_path, orient="records", lines=False)

        print(f"Saved to {json_path}")

    def save_to_html(self) -> None:
        """
        Saves the DataFrame to an HTML file.
        """
        json_data = self.generate_json()

        html_file_path = f"{self.filename}.html"

        html = HTMLTweetsVisualizer(self.username, json_data, html_file_path)

        html_content = html.generate()
        html.save(html_content)

        print(f"Saved to {html_file_path}")
```

## File: `waybacktweets/api/parse.py`
```python
"""
Parses the returned data from the Wayback CDX Server API.
"""

import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import nullcontext
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import unquote

from rich import print as rprint
from rich.progress import Progress

from waybacktweets.config.config import config
from waybacktweets.config.field_options import FIELD_OPTIONS
from waybacktweets.exceptions.exceptions import (
    ConnectionError,
    GetResponseError,
    HTTPError,
)
from waybacktweets.utils.utils import (
    check_double_status,
    check_pattern_tweet,
    check_url_scheme,
    clean_tweet_url,
    delete_tweet_pathnames,
    get_response,
    is_tweet_url,
    semicolon_parser,
    timestamp_parser,
)


class TwitterEmbed:
    """
    This class is responsible for parsing tweets using the Twitter Publish service.

    Args:
        tweet_url (str): The URL of the tweet to be parsed.
    """

    def __init__(self, tweet_url: str):
        self.tweet_url = tweet_url

    def embed(self) -> Optional[Tuple[List[str], List[bool], List[str]]]:
        """
        Parses the archived tweets when they are still available.

        This function goes through each archived tweet and checks if it is still available. If the tweet is available, it extracts the necessary information and adds it to the respective lists. The function returns a tuple of three lists:

        - The first list contains the tweet texts.
        - The second list contains boolean values indicating whether each tweet is still available.
        - The third list contains the URLs of the tweets.

        Returns:
            A tuple of three lists containing the tweet texts, availability statuses, and URLs, respectively. If no tweets are available, returns None.
        """  # noqa: E501
        try:
            url = f"https://publish.twitter.com/oembed?url={self.tweet_url}"
            response = get_response(url=url)
            if response:
                json_response = response.json()
                html = json_response["html"]
                author_name = json_response["author_name"]

                regex = re.compile(
                    r'<blockquote class="twitter-tweet"(?: [^>]+)?><p[^>]*>(.*?)<\/p>.*?&mdash; (.*?)<\/a>',  # noqa
                    re.DOTALL,
                )
                regex_author = re.compile(r"^(.*?)\s*\(")

                matches_html = regex.findall(html)

                tweet_content = []
                user_info = []
                is_RT = []

                for match in matches_html:
                    tweet_content_match = re.sub(
                        r"<a[^>]*>|<\/a>", "", match[0].strip()
                    ).replace("<br>", "\n")
                    user_info_match = re.sub(
                        r"<a[^>]*>|<\/a>", "", match[1].strip()
                    ).replace(")", "), ")
                    match_author = regex_author.search(user_info_match)
                    author_tweet = match_author.group(1) if match_author else ""

                    if tweet_content_match:
                        tweet_content.append(tweet_content_match)
                    if user_info_match:
                        user_info.append(user_info_match)
                        is_RT.append(author_name != author_tweet)

                return tweet_content, is_RT, user_info
        except ConnectionError:
            if config.verbose:
                rprint("[yellow]Error parsing the tweet, but the CDX data was saved.")
        except HTTPError:
            if config.verbose:
                rprint(
                    f"[yellow]{self.tweet_url} not available on the user's Twitter account, but the CDX data was saved."  # noqa: E501
                )
        except GetResponseError as e:
            if config.verbose:
                rprint(f"[red]An error occurred: {str(e)}")

        return None


class JsonParser:
    """
    This class is responsible for parsing tweets when the mimetype is application/json.

    Note: This class is in an experimental phase.

    Args:
        archived_tweet_url (str): The URL of the archived tweet to be parsed.
    """  # noqa: E501

    def __init__(self, archived_tweet_url: str):
        self.archived_tweet_url = archived_tweet_url

    def parse(self) -> str:
        """
        Parses the archived tweets in JSON format.

        Returns:
            The parsed tweet text.
        """
        try:
            response = get_response(url=self.archived_tweet_url)

            if response:
                json_data = response.json()

                if "data" in json_data:
                    return json_data["data"].get("text", json_data["data"])

                if "retweeted_status" in json_data:
                    return json_data["retweeted_status"].get(
                        "text", json_data["retweeted_status"]
                    )

                return json_data.get("text", json_data)
        except ConnectionError:
            if config.verbose:
                rprint(
                    f"[yellow]Connection error with {self.archived_tweet_url}. Max retries exceeded. Error parsing the JSON, but the CDX data was saved."  # noqa: E501
                )
        except GetResponseError as e:
            if config.verbose:
                rprint(f"[red]An error occurred: {str(e)}")

        return None


class TweetsParser:
    """
    This class is responsible for the overall parsing of archived tweets.

    Args:
        archived_tweets_response (List[str]): The response from the archived tweets.
        username (str): The username associated with the tweets.
        field_options (List[str]): The fields to be included in the parsed data. For more details on each option, visit :ref:`field_options`.
    """  # noqa: E501

    def __init__(
        self,
        archived_tweets_response: List[str],
        username: str,
        field_options: List[str],
    ):
        if not all(option in FIELD_OPTIONS for option in field_options):
            raise ValueError("Some field options are not valid.")

        self.archived_tweets_response = archived_tweets_response[0]
        self.username = username
        self.field_options = field_options
        self.parsed_tweets = {option: [] for option in self.field_options}
        self.show_resume_key = archived_tweets_response[1]["show_resume_key"]

        self._add_resumption_key()

    def _add_resumption_key(self):
        """Adds the resumption key from the last archived tweet response to the parsed tweets.

        This method extracts the resumption key from the last item in the archived tweets response list
        and appends it to the 'resumption_key' field in the parsed tweets dictionary. It also prints
        the resumption key with instructions on how to use it with the 'limit' option for continuing
        the query from the end of the previous query.

        Raises:
            ValueError: If the list of archived tweet responses is empty.

        """  # noqa: E501
        if not self.archived_tweets_response:
            raise ValueError("The list of archived tweet responses is empty.")

        resumption_key = (
            self.archived_tweets_response[-1][0] if self.show_resume_key else None
        )
        if self.show_resume_key and "resumption_key" in self.parsed_tweets:
            self.parsed_tweets["resumption_key"] = []
            self.parsed_tweets["resumption_key"].append(resumption_key)

    def _add_field(self, key: str, value: Any) -> None:
        """
        Appends a value to a list in the parsed data structure.

        Args:
            key (str): The key in the parsed data structure.
            value (Any): The value to be appended.
        """
        if key in self.parsed_tweets:
            self.parsed_tweets[key].append(value)

    def _process_response(self, response: List[str]) -> None:
        """
        Processes the archived tweet's response and adds the relevant CDX data.

        Args:
            response (List[str]): The response from the archived tweet.
        """
        tweet_remove_char = unquote(response[2]).replace("’", "")
        cleaned_tweet = check_pattern_tweet(tweet_remove_char).strip('"')

        wayback_machine_url = (
            f"https://web.archive.org/web/{response[1]}/{tweet_remove_char}"
        )
        original_tweet = delete_tweet_pathnames(
            clean_tweet_url(cleaned_tweet, self.username)
        )

        double_status = check_double_status(wayback_machine_url, original_tweet)

        if double_status:
            original_tweet = delete_tweet_pathnames(
                f"https://twitter.com{original_tweet}"
            )
        elif "://" not in original_tweet:
            original_tweet = delete_tweet_pathnames(f"https://{original_tweet}")

        parsed_wayback_machine_url = (
            f"https://web.archive.org/web/{response[1]}/{original_tweet}"
        )

        encoded_archived_tweet = check_url_scheme(semicolon_parser(wayback_machine_url))
        encoded_parsed_archived_tweet = check_url_scheme(
            semicolon_parser(parsed_wayback_machine_url)
        )
        encoded_tweet = check_url_scheme(semicolon_parser(response[2]))
        encoded_parsed_tweet = check_url_scheme(semicolon_parser(original_tweet))

        available_tweet_text = None
        available_tweet_is_RT = None
        available_tweet_info = None

        is_tweet = is_tweet_url(encoded_tweet)

        if is_tweet:
            embed_parser = TwitterEmbed(encoded_tweet)
            content = embed_parser.embed()

            if content:
                available_tweet_text = semicolon_parser(content[0][0])
                available_tweet_is_RT = content[1][0]
                available_tweet_info = semicolon_parser(content[2][0])

        self._add_field("available_tweet_text", available_tweet_text)
        self._add_field("available_tweet_is_RT", available_tweet_is_RT)
        self._add_field("available_tweet_info", available_tweet_info)

        self._add_field("archived_urlkey", response[0])
        self._add_field("archived_timestamp", response[1])
        self._add_field("parsed_archived_timestamp", timestamp_parser(response[1]))
        self._add_field("archived_tweet_url", encoded_archived_tweet)
        self._add_field("parsed_archived_tweet_url", encoded_parsed_archived_tweet)
        self._add_field("original_tweet_url", encoded_tweet)
        self._add_field("parsed_tweet_url", encoded_parsed_tweet)
        self._add_field("archived_mimetype", response[3])
        self._add_field("archived_statuscode", response[4])
        self._add_field("archived_digest", response[5])
        self._add_field("archived_length", response[6])

    def parse(self, print_progress=False) -> Dict[str, List[Any]]:
        """
        Parses the archived tweets CDX data and structures it.

        Args:
            print_progress (bool): A boolean indicating whether to print progress or not.

        Returns:
            The parsed tweets data.
        """  # noqa: E501
        with ThreadPoolExecutor(max_workers=10) as executor:

            futures = {
                executor.submit(self._process_response, response): response
                for response in self.archived_tweets_response[1:]
            }

            progress_context = Progress() if print_progress else nullcontext()
            with progress_context as progress:
                task = None
                if print_progress:
                    task = progress.add_task(
                        f"Parsing the archived tweets of @{self.username}\n",
                        total=len(futures),
                    )

                for future in as_completed(futures):
                    try:
                        future.result()
                    except IndexError:
                        pass
                    except Exception as e:
                        rprint(f"[red]{e}")

                    if print_progress:
                        progress.update(task, advance=1)

            if self.show_resume_key:
                rprint(
                    f'[blue]Resumption Key: [bold]{self.archived_tweets_response[-1][0]}[/bold][/blue]\nUse this Resumption Key option (--resumption_key in the CLI or "resumption_key" in the Module) to continue the query from where the previous one left off. This allows you to split a large query into smaller, more efficient ones.\n'  # noqa: E501
                )

            return self.parsed_tweets
```

## File: `waybacktweets/api/request.py`
```python
"""
Requests data from the Wayback Machine API.
"""

from typing import Any, Dict, Optional

from rich import print as rprint

from waybacktweets.config.config import config
from waybacktweets.exceptions.exceptions import (
    ConnectionError,
    EmptyResponseError,
    GetResponseError,
    HTTPError,
    ReadTimeoutError,
)
from waybacktweets.utils.utils import get_response


class WaybackTweets:
    """
    Class responsible for requesting data from the Wayback CDX Server API.

    Args:
        username (str): The username associated with the tweets.
        collapse (str, optional): The field to collapse duplicate lines on.
        timestamp_from (str, optional): The timestamp to start retrieving tweets from.
        timestamp_to (str, optional): The timestamp to stop retrieving tweets at.
        limit (int, optional): The maximum number of results to return.
        resumption_key (int, optional): Key to continue the query from the end of the previous query.
        matchtype (str, optional): Results matching a certain prefix, a certain host or all subdomains.
    """  # noqa: E501

    def __init__(
        self,
        username: str,
        collapse: str = None,
        timestamp_from: str = None,
        timestamp_to: str = None,
        limit: int = None,
        resumption_key: str = None,
        matchtype: str = None,
    ):
        self.username = username
        self.collapse = collapse
        self.timestamp_from = timestamp_from
        self.timestamp_to = timestamp_to
        self.limit = limit
        self.resumption_key = resumption_key
        self.matchtype = matchtype

    def get(self) -> Optional[Dict[str, Any]]:
        """
        Sends a GET request to the Internet Archive's CDX API to retrieve archived tweets.

        Returns:
            The response from the CDX API in JSON format, if successful. Otherwise, None.
        """  # noqa: E501
        url = "https://web.archive.org/cdx/search/cdx"

        wildcard_pathname = "" if self.matchtype else "/*"

        show_resume_key = bool(self.limit)

        params = {
            "url": f"https://twitter.com/{self.username}/status{wildcard_pathname}",
            "showResumeKey": show_resume_key,
            "output": "json",
        }

        if self.collapse:
            params["collapse"] = self.collapse

        if self.timestamp_from:
            params["from"] = self.timestamp_from

        if self.timestamp_to:
            params["to"] = self.timestamp_to

        if self.limit:
            params["limit"] = self.limit

        if self.resumption_key:
            params["resumption_key"] = self.resumption_key

        if self.matchtype:
            params["matchType"] = self.matchtype

        try:
            response = get_response(url=url, params=params)
            return response.json(), {"show_resume_key": show_resume_key}
        except ReadTimeoutError:
            if config.verbose:
                rprint("[red]Connection to web.archive.org timed out.")
        except ConnectionError:
            if config.verbose:
                rprint(
                    "[red]Failed to establish a new connection with web.archive.org. Max retries exceeded. Please wait a few minutes and try again."  # noqa: E501
                )
        except HTTPError as e:
            if config.verbose:
                rprint(f"[red]HTTP error occurred: {str(e)}")
        except EmptyResponseError:
            if config.verbose:
                rprint("[red]No data was saved due to an empty response.")
        except GetResponseError as e:
            if config.verbose:
                rprint(f"[red]An error occurred: {str(e)}")

        return None
```

## File: `waybacktweets/api/visualize.py`
```python
# flake8: noqa: E501
"""
Generates an HTML file to visualize the parsed data.
"""

import json
import os
from typing import Any, Dict, List, Union

from waybacktweets.utils import timestamp_parser


class HTMLTweetsVisualizer:
    """
    Class responsible for generating an HTML file to visualize the parsed data.

    Args:
        username (str): The username associated with the tweets.
        json_path (Union[str, List[str]]): The path of the JSON file or the JSON data itself.
        html_file_path (str, optional): The path where the HTML file will be saved.
    """

    def __init__(
        self,
        username: str,
        json_path: Union[str, List[str]],
        html_file_path: str = None,
    ):
        self.username = username
        self.json_path = self._json_loader(json_path)
        self.html_file_path = html_file_path

    @staticmethod
    def _json_loader(json_path: Union[str, List[str]]) -> List[Dict[str, Any]]:
        """
        Reads and loads JSON data from a specified file path or JSON string.

        Args:
            json_path (Union[str, List[str]]): The path of the JSON file or the JSON data itself.

        Returns:
            The content of the JSON file or data.
        """
        if os.path.isfile(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)

        return json.loads(json_path)

    def generate(self) -> str:
        """
        Generates an HTML string that represents the parsed data.

        Returns:
            The generated HTML string.
        """
        tweets_per_page = 24
        total_pages = (len(self.json_path) + tweets_per_page - 1) // tweets_per_page

        html = "<!DOCTYPE html>\n"
        html += '<html lang="en">\n'
        html += "<!-- This document was generated by Wayback Tweets. Visit: https://waybacktweets.claromes.com/ -->\n"

        html += "<head>"
        html += '<meta charset="UTF-8">\n'
        html += (
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        )
        html += f"<title>Archived tweets of @{self.username}</title>\n"

        # Adds styling
        html += "<style>\n"
        html += "body { font-family: monospace; background-color: whitesmoke; color: #1c1e21; margin: 0; padding: 20px; }\n"
        html += ".container { display: flex; flex-wrap: wrap; gap: 20px; }\n"
        html += ".tweet { flex: 0 1 calc(33.33% - 20px); background-color: #ffffff; border: 1px solid #e2e2e2; border-radius: 10px; padding: 15px; overflow-wrap: break-word; margin: auto; width: 600px; }\n"
        html += ".tweet strong { font-weight: bold; }\n"
        html += ".tweet a { color: #000000; text-decoration: none; }\n"
        html += ".content { color: #000000; }\n"
        html += ".source { font-size: 12px; text-align: center; }\n"
        html += ".tweet a:hover { text-decoration: underline; }\n"
        html += "h1, h3, .note { text-align: center; }\n"
        html += "iframe { width: 600px; height: 600px; }\n"
        html += "input { position: absolute; opacity: 0; z-index: -1; }\n"
        html += ".accordion { margin: 10px; border-radius: 5px; overflow: hidden; box-shadow: 0 4px 4px -2px rgba(0, 0, 0, 0.4); }\n"
        html += ".accordion-label { display: flex; justify-content: space-between; padding: 1em; font-weight: bold; cursor: pointer; background: #000000; color: #ffffff; }\n"
        html += ".accordion-content { max-height: 0; padding: 0 1em; background: white; transition: all 0.35s; }\n"
        html += (
            "input:checked ~ .accordion-content { max-height: 100vh; padding: 1em; }\n"
        )
        html += ".pagination { text-align: center; margin-top: 20px; }\n"
        html += ".pagination a { margin: 0 5px; text-decoration: none; color: #000000; padding: 1px 2px; border-radius: 5px; }\n"
        html += ".pagination a:hover { background-color: #e2e2e2; }\n"
        html += ".pagination a.selected { background-color: #e2e2e2; color: #000000; font-weight: bold; }\n"
        html += "</style>\n"

        html += "</head>\n<body>\n"

        html += f"<h1>Archived tweets of @{self.username}</h1>\n"
        html += (
            '<p class="note">The iframes (accordions) are best viewed in Firefox.</p>\n'
        )

        html += (
            '<p id="loading_first_page">Building pagination with JavaScript...</p>\n'
        )

        for page in range(1, total_pages + 1):
            html += (
                f'<div id="page_{page}" style="display:none;">\n'  # Starts a new page
            )
            html += '<div class="container">\n'

            start_index = (page - 1) * tweets_per_page
            end_index = min(start_index + tweets_per_page, len(self.json_path))

            for index in range(start_index, end_index):
                tweet = self.json_path[index]
                html += '<div class="tweet">\n'

                if not tweet.get("available_tweet_text"):
                    iframe_src = {
                        "Archived Tweet": tweet.get("archived_tweet_url"),
                        "Parsed Archived Tweet": tweet.get("parsed_archived_tweet_url"),
                        "Original Tweet": tweet.get("original_tweet_url"),
                        "Parsed Tweet": tweet.get("parsed_tweet_url"),
                    }

                    for key, value in (
                        (k, v) for k, v in iframe_src.items() if v is not None
                    ):
                        key_cleaned = key.replace(" ", "_")

                        html += '<div class="accordion">\n'
                        html += f'<input type="checkbox" id="tab_{index}_{key_cleaned}" />\n'
                        html += f'<label class="accordion-label" for="tab_{index}_{key_cleaned}">Click to load the iframe from {key}</label>\n'
                        html += '<div class="accordion-content">\n'

                        html += f'<div id="loading_{index}_{key_cleaned}" class="loading">Loading...</div>\n'
                        html += f'<iframe id="iframe_{index}_{key_cleaned}" height="600" width="600" frameborder="0" scrolling="auto" style="display: none;" onload="document.getElementById(\'loading_{index}_{key_cleaned}\').style.display=\'none\'; this.style.display=\'block\';"></iframe>\n'
                        html += "</div>\n"
                        html += "</div>\n"

                        html += """
                        <script>
                        // Loads the src attribute of the iframe tag
                        document.getElementById('tab_{index}_{key_cleaned}').addEventListener('change', function() {{
                            if (this.checked) {{
                                document.getElementById('loading_{index}_{key_cleaned}').style.display = 'block';
                                document.getElementById('iframe_{index}_{key_cleaned}').src = '{url}';
                            }}
                        }});
                        </script>
                        """.format(
                            index=index, url=value, key_cleaned=key_cleaned
                        )

                if tweet.get("available_tweet_text"):
                    html += "<br>\n"
                    html += f'<p><strong class="content">Available Tweet Content:</strong> {tweet.get("available_tweet_text")}</p>\n'
                    html += f'<p><strong class="content">Available Tweet Is Retweet:</strong> {tweet.get("available_tweet_is_RT")}</p>\n'
                    html += f'<p><strong class="content">Available Tweet Username:</strong> {tweet.get("available_tweet_info")}</p>\n'

                html += "<br>\n"
                html += f'<p><strong>Archived Tweet:</strong> <a href="{tweet.get("archived_tweet_url")}" target="_blank">{tweet.get("archived_tweet_url")}</a></p>\n'
                html += f'<p><strong>Parsed Archived Tweet:</strong> <a href="{tweet.get("parsed_archived_tweet_url")}" target="_blank">{tweet.get("parsed_archived_tweet_url")}</a></p>\n'
                html += f'<p><strong>Original Tweet:</strong> <a href="{tweet.get("original_tweet_url")}" target="_blank">{tweet.get("original_tweet_url")}</a></p>\n'
                html += f'<p><strong>Parsed Tweet:</strong> <a href="{tweet.get("parsed_tweet_url")}" target="_blank">{tweet.get("parsed_tweet_url")}</a></p>\n'
                html += f'<p><strong>Archived URL Key:</strong> {tweet.get("archived_urlkey")}</p>\n'
                html += f'<p><strong>Archived Timestamp:</strong> {timestamp_parser(tweet.get("archived_timestamp"))} ({tweet.get("archived_timestamp")})</p>\n'
                html += f'<p><strong>Archived mimetype:</strong> {tweet.get("archived_mimetype")}</p>\n'
                html += f'<p><strong>Archived Statuscode:</strong> {tweet.get("archived_statuscode")}</p>\n'
                html += f'<p><strong>Archived Digest:</strong> {tweet.get("archived_digest")}\n'
                html += f'<p><strong>Archived Length:</strong> {tweet.get("archived_length")}</p>\n'
                html += "</div>\n"

            html += "</div>\n</div>\n"  # Closes the page div and the container

        html += "<br>\n"

        # Adds navigation for the pages
        html += '<div class="pagination">\n'
        for page in range(1, total_pages + 1):
            html += f'<a href="#" id="page_link_{page}" onclick="showPage({page})">{page}</a>\n'
        html += "</div>\n"

        html += '<br><p class="source">generated by <a href="https://waybacktweets.claromes.com/" target="_blank">Wayback Tweets↗</a></p>\n'

        html += """
        <script>
        // Function to show the selected page and hide the others
        function showPage(page) {{
            for (let i = 1; i <= {total_pages}; i++) {{
                document.getElementById('page_' + i).style.display = 'none';
                document.getElementById('page_link_' + i).classList.remove('selected');
            }}

            document.getElementById('page_' + page).style.display = 'block';
            document.getElementById('page_link_' + page).classList.add('selected');
        }}

        // Initializes the page to show only the first page
        document.addEventListener('DOMContentLoaded', (event) => {{
            showPage(1); // Shows only the first page on load
            document.getElementById('loading_first_page').style.display = 'none';
        }});
        </script>
        """.format(
            total_pages=total_pages
        )

        html += "</body>\n"
        html += "</html>"

        return html

    def save(self, html_content: str) -> None:
        """
        Saves the generated HTML string to a file.

        Args:
            html_content (str): The HTML string to be saved.
        """
        with open(self.html_file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
```

## File: `waybacktweets/config/__init__.py`
```python
# flake8: noqa: F401

from waybacktweets.config.config import config
from waybacktweets.config.field_options import FIELD_OPTIONS
```

## File: `waybacktweets/config/config.py`
```python
"""
Configuration module.

Manages global configuration settings throughout the application.
"""

from dataclasses import dataclass


@dataclass
class _Config:
    """
    A class used to represent the configuration settings.

    Attributes:
        verbose (bool): Determines if verbose logging should be enabled.
    """

    verbose: bool = False


config = _Config()
"""
Global configuration instance.

Attributes:
    verbose (bool): Determines if verbose logging should be enabled.
"""
```

## File: `waybacktweets/config/field_options.py`
```python
"""
List of valid field options that can be used for parsing tweets.
"""

FIELD_OPTIONS = [
    "archived_urlkey",
    "archived_timestamp",
    "parsed_archived_timestamp",
    "archived_tweet_url",
    "parsed_archived_tweet_url",
    "original_tweet_url",
    "parsed_tweet_url",
    "available_tweet_text",
    "available_tweet_is_RT",
    "available_tweet_info",
    "archived_mimetype",
    "archived_statuscode",
    "archived_digest",
    "archived_length",
    "resumption_key",
]
```

## File: `waybacktweets/exceptions/__init__.py`
```python
# flake8: noqa: F401

from waybacktweets.exceptions.exceptions import (
    ConnectionError,
    EmptyResponseError,
    GetResponseError,
    HTTPError,
    ReadTimeoutError,
)
```

## File: `waybacktweets/exceptions/exceptions.py`
```python
"""
Wayback Tweets Exceptions
"""


class GetResponseError(Exception):
    """
    Base class for exceptions in get_response.
    """


class ReadTimeoutError(GetResponseError):
    """
    Exception raised for read timeout errors.
    """


class ConnectionError(GetResponseError):
    """
    Exception raised for connection errors.
    """


class HTTPError(GetResponseError):
    """
    Exception raised for HTTP errors.
    """


class EmptyResponseError(GetResponseError):
    """
    Exception raised for empty responses.
    """
```

## File: `waybacktweets/utils/__init__.py`
```python
# flake8: noqa: F401

from waybacktweets.utils.utils import (
    check_double_status,
    check_pattern_tweet,
    check_url_scheme,
    clean_tweet_url,
    clean_wayback_machine_url,
    delete_tweet_pathnames,
    get_response,
    is_tweet_url,
    semicolon_parser,
    timestamp_parser,
)
```

## File: `waybacktweets/utils/utils.py`
```python
"""
Utility functions for handling HTTP requests and manipulating URLs.
"""

import html
import re
from datetime import datetime
from typing import Optional, Tuple

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from waybacktweets.exceptions.exceptions import (
    ConnectionError,
    EmptyResponseError,
    GetResponseError,
    HTTPError,
    ReadTimeoutError,
)


def get_response(
    url: str, params: Optional[dict] = None
) -> Tuple[Optional[requests.Response], Optional[str], Optional[str]]:
    """
    Sends a GET request to the specified URL and returns the response.

    Args:
        url (str): The URL to send the GET request to.
        params (dict, optional): The parameters to include in the GET request.

    Returns:
        The response from the server.

    Raises:
        ReadTimeoutError: If a read timeout occurs.
        ConnectionError: If a connection error occurs.
        HTTPError: If an HTTP error occurs.
        EmptyResponseError: If the response is empty.
    """
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.3)
    adapter = HTTPAdapter(max_retries=retry)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"  # noqa: E501
    }

    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        response = session.get(url, params=params, headers=headers)
        response.raise_for_status()

        if not response or response.json() == []:
            raise EmptyResponseError("No data was saved due to an empty response.")
        return response
    except requests.exceptions.ReadTimeout:
        raise ReadTimeoutError
    except requests.exceptions.ConnectionError:
        raise ConnectionError
    except requests.exceptions.HTTPError:
        raise HTTPError
    except requests.exceptions.RequestException:
        raise GetResponseError


def clean_tweet_url(tweet_url: str, username: str) -> str:
    """
    Cleans a tweet URL by ensuring it is associated with the correct username.

    Args:
        tweet_url (str): The tweet URL to clean.
        username (str): The username to associate with the tweet URL.

    Returns:
        The cleaned tweet URL.
    """
    tweet_lower = tweet_url.lower()

    pattern = re.compile(r"/status/(\d+)")
    match_lower_case = pattern.search(tweet_lower)
    match_original_case = pattern.search(tweet_url)

    if match_lower_case and username in tweet_lower:
        return f"https://twitter.com/{username}/status/{match_original_case.group(1)}"
    else:
        return tweet_url


def clean_wayback_machine_url(
    wayback_machine_url: str, archived_timestamp: str, username: str
) -> str:
    """
    Cleans a Wayback Machine URL by ensuring it is associated with the correct username and timestamp.

    Args:
        wayback_machine_url (str): The Wayback Machine URL to clean.
        archived_timestamp (str): The timestamp to associate with the Wayback Machine URL.
        username (str): The username to associate with the Wayback Machine URL.

    Returns:
        The cleaned Wayback Machine URL.
    """  # noqa: E501
    wayback_machine_url = wayback_machine_url.lower()

    pattern = re.compile(r"/status/(\d+)")
    match = pattern.search(wayback_machine_url)

    if match and username in wayback_machine_url:
        return f"https://web.archive.org/web/{archived_timestamp}/https://twitter.com/{username}/status/{match.group(1)}"  # noqa: E501
    else:
        return wayback_machine_url


def check_pattern_tweet(tweet_url: str) -> str:
    """
    Extracts the URL from a tweet URL with patterns such as:

    - Reply: /status//
    - Link:  /status///
    - Twimg: /status/https://pbs

    Args:
        tweet_url (str): The tweet URL to extract the URL from.

    Returns:
        Only the extracted URL from a tweet.
    """
    pattern = r'/status/((?:"(.*?)"|&quot;(.*?)(?=&|$)|&quot%3B(.*?)(?=&|$)))'
    match = re.search(pattern, tweet_url)

    if match:
        if match.group(2):
            parsed_tweet_url = match.group(2)
        elif match.group(3):
            parsed_tweet_url = match.group(3)
        elif match.group(4):
            parsed_tweet_url = match.group(4)
        else:
            parsed_tweet_url = ""

        parsed_tweet_url = html.unescape(parsed_tweet_url)

        return parsed_tweet_url

    return tweet_url


def delete_tweet_pathnames(tweet_url: str) -> str:
    """
    Removes any pathnames from a tweet URL.

    Args:
        tweet_url (str): The tweet URL to remove pathnames from.

    Returns:
        The tweet URL without any pathnames.
    """
    pattern_username = re.compile(r"https://twitter\.com/([^/]+)/status/\d+")
    match_username = pattern_username.match(tweet_url)

    pattern_id = r"https://twitter.com/\w+/status/(\d+)"
    match_id = re.search(pattern_id, tweet_url)

    if match_id and match_username:
        tweet_id = match_id.group(1)
        username = match_username.group(1)
        return f"https://twitter.com/{username}/status/{tweet_id}"
    else:
        return tweet_url


def check_double_status(wayback_machine_url: str, original_tweet_url: str) -> bool:
    """
    Checks if a Wayback Machine URL contains two occurrences of "/status/" and if the original tweet does not contain "twitter.com".

    Args:
        wayback_machine_url (str): The Wayback Machine URL to check.
        original_tweet_url (str): The original tweet URL to check.

    Returns:
        True if the conditions are met, False otherwise.
    """  # noqa: E501
    if (
        wayback_machine_url.count("/status/") == 2
        and "twitter.com" not in original_tweet_url
    ):
        return True

    return False


def semicolon_parser(string: str) -> str:
    """
    Replaces semicolons in a string with %3B.

    Args:
        string (str): The string to replace semicolons in.

    Returns:
        The string with semicolons replaced by %3B.
    """
    return "".join("%3B" if c == ";" else c for c in string)


def is_tweet_url(twitter_url: str) -> bool:
    """
    Checks if the provided URL is a Twitter status URL.

    This function checks if the provided URL contains "/status/" exactly once, which is a common pattern in Twitter status URLs.

    Args:
        twitter_url (str): The URL to check.

    Returns:
        True if the URL is a Twitter status URL, False otherwise.
    """  # noqa: E501
    if twitter_url.count("/status/") == 1:
        return True

    return False


def timestamp_parser(timestamp: str) -> Optional[str]:
    """
    Parses a timestamp into a formatted string.

    Args:
        timestamp (str): The timestamp string to parse.

    Returns:
        Returns the parsed timestamp in strftime format, or None if parsing fails.
    """  # noqa: E501
    formats = [
        "%Y",
        "%Y%m",
        "%Y%m%d",
        "%Y%m%d%H",
        "%Y%m%d%H%M",
        "%Y%m%d%H%M%S",
    ]

    for fmt in formats:
        try:
            if not timestamp:
                return None
            parsed_time = datetime.strptime(timestamp, fmt)

            formatted_time = parsed_time.strftime("%Y/%m/%d %H:%M:%S")
            return formatted_time
        except ValueError:
            return None

    return None


def check_url_scheme(url):
    """
    Corrects the URL scheme if it contains more than two slashes following the scheme.

    This function uses a regular expression to find 'http:' or 'https:' followed by two or more slashes.
    It then replaces this with the scheme followed by exactly two slashes.

    Args:
        url (str): The URL to be corrected.

    Returns:
        The corrected URL.
    """  # noqa: E501
    pattern = r"(http:|https:)(/{2,})"

    def replace_function(match):
        scheme = match.group(1)
        return f"{scheme}//"

    parsed_url = re.sub(pattern, replace_function, url)

    return parsed_url
```

