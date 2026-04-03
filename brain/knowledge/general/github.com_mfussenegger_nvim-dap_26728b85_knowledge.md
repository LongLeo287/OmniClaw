---
id: github.com-mfussenegger-nvim-dap-26728b85-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:24.987239
---

# KNOWLEDGE EXTRACT: github.com_mfussenegger_nvim-dap_26728b85
> **Extracted on:** 2026-04-01 07:27:37
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007518947/github.com_mfussenegger_nvim-dap_26728b85

---

## File: `.busted`
```
return {
  _all = {
    coverage = false,
    lpath = "lua/?.lua;lua/?/init.lua",
    lua = "nvim -l",
  },
  default = {
    verbose = true
  },
  tests = {
    verbose = true
  },
}
```

## File: `.editorconfig`
```
root = true

[*.lua]
charset = utf-8
indent_style = space
indent_size = 2
trim_trailing_whitespace = true
insert_final_newline = true
```

## File: `.gitignore`
```
doc/tags
```

## File: `.luacheckrc`
```
ignore = {
  "631",    -- max_line_length
}
globals = {
  "vim",
}
read_globals = {
  "describe",
  "it",
  "before_each",
  "after_each",
  "assert"
}
```

## File: `.luarc.json`
```json
{
    "$schema": "https://raw.githubusercontent.com/sumneko/vscode-lua/master/setting/schema.json",
    "Lua.workspace.checkThirdParty": false
}
```

## File: `.woodpecker.yaml`
```yaml
---
when:
  - event: push
    branch: master
  - event: pull_request

matrix:
  nvim_version:
    - latest
    - 0.10
    - 0.11

steps:
  - name: test
    image: codeberg.org/mfussenegger/nvimdev:${nvim_version}
    pull: true
    commands:
      - apk add python3
      - luacheck .
      - busted
```

## File: `LICENSE.txt`
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
# DAP (Debug Adapter Protocol)

`nvim-dap` is a Debug Adapter Protocol client implementation for [Neovim][1].
`nvim-dap` allows you to:

- Launch an application to debug
- Attach to running applications and debug them
- Set breakpoints and step through code
- Inspect the state of the application

![demo][demo]

## Installation

[![LuaRocks](https://img.shields.io/luarocks/v/mfussenegger/nvim-dap?logo=lua&color=purple)](https://luarocks.org/modules/mfussenegger/nvim-dap)

- Install nvim-dap like any other Neovim plugin:
  - `git clone https://codeberg.org/mfussenegger/nvim-dap.git ~/.config/nvim/pack/plugins/start/nvim-dap`
  - Or with [vim-plug][11]: `Plug 'mfussenegger/nvim-dap'`
  - Or with [packer.nvim][12]: `use 'mfussenegger/nvim-dap'`
- Generate the documentation for nvim-dap using `:helptags ALL` or
  `:helptags <PATH-TO-PLUGIN/doc/>`

Supported Neovim versions:

- Latest nightly
- 0.11.x (Recommended)
- 0.10.4

You'll need to install and configure a debug adapter per language. See

- [:help dap.txt](doc/dap.txt)
- the [Debug-Adapter Installation][5] wiki
- `:help dap-adapter`
- `:help dap-configuration`

## Usage

A typical debug flow consists of:

- Setting breakpoints via `:DapToggleBreakpoint` or `:lua
  require'dap'.toggle_breakpoint()`.
- Launching debug sessions and resuming execution via `:DapNew` and
  `:DapContinue` or `:lua require'dap'.continue()`.
- Stepping through code via `:DapStepOver`, `:DapStepInto` or the corresponding
  functions `:lua require'dap'.step_over()` and `:lua
  require'dap'.step_into()`.
- Inspecting the state:
  - Via the built-in REPL: `:lua require'dap'.repl.open()`
    - Try typing an expression followed by ENTER to evaluate it.
    - Try commands like `.help`, `.frames`, `.threads`.
    - Variables with structure can be expanded and collapsed with ENTER on the
      corresponding line.
  - Via the widget UI (`:help dap-widgets`). Typically you'd inspect values,
    threads, stacktrace ad-hoc when needed instead of showing the information
    all the time, but you can also create sidebars for a permanent display
  - Via UI extensions:
    - IDE like: [nvim-dap-ui][15]
    - Middle ground between the IDE like nvim-dap-ui and the built-in widgets: [nvim-dap-view][nvim-dap-view]
    - Show inline values: [nvim-dap-virtual-text][7]

See [:help dap.txt](doc/dap.txt), `:help dap-mapping` and `:help dap-api`.

**Tip:**

The arrow keys are good candidates for keymaps to step through code as their
direction resembles the direction you'll step to.

- Down: Step over
- Right: Step into
- Left: Step out
- Up: Restart frame

You can setup keymaps temporary during a debug session using event listeners.
See `:help dap-listeners`.

## Supported languages

In theory all of the languages for which a debug adapter exists should be
supported.

- [Available debug adapters][13]
- [nvim-dap Debug-Adapter Installation & Configuration][5]

The Wiki is community maintained. If you got an adapter working that isn't
listed yet, please extend the Wiki.

Some debug adapters have [language specific
extensions](https://codeberg.org/mfussenegger/nvim-dap/wiki/Extensions#language-specific-extensions).
Using them over a manual configuration is recommended, as they're
usually better maintained.

If the instructions in the wiki for a debug adapter are not working, consider
that debug adapters may have made changes since the instructions were written.
You may want to read the release notes of the debug adapters or try with an
older version. Please update the wiki if you discover outdated examples.

## Goals

- Have a basic debugger in Neovim.
- Extensibility and double as a DAP client library. This allows other plugins
  to extend the debugging experience. Either by improving the UI or by making
  it easier to debug parts of an application.

  All known extensions are listed in the [Wiki][10]. The wiki is community
  maintained. Please add new extensions if you built one or if you discovered
  one that's not listed.

## Non-Goals

- Debug adapter installations are out of scope. It's not the business of an
  editor plugin to re-invent a package manager. Use your system package
  manager. Use Nix. Use Ansible.

- [nvim-dapconfig](https://github.com/nvim-lua/wishlist/issues/37#issuecomment-1023363686)

- Vim support. It's not going to happen. Use [vimspector][2] instead.

## Alternatives

- [vimspector][2]


## Contributing

Contributions are welcome:

- Give concrete feedback about usability.
- Triage issues. Many of the problems people encounter are debug
  adapter specific.
- Improve upstream debug adapter documentation to make them more editor
  agnostic.
- Improve the Wiki. But please refrain from turning it into comprehensive debug
  adapter documentation that should go upstream.
- Write extensions.

Before making direct code contributions, please create a discussion or issue to
clarify whether the change is in scope of the nvim-dap core.

Please keep pull requests focused and don't change multiple things at the same
time.

## Features

- [x] launch debug adapter
- [x] attach to debug adapter
- [x] toggle breakpoints
- [x] breakpoints with conditions
- [x] logpoints
- [x] set exception breakpoints
- [x] step over, step into, step out
- [x] step back, reverse continue
- [x] Goto
- [x] restart
- [x] stop
- [x] pause
- [x] evaluate expressions
- [x] REPL (incl. commands to show threads, frames and scopes)


[1]: https://neovim.io/
[2]: https://github.com/puremourning/vimspector
[5]: https://codeberg.org/mfussenegger/nvim-dap/wiki/Debug-Adapter-installation
[7]: https://github.com/theHamsta/nvim-dap-virtual-text
[10]: https://codeberg.org/mfussenegger/nvim-dap/wiki/Extensions
[11]: https://github.com/junegunn/vim-plug
[12]: https://github.com/wbthomason/packer.nvim
[13]: https://microsoft.github.io/debug-adapter-protocol/implementors/adapters/
[15]: https://github.com/rcarriga/nvim-dap-ui
[demo]: https://user-images.githubusercontent.com/38700/124292938-669a7100-db56-11eb-93b8-77b66994fc8a.gif
[nvim-dap-view]: https://github.com/igorlfs/nvim-dap-view
```

## File: `nvim-dap-scm-1.rockspec`
```
local _MODREV, _SPECREV = 'scm', '-1'
rockspec_format = "3.0"
package = 'nvim-dap'
version = _MODREV .. _SPECREV

description = {
  summary = 'Debug Adapter Protocol client implementation for Neovim.',
  detailed = [[
  nvim-dap allows you to:

  * Launch an application to debug
  * Attach to running applications and debug them
  * Set breakpoints and step through code
  * Inspect the state of the application
  ]],
  labels = {
    'neovim',
    'plugin',
    'debug-adapter-protocol',
    'debugger',
  },
  homepage = 'https://codeberg.org/mfussenegger/nvim-dap',
  license = 'GPL-3.0',
}

dependencies = {
  'lua >= 5.1, < 5.4',
}

test_dependencies = {
}

source = {
   url = 'git://codeberg.org/mfussenegger/nvim-dap',
}

build = {
   type = 'builtin',
   copy_directories = {
     'doc',
     'plugin',
   },
}
```

## File: `doc/dap.txt`
```
*dap.txt*                                         DAP client


nvim-dap is a Debug Adapter Protocol client, or "debugger", or "debug-frontend".

With the help of a debug adapter it can:

- Launch an application to debug
- Attach to running applications to debug them
- Set breakpoints and step through code
- Inspect the state of the application

A debug adapter is a facilitator between nvim-dap (the client), and a
language-specific debugger:


    DAP-Client ----- Debug Adapter ------- Debugger ------ Debugee
    (nvim-dap)  |   (per language)  |   (per language)    (your app)
                |                   |
                |        Implementation specific communication
                |        Debug adapter and debugger could be the same process
                |
         Communication via the Debug Adapter Protocol


To debug applications, you need to configure two things per language:

- A debug adapter (|dap-adapter|).
- How to launch your application to debug or how to attach to a running
  application (|dap-configuration|).


Available debug adapters:
  https://microsoft.github.io/debug-adapter-protocol/implementors/adapters/

Debug adapter configuration and installation instructions:
  https://codeberg.org/mfussenegger/nvim-dap/wiki/Debug-Adapter-installation

Debug Adapter Protocol:
  https://microsoft.github.io/debug-adapter-protocol/

                                      Type |gO| to see the table of contents.

==============================================================================
ADAPTER CONFIGURATION                                *dap-adapter*


Neovim needs a debug adapter with which it can communicate. Neovim can either
launch the debug adapter itself, or it can attach to an existing one.

To tell Neovim if it should launch a debug adapter or connect to one, and if
so, how, you need to configure them via the `dap.adapters` table. The key of
the table is an arbitrary name that debug adapters are looked up by when using
a |dap-configuration|.

For example, to register the `debugpy` debug adapter you can add the following 
entry:

>lua
  local dap = require('dap')
  dap.adapters.debugpy = {
    type = 'executable';
    command = os.getenv('HOME') .. '/.virtualenvs/tools/bin/python';
    args = { '-m', 'debugpy.adapter' };
  }
<

`dap.adapters.<name>` is set to a `Adapter`.

The `Adapter` needs to contain a `type`, which can be one of:

- `executable`, to indicate that nvim-dap must launch the debug adapter. In
  this case nvim-dap will spawn the given process and communicate with it using
  stdio.

- `server`, to connect to a debug adapter via TCP.
  The adapter must be running, or started with a debug session via a
  `executable` configuration of the adapter. See the options further below.

- `pipe`, to connect to a debug adapter via a unix domain socket or named pipe.
  The adapter must be running, or started with a debug session via a
  `executable` configuration of the adapter. See the options further below.

For `executable` the following options are supported:

>
    command: string         -- command to invoke
    args:    string[]       -- arguments for the command
    options?: {
      env?: {}              -- Set the environment variables for the command
      cwd?: string          -- Set the working directory for the command
      detached?: boolean    -- Spawn the debug adapter process in a detached state.
                               Defaults to true.
    }
    id?: string             -- Identifier of the adapter. This is used for the
                               `adapterId` property of the initialize request.
                               For most debug adapters setting this is not
                               necessary.

For `server` the following options are supported:

>
    host?: string             -- host to connect to, defaults to 127.0.0.1
    port:  number|"${port}"   -- port to connect to.
                              -- If "${port}" nvim-dap resolves a free port.
                              -- This is intended to be used with
                              -- `executable.args` further below below
    id?: string               -- Identifier of the adapter. This is used for the
                                 `adapterId` property of the initialize request.
                                  For most debug adapters setting this is not
                                  necessary.

    -- nvim-dap can optionally launch the debug-adapter on each new debug session
    -- And then connect via TCP.
    --
    executable?: {
      command: string       -- command that spawns the server
      args?: string[]       -- command arguments
                            -- ${port} used in the args is replaced with a
                            -- dynamically resolved free port number
      detached?: boolean    -- Spawn the debug adapter in detached mode.
                            -- Defaults to true.
      cwd?: string          -- Working directory
    }

    options?: {
      max_retries?: number  -- Amount of times the client should attempt to
                            -- connect before erroring out.
                            -- There is a 250ms delay between each retry
                            -- Defaults to 14 (3.5 seconds)
    }


For `pipe` the following options are supported:

>
    pipe: string      -- Absolute path to the pipe file.
                      -- If `${pipe}` nvim-dap generates a temporary filename
                      -- that is intended for use with `executable`

    -- nvim-dap can optionally launch the debug-adapter on each new debug session
    -- And then connect to the socket or named pipe
    executable?: {
      command: string       -- command that spawns the server
      args?: string[]       -- command arguments
                            -- ${pipe} used in the args is replaced with a
                            -- dynamically resolved temporary file
      detached?: boolean    -- Spawn the debug adapter in detached mode.
                            -- Defaults to true.
      cwd?: string          -- Working directory
    }

    options?: {
      timeout?: integer  -- Max amount of time in ms to wait between spawning
                         -- the executable and connecting to the pipe. This
                         -- gives the executable time to create the pipe.
                         -- Defaults to 5000ms
    }


All types support the following additional options:

>
    options?: {
      initialize_timeout_sec?: number  -- How many seconds the client waits for a
                                       -- response on a initialize request before
                                       -- emitting a warning. Defaults to 4

      disconnect_timeout_sec?: number  -- How many seconds the client waits for
                                       -- a disconnect response from the debug
                                       -- adapter before emitting a warning and
                                       -- closing the connection. Defaults to 3

      source_filetype?: string         -- The filetype to use for content
                                       -- retrieved via a source request.


`dap.adapters.<name>` can also be set to a function which takes three arguments:

- A `on_config` callback. This must be called with the actual adapter table.
- The |dap-configuration| which the user wants to use.
- An optional parent session. This is only available if the debug-adapter
  wants to start a child-session via a `startDebugging` request.


This can be used to defer the resolving of the values to when a configuration
is used. A use-case for this is starting an adapter asynchronous. For example,
for java-debug:
>
>lua
  dap.adapters.java = function(callback, config)
    M.execute_command({command = 'vscode.java.startDebugSession'}, function(err0, port)
      assert(not err0, vim.inspect(err0))
      callback({ type = 'server'; host = '127.0.0.1'; port = port; })
    end)
  end
<

There is an additional `enrich_config` property available for both adapter
types. This property is a function which allows an adapter to enrich a
configuration with additional information. It receives a configuration as first
argument, and a callback that must be called with the final configuration as
second argument.

An example use-case of this is the Java Debug Adapter, which can resolve
classPaths or modulePaths dynamically, so that users don't have to do that.

>lua
  local adapter = {
    type = 'server';
    host = '127.0.0.1';
    port = 8080;
    enrich_config = function(config, on_config)
      local final_config = vim.deepcopy(config)
      final_config.extra_property = 'This got injected by the adapter'
      on_config(final_config)
    end;
  }
<

==============================================================================
DEBUGEE CONFIGURATION                                *dap-configuration*


In addition to launching (possibly) and connecting to a debug adapter, Neovim
needs to instruct the debug adapter itself how to launch and connect to the
debugee. The debugee is the application you want to debug.

This is controlled via a `Configuration`, which has 3 required fields:

>
    type: string        -- Which debug adapter to use.
    request: string     -- Either `attach` or `launch`. Indicates whether the
                        -- debug adapter should launch a debugee or attach to
                        -- one that is already running.
    name: string        -- A user-readable name for the configuration.
<

In addition, a `Configuration` accepts an arbitrary number of further options
which are debug-adapter-specific.

Configurations are set in the `dap.configurations` table. The keys are
filetypes. If you run |dap.continue()| it will look up configurations under the
current filetype.

For example:

>lua
    local dap = require('dap')
    dap.configurations.python = {
      {
        type = 'debugpy';
        request = 'launch';
        name = "Launch file";
        program = "${file}";
        pythonPath = function()
          return '/usr/bin/python'
        end;
      },
    }
<

Things to note:

- Values for properties other than the 3 required properties `type`,
  `request`, and `name` can be functions. If a value is given as a function,
  the function will be evaluated to get the property value when the
  configuration is used.

  To support asynchronous operations, the function can return a `thread`
  (created via `coroutine.create`) following two constraints:

    - The coroutine/thread must be in a suspended state
    - The coroutine/thread must resume the nvim-dap `run` coroutine with the
      result

  An example:

>lua
    foo = function()
      return coroutine.create(function(dap_run_co)
        local items = {'one', 'two'}
        vim.ui.select(items, { label = 'foo> '}, function(choice)
          coroutine.resume(dap_run_co, choice)
        end)
      end)
    end,
<

- Functions for top level properties can return the `dap.ABORT` constant to
  signal that you want to abort starting a debug session. An example:

>lua
    program = function()
      local path = vim.fn.input({
        prompt = 'Path to executable: ',
        default = vim.fn.getcwd() .. '/',
        completion = 'file'
      })
      return (path and path ~= "") and path or dap.ABORT
    end
<

- The configuration can have an optional metatable with `__call`
  implementation. The function will get called when the configuration is used
  and it must return a new configuration table. This can be used to
  dynamically add multiple properties at once.

- Some variables are supported:
  - `${file}`: Active filename
  - `${fileBasename}`: The current file's basename
  - `${fileBasenameNoExtension}`: The current file's basename without extension
  - `${fileDirname}`: The current file's dirname
  - `${fileExtname}`: The current file's extension
  - `${relativeFile}`: The current file relative to |getcwd()|
  - `${relativeFileDirname}`: The current file's dirname relative to |getcwd()|
  - `${workspaceFolder}`: The current working directory of Neovim
  - `${workspaceFolderBasename}`: The name of the folder opened in Neovim
  - `${command:pickProcess}`: Open dialog to pick process using |vim.ui.select|
  - `${command:pickFile}`: Open dialog to pick file using |vim.ui.select|
  - `${env:Name}`: Environment variable named `Name`, for example: `${env:HOME}`.

==============================================================================
DEBUGEE CONFIGURATION via launch.json                *dap-launch.json*


nvim-dap supports a subset of the `launch.json` file format used to configure
debug adapters in Visual Studio Code.
`.vscode/launch.json` are read automatically whenever you start a new debug
session using |dap.continue()| or `:DapNew`. (via a configuration provider,
see |dap-providers-configs|)

Unlike VS Code, nvim-dap supports standard JSON. Trailing commas on the
last item of a list are an error.
If you install a 3rd-party json5 parser you can override the json decode
function to support json5 features like trailing comma.
>
    require('dap.ext.vscode').json_decode = require'json5'.parse
<
(One json5 parser implementation is https://github.com/Joakker/lua-json5)


An example `launch.json` looks like this:

>json
  {
      "version": "0.2.0",
      "configurations": [
          {
              "type": "java",
              "request": "launch",
              "name": "Launch Java"
          },
          {
              "type": "cppdbg",
              "request": "launch",
              "name": "Launch CPP"
          }
      ]
  }
<

load_launchjs supports `inputs`. Inputs can be used to define custom input prompts.
They are declared in an "inputs" array and each input must have the following properties:

- "id": the identifier of an input
- "type": Either `pickString` or `promptString`
- "description": Descriptive text shown to the user
- "default": Default value (Defaults to '' if not provided)

`pickString` has an additional "options" property, which is an array of strings
or an array of option objects with label and value:

- [ "my value 1", "my value 2", "my value 3" ]
- [ { "label": "my label", "value", "my value"} ]

These are shown to the user as options.

Inputs can be referenced with `${input:<id>}` placeholders.

>json
  {
      "version": "0.2.0",
      "configurations": [
          {
              "type": "debugpy",
              "request": "launch",
              "name": "Launch",
              "program": "${input:myPrompt}"
          }
      ],
      "inputs": [
          {
              "id": "myPrompt",
              "type": "pickString",
              "description": "Program to run: ",
              "default": "foobar"
          }
      ]
  }
<

You can define system specific properties by placing them into a `linux`, `osx` or
`windows` sub-object. An example:
>json
  {
    "type": "cppdbg",
    "request": "launch",
    "name": "Launch CPP",
    "linux": {
      "MIMode": "gdb",
      "miDebuggerPath": "/usr/bin/gdb"
    },
    "osx": {
      "MIMode": "lldb",
      "miDebuggerPath": "/usr/local/bin/lldb-mi"
    },
    "windows": {
      "MIMode": "gdb",
      "miDebuggerPath": "C:\\MinGw\\bin\\gdb.exe"
    }
  }
<

On `linux`, the final configuration will look like this:

>json
  {
    "type": "cppdbg",
    "request": "launch",
    "name": "Launch CPP",
    "MIMode": "gdb",
    "miDebuggerPath": "/usr/bin/gdb"
  }
<

And on `windows` it will look like this:

>json
  {
    "type": "cppdbg",
    "request": "launch",
    "name": "Launch CPP",
    "MIMode": "gdb",
    "miDebuggerPath": "C:\\MinGw\\bin\\gdb.exe"
  }
<

==============================================================================
SIGNS CONFIGURATION


nvim-dap uses five signs:

- `DapBreakpoint` for breakpoints (default: `B`)
- `DapBreakpointCondition` for conditional breakpoints (default: `C`)
- `DapLogPoint` for log points (default: `L`)
- `DapStopped` to indicate where the debugee is stopped (default: `→`)
- `DapBreakpointRejected` to indicate breakpoints rejected by the debug
  adapter (default: `R`)

You can customize the signs by setting them with the |sign_define()| function.
For example:

>
>lua
  vim.fn.sign_define('DapBreakpoint', {text='🛑', texthl='', linehl='', numhl=''})
<

==============================================================================
REPL COMPLETION                                               *dap-completion*


nvim-dap includes an omnifunc implementation which uses the active debug
session to get completion candidates.

It is enabled by default in the REPL, which means you can use `CTRL-X CTRL-O`
to trigger completion within the REPL.

You can also configure completion to trigger automatically:

>vim
  au FileType dap-repl lua require('dap.ext.autocompl').attach()
<

Completion will then trigger automatically on any of the completion trigger
characters reported by the debug adapter, or on `.` if none are reported.

==============================================================================
MAPPINGS                                             *dap-mappings*


nvim-dap does not configure any mappings by default to avoid conflicts with
user defined keymaps.

Some example mappings you could configure:
>lua
    vim.keymap.set('n', '<F5>', function() require('dap').continue() end)
    vim.keymap.set('n', '<F10>', function() require('dap').step_over() end)
    vim.keymap.set('n', '<F11>', function() require('dap').step_into() end)
    vim.keymap.set('n', '<F12>', function() require('dap').step_out() end)
    vim.keymap.set('n', '<Leader>b', function() require('dap').toggle_breakpoint() end)
    vim.keymap.set('n', '<Leader>B', function() require('dap').set_breakpoint() end)
    vim.keymap.set('n', '<Leader>lp', function() require('dap').set_breakpoint(nil, nil, vim.fn.input('Log point message: ')) end)
    vim.keymap.set('n', '<Leader>dr', function() require('dap').repl.open() end)
    vim.keymap.set('n', '<Leader>dl', function() require('dap').run_last() end)
    vim.keymap.set({'n', 'v'}, '<Leader>dh', function()
      require('dap.ui.widgets').hover()
    end)
    vim.keymap.set({'n', 'v'}, '<Leader>dp', function()
      require('dap.ui.widgets').preview()
    end)
    vim.keymap.set('n', '<Leader>df', function()
      local widgets = require('dap.ui.widgets')
      widgets.centered_float(widgets.frames)
    end)
    vim.keymap.set('n', '<Leader>ds', function()
      local widgets = require('dap.ui.widgets')
      widgets.centered_float(widgets.scopes)
    end)
<

==============================================================================
USER COMMANDS                                             *dap-user-commands*

nvim-dap provides the following user commands.

Session management:

- `DapContinue`: Continue executing a paused session or start a new one
- `DapDisconnect`: Disconnect from an active debugging session
- `DapNew`: Start one or more new debug sessions
- `DapTerminate`: Terminate the current session

Stepping:

- `DapRestartFrame`: Restart the active sessions' current frame
- `DapStepInto`: Step into the current expression
- `DapStepOut`: Step out of the current scope
- `DapStepOver`: Step over the current line
- `DapPause`: Pause the current thread or pick a thread to pause

REPL:

- `DapEval`: Create a new window & buffer to evaluate expressions. Use `:w` to
trigger evaluation of the buffer contents.
- `DapToggleRepl`: Open or close the REPL

Breakpoints:

- `DapClearBreakpoints` : Clear all breakpoints
- `DapToggleBreakpoint` : Set or remove a breakpoint at the current line

Diagnostics:

- `DapSetLogLevel` : Set the log level
- `DapShowLog` : Show the session log in a split window

==============================================================================
CLIENT CONFIGURATION                                             *dap.defaults*

nvim-dap has a few client configuration options which you can either set
globally, or scoped to a specific "type" (from |dap-configuration|).

The configuration values are set via `dap.defaults.fallback` (for global) or
`dap.defaults.<type>`. The configuration options are:

- `stepping_granularity`: (string) The default stepping granularity to use when
  stepping. Defaults to `statement`, can be `statement`, `line` or
  `instructions`.

- `terminal_win_cmd`: (string|fun) The command used to create the window for
  the integrated terminal. (See |dap-terminal|). Either a string or a function
  that must return a buffer number and a window number of the buffer/window
  for the terminal.
  When using a function, it receives the current debug configuration as an 
  argument, allowing for dynamic terminal naming and setup based on the 
  session's configuration.

  Note that extensions like `nvim-dap-ui` use this to control the UI.
  If you customize it, you may break their behavior.

- `focus_terminal`: (boolean) If the integrated terminal should get focus when
  its created. Defaults to false

- `auto_continue_if_many_stopped`. (boolean). Controls if a thread should
  automatically resume on a stopped event if another thread is already
  stopped. If your application uses multi-threading and you want multiple
  threads to be able to stop, you may want to set this to false.
  Defaults to true.

- switchbuf. (string|fun). Controls the behavior when jumping to a
  breakpoint. See |'switchbuf'|. Defaults to the global `'switchbuf'` setting.

  nvim-dap provides an additional `usevisible` option
  that can be used to prevent jumps within the active
  window if a stopped event is within the visible region.
  Best used in combination with other options. For
  example: 'usevisible,usetab,uselast'

  For more complex use cases, nvim-dap allows overriding with a function. The
  function receives 3 arguments: (bufnr, line, column). It has full control of
  how Neovim should behave and it is not expected to return anything.


- `on_output`. A function with two parameters: `session` and `output_event`:
  Overrides the default output handling with a custom handler.

  If you'd like to keep the default handling and still execute custom logic
  for output events you can instead use the listener system. See |dap-extensions|.

  See https://microsoft.github.io/debug-adapter-protocol/specification#Events_Output
  for a description of the payload.

  An example:
>lua
  ---@param session dap.Session
  ---@param output_event dap.OutputEvent
  dap.defaults.fallback.on_output = function(session, output_event)
    -- ignore all outputs
  end


- `autostart`. Name of a configuration to start implicitly if evaluating an
  expression in the REPL without active session.
<

Some more examples:
>lua
  local dap = require('dap')
  -- Use "tabnew" for all debug adapters
  dap.defaults.fallback.terminal_win_cmd = 'tabnew'
  -- Except for debugpy
  dap.defaults.debugpy.terminal_win_cmd = 'belowright new'

  dap.defaults.java.auto_continue_if_many_stopped = false

  dap.defaults.fallback.autostart = "nluarepl"
<

==============================================================================
TERMINAL CONFIGURATION                                          *dap-terminal*


Some debug adapters support launching the debugee in an integrated or external
terminal.

For that they usually provide a `console` option in their |dap-configuration|.
The supported values are sometimes called `internalConsole`,
`integratedTerminal` and `externalTerminal`, but you need to consult the debug
adapter documentation to figure out the concrete property name and values.


If you want to use the `externalTerminal` you need to setup the terminal which
should be launched by nvim-dap:

>lua
  local dap = require('dap')
  dap.defaults.fallback.external_terminal = {
    command = '/usr/bin/alacritty';
    args = {'-e'};
  }
<

Some debug adapters support launching the debugee in a terminal, but don't
provide an option to choose between integrated terminal or external terminal.
`nvim-dap` provides an option to force the external terminal.

>lua
  local dap = require('dap')
  dap.defaults.fallback.force_external_terminal = true
<

If you're using the integrated terminal, you can configure the command
that is used to create a split window:

>lua
  local dap = require('dap')
  dap.defaults.fallback.terminal_win_cmd = '50vsplit new'
<

The `terminal_win_cmd` defaults to `belowright new`. The value can also be a
function which returns a buffer number and optionally a window ID.

Be default `dap` opens the integrated terminal but keeps focus on the current
buffer. If you rather have focus to be shifted to the terminal when it opens
you can configure:

>lua
  local dap = require('dap')
  dap.defaults.fallback.focus_terminal = true
<

`fallback` can be replaced with the |dap-adapter| type to have type
specific terminal configurations.

==============================================================================
API                                                  *dap-api*


Lua module: dap


continue({opts})                                                *dap.continue()*
        `continue()` resumes the execution of an application [count] times if a
        debug session is active and a thread was stopped. Threads are usually
        stopped when a breakpoint is hit or an exception occurred.

        If no debug session is active, `continue()` will start a new debug session by:

        - Looking up the configurations (|dap-configuration|) for the current filetype.
        - If there is more than one configuration it will prompt the user to
          select one of them.
        - It calls |dap.run()| on the selected configuration.

        `continue()` is the main entry-point for users to start debugging an
        application.

        Parameters:
            {opts}    Optional table with:
                      - `new: boolean` force starting an additional debug session


run({config}, {opts})                                                *dap.run()*
        Looks up a debug adapter entry for the given configuration and runs it.
        This is implicitly called by |dap.continue()| if no debug session is
        active.

        Most users will want to start debugging using |dap.continue()| instead
        of using `run()`.  `run()` is intended for nvim-dap extensions which
        create configurations dynamically, for example to debug individual test
        cases.

        If a debug session with the same name is already active, it will
        restart the session.

        Parameters:
            {config}  |dap-configuration| to run
            {opts}    Optional table with:
                      - `new: boolean` force starting an additional debug session


run_last()                                                      *dap.run_last()*
        Re-runs the last debug adapter / configuration that ran using
        |dap.run()|.


restart({config})                                                *dap.restart()*
        Restart the current session.
        Does nothing if there is no active session.

        Parameters:
          {config}  |dap-configuration| to use. Defaults to the same
          configuration used to start the current session.


terminate(opts),                                              *dap.terminate()*
        Terminates the debug session.

        If the debug adapter doesn't support the `terminateRequest`
        capability, this will instead call |dap.disconnect()| with
        `terminateDebugee = true`.

        If disconnect is used, the `terminateDebugee` and `suspendDebugee`
        options will only take effect if the debug adapter has the
        corresponding capabilities.

        Parameters: ~
            {opts}  Table containing:

                     - `terminate_args`: table; used if terminate is supported:
                       - `restart: boolean?

                     - `disconnect_args`: table; used if terminate is not
                       supported:
                       - `restart`: `boolean?`
                       - `terminateDebugee`: `boolean?`
                       - `suspendDebugee`: `boolean?`

                     - `on_done`: function triggered once terminate or
                       disconnect completes

                     - `all`: `boolean`: flag indicating that all root sessions
                       should be terminated instead of only the currently
                       focused session. Defaults to false

                     - `hierarchy`: `boolean`: flag indicating that child and
                       parent sessions should be terminated. This will affect
                       the current focused session unless combined with `all`,
                       in that case it terminates all root sessions including
                       all their children.


set_breakpoint({condition}, {hit_condition}, {log_message})
                                                          *dap.set_breakpoint()*

        Same as |toggle_breakpoint|, but is guaranteed to overwrite previous 
        breakpoint.

toggle_breakpoint({condition}, {hit_condition}, {log_message})
                                                       *dap.toggle_breakpoint()*

        Creates or removes a breakpoint at the current line.

        Parameters: ~
            {condition}     Optional condition that must be met for the debugger
                            to stop at the breakpoint.
            {hit_condition} Optional hit condition, e.g. a number as a string
                            that tells how often this breakpoint should be visited
                            to stop.
            {log_message}   Optional log message. This transforms the breakpoint 
                            into a log point. Variable interpolation with {foo} is
                            supported within the message.

list_breakpoints()                                     *dap.list_breakpoints()*

        Lists all breakpoints and log points in quickfix window.

clear_breakpoints()                                   *dap.clear_breakpoints()*

    Removes all breakpoints

set_exception_breakpoints({filters}, {exceptionOptions})
                                              *dap.set_exception_breakpoints()*

    Sets breakpoints on exceptions filtered by `filters`. If `filters` is not
    provided it will prompt the user to choose from the available filters of the
    debug adapter.

    Parameters: ~
        {filters}          A list of exception types to stop on (optional).
                           Most debug adapters offer categories like `"uncaught"` and
                           `"raised"` to filter the exceptions.
                           If set to "default" instead of a table, the
                           default options as recommended by the debug adapter are
                           used.
        {exceptionOptions} ExceptionOptions[]?
                           (https://microsoft.github.io/debug-adapter-protocol/specification#Types_ExceptionOptions)

    >lua
        -- Ask user to stop on which kinds of exceptions
        require'dap'.set_exception_breakpoints()
        -- don't stop on exceptions
        require'dap'.set_exception_breakpoints({})
        -- stop only on certain exceptions (debugpy offers "raised", "uncaught")
        require'dap'.set_exception_breakpoints({"uncaught"})
        require'dap'.set_exception_breakpoints({"raised", "uncaught"})
        -- use default settings of debug adapter
        require'dap'.set_exception_breakpoints("default")
<

    You can also set the default value via a `defaults.fallback` table:

>lua
        require('dap').defaults.fallback.exception_breakpoints = {'raised'}
<

    Or per config/adapter type:

>lua
        require('dap').defaults.debugpy.exception_breakpoints = {'raised'}
<

    In this example `debugpy` is the type. This is the same type used in
    |dap-configuration| or the |dap-adapter| definition.


step_over([{opts}])                                            *dap.step_over()*
        Requests the debugee to run again for [count] steps.

        For {opts} see |step_into|.


step_into([{opts}])                                            *dap.step_into()*
        Requests the debugee to step into a function or method if possible.
        If it cannot step into a function or method it behaves like
        |dap.step_over()|.

        If the debug adapter has the `supportsStepInTargetsRequest` capability and
        {askForTargets} is true, the user can choose into which function they
        want to step into if there are multiple choices.

        Some debug adapters allow a more fine-grained control over the
        behavior of this command using the `granularity` {opts} parameter:

        granularity:
          Can be 'statement' | 'line' | 'instruction'
          Will fall back to dap.defaults.fallback.stepping_granularity
          Default: 'statement'

        askForTargets:
          Ask the user to step into which function if there are multiple choices.
          Only for step_into.


step_out([{opts}])                                              *dap.step_out()*
        Requests the debugee to step out of a function or method if possible.

        For options see |step_into|.

step_back([{opts}]                                             *dap.step_back()*
        Steps one step back. Debug adapter must support reverse debugging.

        For {opts} see |step_into|.

pause({thread_id})                                                 *dap.pause()*
        Requests debug adapter to pause a thread. If there are multiple threads
        it stops `thread_id` from the optional parameter or asks the user which
        thread to pause.

reverse_continue()                                      *dap.reverse_continue()*
        Continues execution reverse in time until last breakpoint.
        Debug adapter must support reverse debugging.

up()                                                                  *dap.up()*
        Go up in current stacktrace without stepping.

down()                                                              *dap.down()*
        Go down in current stacktrace without stepping.


goto_({line})                                                      *dap.goto_()*
        Let the debugger jump to a specific line or line under cursor.
        This is an optional feature and not all debug adapters support it.

        The code between the current location and the goto target is not
        executed but skipped.

        Parameters: ~
            {line}  Line number or line under cursor if nil.

focus_frame()                                                 *dap.focus_frame()*
        Jump/focus the current frame.

        Which window to use depends on the `switchbuf` setting. See
        |dap.defaults|.

        A current frame is set when breakpoints are hit or when traversing
        the stack using |dap.up()|, |dap.down()| or the threads and frames
        widgets. See |dap-widgets|.

        This is a no-op if there is no active session.
        If there is a session active but no current frame it opens the threads
        widget to allow pausing threads and picking a frame to focus.


restart_frame()                                            *dap.restart_frame()*
        Restart execution of the current frame

        This is an optional feature and not all debug adapters support it.


run_to_cursor()                                            *dap.run_to_cursor()*
        Continues execution to the current cursor.

        This temporarily removes all breakpoints, sets a breakpoint at the
        cursor, resumes execution and then adds back all breakpoints again.


repl.open({winopts}, {wincmd})                                 *dap.repl.open()*
        Open a REPL / Debug-console.

        Parameters: ~
            {winopts}  optional table which may include:
                        `height` to set the window height
                        `width` to set the window width
                        Any other key/value pair, that will be treated as window
                        option.

            {wincmd} command that is used to create the window for
                     the REPL. Defaults to 'belowright split'


        The REPL can be used to evaluate expressions.

        Starting with nvim 0.12 you can input multiline text by using
        Shift+Enter to add a new line without submitting the prompt, or just
        |put| or |paste| multiline text.

        Alternatively you can write the input text in a dedicated
        `dap-eval://` buffer. Open one using `:DapEval`, input any expression
        you want to evaluate as regular text and then use
        `:w` to evaluate the expression.

        A `omnifunc` is set to support completion of expressions.
        It supports the following special commands:

          .exit               Closes the REPL
          .c or .continue     Same as |dap.continue|
          .n or .next         Same as |dap.step_over|
          .ni or .nexti       Same as |dap.step_over| with instruction granularity
          .into               Same as |dap.step_into|
          .intoi              Same as |dap.step_into| with instruction granularity
          .into_target        Same as |dap.step_into{askForTargets=true}|
          .out                Same as |dap.step_out|
          .up                 Same as |dap.up|
          .down               Same as |dap.down|
          .goto               Same as |dap.goto_|
          .scopes             Prints the variables in the current scopes
          .threads            Prints all threads
          .frames             Print the stack frames
          .capabilities       Print the capabilities of the debug adapter
          .b or .back         Same as |dap.step_back|
          .bi or .backi       Same as |dap.step_back| with instruction granularity
          .rc or
          .reverse-continue   Same as |dap.reverse_continue|

        You can customize the builtin command names or define your own
        custom commands by extending `dap.repl.commands`:

        >lua
          local repl = require 'dap.repl'
          repl.commands = vim.tbl_extend('force', repl.commands, {
            -- Add a new alias for the existing .exit command
            exit = {'exit', '.exit', '.bye'},
            -- Add your own commands; run `.echo hello world` to invoke
            -- this function with the text "hello world"
            custom_commands = {
              ['.echo'] = function(text)
                dap.repl.append(text)
              end,
              -- Hook up a new command to an existing dap function
              ['.restart'] = dap.restart,
            },
          }

        <


repl.toggle({winopts}, {wincmd})                             *dap.repl.toggle()*
        Opens the REPL if it is closed, otherwise closes it.

        See |dap.repl.open| for a description of the argument.


repl.close()                                                  *dap.repl.close()*
        Closes the REPL if it is open.


repl.execute({text})                                        *dap.repl.execute()*
        Add and execute text as if entered directly


set_log_level(level)                                       *dap.set_log_level()*
        Sets the log level. Defaults to `INFO`  >

            :lua require('dap').set_log_level('TRACE')
<

        Available log levels:

          TRACE
          DEBUG
          INFO
          WARN
          ERROR

        The log file is in the |stdpath| `cache` folder.
        To print the location:  >

            :lua print(vim.fn.stdpath('cache'))
<
        The filename is `dap.log`


session()                                                        *dap.session()*
        Returns the currently focused session or nil if no session exists or
        has focus.

        See |dap-session| for a description of a session object.

sessions()                                                      *dap.sessions()*
        Returns a table with the active top-level debug sessions.
        The keys are session ids and the values are the `Session` instances.

status()                                                          *dap.status()*
        Returns the status of the current debug session as text
        If no debug session is active the result is empty.

        This is intended to be used within the statusline with an expression
        like `%{luaeval("require'dap'.status()")}`. See |'statusline'| for
        more information.

        You may also want to redraw the statusline whenever the status of the
        debug session changes, for that you can setup an autocmd like this:

>lua
            api.nvim_create_autocmd("User", {
              pattern = "DapProgressUpdate",
              command = "redrawstatus"
            })
<

disconnect(opts, cb)                                          *dap.disconnect()*

        disconnect asks the debug adapter to disconnect from the debuggee and
        to terminate the debug adapter.

        The client session may remain open if the debug adapter does not
        terminate. To ensure the session gets closed, also call |dap.close()|.

        Requires an active session.

        Parameters: ~
            {opts}    Table with options for the disconnect request.
                      Defaults to `{ restart = false, terminateDebuggee = null }`

            {cb}      Callback that is invoked once the session
                      disconnected or immediately if no session is active.


close()                                                            *dap.close()*
        Closes the current session.

        This does NOT terminate the debug adapter or debugee.
        You usually want to use either |dap.terminate()| or |dap.disconnect()|
        instead.


launch({adapter}, {config})                                       *dap.launch()*
        Launch a new debug adapter and then initialize it with the given
        |dap-configuration|

        You typically do not want to call this directly but use
        |dap.continue()| or |dap.run()|

        Parameters: ~
            {adapter}   `Adapter` to launch, see |dap-adapter|, the `type` is
                        not required in this case.
            {config}    |dap-configuration|


attach({adapter}, {config})                                       *dap.attach()*
        Attach to a running debug adapter and then initialize it with the
        given |dap-configuration|

        You typically do not want to call this directly but use
        |dap.continue()| or |dap.run()|



==============================================================================
WIDGET API                                                    *dap-widgets*


Warning: API is experimental and subject to change.


The UI of nvim-dap is by default minimal and noninvasive, but it provides
widget primitives that can be used to build and customize a UI.

Some examples:


View the current scopes in a sidebar:

>lua
  local widgets = require('dap.ui.widgets')
  local my_sidebar = widgets.sidebar(widgets.scopes)
  my_sidebar.open()
<

View the current frames in a sidebar:

>lua
  local widgets = require('dap.ui.widgets')
  local my_sidebar = widgets.sidebar(widgets.frames)
  my_sidebar.open()
<


View the current scopes in a centered floating window:

>lua
  local widgets = require('dap.ui.widgets')
  widgets.centered_float(widgets.scopes)
<


View the value for the expression under the cursor in a floating window:

>lua
  require('dap.ui.widgets').hover()
<


The widgets may have the following custom mappings enabled:

- `<CR>` to expand or collapse an entry
- `a` to show a menu with available actions


Available widgets entities:

- sessions
- scopes
- frames
- expression
- threads


Available widget builder functions:

- sidebar({widget}, {winopts}, {wincmd})
    Creates a view for a sidebar. You must call `open` on the result to open the window.

    See |dap.repl.open()| for a description of `winopts` and `wincmd`.

- cursor_float({widget}, {winopts})
    Opens the contents of the widget in a floating window anchored at the cursor.

- centered_float({widget}, {winopts})
    Opens the contents of the widget in a centered floating window.

- hover({expr}, {winopts})
    Evaluates the expression and displays the result in a floating window.

    {expr} defaults to `<cexpr>`.
    It can be either a string as described in |expand()| or a function that
    should return the variable or expression that should be evaluated.

- preview({expr}, {opts})
    Like hover but uses the preview window

    {opts} optional table with:

      - listener?: string[]
          Names of commands or events which trigger an update of the view.
          Defaults to none; freezing the value.

          See |dap-extensions| for information about available commands and
          events and the listener system.

All widget builder functions return a `view`. A view has the following methods:

- open()
- close()
- toggle()


You could also customize the buffer and window creation using a low-level builder:

>lua
  local widgets = require('dap.ui.widgets')
  widgets.builder(widgets.scopes)
    .new_buf(function_that_creates_and_returns_a_buffer)
    .new_win(function_that_creates_and_returns_a_window)
    .build()
<

==============================================================================
EXTENSIONS API                                                *dap-extensions*

nvim-dap provides extension points for plugins:

- |dap-listeners|
- |dap-providers|


==============================================================================
LISTENERS EXTENSIONS API                                       *dap-listeners*


nvim-dap supports subscribing and listening to all responses or events that a
debug adapter might send to nvim-dap.

There are two tables for that:

- `dap.listeners.before`
- `dap.listeners.after`

Both `before` and `after` are nested tables where the first key is
`event_<event>` for events or `<command>` for request responses. The second key
is an arbitrary key used to identify the subscription. The second key must be
unique. If you're developing a plugin, using the plugin name might be a good
option to avoid conflicts with others.

`<event>` is the name of the event.
`<command>` is the name of the command that got executed and resulted in the
response.

Please refer to the Debug Adapter Protocol specification to get a list of all
events or requests and their response formats:

- https://microsoft.github.io/debug-adapter-protocol/specification#Requests
- https://microsoft.github.io/debug-adapter-protocol/specification#Events

For example:

>lua
  local dap = require('dap')
  dap.listeners.before['event_terminated']['my-plugin'] = function(session, body)
    print('Session terminated', vim.inspect(session), vim.inspect(body))
  end
<

Listeners registered in the `before` table are called *before* the internal `nvim-dap` handlers are called. The listeners registered in the `after` table are called *after* internal `nvim-dap` handlers.


For commands (request responses), the listeners are called with five arguments:

1. The session
2. An error: A optional table with `message` and `body` properties.
3. A table with the response. `nil` if an error occurred.
4. The original payload of the request
5. The sequence number for the request (also known as message ID)

For events, the listeners are called with two arguments:

1. The session
2. The event payload


Both command and event listeners can return a boolean `true` to remove the
registered listener.

==============================================================================
BUILT-IN CLIENT EVENTS                                     *dap-listeners-ext*

In addition to the debug adapter protocol messages, the `dap.listeners` also
provides hooks to listen on and react to synthethic events created by the
client.

Currently there are:

- `dap.listeners.on_config` (See |dap-listeners-on_config|)
- `dap.listeners.on_session` (See |dap-listeners-on_session|)

==============================================================================
ON_CONFIG LISTENER                                    *dap-listeners-on_config*


Plugins can pre-process the |dap-configuration| whenever a debug session
starts.

To do so, register a `on_config` hook in the `dap.listeners.on_config` table.

The key for the table is a `plugin-id`. Plugins should use their plugin name.
Do _not_ use the `dap.` namespace. It is reserved for nvim-dap itself.

The value for the table is a function that takes a |dap-configuration| as
parameter and must return a |dap-configuration|.

Before making modifications to the config you should copy it, to ensure you
don't make permanent changes to a configuration stored within
`dap.configurations.<filetype>` via mutations.

Example:
>lua
  local dap = require("dap")
  dap.listeners.on_config["dummy-noop"] = function(config)
    return vim.deepcopy(config)
  end
<
To support async operations, the on_config functions are called within a
coroutine.

This functionality should only be used by plugins that implement generic
functionality applicable for all or most configurations.
If you are writing a plugin that already owns an adapter definition, you
should prefer using the `enrich_config` function available in |dap-adapter|.
If you are not owning the adapter definition but the plugin's functionality is
still specific to a limited selection of adapters, please make sure you're not
messing with configurations used with adapters foreign to your plugin.

==============================================================================
ON_SESSION LISTENER                                  *dap-listeners-on_session*

`on_session` listeners can be used to listen to session changes. Opposed to
the initialize and terminated events from debug adapters - to which you
could listen to using |dap-listeners| - `on_session` listeners are also called
whenever the focused session changes. The full list of triggers is:

- New sessions
- Focused session changes
- Last remaining session finishes

A listener is a function with two parameters, the old session and the new
session.

To register a `on_session` listener, add an entry to the
`dap.listeners.on_session` table. For example:
>lua
  local dap = require("dap")
  dap.listeners.on_session["dummy-noop"] = function(old, new)
    if new then
      vim.print("New session: ", new.id)
    end
  end
<
As with other listeners, `dummy-noop` in the example above is an arbitrary
name. Plugins should namespace those with their name to avoid conflicts with
others.

==============================================================================
PROVIDERS EXTENSIONS API                                       *dap-providers*

==============================================================================
CONFIG PROVIDERS EXTENSIONS API                         *dap-providers-configs*

If a user starts a debug session via |dap.continue()|, nvim-dap looks for
a suitable configuration (|dap-configuration|) to use.

To do so it uses so called configuration providers registered in a
`dap.providers.configs` table.

Plugins can extend this table with additional config providers.

There are two providers built-in:

- `dap.global` - looks for configuration entries in
  `dap.configurations.<filetype>`

- `dap.launch.json` - looks for configuration entries in a
  `.vscode/launch.json` file.


The key for the table is a `plugin-id`. Plugins should use their plugin name.
Do _not_ use the `dap.` namespace. It is reserved for nvim-dap itself.

The value for the table is a function that takes a buffer number as parameter
and must return |dap-configuration| entries as list.

An example:

>lua
  local dap = require("dap")
  dap.providers.configs["mydummy_provider"] = function(bufnr)
    return {
      {
        name = "This config always shows up",
        type = "gdb",
        request = "launch",
        program = "/usr/bin/zig",
        args = {"run", "${file}"},
        cwd = "${workspaceFolder}",
      },
    }
  end
<

To support async operations, the config providers functions are called
within a coroutine.

==============================================================================
UTILS API                                                          *dap-utils*


Lua module: dap.utils

pick_process({opts})                                    *dap.utils.pick_process*
    Show a prompt to select a process pid
    Requires `ps ah -U $USER` on Linux/Mac and `tasklist /nh /fo csv` on windows.


    Parameters:
      {opts}  optional table with the following properties:

                - filter string|fun:
                    A lua pattern or function to filter the processes.
                    If a function the parameter is a table with
                    {pid: integer, name: string}
                    and it must return a boolean.
                    Matches are included.

    >lua
    require("dap.utils").pick_process({ filter = "sway" })
<
    >lua
    require("dap.utils").pick_process({
      filter = function(proc) return vim.endswith(proc.name, "sway") end
    })
<


pick_file({opts})                                         *dap.utils.pick_file*
    Show a prompt to select a file.
    Returns the path to the selected file.
    Requires nvim 0.10+ or a `find` executable

    Parameters:
      {opts} optional table with:

              - filter? string|fun: A |lua-pattern| or a function to filter the
                files.
                If a function the parameter is a string and it must return a
                boolean. Matches are included.

              - executables? boolean: Show only executables. Defaults
                to true

              - path? string: Path to search for files.
                              Defaults to the current working directory.

    >lua
    require("dap.utils").pick_file({ filter = ".*%.py", executables = false })
    require("dap.utils").pick_file({
      executables = false,
      filter = function(filepath)
        return vim.endswith(filepath, ".py")
      end,
    })
<

splitstr({str})                                           *dap.utils.splitstr*

    Split an argument string on whitespace into a list, except if the
    whitespace is contained within single or double quotes.

    Parameters:
      {str} The string to split

    >lua
    require("dap.utils").splitstr("Hello world")
    -- result: {"Hello", "world"}

    require("dap.utils").splitstr("Keeps 'a quoted string' intact")
    -- result: {"Keeps", "a quoted string", "intact"}
<

==============================================================================
DAP Session                                                        *dap-session*

nvim-dap creates a session object per debug session. You can either get the current
session via |dap.session()|, or get access to one via a listener (|dap-extensions|).

The session object is a low level primitive, used to interact with the debug
session. This is not indented for regular debug-client users, but rather for
extension authors, or power users.

The session contains methods - functions where the first parameter is the
session itself. To call them, you can use the method call syntax:
`obj:function_name()`, instead of `obj.function_name(obj)`.
See |lua-function|.


request({command}, {arguments}, {callback})             *dap-session:request()*

    Send a request to the debug adapter.
    See the requests section in https://microsoft.github.io/debug-adapter-protocol/specification
    for a list of supported payloads.

    Parameters:
      {command} string      The command to execute
      {arguments} any|nil   Arguments
      {callback} function   Callback called with two parameters: err and result.

    For example, to make a `evaluate` request, you'd use:
>lua
      local session = assert(require("dap").session(), "has active session")
      local arguments = {
        expression = "1 + 2"
      }
      ---@param err dap.ErrorResponse
      ---@param result dap.EvaluateResponse
      local function on_result(err, result)
        vim.print(err or "No error")
        vim.print(result or "No result")
      end
      session:request("evaluate", arguments, on_result)
<

    The method is coroutine aware. If it is running inside a coroutine you can
    omit the callback and it will default to resume the coroutine with the
    result.

    An example:

>lua
      local session = assert(require("dap").session(), "has active session")
      local arguments = {
        expression = "1 + 2"
      }
      coroutine.wrap(function()
        local err, result = session:request("evaluate", arguments)
        vim.print(err or "No error")
        vim.print(result or "No result")
      end)()
<

    This is convenient if you want to make multiple requests as it helps
    prevent callback nesting.

    Note that `coroutine.wrap` doesn't propagate errors but you could setup
    error handling via |xpcall()|


vim:ft=help
```

## File: `lua/dap.lua`
```
local api = vim.api
local M = {}

---@diagnostic disable-next-line: deprecated
local islist = vim.islist or vim.tbl_islist

---@type table<number, dap.Session>
local sessions = {}

---@type dap.Session|nil
local session = nil
local last_run = nil

---@type dap.log.Log?
local _log = nil


-- lazy import other modules to have a lower startup footprint
local lazy = setmetatable({
  async = nil, --- @module "dap.async"
  utils = nil, --- @module "dap.utils"
  progress = nil, --- @module "dap.progress"
  ui = nil, --- @module "dap.ui"
  breakpoints = nil, --- @module "dap.breakpoints"
  }, {
  __index = function(_, key)
    return require('dap.' .. key)
  end
})


---@return dap.log.Log
local function log()
  if not _log then
    _log = require('dap.log').create_logger('dap.log')
  end
  return _log
end

local function notify(...)
  lazy.utils.notify(...)
end

--- Sentinel value; signals an operation should be aborted.
---@class dap.Abort
M.ABORT = {}

M.status = function()
  return lazy.progress.status()
end

--- @module "dap.repl"
M.repl = setmetatable({}, {
  __index = function(_, key)
    return require('dap.repl')[key]
  end
})

---@alias dap.RequestListener<T, U> fun(session: dap.Session, err: dap.ErrorResponse?, response: T, args: U, seq: number):boolean?

---@alias dap.EventListener<T> fun(session: dap.Session, body: T):boolean?

---@class dap.listeners
---@field event_breakpoint table<string, dap.EventListener<dap.BreakpointEvent>>
---@field event_capabilities table<string, dap.EventListener<any>>
---@field event_continued table<string, dap.EventListener<dap.ContinuedEvent>>
---@field event_exited table<string, dap.EventListener<any>>
---@field event_initialized table<string, dap.EventListener<dap.InitializedEvent>>
---@field event_invalidated table<string, dap.EventListener<any>>
---@field event_loadedSource table<string, dap.EventListener<any>>
---@field event_memory table<string, dap.EventListener<any>>
---@field event_module table<string, dap.EventListener<any>>
---@field event_output table<string, dap.EventListener<dap.OutputEvent>>
---@field event_process table<string, dap.EventListener<any>>
---@field event_progressEnd table<string, dap.EventListener<dap.ProgressEndEvent>>
---@field event_progressStart table<string, dap.EventListener<dap.ProgressStartEvent>>
---@field event_progressUpdate table<string, dap.EventListener<dap.ProgressUpdateEvent>>
---@field event_stopped table<string, dap.EventListener<dap.StoppedEvent>>
---@field event_terminated table<string, dap.EventListener<dap.TerminatedEvent>>
---@field event_thread table<string, dap.EventListener<dap.ThreadEvent>>
---@field attach table<string, dap.RequestListener>
---@field breakpointLocations table<string, dap.RequestListener>
---@field completions table<string, dap.RequestListener<dap.CompletionsResponse, dap.CompletionsArguments>>
---@field configurationDone table<string, dap.RequestListener>
---@field continue table<string, dap.RequestListener>
---@field dataBreakpointInfo table<string, dap.RequestListener>
---@field disassemble table<string, dap.RequestListener>
---@field disconnect table<string, dap.RequestListener<any, dap.DisconnectArguments>>
---@field evaluate table<string, dap.RequestListener<dap.EvaluateResponse, dap.EvaluateArguments>>
---@field exceptionInfo table<string, dap.RequestListener>
---@field goto table<string, dap.RequestListener>
---@field gotoTargets table<string, dap.RequestListener>
---@field initialize table<string, dap.RequestListener<dap.Capabilities?, dap.InitializeRequestArguments>>
---@field launch table<string, dap.RequestListener>
---@field loadedSources table<string, dap.RequestListener>
---@field modules table<string, dap.RequestListener>
---@field next table<string, dap.RequestListener>
---@field pause table<string, dap.RequestListener>
---@field readMemory table<string, dap.RequestListener>
---@field restart table<string, dap.RequestListener>
---@field restartFrame table<string, dap.RequestListener>
---@field reverseContinue table<string, dap.RequestListener>
---@field scopes table<string, dap.RequestListener>
---@field setBreakpoints table<string, dap.RequestListener>
---@field setDataBreakpoints table<string, dap.RequestListener>
---@field setExceptionBreakpoints table<string, dap.RequestListener>
---@field setExpression table<string, dap.RequestListener>
---@field setFunctionBreakpoints table<string, dap.RequestListener>
---@field setInstructionBreakpoints table<string, dap.RequestListener>
---@field setVariable table<string, dap.RequestListener>
---@field source table<string, dap.RequestListener>
---@field stackTrace table<string, dap.RequestListener>
---@field stepBack table<string, dap.RequestListener>
---@field stepIn table<string, dap.RequestListener>
---@field stepInTargets table<string, dap.RequestListener>
---@field stepOut table<string, dap.RequestListener>
---@field terminate table<string, dap.RequestListener>
---@field terminateThreads table<string, dap.RequestListener>
---@field threads table<string, dap.RequestListener>
---@field variables table<string, dap.RequestListener<dap.VariableResponse, dap.VariablesArguments>>
---@field writeMemory table<string, dap.RequestListener>


M.listeners = {
  ---@type dap.listeners
  before = setmetatable({}, {
    __index = function(tbl, key)
      rawset(tbl, key, {})
      return rawget(tbl, key)
    end
  }),
  ---@type dap.listeners
  after = setmetatable({}, {
    __index = function(tbl, key)
      rawset(tbl, key, {})
      return rawget(tbl, key)
    end
  }),

  ---@type table<string, fun(config: dap.Configuration):dap.Configuration>
  on_config = {},

  ---@type table<string, fun(old: dap.Session?, new: dap.Session?)>
  on_session = {}
}


M.listeners.after.event_stopped['dap.sessions'] = function(s)
  local lsession = session
  if not lsession or not lsession.stopped_thread_id then
    M.set_session(s)
  end
end


local function from_fallback(_, key)
  return M.defaults.fallback[key]
end
M.defaults = setmetatable(
  {
    fallback = {
      exception_breakpoints = 'default',
      ---@type "statement"|"line"|"instruction"
      stepping_granularity = 'statement',

      ---@type string|fun(config: dap.Configuration):(integer, integer?)
      terminal_win_cmd = 'belowright new',
      focus_terminal = false,
      auto_continue_if_many_stopped = true,

      ---@type string|fun(bufnr: integer, line: integer, column: integer):nil|nil
      switchbuf = nil,

      ---@type nil|fun(session: dap.Session, output: dap.OutputEvent)
      on_output = nil,
    },
  },
  {
    __index = function(tbl, key)
      tbl[key] = {} -- call __newindex to add metatable to child
      return rawget(tbl, key)
    end,
    __newindex = function(tbl, key)
      rawset(tbl, key, setmetatable({}, {
        __index = from_fallback
      }))
    end
  }
)


local DAP_QUICKFIX_TITLE = "DAP Breakpoints"
local DAP_QUICKFIX_CONTEXT = DAP_QUICKFIX_TITLE

---@class dap.Adapter
---@field type string
---@field id string|nil
---@field options nil|dap.Adapter.options
---@field enrich_config? fun(config: dap.Configuration, on_config: fun(config: dap.Configuration))
---@field reverse_request_handlers? table<string, fun(session: dap.Session, request: dap.Request)>

---@class dap.Adapter.options
---@field initialize_timeout_sec nil|number
---@field disconnect_timeout_sec nil|number
---@field source_filetype nil|string

---@class dap.ExecutableAdapter : dap.Adapter
---@field type "executable"
---@field command string
---@field args string[]
---@field options nil|dap.ExecutableAdapter.options

---@class dap.ExecutableAdapter.options : dap.Adapter.options
---@field env nil|table<string, string>
---@field cwd nil|string
---@field detached nil|boolean

---@class ServerOptions : dap.Adapter.options
---@field max_retries nil|number

---@class dap.ServerAdapter : dap.Adapter
---@field type "server"
---@field host string|nil
---@field port integer|"${port}"
---@field executable nil|dap.ServerAdapterExecutable
---@field options nil|ServerOptions


---@class dap.PipeAdapter.options
---@field timeout? integer max amount of time in ms to wait between spawning the executable and connecting. This gives the executable time to create the pipe. Defaults to 5000

---@class dap.PipeAdapter : dap.Adapter
---@field type "pipe"
---@field pipe string absolute path to the pipe or ${pipe} to use random tmp path
---@field executable? dap.ServerAdapterExecutable
---@field options? dap.PipeAdapter.options

---@class dap.ServerAdapterExecutable
---@field command string
---@field args nil|string[]
---@field cwd nil|string
---@field detached nil|boolean


---@alias dap.AdapterFactory fun(callback: fun(adapter: dap.Adapter), config: dap.Configuration, parent?: dap.Session)

--- Adapter definitions. See `:help dap-adapter` for more help
---
--- An example:
---
--- ```
--- require('dap').adapter.debugpy = {
---   {
---       type = "executable"
---       command = "/usr/bin/python",
---       args = {"-m", "debugpy.adapter"},
---   },
--- }
--- ```
---@type table<string, dap.Adapter|dap.AdapterFactory>
M.adapters = {}


---@class dap.Configuration
---@field type string
---@field request "launch"|"attach"
---@field name string
---@field [string] any


--- Configurations per adapter. See `:help dap-configuration` for more help.
---
--- An example:
---
--- ```
--- require('dap').configurations.python = {
---   {
---       name = "My configuration",
---       type = "debugpy", -- references an entry in dap.adapters
---       request = "launch",
---       -- + Other debug adapter specific configuration options
---   },
--- }
--- ```
---@type table<string, dap.Configuration[]>
M.configurations = {}

local providers = {
  ---@type table<string, fun(bufnr: integer): dap.Configuration[]>
  configs = {},
}
do
  local providers_mt = {
    __newindex = function()
      error("Cannot add item to dap.providers")
    end,
  }
  M.providers = setmetatable(providers, providers_mt)
end


providers.configs["dap.global"] = function(bufnr)
  local filetype = vim.b["dap-srcft"] or vim.bo[bufnr].filetype
  local configurations = M.configurations[filetype] or {}
  assert(
    islist(configurations),
    string.format(
      '`dap.configurations.%s` must be a list of configurations, got %s',
      filetype,
      vim.inspect(configurations)
    )
  )
  return configurations
end

providers.configs["dap.launch.json"] = function()
  local ok, configs = pcall(require("dap.ext.vscode").getconfigs)
  if not ok then
    local msg = "Can't get configurations from launch.json:\n%s" .. configs
    vim.notify_once(msg, vim.log.levels.WARN, {title = "DAP"})
    return {}
  end
  return configs
end

do
  local function eval_option(option)
    if type(option) == 'function' then
      option = option()
    end
    if type(option) == "thread" then
      assert(coroutine.status(option) == "suspended", "If option is a thread it must be suspended")
      local co = coroutine.running()
      -- Schedule ensures `coroutine.resume` happens _after_ coroutine.yield
      -- This is necessary in case the option coroutine is synchronous and
      -- gives back control immediately
      vim.schedule(function()
        coroutine.resume(option, co)
      end)
      option = coroutine.yield()
    end
    -- Users could resume coroutine from luv threads which would break subsequent logic
    -- Schedule back onto main thread if this is the case.
    if vim.in_fast_event() then
      local co = coroutine.running()
      vim.schedule(function()
        coroutine.resume(co)
      end)
      coroutine.yield()
    end
    return option
  end

  local var_placeholders_once = {
    ['${command:pickProcess}'] = lazy.utils.pick_process,
    ['${command:pickFile}'] = lazy.utils.pick_file,
  }

  local var_placeholders = {
    ['${file}'] = function(_)
      return vim.fn.expand("%:p")
    end,
    ['${fileBasename}'] = function(_)
      return vim.fn.expand("%:t")
    end,
    ['${fileBasenameNoExtension}'] = function(_)
      return vim.fn.fnamemodify(vim.fn.expand("%:t"), ":r")
    end,
    ['${fileDirname}'] = function(_)
      return vim.fn.expand("%:p:h")
    end,
    ['${fileExtname}'] = function(_)
      return vim.fn.expand("%:e")
    end,
    ['${relativeFile}'] = function(_)
      return vim.fn.expand("%:.")
    end,
    ['${relativeFileDirname}'] = function(_)
      return vim.fn.fnamemodify(vim.fn.expand("%:.:h"), ":r")
    end,
    ['${fileDirnameBasename}'] = function(_)
      return vim.fn.fnamemodify(vim.fn.expand("%:p:h"), ":t")
    end,
    ['${workspaceFolder}'] = function(_)
      return vim.fn.getcwd()
    end,
    ['${workspaceFolderBasename}'] = function(_)
      return vim.fn.fnamemodify(vim.fn.getcwd(), ":t")
    end,
    ['${env:([%w_]+)}'] = function(match)
      return os.getenv(match) or ''
    end,
  }


  local function expand_config_variables(option)
    option = eval_option(option)
    if option == M.ABORT then
      return option
    end
    if type(option) == "table" then
      local mt = getmetatable(option)
      local result = {}
      for k, v in pairs(option) do
        result[expand_config_variables(k)] = expand_config_variables(v)
      end
      return setmetatable(result, mt)
    end
    if type(option) ~= "string" then
      return option
    end
    local ret = option
    for key, fn in pairs(var_placeholders) do
      ret = ret:gsub(key, fn)
    end
    for key, fn in pairs(var_placeholders_once) do
      if ret:find(key) then
        local val = eval_option(fn)
        ret = ret:gsub(key, val)
      end
    end
    return ret
  end

  M.listeners.on_config["dap.expand_variable"] = function(config)
    return vim.tbl_map(expand_config_variables, config)
  end
end


local signs = {
  DapBreakpoint = { text = "B", texthl = "SignColumn", linehl = "", numhl = "" },
  DapBreakpointCondition = { text = "C", texthl = "SignColumn", linehl = "", numhl = "" },
  DapBreakpointRejected = { text = 'R', texthl = "SignColumn", linehl = '', numhl = '' },
  DapLogPoint = { text = 'L', texthl = "SignColumn", linehl = '', numhl = '' },
  DapStopped = { text = '→', texthl = "SignColumn", linehl = 'debugPC', numhl = '' },
}

local function sign_try_define(name)
  local s = vim.fn.sign_getdefined(name)
  if vim.tbl_isempty(s) then
    local opts = signs[name]
    vim.fn.sign_define(name, opts)
  end
end

for name in pairs(signs) do
  sign_try_define(name)
end


---@param lsession dap.Session
local function add_reset_session_hook(lsession)
  lsession.on_close['dap.session'] = function(s)
    assert(s.id == lsession.id, "on_close must not be called with a foreign session")
    lazy.progress.report('Closed session: ' .. tostring(s.id))
    sessions[s.id] = nil
    M.set_session(nil)
  end
end

local adapter_types = {
  executable = true,
  server = true,
  pipe = true
}

---@param adapter dap.Adapter
---@param config dap.Configuration
---@param opts table
local function run_adapter(adapter, config, opts)
  local name = config.name or '[no name]'
  local valid_type = adapter_types[adapter.type]
  if not valid_type then
    local msg = string.format('Invalid adapter type %s, expected `executable`, `server` or `pipe`', adapter.type)
    notify(msg, vim.log.levels.ERROR)
    return
  end
  lazy.progress.report('Running: ' .. name)
  local lsession
  if adapter.type == 'executable' then
    ---@cast adapter dap.ExecutableAdapter
    local options = adapter.options or {}
    opts = vim.tbl_extend('keep', opts, {
      cwd = options.cwd,
      env = options.env
    })
    lsession = M.launch(adapter, config, opts)
  elseif adapter.type == 'server' then
    ---@cast adapter dap.ServerAdapter
    lsession = M.attach(adapter, config, opts)
  elseif adapter.type == "pipe" then
    ---@cast adapter dap.PipeAdapter
    lsession = require("dap.session").pipe(adapter, config, opts, function(err)
      if not err then
        lsession:initialize(config)
      end
    end)
  end
  if lsession then
    add_reset_session_hook(lsession)
    M.set_session(lsession)
  end
end


local function maybe_enrich_config_and_run(adapter, configuration, opts)
  assert(type(adapter) == 'table', 'adapter must be a table, not' .. vim.inspect(adapter))
  assert(
    adapter.type,
    'Adapter for ' .. configuration.type .. ' must have the `type` property set to `executable` or `server`'
  )
  if adapter.enrich_config then
    assert(
      type(adapter.enrich_config) == 'function',
      '`enrich_config` property of adapter must be a function: ' .. vim.inspect(adapter)
    )
    adapter.enrich_config(configuration, function(config)
      run_adapter(adapter, config, opts)
    end)
  else
    run_adapter(adapter, configuration, opts)
  end
end


local function select_config_and_run(opts)
  local bufnr = api.nvim_get_current_buf()
  local filetype = vim.bo[bufnr].filetype
  lazy.async.run(function()
    local all_configs = {}
    local provider_keys = vim.tbl_keys(providers.configs)
    table.sort(provider_keys)
    for _, provider in ipairs(provider_keys) do
      local config_provider = providers.configs[provider]
      local configs = config_provider(bufnr)
      if islist(configs) then
        vim.list_extend(all_configs, configs)
      else
        local msg = "Configuration provider %s must return a list of configurations. Got: %s"
        notify(msg:format(provider, vim.inspect(configs)), vim.log.levels.WARN)
      end
    end

    if #all_configs == 0 then
      local msg = 'No configuration found for `%s`. You need to add configs to `dap.configurations.%s` (See `:h dap-configuration`)'
      notify(string.format(msg, filetype, filetype), vim.log.levels.INFO)
      return
    end

    opts = opts or {}
    opts.filetype = opts.filetype or filetype
    lazy.ui.pick_if_many(
      all_configs,
      "Configuration: ",
      function(i) return i.name end,
      function(configuration)
        if configuration then
          M.run(configuration, opts)
        else
          notify('No configuration selected', vim.log.levels.INFO)
        end
      end
    )
  end)
end


--- Get the first stopped session.
--- If no session is stopped, it returns the active session or next in sessions.
---@return dap.Session|nil
local function first_stopped_session()
  if session and session.stopped_thread_id then
    return session
  end
  for _, s in pairs(sessions) do
    if s.stopped_thread_id then
      return s
    end
  end
  if session then
    return session
  end
  local _, s = next(sessions)
  return s
end


---@param config dap.Configuration
---@return dap.Configuration
local function prepare_config(config)
  local co, is_main = coroutine.running()
  assert(co and not is_main, "prepare_config must be running in coroutine")
  local mt = getmetatable(config)
  if mt and type(mt.__call) == "function" then
    config = config()
    assert(config and type(config) == "table", "config metatable __call must return a config table")
  end
  for _, on_config in pairs(M.listeners.on_config) do
    config = on_config(config)
  end
  return config
end


---@class dap.run.opts
---@field new? boolean force new session
---@field before? fun(config: dap.Configuration): dap.Configuration pre-process config


--- Start a debug session
---@param config dap.Configuration
---@param opts dap.run.opts?
function M.run(config, opts)
  assert(
    type(config) == 'table',
    'dap.run() must be called with a valid configuration, got ' .. vim.inspect(config))

  opts = opts or {}
  if session and (opts.new == false or (opts.new == nil and session.config.name == config.name)) then
    M.restart(config, opts)
    return
  end
  opts.filetype = opts.filetype or vim.bo.filetype
  opts.new = nil
  last_run = {
    config = config,
    opts = opts,
  }
  if opts.before then
    config = opts.before(config)
  end
  local trigger_run = function()
    config = prepare_config(config)
    for _, val in pairs(config) do
      if val == M.ABORT then
        notify("Run aborted", vim.log.levels.INFO)
        return
      end
    end
    local adapter = M.adapters[config.type]
    if type(adapter) == 'table' then
      lazy.progress.report('Starting adapter ' .. config.type)
      maybe_enrich_config_and_run(adapter, config, opts)
    elseif type(adapter) == 'function' then
      lazy.progress.report('Starting adapter ' .. config.type)
      adapter(
        function(resolved_adapter)
          maybe_enrich_config_and_run(resolved_adapter, config, opts)
        end,
        config
      )
    elseif adapter == nil then
      notify(string.format(
        'Config references missing adapter `%s`. Available are: %s',
        config.type,
        table.concat(vim.tbl_keys(M.adapters), ", ")
      ), vim.log.levels.ERROR)
    else
      notify(string.format(
          'Invalid adapter `%s` for config `%s`. Expected a table or function. '
            .. 'Read :help dap-adapter and define a valid adapter.',
          vim.inspect(adapter),
          config.type
        ),
        vim.log.levels.ERROR
      )
    end
  end
  lazy.async.run(trigger_run)
end


--- Run the last debug session again
function M.run_last()
  if last_run then
    M.run(last_run.config, last_run.opts)
  else
    notify('No configuration available to re-run', vim.log.levels.INFO)
  end
end

--- Step over the current line
---@param opts table|nil
function M.step_over(opts)
  M.set_session(first_stopped_session())
  if not session then
    return
  end
  session:_step('next', opts)
end


function M.focus_frame()
  if session then
    if session.current_frame then
      session:_frame_set(session.current_frame)
    else
      local w = require('dap.ui.widgets')
      w.centered_float(w.threads)
    end
  else
    notify('No active session', vim.log.levels.INFO)
  end
end


function M.restart_frame()
  if session then
    session:restart_frame()
  else
    notify('No active session', vim.log.levels.INFO)
  end
end


---@param opts? {askForTargets?: boolean, steppingGranularity?: dap.SteppingGranularity}
function M.step_into(opts)
  M.set_session(first_stopped_session())
  if not session then
    return
  end
  ---@type {[any]: any}
  opts = opts or {}
  local askForTargets = opts.askForTargets
  opts.askForTargets = nil
  if not (askForTargets and session.capabilities.supportsStepInTargetsRequest) then
    session:_step('stepIn', opts)
    return
  end

  session:request('stepInTargets', { frameId = session.current_frame.id }, function(err, response)
    if err then
      notify(
        'Error on step_into: ' .. tostring(err) .. ' (while requesting stepInTargets)',
        vim.log.levels.ERROR
      )
      return
    end

    if #response.targets == 0 then
      notify('No targets found. Trying regular step_into.', vim.log.levels.INFO)
      session:_step('stepIn', opts)
      return
    end

    lazy.ui.pick_if_many(
      response.targets,
      "Step into which function?",
      function(target) return target.label end,
      function(target)
        if not target or not target.id then
          notify('No target selected. No stepping.', vim.log.levels.INFO)
        else
          opts.targetId = target.id
          session:_step('stepIn', opts)
        end
      end)
  end)
end


function M.step_out(opts)
  M.set_session(first_stopped_session())
  if not session then
    return
  end
  session:_step('stepOut', opts)
end


function M.step_back(opts)
  M.set_session(first_stopped_session())
  if not session then
    return
  end
  if session.capabilities.supportsStepBack then
    session:_step('stepBack', opts)
  else
    notify('Debug Adapter does not support stepping backwards.', vim.log.levels.ERROR)
  end
end

function M.reverse_continue(opts)
  if not session then return end
  if session.capabilities.supportsStepBack then
    session:_step('reverseContinue', opts)
  else
    notify('Debug Adapter does not support stepping backwards.', vim.log.levels.ERROR)
  end
end


function M.pause(thread_id)
  if session then
    session:_pause(thread_id)
  end
end


function M.stop()
  notify('dap.stop() is deprecated. Call dap.close() instead', vim.log.levels.WARN)
  M.close()
end


---@param lsession dap.Session?
---@param opts dap.terminate.Opts?
local function terminate(lsession, opts)
  opts = opts or {}
  local on_done = opts.on_done or function() end
  if not lsession then
    notify('No active session')
    on_done()
    return
  end

  if lsession.closed then
    log():warn('User called terminate on already closed session that is still in use')
    sessions[lsession.id] = nil
    M.set_session(nil)
    on_done()
    return
  end
  local capabilities = lsession.capabilities or {}
  if capabilities.supportsTerminateRequest then
    capabilities.supportsTerminateRequest = false
    local args = opts.terminate_args or vim.empty_dict()
    local timeout_sec = (lsession.adapter.options or {}).disconnect_timeout_sec or 3
    local timeout_ms = timeout_sec * 1000
    lsession:request_with_timeout('terminate', args, timeout_ms, function(err)
      if err then
        log():warn(tostring(err))
      end
      if not lsession.closed then
        lsession:close()
      end
      notify('Session terminated')
      on_done()
    end)
  else
    local args = opts.disconnect_args or { terminateDebuggee = true }
    lsession:disconnect(args, on_done)
  end
end

---@class dap.terminate.Opts
---@field terminate_args dap.TerminateArguments?
---@field disconnect_args dap.DisconnectArguments?
---@field on_done function?
---@field hierarchy boolean? terminate full hierarchy. Defaults to false
---@field all boolean? terminate all root sessions. Can be combined with hierarchy. Defaults to false


---@param opts dap.terminate.Opts?
function M.terminate(opts, disconnect_opts, cb)
  opts = opts or {}
  -- old signature was:
  --- - terminate_opts dap.TerminateArguments?
  --- - disconnect_opts dap.DisconnectArguments?
  --- - cb fun()?
  ---@diagnostic disable-next-line: undefined-field
  if opts.restart ~= nil or disconnect_opts ~= nil or cb ~= nil then
    opts = {
      ---@diagnostic disable-next-line: assign-type-mismatch
      terminate_args = opts,
      disconnect_args = disconnect_opts,
      on_done = cb,
      hierarchy = false,
      all = false,
    }
  end

  local hierarchy = lazy.utils.if_nil(opts.hierarchy, false)
  local all = lazy.utils.if_nil(opts.all, false)

  ---@param s dap.Session
  local function rec_terminate(s)
    terminate(s, opts)
    if hierarchy then
      for _, child in pairs(s.children) do
        rec_terminate(child)
      end
    end
  end

  if all then
    for _, s in pairs(sessions) do
      rec_terminate(s)
    end
  else
    local lsession = session
    if not lsession then
      local _, s = next(sessions)
      if s then
        log():info("Terminate called without active session, switched to", s.id)
      end
      lsession = s
    end
    if not lsession then
      return
    end
    if hierarchy then
      while lsession.parent ~= nil do
        lsession = lsession.parent
        assert(lsession)
      end
    end
    rec_terminate(lsession)
  end
end


function M.close()
  if session then
    session:close()
    M.set_session(nil)
  end
end


function M.up()
  if session then
    session:_frame_delta(1)
  end
end


function M.down()
  if session then
    session:_frame_delta(-1)
  end
end


function M.goto_(line)
  if session then
    local source, col
    if not line then
      line, col = unpack(api.nvim_win_get_cursor(0))
      col = col + 1
      source = { path = vim.uri_from_bufnr(0) }
    end
    session:_goto(line, source, col)
  end
end


---@param config dap.Configuration?
---@param opts? dap.run.opts
function M.restart(config, opts)
  local lsession = session
  if not lsession then
    notify('No active session', vim.log.levels.INFO)
    return
  end
  config = config or lsession.config
  if lsession.capabilities.supportsRestartRequest then
    lazy.async.run(function()
      config = prepare_config(config)
      lsession:request('restart', { arguments = config }, function(err0, _)
        if err0 then
          notify('Error restarting debug adapter: ' .. tostring(err0), vim.log.levels.ERROR)
        else
          notify('Restarted debug adapter', vim.log.levels.INFO)
        end
      end)
    end)
  else
    local terminate_opts = {
      on_done = vim.schedule_wrap(function()
        local nopts = opts and vim.deepcopy(opts) or {}
        nopts.new = true
        M.run(config, nopts)
      end)
    }
    terminate(lsession, terminate_opts)
  end
end


---@param openqf boolean?
function M.list_breakpoints(openqf)
  local qf_list = lazy.breakpoints.to_qf_list(lazy.breakpoints.get())
  local current_qflist_title = vim.fn.getqflist({ title = 1 }).title
  local action = ' '
  if current_qflist_title == DAP_QUICKFIX_TITLE then
    action = 'r'
  end
  vim.fn.setqflist({}, action, {
    items = qf_list,
    context = { DAP_QUICKFIX_CONTEXT },
    title = DAP_QUICKFIX_TITLE
  })
  if openqf then
    if #qf_list == 0 then
      notify('No breakpoints set!', vim.log.levels.INFO)
    else
      api.nvim_command('copen')
    end
  end
end

---@param condition string?
---@param hit_condition string?
---@param log_message string?
function M.set_breakpoint(condition, hit_condition, log_message)
  M.toggle_breakpoint(condition, hit_condition, log_message, true)
end


---@param lsessions table<integer, dap.Session>
---@param fn fun(lsession: dap.Session)
local function broadcast(lsessions, fn)
  for _, lsession in pairs(lsessions) do
    fn(lsession)
    broadcast(lsession.children, fn)
  end
end


---@param condition string?
---@param hit_condition string?
---@param log_message string?
---@param replace_old boolean?
function M.toggle_breakpoint(condition, hit_condition, log_message, replace_old)
  assert(
    not condition or type(condition) == "string",
    "breakpoint condition must be a string. Got: " .. vim.inspect(condition)
  )
  assert(
    not hit_condition or type(hit_condition) == "string",
    "breakpoint hit-condition must be a string. Got: " .. vim.inspect(hit_condition)
  )
  assert(
    not log_message or type(log_message) == "string",
    "breakpoint log-message must be a string. Got: " .. vim.inspect(log_message)
  )
  lazy.breakpoints.toggle({
    condition = condition,
    hit_condition = hit_condition,
    log_message = log_message,
    replace = replace_old
  })
  local bufnr = api.nvim_get_current_buf()
  local bps = lazy.breakpoints.get(bufnr)
  broadcast(sessions, function(s)
    s:set_breakpoints(bps)
  end)
  if vim.fn.getqflist({context = DAP_QUICKFIX_CONTEXT}).context == DAP_QUICKFIX_CONTEXT then
    M.list_breakpoints(false)
  end
end


function M.clear_breakpoints()
  local bps = lazy.breakpoints.get()
  for bufnr, _ in pairs(bps) do
    bps[bufnr] = {}
  end
  lazy.breakpoints.clear()
  broadcast(sessions, function(lsession)
    lsession:set_breakpoints(bps)
  end)
end


-- setExceptionBreakpoints (https://microsoft.github.io/debug-adapter-protocol/specification#Requests_SetExceptionBreakpoints)
--- filters: string[]
--- exceptionOptions: exceptionOptions?: ExceptionOptions[] (https://microsoft.github.io/debug-adapter-protocol/specification#Types_ExceptionOptions)
function M.set_exception_breakpoints(filters, exceptionOptions)
  if session then
    session:set_exception_breakpoints(filters, exceptionOptions)
  else
    notify('Cannot set exception breakpoints: No active session!', vim.log.levels.INFO)
  end
end


function M.run_to_cursor()
  local lsession = session
  if not lsession then
    notify('Cannot use run_to_cursor without active session', vim.log.levels.INFO)
    return
  end
  if not lsession.stopped_thread_id then
    notify('run_to_cursor can only be used if stopped at a breakpoint', vim.log.levels.INFO)
    return
  end

  local bps_before = lazy.breakpoints.get()
  lazy.breakpoints.clear()
  local cur_bufnr = api.nvim_get_current_buf()
  local lnum = api.nvim_win_get_cursor(0)[1]
  lazy.breakpoints.set({}, cur_bufnr, lnum)

  local temp_bps = lazy.breakpoints.get(cur_bufnr)
  for bufnr, _ in pairs(bps_before) do
    if bufnr ~= cur_bufnr then
      temp_bps[bufnr] = {}
    end
  end

  if bps_before[cur_bufnr] == nil then
    bps_before[cur_bufnr] = {}
  end

  local function restore_breakpoints()
    M.listeners.before.event_stopped['dap.run_to_cursor'] = nil
    M.listeners.before.event_terminated['dap.run_to_cursor'] = nil
    lazy.breakpoints.clear()
    for buf, buf_bps in pairs(bps_before) do
      for _, bp in pairs(buf_bps) do
        local line = bp.line
        local opts = {
          condition = bp.condition,
          log_message = bp.logMessage,
          hit_condition = bp.hitCondition
        }
        lazy.breakpoints.set(opts, buf, line)
      end
    end
    lsession:set_breakpoints(bps_before, nil)
  end

  M.listeners.before.event_stopped['dap.run_to_cursor'] = restore_breakpoints
  M.listeners.before.event_terminated['dap.run_to_cursor'] = restore_breakpoints
  lsession:set_breakpoints(temp_bps, function()
    lsession:_step('continue')
  end)
end


---@param opts? {new?: boolean}
function M.continue(opts)
  if not session then
    M.set_session(first_stopped_session())
  end

  opts = opts or {}
  if not session or opts.new then
    select_config_and_run(opts)
  elseif session.stopped_thread_id then
    session:_step('continue')
  else
    local other_stopped_session = first_stopped_session()
    if other_stopped_session and other_stopped_session.stopped_thread_id then
      other_stopped_session:_step('continue')
      return
    end
    local stopped_threads = vim.tbl_filter(function(t) return t.stopped end, session.threads)
    local prompt
    if not session.initialized then
      prompt = "Session still initializing> "
    elseif next(stopped_threads) then
      prompt = "Not focused on any stopped Thread> "
    else
      prompt = "Session active, but not stopped at breakpoint> "
    end
    local choices = {
      {
        label = "Terminate session",
        action = M.terminate
      },
      {
        label = "Pause a thread",
        action = M.pause
      },
      {
        label = "Restart session",
        action = M.restart,
      },
      {
        label = "Disconnect (terminate = true)",
        action = function()
          M.disconnect({ terminateDebuggee = true })
        end
      },
      {
        label = "Disconnect (terminate = false)",
        action = function()
          M.disconnect({ terminateDebuggee = false })
        end,
      },
      {
        label = "Start additional session",
        action = function()
          M.continue({ new = true })
        end,
      },
      {
        label = "Do nothing",
        action = function() end,
      },
    }
    if next(stopped_threads) then
      table.insert(choices, 1, {
        label = "Resume stopped thread",
        action = vim.schedule_wrap(function()
          lazy.ui.pick_if_many(
            stopped_threads,
            'Thread to resume> ',
            function(t) return t.name or t.id end,
            function(choice)
              if choice then
                session.stopped_thread_id = choice.id
                session:_step('continue')
              end
            end
          )
        end),
      })
    end
    lazy.ui.pick_one(choices, prompt, function(x) return x.label end, function(choice)
      if choice then
        choice.action()
      end
    end)
  end
end


--- Disconnects an active session
function M.disconnect(opts, cb)
  if session then
    session:disconnect(opts, cb)
  else
    notify('No active session. Doing nothing.', vim.log.levels.INFO)
    if cb then
      cb()
    end
  end
end


---@private
--- Connect to a debug adapter via TCP
---@param adapter dap.ServerAdapter
---@param config dap.Configuration
---@param opts table
function M.attach(adapter, config, opts)
  if not config.request then
    notify('Config needs the `request` property which must be one of `attach` or `launch`', vim.log.levels.ERROR)
    return
  end
  assert(adapter.port, 'Adapter used with attach must have a port property')
  local s
  s = require('dap.session').connect(adapter, config, opts, function(err)
    if err then
      notify(
        string.format("Couldn't connect to %s:%s: %s", adapter.host or '127.0.0.1', adapter.port, err),
        vim.log.levels.ERROR
      )
    else
      if s then
        s:initialize(config)
      end
    end
  end)
  return s
end


---@private
--- Launch an executable debug adapter and initialize a session
---
---@param adapter dap.ExecutableAdapter
---@param config dap.Configuration
---@param opts table
function M.launch(adapter, config, opts)
  local s = require('dap.session').spawn(adapter, config, opts)
  if not s then
    return
  end
  s:initialize(config)
  return s
end


function M.set_log_level(level)
  require("dap.log").set_level(level)
end


--- Currently focused session
---@return dap.Session|nil
function M.session()
  return session
end


---@return table<number, dap.Session>
function M.sessions()
  return sessions
end


---@param new_session dap.Session|nil
function M.set_session(new_session)
  if session and new_session and session.id == new_session.id then
    return
  end
  local old_session = session
  if not new_session then
    local _, lsession = next(sessions)
    new_session = lsession
  end
  local msg = new_session and ("Running: " .. new_session.config.name) or ""
  lazy.progress.report(msg)
  if new_session and new_session.parent == nil then
    sessions[new_session.id] = new_session
  end
  session = new_session
  for _, on_session in pairs(M.listeners.on_session) do
    on_session(old_session, new_session)
  end
end


function M._tagfunc(_, flags, _)
  local lsession = session
  if not lsession then
    return vim.NIL
  end
  if not flags:match("c") then
    return vim.NIL
  end
  local ui = require("dap.ui")
  local buf = api.nvim_get_current_buf()
  local layer = ui.get_layer(buf)
  if not layer then
    return vim.NIL
  end
  local cursor = api.nvim_win_get_cursor(0)
  local lnum = cursor[1] - 1
  local lineinfo = layer.get(lnum)
  if not lineinfo or not lineinfo.item then
    return vim.NIL
  end
  ---@type dap.Variable|dap.EvaluateResponse
  local item = lineinfo.item
  local loc = item.valueLocationReference or item.declarationLocationReference
  if not loc then
    return vim.NIL
  end

  ---@type dap.ErrorResponse?
  local err
  ---@type dap.LocationsResponse?
  local result

  ---@type dap.LocationsArguments
  local args = {
    locationReference = loc
  }
  lsession:request("locations", args, function(e, r)
    err = e
    result = r
  end)
  vim.wait(2000, function() return err ~= nil or result ~= nil end)
  if result and result.source.path then
    local match = {
      name = item.name or item.result,
      filename = result.source.path,
      cmd = string.format([[/\%%%dl\%%%dc/]], result.line, result.column or 0)
    }
    return { match }
  end
  return {}
end


api.nvim_create_autocmd("ExitPre", {
  pattern = "*",
  group = api.nvim_create_augroup("dap.exit", { clear = true }),
  callback = function()
    ---@param s dap.Session
    local function close_session(s)
      s.adapter.options = {
        disconnect_timeout_sec = 0.1
      }
      if s.config.request == "attach" then
        s:disconnect({ terminateDebuggee = false })
      else
        terminate(s)
      end
    end
    for _, s in pairs(sessions) do
      close_session(s)
    end
    vim.wait(5000, function()
      ---@diagnostic disable-next-line: redundant-return-value
      return session == nil and next(sessions) == nil
    end)
    M.repl._exit()
    if _log then
      _log:close()
    end
  end
})


return M
```

## File: `lua/dap/_cmds.lua`
```
local api = vim.api
local M = {}
local mime_to_filetype = {
  ['text/javascript'] = 'javascript'
}


---@param args vim.api.keyset.create_user_command.command_args
function M.eval(args)
  local oldbuf = api.nvim_get_current_buf()
  local name = string.format("dap-eval://%s", vim.bo[oldbuf].filetype)
  if args.smods.vertical then
    vim.cmd.vsplit({name})
  elseif args.smods.tab == 1 then
    vim.cmd.tabedit(name)
  else
    local size = math.max(5, math.floor(vim.o.lines * 1/5))
    vim.cmd.split({name, mods = args.smods, range = { size }})
  end
  local newbuf = api.nvim_get_current_buf()
  if args.range ~= 0 then
    local lines = api.nvim_buf_get_lines(oldbuf, args.line1 -1 , args.line2, true)
    local indent = math.huge
    for _, line in ipairs(lines) do
      indent = math.min(line:find("[^ ]") or math.huge, indent)
    end
    if indent ~= math.huge and indent > 0 then
      for i, line in ipairs(lines) do
        lines[i] = line:sub(indent)
      end
    end
    api.nvim_buf_set_lines(newbuf, 0, -1, true, lines)
    vim.bo[newbuf].modified = false
  end
  if args.bang then
    vim.cmd.w()
  end
end


---@param args vim.api.keyset.create_user_command.command_args
function M.new(args)
  local dap = require("dap")
  local fargs = args.fargs
  if not next(fargs) then
    dap.continue({ new = true })
    return
  end
  local bufnr = api.nvim_get_current_buf()
  require("dap.async").run(function()
    for _, get_configs in pairs(dap.providers.configs) do
      local configs = get_configs(bufnr)
      for _, config in ipairs(configs) do
        if vim.tbl_contains(fargs, config.name) then
          dap.run(config)
        end
      end
    end
  end)
end


---@param buf integer
function M.source(buf)
  local fname = api.nvim_buf_get_name(buf)
  local session_id, source_ref, source_path = fname:match("dap%-src://(%d+)/(%d+)/(.*)")
  session_id = tonumber(session_id)
  source_ref = tonumber(source_ref)
  local dap = require("dap")
  local session = dap.sessions()[session_id]
  if not session then
    return
  end
  local params = {
    source = {
      sourceReference = source_ref
    },
    sourceReference = source_ref
  }
  local response
  session:request("source", params, function (err, result)
    response = {err, result}
  end)
  vim.wait(5000, function() return response ~= nil end)
  local err = response[1]
  if err then
    require("dap.utils").notify(tostring(err), vim.log.levels.WARN)
    return
  end
  local result = response[2]
  api.nvim_buf_set_lines(buf, 0, -1, true, vim.split(result.content, "\n", { plain = true }))
  local adapter_options = session.adapter.options or {}
  local ft = mime_to_filetype[response.mimeType] or adapter_options.source_filetype
  if ft then
    vim.bo[buf].filetype = ft
  elseif source_path ~= "" and vim.filetype then
    local ok
    ok, ft = pcall(vim.filetype.match, { buf = buf, filename = source_path })
    if ok and ft then
      vim.bo[buf].filetype = ft
    end
  end
end


function M.new_complete()
  local bufnr = api.nvim_get_current_buf()
  local dap = require("dap")
  local candidates = {}
  local done = false
  require("dap.async").run(function()
    for _, get_configs in pairs(dap.providers.configs) do
      local configs = get_configs(bufnr)
      for _, config in ipairs(configs) do
        local name = config.name:gsub(" ", "\\ ")
        table.insert(candidates, name)
      end
    end
    done = true
  end)
  vim.wait(2000, function() return done == true end)
  return candidates
end


function M.bufread_eval()
  local bufnr = api.nvim_get_current_buf()
  local fname = api.nvim_buf_get_name(bufnr)
  vim.bo[bufnr].swapfile = false
  vim.bo[bufnr].buftype = "acwrite"
  vim.bo[bufnr].bufhidden = "wipe"
  local ft = fname:match("dap%-eval://(%w+)(.*)")
  if ft and ft ~= "" then
    vim.bo[bufnr].filetype = ft
  else
    local altbuf = vim.fn.bufnr("#", false)
    if altbuf then
      vim.bo[bufnr].filetype = vim.bo[altbuf].filetype
    end
  end
  api.nvim_create_autocmd("BufWriteCmd", {
    buffer = bufnr,
    callback = function(args)
      vim.bo[args.buf].modified = false
      local repl = require("dap.repl")
      local lines = api.nvim_buf_get_lines(args.buf, 0, -1, true)
      repl.execute(table.concat(lines, "\n"))
      repl.open()
    end,
  })
end


---@param args vim.api.keyset.create_autocmd.callback_args
function M.newlaunchjson(args)
  if vim.snippet then
    local text = [[{
    "\$schema": "https://raw.githubusercontent.com/mfussenegger/dapconfig-schema/master/dapconfig-schema.json",
    "version": "0.2.0",
    "configurations": [
        {
            "type": "${1:adaptername}",
            "request": "${2|launch,request|}",
            "name": "${3:run}"${0}
        }
    ]
}]]
    api.nvim_buf_call(args.buf, function()
      vim.snippet.expand(text)
    end)
  else
    local lines = {
      '{',
      '   "$schema": "https://raw.githubusercontent.com/mfussenegger/dapconfig-schema/master/dapconfig-schema.json",',
      '   "version": "0.2.0",',
      '   "configurations": [',
      '       {',
      '           "type": "<adapter-name>",',
      '           "request": "launch",',
      '           "name": "Launch"',
      '       }',
      '   ]',
      '}'
    }
    api.nvim_buf_set_lines(args.buf, 0, -1, true, lines)
  end
end


function M.yank_evalname()
  if vim.v.event.operator ~= "y" or vim.v.event.visual == true then
    return
  end
  local buf = api.nvim_get_current_buf()
  local layer = require("dap.ui").get_layer(buf)
  if not layer then
    return
  end
  local lnum = api.nvim_win_get_cursor(0)[1] - 1
  local item = (layer.get(lnum) or {}).item
  if item and item.evaluateName then
    vim.fn.setreg("e", item.evaluateName)
  end
end


function M.show_logs()
  local log = require("dap.log")
  log.create_logger("dap.log")
  for _, logger in pairs(log._loggers) do
    vim.cmd.tabnew(logger._path)
  end
end


return M
```

## File: `lua/dap/async.lua`
```
local M = {}

--- Run a function in a coroutine with error handling via vim.notify
---
--- If run is called within a coroutine, no new coroutine is created.
function M.run(fn)
  local co, is_main = coroutine.running()
  if co and not is_main then
    fn()
  else
    coroutine.wrap(function()
      xpcall(fn, function(err)
        local msg = debug.traceback(err, 2)
        require("dap.utils").notify(msg, vim.log.levels.ERROR)
      end)
    end)()
  end
end

return M
```

## File: `lua/dap/breakpoints.lua`
```
local api = vim.api
local non_empty = require('dap.utils').non_empty

---@class dap.bp
---@field buf integer
---@field line integer
---@field condition string?
---@field logMessage string?
---@field hitCondition string?
---@field state dap.Breakpoint?

---@type table<integer, table<integer, dap.bp>> buffer → sign id → bp
local bp_by_sign_by_buf = {}
local ns = 'dap_breakpoints'
local M = {}


---@param bufexpr? string|integer
---@return vim.fn.sign_getplaced.ret.item[]
local function get_breakpoint_signs(bufexpr)
  if bufexpr then
    return vim.fn.sign_getplaced(bufexpr, {group = ns})
  end
  local bufs_with_signs = vim.fn.sign_getplaced()
  local result = {}
  for _, buf_signs in ipairs(bufs_with_signs) do
    buf_signs = vim.fn.sign_getplaced(buf_signs.bufnr, {group = ns})[1]
    if #buf_signs.signs > 0 then
      table.insert(result, buf_signs)
    end
  end
  return result
end

---@param bp dap.bp
local function get_sign_name(bp)
  if bp.state and bp.state.verified == false then
    return 'DapBreakpointRejected'
  elseif non_empty(bp.condition) then
    return 'DapBreakpointCondition'
  elseif non_empty(bp.logMessage) then
    return 'DapLogPoint'
  else
    return 'DapBreakpoint'
  end
end


---@param breakpoint dap.Breakpoint
function M.update(breakpoint)
  assert(breakpoint.id, "To update a breakpoint it must have an id property")
  for _, bp_by_sign in pairs(bp_by_sign_by_buf) do
    for sign_id, bp in pairs(bp_by_sign) do
      if bp.state and bp.state.id == breakpoint.id then
        local verified_changed = bp.state.verified ~= breakpoint.verified
        bp.state.verified = breakpoint.verified
        bp.state.message = breakpoint.message
        if verified_changed then
          vim.fn.sign_place(
            sign_id,
            ns,
            get_sign_name(bp),
            bp.buf,
            { lnum = bp.line; priority = 21; }
          )
        end
        return
      end
    end
  end
end


---@param bufnr integer
---@param state dap.Breakpoint
function M.set_state(bufnr, state)
  local ok, placements = pcall(vim.fn.sign_getplaced, bufnr, { group = ns; lnum = state.line; })
  if not ok then
    return
  end
  local signs = (placements[1] or {}).signs
  if not signs or next(signs) == nil then
    return
  end
  for _, sign in pairs(signs) do
    local bp = bp_by_sign_by_buf[bufnr][sign.id]
    if bp then
      bp.state = state
    end
    if not state.verified then
      vim.fn.sign_place(
        sign.id,
        ns,
        'DapBreakpointRejected',
        bufnr,
        { lnum = state.line; priority = 21; }
      )
    end
  end
end


function M.remove(bufnr, lnum)
  local placements = vim.fn.sign_getplaced(bufnr, { group = ns; lnum = lnum; })
  local signs = placements[1].signs
  if signs and #signs > 0 then
    for _, sign in pairs(signs) do
      vim.fn.sign_unplace(ns, { buffer = bufnr; id = sign.id; })
      bp_by_sign_by_buf[bufnr][sign.id] = nil
    end
    return true
  else
    return false
  end
end

function M.remove_by_id(id)
  for _, bp_by_sign in pairs(bp_by_sign_by_buf) do
    for sign_id, bp in pairs(bp_by_sign) do
      if bp.state and bp.state.id == id then
        vim.fn.sign_unplace(ns, { buffer = bp.buf, id = sign_id, })
        bp_by_sign_by_buf[bp.buf][sign_id] = nil
        return
      end
    end
  end
end

function M.toggle(opts, bufnr, lnum)
  opts = opts or {}
  bufnr = bufnr or api.nvim_get_current_buf()
  lnum = lnum or api.nvim_win_get_cursor(0)[1]
  if M.remove(bufnr, lnum) and not opts.replace then
    return
  end
  local bp = { ---@type dap.bp
    buf = bufnr,
    line = lnum,
    condition = opts.condition,
    logMessage = opts.log_message,
    hitCondition = opts.hit_condition
  }
  local sign_name = get_sign_name(bp)
  local sign_id = vim.fn.sign_place(
    0,
    ns,
    sign_name,
    bufnr,
    { lnum = lnum; priority = 21; }
  )
  if sign_id ~= -1 then
    if not bp_by_sign_by_buf[bufnr] then
      bp_by_sign_by_buf[bufnr] = {}
    end
    bp_by_sign_by_buf[bufnr][sign_id] = bp
  end
end


function M.set(opts, bufnr, lnum)
  opts = opts or {}
  opts.replace = true
  M.toggle(opts, bufnr, lnum)
end


--- Returns all breakpoints grouped by bufnr
---@param bufexpr? integer|string
---@return table<integer, dap.bp>
function M.get(bufexpr)
  local signs = get_breakpoint_signs(bufexpr)
  if #signs == 0 then
    return {}
  end
  local result = {}
  for _, buf_bp_signs in pairs(signs) do
    local breakpoints = {}
    local bufnr = buf_bp_signs.bufnr
    result[bufnr] = breakpoints
    for _, bp in pairs(buf_bp_signs.signs) do
      local bp_entry = bp_by_sign_by_buf[bufnr][bp.id] or {}
      table.insert(breakpoints, {
        buf = bufnr,
        line = bp.lnum;
        condition = bp_entry.condition;
        hitCondition = bp_entry.hitCondition;
        logMessage = bp_entry.logMessage;
        state = bp_entry.state,
      })
    end
  end
  return result
end


function M.clear()
  vim.fn.sign_unplace(ns)
  bp_by_sign_by_buf = {}
end


do
  local function not_nil(x)
    return x ~= nil
  end

  function M.to_qf_list(breakpoints)
    local qf_list = {}
    for bufnr, buf_bps in pairs(breakpoints) do
      for _, bp in pairs(buf_bps) do
        local state = bp.state or {}
        local text_parts = {
          unpack(api.nvim_buf_get_lines(bufnr, bp.line - 1, bp.line, false), 1),
          state.verified == false and (state.message and 'Rejected: ' .. state.message or 'Rejected') or nil,
          non_empty(bp.logMessage) and "Log message: " .. bp.logMessage or nil,
          non_empty(bp.condition) and "Condition: " .. bp.condition or nil,
          non_empty(bp.hitCondition) and "Hit condition: " .. bp.hitCondition or nil,
        }
        local text = table.concat(vim.tbl_filter(not_nil, text_parts), ', ')
        table.insert(qf_list, {
          bufnr = bufnr,
          lnum = bp.line,
          col = 0,
          text = text,
        })
      end
    end
    return qf_list
  end
end


return M
```

## File: `lua/dap/entity.lua`
```
local utils = require('dap.utils')
local M = {}


local variable = {}
M.variable = variable

local types_to_hl_group = {
  boolean = "Boolean",
  str = "String",
  string = "String",
  int = "Number",
  long = "Number",
  number = "Number",
  double = "Float",
  float = "Float",
  nonetype = "Constant",
  ["function"] = "Function",
}


---@param var dap.Variable|dap.EvaluateResponse
function variable.get_key(var)
  return var.name or var.result
end


function variable.is_lazy(var)
  return (var.presentationHint or {}).lazy
end


---@alias dap.entity.hl [string, integer, integer][]


---@param var dap.Variable|dap.EvaluateResponse
---@result string, dap.entity.hl[]
function variable.render_parent(var)
  if var.name then
    return variable.render_child(var --[[@as dap.Variable]], 0)
  end
  local syntax_group = var.type and types_to_hl_group[var.type:lower()]
  if syntax_group then
    return var.result, {{syntax_group, 0, -1},}
  end
  return var.result
end

---@param var dap.Variable
---@param indent integer
---@result string, dap.entity.hl[]
function variable.render_child(var, indent)
  indent = indent or 0
  local hl_regions = {
    {'Identifier', indent, #var.name + indent + 1}
  }
  local prefix = string.rep(' ', indent) .. var.name .. ': '
  local syntax_group = var.type and types_to_hl_group[var.type:lower()]
  if syntax_group then
    table.insert(hl_regions, {syntax_group, #prefix, -1})
  end
  return prefix .. var.value, hl_regions
end

function variable.has_children(var)
  return (var.variables and #var.variables > 0) or var.variablesReference ~= 0
end

---@param var dap.Variable|dap.Scope
---@result dap.Variable[]
function variable.get_children(var)
  return var.variables or {}
end


---@param a dap.Variable
---@param b dap.Variable
local function cmp_vars(a, b)
  local num_a = string.match(a.name, '^%[?(%d+)%]?$')
  local num_b = string.match(b.name, '^%[?(%d+)%]?$')
  if num_a and num_b then
    return tonumber(num_a) < tonumber(num_b)
  else
    return a.name < b.name
  end
end


---@param var dap.Variable|dap.Scope
---@param cb fun(variables: dap.Variable[])
function variable.fetch_children(var, cb)
  local session = require('dap').session()
  if var.variables then
    cb(variable.get_children(var))
  elseif session and var.variablesReference > 0 then

    ---@param err? dap.ErrorResponse
    ---@param resp? dap.VariableResponse
    local function on_variables(err, resp)
      if err then
        utils.notify('Error fetching variables: ' .. err.message, vim.log.levels.ERROR)
      elseif resp then
        local variables = resp.variables
        local unloaded = #variables
        var.variables = variables

        if unloaded == 0 then
          cb(variables)
          return
        end

        local function countdown()
          unloaded = unloaded - 1
          if unloaded == 0 then
            cb(variables)
          end
        end

        table.sort(variables, cmp_vars)
        for i, v in ipairs(variables) do
          v.parent = var
          if variable.is_lazy(v) then
            variable.load_value(v, function(loaded_v)
              variables[i] = loaded_v
              countdown()
            end)
          else
            countdown()
          end
        end
      end
    end
    ---@type dap.VariablesArguments
    local params = { variablesReference = var.variablesReference }
    session:request('variables', params, on_variables)
  else
    cb({})
  end
end


function variable.load_value(var, cb)
  assert(variable.is_lazy(var), "Must not call load_value if not lazy")
  local session = require('dap').session()
  if not session then
    cb(var)
  else
    ---@type dap.VariablesArguments
    local params = { variablesReference = var.variablesReference }
    ---@param err? dap.ErrorResponse
    ---@param resp? dap.VariableResponse
    local function on_variables(err, resp)
      if err then
        utils.notify('Error fetching variable: ' .. err.message, vim.log.levels.ERROR)
      elseif resp then
        local new_var = resp.variables[1]
        -- keep using the old variable;
        -- it has parent references and the parent contains references to the child
        var.value = new_var.value
        var.presentationHint = new_var.presentationHint
        var.variablesReference = new_var.variablesReference
        var.namedVariables = new_var.namedVariables
        var.indexedVariables = new_var.indexedVariables
        cb(var)
      end
    end
    session:request('variables', params, on_variables)
  end
end


---@param item dap.Variable
local function set_variable(_, item, _, context)
  local session = require('dap').session()
  if not session then
    utils.notify('No active session, cannot set variable')
    return
  end
  if not session.current_frame then
    utils.notify('Session has no active frame, cannot set variable')
    return
  end
  local parent = item.parent
  if not parent then
    utils.notify(string.format(
      "Cannot set variable on %s, couldn't find its parent container",
      item.name
    ))
    return
  end
  local view = context.view
  if view and vim.bo.bufhidden == 'wipe' then
    view.close()
  end
  local value = vim.fn.input(string.format('New `%s` value: ', item.name))
  local params = {
    variablesReference = parent.variablesReference,
    name = item.name,
    value = value,
  }
  session:request('setVariable', params, function(err)
    if err then
      utils.notify('Error setting variable: ' .. err.message, vim.log.levels.WARN)
    else
      session:_request_scopes(session.current_frame)
    end
  end)
end


local function set_expression(_, item, _, context)
  local session = require('dap').session()
  if not session then
    utils.notify('No activate session, cannot set expression')
    return
  end
  local view = context.view
  if view and vim.bo.bufhidden == 'wipe' then
    view.close()
  end
  local value = vim.fn.input(string.format('New `%s` expression: ', item.name))
  local params = {
    expression = item.evaluateName,
    value = value,
    frameId = session.current_frame and session.current_frame.id
  }
  session:request('setExpression', params, function(err)
    if err then
      utils.notify('Error on setExpression: ' .. tostring(err), vim.log.levels.WARN)
    else
      session:_request_scopes(session.current_frame)
    end
  end)
end


---@param item dap.Variable
local function copy_evalname(_, item, _, _)
  vim.fn.setreg("", item.evaluateName)
end


variable.tree_spec = {
  get_key = variable.get_key,
  render_parent = variable.render_parent,
  render_child = variable.render_child,
  has_children = variable.has_children,
  get_children = variable.get_children,
  is_lazy = variable.is_lazy,
  load_value = variable.load_value,
  fetch_children = variable.fetch_children,
  compute_actions = function(info)
    local session = require('dap').session()
    if not session then
      return {}
    end
    local result = {}
    local capabilities = session.capabilities
    ---@type dap.Variable
    local item = info.item
    if item.evaluateName then
      table.insert(result, { label = "Copy as expression", fn = copy_evalname, })
    end
    if item.evaluateName and capabilities.supportsSetExpression then
      table.insert(result, { label = 'Set expression', fn = set_expression, })
    elseif capabilities.supportsSetVariable then
      table.insert(result, { label = 'Set variable', fn = set_variable, })
    end
    return result
  end
}


local scope = {}
M.scope = scope


function scope.render_parent(value)
  return value.name
end

scope.tree_spec = vim.tbl_extend('force', variable.tree_spec, {
  render_parent = scope.render_parent,
})


local frames = {}
M.frames = frames

function frames.render_item(frame)
  local session = require('dap').session()
  local line
  if session and frame.id == (session.current_frame or {}).id then
    line = '→ ' .. frame.name .. ':' .. frame.line
  else
    line = '  ' .. frame.name .. ':' .. frame.line
  end
  if frame.presentationHint == 'subtle' then
    return line, {{'Comment', 0, -1},}
  end
  return line
end


M.threads = {
  tree_spec = {
    implicit_expand_action = false,
  },
}
local threads_spec = M.threads.tree_spec

function threads_spec.get_key(thread)
  return thread.id
end

function threads_spec.render_parent(thread)
  return thread.name
end

function threads_spec.render_child(thread_or_frame)
  if thread_or_frame.line then
    -- it's a frame
    return frames.render_item(thread_or_frame)
  end
  if thread_or_frame.stopped then
    return '⏸️ ' .. thread_or_frame.name
  else
    return '▶️ ' .. thread_or_frame.name
  end
end

function threads_spec.has_children(thread_or_frame)
  -- Threads have frames
  return thread_or_frame.line == nil
end

function threads_spec.get_children(thread)
  if thread.threads then
    return thread.threads or {}
  end
  return thread.frames or {}
end


function threads_spec.fetch_children(thread, cb)
  local session = require('dap').session()
  if thread.line then
    -- this is a frame, not a thread
    cb({})
  elseif thread.threads then
    cb(thread.threads)
  elseif session then
    coroutine.wrap(function()
      local co = coroutine.running()
      local is_stopped = thread.stopped
      if not is_stopped then
        session:_pause(thread.id, function(err, result)
          coroutine.resume(co, err, result)
        end)
        coroutine.yield()
      end
      local params = { threadId = thread.id }
      local err, resp = session:request('stackTrace', params)
      if err then
        utils.notify('Error fetching stackTrace: ' .. tostring(err), vim.log.levels.WARN)
      else
        thread.frames = resp.stackFrames
      end
      if not is_stopped then
        local err0 = session:request('continue', params)
        if err0 then
          utils.notify('Error on continue: ' .. tostring(err0), vim.log.levels.WARN)
        else
          thread.stopped = false
          local progress = require('dap.progress')
          progress.report('Thread resumed: ' .. tostring(thread.id))
          progress.report('Running: ' .. session.config.name)
        end
      end
      cb(threads_spec.get_children(thread))
    end)()
  else
    cb({})
  end
end


function threads_spec.compute_actions(info)
  local session = require('dap').session()
  if not session then
    return {}
  end
  local context = info.context
  local thread = info.item
  local result = {}
  if thread.line then
    -- this is a frame, not a thread
    table.insert(result, {
      label = 'Jump to frame',
      fn = function(_, frame)
        session:_frame_set(frame)
        if context.view and vim.bo[context.view.buf].bufhidden == 'wipe' then
          context.view.close()
        end
      end
    })
  else
    table.insert(result, { label = 'Expand', fn = context.tree.toggle })
    if thread.stopped then
      table.insert(result, {
        label = 'Resume thread',
        fn = function()
          if session.stopped_thread_id == thread.id then
            session:_step('continue')
            context.refresh()
          else
            thread.stopped = false
            session:request('continue', { threadId = thread.id }, function(err)
              if err then
                utils.notify('Error on continue: ' .. tostring(err), vim.log.levels.WARN)
              end
              context.refresh()
            end)
          end
        end
      })
    else
      table.insert(result, {
        label = 'Stop thread',
        fn = function()
          session:_pause(thread.id, context.refresh)
        end
      })
    end
  end
  return result
end


return M
```

## File: `lua/dap/health.lua`
```
local M = {}

---@param command string?
local function check_executable(command)
  local health = vim.health
  if not command then
    health.error("Missing required `command` property")
  else
    if vim.fn.executable(command) ~= 1 then
      health.error(table.concat({
        "`command` is not executable.",
        "Check path and permissions.",
        "Use vim.fn.expand to handle ~ or $HOME:\n  ",
        command
      }, " "))
    else
      health.ok("is executable: " .. command)
    end
  end
end


function M.check()
  local health = vim.health
  if not health or not health.start then
    return
  end
  health.start("dap: Adapters")
  local dap = require("dap")
  for t, adapter in pairs(dap.adapters) do
    health.start("dap.adapter: " .. t)
    if type(adapter) == "function" then
      health.info("Adapter is a function. Can't validate it")
    else
      if adapter.type == "executable" then
        adapter = adapter --[[@as dap.ExecutableAdapter]]
        check_executable(adapter.command)
      elseif adapter.type == "server" then
        adapter = adapter --[[@as dap.ServerAdapter]]
        if not adapter.port then
          health.error("Missing required `port` property")
        end
        if adapter.executable then
          check_executable(adapter.executable.command)
        end
      elseif adapter.type == "pipe" then
        adapter = adapter --[[@as dap.PipeAdapter]]
        if not adapter.pipe then
          health.error("Missing required `pipe` property")
        end
      else
        health.error(adapter.type .. " must be one of: executable, server or pipe")
      end
    end
  end

  health.start("dap: Sessions")
  local sessions = dap.sessions()
  if not next(sessions) then
    health.ok("No active sessions")
  else
    for _, session in pairs(sessions) do
      if session.initialized then
        health.ok("  id: " .. session.id .. "\n  type: " .. session.config.type)
      else
        health.warn(table.concat({
          "\n  id: ", session.id,
          "\n  type: ", session.config.type,
          "\n  started, but not initialized. ",
          "Either the adapter definition or the used configuration is wrong, ",
          "or the defined adapter doesn't speak DAP",
        }))
      end
    end
  end
end


return M
```

## File: `lua/dap/log.lua`
```
local M = {}

---@type table<string, dap.log.Log>
local loggers = {}

M._loggers = loggers

---@enum dap.log.Level
M.levels = {
  TRACE = 0,
  DEBUG = 1,
  INFO  = 2,
  WARN  = 3,
  ERROR = 4,
}

---@alias dap.log.Levels "TRACE"|"DEBUG"|"INFO"|"WARN"|"ERROR"

local default_level = M.levels.INFO
local log_date_format = "!%F %H:%M:%S"


---@param level dap.log.Level|dap.log.Levels
---@return dap.log.Level
local function tolevel(level)
  if type(level) == "string" then
    return assert(
      M.levels[tostring(level):upper()],
      string.format('Log level must be one of (trace, debug, info, warn, error), got: %q', level)
    )
  end
  return level
end


---@class dap.log.Log
---@field _fname string
---@field _path string
---@field _file file*?
---@field _level dap.log.Level


---@class dap.log.Log
local Log = {}
local log_mt = {
  __index = Log
}


function Log:write(...)
  self:open()
  self._file:write(...)
  self._file:flush()
end

function Log:open()
  if not self._file then
    local f = assert(io.open(self._path, "w+"))
    self._file = f
  end
end

---@param level dap.log.Level|string
function Log:set_level(level)
  self._level = tolevel(level)
end

function Log:get_path()
  return self._path
end


function Log:close()
  if self._file then
    self._file:flush()
    self._file:close()
    self._file = nil
  end
end

function Log:remove()
  self:close()
  os.remove(self._path)
  loggers[self._fname] = nil
end


---@param level string
---@param levelnr integer
---@return boolean
function Log:_log(level, levelnr, ...)
  local argc = select('#', ...)
  if levelnr < self._level then
    return false
  end
  if argc == 0 then
    return true
  end
  local info = debug.getinfo(3, 'Sl')
  local _, end_ = info.short_src:find("nvim-dap/lua", 1, true)
  local src = end_ and info.short_src:sub(end_ + 2) or info.short_src
  local fileinfo = string.format('%s:%s', src, info.currentline)
  local parts = {
    table.concat({'[', level, '] ', os.date(log_date_format), ' ', fileinfo}, '')
  }
  for i = 1, argc do
    local arg = select(i, ...)
    if arg == nil then
      table.insert(parts, "nil")
    else
      table.insert(parts, vim.inspect(arg))
    end
  end
  self:write(table.concat(parts, '\t'), '\n')
  return true
end



--- Not generating methods below in a loop to help out luals


function Log:trace(...)
  self:_log("TRACE", M.levels.TRACE, ...)
end

function Log:debug(...)
  self:_log("DEBUG", M.levels.DEBUG, ...)
end

function Log:info(...)
  self:_log("INFO", M.levels.INFO, ...)
end

function Log:warn(...)
  self:_log("WARN", M.levels.WARN, ...)
end

function Log:error(...)
  self:_log("ERROR", M.levels.ERROR, ...)
end


---@param level dap.log.Level|dap.log.Levels
function M.set_level(level)
  for _, logger in pairs(loggers) do
    logger:set_level(level)
  end
  default_level = tolevel(level)
end


---@param fname string
---@return string path
---@return string cache_dir
local function getpath(fname)
  local path_sep = vim.loop.os_uname().sysname == "Windows" and "\\" or "/"
  local joinpath = (vim.fs or {}).joinpath or function(...)
    ---@diagnostic disable-next-line: deprecated
    return table.concat(vim.tbl_flatten{...}, path_sep)
  end
  local cache_dir = vim.fn.stdpath('cache')
  assert(type(cache_dir) == "string")
  return joinpath(cache_dir, fname), cache_dir
end


---@param filename string
---@return dap.log.Log
function M.create_logger(filename)
  local logger = loggers[filename]
  if logger then
    logger:open()
    return logger
  end
  local path, cache_dir = getpath(filename)
  local log = {
    _fname = filename,
    _path = path,
    _level = default_level
  }
  logger = setmetatable(log, log_mt)
  loggers[filename] = logger

  vim.fn.mkdir(cache_dir, "p")
  logger:open()
  return logger
end


return M
```

## File: `lua/dap/progress.lua`
```
local M = {}
local messages = {}

local max_size = 11
local idx_read = 0
local idx_write = 0

local last_msg = nil


function M.reset()
  messages = {}
  idx_read = 0
  idx_write = 0
  last_msg = nil
end


---@param msg string
function M.report(msg)
  messages[idx_write] = msg
  idx_write = (idx_write + 1) % max_size
  if idx_write == idx_read then
    idx_read = (idx_read + 1) % max_size
  end

  if vim.in_fast_event() then
    vim.schedule(function()
      vim.cmd('doautocmd <nomodeline> User DapProgressUpdate')
    end)
  else
    vim.cmd('doautocmd <nomodeline> User DapProgressUpdate')
  end
end


---@return string?
function M.poll_msg()
  if idx_read == idx_write then
    return nil
  end
  local msg = messages[idx_read]
  messages[idx_read] = nil
  idx_read = (idx_read + 1) % max_size
  return msg
end


---@return string
function M.status()
  local msg = M.poll_msg() or last_msg
  if msg then
    last_msg = msg
    return msg
  else
    return ''
  end
end


return M
```

## File: `lua/dap/protocol.lua`
```
---@meta

---@class dap.ProtocolMessage
---@field seq number
---@field type "request"|"response"|"event"|string

---@class dap.Request: dap.ProtocolMessage
---@field type "request"
---@field command string
---@field arguments? any


---@class dap.Event: dap.ProtocolMessage
---@field type "event"
---@field event string
---@field body? any


---@class dap.Response: dap.ProtocolMessage
---@field type "response"
---@field request_seq number
---@field success boolean
---@field command string
---@field message? "cancelled"|"notStopped"|string
---@field body? any


---@class dap.ErrorResponse: dap.Response
---@field message? "cancelled"|"notStopped"|string
---@field body {error?: dap.Message}


---@class dap.Message
---@field id number
---@field format string
---@field variables nil|table
---@field showUser nil|boolean


---@class dap.Thread
---@field id number
---@field name string
---@field frames nil|dap.StackFrame[] not part of the spec; added by nvim-dap
---@field stopped nil|boolean not part of the spec; added by nvim-dap


---@class dap.ThreadResponse
---@field threads dap.Thread[]

---@class dap.StackFrame
---@field id number
---@field name string
---@field source dap.Source|nil
---@field line number
---@field column number
---@field endLine nil|number
---@field endColumn nil|number
---@field canRestart boolean|nil
---@field presentationHint nil|"normal"|"label"|"subtle";
---@field scopes? dap.Scope[] Not part of spec; added by nvim-dap


---@class dap.StackFrameFormat : dap.ValueFormat
--- Displays parameters for the stack frame.
--- @field parameters? boolean
---
--- Displays the types of parameters for the stack frame.
--- @field parameterTypes? boolean
---
--- Displays the names of parameters for the stack frame.
--- @field parameterNames? boolean
---
--- Displays the values of parameters for the stack frame.
--- @field parameterValues? boolean
---
--- Displays the line number of the stack frame.
--- @field line? boolean
---
--- Displays the module of the stack frame.
--- @field module? boolean
---
--- Includes all stack frames, including those the debug adapter might
--- otherwise hide.
--- @field includeAll? boolean


---@class dap.StackTraceArguments
---@field threadId number thread for which to retrieve the stackTrace
---@field startFrame? number index of the first frame to return. If omitted frames start at 0
---@field levels? number maximum number of frames to return. If absent or 0 all frames are returned
---@field format? dap.StackFrameFormat only honored with supportsValueFormattingOptions capability

---@class dap.StackTraceResponse
---@field stackFrames dap.StackFrame[]
---@field totalFrames? number


---@class dap.Scope
---@field name string
---@field presentationHint? "arguments"|"locals"|"registers"|string
---@field variablesReference number
---@field namedVariables? number
---@field indexedVariables? number
---@field expensive boolean
---@field source? dap.Source
---@field line? number
---@field column? number
---@field endLine? number
---@field endColumn? number
---@field variables? table<string, dap.Variable> by variable name. Not part of spec


---@class dap.ScopesResponse
---@field scopes dap.Scope[]


---@class dap.ValueFormat
---@field hex? boolean Display the value in hex

---@class dap.VariablesArguments
---@field variablesReference number variable for which to retrieve its children
---@field filter? "indexed"|"named" filter to limit child variables. Both are fetched if nil
---@field start? number index of the first variable to return. If nil children start at 0. Requires `supportsVariablePaging`
---@field count? number number of variables to return. If missing or 0, all variables are returned. Requires `supportsVariablePaging`
---@field format? dap.ValueFormat

---@class dap.VariableResponse
---@field variables dap.Variable[]

---@class dap.Variable
---@field name string
---@field value string
---@field type? string
---@field presentationHint? dap.VariablePresentationHint
---@field evaluateName? string
---@field variablesReference number if > 0 the variable is structured
---@field namedVariables? number
---@field indexedVariables? number
---@field memoryReference? string
---@field declarationLocationReference? number
---@field valueLocationReference? number
---@field variables? dap.Variable[] resolved variablesReference. Not part of the spec; added by nvim-dap
---@field parent? dap.Variable|dap.Scope injected by nvim-dap

---@class dap.EvaluateArguments
---@field expression string
---@field frameId? number
---@field context? "watch"|"repl"|"hover"|"clipboard"|"variables"|string
---@field format? dap.ValueFormat

---@class dap.EvaluateResponse
---@field result string
---@field type? string
---@field presentationHint? dap.VariablePresentationHint
---@field variablesReference number
---@field namedVariables? number
---@field indexedVariables? number
---@field memoryReference? string
---@field valueLocationReference? number


---@class dap.VariablePresentationHint
---@field kind?
---|'property'
---|'method'
---|'class'
---|'data'
---|'event'
---|'baseClass'
---|'innerClass'
---|'interface'
---|'mostDerivedClass'
---|'virtual'
---|'dataBreakpoint'
---|string;
---@field attributes? ('static'|'constant'|'readOnly'|'rawString'|'hasObjectId'|'canHaveObjectId'|'hasSideEffects'|'hasDataBreakpoint'|string)[]
---@field visibility?
---|'public'
---|'private'
---|'protected'
---|'internal'
---|'final'
---|string
---@field lazy? boolean


---@class dap.Source
---@field name nil|string
---@field path nil|string
---@field sourceReference nil|number
---@field presentationHint nil|"normal"|"emphasize"|"deemphasize"
---@field origin nil|string
---@field sources nil|dap.Source[]
---@field adapterData nil|any


---@class dap.SourceResponse
---@field content string
---@field mimeType? string


---@class dap.Capabilities
---@field supportsConfigurationDoneRequest boolean|nil
---@field supportsFunctionBreakpoints boolean|nil
---@field supportsConditionalBreakpoints boolean|nil
---@field supportsHitConditionalBreakpoints boolean|nil
---@field supportsEvaluateForHovers boolean|nil
---@field exceptionBreakpointFilters dap.ExceptionBreakpointsFilter[]|nil
---@field supportsStepBack boolean|nil
---@field supportsSetVariable boolean|nil
---@field supportsRestartFrame boolean|nil
---@field supportsGotoTargetsRequest boolean|nil
---@field supportsStepInTargetsRequest boolean|nil
---@field supportsCompletionsRequest boolean|nil
---@field completionTriggerCharacters string[]|nil
---@field supportsModulesRequest boolean|nil
---@field additionalModuleColumns dap.ColumnDescriptor[]|nil
---@field supportedChecksumAlgorithms dap.ChecksumAlgorithm[]|nil
---@field supportsRestartRequest boolean|nil
---@field supportsExceptionOptions boolean|nil
---@field supportsValueFormattingOptions boolean|nil
---@field supportsExceptionInfoRequest boolean|nil
---@field supportTerminateDebuggee boolean|nil
---@field supportSuspendDebuggee boolean|nil
---@field supportsDelayedStackTraceLoading boolean|nil
---@field supportsLoadedSourcesRequest boolean|nil
---@field supportsLogPoints boolean|nil
---@field supportsTerminateThreadsRequest boolean|nil
---@field supportsSetExpression boolean|nil
---@field supportsTerminateRequest boolean|nil
---@field supportsDataBreakpoints boolean|nil
---@field supportsReadMemoryRequest boolean|nil
---@field supportsWriteMemoryRequest boolean|nil
---@field supportsDisassembleRequest boolean|nil
---@field supportsCancelRequest boolean|nil
---@field supportsBreakpointLocationsRequest boolean|nil
---@field supportsClipboardContext boolean|nil
---@field supportsSteppingGranularity boolean|nil
---@field supportsInstructionBreakpoints boolean|nil
---@field supportsExceptionFilterOptions boolean|nil
---@field supportsSingleThreadExecutionRequests boolean|nil

---@class dap.InitializeRequestArguments
---@field clientId? string
---@field clientName? string
---@field adapterId string
---@field locale string
---@field linesStartAt1? boolean
---@field columnsStartAt1? boolean
---@field pathFormat? "path" | "uri" | string
---@field supportsVariableType? boolean
---@field supportsVariablePaging? boolean
---@field supportsRunInTerminalRequest? boolean
---@field supportsMemoryReferences? boolean
---@field supportsProgressReporting? boolean
---@field supportsInvalidatedEvent? boolean
---@field supportsMemoryEvent? boolean
---@field supportsArgsCanBeInterpretedByShell? boolean
---@field supportsStartDebuggingRequest? boolean
---@field supportsANSIStyling? boolean

---@class dap.ExceptionBreakpointsFilter
---@field filter string
---@field label string
---@field description string|nil
---@field default boolean|nil
---@field supportsCondition boolean|nil
---@field conditionDescription string|nil

---@class dap.ColumnDescriptor
---@field attributeName string
---@field label string
---@field format string|nil
---@field type nil|"string"|"number"|"number"|"unixTimestampUTC"
---@field width number|nil


---@class dap.ChecksumAlgorithm
---@field algorithm "MD5"|"SHA1"|"SHA256"|"timestamp"
---@field checksum string

---@class dap.SetBreakpointsResponse
---@field breakpoints dap.Breakpoint[]


---@class dap.SetBreakpointsArguments
---
--- location of the breakpoint.
--- Either source.path or source.sourceReference must be specified.
---@field source dap.Source
---@field breakpoints? dap.SourceBreakpoint[]
---@field sourceModified? boolean


---@class dap.SourceBreakpoint
---@field line integer
---@field column? integer
---@field condition? string
---@field hitCondition? string
---@field logMessage? string
---@field mode? string


---@class dap.Breakpoint
---@field id? number
---@field verified boolean
---@field message? string
---@field source? dap.Source
---@field line? number
---@field column? number
---@field endLine? number
---@field endColumn? number
---@field instructionReference? string
---@field offset? number

---@class dap.InitializedEvent

---@class dap.StoppedEvent
---@field reason "step"|"breakpoint"|"exception"|"pause"|"entry"|"goto"|"function breakpoint"|"data breakpoint"|"instruction breakpoint"|string;
---@field description nil|string
---@field threadId nil|number
---@field preserveFocusHint nil|boolean
---@field text nil|string
---@field allThreadsStopped nil|boolean
---@field hitBreakpointIds nil|number[]

---@class dap.TerminatedEvent
---@field restart? any

---@class dap.TerminateArguments
---@field restart? boolean

---@class dap.DisconnectArguments
---@field restart? boolean
---@field terminateDebuggee? boolean requires `supportTerminateDebuggee` capability
---@field suspendDebuggee? boolean requires `supportSuspendDebuggee` capability


---@class dap.ThreadEvent
---@field reason "started"|"exited"|string
---@field threadId number


---@class dap.ContinuedEvent
---@field threadId number
---@field allThreadsContinued? boolean


---@class dap.BreakpointEvent
---@field reason "changed"|"new"|"removed"|string
---@field breakpoint dap.Breakpoint


---@class dap.ProgressStartEvent
---@field progressId string
---@field title string
---@field requestId? number
---@field cancellable? boolean
---@field message? string
---@field percentage? number

---@class dap.ProgressUpdateEvent
---@field progressId string
---@field message? string
---@field percentage? number

---@class dap.ProgressEndEvent
---@field progressId string
---@field message? string


---@class dap.OutputEvent
---@field category? "console"|"important"|"stdout"|"stderr"|"telemetry"|string
---@field output string
---@field group? "start"|"startCollapsed"|"end"
---
--- if > 0 the output contains objects which
--- can be retrieved by passing `variablesReference` to the `variables` request
--- as long as execution remains suspended.
---@field variablesReference? number
---@field source? dap.Source
---@field line? integer
---@field column? integer
---@field data? any


---@class dap.StartDebuggingRequestArguments
---@field configuration table<string, any>
---@field request 'launch'|'attach'


---@class dap.CompletionsResponse
---@field targets dap.CompletionItem[]


---@class dap.LocationsArguments
---@field locationReference number


---@class dap.LocationsResponse
---@field source dap.Source
---@field line integer
---@field column? integer
---@field endLine? integer
---@field endColumn? integer


---@alias dap.CompletionItemType
---|'method'
---|'function'
---|'constructor'
---|'field'
---|'variable'
---|'class'
---|'interface'
---|'module'
---|'property'
---|'unit'
---|'value'
---|'enum'
---|'keyword'
---|'snippet'
---|'text'
---|'color'
---|'file'
---|'reference'
---|'customcolor'

---@class dap.CompletionsArguments
---@field frameId? number
---@field text string
---@field column integer utf-16 code units, 0- or 1-based depending on columnsStartAt1
---@field line? integer

---@class dap.CompletionItem
---@field label string By default this is also the text that is inserted when selecting this completion
---@field text? string If present and not empty this is inserted instead of the label
---@field sortText? string Used to sort completion items if present and not empty. Otherwise label is used
---@field detail? string human-readable string with additional information about this item. Like type or symbol information
---@field type? dap.CompletionItemType
---@field start? number Start position in UTF-16 code units. (within the `text` attribute of the `completions` request) 0- or 1-based depending on `columnsStartAt1` capability. If omitted, the text is added at the location of the `column` attribute of the `completions` request.
---@field length? number How many characters are overwritten by the completion text. Measured in UTF-16 code units. If missing the value 0 is assumed which results in the completion text being inserted.
---@field selectionStart? number
---@field selectionLength? number

---@alias dap.SteppingGranularity 'statement'|'line'|'instruction'

---@class dap.RunInTerminalRequestArguments
---@field kind? 'integrated'|'external'
---@field title? string
---@field cwd string
---@field args string[]
---@field env? table<string, string>
---@field argsCanBeInterpretedByShell? boolean
```

## File: `lua/dap/repl.lua`
```
local api = vim.api
local ui = require('dap.ui')
local utils = require('dap.utils')
local prompt = "dap> "
local M = {}

local history = {
  last = nil,
  entries = {},
  idx = 1,
  max_size = 100,
}

local autoscroll = vim.fn.has('nvim-0.7') == 1

local function get_session()
  return require('dap').session()
end

local execute  -- required for forward reference


---@param buf integer
local function line_count(buf)
  assert(vim.bo[buf].buftype == "prompt", "buf must have buftype=prompt")
  if vim.fn.has("nvim-0.12") == 1 then
    local ok, mark = pcall(api.nvim_buf_get_mark, buf, ":")
    if ok then
      return mark[1] - 1
    end
  end
  return api.nvim_buf_line_count(buf) - 1
end


local function new_buf()
  local prev_buf = api.nvim_get_current_buf()
  local buf = api.nvim_create_buf(true, true)
  api.nvim_buf_set_name(buf, string.format('[dap-repl-%d]', buf))
  vim.b[buf]["dap-srcft"] = vim.bo[prev_buf].filetype
  vim.bo[buf].buftype = "prompt"
  vim.bo[buf].omnifunc = "v:lua.require'dap.repl'.omnifunc"
  vim.bo[buf].buflisted = false
  vim.bo[buf].tagfunc = "v:lua.require'dap'._tagfunc"
  local path = vim.bo[prev_buf].path
  if path and path ~= "" then
    vim.bo[buf].path = path
  end
  api.nvim_buf_set_keymap(buf, 'n', '<CR>', "<Cmd>lua require('dap.ui').trigger_actions({ mode = 'first' })<CR>", {})
  api.nvim_buf_set_keymap(buf, 'n', 'o', "<Cmd>lua require('dap.ui').trigger_actions()<CR>", {})
  api.nvim_buf_set_keymap(buf, 'i', '<up>', "<Cmd>lua require('dap.repl').on_up()<CR>", {})
  api.nvim_buf_set_keymap(buf, 'i', '<down>', "<Cmd>lua require('dap.repl').on_down()<CR>", {})
  vim.keymap.set("n", "]]", function()
    local lnum = api.nvim_win_get_cursor(0)[1] - 1
    local lines = api.nvim_buf_get_lines(buf, lnum + 1, -1, false)
    for i, line in ipairs(lines) do
      if vim.startswith(line, prompt) then
        api.nvim_win_set_cursor(0, { i + lnum + 1, #line - 1 })
        break
      end
    end
  end, { buffer = buf, desc = "Move to next prompt" })
  vim.keymap.set("n", "[[", function()
    local lnum = api.nvim_win_get_cursor(0)[1] - 1
    local lines = api.nvim_buf_get_lines(buf, 0, lnum, true)
    local num_lines = #lines
    for i = num_lines, 1, -1 do
      local line = lines[i]
      if vim.startswith(line, prompt) then
        api.nvim_win_set_cursor(0, { lnum - (num_lines - i), #line - 1 })
        break
      end
    end
  end, { buffer = buf, desc = "Move to previous prompt" })
  api.nvim_create_autocmd("TextYankPost", {
    buffer = buf,
    callback = function()
      require("dap._cmds").yank_evalname()
    end,
  })
  vim.fn.prompt_setprompt(buf, prompt)
  vim.fn.prompt_setcallback(buf, execute)
  if vim.fn.has('nvim-0.7') == 1 then
    vim.keymap.set('n', 'G', function()
      autoscroll = vim.v.count == 0
      vim.cmd(string.format('normal! %dG', vim.v.count))
    end, { silent = true, buffer = buf })
    api.nvim_create_autocmd({'InsertEnter', 'CursorMoved'}, {
      group = api.nvim_create_augroup('dap-repl-au', {clear = true}),
      buffer = buf,
      callback = function()
        local active_buf = api.nvim_win_get_buf(0)
        if active_buf == buf then
          local lnum = api.nvim_win_get_cursor(0)[1]
          autoscroll = lnum >= line_count(buf)
        end
      end
    })
  end
  vim.bo[buf].filetype = "dap-repl"
  return buf
end


local function new_win(buf, winopts, wincmd)
  assert(not wincmd or type(wincmd) == 'string', 'wincmd must be nil or a string')
  api.nvim_command(wincmd or 'belowright split')
  local win = api.nvim_get_current_win()
  api.nvim_win_set_buf(win, buf)
  if vim.fn.has("nvim-0.11") == 1 then
    vim.wo[win][0].relativenumber = false
    vim.wo[win][0].number = false
    vim.wo[win][0].foldcolumn = "0"
    vim.wo[win][0].signcolumn = "auto"
    vim.wo[win][0].wrap = false
  else
    vim.wo[win].wrap = false
  end
  ui.apply_winopts(win, winopts)
  return win
end

local repl = ui.new_view(
  new_buf,
  new_win, {
    before_open = function()
      return api.nvim_get_current_win()
    end,
    after_open = function(_, prev_win)
      api.nvim_set_current_win(prev_win)
    end
  }
)


M.commands = {
  continue = {'.continue', '.c'},
  next_ = {'.next', '.n'},
  nexti = {'.nexti', '.ni'},
  step_back = {'.back', '.b'},
  step_backi = {'.backi', '.bi'},
  reverse_continue = {'.reverse-continue', '.rc'},
  into = {'.into'},
  intoi = {'.intoi'},
  into_targets = {'.into-targets'},
  out = {'.out'},
  scopes = {'.scopes'},
  threads = {'.threads'},
  frames = {'.frames'},
  exit = {'exit', '.exit'},
  up = {'.up'},
  down = {'.down'},
  goto_ = {'.goto'},
  pause = {'.pause', '.p'},
  clear = {'.clear'},
  capabilities = {'.capabilities'},
  help = {'help', '.help', '.h'},
  custom_commands = {}
}


function M.print_stackframes(frames)
  if not repl.buf then
    return
  end
  local session = get_session()
  frames = frames or (session and session.threads[session.stopped_thread_id] or {}).frames or {}
  local context = {}
  M.append('(press enter on line to jump to frame)')
  local start = api.nvim_buf_line_count(repl.buf) - 1
  local render_frame = require('dap.entity').frames.render_item
  context.actions = {
    {
      label = 'Jump to frame',
      fn = function(layer, frame)
        local s = get_session()
        if s then
          s:_frame_set(frame)
          layer.render(frames, render_frame, context, start, start + #frames)
        else
          utils.notify('Cannot navigate to frame without active session', vim.log.levels.INFO)
        end
      end,
    },
  }
  local layer = ui.layer(repl.buf)
  layer.render(frames, render_frame, context)
end


local function print_commands()
  M.append('Commands:')
  for _, commands in pairs(M.commands) do
    if #commands > 0 then
      M.append('  ' .. table.concat(commands, ', '))
    end
  end

  M.append('Custom commands:')
  for command, _ in pairs(M.commands.custom_commands or {}) do
    M.append('  ' .. command)
  end
end


local function evaluate_handler(err, resp)
  if err then
    M.append(tostring(err), nil, { newline = true })
    return
  end
  local layer = ui.layer(repl.buf)
  local attributes = (resp.presentationHint or {}).attributes or {}
  if resp.variablesReference > 0 or vim.tbl_contains(attributes, 'rawString') then
    local spec = require('dap.entity').variable.tree_spec
    local tree = ui.new_tree(spec)
    -- tree.render would "append" twice, once for the top element and once for the children
    -- Appending twice would result in a intermediate "dap> " prompt
    -- To avoid that this eagerly fetches the children; pre-renders the region
    -- and lets tree.render override it
    if spec.has_children(resp) then
      spec.fetch_children(resp, function()
        tree.render(layer, resp, nil)
      end)
    else
      tree.render(layer, resp, nil)
    end
  else
    M.append(resp.result, nil, { newline = true })
  end
end


local function print_scopes(frame)
  if not frame then return end
  local tree = ui.new_tree(require('dap.entity').scope.tree_spec)
  local layer = ui.layer(repl.buf)
  for _, scope in pairs(frame.scopes or {}) do
    tree.render(layer, scope)
  end
end


local function print_threads(threads)
  if not threads then
    return
  end
  local spec = vim.deepcopy(require('dap.entity').threads.tree_spec)
  spec.extra_context = {
    refresh = function()
      local session = get_session()
      if session then
        print_threads(vim.tbl_values(session.threads))
      end
    end
  }
  local tree = ui.new_tree(spec)
  local layer = ui.layer(repl.buf)
  local root = {
    id = 0,
    name = 'Threads',
    threads = vim.tbl_values(threads)
  }
  tree.render(layer, root)
end


---@param confname string
---@return dap.Session?
local function trystart(confname)
  assert(coroutine.running() ~= nil, "Must run in coroutine")
  local dap = require("dap")
  local bufnr = api.nvim_get_current_buf()
  for _, get_configs in pairs(dap.providers.configs) do
    local configs = get_configs(bufnr)
    for _, config in ipairs(configs) do
      if confname == config.name then
        dap.run(config)
      end
    end
  end
  return dap.session()
end


---@param text string
---@param opts? dap.repl.execute.Opts
local function coexecute(text, opts)
  assert(coroutine.running() ~= nil, "Must run in coroutine")
  opts = opts or {}

  local session = get_session()
  if not session then
    local ft = vim.b["dap-srcft"] or vim.bo.filetype
    local autostart = require("dap").defaults[ft].autostart
    if autostart then
      session = trystart(autostart)
    end
    if not session then
      M.append('No active debug session')
      return
    end
  end
  local words = vim.split(text, ' ', { plain = true })
  if vim.tbl_contains(M.commands.continue, text) then
    require('dap').continue()
  elseif vim.tbl_contains(M.commands.next_, text) then
    require('dap').step_over()
  elseif vim.tbl_contains(M.commands.nexti, text) then
    require('dap').step_over({granularity = "instruction"})
  elseif vim.tbl_contains(M.commands.capabilities, text) then
    M.append(vim.inspect(session.capabilities))
  elseif vim.tbl_contains(M.commands.into, text) then
    require('dap').step_into()
  elseif vim.tbl_contains(M.commands.intoi, text) then
    require('dap').step_into({granularity = "instruction"})
  elseif vim.tbl_contains(M.commands.into_targets, text) then
    require('dap').step_into({askForTargets=true})
  elseif vim.tbl_contains(M.commands.out, text) then
    require('dap').step_out()
  elseif vim.tbl_contains(M.commands.up, text) then
    session:_frame_delta(1)
    M.print_stackframes()
  elseif vim.tbl_contains(M.commands.step_back, text) then
    require('dap').step_back()
  elseif vim.tbl_contains(M.commands.step_backi, text) then
    require('dap').step_back({granularity = "instruction"})
  elseif vim.tbl_contains(M.commands.pause, text) then
    session:_pause()
  elseif vim.tbl_contains(M.commands.reverse_continue, text) then
    require('dap').reverse_continue()
  elseif vim.tbl_contains(M.commands.down, text) then
    session:_frame_delta(-1)
    M.print_stackframes()
  elseif vim.tbl_contains(M.commands.goto_, words[1]) then
    if words[2] then
      session:_goto(tonumber(words[2]))
    end
  elseif vim.tbl_contains(M.commands.scopes, text) then
    print_scopes(session.current_frame)
  elseif vim.tbl_contains(M.commands.threads, text) then
    print_threads(vim.tbl_values(session.threads))
  elseif vim.tbl_contains(M.commands.frames, text) then
    M.print_stackframes()
  elseif M.commands.custom_commands[words[1]] then
    local command = words[1]
    local args = string.sub(text, string.len(command)+2)
    M.commands.custom_commands[command](args)
  else
    ---@type dap.EvaluateArguments
    local params = {
      expression = text,
      context = opts.context or "repl"
    }
    session:evaluate(params, evaluate_handler)
  end
end


---@class dap.repl.execute.Opts
---@field context? "watch"|"repl"|"hover"|"variables"|"clipboard"


---@param text string
---@param opts? dap.repl.execute.Opts
function execute(text, opts)
  if text == '' then
    if history.last then
      text = history.last
    else
      return
    end
  else
    history.last = text
    if #history.entries == history.max_size then
      table.remove(history.entries, 1)
    end
    table.insert(history.entries, text)
    history.idx = #history.entries + 1
  end
  if vim.tbl_contains(M.commands.exit, text) then
    local session = get_session()
    if session then
      -- Should result in a `terminated` event which closes the session and sets it to nil
      session:disconnect()
    end
    api.nvim_command('close')
    return
  end
  if vim.tbl_contains(M.commands.help, text) then
    print_commands()
  elseif vim.tbl_contains(M.commands.clear, text) then
    if repl.buf and api.nvim_buf_is_loaded(repl.buf) then
      M.clear()
    end
  else
    require("dap.async").run(function()
      coexecute(text, opts)
    end)
  end
end


--- Add and execute text as if entered directly
---@param text string
---@param opts? dap.repl.execute.Opts
function M.execute(text, opts)
  M.append(prompt .. text, "$", { newline = true })
  local numlines = line_count(repl.buf)
  if repl.win and api.nvim_win_is_valid(repl.win) then
    pcall(api.nvim_win_set_cursor, repl.win, { numlines, 0 })
    api.nvim_win_call(repl.win, function()
      vim.cmd.normal({"zt", bang = true })
    end)
  end
  execute(text, opts)
end


--- Close the REPL if it is open.
--
-- Does not disconnect an active session.
--
-- Returns true if the REPL was open and got closed. false otherwise
M.close = repl.close

--- Open the REPL
--
--@param winopts  optional table which may include:
--                  `height` to set the window height
--                  `width` to set the window width
--
--                  Any other key/value pair, that will be treated as window
--                  option.
--
--@param wincmd command that is used to create the window for the REPL.
--              Defaults to 'belowright split'
M.open = repl.open

--- Open the REPL if it is closed, close it if it is open.
M.toggle = repl.toggle


local function select_history(delta)
  if not repl.buf then
    return
  end
  history.idx = history.idx + delta
  if history.idx < 1 then
    history.idx = #history.entries
  elseif history.idx > #history.entries then
    history.idx = 1
  end
  local text = history.entries[history.idx]
  if text then
    local lnum = vim.fn.line('$')
    local lines = vim.split(text, "\n", { plain = true })
    lines[1] = prompt .. lines[1]
    api.nvim_buf_set_lines(repl.buf, lnum - 1, -1, true, lines)
    vim.fn.setcursorcharpos({ vim.fn.line("$"), vim.fn.col('$') })  -- move cursor to the end of line
  end
end


function M.on_up()
  select_history(-1)
end

function M.on_down()
  select_history(1)
end



---@param line string
---@param lnum (integer|string)?
---@param opts? {newline: boolean}
function M.append(line, lnum, opts)
  opts = opts or {}
  local buf = repl._init_buf()
  line = line:gsub("\r\n", "\n")
  local lines = vim.split(line, "\n")
  if lnum == '$' or not lnum then
    lnum = line_count(buf)
    if opts.newline == false then
      if lnum == 0 then
        api.nvim_buf_set_lines(buf, lnum, lnum, true, lines)
      else
        local last_line = api.nvim_buf_get_lines(buf, lnum - 1, lnum, true)[1]
        api.nvim_buf_set_text(buf, lnum - 1, #last_line, lnum - 1, #last_line, lines)
      end
    else
      api.nvim_buf_set_lines(buf, lnum, lnum, true, lines)
    end
  elseif type(lnum) == "number" then
    api.nvim_buf_set_lines(buf, lnum, lnum, true, lines)
  else
    error("Unsupported lnum argument: " .. tostring(lnum))
  end
  if autoscroll and repl.win and api.nvim_win_is_valid(repl.win) then
    pcall(api.nvim_win_set_cursor, repl.win, { lnum + 2, 0 })
  end
  return lnum
end


function M.clear()
  if repl.buf and api.nvim_buf_is_loaded(repl.buf) then
    local layer = ui.layer(repl.buf)
    layer.render({}, tostring, {}, 0, - 1)
  end
end

do

  ---@param candidates dap.CompletionItem[]
  local function completions_to_items(candidates)
    table.sort(candidates, function(a, b)
      return (a.sortText or a.label) < (b.sortText or b.label)
    end)
    local items = {}
    for _, candidate in pairs(candidates) do
      table.insert(items, {
        word = candidate.text or candidate.label,
        abbr = candidate.label,
        dup = 0;
        icase = 1;
      })
    end
    return items
  end

  --- Finds word boundary for [vim.fn.complete]
  ---
  ---@param items dap.CompletionItem[]
  ---@return boolean mixed, integer? start
  local function get_start(items, prefix)
    local start = nil
    local mixed = false
    for _, item in ipairs(items) do
      if item.start and (item.length or 0) > 0 then
        if start and start ~= item.start then
          mixed = true
          start = math.min(start, item.start)
        else
          start = item.start
        end
      end
      if not start and (item.text or item.label):sub(1, #prefix) == prefix then
        start = 0
      end
    end
    return mixed, start
  end

  function M.omnifunc(findstart, base)
    local session = get_session()
    local col = api.nvim_win_get_cursor(0)[2]
    local line = api.nvim_get_current_line()
    local offset = vim.startswith(line, prompt) and 5 or 0
    local line_to_cursor = line:sub(offset + 1, col)
    local text_match = vim.fn.match(line_to_cursor, '\\k*$')
    if vim.startswith(line_to_cursor, '.') or base ~= '' then
      if findstart == 1 then
        return offset
      end
      local completions = {}
      for key, values in pairs(M.commands) do
        if key ~= "custom_commands" then
          for _, val in pairs(values) do
            if vim.startswith(val, base) then
              table.insert(completions, val)
            end
          end
        end
      end
      for key, _ in pairs(M.commands.custom_commands or {}) do
        if vim.startswith(key, base) then
          table.insert(completions, key)
        end
      end

      return completions
    end
    local supportsCompletionsRequest = ((session or {}).capabilities or {}).supportsCompletionsRequest;
    if not supportsCompletionsRequest then
      if findstart == 1 then
        return -1
      else
        return {}
      end
    end
    assert(session, 'Session must exist if supportsCompletionsRequest is true')
    ---@type dap.CompletionsArguments
    local args = {
      frameId = (session.current_frame or {}).id,
      text = line_to_cursor,
      column = col + 1 - offset
    }
    ---@param err dap.ErrorResponse?
    ---@param response dap.CompletionsResponse?
    local function on_response(err, response)
      if err then
        require('dap.utils').notify('completions request failed: ' .. err.message, vim.log.levels.WARN)
      elseif response then
        local items = response.targets
        local mixed, start = get_start(items, line_to_cursor)
        if start and not mixed then
          vim.fn.complete(offset + start + 1, completions_to_items(items))
        else
          vim.fn.complete(offset + text_match + 1, completions_to_items(items))
        end
      end
    end
    session:request('completions', args, on_response)

    -- cancel but stay in completion mode for completion via `completions` callback
    return -2
  end
end


function M._exit()
  local buf = repl.buf
  if buf and vim.bo[buf].modified then
    vim.bo[buf].modified = false
  end
end


return M
```

## File: `lua/dap/rpc.lua`
```
local utils = require('dap.utils')
local M = {}

---@param header string
---@return integer?
local function get_content_length(header)
  for line in header:gmatch("(.-)\r\n") do
    local key, value = line:match('^%s*(%S+)%s*:%s*(%d+)%s*$')
    if key and key:lower() == "content-length" then
      return tonumber(value)
    end
  end
end


local parse_chunk_loop
local has_strbuffer, strbuffer = pcall(require, "string.buffer")

if has_strbuffer then
  parse_chunk_loop = function()
    local buf = strbuffer.new()
    while true do
      local msg = buf:tostring()
      local header_end = msg:find('\r\n\r\n', 1, true)
      if header_end then
        local header = buf:get(header_end + 1)
        buf:skip(2) -- skip past header boundary
        local content_length = get_content_length(header)
        if not content_length then
          error("Content-Length not found in headers: " .. header)
        end
        while #buf < content_length do
          local chunk = coroutine.yield()
          buf:put(chunk)
        end
        local body = buf:get(content_length)
        coroutine.yield(body)
      else
        local chunk = coroutine.yield()
        buf:put(chunk)
      end
    end
  end
else
  parse_chunk_loop = function()
    local buffer = ''
    while true do
      local header_end, body_start = buffer:find('\r\n\r\n', 1, true)
      if header_end then
        local header = buffer:sub(1, header_end + 1)
        local content_length = get_content_length(header)
        if not content_length then
          error("Content-Length not found in headers: " .. header)
        end
        local body_chunks = {buffer:sub(body_start + 1)}
        local body_length = #body_chunks[1]
        while body_length < content_length do
          local chunk = coroutine.yield()
            or error("Expected more data for the body. The server may have died.")
          table.insert(body_chunks, chunk)
          body_length = body_length + #chunk
        end
        local last_chunk = body_chunks[#body_chunks]

        body_chunks[#body_chunks] = last_chunk:sub(1, content_length - body_length - 1)
        local rest = ''
        if body_length > content_length then
          rest = last_chunk:sub(content_length - body_length)
        end
        local body = table.concat(body_chunks)
        buffer = rest .. (coroutine.yield(body)
          or error("Expected more data for the body. The server may have died."))
      else
        buffer = buffer .. (coroutine.yield()
          or error("Expected more data for the header. The server may have died."))
      end
    end
  end
end


function M.create_read_loop(handle_body, on_no_chunk)
  local parse_chunk = coroutine.wrap(parse_chunk_loop)
  parse_chunk()
  return function (err, chunk)
    if err then
      utils.notify(err, vim.log.levels.ERROR)
      return
    end
    if not chunk then
      if on_no_chunk then
        on_no_chunk()
      end
      return
    end
    while true do
      local body = parse_chunk(chunk)
      if body then
        handle_body(body)
        chunk = ""
      else
        break
      end
    end
  end
end


function M.msg_with_content_length(msg)
  return table.concat {
    'Content-Length: ';
    tostring(#msg);
    '\r\n\r\n';
    msg
  }
end


return M
```

## File: `lua/dap/session.lua`
```
local uv = vim.loop
local api = vim.api
local rpc = require('dap.rpc')

local utils = require('dap.utils')
local breakpoints = require('dap.breakpoints')
local progress = require('dap.progress')
local log = require('dap.log').create_logger('dap.log')
local repl = require('dap.repl')
local sec_to_ms = 1000
local non_empty = utils.non_empty
local index_of = utils.index_of
local mime_to_filetype = {
  ['text/javascript'] = 'javascript'
}

local err_mt = {
  __tostring = function(e)
    return utils.fmt_error(e) or "Undefined error"
  end,
}


local ns_pool = {}
do
  local next_id = 1
  local pool = {}

  ---@return number
  function ns_pool.acquire()
    local ns = next(pool)
    if ns then
      pool[ns] = nil
      return ns
    end
    ns = api.nvim_create_namespace('dap-' .. tostring(next_id))
    next_id = next_id + 1
    return ns
  end

  ---@param ns number
  function ns_pool.release(ns)
    pool[ns] = true
  end
end


---@class dap.Session
---@field capabilities dap.Capabilities
---@field adapter dap.Adapter
---@field private dirty table<string, boolean>
---@field private handlers table<string, fun(self: dap.Session, payload: table)|fun()>
---@field private message_callbacks table<number, fun(err: nil|dap.ErrorResponse, body: nil|table, seq: number)>
---@field private message_requests table<number, any>
---@field private client dap.TransportClient
---@field private handle uv.uv_stream_t
---@field current_frame dap.StackFrame|nil
---@field initialized boolean
---@field term_buf? integer
---@field stopped_thread_id number|nil
---@field id number
---@field threads table<number, dap.Thread>
---@field filetype string filetype of the buffer where the session was started
---@field ns number Namespace id. Valid during lifecycle of a session
---@field sign_group string
---@field closed boolean
---@field on_close table<string, fun(session: dap.Session)> Handler per plugin-id. Invoked when a session closes (due to terminated event, disconnect or error cases like initialize errors, debug adapter process exit, ...). Session is assumed non-functional at this point and handler can be invoked within luv event loop (not API safe, may require vim.schedule)
---@field children table<number, dap.Session>
---@field parent dap.Session|nil
---@field config dap.Configuration


---@class dap.TransportClient
---@field close fun(cb: function)
---@field write fun(line: string)

---@class dap.Session
local Session = {}
local session_mt = { __index = Session }


local function json_decode(payload)
  return vim.json.decode(payload, { luanil = { object = true }})
end
local json_encode = vim.json.encode
local function send_payload(client, payload)
  local msg = rpc.msg_with_content_length(json_encode(payload))
  client.write(msg)
end


local function dap()
  return require('dap')
end

local function ui()
  return require('dap.ui')
end

---@param session dap.Session
local function defaults(session)
  return dap().defaults[session.config.type]
end


local function coresume(co)
  return function(...)
    if coroutine.status(co) == "suspended" then
      coroutine.resume(co, ...)
    else
      local args = {...}
      vim.schedule(function()
        assert(
          coroutine.status(co) == "suspended",
          "Incorrect use of coresume. Callee must have yielded"
        )
        coroutine.resume(co, unpack(args))
      end)
    end
  end
end


---@param env table<string, string>?
---@param terminal {command: string, args: string[]?}
---@param args string[]
---@param cwd string
local function launch_external_terminal(env, terminal, args, cwd)
  local handle
  local pid_or_err
  local full_args = {}
  vim.list_extend(full_args, terminal.args or {})
  vim.list_extend(full_args, args)
  -- Initializing to nil is important so environment is inherited by the terminal
  local env_formatted = nil
  if env then
    env_formatted = {}
    -- Copy environment, prefer vars set by client
    for k, v in pairs(vim.tbl_extend('keep', env, vim.fn.environ())) do
      if k:find "^[^=]*$" then -- correct variable?
        env_formatted[#env_formatted+1] = k.."="..tostring(v)
      end
    end
  end
  local opts = {
    args = full_args,
    detached = true,
    cwd = (cwd and cwd ~= "") and cwd or nil,
    env = env_formatted,
  }
  handle, pid_or_err = uv.spawn(terminal.command, opts, function(code)
    if handle then
      handle:close()
    end
    if code ~= 0 then
      utils.notify(string.format('Terminal exited %d running %s %s', code, terminal.command, table.concat(full_args, ' ')), vim.log.levels.ERROR)
    end
  end)
  return handle, pid_or_err
end


---@param terminal_win_cmd string|fun(config: dap.Configuration):(integer, integer?)
---@param config dap.Configuration
---@return integer bufnr, integer? winnr
local function create_terminal_buf(terminal_win_cmd, config)
  local cur_win = api.nvim_get_current_win()
  if type(terminal_win_cmd) == "string" then
    api.nvim_command(terminal_win_cmd)
    local bufnr = api.nvim_get_current_buf()
    local win = api.nvim_get_current_win()
    api.nvim_set_current_win(cur_win)
    return bufnr, win
  else
    assert(type(terminal_win_cmd) == "function", "terminal_win_cmd must be a string or a function")
    return terminal_win_cmd(config)
  end
end


local terminals = {}
do
  ---@type table<integer, boolean>
  local pool = {}

  ---@param filetype string
  ---@return integer, integer|nil
  function terminals.acquire(win_cmd, config, filetype)
    local buf = next(pool)
    if buf then
      pool[buf] = nil
      if api.nvim_buf_is_valid(buf) then
        vim.bo[buf].modified = false
        return buf
      end
    end
    local terminal_win
    local prev_buf = api.nvim_get_current_buf()
    buf, terminal_win = create_terminal_buf(win_cmd, config)
    assert(buf, "terminal_win_cmd must return a buffer number")
    vim.bo[buf].errorformat = vim.bo[prev_buf].errorformat
    if vim.filetype then
      local path = vim.filetype.get_option(filetype, "path")
      assert(type(path) == "string", "path option must be a string")
      vim.bo[buf].path = path
    else
      vim.bo[buf].path = vim.bo[prev_buf].path
    end
    if terminal_win then
      if vim.fn.has('nvim-0.8') == 1 then
        -- older versions don't support the `win` key
        api.nvim_set_option_value('number', false, { scope = 'local', win = terminal_win })
        api.nvim_set_option_value('relativenumber', false, { scope = 'local', win = terminal_win })
        api.nvim_set_option_value('signcolumn', 'no', { scope = 'local', win = terminal_win })
      else
        -- this is like `:set` so new windows will inherit the values :/
        vim.wo[terminal_win].number = false
        vim.wo[terminal_win].relativenumber = false
        vim.wo[terminal_win].signcolumn = "no"
      end
    end
    vim.b[buf]['dap-type'] = config.type
    return buf, terminal_win
  end

  ---@param b number
  function terminals.release(b)
    pool[b] = true
  end
end


---@param lsession dap.Session
local function run_in_terminal(lsession, request)
  ---@type dap.RunInTerminalRequestArguments
  local body = request.arguments
  log:debug('run_in_terminal', body)
  local settings = dap().defaults[lsession.config.type]
  if body.kind == 'external' or (settings.force_external_terminal and settings.external_terminal) then
    local terminal = settings.external_terminal
    if not terminal then
      utils.notify('Requested external terminal, but none configured. Fallback to integratedTerminal', vim.log.levels.WARN)
    else
      local handle, pid = launch_external_terminal(body.env, terminal, body.args, body.cwd)
      if not handle then
        utils.notify('Could not launch terminal ' .. terminal.command, vim.log.levels.ERROR)
      end
      lsession:response(request, {
        success = handle ~= nil;
        body = { processId = pid; };
      })
      return
    end
  end
  local cur_buf = api.nvim_get_current_buf()
  local terminal_buf, terminal_win = terminals.acquire(
    settings.terminal_win_cmd,
    lsession.config,
    lsession.filetype
  )
  pcall(api.nvim_buf_del_keymap, terminal_buf, "t", "<CR>")
  local path = vim.bo[cur_buf].path
  if path and path ~= "" then
    vim.bo[terminal_buf].path = path
  end

  local jobid
  lsession.term_buf = terminal_buf
  vim.api.nvim_buf_call(terminal_buf, function()
    ---@diagnostic disable-next-line: deprecated
    local termopen = vim.fn.has("nvim-0.11") == 1 and vim.fn.jobstart or vim.fn.termopen
    jobid = termopen(body.args, {
      env = next(body.env or {}) and body.env or vim.empty_dict(),
      cwd = (body.cwd and body.cwd ~= '') and body.cwd or nil,
      height = terminal_win and api.nvim_win_get_height(terminal_win) or math.ceil(vim.o.lines / 2),
      width = terminal_win and api.nvim_win_get_width(terminal_win) or vim.o.columns,
      term = vim.fn.has("nvim-0.11") == 1 and true or nil,
      on_exit = function()
        terminals.release(terminal_buf)
      end
    })
  end)

  local terminal_buf_name = "[dap-terminal] " .. (lsession.config.name or body.args[1])
  local terminal_name_ok = pcall(api.nvim_buf_set_name, terminal_buf, terminal_buf_name)
  if not terminal_name_ok then
    log:warn(terminal_buf_name .. " is not a valid buffer name")
    api.nvim_buf_set_name(terminal_buf, "[dap-terminal] dap-" .. tostring(lsession.id))
  end

  if settings.focus_terminal then
    for _, win in pairs(api.nvim_tabpage_list_wins(0)) do
      if api.nvim_win_get_buf(win) == terminal_buf then
        api.nvim_set_current_win(win)
        break
      end
    end
  end
  if jobid == 0 or jobid == -1 then
    log:error('Could not spawn terminal', jobid, request)
    lsession:response(request, {
      success = false;
      message = 'Could not spawn terminal';
    })
  else
    lsession:response(request, {
      success = true;
      body = {
        processId = vim.fn.jobpid(jobid);
      };
    })
  end
end


function Session:event_initialized()
  local function on_done()
    if self.capabilities.supportsConfigurationDoneRequest then
      self:request('configurationDone', nil, function(err1, _)
        if err1 then
          utils.notify(tostring(err1), vim.log.levels.ERROR)
        end
        self.initialized = true
      end)
    else
      self.initialized = true
    end
  end

  local bps = breakpoints.get()
  self:set_breakpoints(bps, function()
    if self.capabilities.exceptionBreakpointFilters then
      self:set_exception_breakpoints(dap().defaults[self.config.type].exception_breakpoints, nil, on_done)
    else
      on_done()
    end
  end)
end


---@param thread_id number
---@param bufnr integer
---@param frame dap.StackFrame
function Session:_show_exception_info(thread_id, bufnr, frame)
  if not self.capabilities.supportsExceptionInfoRequest then
    return
  end
  local err, response = self:request('exceptionInfo', {threadId = thread_id})
  if err then
    utils.notify('Error getting exception info: ' .. tostring(err), vim.log.levels.ERROR)
  end
  if not response then
    return
  end
  local msg_parts = {}
  local exception_type = response.details and response.details.typeName
  local of_type = exception_type and ' of type '..exception_type or ''
  table.insert(msg_parts, ('Thread stopped due to exception'..of_type..' ('..response.breakMode..')'))
  if response.description then
    table.insert(msg_parts, ('Description: '..response.description))
  end
  local details = response.details or {}
  if details.stackTrace then
    table.insert(msg_parts, "Stack trace:")
    table.insert(msg_parts, details.stackTrace)
  end
  if details.innerException then
    table.insert(msg_parts, "Inner Exceptions:")
    for _, e in pairs(details.innerException) do
      table.insert(msg_parts, vim.inspect(e))
    end
  end
  vim.diagnostic.set(self.ns, bufnr, {
    {
      bufnr = bufnr,
      lnum = frame.line - 1,
      end_lnum = frame.endLine and (frame.endLine - 1) or nil,
      col = frame.column and (frame.column - 1) or 0,
      end_col = frame.endColumn,
      severity = vim.diagnostic.severity.ERROR,
      message = table.concat(msg_parts, '\n'),
      source = 'nvim-dap',
    }
  })
end



---@param win integer
---@param line integer
---@param column integer
local function set_cursor(win, line, column)
  local ok, err = pcall(api.nvim_win_set_cursor, win, { line, column - 1 })
  if ok then
    local curbuf = api.nvim_get_current_buf()
    if vim.bo[curbuf].filetype ~= "dap-repl" then
      api.nvim_set_current_win(win)
    end
    api.nvim_win_call(win, function()
      api.nvim_command('normal! zv')
    end)
  else
    local msg = string.format(
      "Adapter reported frame in buf %d line %d:%d, but: %s. "
      .. "Ensure executable is up2date and if using a source mapping ensure it is correct",
      api.nvim_win_get_buf(win),
      line,
      column,
      err
    )
    utils.notify(msg, vim.log.levels.WARN)
  end
end


---@param bufnr number
---@param line number
---@param column number
---@param switchbuf string|fun(bufnr: integer, line: integer, column: integer):nil
---@param filetype string
---@return boolean
local function jump_to_location(bufnr, line, column, switchbuf, filetype)
  -- vscode-go sends columns with 0
  -- That would cause a "Column value outside range" error calling nvim_win_set_cursor
  -- nvim-dap says "columnsStartAt1 = true" on initialize :/
  if column == 0 then
    column = 1
  end
  local cur_buf = api.nvim_get_current_buf()
  if cur_buf == bufnr and api.nvim_win_get_cursor(0)[1] == line and column == 1 then
    -- A user might have positioned the cursor over a variable in anticipation of hitting a breakpoint
    -- Don't move the cursor to the beginning of the line if it's in the right place
    return true
  end

  local cur_win = api.nvim_get_current_win()
  local switchbuf_fn = {}

  function switchbuf_fn.uselast()
    local ok, is_source_buf = pcall(vim.api.nvim_buf_get_var, cur_buf, 'dap_source_buf')
    is_source_buf = ok and is_source_buf
    if vim.bo[cur_buf].buftype == '' or vim.bo[cur_buf].filetype == filetype or is_source_buf then
      api.nvim_win_set_buf(cur_win, bufnr)
      set_cursor(cur_win, line, column)
    else
      local win = vim.fn.win_getid(vim.fn.winnr('#'))
      if win then
        api.nvim_win_set_buf(win, bufnr)
        set_cursor(win, line, column)
      end
    end
    return true
  end

  function switchbuf_fn.usevisible()
    if api.nvim_win_get_buf(cur_win) == bufnr then
      local first = vim.fn.line("w0", cur_win)
      local last = vim.fn.line("w$", cur_win)
      if first <= line and line <= last then
        return true
      end
    end
    return false
  end

  function switchbuf_fn.useopen()
    if api.nvim_win_get_buf(cur_win) == bufnr then
      set_cursor(cur_win, line, column)
      return true
    end
    for _, win in ipairs(api.nvim_tabpage_list_wins(0)) do
      if api.nvim_win_get_buf(win) == bufnr then
        set_cursor(win, line, column)
        return true
      end
    end
    return false
  end

  function switchbuf_fn.usetab()
    if api.nvim_win_get_buf(cur_win) == bufnr then
      set_cursor(cur_win, line, column)
      return true
    end
    local tabs = {0,}
    vim.list_extend(tabs, api.nvim_list_tabpages())
    for _, tabpage in ipairs(tabs) do
      for _, win in ipairs(api.nvim_tabpage_list_wins(tabpage)) do
        if api.nvim_win_get_buf(win) == bufnr then
          api.nvim_set_current_tabpage(tabpage)
          set_cursor(win, line, column)
          return true
        end
      end
    end
    return false
  end

  function switchbuf_fn.split()
    vim.cmd('split ' .. api.nvim_buf_get_name(bufnr))
    set_cursor(0, line, column)
    return true
  end

  function switchbuf_fn.vsplit()
    vim.cmd('vsplit ' .. api.nvim_buf_get_name(bufnr))
    set_cursor(0, line, column)
    return true
  end

  function switchbuf_fn.newtab()
    vim.cmd('tabnew ' .. api.nvim_buf_get_name(bufnr))
    set_cursor(0, line, column)
    return true
  end

  if type(switchbuf) == "string" and switchbuf:find('usetab') then
    switchbuf_fn.useopen = switchbuf_fn.usetab
  end

  if type(switchbuf) == "string" and switchbuf:find('newtab') then
    switchbuf_fn.vsplit = switchbuf_fn.newtab
    switchbuf_fn.split = switchbuf_fn.newtab
  end

  if type(switchbuf) == "function" then
    switchbuf(bufnr, line, column)
    return true
  end

  local opts = vim.split(switchbuf, ',', { plain = true })
  for _, opt in pairs(opts) do
    local fn = switchbuf_fn[opt]
    if fn and fn() then
      return true
    end
  end
  utils.notify(
    'Stopped at line ' .. line .. ' but `switchbuf` setting prevented jump to location. Target buffer ' .. bufnr .. ' not open in any window?',
    vim.log.levels.WARN
  )
  return false
end


--- Get the bufnr for a frame.
--- Might load source as a side effect if frame.source has sourceReference ~= 0
--- Must be called in a coroutine
---
---@param session dap.Session
---@param source dap.Source?
---@return number|nil
local function source_to_bufnr(session, source)
  if not source then
    return nil
  end
  local source_ref = source.sourceReference
  if not source_ref or source_ref == 0 then
    if not source.path then
      return nil
    end
    local scheme = source.path:match('^([a-z]+)://.*')
    if scheme then
      return vim.uri_to_bufnr(source.path)
    else
      return vim.uri_to_bufnr(vim.uri_from_fname(source.path))
    end
  end
  local fname = string.format(
    "dap-src://%d/%d/%s",
    session.id,
    source_ref,
    source.path or ""
  )
  return vim.uri_to_bufnr(fname)
end


---@param session dap.Session
---@param frame dap.StackFrame
---@param preserve_focus_hint boolean
---@param stopped nil|dap.StoppedEvent
---@return boolean
local function jump_to_frame(session, frame, preserve_focus_hint, stopped)
  local source = frame.source
  if not source then
    utils.notify('Source missing, cannot jump to frame: ' .. frame.name, vim.log.levels.INFO)
    return false
  end
  vim.fn.sign_unplace(session.sign_group)
  if preserve_focus_hint or frame.line < 0 then
    return false
  end
  local bufnr = source_to_bufnr(session, frame.source)
  if not bufnr then
    utils.notify('Source missing, cannot jump to frame: ' .. frame.name, vim.log.levels.INFO)
    return false
  end
  vim.fn.bufload(bufnr)
  vim.bo[bufnr].buflisted = true
  local ok, failure = pcall(vim.fn.sign_place, 0, session.sign_group, 'DapStopped', bufnr, { lnum = frame.line; priority = 22 })
  if not ok then
    utils.notify(tostring(failure), vim.log.levels.ERROR)
  end
  local switchbuf = defaults(session).switchbuf or vim.o.switchbuf or 'uselast'
  local jumped = jump_to_location(bufnr, frame.line, frame.column, switchbuf, session.filetype)
  if stopped and stopped.reason == 'exception' then
    session:_show_exception_info(stopped.threadId, bufnr, frame)
  end
  return jumped
end


--- Request a source
---@param source dap.Source
---@param cb fun(err: dap.ErrorResponse?, buf: integer?) the buffer will have the contents of the source
---@deprecated Open a buffer named "dap-src://<session-id>/<source-ref>/<source-path>" instead
function Session:source(source, cb)
  assert(source, 'source is required')
  assert(source.sourceReference, 'sourceReference is required')
  assert(source.sourceReference ~= 0, 'sourceReference must not be 0')
  local params = {
    source = source,
    sourceReference = source.sourceReference
  }

  ---@param err dap.ErrorResponse
  ---@param response dap.SourceResponse
  local function on_source(err, response)
    if err then
      cb(err, nil)
      return
    end
    local buf = api.nvim_create_buf(false, true)
    api.nvim_buf_set_var(buf, 'dap_source_buf', true)
    local adapter_options = self.adapter.options or {}
    local ft = mime_to_filetype[response.mimeType] or adapter_options.source_filetype
    if ft then
      vim.bo[buf].filetype = ft
    end
    api.nvim_buf_set_lines(buf, 0, -1, false, vim.split(response.content, '\n'))
    if not ft and source.path and vim.filetype then
      pcall(api.nvim_buf_set_name, buf, source.path)
      local ok, filetype = pcall(vim.filetype.match, source.path, buf)
      if not ok then
        -- API changed
        ok, filetype = pcall(vim.filetype.match, { buf = buf })
      end
      if ok and filetype then
        vim.bo[buf].filetype = filetype
      end
    end
    cb(nil, buf)
  end

  self:request('source', params, on_source)
end


---@param cb fun(err: dap.ErrorResponse?)
function Session:update_threads(cb)

  ---@param err dap.ErrorResponse?
  ---@param response dap.ThreadResponse?
  local on_threads = function(err, response)
    if err then
      cb(err)
      return
    end
    local threads = {}
    for _, thread in ipairs((response or {}).threads) do
      threads[thread.id] = thread
      local old_thread = self.threads[thread.id]
      if old_thread then
        local stopped = old_thread.stopped == nil and false or old_thread.stopped
        thread.stopped = stopped
        thread.frames = old_thread.frames
      end
    end
    self.threads = threads
    self.dirty.threads = false
    cb(nil)
  end

  self:request('threads', nil, on_threads)
end


---@param frames dap.StackFrame[]
---@return dap.StackFrame|nil
local function get_top_frame(frames)
  for _, frame in pairs(frames) do
    if frame.source then
      return frame
    end
  end
  local _, first = next(frames)
  return first
end


---@param stopped dap.StoppedEvent
function Session:event_stopped(stopped)
  require("dap.async").run(function()
    local co = coroutine.running()

    if self.dirty.threads or (stopped.threadId and self.threads[stopped.threadId] == nil) then
      local thread = {
        id = stopped.threadId,
        name = "Unknown",
        stopped = true
      }
      if thread.id then
        self.threads[thread.id] = thread
      end
      self:update_threads(coresume(co))
      local err = coroutine.yield()
      if err then
        utils.notify('Error retrieving threads: ' .. tostring(err), vim.log.levels.ERROR)
        return
      end
      if thread.stopped == false then
        log:debug("Thread resumed during stopped event handling", stopped, thread)
        return
      end
    end

    local should_jump = stopped.reason ~= 'pause' or stopped.allThreadsStopped

    -- Some debug adapters allow to continue/step via custom REPL commands (via evaluate)
    -- That by-passes `clear_running`, resulting in self.stopped_thread_id still being set
    -- Dont auto-continue if`threadId == self.stopped_thread_id`, but stop & jump
    if self.stopped_thread_id and self.stopped_thread_id ~= stopped.threadId and should_jump then
      if defaults(self).auto_continue_if_many_stopped then
        local thread = self.threads[self.stopped_thread_id]
        local thread_name = thread and thread.name or self.stopped_thread_id
        log:debug(
          'Received stopped event, but ' .. thread_name .. ' is already stopped. ' ..
          'Resuming newly stopped thread. ' ..
          'To disable this set the `auto_continue_if_many_stopped` option to false.')
        self:request('continue', { threadId = stopped.threadId }, function() end)
        return
      else
        -- Allow thread to stop, but don't jump to it because stepping
        -- interleaved between threads is confusing
        should_jump = false
      end
    end
    if should_jump then
      self.stopped_thread_id = stopped.threadId
    end

    if stopped.allThreadsStopped then
      progress.report('All threads stopped')
      for _, thread in pairs(self.threads) do
        thread.stopped = true
      end
    elseif not stopped.threadId then
      utils.notify('Stopped event received, but no threadId or allThreadsStopped', vim.log.levels.WARN)
    end

    if not stopped.threadId then
      return
    end
    progress.report('Thread stopped: ' .. stopped.threadId)
    local thread = self.threads[stopped.threadId]
    if not thread then
      thread = {
        id = stopped.threadId,
        name = "Unknown",
      }
      self.threads[stopped.threadId] = thread
    end
    thread.stopped = true

    ---@type dap.StackTraceArguments
    local params = {
      startFrame = 0,
      threadId = stopped.threadId
    }
    local err, response = self:request('stackTrace', params)
    if thread.stopped == false then
      log:debug("Debug adapter resumed during stopped event handling", thread, err)
      return
    end
    if err then
      utils.notify('Error retrieving stack traces: ' .. tostring(err), vim.log.levels.ERROR)
      return
    end
    assert(response, "Must have response if there is no error")
    local frames = response.stackFrames --[=[@as dap.StackFrame[]]=]
    thread.frames = frames
    local current_frame = get_top_frame(frames)
    if not current_frame then
      utils.notify('Debug adapter stopped at unavailable location', vim.log.levels.WARN)
      return
    end
    if should_jump then
      self.current_frame = current_frame
      local jumped = jump_to_frame(self, current_frame, stopped.preserveFocusHint, stopped)
      if jumped then
        progress.report('Stopped at line ' .. tostring(current_frame.line))
      end
      self:_request_scopes(current_frame)
    elseif stopped.reason == "exception" then
      local bufnr = source_to_bufnr(self, current_frame.source)
      if bufnr then
        self:_show_exception_info(stopped.threadId, bufnr, current_frame)
      end
    end
  end)
end


---@param body dap.TerminatedEvent
function Session:event_terminated(body)
  self:close()
  if body and body.restart ~= nil and body.restart ~= false then
    local config = vim.deepcopy(self.config)

    ---@diagnostic disable-next-line: inject-field
    config.__restart = body.restart
    -- This will set global session, is this still okay once startDebugging is implemented?
    dap().run(config, { filetype = self.filetype, new = true })
  end
end


---@param body dap.OutputEvent
function Session:event_output(body)
  local settings = defaults(self)
  local on_output = settings.on_output
  if on_output then
    on_output(self, body)
    return
  end
  if body.category == 'telemetry' then
    log:info('Telemetry', body.output)
  else
    repl.append(body.output, '$', { newline = false })
  end
end


---@param current_frame dap.StackFrame
function Session:_request_scopes(current_frame)
  local params = {
    frameId = current_frame.id
  }
  ---@param scope_resp dap.ScopesResponse?
  local function on_scopes(_, scope_resp)
    if not scope_resp then
      return
    end
    local scopes = scope_resp.scopes
    current_frame.scopes = scopes
    for _, scope in ipairs(scopes) do
      if not scope.expensive then

        ---@param resp dap.VariableResponse?
        local function on_variables(_, resp)
          scope.variables = resp and resp.variables or nil
          for _, v in ipairs(scope.variables or {}) do
            v.parent = scope
          end
        end

        local varparams = { variablesReference = scope.variablesReference }
        self:request('variables', varparams, on_variables)
      end
    end
  end
  self:request('scopes', params, on_scopes)
end


---@param session dap.Session
local function clear_running(session, thread_id)
  vim.fn.sign_unplace(session.sign_group)
  thread_id = thread_id or session.stopped_thread_id
  session.stopped_thread_id = nil
  local thread = session.threads[thread_id]
  if thread then
    thread.stopped = false
  end
end


--- Goto specified line (source and col are optional)
function Session:_goto(line, source, col)
  local frame = self.current_frame
  if not frame then
    utils.notify("No current frame available, cannot use goto", vim.log.levels.INFO)
    return
  end
  if not self.capabilities.supportsGotoTargetsRequest then
    utils.notify("Debug Adapter doesn't support GotoTargetRequest", vim.log.levels.INFO)
    return
  end
  coroutine.wrap(function()
    local err, response = self:request('gotoTargets',  {source = source or frame.source, line = line, col = col})
    if err then
      utils.notify('Error getting gotoTargets: ' .. tostring(err), vim.log.levels.ERROR)
      return
    end
    if not response or not response.targets then
      utils.notify("No goto targets available. Can't execute goto", vim.log.levels.INFO)
      return
    end
    local target = ui().pick_if_many(
      response.targets,
      'goto target> ',
      function(target) return target.label end
    )
    if not target then
      return
    end
    local stopped_thread_id = self.stopped_thread_id
    local params = {threadId = stopped_thread_id, targetId = target.id }
    local thread = self.threads[stopped_thread_id]
    clear_running(self, stopped_thread_id)
    local goto_err = self:request('goto', params)
    if goto_err then
      self.stopped_thread_id = stopped_thread_id
      if thread then
        thread.stopped = true
      end
      utils.notify('Error executing goto: ' .. tostring(goto_err), vim.log.levels.ERROR)
    end
  end)()
end


do
  local function notify_if_missing_capability(bps, capabilities)
    for _, bp in pairs(bps) do
      if non_empty(bp.condition) and not capabilities.supportsConditionalBreakpoints then
        utils.notify("Debug adapter doesn't support breakpoints with conditions", vim.log.levels.WARN)
      end
      if non_empty(bp.hitCondition) and not capabilities.supportsHitConditionalBreakpoints then
        utils.notify("Debug adapter doesn't support breakpoints with hit conditions", vim.log.levels.WARN)
      end
      if non_empty(bp.logMessage) and not capabilities.supportsLogPoints then
        utils.notify("Debug adapter doesn't support log points", vim.log.levels.WARN)
      end
    end
  end

  ---@param args vim.api.keyset.create_autocmd.callback_args
  local function remove_breakpoints(args)
    local session = dap().session()
    if session then
      session:set_breakpoints({[args.buf] = {}})
    end
    return true
  end

  function Session:set_breakpoints(bps, on_done)
    local num_requests = vim.tbl_count(bps)
    if num_requests == 0 then
      if on_done then
        on_done()
      end
      return
    end
    for bufnr, buf_bps in pairs(bps) do
      notify_if_missing_capability(buf_bps, self.capabilities)
      if non_empty(buf_bps) then
        local group = "dap-bps-del-" .. tostring(bufnr)
        api.nvim_create_autocmd("BufWipeout", {
          group = api.nvim_create_augroup(group, { clear = true }),
          buffer = bufnr,
          callback = remove_breakpoints,
        })
      end
      local path = api.nvim_buf_get_name(bufnr)
      ---@type dap.SetBreakpointsArguments
      local payload = {
        source = {
          path = path;
          name = vim.fn.fnamemodify(path, ':t')
        };
        sourceModified = false;
        breakpoints = vim.tbl_map(
          function(bp)
            -- trim extra information like the state
            return {
              line = bp.line,
              column = bp.column,
              condition = bp.condition,
              hitCondition = bp.hitCondition,
              logMessage = bp.logMessage,
            }
          end,
          buf_bps
        ),
        lines = vim.tbl_map(function(x) return x.line end, buf_bps);
      }
      ---@param err1 dap.ErrorResponse
      ---@param resp dap.SetBreakpointsResponse
      local function on_response(err1, resp)
        if err1 then
          utils.notify('Error setting breakpoints: ' .. tostring(err1), vim.log.levels.ERROR)
        elseif resp then
          for _, bp in pairs(resp.breakpoints) do
            breakpoints.set_state(bufnr, bp)
            if not bp.verified then
              log:info('Breakpoint unverified', bp)
            end
          end
        end
        num_requests = num_requests - 1
        if num_requests == 0 and on_done then
          on_done()
        end
      end
      self:request('setBreakpoints', payload, on_response)
    end
  end
end

function Session:set_exception_breakpoints(filters, exceptionOptions, on_done)
  if not self.capabilities.exceptionBreakpointFilters then
    utils.notify("Debug adapter doesn't support exception breakpoints", vim.log.levels.INFO)
    return
  end

  if filters == 'default' then
    local default_filters = {}
    for _, f in pairs(self.capabilities.exceptionBreakpointFilters) do
      if f.default then
        table.insert(default_filters, f.filter)
      end
    end
    filters = default_filters
  end

  if not filters then
    local possible_filters = {}
    for _, f in ipairs(self.capabilities.exceptionBreakpointFilters) do
      table.insert(possible_filters, f.filter)
    end
    ---@diagnostic disable-next-line: redundant-parameter, param-type-mismatch
    filters = vim.split(vim.fn.input("Exception breakpoint filters: ", table.concat(possible_filters, ' ')), ' ')
  end

  if exceptionOptions and not self.capabilities.supportsExceptionOptions then
    utils.notify('Debug adapter does not support ExceptionOptions', vim.log.levels.INFO)
    return
  end

  -- setExceptionBreakpoints (https://microsoft.github.io/debug-adapter-protocol/specification#Requests_SetExceptionBreakpoints)
  --- filters: string[]
  --- exceptionOptions: exceptionOptions?: ExceptionOptions[] (https://microsoft.github.io/debug-adapter-protocol/specification#Types_ExceptionOptions)
  self:request(
    'setExceptionBreakpoints',
    { filters = filters, exceptionOptions = exceptionOptions },
    function(err, _)
      if err then
        utils.notify('Error setting exception breakpoints: ' .. tostring(err), vim.log.levels.ERROR)
      end
      if on_done then
        on_done()
      end
  end)
end


---@param listeners table<string, dap.RequestListener<any>|dap.EventListener<any>>
local function call_listener(listeners, ...)
  for key, listener in pairs(listeners) do
    local remove = listener(...)
    if remove then
      listeners[key] = nil
    end
  end
end


function Session:handle_body(body)
  local decoded = assert(json_decode(body), "Debug adapter must send JSON objects")
  log:debug(self.id, decoded)
  local listeners = dap().listeners
  if decoded.request_seq then
    local callback = self.message_callbacks[decoded.request_seq]
    local request = self.message_requests[decoded.request_seq]
    self.message_requests[decoded.request_seq] = nil
    self.message_callbacks[decoded.request_seq] = nil
    if not callback then
      log:error('No callback found. Did the debug adapter send duplicate responses?', decoded)
      return
    end
    local err = nil
    local response = nil
    if decoded.success then
      response = decoded.body
    else
      err = {
        message = decoded.message,
        body = decoded.body,
      }
      setmetatable(err, err_mt)
    end
    vim.schedule(function()
      local before = listeners.before[decoded.command]
      call_listener(before, self, err, response, request, decoded.request_seq)
      callback(err, response, decoded.request_seq)
      local after = listeners.after[decoded.command]
      call_listener(after, self, err, response, request, decoded.request_seq)
    end)
  elseif decoded.event then
    local callback_name = "event_" .. decoded.event
    local callback = self[callback_name]
    vim.schedule(function()
      local before = listeners.before[callback_name]
      call_listener(before, self, decoded.body)
      if callback then
        callback(self, decoded.body)
      end
      local after = listeners.after[callback_name]
      call_listener(after, self, decoded.body)
      if not callback and not next(before) and not next(after) then
        log:warn('No event handler for ', decoded)
      end
    end)
  elseif decoded.type == 'request' then
    local handler = self.handlers.reverse_requests[decoded.command]
    if handler then
      handler(self, decoded)
    else
      log:warn('No handler for reverse request', decoded)
    end
  else
    log:warn('Received unexpected message', decoded)
  end
end


---@param self dap.Session
local function start_debugging(self, request)
  local body = request.arguments --[[@as dap.StartDebuggingRequestArguments]]
  coroutine.wrap(function()
    local co = coroutine.running()
    local opts = {
      filetype = self.filetype
    }
    local config = body.configuration
    local adapter = dap().adapters[config.type or self.config.type]
    config.request = body.request

    if type(adapter) == "function" then
      adapter(coresume(co), config, self)
      adapter = coroutine.yield()
    end

    -- Prefer connecting to root server again if it is of type server and
    -- the new adapter would have an executable.
    -- Spawning a new executable is likely the wrong thing to do
    if self.adapter.type == "server" and adapter.executable then
      adapter = vim.deepcopy(self.adapter)
      ---@diagnostic disable-next-line: inject-field
      adapter.executable = nil
    end

    local expected_types = {"executable", "server"}
    if type(adapter) ~= "table" or not vim.tbl_contains(expected_types, adapter.type) then
      local msg = "Invalid adapter definition. Expected a table with type `executable` or `server`: "
      utils.notify(msg .. vim.inspect(adapter), vim.log.levels.ERROR)
      return
    end

    ---@param session dap.Session
    local function on_child_session(session)
      session.parent = self
      self.children[session.id] = session
      session.on_close['dap.session.child'] = function(s)
        if s.parent then
          s.parent.children[s.id] = nil
          s.parent = nil
        end
      end
      session:initialize(config)
      self:response(request, {success = true})
    end

    if adapter.type == "executable" then
      local session = Session.spawn(adapter, config, opts)
      if session then
        on_child_session(session)
      end
    elseif adapter.type == "server" then
      local session
      session = Session.connect(adapter, config, opts, function(err)
        if err then
          utils.notify(string.format(
            "Could not connect startDebugging child session %s:%s: %s",
            adapter.host or '127.0.0.1',
            adapter.port,
            err
          ), vim.log.levels.WARN)
        elseif session then
          on_child_session(session)
        end
      end)
    end
  end)()
end


local default_reverse_request_handlers = {
  runInTerminal = run_in_terminal,
  startDebugging = start_debugging,
}

local next_session_id = 1

---@param adapter dap.Adapter
---@param config dap.Configuration
---@param handle uv.uv_stream_t
---@return dap.Session
local function new_session(adapter, config, opts, handle)
  local handlers = {}
  handlers.after = opts.after
  handlers.reverse_requests = vim.tbl_extend(
    'error',
    default_reverse_request_handlers,
    adapter.reverse_request_handlers or {}
  )
  local ns = ns_pool.acquire()
  local state = {
    id = next_session_id,
    handlers = handlers;
    message_callbacks = {},
    message_requests = {},
    initialized = false,
    seq = 1,
    stopped_thread_id = nil,
    current_frame = nil,
    threads = {},
    adapter = vim.deepcopy(adapter),
    dirty = {},
    capabilities = {},
    filetype = opts.filetype or vim.bo.filetype,
    ns = ns,
    sign_group = 'dap-' .. tostring(ns),
    closed = false,
    on_close = {},
    children = {},
    handle = handle,
    client = {},
    config = config,
  }
  function state.client.write(line)
    state.handle:write(line)
  end

  function state.client.close(cb)
    cb = cb or function() end
    if state.handle:is_closing() then
      cb()
      return
    end
    state.handle:shutdown(function()
      state.handle:close()
      state.closed = true
      cb()
    end)
  end
  next_session_id = next_session_id + 1
  return setmetatable(state, session_mt)
end


local function get_free_port()
  local tcp = assert(uv.new_tcp(), "Must be able to create tcp client")
  tcp:bind('127.0.0.1', 0)
  local port = tcp:getsockname().port
  tcp:shutdown()
  tcp:close()
  return port
end


---@param code integer
---@param command string
---@param adapter_name string
---@return string
local function get_badexit_msg(code, command, adapter_name)
  return string.format(
    "command `%s` of adapter `%s` exited with %d. Run :DapShowLog to open logs",
    command,
    adapter_name,
    code
  )
end


---@param err string
---@param command string
---@param adapter_name string
---@return string
local function get_spawn_errmsg(err, command, adapter_name)
  if vim.startswith(err, "ENOENT") then
    return string.format(
      "Executable `%s` not found, fix the adapter definition for `%s` (%s)",
      command,
      adapter_name,
      err
    )
  elseif command == "" then
    return string.format("`command` of adapter `%s` must not be empty", adapter_name)
  else
    return string.format("Error running `%s` of `%s`: ", command, adapter_name, err)
  end
end


--- Spawn the executable or raise an error if the command doesn't start.
---
--- Adds a on_close hook on the session to terminate the executable once the
--- session closes.
---
---@param executable dap.ServerAdapterExecutable
---@param session dap.Session
local function spawn_server_executable(executable, session)
  local cmd = assert(executable.command, "executable of server adapter must have a `command` property")
  log:debug("Starting debug adapter server executable", executable)
  local stdout = assert(uv.new_pipe(false), "Must be able to create pipe")
  local stderr = assert(uv.new_pipe(false), "Must be able to create pipe")
  local opts = {
    stdio = {nil, stdout, stderr},
    args = executable.args or {},
    detached = utils.if_nil(executable.detached, true),
    cwd = executable.cwd,
  }
  local handle, pid_or_err
  local daplog = require("dap.log")
  local stdoutlog = daplog.create_logger("dap-" .. session.config.type .. "-stdout.log")
  local stderrlog = daplog.create_logger("dap-" .. session.config.type .. "-stderr.log")
  handle, pid_or_err = uv.spawn(cmd, opts, function(code)
    log:info('Process exit', cmd, code, pid_or_err)
    if handle then
      handle:close()
    end
    if code == 0 then
      stdoutlog:remove()
      stderrlog:remove()
    else
      stdoutlog:close()
      stderrlog:close()
      utils.notify(get_badexit_msg(code, cmd, session.config.type), vim.log.levels.WARN)
    end
  end)
  if not handle then
    stdout:close()
    stderr:close()
    utils.notify(get_spawn_errmsg(tostring(pid_or_err), cmd, session.config.type), vim.log.levels.ERROR)
    stdoutlog:remove()
    stderrlog:remove()
    return
  end
  local read_output = function(logger, pipe)
    return function(err, chunk)
      assert(not err, err)
      if chunk then
        logger:write(chunk)
      else
        pipe:close()
      end
    end
  end
  stderr:read_start(read_output(stderrlog, stderr))
  stdout:read_start(read_output(stdoutlog, stdout))

  local is_windows = vim.fn.has("win32")
  session.on_close["dap.server_executable"] = function()
    if not handle:is_closing() then
      if is_windows == 1 then
        handle:kill("sighup")
      else
        handle:kill("sigterm")
      end
    end
  end
end


---@param adapter dap.PipeAdapter
---@param opts? table
---@param config dap.Configuration
---@param on_connect fun(err?: string)
---@return dap.Session
function Session.pipe(adapter, config, opts, on_connect)
  local pipe = assert(uv.new_pipe(), "Must be able to create pipe")
  local session = new_session(adapter, config, opts or {}, pipe)

  local session_adapter = session.adapter
  ---@cast session_adapter dap.PipeAdapter
  adapter = session_adapter

  if adapter.executable then
    if adapter.pipe == "${pipe}" then
      local filepath = os.tmpname()
      os.remove(filepath)
      session.on_close["dap.server_executable_pipe"] = function()
        os.remove(filepath)
      end
      adapter.pipe = filepath
      if adapter.executable.args then
        local args = assert(adapter.executable.args)
        for idx, arg in pairs(args) do
          args[idx] = arg:gsub('${pipe}', filepath)
        end
      end
    end
    spawn_server_executable(adapter.executable, session)
    log:debug(
      "Debug adapter server executable started with pipe " .. adapter.pipe)
    -- The adapter should create the pipe

    local adapter_opts = adapter.options or {}
    local timeout = adapter_opts.timeout or 5000
    vim.wait(timeout, function()
      return uv.fs_stat(adapter.pipe) ~= nil
    end)
  end

  pipe:connect(adapter.pipe, function(err)
    if err then
      local msg = string.format("Couldn't connect to pipe %s: %s", adapter.pipe, err)
      utils.notify(msg, vim.log.levels.ERROR)
      session:close()
    else
      progress.report("Connected to " .. adapter.pipe)
      local handle_body = vim.schedule_wrap(function(body)
        session:handle_body(body)
      end)
      pipe:read_start(rpc.create_read_loop(handle_body, function()
        if not session.closed then
          session:close()
          utils.notify("Debug adapter disconnected", vim.log.levels.INFO)
        end
      end))
    end
    on_connect(err)
  end)
  return session
end


---@param adapter dap.ServerAdapter
---@param config dap.Configuration
function Session.connect(adapter, config, opts, on_connect)
  local client = assert(uv.new_tcp(), "Must be able to create TCP client")
  local session = new_session(adapter, config, opts or {}, client)

  local session_adapter = session.adapter
  ---@cast session_adapter dap.ServerAdapter
  adapter = session_adapter

  if adapter.executable then
    if adapter.port == "${port}" then
      local port = get_free_port()
      session.adapter = adapter
      adapter.port = port
      if adapter.executable.args then
        local args = assert(adapter.executable.args)
        for idx, arg in pairs(args) do
          args[idx] = arg:gsub('${port}', tostring(port))
        end
      end
    end
    spawn_server_executable(adapter.executable, session)
    log:debug(
      "Debug adapter server executable started, listening on " .. adapter.port)
  end

  log:debug('Connecting to debug adapter', adapter)
  local max_retries = (adapter.options or {}).max_retries or 14

  local host = adapter.host or '127.0.0.1'
  local on_addresses
  on_addresses = function(err, addresses, retry_count)
    if err or #addresses == 0 then
      err = err or ('Could not resolve ' .. host)
      session:close()
      on_connect(err)
      return
    end
    local address = addresses[1]
    local port = assert(tonumber(adapter.port), "adapter.port is required for server adapter")
    client:connect(address.addr, port, function(conn_err)
      if conn_err then
        retry_count = retry_count or 1
        if retry_count < max_retries then
          -- Possible luv bug? A second client:connect gets stuck
          -- Create new handle as workaround
          client:close()
          client = assert(uv.new_tcp(), "Must be able to create TCP client")
          ---@diagnostic disable-next-line: invisible
          session.handle = client
          local timer = assert(uv.new_timer(), "Must be able to create timer")
          timer:start(250, 0, function()
            timer:stop()
            timer:close()
            on_addresses(nil, addresses, retry_count + 1)
          end)
        else
          session:close()
          on_connect(conn_err)
        end
        return
      end
      local handle_body = vim.schedule_wrap(function(body)
        session:handle_body(body)
      end)
      client:read_start(rpc.create_read_loop(handle_body, function()
        if not session.closed then
          session:close()
          utils.notify('Debug adapter disconnected', vim.log.levels.INFO)
        end
      end))
      on_connect(nil)
    end)
  end
  -- getaddrinfo fails for some users with `bad argument #3 to 'getaddrinfo' (Invalid protocol hint)`
  -- It should generally work with luv 1.42.0 but some still get errors
  if uv.version() >= 76288 then
    ---@diagnostic disable-next-line: missing-fields
    local ok, err = pcall(uv.getaddrinfo, host, nil, { protocol = 'tcp' }, on_addresses)
    if not ok then
      log:warn(err)
      on_addresses(nil, { { addr = host }, })
    end
  else
    on_addresses(nil, { { addr = host }, })
  end
  return session
end


---@param adapter dap.ExecutableAdapter
---@param config dap.Configuration
---@param opts table|nil
---@return dap.Session?
function Session.spawn(adapter, config, opts)
  log:debug('Spawning debug adapter', adapter)

  local handle
  local pid_or_err
  local closed = false

  local function sigint(cb)
    if not handle or handle:is_closing() then
      cb()
      return
    end
    handle:kill("sigint")
    local timer = assert(uv.new_timer())
    local start = uv.hrtime()
    timer:start(0, 50, function()
      if handle:is_closing() then
        timer:stop()
        timer:close()
        handle = nil
        cb()
      elseif (uv.hrtime() - start) > 5000000000 then
        handle:kill("sigkill")
        timer:stop()
        timer:close()
        handle = nil
        cb()
      end
    end)
  end

  local stdin = assert(uv.new_pipe(false), "Must be able to create pipe")
  local stdout = assert(uv.new_pipe(false), "Must be able to create pipe")
  local stderr = assert(uv.new_pipe(false), "Must be able to create pipe")

  local function onexit(cb)
    if closed then
      return
    end
    cb = cb or function() end
    closed = true
    if stdin:is_closing() then
      sigint(cb)
    else
      stdin:close(function()
        sigint(cb)
      end)
    end
  end

  local options = adapter.options or {}
  local spawn_opts = {
    args = adapter.args;
    stdio = {stdin, stdout, stderr};
    cwd = options.cwd;
    env = options.env;
    detached = utils.if_nil(options.detached, true);
  }
  local session
  local stderrlog = require("dap.log").create_logger("dap-" .. config.type .. "-stderr.log")
  handle, pid_or_err = uv.spawn(adapter.command, spawn_opts, function(code)
    log:info('Process exit', adapter.command, code, pid_or_err)
    onexit()
    if code == 0 then
      stderrlog:remove()
    else
      stderrlog:close()
      utils.notify(get_badexit_msg(code, adapter.command, config.type), vim.log.levels.WARN)
    end
    if session and not session.closed then
      session:close()
    end
  end)
  if not handle then
    stdin:close()
    stdout:close()
    stderr:close()
    onexit()
    stderrlog:remove()
    local msg = get_spawn_errmsg(tostring(pid_or_err), adapter.command, config.type)
    vim.notify(msg, vim.log.levels.ERROR)
    return
  end
  session = new_session(adapter, config, opts or {}, stdin)
  session.client.close = onexit

  local function on_body(body)
    session:handle_body(body)
  end
  local function on_eof()
    stdout:close()
  end
  stdout:read_start(rpc.create_read_loop(vim.schedule_wrap(on_body), on_eof))
  stderr:read_start(function(err, chunk)
    assert(not err, err)
    if chunk then
      stderrlog:write(chunk)
    else
      stderr:close()
    end
  end)
  return session
end


local function pause_thread(session, thread_id, cb)
  assert(session, 'Cannot pause thread without active session')
  assert(thread_id, 'thread_id is required to pause thread')

  session:request('pause', { threadId = thread_id; }, function(err)
    if err then
      utils.notify('Error pausing: ' .. tostring(err), vim.log.levels.ERROR)
    else
      utils.notify('Thread paused ' .. thread_id, vim.log.levels.INFO)
      local thread = session.threads[thread_id]
      if thread then
        thread.stopped = true
      end
    end
    if cb then
      cb(err)
    end
  end)
end


function Session:_pause(thread_id, cb)
  if thread_id then
    pause_thread(self, thread_id, cb)
    return
  end
  if self.dirty.threads then
    self:update_threads(function(err)
      if err then
        utils.notify('Error requesting threads: ' .. tostring(err), vim.log.levels.ERROR)
        return
      end
      self:_pause(nil, cb)
    end)
    return
  end
  ui().pick_if_many(
    vim.tbl_values(self.threads),
    "Which thread?: ",
    function(t) return t.name end,
    function(thread)
      if not thread or not thread.id then
        utils.notify('No thread to stop. Not pausing...', vim.log.levels.INFO)
      else
        pause_thread(self, thread.id, cb)
      end
    end
  )
end


function Session:restart_frame()
  if not self.capabilities.supportsRestartFrame then
    utils.notify('Debug Adapter does not support restart frame', vim.log.levels.INFO)
    return
  end
  local frame = self.current_frame
  if not frame then
    local msg = 'Current frame not set. Debug adapter needs to be stopped at breakpoint to use restart frame'
    utils.notify(msg, vim.log.levels.INFO)
    return
  end
  coroutine.wrap(function()
    if frame.canRestart == false then
      local thread = self.threads[self.stopped_thread_id] or {}
      local frames = vim.tbl_filter(
        function(f) return f.canRestart == nil or f.canRestart == true end,
        thread.frames or {}
      )
      if not next(frames) then
        utils.notify("No frame available that can be restarted", vim.log.levels.WARN)
        return
      end
      frame = ui().pick_one(
        frames,
        "Can't restart current frame, pick another frame to restart: ",
        require('dap.entity').frames.render_item
      )
      if not frame then
        return
      end
    end
    clear_running(self)
    local err = self:request('restartFrame', { frameId = frame.id })
    if err then
      utils.notify('Error on restart_frame: ' .. tostring(err), vim.log.levels.ERROR)
    end
  end)()
end


---@param step "next"|"stepIn"|"stepOut"|"stepBack"|"continue"|"reverseContinue"
---@param params table|nil
function Session:_step(step, params)
  local count = vim.v.count1 - 1
  local function step_thread(thread_id)
    if count > 0 then
      local listeners = dap().listeners
      local clear_listeners = function()
        listeners.after.event_stopped['dap.step'] = nil
        listeners.after.event_terminated['dap.step'] = nil
        listeners.after.disconnect['dap.step'] = nil
      end
      listeners.after.event_stopped['dap.step'] = function()
        if count > 0 then
          count = count - 1
          step_thread(thread_id)
        else
          clear_listeners()
        end
      end
      listeners.after.event_terminated['dap.step'] = clear_listeners
      listeners.after.disconnect['dap.step'] = clear_listeners
    end
    params = params or {}
    params.threadId = thread_id
    if not params.granularity then
      params.granularity = dap().defaults[self.config.type].stepping_granularity
    end
    clear_running(self, thread_id)
    self:request(step, params, function(err)
      if err then
        utils.notify('Error on '.. step .. ': ' .. tostring(err), vim.log.levels.ERROR)
      end
      progress.report('Running')
    end)
  end

  if self.stopped_thread_id then
    step_thread(self.stopped_thread_id)
  else
    local paused_threads = vim.tbl_filter(
      function(t) return t.stopped end,
      vim.tbl_values(self.threads)
    )
    if not next(paused_threads) then
      utils.notify('No stopped threads. Cannot move', vim.log.levels.ERROR)
      return
    end
    ui().pick_if_many(
      paused_threads,
      "Select thread to step in> ",
      function(t) return t.name end,
      function(thread)
        if thread then
          step_thread(thread.id)
        end
      end
    )
  end
end


function Session:close()
  self.closed = true
  for _, on_close in pairs(self.on_close) do
    local ok, err = pcall(on_close, self)
    if not ok then
      log:warn(err)
    end
  end
  self.on_close = {}
  if self.handlers.after then
    local ok, err = pcall(self.handlers.after)
    if not ok then
      log:warn(err)
    end
    self.handlers.after = nil
  end
  vim.schedule(function()
    pcall(vim.fn.sign_unplace, self.sign_group)
    vim.diagnostic.reset(self.ns)
    ns_pool.release(self.ns)
  end)
  if log._file then
    log._file:write("\n")
    log._file:flush()
  end
  self.client.close(function()
    self.threads = {}
    self.message_callbacks = {}
    self.message_requests = {}
  end)
end


function Session:request_with_timeout(command, arguments, timeout_ms, callback)
  local cb_triggered = false
  local timed_out = false
  local function cb(err, response)
    if timed_out then
      return
    end
    cb_triggered = true
    if callback then
      callback(err, response)
    end
  end
  self:request(command, arguments, cb)
  local timer = assert(uv.new_timer(), "Must be able to create timer")
  timer:start(timeout_ms, 0, function()
    timer:stop()
    timer:close()
    timed_out = true
    if not cb_triggered then
      local err = { message = 'Request `' .. command .. '` timed out after ' .. timeout_ms .. 'ms' }
      if callback then
        vim.schedule(function()
          callback(err, nil)
        end)
      else
        utils.notify(err.message, vim.log.levels.INFO)
      end
    end
  end)
end


--- Send a request to the debug adapter
---
---@param command string command name
---@param arguments any? command arguments
---@param on_result fun(err: dap.ErrorResponse?, result: any)? response callback
---@return dap.ErrorResponse? err, any response # (if running in coroutine and on_response is empty)
---@overload fun(self: dap.Session, command: "evaluate", arguments: dap.EvaluateArguments, on_result: fun(err: dap.ErrorResponse?, result: dap.EvaluateResponse?)?):(dap.ErrorResponse?, dap.EvaluateResponse?)
---@overload fun(self: dap.Session, command: "variables", arguments: dap.VariablesArguments, on_result: fun(err: dap.ErrorResponse?, result: dap.VariableResponse?)?):(dap.ErrorResponse?, dap.VariableResponse?)
---@overload fun(self: dap.Session, command: "threads", arguments: nil, on_result: fun(err: dap.ErrorResponse?, result: dap.ThreadResponse?)?):(dap.ErrorResponse?, dap.ThreadResponse?)
---@overload fun(self: dap.Session, command: "stackTrace", arguments: dap.StackTraceArguments, on_result: fun(err: dap.ErrorResponse?, result: dap.StackTraceResponse?)?):(dap.ErrorResponse?, dap.StackTraceResponse?)
function Session:request(command, arguments, on_result)
  local payload = {
    seq = self.seq,
    type = 'request',
    command = command,
    arguments = arguments,
  }
  log:debug('request', payload)
  local current_seq = self.seq
  self.seq = self.seq + 1
  local co, is_main
  if not on_result then
    co, is_main = coroutine.running()
    if co and not is_main then
      on_result = coresume(co)
    else
      -- Assume missing callback is intentional.
      -- Prevent error logging in Session:handle_body
      on_result = function(_, _)
      end
    end
  end
  self.message_callbacks[current_seq] = on_result
  self.message_requests[current_seq] = arguments
  send_payload(self.client, payload)
  if co then
    return coroutine.yield()
  end
end


function Session:response(request, payload)
  payload.seq = self.seq
  self.seq = self.seq + 1
  payload.type = 'response'
  payload.request_seq = request.seq;
  payload.command = request.command;
  log:debug('response', payload)
  send_payload(self.client, payload)
end


--- Initialize the debug session
---@param config dap.Configuration
function Session:initialize(config)
  vim.schedule(repl.clear)
  local adapter_responded = false

  ---@param err0 dap.ErrorResponse?
  ---@param result dap.Capabilities?
  local function on_initialize(err0, result)
    if err0 then
      utils.notify('Could not initialize debug adapter: ' .. tostring(err0), vim.log.levels.ERROR)
      adapter_responded = true
      return
    end
    self.capabilities = vim.tbl_extend('force', self.capabilities, result or {})
    self:request(config.request, config, function(err)
      adapter_responded = true
      if err then
        utils.notify(string.format('Error on %s: %s', config.request, err), vim.log.levels.ERROR)
        self:close()
      end
    end)
  end
  local params = {
    clientID = 'neovim';
    clientName = 'neovim';
    adapterID = self.adapter.id or 'nvim-dap';
    pathFormat = 'path';
    columnsStartAt1 = true;
    linesStartAt1 = true;
    supportsRunInTerminalRequest = true;
    supportsVariableType = true;
    supportsProgressReporting = true,
    supportsStartDebuggingRequest = true,
    locale = os.getenv('LANG') or 'en_US';
  }
  self:request('initialize', params, on_initialize)
  local adapter = self.adapter
  local sec_to_wait = (adapter.options or {}).initialize_timeout_sec or 4
  local timer = assert(uv.new_timer(), "Must be able to create timer")
  timer:start(sec_to_wait * sec_to_ms, 0, function()
    timer:stop()
    timer:close()
    if not adapter_responded and not self.closed then
      vim.schedule(function()
        utils.notify(
          string.format(
            ("Debug adapter didn't respond. "
              .. "Either the adapter is slow (then wait and ignore this) "
              .. "or there is a problem with your adapter or `%s` configuration. Check the logs for errors (:help dap.set_log_level)"),
            config.type),
            vim.log.levels.WARN
          )
      end)
    end
  end)
end


---@param args string|dap.EvaluateArguments expression as string, or evaluate arguments
---@param fn fun(err?: dap.ErrorResponse, result?: dap.EvaluateResponse)
function Session:evaluate(args, fn)
  if type(args) == "string" then
    args = {
      expression = args,
      context = "repl"
    }
  end
  args.frameId = args.frameId or (self.current_frame or {}).id
  return self:request("evaluate", args, fn)
end


function Session:disconnect(opts, cb)
  opts = vim.tbl_extend('force', {
    restart = false,
    terminateDebuggee = nil;
  }, opts or {})
  local disconnect_timeout_sec = (self.adapter.options or {}).disconnect_timeout_sec or 3
  self:request_with_timeout('disconnect', opts, disconnect_timeout_sec * sec_to_ms, function(err, resp)
    self:close()
    log:info('Session closed due to disconnect')
    if cb then
      cb(err, resp)
    end
  end)
end


---@param frame? dap.StackFrame
function Session:_frame_set(frame)
  if not frame then
    return
  end
  self.current_frame = frame
  coroutine.wrap(function()
    local jumped = jump_to_frame(self, frame, false)
    if jumped then
      progress.report(string.format("Set frame: %s:%s:%s", frame.name, frame.line, frame.column))
    end
    self:_request_scopes(frame)
  end)()
end


function Session:_frame_delta(delta)
  if not self.stopped_thread_id then
    utils.notify('Cannot move frame if not stopped', vim.log.levels.ERROR)
    return
  end
  local frames = self.threads[self.stopped_thread_id].frames
  assert(frames, 'Stopped thread must have frames')
  local frameidx = index_of(frames, function(i)
    return i.id == self.current_frame.id
  end)
  assert(frameidx, 'id of current frame must be present in frames')

  frameidx = frameidx + delta
  if frameidx < 1 then
    frameidx = 1
    utils.notify("Can't move past first frame", vim.log.levels.INFO)
  elseif frameidx > #frames then
    frameidx = #frames
    utils.notify("Can't move past last frame", vim.log.levels.INFO)
  end
  self:_frame_set(frames[frameidx])
end


function Session.event_exited()
end

function Session.event_module()
end

function Session.event_process()
end

function Session.event_loadedSource()
end


---@param event dap.ThreadEvent
function Session:event_thread(event)
  if event.reason == 'exited' then
    self.threads[event.threadId] = nil
  else
    local thread = self.threads[event.threadId]
    if thread then
      thread.stopped = false
      if self.stopped_thread_id == thread.id then
        self.stopped_thread_id = nil
        self.current_frame = nil
      end
    else
      self.dirty.threads = true
      self.threads[event.threadId] = {
        id = event.threadId,
        name = 'Unknown'
      }
    end
  end
end


---@param event dap.ContinuedEvent
function Session:event_continued(event)
  if event.allThreadsContinued == nil or event.allThreadsContinued == true then
    for _, t in pairs(self.threads) do
      t.stopped = false
    end
    self.stopped_thread_id = nil
    self.current_frame = nil
    vim.fn.sign_unplace(self.sign_group)
  else
    if self.stopped_thread_id == event.threadId then
      self.stopped_thread_id = nil
      self.current_frame = nil
      vim.fn.sign_unplace(self.sign_group)
    end
    local thread = self.threads[event.threadId]
    if thread and thread.stopped then
      thread.stopped = false
    end
  end
end


---@param event dap.BreakpointEvent
function Session.event_breakpoint(session, event)
  if event.reason == 'changed' then
    local bp = event.breakpoint
    if bp.id then
      breakpoints.update(bp)
    end
  elseif event.reason == 'new' then
    local bp = event.breakpoint
    if bp.id then
      local bufnr = source_to_bufnr(session, bp.source)
      if bufnr then
        breakpoints.set({}, bufnr, bp.line)
        breakpoints.set_state(bufnr, bp)
      end
    end
  elseif event.reason == 'removed' then
    local bp = event.breakpoint
    if bp.id then
      breakpoints.remove_by_id(bp.id)
    end
  end
end


function Session:event_capabilities(body)
  self.capabilities = vim.tbl_extend('force', self.capabilities, body.capabilities)
end


---@param body dap.ProgressStartEvent
function Session.event_progressStart(_, body)
  if body.message then
    progress.report(body.title .. ': ' .. body.message)
  else
    progress.report(body.title)
  end
end

---@param body dap.ProgressUpdateEvent
function Session.event_progressUpdate(_, body)
  if body.message then
    progress.report(body.message)
  end
end

---@param body dap.ProgressEndEvent
function Session:event_progressEnd(body)
  if body.message then
    progress.report(body.message)
  else
    progress.report('Running: ' .. (self.config.name or '[No Name]'))
  end
end


return Session
```

## File: `lua/dap/ui.lua`
```
local api = vim.api
local utils = require('dap.utils')
local if_nil = utils.if_nil
local M = {}


---@param win integer
---@param opts table<string, any>?
function M.apply_winopts(win, opts)
  if not opts then
    return
  end
  assert(
    type(opts) == 'table',
    'winopts must be a table, not ' .. type(opts) .. ': ' .. vim.inspect(opts)
  )
  for k, v in pairs(opts) do
    if k == 'width' then
      api.nvim_win_set_width(win, v)
    elseif k == 'height' then
      api.nvim_win_set_height(win, v)
    elseif vim.tbl_contains({ 'border', 'title' }, k) then
      api.nvim_win_set_config(win, {[k]=v})
    else
      vim.wo[win][k] = v
    end
  end
end


--- Same as M.pick_one except that it skips the selection prompt if `items`
--  contains exactly one item.
function M.pick_if_many(items, prompt, label_fn, cb)
  if #items == 1 then
    if not cb then
      return items[1]
    else
      cb(items[1])
    end
  else
    return M.pick_one(items, prompt, label_fn, cb)
  end
end


function M.pick_one_sync(items, prompt, label_fn)
  local choices = {prompt}
  for i, item in ipairs(items) do
    table.insert(choices, string.format('%d: %s', i, label_fn(item)))
  end
  local choice = vim.fn.inputlist(choices)
  if choice < 1 or choice > #items then
    return nil
  end
  return items[choice]
end


function M.pick_one(items, prompt, label_fn, cb)
  local co
  if not cb then
    co = coroutine.running()
    if co then
      cb = function(item)
        coroutine.resume(co, item)
      end
    end
  end
  cb = vim.schedule_wrap(cb)
  if vim.ui then
    vim.ui.select(items, {
      prompt = prompt,
      format_item = label_fn,
    }, cb)
  else
    local result = M.pick_one_sync(items, prompt, label_fn)
    cb(result)
  end
  if co then
    return coroutine.yield()
  end
end


local function with_indent(indent, fn)
  local move_cols = function(hl_group)
    local end_col = hl_group[3] == -1 and -1 or hl_group[3] + indent
    return {hl_group[1], hl_group[2] + indent, end_col}
  end
  return function(...)
    local text, hl_groups = fn(...)
    return string.rep(' ', indent) .. text, vim.tbl_map(move_cols, hl_groups or {})
  end
end


function M.new_tree(opts)
  assert(opts.render_parent, 'opts for tree requires a `render_parent` function')
  assert(opts.get_children, 'opts for tree requires a `get_children` function')
  assert(opts.has_children, 'opts for tree requires a `has_children` function')
  local get_key = opts.get_key or function(x) return x end
  opts.fetch_children = opts.fetch_children or function(item, cb)
    cb(opts.get_children(item))
  end
  opts.render_child = opts.render_child or opts.render_parent
  local compute_actions = opts.compute_actions or function() return {} end
  local extra_context = opts.extra_context or {}
  local implicit_expand_action = if_nil(opts.implicit_expand_action, true)
  local is_lazy = opts.is_lazy or function(_) return false end
  local load_value = opts.load_value or function(_, _) assert(false, "load_value not implemented") end

  local self  -- forward reference

  -- tree supports to re-draw with new data while retaining previously
  -- expansion information.
  --
  -- Since the data is completely changed, the expansion information must be
  -- held separately.
  --
  -- The structure must supports constructs like this:
  --
  --         root
  --       /     \
  --      a      b
  --     /       \
  --    x        x
  --   / \
  --  aa bb
  --
  -- It must be possible to distinguish the two `x`
  -- This assumes that `get_key` within a level is unique and that it is
  -- deterministic between two `render` operations.
  local expanded_root = {}

  local function get_expanded(item)
    local ancestors = {}
    local parent = item
    while true do
      parent = parent.__parent
      if parent then
        table.insert(ancestors, parent.key)
      else
        break
      end
    end
    local expanded = expanded_root
    for i = #ancestors, 1, -1 do
      local parent_expanded = expanded[ancestors[i]]
      if parent_expanded then
        expanded = parent_expanded
      else
        break
      end
    end
    return expanded
  end

  local function set_expanded(item, value)
    local expanded = get_expanded(item)
    expanded[get_key(item)] = value
  end

  local function is_expanded(item)
    local expanded = get_expanded(item)
    return expanded[get_key(item)] ~= nil
  end

  local expand = function(layer, value, lnum, context)
    set_expanded(value, {})
    opts.fetch_children(value, function(children)
      local ctx = {
        actions = context.actions,
        indent = context.indent + 2,
        compute_actions = context.compute_actions,
        tree = self,
      }
      ctx = vim.tbl_deep_extend('keep', ctx, extra_context)
      for _, child in pairs(children) do
        if opts.has_children(child) then
          child.__parent = { key = get_key(value), __parent = value.__parent }
        end
      end
      local render = with_indent(ctx.indent, opts.render_child)
      layer.render(children, render, ctx, lnum + 1)
    end)
  end

  local function eager_fetch_expanded_children(value, cb, ctx)
    ctx = ctx or { to_traverse = 1 }
    opts.fetch_children(value, function(children)
      ctx.to_traverse = ctx.to_traverse + #children
      for _, child in pairs(children) do
        if opts.has_children(child) then
          child.__parent = { key = get_key(value), __parent = value.__parent }
        end
        if is_expanded(child) then
          eager_fetch_expanded_children(child, cb, ctx)
        else
          ctx.to_traverse = ctx.to_traverse - 1
        end
      end
      ctx.to_traverse = ctx.to_traverse - 1
      if ctx.to_traverse == 0 then
        cb()
      end
    end)
  end

  local function render_all_expanded(layer, value, indent)
    indent = indent or 2
    local context = {
      actions = implicit_expand_action and { { label ='Expand', fn = self.toggle, }, } or {},
      indent = indent,
      compute_actions = compute_actions,
      tree = self,
    }
    context = vim.tbl_deep_extend('keep', context, extra_context)
    for _, child in pairs(opts.get_children(value)) do
      layer.render({child}, with_indent(indent, opts.render_child), context)
      if is_expanded(child) then
        render_all_expanded(layer, child, indent + 2)
      end
    end
  end

  local collapse = function(layer, value, lnum, context)
    if not is_expanded(value) then
      return
    end
    local num_vars = 1
    local collapse_child
    collapse_child = function(parent)
      num_vars = num_vars + 1
      if is_expanded(parent) then
        for _, child in pairs(opts.get_children(parent)) do
          collapse_child(child)
        end
        set_expanded(parent, nil)
      end
    end
    for _, child in ipairs(opts.get_children(value)) do
      collapse_child(child)
    end
    set_expanded(value, nil)
    layer.render({}, tostring, context, lnum + 1, lnum + num_vars)
  end

  self = {
    toggle = function(layer, value, lnum, context)
      if is_lazy(value) then
        load_value(value, function(var)
          local render = with_indent(context.indent, opts.render_child)
          layer.render({var}, render, context, lnum, lnum + 1)
        end)
      elseif is_expanded(value) then
        collapse(layer, value, lnum, context)
      elseif opts.has_children(value) then
        expand(layer, value, lnum, context)
      else
        utils.notify("No children on line " .. tostring(lnum) .. ". Can't expand", vim.log.levels.INFO)
      end
    end,

    render = function(layer, value, on_done, lnum, end_)
      layer.render({value}, opts.render_parent, nil, lnum, end_)
      if not opts.has_children(value) then
        if on_done then
          on_done()
        end
        return
      end
      if not is_expanded(value) then
        set_expanded(value, {})
      end
      eager_fetch_expanded_children(value, function()
        render_all_expanded(layer, value)
        if on_done then
          on_done()
        end
      end)
    end,
  }
  return self
end


--- Create a view that can be opened, closed and toggled.
--
-- The view manages a single buffer and a single window. Both are created when
-- the view is opened and destroyed when the view is closed.
--
-- Arguments passed to `view.open()` are forwarded to the `new_win` function
--
-- @param new_buf (view -> number): function to create a new buffer. Must return the bufnr
-- @param new_win (-> number): function to create a new window. Must return the winnr
-- @param opts A dictionary with `before_open` and `after_open` hooks.
function M.new_view(new_buf, new_win, opts)
  assert(new_buf, 'new_buf must not be nil')
  assert(new_win, 'new_win must not be nil')
  opts = opts or {}
  local self
  self = {
    buf = nil,
    win = nil,

    toggle = function(...)
      if not self.close({ mode = 'toggle' }) then
        self.open(...)
      end
    end,

    close = function(close_opts)
      close_opts = close_opts or {}
      local closed = false
      local win = self.win
      local buf = self.buf
      if win and api.nvim_win_is_valid(win) and api.nvim_win_get_buf(win) == buf then
        api.nvim_win_close(win, true)
        self.win = nil
        closed = true
      end
      local hide = close_opts.mode == 'toggle'
      if buf and not hide then
        pcall(api.nvim_buf_delete, buf, {force=true})
        self.buf = nil
      end
      return closed
    end,

    ---@return integer
    _init_buf = function()
      if self.buf then
        return self.buf
      end
      local buf = new_buf(self)
      assert(buf, 'The `new_buf` function is supposed to return a buffer')
      api.nvim_buf_attach(buf, false, { on_detach = function() self.buf = nil end })
      self.buf = buf
      return buf
    end,

    open = function(...)
      local win = self.win
      local before_open_result
      if opts.before_open then
        before_open_result = opts.before_open(self, ...)
      end
      local buf = self._init_buf()
      if not win or not api.nvim_win_is_valid(win) then
        win = new_win(buf, ...)
      end
      api.nvim_win_set_buf(win, buf)

      -- Trigger filetype again to ensure ftplugin files can change window settings
      local ft = vim.bo[buf].filetype
      vim.bo[buf].filetype = ft

      self.buf = buf
      self.win = win
      if opts.after_open then
        opts.after_open(self, before_open_result, ...)
      end
      return buf, win
    end
  }
  return self
end


function M.trigger_actions(opts)
  opts = opts or {}
  local buf = api.nvim_get_current_buf()
  local layer = M.get_layer(buf)
  if not layer then return end
  local lnum, col = unpack(api.nvim_win_get_cursor(0))
  lnum = lnum - 1
  local info = layer.get(lnum, 0, col) or {}
  local context = info.context or {}
  local actions = {}
  vim.list_extend(actions, context.actions or {})
  if context.compute_actions then
    vim.list_extend(actions, context.compute_actions(info))
  end
  if opts.filter then
    local filter = (type(opts.filter) == 'function'
      and opts.filter
      or function(x) return x.label == opts.filter end
    )
    actions = vim.tbl_filter(filter, actions)
  end
  if #actions == 0 then
    utils.notify('No action possible on: ' .. api.nvim_buf_get_lines(buf, lnum, lnum + 1, true)[1], vim.log.levels.INFO)
    return
  end
  if opts.mode == 'first' then
    local action = actions[1]
    action.fn(layer, info.item, lnum, info.context)
    return
  end
  M.pick_if_many(
    actions,
    'Actions> ',
    function(x) return type(x.label) == 'string' and x.label or x.label(info.item) end,
    function(action)
      if action then
        action.fn(layer, info.item, lnum, info.context)
      end
    end
  )
end


---@type table<number, dap.ui.Layer>
local layers = {}

--- Return an existing layer
---
---@param buf integer
---@return nil|dap.ui.Layer
function M.get_layer(buf)
  return layers[buf]
end

---@class dap.ui.LineInfo
---@field mark_id number
---@field item any
---@field context table|nil


---@param buf integer
local function line_count(buf)
  if vim.bo[buf].buftype ~= "prompt" then
    return api.nvim_buf_line_count(buf)
  end
  if vim.fn.has("nvim-0.12") == 1 then
    local ok, mark = pcall(api.nvim_buf_get_mark, buf, ":")
    if ok then
      return mark[1] - 1
    end
  end
  return api.nvim_buf_line_count(buf) - 1
end

--- Returns a layer, creating it if it's missing.
---@param buf integer
---@return dap.ui.Layer
function M.layer(buf)
  assert(buf, 'Need a buffer to operate on')
  local layer = layers[buf]
  if layer then
    return layer
  end

  ---@type table<number, dap.ui.LineInfo>
  local marks = {}
  local ns = api.nvim_create_namespace('dap.ui_layer_' .. buf)
  local nshl = api.nvim_create_namespace('dap.ui_layer_hl_' .. buf)
  local remove_marks = function(extmarks)
    for _, mark in pairs(extmarks) do
      local mark_id = mark[1]
      marks[mark_id] = nil
      api.nvim_buf_del_extmark(buf, ns, mark_id)
    end
  end

  ---@class dap.ui.Layer
  layer = {
    buf = buf,
    __marks = marks,

    --- Render the items and associate each item to the rendered line
    ---  The item and context can then be retrieved using `.get(lnum)`
    ---
    ---  lines between start and end_ are replaced
    ---  If start == end_, new lines are inserted at the given position
    ---  If start == nil, appends to the end of the buffer
    ---
    ---@generic T
    ---@param xs T[]
    ---@param render_fn? fun(T):string
    ---@param context table|nil
    ---@param start nil|number 0-indexed
    ---@param end_ nil|number 0-indexed exclusive
    render = function(xs, render_fn, context, start, end_)
      if not api.nvim_buf_is_valid(buf) then
        return
      end
      local modifiable = vim.bo[buf].modifiable
      vim.bo[buf].modifiable = true
      if not start and not end_ then
        start = line_count(buf)
        -- Avoid inserting a new line at the end of the buffer
        -- The case of no lines and one empty line are ambiguous;
        -- set_lines(buf, 0, 0) would "preserve" the "empty buffer line" while set_lines(buf, 0, -1) replaces it
        -- Need to use regular end_ = start in other cases to support injecting lines in all other cases
        if start == 1 and (api.nvim_buf_get_lines(buf, 0, -1, true))[1] == "" then
          start = 0
          end_ = -1
        else
          end_ = start
        end
      else
        start = start or (line_count(buf) - 1)
        end_ = end_ or start
      end
      render_fn = render_fn or tostring
      if end_ > start then
        remove_marks(api.nvim_buf_get_extmarks(buf, ns, {start, 0}, {end_ - 1, -1}, {}))
      elseif end_ == -1 then
        remove_marks(api.nvim_buf_get_extmarks(buf, ns, {start, 0}, {-1, -1}, {}))
      end
      -- This is a dummy call to insert new lines in a region
      -- the loop below will add the actual values
      local lines = vim.tbl_map(function() return '' end, xs)
      api.nvim_buf_set_lines(buf, start, end_, true, lines)
      if start == -1 then
        start = line_count(buf) - #lines
      end

      for i = start, start + #lines - 1 do
        local item = xs[i + 1 - start]
        local text, hl_regions = render_fn(item)
        if not text then
          local debuginfo = debug.getinfo(render_fn)
          error(('render function must return a string, got nil instead. render_fn: '
            .. debuginfo.short_src .. ':' .. debuginfo.linedefined
            .. ' '
            .. vim.inspect(xs)
          ))
        end
        text = text:gsub('\n', '\\n')
        api.nvim_buf_set_lines(buf, i, i + 1, true, {text})
        if hl_regions then
          for _, hl_region in pairs(hl_regions) do
            api.nvim_buf_add_highlight(
              buf, nshl, hl_region[1], i, hl_region[2], hl_region[3])
          end
        end

        local end_col = math.max(0, #text - 1)
        local mark_id = api.nvim_buf_set_extmark(buf, ns, i, 0, {end_col=end_col})
        marks[mark_id] = { mark_id = mark_id, item = item, context = context }
      end
      vim.bo[buf].modifiable = modifiable
    end,

    --- Get the information associated with a line
    ---
    ---@param lnum number 0-indexed line number
    ---@param start_col nil|number
    ---@param end_col nil|number
    ---@return nil|dap.ui.LineInfo
    get = function(lnum, start_col, end_col)
      local line = api.nvim_buf_get_lines(buf, lnum, lnum + 1, true)[1]
      start_col = start_col or 0
      end_col = end_col or #line
      local start = {lnum, start_col}
      local end_ = {lnum, end_col}
      local extmarks = api.nvim_buf_get_extmarks(buf, ns, start, end_, {})
      if not extmarks or #extmarks == 0 then
        return
      end
      assert(#extmarks == 1, 'Expecting only a single mark per line and region: ' .. vim.inspect(extmarks))
      local extmark = extmarks[1]
      return marks[extmark[1]]
    end
  }
  layers[buf] = layer
  api.nvim_buf_attach(buf, false, { on_detach = function(_, b) layers[b] = nil end })
  return layer
end


return M
```

## File: `lua/dap/utils.lua`
```
local M = {}


---@param err dap.ErrorResponse
---@return string?
function M.fmt_error(err)
  local body = err.body or {}
  if body.error and body.error.showUser then
    local msg = body.error.format
    for key, val in pairs(body.error.variables or {}) do
      msg = msg:gsub('{' .. key .. '}', val)
    end
    return msg
  end
  return err.message
end


-- Group values (a list) into a dictionary.
--  `get_key`   is used to get the key from an element of values
--  `get_value` is used to set the value from an element of values and
--               defaults to the full element
---@deprecated
function M.to_dict(values, get_key, get_value)
  if vim.notify_once then
    vim.notify_once("dap.utils.to_dict is deprecated for removal in nvim-dap 0.10.0")
  end
  local rtn = {}
  get_value = get_value or function(v) return v end
  for _, v in pairs(values or {}) do
    rtn[get_key(v)] = get_value(v)
  end
  return rtn
end


---@param object? table|string
---@return boolean
function M.non_empty(object)
  if type(object) == "table" then
    return next(object) ~= nil
  end
  return object and #object > 0 or false
end


---@generic T
---@param items T[]
---@param predicate fun(items: T):boolean
---@result integer?
function M.index_of(items, predicate)
  for i, item in ipairs(items) do
    if predicate(item) then
      return i
    end
  end
  return nil
end


--- Return running processes as a list with { pid, name } tables.
---
--- Takes an optional `opts` table with the following options:
---
--- - filter string|fun: A lua pattern or function to filter the processes.
---                      If a function the parameter is a table with
---                      {pid: integer, name: string}
---                      and it must return a boolean.
---                      Matches are included.
---
--- <pre>
--- require("dap.utils").pick_process({ filter = "sway" })
--- </pre>
---
--- <pre>
--- require("dap.utils").pick_process({
---   filter = function(proc) return vim.endswith(proc.name, "sway") end
--- })
--- </pre>
---
---@param opts? {filter: string|(fun(proc: dap.utils.Proc): boolean)}
---
---@return dap.utils.Proc[]
function M.get_processes(opts)
  opts = opts or {}
  local is_windows = vim.fn.has('win32') == 1
  local separator = is_windows and ',' or ' \\+'
  local command = is_windows and {'tasklist', '/nh', '/fo', 'csv'} or {'ps', 'ah', '-U', os.getenv("USER")}
  -- output format for `tasklist /nh /fo` csv
  --    '"smss.exe","600","Services","0","1,036 K"'
  -- output format for `ps ah`
  --    " 107021 pts/4    Ss     0:00 /bin/zsh <args>"
  local get_pid = function (parts)
    if is_windows then
      return vim.fn.trim(parts[2], '"')
    else
      return parts[1]
    end
  end

  local get_process_name = function (parts)
    if is_windows then
      return vim.fn.trim(parts[1], '"')
    else
      return table.concat({unpack(parts, 5)}, ' ')
    end
  end

  local output = vim.fn.system(command)
  local lines = vim.split(output, '\n')
  local procs = {}

  local nvim_pid = vim.fn.getpid()
  for _, line in pairs(lines) do
    if line ~= "" then -- tasklist command outputs additional empty line in the end
      local parts = vim.fn.split(vim.fn.trim(line), separator)
      local pid, name = get_pid(parts), get_process_name(parts)
      pid = tonumber(pid)
      if pid and pid ~= nvim_pid then
        table.insert(procs, { pid = pid, name = name })
      end
    end
  end

  if opts.filter then
    local filter
    if type(opts.filter) == "string" then
      filter = function(proc)
        return proc.name:find(opts.filter)
      end
    elseif type(opts.filter) == "function" then
      filter = function(proc)
        return opts.filter(proc)
      end
    else
      error("opts.filter must be a string or a function")
    end
    procs = vim.tbl_filter(filter, procs)
  end

  return procs
end




--- Trim a process name to better fit into `columns`
---
---@param name string
---@param columns integer
---@param wordlimit integer
---@return string
local function trim_procname(name, columns, wordlimit)
  if #name <= columns then
    return name
  end

  local function trimpart(part, i)
    if #part <= wordlimit then
      return part
    end
    -- `/usr/bin/cmd` -> `cmd`
    part = part:gsub("(/?[^/]+/)", "")

    -- preserve command name in full length, but trim arguments if they exceed word limit
    if i > 1 and #part > wordlimit then
      return "‥" .. part:sub(#part - wordlimit)
    end
    return part
  end

  -- proc name can include arguments `foo --bar --baz`
  -- trim each element and drop trailing args if still too long
  local i = 0
  local parts = {}
  local len = 0
  for word in name:gmatch("[^%s]+") do
    i = i + 1
    local trimmed = trimpart(word, i)
    len = len + #trimmed
    if i > 1 and len > columns then
      table.insert(parts, "[‥]")
      break
    else
      table.insert(parts, trimmed)
    end
  end
  return i > 0 and table.concat(parts, " ") or trimpart(name, 1)
end

---@private
M._trim_procname = trim_procname


---@class dap.utils.Proc
---@field pid integer
---@field name string

---@class dap.utils.pick_process.Opts
---@field filter? string|fun(proc: dap.utils.Proc):boolean
---@field label? fun(proc: dap.utils.Proc): string
---@field prompt? string

--- Show a prompt to select a process pid and returns the pid on selection
--- Requires `ps ah -u $USER` on Linux/Mac and `tasklist /nh /fo csv` on windows.
--
--- Takes an optional `opts` table with the following options:
---
--- - filter string|fun: A lua pattern or function to filter the processes.
---                      If a function the parameter is a table with
---                      {pid: integer, name: string}
---                      and it must return a boolean.
---                      Matches are included.
---
--- - label         fun: A function to generate a custom label for the processes.
---                      If not provided, a default label is used.
--- - prompt     string: The title/prompt of pick process select.
---
--- <pre>
--- require("dap.utils").pick_process({ filter = "sway" })
--- </pre>
---
--- <pre>
--- require("dap.utils").pick_process({
---   filter = function(proc) return vim.endswith(proc.name, "sway") end
--- })
--- </pre>
---
--- <pre>
--- require("dap.utils").pick_process({
---   label = function(proc) return string.format("Process: %s (PID: %d)", proc.name, proc.pid) end
--- })
--- </pre>
---
---@param opts? dap.utils.pick_process.Opts
---@return integer|dap.Abort
function M.pick_process(opts)
  opts = opts or {}
  local cols = math.max(14, math.floor(vim.o.columns * 0.7))
  local wordlimit = math.max(10, math.floor(cols / 3))
  local label_fn = opts.label or function(proc)
    local name = trim_procname(proc.name, cols, wordlimit)
    return string.format("id=%d name=%s", proc.pid, name)
  end
  local procs = M.get_processes(opts)
  local co, ismain = coroutine.running()
  local ui = require("dap.ui")
  local pick = (co and not ismain) and ui.pick_one or ui.pick_one_sync
  local result = pick(procs, opts.prompt or "Select process: ", label_fn)
  return result and result.pid or require("dap").ABORT
end


---@param msg string
---@param log_level? integer
function M.notify(msg, log_level)
  if vim.in_fast_event() then
    vim.schedule(function()
      vim.notify(msg, log_level, {title = 'DAP'})
    end)
  else
    vim.notify(msg, log_level, {title = 'DAP'})
  end
end


---@generic T
---@param x T?
---@param default T
---@return T
function M.if_nil(x, default)
  return x == nil and default or x
end


---@param opts {filter?: string|(fun(name: string):boolean), executables?: boolean}
---@return string[]
local function get_files(path, opts)
  local filter = function(_) return true end
  if opts.filter then
    if type(opts.filter) == "string" then
      filter = function(filepath)
        return filepath:find(opts.filter)
      end
    elseif type(opts.filter) == "function" then
      filter = function(filepath)
        return opts.filter(filepath)
      end
    else
      error('opts.filter must be a string or a function')
    end
  end
  if opts.executables then
    local f = filter
    local uv = vim.uv or vim.loop
    if vim.fn.has("win32") == 1 then
      filter = function(filepath)
        if not f(filepath) then
          return false
        end
        local ext = vim.fn.fnamemodify(filepath, ":e")
        return vim.tbl_contains({".exe", ".bat", ".cmd", ".ps1", ".com"}, ext)
      end
    else
      local user_execute = tonumber("00100", 8)
      filter = function(filepath)
        if not f(filepath) then
          return false
        end
        local stat = uv.fs_stat(filepath)
        return stat and bit.band(stat.mode, user_execute) == user_execute or false
      end
    end
  end

  if vim.fs.dir then
    local files = {}
    for name, type in vim.fs.dir(path, { depth = 50 }) do
      if type == "file" then
        local filepath = vim.fs.joinpath(path, name)
        if filter(filepath) then
          table.insert(files, filepath)
        end
      end
    end
    return files
  end


  local cmd = {"find", path, "-type", "f"}
  if opts.executables then
    -- The order of options matters!
    table.insert(cmd, "-executable")
  end
  table.insert(cmd, "-follow")

  local output = vim.fn.system(cmd)
  return vim.tbl_filter(filter, vim.split(output, '\n'))
end


--- Show a prompt to select a file.
--- Returns the path to the selected file.
--- Requires nvim 0.10+ or a `find` executable
---
--- Takes an optional `opts` table with following options:
---
--- - filter string|fun: A lua pattern or function to filter the files.
---                      If a function the parameter is a string and it
---                      must return a boolean. Matches are included.
---
--- - executables boolean: Show only executables. Defaults to true
--- - path string: Path to search for files. Defaults to cwd
---
--- <pre>
--- require('dap.utils').pick_file({ filter = '.*%.py', executables = true })
--- </pre>
---@param opts? {filter?: string|(fun(name: string): boolean), executables?: boolean, path?: string}
---
---@return thread|string|dap.Abort
function M.pick_file(opts)
  opts = opts or {}
  local executables = opts.executables == nil and true or opts.executables
  local path = opts.path or vim.fn.getcwd()
  local files = get_files(path, {
    filter = opts.filter,
    executables = executables
  })
  local prompt = executables and "Select executable: " or "Select file: "
  local co, ismain = coroutine.running()
  local ui = require("dap.ui")
  local pick = (co and not ismain) and ui.pick_one or ui.pick_one_sync

  if not vim.endswith(path, "/") then
    path = path .. "/"
  end

  ---@param abspath string
  ---@return string
  local function relpath(abspath)
    local _, end_ = abspath:find(path)
    return end_ and abspath:sub(end_ + 1) or abspath
  end
  return pick(files, prompt, relpath) or require("dap").ABORT
end


--- Split an argument string on whitespace characters into a list,
--- except if the whitespace is contained within single or double quotes.
---
--- Leading and trailing whitespace is removed.
---
--- Examples:
---
--- ```lua
--- require("dap.utils").splitstr("hello world")
--- {"hello", "world"}
--- ```
---
--- ```lua
--- require("dap.utils").splitstr('a "quoted string" is preserved')
--- {"a", "quoted string", "is, "preserved"}
--- ```
---
--- Requires nvim 0.10+
---
--- @param str string
--- @return string[]
function M.splitstr(str)
  local lpeg = vim.lpeg
  local P, S, C = lpeg.P, lpeg.S, lpeg.C

  ---@param quotestr string
  ---@return vim.lpeg.Pattern
  local function qtext(quotestr)
    local quote = P(quotestr)
    local escaped_quote = P('\\') * quote
    return quote * C(((1 - P(quote)) + escaped_quote) ^ 0) * quote
  end
  str = str:match("^%s*(.*%S)")
  if not str or str == "" then
    return {}
  end

  local space = S(" \t\n\r")
  local unquoted = P('\\') * C(P(1)) + C(P(1) - space)
  local word = qtext('"') + qtext("'") + unquoted
  local element = lpeg.Cf(word ^ 1, function(acc, val) return acc .. val end)
  local p = lpeg.Ct(element * (space ^ 1 * element) ^ 0)
  return lpeg.match(p, str)
end


return M
```

## File: `lua/dap/ext/autocompl.lua`
```
local M = {}
local api = vim.api
local timer = nil


local function destroy_timer()
  if timer then
    timer:stop()
    timer:close()
    timer = nil
  end
end


local function trigger_completion(buf)
  destroy_timer()
  if api.nvim_get_current_buf() == buf then
    api.nvim_feedkeys(api.nvim_replace_termcodes('<C-x><C-o>', true, false, true), 'm', true)
  end
end


function M._InsertCharPre()
  if timer then
    return
  end
  if tonumber(vim.fn.pumvisible()) == 1 then
    return
  end
  local buf = api.nvim_get_current_buf()
  local char = api.nvim_get_vvar('char')
  local session = require('dap').session()
  local trigger_characters = ((session or {}).capabilities or {}).completionTriggerCharacters
  local triggers
  if trigger_characters and next(trigger_characters) then
    triggers = trigger_characters
  else
    triggers = {'.'}
  end
  if vim.tbl_contains(triggers, char) then
    timer = vim.loop.new_timer()
    timer:start(50, 0, vim.schedule_wrap(function()
      trigger_completion(buf)
    end))
  end
end


function M._InsertLeave()
  destroy_timer()
end


function M.attach(bufnr)
  bufnr = bufnr or api.nvim_get_current_buf()
  if api.nvim_create_autocmd then
    local group = api.nvim_create_augroup(("dap.ext.autocmpl-%d"):format(bufnr), { clear = true })
    api.nvim_create_autocmd("InsertCharPre", {
      group = group,
      buffer = bufnr,
      callback = function()
        pcall(M._InsertCharPre)
      end,
    })
    api.nvim_create_autocmd("InsertLeave", {
      group = group,
      buffer = bufnr,
      callback = destroy_timer
    })
  else
    vim.cmd(string.format([[
      augroup dap_autocomplete-%d
      au!
      autocmd InsertCharPre <buffer=%d> lua require('dap.ext.autocompl')._InsertCharPre()
      autocmd InsertLeave <buffer=%d> lua require('dap.ext.autocompl')._InsertLeave()
      augroup end
      ]],
      bufnr,
      bufnr,
      bufnr
    ))
  end
end


return M
```

## File: `lua/dap/ext/vscode.lua`
```
local dap = require('dap')
local notify = require('dap.utils').notify
local M = {}

M.json_decode = vim.json.decode
M.type_to_filetypes = {}


---@class dap.vscode.launch.Input
---@field id string
---@field type "promptString"|"pickString"
---@field description string
---@field default? string
---@field options string[]|{label: string, value: string}[]


---@param input dap.vscode.launch.Input
---@return function
local function create_input(input)
  if input.type == "promptString" then
    return function()
      local description = input.description or 'Input'
      if not vim.endswith(description, ': ') then
        description = description .. ': '
      end
      if vim.ui.input then
        local co = coroutine.running()
        local opts = {
          prompt = description,
          default = input.default or '',
        }
        vim.ui.input(opts, function(result)
          vim.schedule(function()
            coroutine.resume(co, result)
          end)
        end)
        return coroutine.yield()
      else
        return vim.fn.input(description, input.default or '')
      end
    end
  elseif input.type == "pickString" then
    return function()
      local options = assert(input.options, "input of type pickString must have an `options` property")
      local opts = {
        prompt = input.description,
        format_item = function(x)
          return x.label and x.label or x
        end,
      }
      local co = coroutine.running()
      vim.ui.select(options, opts, function(option)
        vim.schedule(function()
          local value = option and option.value or option
          coroutine.resume(co, value or (input.default or ''))
        end)
      end)
      return coroutine.yield()
    end
  else
    local msg = "Unsupported input type in vscode launch.json: " .. input.type
    notify(msg, vim.log.levels.WARN)
    return function()
      return "${input:" .. input.id .. "}"
    end
  end
end


---@param inputs dap.vscode.launch.Input[]
---@return table<string, function> inputs map from ${input:<id>} to function resolving the input value
local function create_inputs(inputs)
  local result = {}
  for _, input in ipairs(inputs) do
    local id = assert(input.id, "input must have a `id`")
    local key = "${input:" .. id .. "}"
    assert(input.type, "input must have a `type`")
    local fn = create_input(input)
    if fn then
      result[key] = fn
    end
  end
  return result
end


---@param inputs table<string, function>
---@param value any
---@param cache table<string, any>
local function apply_input(inputs, value, cache)
  if type(value) == "table" then
    local new_value = {}
    for k, v in pairs(value) do
      new_value[k] = apply_input(inputs, v, cache)
    end
    value = new_value
  end
  if type(value) ~= "string" then
    return value
  end

  local matches = string.gmatch(value, "${input:([%w_]+)}")
  for input_id in matches do
    local input_key = "${input:" .. input_id .. "}"
    local result = cache[input_key]
    if not result then
      local input = inputs[input_key]
      if not input then
        local msg = "No input with id `" .. input_id .. "` found in inputs"
        notify(msg, vim.log.levels.WARN)
      else
        result = input()
        cache[input_key] = result
      end
    end
    if result then
      value = value:gsub(input_key, result)
    end
  end
  return value
end


---@param config table<string, any>
---@param inputs table<string, function>
local function apply_inputs(config, inputs)
  local result = {}
  local cache = {}
  for key, value in pairs(config) do
    result[key] = apply_input(inputs, value, cache)
  end
  return result
end


--- Lift properties of a child table to top-level
local function lift(tbl, key)
  local child = tbl[key]
  if child then
    tbl[key] = nil
    return vim.tbl_extend('force', tbl, child)
  end
  return tbl
end


function M._load_json(jsonstr)
  local ok, data = pcall(M.json_decode, jsonstr, { skip_comments = true })
  if not ok then
    error("Error parsing launch.json: " .. data)
  end
  assert(type(data) == "table", "launch.json must contain a JSON object")
  local inputs = create_inputs(data.inputs or {})
  local has_inputs = next(inputs) ~= nil

  local sysname
  if vim.fn.has('linux') == 1 then
    sysname = 'linux'
  elseif vim.fn.has('mac') == 1 then
    sysname = 'osx'
  elseif vim.fn.has('win32') == 1 then
    sysname = 'windows'
  end

  local configs = {}
  for _, config in ipairs(data.configurations or {}) do
    config = lift(config, sysname)
    if (has_inputs) then
      config = setmetatable(config, {
        __call = function()
          local c = vim.deepcopy(config)
          return apply_inputs(c, inputs)
        end
      })
    end
    table.insert(configs, config)
  end
  return configs
end

---@param path string?
---@return dap.Configuration[]
function M.getconfigs(path)
  local resolved_path = path or (vim.fn.getcwd() .. '/.vscode/launch.json')
  if not vim.loop.fs_stat(resolved_path) then
    return {}
  end
  local contents
  if vim.fn.has("nvim-0.12") == 1 then
    local fp = io.open(resolved_path, "r")
    if fp then
      contents = fp:read("*a")
    else
      return {}
    end
  else
    local lines = {}
    for line in io.lines(resolved_path) do
      if not vim.startswith(vim.trim(line), '//') then
        table.insert(lines, line)
      end
    end
    contents = table.concat(lines, '\n')
  end
  return M._load_json(contents)
end


--- Extends dap.configurations with entries read from .vscode/launch.json
---@deprecated
function M.load_launchjs(path, type_to_filetypes)
  local msg = "dap.ext.vscode.load_launchjs is deprecated as it is no longer needed. ./.vscode/launch.json files are read automatically on-demand. See :help dap-providers"
  vim.notify_once(msg, vim.log.levels.WARN)
  type_to_filetypes = vim.tbl_extend('keep', type_to_filetypes or {}, M.type_to_filetypes)
  local configurations = M.getconfigs(path)

  assert(configurations, "launch.json must have a 'configurations' key")
  for _, config in ipairs(configurations) do
    assert(config.type, "Configuration in launch.json must have a 'type' key")
    assert(config.name, "Configuration in launch.json must have a 'name' key")
    local filetypes = type_to_filetypes[config.type] or { config.type, }
    for _, filetype in pairs(filetypes) do
      local dap_configurations = dap.configurations[filetype] or {}
      for i, dap_config in pairs(dap_configurations) do
        if dap_config.name == config.name then
          -- remove old value
          table.remove(dap_configurations, i)
        end
      end
      table.insert(dap_configurations, config)
      dap.configurations[filetype] = dap_configurations
    end
  end
end

return M
```

## File: `lua/dap/ui/widgets.lua`
```
local ui = require('dap.ui')
local utils = require('dap.utils')
local api = vim.api
local M = {}


local function set_default_bufopts(buf)
  vim.bo[buf].modifiable = false
  vim.bo[buf].buftype = "nofile"
  api.nvim_buf_set_keymap(
    buf, "n", "<CR>", "<Cmd>lua require('dap.ui').trigger_actions({ mode = 'first' })<CR>", {})
  api.nvim_buf_set_keymap(
    buf, "n", "a", "<Cmd>lua require('dap.ui').trigger_actions()<CR>", {})
  api.nvim_buf_set_keymap(
    buf, "n", "o", "<Cmd>lua require('dap.ui').trigger_actions()<CR>", {})
  api.nvim_buf_set_keymap(
    buf, "n", "<2-LeftMouse>", "<Cmd>lua require('dap.ui').trigger_actions()<CR>", {})
end


local function new_buf()
  local buf = api.nvim_create_buf(false, true)
  set_default_bufopts(buf)
  return buf
end


function M.new_cursor_anchored_float_win(buf)
  vim.bo[buf].bufhidden = "wipe"
  local border = vim.fn.exists('&winborder') == 1 and vim.o.winborder or 'single'
  local opts = vim.lsp.util.make_floating_popup_options(50, 30, {border = border})
  local win = api.nvim_open_win(buf, true, opts)
  if vim.fn.has("nvim-0.11") == 1 then
    vim.wo[win][0].scrolloff = 0
    vim.wo[win][0].wrap = false
  else
    vim.wo[win].scrolloff = 0
    vim.wo[win].wrap = false
  end
  vim.bo[buf].filetype = "dap-float"
  return win
end


function M.new_centered_float_win(buf)
  vim.bo[buf].bufhidden = "wipe"
  local columns = vim.o.columns
  local lines = vim.o.lines
  local width = math.floor(columns * 0.9)
  local height = math.floor(lines * 0.8)
  local border = vim.fn.exists('&winborder') == 1 and vim.o.winborder or 'single'
  local opts = {
    relative = 'editor',
    style = 'minimal',
    row = math.floor((lines - height) * 0.5),
    col = math.floor((columns - width) * 0.5),
    width = width,
    height = height,
    border = border,
  }
  local win = api.nvim_open_win(buf, true, opts)
  if vim.fn.has("nvim-0.11") == 1 then
    vim.wo[win][0].scrolloff = 0
    vim.wo[win][0].wrap = false
  else
    vim.wo[win].scrolloff = 0
    vim.wo[win].wrap = false
  end
  vim.bo[buf].filetype = "dap-float"
  return win
end


local function with_winopts(new_win, winopts)
  return function(...)
    local win = new_win(...)
    ui.apply_winopts(win, winopts)
    return win
  end
end


local function mk_sidebar_win_func(winopts, wincmd)
  return function()
    vim.cmd(wincmd or '30 vsplit')
    local win = api.nvim_get_current_win()
    vim.wo[win].number = false
    vim.wo[win].relativenumber = false
    vim.wo[win].statusline = ' '
    ui.apply_winopts(win, winopts)
    return win
  end
end


--- Decorates a `new_win` function, adding a hook that will cause the window to
-- be resized if the content changes.
function M.with_resize(new_win)
  return setmetatable({resize=true}, {
    __call = function(_, buf)
      return new_win(buf)
    end
  })
end


local function resize_window(win, buf)
  if not api.nvim_win_is_valid(win) then
    -- Could happen if the user moves the buffer into a new window
    return
  end
  local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
  local width = 0
  local height = #lines
  for _, line in pairs(lines) do
    width = math.max(width, #line)
  end
  local columns = vim.o.columns
  local max_win_width = math.floor(columns * 0.9)
  width = math.min(width, max_win_width)
  local max_win_height = vim.o.lines
  height = math.min(height, max_win_height)
  api.nvim_win_set_width(win, width)
  api.nvim_win_set_height(win, height)
end


local function resizing_layer(win, buf)
  local layer = ui.layer(buf)
  local orig_render = layer.render
  ---@diagnostic disable-next-line: inject-field
  layer.render = function(...)
    orig_render(...)
    if api.nvim_win_is_valid(win) and api.nvim_win_get_config(win).relative ~= '' then
      resize_window(win, buf)
    end
  end
  return layer
end


M.scopes = {
  refresh_listener = 'scopes',
  new_buf = function(view)
    local dap = require('dap')
    local function reset_tree()
      view.tree = nil
    end
    dap.listeners.after['event_terminated'][view] = reset_tree
    dap.listeners.after['event_exited'][view] = reset_tree
    local buf = new_buf()
    api.nvim_create_autocmd("TextYankPost", {
      buffer = buf,
      callback = function()
        require("dap._cmds").yank_evalname()
      end,
    })
    vim.bo[buf].tagfunc = "v:lua.require'dap'._tagfunc"
    api.nvim_buf_attach(buf, false, {
      on_detach = function()
        dap.listeners.after['event_terminated'][view] = nil
        dap.listeners.after['event_exited'][view] = nil
      end
    })
    api.nvim_buf_set_name(buf, 'dap-scopes-' .. tostring(buf))
    return buf
  end,
  render = function(view)
    local session = require('dap').session()
    local frame = session and session.current_frame or {}
    local tree = view.tree
    if not tree then
      local spec = vim.deepcopy(require('dap.entity').scope.tree_spec)
      spec.extra_context = { view = view }
      tree = ui.new_tree(spec)
      view.tree = tree
    end
    local layer = view.layer()
    local scopes = frame.scopes or {}
    local render
    render = function(idx, scope, replace)
      if not scope then
        return
      end

      tree.render(layer, scope, function()
        render(next(scopes, idx))
      end, replace and 0 or nil, replace and -1 or nil)
    end
    local idx, scope = next(scopes)
    render(idx, scope, true)
  end,
}


M.threads = {
  refresh_listener = 'event_thread',
  new_buf = function()
    local buf = new_buf()
    api.nvim_buf_set_name(buf, 'dap-threads-' .. tostring(buf))
    return buf
  end,
  render = function(view)
    local layer = view.layer()
    local session = require('dap').session()
    if not session then
      layer.render({'No active session'})
      return
    end

    ---@diagnostic disable-next-line: invisible
    if session.dirty.threads then
      session:update_threads(function()
        M.threads.render(view)
      end)
      return
    end

    local tree = view.tree
    if not tree then
      local spec = vim.deepcopy(require('dap.entity').threads.tree_spec)
      spec.extra_context = {
        view = view,
        refresh = view.refresh,
      }
      tree = ui.new_tree(spec)
      view.tree = tree
    end

    local root = {
      id = 0,
      name = 'Threads',
      threads = vim.tbl_values(session.threads)
    }
    tree.render(layer, root)
  end,
}


M.frames = {
  refresh_listener = 'scopes',
  new_buf = function()
    local buf = new_buf()
    api.nvim_buf_set_name(buf, 'dap-frames-' .. tostring(buf))
    return buf
  end,
  render = function(view)
    local session = require('dap').session()
    local layer = view.layer()
    if not session then
      layer.render({'No active session'})
      return
    end
    if not session.stopped_thread_id then
      layer.render({'Not stopped at any breakpoint. No frames available'})
      return
    end
    local thread = session.threads[session.stopped_thread_id]
    if not thread then
      local msg = string.format("Stopped thread (%d) not found. Can't display frames", session.stopped_thread_id)
      layer.render({msg})
      return
    end

    local frames = thread.frames
    require("dap.async").run(function()
      if not frames then
        local err, response = session:request("stackTrace", { threadId = thread.id })
        ---@cast response dap.StackTraceResponse
        if err or not response then
          layer.render({"Stopped thread has no frames"})
          return
        end
        frames = response.stackFrames
      end
      local context = {}
      context.actions = {
        {
          label = "Jump to frame",
          fn = function(_, frame)
            if session then
              local close = vim.bo.bufhidden == "wipe"
              session:_frame_set(frame)
              if close then
                view.close()
              end
            else
              utils.notify('Cannot navigate to frame without active session', vim.log.levels.INFO)
            end
          end
        },
      }
      local render_frame = require('dap.entity').frames.render_item
      layer.render(frames, render_frame, context)
    end)
  end
}


M.sessions = {
  refresh_listener = {
    'event_initialized',
    'event_terminated',
    'disconnect',
    'event_stopped'
  },
  new_buf = function()
    local buf = new_buf()
    api.nvim_buf_set_name(buf, 'dap-sessions-' .. tostring(buf))
    return buf
  end,
  render = function(view)
    local dap = require('dap')
    local sessions = dap.sessions()
    local layer = view.layer()
    local lsessions = {}

    local add
    add = function(s)
      table.insert(lsessions, s)
      for _, child in pairs(s.children) do
        add(child)
      end
    end
    for _, s in pairs(sessions) do
      add(s)
    end
    local context = {}
    context.actions = {
      {
        label = "Focus session",
        fn = function(_, s)
          local close = vim.bo.bufhidden == "wipe"
          if s then
            dap.set_session(s)
            view.refresh()
          end
          if close then
            view.close()
          end
        end
      }
    }
    local focused = dap.session()
    local render_session = function(s)
      local text = s.id .. ': ' .. s.config.name
      local parent = s.parent
      local num_parents = 0
      while parent ~= nil do
        parent = parent.parent
        num_parents = num_parents + 1
      end
      local prefix
      if focused and s.id == focused.id then
        prefix = "→ "
      else
        prefix = "  "
      end
      return prefix .. string.rep("  ", num_parents) .. text
    end
    layer.render({}, tostring, nil, 0, -1)
    layer.render(lsessions, render_session, context)
  end,
}


do

  ---@param scopes dap.Scope[]
  ---@param expression string
  ---@return dap.Variable?
  local function find_var(scopes, expression)
    for _, s in ipairs(scopes) do
      for _, var in ipairs(s.variables or {}) do
        if var.name == expression then
          return var
        end
      end
    end
    return nil
  end

  M.expression = {
    new_buf = function()
      local buf = new_buf()
      vim.bo[buf].tagfunc = "v:lua.require'dap'._tagfunc"
      api.nvim_create_autocmd("TextYankPost", {
        buffer = buf,
        callback = function()
          require("dap._cmds").yank_evalname()
        end,
      })
      return buf
    end,
    before_open = function(view)
      view.__expression = vim.fn.expand('<cexpr>')
    end,
    render = function(view, expr)
      local session = require('dap').session()
      local layer = view.layer()
      if not session then
        layer.render({'No active session'})
        return
      end
      local expression = expr or view.__expression
      local context = session.capabilities.supportsEvaluateForHovers and "hover" or "repl"
      local args = {
        expression = expression,
        context = context
      }
      local frame = session.current_frame or {}
      local scopes = frame.scopes or {}
      session:evaluate(args, function(err, resp)
        local spec = vim.deepcopy(require('dap.entity').variable.tree_spec)
        spec.extra_context = { view = view }
        if err then
          local variable = find_var(scopes, expression)
          if variable then
            local tree = ui.new_tree(spec)
            tree.render(view.layer(), variable)
          else
            local msg = "Error evaluating '" .. expression .. "':"
            layer.render({msg, "", tostring(err)})
          end
        elseif resp and resp.result then
          local attributes = (resp.presentationHint or {}).attributes or {}
          if resp.variablesReference > 0 or vim.tbl_contains(attributes, "rawString") then
            local tree = ui.new_tree(spec)
            tree.render(layer, resp)
          else
            local lines = vim.split(resp.result, "\n", { plain = true })
            layer.render(lines)
          end
        end
      end)
    end,
  }
end


function M.builder(widget)
  assert(widget, 'widget is required')
  local nwin
  local nbuf = widget.new_buf
  local hooks = {{widget.before_open, widget.after_open},}
  local builder = {}

  function builder.add_hooks(before_open, after_open)
    table.insert(hooks, {before_open, after_open})
    return builder
  end

  function builder.keep_focus()
    builder.add_hooks(
      function()
        return api.nvim_get_current_win()
      end,
      function(_, win)
        api.nvim_set_current_win(win)
      end
    )
    return builder
  end

  function builder.new_buf(val)
    assert(val and type(val) == "function", '`new_buf` must be a function')
    nbuf = val
    return builder
  end

  function builder.new_win(val)
    assert(val, '`new_win` must be a callable')
    nwin = val
    return builder
  end

  function builder.build()
    assert(nwin, '`new_win` function must be set')
    local before_open_results
    local view = ui.new_view(nbuf, nwin, {

      before_open = function(view)
        before_open_results = {}
        for _, hook in pairs(hooks) do
          local result = hook[1] and hook[1](view) or vim.NIL
          table.insert(before_open_results, result)
        end
      end,

      after_open = function(view, _, ...)
        for idx, hook in pairs(hooks) do
          if hook[2] then
            hook[2](view, before_open_results[idx])
          end
        end
        before_open_results = {}
        return widget.render(view, ...)
      end
    })

    view.layer = function()
      if type(nwin) == "table" and nwin.resize then
        return resizing_layer(view.win, view.buf)
      else
        return ui.layer(view.buf)
      end
    end

    view.refresh = function()
      local layer = view.layer()
      layer.render({}, tostring, nil, 0, -1)
      widget.render(view)
    end
    return view
  end
  return builder
end


---@param expr nil|string|fun():string
---@return string
local function eval_expression(expr)
  local mode = api.nvim_get_mode()
  if mode.mode == 'v' then
    -- [bufnum, lnum, col, off]; 1-indexed
    local start = vim.fn.getpos('v')
    local end_ = vim.fn.getpos('.')

    local start_row = start[2]
    local start_col = start[3]

    local end_row = end_[2]
    local end_col = end_[3]

    if start_row == end_row and end_col < start_col then
      end_col, start_col = start_col, end_col
    elseif end_row < start_row then
      start_row, end_row = end_row, start_row
      start_col, end_col = end_col, start_col
    end

    api.nvim_feedkeys(api.nvim_replace_termcodes('<ESC>', true, false, true), 'n', false)

    -- buf_get_text is 0-indexed; end-col is exclusive
    local lines = api.nvim_buf_get_text(0, start_row - 1, start_col - 1, end_row - 1, end_col, {})
    return table.concat(lines, '\n')
  end
  expr = expr or '<cexpr>'
  if type(expr) == "function" then
    return expr()
  else
    return vim.fn.expand(expr)
  end
end


---@param expr nil|string|fun():string
---@param winopts table<string, any>?
function M.hover(expr, winopts)
  local value = eval_expression(expr)
  local view = M.builder(M.expression)
    .new_win(M.with_resize(with_winopts(M.new_cursor_anchored_float_win, winopts)))
    .build()
  local buf = view.open(value)
  api.nvim_buf_set_name(buf, 'dap-hover-' .. tostring(buf) .. ': ' .. value)
  api.nvim_win_set_cursor(view.win, {1, 0})
  return view
end


function M.cursor_float(widget, winopts)
  local view = M.builder(widget)
    .new_win(M.with_resize(with_winopts(M.new_cursor_anchored_float_win, winopts)))
    .build()
  view.open()
  return view
end


function M.centered_float(widget, winopts)
  local view = M.builder(widget)
    .new_win(with_winopts(M.new_centered_float_win, winopts))
    .build()
  view.open()
  return view
end


--- View the value of the expression under the cursor in a preview window
---
---@param expr nil|string|fun():string
---@param opts? {listener?: string[]}
function M.preview(expr, opts)
  opts = opts or {}
  local value = eval_expression(expr)

  local function new_preview_buf()
    vim.cmd('pedit ' .. 'dap-preview: ' .. value)
    for _, win in pairs(api.nvim_list_wins()) do
      if vim.wo[win].previewwindow then
        local buf = api.nvim_win_get_buf(win)
        set_default_bufopts(buf)
        vim.bo[buf].bufhidden = 'delete'
        return buf
      end
    end
  end

  local function new_preview_win()
    -- Avoid pedit call if window is already open
    -- Otherwise on_detach is triggered
    for _, win in ipairs(api.nvim_list_wins()) do
      if vim.wo[win].previewwindow then
        return win
      end
    end
    vim.cmd('pedit ' .. 'dap-preview: ' .. value)
    for _, win in ipairs(api.nvim_list_wins()) do
      if vim.wo[win].previewwindow then
        return win
      end
    end
  end

  if opts.listener and next(opts.listener) then
    new_preview_buf = M.with_refresh(new_preview_buf, opts.listener)
  end
  local view = M.builder(M.expression)
    .new_buf(new_preview_buf)
    .new_win(new_preview_win)
    .build()
  view.open(value)
  view.__expression = value
  return view
end


--- Decorate a `new_buf` function so that it will register a
-- `dap.listeners.after[listener]` which will trigger a `view.refresh` call.
--
-- Use this if you want a widget to live-update.
---@param listener string|string[]
function M.with_refresh(new_buf_, listener)
  local listeners
  if type(listener) == "table" then
    listeners = listener
  else
    listeners = {listener}
  end
  return function(view)
    local dap = require('dap')
    for _, l in pairs(listeners) do
      dap.listeners.after[l][view] = view.refresh
    end
    local buf = new_buf_(view)
    api.nvim_buf_attach(buf, false, {
      on_detach = function()
        for _, l in pairs(listeners) do
          dap.listeners.after[l][view] = nil
        end
      end
    })
    return buf
  end
end


--- Open the given widget in a sidebar
--@param winopts with options that configure the window
--@param wincmd command used to create the sidebar
function M.sidebar(widget, winopts, wincmd)
  return M.builder(widget)
    .keep_focus()
    .new_win(mk_sidebar_win_func(winopts, wincmd))
    .new_buf(M.with_refresh(widget.new_buf, widget.refresh_listener or 'event_stopped'))
    .build()
end


---@param session dap.Session
---@param expr string
---@param max_level integer
local function get_var_lines(session, expr, max_level)
  local req_args = {
    expression = expr,
    context = "repl",
    frameId = (session.current_frame or {}).id
  }
  local eval_err, eval_result = session:request("evaluate", req_args)
  assert(not eval_err, vim.inspect(eval_err))

  local lines = {}
  local value = eval_result.result:gsub("\n", "\\n")
  table.insert(lines, value)

  local function add_children(ref, level)
    require("dap.progress").report("Fetching " .. tostring(ref))

    ---@type dap.VariablesArguments
    local vargs = {
      variablesReference = ref,
    }
    ---@type dap.ErrorResponse, dap.VariableResponse
    local err, result = session:request("variables", vargs)
    assert(not err, vim.inspect(err))
    for _, variable in ipairs(result.variables) do
      local val = variable.value:gsub("\n", "\\n")
      local indent = level * 2
      local line = string.rep(" ", indent) .. variable.name .. ": " .. val
      table.insert(lines, line)
      if level < max_level and variable.variablesReference > 0 then
        add_children(variable.variablesReference, level + 1)
      end
    end
  end

  if eval_result.variablesReference > 0 then
    add_children(eval_result.variablesReference, 0)
  end

  return lines
end


--- Generate a diff between two expressions
---
--- Opens a new tab with two windows and buffers in diff mode.
--- The diff is based on the lines of the variable tree's, expanded up to `max_level`
---
---@param expr1 string
---@param expr2 string
---@param max_level? integer default: 1
function M.diff_var(expr1, expr2, max_level)
  local dap = require("dap")
  local session = dap.session()
  if not session then
    utils.notify("No active session", vim.log.levels.INFO)
    return
  end
  max_level = max_level or 1
  require("dap.async").run(function()
    local lines1 = get_var_lines(session, expr1, max_level)
    local lines2 = get_var_lines(session, expr2, max_level)
    require("dap.progress").report("Diff operation done")
    require("dap.progress").report("Running: " .. session.config.name)
    vim.cmd.tabnew()
    local buf1 = api.nvim_get_current_buf()
    api.nvim_buf_set_lines(buf1, 0, -1, true, lines1)
    vim.bo[buf1].modified = false
    vim.bo[buf1].bufhidden = "wipe"
    vim.cmd.diffthis()

    vim.cmd.vnew()
    local buf2 = api.nvim_get_current_buf()
    api.nvim_buf_set_lines(buf2, 0, -1, true, lines2)
    vim.bo[buf2].modified = false
    vim.bo[buf2].bufhidden = "wipe"
    vim.cmd.diffthis()
  end)
end


return M
```

## File: `plugin/dap.lua`
```
local api = vim.api
if not api.nvim_create_user_command then
  return
end

local cmd = api.nvim_create_user_command
cmd('DapSetLogLevel',
  ---@param opts vim.api.keyset.create_user_command.command_args
  function(opts)
    require('dap').set_log_level(vim.trim(opts.args))
  end,
  {
    nargs = 1,
    complete = function()
      return vim.tbl_keys(require('dap.log').levels)
    end
  }
)
cmd('DapShowLog', function() require("dap._cmds").show_logs() end, { nargs = 0 })
cmd('DapContinue', function() require('dap').continue() end, { nargs = 0 })
cmd('DapToggleBreakpoint', function() require('dap').toggle_breakpoint() end, { nargs = 0 })
cmd('DapClearBreakpoints', function() require('dap').clear_breakpoints() end, { nargs = 0 })
cmd('DapToggleRepl', function() require('dap.repl').toggle() end, { nargs = 0 })
cmd('DapStepOver', function() require('dap').step_over() end, { nargs = 0 })
cmd('DapStepInto', function() require('dap').step_into() end, { nargs = 0 })
cmd('DapStepOut', function() require('dap').step_out() end, { nargs = 0 })
cmd('DapPause', function () require('dap').pause() end, { nargs = 0 })
cmd('DapTerminate', function() require('dap').terminate() end, { nargs = 0 })
cmd('DapDisconnect', function() require('dap').disconnect({ terminateDebuggee = false }) end, { nargs = 0 })
cmd('DapRestartFrame', function() require('dap').restart_frame() end, { nargs = 0 })

local function dapnew(args)
  return require("dap._cmds").new(args)
end
cmd("DapNew", dapnew, {
  nargs = "*",
  desc = "Start one or more new debug sessions",
  complete = function ()
    return require("dap._cmds").new_complete()
  end
})

cmd("DapEval", function(params)
  require("dap._cmds").eval(params)
end, {
  nargs = 0,
  range = "%",
  bang = true,
  bar = true,
  desc = "Create a new window & buffer to evaluate expressions",
})


if api.nvim_create_autocmd then
  local launchjson_group = api.nvim_create_augroup('dap-launch.json', { clear = true })
  local pattern =  '*/.vscode/launch.json'
  api.nvim_create_autocmd('BufNewFile', {
    group = launchjson_group,
    pattern = pattern,
    callback = function(args)
      require("dap._cmds").newlaunchjson(args)
    end
  })

  local readcmds = api.nvim_create_augroup("dap-readcmds", { clear = true })
  api.nvim_create_autocmd("BufReadCmd", {
    group = readcmds,
    pattern = "dap-eval://*",
    callback = function()
      require("dap._cmds").bufread_eval()
    end,
  })

  api.nvim_create_autocmd("BufReadCmd", {
    group = readcmds,
    pattern = "dap-src://*",
    ---@param args vim.api.keyset.create_autocmd.callback_args
    callback = function(args)
      require("dap._cmds").source(args.buf)
    end,
  })
end
```

## File: `spec/bad_adapter.py`
```python
import sys

sys.exit(10)
```

## File: `spec/breakpoints_spec.lua`
```
local api = vim.api

describe('breakpoints', function()

  require('dap')
  local breakpoints = require('dap.breakpoints')
  after_each(function()
    breakpoints.clear()
    for _, b in ipairs(api.nvim_list_bufs()) do
      api.nvim_buf_delete(b, { force = true })
    end
  end)

  it('can set normal breakpoints', function()
    breakpoints.set()
    local expected = {
      [1] = {
        {
          buf = 1,
          line = 1,
        },
      },
    }
    assert.are.same(expected, breakpoints.get())
    breakpoints.set() -- still on the same line, so this replaces the previous one
    assert.are.same(expected, breakpoints.get())
  end)

  it('can set a logpoint', function()
    breakpoints.set({ log_message = 'xs={xs}' })
    local expected = {
      [1] = {
        {
          buf = 1,
          line = 1,
          logMessage = 'xs={xs}',
        },
      },
    }
    assert.are.same(expected, breakpoints.get())
  end)

  it('can remove a breakpoint', function()
    local lnum = api.nvim_win_get_cursor(0)[1]
    breakpoints.toggle({ log_message = 'xs={xs}'})
    local expected = {
      [1] = {
        {
          buf = 1,
          line = 1,
          logMessage = 'xs={xs}',
        },
      },
    }
    assert.are.same(expected, breakpoints.get())
    breakpoints.remove(api.nvim_get_current_buf(), lnum)
    assert.are.same({}, breakpoints.get())
  end)

  it('can remove breakpoint by id', function()
    local lnum = api.nvim_win_get_cursor(0)[1]
    breakpoints.toggle()
    local state = { line = lnum, id = 1 }
    local fstbuf = api.nvim_get_current_buf()
    breakpoints.set_state(fstbuf, state)
    local newbuf = api.nvim_create_buf(true, true)
    api.nvim_set_current_buf(newbuf)
    api.nvim_buf_set_lines(newbuf, 0, -1, true, {"Hello", "World"})
    breakpoints.toggle({}, newbuf, 2)
    local expected = {
      [fstbuf] = {
        {
          buf = fstbuf,
          line = lnum,
          state = state,
        },
      },
      [newbuf] = {
        {
          buf = newbuf,
          line = 2,
        }
      }
    }
    assert.are.same(expected, breakpoints.get())
    breakpoints.remove_by_id(1)
    expected[fstbuf] = nil
    assert.are.same(expected, breakpoints.get())
  end)

  it('toggle adds bp if missing, otherwise removes', function()
    breakpoints.toggle()
    local buf = api.nvim_get_current_buf()
    local expected = {
      [buf] = {
        {
          buf = buf,
          line = 1
        },
      }
    }
    assert.are.same(expected, breakpoints.get())
    breakpoints.toggle()
    assert.are.same({}, breakpoints.get())
  end)

  it('can convert breakpoints to qf_list items', function()
    local buf = api.nvim_get_current_buf()
    api.nvim_buf_set_lines(buf, 0, -1, true, {'Hello breakpoint'})
    breakpoints.toggle({ condition = 'x > 10' })
    assert.are.same(
      {
        {
          bufnr = buf,
          col = 0,
          lnum = 1,
          text = 'Hello breakpoint, Condition: x > 10'
        }
      },
      breakpoints.to_qf_list(breakpoints.get())
    )

    local bps = {
      [buf] = {
        {
          line = 1,
          condition = ""
        },
      }
    }
    assert.are.same(
      {
        {
          bufnr = buf,
          col = 0,
          lnum = 1,
          text = "Hello breakpoint"
        }
      },
      breakpoints.to_qf_list(bps)
    )
  end)
end)
```

## File: `spec/debugpy_spec.lua`
```
local luassert = require('luassert')
local spy = require('luassert.spy')
local venv_dir = os.tmpname()
local dap = require('dap')
local helpers = require("spec.helpers")

local function get_num_handles()
  local pid = vim.fn.getpid()
  local output = vim.fn.system({"lsof", "-p", tostring(pid)})
  local lines = vim.split(output, "\n", { plain = true })
  return #lines, output
end


describe('dap with debugpy', function()
  os.remove(venv_dir)
  if vim.fn.executable("uv") == 1 then
    os.execute(string.format("uv venv '%s'", venv_dir))
    -- tmpfile could be on tmpfs in which case uv pip spits out hard-copy not-working warnings
    -- -> use link-mode=copy
    os.execute(string.format("uv --directory '%s' pip install --link-mode=copy debugpy", venv_dir))
  else
    os.execute('python -m venv "' .. venv_dir .. '"')
    os.execute(venv_dir .. '/bin/python -m pip install debugpy')
  end
  after_each(function()
    dap.terminate()
    require('dap.breakpoints').clear()
  end)

  it('Basic debugging flow', function()
    local breakpoints = require('dap.breakpoints')
    dap.adapters.python = {
      type = 'executable',
      command = venv_dir .. '/bin/debugpy-adapter',
      options = {
        cwd = venv_dir,
      }
    }
    local program = vim.fn.expand('%:p:h') .. '/spec/example.py'
    local config = {
      type = 'python',
      request = 'launch',
      name = 'Launch file',
      program = program,
      dummy_payload = {
        cwd = '${workspaceFolder}',
        ['key_with_${workspaceFolder}'] = 'value',
        numbers = {1, 2, 3, 4},
        strings = {'a', 'b', 'c'},
      }
    }
    local bp_lnum = 8
    local bufnr = vim.fn.bufadd(program)
    vim.fn.bufload(bufnr)
    breakpoints.set({}, bufnr, bp_lnum)
    local events = {}
    local dummy_payload = nil
    dap.listeners.after.event_initialized['dap.tests'] = function(session)
      events.initialized = true
      ---@diagnostic disable-next-line: undefined-field
      dummy_payload = session.config.dummy_payload
    end
    dap.listeners.after.setBreakpoints['dap.tests'] = function(_, _, resp)
      events.setBreakpoints = resp
    end
    dap.listeners.after.event_stopped['dap.tests'] = function(session)
      vim.wait(5000, function()
        return session.stopped_thread_id ~= nil
      end)
      dap.continue()
      events.stopped = true
    end

    -- force log creation now to not interfere with handle leak check
    require("dap.session")

    local num_handles, lsof_output = get_num_handles()

    local launch = spy.on(dap, 'launch')
    dap.run(config, { filetype = 'python' })
    helpers.wait(
      function() return events.stopped end,
      function() return "Must hit breakpoints. Events: " .. vim.json.encode(events) end
    )
    assert.are.same({
      initialized = true,
      setBreakpoints = {
        breakpoints = {
          {
            id = 0,
            line = bp_lnum,
            source = {
              name = 'example.py',
              path = program,
            },
            verified = true
          },
        },
      },
      stopped = true,
    }, events)

    -- variable must expand to concrete value
    assert(dummy_payload)
    assert.are_not.same(dummy_payload.cwd, '${workspaceFolder}')
    assert.are.same(dummy_payload.numbers, {1, 2, 3, 4})
    assert.are.same(dummy_payload.strings, {'a', 'b', 'c'})
    assert.are.same(dummy_payload['key_with_' .. vim.fn.getcwd()], 'value')

    -- ensure `called_with` below passes
    config.dummy_payload = dummy_payload

    luassert.spy(launch).was.called_with(dap.adapters.python, config, { cwd = venv_dir, filetype = 'python' })

    dap.terminate()
    vim.wait(1000, function() return dap.session() == nil end)

    helpers.wait(
      function()
        return num_handles == get_num_handles()
      end,
      function()
        local pid = vim.fn.getpid()
        local output = vim.fn.system({"lsof", "-p", tostring(pid)})
        local lines = vim.split(output, "\n", { plain = true })
        local new_num_handles = #lines
        return string.format(
          "Must not leak handles. %d should be %d\nHandles:\n%s\n\nBefore:\n%s\n\n",
          new_num_handles,
          num_handles,
          output,
          lsof_output
        )
      end
    )
    assert.are.same(num_handles, get_num_handles())
  end)
end)
vim.fn.delete(venv_dir, 'rf')
```

## File: `spec/entity_spec.lua`
```
local dap = require('dap')
local helpers = require("spec.helpers")

local config = {
  type = 'dummy',
  request = 'launch',
  name = 'Launch file',
}


describe("variable entity", function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    server.stop()
    dap.close()
    helpers.wait(function() return dap.session() == nil end, "session should become nil")
  end)

  it("fetch_children triggers callback on empty variables", function()
    server.client.variables = function(self, request)
      self:send_response(request, {
        variables = {}
      })
    end
    helpers.run_and_wait_until_initialized(config, server)
    local variable = require("dap.entity").variable

    local var = {
      name = "x",
      value = 1,
      variablesReference = 1,
    }
    local variables = nil
    variable.fetch_children(var, function (vars)
      variables = vars
    end)

    helpers.wait(function() return variables ~= nil end, "must call callback with variables")
    assert.are.same({}, variables)
  end)
end)
```

## File: `spec/example.py`
```python
#!/usr/bin/env python3

import os


def main():
    cwd = os.getcwd()
    print(cwd)
    a = 10
    b = 30
    return print(a + b)


if __name__ == '__main__':
    main()
```

## File: `spec/ext_vscode_spec.lua`
```
---@diagnostic disable: duplicate-set-field
local ui_input = vim.ui.input
local vscode = require('dap.ext.vscode')
describe('dap.ext.vscode', function()
  after_each(function()
    vim.ui.input = ui_input
  end)

  it('can load launch.json file and map adapter type to filetypes', function()
    local dap = require('dap')
    vscode.load_launchjs('spec/launch.json', { bar = { 'c', 'cpp' } })
    assert.are.same(3, vim.tbl_count(dap.configurations))
    assert.are.same({ { type = 'java', request = 'launch', name = "java test" }, }, dap.configurations.java)
    assert.are.same({ { type = 'bar', request = 'attach', name = "bar test" }, }, dap.configurations.c)
    assert.are.same({ { type = 'bar', request = 'attach', name = "bar test" }, }, dap.configurations.cpp)
  end)

  it('supports promptString input', function()
    local prompt
    local default
    vim.ui.input = function(opts, on_input)
      prompt = opts.prompt
      default = opts.default
      on_input('Fake input')
    end
    local jsonstr = [[
      {
        "configurations": [
          {
            "type": "dummy",
            "request": "launch",
            "name": "Dummy",
            "program": "${workspaceFolder}/${input:myInput}"
          }
        ],
        "inputs": [
          {
            "id": "myInput",
            "type": "promptString",
            "description": "Your input",
            "default": "the default value"
          }
        ]
      }
    ]]
    local configs = vscode._load_json(jsonstr)
    local ok = false
    local result
    coroutine.wrap(function()
      local conf = configs[1]()
      result = conf.program
      ok = true
    end)()
    vim.wait(1000, function() return ok end)
    assert.are.same("${workspaceFolder}/Fake input", result)
    assert.are.same("Your input: ", prompt)
    assert.are.same("the default value", default)
  end)

  it('supports pickString input', function()
    local options
    local opts
    local label
    vim.ui.select = function(options_, opts_, on_choice)
      options = options_
      opts = opts_
      label = opts_.format_item(options_[1])
      on_choice(options_[1])
    end
    local jsonstr = [[
      {
        "configurations": [
          {
            "type": "dummy",
            "request": "launch",
            "name": "Dummy",
            "program": "${workspaceFolder}/${input:my_input}"
          }
        ],
        "inputs": [
          {
            "id": "my_input",
            "type": "pickString",
            "options": ["one", "two", "three"],
            "description": "Select input"
          }
        ]
      }
    ]]
    local configs = vscode._load_json(jsonstr)
    local ok = false
    local result
    coroutine.wrap(function()
      local config = configs[1]()
      result = config.program
      ok = true
    end)()
    vim.wait(1000, function() return ok end)
    assert.are.same(true, ok, "coroutine must finish")
    assert.are.same("one", label)
    assert.are.same("${workspaceFolder}/one", result)
    assert.are.same("Select input", opts.prompt)
    assert.are.same({"one", "two", "three"}, options)
  end)

  it('inputs can be used in arrays or dicts', function()
    vim.fn.input = function(opts)
      return opts.default
    end
    local jsonstr = [[
      {
        "configurations": [
          {
            "type": "dummy",
            "request": "launch",
            "name": "Dummy",
            "args": ["one", "${input:myInput}", "three"]
          }
        ],
        "inputs": [
          {
            "id": "myInput",
            "type": "promptString",
            "description": "Your input",
            "default": "the default value"
          }
        ]
      }
    ]]
    local config = vscode._load_json(jsonstr)[1]
    assert.are.same(3, #config.args)
    assert.are.same("one", config.args[1])
    assert.are.same("${input:myInput}", config.args[2])
    assert.are.same("three", config.args[3])
    local ok = false
    coroutine.wrap(function()
      config = config()
      ok = true
    end)()
    vim.wait(1000, function() return ok end)
    assert.are.same("the default value", config.args[2])
  end)
  it('can use two inputs within one property', function()
    vim.fn.input = function(opts)
      return opts.default
    end
    local jsonstr = [[
      {
        "configurations": [
          {
            "type": "dummy",
            "request": "launch",
            "name": "Dummy",
            "program": "${input:input1}-${input:input2}"
          }
        ],
        "inputs": [
          {
            "id": "input1",
            "type": "promptString",
            "description": "first input",
            "default": "one"
          },
          {
            "id": "input2",
            "type": "promptString",
            "description": "second input",
            "default": "two"
          }
        ]
      }
    ]]
    local config = vscode._load_json(jsonstr)[1]
    local ok = false
    coroutine.wrap(function()
      ok, config = true, config()
    end)()
    vim.wait(1000, function() return ok end)
    assert.are.same("one-two", config.program)
  end)

  it('supports OS specific properties which are lifted to top-level', function()
    if vim.loop.os_uname().sysname == 'Linux' then
      local jsonstr = [[
      {
        "configurations": [
          {
            "type": "dummy",
            "request": "launch",
            "name": "Dummy",
            "linux": {
              "foo": "bar"
            }
          }
        ]
      }
      ]]
    local config = vscode._load_json(jsonstr)[1]
    assert.are.same("bar", config.foo)
    end
  end)

  it('supports promptString without default value', function()
    local prompt
    local default
    vim.fn.input = function(opts)
      prompt = opts.prompt
      default = opts.default
      return 'Fake input'
    end
    local jsonstr = [[
      {
        "configurations": [
          {
            "type": "dummy",
            "request": "launch",
            "name": "Dummy",
            "program": "${workspaceFolder}/${input:myInput}"
          }
        ],
        "inputs": [
          {
            "id": "myInput",
            "type": "promptString",
            "description": "Your input"
          }
        ]
      }
    ]]
    local configs = vscode._load_json(jsonstr)
    local config
    coroutine.wrap(function()
      config = configs[1]()
    end)()
    vim.wait(1000, function() return config ~= nil end)
    assert.are.same("${workspaceFolder}/Fake input", config.program)
    assert.are.same("Your input: ", prompt)
    assert.are.same("", default)
  end)

  it('supports pickString with options', function()
    local opts
    local label
    vim.ui.select = function(options_, opts_, on_choice)
      opts = opts_
      label = opts_.format_item(options_[1])
      on_choice(options_[1])
    end
    local jsonstr = [[
      {
        "configurations": [
          {
            "type": "dummy",
            "request": "launch",
            "name": "Dummy",
            "program": "${workspaceFolder}/${input:my_input}"
          }
        ],
        "inputs": [
          {
            "id": "my_input",
            "type": "pickString",
            "options": [
              { "label": "First value", "value": "one" },
              { "label": "Second value", "value": "two" }
            ],
            "description": "Select input"
          }
        ]
      }
    ]]
    local configs = vscode._load_json(jsonstr)
    local config
    coroutine.wrap(function()
      config = configs[1]()
    end)()
    vim.wait(1000, function() return config ~= nil end)
    assert(config, "coroutine must finish")
    assert.are.same("${workspaceFolder}/one", config.program)
    assert.are.same("Select input", opts.prompt)
    assert.are.same("First value", label)
  end)

  it('supports pickString with options, nothing selected', function()
    vim.ui.select = function(_, _, on_choice)
      on_choice(nil)
    end
    local jsonstr = [[
      {
        "configurations": [
          {
            "type": "dummy",
            "request": "launch",
            "name": "Dummy",
            "program": "${workspaceFolder}/${input:my_input}"
          }
        ],
        "inputs": [
          {
            "id": "my_input",
            "type": "pickString",
            "options": [
              { "label": "First value", "value": "one" },
              { "label": "Second value", "value": "two" }
            ],
            "description": "Select input"
          }
        ]
      }
    ]]
    local configs = vscode._load_json(jsonstr)
    local config
    coroutine.wrap(function()
      config = configs[1]()
    end)()
    vim.wait(1000, function() return config ~= nil end)
    assert(config, "coroutine must finish")
    -- input defaults to ''
    assert.are.same("${workspaceFolder}/", config.program)
  end)

  it("evaluates input once per config use", function()
    local prompt
    local default
    local calls = 0
    vim.fn.input = function(opts)
      prompt = opts.prompt
      default = opts.default
      calls = calls + 1
      return 'Fake input'
    end
    local jsonstr = [[
      {
        "configurations": [
          {
            "type": "dummy",
            "request": "launch",
            "name": "Dummy",
            "program": "${input:myInput}",
            "args": [
              "${input:myInput}",
              "foo",
              "${input:myInput}"
            ]
          }
        ],
        "inputs": [
          {
            "id": "myInput",
            "type": "promptString",
            "description": "Your input"
          }
        ]
      }
    ]]
    local configs = vscode._load_json(jsonstr)
    local config
    coroutine.wrap(function()
      config = configs[1]()
    end)()
    vim.wait(1000, function() return config ~= nil end)

    assert.are.same(calls, 1)
    assert.are.same("Your input: ", prompt)
    assert.are.same("", default)
  end)

  it('keeps unsupported input types as is', function()
    local jsonstr = [[
      {
        "configurations": [
          {
            "type": "dummy",
            "request": "launch",
            "name": "Dummy",
            "program": "${input:myCommand}"
          }
        ],
        "inputs": [
          {
            "id": "myCommand",
            "type": "command",
            "command": "shellCommand.execute"
          }
        ]
      }
    ]]
    local configs = vscode._load_json(jsonstr)
    local ok = false
    local result
    coroutine.wrap(function()
      local conf = configs[1]()
      result = conf.program
      ok = true
    end)()
    vim.wait(1000, function() return ok end)
    assert.are.same("${input:myCommand}", result)
  end)
end)
```

## File: `spec/helpers.lua`
```
local M = {}
local dap = require("dap")
local assert = require("luassert")

function M.wait(predicate, msg)
  vim.wait(5000, predicate)
  local result = predicate()
  if type(msg) == "string" then
    assert.are_not.same(false, result, msg)
  else
    assert.are_not.same(false, result, msg and vim.inspect(msg()) or nil)
  end
  assert.are_not.same(nil, result)
end


---@param command string
---@return string[] commands received
function M.wait_for_response(server, command)
  local function received_command()
    for _, response in pairs(server.spy.responses) do
      if response.command == command then
        return true
      end
    end
    return false
  end
  local function get_command(x)
    return x.command
  end
  M.wait(received_command, function()
    if next(server.spy.responses) then
      local responses = vim.tbl_map(get_command, server.spy.responses)
      return string.format("Expected `%s` in: %s", command, table.concat(responses, ", "))
    else
      return "Server sent no responses, expected: " .. command
    end
  end)
  return vim.tbl_map(get_command, server.spy.responses)
end


---@param conf dap.Configuration
---@param server table?
---@return dap.Session
function M.run_and_wait_until_initialized(conf, server)
  dap.run(conf)
  vim.wait(5000, function()
    local session = dap.session()
    -- wait for initialize and launch requests
    return (
      session ~= nil
      and session.initialized == true
      and (server == nil or (#server.spy.requests == 2 and #server.spy.responses == 2))
    )
  end, 100)
  return assert(dap.session(), "Must have session after run")
end

return M
```

## File: `spec/integration_spec.lua`
```
local api = vim.api
local dap = require('dap')
local helpers = require("spec.helpers")
local wait = helpers.wait
local wait_for_response= helpers.wait_for_response
local run_and_wait_until_initialized = helpers.run_and_wait_until_initialized

local config = {
  type = 'dummy',
  request = 'launch',
  name = 'Launch file',
}


describe('dap with fake server', function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    server.stop()
    dap.terminate({ all = true, hierarchy = true })
    dap.close()
    require('dap.breakpoints').clear()
    wait(function() return dap.session() == nil end)
  end)

  it("handler is called without response if there is an error", function()
    local session = run_and_wait_until_initialized(config, server)
    server.client.threads = function(self, request)
      self:send_err_response(request, "this is wrong", "err1")
    end

    local err, resp
    session:request("threads", nil, function (e, r)
      err = e
      resp = r
    end)
    wait(function() return err ~= nil end)
    assert.is_nil(resp)
    assert.are.same(tostring(err), "this is wrong")
  end)

  it('clear breakpoints clears all active breakpoints', function()
    local session = run_and_wait_until_initialized(config, server)
    assert.are_not.same(session, nil)
    assert.are.same(true, session.initialized)

    server.spy.clear()

    local buf1 = api.nvim_create_buf(false, true)
    api.nvim_buf_set_lines(buf1, 0, -1, false, {'line 1'})
    api.nvim_win_set_buf(0, buf1)
    api.nvim_win_set_cursor(0, { 1, 1 })
    dap.toggle_breakpoint()
    vim.wait(1000, function() return #server.spy.requests == 1 end, 100)
    assert.are.same(1, vim.tbl_count(require('dap.breakpoints').get()))
    assert.are.same('setBreakpoints', server.spy.requests[1].command)

    local buf2 = api.nvim_create_buf(false, true)
    api.nvim_buf_set_lines(buf2, 0, -1, false, {'line 1', 'line 2'})
    api.nvim_win_set_buf(0, buf2)
    api.nvim_win_set_cursor(0, { 1, 1 })
    dap.toggle_breakpoint()
    vim.wait(1000, function() return #server.spy.requests == 2 end, 100)

    assert.are.same(2, vim.tbl_count(require('dap.breakpoints').get()))

    server.spy.clear()
    dap.clear_breakpoints()
    vim.wait(1000, function() return #server.spy.requests == 2 end, 100)

    assert.are.same(0, vim.tbl_count(require('dap.breakpoints').get()))
    assert.are.same(2, vim.tbl_count(server.spy.requests))
    local setBreakpoints = server.spy.requests[1]
    assert.are.same({}, setBreakpoints.arguments.breakpoints)
  end)

  it('can handle stopped event for all threads', function()
    local session = run_and_wait_until_initialized(config, server)
    session:event_stopped({
      allThreadsStopped = true,
      reason = 'unknown',
    })
  end)

  it('Adds error diagnostic on stopped event due to exception', function()
    local buf = api.nvim_create_buf(true, false)
    local win = api.nvim_get_current_win()
    local tmpname = os.tmpname()
    os.remove(tmpname)
    api.nvim_buf_set_name(buf, tmpname)
    api.nvim_buf_set_lines(buf, 0, -1, false, {'line 1', 'line 2'})
    api.nvim_win_set_buf(win, buf)
    api.nvim_win_set_cursor(win, { 1, 0})

    local session = run_and_wait_until_initialized(config, server)
    server.spy.clear()
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    local path = vim.uri_from_bufnr(buf)
    server.client.stackTrace = function(self, request)
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            line = 1,
            column = 1,
            source = {
              path = path
            }
          },
        },
      })
    end
    session.capabilities.supportsExceptionInfoRequest = true
    server.client.exceptionInfo = function(self, request)
      self:send_response(request, {
        exceptionId = "XXX",
        breakMode = "unhandled"
      })
    end
    session:event_stopped({
      threadId = 1,
      reason = 'exception',
    })
    wait(function() return #server.spy.requests == 4 end, function()
      return {
        requests = server.spy.requests,
        responses = server.spy.responses
      }
    end)
    local diagnostics = vim.diagnostic.get(buf)
    for _, d in ipairs(diagnostics) do
      d._extmark_id = nil
    end
    local expected = {
      {
        bufnr = buf,
        col = 0,
        end_col = 0,
        end_lnum = 0,
        lnum = 0,
        message = 'Thread stopped due to exception (unhandled)',
        namespace = session.ns,
        severity = 1,
        source = 'nvim-dap',
      }
    }
    assert.are.same(expected, diagnostics)
  end)

  it('jumps to location if thread with same id is already stopped', function()
    local session = run_and_wait_until_initialized(config, server)

    -- Pretend to be stopped
    session.stopped_thread_id = 1

    server.spy.clear()
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    server.client.stackTrace = function(self, request)
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            line = 1,
          },
        },
      })
    end
    session:event_stopped({
      allThreadsStopped = false,
      threadId = 1,
      reason = 'breakpoint',
    })
    vim.wait(1000, function() return #server.spy.requests == 3 end)
    local expected_commands = {"threads", "stackTrace", "scopes"}
    assert.are.same(
      expected_commands,
      vim.tbl_map(function(x) return x.command end, server.spy.requests)
    )
  end)

  it("jumps to location on stopped with threadId that is missing", function()
    local session = run_and_wait_until_initialized(config, server)

    server.spy.clear()
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    local frame1 = {
      id = 1,
      name = "stackFrame1",
      line = 1,
    }
    server.client.stackTrace = function(self, request)
      self:send_response(request, {
        stackFrames = { frame1 },
      })
    end
    session:event_stopped({
      allThreadsStopped = false,
      threadId = 2,
      reason = 'breakpoint',
    })
    vim.wait(1000, function() return #server.spy.requests == 3 end)
    local expected_commands = {"threads", "stackTrace", "scopes"}
    assert.are.same(
      expected_commands,
      vim.tbl_map(function(x) return x.command end, server.spy.requests)
    )
    assert.are_same({
      [1] = {
        id = 1,
        name = "thread1",
      },
      [2] = {
        id = 2,
        name = "Unknown",
        stopped = true,
        frames = {
          frame1,
        }
      }
    }, session.threads)
  end)

  it('jumps to location on stopped with reason=pause and allThreadsStopped', function()
    local session = run_and_wait_until_initialized(config, server)
    server.spy.clear()
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    server.client.stackTrace = function(self, request)
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            line = 1,
          },
        },
      })
    end
    session:event_stopped({
      allThreadsStopped = true,
      threadId = 1,
      reason = 'pause',
    })
    -- should request threads, stackTrace and scopes on stopped event
    vim.wait(1000, function() return #server.spy.requests == 3 end)
    assert.are.same('threads', server.spy.requests[1].command)
    assert.are.same('stackTrace', server.spy.requests[2].command)
    assert.are_not.same(nil, session.current_frame)
    assert.are.same('stackFrame1', session.current_frame.name)
  end)

  it('jump to location results in nice error if location outside buffer contents', function()
    local buf = api.nvim_create_buf(true, false)
    local win = api.nvim_get_current_win()
    api.nvim_buf_set_lines(buf, 0, -1, false, {'line 1', 'line 2'})
    api.nvim_win_set_buf(win, buf)
    api.nvim_win_set_cursor(win, { 1, 0})

    local session = run_and_wait_until_initialized(config, server)
    server.spy.clear()
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    local path = vim.uri_from_bufnr(buf)
    server.client.stackTrace = vim.schedule_wrap(function(self, request)
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            line = 40,
            column = 3,
            source = {
              sourceReference = 0,
              path = path,
            },
          },
        },
      })
    end)
    local captured_msg
    vim.notify = function(...)
      local msg = select(1, ...)
      captured_msg = msg
    end
    session:event_stopped({
      threadId = 1,
      reason = 'breakpoint',
    })
    vim.wait(1000, function() return captured_msg ~= nil end)
    local msg
    if vim.fn.has("nvim-0.12") == 1 then
      msg = "Adapter reported frame in buf %d line 40:3, but: Invalid cursor line: out of range. Ensure executable is up2date and if using a source mapping ensure it is correct"
    else
      msg = 'Adapter reported frame in buf %d line 40:3, but: Cursor position outside buffer. Ensure executable is up2date and if using a source mapping ensure it is correct'
    end
    assert.are.same(string.format(msg, vim.uri_to_bufnr(path)), captured_msg)
  end)

  it('Can handle frames without source/path on stopped event', function()
    run_and_wait_until_initialized(config, server)
    server.spy.clear()
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    server.client.stackTrace = function(self, request)
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            line = 1,
          },
        },
      })
    end
    server.client:send_event('stopped', {
      threadId = 1,
      reason = 'unknown',
    })
    vim.wait(1000, function() return #server.spy.requests == 3 end, 100)
  end)

  it("Doesn't jump on stopped if continue is received before stacktrace response", function()
    local buf = api.nvim_create_buf(true, false)
    local win = api.nvim_get_current_win()
    api.nvim_buf_set_name(buf, "/tmp/dummy")
    api.nvim_buf_set_lines(buf, 0, -1, false, {"line 1", "line 2", "line 3"})
    api.nvim_win_set_buf(win, buf)
    api.nvim_win_set_cursor(win, { 1, 0})

    run_and_wait_until_initialized(config, server)
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    server.client:send_event('stopped', {
      threadId = 1,
      reason = 'unknown',
    })
    local path = vim.uri_from_bufnr(buf)
    server.client.stackTrace = function(self, request)
      self:send_event("continued", {
        threadId = 1,
      })
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            line = 2,
            column = 4,
            source = {
              sourceReference = 0,
              path = path,
            },
          },
        },
      })
    end
    wait(function() return #server.spy.responses == 4 end)
    local expected = {
      bufnr = buf,
      cursor = {1 , 0}
    }
    assert.are.same(expected, {
      bufnr = api.nvim_win_get_buf(win),
      cursor = api.nvim_win_get_cursor(win)
    })
  end)

  it("Doesn't jump on stopped if continue is received before threads response", function()
    run_and_wait_until_initialized(config, server)
    server.client.threads = function(self, request)
      self:send_event("continued", {
        threadId = 1,
      })
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    local log = require('dap.log').create_logger('dap.log')
    local debug = log.debug
    local messages = {}
    log.debug = function(self, ...)
      table.insert(messages, {...})
      debug(self, ...)
    end
    server.client:send_event('stopped', {
      threadId = 1,
      reason = 'unknown',
    })
    wait_for_response(server, "threads")
    wait(function() return #messages >= 5 end)
    assert.are.same("Thread resumed during stopped event handling", messages[6][1])
  end)

  it("Clears stopped state on continued event", function()
    local buf = api.nvim_create_buf(true, false)
    local win = api.nvim_get_current_win()
    api.nvim_buf_set_name(buf, "/tmp/dummy1")
    api.nvim_buf_set_lines(buf, 0, -1, false, {"line 1", "line 2", "line 3"})
    api.nvim_win_set_buf(win, buf)
    api.nvim_win_set_cursor(win, { 1, 0})

    local session = run_and_wait_until_initialized(config, server)
    server.spy.clear()
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    local path = vim.uri_from_bufnr(buf)
    server.client.stackTrace = function(self, request)
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            line = 2,
            column = 4,
            source = {
              sourceReference = 0,
              path = path,
            },
          },
        },
      })
    end
    server.client.scopes = function(self, request)
      self:send_response(request, {
        scopes = {}
      })
    end
    server.client:send_event('stopped', {
      threadId = 1,
      reason = 'unknown',
    })

    wait_for_response(server, "scopes")
    assert.are.same({2, 3}, api.nvim_win_get_cursor(win))
    server.client:send_event('continued', {
      threadId = 1,
    })
    wait(function() return session.threads[1].stopped == false end)
    assert.is_nil(session.stopped_thread_id)
    assert.is_nil(session.current_frame)
    local signs = vim.fn.sign_getplaced(vim.uri_to_bufnr(path), {group = session.sign_group})
    assert.are.same({}, signs[1].signs)
  end)

  it('Deleting a buffer clears breakpoints for that buffer', function()
    local win = api.nvim_get_current_win()
    local buf1 = api.nvim_create_buf(false, true)
    api.nvim_buf_set_name(buf1, 'dummy_buf1')
    api.nvim_buf_set_lines(buf1, 0, -1, false, {'buf1: line1'})
    api.nvim_win_set_buf(win, buf1)
    api.nvim_win_set_cursor(win, { 1, 0 })
    dap.toggle_breakpoint()

    run_and_wait_until_initialized(config, server)
    -- wait for initialize, launch and one setBreakpoints request
    vim.wait(1000, function() return #server.spy.requests == 3 end, 100)
    assert.are.same(3, #server.spy.requests)
    server.spy.clear()
    api.nvim_buf_delete(buf1, { force = true })

    vim.wait(1000, function() return #server.spy.requests == 1 end, 100)
    local setBreakpoints = server.spy.requests[1]
    assert.are.same('setBreakpoints', setBreakpoints.command)
    assert.are.same('dummy_buf1', setBreakpoints.arguments.source.name)
    assert.are.same({}, setBreakpoints.arguments.breakpoints)

    assert.are.same({}, require('dap.breakpoints').get())
  end)

  it('prints formatted error on launch error', function()
    local captured_msg
    vim.notify = function(...)
      local msg = select(1, ...)
      captured_msg = msg
    end
    server.client.launch = function(self, request)
      self:send_err_response(request, 'Failure', {
        id = 1,
        format = 'Failed: {e}',
        showUser = true,
        variables = {
          e = 'Dummy'
        },
      })
    end
    run_and_wait_until_initialized(config, server)
    wait(function() return captured_msg ~= nil end)
    assert.are.same('Error on launch: Failed: Dummy', captured_msg)
  end)

  it('evaluates callable config', function()
    local callable_config = setmetatable(config, {
      __call = function(conf)
        local result = {}
        for k, v in pairs(conf) do
          result[k] = v
        end
        result.x = 1
        return result
      end,
    })
    local session = run_and_wait_until_initialized(callable_config, server)
    assert.are.same(session.config.x, 1)
  end)

  it("step does nothing if session is not stopped", function()
    local session = run_and_wait_until_initialized(config, server)
    dap.step_over()
    assert.are.same(session, dap.session())
  end)

  it("step_into askForTargets=true uses step fallbacks on empty targets response", function()
    local session = run_and_wait_until_initialized(config, server)
    session.capabilities.supportsStepInTargetsRequest = true
    server.spy.clear()
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end

    local buf = api.nvim_create_buf(true, false)
    local win = api.nvim_get_current_win()
    local tmpname = os.tmpname()
    os.remove(tmpname)
    api.nvim_buf_set_name(buf, tmpname)
    api.nvim_buf_set_lines(buf, 0, -1, false, {'line 1', 'line 2'})
    api.nvim_win_set_buf(win, buf)
    api.nvim_win_set_cursor(win, { 1, 0})
    local path = vim.uri_from_bufnr(buf)

    server.client.stackTrace = function(self, request)
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            line = 1,
            column = 1,
            source = {
              path = path
            }
          },
        },
      })
    end
    server.client.scopes = function(self, request)
      self:send_response(request, {
        scopes = {}
      })
    end
    server.client:send_event('stopped', {
      threadId = 1,
      reason = 'breakpoint',
    })
    wait_for_response(server, "scopes")

    server.client.stepInTargets = function(self, request)
      self:send_response(request, {
        targets = {}
      })
    end
    server.client.stepIn = function(self, request)
      self:send_response(request, {})
    end

    dap.step_into({ askForTargets = true })
    wait_for_response(server, "stepIn")
    local commands = vim.tbl_map(function(x) return x.command end, server.spy.requests)
    assert.are.same({"threads", "stackTrace", "scopes", "stepInTargets", "stepIn"}, commands)
  end)

  it("Run aborts if config value is dap.ABORT", function()
    local msg = nil
    require('dap.utils').notify = function(m)
      msg = m
    end
    dap.run({
      name = "dummy",
      type = "dummy",
      request = "launch",
      foo = function()
        return dap.ABORT
      end,
    })
    wait(function() return msg ~= nil end)
    assert.is_nil(dap.session())
    assert.are.same("Run aborted", msg)
  end)

  it("Can trigger config property from luv thread", function()
    local conf = {
      name = "dummy",
      type = "dummy",
      request = "launch",
      foo = function()
        local co = coroutine.running()
        vim.system({"echo", "test"}, function()
          coroutine.resume(co, 1)
        end)
        return coroutine.yield()
      end,
    }
    local session = run_and_wait_until_initialized(conf, server)
    assert.is_not_nil(session)
  end)

  it("triggers on_session listener on session changes", function()
    local on_session_results = {}
    local conf1 = {
      name = "s1",
      type = "dummy",
      request = "launch"
    }
    dap.listeners.on_session["dap.testcase"] = function (old, new)
      table.insert(on_session_results, { old = old, new = new })
    end
    local session1 = run_and_wait_until_initialized(conf1, server)
    assert.are.same(1, #on_session_results)
    assert.are.same(session1.id, on_session_results[1].new.id)

    local conf2 = {
      name = "s2",
      type = "dummy",
      request = "launch"
    }
    local session2 = run_and_wait_until_initialized(conf2, server)
    assert.are.same(2, #on_session_results)
    assert.are.same(session1.id, on_session_results[2].old.id)
    assert.are.same(session2.id, on_session_results[2].new.id)

    dap.set_session(session1)
    assert.are.same(3, #on_session_results)

    dap.terminate({ all = true })
    wait(function() return dap.session() == nil end)
    assert.are.same(5, #on_session_results)
    assert.is_nil(on_session_results[5].new)
  end)
end)

describe('session disconnect', function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    dap.close()
    require('dap.breakpoints').clear()
    server.stop()
    wait(function() return dap.session() == nil end)
  end)

  it('Can call close on session after session has already closed', function()
    local session = run_and_wait_until_initialized(config, server)
    assert.are.not_same(nil, session)
    local cb_called = false
    dap.disconnect(nil, function()
      cb_called = true
    end)
    vim.wait(1000, function() return cb_called end, 100)
    assert.are.same(true, cb_called)
    assert.are.same(nil, dap.session())
    session:close()
  end)

  it('Closes session on disconnect response', function()
    run_and_wait_until_initialized(config, server)
    server.spy.clear()

    local client = server.client
    -- override to not send terminate event as well
    client.disconnect = function(self, request)
      self:send_response(request, {})
    end

    local cb_called = false
    dap.disconnect(nil, function()
      cb_called = true
    end)
    vim.wait(1000, function() return cb_called end, 100)
    assert.are.same({}, server.spy.events)
    assert.are.same(1, #server.spy.responses)
    assert.are.same('disconnect', server.spy.responses[1].command)
    assert.are.same(nil, dap.session())
  end)

  it('Closes session if server closes connection', function()
    local session = run_and_wait_until_initialized(config, server)
    assert.are_not.same(nil, dap.session())
    assert.are.same(session, dap.session())
    server.stop()
    vim.wait(1000, function() return dap.session() == nil end, 100)
    assert.are.same(nil, server.client.socket)
    assert.are.same(nil, dap.session())
  end)

  it('Closes session if initialization fails', function()
    local launch_called = false
    server.client.launch = function(self, request)
      launch_called = true
      self:send_err_response(request, 'Dummy error')
    end
    local msg = nil
    require('dap.utils').notify = function(m)
      msg = m
    end
    dap.run(config)
    vim.wait(1000, function() return launch_called end, 100)
    vim.wait(1000, function() return dap.session() == nil end, 100)
    assert.are.same(nil, dap.session())
    assert.are.same('Error on launch: Dummy error', msg)
  end)

  it('Repeated disconnect after stopped server is safe and resets session', function()
    run_and_wait_until_initialized(config, server)
    server.stop()
    local cb_called = false
    for _ = 1, 10 do
      dap.disconnect()
    end
    dap.disconnect(nil, function()
      cb_called = true
    end)
    vim.wait(1000, function() return cb_called end, 100)
    assert.are.same(nil, dap.session())
  end)
end)

describe('request source', function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    dap.close()
    server.stop()
    wait(function() return dap.session() == nil end)
  end)

  it('can jump to frame if source needs to be fetched', function()
    api.nvim_create_autocmd("BufReadCmd", {
      group = api.nvim_create_augroup("dap-readcmds", { clear = true }),
      pattern = "dap-src://*",
      ---@param args vim.api.keyset.create_autocmd.callback_args
      callback = function(args)
        require("dap._cmds").source(args.buf)
      end,
    })

    server.client.source = function(self, request)
      self:send_response(request, {
        content = 'foobar',
        mimeType = 'text/x-lldb.disassembly',
      })
    end
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    server.client.stackTrace = function(self, request)
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            line = 1,
            column = 1,
            source = {
              sourceReference = 1
            }
          },
        },
      })
    end
    run_and_wait_until_initialized(config, server)
    server.spy.clear()
    server.client:send_event('stopped', {
      threadId = 1,
      reason = 'breakpoint',
    })
    wait_for_response(server, 'source')
    assert.are.same('source', server.spy.responses[3].command)
    assert.are.same('foobar', server.spy.responses[3].body.content)
    wait(function()
      return 'foobar' == api.nvim_buf_get_lines(0, 0, -1, false)[1]
    end)
    local lines = api.nvim_buf_get_lines(0, 0, -1, false)
    assert.are.same({'foobar'}, lines)
  end)

  it('sets filetype based on mimetype if available', function()
    server.client.source = function(self, request)
      self:send_response(request, {
        content = '',
        mimeType = 'text/javascript',
      })
    end

    local session = run_and_wait_until_initialized(config, server)
    local source = {
      sourceReference = 1
    }
    local bufnr = nil
    session:source(source, function(_, buf)
      bufnr = buf
    end)
    vim.wait(1000, function() return bufnr ~= nil end, 100)
    assert.are.same('javascript', vim.bo[bufnr].filetype)
  end)

  it('sets filetype based on adapter option if available', function()
    server.client.source = function(self, request)
      self:send_response(request, {
        content = '',
      })
    end
    dap.adapters.dummy.options = {
      source_filetype = 'lua'
    }
    local session = run_and_wait_until_initialized(config, server)
    local source = {
      sourceReference = 1
    }
    local bufnr = nil
    session:source(source, function(_, buf)
      bufnr = buf
    end)
    vim.wait(1000, function() return bufnr ~= nil end, 100)
    assert.are.same('lua', vim.bo[bufnr].filetype)
  end)

  if vim.filetype then
    it('derives filetype from source.path if available', function()
      server.client.source = function(self, request)
        self:send_response(request, {
          content = '',
        })
      end
      local session = run_and_wait_until_initialized(config, server)
      local source = {
        sourceReference = 1,
        path = 'foo/bar/baz.lua',
      }
      local bufnr = nil
      session:source(source, function(_, buf)
        bufnr = buf
      end)
      vim.wait(1000, function() return bufnr ~= nil end, 100)
      assert.are.same('lua', vim.bo[bufnr].filetype)
    end)
  end
end)

describe('run_to_cursor', function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
    server.client.setBreakpoints = function(self, request)
      local breakpoints = request.arguments.breakpoints
      self:send_response(request, {
        breakpoints = vim.tbl_map(function() return { verified = true } end, breakpoints)
      })
    end
  end)
  after_each(function()
    dap.close()
    server.stop()
    for _, buf in pairs(api.nvim_list_bufs()) do
      api.nvim_buf_delete(buf, { force = true })
    end
    wait(function() return dap.session() == nil end)
  end)

  it('clears breakpoints from buffers, adds breakpoint for current line, continues, restores breakpoints', function()
    local win = api.nvim_get_current_win()
    local buf1 = api.nvim_create_buf(false, true)
    local buf2 = api.nvim_create_buf(false, true)
    api.nvim_buf_set_name(buf1, 'dummy_buf1')
    api.nvim_buf_set_name(buf2, 'dummy_buf2')
    api.nvim_buf_set_lines(buf1, 0, -1, false, {'buf1: line1'})
    api.nvim_buf_set_lines(buf2, 0, -1, false, {'buf2: line 1', 'buf2: line2'})

    api.nvim_win_set_buf(win, buf1)
    api.nvim_win_set_cursor(win, { 1, 0 })
    dap.toggle_breakpoint()

    api.nvim_win_set_buf(win, buf2)
    api.nvim_win_set_cursor(win, { 1, 0 })
    dap.toggle_breakpoint()

    local session = run_and_wait_until_initialized(config, server)
    -- wait for initialize, launch, and setBreakpoints (two buffers, two setBreakpoints)
    vim.wait(1000, function() return #server.spy.requests == 4 end, 100)
    server.spy.clear()
    assert.are.same(2, vim.tbl_count(require('dap.breakpoints').get()))

    api.nvim_win_set_buf(win, buf2)
    api.nvim_win_set_cursor(win, { 2, 0 })

    -- Pretend to be stopped
    session.stopped_thread_id = 1

    dap.run_to_cursor()
    vim.wait(1000, function() return #server.spy.requests == 3 end, 100)

    -- sets breakpoint for current buffer to current line to run to the cursor
    local set_bps_requests = { server.spy.requests[1], server.spy.requests[2] }
    table.sort(set_bps_requests, function(a, b)
      return a.arguments.source.name > b.arguments.source.name
    end)
    local set_bps1 = set_bps_requests[1]
    assert.are.same('setBreakpoints', set_bps1.command)
    assert.are.same('dummy_buf2', set_bps1.arguments.source.name)
    assert.are.same({ { line = 2 }, }, set_bps1.arguments.breakpoints)

    -- resets breakpoints everywhere else
    local set_bps2 = set_bps_requests[2]
    assert.are.same('setBreakpoints', set_bps2.command)
    assert.are.same('dummy_buf1', set_bps2.arguments.source.name)
    assert.are.same({}, set_bps2.arguments.breakpoints)

    -- continues to run to the cursor
    local continue_req = server.spy.requests[3]
    assert.are.same('continue', continue_req.command)

    server.spy.clear()

    -- restores original breakpoints once stopped
    server.client:send_event('stopped', {
      reason = 'stopped',
      allThreadsStopped = true,
    })
    vim.wait(1000, function() return #server.spy.requests == 3 end, 100)

    set_bps_requests = { server.spy.requests[1], server.spy.requests[2] }
    table.sort(set_bps_requests, function(a, b)
      return a.arguments.source.name > b.arguments.source.name
    end)
    set_bps1 = set_bps_requests[1]
    assert.are.same('setBreakpoints', set_bps1.command)
    assert.are.same('dummy_buf2', set_bps1.arguments.source.name)
    assert.are.same({ { line = 1 }, }, set_bps1.arguments.breakpoints)

    set_bps2 = set_bps_requests[2]
    assert.are.same('setBreakpoints', set_bps2.command)
    assert.are.same('dummy_buf1', set_bps2.arguments.source.name)
    assert.are.same({ { line = 1 }, }, set_bps2.arguments.breakpoints)
  end)
  it('clears temporary run_to_cursor breakpoint if buffer contained no breakpoints before', function()
    local win = api.nvim_get_current_win()
    local buf1 = api.nvim_create_buf(false, true)
    local buf2 = api.nvim_create_buf(false, true)
    api.nvim_buf_set_name(buf1, 'dummy_buf1')
    api.nvim_buf_set_name(buf2, 'dummy_buf2')
    api.nvim_buf_set_lines(buf1, 0, -1, false, {'buf1: line1'})
    api.nvim_buf_set_lines(buf2, 0, -1, false, {'buf2: line 1', 'buf2: line2'})

    api.nvim_win_set_buf(win, buf1)
    api.nvim_win_set_cursor(win, { 1, 0 })
    dap.toggle_breakpoint()
    local session = run_and_wait_until_initialized(config, server)
    -- wait for initialize, launch, and setBreakpoints
    vim.wait(1000, function() return #server.spy.requests == 3 end, 100)
    server.spy.clear()
    assert.are.same(1, vim.tbl_count(require('dap.breakpoints').get()))

    api.nvim_win_set_buf(win, buf2)
    api.nvim_win_set_cursor(win, { 2, 0 })

    -- Pretend to be stopped
    session.stopped_thread_id = 1
    dap.run_to_cursor()
    -- sets breakpoints in two buffers
    vim.wait(1000, function() return #server.spy.requests == 2 end, 100)
    server.spy.clear()
    server.client:send_event('stopped', {
      reason = 'stopped',
      allThreadsStopped = true,
    })
    -- continues, resets breakpoints in both buffers
    vim.wait(1000, function() return #server.spy.requests == 3 end, 100)
    local set_bps_requests = { server.spy.requests[2], server.spy.requests[3] }
    table.sort(set_bps_requests, function(a, b)
      return a.arguments.source.name < b.arguments.source.name
    end)
    local set_bps1 = set_bps_requests[1]
    assert.are.same('setBreakpoints', set_bps1.command)
    assert.are.same('dummy_buf1', set_bps1.arguments.source.name)
    assert.are.same({ { line = 1 }, }, set_bps1.arguments.breakpoints)

    local set_bps2 = set_bps_requests[2]
    assert.are.same('setBreakpoints', set_bps2.command)
    assert.are.same('dummy_buf2', set_bps2.arguments.source.name)
    assert.are.same({}, set_bps2.arguments.breakpoints)
    local expected_bps = {
      [buf1] = {
        {
          buf = buf1,
          line = 1,
        },
      }
    }
    assert.are.same(expected_bps, require('dap.breakpoints').get())
  end)
end)

describe('breakpoint events', function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    server.stop()
    dap.close()
    require('dap.breakpoints').clear()
    wait(function() return dap.session() == nil end)
  end)
  it('can change state from rejected to verified', function()
    server.client.setBreakpoints = function(self, request)
      self:send_response(request, {
        breakpoints = {
          {
            id = 1,
            verified = false,
            message = "I don't like this breakpoint",
          }
        }
      })
    end

    run_and_wait_until_initialized(config, server)
    local win = api.nvim_get_current_win()
    local buf1 = api.nvim_create_buf(false, true)
    api.nvim_buf_set_name(buf1, 'dummy_buf1')
    api.nvim_buf_set_lines(buf1, 0, -1, false, {'buf1: line1'})
    api.nvim_win_set_buf(win, buf1)
    api.nvim_win_set_cursor(win, { 1, 0 })
    dap.toggle_breakpoint()

    local breakpoints = require('dap.breakpoints')

    -- initialize, launch, setBreakpoints == 3 requests
    wait(function() return #server.spy.requests == 3 end)
    wait(function() return #server.spy.responses == 3 end)
    wait(function() return breakpoints.get()[buf1][1].state end)

    local bps = breakpoints.get()
    assert.are.same(1, vim.tbl_count(bps))
    local expected_breakpoint = {
      buf = buf1,
      line = 1,
      state = {
        id = 1,
        message = "I don't like this breakpoint",
        verified = false,
      }
    }
    assert.are.same(expected_breakpoint, bps[buf1][1])
    local signs = vim.fn.sign_getplaced(buf1, { group = 'dap_breakpoints' })
    assert.are.same('DapBreakpointRejected', signs[1].signs[1].name)

    local num_events = #server.spy.events
    server.client:send_event('breakpoint', {
      reason = 'changed',
      breakpoint = {
        id = 1,
        verified = true,
        message = "I don't like this breakpoint",
      }
    })
    wait(function() return #server.spy.events == num_events + 1 end)
    wait(function() return breakpoints.get()[buf1][1].state.verified end)
    assert.are.same(num_events + 1, #server.spy.events)
    expected_breakpoint.state.verified = true
    assert.are.same(expected_breakpoint, breakpoints.get()[buf1][1])

    signs = vim.fn.sign_getplaced(buf1, { group = 'dap_breakpoints' })
    assert.are.same('DapBreakpoint', signs[1].signs[1].name)
  end)

  it('can add and remove breakpoints from adapter events', function()
    run_and_wait_until_initialized(config, server)

    local win = api.nvim_get_current_win()
    local buf2 = api.nvim_create_buf(false, true)
    api.nvim_buf_set_name(buf2, 'dummy_buf2')
    api.nvim_buf_set_lines(buf2, 0, -1, false, {'buf2: line1'})
    api.nvim_win_set_buf(win, buf2)
    api.nvim_win_set_cursor(win, { 1, 0 })

    -- initialize, launch == 2 requests
    wait(function() return #server.spy.requests == 2 end)
    wait(function() return #server.spy.responses == 2 end)

    local breakpoint_state = {
      id = 1,
      line = 1,
      verified = true,
      source = {
        path = vim.uri_from_bufnr(buf2)
      },
    }

    local num_events = #server.spy.events
    server.client:send_event('breakpoint', {
      reason = 'new',
      breakpoint = breakpoint_state,
    })

    local breakpoints = require('dap.breakpoints')

    wait(function() return #server.spy.events == num_events + 1 end)
    wait(function() return breakpoints.get()[buf2] ~= nil end)

    local expected_breakpoints = {
      [buf2] = {
        [1] = {
          buf = buf2,
          line = breakpoint_state.line,
          state = breakpoint_state,
        }
      }
    }

    assert.are.same(expected_breakpoints, breakpoints.get())

    num_events = #server.spy.events
    server.client:send_event('breakpoint', {
      reason = 'removed',
      breakpoint = { id = 1 },
    })

    wait(function() return #server.spy.events == num_events + 1 end)
    wait(function() return breakpoints.get()[buf2] == nil end)

    assert.are.same({}, breakpoints.get())
  end)
end)

describe('restart_frame', function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    server.stop()
    dap.close()
    wait(function() return dap.session() == nil end)
  end)
  it('Requires restart capability', function()
    run_and_wait_until_initialized(config, server)
    local msg
    require('dap.utils').notify = function(m, _)
      msg = m
    end
    dap.restart_frame()
    assert.are.same('Debug Adapter does not support restart frame', msg)
  end)

  it('Requires to be stopped', function()
    local session = run_and_wait_until_initialized(config, server)
    assert(session)
    session.capabilities.supportsRestartFrame = true
    local msg
    require('dap.utils').notify = function(m, _)
      msg = m
    end
    dap.restart_frame()
    assert.are.same('Current frame not set. Debug adapter needs to be stopped at breakpoint to use restart frame', msg)
  end)

  it('Restarts frame if stopped at breakpoint', function()
    local session = run_and_wait_until_initialized(config, server)
    server.spy.clear()
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    server.client.stackTrace = function(self, request)
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            line = 1,
          },
        },
      })
    end
    assert(session)
    session.capabilities.supportsRestartFrame = true
    session:event_stopped({
      allThreadsStopped = false,
      threadId = 1,
      reason = 'breakpoint',
    })

    wait(function() return #server.spy.requests == 3 end)
    dap.restart_frame()
    wait(function() return #server.spy.requests == 4 end)
    assert.are.same('restartFrame', server.spy.requests[4].command)
  end)

  it('Asks for frame to restart, if current frame cannot', function()
    local session = run_and_wait_until_initialized(config, server)
    server.spy.clear()
    server.client.threads = function(self, request)
      self:send_response(request, {
        threads = { { id = 1, name = 'thread1' }, }
      })
    end
    server.client.stackTrace = function(self, request)
      self:send_response(request, {
        stackFrames = {
          {
            id = 1,
            name = 'stackFrame1',
            canRestart = false,
            line = 2,
          },
          {
            id = 2,
            name = 'stackFrame2',
            canRestart = true,
            line = 1,
          },
        },
      })
    end
    assert(session)
    session.capabilities.supportsRestartFrame = true
    session:event_stopped({
      allThreadsStopped = false,
      threadId = 1,
      reason = 'breakpoint',
    })
    local asked = false
    vim.ui.select = function(items, _, cb)
      asked = true
      cb(items[1])
    end

    wait(function() return #server.spy.requests == 3 end)
    dap.restart_frame()
    wait(function() return asked end)
    assert.are.same(true, asked)
    wait(function() return #server.spy.requests == 4 end)
    assert.are.same('restartFrame', server.spy.requests[4].command)
  end)
end)


describe('event_terminated', function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    server.stop()
    dap.terminate()
    wait(function() return dap.session() == nil end)
  end)
  it('can restart session', function()
    local session = run_and_wait_until_initialized(config, server)

    server.spy.clear()
    server.client:send_event('terminated', {
      restart = 'dummy_value'
    })

    -- should start new session
    -- wait for initialize and launch
    wait(function() return #server.spy.requests == 2 end)
    local request = server.spy.requests[2]
    assert.are.same('launch', request.command, 'launch')
    local expected_args = vim.deepcopy(session.config)
    expected_args.__restart = 'dummy_value'
    assert.are.same(expected_args, request.arguments)
    local new_session = dap.session()
    assert.is_not_nil(new_session)
    assert.are_not_same(session.id, assert(new_session).id)

    server.client:send_event('terminated')
    dap.terminate()
    wait(function() return dap.session() == nil end)
  end)
end)


describe('progress support', function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    server.stop()
    dap.terminate()
    wait(function() return dap.session() == nil end)
  end)

  it('shows progress in status', function()
    run_and_wait_until_initialized(config, server)
    local progress = require('dap.progress')
    wait(function() return #server.spy.events == 1 end)

    progress.reset()
    server.spy.clear()
    server.client:send_event('progressStart', {
      progressId = '1',
      title = 'progress title',
    })
    wait(function() return #server.spy.events == 1 end)
    assert.are.same('progressStart', server.spy.events[1].event)
    wait(function() return progress.status() ~= '' end)
    assert.are.same('progress title', progress.status())

    server.client:send_event('progressEnd', {
      progressId = '1',
    })
    wait(function() return progress.status() ~= 'progress title' end)
    assert.are.same('Running: Launch file', progress.status())
  end)
end)


describe("run_last", function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    server.stop()
    dap.terminate()
    wait(function() return dap.session() == nil end, "Session should become nil after terminate")
    assert.are.same(0, vim.tbl_count(dap.sessions()), "Sessions should go down to 0 after terminate/stop")
  end)

  it('can repeat run_last and it always clears session', function()
    server.client.initialize = function(self, request)
      self:send_response(request, {
        supportsTerminateRequest = true,
      })
      self:send_event("initialized", {})
    end

    run_and_wait_until_initialized(config, server)
    server.spy.clear()
    dap.run_last()
    wait(function() return #server.spy.requests == 3 end)
    local commands = vim.tbl_map(function(x) return x.command end, server.spy.requests)
    assert.are.same({"terminate", "initialize", "launch"}, commands)
    assert.are.same(1, vim.tbl_count(dap.sessions()))

    dap.run_last()
    wait(function() return #server.spy.requests == 3 end)
    commands = vim.tbl_map(function(x) return x.command end, server.spy.requests)
    assert.are.same({"terminate", "initialize", "launch"}, commands)
    assert.are.same(1, vim.tbl_count(dap.sessions()))
  end)

  it("re-evaluates functions if adapter supports restart", function()
    server.client.initialize = function(self, request)
      self:send_response(request, {
        supportsRestartRequest = true,
      })
      self:send_event("initialized", {})
    end
    server.client.restart = function(self, request)
      self:send_response(request, {})
    end
    local num_called = 0
    local dummy_config = {
      type = 'dummy',
      request = 'launch',
      name = 'Launch file',
      called = function()
        num_called = num_called + 1
        return num_called
      end
    }
    run_and_wait_until_initialized(dummy_config, server)
    assert.are.same(1, num_called)
    server.spy.clear()
    dap.run_last()
    wait_for_response(server, "restart")
    local commands = vim.tbl_map(function(x) return x.command end, server.spy.requests)
    assert.are.same({"restart"}, commands)
    assert.are.same(2, num_called)
  end)
end)


describe("bad debug adapter", function()
  it("calls notify with warning", function()
    dap.adapters.bad = {
      type = "executable",
      command = "python",
      args = { vim.fn.expand("%:p:h") .. "/spec/bad_adapter.py" }
    }
    local captured_msg
    local captured_log_level
    ---@diagnostic disable-next-line: duplicate-set-field
    require("dap.utils").notify = function(msg, log_level)
      captured_msg = msg
      captured_log_level = log_level
    end
    local bad_config = {
      type = 'bad',
      request = 'launch',
      name = 'Launch file',
    }
    dap.run(bad_config)
    wait(function() return captured_msg ~= nil end)
    assert.are.same("command `python` of adapter `bad` exited with 10. Run :DapShowLog to open logs", captured_msg)
    assert.are.same(vim.log.levels.WARN, captured_log_level)
  end)
end)


describe("on_output", function()
  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy_on_output = server.adapter
  end)
  after_each(function()
    dap.terminate()
    server.stop()
    wait(function() return dap.session() == nil end, "Session should become nil after terminate")
    assert.are.same(0, vim.tbl_count(dap.sessions()), "Sessions should go down to 0 after terminate/stop")
    dap.defaults.dummy_on_output.on_output = nil
    assert.are.is_nil(dap.defaults.dummy_on_output.on_output)
  end)

  it("can override output handling", function()
    local captured_output = nil

    function dap.defaults.dummy_on_output.on_output(_, output)
      captured_output = output
    end

    server.client.initialize = function(self, request)
      self:send_response(request, {})
      self:send_event("initialized", {})
      self:send_event("output", {
        category = "stdout",
        output = "dummy output"
      })
    end

    run_and_wait_until_initialized({
      type = "dummy_on_output",
      request = "launch",
      name = "dummy"
    }, server)

    assert.are.same(captured_output, {
      category = "stdout",
      output = "dummy output"
    })
  end)
end)
```

## File: `spec/launch.json`
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "request": "launch",
            "name": "java test"
        },
        {
            "type": "bar",
            "request": "attach",
            "name": "bar test"
        }
    ]
}
```

## File: `spec/pipe_spec.lua`
```
local dap = require('dap')

local function wait(predicate, msg)
  vim.wait(1000, predicate)
  local result = predicate()
  assert.are_not.same(false, result, msg and vim.inspect(msg()) or nil)
  assert.are_not.same(nil, result)
end


describe('dap with fake pipe server', function()
  local server
  before_each(function()
    server = require('spec.server').spawn({ new_sock = vim.loop.new_pipe })
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    server.stop()
    dap.close()
    require('dap.breakpoints').clear()
    wait(function() return dap.session() == nil end)
  end)
  it("can connect and terminate", function()
    local config = {
      type = 'dummy',
      request = 'launch',
      name = 'Launch file',
    }
    dap.run(config)
    wait(function()
      local session = dap.session()
      return session and session.initialized and #server.spy.requests == 2
    end)
    local session = dap.session()
    assert.is_not_nil(session)
    assert.are.same(1, server.client.num_connected)
    dap.terminate()
    wait(function()
      return (
        dap.session() == nil
        and #server.spy.events == 2
        and server.spy.events[2].event == "terminated"
        and server.client.num_connected == 0
      )
    end, function() return server.spy.events end)
    assert.is_nil(dap.session())
    assert(session)
    assert.is_true(session.closed)
    ---@diagnostic disable-next-line: invisible
    assert.is_true(session.handle:is_closing())
    assert.are.same(0, server.client.num_connected)
  end)
end)
```

## File: `spec/progress_spec.lua`
```
describe('progress', function()
  local progress = require('dap.progress')

  after_each(progress.reset)

  it('Polling on empty buffer returns nil, report and poll after', function()
    assert.are.same(nil, progress.poll_msg())
    assert.are.same(nil, progress.poll_msg())

    progress.report('hello')
    assert.are.same('hello', progress.poll_msg())
  end)

  it('Interleave report and poll', function()
    progress.report('one')
    progress.report('two')
    assert.are.same('one', progress.poll_msg())
    progress.report('three')
    assert.are.same('two', progress.poll_msg())
    assert.are.same('three', progress.poll_msg())
  end)
  it('Oldest messages are overridden once size limit is reached', function()
    for i = 1, 11 do
      progress.report(tostring(i))
    end
    assert.are.same('2', progress.poll_msg())
    assert.are.same('3', progress.poll_msg())
    progress.report('a')
    assert.are.same('4', progress.poll_msg())
  end)
end)
```

## File: `spec/repl_spec.lua`
```
local dap = require("dap")
local api = vim.api
local helpers = require("spec.helpers")
local repl = require('dap.repl')
local config = {
  type = "dummy",
  request = "launch",
  name = "Launch file",
}


---@param replline string
---@param completion_results dap.CompletionItem[]
local function prepare_session(server, replline, completion_results)
  server.client.initialize = function(self, request)
    self:send_response(request, {
      supportsCompletionsRequest = true,
    })
    self:send_event("initialized", {})
  end
  server.client.completions = function(self, request)
    self:send_response(request, {
      targets = completion_results
    })
  end
  helpers.run_and_wait_until_initialized(config, server)
  local bufnr, win = repl.open()
  api.nvim_set_current_buf(bufnr)
  api.nvim_set_current_win(win)
  api.nvim_buf_set_lines(bufnr, 0, -1, true, {replline})
  api.nvim_win_set_cursor(win, {1, #replline})
end


local function getcompletion_results(server)
  local captured_startcol = nil
  local captured_items = nil

  ---@diagnostic disable-next-line, duplicate-set-field: 211
  function vim.fn.complete(startcol, items)
    captured_startcol = startcol
    captured_items = items
  end

  repl.omnifunc(1, "")

  helpers.wait_for_response(server, "completions")
  helpers.wait(function() return captured_startcol ~= nil end)
  return captured_startcol, captured_items
end


---@param buf integer
---@param lnum integer
local function assert_prompt_mark(buf, lnum)
  if vim.fn.has("nvim-0.12") == 1 then
    local prompt_mark = api.nvim_buf_get_mark(buf, ":")
    assert.are.same(lnum, prompt_mark[1], "prompt mark expected to be in line " .. tostring(lnum))
  end
end


describe('dap.repl', function()
  local prompt_line = vim.fn.has("nvim-0.12") == 1 and "dap> " or ""
  local server
  after_each(function()
    if server then
      dap.terminate()
      server.stop()
      helpers.wait(function() return dap.session() == nil end, "session should become nil")
      server = nil
      dap.adapters.dummy = nil
    end
    repl.execute(".format structured")
    local buf = repl.open()
    api.nvim_buf_delete(buf, {force = true})
  end)

  it("append doesn't add newline with newline = false", function()
    local buf = repl.open()
    repl.append('foo', nil, { newline = false })
    local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
    assert.are.same({"foo", prompt_line}, lines)
    assert_prompt_mark(buf, 2)

    repl.append('bar', nil, { newline = false })
    lines = api.nvim_buf_get_lines(buf, 0, -1, true)
    assert.are.same({"foobar", prompt_line}, lines)
    assert_prompt_mark(buf, 2)

    repl.append('\nbaz\n', nil, { newline = false })
    lines = api.nvim_buf_get_lines(buf, 0, -1, true)
    assert.are.same({"foobar", "baz", "", prompt_line}, lines)
    assert_prompt_mark(buf, 4)
  end)

  it("adds newline with newline = true", function()
    local buf = repl.open()
    assert_prompt_mark(buf, 1)
    repl.append("foo", nil, { newline = true })
    assert_prompt_mark(buf, 2)
    repl.append("bar", nil, { newline = true })
    assert_prompt_mark(buf, 3)
    repl.append("\nbaz\n", nil, { newline = true })
    assert_prompt_mark(buf, 6)

    local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
    assert.are.same({"foo", "bar", "", "baz", "", prompt_line}, lines)
  end)

  it("replaces \\r\\n with \\n", function ()
    local buf = repl.open()
    repl.append("f\roo\r\nbar", nil, { newline = true })
    local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
    assert.are.same({"f\roo", "bar", prompt_line}, lines)
  end)

  it("repl.execute inserts text and executes it, shows result", function()
    server = require("spec.server").spawn()
    dap.adapters.dummy = server.adapter
    server.client.evaluate = function(self, request)
      self:send_response(request, {
        result = "2",
        variablesReference = 0
      })
    end
    helpers.run_and_wait_until_initialized(config, server)
    local buf = repl.open()
    repl.execute("1 + 1")
    local commands = helpers.wait_for_response(server, "evaluate")
    assert.are.same({"initialize", "launch", "evaluate"}, commands)
    helpers.wait(
      function()
        local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
        return lines[2] == "2"
      end,
      function()
        return api.nvim_buf_get_lines(buf, 0, -1, true)
      end
    )
    local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
    assert.are.same({"dap> 1 + 1", "2", prompt_line}, lines)
    assert_prompt_mark(buf, 3)
  end)
  it("repl.execute shows structured results", function()
    server = require("spec.server").spawn()
    dap.adapters.dummy = server.adapter
    server.client.evaluate = function(self, request)
      self:send_response(request, {
        result = "table xy",
        variablesReference = 1
      })
    end
    server.client.variables = function(self, request)
      self:send_response(request, {
        variables = {
          {
            name = "x",
            value = 1,
            variablesReference = 0
          },
          {
            name = "y",
            value = 2,
            variablesReference = 0
          }
        }
      })
    end
    helpers.run_and_wait_until_initialized(config, server)
    local buf = repl.open()
    repl.execute("tbl")
    local commands = helpers.wait_for_response(server, "evaluate")
    assert.are.same({"initialize", "launch", "evaluate"}, commands)
    helpers.wait(
      function()
        local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
        return lines[2] == "table xy"
      end,
      function()
        return api.nvim_buf_get_lines(buf, 0, -1, true)
      end
    )
    local expected = {
      "dap> tbl",
      "table xy",
      "  x: 1",
      "  y: 2",
      prompt_line,
    }
    assert.are.same(expected, api.nvim_buf_get_lines(buf, 0, -1, true))
    assert_prompt_mark(buf, 5)

    server.spy.clear()
    repl.execute("tbl")
    commands = helpers.wait_for_response(server, "evaluate")
    assert.are.same({"evaluate"}, commands)
    helpers.wait(
      function()
        local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
        return lines[6] == "table xy"
      end,
      function()
        return api.nvim_buf_get_lines(buf, 0, -1, true)
      end
    )
    expected = {
      "dap> tbl",
      "table xy",
      "  x: 1",
      "  y: 2",
      "dap> tbl",
      "table xy",
      "  x: 1",
      "  y: 2",
      prompt_line,
    }
    assert.are.same(expected, api.nvim_buf_get_lines(buf, 0, -1, true))
  end)
end)


describe("dap.repl completion", function()
  local server
  before_each(function()
    server = require("spec.server").spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    dap.terminate()
    server.stop()
    require('dap.breakpoints').clear()
    helpers.wait(function() return dap.session() == nil end, "session should become nil")
    local repl_buf = repl.open()
    api.nvim_buf_delete(repl_buf, { force = true })
  end)
  it("Uses start position from completion response", function()
    prepare_session(server, "dap> com. ", {
        {
          label = "com.sun.org.apache.xpath",
          number = 0,
          sortText = "999999183",
          start = 0,
          text = "sun.org.apache.xpath",
          type = "module"
        }
    })

    local startcol, items = getcompletion_results(server)
    assert.are.same(#"dap> com." + 1, startcol)
    local expected_items = {
      {
        abbr = "com.sun.org.apache.xpath",
        dup = 0,
        icase = 1,
        word = "sun.org.apache.xpath"
      }
    }
    assert.are.same(expected_items, items)
  end)

  it("Can handle responses without explicit start column and prefix overlap", function()
    prepare_session(server, "dap> info b", {
        {
          label = "info b",
          length = 6,
        },
        {
          label = "info bookmarks",
          length = 14,
        },
        {
          label = "info breakpoints",
          length = 16,
        }
    })

    local startcol, items = getcompletion_results(server)
    assert.are.same(#"dap> " + 1 , startcol)
    local expected_items = {
      {
        abbr = 'info b',
        dup = 0,
        icase = 1,
        word = 'info b',
      },
      {
        abbr = 'info bookmarks',
        dup = 0,
        icase = 1,
        word = 'info bookmarks',
      },
      {
        abbr = 'info breakpoints',
        dup = 0,
        icase = 1,
        word = 'info breakpoints',
      }
    }
    assert.are.same(expected_items, items)
  end)

  it("Can handle responses with explicit start column and prefix overlap", function()
    prepare_session(server, "dap> `info b", {
      {
        label = "`info bookmarks",
        length = 15,
        start = 0,
        type = "text"
      },
      {
        label = "`info breakpoints",
        length = 17,
        start = 0,
        type = "text"
      }
    })

    local startcol, items = getcompletion_results(server)
    assert.are.same(#"dap> " + 1, startcol)
    local expected_items = {
      {
        abbr = '`info bookmarks',
        dup = 0,
        icase = 1,
        word = '`info bookmarks',
      },
      {
        abbr = '`info breakpoints',
        dup = 0,
        icase = 1,
        word = '`info breakpoints',
      }
    }
    assert.are.same(expected_items, items)
  end)
end)
```

## File: `spec/run_server.lua`
```
local server = require('spec.server')
local opts = {
  port = _G.DAP_PORT
}
io.stdout:setvbuf("no")
io.stderr:setvbuf("no")
local debug_adapter = server.spawn(opts)
io.stderr:write("Listening on port=" .. debug_adapter.adapter.port .. "\n")
local original_disconnect = debug_adapter.client.disconnect
debug_adapter.client.disconnect = function(self, request)
  original_disconnect(self, request)
  os.exit(0)
end
vim.loop.run()
vim.loop.walk(vim.loop.close)
vim.loop.run()
```

## File: `spec/server.lua`
```
local uv = vim.loop
local rpc = require('dap.rpc')

local json_decode = vim.json.decode
local json_encode = vim.json.encode

local M = {}
local Client = {}


function Client:send_err_response(request, message, error)
  self.seq = request.seq + 1
  local payload = {
    seq = self.seq,
    type = 'response',
    command = request.command,
    success = false,
    request_seq = request.seq,
    message = message,
    body = {
      error = error,
    },
  }
  if self.socket then
    self.socket:write(rpc.msg_with_content_length(json_encode(payload)))
  end
  table.insert(self.spy.responses, payload)
end


function Client:send_response(request, body)
  self.seq = request.seq + 1
  local payload = {
    seq = self.seq,
    type = 'response',
    command = request.command,
    success = true,
    request_seq = request.seq,
    body = body,
  }
  if self.socket then
    self.socket:write(rpc.msg_with_content_length(json_encode(payload)))
  end
  table.insert(self.spy.responses, payload)
end


function Client:send_event(event, body)
  self.seq = self.seq + 1
  local payload = {
    seq = self.seq,
    type = 'event',
    event = event,
    body = body,
  }
  if self.socket then
    self.socket:write(rpc.msg_with_content_length(json_encode(payload)))
  end
  table.insert(self.spy.events, payload)
end


---@param command string
---@param arguments any
function Client:send_request(command, arguments)
  self.seq = self.seq + 1
  local payload = {
    seq = self.seq,
    type = "request",
    command = command,
    arguments = arguments,
  }
  self.socket:write(rpc.msg_with_content_length(json_encode(payload)))
end


function Client:handle_input(body)
  local request = json_decode(body)
  table.insert(self.spy.requests, request)
  local handler = self[request.command]
  if handler then
    handler(self, request)
  else
    print('no handler for ' .. request.command)
  end
end


function Client:initialize(request)
  self:send_response(request, {})
  self:send_event('initialized', {})
end


function Client:disconnect(request)
  self:send_event('terminated', {})
  self:send_response(request, {})
end


function Client:terminate(request)
  self:send_event('terminated', {})
  self:send_response(request, {})
end


function Client:launch(request)
  self:send_response(request, {})
end


function M.spawn(opts)
  opts = opts or {}
  opts.mode = opts.mode or "tcp"
  local spy = {
    requests = {},
    responses = {},
    events = {},
  }
  function spy.clear()
    spy.requests = {}
    spy.responses = {}
    spy.events = {}
  end
  local adapter
  local server
  if opts.mode == "tcp" then
    server = assert(uv.new_tcp())
    assert(server:bind("127.0.0.1", opts.port or 0), "Must be able to bind to ip:port")
    adapter = {
      type = "server",
      host = "127.0.0.1",
      port = server:getsockname().port,
      options = {
        disconnect_timeout_sec = 0.1
      }
    }
  else
    server = assert(uv.new_pipe())
    local pipe = os.tmpname()
    os.remove(pipe)
    assert(server:bind(pipe), "Must be able to bind to pipe")
    adapter = {
      type = "pipe",
      pipe = pipe,
      options = {
        disconnect_timeout_sec = 0.1
      }
    }
  end
  local client = {
    seq = 0,
    handlers = {},
    spy = spy,
    num_connected = 0,
  }
  setmetatable(client, {__index = Client})
  server:listen(128, function(err)
    assert(not err, err)
    client.num_connected = client.num_connected + 1
    local socket = assert(opts.mode == "tcp" and uv.new_tcp() or uv.new_pipe())
    client.socket = socket
    server:accept(socket)
    local function on_chunk(body)
      client:handle_input(body)
    end
    local function on_eof()
      client.num_connected = client.num_connected - 1
    end
    socket:read_start(rpc.create_read_loop(on_chunk, on_eof))
  end)
  return {
    client = client,
    adapter = adapter,
    spy = spy,
    stop = function()
      if opts.mode ~= "tcp" then
        pcall(os.remove, adapter.pipe)
      end
      if client.socket then
        client.socket:shutdown(function()
          client.socket:close()
          client.socket = nil
        end)
      end
    end,
  }
end


return M
```

## File: `spec/server_executable_spec.lua`
```
local helpers = require("spec.helpers")
local wait = helpers.wait
local run_and_wait_until_initialized = helpers.run_and_wait_until_initialized
local uv = vim.uv or vim.loop

local spec_root = vim.fn.fnamemodify(debug.getinfo(1, "S").source:match("@?(.*/)"), ":h:p")

local dap = require('dap')
dap.adapters.dummy = {
  type = 'server',
  port = '${port}',
  executable = {
    command = vim.v.progpath,
    args = {
      '-Es',
      '-u', 'NONE',
      '--headless',
      '-c', 'set rtp+=.',
      '-c', 'lua DAP_PORT=${port}',
      '-c', ('luafile %s/run_server.lua'):format(spec_root)
    },
  }
}

describe('server executable', function()
  before_each(function()
  end)
  after_each(function()
    dap.terminate()
    vim.wait(100, function()
      return dap.session() == nil
    end)
    assert.are.same(nil, dap.session())
  end)

  it('Starts adapter executable and connects', function()
    local config = {
      type = 'dummy',
      request = 'launch',
      name = 'Launch',
    }
    local log = require("dap.log").create_logger("dap-dummy-stderr.log")
    local session = run_and_wait_until_initialized(config)
    local adapter = session.adapter --[[@as dap.ServerAdapter]]
    assert.are.same(adapter.port, tonumber(adapter.executable.args[8]:match("(%d+)$")))
    assert.are.same(true, session.initialized, "initialized must be true")

    local expected_msg = "Listening on port=" .. adapter.port .. "\n"
    log._file:flush()
    local f = io.open(log._path, "r")
    assert(f)
    local content = f:read("*a")
    f:close()
    assert.are.same(expected_msg, content)

    dap.terminate()
    wait(function() return dap.session() == nil end, "Must remove session")
    wait(function() return uv.fs_stat(log._path) == nil end)
    assert.is_nil(dap.session())
    assert.is_nil(uv.fs_stat(log._path))
  end)

  it('Clears session after closing', function()
    local config = {
      type = 'dummy',
      request = 'launch',
      name = 'Launch',
    }
    local session = run_and_wait_until_initialized(config)
    assert.are.same(true, session.initialized, "initialized must be true")
    dap.close()
    wait(function() return dap.session() == nil end, "Must remove session")
    assert.are.same(nil, dap.session())
  end)
end)
```

## File: `spec/sessions_spec.lua`
```
local dap = require('dap')


local function wait(predicate, msg)
  vim.wait(1000, predicate)
  local result = predicate()
  assert.are_not.same(false, result, msg and vim.inspect(msg()) or nil)
  assert.are_not.same(nil, result)
end


local function run_and_wait_until_initialized(conf, server)
  dap.run(conf)
  wait(function()
    local session = dap.session()
    -- wait for initialize and launch requests
    return (session and session.initialized and #server.spy.requests == 2)
  end)
  return assert(dap.session(), "Must have session after dap.run")
end


describe('sessions', function()
  local srv1
  local srv2

  before_each(function()
    srv1 = require('spec.server').spawn()
    srv2 = require('spec.server').spawn()
    dap.adapters.dummy1 = srv1.adapter
    dap.adapters.dummy2 = srv2.adapter
  end)
  after_each(function()
    srv1.stop()
    srv2.stop()
    dap.terminate()
    dap.terminate()
  end)
  it('can run multiple sessions', function()
    local conf1 = {
      type = 'dummy1',
      request = 'launch',
      name = 'Launch file 1',
    }
    local conf2 = {
      type = 'dummy2',
      request = 'launch',
      name = 'Launch file 2',
    }
    local s1 = run_and_wait_until_initialized(conf1, srv1)
    local s2 = run_and_wait_until_initialized(conf2, srv2)
    assert.are.same(2, #dap.sessions())
    assert.are.not_same(s1.id, s2.id)

    dap.terminate()
    wait(function() return #dap.sessions() == 1 end, function() return dap.sessions() end)
    assert.are.same(true, s2.closed)
    assert.are.same(false, s1.closed)
    assert.are.same(s1, dap.session())

    dap.terminate()
    wait(function() return #dap.sessions() == 0 end, function() return dap.sessions() end)
    assert.are.same(nil, dap.session())
  end)

  it("startDebugging starts a child session", function()
    local conf1 = {
      type = 'dummy1',
      request = 'launch',
      name = 'Launch file 1',
    }
    run_and_wait_until_initialized(conf1, srv1)
    srv1.client:send_request("startDebugging", {
      request = "launch",
      configuration = {
        type = "dummy2",
        name = "Subprocess"
      }
    })
    wait(
      function() return vim.tbl_count(dap.session().children) == 1 end,
      function() return dap.session() end
    )
    local _, child = next(dap.session().children)
    assert.are.same("Subprocess", child.config.name)

    srv2.stop()
    wait(function() return vim.tbl_count(dap.session().children) == 0 end)
    assert.are.same({}, dap.session().children)
  end)

  it("startDebugging connects to root adapter if type server with executable", function()
    local conf1 = {
      type = 'dummy1',
      request = 'launch',
      name = 'Launch file 1',
    }
    local session = run_and_wait_until_initialized(conf1, srv1)
    assert.are.same(1, srv1.client.num_connected)
    dap.adapters.dummy2 = {
      type = "server",
      executable = {
        command = "echo",
        args = {"not", "used"},
      }
    }
    srv1.client:send_request("startDebugging", {
      request = "launch",
      configuration = {
        type = "dummy2",
        name = "Subprocess"
      }
    })
    wait(
      function() return vim.tbl_count(session.children) == 1 end,
      function() return dap.session() end
    )
    assert.are.same(2, srv1.client.num_connected)
    dap.terminate()
  end)
end)
```

## File: `spec/ui_spec.lua`
```
local api = vim.api
local ui = require('dap.ui')

describe('ui', function()
  describe('layered buf', function()

    -- note that test cases build on each other
    local render_item = function(x) return x.label end
    local buf = api.nvim_create_buf(true, true)
    local layer = ui.layer(buf)

    it('can append items to empty buffer', function()
      local items = {
        { label = "aa", x = 1 },
        { label = "", x = 3 },
        { label = "dd", x = 4 },
      }
      layer.render(items, render_item)
      local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({
        'aa',
        '',
        'dd',
      }, lines)

      assert.are.same(3, vim.tbl_count(layer.__marks))
      for i = 1, #items do
        assert.are.same(items[i], layer.get(i - 1).item)
      end
    end)

    it('can append at arbitrary position', function()
      layer.render({{ label = "bb", x = 2 },}, render_item, nil, 1)
      local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({
        'aa',
        'bb',
        '',
        'dd',
      }, lines)
      assert.are.same('aa', layer.get(0).item.label)
      assert.are.same('bb', layer.get(1).item.label)
      assert.are.same('', layer.get(2).item.label)
    end)

    it('can override a region', function()
      local items = {
        { label = "bbb", x = 22 },
        { label = "bbbb", x = 222 },
      }
      layer.render(items, render_item, nil, 1, 2)
      local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({
        'aa',
        'bbb',
        'bbbb',
        '',
        'dd',
      }, lines)
      assert.are.same('aa', layer.get(0).item.label)
      assert.are.same('bbb', layer.get(1).item.label)
      assert.are.same('bbbb', layer.get(2).item.label)
      assert.are.same('', layer.get(3).item.label)
    end)

    it('can append at the end', function()
      layer.render({{ label = "e" }}, render_item, nil, nil, nil)
      local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({
        'aa',
        'bbb',
        'bbbb',
        '',
        'dd',
        'e',
      }, lines)
      assert.are.same('dd', layer.get(4).item.label)
      assert.are.same('e', layer.get(5).item.label)
    end)
  end)

  local opts = {
    get_key = function(val) return val.name end,
    render_parent = function(val) return val.name end,
    has_children = function(val) return val.children end,
    get_children = function(val) return val.children end
  }

  describe('tree can render a tree structure', function()
    local tree = ui.new_tree(opts)
    local buf = api.nvim_create_buf(true, true)
    local layer = ui.layer(buf)
    local d = { name = 'd' }
    local c = { name = 'c', children = { d, } }
    local b = { name = 'b', children = { c, } }
    local a = { name = 'a' }
    local root = {
      name = 'root',
      children = { a, b }
    }
    local root_copy = vim.deepcopy(root)
    tree.render(layer, root)
    local lines = api.nvim_buf_get_lines(buf, 0, -1, true)
    assert.are.same({
      'root',
      '  a',
      '  b',
    }, lines)

    it('can expand an element with children', function()
      local lnum = 2
      local info = layer.get(lnum)
      info.context.actions[1].fn(layer, info.item, lnum, info.context)
      lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({
        'root',
        '  a',
        '  b',
        '    c',
      }, lines)

      lnum = 3
      info = layer.get(lnum)
      info.context.actions[1].fn(layer, info.item, lnum, info.context)
      lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({
        'root',
        '  a',
        '  b',
        '    c',
        '      d',
      }, lines)
    end)

    it('can render with new data and previously expanded elements are still expanded', function()
      layer.render({}, tostring, nil, 0, -1)
      lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({''}, lines)
      tree.render(layer, root_copy)
      lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({
        'root',
        '  a',
        '  b',
        '    c',
        '      d',
      }, lines)
    end)

    it('can collapse an expanded item', function()
      local lnum = 2
      local info = layer.get(lnum)
      info.context.actions[1].fn(layer, info.item, lnum, info.context)
      lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({
        'root',
        '  a',
        '  b',
      }, lines)
    end)

    it('can re-use a subnode in a different tree', function()
      local lnum = 2
      local info = layer.get(lnum)
      info.context.actions[1].fn(layer, info.item, lnum, info.context)
      lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({
        'root',
        '  a',
        '  b',
        '    c',
      }, lines)
      layer.render({}, tostring, nil, 0, -1)
      local subtree = ui.new_tree(opts)
      subtree.render(layer, b)
      lines = api.nvim_buf_get_lines(buf, 0, -1, true)
      assert.are.same({
        'b',
        '  c',
      }, lines)
    end)
  end)
end)
```

## File: `spec/utils_spec.lua`
```
local utils = require('dap.utils')

describe('utils.index_of', function()
  it('returns index of first item where predicate matches', function()
    local result = require('dap.utils').index_of(
      {'a', 'b', 'c'},
      function(x) return x == 'b' end
    )
    assert.are.same(2, result)
  end)
end)

describe('utils.to_dict', function()
  it('converts a list to a dictionary', function()
    local values = { { k='a', val=1 }, { k='b', val = 2 } }
    local result = require('dap.utils').to_dict(
      values,
      function(x) return x.k end,
      function(x) return x.val end
    )
    local expected = {
      a = 1,
      b = 2
    }
    assert.are.same(expected, result)
  end)

  it('supports nil values as argument', function()
    local result = require('dap.utils').to_dict(nil, function(x) return x end)
    assert.are.same(result, {})
  end)
end)


describe('utils.non_empty', function()
  it('non_empty returns true on non-empty dicts with numeric keys', function()
    local d = {
      [20] = 'a',
      [30] = 'b',
    }
    local result = require('dap.utils').non_empty(d)
    assert.are.same(true, result)
  end)
end)

describe('utils.fmt_error', function ()
  it('interpolates message objects with variables', function ()
    assert.are.equal('Hello, John!', require('dap.utils').fmt_error({
      body = {
        error = {
          showUser = true,
          format = '{greeting}, {name}!',
          variables = {
            greeting = 'Hello',
            name = 'John',
          }
        }
      }
    }))
  end)

  it('interpolates message objects without variables', function ()
    assert.are.equal('Hello, John!', require('dap.utils').fmt_error({
      body = {
        error = {
          showUser = true,
          format = 'Hello, John!',
        }
      }
    }))
  end)

  it('return message if showUser is false', function ()
    assert.are.equal('Something went wrong.', require('dap.utils').fmt_error({
      message = 'Something went wrong.',
      body = {
        error = {
          showUser = false,
          format = 'Hello, John!',
        }
      }
    }))
  end)

  it('can handle response without body part', function()
    local result = utils.fmt_error({
      message = 'Bad things happen',
    })
    assert.are.same('Bad things happen', result)
  end)
end)

describe('utils.splitstr', function ()
  if vim.fn.has("nvim-0.10") == 0 then
    return
  end
  it('works with plain string', function ()
    assert.are.same({"hello", "world"}, utils.splitstr("hello world"))
  end)

  it('works extra whitespace', function ()
    assert.are.same({"hello", "world"}, utils.splitstr('hello  	world'))
  end)

  it('empty quoted', function ()
    assert.are.same({"hello", "", "world"}, utils.splitstr('hello "" world'))
  end)

  it('with double quoted string', function ()
    assert.are.same({'with', 'double quoted', 'string'}, utils.splitstr('with "double quoted" string'))
  end)

  it("with single quoted string", function ()
    assert.are.same({'with', 'single quoted', 'string'}, utils.splitstr("with 'single quoted' string"))
  end)

  it("with unbalanced quote", function ()
    assert.are.same({"with", "\"single", "quoted", "string"}, utils.splitstr("with \"single quoted string"))
  end)

  it("with unbalanced single quoted string", function ()
    assert.are.same({"with", "'single", "quoted", "string"}, utils.splitstr("with 'single quoted string"))
  end)

  it('escaped quote', function ()
    assert.are.same({'foo', '"bar'}, utils.splitstr([[foo \"bar]]))
  end)

  it("returns empty list for empty strings", function ()
    assert.are.same({}, utils.splitstr(""))
    assert.are.same({}, utils.splitstr("  "))
  end)
  it("trims leading and trailing whitespace", function ()
    assert.are.same({"a"}, utils.splitstr("a   "))
    assert.are.same({"a", "b"}, utils.splitstr("     a       b   "))
  end)

  it("mixed and balanced quotes", function ()
    assert.are.same({"abc", 'def', 'ghi'}, utils.splitstr([['a'b'c' d"e"f "g"'h'i]]))
  end)
end)

describe("trim_procname", function()
  it("trims long full paths to name", function()
    local name = utils._trim_procname("/usr/bin/foobar", 10, 4)
    assert.are.same("foobar", name)
  end)

  it("drops arguments if there are too many", function()
    local name = utils._trim_procname("cmd --one --two --three", 15, 5)
    assert.are.same("cmd --one --two [‥]", name)
  end)

  it("trims long arguments", function()
    local name = utils._trim_procname("foobar --too-long-sorry", 20, 8)
    assert.are.same("foobar ‥ong-sorry", name)
  end)
end)
```

## File: `spec/widgets_spec.lua`
```
local dap = require('dap')
local widgets = require("dap.ui.widgets")
local api = vim.api
local helpers = require("spec.helpers")

local config = {
  type = 'dummy',
  request = 'launch',
  name = 'Launch file',
}


describe("hover widget", function()

  local server
  before_each(function()
    server = require('spec.server').spawn()
    dap.adapters.dummy = server.adapter
  end)
  after_each(function()
    server.stop()
    dap.close()
    require('dap.breakpoints').clear()
    helpers.wait(function() return dap.session() == nil end, "session should become nil")
  end)

  it("evaluates expression with hover context", function()
    server.client.initialize = function(self, request)
      self:send_response(request, {
        supportsEvaluateForHovers = true,
      })
      self:send_event("initialized", {})
    end
    server.client.evaluate = function(self, request)
      self:send_response(request, {
        result = "2",
        variablesReference = 0,
      })
    end
    helpers.run_and_wait_until_initialized(config, server)
    server.spy.clear()
    local buf = api.nvim_create_buf(false, true)
    api.nvim_buf_set_lines(buf, 0, -1, true, {"foo", "bar"})
    api.nvim_set_current_buf(buf)
    api.nvim_win_set_cursor(0, {1, 0})
    widgets.hover("1 + 1")
    local commands = helpers.wait_for_response(server, "evaluate")
    assert.are.same({"evaluate"}, commands)
    assert.are.same("hover", server.spy.requests[1].arguments.context)
    assert.are.same("1 + 1", server.spy.requests[1].arguments.expression)
  end)
end)
```

