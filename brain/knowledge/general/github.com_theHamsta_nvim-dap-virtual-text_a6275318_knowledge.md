---
id: github.com-thehamsta-nvim-dap-virtual-text-a627531
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:27.274335
---

# KNOWLEDGE EXTRACT: github.com_theHamsta_nvim-dap-virtual-text_a6275318
> **Extracted on:** 2026-04-01 08:19:08
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519403/github.com_theHamsta_nvim-dap-virtual-text_a6275318

---

## File: `.gitignore`
```
.luacheckcache
```

## File: `.luacheckrc`
```
-- Rerun tests only if their modification time changed.
cache = true

-- Glorious list of warnings: https://luacheck.readthedocs.io/en/stable/warnings.html
ignore = {
  "212", -- Unused argument, In the case of callback function, _arg_name is easier to understand than _, so this option is set to off.
  "411", -- Redefining a local variable.
  "412", -- Redefining an argument.
  "421", -- Shadowing a variable
  "422", -- Shadowing an argument
  "431", -- Shadowing a variable
  "122" -- Indirectly setting a readonly global
}

-- Global objects defined by the C code
read_globals = {
  "vim",
}
```

## File: `.stylua.toml`
```
indent_type = "Spaces"
indent_width = 2
no_call_parentheses = true
quote_style = "AutoPreferSingle"
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
# nvim-dap-virtual-text

This plugin adds virtual text support to [nvim-dap](https://github.com/mfussenegger/nvim-dap).
[nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter) is used to find variable definitions.

```vim
Plug 'mfussenegger/nvim-dap'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'theHamsta/nvim-dap-virtual-text'
```

> [!NOTE]
>
> With Neovim 0.9 and above, `nvim-treesitter` is not hard a dependency.
> This plugin only needs the parsers for the languages you want to use it with
> and `locals.scm` queries defining references and definitions of variables
> (typically provided by nvim-treesitter).

The hlgroup for the virtual text is `NvimDapVirtualText` (linked to `Comment`).
Exceptions that caused the debugger to stop are displayed as `NvimDapVirtualTextError`
(linked to `DiagnosticVirtualTextError`). Changed and new variables will be highlighted with
`NvimDapVirtualTextChanged` (default linked to `DiagnosticVirtualTextWarn`).

The behavior of this plugin can be activated and controlled via a `setup` call

```lua
require("nvim-dap-virtual-text").setup()
```

Wrap this call with `lua <<EOF` when you are using viml for your config:

```vim
lua <<EOF
require("nvim-dap-virtual-text").setup()
EOF
```

or with additional options:
```lua
require("nvim-dap-virtual-text").setup {
    enabled = true,                        -- enable this plugin (the default)
    enabled_commands = true,               -- create commands DapVirtualTextEnable, DapVirtualTextDisable, DapVirtualTextToggle, (DapVirtualTextForceRefresh for refreshing when debug adapter did not notify its termination)
    highlight_changed_variables = true,    -- highlight changed values with NvimDapVirtualTextChanged, else always NvimDapVirtualText
    highlight_new_as_changed = false,      -- highlight new variables in the same way as changed variables (if highlight_changed_variables)
    show_stop_reason = true,               -- show stop reason when stopped for exceptions
    commented = false,                     -- prefix virtual text with comment string
    only_first_definition = true,          -- only show virtual text at first definition (if there are multiple)
    all_references = false,                -- show virtual text on all all references of the variable (not only definitions)
    clear_on_continue = false,             -- clear virtual text on "continue" (might cause flickering when stepping)
    --- A callback that determines how a variable is displayed or whether it should be omitted
    --- @param variable Variable https://microsoft.github.io/debug-adapter-protocol/specification#Types_Variable
    --- @param buf number
    --- @param stackframe dap.StackFrame https://microsoft.github.io/debug-adapter-protocol/specification#Types_StackFrame
    --- @param node userdata tree-sitter node identified as variable definition of reference (see `:h tsnode`)
    --- @param options nvim_dap_virtual_text_options Current options for nvim-dap-virtual-text
    --- @return string|nil A text how the virtual text should be displayed or nil, if this variable shouldn't be displayed
    display_callback = function(variable, buf, stackframe, node, options)
    -- by default, strip out new line characters
      if options.virt_text_pos == 'inline' then
        return ' = ' .. variable.value:gsub("%s+", " ")
      else
        return variable.name .. ' = ' .. variable.value:gsub("%s+", " ")
      end
    end,
    -- position of virtual text, see `:h nvim_buf_set_extmark()`, default tries to inline the virtual text. Use 'eol' to set to end of line
    virt_text_pos = vim.fn.has 'nvim-0.10' == 1 and 'inline' or 'eol',

    -- experimental features:
    all_frames = false,                    -- show virtual text for all stack frames not only current. Only works for debugpy on my machine.
    virt_lines = false,                    -- show virtual lines instead of virtual text (will flicker!)
    virt_text_win_col = nil                -- position the virtual text at a fixed window column (starting from the first text column) ,
                                           -- e.g. 80 to position at column 80, see `:h nvim_buf_set_extmark()`
}
```

With support for inline virtual text (nvim 0.10), `virt_text_pos = 'inline'`

![image](https://user-images.githubusercontent.com/7189118/236633778-5e18c02c-4415-46a4-b903-6ee06764ef2a.png)


With `highlight_changed_variables = false, all_frames = false`

![current_frame](https://user-images.githubusercontent.com/7189118/81495691-5d937400-92b2-11ea-8995-17daeda593cc.gif)

With `highlight_changed_variables = false, all_frames = true`

![all_scopes](https://user-images.githubusercontent.com/7189118/81495701-6b48f980-92b2-11ea-8df4-dd476dc825bc.gif)

It works for all languages with `locals.scm` in nvim-treesitter (`@definition.var` is required for variable definitions).
This should include C/C++, Python, Rust, Go, Java...

![image](https://user-images.githubusercontent.com/7189118/82733259-f4304e00-9d12-11ea-90da-addebada2e18.png)

![image](https://user-images.githubusercontent.com/7189118/91160889-485c1d00-e6ca-11ea-9c70-e329c50ed1e1.png)

The virtual text can additionally use a comment-like syntax to further improve distinguishability between actual code and debugger info by setting the following option:
```lua
require("nvim-dap-virtual-text").setup {
  commented = true,
}
```

This will use the `commentstring` option to choose the appropriate comment-syntax for the current filetype

![image](https://user-images.githubusercontent.com/6146545/134688673-49c86368-ed51-4f16-82b4-fce05bcd9767.PNG)

With `virt_text_win_col = 80, highlight_changed_variables = true` (x has just changed its value)

![image](https://user-images.githubusercontent.com/7189118/139598856-d45e02ef-62f6-4f7e-a619-ed9b48d53cc1.png)


## Show Stop Reason on Exception

![image](https://user-images.githubusercontent.com/7189118/115946315-b3136180-a4c0-11eb-8d8b-980b11464448.png)
![image](https://user-images.githubusercontent.com/7189118/115946346-db9b5b80-a4c0-11eb-8582-6075d818d869.png)

Exception virtual text can be deactivated via

```lua
require("nvim-dap-virtual-text").setup {
  show_stop_reason = false,
}
```
```

