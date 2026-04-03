---
id: student-perfomance-prediction-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:18.978365
---

# KNOWLEDGE EXTRACT: Student-Perfomance-Prediction
> **Extracted on:** 2026-03-29 21:32:15
> **Source:** Student-Perfomance-Prediction

---

## File: `.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
brain/knowledge/docs_legacy/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
studenv/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/
```

## File: `app.py`
```python
import numpy as np
import pandas as pd
from flask import Flask,request,render_template
from sklearn.preprocessing import StandardScaler
from src.pipeline.Prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')))
        
        pred_df=data.get_data_as_data_frame()
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)        
```

## File: `Dockerfile`
```
FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD python app.py
```

## File: `LICENSE`
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

## File: `README.md`
```markdown
# Student Performance Prediction

## About The Project

The primary objective of this project is to develop a predictive model that can forecast the performance of students in their academic projects. The model aims to help educators and institutions identify students who may need additional support or intervention early in the project development process, ultimately enhancing overall student success.

## Built With

 - Pandas
 - Numpy
 - Seaborn
 - Matplotlib
 - Scikit-learn
 - Catboost
 - Flask
 - Dill

## Getting Started

This will help you understand how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation Steps

### Option 1: Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
     ```
     git clone https://github.com/KalyanMurapaka45/Student-PerfoRmance-Prediction.git
     ```

2. **Create a Virtual Environment** (Optional but recommended)
   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)
   - Activate the virtual environment based on your operating system:
       ```
       conda activate <Environment_Name>/
       ```

4. **Install Dependencies**
   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**
   - Start the project by running the appropriate command.
     ```
     python app.py
     ```

6. **Access the Project**
   - Open a web browser or the appropriate client to access the project.
  
<br><br>
### Option 2: Installation from DockerHub

If you prefer to use Docker, you can install and run the project using a Docker container from DockerHub:

1. **Pull the Docker Image**
   - Open your terminal or command prompt.
   - Run the following command to pull the Docker image from DockerHub:
     ```
     docker pull kalyan45/student-app
     ```

2. **Run the Docker Container**
   - Start the Docker container by running the following command, and mapping any necessary ports:
     ```
     docker run -p 5000:5000 kalyan45/student-app
     ```

3. **Access the Project**
   - Open a web browser or the appropriate client to access the project.


## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact

Hema Kalyan Murapaka - [@kalyanmurapaka274@gmail.com](kalyanmurapaka274@gmail.com)


## Acknowledgements

We'd like to extend our gratitude to all individuals and organizations who have played a role in the development and success of this project. Your support, whether through contributions, inspiration, or encouragement, has been invaluable. Thank you for being a part of our journey.
```

## File: `requirements.txt`
```
pandas
numpy
seaborn
matplotlib
scikit-learn
catboost
xgboost
Flask
dill
-e .
```

## File: `setup.py`
```python
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='StudentPerformance',
version='0.0.1',
author='Kalyan',
author_email='kalyanmurapaka274@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'))
```

## File: `template.py`
```python
import os
from pathlib import Path

list_of_files = [
    ".github/workflows/main.yaml",
    "Notebook_Experiments/Data/.gitkeep",
    "Notebook_Experiments/Exploratoey_Data_Analysis.ipynb",
    "Notebook_Experiments/Model_Training.ipynb",
    "src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",
    "src/components/__init__.py",
    "src/components/Data_ingestion.py",
    "src/components/Data_transformation.py",
    "src/components/Model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/Prediction_pipeline.py",
    "src/pipeline/Training_pipeline.py",
    "static/styles.css",
    "templates/home.html",
    ".gitignore",
    "app.py",
    "Dockerfile",
    "README.md",
    "requirements.txt",
    "setup.py"]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
```

## File: `Artifacts/Raw_Data.csv`
```
gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,math_score,reading_score,writing_score
female,group B,bachelor's degree,standard,none,72,72,74
female,group C,some college,standard,completed,69,90,88
female,group B,master's degree,standard,none,90,95,93
male,group A,associate's degree,free/reduced,none,47,57,44
male,group C,some college,standard,none,76,78,75
female,group B,associate's degree,standard,none,71,83,78
female,group B,some college,standard,completed,88,95,92
male,group B,some college,free/reduced,none,40,43,39
male,group D,high school,free/reduced,completed,64,64,67
female,group B,high school,free/reduced,none,38,60,50
male,group C,associate's degree,standard,none,58,54,52
male,group D,associate's degree,standard,none,40,52,43
female,group B,high school,standard,none,65,81,73
male,group A,some college,standard,completed,78,72,70
female,group A,master's degree,standard,none,50,53,58
female,group C,some high school,standard,none,69,75,78
male,group C,high school,standard,none,88,89,86
female,group B,some high school,free/reduced,none,18,32,28
male,group C,master's degree,free/reduced,completed,46,42,46
female,group C,associate's degree,free/reduced,none,54,58,61
male,group D,high school,standard,none,66,69,63
female,group B,some college,free/reduced,completed,65,75,70
male,group D,some college,standard,none,44,54,53
female,group C,some high school,standard,none,69,73,73
male,group D,bachelor's degree,free/reduced,completed,74,71,80
male,group A,master's degree,free/reduced,none,73,74,72
male,group B,some college,standard,none,69,54,55
female,group C,bachelor's degree,standard,none,67,69,75
male,group C,high school,standard,none,70,70,65
female,group D,master's degree,standard,none,62,70,75
female,group D,some college,standard,none,69,74,74
female,group B,some college,standard,none,63,65,61
female,group E,master's degree,free/reduced,none,56,72,65
male,group D,some college,standard,none,40,42,38
male,group E,some college,standard,none,97,87,82
male,group E,associate's degree,standard,completed,81,81,79
female,group D,associate's degree,standard,none,74,81,83
female,group D,some high school,free/reduced,none,50,64,59
female,group D,associate's degree,free/reduced,completed,75,90,88
male,group B,associate's degree,free/reduced,none,57,56,57
male,group C,associate's degree,free/reduced,none,55,61,54
female,group C,associate's degree,standard,none,58,73,68
female,group B,associate's degree,standard,none,53,58,65
male,group B,some college,free/reduced,completed,59,65,66
female,group E,associate's degree,free/reduced,none,50,56,54
male,group B,associate's degree,standard,none,65,54,57
female,group A,associate's degree,standard,completed,55,65,62
female,group C,high school,standard,none,66,71,76
female,group D,associate's degree,free/reduced,completed,57,74,76
male,group C,high school,standard,completed,82,84,82
male,group E,some college,standard,none,53,55,48
male,group E,associate's degree,free/reduced,completed,77,69,68
male,group C,some college,standard,none,53,44,42
male,group D,high school,standard,none,88,78,75
female,group C,some high school,free/reduced,completed,71,84,87
female,group C,high school,free/reduced,none,33,41,43
female,group E,associate's degree,standard,completed,82,85,86
male,group D,associate's degree,standard,none,52,55,49
male,group D,some college,standard,completed,58,59,58
female,group C,some high school,free/reduced,none,0,17,10
male,group E,bachelor's degree,free/reduced,completed,79,74,72
male,group A,some high school,free/reduced,none,39,39,34
male,group A,associate's degree,free/reduced,none,62,61,55
female,group C,associate's degree,standard,none,69,80,71
female,group D,some high school,standard,none,59,58,59
male,group B,some high school,standard,none,67,64,61
male,group D,some high school,free/reduced,none,45,37,37
female,group C,some college,standard,none,60,72,74
male,group B,associate's degree,free/reduced,none,61,58,56
female,group C,associate's degree,standard,none,39,64,57
female,group D,some college,free/reduced,completed,58,63,73
male,group D,some college,standard,completed,63,55,63
female,group A,associate's degree,free/reduced,none,41,51,48
male,group C,some high school,free/reduced,none,61,57,56
male,group C,some high school,standard,none,49,49,41
male,group B,associate's degree,free/reduced,none,44,41,38
male,group E,some high school,standard,none,30,26,22
male,group A,bachelor's degree,standard,completed,80,78,81
female,group D,some high school,standard,completed,61,74,72
female,group E,master's degree,standard,none,62,68,68
female,group B,associate's degree,standard,none,47,49,50
male,group B,high school,free/reduced,none,49,45,45
male,group A,some college,free/reduced,completed,50,47,54
male,group E,associate's degree,standard,none,72,64,63
male,group D,high school,free/reduced,none,42,39,34
female,group C,some college,standard,none,73,80,82
female,group C,some college,free/reduced,none,76,83,88
female,group D,associate's degree,standard,none,71,71,74
female,group A,some college,standard,none,58,70,67
female,group D,some high school,standard,none,73,86,82
female,group C,bachelor's degree,standard,none,65,72,74
male,group C,high school,free/reduced,none,27,34,36
male,group C,high school,standard,none,71,79,71
male,group C,associate's degree,free/reduced,completed,43,45,50
female,group B,some college,standard,none,79,86,92
male,group C,associate's degree,free/reduced,completed,78,81,82
male,group B,some high school,standard,completed,65,66,62
female,group E,some college,standard,completed,63,72,70
female,group D,some college,free/reduced,none,58,67,62
female,group D,bachelor's degree,standard,none,65,67,62
male,group B,some college,standard,none,79,67,67
male,group D,bachelor's degree,standard,completed,68,74,74
female,group D,associate's degree,standard,none,85,91,89
male,group B,high school,standard,completed,60,44,47
male,group C,some college,standard,completed,98,86,90
female,group C,some college,standard,none,58,67,72
female,group D,master's degree,standard,none,87,100,100
male,group E,associate's degree,standard,completed,66,63,64
female,group B,associate's degree,free/reduced,none,52,76,70
female,group B,some high school,standard,none,70,64,72
female,group D,associate's degree,free/reduced,completed,77,89,98
male,group C,high school,standard,none,62,55,49
male,group A,associate's degree,standard,none,54,53,47
female,group D,some college,standard,none,51,58,54
female,group E,bachelor's degree,standard,completed,99,100,100
male,group C,high school,standard,none,84,77,74
female,group B,bachelor's degree,free/reduced,none,75,85,82
female,group D,bachelor's degree,standard,none,78,82,79
female,group D,some high school,standard,none,51,63,61
female,group C,some college,standard,none,55,69,65
female,group C,bachelor's degree,standard,completed,79,92,89
male,group B,associate's degree,standard,completed,91,89,92
female,group C,some college,standard,completed,88,93,93
male,group D,high school,free/reduced,none,63,57,56
male,group E,some college,standard,none,83,80,73
female,group B,high school,standard,none,87,95,86
male,group B,some high school,standard,none,72,68,67
male,group D,some college,standard,completed,65,77,74
male,group D,master's degree,standard,none,82,82,74
female,group A,bachelor's degree,standard,none,51,49,51
male,group D,master's degree,standard,none,89,84,82
male,group C,some high school,free/reduced,completed,53,37,40
male,group E,some college,free/reduced,completed,87,74,70
female,group C,some college,standard,completed,75,81,84
male,group D,bachelor's degree,free/reduced,completed,74,79,75
male,group C,bachelor's degree,standard,none,58,55,48
male,group B,some high school,standard,completed,51,54,41
male,group E,high school,standard,none,70,55,56
female,group C,associate's degree,standard,none,59,66,67
male,group D,some college,standard,completed,71,61,69
female,group D,some high school,standard,none,76,72,71
female,group C,some college,free/reduced,none,59,62,64
female,group E,some college,free/reduced,completed,42,55,54
male,group A,high school,standard,none,57,43,47
male,group D,some college,standard,none,88,73,78
female,group C,some college,free/reduced,none,22,39,33
male,group B,some high school,standard,none,88,84,75
male,group C,associate's degree,free/reduced,none,73,68,66
female,group D,bachelor's degree,standard,completed,68,75,81
male,group E,associate's degree,free/reduced,completed,100,100,93
male,group A,some high school,standard,completed,62,67,69
male,group A,bachelor's degree,standard,none,77,67,68
female,group B,associate's degree,standard,completed,59,70,66
male,group D,bachelor's degree,standard,none,54,49,47
male,group D,some high school,standard,none,62,67,61
female,group C,some college,standard,completed,70,89,88
female,group E,high school,free/reduced,completed,66,74,78
male,group B,some college,free/reduced,none,60,60,60
female,group B,associate's degree,standard,completed,61,86,87
male,group D,associate's degree,free/reduced,none,66,62,64
male,group B,associate's degree,free/reduced,completed,82,78,74
female,group E,some college,free/reduced,completed,75,88,85
male,group B,master's degree,free/reduced,none,49,53,52
male,group C,high school,standard,none,52,53,49
female,group E,master's degree,standard,none,81,92,91
female,group C,bachelor's degree,standard,completed,96,100,100
male,group C,high school,free/reduced,completed,53,51,51
female,group B,master's degree,free/reduced,completed,58,76,78
female,group B,high school,standard,completed,68,83,78
female,group C,some college,free/reduced,completed,67,75,70
male,group A,high school,standard,completed,72,73,74
male,group E,some high school,standard,none,94,88,78
female,group D,some college,standard,none,79,86,81
female,group C,associate's degree,standard,none,63,67,70
female,group C,bachelor's degree,free/reduced,completed,43,51,54
female,group C,master's degree,standard,completed,81,91,87
female,group B,high school,free/reduced,completed,46,54,58
female,group C,associate's degree,standard,completed,71,77,77
female,group B,master's degree,free/reduced,completed,52,70,62
female,group D,some high school,standard,completed,97,100,100
male,group C,master's degree,free/reduced,completed,62,68,75
female,group C,some college,free/reduced,none,46,64,66
female,group E,high school,standard,none,50,50,47
female,group D,associate's degree,standard,none,65,69,70
male,group C,some high school,free/reduced,completed,45,52,49
male,group C,associate's degree,free/reduced,completed,65,67,65
male,group E,high school,standard,none,80,76,65
male,group D,some high school,standard,completed,62,66,68
male,group B,some high school,free/reduced,none,48,52,45
female,group C,bachelor's degree,standard,none,77,88,87
female,group E,associate's degree,standard,none,66,65,69
male,group D,some college,standard,completed,76,83,79
female,group B,some high school,standard,none,62,64,66
male,group D,some college,standard,completed,77,62,62
female,group C,master's degree,standard,completed,69,84,85
male,group D,associate's degree,standard,none,61,55,52
male,group C,some high school,free/reduced,completed,59,69,65
male,group E,high school,free/reduced,none,55,56,51
female,group B,some college,free/reduced,none,45,53,55
female,group B,bachelor's degree,free/reduced,none,78,79,76
female,group C,associate's degree,standard,completed,67,84,86
female,group D,some college,free/reduced,none,65,81,77
male,group C,associate's degree,standard,none,69,77,69
female,group B,associate's degree,standard,none,57,69,68
male,group C,some college,standard,none,59,41,42
male,group D,some high school,standard,completed,74,71,78
male,group E,bachelor's degree,standard,none,82,62,62
male,group E,high school,standard,completed,81,80,76
female,group B,some college,free/reduced,none,74,81,76
female,group B,some college,free/reduced,none,58,61,66
male,group D,some high school,free/reduced,completed,80,79,79
male,group C,some college,free/reduced,none,35,28,27
female,group C,high school,free/reduced,none,42,62,60
male,group C,associate's degree,free/reduced,completed,60,51,56
male,group E,high school,standard,completed,87,91,81
male,group B,some high school,standard,completed,84,83,75
female,group E,associate's degree,free/reduced,completed,83,86,88
female,group C,high school,free/reduced,none,34,42,39
male,group B,high school,free/reduced,none,66,77,70
male,group B,some high school,standard,completed,61,56,56
female,group D,high school,standard,completed,56,68,74
male,group B,associate's degree,standard,none,87,85,73
female,group C,some high school,free/reduced,none,55,65,62
male,group D,some high school,standard,none,86,80,75
female,group B,associate's degree,standard,completed,52,66,73
female,group E,master's degree,free/reduced,none,45,56,54
female,group C,some college,standard,none,72,72,71
male,group D,high school,standard,none,57,50,54
male,group A,some high school,free/reduced,none,68,72,64
female,group C,some college,standard,completed,88,95,94
male,group D,some college,standard,none,76,64,66
male,group C,associate's degree,standard,none,46,43,42
female,group B,bachelor's degree,standard,none,67,86,83
male,group E,some high school,standard,none,92,87,78
male,group C,bachelor's degree,standard,completed,83,82,84
male,group D,associate's degree,standard,none,80,75,77
male,group D,bachelor's degree,free/reduced,none,63,66,67
female,group D,some high school,standard,completed,64,60,74
male,group B,some college,standard,none,54,52,51
male,group C,associate's degree,standard,none,84,80,80
male,group D,high school,free/reduced,completed,73,68,66
female,group E,bachelor's degree,standard,none,80,83,83
female,group D,high school,standard,none,56,52,55
male,group E,some college,standard,none,59,51,43
male,group D,some high school,standard,none,75,74,69
male,group C,associate's degree,standard,none,85,76,71
male,group E,associate's degree,standard,none,89,76,74
female,group B,high school,standard,completed,58,70,68
female,group B,high school,standard,none,65,64,62
male,group C,high school,standard,none,68,60,53
male,group A,some high school,standard,completed,47,49,49
female,group D,some college,free/reduced,none,71,83,83
female,group B,some high school,standard,completed,60,70,70
male,group D,master's degree,standard,none,80,80,72
male,group D,high school,standard,none,54,52,52
female,group E,some college,standard,none,62,73,70
female,group C,associate's degree,free/reduced,none,64,73,68
male,group C,associate's degree,standard,completed,78,77,77
female,group B,some college,standard,none,70,75,78
female,group C,master's degree,free/reduced,completed,65,81,81
female,group C,some high school,free/reduced,completed,64,79,77
male,group C,some college,standard,completed,79,79,78
female,group C,some high school,free/reduced,none,44,50,51
female,group E,high school,standard,none,99,93,90
male,group D,high school,standard,none,76,73,68
male,group D,some high school,free/reduced,none,59,42,41
female,group C,bachelor's degree,standard,none,63,75,81
female,group D,high school,standard,none,69,72,77
female,group D,associate's degree,standard,completed,88,92,95
female,group E,some college,free/reduced,none,71,76,70
male,group C,bachelor's degree,standard,none,69,63,61
male,group C,some college,standard,none,58,49,42
female,group D,associate's degree,free/reduced,none,47,53,58
female,group D,some college,standard,none,65,70,71
male,group B,some college,standard,completed,88,85,76
male,group C,bachelor's degree,standard,none,83,78,73
female,group C,some high school,standard,completed,85,92,93
female,group E,high school,standard,completed,59,63,75
female,group C,some high school,free/reduced,none,65,86,80
male,group B,bachelor's degree,free/reduced,none,73,56,57
male,group D,high school,standard,none,53,52,42
male,group D,high school,standard,none,45,48,46
female,group D,bachelor's degree,free/reduced,none,73,79,84
female,group D,some college,free/reduced,completed,70,78,78
female,group B,some high school,standard,none,37,46,46
male,group B,associate's degree,standard,completed,81,82,82
male,group E,associate's degree,standard,completed,97,82,88
female,group B,some high school,standard,none,67,89,82
male,group B,bachelor's degree,free/reduced,none,88,75,76
male,group E,some high school,standard,completed,77,76,77
male,group C,associate's degree,standard,none,76,70,68
male,group D,some high school,standard,none,86,73,70
male,group C,some high school,standard,completed,63,60,57
female,group E,bachelor's degree,standard,none,65,73,75
male,group D,high school,free/reduced,completed,78,77,80
male,group B,associate's degree,free/reduced,none,67,62,60
male,group A,some high school,standard,completed,46,41,43
male,group E,associate's degree,standard,completed,71,74,68
male,group C,high school,free/reduced,completed,40,46,50
male,group D,associate's degree,free/reduced,none,90,87,75
male,group A,some college,free/reduced,completed,81,78,81
male,group D,some high school,free/reduced,none,56,54,52
female,group C,associate's degree,standard,completed,67,84,81
male,group B,associate's degree,standard,none,80,76,64
female,group C,associate's degree,standard,completed,74,75,83
male,group A,some college,standard,none,69,67,69
male,group E,some college,standard,completed,99,87,81
male,group C,some high school,standard,none,51,52,44
female,group B,associate's degree,free/reduced,none,53,71,67
female,group D,high school,free/reduced,none,49,57,52
female,group B,associate's degree,standard,none,73,76,80
male,group B,bachelor's degree,standard,none,66,60,57
male,group D,bachelor's degree,standard,completed,67,61,68
female,group C,associate's degree,free/reduced,completed,68,67,69
female,group C,bachelor's degree,standard,completed,59,64,75
male,group C,high school,standard,none,71,66,65
female,group D,master's degree,standard,completed,77,82,91
male,group C,associate's degree,standard,none,83,72,78
male,group B,bachelor's degree,standard,none,63,71,69
female,group D,associate's degree,free/reduced,none,56,65,63
female,group C,high school,free/reduced,completed,67,79,84
female,group E,high school,standard,none,75,86,79
female,group C,some college,standard,none,71,81,80
female,group C,some high school,free/reduced,none,43,53,53
female,group C,high school,free/reduced,none,41,46,43
female,group C,some college,standard,none,82,90,94
male,group C,some college,standard,none,61,61,62
male,group A,some college,free/reduced,none,28,23,19
male,group C,associate's degree,standard,completed,82,75,77
female,group B,some high school,standard,none,41,55,51
male,group C,high school,standard,none,71,60,61
male,group C,associate's degree,standard,none,47,37,35
male,group E,associate's degree,standard,completed,62,56,53
male,group B,associate's degree,standard,none,90,78,81
female,group C,bachelor's degree,standard,none,83,93,95
female,group B,some college,free/reduced,none,61,68,66
male,group D,some high school,standard,completed,76,70,69
male,group C,associate's degree,standard,none,49,51,43
female,group B,some high school,free/reduced,none,24,38,27
female,group D,some high school,free/reduced,completed,35,55,60
male,group C,high school,free/reduced,none,58,61,52
female,group C,high school,standard,none,61,73,63
female,group B,high school,standard,completed,69,76,74
male,group D,associate's degree,standard,completed,67,72,67
male,group D,some college,standard,none,79,73,67
female,group C,high school,standard,none,72,80,75
male,group B,some college,standard,none,62,61,57
female,group C,bachelor's degree,standard,completed,77,94,95
male,group D,high school,free/reduced,none,75,74,66
male,group E,associate's degree,standard,none,87,74,76
female,group B,bachelor's degree,standard,none,52,65,69
male,group E,some college,standard,none,66,57,52
female,group C,some college,standard,completed,63,78,80
female,group C,associate's degree,standard,none,46,58,57
female,group C,some college,standard,none,59,71,70
female,group B,bachelor's degree,standard,none,61,72,70
male,group A,associate's degree,standard,none,63,61,61
female,group C,some college,free/reduced,completed,42,66,69
male,group D,some college,free/reduced,none,59,62,61
female,group D,some college,standard,none,80,90,89
female,group B,high school,standard,none,58,62,59
male,group B,some high school,standard,completed,85,84,78
female,group C,some college,standard,none,52,58,58
female,group D,some high school,free/reduced,none,27,34,32
male,group C,some college,standard,none,59,60,58
male,group A,bachelor's degree,free/reduced,completed,49,58,60
male,group C,high school,standard,completed,69,58,53
male,group C,bachelor's degree,free/reduced,none,61,66,61
female,group A,some high school,free/reduced,none,44,64,58
female,group D,some high school,standard,none,73,84,85
male,group E,some college,standard,none,84,77,71
female,group C,some college,free/reduced,completed,45,73,70
male,group D,some high school,standard,none,74,74,72
female,group D,some college,standard,completed,82,97,96
female,group D,bachelor's degree,standard,none,59,70,73
male,group E,associate's degree,free/reduced,none,46,43,41
female,group D,some high school,standard,none,80,90,82
female,group D,master's degree,free/reduced,completed,85,95,100
female,group A,some high school,standard,none,71,83,77
male,group A,bachelor's degree,standard,none,66,64,62
female,group B,associate's degree,standard,none,80,86,83
male,group C,associate's degree,standard,completed,87,100,95
male,group C,master's degree,free/reduced,none,79,81,71
female,group E,some high school,free/reduced,none,38,49,45
female,group A,some high school,free/reduced,none,38,43,43
female,group E,some college,standard,none,67,76,75
female,group E,bachelor's degree,standard,none,64,73,70
female,group C,associate's degree,free/reduced,none,57,78,67
female,group D,high school,standard,none,62,64,64
male,group D,master's degree,standard,none,73,70,75
male,group E,some high school,free/reduced,completed,73,67,59
female,group D,some college,standard,none,77,68,77
male,group E,some college,standard,none,76,67,67
male,group C,associate's degree,standard,completed,57,54,56
female,group C,some high school,standard,completed,65,74,77
male,group A,high school,free/reduced,none,48,45,41
female,group B,high school,free/reduced,none,50,67,63
female,group C,associate's degree,standard,none,85,89,95
male,group B,some high school,standard,none,74,63,57
male,group D,some high school,standard,none,60,59,54
female,group C,some high school,standard,completed,59,54,67
male,group A,some college,standard,none,53,43,43
female,group A,some college,free/reduced,none,49,65,55
female,group D,high school,standard,completed,88,99,100
female,group C,high school,standard,none,54,59,62
female,group C,some high school,standard,none,63,73,68
male,group B,associate's degree,standard,completed,65,65,63
female,group B,associate's degree,standard,none,82,80,77
female,group D,high school,free/reduced,completed,52,57,56
male,group D,associate's degree,standard,completed,87,84,85
female,group D,master's degree,standard,completed,70,71,74
male,group E,some college,standard,completed,84,83,78
male,group D,associate's degree,standard,none,71,66,60
male,group B,some high school,standard,completed,63,67,67
female,group C,bachelor's degree,free/reduced,completed,51,72,79
male,group E,high school,standard,none,84,73,69
male,group C,bachelor's degree,standard,completed,71,74,68
male,group C,associate's degree,standard,none,74,73,67
male,group D,some college,standard,none,68,59,62
male,group E,high school,free/reduced,completed,57,56,54
female,group C,associate's degree,free/reduced,completed,82,93,93
female,group D,high school,standard,completed,57,58,64
female,group D,master's degree,free/reduced,completed,47,58,67
female,group A,some high school,standard,completed,59,85,80
male,group B,some college,free/reduced,none,41,39,34
female,group C,some college,free/reduced,none,62,67,62
male,group C,bachelor's degree,standard,none,86,83,86
male,group C,some high school,free/reduced,none,69,71,65
male,group A,some high school,free/reduced,none,65,59,53
male,group C,some high school,free/reduced,none,68,63,54
male,group C,associate's degree,free/reduced,none,64,66,59
female,group C,high school,standard,none,61,72,70
male,group C,high school,standard,none,61,56,55
female,group A,some high school,free/reduced,none,47,59,50
male,group C,some high school,standard,none,73,66,66
male,group C,some college,free/reduced,completed,50,48,53
male,group D,associate's degree,standard,none,75,68,64
male,group D,associate's degree,free/reduced,none,75,66,73
male,group C,high school,standard,none,70,56,51
male,group D,some high school,standard,completed,89,88,82
female,group C,some college,standard,completed,67,81,79
female,group D,high school,standard,none,78,81,80
female,group A,some high school,free/reduced,none,59,73,69
female,group B,associate's degree,standard,none,73,83,76
male,group A,some high school,free/reduced,none,79,82,73
female,group C,some high school,standard,completed,67,74,77
male,group D,some college,free/reduced,none,69,66,60
male,group C,high school,standard,completed,86,81,80
male,group B,high school,standard,none,47,46,42
male,group B,associate's degree,standard,none,81,73,72
female,group C,some college,free/reduced,completed,64,85,85
female,group E,some college,standard,none,100,92,97
female,group C,associate's degree,free/reduced,none,65,77,74
male,group C,some college,free/reduced,none,65,58,49
female,group C,associate's degree,free/reduced,none,53,61,62
male,group C,bachelor's degree,free/reduced,none,37,56,47
female,group D,bachelor's degree,standard,none,79,89,89
male,group D,associate's degree,free/reduced,none,53,54,48
female,group E,bachelor's degree,standard,none,100,100,100
male,group B,high school,standard,completed,72,65,68
male,group C,bachelor's degree,free/reduced,none,53,58,55
male,group B,some college,free/reduced,none,54,54,45
female,group E,some college,standard,none,71,70,76
female,group C,some college,free/reduced,none,77,90,91
male,group A,bachelor's degree,standard,completed,75,58,62
female,group C,some college,standard,none,84,87,91
female,group D,associate's degree,free/reduced,none,26,31,38
male,group A,high school,free/reduced,completed,72,67,65
female,group A,high school,free/reduced,completed,77,88,85
male,group C,some college,standard,none,91,74,76
female,group C,associate's degree,standard,completed,83,85,90
female,group C,high school,standard,none,63,69,74
female,group C,associate's degree,standard,completed,68,86,84
female,group D,some high school,standard,none,59,67,61
female,group B,associate's degree,standard,completed,90,90,91
female,group D,bachelor's degree,standard,completed,71,76,83
male,group E,bachelor's degree,standard,completed,76,62,66
male,group D,associate's degree,standard,none,80,68,72
female,group D,master's degree,standard,none,55,64,70
male,group E,associate's degree,standard,none,76,71,67
male,group B,high school,standard,completed,73,71,68
female,group D,associate's degree,free/reduced,none,52,59,56
male,group C,some college,free/reduced,none,68,68,61
male,group A,high school,standard,none,59,52,46
female,group B,associate's degree,standard,none,49,52,54
male,group C,high school,standard,none,70,74,71
male,group D,some college,free/reduced,none,61,47,56
female,group C,associate's degree,free/reduced,none,60,75,74
male,group B,some high school,standard,completed,64,53,57
male,group A,associate's degree,free/reduced,completed,79,82,82
female,group A,associate's degree,free/reduced,none,65,85,76
female,group C,associate's degree,standard,none,64,64,70
female,group C,some college,standard,none,83,83,90
female,group C,bachelor's degree,standard,none,81,88,90
female,group B,high school,standard,none,54,64,68
male,group D,high school,standard,completed,68,64,66
female,group C,some college,standard,none,54,48,52
female,group D,some college,free/reduced,completed,59,78,76
female,group B,some high school,standard,none,66,69,68
male,group E,some college,standard,none,76,71,72
female,group D,master's degree,standard,none,74,79,82
female,group B,associate's degree,standard,completed,94,87,92
male,group C,some college,free/reduced,none,63,61,54
female,group E,associate's degree,standard,completed,95,89,92
female,group D,master's degree,free/reduced,none,40,59,54
female,group B,some high school,standard,none,82,82,80
male,group A,high school,standard,none,68,70,66
male,group B,bachelor's degree,free/reduced,none,55,59,54
male,group C,master's degree,standard,none,79,78,77
female,group C,bachelor's degree,standard,none,86,92,87
male,group D,some college,standard,none,76,71,73
male,group A,some high school,standard,none,64,50,43
male,group D,some high school,free/reduced,none,62,49,52
female,group B,some high school,standard,completed,54,61,62
female,group B,master's degree,free/reduced,completed,77,97,94
female,group C,some high school,standard,completed,76,87,85
female,group D,some college,standard,none,74,89,84
female,group E,some college,standard,completed,66,74,73
female,group D,some high school,standard,completed,66,78,78
female,group B,high school,free/reduced,completed,67,78,79
male,group D,some college,standard,none,71,49,52
female,group C,associate's degree,standard,none,91,86,84
male,group D,bachelor's degree,standard,none,69,58,57
male,group C,master's degree,free/reduced,none,54,59,50
male,group C,high school,standard,completed,53,52,49
male,group E,some college,standard,none,68,60,59
male,group C,some high school,free/reduced,completed,56,61,60
female,group C,high school,free/reduced,none,36,53,43
female,group D,bachelor's degree,free/reduced,none,29,41,47
female,group C,associate's degree,standard,none,62,74,70
female,group C,associate's degree,standard,completed,68,67,73
female,group C,some high school,standard,none,47,54,53
male,group E,associate's degree,standard,completed,62,61,58
female,group E,associate's degree,standard,completed,79,88,94
male,group B,high school,standard,completed,73,69,68
female,group C,bachelor's degree,free/reduced,completed,66,83,83
male,group C,associate's degree,standard,completed,51,60,58
female,group D,high school,standard,none,51,66,62
male,group E,bachelor's degree,standard,completed,85,66,71
male,group A,associate's degree,standard,completed,97,92,86
male,group C,high school,standard,completed,75,69,68
male,group D,associate's degree,free/reduced,completed,79,82,80
female,group C,associate's degree,standard,none,81,77,79
female,group D,associate's degree,standard,none,82,95,89
female,group D,master's degree,standard,none,64,63,66
male,group E,some high school,free/reduced,completed,78,83,80
female,group A,some high school,standard,completed,92,100,97
male,group C,high school,standard,completed,72,67,64
female,group C,high school,free/reduced,none,62,67,64
male,group C,master's degree,standard,none,79,72,69
male,group C,some high school,free/reduced,none,79,76,65
male,group B,bachelor's degree,free/reduced,completed,87,90,88
female,group B,associate's degree,standard,none,40,48,50
male,group D,some college,free/reduced,none,77,62,64
male,group E,associate's degree,standard,none,53,45,40
female,group C,some college,free/reduced,none,32,39,33
female,group C,associate's degree,standard,completed,55,72,79
male,group C,master's degree,free/reduced,none,61,67,66
female,group B,associate's degree,free/reduced,none,53,70,70
male,group D,some high school,standard,none,73,66,62
female,group D,some college,standard,completed,74,75,79
female,group C,some college,standard,none,63,74,74
male,group C,bachelor's degree,standard,completed,96,90,92
female,group D,some college,free/reduced,completed,63,80,80
male,group B,bachelor's degree,free/reduced,none,48,51,46
male,group B,associate's degree,standard,none,48,43,45
female,group E,bachelor's degree,free/reduced,completed,92,100,100
female,group D,master's degree,free/reduced,completed,61,71,78
male,group B,high school,free/reduced,none,63,48,47
male,group D,bachelor's degree,free/reduced,none,68,68,67
male,group B,some college,standard,completed,71,75,70
male,group A,bachelor's degree,standard,none,91,96,92
female,group C,some college,standard,none,53,62,56
female,group C,high school,free/reduced,completed,50,66,64
female,group E,high school,standard,none,74,81,71
male,group A,associate's degree,free/reduced,completed,40,55,53
male,group A,some college,standard,completed,61,51,52
female,group B,high school,standard,none,81,91,89
female,group B,some college,free/reduced,completed,48,56,58
female,group D,master's degree,standard,none,53,61,68
female,group D,some high school,standard,none,81,97,96
female,group E,some high school,standard,none,77,79,80
female,group D,bachelor's degree,free/reduced,none,63,73,78
female,group D,associate's degree,standard,completed,73,75,80
female,group D,some college,standard,none,69,77,77
female,group C,associate's degree,standard,none,65,76,76
female,group A,high school,standard,none,55,73,73
female,group C,bachelor's degree,free/reduced,none,44,63,62
female,group C,some college,standard,none,54,64,65
female,group A,some high school,standard,none,48,66,65
male,group C,some college,free/reduced,none,58,57,54
male,group A,some high school,standard,none,71,62,50
male,group E,bachelor's degree,standard,none,68,68,64
female,group E,high school,standard,none,74,76,73
female,group C,bachelor's degree,standard,completed,92,100,99
female,group C,bachelor's degree,standard,completed,56,79,72
male,group B,high school,free/reduced,none,30,24,15
male,group A,some high school,standard,none,53,54,48
female,group D,high school,standard,none,69,77,73
female,group D,some high school,standard,none,65,82,81
female,group D,master's degree,standard,none,54,60,63
female,group C,high school,standard,none,29,29,30
female,group E,some college,standard,none,76,78,80
male,group D,high school,free/reduced,none,60,57,51
male,group D,master's degree,free/reduced,completed,84,89,90
male,group C,some high school,standard,none,75,72,62
female,group C,associate's degree,standard,none,85,84,82
female,group C,master's degree,free/reduced,none,40,58,54
female,group E,some college,standard,none,61,64,62
female,group B,associate's degree,standard,none,58,63,65
male,group D,some college,free/reduced,completed,69,60,63
female,group C,some college,standard,none,58,59,66
male,group C,bachelor's degree,standard,completed,94,90,91
female,group C,associate's degree,standard,none,65,77,74
female,group A,associate's degree,standard,none,82,93,93
female,group C,high school,standard,none,60,68,72
female,group E,bachelor's degree,standard,none,37,45,38
male,group D,bachelor's degree,standard,none,88,78,83
male,group D,master's degree,standard,none,95,81,84
male,group C,associate's degree,free/reduced,completed,65,73,68
female,group C,high school,free/reduced,none,35,61,54
male,group B,bachelor's degree,free/reduced,none,62,63,56
male,group C,high school,free/reduced,completed,58,51,52
male,group A,some college,standard,completed,100,96,86
female,group E,bachelor's degree,free/reduced,none,61,58,62
male,group D,some college,standard,completed,100,97,99
male,group B,associate's degree,free/reduced,completed,69,70,63
male,group D,associate's degree,standard,none,61,48,46
male,group D,some college,free/reduced,none,49,57,46
female,group C,some high school,standard,completed,44,51,55
male,group D,some college,standard,none,67,64,70
male,group B,high school,standard,none,79,60,65
female,group B,bachelor's degree,standard,completed,66,74,81
female,group C,high school,standard,none,75,88,85
male,group D,some high school,standard,none,84,84,80
male,group A,high school,standard,none,71,74,64
female,group B,high school,free/reduced,completed,67,80,81
female,group D,some high school,standard,completed,80,92,88
male,group E,some college,standard,none,86,76,74
female,group D,associate's degree,standard,none,76,74,73
male,group D,high school,standard,none,41,52,51
female,group D,associate's degree,free/reduced,completed,74,88,90
female,group B,some high school,free/reduced,none,72,81,79
female,group E,high school,standard,completed,74,79,80
male,group B,high school,standard,none,70,65,60
female,group B,bachelor's degree,standard,completed,65,81,81
female,group D,associate's degree,standard,none,59,70,65
female,group E,high school,free/reduced,none,64,62,68
female,group B,high school,standard,none,50,53,55
female,group D,some college,standard,completed,69,79,81
male,group C,some high school,free/reduced,completed,51,56,53
female,group A,high school,standard,completed,68,80,76
female,group D,some college,standard,completed,85,86,98
female,group A,associate's degree,standard,completed,65,70,74
female,group B,some high school,standard,none,73,79,79
female,group B,some college,standard,none,62,67,67
male,group C,associate's degree,free/reduced,none,77,67,64
male,group D,some high school,standard,none,69,66,61
female,group D,associate's degree,free/reduced,none,43,60,58
male,group D,associate's degree,standard,none,90,87,85
male,group C,some college,free/reduced,none,74,77,73
male,group C,some high school,standard,none,73,66,63
female,group D,some college,free/reduced,none,55,71,69
female,group C,high school,standard,none,65,69,67
male,group D,associate's degree,standard,none,80,63,63
female,group C,some high school,free/reduced,completed,50,60,60
female,group C,some college,free/reduced,completed,63,73,71
female,group B,bachelor's degree,free/reduced,none,77,85,87
male,group C,some college,standard,none,73,74,61
male,group D,associate's degree,standard,completed,81,72,77
female,group C,high school,free/reduced,none,66,76,68
male,group D,associate's degree,free/reduced,none,52,57,50
female,group C,some college,standard,none,69,78,76
female,group C,associate's degree,standard,completed,65,84,84
female,group D,high school,standard,completed,69,77,78
female,group B,some college,standard,completed,50,64,66
female,group E,some college,standard,completed,73,78,76
female,group C,some high school,standard,completed,70,82,76
male,group D,associate's degree,free/reduced,none,81,75,78
male,group D,some college,free/reduced,none,63,61,60
female,group D,high school,standard,none,67,72,74
male,group B,high school,standard,none,60,68,60
male,group B,high school,standard,none,62,55,54
female,group C,some high school,free/reduced,completed,29,40,44
male,group B,some college,standard,completed,62,66,68
female,group E,master's degree,standard,completed,94,99,100
male,group E,some college,standard,completed,85,75,68
male,group D,associate's degree,free/reduced,none,77,78,73
male,group A,high school,free/reduced,none,53,58,44
male,group E,some college,free/reduced,none,93,90,83
female,group C,associate's degree,standard,none,49,53,53
female,group E,associate's degree,free/reduced,none,73,76,78
female,group C,bachelor's degree,free/reduced,completed,66,74,81
female,group D,associate's degree,standard,none,77,77,73
female,group C,some high school,standard,none,49,63,56
female,group D,some college,free/reduced,none,79,89,86
female,group C,associate's degree,standard,completed,75,82,90
female,group A,bachelor's degree,standard,none,59,72,70
female,group D,associate's degree,standard,completed,57,78,79
male,group C,high school,free/reduced,none,66,66,59
female,group E,bachelor's degree,standard,completed,79,81,82
female,group B,some high school,standard,none,57,67,72
male,group A,bachelor's degree,standard,completed,87,84,87
female,group D,some college,standard,none,63,64,67
female,group B,some high school,free/reduced,completed,59,63,64
male,group A,bachelor's degree,free/reduced,none,62,72,65
male,group D,high school,standard,none,46,34,36
male,group C,some college,standard,none,66,59,52
male,group D,high school,standard,none,89,87,79
female,group D,associate's degree,free/reduced,completed,42,61,58
male,group C,some college,standard,completed,93,84,90
female,group E,some high school,standard,completed,80,85,85
female,group D,some college,standard,none,98,100,99
male,group D,master's degree,standard,none,81,81,84
female,group B,some high school,standard,completed,60,70,74
female,group B,associate's degree,free/reduced,completed,76,94,87
male,group C,associate's degree,standard,completed,73,78,72
female,group C,associate's degree,standard,completed,96,96,99
female,group C,high school,standard,none,76,76,74
male,group E,associate's degree,free/reduced,completed,91,73,80
female,group C,some college,free/reduced,none,62,72,70
male,group D,some high school,free/reduced,completed,55,59,59
female,group B,some high school,free/reduced,completed,74,90,88
male,group C,high school,standard,none,50,48,42
male,group B,some college,standard,none,47,43,41
male,group E,some college,standard,completed,81,74,71
female,group E,associate's degree,standard,completed,65,75,77
male,group E,some high school,standard,completed,68,51,57
female,group D,high school,free/reduced,none,73,92,84
male,group C,some college,standard,none,53,39,37
female,group B,associate's degree,free/reduced,completed,68,77,80
male,group A,some high school,free/reduced,none,55,46,43
female,group C,some college,standard,completed,87,89,94
male,group D,some high school,standard,none,55,47,44
female,group E,some college,free/reduced,none,53,58,57
male,group C,master's degree,standard,none,67,57,59
male,group C,associate's degree,standard,none,92,79,84
female,group B,some college,free/reduced,completed,53,66,73
male,group D,associate's degree,standard,none,81,71,73
male,group C,high school,free/reduced,none,61,60,55
male,group D,bachelor's degree,standard,none,80,73,72
female,group A,associate's degree,free/reduced,none,37,57,56
female,group C,high school,standard,none,81,84,82
female,group C,associate's degree,standard,completed,59,73,72
male,group B,some college,free/reduced,none,55,55,47
male,group D,associate's degree,standard,none,72,79,74
male,group D,high school,standard,none,69,75,71
male,group C,some college,standard,none,69,64,68
female,group C,bachelor's degree,free/reduced,none,50,60,59
male,group B,some college,standard,completed,87,84,86
male,group D,some high school,standard,completed,71,69,68
male,group E,some college,standard,none,68,72,65
male,group C,master's degree,free/reduced,completed,79,77,75
female,group C,some high school,standard,completed,77,90,85
male,group C,associate's degree,free/reduced,none,58,55,53
female,group E,associate's degree,standard,none,84,95,92
male,group D,some college,standard,none,55,58,52
male,group E,bachelor's degree,free/reduced,completed,70,68,72
female,group D,some college,free/reduced,completed,52,59,65
male,group B,some college,standard,completed,69,77,77
female,group C,high school,free/reduced,none,53,72,64
female,group D,some high school,standard,none,48,58,54
male,group D,some high school,standard,completed,78,81,86
female,group B,high school,standard,none,62,62,63
male,group D,some college,standard,none,60,63,59
female,group B,high school,standard,none,74,72,72
female,group C,high school,standard,completed,58,75,77
male,group B,high school,standard,completed,76,62,60
female,group D,some high school,standard,none,68,71,75
male,group A,some college,free/reduced,none,58,60,57
male,group B,high school,standard,none,52,48,49
male,group D,bachelor's degree,standard,none,75,73,74
female,group B,some high school,free/reduced,completed,52,67,72
female,group C,bachelor's degree,free/reduced,none,62,78,79
male,group B,some college,standard,none,66,65,60
female,group B,some high school,free/reduced,none,49,58,55
female,group B,high school,standard,none,66,72,70
female,group C,some college,free/reduced,none,35,44,43
female,group A,some college,standard,completed,72,79,82
male,group E,associate's degree,standard,completed,94,85,82
female,group D,associate's degree,free/reduced,none,46,56,57
female,group B,master's degree,standard,none,77,90,84
female,group B,high school,free/reduced,completed,76,85,82
female,group C,associate's degree,standard,completed,52,59,62
male,group C,bachelor's degree,standard,completed,91,81,79
female,group B,some high school,standard,completed,32,51,44
female,group E,some high school,free/reduced,none,72,79,77
female,group B,some college,standard,none,19,38,32
male,group C,associate's degree,free/reduced,none,68,65,61
female,group C,master's degree,free/reduced,none,52,65,61
female,group B,high school,standard,none,48,62,60
female,group D,some college,free/reduced,none,60,66,70
male,group D,high school,free/reduced,none,66,74,69
male,group E,some high school,standard,completed,89,84,77
female,group B,high school,standard,none,42,52,51
female,group E,associate's degree,free/reduced,completed,57,68,73
male,group D,high school,standard,none,70,70,70
female,group E,associate's degree,free/reduced,none,70,84,81
male,group E,some college,standard,none,69,60,54
female,group C,associate's degree,standard,none,52,55,57
male,group C,some high school,standard,completed,67,73,68
male,group C,some high school,standard,completed,76,80,73
female,group E,associate's degree,standard,none,87,94,95
female,group B,some college,standard,none,82,85,87
female,group C,some college,standard,none,73,76,78
male,group A,some college,free/reduced,none,75,81,74
female,group D,some college,free/reduced,none,64,74,75
female,group E,high school,free/reduced,none,41,45,40
male,group C,high school,standard,none,90,75,69
male,group B,bachelor's degree,standard,none,59,54,51
male,group A,some high school,standard,none,51,31,36
male,group A,high school,free/reduced,none,45,47,49
female,group C,master's degree,standard,completed,54,64,67
male,group E,some high school,standard,completed,87,84,76
female,group C,high school,standard,none,72,80,83
male,group B,some high school,standard,completed,94,86,87
female,group A,bachelor's degree,standard,none,45,59,64
male,group D,bachelor's degree,free/reduced,completed,61,70,76
female,group B,high school,free/reduced,none,60,72,68
female,group C,some high school,standard,none,77,91,88
female,group A,some high school,standard,completed,85,90,92
female,group D,bachelor's degree,free/reduced,none,78,90,93
male,group E,some college,free/reduced,completed,49,52,51
female,group B,high school,free/reduced,none,71,87,82
female,group C,some high school,free/reduced,none,48,58,52
male,group C,high school,standard,none,62,67,58
female,group C,associate's degree,free/reduced,completed,56,68,70
female,group C,some high school,standard,none,65,69,76
female,group D,some high school,free/reduced,completed,69,86,81
male,group B,some high school,standard,none,68,54,53
female,group A,some college,free/reduced,none,61,60,57
female,group C,bachelor's degree,free/reduced,completed,74,86,89
male,group A,bachelor's degree,standard,none,64,60,58
female,group B,high school,standard,completed,77,82,89
male,group B,some college,standard,none,58,50,45
female,group C,high school,standard,completed,60,64,74
male,group E,high school,standard,none,73,64,57
female,group A,high school,standard,completed,75,82,79
male,group B,associate's degree,free/reduced,completed,58,57,53
female,group C,associate's degree,standard,none,66,77,73
female,group D,high school,free/reduced,none,39,52,46
male,group C,some high school,standard,none,64,58,51
female,group B,high school,free/reduced,completed,23,44,36
male,group B,some college,free/reduced,completed,74,77,76
female,group D,some high school,free/reduced,completed,40,65,64
male,group E,master's degree,standard,none,90,85,84
male,group C,master's degree,standard,completed,91,85,85
male,group D,high school,standard,none,64,54,50
female,group C,high school,standard,none,59,72,68
male,group D,associate's degree,standard,none,80,75,69
male,group C,master's degree,standard,none,71,67,67
female,group A,high school,standard,none,61,68,63
female,group E,some college,standard,none,87,85,93
male,group E,some high school,standard,none,82,67,61
male,group C,some high school,standard,none,62,64,55
female,group B,bachelor's degree,standard,none,97,97,96
male,group B,some college,free/reduced,none,75,68,65
female,group C,bachelor's degree,standard,none,65,79,81
male,group B,high school,standard,completed,52,49,46
male,group C,associate's degree,free/reduced,none,87,73,72
female,group C,associate's degree,standard,none,53,62,53
female,group E,master's degree,free/reduced,none,81,86,87
male,group D,bachelor's degree,free/reduced,completed,39,42,38
female,group C,some college,standard,completed,71,71,80
male,group C,associate's degree,standard,none,97,93,91
male,group D,some college,standard,completed,82,82,88
male,group C,high school,free/reduced,none,59,53,52
male,group B,associate's degree,standard,none,61,42,41
male,group E,associate's degree,free/reduced,completed,78,74,72
male,group C,associate's degree,free/reduced,none,49,51,51
male,group B,high school,standard,none,59,58,47
female,group C,some college,standard,completed,70,72,76
male,group B,associate's degree,standard,completed,82,84,78
male,group E,associate's degree,free/reduced,none,90,90,82
female,group C,bachelor's degree,free/reduced,none,43,62,61
male,group C,some college,free/reduced,none,80,64,66
male,group D,some college,standard,none,81,82,84
male,group C,some high school,standard,none,57,61,54
female,group D,some high school,standard,none,59,72,80
female,group D,associate's degree,standard,none,64,76,74
male,group C,bachelor's degree,standard,completed,63,64,66
female,group E,bachelor's degree,standard,completed,71,70,70
female,group B,high school,free/reduced,none,64,73,71
male,group D,bachelor's degree,free/reduced,none,55,46,44
female,group E,associate's degree,standard,none,51,51,54
female,group C,associate's degree,standard,completed,62,76,80
female,group E,associate's degree,standard,completed,93,100,95
male,group C,high school,free/reduced,none,54,72,59
female,group D,some college,free/reduced,none,69,65,74
male,group D,high school,free/reduced,none,44,51,48
female,group E,some college,standard,completed,86,85,91
female,group E,associate's degree,standard,none,85,92,85
female,group A,master's degree,free/reduced,none,50,67,73
male,group D,some high school,standard,completed,88,74,75
female,group E,associate's degree,standard,none,59,62,69
female,group E,some high school,free/reduced,none,32,34,38
male,group B,high school,free/reduced,none,36,29,27
female,group B,some high school,free/reduced,completed,63,78,79
male,group D,associate's degree,standard,completed,67,54,63
female,group D,some high school,standard,completed,65,78,82
male,group D,master's degree,standard,none,85,84,89
female,group C,master's degree,standard,none,73,78,74
female,group A,high school,free/reduced,completed,34,48,41
female,group D,bachelor's degree,free/reduced,completed,93,100,100
female,group D,some high school,free/reduced,none,67,84,84
male,group D,some college,standard,none,88,77,77
male,group B,high school,standard,none,57,48,51
female,group D,some college,standard,completed,79,84,91
female,group C,bachelor's degree,free/reduced,none,67,75,72
male,group E,bachelor's degree,standard,completed,70,64,70
male,group D,bachelor's degree,free/reduced,none,50,42,48
female,group A,some college,standard,none,69,84,82
female,group C,bachelor's degree,standard,completed,52,61,66
female,group C,bachelor's degree,free/reduced,completed,47,62,66
female,group B,associate's degree,free/reduced,none,46,61,55
female,group E,some college,standard,none,68,70,66
male,group E,bachelor's degree,standard,completed,100,100,100
female,group C,high school,standard,none,44,61,52
female,group C,associate's degree,standard,completed,57,77,80
male,group B,some college,standard,completed,91,96,91
male,group D,high school,free/reduced,none,69,70,67
female,group C,high school,free/reduced,none,35,53,46
male,group D,high school,standard,none,72,66,66
female,group B,associate's degree,free/reduced,none,54,65,65
male,group D,high school,free/reduced,none,74,70,69
male,group E,some high school,standard,completed,74,64,60
male,group E,associate's degree,free/reduced,none,64,56,52
female,group D,high school,free/reduced,completed,65,61,71
male,group E,associate's degree,free/reduced,completed,46,43,44
female,group C,some high school,free/reduced,none,48,56,51
male,group C,some college,free/reduced,completed,67,74,70
male,group D,some college,free/reduced,none,62,57,62
male,group D,associate's degree,free/reduced,completed,61,71,73
male,group C,bachelor's degree,free/reduced,completed,70,75,74
male,group C,associate's degree,standard,completed,98,87,90
male,group D,some college,free/reduced,none,70,63,58
male,group A,associate's degree,standard,none,67,57,53
female,group E,high school,free/reduced,none,57,58,57
male,group D,some college,standard,completed,85,81,85
male,group D,some high school,standard,completed,77,68,69
male,group C,master's degree,free/reduced,completed,72,66,72
female,group D,master's degree,standard,none,78,91,96
male,group C,high school,standard,none,81,66,64
male,group A,some high school,free/reduced,completed,61,62,61
female,group B,high school,standard,none,58,68,61
female,group C,associate's degree,standard,none,54,61,58
male,group B,high school,standard,none,82,82,80
female,group D,some college,free/reduced,none,49,58,60
male,group B,some high school,free/reduced,completed,49,50,52
female,group E,high school,free/reduced,completed,57,75,73
male,group E,high school,standard,none,94,73,71
female,group D,some college,standard,completed,75,77,83
female,group E,some high school,free/reduced,none,74,74,72
male,group C,high school,standard,completed,58,52,54
female,group C,some college,standard,none,62,69,69
male,group E,associate's degree,standard,none,72,57,62
male,group C,some college,standard,none,84,87,81
female,group D,master's degree,standard,none,92,100,100
female,group D,high school,standard,none,45,63,59
male,group C,high school,standard,none,75,81,71
female,group A,some college,standard,none,56,58,64
female,group D,some high school,free/reduced,none,48,54,53
female,group E,associate's degree,standard,none,100,100,100
female,group C,some high school,free/reduced,completed,65,76,75
male,group D,some college,standard,none,72,57,58
female,group D,some college,standard,none,62,70,72
male,group A,some high school,standard,completed,66,68,64
male,group C,some college,standard,none,63,63,60
female,group E,associate's degree,standard,none,68,76,67
female,group B,bachelor's degree,standard,none,75,84,80
female,group D,bachelor's degree,standard,none,89,100,100
male,group C,some high school,standard,completed,78,72,69
female,group A,high school,free/reduced,completed,53,50,60
female,group D,some college,free/reduced,none,49,65,61
female,group A,some college,standard,none,54,63,67
female,group C,some college,standard,completed,64,82,77
male,group B,some college,free/reduced,completed,60,62,60
male,group C,associate's degree,standard,none,62,65,58
male,group D,high school,standard,completed,55,41,48
female,group C,associate's degree,standard,none,91,95,94
female,group B,high school,free/reduced,none,8,24,23
male,group D,some high school,standard,none,81,78,78
male,group B,some high school,standard,completed,79,85,86
female,group A,some college,standard,completed,78,87,91
female,group C,some high school,standard,none,74,75,82
male,group A,high school,standard,none,57,51,54
female,group C,associate's degree,standard,none,40,59,51
male,group E,some high school,standard,completed,81,75,76
female,group A,some high school,free/reduced,none,44,45,45
female,group D,some college,free/reduced,completed,67,86,83
male,group E,high school,free/reduced,completed,86,81,75
female,group B,some high school,standard,completed,65,82,78
female,group D,associate's degree,free/reduced,none,55,76,76
female,group D,bachelor's degree,free/reduced,none,62,72,74
male,group A,high school,standard,none,63,63,62
female,group E,master's degree,standard,completed,88,99,95
male,group C,high school,free/reduced,none,62,55,55
female,group C,high school,free/reduced,completed,59,71,65
female,group D,some college,standard,completed,68,78,77
female,group D,some college,free/reduced,none,77,86,86
```

## File: `Artifacts/Test_Data.csv`
```
gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,math_score,reading_score,writing_score
female,group C,associate's degree,standard,none,91,86,84
female,group B,some college,free/reduced,completed,53,66,73
male,group D,bachelor's degree,standard,none,80,73,72
male,group C,some college,free/reduced,none,74,77,73
male,group E,some college,standard,completed,84,83,78
male,group D,associate's degree,free/reduced,none,81,75,78
male,group B,associate's degree,free/reduced,completed,69,70,63
female,group B,some high school,standard,completed,54,61,62
male,group C,associate's degree,free/reduced,none,87,73,72
male,group B,some high school,standard,completed,51,54,41
male,group A,high school,free/reduced,none,45,47,49
male,group E,some high school,standard,none,30,26,22
female,group B,high school,free/reduced,completed,67,80,81
female,group D,some college,free/reduced,none,49,65,61
male,group D,some college,standard,completed,85,81,85
female,group D,some high school,standard,completed,65,78,82
male,group D,high school,standard,none,53,52,42
male,group D,bachelor's degree,free/reduced,none,55,46,44
female,group D,some high school,standard,none,48,58,54
female,group D,associate's degree,free/reduced,none,56,65,63
male,group C,master's degree,standard,none,79,72,69
female,group C,bachelor's degree,free/reduced,completed,43,51,54
female,group C,some college,free/reduced,completed,45,73,70
female,group C,high school,free/reduced,none,36,53,43
male,group D,some high school,free/reduced,completed,80,79,79
male,group D,associate's degree,standard,none,80,75,77
male,group D,bachelor's degree,standard,completed,68,74,74
female,group C,associate's degree,standard,none,40,59,51
female,group A,high school,free/reduced,completed,34,48,41
female,group D,some college,free/reduced,none,49,58,60
male,group B,some college,standard,none,62,61,57
male,group D,some college,standard,completed,71,61,69
male,group B,bachelor's degree,free/reduced,none,62,63,56
male,group E,some college,standard,none,76,71,72
male,group E,some college,standard,none,84,77,71
female,group B,some college,free/reduced,none,45,53,55
male,group D,associate's degree,free/reduced,none,77,78,73
female,group D,some college,standard,none,69,77,77
female,group C,master's degree,standard,none,73,78,74
female,group C,some high school,free/reduced,none,0,17,10
male,group C,associate's degree,standard,completed,82,75,77
male,group B,some high school,standard,completed,65,66,62
male,group D,bachelor's degree,standard,completed,67,61,68
female,group A,some college,standard,none,54,63,67
male,group D,associate's degree,free/reduced,none,90,87,75
female,group E,high school,standard,completed,59,63,75
male,group D,high school,free/reduced,none,74,70,69
female,group C,high school,standard,none,29,29,30
male,group D,some high school,standard,completed,89,88,82
female,group A,high school,standard,completed,75,82,79
male,group B,some college,standard,completed,71,75,70
female,group D,associate's degree,standard,none,64,76,74
male,group C,some college,standard,completed,79,79,78
female,group B,some college,free/reduced,completed,48,56,58
female,group C,some high school,standard,none,69,73,73
female,group D,some college,standard,none,69,74,74
male,group D,bachelor's degree,standard,none,88,78,83
male,group C,associate's degree,standard,none,58,54,52
male,group B,associate's degree,standard,none,87,85,73
female,group A,some high school,standard,completed,85,90,92
male,group A,some high school,standard,completed,46,41,43
female,group C,some high school,free/reduced,completed,71,84,87
female,group C,associate's degree,standard,none,81,77,79
female,group B,some college,free/reduced,none,58,61,66
male,group D,master's degree,free/reduced,completed,84,89,90
female,group C,bachelor's degree,free/reduced,completed,66,74,81
female,group D,some college,free/reduced,none,55,71,69
male,group C,high school,free/reduced,none,59,53,52
female,group D,some college,free/reduced,completed,58,63,73
female,group D,associate's degree,standard,none,82,95,89
male,group E,associate's degree,standard,completed,66,63,64
female,group C,bachelor's degree,standard,none,81,88,90
male,group C,some college,free/reduced,none,58,57,54
female,group A,associate's degree,free/reduced,none,37,57,56
male,group C,some high school,standard,completed,63,60,57
male,group E,some high school,standard,completed,77,76,77
female,group D,some college,standard,completed,85,86,98
male,group B,associate's degree,free/reduced,none,57,56,57
female,group A,some high school,standard,none,48,66,65
male,group C,some high school,standard,none,51,52,44
male,group D,some college,free/reduced,none,63,61,60
male,group D,some high school,free/reduced,none,45,37,37
male,group C,bachelor's degree,standard,none,83,78,73
female,group C,some college,standard,none,60,72,74
male,group B,bachelor's degree,standard,none,63,71,69
female,group C,high school,free/reduced,none,62,67,64
female,group D,some college,standard,completed,68,78,77
female,group B,some high school,standard,completed,60,70,74
female,group C,some high school,standard,completed,77,90,85
male,group A,some college,free/reduced,none,28,23,19
male,group C,master's degree,free/reduced,none,79,81,71
female,group E,some college,standard,none,100,92,97
male,group D,bachelor's degree,standard,none,69,58,57
male,group B,high school,free/reduced,none,66,77,70
female,group B,some college,standard,none,19,38,32
male,group D,associate's degree,standard,none,75,68,64
male,group D,some college,standard,none,60,63,59
female,group A,some college,standard,none,58,70,67
female,group C,associate's degree,standard,none,69,80,71
female,group C,associate's degree,free/reduced,completed,56,68,70
male,group C,associate's degree,standard,completed,73,78,72
male,group E,some college,standard,none,66,57,52
male,group A,associate's degree,standard,none,67,57,53
female,group C,associate's degree,free/reduced,none,64,73,68
male,group A,high school,standard,none,71,74,64
male,group B,high school,standard,none,70,65,60
male,group E,associate's degree,standard,none,53,45,40
male,group C,high school,standard,none,75,81,71
female,group B,high school,standard,completed,68,83,78
female,group C,high school,standard,none,44,61,52
female,group D,bachelor's degree,free/reduced,none,29,41,47
female,group B,high school,free/reduced,none,71,87,82
male,group A,high school,standard,none,57,51,54
female,group A,bachelor's degree,standard,none,45,59,64
female,group C,some college,free/reduced,none,76,83,88
male,group C,high school,standard,none,61,56,55
male,group C,some high school,free/reduced,completed,45,52,49
male,group D,high school,standard,completed,55,41,48
male,group B,high school,standard,completed,73,69,68
male,group D,high school,free/reduced,completed,78,77,80
female,group A,master's degree,free/reduced,none,50,67,73
female,group C,some college,free/reduced,none,62,67,62
male,group D,master's degree,standard,none,81,81,84
female,group C,some high school,free/reduced,completed,64,79,77
female,group D,some high school,standard,completed,64,60,74
male,group D,some high school,standard,none,73,66,62
female,group D,associate's degree,standard,completed,73,75,80
female,group C,some high school,standard,completed,67,74,77
male,group B,associate's degree,standard,none,61,42,41
male,group C,some high school,standard,completed,67,73,68
female,group D,some high school,standard,none,65,82,81
male,group D,associate's degree,standard,none,80,75,69
male,group D,some high school,free/reduced,none,59,42,41
female,group E,master's degree,standard,completed,88,99,95
female,group C,associate's degree,standard,none,62,74,70
female,group C,high school,free/reduced,none,33,41,43
female,group C,bachelor's degree,standard,completed,79,92,89
male,group B,some high school,standard,completed,84,83,75
male,group A,master's degree,free/reduced,none,73,74,72
female,group A,associate's degree,free/reduced,none,41,51,48
female,group E,associate's degree,free/reduced,none,50,56,54
female,group B,high school,standard,completed,58,70,68
male,group D,some high school,free/reduced,completed,55,59,59
male,group D,high school,standard,none,45,48,46
male,group D,some high school,standard,completed,88,74,75
female,group B,associate's degree,free/reduced,none,46,61,55
male,group A,some high school,standard,none,51,31,36
male,group D,some high school,standard,none,75,74,69
male,group E,some college,free/reduced,completed,49,52,51
female,group E,high school,standard,none,75,86,79
female,group E,high school,standard,completed,74,79,80
female,group B,associate's degree,standard,completed,61,86,87
male,group C,associate's degree,standard,none,62,65,58
male,group C,some high school,free/reduced,none,68,63,54
female,group D,master's degree,standard,none,78,91,96
female,group E,some college,standard,none,71,70,76
female,group D,high school,free/reduced,none,49,57,52
female,group A,bachelor's degree,standard,none,59,72,70
male,group E,bachelor's degree,free/reduced,completed,79,74,72
female,group E,associate's degree,standard,none,51,51,54
female,group C,bachelor's degree,standard,completed,56,79,72
male,group B,high school,standard,completed,76,62,60
female,group D,some college,standard,completed,69,79,81
male,group C,some high school,free/reduced,completed,51,56,53
male,group D,some college,standard,completed,82,82,88
male,group C,some college,standard,none,73,74,61
male,group C,high school,free/reduced,completed,40,46,50
male,group E,some college,free/reduced,none,93,90,83
female,group C,bachelor's degree,standard,completed,59,64,75
female,group B,associate's degree,standard,none,73,76,80
male,group B,some high school,standard,completed,85,84,78
male,group E,associate's degree,standard,none,76,71,67
female,group D,associate's degree,free/reduced,completed,77,89,98
female,group D,some college,free/reduced,completed,67,86,83
male,group D,some college,free/reduced,none,61,47,56
female,group D,some high school,free/reduced,none,27,34,32
male,group D,high school,standard,none,54,52,52
female,group C,master's degree,free/reduced,completed,65,81,81
female,group E,associate's degree,standard,none,87,94,95
female,group C,some high school,standard,completed,70,82,76
female,group B,high school,standard,none,54,64,68
female,group C,high school,free/reduced,none,66,76,68
female,group D,master's degree,free/reduced,completed,85,95,100
male,group C,some high school,free/reduced,completed,56,61,60
male,group E,master's degree,standard,none,90,85,84
male,group E,high school,standard,none,70,55,56
female,group B,bachelor's degree,standard,none,61,72,70
male,group A,bachelor's degree,free/reduced,completed,49,58,60
male,group C,high school,standard,none,81,66,64
male,group B,some college,standard,completed,87,84,86
male,group B,some high school,free/reduced,completed,49,50,52
male,group B,some high school,standard,none,68,54,53
male,group C,associate's degree,free/reduced,none,77,67,64
female,group B,bachelor's degree,free/reduced,none,78,79,76
male,group C,associate's degree,free/reduced,completed,60,51,56
female,group D,high school,free/reduced,completed,52,57,56
male,group E,associate's degree,standard,completed,62,56,53
female,group B,some college,free/reduced,none,74,81,76
female,group C,associate's degree,standard,none,65,77,74
female,group D,some high school,standard,completed,61,74,72
```

## File: `Artifacts/Train_Data.csv`
```
gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,math_score,reading_score,writing_score
female,group D,master's degree,standard,none,62,70,75
female,group C,bachelor's degree,free/reduced,completed,66,83,83
female,group D,some college,free/reduced,none,79,89,86
male,group C,master's degree,free/reduced,none,61,67,66
male,group E,high school,standard,none,73,64,57
male,group B,high school,free/reduced,none,30,24,15
female,group C,bachelor's degree,standard,completed,96,100,100
female,group C,associate's degree,standard,completed,57,77,80
male,group D,high school,standard,completed,68,64,66
female,group C,some high school,free/reduced,none,48,58,52
male,group B,some high school,standard,none,67,64,61
female,group C,some college,free/reduced,none,59,62,64
male,group E,some high school,standard,completed,74,64,60
female,group C,some high school,standard,none,65,69,76
female,group B,some college,standard,none,62,67,67
male,group C,associate's degree,standard,none,47,37,35
male,group D,associate's degree,standard,none,80,63,63
male,group C,high school,standard,none,68,60,53
female,group D,some college,standard,completed,79,84,91
male,group D,high school,standard,none,89,87,79
male,group A,some college,standard,none,69,67,69
female,group E,some college,free/reduced,none,53,58,57
female,group C,some college,standard,completed,64,82,77
male,group C,high school,standard,completed,82,84,82
male,group B,high school,free/reduced,none,36,29,27
female,group B,master's degree,standard,none,90,95,93
female,group D,master's degree,standard,none,64,63,66
female,group B,bachelor's degree,standard,none,52,65,69
female,group D,some high school,free/reduced,none,67,84,84
male,group C,associate's degree,standard,completed,51,60,58
male,group D,some college,standard,none,79,73,67
male,group A,high school,standard,none,63,63,62
female,group D,associate's degree,free/reduced,none,52,59,56
male,group A,associate's degree,free/reduced,completed,40,55,53
male,group D,some college,standard,none,40,42,38
female,group B,some college,standard,none,63,65,61
male,group C,associate's degree,standard,none,46,43,42
female,group C,some high school,free/reduced,completed,65,76,75
female,group B,some high school,standard,none,62,64,66
male,group B,associate's degree,standard,none,90,78,81
male,group A,associate's degree,free/reduced,none,47,57,44
male,group C,some college,standard,none,59,41,42
female,group B,master's degree,free/reduced,completed,77,97,94
female,group C,associate's degree,standard,none,52,55,57
male,group E,some college,standard,completed,99,87,81
female,group B,some high school,standard,none,70,64,72
male,group C,associate's degree,free/reduced,none,64,66,59
male,group A,bachelor's degree,standard,completed,80,78,81
male,group D,high school,free/reduced,none,42,39,34
male,group E,associate's degree,standard,completed,97,82,88
male,group A,some college,free/reduced,completed,50,47,54
female,group B,some high school,standard,completed,65,82,78
female,group C,master's degree,free/reduced,none,52,65,61
female,group E,associate's degree,standard,none,59,62,69
male,group B,some high school,standard,none,74,63,57
female,group C,some high school,free/reduced,none,43,53,53
female,group B,high school,free/reduced,completed,67,78,79
male,group E,bachelor's degree,standard,completed,100,100,100
male,group D,high school,standard,none,72,66,66
female,group B,associate's degree,standard,none,71,83,78
male,group A,some high school,free/reduced,none,55,46,43
female,group C,some college,standard,none,84,87,91
female,group E,some college,standard,completed,63,72,70
female,group C,bachelor's degree,standard,none,63,75,81
female,group C,some college,free/reduced,completed,42,66,69
male,group E,associate's degree,free/reduced,completed,78,74,72
male,group E,some college,standard,none,69,60,54
female,group B,associate's degree,standard,none,80,86,83
male,group B,high school,standard,none,79,60,65
male,group C,associate's degree,standard,completed,87,100,95
female,group A,associate's degree,free/reduced,none,65,85,76
female,group D,some high school,standard,none,51,63,61
male,group D,master's degree,standard,none,85,84,89
male,group A,some high school,standard,completed,47,49,49
male,group C,master's degree,free/reduced,none,54,59,50
female,group B,high school,free/reduced,none,38,60,50
male,group C,some high school,free/reduced,completed,59,69,65
male,group D,high school,free/reduced,none,60,57,51
male,group B,high school,free/reduced,none,49,45,45
female,group C,associate's degree,standard,completed,52,59,62
female,group C,bachelor's degree,free/reduced,none,44,63,62
female,group E,associate's degree,free/reduced,none,70,84,81
male,group C,associate's degree,standard,none,84,80,80
male,group C,associate's degree,standard,none,76,70,68
male,group C,some college,free/reduced,none,35,28,27
female,group C,associate's degree,standard,completed,96,96,99
female,group D,some college,standard,none,80,90,89
male,group B,associate's degree,standard,none,81,73,72
male,group D,high school,standard,none,57,50,54
male,group E,high school,standard,none,94,73,71
male,group B,high school,standard,none,82,82,80
male,group D,high school,standard,none,70,70,70
female,group B,associate's degree,standard,completed,94,87,92
male,group A,bachelor's degree,standard,completed,75,58,62
female,group C,some college,standard,none,52,58,58
female,group A,high school,free/reduced,completed,77,88,85
male,group D,some college,free/reduced,none,70,63,58
male,group A,some high school,free/reduced,none,65,59,53
male,group B,some college,free/reduced,none,40,43,39
female,group C,some college,standard,completed,70,89,88
male,group D,associate's degree,free/reduced,completed,79,82,80
female,group C,some college,standard,completed,67,81,79
male,group C,some college,free/reduced,none,68,68,61
female,group D,master's degree,free/reduced,completed,47,58,67
female,group A,some college,standard,completed,72,79,82
female,group E,high school,free/reduced,completed,57,75,73
female,group C,bachelor's degree,standard,none,83,93,95
male,group A,some college,standard,completed,61,51,52
male,group C,associate's degree,standard,completed,98,87,90
female,group D,master's degree,free/reduced,completed,61,71,78
female,group C,bachelor's degree,standard,completed,92,100,99
female,group C,associate's degree,standard,completed,68,67,73
female,group E,some high school,standard,none,77,79,80
male,group C,some college,standard,none,66,59,52
male,group B,high school,standard,none,47,46,42
male,group C,some college,free/reduced,none,65,58,49
male,group A,some high school,free/reduced,none,68,72,64
female,group C,some college,standard,completed,63,78,80
female,group D,high school,free/reduced,none,73,92,84
female,group C,high school,free/reduced,none,42,62,60
female,group E,master's degree,standard,none,62,68,68
female,group D,bachelor's degree,standard,completed,68,75,81
female,group C,associate's degree,standard,completed,67,84,81
male,group D,some college,free/reduced,none,49,57,46
female,group C,some college,free/reduced,none,35,44,43
male,group A,high school,standard,none,68,70,66
female,group B,high school,standard,completed,69,76,74
male,group C,high school,standard,none,70,74,71
female,group E,some high school,standard,completed,80,85,85
female,group C,some college,standard,completed,75,81,84
female,group D,some college,standard,none,63,64,67
male,group B,bachelor's degree,standard,none,66,60,57
female,group B,some high school,free/reduced,completed,74,90,88
female,group C,some high school,standard,completed,44,51,55
female,group B,bachelor's degree,standard,none,72,72,74
female,group D,master's degree,standard,completed,77,82,91
male,group D,high school,standard,none,46,34,36
male,group C,high school,standard,completed,72,67,64
male,group B,associate's degree,standard,completed,82,84,78
male,group E,associate's degree,standard,completed,62,61,58
male,group D,associate's degree,standard,none,80,68,72
female,group C,high school,standard,none,54,59,62
female,group D,some college,standard,none,79,86,81
female,group B,high school,standard,none,87,95,86
female,group C,some high school,standard,completed,65,74,77
female,group C,associate's degree,free/reduced,completed,82,93,93
female,group B,associate's degree,standard,none,40,48,50
female,group D,bachelor's degree,free/reduced,completed,93,100,100
female,group C,bachelor's degree,standard,none,65,72,74
male,group D,some high school,standard,completed,77,68,69
female,group C,some college,free/reduced,none,46,64,66
male,group B,some college,standard,completed,88,85,76
female,group E,some high school,free/reduced,none,32,34,38
female,group C,associate's degree,standard,none,39,64,57
male,group D,some high school,standard,none,86,73,70
male,group C,some high school,free/reduced,completed,53,37,40
male,group A,some college,free/reduced,completed,81,78,81
male,group B,some college,free/reduced,none,41,39,34
male,group C,some college,standard,none,61,61,62
male,group D,some college,standard,none,88,73,78
female,group A,some high school,standard,completed,59,85,80
female,group D,some high school,standard,none,81,97,96
male,group C,bachelor's degree,standard,none,58,55,48
female,group C,some college,free/reduced,completed,64,85,85
female,group E,master's degree,standard,none,81,92,91
male,group C,high school,standard,none,70,70,65
female,group C,bachelor's degree,free/reduced,none,62,78,79
male,group D,some college,standard,completed,77,62,62
female,group D,high school,standard,none,62,64,64
female,group E,some college,standard,none,87,85,93
female,group C,some college,free/reduced,completed,67,75,70
male,group A,bachelor's degree,free/reduced,none,62,72,65
female,group D,some high school,standard,none,76,72,71
female,group C,associate's degree,standard,none,63,67,70
female,group B,some college,standard,completed,88,95,92
male,group D,associate's degree,standard,none,72,79,74
female,group D,master's degree,standard,none,55,64,70
male,group C,some high school,free/reduced,none,61,57,56
male,group D,bachelor's degree,free/reduced,none,50,42,48
male,group E,some high school,standard,completed,87,84,76
male,group B,some college,standard,none,54,52,51
female,group C,some college,free/reduced,none,22,39,33
male,group D,high school,free/reduced,none,66,74,69
male,group C,bachelor's degree,standard,completed,83,82,84
female,group D,high school,standard,completed,56,68,74
female,group B,associate's degree,free/reduced,none,54,65,65
female,group D,master's degree,standard,none,74,79,82
male,group E,some college,free/reduced,completed,87,74,70
male,group E,high school,free/reduced,completed,86,81,75
male,group B,some college,standard,none,66,65,60
male,group C,associate's degree,free/reduced,completed,65,67,65
female,group C,associate's degree,standard,none,58,73,68
female,group C,associate's degree,standard,completed,75,82,90
female,group B,associate's degree,free/reduced,none,52,76,70
female,group C,some college,standard,none,54,64,65
female,group E,associate's degree,standard,completed,82,85,86
female,group C,some high school,standard,none,63,73,68
female,group A,some high school,free/reduced,none,59,73,69
male,group E,bachelor's degree,free/reduced,completed,70,68,72
female,group C,high school,free/reduced,completed,59,71,65
male,group D,bachelor's degree,free/reduced,completed,74,71,80
male,group A,high school,free/reduced,completed,72,67,65
male,group A,associate's degree,standard,completed,97,92,86
female,group C,some high school,standard,none,47,54,53
male,group D,master's degree,standard,none,95,81,84
female,group C,some high school,standard,none,49,63,56
male,group E,associate's degree,free/reduced,none,64,56,52
female,group B,some high school,free/reduced,none,24,38,27
male,group E,associate's degree,free/reduced,completed,77,69,68
male,group B,bachelor's degree,free/reduced,none,55,59,54
female,group D,some college,standard,none,74,89,84
male,group D,high school,free/reduced,none,69,70,67
female,group B,master's degree,standard,none,77,90,84
male,group D,high school,standard,none,76,73,68
male,group D,bachelor's degree,free/reduced,completed,61,70,76
male,group C,some college,standard,completed,93,84,90
male,group B,high school,standard,none,62,55,54
male,group A,bachelor's degree,standard,none,64,60,58
female,group D,some high school,standard,completed,66,78,78
male,group C,high school,standard,completed,86,81,80
male,group C,master's degree,free/reduced,completed,46,42,46
female,group B,associate's degree,free/reduced,completed,76,94,87
male,group A,high school,standard,none,59,52,46
male,group B,high school,free/reduced,none,63,48,47
female,group A,some high school,free/reduced,none,47,59,50
male,group C,bachelor's degree,free/reduced,none,61,66,61
male,group E,associate's degree,standard,none,72,64,63
male,group A,some high school,free/reduced,none,39,39,34
male,group E,some college,standard,none,86,76,74
female,group D,associate's degree,free/reduced,none,47,53,58
male,group B,associate's degree,standard,completed,81,82,82
female,group B,high school,standard,none,58,62,59
female,group C,some college,standard,none,59,71,70
female,group D,bachelor's degree,standard,none,79,89,89
female,group C,some high school,free/reduced,none,65,86,80
female,group B,high school,standard,none,65,81,73
female,group E,high school,standard,none,50,50,47
female,group A,some high school,free/reduced,none,44,64,58
female,group E,bachelor's degree,standard,completed,71,70,70
female,group C,high school,standard,none,60,68,72
male,group D,some high school,standard,none,86,80,75
female,group C,some college,standard,none,53,62,56
female,group D,bachelor's degree,standard,none,89,100,100
female,group A,associate's degree,standard,completed,65,70,74
male,group E,some high school,free/reduced,completed,78,83,80
female,group D,bachelor's degree,free/reduced,none,63,73,78
female,group C,high school,standard,none,75,88,85
female,group B,high school,free/reduced,completed,46,54,58
female,group C,some high school,free/reduced,completed,50,60,60
female,group C,associate's degree,standard,completed,65,84,84
female,group C,associate's degree,standard,none,65,76,76
male,group E,associate's degree,free/reduced,none,90,90,82
male,group C,associate's degree,standard,completed,57,54,56
male,group C,high school,standard,none,52,53,49
female,group B,high school,standard,none,65,64,62
male,group D,some high school,standard,none,84,84,80
female,group C,associate's degree,standard,completed,62,76,80
male,group D,associate's degree,standard,completed,81,72,77
male,group E,associate's degree,free/reduced,none,46,43,41
male,group D,associate's degree,standard,none,71,66,60
male,group C,some high school,standard,none,49,49,41
female,group D,some college,standard,none,51,58,54
female,group D,high school,standard,none,69,77,73
female,group D,some high school,free/reduced,none,48,54,53
male,group E,some high school,free/reduced,completed,73,67,59
male,group C,some college,standard,completed,98,86,90
female,group E,bachelor's degree,standard,completed,99,100,100
male,group C,associate's degree,standard,none,74,73,67
male,group E,some college,standard,none,68,60,59
male,group D,associate's degree,free/reduced,none,53,54,48
male,group D,associate's degree,standard,completed,87,84,85
male,group C,high school,standard,none,71,79,71
male,group C,some college,free/reduced,completed,67,74,70
female,group D,some high school,standard,none,73,86,82
male,group D,some high school,standard,completed,76,70,69
female,group A,some high school,free/reduced,none,44,45,45
female,group C,high school,free/reduced,none,35,53,46
male,group C,bachelor's degree,free/reduced,completed,70,75,74
male,group C,some high school,standard,none,75,72,62
female,group E,high school,standard,none,74,76,73
female,group C,some college,standard,none,58,59,66
female,group B,some college,standard,none,79,86,92
male,group D,associate's degree,standard,none,40,52,43
female,group B,high school,free/reduced,none,50,67,63
female,group E,associate's degree,standard,completed,79,88,94
male,group B,some college,free/reduced,completed,59,65,66
female,group B,associate's degree,standard,none,53,58,65
female,group B,some high school,standard,none,41,55,51
female,group B,master's degree,free/reduced,completed,58,76,78
female,group D,some college,free/reduced,completed,59,78,76
male,group D,some college,standard,none,81,82,84
male,group A,some high school,standard,none,53,54,48
male,group D,some college,standard,none,55,58,52
male,group B,some college,standard,none,79,67,67
male,group C,bachelor's degree,standard,none,86,83,86
female,group B,master's degree,free/reduced,completed,52,70,62
male,group A,some high school,free/reduced,none,79,82,73
male,group C,bachelor's degree,standard,completed,71,74,68
male,group B,high school,standard,none,59,58,47
female,group B,high school,free/reduced,none,64,73,71
female,group D,high school,standard,none,67,72,74
female,group C,associate's degree,standard,completed,71,77,77
male,group A,high school,free/reduced,none,48,45,41
female,group A,some college,standard,none,69,84,82
male,group E,some high school,standard,completed,89,84,77
female,group A,some college,standard,none,56,58,64
male,group B,some college,standard,completed,62,66,68
female,group E,some high school,free/reduced,none,38,49,45
male,group C,some college,standard,none,84,87,81
male,group E,some college,standard,none,68,72,65
male,group C,associate's degree,standard,completed,78,77,77
male,group E,bachelor's degree,standard,completed,85,66,71
female,group B,some college,free/reduced,none,61,68,66
female,group C,some high school,standard,none,69,75,78
female,group C,high school,free/reduced,none,41,46,43
female,group D,some college,free/reduced,completed,52,59,65
female,group C,some high school,free/reduced,none,55,65,62
female,group D,some high school,standard,completed,97,100,100
female,group A,some college,standard,completed,78,87,91
male,group D,some college,standard,none,44,54,53
male,group A,associate's degree,standard,none,63,61,61
female,group C,some college,free/reduced,completed,63,73,71
female,group E,master's degree,free/reduced,none,81,86,87
male,group C,high school,free/reduced,none,58,61,52
female,group C,high school,standard,none,61,72,70
male,group B,bachelor's degree,free/reduced,completed,87,90,88
female,group B,high school,standard,completed,77,82,89
female,group B,associate's degree,standard,none,57,69,68
male,group D,some college,standard,none,67,64,70
male,group C,associate's degree,free/reduced,completed,43,45,50
female,group B,associate's degree,free/reduced,none,53,70,70
male,group B,associate's degree,free/reduced,none,61,58,56
male,group C,high school,free/reduced,completed,58,51,52
female,group B,some high school,standard,none,37,46,46
female,group D,some high school,free/reduced,completed,40,65,64
male,group C,some high school,standard,none,73,66,66
male,group D,bachelor's degree,standard,none,54,49,47
male,group B,associate's degree,free/reduced,none,44,41,38
female,group B,associate's degree,free/reduced,completed,68,77,80
male,group D,some college,free/reduced,none,69,66,60
male,group B,some high school,free/reduced,none,48,52,45
male,group C,some college,standard,none,58,49,42
male,group D,bachelor's degree,free/reduced,none,63,66,67
female,group C,associate's degree,free/reduced,none,60,75,74
female,group D,bachelor's degree,standard,none,78,82,79
male,group A,some high school,free/reduced,completed,61,62,61
male,group D,some high school,free/reduced,none,62,49,52
male,group C,high school,standard,none,62,67,58
male,group A,some high school,standard,none,71,62,50
male,group B,some high school,standard,none,72,68,67
female,group B,bachelor's degree,free/reduced,none,75,85,82
female,group D,some high school,standard,none,59,67,61
female,group D,associate's degree,standard,none,77,77,73
male,group D,associate's degree,standard,none,52,55,49
female,group C,some college,standard,completed,71,71,80
female,group C,bachelor's degree,standard,completed,52,61,66
female,group D,some high school,standard,none,73,84,85
female,group D,associate's degree,standard,completed,88,92,95
female,group A,associate's degree,standard,completed,55,65,62
male,group E,associate's degree,standard,none,87,74,76
male,group D,associate's degree,standard,none,61,55,52
female,group D,some college,free/reduced,none,77,86,86
male,group B,some college,standard,none,58,50,45
male,group C,associate's degree,standard,none,92,79,84
female,group E,high school,standard,none,99,93,90
female,group B,associate's degree,standard,none,73,83,76
female,group B,some college,standard,completed,50,64,66
female,group C,associate's degree,standard,completed,74,75,83
female,group C,high school,standard,none,61,73,63
male,group A,some high school,standard,completed,66,68,64
male,group E,associate's degree,free/reduced,completed,100,100,93
male,group E,some college,standard,none,83,80,73
female,group E,some high school,free/reduced,none,72,79,77
male,group E,some college,standard,none,53,55,48
female,group C,associate's degree,standard,none,46,58,57
female,group D,high school,free/reduced,completed,65,61,71
female,group E,some college,free/reduced,completed,42,55,54
female,group C,associate's degree,standard,completed,83,85,90
male,group D,some high school,standard,none,60,59,54
male,group D,some college,standard,completed,100,97,99
female,group C,high school,free/reduced,completed,67,79,84
female,group C,associate's degree,free/reduced,none,54,58,61
male,group B,bachelor's degree,standard,none,59,54,51
female,group B,high school,standard,none,48,62,60
male,group C,high school,standard,none,90,75,69
female,group B,associate's degree,standard,none,82,80,77
female,group D,high school,standard,none,51,66,62
female,group C,high school,free/reduced,none,35,61,54
female,group D,associate's degree,free/reduced,completed,75,90,88
female,group C,master's degree,standard,completed,81,91,87
male,group C,associate's degree,standard,none,85,76,71
female,group D,some high school,free/reduced,completed,69,86,81
female,group B,bachelor's degree,free/reduced,none,77,85,87
male,group C,associate's degree,free/reduced,none,58,55,53
male,group B,high school,standard,completed,52,49,46
male,group D,some high school,standard,none,62,67,61
female,group B,some high school,standard,none,67,89,82
female,group E,some college,standard,none,76,78,80
male,group D,bachelor's degree,free/reduced,none,68,68,67
female,group C,associate's degree,standard,completed,59,73,72
female,group B,some high school,free/reduced,none,18,32,28
male,group D,some college,standard,completed,65,77,74
female,group C,some college,standard,none,71,81,80
female,group E,some college,standard,none,62,73,70
male,group D,some high school,standard,none,69,66,61
male,group D,some college,standard,none,72,57,58
female,group E,associate's degree,standard,none,66,65,69
male,group C,high school,standard,none,84,77,74
female,group E,bachelor's degree,standard,none,37,45,38
female,group C,associate's degree,standard,none,85,84,82
male,group C,master's degree,free/reduced,completed,62,68,75
male,group D,some high school,free/reduced,none,56,54,52
male,group B,some college,standard,completed,69,77,77
female,group D,some college,standard,none,98,100,99
male,group C,high school,standard,none,50,48,42
female,group E,master's degree,standard,completed,94,99,100
female,group C,associate's degree,standard,none,91,95,94
female,group E,some college,standard,completed,66,74,73
female,group C,some high school,standard,none,74,75,82
male,group B,associate's degree,standard,none,65,54,57
male,group E,bachelor's degree,standard,completed,70,64,70
male,group B,some college,free/reduced,none,60,60,60
female,group A,high school,standard,none,61,68,63
male,group E,some high school,standard,none,94,88,78
male,group C,high school,standard,none,88,89,86
male,group A,some high school,standard,none,64,50,43
female,group D,associate's degree,free/reduced,completed,57,74,76
male,group C,some high school,standard,completed,78,72,69
male,group C,master's degree,free/reduced,completed,72,66,72
female,group C,some high school,standard,completed,76,87,85
female,group E,some high school,free/reduced,none,74,74,72
male,group B,high school,standard,completed,73,71,68
female,group D,some college,free/reduced,completed,70,78,78
female,group C,high school,standard,none,76,76,74
male,group C,some high school,standard,none,57,61,54
female,group E,master's degree,free/reduced,none,45,56,54
male,group B,some college,standard,none,69,54,55
female,group C,some college,standard,none,62,69,69
male,group D,associate's degree,free/reduced,none,75,66,73
female,group D,some college,standard,completed,75,77,83
male,group C,some college,standard,none,59,60,58
female,group C,some college,standard,completed,88,95,94
female,group D,some high school,free/reduced,none,50,64,59
female,group D,some college,standard,none,62,70,72
female,group D,bachelor's degree,standard,none,59,70,73
male,group C,some college,standard,none,91,74,76
male,group C,some college,standard,none,63,63,60
male,group C,master's degree,standard,none,71,67,67
female,group B,some high school,free/reduced,completed,59,63,64
male,group C,some high school,standard,none,64,58,51
female,group C,master's degree,standard,completed,69,84,85
male,group C,some high school,standard,none,62,64,55
male,group C,associate's degree,standard,none,97,93,91
female,group E,associate's degree,standard,completed,95,89,92
female,group B,bachelor's degree,standard,none,75,84,80
female,group A,some college,free/reduced,none,61,60,57
female,group D,master's degree,standard,none,53,61,68
female,group E,associate's degree,standard,none,68,76,67
male,group B,master's degree,free/reduced,none,49,53,52
female,group C,bachelor's degree,free/reduced,none,67,75,72
female,group B,associate's degree,standard,completed,59,70,66
male,group C,some high school,standard,completed,76,80,73
female,group D,bachelor's degree,free/reduced,none,62,72,74
female,group E,associate's degree,standard,none,84,95,92
male,group C,high school,standard,none,62,55,49
female,group C,some college,standard,none,72,72,71
male,group A,high school,free/reduced,none,53,58,44
male,group B,high school,standard,completed,60,44,47
female,group D,high school,standard,completed,57,58,64
male,group E,high school,free/reduced,completed,57,56,54
male,group D,some high school,standard,completed,71,69,68
female,group A,high school,standard,none,55,73,73
female,group D,associate's degree,free/reduced,none,46,56,57
female,group C,some college,standard,none,69,78,76
female,group C,some college,standard,none,55,69,65
male,group D,high school,standard,none,88,78,75
male,group A,bachelor's degree,standard,none,77,67,68
female,group D,high school,standard,completed,88,99,100
female,group C,associate's degree,standard,none,54,61,58
male,group E,high school,standard,completed,81,80,76
female,group D,associate's degree,free/reduced,none,43,60,58
male,group B,some college,free/reduced,completed,74,77,76
male,group D,some high school,standard,completed,78,81,86
male,group D,high school,free/reduced,completed,64,64,67
female,group E,high school,free/reduced,none,41,45,40
female,group D,associate's degree,standard,none,74,81,83
female,group C,associate's degree,free/reduced,none,65,77,74
female,group A,high school,standard,completed,68,80,76
male,group D,master's degree,standard,none,80,80,72
male,group B,associate's degree,standard,none,80,76,64
male,group D,high school,standard,none,69,75,71
male,group A,bachelor's degree,standard,none,91,96,92
male,group A,some college,standard,completed,100,96,86
female,group C,some college,standard,completed,87,89,94
female,group E,associate's degree,standard,none,85,92,85
female,group C,some high school,free/reduced,none,44,50,51
male,group D,some college,free/reduced,completed,69,60,63
male,group E,associate's degree,standard,completed,71,74,68
female,group C,bachelor's degree,free/reduced,completed,51,72,79
male,group A,some high school,standard,completed,62,67,69
male,group C,associate's degree,free/reduced,none,68,65,61
male,group D,high school,standard,none,41,52,51
male,group D,high school,free/reduced,none,44,51,48
male,group C,some high school,free/reduced,none,79,76,65
female,group E,associate's degree,standard,completed,93,100,95
male,group B,some high school,standard,completed,64,53,57
male,group C,associate's degree,free/reduced,none,73,68,66
male,group B,some high school,standard,none,88,84,75
female,group C,some college,free/reduced,none,62,72,70
male,group D,some college,free/reduced,none,62,57,62
male,group C,high school,free/reduced,none,61,60,55
male,group D,associate's degree,standard,none,90,87,85
male,group D,high school,free/reduced,none,75,74,66
female,group C,some college,free/reduced,none,77,90,91
female,group C,some college,standard,none,82,90,94
male,group E,high school,standard,none,80,76,65
male,group D,high school,free/reduced,none,63,57,56
male,group E,some high school,standard,none,82,67,61
female,group E,some college,standard,none,61,64,62
male,group A,high school,standard,none,57,43,47
female,group D,high school,standard,none,45,63,59
male,group E,high school,free/reduced,none,55,56,51
female,group B,associate's degree,standard,none,58,63,65
male,group B,bachelor's degree,free/reduced,none,73,56,57
female,group E,bachelor's degree,standard,none,65,73,75
female,group C,some high school,standard,completed,59,54,67
female,group C,some college,standard,completed,88,93,93
female,group D,associate's degree,standard,none,65,69,70
male,group C,associate's degree,standard,none,69,77,69
male,group C,high school,standard,none,70,56,51
male,group E,associate's degree,standard,none,89,76,74
male,group E,high school,standard,none,84,73,69
male,group D,associate's degree,free/reduced,completed,61,71,73
female,group B,high school,standard,none,74,72,72
male,group B,high school,standard,none,57,48,51
female,group C,high school,standard,completed,60,64,74
male,group C,high school,free/reduced,none,54,72,59
female,group A,bachelor's degree,standard,none,51,49,51
female,group D,some high school,standard,completed,80,92,88
female,group A,some college,free/reduced,none,49,65,55
male,group C,bachelor's degree,standard,completed,91,81,79
male,group B,high school,standard,none,52,48,49
male,group C,master's degree,standard,none,67,57,59
female,group C,bachelor's degree,free/reduced,completed,47,62,66
male,group B,some high school,standard,completed,61,56,56
female,group D,associate's degree,free/reduced,completed,74,88,90
female,group E,some college,standard,none,68,70,66
male,group C,master's degree,free/reduced,completed,79,77,75
female,group D,some college,free/reduced,none,64,74,75
male,group B,some college,standard,completed,91,96,91
female,group E,bachelor's degree,free/reduced,none,61,58,62
female,group C,bachelor's degree,free/reduced,none,43,62,61
female,group C,high school,free/reduced,none,53,72,64
female,group E,bachelor's degree,standard,none,64,73,70
female,group A,high school,free/reduced,completed,53,50,60
female,group C,bachelor's degree,standard,none,86,92,87
female,group D,high school,standard,none,69,72,77
female,group C,some high school,standard,none,77,91,88
female,group D,high school,standard,none,78,81,80
female,group C,some college,standard,none,54,48,52
male,group A,associate's degree,standard,none,54,53,47
female,group E,associate's degree,free/reduced,none,73,76,78
female,group B,bachelor's degree,standard,none,67,86,83
male,group C,associate's degree,free/reduced,none,49,51,51
female,group C,master's degree,free/reduced,none,40,58,54
male,group D,associate's degree,free/reduced,none,52,57,50
female,group D,some college,standard,completed,82,97,96
male,group D,some high school,standard,none,81,78,78
female,group B,high school,free/reduced,completed,23,44,36
male,group E,some high school,standard,none,92,87,78
female,group B,some high school,standard,completed,32,51,44
female,group E,some college,standard,completed,73,78,76
male,group C,associate's degree,standard,none,83,72,78
female,group B,high school,standard,none,50,53,55
female,group D,master's degree,standard,completed,70,71,74
male,group D,associate's degree,standard,completed,67,54,63
female,group D,associate's degree,free/reduced,completed,42,61,58
male,group D,some college,free/reduced,none,59,62,61
female,group B,some college,standard,none,70,75,78
male,group B,some college,free/reduced,none,55,55,47
male,group D,associate's degree,standard,none,61,48,46
female,group B,bachelor's degree,standard,completed,66,74,81
female,group D,bachelor's degree,free/reduced,none,73,79,84
female,group D,some high school,standard,none,80,90,82
female,group A,some high school,free/reduced,none,38,43,43
female,group B,associate's degree,standard,completed,52,66,73
male,group C,high school,standard,completed,58,52,54
female,group C,high school,standard,none,72,80,83
female,group C,associate's degree,standard,completed,68,86,84
female,group C,bachelor's degree,standard,completed,77,94,95
female,group B,some high school,standard,none,82,82,80
female,group D,associate's degree,standard,none,76,74,73
male,group E,some high school,standard,completed,81,75,76
male,group E,associate's degree,free/reduced,completed,46,43,44
male,group D,some college,standard,none,88,77,77
male,group C,associate's degree,free/reduced,completed,65,73,68
female,group B,bachelor's degree,standard,none,97,97,96
female,group B,some college,standard,none,82,85,87
female,group B,bachelor's degree,standard,completed,65,81,81
male,group C,master's degree,standard,completed,91,85,85
female,group C,associate's degree,standard,completed,55,72,79
female,group D,master's degree,standard,none,92,100,100
female,group B,high school,standard,none,81,91,89
female,group E,associate's degree,free/reduced,completed,57,68,73
female,group C,some college,standard,none,73,80,82
female,group D,high school,standard,none,56,52,55
female,group D,associate's degree,standard,completed,57,78,79
male,group D,associate's degree,free/reduced,none,66,62,64
male,group C,high school,standard,completed,53,52,49
male,group E,associate's degree,standard,completed,81,81,79
male,group C,high school,standard,completed,75,69,68
male,group A,high school,standard,completed,72,73,74
female,group B,some high school,standard,none,73,79,79
female,group E,some college,standard,completed,86,85,91
female,group C,bachelor's degree,standard,none,65,79,81
male,group D,high school,standard,none,64,54,50
female,group B,high school,standard,none,58,68,61
male,group D,some high school,standard,none,55,47,44
male,group C,associate's degree,free/reduced,completed,78,81,82
female,group D,some college,free/reduced,completed,63,80,80
male,group D,high school,free/reduced,completed,73,68,66
female,group C,high school,standard,none,81,84,82
female,group E,high school,standard,none,74,81,71
female,group C,associate's degree,standard,none,49,53,53
male,group C,bachelor's degree,free/reduced,none,53,58,55
male,group D,some college,free/reduced,none,77,62,64
female,group D,some college,free/reduced,none,69,65,74
male,group E,bachelor's degree,standard,none,82,62,62
male,group E,some college,standard,none,76,67,67
female,group B,high school,standard,none,42,52,51
female,group C,associate's degree,standard,none,85,89,95
female,group C,high school,standard,completed,58,75,77
female,group C,high school,standard,none,59,72,68
female,group C,high school,free/reduced,none,34,42,39
male,group C,some college,standard,none,76,78,75
female,group D,some high school,standard,none,68,71,75
female,group B,some high school,free/reduced,none,72,81,79
female,group C,some high school,free/reduced,none,48,56,51
male,group C,bachelor's degree,standard,completed,94,90,91
male,group D,associate's degree,standard,none,81,71,73
female,group A,some high school,standard,completed,92,100,97
male,group E,some college,standard,completed,81,74,71
female,group C,some high school,free/reduced,completed,29,40,44
female,group D,some college,free/reduced,none,58,67,62
female,group C,some college,standard,none,73,76,78
male,group E,some high school,standard,completed,68,51,57
female,group C,high school,free/reduced,completed,50,66,64
male,group B,associate's degree,standard,completed,65,65,63
male,group C,some college,free/reduced,none,63,61,54
female,group C,high school,standard,none,66,71,76
female,group E,master's degree,free/reduced,none,56,72,65
male,group E,associate's degree,standard,completed,94,85,82
female,group C,associate's degree,standard,none,66,77,73
female,group C,associate's degree,standard,completed,67,84,86
male,group D,bachelor's degree,free/reduced,completed,74,79,75
female,group C,bachelor's degree,standard,none,67,69,75
male,group C,bachelor's degree,standard,completed,63,64,66
male,group D,some college,standard,none,76,64,66
male,group A,associate's degree,free/reduced,completed,79,82,82
female,group B,some high school,free/reduced,completed,52,67,72
female,group A,some high school,standard,none,71,83,77
male,group B,bachelor's degree,free/reduced,none,88,75,76
male,group D,some college,standard,none,68,59,62
female,group D,high school,standard,completed,69,77,78
female,group D,some college,standard,none,77,68,77
male,group E,bachelor's degree,standard,none,68,68,64
female,group B,some high school,standard,none,66,69,68
female,group C,associate's degree,standard,none,59,66,67
male,group A,associate's degree,free/reduced,none,62,61,55
female,group C,high school,standard,none,63,69,74
female,group E,high school,free/reduced,none,64,62,68
male,group D,master's degree,standard,none,82,82,74
male,group B,some college,free/reduced,completed,60,62,60
male,group D,some college,standard,none,71,49,52
male,group B,associate's degree,free/reduced,completed,58,57,53
female,group E,associate's degree,standard,none,100,100,100
female,group D,some high school,standard,none,59,58,59
female,group C,master's degree,standard,completed,54,64,67
female,group A,master's degree,standard,none,50,53,58
female,group E,high school,free/reduced,completed,66,74,78
male,group C,associate's degree,free/reduced,none,55,61,54
female,group C,some college,standard,none,83,83,90
male,group A,bachelor's degree,standard,none,66,64,62
male,group D,some high school,standard,completed,62,66,68
female,group B,high school,standard,none,62,62,63
female,group E,associate's degree,free/reduced,completed,83,86,88
female,group D,some college,free/reduced,none,60,66,70
male,group C,some college,standard,none,53,44,42
female,group D,some high school,standard,none,59,72,80
male,group C,associate's degree,standard,none,49,51,43
female,group C,bachelor's degree,free/reduced,none,50,60,59
male,group E,associate's degree,free/reduced,completed,91,73,80
male,group B,some college,standard,none,47,43,41
male,group B,associate's degree,free/reduced,none,67,62,60
female,group B,some high school,standard,none,57,67,72
female,group D,some college,free/reduced,none,71,83,83
female,group E,associate's degree,standard,completed,65,75,77
male,group B,some college,free/reduced,none,54,54,45
male,group C,bachelor's degree,free/reduced,none,37,56,47
male,group C,high school,free/reduced,none,62,55,55
male,group B,some high school,standard,completed,94,86,87
male,group D,bachelor's degree,free/reduced,completed,39,42,38
female,group E,some college,free/reduced,none,71,76,70
female,group D,some college,free/reduced,none,65,81,77
female,group E,some college,free/reduced,completed,75,88,85
female,group C,some college,free/reduced,none,32,39,33
male,group C,some college,standard,none,53,39,37
male,group A,some college,standard,none,53,43,43
male,group A,bachelor's degree,standard,completed,87,84,87
male,group E,bachelor's degree,standard,completed,76,62,66
female,group D,bachelor's degree,free/reduced,none,78,90,93
male,group D,bachelor's degree,standard,none,75,73,74
female,group C,some college,standard,none,58,67,72
male,group B,associate's degree,standard,none,48,43,45
male,group D,master's degree,standard,none,73,70,75
female,group C,some college,standard,completed,69,90,88
female,group E,high school,free/reduced,none,57,58,57
male,group B,some high school,standard,completed,79,85,86
female,group C,some college,standard,none,63,74,74
female,group B,associate's degree,standard,none,47,49,50
male,group D,some high school,standard,completed,74,71,78
male,group E,some college,standard,none,97,87,82
female,group B,some high school,free/reduced,none,49,58,55
male,group C,master's degree,standard,none,79,78,77
male,group C,some high school,free/reduced,none,69,71,65
female,group C,associate's degree,free/reduced,none,53,61,62
male,group C,high school,standard,completed,69,58,53
male,group C,high school,free/reduced,none,27,34,36
female,group D,some high school,free/reduced,completed,35,55,60
female,group B,some high school,free/reduced,completed,63,78,79
male,group B,bachelor's degree,free/reduced,none,48,51,46
female,group C,high school,standard,none,72,80,75
female,group B,high school,standard,none,66,72,70
female,group E,bachelor's degree,standard,none,80,83,83
male,group A,some college,standard,completed,78,72,70
male,group C,high school,standard,none,71,66,65
female,group D,master's degree,standard,none,54,60,63
female,group C,associate's degree,free/reduced,none,57,78,67
female,group D,some college,standard,none,65,70,71
male,group C,high school,free/reduced,completed,53,51,51
female,group D,high school,free/reduced,none,39,52,46
female,group D,associate's degree,free/reduced,none,55,76,76
female,group D,associate's degree,standard,none,59,70,65
female,group B,high school,free/reduced,none,60,72,68
female,group B,associate's degree,standard,none,49,52,54
female,group B,high school,free/reduced,none,8,24,23
female,group D,master's degree,free/reduced,none,40,59,54
female,group C,bachelor's degree,free/reduced,completed,74,86,89
male,group E,some college,standard,none,59,51,43
female,group E,bachelor's degree,free/reduced,completed,92,100,100
male,group C,some college,free/reduced,none,80,64,66
male,group C,bachelor's degree,standard,completed,96,90,92
male,group E,some college,standard,completed,85,75,68
female,group C,bachelor's degree,standard,none,77,88,87
female,group B,high school,free/reduced,completed,76,85,82
male,group C,high school,free/reduced,none,66,66,59
female,group D,bachelor's degree,standard,completed,71,76,83
male,group B,high school,standard,none,60,68,60
male,group D,some college,standard,none,76,71,73
male,group D,some college,standard,completed,58,59,58
female,group B,associate's degree,standard,completed,90,90,91
female,group D,some college,standard,completed,74,75,79
male,group B,some college,free/reduced,none,75,68,65
male,group C,some college,standard,none,69,64,68
female,group B,some high school,standard,completed,60,70,70
female,group B,some college,free/reduced,completed,65,75,70
female,group C,associate's degree,free/reduced,completed,68,67,69
male,group B,high school,standard,completed,72,65,68
male,group B,associate's degree,free/reduced,completed,82,78,74
female,group C,some high school,standard,completed,85,92,93
male,group E,associate's degree,standard,none,72,57,62
male,group D,some college,standard,completed,76,83,79
female,group E,some college,standard,none,67,76,75
male,group A,some college,free/reduced,none,75,81,74
male,group B,some high school,standard,completed,63,67,67
female,group C,associate's degree,standard,none,64,64,70
male,group D,associate's degree,standard,completed,67,72,67
male,group A,some college,free/reduced,none,58,60,57
female,group B,associate's degree,free/reduced,none,53,71,67
male,group C,some high school,standard,none,73,66,63
male,group D,master's degree,standard,none,89,84,82
female,group C,high school,standard,none,65,69,67
female,group C,some college,standard,completed,70,72,76
female,group D,bachelor's degree,standard,none,65,67,62
male,group D,some high school,standard,none,74,74,72
female,group D,associate's degree,standard,none,71,71,74
female,group E,bachelor's degree,standard,none,100,100,100
male,group C,high school,standard,none,71,60,61
male,group E,high school,standard,completed,87,91,81
female,group D,associate's degree,free/reduced,none,26,31,38
male,group B,associate's degree,standard,completed,91,89,92
female,group A,associate's degree,standard,none,82,93,93
male,group D,high school,standard,none,66,69,63
female,group E,bachelor's degree,standard,completed,79,81,82
male,group D,some college,standard,completed,63,55,63
female,group D,master's degree,standard,none,87,100,100
male,group C,bachelor's degree,standard,none,69,63,61
female,group C,associate's degree,standard,none,53,62,53
male,group C,some college,free/reduced,completed,50,48,53
female,group D,associate's degree,standard,none,85,91,89
```

## File: `catboost_info/catboost_training.json`
```json
{
"meta":{"test_sets":[],"test_metrics":[],"learn_metrics":[{"best_value":"Min","name":"RMSE"}],"launch_mode":"Train","parameters":"","iteration_count":100,"learn_sets":["learn"],"name":"experiment"},
"iterations":[
{"learn":[14.84063055],"iteration":0,"passed_time":0.0005725027525,"remaining_time":0.0566777725},
{"learn":[14.0277146],"iteration":1,"passed_time":0.001078311337,"remaining_time":0.05283725553},
{"learn":[13.28168108],"iteration":2,"passed_time":0.001542116958,"remaining_time":0.04986178166},
{"learn":[12.67295736],"iteration":3,"passed_time":0.001974468832,"remaining_time":0.04738725197},
{"learn":[12.13118282],"iteration":4,"passed_time":0.002499736343,"remaining_time":0.04749499052},
{"learn":[11.64284615],"iteration":5,"passed_time":0.003177419316,"remaining_time":0.04977956928},
{"learn":[11.17583451],"iteration":6,"passed_time":0.003660929653,"remaining_time":0.04863806539},
{"learn":[10.70698042],"iteration":7,"passed_time":0.004134578984,"remaining_time":0.04754765831},
{"learn":[10.30261074],"iteration":8,"passed_time":0.004600830967,"remaining_time":0.04651951311},
{"learn":[9.897928797],"iteration":9,"passed_time":0.005068756745,"remaining_time":0.0456188107},
{"learn":[9.43818595],"iteration":10,"passed_time":0.00550877421,"remaining_time":0.04457099134},
{"learn":[9.067087678],"iteration":11,"passed_time":0.005975359678,"remaining_time":0.0438193043},
{"learn":[8.769647814],"iteration":12,"passed_time":0.006476589299,"remaining_time":0.04334332839},
{"learn":[8.494260327],"iteration":13,"passed_time":0.006986012504,"remaining_time":0.04291407681},
{"learn":[8.18170444],"iteration":14,"passed_time":0.007435374211,"remaining_time":0.04213378719},
{"learn":[7.872819124],"iteration":15,"passed_time":0.007934438155,"remaining_time":0.04165580031},
{"learn":[7.637017332],"iteration":16,"passed_time":0.008394759637,"remaining_time":0.0409861794},
{"learn":[7.415872705],"iteration":17,"passed_time":0.008891902177,"remaining_time":0.04050755436},
{"learn":[7.161020449],"iteration":18,"passed_time":0.009343504207,"remaining_time":0.03983283373},
{"learn":[6.971236341],"iteration":19,"passed_time":0.009773481938,"remaining_time":0.03909392775},
{"learn":[6.841615556],"iteration":20,"passed_time":0.0102961808,"remaining_time":0.03873325158},
{"learn":[6.687931434],"iteration":21,"passed_time":0.01084692877,"remaining_time":0.03845729292},
{"learn":[6.508058838],"iteration":22,"passed_time":0.01128401801,"remaining_time":0.03777692985},
{"learn":[6.348045518],"iteration":23,"passed_time":0.01184822067,"remaining_time":0.03751936544},
{"learn":[6.190854657],"iteration":24,"passed_time":0.01232796527,"remaining_time":0.03698389581},
{"learn":[6.083848414],"iteration":25,"passed_time":0.01280227884,"remaining_time":0.03643725515},
{"learn":[5.948861607],"iteration":26,"passed_time":0.01325531889,"remaining_time":0.03583845477},
{"learn":[5.820594273],"iteration":27,"passed_time":0.01373480465,"remaining_time":0.0353180691},
{"learn":[5.718358733],"iteration":28,"passed_time":0.0142543829,"remaining_time":0.03489866158},
{"learn":[5.62831756],"iteration":29,"passed_time":0.0147020259,"remaining_time":0.0343047271},
{"learn":[5.501668539],"iteration":30,"passed_time":0.01518440591,"remaining_time":0.03379754864},
{"learn":[5.404367962],"iteration":31,"passed_time":0.01564985073,"remaining_time":0.03325593281},
{"learn":[5.312889065],"iteration":32,"passed_time":0.0161892921,"remaining_time":0.0328691688},
{"learn":[5.220401854],"iteration":33,"passed_time":0.01671813023,"remaining_time":0.03245284103},
{"learn":[5.130160358],"iteration":34,"passed_time":0.01719500759,"remaining_time":0.03193358553},
{"learn":[5.056241699],"iteration":35,"passed_time":0.01766281836,"remaining_time":0.03140056598},
{"learn":[4.971821431],"iteration":36,"passed_time":0.01809684949,"remaining_time":0.03081355454},
{"learn":[4.90630594],"iteration":37,"passed_time":0.01857493881,"remaining_time":0.03030647911},
{"learn":[4.847558899],"iteration":38,"passed_time":0.0190151347,"remaining_time":0.02974162094},
{"learn":[4.795388439],"iteration":39,"passed_time":0.01945923409,"remaining_time":0.02918885113},
{"learn":[4.763423781],"iteration":40,"passed_time":0.01993290982,"remaining_time":0.0286839434},
{"learn":[4.718909606],"iteration":41,"passed_time":0.02039454643,"remaining_time":0.02816389745},
{"learn":[4.660496339],"iteration":42,"passed_time":0.02090872368,"remaining_time":0.02771621511},
{"learn":[4.619083415],"iteration":43,"passed_time":0.0213830327,"remaining_time":0.02721476889},
{"learn":[4.578792627],"iteration":44,"passed_time":0.02187593401,"remaining_time":0.02673725268},
{"learn":[4.53420217],"iteration":45,"passed_time":0.0224436205,"remaining_time":0.02634685885},
{"learn":[4.480755407],"iteration":46,"passed_time":0.02293770099,"remaining_time":0.02586591814},
{"learn":[4.440459443],"iteration":47,"passed_time":0.02343692971,"remaining_time":0.02539000718},
{"learn":[4.399489675],"iteration":48,"passed_time":0.02398921826,"remaining_time":0.02496837003},
{"learn":[4.351777663],"iteration":49,"passed_time":0.02446975516,"remaining_time":0.02446975516},
{"learn":[4.322290972],"iteration":50,"passed_time":0.02497672654,"remaining_time":0.02399724706},
{"learn":[4.294233013],"iteration":51,"passed_time":0.02548184691,"remaining_time":0.02352170484},
{"learn":[4.275623532],"iteration":52,"passed_time":0.02606073108,"remaining_time":0.02311045964},
{"learn":[4.237862852],"iteration":53,"passed_time":0.02651882772,"remaining_time":0.0225901125},
{"learn":[4.20766476],"iteration":54,"passed_time":0.02697740865,"remaining_time":0.02207242526},
{"learn":[4.188319833],"iteration":55,"passed_time":0.02743283983,"remaining_time":0.02155437415},
{"learn":[4.150006672],"iteration":56,"passed_time":0.02791423213,"remaining_time":0.02105810494},
{"learn":[4.109226526],"iteration":57,"passed_time":0.02839133253,"remaining_time":0.0205592408},
{"learn":[4.077151393],"iteration":58,"passed_time":0.02890729039,"remaining_time":0.02008811705},
{"learn":[4.043789762],"iteration":59,"passed_time":0.0293752019,"remaining_time":0.01958346794},
{"learn":[4.035036878],"iteration":60,"passed_time":0.02980697572,"remaining_time":0.0190569189},
{"learn":[4.013853126],"iteration":61,"passed_time":0.03030495121,"remaining_time":0.01857400235},
{"learn":[3.979587038],"iteration":62,"passed_time":0.03075632262,"remaining_time":0.0180632371},
{"learn":[3.950449041],"iteration":63,"passed_time":0.0312935003,"remaining_time":0.01760259392},
{"learn":[3.941048557],"iteration":64,"passed_time":0.03166809897,"remaining_time":0.01705205329},
{"learn":[3.919502044],"iteration":65,"passed_time":0.03220422945,"remaining_time":0.0165900576},
{"learn":[3.908419086],"iteration":66,"passed_time":0.03264244325,"remaining_time":0.0160776213},
{"learn":[3.883974731],"iteration":67,"passed_time":0.03309432779,"remaining_time":0.01557380131},
{"learn":[3.862579573],"iteration":68,"passed_time":0.03361098327,"remaining_time":0.01510058669},
{"learn":[3.849836895],"iteration":69,"passed_time":0.03408590888,"remaining_time":0.01460824666},
{"learn":[3.824998864],"iteration":70,"passed_time":0.03457868547,"remaining_time":0.01412368843},
{"learn":[3.791315502],"iteration":71,"passed_time":0.03504161141,"remaining_time":0.01362729333},
{"learn":[3.758805858],"iteration":72,"passed_time":0.03550159547,"remaining_time":0.01313072709},
{"learn":[3.739757196],"iteration":73,"passed_time":0.03603040325,"remaining_time":0.01265933087},
{"learn":[3.727492189],"iteration":74,"passed_time":0.03649202712,"remaining_time":0.01216400904},
{"learn":[3.706251604],"iteration":75,"passed_time":0.03698083679,"remaining_time":0.01167815899},
{"learn":[3.685860196],"iteration":76,"passed_time":0.03741927574,"remaining_time":0.01117718626},
{"learn":[3.663779561],"iteration":77,"passed_time":0.03788451635,"remaining_time":0.01068537641},
{"learn":[3.648059878],"iteration":78,"passed_time":0.03832493436,"remaining_time":0.01018764078},
{"learn":[3.643276906],"iteration":79,"passed_time":0.03879007119,"remaining_time":0.009697517797},
{"learn":[3.638022193],"iteration":80,"passed_time":0.03928673064,"remaining_time":0.009215405954},
{"learn":[3.625433746],"iteration":81,"passed_time":0.03980591563,"remaining_time":0.008737883919},
{"learn":[3.596253585],"iteration":82,"passed_time":0.04034440964,"remaining_time":0.008263312818},
{"learn":[3.571081695],"iteration":83,"passed_time":0.04077575044,"remaining_time":0.007766809607},
{"learn":[3.56195045],"iteration":84,"passed_time":0.04123372964,"remaining_time":0.007276540525},
{"learn":[3.518241793],"iteration":85,"passed_time":0.04171046469,"remaining_time":0.006790075647},
{"learn":[3.494336727],"iteration":86,"passed_time":0.04219215376,"remaining_time":0.006304574699},
{"learn":[3.478022077],"iteration":87,"passed_time":0.04268743255,"remaining_time":0.005821013529},
{"learn":[3.450668514],"iteration":88,"passed_time":0.04315590574,"remaining_time":0.00533387599},
{"learn":[3.419074933],"iteration":89,"passed_time":0.04359971989,"remaining_time":0.004844413321},
{"learn":[3.376901598],"iteration":90,"passed_time":0.04412376695,"remaining_time":0.004363889039},
{"learn":[3.365852239],"iteration":91,"passed_time":0.04457742784,"remaining_time":0.003876298073},
{"learn":[3.34189864],"iteration":92,"passed_time":0.04515220885,"remaining_time":0.003398553354},
{"learn":[3.320205229],"iteration":93,"passed_time":0.04561902645,"remaining_time":0.002911852752},
{"learn":[3.307646434],"iteration":94,"passed_time":0.04609856411,"remaining_time":0.002426240216},
{"learn":[3.304337773],"iteration":95,"passed_time":0.04662216389,"remaining_time":0.001942590162},
{"learn":[3.28404604],"iteration":96,"passed_time":0.04705139454,"remaining_time":0.001455197769},
{"learn":[3.262609827],"iteration":97,"passed_time":0.04751483118,"remaining_time":0.0009696904322},
{"learn":[3.252134778],"iteration":98,"passed_time":0.04798855455,"remaining_time":0.0004847328742},
{"learn":[3.245174796],"iteration":99,"passed_time":0.04854740143,"remaining_time":0}
]}
```

## File: `catboost_info/learn_error.tsv`
```
iter	RMSE
0	14.84063055
1	14.0277146
2	13.28168108
3	12.67295736
4	12.13118282
5	11.64284615
6	11.17583451
7	10.70698042
8	10.30261074
9	9.897928797
10	9.43818595
11	9.067087678
12	8.769647814
13	8.494260327
14	8.18170444
15	7.872819124
16	7.637017332
17	7.415872705
18	7.161020449
19	6.971236341
20	6.841615556
21	6.687931434
22	6.508058838
23	6.348045518
24	6.190854657
25	6.083848414
26	5.948861607
27	5.820594273
28	5.718358733
29	5.62831756
30	5.501668539
31	5.404367962
32	5.312889065
33	5.220401854
34	5.130160358
35	5.056241699
36	4.971821431
37	4.90630594
38	4.847558899
39	4.795388439
40	4.763423781
41	4.718909606
42	4.660496339
43	4.619083415
44	4.578792627
45	4.53420217
46	4.480755407
47	4.440459443
48	4.399489675
49	4.351777663
50	4.322290972
51	4.294233013
52	4.275623532
53	4.237862852
54	4.20766476
55	4.188319833
56	4.150006672
57	4.109226526
58	4.077151393
59	4.043789762
60	4.035036878
61	4.013853126
62	3.979587038
63	3.950449041
64	3.941048557
65	3.919502044
66	3.908419086
67	3.883974731
68	3.862579573
69	3.849836895
70	3.824998864
71	3.791315502
72	3.758805858
73	3.739757196
74	3.727492189
75	3.706251604
76	3.685860196
77	3.663779561
78	3.648059878
79	3.643276906
80	3.638022193
81	3.625433746
82	3.596253585
83	3.571081695
84	3.56195045
85	3.518241793
86	3.494336727
87	3.478022077
88	3.450668514
89	3.419074933
90	3.376901598
91	3.365852239
92	3.34189864
93	3.320205229
94	3.307646434
95	3.304337773
96	3.28404604
97	3.262609827
98	3.252134778
99	3.245174796
```

## File: `catboost_info/time_left.tsv`
```
iter	Passed	Remaining
0	0	56
1	1	52
2	1	49
3	1	47
4	2	47
5	3	49
6	3	48
7	4	47
8	4	46
9	5	45
10	5	44
11	5	43
12	6	43
13	6	42
14	7	42
15	7	41
16	8	40
17	8	40
18	9	39
19	9	39
20	10	38
21	10	38
22	11	37
23	11	37
24	12	36
25	12	36
26	13	35
27	13	35
28	14	34
29	14	34
30	15	33
31	15	33
32	16	32
33	16	32
34	17	31
35	17	31
36	18	30
37	18	30
38	19	29
39	19	29
40	19	28
41	20	28
42	20	27
43	21	27
44	21	26
45	22	26
46	22	25
47	23	25
48	23	24
49	24	24
50	24	23
51	25	23
52	26	23
53	26	22
54	26	22
55	27	21
56	27	21
57	28	20
58	28	20
59	29	19
60	29	19
61	30	18
62	30	18
63	31	17
64	31	17
65	32	16
66	32	16
67	33	15
68	33	15
69	34	14
70	34	14
71	35	13
72	35	13
73	36	12
74	36	12
75	36	11
76	37	11
77	37	10
78	38	10
79	38	9
80	39	9
81	39	8
82	40	8
83	40	7
84	41	7
85	41	6
86	42	6
87	42	5
88	43	5
89	43	4
90	44	4
91	44	3
92	45	3
93	45	2
94	46	2
95	46	1
96	47	1
97	47	0
98	47	0
99	48	0
```

## File: `Notebook_Experiments/Exploratory_Data_Analysis.ipynb`
```
{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "1e233234",
   "metadata": {},
   "source": [
    "## Student Performance Indicator\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62e05101",
   "metadata": {},
   "source": [
    "#### Life cycle of Machine learning Project\n",
    "\n",
    "- Understanding the Problem Statement\n",
    "- Data Collection\n",
    "- Data Checks to perform\n",
    "- Exploratory data analysis\n",
    "- Data Pre-Processing\n",
    "- Model Training\n",
    "- Choose best model"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dfcea981",
   "metadata": {},
   "source": [
    "### 1) Problem statement\n",
    "- This project understands how the student's performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course.\n",
    "\n",
    "\n",
    "### 2) Data Collection\n",
    "- Dataset Source - https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977\n",
    "- The data consists of 8 column and 1000 rows."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "15b1355f",
   "metadata": {},
   "source": [
    "### 2.1 Import Data and Required Packages\n",
    "####  Importing Pandas, Numpy, Matplotlib, Seaborn and Warings Library."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7eaae1d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3caeb0bb",
   "metadata": {},
   "source": [
    "#### Import the CSV Data as Pandas DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "57907087",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('data/stud.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92c8fd8a",
   "metadata": {},
   "source": [
    "#### Show Top 5 Records"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7d1a2a0b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race_ethnicity</th>\n",
       "      <th>parental_level_of_education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test_preparation_course</th>\n",
       "      <th>math_score</th>\n",
       "      <th>reading_score</th>\n",
       "      <th>writing_score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>master's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>male</td>\n",
       "      <td>group A</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>male</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender race_ethnicity parental_level_of_education         lunch  \\\n",
       "0  female        group B           bachelor's degree      standard   \n",
       "1  female        group C                some college      standard   \n",
       "2  female        group B             master's degree      standard   \n",
       "3    male        group A          associate's degree  free/reduced   \n",
       "4    male        group C                some college      standard   \n",
       "\n",
       "  test_preparation_course  math_score  reading_score  writing_score  \n",
       "0                    none          72             72             74  \n",
       "1               completed          69             90             88  \n",
       "2                    none          90             95             93  \n",
       "3                    none          47             57             44  \n",
       "4                    none          76             78             75  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "56a49220",
   "metadata": {},
   "source": [
    "#### Shape of the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "417e5820",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1000, 8)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "041aa39d",
   "metadata": {},
   "source": [
    "### 2.2 Dataset information"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e3cff9d",
   "metadata": {},
   "source": [
    "- gender : sex of students  -> (Male/female)\n",
    "- race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)\n",
    "- parental level of education : parents' final education ->(bachelor's degree,some college,master's degree,associate's degree,high school)\n",
    "- lunch : having lunch before test (standard or free/reduced) \n",
    "- test preparation course : complete or not complete before test\n",
    "- math score\n",
    "- reading score\n",
    "- writing score"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "27c4b61b",
   "metadata": {},
   "source": [
    "### 3. Data Checks to perform\n",
    "\n",
    "- Check Missing values\n",
    "- Check Duplicates\n",
    "- Check data type\n",
    "- Check the number of unique values of each column\n",
    "- Check statistics of data set\n",
    "- Check various categories present in the different categorical column"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c31d4123",
   "metadata": {},
   "source": [
    "### 3.1 Check Missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "707d6a7b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gender                         0\n",
       "race_ethnicity                 0\n",
       "parental_level_of_education    0\n",
       "lunch                          0\n",
       "test_preparation_course        0\n",
       "math_score                     0\n",
       "reading_score                  0\n",
       "writing_score                  0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ce8f7b83",
   "metadata": {},
   "source": [
    "#### There are no missing values in the data set"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5840ff7f",
   "metadata": {},
   "source": [
    "### 3.2 Check Duplicates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ae16686e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5d7ae8e",
   "metadata": {},
   "source": [
    "#### There are no duplicates  values in the data set"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "30dfacc8",
   "metadata": {},
   "source": [
    "### 3.3 Check data types"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "25f95bc8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1000 entries, 0 to 999\n",
      "Data columns (total 8 columns):\n",
      " #   Column                       Non-Null Count  Dtype \n",
      "---  ------                       --------------  ----- \n",
      " 0   gender                       1000 non-null   object\n",
      " 1   race_ethnicity               1000 non-null   object\n",
      " 2   parental_level_of_education  1000 non-null   object\n",
      " 3   lunch                        1000 non-null   object\n",
      " 4   test_preparation_course      1000 non-null   object\n",
      " 5   math_score                   1000 non-null   int64 \n",
      " 6   reading_score                1000 non-null   int64 \n",
      " 7   writing_score                1000 non-null   int64 \n",
      "dtypes: int64(3), object(5)\n",
      "memory usage: 62.6+ KB\n"
     ]
    }
   ],
   "source": [
    "# Check Null and Dtypes\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0dbbf5b4",
   "metadata": {},
   "source": [
    "### 3.4 Checking the number of unique values of each column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2c2b61b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gender                          2\n",
       "race_ethnicity                  5\n",
       "parental_level_of_education     6\n",
       "lunch                           2\n",
       "test_preparation_course         2\n",
       "math_score                     81\n",
       "reading_score                  72\n",
       "writing_score                  77\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.nunique()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a4f6b022",
   "metadata": {},
   "source": [
    "### 3.5 Check statistics of data set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "76c608dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>math_score</th>\n",
       "      <th>reading_score</th>\n",
       "      <th>writing_score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1000.00000</td>\n",
       "      <td>1000.000000</td>\n",
       "      <td>1000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>66.08900</td>\n",
       "      <td>69.169000</td>\n",
       "      <td>68.054000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>15.16308</td>\n",
       "      <td>14.600192</td>\n",
       "      <td>15.195657</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.00000</td>\n",
       "      <td>17.000000</td>\n",
       "      <td>10.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>57.00000</td>\n",
       "      <td>59.000000</td>\n",
       "      <td>57.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>66.00000</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>69.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>77.00000</td>\n",
       "      <td>79.000000</td>\n",
       "      <td>79.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>100.00000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>100.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       math_score  reading_score  writing_score\n",
       "count  1000.00000    1000.000000    1000.000000\n",
       "mean     66.08900      69.169000      68.054000\n",
       "std      15.16308      14.600192      15.195657\n",
       "min       0.00000      17.000000      10.000000\n",
       "25%      57.00000      59.000000      57.750000\n",
       "50%      66.00000      70.000000      69.000000\n",
       "75%      77.00000      79.000000      79.000000\n",
       "max     100.00000     100.000000     100.000000"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9dc41207",
   "metadata": {},
   "source": [
    "#### Insight\n",
    "- From above description of numerical data, all means are very close to each other - between 66 and 68.05;\n",
    "- All standard deviations are also close - between 14.6 and 15.19;\n",
    "- While there is a minimum score  0 for math, for writing minimum is much higher = 10 and for reading myet higher = 17"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac52d9cb",
   "metadata": {},
   "source": [
    "### 3.7 Exploring Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1afd3c09",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race_ethnicity</th>\n",
       "      <th>parental_level_of_education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test_preparation_course</th>\n",
       "      <th>math_score</th>\n",
       "      <th>reading_score</th>\n",
       "      <th>writing_score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>master's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>male</td>\n",
       "      <td>group A</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>male</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender race_ethnicity parental_level_of_education         lunch  \\\n",
       "0  female        group B           bachelor's degree      standard   \n",
       "1  female        group C                some college      standard   \n",
       "2  female        group B             master's degree      standard   \n",
       "3    male        group A          associate's degree  free/reduced   \n",
       "4    male        group C                some college      standard   \n",
       "\n",
       "  test_preparation_course  math_score  reading_score  writing_score  \n",
       "0                    none          72             72             74  \n",
       "1               completed          69             90             88  \n",
       "2                    none          90             95             93  \n",
       "3                    none          47             57             44  \n",
       "4                    none          76             78             75  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b9081742",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Categories in 'gender' variable:      ['female' 'male']\n",
      "Categories in 'race_ethnicity' variable:   ['group B' 'group C' 'group A' 'group D' 'group E']\n",
      "Categories in'parental level of education' variable: [\"bachelor's degree\" 'some college' \"master's degree\" \"associate's degree\"\n",
      " 'high school' 'some high school']\n",
      "Categories in 'lunch' variable:      ['standard' 'free/reduced']\n",
      "Categories in 'test preparation course' variable:      ['none' 'completed']\n"
     ]
    }
   ],
   "source": [
    "print(\"Categories in 'gender' variable:     \",end=\" \" )\n",
    "print(df['gender'].unique())\n",
    "\n",
    "print(\"Categories in 'race_ethnicity' variable:  \",end=\" \")\n",
    "print(df['race_ethnicity'].unique())\n",
    "\n",
    "print(\"Categories in'parental level of education' variable:\",end=\" \" )\n",
    "print(df['parental_level_of_education'].unique())\n",
    "\n",
    "print(\"Categories in 'lunch' variable:     \",end=\" \" )\n",
    "print(df['lunch'].unique())\n",
    "\n",
    "print(\"Categories in 'test preparation course' variable:     \",end=\" \" )\n",
    "print(df['test_preparation_course'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2dd97e26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We have 3 numerical features : ['math_score', 'reading_score', 'writing_score']\n",
      "\n",
      "We have 5 categorical features : ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']\n"
     ]
    }
   ],
   "source": [
    "# define numerical & categorical columns\n",
    "numeric_features = [feature for feature in df.columns if df[feature].dtype != 'O']\n",
    "categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']\n",
    "\n",
    "# print columns\n",
    "print('We have {} numerical features : {}'.format(len(numeric_features), numeric_features))\n",
    "print('\\nWe have {} categorical features : {}'.format(len(categorical_features), categorical_features))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ae2822d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race_ethnicity</th>\n",
       "      <th>parental_level_of_education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test_preparation_course</th>\n",
       "      <th>math_score</th>\n",
       "      <th>reading_score</th>\n",
       "      <th>writing_score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender race_ethnicity parental_level_of_education     lunch  \\\n",
       "0  female        group B           bachelor's degree  standard   \n",
       "1  female        group C                some college  standard   \n",
       "\n",
       "  test_preparation_course  math_score  reading_score  writing_score  \n",
       "0                    none          72             72             74  \n",
       "1               completed          69             90             88  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "204aa708",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "bd42eda6",
   "metadata": {},
   "source": [
    "### 3.8 Adding columns for \"Total Score\" and \"Average\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "3ffbfdf7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race_ethnicity</th>\n",
       "      <th>parental_level_of_education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test_preparation_course</th>\n",
       "      <th>math_score</th>\n",
       "      <th>reading_score</th>\n",
       "      <th>writing_score</th>\n",
       "      <th>total score</th>\n",
       "      <th>average</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "      <td>218</td>\n",
       "      <td>72.666667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>247</td>\n",
       "      <td>82.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>master's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "      <td>278</td>\n",
       "      <td>92.666667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>male</td>\n",
       "      <td>group A</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "      <td>148</td>\n",
       "      <td>49.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>male</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "      <td>229</td>\n",
       "      <td>76.333333</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender race_ethnicity parental_level_of_education         lunch  \\\n",
       "0  female        group B           bachelor's degree      standard   \n",
       "1  female        group C                some college      standard   \n",
       "2  female        group B             master's degree      standard   \n",
       "3    male        group A          associate's degree  free/reduced   \n",
       "4    male        group C                some college      standard   \n",
       "\n",
       "  test_preparation_course  math_score  reading_score  writing_score  \\\n",
       "0                    none          72             72             74   \n",
       "1               completed          69             90             88   \n",
       "2                    none          90             95             93   \n",
       "3                    none          47             57             44   \n",
       "4                    none          76             78             75   \n",
       "\n",
       "   total score    average  \n",
       "0          218  72.666667  \n",
       "1          247  82.333333  \n",
       "2          278  92.666667  \n",
       "3          148  49.333333  \n",
       "4          229  76.333333  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['total score'] = df['math_score'] + df['reading_score'] + df['writing_score']\n",
    "df['average'] = df['total score']/3\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "26dc3844",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of students with full marks in Maths: 7\n",
      "Number of students with full marks in Writing: 14\n",
      "Number of students with full marks in Reading: 17\n"
     ]
    }
   ],
   "source": [
    "reading_full = df[df['reading_score'] == 100]['average'].count()\n",
    "writing_full = df[df['writing_score'] == 100]['average'].count()\n",
    "math_full = df[df['math_score'] == 100]['average'].count()\n",
    "\n",
    "print(f'Number of students with full marks in Maths: {math_full}')\n",
    "print(f'Number of students with full marks in Writing: {writing_full}')\n",
    "print(f'Number of students with full marks in Reading: {reading_full}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "572c8a75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of students with less than 20 marks in Maths: 4\n",
      "Number of students with less than 20 marks in Writing: 3\n",
      "Number of students with less than 20 marks in Reading: 1\n"
     ]
    }
   ],
   "source": [
    "reading_less_20 = df[df['reading_score'] <= 20]['average'].count()\n",
    "writing_less_20 = df[df['writing_score'] <= 20]['average'].count()\n",
    "math_less_20 = df[df['math_score'] <= 20]['average'].count()\n",
    "\n",
    "print(f'Number of students with less than 20 marks in Maths: {math_less_20}')\n",
    "print(f'Number of students with less than 20 marks in Writing: {writing_less_20}')\n",
    "print(f'Number of students with less than 20 marks in Reading: {reading_less_20}')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "190e078c",
   "metadata": {},
   "source": [
    "#####  Insights\n",
    " - From above values we get students have performed the worst in Maths \n",
    " - Best performance is in reading section"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e598bc93",
   "metadata": {},
   "source": [
    "### 4. Exploring Data ( Visualization )\n",
    "#### 4.1 Visualize average score distribution to make some conclusion. \n",
    "- Histogram\n",
    "- Kernel Distribution Function (KDE)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4726058",
   "metadata": {},
   "source": [
    "#### 4.1.1 Histogram & KDE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c2510266",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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27ZtMzrGiGU2OoCIiIiIiIiIiMhwo6KZiIiIiIiIiIjISVQ0ExEREREREREROYmKZiIiIiIiIiIiIidR0UxEREREREREROQk6p4pIiIiIiIiIhJkDoeDhoaGkM2XmppKfn5+v9/v8/m47bbb+Pvf/05TUxPvv/8+M2fODF7A0zh06BAFBQWGzf9RKpqJiIiIiIiIiASRw+FgUnExzs7OkM0ZFR3NvpKSfhfO3nrrLf70pz+xevVqxo0bR2pqapATDn8qmomIiIiIiIiIBFFDQwPOzk5u/O7/kJFfGPT5ah3l/OWR79DQ0NDvoll5eTlZWVksXLgwyOnCh840ExEREREREREJgYz8QnKLpgT9a6CFuS996UvcfvvtOBwOTCYTY8eOxev1snTpUgoKCoiKimLGjBn8/e9/77tm9erVmEwmli1bxqxZs4iKiuLiiy+mrq6ON998k+LiYuLj4/nCF75A50dW2L311lucd955JCYmkpKSwtVXX015efkZ8+3evZsrr7yS2NhYMjIyuPnmm0Oy1VVFMxERERERERGRUex///d/efDBB8nNzaW6upotW7awdOlSnnvuOZ566in27NnDXXfdxU033cSaNWtOuPaHP/whv/71r9mwYQOVlZXccMMNPP744zz//PO8/vrrvP322/zqV7/qe39HRwd33303W7duZcWKFZjNZq677jq8Xu8pszU3N3PxxRcza9Ystm7dyltvvUVtbS033HBDUH9PQNszRURERERERERGtYSEBOLi4rBYLGRmZuJyuXj44YdZvnw5CxYsAGDcuHGsW7eO3/72t1x44YV91z700EMsWrQIgK985Svcd999lJeXM27cOAA+/elPs2rVKr773e8CcP31158w9x//+EfS0tLYu3cvU6dO/Vi2X//618yaNYuHH374hGvy8vI4cOAAEyZMCOxvxkeoaCYiIiIiIiIiIn3Kysro7Ozk0ksvPeH57u5uZs2adcJz06dP73uckZFBdHR0X8Gs97n33nuv7/vS0lJ+8IMfsHnzZhoaGvpWmDkcjlMWzXbs2MGqVauIjY392Gvl5eUqmomIiIiIiIiISGi0t7cD8Prrr5OTk3PCa3a7/YTvrVZr32OTyXTC973PfXTr5TXXXMOYMWP43e9+R3Z2Nl6vl6lTp9Ld3X3aLNdccw2PPPLIx17Lysoa2A82QCqa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v/jVeBpP42k8jReb41VV1QDQ3d1t/nWeEcNqamoMwHjnnXeOe/6rX/2qcd55553wnG9/+9sGoa/ndNNNN91000033QZ0q66ujsYlz7Ck6zzddNNNN910083MW3+u82J6pVl2djY2m42Ghobjnm9oaCA/P/+E5zz44IM88MADfT8Hg0Gam5vJysr6QM8I6b/29naKioqorq4mNTXV7HDkJPQ+xT69R4OD3qfYF+n3yDAMOjo6KCwsDPvYEqLrvNih33mDg96n2Kf3aHDQ+xT7Yuk6L6aTZnFxccyePZtly5Zx8803A6GLo2XLlnHfffed8Byn04nT6TzuufT09AhHOnykpqbqF8sgoPcp9uk9Ghz0PsW+SL5HaWlpERlXQnSdF3v0O29w0PsU+/QeDQ56n2JfLFznxXTSDOCBBx7g7rvvZs6cOZx33nn88pe/pKurq2+XJREREREZnHSdJyIiIrEs5pNmH/nIR2hqauJb3/oW9fX1zJgxg1dfffUDTWNFREREZHDRdZ6IiIjEsphPmgHcd999J12mL9HhdDr59re//YGSCIktep9in96jwUHvU+zTezR06DrPfPr7NDjofYp9eo8GB71PsS+W3iOLYWgvdRERERERERERkfeymh2AiIiIiIiIiIhIrFHSTERERERERERE5H2UNBMREREREREREXkfJc1ERERERERERETeR0kz6fPII49w7rnnkpKSQm5uLjfffDPl5eXHHePxeFi0aBFZWVkkJydz22230dDQYFLEAvDjH/8Yi8XC/fff3/ec3ifz1dTUcOedd5KVlUVCQgJTp05l06ZNfa8bhsG3vvUtCgoKSEhI4IorrqCiosLEiIefQCDAww8/zOjRo0lISGDs2LF8//vf57374+h9ir63336bG264gcLCQiwWCy+88MJxr/fnPWlubmbhwoWkpqaSnp7OvffeS2dnZxT/FCKxR9d5g5Ou82KTrvNin67zYtNgvM5T0kz6rFy5kkWLFrFu3TreeOMN/H4/V111FV1dXX3HfOlLX+Kll17iueeeY+XKldTW1nLrrbeaGPXwtnHjRn7/+98zbdq0457X+2SulpYW5s+fj8PhYOnSpezZs4f/+Z//ISMjo++Yn/70p/z617/mscceY/369SQlJXH11Vfj8XhMjHx4+clPfsLvfvc7/vd//5eysjJ+8pOf8NOf/pTf/OY3fcfofYq+rq4upk+fzqOPPnrC1/vznixcuJDdu3fzxhtv8PLLL/P222/zmc98Jlp/BJGYpOu8wUfXebFJ13mDg67zYtOgvM4zRE6isbHRAIyVK1cahmEYra2thsPhMJ577rm+Y8rKygzAWLt2rVlhDlsdHR1GaWmp8cYbbxgXX3yx8cUvftEwDL1PseDrX/+6sWDBgpO+HgwGjfz8fONnP/tZ33Otra2G0+k0/v73v0cjRDEM4/rrrzc++clPHvfcrbfeaixcuNAwDL1PsQAwFi9e3Pdzf96TPXv2GICxcePGvmOWLl1qWCwWo6amJmqxi8Q6XefFNl3nxS5d5w0Ous6LfYPlOk8rzeSk2traAMjMzARg8+bN+P1+rrjiir5jJk6cSHFxMWvXrjUlxuFs0aJFXH/99ce9H6D3KRa8+OKLzJkzh9tvv53c3FxmzpzJ448/3vf6oUOHqK+vP+49SktLY+7cuXqPouiCCy5g2bJl7Nu3D4Dt27ezevVqrr32WkDvUyzqz3uydu1a0tPTmTNnTt8xV1xxBVarlfXr10c9ZpFYpeu82KbrvNil67zBQdd5g0+sXufZIzKqDHrBYJD777+f+fPnM2XKFADq6+uJi4sjPT39uGPz8vKor683Icrh65lnnmHLli1s3LjxA6/pfTLfwYMH+d3vfscDDzzAQw89xMaNG/nCF75AXFwcd999d9/7kJeXd9x5eo+i6xvf+Abt7e1MnDgRm81GIBDghz/8IQsXLgTQ+xSD+vOe1NfXk5ube9zrdrudzMxMvW8ix+g6L7bpOi+26TpvcNB13uATq9d5SprJCS1atIhdu3axevVqs0OR96muruaLX/wib7zxBvHx8WaHIycQDAaZM2cOP/rRjwCYOXMmu3bt4rHHHuPuu+82OTrp9Y9//IOnnnqKp59+msmTJ7Nt2zbuv/9+CgsL9T6JyJCm67zYpeu82KfrvMFB13kSLirPlA+47777ePnll1m+fDkjR47sez4/Px+fz0dra+txxzc0NJCfnx/lKIevzZs309jYyKxZs7Db7djtdlauXMmvf/1r7HY7eXl5ep9MVlBQwDnnnHPcc5MmTaKqqgqg7314/05Xeo+i66tf/Srf+MY3+OhHP8rUqVP5+Mc/zpe+9CUeeeQRQO9TLOrPe5Kfn09jY+Nxr/f09NDc3Kz3TQRd58U6XefFPl3nDQ66zht8YvU6T0kz6WMYBvfddx+LFy/mrbfeYvTo0ce9Pnv2bBwOB8uWLet7rry8nKqqKubNmxftcIetyy+/nJ07d7Jt27a+25w5c1i4cGHfY71P5po/fz7l5eXHPbdv3z5KSkoAGD16NPn5+ce9R+3t7axfv17vURR1d3djtR7/z6DNZiMYDAJ6n2JRf96TefPm0drayubNm/uOeeuttwgGg8ydOzfqMYvECl3nDQ66zot9us4bHHSdN/jE7HVeRLYXkEHps5/9rJGWlmasWLHCqKur67t1d3f3HfNf//VfRnFxsfHWW28ZmzZtMubNm2fMmzfPxKjFMIzjdlUyDL1PZtuwYYNht9uNH/7wh0ZFRYXx1FNPGYmJicaTTz7Zd8yPf/xjIz093fj3v/9t7Nixw7jpppuM0aNHG26328TIh5e7777bGDFihPHyyy8bhw4dMp5//nkjOzvb+NrXvtZ3jN6n6Ovo6DC2bt1qbN261QCMn//858bWrVuNyspKwzD6955cc801xsyZM43169cbq1evNkpLS4077rjDrD+SSEzQdd7gpeu82KLrvMFB13mxaTBe5ylpJn2AE96eeOKJvmPcbrfxuc99zsjIyDASExONW265xairqzMvaDEM44MXU3qfzPfSSy8ZU6ZMMZxOpzFx4kTjD3/4w3GvB4NB4+GHHzby8vIMp9NpXH755UZ5eblJ0Q5P7e3txhe/+EWjuLjYiI+PN8aMGWN885vfNLxeb98xep+ib/ny5Sf8t+juu+82DKN/78nRo0eNO+64w0hOTjZSU1ONT3ziE0ZHR4cJfxqR2KHrvMFL13mxR9d5sU/XebFpMF7nWQzDMCKzhk1ERERERERERGRwUk8zERERERERERGR91HSTERERERERERE5H2UNBMREREREREREXkfJc1ERERERERERETeR0kzERERERERERGR91HSTERERERERERE5H2UNBMREREREREREXkfJc1ERERERERERETeR0kzERERERERERGR91HSTESGvUAgQDAYNDsMEREREYkAXeuJyNlS0kxEYs6rr77KggULSE9PJysriw996EMcOHAAgAsuuICvf/3rxx3f1NSEw+Hg7bffBsDr9fKVr3yFESNGkJSUxNy5c1mxYkXf8X/5y19IT0/nxRdf5JxzzsHpdFJVVcXGjRu58soryc7OJi0tjYsvvpgtW7YcN9fevXtZsGAB8fHxnHPOObz55ptYLBZeeOGFvmOqq6v58Ic/THp6OpmZmdx0000cPnw4Iv+tRERERAYbXeuJyGChpJmIxJyuri4eeOABNm3axLJly7Bardxyyy0Eg0EWLlzIM888g2EYfcc/++yzFBYWcuGFFwJw3333sXbtWp555hl27NjB7bffzjXXXENFRUXfOd3d3fzkJz/hj3/8I7t37yY3N5eOjg7uvvtuVq9ezbp16ygtLeW6666jo6MDCH1LefPNN5OYmMj69ev5wx/+wDe/+c3jYvf7/Vx99dWkpKSwatUq1qxZQ3JyMtdccw0+ny8K//VEREREYpuu9URk0DBERGJcU1OTARg7d+40GhsbDbvdbrz99tt9r8+bN8/4+te/bhiGYVRWVho2m82oqak5bozLL7/cePDBBw3DMIwnnnjCAIxt27adct5AIGCkpKQYL730kmEYhrF06VLDbrcbdXV1fce88cYbBmAsXrzYMAzD+Nvf/mZMmDDBCAaDfcd4vV4jISHBeO21187+P4KIiIjIEKVrPRGJVVppJiIxp6KigjvuuIMxY8aQmprKqFGjAKiqqiInJ4errrqKp556CoBDhw6xdu1aFi5cCMDOnTsJBAKMHz+e5OTkvtvKlSv7lv0DxMXFMW3atOPmbWho4NOf/jSlpaWkpaWRmppKZ2cnVVVVAJSXl1NUVER+fn7fOeedd95xY2zfvp39+/eTkpLSN3dmZiYej+e4+UVERESGK13richgYTc7ABGR97vhhhsoKSnh8ccfp7CwkGAwyJQpU/qWvC9cuJAvfOEL/OY3v+Hpp59m6tSpTJ06FYDOzk5sNhubN2/GZrMdN25ycnLf44SEBCwWy3Gv33333Rw9epRf/epXlJSU4HQ6mTdv3hktte/s7GT27Nl9F3rvlZOT0+9xRERERIYqXeuJyGChpJmIxJSjR49SXl7O448/3te3YvXq1ccdc9NNN/GZz3yGV199laeffpq77rqr77WZM2cSCARobGzsO7+/1qxZw29/+1uuu+46INTk1eVy9b0+YcIEqquraWhoIC8vD4CNGzceN8asWbN49tlnyc3NJTU19YzmFxERERnqdK0nIoOJyjNFJKZkZGSQlZXFH/7wB/bv389bb73FAw88cNwxSUlJ3HzzzTz88MOUlZVxxx139L02fvx4Fi5cyF133cXzzz/PoUOH2LBhA4888givvPLKKecuLS3lb3/7G2VlZaxfv56FCxeSkJDQ9/qVV17J2LFjufvuu9mxYwdr1qzhv//7vwH6vslcuHAh2dnZ3HTTTaxatYpDhw6xYsUKvvCFL3DkyJFw/WcSERERGZR0rScig4mSZiISU6xWK8888wybN29mypQpfOlLX+JnP/vZB45buHAh27dv58ILL6S4uPi415544gnuuusuvvzlLzNhwgRuvvlmNm7c+IHj3u9Pf/oTLS0tzJo1i49//ON84QtfIDc3t+91m83GCy+8QGdnJ+eeey6f+tSn+nZUio+PByAxMZG3336b4uJibr31ViZNmsS9996Lx+PRt5EiIiIy7OlaT0QGE4thvGcvXxEROSNr1qxhwYIF7N+/n7Fjx5odjoiIiIiEka71RIY3Jc1ERM7A4sWLSU5OprS0lP379/PFL36R/9/eHZxAEAJRFOwUBEMyJ6MwSVMwgb3K39PCwLBQFYHH5tHYrbWvvzgAAPg/Zj3g5hAAwA/OOTXnrL139d5rjFFrrbefBQDAA8x6wM2mGQAAAAAEhwAAAAAAIIhmAAAAABBEMwAAAAAIohkAAAAABNEMAAAAAIJoBgAAAABBNAMAAACAIJoBAAAAQBDNAAAAACB8APFmyNTpQFSFAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1500x700 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, axs = plt.subplots(1, 2, figsize=(15, 7))\n",
    "plt.subplot(121)\n",
    "sns.histplot(data=df,x='average',bins=30,kde=True,color='g')\n",
    "plt.subplot(122)\n",
    "sns.histplot(data=df,x='average',kde=True,hue='gender')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e7967c7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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27ZtMzrGiGU2OoCIiIiIiIiIiMhwo6KZiIiIiIiIiIjISVQ0ExEREREREREROYmKZiIiIiIiIiIiIidR0UxEREREREREROQk6p4pIiIiIiIiIhJkDoeDhoaGkM2XmppKfn5+v9/v8/m47bbb+Pvf/05TUxPvv/8+M2fODF7A0zh06BAFBQWGzf9RKpqJiIiIiIiIiASRw+FgUnExzs7OkM0ZFR3NvpKSfhfO3nrrLf70pz+xevVqxo0bR2pqapATDn8qmomIiIiIiIiIBFFDQwPOzk5u/O7/kJFfGPT5ah3l/OWR79DQ0NDvoll5eTlZWVksXLgwyOnCh840ExEREREREREJgYz8QnKLpgT9a6CFuS996UvcfvvtOBwOTCYTY8eOxev1snTpUgoKCoiKimLGjBn8/e9/77tm9erVmEwmli1bxqxZs4iKiuLiiy+mrq6ON998k+LiYuLj4/nCF75A50dW2L311lucd955JCYmkpKSwtVXX015efkZ8+3evZsrr7yS2NhYMjIyuPnmm0Oy1VVFMxERERERERGRUex///d/efDBB8nNzaW6upotW7awdOlSnnvuOZ566in27NnDXXfdxU033cSaNWtOuPaHP/whv/71r9mwYQOVlZXccMMNPP744zz//PO8/vrrvP322/zqV7/qe39HRwd33303W7duZcWKFZjNZq677jq8Xu8pszU3N3PxxRcza9Ystm7dyltvvUVtbS033HBDUH9PQNszRURERERERERGtYSEBOLi4rBYLGRmZuJyuXj44YdZvnw5CxYsAGDcuHGsW7eO3/72t1x44YV91z700EMsWrQIgK985Svcd999lJeXM27cOAA+/elPs2rVKr773e8CcP31158w9x//+EfS0tLYu3cvU6dO/Vi2X//618yaNYuHH374hGvy8vI4cOAAEyZMCOxvxkeoaCYiIiIiIiIiIn3Kysro7Ozk0ksvPeH57u5uZs2adcJz06dP73uckZFBdHR0X8Gs97n33nuv7/vS0lJ+8IMfsHnzZhoaGvpWmDkcjlMWzXbs2MGqVauIjY392Gvl5eUqmomIiIiIiIiISGi0t7cD8Prrr5OTk3PCa3a7/YTvrVZr32OTyXTC973PfXTr5TXXXMOYMWP43e9+R3Z2Nl6vl6lTp9Ld3X3aLNdccw2PPPLIx17Lysoa2A82QCqa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OwzDCG1H/uCDDxo5OTmG0+k0Lr30UqO8vPyYNo4cOWLccsstRmJiopGcnGx84hOfMDo7O034bYaek13fnp4e47LLLjOysrIMh8NhFBcXG3ffffcxWwsbhq7viRzvugLGn//85/5jBvJ+cOjQIePKK6804uLijMzMTOPLX/6y4fP5ovzbDD2nur7V1dXGhRdeaKSnpxtOp9OYMGGC8dWvftVob28/ph1d3+P75Cc/aRQXFxsxMTFGVlaWcemll/YPpAxDf7syemmcF14a50WWxnmRo3FeZGmcF1nDdZxnMQzDCP/8NRERERERERERkeFLNc1ERERERERERETeR0kzERERERERERGR91HSTERERERERERE5H2UNBMREREREREREXkfJc1ERERERERERETeR0kzERERERERERGR91HSTERERERERERE5H2UNBOREe3OO+/k+uuvNzsMEREREQkzjfNEJNKUNBORqFq0aBFf/OIXo3aeiIiIiESHxnkiMtIoaSYiEkU+n8/sEEREREQkAjTOExl5lDQTkai58847Wb16Nb/61a+wWCxYLBYOHToEwOrVqznnnHNwOp3k5eXx9a9/Hb/ff9LzAoEAd911FyUlJcTFxTFp0iR+9atfnVZMVVVVXHPNNaSlpZGQkMDUqVNZtmxZ/+u7d+/mwx/+MMnJySQlJXHBBRdQWVkJQDAY5Lvf/S4FBQU4nU5mzZrFyy+/3H/uoUOHsFgsPP3001x00UXExsbyt7/9DYBHH32UKVOmEBsby+TJk/ntb387mEsrIiIiYiqN8zTOExmJ7GYHICKjx69+9Sv27dvHtGnT+O53vwtAVlYWtbW1XHXVVdx555389a9/Ze/evdx9993Exsby7W9/+4TnBYNBCgoKeOaZZ8jIyODtt9/m05/+NHl5eXz0ox8dUExLlizB6/Xy5ptvkpCQwJ49e0hMTASgtraWCy+8kEWLFvHGG2+QnJzM2rVr+wd5v/rVr/jZz37GH/7wB2bPns1jjz3Gtddey+7duyktLe3v4+tf/zo/+9nPmD17dv+A6pvf/Cb/+7//y+zZs9m6dSt33303CQkJ3HHHHeG85CIiIiJRoXGexnkiI5IhIhJFF110kfGFL3zhmOceeOABY9KkSUYwGOx/7uGHHzYSExONQCBwwvOOZ8mSJcZNN93U//Mdd9xhXHfddSc8fvr06ca3v/3t4752//33GyUlJYbX6z3u6/n5+cYPfvCDY547++yzjXvuuccwDMM4ePCgARi//OUvjzlm/PjxxpNPPnnMc9/73veMBQsWnDBOERERkaFO4zyN80RGGs00ExHTlZWVsWDBAiwWS/9zCxcupKuri8OHD1NUVHTCcx9++GEee+wxqqurcbvdeL1eZs2aNeC+P//5z/PZz36WV199lcWLF3PTTTcxY8YMALZt28YFF1yAw+H4wHkdHR3U1dWxcOHCY55fuHAh27dvP+a5efPm9T/u7u6msrKSu+66i7vvvrv/eb/fT0pKyoDjFhERERkONM7TOE9kOFNNMxEZtp566im+8pWvcNddd/Hqq6+ybds2PvGJT+D1egfcxqc+9SkOHDjAf/7nf7Jz507mzZvHb37zGwDi4uLCEmdCQkL/466uLgAeeeQRtm3b1n/btWsX69evD0t/IiIiIsOdxnkiMhQoaSYiURUTE0MgEDjmuSlTprBu3ToMw+h/bu3atSQlJVFQUHDC89auXct5553HPffcw+zZs5kwYUJ/8dbTUVhYyGc+8xmeffZZvvzlL/PII48AMGPGDNasWXPcnZCSk5PJz89n7dq1H4jprLPOOmFfOTk55Ofnc+DAASZMmHDMraSk5LRjFxERERkqNM7TOE9kpFHSTESiauzYsWzYsIFDhw7hcrkIBoPcc8891NTU8LnPfY69e/fy/PPP861vfYv77rsPq9V6wvNKS0vZtGkTr7zy/9u5Q5bIojAAw98GRxREDYJgNJnGIkzR6G+wCFZhwCkyUwRNYjH4BwyDwWKVSdoVdTDdEZk/MMkkDMO3YVlZ7oLLWlbc56mXw7mc9PFy7+lEr9eLvb29uLm5+av3aTQa0el0ot/vx93dXVxdXcXS0lJERNTr9Xh5eYmNjY24vb2Np6enaLfbURRFRETs7u7G0dFRnJ+fR1EU0Wq14uHhIXZ2dt7d8+DgIA4PD+Pk5CR6vV48Pj7G6elpHB8ff+BEAQA+B3OeOQ++nH99qRrwfymKImu1Wk5MTGREZL/fz8zM6+vrXFlZyUqlkvPz89lsNnM4HL677vX1Nbe2tnJ6ejpnZmZye3s7W61WVqvVt3V/uiC2Xq/n4uJijo+P59zcXG5ubuZgMHh7unb20AAAAL9JREFU3u12c319PScnJ3NqaipXV1fz+fk5MzNHo1Hu7+/nwsJCjo2NZbVazcvLy7e1Py+Ivb+//23fs7OzXF5ezkqlkrOzs7m2tpYXFxcfO1QAgE/AnPeDOQ++jm+Zv3wnCwAAAAD4PRMAAAAAykQzAAAAACgRzQAAAACgRDQDAAAAgBLRDAAAAABKRDMAAAAAKBHNAAAAAKBENAMAAACAEtEMAAAAAEpEMwAAAAAoEc0AAAAAoEQ0AwAAAICS713Hiq/H6H8kAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1500x700 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, axs = plt.subplots(1, 2, figsize=(15, 7))\n",
    "plt.subplot(121)\n",
    "sns.histplot(data=df,x='total score',bins=30,kde=True,color='g')\n",
    "plt.subplot(122)\n",
    "sns.histplot(data=df,x='total score',kde=True,hue='gender')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d200b76",
   "metadata": {},
   "source": [
    "#####  Insights\n",
    "- Female students tend to perform well then male students."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "15522737",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABdoAAAINCAYAAAAp7s0nAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAEAAElEQVR4nOzdd3iV9f3/8ec5Odl7h5DFTkBQhgMXigpStbbQ2vJDq1W/ta0LnLWOuiqOqriqrVWwVYujrmpdIKAgIILssGLgMLL3PCfJOb8/TnI0sjLOyX3OyetxXbnOnTPu+xUgfM79Pp/7/TE5nU4nIiIiIiIiIiIiIiLSI2ajA4iIiIiIiIiIiIiI+DMV2kVEREREREREREREekGFdhERERERERERERGRXlChXURERERERERERESkF1RoFxERERERERERERHpBRXaRURERERERERERER6QYV2EREREREREREREZFeUKFdRERERERERERERKQXLEYH8DaHw8GBAweIjo7GZDIZHUdERPoxp9NJXV0d6enpmM36rLu3NMaLiIgv0TjvWRrnRUTEV3R1jA/4QvuBAwfIzMw0OoaIiIjb3r17ycjIMDqG39MYLyIivkjjvGdonBcREV9ztDE+4Avt0dHRgOsPIiYmxuA0IiLSn9XW1pKZmekem6R3NMaLiIgv0TjvWRrnRUTEV3R1jA/4QnvHJWYxMTEanEVExCfo8mfP0BgvIiK+SOO8Z2icFxERX3O0MV6N40REREREREREREREekGFdhERERERERERERGRXlChXURERERERERERESkFwzt0d7W1sbdd9/Nyy+/THFxMenp6Vx22WXccccd7p43TqeTP/3pTzz//PNUV1dzyimn8OyzzzJs2DCP5XA6nbS2ttLW1uaxfUrgCAoKwmKxqNeiiIgf0hgvR6IxXkRERKR/0HmBHImnzgsMLbQ/9NBDPPvss7z00kuMGjWKr7/+ml//+tfExsZy3XXXAfDwww/z5JNP8tJLLzFo0CDuvPNOpk6dytatWwkLC+t1BrvdTlFREY2Njb3elwSuiIgIBgwYQEhIiNFRRESkizTGS1dojBcREREJbDovkK7wxHmBoYX2L7/8kgsvvJDzzjsPgJycHP7973/z1VdfAa5Pm+bNm8cdd9zBhRdeCMA///lPUlNTeeedd/jlL3/Zq+M7HA4K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WL16NWVlZeTl5dHc3MzHH3/M9u3bSUxMJDY2lmHDhmG1Wlm4cCHHH388H3zwAW+//Xa3jhkVFcUVV1zBzTffTGJiIikpKdx+++2Yzd+tp5uVlUVISAhPPfUUv/3tb9m8eTP33XefR/YtIiLSH2iMF+m+1KwhZAwbZXQMERER6YGh6fGMGz7w6E+UQxo3bhz/+c9/yMnJwWI5uMw7cuRIQkNDsVqth53osnTpUuLj4zn22GOPeqzXXnuNlJSUg1pVdhgwYACrV6/m9NNPB6C1tZW1a9cybtw493OSk5MpKipyf19bW0thYaH7+zFjxrBv3z527NhxyFnt48aNY+vWrQwdOvSQGXJzc93H7Wgds337dqqrq4/483mCCu2HUWIt8NnjxMTE8PnnnzNv3jxqa2vJzs7m0UcfZdq0aUyYMIGlS5cyYcIE6uvrWbJkCT/+8Y+ZM2cO11xzDTabjfPOO48777yz02q+XfHII4+4PymLjo7mxhtvpKamxv14cnIyCxYs4I9//CNPPvkk48aN4y9/+ctBl570ZN8iIiKe5KvjvMZ4EREREZG+46vnBV119dVX8/zzzzNz5kxuueUWEhIS2LVrFwsXLuQf//gH0dHR3HTTTcyZMweHw8Gpp55KTU0NK1asICYmhksvvZT33nuvS+/rZ82axSOPPMKFF17IvffeS0ZGBnv27OGtt97illtuISMjg+uvv54HH3yQYcOGkZuby2OPPXZQgXvy5MksWLCACy64gLi4OO666y73QqcAkyZN4vTTT2fGjBk89thjDB06lG3btmEymTj33HO59dZbOemkk7jmmmu48soriYyMZOvWrXz66ac8/fTTjBgxgnPPPZerrrqKZ599FovFwuzZs486U94TVGj/gaSkJMIjInjloZv77JjhEREkJSV1+fl5eXl89NFHh3wsOTmZTz755KD7H3744U6LJQDuRQMA7r777oNOymfPnt3pOVFRUfzrX//qtALxzTd3/nOaOXMmM2fO7HTf9y8HOeOMMw7Zl6kr+xYREektXx/nNcaLiIiIiHifr58XdFV6ejorVqzg1ltvZcqUKdhsNrKzszn33HPdV5Hed999JCcnM3fuXL799lvi4uIYN26cu1XMe++9x4svvnjUY0VERPD5559z6623Mn36dOrq6hg4cCBnnXWWe4b7jTfeSFFREZdeeilm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EpwwkH9vrvdkTBEJQBrjNcaL8d5df4BPt5YQHGTi0Z8fS6glqEuvu2hUFK01JTS2mfiqsNLLKUVERCSQFRUVMXPmTC6//HLy8/NZunQp06dP509/+hMXXXQR5557LkVFRRQVFbkn6ERHR7NgwQK2bt3KE088wfPPP8/jjz/eab8FBQW88847vP/++7z//vssW7aMBx980P34zTffzLJly3j33Xf55JNPWLp0KevWreu0j5aWFu677z42bNjAO++8w+7du7nssssO+hn+8Ic/8OCDD5Kfn8+YMWO6tG9/p0K7H3riiSe49957ycjIoKioiDVr1gDw0ksvERISwooVK3juueeorq5m8uTJjB07lq+//pqPPvqIkpISLrroIve+5s6dyz//+U+ee+45tmzZwpw5c7j44otZtmyZ+znV1dUsX77cfRIOsHjxYrZv386nn37K+++/T0tLC1OnTiU6OpovvviCFStWEBUVxbnnnovdbgfg0UcfZcGCBbz44ossX76cyspK3n777W797A6Hg2nTprFixQpefvlltm7dyoMPPkhQkOsEqKCggHPPPZcZM2awceNGXnvtNZYvX84111zj3sdll13G3r17WbJkCW+++SZ//etfKS0t7f5fhASsr/dU0mBvIzY8mFOGJPZqX2HBQYxPaAXgf7sayC+q9UREEQlQGuM1xoux6m2t3P/BVgCumzyMkekxXX5tmMVM5eLnAdiwr5rmljavZBQREfFrbS3QWEEUDYR27bPsfqmoqIjW1lamT59OTk4Oo0eP5ve//z1RUVGEh4cTGhpKWloaaWlp7itQ77jjDk4++WRycnK44IILuOmmm3j99dc77dfhcLBgwQKOOeYYTjvtNC655BIWL14MQH19PS+88AJ/+ctfOOussxg9ejQvvfQSra2tnfZx+eWXM23aNAYPHsxJJ53Ek08+yYcffkh9fefJhffeey/nnHMOQ4YMISQkpEv79ndqHeOHYmNjiY6OJigoiLS0NPf9w4YN4+GHH3Z/f//99zN27FgeeOC7vtIvvvgimZmZ7Nixg+zsbB544AEWLVrExIkTARg8eDDLly/nb3/7G5MmTQLgf//7H2PGjCE9Pd29n8jISP7xj3+4f5lffvllHA4H//jHP9yXrsyfP5+4uDiWLl3KlClTmDdvHrfddhvTp08H4LnnnuPjjz/u1s++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s3bt2ubl3fEcun2OVyJgnHHGGeqtt95S27ZtU5s2bVJnnXWWysjIUA0NDc3rXH/99So9PV0tWLBArVu3To0dO1aNHz/eh1F3f2vWrFE9evRQQ4YMUbfcckvzfLmWbVNVVaUyMzPVVVddpVavXq327dunvvvuO5Wbm9u8zhNPPKEiIyPV7Nmz1ebNm9V5552nevbsqZqamnwYeff06KOPqtjYWDVnzhyVl5enPv30UxUWFqaee+655nXkeh7bN998o+677z71+eefK0B98cUXLZa35tpNmzZNDR06VK1atUotXbpU9enTR1166aVdfCbiRCE5vvNInu84yfHeJTm+4yTP+69AyXdfffWVmjt3rtq9e7fatWuXuvfee5XRaFTbtm1TSvnHOfycP+fKBx98UA0cOFAVFxc3T+Xl5c3L/eEclAqcXFtWVtbiZzF//nwFqEWLFiml/OfnESi5+uKLL1YDBgxQixcvVnv27FEPPvigioiIUIWFhUqp7nkO3T3HS6E9gJWVlSlALV68WCmlVE1NjTIajerTTz9tXicnJ0cBauXKlb4Ks1urr69XWVlZav78+WrixInNbyrkWrbdXXfdpSZMmHDM5W63WyUlJamnn366eV5NTY0ymUzqww8/7IoQ/crZZ5+trr766hbzLrjgAjVz5kyllFzPtvhlcm7NtduxY4cC1Nq1a5vX+fbbb5WmaaqoqKjLYhcnLsnx3iF53jskx3uX5Hjvkjzv3wIp30VHR6vXX3/d787B33Plgw8+qIYOHXrUZf5yDkoFbq695ZZbVO/evZXb7farn0cg5GqLxaL0er2aM2dOi/kjRoxQ9913n1+cQ3fM8dJ1TACrra0FICYmBoD169fjcDiYMmVK8zr9+/cnIyODlStX+iTG7u7GG2/k7LPPbnHNQK5le3z11VeMGjWKiy66iISEBIYPH85rr73WvDwvL4+SkpIW1zQyMpIxY8bINT2K8ePHs2DBAnbv3g3A5s2bWbZsGWeeeSYg17MjWnPtVq5cSVRUFKNGjWpeZ8qUKeh0OlavXt3lMYsTj+R475A87x2S471LcnznkjzvXwIh37lcLj766CMaGxsZN26c351DIOTKPXv2kJKSQq9evZg5cyb5+fmAf51DIOZau93Oe++9x9VXX42maX718wiEXO10OnG5XAQHB7eYbzabWbZsmV+cwy91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diGEEEIIIYQQQgghhBCiA6TQLoQQQgghhBBCCCGEEEJ0gBTahRBCCCGEEEIIIYQQQogOkEK7EEIIIYQQQgghhBBCCNEBUmgXQgghhBBCCCGEEEIIITpACu1CiDZxuVy43W5fhyGEEEIIL5McL4QQQgQuyfNCdD4ptAvh5+bNm8eECROIiooiNjaWc845h7179wIwfvx47rrrrhbrl5eXYzQaWbJkCQA2m42//OUvpKamEhoaypgxY/jxxx+b13/77beJioriq6++YsCAAZhMJvLz81m7di2nn346cXFxREZGMnHiRDZs2NDiWDt37mTChAkEBwczYMAAfvjhBzRNY/bs2c3rFBQUcPHFFxMVFUVMTAzTp09n//79nXKthBBCCH8iOV4IIYQIXJLnhQg8UmgXws81NjZy++23s27dOhYsWIBOp+P888/H7XYzc+ZMPvroI5RSzet//PHHpKSkcMoppwBw0003sXLlSj766CO2bNnCRRddxLRp09izZ0/zNhaLhSeffJLXX3+d7du3k5CQQH19PbNmzWLZsmWsWrWKrKwszjrrLOrr6wHPp+UzZswgJCSE1atX8+qrr3Lfffe1iN3hcHDGGWcQHh7O0qVLWb58OWFhYUybNg273d4FV08IIYToviTHCyGEEIFL8rwQAUgJIQJKeXm5AtTWrVtVWVmZMhgMasmSJc3Lx40bp+666y6llFIHDhxQer1eFRUVtdjH5MmT1T333KOUUuqtt95SgNq0adOvHtflcqnw8HD19ddfK6WU+vbbb5XBYFDFxcXN68yfP18B6osvvlBKKfXuu++qfv36Kbfb3byOzWZTZrNZfffdd+2/CEIIIUQAkhwvhBBCBC7J80L4P2nRLoSf27NnD5deeim9evUiIiKCHj16AJCfn098fDxTp07l/fffByAvL4+VK1cyc+ZMALZu3YrL5aJv376EhYU1T4sXL25+ZA0gKCiIIUOGtDhuaWkpf/jDH8jKyiIyMpKIiAgaGhrIz88HYNeuXaSnp5OUlNS8zUknndRiH5s3byY3N5fw8PDmY8fExGC1WlscXwghhDgRSY4XQgghApfkeSECj8HXAQghOubcc88lMzOT1157jZSUFNxuN4MGDWp+XGvmzJncfPPNvPDCC3zwwQcMHjyYwYMHA9DQ0IBer2f9+vXo9foW+w0LC2v+3mw2o2lai+WzZs2isrKS5557jszMTEwmE+PGjWvTY2INDQ2MHDmy+c3Dz8XHx7d6P0IIIUQgkhwvhBBCBC7J80IEHim0C+HHKisr2bVrF6+99lpzP23Lli1rsc706dO57rrrmDdvHh988AFXXnll87Lhw4fjcrkoKytr3r61li9fzn/+8x/OOusswDMQSkVFRfPyfv36UVBQQGlpKYmJiQCsXbu2xT5GjBjBxx9/TEJCAhEREW06vhBCCBHIJMcLIYQQgUvyvBCBSbqOEcKPRUdHExsby6uvvkpubi4LFy7k9ttvb7FOaGgoM2bM4IEHHiAnJ4dLL720eVnfvn2ZOXMmV155JZ9//jl5eXmsWbOGxx9/nLlz5/7qsbOysnj33XfJyclh9erVzJw5E7PZ3Lz89NNPp3fv3syaNYstW7awfPly7r//foDmT9RnzpxJXFwc06dPZ+nSpeTl5fHjjz9y8803U1hY6K3LJIQQQvgdyfFCCCFE4JI8L0RgkkK7EH5Mp9Px0UcfsX79egYNGsRtt93G008/fcR6M2fOZPPmzZxyyilkZGS0WPbWW29x5ZVXcscdd9CvXz9mzJjB2rVrj1jvl9544w2qq6sZMWIEV1xxBTfffDMJCQnNy/V6PbNnz6ahoYHRo0dz7bXXNo9UHhwcDEBISAhLliwhIyODCy64gOzsbK655hqsVqt8Ki6EEOKEJjleCCGECFyS54UITJpSSvk6CCHEiWH58uVMmDCB3Nxcevfu7etwhBBCCOElkuOFEEKIwCV5XojWkUK7EKLTfPHFF4SFhZGVlUVubi633HIL0dHRR/Q9J4QQQgj/IjleCCGECFyS54VoHxkMVQjRaerr67nrrrvIz88nLi6OKVOm8K9//cvXYQkhhBCigyTHCyGEEIFL8rwQ7SMt2oUQQgghhBBCCCGEEEKIDpDBUIUQQgghhBBCCCGEEEKIDpBCuxBCCCGEEEIIIYQQQgjRAVJoF0IIIYQQQgghhBBCCCE6QArtQgghhBBCCCGEEEIIIUQHSKFdCCGEEEIIIYQQQgghhOgAKbQLIYQQQgghhBBCCCGEEB0ghXYhhBBCCCGEEEIIIYQQogOk0C6EEEIIIYQQQgghhBBCdIAU2oUQQgghhBBCCCGEEEKIDvh/lh40uK+0DYwAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 2500x600 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.subplots(1,3,figsize=(25,6))\n",
    "plt.subplot(141)\n",
    "sns.histplot(data=df,x='average',kde=True,hue='lunch')\n",
    "plt.subplot(142)\n",
    "sns.histplot(data=df[df.gender=='female'],x='average',kde=True,hue='lunch')\n",
    "plt.subplot(143)\n",
    "sns.histplot(data=df[df.gender=='male'],x='average',kde=True,hue='lunch')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "569113e7",
   "metadata": {},
   "source": [
    "#####  Insights\n",
    "- Standard lunch helps perform well in exams.\n",
    "- Standard lunch helps perform well in exams be it a male or a female."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b6c697a",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.subplots(1,3,figsize=(25,6))\n",
    "plt.subplot(141)\n",
    "ax =sns.histplot(data=df,x='average',kde=True,hue='parental level of education')\n",
    "plt.subplot(142)\n",
    "ax =sns.histplot(data=df[df.gender=='male'],x='average',kde=True,hue='parental level of education')\n",
    "plt.subplot(143)\n",
    "ax =sns.histplot(data=df[df.gender=='female'],x='average',kde=True,hue='parental level of education')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e7fd489",
   "metadata": {},
   "source": [
    "#####  Insights\n",
    "- In general parent's education don't help student perform well in exam.\n",
    "- 2nd plot shows that parent's whose education is of associate's degree or master's degree their male child tend to perform well in exam\n",
    "- 3rd plot we can see there is no effect of parent's education on female students."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b30cbd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.subplots(1,3,figsize=(25,6))\n",
    "plt.subplot(141)\n",
    "ax =sns.histplot(data=df,x='average',kde=True,hue='race/ethnicity')\n",
    "plt.subplot(142)\n",
    "ax =sns.histplot(data=df[df.gender=='female'],x='average',kde=True,hue='race/ethnicity')\n",
    "plt.subplot(143)\n",
    "ax =sns.histplot(data=df[df.gender=='male'],x='average',kde=True,hue='race/ethnicity')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6180a334",
   "metadata": {},
   "source": [
    "#####  Insights\n",
    "- Students of group A and group B tends to perform poorly in exam.\n",
    "- Students of group A and group B tends to perform poorly in exam irrespective of whether they are male or female"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a1f7eef3",
   "metadata": {},
   "source": [
    "#### 4.2 Maximumum score of students in all three subjects"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14db115f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "plt.figure(figsize=(18,8))\n",
    "plt.subplot(1, 4, 1)\n",
    "plt.title('MATH SCORES')\n",
    "sns.violinplot(y='math score',data=df,color='red',linewidth=3)\n",
    "plt.subplot(1, 4, 2)\n",
    "plt.title('READING SCORES')\n",
    "sns.violinplot(y='reading score',data=df,color='green',linewidth=3)\n",
    "plt.subplot(1, 4, 3)\n",
    "plt.title('WRITING SCORES')\n",
    "sns.violinplot(y='writing score',data=df,color='blue',linewidth=3)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66d1041f",
   "metadata": {},
   "source": [
    "#### Insights\n",
    "- From the above three plots its clearly visible that most of the students score in between 60-80 in Maths whereas in reading and writing most of them score from 50-80"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae77a33d",
   "metadata": {},
   "source": [
    "#### 4.3 Multivariate analysis using pieplot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ddf9ce3",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.rcParams['figure.figsize'] = (30, 12)\n",
    "\n",
    "plt.subplot(1, 5, 1)\n",
    "size = df['gender'].value_counts()\n",
    "labels = 'Female', 'Male'\n",
    "color = ['red','green']\n",
    "\n",
    "\n",
    "plt.pie(size, colors = color, labels = labels,autopct = '.%2f%%')\n",
    "plt.title('Gender', fontsize = 20)\n",
    "plt.axis('off')\n",
    "\n",
    "\n",
    "\n",
    "plt.subplot(1, 5, 2)\n",
    "size = df['race/ethnicity'].value_counts()\n",
    "labels = 'Group C', 'Group D','Group B','Group E','Group A'\n",
    "color = ['red', 'green', 'blue', 'cyan','orange']\n",
    "\n",
    "plt.pie(size, colors = color,labels = labels,autopct = '.%2f%%')\n",
    "plt.title('Race/Ethnicity', fontsize = 20)\n",
    "plt.axis('off')\n",
    "\n",
    "\n",
    "\n",
    "plt.subplot(1, 5, 3)\n",
    "size = df['lunch'].value_counts()\n",
    "labels = 'Standard', 'Free'\n",
    "color = ['red','green']\n",
    "\n",
    "plt.pie(size, colors = color,labels = labels,autopct = '.%2f%%')\n",
    "plt.title('Lunch', fontsize = 20)\n",
    "plt.axis('off')\n",
    "\n",
    "\n",
    "plt.subplot(1, 5, 4)\n",
    "size = df['test preparation course'].value_counts()\n",
    "labels = 'None', 'Completed'\n",
    "color = ['red','green']\n",
    "\n",
    "plt.pie(size, colors = color,labels = labels,autopct = '.%2f%%')\n",
    "plt.title('Test Course', fontsize = 20)\n",
    "plt.axis('off')\n",
    "\n",
    "\n",
    "plt.subplot(1, 5, 5)\n",
    "size = df['parental level of education'].value_counts()\n",
    "labels = 'Some College', \"Associate's Degree\",'High School','Some High School',\"Bachelor's Degree\",\"Master's Degree\"\n",
    "color = ['red', 'green', 'blue', 'cyan','orange','grey']\n",
    "\n",
    "plt.pie(size, colors = color,labels = labels,autopct = '.%2f%%')\n",
    "plt.title('Parental Education', fontsize = 20)\n",
    "plt.axis('off')\n",
    "\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.grid()\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e2d686a",
   "metadata": {},
   "source": [
    "#####  Insights\n",
    "- Number of Male and Female students is almost equal\n",
    "- Number students are greatest in Group C\n",
    "- Number of students who have standard lunch are greater\n",
    "- Number of students who have not enrolled in any test preparation course is greater\n",
    "- Number of students whose parental education is \"Some College\" is greater followed closely by \"Associate's Degree\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab008237",
   "metadata": {},
   "source": [
    "#### 4.4 Feature Wise Visualization\n",
    "#### 4.4.1 GENDER COLUMN\n",
    "- How is distribution of Gender ?\n",
    "- Is gender has any impact on student's performance ?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1a2c8f5",
   "metadata": {},
   "source": [
    "#### UNIVARIATE ANALYSIS ( How is distribution of Gender ? )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c435f53b",
   "metadata": {},
   "outputs": [],
   "source": [
    "f,ax=plt.subplots(1,2,figsize=(20,10))\n",
    "sns.countplot(x=df['gender'],data=df,palette ='bright',ax=ax[0],saturation=0.95)\n",
    "for container in ax[0].containers:\n",
    "    ax[0].bar_label(container,color='black',size=20)\n",
    "    \n",
    "plt.pie(x=df['gender'].value_counts(),labels=['Male','Female'],explode=[0,0.1],autopct='%1.1f%%',shadow=True,colors=['#ff4d4d','#ff8000'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cfb8c9b2",
   "metadata": {},
   "source": [
    "#### Insights \n",
    "- Gender has balanced data with female students are 518 (48%) and male students are 482 (52%) "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e440a3a5",
   "metadata": {},
   "source": [
    "#### BIVARIATE ANALYSIS ( Is gender has any impact on student's performance ? ) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "526d49f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "gender_group = df.groupby('gender').mean()\n",
    "gender_group"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b704f144",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(10, 8))\n",
    "\n",
    "X = ['Total Average','Math Average']\n",
    "\n",
    "\n",
    "female_scores = [gender_group['average'][0], gender_group['math score'][0]]\n",
    "male_scores = [gender_group['average'][1], gender_group['math score'][1]]\n",
    "\n",
    "X_axis = np.arange(len(X))\n",
    "  \n",
    "plt.bar(X_axis - 0.2, male_scores, 0.4, label = 'Male')\n",
    "plt.bar(X_axis + 0.2, female_scores, 0.4, label = 'Female')\n",
    "  \n",
    "plt.xticks(X_axis, X)\n",
    "plt.ylabel(\"Marks\")\n",
    "plt.title(\"Total average v/s Math average marks of both the genders\", fontweight='bold')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72fbab62",
   "metadata": {},
   "source": [
    "#### Insights \n",
    "- On an average females have a better overall score than men.\n",
    "- whereas males have scored higher in Maths."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a903c5c",
   "metadata": {},
   "source": [
    "#### 4.4.2 RACE/EHNICITY COLUMN\n",
    "- How is Group wise distribution ?\n",
    "- Is Race/Ehnicity has any impact on student's performance ?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "69fe557f",
   "metadata": {},
   "source": [
    "#### UNIVARIATE ANALYSIS ( How is Group wise distribution ?)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "acbc5c8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "f,ax=plt.subplots(1,2,figsize=(20,10))\n",
    "sns.countplot(x=df['race/ethnicity'],data=df,palette = 'bright',ax=ax[0],saturation=0.95)\n",
    "for container in ax[0].containers:\n",
    "    ax[0].bar_label(container,color='black',size=20)\n",
    "    \n",
    "plt.pie(x = df['race/ethnicity'].value_counts(),labels=df['race/ethnicity'].value_counts().index,explode=[0.1,0,0,0,0],autopct='%1.1f%%',shadow=True)\n",
    "plt.show()   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1762646a",
   "metadata": {},
   "source": [
    "#### Insights \n",
    "- Most of the student belonging from group C /group D.\n",
    "- Lowest number of students belong to groupA."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d3a3719",
   "metadata": {},
   "source": [
    "#### BIVARIATE ANALYSIS ( Is Race/Ehnicity has any impact on student's performance ? )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db261c61",
   "metadata": {},
   "outputs": [],
   "source": [
    "Group_data2=df.groupby('race/ethnicity')\n",
    "f,ax=plt.subplots(1,3,figsize=(20,8))\n",
    "sns.barplot(x=Group_data2['math score'].mean().index,y=Group_data2['math score'].mean().values,palette = 'mako',ax=ax[0])\n",
    "ax[0].set_title('Math score',color='#005ce6',size=20)\n",
    "\n",
    "for container in ax[0].containers:\n",
    "    ax[0].bar_label(container,color='black',size=15)\n",
    "\n",
    "sns.barplot(x=Group_data2['reading score'].mean().index,y=Group_data2['reading score'].mean().values,palette = 'flare',ax=ax[1])\n",
    "ax[1].set_title('Reading score',color='#005ce6',size=20)\n",
    "\n",
    "for container in ax[1].containers:\n",
    "    ax[1].bar_label(container,color='black',size=15)\n",
    "\n",
    "sns.barplot(x=Group_data2['writing score'].mean().index,y=Group_data2['writing score'].mean().values,palette = 'coolwarm',ax=ax[2])\n",
    "ax[2].set_title('Writing score',color='#005ce6',size=20)\n",
    "\n",
    "for container in ax[2].containers:\n",
    "    ax[2].bar_label(container,color='black',size=15)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e292ddd",
   "metadata": {},
   "source": [
    "#### Insights \n",
    "- Group E students have scored the highest marks. \n",
    "- Group A students have scored the lowest marks. \n",
    "- Students from a lower Socioeconomic status have a lower avg in all course subjects"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1409042e",
   "metadata": {},
   "source": [
    "#### 4.4.3 PARENTAL LEVEL OF EDUCATION COLUMN\n",
    "- What is educational background of student's parent ?\n",
    "- Is parental education has any impact on student's performance ?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38aca4fc",
   "metadata": {},
   "source": [
    "#### UNIVARIATE ANALYSIS ( What is educational background of student's parent ? )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c05ab987",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.rcParams['figure.figsize'] = (15, 9)\n",
    "plt.style.use('fivethirtyeight')\n",
    "sns.countplot(df['parental level of education'], palette = 'Blues')\n",
    "plt.title('Comparison of Parental Education', fontweight = 30, fontsize = 20)\n",
    "plt.xlabel('Degree')\n",
    "plt.ylabel('count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d351e1d",
   "metadata": {},
   "source": [
    "#### Insights \n",
    "- Largest number of parents are from some college."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f38ab41",
   "metadata": {},
   "source": [
    "#### BIVARIATE ANALYSIS ( Is parental education has any impact on student's performance ? )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "122b2581",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.groupby('parental level of education').agg('mean').plot(kind='barh',figsize=(10,10))\n",
    "plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58b3999d",
   "metadata": {},
   "source": [
    "#### Insights \n",
    "- The score of student whose parents possess master and bachelor level education are higher than others."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "079f4f29",
   "metadata": {},
   "source": [
    "#### 4.4.4 LUNCH COLUMN \n",
    "- Which type of lunch is most common amoung students ?\n",
    "- What is the effect of lunch type on test results?\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8584c755",
   "metadata": {},
   "source": [
    "#### UNIVARIATE ANALYSIS ( Which type of lunch is most common amoung students ? )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3a277e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.rcParams['figure.figsize'] = (15, 9)\n",
    "plt.style.use('seaborn-talk')\n",
    "sns.countplot(df['lunch'], palette = 'PuBu')\n",
    "plt.title('Comparison of different types of lunch', fontweight = 30, fontsize = 20)\n",
    "plt.xlabel('types of lunch')\n",
    "plt.ylabel('count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "332b0c50",
   "metadata": {},
   "source": [
    "#### Insights \n",
    "- Students being served Standard lunch was more than free lunch"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d75db26f",
   "metadata": {},
   "source": [
    "#### BIVARIATE ANALYSIS (  Is lunch type intake has any impact on student's performance ? )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "666babd5",
   "metadata": {},
   "outputs": [],
   "source": [
    "f,ax=plt.subplots(1,2,figsize=(20,8))\n",
    "sns.countplot(x=df['parental level of education'],data=df,palette = 'bright',hue='test preparation course',saturation=0.95,ax=ax[0])\n",
    "ax[0].set_title('Students vs test preparation course ',color='black',size=25)\n",
    "for container in ax[0].containers:\n",
    "    ax[0].bar_label(container,color='black',size=20)\n",
    "    \n",
    "sns.countplot(x=df['parental level of education'],data=df,palette = 'bright',hue='lunch',saturation=0.95,ax=ax[1])\n",
    "for container in ax[1].containers:\n",
    "    ax[1].bar_label(container,color='black',size=20)   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0677b04c",
   "metadata": {},
   "source": [
    "#### Insights \n",
    "- Students who get Standard Lunch tend to perform better than students who got free/reduced lunch"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "edd0ec29",
   "metadata": {},
   "source": [
    "#### 4.4.5 TEST PREPARATION COURSE COLUMN \n",
    "- Which type of lunch is most common amoung students ?\n",
    "- Is Test prepration course has any impact on student's performance ?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf8f65bd",
   "metadata": {},
   "source": [
    "#### BIVARIATE ANALYSIS ( Is Test prepration course has any impact on student's performance ? )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b08ed26",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(12,6))\n",
    "plt.subplot(2,2,1)\n",
    "sns.barplot (x=df['lunch'], y=df['math score'], hue=df['test preparation course'])\n",
    "plt.subplot(2,2,2)\n",
    "sns.barplot (x=df['lunch'], y=df['reading score'], hue=df['test preparation course'])\n",
    "plt.subplot(2,2,3)\n",
    "sns.barplot (x=df['lunch'], y=df['writing score'], hue=df['test preparation course'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5bab116e",
   "metadata": {},
   "source": [
    "#### Insights  \n",
    "- Students who have completed the Test Prepration Course have scores higher in all three categories than those who haven't taken the course"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4069d6e6",
   "metadata": {},
   "source": [
    "#### 4.4.6 CHECKING OUTLIERS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62a813a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.subplots(1,4,figsize=(16,5))\n",
    "plt.subplot(141)\n",
    "sns.boxplot(df['math score'],color='skyblue')\n",
    "plt.subplot(142)\n",
    "sns.boxplot(df['reading score'],color='hotpink')\n",
    "plt.subplot(143)\n",
    "sns.boxplot(df['writing score'],color='yellow')\n",
    "plt.subplot(144)\n",
    "sns.boxplot(df['average'],color='lightgreen')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "957e8bef",
   "metadata": {},
   "source": [
    "#### 4.4.7 MUTIVARIATE ANALYSIS USING PAIRPLOT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f09f746c",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.pairplot(df,hue = 'gender')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7991322",
   "metadata": {},
   "source": [
    "#### Insights\n",
    "- From the above plot it is clear that all the scores increase linearly with each other."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7e20716",
   "metadata": {},
   "source": [
    "### 5. Conclusions\n",
    "- Student's Performance is related with lunch, race, parental level education\n",
    "- Females lead in pass percentage and also are top-scorers\n",
    "- Student's Performance is not much related with test preparation course\n",
    "- Finishing preparation course is benefitial."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.0"
  },
  "vscode": {
   "interpreter": {
    "hash": "7f9dc718a552478e14f37d36e0ca2ac7de1ac15c04a40a415ea3abc3fe8a0a39"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `Notebook_Experiments/Model_Training.ipynb`
```
{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "92e48866",
   "metadata": {},
   "source": [
    "## Model Training"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25791a74",
   "metadata": {},
   "source": [
    "#### 1.1 Import Data and Required Packages\n",
    "##### Importing Pandas, Numpy, Matplotlib, Seaborn and Warings Library."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b080dfb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Basic Import\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt \n",
    "import seaborn as sns\n",
    "# Modelling\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "from sklearn.neighbors import KNeighborsRegressor\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor\n",
    "from sklearn.svm import SVR\n",
    "from sklearn.linear_model import LinearRegression, Ridge,Lasso\n",
    "from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error\n",
    "from sklearn.model_selection import RandomizedSearchCV\n",
    "from catboost import CatBoostRegressor\n",
    "from xgboost import XGBRegressor\n",
    "import warnings"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e45079ad",
   "metadata": {},
   "source": [
    "#### Import the CSV Data as Pandas DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e11c6255",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('data/stud.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20634923",
   "metadata": {},
   "source": [
    "#### Show Top 5 Records"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e7e412a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race_ethnicity</th>\n",
       "      <th>parental_level_of_education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test_preparation_course</th>\n",
       "      <th>math_score</th>\n",
       "      <th>reading_score</th>\n",
       "      <th>writing_score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>master's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>male</td>\n",
       "      <td>group A</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>male</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender race_ethnicity parental_level_of_education         lunch  \\\n",
       "0  female        group B           bachelor's degree      standard   \n",
       "1  female        group C                some college      standard   \n",
       "2  female        group B             master's degree      standard   \n",
       "3    male        group A          associate's degree  free/reduced   \n",
       "4    male        group C                some college      standard   \n",
       "\n",
       "  test_preparation_course  math_score  reading_score  writing_score  \n",
       "0                    none          72             72             74  \n",
       "1               completed          69             90             88  \n",
       "2                    none          90             95             93  \n",
       "3                    none          47             57             44  \n",
       "4                    none          76             78             75  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fbd32281",
   "metadata": {},
   "source": [
    "#### Preparing X and Y variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "56d72fde",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df.drop(columns=['math_score'],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cd613177",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race_ethnicity</th>\n",
       "      <th>parental_level_of_education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test_preparation_course</th>\n",
       "      <th>reading_score</th>\n",
       "      <th>writing_score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>master's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>male</td>\n",
       "      <td>group A</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>male</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender race_ethnicity parental_level_of_education         lunch  \\\n",
       "0  female        group B           bachelor's degree      standard   \n",
       "1  female        group C                some college      standard   \n",
       "2  female        group B             master's degree      standard   \n",
       "3    male        group A          associate's degree  free/reduced   \n",
       "4    male        group C                some college      standard   \n",
       "\n",
       "  test_preparation_course  reading_score  writing_score  \n",
       "0                    none             72             74  \n",
       "1               completed             90             88  \n",
       "2                    none             95             93  \n",
       "3                    none             57             44  \n",
       "4                    none             78             75  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f237ea14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Categories in 'gender' variable:      ['female' 'male']\n",
      "Categories in 'race_ethnicity' variable:   ['group B' 'group C' 'group A' 'group D' 'group E']\n",
      "Categories in'parental level of education' variable: [\"bachelor's degree\" 'some college' \"master's degree\" \"associate's degree\"\n",
      " 'high school' 'some high school']\n",
      "Categories in 'lunch' variable:      ['standard' 'free/reduced']\n",
      "Categories in 'test preparation course' variable:      ['none' 'completed']\n"
     ]
    }
   ],
   "source": [
    "print(\"Categories in 'gender' variable:     \",end=\" \" )\n",
    "print(df['gender'].unique())\n",
    "\n",
    "print(\"Categories in 'race_ethnicity' variable:  \",end=\" \")\n",
    "print(df['race_ethnicity'].unique())\n",
    "\n",
    "print(\"Categories in'parental level of education' variable:\",end=\" \" )\n",
    "print(df['parental_level_of_education'].unique())\n",
    "\n",
    "print(\"Categories in 'lunch' variable:     \",end=\" \" )\n",
    "print(df['lunch'].unique())\n",
    "\n",
    "print(\"Categories in 'test preparation course' variable:     \",end=\" \" )\n",
    "print(df['test_preparation_course'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "924b7f9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "y = df['math_score']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ffc69816",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      72\n",
       "1      69\n",
       "2      90\n",
       "3      47\n",
       "4      76\n",
       "       ..\n",
       "995    88\n",
       "996    62\n",
       "997    59\n",
       "998    68\n",
       "999    77\n",
       "Name: math_score, Length: 1000, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1e290fe3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create Column Transformer with 3 types of transformers\n",
    "num_features = X.select_dtypes(exclude=\"object\").columns\n",
    "cat_features = X.select_dtypes(include=\"object\").columns\n",
    "\n",
    "from sklearn.preprocessing import OneHotEncoder, StandardScaler\n",
    "from sklearn.compose import ColumnTransformer\n",
    "\n",
    "numeric_transformer = StandardScaler()\n",
    "oh_transformer = OneHotEncoder()\n",
    "\n",
    "preprocessor = ColumnTransformer(\n",
    "    [\n",
    "        (\"OneHotEncoder\", oh_transformer, cat_features),\n",
    "         (\"StandardScaler\", numeric_transformer, num_features),        \n",
    "    ]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9c68f99a",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = preprocessor.fit_transform(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "72459f1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1000, 19)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ed5c4e99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((800, 19), (200, 19))"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# separate dataset into train and test\n",
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)\n",
    "X_train.shape, X_test.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4cd80317",
   "metadata": {},
   "source": [
    "#### Create an Evaluate Function to give all metrics after model Training"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8c247bd0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def evaluate_model(true, predicted):\n",
    "    mae = mean_absolute_error(true, predicted)\n",
    "    mse = mean_squared_error(true, predicted)\n",
    "    rmse = np.sqrt(mean_squared_error(true, predicted))\n",
    "    r2_square = r2_score(true, predicted)\n",
    "    return mae, rmse, r2_square"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "79ccb8e7",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Linear Regression\n",
      "Model performance for Training set\n",
      "- Root Mean Squared Error: 5.3243\n",
      "- Mean Absolute Error: 4.2671\n",
      "- R2 Score: 0.8743\n",
      "----------------------------------\n",
      "Model performance for Test set\n",
      "- Root Mean Squared Error: 5.3960\n",
      "- Mean Absolute Error: 4.2158\n",
      "- R2 Score: 0.8803\n",
      "===================================\n",
      "\n",
      "\n",
      "Lasso\n",
      "Model performance for Training set\n",
      "- Root Mean Squared Error: 6.5938\n",
      "- Mean Absolute Error: 5.2063\n",
      "- R2 Score: 0.8071\n",
      "----------------------------------\n",
      "Model performance for Test set\n",
      "- Root Mean Squared Error: 6.5197\n",
      "- Mean Absolute Error: 5.1579\n",
      "- R2 Score: 0.8253\n",
      "===================================\n",
      "\n",
      "\n",
      "Ridge\n",
      "Model performance for Training set\n",
      "- Root Mean Squared Error: 5.3233\n",
      "- Mean Absolute Error: 4.2650\n",
      "- R2 Score: 0.8743\n",
      "----------------------------------\n",
      "Model performance for Test set\n",
      "- Root Mean Squared Error: 5.3904\n",
      "- Mean Absolute Error: 4.2111\n",
      "- R2 Score: 0.8806\n",
      "===================================\n",
      "\n",
      "\n",
      "K-Neighbors Regressor\n",
      "Model performance for Training set\n",
      "- Root Mean Squared Error: 5.7077\n",
      "- Mean Absolute Error: 4.5167\n",
      "- R2 Score: 0.8555\n",
      "----------------------------------\n",
      "Model performance for Test set\n",
      "- Root Mean Squared Error: 7.2530\n",
      "- Mean Absolute Error: 5.6210\n",
      "- R2 Score: 0.7838\n",
      "===================================\n",
      "\n",
      "\n",
      "Decision Tree\n",
      "Model performance for Training set\n",
      "- Root Mean Squared Error: 0.2795\n",
      "- Mean Absolute Error: 0.0187\n",
      "- R2 Score: 0.9997\n",
      "----------------------------------\n",
      "Model performance for Test set\n",
      "- Root Mean Squared Error: 7.6371\n",
      "- Mean Absolute Error: 6.0250\n",
      "- R2 Score: 0.7603\n",
      "===================================\n",
      "\n",
      "\n",
      "Random Forest Regressor\n",
      "Model performance for Training set\n",
      "- Root Mean Squared Error: 2.2851\n",
      "- Mean Absolute Error: 1.8253\n",
      "- R2 Score: 0.9768\n",
      "----------------------------------\n",
      "Model performance for Test set\n",
      "- Root Mean Squared Error: 6.0959\n",
      "- Mean Absolute Error: 4.7194\n",
      "- R2 Score: 0.8473\n",
      "===================================\n",
      "\n",
      "\n",
      "XGBRegressor\n",
      "Model performance for Training set\n",
      "- Root Mean Squared Error: 0.9087\n",
      "- Mean Absolute Error: 0.6148\n",
      "- R2 Score: 0.9963\n",
      "----------------------------------\n",
      "Model performance for Test set\n",
      "- Root Mean Squared Error: 6.5889\n",
      "- Mean Absolute Error: 5.0844\n",
      "- R2 Score: 0.8216\n",
      "===================================\n",
      "\n",
      "\n",
      "CatBoosting Regressor\n",
      "Model performance for Training set\n",
      "- Root Mean Squared Error: 3.0427\n",
      "- Mean Absolute Error: 2.4054\n",
      "- R2 Score: 0.9589\n",
      "----------------------------------\n",
      "Model performance for Test set\n",
      "- Root Mean Squared Error: 6.0086\n",
      "- Mean Absolute Error: 4.6125\n",
      "- R2 Score: 0.8516\n",
      "===================================\n",
      "\n",
      "\n",
      "AdaBoost Regressor\n",
      "Model performance for Training set\n",
      "- Root Mean Squared Error: 5.7843\n",
      "- Mean Absolute Error: 4.7564\n",
      "- R2 Score: 0.8516\n",
      "----------------------------------\n",
      "Model performance for Test set\n",
      "- Root Mean Squared Error: 6.0447\n",
      "- Mean Absolute Error: 4.6813\n",
      "- R2 Score: 0.8498\n",
      "===================================\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "models = {\n",
    "    \"Linear Regression\": LinearRegression(),\n",
    "    \"Lasso\": Lasso(),\n",
    "    \"Ridge\": Ridge(),\n",
    "    \"K-Neighbors Regressor\": KNeighborsRegressor(),\n",
    "    \"Decision Tree\": DecisionTreeRegressor(),\n",
    "    \"Random Forest Regressor\": RandomForestRegressor(),\n",
    "    \"XGBRegressor\": XGBRegressor(), \n",
    "    \"CatBoosting Regressor\": CatBoostRegressor(verbose=False),\n",
    "    \"AdaBoost Regressor\": AdaBoostRegressor()\n",
    "}\n",
    "model_list = []\n",
    "r2_list =[]\n",
    "\n",
    "for i in range(len(list(models))):\n",
    "    model = list(models.values())[i]\n",
    "    model.fit(X_train, y_train) # Train model\n",
    "\n",
    "    # Make predictions\n",
    "    y_train_pred = model.predict(X_train)\n",
    "    y_test_pred = model.predict(X_test)\n",
    "    \n",
    "    # Evaluate Train and Test dataset\n",
    "    model_train_mae , model_train_rmse, model_train_r2 = evaluate_model(y_train, y_train_pred)\n",
    "\n",
    "    model_test_mae , model_test_rmse, model_test_r2 = evaluate_model(y_test, y_test_pred)\n",
    "\n",
    "    \n",
    "    print(list(models.keys())[i])\n",
    "    model_list.append(list(models.keys())[i])\n",
    "    \n",
    "    print('Model performance for Training set')\n",
    "    print(\"- Root Mean Squared Error: {:.4f}\".format(model_train_rmse))\n",
    "    print(\"- Mean Absolute Error: {:.4f}\".format(model_train_mae))\n",
    "    print(\"- R2 Score: {:.4f}\".format(model_train_r2))\n",
    "\n",
    "    print('----------------------------------')\n",
    "    \n",
    "    print('Model performance for Test set')\n",
    "    print(\"- Root Mean Squared Error: {:.4f}\".format(model_test_rmse))\n",
    "    print(\"- Mean Absolute Error: {:.4f}\".format(model_test_mae))\n",
    "    print(\"- R2 Score: {:.4f}\".format(model_test_r2))\n",
    "    r2_list.append(model_test_r2)\n",
    "    \n",
    "    print('='*35)\n",
    "    print('\\n')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06480b5a",
   "metadata": {},
   "source": [
    "### Results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e0159e5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model Name</th>\n",
       "      <th>R2_Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Ridge</td>\n",
       "      <td>0.880593</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Linear Regression</td>\n",
       "      <td>0.880345</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>CatBoosting Regressor</td>\n",
       "      <td>0.851632</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>AdaBoost Regressor</td>\n",
       "      <td>0.849847</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Random Forest Regressor</td>\n",
       "      <td>0.847291</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Lasso</td>\n",
       "      <td>0.825320</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>XGBRegressor</td>\n",
       "      <td>0.821589</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>K-Neighbors Regressor</td>\n",
       "      <td>0.783813</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Decision Tree</td>\n",
       "      <td>0.760313</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Model Name  R2_Score\n",
       "2                    Ridge  0.880593\n",
       "0        Linear Regression  0.880345\n",
       "7    CatBoosting Regressor  0.851632\n",
       "8       AdaBoost Regressor  0.849847\n",
       "5  Random Forest Regressor  0.847291\n",
       "1                    Lasso  0.825320\n",
       "6             XGBRegressor  0.821589\n",
       "3    K-Neighbors Regressor  0.783813\n",
       "4            Decision Tree  0.760313"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(list(zip(model_list, r2_list)), columns=['Model Name', 'R2_Score']).sort_values(by=[\"R2_Score\"],ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "357a7c1c",
   "metadata": {},
   "source": [
    "## Linear Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "9a6ad559",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Accuracy of the model is 88.03\n"
     ]
    }
   ],
   "source": [
    "lin_model = LinearRegression(fit_intercept=True)\n",
    "lin_model = lin_model.fit(X_train, y_train)\n",
    "y_pred = lin_model.predict(X_test)\n",
    "score = r2_score(y_test, y_pred)*100\n",
    "print(\" Accuracy of the model is %.2f\" %score)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1d31453e",
   "metadata": {},
   "source": [
    "## Plot y_pred and y_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "eb557b0a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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1W9+8xsdOXJER44cMf2ZlZWVmjBhgtavX6+NGzeqR48eGjFihCorKyPyHQFET7NYDwBA07JkyRKNHz9ekjR8+HCVl5dr7dq1+s53vqN58+ZpzJgxmjNnjvv8q6++WpKUmZmp5ORktW7dWg6HI6jPHDJkiMfvixYtUps2bbR27Vp973vfC/MbAYglZmQARM3OnTtVVFSksWPHSpKaNWumH/3oR1qyZIkkadu2bRo6dKjln1tWVqaJEyeqR48estvtysjI0OnTp3XgwAHLPwtAdDEjAyBqlixZoosXL6pTp07uY4ZhKDU1VU899ZTS09ODvmZSUpJ7acrlwoULHr9PmDBBx48f1x/+8Ad17dpVqampysvL0/nz50P7IgDiBjMyAKLi4sWLevHFF/X73/9e27Ztc/9s375dnTp10ooVK3TVVVepoKDA5zVSUlJUU1PjcexrX/uaSktLPYKZbdu2eZyzYcMG3XPPPRoxYoSuuOIKpaam6tixY5Z+PwCxwYwMgKh46623dPLkSd11112y2+0er916661asmSJfve732no0KHq3r27xowZo4sXL+qdd97R/fffL6m2jsy6des0ZswYpaamqn379vrOd76j//znP/rtb3+r73//+1q9erXeffddZWRkuK/fo0cP/eUvf1G/fv1UUVGhe++9N6TZHwDxhxkZAFGxZMkS5efnNwhipNpA5uOPP1ZmZqZeeeUVvfnmm+rdu7eGDBmioqIi93m/+c1vtG/fPnXv3l1f+9rXJEm9evXSM888o6efflpXX321ioqK9Mtf/rLBZ588eVJ9+/bVj3/8Y91zzz3q0KFDZL8wgKiwGfUXlwEAABIEMzIAACBhEcgAAICERSADAAASFoEMAABIWAQyAAAgYRHIAACAhEUgAwAAEhaBDAAASFgEMgAAIGERyAAAgIRFIAMAABLW/w9Y9MBy40+TIwAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(y_test,y_pred);\n",
    "plt.xlabel('Actual');\n",
    "plt.ylabel('Predicted');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "1e707ec3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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gwcP4pZbbsHnn3+OyMjIYA+n3XI4HBg5ciQefvhhAMDw4cPx448/YtmyZZgxY0aQR9e+vPvuu3jrrbewcuVKDB48GNu2bcOCBQuQlpbG77oD4RQPgC5dusBisTRY1ZCXl4eUlJQgjar9mDdvHj7++GN8+eWX6NGjR/3xlJQU1NbWori42On1/N59k52djfz8fJxyyimwWq2wWq1Yv349nn76aVitViQnJ/N79oPU1FScdNJJTsdOPPFEHDhwAADqv0v+PdJyt99+O+68805MnToVQ4YMwfTp03Hrrbdi6dKlAPhdB4I332lKSgry8/OdnrfZbCgsLAzI984ABUB4eDhGjBiBdevW1R9zOBxYt24dxowZE8SRtW2apmHevHn44IMPkJWVhfT0dKfnR4wYgbCwMKfvfffu3Thw4AC/dx+ce+652LlzJ7Zt21Z/GzlyJKZNm1b/M7/nlhs7dmyDZfJ79uxB7969AQDp6elISUlx+p5LS0uxceNGfs8+qqyshNnsfHmyWCxwOBwA+F0Hgjff6ZgxY1BcXIzs7Oz612RlZcHhcGD06NH+H5Tfy27bqFWrVmkRERHaq6++qv3888/arFmztM6dO2u5ubnBHlqbdeONN2rx8fHaV199pR09erT+VllZWf+aOXPmaL169dKysrK0LVu2aGPGjNHGjBkTxFG3D8ZVPJrG79kfNm3apFmtVu2hhx7S9u7dq7311ltadHS09uabb9a/5pFHHtE6d+6s/fvf/9Z27NihXXLJJVz62gwzZszQunfvXr/MePXq1VqXLl20xYsX17+G37XvysrKtK1bt2pbt27VAGhPPPGEtnXrVi0nJ0fTNO++04kTJ2rDhw/XNm7cqH377bda//79ucy4NTzzzDNar169tPDwcO3UU0/Vvv/++2APqU0D4Pa2YsWK+tdUVVVpN910k5aQkKBFR0drl156qXb06NHgDbqdcA1Q+D37x0cffaSdfPLJWkREhDZo0CDtxRdfdHre4XBo9957r5acnKxFRERo5557rrZ79+4gjbbtKi0t1W655RatV69eWmRkpHbCCSdod999t1ZTU1P/Gn7Xvvvyyy/d/p08Y8YMTdO8+04LCgq0K664QouJidHi4uK0a6+9VisrKwvIeLmbMREREYUc1qAQERFRyGGAQkRERCGHAQoRERGFHAYoREREFHIYoBAREVHIYYBCREREIYcBChEREYUcBihEREQUchigEFFA/f777zCZTNi2bVuwh0JEbQgDFCLym2uuuQaTJk0K9jCIqB1ggEJEZFBXVxfsIRARGKAQdVjjxo3DzTffjAULFiAhIQHJyclYvnw5KioqcO211yI2Nhb9+vXDp59+CgCw2+2YOXMm0tPTERUVhYEDB+If//hH/fn+3//7f3jttdfw73//GyaTCSaTCV999VX98/v27cM555yD6OhoDB06FBs2bPBqnDk5OfjjH/+IhIQEdOrUCYMHD8Ynn3xS//xPP/2Eiy66CHFxcYiNjcWZZ56J3377DQDgcDjw17/+FT169EBERASGDRuGNWvW1L9XTT+98847OPvssxEZGYm33noLAPDSSy/hxBNPRGRkJAYNGoTnnnuu2d81ETVDQLYgJKKQd/bZZ2uxsbHaAw88oO3Zs0d74IEHNIvFop1//vnaiy++qO3Zs0e78cYbtaSkJK2iokKrra3V7rvvPm3z5s3avn37tDfffFOLjo7W3nnnHU3TZCv3P/3pT9rEiRO1o0ePakePHtVqamq0/fv3awC0QYMGaR9//LG2e/du7bLLLtN69+6t1dXVNTnOCy+8UDvvvPO0HTt2aL/99pv20UcfaevXr9c0TdMOHTqkJSYmapMnT9Y2b96s7d69W3vllVe0Xbt2aZqmaU888YQWFxenvf3229quXbu0xYsXa2FhYdqePXs0TdPqx9anTx/t/fff1/bt26cdOXJEe/PNN7XU1NT6Y++//76WmJiovfrqqwH6r0FErhigEHVQZ599tnbGGWfUP7bZbFqnTp206dOn1x87evSoBkDbsGGD23PMnTtXmzJlSv3jGTNmaJdcconTa1QQ8NJLL9Uf++mnnzQA2i+//NLkOIcMGaL9v//3/9w+t2TJEi09PV2rra11+3xaWpr20EMPOR0bNWqUdtNNNzmN7amnnnJ6Td++fbWVK1c6HXvggQe0MWPGNDleIvIPazCzN0QUXBkZGfU/WywWJCUlYciQIfXHkpOTAQD5+fkAgGeffRavvPIKDhw4gKqqKtTW1mLYsGE+f1Zqamr9eQcNGtTo++bPn48bb7wRn332GTIzMzFlypT6c23btg1nnnkmwsLCGryvtLQUR44cwdixY52Ojx07Ftu3b3c6NnLkyPqfKyoq8Ntvv2HmzJm44YYb6o/bbDbEx8d79bsSUcuxBoWoA3O9sJtMJqdjJpMJgNRyrFq1CrfddhtmzpyJzz77DNu2bcO1116L2tpanz/LeN6mXH/99di3bx+mT5+OnTt3YuTIkXjmmWcAAFFRUV59dlM6depU/3N5eTkAYPny5di2bVv97ccff8T333/vl88joqYxQCEir3z33Xc4/fTTcdNNN2H48OHo169ffTGqEh4eDrvd7vfP7tmzJ+bMmYPVq1dj0aJFWL58OQDJynzzzTduV97ExcUhLS0N3333XYPf46STTvL4WcnJyUhLS8O+ffvQr18/p1t6erp/fzEi8ohTPETklf79++P111/H2rVrkZ6ejjfeeAObN292umj36dMHa9euxe7du5GUlOSXKZEFCxbg/PPPx4ABA1BUVIQvv/wSJ554IgBg3rx5eOaZZzB16lQsWbIE8fHx+P7773Hqqadi4MCBuP3223H//fejb9++GDZsGFasWIFt27bVr9Tx5C9/+Qvmz5+P+Ph4TJw4ETU1NdiyZQuKioqwcOHCFv9ORNQ0BihE5JXZs2dj69at+POf/wyTyYQrrrgCN910U/0yZAC44YYb8NVXX2HkyJEoLy/Hl19+iT59+rToc+12O+bOnYtDhw4hLi4OEydOxJNPPgkASEpKQlZWFm6//XacffbZsFgsGDZsWH3dyfz581FSUoJFixYhPz8fJ510Ev7zn/+gf//+jX7m9ddfj+joaDz22GO4/fbb0alTJwwZMgQLFixo0e9CRN4zaZqmBXsQREREREasQSEiIqKQwwCFiILq/PPPR0xMjNvbww8/HOzhEVGQcIqHiILq8OHDqKqqcvtcYmIiEhMTW3lERBQKGKAQERFRyOEUDxEREYUcBihEREQUchigEBERUchhgEJEREQhhwEKERERhRwGKERERBRyGKAQERFRyGGAQkRERCHn/wPLz3prSnmp+QAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.regplot(x=y_test,y=y_pred,ci=None,color ='red');"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79c2fe28",
   "metadata": {},
   "source": [
    "#### Difference between Actual and Predicted Values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7c9a8b48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Actual Value</th>\n",
       "      <th>Predicted Value</th>\n",
       "      <th>Difference</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>521</th>\n",
       "      <td>91</td>\n",
       "      <td>76.507812</td>\n",
       "      <td>14.492188</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>737</th>\n",
       "      <td>53</td>\n",
       "      <td>58.953125</td>\n",
       "      <td>-5.953125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>740</th>\n",
       "      <td>80</td>\n",
       "      <td>76.960938</td>\n",
       "      <td>3.039062</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>660</th>\n",
       "      <td>74</td>\n",
       "      <td>76.757812</td>\n",
       "      <td>-2.757812</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>411</th>\n",
       "      <td>84</td>\n",
       "      <td>87.539062</td>\n",
       "      <td>-3.539062</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>408</th>\n",
       "      <td>52</td>\n",
       "      <td>43.546875</td>\n",
       "      <td>8.453125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>332</th>\n",
       "      <td>62</td>\n",
       "      <td>62.031250</td>\n",
       "      <td>-0.031250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>208</th>\n",
       "      <td>74</td>\n",
       "      <td>67.976562</td>\n",
       "      <td>6.023438</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>613</th>\n",
       "      <td>65</td>\n",
       "      <td>67.132812</td>\n",
       "      <td>-2.132812</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>78</th>\n",
       "      <td>61</td>\n",
       "      <td>62.492188</td>\n",
       "      <td>-1.492188</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>200 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Actual Value  Predicted Value  Difference\n",
       "521            91        76.507812   14.492188\n",
       "737            53        58.953125   -5.953125\n",
       "740            80        76.960938    3.039062\n",
       "660            74        76.757812   -2.757812\n",
       "411            84        87.539062   -3.539062\n",
       "..            ...              ...         ...\n",
       "408            52        43.546875    8.453125\n",
       "332            62        62.031250   -0.031250\n",
       "208            74        67.976562    6.023438\n",
       "613            65        67.132812   -2.132812\n",
       "78             61        62.492188   -1.492188\n",
       "\n",
       "[200 rows x 3 columns]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred_df=pd.DataFrame({'Actual Value':y_test,'Predicted Value':y_pred,'Difference':y_test-y_pred})\n",
    "pred_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3acf1fbc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `Notebook_Experiments/catboost_info/catboost_training.json`
```json
{
"meta":{"test_sets":[],"test_metrics":[],"learn_metrics":[{"best_value":"Min","name":"RMSE"}],"launch_mode":"Train","parameters":"","iteration_count":1000,"learn_sets":["learn"],"name":"experiment"},
"iterations":[
{"learn":[14.59871775],"iteration":0,"passed_time":0.147788617,"remaining_time":147.6408284},
{"learn":[14.22518863],"iteration":1,"passed_time":0.1487169599,"remaining_time":74.20976297},
{"learn":[13.8866124],"iteration":2,"passed_time":0.1495376472,"remaining_time":49.69634474},
{"learn":[13.52356875],"iteration":3,"passed_time":0.1503048824,"remaining_time":37.42591571},
{"learn":[13.18870211],"iteration":4,"passed_time":0.1511683207,"remaining_time":30.08249582},
{"learn":[12.9124226],"iteration":5,"passed_time":0.1521207779,"remaining_time":25.20134221},
{"learn":[12.60003351],"iteration":6,"passed_time":0.1530873544,"remaining_time":21.7165347},
{"learn":[12.32990573],"iteration":7,"passed_time":0.1540249243,"remaining_time":19.09909062},
{"learn":[12.0660619],"iteration":8,"passed_time":0.1548264651,"remaining_time":17.0481141},
{"learn":[11.77309809],"iteration":9,"passed_time":0.1556374338,"remaining_time":15.40810595},
{"learn":[11.49227636],"iteration":10,"passed_time":0.1563768659,"remaining_time":14.05970185},
{"learn":[11.26264833],"iteration":11,"passed_time":0.1571106773,"remaining_time":12.93544576},
{"learn":[11.04260393],"iteration":12,"passed_time":0.157963854,"remaining_time":11.99310184},
{"learn":[10.79916926],"iteration":13,"passed_time":0.1588334147,"remaining_time":11.18641049},
{"learn":[10.5541002],"iteration":14,"passed_time":0.1597001499,"remaining_time":10.48697651},
{"learn":[10.31918115],"iteration":15,"passed_time":0.160580411,"remaining_time":9.875695274},
{"learn":[10.10004441],"iteration":16,"passed_time":0.1613927222,"remaining_time":9.332296822},
{"learn":[9.894556723],"iteration":17,"passed_time":0.162112597,"remaining_time":8.844142792},
{"learn":[9.690174082],"iteration":18,"passed_time":0.1629316712,"remaining_time":8.412419445},
{"learn":[9.506034866],"iteration":19,"passed_time":0.1639871268,"remaining_time":8.035369216},
{"learn":[9.338524633],"iteration":20,"passed_time":0.1654205111,"remaining_time":7.711746683},
{"learn":[9.170203312],"iteration":21,"passed_time":0.1663705749,"remaining_time":7.395928283},
{"learn":[9.010299969],"iteration":22,"passed_time":0.167387711,"remaining_time":7.110338856},
{"learn":[8.843866678],"iteration":23,"passed_time":0.1682539253,"remaining_time":6.842326294},
{"learn":[8.690548059],"iteration":24,"passed_time":0.1690473619,"remaining_time":6.592847116},
{"learn":[8.555307687],"iteration":25,"passed_time":0.1698221215,"remaining_time":6.361797937},
{"learn":[8.413851302],"iteration":26,"passed_time":0.1708132784,"remaining_time":6.155604439},
{"learn":[8.29256019],"iteration":27,"passed_time":0.1717490655,"remaining_time":5.962146129},
{"learn":[8.162193833],"iteration":28,"passed_time":0.1725042176,"remaining_time":5.775917079},
{"learn":[8.040736294],"iteration":29,"passed_time":0.1732172693,"remaining_time":5.600691708},
{"learn":[7.921220278],"iteration":30,"passed_time":0.1740177569,"remaining_time":5.439458272},
{"learn":[7.809589039],"iteration":31,"passed_time":0.1748534027,"remaining_time":5.289315433},
{"learn":[7.699675801],"iteration":32,"passed_time":0.1756734188,"remaining_time":5.147763513},
{"learn":[7.60645267],"iteration":33,"passed_time":0.1764319273,"remaining_time":5.012742405},
{"learn":[7.498880302],"iteration":34,"passed_time":0.1771467624,"remaining_time":4.884189307},
{"learn":[7.401158744],"iteration":35,"passed_time":0.1779858148,"remaining_time":4.766064596},
{"learn":[7.306431077],"iteration":36,"passed_time":0.1787178328,"remaining_time":4.651493863},
{"learn":[7.223863468],"iteration":37,"passed_time":0.1794464242,"remaining_time":4.542827896},
{"learn":[7.143477682],"iteration":38,"passed_time":0.1802004241,"remaining_time":4.440323271},
{"learn":[7.062817131],"iteration":39,"passed_time":0.1809447255,"remaining_time":4.342673412},
{"learn":[6.990793435],"iteration":40,"passed_time":0.1818400453,"remaining_time":4.253283011},
{"learn":[6.931862224],"iteration":41,"passed_time":0.1828514984,"remaining_time":4.170755605},
{"learn":[6.858296558],"iteration":42,"passed_time":0.1840598517,"remaining_time":4.096401816},
{"learn":[6.786268161],"iteration":43,"passed_time":0.1849023191,"remaining_time":4.017423116},
{"learn":[6.717118549],"iteration":44,"passed_time":0.1857232669,"remaining_time":3.941460443},
{"learn":[6.652948106],"iteration":45,"passed_time":0.1866938605,"remaining_time":3.871868324},
{"learn":[6.589686076],"iteration":46,"passed_time":0.1874593323,"remaining_time":3.8010371},
{"learn":[6.531283097],"iteration":47,"passed_time":0.1882424278,"remaining_time":3.733474819},
{"learn":[6.471368031],"iteration":48,"passed_time":0.1890955471,"remaining_time":3.66999725},
{"learn":[6.416481395],"iteration":49,"passed_time":0.189875727,"remaining_time":3.607638813},
{"learn":[6.369870822],"iteration":50,"passed_time":0.1906159907,"remaining_time":3.546952454},
{"learn":[6.325678067],"iteration":51,"passed_time":0.1913317877,"remaining_time":3.488125668},
{"learn":[6.275766122],"iteration":52,"passed_time":0.1920481858,"remaining_time":3.43150249},
{"learn":[6.224773967],"iteration":53,"passed_time":0.1927579813,"remaining_time":3.376834265},
{"learn":[6.182249254],"iteration":54,"passed_time":0.193489338,"remaining_time":3.324498626},
{"learn":[6.139904173],"iteration":55,"passed_time":0.1941824717,"remaining_time":3.273361666},
{"learn":[6.100525536],"iteration":56,"passed_time":0.1948702351,"remaining_time":3.22390582},
{"learn":[6.062568564],"iteration":57,"passed_time":0.1956144764,"remaining_time":3.17704891},
{"learn":[6.030559288],"iteration":58,"passed_time":0.1965277256,"remaining_time":3.134450675},
{"learn":[5.997931376],"iteration":59,"passed_time":0.1974295828,"remaining_time":3.093063464},
{"learn":[5.964103835],"iteration":60,"passed_time":0.1981637649,"remaining_time":3.050422545},
{"learn":[5.933729724],"iteration":61,"passed_time":0.198891164,"remaining_time":3.009030836},
{"learn":[5.901932711],"iteration":62,"passed_time":0.1996641602,"remaining_time":2.969608224},
{"learn":[5.873727795],"iteration":63,"passed_time":0.2004325265,"remaining_time":2.931325699},
{"learn":[5.846485734],"iteration":64,"passed_time":0.2012452786,"remaining_time":2.89483593},
{"learn":[5.820630862],"iteration":65,"passed_time":0.2024793553,"remaining_time":2.865389665},
{"learn":[5.793646238],"iteration":66,"passed_time":0.203248424,"remaining_time":2.830310144},
{"learn":[5.765388646],"iteration":67,"passed_time":0.2040823166,"remaining_time":2.797128221},
{"learn":[5.747073912],"iteration":68,"passed_time":0.2048559339,"remaining_time":2.764070645},
{"learn":[5.722315217],"iteration":69,"passed_time":0.2056053652,"remaining_time":2.731614137},
{"learn":[5.699970599],"iteration":70,"passed_time":0.2064102637,"remaining_time":2.700776549},
{"learn":[5.682732647],"iteration":71,"passed_time":0.2072836817,"remaining_time":2.671656342},
{"learn":[5.663525791],"iteration":72,"passed_time":0.2080896108,"remaining_time":2.642453003},
{"learn":[5.642381613],"iteration":73,"passed_time":0.2090689797,"remaining_time":2.616187503},
{"learn":[5.621404779],"iteration":74,"passed_time":0.2098190521,"remaining_time":2.58776831},
{"learn":[5.602460129],"iteration":75,"passed_time":0.2106191,"remaining_time":2.560684848},
{"learn":[5.587337574],"iteration":76,"passed_time":0.2113198783,"remaining_time":2.533094126},
{"learn":[5.572393026],"iteration":77,"passed_time":0.2120937762,"remaining_time":2.507057201},
{"learn":[5.558425806],"iteration":78,"passed_time":0.2128829233,"remaining_time":2.481837625},
{"learn":[5.541518902],"iteration":79,"passed_time":0.2136914874,"remaining_time":2.457452106},
{"learn":[5.526157283],"iteration":80,"passed_time":0.214548985,"remaining_time":2.434203917},
{"learn":[5.511746977],"iteration":81,"passed_time":0.2153156692,"remaining_time":2.410485175},
{"learn":[5.504975022],"iteration":82,"passed_time":0.215770087,"remaining_time":2.383869515},
{"learn":[5.493980522],"iteration":83,"passed_time":0.2165325631,"remaining_time":2.361236045},
{"learn":[5.480745463],"iteration":84,"passed_time":0.2173293462,"remaining_time":2.339486491},
{"learn":[5.464052013],"iteration":85,"passed_time":0.218077174,"remaining_time":2.317703919},
{"learn":[5.449143727],"iteration":86,"passed_time":0.2189353873,"remaining_time":2.297563317},
{"learn":[5.438255432],"iteration":87,"passed_time":0.2197187834,"remaining_time":2.277085573},
{"learn":[5.425927931],"iteration":88,"passed_time":0.2205417908,"remaining_time":2.257455859},
{"learn":[5.412331217],"iteration":89,"passed_time":0.2214262398,"remaining_time":2.238865314},
{"learn":[5.400691499],"iteration":90,"passed_time":0.2222474081,"remaining_time":2.220031801},
{"learn":[5.391618744],"iteration":91,"passed_time":0.2229821412,"remaining_time":2.200736785},
{"learn":[5.380766572],"iteration":92,"passed_time":0.2236979582,"remaining_time":2.181656431},
{"learn":[5.372207183],"iteration":93,"passed_time":0.2244847095,"remaining_time":2.163650498},
{"learn":[5.362918837],"iteration":94,"passed_time":0.2254869335,"remaining_time":2.148059735},
{"learn":[5.348292324],"iteration":95,"passed_time":0.2263625958,"remaining_time":2.13158111},
{"learn":[5.339772295],"iteration":96,"passed_time":0.22746443,"remaining_time":2.117529694},
{"learn":[5.331515983],"iteration":97,"passed_time":0.2283758305,"remaining_time":2.101989787},
{"learn":[5.323861644],"iteration":98,"passed_time":0.2291391898,"remaining_time":2.08539808},
{"learn":[5.313277281],"iteration":99,"passed_time":0.2299235777,"remaining_time":2.069312199},
{"learn":[5.30685627],"iteration":100,"passed_time":0.2306782987,"remaining_time":2.053265253},
{"learn":[5.29652059],"iteration":101,"passed_time":0.2314369175,"remaining_time":2.03755247},
{"learn":[5.288350766],"iteration":102,"passed_time":0.2321533156,"remaining_time":2.02176237},
{"learn":[5.27993346],"iteration":103,"passed_time":0.2329002921,"remaining_time":2.006525594},
{"learn":[5.271789139],"iteration":104,"passed_time":0.2336971139,"remaining_time":1.991989685},
{"learn":[5.262684686],"iteration":105,"passed_time":0.2344194533,"remaining_time":1.977084823},
{"learn":[5.251619772],"iteration":106,"passed_time":0.2352034906,"remaining_time":1.962959973},
{"learn":[5.241012171],"iteration":107,"passed_time":0.2359309799,"remaining_time":1.948615131},
{"learn":[5.232684032],"iteration":108,"passed_time":0.2367573924,"remaining_time":1.935328777},
{"learn":[5.224267141],"iteration":109,"passed_time":0.237517985,"remaining_time":1.921736424},
{"learn":[5.216324968],"iteration":110,"passed_time":0.238511516,"remaining_time":1.910240881},
{"learn":[5.211102527],"iteration":111,"passed_time":0.2393026168,"remaining_time":1.897327891},
{"learn":[5.206364257],"iteration":112,"passed_time":0.2400754628,"remaining_time":1.884486155},
{"learn":[5.196937641],"iteration":113,"passed_time":0.2411054732,"remaining_time":1.873854818},
{"learn":[5.190746047],"iteration":114,"passed_time":0.2419453071,"remaining_time":1.861926928},
{"learn":[5.181885213],"iteration":115,"passed_time":0.2432315205,"remaining_time":1.853591932},
{"learn":[5.178293568],"iteration":116,"passed_time":0.2440268795,"remaining_time":1.841672945},
{"learn":[5.170991438],"iteration":117,"passed_time":0.245036718,"remaining_time":1.831545638},
{"learn":[5.166257212],"iteration":118,"passed_time":0.2457987733,"remaining_time":1.819737137},
{"learn":[5.161421246],"iteration":119,"passed_time":0.2466124271,"remaining_time":1.808491132},
{"learn":[5.158223542],"iteration":120,"passed_time":0.2474336254,"remaining_time":1.79747237},
{"learn":[5.15470988],"iteration":121,"passed_time":0.2479856196,"remaining_time":1.784683393},
{"learn":[5.146388143],"iteration":122,"passed_time":0.248760309,"remaining_time":1.773681228},
{"learn":[5.139529364],"iteration":123,"passed_time":0.2497158541,"remaining_time":1.764121679},
{"learn":[5.134276023],"iteration":124,"passed_time":0.2505001419,"remaining_time":1.753500993},
{"learn":[5.128536065],"iteration":125,"passed_time":0.2513259389,"remaining_time":1.74332437},
{"learn":[5.123300353],"iteration":126,"passed_time":0.251971071,"remaining_time":1.73205311},
{"learn":[5.116200518],"iteration":127,"passed_time":0.2527876504,"remaining_time":1.722115868},
{"learn":[5.108728704],"iteration":128,"passed_time":0.2536703561,"remaining_time":1.712766513},
{"learn":[5.104075866],"iteration":129,"passed_time":0.2546307502,"remaining_time":1.704067328},
{"learn":[5.100317606],"iteration":130,"passed_time":0.2553960417,"remaining_time":1.694192063},
{"learn":[5.095814182],"iteration":131,"passed_time":0.2561295826,"remaining_time":1.684246043},
{"learn":[5.092146915],"iteration":132,"passed_time":0.2570465263,"remaining_time":1.675634122},
{"learn":[5.085258329],"iteration":133,"passed_time":0.257894696,"remaining_time":1.666692588},
{"learn":[5.079219421],"iteration":134,"passed_time":0.2587798665,"remaining_time":1.658108033},
{"learn":[5.076476829],"iteration":135,"passed_time":0.2595322433,"remaining_time":1.648793075},
{"learn":[5.072133867],"iteration":136,"passed_time":0.2604301381,"remaining_time":1.640519775},
{"learn":[5.067031564],"iteration":137,"passed_time":0.2612236134,"remaining_time":1.631701121},
{"learn":[5.061358312],"iteration":138,"passed_time":0.2619581361,"remaining_time":1.622632771},
{"learn":[5.056759124],"iteration":139,"passed_time":0.2628859654,"remaining_time":1.614870931},
{"learn":[5.050254],"iteration":140,"passed_time":0.2638510084,"remaining_time":1.607432739},
{"learn":[5.048376474],"iteration":141,"passed_time":0.2644541102,"remaining_time":1.597898778},
{"learn":[5.042603751],"iteration":142,"passed_time":0.2652781138,"remaining_time":1.589813591},
{"learn":[5.037477349],"iteration":143,"passed_time":0.266138036,"remaining_time":1.58204277},
{"learn":[5.03230489],"iteration":144,"passed_time":0.2670491961,"remaining_time":1.574669398},
{"learn":[5.025976187],"iteration":145,"passed_time":0.2678052499,"remaining_time":1.566477284},
{"learn":[5.01952451],"iteration":146,"passed_time":0.268550443,"remaining_time":1.558323319},
{"learn":[5.017569424],"iteration":147,"passed_time":0.2693753484,"remaining_time":1.550728357},
{"learn":[5.008962367],"iteration":148,"passed_time":0.2701402992,"remaining_time":1.542881843},
{"learn":[5.003880266],"iteration":149,"passed_time":0.2709003607,"remaining_time":1.535102044},
{"learn":[4.996387564],"iteration":150,"passed_time":0.2716399331,"remaining_time":1.527300021},
{"learn":[4.993361683],"iteration":151,"passed_time":0.2725218774,"remaining_time":1.520385211},
{"learn":[4.99005752],"iteration":152,"passed_time":0.2733598677,"remaining_time":1.513305934},
{"learn":[4.986908764],"iteration":153,"passed_time":0.2742073453,"remaining_time":1.506359832},
{"learn":[4.985207175],"iteration":154,"passed_time":0.2750147573,"remaining_time":1.499273999},
{"learn":[4.979003494],"iteration":155,"passed_time":0.2758022411,"remaining_time":1.492160843},
{"learn":[4.973142217],"iteration":156,"passed_time":0.2766160152,"remaining_time":1.485269432},
{"learn":[4.967056696],"iteration":157,"passed_time":0.2774267836,"remaining_time":1.478438935},
{"learn":[4.961460696],"iteration":158,"passed_time":0.278296755,"remaining_time":1.471997301},
{"learn":[4.954240363],"iteration":159,"passed_time":0.2790295644,"remaining_time":1.464905213},
{"learn":[4.952320707],"iteration":160,"passed_time":0.2797041184,"remaining_time":1.457588542},
{"learn":[4.948337777],"iteration":161,"passed_time":0.2806609356,"remaining_time":1.451813976},
{"learn":[4.943228639],"iteration":162,"passed_time":0.2815577082,"remaining_time":1.445790195},
{"learn":[4.938545759],"iteration":163,"passed_time":0.2823394311,"remaining_time":1.439242466},
{"learn":[4.935330572],"iteration":164,"passed_time":0.2831691098,"remaining_time":1.433007313},
{"learn":[4.932051543],"iteration":165,"passed_time":0.2839556419,"remaining_time":1.426620514},
{"learn":[4.928964153],"iteration":166,"passed_time":0.284681478,"remaining_time":1.419998031},
{"learn":[4.922860227],"iteration":167,"passed_time":0.285434436,"remaining_time":1.413580064},
{"learn":[4.917668772],"iteration":168,"passed_time":0.2862342935,"remaining_time":1.407459751},
{"learn":[4.910365386],"iteration":169,"passed_time":0.2870128804,"remaining_time":1.401298181},
{"learn":[4.906457206],"iteration":170,"passed_time":0.2877249803,"remaining_time":1.394877244},
{"learn":[4.901996508],"iteration":171,"passed_time":0.2884750728,"remaining_time":1.388705583},
{"learn":[4.896816173],"iteration":172,"passed_time":0.2891446815,"remaining_time":1.382211859},
{"learn":[4.891123132],"iteration":173,"passed_time":0.2899159044,"remaining_time":1.376267454},
{"learn":[4.887630202],"iteration":174,"passed_time":0.2906485535,"remaining_time":1.370200324},
{"learn":[4.885259712],"iteration":175,"passed_time":0.2914395441,"remaining_time":1.364466956},
{"learn":[4.880659728],"iteration":176,"passed_time":0.2928303699,"remaining_time":1.3615785},
{"learn":[4.877299723],"iteration":177,"passed_time":0.2936529711,"remaining_time":1.356082822},
{"learn":[4.874038772],"iteration":178,"passed_time":0.2944008394,"remaining_time":1.350296587},
{"learn":[4.86943698],"iteration":179,"passed_time":0.295197266,"remaining_time":1.344787545},
{"learn":[4.861268711],"iteration":180,"passed_time":0.2959740595,"remaining_time":1.339241739},
{"learn":[4.858673056],"iteration":181,"passed_time":0.2968061786,"remaining_time":1.333997001},
{"learn":[4.854036207],"iteration":182,"passed_time":0.2975154331,"remaining_time":1.328251961},
{"learn":[4.85130244],"iteration":183,"passed_time":0.2982395059,"remaining_time":1.322627374},
{"learn":[4.847510084],"iteration":184,"passed_time":0.2991386564,"remaining_time":1.317827054},
{"learn":[4.845691673],"iteration":185,"passed_time":0.2999663171,"remaining_time":1.312755818},
{"learn":[4.842058646],"iteration":186,"passed_time":0.3007295646,"remaining_time":1.307449925},
{"learn":[4.838623675],"iteration":187,"passed_time":0.3015070795,"remaining_time":1.302253982},
{"learn":[4.834602161],"iteration":188,"passed_time":0.3023154733,"remaining_time":1.297237295},
{"learn":[4.830858976],"iteration":189,"passed_time":0.3031658874,"remaining_time":1.292444046},
{"learn":[4.827590511],"iteration":190,"passed_time":0.3040415797,"remaining_time":1.287799152},
{"learn":[4.822246226],"iteration":191,"passed_time":0.3047967118,"remaining_time":1.282686162},
{"learn":[4.816686395],"iteration":192,"passed_time":0.3055930325,"remaining_time":1.277790556},
{"learn":[4.814797121],"iteration":193,"passed_time":0.3064245104,"remaining_time":1.273083275},
{"learn":[4.811639392],"iteration":194,"passed_time":0.3073000413,"remaining_time":1.268597606},
{"learn":[4.804813432],"iteration":195,"passed_time":0.3083467637,"remaining_time":1.26485101},
{"learn":[4.80251613],"iteration":196,"passed_time":0.3091970238,"remaining_time":1.260331016},
{"learn":[4.800087884],"iteration":197,"passed_time":0.3099049059,"remaining_time":1.255271387},
{"learn":[4.794773135],"iteration":198,"passed_time":0.3106133989,"remaining_time":1.250257952},
{"learn":[4.791664833],"iteration":199,"passed_time":0.3113942501,"remaining_time":1.245577001},
{"learn":[4.785989873],"iteration":200,"passed_time":0.3123012623,"remaining_time":1.241436361},
{"learn":[4.782387142],"iteration":201,"passed_time":0.3131308781,"remaining_time":1.237021984},
{"learn":[4.778623704],"iteration":202,"passed_time":0.3138946652,"remaining_time":1.232384474},
{"learn":[4.775772178],"iteration":203,"passed_time":0.3148198031,"remaining_time":1.228414526},
{"learn":[4.77023101],"iteration":204,"passed_time":0.3157363177,"remaining_time":1.224440842},
{"learn":[4.764496689],"iteration":205,"passed_time":0.3164919909,"remaining_time":1.219876897},
{"learn":[4.763138716],"iteration":206,"passed_time":0.3172794246,"remaining_time":1.215471419},
{"learn":[4.758053283],"iteration":207,"passed_time":0.3180632315,"remaining_time":1.21108692},
{"learn":[4.755063788],"iteration":208,"passed_time":0.3188337329,"remaining_time":1.20668652},
{"learn":[4.752465267],"iteration":209,"passed_time":0.3196904691,"remaining_time":1.202645098},
{"learn":[4.748067377],"iteration":210,"passed_time":0.3203951448,"remaining_time":1.198065257},
{"learn":[4.744163298],"iteration":211,"passed_time":0.3210719127,"remaining_time":1.193418241},
{"learn":[4.736670896],"iteration":212,"passed_time":0.3219631352,"remaining_time":1.18960088},
{"learn":[4.73349255],"iteration":213,"passed_time":0.3228417927,"remaining_time":1.185764715},
{"learn":[4.731864595],"iteration":214,"passed_time":0.3236558673,"remaining_time":1.18172026},
{"learn":[4.728398311],"iteration":215,"passed_time":0.3243920432,"remaining_time":1.177422972},
{"learn":[4.723865975],"iteration":216,"passed_time":0.3252252244,"remaining_time":1.173508528},
{"learn":[4.723483365],"iteration":217,"passed_time":0.3259483554,"remaining_time":1.169227587},
{"learn":[4.72095416],"iteration":218,"passed_time":0.3267474815,"remaining_time":1.165250151},
{"learn":[4.716173382],"iteration":219,"passed_time":0.3275684877,"remaining_time":1.161379183},
{"learn":[4.710563974],"iteration":220,"passed_time":0.328347866,"remaining_time":1.157389084},
{"learn":[4.707160263],"iteration":221,"passed_time":0.3291304806,"remaining_time":1.153439252},
{"learn":[4.70408351],"iteration":222,"passed_time":0.3298486521,"remaining_time":1.149293286},
{"learn":[4.702501831],"iteration":223,"passed_time":0.3306110538,"remaining_time":1.145331151},
{"learn":[4.700269738],"iteration":224,"passed_time":0.3314669727,"remaining_time":1.141719573},
{"learn":[4.695346302],"iteration":225,"passed_time":0.3322176119,"remaining_time":1.137771821},
{"learn":[4.689769299],"iteration":226,"passed_time":0.3329602301,"remaining_time":1.133824925},
{"learn":[4.687919514],"iteration":227,"passed_time":0.333801481,"remaining_time":1.130240102},
{"learn":[4.682982074],"iteration":228,"passed_time":0.3345507318,"remaining_time":1.126369494},
{"learn":[4.679578702],"iteration":229,"passed_time":0.3352908052,"remaining_time":1.122495304},
{"learn":[4.675751423],"iteration":230,"passed_time":0.3362817734,"remaining_time":1.119483479},
{"learn":[4.672710726],"iteration":231,"passed_time":0.3371914649,"remaining_time":1.116220022},
{"learn":[4.6690533],"iteration":232,"passed_time":0.3380901211,"remaining_time":1.112940442},
{"learn":[4.667595702],"iteration":233,"passed_time":0.3389268791,"remaining_time":1.109478587},
{"learn":[4.664241291],"iteration":234,"passed_time":0.3396826925,"remaining_time":1.105775573},
{"learn":[4.662246999],"iteration":235,"passed_time":0.3404737532,"remaining_time":1.102211642},
{"learn":[4.658668443],"iteration":236,"passed_time":0.3412667275,"remaining_time":1.098677271},
{"learn":[4.658017572],"iteration":237,"passed_time":0.341960803,"remaining_time":1.094849294},
{"learn":[4.657656705],"iteration":238,"passed_time":0.3426914684,"remaining_time":1.091164048},
{"learn":[4.653242871],"iteration":239,"passed_time":0.3434128561,"remaining_time":1.087474044},
{"learn":[4.6507302],"iteration":240,"passed_time":0.3443522844,"remaining_time":1.084495369},
{"learn":[4.647671336],"iteration":241,"passed_time":0.3451516367,"remaining_time":1.081094796},
{"learn":[4.645506007],"iteration":242,"passed_time":0.346004753,"remaining_time":1.077883119},
{"learn":[4.641297906],"iteration":243,"passed_time":0.3467694534,"remaining_time":1.074416831},
{"learn":[4.63798107],"iteration":244,"passed_time":0.3475451047,"remaining_time":1.071006343},
{"learn":[4.635062318],"iteration":245,"passed_time":0.348383158,"remaining_time":1.067808541},
{"learn":[4.631606017],"iteration":246,"passed_time":0.3492768647,"remaining_time":1.064799511},
{"learn":[4.630215494],"iteration":247,"passed_time":0.3500890558,"remaining_time":1.061560363},
{"learn":[4.62729814],"iteration":248,"passed_time":0.3508565815,"remaining_time":1.058205995},
{"learn":[4.624691756],"iteration":249,"passed_time":0.3516125996,"remaining_time":1.054837799},
{"learn":[4.621840053],"iteration":250,"passed_time":0.352358454,"remaining_time":1.051460088},
{"learn":[4.619602091],"iteration":251,"passed_time":0.3533196253,"remaining_time":1.04874238},
{"learn":[4.613584029],"iteration":252,"passed_time":0.354126917,"remaining_time":1.045584217},
{"learn":[4.6119388],"iteration":253,"passed_time":0.3548592756,"remaining_time":1.042224487},
{"learn":[4.60870702],"iteration":254,"passed_time":0.3557118237,"remaining_time":1.039236505},
{"learn":[4.604771557],"iteration":255,"passed_time":0.3564376699,"remaining_time":1.035896978},
{"learn":[4.604231277],"iteration":256,"passed_time":0.3572088927,"remaining_time":1.032708978},
{"learn":[4.600750354],"iteration":257,"passed_time":0.357907646,"remaining_time":1.029331292},
{"learn":[4.596488253],"iteration":258,"passed_time":0.3586438319,"remaining_time":1.026081388},
{"learn":[4.59470784],"iteration":259,"passed_time":0.3593692072,"remaining_time":1.022820051},
{"learn":[4.588818005],"iteration":260,"passed_time":0.3600992113,"remaining_time":1.019591253},
{"learn":[4.585054174],"iteration":261,"passed_time":0.360796022,"remaining_time":1.016288031},
{"learn":[4.581471435],"iteration":262,"passed_time":0.36152281,"remaining_time":1.013088635},
{"learn":[4.577555199],"iteration":263,"passed_time":0.3622576132,"remaining_time":1.009930316},
{"learn":[4.57457145],"iteration":264,"passed_time":0.3630693434,"remaining_time":1.007003651},
{"learn":[4.573029224],"iteration":265,"passed_time":0.3637876352,"remaining_time":1.003835053},
{"learn":[4.571326203],"iteration":266,"passed_time":0.3645330888,"remaining_time":1.000759379},
{"learn":[4.571019224],"iteration":267,"passed_time":0.3652850849,"remaining_time":0.9977189632},
{"learn":[4.565766631],"iteration":268,"passed_time":0.3663115852,"remaining_time":0.9954415197},
{"learn":[4.563383471],"iteration":269,"passed_time":0.3671762766,"remaining_time":0.9927358588},
{"learn":[4.558165805],"iteration":270,"passed_time":0.3680717667,"remaining_time":0.9901266344},
{"learn":[4.55629209],"iteration":271,"passed_time":0.3689485311,"remaining_time":0.987479892},
{"learn":[4.549383848],"iteration":272,"passed_time":0.3697968305,"remaining_time":0.9847703142},
{"learn":[4.546227503],"iteration":273,"passed_time":0.3706082701,"remaining_time":0.9819766574},
{"learn":[4.540620977],"iteration":274,"passed_time":0.371374283,"remaining_time":0.9790776552},
{"learn":[4.532898237],"iteration":275,"passed_time":0.372095851,"remaining_time":0.9760775222},
{"learn":[4.529757367],"iteration":276,"passed_time":0.3728391405,"remaining_time":0.9731505364},
{"learn":[4.52579294],"iteration":277,"passed_time":0.3736227069,"remaining_time":0.9703438647},
{"learn":[4.521572155],"iteration":278,"passed_time":0.3743912446,"remaining_time":0.9675128579},
{"learn":[4.518818099],"iteration":279,"passed_time":0.3751662146,"remaining_time":0.9647131232},
{"learn":[4.514012334],"iteration":280,"passed_time":0.3764282948,"remaining_time":0.9631741778},
{"learn":[4.508331416],"iteration":281,"passed_time":0.3772623476,"remaining_time":0.9605473957},
{"learn":[4.506038537],"iteration":282,"passed_time":0.3779910492,"remaining_time":0.9576663686},
{"learn":[4.505805643],"iteration":283,"passed_time":0.3787215543,"remaining_time":0.9548050454},
{"learn":[4.501550352],"iteration":284,"passed_time":0.3795847428,"remaining_time":0.9522915476},
{"learn":[4.494692643],"iteration":285,"passed_time":0.380346778,"remaining_time":0.9495370613},
{"learn":[4.489330245],"iteration":286,"passed_time":0.3810700092,"remaining_time":0.9467000577},
{"learn":[4.484826955],"iteration":287,"passed_time":0.3818685588,"remaining_time":0.944063937},
{"learn":[4.478285428],"iteration":288,"passed_time":0.3826448212,"remaining_time":0.9413857021},
{"learn":[4.475311671],"iteration":289,"passed_time":0.3833944128,"remaining_time":0.9386552864},
{"learn":[4.471581298],"iteration":290,"passed_time":0.3841237456,"remaining_time":0.9358891258},
{"learn":[4.469164956],"iteration":291,"passed_time":0.3849725408,"remaining_time":0.9334265716},
{"learn":[4.462068024],"iteration":292,"passed_time":0.3857947124,"remaining_time":0.9309107906},
{"learn":[4.458540976],"iteration":293,"passed_time":0.3865640015,"remaining_time":0.9282795411},
{"learn":[4.455757458],"iteration":294,"passed_time":0.3873314772,"remaining_time":0.9256565811},
{"learn":[4.453027414],"iteration":295,"passed_time":0.3881573343,"remaining_time":0.9231850114},
{"learn":[4.450659338],"iteration":296,"passed_time":0.3889328353,"remaining_time":0.9206053308},
{"learn":[4.444696901],"iteration":297,"passed_time":0.3897666377,"remaining_time":0.9181750995},
{"learn":[4.442052813],"iteration":298,"passed_time":0.3906274058,"remaining_time":0.9158187674},
{"learn":[4.440036756],"iteration":299,"passed_time":0.3914985852,"remaining_time":0.9134966989},
{"learn":[4.435017051],"iteration":300,"passed_time":0.3923664125,"remaining_time":0.9111764863},
{"learn":[4.429962125],"iteration":301,"passed_time":0.3931744557,"remaining_time":0.9087277154},
{"learn":[4.427666256],"iteration":302,"passed_time":0.3940276439,"remaining_time":0.9063936231},
{"learn":[4.425030004],"iteration":303,"passed_time":0.3947598422,"remaining_time":0.9037922703},
{"learn":[4.422588771],"iteration":304,"passed_time":0.3954798171,"remaining_time":0.901175321},
{"learn":[4.418936667],"iteration":305,"passed_time":0.3963403305,"remaining_time":0.8988895077},
{"learn":[4.416887976],"iteration":306,"passed_time":0.3971110023,"remaining_time":0.8964101777},
{"learn":[4.413773354],"iteration":307,"passed_time":0.3981740223,"remaining_time":0.8945987775},
{"learn":[4.411129391],"iteration":308,"passed_time":0.3992413922,"remaining_time":0.8928019481},
{"learn":[4.40850819],"iteration":309,"passed_time":0.4003065449,"remaining_time":0.8910048902},
{"learn":[4.404880292],"iteration":310,"passed_time":0.4010488425,"remaining_time":0.8884972748},
{"learn":[4.404593827],"iteration":311,"passed_time":0.4020753929,"remaining_time":0.8866277895},
{"learn":[4.402139942],"iteration":312,"passed_time":0.4030312684,"remaining_time":0.8846085666},
{"learn":[4.400284725],"iteration":313,"passed_time":0.4038192832,"remaining_time":0.8822293895},
{"learn":[4.395805521],"iteration":314,"passed_time":0.4045203721,"remaining_time":0.8796712854},
{"learn":[4.392838833],"iteration":315,"passed_time":0.405269082,"remaining_time":0.8772280129},
{"learn":[4.389213061],"iteration":316,"passed_time":0.4060454346,"remaining_time":0.87485499},
{"learn":[4.3861981],"iteration":317,"passed_time":0.4067795265,"remaining_time":0.8724013744},
{"learn":[4.385054234],"iteration":318,"passed_time":0.4074907247,"remaining_time":0.8699096662},
{"learn":[4.379364607],"iteration":319,"passed_time":0.4082202579,"remaining_time":0.867468048},
{"learn":[4.378387619],"iteration":320,"passed_time":0.4089789877,"remaining_time":0.8650988557},
{"learn":[4.375816727],"iteration":321,"passed_time":0.409860841,"remaining_time":0.8629989136},
{"learn":[4.374600202],"iteration":322,"passed_time":0.4106605582,"remaining_time":0.8607343588},
{"learn":[4.37098897],"iteration":323,"passed_time":0.4114501261,"remaining_time":0.8584576704},
{"learn":[4.367418484],"iteration":324,"passed_time":0.4122517269,"remaining_time":0.8562151251},
{"learn":[4.363584638],"iteration":325,"passed_time":0.4130324879,"remaining_time":0.853938334},
{"learn":[4.360770706],"iteration":326,"passed_time":0.4137359213,"remaining_time":0.8515115445},
{"learn":[4.358675808],"iteration":327,"passed_time":0.4144993693,"remaining_time":0.84921822},
{"learn":[4.354228195],"iteration":328,"passed_time":0.4152563959,"remaining_time":0.8469210992},
{"learn":[4.353773425],"iteration":329,"passed_time":0.4161725054,"remaining_time":0.8449562988},
{"learn":[4.351648009],"iteration":330,"passed_time":0.416897029,"remaining_time":0.8426106115},
{"learn":[4.348209927],"iteration":331,"passed_time":0.4177982046,"remaining_time":0.8406301225},
{"learn":[4.345852733],"iteration":332,"passed_time":0.4186058269,"remaining_time":0.8384687284},
{"learn":[4.34237339],"iteration":333,"passed_time":0.4195149388,"remaining_time":0.8365178121},
{"learn":[4.340814362],"iteration":334,"passed_time":0.4202892475,"remaining_time":0.8343055212},
{"learn":[4.339707068],"iteration":335,"passed_time":0.420985407,"remaining_time":0.8319473519},
{"learn":[4.335430786],"iteration":336,"passed_time":0.4217523917,"remaining_time":0.8297383849},
{"learn":[4.33521887],"iteration":337,"passed_time":0.42245838,"remaining_time":0.8274184838},
{"learn":[4.328507238],"iteration":338,"passed_time":0.4232242514,"remaining_time":0.8252248678},
{"learn":[4.326140732],"iteration":339,"passed_time":0.4240006642,"remaining_time":0.8230601128},
{"learn":[4.323785636],"iteration":340,"passed_time":0.4246837988,"remaining_time":0.8207232357},
{"learn":[4.320632534],"iteration":341,"passed_time":0.4254031024,"remaining_time":0.8184656181},
{"learn":[4.31973724],"iteration":342,"passed_time":0.4261365631,"remaining_time":0.8162440874},
{"learn":[4.318000924],"iteration":343,"passed_time":0.4268667075,"remaining_time":0.8140248841},
{"learn":[4.312713628],"iteration":344,"passed_time":0.4276745812,"remaining_time":0.811961886},
{"learn":[4.308220789],"iteration":345,"passed_time":0.4284998578,"remaining_time":0.8099390376},
{"learn":[4.305890947],"iteration":346,"passed_time":0.4297618399,"remaining_time":0.8087449033},
{"learn":[4.305137856],"iteration":347,"passed_time":0.4308542252,"remaining_time":0.8072326287},
{"learn":[4.304787172],"iteration":348,"passed_time":0.431719187,"remaining_time":0.8052985408},
{"learn":[4.30350134],"iteration":349,"passed_time":0.4326485418,"remaining_time":0.8034901491},
{"learn":[4.30293809],"iteration":350,"passed_time":0.4335106582,"remaining_time":0.8015624421},
{"learn":[4.299548459],"iteration":351,"passed_time":0.4342318154,"remaining_time":0.7993812966},
{"learn":[4.294768408],"iteration":352,"passed_time":0.4349700352,"remaining_time":0.7972396963},
{"learn":[4.294581479],"iteration":353,"passed_time":0.435675753,"remaining_time":0.795046713},
{"learn":[4.292551604],"iteration":354,"passed_time":0.4365632579,"remaining_time":0.7931923981},
{"learn":[4.288628894],"iteration":355,"passed_time":0.4373186805,"remaining_time":0.7911045793},
{"learn":[4.287802767],"iteration":356,"passed_time":0.4380109926,"remaining_time":0.7889105554},
{"learn":[4.284566905],"iteration":357,"passed_time":0.4387552339,"remaining_time":0.7868180452},
{"learn":[4.27890232],"iteration":358,"passed_time":0.4395193732,"remaining_time":0.7847685745},
{"learn":[4.276938023],"iteration":359,"passed_time":0.4404345123,"remaining_time":0.7829946886},
{"learn":[4.273425094],"iteration":360,"passed_time":0.4412428961,"remaining_time":0.7810365945},
{"learn":[4.269726505],"iteration":361,"passed_time":0.4420011041,"remaining_time":0.778996421},
{"learn":[4.265565857],"iteration":362,"passed_time":0.4427088457,"remaining_time":0.7768747512},
{"learn":[4.262117173],"iteration":363,"passed_time":0.4434988137,"remaining_time":0.7749045207},
{"learn":[4.259185148],"iteration":364,"passed_time":0.4442192195,"remaining_time":0.772819738},
{"learn":[4.257668507],"iteration":365,"passed_time":0.445055145,"remaining_time":0.770942519},
{"learn":[4.253432436],"iteration":366,"passed_time":0.4458880657,"remaining_time":0.7690657918},
{"learn":[4.250216667],"iteration":367,"passed_time":0.4468771345,"remaining_time":0.767462905},
{"learn":[4.24514828],"iteration":368,"passed_time":0.4476495797,"remaining_time":0.7654929127},
{"learn":[4.244015772],"iteration":369,"passed_time":0.4488341118,"remaining_time":0.7642310553},
{"learn":[4.240329192],"iteration":370,"passed_time":0.4496919901,"remaining_time":0.7624158},
{"learn":[4.236718014],"iteration":371,"passed_time":0.4505570522,"remaining_time":0.7606178193},
{"learn":[4.233495944],"iteration":372,"passed_time":0.4514013445,"remaining_time":0.7587899277},
{"learn":[4.230357491],"iteration":373,"passed_time":0.4521516989,"remaining_time":0.7568100629},
{"learn":[4.227381215],"iteration":374,"passed_time":0.4532157095,"remaining_time":0.7553595158},
{"learn":[4.226169067],"iteration":375,"passed_time":0.4539711822,"remaining_time":0.7533989833},
{"learn":[4.225963861],"iteration":376,"passed_time":0.4548309642,"remaining_time":0.7516172167},
{"learn":[4.224346548],"iteration":377,"passed_time":0.4556542164,"remaining_time":0.7497802185},
{"learn":[4.222595381],"iteration":378,"passed_time":0.4563927367,"remaining_time":0.7478097349},
{"learn":[4.219700938],"iteration":379,"passed_time":0.4572282323,"remaining_time":0.746003958},
{"learn":[4.216356207],"iteration":380,"passed_time":0.4579486882,"remaining_time":0.7440163727},
{"learn":[4.214326494],"iteration":381,"passed_time":0.4587174263,"remaining_time":0.7421135325},
{"learn":[4.212901398],"iteration":382,"passed_time":0.4595204698,"remaining_time":0.7402718796},
{"learn":[4.211331091],"iteration":383,"passed_time":0.4605080258,"remaining_time":0.7387316247},
{"learn":[4.208624791],"iteration":384,"passed_time":0.4613801113,"remaining_time":0.7370097881},
{"learn":[4.204659106],"iteration":385,"passed_time":0.4622594706,"remaining_time":0.7353039247},
{"learn":[4.202968852],"iteration":386,"passed_time":0.462976029,"remaining_time":0.7333444594},
{"learn":[4.197261935],"iteration":387,"passed_time":0.46369391,"remaining_time":0.7313934869},
{"learn":[4.196934403],"iteration":388,"passed_time":0.4643487405,"remaining_time":0.7293498212},
{"learn":[4.192479929],"iteration":389,"passed_time":0.4650516529,"remaining_time":0.7273884827},
{"learn":[4.190243116],"iteration":390,"passed_time":0.4657637127,"remaining_time":0.7254478288},
{"learn":[4.185852431],"iteration":391,"passed_time":0.4665167709,"remaining_time":0.7235770324},
{"learn":[4.180967944],"iteration":392,"passed_time":0.4674412063,"remaining_time":0.7219766214},
{"learn":[4.178283162],"iteration":393,"passed_time":0.4682845368,"remaining_time":0.7202548967},
{"learn":[4.176341157],"iteration":394,"passed_time":0.4691001945,"remaining_time":0.7184952346},
{"learn":[4.176041504],"iteration":395,"passed_time":0.4699588042,"remaining_time":0.7168058529},
{"learn":[4.175564513],"iteration":396,"passed_time":0.4706888083,"remaining_time":0.7149253184},
{"learn":[4.170830274],"iteration":397,"passed_time":0.4714175801,"remaining_time":0.7130487015},
{"learn":[4.167804808],"iteration":398,"passed_time":0.4721336275,"remaining_time":0.711158672},
{"learn":[4.165860548],"iteration":399,"passed_time":0.473085295,"remaining_time":0.7096279424},
{"learn":[4.160950571],"iteration":400,"passed_time":0.4738894607,"remaining_time":0.707879768},
{"learn":[4.158544115],"iteration":401,"passed_time":0.4747292244,"remaining_time":0.7061892443},
{"learn":[4.154448767],"iteration":402,"passed_time":0.4754912396,"remaining_time":0.7043877669},
{"learn":[4.15197457],"iteration":403,"passed_time":0.4763533561,"remaining_time":0.7027391094},
{"learn":[4.149562679],"iteration":404,"passed_time":0.4770784909,"remaining_time":0.7008930915},
{"learn":[4.149327961],"iteration":405,"passed_time":0.4777337322,"remaining_time":0.6989503373},
{"learn":[4.147444889],"iteration":406,"passed_time":0.4784826424,"remaining_time":0.6971503856},
{"learn":[4.147254809],"iteration":407,"passed_time":0.4796803165,"remaining_time":0.6960067337},
{"learn":[4.144589165],"iteration":408,"passed_time":0.4804880176,"remaining_time":0.6942993114},
{"learn":[4.141691034],"iteration":409,"passed_time":0.4811892868,"remaining_time":0.69244312},
{"learn":[4.138893468],"iteration":410,"passed_time":0.4819286287,"remaining_time":0.6906471103},
{"learn":[4.136964597],"iteration":411,"passed_time":0.4826486137,"remaining_time":0.688828604},
{"learn":[4.133773523],"iteration":412,"passed_time":0.4834688301,"remaining_time":0.6871578772},
{"learn":[4.131363444],"iteration":413,"passed_time":0.4842362414,"remaining_time":0.6854165155},
{"learn":[4.130228592],"iteration":414,"passed_time":0.4850980973,"remaining_time":0.6838129805},
{"learn":[4.12884186],"iteration":415,"passed_time":0.4859856222,"remaining_time":0.6822490465},
{"learn":[4.12413494],"iteration":416,"passed_time":0.4868248549,"remaining_time":0.6806208403},
{"learn":[4.119422508],"iteration":417,"passed_time":0.4877629564,"remaining_time":0.6791340685},
{"learn":[4.117038244],"iteration":418,"passed_time":0.4885358725,"remaining_time":0.6774208637},
{"learn":[4.116067631],"iteration":419,"passed_time":0.4891750632,"remaining_time":0.6755274682},
{"learn":[4.110343455],"iteration":420,"passed_time":0.489944222,"remaining_time":0.6738187757},
{"learn":[4.105604544],"iteration":421,"passed_time":0.4906806384,"remaining_time":0.6720696895},
{"learn":[4.103390131],"iteration":422,"passed_time":0.4914425635,"remaining_time":0.670360187},
{"learn":[4.096724402],"iteration":423,"passed_time":0.4922990591,"remaining_time":0.6687836275},
{"learn":[4.093431279],"iteration":424,"passed_time":0.4930447131,"remaining_time":0.6670604942},
{"learn":[4.091412744],"iteration":425,"passed_time":0.4938487186,"remaining_time":0.6654205738},
{"learn":[4.091192901],"iteration":426,"passed_time":0.4946983611,"remaining_time":0.6638458102},
{"learn":[4.088994581],"iteration":427,"passed_time":0.4954506278,"remaining_time":0.6621442969},
{"learn":[4.087845355],"iteration":428,"passed_time":0.4962400153,"remaining_time":0.6604966171},
{"learn":[4.083650279],"iteration":429,"passed_time":0.4970459243,"remaining_time":0.6588748299},
{"learn":[4.079840652],"iteration":430,"passed_time":0.497752654,"remaining_time":0.6571258936},
{"learn":[4.075707828],"iteration":431,"passed_time":0.4984754043,"remaining_time":0.6554028463},
{"learn":[4.071345409],"iteration":432,"passed_time":0.4992258317,"remaining_time":0.6537206618},
{"learn":[4.067460475],"iteration":433,"passed_time":0.4999944195,"remaining_time":0.6520664549},
{"learn":[4.064914749],"iteration":434,"passed_time":0.5007342924,"remaining_time":0.6503790235},
{"learn":[4.063823175],"iteration":435,"passed_time":0.501453576,"remaining_time":0.6486693048},
{"learn":[4.058898471],"iteration":436,"passed_time":0.5021750939,"remaining_time":0.6469669975},
{"learn":[4.054120355],"iteration":437,"passed_time":0.5030750701,"remaining_time":0.6454981493},
{"learn":[4.052715901],"iteration":438,"passed_time":0.5038215156,"remaining_time":0.6438356953},
{"learn":[4.052114167],"iteration":439,"passed_time":0.5046325645,"remaining_time":0.6422596275},
{"learn":[4.051377267],"iteration":440,"passed_time":0.505657438,"remaining_time":0.6409580676},
{"learn":[4.049275336],"iteration":441,"passed_time":0.5065111183,"remaining_time":0.639441638},
{"learn":[4.047099198],"iteration":442,"passed_time":0.5072882925,"remaining_time":0.6378320066},
{"learn":[4.044348685],"iteration":443,"passed_time":0.5079837706,"remaining_time":0.6361238209},
{"learn":[4.042822379],"iteration":444,"passed_time":0.508663088,"remaining_time":0.634400031},
{"learn":[4.041258611],"iteration":445,"passed_time":0.5093986126,"remaining_time":0.632750743},
{"learn":[4.040044254],"iteration":446,"passed_time":0.5100988499,"remaining_time":0.6310618881},
{"learn":[4.036860137],"iteration":447,"passed_time":0.510852437,"remaining_time":0.6294431813},
{"learn":[4.036372284],"iteration":448,"passed_time":0.5117888894,"remaining_time":0.6280527351},
{"learn":[4.03368231],"iteration":449,"passed_time":0.512617602,"remaining_time":0.6265326247},
{"learn":[4.032439519],"iteration":450,"passed_time":0.5134059676,"remaining_time":0.624966466},
{"learn":[4.032008634],"iteration":451,"passed_time":0.5142554083,"remaining_time":0.6234777959},
{"learn":[4.030034932],"iteration":452,"passed_time":0.5150056912,"remaining_time":0.6218722143},
{"learn":[4.028173412],"iteration":453,"passed_time":0.5157199352,"remaining_time":0.6202270586},
{"learn":[4.023806097],"iteration":454,"passed_time":0.5165553709,"remaining_time":0.6187311586},
{"learn":[4.020239186],"iteration":455,"passed_time":0.5173596268,"remaining_time":0.6172009583},
{"learn":[4.017384838],"iteration":456,"passed_time":0.5184950652,"remaining_time":0.6160674407},
{"learn":[4.016468229],"iteration":457,"passed_time":0.5192371624,"remaining_time":0.6144684324},
{"learn":[4.014530169],"iteration":458,"passed_time":0.5199486411,"remaining_time":0.6128370694},
{"learn":[4.012884822],"iteration":459,"passed_time":0.5206783146,"remaining_time":0.611231065},
{"learn":[4.008924707],"iteration":460,"passed_time":0.5215136499,"remaining_time":0.6097524019},
{"learn":[4.008286778],"iteration":461,"passed_time":0.5225874105,"remaining_time":0.6085541706},
{"learn":[4.006444202],"iteration":462,"passed_time":0.5237524353,"remaining_time":0.6074623278},
{"learn":[4.003284363],"iteration":463,"passed_time":0.5251480305,"remaining_time":0.606636518},
{"learn":[3.999811484],"iteration":464,"passed_time":0.5260497125,"remaining_time":0.6052399918},
{"learn":[3.997483319],"iteration":465,"passed_time":0.5269133919,"remaining_time":0.6038020414},
{"learn":[3.99708333],"iteration":466,"passed_time":0.5276304513,"remaining_time":0.6021992089},
{"learn":[3.995860263],"iteration":467,"passed_time":0.5283705146,"remaining_time":0.6006263115},
{"learn":[3.994131111],"iteration":468,"passed_time":0.5290616044,"remaining_time":0.599001518},
{"learn":[3.993125499],"iteration":469,"passed_time":0.5298281383,"remaining_time":0.5974657729},
{"learn":[3.992954084],"iteration":470,"passed_time":0.5306901067,"remaining_time":0.5960404807},
{"learn":[3.990635743],"iteration":471,"passed_time":0.5315957359,"remaining_time":0.5946664164},
{"learn":[3.986678254],"iteration":472,"passed_time":0.5327708503,"remaining_time":0.5935945838},
{"learn":[3.986393291],"iteration":473,"passed_time":0.5339378235,"remaining_time":0.5925132809},
{"learn":[3.986152671],"iteration":474,"passed_time":0.5347962483,"remaining_time":0.5910905902},
{"learn":[3.985596662],"iteration":475,"passed_time":0.535557472,"remaining_time":0.5895632675},
{"learn":[3.983853457],"iteration":476,"passed_time":0.5363029056,"remaining_time":0.5880218441},
{"learn":[3.983263928],"iteration":477,"passed_time":0.5370203056,"remaining_time":0.5864531371},
{"learn":[3.980067202],"iteration":478,"passed_time":0.5378551299,"remaining_time":0.585015705},
{"learn":[3.978115407],"iteration":479,"passed_time":0.5386190645,"remaining_time":0.5835039866},
{"learn":[3.972661644],"iteration":480,"passed_time":0.5395107975,"remaining_time":0.5821332721},
{"learn":[3.969938254],"iteration":481,"passed_time":0.5403873832,"remaining_time":0.5807482666},
{"learn":[3.968211434],"iteration":482,"passed_time":0.5411646376,"remaining_time":0.5792590427},
{"learn":[3.966113368],"iteration":483,"passed_time":0.5419509764,"remaining_time":0.5777824459},
{"learn":[3.962246044],"iteration":484,"passed_time":0.5428031839,"remaining_time":0.5763786386},
{"learn":[3.961319703],"iteration":485,"passed_time":0.5436019193,"remaining_time":0.5749205484},
{"learn":[3.96078191],"iteration":486,"passed_time":0.5443720214,"remaining_time":0.5734350041},
{"learn":[3.958913633],"iteration":487,"passed_time":0.5453671604,"remaining_time":0.5721884962},
{"learn":[3.957428286],"iteration":488,"passed_time":0.5461350569,"remaining_time":0.5707055502},
{"learn":[3.952641965],"iteration":489,"passed_time":0.5471099298,"remaining_time":0.5694409473},
{"learn":[3.951486786],"iteration":490,"passed_time":0.5479176523,"remaining_time":0.5680042465},
{"learn":[3.94938344],"iteration":491,"passed_time":0.5487861452,"remaining_time":0.5666328491},
{"learn":[3.947297924],"iteration":492,"passed_time":0.5494984254,"remaining_time":0.5651028432},
{"learn":[3.946284886],"iteration":493,"passed_time":0.5502954146,"remaining_time":0.5636629145},
{"learn":[3.943288204],"iteration":494,"passed_time":0.5511527318,"remaining_time":0.5622871305},
{"learn":[3.943076488],"iteration":495,"passed_time":0.5519292949,"remaining_time":0.5608313803},
{"learn":[3.942347078],"iteration":496,"passed_time":0.5529900406,"remaining_time":0.5596659767},
{"learn":[3.940251541],"iteration":497,"passed_time":0.5541508875,"remaining_time":0.5586018986},
{"learn":[3.939011019],"iteration":498,"passed_time":0.5550433831,"remaining_time":0.5572680058},
{"learn":[3.938760512],"iteration":499,"passed_time":0.555771734,"remaining_time":0.555771734},
{"learn":[3.934522727],"iteration":500,"passed_time":0.5565923912,"remaining_time":0.5543704655},
{"learn":[3.930091193],"iteration":501,"passed_time":0.5574521016,"remaining_time":0.5530102522},
{"learn":[3.927671752],"iteration":502,"passed_time":0.5584344677,"remaining_time":0.5517732215},
{"learn":[3.927280041],"iteration":503,"passed_time":0.559136298,"remaining_time":0.5502611186},
{"learn":[3.925987561],"iteration":504,"passed_time":0.5598530267,"remaining_time":0.5487668282},
{"learn":[3.921645957],"iteration":505,"passed_time":0.5606503294,"remaining_time":0.5473542741},
{"learn":[3.920333743],"iteration":506,"passed_time":0.5614038784,"remaining_time":0.5459016017},
{"learn":[3.918659461],"iteration":507,"passed_time":0.5621615454,"remaining_time":0.5444556699},
{"learn":[3.916124385],"iteration":508,"passed_time":0.5630733467,"remaining_time":0.5431611262},
{"learn":[3.913849268],"iteration":509,"passed_time":0.5640333552,"remaining_time":0.5419144001},
{"learn":[3.912826119],"iteration":510,"passed_time":0.5648802926,"remaining_time":0.5405605931},
{"learn":[3.910034145],"iteration":511,"passed_time":0.5657266088,"remaining_time":0.539208174},
{"learn":[3.90792379],"iteration":512,"passed_time":0.5666031428,"remaining_time":0.5378864143},
{"learn":[3.907823851],"iteration":513,"passed_time":0.5673349703,"remaining_time":0.5364295634},
{"learn":[3.904527401],"iteration":514,"passed_time":0.5682959604,"remaining_time":0.5351913414},
{"learn":[3.903378283],"iteration":515,"passed_time":0.5691284405,"remaining_time":0.5338336535},
{"learn":[3.902170135],"iteration":516,"passed_time":0.5699390786,"remaining_time":0.5324575918},
{"learn":[3.899435429],"iteration":517,"passed_time":0.5707435049,"remaining_time":0.5310779331},
{"learn":[3.897497505],"iteration":518,"passed_time":0.5714724169,"remaining_time":0.5296305058},
{"learn":[3.896426119],"iteration":519,"passed_time":0.5721934739,"remaining_time":0.5281785913},
{"learn":[3.896044669],"iteration":520,"passed_time":0.5729409113,"remaining_time":0.5267537361},
{"learn":[3.892795942],"iteration":521,"passed_time":0.5736867156,"remaining_time":0.5253299809},
{"learn":[3.892413888],"iteration":522,"passed_time":0.5744649919,"remaining_time":0.5239384343},
{"learn":[3.891738985],"iteration":523,"passed_time":0.5751551399,"remaining_time":0.5224691729},
{"learn":[3.88822057],"iteration":524,"passed_time":0.5761243892,"remaining_time":0.5212553997},
{"learn":[3.883837053],"iteration":525,"passed_time":0.576999614,"remaining_time":0.5199578271},
{"learn":[3.881769742],"iteration":526,"passed_time":0.5777924765,"remaining_time":0.5185879343},
{"learn":[3.880356898],"iteration":527,"passed_time":0.578568657,"remaining_time":0.5172053146},
{"learn":[3.879250273],"iteration":528,"passed_time":0.5793156336,"remaining_time":0.5157989856},
{"learn":[3.877174493],"iteration":529,"passed_time":0.5800517293,"remaining_time":0.5143854958},
{"learn":[3.875854201],"iteration":530,"passed_time":0.580856947,"remaining_time":0.5130356086},
{"learn":[3.873189396],"iteration":531,"passed_time":0.5817327195,"remaining_time":0.511749836},
{"learn":[3.871583368],"iteration":532,"passed_time":0.5825437083,"remaining_time":0.5104088401},
{"learn":[3.869622679],"iteration":533,"passed_time":0.5836113171,"remaining_time":0.5092937711},
{"learn":[3.866860164],"iteration":534,"passed_time":0.5844573829,"remaining_time":0.5079863235},
{"learn":[3.864498444],"iteration":535,"passed_time":0.5853971633,"remaining_time":0.5067617235},
{"learn":[3.861416322],"iteration":536,"passed_time":0.5863383167,"remaining_time":0.505539368},
{"learn":[3.860265769],"iteration":537,"passed_time":0.587121845,"remaining_time":0.5041826996},
{"learn":[3.859328725],"iteration":538,"passed_time":0.5879396368,"remaining_time":0.502857463},
{"learn":[3.858521278],"iteration":539,"passed_time":0.5888915527,"remaining_time":0.5016483597},
{"learn":[3.85599111],"iteration":540,"passed_time":0.5897805747,"remaining_time":0.5003868462},
{"learn":[3.852379816],"iteration":541,"passed_time":0.5905988068,"remaining_time":0.4990668884},
{"learn":[3.851327537],"iteration":542,"passed_time":0.5914695997,"remaining_time":0.4977930149},
{"learn":[3.847854898],"iteration":543,"passed_time":0.5923110667,"remaining_time":0.4964960412},
{"learn":[3.847083414],"iteration":544,"passed_time":0.593084563,"remaining_time":0.495143993},
{"learn":[3.845397429],"iteration":545,"passed_time":0.5939060318,"remaining_time":0.4938339532},
{"learn":[3.841933528],"iteration":546,"passed_time":0.5946819837,"remaining_time":0.4924880047},
{"learn":[3.840996474],"iteration":547,"passed_time":0.5955510533,"remaining_time":0.4912209418},
{"learn":[3.838355966],"iteration":548,"passed_time":0.596327728,"remaining_time":0.4898794268},
{"learn":[3.83342799],"iteration":549,"passed_time":0.5970748147,"remaining_time":0.4885157575},
{"learn":[3.828161535],"iteration":550,"passed_time":0.5978760844,"remaining_time":0.4871984789},
{"learn":[3.823502399],"iteration":551,"passed_time":0.5986189722,"remaining_time":0.4858356876},
{"learn":[3.820068862],"iteration":552,"passed_time":0.5993778515,"remaining_time":0.4844880644},
{"learn":[3.817951642],"iteration":553,"passed_time":0.6001929996,"remaining_time":0.4831878661},
{"learn":[3.815785958],"iteration":554,"passed_time":0.6009850508,"remaining_time":0.4818708966},
{"learn":[3.81503012],"iteration":555,"passed_time":0.6017103659,"remaining_time":0.4805025224},
{"learn":[3.813529315],"iteration":556,"passed_time":0.6025745663,"remaining_time":0.4792469172},
{"learn":[3.808881326],"iteration":557,"passed_time":0.6032705455,"remaining_time":0.4778594643},
{"learn":[3.808740434],"iteration":558,"passed_time":0.6040013826,"remaining_time":0.4765019852},
{"learn":[3.80714352],"iteration":559,"passed_time":0.6047347631,"remaining_time":0.4751487425},
{"learn":[3.80573346],"iteration":560,"passed_time":0.6054418735,"remaining_time":0.4737771524},
{"learn":[3.803370052],"iteration":561,"passed_time":0.6061582616,"remaining_time":0.4724151576},
{"learn":[3.803215211],"iteration":562,"passed_time":0.6068959805,"remaining_time":0.4710720133},
{"learn":[3.801309667],"iteration":563,"passed_time":0.6076535773,"remaining_time":0.4697463824},
{"learn":[3.800003847],"iteration":564,"passed_time":0.6083997122,"remaining_time":0.4684139377},
{"learn":[3.798026138],"iteration":565,"passed_time":0.6091539426,"remaining_time":0.4670897722},
{"learn":[3.794745847],"iteration":566,"passed_time":0.6099744696,"remaining_time":0.4658182457},
{"learn":[3.794312041],"iteration":567,"passed_time":0.6107201937,"remaining_time":0.4644914149},
{"learn":[3.792205926],"iteration":568,"passed_time":0.6115328256,"remaining_time":0.4632173073},
{"learn":[3.788991061],"iteration":569,"passed_time":0.6122893804,"remaining_time":0.461902515},
{"learn":[3.787391572],"iteration":570,"passed_time":0.6130619859,"remaining_time":0.4606017372},
{"learn":[3.7826445],"iteration":571,"passed_time":0.6138766514,"remaining_time":0.4593342776},
{"learn":[3.781700331],"iteration":572,"passed_time":0.6147522378,"remaining_time":0.4581137967},
{"learn":[3.780045374],"iteration":573,"passed_time":0.6156245937,"remaining_time":0.4568921201},
{"learn":[3.775462644],"iteration":574,"passed_time":0.6163684543,"remaining_time":0.4555766836},
{"learn":[3.773711943],"iteration":575,"passed_time":0.617134367,"remaining_time":0.4542794646},
{"learn":[3.772415806],"iteration":576,"passed_time":0.6178801512,"remaining_time":0.452969331},
{"learn":[3.770170875],"iteration":577,"passed_time":0.618594265,"remaining_time":0.4516380274},
{"learn":[3.765166479],"iteration":578,"passed_time":0.619517438,"remaining_time":0.450460866},
{"learn":[3.763976102],"iteration":579,"passed_time":0.6203378347,"remaining_time":0.4492101562},
{"learn":[3.760761708],"iteration":580,"passed_time":0.6212039889,"remaining_time":0.4479939266},
{"learn":[3.758155662],"iteration":581,"passed_time":0.6219573576,"remaining_time":0.446697896},
{"learn":[3.756844548],"iteration":582,"passed_time":0.6227165575,"remaining_time":0.4454078979},
{"learn":[3.753098923],"iteration":583,"passed_time":0.6234607988,"remaining_time":0.4441090621},
{"learn":[3.751618946],"iteration":584,"passed_time":0.624129626,"remaining_time":0.4427586236},
{"learn":[3.751398464],"iteration":585,"passed_time":0.6249748519,"remaining_time":0.4415351343},
{"learn":[3.749920103],"iteration":586,"passed_time":0.6259270638,"remaining_time":0.4403882067},
{"learn":[3.748237465],"iteration":587,"passed_time":0.6267704782,"remaining_time":0.4391657092},
{"learn":[3.746021536],"iteration":588,"passed_time":0.6279502713,"remaining_time":0.4381792216},
{"learn":[3.74417648],"iteration":589,"passed_time":0.6288550291,"remaining_time":0.4370009524},
{"learn":[3.738788389],"iteration":590,"passed_time":0.6295891711,"remaining_time":0.4357055347},
{"learn":[3.736021611],"iteration":591,"passed_time":0.6304301872,"remaining_time":0.4344856696},
{"learn":[3.734546151],"iteration":592,"passed_time":0.6311520859,"remaining_time":0.4331853271},
{"learn":[3.733527479],"iteration":593,"passed_time":0.6320249528,"remaining_time":0.4319901193},
{"learn":[3.733026392],"iteration":594,"passed_time":0.632735129,"remaining_time":0.4306852559},
{"learn":[3.730314752],"iteration":595,"passed_time":0.633764044,"remaining_time":0.4295984459},
{"learn":[3.727342596],"iteration":596,"passed_time":0.6346073344,"remaining_time":0.4283865256},
{"learn":[3.725459604],"iteration":597,"passed_time":0.6353717643,"remaining_time":0.4271228248},
{"learn":[3.723158842],"iteration":598,"passed_time":0.6361182198,"remaining_time":0.4258487582},
{"learn":[3.722362756],"iteration":599,"passed_time":0.6369169652,"remaining_time":0.4246113101},
{"learn":[3.721443615],"iteration":600,"passed_time":0.6380953957,"remaining_time":0.4236273925},
{"learn":[3.720743486],"iteration":601,"passed_time":0.6390701071,"remaining_time":0.4225081439},
{"learn":[3.720215334],"iteration":602,"passed_time":0.6399520614,"remaining_time":0.4213283058},
{"learn":[3.719436563],"iteration":603,"passed_time":0.6407482118,"remaining_time":0.4200931985},
{"learn":[3.715046574],"iteration":604,"passed_time":0.6415166293,"remaining_time":0.4188414357},
{"learn":[3.71443396],"iteration":605,"passed_time":0.6422516029,"remaining_time":0.417569524},
{"learn":[3.712938941],"iteration":606,"passed_time":0.6429995312,"remaining_time":0.416307769},
{"learn":[3.712814764],"iteration":607,"passed_time":0.6436720756,"remaining_time":0.4149991014},
{"learn":[3.71235348],"iteration":608,"passed_time":0.6444206953,"remaining_time":0.4137413659},
{"learn":[3.711223749],"iteration":609,"passed_time":0.6451847544,"remaining_time":0.4124951709},
{"learn":[3.710755648],"iteration":610,"passed_time":0.6459050901,"remaining_time":0.4112227169},
{"learn":[3.708668039],"iteration":611,"passed_time":0.6471383252,"remaining_time":0.4102772389},
{"learn":[3.705623591],"iteration":612,"passed_time":0.6479166115,"remaining_time":0.409043603},
{"learn":[3.704045802],"iteration":613,"passed_time":0.6487810524,"remaining_time":0.4078656127},
{"learn":[3.699915209],"iteration":614,"passed_time":0.6495876427,"remaining_time":0.4066524268},
{"learn":[3.696182221],"iteration":615,"passed_time":0.650547095,"remaining_time":0.4055358514},
{"learn":[3.694263278],"iteration":616,"passed_time":0.6512064943,"remaining_time":0.4042335289},
{"learn":[3.693810229],"iteration":617,"passed_time":0.6519248361,"remaining_time":0.4029697207},
{"learn":[3.690900932],"iteration":618,"passed_time":0.6528028229,"remaining_time":0.4018059378},
{"learn":[3.688020895],"iteration":619,"passed_time":0.653730765,"remaining_time":0.4006736947},
{"learn":[3.685491894],"iteration":620,"passed_time":0.6545035508,"remaining_time":0.3994474167},
{"learn":[3.684328128],"iteration":621,"passed_time":0.6552589534,"remaining_time":0.3982120328},
{"learn":[3.680640153],"iteration":622,"passed_time":0.6560038459,"remaining_time":0.3969718297},
{"learn":[3.678932783],"iteration":623,"passed_time":0.6568217379,"remaining_time":0.395777201},
{"learn":[3.674167041],"iteration":624,"passed_time":0.6576084302,"remaining_time":0.3945650581},
{"learn":[3.672200976],"iteration":625,"passed_time":0.6583555771,"remaining_time":0.3933306483},
{"learn":[3.670606604],"iteration":626,"passed_time":0.6590483,"remaining_time":0.3920654161},
{"learn":[3.665506042],"iteration":627,"passed_time":0.6600611944,"remaining_time":0.3909916629},
{"learn":[3.664214007],"iteration":628,"passed_time":0.6608179596,"remaining_time":0.3897670318},
{"learn":[3.66261643],"iteration":629,"passed_time":0.6615388162,"remaining_time":0.3885227968},
{"learn":[3.662118449],"iteration":630,"passed_time":0.6623177237,"remaining_time":0.3873141681},
{"learn":[3.660871366],"iteration":631,"passed_time":0.6631088846,"remaining_time":0.3861140341},
{"learn":[3.656695243],"iteration":632,"passed_time":0.6638549694,"remaining_time":0.3848890581},
{"learn":[3.654497801],"iteration":633,"passed_time":0.6646021463,"remaining_time":0.3836662233},
{"learn":[3.654189134],"iteration":634,"passed_time":0.6653400555,"remaining_time":0.3824395595},
{"learn":[3.653957699],"iteration":635,"passed_time":0.6660675148,"remaining_time":0.3812084519},
{"learn":[3.651920725],"iteration":636,"passed_time":0.6671214175,"remaining_time":0.3801649522},
{"learn":[3.65106705],"iteration":637,"passed_time":0.6679085907,"remaining_time":0.3789700781},
{"learn":[3.650612844],"iteration":638,"passed_time":0.668634988,"remaining_time":0.377742145},
{"learn":[3.649884732],"iteration":639,"passed_time":0.6694899521,"remaining_time":0.3765880981},
{"learn":[3.646276182],"iteration":640,"passed_time":0.6705078847,"remaining_time":0.3755262568},
{"learn":[3.645808194],"iteration":641,"passed_time":0.6712482477,"remaining_time":0.3743097705},
{"learn":[3.645042989],"iteration":642,"passed_time":0.6719782819,"remaining_time":0.3730890305},
{"learn":[3.639864499],"iteration":643,"passed_time":0.6731079492,"remaining_time":0.3720907297},
{"learn":[3.637318478],"iteration":644,"passed_time":0.6738497659,"remaining_time":0.3708785533},
{"learn":[3.636344905],"iteration":645,"passed_time":0.6746758349,"remaining_time":0.3697140024},
{"learn":[3.634754643],"iteration":646,"passed_time":0.675450869,"remaining_time":0.3685226534},
{"learn":[3.630724975],"iteration":647,"passed_time":0.676378897,"remaining_time":0.3674156971},
{"learn":[3.629408252],"iteration":648,"passed_time":0.6774522869,"remaining_time":0.3663879086},
{"learn":[3.62790646],"iteration":649,"passed_time":0.6782144724,"remaining_time":0.3651924082},
{"learn":[3.627388973],"iteration":650,"passed_time":0.6790115346,"remaining_time":0.3640169364},
{"learn":[3.625163557],"iteration":651,"passed_time":0.6799396459,"remaining_time":0.3629125717},
{"learn":[3.623701985],"iteration":652,"passed_time":0.680674359,"remaining_time":0.3617059764},
{"learn":[3.622342639],"iteration":653,"passed_time":0.6814123383,"remaining_time":0.3605025521},
{"learn":[3.621130639],"iteration":654,"passed_time":0.6821082774,"remaining_time":0.3592784057},
{"learn":[3.619125665],"iteration":655,"passed_time":0.6828407863,"remaining_time":0.3580750465},
{"learn":[3.618878783],"iteration":656,"passed_time":0.6835610418,"remaining_time":0.3568667235},
{"learn":[3.616207429],"iteration":657,"passed_time":0.6843744151,"remaining_time":0.3557082826},
{"learn":[3.61206486],"iteration":658,"passed_time":0.6853570817,"remaining_time":0.3546384899},
{"learn":[3.611955873],"iteration":659,"passed_time":0.6860982471,"remaining_time":0.3534445516},
{"learn":[3.610713743],"iteration":660,"passed_time":0.687118335,"remaining_time":0.3523950311},
{"learn":[3.610044025],"iteration":661,"passed_time":0.6878827247,"remaining_time":0.3512150468},
{"learn":[3.607342669],"iteration":662,"passed_time":0.68874951,"remaining_time":0.3500883633},
{"learn":[3.602510618],"iteration":663,"passed_time":0.6895927504,"remaining_time":0.3489505484},
{"learn":[3.600492392],"iteration":664,"passed_time":0.6908452137,"remaining_time":0.3480197693},
{"learn":[3.597171065],"iteration":665,"passed_time":0.6916962489,"remaining_time":0.3468867074},
{"learn":[3.594358798],"iteration":666,"passed_time":0.6925432064,"remaining_time":0.3457524554},
{"learn":[3.593945251],"iteration":667,"passed_time":0.6934710984,"remaining_time":0.3446592884},
{"learn":[3.593607748],"iteration":668,"passed_time":0.6943000916,"remaining_time":0.3435176836},
{"learn":[3.592238714],"iteration":669,"passed_time":0.6950965626,"remaining_time":0.3423609935},
{"learn":[3.590144654],"iteration":670,"passed_time":0.6958866958,"remaining_time":0.3412022696},
{"learn":[3.587151536],"iteration":671,"passed_time":0.6967006402,"remaining_time":0.3400562649},
{"learn":[3.586070865],"iteration":672,"passed_time":0.697465541,"remaining_time":0.3388874174},
{"learn":[3.585102746],"iteration":673,"passed_time":0.698269867,"remaining_time":0.3377388378},
{"learn":[3.584362847],"iteration":674,"passed_time":0.6991157725,"remaining_time":0.3366112979},
{"learn":[3.581407561],"iteration":675,"passed_time":0.6998934977,"remaining_time":0.3354519131},
{"learn":[3.57919422],"iteration":676,"passed_time":0.7006373884,"remaining_time":0.3342775132},
{"learn":[3.577632204],"iteration":677,"passed_time":0.7014051446,"remaining_time":0.3331157176},
{"learn":[3.573911195],"iteration":678,"passed_time":0.7021446969,"remaining_time":0.3319417492},
{"learn":[3.573408216],"iteration":679,"passed_time":0.7028708537,"remaining_time":0.3307627547},
{"learn":[3.571076482],"iteration":680,"passed_time":0.703613542,"remaining_time":0.3295928339},
{"learn":[3.568177107],"iteration":681,"passed_time":0.7043541764,"remaining_time":0.3284232084},
{"learn":[3.564824621],"iteration":682,"passed_time":0.7050964039,"remaining_time":0.3272555784},
{"learn":[3.562475026],"iteration":683,"passed_time":0.7059256317,"remaining_time":0.3261293854},
{"learn":[3.561226889],"iteration":684,"passed_time":0.7068863238,"remaining_time":0.3250645139},
{"learn":[3.559383467],"iteration":685,"passed_time":0.7077082134,"remaining_time":0.3239364126},
{"learn":[3.555209766],"iteration":686,"passed_time":0.7086093543,"remaining_time":0.3228453099},
{"learn":[3.55345383],"iteration":687,"passed_time":0.7095112636,"remaining_time":0.3217551079},
{"learn":[3.552300968],"iteration":688,"passed_time":0.7102866444,"remaining_time":0.3206083402},
{"learn":[3.551253986],"iteration":689,"passed_time":0.7111310269,"remaining_time":0.3194936498},
{"learn":[3.549807725],"iteration":690,"passed_time":0.7119718527,"remaining_time":0.3183781512},
{"learn":[3.547992926],"iteration":691,"passed_time":0.7128766417,"remaining_time":0.3172919157},
{"learn":[3.545438607],"iteration":692,"passed_time":0.7138605913,"remaining_time":0.3162412721},
{"learn":[3.543313763],"iteration":693,"passed_time":0.7147235995,"remaining_time":0.3151374949},
{"learn":[3.542962896],"iteration":694,"passed_time":0.7154733613,"remaining_time":0.3139847125},
{"learn":[3.539800465],"iteration":695,"passed_time":0.716178037,"remaining_time":0.3128133955},
{"learn":[3.53953187],"iteration":696,"passed_time":0.7168337392,"remaining_time":0.3116221277},
{"learn":[3.536332425],"iteration":697,"passed_time":0.7177759873,"remaining_time":0.3105563727},
{"learn":[3.534993327],"iteration":698,"passed_time":0.7186340459,"remaining_time":0.3094547179},
{"learn":[3.531637011],"iteration":699,"passed_time":0.7193745,"remaining_time":0.3083033571},
{"learn":[3.531040284],"iteration":700,"passed_time":0.7201147637,"remaining_time":0.3071530875},
{"learn":[3.529973872],"iteration":701,"passed_time":0.7209180386,"remaining_time":0.3060307343},
{"learn":[3.527325183],"iteration":702,"passed_time":0.7216615576,"remaining_time":0.3048840436},
{"learn":[3.527200815],"iteration":703,"passed_time":0.7224591408,"remaining_time":0.3037612297},
{"learn":[3.523459911],"iteration":704,"passed_time":0.7231781239,"remaining_time":0.302606449},
{"learn":[3.522729934],"iteration":705,"passed_time":0.7239967987,"remaining_time":0.3014944176},
{"learn":[3.522260582],"iteration":706,"passed_time":0.7247550468,"remaining_time":0.3003581736},
{"learn":[3.518641591],"iteration":707,"passed_time":0.7255739807,"remaining_time":0.2992480259},
{"learn":[3.516856405],"iteration":708,"passed_time":0.7264942124,"remaining_time":0.2981802762},
{"learn":[3.515083413],"iteration":709,"passed_time":0.7273343869,"remaining_time":0.2970802425},
{"learn":[3.514671214],"iteration":710,"passed_time":0.7283324486,"remaining_time":0.2960451163},
{"learn":[3.512617621],"iteration":711,"passed_time":0.7293271397,"remaining_time":0.2950087306},
{"learn":[3.510747971],"iteration":712,"passed_time":0.7301781222,"remaining_time":0.2939146158},
{"learn":[3.508149266],"iteration":713,"passed_time":0.730977609,"remaining_time":0.2928005549},
{"learn":[3.504557165],"iteration":714,"passed_time":0.7317639015,"remaining_time":0.2916821146},
{"learn":[3.501367208],"iteration":715,"passed_time":0.7325062784,"remaining_time":0.290547183},
{"learn":[3.497593362],"iteration":716,"passed_time":0.7334133707,"remaining_time":0.2894783597},
{"learn":[3.496291169],"iteration":717,"passed_time":0.7341799861,"remaining_time":0.2883548135},
{"learn":[3.49330374],"iteration":718,"passed_time":0.7349170237,"remaining_time":0.2872207005},
{"learn":[3.490044385],"iteration":719,"passed_time":0.735736898,"remaining_time":0.2861199048},
{"learn":[3.488891789],"iteration":720,"passed_time":0.7366175798,"remaining_time":0.2850434185},
{"learn":[3.486869081],"iteration":721,"passed_time":0.7375299033,"remaining_time":0.283979658},
{"learn":[3.486303638],"iteration":722,"passed_time":0.73833461,"remaining_time":0.2828750857},
{"learn":[3.486035862],"iteration":723,"passed_time":0.7390658866,"remaining_time":0.281743349},
{"learn":[3.482668951],"iteration":724,"passed_time":0.7399658953,"remaining_time":0.2806767189},
{"learn":[3.47820549],"iteration":725,"passed_time":0.7407238024,"remaining_time":0.2795569172},
{"learn":[3.474392283],"iteration":726,"passed_time":0.7415626344,"remaining_time":0.2784684996},
{"learn":[3.472268163],"iteration":727,"passed_time":0.7422910955,"remaining_time":0.2773395302},
{"learn":[3.471209164],"iteration":728,"passed_time":0.7430781893,"remaining_time":0.2762334558},
{"learn":[3.470049971],"iteration":729,"passed_time":0.7440135641,"remaining_time":0.2751830991},
{"learn":[3.469078654],"iteration":730,"passed_time":0.7448249551,"remaining_time":0.2740874322},
{"learn":[3.468643292],"iteration":731,"passed_time":0.7456334792,"remaining_time":0.2729914924},
{"learn":[3.468134848],"iteration":732,"passed_time":0.7464206424,"remaining_time":0.271888556},
{"learn":[3.467820182],"iteration":733,"passed_time":0.7472818872,"remaining_time":0.270813327},
{"learn":[3.465776156],"iteration":734,"passed_time":0.7480164099,"remaining_time":0.2696929913},
{"learn":[3.463037608],"iteration":735,"passed_time":0.7488373777,"remaining_time":0.2686047116},
{"learn":[3.45965637],"iteration":736,"passed_time":0.7495743752,"remaining_time":0.2674871922},
{"learn":[3.457275091],"iteration":737,"passed_time":0.7504199099,"remaining_time":0.2664092363},
{"learn":[3.455522955],"iteration":738,"passed_time":0.7512771364,"remaining_time":0.2653360387},
{"learn":[3.451270508],"iteration":739,"passed_time":0.7522701019,"remaining_time":0.2643111169},
{"learn":[3.450978947],"iteration":740,"passed_time":0.7530968307,"remaining_time":0.263228177},
{"learn":[3.450608492],"iteration":741,"passed_time":0.7538201921,"remaining_time":0.2621099859},
{"learn":[3.448122004],"iteration":742,"passed_time":0.7545178545,"remaining_time":0.2609839685},
{"learn":[3.445646714],"iteration":743,"passed_time":0.7552600819,"remaining_time":0.2598744368},
{"learn":[3.44411263],"iteration":744,"passed_time":0.7559669819,"remaining_time":0.2587537992},
{"learn":[3.443264164],"iteration":745,"passed_time":0.7568800957,"remaining_time":0.257704483},
{"learn":[3.439521363],"iteration":746,"passed_time":0.7576800634,"remaining_time":0.2566172102},
{"learn":[3.436809225],"iteration":747,"passed_time":0.7584393234,"remaining_time":0.2555169913},
{"learn":[3.435509465],"iteration":748,"passed_time":0.759178515,"remaining_time":0.2544109576},
{"learn":[3.434450277],"iteration":749,"passed_time":0.7598726607,"remaining_time":0.2532908869},
{"learn":[3.431786753],"iteration":750,"passed_time":0.7605820755,"remaining_time":0.252177013},
{"learn":[3.430150302],"iteration":751,"passed_time":0.7613013892,"remaining_time":0.2510674794},
{"learn":[3.42696281],"iteration":752,"passed_time":0.7623598746,"remaining_time":0.2500702377},
{"learn":[3.426870334],"iteration":753,"passed_time":0.7632442128,"remaining_time":0.2490160164},
{"learn":[3.425200309],"iteration":754,"passed_time":0.7641688263,"remaining_time":0.2479753145},
{"learn":[3.423383783],"iteration":755,"passed_time":0.7649705073,"remaining_time":0.2468952431},
{"learn":[3.422752979],"iteration":756,"passed_time":0.7657120234,"remaining_time":0.245796594},
{"learn":[3.420845924],"iteration":757,"passed_time":0.7664628415,"remaining_time":0.2447018571},
{"learn":[3.418917862],"iteration":758,"passed_time":0.767322519,"remaining_time":0.2436425917},
{"learn":[3.417095735],"iteration":759,"passed_time":0.768335764,"remaining_time":0.2426323465},
{"learn":[3.414391848],"iteration":760,"passed_time":0.7693093533,"remaining_time":0.2416096392},
{"learn":[3.41426711],"iteration":761,"passed_time":0.7701281871,"remaining_time":0.2405387251},
{"learn":[3.411976013],"iteration":762,"passed_time":0.7709259205,"remaining_time":0.2394619176},
{"learn":[3.408614844],"iteration":763,"passed_time":0.7717102784,"remaining_time":0.238381709},
{"learn":[3.407906721],"iteration":764,"passed_time":0.7724726544,"remaining_time":0.2372955213},
{"learn":[3.407494015],"iteration":765,"passed_time":0.7732037706,"remaining_time":0.2362006297},
{"learn":[3.406287128],"iteration":766,"passed_time":0.7740975274,"remaining_time":0.2351560937},
{"learn":[3.404600442],"iteration":767,"passed_time":0.7748653137,"remaining_time":0.2340738968},
{"learn":[3.404012662],"iteration":768,"passed_time":0.7755725443,"remaining_time":0.2329743274},
{"learn":[3.400398762],"iteration":769,"passed_time":0.7763963976,"remaining_time":0.2319106123},
{"learn":[3.399737714],"iteration":770,"passed_time":0.7772346585,"remaining_time":0.2308517987},
{"learn":[3.399185251],"iteration":771,"passed_time":0.7780248063,"remaining_time":0.2297793469},
{"learn":[3.397245411],"iteration":772,"passed_time":0.7788495814,"remaining_time":0.2287177943},
{"learn":[3.396229831],"iteration":773,"passed_time":0.7796375376,"remaining_time":0.2276461027},
{"learn":[3.394002836],"iteration":774,"passed_time":0.7805263041,"remaining_time":0.2266044109},
{"learn":[3.389617243],"iteration":775,"passed_time":0.7819155729,"remaining_time":0.2257075881},
{"learn":[3.385426488],"iteration":776,"passed_time":0.7827838536,"remaining_time":0.2246599734},
{"learn":[3.385072258],"iteration":777,"passed_time":0.7834802235,"remaining_time":0.2235637656},
{"learn":[3.383842366],"iteration":778,"passed_time":0.7843698224,"remaining_time":0.2225234028},
{"learn":[3.380110746],"iteration":779,"passed_time":0.7851817129,"remaining_time":0.2214615088},
{"learn":[3.378595218],"iteration":780,"passed_time":0.7859234995,"remaining_time":0.2203805972},
{"learn":[3.377371219],"iteration":781,"passed_time":0.7867236876,"remaining_time":0.2193168336},
{"learn":[3.375814782],"iteration":782,"passed_time":0.7875395858,"remaining_time":0.2182580972},
{"learn":[3.374195887],"iteration":783,"passed_time":0.7884806822,"remaining_time":0.2172344737},
{"learn":[3.373704309],"iteration":784,"passed_time":0.7893863918,"remaining_time":0.2162013685},
{"learn":[3.372971757],"iteration":785,"passed_time":0.7902655207,"remaining_time":0.2151613504},
{"learn":[3.371565136],"iteration":786,"passed_time":0.7910611101,"remaining_time":0.2140991314},
{"learn":[3.3700309],"iteration":787,"passed_time":0.7918087879,"remaining_time":0.2130246993},
{"learn":[3.368186663],"iteration":788,"passed_time":0.7926253073,"remaining_time":0.2119695055},
{"learn":[3.366710398],"iteration":789,"passed_time":0.7933093035,"remaining_time":0.2108796883},
{"learn":[3.364598042],"iteration":790,"passed_time":0.7940228662,"remaining_time":0.2097987093},
{"learn":[3.36348442],"iteration":791,"passed_time":0.7947107198,"remaining_time":0.2087119062},
{"learn":[3.362001759],"iteration":792,"passed_time":0.7957216404,"remaining_time":0.2077104408},
{"learn":[3.361580401],"iteration":793,"passed_time":0.7963830535,"remaining_time":0.2066182733},
{"learn":[3.359543675],"iteration":794,"passed_time":0.7971107933,"remaining_time":0.2055442926},
{"learn":[3.35766119],"iteration":795,"passed_time":0.7978737804,"remaining_time":0.2044802151},
{"learn":[3.354592969],"iteration":796,"passed_time":0.7986927945,"remaining_time":0.2034311635},
{"learn":[3.350985986],"iteration":797,"passed_time":0.7997294342,"remaining_time":0.2024377766},
{"learn":[3.349589624],"iteration":798,"passed_time":0.8005674245,"remaining_time":0.2013943083},
{"learn":[3.349110856],"iteration":799,"passed_time":0.8014828427,"remaining_time":0.2003707107},
{"learn":[3.345315441],"iteration":800,"passed_time":0.8026511739,"remaining_time":0.1994102167},
{"learn":[3.34397474],"iteration":801,"passed_time":0.8035712711,"remaining_time":0.1983879198},
{"learn":[3.343800902],"iteration":802,"passed_time":0.8044229075,"remaining_time":0.1973490819},
{"learn":[3.342329465],"iteration":803,"passed_time":0.8052026465,"remaining_time":0.1962931825},
{"learn":[3.34220347],"iteration":804,"passed_time":0.8060293854,"remaining_time":0.1952493542},
{"learn":[3.341279219],"iteration":805,"passed_time":0.8068336112,"remaining_time":0.1942006459},
{"learn":[3.337329521],"iteration":806,"passed_time":0.8075494583,"remaining_time":0.193131407},
{"learn":[3.336708453],"iteration":807,"passed_time":0.8085026587,"remaining_time":0.1921194436},
{"learn":[3.333252703],"iteration":808,"passed_time":0.8094526157,"remaining_time":0.1911068598},
{"learn":[3.332186769],"iteration":809,"passed_time":0.8103894431,"remaining_time":0.1900913508},
{"learn":[3.330594851],"iteration":810,"passed_time":0.8112182702,"remaining_time":0.1890508669},
{"learn":[3.327867442],"iteration":811,"passed_time":0.8120320643,"remaining_time":0.1880074238},
{"learn":[3.327563111],"iteration":812,"passed_time":0.8129043704,"remaining_time":0.186978004},
{"learn":[3.326308994],"iteration":813,"passed_time":0.8136721066,"remaining_time":0.185925076},
{"learn":[3.326249879],"iteration":814,"passed_time":0.8147443243,"remaining_time":0.1849419632},
{"learn":[3.322336238],"iteration":815,"passed_time":0.8158699382,"remaining_time":0.1839706723},
{"learn":[3.320491154],"iteration":816,"passed_time":0.8165849336,"remaining_time":0.1829070292},
{"learn":[3.320434271],"iteration":817,"passed_time":0.8172997587,"remaining_time":0.1818442006},
{"learn":[3.319609638],"iteration":818,"passed_time":0.8180288411,"remaining_time":0.1807853727},
{"learn":[3.316182682],"iteration":819,"passed_time":0.8188290092,"remaining_time":0.1797429532},
{"learn":[3.313126612],"iteration":820,"passed_time":0.8195553763,"remaining_time":0.1786850333},
{"learn":[3.311222803],"iteration":821,"passed_time":0.8202920732,"remaining_time":0.177630157},
{"learn":[3.309627335],"iteration":822,"passed_time":0.8210850376,"remaining_time":0.1765881551},
{"learn":[3.307974895],"iteration":823,"passed_time":0.8219060855,"remaining_time":0.1755527561},
{"learn":[3.307321505],"iteration":824,"passed_time":0.8227714181,"remaining_time":0.1745272705},
{"learn":[3.306759087],"iteration":825,"passed_time":0.8237794632,"remaining_time":0.1735322356},
{"learn":[3.30484037],"iteration":826,"passed_time":0.8245143566,"remaining_time":0.1724800287},
{"learn":[3.30201994],"iteration":827,"passed_time":0.8253192437,"remaining_time":0.1714431279},
{"learn":[3.299302297],"iteration":828,"passed_time":0.8260326161,"remaining_time":0.17038791},
{"learn":[3.298132671],"iteration":829,"passed_time":0.8267820774,"remaining_time":0.1693409074},
{"learn":[3.296976183],"iteration":830,"passed_time":0.8275650841,"remaining_time":0.1683014431},
{"learn":[3.293144745],"iteration":831,"passed_time":0.828452058,"remaining_time":0.1672835886},
{"learn":[3.290284404],"iteration":832,"passed_time":0.8292487294,"remaining_time":0.1662479446},
{"learn":[3.288285745],"iteration":833,"passed_time":0.8300034607,"remaining_time":0.1652045258},
{"learn":[3.286662667],"iteration":834,"passed_time":0.8308105415,"remaining_time":0.1641721429},
{"learn":[3.285692682],"iteration":835,"passed_time":0.8316310384,"remaining_time":0.163142931},
{"learn":[3.284565611],"iteration":836,"passed_time":0.8325151268,"remaining_time":0.1621266017},
{"learn":[3.283897383],"iteration":837,"passed_time":0.8333464143,"remaining_time":0.1611003808},
{"learn":[3.280712855],"iteration":838,"passed_time":0.8341221858,"remaining_time":0.1600639713},
{"learn":[3.280468341],"iteration":839,"passed_time":0.8347736099,"remaining_time":0.1590044971},
{"learn":[3.277814895],"iteration":840,"passed_time":0.8356279514,"remaining_time":0.157984357},
{"learn":[3.276316385],"iteration":841,"passed_time":0.8364930836,"remaining_time":0.1569666356},
{"learn":[3.27557063],"iteration":842,"passed_time":0.8374712536,"remaining_time":0.1559703284},
{"learn":[3.27499628],"iteration":843,"passed_time":0.8382331486,"remaining_time":0.1549340891},
{"learn":[3.273569958],"iteration":844,"passed_time":0.8389757668,"remaining_time":0.1538949631},
{"learn":[3.269665595],"iteration":845,"passed_time":0.8397397057,"remaining_time":0.1528604192},
{"learn":[3.267984685],"iteration":846,"passed_time":0.8407271861,"remaining_time":0.1518668943},
{"learn":[3.267702508],"iteration":847,"passed_time":0.8416463967,"remaining_time":0.1508611466},
{"learn":[3.266671924],"iteration":848,"passed_time":0.8424520753,"remaining_time":0.1498354103},
{"learn":[3.265359825],"iteration":849,"passed_time":0.8432366336,"remaining_time":0.1488064648},
{"learn":[3.2618983],"iteration":850,"passed_time":0.8439750839,"remaining_time":0.1477700206},
{"learn":[3.260456253],"iteration":851,"passed_time":0.8447398143,"remaining_time":0.146738841},
{"learn":[3.258389147],"iteration":852,"passed_time":0.845490528,"remaining_time":0.1457058706},
{"learn":[3.258108469],"iteration":853,"passed_time":0.8461698653,"remaining_time":0.1446613587},
{"learn":[3.256424936],"iteration":854,"passed_time":0.8472903342,"remaining_time":0.1436925128},
{"learn":[3.254817983],"iteration":855,"passed_time":0.8480654445,"remaining_time":0.142665215},
{"learn":[3.253898449],"iteration":856,"passed_time":0.8489732081,"remaining_time":0.1416606403},
{"learn":[3.253023652],"iteration":857,"passed_time":0.8498437906,"remaining_time":0.1406501378},
{"learn":[3.252845542],"iteration":858,"passed_time":0.8507452923,"remaining_time":0.1396450363},
{"learn":[3.252316026],"iteration":859,"passed_time":0.8515471837,"remaining_time":0.1386239601},
{"learn":[3.24975301],"iteration":860,"passed_time":0.8523896125,"remaining_time":0.1376099374},
{"learn":[3.249151075],"iteration":861,"passed_time":0.8533866465,"remaining_time":0.1366210641},
{"learn":[3.246257135],"iteration":862,"passed_time":0.8545165744,"remaining_time":0.1356532685},
{"learn":[3.243826471],"iteration":863,"passed_time":0.8553334644,"remaining_time":0.1346358231},
{"learn":[3.243190653],"iteration":864,"passed_time":0.8561447938,"remaining_time":0.1336179736},
{"learn":[3.24008797],"iteration":865,"passed_time":0.8568944054,"remaining_time":0.1325910512},
{"learn":[3.240036811],"iteration":866,"passed_time":0.8576533047,"remaining_time":0.1315661932},
{"learn":[3.238676314],"iteration":867,"passed_time":0.8583910736,"remaining_time":0.1305387347},
{"learn":[3.237848782],"iteration":868,"passed_time":0.8591411661,"remaining_time":0.1295138006},
{"learn":[3.236405498],"iteration":869,"passed_time":0.8599505718,"remaining_time":0.1284983613},
{"learn":[3.233378068],"iteration":870,"passed_time":0.860709912,"remaining_time":0.1274759801},
{"learn":[3.233169169],"iteration":871,"passed_time":0.8616892923,"remaining_time":0.1264865016},
{"learn":[3.232434885],"iteration":872,"passed_time":0.8627355604,"remaining_time":0.1255067768},
{"learn":[3.229978115],"iteration":873,"passed_time":0.8636052427,"remaining_time":0.1245014423},
{"learn":[3.229648848],"iteration":874,"passed_time":0.8644288656,"remaining_time":0.1234898379},
{"learn":[3.227208761],"iteration":875,"passed_time":0.8652186524,"remaining_time":0.1224738732},
{"learn":[3.226258869],"iteration":876,"passed_time":0.8660257437,"remaining_time":0.1214608512},
{"learn":[3.225331995],"iteration":877,"passed_time":0.8668854255,"remaining_time":0.1204556058},
{"learn":[3.221968268],"iteration":878,"passed_time":0.86786173,"remaining_time":0.1194667455},
{"learn":[3.221166317],"iteration":879,"passed_time":0.8686513379,"remaining_time":0.1184524552},
{"learn":[3.220047503],"iteration":880,"passed_time":0.8694447331,"remaining_time":0.1174391864},
{"learn":[3.21982781],"iteration":881,"passed_time":0.8701876619,"remaining_time":0.1164196645},
{"learn":[3.216693405],"iteration":882,"passed_time":0.8709465511,"remaining_time":0.1154028839},
{"learn":[3.214798761],"iteration":883,"passed_time":0.8716757237,"remaining_time":0.1143827873},
{"learn":[3.214395085],"iteration":884,"passed_time":0.8724810817,"remaining_time":0.1133732479},
{"learn":[3.213470696],"iteration":885,"passed_time":0.8732167867,"remaining_time":0.1123552073},
{"learn":[3.211595017],"iteration":886,"passed_time":0.8740905161,"remaining_time":0.1113553871},
{"learn":[3.210965255],"iteration":887,"passed_time":0.8749315815,"remaining_time":0.110351731},
{"learn":[3.209413583],"iteration":888,"passed_time":0.8759117333,"remaining_time":0.109365807},
{"learn":[3.208331683],"iteration":889,"passed_time":0.8766487708,"remaining_time":0.1083498481},
{"learn":[3.207110711],"iteration":890,"passed_time":0.8774626606,"remaining_time":0.1073439169},
{"learn":[3.204519413],"iteration":891,"passed_time":0.8782147325,"remaining_time":0.1063309317},
{"learn":[3.201421296],"iteration":892,"passed_time":0.8791576212,"remaining_time":0.1053413947},
{"learn":[3.200691259],"iteration":893,"passed_time":0.879961837,"remaining_time":0.1043355198},
{"learn":[3.200485067],"iteration":894,"passed_time":0.8806754899,"remaining_time":0.1033194709},
{"learn":[3.197467568],"iteration":895,"passed_time":0.8814195709,"remaining_time":0.1023076288},
{"learn":[3.195838544],"iteration":896,"passed_time":0.882142762,"remaining_time":0.1012939849},
{"learn":[3.195671746],"iteration":897,"passed_time":0.8828145048,"remaining_time":0.1002751442},
{"learn":[3.194213094],"iteration":898,"passed_time":0.8835961742,"remaining_time":0.09926942557},
{"learn":[3.192884691],"iteration":899,"passed_time":0.8843885274,"remaining_time":0.09826539193},
{"learn":[3.188364239],"iteration":900,"passed_time":0.885233767,"remaining_time":0.09726763921},
{"learn":[3.185219478],"iteration":901,"passed_time":0.8860860846,"remaining_time":0.09627099368},
{"learn":[3.184120387],"iteration":902,"passed_time":0.886896853,"remaining_time":0.09527020459},
{"learn":[3.183725321],"iteration":903,"passed_time":0.8877043651,"remaining_time":0.0942694901},
{"learn":[3.181264554],"iteration":904,"passed_time":0.8888048167,"remaining_time":0.09329995313},
{"learn":[3.180741589],"iteration":905,"passed_time":0.8895132596,"remaining_time":0.09228945519},
{"learn":[3.179782639],"iteration":906,"passed_time":0.8902743731,"remaining_time":0.09128502393},
{"learn":[3.176377564],"iteration":907,"passed_time":0.8909995079,"remaining_time":0.09027748318},
{"learn":[3.174078182],"iteration":908,"passed_time":0.8917746382,"remaining_time":0.08927556884},
{"learn":[3.171242379],"iteration":909,"passed_time":0.8926585362,"remaining_time":0.08828491018},
{"learn":[3.170421012],"iteration":910,"passed_time":0.8936441385,"remaining_time":0.08730442187},
{"learn":[3.170087224],"iteration":911,"passed_time":0.8945493815,"remaining_time":0.08631616839},
{"learn":[3.167303059],"iteration":912,"passed_time":0.8952699877,"remaining_time":0.08531050266},
{"learn":[3.16705966],"iteration":913,"passed_time":0.8959942508,"remaining_time":0.08430580478},
{"learn":[3.165667683],"iteration":914,"passed_time":0.8967707437,"remaining_time":0.08330657182},
{"learn":[3.164689733],"iteration":915,"passed_time":0.8974711413,"remaining_time":0.08230084702},
{"learn":[3.163311455],"iteration":916,"passed_time":0.8982181235,"remaining_time":0.08130000464},
{"learn":[3.159425016],"iteration":917,"passed_time":0.8991614639,"remaining_time":0.08031725495},
{"learn":[3.159327058],"iteration":918,"passed_time":0.8999201328,"remaining_time":0.0793183142},
{"learn":[3.15819426],"iteration":919,"passed_time":0.9007903246,"remaining_time":0.07832959344},
{"learn":[3.157086603],"iteration":920,"passed_time":0.9015883386,"remaining_time":0.07733493892},
{"learn":[3.153354154],"iteration":921,"passed_time":0.9022468862,"remaining_time":0.07632891228},
{"learn":[3.153261317],"iteration":922,"passed_time":0.9028857763,"remaining_time":0.07532199867},
{"learn":[3.153168454],"iteration":923,"passed_time":0.9035375911,"remaining_time":0.07431694472},
{"learn":[3.152080399],"iteration":924,"passed_time":0.9043389515,"remaining_time":0.07332477985},
{"learn":[3.151635144],"iteration":925,"passed_time":0.9050720415,"remaining_time":0.07232757135},
{"learn":[3.147762655],"iteration":926,"passed_time":0.9058667904,"remaining_time":0.07133578824},
{"learn":[3.147172317],"iteration":927,"passed_time":0.9067819982,"remaining_time":0.07035377572},
{"learn":[3.146254125],"iteration":928,"passed_time":0.9076665875,"remaining_time":0.06936956697},
{"learn":[3.144869828],"iteration":929,"passed_time":0.9084490518,"remaining_time":0.06837788562},
{"learn":[3.143466218],"iteration":930,"passed_time":0.9091640372,"remaining_time":0.0673816526},
{"learn":[3.141919643],"iteration":931,"passed_time":0.9099120858,"remaining_time":0.06638843544},
{"learn":[3.141054135],"iteration":932,"passed_time":0.9106209796,"remaining_time":0.06539293208},
{"learn":[3.139390417],"iteration":933,"passed_time":0.9113982983,"remaining_time":0.06440287761},
{"learn":[3.139025283],"iteration":934,"passed_time":0.9121650584,"remaining_time":0.06341254416},
{"learn":[3.137824183],"iteration":935,"passed_time":0.9129599364,"remaining_time":0.06242461103},
{"learn":[3.135620453],"iteration":936,"passed_time":0.9138412294,"remaining_time":0.06144290016},
{"learn":[3.13443178],"iteration":937,"passed_time":0.9146665756,"remaining_time":0.06045770542},
{"learn":[3.132765713],"iteration":938,"passed_time":0.9153912695,"remaining_time":0.0594663125},
{"learn":[3.131434124],"iteration":939,"passed_time":0.9161654881,"remaining_time":0.05847864818},
{"learn":[3.128384262],"iteration":940,"passed_time":0.9169538036,"remaining_time":0.05749232137},
{"learn":[3.128120455],"iteration":941,"passed_time":0.9177171614,"remaining_time":0.0565048783},
{"learn":[3.126314615],"iteration":942,"passed_time":0.9186290786,"remaining_time":0.05552689022},
{"learn":[3.125409666],"iteration":943,"passed_time":0.919507426,"remaining_time":0.05454705069},
{"learn":[3.123072589],"iteration":944,"passed_time":0.9202685495,"remaining_time":0.05356060341},
{"learn":[3.122921099],"iteration":945,"passed_time":0.9210585571,"remaining_time":0.05257628127},
{"learn":[3.122182662],"iteration":946,"passed_time":0.9218115952,"remaining_time":0.05159030047},
{"learn":[3.120040951],"iteration":947,"passed_time":0.9226150095,"remaining_time":0.05060757436},
{"learn":[3.118767799],"iteration":948,"passed_time":0.9233493519,"remaining_time":0.04962151417},
{"learn":[3.118203218],"iteration":949,"passed_time":0.9240890846,"remaining_time":0.04863626761},
{"learn":[3.116343362],"iteration":950,"passed_time":0.9249471132,"remaining_time":0.04765763254},
{"learn":[3.11480829],"iteration":951,"passed_time":0.9260795867,"remaining_time":0.04669308841},
{"learn":[3.112607903],"iteration":952,"passed_time":0.9267959949,"remaining_time":0.04570767236},
{"learn":[3.111661241],"iteration":953,"passed_time":0.927635448,"remaining_time":0.04472875326},
{"learn":[3.110249676],"iteration":954,"passed_time":0.9284088249,"remaining_time":0.04374701269},
{"learn":[3.107333579],"iteration":955,"passed_time":0.9291458625,"remaining_time":0.04276403551},
{"learn":[3.107149851],"iteration":956,"passed_time":0.9298913762,"remaining_time":0.04178195316},
{"learn":[3.106867336],"iteration":957,"passed_time":0.9307726083,"remaining_time":0.04080631477},
{"learn":[3.10364681],"iteration":958,"passed_time":0.9316011815,"remaining_time":0.03982862194},
{"learn":[3.102703811],"iteration":959,"passed_time":0.9325691291,"remaining_time":0.03885704705},
{"learn":[3.101469264],"iteration":960,"passed_time":0.9333575849,"remaining_time":0.03787819543},
{"learn":[3.09863569],"iteration":961,"passed_time":0.934116915,"remaining_time":0.03689858916},
{"learn":[3.09645939],"iteration":962,"passed_time":0.9348546338,"remaining_time":0.03591861002},
{"learn":[3.096240186],"iteration":963,"passed_time":0.9355498114,"remaining_time":0.03493754482},
{"learn":[3.094838828],"iteration":964,"passed_time":0.9362469027,"remaining_time":0.03395714155},
{"learn":[3.094176802],"iteration":965,"passed_time":0.9369527707,"remaining_time":0.03297763375},
{"learn":[3.093182279],"iteration":966,"passed_time":0.9376983646,"remaining_time":0.0320000476},
{"learn":[3.090150687],"iteration":967,"passed_time":0.9384536169,"remaining_time":0.03102326006},
{"learn":[3.088612829],"iteration":968,"passed_time":0.9393408524,"remaining_time":0.03005115214},
{"learn":[3.087153684],"iteration":969,"passed_time":0.9401041301,"remaining_time":0.02907538547},
{"learn":[3.085866843],"iteration":970,"passed_time":0.940956558,"remaining_time":0.02810271903},
{"learn":[3.082669094],"iteration":971,"passed_time":0.9416987954,"remaining_time":0.02712712579},
{"learn":[3.081047548],"iteration":972,"passed_time":0.9424532462,"remaining_time":0.02615235113},
{"learn":[3.079684322],"iteration":973,"passed_time":0.9431753352,"remaining_time":0.02517716501},
{"learn":[3.07613431],"iteration":974,"passed_time":0.9439061409,"remaining_time":0.02420272156},
{"learn":[3.074005935],"iteration":975,"passed_time":0.9448484647,"remaining_time":0.02323397864},
{"learn":[3.072988853],"iteration":976,"passed_time":0.9455877566,"remaining_time":0.02226051013},
{"learn":[3.072344268],"iteration":977,"passed_time":0.9463700563,"remaining_time":0.02128848797},
{"learn":[3.070654438],"iteration":978,"passed_time":0.9472095695,"remaining_time":0.02031808065},
{"learn":[3.069724506],"iteration":979,"passed_time":0.9479371991,"remaining_time":0.01934565712},
{"learn":[3.067763166],"iteration":980,"passed_time":0.9488508184,"remaining_time":0.01837733491},
{"learn":[3.066737893],"iteration":981,"passed_time":0.9498562391,"remaining_time":0.01741080683},
{"learn":[3.065248174],"iteration":982,"passed_time":0.9509666285,"remaining_time":0.01644601494},
{"learn":[3.063186837],"iteration":983,"passed_time":0.9519131898,"remaining_time":0.01547826325},
{"learn":[3.062880371],"iteration":984,"passed_time":0.9527262325,"remaining_time":0.01450852131},
{"learn":[3.061288645],"iteration":985,"passed_time":0.9535030761,"remaining_time":0.01353858323},
{"learn":[3.059970575],"iteration":986,"passed_time":0.9543421485,"remaining_time":0.01256985606},
{"learn":[3.059576341],"iteration":987,"passed_time":0.9552484994,"remaining_time":0.01160220849},
{"learn":[3.058175919],"iteration":988,"passed_time":0.9561627253,"remaining_time":0.01063477248},
{"learn":[3.056830702],"iteration":989,"passed_time":0.9569452798,"remaining_time":0.009666113937},
{"learn":[3.056336579],"iteration":990,"passed_time":0.9577918865,"remaining_time":0.008698412693},
{"learn":[3.055810414],"iteration":991,"passed_time":0.9585501947,"remaining_time":0.007730243506},
{"learn":[3.055476518],"iteration":992,"passed_time":0.9593350035,"remaining_time":0.006762683811},
{"learn":[3.053331734],"iteration":993,"passed_time":0.9600861981,"remaining_time":0.005795288922},
{"learn":[3.050890374],"iteration":994,"passed_time":0.9609256512,"remaining_time":0.004828772116},
{"learn":[3.04972623],"iteration":995,"passed_time":0.9616608853,"remaining_time":0.003862091909},
{"learn":[3.047217327],"iteration":996,"passed_time":0.9623554918,"remaining_time":0.002895753737},
{"learn":[3.047155483],"iteration":997,"passed_time":0.9631011057,"remaining_time":0.001930062336},
{"learn":[3.04430671],"iteration":998,"passed_time":0.9638549353,"remaining_time":0.0009648197551},
{"learn":[3.042664195],"iteration":999,"passed_time":0.9646871646,"remaining_time":0}
]}
```

## File: `Notebook_Experiments/catboost_info/learn_error.tsv`
```
iter	RMSE
0	14.59871775
1	14.22518863
2	13.8866124
3	13.52356875
4	13.18870211
5	12.9124226
6	12.60003351
7	12.32990573
8	12.0660619
9	11.77309809
10	11.49227636
11	11.26264833
12	11.04260393
13	10.79916926
14	10.5541002
15	10.31918115
16	10.10004441
17	9.894556723
18	9.690174082
19	9.506034866
20	9.338524633
21	9.170203312
22	9.010299969
23	8.843866678
24	8.690548059
25	8.555307687
26	8.413851302
27	8.29256019
28	8.162193833
29	8.040736294
30	7.921220278
31	7.809589039
32	7.699675801
33	7.60645267
34	7.498880302
35	7.401158744
36	7.306431077
37	7.223863468
38	7.143477682
39	7.062817131
40	6.990793435
41	6.931862224
42	6.858296558
43	6.786268161
44	6.717118549
45	6.652948106
46	6.589686076
47	6.531283097
48	6.471368031
49	6.416481395
50	6.369870822
51	6.325678067
52	6.275766122
53	6.224773967
54	6.182249254
55	6.139904173
56	6.100525536
57	6.062568564
58	6.030559288
59	5.997931376
60	5.964103835
61	5.933729724
62	5.901932711
63	5.873727795
64	5.846485734
65	5.820630862
66	5.793646238
67	5.765388646
68	5.747073912
69	5.722315217
70	5.699970599
71	5.682732647
72	5.663525791
73	5.642381613
74	5.621404779
75	5.602460129
76	5.587337574
77	5.572393026
78	5.558425806
79	5.541518902
80	5.526157283
81	5.511746977
82	5.504975022
83	5.493980522
84	5.480745463
85	5.464052013
86	5.449143727
87	5.438255432
88	5.425927931
89	5.412331217
90	5.400691499
91	5.391618744
92	5.380766572
93	5.372207183
94	5.362918837
95	5.348292324
96	5.339772295
97	5.331515983
98	5.323861644
99	5.313277281
100	5.30685627
101	5.29652059
102	5.288350766
103	5.27993346
104	5.271789139
105	5.262684686
106	5.251619772
107	5.241012171
108	5.232684032
109	5.224267141
110	5.216324968
111	5.211102527
112	5.206364257
113	5.196937641
114	5.190746047
115	5.181885213
116	5.178293568
117	5.170991438
118	5.166257212
119	5.161421246
120	5.158223542
121	5.15470988
122	5.146388143
123	5.139529364
124	5.134276023
125	5.128536065
126	5.123300353
127	5.116200518
128	5.108728704
129	5.104075866
130	5.100317606
131	5.095814182
132	5.092146915
133	5.085258329
134	5.079219421
135	5.076476829
136	5.072133867
137	5.067031564
138	5.061358312
139	5.056759124
140	5.050254
141	5.048376474
142	5.042603751
143	5.037477349
144	5.03230489
145	5.025976187
146	5.01952451
147	5.017569424
148	5.008962367
149	5.003880266
150	4.996387564
151	4.993361683
152	4.99005752
153	4.986908764
154	4.985207175
155	4.979003494
156	4.973142217
157	4.967056696
158	4.961460696
159	4.954240363
160	4.952320707
161	4.948337777
162	4.943228639
163	4.938545759
164	4.935330572
165	4.932051543
166	4.928964153
167	4.922860227
168	4.917668772
169	4.910365386
170	4.906457206
171	4.901996508
172	4.896816173
173	4.891123132
174	4.887630202
175	4.885259712
176	4.880659728
177	4.877299723
178	4.874038772
179	4.86943698
180	4.861268711
181	4.858673056
182	4.854036207
183	4.85130244
184	4.847510084
185	4.845691673
186	4.842058646
187	4.838623675
188	4.834602161
189	4.830858976
190	4.827590511
191	4.822246226
192	4.816686395
193	4.814797121
194	4.811639392
195	4.804813432
196	4.80251613
197	4.800087884
198	4.794773135
199	4.791664833
200	4.785989873
201	4.782387142
202	4.778623704
203	4.775772178
204	4.77023101
205	4.764496689
206	4.763138716
207	4.758053283
208	4.755063788
209	4.752465267
210	4.748067377
211	4.744163298
212	4.736670896
213	4.73349255
214	4.731864595
215	4.728398311
216	4.723865975
217	4.723483365
218	4.72095416
219	4.716173382
220	4.710563974
221	4.707160263
222	4.70408351
223	4.702501831
224	4.700269738
225	4.695346302
226	4.689769299
227	4.687919514
228	4.682982074
229	4.679578702
230	4.675751423
231	4.672710726
232	4.6690533
233	4.667595702
234	4.664241291
235	4.662246999
236	4.658668443
237	4.658017572
238	4.657656705
239	4.653242871
240	4.6507302
241	4.647671336
242	4.645506007
243	4.641297906
244	4.63798107
245	4.635062318
246	4.631606017
247	4.630215494
248	4.62729814
249	4.624691756
250	4.621840053
251	4.619602091
252	4.613584029
253	4.6119388
254	4.60870702
255	4.604771557
256	4.604231277
257	4.600750354
258	4.596488253
259	4.59470784
260	4.588818005
261	4.585054174
262	4.581471435
263	4.577555199
264	4.57457145
265	4.573029224
266	4.571326203
267	4.571019224
268	4.565766631
269	4.563383471
270	4.558165805
271	4.55629209
272	4.549383848
273	4.546227503
274	4.540620977
275	4.532898237
276	4.529757367
277	4.52579294
278	4.521572155
279	4.518818099
280	4.514012334
281	4.508331416
282	4.506038537
283	4.505805643
284	4.501550352
285	4.494692643
286	4.489330245
287	4.484826955
288	4.478285428
289	4.475311671
290	4.471581298
291	4.469164956
292	4.462068024
293	4.458540976
294	4.455757458
295	4.453027414
296	4.450659338
297	4.444696901
298	4.442052813
299	4.440036756
300	4.435017051
301	4.429962125
302	4.427666256
303	4.425030004
304	4.422588771
305	4.418936667
306	4.416887976
307	4.413773354
308	4.411129391
309	4.40850819
310	4.404880292
311	4.404593827
312	4.402139942
313	4.400284725
314	4.395805521
315	4.392838833
316	4.389213061
317	4.3861981
318	4.385054234
319	4.379364607
320	4.378387619
321	4.375816727
322	4.374600202
323	4.37098897
324	4.367418484
325	4.363584638
326	4.360770706
327	4.358675808
328	4.354228195
329	4.353773425
330	4.351648009
331	4.348209927
332	4.345852733
333	4.34237339
334	4.340814362
335	4.339707068
336	4.335430786
337	4.33521887
338	4.328507238
339	4.326140732
340	4.323785636
341	4.320632534
342	4.31973724
343	4.318000924
344	4.312713628
345	4.308220789
346	4.305890947
347	4.305137856
348	4.304787172
349	4.30350134
350	4.30293809
351	4.299548459
352	4.294768408
353	4.294581479
354	4.292551604
355	4.288628894
356	4.287802767
357	4.284566905
358	4.27890232
359	4.276938023
360	4.273425094
361	4.269726505
362	4.265565857
363	4.262117173
364	4.259185148
365	4.257668507
366	4.253432436
367	4.250216667
368	4.24514828
369	4.244015772
370	4.240329192
371	4.236718014
372	4.233495944
373	4.230357491
374	4.227381215
375	4.226169067
376	4.225963861
377	4.224346548
378	4.222595381
379	4.219700938
380	4.216356207
381	4.214326494
382	4.212901398
383	4.211331091
384	4.208624791
385	4.204659106
386	4.202968852
387	4.197261935
388	4.196934403
389	4.192479929
390	4.190243116
391	4.185852431
392	4.180967944
393	4.178283162
394	4.176341157
395	4.176041504
396	4.175564513
397	4.170830274
398	4.167804808
399	4.165860548
400	4.160950571
401	4.158544115
402	4.154448767
403	4.15197457
404	4.149562679
405	4.149327961
406	4.147444889
407	4.147254809
408	4.144589165
409	4.141691034
410	4.138893468
411	4.136964597
412	4.133773523
413	4.131363444
414	4.130228592
415	4.12884186
416	4.12413494
417	4.119422508
418	4.117038244
419	4.116067631
420	4.110343455
421	4.105604544
422	4.103390131
423	4.096724402
424	4.093431279
425	4.091412744
426	4.091192901
427	4.088994581
428	4.087845355
429	4.083650279
430	4.079840652
431	4.075707828
432	4.071345409
433	4.067460475
434	4.064914749
435	4.063823175
436	4.058898471
437	4.054120355
438	4.052715901
439	4.052114167
440	4.051377267
441	4.049275336
442	4.047099198
443	4.044348685
444	4.042822379
445	4.041258611
446	4.040044254
447	4.036860137
448	4.036372284
449	4.03368231
450	4.032439519
451	4.032008634
452	4.030034932
453	4.028173412
454	4.023806097
455	4.020239186
456	4.017384838
457	4.016468229
458	4.014530169
459	4.012884822
460	4.008924707
461	4.008286778
462	4.006444202
463	4.003284363
464	3.999811484
465	3.997483319
466	3.99708333
467	3.995860263
468	3.994131111
469	3.993125499
470	3.992954084
471	3.990635743
472	3.986678254
473	3.986393291
474	3.986152671
475	3.985596662
476	3.983853457
477	3.983263928
478	3.980067202
479	3.978115407
480	3.972661644
481	3.969938254
482	3.968211434
483	3.966113368
484	3.962246044
485	3.961319703
486	3.96078191
487	3.958913633
488	3.957428286
489	3.952641965
490	3.951486786
491	3.94938344
492	3.947297924
493	3.946284886
494	3.943288204
495	3.943076488
496	3.942347078
497	3.940251541
498	3.939011019
499	3.938760512
500	3.934522727
501	3.930091193
502	3.927671752
503	3.927280041
504	3.925987561
505	3.921645957
506	3.920333743
507	3.918659461
508	3.916124385
509	3.913849268
510	3.912826119
511	3.910034145
512	3.90792379
513	3.907823851
514	3.904527401
515	3.903378283
516	3.902170135
517	3.899435429
518	3.897497505
519	3.896426119
520	3.896044669
521	3.892795942
522	3.892413888
523	3.891738985
524	3.88822057
525	3.883837053
526	3.881769742
527	3.880356898
528	3.879250273
529	3.877174493
530	3.875854201
531	3.873189396
532	3.871583368
533	3.869622679
534	3.866860164
535	3.864498444
536	3.861416322
537	3.860265769
538	3.859328725
539	3.858521278
540	3.85599111
541	3.852379816
542	3.851327537
543	3.847854898
544	3.847083414
545	3.845397429
546	3.841933528
547	3.840996474
548	3.838355966
549	3.83342799
550	3.828161535
551	3.823502399
552	3.820068862
553	3.817951642
554	3.815785958
555	3.81503012
556	3.813529315
557	3.808881326
558	3.808740434
559	3.80714352
560	3.80573346
561	3.803370052
562	3.803215211
563	3.801309667
564	3.800003847
565	3.798026138
566	3.794745847
567	3.794312041
568	3.792205926
569	3.788991061
570	3.787391572
571	3.7826445
572	3.781700331
573	3.780045374
574	3.775462644
575	3.773711943
576	3.772415806
577	3.770170875
578	3.765166479
579	3.763976102
580	3.760761708
581	3.758155662
582	3.756844548
583	3.753098923
584	3.751618946
585	3.751398464
586	3.749920103
587	3.748237465
588	3.746021536
589	3.74417648
590	3.738788389
591	3.736021611
592	3.734546151
593	3.733527479
594	3.733026392
595	3.730314752
596	3.727342596
597	3.725459604
598	3.723158842
599	3.722362756
600	3.721443615
601	3.720743486
602	3.720215334
603	3.719436563
604	3.715046574
605	3.71443396
606	3.712938941
607	3.712814764
608	3.71235348
609	3.711223749
610	3.710755648
611	3.708668039
612	3.705623591
613	3.704045802
614	3.699915209
615	3.696182221
616	3.694263278
617	3.693810229
618	3.690900932
619	3.688020895
620	3.685491894
621	3.684328128
622	3.680640153
623	3.678932783
624	3.674167041
625	3.672200976
626	3.670606604
627	3.665506042
628	3.664214007
629	3.66261643
630	3.662118449
631	3.660871366
632	3.656695243
633	3.654497801
634	3.654189134
635	3.653957699
636	3.651920725
637	3.65106705
638	3.650612844
639	3.649884732
640	3.646276182
641	3.645808194
642	3.645042989
643	3.639864499
644	3.637318478
645	3.636344905
646	3.634754643
647	3.630724975
648	3.629408252
649	3.62790646
650	3.627388973
651	3.625163557
652	3.623701985
653	3.622342639
654	3.621130639
655	3.619125665
656	3.618878783
657	3.616207429
658	3.61206486
659	3.611955873
660	3.610713743
661	3.610044025
662	3.607342669
663	3.602510618
664	3.600492392
665	3.597171065
666	3.594358798
667	3.593945251
668	3.593607748
669	3.592238714
670	3.590144654
671	3.587151536
672	3.586070865
673	3.585102746
674	3.584362847
675	3.581407561
676	3.57919422
677	3.577632204
678	3.573911195
679	3.573408216
680	3.571076482
681	3.568177107
682	3.564824621
683	3.562475026
684	3.561226889
685	3.559383467
686	3.555209766
687	3.55345383
688	3.552300968
689	3.551253986
690	3.549807725
691	3.547992926
692	3.545438607
693	3.543313763
694	3.542962896
695	3.539800465
696	3.53953187
697	3.536332425
698	3.534993327
699	3.531637011
700	3.531040284
701	3.529973872
702	3.527325183
703	3.527200815
704	3.523459911
705	3.522729934
706	3.522260582
707	3.518641591
708	3.516856405
709	3.515083413
710	3.514671214
711	3.512617621
712	3.510747971
713	3.508149266
714	3.504557165
715	3.501367208
716	3.497593362
717	3.496291169
718	3.49330374
719	3.490044385
720	3.488891789
721	3.486869081
722	3.486303638
723	3.486035862
724	3.482668951
725	3.47820549
726	3.474392283
727	3.472268163
728	3.471209164
729	3.470049971
730	3.469078654
731	3.468643292
732	3.468134848
733	3.467820182
734	3.465776156
735	3.463037608
736	3.45965637
737	3.457275091
738	3.455522955
739	3.451270508
740	3.450978947
741	3.450608492
742	3.448122004
743	3.445646714
744	3.44411263
745	3.443264164
746	3.439521363
747	3.436809225
748	3.435509465
749	3.434450277
750	3.431786753
751	3.430150302
752	3.42696281
753	3.426870334
754	3.425200309
755	3.423383783
756	3.422752979
757	3.420845924
758	3.418917862
759	3.417095735
760	3.414391848
761	3.41426711
762	3.411976013
763	3.408614844
764	3.407906721
765	3.407494015
766	3.406287128
767	3.404600442
768	3.404012662
769	3.400398762
770	3.399737714
771	3.399185251
772	3.397245411
773	3.396229831
774	3.394002836
775	3.389617243
776	3.385426488
777	3.385072258
778	3.383842366
779	3.380110746
780	3.378595218
781	3.377371219
782	3.375814782
783	3.374195887
784	3.373704309
785	3.372971757
786	3.371565136
787	3.3700309
788	3.368186663
789	3.366710398
790	3.364598042
791	3.36348442
792	3.362001759
793	3.361580401
794	3.359543675
795	3.35766119
796	3.354592969
797	3.350985986
798	3.349589624
799	3.349110856
800	3.345315441
801	3.34397474
802	3.343800902
803	3.342329465
804	3.34220347
805	3.341279219
806	3.337329521
807	3.336708453
808	3.333252703
809	3.332186769
810	3.330594851
811	3.327867442
812	3.327563111
813	3.326308994
814	3.326249879
815	3.322336238
816	3.320491154
817	3.320434271
818	3.319609638
819	3.316182682
820	3.313126612
821	3.311222803
822	3.309627335
823	3.307974895
824	3.307321505
825	3.306759087
826	3.30484037
827	3.30201994
828	3.299302297
829	3.298132671
830	3.296976183
831	3.293144745
832	3.290284404
833	3.288285745
834	3.286662667
835	3.285692682
836	3.284565611
837	3.283897383
838	3.280712855
839	3.280468341
840	3.277814895
841	3.276316385
842	3.27557063
843	3.27499628
844	3.273569958
845	3.269665595
846	3.267984685
847	3.267702508
848	3.266671924
849	3.265359825
850	3.2618983
851	3.260456253
852	3.258389147
853	3.258108469
854	3.256424936
855	3.254817983
856	3.253898449
857	3.253023652
858	3.252845542
859	3.252316026
860	3.24975301
861	3.249151075
862	3.246257135
863	3.243826471
864	3.243190653
865	3.24008797
866	3.240036811
867	3.238676314
868	3.237848782
869	3.236405498
870	3.233378068
871	3.233169169
872	3.232434885
873	3.229978115
874	3.229648848
875	3.227208761
876	3.226258869
877	3.225331995
878	3.221968268
879	3.221166317
880	3.220047503
881	3.21982781
882	3.216693405
883	3.214798761
884	3.214395085
885	3.213470696
886	3.211595017
887	3.210965255
888	3.209413583
889	3.208331683
890	3.207110711
891	3.204519413
892	3.201421296
893	3.200691259
894	3.200485067
895	3.197467568
896	3.195838544
897	3.195671746
898	3.194213094
899	3.192884691
900	3.188364239
901	3.185219478
902	3.184120387
903	3.183725321
904	3.181264554
905	3.180741589
906	3.179782639
907	3.176377564
908	3.174078182
909	3.171242379
910	3.170421012
911	3.170087224
912	3.167303059
913	3.16705966
914	3.165667683
915	3.164689733
916	3.163311455
917	3.159425016
918	3.159327058
919	3.15819426
920	3.157086603
921	3.153354154
922	3.153261317
923	3.153168454
924	3.152080399
925	3.151635144
926	3.147762655
927	3.147172317
928	3.146254125
929	3.144869828
930	3.143466218
931	3.141919643
932	3.141054135
933	3.139390417
934	3.139025283
935	3.137824183
936	3.135620453
937	3.13443178
938	3.132765713
939	3.131434124
940	3.128384262
941	3.128120455
942	3.126314615
943	3.125409666
944	3.123072589
945	3.122921099
946	3.122182662
947	3.120040951
948	3.118767799
949	3.118203218
950	3.116343362
951	3.11480829
952	3.112607903
953	3.111661241
954	3.110249676
955	3.107333579
956	3.107149851
957	3.106867336
958	3.10364681
959	3.102703811
960	3.101469264
961	3.09863569
962	3.09645939
963	3.096240186
964	3.094838828
965	3.094176802
966	3.093182279
967	3.090150687
968	3.088612829
969	3.087153684
970	3.085866843
971	3.082669094
972	3.081047548
973	3.079684322
974	3.07613431
975	3.074005935
976	3.072988853
977	3.072344268
978	3.070654438
979	3.069724506
980	3.067763166
981	3.066737893
982	3.065248174
983	3.063186837
984	3.062880371
985	3.061288645
986	3.059970575
987	3.059576341
988	3.058175919
989	3.056830702
990	3.056336579
991	3.055810414
992	3.055476518
993	3.053331734
994	3.050890374
995	3.04972623
996	3.047217327
997	3.047155483
998	3.04430671
999	3.042664195
```

## File: `Notebook_Experiments/catboost_info/time_left.tsv`
```
iter	Passed	Remaining
0	147	147640
1	148	74209
2	149	49696
3	150	37425
4	151	30082
5	152	25201
6	153	21716
7	154	19099
8	154	17048
9	155	15408
10	156	14059
11	157	12935
12	157	11993
13	158	11186
14	159	10486
15	160	9875
16	161	9332
17	162	8844
18	162	8412
19	163	8035
20	165	7711
21	166	7395
22	167	7110
23	168	6842
24	169	6592
25	169	6361
26	170	6155
27	171	5962
28	172	5775
29	173	5600
30	174	5439
31	174	5289
32	175	5147
33	176	5012
34	177	4884
35	177	4766
36	178	4651
37	179	4542
38	180	4440
39	180	4342
40	181	4253
41	182	4170
42	184	4096
43	184	4017
44	185	3941
45	186	3871
46	187	3801
47	188	3733
48	189	3669
49	189	3607
50	190	3546
51	191	3488
52	192	3431
53	192	3376
54	193	3324
55	194	3273
56	194	3223
57	195	3177
58	196	3134
59	197	3093
60	198	3050
61	198	3009
62	199	2969
63	200	2931
64	201	2894
65	202	2865
66	203	2830
67	204	2797
68	204	2764
69	205	2731
70	206	2700
71	207	2671
72	208	2642
73	209	2616
74	209	2587
75	210	2560
76	211	2533
77	212	2507
78	212	2481
79	213	2457
80	214	2434
81	215	2410
82	215	2383
83	216	2361
84	217	2339
85	218	2317
86	218	2297
87	219	2277
88	220	2257
89	221	2238
90	222	2220
91	222	2200
92	223	2181
93	224	2163
94	225	2148
95	226	2131
96	227	2117
97	228	2101
98	229	2085
99	229	2069
100	230	2053
101	231	2037
102	232	2021
103	232	2006
104	233	1991
105	234	1977
106	235	1962
107	235	1948
108	236	1935
109	237	1921
110	238	1910
111	239	1897
112	240	1884
113	241	1873
114	241	1861
115	243	1853
116	244	1841
117	245	1831
118	245	1819
119	246	1808
120	247	1797
121	247	1784
122	248	1773
123	249	1764
124	250	1753
125	251	1743
126	251	1732
127	252	1722
128	253	1712
129	254	1704
130	255	1694
131	256	1684
132	257	1675
133	257	1666
134	258	1658
135	259	1648
136	260	1640
137	261	1631
138	261	1622
139	262	1614
140	263	1607
141	264	1597
142	265	1589
143	266	1582
144	267	1574
145	267	1566
146	268	1558
147	269	1550
148	270	1542
149	270	1535
150	271	1527
151	272	1520
152	273	1513
153	274	1506
154	275	1499
155	275	1492
156	276	1485
157	277	1478
158	278	1471
159	279	1464
160	279	1457
161	280	1451
162	281	1445
163	282	1439
164	283	1433
165	283	1426
166	284	1419
167	285	1413
168	286	1407
169	287	1401
170	287	1394
171	288	1388
172	289	1382
173	289	1376
174	290	1370
175	291	1364
176	292	1361
177	293	1356
178	294	1350
179	295	1344
180	295	1339
181	296	1333
182	297	1328
183	298	1322
184	299	1317
185	299	1312
186	300	1307
187	301	1302
188	302	1297
189	303	1292
190	304	1287
191	304	1282
192	305	1277
193	306	1273
194	307	1268
195	308	1264
196	309	1260
197	309	1255
198	310	1250
199	311	1245
200	312	1241
201	313	1237
202	313	1232
203	314	1228
204	315	1224
205	316	1219
206	317	1215
207	318	1211
208	318	1206
209	319	1202
210	320	1198
211	321	1193
212	321	1189
213	322	1185
214	323	1181
215	324	1177
216	325	1173
217	325	1169
218	326	1165
219	327	1161
220	328	1157
221	329	1153
222	329	1149
223	330	1145
224	331	1141
225	332	1137
226	332	1133
227	333	1130
228	334	1126
229	335	1122
230	336	1119
231	337	1116
232	338	1112
233	338	1109
234	339	1105
235	340	1102
236	341	1098
237	341	1094
238	342	1091
239	343	1087
240	344	1084
241	345	1081
242	346	1077
243	346	1074
244	347	1071
245	348	1067
246	349	1064
247	350	1061
248	350	1058
249	351	1054
250	352	1051
251	353	1048
252	354	1045
253	354	1042
254	355	1039
255	356	1035
256	357	1032
257	357	1029
258	358	1026
259	359	1022
260	360	1019
261	360	1016
262	361	1013
263	362	1009
264	363	1007
265	363	1003
266	364	1000
267	365	997
268	366	995
269	367	992
270	368	990
271	368	987
272	369	984
273	370	981
274	371	979
275	372	976
276	372	973
277	373	970
278	374	967
279	375	964
280	376	963
281	377	960
282	377	957
283	378	954
284	379	952
285	380	949
286	381	946
287	381	944
288	382	941
289	383	938
290	384	935
291	384	933
292	385	930
293	386	928
294	387	925
295	388	923
296	388	920
297	389	918
298	390	915
299	391	913
300	392	911
301	393	908
302	394	906
303	394	903
304	395	901
305	396	898
306	397	896
307	398	894
308	399	892
309	400	891
310	401	888
311	402	886
312	403	884
313	403	882
314	404	879
315	405	877
316	406	874
317	406	872
318	407	869
319	408	867
320	408	865
321	409	862
322	410	860
323	411	858
324	412	856
325	413	853
326	413	851
327	414	849
328	415	846
329	416	844
330	416	842
331	417	840
332	418	838
333	419	836
334	420	834
335	420	831
336	421	829
337	422	827
338	423	825
339	424	823
340	424	820
341	425	818
342	426	816
343	426	814
344	427	811
345	428	809
346	429	808
347	430	807
348	431	805
349	432	803
350	433	801
351	434	799
352	434	797
353	435	795
354	436	793
355	437	791
356	438	788
357	438	786
358	439	784
359	440	782
360	441	781
361	442	778
362	442	776
363	443	774
364	444	772
365	445	770
366	445	769
367	446	767
368	447	765
369	448	764
370	449	762
371	450	760
372	451	758
373	452	756
374	453	755
375	453	753
376	454	751
377	455	749
378	456	747
379	457	746
380	457	744
381	458	742
382	459	740
383	460	738
384	461	737
385	462	735
386	462	733
387	463	731
388	464	729
389	465	727
390	465	725
391	466	723
392	467	721
393	468	720
394	469	718
395	469	716
396	470	714
397	471	713
398	472	711
399	473	709
400	473	707
401	474	706
402	475	704
403	476	702
404	477	700
405	477	698
406	478	697
407	479	696
408	480	694
409	481	692
410	481	690
411	482	688
412	483	687
413	484	685
414	485	683
415	485	682
416	486	680
417	487	679
418	488	677
419	489	675
420	489	673
421	490	672
422	491	670
423	492	668
424	493	667
425	493	665
426	494	663
427	495	662
428	496	660
429	497	658
430	497	657
431	498	655
432	499	653
433	499	652
434	500	650
435	501	648
436	502	646
437	503	645
438	503	643
439	504	642
440	505	640
441	506	639
442	507	637
443	507	636
444	508	634
445	509	632
446	510	631
447	510	629
448	511	628
449	512	626
450	513	624
451	514	623
452	515	621
453	515	620
454	516	618
455	517	617
456	518	616
457	519	614
458	519	612
459	520	611
460	521	609
461	522	608
462	523	607
463	525	606
464	526	605
465	526	603
466	527	602
467	528	600
468	529	599
469	529	597
470	530	596
471	531	594
472	532	593
473	533	592
474	534	591
475	535	589
476	536	588
477	537	586
478	537	585
479	538	583
480	539	582
481	540	580
482	541	579
483	541	577
484	542	576
485	543	574
486	544	573
487	545	572
488	546	570
489	547	569
490	547	568
491	548	566
492	549	565
493	550	563
494	551	562
495	551	560
496	552	559
497	554	558
498	555	557
499	555	555
500	556	554
501	557	553
502	558	551
503	559	550
504	559	548
505	560	547
506	561	545
507	562	544
508	563	543
509	564	541
510	564	540
511	565	539
512	566	537
513	567	536
514	568	535
515	569	533
516	569	532
517	570	531
518	571	529
519	572	528
520	572	526
521	573	525
522	574	523
523	575	522
524	576	521
525	576	519
526	577	518
527	578	517
528	579	515
529	580	514
530	580	513
531	581	511
532	582	510
533	583	509
534	584	507
535	585	506
536	586	505
537	587	504
538	587	502
539	588	501
540	589	500
541	590	499
542	591	497
543	592	496
544	593	495
545	593	493
546	594	492
547	595	491
548	596	489
549	597	488
550	597	487
551	598	485
552	599	484
553	600	483
554	600	481
555	601	480
556	602	479
557	603	477
558	604	476
559	604	475
560	605	473
561	606	472
562	606	471
563	607	469
564	608	468
565	609	467
566	609	465
567	610	464
568	611	463
569	612	461
570	613	460
571	613	459
572	614	458
573	615	456
574	616	455
575	617	454
576	617	452
577	618	451
578	619	450
579	620	449
580	621	447
581	621	446
582	622	445
583	623	444
584	624	442
585	624	441
586	625	440
587	626	439
588	627	438
589	628	437
590	629	435
591	630	434
592	631	433
593	632	431
594	632	430
595	633	429
596	634	428
597	635	427
598	636	425
599	636	424
600	638	423
601	639	422
602	639	421
603	640	420
604	641	418
605	642	417
606	642	416
607	643	414
608	644	413
609	645	412
610	645	411
611	647	410
612	647	409
613	648	407
614	649	406
615	650	405
616	651	404
617	651	402
618	652	401
619	653	400
620	654	399
621	655	398
622	656	396
623	656	395
624	657	394
625	658	393
626	659	392
627	660	390
628	660	389
629	661	388
630	662	387
631	663	386
632	663	384
633	664	383
634	665	382
635	666	381
636	667	380
637	667	378
638	668	377
639	669	376
640	670	375
641	671	374
642	671	373
643	673	372
644	673	370
645	674	369
646	675	368
647	676	367
648	677	366
649	678	365
650	679	364
651	679	362
652	680	361
653	681	360
654	682	359
655	682	358
656	683	356
657	684	355
658	685	354
659	686	353
660	687	352
661	687	351
662	688	350
663	689	348
664	690	348
665	691	346
666	692	345
667	693	344
668	694	343
669	695	342
670	695	341
671	696	340
672	697	338
673	698	337
674	699	336
675	699	335
676	700	334
677	701	333
678	702	331
679	702	330
680	703	329
681	704	328
682	705	327
683	705	326
684	706	325
685	707	323
686	708	322
687	709	321
688	710	320
689	711	319
690	711	318
691	712	317
692	713	316
693	714	315
694	715	313
695	716	312
696	716	311
697	717	310
698	718	309
699	719	308
700	720	307
701	720	306
702	721	304
703	722	303
704	723	302
705	723	301
706	724	300
707	725	299
708	726	298
709	727	297
710	728	296
711	729	295
712	730	293
713	730	292
714	731	291
715	732	290
716	733	289
717	734	288
718	734	287
719	735	286
720	736	285
721	737	283
722	738	282
723	739	281
724	739	280
725	740	279
726	741	278
727	742	277
728	743	276
729	744	275
730	744	274
731	745	272
732	746	271
733	747	270
734	748	269
735	748	268
736	749	267
737	750	266
738	751	265
739	752	264
740	753	263
741	753	262
742	754	260
743	755	259
744	755	258
745	756	257
746	757	256
747	758	255
748	759	254
749	759	253
750	760	252
751	761	251
752	762	250
753	763	249
754	764	247
755	764	246
756	765	245
757	766	244
758	767	243
759	768	242
760	769	241
761	770	240
762	770	239
763	771	238
764	772	237
765	773	236
766	774	235
767	774	234
768	775	232
769	776	231
770	777	230
771	778	229
772	778	228
773	779	227
774	780	226
775	781	225
776	782	224
777	783	223
778	784	222
779	785	221
780	785	220
781	786	219
782	787	218
783	788	217
784	789	216
785	790	215
786	791	214
787	791	213
788	792	211
789	793	210
790	794	209
791	794	208
792	795	207
793	796	206
794	797	205
795	797	204
796	798	203
797	799	202
798	800	201
799	801	200
800	802	199
801	803	198
802	804	197
803	805	196
804	806	195
805	806	194
806	807	193
807	808	192
808	809	191
809	810	190
810	811	189
811	812	188
812	812	186
813	813	185
814	814	184
815	815	183
816	816	182
817	817	181
818	818	180
819	818	179
820	819	178
821	820	177
822	821	176
823	821	175
824	822	174
825	823	173
826	824	172
827	825	171
828	826	170
829	826	169
830	827	168
831	828	167
832	829	166
833	830	165
834	830	164
835	831	163
836	832	162
837	833	161
838	834	160
839	834	159
840	835	157
841	836	156
842	837	155
843	838	154
844	838	153
845	839	152
846	840	151
847	841	150
848	842	149
849	843	148
850	843	147
851	844	146
852	845	145
853	846	144
854	847	143
855	848	142
856	848	141
857	849	140
858	850	139
859	851	138
860	852	137
861	853	136
862	854	135
863	855	134
864	856	133
865	856	132
866	857	131
867	858	130
868	859	129
869	859	128
870	860	127
871	861	126
872	862	125
873	863	124
874	864	123
875	865	122
876	866	121
877	866	120
878	867	119
879	868	118
880	869	117
881	870	116
882	870	115
883	871	114
884	872	113
885	873	112
886	874	111
887	874	110
888	875	109
889	876	108
890	877	107
891	878	106
892	879	105
893	879	104
894	880	103
895	881	102
896	882	101
897	882	100
898	883	99
899	884	98
900	885	97
901	886	96
902	886	95
903	887	94
904	888	93
905	889	92
906	890	91
907	890	90
908	891	89
909	892	88
910	893	87
911	894	86
912	895	85
913	895	84
914	896	83
915	897	82
916	898	81
917	899	80
918	899	79
919	900	78
920	901	77
921	902	76
922	902	75
923	903	74
924	904	73
925	905	72
926	905	71
927	906	70
928	907	69
929	908	68
930	909	67
931	909	66
932	910	65
933	911	64
934	912	63
935	912	62
936	913	61
937	914	60
938	915	59
939	916	58
940	916	57
941	917	56
942	918	55
943	919	54
944	920	53
945	921	52
946	921	51
947	922	50
948	923	49
949	924	48
950	924	47
951	926	46
952	926	45
953	927	44
954	928	43
955	929	42
956	929	41
957	930	40
958	931	39
959	932	38
960	933	37
961	934	36
962	934	35
963	935	34
964	936	33
965	936	32
966	937	32
967	938	31
968	939	30
969	940	29
970	940	28
971	941	27
972	942	26
973	943	25
974	943	24
975	944	23
976	945	22
977	946	21
978	947	20
979	947	19
980	948	18
981	949	17
982	950	16
983	951	15
984	952	14
985	953	13
986	954	12
987	955	11
988	956	10
989	956	9
990	957	8
991	958	7
992	959	6
993	960	5
994	960	4
995	961	3
996	962	2
997	963	1
998	963	0
999	964	0
```

## File: `Notebook_Experiments/Data/stud.csv`
```
"gender","race_ethnicity","parental_level_of_education","lunch","test_preparation_course","math_score","reading_score","writing_score"
"female","group B","bachelor's degree","standard","none","72","72","74"
"female","group C","some college","standard","completed","69","90","88"
"female","group B","master's degree","standard","none","90","95","93"
"male","group A","associate's degree","free/reduced","none","47","57","44"
"male","group C","some college","standard","none","76","78","75"
"female","group B","associate's degree","standard","none","71","83","78"
"female","group B","some college","standard","completed","88","95","92"
"male","group B","some college","free/reduced","none","40","43","39"
"male","group D","high school","free/reduced","completed","64","64","67"
"female","group B","high school","free/reduced","none","38","60","50"
"male","group C","associate's degree","standard","none","58","54","52"
"male","group D","associate's degree","standard","none","40","52","43"
"female","group B","high school","standard","none","65","81","73"
"male","group A","some college","standard","completed","78","72","70"
"female","group A","master's degree","standard","none","50","53","58"
"female","group C","some high school","standard","none","69","75","78"
"male","group C","high school","standard","none","88","89","86"
"female","group B","some high school","free/reduced","none","18","32","28"
"male","group C","master's degree","free/reduced","completed","46","42","46"
"female","group C","associate's degree","free/reduced","none","54","58","61"
"male","group D","high school","standard","none","66","69","63"
"female","group B","some college","free/reduced","completed","65","75","70"
"male","group D","some college","standard","none","44","54","53"
"female","group C","some high school","standard","none","69","73","73"
"male","group D","bachelor's degree","free/reduced","completed","74","71","80"
"male","group A","master's degree","free/reduced","none","73","74","72"
"male","group B","some college","standard","none","69","54","55"
"female","group C","bachelor's degree","standard","none","67","69","75"
"male","group C","high school","standard","none","70","70","65"
"female","group D","master's degree","standard","none","62","70","75"
"female","group D","some college","standard","none","69","74","74"
"female","group B","some college","standard","none","63","65","61"
"female","group E","master's degree","free/reduced","none","56","72","65"
"male","group D","some college","standard","none","40","42","38"
"male","group E","some college","standard","none","97","87","82"
"male","group E","associate's degree","standard","completed","81","81","79"
"female","group D","associate's degree","standard","none","74","81","83"
"female","group D","some high school","free/reduced","none","50","64","59"
"female","group D","associate's degree","free/reduced","completed","75","90","88"
"male","group B","associate's degree","free/reduced","none","57","56","57"
"male","group C","associate's degree","free/reduced","none","55","61","54"
"female","group C","associate's degree","standard","none","58","73","68"
"female","group B","associate's degree","standard","none","53","58","65"
"male","group B","some college","free/reduced","completed","59","65","66"
"female","group E","associate's degree","free/reduced","none","50","56","54"
"male","group B","associate's degree","standard","none","65","54","57"
"female","group A","associate's degree","standard","completed","55","65","62"
"female","group C","high school","standard","none","66","71","76"
"female","group D","associate's degree","free/reduced","completed","57","74","76"
"male","group C","high school","standard","completed","82","84","82"
"male","group E","some college","standard","none","53","55","48"
"male","group E","associate's degree","free/reduced","completed","77","69","68"
"male","group C","some college","standard","none","53","44","42"
"male","group D","high school","standard","none","88","78","75"
"female","group C","some high school","free/reduced","completed","71","84","87"
"female","group C","high school","free/reduced","none","33","41","43"
"female","group E","associate's degree","standard","completed","82","85","86"
"male","group D","associate's degree","standard","none","52","55","49"
"male","group D","some college","standard","completed","58","59","58"
"female","group C","some high school","free/reduced","none","0","17","10"
"male","group E","bachelor's degree","free/reduced","completed","79","74","72"
"male","group A","some high school","free/reduced","none","39","39","34"
"male","group A","associate's degree","free/reduced","none","62","61","55"
"female","group C","associate's degree","standard","none","69","80","71"
"female","group D","some high school","standard","none","59","58","59"
"male","group B","some high school","standard","none","67","64","61"
"male","group D","some high school","free/reduced","none","45","37","37"
"female","group C","some college","standard","none","60","72","74"
"male","group B","associate's degree","free/reduced","none","61","58","56"
"female","group C","associate's degree","standard","none","39","64","57"
"female","group D","some college","free/reduced","completed","58","63","73"
"male","group D","some college","standard","completed","63","55","63"
"female","group A","associate's degree","free/reduced","none","41","51","48"
"male","group C","some high school","free/reduced","none","61","57","56"
"male","group C","some high school","standard","none","49","49","41"
"male","group B","associate's degree","free/reduced","none","44","41","38"
"male","group E","some high school","standard","none","30","26","22"
"male","group A","bachelor's degree","standard","completed","80","78","81"
"female","group D","some high school","standard","completed","61","74","72"
"female","group E","master's degree","standard","none","62","68","68"
"female","group B","associate's degree","standard","none","47","49","50"
"male","group B","high school","free/reduced","none","49","45","45"
"male","group A","some college","free/reduced","completed","50","47","54"
"male","group E","associate's degree","standard","none","72","64","63"
"male","group D","high school","free/reduced","none","42","39","34"
"female","group C","some college","standard","none","73","80","82"
"female","group C","some college","free/reduced","none","76","83","88"
"female","group D","associate's degree","standard","none","71","71","74"
"female","group A","some college","standard","none","58","70","67"
"female","group D","some high school","standard","none","73","86","82"
"female","group C","bachelor's degree","standard","none","65","72","74"
"male","group C","high school","free/reduced","none","27","34","36"
"male","group C","high school","standard","none","71","79","71"
"male","group C","associate's degree","free/reduced","completed","43","45","50"
"female","group B","some college","standard","none","79","86","92"
"male","group C","associate's degree","free/reduced","completed","78","81","82"
"male","group B","some high school","standard","completed","65","66","62"
"female","group E","some college","standard","completed","63","72","70"
"female","group D","some college","free/reduced","none","58","67","62"
"female","group D","bachelor's degree","standard","none","65","67","62"
"male","group B","some college","standard","none","79","67","67"
"male","group D","bachelor's degree","standard","completed","68","74","74"
"female","group D","associate's degree","standard","none","85","91","89"
"male","group B","high school","standard","completed","60","44","47"
"male","group C","some college","standard","completed","98","86","90"
"female","group C","some college","standard","none","58","67","72"
"female","group D","master's degree","standard","none","87","100","100"
"male","group E","associate's degree","standard","completed","66","63","64"
"female","group B","associate's degree","free/reduced","none","52","76","70"
"female","group B","some high school","standard","none","70","64","72"
"female","group D","associate's degree","free/reduced","completed","77","89","98"
"male","group C","high school","standard","none","62","55","49"
"male","group A","associate's degree","standard","none","54","53","47"
"female","group D","some college","standard","none","51","58","54"
"female","group E","bachelor's degree","standard","completed","99","100","100"
"male","group C","high school","standard","none","84","77","74"
"female","group B","bachelor's degree","free/reduced","none","75","85","82"
"female","group D","bachelor's degree","standard","none","78","82","79"
"female","group D","some high school","standard","none","51","63","61"
"female","group C","some college","standard","none","55","69","65"
"female","group C","bachelor's degree","standard","completed","79","92","89"
"male","group B","associate's degree","standard","completed","91","89","92"
"female","group C","some college","standard","completed","88","93","93"
"male","group D","high school","free/reduced","none","63","57","56"
"male","group E","some college","standard","none","83","80","73"
"female","group B","high school","standard","none","87","95","86"
"male","group B","some high school","standard","none","72","68","67"
"male","group D","some college","standard","completed","65","77","74"
"male","group D","master's degree","standard","none","82","82","74"
"female","group A","bachelor's degree","standard","none","51","49","51"
"male","group D","master's degree","standard","none","89","84","82"
"male","group C","some high school","free/reduced","completed","53","37","40"
"male","group E","some college","free/reduced","completed","87","74","70"
"female","group C","some college","standard","completed","75","81","84"
"male","group D","bachelor's degree","free/reduced","completed","74","79","75"
"male","group C","bachelor's degree","standard","none","58","55","48"
"male","group B","some high school","standard","completed","51","54","41"
"male","group E","high school","standard","none","70","55","56"
"female","group C","associate's degree","standard","none","59","66","67"
"male","group D","some college","standard","completed","71","61","69"
"female","group D","some high school","standard","none","76","72","71"
"female","group C","some college","free/reduced","none","59","62","64"
"female","group E","some college","free/reduced","completed","42","55","54"
"male","group A","high school","standard","none","57","43","47"
"male","group D","some college","standard","none","88","73","78"
"female","group C","some college","free/reduced","none","22","39","33"
"male","group B","some high school","standard","none","88","84","75"
"male","group C","associate's degree","free/reduced","none","73","68","66"
"female","group D","bachelor's degree","standard","completed","68","75","81"
"male","group E","associate's degree","free/reduced","completed","100","100","93"
"male","group A","some high school","standard","completed","62","67","69"
"male","group A","bachelor's degree","standard","none","77","67","68"
"female","group B","associate's degree","standard","completed","59","70","66"
"male","group D","bachelor's degree","standard","none","54","49","47"
"male","group D","some high school","standard","none","62","67","61"
"female","group C","some college","standard","completed","70","89","88"
"female","group E","high school","free/reduced","completed","66","74","78"
"male","group B","some college","free/reduced","none","60","60","60"
"female","group B","associate's degree","standard","completed","61","86","87"
"male","group D","associate's degree","free/reduced","none","66","62","64"
"male","group B","associate's degree","free/reduced","completed","82","78","74"
"female","group E","some college","free/reduced","completed","75","88","85"
"male","group B","master's degree","free/reduced","none","49","53","52"
"male","group C","high school","standard","none","52","53","49"
"female","group E","master's degree","standard","none","81","92","91"
"female","group C","bachelor's degree","standard","completed","96","100","100"
"male","group C","high school","free/reduced","completed","53","51","51"
"female","group B","master's degree","free/reduced","completed","58","76","78"
"female","group B","high school","standard","completed","68","83","78"
"female","group C","some college","free/reduced","completed","67","75","70"
"male","group A","high school","standard","completed","72","73","74"
"male","group E","some high school","standard","none","94","88","78"
"female","group D","some college","standard","none","79","86","81"
"female","group C","associate's degree","standard","none","63","67","70"
"female","group C","bachelor's degree","free/reduced","completed","43","51","54"
"female","group C","master's degree","standard","completed","81","91","87"
"female","group B","high school","free/reduced","completed","46","54","58"
"female","group C","associate's degree","standard","completed","71","77","77"
"female","group B","master's degree","free/reduced","completed","52","70","62"
"female","group D","some high school","standard","completed","97","100","100"
"male","group C","master's degree","free/reduced","completed","62","68","75"
"female","group C","some college","free/reduced","none","46","64","66"
"female","group E","high school","standard","none","50","50","47"
"female","group D","associate's degree","standard","none","65","69","70"
"male","group C","some high school","free/reduced","completed","45","52","49"
"male","group C","associate's degree","free/reduced","completed","65","67","65"
"male","group E","high school","standard","none","80","76","65"
"male","group D","some high school","standard","completed","62","66","68"
"male","group B","some high school","free/reduced","none","48","52","45"
"female","group C","bachelor's degree","standard","none","77","88","87"
"female","group E","associate's degree","standard","none","66","65","69"
"male","group D","some college","standard","completed","76","83","79"
"female","group B","some high school","standard","none","62","64","66"
"male","group D","some college","standard","completed","77","62","62"
"female","group C","master's degree","standard","completed","69","84","85"
"male","group D","associate's degree","standard","none","61","55","52"
"male","group C","some high school","free/reduced","completed","59","69","65"
"male","group E","high school","free/reduced","none","55","56","51"
"female","group B","some college","free/reduced","none","45","53","55"
"female","group B","bachelor's degree","free/reduced","none","78","79","76"
"female","group C","associate's degree","standard","completed","67","84","86"
"female","group D","some college","free/reduced","none","65","81","77"
"male","group C","associate's degree","standard","none","69","77","69"
"female","group B","associate's degree","standard","none","57","69","68"
"male","group C","some college","standard","none","59","41","42"
"male","group D","some high school","standard","completed","74","71","78"
"male","group E","bachelor's degree","standard","none","82","62","62"
"male","group E","high school","standard","completed","81","80","76"
"female","group B","some college","free/reduced","none","74","81","76"
"female","group B","some college","free/reduced","none","58","61","66"
"male","group D","some high school","free/reduced","completed","80","79","79"
"male","group C","some college","free/reduced","none","35","28","27"
"female","group C","high school","free/reduced","none","42","62","60"
"male","group C","associate's degree","free/reduced","completed","60","51","56"
"male","group E","high school","standard","completed","87","91","81"
"male","group B","some high school","standard","completed","84","83","75"
"female","group E","associate's degree","free/reduced","completed","83","86","88"
"female","group C","high school","free/reduced","none","34","42","39"
"male","group B","high school","free/reduced","none","66","77","70"
"male","group B","some high school","standard","completed","61","56","56"
"female","group D","high school","standard","completed","56","68","74"
"male","group B","associate's degree","standard","none","87","85","73"
"female","group C","some high school","free/reduced","none","55","65","62"
"male","group D","some high school","standard","none","86","80","75"
"female","group B","associate's degree","standard","completed","52","66","73"
"female","group E","master's degree","free/reduced","none","45","56","54"
"female","group C","some college","standard","none","72","72","71"
"male","group D","high school","standard","none","57","50","54"
"male","group A","some high school","free/reduced","none","68","72","64"
"female","group C","some college","standard","completed","88","95","94"
"male","group D","some college","standard","none","76","64","66"
"male","group C","associate's degree","standard","none","46","43","42"
"female","group B","bachelor's degree","standard","none","67","86","83"
"male","group E","some high school","standard","none","92","87","78"
"male","group C","bachelor's degree","standard","completed","83","82","84"
"male","group D","associate's degree","standard","none","80","75","77"
"male","group D","bachelor's degree","free/reduced","none","63","66","67"
"female","group D","some high school","standard","completed","64","60","74"
"male","group B","some college","standard","none","54","52","51"
"male","group C","associate's degree","standard","none","84","80","80"
"male","group D","high school","free/reduced","completed","73","68","66"
"female","group E","bachelor's degree","standard","none","80","83","83"
"female","group D","high school","standard","none","56","52","55"
"male","group E","some college","standard","none","59","51","43"
"male","group D","some high school","standard","none","75","74","69"
"male","group C","associate's degree","standard","none","85","76","71"
"male","group E","associate's degree","standard","none","89","76","74"
"female","group B","high school","standard","completed","58","70","68"
"female","group B","high school","standard","none","65","64","62"
"male","group C","high school","standard","none","68","60","53"
"male","group A","some high school","standard","completed","47","49","49"
"female","group D","some college","free/reduced","none","71","83","83"
"female","group B","some high school","standard","completed","60","70","70"
"male","group D","master's degree","standard","none","80","80","72"
"male","group D","high school","standard","none","54","52","52"
"female","group E","some college","standard","none","62","73","70"
"female","group C","associate's degree","free/reduced","none","64","73","68"
"male","group C","associate's degree","standard","completed","78","77","77"
"female","group B","some college","standard","none","70","75","78"
"female","group C","master's degree","free/reduced","completed","65","81","81"
"female","group C","some high school","free/reduced","completed","64","79","77"
"male","group C","some college","standard","completed","79","79","78"
"female","group C","some high school","free/reduced","none","44","50","51"
"female","group E","high school","standard","none","99","93","90"
"male","group D","high school","standard","none","76","73","68"
"male","group D","some high school","free/reduced","none","59","42","41"
"female","group C","bachelor's degree","standard","none","63","75","81"
"female","group D","high school","standard","none","69","72","77"
"female","group D","associate's degree","standard","completed","88","92","95"
"female","group E","some college","free/reduced","none","71","76","70"
"male","group C","bachelor's degree","standard","none","69","63","61"
"male","group C","some college","standard","none","58","49","42"
"female","group D","associate's degree","free/reduced","none","47","53","58"
"female","group D","some college","standard","none","65","70","71"
"male","group B","some college","standard","completed","88","85","76"
"male","group C","bachelor's degree","standard","none","83","78","73"
"female","group C","some high school","standard","completed","85","92","93"
"female","group E","high school","standard","completed","59","63","75"
"female","group C","some high school","free/reduced","none","65","86","80"
"male","group B","bachelor's degree","free/reduced","none","73","56","57"
"male","group D","high school","standard","none","53","52","42"
"male","group D","high school","standard","none","45","48","46"
"female","group D","bachelor's degree","free/reduced","none","73","79","84"
"female","group D","some college","free/reduced","completed","70","78","78"
"female","group B","some high school","standard","none","37","46","46"
"male","group B","associate's degree","standard","completed","81","82","82"
"male","group E","associate's degree","standard","completed","97","82","88"
"female","group B","some high school","standard","none","67","89","82"
"male","group B","bachelor's degree","free/reduced","none","88","75","76"
"male","group E","some high school","standard","completed","77","76","77"
"male","group C","associate's degree","standard","none","76","70","68"
"male","group D","some high school","standard","none","86","73","70"
"male","group C","some high school","standard","completed","63","60","57"
"female","group E","bachelor's degree","standard","none","65","73","75"
"male","group D","high school","free/reduced","completed","78","77","80"
"male","group B","associate's degree","free/reduced","none","67","62","60"
"male","group A","some high school","standard","completed","46","41","43"
"male","group E","associate's degree","standard","completed","71","74","68"
"male","group C","high school","free/reduced","completed","40","46","50"
"male","group D","associate's degree","free/reduced","none","90","87","75"
"male","group A","some college","free/reduced","completed","81","78","81"
"male","group D","some high school","free/reduced","none","56","54","52"
"female","group C","associate's degree","standard","completed","67","84","81"
"male","group B","associate's degree","standard","none","80","76","64"
"female","group C","associate's degree","standard","completed","74","75","83"
"male","group A","some college","standard","none","69","67","69"
"male","group E","some college","standard","completed","99","87","81"
"male","group C","some high school","standard","none","51","52","44"
"female","group B","associate's degree","free/reduced","none","53","71","67"
"female","group D","high school","free/reduced","none","49","57","52"
"female","group B","associate's degree","standard","none","73","76","80"
"male","group B","bachelor's degree","standard","none","66","60","57"
"male","group D","bachelor's degree","standard","completed","67","61","68"
"female","group C","associate's degree","free/reduced","completed","68","67","69"
"female","group C","bachelor's degree","standard","completed","59","64","75"
"male","group C","high school","standard","none","71","66","65"
"female","group D","master's degree","standard","completed","77","82","91"
"male","group C","associate's degree","standard","none","83","72","78"
"male","group B","bachelor's degree","standard","none","63","71","69"
"female","group D","associate's degree","free/reduced","none","56","65","63"
"female","group C","high school","free/reduced","completed","67","79","84"
"female","group E","high school","standard","none","75","86","79"
"female","group C","some college","standard","none","71","81","80"
"female","group C","some high school","free/reduced","none","43","53","53"
"female","group C","high school","free/reduced","none","41","46","43"
"female","group C","some college","standard","none","82","90","94"
"male","group C","some college","standard","none","61","61","62"
"male","group A","some college","free/reduced","none","28","23","19"
"male","group C","associate's degree","standard","completed","82","75","77"
"female","group B","some high school","standard","none","41","55","51"
"male","group C","high school","standard","none","71","60","61"
"male","group C","associate's degree","standard","none","47","37","35"
"male","group E","associate's degree","standard","completed","62","56","53"
"male","group B","associate's degree","standard","none","90","78","81"
"female","group C","bachelor's degree","standard","none","83","93","95"
"female","group B","some college","free/reduced","none","61","68","66"
"male","group D","some high school","standard","completed","76","70","69"
"male","group C","associate's degree","standard","none","49","51","43"
"female","group B","some high school","free/reduced","none","24","38","27"
"female","group D","some high school","free/reduced","completed","35","55","60"
"male","group C","high school","free/reduced","none","58","61","52"
"female","group C","high school","standard","none","61","73","63"
"female","group B","high school","standard","completed","69","76","74"
"male","group D","associate's degree","standard","completed","67","72","67"
"male","group D","some college","standard","none","79","73","67"
"female","group C","high school","standard","none","72","80","75"
"male","group B","some college","standard","none","62","61","57"
"female","group C","bachelor's degree","standard","completed","77","94","95"
"male","group D","high school","free/reduced","none","75","74","66"
"male","group E","associate's degree","standard","none","87","74","76"
"female","group B","bachelor's degree","standard","none","52","65","69"
"male","group E","some college","standard","none","66","57","52"
"female","group C","some college","standard","completed","63","78","80"
"female","group C","associate's degree","standard","none","46","58","57"
"female","group C","some college","standard","none","59","71","70"
"female","group B","bachelor's degree","standard","none","61","72","70"
"male","group A","associate's degree","standard","none","63","61","61"
"female","group C","some college","free/reduced","completed","42","66","69"
"male","group D","some college","free/reduced","none","59","62","61"
"female","group D","some college","standard","none","80","90","89"
"female","group B","high school","standard","none","58","62","59"
"male","group B","some high school","standard","completed","85","84","78"
"female","group C","some college","standard","none","52","58","58"
"female","group D","some high school","free/reduced","none","27","34","32"
"male","group C","some college","standard","none","59","60","58"
"male","group A","bachelor's degree","free/reduced","completed","49","58","60"
"male","group C","high school","standard","completed","69","58","53"
"male","group C","bachelor's degree","free/reduced","none","61","66","61"
"female","group A","some high school","free/reduced","none","44","64","58"
"female","group D","some high school","standard","none","73","84","85"
"male","group E","some college","standard","none","84","77","71"
"female","group C","some college","free/reduced","completed","45","73","70"
"male","group D","some high school","standard","none","74","74","72"
"female","group D","some college","standard","completed","82","97","96"
"female","group D","bachelor's degree","standard","none","59","70","73"
"male","group E","associate's degree","free/reduced","none","46","43","41"
"female","group D","some high school","standard","none","80","90","82"
"female","group D","master's degree","free/reduced","completed","85","95","100"
"female","group A","some high school","standard","none","71","83","77"
"male","group A","bachelor's degree","standard","none","66","64","62"
"female","group B","associate's degree","standard","none","80","86","83"
"male","group C","associate's degree","standard","completed","87","100","95"
"male","group C","master's degree","free/reduced","none","79","81","71"
"female","group E","some high school","free/reduced","none","38","49","45"
"female","group A","some high school","free/reduced","none","38","43","43"
"female","group E","some college","standard","none","67","76","75"
"female","group E","bachelor's degree","standard","none","64","73","70"
"female","group C","associate's degree","free/reduced","none","57","78","67"
"female","group D","high school","standard","none","62","64","64"
"male","group D","master's degree","standard","none","73","70","75"
"male","group E","some high school","free/reduced","completed","73","67","59"
"female","group D","some college","standard","none","77","68","77"
"male","group E","some college","standard","none","76","67","67"
"male","group C","associate's degree","standard","completed","57","54","56"
"female","group C","some high school","standard","completed","65","74","77"
"male","group A","high school","free/reduced","none","48","45","41"
"female","group B","high school","free/reduced","none","50","67","63"
"female","group C","associate's degree","standard","none","85","89","95"
"male","group B","some high school","standard","none","74","63","57"
"male","group D","some high school","standard","none","60","59","54"
"female","group C","some high school","standard","completed","59","54","67"
"male","group A","some college","standard","none","53","43","43"
"female","group A","some college","free/reduced","none","49","65","55"
"female","group D","high school","standard","completed","88","99","100"
"female","group C","high school","standard","none","54","59","62"
"female","group C","some high school","standard","none","63","73","68"
"male","group B","associate's degree","standard","completed","65","65","63"
"female","group B","associate's degree","standard","none","82","80","77"
"female","group D","high school","free/reduced","completed","52","57","56"
"male","group D","associate's degree","standard","completed","87","84","85"
"female","group D","master's degree","standard","completed","70","71","74"
"male","group E","some college","standard","completed","84","83","78"
"male","group D","associate's degree","standard","none","71","66","60"
"male","group B","some high school","standard","completed","63","67","67"
"female","group C","bachelor's degree","free/reduced","completed","51","72","79"
"male","group E","high school","standard","none","84","73","69"
"male","group C","bachelor's degree","standard","completed","71","74","68"
"male","group C","associate's degree","standard","none","74","73","67"
"male","group D","some college","standard","none","68","59","62"
"male","group E","high school","free/reduced","completed","57","56","54"
"female","group C","associate's degree","free/reduced","completed","82","93","93"
"female","group D","high school","standard","completed","57","58","64"
"female","group D","master's degree","free/reduced","completed","47","58","67"
"female","group A","some high school","standard","completed","59","85","80"
"male","group B","some college","free/reduced","none","41","39","34"
"female","group C","some college","free/reduced","none","62","67","62"
"male","group C","bachelor's degree","standard","none","86","83","86"
"male","group C","some high school","free/reduced","none","69","71","65"
"male","group A","some high school","free/reduced","none","65","59","53"
"male","group C","some high school","free/reduced","none","68","63","54"
"male","group C","associate's degree","free/reduced","none","64","66","59"
"female","group C","high school","standard","none","61","72","70"
"male","group C","high school","standard","none","61","56","55"
"female","group A","some high school","free/reduced","none","47","59","50"
"male","group C","some high school","standard","none","73","66","66"
"male","group C","some college","free/reduced","completed","50","48","53"
"male","group D","associate's degree","standard","none","75","68","64"
"male","group D","associate's degree","free/reduced","none","75","66","73"
"male","group C","high school","standard","none","70","56","51"
"male","group D","some high school","standard","completed","89","88","82"
"female","group C","some college","standard","completed","67","81","79"
"female","group D","high school","standard","none","78","81","80"
"female","group A","some high school","free/reduced","none","59","73","69"
"female","group B","associate's degree","standard","none","73","83","76"
"male","group A","some high school","free/reduced","none","79","82","73"
"female","group C","some high school","standard","completed","67","74","77"
"male","group D","some college","free/reduced","none","69","66","60"
"male","group C","high school","standard","completed","86","81","80"
"male","group B","high school","standard","none","47","46","42"
"male","group B","associate's degree","standard","none","81","73","72"
"female","group C","some college","free/reduced","completed","64","85","85"
"female","group E","some college","standard","none","100","92","97"
"female","group C","associate's degree","free/reduced","none","65","77","74"
"male","group C","some college","free/reduced","none","65","58","49"
"female","group C","associate's degree","free/reduced","none","53","61","62"
"male","group C","bachelor's degree","free/reduced","none","37","56","47"
"female","group D","bachelor's degree","standard","none","79","89","89"
"male","group D","associate's degree","free/reduced","none","53","54","48"
"female","group E","bachelor's degree","standard","none","100","100","100"
"male","group B","high school","standard","completed","72","65","68"
"male","group C","bachelor's degree","free/reduced","none","53","58","55"
"male","group B","some college","free/reduced","none","54","54","45"
"female","group E","some college","standard","none","71","70","76"
"female","group C","some college","free/reduced","none","77","90","91"
"male","group A","bachelor's degree","standard","completed","75","58","62"
"female","group C","some college","standard","none","84","87","91"
"female","group D","associate's degree","free/reduced","none","26","31","38"
"male","group A","high school","free/reduced","completed","72","67","65"
"female","group A","high school","free/reduced","completed","77","88","85"
"male","group C","some college","standard","none","91","74","76"
"female","group C","associate's degree","standard","completed","83","85","90"
"female","group C","high school","standard","none","63","69","74"
"female","group C","associate's degree","standard","completed","68","86","84"
"female","group D","some high school","standard","none","59","67","61"
"female","group B","associate's degree","standard","completed","90","90","91"
"female","group D","bachelor's degree","standard","completed","71","76","83"
"male","group E","bachelor's degree","standard","completed","76","62","66"
"male","group D","associate's degree","standard","none","80","68","72"
"female","group D","master's degree","standard","none","55","64","70"
"male","group E","associate's degree","standard","none","76","71","67"
"male","group B","high school","standard","completed","73","71","68"
"female","group D","associate's degree","free/reduced","none","52","59","56"
"male","group C","some college","free/reduced","none","68","68","61"
"male","group A","high school","standard","none","59","52","46"
"female","group B","associate's degree","standard","none","49","52","54"
"male","group C","high school","standard","none","70","74","71"
"male","group D","some college","free/reduced","none","61","47","56"
"female","group C","associate's degree","free/reduced","none","60","75","74"
"male","group B","some high school","standard","completed","64","53","57"
"male","group A","associate's degree","free/reduced","completed","79","82","82"
"female","group A","associate's degree","free/reduced","none","65","85","76"
"female","group C","associate's degree","standard","none","64","64","70"
"female","group C","some college","standard","none","83","83","90"
"female","group C","bachelor's degree","standard","none","81","88","90"
"female","group B","high school","standard","none","54","64","68"
"male","group D","high school","standard","completed","68","64","66"
"female","group C","some college","standard","none","54","48","52"
"female","group D","some college","free/reduced","completed","59","78","76"
"female","group B","some high school","standard","none","66","69","68"
"male","group E","some college","standard","none","76","71","72"
"female","group D","master's degree","standard","none","74","79","82"
"female","group B","associate's degree","standard","completed","94","87","92"
"male","group C","some college","free/reduced","none","63","61","54"
"female","group E","associate's degree","standard","completed","95","89","92"
"female","group D","master's degree","free/reduced","none","40","59","54"
"female","group B","some high school","standard","none","82","82","80"
"male","group A","high school","standard","none","68","70","66"
"male","group B","bachelor's degree","free/reduced","none","55","59","54"
"male","group C","master's degree","standard","none","79","78","77"
"female","group C","bachelor's degree","standard","none","86","92","87"
"male","group D","some college","standard","none","76","71","73"
"male","group A","some high school","standard","none","64","50","43"
"male","group D","some high school","free/reduced","none","62","49","52"
"female","group B","some high school","standard","completed","54","61","62"
"female","group B","master's degree","free/reduced","completed","77","97","94"
"female","group C","some high school","standard","completed","76","87","85"
"female","group D","some college","standard","none","74","89","84"
"female","group E","some college","standard","completed","66","74","73"
"female","group D","some high school","standard","completed","66","78","78"
"female","group B","high school","free/reduced","completed","67","78","79"
"male","group D","some college","standard","none","71","49","52"
"female","group C","associate's degree","standard","none","91","86","84"
"male","group D","bachelor's degree","standard","none","69","58","57"
"male","group C","master's degree","free/reduced","none","54","59","50"
"male","group C","high school","standard","completed","53","52","49"
"male","group E","some college","standard","none","68","60","59"
"male","group C","some high school","free/reduced","completed","56","61","60"
"female","group C","high school","free/reduced","none","36","53","43"
"female","group D","bachelor's degree","free/reduced","none","29","41","47"
"female","group C","associate's degree","standard","none","62","74","70"
"female","group C","associate's degree","standard","completed","68","67","73"
"female","group C","some high school","standard","none","47","54","53"
"male","group E","associate's degree","standard","completed","62","61","58"
"female","group E","associate's degree","standard","completed","79","88","94"
"male","group B","high school","standard","completed","73","69","68"
"female","group C","bachelor's degree","free/reduced","completed","66","83","83"
"male","group C","associate's degree","standard","completed","51","60","58"
"female","group D","high school","standard","none","51","66","62"
"male","group E","bachelor's degree","standard","completed","85","66","71"
"male","group A","associate's degree","standard","completed","97","92","86"
"male","group C","high school","standard","completed","75","69","68"
"male","group D","associate's degree","free/reduced","completed","79","82","80"
"female","group C","associate's degree","standard","none","81","77","79"
"female","group D","associate's degree","standard","none","82","95","89"
"female","group D","master's degree","standard","none","64","63","66"
"male","group E","some high school","free/reduced","completed","78","83","80"
"female","group A","some high school","standard","completed","92","100","97"
"male","group C","high school","standard","completed","72","67","64"
"female","group C","high school","free/reduced","none","62","67","64"
"male","group C","master's degree","standard","none","79","72","69"
"male","group C","some high school","free/reduced","none","79","76","65"
"male","group B","bachelor's degree","free/reduced","completed","87","90","88"
"female","group B","associate's degree","standard","none","40","48","50"
"male","group D","some college","free/reduced","none","77","62","64"
"male","group E","associate's degree","standard","none","53","45","40"
"female","group C","some college","free/reduced","none","32","39","33"
"female","group C","associate's degree","standard","completed","55","72","79"
"male","group C","master's degree","free/reduced","none","61","67","66"
"female","group B","associate's degree","free/reduced","none","53","70","70"
"male","group D","some high school","standard","none","73","66","62"
"female","group D","some college","standard","completed","74","75","79"
"female","group C","some college","standard","none","63","74","74"
"male","group C","bachelor's degree","standard","completed","96","90","92"
"female","group D","some college","free/reduced","completed","63","80","80"
"male","group B","bachelor's degree","free/reduced","none","48","51","46"
"male","group B","associate's degree","standard","none","48","43","45"
"female","group E","bachelor's degree","free/reduced","completed","92","100","100"
"female","group D","master's degree","free/reduced","completed","61","71","78"
"male","group B","high school","free/reduced","none","63","48","47"
"male","group D","bachelor's degree","free/reduced","none","68","68","67"
"male","group B","some college","standard","completed","71","75","70"
"male","group A","bachelor's degree","standard","none","91","96","92"
"female","group C","some college","standard","none","53","62","56"
"female","group C","high school","free/reduced","completed","50","66","64"
"female","group E","high school","standard","none","74","81","71"
"male","group A","associate's degree","free/reduced","completed","40","55","53"
"male","group A","some college","standard","completed","61","51","52"
"female","group B","high school","standard","none","81","91","89"
"female","group B","some college","free/reduced","completed","48","56","58"
"female","group D","master's degree","standard","none","53","61","68"
"female","group D","some high school","standard","none","81","97","96"
"female","group E","some high school","standard","none","77","79","80"
"female","group D","bachelor's degree","free/reduced","none","63","73","78"
"female","group D","associate's degree","standard","completed","73","75","80"
"female","group D","some college","standard","none","69","77","77"
"female","group C","associate's degree","standard","none","65","76","76"
"female","group A","high school","standard","none","55","73","73"
"female","group C","bachelor's degree","free/reduced","none","44","63","62"
"female","group C","some college","standard","none","54","64","65"
"female","group A","some high school","standard","none","48","66","65"
"male","group C","some college","free/reduced","none","58","57","54"
"male","group A","some high school","standard","none","71","62","50"
"male","group E","bachelor's degree","standard","none","68","68","64"
"female","group E","high school","standard","none","74","76","73"
"female","group C","bachelor's degree","standard","completed","92","100","99"
"female","group C","bachelor's degree","standard","completed","56","79","72"
"male","group B","high school","free/reduced","none","30","24","15"
"male","group A","some high school","standard","none","53","54","48"
"female","group D","high school","standard","none","69","77","73"
"female","group D","some high school","standard","none","65","82","81"
"female","group D","master's degree","standard","none","54","60","63"
"female","group C","high school","standard","none","29","29","30"
"female","group E","some college","standard","none","76","78","80"
"male","group D","high school","free/reduced","none","60","57","51"
"male","group D","master's degree","free/reduced","completed","84","89","90"
"male","group C","some high school","standard","none","75","72","62"
"female","group C","associate's degree","standard","none","85","84","82"
"female","group C","master's degree","free/reduced","none","40","58","54"
"female","group E","some college","standard","none","61","64","62"
"female","group B","associate's degree","standard","none","58","63","65"
"male","group D","some college","free/reduced","completed","69","60","63"
"female","group C","some college","standard","none","58","59","66"
"male","group C","bachelor's degree","standard","completed","94","90","91"
"female","group C","associate's degree","standard","none","65","77","74"
"female","group A","associate's degree","standard","none","82","93","93"
"female","group C","high school","standard","none","60","68","72"
"female","group E","bachelor's degree","standard","none","37","45","38"
"male","group D","bachelor's degree","standard","none","88","78","83"
"male","group D","master's degree","standard","none","95","81","84"
"male","group C","associate's degree","free/reduced","completed","65","73","68"
"female","group C","high school","free/reduced","none","35","61","54"
"male","group B","bachelor's degree","free/reduced","none","62","63","56"
"male","group C","high school","free/reduced","completed","58","51","52"
"male","group A","some college","standard","completed","100","96","86"
"female","group E","bachelor's degree","free/reduced","none","61","58","62"
"male","group D","some college","standard","completed","100","97","99"
"male","group B","associate's degree","free/reduced","completed","69","70","63"
"male","group D","associate's degree","standard","none","61","48","46"
"male","group D","some college","free/reduced","none","49","57","46"
"female","group C","some high school","standard","completed","44","51","55"
"male","group D","some college","standard","none","67","64","70"
"male","group B","high school","standard","none","79","60","65"
"female","group B","bachelor's degree","standard","completed","66","74","81"
"female","group C","high school","standard","none","75","88","85"
"male","group D","some high school","standard","none","84","84","80"
"male","group A","high school","standard","none","71","74","64"
"female","group B","high school","free/reduced","completed","67","80","81"
"female","group D","some high school","standard","completed","80","92","88"
"male","group E","some college","standard","none","86","76","74"
"female","group D","associate's degree","standard","none","76","74","73"
"male","group D","high school","standard","none","41","52","51"
"female","group D","associate's degree","free/reduced","completed","74","88","90"
"female","group B","some high school","free/reduced","none","72","81","79"
"female","group E","high school","standard","completed","74","79","80"
"male","group B","high school","standard","none","70","65","60"
"female","group B","bachelor's degree","standard","completed","65","81","81"
"female","group D","associate's degree","standard","none","59","70","65"
"female","group E","high school","free/reduced","none","64","62","68"
"female","group B","high school","standard","none","50","53","55"
"female","group D","some college","standard","completed","69","79","81"
"male","group C","some high school","free/reduced","completed","51","56","53"
"female","group A","high school","standard","completed","68","80","76"
"female","group D","some college","standard","completed","85","86","98"
"female","group A","associate's degree","standard","completed","65","70","74"
"female","group B","some high school","standard","none","73","79","79"
"female","group B","some college","standard","none","62","67","67"
"male","group C","associate's degree","free/reduced","none","77","67","64"
"male","group D","some high school","standard","none","69","66","61"
"female","group D","associate's degree","free/reduced","none","43","60","58"
"male","group D","associate's degree","standard","none","90","87","85"
"male","group C","some college","free/reduced","none","74","77","73"
"male","group C","some high school","standard","none","73","66","63"
"female","group D","some college","free/reduced","none","55","71","69"
"female","group C","high school","standard","none","65","69","67"
"male","group D","associate's degree","standard","none","80","63","63"
"female","group C","some high school","free/reduced","completed","50","60","60"
"female","group C","some college","free/reduced","completed","63","73","71"
"female","group B","bachelor's degree","free/reduced","none","77","85","87"
"male","group C","some college","standard","none","73","74","61"
"male","group D","associate's degree","standard","completed","81","72","77"
"female","group C","high school","free/reduced","none","66","76","68"
"male","group D","associate's degree","free/reduced","none","52","57","50"
"female","group C","some college","standard","none","69","78","76"
"female","group C","associate's degree","standard","completed","65","84","84"
"female","group D","high school","standard","completed","69","77","78"
"female","group B","some college","standard","completed","50","64","66"
"female","group E","some college","standard","completed","73","78","76"
"female","group C","some high school","standard","completed","70","82","76"
"male","group D","associate's degree","free/reduced","none","81","75","78"
"male","group D","some college","free/reduced","none","63","61","60"
"female","group D","high school","standard","none","67","72","74"
"male","group B","high school","standard","none","60","68","60"
"male","group B","high school","standard","none","62","55","54"
"female","group C","some high school","free/reduced","completed","29","40","44"
"male","group B","some college","standard","completed","62","66","68"
"female","group E","master's degree","standard","completed","94","99","100"
"male","group E","some college","standard","completed","85","75","68"
"male","group D","associate's degree","free/reduced","none","77","78","73"
"male","group A","high school","free/reduced","none","53","58","44"
"male","group E","some college","free/reduced","none","93","90","83"
"female","group C","associate's degree","standard","none","49","53","53"
"female","group E","associate's degree","free/reduced","none","73","76","78"
"female","group C","bachelor's degree","free/reduced","completed","66","74","81"
"female","group D","associate's degree","standard","none","77","77","73"
"female","group C","some high school","standard","none","49","63","56"
"female","group D","some college","free/reduced","none","79","89","86"
"female","group C","associate's degree","standard","completed","75","82","90"
"female","group A","bachelor's degree","standard","none","59","72","70"
"female","group D","associate's degree","standard","completed","57","78","79"
"male","group C","high school","free/reduced","none","66","66","59"
"female","group E","bachelor's degree","standard","completed","79","81","82"
"female","group B","some high school","standard","none","57","67","72"
"male","group A","bachelor's degree","standard","completed","87","84","87"
"female","group D","some college","standard","none","63","64","67"
"female","group B","some high school","free/reduced","completed","59","63","64"
"male","group A","bachelor's degree","free/reduced","none","62","72","65"
"male","group D","high school","standard","none","46","34","36"
"male","group C","some college","standard","none","66","59","52"
"male","group D","high school","standard","none","89","87","79"
"female","group D","associate's degree","free/reduced","completed","42","61","58"
"male","group C","some college","standard","completed","93","84","90"
"female","group E","some high school","standard","completed","80","85","85"
"female","group D","some college","standard","none","98","100","99"
"male","group D","master's degree","standard","none","81","81","84"
"female","group B","some high school","standard","completed","60","70","74"
"female","group B","associate's degree","free/reduced","completed","76","94","87"
"male","group C","associate's degree","standard","completed","73","78","72"
"female","group C","associate's degree","standard","completed","96","96","99"
"female","group C","high school","standard","none","76","76","74"
"male","group E","associate's degree","free/reduced","completed","91","73","80"
"female","group C","some college","free/reduced","none","62","72","70"
"male","group D","some high school","free/reduced","completed","55","59","59"
"female","group B","some high school","free/reduced","completed","74","90","88"
"male","group C","high school","standard","none","50","48","42"
"male","group B","some college","standard","none","47","43","41"
"male","group E","some college","standard","completed","81","74","71"
"female","group E","associate's degree","standard","completed","65","75","77"
"male","group E","some high school","standard","completed","68","51","57"
"female","group D","high school","free/reduced","none","73","92","84"
"male","group C","some college","standard","none","53","39","37"
"female","group B","associate's degree","free/reduced","completed","68","77","80"
"male","group A","some high school","free/reduced","none","55","46","43"
"female","group C","some college","standard","completed","87","89","94"
"male","group D","some high school","standard","none","55","47","44"
"female","group E","some college","free/reduced","none","53","58","57"
"male","group C","master's degree","standard","none","67","57","59"
"male","group C","associate's degree","standard","none","92","79","84"
"female","group B","some college","free/reduced","completed","53","66","73"
"male","group D","associate's degree","standard","none","81","71","73"
"male","group C","high school","free/reduced","none","61","60","55"
"male","group D","bachelor's degree","standard","none","80","73","72"
"female","group A","associate's degree","free/reduced","none","37","57","56"
"female","group C","high school","standard","none","81","84","82"
"female","group C","associate's degree","standard","completed","59","73","72"
"male","group B","some college","free/reduced","none","55","55","47"
"male","group D","associate's degree","standard","none","72","79","74"
"male","group D","high school","standard","none","69","75","71"
"male","group C","some college","standard","none","69","64","68"
"female","group C","bachelor's degree","free/reduced","none","50","60","59"
"male","group B","some college","standard","completed","87","84","86"
"male","group D","some high school","standard","completed","71","69","68"
"male","group E","some college","standard","none","68","72","65"
"male","group C","master's degree","free/reduced","completed","79","77","75"
"female","group C","some high school","standard","completed","77","90","85"
"male","group C","associate's degree","free/reduced","none","58","55","53"
"female","group E","associate's degree","standard","none","84","95","92"
"male","group D","some college","standard","none","55","58","52"
"male","group E","bachelor's degree","free/reduced","completed","70","68","72"
"female","group D","some college","free/reduced","completed","52","59","65"
"male","group B","some college","standard","completed","69","77","77"
"female","group C","high school","free/reduced","none","53","72","64"
"female","group D","some high school","standard","none","48","58","54"
"male","group D","some high school","standard","completed","78","81","86"
"female","group B","high school","standard","none","62","62","63"
"male","group D","some college","standard","none","60","63","59"
"female","group B","high school","standard","none","74","72","72"
"female","group C","high school","standard","completed","58","75","77"
"male","group B","high school","standard","completed","76","62","60"
"female","group D","some high school","standard","none","68","71","75"
"male","group A","some college","free/reduced","none","58","60","57"
"male","group B","high school","standard","none","52","48","49"
"male","group D","bachelor's degree","standard","none","75","73","74"
"female","group B","some high school","free/reduced","completed","52","67","72"
"female","group C","bachelor's degree","free/reduced","none","62","78","79"
"male","group B","some college","standard","none","66","65","60"
"female","group B","some high school","free/reduced","none","49","58","55"
"female","group B","high school","standard","none","66","72","70"
"female","group C","some college","free/reduced","none","35","44","43"
"female","group A","some college","standard","completed","72","79","82"
"male","group E","associate's degree","standard","completed","94","85","82"
"female","group D","associate's degree","free/reduced","none","46","56","57"
"female","group B","master's degree","standard","none","77","90","84"
"female","group B","high school","free/reduced","completed","76","85","82"
"female","group C","associate's degree","standard","completed","52","59","62"
"male","group C","bachelor's degree","standard","completed","91","81","79"
"female","group B","some high school","standard","completed","32","51","44"
"female","group E","some high school","free/reduced","none","72","79","77"
"female","group B","some college","standard","none","19","38","32"
"male","group C","associate's degree","free/reduced","none","68","65","61"
"female","group C","master's degree","free/reduced","none","52","65","61"
"female","group B","high school","standard","none","48","62","60"
"female","group D","some college","free/reduced","none","60","66","70"
"male","group D","high school","free/reduced","none","66","74","69"
"male","group E","some high school","standard","completed","89","84","77"
"female","group B","high school","standard","none","42","52","51"
"female","group E","associate's degree","free/reduced","completed","57","68","73"
"male","group D","high school","standard","none","70","70","70"
"female","group E","associate's degree","free/reduced","none","70","84","81"
"male","group E","some college","standard","none","69","60","54"
"female","group C","associate's degree","standard","none","52","55","57"
"male","group C","some high school","standard","completed","67","73","68"
"male","group C","some high school","standard","completed","76","80","73"
"female","group E","associate's degree","standard","none","87","94","95"
"female","group B","some college","standard","none","82","85","87"
"female","group C","some college","standard","none","73","76","78"
"male","group A","some college","free/reduced","none","75","81","74"
"female","group D","some college","free/reduced","none","64","74","75"
"female","group E","high school","free/reduced","none","41","45","40"
"male","group C","high school","standard","none","90","75","69"
"male","group B","bachelor's degree","standard","none","59","54","51"
"male","group A","some high school","standard","none","51","31","36"
"male","group A","high school","free/reduced","none","45","47","49"
"female","group C","master's degree","standard","completed","54","64","67"
"male","group E","some high school","standard","completed","87","84","76"
"female","group C","high school","standard","none","72","80","83"
"male","group B","some high school","standard","completed","94","86","87"
"female","group A","bachelor's degree","standard","none","45","59","64"
"male","group D","bachelor's degree","free/reduced","completed","61","70","76"
"female","group B","high school","free/reduced","none","60","72","68"
"female","group C","some high school","standard","none","77","91","88"
"female","group A","some high school","standard","completed","85","90","92"
"female","group D","bachelor's degree","free/reduced","none","78","90","93"
"male","group E","some college","free/reduced","completed","49","52","51"
"female","group B","high school","free/reduced","none","71","87","82"
"female","group C","some high school","free/reduced","none","48","58","52"
"male","group C","high school","standard","none","62","67","58"
"female","group C","associate's degree","free/reduced","completed","56","68","70"
"female","group C","some high school","standard","none","65","69","76"
"female","group D","some high school","free/reduced","completed","69","86","81"
"male","group B","some high school","standard","none","68","54","53"
"female","group A","some college","free/reduced","none","61","60","57"
"female","group C","bachelor's degree","free/reduced","completed","74","86","89"
"male","group A","bachelor's degree","standard","none","64","60","58"
"female","group B","high school","standard","completed","77","82","89"
"male","group B","some college","standard","none","58","50","45"
"female","group C","high school","standard","completed","60","64","74"
"male","group E","high school","standard","none","73","64","57"
"female","group A","high school","standard","completed","75","82","79"
"male","group B","associate's degree","free/reduced","completed","58","57","53"
"female","group C","associate's degree","standard","none","66","77","73"
"female","group D","high school","free/reduced","none","39","52","46"
"male","group C","some high school","standard","none","64","58","51"
"female","group B","high school","free/reduced","completed","23","44","36"
"male","group B","some college","free/reduced","completed","74","77","76"
"female","group D","some high school","free/reduced","completed","40","65","64"
"male","group E","master's degree","standard","none","90","85","84"
"male","group C","master's degree","standard","completed","91","85","85"
"male","group D","high school","standard","none","64","54","50"
"female","group C","high school","standard","none","59","72","68"
"male","group D","associate's degree","standard","none","80","75","69"
"male","group C","master's degree","standard","none","71","67","67"
"female","group A","high school","standard","none","61","68","63"
"female","group E","some college","standard","none","87","85","93"
"male","group E","some high school","standard","none","82","67","61"
"male","group C","some high school","standard","none","62","64","55"
"female","group B","bachelor's degree","standard","none","97","97","96"
"male","group B","some college","free/reduced","none","75","68","65"
"female","group C","bachelor's degree","standard","none","65","79","81"
"male","group B","high school","standard","completed","52","49","46"
"male","group C","associate's degree","free/reduced","none","87","73","72"
"female","group C","associate's degree","standard","none","53","62","53"
"female","group E","master's degree","free/reduced","none","81","86","87"
"male","group D","bachelor's degree","free/reduced","completed","39","42","38"
"female","group C","some college","standard","completed","71","71","80"
"male","group C","associate's degree","standard","none","97","93","91"
"male","group D","some college","standard","completed","82","82","88"
"male","group C","high school","free/reduced","none","59","53","52"
"male","group B","associate's degree","standard","none","61","42","41"
"male","group E","associate's degree","free/reduced","completed","78","74","72"
"male","group C","associate's degree","free/reduced","none","49","51","51"
"male","group B","high school","standard","none","59","58","47"
"female","group C","some college","standard","completed","70","72","76"
"male","group B","associate's degree","standard","completed","82","84","78"
"male","group E","associate's degree","free/reduced","none","90","90","82"
"female","group C","bachelor's degree","free/reduced","none","43","62","61"
"male","group C","some college","free/reduced","none","80","64","66"
"male","group D","some college","standard","none","81","82","84"
"male","group C","some high school","standard","none","57","61","54"
"female","group D","some high school","standard","none","59","72","80"
"female","group D","associate's degree","standard","none","64","76","74"
"male","group C","bachelor's degree","standard","completed","63","64","66"
"female","group E","bachelor's degree","standard","completed","71","70","70"
"female","group B","high school","free/reduced","none","64","73","71"
"male","group D","bachelor's degree","free/reduced","none","55","46","44"
"female","group E","associate's degree","standard","none","51","51","54"
"female","group C","associate's degree","standard","completed","62","76","80"
"female","group E","associate's degree","standard","completed","93","100","95"
"male","group C","high school","free/reduced","none","54","72","59"
"female","group D","some college","free/reduced","none","69","65","74"
"male","group D","high school","free/reduced","none","44","51","48"
"female","group E","some college","standard","completed","86","85","91"
"female","group E","associate's degree","standard","none","85","92","85"
"female","group A","master's degree","free/reduced","none","50","67","73"
"male","group D","some high school","standard","completed","88","74","75"
"female","group E","associate's degree","standard","none","59","62","69"
"female","group E","some high school","free/reduced","none","32","34","38"
"male","group B","high school","free/reduced","none","36","29","27"
"female","group B","some high school","free/reduced","completed","63","78","79"
"male","group D","associate's degree","standard","completed","67","54","63"
"female","group D","some high school","standard","completed","65","78","82"
"male","group D","master's degree","standard","none","85","84","89"
"female","group C","master's degree","standard","none","73","78","74"
"female","group A","high school","free/reduced","completed","34","48","41"
"female","group D","bachelor's degree","free/reduced","completed","93","100","100"
"female","group D","some high school","free/reduced","none","67","84","84"
"male","group D","some college","standard","none","88","77","77"
"male","group B","high school","standard","none","57","48","51"
"female","group D","some college","standard","completed","79","84","91"
"female","group C","bachelor's degree","free/reduced","none","67","75","72"
"male","group E","bachelor's degree","standard","completed","70","64","70"
"male","group D","bachelor's degree","free/reduced","none","50","42","48"
"female","group A","some college","standard","none","69","84","82"
"female","group C","bachelor's degree","standard","completed","52","61","66"
"female","group C","bachelor's degree","free/reduced","completed","47","62","66"
"female","group B","associate's degree","free/reduced","none","46","61","55"
"female","group E","some college","standard","none","68","70","66"
"male","group E","bachelor's degree","standard","completed","100","100","100"
"female","group C","high school","standard","none","44","61","52"
"female","group C","associate's degree","standard","completed","57","77","80"
"male","group B","some college","standard","completed","91","96","91"
"male","group D","high school","free/reduced","none","69","70","67"
"female","group C","high school","free/reduced","none","35","53","46"
"male","group D","high school","standard","none","72","66","66"
"female","group B","associate's degree","free/reduced","none","54","65","65"
"male","group D","high school","free/reduced","none","74","70","69"
"male","group E","some high school","standard","completed","74","64","60"
"male","group E","associate's degree","free/reduced","none","64","56","52"
"female","group D","high school","free/reduced","completed","65","61","71"
"male","group E","associate's degree","free/reduced","completed","46","43","44"
"female","group C","some high school","free/reduced","none","48","56","51"
"male","group C","some college","free/reduced","completed","67","74","70"
"male","group D","some college","free/reduced","none","62","57","62"
"male","group D","associate's degree","free/reduced","completed","61","71","73"
"male","group C","bachelor's degree","free/reduced","completed","70","75","74"
"male","group C","associate's degree","standard","completed","98","87","90"
"male","group D","some college","free/reduced","none","70","63","58"
"male","group A","associate's degree","standard","none","67","57","53"
"female","group E","high school","free/reduced","none","57","58","57"
"male","group D","some college","standard","completed","85","81","85"
"male","group D","some high school","standard","completed","77","68","69"
"male","group C","master's degree","free/reduced","completed","72","66","72"
"female","group D","master's degree","standard","none","78","91","96"
"male","group C","high school","standard","none","81","66","64"
"male","group A","some high school","free/reduced","completed","61","62","61"
"female","group B","high school","standard","none","58","68","61"
"female","group C","associate's degree","standard","none","54","61","58"
"male","group B","high school","standard","none","82","82","80"
"female","group D","some college","free/reduced","none","49","58","60"
"male","group B","some high school","free/reduced","completed","49","50","52"
"female","group E","high school","free/reduced","completed","57","75","73"
"male","group E","high school","standard","none","94","73","71"
"female","group D","some college","standard","completed","75","77","83"
"female","group E","some high school","free/reduced","none","74","74","72"
"male","group C","high school","standard","completed","58","52","54"
"female","group C","some college","standard","none","62","69","69"
"male","group E","associate's degree","standard","none","72","57","62"
"male","group C","some college","standard","none","84","87","81"
"female","group D","master's degree","standard","none","92","100","100"
"female","group D","high school","standard","none","45","63","59"
"male","group C","high school","standard","none","75","81","71"
"female","group A","some college","standard","none","56","58","64"
"female","group D","some high school","free/reduced","none","48","54","53"
"female","group E","associate's degree","standard","none","100","100","100"
"female","group C","some high school","free/reduced","completed","65","76","75"
"male","group D","some college","standard","none","72","57","58"
"female","group D","some college","standard","none","62","70","72"
"male","group A","some high school","standard","completed","66","68","64"
"male","group C","some college","standard","none","63","63","60"
"female","group E","associate's degree","standard","none","68","76","67"
"female","group B","bachelor's degree","standard","none","75","84","80"
"female","group D","bachelor's degree","standard","none","89","100","100"
"male","group C","some high school","standard","completed","78","72","69"
"female","group A","high school","free/reduced","completed","53","50","60"
"female","group D","some college","free/reduced","none","49","65","61"
"female","group A","some college","standard","none","54","63","67"
"female","group C","some college","standard","completed","64","82","77"
"male","group B","some college","free/reduced","completed","60","62","60"
"male","group C","associate's degree","standard","none","62","65","58"
"male","group D","high school","standard","completed","55","41","48"
"female","group C","associate's degree","standard","none","91","95","94"
"female","group B","high school","free/reduced","none","8","24","23"
"male","group D","some high school","standard","none","81","78","78"
"male","group B","some high school","standard","completed","79","85","86"
"female","group A","some college","standard","completed","78","87","91"
"female","group C","some high school","standard","none","74","75","82"
"male","group A","high school","standard","none","57","51","54"
"female","group C","associate's degree","standard","none","40","59","51"
"male","group E","some high school","standard","completed","81","75","76"
"female","group A","some high school","free/reduced","none","44","45","45"
"female","group D","some college","free/reduced","completed","67","86","83"
"male","group E","high school","free/reduced","completed","86","81","75"
"female","group B","some high school","standard","completed","65","82","78"
"female","group D","associate's degree","free/reduced","none","55","76","76"
"female","group D","bachelor's degree","free/reduced","none","62","72","74"
"male","group A","high school","standard","none","63","63","62"
"female","group E","master's degree","standard","completed","88","99","95"
"male","group C","high school","free/reduced","none","62","55","55"
"female","group C","high school","free/reduced","completed","59","71","65"
"female","group D","some college","standard","completed","68","78","77"
"female","group D","some college","free/reduced","none","77","86","86"
```

## File: `src/exception.py`
```python
import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    


        
```

## File: `src/logger.py`
```python
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)
```

## File: `src/utils.py`
```python
import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)
```

## File: `src/components/Data_ingestion.py`
```python
import os
import sys
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.exception import CustomException
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('Artifacts',"Train_Data.csv")
    test_data_path: str=os.path.join('Artifacts',"Test_Data.csv")
    raw_data_path: str=os.path.join('Artifacts',"Raw_Data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Started")
        try:
            data=pd.read_csv('Notebook_Experiments\Data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Created the raw data file")

            logging.info("Splitting the data into train and test")
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            logging.info("Data Splitting is done")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Created the train and test data files")
            logging.info("Data ingestion completed")

            return (self.ingestion_config.test_data_path,self.ingestion_config.train_data_path)
                
        except Exception as e:
            logging.info("Excpetion occured while ingesting the data")
            raise CustomException(e,sys)
```

## File: `src/components/Data_transformation.py`
```python
import os
import sys
import numpy as np 
import pandas as pd
from src.logger import logging
from src.utils import save_object
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.exception import CustomException
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('Artifacts',"Preprocessor.pkl")

    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = ["gender","race_ethnicity","parental_level_of_education","lunch","test_preparation_course"]
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())]
                )

            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))]
                )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)]
                )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            logging.info(f'Train Data Before Transformation:\n {train_df.head()}')
            logging.info(f'Test Data Before Transformation:\n {test_df.head()}')

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(f'Input Train Data After Transformation: \n {input_feature_train_df.head()}')
            logging.info(f'Input Test Data After Transformation:\n {input_feature_test_df.head()}')
            logging.info(f'Target Train Data After Transformation: \n{target_feature_train_df.head()}')
            logging.info(f'Target Test Data After Transformation:\n {target_feature_test_df.head()}')

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info(f'Input Train Data After Transformation: \n {input_feature_train_arr.shape}')
            logging.info(f'Input Test Data After Transformation:\n {input_feature_test_arr.shape}')

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
```

## File: `src/components/Model_trainer.py`
```python
import os
import sys
from src.logger import logging
from dataclasses import dataclass
from sklearn.metrics import r2_score
from catboost import CatBoostRegressor
from src.exception import CustomException
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from src.utils import save_object,evaluate_models
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("Artifacts","Model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                } 
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models,param=params)
            
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            logging.info(f'Best Model: {best_model}')
            logging.info(f"R2 score of best model is {r2_square}")
            return r2_square
        
        except Exception as e:
            raise CustomException(e,sys)
```

## File: `src/pipeline/Prediction_pipeline.py`
```python
import os
import sys
import pandas as pd
from src.utils import load_object
from src.exception import CustomException

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("Artifacts","Model.pkl")
            preprocessor_path=os.path.join('Artifacts','Preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

```

## File: `src/pipeline/Training_pipeline.py`
```python
from src.components.Data_ingestion import DataIngestion
from src.components.Data_transformation import DataTransformation
from src.components.Model_trainer import ModelTrainer

obj=DataIngestion()
train_data,test_data=obj.initiate_data_ingestion()

data_transformation=DataTransformation()
train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

modeltrainer=ModelTrainer()
print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
```

## File: `static/styles.css`
```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
}

.container {
    max-width: 500px;
    margin: 50px auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

h1, h2 {
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
}

.mb-3 {
    margin-bottom: 15px;
}

.form-label {
    font-weight: bold;
}

.form-control {
    width: 100%;
    max-width: 400px;
    padding: 10px;
    box-sizing: border-box;
    margin: 5px auto;
    border: 1px solid #ccc;
    border-radius: 4px;
    transition: border-color 0.3s;
}

.form-control:focus {
    outline: none;
    border-color: #007bff;
}

.btn-primary {
    background-color: #007bff;
    color: #fff;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.btn-primary:hover {
    background-color: #0056b3;
}
```

## File: `templates/home.html`
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="static\styles.css">
    <title>Student Performance Prediction</title>
</head>
<body>
    <div class="login">
   
       <form action="{{ url_for('predict_datapoint')}}" method="post">
        <h1>
            <legend>Student Performance Prediction</legend>
        </h1>


        <div class="mb-3">
            <label class="form-label">Gender</label><br>
            <select class="form-control" name="gender" placeholder="Enter you Gender" required>
                <option class="placeholder" selected disabled value="">Select your Gender</option>
                <option value="male">
                    Male
                </option>
                <option value="female">
                    Female
                </option>
            </select>
        </div>


        <div class="mb-3">
            <label class="form-label">Race or Ethnicity</label><br>
            <select class="form-control" name="ethnicity" placeholder="Enter you ethnicity" required>
                <option class="placeholder" selected disabled value="">Select Ethnicity</option>
                <option value="group A">
                    GROUP - A
                </option>
                <option value="group B">
                    GROUP - B
                </option>
                <option value="group C">
                    GROUP - C
                </option>
                <option value="group D">
                    GROUP - D
                </option>
                <option value="group E">
                    GROUP - E
                </option>
            </select>
        </div>


        <div class="mb-3">
            <label class="form-label">Parental Level of Education</label>
            <select class="form-control" name="parental_level_of_education"
                placeholder="Enter you Parent Education" required>
                <option class="placeholder" selected disabled value="">Select Parent Education</option>
                <option value="associate's degree">
                    Associate's Degree
                </option>
                <option value="bachelor's degree">
                    Bachelor's Degree
                </option>
                <option value="high school">
                    High School
                </option>
                <option value="master's degree">
                    Master's Degree
                </option>
                <option value="some college">
                    Some College
                </option>
                <option value="some high school">
                    Some High School
                </option>
            </select>
        </div>


        <div class="mb-3">
            <label class="form-label">Lunch Type</label><br>
            <select class="form-control" name="lunch" placeholder="Enter you Lunch" required>
                <option class="placeholder" selected disabled value="">Select Lunch Type</option>
                <option value="free/reduced">
                    Free / Reduced
                </option>
                <option value="standard">
                    Standard
                </option>
            </select>
        </div>


        <div class="mb-3">
            <label class="form-label">Test preparation Course</label>
            <select class="form-control" name="test_preparation_course" placeholder="Enter you Course"
                required>
                <option class="placeholder" selected disabled value="">Select Test_course</option>
                <option value="none">
                    None
                </option>
                <option value="completed">
                    Completed
                </option>
            </select>
        </div>


        <div class="mb-3">
            <label class="form-label">Writing Score out of 100</label>
            <input class="form-control" type="number" name="reading_score"
                placeholder="Enter your Reading score" min='0' max='100' />
        </div>


        <div class="mb-3">
            <label class="form-label">Reading Score out of 100</label>
            <input class="form-control" type="number" name="writing_score"
                placeholder="Enter your Reading Score" min='0' max='100' />
        </div>

        <div class="mb-3">
            <input class="btn btn-primary" type="submit" value="Predict your Maths Score" required />
        </div>
    </form>
    <h2>
       The Prediction is {{results}}
    </h2>
   <body>
</html>
```

