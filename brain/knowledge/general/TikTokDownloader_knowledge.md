---
id: tiktokdownloader-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.219198
---

# KNOWLEDGE EXTRACT: TikTokDownloader
> **Extracted on:** 2026-03-31 01:40:58
> **Source:** TikTokDownloader

---

## File: `.gitignore`
```
__pycache__/
*.pyc
/.venv/
/.ruff_cache/
/.idea/
/.run/
/Volume/
!/.github/
```

## File: `.python-version`
```
3.12
```

## File: `Dockerfile`
```
# ---- 阶段 1: 构建器 (Builder) ----
# 使用一个功能完整的镜像，它包含编译工具或可以轻松安装它们
FROM python:3.12-bullseye as builder

# 安装编译 uvloop 和 httptools 所需的系统依赖 (C编译器等)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 复制需求文件
COPY requirements.txt .

# 在这个具备编译环境的阶段安装所有 Python 依赖
# 安装到一个独立的目录 /install 中，以便后续复制
RUN pip install --no-cache-dir --prefix="/install" -r requirements.txt

# ---- 阶段 2: 最终镜像 (Final Image) ----
# 使用轻量级 slim 镜像作为最终的运行环境
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 添加元数据标签
LABEL name="DouK-Downloader" authors="JoeanAmier" repository="https://github.com/JoeanAmier/TikTokDownloader"

# 从构建器阶段，将已经安装好的依赖包复制到最终镜像的系统路径中
COPY --from=builder /install /usr/local

# 复制你的应用程序代码和相关文件
COPY src /app/src
COPY locale /app/locale
COPY static /app/static
COPY license /app/license
COPY main.py /app/main.py

# 暴露端口
EXPOSE 5555

# 创建挂载点
VOLUME /app/Volume

# 设置容器启动命令
CMD ["python", "main.py"]
```

## File: `license`
```
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
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
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.
```

## File: `main.py`
```python
from asyncio import CancelledError
from asyncio import run

from src.application import TikTokDownloader


async def main():
    async with TikTokDownloader() as downloader:
        try:
            await downloader.run()
        except (
                KeyboardInterrupt,
                CancelledError,
        ):
            return


if __name__ == "__main__":
    run(main())
```

## File: `pyproject.toml`
```
[project]
name = "DouK-Downloader"
version = "5.8"
description = "TikTok 发布/喜欢/合辑/直播/视频/图集/音乐；抖音发布/喜欢/收藏/收藏夹/视频/图集/实况/直播/音乐/合集/评论/账号/搜索/热榜数据采集工具"
authors = [
    { name = "JoeanAmier", email = "yonglelolu@foxmail.com" },
]
readme = "README.md"
license = "GPL-3.0"
requires-python = ">=3.12,<3.13"
dependencies = [
    "aiofiles>=25.1.0",
    "aiosqlite>=0.21.0",
    "emoji>=2.15.0",
    "fastapi>=0.124.2",
    "gmssl>=3.2.2",
    "httpx[socks]>=0.28.1",
    "lxml>=6.0.2",
    "openpyxl>=3.1.5",
    "pydantic>=2.12.5",
    "pyperclip>=1.11.0",
    "rich>=14.2.0",
    "rookiepy>=0.5.6",
    "uvicorn>=0.38.0",
]

[project.urls]
Repository = "https://github.com/JoeanAmier/TikTokDownloader"

[tool.uv.pip]
index-url = "https://pypi.org/simple"

[tool.ruff]
# Exclude a variety of commonly ignored directories.
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pyenv",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".vscode",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
]

# Same as Black.
line-length = 88
indent-width = 4

# Assume Python 3.12
target-version = "py312"

[tool.ruff.lint]
# Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`)  codes by default.
# Unlike Flake8, Ruff doesn't enable pycodestyle warnings (`W`) or
# McCabe complexity (`C901`) by default.
select = ["E4", "E7", "E9", "F"]
ignore = []

# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[tool.ruff.format]
# Like Black, use double quotes for strings.
quote-style = "double"

# Like Black, indent with spaces, rather than tabs.
indent-style = "space"

# Like Black, respect magic trailing commas.
skip-magic-trailing-comma = false

# Like Black, automatically detect the appropriate line ending.
line-ending = "auto"

# Enable auto-formatting of code examples in docstrings. Markdown,
# reStructuredText code/literal blocks and doctests are all supported.
#
# This is currently disabled by default, but it is planned for this
# to be opt-out in the future.
docstring-code-format = false

# Set the line length limit used when formatting code snippets in
# docstrings.
#
# This only has an effect when the `docstring-code-format` setting is
# enabled.
docstring-code-line-length = "dynamic"

[dependency-groups]
dev = [
    "pytest>=8.3.5",
]
```

## File: `README.md`
```markdown
<div align="center">
<img src="./static/images/DouK-Downloader.png" alt="DouK-Downloader" height="256" width="256"><br>
<h1>DouK-Downloader</h1>
<p>简体中文 | <a href="README_EN.md">English</a></p>
<a href="https://trendshift.io/repositories/6222" target="_blank"><img src="https://trendshift.io/api/badge/repositories/6222" alt="" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<br>
<img alt="GitHub" src="https://img.shields.io/github/license/JoeanAmier/TikTokDownloader?style=flat-square">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/JoeanAmier/TikTokDownloader?style=flat-square&color=55efc4">
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/JoeanAmier/TikTokDownloader?style=flat-square&color=fda7df">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/JoeanAmier/TikTokDownloader?style=flat-square&color=a29bfe">
<br>
<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.12-b8e994?style=flat-square&logo=python&labelColor=3dc1d3">
<img alt="GitHub release (with filter)" src="https://img.shields.io/github/v/release/JoeanAmier/TikTokDownloader?style=flat-square&color=48dbfb">
<img src="https://img.shields.io/badge/Sourcery-enabled-884898?style=flat-square&color=1890ff" alt="">
<img alt="Static Badge" src="https://img.shields.io/badge/Docker-badc58?style=flat-square&logo=docker">
<img alt="GitHub all releases" src="https://img.shields.io/github/downloads/JoeanAmier/TikTokDownloader/total?style=flat-square&color=ffdd59">
</div>
<br>
<p>🔥 <b>TikTok 发布/喜欢/合辑/直播/视频/图集/音乐；抖音发布/喜欢/收藏/收藏夹/视频/图集/实况/直播/音乐/合集/评论/账号/搜索/热榜数据采集工具：</b>完全开源，基于 HTTPX 模块实现的免费数据采集和文件下载工具；批量下载抖音账号发布、喜欢、收藏、收藏夹作品；批量下载 TikTok 账号发布、喜欢作品；下载抖音链接或 TikTok 链接作品；获取抖音直播拉流地址；下载抖音直播视频；获取 TikTok 直播拉流地址；下载 TikTok 直播视频；采集抖音作品评论数据；批量下载抖音合集作品；批量下载 TikTok 合辑作品；采集抖音账号详细数据；采集抖音用户 / 作品 / 直播搜索结果；采集抖音热榜数据。</p>
<p>⭐ 本项目历史名称：<code>TikTokDownloader</code></p>
<p>📣 本项目将于未来进行代码结构重构，目标是让代码更加稳健，并具备更好的可维护性与扩展性；如果你对项目设计、实现方式或优化思路有想法，欢迎提出建议或参与讨论！</p>
<hr>

# 📝 项目功能

<details>
<summary>功能列表（点击展开）</summary>
<ul>
<li>✅ 下载抖音视频/图集</li>
<li>✅ 下载抖音实况/动图</li>
<li>✅ 下载最高画质视频文件</li>
<li>✅ 下载 TikTok 视频原画</li>
<li>✅ 下载 TikTok 视频/图集</li>
<li>✅ 下载抖音账号发布/喜欢/收藏/收藏夹作品</li>
<li>✅ 下载 TikTok 账号发布/喜欢作品</li>
<li>✅ 采集抖音 / TikTok 详细数据</li>
<li>✅ 批量下载链接作品</li>
<li>✅ 多账号批量下载作品</li>
<li>✅ 自动跳过已下载的文件</li>
<li>✅ 持久化保存采集数据</li>
<li>✅ 支持 CSV/XLSX/SQLite 格式保存数据</li>
<li>✅ 下载动态/静态封面图</li>
<li>✅ 获取抖音直播拉流地址</li>
<li>✅ 获取 TikTok 直播拉流地址</li>
<li>✅ 调用 ffmpeg 下载直播</li>
<li>✅ Web UI 交互界面</li>
<li>✅ 采集抖音作品评论数据</li>
<li>✅ 下载抖音合集作品</li>
<li>✅ 下载 TikTok 合辑作品</li>
<li>✅ 记录点赞收藏等统计数据</li>
<li>✅ 筛选作品发布时间</li>
<li>✅ 支持账号作品增量下载</li>
<li>✅ 支持使用代理采集数据</li>
<li>✅ 支持局域网远程访问</li>
<li>✅ 采集抖音账号详细数据</li>
<li>✅ 作品统计数据更新</li>
<li>✅ 支持自定义账号/合集标识</li>
<li>✅ 自动更新账号昵称/标识</li>
<li>✅ 部署至私有服务器</li>
<li>✅ 部署至公开服务器</li>
<li>✅ 采集抖音搜索数据</li>
<li>✅ 采集抖音热榜数据</li>
<li>✅ 记录已下载作品 ID</li>
<li>☑️ <del>扫码登陆获取 Cookie</del></li>
<li>✅ 从浏览器读取 Cookie</li>
<li>✅ 支持 Web API 调用</li>
<li>✅ 支持多线程下载作品</li>
<li>✅ 文件完整性处理机制</li>
<li>✅ 自定义规则筛选作品</li>
<li>✅ 按文件夹归档保存作品文件</li>
<li>✅ 自定义设置文件大小上限</li>
<li>✅ 支持文件断点续传下载</li>
<li>✅ 监听剪贴板链接下载作品</li>
</ul>
</details>

# 💻 程序截图

<p><a href="https://www.bilibili.com/video/BV1d7eAzTEFs/">前往 bilibili 观看演示</a>；<a href="https://youtu.be/yMU-RWl55hg">前往 YouTube 观看演示</a></p>

## 终端交互模式

<p>建议通过配置文件管理账号，更多介绍请查阅 <a href="https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation">文档</a></p>

![终端模式截图](docs/screenshot/终端交互模式截图CN1.png)
*****
![终端模式截图](docs/screenshot/终端交互模式截图CN2.png)
*****
![终端模式截图](docs/screenshot/终端交互模式截图CN3.png)

## Web UI 交互模式

> **项目代码已重构，该模式代码尚未更新，未来开发完成重新开放！**

## Web API 接口模式

![WebAPI模式截图](docs/screenshot/WebAPI模式截图CN1.png)
*****
![WebAPI模式截图](docs/screenshot/WebAPI模式截图CN2.png)

> **启动该模式后，访问 `http://127.0.0.1:5555/docs` 或者 `http://127.0.0.1:5555/redoc` 可以查阅自动生成的文档！**

### API 调用示例代码

```python
from httpx import post
from rich import print


def demo():
    headers = {"token": ""}
    data = {
        "detail_id": "0123456789",
        "pages": 2,
    }
    api = "http://127.0.0.1:5555/douyin/comment"
    response = post(api, json=data, headers=headers)
    print(response.json())


demo()
```

# 📋 项目说明

## 快速入门

<p>⭐ Mac OS、Windows 10 及以上用户可前往 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 或者 <a href="https://github.com/JoeanAmier/TikTokDownloader/actions">Actions</a> 下载已编译的程序，开箱即用！</p>
<p>⭐ 本项目包含自动构建可执行文件的 GitHub Actions，使用者可以随时使用 GitHub Actions 将最新源码构建为可执行文件！</p>
<p>⭐ 自动构建可执行文件教程请查阅本文档的 <code>构建可执行文件指南</code> 部分；如果需要更加详细的图文教程，请 <a href="https://mp.weixin.qq.com/s/TorfoZKkf4-x8IBNLImNuw">查阅文章</a>！</p>
<p><strong>注意：由于 Mac OS 平台的可执行文件 <code>main</code> 未经过代码签名，首次运行时会受到系统安全限制。请先在终端执行 <code>xattr -cr 项目文件夹路径</code> 命令移除安全标记，执行一次后即可正常运行。</strong></p>
<hr>
<ol>
<li><b>运行可执行文件</b> 或者 <b>配置环境运行</b>（二选一）
<ol><b>运行可执行文件</b>
<li>下载 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 或者 Actions 构建的可执行文件压缩包</li>
<li>解压后打开程序文件夹，双击运行 <code>main</code></li>
</ol>
<ol><b>配置环境运行</b>

[//]: # (<li>安装不低于 <code>3.12</code> 版本的 <a href="https://www.python.org/">Python</a> 解释器</li>)
<li>安装 <code>3.12</code> 版本的 <a href="https://www.python.org/">Python</a> 解释器</li>
<li>下载最新的源码或 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 发布的源码至本地</li>
<ol><b>使用 pip 安装项目依赖</b>
<li>运行 <code>python -m venv venv</code> 命令创建虚拟环境（可选）</li>
<li>运行 <code>.\venv\Scripts\activate.ps1</code> 或者 <code>venv\Scripts\activate</code> 命令激活虚拟环境（可选）</li>
<li>运行 <code>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt</code> 命令安装程序所需模块</li>
<li>运行 <code>python .\main.py</code> 或者 <code>python main.py</code> 命令启动 DouK-Downloader</li>
</ol>
<ol><b>使用 uv 安装项目依赖（推荐）</b>
<li>运行 <code>uv sync --no-dev</code> 命令同步环境依赖</li>
<li>运行 <code>uv run main.py</code> 命令启动 DouK-Downloader</li>
</ol>
</ol>
</li>
<li>阅读 DouK-Downloader 的免责声明，根据提示输入内容</li>
<li>将 Cookie 信息写入配置文件
<ol><b>从剪贴板读取 Cookie（推荐）</b>
<li>参考 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 提取教程</a>，复制所需 Cookie 至剪贴板</li>
<li>选择 <code>从剪贴板读取 Cookie</code> 选项，程序会自动读取剪贴板的 Cookie 并写入配置文件</li>
</ol>
<ol><b>从浏览器读取 Cookie</b>
<li>选择 <code>从浏览器读取 Cookie</code> 选项，按照提示输入浏览器类型或序号</li>
</ol>
<ol><b><del>扫码登录获取 Cookie</del>（失效）</b>
<li><del>选择 <code>扫码登录获取 Cookie</code> 选项，程序会显示登录二维码图片，并使用默认应用打开图片</del></li>
<li><del>使用抖音 APP 扫描二维码并登录账号</del></li>
<li><del>按照提示操作，程序会自动将 Cookie 写入配置文件</del></li>
</ol>
</li>
<li>返回程序界面，依次选择 <code>终端交互模式</code> -> <code>批量下载链接作品(通用)</code> -> <code>手动输入待采集的作品链接</code></li>
<li>输入抖音作品链接即可下载作品文件（TikTok 平台需要更多初始设置，详见文档）</li>
<li>更多详细说明请查看 <b><a href="https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation">项目文档</a></b></li>
</ol>
<p>⭐ 推荐使用 <a href="https://learn.microsoft.com/zh-cn/windows/terminal/install">Windows 终端</a>（Windows 11 自带默认终端）</p>

### Docker 容器

<ol>
<li>获取镜像</li>
<ul>
<li>方式一：使用 <code>Dockerfile</code> 文件构建镜像</li>
<li>方式二：使用 <code>docker pull joeanamier/tiktok-downloader</code> 命令拉取镜像</li>
<li>方式三：使用 <code>docker pull ghcr.io/joeanamier/tiktok-downloader</code> 命令拉取镜像</li>
</ul>
<li>创建容器：<code>docker run --name 容器名称(可选) -p 主机端口号:5555 -v tiktok_downloader_volume:/app/Volume -it &lt;镜像名称&gt;</code>
</li>
<br><b>注意：</b>此处的 <code>&lt;镜像名称&gt;</code> 需与您在第一步中使用的镜像名称保持一致（例如 <code>joeanamier/tiktok-downloader</code> 或 <code>ghcr.io/joeanamier/tiktok-downloader</code>）
<li>运行容器
<ul>
<li>启动容器：<code>docker start -i 容器名称/容器 ID</code></li>
<li>重启容器：<code>docker restart -i 容器名称/容器 ID</code></li>
</ul>
</li>
</ol>
<p>Docker 容器无法直接访问宿主机的文件系统，部分功能不可用，例如：<code>从浏览器读取 Cookie</code>；其他功能如有异常请反馈！</p>
<hr>

## 关于 Cookie

[点击查看 Cookie 获取教程](https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md)

> * Cookie 仅需在失效后重新写入配置文件，并非每次运行程序都要写入配置文件！
>
> * Cookie 会影响下载的视频文件分辨率，如果无法下载最高分辨率的视频文件，请尝试更新 Cookie！
>
> * 程序获取数据失败时，可以尝试更新 Cookie 或者使用已登录的 Cookie！

<hr>

## 其他说明

<ul>
<li>程序提示用户输入时，直接回车代表返回上级菜单，输入 <code>Q</code> 或 <code>q</code> 代表结束运行</li>
<li>由于获取账号喜欢作品和收藏作品数据仅返回喜欢 / 收藏作品的发布日期，不返回操作日期，因此程序需要获取全部喜欢 / 收藏作品数据再进行日期筛选；如果作品数量较多，可能会花费较长的时间；可通过 <code>max_pages</code> 参数控制请求次数</li>
<li>获取私密账号的发布作品数据需要登录后的 Cookie，且登录的账号需要关注该私密账号</li>
<li>批量下载账号作品或合集作品时，如果对应的昵称或标识发生变化，程序会自动更新已下载作品文件名称中的昵称和标识</li>
<li>程序下载文件时会先将文件下载至临时文件夹，下载完成后再移动至储存文件夹；程序运行结束时会清空临时文件夹</li>
<li><code>批量下载收藏作品模式</code> 目前仅支持下载当前已登录 Cookie 对应账号的收藏作品，暂不支持多账号</li>
<li>如果想要程序使用代理请求数据，必须在 <code>settings.json</code> 设置 <code>proxy</code> 参数，否则程序不会使用代理</li>
<li>如果您的计算机没有合适的程序编辑 JSON 文件，建议使用 <a href="https://www.toolhelper.cn/JSON/JSONFormat">在线工具</a> 编辑配置文件内容，修改后需要重启软件才能生效。</li>
<li>当程序请求用户输入内容或链接时，请注意避免输入的内容或链接包含换行符，这可能会导致预期之外的问题</li>
<li>本项目不会支持付费作品下载，请勿反馈任何关于付费作品下载的问题</li>
<li>Windows 系统需要以管理员身份运行程序才能读取 Chromium、Chrome、Edge 浏览器 Cookie</li>
<li>本项目并未针对程序多开的情况进行优化，如需程序多开，请复制整个项目的文件夹，避免出现预期之外的问题</li>
<li>程序运行过程中，如需终止程序或 <code>ffmpeg</code>，请按下 <code>Ctrl + C</code> 终止运行，不要直接点击终端窗口的关闭按钮</li>
</ul>
<h2>构建可执行文件指南</h2>
<details>
<summary><b>构建可执行文件指南（点击展开）</b></summary>

本指南将引导您通过 Fork 本仓库并执行 GitHub Actions 自动完成基于最新源码的程序构建和打包！

---

### 使用步骤

#### 1. Fork 本仓库

1. 点击项目仓库右上角的 **Fork** 按钮，将本仓库 Fork 到您的个人 GitHub 账户中
2. 您的 Fork 仓库地址将类似于：`https://github.com/your-username/this-repo`

---

#### 2. 启用 GitHub Actions

1. 前往您 Fork 的仓库页面
2. 点击顶部的 **Settings** 选项卡
3. 点击右侧的 **Actions** 选项卡
4. 点击 **General** 选项
5. 在 **Actions permissions** 下，选择 **Allow all actions and reusable workflows** 选项，点击 **Save** 按钮

---

#### 3. 手动触发打包流程

1. 在您 Fork 的仓库中，点击顶部的 **Actions** 选项卡
2. 找到名为 **构建可执行文件** 的工作流
3. 点击右侧的 **Run workflow** 按钮：
    - 选择 **master** 或者 **develop** 分支
    - 点击 **Run workflow**

---

#### 4. 查看打包进度

1. 在 **Actions** 页面中，您可以看到触发的工作流运行记录
2. 点击运行记录，查看详细的日志以了解打包进度和状态

---

#### 5. 下载打包结果

1. 打包完成后，进入对应的运行记录页面
2. 在页面底部的 **Artifacts** 部分，您将看到打包的结果文件
3. 点击下载并保存到本地，即可获得打包好的程序

---

### 注意事项

1. **资源使用**：
    - Actions 的运行环境由 GitHub 免费提供，普通用户每月有一定的免费使用额度（2000 分钟）

2. **代码修改**：
    - 您可以自由修改 Fork 仓库中的代码以定制程序打包流程
    - 修改后重新触发打包流程，您将得到自定义的构建版本

3. **与主仓库保持同步**：
    - 如果主仓库更新了代码或工作流，建议您定期同步 Fork 仓库以获取最新功能和修复

---

### Actions 常见问题

#### Q1: 为什么我无法触发工作流？

A: 请确认您已按照步骤 **启用 Actions**，否则 GitHub 会禁止运行工作流

#### Q2: 打包流程失败怎么办？

A:

- 检查运行日志，了解失败原因
- 确保代码没有语法错误或依赖问题
- 如果问题仍未解决，可以在本仓库的 [Issues 页面](https://github.com/JoeanAmier/TikTokDownloader/issues) 提出问题

#### Q3: 我可以直接使用主仓库的 Actions 吗？

A: 由于权限限制，您无法直接触发主仓库的 Actions。请通过 Fork 仓库的方式执行打包流程

</details>

## 程序更新

<p><strong>方案一：</strong>下载并解压文件，将旧版本的 <code>_internal\Volume</code> 文件夹复制到新版本的 <code>_internal</code> 文件夹。</p>
<p><strong>方案二：</strong>下载并解压文件（不要运行程序），复制全部文件，直接覆盖旧版本文件。</p>

# ⚠️ 免责声明

<ol>
<li>使用者对本项目的使用由使用者自行决定，并自行承担风险。作者对使用者使用本项目所产生的任何损失、责任、或风险概不负责。</li>
<li>本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。作者按现有技术水平努力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。</li>
<li>本项目依赖的所有第三方库、插件或服务各自遵循其原始开源或商业许可，使用者需自行查阅并遵守相应协议，作者不对第三方组件的稳定性、安全性及合规性承担任何责任。</li>
<li>使用者在使用本项目时必须严格遵守 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/LICENSE">GNU
    General Public License v3.0</a> 的要求，并在适当的地方注明使用了 <a
        href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/LICENSE">GNU General Public License
    v3.0</a> 的代码。
</li>
<li>使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。</li>
<li>使用者不得使用本工具从事任何侵犯知识产权的行为，包括但不限于未经授权下载、传播受版权保护的内容，开发者不参与、不支持、不认可任何非法内容的获取或分发。</li>
<li>本项目不对使用者涉及的数据收集、存储、传输等处理活动的合规性承担责任。使用者应自行遵守相关法律法规，确保处理行为合法正当；因违规操作导致的法律责任由使用者自行承担。</li>
<li>使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。</li>
<li>本项目的作者不会提供 DouK-Downloader 项目的付费版本，也不会提供与 DouK-Downloader 项目相关的任何商业服务。</li>
<li>基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的各种情况负全部责任。</li>
<li>本项目不授予使用者任何专利许可；若使用本项目导致专利纠纷或侵权，使用者自行承担全部风险和责任。未经作者或权利人书面授权，不得使用本项目进行任何商业宣传、推广或再授权。</li>
<li>作者保留随时终止向任何违反本声明的使用者提供服务的权利，并可能要求其销毁已获取的代码及衍生作品。</li>
<li>作者保留在不另行通知的情况下更新本声明的权利，使用者持续使用即视为接受修订后的条款。</li>
</ol>
<b>在使用本项目的代码和功能之前，请您认真考虑并接受以上免责声明。如果您对上述声明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险和后果。</b>
<h1>🌟 贡献指南</h1>
<p><strong>欢迎对本项目做出贡献！为了保持代码库的整洁、高效和易于维护，请仔细阅读以下指南，以确保您的贡献能够顺利被接受和整合。</strong></p>
<ul>
<li>在开始开发前，请从 <code>develop</code> 分支拉取最新的代码，以此为基础进行修改；这有助于避免合并冲突并保证您的改动基于最新的项目状态。</li>
<li>如果您的更改涉及多个不相关的功能或问题，请将它们分成多个独立的提交或拉取请求。</li>
<li>每个拉取请求应尽可能专注于单一功能或修复，以便于代码审查和测试。</li>
<li>遵循现有的代码风格；请确保您的代码与项目中已有的代码风格保持一致；建议使用 Ruff 工具保持代码格式规范。</li>
<li>编写可读性强的代码；添加适当的注释帮助他人理解您的意图。</li>
<li>每个提交都应该包含一个清晰、简洁的提交信息，以描述所做的更改。提交信息应遵循以下格式：<code>&lt;类型&gt;: &lt;简短描述&gt;</code></li>
<li>当您准备提交拉取请求时，请优先将它们提交到 <code>develop</code> 分支；这是为了给维护者一个缓冲区，在最终合并到 <code>master</code>
分支之前进行额外的测试和审查。</li>
<li>建议在开发前或遇到疑问时与作者沟通，确保开发方向一致，避免重复劳动或无效提交。</li>
</ul>
<p><strong>参考资料：</strong></p>
<ul>
<li><a href="https://www.contributor-covenant.org/zh-cn/version/2/1/code_of_conduct/">贡献者公约</a></li>
<li><a href="https://opensource.guide/zh-hans/how-to-contribute/">如何为开源做贡献</a></li>
</ul>

# ♥️ 支持项目

<p>如果 <b>DouK-Downloader</b> 对您有帮助，请考虑为它点个 <b>Star</b> ⭐，感谢您的支持！</p>
<table>
<thead>
<tr>
<th align="center">微信(WeChat)</th>
<th align="center">支付宝(Alipay)</th>
</tr>
</thead>
<tbody><tr>
<td align="center"><img src="./docs/微信赞助二维码.png" alt="微信赞助二维码" height="200" width="200"></td>
<td align="center"><img src="./docs/支付宝赞助二维码.png" alt="支付宝赞助二维码" height="200" width="200"></td>
</tr>
</tbody>
</table>
<p>如果您愿意，可以考虑提供资助为 <b>DouK-Downloader</b> 提供额外的支持！</p>

# 💰 项目赞助

## DartNode

[![Powered by DartNode](docs/AD/DartNode_AD.png)](https://dartnode.com "Powered by DartNode - Free VPS for Open Source")

***

## ZMTO

<p><a href="https://www.zmto.com/"><img src="https://console.zmto.com/templates/2019/dist/images/logo_dark.svg" alt="ZMTO"></a></p>
<p><a href="https://www.zmto.com/">ZMTO</a>：一家专业的云基础设施提供商，以可靠的尖端技术与专业支持，提供高效的解决方案，并为符合条件的开源项目提供企业级VPS基础设施，支持开源生态系统的可持续发展与创新。</p>

***

## TikHub

<p><a href="https://tikhub.io/?utm_source=github&utm_medium=readme&utm_campaign=tiktok_downloader&ref=github_joeanamier_tiktokdownloader"><img src="docs/AD/TIKHUB_AD.jpg" alt="TIKHUB" width="458" height="319"></a></p>
<p><a href="https://tikhub.io/?utm_source=github&utm_medium=readme&utm_campaign=tiktok_downloader&ref=github_joeanamier_tiktokdownloader">TikHub API</a> 提供超过 700 个端点，可用于从 14+ 个社交媒体平台获取与分析数据 —— 包括视频、用户、评论、商店、商品与趋势等，一站式完成所有数据访问与分析。</p>
<p>使用 <strong>邀请码</strong>：<code>ZrdH8McC</code> 注册并充值即可获得 <code>$2</code> 额度。</p>

# ✉️ 联系作者

<ul>
<li>作者邮箱：yonglelolu@foxmail.com</li>
<li>作者微信: Downloader_Tools</li>
<li>微信公众号: Downloader Tools</li>
<li><b>Discord 社区</b>: <a href="https://discord.com/invite/ZYtmgKud9Y">点击加入社区</a></li>
<li>QQ 群聊(用于项目交流与摸鱼闲聊): <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/QQ%E7%BE%A4%E8%81%8A%E4%BA%8C%E7%BB%B4%E7%A0%81.png">扫码加入群聊</a></li>
</ul>
<p>✨ <b>作者的其他开源项目：</b></p>
<ul>
<li><b>XHS-Downloader（小红书、XiaoHongShu、RedNote）</b>：<a href="https://github.com/JoeanAmier/XHS-Downloader">https://github.com/JoeanAmier/XHS-Downloader</a></li>
<li><b>KS-Downloader（快手、KuaiShou）</b>：<a href="https://github.com/JoeanAmier/KS-Downloader">https://github.com/JoeanAmier/KS-Downloader</a></li>
</ul>
<h1>⭐ Star 趋势</h1>
<p>
<img alt="Star History Chart" src="https://api.star-history.com/svg?repos=JoeanAmier/TikTokDownloader&amp;type=Timeline"/>
</p>

# 💡 项目参考

* https://github.com/Johnserf-Seed/f2
* https://github.com/Evil0ctal/Douyin_TikTok_Download_API
* https://github.com/justbeluga/tiktok-web-reverse-engineering
* https://github.com/ihmily/DouyinLiveRecorder
* https://github.com/encode/httpx/
* https://github.com/Textualize/rich
* https://github.com/omnilib/aiosqlite
* https://github.com/Tinche/aiofiles
* https://github.com/pyinstaller/pyinstaller
* https://foss.heptapod.net/openpyxl/openpyxl
* https://github.com/carpedm20/emoji/
* https://github.com/lxml/lxml
* https://ffmpeg.org/ffmpeg-all.html
```

## File: `README_EN.md`
```markdown
<div align="center">
<img src="./static/images/DouK-Downloader.png" alt="DouK-Downloader" height="256" width="256"><br>
<h1>DouK-Downloader</h1>
<p><a href="README.md">简体中文</a> | English</p>
<a href="https://trendshift.io/repositories/6222" target="_blank"><img src="https://trendshift.io/api/badge/repositories/6222" alt="" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<br>
<img alt="GitHub" src="https://img.shields.io/github/license/JoeanAmier/TikTokDownloader?style=flat-square">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/JoeanAmier/TikTokDownloader?style=flat-square&color=55efc4">
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/JoeanAmier/TikTokDownloader?style=flat-square&color=fda7df">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/JoeanAmier/TikTokDownloader?style=flat-square&color=a29bfe">
<br>
<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.12-b8e994?style=flat-square&logo=python&labelColor=3dc1d3">
<img alt="GitHub release (with filter)" src="https://img.shields.io/github/v/release/JoeanAmier/TikTokDownloader?style=flat-square&color=48dbfb">
<img src="https://img.shields.io/badge/Sourcery-enabled-884898?style=flat-square&color=1890ff" alt="">
<img alt="Static Badge" src="https://img.shields.io/badge/Docker-badc58?style=flat-square&logo=docker">
<img alt="GitHub all releases" src="https://img.shields.io/github/downloads/JoeanAmier/TikTokDownloader/total?style=flat-square&color=ffdd59">
</div>
<br>
<p>🔥 <b>TikTok Posts/Liked/Mix/Live/Video/Image/Music; DouYin Posts/Liked/Favorites/Collections/Video/Image/LivePhoto/Live/Music/Mix/Comments/Account/Search/Hot Board Data Acquisition Tools:</b> Fully open-source, free data collection and file download tool based on HTTPX module implementation; batch download of DouYin account posts works, liked works, favorites works and collections works; batch download of TikTok account posts works and liked works; download of DouYin linked or TikTok linked works; obtain DouYin live stream push addresses; download DouYin live stream video; obtain TikTok live stream push addresses; download TikTok live stream video; collect DouYin works comments data; batch download of DouYin Mix works; batch download of TikTok Mix works; collect detailed data of DouYin accounts; collect DouYin user/works/live search results; collect DouYin Hot Board data.</p>
<p>⭐ Previous project names: <code>TikTokDownloader</code></p>
<p>📣 This project will undergo code structure refactoring in the future, with the goal of making the code more robust and providing better maintainability and extensibility. If you have any thoughts on project design, implementation methods, or optimization ideas, you are welcome to make suggestions or participate in discussions!</p>
<p>⭐ Due to the author's limited energy, I was unable to update the English document in a timely manner, and the content may have become outdated, partial translation is machine translation, the translation result may be incorrect, Suggest referring to Chinese documentation. If you want to contribute to translation, we warmly welcome you.</p>
<hr>

# 📝 Project Features

<details>
<summary>Function List (Click to Expand)</summary>
<ul>
<li>✅ Download DouYin video/image</li>
<li>✅ Download DouYin live photo</li>
<li>✅ Download the highest quality video file</li>
<li>✅ Download TikTok video source files</li>
<li>✅ Download TikTok video/image</li>
<li>✅ Download of DouYin account posts/liked/favorites works</li>
<li>✅ Download of TikTok account posts/liked works</li>
<li>✅ Collect detailed data from DouYin/TikTok</li>
<li>✅ Batch download of linked works</li>
<li>✅ Batch download of works from multiple accounts</li>
<li>✅ Automatically skip already downloaded files</li>
<li>✅ Persistently save collected data</li>
<li>✅ Support CSV/XLSX/SQLite format for saving data</li>
<li>✅ Download dynamic/static cover images</li>
<li>✅ Obtain DouYin live stream push addresses</li>
<li>✅ Obtain TikTok live stream push addresses</li>
<li>✅ Use ffmpeg to download live video</li>
<li>✅ Web UI interaction interface</li>
<li>✅ Collect comments data from DouYin works</li>
<li>✅ Batch download of DouYin Mix works</li>
<li>✅ Batch download of TikTok Mix works</li>
<li>✅ Record statistics such as likes and favorites</li>
<li>✅ Filter works based on publication time</li>
<li>✅ Support incremental downloading of account works</li>
<li>✅ Support data Collections using proxies</li>
<li>✅ Support remote access via LAN</li>
<li>✅ Collect detailed data from DouYin accounts</li>
<li>✅ Update statistics of works</li>
<li>✅ Support custom account/mix mark</li>
<li>✅ Automatically update account nickname/mark</li>
<li>✅ Deploy to private servers</li>
<li>✅ Deploy to public servers</li>
<li>✅ Collect DouYin search data</li>
<li>✅ Collect DouYin hot board data</li>
<li>✅ Record IDs of already downloaded works</li>
<li>☑️ <del>Scan QR code to log in and obtain Cookies</del></li>
<li>✅ Obtain Cookies from browsers</li>
<li>✅ Support Web API calls</li>
<li>✅ Support multithreaded downloading of works</li>
<li>✅ File integrity processing mechanism</li>
<li>✅ Custom rules for filtering works</li>
<li>✅ Archive and save works files by folder</li>
<li>✅ Customize file size limit</li>
<li>✅ Support resume downloading of files from breakpoints</li>
<li>✅ Monitor clipboard links to download works</li>
</ul>
</details>

# 💻 Program Screenshot

<p><a href="https://www.bilibili.com/video/BV1d7eAzTEFs/">Watch Demo on Bilibili</a>; <a href="https://youtu.be/yMU-RWl55hg">Watch Demo on YouTube</a></p>

## Terminal interaction mode

<p>It is recommended to manage accounts through configuration files. For more information, please refer to the <a href="https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation">documentation</a></p>

![终端模式截图](docs/screenshot/终端交互模式截图EN1.png)
*****
![终端模式截图](docs/screenshot/终端交互模式截图EN2.png)
*****
![终端模式截图](docs/screenshot/终端交互模式截图EN3.png)

## Web UI interaction mode

> **The project code has been refactored; the code for this mode has not yet been updated. It will be reopened after
future development is completed!**

## Web API mode

![WebAPI模式截图](docs/screenshot/WebAPI模式截图EN1.png)
*****
![WebAPI模式截图](docs/screenshot/WebAPI模式截图EN2.png)

> **After starting this mode, Open http://127.0.0.1:5555/docs or http://127.0.0.1:5555/redoc to access the automatically
generated documentation!**

### API call example code

```python
from httpx import post
from rich import print


def demo():
    headers = {"token": ""}
    data = {
        "detail_id": "0123456789",
        "pages": 2,
    }
    api = "http://127.0.0.1:5555/douyin/comment"
    response = post(api, json=data, headers=headers)
    print(response.json())


demo()
```

# 📋 Project Instructions

## Quick Start

<p>⭐ Mac OS and Windows 10 and above users can go to <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> or <a href="https://github.com/JoeanAmier/TikTokDownloader/actions">Actions</a> to download the compiled program, ready to use!</p>
<p>⭐ This project includes GitHub Actions for automatic building executable files. Users can use GitHub Actions to build the latest source code into executable files at any time!</p>
<p>⭐ For the automatic building executable files tutorial, please refer to the <code>Build of Executable File Guide</code> section of this document. If you need a more detailed step-by-step tutorial with illustrations, please <a href="https://mp.weixin.qq.com/s/TorfoZKkf4-x8IBNLImNuw">check out this article</a>!</p>
<p><strong>Note: Due to the macOS platform's executable file <code>main</code> not being code-signed, it will be restricted by system security measures on first run. Please execute the command <code>xattr -cr project_folder_path</code> in the terminal to remove the security flag, after which it can run normally.</strong></p>
<hr>
<ol>
<li><b>Run the executable file</b> or <b>configure the environment to run</b> (choose one of the two)
<ol><b>Run the executable file</b>
<li>Download the executable file compressed file built by <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> or Actions.</li>
<li>After extracting, open the program folder and double-click to run <code>main</code>.</li>
</ol>
<ol><b>Configure the environment to run</b>

[//]: # (<li>Install Python interpreter version not lower than <code>3.12</code></li>)
<li>Install the <a href="https://www.python.org/">Python</a> interpreter version <code>3.12</code></li>
<li>Download the latest source code or the source code released in <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> to your local machine</li>
<ol><b>Install project dependencies using pip</b>
<li>Run the command <code>python -m venv venv</code> to create a virtual environment (optional)</li>
<li>Run the command <code>.\venv\Scripts\activate.ps1</code> or <code>venv\Scripts\activate</code> to activate the virtual environment (optional)</li>
<li>Run the command <code>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt</code> to install the required modules for the program</li>
<li>Run the command <code>python .\main.py</code> or <code>python main.py</code> to start DouK-Downloader</li>
</ol>
<ol><b>Install project dependencies using uv (recommended)</b>
<li>Run the command <code>uv sync --no-dev</code> to synchronize environment dependencies</li>
<li>Run the command <code>uv run main.py</code> to start DouK-Downloader</li>
</ol>
</ol>
</li>
<li>Read the disclaimer of DouK-Downloader and enter content according to the prompt.</li>
<li>Write Cookie Information into Configuration File 
<ol><b>Read Cookie from Clipboard(Recommended)</b>
<li>Refer to the <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie Extraction Tutorial</a>, copy the required Cookie to the clipboard</li>
<li>Select the <code>Read Cookie from Clipboard</code> option, the program will automatically read the Cookie from the clipboard and write it into the configuration file</li>
</ol>
<ol><b>Read Cookie from Browser</b>
<li>Select the <code>Read Cookie from Browser</code> option, then follow the prompts to input the browser type or its corresponding number</li>
</ol>
<ol><b><del>Obtain Cookie via QR Code Login</del> (No longer valid)</b>
<li><del>Select the <code>Obtain Cookie via QR Code Login</code> option, the program will display a login QR code image and open it with the default application</del></li>
<li><del>Use the TikTok app to scan the QR code and log in</del></li>
<li><del>Follow the prompts, the program will automatically write the Cookie into the configuration file</del></li>
</ol>
</li>
<li>Return to the program interface, sequentially select <code>Terminal interactive mode</code> -> <code>Batch download link works (general)</code> -> <code>Manually enter the link of the works to be collected</code>.</li>
<li>Input the DouYin works link to download the works file (the TikTok platform requires more initial setup, please refer to the documentation for details).</li>
<li>For more detailed instructions, please see <b><a href="https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation">Project Documentation</a></b>.</li>
</ol>
<p>⭐ It is recommended to use <a href="https://learn.microsoft.com/zh-cn/windows/terminal/install">Windows Terminal</a> (the default terminal that comes with Windows 11).</p>

### Docker Container

<ol>
<li>Get the image</li>
<ul>
<li>Method 1: Build the image using the <code>Dockerfile</code>.</li>
<li>Method 2: Pull the image using the command <code>docker pull joeanamier/tiktok-downloader</code>.</li>
<li>Method 3: Pull the image using the command <code>docker pull ghcr.io/joeanamier/tiktok-downloader</code>.</li>
</ul>
<li>Create the container: <code>docker run --name ContainerName(optional) -p HostPort:5555 -v tiktok_downloader_volume:/app/Volume -it &lt;image name&gt;</code>.</li>
<br><b>Note:</b> The <code>&lt;image name&gt;</code> here must be consistent with the image name you used in the first step (<code>joeanamier/tiktok-downloader</code> or <code>ghcr.io/joeanamier/tiktok-downloader</code>)
<li>Run the container
<ul>
<li>Start the container: <code>docker start -i container name/container ID</code>.</li>
<li>Restart the container: <code>docker restart -i container name/container ID</code>.</li>
</ul>
</li>
</ol>
<p>Docker containers cannot directly access the host machine's file system, and some features may be unavailable, for example: <code>Get Cookie from Browser</code>; if there are any other issues, please report!</p>
<hr>

## About Cookie

[Click to view Cookie tutorial](https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md)

> * Cookie only needs to be re-written to the configuration file after it expires, and not every time the program is
    run.
>
> * The Cookie can affect the resolution of the video files downloaded from the DouYin platform. If you are unable to
    download high-resolution video files, please try updating the Cookie!
>
> * When the program fails to obtain data, you can try updating the Cookie or using a Cookie that is already logged in!

<hr>

## Other Instructions

<ul>
<li>When the program prompts the user for input, pressing Enter directly will return to the previous menu, and inputting <code>Q</code> or <code>q</code> will end the program's execution.</li>
<li>Since fetching data for liked and favorites works of an account only returns the publication dates of those works, not the dates of the actions (liking or favouring), the program needs to retrieve all liked and favorites works data before performing date filtering. If there are a large number of works, this may take a considerable amount of time. The number of requests can be controlled via the <code>max_pages</code> parameter.</li>
<li>To obtain data for posts made by a private account, a logged-in Cookie is required, and the logged-in account must follow the private account.</li>
<li>When batch downloading account posts works or mix works, if the corresponding nickname or mark parameter changes, the program will automatically update the nickname and mark parameter in the file names of the downloaded works.</li>
<li>When downloading files, the program first downloads them to a temporary folder and then moves them to the storage folder upon completion. The temporary folder will be emptied when the program ends.</li>
<li>The <code>Batch Download Favorites Works Mode</code> currently only supports downloading Favorites works for the account corresponding to the currently logged-in Cookie and does not support multiple accounts.</li>
<li>If you want the program to use a proxy to request data, you must set the <code>proxy</code> parameter in <code>settings.json</code>; otherwise, the program will not use a proxy.</li>
<li>If your computer does not have a suitable program for editing JSON files, we recommend using the <a href="https://www.toolhelper.cn/JSON/JSONFormat">Online Tool</a> to edit the configuration file content, after modification, the software needs to be restarted to take effect.</li>
<li>When the program prompts the user to input content or links, please be careful to avoid including newline characters, as this may cause unexpected issues.</li>
<li>This project does not support downloading paid works. Please do not report any issues related to downloading paid works.</li>
<li>On Windows systems, the program needs to be run as an administrator to read Cookies from Chromium, Chrome, and Edge browsers.</li>
<li>This project has not been optimized for running multiple instances of the program. If you need to run multiple instances, please copy the entire project folder to avoid unexpected issues.</li>
<li>During program execution, if you need to terminate the program or <code>ffmpeg</code>, please press <code>Ctrl + C</code> to stop the process. Do not click the close button on the terminal window directly.</li>
</ul>
<h2>Build of Executable File Guide</h2>
<details>
<summary>Build of Executable File Guide (Click to Expand)</summary>

This guide will walk you through forking this repository and executing GitHub Actions to automatically build and package
the program based on the latest source code!

---

### Steps to Use

#### 1. Fork the Repository

1. Click the **Fork** button at the top right of the project repository to fork it to your personal GitHub account
2. Your forked repository address will look like this: `https://github.com/your-username/this-repo`

---

#### 2. Enable GitHub Actions

1. Go to the page of your forked repository
2. Click the **Settings** tab at the top
3. Click the **Actions** tab on the right
4. Click the **General** option
5. Under **Actions permissions**, select **Allow all actions and reusable workflows** and click the **Save** button

---

#### 3. Manually Trigger the Build Process

1. In your forked repository, click the **Actions** tab at the top
2. Find the workflow named **构建可执行文件**
3. Click the **Run workflow** button on the right:
    - Select the **master** or **develop** branch
    - Click **Run workflow**

---

#### 4. Check the Build Progress

1. On the **Actions** page, you can see the execution records of the triggered workflow
2. Click on the run record to view detailed logs to check the build progress and status

---

#### 5. Download the Build Result

1. Once the build is complete, go to the corresponding run record page
2. In the **Artifacts** section at the bottom of the page, you will see the built result file
3. Click to download and save it to your local machine to get the built program

---

### Notes

1. **Resource Usage**:
    - GitHub provides free build environments for Actions, with a monthly usage limit (2000 minutes) for free-tier
      users

2. **Code Modifications**:
    - You are free to modify the code in your forked repository to customize the build process
    - After making changes, you can trigger the build process again to get your customized version

3. **Stay in Sync with the Main Repository**:
    - If the main repository is updated with new code or workflows, it is recommended that you periodically sync your
      forked repository to get the latest features and fixes

---

### Frequently Asked Questions

#### Q1: Why can't I trigger the workflow?

A: Please ensure that you have followed the steps to **Enable Actions**. Otherwise, GitHub will prevent the workflow
from running

#### Q2: What should I do if the build process fails?

A:

- Check the run logs to understand the cause of the failure
- Ensure there are no syntax errors or dependency issues in the code
- If the problem persists, please open an issue on
  the [Issues page](https://github.com/JoeanAmier/TikTokDownloader/issues)

#### Q3: Can I directly use the Actions from the main repository?

A: Due to permission restrictions, you cannot directly trigger Actions from the main repository. Please use the forked
repository to execute the build process

</details>

## Program Update

<p><strong>Method 1:</strong> Download and extract the files, then copy the old version of the <code>_internal\Volume</code> folder into the new version's <code>_internal</code> folder.</p>
<p><strong>Method 2:</strong> Download and extract the files (do not run the program), then copy all files and directly overwrite the old version.</p>

# ⚠️ Disclaimer

<ol>
<li>The user's use of this project is entirely at their own discretion and responsibility. The author assumes no liability for any losses, claims, or risks arising from the user's use of this project.</li>
<li>The code and functionalities provided by the author of this project are based on current knowledge and technological developments. The author strives to ensure the correctness and security of the code according to existing technical capabilities but does not guarantee that the code is entirely free of errors or defects.</li>
<li>All third-party libraries, plugins, or services relied upon by this project follow their respective open-source or commercial licenses. Users must review and comply with those license agreements. The author assumes no responsibility for the stability, security, or compliance of third-party components.</li>
<li>Users must strictly comply with the requirements of the <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/LICENSE">GNU General Public License v3.0</a> when using this project and properly indicate that the code was used under the <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/LICENSE">GNU General Public License v3.0</a>.</li>
<li>When using the code and features of this project, users must independently research relevant laws and regulations and ensure their actions are legal and compliant. Any legal liabilities or risks arising from violations of laws and regulations shall be borne solely by the user.</li>
<li>Users must not use this tool to engage in any activities that infringe intellectual property rights, including but not limited to downloading or distributing copyright-protected content without authorization. The developers do not participate in, support, or endorse any unauthorized acquisition or distribution of illegal content.</li>
<li>This project assumes no responsibility for the compliance of any data processing activities (including collection, storage, and transmission) conducted by users. Users must comply with relevant laws and regulations and ensure that their processing activities are lawful and proper. Legal liabilities resulting from non-compliant operations shall be borne by the user.</li>
<li>Under no circumstances may users associate the author, contributors, or other related parties of this project with their usage of the project, nor may they hold these parties responsible for any loss or damage arising from such usage.</li>
<li>The author of this project will not provide a paid version of the DouK-Downloader project, nor will they offer any commercial services related to the DouK-Downloader project.</li>
<li>Any secondary development, modification, or compilation based on this project is unrelated to the original author. The original author assumes no liability for any consequences resulting from such secondary development. Users bear full responsibility for all outcomes arising from such modifications.</li>
<li>This project grants no patent licenses; if the use of this project leads to patent disputes or infringement, the user bears all associated risks and responsibilities. Without written authorization from the author or rights holder, users may not use this project for any commercial promotion, marketing, or re-licensing.</li>
<li>The author reserves the right to terminate service to any user who violates this disclaimer at any time and may require them to destroy all obtained code and derivative works.</li>
<li>The author reserves the right to update this disclaimer at any time without prior notice. Continued use of the project constitutes acceptance of the revised terms.</li>
</ol>
<b>Before using the code and functionalities of this project, please carefully consider and accept the above disclaimer. If you have any questions or disagree with the statement, please do not use the code and functionalities of this project. If you use the code and functionalities of this project, it is considered that you fully understand and accept the above disclaimer, and willingly assume all risks and consequences associated with the use of this project.</b>
<h1>🌟 Contribution Guidelines</h1>
<p><strong>Welcome to contributing to this project! To keep the codebase clean, efficient, and easy to maintain, please read the following guidelines carefully to ensure that your contributions can be accepted and integrated smoothly.</strong></p>
<ul>
<li>Before starting development, please pull the latest code from the <code>develop</code> branch as the basis for your modifications; this helps avoid merge conflicts and ensures your changes are based on the latest state of the project.</li>
<li>If your changes involve multiple unrelated features or issues, please split them into several independent commits or pull requests.</li>
<li>Each pull request should focus on a single feature or fix as much as possible, to facilitate code review and testing.</li>
<li>Follow the existing coding style; make sure your code is consistent with the style already present in the project; please use the Ruff tool to maintain code formatting standards.</li>
<li>Write code that is easy to read; add appropriate annotation to help others understand your intentions.</li>
<li>Each commit should include a clear and concise commit message describing the changes made. The commit message should follow this format: <code>&lt;type&gt;: &lt;short description&gt;</code></li>
<li>When you are ready to submit a pull request, please prioritize submitting them to the <code>develop</code> branch; this provides maintainers with a buffer zone for additional testing and review before final merging into the <code>master</code> branch.</li>
<li>It is recommended to communicate with the author before starting development or when encountering questions to ensure alignment in direction and avoid redundant efforts or unnecessary commits.</li>
</ul>
<p><strong>Reference materials:</strong></p>
<ul>
<li><a href="https://www.contributor-covenant.org/version/2/1/code_of_conduct/">Contributor Covenant</a></li>
<li><a href="https://opensource.guide/how-to-contribute/">How to Contribute to Open Source</a></li>
</ul>

# ♥️ Support the Project

<p>If <b>DouK-Downloader</b> has been helpful to you, please consider giving it a <b>Star</b> ⭐. Your support is greatly appreciated!</p>
<table>
<thead>
<tr>
<th align="center">微信(WeChat)</th>
<th align="center">支付宝(Alipay)</th>
</tr>
</thead>
<tbody><tr>
<td align="center"><img src="./docs/微信赞助二维码.png" alt="微信赞助二维码" height="200" width="200"></td>
<td align="center"><img src="./docs/支付宝赞助二维码.png" alt="支付宝赞助二维码" height="200" width="200"></td>
</tr>
</tbody>
</table>
<p>If you're willing, consider making a contribution to provide additional support for <b>DouK-Downloader</b>!</p>

# 💰 Project Sponsorship

## DartNode

[![Powered by DartNode](docs/AD/DartNode_AD.png)](https://dartnode.com "Powered by DartNode - Free VPS for Open Source")

***

## ZMTO

<p><a href="https://www.zmto.com/"><img src="https://console.zmto.com/templates/2019/dist/images/logo_dark.svg" alt="ZMTO"></a></p>
<p><a href="https://www.zmto.com/">ZMTO</a>: A professional cloud infrastructure provider offering sophisticated solutions with reliable technology and expert support. We also empower qualified open source initiatives with enterprise-grade VPS infrastructure, driving sustainable development and innovation in the open source ecosystem. </p>

***

## TikHub

<p><a href="https://tikhub.io/?utm_source=github&utm_medium=readme&utm_campaign=tiktok_downloader&ref=github_joeanamier_tiktokdownloader"><img src="docs/AD/TIKHUB_AD.jpg" alt="TIKHUB" width="458" height="319"></a></p>
<p><a href="https://tikhub.io/?utm_source=github&utm_medium=readme&utm_campaign=tiktok_downloader&ref=github_joeanamier_tiktokdownloader">TikHub API</a> offers over 700 endpoints to retrieve and analyze data from 14+ social media platforms—including videos, users, comments, stores, products, trends, and more—enabling one-stop access and analysis of all your data.</p>
<p>Use <strong>invitation code</strong>: <code>ZrdH8McC</code> to register and recharge to get <code>$2</code> credit.</p>

# ✉️ Contact the Author

<ul>
<li>Author's Email: yonglelolu@foxmail.com</li>
<li>Author's WeChat: Downloader_Tools</li>
<li>Official WeChat Account: Downloader Tools</li>
<li><b>Discord Community</b>: <a href="https://discord.com/invite/ZYtmgKud9Y">Click to join the community</a></li>
</ul>
<p>✨ <b>The author's other open-source projects:</b></p>
<ul>
<li><b>XHS-Downloader（小红书、XiaoHongShu、RedNote）</b>：<a href="https://github.com/JoeanAmier/XHS-Downloader">https://github.com/JoeanAmier/XHS-Downloader</a></li>
<li><b>KS-Downloader（快手、KuaiShou）</b>：<a href="https://github.com/JoeanAmier/KS-Downloader">https://github.com/JoeanAmier/KS-Downloader</a></li>
</ul>
<h1>⭐ Star History</h1>
<p>
<img alt="Star History Chart" src="https://api.star-history.com/svg?repos=JoeanAmier/TikTokDownloader&amp;type=Timeline"/>
</p>

# 💡 Project References

* https://github.com/Johnserf-Seed/f2
* https://github.com/Evil0ctal/Douyin_TikTok_Download_API
* https://github.com/justbeluga/tiktok-web-reverse-engineering
* https://github.com/ihmily/DouyinLiveRecorder
* https://github.com/encode/httpx/
* https://github.com/Textualize/rich
* https://github.com/omnilib/aiosqlite
* https://github.com/Tinche/aiofiles
* https://github.com/pyinstaller/pyinstaller
* https://foss.heptapod.net/openpyxl/openpyxl
* https://github.com/carpedm20/emoji/
* https://github.com/lxml/lxml
* https://ffmpeg.org/ffmpeg-all.html
```

## File: `requirements.txt`
```
# This file was autogenerated by uv via the following command:
#    uv pip compile pyproject.toml --no-deps --no-strip-extras -o requirements.txt
aiofiles==25.1.0
    # via douk-downloader (pyproject.toml)
aiosqlite==0.22.1
    # via douk-downloader (pyproject.toml)
emoji==2.15.0
    # via douk-downloader (pyproject.toml)
fastapi==0.135.2
    # via douk-downloader (pyproject.toml)
gmssl==3.2.2
    # via douk-downloader (pyproject.toml)
httpx[socks]==0.28.1
    # via douk-downloader (pyproject.toml)
lxml==6.0.2
    # via douk-downloader (pyproject.toml)
openpyxl==3.1.5
    # via douk-downloader (pyproject.toml)
pydantic==2.12.5
    # via douk-downloader (pyproject.toml)
pyperclip==1.11.0
    # via douk-downloader (pyproject.toml)
qrcode==8.2
    # via douk-downloader (pyproject.toml)
rich==14.3.3
    # via douk-downloader (pyproject.toml)
rookiepy==0.5.6
    # via douk-downloader (pyproject.toml)
uvicorn==0.42.0
    # via douk-downloader (pyproject.toml)
```

## File: `uv.lock`
```
version = 1
revision = 3
requires-python = "==3.12.*"

[[package]]
name = "aiofiles"
version = "25.1.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/41/c3/534eac40372d8ee36ef40df62ec129bee4fdb5ad9706e58a29be53b2c970/aiofiles-25.1.0.tar.gz", hash = "sha256:a8d728f0a29de45dc521f18f07297428d56992a742f0cd2701ba86e44d23d5b2", size = 46354, upload-time = "2025-10-09T20:51:04.358Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/bc/8a/340a1555ae33d7354dbca4faa54948d76d89a27ceef032c8c3bc661d003e/aiofiles-25.1.0-py3-none-any.whl", hash = "sha256:abe311e527c862958650f9438e859c1fa7568a141b22abcd015e120e86a85695", size = 14668, upload-time = "2025-10-09T20:51:03.174Z" },
]

[[package]]
name = "aiosqlite"
version = "0.22.1"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/4e/8a/64761f4005f17809769d23e518d915db74e6310474e733e3593cfc854ef1/aiosqlite-0.22.1.tar.gz", hash = "sha256:043e0bd78d32888c0a9ca90fc788b38796843360c855a7262a532813133a0650", size = 14821, upload-time = "2025-12-23T19:25:43.997Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/00/b7/e3bf5133d697a08128598c8d0abc5e16377b51465a33756de24fa7dee953/aiosqlite-0.22.1-py3-none-any.whl", hash = "sha256:21c002eb13823fad740196c5a2e9d8e62f6243bd9e7e4a1f87fb5e44ecb4fceb", size = 17405, upload-time = "2025-12-23T19:25:42.139Z" },
]

[[package]]
name = "annotated-doc"
version = "0.0.4"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/57/ba/046ceea27344560984e26a590f90bc7f4a75b06701f653222458922b558c/annotated_doc-0.0.4.tar.gz", hash = "sha256:fbcda96e87e9c92ad167c2e53839e57503ecfda18804ea28102353485033faa4", size = 7288, upload-time = "2025-11-10T22:07:42.062Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/1e/d3/26bf1008eb3d2daa8ef4cacc7f3bfdc11818d111f7e2d0201bc6e3b49d45/annotated_doc-0.0.4-py3-none-any.whl", hash = "sha256:571ac1dc6991c450b25a9c2d84a3705e2ae7a53467b5d111c24fa8baabbed320", size = 5303, upload-time = "2025-11-10T22:07:40.673Z" },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anyio"
version = "4.12.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "idna" },
    { name = "typing-extensions" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/16/ce/8a777047513153587e5434fd752e89334ac33e379aa3497db860eeb60377/anyio-4.12.0.tar.gz", hash = "sha256:73c693b567b0c55130c104d0b43a9baf3aa6a31fc6110116509f27bf75e21ec0", size = 228266, upload-time = "2025-11-28T23:37:38.911Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/7f/9c/36c5c37947ebfb8c7f22e0eb6e4d188ee2d53aa3880f3f2744fb894f0cb1/anyio-4.12.0-py3-none-any.whl", hash = "sha256:dad2376a628f98eeca4881fc56cd06affd18f659b17a747d3ff0307ced94b1bb", size = 113362, upload-time = "2025-11-28T23:36:57.897Z" },
]

[[package]]
name = "certifi"
version = "2025.11.12"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/a2/8c/58f469717fa48465e4a50c014a0400602d3c437d7c0c468e17ada824da3a/certifi-2025.11.12.tar.gz", hash = "sha256:d8ab5478f2ecd78af242878415affce761ca6bc54a22a27e026d7c25357c3316", size = 160538, upload-time = "2025-11-12T02:54:51.517Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/70/7d/9bc192684cea499815ff478dfcdc13835ddf401365057044fb721ec6bddb/certifi-2025.11.12-py3-none-any.whl", hash = "sha256:97de8790030bbd5c2d96b7ec782fc2f7820ef8dba6db909ccf95449f2d062d4b", size = 159438, upload-time = "2025-11-12T02:54:49.735Z" },
]

[[package]]
name = "click"
version = "8.3.1"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/3d/fa/656b739db8587d7b5dfa22e22ed02566950fbfbcdc20311993483657a5c0/click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a", size = 295065, upload-time = "2025-11-15T20:45:42.706Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/98/78/01c019cdb5d6498122777c1a43056ebb3ebfeef2076d9d026bfe15583b2b/click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6", size = 108274, upload-time = "2025-11-15T20:45:41.139Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "douk-downloader"
version = "5.8"
source = { virtual = "." }
dependencies = [
    { name = "aiofiles" },
    { name = "aiosqlite" },
    { name = "emoji" },
    { name = "fastapi" },
    { name = "gmssl" },
    { name = "httpx", extra = ["socks"] },
    { name = "lxml" },
    { name = "openpyxl" },
    { name = "pydantic" },
    { name = "pyperclip" },
    { name = "rich" },
    { name = "rookiepy" },
    { name = "uvicorn" },
]

[package.dev-dependencies]
dev = [
    { name = "pytest" },
]

[package.metadata]
requires-dist = [
    { name = "aiofiles", specifier = ">=25.1.0" },
    { name = "aiosqlite", specifier = ">=0.21.0" },
    { name = "emoji", specifier = ">=2.15.0" },
    { name = "fastapi", specifier = ">=0.124.2" },
    { name = "gmssl", specifier = ">=3.2.2" },
    { name = "httpx", extras = ["socks"], specifier = ">=0.28.1" },
    { name = "lxml", specifier = ">=6.0.2" },
    { name = "openpyxl", specifier = ">=3.1.5" },
    { name = "pydantic", specifier = ">=2.12.5" },
    { name = "pyperclip", specifier = ">=1.11.0" },
    { name = "rich", specifier = ">=14.2.0" },
    { name = "rookiepy", specifier = ">=0.5.6" },
    { name = "uvicorn", specifier = ">=0.38.0" },
]

[package.metadata.requires-dev]
dev = [{ name = "pytest", specifier = ">=8.3.5" }]

[[package]]
name = "emoji"
version = "2.15.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/a2/78/0d2db9382c92a163d7095fc08efff7800880f830a152cfced40161e7638d/emoji-2.15.0.tar.gz", hash = "sha256:eae4ab7d86456a70a00a985125a03263a5eac54cd55e51d7e184b1ed3b6757e4", size = 615483, upload-time = "2025-09-21T12:13:02.755Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/e1/5e/4b5aaaabddfacfe36ba7768817bd1f71a7a810a43705e531f3ae4c690767/emoji-2.15.0-py3-none-any.whl", hash = "sha256:205296793d66a89d88af4688fa57fd6496732eb48917a87175a023c8138995eb", size = 608433, upload-time = "2025-09-21T12:13:01.197Z" },
]

[[package]]
name = "et-xmlfile"
version = "2.0.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/d3/38/af70d7ab1ae9d4da450eeec1fa3918940a5fafb9055e934af8d6eb0c2313/et_xmlfile-2.0.0.tar.gz", hash = "sha256:dab3f4764309081ce75662649be815c4c9081e88f0837825f90fd28317d4da54", size = 17234, upload-time = "2024-10-25T17:25:40.039Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/c1/8b/5fe2cc11fee489817272089c4203e679c63b570a5aaeb18d852ae3cbba6a/et_xmlfile-2.0.0-py3-none-any.whl", hash = "sha256:7a91720bc756843502c3b7504c77b8fe44217c85c537d85037f0f536151b2caa", size = 18059, upload-time = "2024-10-25T17:25:39.051Z" },
]

[[package]]
name = "fastapi"
version = "0.135.2"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "annotated-doc" },
    { name = "pydantic" },
    { name = "starlette" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/c4/73/5903c4b13beae98618d64eb9870c3fac4f605523dd0312ca5c80dadbd5b9/fastapi-0.135.2.tar.gz", hash = "sha256:88a832095359755527b7f63bb4c6bc9edb8329a026189eed83d6c1afcf419d56", size = 395833, upload-time = "2026-03-23T14:12:41.697Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/8f/ea/18f6d0457f9efb2fc6fa594857f92810cadb03024975726db6546b3d6fcf/fastapi-0.135.2-py3-none-any.whl", hash = "sha256:0af0447d541867e8db2a6a25c23a8c4bd80e2394ac5529bd87501bbb9e240ca5", size = 117407, upload-time = "2026-03-23T14:12:43.284Z" },
]

[[package]]
name = "gmssl"
version = "3.2.2"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "pycryptodomex" },
]
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/41/b1/01d707a2edfaad77715b2d27e5fbf14b6bcd34dd72ea179a5facfe4b1dd7/gmssl-3.2.2-py3-none-any.whl", hash = "sha256:59f069a91eb19ef59b9e7be4d436ed01c92ce064d3d7d45a8778fc07fd2cd068", size = 10185, upload-time = "2023-02-23T06:01:39.296Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[package.optional-dependencies]
socks = [
    { name = "socksio" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "iniconfig"
version = "2.3.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/72/34/14ca021ce8e5dfedc35312d08ba8bf51fdd999c576889fc2c24cb97f4f10/iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730", size = 20503, upload-time = "2025-10-18T21:55:43.219Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/cb/b1/3846dd7f199d53cb17f49cba7e651e9ce294d8497c8c150530ed11865bb8/iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12", size = 7484, upload-time = "2025-10-18T21:55:41.639Z" },
]

[[package]]
name = "lxml"
version = "6.0.2"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/aa/88/262177de60548e5a2bfc46ad28232c9e9cbde697bd94132aeb80364675cb/lxml-6.0.2.tar.gz", hash = "sha256:cd79f3367bd74b317dda655dc8fcfa304d9eb6e4fb06b7168c5cf27f96e0cd62", size = 4073426, upload-time = "2025-09-22T04:04:59.287Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/f3/c8/8ff2bc6b920c84355146cd1ab7d181bc543b89241cfb1ebee824a7c81457/lxml-6.0.2-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:a59f5448ba2ceccd06995c95ea59a7674a10de0810f2ce90c9006f3cbc044456", size = 8661887, upload-time = "2025-09-22T04:01:17.265Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/37/6f/9aae1008083bb501ef63284220ce81638332f9ccbfa53765b2b7502203cf/lxml-6.0.2-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:e8113639f3296706fbac34a30813929e29247718e88173ad849f57ca59754924", size = 4667818, upload-time = "2025-09-22T04:01:19.688Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/f1/ca/31fb37f99f37f1536c133476674c10b577e409c0a624384147653e38baf2/lxml-6.0.2-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:a8bef9b9825fa8bc816a6e641bb67219489229ebc648be422af695f6e7a4fa7f", size = 4950807, upload-time = "2025-09-22T04:01:21.487Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/da/87/f6cb9442e4bada8aab5ae7e1046264f62fdbeaa6e3f6211b93f4c0dd97f1/lxml-6.0.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:65ea18d710fd14e0186c2f973dc60bb52039a275f82d3c44a0e42b43440ea534", size = 5109179, upload-time = "2025-09-22T04:01:23.32Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/c8/20/a7760713e65888db79bbae4f6146a6ae5c04e4a204a3c48896c408cd6ed2/lxml-6.0.2-cp312-cp312-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c371aa98126a0d4c739ca93ceffa0fd7a5d732e3ac66a46e74339acd4d334564", size = 5023044, upload-time = "2025-09-22T04:01:25.118Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/a2/b0/7e64e0460fcb36471899f75831509098f3fd7cd02a3833ac517433cb4f8f/lxml-6.0.2-cp312-cp312-manylinux_2_26_i686.manylinux_2_28_i686.whl", hash = "sha256:700efd30c0fa1a3581d80a748157397559396090a51d306ea59a70020223d16f", size = 5359685, upload-time = "2025-09-22T04:01:27.398Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/b9/e1/e5df362e9ca4e2f48ed6411bd4b3a0ae737cc842e96877f5bf9428055ab4/lxml-6.0.2-cp312-cp312-manylinux_2_26_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:c33e66d44fe60e72397b487ee92e01da0d09ba2d66df8eae42d77b6d06e5eba0", size = 5654127, upload-time = "2025-09-22T04:01:29.629Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/c6/d1/232b3309a02d60f11e71857778bfcd4acbdb86c07db8260caf7d008b08f8/lxml-6.0.2-cp312-cp312-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:90a345bbeaf9d0587a3aaffb7006aa39ccb6ff0e96a57286c0cb2fd1520ea192", size = 5253958, upload-time = "2025-09-22T04:01:31.535Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/35/35/d955a070994725c4f7d80583a96cab9c107c57a125b20bb5f708fe941011/lxml-6.0.2-cp312-cp312-manylinux_2_31_armv7l.whl", hash = "sha256:064fdadaf7a21af3ed1dcaa106b854077fbeada827c18f72aec9346847cd65d0", size = 4711541, upload-time = "2025-09-22T04:01:33.801Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/1e/be/667d17363b38a78c4bd63cfd4b4632029fd68d2c2dc81f25ce9eb5224dd5/lxml-6.0.2-cp312-cp312-manylinux_2_38_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:fbc74f42c3525ac4ffa4b89cbdd00057b6196bcefe8bce794abd42d33a018092", size = 5267426, upload-time = "2025-09-22T04:01:35.639Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/ea/47/62c70aa4a1c26569bc958c9ca86af2bb4e1f614e8c04fb2989833874f7ae/lxml-6.0.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:6ddff43f702905a4e32bc24f3f2e2edfe0f8fde3277d481bffb709a4cced7a1f", size = 5064917, upload-time = "2025-09-22T04:01:37.448Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/bd/55/6ceddaca353ebd0f1908ef712c597f8570cc9c58130dbb89903198e441fd/lxml-6.0.2-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:6da5185951d72e6f5352166e3da7b0dc27aa70bd1090b0eb3f7f7212b53f1bb8", size = 4788795, upload-time = "2025-09-22T04:01:39.165Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/cf/e8/fd63e15da5e3fd4c2146f8bbb3c14e94ab850589beab88e547b2dbce22e1/lxml-6.0.2-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:57a86e1ebb4020a38d295c04fc79603c7899e0df71588043eb218722dabc087f", size = 5676759, upload-time = "2025-09-22T04:01:41.506Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/76/47/b3ec58dc5c374697f5ba37412cd2728f427d056315d124dd4b61da381877/lxml-6.0.2-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:2047d8234fe735ab77802ce5f2297e410ff40f5238aec569ad7c8e163d7b19a6", size = 5255666, upload-time = "2025-09-22T04:01:43.363Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/19/93/03ba725df4c3d72afd9596eef4a37a837ce8e4806010569bedfcd2cb68fd/lxml-6.0.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:6f91fd2b2ea15a6800c8e24418c0775a1694eefc011392da73bc6cef2623b322", size = 5277989, upload-time = "2025-09-22T04:01:45.215Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/c6/80/c06de80bfce881d0ad738576f243911fccf992687ae09fd80b734712b39c/lxml-6.0.2-cp312-cp312-win32.whl", hash = "sha256:3ae2ce7d6fedfb3414a2b6c5e20b249c4c607f72cb8d2bb7cc9c6ec7c6f4e849", size = 3611456, upload-time = "2025-09-22T04:01:48.243Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/f7/d7/0cdfb6c3e30893463fb3d1e52bc5f5f99684a03c29a0b6b605cfae879cd5/lxml-6.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:72c87e5ee4e58a8354fb9c7c84cbf95a1c8236c127a5d1b7683f04bed8361e1f", size = 4011793, upload-time = "2025-09-22T04:01:50.042Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/ea/7b/93c73c67db235931527301ed3785f849c78991e2e34f3fd9a6663ffda4c5/lxml-6.0.2-cp312-cp312-win_arm64.whl", hash = "sha256:61cb10eeb95570153e0c0e554f58df92ecf5109f75eacad4a95baa709e26c3d6", size = 3672836, upload-time = "2025-09-22T04:01:52.145Z" },
]

[[package]]
name = "markdown-it-py"
version = "4.0.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/5b/f5/4ec618ed16cc4f8fb3b701563655a69816155e79e24a17b651541804721d/markdown_it_py-4.0.0.tar.gz", hash = "sha256:cb0a2b4aa34f932c007117b194e945bd74e0ec24133ceb5bac59009cda1cb9f3", size = 73070, upload-time = "2025-08-11T12:57:52.854Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/94/54/e7d793b573f298e1c9013b8c4dade17d481164aa517d1d7148619c2cedbf/markdown_it_py-4.0.0-py3-none-any.whl", hash = "sha256:87327c59b172c5011896038353a81343b6754500a08cd7a4973bb48c6d578147", size = 87321, upload-time = "2025-08-11T12:57:51.923Z" },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729, upload-time = "2022-08-14T12:40:10.846Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979, upload-time = "2022-08-14T12:40:09.779Z" },
]

[[package]]
name = "openpyxl"
version = "3.1.5"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "et-xmlfile" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/3d/f9/88d94a75de065ea32619465d2f77b29a0469500e99012523b91cc4141cd1/openpyxl-3.1.5.tar.gz", hash = "sha256:cf0e3cf56142039133628b5acffe8ef0c12bc902d2aadd3e0fe5878dc08d1050", size = 186464, upload-time = "2024-06-28T14:03:44.161Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/c0/da/977ded879c29cbd04de313843e76868e6e13408a94ed6b987245dc7c8506/openpyxl-3.1.5-py2.py3-none-any.whl", hash = "sha256:5282c12b107bffeef825f4617dc029afaf41d0ea60823bbb665ef3079dc79de2", size = 250910, upload-time = "2024-06-28T14:03:41.161Z" },
]

[[package]]
name = "packaging"
version = "25.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/a1/d4/1fc4078c65507b51b96ca8f8c3ba19e6a61c8253c72794544580a7b6c24d/packaging-25.0.tar.gz", hash = "sha256:d443872c98d677bf60f6a1f2f8c1cb748e8fe762d2bf9d3148b5599295b0fc4f", size = 165727, upload-time = "2025-04-19T11:48:59.673Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/20/12/38679034af332785aac8774540895e234f4d07f7545804097de4b666afd8/packaging-25.0-py3-none-any.whl", hash = "sha256:29572ef2b1f17581046b3a2227d5c611fb25ec70ca1ba8554b24b0e69331a484", size = 66469, upload-time = "2025-04-19T11:48:57.875Z" },
]

[[package]]
name = "pluggy"
version = "1.6.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3", size = 69412, upload-time = "2025-05-15T12:30:07.975Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/54/20/4d324d65cc6d9205fabedc306948156824eb9f0ee1633355a8f7ec5c66bf/pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746", size = 20538, upload-time = "2025-05-15T12:30:06.134Z" },
]

[[package]]
name = "pycryptodomex"
version = "3.23.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/c9/85/e24bf90972a30b0fcd16c73009add1d7d7cd9140c2498a68252028899e41/pycryptodomex-3.23.0.tar.gz", hash = "sha256:71909758f010c82bc99b0abf4ea12012c98962fbf0583c2164f8b84533c2e4da", size = 4922157, upload-time = "2025-05-17T17:23:41.434Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/dd/9c/1a8f35daa39784ed8adf93a694e7e5dc15c23c741bbda06e1d45f8979e9e/pycryptodomex-3.23.0-cp37-abi3-macosx_10_9_universal2.whl", hash = "sha256:06698f957fe1ab229a99ba2defeeae1c09af185baa909a31a5d1f9d42b1aaed6", size = 2499240, upload-time = "2025-05-17T17:22:46.953Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/7a/62/f5221a191a97157d240cf6643747558759126c76ee92f29a3f4aee3197a5/pycryptodomex-3.23.0-cp37-abi3-macosx_10_9_x86_64.whl", hash = "sha256:b2c2537863eccef2d41061e82a881dcabb04944c5c06c5aa7110b577cc487545", size = 1644042, upload-time = "2025-05-17T17:22:49.098Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/8c/fd/5a054543c8988d4ed7b612721d7e78a4b9bf36bc3c5ad45ef45c22d0060e/pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:43c446e2ba8df8889e0e16f02211c25b4934898384c1ec1ec04d7889c0333587", size = 2186227, upload-time = "2025-05-17T17:22:51.139Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/c8/a9/8862616a85cf450d2822dbd4fff1fcaba90877907a6ff5bc2672cafe42f8/pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f489c4765093fb60e2edafdf223397bc716491b2b69fe74367b70d6999257a5c", size = 2272578, upload-time = "2025-05-17T17:22:53.676Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/46/9f/bda9c49a7c1842820de674ab36c79f4fbeeee03f8ff0e4f3546c3889076b/pycryptodomex-3.23.0-cp37-abi3-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:bdc69d0d3d989a1029df0eed67cc5e8e5d968f3724f4519bd03e0ec68df7543c", size = 2312166, upload-time = "2025-05-17T17:22:56.585Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/03/cc/870b9bf8ca92866ca0186534801cf8d20554ad2a76ca959538041b7a7cf4/pycryptodomex-3.23.0-cp37-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:6bbcb1dd0f646484939e142462d9e532482bc74475cecf9c4903d4e1cd21f003", size = 2185467, upload-time = "2025-05-17T17:22:59.237Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/96/e3/ce9348236d8e669fea5dd82a90e86be48b9c341210f44e25443162aba187/pycryptodomex-3.23.0-cp37-abi3-musllinux_1_2_i686.whl", hash = "sha256:8a4fcd42ccb04c31268d1efeecfccfd1249612b4de6374205376b8f280321744", size = 2346104, upload-time = "2025-05-17T17:23:02.112Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/a5/e9/e869bcee87beb89040263c416a8a50204f7f7a83ac11897646c9e71e0daf/pycryptodomex-3.23.0-cp37-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:55ccbe27f049743a4caf4f4221b166560d3438d0b1e5ab929e07ae1702a4d6fd", size = 2271038, upload-time = "2025-05-17T17:23:04.872Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/8d/67/09ee8500dd22614af5fbaa51a4aee6e342b5fa8aecf0a6cb9cbf52fa6d45/pycryptodomex-3.23.0-cp37-abi3-win32.whl", hash = "sha256:189afbc87f0b9f158386bf051f720e20fa6145975f1e76369303d0f31d1a8d7c", size = 1771969, upload-time = "2025-05-17T17:23:07.115Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/69/96/11f36f71a865dd6df03716d33bd07a67e9d20f6b8d39820470b766af323c/pycryptodomex-3.23.0-cp37-abi3-win_amd64.whl", hash = "sha256:52e5ca58c3a0b0bd5e100a9fbc8015059b05cffc6c66ce9d98b4b45e023443b9", size = 1803124, upload-time = "2025-05-17T17:23:09.267Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/f9/93/45c1cdcbeb182ccd2e144c693eaa097763b08b38cded279f0053ed53c553/pycryptodomex-3.23.0-cp37-abi3-win_arm64.whl", hash = "sha256:02d87b80778c171445d67e23d1caef279bf4b25c3597050ccd2e13970b57fd51", size = 1707161, upload-time = "2025-05-17T17:23:11.414Z" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/5f/5d/5f6c63eebb5afee93bcaae4ce9a898f3373ca23df3ccaef086d0233a35a7/pydantic_core-2.41.5-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:f41a7489d32336dbf2199c8c0a215390a751c5b014c2c1c5366e817202e9cdf7", size = 2110990, upload-time = "2025-11-04T13:39:58.079Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/aa/32/9c2e8ccb57c01111e0fd091f236c7b371c1bccea0fa85247ac55b1e2b6b6/pydantic_core-2.41.5-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:070259a8818988b9a84a449a2a7337c7f430a22acc0859c6b110aa7212a6d9c0", size = 1896003, upload-time = "2025-11-04T13:39:59.956Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/68/b8/a01b53cb0e59139fbc9e4fda3e9724ede8de279097179be4ff31f1abb65a/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e96cea19e34778f8d59fe40775a7a574d95816eb150850a85a7a4c8f4b94ac69", size = 1919200, upload-time = "2025-11-04T13:40:02.241Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/38/de/8c36b5198a29bdaade07b5985e80a233a5ac27137846f3bc2d3b40a47360/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ed2e99c456e3fadd05c991f8f437ef902e00eedf34320ba2b0842bd1c3ca3a75", size = 2052578, upload-time = "2025-11-04T13:40:04.401Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/00/b5/0e8e4b5b081eac6cb3dbb7e60a65907549a1ce035a724368c330112adfdd/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:65840751b72fbfd82c3c640cff9284545342a4f1eb1586ad0636955b261b0b05", size = 2208504, upload-time = "2025-11-04T13:40:06.072Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/77/56/87a61aad59c7c5b9dc8caad5a41a5545cba3810c3e828708b3d7404f6cef/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e536c98a7626a98feb2d3eaf75944ef6f3dbee447e1f841eae16f2f0a72d8ddc", size = 2335816, upload-time = "2025-11-04T13:40:07.835Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/0d/76/941cc9f73529988688a665a5c0ecff1112b3d95ab48f81db5f7606f522d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eceb81a8d74f9267ef4081e246ffd6d129da5d87e37a77c9bde550cb04870c1c", size = 2075366, upload-time = "2025-11-04T13:40:09.804Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/d3/43/ebef01f69baa07a482844faaa0a591bad1ef129253ffd0cdaa9d8a7f72d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d38548150c39b74aeeb0ce8ee1d8e82696f4a4e16ddc6de7b1d8823f7de4b9b5", size = 2171698, upload-time = "2025-11-04T13:40:12.004Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/b1/87/41f3202e4193e3bacfc2c065fab7706ebe81af46a83d3e27605029c1f5a6/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:c23e27686783f60290e36827f9c626e63154b82b116d7fe9adba1fda36da706c", size = 2132603, upload-time = "2025-11-04T13:40:13.868Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/49/7d/4c00df99cb12070b6bccdef4a195255e6020a550d572768d92cc54dba91a/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:482c982f814460eabe1d3bb0adfdc583387bd4691ef00b90575ca0d2b6fe2294", size = 2329591, upload-time = "2025-11-04T13:40:15.672Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/cc/6a/ebf4b1d65d458f3cda6a7335d141305dfa19bdc61140a884d165a8a1bbc7/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:bfea2a5f0b4d8d43adf9d7b8bf019fb46fdd10a2e5cde477fbcb9d1fa08c68e1", size = 2319068, upload-time = "2025-11-04T13:40:17.532Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/49/3b/774f2b5cd4192d5ab75870ce4381fd89cf218af999515baf07e7206753f0/pydantic_core-2.41.5-cp312-cp312-win32.whl", hash = "sha256:b74557b16e390ec12dca509bce9264c3bbd128f8a2c376eaa68003d7f327276d", size = 1985908, upload-time = "2025-11-04T13:40:19.309Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/86/45/00173a033c801cacf67c190fef088789394feaf88a98a7035b0e40d53dc9/pydantic_core-2.41.5-cp312-cp312-win_amd64.whl", hash = "sha256:1962293292865bca8e54702b08a4f26da73adc83dd1fcf26fbc875b35d81c815", size = 2020145, upload-time = "2025-11-04T13:40:21.548Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/f9/22/91fbc821fa6d261b376a3f73809f907cec5ca6025642c463d3488aad22fb/pydantic_core-2.41.5-cp312-cp312-win_arm64.whl", hash = "sha256:1746d4a3d9a794cacae06a5eaaccb4b8643a131d45fbc9af23e353dc0a5ba5c3", size = 1976179, upload-time = "2025-11-04T13:40:23.393Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/09/32/59b0c7e63e277fa7911c2fc70ccfb45ce4b98991e7ef37110663437005af/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:7da7087d756b19037bc2c06edc6c170eeef3c3bafcb8f532ff17d64dc427adfd", size = 2110495, upload-time = "2025-11-04T13:42:49.689Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/aa/81/05e400037eaf55ad400bcd318c05bb345b57e708887f07ddb2d20e3f0e98/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:aabf5777b5c8ca26f7824cb4a120a740c9588ed58df9b2d196ce92fba42ff8dc", size = 1915388, upload-time = "2025-11-04T13:42:52.215Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/6e/0d/e3549b2399f71d56476b77dbf3cf8937cec5cd70536bdc0e374a421d0599/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c007fe8a43d43b3969e8469004e9845944f1a80e6acd47c150856bb87f230c56", size = 1942879, upload-time = "2025-11-04T13:42:56.483Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/f7/07/34573da085946b6a313d7c42f82f16e8920bfd730665de2d11c0c37a74b5/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:76d0819de158cd855d1cbb8fcafdf6f5cf1eb8e470abe056d5d161106e38062b", size = 2139017, upload-time = "2025-11-04T13:42:59.471Z" },
]

[[package]]
name = "pygments"
version = "2.19.2"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/b0/77/a5b8c569bf593b0140bde72ea885a803b82086995367bf2037de0159d924/pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887", size = 4968631, upload-time = "2025-06-21T13:39:12.283Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/c7/21/705964c7812476f378728bdf590ca4b771ec72385c533964653c68e86bdc/pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b", size = 1225217, upload-time = "2025-06-21T13:39:07.939Z" },
]

[[package]]
name = "pyperclip"
version = "1.11.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/e8/52/d87eba7cb129b81563019d1679026e7a112ef76855d6159d24754dbd2a51/pyperclip-1.11.0.tar.gz", hash = "sha256:244035963e4428530d9e3a6101a1ef97209c6825edab1567beac148ccc1db1b6", size = 12185, upload-time = "2025-09-26T14:40:37.245Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/df/80/fc9d01d5ed37ba4c42ca2b55b4339ae6e200b456be3a1aaddf4a9fa99b8c/pyperclip-1.11.0-py3-none-any.whl", hash = "sha256:299403e9ff44581cb9ba2ffeed69c7aa96a008622ad0c46cb575ca75b5b84273", size = 11063, upload-time = "2025-09-26T14:40:36.069Z" },
]

[[package]]
name = "pytest"
version = "9.0.2"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
    { name = "pygments" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/d1/db/7ef3487e0fb0049ddb5ce41d3a49c235bf9ad299b6a25d5780a89f19230f/pytest-9.0.2.tar.gz", hash = "sha256:75186651a92bd89611d1d9fc20f0b4345fd827c41ccd5c299a868a05d70edf11", size = 1568901, upload-time = "2025-12-06T21:30:51.014Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/3b/ab/b3226f0bd7cdcf710fbede2b3548584366da3b19b5021e74f5bde2a8fa3f/pytest-9.0.2-py3-none-any.whl", hash = "sha256:711ffd45bf766d5264d487b917733b453d917afd2b0ad65223959f59089f875b", size = 374801, upload-time = "2025-12-06T21:30:49.154Z" },
]

[[package]]
name = "rich"
version = "14.3.3"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/b3/c6/f3b320c27991c46f43ee9d856302c70dc2d0fb2dba4842ff739d5f46b393/rich-14.3.3.tar.gz", hash = "sha256:b8daa0b9e4eef54dd8cf7c86c03713f53241884e814f4e2f5fb342fe520f639b", size = 230582, upload-time = "2026-02-19T17:23:12.474Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/14/25/b208c5683343959b670dc001595f2f3737e051da617f66c31f7c4fa93abc/rich-14.3.3-py3-none-any.whl", hash = "sha256:793431c1f8619afa7d3b52b2cdec859562b950ea0d4b6b505397612db8d5362d", size = 310458, upload-time = "2026-02-19T17:23:13.732Z" },
]

[[package]]
name = "rookiepy"
version = "0.5.6"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/52/b7/b75e3bb8cdd0210a0ffb106002b678170c9a3a50ae1dc1c9bc1f701b4452/rookiepy-0.5.6.tar.gz", hash = "sha256:efa6a93b119478a96b3d8c4454215c4f1af316a24b3b3b3015b73c1c1d887078", size = 45225, upload-time = "2024-11-01T19:28:37.537Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/de/f3/70737571ed2fb7cd9e360b0ec6ce637c8894d712632f7e13b442f5286eef/rookiepy-0.5.6-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:96737f44eab781d5a010b71f7cd70ef43c6a6977dc1c54d019158b8fcfe57167", size = 1404166, upload-time = "2024-11-01T19:26:29.356Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/05/ae/9b69ca2821149cdb5061d6d3098a003affd7ca71b79166e98aed5d7beac8/rookiepy-0.5.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:37a8fc437f49672387d4a512df5522a724c4440442e64cad84680f1718f68c50", size = 1311996, upload-time = "2024-11-01T19:26:31.659Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/d7/29/3a7a44027d542c889f9605843d5c7f8df105eb0b79ad45750d7c0b18875b/rookiepy-0.5.6-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:22d0ece1ef732045f0482f72bc199cad81878154ceb62780c1e2f297c62df7e2", size = 2678772, upload-time = "2024-11-01T19:26:33.995Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/6b/62/fb0a8267604f11e7df565509834279b179eadb785e4d5e0b99cc096a27f4/rookiepy-0.5.6-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:307943d5780492c533bfeb6bc89d1a4b3e5b91b25af6fc1de280acc1e2ff16f6", size = 2583775, upload-time = "2024-11-01T19:26:36.665Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/5b/0b/c1f85445a00107f97f488f5f14ac25f1994c8436c543263e43865380e553/rookiepy-0.5.6-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c607eef14f64ba284f3754449b6eb079aa8aaa66b443d0cdd2ec9aaa1814a8da", size = 2993272, upload-time = "2024-11-01T19:26:39.668Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/4c/b4/7ca3ab1860f38e1d79df051aad6e8826732f3dee77fd694f226e20e8389c/rookiepy-0.5.6-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:19f4b95436705b38e4a55cfa9f3d999bb4edc6a7f91ba13b1b90bb14b1796fdb", size = 2871214, upload-time = "2024-11-01T19:26:42.24Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/8a/36/f45c3a833595285d790d91de20e64dff5ae1780a407033a018f0efccf852/rookiepy-0.5.6-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:95b881f2f3d93bb56808eaaf8ac9e0e5e3245dda837edab194834a3caaadcbe7", size = 2971688, upload-time = "2024-11-01T19:26:44.341Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/19/c4/59b5e0b6efcd919683578605bfac4bc112ac34de5a871094fe3efa58896b/rookiepy-0.5.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2c49a0b59bc0329928a369a479f9b1c16cbe3a2548dd8273b13515c7ced73449", size = 2801469, upload-time = "2024-11-01T19:26:47.997Z" },
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/e4/38/bba16936ece960db7ed10f8ebf05dc6228959511d3837020da1e9b7dcdf6/rookiepy-0.5.6-cp312-none-win_amd64.whl", hash = "sha256:6bb956c9f2dece5101aafc7a715bc672c5b30ddcaa55c9926d12440635d89cfc", size = 2441230, upload-time = "2024-11-01T19:26:50.486Z" },
]

[[package]]
name = "socksio"
version = "1.0.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/f8/5c/48a7d9495be3d1c651198fd99dbb6ce190e2274d0f28b9051307bdec6b85/socksio-1.0.0.tar.gz", hash = "sha256:f88beb3da5b5c38b9890469de67d0cb0f9d494b78b106ca1845f96c10b91c4ac", size = 19055, upload-time = "2020-04-17T15:50:34.664Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/37/c3/6eeb6034408dac0fa653d126c9204ade96b819c936e136c5e8a6897eee9c/socksio-1.0.0-py3-none-any.whl", hash = "sha256:95dc1f15f9b34e8d7b16f06d74b8ccf48f609af32ab33c608d08761c5dcbb1f3", size = 12763, upload-time = "2020-04-17T15:50:31.878Z" },
]

[[package]]
name = "starlette"
version = "0.50.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "anyio" },
    { name = "typing-extensions" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/ba/b8/73a0e6a6e079a9d9cfa64113d771e421640b6f679a52eeb9b32f72d871a1/starlette-0.50.0.tar.gz", hash = "sha256:a2a17b22203254bcbc2e1f926d2d55f3f9497f769416b3190768befe598fa3ca", size = 2646985, upload-time = "2025-11-01T15:25:27.516Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/d9/52/1064f510b141bd54025f9b55105e26d1fa970b9be67ad766380a3c9b74b0/starlette-0.50.0-py3-none-any.whl", hash = "sha256:9e5391843ec9b6e472eed1365a78c8098cfceb7a74bfd4d6b1c0c0095efb3bca", size = 74033, upload-time = "2025-11-01T15:25:25.461Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "uvicorn"
version = "0.42.0"
source = { registry = "https://mirrors.ustc.edu.cn/pypi/simple" }
dependencies = [
    { name = "click" },
    { name = "h11" },
]
sdist = { url = "https://mirrors.ustc.edu.cn/pypi/packages/e3/ad/4a96c425be6fb67e0621e62d86c402b4a17ab2be7f7c055d9bd2f638b9e2/uvicorn-0.42.0.tar.gz", hash = "sha256:9b1f190ce15a2dd22e7758651d9b6d12df09a13d51ba5bf4fc33c383a48e1775", size = 85393, upload-time = "2026-03-16T06:19:50.077Z" }
wheels = [
    { url = "https://mirrors.ustc.edu.cn/pypi/packages/0a/89/f8827ccff89c1586027a105e5630ff6139a64da2515e24dafe860bd9ae4d/uvicorn-0.42.0-py3-none-any.whl", hash = "sha256:96c30f5c7abe6f74ae8900a70e92b85ad6613b745d4879eb9b16ccad15645359", size = 68830, upload-time = "2026-03-16T06:19:48.325Z" },
]
```

## File: `docs/Cookie获取教程.md`
```markdown
# Cookie 获取教程

本教程仅演示部分能够获取所需 `Cookie` 的方法，仍有其他方法能够获取所需 `Cookie`；本教程使用的浏览器为 `Microsoft Edge`
，部分浏览器的开发人员工具可能不支持中文语言。

**方法一\(推荐\)：**

1. 打开浏览器\(可选无痕模式启动\)，访问`https://www.douyin.com/`
2. 登录抖音账号\(可跳过\)
3. 按 `F12` 打开开发人员工具
4. 选择 `网络` 选项卡
5. 勾选 `保留日志`
6. 在 `筛选器` 输入框输入 `cookie-name:odin_tt`
7. 点击加载任意一个作品的评论区
8. 在开发人员工具窗口选择任意一个数据包\(如果无数据包，重复步骤7\)
9. 全选并复制 `Cookie` 的值
10. 运行 `main.py` ，根据提示写入 `Cookie`

**截图示例：**

<img src="screenshot/Cookie获取教程1.png" alt="开发人员工具">

**方法二\(不适用本项目\)：**

1. 打开浏览器\(可选无痕模式启动\)，访问`https://www.douyin.com/`
2. 登录抖音账号\(可跳过\)
3. 按 `F12` 打开开发人员工具
4. 选择 `控制台` 选项卡
5. 输入 `document.cookie` 后回车确认
6. 检查 `Cookie` 是否包含 `passport_csrf_token` 和 `odin_tt` 字段
7. 如果未包含所需字段，尝试刷新网页或者点击加载任意一个作品的评论区，回到步骤5
8. 全选并复制 `Cookie` 的值
9. 运行 `main.py` ，根据提示写入 `Cookie`

**截图示例：**

<img src="screenshot/Cookie获取教程2.png" alt="开发人员工具">

# device_id 参数

`device_id` 参数获取方法与 Cookie 类似。

<img src="screenshot/device_id获取示例图.png" alt="开发人员工具">
```

## File: `docs/DouK-Downloader文档.md`
```markdown
<div align="center">
<img src="https://github.com/JoeanAmier/TikTokDownloader/blob/master/static/images/DouK-Downloader.png" alt="DouK-Downloader" height="256" width="256"><br>
<h1>DouK-Downloader 项目文档</h1>
<a href="https://trendshift.io/repositories/6222" target="_blank"><img src="https://trendshift.io/api/badge/repositories/6222" alt="" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<br>
<img alt="GitHub" src="https://img.shields.io/github/license/JoeanAmier/TikTokDownloader?style=flat-square">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/JoeanAmier/TikTokDownloader?style=flat-square&color=55efc4">
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/JoeanAmier/TikTokDownloader?style=flat-square&color=fda7df">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/JoeanAmier/TikTokDownloader?style=flat-square&color=a29bfe">
<br>
<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.12-b8e994?style=flat-square&logo=python&labelColor=3dc1d3">
<img alt="GitHub release (with filter)" src="https://img.shields.io/github/v/release/JoeanAmier/TikTokDownloader?style=flat-square&color=48dbfb">
<img src="https://img.shields.io/badge/Sourcery-enabled-884898?style=flat-square&color=1890ff" alt="">
<img alt="Static Badge" src="https://img.shields.io/badge/Docker-badc58?style=flat-square&logo=docker">
<img alt="GitHub all releases" src="https://img.shields.io/github/downloads/JoeanAmier/TikTokDownloader/total?style=flat-square&color=ffdd59">
</div>
<br>
<p>🔥 <b>TikTok 发布/喜欢/合辑/直播/视频/图集/音乐；抖音发布/喜欢/收藏/收藏夹/视频/图集/实况/直播/音乐/合集/评论/账号/搜索/热榜数据采集工具：</b>完全开源，基于 HTTPX 模块实现的免费数据采集和文件下载工具；批量下载抖音账号发布、喜欢、收藏、收藏夹作品；批量下载 TikTok 账号发布、喜欢作品；下载抖音链接或 TikTok 链接作品；获取抖音直播拉流地址；下载抖音直播视频；获取 TikTok 直播拉流地址；下载 TikTok 直播视频；采集抖音作品评论数据；批量下载抖音合集作品；批量下载 TikTok 合辑作品；采集抖音账号详细数据；采集抖音用户 / 作品 / 直播搜索结果；采集抖音热榜数据。</p>
<p>⭐ <b>项目版本：<code>5.8 Beta</code>；文档更新日期：<code>2026/2/28</code></b></p>
<p>⭐ <b>项目文档正在完善，如果发现任何错误或描述模糊之处，请告知作者以便改进！本项目历史名称：<code>TikTokDownloader</code></b></p>
<p>⭐ Due to the author’s limited time and energy, the complete English documentation for this project is not yet available. If you wish to read the full documentation, we recommend using AI translation tools to assist your understanding. If you would like to contribute to the translation, your help is warmly welcomed.</p>
<hr>
<h1>快速入门</h1>
<p>⭐ 本项目包含手动构建可执行文件的 GitHub Actions，使用者可以随时使用 GitHub Actions 将最新源码构建为可执行文件！</p>
<p>⭐ 自动构建可执行文件教程请查阅本文档的 <code>构建可执行文件指南</code> 部分；如果需要更加详细的图文教程，请 <a href="https://mp.weixin.qq.com/s/TorfoZKkf4-x8IBNLImNuw">查阅文章</a>！</p>
<p><strong>注意：由于 Mac OS 平台的可执行文件 <code>main</code> 未经过代码签名，首次运行时会受到系统安全限制。请先在终端执行 <code>xattr -cr main.app</code> 命令移除安全标记，执行一次后即可正常运行。</strong></p>
<ol>
<li><b>运行可执行文件</b> 或者 <b>配置环境运行</b>
<ol><b>运行可执行文件</b>
<li>下载 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 或者 Actions 构建的可执行文件压缩包</li>
<li>解压后打开程序文件夹，双击运行 <code>main</code></li>
</ol>
<ol><b>配置环境运行</b>

[//]: # (<li>安装不低于 <code>3.12</code> 版本的 <a href="https://www.python.org/">Python</a> 解释器</li>)
<li>安装 <code>3.12</code> 版本的 <a href="https://www.python.org/">Python</a> 解释器</li>
<li>下载最新的源码或 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 发布的源码至本地</li>
<li>运行 <code>python -m venv venv</code> 命令创建虚拟环境（可选）</li>
<li>运行 <code>.\venv\Scripts\activate.ps1</code> 或者 <code>venv\Scripts\activate</code> 命令激活虚拟环境（可选）</li>
<li>运行 <code>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt</code> 命令安装程序所需模块</li>
<li>运行 <code>python .\main.py</code> 或者 <code>python main.py</code> 命令启动 DouK-Downloader</li>
</ol>
</li>
<li>阅读 DouK-Downloader 的免责声明，根据提示输入内容</li>
<li>将 Cookie 信息写入配置文件
<ol><b>从剪贴板读取 Cookie（推荐）</b>
<li>参考 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 提取教程</a>，复制所需 Cookie 至剪贴板</li>
<li>选择 <code>从剪贴板读取 Cookie</code> 选项，程序会自动读取剪贴板的 Cookie 并写入配置文件</li>
</ol>
<ol><b>从浏览器读取 Cookie</b>
<li>选择 <code>从浏览器读取 Cookie</code> 选项，按照提示输入浏览器类型或序号</li>
</ol>
<ol><b><del>扫码登录获取 Cookie</del>（失效）</b>
<li><del>选择 <code>扫码登录获取 Cookie</code> 选项，程序会显示登录二维码图片，并使用默认应用打开图片</del></li>
<li><del>使用抖音 APP 扫描二维码并登录账号</del></li>
<li><del>按照提示操作，程序会自动将 Cookie 写入配置文件</del></li>
</ol>
</li>
<li>返回程序界面，依次选择 <code>终端交互模式</code> -> <code>批量下载链接作品(抖音)</code> -> <code>手动输入待采集的作品链接</code></li>
<li>输入抖音作品链接即可下载作品文件</li>
</ol>
<p><b>TikTok 平台功能需要额外设置配置文件 <code>browser_info_tiktok</code> 的 <code>device_id</code> 参数，否则 TikTok 平台功能可能无法正常使用！参数获取方式与 Cookie 类似，详见 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 获取教程</a></b></p>
<h2>Docker 容器</h2>
<ol>
<li>获取镜像</li>
<ul>
<li>方式一：使用 <code>Dockerfile</code> 文件构建镜像</li>
<li>方式二：使用 <code>docker pull joeanamier/tiktok-downloader</code> 命令拉取镜像</li>
<li>方式三：使用 <code>docker pull ghcr.io/joeanamier/tiktok-downloader</code> 命令拉取镜像</li>
</ul>
<li>创建容器：<code>docker run --name 容器名称(可选) -p 主机端口号:5555 -v tiktok_downloader_volume:/app/Volume -it &lt;镜像名称&gt;</code>
</li>
<br><b>注意：</b>此处的 <code>&lt;镜像名称&gt;</code> 需与您在第一步中使用的镜像名称保持一致（例如 <code>joeanamier/tiktok-downloader</code> 或 <code>ghcr.io/joeanamier/tiktok-downloader</code>）
<li>运行容器
<ul>
<li>启动容器：<code>docker start -i 容器名称/容器 ID</code></li>
<li>重启容器：<code>docker restart -i 容器名称/容器 ID</code></li>
</ul>
</li>
</ol>
<p>Docker 容器无法直接访问宿主机的文件系统，部分功能不可用，例如：<code>从浏览器读取 Cookie</code>；其他功能如有异常请反馈！</p>
<h1>Cookie 说明</h1>
<p><a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">点击查看 Cookie 获取教程</a>；无效或失效的 Cookie 会导致程序获取数据失败！</p>
<ul>
<li>Cookie 仅需在失效后重新写入配置文件，并非每次运行程序都要写入配置文件！</li>
<li><p>Cookie 会影响下载的视频文件分辨率，如果无法下载最高分辨率的视频文件，请尝试更新 Cookie！</li>
<li>程序获取数据失败时，可以尝试更新 Cookie 或者使用已登录的 Cookie！</li>
</ul>
<h1>入门说明</h1>
<h2>关于终端</h2>
<p>⭐ 推荐使用 <a href="https://learn.microsoft.com/zh-cn/windows/terminal/install">Windows 终端</a>（Windows 11 自带默认终端）运行程序以便获得最佳彩色交互显示效果！</p>
<h2>链接类型</h2>
<ul>
<li>完整链接：使用浏览器打开抖音或 TikTok 链接时，地址栏所显示的 URL 地址。</li>
<li>分享链接：点击 APP 或网页版的分享按钮得到的 URL 地址，抖音平台以 <code>https://v.</code> 开头，掺杂中文和其他字符；TikTok
平台以 <code>https://vm.</code> 或 <code>https://vt.</code> 开头，不掺杂其他字符；使用时<b>不需要</b>手动去除中文和其他字符，程序会自动提取 URL 链接。</li>
</ul>
<h2>数据储存</h2>
<ul>
<li>项目支持使用 <code>CSV</code>、<code>XLSX</code>、<code>SQLite</code> 格式文件储存采集数据。</li>
<li>配置文件 <code>settings.json</code> 的 <code>storage_format</code> 参数可设置数据储存格式类型，如果不设置该参数，程序不会储存任何数据至文件。</li>
<li><code>采集作品评论数据</code>、<code>采集账号详细数据</code>、<code>采集搜索结果数据</code>、<code>采集抖音热榜数据</code> 模式必须设置 <code>storage_format</code> 参数才能正常使用。</li>
<li>程序所有数据均储存至配置文件 <code>root</code> 参数路径下的 <code>Data</code> 文件夹。</li>
</ul>
<h2>文本文档</h2>
<p>项目部分功能支持从文本文档（TXT）读取链接，如需使用，请在计算机任意路径创建一个空白文本文档，然后编辑文件内容，每行输入单个链接，编辑完成后保存文件。</p>
<p>文本文档编码：UTF-8</p>
<h3>文本文档内容示例</h3>

```text
https://www.douyin.com/user/abcd?vid=123456789
https://www.douyin.com/search/key?modal_id=123456789
https://www.douyin.com/video/123456789
https://www.douyin.com/note/123456789
```

<h2>直播下载</h2>
<p><code>获取直播拉流地址</code> 功能需要调用 <code>ffmpeg</code> 下载直播文件；程序会优先调用系统环境的 <code>ffmpeg</code>，其次调用 <code>ffmpeg</code> 参数指定的 <code>ffmpeg</code>，如果 <code>ffmpeg</code> 不可用，程序将不支持直播下载！</p>
<p>建议前往 <a href="https://ffmpeg.org/download.html">官方网站</a> 或者 <a href="https://github.com/BtbN/FFmpeg-Builds">FFmpeg-Builds</a> 获取 <code>ffmpeg</code> 程序！</p>
<p>项目开发时所用的 FFmpeg 版本信息如下，不同版本的 FFmpeg 可能会有差异；若功能异常，请向作者反馈！</p>
<pre>
ffmpeg version n7.1.1-6-g48c0f071d4-20250405 Copyright (c) 2000-2025 the FFmpeg developers
built with gcc 14.2.0 (crosstool-NG 1.27.0.18_7458341)
</pre>
<h2>功能汇总</h2>
<table>
<thead>
<tr>
<th align="center">程序功能</th>
<th align="center">功能类型</th>
</tr>
</thead>
<tbody><tr>
<td align="center">批量下载账号作品（发布、喜欢）</td>
<td align="center">文件下载, 数据采集</td>
</tr>
<tr>
<td align="center">批量下载链接作品</td>
<td align="center">文件下载, 数据采集</td>
</tr>
<tr>
<td align="center">获取直播拉流地址</td>
<td align="center">文件下载, 数据采集</td>
</tr>
<tr>
<td align="center">采集作品评论数据</td>
<td align="center">数据采集</td>
</tr>
<tr>
<td align="center">批量下载合集作品</td>
<td align="center">文件下载, 数据采集</td>
</tr>
<tr>
<td align="center">采集账号详细数据</td>
<td align="center">数据采集</td>
</tr>
<tr>
<td align="center">采集搜索结果数据</td>
<td align="center">数据采集</td>
</tr>
<tr>
<td align="center">采集抖音热榜数据</td>
<td align="center">数据采集</td>
</tr>
<tr>
<td align="center">批量下载收藏作品</td>
<td align="center">文件下载，数据采集</td>
</tr>
<tr>
<td align="center">批量下载收藏夹作品</td>
<td align="center">文件下载，数据采集</td>
</tr>
<tr>
<td align="center">批量下载收藏音乐作品</td>
<td align="center">文件下载，数据采集</td>
</tr>
</tbody></table>
<h2>关闭平台功能</h2>
<p>本项目支持抖音平台和 TikTok 平台的数据采集和文件下载功能，平台功能默认开启，如果不需要使用平台的任何功能，可以编辑配置文件关闭平台功能。</p>
<p>本项目内置参数更新机制，程序会周期性更新抖音与 TikTok 请求的部分参数，以保持参数的有效性（或许没有效果？），该功能无法防止参数失效，参数失效后需要重新写入 Cookie；关闭平台功能后，对应平台的参数更新功能将会禁用！</p>
<h1>配置文件</h1>
<p>配置文件：项目根目录下的 <code>./Volume/settings.json</code> 文件，可以自定义设置程序部分运行参数。</p>
<p>若无特殊需求，大部分配置参数无需修改，直接使用默认值即可。</p>
<p><b><code>cookie</code>、<code>cookie_tiktok</code> 与 <code>device_id</code>参数为必需参数，必须设置该参数才能正常使用程序</b>；其余参数可以根据实际需求进行修改！</p>
<p>如果您的计算机没有合适的程序编辑 JSON 文件，建议使用 <a href="https://www.toolhelper.cn/JSON/JSONFormat">在线工具</a> 编辑配置文件内容，修改后需要重启软件才能生效。</p>
<p>注意: 手动修改 <code>settings.json</code> 后需要重新运行程序才会生效！</p>
<h2>参数说明</h2>
<table>
<thead>
<tr>
<th align="center">参数</th>
<th align="center">类型</th>
<th align="center">说明</th>
<th align="center">默认</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><i>mark</i></td>
<td align="center">str</td>
<td align="center"><a href="#mark"><sup>1</sup></a>账号/合集标识，用于区分账号/合集；<strong>属于 accounts_urls、mix_urls 和 owner_url 子参数</strong></td>
<td align="center">账号昵称/合集标题</td>
</tr>
<tr>
<td align="center"><i>url</i></td>
<td align="center">str</td>
<td align="center">账号主页/合集作品链接；<strong>属于 accounts_urls、mix_urls 和 owner_url 子参数</strong></td>
<td align="center">无</td>
</tr>
<tr>
<td align="center"><i>tab</i></td>
<td align="center">str</td>
<td align="center"><a href="#supplement"><sup>2</sup></a>主页标签，<code>post</code> 代表发布作品、<code>favorite</code> 代表喜欢作品；<strong>属于 accounts_urls 子参数</strong></td>
<td align="center">发布作品</td>
</tr>
<tr>
<td align="center"><i>earliest</i></td>
<td align="center">str | float | int</td>
<td align="center">作品最早发布日期，格式：<code>2023/1/1</code>、<code>整数</code>、<code>浮点数</code>；设置为数值代表基于 <code>latest</code>参数的前 XX 天，<strong>属于 accounts_urls 子参数</strong></td>
<td align="center">不限制</td>
</tr>
<tr>
<td align="center"><i>latest</i></td>
<td align="center">str | float | int</td>
<td align="center">作品最晚发布日期，格式：<code>2023/1/1</code>、<code>整数</code>、<code>浮点数</code>；设置为数值代表基于当天的前 XX 天，<strong>属于 accounts_urls 子参数</strong></td>
<td align="center">不限制</td>
</tr>
<tr>
<td align="center"><i>enable</i></td>
<td align="center">bool</td>
<td align="center">参数对象是否启用，设置为 <code>false</code> 时程序会跳过处理；<strong>属于 accounts_urls 和 mix_urls 子参数</strong></td>
<td align="center">启用</td>
</tr>
<tr>
<td align="center">accounts_urls[mark, url, tab, earliest, latest, enable]</td>
<td align="center">list[dict[str, str, str, Any, str, bool]]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>抖音平台：账号标识，账号链接，主页标签，最早发布日期，最晚发布日期，是否启用；作为 <code>批量下载账号作品</code> 模式选项，支持多账号，以字典格式包含六个参数</td>
<td align="center">无</td>
<tr>
<td align="center">mix_urls[mark, url, enable]</td>
<td align="center">list[dict[str, str, bool]]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>抖音平台：合集标识，合集链接或作品链接，是否启用；作为 <code>批量下载合集作品</code> 模式选项，支持多合集，以字典格式包含三个参数</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">owner_url[mark, url]</td>
<td align="center">dict[str, str]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>抖音平台：当前登录 Cookie 的账号标识，账号主页链接；<code>批量下载收藏作品</code> 模式下用于获取账号信息，以字典格式包含两个参数</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">accounts_urls_tiktok[mark, url, tab, earliest, latest, enable]</td>
<td align="center">list[dict[str, str, str, Any, str, bool]]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>TikTok 平台；参数规则与 <code>accounts_urls</code> 一致</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">mix_urls_tiktok[mark, url, enable]</td>
<td align="center">list[dict[str, str, bool]]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>TikTok 平台；参数规则与 <code>mix_urls</code> 一致</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">owner_url_tiktok[mark, url](未生效)</td>
<td align="center">dict[str, str]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>TikTok 平台；参数规则与 <code>owner_url</code> 一致</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">root</td>
<td align="center">str</td>
<td align="center">作品文件和数据记录保存路径；建议使用绝对路径</td>
<td align="center">项目根路径/Volume</td>
</tr>
<tr>
<td align="center">folder_name</td>
<td align="center">str</td>
<td align="center">批量下载链接作品时，保存文件夹的名称</td>
<td align="center">Download</td>
</tr>
<tr>
<td align="center">name_format</td>
<td align="center">str</td>
<td align="center">文件保存时的命名规则，值之间使用空格分隔，支持：<code>id</code>：作品 ID；<code>desc</code>：作品描述；<code>create_time</code>：发布时间；<code>nickname</code>：账号昵称；<code>mark</code>：账号标识；<code>uid</code>：账号 ID；<code>type</code>：作品类型</td>
<td align="center">发布时间-作品类型-账号昵称-描述</td>
</tr>
<tr>
<td align="center">desc_length</td>
<td align="center">int</td>
<td align="center">作品文件名中描述字段的最大字符数；超过限制的描述字段将折叠处理</td>
<td align="center">64</td>
</tr>
<tr>
<td align="center">name_length</td>
<td align="center">int</td>
<td align="center">作品文件名称的最大字符数；超过限制的文件名称将折叠处理</td>
<td align="center">128</td>
</tr>
<tr>
<td align="center">date_format</td>
<td align="center">str</td>
<td align="center">日期时间格式；<a href="https://docs.python.org/zh-cn/3/library/time.html?highlight=strftime#time.strftime">点击查看设置规则</a></td>
<td align="center">年-月-日 时:分:秒</td>
</tr>
<tr>
<td align="center">split</td>
<td align="center">str</td>
<td align="center">文件命名的分隔符</td>
<td align="center">-</td>
</tr>
<tr>
<td align="center">folder_mode</td>
<td align="center">bool</td>
<td align="center">是否将每个作品的文件储存至单独的文件夹，文件夹名称格式与 <code>name_format</code> 参数一致</td>
<td align="center">false</td>
</tr>
<tr>
<td align="center">music</td>
<td align="center">bool</td>
<td align="center">是否下载作品音乐</td>
<td align="center">false</td>
</tr>
<tr>
<td align="center">truncate</td>
<td align="center">int</td>
<td align="center">文件下载进度条中描述字符串的最大长度，该参数用于调整显示效果</td>
<td align="center">64</td>
</tr>
<tr>
<td align="center">storage_format</td>
<td align="center">str</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>采集数据持久化储存格式，支持：<code>csv</code>、<code>xlsx</code>、<code>sql</code>(SQLite)</td>
<td align="center">不保存</td>
</tr>
<tr>
<td align="center">cookie</td>
<td align="center">dict | str</td>
<td align="center"><a href="#supplement"><sup>4</sup></a>抖音网页版 Cookie, 必需参数; 建议通过程序写入配置文件，亦可手动编辑</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">cookie_tiktok</td>
<td align="center">dict | str</td>
<td align="center"><a href="#supplement"><sup>4</sup></a>TikTok 网页版 Cookie, 必需参数; 建议通过程序写入配置文件，亦可手动编辑</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">dynamic_cover</td>
<td align="center">bool</td>
<td align="center">是否下载视频作品动态封面图</td>
<td align="center">false</td>
</tr>
<tr>
<td align="center">static_cover</td>
<td align="center">bool</td>
<td align="center">是否下载视频作品静态封面图</td>
<td align="center">false</td>
</tr>
<tr>
<td align="center">proxy</td>
<td align="center">str</td>
<td align="center">抖音请求代理地址</td>
<td align="center">不使用代理</td>
</tr>
<tr>
<td align="center">proxy_tiktok</td>
<td align="center">str</td>
<td align="center">TikTok 请求代理地址</td>
<td align="center">不使用代理</td>
</tr>
<tr>
<td align="center"><a href="#twc">twc_tiktok</a></td>
<td align="center">str</td>
<td align="center">TikTok Cookie 的 ttwid 值，一般情况下无需设置</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">download</td>
<td align="center">bool</td>
<td align="center">是否开启项目的下载功能，如果关闭，程序将不会下载任何文件</td>
<td align="center">true</td>
</tr>
<tr>
<td align="center">max_size</td>
<td align="center">int</td>
<td align="center">作品文件大小限制，单位字节，超出大小限制的作品文件将会跳过下载</td>
<td align="center">无限制</td>
</tr>
<tr>
<td align="center">chunk</td>
<td align="center">int</td>
<td align="center">每次从服务器接收的数据块大小，单位字节</td>
<td align="center">2097152(2 MB)</td>
</tr>
<tr>
<td align="center">timeout</td>
<td align="center">int</td>
<td align="center">请求数据的超时限制，单位秒</td>
<td align="center">10</td>
</tr>
<tr>
<td align="center">max_retry</td>
<td align="center">int</td>
<td align="center">发送请求获取数据发生异常时重试的最大次数，设置为 <code>0</code> 代表关闭重试</td>
<td align="center">10</td>
</tr>
<tr>
<td align="center">max_pages</td>
<td align="center">int</td>
<td align="center">批量下载账号喜欢作品、收藏作品或者采集作品评论数据时，请求数据的最大次数（不包括异常重试）</td>
<td align="center">不限制</td>
</tr>
<tr>
<td align="center">run_command</td>
<td align="center">str</td>
<td align="center">设置程序启动执行的默认命令，相当于模拟用户输入序号或内容（多个序号或内容之间使用空格分隔）</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">ffmpeg</td>
<td align="center">str</td>
<td align="center"><a href="#supplement"><sup>3</sup></a><code>ffmpeg.exe</code> 路径，下载直播时使用，如果系统环境存在 <code>ffmpeg</code> 或者不想使用 <code>ffmpeg</code>，无需设置该参数</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">live_qualities</td>
<td align="center">str</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>下载直播时的默认清晰度，支持设置为清晰度或者序号；当设置了该参数时，获取直播拉流地址将会直接下载指定清晰度的直播文件，不再提示输入清晰度；参数示例：<code>FULL_HD1</code>、<code>HD1</code>、<code>1</code>、<code>2</code> 等</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">douyin_platform</td>
<td align="center">bool</td>
<td align="center"><a href="#supplement"><sup>5</sup></a>是否启用抖音平台功能</td>
<td align="center">true</td>
</tr>
<tr>
<td align="center">tiktok_platform</td>
<td align="center">bool</td>
<td align="center"><a href="#supplement"><sup>5</sup></a>是否启用 TikTok 平台功能</td>
<td align="center">true</td>
</tr>
<tr>
<td align="center">browser_info</td>
<td align="center">dict</td>
<td align="center">抖音平台浏览器信息，一般情况下无需修改</td>
<td align="center">内置参数</td>
</tr>
<tr>
<td align="center">browser_info_tiktok</td>
<td align="center">dict</td>
<td align="center">TikTok 平台浏览器信息，一般情况下仅需修改 <code>device_id</code> 参数，获取方式查阅 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 获取教程</a></td>
<td align="center">内置参数</td>
</tr>
</tbody>
</table>
<div id="supplement">
<p><strong>补充说明：</strong></p>
<ol>
<li><a href="#mark">详见标识参数说明</a></li>
<li>设置为 <code>favorite</code> 时，需要确保账号喜欢作品公开可见，或者配置对应账号的登录 Cookie</li>
<li>该参数仅在部分模式和功能中生效，如果不需要使用相应的模式和功能，无需设置该参数</li>
<li>必须设置平台的 Cookie 才能使用该平台的数据采集和文件下载功能</li>
<li>如果不需要使用该平台的任何功能，可以将该参数设置为 <code>false</code></li>
</ol>
</div>
<h2>配置示例</h2>

```json
{
  "accounts_urls": [
    {
      "mark": "账号A",
      "url": "https://www.douyin.com/user/aaa",
      "tab": "post",
      "earliest": "2024/3/1",
      "latest": "2024/7/1",
      "enable": true
    },
    {
      "mark": "账号B",
      "url": "https://v.douyin.com/bbb",
      "tab": "favorite",
      "earliest": 30,
      "latest": "",
      "enable": false
    }
  ],
  "accounts_urls_tiktok": "参数规则与 accounts_urls 一致",
  "mix_urls": [
    {
      "mark": "",
      "url": "https://v.douyin.com/ccc",
      "enable": true
    },
    {
      "mark": "合集B",
      "url": "https://www.douyin.com/video/123",
      "enable": false
    }
  ],
  "mix_urls_tiktok": "参数规则与 mix_urls 一致",
  "owner_url": {
    "mark": "已登录 Cookie 的账号标识，可以设置为空字符串",
    "url": "已登录 Cookie 的账号主页链接"
  },
  "owner_url_tiktok": "参数规则与 owner_url 一致",
  "root": "C:\\DouK-Downloader",
  "folder_name": "SOLO",
  "name_format": "create_time uid id",
  "desc_length": 64,
  "name_length": 128,
  "date_format": "%Y-%m-%d",
  "split": " ",
  "folder_mode": false,
  "music": false,
  "truncate": 32,
  "storage_format": "xlsx",
  "cookie": {
    "key-1": "value-1",
    "key-2": "value-2",
    "key-3": "value-3"
  },
  "cookie_tiktok": "参数规则与 cookie 一致",
  "dynamic_cover": false,
  "static_cover": false,
  "proxy": "http://127.0.0.1:9999",
  "proxy_tiktok": "参数规则与 proxy 一致",
  "twc_tiktok": "",
  "download": true,
  "max_size": 104857600,
  "chunk": 10485760,
  "timeout": 5,
  "max_retry": 10,
  "max_pages": 2,
  "run_command": "6 2 1",
  "ffmpeg": "C:\\DouK-Downloader\\ffmpeg.exe",
  "live_qualities": "1",
  "douyin_platform": true,
  "tiktok_platform": true,
  "browser_info": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "pc_libra_divert": "Windows",
    "browser_language": "zh-SG",
    "browser_platform": "Win32",
    "browser_name": "Chrome",
    "browser_version": "139.0.0.0",
    "engine_name": "Blink",
    "engine_version": "139.0.0.0",
    "os_name": "Windows",
    "os_version": "10",
    "webid": ""
  },
  "browser_info_tiktok": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "app_language": "zh-Hans",
    "browser_language": "zh-SG",
    "browser_name": "Mozilla",
    "browser_platform": "Win32",
    "browser_version": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "language": "zh-Hans",
    "os": "windows",
    "priority_region": "CN",
    "region": "US",
    "tz_name": "Asia/Shanghai",
    "webcast_language": "zh-Hans",
    "device_id": "0123456789"
  }
}
```

<h2>参数详解</h2>
<h3>下载喜欢作品</h3>

```json
{
  "accounts_urls": [
    {
      "mark": "",
      "url": "https://www.douyin.com/user/aaa",
      "tab": "favorite",
      "earliest": "",
      "latest": "",
      "enable": true
    },
    {
      "mark": "",
      "url": "https://v.douyin.com/bbb",
      "tab": "post",
      "earliest": "",
      "latest": "",
      "enable": true
    },
    {
      "mark": "",
      "url": "https://www.douyin.com/user/ccc",
      "tab": "favorite",
      "earliest": "",
      "latest": "",
      "enable": false
    }
  ]
}
```

<p>将待下载的账号信息写入配置文件，每个账号对应一个对象/字典，<code>tab</code> 参数设置为 <code>favorite</code> 代表批量下载喜欢作品，支持多账号；<code>accounts_urls_tiktok</code>参数规则一致。</p>
<p>下载账号喜欢作品需要确保账号喜欢作品公开可见，或者配置对应账号的登录 Cookie！</p>
<p><b>下载账号喜欢作品需要使用已登录的 Cookie，否则可能无法获取正确的账号信息！</b></p>
<h3>发布日期限制</h3>

```json
{
  "accounts_urls": [
    {
      "mark": "账号A",
      "url": "https://v.douyin.com/aaa",
      "tab": "post",
      "earliest": "2023/12/1",
      "latest": "",
      "enable": true
    },
    {
      "mark": "",
      "url": "https://v.douyin.com/bbb",
      "tab": "post",
      "earliest": 30,
      "latest": "2024/12/1",
      "enable": true
    }
  ]
}
```

<p>如果已经采集某账号的全部发布作品，建议设置 <code>earliest</code> 和 <code>latest</code> 参数以减少后续采集请求次数，提高程序运行效率；<code>accounts_urls_tiktok</code>参数规则一致。</p>
<p>示例：将 <code>earliest</code> 参数设置为 <code>2023/12/1</code>，程序获取账号发布作品数据时，不会获取早于 <code>2023/12/1</code> 的作品数据。</p>
<p>示例：将 <code>earliest</code> 参数设置为 <code>30</code>，<code>latest</code> 参数设置为 <code>2024/12/1</code>，程序获取账号发布作品数据时，仅获取 2024 年 12 月 1 日当天及之前 30 天内发布的作品数据。</p>
<p>示例：将 <code>earliest</code> 参数设置为 <code>15</code>，<code>latest</code> 参数设置为 <code>5</code>，程序获取账号发布作品数据时，仅获取前 5 天 ~ 前 20 天之间发布的作品数据。</p>
<h3>文件储存路径</h3>

```json
{
  "root": "C:\\DouK-Downloader",
  "folder_name": "SOLO"
}
```

<p>程序会将账号作品和合集作品的文件 和 记录的数据储存至 <code>C:\DouK-Downloader</code> 文件夹内，链接作品的文件会储存至 <code>C:\DouK-Downloader\SOLO</code> 文件夹内。</p>
<h3>文件名称格式</h3>

```json
{
  "name_format": "create_time uid id",
  "split": " @ "
}
```

<p>作品文件名称格式为: <code>发布时间 @ 作者UID @ 作品ID</code></p>
<ul>
<li>如果作品没有描述，文件名称的描述内容将替换为作品 ID。</li>
<li>批量下载链接作品时，如果在 <code>name_format</code> 参数中设置了 <code>mark</code> 字段，程序会自动替换为 <code>nickname</code> 字段。</li>
</ul>
<h3>日期时间格式</h3>

```json
{
  "date_format": "%Y-%m-%d"
}
```

<p>发布时间格式为：XXXX年-XX月-XX日，详细设置规则可以 <a href="https://docs.python.org/zh-cn/3/library/time.html?highlight=strftime#time.strftime">查看文档</a></p>
<h3>数据储存格式</h3>

```json
{
  "storage_format": "xlsx"
}
```

<p>使用 <code>XLSX</code> 格式储存程序采集数据。</p>
<h3>文件大小限制</h3>

```json
{
  "max_size": 104857600
}
```

<p>作品文件大小限制为 104857600 字节(100 MB)，超过该大小的作品文件会自动跳过下载；直播文件不受限制。</p>
<h3>文件分块下载</h3>

```json
{
  "chunk": 10485760
}
```

<p>下载文件时每次从服务器接收 10485760 字节 (10 MB)的数据块。</p>
<ul>
<li>影响下载速度：较大的 chunk 会增加每次下载的数据量，从而提高下载速度。相反，较小的 chunk 会降低每次下载的数据量，可能导致下载速度稍慢。</li>
<li>影响内存占用：较大的 chunk 会一次性加载更多的数据到内存中，可能导致内存占用增加。相反，较小的 chunk 会减少每次加载的数据量，从而降低内存占用。</li>
</ul>
<h3>请求次数限制</h3>

```json
{
  "max_pages": 2
}
```

<p>下载账号喜欢作品、收藏作品以及采集作品评论数据时，仅获取前 <code>2</code> 页数据；用于解决下载账号喜欢作品、收藏作品需要获取全部数据的问题，以及作品评论数据数量过多的采集问题。</p>
<p>不影响下载账号发布作品，如需控制账号发布作品数据获取次数，请使用 <code>earliest</code> 和 <code>latest</code> 参数实现。</p>
<h3>默认执行命令</h3>

```json
{
  "run_command": "6 1 1 Q"
}
```

<p>上述命令表示运行程序自动依次执行 <code>终端交互模式</code> -> <code>批量下载账号作品(抖音)</code> -> <code>使用 accounts_urls 参数的账号链接(推荐)</code> -> <code>退出程序</code></p>
<p>该参数可以实现设置默认启动模式、运行功能后自动退出、自动读取浏览器 Cookie 等高级自动化功能！</p>
<ul>其他示例：
<li><code>6 2</code>：代表依次执行 <code>终端交互模式</code> -> <code>批量下载账号作品(抖音)</code></li>
<li><code>8</code>：代表执行<code>Web API 模式</code></li>
<li><code>2 7</code>：代表依次执行<code>从浏览器读取 Cookie (抖音)</code> -> <code>Edge</code></li>
</ul>
<h3>程序代理设置</h3>

```json
{
  "proxy": "http://127.0.0.1:9999"
}
```

<p>程序获取网络数据时使用 <code>http://127.0.0.1:9999</code> 作为代理；程序会自动验证代理是否可用，如果代理不可用，则 <code>proxy</code> 参数不生效。</p>
<p>如果您的电脑使用了代理工具且未修改默认端口，可以尝试以下设置：</p>
<ul>
<li>Clash: <code>http://127.0.0.1:7890</code></li>
<li>v2rayN: <code>http://127.0.0.1:10809</code></li>
</ul>
<h1>高级配置</h1>
<p>如果想要进一步修改程序功能，可以编辑 <code>src/custom</code> 文件夹内容（不适用于可执行文件），按照注释指引和实际需求进行自定义修改。</p>
<b>部分可自定义设置的功能：</b>
<ul>
<li>设置作品文件下载的最大线程数量</li>
<li>设置非法字符替换规则</li>
<li>设置服务器模式主机及端口</li>
<li>设置平台参数更新间隔</li>
<li>设置彩色交互提示颜色</li>
<li>设置请求数据延时间隔</li>
<li>设置自定义作品筛选规则</li>
<li>设置分批获取数据策略</li>
<li>设置服务器模式参数验证</li>
</ul>
<h1>功能介绍</h1>
<h2>从剪贴板读取 Cookie</h2>
<p>参考 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 提取教程</a>，手动从浏览器复制所需 Cookie 内容至剪贴板，再按照程序提示操作；程序会自动读取剪贴板的内容并将有效的 Cookie 写入配置文件。</p>
<p>成功写入配置文件后，程序会提示当前 Cookie 登录状态！</p>
<h2>从浏览器读取 Cookie</h2>
<p>自动读取本地浏览器的 Cookie 数据，并提取所需 Cookie 写入配置文件。</p>
<p>成功写入配置文件后，程序会提示当前 Cookie 登录状态！</p>
<p>Windows 系统需要以管理员身份运行程序才能读取 Chromium、Chrome、Edge 浏览器 Cookie！</p>
<p><strong>兼容性提醒：此功能依赖的第三方模块已长期未更新，可能无法正常支持最新浏览器版本。若功能出现异常，请尝试手动获取 Cookie！</strong></p>
<h2><del>扫码登录获取 Cookie</del></h2>
<p><del>程序自动获取抖音登录二维码，随后会在终端输出二维码，并使用系统默认图片浏览器打开二维码图片，使用者通过抖音 APP 扫码并登录账号，操作后关闭二维码图片窗口，程序会自动检查登录结果并将登录后的 Cookie 写入配置文件。</del></p>
<p><b>注意：</b>扫码登录可能会导致抖音账号被风控，该功能仅限学习研究，未来可能禁用或移除该功能！</p>
<h2>终端交互模式</h2>
<p>功能最全面的模式，支持全部功能。</p>
<h3>批量下载账号作品(抖音)</h3>
<ol>
<li>使用 <code>settings.json</code> 的 <code>accounts_urls</code> 参数中的账号链接。</li>
<li>手动输入待采集的账号链接；此选项仅支持批量下载账号发布页作品，暂不支持参数设置。</li>
<li>输入文本文档路径，读取文件包含的账号链接；此选项仅支持批量下载账号发布页作品，暂不支持参数设置。</li>
</ol>
<p>支持链接格式：</p>
<ul>
<li><code>https://v.douyin.com/分享码/</code></li>
<li><code>https://www.douyin.com/user/账号ID</code></li>
<li><code>https://www.douyin.com/user/账号ID?modal_id=作品ID</code></li>
</ul>
<p><del>如果需要大批量采集账号作品，建议启用 <code>src/custom/function.py</code> 文件的 <code>suspend</code> 方法。</del>（默认启用）</p>
<p><b>下载账号喜欢作品时需要使用已登录的 Cookie，否则程序可能无法正常获取账号消息！</b></p>
<p>如果当前账号昵称或账号标识不是有效的文件夹名称时，程序会自动替换为账号 ID。</p>
<p>每个账号的作品会下载至 <code>root</code> 参数路径下的账号文件夹，账号文件夹格式为 <code>UID123456789_mark_类型</code> 或者 <code>UID123456789_账号昵称_类型</code></p>
<h3>批量下载链接作品(抖音)</h3>
<ol>
<li>手动输入待采集的作品链接。</li>
<li>输入文本文档路径，读取文件包含的作品链接。</li>
</ol>
<p>支持链接格式：</p>
<ul>
<li><code>https://v.douyin.com/分享码/</code></li>
<li><code>https://www.douyin.com/note/作品ID</code></li>
<li><code>https://www.douyin.com/video/作品ID</code></li>
<li><code>https://www.douyin.com/discover?modal_id=作品ID</code></li>
<li><code>https://www.douyin.com/user/账号ID?modal_id=作品ID</code></li>
<li><code>https://www.douyin.com/search/关键词?modal_id=作品ID</code></li>
<li><code>https://www.douyin.com/channel/分区ID?modal_id=作品ID</code></li>
</ul>
<p>作品会下载至 <code>root</code> 参数和 <code>folder_name</code> 参数拼接成的文件夹。</p>
<h3>获取直播拉流地址(抖音)</h3>
<p>输入直播链接，不支持已结束的直播。</p>
<p>支持链接格式：</p>
<ul>
<li><code>https://live.douyin.com/直播ID</code></li>
<li><code>https://v.douyin.com/分享码/</code></li>
<li><code>https://www.douyin.com/follow?webRid=直播ID</code></li>
</ul>
<p>下载说明：</p>
<ul>
<li>程序会询问用户是否下载直播视频，支持同时下载多个直播视频。</li>
<li>程序调用 <code>ffmpeg</code> 下载直播时，关闭 DouK-Downloader 不会影响直播下载。</li>
<li><del>程序调用内置下载器下载直播时，需要保持 DouK-Downloader 运行直到直播结束。</del></li>
<li>程序询问是否下载直播时，输入直播清晰度或者对应序号即可下载，例如：下载最高清晰度输入 <code>FULL_HD1</code> 或者 <code>1</code> 均可。</li>
<li><del>程序调用内置下载器下载的直播文件，视频时长会显示为直播总时长，实际视频内容从下载时间开始，靠后部分的片段无法播放。</del></li>
<li>直播视频会下载至 <code>root</code> 参数路径下的 <code>Live</code> 文件夹。</li>
<li>按下 <code>Ctrl + C</code> 终止程序或 <code>ffmpeg</code> 并不会导致已下载文件丢失或损坏，但无法继续下载。</li>
</ul>
<h3>采集作品评论数据(抖音)</h3>
<p><strong>评论回复采集功能暂不开放！</strong></p>
<ol>
<li>手动输入待采集的作品链接。</li>
<li>输入文本文档路径，读取文件包含的作品链接。</li>
</ol>
<p>支持链接格式：</p>
<ul>
<li><code>https://v.douyin.com/分享码/</code></li>
<li><code>https://www.douyin.com/note/作品ID</code></li>
<li><code>https://www.douyin.com/video/作品ID</code></li>
<li><code>https://www.douyin.com/discover?modal_id=作品ID</code></li>
<li><code>https://www.douyin.com/user/账号ID?modal_id=作品ID</code></li>
<li><code>https://www.douyin.com/search/关键词?modal_id=作品ID</code></li>
<li><code>https://www.douyin.com/channel/分区ID?modal_id=作品ID</code></li>
</ul>
<p>支持采集<del>评论回复</del>、评论表情、评论图片；必须设置 <code>storage_format</code> 参数才能正常使用。</p>
<p>储存名称格式：<code>作品123456789_评论数据</code></p>
<h3>批量下载合集作品(抖音)</h3>
<ol>
<li>使用 <code>settings.json</code> 的 <code>mix_urls</code> 参数中的合集链接或作品链接。</li>
<li>获取当前登录 Cookie 的收藏合集信息，并由使用者选择需要下载的合集；该选项暂不支持设置合集标识。</li>
<li>输入合集链接，或者属于合集的任意一个作品链接；该选项暂不支持设置合集标识。</li>
<li>输入文本文档路径，读取文件包含的作品链接或合集链接；该选项暂不支持设置合集标识。</li>
</ol>
<p>支持链接格式：</p>
<ul>
<li><code>https://v.douyin.com/分享码/</code></li>
<li><code>https://www.douyin.com/note/作品ID</code></li>
<li><code>https://www.douyin.com/video/作品ID</code></li>
<li><code>https://www.douyin.com/discover?modal_id=作品ID</code></li>
<li><code>https://www.douyin.com/user/账号ID?modal_id=作品ID</code></li>
<li><code>https://www.douyin.com/search/关键词?modal_id=作品ID</code></li>
<li><code>https://www.douyin.com/collection/合集ID</code></li>
<li><code>https://www.douyin.com/channel/分区ID?modal_id=作品ID</code></li>
</ul>
<p><del>如果需要大批量采集合集作品，建议启用 <code>src/custom/function.py</code> 文件的 <code>suspend</code> 方法。</del>（默认启用）</p>
<p>如果当前合集标题或合集标识不是有效的文件夹名称时，程序会自动替换为合集 ID。</p>
<p>每个合集的作品会下载至 <code>root</code> 参数路径下的合集文件夹，合集文件夹格式为 <code>MIX123456789_mark_合集作品</code> 或者 <code>MIX123456789_合集标题_合集作品</code></p>
<h3>采集账号详细数据(抖音)</h3>
<ol>
<li>使用 <code>settings.json</code> 的 <code>accounts_urls</code> 参数中的账号链接。</li>
<li>手动输入待采集的账号链接。</li>
<li>输入文本文档路径，读取文件包含的账号链接。</li>
</ol>
<p>支持链接格式：</p>
<ul>
<li><code>https://v.douyin.com/分享码/</code></li>
<li><code>https://www.douyin.com/user/账号ID</code></li>
<li><code>https://www.douyin.com/user/账号ID?modal_id=作品ID</code></li>
</ul>
<p>重复获取相同账号数据时会储存为新的数据行，不会覆盖原有数据；必须设置 <code>storage_format</code> 参数才能正常使用。</p>
<h3>采集搜索结果数据(抖音)</h3>
<h4>搜索条件规则</h4>
<ul>
<li>
<strong>综合搜索参数顺序：</strong><code>关键词</code>;<code>总页数</code>;<code>排序依据</code>;<code>发布时间</code>;<code>视频时长</code>;<code>搜索范围</code>;<code>内容格式</code>
</li>
<li>
<strong>视频搜索参数顺序：</strong><code>关键词</code>;<code>总页数</code>;<code>排序依据</code>;<code>发布时间</code>;<code>视频时长</code>;<code>搜索范围</code>
</li>
<li>
<strong>用户搜索参数顺序：</strong><code>关键词</code>;<code>总页数</code>;<code>粉丝数量</code>;<code>用户类型</code>
</li>
<li>
<strong>直播搜索参数顺序：</strong><code>关键词</code>;<code>总页数</code>
</li>
</ul>
<h4>参数含义</h4>
<ul>
<li>排序依据：<code>0</code>：综合排序；<code>1</code>：最多点赞；<code>2</code>：最新发布</li>
<li>发布时间：<code>0</code>：不限；<code>1</code>：一天内；<code>7</code>：一周内；<code>180</code>：半年内</li>
<li>视频时长：<code>0</code>：不限；<code>1</code>：一分钟以内；<code>2</code>：一到五分钟；<code>3</code>：五分钟以上</li>
<li>搜索范围：<code>0</code>：不限；<code>1</code>：最近看过；<code>2</code>：还未看过；<code>3</code>：关注的人</li>
<li>内容形式：<code>0</code>：不限；<code>1</code>：视频；<code>2</code>：图文</li>
<li>粉丝数量：<code>0</code>：不限；<code>1</code>：1000以下；<code>2</code>：1000-1W；<code>3</code>：1W-10W；<code>4</code>：10W-100W；<code>5</code>：100W以上</li>
<li>用户类型：<code>0</code>：不限；<code>1</code>：普通用户；<code>2</code>：企业认证；<code>3</code>：个人认证</li>
</ul>
<p><strong>参数之间使用两个空格分隔；除了搜索关键词以外的参数均只支持输入数值；未输入的参数均视为 <code>0</code></strong></p>
<p>程序采集的搜索结果数据会储存至文件；暂不支持直接下载搜索结果作品；必须设置 <code>storage_format</code> 参数才能正常使用。</p>
<h4>参数输入示例</h4>
<h5>综合搜索/视频搜索</h5>
<p><strong>输入：</strong><code>猫咪</code></p>
<table>
<tr>
<th align="center" rowspan="2">含义</th>
<th align="center">关键词</th>
<th align="center">总页数</th>
<th align="center">排序依据</th>
<th align="center">发布时间</th>
<th align="center">视频时长</th>
<th align="center">搜索范围</th>
<th align="center">内容形式</th>
</tr>
<tr>
<td align="center">猫咪</td>
<td align="center">1</td>
<td align="center">不限</td>
<td align="center">不限</td>
<td align="center">不限</td>
<td align="center">不限</td>
<td align="center">不限</td>
</tr>
</table>
<hr>
<p><strong>输入：</strong><code>猫咪&nbsp;&nbsp;2&nbsp;&nbsp;2&nbsp;&nbsp;7&nbsp;&nbsp;0&nbsp;&nbsp;1</code></p>
<table>
<tr>
<th align="center" rowspan="2">含义</th>
<th align="center">关键词</th>
<th align="center">总页数</th>
<th align="center">排序依据</th>
<th align="center">发布时间</th>
<th align="center">视频时长</th>
<th align="center">搜索范围</th>
<th align="center">内容形式</th>
</tr>
<tr>
<td align="center">猫咪</td>
<td align="center">2</td>
<td align="center">最新发布</td>
<td align="center">一周内</td>
<td align="center">不限</td>
<td align="center">最近看过</td>
<td align="center">不限</td>
</tr>
</table>
<hr>
<p><strong>输入：</strong><code>猫咪&nbsp;&nbsp;10&nbsp;&nbsp;0&nbsp;&nbsp;0&nbsp;&nbsp;0&nbsp;&nbsp;3</code></p>
<table>
<tr>
<th align="center" rowspan="2">含义</th>
<th align="center">关键词</th>
<th align="center">总页数</th>
<th align="center">排序依据</th>
<th align="center">发布时间</th>
<th align="center">视频时长</th>
<th align="center">搜索范围</th>
<th align="center">内容形式</th>
</tr>
<tr>
<td align="center">猫咪</td>
<td align="center">10</td>
<td align="center">不限</td>
<td align="center">不限</td>
<td align="center">不限</td>
<td align="center">关注的人</td>
<td align="center">不限</td>
</tr>
</table>
<hr>
<p><strong>输入：</strong><code>猫咪&nbsp;白&nbsp;&nbsp;5&nbsp;&nbsp;0&nbsp;&nbsp;180</code></p>
<table>
<tr>
<th align="center" rowspan="2">含义</th>
<th align="center">关键词</th>
<th align="center">总页数</th>
<th align="center">排序依据</th>
<th align="center">发布时间</th>
<th align="center">视频时长</th>
<th align="center">搜索范围</th>
<th align="center">内容形式</th>
</tr>
<tr>
<td align="center">猫咪 白</td>
<td align="center">5</td>
<td align="center">不限</td>
<td align="center">半年内</td>
<td align="center">不限</td>
<td align="center">不限</td>
<td align="center">不限</td>
</tr>
</table>
<h5>用户搜索</h5>
<p><strong>输入：</strong><code>小姐姐&nbsp;&nbsp;10&nbsp;&nbsp;0&nbsp;&nbsp;0</code></p>
<table>
<tr>
<th align="center" rowspan="2">含义</th>
<th align="center">关键词</th>
<th align="center">总页数</th>
<th align="center">粉丝数量</th>
<th align="center">用户类型</th>
</tr>
<tr>
<td align="center">小姐姐</td>
<td align="center">10</td>
<td align="center">不限</td>
<td align="center">不限</td>
</tr>
</table>
<hr>
<p><strong>输入：</strong><code>小姐姐&nbsp;&nbsp;5&nbsp;&nbsp;4&nbsp;&nbsp;3</code></p>
<table>
<tr>
<th align="center" rowspan="2">含义</th>
<th align="center">关键词</th>
<th align="center">总页数</th>
<th align="center">粉丝数量</th>
<th align="center">用户类型</th>
</tr>
<tr>
<td align="center">小姐姐</td>
<td align="center">5</td>
<td align="center">10W-100W</td>
<td align="center">个人认证</td>
</tr>
</table>
<h5>直播搜索</h5>
<p><strong>输入：</strong><code>跳舞&nbsp;&nbsp;10</code></p>
<table>
<tr>
<th align="center" rowspan="2">含义</th>
<th align="center">关键词</th>
<th align="center">总页数</th>
</tr>
<tr>
<td align="center">跳舞</td>
<td align="center">10</td>
</tr>
</table>
<h3>采集抖音热榜数据(抖音)</h3>
<p>无需输入任何内容；采集 <code>抖音热榜</code>、<code>娱乐榜</code>、<code>社会榜</code>、<code>挑战榜</code> 数据并储存至文件；必须设置 <code>storage_format</code> 参数才能正常使用。</p>
<p>储存名称格式：<code>热榜数据_采集时间_热榜名称</code></p>
<h3>批量下载话题作品(抖音)</h3>
<p>暂不支持！</p>
<h3>批量下载收藏作品(抖音)</h3>
<p>无需输入任何内容；需要在配置文件写入已登录的 Cookie，并在 <code>owner_url</code> 参数填入对应的账号主页链接和账号标识（可选参数）；目前仅支持采集当前 Cookie 对应账号的收藏作品。</p>
<p>文件夹格式为 <code>UID123456789_mark_收藏作品</code> 或者 <code>UID123456789_账号昵称_收藏作品</code></p>
<h3>批量下载收藏夹作品(抖音)</h3>
<p>无需输入任何内容；需要在配置文件写入已登录的 Cookie，程序会自动获取当前 Cookie 账号的收藏夹数据并展示，根据程序提示输入收藏夹序号下载对应收藏夹作品文件，输入 <code>ALL</code> 下载全部收藏夹作品。</p>
<p>文件夹格式为 <code>CID123456789_收藏夹名称_收藏作品</code></p>
<h3>批量下载账号作品(TikTok)</h3>
<ol>
<li>使用 <code>settings.json</code> 的 <code>accounts_urls_tiktok</code> 参数中的账号链接。</li>
<li>手动输入待采集的账号链接；此选项仅支持批量下载账号发布页作品，暂不支持参数设置。</li>
<li>输入文本文档路径，读取文件包含的账号链接；此选项仅支持批量下载账号发布页作品，暂不支持参数设置。</li>
</ol>
<p>支持链接格式：</p>
<ul>
<li><code>https://www.tiktok.com/@TikTok号</code></li>
<li><code>https://www.tiktok.com/@TikTok号/video/作品ID</code></li>
</ul>
<p><del>如果需要大批量采集账号作品，建议启用 <code>src/custom/function.py</code> 文件的 <code>suspend</code> 方法。</del>（默认启用）</p>
<p>如果当前账号昵称或账号标识不是有效的文件夹名称时，程序会自动替换为账号 ID。</p>
<p>每个账号的作品会下载至 <code>root</code> 参数路径下的账号文件夹，账号文件夹格式为 <code>UID123456789_mark_类型</code> 或者 <code>UID123456789_账号昵称_类型</code></p>
<h3>批量下载链接作品(TikTok)</h3>
<ol>
<li>手动输入待采集的作品链接。</li>
<li>输入文本文档路径，读取文件包含的作品链接。</li>
</ol>
<p>支持链接格式：</p>
<ul>
<li><code>https://vm.tiktok.com/分享码/</code></li>
<li><code>https://www.tiktok.com/@TikTok号/video/作品ID</code></li>
</ul>
<p>作品会下载至 <code>root</code> 参数和 <code>folder_name</code> 参数拼接成的文件夹。</p>
<h3>批量下载合集作品(TikTok)</h3>
<ol>
<li>使用 <code>settings.json</code> 的 <code>mix_urls_tiktok</code> 参数中的合集链接。</li>
<li>输入合集链接；该选项暂不支持设置合集标识。</li>
<li>输入文本文档路径，读取文件包含的合集链接；该选项暂不支持设置合集标识。</li>
</ol>
<p>支持链接格式：</p>
<ul>
<li><code>https://vt.tiktok.com/分享码/</code></li>
<li><code>https://www.tiktok.com/@TikTok号/playlist/合辑信息</code></li>
<li><code>https://www.tiktok.com/@TikTok号/collection/合辑信息</code></li>
</ul>
<p><del>如果需要大批量采集合集作品，建议启用 <code>src/custom/function.py</code> 文件的 <code>suspend</code> 方法。</del>（默认启用）</p>
<p>如果当前合集标题或合集标识不是有效的文件夹名称时，程序会自动替换为合集 ID。</p>
<p>每个合集的作品会下载至 <code>root</code> 参数路径下的合集文件夹，合集文件夹格式为 <code>MIX123456789_mark_合集作品</code> 或者 <code>MIX123456789_合集标题_合集作品</code></p>
<h3>获取直播拉流地址(TikTok)</h3>
<p>输入直播链接，不支持已结束的直播。</p>
<p>支持链接格式：</p>
<ul>
<li><code>https://vt.tiktok.com/分享码/</code></li>
<li><code>https://www.tiktok.com/@TikTok号/live</code></li>
</ul>
<p>下载说明：</p>
<ul>
<li>程序会询问用户是否下载直播视频，支持同时下载多个直播视频。</li>
<li>程序调用 <code>ffmpeg</code> 下载直播时，关闭 DouK-Downloader 不会影响直播下载。</li>
<li><del>程序调用内置下载器下载直播时，需要保持 DouK-Downloader 运行直到直播结束。</del></li>
<li>程序询问是否下载直播时，输入直播清晰度或者对应序号即可下载，例如：下载最高清晰度输入 <code>FULL_HD1</code> 或者 <code>1</code> 均可。</li>
<li><del>程序调用内置下载器下载的直播文件，视频时长会显示为直播总时长，实际视频内容从下载时间开始，靠后部分的片段无法播放。</del></li>
<li>直播视频会下载至 <code>root</code> 参数路径下的 <code>Live</code> 文件夹。</li>
<li>按下 <code>Ctrl + C</code> 终止程序或 <code>ffmpeg</code> 并不会导致已下载文件丢失或损坏，但无法继续下载。</li>
</ul>
<h3><del>批量下载视频原画(TikTok)</del></h3>
<p><strong>注意：本功能为实验性功能，依赖第三方 API 服务，可能不稳定或存在限制！</strong></p>
<ol>
<li>手动输入待采集的作品链接。</li>
<li>输入文本文档路径，读取文件包含的作品链接。</li>
</ol>
<p>支持链接格式：</p>
<ul>
<li><code>https://vm.tiktok.com/分享码/</code></li>
<li><code>https://www.tiktok.com/@TikTok号/video/作品ID</code></li>
</ul>
<p>作品会下载至 <code>root</code> 参数和 <code>folder_name</code> 参数拼接成的文件夹。</p>
<h2>后台监听模式</h2>
<h3>剪贴板监听下载</h3>
<p>程序会自动检测并提取剪贴板中的抖音和 TikTok 作品链接，并自动下载作品文件；如需关闭，请按下 Ctrl+C，或将剪贴板内容设置为“close”以停止监听！</p>
<h2>Web API 接口模式</h2>
<p>启动服务器，提供 API 调用功能；支持局域网远程访问，可以部署至私有服务器或者公开服务器，远程部署建议设置参数验证，防止恶意请求！</p>
<p>默认禁用局域网访问，如需开启，请修改 <code>src/custom/static.py</code> 文件的 <code>SERVER_HOST</code> 变量。</p>
<p><strong>启动该模式后，访问 <code>http://127.0.0.1:5555/docs</code> 或者 <code>http://127.0.0.1:5555/redoc</code> 可以查阅自动生成的文档！</strong></p>
<h3>API 调用示例代码</h3>
<pre>
from httpx import post
from rich import print


def demo():
headers = {"token": ""}
data = {
"detail_id": "0123456789",
"pages": 2,
}
api = "http://127.0.0.1:5555/douyin/comment"
response = post(api, json=data, headers=headers)
print(response.json())

demo()
</pre>
<h2>Web UI 交互模式</h2>
<p><b>项目代码已重构，该模式代码尚未更新，未来开发完成重新开放！</b></p>
<h2>启用/禁用作品下载记录</h2>
<ul>
<li>启用该功能：程序会记录下载成功的作品 ID，如果对作品文件进行移动、重命名或者删除操作，程序不会重复下载该作品，如果想要重新下载该作品，需要删除记录数据中对应的作品 ID。</li>
<li>禁用该功能：程序会在下载文件前检测文件是否存在，如果文件存在会自动跳过下载该作品，如果对作品文件进行移动、重命名或者删除操作，程序将会重新下载该作品。</li>
</ul>
<p>数据路径: <code>./Volume/DouK-Downloader.db</code> 的 <code>download_data</code> 数据表。</p>
<h2>删除指定下载记录</h2>
<p>输入作品 ID 或者作品完整链接（多个作品之间使用空格分隔，支持混合输入），删除作品下载记录中对应的数据，如果输入 <code>all</code>，代表清空作品下载记录数据！</p>
<h2>启用/禁用运行日志记录</h2>
<p>是否将程序运行日志记录保存到文件，默认关闭，日志文件保存路径：<code>./Volume/Log</code></p>
<p>如果在使用过程中发现程序 Bug，可以及时告知作者，并附上日志文件，日志记录有助于作者分析 Bug 原因和修复 Bug。</p>
<h2>检查程序版本更新</h2>
<p>程序会向 <code>https://github.com/JoeanAmier/TikTokDownloader/releases/latest</code>
发送请求获取最新 <code>Releases</code> 版本号，并提示是否存在新版本。</p>
<p>如果检查新版本失败，可能是访问 GitHub 超时，并非功能异常；如果存在新版本会提示新版本的 <code>URL</code> 地址，不会自动下载更新。</p>
<h1>其他功能说明</h1>
<h2>单次输入多个链接</h2>
<p><code>批量下载账号作品</code>、<code>批量下载链接作品</code>、<code>获取直播拉流地址</code>、<code>采集作品评论数据</code>、<code>批量下载合集作品</code>、<code>采集账号详细数据</code>
功能支持单次输入多个链接，实现批量下载 / 提取功能；支持完整链接与分享链接混合输入；输入多个链接时，需要使用空格分隔；无需对复制的链接进行额外处理，程序会自动提取输入文本中的有效链接。</p>
<h2 id="mark">账号/合集标识说明</h2>
<h3>标识设置规则</h3>
<ul>
<li><code>name_format</code> 参数中没有使用 <code>nickname</code> 时，<code>mark</code> 设置没有限制。</li>
<li><code>name_format</code> 参数中使用了 <code>nickname</code> 时，<code>mark</code> 与 <code>nickname</code> 不能设置为包含关系的字符串。</li>
</ul>
<p><strong>标识示例：</strong></p>
<ul>
<li>✔️ <code>nickname</code>：ABC，<code>mark</code>：DEF</li>
<li>✔️ <code>nickname</code>：ABC，<code>mark</code>：BCD</li>
<li>❌ <code>nickname</code>：ABC，<code>mark</code>：AB</li>
<li>❌ <code>nickname</code>：BC，<code>mark</code>：ABC</li>
</ul>
<h3>账号标识说明</h3>
<ul>
<li>账号标识 <code>mark</code> 参数相当于账号备注，便于用户识别账号作品文件夹，避免账号昵称修改导致无法识别已下载作品问题。</li>
<li><code>批量下载账号作品</code> 模式下，如果设置了 <code>mark</code> 参数，下载的作品将会保存至 <code>UID123456789_mark_发布作品</code>
或 <code>UID123456789_mark_喜欢作品</code> 文件夹内。</li>
<li><code>批量下载账号作品</code> 模式下，如果 <code>mark</code>
参数设置为空字符串，程序将会使用账号昵称作为账号标识，下载的作品将会保存至 <code>UID123456789_账号昵称_发布作品</code>
或 <code>UID123456789_账号昵称_喜欢作品</code> 文件夹内。</li>
</ul>
<h3>合集标识说明</h3>
<p>与账号标识作用一致。</p>
<h3>如何修改标识</h3>
<p><strong>修改账号标识:</strong> 修改 <code>accounts_urls</code> 或 <code>accounts_urls_tiktok</code> 的 <code>mark</code> 参数，再次运行 <code>批量下载账号作品</code> 模式，程序会自动应用新的账号标识。</p>
<p><strong>修改合集标识:</strong> 修改 <code>mix_urls</code> 或 <code>mix_urls_tiktok</code> 的 <code>mark</code> 参数，再次运行 <code>批量下载合集作品</code> 模式，程序会自动应用新的账号标识。</p>
<h2>账号昵称/合集标题自动更新</h2>
<p>在 <code>批量下载账号作品</code> 和 <code>批量下载合集作品</code> 模式下，程序会自动判断账号昵称/合集标题是否发生变化，如果发生变化，程序会自动识别已下载作品文件名称中的账号昵称/合集标题，并修改至最新账号昵称/合集标题。</p>
<p>程序会优先使用账号标识/合集标识进行更新处理，如果账号标识/合集标识为空字符串，程序会自动使用账号昵称/合集标题进行更新处理。</p>
<h3>映射缓存数据</h3>
<p><strong>数据路径: <code>./Volume/DouK-Downloader.db</code> 的 <code>mapping_data</code> 数据表；</strong>
用于记录账号 / 合集标识和账号昵称，当账号 / 合集标识或账号昵称发生变化时，程序会对相应的文件夹和文件进行重命名更新处理。</p>
<p><strong>缓存数据仅供程序读取和修改，不建议手动编辑数据内容。</strong></p>

# 构建可执行文件指南

本指南将引导您通过 Fork 本仓库并执行 GitHub Actions 自动完成基于最新源码的程序构建和打包！

---

## 使用步骤

### 1. Fork 本仓库

1. 点击项目仓库右上角的 **Fork** 按钮，将本仓库 Fork 到您的个人 GitHub 账户中
2. 您的 Fork 仓库地址将类似于：`https://github.com/your-username/this-repo`

---

### 2. 启用 GitHub Actions

1. 前往您 Fork 的仓库页面
2. 点击顶部的 **Settings** 选项卡
3. 点击右侧的 **Actions** 选项卡
4. 点击 **General** 选项
5. 在 **Actions permissions** 下，选择 **Allow all actions and reusable workflows** 选项，点击 **Save** 按钮

---

### 3. 手动触发打包流程

1. 在您 Fork 的仓库中，点击顶部的 **Actions** 选项卡
2. 找到名为 **手动构建可执行文件** 的工作流
3. 点击右侧的 **Run workflow** 按钮：
    - 选择 **master** 或者 **develop** 分支
    - 点击 **Run workflow**

---

### 4. 查看打包进度

1. 在 **Actions** 页面中，您可以看到触发的工作流运行记录
2. 点击运行记录，查看详细的日志以了解打包进度和状态

---

### 5. 下载打包结果

1. 打包完成后，进入对应的运行记录页面
2. 在页面底部的 **Artifacts** 部分，您将看到打包的结果文件
3. 点击下载并保存到本地，即可获得打包好的程序

---

## 注意事项

1. **资源使用**：
    - Actions 的运行环境由 GitHub 免费提供，普通用户每月有一定的免费使用额度（2000 分钟）

2. **代码修改**：
    - 您可以自由修改 Fork 仓库中的代码以定制程序打包流程
    - 修改后重新触发打包流程，您将得到自定义的构建版本

3. **与主仓库保持同步**：
    - 如果主仓库更新了代码或工作流，建议您定期同步 Fork 仓库以获取最新功能和修复

---

## Actions 常见问题

### Q1: 为什么我无法触发工作流？

A: 请确认您已按照步骤 **启用 Actions**，否则 GitHub 会禁止运行工作流

### Q2: 打包流程失败怎么办？

A:

- 检查运行日志，了解失败原因
- 确保代码没有语法错误或依赖问题
- 如果问题仍未解决，可以在本仓库的 [Issues 页面](https://github.com/JoeanAmier/TikTokDownloader/issues) 提出问题

### Q3: 我可以直接使用主仓库的 Actions 吗？

A: 由于权限限制，您无法直接触发主仓库的 Actions。请通过 Fork 仓库的方式执行打包流程

<h1>常见问题与解决方案</h1>
<h2>响应内容不是有效的 JSON 数据</h2>
<p>可能是 Cookie 无效或者接口失效；请尝试清除 DNS 缓存，更新 Cookie，如果仍然无法解决，可能是接口失效，请考虑向作者反馈！</p>
<h2 id="twc">获取 ttwid 参数失败</h2>
<p>TikTok 平台的 Cookie ttwid 值无效；可能是当前账号被风控，请考虑更换账号，或者尝试设置 <code>twc_tiktok</code> 参数。</p>
<p><code>twc_tiktok</code> 参数设置教程：</p>
<ul>
<li>以无痕模式打开浏览器</li>
<li>按 <code>F12</code> 打开开发人员工具</li>
<li>选择 <code>网络</code> 选项卡</li>
<li>访问 <code>https://www.tiktok.com/</code></li>
<li>在 <code>筛选器</code> 输入框输入 <code>ttwid</code></li>
<li>在开发人员工具窗口选择任意一个数据包(如果无数据包，刷新网页)</li>
<li>检查 <code>响应标头</code> -> <code>Set-Cookie</code></li>
<li>复制 <code>ttwid=XXX</code> 内容</li>
<li>粘贴至配置文件的 <code>twc_tiktok</code> 参数</li>
</ul>
<p><code>Set-Cookie</code> 的内容格式为：<code>ttwid=XXX; Path=/; Domain=tiktok.com; Max-Age=31536000; HttpOnly; Secure; SameSite=None</code>，复制时只需要复制 <code>ttwid=XXX</code> 部分，而不是复制全部内容！</p>
<h2>采集数据而不下载文件</h2>
<p>将配置文件的 <code>download</code> 参数设置为 <code>false</code>，并设置 <code>storage_format</code> 参数，程序将不会下载任何文件，仅采集数据。</p>
<h2>请求超时：timed out</h2>
<p>网络异常；如果您的网络需要使用代理才能访问 TikTok，请在配置文件设置 <code>proxy</code> 参数！</p>
<h2>self 获取账号信息失败</h2>
<p>请把配置文件的 <code>owner_url</code> 参数修改为实际的抖音主页链接，获取方式请查阅 <a href="https://github.com/JoeanAmier/TikTokDownloader/issues/416">issue</a></p>
<h1>免责声明</h1>
<ol>
<li>使用者对本项目的使用由使用者自行决定，并自行承担风险。作者对使用者使用本项目所产生的任何损失、责任、或风险概不负责。</li>
<li>本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。作者按现有技术水平努力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。</li>
<li>本项目依赖的所有第三方库、插件或服务各自遵循其原始开源或商业许可，使用者需自行查阅并遵守相应协议，作者不对第三方组件的稳定性、安全性及合规性承担任何责任。</li>
<li>使用者在使用本项目时必须严格遵守 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/LICENSE">GNU
    General Public License v3.0</a> 的要求，并在适当的地方注明使用了 <a
        href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/LICENSE">GNU General Public License
    v3.0</a> 的代码。
</li>
<li>使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。</li>
<li>使用者不得使用本工具从事任何侵犯知识产权的行为，包括但不限于未经授权下载、传播受版权保护的内容，开发者不参与、不支持、不认可任何非法内容的获取或分发。</li>
<li>本项目不对使用者涉及的数据收集、存储、传输等处理活动的合规性承担责任。使用者应自行遵守相关法律法规，确保处理行为合法正当；因违规操作导致的法律责任由使用者自行承担。</li>
<li>使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。</li>
<li>本项目的作者不会提供 DouK-Downloader 项目的付费版本，也不会提供与 DouK-Downloader 项目相关的任何商业服务。</li>
<li>基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的各种情况负全部责任。</li>
<li>本项目不授予使用者任何专利许可；若使用本项目导致专利纠纷或侵权，使用者自行承担全部风险和责任。未经作者或权利人书面授权，不得使用本项目进行任何商业宣传、推广或再授权。</li>
<li>作者保留随时终止向任何违反本声明的使用者提供服务的权利，并可能要求其销毁已获取的代码及衍生作品。</li>
<li>作者保留在不另行通知的情况下更新本声明的权利，使用者持续使用即视为接受修订后的条款。</li>
</ol>
<b>在使用本项目的代码和功能之前，请您认真考虑并接受以上免责声明。如果您对上述声明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险和后果。</b>
```

## File: `docs/Release_Notes.md`
```markdown
**更新内容：**

1. API 模式搜索接口增加 `offset` 和 `count` 参数
2. 修复部分 TikTok 账号提取 sec_user_id 失败的问题
3. 修复 API 模式账号作品接口部分参数不生效的问题
4. 修复 API 模式搜索接口多页数据报错的问题
5. 修复 API 模式搜索接口结果为空报错的问题
6. 修复 TikTok 平台批量下载账号作品功能
7. 修复 TikTok 平台批量下载合集作品功能
8. 修复报错时可能损坏 XLSX 文件的问题
9. TikTok 平台新增 X-Gnarly 请求参数
10. 优化提取 secUid 的正则表达式
11. 服务器模式默认启用局域网访问
12. 修复请求参数编码错误的问题
13. 修复提取作品 ID 失败的问题
14. 更新数据接口请求参数
15. 更新项目英语翻译
16. 修正项目功能描述
17. 修复其他已知问题
```

## File: `locale/generate_path.py`
```python
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def find_python_files(dir_, file):
    with open(file, "w", encoding="utf-8") as f:
        for py_file in dir_.rglob("*.py"):  # 递归查找所有 .py 文件
            f.write(str(py_file) + "\n")  # 写入文件路径


# 设置源目录和输出文件
source_directory = ROOT.joinpath("src")  # 源目录
output_file = "py_files.txt"  # 输出文件名

find_python_files(source_directory, output_file)
print(f"所有 .py 文件路径已保存到 {output_file}")
```

## File: `locale/po_to_mo.py`
```python
from pathlib import Path
from subprocess import run

ROOT = Path(__file__).resolve().parent


def scan_directory():
    return [
        item.joinpath("LC_MESSAGES/tk.po") for item in ROOT.iterdir() if item.is_dir()
    ]


def generate_map(files: list[Path]):
    return [(i, i.with_suffix(".mo")) for i in files]


def generate_mo(maps: list[tuple[Path, Path]]):
    for i, j in maps:
        command = f'msgfmt --check -o "{j}" "{i}"'
        print(run(command, shell=True, text=True))


if __name__ == "__main__":
    generate_mo(generate_map(scan_directory()))
```

## File: `locale/README.md`
```markdown
# 命令参考

**运行命令前，确保已经安装了 `gettext` 软件包，并配置好环境变量。**

**Before running the command, ensure that the `gettext` package is installed and the environment variables are properly
configured.**

* `xgettext --files-from=py_files.txt -d tk -o tk.pot`
* `mkdir zh_CN\LC_MESSAGES`
* `msginit -l zh_CN -o zh_CN/LC_MESSAGES/tk.po -i tk.pot`
* `mkdir en_US\LC_MESSAGES`
* `msginit -l en_US -o en_US/LC_MESSAGES/tk.po -i tk.pot`
* `msgmerge -U zh_CN/LC_MESSAGES/tk.po tk.pot`
* `msgmerge -U en_US/LC_MESSAGES/tk.po tk.pot`

# 翻译贡献指南

* 如果想要贡献支持更多语言，请在终端切换至 `locale` 文件夹，运行命令 `msginit -l 语言代码 -o 语言代码/LC_MESSAGES/tk.po -i tk.pot`
  生成 po 文件并编辑翻译。
* 如果想要贡献改进翻译结果，请直接编辑 `tk.po` 文件内容。
* 仅需提交 `tk.po` 文件，作者会转换格式并合并。

# Translation Contribution Guide

* If you want to contribute support for more languages, please switch to the `locale` folder in the terminal and run the
  command `msginit -l language_code -o language_code/LC_MESSAGES/tk.po -i tk.pot` to generate the po file and edit the
  translation.
* If you want to contribute to improving the translation, please directly edit the content of the `tk.po` file.
* Only the `tk.po` file needs to be submitted, and the author will convert the format and merge it.
```

## File: `locale/tk.pot`
```
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <yonglelolu@foxmail.com>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: DouK-Downloader 5.8\n"
"Report-Msgid-Bugs-To: <yonglelolu@foxmail.com>\n"
"POT-Creation-Date: 2025-11-04 10:48+0800\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <yonglelolu@foxmail.com>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"Language: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_monitor.py:41
msgid ""
"程序会自动检测并提取剪贴板中的抖音和 TikTok 作品链接，并自动下载作品文件；如"
"需关闭，请按下 Ctrl+C，或将剪贴板内容设置为“close”以停止监听！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_monitor.py:129
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:941
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:968
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1288
#, python-brace-format
msgid "{url} 提取作品 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:50
msgid "验证失败！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:106
msgid "访问项目 GitHub 仓库"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:107
msgid "重定向至项目 GitHub 仓库主页"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:108
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:123
msgid "项目"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:115
msgid "测试令牌有效性"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:128
msgid "验证成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:135
msgid "更新项目全局配置"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:145
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:158
msgid "配置"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:156
msgid "获取项目全局配置"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:157
msgid "返回项目全部配置参数"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:166
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:511
msgid "获取分享链接重定向的完整链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:175
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:206
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:233
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:259
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:299
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:342
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:379
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:419
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:449
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:477
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:501
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:190
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:444
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:885
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:961
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\cookie.py:26
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:43
msgid "抖音"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:183
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:528
msgid "请求链接成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:188
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:533
msgid "请求链接失败！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:195
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:540
msgid "获取单个作品数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:216
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:561
msgid "获取账号作品数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:243
msgid "获取合集作品数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:269
msgid "参数错误！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:288
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:622
msgid "获取直播数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:326
msgid "获取作品评论数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:364
msgid "获取评论回复数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:398
msgid "获取综合搜索数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:429
msgid "获取视频搜索数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:459
msgid "获取用户搜索数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:487
msgid "获取直播搜索数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:588
msgid "获取合辑作品数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:656
msgid "搜索结果为空！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:709
msgid "获取数据成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:720
msgid "获取数据失败！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:71
msgid ""
"未设置 storage_format 参数，无法正常使用该功能，详细说明请查阅项目文档！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:86
msgid "抖音 Cookie"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:90
#, python-brace-format
msgid "{tip} 未登录，无法使用该功能，详细说明请查阅项目文档！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:143
msgid "批量下载账号作品(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:147
msgid "批量下载链接作品(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:151
msgid "获取直播拉流地址(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:155
msgid "采集作品评论数据(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:159
msgid "批量下载合集作品(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:163
msgid "采集账号详细数据(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:167
msgid "采集搜索结果数据(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:171
msgid "采集抖音热榜数据(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:176
msgid "批量下载收藏作品(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:180
msgid "批量下载收藏音乐(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:185
msgid "批量下载收藏夹作品(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:189
msgid "批量下载账号作品(TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:193
msgid "批量下载链接作品(TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:197
msgid "批量下载合集作品(TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:201
msgid "获取直播拉流地址(TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:206
msgid "批量下载视频原画(TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:211
msgid "使用 accounts_urls 参数的账号链接(推荐)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:212
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:220
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:236
msgid "手动输入待采集的账号链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:213
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:221
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:237
msgid "从文本文档读取待采集的账号链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:217
msgid "使用 accounts_urls_tiktok 参数的账号链接(推荐)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:224
msgid "使用 mix_urls 参数的合集链接(推荐)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:225
msgid "获取当前账号收藏合集列表"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:226
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:231
msgid "手动输入待采集的合集/作品链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:227
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:232
msgid "从文本文档读取待采集的合集/作品链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:230
msgid "使用 mix_urls_tiktok 参数的合集链接(推荐)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:235
msgid "使用 accounts_urls 参数的账号链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:240
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:244
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:248
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:252
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:256
msgid "手动输入待采集的作品链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:241
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:245
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:249
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:253
msgid "从文本文档读取待采集的作品链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:261
msgid "综合搜索数据采集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:265
msgid "视频搜索数据采集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:269
msgid "用户搜索数据采集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:273
msgid "直播搜索数据采集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:283
#, python-brace-format
msgid "请输入{tip}链接: "
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:296
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:322
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:330
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1821
msgid "请选择账号链接来源"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:300
msgid "已退出批量下载账号作品(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:302
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:415
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:535
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\user.py:25
msgid "账号"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:306
#, python-brace-format
msgid "程序共处理 {0} 个{1}，成功 {2} 个，失败 {3} 个，耗时 {4} 分钟 {5} 秒"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:326
msgid "已退出批量下载账号作品(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:382
#, python-brace-format
msgid "共有 {count} 个账号的作品等待下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:393
#, python-brace-format
msgid ""
"配置文件 {name} 参数的 url {url} 提取 sec_user_id 失败，错误配置：{data}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:434
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:451
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1743
msgid "账号主页"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:438
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:455
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1747
#, python-brace-format
msgid "{url} 提取账号 sec_user_id 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:470
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:508
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1776
msgid "从文本文档提取账号 sec_user_id 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:556
#, python-brace-format
msgid "开始处理第 {index} 个账号"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:558
msgid "开始处理账号"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:571
#, python-brace-format
msgid "{sec_user_id} 获取账号信息失败，请检查 Cookie 登录状态！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:582
msgid ""
"如果账号发布作品均为共创作品且该账号均不是作品作者时，请配置已登录的 Cookie "
"后重新运行程序，其余情况请无视该提示！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:730
msgid "开始提取作品数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:743
msgid "提取账号或合集信息发生错误！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:825
msgid "发布作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:827
msgid "喜欢作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:829
msgid "收藏作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:831
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix.py:35
msgid "合集作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:833
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:89
msgid "收藏夹作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:844
#, python-brace-format
msgid "昵称/标题：{name}；标识：{mark}；ID：{id}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:884
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:918
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1272
msgid "请选择作品链接来源"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:888
msgid "已退出批量下载链接作品(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:898
msgid "已退出批量下载链接作品(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:905
msgid "注意：本功能为实验性功能，依赖第三方 API 服务，可能不稳定或存在限制！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:911
msgid "已退出批量下载视频原画(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:938
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:965
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1283
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail.py:24
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail_tiktok.py:24
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\slides.py:26
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\tiktok_unofficial.py:38
msgid "作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:944
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:971
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1017
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1291
#, python-brace-format
msgid "共提取到 {count} 个作品，开始处理！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:984
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1005
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1014
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1312
msgid "从文本文档提取作品 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1093
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:320
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:323
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:405
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:749
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:434
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:453
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:467
msgid "图集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1095
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:326
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:329
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:456
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:751
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:351
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:365
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:480
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:570
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:102
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\tiktok_unofficial.py:116
msgid "视频"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1105
msgid "程序未检测到有效的 ffmpeg，不支持直播下载功能！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1109
msgid "请选择下载清晰度(输入清晰度或者对应序号，直接回车代表不下载): "
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1116
msgid "未输入有效的清晰度或者序号，跳过下载！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1149
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1164
msgid "直播"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1154
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1171
msgid "获取直播数据失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1158
msgid "已退出获取直播拉流地址(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1167
msgid "{} 提取直播 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1181
msgid "已退出获取直播拉流地址(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1197
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1214
msgid "直播标题:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1198
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1215
msgid "主播昵称:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1199
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1217
msgid "在线观众:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1200
msgid "观看次数:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1202
msgid "当前直播已结束！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1216
msgid "开播时间:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1218
msgid "点赞次数:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1223
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1242
msgid "FLV 拉流地址: "
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1226
msgid "M3U8 拉流地址: "
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1264
msgid "已退出采集作品评论数据(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1276
msgid "已退出采集作品评论数据(抖音)模式)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1363
#, python-brace-format
msgid "作品评论数据已储存至 {filename}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1364
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1374
#, python-brace-format
msgid "作品{id}_评论数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1368
msgid "采集评论数据失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1423
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1434
msgid "请选择合集链接来源"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1427
msgid "已退出批量下载合集作品(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1438
msgid "已退出批量下载合集作品(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1455
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1470
msgid "合集或作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1459
#, python-brace-format
msgid "{url} 获取作品 ID 或合集 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1473
#, python-brace-format
msgid "{url} 获取合集 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1502
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1509
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:150
msgid "收藏合集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1513
#, python-brace-format
msgid "{text}列表："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1518
#, python-brace-format
msgid ""
"请输入需要下载的{item}序号(多个序号使用空格分隔，输入 ALL 下载全部{item})："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1532
#, python-brace-format
msgid "{text}序号输入错误！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1540
msgid "从文本文档提取作品 ID 或合集 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1550
msgid "从文本文档提取合集 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1590
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1650
msgid "合集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1626
#, python-brace-format
msgid ""
"配置文件 {name} 参数的 url {url} 获取作品 ID 或合集 ID 失败，错误配置：{data}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1668
#, python-brace-format
msgid "开始处理第 {index} 个合集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1670
msgid "开始处理合集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1704
msgid "采集合集作品数据失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1730
#, python-brace-format
msgid "配置文件 accounts_urls 参数第 {index} 条数据的 url 无效"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1754
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\cli_edition\write.py:40
msgid "请输入文本文档路径："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1761
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\cli_edition\write.py:47
#, python-brace-format
msgid "{path} 文件读取异常: {error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1764
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\cli_edition\write.py:50
#, python-brace-format
msgid "{path} 文件不存在！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1788
#, python-brace-format
msgid "正在获取账号 {sec_user_id} 的数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1815
msgid "账号数据已保存至文件"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1825
msgid "已退出采集账号详细数据模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1832
#, python-brace-format
msgid "请输入搜索参数；参数之间使用两个空格分隔({field})：\n"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1855
msgid "请选择搜索模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1934
msgid "搜索结果为空"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1956
msgid "搜索数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2023
#, python-brace-format
msgid "搜索数据已保存至 {name}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2032
msgid "已退出采集抖音热榜数据(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2052
#, python-brace-format
msgid "热榜数据_{time}_{name}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2066
#, python-brace-format
msgid "热榜数据已储存至: 热榜数据_{time} + 榜单类型"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2081
msgid "已退出批量下载收藏作品(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2101
msgid "已退出批量下载收藏夹作品(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2126
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:27
msgid "收藏夹"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2137
#, python-brace-format
msgid "配置文件 owner_url 的 url 参数 {url} 无效"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2167
msgid "已退出批量下载收藏音乐(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2175
#, python-brace-format
msgid "程序运行耗时 {minutes} 分钟 {seconds} 秒"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2205
msgid "开始获取收藏数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2215
#, python-brace-format
msgid "{sec_user_id} 获取账号信息失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2248
msgid "开始获取收藏夹数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2301
msgid "请选择采集功能"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:108
msgid "禁用"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:109
msgid "启用"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:112
msgid "从剪贴板读取 Cookie (抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:113
msgid "从浏览器读取 Cookie (抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:115
msgid "从剪贴板读取 Cookie (TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:116
msgid "从浏览器读取 Cookie (TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:117
msgid "终端交互模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:118
msgid "后台监听模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:119
msgid "Web API 模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:120
msgid "Web UI 模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:124
msgid "{}作品下载记录"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:127
msgid "删除作品下载记录"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:129
msgid "{}运行日志记录"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:132
msgid "检查程序版本更新"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:133
msgid "切换语言"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:149
msgid ""
"访问 http://127.0.0.1:5555/docs 或者 http://127.0.0.1:5555/redoc 可以查阅 "
"API 模式说明文档！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:190
msgid "是否已仔细阅读上述免责声明(YES/NO): "
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:224
msgid "项目地址: {}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:225
msgid "项目文档: {}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:226
msgid "开源许可: {}\n"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:248
#, python-brace-format
msgid "检测到新版本: {major}.{minor}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:255
msgid "当前版本为开发版, 可更新至正式版"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:260
msgid "当前已是最新开发版"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:264
msgid "当前已是最新正式版"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:268
msgid "检测新版本失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:280
msgid "DouK-Downloader 功能选项"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:322
msgid "修改设置成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:334
msgid "Cookie 获取教程："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:340
msgid ""
"复制 Cookie 内容至剪贴板后，按回车键确认继续；若输入任意内容并按回车，则取消"
"操作："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:379
msgid "作品下载记录功能已禁用！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:445
msgid "正在关闭程序"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:273
#, python-brace-format
msgid "{name} 参数格式错误"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:366
#, python-brace-format
msgid "root 参数 {root} 不是有效的文件夹路径，程序将使用项目根路径作为储存路径"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:386
#, python-brace-format
msgid ""
"folder_name 参数 {folder_name} 不是有效的文件夹名称，程序将使用默认值："
"Download"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:399
#, python-brace-format
msgid ""
"name_format 参数 {name_format} 设置错误，程序将使用默认值：创建时间 作品类型 "
"账号昵称 作品描述"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:412
#, python-brace-format
msgid ""
"date_format 参数 {date_format} 设置错误，程序将使用默认值：年-月-日 时:分:秒"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:421
#, python-brace-format
msgid "split 参数 {split} 包含非法字符，程序将使用默认值：-"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:451
#, python-brace-format
msgid "{remark}代理参数应为字符串格式，未来不再支持字典格式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:467
#, python-brace-format
msgid "{remark}代理 {proxy} 测试成功"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:474
#, python-brace-format
msgid "{remark}代理 {proxy} 测试超时"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:484
#, python-brace-format
msgid "{remark}代理 {proxy} 测试失败：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:519
#, python-brace-format
msgid "max_pages 参数 {max_pages} 设置错误，程序将使用默认值：99999"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:543
#, python-brace-format
msgid ""
"storage_format 参数 {storage_format} 设置错误，程序默认不会储存任何数据至文件"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:561
msgid "正在更新抖音参数，请稍等..."
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:579
msgid "抖音参数更新完毕！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:583
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:644
msgid "配置文件 cookie 参数未设置，抖音平台功能可能无法正常使用"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:593
msgid "正在更新 TikTok 参数，请稍等..."
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:611
msgid "TikTok 参数更新完毕！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:616
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:667
msgid "配置文件 cookie_tiktok 参数未设置，TikTok 平台功能可能无法正常使用"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:772
#, python-brace-format
msgid "TikTok cookie 缺少 {name} 键值对，请尝试重新写入 cookie"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:1112
#, python-brace-format
msgid "{key} 参数 {value} 设置过小，程序将使用默认值：{default}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:1120
#, python-brace-format
msgid "{key} 参数 {value} 设置错误，程序将使用默认值：{default}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:1133
#, python-brace-format
msgid "live_qualities 参数 {live_qualities} 设置错误"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:157
msgid ""
"创建默认配置文件 settings.json 成功！\n"
"请参考项目文档的快速入门部分，设置 Cookie 后重新运行程序！\n"
"建议根据实际使用需求修改配置文件 settings.json！\n"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:174
msgid "配置文件 settings.json 格式错误，请检查 JSON 格式！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:186
#, python-brace-format
msgid "配置文件 settings.json 缺少参数 {i}，已自动添加该参数！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:204
msgid "保存配置成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:216
#, python-brace-format
msgid "配置文件 {old} 参数已变更为 {new} 参数，请注意修改配置文件！"
msgstr ""

msgid ""
"关于 DouK-Downloader 的 免责声明：\n"
"\n"
"1. 使用者对本项目的使用由使用者自行决定，并自行承担风险。作者对使用者使用本项"
"目所产生的任何损失、责任、或风险概不负责。\n"
"2. 本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。作者按现有技术"
"水平努力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。\n"
"3. 本项目依赖的所有第三方库、插件或服务各自遵循其原始开源或商业许可，使用者需"
"自行查阅并遵守相应协议，作者不对第三方组件的稳定性、安全性及合规性承担任何责"
"任。\n"
"4. 使用者在使用本项目时必须严格遵守 GNU General Public License v3.0 的要求，"
"并在适当的地方注明使用了 GNU General Public License v3.0 的代码。\n"
"5. 使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行"
"为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。\n"
"6. 使用者不得使用本工具从事任何侵犯知识产权的行为，包括但不限于未经授权下载、"
"传播受版权保护的内容，开发者不参与、不支持、不认可任何非法内容的获取或分"
"发。\n"
"7. 本项目不对使用者涉及的数据收集、存储、传输等处理活动的合规性承担责任。使用"
"者应自行遵守相关法律法规，确保处理行为合法正当；因违规操作导致的法律责任由使"
"用者自行承担。\n"
"8. 使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行"
"为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。\n"
"9. 本项目的作者不会提供 DouK-Downloader 项目的付费版本，也不会提供与 DouK-"
"Downloader 项目相关的任何商业服务。\n"
"10. 基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不"
"承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的"
"各种情况负全部责任。\n"
"11. 本项目不授予使用者任何专利许可；若使用本项目导致专利纠纷或侵权，使用者自"
"行承担全部风险和责任。未经作者或权利人书面授权，不得使用本项目进行任何商业宣"
"传、推广或再授权。\n"
"12. 作者保留随时终止向任何违反本声明的使用者提供服务的权利，并可能要求其销毁"
"已获取的代码及衍生作品。\n"
"13. 作者保留在不另行通知的情况下更新本声明的权利，使用者持续使用即视为接受修"
"订后的条款。\n"
"\n"
"在使用本项目的代码和功能之前，请您认真考虑并接受以上免责声明。如果您对上述声"
"明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码"
"和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险"
"和后果。\n"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\custom\function.py:56
#, python-brace-format
msgid ""
"程序连续处理了 {batches} 个数据，为了避免请求频率过高导致账号或 IP 被风控，程"
"序已经暂停运行，将在 {rest_time} 秒后恢复运行！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:159
msgid "开始下载作品文件"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:235
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:343
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:501
msgid "音乐"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:255
msgid "程序将会调用 ffmpeg 下载直播，关闭 DouK-Downloader 不会中断下载！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:332
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:335
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:753
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:422
msgid "实况"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:409
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:460
#, python-brace-format
msgid "【{type}】{name} 提取文件下载地址失败，跳过下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:421
#, python-brace-format
msgid "【{type}】{name} 存在下载记录，跳过下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:428
#, python-brace-format
msgid "【{type}】{name}_{index} 文件已存在，跳过下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:472
#, python-brace-format
msgid "【{type}】{name} 存在下载记录或文件已存在，跳过下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:514
#, python-brace-format
msgid "【{type}】{name}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:622
msgid "文件缓存异常，尝试重新下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:660
#, python-brace-format
msgid "网络异常: {error_repr}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:664
#, python-brace-format
msgid "响应码异常: {error_repr}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:668
msgid ""
"如果 TikTok 平台作品下载功能异常，请检查配置文件中 browser_info_tiktok 的 "
"device_id 参数！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:679
#, python-brace-format
msgid "下载文件时发生预期之外的错误，请向作者反馈，错误信息: {error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:715
#, python-brace-format
msgid "{show} 下载中断，错误信息：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:721
#, python-brace-format
msgid "{show} 文件下载成功"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:785
#, python-brace-format
msgid "UID{id_}_{name}_发布作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:787
#, python-brace-format
msgid "UID{id_}_{name}_喜欢作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:789
#, python-brace-format
msgid "MID{id_}_{name}_合集作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:791
#, python-brace-format
msgid "UID{id_}_{name}_收藏作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:793
#, python-brace-format
msgid "CID{id_}_{name}_收藏夹作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:850
#, python-brace-format
msgid "{file_name} 文件已删除"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:854
#, python-brace-format
msgid "下载视频作品 {downloaded_video_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:859
#, python-brace-format
msgid "跳过视频作品 {skipped_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:864
#, python-brace-format
msgid "下载图集作品 {downloaded_image_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:869
#, python-brace-format
msgid "跳过图集作品 {skipped_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:874
#, python-brace-format
msgid "下载实况作品 {downloaded_image_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:879
#, python-brace-format
msgid "跳过实况作品 {skipped_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:957
#, python-brace-format
msgid "未收录的文件类型：{content}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:967
#, python-brace-format
msgid "{show} 响应内容为空"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:976
#, python-brace-format
msgid "{show} 文件大小超出限制，跳过下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\msToken.py:108
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\ttWid.py:42
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\ttWid.py:93
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\webID.py:44
#, python-brace-format
msgid "获取 {name} 参数失败！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:99
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:110
#, python-brace-format
msgid "提取账号信息失败: {data}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:217
#, python-brace-format
msgid "筛选处理后作品数量: {count}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:831
msgid "已注销账号"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:832
msgid "无效账号昵称"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:859
#, python-brace-format
msgid "sec_user_id {user_id} 与 {s} 不一致"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:944
msgid "提取账号信息或合集信息失败，请向作者反馈！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:41
msgid "账号喜欢作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:41
msgid "账号发布作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:68
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:85
msgid ""
"该账号为私密账号，需要使用登录后的 Cookie，且登录的账号需要关注该私密账号"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:207
#, python-brace-format
msgid "tab 参数 {tab} 设置错误，程序将使用默认值: post"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:212
msgid "最早"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:215
msgid "最晚"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:229
#, python-brace-format
msgid "作品{tip}发布日期无效 {date}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:234
#, python-brace-format
msgid "作品{tip}发布日期参数 {date} 类型错误"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:237
#, python-brace-format
msgid "作品{tip}发布日期: {latest_date}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:261
msgid "配置文件 cookie 参数未登录，数据获取已提前结束"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:264
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:200
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail.py:82
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail_tiktok.py:80
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:121
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:391
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:235
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\user.py:64
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\tiktok_unofficial.py:74
#, python-brace-format
msgid "数据解析失败，请告知作者处理: {data}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collection.py:26
msgid "账号收藏作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:58
msgid "当前账号无收藏夹"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:122
#, python-brace-format
msgid "收藏夹 {collects_id} 为空"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:182
msgid "当前账号无收藏合集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:216
msgid "收藏短剧"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:237
msgid "当前账号无收藏短剧"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:270
msgid "收藏音乐"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:291
msgid "当前账号无收藏音乐"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:35
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment_tiktok.py:29
msgid "作品评论"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:77
#, python-brace-format
msgid "作品 {item_id} 无评论"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:105
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:194
#, python-brace-format
msgid "正在获取{text}数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:230
msgid "作品评论回复"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:270
#, python-brace-format
msgid "评论 {comment_id} 无回复"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:18
msgid "抖音热榜"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:23
msgid "娱乐榜"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:28
msgid "社会榜"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:33
msgid "挑战榜"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:52
msgid "热榜"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:87
#, python-brace-format
msgid "{space_name}数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info.py:29
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info_tiktok.py:27
msgid "账号简略"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info.py:64
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info_tiktok.py:57
#, python-brace-format
msgid "获取{text}失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\live_tiktok.py:57
msgid "此直播可能会令部分观众感到不适，请登录后重试！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix.py:71
msgid "获取合集 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix_tiktok.py:32
msgid "合辑作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix_tiktok.py:92
msgid "账号合辑数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:18
msgid "综合搜索"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:25
msgid "视频搜索"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:32
msgid "用户搜索"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:39
msgid "直播搜索"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:60
msgid "关键词  总页数  排序依据  发布时间  视频时长  搜索范围  内容形式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:61
msgid "关键词  总页数  排序依据  发布时间  视频时长  搜索范围"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:62
msgid "关键词  总页数  粉丝数量  用户类型"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:63
msgid "关键词  总页数"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:72
msgid "综合排序"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:73
msgid "最多点赞"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:74
msgid "最新发布"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:77
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:89
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:95
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:101
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:114
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:128
msgid "不限"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:78
msgid "一天内"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:79
msgid "一周内"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:80
msgid "半年内"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:90
msgid "一分钟以内"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:91
msgid "一到五分钟"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:92
msgid "五分钟以上"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:96
msgid "最近看过"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:97
msgid "还未看过"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:98
msgid "关注的人"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:103
msgid "图文"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:115
msgid "1000以下"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:119
msgid "100w以上"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:129
msgid "普通用户"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:130
msgid "企业认证"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:131
msgid "个人认证"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:176
#, python-brace-format
msgid "获取{self_text}数据失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:444
#, python-brace-format
msgid "共获取到 {count} 个{text}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:112
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:131
msgid "文件夹"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:208
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:218
msgid "文件"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:225
#, python-brace-format
msgid "{type} {old}被占用，重命名失败: {error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:232
#, python-brace-format
msgid "{type} {new}名称重复，重命名失败: {error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:239
#, python-brace-format
msgid "处理{type} {old}时发生预期之外的错误: {error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\models\search.py:34
msgid "keyword 参数无效"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\cookie.py:42
msgid "当前剪贴板的内容不是有效的 Cookie 内容！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\storage\sqlite.py:83
msgid "更新数据表名称时发生错误，重命名失败，请向作者反馈以便修复问题！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\storage\xlsx.py:62
#, python-brace-format
msgid "数据包含非法字符，保存数据失败：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:80
#, python-brace-format
msgid ""
"读取指定浏览器的 {platform_name} Cookie 并写入配置文件；\n"
"注意：Windows 系统需要以管理员身份运行程序才能读取 Chromium、Chrome、Edge 浏"
"览器 Cookie！\n"
"{options}\n"
"请输入浏览器名称或序号："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:94
msgid "读取 Cookie 成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:102
msgid "Cookie 数据为空！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:105
msgid "未选择浏览器！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:117
msgid "浏览器名称或序号输入错误！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:125
msgid "读取 Cookie 失败，未找到 Cookie 数据！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:164
msgid "从浏览器读取 Cookie 功能不支持当前平台！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:26
msgid "响应内容不是有效的 JSON 数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:28
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:50
#, python-brace-format
msgid "响应码异常：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:30
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:37
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:52
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:59
#, python-brace-format
msgid "网络异常：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:32
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:54
#, python-brace-format
msgid "请求超时：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:48
msgid "响应内容不是有效的 JSON 数据，请尝试更新 Cookie！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\cleaner.py:46
msgid "不受支持的操作系统类型，可能无法正常去除非法字符！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\error.py:9
msgid "项目代码错误"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\retry.py:19
#, python-brace-format
msgid "正在进行第 {index} 次重试"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\retry.py:48
msgid ""
"如需重新尝试处理该对象，请关闭所有正在访问该对象的窗口或程序，然后直接按下回"
"车键！\n"
"如需跳过处理该对象，请输入任意字符后按下回车键！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\retry.py:63
msgid "请关闭所有正在访问该对象的窗口或程序，然后按下回车键继续处理！"
msgstr ""

msgid ""
"\n"
"项目默认无需令牌；公开部署时，建议设置令牌以防止恶意请求！\n"
"\n"
"令牌设置位置：`src/custom/function.py` - `is_valid_token()`\n"
msgstr ""

msgid ""
"\n"
"更新项目配置文件 settings.json\n"
"\n"
"仅需传入需要更新的配置参数\n"
"\n"
"返回更新后的全部配置参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **text**: 包含分享链接的字符串；必需参数\n"
"- **proxy**: 代理；可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: 抖音作品 ID；必需参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **sec_user_id**: 抖音账号 sec_uid；必需参数\n"
"- **tab**: 账号页面类型；可选参数，默认值：`post`\n"
"- **earliest**: 作品最早发布日期；可选参数\n"
"- **latest**: 作品最晚发布日期；可选参数\n"
"- **pages**: 最大请求次数，仅对请求账号喜欢页数据有效；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **mix_id**: 抖音合集 ID\n"
"- **detail_id**: 属于合集的抖音作品 ID\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
"\n"
"**`mix_id` 和 `detail_id` 二选一，只需传入其中之一即可**\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **web_rid**: 抖音直播 web_rid\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **web_rid**: 抖音直播 web_rid\n"
"- **room_id**: 抖音直播 room_id\n"
"- **sec_user_id**: 抖音直播账号 sec_user_id\n"
"\n"
"**本接口支持两种参数传入方式**:\n"
"\n"
"- 方式一 ：传入 `web_rid`\n"
"- 方式二 ：同时传入 `room_id` 和 `sec_user_id`\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: 抖音作品 ID；必需参数\n"
"- **pages**: 最大请求次数；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
"- **count_reply**: 可选参数\n"
"- **reply**: 可选参数，默认值：False\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: 抖音作品 ID；必需参数\n"
"- **comment_id**: 评论 ID；必需参数\n"
"- **pages**: 最大请求次数；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
"- **sort_type**: 排序依据；可选参数\n"
"- **publish_time**: 发布时间；可选参数\n"
"- **duration**: 视频时长；可选参数\n"
"- **search_range**: 搜索范围；可选参数\n"
"- **content_type**: 内容形式；可选参数\n"
"\n"
"**部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
"- **sort_type**: 排序依据；可选参数\n"
"- **publish_time**: 发布时间；可选参数\n"
"- **duration**: 视频时长；可选参数\n"
"- **search_range**: 搜索范围；可选参数\n"
"\n"
"**部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
"- **douyin_user_fans**: 粉丝数量；可选参数\n"
"- **douyin_user_type**: 用户类型；可选参数\n"
"\n"
"**部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: TikTok 作品 ID；必需参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **sec_user_id**: TikTok 账号 secUid；必需参数\n"
"- **tab**: 账号页面类型；可选参数，默认值：`post`\n"
"- **earliest**: 作品最早发布日期；可选参数\n"
"- **latest**: 作品最晚发布日期；可选参数\n"
"- **pages**: 最大请求次数，仅对请求账号喜欢页数据有效；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **mix_id**: TikTok 合集 ID；必需参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **room_id**: TikTok 直播 room_id；必需参数\n"
msgstr ""
```

## File: `locale/en_US/LC_MESSAGES/tk.po`
```
# English translations for DouK-Downloader package.
# Copyright (C) 2024 THE DouK-Downloader'S COPYRIGHT HOLDER
# This file is distributed under the same license as the DouK-Downloader package.
# FIRST AUTHOR <yonglelolu@foxmail.com>, 2024.
#
msgid ""
msgstr ""
"Project-Id-Version: DouK-Downloader 5.8\n"
"Report-Msgid-Bugs-To: <yonglelolu@foxmail.com>\n"
"POT-Creation-Date: 2025-11-04 10:48+0800\n"
"PO-Revision-Date: 2024-12-22 21:46+0800\n"
"Last-Translator: <yonglelolu@foxmail.com>\n"
"Language-Team: English\n"
"Language: en_US\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=1; plural=0;\n"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_monitor.py:41
msgid ""
"程序会自动检测并提取剪贴板中的抖音和 TikTok 作品链接，并自动下载作品文件；如"
"需关闭，请按下 Ctrl+C，或将剪贴板内容设置为“close”以停止监听！"
msgstr ""
"The program will automatically detect and extract TikTok and DouYin video "
"links from the clipboard, then download the video files. To turn it off, "
"press Ctrl+C or set the clipboard content to \"close\" to stop monitoring!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_monitor.py:129
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:941
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:968
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1288
#, python-brace-format
msgid "{url} 提取作品 ID 失败"
msgstr "Failed to extract works ID from {url}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:50
msgid "验证失败！"
msgstr "Verification failed!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:106
msgid "访问项目 GitHub 仓库"
msgstr "Visit the project's GitHub repository"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:107
msgid "重定向至项目 GitHub 仓库主页"
msgstr "Redirect to the project's GitHub repository homepage"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:108
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:123
msgid "项目"
msgstr "Project"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:115
msgid "测试令牌有效性"
msgstr "Test token validity"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:128
msgid "验证成功！"
msgstr "Verification successful!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:135
msgid "更新项目全局配置"
msgstr "Update project global configuration"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:145
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:158
msgid "配置"
msgstr "Configuration"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:156
msgid "获取项目全局配置"
msgstr "Retrieve project global configuration"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:157
msgid "返回项目全部配置参数"
msgstr "Return all configuration parameters of the project"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:166
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:511
msgid "获取分享链接重定向的完整链接"
msgstr "Retrieve the complete link for the shared link redirect"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:175
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:206
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:233
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:259
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:299
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:342
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:379
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:419
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:449
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:477
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:501
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:190
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:444
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:885
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:961
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\cookie.py:26
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:43
msgid "抖音"
msgstr "DouYin"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:183
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:528
msgid "请求链接成功！"
msgstr "Request link successful!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:188
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:533
msgid "请求链接失败！"
msgstr "Request link failed!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:195
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:540
msgid "获取单个作品数据"
msgstr "Retrieve data for a single works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:216
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:561
msgid "获取账号作品数据"
msgstr "Retrieve account works data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:243
msgid "获取合集作品数据"
msgstr "Retrieve mix works data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:269
msgid "参数错误！"
msgstr "Parameter error!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:288
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:622
msgid "获取直播数据"
msgstr "Retrieve live stream data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:326
msgid "获取作品评论数据"
msgstr "Retrieve work comments data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:364
msgid "获取评论回复数据"
msgstr "Retrieve comment replies data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:398
msgid "获取综合搜索数据"
msgstr "Retrieve general search data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:429
msgid "获取视频搜索数据"
msgstr "Retrieve video search data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:459
msgid "获取用户搜索数据"
msgstr "Retrieve user search data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:487
msgid "获取直播搜索数据"
msgstr "Retrieve live search data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:588
msgid "获取合辑作品数据"
msgstr "Retrieve mix works data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:656
msgid "搜索结果为空！"
msgstr "The search result is empty!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:709
msgid "获取数据成功！"
msgstr "Successfully retrieved data!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:720
msgid "获取数据失败！"
msgstr "Failed to retrieve data!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:71
msgid ""
"未设置 storage_format 参数，无法正常使用该功能，详细说明请查阅项目文档！"
msgstr ""
"The `storage_format` parameter is not set, so this feature cannot be used "
"properly. Please refer to the project documentation for detailed information!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:86
msgid "抖音 Cookie"
msgstr "DouYin Cookie"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:90
#, python-brace-format
msgid "{tip} 未登录，无法使用该功能，详细说明请查阅项目文档！"
msgstr ""
"{tip} Not logged in, unable to use this feature. Please refer to the project "
"documentation for detailed information!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:143
msgid "批量下载账号作品(抖音)"
msgstr "Batch Download Account Works (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:147
msgid "批量下载链接作品(抖音)"
msgstr "Batch Download Works from Links (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:151
msgid "获取直播拉流地址(抖音)"
msgstr "Get live stream pull URL (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:155
msgid "采集作品评论数据(抖音)"
msgstr "Collect Works Comment Data (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:159
msgid "批量下载合集作品(抖音)"
msgstr "Batch Download Mix Works (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:163
msgid "采集账号详细数据(抖音)"
msgstr "Collect Account Detailed Data (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:167
msgid "采集搜索结果数据(抖音)"
msgstr "Collect Search Result Data (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:171
msgid "采集抖音热榜数据(抖音)"
msgstr "Collect DouYin Hot Board Data (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:176
msgid "批量下载收藏作品(抖音)"
msgstr "Batch Download Favorites Works (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:180
msgid "批量下载收藏音乐(抖音)"
msgstr "Batch Download Favorites Music (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:185
msgid "批量下载收藏夹作品(抖音)"
msgstr "Batch Download Collections Works (DouYin)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:189
msgid "批量下载账号作品(TikTok)"
msgstr "Batch Download Account Works (TikTok)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:193
msgid "批量下载链接作品(TikTok)"
msgstr "Batch Download Works from Links (TikTok)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:197
msgid "批量下载合集作品(TikTok)"
msgstr "Batch Download Mix Works (TikTok)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:201
msgid "获取直播拉流地址(TikTok)"
msgstr "Get live stream pull URL (TikTok)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:206
msgid "批量下载视频原画(TikTok)"
msgstr "Batch Download Video original file (TikTok)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:211
msgid "使用 accounts_urls 参数的账号链接(推荐)"
msgstr "Account links using the `accounts_urls` parameter (recommended)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:212
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:220
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:236
msgid "手动输入待采集的账号链接"
msgstr "Manually enter the account links to be collected"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:213
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:221
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:237
msgid "从文本文档读取待采集的账号链接"
msgstr "Read account links to be collected from a text file"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:217
msgid "使用 accounts_urls_tiktok 参数的账号链接(推荐)"
msgstr "Account links using the `accounts_urls_tiktok` parameter (recommended)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:224
msgid "使用 mix_urls 参数的合集链接(推荐)"
msgstr "Mix links using the `mix_urls` parameter (recommended)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:225
msgid "获取当前账号收藏合集列表"
msgstr "Retrieve the current account's Collections Mix list"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:226
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:231
msgid "手动输入待采集的合集/作品链接"
msgstr "Manually enter the Mix/Works links to be collected"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:227
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:232
msgid "从文本文档读取待采集的合集/作品链接"
msgstr "Read the Mix/Works links to be collected from a text file"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:230
msgid "使用 mix_urls_tiktok 参数的合集链接(推荐)"
msgstr "Mix links using the `mix_urls_tiktok` parameter (recommended)"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:235
msgid "使用 accounts_urls 参数的账号链接"
msgstr "Account links using the `accounts_urls` parameter"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:240
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:244
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:248
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:252
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:256
msgid "手动输入待采集的作品链接"
msgstr "Manually enter the works links to be collected"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:241
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:245
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:249
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:253
msgid "从文本文档读取待采集的作品链接"
msgstr "Read the works links to be collected from a text file"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:261
msgid "综合搜索数据采集"
msgstr "General Search"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:265
msgid "视频搜索数据采集"
msgstr "Video Search"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:269
msgid "用户搜索数据采集"
msgstr "User Search"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:273
msgid "直播搜索数据采集"
msgstr "Live Search"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:283
#, python-brace-format
msgid "请输入{tip}链接: "
msgstr "Please enter the {tip} link:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:296
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:322
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:330
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1821
msgid "请选择账号链接来源"
msgstr "Please select the account link source"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:300
msgid "已退出批量下载账号作品(TikTok)模式"
msgstr "Exited Batch Download Account Works (TikTok) mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:302
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:415
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:535
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\user.py:25
msgid "账号"
msgstr "Account"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:306
#, python-brace-format
msgid "程序共处理 {0} 个{1}，成功 {2} 个，失败 {3} 个，耗时 {4} 分钟 {5} 秒"
msgstr ""
"The program processed a total of {0} {1}, with {2} successes, {3} failures, "
"and a duration of {4} minutes {5} seconds."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:326
msgid "已退出批量下载账号作品(抖音)模式"
msgstr "Exited Batch Download Account Works (DouYin) mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:382
#, python-brace-format
msgid "共有 {count} 个账号的作品等待下载"
msgstr "There are {count} accounts' works waiting to be downloaded"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:393
#, python-brace-format
msgid ""
"配置文件 {name} 参数的 url {url} 提取 sec_user_id 失败，错误配置：{data}"
msgstr ""
"Failed to extract sec_user_id from the url {url} in the configuration file "
"{name}, error configuration: {data}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:434
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:451
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1743
msgid "账号主页"
msgstr "Account Page"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:438
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:455
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1747
#, python-brace-format
msgid "{url} 提取账号 sec_user_id 失败"
msgstr "Failed to extract account sec_user_id from {url}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:470
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:508
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1776
msgid "从文本文档提取账号 sec_user_id 失败"
msgstr "Failed to extract account sec_user_id from the text file"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:556
#, python-brace-format
msgid "开始处理第 {index} 个账号"
msgstr "Start processing the {index}th account"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:558
msgid "开始处理账号"
msgstr "Starting to process the account"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:571
#, python-brace-format
msgid "{sec_user_id} 获取账号信息失败，请检查 Cookie 登录状态！"
msgstr ""
"Failed to retrieve account information for {sec_user_id}, please check the "
"Cookie login status!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:582
msgid ""
"如果账号发布作品均为共创作品且该账号均不是作品作者时，请配置已登录的 Cookie "
"后重新运行程序，其余情况请无视该提示！"
msgstr ""
"If all works published by the account are co-created works and the account "
"is not the author of any work, please configure a logged-in Cookie and run "
"the program again. Ignore this message in all other cases!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:730
msgid "开始提取作品数据"
msgstr "Starting to extract works data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:743
msgid "提取账号或合集信息发生错误！"
msgstr "An error occurred while extracting account or collection information!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:825
msgid "发布作品"
msgstr "Posts"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:827
msgid "喜欢作品"
msgstr "Liked"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:829
msgid "收藏作品"
msgstr "Favorites"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:831
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix.py:35
msgid "合集作品"
msgstr "Mix"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:833
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:89
msgid "收藏夹作品"
msgstr "Collections"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:844
#, python-brace-format
msgid "昵称/标题：{name}；标识：{mark}；ID：{id}"
msgstr "Nickname/Title: {name}; Mark: {mark}; ID: {id}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:884
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:918
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1272
msgid "请选择作品链接来源"
msgstr "Please select the works link source"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:888
msgid "已退出批量下载链接作品(抖音)模式"
msgstr "Exited Batch Download Works from Links (DouYin) mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:898
msgid "已退出批量下载链接作品(TikTok)模式"
msgstr "Exited Batch Download Works from Links (TikTok) mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:905
msgid "注意：本功能为实验性功能，依赖第三方 API 服务，可能不稳定或存在限制！"
msgstr ""
"Note: This feature is experimental and relies on unofficial API services, "
"which may be unstable or have limitations!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:911
msgid "已退出批量下载视频原画(TikTok)模式"
msgstr "Exited Batch Download Video original file (TikTok) mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:938
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:965
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1283
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail.py:24
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail_tiktok.py:24
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\slides.py:26
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\tiktok_unofficial.py:38
msgid "作品"
msgstr "Works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:944
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:971
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1017
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1291
#, python-brace-format
msgid "共提取到 {count} 个作品，开始处理！"
msgstr "Successfully extracted {count} works, starting to process!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:984
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1005
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1014
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1312
msgid "从文本文档提取作品 ID 失败"
msgstr "Failed to extract works ID from the text file"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1093
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:320
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:323
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:405
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:749
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:434
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:453
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:467
msgid "图集"
msgstr "Image"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1095
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:326
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:329
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:456
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:751
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:351
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:365
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:480
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:570
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:102
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\tiktok_unofficial.py:116
msgid "视频"
msgstr "Video"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1105
msgid "程序未检测到有效的 ffmpeg，不支持直播下载功能！"
msgstr ""
"The program did not detect a valid ffmpeg tool, live streaming download "
"functionality is not supported!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1109
msgid "请选择下载清晰度(输入清晰度或者对应序号，直接回车代表不下载): "
msgstr ""
"Please select the download resolution (enter the resolution or corresponding "
"number, press Enter to skip download):"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1116
msgid "未输入有效的清晰度或者序号，跳过下载！"
msgstr "No valid resolution or serial number entered, skipping download!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1149
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1164
msgid "直播"
msgstr "Live"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1154
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1171
msgid "获取直播数据失败"
msgstr "Failed to retrieve live stream data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1158
msgid "已退出获取直播拉流地址(抖音)模式"
msgstr "Exited Get DouYin live stream pull URL mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1167
msgid "{} 提取直播 ID 失败"
msgstr "Failed to extract live stream ID from {}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1181
msgid "已退出获取直播拉流地址(TikTok)模式"
msgstr "Exited Get TikTok live stream pull URL mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1197
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1214
msgid "直播标题:"
msgstr "Live Stream Title:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1198
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1215
msgid "主播昵称:"
msgstr "Presenter Nickname:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1199
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1217
msgid "在线观众:"
msgstr "Online Viewers:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1200
msgid "观看次数:"
msgstr "View Count:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1202
msgid "当前直播已结束！"
msgstr "The current live stream has ended!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1216
msgid "开播时间:"
msgstr "Start Time:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1218
msgid "点赞次数:"
msgstr "Like Count:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1223
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1242
msgid "FLV 拉流地址: "
msgstr "FLV Stream push URL:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1226
msgid "M3U8 拉流地址: "
msgstr "M3U8 Stream push URL:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1264
msgid "已退出采集作品评论数据(TikTok)模式"
msgstr "Exited Collect Works Comment Data (TikTok) mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1276
msgid "已退出采集作品评论数据(抖音)模式)"
msgstr "Exited Collect Works Comment Data (DouYin) mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1363
#, python-brace-format
msgid "作品评论数据已储存至 {filename}"
msgstr "Works comment data has been saved to {filename}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1364
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1374
#, python-brace-format
msgid "作品{id}_评论数据"
msgstr "Works{id}_CommentData"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1368
msgid "采集评论数据失败"
msgstr "Failed to collect comment data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1423
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1434
msgid "请选择合集链接来源"
msgstr "Please select the Mix link source"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1427
msgid "已退出批量下载合集作品(抖音)模式"
msgstr "Exited Batch Download Mix Works (DouYin) mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1438
msgid "已退出批量下载合集作品(TikTok)模式"
msgstr "Exited Batch Download Mix Works (TikTok) mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1455
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1470
msgid "合集或作品"
msgstr "Mix or Works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1459
#, python-brace-format
msgid "{url} 获取作品 ID 或合集 ID 失败"
msgstr "Failed to retrieve Works ID or Mix ID from {url}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1473
#, python-brace-format
msgid "{url} 获取合集 ID 失败"
msgstr "Failed to retrieve Mix ID from {url}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1502
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1509
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:150
msgid "收藏合集"
msgstr "Collections Mix"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1513
#, python-brace-format
msgid "{text}列表："
msgstr "{text} List:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1518
#, python-brace-format
msgid ""
"请输入需要下载的{item}序号(多个序号使用空格分隔，输入 ALL 下载全部{item})："
msgstr ""
"Please enter the serial numbers of the {item} to download (separate multiple "
"numbers with spaces, enter ALL to download all {item}):"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1532
#, python-brace-format
msgid "{text}序号输入错误！"
msgstr "Incorrect {text} serial number input!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1540
msgid "从文本文档提取作品 ID 或合集 ID 失败"
msgstr "Failed to extract Works ID or Mix ID from the text file"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1550
msgid "从文本文档提取合集 ID 失败"
msgstr "Failed to extract Mix ID from the text file"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1590
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1650
msgid "合集"
msgstr "Mix"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1626
#, python-brace-format
msgid ""
"配置文件 {name} 参数的 url {url} 获取作品 ID 或合集 ID 失败，错误配置：{data}"
msgstr ""
"Failed to obtain the work ID or collection ID from the url {url} in the "
"configuration file {name}, error configuration: {data}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1668
#, python-brace-format
msgid "开始处理第 {index} 个合集"
msgstr "Starting to process the {index}th Mix"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1670
msgid "开始处理合集"
msgstr "Starting to process the Mix"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1704
msgid "采集合集作品数据失败"
msgstr "Failed to collect Mix Works data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1730
#, python-brace-format
msgid "配置文件 accounts_urls 参数第 {index} 条数据的 url 无效"
msgstr ""
"The URL in parameter {index} of the `accounts_urls` in the configuration "
"file is invalid"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1754
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\cli_edition\write.py:40
msgid "请输入文本文档路径："
msgstr "Please enter the text file path:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1761
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\cli_edition\write.py:47
#, python-brace-format
msgid "{path} 文件读取异常: {error}"
msgstr "File read error at {path}: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1764
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\cli_edition\write.py:50
#, python-brace-format
msgid "{path} 文件不存在！"
msgstr "The file {path} does not exist!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1788
#, python-brace-format
msgid "正在获取账号 {sec_user_id} 的数据"
msgstr "正在获取账号 {sec_user_id} 的数据"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1815
msgid "账号数据已保存至文件"
msgstr "Account data has been saved to the file."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1825
msgid "已退出采集账号详细数据模式"
msgstr "Exited Collect Account Detailed Data mode."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1832
#, python-brace-format
msgid "请输入搜索参数；参数之间使用两个空格分隔({field})：\n"
msgstr ""
"Please enter search parameters; Separate parameters with two spaces "
"({field}): \n"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1855
msgid "请选择搜索模式"
msgstr "Please choose a search mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1934
msgid "搜索结果为空"
msgstr "The search result is empty"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1956
msgid "搜索数据"
msgstr "Search_Data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2023
#, python-brace-format
msgid "搜索数据已保存至 {name}"
msgstr "Search data has been saved to {name}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2032
msgid "已退出采集抖音热榜数据(抖音)模式"
msgstr "Exited Collect DouYin Hot Board Data mode."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2052
#, python-brace-format
msgid "热榜数据_{time}_{name}"
msgstr "HotBoardData_{time}_{name}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2066
#, python-brace-format
msgid "热榜数据已储存至: 热榜数据_{time} + 榜单类型"
msgstr "Hot Board Data has been saved to: HotBoardData_{time} + Board Type"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2081
msgid "已退出批量下载收藏作品(抖音)模式"
msgstr "Exited Batch Download Favorites Works (DouYin) mode."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2101
msgid "已退出批量下载收藏夹作品(抖音)模式"
msgstr "Exited Batch Download Collections Works (DouYin) mode."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2126
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:27
msgid "收藏夹"
msgstr "Collections"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2137
#, python-brace-format
msgid "配置文件 owner_url 的 url 参数 {url} 无效"
msgstr ""
"The URL parameter {url} of owner_url in the configuration file is invalid."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2167
msgid "已退出批量下载收藏音乐(抖音)模式"
msgstr "Exited Batch Download Collections Music (DouYin) mode."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2175
#, python-brace-format
msgid "程序运行耗时 {minutes} 分钟 {seconds} 秒"
msgstr "The program ran for {minutes} minutes {seconds} seconds"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2205
msgid "开始获取收藏数据"
msgstr "Starting to retrieve Favorites data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2215
#, python-brace-format
msgid "{sec_user_id} 获取账号信息失败"
msgstr "Failed to retrieve account information for {sec_user_id}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2248
msgid "开始获取收藏夹数据"
msgstr "Starting to retrieve Collections data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2301
msgid "请选择采集功能"
msgstr "Please select the function menu"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:108
msgid "禁用"
msgstr "Disable"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:109
msgid "启用"
msgstr "Enable"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:112
msgid "从剪贴板读取 Cookie (抖音)"
msgstr "Extracting cookie (DouYin) from clipboard"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:113
msgid "从浏览器读取 Cookie (抖音)"
msgstr "Extracting cookie (DouYin) from browser"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:115
msgid "从剪贴板读取 Cookie (TikTok)"
msgstr "Extracting cookie (TikTok) from clipboard"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:116
msgid "从浏览器读取 Cookie (TikTok)"
msgstr "Extracting cookie (TikTok) from browser"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:117
msgid "终端交互模式"
msgstr "Terminal Mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:118
msgid "后台监听模式"
msgstr "Monitoring Mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:119
msgid "Web API 模式"
msgstr "Web API Mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:120
msgid "Web UI 模式"
msgstr "Web UI Mode"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:124
msgid "{}作品下载记录"
msgstr "{} Works Download History"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:127
msgid "删除作品下载记录"
msgstr "Delete Works Download History"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:129
msgid "{}运行日志记录"
msgstr "{} Run Log History"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:132
msgid "检查程序版本更新"
msgstr "Check for Program Version Updates"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:133
msgid "切换语言"
msgstr "切换到简体中文"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:149
msgid ""
"访问 http://127.0.0.1:5555/docs 或者 http://127.0.0.1:5555/redoc 可以查阅 "
"API 模式说明文档！"
msgstr ""
"Visit http://127.0.0.1:5555/docs or http://127.0.0.1:5555/redoc to view the "
"API mode documentation!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:190
msgid "是否已仔细阅读上述免责声明(YES/NO): "
msgstr "Have you carefully read the above disclaimer (YES/NO):"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:224
msgid "项目地址: {}"
msgstr "Project URL: {}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:225
msgid "项目文档: {}"
msgstr "Project Documentation: {}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:226
msgid "开源许可: {}\n"
msgstr "Open Source License: {}\n"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:248
#, python-brace-format
msgid "检测到新版本: {major}.{minor}"
msgstr "New version detected: {major}.{minor}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:255
msgid "当前版本为开发版, 可更新至正式版"
msgstr ""
"The current version is a development version, update to the stable version."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:260
msgid "当前已是最新开发版"
msgstr "The current version is the latest development version."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:264
msgid "当前已是最新正式版"
msgstr "The current version is the latest stable version."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:268
msgid "检测新版本失败"
msgstr "Failed to check for new version."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:280
msgid "DouK-Downloader 功能选项"
msgstr "DouK-Downloader Feature Options"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:322
msgid "修改设置成功！"
msgstr "Settings updated successfully!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:334
msgid "Cookie 获取教程："
msgstr "Cookie retrieval tutorial:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:340
msgid ""
"复制 Cookie 内容至剪贴板后，按回车键确认继续；若输入任意内容并按回车，则取消"
"操作："
msgstr ""
"After pasting the cookie into the clipboard, press Enter to proceed. Enter "
"any text + Enter to abort."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:379
msgid "作品下载记录功能已禁用！"
msgstr "Works download history feature is disabled!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:445
msgid "正在关闭程序"
msgstr "Shutting down the program"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:273
#, python-brace-format
msgid "{name} 参数格式错误"
msgstr "{name} parameter format error"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:366
#, python-brace-format
msgid "root 参数 {root} 不是有效的文件夹路径，程序将使用项目根路径作为储存路径"
msgstr ""
"The root parameter {root} is not a valid folder path. The program will use "
"the project root path as the storage path."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:386
#, python-brace-format
msgid ""
"folder_name 参数 {folder_name} 不是有效的文件夹名称，程序将使用默认值："
"Download"
msgstr ""
"folder_name parameter {folder_name} is not a valid folder name. The program "
"will use the default value: Download"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:399
#, python-brace-format
msgid ""
"name_format 参数 {name_format} 设置错误，程序将使用默认值：创建时间 作品类型 "
"账号昵称 作品描述"
msgstr ""
"name_format parameter {name_format} is set incorrectly. The program will use "
"the default value: Time, Type, Nickname, Description"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:412
#, python-brace-format
msgid ""
"date_format 参数 {date_format} 设置错误，程序将使用默认值：年-月-日 时:分:秒"
msgstr ""
"date_format parameter {date_format} is set incorrectly. The program will use "
"the default value: Year-Month-Day Hour:Minute:Second"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:421
#, python-brace-format
msgid "split 参数 {split} 包含非法字符，程序将使用默认值：-"
msgstr ""
"split parameter {split} contains illegal characters. The program will use "
"the default value: -"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:451
#, python-brace-format
msgid "{remark}代理参数应为字符串格式，未来不再支持字典格式"
msgstr ""
"{remark} proxy parameter should be in string format. Dictionary format will "
"no longer be supported in the future."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:467
#, python-brace-format
msgid "{remark}代理 {proxy} 测试成功"
msgstr "{remark} proxy {proxy} test successful."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:474
#, python-brace-format
msgid "{remark}代理 {proxy} 测试超时"
msgstr "{remark} proxy {proxy} test timed out."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:484
#, python-brace-format
msgid "{remark}代理 {proxy} 测试失败：{error}"
msgstr "{remark} proxy {proxy} test failed: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:519
#, python-brace-format
msgid "max_pages 参数 {max_pages} 设置错误，程序将使用默认值：99999"
msgstr ""
"max_pages parameter {max_pages} is set incorrectly. The program will use the "
"default value: 99999"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:543
#, python-brace-format
msgid ""
"storage_format 参数 {storage_format} 设置错误，程序默认不会储存任何数据至文件"
msgstr ""
"The storage_format parameter {storage_format} is set incorrectly. By "
"default, the program will not store any data to files."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:561
msgid "正在更新抖音参数，请稍等..."
msgstr "Updating DouYin parameters, please wait..."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:579
msgid "抖音参数更新完毕！"
msgstr "DouYin parameters update completed!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:583
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:644
msgid "配置文件 cookie 参数未设置，抖音平台功能可能无法正常使用"
msgstr ""
"The cookie parameter is not configured in the settings file. DouYin platform "
"features may not work properly."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:593
msgid "正在更新 TikTok 参数，请稍等..."
msgstr "Updating TikTok parameters, please wait..."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:611
msgid "TikTok 参数更新完毕！"
msgstr "TikTok parameters update completed!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:616
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:667
msgid "配置文件 cookie_tiktok 参数未设置，TikTok 平台功能可能无法正常使用"
msgstr ""
"The cookie_tiktok parameter is not configured in the settings file. TikTok "
"platform features may not work properly."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:772
#, python-brace-format
msgid "TikTok cookie 缺少 {name} 键值对，请尝试重新写入 cookie"
msgstr ""
"The TikTok cookie is missing the {name} key-value pair. Please attempt to "
"rewrite the cookie."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:1112
#, python-brace-format
msgid "{key} 参数 {value} 设置过小，程序将使用默认值：{default}"
msgstr ""
"The parameter {key} has been set to a value ({value}) that is too small. The "
"program will use the default value instead: {default}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:1120
#, python-brace-format
msgid "{key} 参数 {value} 设置错误，程序将使用默认值：{default}"
msgstr ""
"The parameter {key} is incorrectly configured ({value}). The program will "
"use the default value: {default}."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:1133
#, python-brace-format
msgid "live_qualities 参数 {live_qualities} 设置错误"
msgstr ""
"The live_qualities parameter is incorrectly configured: {live_qualities}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:157
msgid ""
"创建默认配置文件 settings.json 成功！\n"
"请参考项目文档的快速入门部分，设置 Cookie 后重新运行程序！\n"
"建议根据实际使用需求修改配置文件 settings.json！\n"
msgstr ""
"Default configuration file settings.json created successfully!\n"
"Please refer to the quick start section of the project documentation, set "
"the Cookie, and rerun the program!\n"
"It is recommended to modify the settings.json file according to your actual "
"usage needs!\n"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:174
msgid "配置文件 settings.json 格式错误，请检查 JSON 格式！"
msgstr ""
"The configuration file settings.json has an error. Please check the JSON "
"format!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:186
#, python-brace-format
msgid "配置文件 settings.json 缺少参数 {i}，已自动添加该参数！"
msgstr ""
"The configuration file settings.json is missing the parameter \"{i}\". The "
"program has automatically added this parameter."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:204
msgid "保存配置成功！"
msgstr "Configuration saved successfully!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:216
#, python-brace-format
msgid "配置文件 {old} 参数已变更为 {new} 参数，请注意修改配置文件！"
msgstr ""
"The configuration file parameter {old} has been changed to {new}. Please "
"make sure to update the configuration file accordingly!"

msgid ""
"关于 DouK-Downloader 的 免责声明：\n"
"\n"
"1. 使用者对本项目的使用由使用者自行决定，并自行承担风险。作者对使用者使用本项"
"目所产生的任何损失、责任、或风险概不负责。\n"
"2. 本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。作者按现有技术"
"水平努力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。\n"
"3. 本项目依赖的所有第三方库、插件或服务各自遵循其原始开源或商业许可，使用者需"
"自行查阅并遵守相应协议，作者不对第三方组件的稳定性、安全性及合规性承担任何责"
"任。\n"
"4. 使用者在使用本项目时必须严格遵守 GNU General Public License v3.0 的要求，"
"并在适当的地方注明使用了 GNU General Public License v3.0 的代码。\n"
"5. 使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行"
"为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。\n"
"6. 使用者不得使用本工具从事任何侵犯知识产权的行为，包括但不限于未经授权下载、"
"传播受版权保护的内容，开发者不参与、不支持、不认可任何非法内容的获取或分"
"发。\n"
"7. 本项目不对使用者涉及的数据收集、存储、传输等处理活动的合规性承担责任。使用"
"者应自行遵守相关法律法规，确保处理行为合法正当；因违规操作导致的法律责任由使"
"用者自行承担。\n"
"8. 使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行"
"为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。\n"
"9. 本项目的作者不会提供 DouK-Downloader 项目的付费版本，也不会提供与 DouK-"
"Downloader 项目相关的任何商业服务。\n"
"10. 基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不"
"承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的"
"各种情况负全部责任。\n"
"11. 本项目不授予使用者任何专利许可；若使用本项目导致专利纠纷或侵权，使用者自"
"行承担全部风险和责任。未经作者或权利人书面授权，不得使用本项目进行任何商业宣"
"传、推广或再授权。\n"
"12. 作者保留随时终止向任何违反本声明的使用者提供服务的权利，并可能要求其销毁"
"已获取的代码及衍生作品。\n"
"13. 作者保留在不另行通知的情况下更新本声明的权利，使用者持续使用即视为接受修"
"订后的条款。\n"
"\n"
"在使用本项目的代码和功能之前，请您认真考虑并接受以上免责声明。如果您对上述声"
"明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码"
"和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险"
"和后果。\n"
msgstr ""
"Disclaimer for DouK-Downloader:\n"
"\n"
"1. The use of this project is entirely at the user's own discretion and "
"risk. The author assumes no responsibility or liability of any kind for any "
"loss, damage, or risk arising from the user's use of this project.\n"
"2. The code and functionalities provided by the author of this project are "
"developed based on current knowledge and technology. The author makes every "
"effort to ensure the correctness and security of the code according to "
"current technical standards but does not guarantee that the code is "
"completely free of errors or defects.\n"
"3. All third-party libraries, plugins, or services used by this project "
"follow their original open-source or commercial licenses. Users must review "
"and comply with these license agreements accordingly. The author assumes no "
"responsibility for the stability, security, or compliance of any third-party "
"components.\n"
"4. When using this project, users must strictly comply with the requirements "
"of the GNU General Public License v3.0 and clearly indicate in appropriate "
"places that the code was used under the GNU General Public License v3.0.\n"
"5. When using the code and functionalities of this project, users must "
"independently research relevant laws and regulations and ensure that their "
"usage is legal and compliant. Any legal liabilities or risks arising from "
"violations of laws and regulations shall be borne solely by the user.\n"
"6. Users must not use this tool to engage in any activities that infringe "
"intellectual property rights, including but not limited to downloading or "
"distributing copyrighted content without authorization. Developers do not "
"participate in, support, or endorse the acquisition or distribution of any "
"illegal or unauthorized content.\n"
"7. This project assumes no responsibility for the compliance of data "
"processing activities (including collection, storage, and transmission) "
"performed by users. Users must comply with relevant laws and regulations and "
"ensure that such activities are lawful and proper. Legal liabilities "
"resulting from non-compliant operations shall be borne by the user.\n"
"8. Under no circumstances may users associate the author, contributors, or "
"other related parties of this project with their usage of the project, nor "
"may they hold these parties liable for any loss or damage resulting from "
"such usage.\n"
"9. The author of this project will not provide a paid version of the DouK-"
"Downloader project, nor will they offer any commercial services related to "
"it.\n"
"10. Any secondary development, modification, or compilation based on this "
"project is unrelated to the original author. The original author assumes no "
"liability for any consequences resulting from such secondary development. "
"Users bear full responsibility for all outcomes arising from such "
"modifications.\n"
"11. This project does not grant users any patent licenses. If the use of "
"this project leads to patent disputes or infringement, the user assumes all "
"associated risks and responsibilities. Without written authorization from "
"the author or rights holder, users may not use this project for any "
"commercial promotion, advertising, or re-licensing.\n"
"12. The author reserves the right to terminate service to any user who "
"violates this disclaimer at any time and may require them to destroy all "
"obtained code and derivative works.\n"
"13. The author reserves the right to update this disclaimer at any time "
"without prior notice. Continued use of the project constitutes acceptance of "
"the revised terms.\n"
"\n"
"Before using the code and functionalities of this project, please carefully "
"consider and accept the above disclaimer. If you have any questions or "
"disagree with the above statements, please do not use the code and "
"functionalities of this project. If you do use the code and functionalities "
"of this project, it shall be deemed that you have fully understood and "
"accepted the above disclaimer and voluntarily assume all risks and "
"consequences associated with its use.\n"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\custom\function.py:56
#, python-brace-format
msgid ""
"程序连续处理了 {batches} 个数据，为了避免请求频率过高导致账号或 IP 被风控，程"
"序已经暂停运行，将在 {rest_time} 秒后恢复运行！"
msgstr ""
"The program has continuously processed {batches} items. To avoid high "
"request frequency that could lead to account or IP being restricted, the "
"program has paused and will resume in {rest_time} seconds!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:159
msgid "开始下载作品文件"
msgstr "Start downloading the works file."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:235
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:343
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:501
msgid "音乐"
msgstr "Music"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:255
msgid "程序将会调用 ffmpeg 下载直播，关闭 DouK-Downloader 不会中断下载！"
msgstr ""
"The program will call ffmpeg to download the live stream. Closing DouK-"
"Downloader will not interrupt the download!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:332
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:335
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:753
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:422
msgid "实况"
msgstr "LivePhoto"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:409
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:460
#, python-brace-format
msgid "【{type}】{name} 提取文件下载地址失败，跳过下载"
msgstr ""
"【{type}】{name} failed to retrieve the file download URL, skipping download."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:421
#, python-brace-format
msgid "【{type}】{name} 存在下载记录，跳过下载"
msgstr "【{type}】{name} has a download record, skipping download."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:428
#, python-brace-format
msgid "【{type}】{name}_{index} 文件已存在，跳过下载"
msgstr "【{type}】{name}_{index} file already exists, skipping download."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:472
#, python-brace-format
msgid "【{type}】{name} 存在下载记录或文件已存在，跳过下载"
msgstr ""
"【{type}】{name} has a download record or file already exists, skipping "
"download."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:514
#, python-brace-format
msgid "【{type}】{name}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:622
msgid "文件缓存异常，尝试重新下载"
msgstr "File cache exception, attempting to re-download."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:660
#, python-brace-format
msgid "网络异常: {error_repr}"
msgstr "Network exception: {error_repr}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:664
#, python-brace-format
msgid "响应码异常: {error_repr}"
msgstr "Response code exception: {error_repr}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:668
msgid ""
"如果 TikTok 平台作品下载功能异常，请检查配置文件中 browser_info_tiktok 的 "
"device_id 参数！"
msgstr ""
"If the TikTok platform's content download function is not working, please "
"check the device_id parameter in browser_info_tiktok in the configuration "
"file!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:679
#, python-brace-format
msgid "下载文件时发生预期之外的错误，请向作者反馈，错误信息: {error}"
msgstr ""
"An unexpected error occurred while downloading the file. Please report it to "
"the author, error information: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:715
#, python-brace-format
msgid "{show} 下载中断，错误信息：{error}"
msgstr "{show} download interrupted, error information: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:721
#, python-brace-format
msgid "{show} 文件下载成功"
msgstr "{show} file download successful"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:785
#, python-brace-format
msgid "UID{id_}_{name}_发布作品"
msgstr "UID{id_}_{name}_Posts"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:787
#, python-brace-format
msgid "UID{id_}_{name}_喜欢作品"
msgstr "UID{id_}_{name}_Liked"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:789
#, python-brace-format
msgid "MID{id_}_{name}_合集作品"
msgstr "MID{id_}_{name}_Mix"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:791
#, python-brace-format
msgid "UID{id_}_{name}_收藏作品"
msgstr "UID{id_}_{name}_Favorites"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:793
#, python-brace-format
msgid "CID{id_}_{name}_收藏夹作品"
msgstr "CID{id_}_{name}_Collections"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:850
#, python-brace-format
msgid "{file_name} 文件已删除"
msgstr "{file_name} file has been deleted"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:854
#, python-brace-format
msgid "下载视频作品 {downloaded_video_count} 个"
msgstr "Downloaded {downloaded_video_count} video works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:859
#, python-brace-format
msgid "跳过视频作品 {skipped_count} 个"
msgstr "Skipped {skipped_count} video works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:864
#, python-brace-format
msgid "下载图集作品 {downloaded_image_count} 个"
msgstr "Downloaded {downloaded_image_count} image works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:869
#, python-brace-format
msgid "跳过图集作品 {skipped_count} 个"
msgstr "Skipped {skipped_count} image works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:874
#, python-brace-format
msgid "下载实况作品 {downloaded_image_count} 个"
msgstr "Downloaded {downloaded_image_count} livePhoto works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:879
#, python-brace-format
msgid "跳过实况作品 {skipped_count} 个"
msgstr "Skipped {skipped_count} livePhoto works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:957
#, python-brace-format
msgid "未收录的文件类型：{content}"
msgstr "Unlisted file type: {content}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:967
#, python-brace-format
msgid "{show} 响应内容为空"
msgstr "{show} response content is empty"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:976
#, python-brace-format
msgid "{show} 文件大小超出限制，跳过下载"
msgstr "{show} file size exceeds limit, skipping download"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\msToken.py:108
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\ttWid.py:42
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\ttWid.py:93
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\webID.py:44
#, python-brace-format
msgid "获取 {name} 参数失败！"
msgstr "Failed to retrieve {name} parameter!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:99
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:110
#, python-brace-format
msgid "提取账号信息失败: {data}"
msgstr "Failed to extract account information: {data}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:217
#, python-brace-format
msgid "筛选处理后作品数量: {count}"
msgstr "Number of works after filtering: {count}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:831
msgid "已注销账号"
msgstr "AccountDeactivated"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:832
msgid "无效账号昵称"
msgstr "InvalidNickname"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:859
#, python-brace-format
msgid "sec_user_id {user_id} 与 {s} 不一致"
msgstr "sec_user_id {user_id} does not match {s}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:944
msgid "提取账号信息或合集信息失败，请向作者反馈！"
msgstr ""
"Failed to extract Account or Mix information, please report to the author!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:41
msgid "账号喜欢作品"
msgstr "Account liked works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:41
msgid "账号发布作品"
msgstr "Account post works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:68
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:85
msgid ""
"该账号为私密账号，需要使用登录后的 Cookie，且登录的账号需要关注该私密账号"
msgstr ""
"This is a private account, you need to use the Cookie from a logged-in "
"account, and the logged-in account must follow this private account."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:207
#, python-brace-format
msgid "tab 参数 {tab} 设置错误，程序将使用默认值: post"
msgstr ""
"tab parameter {tab} is set incorrectly, the program will use the default "
"value: post"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:212
msgid "最早"
msgstr "Earliest"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:215
msgid "最晚"
msgstr "Latest"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:229
#, python-brace-format
msgid "作品{tip}发布日期无效 {date}"
msgstr "{tip} publish date of the works is invalid: {date}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:234
#, python-brace-format
msgid "作品{tip}发布日期参数 {date} 类型错误"
msgstr "The {tip} publish date parameter {date} type is incorrect"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:237
#, python-brace-format
msgid "作品{tip}发布日期: {latest_date}"
msgstr "{tip} publish date of the works: {latest_date}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:261
msgid "配置文件 cookie 参数未登录，数据获取已提前结束"
msgstr ""
"Cookie parameter in the configuration file is not logged in, data retrieval "
"has ended prematurely"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:264
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:200
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail.py:82
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail_tiktok.py:80
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:121
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:391
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:235
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\user.py:64
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\tiktok_unofficial.py:74
#, python-brace-format
msgid "数据解析失败，请告知作者处理: {data}"
msgstr "Data parsing failed, please inform the author for handling: {data}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collection.py:26
msgid "账号收藏作品"
msgstr "Account favorites works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:58
msgid "当前账号无收藏夹"
msgstr "The current account has no collections"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:122
#, python-brace-format
msgid "收藏夹 {collects_id} 为空"
msgstr "The collections {collects_id} is empty"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:182
msgid "当前账号无收藏合集"
msgstr "The current account has no collections mix"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:216
msgid "收藏短剧"
msgstr "Favorite Series"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:237
msgid "当前账号无收藏短剧"
msgstr "The current account has no favorite series"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:270
msgid "收藏音乐"
msgstr "Collections music"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:291
msgid "当前账号无收藏音乐"
msgstr "The current account has no collections music"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:35
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment_tiktok.py:29
msgid "作品评论"
msgstr "Works comments"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:77
#, python-brace-format
msgid "作品 {item_id} 无评论"
msgstr "Works {item_id} has no comments"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:105
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:194
#, python-brace-format
msgid "正在获取{text}数据"
msgstr "Fetching {text} data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:230
msgid "作品评论回复"
msgstr "Works comment replies"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:270
#, python-brace-format
msgid "评论 {comment_id} 无回复"
msgstr "Comment {comment_id} has no replies"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:18
msgid "抖音热榜"
msgstr "DouYin Hot Board"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:23
msgid "娱乐榜"
msgstr "EntertainmentBoard"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:28
msgid "社会榜"
msgstr "SocialBoard"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:33
msgid "挑战榜"
msgstr "ChallengeBoard"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:52
msgid "热榜"
msgstr "HotBoard"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:87
#, python-brace-format
msgid "{space_name}数据"
msgstr "{space_name} data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info.py:29
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info_tiktok.py:27
msgid "账号简略"
msgstr "Account summary"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info.py:64
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info_tiktok.py:57
#, python-brace-format
msgid "获取{text}失败"
msgstr "Failed to retrieve {text}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\live_tiktok.py:57
msgid "此直播可能会令部分观众感到不适，请登录后重试！"
msgstr ""
"This live stream may cause discomfort to some viewers. Please log in and try "
"again!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix.py:71
msgid "获取合集 ID 失败"
msgstr "Failed to retrieve Mix ID"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix_tiktok.py:32
msgid "合辑作品"
msgstr "Mix Works"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix_tiktok.py:92
msgid "账号合辑数据"
msgstr "Account Mix data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:18
msgid "综合搜索"
msgstr "GeneralSearch"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:25
msgid "视频搜索"
msgstr "VideoSearch"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:32
msgid "用户搜索"
msgstr "UserSearch"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:39
msgid "直播搜索"
msgstr "LiveSearch"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:60
msgid "关键词  总页数  排序依据  发布时间  视频时长  搜索范围  内容形式"
msgstr ""
"keyword  TotalPages  SortType  PublicationTime  VideoDuration  SearchRange  "
"ContentForm"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:61
msgid "关键词  总页数  排序依据  发布时间  视频时长  搜索范围"
msgstr ""
"keyword  TotalPages  SortType  PublicationTime  VideoDuration  SearchRange"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:62
msgid "关键词  总页数  粉丝数量  用户类型"
msgstr "keyword  TotalPages  Fans  AccountType"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:63
msgid "关键词  总页数"
msgstr "keyword  TotalPages"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:72
msgid "综合排序"
msgstr "GeneralSort"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:73
msgid "最多点赞"
msgstr "MostLikes"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:74
msgid "最新发布"
msgstr "Latest"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:77
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:89
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:95
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:101
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:114
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:128
msgid "不限"
msgstr "Unlimited"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:78
msgid "一天内"
msgstr "Intraday"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:79
msgid "一周内"
msgstr "SevenDays"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:80
msgid "半年内"
msgstr "HalfYear"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:90
msgid "一分钟以内"
msgstr "OneMinute"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:91
msgid "一到五分钟"
msgstr "OneToFive"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:92
msgid "五分钟以上"
msgstr "MoreThanFive"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:96
msgid "最近看过"
msgstr "RecentlyWatched"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:97
msgid "还未看过"
msgstr "NotViewed"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:98
msgid "关注的人"
msgstr "Followed"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:103
msgid "图文"
msgstr "Image"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:115
msgid "1000以下"
msgstr "Below1000"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:119
msgid "100w以上"
msgstr "Over1000W"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:129
msgid "普通用户"
msgstr "GeneralUser"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:130
msgid "企业认证"
msgstr "Enterprise"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:131
msgid "个人认证"
msgstr "Individual"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:176
#, python-brace-format
msgid "获取{self_text}数据失败"
msgstr "Failed to retrieve {self_text} data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:444
#, python-brace-format
msgid "共获取到 {count} 个{text}"
msgstr "A total of {count} {text} retrieved"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:112
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:131
msgid "文件夹"
msgstr "Folder"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:208
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:218
msgid "文件"
msgstr "File"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:225
#, python-brace-format
msgid "{type} {old}被占用，重命名失败: {error}"
msgstr "{type} {old} is occupied, renaming failed: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:232
#, python-brace-format
msgid "{type} {new}名称重复，重命名失败: {error}"
msgstr "{type} {new} name is duplicated, renaming failed: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:239
#, python-brace-format
msgid "处理{type} {old}时发生预期之外的错误: {error}"
msgstr "Unexpected error occurred while processing {type} {old}: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\models\search.py:34
msgid "keyword 参数无效"
msgstr "The keyword parameter is invalid"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\cookie.py:42
msgid "当前剪贴板的内容不是有效的 Cookie 内容！"
msgstr "The current clipboard content is not valid Cookie data!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\storage\sqlite.py:83
msgid "更新数据表名称时发生错误，重命名失败，请向作者反馈以便修复问题！"
msgstr ""
"An error occurred while updating the data table name. The rename operation "
"failed. Please report this issue to the developer for a fix."

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\storage\xlsx.py:62
#, python-brace-format
msgid "数据包含非法字符，保存数据失败：{error}"
msgstr "The data contains illegal characters, failed to save the data: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:80
#, python-brace-format
msgid ""
"读取指定浏览器的 {platform_name} Cookie 并写入配置文件；\n"
"注意：Windows 系统需要以管理员身份运行程序才能读取 Chromium、Chrome、Edge 浏"
"览器 Cookie！\n"
"{options}\n"
"请输入浏览器名称或序号："
msgstr ""
"Read the specified browser's {platform_name} Cookie and write it to the "
"configuration file;\n"
"Note: On Windows, you need to run the program as administrator to read "
"Chromium, Chrome, or Edge browser Cookies!\n"
"{options}\n"
"Please enter the browser name or number:"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:94
msgid "读取 Cookie 成功！"
msgstr "Cookie read successfully!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:102
msgid "Cookie 数据为空！"
msgstr "Cookie data is empty!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:105
msgid "未选择浏览器！"
msgstr "No browser selected!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:117
msgid "浏览器名称或序号输入错误！"
msgstr "Browser name or number input error!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:125
msgid "读取 Cookie 失败，未找到 Cookie 数据！"
msgstr "Failed to read Cookie, no Cookie data found!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:164
msgid "从浏览器读取 Cookie 功能不支持当前平台！"
msgstr ""
"Reading Cookie from the browser is not supported on the current platform!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:26
msgid "响应内容不是有效的 JSON 数据"
msgstr "Response content is not valid JSON data"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:28
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:50
#, python-brace-format
msgid "响应码异常：{error}"
msgstr "Response code error: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:30
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:37
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:52
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:59
#, python-brace-format
msgid "网络异常：{error}"
msgstr "Network exception: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:32
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:54
#, python-brace-format
msgid "请求超时：{error}"
msgstr "Request timed out: {error}"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:48
msgid "响应内容不是有效的 JSON 数据，请尝试更新 Cookie！"
msgstr "Response content is not valid JSON data, Please try updating cookies!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\cleaner.py:46
msgid "不受支持的操作系统类型，可能无法正常去除非法字符！"
msgstr ""
"Unsupported operating system type, illegal characters may not be removed "
"properly!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\error.py:9
msgid "项目代码错误"
msgstr "Project code error"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\retry.py:19
#, python-brace-format
msgid "正在进行第 {index} 次重试"
msgstr "Retrying {index} time"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\retry.py:48
msgid ""
"如需重新尝试处理该对象，请关闭所有正在访问该对象的窗口或程序，然后直接按下回"
"车键！\n"
"如需跳过处理该对象，请输入任意字符后按下回车键！"
msgstr ""
"To retry processing this object, please close all windows or programs "
"accessing this object, then press Enter!\n"
"To skip processing this object, please enter any character and press Enter!"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\retry.py:63
msgid "请关闭所有正在访问该对象的窗口或程序，然后按下回车键继续处理！"
msgstr ""
"Please close all windows or programs accessing this object, then press Enter "
"to continue processing!"

msgid ""
"\n"
"项目默认无需令牌；公开部署时，建议设置令牌以防止恶意请求！\n"
"\n"
"令牌设置位置：`src/custom/function.py` - `is_valid_token()`\n"
msgstr ""
"\n"
"Project defaults to no token; when publicly deployed, it is recommended to "
"set a token to prevent malicious requests!\n"
"\n"
"Token setting location: `src/custom/function.py` - `is_valid_token()`\n"

msgid ""
"\n"
"更新项目配置文件 settings.json\n"
"\n"
"仅需传入需要更新的配置参数\n"
"\n"
"返回更新后的全部配置参数\n"
msgstr ""
"\n"
"Update project configuration file settings.json\n"
"\n"
"Only needs to pass the configuration parameters that need to be updated\n"
"\n"
"Returns all updated configuration parameters\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **text**: 包含分享链接的字符串；必需参数\n"
"- **proxy**: 代理；可选参数\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **text**: String containing the sharing link; required parameter\n"
"- **proxy**: Proxy; optional parameter\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: 抖音作品 ID；必需参数\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **detail_id**: DouYin work ID; required parameter\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **sec_user_id**: 抖音账号 sec_uid；必需参数\n"
"- **tab**: 账号页面类型；可选参数，默认值：`post`\n"
"- **earliest**: 作品最早发布日期；可选参数\n"
"- **latest**: 作品最晚发布日期；可选参数\n"
"- **pages**: 最大请求次数，仅对请求账号喜欢页数据有效；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **sec_user_id**: DouYin account sec_uid; required parameter\n"
"- **tab**: Account page type; optional parameter, default value: `post`\n"
"- **earliest**: Earliest release date of works; optional parameter\n"
"- **latest**: Latest release date of works; optional parameter\n"
"- **pages**: Maximum number of request times, only valid for requesting "
"account favorite page data; optional parameter\n"
"- **cursor**: Optional parameter\n"
"- **count**: Optional parameter\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **mix_id**: 抖音合集 ID\n"
"- **detail_id**: 属于合集的抖音作品 ID\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
"\n"
"**`mix_id` 和 `detail_id` 二选一，只需传入其中之一即可**\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **mix_id**: DouYin collection ID\n"
"- **detail_id**: DouYin work ID that belongs to the collection\n"
"- **cursor**: Optional parameter\n"
"- **count**: Optional parameter\n"
"\n"
"**Either `mix_id` or `detail_id` must be provided — only one of them is "
"required**\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **web_rid**: 抖音直播 web_rid\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **web_rid**: DouYin live stream web_rid\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **web_rid**: 抖音直播 web_rid\n"
"- **room_id**: 抖音直播 room_id\n"
"- **sec_user_id**: 抖音直播账号 sec_user_id\n"
"\n"
"**本接口支持两种参数传入方式**:\n"
"\n"
"- 方式一 ：传入 `web_rid`\n"
"- 方式二 ：同时传入 `room_id` 和 `sec_user_id`\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **web_rid**: DouYin live stream web_rid\n"
"- **room_id**: DouYin live stream room_id\n"
"- **sec_user_id**: DouYin live stream account sec_user_id\n"
"\n"
"**This interface supports two ways of passing parameters**:\n"
"\n"
"- **Method 1**: Pass in `web_rid`\n"
"- **Method 2**: Pass in both `room_id` and `sec_user_id`\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: 抖音作品 ID；必需参数\n"
"- **pages**: 最大请求次数；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
"- **count_reply**: 可选参数\n"
"- **reply**: 可选参数，默认值：False\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **detail_id**: DouYin work ID; required parameter\n"
"- **pages**: Maximum number of request times; optional parameter\n"
"- **cursor**: Optional parameter\n"
"- **count**: Optional parameter\n"
"- **count_reply**: Optional parameter\n"
"- **reply**: Optional parameter, default value: False\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: 抖音作品 ID；必需参数\n"
"- **comment_id**: 评论 ID；必需参数\n"
"- **pages**: 最大请求次数；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **detail_id**: DouYin work ID; required parameter\n"
"- **comment_id**: Comment ID; required parameter\n"
"- **pages**: Maximum number of request times; optional parameter\n"
"- **cursor**: Optional parameter\n"
"- **count**: Optional parameter\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
"- **sort_type**: 排序依据；可选参数\n"
"- **publish_time**: 发布时间；可选参数\n"
"- **duration**: 视频时长；可选参数\n"
"- **search_range**: 搜索范围；可选参数\n"
"- **content_type**: 内容形式；可选参数\n"
"\n"
"**部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/"
"TikTokDownloader/wiki/"
"Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **keyword**: Keyword; required parameter\n"
"- **offset**: Starting page number; optional parameter\n"
"- **count**: Amount of data; optional parameter\n"
"- **pages**: Total number of pages; optional parameter\n"
"- **sort_type**: Sorting criteria; optional parameter\n"
"- **publish_time**: Publication time; optional parameter\n"
"- **duration**: Video duration; optional parameter\n"
"- **search_range**: Search scope; optional parameter\n"
"- **content_type**: Content format; optional parameter\n"
"\n"
"**Note**: For rules on passing certain parameters, please refer to the "
"documentation: [Parameter meanings](https://github.com/JoeanAmier/"
"TikTokDownloader/wiki/"
"Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
"- **sort_type**: 排序依据；可选参数\n"
"- **publish_time**: 发布时间；可选参数\n"
"- **duration**: 视频时长；可选参数\n"
"- **search_range**: 搜索范围；可选参数\n"
"\n"
"**部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/"
"TikTokDownloader/wiki/"
"Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **keyword**: Keyword; required parameter\n"
"- **offset**: Starting page number; optional parameter\n"
"- **count**: Amount of data; optional parameter\n"
"- **pages**: Total number of pages; optional parameter\n"
"- **sort_type**: Sorting criteria; optional parameter\n"
"- **publish_time**: Publication time; optional parameter\n"
"- **duration**: Video duration; optional parameter\n"
"- **search_range**: Search scope; optional parameter\n"
"\n"
"**Note**: For rules on passing certain parameters, please refer to the "
"documentation: [Parameter meanings](https://github.com/JoeanAmier/"
"TikTokDownloader/wiki/"
"Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
"- **douyin_user_fans**: 粉丝数量；可选参数\n"
"- **douyin_user_type**: 用户类型；可选参数\n"
"\n"
"**部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/"
"TikTokDownloader/wiki/"
"Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **keyword**: Keyword; required parameter\n"
"- **offset**: Starting page number; optional parameter\n"
"- **count**: Amount of data; optional parameter\n"
"- **pages**: Total number of pages; optional parameter\n"
"- **douyin_user_fans**: Number of followers; optional parameter\n"
"- **douyin_user_type**: User type; optional parameter\n"
"\n"
"**Note**: For rules on passing certain parameters, please refer to the "
"documentation: [Parameter meanings](https://github.com/JoeanAmier/"
"TikTokDownloader/wiki/"
"Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: DouYin Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **keyword**: Keyword; required parameter\n"
"- **offset**: Starting page number; optional parameter\n"
"- **count**: Amount of data; optional parameter\n"
"- **pages**: Total number of pages; optional parameter\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: TikTok 作品 ID；必需参数\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: TikTok Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **detail_id**: TikTok work ID; required parameter\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **sec_user_id**: TikTok 账号 secUid；必需参数\n"
"- **tab**: 账号页面类型；可选参数，默认值：`post`\n"
"- **earliest**: 作品最早发布日期；可选参数\n"
"- **latest**: 作品最晚发布日期；可选参数\n"
"- **pages**: 最大请求次数，仅对请求账号喜欢页数据有效；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: TikTok Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **sec_user_id**: TikTok account secUid; required parameter\n"
"- **tab**: Account page type; optional parameter, default value: `post`\n"
"- **earliest**: Earliest release date of works; optional parameter\n"
"- **latest**: Latest release date of works; optional parameter\n"
"- **pages**: Maximum number of request times, only valid for requesting "
"account favorite page data; optional parameter\n"
"- **cursor**: Optional parameter\n"
"- **count**: Optional parameter\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **mix_id**: TikTok 合集 ID；必需参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: TikTok Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **mix_id**: TikTok collection ID; required parameter\n"
"- **cursor**: Optional parameter\n"
"- **count**: Optional parameter\n"

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **room_id**: TikTok 直播 room_id；必需参数\n"
msgstr ""
"\n"
"**Parameters**:\n"
"\n"
"- **cookie**: TikTok Cookie; optional parameter\n"
"- **proxy**: Proxy; optional parameter\n"
"- **source**: Whether to return the original response data; optional "
"parameter, default value: False\n"
"- **room_id**: TikTok live stream room_id; required parameter\n"

#~ msgid "是否返回上一级菜单(YES/NO)"
#~ msgstr "Do you want to return to the previous menu (YES/NO)?"

#~ msgid "扫码登录失败，未写入 Cookie！"
#~ msgstr "QR code login failed, Cookie not written!"

#~ msgid "提取 web_rid 或者 room_id 失败！"
#~ msgstr "Failed to extract web_rid or room_id!"

#~ msgid "本次运行将会使用各项参数默认值，程序功能可能无法正常使用！"
#~ msgstr ""
#~ "This run will use the default values for all parameters, and the "
#~ "program's functionality may not work properly!"

#~ msgid "写入 Cookie 成功！"
#~ msgstr "Cookie written successfully!"

#~ msgid "当前 Cookie 已登录"
#~ msgstr "Current Cookie is logged in"

#~ msgid "当前 Cookie 未登录"
#~ msgstr "Current Cookie is not logged in"

#~ msgid "正在启动服务器，如需关闭服务器，请按下 Ctrl + C"
#~ msgstr ""
#~ "Starting the server. To shut down the server, please press Ctrl + C."

#~ msgid "扫码登录获取 Cookie (抖音)"
#~ msgstr "Scan code to login and get cookies (Tiktok)"

#~ msgid "输入任意字符继续处理账号/合集，直接回车停止处理账号/合集: "
#~ msgstr ""
#~ "Enter any character to continue processing Accounts/Mix, press Enter to "
#~ "stop processing Accounts/Mix:"
```

## File: `locale/zh_CN/LC_MESSAGES/tk.po`
```
# Chinese translations for DouK-Downloader package
# Copyright (C) 2024 THE DouK-Downloader'S COPYRIGHT HOLDER
# This file is distributed under the same license as the DouK-Downloader package.
# FIRST AUTHOR <yonglelolu@foxmail.com>, 2024.
#
msgid ""
msgstr ""
"Project-Id-Version: DouK-Downloader 5.8\n"
"Report-Msgid-Bugs-To: <yonglelolu@foxmail.com>\n"
"POT-Creation-Date: 2025-11-04 10:48+0800\n"
"PO-Revision-Date: 2024-12-22 21:46+0800\n"
"Last-Translator: <yonglelolu@foxmail.com>\n"
"Language-Team: Chinese (simplified)\n"
"Language: zh_CN\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=1; plural=0;\n"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_monitor.py:41
msgid ""
"程序会自动检测并提取剪贴板中的抖音和 TikTok 作品链接，并自动下载作品文件；如"
"需关闭，请按下 Ctrl+C，或将剪贴板内容设置为“close”以停止监听！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_monitor.py:129
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:941
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:968
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1288
#, python-brace-format
msgid "{url} 提取作品 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:50
msgid "验证失败！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:106
msgid "访问项目 GitHub 仓库"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:107
msgid "重定向至项目 GitHub 仓库主页"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:108
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:123
msgid "项目"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:115
msgid "测试令牌有效性"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:128
msgid "验证成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:135
msgid "更新项目全局配置"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:145
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:158
msgid "配置"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:156
msgid "获取项目全局配置"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:157
msgid "返回项目全部配置参数"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:166
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:511
msgid "获取分享链接重定向的完整链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:175
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:206
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:233
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:259
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:299
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:342
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:379
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:419
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:449
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:477
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:501
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:190
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:444
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:885
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:961
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\cookie.py:26
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:43
msgid "抖音"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:183
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:528
msgid "请求链接成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:188
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:533
msgid "请求链接失败！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:195
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:540
msgid "获取单个作品数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:216
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:561
msgid "获取账号作品数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:243
msgid "获取合集作品数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:269
msgid "参数错误！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:288
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:622
msgid "获取直播数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:326
msgid "获取作品评论数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:364
msgid "获取评论回复数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:398
msgid "获取综合搜索数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:429
msgid "获取视频搜索数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:459
msgid "获取用户搜索数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:487
msgid "获取直播搜索数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:588
msgid "获取合辑作品数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:656
msgid "搜索结果为空！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:709
msgid "获取数据成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_server.py:720
msgid "获取数据失败！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:71
msgid ""
"未设置 storage_format 参数，无法正常使用该功能，详细说明请查阅项目文档！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:86
msgid "抖音 Cookie"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:90
#, python-brace-format
msgid "{tip} 未登录，无法使用该功能，详细说明请查阅项目文档！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:143
msgid "批量下载账号作品(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:147
msgid "批量下载链接作品(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:151
msgid "获取直播拉流地址(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:155
msgid "采集作品评论数据(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:159
msgid "批量下载合集作品(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:163
msgid "采集账号详细数据(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:167
msgid "采集搜索结果数据(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:171
msgid "采集抖音热榜数据(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:176
msgid "批量下载收藏作品(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:180
msgid "批量下载收藏音乐(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:185
msgid "批量下载收藏夹作品(抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:189
msgid "批量下载账号作品(TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:193
msgid "批量下载链接作品(TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:197
msgid "批量下载合集作品(TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:201
msgid "获取直播拉流地址(TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:206
msgid "批量下载视频原画(TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:211
msgid "使用 accounts_urls 参数的账号链接(推荐)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:212
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:220
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:236
msgid "手动输入待采集的账号链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:213
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:221
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:237
msgid "从文本文档读取待采集的账号链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:217
msgid "使用 accounts_urls_tiktok 参数的账号链接(推荐)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:224
msgid "使用 mix_urls 参数的合集链接(推荐)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:225
msgid "获取当前账号收藏合集列表"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:226
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:231
msgid "手动输入待采集的合集/作品链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:227
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:232
msgid "从文本文档读取待采集的合集/作品链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:230
msgid "使用 mix_urls_tiktok 参数的合集链接(推荐)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:235
msgid "使用 accounts_urls 参数的账号链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:240
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:244
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:248
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:252
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:256
msgid "手动输入待采集的作品链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:241
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:245
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:249
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:253
msgid "从文本文档读取待采集的作品链接"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:261
msgid "综合搜索数据采集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:265
msgid "视频搜索数据采集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:269
msgid "用户搜索数据采集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:273
msgid "直播搜索数据采集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:283
#, python-brace-format
msgid "请输入{tip}链接: "
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:296
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:322
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:330
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1821
msgid "请选择账号链接来源"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:300
msgid "已退出批量下载账号作品(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:302
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:415
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:535
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\user.py:25
msgid "账号"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:306
#, python-brace-format
msgid "程序共处理 {0} 个{1}，成功 {2} 个，失败 {3} 个，耗时 {4} 分钟 {5} 秒"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:326
msgid "已退出批量下载账号作品(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:382
#, python-brace-format
msgid "共有 {count} 个账号的作品等待下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:393
#, python-brace-format
msgid ""
"配置文件 {name} 参数的 url {url} 提取 sec_user_id 失败，错误配置：{data}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:434
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:451
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1743
msgid "账号主页"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:438
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:455
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1747
#, python-brace-format
msgid "{url} 提取账号 sec_user_id 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:470
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:508
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1776
msgid "从文本文档提取账号 sec_user_id 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:556
#, python-brace-format
msgid "开始处理第 {index} 个账号"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:558
msgid "开始处理账号"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:571
#, python-brace-format
msgid "{sec_user_id} 获取账号信息失败，请检查 Cookie 登录状态！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:582
msgid ""
"如果账号发布作品均为共创作品且该账号均不是作品作者时，请配置已登录的 Cookie "
"后重新运行程序，其余情况请无视该提示！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:730
msgid "开始提取作品数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:743
msgid "提取账号或合集信息发生错误！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:825
msgid "发布作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:827
msgid "喜欢作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:829
msgid "收藏作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:831
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix.py:35
msgid "合集作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:833
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:89
msgid "收藏夹作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:844
#, python-brace-format
msgid "昵称/标题：{name}；标识：{mark}；ID：{id}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:884
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:918
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1272
msgid "请选择作品链接来源"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:888
msgid "已退出批量下载链接作品(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:898
msgid "已退出批量下载链接作品(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:905
msgid "注意：本功能为实验性功能，依赖第三方 API 服务，可能不稳定或存在限制！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:911
msgid "已退出批量下载视频原画(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:938
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:965
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1283
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail.py:24
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail_tiktok.py:24
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\slides.py:26
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\tiktok_unofficial.py:38
msgid "作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:944
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:971
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1017
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1291
#, python-brace-format
msgid "共提取到 {count} 个作品，开始处理！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:984
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1005
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1014
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1312
msgid "从文本文档提取作品 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1093
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:320
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:323
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:405
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:749
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:434
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:453
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:467
msgid "图集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1095
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:326
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:329
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:456
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:751
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:351
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:365
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:480
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:570
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:102
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\tiktok_unofficial.py:116
msgid "视频"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1105
msgid "程序未检测到有效的 ffmpeg，不支持直播下载功能！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1109
msgid "请选择下载清晰度(输入清晰度或者对应序号，直接回车代表不下载): "
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1116
msgid "未输入有效的清晰度或者序号，跳过下载！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1149
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1164
msgid "直播"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1154
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1171
msgid "获取直播数据失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1158
msgid "已退出获取直播拉流地址(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1167
msgid "{} 提取直播 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1181
msgid "已退出获取直播拉流地址(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1197
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1214
msgid "直播标题:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1198
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1215
msgid "主播昵称:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1199
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1217
msgid "在线观众:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1200
msgid "观看次数:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1202
msgid "当前直播已结束！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1216
msgid "开播时间:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1218
msgid "点赞次数:"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1223
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1242
msgid "FLV 拉流地址: "
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1226
msgid "M3U8 拉流地址: "
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1264
msgid "已退出采集作品评论数据(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1276
msgid "已退出采集作品评论数据(抖音)模式)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1363
#, python-brace-format
msgid "作品评论数据已储存至 {filename}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1364
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1374
#, python-brace-format
msgid "作品{id}_评论数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1368
msgid "采集评论数据失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1423
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1434
msgid "请选择合集链接来源"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1427
msgid "已退出批量下载合集作品(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1438
msgid "已退出批量下载合集作品(TikTok)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1455
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1470
msgid "合集或作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1459
#, python-brace-format
msgid "{url} 获取作品 ID 或合集 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1473
#, python-brace-format
msgid "{url} 获取合集 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1502
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1509
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:150
msgid "收藏合集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1513
#, python-brace-format
msgid "{text}列表："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1518
#, python-brace-format
msgid ""
"请输入需要下载的{item}序号(多个序号使用空格分隔，输入 ALL 下载全部{item})："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1532
#, python-brace-format
msgid "{text}序号输入错误！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1540
msgid "从文本文档提取作品 ID 或合集 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1550
msgid "从文本文档提取合集 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1590
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1650
msgid "合集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1626
#, python-brace-format
msgid ""
"配置文件 {name} 参数的 url {url} 获取作品 ID 或合集 ID 失败，错误配置：{data}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1668
#, python-brace-format
msgid "开始处理第 {index} 个合集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1670
msgid "开始处理合集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1704
msgid "采集合集作品数据失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1730
#, python-brace-format
msgid "配置文件 accounts_urls 参数第 {index} 条数据的 url 无效"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1754
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\cli_edition\write.py:40
msgid "请输入文本文档路径："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1761
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\cli_edition\write.py:47
#, python-brace-format
msgid "{path} 文件读取异常: {error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1764
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\cli_edition\write.py:50
#, python-brace-format
msgid "{path} 文件不存在！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1788
#, python-brace-format
msgid "正在获取账号 {sec_user_id} 的数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1815
msgid "账号数据已保存至文件"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1825
msgid "已退出采集账号详细数据模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1832
#, python-brace-format
msgid "请输入搜索参数；参数之间使用两个空格分隔({field})：\n"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1855
msgid "请选择搜索模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1934
msgid "搜索结果为空"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:1956
msgid "搜索数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2023
#, python-brace-format
msgid "搜索数据已保存至 {name}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2032
msgid "已退出采集抖音热榜数据(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2052
#, python-brace-format
msgid "热榜数据_{time}_{name}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2066
#, python-brace-format
msgid "热榜数据已储存至: 热榜数据_{time} + 榜单类型"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2081
msgid "已退出批量下载收藏作品(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2101
msgid "已退出批量下载收藏夹作品(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2126
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:27
msgid "收藏夹"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2137
#, python-brace-format
msgid "配置文件 owner_url 的 url 参数 {url} 无效"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2167
msgid "已退出批量下载收藏音乐(抖音)模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2175
#, python-brace-format
msgid "程序运行耗时 {minutes} 分钟 {seconds} 秒"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2205
msgid "开始获取收藏数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2215
#, python-brace-format
msgid "{sec_user_id} 获取账号信息失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2248
msgid "开始获取收藏夹数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\main_terminal.py:2301
msgid "请选择采集功能"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:108
msgid "禁用"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:109
msgid "启用"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:112
msgid "从剪贴板读取 Cookie (抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:113
msgid "从浏览器读取 Cookie (抖音)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:115
msgid "从剪贴板读取 Cookie (TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:116
msgid "从浏览器读取 Cookie (TikTok)"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:117
msgid "终端交互模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:118
msgid "后台监听模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:119
msgid "Web API 模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:120
msgid "Web UI 模式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:124
msgid "{}作品下载记录"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:127
msgid "删除作品下载记录"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:129
msgid "{}运行日志记录"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:132
msgid "检查程序版本更新"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:133
msgid "切换语言"
msgstr "Switch to English"

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:149
msgid ""
"访问 http://127.0.0.1:5555/docs 或者 http://127.0.0.1:5555/redoc 可以查阅 "
"API 模式说明文档！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:190
msgid "是否已仔细阅读上述免责声明(YES/NO): "
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:224
msgid "项目地址: {}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:225
msgid "项目文档: {}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:226
msgid "开源许可: {}\n"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:248
#, python-brace-format
msgid "检测到新版本: {major}.{minor}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:255
msgid "当前版本为开发版, 可更新至正式版"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:260
msgid "当前已是最新开发版"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:264
msgid "当前已是最新正式版"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:268
msgid "检测新版本失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:280
msgid "DouK-Downloader 功能选项"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:322
msgid "修改设置成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:334
msgid "Cookie 获取教程："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:340
msgid ""
"复制 Cookie 内容至剪贴板后，按回车键确认继续；若输入任意内容并按回车，则取消"
"操作："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:379
msgid "作品下载记录功能已禁用！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\application\TikTokDownloader.py:445
msgid "正在关闭程序"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:273
#, python-brace-format
msgid "{name} 参数格式错误"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:366
#, python-brace-format
msgid "root 参数 {root} 不是有效的文件夹路径，程序将使用项目根路径作为储存路径"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:386
#, python-brace-format
msgid ""
"folder_name 参数 {folder_name} 不是有效的文件夹名称，程序将使用默认值："
"Download"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:399
#, python-brace-format
msgid ""
"name_format 参数 {name_format} 设置错误，程序将使用默认值：创建时间 作品类型 "
"账号昵称 作品描述"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:412
#, python-brace-format
msgid ""
"date_format 参数 {date_format} 设置错误，程序将使用默认值：年-月-日 时:分:秒"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:421
#, python-brace-format
msgid "split 参数 {split} 包含非法字符，程序将使用默认值：-"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:451
#, python-brace-format
msgid "{remark}代理参数应为字符串格式，未来不再支持字典格式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:467
#, python-brace-format
msgid "{remark}代理 {proxy} 测试成功"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:474
#, python-brace-format
msgid "{remark}代理 {proxy} 测试超时"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:484
#, python-brace-format
msgid "{remark}代理 {proxy} 测试失败：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:519
#, python-brace-format
msgid "max_pages 参数 {max_pages} 设置错误，程序将使用默认值：99999"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:543
#, python-brace-format
msgid ""
"storage_format 参数 {storage_format} 设置错误，程序默认不会储存任何数据至文件"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:561
msgid "正在更新抖音参数，请稍等..."
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:579
msgid "抖音参数更新完毕！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:583
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:644
msgid "配置文件 cookie 参数未设置，抖音平台功能可能无法正常使用"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:593
msgid "正在更新 TikTok 参数，请稍等..."
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:611
msgid "TikTok 参数更新完毕！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:616
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:667
msgid "配置文件 cookie_tiktok 参数未设置，TikTok 平台功能可能无法正常使用"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:772
#, python-brace-format
msgid "TikTok cookie 缺少 {name} 键值对，请尝试重新写入 cookie"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:1112
#, python-brace-format
msgid "{key} 参数 {value} 设置过小，程序将使用默认值：{default}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:1120
#, python-brace-format
msgid "{key} 参数 {value} 设置错误，程序将使用默认值：{default}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\parameter.py:1133
#, python-brace-format
msgid "live_qualities 参数 {live_qualities} 设置错误"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:157
msgid ""
"创建默认配置文件 settings.json 成功！\n"
"请参考项目文档的快速入门部分，设置 Cookie 后重新运行程序！\n"
"建议根据实际使用需求修改配置文件 settings.json！\n"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:174
msgid "配置文件 settings.json 格式错误，请检查 JSON 格式！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:186
#, python-brace-format
msgid "配置文件 settings.json 缺少参数 {i}，已自动添加该参数！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:204
msgid "保存配置成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\config\settings.py:216
#, python-brace-format
msgid "配置文件 {old} 参数已变更为 {new} 参数，请注意修改配置文件！"
msgstr ""

msgid ""
"关于 DouK-Downloader 的 免责声明：\n"
"\n"
"1. 使用者对本项目的使用由使用者自行决定，并自行承担风险。作者对使用者使用本项"
"目所产生的任何损失、责任、或风险概不负责。\n"
"2. 本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。作者按现有技术"
"水平努力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。\n"
"3. 本项目依赖的所有第三方库、插件或服务各自遵循其原始开源或商业许可，使用者需"
"自行查阅并遵守相应协议，作者不对第三方组件的稳定性、安全性及合规性承担任何责"
"任。\n"
"4. 使用者在使用本项目时必须严格遵守 GNU General Public License v3.0 的要求，"
"并在适当的地方注明使用了 GNU General Public License v3.0 的代码。\n"
"5. 使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行"
"为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。\n"
"6. 使用者不得使用本工具从事任何侵犯知识产权的行为，包括但不限于未经授权下载、"
"传播受版权保护的内容，开发者不参与、不支持、不认可任何非法内容的获取或分"
"发。\n"
"7. 本项目不对使用者涉及的数据收集、存储、传输等处理活动的合规性承担责任。使用"
"者应自行遵守相关法律法规，确保处理行为合法正当；因违规操作导致的法律责任由使"
"用者自行承担。\n"
"8. 使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行"
"为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。\n"
"9. 本项目的作者不会提供 DouK-Downloader 项目的付费版本，也不会提供与 DouK-"
"Downloader 项目相关的任何商业服务。\n"
"10. 基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不"
"承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的"
"各种情况负全部责任。\n"
"11. 本项目不授予使用者任何专利许可；若使用本项目导致专利纠纷或侵权，使用者自"
"行承担全部风险和责任。未经作者或权利人书面授权，不得使用本项目进行任何商业宣"
"传、推广或再授权。\n"
"12. 作者保留随时终止向任何违反本声明的使用者提供服务的权利，并可能要求其销毁"
"已获取的代码及衍生作品。\n"
"13. 作者保留在不另行通知的情况下更新本声明的权利，使用者持续使用即视为接受修"
"订后的条款。\n"
"\n"
"在使用本项目的代码和功能之前，请您认真考虑并接受以上免责声明。如果您对上述声"
"明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码"
"和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险"
"和后果。\n"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\custom\function.py:56
#, python-brace-format
msgid ""
"程序连续处理了 {batches} 个数据，为了避免请求频率过高导致账号或 IP 被风控，程"
"序已经暂停运行，将在 {rest_time} 秒后恢复运行！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:159
msgid "开始下载作品文件"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:235
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:343
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:501
msgid "音乐"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:255
msgid "程序将会调用 ffmpeg 下载直播，关闭 DouK-Downloader 不会中断下载！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:332
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:335
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:753
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:422
msgid "实况"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:409
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:460
#, python-brace-format
msgid "【{type}】{name} 提取文件下载地址失败，跳过下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:421
#, python-brace-format
msgid "【{type}】{name} 存在下载记录，跳过下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:428
#, python-brace-format
msgid "【{type}】{name}_{index} 文件已存在，跳过下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:472
#, python-brace-format
msgid "【{type}】{name} 存在下载记录或文件已存在，跳过下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:514
#, python-brace-format
msgid "【{type}】{name}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:622
msgid "文件缓存异常，尝试重新下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:660
#, python-brace-format
msgid "网络异常: {error_repr}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:664
#, python-brace-format
msgid "响应码异常: {error_repr}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:668
msgid ""
"如果 TikTok 平台作品下载功能异常，请检查配置文件中 browser_info_tiktok 的 "
"device_id 参数！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:679
#, python-brace-format
msgid "下载文件时发生预期之外的错误，请向作者反馈，错误信息: {error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:715
#, python-brace-format
msgid "{show} 下载中断，错误信息：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:721
#, python-brace-format
msgid "{show} 文件下载成功"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:785
#, python-brace-format
msgid "UID{id_}_{name}_发布作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:787
#, python-brace-format
msgid "UID{id_}_{name}_喜欢作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:789
#, python-brace-format
msgid "MID{id_}_{name}_合集作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:791
#, python-brace-format
msgid "UID{id_}_{name}_收藏作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:793
#, python-brace-format
msgid "CID{id_}_{name}_收藏夹作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:850
#, python-brace-format
msgid "{file_name} 文件已删除"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:854
#, python-brace-format
msgid "下载视频作品 {downloaded_video_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:859
#, python-brace-format
msgid "跳过视频作品 {skipped_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:864
#, python-brace-format
msgid "下载图集作品 {downloaded_image_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:869
#, python-brace-format
msgid "跳过图集作品 {skipped_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:874
#, python-brace-format
msgid "下载实况作品 {downloaded_image_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:879
#, python-brace-format
msgid "跳过实况作品 {skipped_count} 个"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:957
#, python-brace-format
msgid "未收录的文件类型：{content}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:967
#, python-brace-format
msgid "{show} 响应内容为空"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\downloader\download.py:976
#, python-brace-format
msgid "{show} 文件大小超出限制，跳过下载"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\msToken.py:108
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\ttWid.py:42
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\ttWid.py:93
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\encrypt\webID.py:44
#, python-brace-format
msgid "获取 {name} 参数失败！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:99
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:110
#, python-brace-format
msgid "提取账号信息失败: {data}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:217
#, python-brace-format
msgid "筛选处理后作品数量: {count}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:831
msgid "已注销账号"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:832
msgid "无效账号昵称"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:859
#, python-brace-format
msgid "sec_user_id {user_id} 与 {s} 不一致"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\extract\extractor.py:944
msgid "提取账号信息或合集信息失败，请向作者反馈！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:41
msgid "账号喜欢作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:41
msgid "账号发布作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:68
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:85
msgid ""
"该账号为私密账号，需要使用登录后的 Cookie，且登录的账号需要关注该私密账号"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:207
#, python-brace-format
msgid "tab 参数 {tab} 设置错误，程序将使用默认值: post"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:212
msgid "最早"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:215
msgid "最晚"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:229
#, python-brace-format
msgid "作品{tip}发布日期无效 {date}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:234
#, python-brace-format
msgid "作品{tip}发布日期参数 {date} 类型错误"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:237
#, python-brace-format
msgid "作品{tip}发布日期: {latest_date}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:261
msgid "配置文件 cookie 参数未登录，数据获取已提前结束"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\account.py:264
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:200
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail.py:82
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\detail_tiktok.py:80
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:121
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:391
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:235
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\user.py:64
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\tiktok_unofficial.py:74
#, python-brace-format
msgid "数据解析失败，请告知作者处理: {data}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collection.py:26
msgid "账号收藏作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:58
msgid "当前账号无收藏夹"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:122
#, python-brace-format
msgid "收藏夹 {collects_id} 为空"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:182
msgid "当前账号无收藏合集"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:216
msgid "收藏短剧"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:237
msgid "当前账号无收藏短剧"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:270
msgid "收藏音乐"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\collects.py:291
msgid "当前账号无收藏音乐"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:35
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment_tiktok.py:29
msgid "作品评论"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:77
#, python-brace-format
msgid "作品 {item_id} 无评论"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:105
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:194
#, python-brace-format
msgid "正在获取{text}数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:230
msgid "作品评论回复"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\comment.py:270
#, python-brace-format
msgid "评论 {comment_id} 无回复"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:18
msgid "抖音热榜"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:23
msgid "娱乐榜"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:28
msgid "社会榜"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:33
msgid "挑战榜"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:52
msgid "热榜"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\hot.py:87
#, python-brace-format
msgid "{space_name}数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info.py:29
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info_tiktok.py:27
msgid "账号简略"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info.py:64
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\info_tiktok.py:57
#, python-brace-format
msgid "获取{text}失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\live_tiktok.py:57
msgid "此直播可能会令部分观众感到不适，请登录后重试！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix.py:71
msgid "获取合集 ID 失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix_tiktok.py:32
msgid "合辑作品"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\mix_tiktok.py:92
msgid "账号合辑数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:18
msgid "综合搜索"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:25
msgid "视频搜索"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:32
msgid "用户搜索"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:39
msgid "直播搜索"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:60
msgid "关键词  总页数  排序依据  发布时间  视频时长  搜索范围  内容形式"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:61
msgid "关键词  总页数  排序依据  发布时间  视频时长  搜索范围"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:62
msgid "关键词  总页数  粉丝数量  用户类型"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:63
msgid "关键词  总页数"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:72
msgid "综合排序"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:73
msgid "最多点赞"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:74
msgid "最新发布"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:77
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:89
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:95
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:101
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:114
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:128
msgid "不限"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:78
msgid "一天内"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:79
msgid "一周内"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:80
msgid "半年内"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:90
msgid "一分钟以内"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:91
msgid "一到五分钟"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:92
msgid "五分钟以上"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:96
msgid "最近看过"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:97
msgid "还未看过"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:98
msgid "关注的人"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:103
msgid "图文"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:115
msgid "1000以下"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:119
msgid "100w以上"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:129
msgid "普通用户"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:130
msgid "企业认证"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\search.py:131
msgid "个人认证"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:176
#, python-brace-format
msgid "获取{self_text}数据失败"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\interface\template.py:444
#, python-brace-format
msgid "共获取到 {count} 个{text}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:112
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:131
msgid "文件夹"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:208
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:218
msgid "文件"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:225
#, python-brace-format
msgid "{type} {old}被占用，重命名失败: {error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:232
#, python-brace-format
msgid "{type} {new}名称重复，重命名失败: {error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\manager\cache.py:239
#, python-brace-format
msgid "处理{type} {old}时发生预期之外的错误: {error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\models\search.py:34
msgid "keyword 参数无效"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\module\cookie.py:42
msgid "当前剪贴板的内容不是有效的 Cookie 内容！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\storage\sqlite.py:83
msgid "更新数据表名称时发生错误，重命名失败，请向作者反馈以便修复问题！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\storage\xlsx.py:62
#, python-brace-format
msgid "数据包含非法字符，保存数据失败：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:80
#, python-brace-format
msgid ""
"读取指定浏览器的 {platform_name} Cookie 并写入配置文件；\n"
"注意：Windows 系统需要以管理员身份运行程序才能读取 Chromium、Chrome、Edge 浏"
"览器 Cookie！\n"
"{options}\n"
"请输入浏览器名称或序号："
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:94
msgid "读取 Cookie 成功！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:102
msgid "Cookie 数据为空！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:105
msgid "未选择浏览器！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:117
msgid "浏览器名称或序号输入错误！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:125
msgid "读取 Cookie 失败，未找到 Cookie 数据！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\browser.py:164
msgid "从浏览器读取 Cookie 功能不支持当前平台！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:26
msgid "响应内容不是有效的 JSON 数据"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:28
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:50
#, python-brace-format
msgid "响应码异常：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:30
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:37
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:52
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:59
#, python-brace-format
msgid "网络异常：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:32
#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:54
#, python-brace-format
msgid "请求超时：{error}"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\capture.py:48
msgid "响应内容不是有效的 JSON 数据，请尝试更新 Cookie！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\cleaner.py:46
msgid "不受支持的操作系统类型，可能无法正常去除非法字符！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\error.py:9
msgid "项目代码错误"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\retry.py:19
#, python-brace-format
msgid "正在进行第 {index} 次重试"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\retry.py:48
msgid ""
"如需重新尝试处理该对象，请关闭所有正在访问该对象的窗口或程序，然后直接按下回"
"车键！\n"
"如需跳过处理该对象，请输入任意字符后按下回车键！"
msgstr ""

#: C:\Users\You\PycharmProjects\TikTokDownloader\src\tools\retry.py:63
msgid "请关闭所有正在访问该对象的窗口或程序，然后按下回车键继续处理！"
msgstr ""

msgid ""
"\n"
"项目默认无需令牌；公开部署时，建议设置令牌以防止恶意请求！\n"
"\n"
"令牌设置位置：`src/custom/function.py` - `is_valid_token()`\n"
msgstr ""

msgid ""
"\n"
"更新项目配置文件 settings.json\n"
"\n"
"仅需传入需要更新的配置参数\n"
"\n"
"返回更新后的全部配置参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **text**: 包含分享链接的字符串；必需参数\n"
"- **proxy**: 代理；可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: 抖音作品 ID；必需参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **sec_user_id**: 抖音账号 sec_uid；必需参数\n"
"- **tab**: 账号页面类型；可选参数，默认值：`post`\n"
"- **earliest**: 作品最早发布日期；可选参数\n"
"- **latest**: 作品最晚发布日期；可选参数\n"
"- **pages**: 最大请求次数，仅对请求账号喜欢页数据有效；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **mix_id**: 抖音合集 ID\n"
"- **detail_id**: 属于合集的抖音作品 ID\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
"\n"
"**`mix_id` 和 `detail_id` 二选一，只需传入其中之一即可**\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **web_rid**: 抖音直播 web_rid\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **web_rid**: 抖音直播 web_rid\n"
"- **room_id**: 抖音直播 room_id\n"
"- **sec_user_id**: 抖音直播账号 sec_user_id\n"
"\n"
"**本接口支持两种参数传入方式**:\n"
"\n"
"- 方式一 ：传入 `web_rid`\n"
"- 方式二 ：同时传入 `room_id` 和 `sec_user_id`\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: 抖音作品 ID；必需参数\n"
"- **pages**: 最大请求次数；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
"- **count_reply**: 可选参数\n"
"- **reply**: 可选参数，默认值：False\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: 抖音作品 ID；必需参数\n"
"- **comment_id**: 评论 ID；必需参数\n"
"- **pages**: 最大请求次数；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
"- **sort_type**: 排序依据；可选参数\n"
"- **publish_time**: 发布时间；可选参数\n"
"- **duration**: 视频时长；可选参数\n"
"- **search_range**: 搜索范围；可选参数\n"
"- **content_type**: 内容形式；可选参数\n"
"\n"
"**部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/"
"TikTokDownloader/wiki/"
"Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
"- **sort_type**: 排序依据；可选参数\n"
"- **publish_time**: 发布时间；可选参数\n"
"- **duration**: 视频时长；可选参数\n"
"- **search_range**: 搜索范围；可选参数\n"
"\n"
"**部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/"
"TikTokDownloader/wiki/"
"Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
"- **douyin_user_fans**: 粉丝数量；可选参数\n"
"- **douyin_user_type**: 用户类型；可选参数\n"
"\n"
"**部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/"
"TikTokDownloader/wiki/"
"Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: 抖音 Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **keyword**: 关键词；必需参数\n"
"- **offset**: 起始页码；可选参数\n"
"- **count**: 数据数量；可选参数\n"
"- **pages**: 总页数；可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **detail_id**: TikTok 作品 ID；必需参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **sec_user_id**: TikTok 账号 secUid；必需参数\n"
"- **tab**: 账号页面类型；可选参数，默认值：`post`\n"
"- **earliest**: 作品最早发布日期；可选参数\n"
"- **latest**: 作品最晚发布日期；可选参数\n"
"- **pages**: 最大请求次数，仅对请求账号喜欢页数据有效；可选参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **mix_id**: TikTok 合集 ID；必需参数\n"
"- **cursor**: 可选参数\n"
"- **count**: 可选参数\n"
msgstr ""

msgid ""
"\n"
"**参数**:\n"
"\n"
"- **cookie**: TikTok Cookie；可选参数\n"
"- **proxy**: 代理；可选参数\n"
"- **source**: 是否返回原始响应数据；可选参数，默认值：False\n"
"- **room_id**: TikTok 直播 room_id；必需参数\n"
msgstr ""
```

## File: `src/application/main_monitor.py`
```python
from contextlib import suppress
from typing import TYPE_CHECKING
from asyncio import Event, create_task, gather, sleep, Queue, QueueEmpty
from .main_terminal import TikTok
from ..translation import _
from pyperclip import copy, paste

if TYPE_CHECKING:
    from ..config import Parameter
    from ..manager import Database

__all__ = ["ClipboardMonitor", "PostMonitor"]


class ClipboardMonitor(TikTok):
    def __init__(
        self,
        parameter: "Parameter",
        database: "Database",
        server_mode: bool = True,
    ):
        super().__init__(
            parameter,
            database,
            server_mode,
        )
        self.event_clipboard = Event()
        self.clipboard_cache = ""
        self.queue_dy = Queue()
        self.queue_tk = Queue()

    async def run(self, run_command: list):
        await self.start_listener()

    async def start_listener(
        self,
        delay: int | float = 1,
    ):
        self.console.info(
            _(
                "程序会自动检测并提取剪贴板中的抖音和 TikTok 作品链接，并自动下载作品文件；如需关闭，请按下 Ctrl+C，或将剪贴板内容设置为“close”以停止监听！"
            ),
        )
        copy("")
        self.event_clipboard.clear()
        await gather(
            self.check_clipboard(
                delay=delay,
            ),
            self.deal_tasks(
                delay=delay,
            ),
            self.deal_tasks_tiktok(
                delay=delay,
            ),
        )

    async def stop_listener(self):
        self.console.debug("停止监听剪贴板！")
        self.event_clipboard.set()

    async def check_clipboard(
        self,
        delay: int | float = 1,
    ):
        self.console.debug("开始监听剪贴板！")
        while not self.event_clipboard.is_set():
            if (c := paste()).lower() == "close":
                await self.stop_listener()
            elif c != self.clipboard_cache:
                self.clipboard_cache = c
                create_task(self.check_link(c))
            await sleep(delay)

    async def check_link(
        self,
        text: str,
    ):
        links = text.split()
        for i in links:
            if "douyin" in i:
                self.console.debug(f"处理抖音链接: {i}")
                await self.queue_dy.put(i)
            elif "tiktok" in i:
                self.console.debug(f"处理 TikTok 链接: {i}")
                await self.queue_tk.put(i)

    async def deal_tasks(
        self,
        delay: int | float = 1,
    ):
        await self._deal_tasks(
            self.parameter.douyin_platform,
            self.queue_dy,
            self.links,
            False,
            delay,
        )

    async def deal_tasks_tiktok(
        self,
        delay: int | float = 1,
    ):
        await self._deal_tasks(
            self.parameter.tiktok_platform,
            self.queue_tk,
            self.links_tiktok,
            True,
            delay,
        )

    async def _deal_tasks(
        self,
        enable: bool,
        queue: Queue,
        link_object,
        tiktok: bool,
        delay: int | float = 1,
    ):
        if not enable:
            return
        root, params, logger = self.record.run(self.parameter, blank=True)
        async with logger(root, console=self.console, **params) as record:
            while not self.event_clipboard.is_set() or queue.qsize() > 0:
                with suppress(QueueEmpty):
                    url = queue.get_nowait()
                    id_ = await link_object.run(url)
                    if not any(id_):
                        self.logger.warning(_("{url} 提取作品 ID 失败").format(url=url))
                    else:
                        await self._handle_detail(
                            id_,
                            tiktok,
                            record,
                        )
                await sleep(delay)


class PostMonitor(TikTok):
    def __init__(
        self,
        parameter: "Parameter",
        database: "Database",
        server_mode: bool = True,
    ):
        super().__init__(
            parameter,
            database,
            server_mode,
        )
```

## File: `src/application/main_server.py`
```python
from textwrap import dedent
from typing import TYPE_CHECKING

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.responses import RedirectResponse
from uvicorn import Config, Server

from ..custom import (
    __VERSION__,
    REPOSITORY,
    SERVER_HOST,
    SERVER_PORT,
    VERSION_BETA,
    is_valid_token,
)
from ..models import (
    Account,
    AccountTiktok,
    Comment,
    DataResponse,
    Detail,
    DetailTikTok,
    GeneralSearch,
    Live,
    LiveSearch,
    LiveTikTok,
    Mix,
    MixTikTok,
    Reply,
    Settings,
    ShortUrl,
    UrlResponse,
    UserSearch,
    VideoSearch,
)
from ..translation import _
from .main_terminal import TikTok

if TYPE_CHECKING:
    from ..config import Parameter
    from ..manager import Database

__all__ = ["APIServer"]


def token_dependency(token: str = Header(None)):
    if not is_valid_token(token):
        raise HTTPException(
            status_code=403,
            detail=_("验证失败！"),
        )


class APIServer(TikTok):
    def __init__(
        self,
        parameter: "Parameter",
        database: "Database",
        server_mode: bool = True,
    ):
        super().__init__(
            parameter,
            database,
            server_mode,
        )
        self.server = None

    async def handle_redirect(self, text: str, proxy: str = None) -> str:
        return await self.links.run(
            text,
            "",
            proxy,
        )

    async def handle_redirect_tiktok(self, text: str, proxy: str = None) -> str:
        return await self.links_tiktok.run(
            text,
            "",
            proxy,
        )

    async def run_server(
        self,
        host=SERVER_HOST,
        port=SERVER_PORT,
        log_level="info",
    ):
        self.server = FastAPI(
            debug=VERSION_BETA,
            title="DouK-Downloader",
            version=__VERSION__,
        )
        self.setup_routes()
        config = Config(
            self.server,
            host=host,
            port=port,
            log_level=log_level,
        )
        server = Server(config)
        await server.serve()

    def setup_routes(self):
        @self.server.get(
            "/",
            summary=_("访问项目 GitHub 仓库"),
            description=_("重定向至项目 GitHub 仓库主页"),
            tags=[_("项目")],
        )
        async def index():
            return RedirectResponse(url=REPOSITORY)

        @self.server.get(
            "/token",
            summary=_("测试令牌有效性"),
            description=_(
                dedent("""
                项目默认无需令牌；公开部署时，建议设置令牌以防止恶意请求！
                
                令牌设置位置：`src/custom/function.py` - `is_valid_token()`
                """)
            ),
            tags=[_("项目")],
            response_model=DataResponse,
        )
        async def handle_test(token: str = Depends(token_dependency)):
            return DataResponse(
                message=_("验证成功！"),
                data=None,
                params=None,
            )

        @self.server.post(
            "/settings",
            summary=_("更新项目全局配置"),
            description=_(
                dedent("""
                更新项目配置文件 settings.json
                
                仅需传入需要更新的配置参数
                
                返回更新后的全部配置参数
                """)
            ),
            tags=[_("配置")],
            response_model=Settings,
        )
        async def handle_settings(
            extract: Settings, token: str = Depends(token_dependency)
        ):
            await self.parameter.set_settings_data(extract.model_dump())
            return Settings(**self.parameter.get_settings_data())

        @self.server.get(
            "/settings",
            summary=_("获取项目全局配置"),
            description=_("返回项目全部配置参数"),
            tags=[_("配置")],
            response_model=Settings,
        )
        async def get_settings(token: str = Depends(token_dependency)):
            return Settings(**self.parameter.get_settings_data())

        @self.server.post(
            "/douyin/share",
            summary=_("获取分享链接重定向的完整链接"),
            description=_(
                dedent("""
                **参数**:
                
                - **text**: 包含分享链接的字符串；必需参数
                - **proxy**: 代理；可选参数
                """)
            ),
            tags=[_("抖音")],
            response_model=UrlResponse,
        )
        async def handle_share(
            extract: ShortUrl, token: str = Depends(token_dependency)
        ):
            if url := await self.handle_redirect(extract.text, extract.proxy):
                return UrlResponse(
                    message=_("请求链接成功！"),
                    url=url,
                    params=extract.model_dump(),
                )
            return UrlResponse(
                message=_("请求链接失败！"),
                url=None,
                params=extract.model_dump(),
            )

        @self.server.post(
            "/douyin/detail",
            summary=_("获取单个作品数据"),
            description=_(
                dedent("""
                **参数**:
                
                - **cookie**: 抖音 Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **detail_id**: 抖音作品 ID；必需参数
                """)
            ),
            tags=[_("抖音")],
            response_model=DataResponse,
        )
        async def handle_detail(
            extract: Detail, token: str = Depends(token_dependency)
        ):
            return await self.handle_detail(extract, False)

        @self.server.post(
            "/douyin/account",
            summary=_("获取账号作品数据"),
            description=_(
                dedent("""
                **参数**:
                
                - **cookie**: 抖音 Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **sec_user_id**: 抖音账号 sec_uid；必需参数
                - **tab**: 账号页面类型；可选参数，默认值：`post`
                - **earliest**: 作品最早发布日期；可选参数
                - **latest**: 作品最晚发布日期；可选参数
                - **pages**: 最大请求次数，仅对请求账号喜欢页数据有效；可选参数
                - **cursor**: 可选参数
                - **count**: 可选参数
                """)
            ),
            tags=[_("抖音")],
            response_model=DataResponse,
        )
        async def handle_account(
            extract: Account, token: str = Depends(token_dependency)
        ):
            return await self.handle_account(extract, False)

        @self.server.post(
            "/douyin/mix",
            summary=_("获取合集作品数据"),
            description=_(
                dedent("""
                **参数**:
                
                - **cookie**: 抖音 Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **mix_id**: 抖音合集 ID
                - **detail_id**: 属于合集的抖音作品 ID
                - **cursor**: 可选参数
                - **count**: 可选参数
                
                **`mix_id` 和 `detail_id` 二选一，只需传入其中之一即可**
                """)
            ),
            tags=[_("抖音")],
            response_model=DataResponse,
        )
        async def handle_mix(extract: Mix, token: str = Depends(token_dependency)):
            is_mix, id_ = self.generate_mix_params(
                extract.mix_id,
                extract.detail_id,
            )
            if not isinstance(is_mix, bool):
                return DataResponse(
                    message=_("参数错误！"),
                    data=None,
                    params=extract.model_dump(),
                )
            if data := await self.deal_mix_detail(
                is_mix,
                id_,
                api=True,
                source=extract.source,
                cookie=extract.cookie,
                proxy=extract.proxy,
                cursor=extract.cursor,
                count=extract.count,
            ):
                return self.success_response(extract, data)
            return self.failed_response(extract)

        @self.server.post(
            "/douyin/live",
            summary=_("获取直播数据"),
            description=_(
                dedent("""
                **参数**:
                
                - **cookie**: 抖音 Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **web_rid**: 抖音直播 web_rid
                """)
            ),
            tags=[_("抖音")],
            response_model=DataResponse,
        )
        async def handle_live(extract: Live, token: str = Depends(token_dependency)):
            # if self.check_live_params(
            #     extract.web_rid,
            #     extract.room_id,
            #     extract.sec_user_id,
            # ):
            #     if data := await self.handle_live(
            #         extract,
            #     ):
            #         return self.success_response(extract, data[0])
            #     return self.failed_response(extract)
            # return DataResponse(
            #     message=_("参数错误！"),
            #     data=None,
            #     params=extract.model_dump(),
            # )
            if data := await self.handle_live(
                extract,
            ):
                return self.success_response(extract, data[0])
            return self.failed_response(extract)

        @self.server.post(
            "/douyin/comment",
            summary=_("获取作品评论数据"),
            description=_(
                dedent("""
                **参数**:
                
                - **cookie**: 抖音 Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **detail_id**: 抖音作品 ID；必需参数
                - **pages**: 最大请求次数；可选参数
                - **cursor**: 可选参数
                - **count**: 可选参数
                - **count_reply**: 可选参数
                - **reply**: 可选参数，默认值：False
                """)
            ),
            tags=[_("抖音")],
            response_model=DataResponse,
        )
        async def handle_comment(
            extract: Comment, token: str = Depends(token_dependency)
        ):
            if data := await self.comment_handle_single(
                extract.detail_id,
                cookie=extract.cookie,
                proxy=extract.proxy,
                source=extract.source,
                pages=extract.pages,
                cursor=extract.cursor,
                count=extract.count,
                count_reply=extract.count_reply,
                reply=extract.reply,
            ):
                return self.success_response(extract, data)
            return self.failed_response(extract)

        @self.server.post(
            "/douyin/reply",
            summary=_("获取评论回复数据"),
            description=_(
                dedent("""
                **参数**:
                
                - **cookie**: 抖音 Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **detail_id**: 抖音作品 ID；必需参数
                - **comment_id**: 评论 ID；必需参数
                - **pages**: 最大请求次数；可选参数
                - **cursor**: 可选参数
                - **count**: 可选参数
                """)
            ),
            tags=[_("抖音")],
            response_model=DataResponse,
        )
        async def handle_reply(extract: Reply, token: str = Depends(token_dependency)):
            if data := await self.reply_handle(
                extract.detail_id,
                extract.comment_id,
                cookie=extract.cookie,
                proxy=extract.proxy,
                pages=extract.pages,
                cursor=extract.cursor,
                count=extract.count,
                source=extract.source,
            ):
                return self.success_response(extract, data)
            return self.failed_response(extract)

        @self.server.post(
            "/douyin/search/general",
            summary=_("获取综合搜索数据"),
            description=_(
                dedent("""
                **参数**:
                
                - **cookie**: 抖音 Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **keyword**: 关键词；必需参数
                - **offset**: 起始页码；可选参数
                - **count**: 数据数量；可选参数
                - **pages**: 总页数；可选参数
                - **sort_type**: 排序依据；可选参数
                - **publish_time**: 发布时间；可选参数
                - **duration**: 视频时长；可选参数
                - **search_range**: 搜索范围；可选参数
                - **content_type**: 内容形式；可选参数
                
                **部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)
                """)
            ),
            tags=[_("抖音")],
            response_model=DataResponse,
        )
        async def handle_search_general(
            extract: GeneralSearch, token: str = Depends(token_dependency)
        ):
            return await self.handle_search(extract)

        @self.server.post(
            "/douyin/search/video",
            summary=_("获取视频搜索数据"),
            description=_(
                dedent("""
                **参数**:
                
                - **cookie**: 抖音 Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **keyword**: 关键词；必需参数
                - **offset**: 起始页码；可选参数
                - **count**: 数据数量；可选参数
                - **pages**: 总页数；可选参数
                - **sort_type**: 排序依据；可选参数
                - **publish_time**: 发布时间；可选参数
                - **duration**: 视频时长；可选参数
                - **search_range**: 搜索范围；可选参数
                
                **部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)
                """)
            ),
            tags=[_("抖音")],
            response_model=DataResponse,
        )
        async def handle_search_video(
            extract: VideoSearch, token: str = Depends(token_dependency)
        ):
            return await self.handle_search(extract)

        @self.server.post(
            "/douyin/search/user",
            summary=_("获取用户搜索数据"),
            description=_(
                dedent("""
                **参数**:
                
                - **cookie**: 抖音 Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **keyword**: 关键词；必需参数
                - **offset**: 起始页码；可选参数
                - **count**: 数据数量；可选参数
                - **pages**: 总页数；可选参数
                - **douyin_user_fans**: 粉丝数量；可选参数
                - **douyin_user_type**: 用户类型；可选参数
                
                **部分参数传入规则请查阅文档**: [参数含义](https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation#%E9%87%87%E9%9B%86%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E6%8A%96%E9%9F%B3)
                """)
            ),
            tags=[_("抖音")],
            response_model=DataResponse,
        )
        async def handle_search_user(
            extract: UserSearch, token: str = Depends(token_dependency)
        ):
            return await self.handle_search(extract)

        @self.server.post(
            "/douyin/search/live",
            summary=_("获取直播搜索数据"),
            description=_(
                dedent("""
                **参数**:
                
                - **cookie**: 抖音 Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **keyword**: 关键词；必需参数
                - **offset**: 起始页码；可选参数
                - **count**: 数据数量；可选参数
                - **pages**: 总页数；可选参数
                """)
            ),
            tags=[_("抖音")],
            response_model=DataResponse,
        )
        async def handle_search_live(
            extract: LiveSearch, token: str = Depends(token_dependency)
        ):
            return await self.handle_search(extract)

        @self.server.post(
            "/tiktok/share",
            summary=_("获取分享链接重定向的完整链接"),
            description=_(
                dedent("""
            **参数**:

            - **text**: 包含分享链接的字符串；必需参数
            - **proxy**: 代理；可选参数
            """)
            ),
            tags=["TikTok"],
            response_model=UrlResponse,
        )
        async def handle_share_tiktok(
            extract: ShortUrl, token: str = Depends(token_dependency)
        ):
            if url := await self.handle_redirect_tiktok(extract.text, extract.proxy):
                return UrlResponse(
                    message=_("请求链接成功！"),
                    url=url,
                    params=extract.model_dump(),
                )
            return UrlResponse(
                message=_("请求链接失败！"),
                url=None,
                params=extract.model_dump(),
            )

        @self.server.post(
            "/tiktok/detail",
            summary=_("获取单个作品数据"),
            description=_(
                dedent("""
                **参数**:

                - **cookie**: TikTok Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **detail_id**: TikTok 作品 ID；必需参数
                """)
            ),
            tags=["TikTok"],
            response_model=DataResponse,
        )
        async def handle_detail_tiktok(
            extract: DetailTikTok, token: str = Depends(token_dependency)
        ):
            return await self.handle_detail(extract, True)

        @self.server.post(
            "/tiktok/account",
            summary=_("获取账号作品数据"),
            description=_(
                dedent("""
                **参数**:

                - **cookie**: TikTok Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **sec_user_id**: TikTok 账号 secUid；必需参数
                - **tab**: 账号页面类型；可选参数，默认值：`post`
                - **earliest**: 作品最早发布日期；可选参数
                - **latest**: 作品最晚发布日期；可选参数
                - **pages**: 最大请求次数，仅对请求账号喜欢页数据有效；可选参数
                - **cursor**: 可选参数
                - **count**: 可选参数
                """)
            ),
            tags=["TikTok"],
            response_model=DataResponse,
        )
        async def handle_account_tiktok(
            extract: AccountTiktok, token: str = Depends(token_dependency)
        ):
            return await self.handle_account(extract, True)

        @self.server.post(
            "/tiktok/mix",
            summary=_("获取合辑作品数据"),
            description=_(
                dedent("""
                **参数**:

                - **cookie**: TikTok Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **mix_id**: TikTok 合集 ID；必需参数
                - **cursor**: 可选参数
                - **count**: 可选参数
                """)
            ),
            tags=["TikTok"],
            response_model=DataResponse,
        )
        async def handle_mix_tiktok(
            extract: MixTikTok, token: str = Depends(token_dependency)
        ):
            if data := await self.deal_mix_detail(
                True,
                extract.mix_id,
                api=True,
                source=extract.source,
                cookie=extract.cookie,
                proxy=extract.proxy,
                cursor=extract.cursor,
                count=extract.count,
            ):
                return self.success_response(extract, data)
            return self.failed_response(extract)

        @self.server.post(
            "/tiktok/live",
            summary=_("获取直播数据"),
            description=_(
                dedent("""
                **参数**:

                - **cookie**: TikTok Cookie；可选参数
                - **proxy**: 代理；可选参数
                - **source**: 是否返回原始响应数据；可选参数，默认值：False
                - **room_id**: TikTok 直播 room_id；必需参数
                """)
            ),
            tags=["TikTok"],
            response_model=DataResponse,
        )
        async def handle_live_tiktok(
            extract: Live, token: str = Depends(token_dependency)
        ):
            if data := await self.handle_live(
                extract,
                True,
            ):
                return self.success_response(extract, data[0])
            return self.failed_response(extract)

    async def handle_search(self, extract):
        if isinstance(
            data := await self.deal_search_data(
                extract,
                extract.source,
            ),
            list,
        ):
            return self.success_response(
                extract,
                *(data, None) if any(data) else (None, _("搜索结果为空！")),
            )
        return self.failed_response(extract)

    async def handle_detail(
        self,
        extract: Detail | DetailTikTok,
        tiktok=False,
    ):
        root, params, logger = self.record.run(self.parameter)
        async with logger(root, console=self.console, **params) as record:
            if data := await self._handle_detail(
                [extract.detail_id],
                tiktok,
                record,
                True,
                extract.source,
                extract.cookie,
                extract.proxy,
            ):
                return self.success_response(extract, data[0])
            return self.failed_response(extract)

    async def handle_account(
        self,
        extract: Account | AccountTiktok,
        tiktok=False,
    ):
        if data := await self.deal_account_detail(
            0,
            extract.sec_user_id,
            tab=extract.tab,
            earliest=extract.earliest,
            latest=extract.latest,
            pages=extract.pages,
            api=True,
            source=extract.source,
            cookie=extract.cookie,
            proxy=extract.proxy,
            tiktok=tiktok,
            cursor=extract.cursor,
            count=extract.count,
        ):
            return self.success_response(extract, data)
        return self.failed_response(extract)

    @staticmethod
    def success_response(
        extract,
        data: dict | list[dict],
        message: str = None,
    ):
        return DataResponse(
            message=message or _("获取数据成功！"),
            data=data,
            params=extract.model_dump(),
        )

    @staticmethod
    def failed_response(
        extract,
        message: str = None,
    ):
        return DataResponse(
            message=message or _("获取数据失败！"),
            data=None,
            params=extract.model_dump(),
        )

    @staticmethod
    def generate_mix_params(mix_id: str = None, detail_id: str = None):
        if mix_id:
            return True, mix_id
        return (False, detail_id) if detail_id else (None, None)

    @staticmethod
    def check_live_params(
        web_rid: str = None,
        room_id: str = None,
        sec_user_id: str = None,
    ) -> bool:
        return bool(web_rid or room_id and sec_user_id)

    async def handle_live(self, extract: Live | LiveTikTok, tiktok=False):
        if tiktok:
            data = await self.get_live_data_tiktok(
                extract.room_id,
                extract.cookie,
                extract.proxy,
            )
        else:
            data = await self.get_live_data(
                extract.web_rid,
                # extract.room_id,
                # extract.sec_user_id,
                cookie=extract.cookie,
                proxy=extract.proxy,
            )
        if extract.source:
            return [data]
        return await self.extractor.run(
            [data],
            None,
            "live",
            tiktok=tiktok,
        )
```

## File: `src/application/main_terminal.py`
```python
from datetime import date, datetime
from pathlib import Path
from platform import system
from time import time
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any, Callable, Union

from pydantic import ValidationError

# from ..custom import failure_handling
from ..custom import suspend
from ..downloader import Downloader
from ..extract import Extractor
from ..interface import (
    API,
    Account,
    AccountTikTok,
    Collection,
    # CommentTikTok,
    Collects,
    CollectsDetail,
    CollectsMix,
    # CollectsSeries,
    CollectsMusic,
    Comment,
    Detail,
    DetailTikTok,
    HashTag,
    Hot,
    Info,
    InfoTikTok,
    Live,
    LiveTikTok,
    Mix,
    MixTikTok,
    Reply,
    Search,
    User,
)
from ..link import Extractor as LinkExtractor
from ..link import ExtractorTikTok
from ..manager import Cache
from ..models import (
    GeneralSearch,
    LiveSearch,
    UserSearch,
    VideoSearch,
)
from ..module import DetailTikTokExtractor, DetailTikTokUnofficial
from ..storage import RecordManager
from ..tools import DownloaderError, choose, safe_pop
from ..translation import _

if TYPE_CHECKING:
    from pydantic import BaseModel

    from ..config import Parameter
    from ..manager import Database

__all__ = [
    "TikTok",
]


def check_storage_format(function):
    async def inner(self, *args, **kwargs):
        if self.parameter.storage_format:
            return await function(self, *args, **kwargs)
        self.console.warning(
            _(
                "未设置 storage_format 参数，无法正常使用该功能，详细说明请查阅项目文档！"
            ),
        )

    return inner


def check_cookie_state(tiktok=False):
    def check_cookie(function):
        async def inner(self, *args, **kwargs):
            if tiktok:
                params = self.parameter.cookie_tiktok_state
                tip = "TikTok Cookie"
            else:
                params = self.parameter.cookie_state
                tip = _("抖音 Cookie")
            if params:
                return await function(self, *args, **kwargs)
            self.console.warning(
                _("{tip} 未登录，无法使用该功能，详细说明请查阅项目文档！").format(
                    tip=tip
                ),
            )

        return inner

    return check_cookie


class TikTok:
    ENCODE = "UTF-8-SIG" if system() == "Windows" else "UTF-8"

    def __init__(
        self,
        parameter: "Parameter",
        database: "Database",
        server_mode: bool = False,
    ):
        self.run_command = None
        self.parameter = parameter
        self.database = database
        self.console = parameter.console
        self.logger = parameter.logger
        API.init_progress_object(
            server_mode,
        )
        self.links = LinkExtractor(parameter)
        self.links_tiktok = ExtractorTikTok(parameter)
        self.downloader = Downloader(
            parameter,
            server_mode,
        )
        self.extractor = Extractor(parameter)
        self.storage = bool(parameter.storage_format)
        self.record = RecordManager()
        self.settings = parameter.settings
        self.accounts = parameter.accounts_urls
        self.accounts_tiktok = parameter.accounts_urls_tiktok
        self.mix = parameter.mix_urls
        self.mix_tiktok = parameter.mix_urls_tiktok
        self.owner = parameter.owner_url
        self.owner_tiktok = parameter.owner_url_tiktok
        self.running = True
        self.ffmpeg = parameter.ffmpeg.state
        self.cache = Cache(
            parameter,
            self.database,
            "mark" in parameter.name_format,
            "nickname" in parameter.name_format,
        )
        self.__function = (
            (
                _("批量下载账号作品(抖音)"),
                self.account_acquisition_interactive,
            ),
            (
                _("批量下载链接作品(抖音)"),
                self.detail_interactive,
            ),
            (
                _("获取直播拉流地址(抖音)"),
                self.live_interactive,
            ),
            (
                _("采集作品评论数据(抖音)"),
                self.comment_interactive,
            ),
            (
                _("批量下载合集作品(抖音)"),
                self.mix_interactive,
            ),
            (
                _("采集账号详细数据(抖音)"),
                self.user_interactive,
            ),
            (
                _("采集搜索结果数据(抖音)"),
                self.search_interactive,
            ),
            (
                _("采集抖音热榜数据(抖音)"),
                self.hot_interactive,
            ),
            # (_("批量下载话题作品(抖音)"),),
            (
                _("批量下载收藏作品(抖音)"),
                self.collection_interactive,
            ),
            (
                _("批量下载收藏音乐(抖音)"),
                self.collection_music_interactive,
            ),
            # (_("批量下载收藏短剧(抖音)"),),
            (
                _("批量下载收藏夹作品(抖音)"),
                self.collects_interactive,
            ),
            (
                _("批量下载账号作品(TikTok)"),
                self.account_acquisition_interactive_tiktok,
            ),
            (
                _("批量下载链接作品(TikTok)"),
                self.detail_interactive_tiktok,
            ),
            (
                _("批量下载合集作品(TikTok)"),
                self.mix_interactive_tiktok,
            ),
            (
                _("获取直播拉流地址(TikTok)"),
                self.live_interactive_tiktok,
            ),
            # (_("采集作品评论数据(TikTok)"), self.comment_interactive_tiktok,),
            # (
            #     _("批量下载视频原画(TikTok)"),
            #     self.detail_interactive_tiktok_unofficial,
            # ),
        )
        self.__function_account = (
            (_("使用 accounts_urls 参数的账号链接(推荐)"), self.account_detail_batch),
            (_("手动输入待采集的账号链接"), self.account_detail_inquire),
            (_("从文本文档读取待采集的账号链接"), self.account_detail_txt),
        )
        self.__function_account_tiktok = (
            (
                _("使用 accounts_urls_tiktok 参数的账号链接(推荐)"),
                self.account_detail_batch_tiktok,
            ),
            (_("手动输入待采集的账号链接"), self.account_detail_inquire_tiktok),
            (_("从文本文档读取待采集的账号链接"), self.account_detail_txt_tiktok),
        )
        self.__function_mix = (
            (_("使用 mix_urls 参数的合集链接(推荐)"), self.mix_batch),
            (_("获取当前账号收藏合集列表"), self.mix_collection),
            (_("手动输入待采集的合集/作品链接"), self.mix_inquire),
            (_("从文本文档读取待采集的合集/作品链接"), self.mix_txt),
        )
        self.__function_mix_tiktok = (
            (_("使用 mix_urls_tiktok 参数的合集链接(推荐)"), self.mix_batch_tiktok),
            (_("手动输入待采集的合集/作品链接"), self.mix_inquire_tiktok),
            (_("从文本文档读取待采集的合集/作品链接"), self.mix_txt_tiktok),
        )
        self.__function_user = (
            (_("使用 accounts_urls 参数的账号链接"), self.user_batch),
            (_("手动输入待采集的账号链接"), self.user_inquire),
            (_("从文本文档读取待采集的账号链接"), self.user_txt),
        )
        self.__function_detail = (
            (_("手动输入待采集的作品链接"), self.__detail_inquire),
            (_("从文本文档读取待采集的作品链接"), self.__detail_txt),
        )
        self.__function_detail_tiktok = (
            (_("手动输入待采集的作品链接"), self.__detail_inquire_tiktok),
            (_("从文本文档读取待采集的作品链接"), self.__detail_txt_tiktok),
        )
        self.__function_detail_tiktok_unofficial = (
            (_("手动输入待采集的作品链接"), self.__detail_inquire_tiktok_unofficial),
            (_("从文本文档读取待采集的作品链接"), self.__detail_txt_tiktok_unofficial),
        )
        self.__function_comment = (
            (_("手动输入待采集的作品链接"), self.__comment_inquire),
            (_("从文本文档读取待采集的作品链接"), self.__comment_txt),
        )
        self.__function_comment_tiktok = (
            (_("手动输入待采集的作品链接"), self.__comment_inquire_tiktok),
            # (_("从文本文档读取待采集的作品链接"), self.__comment_txt_tiktok),
        )
        self.__function_search = (
            (
                _("综合搜索数据采集"),
                self._search_interactive_general,
            ),
            (
                _("视频搜索数据采集"),
                self._search_interactive_video,
            ),
            (
                _("用户搜索数据采集"),
                self._search_interactive_user,
            ),
            (
                _("直播搜索数据采集"),
                self._search_interactive_live,
            ),
        )

    def _inquire_input(
        self,
        tip: str = "",
        problem: str = "",
    ) -> str:
        text = self.console.input(problem or _("请输入{tip}链接: ").format(tip=tip))
        if not text:
            return ""
        elif text.upper() == "Q":
            self.running = False
            return ""
        return text

    async def account_acquisition_interactive_tiktok(
        self,
        select="",
    ):
        await self.__secondary_menu(
            _("请选择账号链接来源"),
            function=self.__function_account_tiktok,
            select=select or safe_pop(self.run_command),
        )
        self.logger.info(_("已退出批量下载账号作品(TikTok)模式"))

    def __summarize_results(self, count: SimpleNamespace, name=_("账号")):
        time_ = time() - count.time
        self.logger.info(
            _(
                "程序共处理 {0} 个{1}，成功 {2} 个，失败 {3} 个，耗时 {4} 分钟 {5} 秒"
            ).format(
                count.success + count.failed,
                name,
                count.success,
                count.failed,
                int(time_ // 60),
                int(time_ % 60),
            )
        )

    async def account_acquisition_interactive(
        self,
        select="",
    ):
        await self.__secondary_menu(
            _("请选择账号链接来源"),
            function=self.__function_account,
            select=select or safe_pop(self.run_command),
        )
        self.logger.info(_("已退出批量下载账号作品(抖音)模式"))

    async def __secondary_menu(
        self,
        problem=_("请选择账号链接来源"),
        function=...,
        select: str | int = ...,
        *args,
        **kwargs,
    ):
        if not select:
            select = choose(
                problem,
                [i[0] for i in function],
                self.console,
            )
        if select.upper() == "Q":
            self.running = False
        try:
            n = int(select) - 1
        except ValueError:
            return
        if n in range(len(function)):
            await function[n][1](
                *args,
                **kwargs,
            )

    async def account_detail_batch(
        self,
        *args,
    ):
        await self.__account_detail_batch(
            self.accounts,
            "accounts_urls",
            False,
        )

    async def account_detail_batch_tiktok(
        self,
        *args,
    ):
        await self.__account_detail_batch(
            self.accounts_tiktok,
            "accounts_urls_tiktok",
            True,
        )

    async def __account_detail_batch(
        self,
        accounts: list[SimpleNamespace],
        params_name: str,
        tiktok: bool,
    ) -> None:
        count = SimpleNamespace(time=time(), success=0, failed=0)
        self.logger.info(
            _("共有 {count} 个账号的作品等待下载").format(count=len(accounts))
        )
        for index, data in enumerate(accounts, start=1):
            if not (
                sec_user_id := await self.check_sec_user_id(
                    data.url,
                    tiktok,
                )
            ):
                self.logger.warning(
                    _(
                        "配置文件 {name} 参数的 url {url} 提取 sec_user_id 失败，错误配置：{data}"
                    ).format(
                        name=params_name,
                        url=data.url,
                        data=vars(data),
                    )
                )
                count.failed += 1
                continue
            if not await self.deal_account_detail(
                index,
                **vars(data) | {"sec_user_id": sec_user_id},
                tiktok=tiktok,
            ):
                count.failed += 1
                continue
            # break  # 调试代码
            count.success += 1
            if index != len(accounts):
                await suspend(index, self.console)
        self.__summarize_results(
            count,
            _("账号"),
        )

    async def check_sec_user_id(
        self,
        sec_user_id: str,
        tiktok=False,
    ) -> str:
        match tiktok:
            case True:
                sec_user_id = await self.links_tiktok.run(sec_user_id, "user")
            case False:
                sec_user_id = await self.links.run(sec_user_id, "user")
        return sec_user_id[0] if len(sec_user_id) > 0 else ""

    async def account_detail_inquire(
        self,
        *args,
    ):
        while url := self._inquire_input(_("账号主页")):
            links = await self.links.run(url, "user")
            if not links:
                self.logger.warning(
                    _("{url} 提取账号 sec_user_id 失败").format(url=url)
                )
                continue
            await self.__account_detail_handle(
                links,
                False,
                *args,
            )

    async def account_detail_inquire_tiktok(
        self,
        *args,
    ):
        while url := self._inquire_input(_("账号主页")):
            links = await self.links_tiktok.run(url, "user")
            if not links:
                self.logger.warning(
                    _("{url} 提取账号 sec_user_id 失败").format(url=url)
                )
                continue
            await self.__account_detail_handle(
                links,
                True,
                *args,
            )

    async def account_detail_txt(
        self,
    ):
        await self._read_from_txt(
            tiktok=False,
            type_="user",
            error=_("从文本文档提取账号 sec_user_id 失败"),
            callback=self.__account_detail_handle,
        )

    async def _read_from_txt(
        self,
        tiktok=False,
        type_: str = ...,
        error: str = ...,
        callback: Callable = ...,
        *args,
        **kwargs,
    ):
        if not (url := self.txt_inquire()):
            return
        link_obj = self.links_tiktok if tiktok else self.links
        links = await link_obj.run(
            url,
            type_,
        )
        if not links or not isinstance(links[0], bool | None):
            links = [links]
        if not links[-1]:
            self.logger.warning(error)
            return
        await callback(
            *links,
            *args,
            tiktok=tiktok,
            **kwargs,
        )

    async def account_detail_txt_tiktok(
        self,
    ):
        await self._read_from_txt(
            tiktok=True,
            type_="user",
            error=_("从文本文档提取账号 sec_user_id 失败"),
            callback=self.__account_detail_handle,
        )

    async def __account_detail_handle(
        self,
        links: list[str],
        tiktok=False,
        *args,
        **kwargs,
    ):
        count = SimpleNamespace(time=time(), success=0, failed=0)
        for index, sec in enumerate(links, start=1):
            if not await self.deal_account_detail(
                index,
                sec_user_id=sec,
                tiktok=tiktok,
                *args,
                **kwargs,
            ):
                count.failed += 1
                continue
            count.success += 1
            if index != len(links):
                await suspend(index, self.console)
        self.__summarize_results(
            count,
            _("账号"),
        )

    async def deal_account_detail(
        self,
        index: int,
        sec_user_id: str,
        mark="",
        tab="post",
        earliest="",
        latest="",
        pages: int = None,
        api=False,
        source=False,
        cookie: str = None,
        proxy: str = None,
        tiktok=False,
        *args,
        **kwargs,
    ):
        self.logger.info(
            _("开始处理第 {index} 个账号").format(index=index)
            if index
            else _("开始处理账号")
        )
        if api:
            info = None
        elif not (
            info := await self.get_user_info_data(
                tiktok,
                cookie,
                proxy,
                sec_user_id=sec_user_id,
            )
        ):
            self.logger.info(
                _("{sec_user_id} 获取账号信息失败，请检查 Cookie 登录状态！").format(
                    sec_user_id=sec_user_id
                )
            )
            if tab in {
                "favorite",
                "collection",
            }:
                return None
            self.logger.info(
                _(
                    "如果账号发布作品均为共创作品且该账号均不是作品作者时，请配置已登录的 Cookie 后重新运行程序，其余情况请无视该提示！"
                )
            )
        acquirer = self._get_account_data_tiktok if tiktok else self._get_account_data
        account_data, earliest, latest = await acquirer(
            cookie=cookie,
            proxy=proxy,
            sec_user_id=sec_user_id,
            tab=tab,
            earliest=earliest,
            latest=latest,
            pages=pages,
            **kwargs,
        )
        if not any(account_data):
            return None
        if source:
            return self.extractor.source_date_filter(
                account_data,
                earliest,
                latest,
                tiktok,
            )
        return await self._batch_process_detail(
            account_data,
            user_id=sec_user_id,
            mark=mark,
            api=api,
            earliest=earliest,
            latest=latest,
            tiktok=tiktok,
            mode=tab,
            info=info,
        )

    async def _get_account_data(
        self,
        cookie: str = None,
        proxy: str = None,
        sec_user_id: Union[str] = ...,
        tab: str = "post",
        earliest: str = "",
        latest: str = "",
        pages: int = None,
        *args,
        **kwargs,
    ):
        return await Account(
            self.parameter,
            cookie,
            proxy,
            sec_user_id,
            tab,
            earliest,
            latest,
            pages,
            **kwargs,
        ).run()

    async def _get_account_data_tiktok(
        self,
        cookie: str = None,
        proxy: str = None,
        sec_user_id: Union[str] = ...,
        tab: str = "post",
        earliest: str = "",
        latest: str = "",
        pages: int = None,
        *args,
        **kwargs,
    ):
        return await AccountTikTok(
            self.parameter,
            cookie,
            proxy,
            sec_user_id,
            tab,
            earliest,
            latest,
            pages,
            **kwargs,
        ).run()

    async def get_user_info_data(
        self,
        tiktok=False,
        cookie: str = None,
        proxy: str = None,
        unique_id: Union[str] = "",
        sec_user_id: Union[str] = "",
    ):
        return (
            await self._get_info_data_tiktok(
                cookie,
                proxy,
                unique_id,
                sec_user_id,
            )
            if tiktok
            else await self._get_info_data(
                cookie,
                proxy,
                sec_user_id,
            )
        )

    async def _get_info_data(
        self,
        cookie: str = None,
        proxy: str = None,
        sec_user_id: Union[str, list[str]] = ...,
    ):
        return await Info(
            self.parameter,
            cookie,
            proxy,
            sec_user_id,
        ).run()

    async def _get_info_data_tiktok(
        self,
        cookie: str = None,
        proxy: str = None,
        unique_id: Union[str] = "",
        sec_user_id: Union[str] = "",
    ):
        return await InfoTikTok(
            self.parameter,
            cookie,
            proxy,
            unique_id,
            sec_user_id,
        ).run()

    async def _batch_process_detail(
        self,
        data: list[dict],
        api: bool = False,
        earliest: date = None,
        latest: date = None,
        tiktok: bool = False,
        info: dict = None,
        mode: str = "",
        mark: str = "",
        user_id: str = "",
        mix_id: str = "",
        mix_title: str = "",
        collect_id: str = "",
        collect_name: str = "",
    ):
        self.logger.info(_("开始提取作品数据"))
        id_, name, mark = self.extractor.preprocessing_data(
            info or data,
            tiktok,
            mode,
            mark,
            user_id,
            mix_id,
            mix_title,
            collect_id,
            collect_name,
        )
        if not api and not all((id_, name, mark)):
            self.logger.error(_("提取账号或合集信息发生错误！"))
            return False
        self.__display_extracted_information(
            id_,
            name,
            mark,
        )
        prefix = self._generate_prefix(mode)
        suffix = self._generate_suffix(mode)
        old_mark = (
            f"{m['MARK']}_{suffix}" if (m := await self.cache.has_cache(id_)) else None
        )
        root, params, logger = self.record.run(
            self.parameter,
            blank=api,
        )
        async with logger(
            root,
            name=f"{prefix}{id_}_{mark}_{suffix}",
            old=old_mark,
            console=self.console,
            **params,
        ) as recorder:
            data = await self.extractor.run(
                data,
                recorder,
                type_="batch",
                tiktok=tiktok,
                name=name,
                mark=mark,
                earliest=earliest or date(2016, 9, 20),
                latest=latest or date.today(),
                same=mode
                in {
                    "post",
                    "mix",
                },
            )
        if api:
            return data
        await self.cache.update_cache(
            self.parameter.folder_mode,
            prefix,
            suffix,
            id_,
            name,
            mark,
        )
        await self.download_detail_batch(
            data,
            tiktok=tiktok,
            mode=mode,
            mark=mark,
            user_id=id_,
            user_name=name,
            mix_id=mix_id,
            mix_title=mix_title,
            collect_id=collect_id,
            collect_name=collect_name,
        )
        return True

    @staticmethod
    def _generate_prefix(
        mode: str,
    ):
        match mode:
            case "post" | "favorite" | "collection":
                return "UID"
            case "mix":
                return "MID"
            case "collects":
                return "CID"
            case _:
                raise DownloaderError

    @staticmethod
    def _generate_suffix(
        mode: str,
    ):
        match mode:
            case "post":
                return _("发布作品")
            case "favorite":
                return _("喜欢作品")
            case "collection":
                return _("收藏作品")
            case "mix":
                return _("合集作品")
            case "collects":
                return _("收藏夹作品")
            case _:
                raise DownloaderError

    def __display_extracted_information(
        self,
        id_: str,
        name: str,
        mark: str,
    ) -> None:
        self.logger.info(
            _("昵称/标题：{name}；标识：{mark}；ID：{id}").format(
                name=name,
                mark=mark,
                id=id_,
            ),
        )

    async def download_detail_batch(
        self,
        data: list[dict],
        type_: str = "batch",
        tiktok: bool = False,
        mode: str = "",
        mark: str = "",
        user_id: str = "",
        user_name: str = "",
        mix_id: str = "",
        mix_title: str = "",
        collect_id: str = "",
        collect_name: str = "",
    ):
        await self.downloader.run(
            data,
            type_,
            tiktok,
            mode=mode,
            mark=mark,
            user_id=user_id,
            user_name=user_name,
            mix_id=mix_id,
            mix_title=mix_title,
            collect_id=collect_id,
            collect_name=collect_name,
        )

    async def detail_interactive(
        self,
        select="",
    ):
        await self.__secondary_menu(
            _("请选择作品链接来源"),
            self.__function_detail,
            select or safe_pop(self.run_command),
        )
        self.logger.info(_("已退出批量下载链接作品(抖音)模式"))

    async def detail_interactive_tiktok(
        self,
        select="",
    ):
        await self.__detail_secondary_menu(
            self.__function_detail_tiktok,
            select or safe_pop(self.run_command),
        )
        self.logger.info(_("已退出批量下载链接作品(TikTok)模式"))

    async def detail_interactive_tiktok_unofficial(
        self,
        select="",
    ):
        self.console.warning(
            _("注意：本功能为实验性功能，依赖第三方 API 服务，可能不稳定或存在限制！")
        )
        await self.__detail_secondary_menu(
            self.__function_detail_tiktok_unofficial,
            select or safe_pop(self.run_command),
        )
        self.logger.info(_("已退出批量下载视频原画(TikTok)模式"))

    async def __detail_secondary_menu(self, menu, select="", *args, **kwargs):
        root, params, logger = self.record.run(self.parameter)
        async with logger(root, console=self.console, **params) as record:
            if not select:
                select = choose(
                    _("请选择作品链接来源"),
                    [i[0] for i in menu],
                    self.console,
                )
            if select.upper() == "Q":
                self.running = False
            try:
                n = int(select) - 1
            except ValueError:
                return
            if n in range(len(menu)):
                await menu[n][1](record)

    async def __detail_inquire(
        self,
        tiktok=False,
    ):
        root, params, logger = self.record.run(self.parameter)
        link_obj = self.links_tiktok if tiktok else self.links
        async with logger(root, console=self.console, **params) as record:
            while url := self._inquire_input(_("作品")):
                ids = await link_obj.run(url)
                if not any(ids):
                    self.logger.warning(_("{url} 提取作品 ID 失败").format(url=url))
                    continue
                self.console.print(
                    _("共提取到 {count} 个作品，开始处理！").format(count=len(ids))
                )
                await self._handle_detail(
                    ids,
                    tiktok,
                    record,
                )

    async def __detail_inquire_tiktok(
        self,
        tiktok=True,
    ):
        await self.__detail_inquire(
            tiktok,
        )

    async def __detail_inquire_tiktok_unofficial(
        self,
        *args,
        **kwargs,
    ):
        while url := self._inquire_input(_("作品")):
            ids = await self.links_tiktok.run(url)
            if not any(ids):
                self.logger.warning(_("{url} 提取作品 ID 失败").format(url=url))
                continue
            self.console.print(
                _("共提取到 {count} 个作品，开始处理！").format(count=len(ids))
            )
            await self.handle_detail_unofficial(ids)

    async def __detail_txt(
        self,
        tiktok=False,
    ):
        root, params, logger = self.record.run(self.parameter)
        async with logger(root, console=self.console, **params) as record:
            await self._read_from_txt(
                tiktok,
                "detail",
                _("从文本文档提取作品 ID 失败"),
                self._handle_detail,
                record=record,
            )

    async def __detail_txt_tiktok(
        self,
        tiktok=True,
    ):
        await self.__detail_txt(
            tiktok=tiktok,
        )

    async def __detail_txt_tiktok_unofficial(
        self,
        *args,
        **kwargs,
    ):
        await self._read_from_txt(
            True,
            "detail",
            _("从文本文档提取作品 ID 失败"),
            self.handle_detail_unofficial,
        )

    async def __read_detail_txt(self):
        if not (url := self.txt_inquire()):
            return
        ids = await self.links.run(url)
        if not any(ids):
            self.logger.warning(_("从文本文档提取作品 ID 失败"))
            return
        self.console.print(
            _("共提取到 {count} 个作品，开始处理！").format(count=len(ids))
        )
        return ids

    async def _handle_detail(
        self,
        ids: list[str],
        tiktok: bool,
        record,
        api=False,
        source=False,
        cookie: str = None,
        proxy: str = None,
    ):
        processor = DetailTikTok if tiktok else Detail
        return await self.__handle_detail(
            tiktok,
            processor,
            ids,
            record,
            api=api,
            source=source,
            cookie=cookie,
            proxy=proxy,
        )

    async def handle_detail_single(
        self,
        processor: Callable,
        cookie: str,
        proxy: str,
        detail_id: str,
    ):
        return await processor(
            self.parameter,
            cookie,
            proxy,
            detail_id,
        ).run()

    async def __handle_detail(
        self,
        tiktok: bool,
        processor: Callable,
        ids: list[str],
        record,
        api=False,
        source=False,
        cookie: str = None,
        proxy: str = None,
    ):
        detail_data = [
            await self.handle_detail_single(
                processor,
                cookie,
                proxy,
                i,
            )
            for i in ids
        ]
        if not any(detail_data):
            return None
        if source:
            return detail_data
        detail_data = await self.extractor.run(
            detail_data,
            record,
            tiktok=tiktok,
        )
        if api:
            return detail_data
        await self.downloader.run(detail_data, "detail", tiktok=tiktok)
        return self._get_preview_image(detail_data[0])

    @staticmethod
    def _get_preview_image(data: dict) -> str:
        if data["type"] == _("图集"):
            return data["downloads"][0]
        elif data["type"] == _("视频"):
            return data["static_cover"]
        return ""

    def _choice_live_quality(
        self,
        flv_items: dict,
        m3u8_items: dict,
    ) -> tuple | None:
        if not self.ffmpeg:
            self.logger.warning(_("程序未检测到有效的 ffmpeg，不支持直播下载功能！"))
            return None
        try:
            choice_ = self.parameter.live_qualities or self.console.input(
                _("请选择下载清晰度(输入清晰度或者对应序号，直接回车代表不下载): "),
            )
            if u := flv_items.get(choice_):
                return u, m3u8_items.get(choice_)
            if not 0 <= (i := int(choice_) - 1) < len(flv_items):
                raise ValueError
        except ValueError:
            self.logger.info(_("未输入有效的清晰度或者序号，跳过下载！"))
            return None
        return list(flv_items.values())[i], list(m3u8_items.values())[i]

    async def get_live_data(
        self,
        web_rid: str = None,
        room_id: str = None,
        sec_user_id: str = None,
        cookie: str = None,
        proxy: str = None,
    ):
        return await Live(
            self.parameter,
            cookie,
            proxy,
            web_rid,
            room_id,
            sec_user_id,
        ).run()

    async def get_live_data_tiktok(
        self,
        room_id: str = None,
        cookie: str = None,
        proxy: str = None,
    ):
        return await LiveTikTok(self.parameter, cookie, proxy, room_id).run()

    async def live_interactive(
        self,
        *args,
    ):
        while url := self._inquire_input(_("直播")):
            ids = await self.links.run(url, type_="live")
            live_data = [await self.get_live_data(i) for i in ids]
            live_data = await self.extractor.run(live_data, None, "live")
            if not [i for i in live_data if i]:
                self.logger.warning(_("获取直播数据失败"))
                continue
            download_tasks = self.show_live_info(live_data)
            await self.downloader.run(download_tasks, type_="live")
        self.logger.info(_("已退出获取直播拉流地址(抖音)模式"))

    async def live_interactive_tiktok(
        self,
        *args,
    ):
        while url := self._inquire_input(_("直播")):
            ids = await self.links_tiktok.run(url, type_="live")
            if not ids:
                self.logger.warning(_("{} 提取直播 ID 失败").format(url=url))
                continue
            live_data = [await self.get_live_data_tiktok(i) for i in ids]
            if not [i for i in live_data if i]:
                self.logger.warning(_("获取直播数据失败"))
                continue
            live_data = await self.extractor.run(
                live_data,
                None,
                "live",
                tiktok=True,
            )
            download_tasks = self.show_live_info_tiktok(live_data)
            await self.downloader.run(download_tasks, type_="live", tiktok=True)
        self.logger.info(_("已退出获取直播拉流地址(TikTok)模式"))

    # def _generate_live_params(self, rid: bool, ids: list[list]) -> list[dict]:
    #     if not ids:
    #         self.console.warning(
    #             _("提取 web_rid 或者 room_id 失败！"),
    #         )
    #         return []
    #     if rid:
    #         return [{"web_rid": id_} for id_ in ids]
    #     else:
    #         return [{"room_id": id_[0], "sec_user_id": id_[1]} for id_ in ids]

    def show_live_info(self, data: list[dict]) -> list[tuple]:
        download_tasks = []
        for item in data:
            self.console.print(_("直播标题:"), item["title"])
            self.console.print(_("主播昵称:"), item["nickname"])
            self.console.print(_("在线观众:"), item["user_count_str"])
            self.console.print(_("观看次数:"), item["total_user_str"])
            if item["status"] == 4:
                self.console.print(_("当前直播已结束！"))
                continue
            self.show_live_stream_url(item, download_tasks)
        return [i for i in download_tasks if isinstance(i, tuple)]

    def show_live_info_tiktok(self, data: list[dict]) -> list[tuple]:
        download_tasks = []
        for item in data:
            if item["message"]:
                self.console.print(item["message"])
                self.console.print(item["prompts"])
                continue
            self.console.print(_("直播标题:"), item["title"])
            self.console.print(_("主播昵称:"), item["nickname"])
            self.console.print(_("开播时间:"), item["create_time"])
            self.console.print(_("在线观众:"), item["user_count"])
            self.console.print(_("点赞次数:"), item["like_count"])
            self.show_live_stream_url_tiktok(item, download_tasks)
        return [i for i in download_tasks if isinstance(i, tuple)]

    def show_live_stream_url(self, item: dict, tasks: list):
        self.console.print(_("FLV 拉流地址: "))
        for i, (k, v) in enumerate(item["flv_pull_url"].items(), start=1):
            self.console.print(i, k, v)
        self.console.print(_("M3U8 拉流地址: "))
        for i, (k, v) in enumerate(item["hls_pull_url_map"].items(), start=1):
            self.console.print(i, k, v)
        if self.parameter.download:
            tasks.append(
                (item, *u)
                if (
                    u := self._choice_live_quality(
                        item["flv_pull_url"],
                        item["hls_pull_url_map"],
                    )
                )
                else u
            )

    def show_live_stream_url_tiktok(self, item: dict, tasks: list):
        self.console.print(_("FLV 拉流地址: "))
        for i, (k, v) in enumerate(item["flv_pull_url"].items(), start=1):
            self.console.print(i, k, v)
        if self.parameter.download:
            tasks.append(
                (
                    item,
                    *u,
                )
                # TikTok 平台 暂无 m3u8 地址
                if (
                    u := self._choice_live_quality(
                        item["flv_pull_url"],
                        item["flv_pull_url"],
                    )
                )
                else u
            )

    @check_storage_format
    async def comment_interactive_tiktok(self, select="", *args, **kwargs):
        ...
        self.logger.info(_("已退出采集作品评论数据(TikTok)模式"))

    @check_storage_format
    async def comment_interactive(
        self,
        select="",
    ):
        await self.__secondary_menu(
            _("请选择作品链接来源"),
            self.__function_comment,
            select or safe_pop(self.run_command),
        )
        self.logger.info(_("已退出采集作品评论数据(抖音)模式)"))

    async def __comment_inquire(
        self,
        tiktok=False,
    ):
        link = self.links_tiktok if tiktok else self.links
        while url := self._inquire_input(_("作品")):
            ids = await link.run(
                url,
            )
            if not any(ids):
                self.logger.warning(_("{url} 提取作品 ID 失败").format(url=url))
                continue
            self.console.print(
                _("共提取到 {count} 个作品，开始处理！").format(count=len(ids))
            )
            await self.comment_handle(
                ids,
                tiktok=tiktok,
            )

    async def __comment_inquire_tiktok(
        self,
    ):
        await self.__comment_inquire(
            True,
        )

    async def __comment_txt(
        self,
        tiktok=False,
    ):
        await self._read_from_txt(
            tiktok,
            "detail",
            _("从文本文档提取作品 ID 失败"),
            self.comment_handle,
        )

    async def comment_handle_single(
        self,
        detail_id: str,
        cookie: str = None,
        proxy: str = None,
        source: bool = False,
        **kwargs,
    ) -> list:
        if data := await Comment(
            self.parameter,
            cookie,
            proxy,
            detail_id=detail_id,
            **kwargs,
        ).run():
            return data if source else await self.save_comment(detail_id, data)
        return []

    async def comment_handle_single_tiktok(
        self,
        detail_id: str,
        cookie: str = None,
        proxy: str = None,
        source: bool = False,
        **kwargs,
    ) -> list: ...

    async def comment_handle(
        self,
        ids: list,
        tiktok=False,
        cookie: str = None,
        proxy: str = None,
        **kwargs,
    ):
        if tiktok:
            processor = self.comment_handle_single_tiktok
        else:
            processor = self.comment_handle_single
        for i in ids:
            if await processor(
                i,
                cookie,
                proxy,
                **kwargs,
            ):
                self.logger.info(
                    _("作品评论数据已储存至 {filename}").format(
                        filename=_("作品{id}_评论数据").format(id=i),
                    )
                )
            else:
                self.logger.warning(_("采集评论数据失败"))

    async def save_comment(self, detail_id: str, data: list[dict]) -> list:
        root, params, logger = self.record.run(self.parameter, type_="comment")
        async with logger(
            root,
            name=_("作品{id}_评论数据").format(
                id=detail_id,
            ),
            console=self.console,
            **params,
        ) as record:
            return await self.extractor.run(data, record, type_="comment")

    async def reply_handle(
        self,
        detail_id: str,
        comment_id: str,
        pages: int = None,
        cursor=0,
        count=3,
        cookie: str = None,
        proxy: str = None,
        source=False,
    ):
        if data := await Reply(
            self.parameter,
            cookie,
            proxy,
            detail_id=detail_id,
            comment_id=comment_id,
            pages=pages,
            cursor=cursor,
            count=count,
        ).run():
            return data if source else await self.save_comment(detail_id, data)
        return []

    async def reply_handle_tiktok(
        self,
        detail_id: str,
        comment_id: str,
        pages: int = None,
        cursor=0,
        count=3,
        cookie: str = None,
        proxy: str = None,
        source=False,
    ): ...

    async def mix_interactive(
        self,
        select="",
    ):
        await self.__secondary_menu(
            _("请选择合集链接来源"),
            self.__function_mix,
            select or safe_pop(self.run_command),
        )
        self.logger.info(_("已退出批量下载合集作品(抖音)模式"))

    async def mix_interactive_tiktok(
        self,
        select="",
    ):
        await self.__secondary_menu(
            _("请选择合集链接来源"),
            self.__function_mix_tiktok,
            select or safe_pop(self.run_command),
        )
        self.logger.info(_("已退出批量下载合集作品(TikTok)模式"))

    @staticmethod
    def _generate_mix_params(mix: bool, id_: str) -> dict:
        return (
            {
                "mix_id": id_,
            }
            if mix
            else {
                "detail_id": id_,
            }
        )

    async def mix_inquire(
        self,
    ):
        while url := self._inquire_input(_("合集或作品")):
            mix_id, ids = await self.links.run(url, type_="mix")
            if not ids:
                self.logger.warning(
                    _("{url} 获取作品 ID 或合集 ID 失败").format(url=url)
                )
                continue
            await self.__mix_handle(
                mix_id,
                ids,
            )

    async def mix_inquire_tiktok(
        self,
    ):
        while url := self._inquire_input(_("合集或作品")):
            __, ids, title = await self.links_tiktok.run(url, type_="mix")
            if not ids:
                self.logger.warning(_("{url} 获取合集 ID 失败").format(url=url))
                continue
            await self.__mix_handle(
                True,
                ids,
                title,
                True,
            )

    @check_cookie_state(tiktok=False)
    async def mix_collection(
        self,
    ):
        if id_ := await self.mix_inquire_collection():
            await self.__mix_handle(
                True,
                id_,
            )

    async def mix_inquire_collection(self) -> list[str]:
        data = await CollectsMix(self.parameter).run()
        if not any(data):
            return []
        data = self.extractor.extract_mix_collect_info(data)
        return self.input_download_index(data)

    def input_download_index(self, data: list[dict]) -> list[str] | None:
        if d := self.__input_download_index(
            data,
            _("收藏合集"),
        ):
            return [i["id"] for i in d]

    def __input_download_index(
        self,
        data: list[dict],
        text=_("收藏合集"),
        select="",
        key="title",
    ) -> list[dict] | None:
        self.console.print(_("{text}列表：").format(text=_(text)))
        for i, j in enumerate(data, start=1):
            self.console.print(f"{i}. {j[key]}")
        index = select or self.console.input(
            _(
                "请输入需要下载的{item}序号(多个序号使用空格分隔，输入 ALL 下载全部{item})："
            ).format(item=text)
        )
        try:
            if not index:
                pass
            elif index.upper() == "ALL":
                return data
            elif index.upper() == "Q":
                self.running = False
            else:
                index = {int(i) for i in index.split()}
                return [j for i, j in enumerate(data, start=1) if i in index]
        except ValueError:
            self.console.warning(_("{text}序号输入错误！").format(text=text))

    async def mix_txt(
        self,
    ):
        await self._read_from_txt(
            tiktok=False,
            type_="mix",
            error=_("从文本文档提取作品 ID 或合集 ID 失败"),
            callback=self.__mix_handle,
        )

    async def mix_txt_tiktok(
        self,
    ):
        await self._read_from_txt(
            tiktok=True,
            type_="mix",
            error=_("从文本文档提取合集 ID 失败"),
            callback=self.__mix_handle,
        )

        if not (url := self.txt_inquire()):
            return
        __, ids, title = await self.links_tiktok.run(url, type_="mix")
        if not ids:
            self.logger.warning()
            return
        await self.__mix_handle(
            True,
            ids,
            title,
            True,
        )

    async def __mix_handle(
        self,
        mix_id: bool,
        ids: list[str],
        mix_title_map: list[str] = None,
        tiktok=False,
    ):
        count = SimpleNamespace(time=time(), success=0, failed=0)
        for index, i in enumerate(ids, start=1):
            if not await self.deal_mix_detail(
                mix_id,
                i,
                index=index,
                tiktok=tiktok,
                mix_title=mix_title_map[index - 1] if mix_title_map else None,
            ):
                count.failed += 1
                continue
            count.success += 1
            if index != len(ids):
                await suspend(index, self.console)
        self.__summarize_results(
            count,
            _("合集"),
        )

    async def mix_batch(
        self,
    ):
        await self.__mix_batch(
            self.mix,
            "mix_urls",
            False,
        )

    async def mix_batch_tiktok(
        self,
    ):
        await self.__mix_batch(
            self.mix_tiktok,
            "mix_urls_tiktok",
            True,
        )

    async def __mix_batch(
        self,
        mix: list[SimpleNamespace],
        params_name: str,
        tiktok: bool,
    ):
        count = SimpleNamespace(time=time(), success=0, failed=0)
        for index, data in enumerate(mix, start=1):
            mix_id, id_, title = await self._check_mix_id(
                data.url,
                tiktok,
            )
            if not id_:
                self.logger.warning(
                    _(
                        "配置文件 {name} 参数的 url {url} 获取作品 ID 或合集 ID 失败，错误配置：{data}"
                    ).format(
                        name=params_name,
                        url=data.url,
                        data=vars(data),
                    )
                )
                count.failed += 1
                continue
            if not await self.deal_mix_detail(
                mix_id,
                id_,
                data.mark,
                index,
                tiktok=tiktok,
                mix_title=title,
            ):
                count.failed += 1
                continue
            count.success += 1
            if index != len(mix):
                await suspend(index, self.console)
        self.__summarize_results(
            count,
            _("合集"),
        )

    async def deal_mix_detail(
        self,
        mix_id: bool = None,
        id_: str = None,
        mark="",
        index: int = 0,
        api=False,
        source=False,
        cookie: str = None,
        proxy: str = None,
        tiktok=False,
        mix_title: str = "",
        **kwargs,
    ):
        self.logger.info(
            _("开始处理第 {index} 个合集").format(index=index)
            if index
            else _("开始处理合集")
        )
        mix_params = self._generate_mix_params(mix_id, id_)
        if tiktok:
            mix_obj = MixTikTok(
                self.parameter,
                cookie,
                proxy,
                mix_title=mix_title,
                **mix_params,
                **kwargs,
            )
        else:
            mix_obj = Mix(
                self.parameter,
                cookie,
                proxy,
                **mix_params,
                **kwargs,
            )
        if any(mix_data := await mix_obj.run()):
            return (
                mix_data
                if source
                else await self._batch_process_detail(
                    mix_data,
                    mode="mix",
                    mix_id=mix_obj.mix_id,
                    mix_title=mix_obj.mix_title,
                    mark=mark,
                    api=api,
                    tiktok=tiktok,
                )
            )
        self.logger.warning(_("采集合集作品数据失败"))

    async def _check_mix_id(
        self,
        url: str,
        tiktok: bool,
    ) -> tuple[bool, str, str]:
        match tiktok:
            case True:
                _, ids, title = await self.links_tiktok.run(url, type_="mix")
                return (True, ids[0], title[0]) if len(ids) > 0 else (None, "", "")
            case False:
                mix_id, ids = await self.links.run(url, type_="mix")
                return (mix_id, ids[0], "") if len(ids) > 0 else (mix_id, "", "")
            case _:
                raise DownloaderError

    async def user_batch(
        self,
        *args,
        **kwargs,
    ):
        users = []
        for index, data in enumerate(self.accounts, start=1):
            if not (sec_user_id := await self.check_sec_user_id(data.url)):
                self.logger.warning(
                    _("配置文件 accounts_urls 参数第 {index} 条数据的 url 无效").format(
                        index=index
                    ),
                )
                continue
            users.append(await self._get_user_data(sec_user_id))
        await self._deal_user_data([i for i in users if i])

    async def user_inquire(
        self,
        *args,
        **kwargs,
    ):
        while url := self._inquire_input(_("账号主页")):
            sec_user_ids = await self.links.run(url, type_="user")
            if not sec_user_ids:
                self.logger.warning(
                    _("{url} 提取账号 sec_user_id 失败").format(url=url)
                )
                continue
            users = [await self._get_user_data(i) for i in sec_user_ids]
            await self._deal_user_data([i for i in users if i])

    def txt_inquire(self) -> str:
        if path := self.console.input(_("请输入文本文档路径：")):
            if (t := Path(path.replace('"', ""))).is_file():
                try:
                    with t.open("r", encoding=self.ENCODE) as f:
                        return f.read()
                except UnicodeEncodeError as e:
                    self.logger.warning(
                        _("{path} 文件读取异常: {error}").format(path=path, error=e)
                    )
            else:
                self.console.print(_("{path} 文件不存在！").format(path=path))
        return ""

    async def user_txt(
        self,
        *args,
        **kwargs,
    ):
        if not (url := self.txt_inquire()):
            return
        sec_user_ids = await self.links.run(url, type_="user")
        if not sec_user_ids:
            self.logger.warning(_("从文本文档提取账号 sec_user_id 失败"))
            return
        users = [await self._get_user_data(i) for i in sec_user_ids]
        await self._deal_user_data([i for i in users if i])

    async def _get_user_data(
        self,
        sec_user_id: str,
        cookie: str = None,
        proxy: str = None,
    ):
        self.logger.info(
            _("正在获取账号 {sec_user_id} 的数据").format(sec_user_id=sec_user_id)
        )
        data = await User(
            self.parameter,
            cookie,
            proxy,
            sec_user_id,
        ).run()
        return data or {}

    async def _deal_user_data(
        self,
        data: list[dict],
        source=False,
    ):
        if not any(data):
            return None
        if source:
            return data
        root, params, logger = self.record.run(
            self.parameter,
            type_="user",
        )
        async with logger(
            root, name="UserData", console=self.console, **params
        ) as recorder:
            data = await self.extractor.run(data, recorder, type_="user")
        self.logger.info(_("账号数据已保存至文件"))
        return data

    @check_storage_format
    async def user_interactive(self, select="", *args, **kwargs):
        await self.__secondary_menu(
            _("请选择账号链接来源"),
            function=self.__function_user,
            select=select or safe_pop(self.run_command),
        )
        self.logger.info(_("已退出采集账号详细数据模式"))

    def _enter_search_criteria(
        self,
        field: str,
    ) -> list[Any]:
        criteria = self.console.input(
            _("请输入搜索参数；参数之间使用两个空格分隔({field})：\n").format(
                field=field
            ),
        )
        if criteria.upper() == "Q":
            self.running = False
            return []
        return criteria.split("  ") if criteria else []

    @staticmethod
    def fill_search_criteria(criteria: list[Any]) -> list[Any]:
        if len(criteria) == 1:
            criteria.append(1)
        while len(criteria) < 9:
            criteria.append(0)
        return criteria

    @check_storage_format
    async def search_interactive(
        self,
        select="",
    ):
        await self.__secondary_menu(
            _("请选择搜索模式"),
            function=self.__function_search,
            select=select or safe_pop(self.run_command),
        )
        self.logger.info("已退出采集搜索结果数据模式")

    @staticmethod
    def generate_model(
        channel: int,
        keyword: str,
        pages: int = 1,
        sort_type: int = 0,
        publish_time: int = 0,
        duration: int = 0,
        search_range: int = 0,
        content_type: int = 0,
        douyin_user_fans: int = 0,
        douyin_user_type: int = 0,
    ) -> Union["BaseModel", str]:
        try:
            match channel:
                case 0:
                    return GeneralSearch(
                        keyword=keyword,
                        pages=pages,
                        sort_type=sort_type,
                        publish_time=publish_time,
                        duration=duration,
                        search_range=search_range,
                        content_type=content_type,
                    )
                case 1:
                    return VideoSearch(
                        keyword=keyword,
                        pages=pages,
                        sort_type=sort_type,
                        publish_time=publish_time,
                        duration=duration,
                        search_range=search_range,
                    )
                case 2:
                    return UserSearch(
                        keyword=keyword,
                        pages=pages,
                        douyin_user_fans=douyin_user_fans,
                        douyin_user_type=douyin_user_type,
                    )
                case 3:
                    return LiveSearch(
                        keyword=keyword,
                        pages=pages,
                    )
                case _:
                    raise DownloaderError
        except ValidationError as e:
            return repr(e)

    async def _search_interactive_general(
        self,
        index=0,
    ):
        while criteria := self._enter_search_criteria(Search.search_criteria[index]):
            criteria = self.fill_search_criteria(criteria)
            if isinstance(
                model := self.generate_model(
                    index,
                    *criteria,
                ),
                str,
            ):
                self.logger.warning(model)
                continue
            self.logger.info(f"搜索参数: {model.model_dump()}", False)
            if isinstance(
                r := await self.deal_search_data(
                    model,
                ),
                list,
            ) and not any(r):
                self.logger.warning(_("搜索结果为空"))

    async def _search_interactive_video(self):
        await self._search_interactive_general(
            1,
        )

    async def _search_interactive_user(self):
        await self._search_interactive_general(
            2,
        )

    async def _search_interactive_live(self):
        await self._search_interactive_general(
            3,
        )

    @staticmethod
    def _generate_search_name(
        model: "BaseModel",
    ) -> str:
        name = [
            _("搜索数据"),
            f"{datetime.now():%Y_%m_%d_%H_%M_%S}",
            Search.search_params[model.channel].note,
        ]
        match model.channel:
            case 0:
                name.extend(
                    [
                        model.keyword,
                        Search.sort_type_help[model.sort_type],
                        Search.publish_time_help[model.publish_time],
                        Search.duration_help[model.duration],
                        Search.search_range_help[model.search_range],
                        Search.content_type_help[model.content_type],
                    ]
                )
            case 1:
                name.extend(
                    [
                        model.keyword,
                        Search.sort_type_help[model.sort_type],
                        Search.publish_time_help[model.publish_time],
                        Search.duration_help[model.duration],
                        Search.search_range_help[model.search_range],
                    ]
                )
            case 2:
                name.extend(
                    [
                        model.keyword,
                        Search.douyin_user_fans_help[model.douyin_user_fans],
                        Search.douyin_user_type_help[model.douyin_user_type],
                    ]
                )
            case 3:
                name.append(
                    model.keyword,
                )
        return "_".join(name)

    async def deal_search_data(
        self,
        model: "BaseModel",
        source=False,
    ):
        data = await Search(
            self.parameter,
            **model.model_dump(),
        ).run()
        if len(data) != 1 and not any(data):
            return None
        if source or not any(data):
            return data
        root, params, logger = self.record.run(
            self.parameter,
            type_=Search.search_data_field[model.channel],
        )
        name = self._generate_search_name(
            model,
        )
        async with logger(root, name=name, console=self.console, **params) as logger:
            search_data = await self.extractor.run(
                data,
                logger,
                type_="search",
                tab=model.channel,
            )
            self.logger.info(_("搜索数据已保存至 {name}").format(name=name))
        return search_data

    @check_storage_format
    async def hot_interactive(
        self,
        *args,
    ):
        await self._deal_hot_data()
        self.logger.info(_("已退出采集抖音热榜数据(抖音)模式"))

    async def _deal_hot_data(
        self,
        source=False,
        cookie: str = None,
        proxy: str = None,
    ):
        time_, board = await Hot(
            self.parameter,
            cookie,
            proxy,
        ).run()
        if not any(board):
            return None, None
        if source:
            return time_, [{Hot.board_params[i].name: j} for i, j in board]
        root, params, logger = self.record.run(self.parameter, type_="hot")
        data = []
        for i, j in board:
            name = _("热榜数据_{time}_{name}").format(
                time=time_, name=Hot.board_params[i].name
            )
            async with logger(
                root, name=name, console=self.console, **params
            ) as record:
                data.append(
                    {
                        Hot.board_params[i].name: await self.extractor.run(
                            j, record, type_="hot"
                        )
                    }
                )
        self.logger.info(
            _("热榜数据已储存至: 热榜数据_{time} + 榜单类型").format(time=time_)
        )
        return time_, data

    @check_cookie_state(tiktok=False)
    async def collection_interactive(
        self,
        *args,
    ):
        if sec_user_id := await self.__check_owner_url():
            start = time()
            await self._deal_collection_data(
                sec_user_id,
            )
            self._time_statistics(start)
        self.logger.info(_("已退出批量下载收藏作品(抖音)模式"))

    @check_cookie_state(tiktok=False)
    async def collects_interactive(
        self,
        select="",
        key: str = "name",
    ):
        if c := await self.__get_collects_list(
            select=select,
            key=key,
        ):
            start = time()
            for i in c:
                await self._deal_collects_data(
                    i[key],
                    i["id"],
                )
            self._time_statistics(start)
        else:
            self.logger.info(_("已退出批量下载收藏夹作品(抖音)模式"))

    async def __get_collects_list(
        self,
        cookie: str = None,
        proxy: str | dict = None,
        # api=False,
        source=False,
        select="",
        key: str = "name",
        *args,
        **kwargs,
    ):
        collects = await Collects(
            self.parameter,
            cookie,
            proxy,
        ).run()
        if not any(collects):
            return None
        if source:
            return collects
        data = self.extractor.extract_collects_info(collects)
        return self.__input_download_index(
            data,
            _("收藏夹"),
            select,
            key,
        )

    async def __check_owner_url(
        self,
        tiktok=False,
    ):
        if not (sec_user_id := await self.check_sec_user_id(self.owner.url)):
            self.logger.warning(
                _("配置文件 owner_url 的 url 参数 {url} 无效").format(
                    url=self.owner.url
                ),
            )
            # if self.console.input(
            #         _("程序无法获取账号信息，建议修改配置文件后重新运行，是否返回上一级菜单(YES/NO)")
            # ).upper != "NO":
            #     return None
            return ""
        return sec_user_id

    @check_cookie_state(tiktok=False)
    async def collection_music_interactive(
        self,
        *args,
    ):
        start = time()
        if data := await self.__handle_collection_music(
            *args,
        ):
            data = await self.extractor.run(
                data,
                None,
                "music",
            )
            await self.downloader.run(
                data,
                type_="music",
            )
        self._time_statistics(start)
        self.logger.info(_("已退出批量下载收藏音乐(抖音)模式"))

    def _time_statistics(
        self,
        start: float,
    ):
        time_ = time() - start
        self.logger.info(
            _("程序运行耗时 {minutes} 分钟 {seconds} 秒").format(
                minutes=int(time_ // 60), seconds=int(time_ % 60)
            )
        )

    async def __handle_collection_music(
        self,
        cookie: str = None,
        proxy: str = None,
        *args,
        **kwargs,
    ):
        data = await CollectsMusic(
            self.parameter,
            cookie,
            proxy,
            *args,
            **kwargs,
        ).run()
        return data if any(data) else None

    async def _deal_collection_data(
        self,
        sec_user_id: str,
        api=False,
        source=False,
        cookie: str = None,
        proxy: str = None,
        tiktok=False,
    ):
        self.logger.info(_("开始获取收藏数据"))
        if not (
            info := await self.get_user_info_data(
                tiktok,
                cookie,
                proxy,
                sec_user_id=sec_user_id,
            )
        ):
            self.logger.warning(
                _("{sec_user_id} 获取账号信息失败").format(sec_user_id=sec_user_id)
            )
            return
        collection = await Collection(
            self.parameter,
            cookie,
            proxy,
            sec_user_id,
        ).run()
        if not any(collection):
            return None
        if source:
            return collection
        await self._batch_process_detail(
            collection,
            api,
            tiktok=tiktok,
            mode="collection",
            mark=self.owner.mark,
            user_id=sec_user_id,
            info=info,
        )

    async def _deal_collects_data(
        self,
        name: str,
        id_: str,
        api=False,
        source=False,
        cookie: str = None,
        proxy: str = None,
        tiktok=False,
    ):
        self.logger.info(_("开始获取收藏夹数据"))
        data = await CollectsDetail(
            self.parameter,
            cookie,
            proxy,
            id_,
        ).run()
        if not any(data):
            return None
        if source:
            return data
        await self._batch_process_detail(
            data,
            mode="collects",
            collect_id=id_,
            collect_name=name,
            api=api,
            tiktok=tiktok,
        )

    async def hashtag_interactive(
        self,
        cookie: str = None,
        proxy: str = None,
        *args,
        **kwargs,
    ):
        await HashTag(
            self.parameter,
            cookie,
            proxy,
        ).run()

    async def handle_detail_unofficial(
        self,
        ids: list[str],
        *args,
        **kwargs,
    ):
        extractor = DetailTikTokExtractor(self.parameter)
        for i in ids:
            if data := await DetailTikTokUnofficial(
                self.parameter,
                detail_id=i,
            ).run():
                if data := extractor.run(data):
                    await self.downloader.run([data], "detail", tiktok=True)

    async def run(self, run_command: list):
        self.run_command = run_command
        while self.running:
            if not (select := safe_pop(self.run_command)):
                select = choose(
                    _("请选择采集功能"),
                    [i for i, __ in self.__function],
                    self.console,
                    (11,),
                )
            if select in {
                "Q",
                "q",
            }:
                self.running = False
            try:
                n = int(select) - 1
            except ValueError:
                break
            if n in range(len(self.__function)):
                await self.__function[n][1](safe_pop(self.run_command))
```

## File: `src/application/TikTokDownloader.py`
```python
from asyncio import CancelledError, run
from threading import Event, Thread
from time import sleep

from httpx import RequestError, get

from src.config import Parameter, Settings
from src.custom import (
    COOKIE_UPDATE_INTERVAL,
    DISCLAIMER_TEXT,
    DOCUMENTATION_URL,
    LICENCE,
    MASTER,
    PROJECT_NAME,
    PROJECT_ROOT,
    RELEASES,
    REPOSITORY,
    SERVER_HOST,
    SERVER_PORT,
    TEXT_REPLACEMENT,
    VERSION_BETA,
    VERSION_MAJOR,
    VERSION_MINOR,
)
from src.manager import Database, DownloadRecorder
from src.module import Cookie, MigrateFolder
from src.record import BaseLogger, LoggerManager
from src.tools import (
    Browser,
    ColorfulConsole,
    DownloaderError,
    RenameCompatible,
    choose,
    remove_empty_directories,
    safe_pop,
)
from src.translation import _, switch_language

from .main_monitor import ClipboardMonitor
from .main_server import APIServer
from .main_terminal import TikTok

# from typing import Type
# from webbrowser import open

__all__ = ["TikTokDownloader"]


class TikTokDownloader:
    VERSION_MAJOR = VERSION_MAJOR
    VERSION_MINOR = VERSION_MINOR
    VERSION_BETA = VERSION_BETA
    NAME = PROJECT_NAME
    WIDTH = 50
    LINE = ">" * WIDTH

    def __init__(
        self,
    ):
        self.rename_compatible()
        self.console = ColorfulConsole(
            debug=self.VERSION_BETA,
        )
        self.logger = None
        self.recorder = None
        self.settings = Settings(PROJECT_ROOT, self.console)
        self.event_cookie = Event()
        self.cookie = Cookie(self.settings, self.console)
        self.params_task = None
        self.parameter = None
        self.running = True
        self.run_command = None
        self.database = Database()
        self.config = None
        self.option = None
        self.__function_menu = None

    @staticmethod
    def rename_compatible():
        RenameCompatible.migration_file()

    async def read_config(self):
        self.config = self.__format_config(await self.database.read_config_data())
        self.option = self.__format_config(await self.database.read_option_data())
        self.set_language(self.option["Language"])

    @staticmethod
    def __format_config(config: list) -> dict:
        return {i["NAME"]: i["VALUE"] for i in config}

    @staticmethod
    def set_language(language: str) -> None:
        switch_language(language)

    async def __aenter__(self):
        await self.database.__aenter__()
        await self.read_config()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.database.__aexit__(exc_type, exc_val, exc_tb)
        if self.parameter:
            await self.parameter.close_client()
            self.close()

    def __update_menu(self):
        options = {
            1: _("禁用"),
            0: _("启用"),
        }
        self.__function_menu = (
            (_("从剪贴板读取 Cookie (抖音)"), self.write_cookie),
            (_("从浏览器读取 Cookie (抖音)"), self.browser_cookie),
            # (_("扫码登录获取 Cookie (抖音)"), self.auto_cookie),
            (_("从剪贴板读取 Cookie (TikTok)"), self.write_cookie_tiktok),
            (_("从浏览器读取 Cookie (TikTok)"), self.browser_cookie_tiktok),
            (_("终端交互模式"), self.complete),
            (_("后台监听模式"), self.monitor),
            (_("Web API 模式"), self.server),
            (_("Web UI 模式"), self.disable_function),
            # (_("Web API 模式"), self.__api_object),
            # (_("Web UI 模式"), self.__web_ui_object),
            (
                _("{}作品下载记录").format(options[self.config["Record"]]),
                self.__modify_record,
            ),
            (_("删除作品下载记录"), self.delete_works_ids),
            (
                _("{}运行日志记录").format(options[self.config["Logger"]]),
                self.__modify_logging,
            ),
            (_("检查程序版本更新"), self.check_update),
            (_("切换语言"), self._switch_language),
        )

    async def disable_function(
        self,
        *args,
        **kwargs,
    ):
        self.console.warning(
            "该功能正在重构，未来开发完成重新开放！",
        )

    async def server(self):
        try:
            self.console.print(
                _(
                    "访问 http://127.0.0.1:5555/docs 或者 http://127.0.0.1:5555/redoc 可以查阅 API 模式说明文档！"
                ),
                highlight=True,
            )
            await APIServer(
                self.parameter,
                self.database,
            ).run_server(
                SERVER_HOST,
                SERVER_PORT,
            )
        except KeyboardInterrupt:
            self.running = False

    async def __modify_record(self):
        await self.change_config("Record")

    async def __modify_logging(self):
        await self.change_config("Logger")

    async def _switch_language(
        self,
    ):
        if self.option["Language"] == "zh_CN":
            language = "en_US"
        elif self.option["Language"] == "en_US":
            language = "zh_CN"
        else:
            raise DownloaderError
        await self._update_language(language)

    async def _update_language(self, language: str) -> None:
        self.option["Language"] = language
        await self.database.update_option_data("Language", language)
        self.set_language(language)

    async def disclaimer(self):
        if not self.config["Disclaimer"]:
            await self.__init_language()
            self.console.print(_(DISCLAIMER_TEXT), style=MASTER)
            if self.console.input(
                _("是否已仔细阅读上述免责声明(YES/NO): ")
            ).upper() not in ("Y", "YES"):
                return False
            await self.database.update_config_data("Disclaimer", 1)
            self.console.print()
        return True

    async def __init_language(self):
        languages = (
            (
                "简体中文",
                "zh_CN",
            ),
            (
                "English",
                "en_US",
            ),
        )
        language = choose(
            "请选择语言(Please Select Language)",
            [i[0] for i in languages],
            self.console,
        )
        try:
            language = languages[int(language) - 1][1]
            await self._update_language(language)
        except ValueError:
            await self.__init_language()

    def project_info(self):
        self.console.print(
            f"{self.LINE}\n\n\n{self.NAME.center(self.WIDTH)}\n\n\n{self.LINE}\n",
            style=MASTER,
        )
        self.console.print(_("项目地址: {}").format(REPOSITORY), style=MASTER)
        self.console.print(_("项目文档: {}").format(DOCUMENTATION_URL), style=MASTER)
        self.console.print(_("开源许可: {}\n").format(LICENCE), style=MASTER)

    def check_config(self):
        self.recorder = DownloadRecorder(
            self.database,
            self.config["Record"],
            self.console,
        )
        self.logger = {1: LoggerManager, 0: BaseLogger}[self.config["Logger"]]

    async def check_update(self):
        try:
            response = get(
                RELEASES,
                timeout=5,
                follow_redirects=True,
            )
            latest_major, latest_minor = map(
                int, str(response.url).split("/")[-1].split(".", 1)
            )
            if latest_major > self.VERSION_MAJOR or latest_minor > self.VERSION_MINOR:
                self.console.warning(
                    _("检测到新版本: {major}.{minor}").format(
                        major=latest_major, minor=latest_minor
                    ),
                )
                self.console.print(RELEASES)
            elif latest_minor == self.VERSION_MINOR and self.VERSION_BETA:
                self.console.warning(
                    _("当前版本为开发版, 可更新至正式版"),
                )
                self.console.print(RELEASES)
            elif self.VERSION_BETA:
                self.console.warning(
                    _("当前已是最新开发版"),
                )
            else:
                self.console.info(
                    _("当前已是最新正式版"),
                )
        except RequestError:
            self.console.error(
                _("检测新版本失败"),
            )

    async def main_menu(
        self,
        mode=None,
    ):
        """选择功能模式"""
        while self.running:
            self.__update_menu()
            if not mode:
                mode = choose(
                    _("DouK-Downloader 功能选项"),
                    [i for i, __ in self.__function_menu],
                    self.console,
                    separate=(
                        4,
                        8,
                    ),
                )
            await self.compatible(mode)
            mode = None

    async def complete(self):
        """终端交互模式"""
        example = TikTok(
            self.parameter,
            self.database,
        )
        try:
            await example.run(self.run_command)
            self.running = example.running
        except KeyboardInterrupt:
            self.running = False

    async def monitor(self):
        await self.monitor_clipboard()

    async def monitor_clipboard(self):
        example = ClipboardMonitor(
            self.parameter,
            self.database,
        )
        try:
            await example.run(self.run_command)
        except (KeyboardInterrupt, CancelledError):
            await example.stop_listener()

    async def change_config(
        self,
        key: str,
    ):
        self.config[key] = 0 if self.config[key] else 1
        await self.database.update_config_data(key, self.config[key])
        self.console.print(_("修改设置成功！"))
        self.check_config()
        await self.check_settings()

    async def write_cookie(self):
        await self.__write_cookie(False)

    async def write_cookie_tiktok(self):
        await self.__write_cookie(True)

    async def __write_cookie(self, tiktok: bool):
        self.console.print(
            _("Cookie 获取教程：")
            + "https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6"
            "%95%99%E7%A8%8B.md"
        )
        if self.console.input(
            _(
                "复制 Cookie 内容至剪贴板后，按回车键确认继续；若输入任意内容并按回车，则取消操作："
            )
        ):
            return
        if self.cookie.run(tiktok):
            await self.check_settings()

    # async def auto_cookie(self):
    #     self.console.error(
    #         _(
    #             "该功能为实验性功能，仅适用于学习和研究目的；目前仅支持抖音平台，建议使用其他方式获取 Cookie，未来可能会禁用或移除该功能！"
    #         ),
    #     )
    #     if self.console.input(_("是否返回上一级菜单(YES/NO)")).upper() != "NO":
    #         return
    #     if cookie := await Register(
    #         self.parameter,
    #         self.settings,
    #     ).run():
    #         self.cookie.extract(cookie, platform=_("抖音"))
    #         await self.check_settings()
    #     else:
    #         self.console.warning(
    #             _("扫码登录失败，未写入 Cookie！"),
    #         )

    async def compatible(self, mode: str):
        if mode in {"Q", "q", ""}:
            self.running = False
        try:
            n = int(mode) - 1
        except ValueError:
            return
        if n in range(len(self.__function_menu)):
            await self.__function_menu[n][1]()

    async def delete_works_ids(self):
        if not self.config["Record"]:
            self.console.warning(
                _("作品下载记录功能已禁用！"),
            )
            return
        await self.recorder.delete_ids(self.console.input("请输入需要删除的作品 ID："))
        self.console.info(
            "删除作品下载记录成功！",
        )

    async def check_settings(self, restart=True):
        if restart:
            await self.parameter.close_client()
        self.parameter = Parameter(
            self.settings,
            self.cookie,
            logger=self.logger,
            console=self.console,
            **self.settings.read(),
            recorder=self.recorder,
        )
        MigrateFolder(self.parameter).compatible()
        self.parameter.set_headers_cookie()
        self.restart_cycle_task(
            restart,
        )
        # await self.parameter.update_params_offline()
        if not restart:
            self.run_command = self.parameter.run_command.copy()
        self.parameter.CLEANER.set_rule(TEXT_REPLACEMENT, True)

    async def run(self):
        self.project_info()
        self.check_config()
        await self.check_settings(
            False,
        )
        if await self.disclaimer():
            await self.main_menu(safe_pop(self.run_command))

    def periodic_update_params(self):
        async def inner():
            while not self.event_cookie.is_set():
                await self.parameter.update_params()
                self.event_cookie.wait(COOKIE_UPDATE_INTERVAL)

        run(
            inner(),
        )

    def restart_cycle_task(
        self,
        restart=True,
    ):
        if restart:
            self.event_cookie.set()
            while self.params_task.is_alive():
                # print("等待子线程结束！")  # 调试代码
                sleep(1)
        self.params_task = Thread(target=self.periodic_update_params)
        self.event_cookie.clear()
        self.params_task.start()

    def close(self):
        self.event_cookie.set()
        if self.parameter.folder_mode:
            remove_empty_directories(self.parameter.ROOT)
            remove_empty_directories(self.parameter.root)
        self.parameter.logger.info(_("正在关闭程序"))

    async def browser_cookie(
        self,
    ):
        if Browser(self.parameter, self.cookie).run(
            select=safe_pop(self.run_command),
        ):
            await self.check_settings()

    async def browser_cookie_tiktok(
        self,
    ):
        if Browser(self.parameter, self.cookie).run(
            True,
            select=safe_pop(self.run_command),
        ):
            await self.check_settings()
```

## File: `src/application/__init__.py`
```python
from .TikTokDownloader import TikTokDownloader

__all__ = ["TikTokDownloader"]
```

## File: `src/cli_edition/main_cli.py`
```python
__all__ = ["cli"]


class Cli:
    pass


def cli():
    pass
```

## File: `src/cli_edition/write.py`
```python
from pathlib import Path

from src.config import Settings
from src.custom import PROJECT_ROOT
from src.tools import ColorfulConsole
from src.translation import _
from src.custom import VERSION_BETA


class Write:
    def __init__(
        self,
    ):
        self.console = ColorfulConsole(
            debug=VERSION_BETA,
        )
        self.settings = Settings(PROJECT_ROOT, self.console)
        self.data = self.settings.read()

    def run(self):
        data = self.txt_inquire()
        self.generate_data(data)
        self.settings.update(self.data)

    def generate_data(self, data: str):
        for i in data.split("\n"):
            if i.strip():
                self.data["accounts_urls_tiktok"].append(
                    {
                        "mark": "",
                        "url": i,
                        "tab": "post",
                        "earliest": "",
                        "latest": "",
                        "enable": True,
                    }
                )

    def txt_inquire(self) -> str:
        if path := self.console.input(_("请输入文本文档路径：")):
            if (t := Path(path.replace('"', ""))).is_file():
                try:
                    with t.open("r", encoding=self.settings.encode) as f:
                        return f.read()
                except UnicodeEncodeError as e:
                    self.console.warning(
                        _("{path} 文件读取异常: {error}").format(path=path, error=e)
                    )
            else:
                self.console.print(_("{path} 文件不存在！").format(path=path))
        return ""


if __name__ == "__main__":
    Write().run()
```

## File: `src/cli_edition/__init__.py`
```python
from .main_cli import cli

__all__ = ["cli"]
```

## File: `src/config/parameter.py`
```python
from pathlib import Path
from shutil import move
from time import localtime, strftime
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any, Type

from httpx import HTTPStatusError, RequestError, TimeoutException, get

from ..custom import (
    BLANK_PREVIEW,
    DATA_HEADERS,
    DATA_HEADERS_TIKTOK,
    DOWNLOAD_HEADERS,
    DOWNLOAD_HEADERS_TIKTOK,
    PARAMS_HEADERS,
    PARAMS_HEADERS_TIKTOK,
    PROJECT_ROOT,
    QRCODE_HEADERS,
    TIMEOUT,
    USERAGENT,
)
from ..encrypt import (
    ABogus,
    MsToken,
    MsTokenTikTok,
    TtWid,
    TtWidTikTok,
    XBogus,
    XGnarly,
)
from ..extract import Extractor
from ..interface import API, APITikTok
from ..module import FFMPEG
from ..record import BaseLogger, LoggerManager
from ..storage import RecordManager
from ..tools import Cleaner, DownloaderError, cookie_dict_to_str, create_client
from ..translation import _

if TYPE_CHECKING:
    from ..manager import DownloadRecorder
    from ..module import Cookie
    from ..tools import ColorfulConsole
    from .settings import Settings

__all__ = ["Parameter"]


class Parameter:
    NAME_KEYS = (
        "id",
        "desc",
        "create_time",
        "nickname",
        "uid",
        "mark",
        "type",
    )
    CLEANER = Cleaner()
    HEADERS = {"User-Agent": USERAGENT}
    NO_PROXY = {
        "http://": None,
        "https://": None,
    }

    def __init__(
        self,
        settings: "Settings",
        cookie_object: "Cookie",
        logger: Type[BaseLogger | LoggerManager],
        console: "ColorfulConsole",
        cookie: dict | str,
        cookie_tiktok: dict | str,
        root: str,
        accounts_urls: list[dict],
        accounts_urls_tiktok: list[dict],
        mix_urls: list[dict],
        mix_urls_tiktok: list[dict],
        folder_name: str,
        name_format: str,
        desc_length: int,
        name_length: int,
        date_format: str,
        split: str,
        music: bool,
        folder_mode: bool,
        truncate: int,
        storage_format: str,
        dynamic_cover: bool,
        static_cover: bool,
        proxy: str | None | dict,
        proxy_tiktok: str | None | dict,
        twc_tiktok: str,
        download: bool,
        max_size: int,
        chunk: int,
        max_retry: int,
        max_pages: int,
        run_command: str,
        owner_url: dict,
        owner_url_tiktok: dict,
        live_qualities: str,
        ffmpeg: str,
        recorder: "DownloadRecorder",
        browser_info: dict,
        browser_info_tiktok: dict,
        timeout=10,
        douyin_platform=True,
        tiktok_platform=True,
        **kwargs,
    ):
        self.settings = settings
        self.cookie_object = cookie_object
        self.ROOT = PROJECT_ROOT  # 项目根路径
        self.cache = PROJECT_ROOT.joinpath("Cache")  # 缓存路径
        self.logger = logger(PROJECT_ROOT, console)
        self.logger.run()
        self.ab = ABogus()
        self.xb = XBogus()
        self.xg = XGnarly()
        self.console = console
        self.recorder = recorder
        self.preview = BLANK_PREVIEW
        self.ms_token = ""
        self.ms_token_tiktok = ""

        self.headers = DATA_HEADERS
        self.headers_tiktok = DATA_HEADERS_TIKTOK
        self.headers_download = DOWNLOAD_HEADERS
        self.headers_download_tiktok = DOWNLOAD_HEADERS_TIKTOK
        self.headers_params = PARAMS_HEADERS
        self.headers_params_tiktok = PARAMS_HEADERS_TIKTOK
        self.headers_qrcode = QRCODE_HEADERS

        self.accounts_urls: list[SimpleNamespace] = self.check_urls_params(
            accounts_urls
        )
        self.accounts_urls_tiktok: list[SimpleNamespace] = self.check_urls_params(
            accounts_urls_tiktok
        )
        self.mix_urls: list[SimpleNamespace] = self.check_urls_params(mix_urls)
        self.mix_urls_tiktok: list[SimpleNamespace] = self.check_urls_params(
            mix_urls_tiktok
        )
        self.owner_url: SimpleNamespace = self.check_url_params(owner_url)
        self.owner_url_tiktok: SimpleNamespace | None = None

        self.cookie_dict, self.cookie_str = self.__check_cookie(cookie)
        self.cookie_dict_tiktok, self.cookie_str_tiktok = self.__check_cookie_tiktok(
            cookie_tiktok,
        )
        self.cookie_state: bool = self.__check_cookie_state()
        self.cookie_tiktok_state: bool = self.__check_cookie_state(True)
        self.set_uif_id()
        # self.set_download_headers()

        self.root = self.__check_root(root)
        self.folder_name = self.__check_folder_name(folder_name)
        self.name_format = self.__check_name_format(name_format)
        self.desc_length = self.__check_desc_length(desc_length)
        self.name_length = self.__check_name_length(name_length)
        self.date_format = self.__check_date_format(date_format)
        self.split = self.__check_split(split)
        self.folder_mode = self.check_bool_false(folder_mode)
        self.music = self.check_bool_false(music)
        self.truncate = self.__check_truncate(truncate)
        self.storage_format = self.__check_storage_format(storage_format)
        self.dynamic_cover = self.check_bool_false(dynamic_cover)
        self.static_cover = self.check_bool_false(static_cover)
        self.twc_tiktok = self.check_str(twc_tiktok)
        self.download = self.check_bool_true(download)
        self.max_size = self.__check_max_size(max_size)
        self.chunk = self.__check_chunk(chunk)
        self.timeout = self.__check_timeout(timeout)
        self.max_retry = self.__check_max_retry(max_retry)
        self.max_pages = self.__check_max_pages(max_pages)
        self.run_command = self.__check_run_command(run_command)
        self.ffmpeg = self.__generate_ffmpeg_object(ffmpeg)
        self.live_qualities = self.__check_live_qualities(live_qualities)
        self.douyin_platform = self.check_bool_true(
            douyin_platform,
        )
        self.tiktok_platform = self.check_bool_true(
            tiktok_platform,
        )

        self.browser_info = self.merge_browser_info(
            browser_info,
            {},
        )
        self.browser_info_tiktok = self.merge_browser_info(
            browser_info_tiktok,
            {},
        )
        self.__set_browser_info(self.browser_info)
        self.__set_browser_info_tiktok(self.browser_info_tiktok)

        self.proxy: str | None = self.__check_proxy(
            proxy,
            remark=_("抖音"),
            enable=self.douyin_platform,
        )
        self.proxy_tiktok: str | None = self.__check_proxy_tiktok(proxy_tiktok)
        self.client = create_client(
            timeout=self.timeout,
            proxy=self.proxy,
        )
        self.client_tiktok = create_client(
            timeout=self.timeout,
            proxy=self.proxy_tiktok,
        )

        self.__generate_folders()

        # self.__URLS_PARAMS = {
        #     "accounts_urls": None,
        #     "accounts_urls_tiktok": None,
        #     "mix_urls": None,
        #     "mix_urls_tiktok": None,
        #     "owner_url": None,
        #     "owner_url_tiktok": None,
        # }
        self.__CHECK = {
            "root": self.__check_root,
            "folder_name": self.__check_folder_name,
            "name_format": self.__check_name_format,
            "desc_length": self.__check_desc_length,
            "name_length": self.__check_name_length,
            "date_format": self.__check_date_format,
            "split": self.__check_split,
            "folder_mode": self.check_bool_false,
            "music": self.check_bool_false,
            "truncate": self.__check_truncate,
            "storage_format": self.__check_storage_format,
            "dynamic_cover": self.check_bool_false,
            "static_cover": self.check_bool_false,
            "twc_tiktok": self.check_str,
            "download": self.check_bool_true,
            "max_size": self.__check_max_size,
            "chunk": self.__check_chunk,
            "timeout": self.__check_timeout,
            "max_retry": self.__check_max_retry,
            "max_pages": self.__check_max_pages,
            "run_command": self.__check_run_command,
            "ffmpeg": self.__generate_ffmpeg_object,
            "live_qualities": self.__check_live_qualities,
            "douyin_platform": self.check_bool_true,
            "tiktok_platform": self.check_bool_true,
        }
        # self.__BROWSER_INFO = {
        #     "browser_info": None,
        #     "browser_info_tiktok": None,
        # }

    @staticmethod
    def check_bool_false(
        value: bool,
    ) -> bool:
        return value if isinstance(value, bool) else False

    @staticmethod
    def check_bool_true(
        value: bool,
    ) -> bool:
        return value if isinstance(value, bool) else True

    def __check_cookie_tiktok(
        self,
        cookie: dict | str,
    ) -> tuple[dict, str]:
        # if isinstance(cookie, str):
        #     self.console.print(
        #         "参数 cookie_tiktok 应为字典格式！请修改配置文件后重新运行程序！",
        #         style=ERROR)
        return self.__check_cookie(cookie, name="cookie_tiktok")

    def __check_cookie(self, cookie: dict | str, name="cookie") -> tuple[dict, str]:
        if isinstance(cookie, dict):
            return cookie, ""
        elif isinstance(cookie, str):
            return {}, cookie
        else:
            self.logger.warning(_("{name} 参数格式错误").format(name=name))
        return {}, ""

    def __get_cookie(
        self,
        cookie: dict,
    ) -> dict:
        return self.__check_cookie(cookie)[0]

    def __get_cookie_cache(
        self,
        cookie: str,
    ) -> str:
        return self.__check_cookie(cookie)[1]

    def __get_cookie_tiktok(
        self,
        cookie: dict,
    ) -> dict:
        return self.__check_cookie_tiktok(cookie)[0]

    def __get_cookie_tiktok_cache(
        self,
        cookie: str,
    ) -> str:
        return self.__check_cookie_tiktok(cookie)[1]

    def __add_cookie(
        self,
        parameters: tuple[dict, ...],
        cookie: dict | str,
    ) -> None | str:
        if isinstance(cookie, dict):
            for i in parameters:
                if i:
                    self.logger.info(
                        f"参数: {i}",
                        False,
                    )
                    cookie |= i
            return None
        elif isinstance(cookie, str):
            for i in parameters:
                if i:
                    self.logger.info(
                        f"参数: {i}",
                        False,
                    )
                    cookie += f"; {cookie_dict_to_str(i)}"
            return cookie
        raise DownloaderError

    async def __get_tt_wid_params(self) -> dict:
        if tt_wid := await TtWid.get_tt_wid(
            self.logger,
            self.headers_params,
            proxy=self.proxy,
        ):
            self.logger.info(f"抖音 {TtWid.NAME} 请求值: {tt_wid[TtWid.NAME]}", False)
            return tt_wid
        return {}

    async def __get_tt_wid_params_tiktok(self) -> dict:
        if tt_wid := await TtWidTikTok.get_tt_wid(
            self.logger,
            self.headers_params_tiktok,
            self.twc_tiktok
            or f"{TtWidTikTok.NAME}={
                self.cookie_dict_tiktok.get(TtWidTikTok.NAME, '')
                or self.get_cookie_value(
                    self.cookie_str_tiktok,
                    TtWidTikTok.NAME,
                )
            }",
            proxy=self.proxy_tiktok,
        ):
            self.logger.info(
                f"TikTok {TtWidTikTok.NAME} 请求值: {tt_wid[TtWidTikTok.NAME]}", False
            )
            return tt_wid
        return {}

    def __check_root(self, root: str) -> Path:
        if not root:
            return self.ROOT
        if (r := Path(root)).is_dir():
            self.logger.info(f"root 参数已设置为 {root}", False)
            return r
        if r := self.__check_root_again(r):
            self.logger.info(f"root 参数已设置为 {r}", False)
            return r
        self.logger.warning(
            _(
                "root 参数 {root} 不是有效的文件夹路径，程序将使用项目根路径作为储存路径"
            ).format(root=root),
        )
        return self.ROOT

    @staticmethod
    def __check_root_again(root: Path) -> bool | Path:
        if root.resolve().parent.is_dir():
            root.mkdir()
            return root
        return False

    def __check_folder_name(self, folder_name: str) -> str:
        if folder_name := self.CLEANER.filter_name(
            folder_name,
        ):
            self.logger.info(f"folder_name 参数已设置为 {folder_name}", False)
            return folder_name
        self.logger.warning(
            _(
                "folder_name 参数 {folder_name} 不是有效的文件夹名称，程序将使用默认值：Download"
            ).format(folder_name=folder_name),
        )
        return "Download"

    def __check_name_format(self, name_format: str) -> list[str]:
        name_keys = name_format.strip().split(" ")
        if all(i in self.NAME_KEYS for i in name_keys):
            self.logger.info(f"name_format 参数已设置为 {name_format}", False)
            return name_keys
        else:
            self.logger.warning(
                _(
                    "name_format 参数 {name_format} 设置错误，程序将使用默认值：创建时间 作品类型 账号昵称 作品描述"
                ).format(name_format=name_format)
            )
            return ["create_time", "type", "nickname", "desc"]

    def __check_date_format(self, date_format: str) -> str:
        try:
            strftime(date_format, localtime())
            self.logger.info(f"date_format 参数已设置为 {date_format}", False)
            return date_format
        except ValueError:
            self.logger.warning(
                _(
                    "date_format 参数 {date_format} 设置错误，程序将使用默认值：年-月-日 时:分:秒"
                ).format(date_format=date_format),
            )
            return "%Y-%m-%d %H:%M:%S"

    def __check_split(self, split: str) -> str:
        for i in split:
            if i in self.CLEANER.rule.keys():
                self.logger.warning(
                    _("split 参数 {split} 包含非法字符，程序将使用默认值：-").format(
                        split=split
                    )
                )
                return "-"
        self.logger.info(f"split 参数已设置为 {split}", False)
        return split

    def __check_proxy_tiktok(
        self,
        proxy: str | None | dict,
    ) -> str | None:
        return self.__check_proxy(
            proxy,
            "https://www.tiktok.com/explore",
            "TikTok",
            self.tiktok_platform,
        )

    def __check_proxy(
        self,
        proxy: str | None | dict,
        url="https://www.douyin.com/?recommend=1",
        remark=_("抖音"),
        enable=True,
    ) -> str | None:
        if enable and proxy:
            # 暂时兼容旧版配置；未来将会移除
            if isinstance(proxy, dict):
                self.console.warning(
                    _("{remark}代理参数应为字符串格式，未来不再支持字典格式").format(
                        remark=remark
                    )
                )
                if not (proxy := proxy.get("https://")):
                    return None
            try:
                response = get(
                    url,
                    headers=self.HEADERS,
                    follow_redirects=True,
                    timeout=TIMEOUT,
                    proxy=proxy,
                )
                response.raise_for_status()
                self.logger.info(
                    _("{remark}代理 {proxy} 测试成功").format(
                        remark=remark, proxy=proxy
                    )
                )
                return proxy
            except TimeoutException:
                self.logger.warning(
                    _("{remark}代理 {proxy} 测试超时").format(
                        remark=remark, proxy=proxy
                    )
                )
                return None
            except (
                RequestError,
                HTTPStatusError,
            ) as e:
                self.logger.warning(
                    _("{remark}代理 {proxy} 测试失败：{error}").format(
                        remark=remark, proxy=proxy, error=e
                    ),
                )
                return None
        return None

    def __check_max_size(self, max_size: int) -> int:
        max_size = max(max_size, 0)
        self.logger.info(f"max_size 参数已设置为 {max_size}", False)
        return max_size

    def __check_chunk(self, chunk: int) -> int:
        return self.__check_number_value(
            chunk,
            "chunk",
            1024 * 128,
            1024 * 1024 * 2,
        )

    def __check_max_retry(self, max_retry: int) -> int:
        return self.__check_number_value(
            max_retry,
            "max_retry",
            0,
            5,
        )

    def __check_max_pages(self, max_pages: int) -> int:
        if isinstance(max_pages, int) and max_pages > 0:
            self.logger.info(f"max_pages 参数已设置为 {max_pages}", False)
            return max_pages
        elif max_pages != 0:
            self.logger.warning(
                _(
                    "max_pages 参数 {max_pages} 设置错误，程序将使用默认值：99999"
                ).format(max_pages=max_pages),
            )
        return 99999

    def __check_timeout(self, timeout: int | float) -> int | float:
        return self.__check_number_value(
            timeout,
            "timeout",
            2,
            10,
        )

    def __check_storage_format(self, storage_format: str) -> str:
        if storage_format in RecordManager.DataLogger.keys():
            self.logger.info(f"storage_format 参数已设置为 {storage_format}", False)
            return storage_format
        if not storage_format:
            self.logger.info(
                "storage_format 参数未设置，程序不会储存任何数据至文件", False
            )
        else:
            self.logger.warning(
                _(
                    "storage_format 参数 {storage_format} 设置错误，程序默认不会储存任何数据至文件"
                ).format(storage_format=storage_format),
            )
        return ""

    @staticmethod
    def __check_run_command(run_command: str) -> list:
        return run_command.split()[::-1] if run_command else []

    async def update_params(self) -> None:
        if self.douyin_platform:
            if any(
                (
                    self.cookie_dict,
                    self.cookie_str,
                )
            ):
                self.console.info(
                    _("正在更新抖音参数，请稍等..."),
                )
                ms_token = await self.__get_token_params()
                tt_wid = await self.__get_tt_wid_params()
                API.params["msToken"] = ms_token.get(MsToken.NAME, "")
                await self.__update_cookie(
                    (
                        ms_token,
                        tt_wid,
                    ),
                    (
                        self.headers,
                        self.headers_download,
                    ),
                    self.cookie_dict,
                    self.cookie_str,
                )
                self.console.info(
                    _("抖音参数更新完毕！"),
                )
            else:
                self.logger.warning(
                    _("配置文件 cookie 参数未设置，抖音平台功能可能无法正常使用")
                )
        if self.tiktok_platform:
            if any(
                (
                    self.cookie_dict_tiktok,
                    self.cookie_str_tiktok,
                )
            ):
                self.console.info(
                    _("正在更新 TikTok 参数，请稍等..."),
                )
                ms_token = await self.__get_token_params_tiktok()
                tt_wid = await self.__get_tt_wid_params_tiktok()
                APITikTok.params["msToken"] = ms_token.get(MsTokenTikTok.NAME, "")
                await self.__update_cookie(
                    (
                        ms_token,
                        tt_wid,
                    ),
                    (
                        self.headers_tiktok,
                        self.headers_download_tiktok,
                    ),
                    self.cookie_dict_tiktok,
                    self.cookie_str_tiktok,
                )
                self.console.info(
                    _("TikTok 参数更新完毕！"),
                )
            else:
                self.logger.warning(
                    _(
                        "配置文件 cookie_tiktok 参数未设置，TikTok 平台功能可能无法正常使用"
                    )
                )

    async def update_params_offline(self) -> None:
        if self.douyin_platform:
            if any(
                (
                    self.cookie_dict,
                    self.cookie_str,
                )
            ):
                ms_token = self.cookie_dict.get(MsToken.NAME) or self.get_cookie_value(
                    self.cookie_str,
                    MsToken.NAME,
                )
                API.params["msToken"] = ms_token
                await self.__update_cookie(
                    ({MsToken.NAME: ms_token},),
                    (
                        self.headers,
                        self.headers_download,
                    ),
                    self.cookie_dict,
                    self.cookie_str,
                )
            else:
                self.logger.warning(
                    _("配置文件 cookie 参数未设置，抖音平台功能可能无法正常使用")
                )
        if self.tiktok_platform:
            if any(
                (
                    self.cookie_dict_tiktok,
                    self.cookie_str_tiktok,
                )
            ):
                ms_token = await self.__get_token_params_tiktok()
                APITikTok.params["msToken"] = ms_token.get(MsTokenTikTok.NAME, "")
                await self.__update_cookie(
                    (ms_token,),
                    (
                        self.headers_tiktok,
                        self.headers_download_tiktok,
                    ),
                    self.cookie_dict_tiktok,
                    self.cookie_str_tiktok,
                )
            else:
                self.logger.warning(
                    _(
                        "配置文件 cookie_tiktok 参数未设置，TikTok 平台功能可能无法正常使用"
                    )
                )

    async def __update_cookie(
        self,
        parameters: tuple[dict, ...],
        headers: tuple[dict, ...],
        cookie_dict: dict,
        cookie_str: str,
    ) -> None:
        cookie = self.__add_cookie(
            parameters,
            cookie_dict or cookie_str,
        )
        if not isinstance(cookie, str):
            cookie = cookie_dict_to_str(cookie_dict)
        for i in headers:
            i["Cookie"] = cookie

    def set_headers_cookie(
        self,
    ) -> None:
        if self.cookie_dict:
            cookie = cookie_dict_to_str(self.cookie_dict)
            self.headers["Cookie"] = cookie
            self.headers_download["Cookie"] = cookie
        elif self.cookie_str:
            self.headers["Cookie"] = self.cookie_str
            self.headers_download["Cookie"] = self.cookie_str
        if self.cookie_dict_tiktok:
            cookie = cookie_dict_to_str(self.cookie_dict_tiktok)
            self.headers_tiktok["Cookie"] = cookie
            self.headers_download_tiktok["Cookie"] = cookie
        elif self.cookie_str_tiktok:
            self.headers_tiktok["Cookie"] = self.cookie_str_tiktok
            self.headers_download_tiktok["Cookie"] = self.cookie_str_tiktok

    def set_download_headers(self) -> None:
        self.__update_download_headers()
        self.__update_download_headers_tiktok()

    def __update_download_headers(self) -> None:
        self.headers_download["Cookie"] = "dy_swidth=1536; dy_sheight=864"

    def __update_download_headers_tiktok(self) -> None:
        key = "tt_chain_token"
        if tk := self.cookie_dict_tiktok.get(
            key,
        ):
            self.headers_download_tiktok["Cookie"] = f"{key}={tk}"
        else:
            self.headers_download_tiktok["Cookie"] = self.cookie_str_tiktok
        # self.headers_download_tiktok["Cookie"] = self.headers_tiktok.get(
        #     "Cookie", "")

    async def __get_token_params(self) -> dict:
        # if not (
        #     m := (
        #         self.cookie_dict.get(MsToken.NAME)
        #         or self.get_cookie_value(
        #             self.cookie_str,
        #             MsToken.NAME,
        #         )
        #     )
        # ):
        #     self.logger.warning(
        #         _("抖音 cookie 缺少 {name} 键值对，请尝试重新写入 cookie").format(
        #             name=MsToken.NAME
        #         )
        #     )
        #     return {}
        if d := await MsToken.get_real_ms_token(
            self.logger,
            self.headers_params,
            # m,
            proxy=self.proxy,
        ):
            self.logger.info(
                f"抖音 MsToken 请求值: {d[MsToken.NAME]}",
                False,
            )
            return d
        else:
            ms_token = self.cookie_dict.get(MsToken.NAME) or self.get_cookie_value(
                self.cookie_str,
                MsToken.NAME,
            )
            self.logger.info(
                f"抖音 MsToken 本地值: {ms_token}",
                False,
            )
            return {MsToken.NAME: ms_token}

    async def __get_token_params_tiktok(self) -> dict:
        if not (
            m := (
                self.cookie_dict_tiktok.get(MsTokenTikTok.NAME)
                or self.get_cookie_value(
                    self.cookie_str_tiktok,
                    MsTokenTikTok.NAME,
                )
            )
        ):
            self.logger.warning(
                _("TikTok cookie 缺少 {name} 键值对，请尝试重新写入 cookie").format(
                    name=MsTokenTikTok.NAME
                )
            )
            return {}
        # if d := await MsTokenTikTok.get_long_ms_token(
        #     self.logger,
        #     self.headers_params_tiktok,
        #     m,
        #     proxy=self.proxy_tiktok,
        # ):
        #     self.logger.info(
        #         f"TikTok MsToken 请求值: {d[MsTokenTikTok.NAME]}",
        #         False,
        #     )
        #     return d
        # else:
        #     self.logger.info(
        #         f"TikTok MsToken 本地值: {m}",
        #         False,
        #     )
        #     return {MsTokenTikTok.NAME: m}
        return {MsTokenTikTok.NAME: m}

    def set_uif_id(
        self,
    ) -> None:
        if self.cookie_dict:
            API.params["uifid"] = self.cookie_dict.get("UIFID", "")
        elif self.cookie_str:
            API.params["uifid"] = self.get_cookie_value(
                self.cookie_str,
                "UIFID",
            )

    @staticmethod
    def __generate_ffmpeg_object(ffmpeg_path: str) -> FFMPEG:
        return FFMPEG(ffmpeg_path)

    def get_settings_data(self) -> dict:
        return {
            "accounts_urls": [vars(i) for i in self.accounts_urls],
            "accounts_urls_tiktok": [vars(i) for i in self.accounts_urls_tiktok],
            "mix_urls": [vars(i) for i in self.mix_urls],
            "mix_urls_tiktok": [vars(i) for i in self.mix_urls_tiktok],
            "owner_url": vars(self.owner_url),
            "owner_url_tiktok": self.owner_url_tiktok,
            "root": str(self.root.resolve()),
            "folder_name": self.folder_name,
            "name_format": " ".join(self.name_format),
            "desc_length": self.desc_length,
            "name_length": self.name_length,
            "date_format": self.date_format,
            "split": self.split,
            "folder_mode": self.folder_mode,
            "music": self.music,
            "truncate": self.truncate,
            "storage_format": self.storage_format,
            "cookie": self.cookie_str or self.cookie_dict,
            "cookie_tiktok": self.cookie_str_tiktok or self.cookie_dict_tiktok,
            "dynamic_cover": self.dynamic_cover,
            "static_cover": self.static_cover,
            "proxy": self.proxy,
            "proxy_tiktok": self.proxy_tiktok,
            "twc_tiktok": self.twc_tiktok,
            "download": self.download,
            "max_size": self.max_size,
            "chunk": self.chunk,
            "max_retry": self.max_retry,
            "max_pages": self.max_pages,
            "run_command": " ".join(self.run_command[::-1]),
            "ffmpeg": self.ffmpeg.path or "",
        }

    async def set_settings_data(
        self,
        data: dict,
    ) -> None:
        self.set_urls_params(
            data.pop("accounts_urls"),
            data.pop("mix_urls"),
            data.pop("owner_url"),
            data.pop("accounts_urls_tiktok"),
            data.pop("mix_urls_tiktok"),
            data.pop("owner_url_tiktok"),
        )
        self.set_cookie(
            data.pop(
                "cookie",
            ),
            data.pop(
                "cookie_tiktok",
            ),
        )
        self.set_browser_info(
            data.pop(
                "browser_info",
            ),
            data.pop(
                "browser_info_tiktok",
            ),
        )
        await self.set_proxy(
            data.pop(
                "proxy",
            ),
            data.pop(
                "proxy_tiktok",
            ),
        )
        self.set_general_params(data)

    async def __update_cookie_data(self, data: dict) -> None:
        for i, j in zip(("cookie", "cookie_tiktok"), (_("抖音"), "TikTok")):
            if c := data.get(i):
                setattr(
                    self, i, self.cookie_object.extract(c, False, key=i, platform=j)
                )
        await self.update_params()

    @staticmethod
    def check_urls_params(data: list[dict]) -> list[SimpleNamespace]:
        items = []
        for item in data:
            if not item.get("url") or not item.get("enable", True):
                continue
            if not isinstance(item.get("mark"), str):
                item["mark"] = ""
            items.append(item)
        return Extractor.generate_data_object(items)

    @staticmethod
    def check_url_params(data: dict) -> SimpleNamespace:
        if not data.get("url"):
            return SimpleNamespace(
                mark="",
                url="",
            )
        if not isinstance(data.get("mark"), str):
            data["mark"] = ""
        return Extractor.generate_data_object(data)

    def set_urls_params(
        self,
        accounts_urls: list[dict],
        mix_urls: list[dict],
        owner_url: dict,
        accounts_urls_tiktok: list[dict],
        mix_urls_tiktok: list[dict],
        owner_url_tiktok: dict,
    ):
        if accounts_urls:
            self.accounts_urls = self.check_urls_params(accounts_urls)
        if accounts_urls_tiktok:
            self.accounts_urls_tiktok = self.check_urls_params(accounts_urls_tiktok)
        if mix_urls:
            self.mix_urls = self.check_urls_params(mix_urls)
        if mix_urls_tiktok:
            self.mix_urls_tiktok = self.check_urls_params(mix_urls_tiktok)
        if owner_url:
            self.owner_url = self.check_url_params(owner_url)
        # if owner_url_tiktok:
        #     self.owner_url_tiktok = self.check_url_params(owner_url_tiktok)

    def set_cookie(
        self, cookie: str | dict[str, str], cookie_tiktok: str | dict[str, str]
    ):
        if cookie:
            self.cookie_dict, self.cookie_str = self.__check_cookie(cookie)
            self.cookie_state: bool = self.__check_cookie_state()
            self.set_uif_id()
        if cookie_tiktok:
            self.cookie_dict_tiktok, self.cookie_str_tiktok = (
                self.__check_cookie_tiktok(
                    cookie_tiktok,
                )
            )
            self.cookie_tiktok_state: bool = self.__check_cookie_state(True)
            self.__update_download_headers_tiktok()

    def set_general_params(self, data: dict[str, Any]) -> None:
        for i, j in data.items():
            if j is not None:
                self.__CHECK[i](j)

    async def set_proxy(self, proxy: str | None, proxy_tiktok: str | None):
        if isinstance(proxy, str):
            self.proxy: str | None = self.__check_proxy(
                proxy,
                remark=_("抖音"),
                enable=self.douyin_platform,
            )
        if isinstance(proxy_tiktok, str):
            self.proxy_tiktok: str | None = self.__check_proxy_tiktok(proxy_tiktok)
        await self.close_client()
        self.client = create_client(
            timeout=self.timeout,
            proxy=self.proxy,
        )
        self.client_tiktok = create_client(
            timeout=self.timeout,
            proxy=self.proxy_tiktok,
        )

    @staticmethod
    def merge_browser_info(
        browser_info: dict,
        new_info: dict,
    ) -> dict:
        return browser_info | new_info

    def set_browser_info(self, browser_info: dict, browser_info_tiktok: dict):
        self.browser_info = self.merge_browser_info(
            self.browser_info,
            browser_info or {},
        )
        self.browser_info_tiktok = self.merge_browser_info(
            self.browser_info_tiktok,
            browser_info_tiktok or {},
        )
        self.__set_browser_info(self.browser_info)
        self.__set_browser_info_tiktok(self.browser_info_tiktok)

    @staticmethod
    def check_str(value: str) -> str:
        return value if isinstance(value, str) else ""

    async def close_client(self) -> None:
        await self.client.aclose()
        await self.client_tiktok.aclose()

    def __generate_folders(self):
        self.compatible()
        self.cache.mkdir(exist_ok=True)

    def __set_browser_info(
        self,
        info: dict[str, str],
    ) -> None:
        self.logger.info(f"抖音浏览器信息: {info}", False)
        if ua := info.get(
            "User-Agent",
        ):
            for i in (
                self.headers,
                self.headers_download,
                self.headers_params,
                self.headers_qrcode,
            ):
                i["User-Agent"] = ua
        else:
            ua = USERAGENT
        for i in (
            "pc_libra_divert",
            "browser_language",
            "browser_platform",
            "browser_name",
            "browser_version",
            "engine_name",
            "engine_version",
            "os_name",
            "os_version",
            # 'webid',
        ):
            if v := info.get(
                i,
            ):
                API.params[i] = v
        self.ab = ABogus(
            ua,
            info.get(
                "browser_platform",
            ),
        )

    def __set_browser_info_tiktok(
        self,
        info: dict,
    ):
        self.logger.info(f"TikTok 浏览器信息: {info}", False)
        if ua := info.get(
            "User-Agent",
        ):
            for i in (
                self.headers_tiktok,
                self.headers_download_tiktok,
                self.headers_params_tiktok,
            ):
                i["User-Agent"] = ua
        for i in (
            "app_language",
            "browser_language",
            "browser_name",
            "browser_platform",
            "browser_version",
            "language",
            "os",
            "priority_region",
            "region",
            "tz_name",
            "webcast_language",
            "device_id",
        ):
            if v := info.get(
                i,
            ):
                APITikTok.params[i] = v

    def __check_truncate(self, truncate: int) -> int:
        return self.__check_number_value(
            truncate,
            "truncate",
            25,
            50,
        )

    def __check_name_length(self, name_length: int) -> int:
        return self.__check_number_value(
            name_length,
            "name_length",
            32,
            128,
        )

    def __check_desc_length(self, desc_length: int) -> int:
        return self.__check_number_value(
            desc_length,
            "desc_length",
            16,
            64,
        )

    def __check_number_value(
        self, value: int, name: str, minimum: int, default: int
    ) -> int:
        if isinstance(value, int):
            if value >= minimum:
                self.logger.info(f"{name} 参数已设置为 {value}", False)
                return value
            self.logger.warning(
                _("{key} 参数 {value} 设置过小，程序将使用默认值：{default}").format(
                    key=name,
                    value=value,
                    default=default,
                ),
            )
            return default
        self.logger.warning(
            _("{key} 参数 {value} 设置错误，程序将使用默认值：{default}").format(
                key=name,
                value=value,
                default=default,
            ),
        )
        return default

    def __check_live_qualities(self, live_qualities: str) -> str:
        if isinstance(live_qualities, str):
            self.logger.info(f"live_qualities 参数已设置为 {live_qualities}", False)
            return live_qualities
        self.logger.warning(
            _("live_qualities 参数 {live_qualities} 设置错误").format(
                live_qualities=live_qualities
            ),
        )
        return ""

    def __check_cookie_state(self, tiktok=False) -> bool:
        if tiktok:
            return (self.cookie_object.STATE_KEY in self.cookie_dict_tiktok) or (
                self.cookie_object.STATE_KEY in self.cookie_str_tiktok
            )
        return (self.cookie_object.STATE_KEY in self.cookie_dict) or (
            self.cookie_object.STATE_KEY in self.cookie_str
        )

    @staticmethod
    def get_cookie_value(cookie_str: str, key: str, return_key=False) -> str:
        """
        解析cookie字符串并返回指定键的值或键值对

        :param cookie_str: cookie字符串（格式如 "name=John; age=30;"）
        :param key: 需要获取的键名
        :param return_key: 是否返回键值对格式，默认为False
        :return: 键值对字符串或值（若不存在返回None）
        """
        cookies = {}
        for pair in cookie_str.split(";"):
            pair = pair.strip()
            if not pair:
                continue
            # 分割键值（最多分割一次，应对含等号的值）
            key_value = pair.split("=", 1)
            if len(key_value) != 2:
                continue  # 跳过无效格式
            k, v = key_value[0].strip(), key_value[1].strip()
            cookies[k] = v

        value = cookies.get(key)
        if value is None:
            return ""

        return f"{key}={value}" if return_key else value

    def compatible(self):
        if (
            old := self.ROOT.parent.joinpath("Cache")
        ).exists() and not self.cache.exists():
            move(old, self.cache)
```

## File: `src/config/settings.py`
```python
from json import dump, load
from json.decoder import JSONDecodeError
from platform import system
from shutil import move
from types import SimpleNamespace
from typing import TYPE_CHECKING

from ..custom import USERAGENT
from ..translation import _

if TYPE_CHECKING:
    from pathlib import Path

    from ..tools import ColorfulConsole

__all__ = ["Settings"]


class Settings:
    encode = "UTF-8-SIG" if system() == "Windows" else "UTF-8"
    default = {
        "accounts_urls": [
            {
                "mark": "",
                "url": "",
                "tab": "",
                "earliest": "",
                "latest": "",
                "enable": True,
            },
        ],
        "accounts_urls_tiktok": [
            {
                "mark": "",
                "url": "",
                "tab": "",
                "earliest": "",
                "latest": "",
                "enable": True,
            },
        ],
        "mix_urls": [
            {
                "mark": "",
                "url": "",
                "enable": True,
            },
        ],
        "mix_urls_tiktok": [
            {
                "mark": "",
                "url": "",
                "enable": True,
            },
        ],
        "owner_url": {
            "mark": "",
            "url": "",
            "uid": "",
            "sec_uid": "",
            "nickname": "",
        },
        "owner_url_tiktok": None,
        "root": "",
        "folder_name": "Download",
        "name_format": "create_time type nickname desc",
        "desc_length": 64,
        "name_length": 128,
        "date_format": "%Y-%m-%d %H:%M:%S",
        "split": "-",
        "folder_mode": False,
        "music": False,
        "truncate": 50,
        "storage_format": "",
        "cookie": "",
        "cookie_tiktok": "",
        "dynamic_cover": False,
        "static_cover": False,
        "proxy": "",
        "proxy_tiktok": "",
        "twc_tiktok": "",
        "download": True,
        "max_size": 0,
        "chunk": 1024 * 1024 * 2,  # 每次从服务器接收的数据块大小
        "timeout": 10,
        "max_retry": 5,  # 重试最大次数
        "max_pages": 0,
        "run_command": "",
        "ffmpeg": "",
        "live_qualities": "",
        "douyin_platform": True,
        "tiktok_platform": True,
        "browser_info": {
            "User-Agent": USERAGENT,
            "pc_libra_divert": "Windows",
            "browser_language": "zh-CN",
            "browser_platform": "Win32",
            "browser_name": "Chrome",
            "browser_version": "139.0.0.0",
            "engine_name": "Blink",
            "engine_version": "139.0.0.0",
            "os_name": "Windows",
            "os_version": "10",
            "webid": "",
        },
        "browser_info_tiktok": {
            "User-Agent": USERAGENT,
            "app_language": "zh-Hans",
            "browser_language": "zh-CN",
            "browser_name": "Mozilla",
            "browser_platform": "Win32",
            "browser_version": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "language": "zh-Hans",
            "os": "windows",
            "priority_region": "US",
            "region": "US",
            "tz_name": "Asia/Shanghai",
            "webcast_language": "zh-Hans",
            "device_id": "",
        },
    }  # 默认配置
    rename_params = (
        (
            "default_mode",
            "run_command",
            "",
        ),
        (
            "update_cookie",
            "douyin_platform",
            True,
        ),
        (
            "update_cookie_tiktok",
            "tiktok_platform",
            True,
        ),
        (
            "original_cover",
            "static_cover",
            False,
        ),
    )  # 兼容旧版本配置文件

    def __init__(self, root: "Path", console: "ColorfulConsole"):
        self.root = root
        self.file = "settings.json"
        self.path = root.joinpath(self.file)  # 配置文件
        self.console = console

    def __create(self) -> dict:
        """创建默认配置文件"""
        with self.path.open("w", encoding=self.encode) as f:
            dump(self.default, f, indent=4, ensure_ascii=False)
        self.console.info(
            _(
                "创建默认配置文件 settings.json 成功！\n"
                "请参考项目文档的快速入门部分，设置 Cookie 后重新运行程序！\n"
                "建议根据实际使用需求修改配置文件 settings.json！\n"
            ),
        )
        return self.default

    def read(self) -> dict:
        """读取配置文件，如果没有配置文件，则生成配置文件"""
        self.compatible()
        try:
            if self.path.exists():
                with self.path.open("r", encoding=self.encode) as f:
                    return self.__check(load(f))
            return self.__create()  # 生成的默认配置文件必须设置 cookie 才可以正常运行
        except JSONDecodeError:
            self.console.error(
                _("配置文件 settings.json 格式错误，请检查 JSON 格式！"),
            )
            return self.default  # 读取配置文件发生错误时返回空配置

    def __check(self, data: dict) -> dict:
        data = self.__compatible_with_old_settings(data)
        update = False
        for i, j in self.default.items():
            if i not in data:
                data[i] = j
                update = True
                self.console.info(
                    _("配置文件 settings.json 缺少参数 {i}，已自动添加该参数！").format(
                        i=i
                    ),
                )
        if update:
            self.update(data)
        return data

    def update(self, settings: dict | SimpleNamespace):
        """更新配置文件"""
        with self.path.open("w", encoding=self.encode) as f:
            dump(
                settings if isinstance(settings, dict) else vars(settings),
                f,
                indent=4,
                ensure_ascii=False,
            )
        self.console.info(
            _("保存配置成功！"),
        )

    def __compatible_with_old_settings(
        self,
        data: dict,
    ) -> dict:
        """兼容旧版本配置文件"""
        for old, new_, default in self.rename_params:
            if old in data:
                self.console.info(
                    _(
                        "配置文件 {old} 参数已变更为 {new} 参数，请注意修改配置文件！"
                    ).format(old=old, new=new_),
                )
                data[new_] = data.get(
                    new_,
                    data.get(
                        old,
                        default,
                    ),
                )
        return data

    def compatible(self):
        if (
            old := self.root.parent.joinpath(self.file)
        ).exists() and not self.path.exists():
            move(old, self.path)
```

## File: `src/config/__init__.py`
```python
from .parameter import Parameter
from .settings import Settings

__all__ = ["Parameter", "Settings"]
```

## File: `src/custom/function.py`
```python
from asyncio import sleep
from random import randint
from typing import TYPE_CHECKING
from src.translation import _

if TYPE_CHECKING:
    from src.tools import ColorfulConsole


async def wait() -> None:
    """
    设置网络请求间隔时间，仅对获取数据生效，不影响下载文件
    """
    # 随机延时
    await sleep(randint(5, 20) * 0.1)
    # 固定延时
    # await sleep(1)
    # 取消延时
    # pass


def failure_handling() -> bool:
    """批量下载账号作品模式 和 批量下载合集作品模式 获取数据失败时，是否继续执行"""
    # 询问用户
    # return bool(input(_("输入任意字符继续处理账号/合集，直接回车停止处理账号/合集: ")))
    # 继续执行
    return True
    # 结束执行
    # return False


def condition_filter(data: dict) -> bool:
    """
    自定义作品筛选规则，例如：筛选作品点赞数、作品类型、视频分辨率等
    需要排除的作品返回 False，否则返回 True
    """
    # if data["ratio"] in ("720p", "540p"):
    #     return False  # 过滤低分辨率的视频作品
    return True


async def suspend(count: int, console: "ColorfulConsole") -> None:
    """
    如需采集大量数据，请启用该函数，可以在处理指定数量的数据后，暂停一段时间，然后继续运行
    batches: 每次处理的数据数量上限，比如：每次处理 10 个数据，就会暂停程序
    rest_time: 程序暂停的时间，单位：秒；比如：每处理 10 个数据，就暂停 5 分钟
    仅对 批量下载账号作品模式 和 批量下载合集作品模式 生效
    说明: 此处的一个数据代表一个账号或者一个合集，并非代表一个数据包
    """
    # 启用该函数
    batches = 10  # 根据实际需求修改
    if not count % batches:
        rest_time = 60 * 5  # 根据实际需求修改
        console.print(
            _(
                "程序连续处理了 {batches} 个数据，为了避免请求频率过高导致账号或 IP 被风控，"
                "程序已经暂停运行，将在 {rest_time} 秒后恢复运行！"
            ).format(batches=batches, rest_time=rest_time),
        )
        await sleep(rest_time)
    # 禁用该函数
    # pass


def is_valid_token(token: str) -> bool:
    """Web API 接口模式 和 Web UI 交互模式 token 参数验证"""
    return True
```

## File: `src/custom/internal.py`
```python
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.joinpath("Volume")
PROJECT_ROOT.mkdir(exist_ok=True)
VERSION_MAJOR = 5
VERSION_MINOR = 8
VERSION_BETA = True
__VERSION__ = f"{VERSION_MAJOR}.{VERSION_MINOR}.{'beta' if VERSION_BETA else 'stable'}"
PROJECT_NAME = f"DouK-Downloader V{VERSION_MAJOR}.{VERSION_MINOR} {
    'Beta' if VERSION_BETA else 'Stable'
}"

REPOSITORY = "https://github.com/JoeanAmier/TikTokDownloader"
LICENCE = "GNU General Public License v3.0"
DOCUMENTATION_URL = "https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation"
RELEASES = "https://github.com/JoeanAmier/TikTokDownloader/releases/latest"

DISCLAIMER_TEXT = (
    "关于 DouK-Downloader 的 免责声明：\n"
    "\n"
    "1. 使用者对本项目的使用由使用者自行决定，并自行承担风险。作者对使用者使用本项目所产生的任何损失、责任、或风险概不负责。\n"
    "2. 本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。作者按现有技术水平努力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。\n"
    "3. 本项目依赖的所有第三方库、插件或服务各自遵循其原始开源或商业许可，使用者需自行查阅并遵守相应协议，作者不对第三方组件的稳定性、安全性及合规性承担任何责任。\n"
    "4. 使用者在使用本项目时必须严格遵守 GNU General Public License v3.0 的要求，并在适当的地方注明使用了 GNU General Public License v3.0 的代码。\n"
    "5. 使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。\n"
    "6. 使用者不得使用本工具从事任何侵犯知识产权的行为，包括但不限于未经授权下载、传播受版权保护的内容，开发者不参与、不支持、不认可任何非法内容的获取或分发。\n"
    "7. 本项目不对使用者涉及的数据收集、存储、传输等处理活动的合规性承担责任。使用者应自行遵守相关法律法规，确保处理行为合法正当；因违规操作导致的法律责任由使用者自行承担。\n"
    "8. 使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。\n"
    "9. 本项目的作者不会提供 DouK-Downloader 项目的付费版本，也不会提供与 DouK-Downloader 项目相关的任何商业服务。\n"
    "10. 基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的各种情况负全部责任。\n"
    "11. 本项目不授予使用者任何专利许可；若使用本项目导致专利纠纷或侵权，使用者自行承担全部风险和责任。未经作者或权利人书面授权，不得使用本项目进行任何商业宣传、推广或再授权。\n"
    "12. 作者保留随时终止向任何违反本声明的使用者提供服务的权利，并可能要求其销毁已获取的代码及衍生作品。\n"
    "13. 作者保留在不另行通知的情况下更新本声明的权利，使用者持续使用即视为接受修订后的条款。\n"
    "\n"
    "在使用本项目的代码和功能之前，请您认真考虑并接受以上免责声明。如果您对上述声"
    "明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码"
    "和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险"
    "和后果。\n"
)

RETRY = 5
TIMEOUT = 10

PHONE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
    "CriOS/125.0.6422.51 Mobile/15E148 Safari/604.1",
}
USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
BLANK_HEADERS = {
    "User-Agent": USERAGENT,
}
REFERER = "https://www.douyin.com/?recommend=1"
REFERER_TIKTOK = "https://www.tiktok.com/explore"
PARAMS_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "*/*",
    "Content-Type": "text/plain;charset=UTF-8",
    "Referer": REFERER,
    "User-Agent": USERAGENT,
}
PARAMS_HEADERS_TIKTOK = PARAMS_HEADERS | {
    "Referer": REFERER_TIKTOK,
}
DATA_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "*/*",
    "Referer": REFERER,
    "User-Agent": USERAGENT,
}
DATA_HEADERS_TIKTOK = DATA_HEADERS | {
    "Referer": REFERER_TIKTOK,
}
DOWNLOAD_HEADERS = {
    "Accept": "*/*",
    "Range": "bytes=0-",
    "Referer": REFERER,
    "User-Agent": USERAGENT,
}
DOWNLOAD_HEADERS_TIKTOK = DOWNLOAD_HEADERS | {
    "Referer": REFERER_TIKTOK,
}
QRCODE_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "*/*",
    "Referer": REFERER,
    "User-Agent": USERAGENT,
}

BLANK_PREVIEW = "static/images/blank.png"

VIDEO_INDEX: int = -1
VIDEO_TIKTOK_INDEX: int = 0
IMAGE_INDEX: int = -1
IMAGE_TIKTOK_INDEX: int = -1
VIDEOS_INDEX: int = -1
DYNAMIC_COVER_INDEX: int = -1
STATIC_COVER_INDEX: int = -1
MUSIC_INDEX: int = -1
COMMENT_IMAGE_INDEX: int = -1
COMMENT_STICKER_INDEX: int = -1
LIVE_COVER_INDEX: int = -1
AUTHOR_COVER_INDEX: int = -1
HOT_WORD_COVER_INDEX: int = -1
COMMENT_IMAGE_LIST_INDEX: int = 0
BITRATE_INFO_TIKTOK_INDEX: int = 0
LIVE_DATA_INDEX: int = 0
AVATAR_LARGER_INDEX: int = 0
AUTHOR_COVER_URL_INDEX: int = 0
SEARCH_USER_INDEX: int = 0
SEARCH_AVATAR_INDEX: int = 0
MUSIC_COLLECTION_COVER_INDEX: int = 0
MUSIC_COLLECTION_DOWNLOAD_INDEX: int = 0

if __name__ == "__main__":
    print(__VERSION__)
```

## File: `src/custom/static.py`
```python
# 同时下载作品文件的最大任务数，对直播无效
MAX_WORKERS = 4

# 非法字符替换规则，key 为替换前的文本，value 为替换后的文本
TEXT_REPLACEMENT = {
    " ": " ",
}

# 服务器模式主机，对 Web API 接口模式、Web UI 交互模式 生效，设置为 "127.0.0.1" 代表仅本地可用
SERVER_HOST = "0.0.0.0"

# 服务器模式端口，对 Web API 接口模式、Web UI 交互模式 生效
SERVER_PORT = 5555

# Cookie 更新间隔，单位：秒
COOKIE_UPDATE_INTERVAL = 15 * 60

# 彩色交互提示颜色设置，支持标准颜色名称、Hex、RGB 格式
MASTER = "b #fff200"
PROMPT = "b turquoise2"
GENERAL = "b bright_white"
PROGRESS = "b bright_magenta"
ERROR = "b bright_red"
WARNING = "b bright_yellow"
INFO = "b bright_green"
DEBUG = "b dark_orange"

# 文件类型签名
FILE_SIGNATURES: tuple[
    tuple[
        int,
        bytes,
        str,
    ],
    ...,
] = (
    # 分别为偏移量(字节)、十六进制签名、后缀
    # 参考：https://en.wikipedia.org/wiki/List_of_file_signatures
    # 参考：https://www.garykessler.net/library/file_sigs.html
    (0, b"\xff\xd8\xff", "jpg"),
    (0, b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a", "png"),
    (4, b"\x66\x74\x79\x70\x61\x76\x69\x66", "avif"),
    (4, b"\x66\x74\x79\x70\x68\x65\x69\x63", "heic"),
    (8, b"\x57\x45\x42\x50", "webp"),
    (4, b"\x66\x74\x79\x70\x4d\x53\x4e\x56", "mp4"),
    (4, b"\x66\x74\x79\x70\x69\x73\x6f\x6d", "mp4"),
    (4, b"\x66\x74\x79\x70\x6d\x70\x34\x32", "m4v"),
    (4, b"\x66\x74\x79\x70\x71\x74\x20\x20", "mov"),
    (0, b"\x1a\x45\xdf\xa3", "mkv"),
    (0, b"\x00\x00\x01\xb3", "mpg"),
    (0, b"\x00\x00\x01\xba", "mpg"),
    (0, b"\x46\x4c\x56\x01", "flv"),
    (8, b"\x41\x56\x49\x20", "avi"),
)
FILE_SIGNATURES_LENGTH = max(
    offset + len(signature) for offset, signature, _ in FILE_SIGNATURES
)
```

## File: `src/custom/__init__.py`
```python
from .function import (
    wait,
    failure_handling,
    condition_filter,
    suspend,
    is_valid_token,
)
from .internal import (
    DISCLAIMER_TEXT,
    PROJECT_ROOT,
    VERSION_MAJOR,
    VERSION_MINOR,
    VERSION_BETA,
    RELEASES,
    REPOSITORY,
    LICENCE,
    DOCUMENTATION_URL,
    USERAGENT,
    RETRY,
    BLANK_PREVIEW,
    TIMEOUT,
    PROJECT_NAME,
    DATA_HEADERS,
    PARAMS_HEADERS,
    DOWNLOAD_HEADERS,
    QRCODE_HEADERS,
    DOWNLOAD_HEADERS_TIKTOK,
    PHONE_HEADERS,
    PARAMS_HEADERS_TIKTOK,
    DATA_HEADERS_TIKTOK,
    VIDEO_INDEX,
    VIDEO_TIKTOK_INDEX,
    IMAGE_INDEX,
    IMAGE_TIKTOK_INDEX,
    VIDEOS_INDEX,
    DYNAMIC_COVER_INDEX,
    STATIC_COVER_INDEX,
    MUSIC_INDEX,
    COMMENT_IMAGE_INDEX,
    COMMENT_STICKER_INDEX,
    LIVE_COVER_INDEX,
    AUTHOR_COVER_INDEX,
    HOT_WORD_COVER_INDEX,
    COMMENT_IMAGE_LIST_INDEX,
    BITRATE_INFO_TIKTOK_INDEX,
    LIVE_DATA_INDEX,
    AVATAR_LARGER_INDEX,
    AUTHOR_COVER_URL_INDEX,
    SEARCH_USER_INDEX,
    SEARCH_AVATAR_INDEX,
    MUSIC_COLLECTION_COVER_INDEX,
    MUSIC_COLLECTION_DOWNLOAD_INDEX,
    __VERSION__,
    BLANK_HEADERS,
)
from .static import (
    MAX_WORKERS,
    TEXT_REPLACEMENT,
    SERVER_HOST,
    SERVER_PORT,
    MASTER,
    PROMPT,
    WARNING,
    ERROR,
    INFO,
    GENERAL,
    PROGRESS,
    DEBUG,
    COOKIE_UPDATE_INTERVAL,
    FILE_SIGNATURES,
    FILE_SIGNATURES_LENGTH,
)
```

## File: `src/downloader/download.py`
```python
from asyncio import Semaphore, gather
from datetime import datetime
from pathlib import Path
from shutil import move
from time import time
from types import SimpleNamespace
from typing import TYPE_CHECKING, Callable, Union

from aiofiles import open
from httpx import HTTPStatusError, RequestError, StreamError
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

from ..custom import (
    MAX_WORKERS,
    PROGRESS,
)
from ..tools import (
    CacheError,
    DownloaderError,
    FakeProgress,
    Retry,
    beautify_string,
    format_size,
)
from ..translation import _

if TYPE_CHECKING:
    from httpx import AsyncClient

    from ..config import Parameter

__all__ = ["Downloader"]


class Downloader:
    semaphore = Semaphore(MAX_WORKERS)
    CONTENT_TYPE_MAP = {
        "image/png": "png",
        "image/jpeg": "jpeg",
        "image/webp": "webp",
        "video/mp4": "mp4",
        "video/quicktime": "mov",
        "audio/mp4": "m4a",
        "audio/mpeg": "mp3",
    }

    def __init__(
        self,
        params: "Parameter",
        server_mode: bool = False,
    ):
        self.cleaner = params.CLEANER
        self.client: "AsyncClient" = params.client
        self.client_tiktok: "AsyncClient" = params.client_tiktok
        self.headers = params.headers_download
        self.headers_tiktok = params.headers_download_tiktok
        self.log = params.logger
        self.xb = params.xb
        self.console = params.console
        self.root = params.root
        self.folder_name = params.folder_name
        self.name_format = params.name_format
        self.desc_length = params.desc_length
        self.name_length = params.name_length
        self.split = params.split
        self.folder_mode = params.folder_mode
        self.music = params.music
        self.dynamic_cover = params.dynamic_cover
        self.static_cover = params.static_cover
        # self.cookie = params.cookie
        # self.cookie_tiktok = params.cookie_tiktok
        self.proxy = params.proxy
        self.proxy_tiktok = params.proxy_tiktok
        self.download = params.download
        self.max_size = params.max_size
        self.chunk = params.chunk
        self.max_retry = params.max_retry
        self.recorder = params.recorder
        self.timeout = params.timeout
        self.ffmpeg = params.ffmpeg
        self.cache = params.cache
        self.truncate = params.truncate
        self.general_progress_object: Callable = self.init_general_progress(
            server_mode,
        )

    def init_general_progress(
        self,
        server_mode: bool = False,
    ) -> Callable:
        if server_mode:
            return self.__fake_progress_object
        return self.__general_progress_object

    @staticmethod
    def __fake_progress_object(
        *args,
        **kwargs,
    ):
        return FakeProgress()

    def __general_progress_object(self):
        """文件下载进度条"""
        return Progress(
            TextColumn(
                "[progress.description]{task.description}",
                style=PROGRESS,
                justify="left",
            ),
            SpinnerColumn(),
            BarColumn(bar_width=20),
            "[progress.percentage]{task.percentage:>3.1f}%",
            "•",
            DownloadColumn(binary_units=True),
            "•",
            TimeRemainingColumn(),
            console=self.console,
            transient=True,
            expand=True,
        )

    def __live_progress_object(self):
        """直播下载进度条"""
        return Progress(
            TextColumn(
                "[progress.description]{task.description}",
                style=PROGRESS,
                justify="left",
            ),
            SpinnerColumn(),
            BarColumn(bar_width=20),
            "•",
            TransferSpeedColumn(),
            "•",
            TimeElapsedColumn(),
            console=self.console,
            transient=True,
            expand=True,
        )

    async def run(
        self,
        data: Union[list[dict], list[tuple]],
        type_: str,
        tiktok=False,
        **kwargs,
    ) -> None:
        if not self.download or not data:
            return
        self.log.info(_("开始下载作品文件"))
        match type_:
            case "batch":
                await self.run_batch(data, tiktok, **kwargs)
            case "detail":
                await self.run_general(data, tiktok, **kwargs)
            case "music":
                await self.run_music(data, **kwargs)
            case "live":
                await self.run_live(data, tiktok, **kwargs)
            case _:
                raise ValueError

    async def run_batch(
        self,
        data: list[dict],
        tiktok: bool,
        mode: str = "",
        mark: str = "",
        user_id: str = "",
        user_name: str = "",
        mix_id: str = "",
        mix_title: str = "",
        collect_id: str = "",
        collect_name: str = "",
    ):
        root = self.storage_folder(
            mode,
            *self.data_classification(
                mode,
                mark,
                user_id,
                user_name,
                mix_id,
                mix_title,
                collect_id,
                collect_name,
            ),
        )
        await self.batch_processing(
            data,
            root,
            tiktok=tiktok,
        )

    async def run_general(self, data: list[dict], tiktok: bool, **kwargs):
        root = self.storage_folder(mode="detail")
        await self.batch_processing(
            data,
            root,
            tiktok=tiktok,
        )

    async def run_music(
        self,
        data: list[dict],
        **kwargs,
    ):
        root = self.root.joinpath("Music")
        tasks = []
        for i in data:
            name = self.generate_music_name(i)
            temp_root, actual_root = self.deal_folder_path(
                root,
                name,
                False,
            )
            self.download_music(
                tasks,
                name,
                i["id"],
                i,
                temp_root,
                actual_root,
                "download",
                True,
                type_=_("音乐"),
            )
        await self.downloader_chart(
            tasks, SimpleNamespace(), self.general_progress_object(), **kwargs
        )

    async def run_live(
        self,
        data: list[tuple],
        tiktok=False,
        **kwargs,
    ):
        if not data or not self.download:
            return
        download_command = []
        self.generate_live_commands(
            data,
            download_command,
        )
        self.console.info(
            _("程序将会调用 ffmpeg 下载直播，关闭 DouK-Downloader 不会中断下载！"),
        )
        self.__download_live(download_command, tiktok)

    def generate_live_commands(
        self,
        data: list[tuple],
        commands: list,
        suffix: str = "mp4",
    ):
        root = self.root.joinpath("Live")
        root.mkdir(exist_ok=True)
        for i, f, m in data:
            name = self.cleaner.filter_name(
                f"{i['title']}{self.split}{i['nickname']}{self.split}{datetime.now():%Y-%m-%d %H.%M.%S}.{suffix}",
                f"{int(time())}{self.split}{datetime.now():%Y-%m-%d %H.%M.%S}.{suffix}",
            )
            path = root.joinpath(name)
            commands.append(
                (
                    m,
                    str(path.resolve()),
                )
            )

    def __download_live(
        self,
        commands: list,
        tiktok: bool,
    ):
        self.ffmpeg.download(
            commands,
            self.proxy_tiktok if tiktok else self.proxy,
            self.headers["User-Agent"],
        )

    async def batch_processing(self, data: list[dict], root: Path, **kwargs):
        count = SimpleNamespace(
            downloaded_image=set(),
            skipped_image=set(),
            downloaded_video=set(),
            skipped_video=set(),
            downloaded_live=set(),
            skipped_live=set(),
        )
        tasks = []
        for item in data:
            item["desc"] = beautify_string(
                item["desc"],
                self.desc_length,
            )
            name = self.generate_detail_name(item)
            temp_root, actual_root = self.deal_folder_path(
                root,
                name,
                self.folder_mode,
            )
            params = {
                "tasks": tasks,
                "name": name,
                "id_": item["id"],
                "item": item,
                "temp_root": temp_root,
                "actual_root": actual_root,
            }
            if (t := item["type"]) == _("图集"):
                await self.download_image(
                    **params,
                    type_=_("图集"),
                    skipped=count.skipped_image,
                )
            elif t == _("视频"):
                await self.download_video(
                    **params,
                    type_=_("视频"),
                    skipped=count.skipped_video,
                )
            elif t == _("实况"):
                await self.download_image(
                    suffix="mp4",
                    type_=_("实况"),
                    **params,
                    skipped=count.skipped_live,
                )
            else:
                raise DownloaderError
            self.download_music(
                **params,
                type=_("音乐"),
            )
            self.download_cover(**params)
        await self.downloader_chart(
            tasks, count, self.general_progress_object(), **kwargs
        )
        self.statistics_count(count)

    async def downloader_chart(
        self,
        tasks: list[tuple],
        count: SimpleNamespace,
        progress: Progress,
        semaphore: Semaphore = None,
        **kwargs,
    ):
        with progress:
            tasks = [
                self.request_file(
                    *task,
                    count=count,
                    **kwargs,
                    progress=progress,
                    semaphore=semaphore,
                )
                for task in tasks
            ]
            await gather(*tasks)

    def deal_folder_path(
        self,
        root: Path,
        name: str,
        folder_mode=False,
    ) -> tuple[Path, Path]:
        """生成文件的临时路径和目标路径"""
        root = self.create_detail_folder(root, name, folder_mode)
        root.mkdir(exist_ok=True)
        cache = self.cache.joinpath(name)
        actual = root.joinpath(name)
        return cache, actual

    async def is_downloaded(self, id_: str) -> bool:
        return await self.recorder.has_id(id_)

    @staticmethod
    def is_exists(path: Path) -> bool:
        return path.exists()

    async def is_skip(self, id_: str, path: Path) -> bool:
        return await self.is_downloaded(id_) or self.is_exists(path)

    async def download_image(
        self,
        tasks: list,
        name: str,
        id_: str,
        item: SimpleNamespace,
        skipped: set,
        temp_root: Path,
        actual_root: Path,
        suffix: str = "jpeg",
        type_: str = _("图集"),
    ) -> None:
        if not item["downloads"]:
            self.log.error(
                _("【{type}】{name} 提取文件下载地址失败，跳过下载").format(
                    type=type_, name=name
                )
            )
            return
        for index, img in enumerate(
            item["downloads"],
            start=1,
        ):
            if await self.is_downloaded(id_):
                skipped.add(id_)
                self.log.info(
                    _("【{type}】{name} 存在下载记录，跳过下载").format(
                        type=type_, name=name
                    )
                )
                break
            elif self.is_exists(p := actual_root.with_name(f"{name}_{index}.{suffix}")):
                self.log.info(
                    _("【{type}】{name}_{index} 文件已存在，跳过下载").format(
                        type=type_, name=name, index=index
                    )
                )
                self.log.info(f"文件路径: {p.resolve()}", False)
                skipped.add(id_)
                continue
            tasks.append(
                (
                    img,
                    temp_root.with_name(f"{name}_{index}.{suffix}"),
                    p,
                    f"【{type_}】{name}_{index}",
                    id_,
                    suffix,
                )
            )

    async def download_video(
        self,
        tasks: list,
        name: str,
        id_: str,
        item: SimpleNamespace,
        skipped: set,
        temp_root: Path,
        actual_root: Path,
        suffix: str = "mp4",
        type_: str = _("视频"),
    ) -> None:
        if not item["downloads"]:
            self.log.error(
                _("【{type}】{name} 提取文件下载地址失败，跳过下载").format(
                    type=type_, name=name
                )
            )
            return
        if await self.is_skip(
            id_,
            p := actual_root.with_name(
                f"{name}.{suffix}",
            ),
        ):
            self.log.info(
                _("【{type}】{name} 存在下载记录或文件已存在，跳过下载").format(
                    type=type_, name=name
                )
            )
            self.log.info(f"文件路径: {p.resolve()}", False)
            skipped.add(id_)
            return
        tasks.append(
            (
                item["downloads"],
                temp_root.with_name(f"{name}.{suffix}"),
                p,
                f"【{type_}】{name}",
                id_,
                suffix,
            )
        )

    def download_music(
        self,
        tasks: list,
        name: str,
        id_: str,
        item: dict,
        temp_root: Path,
        actual_root: Path,
        key: str = "music_url",
        switch: bool = False,
        suffix: str = "mp3",
        type_: str = _("音乐"),
        **kwargs,
    ) -> None:
        if self.check_deal_music(
            url := item[key],
            p := actual_root.with_name(f"{name}.{suffix}"),
            switch,
        ):
            tasks.append(
                (
                    url,
                    temp_root.with_name(f"{name}.{suffix}"),
                    p,
                    _("【{type}】{name}").format(
                        type=type_,
                        name=name,
                    ),
                    id_,
                    suffix,
                )
            )

    def download_cover(
        self,
        tasks: list,
        name: str,
        id_: str,
        item: SimpleNamespace,
        temp_root: Path,
        actual_root: Path,
        static_suffix: str = "jpeg",
        dynamic_suffix: str = "webp",
        **kwargs,
    ) -> None:
        if all(
            (
                self.static_cover,
                url := item["static_cover"],
                not self.is_exists(
                    p := actual_root.with_name(f"{name}.{static_suffix}")
                ),
            )
        ):
            tasks.append(
                (
                    url,
                    temp_root.with_name(f"{name}.{static_suffix}"),
                    p,
                    f"【封面】{name}",
                    id_,
                    static_suffix,
                )
            )
        if all(
            (
                self.dynamic_cover,
                url := item["dynamic_cover"],
                not self.is_exists(
                    p := actual_root.with_name(f"{name}.{dynamic_suffix}")
                ),
            )
        ):
            tasks.append(
                (
                    url,
                    temp_root.with_name(f"{name}.{dynamic_suffix}"),
                    p,
                    f"【动图】{name}",
                    id_,
                    dynamic_suffix,
                )
            )

    def check_deal_music(
        self,
        url: str,
        path: Path,
        switch=False,
    ) -> bool:
        """未传入 switch 参数则判断音乐下载开关设置"""
        return all((switch or self.music, url, not self.is_exists(path)))

    @Retry.retry
    async def request_file(
        self,
        url: str,
        temp: Path,
        actual: Path,
        show: str,
        id_: str,
        suffix: str,
        count: SimpleNamespace,
        progress: Progress,
        headers: dict = None,
        tiktok=False,
        unknown_size=False,
        semaphore: Semaphore = None,
    ) -> bool | None:
        async with semaphore or self.semaphore:
            client = self.client_tiktok if tiktok else self.client
            headers = self.__adapter_headers(
                headers,
                tiktok,
            )
            self.__record_request_messages(
                show,
                url,
                headers,
            )
            try:
                # length, suffix = await self.__head_file(client, url, headers, suffix, )
                position = self.__update_headers_range(
                    headers,
                    temp,
                )
                async with client.stream(
                    "GET",
                    url,
                    headers=headers,
                ) as response:
                    if response.status_code == 416:
                        raise CacheError(_("文件缓存异常，尝试重新下载"))
                    response.raise_for_status()
                    length, suffix = self._extract_content(
                        response.headers,
                        suffix,
                    )
                    length += position
                    self._record_response(
                        response,
                        show,
                        length,
                    )
                    match self._download_initial_check(
                        length,
                        unknown_size,
                        show,
                    ):
                        case 1:
                            return await self.download_file(
                                temp,
                                actual.with_suffix(
                                    f".{suffix}",
                                ),
                                show,
                                id_,
                                response,
                                length,
                                position,
                                count,
                                progress,
                            )
                        case 0:
                            return True
                        case -1:
                            return False
                        case _:
                            raise DownloaderError
            except RequestError as e:
                self.log.warning(_("网络异常: {error_repr}").format(error_repr=repr(e)))
                return False
            except HTTPStatusError as e:
                self.log.warning(
                    _("响应码异常: {error_repr}").format(error_repr=repr(e))
                )
                self.console.warning(
                    _(
                        "如果 TikTok 平台作品下载功能异常，请检查配置文件中 browser_info_tiktok 的 device_id 参数！"
                    ),
                )
                return False
            except CacheError as e:
                self.delete(temp)
                self.log.error(str(e))
                return False
            except Exception as e:
                self.log.error(
                    _(
                        "下载文件时发生预期之外的错误，请向作者反馈，错误信息: {error}"
                    ).format(error=repr(e)),
                )
                self.log.error(f"URL: {url}", False)
                self.log.error(f"Headers: {headers}", False)
                return False

    async def download_file(
        self,
        cache: Path,
        actual: Path,
        show: str,
        id_: str,
        response,
        content: int,
        position: int,
        count: SimpleNamespace,
        progress: Progress,
    ) -> bool:
        task_id = progress.add_task(
            beautify_string(show, self.truncate),
            total=content or None,
            completed=position,
        )
        try:
            async with open(cache, "ab") as f:
                async for chunk in response.aiter_bytes(self.chunk):
                    await f.write(chunk)
                    progress.update(task_id, advance=len(chunk))
                progress.remove_task(task_id)
        except (
            RequestError,
            StreamError,
        ) as e:
            progress.remove_task(task_id)
            self.log.warning(
                _("{show} 下载中断，错误信息：{error}").format(show=show, error=e)
            )
            # self.delete_file(cache)
            await self.recorder.delete_id(id_)
            return False
        self.save_file(cache, actual)
        self.log.info(_("{show} 文件下载成功").format(show=show))
        self.log.info(f"文件路径 {actual.resolve()}", False)
        await self.recorder.update_id(id_)
        self.add_count(show, id_, count)
        return True

    def __record_request_messages(
        self,
        show: str,
        url: str,
        headers: dict,
    ):
        self.log.info(f"{show} URL: {url}", False)
        # 请求头脱敏处理，不记录 Cookie
        desensitize = {k: v for k, v in headers.items() if k != "Cookie"}
        self.log.info(f"{show} Headers: {desensitize}", False)

    def __adapter_headers(
        self,
        headers: dict,
        tiktok: bool,
        *args,
        **kwargs,
    ) -> dict:
        return (headers or self.headers_tiktok if tiktok else self.headers).copy()

    @staticmethod
    def add_count(show: str, id_: str, count: SimpleNamespace):
        if show.startswith(f"【{_('图集')}】"):
            count.downloaded_image.add(id_)
        elif show.startswith(f"【{_('视频')}】"):
            count.downloaded_video.add(id_)
        elif show.startswith(f"【{_('实况')}】"):
            count.downloaded_live.add(id_)

    @staticmethod
    def data_classification(
        mode: str = "",
        mark: str = "",
        user_id: str = "",
        user_name: str = "",
        mix_id: str = "",
        mix_title: str = "",
        collect_id: str = "",
        collect_name: str = "",
    ) -> tuple[str, str]:
        match mode:
            case "post" | "favorite" | "collection":
                return user_id, mark or user_name
            case "mix":
                return mix_id, mark or mix_title
            case "collects":
                return collect_id, mark or collect_name
            case _:
                raise DownloaderError

    def storage_folder(
        self,
        mode: str = "",
        id_: str = "",
        name: str = "",
    ) -> Path:
        match mode:
            case "post":
                folder_name = _("UID{id_}_{name}_发布作品").format(id_=id_, name=name)
            case "favorite":
                folder_name = _("UID{id_}_{name}_喜欢作品").format(id_=id_, name=name)
            case "mix":
                folder_name = _("MID{id_}_{name}_合集作品").format(id_=id_, name=name)
            case "collection":
                folder_name = _("UID{id_}_{name}_收藏作品").format(id_=id_, name=name)
            case "collects":
                folder_name = _("CID{id_}_{name}_收藏夹作品").format(id_=id_, name=name)
            case "detail":
                folder_name = self.folder_name
            case _:
                raise DownloaderError
        folder = self.root.joinpath(folder_name)
        folder.mkdir(exist_ok=True)
        return folder

    def generate_detail_name(self, data: dict) -> str:
        """生成作品文件名称"""
        return beautify_string(
            self.cleaner.filter_name(
                self.split.join(data[i] for i in self.name_format),
                data["id"],
            ),
            length=self.name_length,
        )

    def generate_music_name(self, data: dict) -> str:
        """生成音乐文件名称"""
        return beautify_string(
            self.cleaner.filter_name(
                self.split.join(
                    data[i]
                    for i in (
                        "author",
                        "title",
                        "id",
                    )
                ),
                default=str(time())[:10],
            ),
            length=self.name_length,
        )

    @staticmethod
    def create_detail_folder(
        root: Path,
        name: str,
        folder_mode=False,
    ) -> Path:
        return root.joinpath(name) if folder_mode else root

    @staticmethod
    def delete(
        temp: "Path",
    ):
        if temp.is_file():
            temp.unlink()

    @staticmethod
    def save_file(cache: Path, actual: Path):
        move(cache.resolve(), actual.resolve())

    def delete_file(self, path: Path):
        path.unlink()
        self.log.info(_("{file_name} 文件已删除").format(file_name=path.name))

    def statistics_count(self, count: SimpleNamespace):
        self.log.info(
            _("下载视频作品 {downloaded_video_count} 个").format(
                downloaded_video_count=len(count.downloaded_video)
            ),
        )
        self.log.info(
            _("跳过视频作品 {skipped_count} 个").format(
                skipped_count=len(count.skipped_video)
            )
        )
        self.log.info(
            _("下载图集作品 {downloaded_image_count} 个").format(
                downloaded_image_count=len(count.downloaded_image)
            ),
        )
        self.log.info(
            _("跳过图集作品 {skipped_count} 个").format(
                skipped_count=len(count.skipped_image)
            )
        )
        self.log.info(
            _("下载实况作品 {downloaded_image_count} 个").format(
                downloaded_image_count=len(count.downloaded_live)
            ),
        )
        self.log.info(
            _("跳过实况作品 {skipped_count} 个").format(
                skipped_count=len(count.skipped_live)
            )
        )

    def _record_response(
        self,
        response,
        show: str,
        length: int,
    ):
        self.log.info(f"{show} Response URL: {response.url}", False)
        self.log.info(f"{show} Response Code: {response.status_code}", False)
        self.log.info(f"{show} Response Headers: {response.headers}", False)
        self.log.info(
            f"{show} 文件大小 {format_size(length)}",
            False,
        )

    async def __head_file(
        self,
        client: "AsyncClient",
        url: str,
        headers: dict,
        suffix: str,
    ) -> tuple[int, str]:
        response = await client.head(
            url,
            headers=headers,
        )
        if response.status_code == 405:
            return 0, suffix
        response.raise_for_status()
        return self._extract_content(
            response.headers,
            suffix,
        )

    def _extract_content(
        self,
        headers: dict,
        suffix: str,
    ) -> tuple[int, str]:
        suffix = (
            self.__extract_type(
                headers.get("Content-Type"),
            )
            or suffix
        )
        length = headers.get(
            "Content-Length",
            0,
        )
        return int(length), suffix

    @staticmethod
    def __get_resume_byte_position(file: Path) -> int:
        return file.stat().st_size if file.is_file() else 0

    def __update_headers_range(
        self,
        headers: dict,
        file: Path,
        length: int = 0,
    ) -> int:
        position = self.__get_resume_byte_position(file)
        # if length and position >= length:
        #     self.delete(file)
        #     position = 0
        headers["Range"] = f"bytes={position}-"
        return position

    def __extract_type(self, content: str) -> str:
        if not (s := self.CONTENT_TYPE_MAP.get(content)):
            return self.__unknown_type(content)
        return s

    def __unknown_type(self, content: str) -> str:
        self.log.warning(_("未收录的文件类型：{content}").format(content=content))
        return ""

    def _download_initial_check(
        self,
        length: int,
        unknown_size: bool,
        show: str,
    ) -> int:
        if not length and not unknown_size:  # 响应内容大小判断
            self.log.warning(_("{show} 响应内容为空").format(show=show))
            return -1  # 执行重试
        if all(
            (
                self.max_size,
                length,
                length > self.max_size,
            )
        ):  # 文件下载跳过判断
            self.log.info(_("{show} 文件大小超出限制，跳过下载").format(show=show))
            return 0  # 跳过下载
        return 1  # 继续下载
```

## File: `src/downloader/__init__.py`
```python
from .download import Downloader

__all__ = ["Downloader"]
```

## File: `src/encrypt/aBogus.py`
```python
from random import choice, randint, random
from re import compile
from time import time
from urllib.parse import quote, urlencode

from gmssl import func, sm3

from src.custom import USERAGENT

__all__ = [
    "ABogus",
]


class ABogus:
    __filter = compile(r"%([0-9A-F]{2})")
    __arguments = [0, 1, 14]
    __ua_key = "\u0000\u0001\u000e"
    __end_string = "cus"
    __version = [1, 0, 1, 5]
    __browser = "1536|742|1536|864|0|0|0|0|1536|864|1536|864|1536|742|24|24|Win32"
    __reg = [
        1937774191,
        1226093241,
        388252375,
        3666478592,
        2842636476,
        372324522,
        3817729613,
        2969243214,
    ]
    __str = {
        "s0": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
        "s1": "Dkdpgh4ZKsQB80/Mfvw36XI1R25+WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe=",
        "s2": "Dkdpgh4ZKsQB80/Mfvw36XI1R25-WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe=",
        "s3": "ckdp1h4ZKsUB80/Mfvw36XIgR25+WQAlEi7NLboqYTOPuzmFjJnryx9HVGDaStCe",
        "s4": "Dkdpgh2ZmsQB80/MfvV36XI1R45-WUAlEixNLwoqYTOPuzKFjJnry79HbGcaStCe",
    }

    def __init__(
        self,
        user_agent: str = USERAGENT,
        platform: str = None,
    ):
        self.chunk = []
        self.size = 0
        self.reg = self.__reg[:]
        self.ua_code = self.generate_ua_code(user_agent)
        self.browser = (
            self.generate_browser_info(platform) if platform else self.__browser
        )
        self.browser_len = len(self.browser)
        self.browser_code = self.char_code_at(self.browser)

    @classmethod
    def list_1(
        cls,
        random_num=None,
        a=170,
        b=85,
        c=45,
    ) -> list:
        return cls.random_list(
            random_num,
            a,
            b,
            1,
            2,
            5,
            c & a,
        )

    @classmethod
    def list_2(
        cls,
        random_num=None,
        a=170,
        b=85,
    ) -> list:
        return cls.random_list(
            random_num,
            a,
            b,
            1,
            0,
            0,
            0,
        )

    @classmethod
    def list_3(
        cls,
        random_num=None,
        a=170,
        b=85,
    ) -> list:
        return cls.random_list(
            random_num,
            a,
            b,
            1,
            0,
            5,
            0,
        )

    @staticmethod
    def random_list(
        a: float = None,
        b=170,
        c=85,
        d=0,
        e=0,
        f=0,
        g=0,
    ) -> list:
        r = a or (random() * 10000)
        v = [
            r,
            int(r) & 255,
            int(r) >> 8,
        ]
        s = v[1] & b | d
        v.append(s)
        s = v[1] & c | e
        v.append(s)
        s = v[2] & b | f
        v.append(s)
        s = v[2] & c | g
        v.append(s)
        return v[-4:]

    @staticmethod
    def from_char_code(*args):
        return "".join(chr(code) for code in args)

    @classmethod
    def generate_string_1(
        cls,
        random_num_1=None,
        random_num_2=None,
        random_num_3=None,
    ):
        return (
            cls.from_char_code(*cls.list_1(random_num_1))
            + cls.from_char_code(*cls.list_2(random_num_2))
            + cls.from_char_code(*cls.list_3(random_num_3))
        )

    def generate_string_2(
        self,
        url_params: str,
        method="GET",
        start_time=0,
        end_time=0,
    ) -> str:
        a = self.generate_string_2_list(
            url_params,
            method,
            start_time,
            end_time,
        )
        e = self.end_check_num(a)
        a.extend(self.browser_code)
        a.append(e)
        return self.rc4_encrypt(self.from_char_code(*a), "y")

    def generate_ua_code(self, user_agent: str) -> list[int]:
        u = self.rc4_encrypt(user_agent, self.__ua_key)
        u = self.generate_result(u, "s3")
        return self.sum(u)

    def generate_string_2_list(
        self,
        url_params: str,
        method="GET",
        start_time=0,
        end_time=0,
    ) -> list:
        start_time = start_time or int(time() * 1000)
        end_time = end_time or (start_time + randint(4, 8))
        params_array = self.generate_params_code(url_params)
        method_array = self.generate_method_code(method)
        return self.list_4(
            (end_time >> 24) & 255,
            params_array[21],
            self.ua_code[23],
            (end_time >> 16) & 255,
            params_array[22],
            self.ua_code[24],
            (end_time >> 8) & 255,
            (end_time >> 0) & 255,
            (start_time >> 24) & 255,
            (start_time >> 16) & 255,
            (start_time >> 8) & 255,
            (start_time >> 0) & 255,
            method_array[21],
            method_array[22],
            int(end_time / 256 / 256 / 256 / 256) >> 0,
            int(start_time / 256 / 256 / 256 / 256) >> 0,
            self.browser_len,
        )

    @staticmethod
    def reg_to_array(a):
        o = [0] * 32
        for i in range(8):
            c = a[i]
            o[4 * i + 3] = 255 & c
            c >>= 8
            o[4 * i + 2] = 255 & c
            c >>= 8
            o[4 * i + 1] = 255 & c
            c >>= 8
            o[4 * i] = 255 & c

        return o

    def compress(self, a):
        f = self.generate_f(a)
        i = self.reg[:]
        for o in range(64):
            c = self.de(i[0], 12) + i[4] + self.de(self.pe(o), o)
            c = c & 0xFFFFFFFF
            c = self.de(c, 7)
            s = (c ^ self.de(i[0], 12)) & 0xFFFFFFFF

            u = self.he(o, i[0], i[1], i[2])
            u = (u + i[3] + s + f[o + 68]) & 0xFFFFFFFF

            b = self.ve(o, i[4], i[5], i[6])
            b = (b + i[7] + c + f[o]) & 0xFFFFFFFF

            i[3] = i[2]
            i[2] = self.de(i[1], 9)
            i[1] = i[0]
            i[0] = u

            i[7] = i[6]
            i[6] = self.de(i[5], 19)
            i[5] = i[4]
            i[4] = (b ^ self.de(b, 9) ^ self.de(b, 17)) & 0xFFFFFFFF

        for l in range(8):
            self.reg[l] = (self.reg[l] ^ i[l]) & 0xFFFFFFFF

    @classmethod
    def generate_f(cls, e):
        r = [0] * 132

        for t in range(16):
            r[t] = (
                (e[4 * t] << 24)
                | (e[4 * t + 1] << 16)
                | (e[4 * t + 2] << 8)
                | e[4 * t + 3]
            )
            r[t] &= 0xFFFFFFFF

        for n in range(16, 68):
            a = r[n - 16] ^ r[n - 9] ^ cls.de(r[n - 3], 15)
            a = a ^ cls.de(a, 15) ^ cls.de(a, 23)
            r[n] = (a ^ cls.de(r[n - 13], 7) ^ r[n - 6]) & 0xFFFFFFFF

        for n in range(68, 132):
            r[n] = (r[n - 68] ^ r[n - 64]) & 0xFFFFFFFF

        return r

    @staticmethod
    def pad_array(arr, length=60):
        while len(arr) < length:
            arr.append(0)
        return arr

    def fill(self, length=60):
        size = 8 * self.size
        self.chunk.append(128)
        self.chunk = self.pad_array(self.chunk, length)
        for i in range(4):
            self.chunk.append((size >> 8 * (3 - i)) & 255)

    @staticmethod
    def list_4(
        a: int,
        b: int,
        c: int,
        d: int,
        e: int,
        f: int,
        g: int,
        h: int,
        i: int,
        j: int,
        k: int,
        m: int,
        n: int,
        o: int,
        p: int,
        q: int,
        r: int,
    ) -> list:
        return [
            44,
            a,
            0,
            0,
            0,
            0,
            24,
            b,
            n,
            0,
            c,
            d,
            0,
            0,
            0,
            1,
            0,
            239,
            e,
            o,
            f,
            g,
            0,
            0,
            0,
            0,
            h,
            0,
            0,
            14,
            i,
            j,
            0,
            k,
            m,
            3,
            p,
            1,
            q,
            1,
            r,
            0,
            0,
            0,
        ]

    @staticmethod
    def end_check_num(a: list):
        r = 0
        for i in a:
            r ^= i
        return r

    @classmethod
    def decode_string(
        cls,
        url_string,
    ):
        decoded = cls.__filter.sub(cls.replace_func, url_string)
        return decoded

    @staticmethod
    def replace_func(match):
        return chr(int(match.group(1), 16))

    @staticmethod
    def de(e, r):
        r %= 32
        return ((e << r) & 0xFFFFFFFF) | (e >> (32 - r))

    @staticmethod
    def pe(e):
        return 2043430169 if 0 <= e < 16 else 2055708042

    @staticmethod
    def he(e, r, t, n):
        if 0 <= e < 16:
            return (r ^ t ^ n) & 0xFFFFFFFF
        elif 16 <= e < 64:
            return (r & t | r & n | t & n) & 0xFFFFFFFF
        raise ValueError

    @staticmethod
    def ve(e, r, t, n):
        if 0 <= e < 16:
            return (r ^ t ^ n) & 0xFFFFFFFF
        elif 16 <= e < 64:
            return (r & t | ~r & n) & 0xFFFFFFFF
        raise ValueError

    @staticmethod
    def convert_to_char_code(a):
        d = []
        for i in a:
            d.append(ord(i))
        return d

    @staticmethod
    def split_array(arr, chunk_size=64):
        result = []
        for i in range(0, len(arr), chunk_size):
            result.append(arr[i : i + chunk_size])
        return result

    @staticmethod
    def char_code_at(s):
        return [ord(char) for char in s]

    def write(
        self,
        e,
    ):
        self.size = len(e)
        if isinstance(e, str):
            e = self.decode_string(e)
            e = self.char_code_at(e)
        if len(e) <= 64:
            self.chunk = e
        else:
            chunks = self.split_array(e, 64)
            for i in chunks[:-1]:
                self.compress(i)
            self.chunk = chunks[-1]

    def reset(
        self,
    ):
        self.chunk = []
        self.size = 0
        self.reg = self.__reg[:]

    def sum(self, e, length=60):
        self.reset()
        self.write(e)
        self.fill(length)
        self.compress(self.chunk)
        return self.reg_to_array(self.reg)

    @classmethod
    def generate_result_unit(cls, n, s):
        r = ""
        for i, j in zip(range(18, -1, -6), (16515072, 258048, 4032, 63)):
            r += cls.__str[s][(n & j) >> i]
        return r

    @classmethod
    def generate_result_end(cls, s, e="s4"):
        r = ""
        b = ord(s[120]) << 16
        r += cls.__str[e][(b & 16515072) >> 18]
        r += cls.__str[e][(b & 258048) >> 12]
        r += "=="
        return r

    @classmethod
    def generate_result(cls, s, e="s4"):
        # r = ""
        # for i in range(len(s)//4):
        #     b = ((ord(s[i * 3]) << 16) | (ord(s[i * 3 + 1]))
        #          << 8) | ord(s[i * 3 + 2])
        #     r += cls.generate_result_unit(b, e)
        # return r

        r = []

        for i in range(0, len(s), 3):
            if i + 2 < len(s):
                n = (ord(s[i]) << 16) | (ord(s[i + 1]) << 8) | ord(s[i + 2])
            elif i + 1 < len(s):
                n = (ord(s[i]) << 16) | (ord(s[i + 1]) << 8)
            else:
                n = ord(s[i]) << 16

            for j, k in zip(range(18, -1, -6), (0xFC0000, 0x03F000, 0x0FC0, 0x3F)):
                if j == 6 and i + 1 >= len(s):
                    break
                if j == 0 and i + 2 >= len(s):
                    break
                r.append(cls.__str[e][(n & k) >> j])

        r.append("=" * ((4 - len(r) % 4) % 4))
        return "".join(r)

    @classmethod
    def generate_args_code(cls):
        a = []
        for j in range(24, -1, -8):
            a.append(cls.__arguments[0] >> j)
        a.append(cls.__arguments[1] / 256)
        a.append(cls.__arguments[1] % 256)
        a.append(cls.__arguments[1] >> 24)
        a.append(cls.__arguments[1] >> 16)
        for j in range(24, -1, -8):
            a.append(cls.__arguments[2] >> j)
        return [int(i) & 255 for i in a]

    def generate_method_code(self, method: str = "GET") -> list[int]:
        return self.sm3_to_array(self.sm3_to_array(method + self.__end_string))
        # return self.sum(self.sum(method + self.__end_string))

    def generate_params_code(self, params: str) -> list[int]:
        return self.sm3_to_array(self.sm3_to_array(params + self.__end_string))
        # return self.sum(self.sum(params + self.__end_string))

    @classmethod
    def sm3_to_array(cls, data: str | list) -> list[int]:
        """
        代码参考: https://github.com/Johnserf-Seed/f2/blob/main/f2/utils/abogus.py

        计算请求体的 SM3 哈希值，并将结果转换为整数数组
        Calculate the SM3 hash value of the request body and convert the result to an array of integers

        Args:
            data (Union[str, List[int]]): 输入数据 (Input data).

        Returns:
            List[int]: 哈希值的整数数组 (Array of integers representing the hash value).
        """

        if isinstance(data, str):
            b = data.encode("utf-8")
        else:
            b = bytes(data)  # 将 List[int] 转换为字节数组

        # 将字节数组转换为适合 sm3.sm3_hash 函数处理的列表格式
        h = sm3.sm3_hash(func.bytes_to_list(b))

        # 将十六进制字符串结果转换为十进制整数列表
        return [int(h[i : i + 2], 16) for i in range(0, len(h), 2)]

    @classmethod
    def generate_browser_info(cls, platform: str = "Win32") -> str:
        inner_width = randint(1280, 1920)
        inner_height = randint(720, 1080)
        outer_width = randint(inner_width, 1920)
        outer_height = randint(inner_height, 1080)
        screen_x = 0
        screen_y = choice((0, 30))
        value_list = [
            inner_width,
            inner_height,
            outer_width,
            outer_height,
            screen_x,
            screen_y,
            0,
            0,
            outer_width,
            outer_height,
            outer_width,
            outer_height,
            inner_width,
            inner_height,
            24,
            24,
            platform,
        ]
        return "|".join(str(i) for i in value_list)

    @staticmethod
    def rc4_encrypt(plaintext, key):
        s = list(range(256))
        j = 0

        for i in range(256):
            j = (j + s[i] + ord(key[i % len(key)])) % 256
            s[i], s[j] = s[j], s[i]

        i = 0
        j = 0
        cipher = []

        for k in range(len(plaintext)):
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            s[i], s[j] = s[j], s[i]
            t = (s[i] + s[j]) % 256
            cipher.append(chr(s[t] ^ ord(plaintext[k])))

        return "".join(cipher)

    def get_value(
        self,
        url_params: dict | str,
        method="GET",
        start_time=0,
        end_time=0,
        random_num_1=None,
        random_num_2=None,
        random_num_3=None,
    ) -> str:
        string_1 = self.generate_string_1(
            random_num_1,
            random_num_2,
            random_num_3,
        )
        string_2 = self.generate_string_2(
            urlencode(
                url_params,
                quote_via=quote,
            )
            if isinstance(url_params, dict)
            else url_params,
            method,
            start_time,
            end_time,
        )
        string = string_1 + string_2
        # return self.generate_result(
        #     string, "s4") + self.generate_result_end(string, "s4")
        return self.generate_result(string, "s4")
```

## File: `src/encrypt/device_id.py`
```python
from asyncio import run
from re import compile
from typing import TYPE_CHECKING, Union

from src.custom import PARAMS_HEADERS_TIKTOK
from src.tools import request_params

if TYPE_CHECKING:
    from src.record import BaseLogger, LoggerManager
    from src.testers import Logger


class DeviceId:
    NAME = "device_id"
    URL = "https://www.tiktok.com/explore"
    DEVICE_ID = compile(r'"wid":"(\d{19})"')

    @classmethod
    async def get_device_id(
        cls,
        logger: Union["BaseLogger", "LoggerManager", "Logger"],
        headers: dict,
        **kwargs,
    ) -> [str, str]:
        response = await request_params(
            logger,
            cls.URL,
            "GET",
            headers=headers,
            resp="response",
            **kwargs,
        )
        response.raise_for_status()
        device_id = d.group(1) if (d := cls.DEVICE_ID.search(response.text)) else ""
        cookie = "; ".join(
            [f"{key}={value}" for key, value in response.cookies.items()]
        )
        return device_id, cookie

    @classmethod
    async def get_device_ids(
        cls,
        logger: Union["BaseLogger", "LoggerManager", "Logger"],
        headers: dict,
        number: int,
        **kwargs,
    ) -> [[str, str]]:
        return [
            await cls.get_device_id(
                logger,
                headers,
                **kwargs,
            )
            for _ in range(number)
        ]


async def test():
    from src.testers import Logger

    print(
        await DeviceId.get_device_id(
            Logger(),
            PARAMS_HEADERS_TIKTOK,
            proxy="http://127.0.0.1:10809",
        )
    )
    # print(await DeviceId.get_device_ids(
    #     Logger(),
    #     PARAMS_HEADERS_TIKTOK,
    #     5,
    #     proxy="http://127.0.0.1:10809",
    # ))


if __name__ == "__main__":
    run(test())
```

## File: `src/encrypt/msToken.py`
```python
from asyncio import run
from json import dumps
from random import randint
from string import ascii_lowercase, ascii_uppercase, digits
from time import time
from typing import TYPE_CHECKING, Union
from urllib.parse import quote

from src.custom import PARAMS_HEADERS, PARAMS_HEADERS_TIKTOK, USERAGENT
from src.encrypt.ttWid import TtWid
from src.encrypt.xBogus import XBogusTikTok
from src.tools import request_params
from src.translation import _

if TYPE_CHECKING:
    from src.record import BaseLogger, LoggerManager
    from src.testers import Logger

__all__ = ["MsToken", "MsTokenTikTok"]


class MsToken:
    NAME = "msToken"
    # API = "https://mssdk.bytedance.com/web/report"
    API = "https://mssdk.bytedance.com/web/common"
    DATA = {
        "magic": 538969122,
        "version": 1,
        "dataType": 8,
        "strData": "fWOdJTQR3/jwmZqBBsPO6tdNEc1jX7YTwPg0Z8CT+j3HScLFbj2Zm1XQ7/lqgSutntVKLJWaY3Hc/+vc0h+So9N1t6EqiImu5"
        "jKyUa+S4NPy6cNP0x9CUQQgb4+RRihCgsn4QyV8jivEFOsj3N5zFQbzXRyOV+9aG5B5EAnwpn8C70llsWq0zJz1VjN6y2KZiB"
        "ZRyonAHE8feSGpwMDeUTllvq6BG3AQZz7RrORLWNCLEoGzM6bMovYVPRAJipuUML4Hq/568bNb5vqAo0eOFpvTZjQFgbB7f/C"
        "tAYYmnOYlvfrHKBKvb0TX6AjYrw2qmNNEer2ADJosmT5kZeBsogDui8rNiI/OOdX9PVotmcSmHOLRfw1cYXTgwHXr6cJeJveu"
        "ipgwtUj2FNT4YCdZfUGGyRDz5bR5bdBuYiSRteSX12EktobsKPksdhUPGGv99SI1QRVmR0ETdWqnKWOj/7ujFZsNnfCLxNfqx"
        "QYEZEp9/U01CHhWLVrdzlrJ1v+KJH9EA4P1Wo5/2fuBFVdIz2upFqEQ11DJu8LSyD43qpTok+hFG3Moqrr81uPYiyPHnUvTFg"
        "wA/TIE11mTc/pNvYIb8IdbE4UAlsR90eYvPkI+rK9KpYN/l0s9ti9sqTth12VAw8tzCQvhKtxevJRQntU3STeZ3coz9Dg8qkv"
        "aSNFWuBDuyefZBGVSgILFdMy33//l/eTXhQpFrVc9OyxDNsG6cvdFwu7trkAENHU5eQEWkFSXBx9Ml54+fa3LvJBoacfPViyv"
        "zkJworlHcYYTG392L4q6wuMSSpYUconb+0c5mwqnnLP6MvRdm/bBTaY2Q6RfJcCxyLW0xsJMO6fgLUEjAg/dcqGxl6gDjUVRW"
        "bCcG1NAwPCfmYARTuXQYbFc8LO+r6WQTWikO9Q7Cgda78pwH07F8bgJ8zFBbWmyrghilNXENNQkyIzBqOQ1V3w0WXF9+Z3vG3"
        "aBKCjIENqAQM9qnC14WMrQkfCHosGbQyEH0n/5R2AaVTE/ye2oPQBWG1m0Gfcgs/96f6yYrsxbDcSnMvsA+okyd6GfWsdZYTI"
        "K1E97PYHlncFeOjxySjPpfy6wJc4UlArJEBZYmgveo1SZAhmXl3pJY3yJa9CmYImWkhbpwsVkSmG3g11JitJXTGLIfqKXSAhh"
        "+7jg4HTKe+5KNir8xmbBI/DF8O/+diFAlD+BQd3cV0G4mEtCiPEhOvVLKV1pE+fv7nKJh0t38wNVdbs3qHtiQNN7JhY4uWZAo"
        "sMuBXSjpEtoNUndI+o0cjR8XJ8tSFnrAY8XihiRzLMfeisiZxWCvVwIP3kum9MSHXma75cdCQGFBfFRj0jPn1JildrTh2vRgw"
        "G+KeDZ33BJ2VGw9PgRkztZ2l/W5d32jc7H91FftFFhwXil6sA23mr6nNp6CcrO7rOblcm5SzXJ5MA601+WVicC/g3p6A0lAnh"
        "jsm37qP+xGT+cbCFOfjexDYEhnqz0QZm94CCSnilQ9B/HBLhWOddp9GK0SABIk5i3xAH701Xb4HCcgAulvfO5EK0RL2eN4fb+"
        "CccgZQeO1Zzo4qsMHc13UG0saMgBEH8SqYlHz2S0CVHuDY5j1MSV0nsShjM01vIynw6K0T8kmEyNjt1eRGlleJ5lvE8vonJv7"
        "rAeaVRZ06rlYaxrMT6cK3RSHd2liE50Z3ik3xezwWoaY6zBXvCzljyEmqjNFgAPU3gI+N1vi0MsFmwAwFzYqqWdk3jwRoWLp/"
        "/FnawQX0g5T64CnfAe/o2e/8o5/bvz83OsAAwZoR48GZzPu7KCIN9q4GBjyrePNx5Csq2srblifmzSKwF5MP/RLYsk6mEE15j"
        "pCMKOVlHcu0zhJybNP3AKMVllF6pvn+HWvUnLXNkt0A6zsfvjAva/tbLQiiiYi6vtheasIyDz3HpODlI+BCkV6V8lkTt7m8QJ"
        "1IcgTfqjQBummyjYTSwsQji3DdNCnlKYd13ZQa545utqu837FFAzOZQhbnC3bKqeJqO2sE3m7WBUMbRWLflPRqp/PsklN+9jB"
        "PADKxKPl8g6/NZVq8fB1w68D5EJlGExdDhglo4B0aihHhb1u3+zJ2DqkxkPCGBAZ2AcuFIDzD53yS4NssoWb4HJ7YyzPaJro+"
        "tgG9TshWRBtUw8Or3m0OtQtX+rboYn3+GxvD1O8vWInrg5qxnepelRcQzmnor4rHF6ZNhAJZAf18Rjncra00HPJBugY5rD+Ew"
        "nN9+mGQo43b01qBBRYEnxy9JJYuvXxNXxe47/MEPOw6qsxN+dmyIWZSuzkw8K+iBM/anE11yfU4qTFt0veCaVprK6tXaFK0Zh"
        "GXDOYJd70sjIP4UrPhatp8hqIXSJ2cwi70B+TvlDk/o19CA3bH6YxrAAVeag1P9hmNlfJ7NxK3Jp7+Ny1Vd7JHWVF+R6rSJiX"
        "XPfsXi3ZEy0klJAjI51NrDAnzNtgIQf0V8OWeEVv7F8Rsm3/GKnjdNOcDKymi9agZUgtctENWbCXGFnI40NHuVHtBRZeYAYtw"
        "fV7v6U0bP9s7uZGpkp+OETHMv3AyV0MVbZwQvarnjmct4Z3Vma+DvT+Z4VlMVnkC2x2FLt26K3SIMz+KV2XLv5ocEdPFSn1vM"
        "R7zruCWC8XqAG288biHo/soldmb/nlw8o8qlfZj4h296K3hfdFubGIUtqgsrZCrLCkkRC08Cv1ozEX/y6t2YrQepwiNmwDVk5"
        "IufStVvJMj+y2r9TcYLv7UKWXx3P6aySvM2ZHPaZhv+6Z/A/jIMBSvOizn4qG11iK7Oo6JYhxCSMJZsetjsnL4ecSIAufEmoF"
        "lAScWBh6nFArRpVLvkAZ3tej7H2lWFRXIU7x7mdBfGqU82PpM6znKMMZCpEsvHqpkSPSL+Kwz2z1f5wW7BKcKK4kNZ8iveg9V"
        "zY1NNjs91qU8DJpUnGyM04C7KNMpeilEmoOxvyelMQdi85ndOVmigVKmy5JYlODNX744sHpeqmMEK/ux3xY5O406lm7dZlyGP"
        "SMrFWbm4rzqvSEIskP43+9xVP8L84GeHE4RpOHg3qh/shx+/WnT1UhKuKpByHCpLoEo144udpzZswCYSMp58uPrlwdVF31//A"
        "acTRk8dUP3tBlnSQPa1eTpXWFCn7vIiqOTXaRL//YQK+e7ssrgSUnwhuGKJ8aqNDgdsL+haVZnV9g5Qrju643adyNixvYFEp0"
        "uxzOzVkekOMh2FYnFVIL2mJYGpZEXlAIC0zQbb54rSP89j0G7soJ2HcOkD0NmMEWj/7hUdTuMin1lRNde/qmHjwhbhqL8Z9ME"
        "O/YG3iLMgFTgSNQQhyE8AZAAKnehmzjORJfbK+qxyiJ07J843EDduzOoYt9p/YLqyTFmAgpdfK0uYrtAJ47cbl5WWhVXp5/XU"
        "xwWdL7TvQB0Xh6ir1/XBRcsVSDrR7cPE221ThmW1EPzD+SPf2L2gS0WromZqj1PhLgk92YnnR9s7/nLBXZHPKy+fDbJT16Qqa"
        "bFKqAl9G0blyf+R5UGX2kN+iQp4VGXEoH5lXxNNTlgRskzrW7KliQXcac20oimAHUE8Phf+rXXglpmSv4XN3eiwfXwvOaAMVj"
        "MRmRxsKitl5iZnwpcdbsC4jt16g2r/ihlKzLIYju+XZej4dNMlkftEidyNg24IVimJthXY1H15RZ8Hm7mAM/JZrsxiAVI0A49"
        "pWEiUk3cyZcBzq/vVEjHUy4r6IZnKkRvLjqsvqWE95nAGMor+F0GLHWfBCVkuI51EIOknwSB1eTvLgwgRepV4pdy9cdp6iR8T"
        "ZndPVCikflXYVMlMEJ2bJ2c0Swiq57ORJW6vQwnkxtPudpFRc7tNNDzz4LKEznJxAwGi6pBR7/co2IUgRw1ijLFTHWHQJOjgc"
        "7KaduHI0C6a+BJb4Y8IWuIk2u2qCMF1HNKFAUn/J1gTcqtIJcvK5uykpfJFCYc899TmUc8LMKI9nu57m0S44Y2hPPYeW4XSak"
        "Scsg8bJHMkcXk3Tbs9b4eqiD+kHUhTS2BGfsHadR3d5j8lNhBPzA5e+mE==",
        "tspFromClient": 0,
        "ulr": 0,
    }
    TOKEN = (
        "9cguMjz4GIfQV50B_D49quM-cEyIvWMwWi0gj1bf"
        "-4YprIjt29ZrAxmDb5oIhmzEhwvcmcC4BR_kEZGmXdS1q7Ad3V94izdpXwtxgPPpozVUzQVm7KDrc5H9nfN3pLw="
    )

    @staticmethod
    def get_fake_ms_token(key="msToken", size=156) -> dict:
        """
        根据传入长度产生随机字符串
        """
        base_str = digits + ascii_uppercase + ascii_lowercase
        length = len(base_str) - 1
        return {key: "".join(base_str[randint(0, length)] for _ in range(size))}

    @classmethod
    async def _get_ms_token(
        cls,
        logger: Union["BaseLogger", "LoggerManager", "Logger"],
        params: dict,
        headers: dict,
        proxy: str,
        **kwargs,
    ) -> dict | None:
        if response := await request_params(
            logger,
            cls.API,
            data=dumps(cls.DATA | {"tspFromClient": int(time() * 1000)}),
            headers=headers,
            params=params,
            proxy=proxy,
            **kwargs,
        ):
            return TtWid.extract(logger, response, cls.NAME)
        logger.error(_("获取 {name} 参数失败！").format(name=cls.NAME))

    @classmethod
    async def get_real_ms_token(
        cls,
        logger: Union["BaseLogger", "LoggerManager", "Logger"],
        headers: dict,
        token="",
        proxy: str = None,
        **kwargs,
    ) -> dict | None:
        params = {cls.NAME: token}
        return await cls._get_ms_token(
            logger,
            params,
            headers,
            proxy,
            **kwargs,
        )

    @classmethod
    async def get_long_ms_token(
        cls,
        logger: Union["BaseLogger", "LoggerManager", "Logger"],
        headers: dict,
        token="",
        proxy: str = None,
        **kwargs,
    ) -> dict | None:
        return await cls.get_real_ms_token(
            logger,
            headers,
            token or cls.TOKEN,
            proxy,
            **kwargs,
        )


class MsTokenTikTok(MsToken):
    REFERER = "https://www.tiktok.com/"
    API = "https://mssdk-ttp2.tiktokw.us/web/report"
    DATA = {
        "magic": 538969122,
        "version": 1,
        "dataType": 8,
        "strData": "3DWMSoJNifh/BoM1CDv7lbH3G7vd6C7zPt0YWMVrYRi369yWaBxCOhq+WMznjr1QWKkr/uLgcnRh+LQDtMl/JDLHSPlEqNPz"
        "/iuxeOktia3YM/pJtUX4EQYqBMW8uAx4qFcN8M5H5XhB1FEkk76W09Xq5DwtcjoO4dpH18G3UcI1hasCXVW8B"
        "+igwPIeEuOIayxuf3OZlTmZbNI1guSUBbccxoph0SEb1TVc4/DeQjQvXkXZOmuN144LcENdtflWmcQPqcwnfD2bWGuR4"
        "+LUgRke1GcyVYa440PH/VOm+DYNcbKeBG87gqTHg+Y724ph1RQKlKX4nsi7Wa+V08ESimNbT8DMsbA"
        "//MovFbr0CiVmvqtXg6VLloJH7UlZRQTC7T0l90KssOt0Y4T/H2EbU5XywcZd8OpICK4wB"
        "/m8KuHGzrheYGmIfxUQtWhrlJdtqzoNI/GiEceTHxp4NahNof4KH6+BZMv87B7nYyE2x7eH2AaeG8iVoiyYKrE7ckQX8mjvj12"
        "+BIkhUiKhpe3SGewK0iEB8NYH3fSqap/QnGsYcSy3lCwHlq7wHUcNdwhKFXkMS65Op"
        "/zpS4uOEZqK9a0v8iGwBrd1VSfFki7sXGUFm5fGMh1Z9Z+4tycL7MYk5fzdUkZ+e56h4p5vPg4qpG17ntvn1LcXR/HXZKgMlx"
        "+qqd3hOpnFOGcC2PahUp+zQ3Y/pZ3Jr+0XRmlHm4zpDmYJkqo3XZrTetOI5JwBkTN/GUkWyVC8hV48WyXpUxUiSHSBeN17735"
        "+PrijcAZh/1+R"
        "+gjnTkcAfm4pxlMfEur85pvI9K0qZbosPV3cgd3T3R5djejTilcyJ3wOC29pV4U193BEXqZnfIPYHFxXc5dlxYlq6tGHbdXsih1b"
        "bguCXchz6byslGKDnWTSHA+QufOcfIh6HNijtM1iHNhAz/BkpiehN8u27ntq5p9VH0Um3Q6yh6lmcR5Jexry8l6zXT5HAbImhKK"
        "F2GhMzznMaSFASYTTIyzwLVtZab+9HIEnlRmSg/B2Vrc0M0r+qsucb4vji4q/oWh7SUeqcstUXKt86dSUi0xmH1tRDbK9Gb8Avp"
        "ef5tITSPqwuI9A6uqHctCCC54XMw6RPmmzueXJYM8hRF7PpjK76zxtPImLeg1zxwjnb8GsoaTnNsrDVboTpFtbcA6c3IEYvqZ/Z"
        "OmJww74eMhDAuc0SGnF7RgIeHxHHc1mdoK6lmzjI4c2S7nYusgcLGzzSJm3D98AncBkOQ3BONTCAnb7era4absFz4jPTFWGPN5Z"
        "3xhD5h5E9dHX1V05MUCzcTV+ooEtlcgLfW4nt+CPWeyxfekrlqMZPuwlvgepIOIj2dnYckVbCcXqIhNPVAzDzt847IzPnQGViT8"
        "5VH6n6NKdA0c1om130oa+Zu5kWrzXqekOAkN1K7xlQlqD+t2QFGVZLtZoAUWF6+nAyI3Zz4+7fT/RAzsmRFSCWMiKsSK96tBLNZ"
        "5GXupRlQ/Ns7MH5FCduL+l3I2Dfwas2M+qLr/gTJ/wRGGI4KhXNHlQzzJmOG8VOrwV4hyHBvl1B3j6R+7UZ/Jo57BZIHG+cui3o"
        "AGqCreMByWLy3L+/38MkCCACw6YGvhccrYkjSIcmNv3qbQv1WoLXrGq0k9IOB69KWB7bX0kFUnr1l3Gwvc47U3IJIbGmSOYumtv"
        "naumgZqcyWitMud0kOGW1wCvpyY1+tv1AZtsCIdLJYqj4M1u+iQ/GuJGQlyFWVY/3gcurWoFqhOl156t9mkXhHZeILv2Y/L+IEs"
        "zW6cwu/N0tukf1kgBlLwtmfMQA/rvzn6ueAYNQ0A0KNSfm5ndiZaCxBlHlUBCa4Fe7vMxLhKZ44ffcu0D5RMESjduuykgInMrSp"
        "vE88hHs01A2NL8HiRBQTjBWAiP273kWun6DWecqqkw0kr5ZjVGCYZPFVlLUL9JGcWcTmUZa96bTu7hKB14+P9tOjK+N95tuQnqL"
        "DPS849ceh3qPX8PPn5PgmExPjd7OfMmbn39XCBZQBnMuuV8ceanDlmfnqhtqaEk3jRnkvXn3lDFY5EYw2Uja3XgkgBTyf3hsm7Y"
        "mlqrGR/1mt0WyJiDW2sF+veKVxirGdv3GHJ2IRDo1lb6W/ZEIHiGimteqBXyYE7JdJxeFcrU2+NWoFvP2TX3DJAIEFaFcEQRkZA"
        "+gzR2pCu3jfazUOEP3nKLE6If30xeUClWLC5qZXsRwIjjj5+CvtRNrEkAcnpQenq8RgTQ0fu9CvJZ9bcRWuItsZdjh+ll0+dFs7"
        "yI9Qhus3ccl09aGUc6+EomD96DBuW9B6bEWmKnVJuqZJgeH6v+oCYinFjMdhrGPHf05U06Bu7NCHN361aqE/XKAyN9GmUZTHsp9"
        "8hEbZqaWycuDGJ1PFc54dUEfaACa30WbEkT2zqzq3A9zHx7Rr87h79+t1yjz5CEvU7xfc1WXjV0vFr3+B8yJFhT0fWhNZ7fP/LL"
        "3C/Zcy/3qznQFxavc0TacInSDLqfz8ju31N7LJs9js1Xd7UVyvqOq6nu0YOI1lDAl8xaetH6rAIsEr+IuOKvTVYuUXVjaTnMa2Q"
        "xkORw2l+tfl9QgRF1csGofJl5K1tuSjTMbMxEGhoLcjzPEtqiyXF96CJSbquCwhw8tzQIXoajUgY9wrnUalSARMaXkhUejOMNqH"
        "/0c5S6cyP5p4zk1cfUihY6W2vcNsrdILAib4dMVflXulaTBopkvh6fD6DiWHw36nQeLT9WfvZ3xwUeNjeQca8fWV0950GUNbVk8"
        "Iq35ltuGdFhSiE+6wgXoq78NS5WB4iChkZ5/IIVvfU/0To32SEiHMRINQTZFXPZWjjIdxwkdmOvEbqD4Bfu4jWRSC5pzTN0bTU3"
        "ax+hCYWDAVxsZi7HwkeMnDUueBaXt9QbeH0cA0XJELudePlsfYaqhEytDKG6PyQjROnQKZMDgBdsGi7kbcIJvsq9ldvI4XrYFfL"
        "nNese4Hveij58+Rw0j6wO+7EjiWAEow5Q2Yqlgk2jNgB8xorpUaxxyIfe/rSNs7I0VhynwqJXENKq/ZWlf72liv1g1hMGDy8x9X"
        "Q+x+pefBJ5h0r1Jd+FTE7Dpk7B57zAefH/9uAE/IUS21i78INIYa8QtORZOuLmW27y5fBjD4BdpPb8hYSjX56zHLkGjUNEXEj9C"
        "HKns7tse8zAKUleMVTw5+3juYjsCVvPYntqx9Hbgc3QEG9zWoS6feX1aBIpIRR2M8dn8pWI8WmHWCa1cO/5DAMas83sExxMER4/"
        "dXMIn7mLnsojNje1+XiAF9o2wt7rksJazO+nAxULLLWiMAsd6BpK6GgHZUgFFihSIYZaOrjE/TVoDREEuznHEdHiZMYdjAk9Gq4"
        "SEUmeujJFyXHSQ6yYjpxSlQKFLTUAlYf+j9c55RoYO+/Wy0nb5Gwkzl8GEwa9SsWi/9prCJCNOvlwix5VPqerBpJvFF8dPJizXQ"
        "85ZYJUknOOCxZViPwxsZaRbItUKO/7MVMBfK0Nde/AGrkCFMlwU45NvD0PrXWOIZMZW0Z5vtboqS1yMOHjBV97he4IXThAuLzjB"
        "mzdtmUvIHgdxg1Fx+u//Qmbnqn00e4yqTQUpnfF5jCvRfUtacc6SfT0KbsFyUe4JRa5ZAhZ1OzeiqBOKm+NRF3ko7lnt70Tjwnt"
        "Gcf2YK03kN5VEKYDEIFbQjmlktyxeUpiEW+ZdD7/A0jrC8ob3JhCzsrnntkt9vNK4NI8woIDKvDPAbbEKm4FsTsLfnJrbEL0qs1"
        "n/0ISRhXH0XLYx5sLrVDzXjY6BwC51pkMBvmDT+EOpvln0Ya6+pAd1tuuWjbz3cZvFUe/V+808hjMPnf8ieuunjBKdW/zSDVul9"
        "I/gIOzpJwmujzZh6FHDrAR0oMqyOC27kTfoEBy49s1JK+cvpx6+uUmGfuqEJuKemzHl3F0+4EF32fXngQcMPf2W0V0j5jgccde/"
        "r7ga4Af3uEJNqYBfxX6L+r2aIPlGFvwQw2VLuhIKSiVaqhFrJbb4xYHSFhomTLgEQoxIB6sS4CXAg+sg33xtAwmtgdTFYtvuvYn"
        "qFzB54DIcx/FNPzTUzwh/vhfup4HUWgL1lHnE/uaCZnceQXHxoymjfyBctHqmopigJI4arMEu3Db+xGclUpIrgmxMWs0CaG+yMp"
        "33Ulmay3bNlhBpFzDSzRaMsNa0sk8L5MM0QCeKaTqaRx2qfaLuWlURXflBGRxApIZbMi9lIg119/QuKaXhtdFP00RYzYk03cTNi"
        "MUlm0lKg/DGyOLWTp+huhZHg0umkQHDi0wbLDfwXrTZowQdim9iYPOJaLOUr1rqODk2dHe/gTLcErlAT/OL6MRmOvtwlMfpbN0L"
        "n6xh11L4+WWJFNFT3lCXsFaybLh8R2MxllwT32EjAXSiLrd8rh05PBKGQJE7eg9hScjdNS4UUc8rSTf7pidBbSbMbfDJDWixSBT"
        "nzkLD2Om7etBZ2yw/F14uK9sgtuRkNegmyazk84MChAL3gCCRKoDnwvc/3VhhJYmXyzDyQSZkVfUfr9Vm9TWhKjS7eyor8D/Rc9"
        "K4NCGUQ3EOMnkxi1E3Ae52ZboKci/rZtqhaOZuwxD+fFXT4hXWA5OxK3++LxsKu0tnVRoufxjvDEIW4MfWqfsOOdnUreBJlB5uq"
        "xqtYoGlBfgCntLU/F80FDgAfVDUqWr49fuRdOjsuZm",
    }
    TOKEN = (
        "DFrAJZtLAY2Lrd8Tvmh5cqHYng42N9aIQxG0Rhos9kNznkm4oSeGUOmPptqIveuXzrQARNP"
        "-F08uUkIaCQo_kaYSN6d7X5pQIM8pOFckqCgBLbTMqTZC9rEheMlW88EOKPMVBJ7t-CGQDTTfx0k8tEyx"
    )

    @classmethod
    async def get_real_ms_token(
        cls,
        logger: Union["BaseLogger", "LoggerManager", "Logger"],
        headers: dict,
        token="",
        proxy: str = None,
        **kwargs,
    ) -> dict | None:
        params = {cls.NAME: token}
        if token:
            headers |= {"Cookie": f"{cls.NAME}={token}"}
            params["X-Bogus"] = quote(
                XBogusTikTok().get_x_bogus(
                    params, user_agent=headers.get("User-Agent", USERAGENT)
                ),
                safe="",
            )
        return await cls._get_ms_token(
            logger,
            params,
            headers,
            proxy,
            **kwargs,
        )


async def test():
    from src.testers import Logger

    print("抖音", await MsToken.get_real_ms_token(Logger(), PARAMS_HEADERS, proxy=None))
    print(
        "抖音",
        await MsToken.get_long_ms_token(
            Logger(),
            PARAMS_HEADERS,
            proxy=None,
        ),
    )
    print(
        "TikTok",
        await MsTokenTikTok.get_real_ms_token(
            Logger(), PARAMS_HEADERS_TIKTOK, proxy="http://127.0.0.1:10809"
        ),
    )
    print(
        "TikTok",
        await MsTokenTikTok.get_long_ms_token(
            Logger(), PARAMS_HEADERS_TIKTOK, proxy="http://127.0.0.1:10809"
        ),
    )


if __name__ == "__main__":
    run(test())
```

## File: `src/encrypt/ttWid.py`
```python
from asyncio import run
from http import cookies
from json import dumps
from typing import TYPE_CHECKING, Union

from src.custom import PARAMS_HEADERS, PARAMS_HEADERS_TIKTOK
from src.tools import request_params
from src.translation import _

if TYPE_CHECKING:
    from src.record import BaseLogger, LoggerManager
    from src.testers import Logger

__all__ = ["TtWid", "TtWidTikTok"]


class TtWid:
    NAME = "ttwid"
    API = "https://ttwid.bytedance.com/ttwid/union/register/"
    DATA = (
        '{"region":"cn","aid":1768,"needFid":false,"service":"www.ixigua.com","migrate_info":{"ticket":"",'
        '"source":"node"},"cbUrlProtocol":"https","union":true}'
    )

    @classmethod
    async def get_tt_wid(
        cls,
        logger: Union["BaseLogger", "LoggerManager", "Logger"],
        headers: dict,
        proxy: str = None,
        **kwargs,
    ) -> dict | None:
        if response := await request_params(
            logger,
            cls.API,
            data=cls.DATA,
            headers=headers,
            proxy=proxy,
            **kwargs,
        ):
            return cls.extract(logger, response, cls.NAME)
        logger.error(_("获取 {name} 参数失败！").format(name=cls.NAME))

    @staticmethod
    def extract(
        logger: Union["BaseLogger", "LoggerManager", "Logger"], headers, key: str
    ) -> dict | None:
        if c := headers.get("Set-Cookie"):
            cookie_jar = cookies.SimpleCookie()
            cookie_jar.load(c)
            if v := cookie_jar.get(key):
                return {key: v.value}
        logger.error(f"获取 {key} 参数失败！")


class TtWidTikTok(TtWid):
    API = "https://www.tiktok.com/ttwid/check/"
    DATA = dumps(
        {
            "aid": 1988,
            "service": "www.tiktok.com",
            "union": False,
            "unionHost": "",
            "needFid": False,
            "fid": "",
            "migrate_priority": 0,
        },
        separators=(",", ":"),
    )

    @classmethod
    async def get_tt_wid(
        cls,
        logger: Union["BaseLogger", "LoggerManager", "Logger"],
        headers: dict,
        cookie: str = "",
        proxy: str = None,
        **kwargs,
    ) -> dict | None:
        if response := await request_params(
            logger,
            cls.API,
            data=cls.DATA,
            headers=headers
            | {
                "Cookie": cookie,
                "Content-Type": "application/x-www-form-urlencoded",
            },
            proxy=proxy,
            **kwargs,
        ):
            return cls.extract(logger, response, cls.NAME)
        logger.error(_("获取 {name} 参数失败！").format(name=cls.NAME))


async def test():
    from src.testers import Logger

    print("抖音", await TtWid.get_tt_wid(Logger(), PARAMS_HEADERS, proxy=None))
    print(
        "TikTok",
        await TtWidTikTok.get_tt_wid(
            Logger(),
            PARAMS_HEADERS_TIKTOK,
            cookie="ttwid=",
            proxy="http://localhost:10809",
        ),
    )


if __name__ == "__main__":
    run(test())
```

## File: `src/encrypt/verifyFp.py`
```python
from random import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from time import time

from rich import print

__all__ = [
    "VerifyFp",
]


class VerifyFp:
    """
    var xi = function() {
        return Pi.get(Si) || (null === localStorage || void 0 === localStorage ? void 0 : localStorage.getItem(Si)) || function() {
            var e = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split("")
              , t = e.length
              , n = Date.now().toString(36)
              , r = [];
            r[8] = r[13] = r[18] = r[23] = "_",
            r[14] = "4";
            for (var o = 0, i = void 0; o < 36; o++)
                r[o] || (i = 0 | Math.random() * t,
                r[o] = e[19 == o ? 3 & i | 8 : i]);
            return "verify_" + n + "_" + r.join("")
        }()
    }
    """

    @staticmethod
    def get_verify_fp(timestamp: int = None):
        base_str = digits + ascii_uppercase + ascii_lowercase
        t = len(base_str)
        milliseconds = timestamp or int(round(time() * 1000))
        base36 = ""

        # 转换为 base36
        while milliseconds > 0:
            milliseconds, remainder = divmod(milliseconds, 36)
            if remainder < 10:
                base36 = str(remainder) + base36
            else:
                base36 = chr(ord("a") + remainder - 10) + base36

        # 设置固定字符
        o = [""] * 36
        o[8] = o[13] = o[18] = o[23] = "_"
        o[14] = "4"

        # 随机填充缺失的字符
        for i in range(36):
            if not o[i]:
                n = int(random() * t)  # 优化随机数生成方式
                if i == 19:
                    n = 3 & n | 8
                o[i] = base_str[n]

        # 组合最终字符串
        return f"verify_{base36}_" + "".join(o)


if __name__ == "__main__":
    params = 1710413848097
    print(VerifyFp.get_verify_fp(params))
```

## File: `src/encrypt/webID.py`
```python
from asyncio import run
from typing import TYPE_CHECKING, Union

from src.custom import PARAMS_HEADERS
from src.tools import request_params
from src.translation import _

if TYPE_CHECKING:
    from src.record import BaseLogger, LoggerManager
    from src.testers import Logger

__all__ = ["WebId"]


class WebId:
    NAME = "webid"
    API = "https://mcs.zijieapi.com/webid"
    PARAMS = {"aid": "6383", "sdk_version": "5.1.18_zip", "device_platform": "web"}

    @classmethod
    async def get_web_id(
        cls,
        logger: Union["BaseLogger", "LoggerManager", "Logger"],
        headers: dict,
        proxy: str = None,
        **kwargs,
    ) -> str | None:
        user_agent = headers.get("User-Agent")
        data = (
            f'{{"app_id":6383,"url":"https://www.douyin.com/","user_agent":"{user_agent}","referer":"https://www'
            f'.douyin.com/","user_unique_id":""}}'
        )
        if response := await request_params(
            logger,
            cls.API,
            params=cls.PARAMS,
            data=data,
            headers=headers,
            resp="json",
            proxy=proxy,
            **kwargs,
        ):
            return response.get("web_id")
        logger.error(_("获取 {name} 参数失败！").format(name=cls.NAME))


async def test():
    from src.testers import Logger

    print(await WebId.get_web_id(Logger(), PARAMS_HEADERS, proxy=None))


if __name__ == "__main__":
    run(test())
```

## File: `src/encrypt/xBogus.py`
```python
from base64 import b64encode
from hashlib import md5
from time import time
from urllib.parse import quote, urlencode

from ..custom import USERAGENT

__all__ = ["XBogus", "XBogusTikTok"]


class XBogus:
    __string = "Dkdpgh4ZKsQB80/Mfvw36XI1R25-WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe="
    __array = (
        [None for _ in range(48)]
        + list(range(10))
        + [None for _ in range(39)]
        + list(range(10, 16))
    )
    __canvas = 3873194319

    @staticmethod
    def disturb_array(a, b, e, d, c, f, t, n, o, i, r, _, x, u, s, l, v, h, g):
        array = [0] * 19
        array[0] = a
        array[10] = b
        array[1] = e
        array[11] = d
        array[2] = c
        array[12] = f
        array[3] = t
        array[13] = n
        array[4] = o
        array[14] = i
        array[5] = r
        array[15] = _
        array[6] = x
        array[16] = u
        array[7] = s
        array[17] = l
        array[8] = v
        array[18] = h
        array[9] = g
        return array

    @staticmethod
    def generate_garbled_1(a, b, e, d, c, f, t, n, o, i, r, _, x, u, s, l, v, h, g):
        array = [0] * 19
        array[0] = a
        array[1] = r
        array[2] = b
        array[3] = _
        array[4] = e
        array[5] = x
        array[6] = d
        array[7] = u
        array[8] = c
        array[9] = s
        array[10] = f
        array[11] = l
        array[12] = t
        array[13] = v
        array[14] = n
        array[15] = h
        array[16] = o
        array[17] = g
        array[18] = i
        return "".join(map(chr, map(int, array)))

    @staticmethod
    def generate_num(text):
        return [
            ord(text[i]) << 16 | ord(text[i + 1]) << 8 | ord(text[i + 2]) << 0
            for i in range(0, 21, 3)
        ]

    @staticmethod
    def generate_garbled_2(a, b, c):
        return chr(a) + chr(b) + c

    @staticmethod
    def generate_garbled_3(a, b):
        d = list(range(256))
        c = 0
        f = ""
        for a_idx in range(256):
            d[a_idx] = a_idx
        for b_idx in range(256):
            c = (c + d[b_idx] + ord(a[b_idx % len(a)])) % 256
            e = d[b_idx]
            d[b_idx] = d[c]
            d[c] = e
        t = 0
        c = 0
        for b_idx in range(len(b)):
            t = (t + 1) % 256
            c = (c + d[t]) % 256
            e = d[t]
            d[t] = d[c]
            d[c] = e
            f += chr(ord(b[b_idx]) ^ d[(d[t] + d[c]) % 256])
        return f

    def calculate_md5(self, input_string):
        if isinstance(input_string, str):
            array = self.md5_to_array(input_string)
        elif isinstance(input_string, list):
            array = input_string
        else:
            raise TypeError

        md5_hash = md5()
        md5_hash.update(bytes(array))
        return md5_hash.hexdigest()

    def md5_to_array(self, md5_str):
        if isinstance(md5_str, str) and len(md5_str) > 32:
            return [ord(char) for char in md5_str]
        else:
            return [
                (self.__array[ord(md5_str[index])] << 4)
                | self.__array[ord(md5_str[index + 1])]
                for index in range(0, len(md5_str), 2)
            ]

    def process_url_path(self, url_path):
        return self.md5_to_array(
            self.calculate_md5(self.md5_to_array(self.calculate_md5(url_path)))
        )

    def generate_str(self, num):
        string = [num & 16515072, num & 258048, num & 4032, num & 63]
        string = [i >> j for i, j in zip(string, range(18, -1, -6))]
        return "".join([self.__string[i] for i in string])

    @staticmethod
    def handle_ua(a, b):
        d = list(range(256))
        c = 0
        result = bytearray(len(b))

        for i in range(256):
            c = (c + d[i] + ord(a[i % len(a)])) % 256
            d[i], d[c] = d[c], d[i]

        t = 0
        c = 0

        for i in range(len(b)):
            t = (t + 1) % 256
            c = (c + d[t]) % 256
            d[t], d[c] = d[c], d[t]
            result[i] = b[i] ^ d[(d[t] + d[c]) % 256]

        return result

    def generate_ua_array(self, user_agent: str, params: int) -> list:
        ua_key = ["\u0000", "\u0001", chr(params)]
        value = self.handle_ua(ua_key, user_agent.encode("utf-8"))
        value = b64encode(value)
        return list(md5(value).digest())

    def generate_x_bogus(
        self, query: list, params: int, user_agent: str, timestamp: int
    ):
        ua_array = self.generate_ua_array(user_agent, params)
        array = [
            64,
            0.00390625,
            1,
            params,
            query[-2],
            query[-1],
            69,
            63,
            ua_array[-2],
            ua_array[-1],
            timestamp >> 24 & 255,
            timestamp >> 16 & 255,
            timestamp >> 8 & 255,
            timestamp >> 0 & 255,
            self.__canvas >> 24 & 255,
            self.__canvas >> 16 & 255,
            self.__canvas >> 8 & 255,
            self.__canvas >> 0 & 255,
            None,
        ]
        zero = 0
        for i in array[:-1]:
            if isinstance(i, float):
                i = int(i)
            zero ^= i
        array[-1] = zero
        garbled = self.generate_garbled_1(*self.disturb_array(*array))
        garbled = self.generate_garbled_2(2, 255, self.generate_garbled_3("ÿ", garbled))
        return "".join(self.generate_str(i) for i in self.generate_num(garbled))

    def get_x_bogus(
        self, query: dict | str, params=8, user_agent=USERAGENT, test_time=None
    ):
        timestamp = int(test_time or time())
        query = self.process_url_path(
            urlencode(query, quote_via=quote) if isinstance(query, dict) else query
        )
        return self.generate_x_bogus(query, params, user_agent, timestamp)


class XBogusTikTok(XBogus):
    pass
```

## File: `src/encrypt/xGnarly.py`
```python
from hashlib import md5
from random import randint
from time import time

from src.custom import USERAGENT


class XGnarly:
    _AA = [
        0xFFFFFFFF,
        138,
        1498001188,
        211147047,
        253,
        None,
        203,
        288,
        9,
        1196819126,
        3212677781,
        135,
        263,
        193,
        58,
        18,
        244,
        2931180889,
        240,
        173,
        268,
        2157053261,
        261,
        175,
        14,
        5,
        171,
        270,
        156,
        258,
        13,
        15,
        3732962506,
        185,
        169,
        2,
        6,
        132,
        162,
        200,
        3,
        160,
        217618912,
        62,
        2517678443,
        44,
        164,
        4,
        96,
        183,
        2903579748,
        3863347763,
        119,
        181,
        10,
        190,
        8,
        2654435769,
        259,
        104,
        230,
        128,
        2633865432,
        225,
        1,
        257,
        143,
        179,
        16,
        600974999,
        185100057,
        32,
        188,
        53,
        2718276124,
        177,
        196,
        4294967296,
        147,
        117,
        17,
        49,
        7,
        28,
        12,
        266,
        216,
        11,
        0,
        45,
        166,
        247,
        1451689750,
    ]
    _OT = [_AA[9], _AA[69], _AA[51], _AA[92]]
    _MASK32 = 0xFFFFFFFF
    _BASE64_ALPHABET = (
        "u09tbS3UvgDEe6r-ZVMXzLpsAohTn7mdINQlW412GqBjfYiyk8JORCF5/xKHwacP="
    )

    def __init__(self):
        """
        初始化 XGnarly 实例，并创建其唯一的 PRNG 状态。
        """
        self.St = None
        self._init_prng_state()

    def _init_prng_state(self):
        """
        设置 PRNG 的初始状态，此状态将在此实例的生命周期内持续存在。
        """
        now_ms = int(time() * 1000)
        self.kt = [
            self._AA[44],
            self._AA[74],
            self._AA[10],
            self._AA[62],
            self._AA[42],
            self._AA[17],
            self._AA[2],
            self._AA[21],
            self._AA[3],
            self._AA[70],
            self._AA[50],
            self._AA[32],
            self._AA[0] & now_ms,
            randint(0, self._AA[77]),
            randint(0, self._AA[77]),
            randint(0, self._AA[77]),
        ]
        self.St = self._AA[88]  # position pointer, starts at 0

    # ── BIT HELPERS ────────────────────────────────────────
    @classmethod
    def _u32(cls, x: int) -> int:
        return x & cls._MASK32

    @classmethod
    def _rotl(cls, x: int, n: int) -> int:
        return cls._u32(((x << n) & cls._MASK32) | (x >> (32 - n)))

    # ── CHACHA CORE ────────────────────────────────────────
    @classmethod
    def _quarter(cls, st: list[int], a: int, b: int, c: int, d: int):
        st[a] = cls._u32(st[a] + st[b])
        st[d] = cls._rotl(st[d] ^ st[a], 16)
        st[c] = cls._u32(st[c] + st[d])
        st[b] = cls._rotl(st[b] ^ st[c], 12)
        st[a] = cls._u32(st[a] + st[b])
        st[d] = cls._rotl(st[d] ^ st[a], 8)
        st[c] = cls._u32(st[c] + st[d])
        st[b] = cls._rotl(st[b] ^ st[c], 7)

    @classmethod
    def _chacha_block(cls, state: list[int], rounds: int) -> list[int]:
        w = state.copy()
        r = 0
        while r < rounds:
            cls._quarter(w, 0, 4, 8, 12)
            cls._quarter(w, 1, 5, 9, 13)
            cls._quarter(w, 2, 6, 10, 14)
            cls._quarter(w, 3, 7, 11, 15)
            r += 1
            if r >= rounds:
                break
            cls._quarter(w, 0, 5, 10, 15)
            cls._quarter(w, 1, 6, 11, 12)
            cls._quarter(w, 2, 7, 12, 13)
            cls._quarter(w, 3, 4, 13, 14)
            r += 1
        for i in range(16):
            w[i] = cls._u32(w[i] + state[i])
        return w

    def _bump_counter(self):
        self.kt[12] = self._u32(self.kt[12] + 1)

    # ── JS-faithful PRNG (rand) ────────────────────────────
    def rand(self) -> float:
        e = self._chacha_block(self.kt, 8)
        t = e[self.St]
        r = (e[self.St + 8] & 0xFFFFFFF0) >> 11
        if self.St == 7:
            self._bump_counter()
            self.St = 0
        else:
            self.St += 1
        return (t + 4294967296 * r) / (2**53)

    # ── UTILITIES ──────────────────────────────────────────
    @staticmethod
    def _num_to_bytes(val: int) -> list[int]:
        if val < 65535:
            return [(val >> 8) & 0xFF, val & 0xFF]
        return [(val >> 24) & 0xFF, (val >> 16) & 0xFF, (val >> 8) & 0xFF, val & 0xFF]

    @staticmethod
    def _be_int_from_str(s: str) -> int:
        b = s.encode("utf-8")[:4]
        acc = 0
        for x in b:
            acc = (acc << 8) | x
        return acc & XGnarly._MASK32

    # ── MESSAGE ENCRYPTION ──────────────────────────────
    def _encrypt_chacha(self, key_words: list[int], rounds: int, data: list[int]):
        n_full = len(data) // 4
        leftover = len(data) % 4
        words = [0] * ((len(data) + 3) // 4)

        for i in range(n_full):
            j = 4 * i
            words[i] = (
                data[j] | (data[j + 1] << 8) | (data[j + 2] << 16) | (data[j + 3] << 24)
            )
        if leftover:
            v = 0
            base = 4 * n_full
            for c in range(leftover):
                v |= data[base + c] << (8 * c)
            words[n_full] = v

        o = 0
        state = key_words.copy()
        while o + 16 < len(words):
            stream = self._chacha_block(state, rounds)
            state[12] = self._u32(state[12] + 1)
            for k in range(16):
                words[o + k] ^= stream[k]
            o += 16

        if o < len(words):
            stream = self._chacha_block(state, rounds)
            for k in range(len(words) - o):
                words[o + k] ^= stream[k]

        for i in range(n_full):
            w = words[i]
            j = 4 * i
            data[j : j + 4] = [
                w & 0xFF,
                (w >> 8) & 0xFF,
                (w >> 16) & 0xFF,
                (w >> 24) & 0xFF,
            ]
        if leftover:
            w = words[n_full]
            base = 4 * n_full
            for c in range(leftover):
                data[base + c] = (w >> (8 * c)) & 0xFF

    def _ab22(self, key12_words: list[int], rounds: int, s: str) -> str:
        state = self._OT + key12_words
        data = [ord(ch) for ch in s]
        self._encrypt_chacha(state, rounds, data)
        return "".join(chr(x) for x in data)

    # ── MAIN API ───────────────────────────────────────────
    def generate(
        self,
        query_string: str,
        body: str = "",
        user_agent: str = USERAGENT,
        envcode: int = 0,
        version: str = "5.1.1",
    ) -> str:
        timestamp_ms = int(time() * 1000)

        obj = {
            1: 1,
            2: envcode,
            3: md5(query_string.encode()).hexdigest(),
            4: md5(body.encode()).hexdigest(),
            5: md5(user_agent.encode()).hexdigest(),
            6: timestamp_ms // 1000,
            7: 1508145731,
            8: int((timestamp_ms * 1000) % 2147483648),
            9: version,
        }

        if version == "5.1.1":
            obj[10] = "1.0.0.314"
            obj[11] = 1
            v12 = 0
            for i in range(1, 12):
                v = obj[i]
                to_xor = v if isinstance(v, int) else self._be_int_from_str(v)
                v12 ^= to_xor
            obj[12] = v12 & self._MASK32
        elif version != "5.1.0":
            raise ValueError(f"Unsupported version: {version}")

        v0 = 0
        for i in range(1, len(obj) + 1):
            v = obj[i]
            if isinstance(v, int):
                v0 ^= v
        obj[0] = v0 & self._MASK32

        payload = [len(obj)]
        for k, v in obj.items():
            payload.append(k)
            val_bytes = (
                self._num_to_bytes(v) if isinstance(v, int) else list(v.encode("utf-8"))
            )
            payload.extend(self._num_to_bytes(len(val_bytes)))
            payload.extend(val_bytes)
        base_str = "".join(chr(x) for x in payload)

        key_words = []
        key_bytes = []
        round_accum = 0
        for _ in range(12):
            word = int(self.rand() * 4294967296) & self._MASK32
            key_words.append(word)
            round_accum = (round_accum + (word & 15)) & 15
            key_bytes.extend(
                [
                    word & 0xFF,
                    (word >> 8) & 0xFF,
                    (word >> 16) & 0xFF,
                    (word >> 24) & 0xFF,
                ]
            )
        rounds = round_accum + 5

        enc = self._ab22(key_words, rounds, base_str)

        insert_pos = 0
        for b in key_bytes:
            insert_pos = (insert_pos + b) % (len(enc) + 1)
        for ch in enc:
            insert_pos = (insert_pos + ord(ch)) % (len(enc) + 1)

        key_bytes_str = "".join(chr(b) for b in key_bytes)
        final_str = (
            chr(((1 << 6) ^ (1 << 3) ^ 3) & 0xFF)
            + enc[:insert_pos]
            + key_bytes_str
            + enc[insert_pos:]
        )

        out = []
        full_len = (len(final_str) // 3) * 3
        for i in range(0, full_len, 3):
            block = (
                (ord(final_str[i]) << 16)
                | (ord(final_str[i + 1]) << 8)
                | ord(final_str[i + 2])
            )
            out.extend(
                [
                    self._BASE64_ALPHABET[(block >> 18) & 63],
                    self._BASE64_ALPHABET[(block >> 12) & 63],
                    self._BASE64_ALPHABET[(block >> 6) & 63],
                    self._BASE64_ALPHABET[block & 63],
                ]
            )

        return "".join(out)
```

## File: `src/encrypt/__init__.py`
```python
from .aBogus import ABogus
from .device_id import DeviceId
from .msToken import MsToken, MsTokenTikTok
from .ttWid import TtWid, TtWidTikTok
from .verifyFp import VerifyFp
from .webID import WebId
from .xBogus import XBogus, XBogusTikTok
from .xGnarly import XGnarly
```

## File: `src/extract/extractor.py`
```python
from datetime import datetime
from json import dumps
from time import localtime, strftime
from types import SimpleNamespace
from typing import TYPE_CHECKING
from urllib.parse import urlparse

from ..custom import (
    AUTHOR_COVER_INDEX,
    AUTHOR_COVER_URL_INDEX,
    AVATAR_LARGER_INDEX,
    BITRATE_INFO_TIKTOK_INDEX,
    COMMENT_IMAGE_INDEX,
    COMMENT_IMAGE_LIST_INDEX,
    COMMENT_STICKER_INDEX,
    DYNAMIC_COVER_INDEX,
    HOT_WORD_COVER_INDEX,
    IMAGE_INDEX,
    IMAGE_TIKTOK_INDEX,
    LIVE_COVER_INDEX,
    LIVE_DATA_INDEX,
    MUSIC_COLLECTION_COVER_INDEX,
    MUSIC_COLLECTION_DOWNLOAD_INDEX,
    MUSIC_INDEX,
    SEARCH_AVATAR_INDEX,
    SEARCH_USER_INDEX,
    STATIC_COVER_INDEX,
    VIDEO_INDEX,
    VIDEO_TIKTOK_INDEX,
    condition_filter,
)
from ..tools import DownloaderError
from ..translation import _

if TYPE_CHECKING:
    from datetime import date

    from ..config import Parameter

__all__ = ["Extractor"]


class Extractor:
    statistics_keys = (
        "digg_count",
        "comment_count",
        "collect_count",
        "share_count",
        "play_count",
    )
    statistics_keys_tiktok = (
        "diggCount",
        "commentCount",
        "collectCount",
        "shareCount",
        "playCount",
    )
    detail_necessary_keys = "id"
    comment_necessary_keys = "cid"
    user_necessary_keys = "sec_uid"
    extract_params_tiktok = {
        "sec_uid": "author.secUid",
        "mix_id": "playlistId",
        "uid": "author.id",
        "nickname": "author.nickname",
        "mix_title": "playlistId",  # TikTok 不返回合辑标题
    }
    extract_params = {
        "sec_uid": "author.sec_uid",
        "mix_id": "mix_info.mix_id",
        "uid": "author.uid",
        "nickname": "author.nickname",
        "mix_title": "mix_info.mix_name",
    }

    def __init__(self, params: "Parameter"):
        self.log = params.logger
        self.date_format = params.date_format
        self.cleaner = params.CLEANER
        self.type = {
            "batch": self.__batch,
            "detail": self.__detail,
            "comment": self.__comment,
            "live": self.__live,
            "user": self.__user,
            "search": self.__search,
            "hot": self.__hot,
            "music": self.__music,
        }

    def get_user_info(self, data: dict) -> dict:
        try:
            return {
                "nickname": data["nickname"],
                "sec_uid": data["sec_uid"],
                "uid": data["uid"],
            }
        except (KeyError, TypeError):
            self.log.error(_("提取账号信息失败: {data}").format(data=data))
            return {}

    def get_user_info_tiktok(self, data: dict) -> dict:
        try:
            return {
                "nickname": data["user"]["nickname"],
                "sec_uid": data["user"]["secUid"],
                "uid": data["user"]["id"],
            }
        except (KeyError, TypeError):
            self.log.error(_("提取账号信息失败: {data}").format(data=data))
            return {}

    @staticmethod
    def generate_data_object(
        data: dict | list,
    ) -> SimpleNamespace | list[SimpleNamespace]:
        def depth_conversion(element):
            if isinstance(element, dict):
                return SimpleNamespace(
                    **{k: depth_conversion(v) for k, v in element.items()}
                )
            elif isinstance(element, list):
                return [depth_conversion(item) for item in element]
            else:
                return element

        return depth_conversion(data)

    @staticmethod
    def safe_extract(
        data: SimpleNamespace | list[SimpleNamespace],
        attribute_chain: str,
        default: str | int | list | dict | SimpleNamespace = "",
    ):
        attributes = attribute_chain.split(".")
        for attribute in attributes:
            if "[" in attribute:
                parts = attribute.split("[", 1)
                attribute = parts[0]
                index = parts[1].split("]", 1)[0]
                try:
                    index = int(index)
                    data = getattr(data, attribute, None)[index]
                except (IndexError, TypeError, ValueError):
                    return default
            else:
                data = getattr(data, attribute, None)
                if not data:
                    return default
        return data or default

    async def run(
        self,
        data: list[dict],
        recorder,
        type_="detail",
        tiktok=False,
        **kwargs,
    ) -> list[dict]:
        if type_ not in self.type.keys():
            raise DownloaderError
        return await self.type[type_](data, recorder, tiktok, **kwargs)

    async def __batch(
        self,
        data: list[dict],
        recorder,
        tiktok: bool,
        name: str,
        mark: str,
        earliest,
        latest,
        same=True,
    ) -> list[dict]:
        """批量下载作品"""
        container = SimpleNamespace(
            all_data=[],
            template={
                "collection_time": datetime.now().strftime(self.date_format),
            },
            cache=None,
            name=name,
            mark=mark,
            same=same,  # 是否相同作者
            earliest=earliest,
            latest=latest,
        )
        self.__platform_classify_detail(
            data,
            container,
            tiktok,
        )
        container.all_data = self.__clean_extract_data(
            container.all_data,
            self.detail_necessary_keys,
        )
        self.__extract_item_records(container.all_data)
        await self.__record_data(recorder, container.all_data)
        self.__date_filter(container)
        self.__condition_filter(container)
        self.__summary_detail(container.all_data)
        return container.all_data

    @staticmethod
    def __condition_filter(
        container: SimpleNamespace,
    ):
        """自定义筛选作品"""
        result = [i for i in container.all_data if condition_filter(i)]
        container.all_data = result

    def __summary_detail(
        self,
        data: list[dict],
    ):
        """汇总作品数量"""
        self.log.info(_("筛选处理后作品数量: {count}").format(count=len(data)))

    def __extract_batch(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
    ) -> None:
        """批量提取作品信息"""
        container.cache = container.template.copy()
        self.__extract_detail_info(container.cache, data)
        self.__extract_account_info(container, data)
        self.__extract_music(container.cache, data)
        self.__extract_statistics(container.cache, data)
        self.__extract_tags(container.cache, data)
        self.__extract_extra_info(container.cache, data)
        self.__extract_additional_info(container.cache, data)
        container.all_data.append(container.cache)

    def __extract_batch_tiktok(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
    ) -> None:
        """批量提取作品信息"""
        container.cache = container.template.copy()
        self.__extract_detail_info_tiktok(container.cache, data)
        self.__extract_account_info_tiktok(container, data)
        self.__extract_music(container.cache, data, True)
        self.__extract_statistics_tiktok(container.cache, data)
        self.__extract_tags_tiktok(container.cache, data)
        self.__extract_extra_info_tiktok(container.cache, data)
        self.__extract_additional_info(container.cache, data, True)
        container.all_data.append(container.cache)

    def __extract_extra_info(
        self,
        item: dict,
        data: SimpleNamespace,
    ):
        if e := self.safe_extract(data, "anchor_info"):
            extra = dumps(e, ensure_ascii=False, indent=2, default=lambda x: vars(x))
        else:
            extra = ""
        item["extra"] = extra

    def __extract_extra_info_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
    ):
        # TODO: 尚未适配 TikTok 额外信息
        item["extra"] = ""

    def __extract_commodity_data(
        self,
        item: dict,
        data: SimpleNamespace,
    ):
        pass

    def __extract_game_data(
        self,
        item: dict,
        data: SimpleNamespace,
    ):
        pass

    def __extract_description(self, data: SimpleNamespace) -> str:
        # 2023/11/11: 抖音不再折叠过长的作品描述
        return self.safe_extract(data, "desc")
        # if len(desc := self.safe_extract(data, "desc")) < 107:
        #     return desc
        # long_desc = self.safe_extract(data, "share_info.share_link_desc")
        # return long_desc.split(
        #     "  ", 1)[-1].split("  %s", 1)[0].replace("# ", "#")

    def __clean_description(self, desc: str) -> str:
        return self.cleaner.clear_spaces(self.cleaner.filter(desc))

    def __format_date(
        self,
        data: int,
    ) -> str:
        return strftime(
            self.date_format,
            localtime(data or None),
        )

    def __extract_detail_info(
        self,
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        item["id"] = self.safe_extract(data, "aweme_id")
        item["desc"] = (
            self.__clean_description(
                self.__extract_description(data),
            )
            or item["id"]
        )
        item["create_timestamp"] = self.safe_extract(data, "create_time")
        item["create_time"] = self.__format_date(item["create_timestamp"])
        self.__extract_text_extra(item, data)
        self.__classifying_detail(item, data)

    def __extract_detail_info_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        item["id"] = self.safe_extract(data, "id")
        item["desc"] = (
            self.__clean_description(self.__extract_description(data)) or item["id"]
        )
        item["create_timestamp"] = self.safe_extract(
            data,
            "createTime",
        )
        item["create_time"] = self.__format_date(item["create_timestamp"])
        self.__extract_text_extra_tiktok(item, data)
        self.__classifying_detail_tiktok(item, data)

    def __classifying_detail(
        self,
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        # 作品分类
        if images := self.safe_extract(data, "images"):
            self.__extract_image_info(item, data, images)
        else:
            self.__extract_video_info(
                item,
                data,
                _("视频"),
            )

    def __classifying_detail_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        if images := self.safe_extract(data, "imagePost.images"):
            self.__extract_image_info_tiktok(item, data, images)
        else:
            self.__extract_video_info_tiktok(
                item,
                data,
                _("视频"),
            )

    def __extract_additional_info(
        self,
        item: dict,
        data: SimpleNamespace,
        tiktok=False,
    ):
        # item["ratio"] = self.safe_extract(data, "video.ratio")
        item["share_url"] = self.__generate_link(
            item["type"],
            item["id"],
            item["unique_id"] if tiktok else None,
        )

    @staticmethod
    def __generate_link(
        type_: str,
        id_: str,
        unique_id: str = None,
    ) -> str:
        match bool(unique_id), type_:
            case True, "视频":
                return f"https://www.tiktok.com/@{unique_id}/video/{id_}"
            case True, "图集":
                return f"https://www.tiktok.com/@{unique_id}/photo/{id_}"
            case False, "视频":
                return f"https://www.douyin.com/video/{id_}"
            case False, "图集" | "实况":
                return f"https://www.douyin.com/note/{id_}"
            case _:
                return ""

    @staticmethod
    def __clean_share_url(url: str) -> str:
        if not url:
            return url
        parsed_url = urlparse(url)
        return f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"

    def __extract_image_info(
        self,
        item: dict,
        data: SimpleNamespace,
        images: list[SimpleNamespace],
    ) -> None:
        if any(
            self.safe_extract(
                i,
                "video",
            )
            for i in images
        ):
            self.__set_blank_data(
                item,
                data,
                _("实况"),
            )
            item["downloads"] = [
                self.__classify_slides_item(
                    i,
                )
                for i in images
            ]
        else:
            self.__set_blank_data(
                item,
                data,
                _("图集"),
            )
            item["downloads"] = [
                self.safe_extract(
                    i,
                    f"url_list[{IMAGE_INDEX}]",
                )
                for i in images
            ]

    def __extract_image_info_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
        images: list,
    ) -> None:
        self.__set_blank_data(
            item,
            data,
            _("图集"),
        )
        item["downloads"] = [
            self.safe_extract(
                i,
                f"imageURL.urlList[{IMAGE_TIKTOK_INDEX}]",
            )
            for i in images
        ]

    def __set_blank_data(
        self,
        item: dict,
        data: SimpleNamespace,
        type_=_("图集"),
    ):
        item["type"] = type_
        item["duration"] = "00:00:00"
        item["uri"] = ""
        item["height"] = -1
        item["width"] = -1
        self.__extract_cover(item, data)

    def __extract_video_info(
        self,
        item: dict,
        data: SimpleNamespace,
        type_=_("视频"),
    ) -> None:
        item["type"] = type_
        item["height"], item["width"], item["downloads"] = (
            self.__extract_video_download(
                data,
            )
        )
        item["duration"] = self.time_conversion(
            self.safe_extract(data, "video.duration", 0)
        )
        item["uri"] = self.safe_extract(data, "video.play_addr.uri")
        self.__extract_cover(item, data, True)

    def __classify_slides_item(
        self,
        item: SimpleNamespace,
    ) -> str:
        if self.safe_extract(item, "video"):
            return self.__extract_video_download(
                item,
            )[-1]
        return self.safe_extract(item, f"url_list[{IMAGE_INDEX}]")

    def __extract_video_download(
        self,
        data: SimpleNamespace,
    ) -> tuple[int, int, str]:
        bit_rate: list[SimpleNamespace] = self.safe_extract(
            data,
            "video.bit_rate",
            [],
        )
        try:
            bit_rate: list[tuple[int, int, int, int, int, list[str]]] = [
                (
                    i.FPS,
                    i.bit_rate,
                    i.play_addr.data_size,
                    i.play_addr.height,
                    i.play_addr.width,
                    i.play_addr.url_list,
                )
                for i in bit_rate
            ]
            bit_rate.sort(
                key=lambda x: (
                    max(
                        x[3],
                        x[4],
                    ),
                    x[0],
                    x[1],
                    x[2],
                ),
            )
            return (
                (
                    bit_rate[-1][-3],
                    bit_rate[-1][-2],
                    bit_rate[-1][-1][VIDEO_INDEX],
                )
                if bit_rate
                else (-1, -1, "")
            )
        except AttributeError:
            self.log.error(
                f"视频下载地址解析失败: {data}",
                False,
            )
            height = self.safe_extract(
                bit_rate[0],
                "play_addr.height",
                -1,
            )
            width = self.safe_extract(
                bit_rate[0],
                "play_addr.width",
                -1,
            )
            url = self.safe_extract(
                bit_rate[0],
                f"play_addr.url_list[{VIDEO_INDEX}]",
            )
            return height, width, url

    def __extract_video_info_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
        type_=_("视频"),
    ) -> None:
        item["type"] = type_
        # item["downloads"] = self.safe_extract(
        #     data,
        #     "video.playAddr",
        # )  # 视频文件大小优先
        item["height"], item["width"], item["downloads"] = (
            self.__extract_video_download_tiktok(
                data,
            )
        )  # 视频分辨率优先
        item["duration"] = self.time_conversion_tiktok(
            self.safe_extract(
                data,
                "video.duration",
                0,
            )
        )
        item["uri"] = self.safe_extract(
            data,
            f"video.bitrateInfo[{BITRATE_INFO_TIKTOK_INDEX}].PlayAddr.Uri",
        )
        self.__extract_cover_tiktok(item, data, True)

    def __extract_video_download_tiktok(
        self,
        data: SimpleNamespace,
    ) -> tuple[int, int, str]:
        bitrate_info: list[SimpleNamespace] = self.safe_extract(
            data,
            "video.bitrateInfo",
            [],
        )
        try:
            bitrate_info: list[tuple[int, str, int, int, list[str]]] = [
                (
                    i.Bitrate,
                    i.PlayAddr.DataSize,
                    i.PlayAddr.Height,
                    i.PlayAddr.Width,
                    i.PlayAddr.UrlList,
                )
                for i in bitrate_info
            ]
            bitrate_info.sort(
                key=lambda x: (
                    max(
                        x[2],
                        x[3],
                    ),
                    x[0],
                    x[1],
                ),
            )
            return (
                (
                    bitrate_info[-1][-3],
                    bitrate_info[-1][-2],
                    bitrate_info[-1][-1][VIDEO_TIKTOK_INDEX],
                )
                if bitrate_info
                else (-1, -1, "")
            )
        except AttributeError:
            self.log.error(
                f"视频下载地址解析失败: {data}",
                False,
            )
            height = self.safe_extract(
                bitrate_info[0],
                "PlayAddr.Height",
                -1,
            )
            width = self.safe_extract(
                bitrate_info[0],
                "PlayAddr.Width",
                -1,
            )
            url = self.safe_extract(
                bitrate_info[0],
                f"PlayAddr.UrlList[{VIDEO_TIKTOK_INDEX}]",
            )
            return height, width, url

    @staticmethod
    def time_conversion(time_: int) -> str:
        second = time_ // 1000
        return f"{second // 3600:0>2d}:{second % 3600 // 60:0>2d}:{second % 3600 % 60:0>2d}"

    @staticmethod
    def time_conversion_tiktok(seconds: int) -> str:
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))

    def __extract_text_extra(
        self,
        item: dict,
        data: SimpleNamespace,
    ):
        """作品标签"""
        text = [
            self.safe_extract(i, "hashtag_name")
            for i in self.safe_extract(data, "text_extra", [])
        ]
        item["text_extra"] = [i for i in text if i]

    def __extract_text_extra_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
    ):
        """作品标签"""
        text = [
            self.safe_extract(i, "hashtagName")
            for i in self.safe_extract(data, "textExtra", [])
        ]
        item["text_extra"] = [i for i in text if i]

    def __extract_cover(
        self,
        item: dict,
        data: SimpleNamespace,
        has=False,
    ) -> None:
        if has:
            # 动态封面图链接
            item["dynamic_cover"] = self.safe_extract(
                data, f"video.dynamic_cover.url_list[{DYNAMIC_COVER_INDEX}]"
            )
            # 静态封面图链接
            item["static_cover"] = self.safe_extract(
                data, f"video.cover.url_list[{STATIC_COVER_INDEX}]"
            )
        else:
            item["dynamic_cover"], item["static_cover"] = "", ""

    def __extract_cover_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
        has=False,
    ) -> None:
        if has:
            # 动态封面图链接
            item["dynamic_cover"] = self.safe_extract(data, "video.dynamicCover")
            # 静态封面图链接
            item["static_cover"] = self.safe_extract(data, "video.cover")
        else:
            item["dynamic_cover"], item["static_cover"] = "", ""

    def __extract_music(
        self,
        item: dict,
        data: SimpleNamespace,
        tiktok=False,
    ) -> None:
        if music_data := self.safe_extract(data, "music"):
            if tiktok:
                author = self.safe_extract(music_data, "authorName")
                title = self.safe_extract(music_data, "title")
                url = self.safe_extract(music_data, "playUrl")
            else:
                author = self.safe_extract(music_data, "author")
                title = self.safe_extract(music_data, "title")
                url = self.safe_extract(
                    music_data,
                    f"play_url.url_list[{MUSIC_INDEX}]",
                )  # 部分作品的音乐无法下载

        else:
            author, title, url = "", "", ""
        item["music_author"] = author
        item["music_title"] = title
        item["music_url"] = url

    def __extract_statistics(self, item: dict, data: SimpleNamespace) -> None:
        data = self.safe_extract(data, "statistics")
        for i in self.statistics_keys:
            item[i] = self.safe_extract(
                data,
                i,
                -1,
            )

    def __extract_statistics_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        data = self.safe_extract(data, "stats")
        for i, j in enumerate(self.statistics_keys_tiktok):
            item[self.statistics_keys[i]] = self.safe_extract(
                data,
                j,
                -1,
            )

    def __extract_tags(
        self,
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        if not (t := self.safe_extract(data, "video_tag")):
            item["tag"] = []
        else:
            item["tag"] = [self.safe_extract(i, "tag_name") for i in t]

    def __extract_tags_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        if not (t := self.safe_extract(data, "textExtra")):
            item["tag"] = []
        else:
            item["tag"] = [self.safe_extract(i, "hashtagName") for i in t]

    def __extract_account_info(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
        key="author",
    ) -> None:
        data = self.safe_extract(data, key)
        container.cache["uid"] = self.safe_extract(data, "uid")
        container.cache["sec_uid"] = self.safe_extract(data, "sec_uid")
        # container.cache["short_id"] = self.safe_extract(data, "short_id")
        container.cache["unique_id"] = self.safe_extract(
            data,
            "unique_id",
        )
        container.cache["signature"] = self.safe_extract(data, "signature")
        container.cache["user_age"] = self.safe_extract(data, "user_age", -1)
        self.__extract_nickname_info(container, data)

    def __extract_account_info_tiktok(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
        key="author",
    ) -> None:
        data = self.safe_extract(data, key)
        container.cache["uid"] = self.safe_extract(data, "id")
        container.cache["sec_uid"] = self.safe_extract(data, "secUid")
        container.cache["unique_id"] = self.safe_extract(data, "uniqueId")
        container.cache["signature"] = self.safe_extract(data, "signature")
        container.cache["user_age"] = -1
        self.__extract_nickname_info(container, data)

    def __extract_nickname_info(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
    ) -> None:
        if container.same:
            container.cache["nickname"] = container.name
            container.cache["mark"] = container.mark or container.name
        else:
            name = self.cleaner.filter_name(
                self.safe_extract(data, "nickname", _("已注销账号")),
                default=_("无效账号昵称"),
            )
            container.cache["nickname"] = name
            container.cache["mark"] = name

    def preprocessing_data(
        self,
        data: list[dict] | dict,
        tiktok: bool = False,
        mode: str = ...,
        mark: str = "",
        user_id: str = "",
        mix_id: str = "",
        mix_title: str = "",
        collect_id: str = "",
        collect_name: str = "",
    ) -> tuple[
        str,
        str,
        str,
    ]:
        if isinstance(data, dict):
            info = (
                self.get_user_info_tiktok(data) if tiktok else self.get_user_info(data)
            )
            if user_id != (s := info.get("sec_uid")):
                self.log.error(
                    _("sec_user_id {user_id} 与 {s} 不一致").format(
                        user_id=user_id, s=s
                    ),
                )
                return "", "", ""
            name = self.cleaner.filter_name(
                info["nickname"],
                info["uid"],
            )
            mark = self.cleaner.filter_name(
                mark,
                name,
            )
            return (
                info["uid"],
                name,
                mark,
            )
        elif isinstance(data, list):
            match mode:
                case "post":
                    item = self.__select_item(
                        data,
                        user_id,
                        (self.extract_params_tiktok if tiktok else self.extract_params)[
                            "sec_uid"
                        ],
                    )
                    id_, name, mark = self.__extract_pretreatment_data(
                        item,
                        (self.extract_params_tiktok if tiktok else self.extract_params)[
                            "uid"
                        ],
                        (self.extract_params_tiktok if tiktok else self.extract_params)[
                            "nickname"
                        ],
                        mark,
                    )
                    return id_, name, mark
                case "mix":
                    if tiktok:
                        id_ = mix_id
                        name = self.cleaner.filter_name(
                            mix_title,
                        ).strip()
                        mark = self.cleaner.filter_name(
                            mark,
                            name,
                        ).strip()
                    else:
                        item = self.__select_item(
                            data,
                            mix_id,
                            self.extract_params["mix_id"],
                        )
                        id_, name, mark = self.__extract_pretreatment_data(
                            item,
                            self.extract_params["mix_id"],
                            self.extract_params["mix_title"],
                            mark,
                            mix_title,
                        )
                    return id_, name, mark
                case "collects":
                    collect_name = self.cleaner.filter_name(
                        collect_name,
                        collect_id,
                    )
                    return collect_id, collect_name, collect_name
                case _:
                    raise DownloaderError
        else:
            raise DownloaderError

    def __select_item(
        self,
        data: list[dict],
        id_: str,
        key: str,
    ):
        """从多个数据返回对象"""
        for item in data:
            item = self.generate_data_object(item)
            if id_ == self.safe_extract(item, key):
                return item
        raise DownloaderError(_("提取账号信息或合集信息失败，请向作者反馈！"))

    def __extract_pretreatment_data(
        self,
        item: SimpleNamespace,
        id_: str,
        name: str,
        mark: str,
        title: str = None,  # TikTok 合辑需要直接传入标题
    ):
        id_ = self.safe_extract(item, id_)
        name = self.cleaner.filter_name(
            title
            or self.safe_extract(
                item,
                name,
                id_,
            ),
        )
        mark = self.cleaner.filter_name(
            mark,
            name,
        )
        return id_, name.strip(), mark.strip()

    def __platform_classify_detail(
        self,
        data: list[dict],
        container: SimpleNamespace,
        tiktok: bool,
    ) -> None:
        if tiktok:
            [
                self.__extract_batch_tiktok(
                    container,
                    self.generate_data_object(item),
                )
                for item in data
            ]
        else:
            [
                self.__extract_batch(
                    container,
                    self.generate_data_object(item),
                )
                for item in data
            ]

    async def __detail(
        self,
        data: list[dict],
        recorder,
        tiktok: bool,
    ) -> list[dict]:
        container = SimpleNamespace(
            all_data=[],
            template={
                "collection_time": datetime.now().strftime(self.date_format),
            },
            cache=None,
            same=False,
        )
        self.__platform_classify_detail(
            data,
            container,
            tiktok,
        )
        container.all_data = self.__clean_extract_data(
            container.all_data, self.detail_necessary_keys
        )
        self.__extract_item_records(container.all_data)
        await self.__record_data(recorder, container.all_data)
        self.__condition_filter(container)
        return container.all_data

    async def __comment(
        self,
        data: list[dict],
        recorder,
        tiktok: bool,
        source=False,
    ) -> list[dict]:
        if not any(data):
            return []
        container = SimpleNamespace(
            all_data=[],
            template={
                "collection_time": datetime.now().strftime(self.date_format),
            },
            cache=None,
            same=False,
        )
        if source:
            container.all_data = data
        else:
            [
                self.__extract_comments_data(container, self.generate_data_object(i))
                for i in data
            ]
            container.all_data = self.__clean_extract_data(
                container.all_data, self.comment_necessary_keys
            )
            await self.__record_data(recorder, container.all_data)
        return container.all_data

    def __extract_comments_data(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
    ):
        container.cache = container.template.copy()
        container.cache["create_timestamp"] = self.safe_extract(data, "create_time")
        container.cache["create_time"] = self.__format_date(
            container.cache["create_timestamp"]
        )
        container.cache["ip_label"] = self.safe_extract(data, "ip_label", "未知")
        container.cache["text"] = self.safe_extract(data, "text")
        container.cache["image"] = self.safe_extract(
            data,
            f"image_list[{COMMENT_IMAGE_LIST_INDEX}].origin_url.url_list[{COMMENT_IMAGE_INDEX}]",
        )
        container.cache["sticker"] = self.safe_extract(
            data, f"sticker.static_url.url_list[{COMMENT_STICKER_INDEX}]"
        )
        container.cache["digg_count"] = self.safe_extract(data, "digg_count", -1)
        container.cache["reply_to_reply_id"] = self.safe_extract(
            data, "reply_to_reply_id"
        )
        container.cache["reply_comment_total"] = self.safe_extract(
            data, "reply_comment_total", 0
        )
        container.cache["reply_id"] = self.safe_extract(data, "reply_id")
        container.cache["cid"] = self.safe_extract(data, "cid")
        self.__extract_account_info(container, data, "user")
        container.all_data.append(container.cache)

    @classmethod
    def extract_reply_ids(cls, data: list[dict]) -> list[str]:
        container = SimpleNamespace(
            reply_ids=[],
            cache=None,
        )
        for item in data:
            item = cls.generate_data_object(item)
            container.cache = {
                "reply_comment_total": cls.safe_extract(
                    item,
                    "reply_comment_total",
                    0,
                ),
                "cid": cls.safe_extract(item, "cid"),
            }
            cls.__filter_reply_ids(container)
        return container.reply_ids

    @staticmethod
    def __filter_reply_ids(container: SimpleNamespace):
        if container.cache["reply_comment_total"] > 0:
            container.reply_ids.append(container.cache["cid"])

    async def __live(
        self,
        data: list[dict],
        recorder,
        tiktok: bool,
        *args,
    ) -> list[dict]:
        container = SimpleNamespace(all_data=[])
        if tiktok:
            [
                self.__extract_live_data_tiktok(container, self.generate_data_object(i))
                for i in data
            ]
        else:
            [
                self.__extract_live_data(container, self.generate_data_object(i))
                for i in data
            ]
        return container.all_data

    def __extract_live_data(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
    ):
        if data := self.safe_extract(
            data, f"data.data[{LIVE_DATA_INDEX}]"
        ) or self.safe_extract(data, "data.room"):
            live_data = {
                "status": self.safe_extract(data, "status"),
                "nickname": self.safe_extract(data, "owner.nickname"),
                "title": self.safe_extract(data, "title"),
                "flv_pull_url": vars(
                    self.safe_extract(
                        data,
                        "stream_url.flv_pull_url",
                        SimpleNamespace(),
                    )
                ),
                "hls_pull_url_map": vars(
                    self.safe_extract(
                        data,
                        "stream_url.hls_pull_url_map",
                        SimpleNamespace(),
                    )
                ),
                "cover": self.safe_extract(data, f"cover.url_list[{LIVE_COVER_INDEX}]"),
                "total_user_str": self.safe_extract(data, "stats.total_user_str"),
                "user_count_str": self.safe_extract(data, "stats.user_count_str"),
            }
            container.all_data.append(live_data)

    def __extract_live_data_tiktok(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
    ):
        data = self.safe_extract(data, "data")
        live_data = {
            "create_time": datetime.fromtimestamp(t)
            if (t := self.safe_extract(data, "create_time"))
            else "未知",
            "id_str": self.safe_extract(data, "id_str"),
            "like_count": self.safe_extract(data, "like_count"),
            "nickname": self.safe_extract(data, "owner.nickname"),
            "display_id": self.safe_extract(data, "owner.display_id"),
            "title": self.safe_extract(data, "title"),
            "user_count": self.safe_extract(data, "user_count"),
            "flv_pull_url": vars(self.safe_extract(data, "stream_url.flv_pull_url")),
            "message": self.safe_extract(data, "message"),
            "prompts": self.safe_extract(data, "prompts"),
        }
        container.all_data.append(live_data)

    async def __user(
        self,
        data: list[dict],
        recorder,
        tiktok: bool,
    ) -> list[dict]:
        container = SimpleNamespace(
            all_data=[],
            cache=None,
            template={
                "collection_time": datetime.now().strftime(self.date_format),
            },
        )
        [
            self.__extract_user_data(container, self.generate_data_object(i))
            for i in data
        ]
        container.all_data = self.__clean_extract_data(
            container.all_data, self.user_necessary_keys
        )
        await self.__record_data(recorder, container.all_data)
        return container.all_data

    def __extract_user_data(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
    ):
        container.cache = container.template.copy()
        container.cache["avatar"] = self.safe_extract(
            data, f"avatar_larger.url_list[{AVATAR_LARGER_INDEX}]"
        )
        container.cache["city"] = self.safe_extract(data, "city")
        container.cache["country"] = self.safe_extract(data, "country")
        container.cache["district"] = self.safe_extract(data, "district")
        container.cache["favoriting_count"] = self.safe_extract(
            data, "favoriting_count", -1
        )
        container.cache["follower_count"] = self.safe_extract(
            data, "follower_count", -1
        )
        container.cache["max_follower_count"] = self.safe_extract(
            data, "max_follower_count", -1
        )
        container.cache["following_count"] = self.safe_extract(
            data, "following_count", -1
        )
        container.cache["total_favorited"] = self.safe_extract(
            data, "total_favorited", -1
        )
        container.cache["gender"] = {1: "男", 2: "女"}.get(
            self.safe_extract(data, "gender"),
            "未知",
        )
        container.cache["ip_location"] = self.safe_extract(data, "ip_location")
        container.cache["nickname"] = self.safe_extract(data, "nickname")
        container.cache["province"] = self.safe_extract(data, "province")
        container.cache["school_name"] = self.safe_extract(data, "school_name")
        container.cache["sec_uid"] = self.safe_extract(data, "sec_uid")
        container.cache["signature"] = self.safe_extract(data, "signature")
        container.cache["uid"] = self.safe_extract(data, "uid")
        container.cache["unique_id"] = self.safe_extract(data, "unique_id")
        container.cache["user_age"] = self.safe_extract(data, "user_age", -1)
        container.cache["cover"] = self.safe_extract(
            data, f"cover_url[{AUTHOR_COVER_URL_INDEX}].url_list[{AUTHOR_COVER_INDEX}]"
        )
        container.cache["short_id"] = self.safe_extract(data, "short_id")
        container.cache["aweme_count"] = self.safe_extract(data, "aweme_count", -1)
        container.cache["verify"] = self.safe_extract(data, "custom_verify", "无")
        container.cache["enterprise"] = self.safe_extract(
            data, "enterprise_verify_reason", "无"
        )
        container.cache["url"] = (
            f"https://www.douyin.com/user/{container.cache['sec_uid']}"
        )
        container.all_data.append(container.cache)

    async def __search(
        self,
        data: list[dict],
        recorder,
        tiktok: bool,
        tab: int,
    ) -> list[dict]:
        if tab in {0, 1}:
            return await self.__search_general(data, recorder)
        elif tab == 2:
            return await self.__search_user(data, recorder)
        elif tab == 3:
            return await self.__search_live(data, recorder)

    async def __search_general(
        self,
        data: list[dict],
        recorder,
    ) -> list[dict]:
        container = SimpleNamespace(
            all_data=[],
            cache=None,
            template={
                "collection_time": datetime.now().strftime(self.date_format),
            },
            same=False,
        )
        [
            self.__search_result_classify(container, self.generate_data_object(i))
            for i in data
        ]
        await self.__record_data(recorder, container.all_data)
        return container.all_data

    def __search_result_classify(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
    ):
        if d := self.safe_extract(data, "aweme_info"):
            self.__extract_batch(container, d)
        elif d := self.safe_extract(data, "aweme_mix_info.mix_items"):
            [self.__extract_batch(container, i) for i in d]
        elif d := self.safe_extract(data, "card_info.attached_info.aweme_list"):
            [self.__extract_batch(container, i) for i in d]
        elif d := self.safe_extract(data, f"user_list[{SEARCH_USER_INDEX}].items"):
            [self.__extract_batch(container, i) for i in d]
        # elif d := self.safe_extract(data, "user_list.user_info"):
        #     pass
        # elif d := self.safe_extract(data, "music_list"):
        #     pass
        # elif d := self.safe_extract(data, "common_aladdin"):
        #     pass
        else:
            self.log.error(f"Unreported search results: {data}", False)

    async def __search_user(
        self,
        data: list[dict],
        recorder,
    ) -> list[dict]:
        container = SimpleNamespace(
            all_data=[],
            cache=None,
            template={
                "collection_time": datetime.now().strftime(self.date_format),
            },
        )
        [
            self.__deal_search_user_live(
                container, self.generate_data_object(i["user_info"])
            )
            for i in data
        ]
        await self.__record_data(recorder, container.all_data)
        return container.all_data

    def __deal_search_user_live(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
        user=True,
    ):
        if user:
            container.cache = container.template.copy()
        container.cache["avatar"] = self.safe_extract(
            data,
            f"{'avatar_thumb' if user else 'avatar_larger'}.url_list[{SEARCH_AVATAR_INDEX}]",
        )
        container.cache["nickname"] = self.safe_extract(data, "nickname")
        container.cache["sec_uid"] = self.safe_extract(data, "sec_uid")
        container.cache["signature"] = self.safe_extract(data, "signature")
        container.cache["uid"] = self.safe_extract(data, "uid")
        container.cache["short_id"] = self.safe_extract(data, "short_id")
        container.cache["verify"] = self.safe_extract(data, "custom_verify", "无")
        container.cache["enterprise"] = self.safe_extract(
            data, "enterprise_verify_reason", "无"
        )
        if user:
            container.cache["follower_count"] = self.safe_extract(
                data, "follower_count", -1
            )
            container.cache["total_favorited"] = self.safe_extract(
                data, "total_favorited", -1
            )
            container.cache["unique_id"] = self.safe_extract(data, "unique_id")
            container.all_data.append(container.cache)
        # else:
        #     pass

    async def __search_live(
        self,
        data: list[dict],
        recorder,
    ) -> list[dict]:
        container = SimpleNamespace(
            all_data=[],
            cache=None,
            template={
                "collection_time": datetime.now().strftime(self.date_format),
            },
        )
        [self.__deal_search_live(container, self.generate_data_object(i)) for i in data]
        await self.__record_data(recorder, container.all_data)
        return container.all_data

    def __deal_search_live(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
    ):
        container.cache = container.template.copy()
        self.__deal_search_user_live(
            container, self.safe_extract(data, "author"), False
        )
        container.cache["room_id"] = self.safe_extract(data, "aweme_id")
        container.all_data.append(container.cache)

    async def __hot(
        self,
        data: list[dict],
        recorder,
        tiktok: bool,
    ) -> list[dict]:
        all_data = []
        [self.__deal_hot_data(all_data, self.generate_data_object(i)) for i in data]
        await self.__record_data(recorder, all_data)
        return all_data

    def __deal_hot_data(self, container: list, data: SimpleNamespace):
        cache = {
            "position": str(self.safe_extract(data, "position", -1)),
            "sentence_id": self.safe_extract(data, "sentence_id"),
            "word": self.safe_extract(data, "word"),
            "video_count": str(self.safe_extract(data, "video_count", -1)),
            "event_time": self.__format_date(self.safe_extract(data, "event_time")),
            "view_count": str(self.safe_extract(data, "view_count", -1)),
            "hot_value": str(self.safe_extract(data, "hot_value", -1)),
            "cover": self.safe_extract(
                data, f"word_cover.url_list[{HOT_WORD_COVER_INDEX}]"
            ),
        }
        container.append(cache)

    async def __record_data(self, record, data: list[dict]):
        # 记录数据
        for i in data:
            await record.save(self.__extract_values(record, i))

    @staticmethod
    def __extract_values(record, data: dict) -> list:
        return [data[key] for key in record.field_keys]

    @staticmethod
    def __date_filter(container: SimpleNamespace):
        # print("前", len(container.all_data))  # 调试代码
        result = []
        for item in container.all_data:
            create_time = datetime.fromtimestamp(item["create_timestamp"]).date()
            if container.earliest <= create_time <= container.latest:
                result.append(item)
            # else:
            #     print("丢弃", item)  # 调试代码
        # print("后", len(result))  # 调试代码
        container.all_data = result

    def source_date_filter(
        self,
        data: list[dict],
        earliest: "date",
        latest: "date",
        tiktok=False,
    ) -> list[dict]:
        if tiktok:
            return self.__source_date_filter(
                data,
                "createTime",
                earliest=earliest,
                latest=latest,
            )
        return self.__source_date_filter(
            data,
            earliest=earliest,
            latest=latest,
        )

    def __source_date_filter(
        self,
        data: list[dict],
        key: str = "create_time",
        earliest: "date" = ...,
        latest: "date" = ...,
    ) -> list[dict]:
        result = []
        for item in data:
            if not (create_time := item.get(key, 0)):
                result.append(item)
                continue
            create_time = datetime.fromtimestamp(create_time).date()
            if earliest <= create_time <= latest:
                result.append(item)
        self.__summary_detail(result)
        return result

    @classmethod
    def extract_mix_id(cls, data: dict) -> str:
        data = cls.generate_data_object(data)
        return cls.safe_extract(data, "mix_info.mix_id")

    def __extract_item_records(self, data: list[dict]):
        # 记录提取成功的条目
        for i in data:
            self.log.info(f"{i['type']} {i['id']} 数据提取成功", False)

    @classmethod
    def extract_mix_collect_info(cls, data: list[dict]) -> list[dict]:
        data = cls.generate_data_object(data)
        return [
            {
                "title": Extractor.safe_extract(i, "mix_name"),
                "id": Extractor.safe_extract(i, "mix_id"),
            }
            for i in data
        ]

    @classmethod
    def extract_collects_info(cls, data: list[dict]) -> list[dict]:
        data = cls.generate_data_object(data)
        return [
            {
                "name": Extractor.safe_extract(i, "collects_name"),
                "id": Extractor.safe_extract(i, "collects_id_str"),
            }
            for i in data
        ]

    @staticmethod
    def __clean_extract_data(data: list[dict], key: str) -> list[dict]:
        # 去除无效数据
        return [i for i in data if i.get(key)]

    async def __music(
        self,
        data: list[dict],
        recorder,
        tiktok=False,
    ) -> list[dict]:
        """暂不记录收藏音乐数据"""
        container = SimpleNamespace(
            all_data=[],
            template={
                "collection_time": datetime.now().strftime(self.date_format),
            },
            cache=None,
            same=False,
        )
        [
            self.__extract_collection_music(
                container,
                self.generate_data_object(item),
            )
            for item in data
        ]
        return container.all_data

    def __extract_collection_music(
        self,
        container: SimpleNamespace,
        data: SimpleNamespace,
    ):
        container.cache = container.template.copy()
        container.cache["id"] = self.safe_extract(data, "id_str")
        container.cache["title"] = self.safe_extract(data, "title")
        container.cache["author"] = self.safe_extract(data, "author")
        container.cache["album"] = self.safe_extract(data, "album")
        container.cache["cover"] = self.safe_extract(
            data, f"cover_hd.url_list[{MUSIC_COLLECTION_COVER_INDEX}]"
        )
        container.cache["download"] = self.safe_extract(
            data, f"play_url.url_list[{MUSIC_COLLECTION_DOWNLOAD_INDEX}]"
        )
        container.cache["duration"] = self.time_conversion(
            self.safe_extract(data, "duration", 0)
        )
        container.all_data.append(container.cache)
```

## File: `src/extract/__init__.py`
```python
from .extractor import Extractor

__all__ = ["Extractor"]
```

## File: `src/interface/account.py`
```python
from datetime import date, datetime, timedelta
from typing import TYPE_CHECKING, Callable, Coroutine, Type, Union

from src.interface.template import API
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class Account(API):
    post_api = f"{API.domain}aweme/v1/web/aweme/post/"
    favorite_api = f"{API.domain}aweme/v1/web/aweme/favorite/"

    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        sec_user_id: str = ...,
        tab="post",
        earliest: str | float | int = "",
        latest: str | float | int = "",
        pages: int = None,
        cursor=0,
        count=18,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.sec_user_id = sec_user_id
        self.api, self.favorite, self.pages = self.check_type(
            tab, pages or params.max_pages
        )
        # TODO: 重构数据验证逻辑
        self.latest: date = self.check_latest(latest)
        self.earliest: date = self.check_earliest(earliest)
        self.cursor = cursor
        self.count = count
        self.text = _("账号喜欢作品") if self.favorite else _("账号发布作品")

    async def run(
        self,
        referer: str = None,
        single_page=False,
        data_key: str = "aweme_list",
        error_text="",
        cursor="max_cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        if self.favorite:
            self.set_referer(f"{self.domain}user/{self.sec_user_id}?showTab=like")
        else:
            self.set_referer(f"{self.domain}user/{self.sec_user_id}")
        match single_page:
            case True:
                await self.run_single(
                    data_key,
                    error_text
                    or _(
                        "该账号为私密账号，需要使用登录后的 Cookie，且登录的账号需要关注该私密账号"
                    ),
                    cursor,
                    has_more,
                    params,
                    data,
                    method,
                    headers,
                    *args,
                    **kwargs,
                )
                return self.response
            case False:
                await self.run_batch(
                    data_key,
                    error_text
                    or _(
                        "该账号为私密账号，需要使用登录后的 Cookie，且登录的账号需要关注该私密账号"
                    ),
                    cursor,
                    has_more,
                    params,
                    data,
                    method,
                    headers,
                    *args,
                    **kwargs,
                )
                return self.response, self.earliest, self.latest
        raise ValueError

    async def run_single(
        self,
        data_key: str = "aweme_list",
        error_text="",
        cursor="max_cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        await super().run_single(
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )

    async def run_batch(
        self,
        data_key: str = "aweme_list",
        error_text="",
        cursor="max_cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        callback: Type[Coroutine] = None,
        *args,
        **kwargs,
    ):
        await super().run_batch(
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            callback=callback or self.early_stop,
            *args,
            **kwargs,
        )
        self.summary_works()

    async def early_stop(self):
        """如果获取数据的发布日期已经早于限制日期，就不需要再获取下一页的数据了"""
        if (
            not self.favorite
            and self.earliest
            > datetime.fromtimestamp(max(int(self.cursor) / 1000, 0)).date()
        ):
            self.finished = True

    def generate_params(
        self,
    ) -> dict:
        match self.favorite:
            case True:
                return self.generate_favorite_params()
            case False:
                return self.generate_post_params()
        return {}

    def generate_favorite_params(self) -> dict:
        return self.params | {
            "sec_user_id": self.sec_user_id,
            "max_cursor": self.cursor,
            "min_cursor": "0",
            "whale_cut_token": "",
            "cut_version": "1",
            "count": self.count,
            "publish_video_strategy_type": "2",
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    def generate_post_params(self) -> dict:
        return self.params | {
            "sec_user_id": self.sec_user_id,
            "max_cursor": self.cursor,
            "locate_query": "false",
            "show_live_replay_strategy": "1",
            "need_time_list": "1",
            "time_list_query": "0",
            "whale_cut_token": "",
            "cut_version": "1",
            "count": self.count,
            "publish_video_strategy_type": "2",
        }

    def check_type(self, tab: str, pages: int) -> tuple[str, bool, int]:
        match tab:
            case "favorite":
                return self.favorite_api, True, pages
            case "post":
                pass
            case _:
                self.log.warning(
                    _("tab 参数 {tab} 设置错误，程序将使用默认值: post").format(tab=tab)
                )
        return self.post_api, False, 99999

    def check_earliest(self, date_: str | float | int) -> date:
        return self.check_date(date(2016, 9, 20), self.latest, _("最早"), date_)

    def check_latest(self, date_: str | float | int) -> date:
        return self.check_date(date.today(), date.today(), _("最晚"), date_)

    def check_date(
        self, default: date, start: date, tip: str, value: str | float | int
    ) -> date:
        if not value:
            return default
        if isinstance(value, (int, float)):
            date_ = start - timedelta(days=value)
        elif isinstance(value, str):
            try:
                date_ = datetime.strptime(value, "%Y/%m/%d").date()
            except ValueError:
                self.log.warning(
                    _("作品{tip}发布日期无效 {date}").format(tip=tip, date=value)
                )
                return default
        else:
            raise ValueError(
                _("作品{tip}发布日期参数 {date} 类型错误").format(tip=tip, date=value)
            )
        self.log.info(
            _("作品{tip}发布日期: {latest_date}").format(tip=tip, latest_date=date_)
        )
        return date_  # 返回 date 对象

    def check_response(
        self,
        data_dict: dict,
        data_key: str,
        error_text="",
        cursor="cursor",
        has_more="has_more",
        *args,
        **kwargs,
    ):
        try:
            if not (d := data_dict[data_key]):
                self.log.warning(error_text)
                self.finished = True
            else:
                self.cursor = data_dict[cursor]
                self.append_response(d)
                self.finished = not data_dict[has_more]
        except KeyError:
            if data_dict.get("status_code") == 0:
                self.log.warning(_("配置文件 cookie 参数未登录，数据获取已提前结束"))
            else:
                self.log.error(
                    _("数据解析失败，请告知作者处理: {data}").format(data=data_dict)
                )
            self.finished = True


async def test():
    from src.testers import Params

    async with Params() as params:
        i = Account(
            params,
            sec_user_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/account_tiktok.py`
```python
from typing import TYPE_CHECKING, Callable, Coroutine, Type, Union

from src.interface.account import Account
from src.interface.template import APITikTok

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class AccountTikTok(
    Account,
    APITikTok,
):
    post_api = f"{APITikTok.domain}api/post/item_list/"
    favorite_api = f"{APITikTok.domain}api/favorite/item_list/"

    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        sec_user_id: str = ...,
        tab="post",
        earliest: str | float | int = "",
        latest: str | float | int = "",
        pages: int = None,
        cursor=0,
        count=16,
        *args,
        **kwargs,
    ):
        super().__init__(
            params,
            cookie,
            proxy,
            sec_user_id,
            tab,
            earliest,
            latest,
            pages,
            cursor,
            count,
            *args,
            **kwargs,
        )

    async def run(
        self,
        referer: str = None,
        single_page=False,
        data_key: str = "itemList",
        error_text="",
        cursor="cursor",
        has_more="hasMore",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        self.set_referer(referer)
        match single_page:
            case True:
                await self.run_single(
                    data_key,
                    error_text=error_text,
                    cursor=cursor,
                    has_more=has_more,
                    params=params,
                    data=data,
                    method=method,
                    headers=headers,
                    *args,
                    **kwargs,
                )
                return self.response
            case False:
                await self.run_batch(
                    data_key,
                    error_text=error_text,
                    cursor=cursor,
                    has_more=has_more,
                    params=params,
                    data=data,
                    method=method,
                    headers=headers,
                    *args,
                    **kwargs,
                )
                return self.response, self.earliest, self.latest
        raise ValueError

    async def run_batch(
        self,
        data_key: str = "itemList",
        error_text="",
        cursor="cursor",
        has_more="hasMore",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        callback: Type[Coroutine] = None,
        *args,
        **kwargs,
    ):
        await super().run_batch(
            data_key=data_key,
            error_text=error_text,
            cursor=cursor,
            has_more=has_more,
            params=params,
            data=data,
            method=method,
            headers=headers,
            callback=callback,
            *args,
            **kwargs,
        )

    def generate_favorite_params(self) -> dict:
        return self.generate_post_params()

    def generate_post_params(self) -> dict:
        return self.params | {
            "secUid": self.sec_user_id,
            "count": self.count,
            "cursor": self.cursor,
            "coverFormat": "2",
            "post_item_list_request_type": "0",
            "needPinnedItemIds": "true",
            "video_encoding": "mp4",
        }


async def test():
    from src.testers import Params

    async with Params() as params:
        AccountTikTok.params["msToken"] = params.msToken_tiktok
        i = AccountTikTok(
            params,
            sec_user_id="",
            earliest=15,
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/collection.py`
```python
from typing import TYPE_CHECKING, Callable, Union

from src.interface.template import API
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class Collection(API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        sec_user_id: str = "",
        count=10,
        cursor=0,
        pages: int = None,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.api = f"{self.domain}aweme/v1/web/aweme/listcollection/"
        self.text = _("账号收藏作品")
        self.count = count
        self.cursor = cursor
        self.pages = pages or params.max_pages
        self.sec_user_id = sec_user_id

    async def run(
        self,
        referer: str = "",
        single_page=False,
        data_key: str = "aweme_list",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="POST",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        await super().run(
            referer or f"{self.domain}user/self?showTab=favorite_collection",
            single_page,
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )
        # await self.get_owner_data()
        return self.response

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "publish_video_strategy_type": "2",
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    def generate_data(
        self,
    ) -> dict:
        return {
            "count": self.count,
            "cursor": self.cursor,
        }

    async def request_data(
        self,
        url: str,
        params: dict = None,
        data: dict = None,
        method="GET",
        headers: dict = None,
        encryption="GET",
        finished=False,
        *args,
        **kwargs,
    ):
        return await super().request_data(
            url,
            params,
            data,
            method,
            headers,
            encryption,
            finished,
            *args,
            **kwargs,
        )


async def test():
    from src.testers import Params

    async with Params() as params:
        c = Collection(
            params,
            pages=1,
        )
        print(await c.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/collects.py`
```python
from typing import TYPE_CHECKING, Callable, Union

from src.interface.collection import Collection
from src.interface.template import API
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class Collects(API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        cursor=0,
        count=10,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}aweme/v1/web/collects/list/"
        self.text = _("收藏夹")

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "cursor": self.cursor,
            "count": self.count,
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    async def run(
        self,
        referer: str = "https://www.douyin.com/user/self?showTab=favorite_collection",
        single_page=False,
        data_key: str = "collects_list",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text or _("当前账号无收藏夹"),
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )


class CollectsDetail(Collection, API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        collects_id: str = ...,
        pages: int = None,
        cursor=0,
        count=10,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, None, *args, **kwargs)
        self.collects_id = collects_id
        self.pages = pages or params.max_pages
        self.api = f"{self.domain}aweme/v1/web/collects/video/list/"
        self.cursor = cursor
        self.count = count
        self.text = _("收藏夹作品")

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "collects_id": self.collects_id,
            "cursor": self.cursor,
            "count": self.count,
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    async def run(
        self,
        referer: str = "https://www.douyin.com/user/self?showTab=favorite_collection",
        single_page=False,
        data_key: str = "aweme_list",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        await super(Collection, self).run(
            referer,
            single_page,
            data_key,
            error_text
            or _("收藏夹 {collects_id} 为空").format(collects_id=self.collects_id),
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )
        return self.response


class CollectsMix(API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        cursor=0,
        count=12,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}aweme/v1/web/mix/listcollection/"
        self.text = _("收藏合集")

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "cursor": self.cursor,
            "count": self.count,
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    async def run(
        self,
        referer: str = "https://www.douyin.com/user/self?showTab=favorite_collection",
        single_page=False,
        data_key: str = "mix_infos",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        proxy: str = None,
        *args,
        **kwargs,
    ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text or _("当前账号无收藏合集"),
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            proxy,
            *args,
            **kwargs,
        )


class CollectsSeries(CollectsMix):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        cursor=0,
        count=12,
        *args,
        **kwargs,
    ):
        super().__init__(
            params,
            cookie,
            proxy,
            *args,
            **kwargs,
        )
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}aweme/v1/web/series/collections/"
        self.text = _("收藏短剧")

    async def run(
        self,
        referer: str = "https://www.douyin.com/user/self?showTab=favorite_collection",
        single_page=False,
        data_key: str = "series_infos",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text or _("当前账号无收藏短剧"),
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )


class CollectsMusic(CollectsMix):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        cursor=0,
        count=20,
        *args,
        **kwargs,
    ):
        super().__init__(
            params,
            cookie,
            proxy,
            *args,
            **kwargs,
        )
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}aweme/v1/web/music/listcollection/"
        self.text = _("收藏音乐")

    async def run(
        self,
        referer: str = "https://www.douyin.com/user/self?showTab=favorite_collection",
        single_page=False,
        data_key: str = "mc_list",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text or _("当前账号无收藏音乐"),
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )


async def test():
    from src.testers import Params

    async with Params() as params:
        c = Collects(
            params,
        )
        print(await c.run())
        c = CollectsDetail(params, collects_id="")
        print(await c.run())
        c = CollectsMix(
            params,
        )
        print(await c.run())
        c = CollectsMusic(
            params,
        )
        print(await c.run())
        c = CollectsSeries(
            params,
        )
        print(await c.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/comment.py`
```python
from typing import TYPE_CHECKING, Callable, Coroutine, Type, Union

from src.extract import Extractor
from src.interface.template import API
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class Comment(API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        detail_id: str = ...,
        pages: int = None,
        cursor: int = 0,
        count: int = 20,
        count_reply: int = 3,
        reply: bool = False,
    ):
        super().__init__(params, cookie, proxy)
        self.params_object = params
        self.cookie = cookie
        self.proxy = proxy
        self.item_id = detail_id
        self.pages = pages or params.max_pages
        self.cursor = cursor
        self.count = count
        self.count_reply = count_reply
        self.api = f"{self.domain}aweme/v1/web/comment/list/"
        self.text = _("作品评论")
        self.current_page = []
        self.progress = None
        self.task_id = None
        self.reply = reply

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "aweme_id": self.item_id,
            "cursor": self.cursor,
            "count": self.count,
            "item_type": "0",
            "insert_ids": "",
            "whale_cut_token": "",
            "cut_version": "1",
            "rcFT": "",
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    async def run(
        self,
        referer: str = None,
        single_page=False,
        data_key: str = "comments",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ) -> list[dict]:
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text=error_text
            or _("作品 {item_id} 无评论").format(item_id=self.item_id),
            cursor=cursor,
            has_more=has_more,
            data=data,
            params=params,
            method=method,
            headers=headers,
            callback=self.run_reply,
            *args,
            **kwargs,
        )

    async def run_batch(
        self,
        data_key: str = "comments",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        callback: Type[Coroutine] = None,
        *args,
        **kwargs,
    ):
        with self.progress_object() as self.progress:
            self.task_id = self.progress.add_task(
                _("正在获取{text}数据").format(text=self.text),
                total=None,
            )
            await self.update_progress(
                data_key,
                error_text,
                cursor,
                has_more,
                params,
                data,
                method,
                headers,
                callback,
                *args,
                **kwargs,
            )

    async def update_progress(
        self,
        data_key: str = "comments",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        callback: Type[Coroutine] = None,
        *args,
        **kwargs,
    ):
        while not self.finished and self.pages > 0:
            self.progress.update(self.task_id)
            await self.run_single(
                data_key,
                error_text,
                cursor,
                has_more,
                params,
                data,
                method,
                headers,
                *args,
                **kwargs,
            )
            self.pages -= 1
            if callback:
                await callback()

    async def run_reply(
        self,
    ):
        if not self.reply:
            return
        reply_ids = Extractor.extract_reply_ids(self.current_page)
        for reply_id in reply_ids:
            reply = Reply(
                self.params_object,
                self.cookie,
                self.proxy,
                self.item_id,
                reply_id,
                self.pages,
                cursor=0,
                count=self.count_reply,
                progress=self.progress,
                task_id=self.task_id,
            )
            self.response.extend(await reply.run())
            if (p := reply.pages) > 1:
                self.pages = p
            else:
                break

    def check_response(
        self,
        data_dict: dict,
        data_key: str,
        error_text="",
        cursor="cursor",
        has_more="has_more",
        *args,
        **kwargs,
    ):
        try:
            if not (d := data_dict[data_key]):
                self.log.info(error_text)
                self.finished = True
            else:
                self.cursor = data_dict[cursor]
                self.current_page = d
                self.append_response(d)
                self.finished = not data_dict[has_more]
        except KeyError:
            self.log.error(
                _("数据解析失败，请告知作者处理: {data}").format(data=data_dict)
            )
            self.finished = True


class Reply(Comment):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        detail_id: str = ...,
        comment_id: str = ...,
        pages: int = None,
        cursor=0,
        count=3,
        progress=None,
        task_id=None,
    ):
        super().__init__(
            params,
            cookie,
            proxy,
        )
        self.item_id = detail_id
        self.comment_id = comment_id
        self.pages = pages or params.max_pages
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}aweme/v1/web/comment/list/reply/"
        self.text = _("作品评论回复")
        self.progress = progress
        self.task_id = task_id

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "item_id": self.item_id,
            "comment_id": self.comment_id,
            "cut_version": "1",
            "cursor": self.cursor,
            "count": self.count,
            "item_type": "0",
            "version_code": "170400",
            "version_name": "17.4.0",
            "support_h265": "0",
            "support_dash": "0",
        }

    async def run(
        self,
        referer: str = None,
        single_page=False,
        data_key: str = "comments",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        return await super(Comment, self).run(
            referer,
            single_page=single_page,
            data_key=data_key,
            error_text=error_text
            or _("评论 {comment_id} 无回复").format(comment_id=self.comment_id),
            cursor=cursor,
            has_more=has_more,
            params=params,
            data=data,
            method=method,
            headers=headers,
            *args,
            **kwargs,
        )

    async def run_batch(
        self,
        data_key: str = "comments",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        callback: Type[Coroutine] = None,
        *args,
        **kwargs,
    ):
        if not self.progress:
            return await super(Comment, self).run_batch(
                data_key,
                error_text,
                cursor,
                has_more,
                params,
                data,
                method,
                headers,
                callback,
                *args,
                **kwargs,
            )
        return await self.update_progress(
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            callback,
            *args,
            **kwargs,
        )

    def check_response(
        self,
        data_dict: dict,
        data_key: str,
        error_text="",
        cursor="cursor",
        has_more="has_more",
        *args,
        **kwargs,
    ):
        return super(Comment, self).check_response(
            data_dict,
            data_key,
            error_text,
            cursor,
            has_more,
            *args,
            **kwargs,
        )


async def test():
    from src.testers import Params

    async with Params() as params:
        i = Comment(
            params,
            detail_id="",
        )
        print(await i.run())
        i = Reply(
            params,
            detail_id="",
            comment_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/comment_tiktok.py`
```python
from typing import TYPE_CHECKING, Union

from src.interface.comment import Comment, Reply
from src.interface.template import APITikTok
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class CommentTikTok(Comment, APITikTok):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        detail_id: str = ...,
        pages: int = None,
        cursor=0,
        count=20,
        count_reply=3,
    ):
        super().__init__(
            params, cookie, proxy, detail_id, pages, cursor, count, count_reply
        )
        self.api = f"{self.domain}api/comment/list/"
        self.text = _("作品评论")

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "aweme_id": self.item_id,
            "count": self.count,
            "cursor": self.cursor,
            "enter_from": "tiktok_web",
            "is_non_personalized": "false",
            "fromWeb": "1",
            "from_page": "video",
        }


class ReplyTikTok(Reply, CommentTikTok, APITikTok):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        detail_id: str = "",
        comment_id: str = "",
        pages: int = None,
        cursor=0,
        count=3,
        progress=None,
        task_id=None,
    ):
        super().__init__(
            params,
            cookie,
            proxy,
            detail_id,
            comment_id,
            pages,
            cursor,
            count,
            progress,
            task_id,
        )
        self.api = f"{self.domain}api/comment/list/reply/"

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "comment_id": self.comment_id,
            "count": self.count,
            "cursor": self.cursor,
            "fromWeb": "1",
            "from_page": "video",
            "item_id": self.item_id,
        }


async def test():
    from src.testers import Params

    async with Params() as params:
        CommentTikTok.params["msToken"] = params.msToken_tiktok
        ReplyTikTok.params["msToken"] = params.msToken_tiktok
        i = CommentTikTok(
            params,
            detail_id="",
        )
        print(await i.run())
        i = ReplyTikTok(
            params,
            detail_id="",
            comment_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/detail.py`
```python
from typing import Callable
from typing import TYPE_CHECKING
from typing import Union

from src.interface.template import API
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class Detail(API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        detail_id: str = ...,
    ):
        super().__init__(params, cookie, proxy)
        self.detail_id = detail_id
        self.api = f"{self.domain}aweme/v1/web/aweme/detail/"
        self.text = _("作品")

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "aweme_id": self.detail_id,
            "version_code": "190500",
            "version_name": "19.5.0",
        }

    async def run(
        self,
        referer: str = None,
        single_page=True,
        data_key: str = "aweme_detail",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )

    def check_response(
        self,
        data_dict: dict,
        data_key: str,
        error_text="",
        cursor="cursor",
        has_more="has_more",
        *args,
        **kwargs,
    ):
        try:
            if not (d := data_dict[data_key]):
                self.log.warning(error_text)
            else:
                self.response = d
        except KeyError:
            self.log.error(
                _("数据解析失败，请告知作者处理: {data}").format(data=data_dict)
            )


async def test():
    from src.testers import Params

    async with Params() as params:
        i = Detail(
            params,
            detail_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/detail_tiktok.py`
```python
from typing import TYPE_CHECKING, Callable, Union

from src.interface.template import APITikTok
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class DetailTikTok(APITikTok):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        detail_id: str = ...,
    ):
        super().__init__(params, cookie, proxy)
        self.detail_id = detail_id
        self.api = f"{self.domain}/api/item/detail/"
        self.text = _("作品")

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "itemId": self.detail_id,
        }

    async def run(
        self,
        referer: str = None,
        single_page=True,
        data_key: str = None,
        error_text="",
        cursor=None,
        has_more=None,
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )

    def check_response(
        self,
        data_dict: dict,
        data_key: str = None,
        error_text="",
        cursor=None,
        has_more=None,
        *args,
        **kwargs,
    ):
        try:
            if not (d := data_dict["itemInfo"]["itemStruct"]):
                self.log.info(error_text)
            else:
                self.response = d
        except KeyError:
            self.log.error(
                _("数据解析失败，请告知作者处理: {data}").format(data=data_dict)
            )


async def test():
    from src.testers import Params

    async with Params() as params:
        DetailTikTok.params["msToken"] = params.msToken_tiktok
        i = DetailTikTok(
            params,
            detail_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/hashtag.py`
```python
from typing import TYPE_CHECKING
from typing import Union

from src.interface.template import API

# from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class HashTag(API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)

    async def run(self, *args, **kwargs):
        pass


async def test():
    from src.testers import Params

    async with Params() as params:
        i = HashTag(
            params,
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/hot.py`
```python
from datetime import datetime
from types import SimpleNamespace
from typing import Callable
from typing import TYPE_CHECKING
from typing import Union

from src.interface.template import API
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class Hot(API):
    board_params = (
        SimpleNamespace(
            name=_("抖音热榜"),
            type=0,
            sub_type="",
        ),
        SimpleNamespace(
            name=_("娱乐榜"),
            type=2,
            sub_type=2,
        ),
        SimpleNamespace(
            name=_("社会榜"),
            type=2,
            sub_type=4,
        ),
        SimpleNamespace(
            name=_("挑战榜"),
            type=2,
            sub_type="hotspot_challenge",
        ),
    )

    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.headers = self.headers | {
            "Cookie": "",
        }
        self.api = f"{self.domain}aweme/v1/web/hot/search/list/"
        self.text = _("热榜")
        self.index = None
        self.time = None

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "detail_list": "1",
            "source": "6",
            "board_type": self.board_params[self.index].type,
            "board_sub_type": self.board_params[self.index].sub_type,
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    async def run(
        self,
        referer: str = "https://www.douyin.com/discover",
        single_page=True,
        data_key: str = None,
        error_text=None,
        cursor=None,
        has_more=None,
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        self.time = f"{datetime.now():%Y_%m_%d_%H_%M_%S}"
        self.set_referer(referer)
        for index, space in enumerate(self.board_params):
            self.index = index
            self.text = _("{space_name}数据").format(space_name=space.name)
            await self.run_single(
                data_key,
                "",
                cursor,
                has_more,
                params=self.generate_params,
                data=data,
                method=method,
                headers=headers,
                index=index,
                *args,
                **kwargs,
            )
        return self.time, self.response

    def check_response(
        self,
        data_dict: dict,
        data_key: str = None,
        error_text=None,
        cursor=None,
        has_more=None,
        index: int = None,
        *args,
        **kwargs,
    ):
        try:
            if not (d := data_dict["data"]["word_list"]):
                self.log.info(error_text)
            else:
                self.response.append((index, d))
        except KeyError:
            self.log.error(
                _("数据解析失败，请告知作者处理: {data}").format(data=data_dict)
            )


async def test():
    from src.testers import Params

    async with Params() as params:
        i = Hot(
            params,
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/info.py`
```python
from typing import TYPE_CHECKING
from typing import Union

from src.interface.template import API
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class Info(API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        sec_user_id: Union[str, list[str], tuple[str]] = ...,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.api = f"{self.domain}aweme/v1/web/im/user/info/"
        self.sec_user_id = sec_user_id
        self.static_params = self.params | {
            "version_code": "170400",
            "version_name": "17.4.0",
        }
        self.text = _("账号简略")

    async def run(
        self,
        first=True,
        *args,
        **kwargs,
    ) -> dict | list[dict]:
        self.set_referer()
        await self.run_single()
        if first:
            return self.response[0] if self.response else {}
        return self.response

    async def run_single(
        self,
        *args,
        **kwargs,
    ):
        await super().run_single(
            "",
            params=lambda: self.static_params,
            data=self.__generate_data,
            method="POST",
        )

    def check_response(
        self,
        data_dict: dict,
        *args,
        **kwargs,
    ):
        if d := data_dict.get("data"):
            self.append_response(d)
        else:
            self.log.warning(_("获取{text}失败").format(text=self.text))

    def __generate_data(
        self,
    ) -> dict:
        if isinstance(self.sec_user_id, str):
            self.sec_user_id = [self.sec_user_id]
        value = f"[{','.join(f'"{i}"' for i in self.sec_user_id)}]"
        return {
            "sec_user_ids": value,
        }


async def test():
    from src.testers import Params

    async with Params() as params:
        i = Info(
            params,
            sec_user_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/info_tiktok.py`
```python
from typing import TYPE_CHECKING, Union

from src.interface.template import APITikTok
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class InfoTikTok(APITikTok):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        unique_id: Union[str] = "",
        sec_user_id: Union[str] = "",
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.api = f"{self.domain}api/user/detail/"
        self.unique_id = unique_id
        self.sec_user_id = sec_user_id
        self.text = _("账号简略")

    async def run(
        self,
        # first=True,
        *args,
        **kwargs,
    ) -> dict | list[dict]:
        self.set_referer()
        await self.run_single()
        return self.response[0] if self.response else {}

    async def run_single(
        self,
        *args,
        **kwargs,
    ):
        await super().run_single(
            "",
        )

    def check_response(
        self,
        data_dict: dict,
        *args,
        **kwargs,
    ):
        if d := data_dict.get("userInfo"):
            self.append_response(d)
        else:
            self.log.warning(_("获取{text}失败").format(text=self.text))

    def append_response(
        self,
        data: dict,
        *args,
        **kwargs,
    ) -> None:
        self.response.append(data)

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "abTestVersion": "[object Object]",
            "appType": "m",
            "secUid": self.sec_user_id,
            "uniqueId": self.unique_id,
            "user": "[object Object]",
        }


async def test():
    from src.testers import Params

    async with Params() as params:
        InfoTikTok.params["msToken"] = params.msToken_tiktok
        i = InfoTikTok(
            params,
            unique_id="",
            sec_user_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/live.py`
```python
from typing import TYPE_CHECKING, Union

from src.interface.template import API
from src.tools import DownloaderError

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class Live(API):
    live_api = "https://live.douyin.com/webcast/room/web/enter/"
    live_api_share = "https://webcast.amemv.com/webcast/room/reflow/info/"

    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        web_rid: str = ...,
        room_id: str = ...,
        sec_user_id: str = "",
    ):
        super().__init__(params, cookie, proxy)
        self.black_headers = params.headers_download
        self.web_rid = web_rid
        self.room_id = room_id
        self.sec_user_id = sec_user_id

    async def run(
        self,
        *args,
        **kwargs,
    ) -> dict:
        if isinstance(self.web_rid, str):
            return await self.with_web_rid()
        elif self.room_id:
            return await self.with_room_id()
        else:
            raise DownloaderError

    async def with_web_rid(self) -> dict:
        self.set_referer("https://live.douyin.com/")
        params = {  # TODO: 参数固定
            "aid": "6383",
            "app_name": "douyin_web",
            "live_id": "1",
            "device_platform": "web",
            "language": "zh-CN",
            "enter_from": "web_share_link",
            "cookie_enabled": "true",
            "screen_width": "1536",
            "screen_height": "864",
            "browser_language": "zh-CN",
            "browser_platform": "Win32",
            "browser_name": "Edge",
            "browser_version": "139.0.0.0",
            "web_rid": self.web_rid,
            # "room_id_str": "",
            "enter_source": "",
            "is_need_double_stream": "false",
            "insert_task_id": "",
            "live_reason": "",
        }
        return await self.request_data(
            self.live_api,
            params,
        )

    async def with_room_id(self) -> dict:
        params = {
            "type_id": "0",
            "live_id": "1",
            "room_id": self.room_id,
            "sec_user_id": self.sec_user_id,
            "app_id": "1128",
        }
        return await self.request_data(
            self.live_api_share,
            params,
            headers=self.black_headers,
        )


async def test():
    from src.testers import Params

    async with Params() as params:
        i = Live(
            params,
            room_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/live_tiktok.py`
```python
from typing import TYPE_CHECKING
from typing import Union

from src.interface.template import APITikTok
from src.translation import _

if TYPE_CHECKING:
    from ..config import Parameter
    from src.testers import Params


class LiveTikTok(APITikTok):
    live_api = "https://webcast.us.tiktok.com/webcast/room/enter/"

    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        room_id: str = ...,
    ):
        super().__init__(params, cookie, proxy)
        self.black_headers = params.headers_download
        self.room_id = room_id

    async def run(
        self,
        *args,
        **kwargs,
    ) -> dict:
        response = await self.with_room_id()
        return self.check_response(response)

    async def with_room_id(self) -> dict:
        return await self.request_data(
            self.live_api,
            self.params,
            method="POST",
            data=self.__generate_room_id_data(),
        )

    def __generate_room_id_data(
        self,
    ) -> dict:
        return {
            "enter_source": "others-others",
            "room_id": self.room_id,
        }

    def check_response(
        self,
        data_dict: dict,
        *args,
        **kwargs,
    ):
        if data_dict and "prompt" in data_dict["data"]:
            self.console.warning(_("此直播可能会令部分观众感到不适，请登录后重试！"))
            return {}
        return data_dict


async def test():
    from src.testers import Params

    async with Params() as params:
        i = LiveTikTok(
            params,
            room_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/mix.py`
```python
from typing import Callable
from typing import TYPE_CHECKING
from typing import Union

from src.extract import Extractor
from src.interface.detail import Detail
from src.interface.template import API
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class Mix(API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        mix_id: str = None,
        detail_id: str = None,
        cursor=0,
        count=12,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.mix_title = None
        self.mix_id = mix_id
        self.detail_id = detail_id
        self.count = count
        self.cursor = cursor
        self.api = f"{self.domain}aweme/v1/web/mix/aweme/"
        self.text = _("合集作品")
        self.detail = Detail(
            params,
            cookie,
            proxy,
            self.detail_id,
        )

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "mix_id": self.mix_id,
            "cursor": self.cursor,
            "count": self.count,
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    async def run(
        self,
        referer: str = None,
        single_page=False,
        data_key: str = "aweme_list",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        await self.__get_mix_id()
        if not self.mix_id:
            self.log.warning(_("获取合集 ID 失败"))
            return self.response
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )

    async def __get_mix_id(self):
        if not self.mix_id:
            self.mix_id = Extractor.extract_mix_id(await self.detail.run())


async def test():
    from src.testers import Params

    async with Params() as params:
        i = Mix(
            params,
            mix_id="",
            detail_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/mix_tiktok.py`
```python
from typing import TYPE_CHECKING, Callable, Union

from src.interface.template import APITikTok
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class MixTikTok(APITikTok):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        mix_title: str = ...,
        mix_id: str = ...,
        # detail_id: str = None,
        cursor=0,
        count=30,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.mix_title = mix_title
        self.mix_id = mix_id
        # self.detail_id = detail_id  # 未使用
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}api/collection/item_list/"
        self.text = _("合辑作品")

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "count": self.count,
            "cursor": self.cursor,
            "collectionId": self.mix_id,
            "sourceType": "113",
        }

    async def run(
        self,
        referer: str = None,
        single_page=False,
        data_key: str = "itemList",
        error_text="",
        cursor="cursor",
        has_more="hasMore",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )


class MixListTikTok(APITikTok):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        sec_user_id: str = "",
        cursor=0,
        count=20,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.sec_user_id = sec_user_id
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}api/user/playlist/"
        self.text = _("账号合辑数据")

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "count": self.count,
            "cursor": self.cursor,
            "secUid": self.sec_user_id,
        }

    async def run(
        self,
        referer: str = None,
        single_page=False,
        data_key: str = "playList",
        error_text="",
        cursor="cursor",
        has_more="hasMore",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )


async def test():
    from src.testers import Params

    async with Params() as params:
        MixTikTok.params["msToken"] = params.msToken_tiktok
        MixListTikTok.params["msToken"] = params.msToken_tiktok
        # i = MixTikTok(
        #     params,
        #     mix_id="",
        # )
        # print(await i.run())
        i = MixListTikTok(
            params,
            sec_user_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/search.py`
```python
from json import dumps
from types import SimpleNamespace
from typing import TYPE_CHECKING, Union
from urllib.parse import quote

from src.interface.template import API
from src.tools import DownloaderError
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class Search(API):
    search_params = (
        SimpleNamespace(
            note=_("综合搜索"),
            api=f"{API.domain}aweme/v1/web/general/search/single/",
            channel="aweme_general",
            type="general",
            key="data",
        ),
        SimpleNamespace(
            note=_("视频搜索"),
            api=f"{API.domain}aweme/v1/web/search/item/",
            channel="aweme_video_web",
            type="video",
            key="data",
        ),
        SimpleNamespace(
            note=_("用户搜索"),
            api=f"{API.domain}aweme/v1/web/discover/search/",
            channel="aweme_user_web",
            type="user",
            key="user_list",
        ),
        SimpleNamespace(
            note=_("直播搜索"),
            api=f"{API.domain}aweme/v1/web/live/search/",
            channel="aweme_live",
            type="live",
            key="data",
        ),
        SimpleNamespace(
            note=None,
            api=None,
            channel=None,
            type=None,
            key=None,
        ),
    )
    search_data_field = {
        0: "search_general",
        1: "search_general",
        2: "search_user",
        3: "search_live",
    }
    search_criteria = {
        0: _("关键词  总页数  排序依据  发布时间  视频时长  搜索范围  内容形式"),
        1: _("关键词  总页数  排序依据  发布时间  视频时长  搜索范围"),
        2: _("关键词  总页数  粉丝数量  用户类型"),
        3: _("关键词  总页数"),
    }
    channel_map = {
        0: search_params[0],
        1: search_params[1],
        2: search_params[2],
        3: search_params[3],
    }
    sort_type_help = {
        0: _("综合排序"),
        1: _("最多点赞"),
        2: _("最新发布"),
    }
    publish_time_help = {
        0: _("不限"),
        1: _("一天内"),
        7: _("一周内"),
        180: _("半年内"),
    }
    duration_map = {
        0: "",
        1: "0-1",
        2: "1-5",
        3: "5-10000",
    }
    duration_help = {
        0: _("不限"),
        1: _("一分钟以内"),
        2: _("一到五分钟"),
        3: _("五分钟以上"),
    }
    search_range_help = {
        0: _("不限"),
        1: _("最近看过"),
        2: _("还未看过"),
        3: _("关注的人"),
    }
    content_type_help = {
        0: _("不限"),
        1: _("视频"),
        2: _("图文"),
    }
    douyin_user_fans_map = {
        0: [""],
        1: ["0_1k"],
        2: ["1k_1w"],
        3: ["1w_10w"],
        4: ["10w_100w"],
        5: ["100w_"],
    }
    douyin_user_fans_help = {
        0: _("不限"),
        1: _("1000以下"),
        2: "1000-1w",
        3: "1w-10w",
        4: "10w-100w",
        5: _("100w以上"),
    }
    douyin_user_type_map = {
        0: [""],
        1: ["common_user"],
        2: ["enterprise_user"],
        3: ["personal_user"],
    }
    douyin_user_type_help = {
        0: _("不限"),
        1: _("普通用户"),
        2: _("企业认证"),
        3: _("个人认证"),
    }

    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        keyword: str = ...,
        channel: int = 0,
        pages: int = 99999,
        sort_type: int = 0,
        publish_time: int = 0,
        duration: int = 0,
        search_range: int = 0,
        content_type: int = 0,
        douyin_user_fans: int = 0,
        douyin_user_type: int = 0,
        offset: int = 0,
        count: int = 10,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.keyword = keyword
        self.channel = self.channel_map.get(channel, self.search_params[-1])
        self.pages = pages
        self.sort_type = sort_type
        self.publish_time = publish_time
        self.duration = self.duration_map.get(duration, "")
        self.content_type = content_type
        self.search_range = search_range
        self.douyin_user_fans = self.douyin_user_fans_map.get(douyin_user_fans, [""])
        self.douyin_user_type = self.douyin_user_type_map.get(douyin_user_type, [""])
        self.offset = offset
        self.count = count
        self.type = self.channel.type
        self.api = self.channel.api
        self.key = self.channel.key
        self.text = f"{self.channel.note}"
        self.filter_selected = self.generate_filter_selected() if channel == 0 else None
        self.search_filter_value = (
            self.generate_search_filter_value() if channel == 2 else None
        )
        self.search_id = None
        self.params_func = {
            0: self._generate_params_general,
            1: self._generate_params_video,
            2: self._generate_params_user,
            3: self._generate_params_live,
        }.get(channel)

    async def run(self, single_page=False, *args, **kwargs):
        if not self.api:
            raise DownloaderError
        self.set_referer(
            f"{self.domain}root/search/{quote(self.keyword)}?type={self.type}"
        )
        match single_page:
            case True:
                await self.run_single(
                    self.channel.key,
                    params=self.params_func,
                    *args,
                    **kwargs,
                )
            case False:
                await self.run_batch(
                    self.channel.key,
                    params=self.params_func,
                    *args,
                    **kwargs,
                )
            case _:
                raise DownloaderError
        return self.response

    def generate_filter_selected(
        self,
    ) -> str | None:
        if any(
            (
                self.sort_type,
                self.publish_time,
                self.duration,
                self.search_range,
                self.content_type,
            )
        ):
            return dumps(
                {
                    "sort_type": f"{self.sort_type}",
                    "publish_time": f"{self.publish_time}",
                    "filter_duration": f"{self.duration}",
                    "search_range": f"{self.search_range}",
                    "content_type": f"{self.content_type}",
                },
                separators=(",", ":"),
            )
        return None

    def generate_search_filter_value(
        self,
    ) -> str | None:
        if any(
            (
                self.douyin_user_fans,
                self.douyin_user_type,
            )
        ):
            return dumps(
                {
                    "douyin_user_fans": self.douyin_user_fans,
                    "douyin_user_type": self.douyin_user_type,
                },
                separators=(",", ":"),
            )
        return None

    def _generate_params_general(
        self,
    ) -> dict:
        params = self.params | {
            "pc_search_top_1_params": '{"enable_ai_search_top_1":1}',
            "search_channel": self.channel.channel,
            "enable_history": "1",
            "keyword": self.keyword,
            "search_source": "switch_tab",
            "query_correct_type": "1",
            "is_filter_search": "0",
            "from_group_id": "",
            "disable_rs": "0",
            "offset": self.offset,
            "count": self.count,
            "need_filter_settings": "0",
            "list_type": "single",
            "version_code": "190600",
            "version_name": "19.6.0",
        }
        if self.search_id:
            params |= {"search_id": self.search_id}
        if self.filter_selected:
            params |= {
                "filter_selected": quote(self.filter_selected),
                "is_filter_search": "1",
            }
        return params

    def _generate_params_video(
        self,
    ) -> dict:
        params = self.params | {
            "pc_search_top_1_params": '{"enable_ai_search_top_1":1}',
            "search_channel": self.channel.channel,
            "enable_history": "1",
            "keyword": self.keyword,
            "search_source": "switch_tab",
            "query_correct_type": "1",
            "is_filter_search": "0",
            "from_group_id": "",
            "disable_rs": "0",
            "offset": self.offset,
            "count": self.count,
            "need_filter_settings": "0",
            "list_type": "single",
            "version_code": "170400",
            "version_name": "17.4.0",
        }
        if self.search_id:
            params |= {"search_id": self.search_id}
        if self.sort_type:
            params |= {
                "sort_type": f"{self.sort_type}",
                "is_filter_search": "1",
            }
        if self.publish_time:
            params |= {
                "publish_time": f"{self.publish_time}",
                "is_filter_search": "1",
            }
        if self.duration:
            params |= {
                "filter_duration": f"{self.duration}",
                "is_filter_search": "1",
            }
        if self.search_range:
            params |= {
                "search_range": f"{self.search_range}",
                "is_filter_search": "1",
            }
        return params

    def _generate_params_user(
        self,
    ) -> dict:
        params = self._generate_params_live()
        if self.search_filter_value:
            params |= {
                "search_filter_value": quote(self.search_filter_value),
                "is_filter_search": "1",
            }
        return params

    def _generate_params_live(
        self,
    ) -> dict:
        params = self.params | {
            "pc_search_top_1_params": '{"enable_ai_search_top_1":1}',
            "search_channel": self.channel.channel,
            "keyword": self.keyword,
            "search_source": "switch_tab",
            "query_correct_type": "1",
            "is_filter_search": "0",
            "from_group_id": "",
            "disable_rs": "0",
            "offset": self.offset,
            "count": self.count,
            "need_filter_settings": "0",
            "list_type": "single",
            "version_code": "170400",
            "version_name": "17.4.0",
        }
        if self.search_id:
            params |= {"search_id": self.search_id}
        return params

    def check_response(
        self,
        data_dict: dict,
        data_key: str,
        error_text="",
        cursor="cursor",
        has_more="has_more",
        *args,
        **kwargs,
    ):
        try:
            if not isinstance(d := data_dict[data_key], list):
                self.log.warning(error_text)
                self.finished = True
            elif len(d) == 0:
                if not self.response:
                    self.response.append([])
                self.finished = True
            else:
                self.offset = data_dict[cursor]
                self.search_id = data_dict["log_pb"]["impr_id"]
                match self.type:
                    case "general" | "video" | "user":
                        self.append_response(d)
                    case "live":
                        self.append_response_video(
                            d,
                            "lives",
                        )
                    case _:
                        raise DownloaderError
                self.finished = not data_dict[has_more]
        except KeyError:
            self.log.error(
                _("数据解析失败，请告知作者处理: {data}").format(data=data_dict)
            )
            self.finished = True

    def append_response_video(
        self,
        data: list[dict],
        key: str,
    ) -> None:
        self.append_response([i[key] for i in data])


async def test():
    from src.testers import Params

    async with Params() as params:
        Search.params["uifid"] = params.uifid
        Search.params["msToken"] = params.msToken_tiktok
        i = Search(
            params,
            keyword="",
            channel=3,
            sort_type=2,
            publish_time=7,
            duration=2,
            douyin_user_fans=5,
            pages=1,
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/slides.py`
```python
# from typing import Callable
from typing import TYPE_CHECKING
from typing import Union

from src.interface.template import API
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params

__all__ = ["Slides"]


class Slides(API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        slides_id: str | list | tuple = ...,
    ):
        super().__init__(params, cookie, proxy)
        self.slides_id = slides_id
        self.api = f"{self.short_domain}web/api/v2/aweme/slidesinfo/"
        self.text = _("作品")

    async def run(self, *args, **kwargs):
        pass


async def test():
    from src.testers import Params

    async with Params() as params:
        i = Slides(
            params,
            slides_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/template.py`
```python
from time import time
from typing import TYPE_CHECKING, Callable, Coroutine, Type, Union
from urllib.parse import quote, urlencode

from httpx import AsyncClient, get, post
from rich.progress import (
    BarColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
)

from ..custom import PROGRESS, USERAGENT, wait
from ..tools import DownloaderError, FakeProgress, Retry, capture_error_request
from ..translation import _

if TYPE_CHECKING:
    from ..config import Parameter
    from ..testers import Params

__all__ = [
    "API",
    "APITikTok",
]


class API:
    domain = "https://www.douyin.com/"
    short_domain = "https://www.iesdouyin.com/"
    referer = f"{domain}?recommend=1"
    params = {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "update_version_code": "170400",
        "pc_client_type": "1",
        "pc_libra_divert": "Windows",
        "support_h265": "1",
        "support_dash": "1",
        "version_code": "290100",
        "version_name": "29.1.0",
        "cookie_enabled": "true",
        "screen_width": "1536",
        "screen_height": "864",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Chrome",
        "browser_version": "139.0.0.0",
        "browser_online": "true",
        "engine_name": "Blink",
        "engine_version": "139.0.0.0",
        "os_name": "Windows",
        "os_version": "10",
        "cpu_core_num": "16",
        "device_memory": "8",
        "platform": "PC",
        "downlink": "10",
        "effective_type": "4g",
        "round_trip_time": "200",
        # "webid": "",
        "uifid": "",
        "msToken": "",
    }
    progress_object: Callable

    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        *args,
        **kwargs,
    ):
        self.headers = params.headers.copy()
        self.log = params.logger
        self.ab = params.ab
        self.console = params.console
        self.api = ""
        self.proxy = proxy
        self.max_retry = params.max_retry
        self.timeout = params.timeout
        self.cookie = cookie
        self.client: AsyncClient = params.client
        self.pages = 99999
        self.cursor = 0
        self.response = []
        self.finished = False
        self.text = ""
        self.set_temp_cookie(cookie)

    def set_temp_cookie(self, cookie: str = ""):
        if cookie:
            self.headers["Cookie"] = cookie

    def generate_params(
        self,
    ) -> dict:
        return self.params

    def __generate_params(
        self,
    ) -> dict:
        params = self.generate_params()
        params["msToken"] = params.pop("msToken")
        return params

    def generate_data(self, *args, **kwargs) -> dict:
        return {}

    async def run(
        self,
        referer: str = None,
        single_page=False,
        data_key: str = "",
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        self.set_referer(referer)
        match single_page:
            case True:
                await self.run_single(
                    data_key,
                    error_text,
                    cursor,
                    has_more,
                    params,
                    data,
                    method,
                    headers,
                    *args,
                    **kwargs,
                )
            case False:
                await self.run_batch(
                    data_key,
                    error_text,
                    cursor,
                    has_more,
                    params,
                    data,
                    method,
                    headers,
                    *args,
                    **kwargs,
                )
            case _:
                raise DownloaderError
        return self.response

    async def run_single(
        self,
        data_key: str,
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        *args,
        **kwargs,
    ):
        if data := await self.request_data(
            self.api,
            params=params() or self.__generate_params(),
            data=data() or self.generate_data(),
            method=method,
            headers=headers,
            finished=True,
        ):
            self.check_response(
                data, data_key, error_text, cursor, has_more, *args, **kwargs
            )
        else:
            self.log.warning(_("获取{self_text}数据失败").format(self_text=self.text))

    async def run_batch(
        self,
        data_key: str,
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        callback: Type[Coroutine] = None,
        *args,
        **kwargs,
    ):
        with self.progress_object() as progress:
            task_id = progress.add_task(
                _("正在获取{text}数据").format(text=self.text),
                total=None,
            )
            while not self.finished and self.pages > 0:
                progress.update(task_id)
                await self.run_single(
                    data_key,
                    error_text,
                    cursor,
                    has_more,
                    params,
                    data,
                    method,
                    headers,
                    *args,
                    **kwargs,
                )
                self.pages -= 1
                if callback:
                    await callback()

    def check_response(
        self,
        data_dict: dict,
        data_key: str,
        error_text="",
        cursor="cursor",
        has_more="has_more",
        *args,
        **kwargs,
    ):
        try:
            if not (d := data_dict[data_key]):
                self.log.warning(error_text)
                self.finished = True
            else:
                self.cursor = data_dict[cursor]
                self.append_response(d)
                self.finished = not data_dict[has_more]
        except KeyError:
            self.log.error(
                _("数据解析失败，请告知作者处理: {data}").format(data=data_dict)
            )
            self.finished = True

    def set_referer(self, url: str = None) -> None:
        self.headers["Referer"] = url or self.referer

    async def request_data(
        self,
        url: str,
        params: dict = None,
        data: dict = None,
        method="GET",
        headers: dict = None,
        encryption="GET",
        finished=False,
        *args,
        **kwargs,
    ):
        params = self.deal_url_params(
            params,
            encryption,
        )
        match (method, bool(self.proxy)):
            case ("GET", False):
                return await self.request_data_get(
                    url,
                    params,
                    headers or self.headers,
                    finished=finished,
                    *args,
                    **kwargs,
                )
            case ("GET", True):
                return await self.request_data_get_proxy(
                    url,
                    params,
                    headers or self.headers,
                    finished=finished,
                    *args,
                    **kwargs,
                )
            case ("POST", False):
                return await self.request_data_post(
                    url,
                    params,
                    data,
                    headers or self.headers,
                    finished=finished,
                    *args,
                    **kwargs,
                )
            case ("POST", True):
                return await self.request_data_post_proxy(
                    url,
                    params,
                    data,
                    headers or self.headers,
                    finished=finished,
                    *args,
                    **kwargs,
                )
            case _:
                raise DownloaderError

    @Retry.retry
    @capture_error_request
    async def request_data_get(
        self,
        url: str,
        params: str,
        headers: dict,
        finished=False,
        **kwargs,
    ):
        self.__record_request_messages(
            url,
            params,
            None,
            headers,
            **kwargs,
        )
        response = await self.client.get(
            f"{url}?{params}",
            headers=headers,
            **kwargs,
        )
        return await self.__return_response(response)

    @Retry.retry
    @capture_error_request
    async def request_data_get_proxy(
        self,
        url: str,
        params: str,
        headers: dict,
        finished=False,
        **kwargs,
    ):
        self.__record_request_messages(
            url,
            params,
            None,
            headers,
            **kwargs,
        )
        response = get(
            f"{url}?{params}",
            headers=headers,
            proxy=self.proxy,
            follow_redirects=True,
            verify=False,
            timeout=self.timeout,
            **kwargs,
        )
        return await self.__return_response(response)

    @Retry.retry
    @capture_error_request
    async def request_data_post(
        self, url: str, params: str, data: dict, headers: dict, finished=False, **kwargs
    ):
        self.__record_request_messages(
            url,
            params,
            data,
            headers,
            **kwargs,
        )
        response = await self.client.post(
            f"{url}?{params}",
            data=data,
            headers=headers,
            **kwargs,
        )
        return await self.__return_response(response)

    @Retry.retry
    @capture_error_request
    async def request_data_post_proxy(
        self, url: str, params: str, data: dict, headers: dict, finished=False, **kwargs
    ):
        self.__record_request_messages(
            url,
            params,
            data,
            headers,
            **kwargs,
        )
        response = post(
            f"{url}?{params}",
            data=data,
            headers=headers,
            proxy=self.proxy,
            follow_redirects=True,
            verify=False,
            timeout=self.timeout,
            **kwargs,
        )
        return await self.__return_response(response)

    async def __return_response(self, response):
        self.log.info(f"Response URL: {response.url}", False)
        self.log.info(f"Response Code: {response.status_code}", False)
        self.log.info(f"Response Headers: {dict(response.headers)}", False)
        # 记录请求体数据会导致日志文件体积过大，仅在必要时记录
        # self.log.info(f"Response Content: {response.content}", False)
        response.raise_for_status()
        await wait()
        # if response.status_code != 200:
        #     self.log.error(f"请求 {url} 失败，响应码 {response.status_code}")
        #     return
        return response.json()

    def __record_request_messages(
        self,
        url: str,
        params: str | None,
        data: dict | None,
        headers: dict,
        **kwargs,
    ):
        self.log.info(f"URL: {url}", False)
        self.log.info(f"Params: {params}", False)
        self.log.info(f"Data: {data}", False)
        # 请求头脱敏处理，不记录 Cookie
        desensitize = {k: v for k, v in headers.items() if k != "Cookie"}
        self.log.info(f"Headers: {desensitize}", False)
        self.log.info(f"Other: {kwargs}", False)

    def deal_url_params(
        self,
        params: dict,
        method="GET",
        **kwargs,
    ) -> str:
        if params:
            params = urlencode(
                params,
                safe="=",
                quote_via=quote,
            )
            params += f"&a_bogus={self.ab.get_value(params, method)}"
            return params
        return ""

    def summary_works(
        self,
    ) -> None:
        self.log.info(
            _("共获取到 {count} 个{text}").format(
                count=len(self.response), text=self.text
            )
        )

    @classmethod
    def init_progress_object(
        cls,
        server_mode: bool = False,
    ) -> None:
        if server_mode:
            cls._progress_factory = cls.__fake_progress_object
        else:
            cls._progress_factory = cls.__general_progress_object

    def progress_object(self):
        factory = getattr(self, "_progress_factory", self.__general_progress_object)
        return factory()

    def __general_progress_object(self):
        return Progress(
            TextColumn(
                "[progress.description]{task.description}",
                style=PROGRESS,
                justify="left",
            ),
            "•",
            BarColumn(),
            "•",
            TimeElapsedColumn(),
            console=self.console,
            transient=True,
            expand=True,
        )

    @staticmethod
    def __fake_progress_object(*args, **kwargs):
        return FakeProgress()

    def append_response(
        self,
        data: list[dict],
        start: int = None,
        end: int = None,
        *args,
        **kwargs,
    ) -> None:
        for item in data[start:end]:
            self.response.append(item)
        # self.response.extend(data[start:end])


class APITikTok(API):
    domain = "https://www.tiktok.com/"
    short_domain = ""
    referer = f"{domain}explore"
    params = {
        "WebIdLastTime": int(time()),
        "aid": "1988",
        "app_language": "en",
        "app_name": "tiktok_web",
        "browser_language": "zh-SG",
        "browser_name": "Mozilla",
        "browser_online": "true",
        "browser_platform": "Win32",
        "browser_version": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "channel": "tiktok_web",
        "cookie_enabled": "true",
        "data_collection_enabled": "true",
        "device_id": "",
        "device_platform": "web_pc",
        "enable_cache": "true",
        "focus_state": "true",
        "from_page": "user",
        "history_len": "4",
        "is_fullscreen": "false",
        "is_page_visible": "true",
        "language": "en",
        "os": "windows",
        "priority_region": "US",
        "referer": "",
        "region": "US",
        "screen_height": "864",
        "screen_width": "1536",
        "tz_name": "Asia/Shanghai",
        "user_is_login": "true",
        "webcast_language": "en",
        "msToken": "",
    }

    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.xb = params.xb
        self.xg = params.xg
        self.headers = params.headers_tiktok.copy()
        self.cookie = cookie
        self.client: AsyncClient = params.client_tiktok
        self.set_temp_cookie(cookie)

    async def request_data(
        self,
        url: str,
        params: dict = None,
        data: dict = None,
        method="GET",
        headers: dict = None,
        encryption=8,
        finished=False,
        *args,
        **kwargs,
    ):
        return await super().request_data(
            url=url,
            params=params,
            data=data,
            method=method,
            headers=headers,
            encryption=encryption,
            finished=finished,
            *args,
            **kwargs,
        )

    def deal_url_params(
        self,
        params: dict,
        number=8,
        **kwargs,
    ) -> str:
        if params:
            params = urlencode(
                params,
                safe="=",
                quote_via=quote,
            )
            xb = self.xb.get_x_bogus(
                params, number, self.headers.get("User-Agent", USERAGENT)
            )
            xg = self.xg.generate(
                params, user_agent=self.headers.get("User-Agent", USERAGENT)
            )
            params += f"&X-Bogus={xb}&X-Gnarly={xg}"
            return params
        return ""
```

## File: `src/interface/user.py`
```python
from typing import TYPE_CHECKING, Callable, Type, Coroutine
from typing import Union

from src.interface.template import API
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class User(API):
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        cookie: str = "",
        proxy: str = None,
        sec_user_id: str = ...,
        *args,
        **kwargs,
    ):
        super().__init__(params, cookie, proxy, *args, **kwargs)
        self.sec_user_id = sec_user_id
        self.api = f"{self.domain}aweme/v1/web/user/profile/other/"
        self.text = _("账号")

    async def run(self, *args, **kwargs):
        return await super().run(
            single_page=True,
            data_key="user",
        )

    async def run_batch(
        self,
        data_key: str,
        error_text="",
        cursor="cursor",
        has_more="has_more",
        params: Callable = lambda: {},
        data: Callable = lambda: {},
        method="GET",
        headers: dict = None,
        callback: Type[Coroutine] = None,
        *args,
        **kwargs,
    ):
        pass

    def check_response(
        self,
        data_dict: dict,
        data_key: str,
        error_text="",
        *args,
        **kwargs,
    ):
        try:
            if not (d := data_dict[data_key]):
                self.log.warning(error_text)
            else:
                self.response = d
        except KeyError:
            self.log.error(
                _("数据解析失败，请告知作者处理: {data}").format(data=data_dict)
            )
            self.finished = True

    def generate_params(
        self,
    ) -> dict:
        return self.params | {
            "publish_video_strategy_type": "2",
            "sec_user_id": self.sec_user_id,
            "personal_center_strategy": "1",
            "profile_other_record_enable": "1",
            "land_to": "1",
            "version_code": "170400",
            "version_name": "17.4.0",
        }


async def test():
    from src.testers import Params

    async with Params() as params:
        i = User(
            params,
            sec_user_id="",
        )
        print(await i.run())


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/interface/__init__.py`
```python
from ..interface.account import Account
from ..interface.account_tiktok import AccountTikTok
from ..interface.collection import Collection
from ..interface.collects import (
    Collects,
    CollectsDetail,
    CollectsMix,
    CollectsMusic,
    CollectsSeries,
)
from ..interface.comment import Comment, Reply
from ..interface.comment_tiktok import CommentTikTok, ReplyTikTok
from ..interface.detail import Detail
from ..interface.detail_tiktok import DetailTikTok
from ..interface.hashtag import HashTag
from ..interface.hot import Hot
from ..interface.info import Info
from ..interface.info_tiktok import InfoTikTok
from ..interface.live import Live
from ..interface.live_tiktok import LiveTikTok
from ..interface.mix import Mix
from ..interface.mix_tiktok import MixListTikTok
from ..interface.mix_tiktok import MixTikTok
from ..interface.search import Search
from ..interface.template import API
from ..interface.template import APITikTok
from ..interface.user import User
```

## File: `src/link/extractor.py`
```python
from re import compile
from typing import TYPE_CHECKING, Union
from urllib.parse import parse_qs, unquote, urlparse

from .requester import Requester

if TYPE_CHECKING:
    from src.config import Parameter

__all__ = ["Extractor", "ExtractorTikTok"]


class Extractor:
    WEB_RID = compile(r"\\\"webRid\\\":\\\"(\d+?)\\\"")

    account_link = compile(
        r"\S*?https://www\.douyin\.com/user/([A-Za-z0-9_-]+)(?:\S*?\bmodal_id=(\d{19}))?"
    )  # 账号主页链接
    account_share = compile(
        r"\S*?https://www\.iesdouyin\.com/share/user/(\S*?)\?\S*?"  # 账号主页分享链接
    )

    detail_id = compile(r"\b(\d{19})\b")  # 作品 ID
    detail_link = compile(
        r"\S*?https://www\.douyin\.com/(?:video|note|slides)/([0-9]{19})\S*?"
    )  # 作品链接
    detail_share = compile(
        r"\S*?https://www\.iesdouyin\.com/share/(?:video|note|slides)/([0-9]{19})/\S*?"
    )  # 作品分享链接
    detail_search = compile(
        r"\S*?https://www\.douyin\.com/search/\S+?modal_id=(\d{19})\S*?"
    )  # 搜索作品链接
    detail_discover = compile(
        r"\S*?https://www\.douyin\.com/discover\S*?modal_id=(\d{19})\S*?"
    )  # 首页作品链接

    mix_link = compile(
        r"\S*?https://www\.douyin\.com/collection/(\d{19})\S*?"
    )  # 合集链接
    mix_share = compile(
        r"\S*?https://www\.iesdouyin\.com/share/mix/detail/(\d{19})/\S*?"
    )  # 合集分享链接

    live_link = compile(r"\S*?https://live\.douyin\.com/([0-9]+)\S*?")  # 直播链接
    live_link_self = compile(r"\S*?https://www\.douyin\.com/follow\?webRid=(\d+)\S*?")
    live_link_share = compile(
        r"\S*?https://webcast\.amemv\.com/douyin/webcast/reflow/\S+"
    )

    channel_link = compile(
        r"\S*?https://www\.douyin\.com/channel/\d+?\?modal_id=(\d{19})\S*?"
    )

    def __init__(
        self,
        params: "Parameter",
        tiktok=False,
    ):
        self.requester = Requester(
            params,
            params.client_tiktok if tiktok else params.client,
            params.headers_tiktok if tiktok else params.headers,
        )

    async def run(
        self,
        text: str,
        type_="detail",
        proxy: str = None,
    ) -> Union[list[str], tuple[bool, list[str]], str]:
        text = await self.requester.run(
            text,
            proxy,
        )
        match type_:
            case "detail":
                return self.detail(text)
            case "user":
                return self.user(text)
            case "mix":
                return self.mix(text)
            case "live":
                return await self.live(text)
            case "":
                return text
        raise ValueError

    async def get_html_data(
        self,
        url: str,
        pattern,
        index=1,
    ) -> str:
        html = await self.requester.request_url(
            url,
            "text",
        )
        data = pattern.search(html or "")
        return data.group(index) if data else ""

    def detail(
        self,
        urls: str,
    ) -> list[str]:
        return self.__extract_detail(urls)

    def user(
        self,
        urls: str,
    ) -> list[str]:
        link = self.extract_info(self.account_link, urls, 1)
        share = self.extract_info(self.account_share, urls, 1)
        return link + share

    def mix(
        self,
        urls: str,
    ) -> tuple[bool, list[str]]:
        if detail := self.__extract_detail(urls):
            return False, detail
        link = self.extract_info(self.mix_link, urls, 1)
        share = self.extract_info(self.mix_share, urls, 1)
        return (True, m) if (m := link + share) else (None, [])

    async def live(
        self,
        urls: str,
    ) -> list[str]:
        live_link = self.extract_info(self.live_link, urls, 1)
        live_link_self = self.extract_info(self.live_link_self, urls, 1)
        live_link_share = self.extract_info(self.live_link_share, urls, 0)
        live_link_share = [
            await self.get_html_data(i, self.WEB_RID) for i in live_link_share
        ]
        return live_link + live_link_self + live_link_share

    def __extract_detail(
        self,
        urls: str,
    ) -> list[str]:
        link = self.extract_info(self.detail_link, urls, 1)
        share = self.extract_info(self.detail_share, urls, 1)
        account = self.extract_info(self.account_link, urls, 2)
        search = self.extract_info(self.detail_search, urls, 1)
        discover = self.extract_info(self.detail_discover, urls, 1)
        channel = self.extract_info(self.channel_link, urls, 1)
        return link + share + account + search + discover + channel

    @staticmethod
    def extract_sec_user_id(urls: list[str]) -> list[list]:
        data = []
        for url in urls:
            url = urlparse(url)
            query_params = parse_qs(url.query)
            data.append(
                [url.path.split("/")[-1], query_params.get("sec_user_id", [""])[0]]
            )
        return data

    @staticmethod
    def extract_info(pattern, urls: str, index=1) -> list[str]:
        result = pattern.finditer(urls)
        return [i for i in (i.group(index) for i in result) if i] if result else []


class ExtractorTikTok(Extractor):
    SEC_UID = compile(r'"verified":(?:false|true),"secUid":"([a-zA-Z0-9_-]+)"')
    ROOD_ID = compile(r'"roomId":"(\d+)"')
    MIX_ID = compile(r'"canonical":"\S+?(\d{19})"')

    account_link = compile(r"\S*?(https://www\.tiktok\.com/@[^\s/]+)\S*?")

    detail_link = compile(
        r"\S*?https://www\.tiktok\.com/@[^\s/]+/(?!playlist|collection)(?:(?:video|photo)/(\d{19}))?\S*?"
    )  # 作品链接

    mix_link = compile(
        r"\S*?https://www\.tiktok\.com/@\S+/(?:playlist|collection)/(.+?)-(\d{19})\S*?"
    )  # 合集链接

    live_link = compile(r"\S*?https://www\.tiktok\.com/@[^\s/]+/live\S*?")  # 直播链接

    def __init__(self, params: "Parameter"):
        super().__init__(
            params,
            True,
        )

    async def run(
        self,
        text: str,
        type_="detail",
        proxy: str = None,
    ) -> Union[
        list[str],
        tuple[bool, list[str], list[str | None]],
        str,
    ]:
        text = await self.requester.run(
            text,
            proxy,
        )
        match type_:
            case "detail":
                return await self.detail(text)
            case "user":
                return await self.user(text)
            case "mix":
                return await self.mix(text)
            case "live":
                return await self.live(text)
            case "":
                return text
        raise ValueError

    async def detail(
        self,
        urls: str,
    ) -> list[str]:
        return self.__extract_detail(urls)

    async def user(
        self,
        urls: str,
    ) -> list[str]:
        link = self.extract_info(self.account_link, urls, 1)
        link = [await self.get_html_data(i, self.SEC_UID) for i in link]
        return [i for i in link if i]

    def __extract_detail(
        self,
        urls: str,
        index=1,
    ) -> list[str]:
        link = self.extract_info(self.detail_link, urls, index)
        return link

    async def mix(
        self,
        urls: str,
    ) -> tuple[bool, list[str], list[str | None]]:
        detail = self.__extract_detail(urls, index=0)
        detail = [await self.get_html_data(i, self.MIX_ID) for i in detail]
        detail = [i for i in detail if i]
        mix = self.extract_info(self.mix_link, urls, 2)
        title = [unquote(i) for i in self.extract_info(self.mix_link, urls, 1)]
        return True, detail + mix, [None for _ in detail] + title

    async def live(
        self,
        urls: str,
    ) -> list[str]:
        link = self.extract_info(self.live_link, urls, 0)
        link = [await self.get_html_data(i, self.ROOD_ID) for i in link]
        return [i for i in link if i]
```

## File: `src/link/requester.py`
```python
from re import compile
from typing import TYPE_CHECKING

from ..custom import wait
from ..tools import DownloaderError, Retry, capture_error_request

if TYPE_CHECKING:
    from httpx import AsyncClient, get, head

    from ..config import Parameter

__all__ = ["Requester"]


class Requester:
    URL = compile(r"(https?://[^\s\"<>\\^`{|}，。；！？、【】《》]+)")

    def __init__(
        self,
        params: "Parameter",
        client: "AsyncClient",
        headers: dict[str, str],
    ):
        self.client = client
        self.headers = headers
        self.log = params.logger
        self.max_retry = params.max_retry
        self.timeout = params.timeout

    async def run(
        self,
        text: str,
        proxy: str = None,
    ) -> str:
        urls = self.URL.finditer(text)
        if not urls:
            return ""
        result = []
        for i in urls:
            result.append(
                await self.request_url(
                    u := i.group(),
                    proxy=proxy,
                )
                or u
            )
            await wait()
        return " ".join(i for i in result if i)

    @Retry.retry
    @capture_error_request
    async def request_url(
        self,
        url: str,
        content="url",
        proxy: str = None,
    ):
        self.log.info(f"URL: {url}", False)
        match bool(proxy):
            # case True, True:
            #     response = self.request_url_head_proxy(
            #         url,
            #         proxy,
            #     )
            # case True, False:
            #     response = await self.request_url_head(url)
            case True:
                response = self.request_url_get_proxy(
                    url,
                    proxy,
                )
            case False:
                response = await self.request_url_get(url)
            case _:
                raise DownloaderError
        self.log.info(f"Response URL: {response.url}", False)
        self.log.info(f"Response Code: {response.status_code}", False)
        # 记录请求体数据会导致日志文件体积过大，仅在必要时记录
        # self.log.info(f"Response Content: {response.content}", False)
        self.log.info(f"Response Headers: {dict(response.headers)}", False)
        match content:
            case "text":
                return response.text
            case "content":
                return response.content
            case "json":
                return response.json()
            case "headers":
                return response.headers
            case "url":
                return str(response.url)
            case _:
                raise DownloaderError

    async def request_url_head(
        self,
        url: str,
    ):
        return await self.client.head(
            url,
            headers=self.headers,
        )

    def request_url_head_proxy(
        self,
        url: str,
        proxy: str,
    ):
        return head(
            url,
            headers=self.headers,
            proxy=proxy,
            follow_redirects=True,
            verify=False,
            timeout=self.timeout,
        )

    async def request_url_get(
        self,
        url: str,
    ):
        response = await self.client.get(
            url,
            headers=self.headers,
        )
        response.raise_for_status()
        return response

    def request_url_get_proxy(
        self,
        url: str,
        proxy: str,
    ):
        response = get(
            url,
            headers=self.headers,
            proxy=proxy,
            follow_redirects=True,
            verify=False,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response
```

## File: `src/link/__init__.py`
```python
from .extractor import Extractor, ExtractorTikTok

__all__ = [
    "Extractor",
    "ExtractorTikTok",
]
```

## File: `src/manager/cache.py`
```python
from pathlib import Path
from typing import TYPE_CHECKING

from ..tools import Retry
from ..translation import _

if TYPE_CHECKING:
    from ..config import Parameter
    from .database import Database

__all__ = ["Cache"]


class Cache:
    def __init__(
        self,
        parameter: "Parameter",
        database: "Database",
        mark: bool,
        name: bool,
    ):
        self.console = parameter.console
        self.log = parameter.logger  # 日志记录对象
        self.database = database
        self.root = parameter.root  # 作品文件保存根目录
        self.mark = mark
        self.name = name

    async def update_cache(
        self,
        solo_mode: bool,
        prefix: str,
        suffix: str,
        id_: str,
        name: str,
        mark: str,
    ):
        if d := await self.has_cache(id_):
            self.__check_file(
                solo_mode,
                prefix,
                suffix,
                id_,
                name,
                mark,
                d,
            )
        data = (
            id_,
            name,
            mark,
        )
        await self.database.update_mapping_data(*data)
        self.log.info(f"更新缓存数据: {', '.join(data)}", False)

    async def has_cache(self, id_: str) -> dict:
        return await self.database.read_mapping_data(id_)

    def __check_file(
        self,
        solo_mode: bool,
        prefix: str,
        suffix: str,
        id_: str,
        name: str,
        mark: str,
        data: dict,
    ):
        if not (
            old_folder := self.root.joinpath(
                f"{prefix}{id_}_{data['mark'] or data['name']}_{suffix}"
            )
        ).is_dir():
            self.log.info(f"{old_folder} 文件夹不存在，自动跳过", False)
            return
        if data["mark"] != mark:
            self.__rename_folder(old_folder, prefix, suffix, id_, mark)
            if self.mark:
                self.__scan_file(
                    solo_mode,
                    prefix,
                    suffix,
                    id_,
                    name,
                    mark,
                    key="mark",
                    data=data,
                )
        if data["name"] != name and self.name:
            self.__scan_file(
                solo_mode,
                prefix,
                suffix,
                id_,
                name,
                mark,
                data=data,
            )

    def __rename_folder(
        self,
        old_folder: Path,
        prefix: str,
        suffix: str,
        id_: str,
        mark: str,
    ):
        new_folder = self.root.joinpath(f"{prefix}{id_}_{mark}_{suffix}")
        self.__rename(
            old_folder,
            new_folder,
            _("文件夹"),
        )
        self.log.info(f"文件夹 {old_folder} 已重命名为 {new_folder}", False)

    def __rename_works_folder(
        self,
        old_: Path,
        mark: str,
        name: str,
        key: str,
        data: dict,
    ) -> Path:
        if (s := data[key]) in old_.name:
            new_ = old_.parent / old_.name.replace(
                s, {"name": name, "mark": mark}[key], 1
            )
            self.__rename(
                old_,
                new_,
                _("文件夹"),
            )
            self.log.info(f"文件夹 {old_} 重命名为 {new_}", False)
            return new_
        return old_

    def __scan_file(
        self,
        solo_mode: bool,
        prefix: str,
        suffix: str,
        id_: str,
        name: str,
        mark: str,
        data: dict,
        key="name",
    ):
        root = self.root.joinpath(f"{prefix}{id_}_{mark}_{suffix}")
        item_list = root.iterdir()
        if solo_mode:
            for f in item_list:
                if f.is_dir():
                    f = self.__rename_works_folder(
                        f,
                        mark,
                        name,
                        key,
                        data,
                    )
                    files = f.iterdir()
                    self.__batch_rename(
                        f,
                        files,
                        mark,
                        name,
                        key,
                        data,
                    )
        else:
            self.__batch_rename(
                root,
                item_list,
                mark,
                name,
                key,
                data,
            )

    def __batch_rename(
        self,
        root: Path,
        files,
        mark: str,
        name: str,
        key: str,
        data: dict,
    ):
        for old_file in files:
            if (s := data[key]) not in old_file.name:
                break
            self.__rename_file(root, old_file, s, mark, name, key)

    def __rename_file(
        self,
        root: Path,
        old_file: Path,
        keywords: str,
        mark: str,
        name: str,
        field: str,
    ):
        new_file = root.joinpath(
            old_file.name.replace(keywords, {"name": name, "mark": mark}[field], 1)
        )
        self.__rename(
            old_file,
            new_file,
            _("文件"),
        )
        self.log.info(f"文件 {old_file} 重命名为 {new_file}", False)
        return True

    @Retry.retry_limited
    def __rename(
        self,
        old_: Path,
        new_: Path,
        type_=_("文件"),
    ) -> bool:
        try:
            old_.rename(new_)
            return True
        except PermissionError as e:
            self.console.error(
                _("{type} {old}被占用，重命名失败: {error}").format(
                    type=type_, old=old_, error=e
                ),
            )
            return False
        except FileExistsError as e:
            self.console.error(
                _("{type} {new}名称重复，重命名失败: {error}").format(
                    type=type_, new=new_, error=e
                ),
            )
            return False
        except OSError as e:
            self.console.error(
                _("处理{type} {old}时发生预期之外的错误: {error}").format(
                    type=type_, old=old_, error=e
                ),
            )
            return True
```

## File: `src/manager/database.py`
```python
from asyncio import CancelledError
from contextlib import suppress
from shutil import move

from aiosqlite import Row, connect

from ..custom import PROJECT_ROOT

__all__ = ["Database"]


class Database:
    __FILE = "DouK-Downloader.db"

    def __init__(
        self,
    ):
        self.file = PROJECT_ROOT.joinpath(self.__FILE)
        self.database = None
        self.cursor = None

    async def __connect_database(self):
        self.database = await connect(self.file)
        self.database.row_factory = Row
        self.cursor = await self.database.cursor()
        await self.__create_table()
        await self.__write_default_config()
        await self.__write_default_option()
        await self.database.commit()

    async def __create_table(self):
        await self.database.execute(
            """CREATE TABLE IF NOT EXISTS config_data (
            NAME TEXT PRIMARY KEY,
            VALUE INTEGER NOT NULL CHECK(VALUE IN (0, 1))
            );"""
        )
        await self.database.execute(
            "CREATE TABLE IF NOT EXISTS download_data (ID TEXT PRIMARY KEY);"
        )
        await self.database.execute("""CREATE TABLE IF NOT EXISTS mapping_data (
        ID TEXT PRIMARY KEY,
        NAME TEXT NOT NULL,
        MARK TEXT NOT NULL
        );""")
        await self.database.execute("""CREATE TABLE IF NOT EXISTS option_data (
        NAME TEXT PRIMARY KEY,
        VALUE TEXT NOT NULL
        );""")

    async def __write_default_config(self):
        await self.database.execute("""INSERT OR IGNORE INTO config_data (NAME, VALUE)
                            VALUES ('Record', 1),
                            ('Logger', 0),
                            ('Disclaimer', 0);""")

    async def __write_default_option(self):
        await self.database.execute("""INSERT OR IGNORE INTO option_data (NAME, VALUE)
                            VALUES ('Language', 'zh_CN');""")

    async def read_config_data(self):
        await self.cursor.execute("SELECT * FROM config_data")
        return await self.cursor.fetchall()

    async def read_option_data(self):
        await self.cursor.execute("SELECT * FROM option_data")
        return await self.cursor.fetchall()

    async def update_config_data(
        self,
        name: str,
        value: int,
    ):
        await self.database.execute(
            "REPLACE INTO config_data (NAME, VALUE) VALUES (?,?)", (name, value)
        )
        await self.database.commit()

    async def update_option_data(
        self,
        name: str,
        value: str,
    ):
        await self.database.execute(
            "REPLACE INTO option_data (NAME, VALUE) VALUES (?,?)", (name, value)
        )
        await self.database.commit()

    async def update_mapping_data(self, id_: str, name: str, mark: str):
        await self.database.execute(
            "REPLACE INTO mapping_data (ID, NAME, MARK) VALUES (?,?,?)",
            (id_, name, mark),
        )
        await self.database.commit()

    async def read_mapping_data(self, id_: str):
        await self.cursor.execute(
            "SELECT NAME, MARK FROM mapping_data WHERE ID=?", (id_,)
        )
        return await self.cursor.fetchone()

    async def has_download_data(self, id_: str) -> bool:
        await self.cursor.execute("SELECT ID FROM download_data WHERE ID=?", (id_,))
        return bool(await self.cursor.fetchone())

    async def write_download_data(self, id_: str):
        await self.database.execute(
            "INSERT OR IGNORE INTO download_data (ID) VALUES (?);", (id_,)
        )
        await self.database.commit()

    async def delete_download_data(self, ids: list | tuple | str):
        if not ids:
            return
        if isinstance(ids, str):
            ids = [ids]
        [await self.__delete_download_data(i) for i in ids]
        await self.database.commit()

    async def __delete_download_data(self, id_: str):
        await self.database.execute("DELETE FROM download_data WHERE ID=?", (id_,))

    async def delete_all_download_data(self):
        await self.database.execute("DELETE FROM download_data")
        await self.database.commit()

    async def __aenter__(self):
        self.compatible()
        await self.__connect_database()
        return self

    async def close(self):
        with suppress(CancelledError):
            await self.cursor.close()
        await self.database.close()

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    def compatible(self):
        if (
            old := PROJECT_ROOT.parent.joinpath(self.__FILE)
        ).exists() and not self.file.exists():
            move(old, self.file)
```

## File: `src/manager/recorder.py`
```python
from pathlib import Path
from platform import system
from re import compile
from typing import TYPE_CHECKING

from ..custom import (
    ERROR,
    INFO,
    WARNING,
)

if TYPE_CHECKING:
    from ..tools import ColorfulConsole
    from .database import Database

__all__ = [
    "DownloadRecorder",
]


class __DownloadRecorder:
    encode = "UTF-8-SIG" if system() == "Windows" else "UTF-8"
    works_id = compile(r"\d{19}")

    def __init__(
        self, switch: bool, folder: Path, state: bool, console: "ColorfulConsole"
    ):
        self.switch = switch
        self.state = state
        self.backup = folder.joinpath("IDRecorder_backup.txt")
        self.path = folder.joinpath("IDRecorder.txt")
        self.file = None
        self.console = console
        self.record = self.__get_set()

    def __get_set(self) -> set:
        return self.__read_file() if self.switch else set()

    def __read_file(self):
        if not self.path.is_file():
            blacklist = set()
        else:
            with self.path.open("r", encoding=self.encode) as f:
                blacklist = self.__restore_data({line.strip() for line in f})
        self.file = self.path.open("w", encoding=self.encode)
        return blacklist

    def __save_file(self, file):
        file.write("\n".join(f"{i}" for i in self.record))

    def update_id(self, id_):
        if self.switch:
            self.record.add(id_)

    def __extract_ids(self, ids: str) -> list[str]:
        ids = ids.split()
        result = []
        for i in ids:
            if id_ := self.works_id.search(i):
                result.append(id_.group())
        return result

    def delete_ids(self, ids: str) -> None:
        if ids.upper() == "ALL":
            self.record.clear()
        else:
            ids = self.__extract_ids(ids)
            [self.record.remove(i) for i in ids if i in self.record]

    def backup_file(self):
        if self.file and self.record:
            # print("Backup IDRecorder")  # 调试代码
            with self.backup.open("w", encoding=self.encode) as f:
                self.__save_file(f)

    def close(self):
        if self.file:
            self.__save_file(self.file)
            self.file.close()
            self.file = None
            # print("Close IDRecorder")  # 调试代码

    def __restore_data(self, ids: set) -> set:
        if self.state:
            return ids
        self.console.print(
            f"程序检测到上次运行可能没有正常结束，您的作品下载记录数据可能已经丢失！\n数据文件路径：{
                self.path.resolve()
            }",
            style=ERROR,
        )
        if self.backup.exists():
            if (
                self.console.input(
                    "检测到 IDRecorder 备份文件，是否恢复最后一次备份的数据(YES/NO): ",
                    style=WARNING,
                ).upper()
                == "YES"
            ):
                self.path.write_text(self.backup.read_text(encoding=self.encode))
                self.console.print(
                    "IDRecorder 已恢复最后一次备份的数据，请重新运行程序！", style=INFO
                )
                return set(self.backup.read_text(encoding=self.encode).split())
            else:
                self.console.print(
                    "IDRecorder 数据未恢复，下载任意作品之后，备份数据会被覆盖导致无法恢复！",
                    style=ERROR,
                )
        else:
            self.console.print(
                "未检测到 IDRecorder 备份文件，您的作品下载记录数据无法恢复！",
                style=ERROR,
            )
        return set()


class DownloadRecorder:
    detail = compile(r"\d{19}")

    def __init__(self, database: "Database", switch: bool, console: "ColorfulConsole"):
        self.switch = switch
        self.console = console
        self.database = database

    async def has_id(self, id_: str) -> bool:
        return (
            await self.database.has_download_data(id_) if self.switch and id_ else False
        )

    async def update_id(self, id_: str):
        if self.switch and id_:
            await self.database.write_download_data(id_)

    async def delete_id(self, id_: str) -> None:
        if self.switch and id_:
            await self.database.delete_download_data(id_)

    async def delete_ids(self, ids: str) -> None:
        if ids.upper() == "ALL":
            await self.database.delete_all_download_data()
        else:
            ids = self.__extract_ids(ids)
            await self.database.delete_download_data(ids)

    def __extract_ids(self, ids: str) -> list[str]:
        ids = ids.split()
        result = []
        for i in ids:
            if id_ := self.detail.search(i):
                result.append(id_.group())
        return result
```

## File: `src/manager/__init__.py`
```python
from .cache import Cache
from .database import Database
from .recorder import DownloadRecorder

__all__ = [
    "Cache",
    "DownloadRecorder",
    "Database",
]
```

## File: `src/models/account.py`
```python
from pydantic import Field

from .base import APIModel


class Account(APIModel):
    sec_user_id: str
    tab: str = "post"
    earliest: str | float | int | None = None
    latest: str | float | int | None = None
    pages: int | None = None
    cursor: int = 0
    count: int = Field(
        18,
        gt=0,
    )


class AccountTiktok(Account):
    pass
```

## File: `src/models/base.py`
```python
from pydantic import BaseModel


class APIModel(BaseModel):
    cookie: str = ""
    proxy: str = ""
    source: bool = False
```

## File: `src/models/comment.py`
```python
from pydantic import Field

from .base import APIModel


class Comment(APIModel):
    detail_id: str
    pages: int = Field(
        1,
        gt=0,
    )
    cursor: int = 0
    count: int = Field(
        20,
        gt=0,
    )
    count_reply: int = Field(
        3,
        gt=0,
    )
    reply: bool = False
```

## File: `src/models/detail.py`
```python
from .base import APIModel


class Detail(APIModel):
    detail_id: str


class DetailTikTok(Detail):
    pass
```

## File: `src/models/live.py`
```python
from .base import APIModel


class Live(APIModel):
    web_rid: str | None = None
    # room_id: str | None = None
    # sec_user_id: str | None = None


class LiveTikTok(APIModel):
    room_id: str | None = None
```

## File: `src/models/mix.py`
```python
from pydantic import Field

from .base import APIModel


class Mix(APIModel):
    mix_id: str | None = None
    detail_id: str | None = None
    cursor: int = 0
    count: int = Field(
        12,
        gt=0,
    )


class MixTikTok(APIModel):
    mix_id: str | None = None
    cursor: int = 0
    count: int = Field(
        30,
        gt=0,
    )
```

## File: `src/models/reply.py`
```python
from pydantic import Field

from .base import APIModel


class Reply(APIModel):
    detail_id: str
    comment_id: str
    pages: int = Field(
        1,
        gt=0,
    )
    cursor: int = 0
    count: int = Field(
        3,
        gt=0,
    )
```

## File: `src/models/response.py`
```python
from datetime import datetime

from pydantic import BaseModel, computed_field


class DataResponse(BaseModel):
    message: str
    data: dict | list[dict] | None = None
    params: dict | None

    @computed_field
    @property
    def time(self) -> str:
        """格式化后的时间字符串"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class UrlResponse(BaseModel):
    message: str
    url: str | None = None
    params: dict | None

    @computed_field
    @property
    def time(self) -> str:
        """格式化后的时间字符串"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

## File: `src/models/search.py`
```python
from typing import Literal

from pydantic import Field, field_validator

from src.models.base import APIModel

try:
    from src.translation import _
except ImportError:

    def _(x):
        return x


class BaseSearch(APIModel):
    keyword: str
    pages: int = Field(
        1,
        gt=0,
    )
    offset: int = Field(
        0,
        ge=0,
    )
    count: int = Field(
        10,
        ge=5,
    )

    @field_validator("keyword", mode="before")
    @classmethod
    def keyword_validator(cls, v):
        if not v:
            raise ValueError(_("keyword 参数无效"))
        return v


class GeneralSearch(BaseSearch):
    channel: Literal[0,] = 0
    sort_type: Literal[
        0,
        1,
        2,
    ] = 0
    publish_time: Literal[
        0,
        1,
        7,
        180,
    ] = 0
    duration: Literal[
        0,
        1,
        2,
        3,
    ] = 0
    search_range: Literal[
        0,
        1,
        2,
        3,
    ] = 0
    content_type: Literal[
        0,
        1,
        2,
    ] = 0

    @field_validator(
        "sort_type",
        "publish_time",
        "duration",
        "search_range",
        "content_type",
        mode="before",
    )
    @classmethod
    def val_number(cls, value: str | int) -> int:
        return int(value) if isinstance(value, str) else value


class VideoSearch(BaseSearch):
    channel: Literal[1,] = 1
    sort_type: Literal[
        0,
        1,
        2,
    ] = 0
    publish_time: Literal[
        0,
        1,
        7,
        180,
    ] = 0
    duration: Literal[
        0,
        1,
        2,
        3,
    ] = 0
    search_range: Literal[
        0,
        1,
        2,
        3,
    ] = 0

    @field_validator(
        "sort_type", "publish_time", "duration", "search_range", mode="before"
    )
    @classmethod
    def val_number(cls, value: str | int) -> int:
        return int(value) if isinstance(value, str) else value


class UserSearch(BaseSearch):
    channel: Literal[2,] = 2
    douyin_user_fans: Literal[
        0,
        1,
        2,
        3,
        4,
        5,
    ] = 0
    douyin_user_type: Literal[
        0,
        1,
        2,
        3,
    ] = 0

    @field_validator("douyin_user_fans", "douyin_user_type", mode="before")
    @classmethod
    def val_number(cls, value: str | int) -> int:
        return int(value) if isinstance(value, str) else value


class LiveSearch(BaseSearch):
    channel: Literal[3,] = 3
```

## File: `src/models/settings.py`
```python
from typing import List

from pydantic import BaseModel, Field


class AccountUrl(BaseModel):
    mark: str = ""
    url: str
    tab: str = "post"
    earliest: str | int | float = ""
    latest: str | int | float = ""
    enable: bool = True


class MixUrl(BaseModel):
    mark: str = ""
    url: str
    enable: bool = True


class OwnerUrl(BaseModel):
    mark: str = ""
    url: str
    uid: str = ""
    sec_uid: str = ""
    nickname: str = ""


class BrowserInfo(BaseModel):
    User_Agent: str = Field(
        default="",
        alias="User-Agent",
    )
    pc_libra_divert: str = ""
    browser_language: str = ""
    browser_platform: str = ""
    browser_name: str = ""
    browser_version: str = ""
    engine_name: str = ""
    engine_version: str = ""
    os_name: str = ""
    os_version: str = ""
    webid: str = ""


class TikTokBrowserInfo(BaseModel):
    User_Agent: str = Field(
        "",
        alias="User-Agent",
    )
    app_language: str = ""
    browser_language: str = ""
    browser_name: str = ""
    browser_platform: str = ""
    browser_version: str = ""
    language: str = ""
    os: str = ""
    priority_region: str = ""
    region: str = ""
    tz_name: str = ""
    webcast_language: str = ""
    device_id: str = ""


class Settings(BaseModel):
    accounts_urls: List[AccountUrl] = []
    accounts_urls_tiktok: List[AccountUrl] = []
    mix_urls: List[MixUrl] = []
    mix_urls_tiktok: List[MixUrl] = []
    owner_url: OwnerUrl | dict[str, str] = {}
    owner_url_tiktok: None = None
    root: str | None = None
    folder_name: str | None = None
    name_format: str | None = None
    desc_length: int | None = None
    name_length: int | None = None
    date_format: str | None = None
    split: str | None = None
    folder_mode: bool | None = None
    music: bool | None = None
    truncate: int | None = None
    storage_format: str | None = None
    cookie: str | dict = ""
    cookie_tiktok: str | dict = ""
    dynamic_cover: bool | None = None
    static_cover: bool | None = None
    proxy: str | None = None
    proxy_tiktok: str | None = None
    twc_tiktok: str | None = None
    download: bool | None = None
    max_size: int | None = None
    chunk: int | None = None
    timeout: int | None = None
    max_retry: int | None = None
    max_pages: int | None = None
    run_command: str | None = None
    ffmpeg: str | None = None
    live_qualities: str | None = None
    douyin_platform: bool | None = None
    tiktok_platform: bool | None = None
    browser_info: BrowserInfo | None = None
    browser_info_tiktok: TikTokBrowserInfo | None = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            AccountUrl: lambda v: v.dict(),
            MixUrl: lambda v: v.dict(),
            OwnerUrl: lambda v: v.dict(),
            BrowserInfo: lambda v: v.dict(),
            TikTokBrowserInfo: lambda v: v.dict(),
        }
```

## File: `src/models/share.py`
```python
from pydantic import BaseModel


class ShortUrl(BaseModel):
    text: str
    proxy: str = ""
```

## File: `src/models/__init__.py`
```python
from .response import DataResponse, UrlResponse
from .search import (
    GeneralSearch,
    VideoSearch,
    UserSearch,
    LiveSearch,
)
from .settings import Settings
from .share import ShortUrl
from .detail import Detail, DetailTikTok
from .account import Account, AccountTiktok
from .comment import Comment
from .reply import Reply
from .mix import Mix, MixTikTok
from .live import Live, LiveTikTok

__all__ = (
    "GeneralSearch",
    "VideoSearch",
    "UserSearch",
    "LiveSearch",
    "DataResponse",
    "Settings",
    "UrlResponse",
    "ShortUrl",
    "Detail",
    "DetailTikTok",
    "Account",
    "AccountTiktok",
    "Comment",
    "Reply",
    "Mix",
    "MixTikTok",
    "Live",
    "LiveTikTok",
)
```

## File: `src/module/cookie.py`
```python
from typing import TYPE_CHECKING
from ..tools import cookie_str_to_dict
from ..translation import _
from re import compile
from pyperclip import paste

if TYPE_CHECKING:
    from ..config import Settings
    from ..tools import ColorfulConsole

__all__ = ["Cookie"]


class Cookie:
    PATTERN = compile(r"[!#$%&'*+\-.^_`|~0-9A-Za-z]+=([^;\s][^;]*)")
    STATE_KEY = "sessionid_ss"
    PLATFORM_KEY = {
        False: "cookie",
        True: "cookie_tiktok",
    }

    def __init__(self, settings: "Settings", console: "ColorfulConsole"):
        self.settings = settings
        self.console = console
        self.PLATFORM_NAME = {
            False: _("抖音"),
            True: "TikTok",
        }

    def run(
        self,
        tiktok=False,
    ) -> bool:
        """提取 Cookie 并写入配置文件"""
        if self.validate_cookie_minimal(cookie := paste()):
            self.extract(
                cookie,
                key=self.PLATFORM_KEY[tiktok],
                platform=self.PLATFORM_NAME[tiktok],
            )
            return True
        self.console.warning(_("当前剪贴板的内容不是有效的 Cookie 内容！"))
        return False

    def extract(
        self,
        cookie: str,
        write=True,
        key="cookie",
        platform: str = ...,
    ) -> dict:
        cookie_dict = cookie_str_to_dict(cookie)
        self.__check_state(
            cookie_dict,
            platform,
        )
        if write:
            self.save_cookie(cookie_dict, key)
            self.console.print(
                _(f"写入 {platform} Cookie 成功！").format(platform=platform)
            )
        return cookie_dict

    def __check_state(self, items: dict, platform: str) -> None:
        if items.get(self.STATE_KEY):
            self.console.print(
                _(f"当前 {platform} Cookie 已登录").format(platform=platform)
            )
        else:
            self.console.print(
                _(f"当前 {platform} Cookie 未登录").format(platform=platform)
            )

    def save_cookie(self, cookie: dict, key="cookie") -> None:
        data = self.settings.read()
        data[key] = cookie
        self.settings.update(data)

    @classmethod
    def validate_cookie_minimal(cls, cookie_str: str) -> bool:
        """
        只检查整个字符串中是否存在 key=value 子串，
        且 key 和 value 都非空。
        返回 True 或 False。
        """
        if not isinstance(cookie_str, str):
            return False
        return bool(cls.PATTERN.search(cookie_str))
```

## File: `src/module/ffmpeg.py`
```python
from pathlib import Path
from shutil import which
from platform import system
from subprocess import Popen, run
from textwrap import dedent

__all__ = ["FFMPEG"]


class FFMPEG:
    SYSTEM = system()

    # 常见终端及其执行模板
    linux_terminal_templates = {
        # GNOME Terminal (Ubuntu)
        "gnome-terminal": ["gnome-terminal", "--", "bash", "-c", "{cmd}; exec bash"],
        # Deepin Terminal
        "deepin-terminal": ["deepin-terminal", "--", "bash", "-c", "{cmd}; exec bash"],
        # XFCE4 Terminal (MX Linux 默认)
        "xfce4-terminal": [
            "xfce4-terminal",
            "--hold",
            "-e",
            'bash -c "{cmd}; exec bash"',
        ],
        # Konsole (KDE)
        "konsole": ["konsole", "-e", "bash", "-i", "-c", "{cmd}; bash"],
        # Terminator
        "terminator": ["terminator", "-x", "bash", "-c", "{cmd}; exec bash"],
    }

    def __init__(self, path: str):
        self.path = self.__check_ffmpeg_path(Path(path))
        self.support = {
            "Darwin": self.generate_command_darwin,
            "Linux": self.generate_command_linux,
            "Windows": self.generate_command_windows,
        }
        self.run_command = self.support.get(self.SYSTEM, None)
        self.state = bool(self.path) if self.run_command else False

    @staticmethod
    def generate_command_darwin(command: list) -> None:
        script = dedent(f"""
                tell application "Terminal"
                    do script "{" ".join(command).replace('"', '\\"')}"
                    activate
                end tell
                """)
        Popen(["osascript", "-e", script])

    @staticmethod
    def generate_command_windows(command: list) -> None:
        Popen(
            " ".join(
                [
                    "start",
                    "cmd",
                    "/k",
                ]
                + command
            ),
            shell=True,
        )

    @classmethod
    def generate_command_linux(cls, command: list) -> None:
        # TODO: Linux 系统尚未测试
        command = " ".join(command)
        print("ffmpeg command:", command)
        for term, template in cls.linux_terminal_templates.items():
            if which(term):
                # 填充命令并执行
                filled = [
                    part.format(cmd=command) if "{cmd}" in part else part
                    for part in template
                ]
                run(
                    filled,
                )

    def __check_ffmpeg_path(self, path: Path):
        return self.__check_system_ffmpeg() or self.__check_system_ffmpeg(path)

    def download(self, data: list[tuple], proxy, user_agent):
        for u, p in data:
            command = self.__generate_command(
                u,
                p,
                proxy,
                user_agent,
            )
            self.run_command(command)

    def __generate_command(
        self,
        url,
        file,
        proxy,
        user_agent,
    ) -> list:
        command = [
            self.path,
            "-hide_banner",
            "-rw_timeout",
            f"{30 * 1000 * 1000}",
            "-loglevel",
            "info",
            "-protocol_whitelist",
            "rtmp,crypto,file,http,https,tcp,tls,udp,rtp,httpproxy",
            "-analyzeduration",
            f"{10 * 1000 * 1000}",
            "-probesize",
            f"{10 * 1000 * 1000}",
            "-fflags",
            "+discardcorrupt",
            "-user_agent",
            f'"{user_agent}"',
            "-i",
            f'"{url}"',
            "-bufsize",
            "10240k",
            "-map",
            "0",
            "-c:v",
            "copy",
            "-c:a",
            "copy",
            "-sn",
            "-dn",
            "-reconnect_delay_max",
            "60",
            "-reconnect_streamed",
            "-reconnect_at_eof",
            "-max_muxing_queue_size",
            "128",
            "-correct_ts_overflow",
            "1",
            "-f",
            "mp4",
        ]
        if proxy:
            for insert_index, item in enumerate(("-http_proxy", proxy), start=2):
                command.insert(insert_index, item)
        command.append(f'"{file}"')
        return command

    @staticmethod
    def __check_system_ffmpeg(path: Path = None):
        return which(path or "ffmpeg")
```

## File: `src/module/migrate_folder.py`
```python
from shutil import move
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..config import Parameter


class MigrateFolder:
    def __init__(
        self,
        parameter: "Parameter",
    ):
        self.ROOT = parameter.ROOT
        self.root = parameter.root
        self.folder = parameter.folder_name

    def compatible(self):
        for i in (
            "Music",
            "Data",
            "Live",
        ):
            if (old := self.ROOT.parent.joinpath(i)).exists() and not (
                new_ := self.ROOT.joinpath(i)
            ).exists():
                move(old, new_)
        if self.ROOT != self.root:
            return
        if (old := self.ROOT.parent.joinpath(self.folder)).exists() and not (
            new_ := self.ROOT.joinpath(self.folder)
        ).exists():
            move(old, new_)
        folders = self.ROOT.parent.iterdir()
        for i in folders:
            if not i.is_dir():
                continue
            if len(i.name) > 10 and i.name[1:3] == "ID":
                move(i, self.ROOT.joinpath(i.name))
```

## File: `src/module/register.py`
```python
from platform import system
from subprocess import run
from time import sleep
from typing import TYPE_CHECKING
from urllib.parse import quote

from httpx import HTTPError
from qrcode import QRCode
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)

from ..custom import ERROR, PROGRESS, QRCODE_HEADERS, WARNING
from ..encrypt import MsToken

# from ..encrypt import VerifyFp
from ..tools import Retry, cookie_str_to_str

if TYPE_CHECKING:
    from ..config import Parameter, Settings

__all__ = ["__Register"]


class __Register:
    """
    扫码登录功能已过期
    """

    get_url = "https://sso.douyin.com/get_qrcode/"
    check_url = "https://sso.douyin.com/check_qrconnect/"

    def __init__(
        self,
        params: "Parameter",
        settings: "Settings",
    ):
        self.ab = params.ab
        self.xb = params.xb
        self.client = params.client
        self.settings = settings
        self.console = params.console
        self.log = params.logger
        self.headers = QRCODE_HEADERS
        self.proxy = params.proxy
        # self.verify_fp = None
        self.cache = params.cache
        self.url_params = {
            "service": "https://www.douyin.com",
            "need_logo": "false",
            "need_short_url": "true",
            "passport_jssdk_version": "1.0.22",
            "passport_jssdk_type": "pro",
            "aid": "6383",
            "language": "zh",
            "account_sdk_source": "sso",
            "account_sdk_source_info": "7e276d64776172647760466a6b66707777606b667c273f3433292772606761776c736077273"
            "f63646976602927756970626c6b76273f5e2755414325536c60726077272927466d776a6860"
            "2555414325536c60726077272927466d776a686c70682555414325536c60726077272927486"
            "c66776a766a637125406162602555414325536c607260772729275260674e6c712567706c69"
            "71286c6b2555414327582927756077686c76766c6a6b76273f5e7e276b646860273f2762606"
            "a696a6664716c6a6b2729277671647160273f2761606b6c60612778297e276b646860273f27"
            "6b6a716c636c6664716c6a6b762729277671647160273f2775776a6875712778297e276b646"
            "860273f27736c61606a5a666475717077602729277671647160273f2761606b6c6061277829"
            "7e276b646860273f276470616c6a5a666475717077602729277671647160273f2761606b6c6"
            "06127785829276c6b6b60774d606c626d71273f32313729276c6b6b6077526c61716d273f34"
            "30363329276a707160774d606c626d71273f3d333129276a70716077526c61716d273f34303"
            "633292767606d64736c6a77273f7e27716a70666d273f63646976602927686a707660273f71"
            "77706029276e607c476a647761273f717770607829277260676269273f7e27736077766c6a6"
            "b273f27526067424925342b35252d4a75606b424925405625372b3525466d776a686c70682c"
            "27292773606b616a77273f275260674e6c7127292777606b6160776077273f275260674e6c7"
            "125526067424927782927776074706076715a6d6a7671273f277272722b616a707c6c6b2b66"
            "6a68272927776074706076715a7564716d6b646860273f272a2778",
            "passport_ztsdk": "0",
            "passport_verify": "1.0.14",
            # "biz_trace_id": "26eba5d6",
            "device_platform": "web_app",
            "msToken": "",
        }

    def __check_progress_object(self):
        return Progress(
            TextColumn(
                "[progress.description]{task.description}",
                style=PROGRESS,
                justify="left",
            ),
            SpinnerColumn(),
            BarColumn(),
            "•",
            TimeElapsedColumn(),
            console=self.console,
            transient=True,
            expand=True,
        )

    def generate_qr_code(self, url: str):
        qr_code = QRCode()
        # assert url, "无效的登录二维码数据"
        qr_code.add_data(url)
        qr_code.make(fit=True)
        qr_code.print_ascii(invert=True)
        img = qr_code.make_image()
        img.save(self.cache)
        self.console.print(
            "请使用抖音 APP 扫描二维码登录，如果二维码无法识别，请尝试更换终端或者选择其他方式写入 Cookie！"
        )
        self._open_qrcode_image()

    def _open_qrcode_image(self):
        if (s := system()) == "Darwin":  # macOS
            run(["open", self.cache])
        elif s == "Windows":  # Windows
            run(["start", self.cache], shell=True)
        elif s == "Linux":  # Linux
            run(["xdg-open", self.cache])

    async def get_qr_code(self):
        # self.verify_fp = VerifyFp.get_verify_fp()
        # self.url_params["verifyFp"] = self.verify_fp
        # self.url_params["fp"] = self.verify_fp
        await self.__set_ms_token()
        self.url_params["a_bogus"] = quote(self.ab.get_value(self.url_params), safe="")
        # self.url_params["X-Bogus"] = self.xb.get_x_bogus(self.url_params)
        data, _, _ = await self.request_data(
            url=self.get_url,
            params=self.url_params,
        )
        if not data:
            return None, None
        try:
            url = data["data"]["qrcode_index_url"]
            token = data["data"]["token"]
            return url, token
        except KeyError:
            return None, None

    async def __set_ms_token(self):
        if isinstance(
            t := await MsToken.get_real_ms_token(
                self.log,
                self.headers,
                **self.proxy,
            ),
            dict,
        ):
            self.url_params["msToken"] = t["msToken"]

    async def check_register(self, token):
        self.url_params["token"] = token
        self.url_params |= {"is_frontier": "false"}
        with self.__check_progress_object() as progress:
            task_id = progress.add_task("正在检查登录状态", total=None)
            second = 0
            while second < 30:
                sleep(1)
                progress.update(task_id)
                data, headers, _ = await self.request_data(
                    url=self.check_url, params=self.url_params
                )
                if not data:
                    self.console.print("网络异常，无法获取登录状态！", style=WARNING)
                    second = 30
                    continue
                # print(response.json())  # 调试使用
                if data.get("error_code"):
                    self.console.print(
                        f"该账号疑似被风控，建议近期避免扫码登录账号！\n响应数据: {data}",
                        style=WARNING,
                    )
                    second = 30
                elif not (data := data.get("data")):
                    self.console.print(f"响应内容异常: {data}", style=ERROR)
                    second = 30
                elif (s := data["status"]) == "3":
                    redirect_url = data["redirect_url"]
                    cookie = headers.get("Set-Cookie")
                    break
                elif s in (
                    "4",
                    "5",
                ):
                    second = 30
                else:
                    second += 1
            else:
                self.console.print(
                    "扫码登录失败，请使用其他方式获取 Cookie 并写入配置文件！",
                    style=WARNING,
                )
                return None, None
            return redirect_url, cookie

    async def get_cookie(self, url, cookie):
        self.headers["Cookie"] = cookie_str_to_str(cookie)
        _, _, history = await self.request_data(False, url=url)
        if not history or history[0].status_code != 302:
            return False
        return cookie_str_to_str(history[1].headers.get("Set-Cookie"))

    @Retry.retry_lite
    async def request_data(self, json=True, **kwargs):
        try:
            response = await self.client.get(headers=self.headers, **kwargs)
            data = response.json() if json else None
            headers = response.headers
            history = response.history
            return data, headers, history
        except HTTPError as e:
            self.console.print(
                f"扫码登录发生异常，请向作者反馈，错误信息: {e}", style=ERROR
            )
            return None, None, None

    async def run(
        self,
    ):
        self.cache = str(self.cache.joinpath("扫码后请关闭该图片.png"))
        url, token = await self.get_qr_code()
        if not url:
            return False
        self.generate_qr_code(url)
        url, cookie = await self.check_register(token)
        return await self.get_cookie(url, cookie) if url else False
```

## File: `src/module/tiktok_account_index.py`
```python
from pathlib import Path
from re import compile

from lxml.etree import HTML

from src.tools import timestamp

__all__ = []


class __TikTokAccount:
    urls = '//*[@id="main-content-others_homepage"]/div/div[2]/div[last()]/div/div/div/div/div/a/@href'
    uid = '//*[@id="main-content-others_homepage"]/div/div[1]/div[1]/div[2]/div/div[2]/a/@href'
    uid_re = compile(r".*?u=(\d+).*?")
    nickname = (
        '//*[@id="main-content-others_homepage"]/div/div[1]/div[1]/div[2]/h2/text()'
    )
    works_link_tiktok = compile(
        r"\S*?https://www\.tiktok\.com/@\S+?/video/(\d{19})\S*?"
    )

    def __init__(self, path: str):
        self.path = Path(path.replace('"', ""))

    def run(self) -> list:
        if self.path.is_file() and self.path.suffix == ".html":
            return self.__read_html_file([self.path])
        elif self.path.is_dir():
            return self.__read_html_file(self.path.glob("*.html"))
        return []

    def __read_html_file(self, items) -> list:
        ids = []
        for i in items:
            with i.open("r", encoding="utf-8") as f:
                data = f.read()
            ids.append(self.__extract_id_data(data))
        return [i for i in ids if all(i)]

    def __extract_id_data(self, html: str) -> (str, str, list[str]):
        html_tree = HTML(html)
        urls = html_tree.xpath(self.urls)
        uid = self.__extract_uid(html_tree.xpath(self.uid))
        nickname = self.__extract_nickname(html_tree.xpath(self.nickname))
        return uid, nickname, self.works_link_tiktok.findall(" ".join(urls))

    def __extract_uid(self, text: list):
        if len(text) == 1:
            return u.group(1) if (u := self.uid_re.search(text[0])) else timestamp()
        return timestamp()

    @staticmethod
    def __extract_nickname(text: list):
        return text[0].strip() or timestamp() if len(text) == 1 else timestamp()
```

## File: `src/module/tiktok_unofficial.py`
```python
from time import strftime, localtime
from types import SimpleNamespace
from typing import TYPE_CHECKING
from typing import Union

from httpx import get

from src.custom import BLANK_HEADERS
from src.custom import wait
from src.extract import Extractor
from src.testers import Params
from src.tools import Retry
from src.tools import capture_error_request
from src.translation import _

if TYPE_CHECKING:
    from src.config import Parameter
    from src.testers import Params


class DetailTikTokUnofficial:
    def __init__(
        self,
        params: Union["Parameter", "Params"],
        proxy: str = None,
        detail_id: str = ...,
        *args,
        **kwargs,
    ):
        self.headers = BLANK_HEADERS
        self.log = params.logger
        self.console = params.console
        self.api = "https://www.tikwm.com/api/"
        self.proxy = proxy or params.proxy_tiktok
        self.max_retry = params.max_retry
        self.timeout = params.timeout
        self.detail_id = detail_id
        self.text = _("作品")

    async def run(
        self,
    ) -> dict:
        data = await self.request_data_get()
        data = self.check_response(data)
        return data

    @Retry.retry
    @capture_error_request
    async def request_data_get(
        self,
    ):
        response = get(
            self.api,
            params={"url": self.detail_id, "hd": "1"},
            headers=self.headers,
            timeout=self.timeout,
            follow_redirects=True,
            verify=False,
            proxy=self.proxy,
        )
        response.raise_for_status()
        await wait()
        return response.json()

    def check_response(
        self,
        data: dict,
    ):
        try:
            if data["msg"] == "success" and data["data"]:
                return data["data"]
            raise KeyError
        except KeyError:
            self.log.error(_("数据解析失败，请告知作者处理: {data}").format(data=data))


class DetailTikTokExtractor:
    def __init__(self, params: "Parameter"):
        self.date_format = params.date_format
        self.cleaner = params.CLEANER

    def __clean_description(self, desc: str) -> str:
        return self.cleaner.clear_spaces(self.cleaner.filter(desc))

    def __format_date(
        self,
        data: int,
    ) -> str:
        return strftime(
            self.date_format,
            localtime(data or None),
        )

    def run(self, data: dict) -> dict:
        item = {}
        data = Extractor.generate_data_object(data)
        self.extract_detail_tiktok(item, data)
        self.extract_music_tiktok(item, data)
        self.extract_author_tiktok(item, data)
        self.extract_statistics_tiktok(item, data)
        return item

    def extract_detail_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        item["id"] = Extractor.safe_extract(data, "id")
        item["desc"] = (
            self.__clean_description(Extractor.safe_extract(data, "title"))
            or item["id"]
        )
        item["create_time"] = self.__format_date(
            Extractor.safe_extract(data, "create_time")
        )
        item["type"] = _("视频")
        item["downloads"] = Extractor.safe_extract(data, "hdplay")
        item["dynamic_cover"] = Extractor.safe_extract(data, "ai_dynamic_cover")
        item["static_cover"] = Extractor.safe_extract(data, "origin_cover")

    def extract_author_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        item["uid"] = Extractor.safe_extract(data, "author.id")
        item["nickname"] = Extractor.safe_extract(data, "author.nickname")
        item["unique_id"] = Extractor.safe_extract(data, "author.unique_id")

    def extract_music_tiktok(
        self,
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        item["music_author"] = Extractor.safe_extract(data, "music_info.author")
        item["music_title"] = Extractor.safe_extract(data, "music_info.title")
        item["music_url"] = Extractor.safe_extract(data, "music")

    @staticmethod
    def extract_statistics_tiktok(
        item: dict,
        data: SimpleNamespace,
    ) -> None:
        for i in Extractor.statistics_keys:
            item[i] = Extractor.safe_extract(
                data,
                i,
                -1,
            )


async def test():
    async with Params() as params:
        i = DetailTikTokUnofficial(
            params,
            detail_id="",
        )
        if data := await i.run():
            print(DetailTikTokExtractor(params).run(data))


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/module/__init__.py`
```python
from .cookie import Cookie
from .ffmpeg import FFMPEG
from .migrate_folder import MigrateFolder

# from .register import __Register
from .tiktok_unofficial import DetailTikTokExtractor, DetailTikTokUnofficial

__all__ = [
    "Cookie",
    "FFMPEG",
    # "__Register",
    "DetailTikTokExtractor",
    "DetailTikTokUnofficial",
    "MigrateFolder",
]
```

## File: `src/record/base.py`
```python
from pathlib import Path
from time import localtime, strftime
from typing import TYPE_CHECKING

from ..custom import (
    DEBUG,
    ERROR,
    GENERAL,
    INFO,
    VERSION_BETA,
    WARNING,
)
from ..tools import Cleaner

if TYPE_CHECKING:
    from ..tools import ColorfulConsole


class BaseLogger:
    """不记录日志，空白日志记录器"""

    DEBUG = VERSION_BETA

    def __init__(
        self,
        main_path: Path,
        console: "ColorfulConsole",
        root="",
        folder="",
        name="",
    ):
        self.log = None  # 记录器主体
        self.console = console
        self._root, self._folder, self._name = self.init_check(
            main_path=main_path,
            root=root,
            folder=folder,
            name=name,
        )

    def init_check(
        self,
        main_path: Path,
        root=None,
        folder=None,
        name=None,
    ) -> tuple:
        root = self.check_root(root, main_path)
        folder = self.check_folder(folder)
        name = self.check_name(name)
        return root, folder, name

    def check_root(self, root: str, default: Path) -> Path:
        if not root:
            return default
        if (r := Path(root)).is_dir():
            return r
        self.console.print(
            f"日志储存路径 {root} 无效，程序将使用项目根路径作为储存路径"
        )
        return default

    def check_name(self, name: str) -> str:
        if not name:
            return "%Y-%m-%d %H.%M.%S"
        try:
            _ = strftime(name, localtime())
            return name
        except ValueError:
            self.console.print(
                f"日志名称格式 {name} 无效，程序将使用默认时间格式：年-月-日 时.分.秒"
            )
            return "%Y-%m-%d %H.%M.%S"

    @staticmethod
    def check_folder(folder: str) -> str:
        return Cleaner().filter_name(folder, "Log")

    def run(self, *args, **kwargs):
        pass

    def info(self, text: str, output=True, **kwargs):
        if output:
            self.console.print(text, style=INFO, **kwargs)

    def warning(self, text: str, output=True, **kwargs):
        if output:
            self.console.print(text, style=WARNING, **kwargs)

    def error(self, text: str, output=True, **kwargs):
        if output:
            self.console.print(text, style=ERROR, **kwargs)

    def debug(self, text: str, **kwargs):
        if self.DEBUG:
            self.console.print(text, style=DEBUG, **kwargs)

    def print(self, text: str, style=GENERAL, **kwargs) -> None:
        self.console.print(text, style=style, **kwargs)
```

## File: `src/record/logger.py`
```python
from logging import INFO as INFO_LEVEL
from logging import FileHandler, Formatter, getLogger
from pathlib import Path
from platform import system
from shutil import move
from time import localtime, strftime
from typing import TYPE_CHECKING

from ..custom import (
    DEBUG,
    ERROR,
    INFO,
    WARNING,
)
from .base import BaseLogger

if TYPE_CHECKING:
    from ..tools import ColorfulConsole


class LoggerManager(BaseLogger):
    """日志记录"""

    encode = "UTF-8-SIG" if system() == "Windows" else "UTF-8"

    def __init__(
        self, main_path: Path, console: "ColorfulConsole", root="", folder="", name=""
    ):
        super().__init__(main_path, console, root, folder, name)

    def run(
        self,
        format_="%(asctime)s[%(levelname)s]:  %(message)s",
        filename=None,
    ):
        dir_ = self._root.joinpath(self._folder)
        self.compatible(dir_)
        dir_.mkdir(exist_ok=True)
        file_handler = FileHandler(
            dir_.joinpath(
                f"{filename}.log"
                if filename
                else f"{strftime(self._name, localtime())}.log"
            ),
            encoding=self.encode,
        )
        formatter = Formatter(format_, datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)
        self.log = getLogger(__name__)
        self.log.addHandler(file_handler)
        self.log.setLevel(INFO_LEVEL)

    def info(self, text: str, output=True, **kwargs):
        if output:
            self.console.print(text, style=INFO, **kwargs)
        self.log.info(text.strip())

    def warning(self, text: str, output=True, **kwargs):
        if output:
            self.console.print(text, style=WARNING, **kwargs)
        self.log.warning(text.strip())

    def error(self, text: str, output=True, **kwargs):
        if output:
            self.console.print(text, style=ERROR, **kwargs)
        self.log.error(text.strip())

    def debug(self, text: str, **kwargs):
        if self.DEBUG:
            self.console.print(text, style=DEBUG, **kwargs)
            self.log.debug(text.strip())

    def compatible(
        self,
        path: Path,
    ):
        if (
            old := self._root.parent.joinpath(self._folder)
        ).exists() and not path.exists():
            move(old, path)
```

## File: `src/record/__init__.py`
```python
from .base import BaseLogger
from .logger import LoggerManager

__all__ = ["LoggerManager", "BaseLogger"]
```

## File: `src/storage/csv.py`
```python
from csv import writer
from os.path import getsize
from pathlib import Path
from platform import system
from typing import TYPE_CHECKING

from .text import BaseTextLogger

if TYPE_CHECKING:
    from ..tools import ColorfulConsole

__all__ = ["CSVLogger"]


class CSVLogger(BaseTextLogger):
    """CSV 格式保存数据"""

    __type = "csv"
    encode = "UTF-8-SIG" if system() == "Windows" else "UTF-8"

    def __init__(
        self,
        root: Path,
        title_line: tuple,
        field_keys: tuple,
        console: "ColorfulConsole",
        old=None,
        name="Download",
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.console = console
        self.file = None  # 文件对象
        self.writer = None  # CSV对象
        self.name = self._rename(root, self.__type, old, name)  # 文件名称
        self.path = root.joinpath(f"{self.name}.{self.__type}")  # 文件路径
        self.title_line = title_line  # 标题行
        self.field_keys = field_keys

    async def __aenter__(self):
        self.file = self.path.open("a", encoding=self.encode, newline="")
        self.writer = writer(self.file)
        await self.title()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    async def title(self):
        if getsize(self.path) == 0:
            # 如果文件没有任何数据，则写入标题行
            await self.save(self.title_line)

    async def _save(self, data, *args, **kwargs):
        self.writer.writerow(data)
```

## File: `src/storage/manager.py`
```python
from shutil import move
from typing import TYPE_CHECKING

from .csv import CSVLogger
from .sqlite import SQLLogger
from .text import BaseTextLogger
from .xlsx import XLSXLogger

if TYPE_CHECKING:
    from pathlib import Path

    from ..config import Parameter

__all__ = ["RecordManager"]


class RecordManager:
    """检查数据储存路径和文件夹"""

    detail = (
        (
            "type",
            "作品类型",
            "TEXT",
        ),
        (
            "collection_time",
            "采集时间",
            "TEXT",
        ),
        (
            "uid",
            "UID",
            "TEXT",
        ),
        (
            "sec_uid",
            "SEC_UID",
            "TEXT",
        ),
        (
            "unique_id",
            "ID",
            "TEXT",
        ),
        # ("short_id", "SHORT_ID", "TEXT",),
        (
            "id",
            "作品ID",
            "TEXT",
        ),
        (
            "desc",
            "作品描述",
            "TEXT",
        ),
        (
            "text_extra",
            "作品话题",
            "TEXT",
        ),
        (
            "duration",
            "视频时长",
            "TEXT",
        ),
        # ("ratio", "视频分辨率", "TEXT",),
        (
            "height",
            "视频高度",
            "INTEGER",
        ),
        (
            "width",
            "视频宽度",
            "INTEGER",
        ),
        (
            "share_url",
            "作品链接",
            "TEXT",
        ),
        (
            "create_time",
            "发布时间",
            "TEXT",
        ),
        (
            "uri",
            "视频URI",
            "TEXT",
        ),
        (
            "nickname",
            "账号昵称",
            "TEXT",
        ),
        (
            "user_age",
            "年龄",
            "INTEGER",
        ),
        (
            "signature",
            "账号签名",
            "TEXT",
        ),
        (
            "downloads",
            "下载地址",
            "TEXT",
        ),
        (
            "music_author",
            "音乐作者",
            "TEXT",
        ),
        (
            "music_title",
            "音乐标题",
            "TEXT",
        ),
        (
            "music_url",
            "音乐链接",
            "TEXT",
        ),
        (
            "static_cover",
            "静态封面",
            "TEXT",
        ),
        (
            "dynamic_cover",
            "动态封面",
            "TEXT",
        ),
        (
            "tag",
            "隐藏标签",
            "TEXT",
        ),
        (
            "digg_count",
            "点赞数量",
            "INTEGER",
        ),
        (
            "comment_count",
            "评论数量",
            "INTEGER",
        ),
        (
            "collect_count",
            "收藏数量",
            "INTEGER",
        ),
        (
            "share_count",
            "分享数量",
            "INTEGER",
        ),
        (
            "play_count",
            "播放数量",
            "INTEGER",
        ),
        (
            "extra",
            "额外信息",
            "TEXT",
        ),
    )
    comment = (
        (
            "collection_time",
            "采集时间",
            "TEXT",
        ),
        (
            "cid",
            "评论ID",
            "TEXT",
        ),
        (
            "create_time",
            "评论时间",
            "TEXT",
        ),
        (
            "uid",
            "UID",
            "TEXT",
        ),
        (
            "sec_uid",
            "SEC_UID",
            "TEXT",
        ),
        # ("short_id", "SHORT_ID", "TEXT",),
        # ("unique_id", "抖音号", "TEXT",),
        (
            "nickname",
            "账号昵称",
            "TEXT",
        ),
        (
            "signature",
            "账号签名",
            "TEXT",
        ),
        (
            "user_age",
            "年龄",
            "INTEGER",
        ),
        (
            "ip_label",
            "IP归属地",
            "TEXT",
        ),
        (
            "text",
            "评论内容",
            "TEXT",
        ),
        (
            "sticker",
            "评论表情",
            "TEXT",
        ),
        (
            "image",
            "评论图片",
            "TEXT",
        ),
        (
            "digg_count",
            "点赞数量",
            "INTEGER",
        ),
        (
            "reply_comment_total",
            "回复数量",
            "INTEGER",
        ),
        (
            "reply_id",
            "回复ID",
            "TEXT",
        ),
        (
            "reply_to_reply_id",
            "回复对象",
            "TEXT",
        ),
    )
    user = (
        (
            "collection_time",
            "采集时间",
            "TEXT",
        ),
        (
            "nickname",
            "昵称昵称",
            "TEXT",
        ),
        (
            "url",
            "账号链接",
            "TEXT",
        ),
        (
            "signature",
            "账号签名",
            "TEXT",
        ),
        (
            "unique_id",
            "抖音号",
            "TEXT",
        ),
        (
            "user_age",
            "年龄",
            "INTEGER",
        ),
        (
            "gender",
            "性别",
            "TEXT",
        ),
        (
            "country",
            "国家",
            "TEXT",
        ),
        (
            "province",
            "省份",
            "TEXT",
        ),
        (
            "city",
            "城市",
            "TEXT",
        ),
        (
            "district",
            "地区",
            "TEXT",
        ),
        (
            "ip_location",
            "IP归属地",
            "TEXT",
        ),
        (
            "verify",
            "标签",
            "TEXT",
        ),
        (
            "enterprise",
            "企业",
            "TEXT",
        ),
        (
            "sec_uid",
            "SEC_UID",
            "TEXT",
        ),
        (
            "uid",
            "UID",
            "TEXT",
        ),
        (
            "short_id",
            "SHORT_ID",
            "TEXT",
        ),
        (
            "avatar",
            "头像链接",
            "TEXT",
        ),
        (
            "cover",
            "背景图链接",
            "TEXT",
        ),
        (
            "aweme_count",
            "作品数量",
            "INTEGER",
        ),
        (
            "total_favorited",
            "获赞数量",
            "INTEGER",
        ),
        (
            "favoriting_count",
            "喜欢数量",
            "INTEGER",
        ),
        (
            "follower_count",
            "粉丝数量",
            "INTEGER",
        ),
        (
            "following_count",
            "关注数量",
            "INTEGER",
        ),
        (
            "max_follower_count",
            "粉丝最大值",
            "INTEGER",
        ),
    )
    search_user = (
        (
            "collection_time",
            "采集时间",
            "TEXT",
        ),
        (
            "uid",
            "UID",
            "TEXT",
        ),
        (
            "sec_uid",
            "SEC_UID",
            "TEXT",
        ),
        (
            "nickname",
            "账号昵称",
            "TEXT",
        ),
        (
            "unique_id",
            "抖音号",
            "TEXT",
        ),
        (
            "short_id",
            "SHORT_ID",
            "TEXT",
        ),
        (
            "avatar",
            "头像链接",
            "TEXT",
        ),
        (
            "signature",
            "账号签名",
            "TEXT",
        ),
        (
            "verify",
            "标签",
            "TEXT",
        ),
        (
            "enterprise",
            "企业",
            "TEXT",
        ),
        (
            "follower_count",
            "粉丝数量",
            "INTEGER",
        ),
        (
            "total_favorited",
            "获赞数量",
            "INTEGER",
        ),
    )
    search_live = (
        (
            "collection_time",
            "采集时间",
            "TEXT",
        ),
        (
            "room_id",
            "直播ID",
            "TEXT",
        ),
        (
            "uid",
            "UID",
            "TEXT",
        ),
        (
            "sec_uid",
            "SEC_UID",
            "TEXT",
        ),
        (
            "nickname",
            "账号昵称",
            "TEXT",
        ),
        (
            "short_id",
            "SHORT_ID",
            "TEXT",
        ),
        (
            "avatar",
            "头像链接",
            "TEXT",
        ),
        (
            "signature",
            "账号签名",
            "TEXT",
        ),
        (
            "verify",
            "标签",
            "TEXT",
        ),
        (
            "enterprise",
            "企业",
            "TEXT",
        ),
    )
    hot = (
        (
            "position",
            "排名",
            "INTEGER",
        ),
        (
            "word",
            "内容",
            "TEXT",
        ),
        (
            "hot_value",
            "热度",
            "INTEGER",
        ),
        (
            "cover",
            "封面",
            "TEXT",
        ),
        (
            "event_time",
            "时间",
            "TEXT",
        ),
        (
            "view_count",
            "浏览数量",
            "INTEGER",
        ),
        (
            "video_count",
            "视频数量",
            "INTEGER",
        ),
        (
            "sentence_id",
            "SENTENCE_ID",
            "TEXT",
        ),
    )

    detail_keys = [i[0] for i in detail]
    detail_name = [i[1] for i in detail]
    detail_type = [i[2] for i in detail]
    comment_keys = [i[0] for i in comment]
    comment_name = [i[1] for i in comment]
    comment_type = [i[2] for i in comment]
    user_keys = [i[0] for i in user]
    user_name = [i[1] for i in user]
    user_type = [i[2] for i in user]
    search_user_keys = [i[0] for i in search_user]
    search_user_name = [i[1] for i in search_user]
    search_user_type = [i[2] for i in search_user]
    search_live_keys = [i[0] for i in search_live]
    search_live_name = [i[1] for i in search_live]
    search_live_type = [i[2] for i in search_live]
    hot_keys = [i[0] for i in hot]
    hot_name = [i[1] for i in hot]
    hot_type = [i[2] for i in hot]

    LoggerParams = {
        "detail": {
            "db_name": "DetailData.db",
            "title_line": detail_name,
            "title_type": detail_type,
            "field_keys": detail_keys,
        },
        "comment": {
            "db_name": "CommentData.db",
            "title_line": comment_name,
            "title_type": comment_type,
            "field_keys": comment_keys,
        },
        "user": {
            "db_name": "UserData.db",
            "title_line": user_name,
            "title_type": user_type,
            "field_keys": user_keys,
        },
        "mix": {
            "db_name": "MixData.db",
            "title_line": detail_name,
            "title_type": detail_type,
            "field_keys": detail_keys,
        },
        "search_general": {
            "db_name": "SearchData.db",
            "title_line": detail_name,
            "title_type": detail_type,
            "field_keys": detail_keys,
        },
        "search_user": {
            "db_name": "SearchData.db",
            "title_line": search_user_name,
            "title_type": search_user_type,
            "field_keys": search_user_keys,
        },
        "search_live": {
            "db_name": "SearchData.db",
            "title_line": search_live_name,
            "title_type": search_live_type,
            "field_keys": search_live_keys,
        },
        "hot": {
            "db_name": "BoardData.db",
            "title_line": hot_name,
            "title_type": hot_type,
            "field_keys": hot_keys,
        },
    }
    DataLogger = {
        "csv": CSVLogger,
        "xlsx": XLSXLogger,
        "sql": SQLLogger,
        # "mysql": BaseTextLogger,
    }

    def run(
        self,
        parameter: "Parameter",
        folder="",
        type_="detail",
        blank=False,
    ):
        root = parameter.root.joinpath(
            name := parameter.CLEANER.filter_name(folder, "Data")
        )
        self.compatible(
            parameter.root,
            root,
            name,
        )
        root.mkdir(exist_ok=True)
        params = self.LoggerParams[type_]
        logger = (
            BaseTextLogger
            if blank
            else self.DataLogger.get(parameter.storage_format, BaseTextLogger)
        )
        return root, params, logger

    @staticmethod
    def compatible(
        root: "Path",
        path: "Path",
        name: str,
    ):
        if (old := root.parent.joinpath(name)).exists() and not path.exists():
            move(old, path)
```

## File: `src/storage/mysql.py`
```python
from .sql import BaseSQLLogger

__all__ = ["MySQLLogger"]


class MySQLLogger(BaseSQLLogger):
    pass
```

## File: `src/storage/sql.py`
```python
from re import Pattern
from re import compile

from .text import BaseTextLogger

__all__ = ["BaseSQLLogger"]


class BaseSQLLogger(BaseTextLogger):
    SHEET_NAME: Pattern = compile(r"[^\u4e00-\u9fffa-zA-Z0-9_]")
    CHECK_SQL = "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name=?;"
    UPDATE_SQL = "ALTER TABLE {old_name} RENAME TO {new_name};"
```

## File: `src/storage/sqlite.py`
```python
from pathlib import Path
from re import sub

from aiosqlite import connect
from sqlite3 import OperationalError

from rich.text import Text
from rich import print

from ..custom import ERROR
from ..translation import _
from .sql import BaseSQLLogger

__all__ = ["SQLLogger"]


class SQLLogger(BaseSQLLogger):
    """SQLite 数据库保存数据"""

    def __init__(
        self,
        root: Path,
        db_name: str,
        title_line: tuple,
        title_type: tuple,
        field_keys: tuple,
        old=None,
        name="Download",
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.db = None  # 数据库
        self.cursor = None  # 游标对象
        self.name = (old, name)  # 数据表名称
        self.file = db_name  # 数据库文件名称
        self.path = root.joinpath(self.file)
        self.title_line = title_line  # 数据表列名
        self.title_type = title_type  # 数据表数据类型
        self.field_keys = field_keys

    async def __aenter__(self):
        self.db = await connect(self.path)
        self.cursor = await self.db.cursor()
        await self.update_sheet()
        await self.create()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.db.close()

    async def create(self):
        create_sql = f"""CREATE TABLE IF NOT EXISTS {self.name} ({
            ", ".join([f"{i} {j}" for i, j in zip(self.title_line, self.title_type)])
        });"""
        await self.cursor.execute(create_sql)
        await self.db.commit()

    async def _save(self, data, *args, **kwargs):
        insert_sql = f"""REPLACE INTO {self.name} ({
            ", ".join(self.title_line)
        }) VALUES ({", ".join(["?" for _ in self.title_line])});"""
        await self.cursor.execute(insert_sql, data)
        await self.db.commit()

    async def update_sheet(self):
        old_sheet, new_sheet = self.__clean_sheet_name(self.name)
        mark = new_sheet.split("_", 1)
        if not old_sheet or mark[-1] == old_sheet:
            self.name = new_sheet
            return
        mark[-1] = old_sheet
        old_sheet = "_".join(mark)
        if await self.__check_sheet_exists(old_sheet):
            try:
                await self.cursor.execute(self.UPDATE_SQL.format(old_name=old_sheet, new_name=new_sheet))
            except OperationalError as e:
                print(
                    Text(
                        " ".join(
                            (
                                _(
                                    "更新数据表名称时发生错误，重命名失败，请向作者反馈以便修复问题！"
                                ),
                                str(e),
                                old_sheet,
                                new_sheet,
                            )
                        ),
                        style=ERROR,
                    )
                )
                self.name = old_sheet
                return
            await self.db.commit()
        self.name = new_sheet

    async def __check_sheet_exists(self, sheet: str) -> bool:
        await self.cursor.execute(self.CHECK_SQL, (sheet,))
        exists = await self.cursor.fetchone()
        return exists[0] > 0

    def __clean_sheet_name(self, name: tuple) -> tuple:
        return self.__clean_characters(name[0]), self.__clean_characters(name[1])

    def __clean_characters(self, text: str | None) -> str | None:
        if isinstance(text, str):
            text = self.SHEET_NAME.sub("_", text)
            text = sub(r"_+", "_", text)
        return text
```

## File: `src/storage/text.py`
```python
from pathlib import Path
from typing import TYPE_CHECKING, Union

from ..tools import Retry

if TYPE_CHECKING:
    from typing import Iterable


def convert_to_string(function):
    async def _convert_to_string(self, data: Union["Iterable", list], *args, **kwargs):
        for index, value in enumerate(data):
            if isinstance(value, (int, float)):  # 如果值是数字（整型或浮点型）
                data[index] = str(value)  # 转换为字符串
            elif isinstance(value, list):  # 如果值是列表
                data[index] = " ".join(value)  # 将列表元素转换为字符串并连接
        return await function(self, data, *args, **kwargs)

    return _convert_to_string


class BaseTextLogger:
    def __init__(self, *args, **kwargs):
        self.field_keys = []

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb): ...

    @convert_to_string
    async def save(self, data: "Iterable", *args, **kwargs):
        # 数据保存方法入口
        return await self._save(data, *args, **kwargs)

    async def _save(self, data: "Iterable", *args, **kwargs): ...

    @classmethod
    def _rename(cls, root: Path, type_: str, old: str, new_: str) -> str:
        mark = new_.split("_", 1)
        if not old or mark[-1] == old:
            return new_
        mark[-1] = old
        old_file = root.joinpath(f"{'_'.join(mark)}.{type_}")
        cls.__rename_file(old_file, root.joinpath(f"{new_}.{type_}"))
        return new_

    @staticmethod
    @Retry.retry_infinite
    def __rename_file(old_file: Path, new_file: Path) -> bool:
        if old_file.exists() and not new_file.exists():
            try:
                old_file.rename(new_file)
                return True
            except PermissionError:
                return False
        return True
```

## File: `src/storage/xlsx.py`
```python
from pathlib import Path
from typing import TYPE_CHECKING

from openpyxl import Workbook, load_workbook
from openpyxl.utils.exceptions import IllegalCharacterError

from ..translation import _
from .text import BaseTextLogger

if TYPE_CHECKING:
    from ..tools import ColorfulConsole

__all__ = ["XLSXLogger"]


class XLSXLogger(BaseTextLogger):
    """XLSX 格式保存数据"""

    __type = "xlsx"

    def __init__(
        self,
        root: Path,
        title_line: tuple,
        field_keys: tuple,
        console: "ColorfulConsole",
        old=None,
        name="Download",
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.console = console
        self.book = None  # XLSX数据簿
        self.sheet = None  # XLSX数据表
        self.name = self._rename(root, self.__type, old, name)  # 文件名称
        self.path = root.joinpath(f"{self.name}.{self.__type}")
        self.title_line = title_line  # 标题行
        self.field_keys = field_keys

    async def __aenter__(self):
        self.book = load_workbook(self.path) if self.path.exists() else Workbook()
        self.sheet = self.book.active
        self.title()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.book.save(self.path)
        finally:
            self.book.close()

    def title(self):
        if not self.sheet["A1"].value:
            # 如果文件没有任何数据，则写入标题行
            for col, value in enumerate(self.title_line, start=1):
                self.sheet.cell(row=1, column=col, value=value)

    async def _save(self, data, *args, **kwargs):
        try:
            self.sheet.append(data)
        except IllegalCharacterError as e:
            self.console.warning(
                _("数据包含非法字符，保存数据失败：{error}").format(error=e)
            )
        except Exception as e:
            self.console.error(_("保存数据发生异常：{error}").format(error=e))
```

## File: `src/storage/__init__.py`
```python
from .manager import RecordManager

__all__ = ["RecordManager"]
```

## File: `src/testers/logger.py`
```python
class Logger:
    @staticmethod
    def info(
        *args,
    ):
        print(
            *args,
        )

    @staticmethod
    def warning(
        *args,
    ):
        print(
            *args,
        )

    @staticmethod
    def error(
        *args,
    ):
        print(
            *args,
        )

    @staticmethod
    def debug(
        *args,
    ):
        print(
            *args,
        )
```

## File: `src/testers/params.py`
```python
from configparser import ConfigParser, NoOptionError, NoSectionError

from rich.console import Console

from src.custom import (
    DATA_HEADERS,
    DATA_HEADERS_TIKTOK,
    DOWNLOAD_HEADERS_TIKTOK,
    PROJECT_ROOT,
)
from src.encrypt import ABogus, XBogus, XGnarly
from src.testers.logger import Logger
from src.tools import Cleaner, create_client


class Params:
    CONFIG = PROJECT_ROOT.joinpath("test_cookie.ini")
    CLEANER = Cleaner()

    def __init__(self):
        self.cookie_str = ""
        self.cookie_str_tiktok = ""
        self.uifid = ""
        self.msToken = ""
        self.msToken_tiktok = ""
        self.config = ConfigParser(
            interpolation=None,
        )
        self.read_ini()
        self.headers = DATA_HEADERS | {"Cookie": self.cookie_str}
        self.headers_tiktok = DATA_HEADERS_TIKTOK | {
            "Cookie": self.cookie_str_tiktok,
        }
        self.headers_download = DOWNLOAD_HEADERS_TIKTOK
        self.logger = Logger()
        self.ab = ABogus()
        self.xb = XBogus()
        self.xg = XGnarly()
        self.console = Console()
        self.max_retry = 0
        self.timeout = 5
        self.max_pages = 2
        self.proxy = None
        self.proxy_tiktok = "http://127.0.0.1:10808"
        self.date_format = "%Y-%m-%d %H:%M:%S"
        self.client = create_client(
            timeout=self.timeout,
            proxy=self.proxy,
        )
        self.client_tiktok = create_client(
            timeout=self.timeout,
            proxy=self.proxy_tiktok,
        )

    def create_ini(self):
        self.config["dy"] = {
            "cookie": "",
            "uifid": "",
            "msToken": "",
        }
        self.config["tk"] = {
            "cookie": "",
            "msToken": "",
        }
        with self.CONFIG.open("w", encoding="utf-8") as configfile:
            self.config.write(configfile)

    def read_ini(self):
        if not self.config.read(self.CONFIG):
            self.create_ini()
            return
        try:
            self.cookie_str = self.config.get(
                "dy",
                "cookie",
            )
            self.uifid = self.config.get(
                "dy",
                "uifid",
            )
            self.msToken = self.config.get(
                "dy",
                "msToken",
            )
            self.cookie_str_tiktok = self.config.get(
                "tk",
                "cookie",
            )
            self.msToken_tiktok = self.config.get(
                "tk",
                "msToken",
            )
        except (NoSectionError, NoOptionError) as e:
            print(f"读取 Cookie 错误: {e}")

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()
        await self.client_tiktok.aclose()


async def test():
    async with Params() as params:
        print(params.cookie_str)
        print(params.cookie_str_tiktok)


if __name__ == "__main__":
    from asyncio import run

    run(test())
```

## File: `src/testers/test_format.py`
```python
from http.cookiejar import Cookie, CookieJar

from pytest import mark

from src.tools import (
    cookie_dict_to_str,
    cookie_jar_to_dict,
    cookie_str_to_dict,
    cookie_str_to_str,
    format_size,
)


@mark.parametrize(
    "x, y",
    [
        (
            "UIFID_V=2; UIFID_TEMP=aaa; fpk1=aaa; fpk2=aaa; tiktok",
            {"UIFID_V": "2", "UIFID_TEMP": "aaa", "fpk1": "aaa", "fpk2": "aaa"},
        ),
    ],
)
def test_cookie_str_to_dict(x, y):
    assert cookie_str_to_dict(x) == y


@mark.parametrize(
    "x, y",
    [
        (
            "ixigua-a-s=1; path=/; secure; httponly",
            "ixigua-a-s=1",
        ),
    ],
)
def test_cookie_str_to_str(x, y):
    assert cookie_str_to_str(x) == y


@mark.parametrize(
    "x, y",
    [
        (
            {"UIFID_V": "2", "UIFID_TEMP": "aaa", "fpk1": "aaa", "fpk2": "aaa"},
            "UIFID_V=2; UIFID_TEMP=aaa; fpk1=aaa; fpk2=aaa",
        ),
        ({"name": "value"}, "name=value"),
    ],
)
def test_cookie_dict_to_str(x, y):
    assert cookie_dict_to_str(x) == y


def create_test_cookie_jar():
    jar = CookieJar()
    jar.set_cookie(
        Cookie(
            version=0,
            name="cookie_name",
            value="cookie_value",
            port=None,
            port_specified=False,
            domain="example.com",
            domain_specified=True,
            domain_initial_dot=False,
            path="/",
            path_specified=True,
            secure=False,
            expires=None,
            discard=False,
            comment=None,
            comment_url=None,
            rest={},
        )
    )
    return jar


@mark.parametrize(
    "x, y",
    [
        (
            create_test_cookie_jar(),
            {"cookie_name": "cookie_value"},
        ),
    ],
)
def test_cookie_jar_to_dict(x, y):
    assert cookie_jar_to_dict(x) == y


@mark.parametrize(
    "x, y",
    [
        (1024 * 1024, "1.00 MB"),
        (1024 * 512, "512.00 KB"),
        (1024 * 1024 * 2.25, "2.25 MB"),
    ],
)
def test_format_size(x, y):
    assert format_size(x) == y
```

## File: `src/testers/translate.py`
```python
from src.translation import _, switch_language
from src.custom import DISCLAIMER_TEXT

if __name__ == "__main__":
    print(_(DISCLAIMER_TEXT))

    # 切换到英文并打印翻译
    switch_language("en_US")
    print(_(DISCLAIMER_TEXT))

    # 切换回中文并打印翻译
    switch_language("zh_CN")
    print(_(DISCLAIMER_TEXT))
```

## File: `src/testers/__init__.py`
```python
from .logger import Logger
from .params import Params
```

## File: `src/tools/browser.py`
```python
from contextlib import suppress
from sys import platform
from types import SimpleNamespace
from typing import TYPE_CHECKING

from rookiepy import (
    arc,
    brave,
    chrome,
    chromium,
    edge,
    firefox,
    librewolf,
    opera,
    opera_gx,
    vivaldi,
)

from ..translation import _

if TYPE_CHECKING:
    from ..config import Parameter
    from ..module import Cookie

__all__ = ["Browser"]


class Browser:
    SUPPORT_BROWSER = {
        "Arc": (arc, "Linux, macOS, Windows"),
        "Chrome": (chrome, "Linux, macOS, Windows"),
        "Chromium": (chromium, "Linux, macOS, Windows"),
        "Opera": (opera, "Linux, macOS, Windows"),
        "OperaGX": (opera_gx, "macOS, Windows"),
        "Brave": (brave, "Linux, macOS, Windows"),
        "Edge": (edge, "Linux, macOS, Windows"),
        "Vivaldi": (vivaldi, "Linux, macOS, Windows"),
        "Firefox": (firefox, "Linux, macOS, Windows"),
        "LibreWolf": (librewolf, "Linux, macOS, Windows"),
    }
    PLATFORM = {
        False: SimpleNamespace(
            name=_("抖音"),
            domain=[
                "douyin.com",
            ],
            key="cookie",
        ),
        True: SimpleNamespace(
            name="TikTok",
            domain=[
                "tiktok.com",
            ],
            key="cookie_tiktok",
        ),
    }

    def __init__(self, parameters: "Parameter", cookie_object: "Cookie"):
        self.console = parameters.console
        self.cookie_object = cookie_object
        self.options = "\n".join(
            (
                f"{i}. {k}: {v[1]}"
                for i, (k, v) in enumerate(
                    self.SUPPORT_BROWSER.items(),
                    start=1,
                )
            )
        )

    def run(
        self,
        tiktok=False,
        select: str = None,
    ):
        if browser := (
            select
            or self.console.input(
                _(
                    "读取指定浏览器的 {platform_name} Cookie 并写入配置文件；\n"
                    "注意：Windows 系统需要以管理员身份运行程序才能读取 Chromium、Chrome、Edge 浏览器 Cookie！\n"
                    "{options}\n"
                    "请输入浏览器名称或序号："
                ).format(
                    platform_name=self.PLATFORM[tiktok].name, options=self.options
                ),
            )
        ):
            if cookie := self.get(
                browser,
                self.PLATFORM[tiktok].domain,
            ):
                self.console.info(
                    _("读取 Cookie 成功！"),
                )
                self.__save_cookie(
                    cookie,
                    tiktok,
                )
            else:
                self.console.warning(
                    _("Cookie 数据为空！"),
                )
        else:
            self.console.print(_("未选择浏览器！"))

    def __save_cookie(self, cookie: dict, tiktok: bool):
        self.cookie_object.save_cookie(cookie, self.PLATFORM[tiktok].key)

    def get(
        self,
        browser: str | int,
        domains: list[str],
    ) -> dict[str, str]:
        if not (browser := self.__browser_object(browser)):
            self.console.warning(
                _("浏览器名称或序号输入错误！"),
            )
            return {}
        try:
            cookies = browser(domains=domains)
            return {i["name"]: i["value"] for i in cookies}
        except RuntimeError:
            self.console.warning(
                _("读取 Cookie 失败，未找到 Cookie 数据！"),
            )
        return {}

    @classmethod
    def __browser_object(cls, browser: str | int):
        with suppress(ValueError):
            browser = int(browser) - 1
        if isinstance(browser, int):
            try:
                return list(cls.SUPPORT_BROWSER.values())[browser][0]
            except IndexError:
                return None
        if isinstance(browser, str):
            try:
                return cls.__match_browser(browser)
            except KeyError:
                return None
        raise TypeError

    @classmethod
    def __match_browser(cls, browser: str):
        for i, j in cls.SUPPORT_BROWSER.items():
            if i.lower() == browser.lower():
                return j[0]


match platform:
    case "darwin":
        from rookiepy import safari

        Browser.SUPPORT_BROWSER |= {
            "Safari": (safari, "macOS"),
        }
    case "linux":
        Browser.SUPPORT_BROWSER.pop("OperaGX")
    case "win32":
        pass
    case _:
        print(_("从浏览器读取 Cookie 功能不支持当前平台！"))
```

## File: `src/tools/capture.py`
```python
from json.decoder import JSONDecodeError
from ssl import SSLError
from typing import TYPE_CHECKING, Union

from httpx import HTTPStatusError, NetworkError, RequestError, TimeoutException

from ..translation import _

if TYPE_CHECKING:
    from ..record import BaseLogger, LoggerManager

__all__ = [
    "capture_error_params",
    "capture_error_request",
]


def capture_error_params(function):
    async def inner(logger: Union["BaseLogger", "LoggerManager"], *args, **kwargs):
        try:
            return await function(logger, *args, **kwargs)
        except (
            JSONDecodeError,
            UnicodeDecodeError,
        ):
            logger.error(_("响应内容不是有效的 JSON 数据"))
        except HTTPStatusError as e:
            logger.error(_("响应码异常：{error}").format(error=e))
        except NetworkError as e:
            logger.error(_("网络异常：{error}").format(error=e))
        except TimeoutException as e:
            logger.error(_("请求超时：{error}").format(error=e))
        except (
            RequestError,
            SSLError,
        ) as e:
            logger.error(_("网络异常：{error}").format(error=e))
        return None

    return inner


def capture_error_request(function):
    async def inner(self, *args, **kwargs):
        try:
            return await function(self, *args, **kwargs)
        except (JSONDecodeError, UnicodeDecodeError):
            self.log.error(_("响应内容不是有效的 JSON 数据，请尝试更新 Cookie！"))
        except HTTPStatusError as e:
            self.log.error(_("响应码异常：{error}").format(error=e))
        except NetworkError as e:
            self.log.error(_("网络异常：{error}").format(error=e))
        except TimeoutException as e:
            self.log.error(_("请求超时：{error}").format(error=e))
        except (
            RequestError,
            SSLError,
        ) as e:
            self.log.error(_("网络异常：{error}").format(error=e))
        return None

    return inner
```

## File: `src/tools/choose.py`
```python
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from rich.console import Console

    from src.tools import ColorfulConsole

__all__ = ["choose"]


def choose(
    title: str,
    options: tuple | list,
    console: Union["ColorfulConsole", "Console"],
    separate=None,
) -> str:
    screen = f"{title}:\n"
    for i, j in enumerate(options, start=1):
        screen += f"{i: >2d}. {j}\n"
        if separate and i in separate:
            screen += f"{'=' * 32}\n"
    return console.input(screen)
```

## File: `src/tools/cleaner.py`
```python
from platform import system
from re import compile
from string import whitespace

from emoji import replace_emoji

try:
    from ..translation import _
except ImportError:
    _ = lambda x: x

__all__ = ["Cleaner"]


class Cleaner:
    CONTROL_CHARACTERS = compile(r"[\x00-\x1F\x7F]")

    def __init__(self):
        """
        替换字符串中包含的非法字符，默认根据系统类型生成对应的非法字符字典，也可以自行设置非法字符字典
        """
        self.rule = self.default_rule()  # 默认非法字符字典

    @staticmethod
    def default_rule():
        """根据系统类型生成默认非法字符字典"""
        if (s := system()) in ("Windows", "Darwin"):
            rule = {
                "/": "",
                "\\": "",
                "|": "",
                "<": "",
                ">": "",
                '"': "",
                "?": "",
                ":": "",
                "*": "",
                "\x00": "",
            }  # Windows 系统和 Mac 系统
        elif s == "Linux":
            rule = {
                "/": "",
                "\x00": "",
            }  # Linux 系统
        else:
            print(_("不受支持的操作系统类型，可能无法正常去除非法字符！"))
            rule = {}
        cache = {i: "" for i in whitespace[1:]}  # 补充换行符等非法字符
        return rule | cache

    def set_rule(self, rule: dict[str, str], update=False):
        """
        设置非法字符字典

        :param rule: 替换规则，字典格式，键为非法字符，值为替换后的内容
        :param update: 如果是 True，则与原有规则字典合并，否则替换原有规则字典
        """
        self.rule = {**self.rule, **rule} if update else rule

    def filter(self, text: str) -> str:
        """
        去除非法字符

        :param text: 待处理的字符串
        :return: 替换后的字符串，如果替换后字符串为空，则返回 None
        """
        for i in self.rule:
            text = text.replace(i, self.rule[i])
        return text

    def filter_name(
        self,
        text: str,
        default: str = "",
    ) -> str:
        """过滤文件夹名称中的非法字符"""
        text = text.replace(":", ".")

        text = self.remove_control_characters(text)

        text = self.filter(text)

        text = replace_emoji(text)

        text = self.clear_spaces(text)

        text = text.strip().strip(".")

        return text or default

    @staticmethod
    def clear_spaces(string: str):
        """将连续的空格转换为单个空格"""
        return " ".join(string.split())

    @classmethod
    def remove_control_characters(
        cls,
        text,
        replace="",
    ):
        # 使用正则表达式匹配所有控制字符
        return cls.CONTROL_CHARACTERS.sub(
            replace,
            text,
        )


if __name__ == "__main__":
    demo = Cleaner()
    print(demo.rule)
    print(demo.filter_name(""))
    print(demo.remove_control_characters("hello \x08world"))
```

## File: `src/tools/console.py`
```python
from rich.console import Console
from rich.text import Text

from src.custom import (
    PROMPT,
    GENERAL,
    INFO,
    WARNING,
    ERROR,
    DEBUG,
)

__all__ = ["ColorfulConsole"]


class ColorfulConsole(Console):
    def __init__(self, *args, debug: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        self.debug_mode = debug

    def print(self, *args, style=GENERAL, highlight=False, **kwargs):
        super().print(*args, style=style, highlight=highlight, **kwargs)

    def info(self, *args, highlight=False, **kwargs):
        self.print(*args, style=INFO, highlight=highlight, **kwargs)

    def warning(self, *args, highlight=False, **kwargs):
        self.print(*args, style=WARNING, highlight=highlight, **kwargs)

    def error(self, *args, highlight=False, **kwargs):
        self.print(*args, style=ERROR, highlight=highlight, **kwargs)

    def debug(self, *args, highlight=False, **kwargs):
        if self.debug_mode:
            self.print(*args, style=DEBUG, highlight=highlight, **kwargs)

    def input(self, prompt="", style=PROMPT, *args, **kwargs):
        try:
            return super().input(Text(prompt, style=style), *args, **kwargs)
        except EOFError as e:
            raise KeyboardInterrupt from e
```

## File: `src/tools/error.py`
```python
from ..translation import _


class DownloaderError(Exception):
    def __init__(
        self,
        message: str = "",
    ):
        self.message = message or _("项目代码错误")
        super().__init__(self.message)

    def __str__(self):
        return f"DownloaderError: {self.message}"


class CacheError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
```

## File: `src/tools/file_folder.py`
```python
from contextlib import suppress
from pathlib import Path


def file_switch(path: Path) -> None:
    if path.exists():
        path.unlink()
    else:
        path.touch()


def remove_empty_directories(path: Path) -> None:
    exclude = {
        "\\.",
        "\\_",
        "\\__",
    }
    for dir_path, dir_names, file_names in path.walk(
        top_down=False,
    ):
        if any(i in str(dir_path) for i in exclude):
            continue
        if not dir_names and not file_names:
            with suppress(OSError):
                dir_path.rmdir()
```

## File: `src/tools/format.py`
```python
from http.cookiejar import CookieJar
from re import compile


def cookie_str_to_dict(cookie_str: str) -> dict:
    if not cookie_str:
        return {}
    cookie = {}
    pattern = compile(r"(?P<key>[^=;,]+)=(?P<value>[^;,]+)")
    matches = pattern.finditer(cookie_str)
    for match in matches:
        key = match.group("key").strip()
        value = match.group("value").strip()
        cookie[key] = value
    return cookie


def cookie_str_to_str(cookie_str: str) -> str:
    if not cookie_str:
        return ""
    pattern = compile(r", (?=\D)")
    return "; ".join(cookie.split("; ")[0] for cookie in pattern.split(cookie_str))


def cookie_dict_to_str(cookie_dict: dict | CookieJar) -> str:
    if not cookie_dict:
        return ""
    cookie_pairs = [f"{key}={value}" for key, value in cookie_dict.items()]
    return "; ".join(cookie_pairs)


def cookie_jar_to_dict(cookie_jar: CookieJar) -> dict:
    return {i.name: i.value for i in cookie_jar}


def format_size(size_in_bytes: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    index = 0
    while size_in_bytes >= 1024 and index < len(units) - 1:
        size_in_bytes /= 1024
        index += 1
    return f"{size_in_bytes:.2f} {units[index]}"


if __name__ == "__main__":
    print(format_size(0))
```

## File: `src/tools/list_pop.py`
```python
__all__ = ["safe_pop"]


def safe_pop(data: list):
    return data.pop() if data else None
```

## File: `src/tools/progress.py`
```python
class FakeProgress:
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        pass

    async def __aenter__(self):
        return self

    def __enter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def add_task(
        self,
        *args,
        **kwargs,
    ):
        pass

    def update(
        self,
        *args,
        **kwargs,
    ):
        pass

    def remove_task(
        self,
        *args,
        **kwargs,
    ):
        pass
```

## File: `src/tools/rename_compatible.py`
```python
from ..custom import PROJECT_ROOT
from shutil import copy2


class RenameCompatible:
    OLD_DB_FILE = PROJECT_ROOT.joinpath("TikTokDownloader.db")
    NEW_DB_FILE = PROJECT_ROOT.joinpath("DouK-Downloader.db")

    @classmethod
    def migration_file(
        cls,
    ):
        if cls.OLD_DB_FILE.exists() and not cls.NEW_DB_FILE.exists():
            copy2(cls.OLD_DB_FILE.resolve(), cls.NEW_DB_FILE.resolve())
```

## File: `src/tools/retry.py`
```python
from ..custom import RETRY, wait
from ..translation import _

__all__ = ["Retry"]


class Retry:
    """重试器，仅适用于本项目！"""

    @staticmethod
    def retry(function):
        """发生错误时尝试重新执行，装饰的函数需要返回布尔值"""

        async def inner(self, *args, **kwargs):
            finished = kwargs.pop("finished", False)
            for i in range(self.max_retry):
                if result := await function(self, *args, **kwargs):
                    return result
                self.log.warning(_("正在进行第 {index} 次重试").format(index=i + 1))
                await wait()
            if not (result := await function(self, *args, **kwargs)) and finished:
                self.finished = True
            return result

        return inner

    @staticmethod
    def retry_lite(function):
        async def inner(*args, **kwargs):
            if r := await function(*args, **kwargs):
                return r
            for _ in range(RETRY):
                if r := await function(*args, **kwargs):
                    return r
                await wait()
            return r

        return inner

    @staticmethod
    def retry_limited(function):
        def inner(self, *args, **kwargs):
            while True:
                if function(self, *args, **kwargs):
                    return
                if self.console.input(
                    _(
                        "如需重新尝试处理该对象，请关闭所有正在访问该对象的窗口或程序，然后直接按下回车键！\n"
                        "如需跳过处理该对象，请输入任意字符后按下回车键！"
                    ),
                ):
                    return

        return inner

    @staticmethod
    def retry_infinite(function):
        def inner(self, *args, **kwargs):
            while True:
                if function(self, *args, **kwargs):
                    return
                self.console.input(
                    _("请关闭所有正在访问该对象的窗口或程序，然后按下回车键继续处理！")
                )

        return inner
```

## File: `src/tools/session.py`
```python
from typing import TYPE_CHECKING, Union

from httpx import AsyncClient, AsyncHTTPTransport, Client, HTTPTransport

from ..custom import TIMEOUT, USERAGENT
from ..tools import DownloaderError
from .capture import capture_error_params
from .retry import Retry

if TYPE_CHECKING:
    from ..record import BaseLogger, LoggerManager
    from ..testers import Logger

__all__ = ["request_params", "create_client"]


def create_client(
    user_agent=USERAGENT,
    timeout=TIMEOUT,
    headers: dict = None,
    proxy: str = None,
    *args,
    **kwargs,
) -> AsyncClient:
    return AsyncClient(
        headers=headers
        or {
            "User-Agent": user_agent,
        },
        timeout=timeout,
        follow_redirects=True,
        verify=False,
        mounts={
            "http://": AsyncHTTPTransport(proxy=proxy),
            "https://": AsyncHTTPTransport(proxy=proxy),
        },
        *args,
        **kwargs,
    )


async def request_params(
    logger: Union[
        "BaseLogger",
        "LoggerManager",
        "Logger",
    ],
    url: str,
    method: str = "POST",
    params: dict | str = None,
    data: dict | str = None,
    useragent=USERAGENT,
    timeout=TIMEOUT,
    headers: dict = None,
    resp="headers",
    proxy: str = None,
    **kwargs,
):
    with Client(
        headers=headers
        or {
            "User-Agent": useragent,
            "Content-Type": "application/json; charset=utf-8",
            # "Referer": "https://www.douyin.com/"
        },
        follow_redirects=True,
        timeout=timeout,
        verify=False,
        mounts={
            "http://": HTTPTransport(proxy=proxy),
            "https://": HTTPTransport(proxy=proxy),
        },
    ) as client:
        return await request(
            logger,
            client,
            method,
            url,
            resp,
            params=params,
            data=data,
            **kwargs,
        )


@Retry.retry_lite
@capture_error_params
async def request(
    logger: Union[
        "BaseLogger",
        "LoggerManager",
        "Logger",
    ],
    client: Client,
    method: str,
    url: str,
    resp="json",
    **kwargs,
):
    response = client.request(method, url, **kwargs)
    response.raise_for_status()
    match resp:
        case "headers":
            return response.headers
        case "text":
            return response.text
        case "content":
            return response.content
        case "json":
            return response.json()
        case "url":
            return str(response.url)
        case "response":
            return response
        case _:
            raise DownloaderError
```

## File: `src/tools/temporary.py`
```python
from random import choice
from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits,
)
from time import time

CHARACTER = ascii_lowercase + ascii_uppercase + digits


def timestamp() -> str:
    return str(time())[:10]


def random_string(length: int = 10) -> str:
    return "".join(choice(CHARACTER) for _ in range(length))


if __name__ == "__main__":
    print(timestamp())
    print(random_string())
```

## File: `src/tools/timer.py`
```python
from time import time

__all__ = ["run_time"]


def run_time(function):
    def inner(self, *args, **kwargs):
        start = time()
        result = function(self, *args, **kwargs)
        print(f"{function.__name__}运行耗时: {time() - start}s")
        return result

    return inner
```

## File: `src/tools/truncate.py`
```python
from unicodedata import name


def is_chinese_char(char: str) -> bool:
    return "CJK" in name(char, "")


def truncate_string(s: str, length: int = 64) -> str:
    count = 0
    result = ""
    for char in s:
        count += 2 if is_chinese_char(char) else 1
        if count > length:
            break
        result += char
    return result


def trim_string(s: str, length: int = 64) -> str:
    length = length // 2 - 2
    return f"{s[:length]}...{s[-length:]}" if len(s) > length else s


def beautify_string(s: str, length: int = 64) -> str:
    count = 0
    for char in s:
        count += 2 if is_chinese_char(char) else 1
        if count > length:
            break
    else:
        return s
    length //= 2
    start = truncate_string(s, length)
    end = truncate_string(s[::-1], length)[::-1]
    return f"{start}...{end}"
```

## File: `src/tools/__init__.py`
```python
from .browser import Browser
from .capture import capture_error_params
from .capture import capture_error_request
from .choose import choose
from .cleaner import Cleaner
from .console import ColorfulConsole
from .error import CacheError
from .error import DownloaderError
from .file_folder import file_switch
from .file_folder import remove_empty_directories
from .format import (
    cookie_dict_to_str,
    cookie_str_to_dict,
    cookie_jar_to_dict,
    cookie_str_to_str,
    format_size,
)
from .list_pop import safe_pop
from .retry import Retry
from .session import (
    request_params,
    create_client,
)
from .temporary import random_string
from .temporary import timestamp
from .timer import run_time
from .truncate import beautify_string
from .truncate import trim_string
from .truncate import truncate_string
from .rename_compatible import RenameCompatible
from .progress import FakeProgress
```

## File: `src/translation/static.py`
```python
TRANSLATE_MAP = {
    "发布作品": "Posts",
    "喜欢作品": "Liked",
    "收藏作品": "Favorites",
    "收藏夹": "Collections",
    "收藏夹作品": "Collections Works",
    "收藏音乐": "Collections Music",
    "收藏合集": "Collections Mix",
    "收藏短剧": "Collections Series",
    "作品": "Works",
    "合集": "Mix",
    "合辑": "Mix",
    "热榜": "HotBoard",
    "实况": "LivePhoto",
}
```

## File: `src/translation/translate.py`
```python
from gettext import translation
from locale import getlocale
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


class TranslationManager:
    """管理gettext翻译的类"""

    _instance = None  # 单例实例

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TranslationManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, domain="tk", localedir=None):
        self.domain = domain
        if not localedir:
            localedir = ROOT.joinpath("locale")
        self.localedir = Path(localedir)
        self.current_translator = self.setup_translation(
            self.get_language_code(),
        )

    @staticmethod
    def get_language_code() -> str:
        # 获取当前系统的语言和区域设置
        language_code, __ = getlocale()
        if not language_code:
            return "en_US"
        return (
            "zh_CN"
            if any(
                s in language_code.upper()
                for s in (
                    "CHINESE",
                    "ZH",
                    "CHINA",
                )
            )
            else "en_US"
        )

    def setup_translation(self, language: str = "zh_CN"):
        """设置gettext翻译环境"""
        try:
            return translation(
                self.domain,
                localedir=self.localedir,
                languages=[language],
                fallback=True,
            )
        except FileNotFoundError as e:
            print(
                f"Warning: Translation files for '{self.domain}' not found. Error: {e}"
            )
            return translation(self.domain, fallback=True)

    def switch_language(self, language: str = "en_US"):
        """切换当前使用的语言"""
        self.current_translator = self.setup_translation(language)

    def gettext(self, message):
        """提供gettext方法"""
        return self.current_translator.gettext(message)


# 初始化TranslationManager单例实例
translation_manager = TranslationManager()


def _translate(message):
    """辅助函数来简化翻译调用"""
    return translation_manager.gettext(message)


def switch_language(language: str = "en_US"):
    """切换语言并刷新翻译函数"""
    global _
    translation_manager.switch_language(language)
    _ = translation_manager.gettext


# 设置默认翻译函数
_ = _translate
```

## File: `src/translation/__init__.py`
```python
from .translate import switch_language, _
```

## File: `src/tui_edition/app.py`
```python
__all__ = ["App"]


class App:
    pass
```

## File: `src/tui_edition/setting.py`
```python
__all__ = ["Setting"]


class Setting:
    pass
```

## File: `src/tui_edition/__init__.py`
```python
from .app import App

__all__ = ["App"]
```

## File: `static/js/a_bogus.js`
```javascript
// All the content in this article is only for learning and communication use, not for any other purpose, strictly prohibited for commercial use and illegal use, otherwise all the consequences are irrelevant to the author!
function rc4_encrypt(plaintext, key) {
    var s = [];
    for (var i = 0; i < 256; i++) {
        s[i] = i;
    }
    var j = 0;
    for (var i = 0; i < 256; i++) {
        j = (j + s[i] + key.charCodeAt(i % key.length)) % 256;
        var temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }

    var i = 0;
    var j = 0;
    var cipher = [];
    for (var k = 0; k < plaintext.length; k++) {
        i = (i + 1) % 256;
        j = (j + s[i]) % 256;
        var temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        var t = (s[i] + s[j]) % 256;
        cipher.push(String.fromCharCode(s[t] ^ plaintext.charCodeAt(k)));
    }
    return cipher.join('');
}

function le(e, r) {
    return (e << (r %= 32) | e >>> 32 - r) >>> 0
}

function de(e) {
    return 0 <= e && e < 16 ? 2043430169 : 16 <= e && e < 64 ? 2055708042 : void console['error']("invalid j for constant Tj")
}

function pe(e, r, t, n) {
    return 0 <= e && e < 16 ? (r ^ t ^ n) >>> 0 : 16 <= e && e < 64 ? (r & t | r & n | t & n) >>> 0 : (console['error']('invalid j for bool function FF'),
        0)
}

function he(e, r, t, n) {
    return 0 <= e && e < 16 ? (r ^ t ^ n) >>> 0 : 16 <= e && e < 64 ? (r & t | ~r & n) >>> 0 : (console['error']('invalid j for bool function GG'),
        0)
}

function reset() {
    this.reg[0] = 1937774191,
        this.reg[1] = 1226093241,
        this.reg[2] = 388252375,
        this.reg[3] = 3666478592,
        this.reg[4] = 2842636476,
        this.reg[5] = 372324522,
        this.reg[6] = 3817729613,
        this.reg[7] = 2969243214,
        this["chunk"] = [],
        this["size"] = 0
}

function write(e) {
    var a = "string" == typeof e ? function (e) {
        n = encodeURIComponent(e)['replace'](/%([0-9A-F]{2})/g, (function (e, r) {
                return String['fromCharCode']("0x" + r)
            }
        ))
            , a = new Array(n['length']);
        return Array['prototype']['forEach']['call'](n, (function (e, r) {
                a[r] = e.charCodeAt(0)
            }
        )),
            a
    }(e) : e;
    this.size += a.length;
    var f = 64 - this['chunk']['length'];
    if (a['length'] < f)
        this['chunk'] = this['chunk'].concat(a);
    else
        for (this['chunk'] = this['chunk'].concat(a.slice(0, f)); this['chunk'].length >= 64;)
            this['_compress'](this['chunk']),
                f < a['length'] ? this['chunk'] = a['slice'](f, Math['min'](f + 64, a['length'])) : this['chunk'] = [],
                f += 64
}

function sum(e, t) {
    e && (this['reset'](),
        this['write'](e)),
        this['_fill']();
    for (var f = 0; f < this.chunk['length']; f += 64)
        this._compress(this['chunk']['slice'](f, f + 64));
    var i = null;
    if (t == 'hex') {
        i = "";
        for (f = 0; f < 8; f++)
            i += se(this['reg'][f]['toString'](16), 8, "0")
    } else
        for (i = new Array(32),
                 f = 0; f < 8; f++) {
            var c = this.reg[f];
            i[4 * f + 3] = (255 & c) >>> 0,
                c >>>= 8,
                i[4 * f + 2] = (255 & c) >>> 0,
                c >>>= 8,
                i[4 * f + 1] = (255 & c) >>> 0,
                c >>>= 8,
                i[4 * f] = (255 & c) >>> 0
        }
    return this['reset'](),
        i
}

function _compress(t) {
    if (t < 64)
        console.error("compress error: not enough data");
    else {
        for (var f = function (e) {
            for (var r = new Array(132), t = 0; t < 16; t++)
                r[t] = e[4 * t] << 24,
                    r[t] |= e[4 * t + 1] << 16,
                    r[t] |= e[4 * t + 2] << 8,
                    r[t] |= e[4 * t + 3],
                    r[t] >>>= 0;
            for (var n = 16; n < 68; n++) {
                var a = r[n - 16] ^ r[n - 9] ^ le(r[n - 3], 15);
                a = a ^ le(a, 15) ^ le(a, 23),
                    r[n] = (a ^ le(r[n - 13], 7) ^ r[n - 6]) >>> 0
            }
            for (n = 0; n < 64; n++)
                r[n + 68] = (r[n] ^ r[n + 4]) >>> 0;
            return r
        }(t), i = this['reg'].slice(0), c = 0; c < 64; c++) {
            var o = le(i[0], 12) + i[4] + le(de(c), c)
                , s = ((o = le(o = (4294967295 & o) >>> 0, 7)) ^ le(i[0], 12)) >>> 0
                , u = pe(c, i[0], i[1], i[2]);
            u = (4294967295 & (u = u + i[3] + s + f[c + 68])) >>> 0;
            var b = he(c, i[4], i[5], i[6]);
            b = (4294967295 & (b = b + i[7] + o + f[c])) >>> 0,
                i[3] = i[2],
                i[2] = le(i[1], 9),
                i[1] = i[0],
                i[0] = u,
                i[7] = i[6],
                i[6] = le(i[5], 19),
                i[5] = i[4],
                i[4] = (b ^ le(b, 9) ^ le(b, 17)) >>> 0
        }
        for (var l = 0; l < 8; l++)
            this['reg'][l] = (this['reg'][l] ^ i[l]) >>> 0
    }
}

function _fill() {
    var a = 8 * this['size']
        , f = this['chunk']['push'](128) % 64;
    for (64 - f < 8 && (f -= 64); f < 56; f++)
        this.chunk['push'](0);
    for (var i = 0; i < 4; i++) {
        var c = Math['floor'](a / 4294967296);
        this['chunk'].push(c >>> 8 * (3 - i) & 255)
    }
    for (i = 0; i < 4; i++)
        this['chunk']['push'](a >>> 8 * (3 - i) & 255)

}

function SM3() {
    this.reg = [];
    this.chunk = [];
    this.size = 0;
    this.reset()
}
SM3.prototype.reset = reset;
SM3.prototype.write = write;
SM3.prototype.sum = sum;
SM3.prototype._compress = _compress;
SM3.prototype._fill = _fill;

function result_encrypt(long_str, num = null) {
    let s_obj = {
        "s0": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
        "s1": "Dkdpgh4ZKsQB80/Mfvw36XI1R25+WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe=",
        "s2": "Dkdpgh4ZKsQB80/Mfvw36XI1R25-WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe=",
        "s3": "ckdp1h4ZKsUB80/Mfvw36XIgR25+WQAlEi7NLboqYTOPuzmFjJnryx9HVGDaStCe",
        "s4": "Dkdpgh2ZmsQB80/MfvV36XI1R45-WUAlEixNLwoqYTOPuzKFjJnry79HbGcaStCe"
    }
    let constant = {
        "0": 16515072,
        "1": 258048,
        "2": 4032,
        "str": s_obj[num],
    }

    let result = "";
    let lound = 0;
    let long_int = get_long_int(lound, long_str);
    for (let i = 0; i < long_str.length / 3 * 4; i++) {
        if (Math.floor(i / 4) !== lound) {
            lound += 1;
            long_int = get_long_int(lound, long_str);
        }
        let key = i % 4;
        switch (key) {
            case 0:
                temp_int = (long_int & constant["0"]) >> 18;
                result += constant["str"].charAt(temp_int);
                break;
            case 1:
                temp_int = (long_int & constant["1"]) >> 12;
                result += constant["str"].charAt(temp_int);
                break;
            case 2:
                temp_int = (long_int & constant["2"]) >> 6;
                result += constant["str"].charAt(temp_int);
                break;
            case 3:
                temp_int = long_int & 63;
                result += constant["str"].charAt(temp_int);
                break;
            default:
                break;
        }
    }
    return result;
}

function get_long_int(round, long_str) {
    round = round * 3;
    return (long_str.charCodeAt(round) << 16) | (long_str.charCodeAt(round + 1) << 8) | (long_str.charCodeAt(round + 2));
}

function gener_random(random, option) {
    return [
        (random & 255 & 170) | option[0] & 85, // 163
        (random & 255 & 85) | option[0] & 170, //87
        (random >> 8 & 255 & 170) | option[1] & 85, //37
        (random >> 8 & 255 & 85) | option[1] & 170, //41
    ]
}

//////////////////////////////////////////////
function generate_rc4_bb_str(url_search_params, user_agent, window_env_str, suffix = "cus", Arguments = [0, 1, 14]) {
    let sm3 = new SM3()
    let start_time = Date.now()
    /**
     * 进行3次加密处理
     * 1: url_search_params两次sm3之的结果
     * 2: 对后缀两次sm3之的结果
     * 3: 对ua处理之后的结果
     */
        // url_search_params两次sm3之的结果
    let url_search_params_list = sm3.sum(sm3.sum(url_search_params + suffix))
    // 对后缀两次sm3之的结果
    let cus = sm3.sum(sm3.sum(suffix))
    // 对ua处理之后的结果
    let ua = sm3.sum(result_encrypt(rc4_encrypt(user_agent, String.fromCharCode.apply(null, [0.00390625, 1, 14])), "s3"))
    //
    let end_time = Date.now()
    // b
    let b = {
        8: 3, // 固定
        10: end_time, //3次加密结束时间
        15: {
            "aid": 6383,
            "pageId": 6241,
            "boe": false,
            "ddrt": 7,
            "paths": {
                "include": [
                    {},
                    {},
                    {},
                    {},
                    {},
                    {},
                    {}
                ],
                "exclude": []
            },
            "track": {
                "mode": 0,
                "delay": 300,
                "paths": []
            },
            "dump": true,
            "rpU": ""
        },
        16: start_time, //3次加密开始时间
        18: 44, //固定
        19: [1, 0, 1, 5],
    }

    //3次加密开始时间
    b[20] = (b[16] >> 24) & 255
    b[21] = (b[16] >> 16) & 255
    b[22] = (b[16] >> 8) & 255
    b[23] = b[16] & 255
    b[24] = (b[16] / 256 / 256 / 256 / 256) >> 0
    b[25] = (b[16] / 256 / 256 / 256 / 256 / 256) >> 0

    // 参数Arguments [0, 1, 14, ...]
    // let Arguments = [0, 1, 14]
    b[26] = (Arguments[0] >> 24) & 255
    b[27] = (Arguments[0] >> 16) & 255
    b[28] = (Arguments[0] >> 8) & 255
    b[29] = Arguments[0] & 255

    b[30] = (Arguments[1] / 256) & 255
    b[31] = (Arguments[1] % 256) & 255
    b[32] = (Arguments[1] >> 24) & 255
    b[33] = (Arguments[1] >> 16) & 255

    b[34] = (Arguments[2] >> 24) & 255
    b[35] = (Arguments[2] >> 16) & 255
    b[36] = (Arguments[2] >> 8) & 255
    b[37] = Arguments[2] & 255

    // (url_search_params + "cus") 两次sm3之的结果
    /**let url_search_params_list = [
     91, 186,  35,  86, 143, 253,   6,  76,
     34,  21, 167, 148,   7,  42, 192, 219,
     188,  20, 182,  85, 213,  74, 213, 147,
     37, 155,  93, 139,  85, 118, 228, 213
     ]*/
    b[38] = url_search_params_list[21]
    b[39] = url_search_params_list[22]

    // ("cus") 对后缀两次sm3之的结果
    /**
     * let cus = [
     136, 101, 114, 147,  58,  77, 207, 201,
     215, 162, 154,  93, 248,  13, 142, 160,
     105,  73, 215, 241,  83,  58,  51,  43,
     255,  38, 168, 141, 216, 194,  35, 236
     ]*/
    b[40] = cus[21]
    b[41] = cus[22]

    // 对ua处理之后的结果
    /**
     * let ua = [
     129, 190,  70, 186,  86, 196, 199,  53,
     99,  38,  29, 209, 243,  17, 157,  69,
     147, 104,  53,  23, 114, 126,  66, 228,
     135,  30, 168, 185, 109, 156, 251,  88
     ]*/
    b[42] = ua[23]
    b[43] = ua[24]

    //3次加密结束时间
    b[44] = (b[10] >> 24) & 255
    b[45] = (b[10] >> 16) & 255
    b[46] = (b[10] >> 8) & 255
    b[47] = b[10] & 255
    b[48] = b[8]
    b[49] = (b[10] / 256 / 256 / 256 / 256) >> 0
    b[50] = (b[10] / 256 / 256 / 256 / 256 / 256) >> 0


    // object配置项
    b[51] = b[15]['pageId']
    b[52] = (b[15]['pageId'] >> 24) & 255
    b[53] = (b[15]['pageId'] >> 16) & 255
    b[54] = (b[15]['pageId'] >> 8) & 255
    b[55] = b[15]['pageId'] & 255

    b[56] = b[15]['aid']
    b[57] = b[15]['aid'] & 255
    b[58] = (b[15]['aid'] >> 8) & 255
    b[59] = (b[15]['aid'] >> 16) & 255
    b[60] = (b[15]['aid'] >> 24) & 255

    // 中间进行了环境检测
    // 代码索引:  2496 索引值:  17 （索引64关键条件）
    // '1536|747|1536|834|0|30|0|0|1536|834|1536|864|1525|747|24|24|Win32'.charCodeAt()得到65位数组
    /**
     * let window_env_list = [49, 53, 51, 54, 124, 55, 52, 55, 124, 49, 53, 51, 54, 124, 56, 51, 52, 124, 48, 124, 51,
     * 48, 124, 48, 124, 48, 124, 49, 53, 51, 54, 124, 56, 51, 52, 124, 49, 53, 51, 54, 124, 56,
     * 54, 52, 124, 49, 53, 50, 53, 124, 55, 52, 55, 124, 50, 52, 124, 50, 52, 124, 87, 105, 110,
     * 51, 50]
     */
    let window_env_list = [];
    for (let index = 0; index < window_env_str.length; index++) {
        window_env_list.push(window_env_str.charCodeAt(index))
    }
    b[64] = window_env_list.length
    b[65] = b[64] & 255
    b[66] = (b[64] >> 8) & 255

    b[69] = [].length
    b[70] = b[69] & 255
    b[71] = (b[69] >> 8) & 255

    b[72] = b[18] ^ b[20] ^ b[26] ^ b[30] ^ b[38] ^ b[40] ^ b[42] ^ b[21] ^ b[27] ^ b[31] ^ b[35] ^ b[39] ^ b[41] ^ b[43] ^ b[22] ^
        b[28] ^ b[32] ^ b[36] ^ b[23] ^ b[29] ^ b[33] ^ b[37] ^ b[44] ^ b[45] ^ b[46] ^ b[47] ^ b[48] ^ b[49] ^ b[50] ^ b[24] ^
        b[25] ^ b[52] ^ b[53] ^ b[54] ^ b[55] ^ b[57] ^ b[58] ^ b[59] ^ b[60] ^ b[65] ^ b[66] ^ b[70] ^ b[71]
    let bb = [
        b[18], b[20], b[52], b[26], b[30], b[34], b[58], b[38], b[40], b[53], b[42], b[21], b[27], b[54], b[55], b[31],
        b[35], b[57], b[39], b[41], b[43], b[22], b[28], b[32], b[60], b[36], b[23], b[29], b[33], b[37], b[44], b[45],
        b[59], b[46], b[47], b[48], b[49], b[50], b[24], b[25], b[65], b[66], b[70], b[71]
    ]
    bb = bb.concat(window_env_list).concat(b[72])
    return rc4_encrypt(String.fromCharCode.apply(null, bb), String.fromCharCode.apply(null, [121]));
}

function generate_random_str() {
    let random_str_list = []
    random_str_list = random_str_list.concat(gener_random(Math.random() * 10000, [3, 45]))
    random_str_list = random_str_list.concat(gener_random(Math.random() * 10000, [1, 0]))
    random_str_list = random_str_list.concat(gener_random(Math.random() * 10000, [1, 5]))
    return String.fromCharCode.apply(null, random_str_list)
}

function generate_a_bogus(url_search_params, user_agent) {
    /**
     * url_search_params："device_platform=webapp&aid=6383&channel=channel_pc_web&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=123.0.0.0&browser_online=true&engine_name=Blink&engine_version=123.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7362810250930783783&msToken=VkDUvz1y24CppXSl80iFPr6ez-3FiizcwD7fI1OqBt6IICq9RWG7nCvxKb8IVi55mFd-wnqoNkXGnxHrikQb4PuKob5Q-YhDp5Um215JzlBszkUyiEvR"
     * user_agent："Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
     */
    let result_str = generate_random_str() + generate_rc4_bb_str(
        url_search_params,
        user_agent,
        "1536|747|1536|834|0|30|0|0|1536|834|1536|864|1525|747|24|24|Win32"
    );
    return result_encrypt(result_str, "s4") + "=";
}

//测试调用
// console.log(generate_a_bogus(
//     "device_platform=webapp&aid=6383&channel=channel_pc_web&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=123.0.0.0&browser_online=true&engine_name=Blink&engine_version=123.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7362810250930783783&msToken=VkDUvz1y24CppXSl80iFPr6ez-3FiizcwD7fI1OqBt6IICq9RWG7nCvxKb8IVi55mFd-wnqoNkXGnxHrikQb4PuKob5Q-YhDp5Um215JzlBszkUyiEvR",
//     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
// ));
```

## File: `static/js/X-Bogus.js`
```javascript
var window = null;

function _0x5cd844(e) {
    var b = {
        exports: {}
    };
    return e(b, b.exports), b.exports
}

jsvmp = function (e, b, a) {
    function f(e, b, a) {
        return (f = function () {
            if ("undefined" == typeof Reflect || !Reflect.construct || Reflect.construct.sham) return !1;
            if ("function" == typeof Proxy) return !0;
            try {
                return Date.prototype.toString.call(Reflect.construct(Date, [], function () {
                })), !0
            } catch (e) {
                return !1
            }
        }() ? Reflect.construct : function (e, b, a) {
            var f = [null];
            f.push.apply(f, b);
            var c = new (Function.bind.apply(e, f));
            return a && function (e, b) {
                (Object.setPrototypeOf || function (e, b) {
                    return e.__proto__ = b, e
                })(e, b)
            }(c, a.prototype), c
        }).apply(null, arguments)
    }

    function c(e) {
        return function (e) {
            if (Array.isArray(e)) {
                for (var b = 0, a = new Array(e.length); b < e.length; b++) a[b] = e[b];
                return a
            }
        }(e) || function (e) {
            if (Symbol.iterator in Object(e) || "[object Arguments]" === Object.prototype.toString.call(e)) return Array.from(e)
        }(e) || function () {
            throw new TypeError("Invalid attempt to spread non-iterable instance")
        }()
    }

    for (var r = [], t = 0, d = [], i = 0, n = function (e, b) {
        var a = e[b++],
            f = e[b],
            c = parseInt("" + a + f, 16);
        if (c >> 7 == 0) return [1, c];
        if (c >> 6 == 2) {
            var r = parseInt("" + e[++b] + e[++b], 16);
            return c &= 63, [2, r = (c <<= 8) + r]
        }
        if (c >> 6 == 3) {
            var t = parseInt("" + e[++b] + e[++b], 16),
                d = parseInt("" + e[++b] + e[++b], 16);
            return c &= 63, [3, d = (c <<= 16) + (t <<= 8) + d]
        }
    }, s = function (e, b) {
        var a = parseInt("" + e[b] + e[b + 1], 16);
        return a > 127 ? -256 + a : a
    }, o = function (e, b) {
        var a = parseInt("" + e[b] + e[b + 1] + e[b + 2] + e[b + 3], 16);
        return a > 32767 ? -65536 + a : a
    }, l = function (e, b) {
        var a = parseInt("" + e[b] + e[b + 1] + e[b + 2] + e[b + 3] + e[b + 4] + e[b + 5] + e[b + 6] + e[b + 7], 16);
        return a > 2147483647 ? 0 + a : a
    }, _ = function (e, b) {
        return parseInt("" + e[b] + e[b + 1], 16)
    }, x = function (e, b) {
        return parseInt("" + e[b] + e[b + 1] + e[b + 2] + e[b + 3], 16)
    }, u = u || this || window, h = (e.length, 0), p = "", y = h; y < h + 16; y++) {
        var v = "" + e[y++] + e[y];
        v = parseInt(v, 16), p += String.fromCharCode(v)
    }
    if ("HNOJ@?RC" != p) throw new Error("error magic number " + p);
    parseInt("" + e[h += 16] + e[h + 1], 16), h += 8, t = 0;
    for (var g = 0; g < 4; g++) {
        var w = h + 2 * g,
            A = parseInt("" + e[w++] + e[w], 16);
        t += (3 & A) << 2 * g
    }
    h += 16;
    var C = parseInt("" + e[h += 8] + e[h + 1] + e[h + 2] + e[h + 3] + e[h + 4] + e[h + 5] + e[h + 6] + e[h + 7], 16),
        m = C,
        S = h += 8,
        z = x(e, h += C);
    z[1], h += 4, r = {
        p: [],
        q: []
    };
    for (var B = 0; B < z; B++) {
        for (var R = n(e, h), q = h += 2 * R[0], I = r.p.length, k = 0; k < R[1]; k++) {
            var j = n(e, q);
            r.p.push(j[1]), q += 2 * j[0]
        }
        h = q, r.q.push([I, r.p.length])
    }
    var O = {
            5: 1,
            6: 1,
            70: 1,
            22: 1,
            23: 1,
            37: 1,
            73: 1
        },
        U = {
            72: 1
        },
        D = {
            74: 1
        },
        N = {
            11: 1,
            12: 1,
            24: 1,
            26: 1,
            27: 1,
            31: 1
        },
        J = {
            10: 1
        },
        L = {
            2: 1,
            29: 1,
            30: 1,
            20: 1
        },
        T = [],
        E = [];

    function M(e, b, a) {
        for (var f = b; f < b + a;) {
            var c = _(e, f);
            T[f] = c, f += 2, U[c] ? (E[f] = s(e, f), f += 2) : O[c] ? (E[f] = o(e, f), f += 4) : D[c] ? (E[f] = l(e, f), f += 8) : N[c] ? (E[f] = _(e, f), f += 2) : J[c] ? (E[f] = x(e, f), f += 4) : L[c] && (E[f] = x(e, f), f += 4)
        }
    }

    return F(e, S, m / 2, [], b, a);

    function P(e, b, a, n, h, p, y, v) {
        null == p && (p = this);
        var g, w, A, C, m = [],
            S = 0;
        y && (w = y);
        var z, B, R = b,
            q = R + 2 * a;
        if (!v)
            for (; R < q;) {
                var I = parseInt("" + e[R] + e[R + 1], 16);
                R += 2;
                var j = 3 & (z = 13 * I % 241);
                if (z >>= 2, j < 1)
                    if (j = 3 & z, z >>= 2, j < 1) {
                        if ((j = z) < 1) return [1, m[S--]];
                        j < 5 ? (w = m[S--], m[S] = m[S] * w) : j < 7 ? (w = m[S--], m[S] = m[S] != w) : j < 14 ? (A = m[S--], C = m[S--], (j = m[S--]).x === P ? j.y >= 1 ? m[++S] = F(e, j.c, j.l, A, j.z, C, null, 1) : (m[++S] = F(e, j.c, j.l, A, j.z, C, null, 0), j.y++) : m[++S] = j.apply(C, A)) : j < 16 && (B = o(e, R), (g = function b() {
                            var a = arguments;
                            return b.y > 0 || b.y++, F(e, b.c, b.l, a, b.z, this, null, 0)
                        }).c = R + 4, g.l = B - 2, g.x = P, g.y = 0, g.z = h, m[S] = g, R += 2 * B - 2)
                    } else if (j < 2) (j = z) > 8 ? (w = m[S--], m[S] = typeof w) : j > 4 ? m[S -= 1] = m[S][m[S + 1]] : j > 2 && (A = m[S--], (j = m[S]).x === P ? j.y >= 1 ? m[S] = F(e, j.c, j.l, [A], j.z, C, null, 1) : (m[S] = F(e, j.c, j.l, [A], j.z, C, null, 0), j.y++) : m[S] = j(A));
                    else if (j < 3) {
                        if ((j = z) < 9) {
                            for (w = m[S--], B = x(e, R), j = "", k = r.q[B][0]; k < r.q[B][1]; k++) j += String.fromCharCode(t ^ r.p[k]);
                            R += 4, m[S--][j] = w
                        } else if (j < 13) throw m[S--]
                    } else (j = z) < 1 ? m[++S] = null : j < 3 ? (w = m[S--], m[S] = m[S] >= w) : j < 12 && (m[++S] = void 0);
                else if (j < 2)
                    if (j = 3 & z, z >>= 2, j < 1)
                        if ((j = z) < 5) {
                            B = o(e, R);
                            try {
                                if (d[i][2] = 1, 1 == (w = P(e, R + 4, B - 3, [], h, p, null, 0))[0]) return w
                            } catch (b) {
                                if (d[i] && d[i][1] && 1 == (w = P(e, d[i][1][0], d[i][1][1], [], h, p, b, 0))[0]) return w
                            } finally {
                                if (d[i] && d[i][0] && 1 == (w = P(e, d[i][0][0], d[i][0][1], [], h, p, null, 0))[0]) return w;
                                d[i] = 0, i--
                            }
                            R += 2 * B - 2
                        } else j < 7 ? (B = _(e, R), R += 2, m[S -= B] = 0 === B ? new m[S] : f(m[S], c(m.slice(S + 1, S + B + 1)))) : j < 9 && (w = m[S--], m[S] = m[S] & w);
                    else if (j < 2)
                        if ((j = z) > 12) m[++S] = s(e, R), R += 2;
                        else if (j > 10) w = m[S--], m[S] = m[S] << w;
                        else if (j > 8) {
                            for (B = x(e, R), j = "", k = r.q[B][0]; k < r.q[B][1]; k++) j += String.fromCharCode(t ^ r.p[k]);
                            R += 4, m[S] = m[S][j]
                        } else j > 6 && (A = m[S--], w = delete m[S--][A]);
                    else if (j < 3) (j = z) < 2 ? m[++S] = w : j < 11 ? (w = m[S -= 2][m[S + 1]] = m[S + 2], S--) : j < 13 && (w = m[S], m[++S] = w);
                    else if ((j = z) > 12) m[++S] = p;
                    else if (j > 5) w = m[S--], m[S] = m[S] !== w;
                    else if (j > 3) w = m[S--], m[S] = m[S] / w;
                    else if (j > 1) {
                        if ((B = o(e, R)) < 0) {
                            v = 1, M(e, b, 2 * a), R += 2 * B - 2;
                            break
                        }
                        R += 2 * B - 2
                    } else j > -1 && (m[S] = !m[S]);
                else if (j < 3)
                    if (j = 3 & z, z >>= 2, j < 1) (j = z) > 13 ? (m[++S] = o(e, R), R += 4) : j > 11 ? (w = m[S--], m[S] = m[S] >> w) : j > 9 ? (B = _(e, R), R += 2, w = m[S--], h[B] = w) : j > 7 ? (B = x(e, R), R += 4, A = S + 1, m[S -= B - 1] = B ? m.slice(S, A) : []) : j > 0 && (w = m[S--], m[S] = m[S] > w);
                    else if (j < 2) (j = z) > 12 ? (w = m[S - 1], A = m[S], m[++S] = w, m[++S] = A) : j > 3 ? (w = m[S--], m[S] = m[S] == w) : j > 1 ? (w = m[S--], m[S] = m[S] + w) : j > -1 && (m[++S] = u);
                    else if (j < 3) {
                        if ((j = z) > 13) m[++S] = !1;
                        else if (j > 6) w = m[S--], m[S] = m[S] instanceof w;
                        else if (j > 4) w = m[S--], m[S] = m[S] % w;
                        else if (j > 2)
                            if (m[S--]) R += 4;
                            else {
                                if ((B = o(e, R)) < 0) {
                                    v = 1, M(e, b, 2 * a), R += 2 * B - 2;
                                    break
                                }
                                R += 2 * B - 2
                            }
                        else if (j > 0) {
                            for (B = x(e, R), w = "", k = r.q[B][0]; k < r.q[B][1]; k++) w += String.fromCharCode(t ^ r.p[k]);
                            m[++S] = w, R += 4
                        }
                    } else (j = z) > 7 ? (w = m[S--], m[S] = m[S] | w) : j > 5 ? (B = _(e, R), R += 2, m[++S] = h["$" + B]) : j > 3 && (B = o(e, R), d[i][0] && !d[i][2] ? d[i][1] = [R + 4, B - 3] : d[i++] = [0, [R + 4, B - 3], 0], R += 2 * B - 2);
                else if (j = 3 & z, z >>= 2, j > 2) (j = z) > 13 ? (m[++S] = l(e, R), R += 8) : j > 11 ? (w = m[S--], m[S] = m[S] >>> w) : j > 9 ? m[++S] = !0 : j > 7 ? (B = _(e, R), R += 2, m[S] = m[S][B]) : j > 0 && (w = m[S--], m[S] = m[S] < w);
                else if (j > 1) (j = z) > 10 ? (B = o(e, R), d[++i] = [
                    [R + 4, B - 3], 0, 0
                ], R += 2 * B - 2) : j > 8 ? (w = m[S--], m[S] = m[S] ^ w) : j > 6 && (w = m[S--]);
                else if (j > 0) {
                    if ((j = z) > 7) w = m[S--], m[S] = m[S] in w;
                    else if (j > 5) m[S] = ++m[S];
                    else if (j > 3) B = _(e, R), R += 2, w = h[B], m[++S] = w;
                    else if (j > 1) {
                        var O = 0,
                            U = m[S].length,
                            D = m[S];
                        m[++S] = function () {
                            var e = O < U;
                            if (e) {
                                var b = D[O++];
                                m[++S] = b
                            }
                            m[++S] = e
                        }
                    }
                } else if ((j = z) > 13) w = m[S], m[S] = m[S - 1], m[S - 1] = w;
                else if (j > 4) w = m[S--], m[S] = m[S] === w;
                else if (j > 2) w = m[S--], m[S] = m[S] - w;
                else if (j > 0) {
                    for (B = x(e, R), j = "", k = r.q[B][0]; k < r.q[B][1]; k++) j += String.fromCharCode(t ^ r.p[k]);
                    j = +j, R += 4, m[++S] = j
                }
            }
        if (v)
            for (; R < q;)
                if (I = T[R], R += 2, j = 3 & (z = 13 * I % 241), z >>= 2, j > 2)
                    if (j = 3 & z, z >>= 2, j > 2) (j = z) < 2 ? (w = m[S--], m[S] = m[S] < w) : j < 9 ? (B = E[R], R += 2, m[S] = m[S][B]) : j < 11 ? m[++S] = !0 : j < 13 ? (w = m[S--], m[S] = m[S] >>> w) : j < 15 && (m[++S] = E[R], R += 8);
                    else if (j > 1) (j = z) < 6 || (j < 8 ? w = m[S--] : j < 10 ? (w = m[S--], m[S] = m[S] ^ w) : j < 12 && (B = E[R], d[++i] = [
                        [R + 4, B - 3], 0, 0
                    ], R += 2 * B - 2));
                    else if (j > 0) (j = z) > 7 ? (w = m[S--], m[S] = m[S] in w) : j > 5 ? m[S] = ++m[S] : j > 3 ? (B = E[R], R += 2, w = h[B], m[++S] = w) : j > 1 && (O = 0, U = m[S].length, D = m[S], m[++S] = function () {
                        var e = O < U;
                        if (e) {
                            var b = D[O++];
                            m[++S] = b
                        }
                        m[++S] = e
                    });
                    else if ((j = z) < 2) {
                        for (B = E[R], j = "", k = r.q[B][0]; k < r.q[B][1]; k++) j += String.fromCharCode(t ^ r.p[k]);
                        j = +j, R += 4, m[++S] = j
                    } else j < 4 ? (w = m[S--], m[S] = m[S] - w) : j < 6 ? (w = m[S--], m[S] = m[S] === w) : j < 15 && (w = m[S], m[S] = m[S - 1], m[S - 1] = w);
                else if (j > 1)
                    if (j = 3 & z, z >>= 2, j < 1) (j = z) > 13 ? (m[++S] = E[R], R += 4) : j > 11 ? (w = m[S--], m[S] = m[S] >> w) : j > 9 ? (B = E[R], R += 2, w = m[S--], h[B] = w) : j > 7 ? (B = E[R], R += 4, A = S + 1, m[S -= B - 1] = B ? m.slice(S, A) : []) : j > 0 && (w = m[S--], m[S] = m[S] > w);
                    else if (j < 2) (j = z) < 1 ? m[++S] = u : j < 3 ? (w = m[S--], m[S] = m[S] + w) : j < 5 ? (w = m[S--], m[S] = m[S] == w) : j < 14 && (w = m[S - 1], A = m[S], m[++S] = w, m[++S] = A);
                    else if (j < 3) {
                        if ((j = z) > 13) m[++S] = !1;
                        else if (j > 6) w = m[S--], m[S] = m[S] instanceof w;
                        else if (j > 4) w = m[S--], m[S] = m[S] % w;
                        else if (j > 2) m[S--] ? R += 4 : R += 2 * (B = E[R]) - 2;
                        else if (j > 0) {
                            for (B = E[R], w = "", k = r.q[B][0]; k < r.q[B][1]; k++) w += String.fromCharCode(t ^ r.p[k]);
                            m[++S] = w, R += 4
                        }
                    } else (j = z) > 7 ? (w = m[S--], m[S] = m[S] | w) : j > 5 ? (B = E[R], R += 2, m[++S] = h["$" + B]) : j > 3 && (B = E[R], d[i][0] && !d[i][2] ? d[i][1] = [R + 4, B - 3] : d[i++] = [0, [R + 4, B - 3], 0], R += 2 * B - 2);
                else if (j > 0)
                    if (j = 3 & z, z >>= 2, j < 1) {
                        if ((j = z) > 9) ;
                        else if (j > 7) w = m[S--], m[S] = m[S] & w;
                        else if (j > 5) B = E[R], R += 2, m[S -= B] = 0 === B ? new m[S] : f(m[S], c(m.slice(S + 1, S + B + 1)));
                        else if (j > 3) {
                            B = E[R];
                            try {
                                if (d[i][2] = 1, 1 == (w = P(e, R + 4, B - 3, [], h, p, null, 0))[0]) return w
                            } catch (b) {
                                if (d[i] && d[i][1] && 1 == (w = P(e, d[i][1][0], d[i][1][1], [], h, p, b, 0))[0]) return w
                            } finally {
                                if (d[i] && d[i][0] && 1 == (w = P(e, d[i][0][0], d[i][0][1], [], h, p, null, 0))[0]) return w;
                                d[i] = 0, i--
                            }
                            R += 2 * B - 2
                        }
                    } else if (j < 2)
                        if ((j = z) < 8) A = m[S--], w = delete m[S--][A];
                        else if (j < 10) {
                            for (B = E[R], j = "", k = r.q[B][0]; k < r.q[B][1]; k++) j += String.fromCharCode(t ^ r.p[k]);
                            R += 4, m[S] = m[S][j]
                        } else j < 12 ? (w = m[S--], m[S] = m[S] << w) : j < 14 && (m[++S] = E[R], R += 2);
                    else j < 3 ? (j = z) < 2 ? m[++S] = w : j < 11 ? (w = m[S -= 2][m[S + 1]] = m[S + 2], S--) : j < 13 && (w = m[S], m[++S] = w) : (j = z) > 12 ? m[++S] = p : j > 5 ? (w = m[S--], m[S] = m[S] !== w) : j > 3 ? (w = m[S--], m[S] = m[S] / w) : j > 1 ? R += 2 * (B = E[R]) - 2 : j > -1 && (m[S] = !m[S]);
                else if (j = 3 & z, z >>= 2, j < 1) {
                    if ((j = z) < 1) return [1, m[S--]];
                    j < 5 ? (w = m[S--], m[S] = m[S] * w) : j < 7 ? (w = m[S--], m[S] = m[S] != w) : j < 14 ? (A = m[S--], C = m[S--], (j = m[S--]).x === P ? j.y >= 1 ? m[++S] = F(e, j.c, j.l, A, j.z, C, null, 1) : (m[++S] = F(e, j.c, j.l, A, j.z, C, null, 0), j.y++) : m[++S] = j.apply(C, A)) : j < 16 && (B = E[R], (g = function b() {
                        var a = arguments;
                        return b.y > 0 || b.y++, F(e, b.c, b.l, a, b.z, this, null, 0)
                    }).c = R + 4, g.l = B - 2, g.x = P, g.y = 0, g.z = h, m[S] = g, R += 2 * B - 2)
                } else if (j < 2) (j = z) > 8 ? (w = m[S--], m[S] = typeof w) : j > 4 ? m[S -= 1] = m[S][m[S + 1]] : j > 2 && (A = m[S--], (j = m[S]).x === P ? j.y >= 1 ? m[S] = F(e, j.c, j.l, [A], j.z, C, null, 1) : (m[S] = F(e, j.c, j.l, [A], j.z, C, null, 0), j.y++) : m[S] = j(A));
                else if (j < 3) {
                    if ((j = z) < 9) {
                        for (w = m[S--], B = E[R], j = "", k = r.q[B][0]; k < r.q[B][1]; k++) j += String.fromCharCode(t ^ r.p[k]);
                        R += 4, m[S--][j] = w
                    } else if (j < 13) throw m[S--]
                } else (j = z) < 1 ? m[++S] = null : j < 3 ? (w = m[S--], m[S] = m[S] >= w) : j < 12 && (m[++S] = void 0);
        return [0, null]
    }

    function F(e, b, a, f, c, r, t, d) {
        null == r && (r = this), c && !c.d && (c.d = 0, c.$0 = c, c[1] = {});
        var i, n, s = {},
            o = s.d = c ? c.d + 1 : 0;
        for (s["$" + o] = s, n = 0; n < o; n++) s[i = "$" + n] = c[i];
        for (n = 0, o = s.length = f.length; n < o; n++) s[n] = f[n];
        return d && !T[b] && M(e, b, 2 * a), T[b] ? P(e, b, a, 0, s, r, null, 1)[1] : P(e, b, a, 0, s, r, null, 0)[1]
    }
};
var _0x397dc7 = "undefined" != typeof globalThis ? globalThis : void 0 !== window ? window : "undefined" != typeof global ? global : "undefined" != typeof self ? self : {},
    _0x124d1a = _0x5cd844(function (_0x770f81) {
        !function () {
            var _0x250d36 = "input is invalid type",
                _0x4cfaee = !1,
                _0x1702f9 = {},
                _0x5ccbb3 = !_0x4cfaee && "object" == typeof self,
                _0x54d876 = !_0x1702f9.JS_MD5_NO_NODE_JS && "object" == typeof process && process.versions && process.versions.node,
                _0x185caf;
            _0x54d876 ? _0x1702f9 = _0x397dc7 : _0x5ccbb3 && (_0x1702f9 = self);
            var _0x17dcbf = !_0x1702f9.JS_MD5_NO_COMMON_JS && _0x770f81.exports,
                _0x554fed = !1,
                _0x2de28f = !_0x1702f9.JS_MD5_NO_ARRAY_BUFFER && "undefined" != typeof ArrayBuffer,
                _0x3a9a1b = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"],
                _0x465562 = [128, 32768, 8388608, -2147483648],
                _0x20b37e = [0, 8, 16, 24],
                _0x323604 = ["hex", "array", "digest", "buffer", "arrayBuffer", "base64"],
                _0x2c185e = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"],
                _0x4b59e0 = [];
            if (_0x2de28f) {
                var _0x395837 = new ArrayBuffer(68);
                _0x185caf = new Uint8Array(_0x395837), _0x4b59e0 = new Uint32Array(_0x395837)
            }
            !_0x1702f9.JS_MD5_NO_NODE_JS && Array.isArray || (Array.isArray = function (e) {
                return "[object Array]" === Object.prototype.toString.call(e)
            }), _0x2de28f && (_0x1702f9.JS_MD5_NO_ARRAY_BUFFER_IS_VIEW || !ArrayBuffer.isView) && (ArrayBuffer.isView = function (e) {
                return "object" == typeof e && e.buffer && e.buffer.constructor === ArrayBuffer
            });
            var _0x4e9930 = function (e) {
                    return function (b) {
                        return new _0x5887c8(!0).update(b)[e]()
                    }
                },
                _0x38ba77 = function () {
                    var e = _0x4e9930("hex");
                    _0x54d876 && (e = _0x474989(e)), e.create = function () {
                        return new _0x5887c8
                    }, e.update = function (b) {
                        return e.create().update(b)
                    };
                    for (var b = 0; b < _0x323604.length; ++b) {
                        var a = _0x323604[b];
                        e[a] = _0x4e9930(a)
                    }
                    return e
                },
                _0x474989 = function (_0x57eeaa) {
                    var _0x114910, _0x226465 = eval("require('crypto');"),
                        _0x1f6ae0 = eval("require('buffer')['Buffer'];");
                    return function (e) {
                        if ("string" == typeof e) return _0x226465.createHash("md5").update(e, "utf8").digest("hex");
                        if (null == e) throw _0x250d36;
                        return e.constructor === ArrayBuffer && (e = new Uint8Array(e)), Array.isArray(e) || ArrayBuffer.isView(e) || e.constructor === _0x1f6ae0 ? _0x226465.createHash("md5").update(new _0x1f6ae0.from(e)).digest("hex") : _0x57eeaa(e)
                    }
                };

            function _0x5887c8(e) {
                if (e) _0x4b59e0[0] = _0x4b59e0[16] = _0x4b59e0[1] = _0x4b59e0[2] = _0x4b59e0[3] = _0x4b59e0[4] = _0x4b59e0[5] = _0x4b59e0[6] = _0x4b59e0[7] = _0x4b59e0[8] = _0x4b59e0[9] = _0x4b59e0[10] = _0x4b59e0[11] = _0x4b59e0[12] = _0x4b59e0[13] = _0x4b59e0[14] = _0x4b59e0[15] = 0, this.blocks = _0x4b59e0, this.buffer8 = _0x185caf;
                else if (_0x2de28f) {
                    var b = new ArrayBuffer(68);
                    this.buffer8 = new Uint8Array(b), this.blocks = new Uint32Array(b)
                } else this.blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
                this.h0 = this.h1 = this.h2 = this.h3 = this.start = this.bytes = this.hBytes = 0, this.finalized = this.hashed = !1, this.first = !0
            }

            _0x5887c8.prototype.update = function (e) {
                if (!this.finalized) {
                    var b, a = typeof e;
                    if ("string" !== a) {
                        if ("object" !== a || null === e) throw _0x250d36;
                        if (_0x2de28f && e.constructor === ArrayBuffer) e = new Uint8Array(e);
                        else if (!(Array.isArray(e) || _0x2de28f && ArrayBuffer.isView(e))) throw _0x250d36;
                        b = !0
                    }
                    for (var f, c, r = 0, t = e.length, d = this.blocks, i = this.buffer8; r < t;) {
                        if (this.hashed && (this.hashed = !1, d[0] = d[16], d[16] = d[1] = d[2] = d[3] = d[4] = d[5] = d[6] = d[7] = d[8] = d[9] = d[10] = d[11] = d[12] = d[13] = d[14] = d[15] = 0), b)
                            if (_0x2de28f)
                                for (c = this.start; r < t && c < 64; ++r) i[c++] = e[r];
                            else
                                for (c = this.start; r < t && c < 64; ++r) d[c >> 2] |= e[r] << _0x20b37e[3 & c++];
                        else if (_0x2de28f)
                            for (c = this.start; r < t && c < 64; ++r) (f = e.charCodeAt(r)) < 128 ? i[c++] = f : f < 2048 ? (i[c++] = 192 | f >> 6, i[c++] = 128 | 63 & f) : f < 55296 || f >= 57344 ? (i[c++] = 224 | f >> 12, i[c++] = 128 | f >> 6 & 63, i[c++] = 128 | 63 & f) : (f = 65536 + ((1023 & f) << 10 | 1023 & e.charCodeAt(++r)), i[c++] = 240 | f >> 18, i[c++] = 128 | f >> 12 & 63, i[c++] = 128 | f >> 6 & 63, i[c++] = 128 | 63 & f);
                        else
                            for (c = this.start; r < t && c < 64; ++r) (f = e.charCodeAt(r)) < 128 ? d[c >> 2] |= f << _0x20b37e[3 & c++] : f < 2048 ? (d[c >> 2] |= (192 | f >> 6) << _0x20b37e[3 & c++], d[c >> 2] |= (128 | 63 & f) << _0x20b37e[3 & c++]) : f < 55296 || f >= 57344 ? (d[c >> 2] |= (224 | f >> 12) << _0x20b37e[3 & c++], d[c >> 2] |= (128 | f >> 6 & 63) << _0x20b37e[3 & c++], d[c >> 2] |= (128 | 63 & f) << _0x20b37e[3 & c++]) : (f = 65536 + ((1023 & f) << 10 | 1023 & e.charCodeAt(++r)), d[c >> 2] |= (240 | f >> 18) << _0x20b37e[3 & c++], d[c >> 2] |= (128 | f >> 12 & 63) << _0x20b37e[3 & c++], d[c >> 2] |= (128 | f >> 6 & 63) << _0x20b37e[3 & c++], d[c >> 2] |= (128 | 63 & f) << _0x20b37e[3 & c++]);
                        this.lastByteIndex = c, this.bytes += c - this.start, c >= 64 ? (this.start = c - 64, this.hash(), this.hashed = !0) : this.start = c
                    }
                    return this.bytes > 4294967295 && (this.hBytes += this.bytes / 4294967296 << 0, this.bytes = this.bytes % 4294967296), this
                }
            }, _0x5887c8.prototype.finalize = function () {
                if (!this.finalized) {
                    this.finalized = !0;
                    var e = this.blocks,
                        b = this.lastByteIndex;
                    e[b >> 2] |= _0x465562[3 & b], b >= 56 && (this.hashed || this.hash(), e[0] = e[16], e[16] = e[1] = e[2] = e[3] = e[4] = e[5] = e[6] = e[7] = e[8] = e[9] = e[10] = e[11] = e[12] = e[13] = e[14] = e[15] = 0), e[14] = this.bytes << 3, e[15] = this.hBytes << 3 | this.bytes >>> 29, this.hash()
                }
            }, _0x5887c8.prototype.hash = function () {
                var e, b, a, f, c, r, t = this.blocks;
                this.first ? b = ((b = ((e = ((e = t[0] - 680876937) << 7 | e >>> 25) - 271733879 << 0) ^ (a = ((a = (-271733879 ^ (f = ((f = (-1732584194 ^ 2004318071 & e) + t[1] - 117830708) << 12 | f >>> 20) + e << 0) & (-271733879 ^ e)) + t[2] - 1126478375) << 17 | a >>> 15) + f << 0) & (f ^ e)) + t[3] - 1316259209) << 22 | b >>> 10) + a << 0 : (e = this.h0, b = this.h1, a = this.h2, b = ((b += ((e = ((e += ((f = this.h3) ^ b & (a ^ f)) + t[0] - 680876936) << 7 | e >>> 25) + b << 0) ^ (a = ((a += (b ^ (f = ((f += (a ^ e & (b ^ a)) + t[1] - 389564586) << 12 | f >>> 20) + e << 0) & (e ^ b)) + t[2] + 606105819) << 17 | a >>> 15) + f << 0) & (f ^ e)) + t[3] - 1044525330) << 22 | b >>> 10) + a << 0), b = ((b += ((e = ((e += (f ^ b & (a ^ f)) + t[4] - 176418897) << 7 | e >>> 25) + b << 0) ^ (a = ((a += (b ^ (f = ((f += (a ^ e & (b ^ a)) + t[5] + 1200080426) << 12 | f >>> 20) + e << 0) & (e ^ b)) + t[6] - 1473231341) << 17 | a >>> 15) + f << 0) & (f ^ e)) + t[7] - 45705983) << 22 | b >>> 10) + a << 0, b = ((b += ((e = ((e += (f ^ b & (a ^ f)) + t[8] + 1770035416) << 7 | e >>> 25) + b << 0) ^ (a = ((a += (b ^ (f = ((f += (a ^ e & (b ^ a)) + t[9] - 1958414417) << 12 | f >>> 20) + e << 0) & (e ^ b)) + t[10] - 42063) << 17 | a >>> 15) + f << 0) & (f ^ e)) + t[11] - 1990404162) << 22 | b >>> 10) + a << 0, b = ((b += ((e = ((e += (f ^ b & (a ^ f)) + t[12] + 1804603682) << 7 | e >>> 25) + b << 0) ^ (a = ((a += (b ^ (f = ((f += (a ^ e & (b ^ a)) + t[13] - 40341101) << 12 | f >>> 20) + e << 0) & (e ^ b)) + t[14] - 1502002290) << 17 | a >>> 15) + f << 0) & (f ^ e)) + t[15] + 1236535329) << 22 | b >>> 10) + a << 0, b = ((b += ((f = ((f += (b ^ a & ((e = ((e += (a ^ f & (b ^ a)) + t[1] - 165796510) << 5 | e >>> 27) + b << 0) ^ b)) + t[6] - 1069501632) << 9 | f >>> 23) + e << 0) ^ e & ((a = ((a += (e ^ b & (f ^ e)) + t[11] + 643717713) << 14 | a >>> 18) + f << 0) ^ f)) + t[0] - 373897302) << 20 | b >>> 12) + a << 0, b = ((b += ((f = ((f += (b ^ a & ((e = ((e += (a ^ f & (b ^ a)) + t[5] - 701558691) << 5 | e >>> 27) + b << 0) ^ b)) + t[10] + 38016083) << 9 | f >>> 23) + e << 0) ^ e & ((a = ((a += (e ^ b & (f ^ e)) + t[15] - 660478335) << 14 | a >>> 18) + f << 0) ^ f)) + t[4] - 405537848) << 20 | b >>> 12) + a << 0, b = ((b += ((f = ((f += (b ^ a & ((e = ((e += (a ^ f & (b ^ a)) + t[9] + 568446438) << 5 | e >>> 27) + b << 0) ^ b)) + t[14] - 1019803690) << 9 | f >>> 23) + e << 0) ^ e & ((a = ((a += (e ^ b & (f ^ e)) + t[3] - 187363961) << 14 | a >>> 18) + f << 0) ^ f)) + t[8] + 1163531501) << 20 | b >>> 12) + a << 0, b = ((b += ((f = ((f += (b ^ a & ((e = ((e += (a ^ f & (b ^ a)) + t[13] - 1444681467) << 5 | e >>> 27) + b << 0) ^ b)) + t[2] - 51403784) << 9 | f >>> 23) + e << 0) ^ e & ((a = ((a += (e ^ b & (f ^ e)) + t[7] + 1735328473) << 14 | a >>> 18) + f << 0) ^ f)) + t[12] - 1926607734) << 20 | b >>> 12) + a << 0, b = ((b += ((r = (f = ((f += ((c = b ^ a) ^ (e = ((e += (c ^ f) + t[5] - 378558) << 4 | e >>> 28) + b << 0)) + t[8] - 2022574463) << 11 | f >>> 21) + e << 0) ^ e) ^ (a = ((a += (r ^ b) + t[11] + 1839030562) << 16 | a >>> 16) + f << 0)) + t[14] - 35309556) << 23 | b >>> 9) + a << 0, b = ((b += ((r = (f = ((f += ((c = b ^ a) ^ (e = ((e += (c ^ f) + t[1] - 1530992060) << 4 | e >>> 28) + b << 0)) + t[4] + 1272893353) << 11 | f >>> 21) + e << 0) ^ e) ^ (a = ((a += (r ^ b) + t[7] - 155497632) << 16 | a >>> 16) + f << 0)) + t[10] - 1094730640) << 23 | b >>> 9) + a << 0, b = ((b += ((r = (f = ((f += ((c = b ^ a) ^ (e = ((e += (c ^ f) + t[13] + 681279174) << 4 | e >>> 28) + b << 0)) + t[0] - 358537222) << 11 | f >>> 21) + e << 0) ^ e) ^ (a = ((a += (r ^ b) + t[3] - 722521979) << 16 | a >>> 16) + f << 0)) + t[6] + 76029189) << 23 | b >>> 9) + a << 0, b = ((b += ((r = (f = ((f += ((c = b ^ a) ^ (e = ((e += (c ^ f) + t[9] - 640364487) << 4 | e >>> 28) + b << 0)) + t[12] - 421815835) << 11 | f >>> 21) + e << 0) ^ e) ^ (a = ((a += (r ^ b) + t[15] + 530742520) << 16 | a >>> 16) + f << 0)) + t[2] - 995338651) << 23 | b >>> 9) + a << 0, b = ((b += ((f = ((f += (b ^ ((e = ((e += (a ^ (b | ~f)) + t[0] - 198630844) << 6 | e >>> 26) + b << 0) | ~a)) + t[7] + 1126891415) << 10 | f >>> 22) + e << 0) ^ ((a = ((a += (e ^ (f | ~b)) + t[14] - 1416354905) << 15 | a >>> 17) + f << 0) | ~e)) + t[5] - 57434055) << 21 | b >>> 11) + a << 0, b = ((b += ((f = ((f += (b ^ ((e = ((e += (a ^ (b | ~f)) + t[12] + 1700485571) << 6 | e >>> 26) + b << 0) | ~a)) + t[3] - 1894986606) << 10 | f >>> 22) + e << 0) ^ ((a = ((a += (e ^ (f | ~b)) + t[10] - 1051523) << 15 | a >>> 17) + f << 0) | ~e)) + t[1] - 2054922799) << 21 | b >>> 11) + a << 0, b = ((b += ((f = ((f += (b ^ ((e = ((e += (a ^ (b | ~f)) + t[8] + 1873313359) << 6 | e >>> 26) + b << 0) | ~a)) + t[15] - 30611744) << 10 | f >>> 22) + e << 0) ^ ((a = ((a += (e ^ (f | ~b)) + t[6] - 1560198380) << 15 | a >>> 17) + f << 0) | ~e)) + t[13] + 1309151649) << 21 | b >>> 11) + a << 0, b = ((b += ((f = ((f += (b ^ ((e = ((e += (a ^ (b | ~f)) + t[4] - 145523070) << 6 | e >>> 26) + b << 0) | ~a)) + t[11] - 1120210379) << 10 | f >>> 22) + e << 0) ^ ((a = ((a += (e ^ (f | ~b)) + t[2] + 718787259) << 15 | a >>> 17) + f << 0) | ~e)) + t[9] - 343485551) << 21 | b >>> 11) + a << 0, this.first ? (this.h0 = e + 1732584193 << 0, this.h1 = b - 271733879 << 0, this.h2 = a - 1732584194 << 0, this.h3 = f + 271733878 << 0, this.first = !1) : (this.h0 = this.h0 + e << 0, this.h1 = this.h1 + b << 0, this.h2 = this.h2 + a << 0, this.h3 = this.h3 + f << 0)
            }, _0x5887c8.prototype.hex = function () {
                this.finalize();
                var e = this.h0,
                    b = this.h1,
                    a = this.h2,
                    f = this.h3;
                return _0x3a9a1b[e >> 4 & 15] + _0x3a9a1b[15 & e] + _0x3a9a1b[e >> 12 & 15] + _0x3a9a1b[e >> 8 & 15] + _0x3a9a1b[e >> 20 & 15] + _0x3a9a1b[e >> 16 & 15] + _0x3a9a1b[e >> 28 & 15] + _0x3a9a1b[e >> 24 & 15] + _0x3a9a1b[b >> 4 & 15] + _0x3a9a1b[15 & b] + _0x3a9a1b[b >> 12 & 15] + _0x3a9a1b[b >> 8 & 15] + _0x3a9a1b[b >> 20 & 15] + _0x3a9a1b[b >> 16 & 15] + _0x3a9a1b[b >> 28 & 15] + _0x3a9a1b[b >> 24 & 15] + _0x3a9a1b[a >> 4 & 15] + _0x3a9a1b[15 & a] + _0x3a9a1b[a >> 12 & 15] + _0x3a9a1b[a >> 8 & 15] + _0x3a9a1b[a >> 20 & 15] + _0x3a9a1b[a >> 16 & 15] + _0x3a9a1b[a >> 28 & 15] + _0x3a9a1b[a >> 24 & 15] + _0x3a9a1b[f >> 4 & 15] + _0x3a9a1b[15 & f] + _0x3a9a1b[f >> 12 & 15] + _0x3a9a1b[f >> 8 & 15] + _0x3a9a1b[f >> 20 & 15] + _0x3a9a1b[f >> 16 & 15] + _0x3a9a1b[f >> 28 & 15] + _0x3a9a1b[f >> 24 & 15]
            }, _0x5887c8.prototype.toString = _0x5887c8.prototype.hex, _0x5887c8.prototype.digest = function () {
                this.finalize();
                var e = this.h0,
                    b = this.h1,
                    a = this.h2,
                    f = this.h3;
                return [255 & e, e >> 8 & 255, e >> 16 & 255, e >> 24 & 255, 255 & b, b >> 8 & 255, b >> 16 & 255, b >> 24 & 255, 255 & a, a >> 8 & 255, a >> 16 & 255, a >> 24 & 255, 255 & f, f >> 8 & 255, f >> 16 & 255, f >> 24 & 255]
            }, _0x5887c8.prototype.array = _0x5887c8.prototype.digest, _0x5887c8.prototype.arrayBuffer = function () {
                this.finalize();
                var e = new ArrayBuffer(16),
                    b = new Uint32Array(e);
                return b[0] = this.h0, b[1] = this.h1, b[2] = this.h2, b[3] = this.h3, e
            }, _0x5887c8.prototype.buffer = _0x5887c8.prototype.arrayBuffer, _0x5887c8.prototype.base64 = function () {
                for (var e, b, a, f = "", c = this.array(), r = 0; r < 15;) e = c[r++], b = c[r++], a = c[r++], f += _0x2c185e[e >>> 2] + _0x2c185e[63 & (e << 4 | b >>> 4)] + _0x2c185e[63 & (b << 2 | a >>> 6)] + _0x2c185e[63 & a];
                return f + (_0x2c185e[(e = c[r]) >>> 2] + _0x2c185e[e << 4 & 63] + "==")
            };
            var _0x4dd781 = _0x38ba77();
            _0x17dcbf ? _0x770f81.exports = _0x4dd781 : (_0x1702f9.md5 = _0x4dd781, _0x554fed && (void 0)(function () {
                return _0x4dd781
            }))
        }()
    });

function _0x178cef(e) {
    return jsvmp("484e4f4a403f52430038001eab0015840e8ee21a00000000000000621b000200001d000146000306000e271f001b000200021d00010500121b001b000b021b000b04041d0001071b000b0500000003000126207575757575757575757575757575757575757575757575757575757575757575", [, , void 0 !== _0x124d1a ? _0x124d1a : void 0, _0x178cef, e])
}

for (var _0xb55f3e = {
    boe: !1,
    aid: 0,
    dfp: !1,
    sdi: !1,
    enablePathList: [],
    _enablePathListRegex: [],
    urlRewriteRules: [],
    _urlRewriteRules: [],
    initialized: !1,
    enableTrack: !1,
    track: {
        unitTime: 0,
        unitAmount: 0,
        fre: 0
    },
    triggerUnload: !1,
    region: "",
    regionConf: {},
    umode: 0,
    v: !1,
    perf: !1,
    xxbg: !0
}, _0x3eaf64 = {
    debug: function (e, b) {
        let a = !1;
        a = !1
    }
}, _0x233455 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"], _0x2e9f6d = [], _0x511f86 = [], _0x3d35de = 0; _0x3d35de < 256; _0x3d35de++) _0x2e9f6d[_0x3d35de] = _0x233455[_0x3d35de >> 4 & 15] + _0x233455[15 & _0x3d35de], _0x3d35de < 16 && (_0x3d35de < 10 ? _0x511f86[48 + _0x3d35de] = _0x3d35de : _0x511f86[87 + _0x3d35de] = _0x3d35de);
var _0x2ce54d = function (e) {
        for (var b = e.length, a = "", f = 0; f < b;) a += _0x2e9f6d[e[f++]];
        return a
    },
    _0x5960a2 = function (e) {
        for (var b = e.length >> 1, a = b << 1, f = new Uint8Array(b), c = 0, r = 0; r < a;) f[c++] = _0x511f86[e.charCodeAt(r++)] << 4 | _0x511f86[e.charCodeAt(r++)];
        return f
    },
    _0x4e46b6 = {
        encode: _0x2ce54d,
        decode: _0x5960a2
    };

function sign(e, b) {
    return jsvmp("484e4f4a403f5243001f240fbf2031ccf317480300000000000007181b0002012e1d00921b000b171b000b02402217000a1c1b000b1726402217000c1c1b000b170200004017002646000306000e271f001b000200021d00920500121b001b000b031b000b17041d0092071b000b041e012f17000d1b000b05260a0000101c1b000b06260a0000101c1b001b000b071e01301d00931b001b000b081e00081d00941b0048021d00951b001b000b1b1d00961b0048401d009e1b001b000b031b000b16041d009f1b001b000b09221e0131241b000b031b000b09221e0131241b000b1e0a000110040a0001101d00d51b001b000b09221e0131241b000b031b000b09221e0131241b000b180a000110040a0001101d00d71b001b000b0a1e00101d00d91b001b000b0b261b000b1a1b000b190a0002101d00db1b001b000b0c261b000b221b000b210a0002101d00dc1b001b000b0d261b000b230200200a0002101d00dd1b001b000b09221e0131241b000b031b000b24040a0001101d00df1b001b000b0e1a00221e00de240a0000104903e82b1d00e31b001b000b0f260a0000101d00e41b001b000b1d1d00e71b001b000b1a4901002b1d00e81b001b000b1a4901002c1d00ea1b001b000b191d00f21b001b000b1f480e191d00f81b001b000b1f480f191d00f91b001b000b20480e191d00fb1b001b000b20480f191d00fe1b001b000b25480e191d01001b001b000b25480f191d01011b001b000b264818344900ff2f1d01031b001b000b264810344900ff2f1d01321b001b000b264808344900ff2f1d01331b001b000b264800344900ff2f1d01341b001b000b274818344900ff2f1d01351b001b000b274810344900ff2f1d01361b001b000b274808344900ff2f1d01371b001b000b274800344900ff2f1d01381b001b000b281b000b29311b000b2a311b000b2b311b000b2c311b000b2d311b000b2e311b000b2f311b000b30311b000b31311b000b32311b000b33311b000b34311b000b35311b000b36311b000b37311b000b38311b000b39311d01391b004900ff1d013a1b001b000b10261b000b281b000b2a1b000b2c1b000b2e1b000b301b000b321b000b341b000b361b000b381b000b3a1b000b291b000b2b1b000b2d1b000b2f1b000b311b000b331b000b351b000b371b000b390a0013101d013b1b001b000b0c261b000b111b000b3b041b000b3c0a0002101d013c1b001b000b12261b000b1c1b000b3b1b000b3d0a0003101d013d1b001b000b13261b000b3e0200240a0002101d013e1b000b3f0000013f000126207575757575757575757575757575757575757575757575757575757575757575012b0e7776757a7d7643617c637661676a027a77065c717976706708777671667474766107767d65707c77760374766707707c7d607c7f7607757a61767166740a7c66677661447a77677b0a7a7d7d7661447a77677b0b7c666776615b767a747b670b7a7d7d76615b767a747b6709666076615274767d670b677c5f7c64766150726076077a7d77766b5c7508767f767067617c7d09667d7776757a7d76770963617c677c676a637608677c4067617a7d740470727f7f0763617c7076606010487c71797670673363617c707660604e067c717976706705677a677f76047d7c7776012e0125012402602341525150575655545b5a59585f5e5d5c43424140474645444b4a49727170777675747b7a79787f7e7d7c63626160676665646b6a6923222120272625242b2a383c2e0260224157787763747b2749586042512b233c5e75656420254b5a22412126384446527f567a245d5f717c624a475c4366697e5579597d616a6b2a5b45547072406750762e0260214157787763747b2749586042512b233c5e75656420254b5a224121263e4446527f567a245d5f717c624a475c4366697e5579597d616a6b2a5b45547072406750762e02602041525150575655545b5a59585f5e5d5c43424140474645444b4a49727170777675747b7a79787f7e7d7c63626160676665646b6a6923222120272625242b2a3e4c2e012a022222067f767d74677b0a707b7261507c7776526702222306707b726152670f487c717976706733447a7d777c644e08577c70667e767d6712487c7179767067335d72657a7472677c614e057960777c7e10487c7179767067335b7a60677c616a4e07637f66747a7d60084c637b727d677c7e0b70727f7f437b727d677c7e0b4c4c7d7a747b677e726176055266777a7c1850727d65726041767d7776617a7d74507c7d67766b6721570964767177617a657661137476675c647d43617c637661676a5d727e7660097f727d74667274766006707b617c7e760761667d677a7e7607707c7d7d767067144c4c64767177617a6576614c7665727f66726776134c4c60767f767d7a667e4c7665727f667267761b4c4c64767177617a6576614c6070617a63674c75667d70677a7c7d174c4c64767177617a6576614c6070617a63674c75667d70154c4c64767177617a6576614c6070617a63674c757d134c4c756b77617a6576614c7665727f66726776124c4c77617a6576614c667d64617263637677154c4c64767177617a6576614c667d64617263637677114c4c77617a6576614c7665727f66726776144c4c60767f767d7a667e4c667d64617263637677144c4c756b77617a6576614c667d64617263637677094c60767f767d7a667e0c70727f7f40767f767d7a667e164c40767f767d7a667e4c5a57564c4176707c6177766108777c70667e767d670478766a60057e7267707b06417674566b630a4f3748723e694e77704c067072707b764c04607c7e7608707675407b72616308507675407b72616305767c72637a16767c44767151617c64607661577a60637267707b76610f717a7d775c717976706752606a7d700e7a60565c44767151617c646076610120047c63767d0467766067097a7d707c747d7a677c077c7d7661617c6104707c77761242465c47524c564b5056565756574c5641410e607660607a7c7d40677c61727476076076675a67767e10607c7e7658766a5b766176516a6776770a61767e7c65765a67767e097a7d77766b767757510c437c7a7d6776615665767d670e5e40437c7a7d6776615665767d670d706176726776567f767e767d670670727d65726009677c5772677246415f076176637f727076034f603901740a7d72677a6576707c777614487c717976706733437f66747a7d526161726a4e4a4d7b676763602c294f3c4f3c3b48233e2a4e68223f206e3b4f3d48233e2a4e68223f206e3a68206e6f48723e75233e2a4e68223f276e3b2948723e75233e2a4e68223f276e3a68246e3a0127087f7c7072677a7c7d047b61767504757a7f76107b676763293c3c7f7c70727f7b7c606708637f7267757c617e02222102222007647a7d777c646002222703647a7d02222607727d77617c7a77022225057f7a7d666b022224067a637b7c7d7602222b047a63727702222a047a637c77022123037e7270022122097e72707a7d677c607b0c7e72704c637c64766163703a0470617c60036b22220570617a7c6005756b7a7c6004637a787602212102212002212702212602212502212402212b08757a6176757c6b3c067c637661723c05337c63613c05337c63673c07707b617c7e763c0867617a77767d673c047e607a7602212a0220230665767d777c6106547c7c747f760e4c637261727e40647a67707b5c7d0a777a61767067407a747d0a707c7d607a6067767d670660647a67707b03777c7e07637b727d677c7e047b7c7c7840525150575655545b5a59585f5e5d5c43424140474645444b4a49727170777675747b7a79787f7e7d7c63626160676665646b6a6923222120272625242b2a3e3d03727a77017d01750161096067726167477a7e7601670972717a7f7a677a76600a677a7e766067727e6322137b72617764726176507c7d70666161767d706a0c7776657a70765e767e7c616a087f727d74667274760a6176607c7f66677a7c7d0f7265727a7f4176607c7f66677a7c7d0960706176767d477c630a60706176767d5f767567107776657a7076437a6b767f4172677a7c0a63617c77667067406671077172676776616a016309677c66707b5a7d757c08677a7e76697c7d760a677a7e766067727e6321077463665a7d757c0b7960557c7d67605f7a60670b637f66747a7d605f7a60670a677a7e766067727e63200a76657661507c7c787a760767674c60707a77017e0b606a7d67726b5661617c610c7d72677a65765f767d74677b056167705a43097563457661607a7c7d0b4c4c657661607a7c7d4c4c08707f7a767d675a770a677a7e766067727e63270b766b67767d77557a767f77046366607b03727f7f04677b767d097172607625274c707b0c75617c7e507b7261507c7776067125274c2023022022087172607625274c23022021087172607625274c22022020087172607625274c2102202702202602202507747667477a7e760220240b777c7e5d7c6745727f7a77096066716067617a7d740863617c677c707c7f02202b02202a01230e222323232323232322222323232302272302272207757c616176727f02272104717c776a096067617a7d747a756a02686e0b717c776a45727f216067610a717c776a4c7b72607b2e01350366617f02272005626676616a0a72607c7f774c607a747d096372677b7d727e762e0967674c6476717a772e063566667a772e0227270227260e4c716a6776774c6076704c777a770227250a27212a272a2524212a25097576457661607a7c7d0227240e4c232151274925647c232323232202272b02272a05607f7a7076022623074056505a5d555c037d7c6409677a7e766067727e6305757f7c7c610661727d777c7e0f7476674747447671507c7c787a7660056767647a770867674c6476717a770767674476715a770b67674c6476717a774c65210967674476717a7745210761667d7d7a7d7405757f66607b087e7c65765f7a60670660637f7a70760671765e7c657609707f7a70785f7a6067077176507f7a70780c78766a717c7261775f7a60670a717658766a717c7261770b7270677a657640677267760b647a7d777c6440677267760360477e05676172707808667d7a67477a7e76037270700a667d7a67527e7c667d670871767b72657a7c61077e6074476a637603645a5707727a775f7a60670b63617a6572706a5e7c777606706660677c7e067260607a747d0f4456514c5756455a50564c5a5d555c0479607c7d0a6176747a7c7d507c7d75096176637c616746617f04766b7a67094b3e5e403e404746510c4b3e5e403e43524a5f5c525720232323232323232323232323232323232323232323232323232323232323232320772722772b70772a2b75232371212327762a2b23232a2a2b7670752b272124760165066671707c7776067776707c777602262202262102262002262702262602262502262402262b02262a022523022522022521022520", [, , void 0, void 0 !== _0x178cef ? _0x178cef : void 0, {
        boe: !1,
        aid: 0,
        dfp: !1,
        sdi: !1,
        enablePathList: [],
        _enablePathListRegex: [/\/web\/report/],
        urlRewriteRules: [],
        _urlRewriteRules: [],
        initialized: !1,
        enableTrack: !1,
        track: {
            unitTime: 0,
            unitAmount: 0,
            fre: 0
        },
        triggerUnload: !1,
        region: "",
        regionConf: {},
        umode: 0,
        v: !1,
        perf: !1,
        xxbg: !0
    }, () => 0, () => "03v", {
        ubcode: 0
    }, {
        bogusIndex: 0,
        msNewTokenList: [],
        moveList: [],
        clickList: [],
        keyboardList: [],
        activeState: [],
        aidList: [],
        envcode: 0,
        msToken: "",
        msStatus: 0,
        __ac_testid: "",
        ttwid: "",
        tt_webid: "",
        tt_webid_v2: ""
    }, void 0 !== _0x4e46b6 ? _0x4e46b6 : void 0, {
        userAgent: b
    }, (e, b) => {
        let a = new Uint8Array(3);
        return a[0] = e / 256, a[1] = e % 256, a[2] = b % 256, String.fromCharCode.apply(null, a)
    }, (e, b) => {
        let a, f = [],
            c = 0,
            r = "";
        for (let e = 0; e < 256; e++) f[e] = e;
        for (let b = 0; b < 256; b++) c = (c + f[b] + e.charCodeAt(b % e.length)) % 256, a = f[b], f[b] = f[c], f[c] = a;
        let t = 0;
        c = 0;
        for (let e = 0; e < b.length; e++) c = (c + f[t = (t + 1) % 256]) % 256, a = f[t], f[t] = f[c], f[c] = a, r += String.fromCharCode(b.charCodeAt(e) ^ f[(f[t] + f[c]) % 256]);
        return r
    }, (e, b) => jsvmp("484e4f4a403f524300281018f7b851f02d296e5b00000000000004a21b0002001d1d001e1b00131e00061a001d001f1b000b070200200200210d1b000b070200220200230d1b000b070200240200250d1b000b070200260200270d1b001b000b071b000b05191d00031b000200001d00281b0048001d00291b000b041e002a1b000b0b4803283b1700f11b001b000b04221e002b241b001e0029222d1b00241d00290a0001104900ff2f4810331b000b04221e002b241b001e0029222d1b00241d00290a0001104900ff2f480833301b000b04221e002b241b001e0029222d1b00241d00290a0001104900ff2f301d002c1b00220b091b000b08221e002d241b000b0a4a00fc00002f4812340a000110281d00281b00220b091b000b08221e002d241b000b0a4a0003f0002f480c340a000110281d00281b00220b091b000b08221e002d241b000b0a490fc02f4806340a000110281d00281b00220b091b000b08221e002d241b000b0a483f2f0a000110281d002816ff031b000b041e002a1b000b0b294800391700e01b001b000b04221e002b241b001e0029222d1b00241d00290a0001104900ff2f4810331b000b041e002a1b000b0b3917001e1b000b04221e002b241b000b0b0a0001104900ff2f4808331600054800301d002c1b00220b091b000b08221e002d241b000b0a4a00fc00002f4812340a000110281d00281b00220b091b000b08221e002d241b000b0a4a0003f0002f480c340a000110281d00281b00220b091b000b041e002a1b000b0b3917001e1b000b08221e002d241b000b0a490fc02f4806340a0001101600071b000b06281d00281b00220b091b000b06281d00281b000b090000002e000126207575757575757575757575757575757575757575757575757575757575757575012b0e7776757a7d7643617c637661676a027a77065c717976706708777671667474766107767d65707c77760374766707707c7d607c7f7607757a61767166740a7c66677661447a77677b0a7a7d7d7661447a77677b0b7c666776615b767a747b670b7a7d7d76615b767a747b6709666076615274767d670b677c5f7c64766150726076077a7d77766b5c7508767f767067617c7d09667d7776757a7d76770963617c677c676a637608677c4067617a7d740470727f7f0763617c7076606010487c71797670673363617c707660604e067c717976706705677a677f76047d7c7776012e0125012402602341525150575655545b5a59585f5e5d5c43424140474645444b4a49727170777675747b7a79787f7e7d7c63626160676665646b6a6923222120272625242b2a383c2e0260224157787763747b2749586042512b233c5e75656420254b5a22412126384446527f567a245d5f717c624a475c4366697e5579597d616a6b2a5b45547072406750762e0260214157787763747b2749586042512b233c5e75656420254b5a224121263e4446527f567a245d5f717c624a475c4366697e5579597d616a6b2a5b45547072406750762e02602041525150575655545b5a59585f5e5d5c43424140474645444b4a49727170777675747b7a79787f7e7d7c63626160676665646b6a6923222120272625242b2a3e4c2e012a022222067f767d74677b0a707b7261507c7776526702222306707b72615267", [, , , , e, b]), "undefined" != typeof Date ? Date : void 0, () => 0, (e, b, a, f, c, r, t, d, i, n, s, o, l, _, x, u, h, p, y) => {
        let v = new Uint8Array(19);
        return v[0] = e, v[1] = s, v[2] = b, v[3] = o, v[4] = a, v[5] = l, v[6] = f, v[7] = _, v[8] = c, v[9] = x, v[10] = r, v[11] = u, v[12] = t, v[13] = h, v[14] = d, v[15] = p, v[16] = i, v[17] = y, v[18] = n, String.fromCharCode.apply(null, v)
    }, e => String.fromCharCode(e), (e, b, a) => String.fromCharCode(e) + String.fromCharCode(b) + a, (e, b) => jsvmp("484e4f4a403f524300281018f7b851f02d296e5b00000000000004a21b0002001d1d001e1b00131e00061a001d001f1b000b070200200200210d1b000b070200220200230d1b000b070200240200250d1b000b070200260200270d1b001b000b071b000b05191d00031b000200001d00281b0048001d00291b000b041e002a1b000b0b4803283b1700f11b001b000b04221e002b241b001e0029222d1b00241d00290a0001104900ff2f4810331b000b04221e002b241b001e0029222d1b00241d00290a0001104900ff2f480833301b000b04221e002b241b001e0029222d1b00241d00290a0001104900ff2f301d002c1b00220b091b000b08221e002d241b000b0a4a00fc00002f4812340a000110281d00281b00220b091b000b08221e002d241b000b0a4a0003f0002f480c340a000110281d00281b00220b091b000b08221e002d241b000b0a490fc02f4806340a000110281d00281b00220b091b000b08221e002d241b000b0a483f2f0a000110281d002816ff031b000b041e002a1b000b0b294800391700e01b001b000b04221e002b241b001e0029222d1b00241d00290a0001104900ff2f4810331b000b041e002a1b000b0b3917001e1b000b04221e002b241b000b0b0a0001104900ff2f4808331600054800301d002c1b00220b091b000b08221e002d241b000b0a4a00fc00002f4812340a000110281d00281b00220b091b000b08221e002d241b000b0a4a0003f0002f480c340a000110281d00281b00220b091b000b041e002a1b000b0b3917001e1b000b08221e002d241b000b0a490fc02f4806340a0001101600071b000b06281d00281b00220b091b000b06281d00281b000b090000002e000126207575757575757575757575757575757575757575757575757575757575757575012b0e7776757a7d7643617c637661676a027a77065c717976706708777671667474766107767d65707c77760374766707707c7d607c7f7607757a61767166740a7c66677661447a77677b0a7a7d7d7661447a77677b0b7c666776615b767a747b670b7a7d7d76615b767a747b6709666076615274767d670b677c5f7c64766150726076077a7d77766b5c7508767f767067617c7d09667d7776757a7d76770963617c677c676a637608677c4067617a7d740470727f7f0763617c7076606010487c71797670673363617c707660604e067c717976706705677a677f76047d7c7776012e0125012402602341525150575655545b5a59585f5e5d5c43424140474645444b4a49727170777675747b7a79787f7e7d7c63626160676665646b6a6923222120272625242b2a383c2e0260224157787763747b2749586042512b233c5e75656420254b5a22412126384446527f567a245d5f717c624a475c4366697e5579597d616a6b2a5b45547072406750762e0260214157787763747b2749586042512b233c5e75656420254b5a224121263e4446527f567a245d5f717c624a475c4366697e5579597d616a6b2a5b45547072406750762e02602041525150575655545b5a59585f5e5d5c43424140474645444b4a49727170777675747b7a79787f7e7d7c63626160676665646b6a6923222120272625242b2a3e4c2e012a022222067f767d74677b0a707b7261507c7776526702222306707b72615267", [, , , , e, b]), , sign, e, void 0])
}

module.exports = {
    sign
};
```