## File: `lua/nvim-dap-virtual-text.lua`
```
--
-- nvim-dap-virtual-text.lua
-- Copyright (C) 2020 Stephan Seitz <stephan.seitz@fau.de>
--
-- Distributed under terms of the GPLv3 license.
--
local M = {}

local dap = require 'dap'

local plugin_id = 'nvim-dap-virtual-text'

---@class VariablePresentationHint
---@field kind 'property' | 'method' | 'class' | 'data' | 'event' | 'baseClass' | 'innerClass' | 'interface'
--- | 'mostDerivedClass'
--- | 'virtual'
--- | 'dataBreakpoint'
--- | string
--- | nil
---@field attributes ('static' | 'constant' | 'readOnly' | 'rawString' | 'hasObjectId' | 'canHaveObjectId'
--- | 'hasSideEffects'
--- | 'hasDataBreakpoint'
--- | string)[] | nil
---@field visibility 'public' | 'private' | 'protected' | 'internal' | 'final' | string | nil
---@field lazy boolean|nil

--- @class Variable
--- @field name string
--- @field value string
--- @field type string|nil
--- @field presentationHint VariablePresentationHint|nil
--- @field evaluateName string|nil
--- @field variablesReference number
--- @field namedVariables number|nil
--- @field indexedVariables number|nil
--- @field memoryReference string|nil

---@class nvim_dap_virtual_text_options
local options = {
  -- enable this plugin (the default)
  enabled = true,
  -- create commands `DapVirtualTextEnable`, `DapVirtualTextDisable`, `DapVirtualTextToggle`,
  -- (`DapVirtualTextForceRefresh` for refreshing when debug adapter did not notify its termination)
  enable_commands = true,
  -- show virtual text for all stack frames not only current. Only works for debugpy on my machine.
  all_frames = false,
  -- prefix virtual text with comment string
  commented = false,
  -- highlight changed values with `NvimDapVirtualTextChanged`, else always `NvimDapVirtualText`
  highlight_changed_variables = true,
  -- highlight new variables in the same way as changed variables (if highlight_changed_variables)
  highlight_new_as_changed = false,
  -- show stop reason when stopped for exceptions
  show_stop_reason = true,
  -- only show virtual text at first definition (if there are multiple)
  only_first_definition = true,
  -- show virtual text on all all references of the variable (not only definitions)
  all_references = false,
  -- clear virtual text on "continue" (might cause flickering when stepping)
  clear_on_continue = false,
  text_prefix = '',
  separator = ',',
  error_prefix = '  ',
  info_prefix = '  ',
  -- position of virtual text, see `:h nvim_buf_set_extmark()`
  virt_text_pos = vim.fn.has 'nvim-0.10' == 1 and 'inline' or 'eol',
  -- show virtual lines instead of virtual text (will flicker!)
  virt_lines = false,
  virt_lines_above = true,
  -- position the virtual text at a fixed window column (starting from the first text column) ,
  -- e.g. `80` to position at column `80`, see `:h nvim_buf_set_extmark()`
  virt_text_win_col = nil,
  -- filter references (not definitions) pattern when `all_references` is activated
  -- (Lua gmatch pattern, default filters out Python modules)
  --- @deprecated Use display_callback instead with nil return value instead!
  filter_references_pattern = '<module',
  --- A callback that determines how a variable is displayed or whether it should be omitted
  --- @param variable Variable https://microsoft.github.io/debug-adapter-protocol/specification#Types_Variable
  --- @param buf number
  --- @param stackframe dap.StackFrame https://microsoft.github.io/debug-adapter-protocol/specification#Types_StackFrame
  --- @param node userdata tree-sitter node identified as variable definition of reference (see `:h tsnode`)
  --- @param options nvim_dap_virtual_text_options Current options for nvim-dap-virtual-text
  --- @return string|nil text how the virtual text should be displayed or nil, if this variable shouldn't be displayed
  --- @diagnostic disable-next-line: unused-local
  display_callback = function(variable, buf, stackframe, node, options)
    -- by default, strip out new line characters
    if options.virt_text_pos == 'inline' then
      return ' = ' .. variable.value:gsub('%s+', ' ')
    else
      return variable.name .. ' = ' .. variable.value:gsub('%s+', ' ')
    end
  end,
}

function M.refresh(session)
  session = session or dap.session()
  local virtual_text = require 'nvim-dap-virtual-text/virtual_text'

  virtual_text.clear_virtual_text()

  if not options.enabled then
    return
  end
  if not session then
    return
  end

  if options.all_frames and session.threads and session.threads[session.stopped_thread_id] then
    local frames = session.threads[session.stopped_thread_id].frames
    for _, f in pairs(frames or {}) do
      virtual_text.set_virtual_text(f, options)
    end
  else
    virtual_text.set_virtual_text(session.current_frame, options)
  end
end

function M.is_enabled()
  return options.enabled
end

function M.enable()
  options.enabled = true
  M.refresh()
end

function M.toggle()
  options.enabled = not options.enabled
  M.refresh()
end

function M.disable()
  options.enabled = false
  M.refresh()
end

---@param opts nvim_dap_virtual_text_options
function M.setup(opts)
  ---@type nvim_dap_virtual_text_options
  options = vim.tbl_deep_extend('force', options, opts or {})

  vim.cmd [[
  highlight default link NvimDapVirtualText Comment
  highlight default link NvimDapVirtualTextChanged DiagnosticVirtualTextWarn
  highlight default link NvimDapVirtualTextError DiagnosticVirtualTextError
  highlight default link NvimDapVirtualTextInfo DiagnosticVirtualTextInfo
  ]]

  if options.enable_commands then
    vim.cmd [[
    command! DapVirtualTextEnable :lua require'nvim-dap-virtual-text'.enable()
    command! DapVirtualTextDisable :lua require'nvim-dap-virtual-text'.disable()
    command! DapVirtualTextToggle :lua require'nvim-dap-virtual-text'.toggle()
    command! DapVirtualTextForceRefresh :lua require'nvim-dap-virtual-text'.refresh()
    ]]
  end

  local function on_continue()
    local virtual_text = require 'nvim-dap-virtual-text/virtual_text'
    virtual_text._on_continue(options)
  end

  local function on_exit()
    local virtual_text = require 'nvim-dap-virtual-text/virtual_text'
    virtual_text.clear_virtual_text()
    virtual_text.clear_last_frames()
  end

  dap.listeners.after.event_terminated[plugin_id] = on_exit
  dap.listeners.after.event_exited[plugin_id] = on_exit
  dap.listeners.before.event_continued[plugin_id] = on_continue
  dap.listeners.before.continue[plugin_id] = on_continue

  dap.listeners.before.event_stopped[plugin_id] = function(session)
    local virtual_text = require 'nvim-dap-virtual-text/virtual_text'
    virtual_text.set_last_frames(session.threads)
  end
  dap.listeners.after.event_stopped[plugin_id] = function(_, event)
    local virtual_text = require 'nvim-dap-virtual-text/virtual_text'
    if options.show_stop_reason then
      if event and event.reason == 'exception' then
        virtual_text.set_error('Stopped due to exception', options)
      elseif event and event.reason == 'data breakpoint' then
        virtual_text.set_info('Stopped due to ' .. event.reason, options)
      end
    end
  end

  dap.listeners.after.variables[plugin_id] = M.refresh

  dap.listeners.after.stackTrace[plugin_id] = function(session, body, _)
    if not options.enabled then
      return
    end

    local virtual_text = require 'nvim-dap-virtual-text/virtual_text'
    if
      session.stopped_thread_id
      and session.threads[session.stopped_thread_id]
      and session.threads[session.stopped_thread_id].frames
    then
      local frames_with_source = vim.tbl_filter(function(f)
        return f.source and f.source.path
      end, session.threads[session.stopped_thread_id].frames)
      virtual_text.set_stopped_frame(frames_with_source[1])
    end

    -- request additional stack frames for "all frames"
    if options.all_frames then
      local requested_functions = {}

      if body then
        for _, f in pairs(body.stackFrames) do
          -- Ensure to evaluate the same function only once to avoid race conditions
          -- since a function can be evaluated in multiple frames.
          if not requested_functions[f.name] then
            if not f.scopes or #f.scopes == 0 then
              pcall(session._request_scopes, session, f)
            end
            requested_functions[f.name] = true
          end
        end
      end
    end
  end

  dap.listeners.after.exceptionInfo[plugin_id] = function(_, _, response)
    local virtual_text = require 'nvim-dap-virtual-text/virtual_text'
    if not options.enabled then
      return
    end
    virtual_text.set_error(response, options)
  end
end

return M
```

## File: `lua/nvim-dap-virtual-text/virtual_text.lua`
```
--
-- virtual_text.lua
-- Copyright (C) 2020 Stephan Seitz <stephan.seitz@fau.de>
--
-- Distributed under terms of the GPLv3 license.
--

local M = {}

local api = vim.api

local ts = vim.treesitter
local tsq = ts.query

local is_in_node_range
if vim.treesitter.is_in_node_range then
  is_in_node_range = vim.treesitter.is_in_node_range
else
  local _, ts_utils = pcall(require, 'nvim-treesitter.ts_utils')
  is_in_node_range = ts_utils.is_in_node_range
end

local hl_namespace = api.nvim_create_namespace 'nvim-dap-virtual-text'
local error_set
local info_set
---@type dap.StackFrame|nil
local stopped_frame
---@type dap.StackFrame[]
local last_frames = {}

local function variables_from_scopes(scopes, lang)
  local variables = {}

  scopes = scopes or {}
  for _, s in ipairs(scopes) do
    if s.variables then
      for _, v in pairs(s.variables) do
        local key = lang == 'php' and v.name:gsub('^%$', '') or v.name
        -- prefer "locals"
        if not variables[key] or variables[key].presentationHint ~= 'locals' then
          variables[key] = { value = v, presentationHint = s.presentationHint }
        end
      end
    end
  end
  return variables
end

local function get_query(lang, query_name)
  return (tsq.get or tsq.get_query)(lang, query_name)
end

---@class Scope
---@field name string
---@field presentationHint 'arguments' | 'locals' | 'registers' | string | nil
---@field variablesReference number
---@field namedVariables number|nil
---@field indexedVariables number|nil
---@field expensive boolean
---@field source dap.Source|nil
---@field line number|nil
---@field column number|nil
---@field endLine number|nil
---@field endColumn number|nil
--- nvim-dap internal
---@field variables table<string,Variable>

---@class dap.StackFrame
--- nvim-dap internal
---@field scopes Scope[]

---@param stackframe dap.StackFrame
---@param options nvim_dap_virtual_text_options
function M.set_virtual_text(stackframe, options)
  if not stackframe then
    return
  end
  if not stackframe.scopes then
    return
  end
  if not stackframe.source then
    return
  end
  if not stackframe.source.path then
    return
  end
  local buf = vim.fn.bufnr(stackframe.source.path, false)
  if buf == -1 then
    buf = vim.uri_to_bufnr(vim.uri_from_fname(stackframe.source.path))
  end
  local parser
  local lang
  local ft = vim.bo[buf].ft
  if ft == '' then
    ft = vim.filetype.match { buf = buf } or ''
    if ft == '' then
      return
    end
  end
  if vim.treesitter.get_parser and vim.treesitter.language and vim.treesitter.language.get_lang then
    lang = vim.treesitter.language.get_lang(ft)
    if not lang then
      return
    end
    local ok
    ok, parser = pcall(vim.treesitter.get_parser, buf, lang)
    if not ok then
      return
    end
  else
    local require_ok, parsers = pcall(require, 'nvim-treesitter.parsers')
    if not require_ok then
      return
    end
    lang = parsers.get_buf_lang(buf)
    if not lang then
      return
    end
    local ok
    ok, parser = pcall(parsers.get_parser, buf, lang)
    if not ok then
      return
    end
  end

  local scope_nodes = {}
  local definition_nodes = {}

  if not parser then
    return
  end
  parser:parse()
  parser:for_each_tree(function(tree, ltree)
    local query = get_query(ltree:lang(), 'locals')
    if query then
      for _, match, _ in query:iter_matches(tree:root(), buf, 0, -1) do
        for id, nodes in pairs(match) do
          if type(nodes) ~= 'table' then
            nodes = { nodes }
          end
          for _, node in ipairs(nodes) do
            local cap_id = query.captures[id]
            if cap_id:find('scope', 1, true) then
              table.insert(scope_nodes, node)
            elseif cap_id:find('definition', 1, true) then
              table.insert(definition_nodes, node)
            elseif options.all_references and cap_id:find('reference', 1, true) then
              table.insert(definition_nodes, node)
            end
          end
        end
      end
    end
  end)

  local variables = variables_from_scopes(stackframe.scopes)

  local scopes = stackframe.scopes or {}
  for _, s in ipairs(scopes) do
    if s.variables then
      for _, v in pairs(s.variables) do
        local key = lang == 'php' and v.name:gsub('^%$', '') or v.name
        -- prefer "locals"
        if not variables[key] or variables[key].presentationHint ~= 'locals' then
          variables[key] = { value = v, presentationHint = s.presentationHint }
        end
      end
    end
  end

  local inline = options.virt_text_pos == 'inline'
  local last_scopes = last_frames[stackframe.id] and last_frames[stackframe.id].scopes or {}
  local last_variables = variables_from_scopes(last_scopes)

  local virt_lines = {}

  local node_ids = {}
  for _, node in pairs(definition_nodes) do
    if node then
      local get_node_text = vim.treesitter.get_node_text or vim.treesitter.query.get_node_text
      local name = get_node_text(node, buf)
      local var_line, var_col = node:start()

      local evaluated = variables[name]
      evaluated = evaluated and evaluated.value
      local last_value = last_variables[name]
      last_value = last_value and last_value.value
      if
        evaluated
        ---@diagnostic disable-next-line: deprecated
        and not (options.filter_references_pattern and evaluated.value:find(options.filter_references_pattern))
      then -- evaluated local with same name exists
        -- is this name really the local or is it in another scope?
        local in_scope = true
        for _, scope in ipairs(scope_nodes) do
          if is_in_node_range(scope, var_line, var_col) and not is_in_node_range(scope, stackframe.line - 1, 0) then
            in_scope = false
            break
          end
        end

        if in_scope then
          if options.only_first_definition and not options.all_references then
            variables[name] = nil
          end
          if not node_ids[node:id()] then
            node_ids[node:id()] = true
            local has_changed = options.highlight_changed_variables
              and (evaluated.value ~= (last_value and last_value.value))
              and (options.highlight_new_as_changed or last_value)
            local text = options.display_callback(evaluated, buf, stackframe, node, options)
            if text then
              if options.commented then
                text = vim.o.commentstring:gsub('%%s', { ['%s'] = text })
              end
              text = options.text_prefix .. text

              if virt_lines[node:start()] then
                if options.virt_lines then
                  text = ' ' .. options.separator .. text
                end
              else
                virt_lines[node:start()] = {}
              end
              table.insert(virt_lines[node:start()], {
                text,
                has_changed and 'NvimDapVirtualTextChanged' or 'NvimDapVirtualText',
                node = node,
              })
            end
          end
        end
      end
    end
  end

  for line, content in pairs(virt_lines) do
    -- Filtering necessary with all_references: there can be more than on reference on one line
    if options.all_references then
      local avoid_duplicates = {}
      content = vim.tbl_filter(function(c)
        local text = c[1]
        local was_duplicate = avoid_duplicates[text]
        avoid_duplicates[text] = true
        return not was_duplicate
      end, content)
    end
    if options.virt_lines then
      for _, virt_text in ipairs(content) do
        virt_text.node = nil
      end
      vim.api.nvim_buf_set_extmark(
        buf,
        hl_namespace,
        line,
        0,
        { virt_lines = { content }, virt_lines_above = options.virt_lines_above }
      )
    else
      local line_text = api.nvim_buf_get_lines(buf, line, line + 1, true)[1]
      local win_col = math.max(options.virt_text_win_col or 0, #line_text + 1)
      for i, virt_text in ipairs(content) do
        local node_range = { virt_text.node:range() }
        if i < #content and not inline then
          virt_text[1] = virt_text[1] .. options.separator
        end
        virt_text.node = nil
        vim.api.nvim_buf_set_extmark(buf, hl_namespace, node_range[inline and 3 or 1], node_range[inline and 4 or 2], {
          end_line = node_range[3],
          end_col = node_range[4],
          hl_mode = 'combine',
          virt_text = { virt_text },
          virt_text_pos = options.virt_text_pos,
          virt_text_win_col = options.virt_text_win_col and win_col,
        })
        win_col = win_col + #virt_text[1] + 1
      end
    end
  end

  if stopped_frame and stopped_frame.line and stopped_frame.source and stopped_frame.source.path then
    local buf = vim.uri_to_bufnr(vim.uri_from_fname(stopped_frame.source.path))
    if error_set then
      local error_msg = error_set
      if options.commented then
        error_msg = vim.o.commentstring:gsub('%%s', { ['%s'] = error_set })
      end
      pcall(api.nvim_buf_set_extmark, buf, hl_namespace, stopped_frame.line - 1, 0, {
        hl_mode = 'combine',
        virt_text = { { error_msg, 'NvimDapVirtualTextError' } },
        virt_text_pos = inline and 'eos' or options.virt_text_pos,
      })
    end
    if info_set then
      local info_msg = info_set
      if options.commented then
        info_msg = vim.o.commentstring:gsub('%%s', { ['%s'] = info_set })
      end
      pcall(api.nvim_buf_set_extmark, buf, hl_namespace, stopped_frame.line - 1, 0, {
        hl_mode = 'combine',
        virt_text = { { info_msg, 'NvimDapVirtualTextInfo' } },
        virt_text_pos = inline and 'eos' or options.virt_text_pos,
      })
    end
  end
end

---@param options nvim_dap_virtual_text_options
function M.set_info(message, options)
  info_set = options.info_prefix .. message
end

---@param frame dap.StackFrame
function M.set_stopped_frame(frame)
  stopped_frame = frame
end

---@param options nvim_dap_virtual_text_options
function M.set_error(response, options)
  if response then
    local exception_type = response.details and response.details.typeName
    local message = options.error_prefix
      .. (exception_type or '')
      .. (response.description and ((exception_type and ': ' or '') .. response.description) or '')
    error_set = message
  end
end

function M._on_continue(options)
  error_set = nil
  info_set = nil
  stopped_frame = nil

  if type(options) == 'table' and options.clear_on_continue then
    M.clear_virtual_text()
  end
end

---@param stackframe dap.StackFrame|nil
function M.clear_virtual_text(stackframe)
  if stackframe then
    local buf = vim.uri_to_bufnr(vim.uri_from_fname(stackframe.source.path))
    api.nvim_buf_clear_namespace(buf, hl_namespace, 0, -1)
  else
    for _, buf in ipairs(api.nvim_list_bufs()) do
      api.nvim_buf_clear_namespace(buf, hl_namespace, 0, -1)
    end
  end
end

---@param threads dap.Thread[]
function M.set_last_frames(threads)
  for _, t in pairs(threads or {}) do
    for _, f in pairs(t.frames or {}) do
      if f and f.id then
        last_frames[f.id] = f
      end
    end
  end
end

function M.clear_last_frames()
  last_frames = {}
end

return M
```

## File: `scripts/style-check.sh`
```bash
#!/usr/bin/env bash

luacheck `find -name  "*.lua"` --codes
```

## File: `test_cases/issue_36_value_not_updated.py`
```python
# See Issue #36: Value not updated after changing the value of a parameter

from operator import itemgetter


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) < 2:
            return nums

        arr = list(sorted(enumerate(nums), key=itemgetter(1)))
        i = 0
        j = len(nums) - 1

        while i < j:
            arri = arr[i]
            arrj = arr[j]
            sum_ = arri[1] + arrj[1]
            if sum_ == target:
                return [arri[0], arrj[0]]
            elif sum_ > target:
                j -= 1
            else:
                i += 1
        return []

arr = [2, 7, 11, 15]
target = 9

Solution().twoSum(arr, target) == [0, 1]
```

