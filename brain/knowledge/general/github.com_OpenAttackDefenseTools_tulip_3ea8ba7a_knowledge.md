---
id: github.com-openattackdefensetools-tulip-3ea8ba7a-k
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:08.906531
---

# KNOWLEDGE EXTRACT: github.com_OpenAttackDefenseTools_tulip_3ea8ba7a
> **Extracted on:** 2026-04-01 07:42:44
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519183/github.com_OpenAttackDefenseTools_tulip_3ea8ba7a

---

## File: `.dockerignore`
```
/traffic
```

## File: `.env.example`
```
##############################
# Tulip config
##############################

# Timescale connection
TIMESCALE="postgres://tulip@timescale:5432/tulip"

# The location of your pcaps as seen by the host
TRAFFIC_DIR_HOST="./services/test_pcap"

# The location of your pcaps (and eve.json), as seen by the container
TRAFFIC_DIR_DOCKER="/traffic"

# Set BPF filter expression (see https://www.tcpdump.org/manpages/pcap-filter.7.html)
#BPF="port 8080"

# Visualizer
#VISUALIZER_URL="http://scraper.example.com"

##############################
# Game config
##############################

# Start time of the CTF (or network open if you prefer)
TICK_START="2024-11-30T13:00:00Z"

# Tick length in ms
TICK_LENGTH=180000

# The flag format in regex
FLAG_REGEX="[A-Z0-9]{31}="

# VM IP (inside gamenet)
# Currently ignored unless FLAGID_SCRAPE is set
VM_IP="10.10.3.1"
TEAM_ID="3"

##############################
# PCAP_OVER_IP CONFIGS
##############################

# Enable pcap-over-ip and choose server endpoint
# Empty value = disabled
PCAP_OVER_IP=
#PCAP_OVER_IP="host.docker.internal:1337"
# For multiple PCAP_OVER_IP you can comma separate
#PCAP_OVER_IP="host.docker.internal:1337,otherhost.com:5050"

##############################
# DUMP_PCAPS CONFIGS
##############################

# Enable pcap dumping and select target location
# Empty value = disabled
DUMP_PCAPS=
#DUMP_PCAPS="/traffic"

# Dumping options
# Ignored unless DUMP_PCAPS is set
DUMP_PCAPS_INTERVAL="1m"
DUMP_PCAPS_FILENAME="2006-01-02_15-04-05.pcap"

##############################
# FLAGID CONFIGS
##############################

# Enable flagid scrapping
# Empty value = disabled
FLAGID_SCRAPE=
#FLAGID_SCRAPE=1

# Enable flagid scanning - Tags flag ids in traffic
# Empty value = disabled
# Does nothing unless FLAGID_SCRAPE is set
FLAGID_SCAN=
#FLAGID_SCAN=1

# Flag lifetime in ticks
# Empty value = Fallback to TICK_LENGTH
# -1 = No check, pls don't use outside testing
FLAG_LIFETIME=
#FLAG_LIFETIME=-1
#FLAG_LIFETIME=5

# Flagid endpoint
# Default value is a test container in docker-compose-test.yml, change this for production
# Ignored unless FLAGID_SCRAPE is set
FLAGID_ENDPOINT="http://flagidendpoint:8000/flagids.json"

##############################
# FLAG_VALIDATOR CONFIGS
##############################

# Enables flag validation / fake flag feature. Must be one of: faust, enowars, eno, itad
# Empty value = disabled
FLAG_VALIDATOR_TYPE=

# Some flag validators can make use of (our) team number/ID
# Ignored unless FLAG_VALIDATOR_TYPE is set
FLAG_VALIDATOR_TEAM=42

##############################
# SURICATA CONFIGS
##############################

# Directory for Suricata files (see suricata/etc, suricata/lib/rules, suricata/logs)
# (they should be generated on first run)
#SURICATA_DIR_HOST="./suricata"
```

## File: `.gitignore`
```
# See https://help.github.com/ignore-files/ for more about ignoring files.

# dependencies
/node_modules

# testing
/coverage

# production
/build

# misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*


#PYTHON

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
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
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

workspace.xml
.idea

/traffic
suricata
```

## File: `LICENSE`
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
# 🌷 Tulip

Tulip is a flow analyzer meant for use during Attack / Defence CTF competitions. It allows players to easily find some traffic related to their service and automatically generates python snippets to replicate attacks.

## Origins
Tulip was developed by Team Europe for use in the first International Cyber Security Challenge. The project is a fork of [flower](https://github.com/secgroup/flower), but it contains quite some changes:
* New front-end (typescript / react / tailwind)
* New ingestor code, based on gopacket
* IPv6 support
* Vastly improved filter and tagging system.
* Deep links for easy collaboration
* Added an http decoding pass for compressed data
* Synchronized with Suricata.
* Flow diffing
* Time and size-based plots for correlation.
* Linking HTTP sessions together based on cookies (Experimental*, disabled by default)
* PCAP-over-IP with BPF filtering support**

\* - to enable, add `-experimental` after `./assembler` in `docker-compose.yml`

\*\* - to enable, configure PCAP-over-IP server (e.g. [pcap-broker](https://github.com/fox-it/pcap-broker) as suggested in [PR 24](https://github.com/OpenAttackDefenseTools/tulip/pull/24)) and set `PCAP_OVER_IP` (and `BPF` if necessary) in `.env`

## Screenshots
![](./demo_images/demo1.png)
![](./demo_images/demo2.png)
![](./demo_images/demo3.png)

## Configuration
Before starting the stack, edit `services/api/configurations.py`:

```
vm_ip = "10.60.4.1"
services = [{"ip": vm_ip, "port": 18080, "name": "BIOMarkt"},
            {"ip": vm_ip, "port": 5555, "name": "SaaS"},
]
```

You can also edit this during the CTF, just rebuild the `api` service:
```
docker-compose up --build -d api
```

## Usage

The stack can be started with docker-compose, after creating an `.env` file. See `.env.example` as an example of how to configure your environment.
```
cp .env.example .env
# < Edit the .env file with your favourite text editor >
docker-compose up -d --build
```
To ingest traffic, it is recommended to create a shared bind mount with the docker-compose. One convenient way to set this up is as follows:
1. On the vulnbox, start a rotating packet sniffer (e.g. tcpdump, suricata, ...)
```bash
tcpdump -i eth0 -G 180 -w "traffic_%H:%M:%S.pcap" port 8080
```
2. Using rsync, copy complete captures to the machine running tulip (e.g. to /traffic)
```bash
rsync -avz -e ssh --progress root@10.0.0.2:/pcaps ./pcaps
```
3. Add a bind to the assembler service so it can read /traffic
   > (Just change `TRAFFIC_DIR_HOST` in `.env`)

The ingestor will use inotify to watch for new pcap's and suricata logs. No need to set a chron job.


## Suricata synchronization

### Run in Docker

Configure `SURICATA_DIR_HOST` in `.env`.

Create some rules (404 for testing):
```bash
. .env
mkdir -p ${SURICATA_DIR_HOST}/{etc,lib/rules,log}
echo 'alert tcp any any -> any any (msg: "404 Not Found"; http.stat_code; content:"404"; metadata: tag notfound; sid:4; rev: 1;)' >> ${SURICATA_DIR_HOST}/lib/rules/suricata.rules
```

After that run (default config for `eve.json` logging was good enough):

```bash
docker compose -f docker-compose-suricata.yml up -d --build
```

### Metadata
Tags are read from the metadata field of a rule. For example, here's a simple rule to detect a path traversal:
```
alert tcp any any -> any any (msg: "Path Traversal-../"; flow:to_server; content: "../"; metadata: tag path_traversal; sid:1; rev: 1;)
```
Once this rule is seen in traffic, the `path_traversal` tag will automatically be added to the filters in Tulip.

> [!NOTE]
>
> After editing Suricata rules (renaming or id change) please:
>
> Remove old logs: `rm ${SURICATA_DIR_HOST}/log/*` (otherwise old signatures will be repopulated).
>
> Restart Docker containers.
>
> If database was only restarted (not dropped), try cleaning tags/signatures manually.

### eve.json
Suricata alerts are read directly from the `eve.json` file. Because this file can get quite verbose when all extensions are enabled, it is recommended to strip the config down a fair bit. For example:
```yaml
# ...
  - eve-log:
      enabled: yes
      filetype: regular #regular|syslog|unix_dgram|unix_stream|redis
      filename: eve.json
      pcap-file: false
      community-id: false
      community-id-seed: 0
      types:
        - alert:
            metadata: yes
            # Enable the logging of tagged packets for rules using the
            # "tag" keyword.
            tagged-packets: yes
# ...
```

Sessions with matched alerts will be highlighted in the front-end and include which rule was matched.

# Security
Your Tulip instance will probably contain sensitive CTF information, like flags stolen from your machines. If you expose it to the internet and other people find it, you risk losing additional flags. It is recommended to host it on an internal network (for instance behind a VPN) or to put Tulip behind some form of authentication.

# Contributing
If you have an idea for a new feature, bug fixes, UX improvements, or other contributions, feel free to open a pull request or create an issue!      

# Credits
Tulip was written by [@RickdeJager](https://github.com/rickdejager) and [@Bazumo](https://github.com/bazumo), with additional help from [@Sijisu](https://github.com/sijisu). Thanks to our fellow Team Europe players and coaches for testing, feedback and suggestions. Finally, thanks to the team behind [flower](https://github.com/secgroup/flower) for opensourcing their tooling.
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions
Please only report issues that are present in the latest commit on the master branch.

## Reporting a Vulnerability
As this is an A/D CTF tool, most people will not run long-term publicly reachable instances. As such, feel free to report security issues directly in the github issues tracker.  
  
 If you prefer an email contact, you can email `tulip-sec<at>bricked.tech`.
```

## File: `dev.sh`
```bash
#!/bin/bash

# Requires internet
# docker-compose -f docker-compose.yml.dev up

docker-compose up -d mongo
docker-compose up -d api
```

## File: `docker-compose-suricata.yml`
```yaml
version: "3.5"
services:
  timescale:
    build: services/timescale
    image: tulip-timescale:latest
    restart: unless-stopped
    volumes:
    - timescale-data:/var/lib/postgresql/data
    - ./services/schema/system.sql:/docker-entrypoint-initdb.d/100_system.sql:ro
    - ./services/schema/functions.sql:/docker-entrypoint-initdb.d/101_functions.sql:ro
    - ./services/schema/schema.sql:/docker-entrypoint-initdb.d/102_schema.sql:ro
    networks:
      - internal
    environment:
      POSTGRES_HOST_AUTH_METHOD: trust
      POSTGRES_USER: tulip
      POSTGRES_DB: tulip
    # This does not need to be adjusted, unless you actually want to limit it
    # Postgres uses shared memory for caching, and docker assigns just 64 MB by default
    shm_size: '128g'

  frontend:
    build:
      context: frontend
      dockerfile: Dockerfile-frontend
    image: tulip-frontend:latest
    restart: unless-stopped
    ports:
      - "3000:3000"
    expose:
      - 3000
    depends_on:
      - timescale
      - api
    networks:
      - internal
    environment:
      API_SERVER_ENDPOINT: http://api:5000/
      VIRTUAL_HOST: tulip.h4xx.eu

  api:
    build:
      context: services/api
      dockerfile: Dockerfile-api
    image: tulip-api:latest
    restart: unless-stopped
    depends_on:
      - timescale
    networks:
      - internal
    volumes:
      - ${TRAFFIC_DIR_HOST}:${TRAFFIC_DIR_DOCKER}:ro
    environment:
      TIMESCALE: ${TIMESCALE}
      TULIP_TRAFFIC_DIR: ${TRAFFIC_DIR_DOCKER}
      FLAG_REGEX: ${FLAG_REGEX}
      TICK_START: ${TICK_START}
      TICK_LENGTH: ${TICK_LENGTH}
      VM_IP: ${VM_IP}

  flagids:
    restart: unless-stopped
    build:
      context: services/flagids
    image: tulip-flagids:latest
    depends_on:
      - timescale
    networks:
      - internal
    environment:
      TIMESCALE: ${TIMESCALE}
      TICK_START: ${TICK_START}
      TICK_LENGTH: ${TICK_LENGTH}
      FLAGID_SCRAPE: ${FLAGID_SCRAPE}
      TEAM_ID: ${TEAM_ID}
      FLAGID_ENDPOINT: ${FLAGID_ENDPOINT}
      VISUALIZER_URL: ${VISUALIZER_URL}
      DUMP_PCAPS: ${DUMP_PCAPS}

  assembler:
    build:
      context: services/go-importer
      dockerfile: Dockerfile-assembler
    image: tulip-assembler:latest
    restart: unless-stopped
    depends_on:
      - timescale
    networks:
      - internal
    volumes:
      - ${TRAFFIC_DIR_HOST}:${TRAFFIC_DIR_DOCKER}:ro,z
    # Command line flags most likely to fix a tulip issue:
    # - -http-session-tracking: enable HTTP session tracking
    # - -dir: directory to read traffic from
    # - -skipchecksum: skip checksum validation
    # - -flush-after: i.e. 2m Not needed in pcap rotation mode
    # - -disable-converters: disable converters
    # - -discard-extra-data: dont split large flow items, just discard them
    command: "./assembler -http-session-tracking -skipchecksum -disable-converters -dir ${TRAFFIC_DIR_DOCKER}"
    environment:
      TIMESCALE: ${TIMESCALE}
      FLAG_REGEX: ${FLAG_REGEX}
      TICK_START: ${TICK_START}
      TICK_LENGTH: ${TICK_LENGTH}
      FLAGID_SCAN: ${FLAGID_SCAN}
      FLAG_LIFETIME: ${FLAG_LIFETIME}
      FLAG_VALIDATOR_TYPE: ${FLAG_VALIDATOR_TYPE}
      FLAG_VALIDATOR_TEAM: ${FLAG_VALIDATOR_TEAM}
      PCAP_OVER_IP: ${PCAP_OVER_IP}
      DUMP_PCAPS: ${DUMP_PCAPS}
      DUMP_PCAPS_INTERVAL: ${DUMP_PCAPS_INTERVAL}
      DUMP_PCAPS_FILENAME: ${DUMP_PCAPS_FILENAME}
      BPF: ${BPF}
    extra_hosts:
      - "host.docker.internal:host-gateway"

  enricher:
    build:
      context: services/go-importer
      dockerfile: Dockerfile-enricher
    image: tulip-enricher:latest
    restart: unless-stopped
    depends_on:
      - timescale
    networks:
      - internal
    volumes:
      - ${SURICATA_DIR_HOST}/log:/suricata
      - ${TRAFFIC_DIR_HOST}:${TRAFFIC_DIR_DOCKER}:ro
    command: "./enricher -eve /suricata/eve.json"
    environment:
      TIMESCALE: ${TIMESCALE}

  suricata:
    image: jasonish/suricata:7.0
    restart: unless-stopped
    volumes:
      - ${TRAFFIC_DIR_HOST}:${TRAFFIC_DIR_DOCKER}:ro
      - ${SURICATA_DIR_HOST}/log:/var/log/suricata
      - ${SURICATA_DIR_HOST}/etc:/etc/suricata
      - ${SURICATA_DIR_HOST}/lib:/var/lib/suricata
    environment:
      SURICATA_OPTIONS: "-l /var/log/suricata -v -r ${TRAFFIC_DIR_DOCKER} --pcap-file-continuous"

volumes:
  timescale-data:

networks:
  internal:
```

## File: `docker-compose-test.yml`
```yaml
version: "3.2"
services:
  mongo:
    image: mongo:5
    networks:
      - internal
    restart: always
    ports:
      - "27017:27017"

  frontend:
    build:
      context: frontend
      dockerfile: Dockerfile-frontend
    image: tulip-frontend:latest
    restart: unless-stopped
    ports:
      - "3000:3000"
    depends_on:
      - mongo
      - api
    networks:
      - internal
    environment:
      API_SERVER_ENDPOINT: http://api:5000/

  api:
    build:
      context: services/api
      dockerfile: Dockerfile-api
    image: tulip-api:latest
    restart: unless-stopped
    depends_on:
      - mongo
    networks:
      - internal
    volumes:
      - ${TRAFFIC_DIR_HOST}:${TRAFFIC_DIR_DOCKER}:ro
    environment:
      TULIP_MONGO: ${TULIP_MONGO}
      TULIP_TRAFFIC_DIR: ${TRAFFIC_DIR_DOCKER}
      FLAG_REGEX: ${FLAG_REGEX}
      TICK_START: ${TICK_START}
      TICK_LENGTH: ${TICK_LENGTH}
      VM_IP: ${VM_IP}

  # Only for testing
  flagidendpoint:
    restart: always
    build:
      context: services/go-importer/test_data
    image: flagid-endpoint:latest
    depends_on:
      - mongo
    networks:
      - internal
    ports:
      - "127.0.0.1:8000:8000"

  flagids:
    restart: on-failure
    build:
      context: services/flagids
    image: tulip-flagids:latest
    depends_on:
      - mongo
      - flagidendpoint
    networks:
      - internal
    environment:
      TULIP_MONGO: ${TULIP_MONGO}
      TICK_START: ${TICK_START}
      TICK_LENGTH: ${TICK_LENGTH}
      FLAGID_SCRAPE: ${FLAGID_SCRAPE}
      TEAM_ID: ${TEAM_ID}
      FLAGID_ENDPOINT: ${FLAGID_ENDPOINT}

  assembler:
    build:
      context: services/go-importer
      dockerfile: Dockerfile-assembler
    image: tulip-assembler:latest
    restart: unless-stopped
    depends_on:
      - mongo
    networks:
      - internal
    volumes:
      - ${TRAFFIC_DIR_HOST}:${TRAFFIC_DIR_DOCKER}:ro
    command: "./assembler -dir ${TRAFFIC_DIR_DOCKER}"
    environment:
      DELAY: 5
      TULIP_MONGO: ${TULIP_MONGO}
      FLAG_REGEX: ${FLAG_REGEX}
      TICK_LENGTH: ${TICK_LENGTH}
      FLAGID_SCAN: ${FLAGID_SCAN}
      FLAG_LIFETIME: ${FLAG_LIFETIME}
      PCAP_OVER_IP: ${PCAP_OVER_IP}
    extra_hosts:
      - "host.docker.internal:host-gateway"


  enricher:
    build:
      context: services/go-importer
      dockerfile: Dockerfile-enricher
    image: tulip-enricher:latest
    restart: unless-stopped
    depends_on:
      - mongo
    networks:
      - internal
    volumes:
      - ${TRAFFIC_DIR_HOST}:${TRAFFIC_DIR_DOCKER}:ro
    command: "./enricher -eve ${TRAFFIC_DIR_DOCKER}/eve.json"
    environment:
      TULIP_MONGO: ${TULIP_MONGO}

networks:
  internal:
```

## File: `docker-compose.yml`
```yaml
version: "3.5"
services:
  timescale:
    build: services/timescale
    image: tulip-timescale:latest
    restart: unless-stopped
    volumes:
    - timescale-data:/var/lib/postgresql/data
    - ./services/schema/system.sql:/docker-entrypoint-initdb.d/100_system.sql:ro
    - ./services/schema/functions.sql:/docker-entrypoint-initdb.d/101_functions.sql:ro
    - ./services/schema/schema.sql:/docker-entrypoint-initdb.d/102_schema.sql:ro
    networks:
      - internal
    environment:
      POSTGRES_HOST_AUTH_METHOD: trust
      POSTGRES_USER: tulip
      POSTGRES_DB: tulip
    # This does not need to be adjusted, unless you actually want to limit it
    # Postgres uses shared memory for caching, and docker assigns just 64 MB by default
    shm_size: '128g'

  frontend:
    build:
      context: frontend
      dockerfile: Dockerfile-frontend
    image: tulip-frontend:latest
    restart: unless-stopped
    ports:
      - "3000:3000"
    expose:
      - 3000
    depends_on:
      - timescale
      - api
    networks:
      - internal
    environment:
      API_SERVER_ENDPOINT: http://api:5000/
      VIRTUAL_HOST: tulip.h4xx.eu

  api:
    build:
      context: services/api
      dockerfile: Dockerfile-api
    image: tulip-api:latest
    restart: unless-stopped
    depends_on:
      - timescale
    networks:
      - internal
    volumes:
      - ${TRAFFIC_DIR_HOST}:${TRAFFIC_DIR_DOCKER}:ro
    environment:
      TIMESCALE: ${TIMESCALE}
      TULIP_TRAFFIC_DIR: ${TRAFFIC_DIR_DOCKER}
      FLAG_REGEX: ${FLAG_REGEX}
      TICK_START: ${TICK_START}
      TICK_LENGTH: ${TICK_LENGTH}
      VM_IP: ${VM_IP}

  flagids:
    restart: unless-stopped
    build:
      context: services/flagids
    image: tulip-flagids:latest
    depends_on:
      - timescale
    networks:
      - internal
    environment:
      TIMESCALE: ${TIMESCALE}
      TICK_START: ${TICK_START}
      TICK_LENGTH: ${TICK_LENGTH}
      FLAGID_SCRAPE: ${FLAGID_SCRAPE}
      TEAM_ID: ${TEAM_ID}
      FLAGID_ENDPOINT: ${FLAGID_ENDPOINT}
      VISUALIZER_URL: ${VISUALIZER_URL}
      DUMP_PCAPS: ${DUMP_PCAPS}

  assembler:
    build:
      context: services/go-importer
      dockerfile: Dockerfile-assembler
    image: tulip-assembler:latest
    restart: unless-stopped
    depends_on:
      - timescale
    networks:
      - internal
    volumes:
      - ${TRAFFIC_DIR_HOST}:${TRAFFIC_DIR_DOCKER}:ro,z
    # Command line flags most likely to fix a tulip issue:
    # - -http-session-tracking: enable HTTP session tracking
    # - -dir: directory to read traffic from
    # - -skipchecksum: skip checksum validation
    # - -flush-after: i.e. 2m Not needed in pcap rotation mode
    # - -disable-converters: disable converters
    # - -discard-extra-data: dont split large flow items, just discard them
    command: "./assembler -http-session-tracking -skipchecksum -disable-converters -dir ${TRAFFIC_DIR_DOCKER}"
    environment:
      TIMESCALE: ${TIMESCALE}
      FLAG_REGEX: ${FLAG_REGEX}
      TICK_START: ${TICK_START}
      TICK_LENGTH: ${TICK_LENGTH}
      FLAGID_SCAN: ${FLAGID_SCAN}
      FLAG_LIFETIME: ${FLAG_LIFETIME}
      FLAG_VALIDATOR_TYPE: ${FLAG_VALIDATOR_TYPE}
      FLAG_VALIDATOR_TEAM: ${FLAG_VALIDATOR_TEAM}
      PCAP_OVER_IP: ${PCAP_OVER_IP}
      DUMP_PCAPS: ${DUMP_PCAPS}
      DUMP_PCAPS_INTERVAL: ${DUMP_PCAPS_INTERVAL}
      DUMP_PCAPS_FILENAME: ${DUMP_PCAPS_FILENAME}
      BPF: ${BPF}
    extra_hosts:
      - "host.docker.internal:host-gateway"

  enricher:
    build:
      context: services/go-importer
      dockerfile: Dockerfile-enricher
    image: tulip-enricher:latest
    restart: unless-stopped
    depends_on:
      - timescale
    networks:
      - internal
    volumes:
      - ${TRAFFIC_DIR_HOST}:${TRAFFIC_DIR_DOCKER}:ro,z
    command: "./enricher -eve ${TRAFFIC_DIR_DOCKER}/eve.json"
    environment:
      TIMESCALE: ${TIMESCALE}

volumes:
  timescale-data:

networks:
  internal:
```

## File: `start.sh`
```bash
#!/bin/bash

source .env

if [ -n "$FLAGID_SCRAPE" ]; then
  docker-compose -f docker-compose-flagid.yml up;
else
  docker-compose up 
fi

```

## File: `test.sh`
```bash
#!/bin/bash

docker compose -f docker-compose-test.yml up --build
```

## File: `frontend/.dockerignore`
```
node_modules
```

## File: `frontend/.env.development`
```
API_SERVER_ENDPOINT=http://localhost:5000/
```

## File: `frontend/.gitignore`
```
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
```

## File: `frontend/Dockerfile-frontend`
```
FROM node:17

COPY package.json /app/
COPY yarn.lock /app/

WORKDIR /app

RUN yarn

COPY . /app/

RUN yarn run build

EXPOSE 3000

CMD ["yarn", "run", "preview", "--host", "--port", "3000"]
```

## File: `frontend/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tulip</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

## File: `frontend/package.json`
```json
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "scripts": {
    "dev": "vite --host",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@heroicons/react": "^1.0.6",
    "@reduxjs/toolkit": "^1.8.5",
    "apexcharts": "^3.35.5",
    "buffer": "^6.0.3",
    "classnames": "^2.3.1",
    "color": "^4.2.3",
    "date-fns": "^2.28.0",
    "escape-string-regexp": "^5.0.0",
    "hexy": "^0.3.4",
    "http-parser-js": "^0.5.6",
    "react": "^18.0.0",
    "react-apexcharts": "^1.4.0",
    "react-diff-viewer": "^3.1.1",
    "react-dom": "^18.0.0",
    "react-hotkeys-hook": "^4.4.1",
    "react-redux": "^8.0.2",
    "react-router-dom": "^6.3.0",
    "react-virtuoso": "^2.12.1"
  },
  "devDependencies": {
    "@types/color": "^3.0.3",
    "@types/node": "^17.0.38",
    "@types/react": "^18.0.0",
    "@types/react-dom": "^18.0.0",
    "@vitejs/plugin-react": "^1.3.0",
    "autoprefixer": "^10.4.7",
    "postcss": "^8.4.13",
    "prettier": "^2.6.2",
    "tailwindcss": "^3.0.24",
    "typescript": "^4.6.3",
    "vite": "^2.9.13"
  }
}
```

## File: `frontend/postcss.config.js`
```javascript
module.exports = {
  plugins: {
    'tailwindcss/nesting': {},
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

## File: `frontend/tailwind.config.js`
```javascript
module.exports = {
  content: [
    './src/**/*.tsx',

  ],
  presets: [],
  darkMode: 'media', // or 'class'
  theme: {
    screens: {
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1280px',
      '2xl': '1536px',
    },
    colors: ({ colors }) => ({
      inherit: colors.inherit,
      current: colors.current,
      transparent: colors.transparent,
      black: colors.black,
      white: colors.white,
      slate: colors.slate,
      gray: colors.gray,
      zinc: colors.zinc,
      neutral: colors.neutral,
      stone: colors.stone,
      red: colors.red,
      orange: colors.orange,
      amber: colors.amber,
      yellow: colors.yellow,
      lime: colors.lime,
      green: colors.green,
      emerald: colors.emerald,
      teal: colors.teal,
      cyan: colors.cyan,
      sky: colors.sky,
      blue: colors.blue,
      indigo: colors.indigo,
      violet: colors.violet,
      purple: colors.purple,
      fuchsia: colors.fuchsia,
      pink: colors.pink,
      rose: colors.rose,
    }),
    columns: {
      auto: 'auto',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
      8: '8',
      9: '9',
      10: '10',
      11: '11',
      12: '12',
      '3xs': '16rem',
      '2xs': '18rem',
      xs: '20rem',
      sm: '24rem',
      md: '28rem',
      lg: '32rem',
      xl: '36rem',
      '2xl': '42rem',
      '3xl': '48rem',
      '4xl': '56rem',
      '5xl': '64rem',
      '6xl': '72rem',
      '7xl': '80rem',
    },
    spacing: {
      px: '1px',
      0: '0px',
      0.5: '0.125rem',
      1: '0.25rem',
      1.5: '0.375rem',
      2: '0.5rem',
      2.5: '0.625rem',
      3: '0.75rem',
      3.5: '0.875rem',
      4: '1rem',
      5: '1.25rem',
      6: '1.5rem',
      7: '1.75rem',
      8: '2rem',
      9: '2.25rem',
      10: '2.5rem',
      11: '2.75rem',
      12: '3rem',
      14: '3.5rem',
      16: '4rem',
      20: '5rem',
      24: '6rem',
      28: '7rem',
      32: '8rem',
      36: '9rem',
      40: '10rem',
      44: '11rem',
      48: '12rem',
      52: '13rem',
      56: '14rem',
      60: '15rem',
      64: '16rem',
      72: '18rem',
      80: '20rem',
      96: '24rem',
    },
    animation: {
      none: 'none',
      spin: 'spin 1s linear infinite',
      ping: 'ping 1s cubic-bezier(0, 0, 0.2, 1) infinite',
      pulse: 'pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      bounce: 'bounce 1s infinite',
    },
    aspectRatio: {
      auto: 'auto',
      square: '1 / 1',
      video: '16 / 9',
    },
    backdropBlur: ({ theme }) => theme('blur'),
    backdropBrightness: ({ theme }) => theme('brightness'),
    backdropContrast: ({ theme }) => theme('contrast'),
    backdropGrayscale: ({ theme }) => theme('grayscale'),
    backdropHueRotate: ({ theme }) => theme('hueRotate'),
    backdropInvert: ({ theme }) => theme('invert'),
    backdropOpacity: ({ theme }) => theme('opacity'),
    backdropSaturate: ({ theme }) => theme('saturate'),
    backdropSepia: ({ theme }) => theme('sepia'),
    backgroundColor: ({ theme }) => theme('colors'),
    backgroundImage: {
      none: 'none',
      'gradient-to-t': 'linear-gradient(to top, var(--tw-gradient-stops))',
      'gradient-to-tr': 'linear-gradient(to top right, var(--tw-gradient-stops))',
      'gradient-to-r': 'linear-gradient(to right, var(--tw-gradient-stops))',
      'gradient-to-br': 'linear-gradient(to bottom right, var(--tw-gradient-stops))',
      'gradient-to-b': 'linear-gradient(to bottom, var(--tw-gradient-stops))',
      'gradient-to-bl': 'linear-gradient(to bottom left, var(--tw-gradient-stops))',
      'gradient-to-l': 'linear-gradient(to left, var(--tw-gradient-stops))',
      'gradient-to-tl': 'linear-gradient(to top left, var(--tw-gradient-stops))',
    },
    backgroundOpacity: ({ theme }) => theme('opacity'),
    backgroundPosition: {
      bottom: 'bottom',
      center: 'center',
      left: 'left',
      'left-bottom': 'left bottom',
      'left-top': 'left top',
      right: 'right',
      'right-bottom': 'right bottom',
      'right-top': 'right top',
      top: 'top',
    },
    backgroundSize: {
      auto: 'auto',
      cover: 'cover',
      contain: 'contain',
    },
    blur: {
      0: '0',
      none: '0',
      sm: '4px',
      DEFAULT: '8px',
      md: '12px',
      lg: '16px',
      xl: '24px',
      '2xl': '40px',
      '3xl': '64px',
    },
    brightness: {
      0: '0',
      50: '.5',
      75: '.75',
      90: '.9',
      95: '.95',
      100: '1',
      105: '1.05',
      110: '1.1',
      125: '1.25',
      150: '1.5',
      200: '2',
    },
    borderColor: ({ theme }) => ({
      ...theme('colors'),
      DEFAULT: theme('colors.gray.200', 'currentColor'),
    }),
    borderOpacity: ({ theme }) => theme('opacity'),
    borderRadius: {
      none: '0px',
      sm: '0.125rem',
      DEFAULT: '0.25rem',
      md: '0.375rem',
      lg: '0.5rem',
      xl: '0.75rem',
      '2xl': '1rem',
      '3xl': '1.5rem',
      full: '9999px',
    },
    /*
    borderSpacing: ({ theme }) => ({
      ...theme('spacing'),
    }),
    */
    borderWidth: {
      DEFAULT: '1px',
      0: '0px',
      2: '2px',
      4: '4px',
      8: '8px',
    },
    boxShadow: {
      sm: '0 1px 2px 0 rgb(0 0 0 / 0.05)',
      DEFAULT: '0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)',
      md: '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)',
      lg: '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
      xl: '0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)',
      '2xl': '0 25px 50px -12px rgb(0 0 0 / 0.25)',
      inner: 'inset 0 2px 4px 0 rgb(0 0 0 / 0.05)',
      none: 'none',
    },
    boxShadowColor: ({ theme }) => theme('colors'),
    caretColor: ({ theme }) => theme('colors'),
    accentColor: ({ theme }) => ({
      ...theme('colors'),
      auto: 'auto',
    }),
    contrast: {
      0: '0',
      50: '.5',
      75: '.75',
      100: '1',
      125: '1.25',
      150: '1.5',
      200: '2',
    },
    container: {},
    content: {
      none: 'none',
    },
    cursor: {
      auto: 'auto',
      default: 'default',
      pointer: 'pointer',
      wait: 'wait',
      text: 'text',
      move: 'move',
      help: 'help',
      'not-allowed': 'not-allowed',
      none: 'none',
      'context-menu': 'context-menu',
      progress: 'progress',
      cell: 'cell',
      crosshair: 'crosshair',
      'vertical-text': 'vertical-text',
      alias: 'alias',
      copy: 'copy',
      'no-drop': 'no-drop',
      grab: 'grab',
      grabbing: 'grabbing',
      'all-scroll': 'all-scroll',
      'col-resize': 'col-resize',
      'row-resize': 'row-resize',
      'n-resize': 'n-resize',
      'e-resize': 'e-resize',
      's-resize': 's-resize',
      'w-resize': 'w-resize',
      'ne-resize': 'ne-resize',
      'nw-resize': 'nw-resize',
      'se-resize': 'se-resize',
      'sw-resize': 'sw-resize',
      'ew-resize': 'ew-resize',
      'ns-resize': 'ns-resize',
      'nesw-resize': 'nesw-resize',
      'nwse-resize': 'nwse-resize',
      'zoom-in': 'zoom-in',
      'zoom-out': 'zoom-out',
    },
    divideColor: ({ theme }) => theme('borderColor'),
    divideOpacity: ({ theme }) => theme('borderOpacity'),
    divideWidth: ({ theme }) => theme('borderWidth'),
    dropShadow: {
      sm: '0 1px 1px rgb(0 0 0 / 0.05)',
      DEFAULT: ['0 1px 2px rgb(0 0 0 / 0.1)', '0 1px 1px rgb(0 0 0 / 0.06)'],
      md: ['0 4px 3px rgb(0 0 0 / 0.07)', '0 2px 2px rgb(0 0 0 / 0.06)'],
      lg: ['0 10px 8px rgb(0 0 0 / 0.04)', '0 4px 3px rgb(0 0 0 / 0.1)'],
      xl: ['0 20px 13px rgb(0 0 0 / 0.03)', '0 8px 5px rgb(0 0 0 / 0.08)'],
      '2xl': '0 25px 25px rgb(0 0 0 / 0.15)',
      none: '0 0 #0000',
    },
    fill: ({ theme }) => theme('colors'),
    grayscale: {
      0: '0',
      DEFAULT: '100%',
    },
    hueRotate: {
      0: '0deg',
      15: '15deg',
      30: '30deg',
      60: '60deg',
      90: '90deg',
      180: '180deg',
    },
    invert: {
      0: '0',
      DEFAULT: '100%',
    },
    flex: {
      1: '1 1 0%',
      auto: '1 1 auto',
      initial: '0 1 auto',
      none: 'none',
    },
    flexBasis: ({ theme }) => ({
      auto: 'auto',
      ...theme('spacing'),
      '1/2': '50%',
      '1/3': '33.333333%',
      '2/3': '66.666667%',
      '1/4': '25%',
      '2/4': '50%',
      '3/4': '75%',
      '1/5': '20%',
      '2/5': '40%',
      '3/5': '60%',
      '4/5': '80%',
      '1/6': '16.666667%',
      '2/6': '33.333333%',
      '3/6': '50%',
      '4/6': '66.666667%',
      '5/6': '83.333333%',
      '1/12': '8.333333%',
      '2/12': '16.666667%',
      '3/12': '25%',
      '4/12': '33.333333%',
      '5/12': '41.666667%',
      '6/12': '50%',
      '7/12': '58.333333%',
      '8/12': '66.666667%',
      '9/12': '75%',
      '10/12': '83.333333%',
      '11/12': '91.666667%',
      full: '100%',
    }),
    flexGrow: {
      0: '0',
      DEFAULT: '1',
    },
    flexShrink: {
      0: '0',
      DEFAULT: '1',
    },
    fontFamily: {
      sans: [
        'Recursive',
        'ui-sans-serif',
        'system-ui',
        '-apple-system',
        'BlinkMacSystemFont',
        '"Segoe UI"',
        'Roboto',
        '"Helvetica Neue"',
        'Arial',
        '"Noto Sans"',
        'sans-serif',
        '"Apple Color Emoji"',
        '"Segoe UI Emoji"',
        '"Segoe UI Symbol"',
        '"Noto Color Emoji"',
      ],
      serif: ['ui-serif', 'Georgia', 'Cambria', '"Times New Roman"', 'Times', 'serif']
    },
    fontSize: {
      xs: ['0.75rem', { lineHeight: '1rem' }],
      sm: ['0.875rem', { lineHeight: '1.25rem' }],
      base: ['1rem', { lineHeight: '1.5rem' }],
      lg: ['1.125rem', { lineHeight: '1.75rem' }],
      xl: ['1.25rem', { lineHeight: '1.75rem' }],
      '2xl': ['1.5rem', { lineHeight: '2rem' }],
      '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
      '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
      '5xl': ['3rem', { lineHeight: '1' }],
      '6xl': ['3.75rem', { lineHeight: '1' }],
      '7xl': ['4.5rem', { lineHeight: '1' }],
      '8xl': ['6rem', { lineHeight: '1' }],
      '9xl': ['8rem', { lineHeight: '1' }],
    },
    fontWeight: {
      thin: '100',
      extralight: '200',
      light: '300',
      normal: '400',
      medium: '500',
      semibold: '600',
      bold: '700',
      extrabold: '800',
      black: '900',
    },
    gap: ({ theme }) => theme('spacing'),
    gradientColorStops: ({ theme }) => theme('colors'),
    gridAutoColumns: {
      auto: 'auto',
      min: 'min-content',
      max: 'max-content',
      fr: 'minmax(0, 1fr)',
    },
    gridAutoRows: {
      auto: 'auto',
      min: 'min-content',
      max: 'max-content',
      fr: 'minmax(0, 1fr)',
    },
    gridColumn: {
      auto: 'auto',
      'span-1': 'span 1 / span 1',
      'span-2': 'span 2 / span 2',
      'span-3': 'span 3 / span 3',
      'span-4': 'span 4 / span 4',
      'span-5': 'span 5 / span 5',
      'span-6': 'span 6 / span 6',
      'span-7': 'span 7 / span 7',
      'span-8': 'span 8 / span 8',
      'span-9': 'span 9 / span 9',
      'span-10': 'span 10 / span 10',
      'span-11': 'span 11 / span 11',
      'span-12': 'span 12 / span 12',
      'span-full': '1 / -1',
    },
    gridColumnEnd: {
      auto: 'auto',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
      8: '8',
      9: '9',
      10: '10',
      11: '11',
      12: '12',
      13: '13',
    },
    gridColumnStart: {
      auto: 'auto',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
      8: '8',
      9: '9',
      10: '10',
      11: '11',
      12: '12',
      13: '13',
    },
    gridRow: {
      auto: 'auto',
      'span-1': 'span 1 / span 1',
      'span-2': 'span 2 / span 2',
      'span-3': 'span 3 / span 3',
      'span-4': 'span 4 / span 4',
      'span-5': 'span 5 / span 5',
      'span-6': 'span 6 / span 6',
      'span-full': '1 / -1',
    },
    gridRowStart: {
      auto: 'auto',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
    },
    gridRowEnd: {
      auto: 'auto',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
    },
    gridTemplateColumns: {
      none: 'none',
      1: 'repeat(1, minmax(0, 1fr))',
      2: 'repeat(2, minmax(0, 1fr))',
      3: 'repeat(3, minmax(0, 1fr))',
      4: 'repeat(4, minmax(0, 1fr))',
      5: 'repeat(5, minmax(0, 1fr))',
      6: 'repeat(6, minmax(0, 1fr))',
      7: 'repeat(7, minmax(0, 1fr))',
      8: 'repeat(8, minmax(0, 1fr))',
      9: 'repeat(9, minmax(0, 1fr))',
      10: 'repeat(10, minmax(0, 1fr))',
      11: 'repeat(11, minmax(0, 1fr))',
      12: 'repeat(12, minmax(0, 1fr))',
    },
    gridTemplateRows: {
      none: 'none',
      1: 'repeat(1, minmax(0, 1fr))',
      2: 'repeat(2, minmax(0, 1fr))',
      3: 'repeat(3, minmax(0, 1fr))',
      4: 'repeat(4, minmax(0, 1fr))',
      5: 'repeat(5, minmax(0, 1fr))',
      6: 'repeat(6, minmax(0, 1fr))',
    },
    height: ({ theme }) => ({
      auto: 'auto',
      ...theme('spacing'),
      '1/2': '50%',
      '1/3': '33.333333%',
      '2/3': '66.666667%',
      '1/4': '25%',
      '2/4': '50%',
      '3/4': '75%',
      '1/5': '20%',
      '2/5': '40%',
      '3/5': '60%',
      '4/5': '80%',
      '1/6': '16.666667%',
      '2/6': '33.333333%',
      '3/6': '50%',
      '4/6': '66.666667%',
      '5/6': '83.333333%',
      full: '100%',
      screen: '100vh',
      min: 'min-content',
      max: 'max-content',
      fit: 'fit-content',
    }),
    inset: ({ theme }) => ({
      auto: 'auto',
      ...theme('spacing'),
      '1/2': '50%',
      '1/3': '33.333333%',
      '2/3': '66.666667%',
      '1/4': '25%',
      '2/4': '50%',
      '3/4': '75%',
      full: '100%',
    }),
    keyframes: {
      spin: {
        to: {
          transform: 'rotate(360deg)',
        },
      },
      ping: {
        '75%, 100%': {
          transform: 'scale(2)',
          opacity: '0',
        },
      },
      pulse: {
        '50%': {
          opacity: '.5',
        },
      },
      bounce: {
        '0%, 100%': {
          transform: 'translateY(-25%)',
          animationTimingFunction: 'cubic-bezier(0.8,0,1,1)',
        },
        '50%': {
          transform: 'none',
          animationTimingFunction: 'cubic-bezier(0,0,0.2,1)',
        },
      },
    },
    letterSpacing: {
      tighter: '-0.05em',
      tight: '-0.025em',
      normal: '0em',
      wide: '0.025em',
      wider: '0.05em',
      widest: '0.1em',
    },
    lineHeight: {
      none: '1',
      tight: '1.25',
      snug: '1.375',
      normal: '1.5',
      relaxed: '1.625',
      loose: '2',
      3: '.75rem',
      4: '1rem',
      5: '1.25rem',
      6: '1.5rem',
      7: '1.75rem',
      8: '2rem',
      9: '2.25rem',
      10: '2.5rem',
    },
    listStyleType: {
      none: 'none',
      disc: 'disc',
      decimal: 'decimal',
    },
    margin: ({ theme }) => ({
      auto: 'auto',
      ...theme('spacing'),
    }),
    maxHeight: ({ theme }) => ({
      ...theme('spacing'),
      full: '100%',
      screen: '100vh',
      min: 'min-content',
      max: 'max-content',
      fit: 'fit-content',
    }),
    maxWidth: ({ theme, breakpoints }) => ({
      none: 'none',
      0: '0rem',
      xs: '20rem',
      sm: '24rem',
      md: '28rem',
      lg: '32rem',
      xl: '36rem',
      '2xl': '42rem',
      '3xl': '48rem',
      '4xl': '56rem',
      '5xl': '64rem',
      '6xl': '72rem',
      '7xl': '80rem',
      full: '100%',
      min: 'min-content',
      max: 'max-content',
      fit: 'fit-content',
      prose: '65ch',
      ...breakpoints(theme('screens')),
    }),
    minHeight: {
      0: '0px',
      full: '100%',
      screen: '100vh',
      min: 'min-content',
      max: 'max-content',
      fit: 'fit-content',
    },
    minWidth: {
      0: '0px',
      full: '100%',
      min: 'min-content',
      max: 'max-content',
      fit: 'fit-content',
    },
    objectPosition: {
      bottom: 'bottom',
      center: 'center',
      left: 'left',
      'left-bottom': 'left bottom',
      'left-top': 'left top',
      right: 'right',
      'right-bottom': 'right bottom',
      'right-top': 'right top',
      top: 'top',
    },
    opacity: {
      0: '0',
      5: '0.05',
      10: '0.1',
      20: '0.2',
      25: '0.25',
      30: '0.3',
      40: '0.4',
      50: '0.5',
      60: '0.6',
      70: '0.7',
      75: '0.75',
      80: '0.8',
      90: '0.9',
      95: '0.95',
      100: '1',
    },
    order: {
      first: '-9999',
      last: '9999',
      none: '0',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
      8: '8',
      9: '9',
      10: '10',
      11: '11',
      12: '12',
    },
    padding: ({ theme }) => theme('spacing'),
    placeholderColor: ({ theme }) => theme('colors'),
    placeholderOpacity: ({ theme }) => theme('opacity'),
    outlineColor: ({ theme }) => theme('colors'),
    outlineOffset: {
      0: '0px',
      1: '1px',
      2: '2px',
      4: '4px',
      8: '8px',
    },
    outlineWidth: {
      0: '0px',
      1: '1px',
      2: '2px',
      4: '4px',
      8: '8px',
    },
    ringColor: ({ theme }) => ({
      DEFAULT: theme('colors.blue.500', '#3b82f6'),
      ...theme('colors'),
    }),
    ringOffsetColor: ({ theme }) => theme('colors'),
    ringOffsetWidth: {
      0: '0px',
      1: '1px',
      2: '2px',
      4: '4px',
      8: '8px',
    },
    ringOpacity: ({ theme }) => ({
      DEFAULT: '0.5',
      ...theme('opacity'),
    }),
    ringWidth: {
      DEFAULT: '3px',
      0: '0px',
      1: '1px',
      2: '2px',
      4: '4px',
      8: '8px',
    },
    rotate: {
      0: '0deg',
      1: '1deg',
      2: '2deg',
      3: '3deg',
      6: '6deg',
      12: '12deg',
      45: '45deg',
      90: '90deg',
      180: '180deg',
    },
    saturate: {
      0: '0',
      50: '.5',
      100: '1',
      150: '1.5',
      200: '2',
    },
    scale: {
      0: '0',
      50: '.5',
      75: '.75',
      90: '.9',
      95: '.95',
      100: '1',
      105: '1.05',
      110: '1.1',
      125: '1.25',
      150: '1.5',
    },
    scrollMargin: ({ theme }) => ({
      ...theme('spacing'),
    }),
    scrollPadding: ({ theme }) => theme('spacing'),
    sepia: {
      0: '0',
      DEFAULT: '100%',
    },
    skew: {
      0: '0deg',
      1: '1deg',
      2: '2deg',
      3: '3deg',
      6: '6deg',
      12: '12deg',
    },
    space: ({ theme }) => ({
      ...theme('spacing'),
    }),
    stroke: ({ theme }) => theme('colors'),
    strokeWidth: {
      0: '0',
      1: '1',
      2: '2',
    },
    textColor: ({ theme }) => theme('colors'),
    textDecorationColor: ({ theme }) => theme('colors'),
    textDecorationThickness: {
      auto: 'auto',
      'from-font': 'from-font',
      0: '0px',
      1: '1px',
      2: '2px',
      4: '4px',
      8: '8px',
    },
    textUnderlineOffset: {
      auto: 'auto',
      0: '0px',
      1: '1px',
      2: '2px',
      4: '4px',
      8: '8px',
    },
    textIndent: ({ theme }) => ({
      ...theme('spacing'),
    }),
    textOpacity: ({ theme }) => theme('opacity'),
    transformOrigin: {
      center: 'center',
      top: 'top',
      'top-right': 'top right',
      right: 'right',
      'bottom-right': 'bottom right',
      bottom: 'bottom',
      'bottom-left': 'bottom left',
      left: 'left',
      'top-left': 'top left',
    },
    transitionDelay: {
      75: '75ms',
      100: '100ms',
      150: '150ms',
      200: '200ms',
      300: '300ms',
      500: '500ms',
      700: '700ms',
      1000: '1000ms',
    },
    transitionDuration: {
      DEFAULT: '150ms',
      75: '75ms',
      100: '100ms',
      150: '150ms',
      200: '200ms',
      300: '300ms',
      500: '500ms',
      700: '700ms',
      1000: '1000ms',
    },
    transitionProperty: {
      none: 'none',
      all: 'all',
      DEFAULT:
        'color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter',
      colors: 'color, background-color, border-color, text-decoration-color, fill, stroke',
      opacity: 'opacity',
      shadow: 'box-shadow',
      transform: 'transform',
    },
    transitionTimingFunction: {
      DEFAULT: 'cubic-bezier(0.4, 0, 0.2, 1)',
      linear: 'linear',
      in: 'cubic-bezier(0.4, 0, 1, 1)',
      out: 'cubic-bezier(0, 0, 0.2, 1)',
      'in-out': 'cubic-bezier(0.4, 0, 0.2, 1)',
    },
    translate: ({ theme }) => ({
      ...theme('spacing'),
      '1/2': '50%',
      '1/3': '33.333333%',
      '2/3': '66.666667%',
      '1/4': '25%',
      '2/4': '50%',
      '3/4': '75%',
      full: '100%',
    }),
    width: ({ theme }) => ({
      auto: 'auto',
      ...theme('spacing'),
      '1/2': '50%',
      '1/3': '33.333333%',
      '2/3': '66.666667%',
      '1/4': '25%',
      '2/4': '50%',
      '3/4': '75%',
      '1/5': '20%',
      '2/5': '40%',
      '3/5': '60%',
      '4/5': '80%',
      '1/6': '16.666667%',
      '2/6': '33.333333%',
      '3/6': '50%',
      '4/6': '66.666667%',
      '5/6': '83.333333%',
      '1/12': '8.333333%',
      '2/12': '16.666667%',
      '3/12': '25%',
      '4/12': '33.333333%',
      '5/12': '41.666667%',
      '6/12': '50%',
      '7/12': '58.333333%',
      '8/12': '66.666667%',
      '9/12': '75%',
      '10/12': '83.333333%',
      '11/12': '91.666667%',
      full: '100%',
      screen: '100vw',
      min: 'min-content',
      max: 'max-content',
      fit: 'fit-content',
    }),
    willChange: {
      auto: 'auto',
      scroll: 'scroll-position',
      contents: 'contents',
      transform: 'transform',
    },
    zIndex: {
      auto: 'auto',
      0: '0',
      10: '10',
      20: '20',
      30: '30',
      40: '40',
      50: '50',
    },
  },
  variantOrder: [
    'first',
    'last',
    'odd',
    'even',
    'visited',
    'checked',
    'empty',
    'read-only',
    'group-hover',
    'group-focus',
    'focus-within',
    'hover',
    'focus',
    'focus-visible',
    'active',
    'disabled',
  ],
  plugins: [],
}
```

## File: `frontend/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "es2020",
    "useDefineForClassFields": true,
    "lib": ["DOM", "DOM.Iterable", "ESNext", "es2020"],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": false,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

## File: `frontend/tsconfig.node.json`
```json
{
  "compilerOptions": {
    "composite": true,
    "module": "esnext",
    "moduleResolution": "node"
  },
  "include": ["vite.config.ts"]
}
```

## File: `frontend/vite.config.ts`
```typescript
import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {


  const env = loadEnv(mode, process.cwd(), '')

  return ({
    plugins: [react()],
    build: {
      target: ['es2020']
    },
    server: {
      proxy: {
        '/api': {
          target: env["API_SERVER_ENDPOINT"] ?? "http://localhost:5000/",
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, '')
        }
      }
    }
  })
})
```

## File: `frontend/src/App.css`
```css


/* Grid */
.grid-container {
  display: grid;
  grid-template-columns: 400px 1fr;
  grid-template-rows: 50px calc(100vh - 50px);
  grid-column-gap: 0px;
  grid-row-gap: 0px;
}

.flow-list-area {
  grid-area: 2 / 1 / 3 / 2;
  border-right: 1px solid rgba(0, 0, 0, 0.2);
  overflow: auto;
}

.flow-details-area {
  grid-area: 2 / 2 / 3 / 3;
  overflow-y: auto;
  overflow-x: auto;
}

.header-area {
  grid-area: 1 / 1 / 2 / 3;
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

/* no need for footer
.footer-area {
  grid-area: 3 / 1 / 4 / 3;
}*/


/* Header */

.header {
  display: flex;
  align-items: center;
  height: 50px;
  @apply gap-3;

  input {
    @apply flex bg-gray-200 py-1 px-3 rounded-md;
  }

  .header-icon {
    @apply text-2xl pl-5 pr-2
  }
  
}

.text-mono {
  font-family: 'Recursive';
  --mono: "MONO" 1;
  font-variation-settings: var(--mono);
}


/* Loading state */
.sidebar-loading {
  background: #eee;
  background: linear-gradient(90deg, #ececec 8%, #f5f5f5 18%, #ececec 33%);
  border-radius: 5px;
  background-size: 200% 100%;
  animation: 3s shine linear infinite;
}

@keyframes shine {
  to {
    background-position-x: -400%;
  }
}
```

## File: `frontend/src/App.tsx`
```tsx
import { BrowserRouter, Routes, Route, Outlet } from "react-router-dom";
import { Suspense } from "react";
import { useHotkeys } from 'react-hotkeys-hook';

import "./App.css";
import { Header } from "./components/Header";
import { Home } from "./pages/Home";
import { FlowList } from "./components/FlowList";
import { FlowView } from "./pages/FlowView";
import { DiffView } from "./pages/DiffView";
import { Corrie } from "./components/Corrie";

function App() {
  useHotkeys('esc', () => (document.activeElement as HTMLElement).blur(), {enableOnFormTags: true});
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route
            path="flow/:id"
            element={
              <Suspense>
                <FlowView />
              </Suspense>
            }
          />
          <Route
            path="diff/:id"
            element={
              <Suspense>
                <DiffView />
              </Suspense>
            }
          />
          <Route
            path="corrie/"
            element={
              <Suspense>
                <Corrie />
              </Suspense>
            }
          />
        </Route>
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

function Layout() {
  return (
    <div className="grid-container">
      <header className="header-area">
        <div className="header">
          <Header></Header>
        </div>
      </header>
      <aside className="flow-list-area">
        <Suspense>
          <FlowList></FlowList>
        </Suspense>
      </aside>
      <main className="flow-details-area">
        <Outlet />
      </main>
      <footer className="footer-area"></footer>
    </div>
  );
}


function PageNotFound() {
  return (
    <div>
      <h2>404 Page not found</h2>
    </div>
  );
}

export default App;
```

## File: `frontend/src/api.ts`
```typescript
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

import { API_BASE_PATH } from "./const";
import {
  Service,
  FullFlow,
  TickInfo,
  Flow,
  FlowsQuery,
  StatsQuery,
  Stats,
  TicksAttackInfo,
  TicksAttackQuery,
} from "./types";

function base64DecodeUnicode(str: string) : string {
  const text = atob(str);
  const bytes = new Uint8Array(text.length);
  for(let i = 0; i < text.length; i++)
    bytes[i] = text.charCodeAt(i);
  return new TextDecoder().decode(bytes);
}

export const tulipApi = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: API_BASE_PATH }),
  endpoints: (builder) => ({
    getServices: builder.query<Service[], void>({
      query: () => "/services",
    }),
    getFlagRegex: builder.query<string, void>({
      query: () => "/flag_regex",
    }),
    getFlow: builder.query<FullFlow, string>({
      query: (id) => `/flow/${id}`,
      transformResponse: (flow: any): FullFlow => {
        const representations: any = {};

        for(const item of flow.items) {
          if(!(item.kind in representations))
            representations[item.kind] = { type: item.kind, flow: [] };
          representations[item.kind].flow.push({
            from: item.direction,
            data: base64DecodeUnicode(item.data),
            b64: item.data,
            time: new Date(item.time).getTime(),
          });
        }

        return {
          id: flow.id,
          src_port: flow.port_src,
          dst_port: flow.port_dst,
          src_ip: flow.ip_src,
          dst_ip: flow.ip_dst,
          time: new Date(flow.time).getTime(),
          duration: +(flow.duration * 1000).toFixed(0),
          num_packets: flow.packets_count,
          parent_id: flow.link_parent_id,
          child_id: flow.link_child_id,
          tags: flow.tags,
          flags: flow.flags,
          flagids: flow.flagids,
          filename: flow.pcap_name,
          service_tag: "",
          suricata: [],
          signatures: flow.signatures,
          flow: Object.values(representations),
        };
      },
    }),
    getFlows: builder.query<Flow[], FlowsQuery>({
      query: (query) => ({
        url: `/query`,
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: query,
      }),
      transformResponse: (response: Array<any>) => {
        return response.map((flow: any): Flow => ({
          id: flow.id,
          src_port: flow.port_src,
          dst_port: flow.port_dst,
          src_ip: flow.ip_src,
          dst_ip: flow.ip_dst,
          time: new Date(flow.time).getTime(),
          duration: +(flow.duration * 1000).toFixed(0),
          num_packets: flow.packets_count,
          parent_id: flow.link_parent_id,
          child_id: flow.link_child_id,
          tags: flow.tags,
          flags: flow.flags,
          flagids: flow.flagids,
          filename: flow.pcap_name,
          service_tag: "",
          suricata: [],
        }));
      },
    }),
    getStats: builder.query<Stats[], StatsQuery>({
      query: (query) => ({
        url: `/stats`,
        method: "GET",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        params: {
          service: query.service,
          tick_from: query.tick_from,
          tick_to: query.tick_to,
        }
      })
    }),
    getTags: builder.query<string[], void>({
      query: () => `/tags`,
    }),
    getTickInfo: builder.query<TickInfo, void>({
      query: () => `/tick_info`,
    }),
    getUnderAttack: builder.query<TicksAttackInfo, TicksAttackQuery>({
      query: (query) => ({
        url: '/under_attack',
        params: {
          from_tick: query.from_tick,
          to_tick: query.to_tick,
        }
      }),
    }),
    toPwnTools: builder.query<string, string>({
      query: (id) => ({ url: `/to_pwn/${id}`, responseHandler: "text" }),
    }),
    toSinglePythonRequest: builder.query<
      string,
      { body: string; id: string; item_index: number; tokenize: boolean }
    >({
      query: ({ body, id, item_index, tokenize }) => ({
        url: `/to_single_python_request?tokenize=${
          tokenize ? "1" : "0"
        }&id=${id}&index=${item_index}`,
        method: "POST",
        responseHandler: "text",
        headers: {
          "Content-Type": "text/plain;charset=UTF-8",
        },
        body,
      }),
    }),
    toFullPythonRequest: builder.query<string, string>({
      query: (id) => ({
        url: `/to_python_request/${id}`,
        responseHandler: "text",
      }),
    }),
    starFlow: builder.mutation<unknown, { id: string; star: boolean }>({
      query: ({ id, star }) => ({
        url: `/star`,
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: { id, star },
      }),
      // TODO: optimistic cache update

      async onQueryStarted({ id, star }, { dispatch, queryFulfilled }) {
        // `updateQueryData` requires the endpoint name and cache key arguments,
        // so it knows which piece of cache state to update
        const patchResult = dispatch(
          tulipApi.util.updateQueryData("getFlows", {service: "undefined", tags_include: [], tags_exclude:[]}, (flows) => {
            // The `flows` is Immer-wrapped and can be "mutated" like in createSlice
            const flow = flows.find((flow) => flow.id === id);
            if (flow) {
              if (star) {
                flow.tags.push("starred");
              } else {
                flow.tags = flow.tags.filter((tag) => tag != "starred");
              }
            }
          })
        );
        try {
          await queryFulfilled;
        } catch {
          patchResult.undo();
        }
      },
    }),
  }),
});

export const {
  useGetServicesQuery,
  useGetFlagRegexQuery,
  useGetFlowQuery,
  useGetFlowsQuery,
  useLazyGetFlowsQuery,
  useGetTagsQuery,
  useGetTickInfoQuery,
  useLazyToPwnToolsQuery,
  useLazyToFullPythonRequestQuery,
  useToSinglePythonRequestQuery,
  useStarFlowMutation,
  useGetStatsQuery,
  useGetUnderAttackQuery,
} = tulipApi;
```

## File: `frontend/src/const.ts`
```typescript
export const API_BASE_PATH = `${window.location.origin}/api`;

export const TEXT_FILTER_KEY = "text";
export const SERVICE_FILTER_KEY = "service";
export const START_FILTER_KEY = "start";
export const END_FILTER_KEY = "end";
export const FIRST_DIFF_KEY = "first";
export const SECOND_DIFF_KEY = "second";
export const REPR_ID_KEY = "reprid";
export const CORRELATION_MODE_KEY = "correlation";

export const SERVICE_REFETCH_INTERVAL_MS = 15000;
export const TICK_REFETCH_INTERVAL_MS = 10000;
export const FLOW_LIST_REFETCH_INTERVAL_MS = 30000;
export const UNDER_ATTACK_REFETCH_INTERVAL_MS = 30000;
export const MAX_LENGTH_FOR_HIGHLIGHT = 400000;

export const FORCE_REFETCH_ON_STAR = true;
```

## File: `frontend/src/index.css`
```css
@import url('https://fonts.googleapis.com/css2?family=Recursive:wght,MONO@300..800,0..1&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;
```

## File: `frontend/src/main.tsx`
```tsx
import React from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { store } from "./store";
import App from "./App";
import "./index.css";

const container = document.getElementById("root")!;
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);
```

## File: `frontend/src/tick.ts`
```typescript
import { useSearchParams } from "react-router-dom";

import {
  END_FILTER_KEY,
  START_FILTER_KEY,
  TICK_REFETCH_INTERVAL_MS,
} from "./const";
import { useGetTickInfoQuery } from "./api";

export function getTickStuff() {
  const { data: tickInfoData } = useGetTickInfoQuery(undefined, {
    pollingInterval: TICK_REFETCH_INTERVAL_MS,
  });
  const startDate = tickInfoData?.startDate ?? "1970-01-01T00:00:00Z";
  const tickLength = tickInfoData?.tickLength ?? 1000;
  const flagLifetime = tickInfoData?.flagLifetime ?? 0;
  const currentTick = unixTimeToTick(new Date().valueOf());

  function tickToUnixTime(tick: number): number {
    return new Date(startDate).valueOf() + tickLength * tick;;
  }

  function unixTimeToTick(unixTime: number): number {
    return Math.floor(
      (unixTime - new Date(startDate).valueOf()) / tickLength
    );
  }

  let [searchParams, setSearchParams] = useSearchParams();
  const startTimeParam = searchParams.get(START_FILTER_KEY);
  const endTimeParam = searchParams.get(END_FILTER_KEY);
  const startTimeParamUnix = startTimeParam === null ? undefined : parseInt(startTimeParam);
  const endTimeParamUnix = endTimeParam === null ? undefined : parseInt(endTimeParam);
  const startTickParam = startTimeParamUnix === undefined ? undefined : unixTimeToTick(startTimeParamUnix);
  const endTickParam = endTimeParamUnix === undefined ? undefined : unixTimeToTick(endTimeParamUnix);

  function setTimeParam(startTick: number | null, param: string) {
    if (startTick === null) {
      searchParams.delete(param);
    } else {
      searchParams.set(param, tickToUnixTime(startTick).toString());
    }
    setSearchParams(searchParams);
  }

  function setToLastnTicks(n: number) {
    const startTick = (currentTick ?? 0) - n;
    const endTick = (currentTick ?? 0) + 1; // to be sure
    setTimeParam(startTick, START_FILTER_KEY);
    setTimeParam(endTick, END_FILTER_KEY);
  }

  return {
    startDate,
    tickLength,
    flagLifetime,
    currentTick,
    tickToUnixTime,
    unixTimeToTick,
    startTickParam,
    endTickParam,
    setTimeParam,
    setToLastnTicks,
  }

}
```

## File: `frontend/src/types.ts`
```typescript
export interface Flow {
  id: Id;
  src_port: number;
  dst_port: number;
  src_ip: string;
  dst_ip: string;
  time: number;
  duration: number;
  // TODO: Get this from backend instead of hacky workaround
  service_tag: string;
  num_packets: number;
  parent_id: Id;
  child_id: Id;
  tags: string[];
  flags: string[];
  flagids: string[];
  suricata: number[];
  filename: string;
}

export interface TickInfo {
  startDate: string;
  tickLength: number;
  flagLifetime: number;
}

export interface FullFlow extends Flow {
  signatures: Signature[];
  flow: FlowRepresentation[];
}

export type Id = string;

export interface FlowRepresentation {
  type: string;
  flow: FlowData[];
}

export interface FlowData {
  from: string;
  data: string;
  b64: string;
  time: number;
}

export interface Signature {
  id: number;
  message: string;
  action: string;
}

// TODO: pagination WTF
export interface FlowsQuery {
  // Text filter
  regex_insensitive?: string;
  // Service filter
  // TODO: Why not use service name here?
  service?: string;
  ip_dst?: string;
  port_dst?: number;
  time_from?: string;
  time_to?: string;
  tags_include?: string[];
  tags_exclude?: string[];
  tag_intersection_mode?: "AND" | "OR";
  flags?: string[];
  flagids?: string[];
}

export interface StatsQuery {
  service: string;
  tick_from: number;
  tick_to: number;
}

export interface Stats {
  [key: string]: number; // little hack to make typescript happy
  tick: number;
  tag_flag_in: number;
  tag_flag_out: number;
  tag_blocked: number;
  tag_suricata: number;
  tag_enemy: number;
  flag_in: number;
  flag_out: number;
};

export type Service = {
  ip: string;
  port: number;
  name: string;
};

export type TicksAttackInfo = Record<number, Record<string, number>>;

export interface TicksAttackQuery {
  from_tick: number;
  to_tick: number;
}
```

## File: `frontend/src/vite-env.d.ts`
```typescript
/// <reference types="vite/client" />
```

## File: `frontend/src/components/Corrie.tsx`
```tsx
import { useSearchParams, useNavigate } from "react-router-dom";
import { useCallback } from "react";
import { Flow, Stats, TicksAttackInfo } from "../types";
import {
  SERVICE_FILTER_KEY,
  TEXT_FILTER_KEY,
  START_FILTER_KEY,
  END_FILTER_KEY,
  CORRELATION_MODE_KEY,
  FLOW_LIST_REFETCH_INTERVAL_MS,
  UNDER_ATTACK_REFETCH_INTERVAL_MS,
} from "../const";
import useDebounce from "../hooks/useDebounce";

import ReactApexChart from "react-apexcharts";
import { ApexOptions } from "apexcharts";
import {
  useGetFlowsQuery,
  useGetServicesQuery,
  useGetStatsQuery,
  useGetUnderAttackQuery
} from "../api";
import { getTickStuff } from "../tick";
import { useAppSelector } from "../store";
import { tagToColor } from "./Tag";

interface TickInfoData {
  startTick: number;
  endTick: number;
  flagLifetime: number;
  tickToUnixTime: (a: number) => number;
  unixTimeToTick: (a: number) => number;
}
interface GraphProps {
  flowList: Flow[];
  statsList: Stats[];
  underAttackData: TicksAttackInfo;
  mode: string;
  searchParams: URLSearchParams;
  setSearchParams: (a: URLSearchParams) => void;
  onClickNavigate: (a: string) => void;
  tickInfoData: TickInfoData
}

export const Corrie = () => {
  const { data: services } = useGetServicesQuery();
  const includeTags = useAppSelector((state) => state.filter.includeTags);
  const excludeTags = useAppSelector((state) => state.filter.excludeTags);
  const filterFlags = useAppSelector((state) => state.filter.filterFlags);
  const filterFlagids = useAppSelector((state) => state.filter.filterFlagids);
  const tagIntersectionMode = useAppSelector((state) => state.filter.tagIntersectionMode);

  const [searchParams, setSearchParams] = useSearchParams();

  const service_name = searchParams.get(SERVICE_FILTER_KEY) ?? "";
  const service = services && services.find((s) => s.name == service_name);

  const text_filter = searchParams.get(TEXT_FILTER_KEY) ?? undefined;
  const from_filter = searchParams.get(START_FILTER_KEY) ?? undefined;
  const to_filter = searchParams.get(END_FILTER_KEY) ?? undefined;

  const debounced_text_filter = useDebounce(text_filter, 300);

  const mode = searchParams.get("correlation") ?? "time";
  const setCorrelationMode = (mode: string) => {
    searchParams.set(CORRELATION_MODE_KEY, mode);
    setSearchParams(searchParams);
  };

  const inactiveButtonClass = "bg-blue-100 text-gray-800 rounded-md px-2 py-1";
  const activeButtonClass = `${inactiveButtonClass} ring-2 ring-gray-500`;

  const navigate = useNavigate();
  const onClickNavigate = useCallback(
    (loc: string) => navigate(loc, { replace: true }),
    [navigate]
  );

  let { currentTick, flagLifetime, startTickParam, endTickParam, unixTimeToTick, tickToUnixTime } = getTickStuff();

  let startTick = startTickParam ?? 0;
  let endTick = endTickParam ?? currentTick;
  if (startTick < 0) {
    startTick = 0;
  }
  if (endTick < startTick) {
    endTick = startTick;
  }

  const needsStats = mode == "flags" || mode == "tags";

  const statsData = needsStats ? useGetStatsQuery(
    {
      service: service_name,
      tick_from: startTick,
      tick_to: endTick,
    }
  ).data : [];

  const flowData = !needsStats ? useGetFlowsQuery(
    {
      regex_insensitive: debounced_text_filter,
      ip_dst: service?.ip,
      port_dst: service?.port,
      time_from: from_filter ? new Date(parseInt(from_filter)).toISOString() : undefined,
      time_to: to_filter ? new Date(parseInt(to_filter)).toISOString() : undefined,
      tags_include: includeTags,
      tags_exclude: excludeTags,
      tag_intersection_mode: tagIntersectionMode,
      flags: filterFlags,
      flagids: filterFlagids,
    },
    {
      refetchOnMountOrArgChange: true,
      pollingInterval: FLOW_LIST_REFETCH_INTERVAL_MS,
    }
  ).data : [];

  // TODO: this fetches under attack data always - not sure how to fetch it only in under-attack mode due to react hooks having to be called in same order always
  const underAttackData = useGetUnderAttackQuery(
    {
      from_tick: startTick,
      to_tick: endTick + flagLifetime,
    },
    {
      pollingInterval: UNDER_ATTACK_REFETCH_INTERVAL_MS,
    }
  ).data;

  // TODO: fix the below transformation - move it to server
  // Diederik gives you a beer once it has been fixed
  const transformedFlowData = flowData?.map((flow) => ({
    ...flow,
    service_tag:
      services?.find((s) => s.ip === flow.dst_ip && s.port === flow.dst_port)
        ?.name ?? "unknown",
  }));

  const graphProps: GraphProps = {
    flowList: transformedFlowData || [],
    statsList: statsData || [],
    underAttackData: underAttackData || {},
    mode: mode,
    searchParams: searchParams,
    setSearchParams: setSearchParams,
    onClickNavigate: onClickNavigate,
    tickInfoData: { startTick, endTick, flagLifetime, unixTimeToTick, tickToUnixTime },
  };

  return (
    <div className="flex flex-col h-full">
      <div className="text-sm bg-white border-b-gray-300 border-b shadow-md flex flex-col">
        <div className="p-2 flex space-x-2" style={{ height: 50 }}>
          <a className="text-center px-2 py-2">Correlation mode: </a>
          <button
            className={mode == "time" ? activeButtonClass : inactiveButtonClass}
            onClick={() => setCorrelationMode("time")}
          >
            time
          </button>
          <button
            className={
              mode == "packets" ? activeButtonClass : inactiveButtonClass
            }
            onClick={() => setCorrelationMode("packets")}
          >
            packets
          </button>
          <button
            className={mode == "volume" ? activeButtonClass : inactiveButtonClass}
            onClick={() => setCorrelationMode("volume")}
          >
            volume
          </button>
          <button
            className={mode == "tags" ? activeButtonClass : inactiveButtonClass}
            onClick={() => setCorrelationMode("tags")}
          >
            tags
          </button>
          <button
            className={mode == "flags" ? activeButtonClass : inactiveButtonClass}
            onClick={() => setCorrelationMode("flags")}
          >
            flags
          </button>
          <button
            className={mode == "under-attack" ? activeButtonClass : inactiveButtonClass}
            onClick={() => setCorrelationMode("under-attack")}
          >
            under attack
          </button>
          <p className="text-left px-2 py-2">After clicking on a flow, press 'w' to scroll to it in flow list</p>
        </div>
      </div>
      <div className="flex-1 w-full overflow-hidden p-4">
        {(mode == "packets" || mode == "time") && TimePacketGraph(graphProps)}
        {mode == "volume" && VolumeGraph(graphProps)}
        {(mode == "tags" || mode == "flags") && BarPerTickGraph(graphProps, mode)}
        {(mode == "under-attack") && UnderAttackGraph(graphProps)}
      </div>
    </div>
  );
};

function BarPerTickGraph(graphProps: GraphProps, mode: string) {
  const statsList = graphProps.statsList;
  const searchParams = graphProps.searchParams;
  const setSearchParams = graphProps.setSearchParams;
  let startTick = graphProps.tickInfoData.startTick;
  let endTick = graphProps.tickInfoData.endTick;
  let tickToUnixTime = graphProps.tickInfoData.tickToUnixTime;

  const SEARCH_CAP = 50;
  const DEFAULT_CAP = 15;

  // Hard limit for performance reasons
  if (searchParams.has(START_FILTER_KEY) && searchParams.has(END_FILTER_KEY)) {
    startTick = Math.max(Math.max(0, startTick), endTick - SEARCH_CAP);
  } else if (endTick - startTick > DEFAULT_CAP) {
    startTick = Math.max(0, endTick - DEFAULT_CAP);
  }

  var options: ApexOptions = {
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "90%",
      }
    },
    grid: {
      position: "back",
      xaxis: {
        lines: {
          show: endTick !== startTick + 1
        }
      },
      yaxis: {
        lines: {
          show: false
        }
      }
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: Array.from({ length: endTick - startTick }, (_, i) => startTick + i),
      title: {
        text: "Ticks"
      }
    },
    yaxis: {
      title: {
        text: "Number of flows"
      }
    },
    tooltip: {
      x: {
        formatter: function (v) {
          return "Tick " + v;
        }
      }
    },
    chart: {
      animations: {
        enabled: false
      },
      events: {
        click: function (e, chartContext, options) {
          const tick = options.dataPointIndex;
          if (tick !== -1) {
            const start = Math.floor(tickToUnixTime(tick + startTick));
            const end = Math.ceil(tickToUnixTime(tick + startTick + 1));
            searchParams.set(START_FILTER_KEY, start.toString());
            searchParams.set(END_FILTER_KEY, end.toString());
            setSearchParams(searchParams);
          }
        },
      },
    },
  };

  let series: ApexAxisChartSeries = [];

  const colors: any = {
    "tag_flag_in": tagToColor("flag-in"),
    "tag_flag_out": tagToColor("flag-out"),
    "tag_enemy": tagToColor("enemy"),
    "tag_blocked": tagToColor("blocked"),
    "tag_suricata": tagToColor("suricata"),

    "flag_in": tagToColor("flag-in"),
    "flag_out": tagToColor("flag-out"),
  };

  Object.keys(colors).forEach(t => {
    if ((mode == "tags" && t.startsWith("tag_")) || (mode == "flags" && t.startsWith("flag_"))) {
      const data = Array(endTick - startTick).fill(0);

      statsList.forEach(s => {
        data[s.tick - startTick] = s[t];
      });

      series.push({
        name: t,
        data: data,
        color: colors[t]
      });
    }
  });

  return (
    <ReactApexChart
      options={options}
      series={series}
      type="bar"
      height="100%"
      width="100%"
    />
  );
}

function TimePacketGraph(graphProps: GraphProps) {
  const flowList = graphProps.flowList;
  const mode = graphProps.mode;
  const searchParams = graphProps.searchParams;
  const setSearchParams = graphProps.setSearchParams;
  const onClickNavigate = graphProps.onClickNavigate;

  const series: ApexAxisChartSeries = [
    {
      name: "Flows",
      data: flowList.map((flow) => {
        let y = flow.duration;
        if (mode == "packets") {
          y = flow.num_packets;
        }
        return { x: flow.time, y: y };
      }),
    },
  ];

  const options: ApexOptions = {
    dataLabels: {
      enabled: false,
    },
    grid: {
      xaxis: {
        lines: {
          show: true,
        },
      },
      yaxis: {
        lines: {
          show: true,
        },
      },
    },
    xaxis: {
      type: "datetime", // FIXME: Timezone is not displayed correctly
    },
    labels: flowList.map((flow) => {
      return flow.id;
    }),
    chart: {
      animations: {
        enabled: false,
      },
      events: {
        dataPointSelection: (event: any, chartContext: any, config: any) => {
          // Retrieve flowList from chart's labels. This is hacky, refer to FIXME above.
          const flowIdList = config.w.config.labels;
          const flow = flowIdList[config.dataPointIndex];
          onClickNavigate(`/flow/${flow}?${searchParams}`);
        },
        beforeZoom: function (chartContext, { xaxis }) {
          const start = Math.floor(xaxis.min);
          const end = Math.ceil(xaxis.max);
          searchParams.set(START_FILTER_KEY, start.toString());
          searchParams.set(END_FILTER_KEY, end.toString());
          setSearchParams(searchParams);
        },
      },
    },
  };

  return (
    <ReactApexChart
      options={options}
      series={series}
      type="scatter"
      width="100%"
      height="100%"
    />
  );
}

function VolumeGraph(graphProps: GraphProps) {
  const flowList = graphProps.flowList;
  const mode = graphProps.mode;
  const searchParams = graphProps.searchParams;
  const setSearchParams = graphProps.setSearchParams;

  function chunkData(flowList: Flow[]) {
    let ret: any = [];
    let ts = 0;
    let acc = 0;
    const window_size = 30000;
    flowList.forEach((flow) => {
      if (ts == 0) {
        ts = flow.time;
      }

      if (ts - flow.time > window_size) {
        ret.push({ x: ts, y: acc });
        ts = 0;
        acc = 0;
      } else {
        acc++;
      }
    });

    return ret;
  }

  const series_out: ApexAxisChartSeries = [
    {
      name: "Volume",
      data: chunkData(flowList),
    },
  ];

  const options: ApexOptions = {
    dataLabels: {
      enabled: false,
    },
    grid: {
      xaxis: {
        lines: {
          show: true,
        },
      },
      yaxis: {
        lines: {
          show: true,
        },
      },
    },
    xaxis: {
      type: "datetime", // FIXME: Timezone is not displayed correctly
    },
    labels: flowList.map((flow) => {
      return flow.id;
    }),
    chart: {
      animations: {
        enabled: false,
      },
      events: {
        beforeZoom: function (chartContext, { xaxis }) {
          const start = Math.floor(xaxis.min);
          const end = Math.ceil(xaxis.max);
          searchParams.set(START_FILTER_KEY, start.toString());
          searchParams.set(END_FILTER_KEY, end.toString());
          setSearchParams(searchParams);
        },
      },
    },
  };

  return <ReactApexChart options={options} series={series_out} type="line" />;
}

function UnderAttackGraph(graphProps: GraphProps) {
  const underAttackData = graphProps.underAttackData;
  const tickInfoData = graphProps.tickInfoData;
  const tickToUnixTime = tickInfoData.tickToUnixTime;
  const searchParams = graphProps.searchParams;
  const setSearchParams = graphProps.setSearchParams;

  const options: ApexOptions = {
    plotOptions: {
      bar: {
        horizontal: true,
        barHeight: '30%',
        rangeBarGroupRows: true,
      },
    },
    tooltip: {
      custom: (opts) => {
        if (opts.y1 === opts.y2 - 1) return `Tick ${opts.y1}`;

        return `Ticks ${opts.y1} - ${opts.y2 - 1}`;
      },
    },
    legend: {
      show: false,
    },
    xaxis: {
      min: tickInfoData.startTick,
      max: tickInfoData.endTick,
      tickAmount: Math.min(Math.abs(tickInfoData.startTick - tickInfoData.endTick), 25),
      decimalsInFloat: 0,
      title: {
        text: "Tick",
      },
    },
    yaxis: {
      tickAmount: 0,
    },
    chart: {
      animations: {
        enabled: false,
      },
      events: {
        dataPointSelection: (event, ctx, config) => {
          const y = config.w.config.series[config.seriesIndex].data[0].y;
          const start = Math.floor(tickToUnixTime(y[0]));
          const end = Math.ceil(tickToUnixTime(y[1]));
          searchParams.set(START_FILTER_KEY, start.toString());
          searchParams.set(END_FILTER_KEY, end.toString());
          setSearchParams(searchParams);
        },
        beforeZoom: function (chartContext, { xaxis }) {
          const start = Math.floor(tickToUnixTime(xaxis.min));
          const end = Math.ceil(tickToUnixTime(xaxis.max));
          searchParams.set(START_FILTER_KEY, start.toString());
          searchParams.set(END_FILTER_KEY, end.toString());
          setSearchParams(searchParams);
        },
      },
    }
  };

  // TODO: service names between visualizer and tulip don't necessarily match, how should we consider filters?
  const ranges: Record<string, { from_tick: number, to_tick: number }[]> = {};
  const lastSeen: Record<string, number | undefined> = {};
  for (const tick in underAttackData) {
    const tickNumber = Number(tick);
    let from_tick = Math.max(0, tickNumber - (tickInfoData.flagLifetime - 1));

    const services = underAttackData[tick];
    for (const service in services) {
      const value = services[service];
      if (value <= 0) continue;

      ranges[service] = ranges[service] || [];

      // Heuristic: if we had previous ticks where we lost the flags, most likely an attack occured afterward
      if (lastSeen[service] !== undefined) from_tick = Math.max(from_tick, lastSeen[service]!);

      ranges[service].push({
        from_tick: from_tick,
        to_tick: tickNumber + 1,
      })
      lastSeen[service] = tickNumber + 1;
    }
  }

  const series: ApexAxisChartSeries = [];
  for (const service in ranges) {
    for (const range of ranges[service]) {
      series.push({
        data: [
          {
            x: service,
            y: [range.from_tick, range.to_tick],
            goals: [
              {
                name: 'tick start',
                value: range.to_tick - 1,
                strokeColor: '#CD2F2A',
              },
              {
                name: 'tick end',
                value: range.to_tick,
                strokeColor: '#CD2F2A',
              }
            ],
          },
        ],
      })
    }
  }

  return <ReactApexChart options={options} series={series} type="rangeBar" />;
}
```

## File: `frontend/src/components/FlowList.module.css`
```css
.list_container {

    @apply flex flex-col;

    a {
        @apply pb-1;
    }

    li {
        @apply bg-gray-100 p-2 focus:ring-4 border-t border-gray-200 list-none;
    }

    li.active {
        @apply border-y border-l-4 border-gray-500 bg-gray-300/50
    }

}
```

## File: `frontend/src/components/FlowList.tsx`
```tsx
import {
  useSearchParams,
  Link,
  useParams,
  useNavigate,
} from "react-router-dom";
import { useState, useRef, useEffect } from "react";
import { useHotkeys } from 'react-hotkeys-hook';
import { FetchBaseQueryError } from '@reduxjs/toolkit/query'
import { Flow } from "../types";
import {
  SERVICE_FILTER_KEY,
  TEXT_FILTER_KEY,
  START_FILTER_KEY,
  END_FILTER_KEY,
  FLOW_LIST_REFETCH_INTERVAL_MS,
  FORCE_REFETCH_ON_STAR,
} from "../const";
import { useAppSelector, useAppDispatch } from "../store";
import { toggleFilterTag, toggleTagIntersectMode } from "../store/filter";

import { HeartIcon, FilterIcon, LinkIcon } from "@heroicons/react/solid";
import { HeartIcon as EmptyHeartIcon } from "@heroicons/react/outline";

import classes from "./FlowList.module.css";
import { format } from "date-fns";
import useDebounce from "../hooks/useDebounce";
import { Virtuoso, VirtuosoHandle } from "react-virtuoso";
import classNames from "classnames";
import { Tag } from "./Tag";
import {
  useGetFlowsQuery,
  useGetServicesQuery,
  useGetTagsQuery,
  useStarFlowMutation,
} from "../api";

export function FlowList() {
  let [searchParams] = useSearchParams();
  let params = useParams();

  // we add a local variable to prevent racing with the browser location API
  let openedFlowID = params.id

  const { data: availableTags } = useGetTagsQuery();
  const { data: services } = useGetServicesQuery();

  const filterFlags = useAppSelector((state) => state.filter.filterFlags);
  const filterFlagids = useAppSelector((state) => state.filter.filterFlagids);
  const includeTags = useAppSelector((state) => state.filter.includeTags);
  const excludeTags = useAppSelector((state) => state.filter.excludeTags);
  const tagIntersectionMode = useAppSelector((state) => state.filter.tagIntersectionMode);

  const dispatch = useAppDispatch();

  const [starFlow] = useStarFlowMutation();

  const [flowIndex, setFlowIndex] = useState<number>(0);

  const virtuoso = useRef<VirtuosoHandle>(null);

  const service_name = searchParams.get(SERVICE_FILTER_KEY) ?? "";
  const service = services?.find((s) => s.name == service_name);

  const text_filter = searchParams.get(TEXT_FILTER_KEY) ?? undefined;
  const from_filter = searchParams.get(START_FILTER_KEY) ?? undefined;
  const to_filter = searchParams.get(END_FILTER_KEY) ?? undefined;

  const debounced_text_filter = useDebounce(text_filter, 300);

  const {
    data: flowData, error: flowQueryError,
    isLoading, isFetching, refetch,
    startedTimeStamp, fulfilledTimeStamp,
  } = useGetFlowsQuery(
    {
      regex_insensitive: debounced_text_filter,
      ip_dst: service?.ip,
      port_dst: service?.port,
      time_from: from_filter ? new Date(parseInt(from_filter)).toISOString() : undefined,
      time_to: to_filter ? new Date(parseInt(to_filter)).toISOString() : undefined,
      tags_include: includeTags,
      tags_exclude: excludeTags,
      tag_intersection_mode: tagIntersectionMode,
      flags: filterFlags,
      flagids: filterFlagids,
    },
    {
      refetchOnMountOrArgChange: true,
      pollingInterval: FLOW_LIST_REFETCH_INTERVAL_MS,
    }
  );

  interface FlowQueryError { error: string }
  const isFetchBaseQueryError = (error: unknown): error is FetchBaseQueryError =>
    typeof error === 'object' && error != null && 'status' in error
  const isFlowQueryError = (error: unknown): error is FlowQueryError =>
    typeof error === 'object' && error != null && 'error' in error
  const flowQueryErrorMessage = isFetchBaseQueryError(flowQueryError)
    && isFlowQueryError(flowQueryError.data)
    ? flowQueryError.data.error : null;

  let searchMessage = null;
  if(isFetching)
    searchMessage = "Searching...";
  else if(flowQueryErrorMessage)
    searchMessage = `Error: ${flowQueryErrorMessage}`;
  else if(startedTimeStamp && fulfilledTimeStamp)
    searchMessage = `Search took ${fulfilledTimeStamp - startedTimeStamp}ms`

  // TODO: fix the below transformation - move it to server
  // Diederik gives you a beer once it has been fixed
  const transformedFlowData = flowData?.map((flow) => ({
    ...flow,
    service_tag:
      services?.find((s) => s.ip === flow.dst_ip && s.port === flow.dst_port)
        ?.name ?? "unknown",
  }));

  const onHeartHandler = async (flow: Flow) => {
    await starFlow({ id: flow.id, star: !flow.tags.includes("starred") });
    if(FORCE_REFETCH_ON_STAR) refetch();
  };

  const navigate = useNavigate();

  useEffect(() => {
      virtuoso?.current?.scrollIntoView({
        index: flowIndex,
        behavior: 'auto',
        done: () => {
          if (transformedFlowData && transformedFlowData[flowIndex ?? 0]) {
            let idAtIndex = transformedFlowData[flowIndex ?? 0].id;
            // if the current flow ID at the index indeed did change (ie because of keyboard navigation), we need to update the URL as well as local ID
            if (idAtIndex !== openedFlowID) {
              navigate(`/flow/${idAtIndex}?${searchParams}`)
              openedFlowID = idAtIndex
            }
          }
        },
      })
    },
    [flowIndex]
  )

  // TODO: there must be a better way to do this
  // this gets called on every refetch, we dont want to iterate all flows on every refetch
  // so because performance, we hack this by checking if the transformedFlowData length changed
  const [transformedFlowDataLength, setTransformedFlowDataLength] = useState<number>(0);
  useEffect(
    () => {
      if (transformedFlowData && transformedFlowDataLength != transformedFlowData?.length) {
        setTransformedFlowDataLength(transformedFlowData?.length)

        for (let i = 0; i < transformedFlowData?.length; i++) {
          if (transformedFlowData[i].id === openedFlowID) {
            if (i !== flowIndex) {
              setFlowIndex(i)
            }
            return
          }
        }
        setFlowIndex(0)
      }
    },
    [transformedFlowData]
  )

  useHotkeys('x', async () => {
    if(transformedFlowData) {
      let flow = transformedFlowData[flowIndex ?? 0]
      await onHeartHandler(flow);
    }
  })

  useHotkeys('j', () => setFlowIndex(fi => Math.min((transformedFlowData?.length ?? 1)-1, fi + 1)), [transformedFlowData?.length]);
  useHotkeys('w', () => {
    if(transformedFlowData) {
      let idAtIndex = transformedFlowData[flowIndex ?? 0].id;
      if (idAtIndex != openedFlowID) {
        let flowids = flowData?.map((flow, idx) => ([flow.id, idx]))
        if (flowids) {
          let found = flowids.filter((el)=>(el[0] == openedFlowID))
          if (found.length > 0) {
            let n = Number(found[0][1])
            setFlowIndex(n)
          }
        }
      }
    }
  }
  );
  useHotkeys('k', () => setFlowIndex(fi => Math.max(0, fi - 1)));
  useHotkeys('i', () => {
    setShowFilters(true)
    if ((availableTags ?? []).includes("flag-in")) {
      dispatch(toggleFilterTag("flag-in"))
    }
  }, [availableTags]);
  useHotkeys('o', () => {
    setShowFilters(true)
    if ((availableTags ?? []).includes("flag-out")) {
      dispatch(toggleFilterTag("flag-out"))
    }
  }, [availableTags]);
  useHotkeys('t', () => {
    setShowFilters(true)
    if ((availableTags ?? []).includes("starred")) {
      dispatch(toggleFilterTag("starred"))
    }
  }, [availableTags]);
  useHotkeys('r', () => refetch());

  const [showFilters, setShowFilters] = useState(false);

  return (
    <div className="flex flex-col h-full">
      <div className="bg-white border-b-gray-300 border-b shadow-md flex flex-col">
        <div className="p-2 flex" style={{ height: 50 }}>
          <button
            className="flex gap-1 items-center text-sm"
            onClick={() => setShowFilters(!showFilters)}
          >
            {<FilterIcon height={20} className="text-gray-400"></FilterIcon>}
            {showFilters ? "Close" : "Open"} filters
          </button>
          {/* Maybe we want to use a search button instead of live search */}
          {false && (
            <button className="ml-auto items-center bg-blue-600 text-white px-2 rounded-md text-sm">
              Search
            </button>
          )}
        </div>
        {showFilters && (
          <div className="border-t-gray-300 border-t p-2">
            <div className="flex">
              <p className="text-sm font-bold text-gray-600 pb-2">
                Intersection filter
              </p>
              <button
                className="w-24 h-5 bg-blue-100 text-sm rounded-md ml-auto"
                onClick={() => dispatch(toggleTagIntersectMode())}
              >
                Mode:&nbsp;{tagIntersectionMode}
              </button>
            </div>
            <div className="flex gap-2 flex-wrap">
              {(availableTags ?? []).map((tag) => (
                <Tag
                  key={tag}
                  tag={tag}
                  disabled={!includeTags.includes(tag)}
                  excluded={excludeTags.includes(tag)}
                  onClick={() => dispatch(toggleFilterTag(tag))}
                ></Tag>
              ))}
            </div>
          </div>
        )}
      </div>
      <div></div>
      { searchMessage && <div>{searchMessage}</div> }
      <Virtuoso
        className={classNames({
          "flex-1": true,
          [classes.list_container]: true,
          "sidebar-loading": isLoading,
        })}
        data={transformedFlowData}
        ref={virtuoso}
        initialTopMostItemIndex={flowIndex}
        itemContent={(index, flow) => (
          <Link
            to={`/flow/${flow.id}?${searchParams}`}
            onClick={() => setFlowIndex(index)}
            key={flow.id}
            className="focus-visible:rounded-md"
            //style={{ paddingTop: '1em' }}
          >
            <FlowListEntry
              key={flow.id}
              flow={flow}
              isActive={flow.id === openedFlowID}
              onHeartClick={onHeartHandler}
            />
          </Link>
        )}
      />
    </div>
  );
}

interface FlowListEntryProps {
  flow: Flow;
  isActive: boolean;
  onHeartClick: (flow: Flow) => void;
}

function FlowListEntry({ flow, isActive, onHeartClick }: FlowListEntryProps) {
  const formatted_time_h_m_s = format(new Date(flow.time), "HH:mm:ss");
  const formatted_time_ms = format(new Date(flow.time), ".SSS");

  const [isStarred, setStarred] = useState(flow.tags.includes("starred"));

  // Filter tag list for tags that are handled specially
  const filtered_tag_list = flow.tags.filter((t) => t != "starred");

  const duration =
    flow.duration > 10000 ? (
      <div className="text-red-500">&gt;10s</div>
    ) : (
      <div>{flow.duration}ms</div>
    );
  return (
    <li
      className={classNames({
        [classes.active]: isActive,
      })}
    >
      <div className="flex">
        <div
          className="w-5 ml-1 mr-1 self-center shrink-0"
          onClick={() => {
            setStarred(!isStarred);
            onHeartClick(flow);
          }}
        >
          {isStarred ? (
            <HeartIcon className="text-red-500" />
          ) : (
            <EmptyHeartIcon />
          )}
        </div>

        <div className="w-5 mr-2 self-center shrink-0">
          {flow.child_id != null || flow.parent_id != null ? (
            <LinkIcon className="text-blue-500" />
          ) : undefined}
        </div>
        <div className="flex-1 shrink">
          <div className="flex">
            <div className="shrink-0">
              <span className="text-gray-700 font-bold overflow-ellipsis overflow-hidden ">
                {flow.service_tag}
              </span>
              <span className="text-gray-500">:{flow.dst_port}</span>
            </div>

            <div className="ml-2">
              <span className="text-gray-500">{formatted_time_h_m_s}</span>
              <span className="text-gray-300">{formatted_time_ms}</span>
            </div>
            <div className="text-gray-500 ml-auto">{duration}</div>
          </div>
          <div className="flex gap-2 flex-wrap">
            {filtered_tag_list.map((tag) => (
              <Tag key={tag} tag={tag}></Tag>
            ))}
          </div>
        </div>
      </div>
    </li>
  );
}

export { FlowListEntry };
```

## File: `frontend/src/components/Header.tsx`
```tsx
import { format, parse } from "date-fns";
import { Suspense, useState } from "react";
import { useHotkeys } from 'react-hotkeys-hook';
import {
  Link,
  useParams,
  useSearchParams,
  useNavigate,
} from "react-router-dom";
import ReactDiffViewer from "react-diff-viewer";

import {
  END_FILTER_KEY,
  SERVICE_FILTER_KEY,
  START_FILTER_KEY,
  TEXT_FILTER_KEY,
  FIRST_DIFF_KEY,
  SECOND_DIFF_KEY,
  SERVICE_REFETCH_INTERVAL_MS,
  REPR_ID_KEY,
} from "../const";
import {
  useGetFlowQuery,
  useGetServicesQuery,
} from "../api";
import { getTickStuff } from "../tick";

function ServiceSelection() {
  const FILTER_KEY = SERVICE_FILTER_KEY;

  // TODO add all, maybe user react-select

  const { data: services } = useGetServicesQuery(undefined, {
    pollingInterval: SERVICE_REFETCH_INTERVAL_MS,
  });

  const service_select = [
    {
      ip: "",
      port: 0,
      name: "all",
    },
    ...(services || []),
  ];
  let [searchParams, setSearchParams] = useSearchParams();
  return (
    <select
      value={searchParams.get(FILTER_KEY) ?? ""}
      onChange={(event) => {
        let serviceFilter = event.target.value;
        if (serviceFilter && serviceFilter != "all") {
          searchParams.set(FILTER_KEY, serviceFilter);
        } else {
          searchParams.delete(FILTER_KEY);
        }
        setSearchParams(searchParams);
      }}
    >
      {service_select.map((service) => (
        <option key={service.name} value={service.name}>
          {service.name}
        </option>
      ))}
    </select>
  );
}

function TextSearch() {
  const FILTER_KEY = TEXT_FILTER_KEY;
  let [searchParams, setSearchParams] = useSearchParams();
  useHotkeys('s', (e) => {
    let el = document.getElementById('search') as HTMLInputElement;
    el?.focus();
    el?.select();
    e.preventDefault()
  });
  return (
    <div>
      <input
        type="text"
        placeholder="regex"
        id="search"
        value={searchParams.get(FILTER_KEY) || ""}
        onChange={(event) => {
          let textFilter = event.target.value;
          if (textFilter) {
            searchParams.set(FILTER_KEY, textFilter);
          } else {
            searchParams.delete(FILTER_KEY);
          }
          setSearchParams(searchParams);
        }}
      ></input>
    </div>
  );
}


function StartDateSelection() {
  let { startTickParam, setTimeParam } = getTickStuff();
  return (
    <div>
      <input
        className="w-20"
        id="startdateselection"
        type="number"
        placeholder="from"
        value={startTickParam}
        onChange={(event) => {
          setTimeParam(event.target.value == "" ? null : parseInt(event.target.value), START_FILTER_KEY);
        }}
      ></input>
    </div>
  );
}

function EndDateSelection() {
  let { endTickParam, setTimeParam } = getTickStuff();
  return (
    <div>
      <input
        className="w-20"
        id="enddateselection"
        type="number"
        placeholder="to"
        value={endTickParam}
        onChange={(event) => {
          setTimeParam(event.target.value == "" ? null : parseInt(event.target.value), END_FILTER_KEY);
        }}
      ></input>
    </div>
  );
}

function FirstDiff() {
  let params = useParams();
  let [searchParams, setSearchParams] = useSearchParams();
  const [firstFlow, setFirstFlow] = useState<string>(
    searchParams.get(FIRST_DIFF_KEY) ?? ""
  );

  function setFirstDiffFlow() {
    let textFilter = params.id;
    let reprId = searchParams.get(REPR_ID_KEY);
    let reprIdSlug = reprId ? `${textFilter}:${reprId}` : `${textFilter}`
    if (textFilter) {
      searchParams.set(FIRST_DIFF_KEY, reprIdSlug);
      setFirstFlow(reprIdSlug);
    } else {
      searchParams.delete(FIRST_DIFF_KEY);
      setFirstFlow("");
    }
    setSearchParams(searchParams);
  }

  useHotkeys("f", () => {
    setFirstDiffFlow();
  });

  return (
    <input
      type="text"
      className="md:w-72"
      placeholder="First Diff ID"
      readOnly
      value={firstFlow}
      onClick={(event) => setFirstDiffFlow()}
      onContextMenu={(event) => {
        searchParams.delete(FIRST_DIFF_KEY);
        setFirstFlow("");
        setSearchParams(searchParams);
        event.preventDefault();
      }}
    ></input>
  );
}

function SecondDiff() {
  let params = useParams();
  let [searchParams, setSearchParams] = useSearchParams();
  const [secondFlow, setSecondFlow] = useState<string>(
    searchParams.get(SECOND_DIFF_KEY) ?? ""
  );

  function setSecondDiffFlow() {
    let textFilter = params.id;
    let reprId = searchParams.get(REPR_ID_KEY);
    let reprIdSlug = reprId ? `${textFilter}:${reprId}` : `${textFilter}`
    if (textFilter) {
      searchParams.set(SECOND_DIFF_KEY, reprIdSlug);
      setSecondFlow(reprIdSlug);
    } else {
      searchParams.delete(SECOND_DIFF_KEY);
      setSecondFlow("");
    }
    setSearchParams(searchParams);
  }

  useHotkeys("e", () => {
    setSecondDiffFlow();
  });

  return (
    <input
      type="text"
      className="md:w-72"
      placeholder="Second Flow ID"
      readOnly
      value={secondFlow}
      onClick={(event) => setSecondDiffFlow()}
      onContextMenu={(event) => {
        searchParams.delete(SECOND_DIFF_KEY);
        setSecondFlow("");
        setSearchParams(searchParams);
        event.preventDefault();
      }}
    ></input>
  );
}

function Diff() {
  let params = useParams();

  let [searchParams] = useSearchParams();

  let navigate = useNavigate();

  function navigateToDiff() {
    navigate(`/diff/${params.id ?? ""}?${searchParams}`, { replace: true });
  }

  useHotkeys("d", () => {
    navigateToDiff();
  });

  return (
    <button
      className=" bg-amber-100 text-gray-800 rounded-md px-2 py-1"
      onClick={() => {
        navigateToDiff()
      }}
    >
      Diff
    </button>
  );
}

export function Header() {
  let { currentTick, setToLastnTicks, setTimeParam } = getTickStuff();
  let [searchParams] = useSearchParams();

  let navigate = useNavigate();

  useHotkeys('g', () => navigate(`/corrie?${searchParams}`, { replace: true }))
  useHotkeys('a', () => setToLastnTicks(5));
  useHotkeys('c', () => {
    (document.getElementById("startdateselection") as HTMLInputElement).value = "";
    (document.getElementById("enddateselection") as HTMLInputElement).value = "";
    setTimeParam(null, START_FILTER_KEY);
    setTimeParam(null, END_FILTER_KEY);
  });

  return (
    <>
      <Link to={`/?${searchParams}`}>
        <div className="header-icon">🌷</div>
      </Link>
      <div>
        <TextSearch></TextSearch>
      </div>
      <div>
        <Suspense>
          <ServiceSelection></ServiceSelection>
        </Suspense>
      </div>
      <div>
        <StartDateSelection></StartDateSelection>
      </div>
      <div>
        <EndDateSelection></EndDateSelection>
      </div>
      <div>
        <button
          className=" bg-amber-100 text-gray-800 rounded-md px-2 py-1"
          onClick={() => setToLastnTicks(5)}
        >
          Last 5 ticks
        </button>
      </div>
      <Link to={`/corrie?${searchParams}`}>
        <div className="bg-blue-100 text-gray-800 rounded-md px-2 py-1">
          Graph view
        </div>
      </Link>
      <div className="ml-auto mr-4" style={{ display: "flex" }}>
        <div className="mr-4">
          <FirstDiff />
        </div>
        <div className="mr-4">
          <SecondDiff />
        </div>
        <div className="mr-6">
          <Suspense>
            <Diff />
          </Suspense>
        </div>
        <div
          className="ml-auto"
          style={{
            display: "flex",
            justifyContent: "center",
            alignContent: "center",
            flexDirection: "column",
          }}
        >
          Current: {currentTick}
        </div>
      </div>
    </>
  );
}
```

## File: `frontend/src/components/RadioGroup.tsx`
```tsx
import classNames from "classnames";

export interface RadioGroupProps {
  options: string[];
  value: string;
  className: string;
  onChange: (option: string) => void;
}

export function RadioGroup(props: RadioGroupProps) {
  return (
    <div className={props.className}>
      {props.options.map((option) => (
        <div
          key={option}
          onClick={() => props.onChange(option)}
          className={classNames("py-1 px-2 rounded-md cursor-pointer", {
            "bg-gray-200": option === props.value,
          })}
        >
          {option}
        </div>
      ))}
    </div>
  );
}
```

## File: `frontend/src/components/Tag.tsx`
```tsx
import classNames from "classnames";
import Color from "color";

const computeColorFromString = (str: string) => {
  const hue = Array.from(str).reduce(
    (hash, char) => 0 | (31 * hash + char.charCodeAt(0)),
    0
  );
  return Color(`hsl(${hue}, 100%, 50%)`).hex();
};

// Hardcode colors here
const tagColorMap: Record<string, string> = {
  fishy: "rgb(191, 219, 254)",
  blocked: "rgb(233, 213, 255)",
  flag_out: "rgb(254, 204, 204)",
  flag_in: "rgb(209, 213, 219)",
};

export function tagToColor(tag: string) {
  return tagColorMap[tag] ?? computeColorFromString(tag);
}
interface TagProps {
  tag: string;
  color?: string;
  disabled?: boolean;
  excluded?: boolean;
  onClick?: () => void;
}
export const Tag = ({ tag, color, disabled = false, excluded = false, onClick }: TagProps) => {
  var tagBackgroundColor = disabled ? "#eee" : color ?? tagToColor(tag);

  var tagTextColor = disabled
    ? "#bbb"
    : Color(tagBackgroundColor).isDark()
      ? "#fff"
      : "#000";


  if (excluded) {
    tagTextColor = "white";
    tagBackgroundColor = "black";
  }
  return (
    <div
      onClick={onClick}
      className={classNames("p-3 cursor-pointer rounded-md uppercase text-xs h-5 text-center flex items-center hover:opacity-90 transition-colors duration-250 text-ellipsis overflow-hidden whitespace-nowrap", {
        "bg-gray-300": disabled,
      })}
      style={{
        backgroundColor: tagBackgroundColor,
        color: tagTextColor,
      }}
    >
      <span  style={excluded ? { textDecoration: 'line-through' } : {}}>{tag}</span>
    </div>
  );
};
```

## File: `frontend/src/hooks/useCopy.ts`
```typescript
import { useState, useCallback } from "react";

//https://stackoverflow.com/questions/51805395/navigator-clipboard-is-undefined
function copyToClipboard(textToCopy: string) {
    // navigator clipboard api needs a secure context (https)
    if (navigator.clipboard && window.isSecureContext) {
        // navigator clipboard api method'
        return navigator.clipboard.writeText(textToCopy);
    } else {
        // text area method
        let textArea = document.createElement("textarea");
        textArea.value = textToCopy;
        // make the textarea out of viewport
        textArea.style.position = "fixed";
        textArea.style.left = "-999999px";
        textArea.style.top = "-999999px";
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        return new Promise<void>((res, rej) => {
            // here the magic happens
            document.execCommand("copy") ? res() : rej();
            textArea.remove();
        });
    }
}

type CopyState = "failed" | "copied" | "copying" | "default";

const defaultCopyStateToText: Record<CopyState, string> = {
    copied: "Copied",
    default: "Copy",
    failed: "Copy failed",
    copying: "Copying",
};

interface useCopyParams {
    copyStateToText?: Record<CopyState, string>;
    getText: () => Promise<string>;
}

export function useCopy(params: useCopyParams) {
    const [copyState, setCopyState] = useState<CopyState>("default");

    const copyStateToText = params.copyStateToText ?? defaultCopyStateToText;

    const copy = useCallback(async () => {
        setCopyState("copying");
        const textToCopy = await params.getText();
        copyToClipboard(textToCopy)
            .then(() => {
                setCopyState("copied");
                setTimeout(() => setCopyState("default"), 2000);
            })
            .catch(() => setCopyState("failed"));
    }, [params.getText, setCopyState]);

    return {
        copyState,
        copy,
        statusText: copyStateToText[copyState],
    };
}
```

## File: `frontend/src/hooks/useDebounce.ts`
```typescript
// https://usehooks-ts.com/react-hook/use-debounce

import { useEffect, useState } from 'react'

function useDebounce<T>(value: T, delay?: number): T {
    const [debouncedValue, setDebouncedValue] = useState<T>(value)

    useEffect(() => {
        const timer = setTimeout(() => setDebouncedValue(value), delay || 500)

        return () => {
            clearTimeout(timer)
        }
    }, [value, delay])

    return debouncedValue
}

export default useDebounce
```

## File: `frontend/src/pages/DiffView.tsx`
```tsx
import { useSearchParams, Link, useParams } from "react-router-dom";
import { useState } from "react";
import { Buffer } from "buffer";

import { FullFlow } from "../types";

import ReactDiffViewer from "react-diff-viewer";
import { RadioGroup } from "../components/RadioGroup";

import { hexy } from "hexy";

import { FIRST_DIFF_KEY, SECOND_DIFF_KEY } from "../const";
import { useGetFlowQuery } from "../api";

function Flow(flow1: string, flow2: string) {
  return (
    <div>
      <ReactDiffViewer
        oldValue={flow1}
        newValue={flow2}
        splitView={true}
        showDiffOnly={false}
        useDarkTheme={false}
        hideLineNumbers={true}
        styles={{
          line: {
            wordBreak: "break-word",
          },
        }}
      />
      <hr
        style={{
          height: "1px",
          color: "inherit",
          borderTopWidth: "5px",
        }}
      />
    </div>
  );
}

function isASCII(str: string) {
  return /^[\x00-\x7F]*$/.test(str);
}

const displayOptions = ["Plain", "Hex"];

// Derives the display mode for two given flows
const deriveDisplayMode = (
  firstFlow: FullFlow,
  secondFlow: FullFlow
): typeof displayOptions[number] => {
  if (firstFlow && secondFlow) {
    for (
      let i = 0;
      i < Math.min(firstFlow.flow.length, secondFlow.flow.length);
      i++
    ) {
      if (
        !isASCII(firstFlow.flow[0].flow[i].data) ||
        !isASCII(secondFlow.flow[0].flow[i].data)
      ) {
        return displayOptions[1];
      }
    }
  }

  return displayOptions[0];
};

export function DiffView() {
  let [searchParams] = useSearchParams();
  const firstFlowParam = searchParams.get(FIRST_DIFF_KEY);
  const firstFlowId = firstFlowParam?.split(":")[0];
  const firstFlowRepr = parseInt(firstFlowParam?.split(":")[1] ?? "0");
  const secondFlowParam = searchParams.get(SECOND_DIFF_KEY);
  const secondFlowId = secondFlowParam?.split(":")[0];
  const secondFlowRepr = parseInt(secondFlowParam?.split(":")[1] ?? "0");

  let { data: firstFlow, isLoading: firstFlowLoading, isError: firstFlowError } = useGetFlowQuery(
    firstFlowId!,
    {
      skip: firstFlowId === null,
    }
  );
  let { data: secondFlow, isLoading: secondFlowLoading, isError: secondFlowError } = useGetFlowQuery(
    secondFlowId!,
    {
      skip: secondFlowId === null,
    }
  );

  const [displayOption, setDisplayOption] = useState(
    deriveDisplayMode(firstFlow!, secondFlow!)
  );

  if (firstFlowError || secondFlowError) {
    return <div>Invalid flow id</div>;
  }

  if (firstFlowLoading || secondFlowLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <div className="sticky shadow-md bg-white overflow-auto py-1 border-y flex items-center">
        <RadioGroup
          options={displayOptions}
          value={displayOption}
          onChange={setDisplayOption}
          className="flex gap-2 text-gray-800 text-sm mr-4"
        />
      </div>

      {/* Plain */}
      {displayOption === displayOptions[0] && (
        <div>
          {Array.from(
            {
              length: Math.min(firstFlow!.flow[firstFlowRepr].flow.length, secondFlow!.flow[secondFlowRepr].flow.length),
            },
            (_, i) => Flow(firstFlow!.flow[firstFlowRepr].flow[i].data, secondFlow!.flow[secondFlowRepr].flow[i].data)
          )}
        </div>
      )}

      {/* Hex */}
      {displayOption === displayOptions[1] && (
        <div>
          {Array.from(
            {
              length: Math.min(firstFlow!.flow[firstFlowRepr].flow.length, secondFlow!.flow[secondFlowRepr].flow.length),
            },
            (_, i) =>
              Flow(
                hexy(Buffer.from(firstFlow!.flow[firstFlowRepr].flow[i].b64, 'base64'), { format: "twos" }),
                hexy(Buffer.from(secondFlow!.flow[secondFlowRepr].flow[i].b64, 'base64'), { format: "twos" })
              )
          )}
        </div>
      )}
    </div>
  );
}
```

## File: `frontend/src/pages/FlowView.tsx`
```tsx
import { useSearchParams, Link, useParams, useNavigate } from "react-router-dom";
import React, { ChangeEvent, useDeferredValue, useEffect, useState } from "react";
import { useHotkeys } from "react-hotkeys-hook";
import { FlowData, FullFlow } from "../types";
import { Buffer } from "buffer";
import {
  TEXT_FILTER_KEY,
  MAX_LENGTH_FOR_HIGHLIGHT,
  API_BASE_PATH,
  REPR_ID_KEY,
  FIRST_DIFF_KEY,
  SECOND_DIFF_KEY,
} from "../const";
import {
  ArrowCircleLeftIcon,
  ArrowCircleRightIcon,
  ArrowCircleUpIcon,
  ArrowCircleDownIcon,
  DownloadIcon,
  LightningBoltIcon,
} from "@heroicons/react/solid";
import { format } from "date-fns";

import { hexy } from "hexy";
import { useCopy } from "../hooks/useCopy";
import { RadioGroup } from "../components/RadioGroup";
import {
  useGetFlowQuery,
  useGetServicesQuery,
  useLazyToFullPythonRequestQuery,
  useLazyToPwnToolsQuery,
  useToSinglePythonRequestQuery,
  useGetFlagRegexQuery,
} from "../api";
import { getTickStuff } from "../tick";
import escapeStringRegexp from "escape-string-regexp";

const SECONDARY_NAVBAR_HEIGHT = 50;

function CopyButton({ copyText }: { copyText?: string }) {
  const { statusText, copy, copyState } = useCopy({
    getText: async () => copyText ?? "",
  });
  return (
    <>
      {copyText && (
        <button
          className="p-2 text-sm text-blue-500"
          onClick={copy}
          disabled={!copyText}
        >
          {statusText}
        </button>
      )}
    </>
  );
}

function FlowContainer({
  copyText,
  children,
}: {
  copyText?: string;
  children: React.ReactNode;
}) {
  return (
    <div className=" pb-5 flex flex-col">
      <div className="ml-auto">
        <CopyButton copyText={copyText}></CopyButton>
      </div>
      <pre className="p-5 overflow-auto">{children}</pre>
    </div>
  );
}

function HexFlow({ flow }: { flow: FlowData }) {
  const hex = hexy(Buffer.from(flow.b64, "base64"), { format: "twos" });
  return <FlowContainer copyText={hex}>{hex}</FlowContainer>;
}
function highlightText(flowText: string, search_string: string, flag_string: string) {
  if (flowText.length > MAX_LENGTH_FOR_HIGHLIGHT || (flag_string === "" && search_string === "")) {
    return flowText
  }
  try {
    const searchClasses = "bg-orange-200 rounded-sm";
    const flagClasses = "bg-red-200 rounded-sm";

    // Matches are stored as `[start index, end index]`.
    // For some reason tsc compiler (during build) thinks that `x.index` can be undefined (no, it can't).
    // I wasn't able to find a workaround for it so @ts-ignore it is...
    // Other way would be `x.index ?? 0` but that seems like it is doing something more than fixing typescript issues.
    // @ts-ignore
    const flagMatches: [number, number][] = (
      flag_string === ""
        ? []
        // @ts-ignore
        : [...flowText.matchAll(new RegExp(flag_string, "g"))].map(x => [x.index, x.index + x[0].length])
    );
    // @ts-ignore
    const searchMatches: [number, number][] = (
      search_string === ""
        ? []
        // @ts-ignore
        : [...flowText.matchAll(new RegExp(search_string, "gi"))].map(x => [x.index, x.index + x[0].length])
    );

    let parts = [];
    let currentIndex = 0, flagMatchIndex = 0, searchMatchIndex = 0;
    while (true) {
      // Pick next match
      let isSearchMatch = null;
      if (flagMatchIndex < flagMatches.length && searchMatchIndex < searchMatches.length) {
        isSearchMatch = searchMatches[searchMatchIndex][0] <= flagMatches[flagMatchIndex][0];
      } else if (searchMatchIndex < searchMatches.length) {
        isSearchMatch = true;
      } else if (flagMatchIndex < flagMatches.length) {
        isSearchMatch = false;
      }
      let match = (
        isSearchMatch === null
          ? null
          : isSearchMatch ? searchMatches[searchMatchIndex] : flagMatches[flagMatchIndex]
      );

      // Produce element for remaining text if there is no match
      if (match === null) {
        parts.push(<span key={currentIndex}>{flowText.slice(currentIndex)}</span>);
        break;
      }

      // Produce element for part between previous and next/current match
      if (currentIndex != match[0]) {
        parts.push(<span key={currentIndex}>{flowText.slice(currentIndex, match[0])}</span>);
      }

      // Produce element for current match
      parts.push(<span key={match[0]} className={isSearchMatch ? searchClasses : flagClasses}>{flowText.slice(match[0], match[1])}</span>);

      // Advance position to end of match
      currentIndex = match[1];

      // Advance "pointers" for flag matches
      while (flagMatchIndex < flagMatches.length && flagMatches[flagMatchIndex][1] <= currentIndex) flagMatchIndex++;
      // If current match ends in the middle of next match, we cut that overlaping part out
      if (flagMatchIndex < flagMatches.length && flagMatches[flagMatchIndex][0] < currentIndex) flagMatches[flagMatchIndex][0] = currentIndex;
      // Do the same also for search matches
      while (searchMatchIndex < searchMatches.length && searchMatches[searchMatchIndex][1] <= currentIndex) searchMatchIndex++;
      if (searchMatchIndex < searchMatches.length && searchMatches[searchMatchIndex][0] < currentIndex) searchMatches[searchMatchIndex][0] = currentIndex;
    }

    return <span>{parts}</span>;
  } catch (error) {
    console.log(error);
    return flowText;
  }
}

function TextFlow({ flow }: { flow: FlowData }) {
  let [searchParams] = useSearchParams();
  const text_filter = searchParams.get(TEXT_FILTER_KEY);
  const { data: flag_regex } = useGetFlagRegexQuery();
  const text = highlightText(flow.data, text_filter ?? "", flag_regex ?? "");

  return <FlowContainer copyText={flow.data}>{text}</FlowContainer>;
}

function WebFlow({ flow }: { flow: FlowData }) {
  const data = flow.data;
  const [header, ...rest] = data.split("\r\n\r\n");
  const http_content = rest.join("\r\n\r\n");

  const Hack = "iframe" as any;
  return (
    <FlowContainer>
      <pre>{header}</pre>
      <div className="border border-gray-200 rounded-lg">
        <Hack
          srcDoc={http_content}
          sandbox=""
          height={300}
          csp="default-src none" // there is a warning here but it actually works, not supported in firefox though :(
        ></Hack>
      </div>
    </FlowContainer>
  );
}

function PythonRequestFlow({
  full_flow,
  flow,
  item_index,
}: {
  full_flow: FullFlow;
  flow: FlowData;
  item_index: number,
}) {
  const { data } = useToSinglePythonRequestQuery({
    body: flow.b64,
    id: full_flow.id,
    item_index,
    tokenize: true,
  });

  return <FlowContainer copyText={data}>{data}</FlowContainer>;
}

interface FlowProps {
  full_flow: FullFlow;
  flow: FlowData;
  flow_item_index: number;
  delta_time: number;
  id: string;
}

function detectType(flow: FlowData) {
  const firstLine = flow.data.split("\n")[0];
  if (firstLine.includes("HTTP")) {
    return "Web";
  }

  return "Plain";
}

function getFlowBody(flow: FlowData, flowType: string) {
  if (flowType == "Web") {
    const contentType = flow.data.match(/Content-Type: ([^\s;]+)/im)?.[1];
    if (contentType) {
      const body = Buffer.from(flow.b64, "base64").subarray(flow.data.indexOf("\r\n\r\n") + 4);
      return [contentType, body]
    }
  }
  return null
}

function Flow({ full_flow, flow, flow_item_index, delta_time, id }: FlowProps) {
  const formatted_time = format(new Date(flow.time), "HH:mm:ss:SSS");
  const displayOptions = flow.from === "s"
    ? ["Plain", "Hex", "Web"]
    : ["Plain", "Hex", "PythonRequest"];

  // Basic type detection, currently unused
  const [displayOption, setDisplayOption] = useState("Plain");

  const flowType = detectType(flow);
  const flowBody = getFlowBody(flow, flowType);

  return (
    <div className="text-mono" id={id}>
      <div
        className="sticky shadow-md bg-white overflow-auto py-1 border-y"
        style={{ top: SECONDARY_NAVBAR_HEIGHT }}
      >
        <div className="flex items-center h-6">
          <div className="w-8 px-2">
            {flow.from === "s" ? (
              <ArrowCircleLeftIcon className="fill-green-700" />
            ) : (
              <ArrowCircleRightIcon className="fill-red-700" />
            )}
          </div>
          <div style={{ width: 200 }}>
            {formatted_time}
            <span className="text-gray-400 pl-3">{delta_time}ms</span>
          </div>
          <button
            className="bg-gray-200 py-1 px-2 rounded-md text-sm"
            onClick={async () => {
              window.open(
                "https://gchq.github.io/CyberChef/#input=" +
                encodeURIComponent(flow.b64)
              );
            }}
          >
            Open in CC
          </button>
          {flowType == "Web" && flowBody && (
            <button
              className="bg-gray-200 py-1 px-2 rounded-md text-sm ml-2"
              onClick={async () => {
                window.open(
                  "https://gchq.github.io/CyberChef/#input=" +
                  encodeURIComponent(flowBody[1].toString("base64"))
                );
              }}
            >
              Open body in CC
            </button>
          )}
          <button
            className="bg-gray-200 py-1 px-2 rounded-md text-sm ml-2"
            onClick={async () => {
              const blob = new Blob([Buffer.from(flow.b64, "base64")], {
                type: "application/octet-stream",
              });
              const url = window.URL.createObjectURL(blob);
              const a = document.createElement("a");
              a.style.display = "none";
              a.href = url;
              a.download = "tulip-dl-" + id + ".dat";
              document.body.appendChild(a);
              a.click();
              window.URL.revokeObjectURL(url);
              a.remove();
            }}
          >
            Download
          </button>
          {flowType == "Web" && flowBody && (
            <button
              className="bg-gray-200 py-1 px-2 rounded-md text-sm ml-2"
              onClick={async () => {
                const blob = new Blob([flowBody[1]], {
                  type: flowBody[0].toString(),
                });
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement("a");
                a.style.display = "none";
                a.href = url;
                a.download = "tulip-dl-" + id + ".dat";
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                a.remove();
              }}
            >
              Download body
            </button>
          )}
          <RadioGroup
            options={displayOptions}
            value={displayOption}
            onChange={setDisplayOption}
            className="flex gap-2 text-gray-800 text-sm mr-4 ml-auto"
          />
        </div>
      </div>
      <div
        className={
          flow.from === "s"
            ? "border-l-8 border-green-300"
            : "border-l-8 border-red-300"
        }
      >
        {displayOption === "Hex" && <HexFlow flow={flow}></HexFlow>}
        {displayOption === "Plain" && <TextFlow flow={flow}></TextFlow>}
        {displayOption === "Web" && <WebFlow flow={flow}></WebFlow>}
        {displayOption === "PythonRequest" && (
          <PythonRequestFlow
            flow={flow}
            full_flow={full_flow}
            item_index={flow_item_index}
          ></PythonRequestFlow>
        )}
      </div>
    </div>
  );
}

// Helper function to format the IP for display. If the IP contains ":",
// assume it is an ipv6 address and surround it in square brackets
function formatIP(ip: string) {
  return ip.includes(":") ? `[${ip}]` : ip;
}

function FlowOverview({ flow }: { flow: FullFlow }) {
  let [searchParams, setSearchParams] = useSearchParams();
  const { unixTimeToTick } = getTickStuff();
  const { data: services } = useGetServicesQuery();
  const service = services?.find((s) => s.ip === flow.dst_ip && s.port === flow.dst_port)?.name ?? "unknown";
  return (
    <div>
      {flow.signatures?.length > 0 ? (
        <div className="bg-blue-200 p-2">
          <div className="font-extrabold">Suricata</div>
          <div className="pl-2">
            {flow.signatures.map((sig) => {
              return (
                <div className="py-1">
                  <div className="flex">
                    <div>Message:&nbsp;</div>
                    <div className="font-bold">{sig.message}</div>
                  </div>
                  <div className="flex">
                    <div>Rule ID:&nbsp;</div>
                    <div className="font-bold">{sig.id}</div>
                  </div>
                  <div className="flex">
                    <div>Action taken:&nbsp;</div>
                    <div
                      className={
                        sig.action === "blocked"
                          ? "font-bold text-red-800"
                          : "font-bold text-green-800"
                      }
                    >
                      {sig.action}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      ) : undefined}
      <div className="bg-yellow-200 p-2">
        <div className="font-extrabold">Meta</div>
        <div className="pl-2">
          <div>
            Source:&nbsp;
            <a className="font-bold" href={`${API_BASE_PATH}/download/?file=${flow.filename}`}>
              {flow.filename}
              <DownloadIcon className="inline-flex items-baseline w-5 h-5" />
            </a>
          </div>
          <div>
            Tags:&nbsp;
            <span className="font-bold">[{flow.tags.join(", ")}]</span>
          </div>
          <div>
            Tick:&nbsp;
            <span className="font-bold">{unixTimeToTick(flow.time)}</span>
          </div>
          <div>
            Service:&nbsp;
            <span className="font-bold">{service}</span>
          </div>
          <div>
            Flags:&nbsp;
            <span className="font-bold">
              [{flow.flags.map((query, i) => (
                <span>
                  {i > 0 ? ", " : ""}
                  <button className="font-bold"
                    onClick={() => {
                      searchParams.set(TEXT_FILTER_KEY, escapeStringRegexp(query));
                      setSearchParams(searchParams);
                    }}
                  >
                    {query}
                  </button>
                </span>
              ))}]
            </span>
          </div>
          <div>
            Flagids:&nbsp;
            <span className="font-bold">
              [{flow.flagids.map((query, i) => (
                <span>
                  {i > 0 ? ", " : ""}
                  <button className="font-bold"
                    onClick={() => {
                      searchParams.set(TEXT_FILTER_KEY, escapeStringRegexp(query));
                      setSearchParams(searchParams);
                    }}
                  >
                    {query}
                  </button>
                </span>
              ))}]
            </span>
          </div>
          <div>
            Source - Target (Duration):&nbsp;
            <div className="inline-flex items-center gap-1">
              <div>
                <span>{formatIP(flow.src_ip)}</span>:
                <span className="font-bold">{flow.src_port}</span>
              </div>
              <span>-</span>
              <div>
                <span>{formatIP(flow.dst_ip)}</span>:
                <span className="font-bold">{flow.dst_port}</span>
              </div>
              <span className="italic">({flow.duration} ms)</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export function FlowView() {
  let [searchParams, setSearchParams] = useSearchParams();
  const params = useParams();
  const navigate = useNavigate();

  const id = params.id;

  const [reprId, setReprId] = useState(parseInt(searchParams.get(REPR_ID_KEY) ?? "0"));

  const { data: flow, isError, isLoading } = useGetFlowQuery(id!, { skip: id === undefined });

  const [triggerPwnToolsQuery] = useLazyToPwnToolsQuery();
  const [triggerFullPythonRequestQuery] = useLazyToFullPythonRequestQuery();

  async function copyAsPwn() {
    if (flow?.id) {
      const { data } = await triggerPwnToolsQuery(flow?.id);
      console.log(data);
      return data || "";
    }
    return "";
  }

  const { statusText: pwnCopyStatusText, copy: copyPwn } = useCopy({
    getText: copyAsPwn,
    copyStateToText: {
      copied: "Copied",
      default: "Copy as pwntools",
      failed: "Failed",
      copying: "Generating payload",
    },
  });

  async function copyAsRequests() {
    if (flow?.id) {
      const { data } = await triggerFullPythonRequestQuery(flow?.id);
      return data || "";
    }
    return "";
  }

  const { statusText: requestsCopyStatusText, copy: copyRequests } = useCopy({
    getText: copyAsRequests,
    copyStateToText: {
      copied: "Copied",
      default: "Copy as requests",
      failed: "Failed",
      copying: "Generating payload",
    },
  });

  // TODO: account for user scrolling - update currentFlow accordingly
  const [currentFlow, setCurrentFlow] = useState<number>(-1);

  // reset scroll on flow switch
  useHotkeys('j', () => setCurrentFlow(0))
  useHotkeys('k', () => setCurrentFlow(0))

  useHotkeys('h', () => {
    // we do this for the scroll to top
    if (currentFlow === 0) {
      // document.getElementById(`${id}-${currentFlow}`)?.scrollIntoView(true)
      let el = document.querySelector("main > div > div:nth-child(2)")
      if (el) el.scrollIntoView()
    }
    setCurrentFlow(fi => Math.max(0, fi - 1))
  }, [currentFlow]);
  useHotkeys('l', () => {
    // if (currentFlow === (flow?.flow?.length ?? 1)-1) {
    //   document.getElementById(`${id}-${currentFlow}`)?.scrollIntoView(true)
    // }
    setCurrentFlow(fi => Math.min((flow?.flow?.length ?? 1)-1, fi + 1))
  }, [currentFlow, flow?.flow?.length]);

  useEffect(
    () => {
      if (currentFlow < 0) {
        return
      }
      document.getElementById(`${id}-${currentFlow}`)?.scrollIntoView(true)
    },
    [currentFlow]
  )

  useHotkeys("m", () => {
    setReprId(ri => (ri + 1) % (flow?.flow.length ?? 1))
  }, [reprId, flow?.flow.length]);

  // when the reprId changes, we update the url
  useEffect(
    () => {
      if (reprId === 0) {
        searchParams.delete(REPR_ID_KEY)
        setSearchParams(searchParams)
        return
      }
      searchParams.set(REPR_ID_KEY, reprId.toString());
      setSearchParams(searchParams)
    },
    [reprId]
  )

  // if the flow doesn't have the representation we're looking for, we fallback to raw
  useEffect(
    () => {
      if (flow?.flow.length == undefined || flow?.flow.length === 0) {
        return
      }
      if ((flow?.flow.length - 1) < reprId) {
        setReprId(0)
      }
    },
    [flow?.flow.length]
  )

  if (isError) {
    return <div>Error while fetching flow</div>;
  }

  if (isLoading || flow == undefined) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <div
        className="sticky shadow-md top-0 bg-white overflow-auto border-b border-b-gray-200 flex"
        style={{ height: SECONDARY_NAVBAR_HEIGHT, zIndex: 100 }}
      >
        {(flow?.child_id != null || flow?.parent_id != null) ? (
          <div className="flex align-middle p-2 gap-3">
            <button
              className="bg-yellow-700 text-white px-2 text-sm rounded-md disabled:opacity-50"
              key={"parent" + flow.parent_id}
              disabled={flow?.parent_id === null}
              onMouseDown={(e) => {
                if (e.button === 1) { // handle opening in new tab
                  window.open(`/flow/${flow.parent_id}?${searchParams}`, "_blank")
                } else if (e.button === 0) {
                  navigate(`/flow/${flow.parent_id}?${searchParams}`)
                }
              }}
            >
              <ArrowCircleUpIcon className="inline-flex items-baseline w-5 h-5"></ArrowCircleUpIcon> Parent
            </button>
            <button
              className="bg-yellow-700 text-white px-2 text-sm rounded-md disabled:opacity-50"
              key={"child" + flow.child_id}
              disabled={flow?.child_id === null}
              onMouseDown={(e) => {
                if (e.button === 1) { // handle opening in new tab
                  window.open(`/flow/${flow.child_id}?${searchParams}`, "_blank")
                } else if (e.button === 0) {
                  navigate(`/flow/${flow.child_id}?${searchParams}`)
                }
              }}
            >
              <ArrowCircleDownIcon className="inline-flex items-baseline w-5 h-5"></ArrowCircleDownIcon> Child
            </button>
          </div>
        ) : undefined}
        <div className="flex align-middle p-2 gap-3 ml-auto">
          <p className="my-auto">Decoders <abbr title={"Number of decoders available for this flow: " + flow?.flow.length}>({flow?.flow.length})</abbr>:</p>
          <select
            id="repr-select"
            value={reprId}
            className="border-2 border-gray-700 text-black px-2 text-sm rounded-md"
            onChange={(e) => {
              const target = e.target as HTMLSelectElement;
              const newreprid = parseInt(target.value);
              setReprId(newreprid);
            }}
          >
            {flow?.flow.map((e, i) => <option key={id + "reprselect" + i} value={i}>{e["type"]}</option>)}
          </select>
          {reprId > 0 ? <button
            className="bg-gray-700 text-white px-2 text-sm rounded-md"
            title="Diff this representation with the base"
            onClick={(e) => {
              searchParams.set(FIRST_DIFF_KEY, `${id}`);
              searchParams.set(SECOND_DIFF_KEY, `${id}:${reprId}`);
              navigate(`/diff/${id ?? ""}?${searchParams}`, { replace: true });
            }}
          >
            <LightningBoltIcon className="h-5 w-5"></LightningBoltIcon>
          </button> : undefined}
          <button
            className="bg-gray-700 text-white px-2 text-sm rounded-md"
            onClick={copyPwn}
          >
            {pwnCopyStatusText}
          </button>

          <button
            className="bg-gray-700 text-white px-2 text-sm rounded-md"
            onClick={copyRequests}
          >
            {requestsCopyStatusText}
          </button>
        </div>
      </div>

      {flow ? <FlowOverview flow={flow}></FlowOverview> : undefined}
      {flow?.flow[(reprId < flow?.flow.length) ? reprId : 0].flow.map((flow_data, i, a) => {
        const delta_time = a[i].time - (a[i - 1]?.time ?? a[i].time);
        return (
          <Flow
            flow={flow_data}
            flow_item_index={i}
            delta_time={delta_time}
            full_flow={flow}
            key={flow.id + "-" + i}
            id={flow.id + "-" + i}
          ></Flow>
        );
      })}
    </div>
  );
}
```

## File: `frontend/src/pages/Home.tsx`
```tsx
const shortcutTableData = [
  [
    { key: 'j/k', action: 'Down/Up in FlowList' },
    { key: 'h/l', action: 'Up/Down in Flow' },
    { key: 's', action: 'Focus (s)earch bar' },
    { key: 'esc', action: 'Unfocus search bar' },
  ],
  [
    { key: 'a', action: 'L(a)st 5 ticks' },
    { key: 'c', action: '(C)lear time selection' },
    { key: 'r', action: '(R)efresh flows' },
  ],
  [
    { key: 'd', action: '(D)iff view' },
    { key: 'f', action: 'Load flow to (f)irst diff slot' },
    { key: 'e', action: 'Load flow to s(e)cond diff slot' },
    { key: 'g', action: '(G)raph view' },
  ],
  [
    { key: 'w', action: 'Scroll to current flo(w) in flow list' },
    { key: 'i/o', action: 'Toggle flag in/out filters' },
    { key: 't', action: 'Toggle s(t)arred filters' },
    { key: 'x', action: 'Star selected flow' },
  ]
];

const generateShortcutTable = (data: { key: string; action: string; }[][]) => {
  return (
        <div className="flex flex-row gap-4">
          {data.map((table, tableIndex) => (
            <table key={tableIndex} className="border-collapse border border-slate-500 table-auto">
              <thead>
                <tr>
                  <th className="border border-slate-600 px-4">Key</th>
                  <th className="border border-slate-600 px-4">Action</th>
                </tr>
              </thead>
              <tbody>
              {table.map((row, rowIndex) => (
                <tr key={rowIndex}>
                  {Object.entries(row).map((cell, cellIndex) => (
                    <td className="border border-slate-700 px-4" key={cellIndex}>
                      {cell[1]}
                    </td>
                  ))}
                </tr>
              ))}
              </tbody>
            </table>
          ))}
        </div>
  );
};


export function Home() {
  return (
    <div className="p-4 flex flex-col gap-4 justify-center items-center h-full opacity-40">
      <span className="text-9xl">🌷</span>
      <h1 className="text-5xl text-gray-600">Welcome to Tulip</h1>
      <h1 className="text-2xl text-gray-500">Shortcut reference:</h1>
      {generateShortcutTable(shortcutTableData)}
      {/* <h1 className="text-3xl font-bold pt-2 pb-4"></h1> */}
    </div>
  );
}
```

## File: `frontend/src/store/filter.ts`
```typescript
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

export interface TulipFilterState {
  filterFlags: string[];
  filterFlagids: string[];
  includeTags: string[];
  excludeTags: string[];
  tagIntersectionMode: "AND" | "OR";
  // startTick?: number;
  // endTick?: number;
  // service?: string;
  // textSearch?: string;
}

const initialState: TulipFilterState = {
  includeTags: [],
  excludeTags: [],
  filterFlags: [],
  filterFlagids: [],
  tagIntersectionMode: "OR",
};

export const filterSlice = createSlice({
  name: "filter",
  initialState,
  reducers: {
    // updateStartTick: (state, action: PayloadAction<number>) => {
    //   state.startTick = action.payload;
    // },
    // updateEndTick: (state, action: PayloadAction<number>) => {
    //   state.endTick = action.payload;
    // },
    toggleFilterTag: (state, action: PayloadAction<string>) => {
      var included = state.includeTags.includes(action.payload)
      var excluded = state.excludeTags.includes(action.payload)

      // If a user clicks a 'included' tag, the tag should be 'excluded' instead.
      if (included) {
        // Remove from included
        state.includeTags = state.includeTags.filter((t) => t !== action.payload);

        // Add to excluded
        state.excludeTags = [...state.excludeTags, action.payload]
      } else {
        // If the user clicks on an 'excluded' tag, the tag should be 'unset' from both include / exclude tags
        if (excluded) {
          // Remove from excluded
          state.excludeTags = state.excludeTags.filter((t) => t !== action.payload);
        } else {
          if (!included && !excluded) {
            // The tag was disabled, so it should be added to included now
            state.includeTags = [...state.includeTags, action.payload]
          }
        }
      }
    },
    toggleFilterFlags: (state, action: PayloadAction<string>) => {
      state.filterFlags = state.filterFlags.includes(action.payload)
          ? state.filterFlags.filter((t) => t !== action.payload)
          : [...state.filterFlags, action.payload];
    },
    toggleFilterFlagids: (state, action: PayloadAction<string>) => {
      state.filterFlagids = state.filterFlagids.includes(action.payload)
          ? state.filterFlagids.filter((t) => t !== action.payload)
          : [...state.filterFlagids, action.payload];
    },
    toggleTagIntersectMode: (state) => {
      state.tagIntersectionMode = state.tagIntersectionMode == "AND" ? "OR" : "AND";
    },
  },
});

export const { toggleFilterTag, toggleTagIntersectMode } = filterSlice.actions;

export default filterSlice.reducer;
```

## File: `frontend/src/store/index.ts`
```typescript
import { configureStore } from "@reduxjs/toolkit";
import { setupListeners } from "@reduxjs/toolkit/query";
import { useDispatch, useSelector } from "react-redux";
import type { TypedUseSelectorHook } from "react-redux";

import { tulipApi } from "../api";

import filterReducer from "./filter";

export const store = configureStore({
  reducer: {
    [tulipApi.reducerPath]: tulipApi.reducer,
    filter: filterReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(tulipApi.middleware),
});

setupListeners(store.dispatch);

// Use throughout your app instead of plain `useDispatch` and `useSelector`
export const useAppDispatch: () => typeof store.dispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<
  ReturnType<typeof store.getState>
> = useSelector;
```

## File: `frontend/types/twin.d.ts`
```typescript
import 'twin.macro'
import styledImport, { CSSProp, css as cssImport } from 'styled-components'

// Type hack for babel macro

declare module 'twin.macro' {
    // The styled and css imports
    const styled: typeof styledImport
    const css: typeof cssImport
}

declare module 'react' {
    // The css prop
    interface HTMLAttributes<T> extends DOMAttributes<T> {
        css?: CSSProp
        tw?: string
    }
    // The inline svg css prop
    interface SVGProps<T> extends SVGProps<SVGSVGElement> {
        css?: CSSProp
        tw?: string
    }
}

// The 'as' prop on styled components
declare global {
    namespace JSX {
        interface IntrinsicAttributes<T> extends DOMAttributes<T> {
            as?: string | Element
        }
    }
}
```

## File: `services/.gitignore`
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
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
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

workspace.xml
```

## File: `services/README.md`
```markdown
# Services



### General idea
We create pcap of N minutes on the virtual machine. We somehow download them, and use the `importer.py` script to analyze and import them into mongodb. The webapp does rest request to the webservices, that does query to mongodb.


### MongoDB structure
We use a single collection for all the pcaps
Each document will have:
```{
        "inx": //progressive flow index inside pcap
        "time": //start timestamp
        "duration": //end_time-start_time
        "src_ip": "127.0.0.1",
        "src_port": 1234 ,
        "dst_ip": "127.0.0.1",
        "dst_port": 1234,
        "contains_flag": //true if the importer have found that the flow contains a flag based on the env var regex
        "flow": [
            {
                "data": "...", // session data (capped at 15 MB)
                "from": "c" // "c" for client, "s" for server
                "time": //timestamp
            }, 
            ...
        ],

    }

```

# Services description
All the end-points return an object or an array of objects.

##### POST /query
Accept the following payload
```
    {
       flow.data: "regex on data field of flow",
       dst_ip: "1.2.3.4"
       dst_port: "1.2.3.4"
       time : {"$gte": from_millis,
               "$lt": to_millis}
    }

```
It returns an array of documents, WITHOUT the "flow" field

##### GET /services
Returns informations about all services. It is configurable on `configurations.py`

##### GET /flow/(flow_id)
Returns the all document with `flow_id` id, including the field `flow`

##### GET /star/(flow_id)/(0,1)
Set the flow favourite (1) or not (0)

##### POST /to_python_request/(tokenize)
convert the request to python syntax. Tokenize is used to toggle the auto-parsing of args.

##### GET /to_pwn/(id)
Convert the flow with the specified id in pwntools syntax
```

## File: `services/api/Dockerfile-api`
```
FROM python:3.10

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

STOPSIGNAL SIGINT

CMD ["gunicorn", "-w", "3", "-t", "60", "--log-level", "debug", "--capture-output", "--enable-stdio-inheritance", "-b", "0.0.0.0:5000", "webservice:create_app()"]
```

## File: `services/api/configurations.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Flower.
#
# Copyright ©2018 Nicolò Mazzucato
# Copyright ©2018 Antonio Groza
# Copyright ©2018 Brunello Simone
# Copyright ©2018 Alessio Marotta
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# Flower is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Flower is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Flower.  If not, see <https://www.gnu.org/licenses/>.

import os
from pathlib import Path

traffic_dir = Path(os.getenv("TULIP_TRAFFIC_DIR", "/traffic"))
dump_pcaps_dir = Path(os.getenv("DUMP_PCAPS", "/traffic"))
tick_length = os.getenv("TICK_LENGTH", 2*60*1000)
flag_lifetime = os.getenv("FLAG_LIFETIME", 5)
start_date = os.getenv("TICK_START", "2018-06-27T13:00:00+02:00")
flag_regex = os.getenv("FLAG_REGEX", "[A-Z0-9]{31}=")
vm_ip = os.getenv("VM_IP", "10.10.3.1")
visualizer_url = os.getenv("VISUALIZER_URL", "http://127.0.0.1:1337")

vm_ip_1 = "10.60.2.1"
helper = '''
10.61.5.1:1237 CyberUni 4
10.61.5.1:1236 CyberUni 3
10.61.5.1:1235 CyberUni 1
10.61.5.1:1234 CyberUni 2
10.60.5.1:3003 ClosedSea 1
10.60.5.1:3004 ClosedSea 2
10.62.5.1:5000 Trademark
10.63.5.1:1337 RPN
'''

services = [{"ip": x.split(" ")[0].split(":")[0], "port": int(x.split(" ")[0].split(":")[1]), "name": " ".join(x.split(" ")[1:])} for x in helper.strip().split("\n")]
services += [{"ip": vm_ip_1, "port": -1, "name": "other"}]
```

## File: `services/api/data2req.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Flower.
#
# Copyright ©2018 Nicolò Mazzucato
# Copyright ©2018 Antonio Groza
# Copyright ©2018 Brunello Simone
# Copyright ©2018 Alessio Marotta
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# Flower is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Flower is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Flower.  If not, see <https://www.gnu.org/licenses/>.

from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
from jinja2 import Environment, BaseLoader
from io import BytesIO
import json

from database import FlowDetail

DISCARD_COOKIES = ["PHPSESSID", "wordpress_logged_in_", "session"]


HEADER_TEMPLATE = """import json
import os
import sys

import requests

HOST = os.getenv('TARGET_IP')
EXTRA = json.loads(os.getenv('TARGET_EXTRA', '[]'))
{% if use_requests_session %}
s = requests.Session()
{% endif -%}
"""

REQUEST_TEMPLATE = """
{{"s." if use_requests_session}}headers = {{headers}}
{% if data -%}
data = {{data}}
{% endif -%}
{{"res = " if print_info}}{{"s" if use_requests_session else "requests"}}.{{request_method}}(f"http://{HOST}:{{port}}" + {{request_path_repr}}{% if data %}, {{data_param_name}}=data{% endif %}{{ ", headers=headers" if not use_requests_session}})
{% if print_info -%}
print(res.text)
print(res.status_code, res.headers)
{% endif %}
"""


def render(template, **kwargs):
    return Environment(loader=BaseLoader()).from_string(template).render(kwargs)


# class to parse request informations
class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, raw_http_request: bytes):
        self.rfile = BytesIO(raw_http_request)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

        self.headers: dict[str, str]
        try:
            self.headers = dict(self.headers)
        except AttributeError:
            self.headers = {}

        # Data
        try:
            self.body = raw_http_request.split(b"\r\n\r\n", 1)[1].rstrip()
        except IndexError:
            self.body = None

    def send_error(self, code, message=None, explain=None):
        self.error_code = code
        self.error_message = message


def decode_http_request(raw_request: bytes, tokenize):
    request = HTTPRequest(raw_request)
    headers = {}
    blocked_headers = [
        "content-length",
        "accept-encoding",
        "connection",
        "accept",
        "host",
    ]
    content_type = ""
    data = None
    data_param_name = None

    for i in request.headers:
        normalized_header = i.lower()

        if normalized_header == "content-type":
            content_type = request.headers[i]
        if not normalized_header in blocked_headers:
            headers[i] = request.headers[i]

    # if tokenization is enabled and body is not empty, try to decode form body or JSON body
    if tokenize and request.body:
        # try to deserialize form data
        if content_type.startswith("application/x-www-form-urlencoded"):
            data_param_name = "data"
            data = {}
            body_dict = parse_qs(request.body.decode())
            for key, value in body_dict.items():
                if len(value) == 1:
                    data[key] = value[0]
                else:
                    data[key] = value

        # try to deserialize json
        if content_type.startswith("application/json"):
            data_param_name = "json"
            try:
                data = json.loads(request.body)
            except json.decoder.JSONDecodeError:
                pass

        # Forms with files are not yet implemented
        # # try to extract files
        # if content_type.startswith("multipart/form-data"):
        #     data_param_name = "files"
        #     data  = ...

        # Fallback to use raw text if nothing else worked out
        if data is None:
            data_param_name = "data"
            data = request.body

    return request, data, data_param_name, headers


# tokenize used for automatically fill data param of request
def convert_single_http_requests(
    flow: FlowDetail,
    item_index: int,
    tokenize: bool = True,
    use_requests_session: bool = False,
):
    if not flow.items:
        return "No data"

    request, data, data_param_name, headers = decode_http_request(
        flow.items[item_index].data, tokenize
    )
    if not request.path.startswith("/"):
        raise Exception("request path must start with / to be a valid HTTP request")
    request_path_repr = repr(request.path)
    request_method = validate_request_method(request.command)

    return render(
        HEADER_TEMPLATE,
        use_requests_session=use_requests_session,
        port=flow.port_dst,
    ) + render(
        REQUEST_TEMPLATE,
        headers=repr(headers),
        data=data,
        request_method=request_method,
        request_path_repr=request_path_repr,
        data_param_name=data_param_name,
        use_requests_session=use_requests_session,
        port=flow.port_dst,
        print_info=True,
    )


def convert_flow_to_http_requests(
    flow: FlowDetail, tokenize: bool = True, use_requests_session: bool = True
):
    port = flow.port_dst
    script = render(
        HEADER_TEMPLATE,
        use_requests_session=use_requests_session,
        port=port,
    )

    for item in flow.kind_items():
        if item.direction == "c":
            request, data, data_param_name, headers = decode_http_request(
                item.data, tokenize
            )
            request_method = validate_request_method(request.command)
            if not request.path.startswith("/"):
                raise Exception(
                    "request path must start with / to be a valid HTTP request"
                )
            request_path_repr = repr(request.path)

            script += render(
                REQUEST_TEMPLATE,
                headers=repr(headers),
                data=data,
                request_method=request_method,
                request_path_repr=request_path_repr,
                data_param_name=data_param_name,
                use_requests_session=use_requests_session,
                port=port,
                print_info=True,
            )
    return script


def validate_request_method(request_method: str):
    request_method = request_method.lower()
    if request_method not in [
        "delete",
        "get",
        "head",
        "options",
        "patch",
        "post",
        "put",
    ]:
        # Throw Exception for a bad method to prevent command inject via a nasty request method
        raise Exception(f"Invalid request method: {request_method}")
    return request_method
```

## File: `services/api/database.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations

import base64
import re
import uuid
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from typing import Any, Iterator, cast

import dateutil.parser
import psycopg
import psycopg_pool
from psycopg import sql
from psycopg.rows import class_row, dict_row

import configurations
from json_util import JsonFactory


@dataclass(slots=True, kw_only=True)
class FlowQuery:
    regex_insensitive: re.Pattern | None = None
    ip_src: IPv4Network | IPv6Network | None = None
    ip_dst: IPv4Network | IPv6Network | None = None
    port_src: int | None = None
    port_dst: int | None = None
    time_from: datetime | None = None
    time_to: datetime | None = None
    tags_include: list[str] = field(default_factory=list)
    tags_exclude: list[str] = field(default_factory=list)
    tag_intersection_and: bool = False
    limit: int = 1000


@dataclass(slots=True, kw_only=True)
class Flow:
    id: uuid.UUID
    time: datetime
    port_src: int
    port_dst: int
    ip_src: IPv4Address | IPv6Address
    ip_dst: IPv4Address | IPv6Address
    duration: timedelta
    pcap_id: uuid.UUID
    pcap_name: str
    link_parent_id: uuid.UUID
    link_child_id: uuid.UUID
    fingerprints: list[int]
    packets_count: int
    packets_size: int
    flags_in: int
    flags_out: int
    signatures: list[Signature]
    tags: list[str]
    flags: list[str]
    flagids: list[str]
    rank: int = 0


@dataclass(slots=True, kw_only=True)
class Signature:
    id: int
    message: str
    action: str


@dataclass(slots=True, kw_only=True)
class FlowItem(JsonFactory):
    id: uuid.UUID
    flow_id: uuid.UUID
    kind: str
    time: datetime
    direction: str
    data: bytes

    def to_json(self) -> Any:
        result = JsonFactory.to_json(self)
        result["data"] = base64.b64encode(result["data"]).decode("ascii")
        return result


@dataclass(slots=True, kw_only=True)
class FlowDetail(Flow):
    items: list[FlowItem] = field(default_factory=list)

    def kind_items(self, kind: str = "raw") -> list[FlowItem]:
        return [i for i in self.items if i.kind == kind]

    def item_data(self, kind: str = "raw") -> list[bytes]:
        return [i.data for i in self.kind_items(kind)]

    def collect_data(self, kind: str = "raw") -> bytes:
        return b"".join(self.item_data(kind))


@dataclass(slots=True, kw_only=True)
class StatsQuery:
    service: str | None = None
    tick_from: int | None = None
    tick_to: int | None = None


@dataclass(slots=True)
class Stats:
    tick: int
    flow_count: int = 0
    tag_flag_in: int = 0
    tag_flag_out: int = 0
    tag_blocked: int = 0
    tag_suricata: int = 0
    tag_enemy: int = 0
    flag_in: int = 0
    flag_out: int = 0


class Pool(psycopg_pool.ConnectionPool):
    def __init__(self, connection_string: str, *, open: bool = False, **kwargs) -> None:
        super().__init__(
            connection_string,
            open=open,
            connection_class=Connection,
            **kwargs,
        )

    @contextmanager
    def connection(self, timeout: float | None = None) -> Iterator[Connection]:
        with super().connection(timeout) as connection:
            yield cast(Connection, connection)


class Connection(psycopg.Connection):
    def flow_query(self, query: FlowQuery) -> list[Flow]:
        pre_select = sql.SQL(
            "WITH f AS (SELECT *, fid_rank_desc(id) AS rank FROM flow ORDER BY id DESC)"
        )
        conditions = [sql.SQL("true")]
        pre_conditions = [sql.SQL("true")]
        parameters = {}

        if query.ip_src:
            parameters["ip_src"] = query.ip_src
            conditions.append(sql.SQL("f.ip_src <<= %(ip_src)s"))
        if query.ip_dst:
            parameters["ip_dst"] = query.ip_dst
            conditions.append(sql.SQL("f.ip_dst <<= %(ip_dst)s"))

        if query.port_src:
            parameters["port_src"] = query.port_src
            conditions.append(sql.SQL("f.port_src = %(port_src)s"))
        if query.port_dst:
            parameters["port_dst"] = query.port_dst
            conditions.append(sql.SQL("f.port_dst = %(port_dst)s"))

        if query.time_from:
            parameters["time_from"] = query.time_from
            conditions.append(sql.SQL("f.id > fid_pack_low(%(time_from)s)"))
            pre_conditions.append(sql.SQL("flow_id > fid_pack_low(%(time_from)s)"))
        if query.time_to:
            parameters["time_to"] = query.time_to
            conditions.append(sql.SQL("f.id < fid_pack_high(%(time_to)s)"))
            pre_conditions.append(sql.SQL("flow_id < fid_pack_high(%(time_to)s)"))

        if query.tags_include:
            parameters["tags_include"] = query.tags_include
            if query.tag_intersection_and:
                conditions.append(sql.SQL("f.tags ?& %(tags_include)s"))
            else:
                conditions.append(sql.SQL("f.tags ?| %(tags_include)s"))
        if query.tags_exclude:
            parameters["tags_exclude"] = query.tags_exclude
            conditions.append(sql.SQL("NOT f.tags ?| %(tags_exclude)s"))

        if query.regex_insensitive:
            parameters["regex_insensitive"] = query.regex_insensitive.pattern
            text = """
                WITH fi AS (
                    SELECT flow_id, fid_rank_desc(flow_id) AS rank
                    FROM flow_index
                    WHERE text ~* %(regex_insensitive)s
                        AND {pre_conditions}
                    ORDER BY rank
                ), fd AS (
                    SELECT DISTINCT flow_id, rank
                    FROM fi
                ), f AS (
                    SELECT fl.*, fd.rank
                    FROM fd
                    LEFT JOIN flow AS fl
                        ON fl.id = fd.flow_id
                )
            """
            pre_select = sql.SQL(text).format(
                pre_conditions=sql.SQL(" AND ").join(pre_conditions)
            )

        text_query = """
            /*+
                IndexScan(flow_index)
                Set(enable_material false)
            */
            {pre_select}
            SELECT f.*, p.name AS pcap_name
            FROM f
            LEFT JOIN pcap AS p
                ON p.id = f.pcap_id
            WHERE {conditions}
            LIMIT {limit}
        """

        sql_query = sql.SQL(text_query).format(
            conditions=sql.SQL(" AND ").join(conditions),
            pre_select=pre_select,
            limit=query.limit,
        )

        with self.cursor(row_factory=class_row(Flow)) as cursor:
            flows = cursor.execute(sql_query, parameters).fetchall()

        # Filter out non-existing tags
        tags = self.tag_list()
        for flow in flows:
            flow.tags = list(filter(lambda t: t in flow.tags, tags))

        return list(sorted(flows, key=lambda f: f.rank))

    def flow_detail(self, id: uuid.UUID) -> FlowDetail | None:
        sql_query = """
            SELECT f.*, p.name AS pcap_name
            FROM flow AS f
            INNER JOIN pcap AS p
                ON p.id = f.pcap_id
            WHERE f.id = %(id)s
            ORDER BY id DESC
            LIMIT 2000
        """
        with self.cursor(row_factory=class_row(FlowDetail)) as cursor:
            flow = cursor.execute(sql_query, {"id": id}).fetchone()

        if flow is None:
            return None

        flow.items = self.flow_item_query(flow)

        # Filter out non-existing tags and sort the rest
        flow.tags = list(filter(lambda t: t in flow.tags, self.tag_list()))

        return flow

    def flow_item_query(self, flow: Flow) -> list[FlowItem]:
        sql_query = """
            SELECT fi.*
            FROM flow_item AS fi
            WHERE fi.flow_id = %(flow_id)s
                AND fi.id > fid_pack_low(%(time_start)s)
                AND fi.id < fid_pack_high(%(time_end)s)
        """

        parameters = {
            "flow_id": flow.id,
            "time_start": flow.time,
            "time_end": flow.time + flow.duration,
        }

        with self.cursor(row_factory=class_row(FlowItem)) as cursor:
            return cursor.execute(sql_query, parameters).fetchall()

    def flow_tag(self, flow_id: uuid.UUID, tag: str, apply: bool) -> None:
        if apply:
            sql_query = """
                UPDATE flow
                SET tags = jsonb_unique(tags || jsonb_build_array(%(tag)s::text))
                WHERE id = %(flow_id)s
            """
        else:
            sql_query = """
                UPDATE flow
                SET tags = tags - %(tag)s::text
                WHERE id = %(flow_id)s
            """

        self.execute(sql_query, {"flow_id": flow_id, "tag": tag})

    def stats_query(self, query: StatsQuery) -> dict[int, Stats]:
        now = datetime.now(tz=timezone.utc)
        tick_first = dateutil.parser.parse(configurations.start_date)
        tick_length = timedelta(milliseconds=int(configurations.tick_length))
        tick_current = ((now - tick_first) // tick_length) + 1
        tick_start = query.tick_from if query.tick_from else 0
        tick_end = query.tick_to if query.tick_to else tick_current
        time_start = tick_first + (tick_start * tick_length)
        time_end = tick_first + (tick_end * tick_length)

        stats: dict[int, Stats] = {i: Stats(i) for i in range(tick_start, tick_end)}

        parameters = {
            "tick_length": tick_length,
            "tick_first": tick_first,
            "time_start": time_start,
            "time_end": time_end,
        }

        sql_query = """
            SELECT tick_number_bucket(%(tick_first)s, %(tick_length)s, time) AS tick,
                count(id) AS count, sum(flags_in) AS flags_in, sum(flags_out) AS flags_out
            FROM flow AS f
            WHERE f.id > fid_pack_low(%(time_start)s)
                AND f.id < fid_pack_high(%(time_end)s)
            GROUP BY tick
        """
        with self.cursor(row_factory=dict_row) as cursor:
            for row in cursor.execute(sql_query, parameters):
                stats[row["tick"]].flow_count = row["count"]
                stats[row["tick"]].flag_in = row["flags_in"]
                stats[row["tick"]].flag_out = row["flags_out"]

        # TODO: Maybe count all tags? The query already selects the numbers
        sql_query = """
            SELECT tick_time_bucket(%(tick_first)s, %(tick_length)s, time) AS tick_start,
                tick_number_bucket(%(tick_first)s, %(tick_length)s, time) AS tick,
                t.name AS tag, count(f.id) AS count
            FROM flow AS f
            JOIN tag AS t
                ON f.tags ? t.name
            WHERE f.id > fid_pack_low(%(time_start)s)
                AND f.id < fid_pack_high(%(time_end)s)
            GROUP BY tick_start, tick, t.name
            ORDER BY tick ASC
        """
        with self.cursor(row_factory=dict_row) as cursor:
            for row in cursor.execute(sql_query, parameters):
                if row["tag"] == "flag-in":
                    stats[row["tick"]].tag_flag_in += row["count"]
                elif row["tag"] == "flag-out":
                    stats[row["tick"]].tag_flag_out += row["count"]
                elif row["tag"] == "blocked":
                    stats[row["tick"]].tag_blocked += row["count"]
                elif row["tag"] == "suricata":
                    stats[row["tick"]].tag_suricata += row["count"]
                elif row["tag"] == "enemy":
                    stats[row["tick"]].tag_enemy += row["count"]

        return stats

    def tag_list(self) -> list[str]:
        with self.cursor(row_factory=dict_row) as cursor:
            tags = cursor.execute("SELECT name FROM tag ORDER BY sort ASC").fetchall()
            return [t["name"] for t in tags]
```

## File: `services/api/flow2pwn.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Flower.
#
# Copyright ©2018 Nicolò Mazzucato
# Copyright ©2018 Antonio Groza
# Copyright ©2018 Brunello Simone
# Copyright ©2018 Alessio Marotta
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# Flower is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Flower is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Flower.  If not, see <https://www.gnu.org/licenses/>.

import base64

from database import FlowDetail


def escape(i):
    if isinstance(i, str):
        i = ord(i)
    ret = chr(i) if 0x20 <= i and i < 0x7F else f"\\x{i:02x}"
    if ret in '\\"':
        ret = "\\" + ret
    return ret


def convert(message):
    return "".join([escape(i) for i in message])


# convert a flow into pwn script
def flow2pwn(flow: FlowDetail):
    script = """import json
import sys

from pwn import *

HOST = os.getenv('TARGET_IP')
EXTRA = json.loads(os.getenv('TARGET_EXTRA', '[]'))

proc = remote(HOST, {})
""".format(
        flow.port_dst
    )

    for item in flow.kind_items():
        if item.direction == "c":
            script += """proc.write(b"{}")\n""".format(convert(item.data))

        else:
            script += """proc.recvuntil(b"{}")\n""".format(
                convert(item.data[-10:]).replace("\n", "\\n")
            )

    return script
```

## File: `services/api/json_util.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import dataclasses
import json
import uuid
from datetime import datetime, timedelta
from ipaddress import IPv4Address, IPv6Address
from typing import Any


def encode(obj: Any) -> Any:
    if dataclasses.is_dataclass(obj):
        fields = dataclasses.fields(obj)
        return {f.name: getattr(obj, f.name) for f in fields}
    if isinstance(obj, timedelta):
        return obj.total_seconds()
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, uuid.UUID):
        return str(obj)
    if isinstance(obj, IPv4Address) or isinstance(obj, IPv6Address):
        return str(obj)
    return json.JSONEncoder().default(obj)


class JsonFactory(abc.ABC):
    @abc.abstractmethod
    def to_json(self) -> Any:
        return encode(self)


class Encoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, JsonFactory):
            return o.to_json()
        return encode(o)


def dumps(*args, **kwargs) -> str:
    return json.dumps(*args, cls=Encoder, **kwargs)


def loads(*args, **kwargs) -> Any:
    return json.loads(*args, **kwargs)
```

## File: `services/api/requirements.txt`
```
Flask_Cors
Flask
requests
gunicorn
python-dateutil
psycopg[binary,pool]
```

## File: `services/api/webservice.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of Flower.
#
# Copyright ©2018 Nicolò Mazzucato
# Copyright ©2018 Antonio Groza
# Copyright ©2018 Brunello Simone
# Copyright ©2018 Alessio Marotta
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# Flower is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Flower is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Flower.  If not, see <https://www.gnu.org/licenses/>.

import dataclasses
import os
import re
import traceback
import uuid
from flask import Flask, Response, send_file
from requests import get
import dateutil.parser
from ipaddress import ip_network

from configurations import (
    services,
    traffic_dir,
    start_date,
    tick_length,
    visualizer_url,
    flag_lifetime,
    flag_regex,
    dump_pcaps_dir,
)
from pathlib import Path
from data2req import convert_flow_to_http_requests, convert_single_http_requests
from flask_cors import CORS
from flask import request

from flow2pwn import flow2pwn
import database, json_util

application = Flask(__name__)
CORS(application)
db = database.Pool(os.environ["TIMESCALE"])


def return_json_response(object, **kwargs):
    return Response(json_util.dumps(object), mimetype="application/json", **kwargs)


def return_text_response(object, **kwargs):
    return Response(object, mimetype="text/plain", **kwargs)


@application.route("/")
def hello_world():
    return "Hello, World!"


@application.route("/tick_info")
def getTickInfo():
    data = {
        "startDate": start_date,
        "tickLength": tick_length,
        "flagLifetime": flag_lifetime,
    }
    return return_json_response(data)


@application.route("/query", methods=["POST"])
def query():
    query = request.get_json()

    try:
        query = database.FlowQuery(
            regex_insensitive=(
                re.compile(query["regex_insensitive"])
                if "regex_insensitive" in query
                else None
            ),
            ip_src=ip_network(query["ip_src"]) if "ip_src" in query else None,
            ip_dst=ip_network(query["ip_dst"]) if "ip_dst" in query else None,
            port_src=query.get("port_src"),
            port_dst=query.get("port_dst"),
            time_from=(
                dateutil.parser.parse(query["time_from"])
                if "time_from" in query
                else None
            ),
            time_to=(
                dateutil.parser.parse(query["time_to"]) if "time_to" in query else None
            ),
            tags_include=[str(elem) for elem in query.get("tags_include", [])],
            tags_exclude=[str(elem) for elem in query.get("tags_exclude", [])],
            tag_intersection_and=query.get("tag_intersection_mode", "").lower() == "and",
        )
    except re.error as error:
        return return_json_response(
            {
                "error": str(error),
            },
            status=400,
        )

    with db.connection() as c:
        flows = c.flow_query(query)
    flows = list(map(dataclasses.asdict, flows))
    return return_json_response(flows)


@application.route("/stats")
def getStats():
    query = request.args

    query = database.StatsQuery(
        service=query.get("service"),
        tick_from=int(query["tick_from"]) if "tick_from" in query else None,
        tick_to=int(query["tick_to"]) if "tick_to" in query else None,
    )

    with db.connection() as c:
        stats = c.stats_query(query)
    stats = list(stats.values())
    return return_json_response(stats)


@application.route("/under_attack")
def getUnderAttack():
    res = get(
        f"{visualizer_url}/api/under-attack",
        params={
            "from_tick": request.args.get("from_tick"),
            "to_tick": request.args.get("to_tick"),
        },
    )
    assert res.status_code == 200

    tick_data = res.json()
    return return_json_response(tick_data)


@application.route("/tags")
def getTags():
    with db.connection() as c:
        tags = c.tag_list()
    return return_json_response(tags)


@application.route("/star", methods=["POST"])
def setStar():
    query = request.get_json()
    flow_id = uuid.UUID(query.get("id"))
    apply = bool(query.get("star"))
    with db.connection() as c:
        c.flow_tag(flow_id, "starred", apply)
    return "ok!"


@application.route("/services")
def getServices():
    return return_json_response(services)


@application.route("/flag_regex")
def getFlagRegex():
    return return_json_response(flag_regex)


@application.route("/flow/<id>")
def getFlowDetail(id):
    id = uuid.UUID(id)
    with db.connection() as c:
        flow = c.flow_detail(id)
    return return_json_response(flow)


@application.route("/to_single_python_request", methods=["POST"])
def convertToSingleRequest():
    flow_id = request.args.get("id", "")
    item_index = request.args.get("index", "")

    if flow_id == "":
        return return_text_response(
            "There was an error while converting the request:\n{}: {}".format(
                "No flow id", "No flow id param"
            )
        )
    if item_index == "":
        return return_text_response(
            "There was an error while converting the request:\n{}: {}".format(
                "No index", "No item index param"
            )
        )

    flow_id = uuid.UUID(flow_id)
    item_index = int(item_index)
    with db.connection() as c:
        flow = c.flow_detail(flow_id)
    if not flow:
        return return_text_response(
            "There was an error while converting the request:\n{}: {}".format(
                "Invalid flow", "Invalid flow id"
            )
        )
    if item_index >= len(flow.items):
        return return_text_response(
            "There was an error while converting the request:\n{}: {}".format(
                "Invalid index", "Index out of range"
            )
        )

    tokenize = bool(request.args.get("tokenize", False))
    use_requests_session = bool(request.args.get("use_requests_session", False))
    try:
        converted = convert_single_http_requests(
            flow, item_index, tokenize, use_requests_session
        )
    except Exception as ex:
        return return_text_response(
            "There was an error while converting the request:\n{}: {}".format(
                type(ex).__name__, traceback.format_exc()
            )
        )
    return return_text_response(converted)


@application.route("/to_python_request/<id>")
def convertToRequests(id):
    id = uuid.UUID(id)
    with db.connection() as c:
        flow = c.flow_detail(id)
    if not flow:
        return return_text_response(
            "There was an error while converting the request:\n{}: {}".format(
                "Invalid flow", "Invalid flow id"
            )
        )
    tokenize = bool(request.args.get("tokenize", True))
    use_requests_session = bool(request.args.get("use_requests_session", True))
    try:
        converted = convert_flow_to_http_requests(flow, tokenize, use_requests_session)
    except Exception as ex:
        return return_text_response(
            "There was an error while converting the request:\n{}: {}".format(
                type(ex).__name__, traceback.format_exc()
            )
        )
    return return_text_response(converted)


@application.route("/to_pwn/<id>")
def confertToPwn(id):
    id = uuid.UUID(id)
    with db.connection() as c:
        flow = c.flow_detail(id)
    if not flow:
        return return_text_response(
            "There was an error while converting the request:\n{}: {}".format(
                "Invalid flow", "Invalid flow id"
            )
        )
    return return_text_response(flow2pwn(flow))


@application.route("/download/")
def downloadFile():
    filepath = request.args.get("file")
    if filepath is None:
        return return_text_response(
            "There was an error while downloading the requested file:\n{}: {}".format(
                "Invalid 'file'", "No 'file' given"
            )
        )
    filepath = Path(filepath)

    # Check for path traversal by resolving the file first.
    filepath = filepath.resolve()
    if traffic_dir not in filepath.parents and dump_pcaps_dir not in filepath.parents:
        return return_text_response(
            "There was an error while downloading the requested file:\n{}: {}".format(
                "Invalid 'file'",
                "'file' was not in a subdirectory of traffic_dir or dump_pcaps_dir",
            )
        )

    try:
        return send_file(filepath, as_attachment=True)
    except FileNotFoundError:
        return return_text_response(
            "There was an error while downloading the requested file:\n{}: {}".format(
                "Invalid 'file'", "'file' not found"
            )
        )

def create_app():
    db.open()
    return application

if __name__ == "__main__":
    try:
        db.open()
        application.run(host="0.0.0.0", threaded=True)
    finally:
        db.close()
```

## File: `services/flagids/Dockerfile`
```
FROM python:3.10

WORKDIR /app

COPY ./ /app/

COPY ./requirements.txt /app/

RUN pip install -r ./requirements.txt

COPY ./flagids.py /app/

STOPSIGNAL SIGINT

CMD ["python3", "./flagids.py"]
```

## File: `services/flagids/flagids.py`
```python
#!/bin/env python
import os
import time
from datetime import datetime

import psycopg_pool
import requests

DELAY = 5  # DELAY from start of tick
tick_length = int(os.getenv("TICK_LENGTH", 10 * 1000)) // 1000
start_date = os.getenv("TICK_START", "2018-06-27T13:00+02:00")
team_id = os.getenv("TEAM_ID", "10.10.3.1")
team_id_is_digit = team_id.isdigit()
team_id_int = int(team_id) if team_id_is_digit else None
flagid_endpoint = os.getenv("FLAGID_ENDPOINT", "http://localhost:8000/flagids.json")
flagid_scrape_enabled = os.getenv("FLAGID_SCRAPE", "") != ""

client = None
db = None
if flagid_scrape_enabled:
    print("STARTING FLAGIDS")
    print("CONFIG:")
    print("  DELAY: ", DELAY)
    print("  TICK_LENGTH: ", tick_length)
    print("  TICK_START: ", start_date)
    print("  TIMESCALE: ", os.environ.get("TIMESCALE"))
    print("  TEAM_ID: ", team_id)
    print("  FLAGID_ENDPOINT: ", flagid_endpoint)
    db = psycopg_pool.ConnectionPool(os.environ["TIMESCALE"])
    print("CONNECTION TO MONGO ESTABLISHED", flush=True)
else:
    print("FLAGID SCRAPE DISABLED", flush=True)


# get leaf nodes of a json data struct
def get_leaf_nodes(data):
    if isinstance(data, dict):
        if team_id in data.keys():
            yield from get_leaf_nodes(data[team_id])
        elif team_id_is_digit and team_id_int in data.keys():
            yield from get_leaf_nodes(data[team_id_int])
        else:
            for value in data.values():
                yield from get_leaf_nodes(value)
    elif isinstance(data, list):
        if team_id in data or (team_id_is_digit and team_id_int in data):
            yield
        else:
            for item in data:
                print(item, end=" ", flush=True)
                yield from get_leaf_nodes(item)
    else:
        # prevent id from being used as Flagids
        yield data


def update_flagids():
    assert db is not None

    response = requests.get(flagid_endpoint)
    rows = [(node,) for node in get_leaf_nodes(response.json()) if node is not None]
    print("Updating flagids: ", time.time(), f"({len(rows)})", flush=True)

    with db.connection() as conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO flag_id (content) VALUES (%s)", rows)
            conn.commit()


def main():
    start_datetime = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S%z")
    unixtime = time.mktime(start_datetime.timetuple())
    while True:
        try:
            if flagid_scrape_enabled:
                update_flagids()
            crnt_time = time.time()
            time_diff = max(0, crnt_time - unixtime)
            wait = (
                DELAY
                + tick_length * (time_diff // tick_length)
                + time_diff % tick_length
            )
            time.sleep(wait)
        except Exception as e:
            print("ERROR: ", e, flush=True)
            time.sleep(10)


if __name__ == "__main__":
    main()
```

## File: `services/flagids/requirements.txt`
```
requests
psycopg[binary,pool]
```

## File: `services/go-importer/.gitignore`
```
/assembler
/enricher

__debug_bin
```

## File: `services/go-importer/Dockerfile-assembler`
```
FROM golang:1.25-alpine

RUN apk add --no-cache git make build-base libpcap-dev python3 py3-pip python3-dev bsd-compat-headers openssl-dev

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download
COPY ./converters/helpers/requirements.txt ./converters/helpers/requirements.txt
RUN python3 -m pip install -r ./converters/helpers/requirements.txt --break-system-packages

COPY . .

RUN go build ./cmd/assembler
```

## File: `services/go-importer/Dockerfile-enricher`
```
FROM golang:1.25-alpine

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN go build ./cmd/enricher
```

## File: `services/go-importer/go.mod`
```
module go-importer

go 1.23.0

toolchain go1.24.7

require (
	github.com/andybalholm/brotli v1.0.4
	github.com/cloudflare/ahocorasick v0.0.0-20210425175752-730270c3e184
	github.com/fsnotify/fsnotify v1.5.4
	github.com/gammazero/workerpool v1.1.3
	github.com/gofrs/uuid/v5 v5.0.0
	github.com/gopacket/gopacket v1.3.0
	github.com/jackc/pgx-gofrs-uuid v0.0.0-20230224015001-1d428863c2e2
	github.com/jackc/pgx/v5 v5.4.3
	github.com/tidwall/gjson v1.14.1
	github.com/vmihailenco/msgpack/v5 v5.3.5
)

require (
	github.com/gammazero/deque v0.2.0 // indirect
	github.com/jackc/pgpassfile v1.0.0 // indirect
	github.com/jackc/pgservicefile v0.0.0-20221227161230-091c0ba34f0a // indirect
	github.com/jackc/puddle/v2 v2.2.1 // indirect
	github.com/tidwall/match v1.1.1 // indirect
	github.com/tidwall/pretty v1.2.0 // indirect
	github.com/vmihailenco/tagparser/v2 v2.0.0 // indirect
	golang.org/x/crypto v0.26.0 // indirect
	golang.org/x/net v0.28.0 // indirect
	golang.org/x/sync v0.8.0 // indirect
	golang.org/x/sys v0.24.0 // indirect
	golang.org/x/text v0.17.0 // indirect
)
```

## File: `services/go-importer/go.sum`
```
github.com/andybalholm/brotli v1.0.4 h1:V7DdXeJtZscaqfNuAdSRuRFzuiKlHSC/Zh3zl9qY3JY=
github.com/andybalholm/brotli v1.0.4/go.mod h1:fO7iG3H7G2nSZ7m0zPUDn85XEX2GTukHGRSepvi9Eig=
github.com/cloudflare/ahocorasick v0.0.0-20210425175752-730270c3e184 h1:8yL+85JpbwrIc6m+7N1iYrjn/22z68jwrTIBOJHNe4k=
github.com/cloudflare/ahocorasick v0.0.0-20210425175752-730270c3e184/go.mod h1:tGWUZLZp9ajsxUOnHmFFLnqnlKXsCn6GReG4jAD59H0=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/fsnotify/fsnotify v1.5.4 h1:jRbGcIw6P2Meqdwuo0H1p6JVLbL5DHKAKlYndzMwVZI=
github.com/fsnotify/fsnotify v1.5.4/go.mod h1:OVB6XrOHzAwXMpEM7uPOzcehqUV2UqJxmVXmkdnm1bU=
github.com/gammazero/deque v0.2.0 h1:SkieyNB4bg2/uZZLxvya0Pq6diUlwx7m2TeT7GAIWaA=
github.com/gammazero/deque v0.2.0/go.mod h1:LFroj8x4cMYCukHJDbxFCkT+r9AndaJnFMuZDV34tuU=
github.com/gammazero/workerpool v1.1.3 h1:WixN4xzukFoN0XSeXF6puqEqFTl2mECI9S6W44HWy9Q=
github.com/gammazero/workerpool v1.1.3/go.mod h1:wPjyBLDbyKnUn2XwwyD3EEwo9dHutia9/fwNmSHWACc=
github.com/gofrs/uuid/v5 v5.0.0 h1:p544++a97kEL+svbcFbCQVM9KFu0Yo25UoISXGNNH9M=
github.com/gofrs/uuid/v5 v5.0.0/go.mod h1:CDOjlDMVAtN56jqyRUZh58JT31Tiw7/oQyEXZV+9bD8=
github.com/gopacket/gopacket v1.3.0 h1:MouZCc+ej0vnqzB0WeiaO/6+tGvb+KU7UczxoQ+X0Yc=
github.com/gopacket/gopacket v1.3.0/go.mod h1:WnFrU1Xkf5lWKV38uKNR9+yYtppn+ZYzOyNqMeH4oNE=
github.com/jackc/pgpassfile v1.0.0 h1:/6Hmqy13Ss2zCq62VdNG8tM1wchn8zjSGOBJ6icpsIM=
github.com/jackc/pgpassfile v1.0.0/go.mod h1:CEx0iS5ambNFdcRtxPj5JhEz+xB6uRky5eyVu/W2HEg=
github.com/jackc/pgservicefile v0.0.0-20221227161230-091c0ba34f0a h1:bbPeKD0xmW/Y25WS6cokEszi5g+S0QxI/d45PkRi7Nk=
github.com/jackc/pgservicefile v0.0.0-20221227161230-091c0ba34f0a/go.mod h1:5TJZWKEWniPve33vlWYSoGYefn3gLQRzjfDlhSJ9ZKM=
github.com/jackc/pgx-gofrs-uuid v0.0.0-20230224015001-1d428863c2e2 h1:QWdhlQz98hUe1xmjADOl2mr8ERLrOqj0KWLdkrnNsRQ=
github.com/jackc/pgx-gofrs-uuid v0.0.0-20230224015001-1d428863c2e2/go.mod h1:Ti7pyNDU/UpXKmBTeFgxTvzYDM9xHLiYKMsLdt4b9cg=
github.com/jackc/pgx/v5 v5.4.3 h1:cxFyXhxlvAifxnkKKdlxv8XqUf59tDlYjnV5YYfsJJY=
github.com/jackc/pgx/v5 v5.4.3/go.mod h1:Ig06C2Vu0t5qXC60W8sqIthScaEnFvojjj9dSljmHRA=
github.com/jackc/puddle/v2 v2.2.1 h1:RhxXJtFG022u4ibrCSMSiu5aOq1i77R3OHKNJj77OAk=
github.com/jackc/puddle/v2 v2.2.1/go.mod h1:vriiEXHvEE654aYKXXjOvZM39qJ0q+azkZFrfEOc3H4=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.6.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.7.0/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.8.1 h1:w7B6lhMri9wdJUVmEZPGGhZzrYTPvgJArz7wNPgYKsk=
github.com/stretchr/testify v1.8.1/go.mod h1:w2LPCIKwWwSfY2zedu0+kehJoqGctiVI29o6fzry7u4=
github.com/tidwall/gjson v1.14.1 h1:iymTbGkQBhveq21bEvAQ81I0LEBork8BFe1CUZXdyuo=
github.com/tidwall/gjson v1.14.1/go.mod h1:/wbyibRr2FHMks5tjHJ5F8dMZh3AcwJEMf5vlfC0lxk=
github.com/tidwall/match v1.1.1 h1:+Ho715JplO36QYgwN9PGYNhgZvoUSc9X2c80KVTi+GA=
github.com/tidwall/match v1.1.1/go.mod h1:eRSPERbgtNPcGhD8UCthc6PmLEQXEWd3PRB5JTxsfmM=
github.com/tidwall/pretty v1.2.0 h1:RWIZEg2iJ8/g6fDDYzMpobmaoGh5OLl4AXtGUGPcqCs=
github.com/tidwall/pretty v1.2.0/go.mod h1:ITEVvHYasfjBbM0u2Pg8T2nJnzm8xPwvNhhsoaGGjNU=
github.com/vishvananda/netlink v1.1.0 h1:1iyaYNBLmP6L0220aDnYQpo1QEV4t4hJ+xEEhhJH8j0=
github.com/vishvananda/netlink v1.1.0/go.mod h1:cTgwzPIzzgDAYoQrMm0EdrjRUBkTqKYppBueQtXaqoE=
github.com/vishvananda/netns v0.0.0-20211101163701-50045581ed74 h1:gga7acRE695APm9hlsSMoOoE65U4/TcqNj90mc69Rlg=
github.com/vishvananda/netns v0.0.0-20211101163701-50045581ed74/go.mod h1:DD4vA1DwXk04H54A1oHXtwZmA0grkVMdPxx/VGLCah0=
github.com/vmihailenco/msgpack/v5 v5.3.5 h1:5gO0H1iULLWGhs2H5tbAHIZTV8/cYafcFOr9znI5mJU=
github.com/vmihailenco/msgpack/v5 v5.3.5/go.mod h1:7xyJ9e+0+9SaZT0Wt1RGleJXzli6Q/V5KbhBonMG9jc=
github.com/vmihailenco/tagparser/v2 v2.0.0 h1:y09buUbR+b5aycVFQs/g70pqKVZNBmxwAhO7/IwNM9g=
github.com/vmihailenco/tagparser/v2 v2.0.0/go.mod h1:Wri+At7QHww0WTrCBeu4J6bNtoV6mEfg5OIWRZA9qds=
go.uber.org/goleak v1.1.12 h1:gZAh5/EyT/HQwlpkCy6wTpqfH9H8Lz8zbm3dZh+OyzA=
go.uber.org/goleak v1.1.12/go.mod h1:cwTWslyiVhfpKIDGSZEM2HlOvcqm+tG4zioyIeLoqMQ=
golang.org/x/crypto v0.26.0 h1:RrRspgV4mU+YwB4FYnuBoKsUapNIL5cohGAmSH3azsw=
golang.org/x/crypto v0.26.0/go.mod h1:GY7jblb9wI+FOo5y8/S2oY4zWP07AkOJ4+jxCqdqn54=
golang.org/x/net v0.28.0 h1:a9JDOJc5GMUJ0+UDqmLT86WiEy7iWyIhz8gz8E4e5hE=
golang.org/x/net v0.28.0/go.mod h1:yqtgsTWOOnlGLG9GFRrK3++bGOUEkNBoHZc8MEDWPNg=
golang.org/x/sync v0.8.0 h1:3NFvSEYkUoMifnESzZl15y791HH1qU2xm6eCJU5ZPXQ=
golang.org/x/sync v0.8.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sys v0.0.0-20220412211240-33da011f77ad/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.24.0 h1:Twjiwq9dn6R1fQcyiK+wQyHWfaz/BJB+YIpzU/Cv3Xg=
golang.org/x/sys v0.24.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/text v0.17.0 h1:XtiM5bkSOt+ewxlOE/aE/AKEHibwj/6gvWMl9Rsh0Qc=
golang.org/x/text v0.17.0/go.mod h1:BuEKDfySbSR4drPmRPG/7iBdf8hvFMuRexcpahXilzY=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `services/go-importer/cmd/assembler/flagValidator.go`
```go
package main

import (
	"encoding/base64"
	"encoding/binary"
	"log"
	"strconv"
	"time"
)

type FlagValidator interface {
	IsValid(flag string, refTime time.Time) bool
}

type DummyFlagValidator struct{}

func (f *DummyFlagValidator) IsValid(flag string, refTime time.Time) bool { return true }

// Helper function for time validation
func IsFlagTimeValid(timeFromFlag, referenceTime time.Time, tolerance time.Duration) bool {
	return timeFromFlag.Before(referenceTime.Add(tolerance)) && timeFromFlag.After(referenceTime.Add(-tolerance))
}


// Team net checking can be disabled by setting teamNet to -1.
// Time checking can be disabled by setting timeTolerance to zero.
type FaustFlagValidator struct {
	teamNet       int
	timeTolerance time.Duration
	xorString     string
}

func (validator *FaustFlagValidator) IsValid(flag string, refTime time.Time) bool {
	const RAW_FLAG_DATA_LEN = 32
	const FLAG_DATA_LEN = 8 + 4 + 2
	data, err := base64.StdEncoding.DecodeString(flag[len(flag)-RAW_FLAG_DATA_LEN:])
	if err != nil {
		// We weren't able to decode it, probably fake flag
		log.Printf("Error during decode of flag %q: %s\n", flag, err)
		return false
	}
	if len(data) < FLAG_DATA_LEN {
		return false
	}

	for x := range [FLAG_DATA_LEN]int{} {
		data[x] = data[x] ^ validator.xorString[x]
	}

	flagTime := time.UnixMilli(int64(binary.BigEndian.Uint64(data[:8])))
	// flagId := int(binary.BigEndian.Uint32(data[8:12]))
	teamNet := int(binary.BigEndian.Uint16(data[12:14]))

	return (validator.teamNet == -1 || validator.teamNet == teamNet) &&
		(validator.timeTolerance == 0 || IsFlagTimeValid(flagTime, refTime, validator.timeTolerance))
}

// Team ID checking can be disabled by setting teamId to -1.
// Time checking can be disabled by setting timeTolerance, startTime and/or tickLength to zero.
type EnowarsFlagValidator struct {
	teamId        int
	serviceCount  int
	maxFlagStores int
	timeTolerance time.Duration
	startTime     time.Time
	tickLength    time.Duration
}

func (validator *EnowarsFlagValidator) IsValid(flag string, refTime time.Time) bool {
	const RAW_FLAG_DATA_LEN = 48
	const FLAG_DATA_LEN = 4 * 4
	data, err := base64.StdEncoding.DecodeString(flag[len(flag)-RAW_FLAG_DATA_LEN:])
	if err != nil {
		// We weren't able to decode it, probably fake flag
		log.Printf("Error during decode of flag %q: %s\n", flag, err)
		return false
	}
	if len(data) < FLAG_DATA_LEN {
		return false
	}

	serviceId := int(binary.LittleEndian.Uint32(data[0:4])) // = Service
	roundOffset := int(binary.LittleEndian.Uint32(data[4:8])) // Flag store
	ownerId := int(binary.LittleEndian.Uint32(data[8:12])) // = Team
	roundId := binary.LittleEndian.Uint32(data[12:16]) // = Tick

	return (validator.teamId == -1 || validator.teamId == ownerId) &&
		serviceId <= validator.serviceCount &&
		roundOffset <= validator.maxFlagStores &&
		(validator.startTime.IsZero() ||
			validator.tickLength <= 0 ||
			validator.timeTolerance == 0 ||
			IsFlagTimeValid(validator.startTime.Add(time.Duration(roundId) * validator.tickLength), refTime, validator.timeTolerance))
}

// Team ID checking can be disabled by setting teamId to -1.
// Time checking can be disabled by setting timeTolerance, startTime and/or tickLength to zero.
type ItallyADFlagValidator struct {
	teamId        int
	serviceCount  int
	timeTolerance time.Duration
	startTime     time.Time
	tickLength    time.Duration
}

func (validator *ItallyADFlagValidator) IsValid(flag string, refTime time.Time) bool {
	var round, team, service int64
	var err error

	round, err = strconv.ParseInt(flag[0:2], 36, 0) // = Tick
	if err != nil {
		return false
	}
	team, err = strconv.ParseInt(flag[3:4], 36, 0) // = Team
	if err != nil {
		return false
	}
	service, err = strconv.ParseInt(flag[5:6], 36, 0) // = Service
	if err != nil {
		return false
	}

	return (validator.teamId == -1 || validator.teamId == int(team)) &&
		int(service) <= validator.serviceCount &&
		(validator.startTime.IsZero() ||
			validator.tickLength <= 0 ||
			validator.timeTolerance == 0 ||
			IsFlagTimeValid(validator.startTime.Add(time.Duration(round) * validator.tickLength), refTime, validator.timeTolerance))
}
```

## File: `services/go-importer/cmd/assembler/http.go`
```go
package main

import (
	"bufio"
	"bytes"
	"compress/gzip"
	"go-importer/internal/pkg/db"
	"hash/crc32"
	"io"
	"net/http"
	"net/http/httputil"
	"net/url"

	"github.com/andybalholm/brotli"
)

func AddFingerprints(cookies []*http.Cookie, fingerPrints map[uint32]bool) {
	for _, cookie := range cookies {

		// Prevent exploitation by encoding :pray:, who cares about collisions
		checksum := crc32.Checksum([]byte(url.QueryEscape(cookie.Name)), crc32.IEEETable)
		checksum = crc32.Update(checksum, crc32.IEEETable, []byte("="))
		checksum = crc32.Update(checksum, crc32.IEEETable, []byte(url.QueryEscape(cookie.Value)))
		fingerPrints[checksum] = true
	}
}

// Parse and simplify every item in the flow. Items that were not successfuly
// parsed are left as-is.
//
// If we manage to simplify a flow, the new data is placed in flowEntry.data
func ParseHttpFlow(g_db *db.Database, flow *db.FlowEntry) {
	// Use a set to get rid of duplicates
	fingerprintsSet := make(map[uint32]bool)

	for i := range flow.Flow {
		flowItem := &flow.Flow[i]
		// Run only on raw representation
		if flowItem.Kind != "raw" {
			continue
		}

		// TODO; rethink the flowItem format to make this less clunky
		reader := bufio.NewReader(bytes.NewReader(flowItem.Data))

		if flowItem.From == "c" {
			// HTTP Request
			req, err := http.ReadRequest(reader)
			if err != nil || req == nil {
				continue
			}

			if !contains(flow.Tags, "http") {
				flow.Tags = append(flow.Tags, "http")
			}

			if *http_session_tracking {
				// Parse cookie and grab fingerprints
				AddFingerprints(req.Cookies(), fingerprintsSet)
			}

			//TODO; replace the HTTP data.
			// Remember to use a `LimitReader` when implementing this to prevent
			// decompressions bombs / DOS!
		} else if flowItem.From == "s" {
			// Parse HTTP Response
			res, err := http.ReadResponse(reader, nil)
			if err != nil || res == nil {
				continue
			}

			if !contains(flow.Tags, "http") {
				flow.Tags = append(flow.Tags, "http")
			}

			if *http_session_tracking {
				// Parse cookie and grab fingerprints
				AddFingerprints(res.Cookies(), fingerprintsSet)
			}

			// Substitute body
			encoding := res.Header["Content-Encoding"]
			if encoding == nil || len(encoding) == 0 {
				// If we don't find an encoding header, it is either not valid,
				// or already in plain text. In any case, we don't have to edit anything.
				continue
			}

			var newReader io.Reader
			if err != nil {
				// Failed to fully read the body. Bail out here
				continue
			}

			switch encoding[0] {
			case "gzip":
				newReader, err = handleGzip(res.Body)
				break
			case "br":
				newReader, err = handleBrotili(res.Body)
				break
			case "deflate":
				//TODO; verify this is correct
				newReader, err = handleGzip(res.Body)
				break
			default:
				// Skipped, unknown or identity encoding
				continue
			}

			// Replace the reader to allow for in-place decompression
			if err == nil && newReader != nil {
				// Limit the reader to prevent potential decompression bombs
				res.Body = io.NopCloser(io.LimitReader(newReader, int64(*maxFlowItemSize * 1024 * 1024)))
				// Delete the content-encoding header as we've basically skipped its purpose (otherwise, pkappa converters will have issues as they think it's still encoded).
				// In case of multiple values there, this logic wouldn't be hit anyway
				res.Header.Del("Content-Encoding")
				// invalidate the content length, since decompressing the body will change its value.
				res.ContentLength = -1
				replacement, err := httputil.DumpResponse(res, true)
				if err != nil {
					// HTTPUtil failed us, continue without replacing anything.
					continue
				}
				// This can exceed the mongo document limit, so we need to make sure
				// the replacement will fit
				new_size := flow.Size + (len(replacement) - len(flowItem.Data))
				if new_size <= *maxFlowItemSize * 1024 * 1024 {
					flowItem.Data = replacement
					flow.Size = new_size
				}
			}
		}
	}

	if *http_session_tracking {
		// Use maps.Keys(fingerprintsSet) in the future
		flow.Fingerprints = make([]uint32, 0, len(fingerprintsSet))
		for k := range fingerprintsSet {
			flow.Fingerprints = append(flow.Fingerprints, k)
		}
	}
}

func handleGzip(r io.Reader) (io.Reader, error) {
	return gzip.NewReader(r)
}

func handleBrotili(r io.Reader) (io.Reader, error) {
	reader := brotli.NewReader(r)
	return reader, nil
}
```

## File: `services/go-importer/cmd/assembler/main.go`
```go
package main

import (
	"go-importer/internal/converters"
	"go-importer/internal/pkg/db"
	"io/ioutil"
	"runtime"

	"github.com/gammazero/workerpool"

	"flag"
	"fmt"
	"log"
	"math"
	"net"
	"os"
	"os/signal"
	"path/filepath"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/fsnotify/fsnotify"
	"github.com/gopacket/gopacket"
	"github.com/gopacket/gopacket/examples/util"
	"github.com/gopacket/gopacket/ip4defrag"
	"github.com/gopacket/gopacket/layers"
	"github.com/gopacket/gopacket/pcap"
  "github.com/gopacket/gopacket/pcapgo"
	"github.com/gopacket/gopacket/reassembly"
)

var decoder = ""
var lazy = false
var checksum = false
var nohttp = true

var snaplen = 65536
var tstype = ""
var promisc = true

var watch_dir = flag.String("dir", "", "Directory to watch for new pcaps")
var timescale = flag.String("timescale", "", "Timescale connection string (e. g. postgres://usr:pwd@host:5432/tulip)")
var flag_regex = flag.String("flag", "", "flag regex, used for flag in/out tagging")
var pcap_over_ip = flag.String("pcap-over-ip", "", "PCAP-over-IP host + port (e.g. remote:1337)")
var bpf = flag.String("bpf", "", "BPF filter")
var nonstrict = flag.Bool("nonstrict", false, "Do not check strict TCP / FSM flags")

var flagid = flag.Bool("flagid", false, "Check for flagids in traffic (must be present in mong)")
var ticklength = flag.Int("tick-length", -1, "the length (in seconds) of a tick")
var flaglifetime = flag.Int("flag-lifetime", -1, "the lifetime of a flag in ticks")
var flagTickStartRaw = flag.String("flag-tick-start", "", "CTF start time (used for flag validation)")
var flagTickStart time.Time
var flagValidatorType = flag.String("flag-validator-type", "", "Flag validator type, this must be set to enable flag validation. Must be one of the following: FAUST, ENO/ENOWARS, ITAD")
var flagValidatorTeam = flag.Int("flag-validator-team", -1, "Team ID used for flag validation")

var skipchecksum = flag.Bool("skipchecksum", false, "Do not check the TCP checksum")
var http_session_tracking = flag.Bool("http-session-tracking", false, "Enable http session tracking.")
var disableConverters = flag.Bool("disable-converters", false, "Disable converters in case they cause issues")
var concurrentConverters = flag.Int("concurrent-converters", 2, "How many processes should be started per single converter")
var concurrentFlows = flag.Int("concurrent-flows", 0, "How many flows should be processed at the same time")

var flushAfter = flag.String("flush-after", "30s", `(TCP) Connections which have buffered packets (they've gotten packets out of order and
are waiting for old packets to fill the gaps) can be flushed after they're this old
(their oldest gap is skipped). This is particularly useful for pcap-over-ip captures.
Any string parsed by time.ParseDuration is acceptable here (ie. "3m", "2h45m").
This setting defaults to "30s" unless specified. To prevent connection flooding,
it is not recommended setting this to a high value, since assembler persists between pcaps.
Setting this to empty value disables TCP flushing.`)
var flushAfterUdp = flag.String("flush-after-udp", "30s", `Same as flush-after, except for UDP connections.
UDP connections are assembled by unique pairings of ip addressed and ports on both sides.
The only way a UDP connection is considered closed, is if this timeout passes without seeing any new packets.
This setting defaults to "30s" unless specified. To prevent connection flooding,
it is not recommended setting this to a high value, since assembler persists between pcaps.
Setting this to empty value disables UDP flushing.`)
var flushInterval = flag.String("flush-interval", "15s", `Period of flushing while processing one pcap.
Any string parsed by time.ParseDuration is acceptable here (ie. "3m", "2h45m").
Flushing always happens between pcaps, but sometimes (for example with PCAP-over-IP) it is required to flush periodically
while processing one file (since PCAP-over-IP treats whole connection as one pcap file). This is also the period for debug prints.`)
var dumpPcaps = flag.String("dump-pcaps", "", `Generate a pcap in this directory every "dump-pcaps-interval".
Empty string (default) disables this behavior. This is useful for saving pcaps from PCAP-over-IP.`)
var dumpPcapsInterval = flag.String("dump-pcaps-interval", "5m", `Period for PCAP dumping. Requres "dump-pcaps" to be set.
Any string parsed by time.ParseDuration is acceptable here (ie. "3m", "2h45m").`)
var dumpPcapsFilename = flag.String("dump-pcaps-filename", "2006-01-02_15-04-05.pcap", `Filename for dumped PCAP.
Reference: https://pkg.go.dev/time#Layout`)
var maxFlowItemSize = flag.Int("max-flow-item-size", 16, `Maximum size in MiB of one flow item record.
While PostgreSQL technically supports values up to 1GiB, they are not very nice to work with.`)

var g_db *db.Database
var workerPool *workerpool.WorkerPool
var flagValidator FlagValidator

// flagid caching (only once per tick)
var flagids []db.FlagId
var flagidUpdate int64 = 0

// TODO; FIXME; RDJ; this is kinda gross, but this is PoC level code
func reassemblyCallback(entry db.FlowEntry) {
	// By default, the callback passed is blocking per single packet. If for some reason converters hang,
	// we *really* don't want to end up in a situation where we don't get any packets ingested until the converter
	// times out.
	workerPool.Submit(func() {
		// Parsing HTTP will decode encodings to a plaintext format
		ParseHttpFlow(g_db, &entry)

		if !*disableConverters {
			converters.RunPipeline(g_db, &entry)
		}

		// Apply flag in / flagout
		if *flag_regex != "" {
			ApplyFlagTags(&entry, flag_regex, flagValidator)
		}

		// Apply flagid in / out
		if *flagid {
			unix := time.Now().Unix()
			if flagidUpdate+int64(*ticklength) < unix {
				flagidUpdate = unix
				zwi, err := g_db.FlagIdsQuery(*flaglifetime)
				if err != nil {
					log.Fatal(err)
				}
				flagids = zwi
			}
			ApplyFlagids(&entry, flagids)
		}

		// Finally, insert the new entry
		g_db.FlowInsert(entry)
	})
}

type AssemblerService struct {
	Defragmenter         *ip4defrag.IPv4Defragmenter
	StreamFactory        *TcpStreamFactory
	StreamPool           *reassembly.StreamPool
	AssemblerTcp         *reassembly.Assembler
	AssemblerUdp         *UdpAssembler
	ConnectionTcpTimeout time.Duration
	ConnectionUdpTimeout time.Duration
	FlushInterval        time.Duration
	BpfFilter            string
	PcapOverIp           bool
	DumpDirectory        string
	DumpInterval         time.Duration
	DumpFile             *os.File
	DumpWriter           *pcapgo.Writer
	DumpLast             time.Time
	DumpCount            uint64
	DumpFilename         string
}

func NewAssemblerService() *AssemblerService {
	streamFactory := &TcpStreamFactory{reassemblyCallback: reassemblyCallback}
	streamPool := reassembly.NewStreamPool(streamFactory)
	assemblerUdp := NewUdpAssembler()

	return &AssemblerService{
		Defragmenter:  ip4defrag.NewIPv4Defragmenter(),
		StreamFactory: streamFactory,
		StreamPool:    streamPool,
		AssemblerTcp:  reassembly.NewAssembler(streamPool),
		AssemblerUdp:  &assemblerUdp,
		DumpLast:      time.Now(),
	}
}

func (service *AssemblerService) FlushConnections() {
	thresholdTcp := time.Now().Add(-service.ConnectionTcpTimeout)
	thresholdUdp := time.Now().Add(-service.ConnectionUdpTimeout)
	flushed, closed, discarded := 0, 0, 0

	if service.ConnectionTcpTimeout != 0 {
		flushed, closed = service.AssemblerTcp.FlushCloseOlderThan(thresholdTcp)
		discarded = service.Defragmenter.DiscardOlderThan(thresholdTcp)
	}

	if flushed != 0 || closed != 0 || discarded != 0 {
		log.Println("Flushed", flushed, "closed", closed, "and discarded", discarded, "connections")
	}

	if service.ConnectionUdpTimeout != 0 {
		udpFlows := service.AssemblerUdp.CompleteOlderThan(thresholdUdp)
		for _, flow := range udpFlows {
			reassemblyCallback(*flow)
		}

		if len(udpFlows) != 0 {
			log.Println("Assembled", len(udpFlows), "udp flows")
		}
	}
}

func main() {
	defer util.Run()()

	flag.Parse()
	if flag.NArg() < 1 && *watch_dir == "" {
		log.Fatal("Usage: ./go-importer <file0.pcap> ... <fileN.pcap>")
	}

	// DELAY for testing
	strdelay := os.Getenv("DELAY")
	if strdelay != "" {
		delay, err := strconv.Atoi(strdelay)
		if err != nil {
			log.Println("Error: ", err)
		} else {
			time.Sleep(time.Second * time.Duration(delay))
		}
	}

	// get TICK_LENGTH
	strticklength := os.Getenv("TICK_LENGTH")
	if *ticklength == -1 && strticklength != "" {
		zwi, err := strconv.ParseInt(strticklength, 10, 64)
		if err != nil {
			log.Println("Error: ", err)
		} else {
			*ticklength = int(zwi / 1000)
		}
	}

	// get Flag_LIFETIME
	if strflaglifetime := os.Getenv("FLAG_LIFETIME"); *flaglifetime == -1 && strflaglifetime != "" {
		zwi, err := strconv.Atoi(strflaglifetime)
		if err != nil {
			log.Println("Error: ", err)
		} else {
			*flaglifetime = zwi
		}
	}

	if *ticklength != -1 && *flaglifetime != -1 {
		*flaglifetime *= *ticklength
	}

	// get TICK_START
	if *flagTickStartRaw == "" {
		*flagTickStartRaw = os.Getenv("TICK_START")
	}
	if *flagTickStartRaw != "" {
		startTime, err := time.Parse("2006-01-02T15:04Z07:00", *flagTickStartRaw)
		if err != nil {
			// If that format fail, we try it to parse it as RFC3339 ("2006-01-02T15:04:05Z07:00")
			startTime, err = time.Parse(time.RFC3339, *flagTickStartRaw)
		}
		if err != nil {
			log.Fatal("Invalid start time: ", err)
		}
		flagTickStart = startTime
	} 

	if concurrentFlows == nil || *concurrentFlows == 0 {
		*concurrentFlows = runtime.NumCPU() / 2
		if *concurrentFlows < 4 {
			*concurrentFlows = 4
		}
	}

	workerPool = workerpool.New(*concurrentFlows)

	// If no timescale connection string was supplied, use env variable
	if *timescale == "" {
		*timescale = os.Getenv("TIMESCALE")
	}

	// If no flag regex was supplied via cli, check the env
	if *flag_regex == "" {
		*flag_regex = os.Getenv("FLAG_REGEX")
		// if that didn't work, warn the user and continue
		if *flag_regex == "" {
			log.Print("WARNING; no flag regex found. No flag-in or flag-out tags will be applied.")
		}
	}

	if *pcap_over_ip == "" {
		*pcap_over_ip = os.Getenv("PCAP_OVER_IP")
	}

	// if flagid scans should be done
	if !*flagid {
		flagid_val := os.Getenv("FLAGID_SCAN")
		*flagid = flagid_val != "" && flagid_val != "0" && !strings.EqualFold(flagid_val, "false")

	}

	if *bpf == "" {
		*bpf = os.Getenv("BPF")
	}

	// Load flag validator variables
	if *flagValidatorType == "" {
		*flagValidatorType = os.Getenv("FLAG_VALIDATOR_TYPE")
	}
	if unparsed := os.Getenv("FLAG_VALIDATOR_TEAM"); *flagValidatorTeam == -1 && unparsed != "" {
		parsed, err := strconv.Atoi(unparsed)
		if err != nil {
			log.Fatal("Invalid flag validator team: ", err)
		}
		*flagValidatorTeam = parsed
	}
	
	// Flag validator setup
	if *flagValidatorType != "" && *flag_regex == "" {
		log.Println("WARNING: Flag validation enabled but no flag regex specified. No flag validation will be done.")
	}
	switch strings.ToLower(*flagValidatorType) {
	case "faust":
		flagValidator = &FaustFlagValidator{*flagValidatorTeam, time.Hour, "CTF-GAMESERVER"}
	case "enowars", "eno":
		// I don't think that there will be more than 20 services and 20 flag stores (per service)...
		flagValidator = &EnowarsFlagValidator{
			*flagValidatorTeam,
			20,
			20,
			time.Hour,
			flagTickStart,
			time.Duration(*ticklength) * time.Second,
		}
	case "itad":
		// 20 services should be more than enough...
		flagValidator = &ItallyADFlagValidator{
			*flagValidatorTeam,
			20,
			time.Hour,
			flagTickStart,
			time.Duration(*ticklength) * time.Second,
		}
	case "":
		if *flagValidatorTeam != -1  {
			log.Println("WARNING: No flag validator type specified but additional flag validator options are set. No flag validation will be done.")
		}
		flagValidator = &DummyFlagValidator{}
	default:
		log.Fatalln("Uknown -flag-validator-type: ", *flagValidatorType)
	}


	log.Println("Connecting to Timescale:", *timescale)
	g_db = db.NewDatabase(*timescale)

	service := NewAssemblerService()
	service.BpfFilter = *bpf

	// PCAP dumping parameters
	if os.Getenv("DUMP_PCAPS") != "" {
		*dumpPcaps = os.Getenv("DUMP_PCAPS")
	}
	if os.Getenv("DUMP_PCAPS_INTERVAL") != "" {
		*dumpPcapsInterval = os.Getenv("DUMP_PCAPS_INTERVAL")
	}
	if os.Getenv("DUMP_PCAPS_FILENAME") != "" {
		*dumpPcapsFilename = os.Getenv("DUMP_PCAPS_FILENAME")
	}

	dumpInterval, err := time.ParseDuration(*dumpPcapsInterval)
	if err != nil {
		log.Fatal("Invalid dump-pcaps-interval duration: ", *dumpPcapsInterval)
	}
	service.DumpInterval = dumpInterval
	service.DumpDirectory = *dumpPcaps

	// Parse flush duration parameter (TCP)
	if *flushAfter != "" {
		flushDuration, err := time.ParseDuration(*flushAfter)
		if err != nil {
			log.Fatal("Invalid flush-after duration: ", *flushAfter)
		}

		service.ConnectionTcpTimeout = flushDuration
	}

	// Parse flush duration parameter (UDP)
	if *flushAfterUdp != "" {
		flushDurationUdp, err := time.ParseDuration(*flushAfterUdp)
		if err != nil {
			log.Fatal("Invalid flush-after-udp duration: ", *flushAfterUdp)
		}

		service.ConnectionUdpTimeout = flushDurationUdp
	}

	// Parse flush interval
	if *flushAfter != "" {
		flushIntervalDuration, err := time.ParseDuration(*flushInterval)
		if err != nil {
			log.Fatal("Invalid flush-interval duration: ", *flushInterval)
		}

		service.FlushInterval = flushIntervalDuration
	}

	if !*disableConverters {
		converters.StartWorkers(*concurrentConverters)
	}

	// Pass positional arguments to the pcap handler
	for _, uri := range flag.Args() {
		service.HandlePcapUri(uri)
	}

	// If PCAP-over-IP was configured, connect to it
	// NOTE: Configuring PCAP-over-IP ignores watch dir
	if *pcap_over_ip != "" {
		// for handling multiple pcap over ip
		if strings.Contains(*pcap_over_ip, ",") {
			pcapOverIPs := strings.Split(*pcap_over_ip, ",")
			waitGroup := sync.WaitGroup{}
			waitGroup.Add(len(pcapOverIPs))
			for _, pcapIP := range pcapOverIPs {
				go func(pcapIP string) {
					defer waitGroup.Done()
					connectToPCAPOverIP(service, pcapIP)
				}(pcapIP)
			}

			waitGroup.Wait()
		} else {
			connectToPCAPOverIP(service, *pcap_over_ip)
		}
	} else {
		// If a watch dir was configured, handle all files in the directory, then
		// keep monitoring it for new files.
		if *watch_dir != "" {
			service.WatchDir(*watch_dir)
		}
	}
}

func connectToPCAPOverIP(service *AssemblerService, pcapIP string) {
	for {
		time.Sleep(5 * time.Second)

		log.Println("Connecting to PCAP-over-IP:", pcapIP)

		tcpServer, err := net.ResolveTCPAddr("tcp", pcapIP)
		if err != nil {
			log.Println(err)
			continue
		}

		conn, err := net.DialTCP("tcp", nil, tcpServer)
		if err != nil {
			log.Println(err)
			continue
		}

		pcapFile, err := conn.File()
		if err != nil {
			log.Println(err)
			conn.Close()
			continue
		}

		// Name the file uniquely per connection to not skip packets on reconnect
		sourceName := pcapIP + ":" + fmt.Sprintf("%d", time.Now().Unix())

		log.Println("Connected to PCAP-over-IP:", sourceName)
		service.PcapOverIp = true
		service.HandlePcapFile(pcapFile, sourceName)
		log.Println("Disconnected from PCAP-over-IP:", sourceName)
		conn.Close()
		pcapFile.Close()
	}
}

func (service *AssemblerService) WatchDir(watch_dir string) {
	stat, err := os.Stat(watch_dir)
	if err != nil {
		log.Fatal("Failed to open the watch_dir with error: ", err)
	}

	if !stat.IsDir() {
		log.Fatal("watch_dir is not a directory")
	}

	log.Println("Monitoring dir: ", watch_dir)

	files, err := ioutil.ReadDir(watch_dir)
	if err != nil {
		log.Fatal(err)
	}

	for _, file := range files {
		// accepts files with prefixes that start with .pcap (.pcapng .pcap1 etc)
		if strings.HasPrefix(filepath.Ext(file.Name()), ".pcap") {
			service.HandlePcapUri(filepath.Join(watch_dir, file.Name())) //FIXME; this is a little clunky
		}
	}

	watcher, err := fsnotify.NewWatcher()
	if err != nil {
		log.Fatal(err)
	}

	defer watcher.Close()

	signalChan := make(chan os.Signal, 1)
	signal.Notify(signalChan, os.Interrupt)
	// Keep running until Interrupt
	go func() {
		for {
			select {
			case event, ok := <-watcher.Events:
				if !ok {
					return
				}
				if event.Op&(fsnotify.Rename|fsnotify.Create|fsnotify.Write) != 0 {
					// accepts files with prefixes that start with .pcap (.pcapng .pcap1 etc)
					if strings.HasPrefix(filepath.Ext(event.Name), ".pcap") {
						log.Println("Found new file", event.Name, event.Op.String())
						time.Sleep(2 * time.Second) // FIXME; bit of race here between file creation and writes.
						service.HandlePcapUri(event.Name)
					}
				}
			case err, ok := <-watcher.Errors:
				if !ok {
					return
				}
				log.Println("watcher error:", err)
			}
		}
	}()

	err = watcher.Add(watch_dir)
	if err != nil {
		log.Fatal(err)
	}
	<-signalChan
	log.Println("Watcher stopped")

}

func (service *AssemblerService) HandlePcapUri(sourceName string) {
	var handle *pcap.Handle
	var err error

	if handle, err = pcap.OpenOffline(sourceName); err != nil {
		log.Println("PCAP OpenOffline error:", err)
		return
	}
	defer handle.Close()

	service.ProcessPcapHandle(handle, sourceName)
}

func (service *AssemblerService) HandlePcapFile(file *os.File, sourceName string) {
	var handle *pcap.Handle
	var err error

	if handle, err = pcap.OpenOfflineFile(file); err != nil {
		log.Println("PCAP OpenOfflineFile error:", err)
		return
	}
	defer handle.Close()

	service.ProcessPcapHandle(handle, sourceName)
}

func (service *AssemblerService) ProcessPcapHandle(handle *pcap.Handle, sourceName string) {
	if service.BpfFilter != "" {
		if err := handle.SetBPFFilter(service.BpfFilter); err != nil {
			log.Println("Set BPF Filter error: ", err)
			return
		}
	}

	pcap := g_db.PcapFindOrInsert(sourceName)
	if pcap.Position != 0 {
		log.Println("Skipped", pcap.Position, "packets from", sourceName)
	}

	var source *gopacket.PacketSource
	nodefrag := false
	linktype := handle.LinkType()
	switch linktype {
	case layers.LinkTypeIPv4:
		source = gopacket.NewPacketSource(handle, layers.LayerTypeIPv4)
		break
	default:
		source = gopacket.NewPacketSource(handle, linktype)
	}

	source.Lazy = lazy
	source.NoCopy = true
	count := int64(0)
	bytes := int64(0)
	lastFlush := time.Now()

	signalChan := make(chan os.Signal, 1)
	signal.Notify(signalChan, os.Interrupt)

	service.FlushConnections()
	service.DumpFlush()

	for packet := range source.Packets() {
		// Try flushing connections here. When using PCAP-over-IP this is required, since it treats whole connection as one pcap.
		// NOTE: PCAP-over-IP: pcapOpenOfflineFile is blocking so we need at least see some packets passing by to get here.
		if service.FlushInterval != 0 && lastFlush.Add(service.FlushInterval).Unix() < time.Now().Unix() {
			service.FlushConnections()
			log.Println("Processed", count - pcap.Position, "packets from", sourceName, "(so far)")
			lastFlush = time.Now()
		}

		count++

		// Skip packets that were already processed from this pcap
		if count < pcap.Position + 1 {
			continue
		}

		// PCAP dump
		service.DumpFlush()
		service.DumpPacket(&packet)

		// Replace name with dumped if PCAP-over-IP is enabled to allow downloads
		flowSourceName := sourceName
		if service.DumpFilename != "" && service.PcapOverIp {
			flowSourceName = service.DumpFilename
		}

		data := packet.Data()
		bytes += int64(len(data))
		done := false

		// defrag the IPv4 packet if required
		// (TODO; IPv6 will not be defragged)
		ip4Layer := packet.Layer(layers.LayerTypeIPv4)
		if !nodefrag && ip4Layer != nil {
			ip4 := ip4Layer.(*layers.IPv4)
			l := ip4.Length
			newip4, err := service.Defragmenter.DefragIPv4(ip4)
			if err != nil {
				log.Fatalln("Error while de-fragmenting", err)
			} else if newip4 == nil {
				continue // packet fragment, we don't have whole packet yet.
			}
			if newip4.Length != l {
				pb, ok := packet.(gopacket.PacketBuilder)
				if !ok {
					panic("Not a PacketBuilder")
				}
				nextDecoder := newip4.NextLayerType()
				nextDecoder.Decode(newip4.Payload, pb)
			}
		}

		transport := packet.TransportLayer()
		if transport == nil {
			continue
		}

		switch transport.LayerType() {
		case layers.LayerTypeTCP:
			tcp := transport.(*layers.TCP)
			flow := packet.NetworkLayer().NetworkFlow()
			captureInfo := packet.Metadata().CaptureInfo
			captureInfo.AncillaryData = []interface{}{flowSourceName}
			context := &Context{CaptureInfo: captureInfo}

			if !*skipchecksum {
				// TODO: sijisu: this is broken
				// Compute the checksum
				tcp.SetNetworkLayerForChecksum(packet.NetworkLayer())
				csum, err := tcp.ComputeChecksum()
				if err != nil {
					fmt.Printf("Failed to compute checksum: %s\n", err)
					break
				}
				// check if the checksum is valid
				if csum != tcp.Checksum {
					fmt.Printf("Invalid checksum: 0x%x\n", csum)
					break
				}
			}

			service.AssemblerTcp.AssembleWithContext(flow, tcp, context)
			break
		case layers.LayerTypeUDP:
			udp := transport.(*layers.UDP)
			flow := packet.NetworkLayer().NetworkFlow()
			captureInfo := packet.Metadata().CaptureInfo
			service.AssemblerUdp.Assemble(flow, udp, &captureInfo, flowSourceName)
			break
		default:
			// pass
		}

		select {
		case <-signalChan:
			fmt.Fprintf(os.Stderr, "\nCaught SIGINT: aborting\n")
			done = true
		default:
			// NOP: continue
		}

		if done {
			break
		}
	}

	g_db.PcapSetPosition(pcap.Id, count)
	service.FlushConnections()
	log.Println("Processed", count - pcap.Position, "packets from", sourceName)
}

func (service *AssemblerService) DumpPacket(packet *gopacket.Packet) {
	if service.DumpDirectory == "" {
		return
	}

	if service.DumpWriter == nil {
		now := time.Now()
		service.DumpFilename = filepath.Join(service.DumpDirectory, now.Format(*dumpPcapsFilename))

		// Do this to make sure we dont try to read this pcap with watch-dir
		pcap := g_db.PcapFindOrInsert(service.DumpFilename)
		g_db.PcapSetPosition(pcap.Id, math.MaxInt64)

		file, err := os.Create(service.DumpFilename)
		if err != nil {
			log.Println("Unable to open PCAP file", service.DumpFilename, err)
			return
		}

		service.DumpFile = file
		service.DumpWriter = pcapgo.NewWriter(service.DumpFile)
		service.DumpLast = now
		service.DumpCount = 0

		err = service.DumpWriter.WriteFileHeader(65536, layers.LinkTypeEthernet)
		if err != nil {
			log.Println("Unable to write packet header", err)
			return
		}

		log.Println("Created PCAP file", service.DumpFilename)
	}

	err := service.DumpWriter.WritePacket((*packet).Metadata().CaptureInfo, (*packet).Data())
	if err != nil {
		log.Println("Unable to write packet", err)
		return
	}
	service.DumpCount += 1
}

func (service *AssemblerService) DumpFlush() {
	if service.DumpWriter != nil && time.Now().Unix() > service.DumpLast.Add(service.DumpInterval).Unix() {
		service.DumpFile.Close()
		service.DumpWriter = nil

		log.Println("Closed PCAP file", service.DumpFilename, "with", service.DumpCount, "packets")
	}
}
```

## File: `services/go-importer/cmd/assembler/tags.go`
```go
package main

import (
	"go-importer/internal/pkg/db"

	"log"
	"regexp"

	"github.com/cloudflare/ahocorasick"
)

var flagRegex *regexp.Regexp

func EnsureRegex(reg *string) {
	if flagRegex == nil {
		reg, err := regexp.Compile(*reg)
		if err != nil {
			log.Fatal("Failed to compile flag regex: ", err)
		} else {
			flagRegex = reg
		}
	}
}

func contains(s []string, e string) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

// Apply flag in/flag out tags to the entire flow.
// This assumes the `Data` part of the flowItem is already pre-processed, s.t.
// we can run regex tags over the payload directly
// also add the matched flags to the FlowItem
func ApplyFlagTags(flow *db.FlowEntry, reg *string, flagValidator FlagValidator) {
	EnsureRegex(reg)

	// If the regex is not valid, bail here
	if flagRegex == nil {
		return
	}

	flagsIn := 0
	flagsOut := 0
	for idx := 0; idx < len(flow.Flow); idx++ {
		flowItem := &flow.Flow[idx]
		matches := flagRegex.FindAll(flowItem.Data, -1)

		if len(matches) > 0 {
			var tags []string
			if flowItem.From == "c" {
				tags = append(tags, "flag-in")
				if len(matches) > flagsIn {
					flagsIn = len(matches)
				}
			} else {
				tags = append(tags, "flag-out")
				if len(matches) > flagsOut {
					flagsOut = len(matches)
				}
			}

			hasFakeFlag := false
			for _, match := range matches {
				flag := string(match)
				// Add the flag if it doesn't already exist
				if !contains(flow.Flags, flag) {
					flow.Flags = append(flow.Flags, flag)
				}
				// Check if it is a fake flag
				if !hasFakeFlag && !flagValidator.IsValid(flag, flowItem.Time) {
					tags = append(tags, "fake-flag")
					hasFakeFlag = true
				}
			}

			for _, tag := range tags {
				// Add the tag if it doesn't already exist
				if !contains(flow.Tags, tag) {
					flow.Tags = append(flow.Tags, tag)
				}
			}
		}
	}

	// Different repr may have multiple duplicate flags between each other, so assume that the "max" inside a repr is the most accurate value
	flow.Flags_In += flagsIn
	flow.Flags_Out += flagsOut
}

// Apply flagids to the entire flow.
// This assumes the `Data` part of the flowItem is already pre-processed, s.t.
func ApplyFlagids(flow *db.FlowEntry, flagidsDb []db.FlagId) {

	var flagids []string
	var matches = make(map[int]int)

	for _, flagid := range flagidsDb {
		flagids = append(flagids, flagid.Content)
	}

	matcher := ahocorasick.NewStringMatcher(flagids)
	for idx := 0; idx < len(flow.Flow); idx++ {
		flowItem := &flow.Flow[idx]
		found := matcher.Match([]byte(flowItem.Data))

		if len(found) > 0 {
			var tag string

			if flowItem.From == "c" {
				tag = "flagid-in"
			} else {
				tag = "flagid-out"
			}

			// Add the tag if it doesn't already exist
			if !contains(flow.Tags, tag) {
				flow.Tags = append(flow.Tags, tag)
			}

			for _, match := range found {
				matches[match] = 1
			}
		}
	}

	for match, _ := range matches {
		flow.Flagids = append(flow.Flagids, flagids[match])
	}
}
```

## File: `services/go-importer/cmd/assembler/tcp.go`
```go
// Copyright 2012 Google, Inc. All rights reserved.
//
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file in the root of the source
// tree.

// The pcapdump binary implements a tcpdump-like command line tool with gopacket
// using pcap as a backend data collection mechanism.
package main

import (
	"go-importer/internal/pkg/db"
	"net/netip"

	"sync"

	"github.com/gopacket/gopacket"
	"github.com/gopacket/gopacket/layers"
	"github.com/gopacket/gopacket/reassembly"
)

var allowmissinginit = true
var verbose = false
var debug = false
var quiet = true

/*
 * The TCP factory: returns a new Stream
 */
type TcpStreamFactory struct {
	reassemblyCallback func(db.FlowEntry)
}

func (factory *TcpStreamFactory) New(net, transport gopacket.Flow, tcp *layers.TCP, ac reassembly.AssemblerContext) reassembly.Stream {
	source := ac.GetCaptureInfo().AncillaryData[0].(string);
	fsmOptions := reassembly.TCPSimpleFSMOptions{
		SupportMissingEstablishment: *nonstrict,
	}
	stream := &TcpStream{
		net:                net,
		transport:          transport,
		tcpstate:           reassembly.NewTCPSimpleFSM(fsmOptions),
		optchecker:         reassembly.NewTCPOptionCheck(),
		source:             source,
		FlowItems:          []db.FlowItem{},
		src_port:           tcp.SrcPort,
		dst_port:           tcp.DstPort,
		reassemblyCallback: factory.reassemblyCallback,
	}
	return stream
}

/*
 * The assembler context
 */
type Context struct {
	CaptureInfo gopacket.CaptureInfo
}

func (c *Context) GetCaptureInfo() gopacket.CaptureInfo {
	return c.CaptureInfo
}

/*
 * TCP stream
 */

/* It's a connection (bidirectional) */
type TcpStream struct {
	tcpstate       *reassembly.TCPSimpleFSM
	fsmerr         bool
	optchecker     reassembly.TCPOptionCheck
	net, transport gopacket.Flow
	sync.Mutex
	// RDJ; These field are added to make mongo convertion easier
	source             string
	reassemblyCallback func(db.FlowEntry)
	FlowItems          []db.FlowItem
	src_port           layers.TCPPort
	dst_port           layers.TCPPort
	total_size         int
	num_packets        int
}

func (t *TcpStream) Accept(tcp *layers.TCP, ci gopacket.CaptureInfo, dir reassembly.TCPFlowDirection, nextSeq reassembly.Sequence, start *bool, ac reassembly.AssemblerContext) bool {
	// FSM
	if !t.tcpstate.CheckState(tcp, dir) {
		if !t.fsmerr {
			t.fsmerr = true
		}
		if !*nonstrict {
			return false
		}
	}

	return true
}

// ReassembledSG is called zero or more times.
// ScatterGather is reused after each Reassembled call,
// so it's important to copy anything you need out of it,
// especially bytes (or use KeepFrom())
func (t *TcpStream) ReassembledSG(sg reassembly.ScatterGather, ac reassembly.AssemblerContext) {
	dir, _, _, _ := sg.Info()
	length, _ := sg.Lengths()
	capInfo := ac.GetCaptureInfo()
	timestamp := capInfo.Timestamp
	t.num_packets += 1

	// Don't add empty streams to the DB
	if length == 0 {
		return
	}

	data := sg.Fetch(length)

	// We have to make sure to stay under the document limit
	t.total_size += length
	bytes_available := (*maxFlowItemSize * 1024 * 1024) - t.total_size
	if length > bytes_available {
		length = bytes_available
	}
	if length < 0 {
		length = 0
	}
	data = data[:length]

	var from string
	if dir == reassembly.TCPDirClientToServer {
		from = "c"
	} else {
		from = "s"
	}

	// consolidate subsequent elements from the same origin
	l := len(t.FlowItems)
	if l > 0 {
		if t.FlowItems[l-1].From == from {
			t.FlowItems[l-1].Data = append(t.FlowItems[l-1].Data, data...)
			// All done, no need to add a new item
			return
		}
	}

	// Add a FlowItem based on the data we just reassembled
	t.FlowItems = append(t.FlowItems, db.FlowItem{
		Kind: "raw",
		From: from,
		Data: data,
		Time: timestamp,
	})
}

// ReassemblyComplete is called when assembly decides there is
// no more data for this Stream, either because a FIN or RST packet
// was seen, or because the stream has timed out without any new
// packet data (due to a call to FlushCloseOlderThan).
// It should return true if the connection should be removed from the pool
// It can return false if it want to see subsequent packets with Accept(), e.g. to
// see FIN-ACK, for deeper state-machine analysis.
func (t *TcpStream) ReassemblyComplete(ac reassembly.AssemblerContext) bool {
	if len(t.FlowItems) == 0 {
		// No point in inserting this element, it has no data and even if we wanted to,
		// we can't timestamp it so the front-end can't display it either
		return false
	}

	src, dst := t.net.Endpoints()
	ip_src, _ := netip.ParseAddr(src.String())
	ip_dst, _ := netip.ParseAddr(dst.String())

	timeStart := t.FlowItems[0].Time
	timeEnd := t.FlowItems[0].Time
	for _, item := range t.FlowItems {
		if timeEnd.Before(item.Time) {
			timeEnd = item.Time
		}
	}

	entry := db.FlowEntry{
		Src_port:    uint16(t.src_port),
		Dst_port:    uint16(t.dst_port),
		Src_ip:      ip_src,
		Dst_ip:      ip_dst,
		Time:        timeStart,
		Duration:    timeEnd.Sub(timeStart),
		Num_packets: t.num_packets,
		Parent_id:   nil,
		Child_id:    nil,
		Tags:        []string { "tcp" },
		Filename:    t.source,
		Flow:        t.FlowItems,
		Size:        t.total_size,
		Flags:       make([]string, 0),
		Flagids:     make([]string, 0),
	}

	t.reassemblyCallback(entry)

	// do not remove the connection to allow last ACK
	return false
}
```

## File: `services/go-importer/cmd/assembler/udp.go`
```go
package main

import (
	"go-importer/internal/pkg/db"

	"time"
	"net/netip"

	"github.com/gopacket/gopacket"
	"github.com/gopacket/gopacket/layers"
)

type UdpAssembler struct {
	Streams map[UdpStreamIdendifier]*UdpStream
}

func NewUdpAssembler() UdpAssembler {
	return UdpAssembler{
		Streams: map[UdpStreamIdendifier]*UdpStream{},
	}
}

func (assembler *UdpAssembler) Assemble(flow gopacket.Flow, udp *layers.UDP, captureInfo *gopacket.CaptureInfo, source string) *UdpStream {
	endpointSrc := flow.Src().FastHash()
	endpointDst := flow.Dst().FastHash()
	portSrc := uint16(udp.SrcPort)
	portDst := uint16(udp.DstPort)
	id := UdpStreamIdendifier{}

	if endpointSrc > endpointDst {
		id.EndpointLower = endpointDst
		id.EndpointUpper = endpointSrc
	} else {
		id.EndpointLower = endpointSrc
		id.EndpointUpper = endpointDst
	}

	if portSrc > portDst {
		id.PortLower = portDst
		id.PortUpper = portSrc
	} else {
		id.PortLower = portSrc
		id.PortUpper = portDst
	}

	stream, ok := assembler.Streams[id]
	if !ok {
		stream = &UdpStream{
			Identifier: id,
			Flow:       flow,
			PortSrc:    udp.SrcPort,
			PortDst:    udp.DstPort,
			Source:     source,
		}

		assembler.Streams[id] = stream
	}

	stream.ProcessSegment(flow, udp, captureInfo)
	return stream
}

func (assembler *UdpAssembler) CompleteOlderThan(threshold time.Time) []*db.FlowEntry {
	flows := make([]*db.FlowEntry, 0)

	for id, stream := range assembler.Streams {
		if stream.LastSeen.Unix() < threshold.Unix() {
			flow := stream.CompleteReassembly()
			if flow != nil {
				flows = append(flows, flow)
			}
			delete(assembler.Streams, id)
		}
	}

	return flows
}

type UdpStreamIdendifier struct {
	EndpointLower uint64
	EndpointUpper uint64
	PortLower     uint16
	PortUpper     uint16
}

type UdpStream struct {
	Identifier  UdpStreamIdendifier
	Flow        gopacket.Flow
	PacketCount uint
	PacketSize  uint
	Items       []db.FlowItem
	PortSrc     layers.UDPPort
	PortDst     layers.UDPPort
	Source      string
	LastSeen    time.Time
}

func (stream *UdpStream) ProcessSegment(flow gopacket.Flow, udp *layers.UDP, captureInfo *gopacket.CaptureInfo) {
	if len(udp.Payload) == 0 {
		return
	}

	from := "s"
	if flow.Dst().FastHash() == stream.Flow.Src().FastHash() {
		from = "c"
	}

	stream.LastSeen = captureInfo.Timestamp
	stream.PacketCount += 1
	stream.PacketSize += uint(len(udp.Payload))

	// We have to make sure to stay under the document limit
	available := uint(*maxFlowItemSize * 1024 * 1024) - stream.PacketSize
	length := uint(len(udp.Payload))
	if length > available {
		length = available
	}
	if length < 0 {
		length = 0
	}

	stream.Items = append(stream.Items, db.FlowItem{
		Kind: "raw",
		From: from,
		Data: udp.Payload[:length],
		Time: captureInfo.Timestamp,
	})
}

func (stream *UdpStream) CompleteReassembly() *db.FlowEntry {
	if len(stream.Items) == 0 {
		return nil
	}

	src, dst := stream.Flow.Endpoints()
	ip_src, _ := netip.ParseAddr(src.String())
	ip_dst, _ := netip.ParseAddr(dst.String())

	timeStart := stream.Items[0].Time
	timeEnd := stream.Items[0].Time
	for _, item := range stream.Items {
		if timeEnd.Before(item.Time) {
			timeEnd = item.Time
		}
	}

	return &db.FlowEntry{
		Src_port:    uint16(stream.PortSrc),
		Dst_port:    uint16(stream.PortDst),
		Src_ip:      ip_src,
		Dst_ip:      ip_dst,
		Time:        timeStart,
		Duration:    timeEnd.Sub(timeStart),
		Num_packets: int(stream.PacketCount),
		Parent_id:   nil,
		Child_id:    nil,
		Tags:        []string{"udp"},
		Filename:    stream.Source,
		Flow:        stream.Items,
		Size:        int(stream.PacketSize),
		Flags:       make([]string, 0),
		Flagids:     make([]string, 0),
	}
}
```

## File: `services/go-importer/cmd/enricher/main.go`
```go
package main

import (
	"go-importer/internal/pkg/db"
	"io"
	"net/netip"

	"bufio"
	"errors"
	"flag"
	"log"
	"os"
	"time"

	"github.com/gofrs/uuid/v5"
	"github.com/tidwall/gjson"
)

var eve_file = flag.String("eve", "", "Eve file to watch for suricata's tags")
var timescale = flag.String("timescale", "", "Timescale connection string (e. g. postgres://usr:pwd@host:5432/tulip)")
var tag_flowbits = flag.Bool("flowbits", true, "Tag flows with their flowbits")
var rescan_period = flag.Int("t", 30, "rescan period (in seconds).")

var g_db *db.Database

func main() {
	flag.Parse()
	if *eve_file == "" {
		log.Fatal("Usage: ./enricher -eve eve.json")
	}

	// If no timescale connection string was supplied, use env variable
	if *timescale == "" {
		*timescale = os.Getenv("TIMESCALE")
	}

	log.Println("Connecting to Timescale:", *timescale, "...")
	g_db = db.NewDatabase(*timescale)

	watchEve(*eve_file)
}

func watchEve(eve_file string) {
	// Do the initial scan
	log.Println("Parsing initial eve contents...")
	ratchet := updateEve(eve_file, 0)

	log.Println("Monitoring eve file: ", eve_file)
	stat, err := os.Stat(eve_file)
	prevSize := int64(0)
	if err == nil {
		prevSize = stat.Size()
	}

	for {
		time.Sleep(time.Duration(*rescan_period) * time.Second)

		new_stat, err := os.Stat(eve_file)
		if err != nil {
			log.Println("Failed to open the eve file with error: ", err)
			continue
		}

		if new_stat.Size() > prevSize {
			log.Println("Eve file was updated. New size:, ", new_stat.Size())
			ratchet = updateEve(eve_file, ratchet)
		}
		prevSize = new_stat.Size()

	}

}

// The eve file was just written to, let's parse some logs!
func updateEve(eve_file string, ratchet int64) int64 {

	// Open a handle to the eve file
	eve_handle, err := os.Open(eve_file)
	if err != nil {
		log.Println("Failed to open the eve file")
		return ratchet
	}
	eve_handle.Seek(ratchet, 0)
	eve_reader := bufio.NewReader(eve_handle)
	defer eve_handle.Close()

	log.Println("Start scanning eve file at offset", ratchet)

	// iterate over each line in the file
	for {
		line, err := eve_reader.ReadString('\n')

		// Found EOF, this line is incomplete
		if err == io.EOF {
			break
		}

		// Something other then EOF, stop and log it
		if err != nil {
			log.Printf("Error reading eve at offset %d: %s\n", ratchet, err)
			break
		}

		err = handleEveLine(line)

		// Line was successfully parsed, continue from the next one
		if err == nil {
			ratchet += int64(len(line))
		}

		// Line parsing failed. Line is corrupt
		// Since we only get here if the line was complete (we did not read EOF before newline),
		// we can simply skip this line. Rescaning it will not help.
		if err != nil {
			log.Printf("Error parsing eve at offset %d: %s\n", ratchet, err)
			ratchet += int64(len(line))
		}
	}

	// Roll the eve handle back to the last successfully applied rule, so it can continue there
	// next time this function is called.
	return ratchet
}

/*
	{
		"timestamp": "2022-05-17T19:39:57.283547+0000",
		"flow_id": 1905964640824789,
		"in_iface": "eth0",
		"event_type": "alert",
		"src_ip": "131.155.9.104",
		"src_port": 53604,
		"dest_ip": "165.232.89.44",
		"dest_port": 1337,
		"protobufs": "TCP",
		"pkt_src": "stream (flow timeout)",
		"alert": {
			"action": "allowed",
			"gid": 1,
			"signature_id": 1338,
			"rev": 1,
			"signature": "Detected too many A's (smart)",
			"category": "",
			"severity": 3
		},
		"app_proto": "failed",
		"flow": {
			"pkts_toserver": 6,
			"pkts_toclient": 6,
			"bytes_toserver": 437,
			"bytes_toclient": 477,
			"start": "2022-05-17T19:37:02.978389+0000"
		}
	}
*/

func handleEveLine(json string) error {
	if !gjson.Valid(json) {
		return errors.New("Invalid json in eve line")
	}

	// TODO; error check this
	src_port := gjson.Get(json, "src_port")
	src_ip := gjson.Get(json, "src_ip")
	dst_port := gjson.Get(json, "dest_port")
	dst_ip := gjson.Get(json, "dest_ip")
	start_time := gjson.Get(json, "flow.start")

	sig_msg := gjson.Get(json, "alert.signature")
	sig_id := gjson.Get(json, "alert.signature_id")
	sig_action := gjson.Get(json, "alert.action")
	sig_tags := gjson.Get(json, "alert.metadata.tag")
	flowbits := gjson.Get(json, "metadata.flowbits")

	// canonicalize the IP address notation to make sure it matches what the assembler entered
	// into the database.
	// TODO; just assuming these are all valid for now. Should be fine, since this is coming from
	// suricata and is not _really_ user controlled. Might panic in some obscure case though.
	ip_src, _ := netip.ParseAddr(src_ip.String())
	ip_dst, _ := netip.ParseAddr(dst_ip.String())

	// TODO; Double check this, might be broken for non-UTC?
	start_time_obj, _ := time.Parse("2006-01-02T15:04:05.999999999-0700", start_time.String())

	// If no action was taken, there's no need for us to do anything with this line.
	if !(sig_action.Exists() || (flowbits.Exists() && *tag_flowbits)) {
		return nil
	}

	flow_id, _ := g_db.SuricataIdFindFlow(db.SuricataId {
		Src_port: int(src_port.Int()),
		Src_ip:   ip_src,
		Dst_port: int(dst_port.Int()),
		Dst_ip:   ip_dst,
		Time:     start_time_obj,
	})

	if flow_id == uuid.Nil {
		flow_id, _ = g_db.SuricataIdFindFlow(db.SuricataId {
			Dst_port: int(src_port.Int()),
			Dst_ip:   ip_src,
			Src_port: int(dst_port.Int()),
			Src_ip:   ip_dst,
			Time:     start_time_obj,
		})
	}

	// Flow not found
	if flow_id == uuid.Nil {
		return nil
	}

	tags := []string{}
	if sig_tags.Exists() {
		sig_tags.ForEach(func(key, value gjson.Result) bool {
		tags = append(tags, value.String())
			return true
		})
	}

	if sig_action.Exists() {
		sig := db.Signature{
			Id:      int32(sig_id.Int()),
			Message: sig_msg.String(),
			Action:  sig_action.String(),
		}

		tags = append(tags, "suricata")
		if sig.Action == "blocked" {
			tags = append(tags, "blocked")
		}

		g_db.FlowAddSignatures(flow_id, []db.Signature{sig})
	}

	if flowbits.Exists() && *tag_flowbits {
		flowbits.ForEach(func(key, value gjson.Result) bool {
			tags = append(tags, value.String())
			return true // keep iterating
		})
	}

	g_db.FlowAddTags(flow_id, tags)

	if len(tags) > 0 {
		log.Println("Applied", tags, "tags to flow", flow_id)
	}

	return nil
}
```

## File: `services/go-importer/converters/b64decode.py`
```python
#!/usr/bin/env python3

# TODO: add license notice from https://github.com/spq/pkappa2

import base64
import binascii
import re
from helpers import Converter, StreamChunk, Result, Stream

class Base64DecodeConverter(Converter):

    def __init__(self):
        super().__init__()
        self._pattern = re.compile(
            rb"([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?")

    def decode_possible_base64(self, data: bytes) -> bytes:
        content = b''
        pos = 0
        for match in self._pattern.finditer(data):
            content += data[pos:match.start()]

            # Some heuristics to determine if the data is base64 encoded
            chunk = match.group(0).decode()
            uppercase = len(list(filter(lambda c: c.isupper(), chunk)))
            lowercase = len(list(filter(lambda c: c.islower(), chunk)))
            digits = len(list(filter(lambda c: c.isdigit(), chunk)))

            if uppercase > 0 and lowercase > 0 and digits > 0:
                try:
                    content += base64.b64decode(match.group(0))
                except binascii.Error:
                    content += data[match.start():match.end()]
            else:
                content += data[match.start():match.end()]
            pos = match.end()
        content += data[pos:]
        return content

    def handle_stream(self, stream: Stream) -> Result:
        result_data = []
        for chunk in stream.Chunks:
            content = self.decode_possible_base64(chunk.Content)
            result_data.append(StreamChunk(chunk.Direction, content))
        return Result(result_data)


if __name__ == "__main__":
    Base64DecodeConverter().run()
```

## File: `services/go-importer/converters/dns.py`
```python
#!/usr/bin/env python3
from helpers import Converter, Result, Stream, StreamChunk
from dnslib import DNSRecord

# TODO: add license notice from https://github.com/spq/pkappa2

class DNSConverter(Converter):

    def handle_stream(self, stream: Stream) -> Result:
        result_data = []
        for chunk in stream.Chunks:
            try:
                dns = DNSRecord.parse(chunk.Content)
                result_data.append(
                    StreamChunk(chunk.Direction,
                                str(dns).encode() + b'\n'))
            except Exception as ex:
                result_data.append(
                    StreamChunk(chunk.Direction,
                                str(ex).encode() + b'\n' + chunk.Content))
        return Result(result_data)


if __name__ == "__main__":
    DNSConverter().run()
```

## File: `services/go-importer/converters/grpc.py`
```python
#!/usr/bin/env python3
from collections import defaultdict
from io import BytesIO
import re
from struct import unpack
from typing import Dict, List
import zlib

from http2 import HTTP2Converter, HeaderTuple
from helpers import Direction, Result, Stream
import hyperframe.frame
from protobuf_inspector.types import StandardParser

# TODO: add license notice from https://github.com/spq/pkappa2
# TODO: Support for gRPC-Web https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-WEB.md


class GRPCConverter(HTTP2Converter):

    _stream_content_type: Dict[int, Dict[Direction, bool]]
    _stream_responded_grpc_once: bool
    _stream_encoding: Dict[int, Dict[Direction, str]]

    def __init__(self):
        super().__init__()
        self._ansi_escape = re.compile(
            r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

        self.SETTINGS_NAMES.update({
            65027:
            'GRPC_ALLOW_TRUE_BINARY_METADATA',
            65028:
            'GRPC_PREFERRED_RECEIVE_CRYPTO_FRAME_SIZE'
        })

    def is_valid_encoding(self, encoding: str) -> bool:
        return encoding.lower() in ["identity", "deflate", "gzip"]

    def handle_encoding(self, encoding: str, message_data: bytes) -> bytes:
        encoding = encoding.lower()
        if encoding == "identity":
            return message_data
        elif encoding == "deflate":
            try:
                deflate = zlib.decompressobj(wbits=15)
                return deflate.decompress(message_data)
            except:
                return message_data
        elif encoding == "gzip":
            try:
                deflate = zlib.decompressobj(wbits=15 | 16)
                return deflate.decompress(message_data)
            except:
                return message_data
        else:
            raise ValueError(f"Unknown encoding '{encoding}'")

    def handle_http2_headers(self, direction: Direction,
                             frame: hyperframe.frame.Frame,
                             headers: List[HeaderTuple]) -> None:
        # extract content-type and check if it is grpc
        content_type = next((x[1] for x in headers if x[0] == "content-type"),
                            None)
        if content_type is not None:
            self._stream_content_type[
                frame.stream_id][direction] = content_type.lower() in [
                    "application/grpc", "application/grpc+proto"
                ]
        if self._stream_content_type[frame.stream_id][
                direction] and direction == Direction.SERVERTOCLIENT:
            self._stream_responded_grpc_once = True

        # extract encoding for compression
        # https://github.com/grpc/grpc/blob/master/doc/compression.md
        encoding = next((x[1] for x in headers if x[0] == "grpc-encoding"),
                        None)
        if encoding is not None:
            self._stream_encoding[frame.stream_id][direction] = encoding

    def handle_http2_event(self, direction: Direction,
                           frame: hyperframe.frame.Frame) -> bytes:
        # https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md

        # FIXME: DATA frame boundaries have no relation to Length-Prefixed-Message
        #        boundaries and implementations should make no assumptions about
        #        their alignment.
        #        Do we need to care about this?
        if isinstance(frame, hyperframe.frame.DataFrame):
            # only look at grpc frames
            if frame.stream_id not in self._stream_content_type \
            or not self._stream_content_type[frame.stream_id][direction]:
                # Some servers only send a content-type header in the first
                # response frame in a http2 connection.
                # If we haven't seen a content-type header yet, we assume that
                # the stream is not grpc.
                if direction == Direction.SERVERTOCLIENT and not self._stream_responded_grpc_once:
                    return super().handle_http2_event(direction, frame)

            if len(frame.data) == 0:
                return super().handle_http2_event(direction, frame)

            encoding = "identity"
            if frame.stream_id in self._stream_encoding and direction in self._stream_encoding[
                    frame.stream_id]:
                encoding = self._stream_encoding[frame.stream_id][direction]

            try:
                if len(frame.data) < 5:
                    raise ValueError("Data length is less than 5 bytes")
                output = str(frame).encode()
                compressed_flag = frame.data[0]
                if compressed_flag != 0 and not self.is_valid_encoding(
                        encoding):
                    raise NotImplementedError(
                        "Compressed grpc data is not supported")
                message_length = unpack(">I", frame.data[1:5])[0]
                message_data = frame.data[5:message_length + 5]
                if len(message_data) != message_length:
                    raise ValueError(
                        "Message length does not match the length of the message data"
                    )
                if len(frame.data) > message_length + 5:
                    raise ValueError(
                        "Message data is longer than the message length")
                if compressed_flag != 0:
                    message_data = self.handle_encoding(encoding, message_data)
                output += f"\nGRPC-Compressed: {compressed_flag}\n".encode()
                output += f"GRPC-Message-Length: {message_length}".encode()
                protobuf_message = ""
                if message_data:
                    parser = StandardParser()
                    frame_data = BytesIO(message_data)
                    protobuf_message = parser.parse_message(
                        frame_data, "message")
                output += b"\n" + self._ansi_escape.sub(
                    '', protobuf_message).encode()
                return output + b'\n'
            except Exception as ex:
                return str(ex).encode() + b'\n' + super().handle_http2_event(
                    direction, frame)

        return super().handle_http2_event(direction, frame)

    def handle_stream(self, stream: Stream) -> Result:
        self._stream_content_type = defaultdict(lambda: defaultdict(bool))
        self._stream_responded_grpc_once = False
        self._stream_encoding = defaultdict(lambda: defaultdict(str))
        return super().handle_stream(stream)


if __name__ == "__main__":
    GRPCConverter().run()
```

## File: `services/go-importer/converters/http2.py`
```python
#!/usr/bin/env python3
from base64 import urlsafe_b64decode
from collections import defaultdict
from typing import Dict, List, Optional
import h2.frame_buffer
from h2.exceptions import H2Error
import hyperframe.frame
from hpack import Decoder, HeaderTuple
from http_gzip import HTTPConverter, HTTPRequest, HTTPResponse
from helpers import StreamChunk, Direction, Result, Stream

# TODO: add license notice from https://github.com/spq/pkappa2
# pip install h2


class HTTP2Converter(HTTPConverter):

    SETTINGS_NAMES = {
        1: "HEADER_TABLE_SIZE",
        2: "ENABLE_PUSH",
        3: "MAX_CONCURRENT_STREAMS",
        4: "INITIAL_WINDOW_SIZE",
        5: "MAX_FRAME_SIZE",
        6: "MAX_HEADER_LIST_SIZE",
    }

    hpack_decoder: Dict[Direction, Decoder]

    def __init__(self):
        super().__init__()
        self.h2_client_buffer = None
        self.h2_server_buffer = None
        self.h2_active = False

    def handle_http2_event(self, direction: Direction,
                           frame: hyperframe.frame.Frame) -> bytes:
        return self.format_http2_frame(direction, frame)

    # Avoid decoding the headers multiple times.
    def handle_http2_headers(self, direction: Direction,
                             frame: hyperframe.frame.Frame,
                             headers: List[HeaderTuple]) -> None:
        pass

    def format_http2_frame(self, direction: Direction,
                           frame: hyperframe.frame.Frame) -> bytes:
        if isinstance(
                frame,
            (hyperframe.frame.HeadersFrame, hyperframe.frame.PushPromiseFrame,
             hyperframe.frame.ContinuationFrame)):
            if 'END_HEADERS' not in frame.flags:
                raise Exception('TODO: Handle fragmented headers')
            headers = self.hpack_decoder[direction].decode(frame.data)
            self.handle_http2_headers(direction, frame, headers)
            output = ''
            for header in headers:
                output += f"{header[0]}: {header[1]}\n"
            return f"{frame}\n{output}".encode()
        elif isinstance(frame, hyperframe.frame.DataFrame):
            return str(frame).encode() + b"\n" + frame.data + b"\n"
        elif isinstance(frame, hyperframe.frame.SettingsFrame):
            settings = {
                self.SETTINGS_NAMES.get(k, k): v
                for k, v in frame.settings.items()
            }
            # TODO: Update hpack decoder MAX_HEADER_LIST_SIZE with setting. The values only take effect after an ACK.
            output = ''
            for k, v in settings.items():
                output += f"{k}: {v}\n"
            return f"{type(frame).__name__}(stream_id={frame.stream_id}, flags={frame.flags!r}):\n{output}".encode(
            )
        return (str(frame) + "\n").encode()

    def setup_http2_buffers(self):
        self.h2_server_buffer = h2.frame_buffer.FrameBuffer(server=True)
        self.h2_server_buffer.max_frame_size = 16384
        self.h2_client_buffer = h2.frame_buffer.FrameBuffer(server=False)
        self.h2_client_buffer.max_frame_size = 16384

    def handle_http2_upgrade(self, request: HTTPRequest) -> List[StreamChunk]:
        self.setup_http2_buffers()
        settings = request.headers.get("HTTP2-Settings")
        if settings:
            f = hyperframe.frame.SettingsFrame(0)
            f.parse_body(urlsafe_b64decode(settings))
            return [
                StreamChunk(
                    Direction.CLIENTTOSERVER,
                    self.handle_http2_event(Direction.CLIENTTOSERVER, f) +
                    b"\n")
            ]
        return []

    def handle_http2_init(self, chunk: bytes) -> List[StreamChunk]:
        self.setup_http2_buffers()
        self.h2_active = True
        return self.handle_http2_request(chunk)

    def handle_http2_request(self, chunk: bytes) -> List[StreamChunk]:
        if not self.h2_server_buffer:
            return [StreamChunk(Direction.CLIENTTOSERVER, chunk)]
        self.h2_server_buffer.add_data(chunk)
        # TODO: Update max_frame_size when observing SETTINGS frames updating it
        events = []
        for event in self.h2_server_buffer:
            events.append(
                StreamChunk(
                    Direction.CLIENTTOSERVER,
                    self.handle_http2_event(Direction.CLIENTTOSERVER, event) +
                    b"\n"))
        return events

    def handle_http2_response(self, chunk: bytes) -> List[StreamChunk]:
        if not self.h2_client_buffer:
            return [StreamChunk(Direction.SERVERTOCLIENT, chunk)]
        self.h2_active = True
        self.h2_client_buffer.add_data(chunk)
        events = []
        for event in self.h2_client_buffer:
            events.append(
                StreamChunk(
                    Direction.SERVERTOCLIENT,
                    self.handle_http2_event(Direction.SERVERTOCLIENT, event) +
                    b"\n"))
        return events

    def handle_raw_client_chunk(
            self, chunk: StreamChunk) -> Optional[List[StreamChunk]]:
        try:
            if self.h2_active:
                return self.handle_http2_request(chunk.Content)

            if chunk.Content.startswith(b"PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n"):
                # HTTP/2
                return self.handle_http2_init(chunk.Content)
        except H2Error as ex:
            data = f"Unable to parse HTTP2 init request: {ex}".encode()
            return [StreamChunk(chunk.Direction, data)]
        # continue parsing HTTP/1 request
        return super().handle_raw_client_chunk(chunk)

    def handle_raw_server_chunk(
            self, chunk: StreamChunk) -> Optional[List[StreamChunk]]:
        if self.h2_active:
            # HTTP/2
            try:
                return self.handle_http2_response(chunk.Content)
            except H2Error as ex:
                data = f"Unable to parse HTTP2 response: {ex}".encode()
                return [StreamChunk(chunk.Direction, data)]
        # continue parsing HTTP/1 response
        return super().handle_raw_server_chunk(chunk)

    def handle_http1_request(self, chunk: StreamChunk,
                             request: HTTPRequest) -> List[StreamChunk]:

        # https://httpwg.org/specs/rfc7540.html#discover-http
        connection = request.headers.get("Connection")
        if connection:
            connection_headers = list(
                map(lambda h: h.strip(), connection.split(",")))
            if "Upgrade" in connection_headers and request.headers.get(
                    "Upgrade") == "h2c":
                # HTTP/2
                return [chunk] + self.handle_http2_upgrade(request)

        return super().handle_http1_request(chunk, request)

    def handle_http1_response(self, header: bytes, body: bytes,
                              chunk: StreamChunk,
                              response: HTTPResponse) -> List[StreamChunk]:

        if response.headers.get(
                "Connection") == "Upgrade" and response.headers.get(
                    "Upgrade") == "h2c":
            # HTTP/2
            if self.h2_server_buffer is None:
                raise Exception("HTTP/2 upgrade request not found")

            return [StreamChunk(chunk.Direction, header + b'\r\n\r\n')
                    ] + self.handle_http2_response(response.data)

        return super().handle_http1_response(header, body, chunk, response)

    def handle_stream(self, stream: Stream) -> Result:
        self.h2_active = False
        self.h2_client_buffer = None
        self.hpack_decoder = defaultdict(Decoder)
        self.h2_server_buffer = None
        if len(stream.Chunks) > 1 and stream.Chunks[
                0].Direction == Direction.SERVERTOCLIENT:
            # the server send something before the request arrived?!
            # try to fix it by switching the first and second chunk transparently.
            return super().handle_stream(
                Stream(
                    stream.Metadata, stream.Chunks[1:2] + stream.Chunks[0:1] +
                    stream.Chunks[2:]))
        return super().handle_stream(stream)


if __name__ == "__main__":
    HTTP2Converter().run()
```

## File: `services/go-importer/converters/http_gzip.py`
```python
#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler
from http.client import parse_headers
from io import BytesIO
from typing import List, Optional
from urllib3 import HTTPResponse
from helpers import Converter, StreamChunk, Direction, Result, Stream
import traceback

# TODO: add license notice from https://github.com/spq/pkappa2
# https://stackoverflow.com/questions/4685217/parse-raw-http-headers
class HTTPRequest(BaseHTTPRequestHandler):

    def __init__(self, request_text: str):
        self.rfile = BytesIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message


class HTTPConverter(Converter):

    def handle_raw_client_chunk(
            self, chunk: StreamChunk) -> Optional[List[StreamChunk]]:
        """
        Handle raw client chunk. Return None to continue parsing HTTP1 request.

        Args:
            chunk (StreamChunk): Raw client chunk.
        
        Returns:
            Optional[List[StreamChunk]]: List of chunks to be added to the result.
        """
        return None

    def handle_raw_server_chunk(
            self, chunk: StreamChunk) -> Optional[List[StreamChunk]]:
        return None

    def handle_http1_request(self, chunk: StreamChunk,
                             request: HTTPRequest) -> List[StreamChunk]:

        # Just pass HTTP1 requests through untouched
        return [StreamChunk(chunk.Direction, chunk.Content)]

    def handle_http1_response(self, header: bytes, body: bytes,
                              chunk: StreamChunk,
                              response: HTTPResponse) -> List[StreamChunk]:

        data = header + b"\r\n\r\n" + response.data
        return [StreamChunk(chunk.Direction, data)]

    def handle_stream(self, stream: Stream) -> Result:

        result_data = []
        for chunk in stream.Chunks:
            if chunk.Direction == Direction.CLIENTTOSERVER:

                raw_result: Optional[
                    List[StreamChunk]] = self.handle_raw_client_chunk(chunk)
                if raw_result is not None:
                    result_data.extend(raw_result)
                    continue

                try:
                    request = HTTPRequest(chunk.Content)
                    if request.error_code:
                        raise Exception(
                            f"{request.error_code} {request.error_message}".
                            encode())

                    result_data.extend(
                        self.handle_http1_request(chunk, request))
                except Exception as ex:
                    data = f"Unable to parse HTTP request: {ex}".encode()
                    result_data.append(StreamChunk(chunk.Direction, data))
            else:
                try:
                    raw_response: Optional[List[
                        StreamChunk]] = self.handle_raw_server_chunk(chunk)
                    if raw_response is not None:
                        result_data.extend(raw_response)
                        continue

                    # https://stackoverflow.com/a/52418392
                    header, body = chunk.Content.split(b"\r\n\r\n", 1)
                    header_stream = BytesIO(header)
                    requestline = header_stream.readline().split(b' ')
                    status = int(requestline[1])
                    headers = parse_headers(header_stream)

                    # tulip: fix the header format, HTTPResponse expects a dict?
                    headers = headers.items()

                    body_stream = BytesIO(body)
                    response = HTTPResponse(
                        body=body_stream,
                        headers=headers,
                        status=status,
                    )

                    result_data.extend(
                        self.handle_http1_response(header, body, chunk,
                                                   response))
                except Exception as ex:
                    data = f"Unable to parse HTTP response: {ex}\n{traceback.format_exc()}".encode()
                    result_data.append(StreamChunk(chunk.Direction, data))
        return Result(result_data)


if __name__ == "__main__":
    HTTPConverter().run()
```

## File: `services/go-importer/converters/protobuf.py`
```python
#!/usr/bin/env python3
import re
from io import BytesIO
from helpers import Converter, Result, Stream, StreamChunk
from protobuf_inspector.types import StandardParser

# TODO: add license notice from https://github.com/spq/pkappa2

class ProtobufConverter(Converter):

    def __init__(self):
        super().__init__()
        self._ansi_escape = re.compile(
            r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    def handle_stream(self, stream: Stream) -> Result:
        result_data = []
        for chunk in stream.Chunks:
            try:
                parser = StandardParser()
                frame_data = BytesIO(chunk.Content)
                protobuf_message = parser.parse_message(frame_data, "message")
                result_data.append(
                    StreamChunk(
                        chunk.Direction,
                        self._ansi_escape.sub('', protobuf_message).encode()))
            except Exception as ex:
                result_data.append(
                    StreamChunk(
                        chunk.Direction, b'Protobuf ERROR: ' +
                        str(ex).encode() + b'\n' + chunk.Content))
        return Result(result_data)


if __name__ == "__main__":
    ProtobufConverter().run()
```

## File: `services/go-importer/converters/pwntools.py`
```python
#!/usr/bin/env python3
from helpers import Converter, StreamChunk, Result, Stream, Direction, Protocol

# TODO: add license notice from https://github.com/spq/pkappa2

class PwntoolsRemoteConverter(Converter):

    def handle_stream(self, stream: Stream) -> Result:
        typ = ''
        if stream.Metadata.Protocol == Protocol.UDP:
            typ = ', typ = "udp"'
        output = f'''#!/usr/bin/env python3
from pwn import *
import sys

# Generated from stream {stream.Metadata.StreamID}
# io = remote(sys.argv[1], {stream.Metadata.ServerPort}{typ})
io = remote({stream.Metadata.ServerHost!r}, {stream.Metadata.ServerPort}{typ})
'''
        for i, chunk in enumerate(stream.Chunks):
            if chunk.Direction == Direction.CLIENTTOSERVER:
                if chunk.Content[-1:] == b'\n':
                    output += f"io.sendline({chunk.Content[:-1]!r})\n"
                else:
                    output += f"io.send({chunk.Content!r})\n"
            else:
                if i == len(stream.Chunks) - 1:
                    output += "io.stream()\n"
                else:
                    output += f"io.recvuntil({chunk.Content[-20:]!r})\n"
        if len(stream.Chunks) > 0 and stream.Chunks[
                -1].Direction == Direction.CLIENTTOSERVER:
            output += "io.interactive()\n"
        return Result([StreamChunk(Direction.CLIENTTOSERVER, output.encode())])


if __name__ == "__main__":
    PwntoolsRemoteConverter().run()
```

## File: `services/go-importer/converters/pythonrequests.py`
```python
#!/usr/bin/env python3
from typing import List
from http_gzip import HTTPConverter, HTTPRequest, HTTPResponse
from helpers import Direction, Result, Stream, StreamChunk

# TODO: add license notice from https://github.com/spq/pkappa2

class PythonRequestsConverter(HTTPConverter):

    requests_output: str
    target_host: str

    SHORTCUT_METHODS = ["get", "post", "put", "delete", "head", "patch"]

    def handle_http1_request(self, chunk: StreamChunk,
                             request: HTTPRequest) -> List[StreamChunk]:

        data = request.rfile.read()
        headers = {}
        for k, v in request.headers.items():
            headers[k] = v
        if request.command.lower() in self.SHORTCUT_METHODS:
            self.requests_output += f'r = s.{request.command.lower()}('
        else:
            self.requests_output += f'r = s.request({request.command!r}, '
        self.requests_output += f'f"http://{self.target_host}{request.path}"'
        if len(headers) > 0:
            self.requests_output += f', headers={headers}'
        if len(data) > 0:
            self.requests_output += f', data={data}'
        self.requests_output += ')\n'

        return []

    # ignore responses
    def handle_http1_response(self, header: bytes, body: bytes,
                              chunk: StreamChunk,
                              response: HTTPResponse) -> List[StreamChunk]:
        return []

    def handle_stream(self, stream: Stream) -> Result:
        self.requests_output = f'''#!/usr/bin/env python3
import requests
import sys

IP = '{stream.Metadata.ServerHost}'
# IP = sys.argv[1]

# Generated from stream {stream.Metadata.StreamID}
s = requests.Session()

'''
        port = ''
        if stream.Metadata.ServerPort != 80:
            port = f':{stream.Metadata.ServerPort}'
        self.target_host = f'{{IP}}{port}'
        result = super().handle_stream(stream)

        return Result(result.Chunks + [
            StreamChunk(Direction.CLIENTTOSERVER,
                        self.requests_output.encode())
        ])


if __name__ == "__main__":
    PythonRequestsConverter().run()
```

## File: `services/go-importer/converters/quic.py`
```python
#!/usr/bin/env python3
from helpers import Direction, Converter, Result, Stream, StreamChunk
from aioquic.quic.connection import dump_cid
from aioquic.quic.crypto import CryptoPair
from aioquic.quic.logger import QuicLoggerTrace
from aioquic.quic.packet import pull_quic_header, PACKET_TYPE_MASK, PACKET_TYPE_INITIAL
from aioquic._buffer import Buffer
from scapy.layers.tls.all import TLS

# TODO: add license notice from https://github.com/spq/pkappa2

class QUICConverter(Converter):

    def handle_stream(self, stream: Stream) -> Result:
        logger = QuicLoggerTrace(is_client=True, odcid=b'1234')
        result_data = []
        connection_id_length = 8
        for chunk in stream.Chunks:
            buf = Buffer(data=chunk.Content)
            while not buf.eof():
                start_off = buf.tell()
                output = ''
                try:
                    header = pull_quic_header(
                        buf, host_cid_length=connection_id_length)

                    output = f'  is_long_header: {header.is_long_header}\n' + \
                                f'  version: {header.version}\n' + \
                                f'  packet_type: {logger.packet_type(header.packet_type)} ({header.packet_type})\n' + \
                                f'  destination_cid: {dump_cid(header.destination_cid)}\n' + \
                                f'  source_cid: {dump_cid(header.source_cid)}\n' + \
                                f'  token: {header.token}\n' + \
                                f'  integrity_tag: {header.integrity_tag}\n' + \
                                f'  rest_length: {header.rest_length}\n'

                    encrypted_off = buf.tell() - start_off
                    end_off = buf.tell() + header.rest_length
                    buf.seek(end_off)

                    if header.packet_type & PACKET_TYPE_MASK == PACKET_TYPE_INITIAL:
                        crypto = CryptoPair()
                        if chunk.Direction == Direction.CLIENTTOSERVER:
                            crypto.setup_initial(header.destination_cid,
                                                 is_client=False,
                                                 version=header.version)
                        else:
                            crypto.setup_initial(header.source_cid,
                                                 is_client=True,
                                                 version=header.version)
                        plain_header, plain_payload, packet_number = crypto.decrypt_packet(
                            chunk.Content[start_off:end_off], encrypted_off, 0)
                        tls = TLS(plain_header + plain_payload)
                        output += f'  plain_header: {plain_header}\n' + \
                                f'  plain_payload: \n{tls.show(dump=True)}\n'
                    else:
                        output += f'  encrypted: {chunk.Content[start_off:end_off]}\n'
                    result_data.append(
                        StreamChunk(chunk.Direction,
                                    output.encode() + b'\n'))
                except Exception as ex:
                    result_data.append(
                        StreamChunk(
                            chunk.Direction,
                            output.encode() + str(ex).encode() + b'\n' +
                            chunk.Content[start_off:] + b'\n'))
                    break

        return Result(result_data)


if __name__ == "__main__":
    QUICConverter().run()
```

## File: `services/go-importer/converters/tls.py`
```python
#!/usr/bin/env python3
from helpers import Converter, Result, Stream, StreamChunk
from scapy.layers.tls.all import TLS

# TODO: add license notice from https://github.com/spq/pkappa2

class TLSConverter(Converter):

    def handle_stream(self, stream: Stream) -> Result:
        result_data = []
        for chunk in stream.Chunks:
            try:
                tls = TLS(chunk.Content)
                result_data.append(
                    StreamChunk(chunk.Direction,
                                tls.show(dump=True).encode()))
            except Exception as ex:
                result_data.append(
                    StreamChunk(chunk.Direction,
                                str(ex).encode() + b'\n' + chunk.Content))

        return Result(result_data)


if __name__ == "__main__":
    TLSConverter().run()
```

## File: `services/go-importer/converters/websockets.py`
```python
#!/usr/bin/env python3
from base64 import b64encode
from collections import defaultdict
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from hashlib import sha1
import zlib
import traceback

from http2 import HTTP2Converter, HTTPRequest, HTTPResponse, HeaderTuple
import hyperframe.frame
from helpers import StreamChunk, Direction, Result, Stream

# TODO: add license notice from https://github.com/spq/pkappa2

@dataclass
class WebsocketFrame:
    Direction: Direction
    Header: bytearray
    Data: bytearray


class WebsocketConverter(HTTP2Converter):

    websocket_key: Union[bytes, None]
    switched_protocols: bool
    websocket_deflate: Dict[int, bool]
    websocket_deflate_decompressor: Dict[int, Dict[Direction, Any]]
    websocket_message_fragmented_frames: Dict[int, List[WebsocketFrame]]
    websocket_enable_connect_protocol: bool
    websocket_stream: Dict[int, bool]

    def __init__(self):
        super().__init__()
        self.SETTINGS_NAMES.update({
            8: 'ENABLE_CONNECT_PROTOCOL',
        })

    def unmask_websocket_frames(self, frame: WebsocketFrame) -> WebsocketFrame:
        # this frame is unmasked
        if frame.Header[1] & 0x80 == 0:
            return frame

        unmasked = [
            frame.Data[4 + i] ^ frame.Data[i % 4]
            for i in range(len(frame.Data) - 4)
        ]
        # remove mask bit
        frame.Header[1] = frame.Header[1] & 0x7F
        return WebsocketFrame(frame.Direction, frame.Header,
                              bytearray(unmasked))

    def handle_websocket_permessage_deflate(
            self, stream_id: int,
            frame: WebsocketFrame) -> Union[WebsocketFrame, None]:
        opcode = frame.Header[0] & 0x0F
        # control frames are not compressed
        if opcode & 0x08 != 0:
            return frame

        # handle fragmented messages
        if frame.Header[0] & 0x80 == 0:  # FIN bit not set
            self.websocket_message_fragmented_frames[stream_id].append(frame)
            if len(self.websocket_message_fragmented_frames
                   ) > 0 and opcode != 0:
                self.websocket_message_fragmented_frames = []
                raise Exception("Invalid fragmented message")
            if len(self.websocket_message_fragmented_frames
                   ) > 50:  # arbitrary limit
                self.websocket_message_fragmented_frames = []
                raise Exception("Fragmented message too long")
            return None

        if len(self.websocket_message_fragmented_frames) > 0:
            if opcode != 0:
                self.websocket_message_fragmented_frames = []
                raise Exception("Invalid fragmented message")
            # this is the last frame of a fragmented message
            self.websocket_message_fragmented_frames[stream_id].append(frame)
            frame = WebsocketFrame(
                Direction=frame.Direction,
                Header=self.websocket_message_fragmented_frames[stream_id]
                [0].Header,
                Data=bytearray(b''.join([
                    f.Data for f in
                    self.websocket_message_fragmented_frames[stream_id]
                ])))
            frame.Header[0] |= 0x80  # set FIN bit
            # datalength in the header is wrong now, but we don't care
            self.websocket_message_fragmented_frames = []

        # only the first frame of a fragmented message has the RSV1 bit set
        if frame.Header[
                0] & 0x40 == 0:  # RSV1 "Per-Message Compressed" bit not set
            return frame

        data = frame.Data + b'\x00\x00\xff\xff'
        data = self.websocket_deflate_decompressor[stream_id][
            frame.Direction].decompress(data)
        frame.Header[0] = frame.Header[0] & 0xBF  # remove RSV1 bit
        return WebsocketFrame(frame.Direction, frame.Header, bytearray(data))

    def handle_websocket_frame(self, frame: WebsocketFrame) -> WebsocketFrame:
        """
        Handle a websocket frame and possibly return a new frame.
        Use this to implement custom websocket protocols.

        Args:
            chunk (StreamChunk): The chunk that contains the frame
            frame (WebsocketFrame): The frame to handle

        Returns:
            WebsocketFrame: The frame to send to display. Header and Body concatenated.
        """
        return frame

    def handle_websocket_frames(self, direction: Direction, stream_id: int,
                                content: bytes) -> bytes:
        try:
            frames: List[bytes] = []
            frame = bytearray(content)
            while len(frame) > 0:
                data_length = frame[1] & 0x7F
                mask_offset = 2
                if data_length == 126:
                    mask_offset = 4
                    data_length = int.from_bytes(frame[2:4], byteorder="big")
                elif data_length == 127:
                    mask_offset = 10
                    data_length = int.from_bytes(frame[2:10], byteorder="big")

                data_offset = mask_offset
                # frame masked?
                if frame[1] & 0x80 != 0:
                    data_offset += 4

                websocket_frame = WebsocketFrame(
                    Direction=direction,
                    Header=frame[:mask_offset],
                    Data=frame[mask_offset:data_offset + data_length])
                websocket_frame = self.unmask_websocket_frames(websocket_frame)
                if self.websocket_deflate:
                    websocket_frame = self.handle_websocket_permessage_deflate(
                        stream_id, websocket_frame)
                    if websocket_frame is None:
                        continue

                websocket_frame = self.handle_websocket_frame(websocket_frame)

                frames.append(websocket_frame.Header +
                              bytes(websocket_frame.Data))
                frame = frame[data_offset + data_length:]
            return b''.join(frames)
        except Exception as ex:
            self.log(f"Error while handling websocket frame: {ex}")
            self.log(traceback.format_exc())

            raise Exception(
                f"Error while handling websocket frame: {ex}") from ex

    def handle_permessage_deflate_extension(
            self, stream_id: int,
            websocket_deflate_parameters: Dict[str, Union[bool, str]]) -> None:
        self.websocket_deflate[stream_id] = True
        self.websocket_message_fragmented_frames[stream_id] = []
        window_bits = 15
        if 'server_max_window_bits' in websocket_deflate_parameters:
            window_bits = int(
                websocket_deflate_parameters['server_max_window_bits'])
        self.websocket_deflate_decompressor[stream_id][
            Direction.SERVERTOCLIENT] = zlib.decompressobj(wbits=-window_bits)
        window_bits = 15
        if 'client_max_window_bits' in websocket_deflate_parameters:
            window_bits = int(
                websocket_deflate_parameters['client_max_window_bits'])
        self.websocket_deflate_decompressor[stream_id][
            Direction.CLIENTTOSERVER] = zlib.decompressobj(wbits=-window_bits)

    def decode_websocket_extensions(
            self,
            extensions_header: str) -> Dict[str, Dict[str, Union[bool, str]]]:
        extensions: Dict[str, Dict[str, Union[str, bool]]] = {}
        if extensions_header:
            raw_extensions = map(lambda s: s.strip().lower(),
                                 extensions_header.split(","))
            for extension in raw_extensions:
                extension, raw_params = extension.split(
                    ";", 1) if ";" in extension else (extension, '')
                params: Dict[str, Union[str, bool]] = {}
                raw_params = filter(
                    lambda p: len(p) != 0,
                    map(lambda p: p.strip(), raw_params.split(";")))
                for param in raw_params:
                    param = param.split("=", 1)
                    if len(param) == 1:
                        params[param[0]] = True
                    else:
                        if param[1].startswith('"') and param[1].endswith('"'):
                            param[1] = param[1][1:-1]
                        params[param[0]] = param[1]
                extensions[extension] = params
        return extensions

    def handle_http2_headers(self, direction: Direction,
                             frame: hyperframe.frame.Frame,
                             headers: List[HeaderTuple]) -> None:
        if not self.websocket_enable_connect_protocol or direction != Direction.CLIENTTOSERVER:
            return

        # The client wants to use the extended CONNECT protocol
        # using the ":protocol" pseudo header.
        protocol = None
        scheme = None
        extensions_header = None
        for header in headers:
            if header[0] == ":protocol":
                protocol = header[1].decode()
            elif header[0] == ":scheme":
                scheme = header[1].decode()
            elif header[0] == "sec-websocket-extensions":
                extensions_header = header[1].decode()

        # The client doesn't want to use the extended CONNECT protocol
        if protocol is None:
            return

        if protocol != "websocket":
            return

        # I doubt we'll see "https" yet, but let's be prepared
        if scheme not in ["http", "https"]:
            return

        # Decode extensions header
        if extensions_header is not None:
            # sec-websocket-extensions: extension-name; param1=value1; param2="value2", extension-name2; param1, extension-name3, extension-name4; param1=value1
            extensions = self.decode_websocket_extensions(extensions_header)
            if "permessage-deflate" in extensions:
                self.handle_permessage_deflate_extension(
                    frame.stream_id, extensions["permessage-deflate"])
            elif len(extensions) > 0:
                self.log(f"Unsupported extensions: {extensions}")

        # Switch this stream to websocket mode
        self.websocket_stream[frame.stream_id] = True

    def handle_http2_event(self, direction: Direction,
                           frame: hyperframe.frame.Frame) -> bytes:
        if isinstance(frame, hyperframe.frame.SettingsFrame):
            if direction != Direction.SERVERTOCLIENT or frame.settings.get(
                    frame.ENABLE_CONNECT_PROTOCOL, 0) == 0:
                return super().handle_http2_event(direction, frame)

            # The client can use the extended CONNECT protocol
            # using the ":protocol" pseudo header.
            self.websocket_enable_connect_protocol = True
        elif isinstance(frame, hyperframe.frame.DataFrame):
            if not self.websocket_stream[frame.stream_id]:
                return super().handle_http2_event(direction, frame)

            return self.handle_websocket_frames(direction, frame.stream_id,
                                                frame.data)

        return super().handle_http2_event(direction, frame)

    def handle_raw_client_chunk(
            self, chunk: StreamChunk) -> Optional[List[StreamChunk]]:
        try:
            if self.switched_protocols:
                return [
                    StreamChunk(
                        chunk.Direction,
                        self.handle_websocket_frames(chunk.Direction, 0,
                                                     chunk.Content))
                ]
            return super().handle_raw_client_chunk(chunk)
        except Exception as ex:
            return [StreamChunk(chunk.Direction, str(ex).encode())]

    def handle_raw_server_chunk(
            self, chunk: StreamChunk) -> Optional[List[StreamChunk]]:
        try:
            if self.switched_protocols:
                return [
                    StreamChunk(
                        chunk.Direction,
                        self.handle_websocket_frames(chunk.Direction, 0,
                                                     chunk.Content))
                ]
            return super().handle_raw_server_chunk(chunk)
        except Exception as ex:
            return [StreamChunk(chunk.Direction, str(ex).encode())]

    def handle_http1_request(self, chunk: StreamChunk,
                             request: HTTPRequest) -> List[StreamChunk]:
        # tulip: Connection: keep-alive, Upgrade is also valid for websocket traffic
        if "Upgrade" in request.headers.get(
                "Connection") and request.headers.get(
                    "Upgrade") == "websocket":
            websocket_key = request.headers.get("Sec-WebSocket-Key", None)
            if websocket_key is None:
                return [
                    StreamChunk(chunk.Direction, b"No websocket key found")
                ]
            self.websocket_key = websocket_key.encode()

        return super().handle_http1_request(chunk, request)

    def handle_http1_response(self, header: bytes, body: bytes,
                              chunk: StreamChunk,
                              response: HTTPResponse) -> List[StreamChunk]:
        try:
            if response.status == 101 and response.headers.get(
                    "Connection").lower(
                    ) == "upgrade" and response.headers.get(
                        "Upgrade").lower() == "websocket":
                if not self.websocket_key:
                    raise Exception("No websocket key found")
                expected_accept = b64encode(
                    sha1(self.websocket_key +
                         b"258EAFA5-E914-47DA-95CA-C5AB0DC85B11").digest()
                ).decode()
                if response.headers.get(
                        "Sec-WebSocket-Accept") != expected_accept:
                    raise Exception(
                        f"Invalid websocket key: {response.headers.get('Sec-WebSocket-Accept')} != {expected_accept}"
                    )
                self.switched_protocols = True

                # Decode extensions header
                # Sec-WebSocket-Extensions: extension-name; param1=value1; param2="value2", extension-name2; param1, extension-name3, extension-name4; param1=value1
                extensions_header = response.headers.get(
                    "Sec-WebSocket-Extensions")
                extensions = self.decode_websocket_extensions(
                    extensions_header)
                if "permessage-deflate" in extensions:
                    self.handle_permessage_deflate_extension(
                        0, extensions["permessage-deflate"])
                elif len(extensions) > 0:
                    self.log(f"Unsupported extensions: {extensions}")

                data = response.data
                if len(data) > 0:
                    data = self.handle_websocket_frames(
                        chunk.Direction, 0, data)

                return [
                    StreamChunk(chunk.Direction, header + b"\r\n\r\n" + data)
                ]

            return super().handle_http1_response(header, body, chunk, response)
        except Exception as ex:
            return [
                StreamChunk(chunk.Direction,
                            f"Unable to parse HTTP response: {ex}".encode())
            ]

    def handle_stream(self, stream: Stream) -> Result:
        # http1
        self.websocket_key = None
        self.switched_protocols = False

        # http2
        self.websocket_enable_connect_protocol = False
        self.websocket_stream = defaultdict(bool)

        # deflate extension
        self.websocket_deflate = defaultdict(bool)
        self.websocket_deflate_decompressor = defaultdict(dict)
        self.websocket_message_fragmented_frames = defaultdict(list)
        return super().handle_stream(stream)


if __name__ == "__main__":
    WebsocketConverter().run()
```

## File: `services/go-importer/converters/helpers/__init__.py`
```python
# TODO: add license notice from https://github.com/spq/pkappa2

from dataclasses import dataclass
from enum import Enum
from typing import List
import traceback
import datetime
import os
import sys
import msgpack


class Protocol(Enum):
    TCP = 0
    UDP = 1


@dataclass
class StreamMetadata:
    StreamID: int
    ClientHost: str
    ClientPort: int
    ServerHost: str
    ServerPort: int
    Protocol: Protocol


class Direction(Enum):
    CLIENTTOSERVER = 0
    SERVERTOCLIENT = 1


@dataclass
class StreamChunk:
    Direction: Direction
    Content: bytes


@dataclass
class Stream:
    Metadata: StreamMetadata
    Chunks: List[StreamChunk]


@dataclass
class Result:
    Chunks: List[StreamChunk]


class Converter:
    """
    Base class for pkappa2 converters.

    Converters are expected to be implemented as a class that inherits from this
    class and implements the handle_stream method. The handle_stream method
    is called for each stream that is passed to the converter. The converter is
    expected to return a Result object that contains the data that should be
    displayed in the UI.
    """

    current_stream_id: int

    def log(self, message: str):
        """
        Log a message to stderr.

        This method can be used to log messages to the UI. The message will be
        displayed in the stderr tab of the UI.

        Can be used for debugging.
        """
        now = datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")
        print(f'{now} (stream: {self.current_stream_id}): {message}',
              flush=True,
              file=sys.stderr)

    def run(self):
        """
        Run the converter.

        This method goes into an endless loop that parses the input from
        pkappa2 and calls the handle_stream method for each stream. The
        result of the handle_stream method is then written to stdout.
        """
        self.current_stream_id = -1
        stdin = os.fdopen(sys.stdin.fileno(), 'rb', buffering=0)
        unpacker = msgpack.Unpacker(stdin, raw=True)

        for data in unpacker:
            try:
                metadata = StreamMetadata(
                    StreamID=0,  # TODO: is this needed?
                    ClientHost=data[b'Src_ip'],
                    ClientPort=data[b'Src_port'],
                    ServerHost=data[b'Dst_ip'],
                    ServerPort=data[b'Dst_port'],
                    Protocol=Protocol.TCP,
                )

                self.current_stream_id = metadata.StreamID
                stream_chunks = []
                for chunk in data[b'Flow']:
                    stream_chunks.append(StreamChunk(
                        Content=chunk[b'Data'],
                        Direction=Direction.CLIENTTOSERVER if chunk[b'From'] == b'c' else Direction.SERVERTOCLIENT,
                    ))

                stream = Stream(metadata, stream_chunks)
                result = self.handle_stream(stream)

                formatted_chunks = []
                for chunk in result.Chunks:
                    formatted_chunks.append({
                        'From': 'c' if chunk.Direction == Direction.CLIENTTOSERVER else 's',
                        'Data': chunk.Content,
                    })

                # Naive implementation of checking if it looks like the output data changed at all, if it seems
                # like it didn't, avoid showing it
                # TODO: is just comparing full payload a good idea? should it be implemented on converter-level instead?
                changed = False
                if len(stream_chunks) != len(formatted_chunks):
                    changed = True
                else:
                    for stream_chunk, formatted_chunk in zip(stream_chunks, formatted_chunks):
                        if len(stream_chunk.Content) != len(formatted_chunk['Data']):
                            changed = True
                            break

                sys.stdout.buffer.write(
                    msgpack.packb(formatted_chunks if changed else [], use_bin_type=True)
                )
                sys.stdout.buffer.flush()
            except KeyboardInterrupt:
                return
            except Exception as e:
                print(f'Ran into an exception: {e}\n{traceback.format_exc()}', file=sys.stderr, flush=True)
                sys.stdout.buffer.write(
                    msgpack.packb([], use_bin_type=True)
                )
                sys.stdout.buffer.flush()

    def handle_stream(self, stream: Stream) -> Result:
        """
        Transform the data of a stream and return the changed stream.
        The stream contains metadata of the source and target and a list of
        chunks of data. Each chunk contains the direction of the data and the
        data itself. The data is a byte array.

        This method is called for each stream that is passed to the converter.

        Args:
            stream: The stream to transform.

        Returns:
            A Result object that contains the data that should be displayed
            in the UI.
        """
        raise NotImplementedError
```

## File: `services/go-importer/converters/helpers/requirements.txt`
```
h2
urllib3
protobuf-inspector
dnslib
cryptography
scapy
aioquic
msgpack
```

## File: `services/go-importer/internal/converters/pool.go`
```go
package converters

import (
	"fmt"
	"sync/atomic"
)

// TODO: we need some configuration file for this/re-use configuration.py somehow
// Waterfall-like effect, each stage's outputs keep falling towards next group, e.g.
// using 2 converters will cause the next group to get the output of those two passed to it.
// Additionally, the original entry is always sent to all of the groups.
var serviceConfig = map[int][][]string{
	// CyberUniAuth
	1234: {
		{"b64decode"},
	},
	// ExamNotes
	1235: {
		{"b64decode"},
	},
	// EncryptedNotes
	1236: {
		{"b64decode"},
	},
	1237: {
		{"b64decode"},
	},
	// RPN
	1337: {
		{"b64decode"},
	},
	// closedsea
	3003: {
		// Protocol
		{"websockets"},
		// Various encodings one could use (should always be last)
		{"b64decode"},
	},
	// closedseaMinter
	3004: {
		{"b64decode"},
	},
	// Trademark
	5000: {
		{"b64decode"},
	},
}

var workerPool = map[string][]*Process{}
var workerAccessCounter = map[string]*uint64{}

// GetWorker
// This is a naive implementation of round-robin, ideally the pool load balancing would give the first free one,
// but this is a lot easier to implement on a shorter timeline (and significantly more reliable against deadlocks!)
func GetWorker(converter string) (*Process, error) {
	workers, ok := workerPool[converter]
	if !ok {
		return nil, fmt.Errorf("no worker for converter %s exists", converter)
	}

	counter := atomic.AddUint64(workerAccessCounter[converter], 1)
	return workers[counter%uint64(len(workers))], nil
}

func StartWorkers(workerCountPerConverter int) {
	var converters = map[string]bool{}
	for _, service := range serviceConfig {
		for _, stages := range service {
			for _, converter := range stages {
				converters[converter] = true
			}
		}
	}

	for converter := range converters {
		var zero uint64 = 0
		workerAccessCounter[converter] = &zero

		// TODO: we could have smarter logic here, e.g. if each service uses b64 converter we want that to have more workers than a static amount
		for i := 0; i < workerCountPerConverter; i++ {
			process, err := NewProcess(converter)
			if err != nil {
				panic(fmt.Errorf("starting converter worker failed: %w", err))
			}

			workerPool[converter] = append(workerPool[converter], process)
		}
	}
}
```

## File: `services/go-importer/internal/converters/process.go`
```go
package converters

import (
	"fmt"
	"github.com/vmihailenco/msgpack/v5"
	"log"
	"os"
	"os/exec"
	"sync"
	"time"
)

var pythonPath *string

func GetPythonPath() string {
	if pythonPath == nil {
		path, err := exec.LookPath("python3")
		if err != nil {
			panic(fmt.Errorf("failed to find python3: %w", err))
		}

		pythonPath = &path
	}

	return *pythonPath
}

type Process struct {
	Mutex sync.RWMutex

	Name    string
	Cmd     *exec.Cmd
	Encoder *msgpack.Encoder
	Decoder *msgpack.Decoder

	RestartMutex  sync.RWMutex
	Restarting    bool
	RestartWaiter chan bool
}

func (process *Process) createCmd() error {
	process.Cmd = exec.Command(GetPythonPath(), fmt.Sprintf("converters/%s.py", process.Name))

	stdin, err := process.Cmd.StdinPipe()
	if err != nil {
		return fmt.Errorf("failed to create stdin pipe: %w", err)
	}
	process.Encoder = msgpack.NewEncoder(stdin)

	stdout, err := process.Cmd.StdoutPipe()
	if err != nil {
		return fmt.Errorf("failed to create stdout pipe: %w", err)
	}
	process.Decoder = msgpack.NewDecoder(stdout)

	// TODO: better handling around this?
	process.Cmd.Stderr = os.Stderr

	if err := process.Cmd.Start(); err != nil {
		return fmt.Errorf("failed to start converter for %s: %w", process.Name, err)
	}

	return nil
}

func (process *Process) Restart() error {
	process.RestartMutex.Lock()
	process.Restarting = true
	process.RestartMutex.Unlock()

	if err := process.Cmd.Process.Kill(); err != nil {
		return fmt.Errorf("killing converter failed: %w", err)
	}

	return nil
}

func NewProcess(converter string) (*Process, error) {
	process := &Process{
		Name: converter,

		Restarting:    false,
		RestartWaiter: make(chan bool, 1),
	}
	if err := process.createCmd(); err != nil {
		return nil, fmt.Errorf("failed to create converter: %w", err)
	}

	go func() {
		for {
			err := process.Cmd.Wait()

			// This aims to minimize the loss of conversions that happen. If it's a timeout restart, only
			// that specific conversion will be lost. Otherwise, there may be small delay where the converter
			// will be completely broken and leak more conversions (though it shouldn't really randomly crash...?)
			process.RestartMutex.Lock()
			process.Restarting = true
			process.RestartMutex.Unlock()

			log.Printf("WARN: Converter for %s died: %s\n", converter, err.Error())

			process.Mutex.Lock()
			for {
				if err := process.createCmd(); err != nil {
					log.Printf("!!! FAILED TO CREATE CONVERTER: %s\n", err.Error())
					time.Sleep(5 * time.Second)
					continue
				}

				break
			}
			process.Mutex.Unlock()

			process.RestartMutex.Lock()
			process.Restarting = false
			process.RestartMutex.Unlock()

			// This should never be anything else than zero, but don't hang things if it for some reason is
			if len(process.RestartWaiter) == 0 {
				process.RestartWaiter <- true
			}
		}
	}()

	return process, nil
}
```

## File: `services/go-importer/internal/converters/runner.go`
```go
package converters

import (
	"fmt"
	"go-importer/internal/pkg/db"
	"log"
	"time"
)

func RunPipeline(g_db *db.Database, entry *db.FlowEntry) {
	// TODO: should we also check src port?
	config, ok := serviceConfig[int(entry.Dst_port)]
	if !ok {
		return
	}

	for _, converters := range config {
		// Split flows into groups by their kinds
		var flows map[string][]db.FlowItem
		for _, item := range entry.Flow {
			_, ok := flows[item.Kind]
			if !ok {
				flows[item.Kind] = []db.FlowItem{}
			}

			flows[item.Kind] = append(flows[item.Kind], item)
		}

		for parent_kind, items := range flows {
			for _, converter := range converters {
				child_kind := fmt.Sprintf("%s -> %s", parent_kind, converter)

				converterFlow, err := TryConverter(converter, entry, items)
				if err != nil {
					log.Printf("WARN: Failed to run converter %s: %s\n", converter, err.Error())
					continue
				}

				// Something went wrong or there's no difference in the data
				if len(converterFlow) == 0 {
					continue
				}

				for _, flow := range converterFlow {
					flow.Kind = child_kind
					entry.Flow = append(entry.Flow, flow)
				}
			}
		}
	}
}

type RequestChunk struct {
	Src_ip   string
	Src_port uint16
	Dst_ip   string
	Dst_port uint16
	Flow     []db.FlowItem
}

type ProcessedChunk struct {
	From string
	Data []byte
	Time time.Time
}

func TryConverter(converter string, entry *db.FlowEntry, flow []db.FlowItem) ([]db.FlowItem, error) {
	process, err := GetWorker(converter)
	if err != nil {
		return nil, fmt.Errorf("failed to get worker for converter %s: %w", converter, err)
	}

	process.RestartMutex.RLock()
	restarting := process.Restarting
	process.RestartMutex.RUnlock()

	if restarting {
		<-process.RestartWaiter
	}

	process.Mutex.Lock()
	defer process.Mutex.Unlock()

	ch := make(chan error, 1)

	var streamChunks []ProcessedChunk
	go func() {
		if err := process.Encoder.Encode(RequestChunk{
			Src_ip:   entry.Src_ip.String(),
			Src_port: entry.Src_port,
			Dst_ip:   entry.Dst_ip.String(),
			Dst_port: entry.Dst_port,
			Flow:     flow,
		}); err != nil {
			ch <- fmt.Errorf("failed to marshal flow entry: %w", err)
			return
		}

		if err := process.Decoder.Decode(&streamChunks); err != nil {
			ch <- fmt.Errorf("failed to unmarshal stream chunks: %w", err)
			return
		}

		if len(flow) != 0 {
			streamChunks[len(streamChunks)].Time = flow[0].Time
		}

		ch <- nil
	}()

	select {
	case <-time.After(time.Second):
		log.Printf("WARN: Converter %s somehow timed out, restarting it...\n", converter)
		if err := process.Restart(); err != nil {
			log.Printf("WARN: Failed to restart the converter: %s\n", err.Error())
		}

		// Trying again will (most likely) just lead to it crashing again
		return nil, fmt.Errorf("timed out encoding flow entry")
	case err := <-ch:
		if err != nil {
			return nil, err
		}
	}

	// TODO: pkappa2 does some post-processing here - same direction streams are merged into one (is this worth the effort?)

	var flowItems []db.FlowItem
	for _, chunk := range streamChunks {
		flowItems = append(flowItems, db.FlowItem{
			From: chunk.From,
			Data: chunk.Data,
			Time: chunk.Time,
		})
	}

	return flowItems, nil
}
```

## File: `services/go-importer/internal/pkg/db/batcher.go`
```go
package db

import (
	"context"
	"log"
	"sync"
	"time"

	"go-importer/internal/pkg/event"

	"github.com/jackc/pgx/v5"
)

const BATCH_DEFAULT_SIZE = 1000;
const BATCH_DEFAULT_TIMEOUT = time.Duration(5 * float64(time.Second));

type CopyBatcherConfig struct {
	db *Database
	context context.Context
	tableName pgx.Identifier
	columns []string
	batchSize int
	batchTimeout time.Duration
	errorHook func(*CopyBatcherConfig, error)
}

type CopyBatcher struct {
	dataIn chan<- CopyBatcherItem
	config CopyBatcherConfig
}

func NewCopyBatcher(config CopyBatcherConfig) *CopyBatcher {
	dataIn := make(chan CopyBatcherItem)
	errorOut := make(chan error)

	if config.batchSize == 0 {
		config.batchSize = BATCH_DEFAULT_SIZE
	}

	if config.batchTimeout == 0 {
		config.batchTimeout = BATCH_DEFAULT_TIMEOUT
	}

	if config.context == nil {
		config.context = context.Background()
	}

	if config.errorHook == nil {
		config.errorHook = CopyBatcherLoggerErrorHook
	}

	batcher := &CopyBatcher {
		dataIn: dataIn,
		config: config,
	}

	go func() {
		for {
			err, open := <-errorOut
			if err != nil {
				config.errorHook(&batcher.config, err)
			}
			if !open {
				break
			}
		}
	}()

	go func() {
		defer close(dataIn)
		defer close(errorOut)

		var index int
		batchDataIn, batchErrorIn, batchTimeout := NewCopyBatcherBatch(&batcher.config, errorOut)

		newBatch := func() {
			close(batchDataIn)
			close(batchErrorIn)

			batchDataIn, batchErrorIn, batchTimeout = NewCopyBatcherBatch(&batcher.config, errorOut)
			index = 0
		}

		for {
			select {
			case <-batchTimeout.Select():
				newBatch()
			case record, open := <-dataIn:
				if !open {
					break
				}

				if batchTimeout.IsSet() {
					newBatch()
				}

				batchDataIn <- record
				index++

				if index == batcher.config.batchSize {
					newBatch()
				}
			case <-batcher.config.context.Done():
				if err := batcher.config.context.Err(); err != nil {
					batchErrorIn <- err
					errorOut <- err
					break
				}
			}
		}
	}()

	return batcher
}

func (batcher *CopyBatcher) Push(data []any) {
	batcher.PushCallback(data, nil)
}

func (batcher *CopyBatcher) PushCallback(data []any, callback func(error)) {
	batcher.dataIn <- CopyBatcherItem { data: data, callback: callback }
}

func (batcher *CopyBatcher) PushAll(data [][]any) {
	for i := range data {
		batcher.Push(data[i])
	}
}

func (batcher *CopyBatcher) PushAllCallback(data [][]any, callback func(<-chan error)) {
	errors := make(chan error, len(data))
	var wg sync.WaitGroup
	wg.Add(len(data))

	for i := range data {
		batcher.PushCallback(data[i], func(err error) {
			if err != nil {
				errors <- err
			}
			wg.Done()
		})
	}

	go func() {
		wg.Wait()
		callback(errors)
	}()
}

type CopyBatcherItem struct {
	data []any
	callback func(error)
}

type CopyBatcherBatch struct {
	dataIn <-chan CopyBatcherItem
	errorIn <-chan error
	start event.Event
	close event.Event
	timeout event.Event
	data []any
	error error
	callbacks []func(error)
	config *CopyBatcherConfig
}

func NewCopyBatcherBatch(config *CopyBatcherConfig, errorOut chan<- error) (chan<- CopyBatcherItem, chan<- error, event.Event) {
	dataIn := make(chan CopyBatcherItem)
	errorIn := make(chan error)
	timeout := event.New()

	config.db.workerPool.Submit(func() {
		batch := CopyBatcherBatch {
			dataIn: dataIn,
			errorIn: errorIn,
			config: config,
			start: event.New(),
			close: event.New(),
			timeout: timeout,
		}

		go func() {
			batch.start.Wait()
			time.AfterFunc(batch.config.batchTimeout, batch.timeout.Set)
		}()

		count, err := config.db.pool.CopyFrom(
			config.context,
			config.tableName,
			config.columns,
			&batch,
		)

		if !batch.start.IsSet() {
			CopyBatcherLoggerErrorHook(config, err)
			log.Fatalln("CopyBatcher: CopyFrom returned before any data was received")
		}

		if err != nil {
			errorOut <- err
		} else if count > 0 {
			log.Printf("Copied %d rows into table %s\n", count, config.tableName)
		}

		for _, callback := range batch.callbacks {
			callback(err)
		}
	})

	return dataIn, errorIn, timeout
}

func (batch *CopyBatcherBatch) Next() bool {
	if !batch.start.IsSet() {
		batch.start.Set()
	}

	if batch.close.IsSet() {
		return false
	}

	var open bool
	var item CopyBatcherItem
	select {
	case item, open = <-batch.dataIn:
		batch.data = item.data
		if item.callback != nil {
			batch.callbacks = append(batch.callbacks, item.callback)
		}
	case batch.error = <-batch.errorIn:
	}

	if !open {
		batch.close.Set()
		return false
	}

	if batch.error != nil {
		return false
	}

	return true
}

func (batch *CopyBatcherBatch) Values() ([]any, error) {
	return batch.data, batch.error
}

func (batch *CopyBatcherBatch) Err() error {
	return batch.error
}

func CopyBatcherLoggerErrorHook(config *CopyBatcherConfig, err error) {
	log.Printf("Error in copy channel for table %s: %s", config.tableName.Sanitize(), err)
}
```

## File: `services/go-importer/internal/pkg/db/db.go`
```go
package db

import (
	"bytes"
	"context"
	"encoding/json"
	"log"
	"net/netip"
	"runtime"
	"sync"
	"time"
	"math"

	"github.com/gammazero/workerpool"
	"github.com/gofrs/uuid/v5"

	pgxuuid "github.com/jackc/pgx-gofrs-uuid"
	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgxpool"
)

type Database struct {
	pool *pgxpool.Pool
	workerPool *workerpool.WorkerPool
	batcherFlowEntry *CopyBatcher
	batcherFlowItem *CopyBatcher
	batcherFlowIndex *CopyBatcher
	knownTags map[string]struct{}
	knownTagsMutex *sync.RWMutex
	fingerprints [][]int32
	fingerprintsMutex *sync.Mutex
	suricataIdWindow time.Duration
}

func NewDatabase(connectionString string) *Database {
	poolConfig, err := pgxpool.ParseConfig(connectionString)
	if err != nil {
		log.Fatalln("Unable to parse database config: ", err)
	}

	database := &Database {}
	poolConfig.AfterConnect = database.AfterConnect

	// Database connection pool
	database.pool, err = pgxpool.New(context.Background(), connectionString)
	if err != nil {
		log.Fatalln("Unable to create db connection pool: ", err)
	}

	for {
		err := database.pool.Ping(context.Background())
		if err == nil {
			break
		}

		log.Println("Unable to connect to database (retrying in 5s):", err)
		time.Sleep(5 * time.Second)
	}

	database.workerPool = workerpool.New(runtime.NumCPU() / 2)
	database.batcherFlowEntry = NewCopyBatcher(CopyBatcherConfig {
		db: database,
		tableName: pgx.Identifier{"flow"},
		columns: []string {
			"id", "port_src", "port_dst", "ip_src", "ip_dst", "duration", "tags",
			"flags", "flagids", "pcap_id", "link_child_id", "link_parent_id",
			"fingerprints", "packets_count", "packets_size", "flags_in", "flags_out",
		},
	})
	database.batcherFlowItem = NewCopyBatcher(CopyBatcherConfig {
		db: database,
		tableName: pgx.Identifier{"flow_item"},
		columns: []string{"id", "flow_id", "kind", "direction", "data"},
		batchSize: 2000,
	})
	database.batcherFlowIndex = NewCopyBatcher(CopyBatcherConfig {
		db: database,
		tableName: pgx.Identifier{"flow_index"},
		columns: []string{"flow_id", "text"},
		batchSize: 4000,
	})

	// Fingerprints
	// Periodically flush them into database
	database.fingerprintsMutex = &sync.Mutex{}
	go func() {
		for range time.Tick(5 * time.Second) {
			database.FingerprintsFlush()
		}
	}()

	// Known tags
	// Periodically update them in the background
	// in case someone else added some, or we did
	database.knownTagsMutex = &sync.RWMutex{}
	database.knownTags = make(map[string]struct{})
	database.KnownTagsUpdate()
	go func() {
		for range time.Tick(5 * time.Second) {
			database.KnownTagsUpdate()
		}
	}()

	// Suricata id search window
	if database.suricataIdWindow == 0 {
		database.suricataIdWindow = time.Duration(time.Minute)
	}

	return database
}

func (db *Database) AfterConnect(ctx context.Context, conn *pgx.Conn) error {
	pgxuuid.Register(conn.TypeMap())
	return nil
}

// Pcap files
type Pcap struct {
	Id uuid.UUID
	Name string
	Position int64
}

func (db *Database) PcapFindOrInsert(name string) Pcap {
	// With the amount of concurrency here we have to use ON CONFLICT,
	// any other solution (except maybe explicit locking) will cause
	// concurrency problems
	// UUIDs are used because sequence + ON CONFLICT increments evenry time this is run,
	// this is bad if the check is run a lot so we stick with random uuid
	// INDEX: Unique on pcap.name
	_, err := db.pool.Exec(context.Background(), `
		INSERT INTO pcap (id, name)
		VALUES (uuid_generate_v4(), @name)
		ON CONFLICT (name) DO NOTHING
	`, pgx.NamedArgs {
		"name": name,
	})

	if err != nil {
		log.Fatalln("Error inserting pcap: ", err)
	}

	// When DO NOTHING happens, no rows are returned
	// even with RETURNING so we kinda need a second query here
	// INDEX: Unique on pcap.name
	rows, _ := db.pool.Query(context.Background(), `
		SELECT *
		FROM pcap
		WHERE name = @name
	`, pgx.NamedArgs {
		"name": name,
	})
	defer rows.Close()

	pcap, err := pgx.CollectOneRow(rows, pgx.RowToStructByName[Pcap])
	if err != nil {
		log.Fatalln("Error inserting pcap: ", err)
	}

	return pcap
}

func (db *Database) PcapSetPosition(id uuid.UUID, position int64) error {
	// INDEX: Primary on pcap.id
	_, err := db.pool.Exec(context.Background(), `
		UPDATE pcap
		SET position = @position
		WHERE id = @id
	`, pgx.NamedArgs {
		"id": id,
		"position": position,
	})

	if err != nil {
		log.Println("Error updating pcap position: ", err)
	}

	return err
}

// Known tags
// The Database struct has a list of all tags previously encountered
// Any new tags are asyncronusly inserted to the db and added to this list
func (db *Database) KnownTagsUpdate() {
	db.knownTagsMutex.Lock()
	defer db.knownTagsMutex.Unlock()

	// Insert any new tags
	// This will trigger ON CONFLICT if two assemblers
	// try to do this at the same time, which is fine
	if len(db.knownTags) != 0 {
		var knownTags []string
		for tag := range db.knownTags {
			knownTags = append(knownTags, tag)
		}

		// INDEX: Primary on tag.name
		_, err := db.pool.Exec(context.Background(), `
			INSERT INTO tag (name)
			SELECT jsonb_array_elements_text(@tags::jsonb - array_agg(name)) FROM tag
			ON CONFLICT (name) DO NOTHING
		`, pgx.NamedArgs {
			"tags": knownTags,
		})

		if err != nil {
			log.Fatalln("Error inserting tags: ", err)
		}
	}

	var tags []string
	err := db.pool.QueryRow(context.Background(), `
		SELECT array_agg(t.name)
		FROM (SELECT name FROM tag ORDER BY sort ASC) AS t
	`).Scan(&tags)

	if err != nil {
		log.Println("Error updating known tags: ", err)
		return
	}

	for _, tag := range tags {
		db.knownTags[tag] = struct{}{}
	}
}

func (db *Database) KnownTagExists(tag string) bool {
	db.knownTagsMutex.RLock()
	defer db.knownTagsMutex.RUnlock()
	_, ok := db.knownTags[tag]
	return ok
}

func (db *Database) KnownTagsUpsert(tag string) {
	if db.KnownTagExists(tag) {
		return
	}

	db.knownTagsMutex.Lock()
	defer db.knownTagsMutex.Unlock()

	// Tags are periodically upserted into database
	// see Database::KnownTagsUpdate
	db.knownTags[tag] = struct{}{}
}

// Flows
type FlowEntry struct {
	Id           uuid.UUID
	Src_port     uint16 `db:"port_src"`
	Dst_port     uint16 `db:"port_dst"`
	Src_ip       netip.Addr `db:"ip_src"`
	Dst_ip       netip.Addr `db:"ip_dst"`
	Time         time.Time
	Duration     time.Duration
	Filename     string `db:"-"`
	PcapId       uuid.UUID `db:"pcap_id"`
	Parent_id    *uuid.UUID `db:"link_parent_id"`
	Child_id     *uuid.UUID `db:"link_child_id"`
	Fingerprints []uint32
	Flow         []FlowItem `db:"-"`
	Tags         []string `db:"tags"`
	Flags        []string `db:"flags"`
	Flagids      []string `db:"flagids"`
	Num_packets  int `db:"packets_count"`
	Size         int `db:"packets_size"`
	Flags_In     int `db:"flags_in"`
	Flags_Out    int `db:"flags_out"`
}

type FlowItem struct {
	Id uuid.UUID
	FlowId uuid.UUID `db:"flow_id"`
	Kind string
	/// From: "s" / "c" for server or client
	From string `db:"direction"`
	/// The raw packet bytes
	Data []byte `msgpack:"-"`
	/// Timestamp of the first packet in the flow
	Time time.Time
}

// Flows are either coming from a file, in which case we'll dedupe them by pcap file name.
// If they're coming from a live capture, we can do pretty much the same thing, but we'll
// just have to come up with a label. (e.g. capture-<epoch>)
// We can always swap this out with something better, but this is how flower currently handles deduping.
//
// A single flow is defined by a db.FlowEntry" struct, containing an array of flowitems and some metadata
func (db *Database) FlowInsert(flow FlowEntry) {
	// Dont even try to insert empty flows
	if len(flow.Flow) == 0 {
		return
	}

	// Make sure tags exist
	// This can be done async
	for _, tag := range flow.Tags {
		tag := tag
		db.workerPool.Submit(func() {
			db.KnownTagsUpsert(tag)
		})
	}

	// Fallback to filename for pcap id
	pcap_id := flow.PcapId
	if pcap_id == uuid.Nil {
		pcap_id = db.PcapFindOrInsert(flow.Filename).Id
	}

	// Generate flow id
	flow_id := FidCreate(flow.Time)

	// Prepare index rows
	// These are split to chunks of maximum 1024 chars
	// This is to ensure length of records is not too different
	// between rows and to avoid rechecking large chunks of data
	// in memory after a lossy index search has been used
	chunkLength := 1024
	chunkOverlap := 64
	indexes := make([][]any, 0)
	for _, item := range flow.Flow {
		text := []rune(string(bytes.Replace(bytes.ToValidUTF8(item.Data, []byte{}), []byte{0}, []byte{}, -1)))
		chunkCount := int(math.Ceil(float64(len(text)) / float64(chunkLength)))

		// Each split between index rows has a 64 char overlap
		// This is to accomodate searches hitting the boundary
		for i := 0; i < chunkCount; i++ {
			startIndex := i * chunkLength
			endIndex := i * chunkLength + chunkLength + chunkOverlap
			if endIndex >= len(text) {
				endIndex = len(text)
			}

			chunk := string(text[startIndex:endIndex])
			indexes = append(indexes, []any { flow_id, chunk })
		}
	}

	// Insert index rows
	// This is async, since the index is not required to be peresent when we insert the flow
	// At worst it will take a few seconds before this flow is searchable
	db.batcherFlowIndex.PushAllCallback(indexes, func(errors <-chan error) {
		// Error inserting flow indexes
		if len(errors) != 0 {
			log.Println("Error inserting flow indexes (flow will not be fully searchable): ", <-errors)
		}
	})

	// Prepare flow items
	items := make([][]any, len(flow.Flow))
	for i := range flow.Flow {
		items[i] = []any {
			FidCreate(flow.Flow[i].Time),
			flow_id,
			flow.Flow[i].Kind,
			flow.Flow[i].From,
			&flow.Flow[i].Data,
		}
	}

	// Insert the flow items first, so that when flow is inserted, it is complete
	db.batcherFlowItem.PushAllCallback(items, func(errors <-chan error) {
		// Error inserting flow items
		// Only continue if we managed to insert at least one flow
		// If we got here with and empty flow, I guess just insert it
		if len(errors) != 0 && len(errors) == len(items) {
			// Just print the first error, they will all be the same probably
			log.Println("Error inserting flow items (flow will not be inserted): ", <-errors)
			return
		}

		// Fingerprints are uint32, but psql only has signed integer types
		// So we make them into int32, instead of using a larger psql int
		fingerprints := make([]int32, len(flow.Fingerprints))
		for i, fingerprint := range flow.Fingerprints {
			fingerprints[i] = int32(fingerprint)
		}

		// Push fingerprints for async flow connecting
		db.FingerprintsPush(fingerprints)

		// Now insert the flow
		db.batcherFlowEntry.PushCallback([]any {
			flow_id,
			flow.Src_port, flow.Dst_port,
			flow.Src_ip, flow.Dst_ip,
			// Postgres keeps duration with 1 microsecond precision
			// If we round down we risk some flow items being ouside of this duration
			flow.Duration.Truncate(time.Microsecond) + time.Microsecond,
			flow.Tags,
			flow.Flags,
			flow.Flagids,
			pcap_id,
			flow.Child_id,
			flow.Parent_id,
			fingerprints,
			flow.Num_packets,
			flow.Size,
			flow.Flags_In,
			flow.Flags_Out,
		}, func(err error) {
			if err != nil {
				log.Println("Error inserting flow: ", err)
			}
		})
	})
}

func (db *Database) FlowAddSignatures(flow_id uuid.UUID, signatures []Signature) {
	db.workerPool.Submit(func() {
		signaturesJson, _ := json.Marshal(signatures)

		// INDEX: Primary on flow.id
		_, err := db.pool.Exec(context.Background(), `
			UPDATE flow
			SET signatures = jsonb_unique(signatures || @signatures)
			WHERE id = @flow_id
		`, pgx.NamedArgs {
			"flow_id": flow_id,
			"signatures": signaturesJson,
		})

		if err != nil {
			log.Printf("Error inserting signatures for flow %s: %s\n", flow_id, err)
		}
	})
}

func (db *Database) FlowAddTags(flow_id uuid.UUID, tags []string) {
	// Make sure tags exist
	// This can (and will) be done async
	for _, tag := range tags {
		tag := tag
		db.workerPool.Submit(func() {
			db.KnownTagsUpsert(tag)
		})
	}

	db.workerPool.Submit(func() {
		tagsJson, _ := json.Marshal(tags)

		// INDEX: Primary on flow.id
		_, err := db.pool.Exec(context.Background(), `
			UPDATE flow
			SET tags = jsonb_unique(tags || @tags)
			WHERE id = @flow_id
		`, pgx.NamedArgs {
			"flow_id": flow_id,
			"tags": tagsJson,
		})

		if err != nil {
			log.Printf("Error inserting tags for flow %s: %s\n", flow_id, err)
		}
	})
}

// Suricata flows
type SuricataId struct {
	Src_port int
	Dst_port int
	Src_ip   netip.Addr
	Dst_ip   netip.Addr
	Time     time.Time
}

func (db *Database) SuricataIdFindFlow(id SuricataId) (uuid.UUID, error) {
	var flow_id uuid.UUID

	// INDEX: `f.id` is parition key, limiting scope to specific chunks
	// INDEX: `time_start` and `time_end` should be computed before passing as parameters
	// INDEX: Btree on (id, port_src, port_dst, ip_src, ip_dst)
	// INDEX: Make sure to run EXPLAIN ANALYZE when changing this
	err := db.pool.QueryRow(context.Background(), `
		SELECT id
		FROM flow
		WHERE port_src = @port_src
			AND port_dst = @port_dst
			AND ip_src = @ip_src
			AND ip_dst = @ip_dst
			AND id > fid_pack_low(@time_start)
			AND id < fid_pack_high(@time_end)
	`, pgx.NamedArgs {
		"time_start": id.Time.Add(-db.suricataIdWindow),
		"time_end": id.Time.Add(db.suricataIdWindow),
		"port_src": id.Src_port,
		"port_dst": id.Dst_port,
		"ip_src": id.Src_ip,
		"ip_dst": id.Dst_ip,
	}).Scan(&flow_id)

	return flow_id, err
}

// Suricata signature
type Signature struct {
	Id      int32 `json:"id"`
	Message string `json:"message"`
	Action  string `json:"action"`
}

// Fingerprints
func (db *Database) FingerprintsPush(fingerprints []int32) {
	if len(fingerprints) == 0 {
		return
	}

	db.fingerprintsMutex.Lock()
	defer db.fingerprintsMutex.Unlock()
	db.fingerprints = append(db.fingerprints, fingerprints)
}

func (db *Database) FingerprintsFlush() {
	db.fingerprintsMutex.Lock()

	if len(db.fingerprints) == 0 {
		db.fingerprintsMutex.Unlock()
		return
	}

	fingerprintsMap := make(map[int32]struct{})
	for _, ff := range db.fingerprints {
		if len(ff) > 1 {
			for _, f := range ff {
				fingerprintsMap[f] = struct{}{}
			}
		}
	}

	var fingerprintsUnique []int32
	for f := range fingerprintsMap {
		fingerprintsUnique = append(fingerprintsUnique, f)
	}

	fingerprintsJson, _ := json.Marshal(db.fingerprints)
	db.fingerprints = nil
	db.fingerprintsMutex.Unlock()

	// INDEX: Primary on fingerprint.id
	_, err := db.pool.Exec(context.Background(), `
		INSERT INTO fingerprint (id, grp)
		SELECT jsonb_array_elements(v.value)::int, coalesce(f.grp, v.value[0]::int)
			FROM jsonb_array_elements(@fingerprints) AS v
			LEFT JOIN fingerprint AS f
				ON f.id = ANY(ARRAY(SELECT value::int FROM jsonb_array_elements(v.value)))
		ON CONFLICT (id) DO NOTHING
	`, pgx.NamedArgs {
		"fingerprints": fingerprintsJson,
	})

	if err != nil {
		log.Println("Error inserting fingerprints: ", err)
	}

	// INDEX: Primary on fingerprint.id
	// INDEX: Btree on fingerprint.grp
	// INDEX: Gin on flow.fingerprints
	cmd, err := db.pool.Exec(context.Background(), `
		UPDATE flow AS ff
			SET link_parent_id = d.parent,
			link_child_id = d.child
		FROM (
			SELECT f.id, lag(f.id) OVER (w) AS parent, lead(f.id) OVER (w) AS child
			FROM flow AS f
			INNER JOIN fingerprint AS fp
				ON fp.grp = (SELECT grp FROM fingerprint AS fpp WHERE fpp.id = f.fingerprints[1])
			WHERE fp.id = ANY(@fingerprints)
			GROUP BY f.id, fp.grp
			WINDOW w AS (PARTITION BY fp.grp ORDER BY f.id)
			ORDER BY fp.grp, f.id
		) AS d
		WHERE d.id = ff.id
			AND (
				d.child != link_child_id
				OR d.parent != link_parent_id
				OR (d.child IS NULL) != (link_child_id IS NULL)
				OR (d.parent IS NULL) != (link_parent_id IS NULL)
			)
	`, pgx.NamedArgs {
		"fingerprints": fingerprintsUnique,
	})

	if err != nil {
		log.Println("Error linking flows: ", err)
	}

	if cmd.RowsAffected() != 0 {
		log.Printf("Linked %d flows\n", cmd.RowsAffected())
	}
}

// Flag ids
type FlagId struct {
	Id int32
	Content string
	Time time.Time
}

// Query all valid flag ids
func (db *Database) FlagIdsQuery(lifetime int) ([]FlagId, error) {
	rows, _ := db.pool.Query(context.Background(), `
		SELECT *
		FROM flag_id
		WHERE time > @time_limit
	`, pgx.NamedArgs {
		"time_limit": time.Now().Add(-time.Duration(float64(lifetime) * float64(time.Second))),
	});
	defer rows.Close()

	return pgx.CollectRows(rows, pgx.RowToStructByName[FlagId])
}
```

## File: `services/go-importer/internal/pkg/db/fid.go`
```go
package db

import (
	"crypto/rand"
	"encoding/binary"
	"encoding/hex"
	"log"
	"time"

	"github.com/gofrs/uuid/v5"
)

func FidPack(t time.Time, bytes_rand []byte) uuid.UUID {
	bytes_time := make([]byte, 8)
	binary.BigEndian.PutUint64(bytes_time, uint64(t.UnixMicro()))
	_, error := rand.Read(bytes_rand)
	if error != nil {
		log.Fatal(error)
	}

	hex_time := make([]byte, 16)
	hex_rand := make([]byte, 14)
	hex.Encode(hex_time, bytes_time)
	hex.Encode(hex_rand, bytes_rand)
	str_time := string(hex_time)
	str_rand := string(hex_rand)

	uuid, error := uuid.FromString(str_time[0:12] + "8" + str_time[12:15] + "8" + str_time[15:16] + str_rand)
	if error != nil {
		log.Fatal(error)
	}
	return uuid
}

func FidCreate(t time.Time) uuid.UUID {
	bytes_rand := make([]byte, 7)
	_, error := rand.Read(bytes_rand)
	if error != nil {
		log.Fatal(error)
	}

	return FidPack(t, bytes_rand)
}
```

## File: `services/go-importer/internal/pkg/event/event.go`
```go
package event

type Event struct {
	trigger chan struct{}
}

func New() Event {
	return Event {
		trigger: make(chan struct{}),
	}
}

func (event *Event) IsSet() bool {
	select {
	case <-event.trigger: return true
	default: return false
	}
}

func (event *Event) Set() {
	close(event.trigger)
}

func (event *Event) Wait() {
	<-event.trigger
}

func (event *Event) Select() <-chan struct{} {
	return event.trigger
}
```

## File: `services/go-importer/test_data/Dockerfile`
```
FROM python:3.10


WORKDIR /app

COPY ./ /app/

CMD python3 ./flagid_endpoint.py
```

## File: `services/go-importer/test_data/flagid_endpoint.py`
```python
import http.server
import socketserver

PORT = 8000
JSON_FILE = "flagids.json"

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving JSON file at http://localhost:{PORT}/{JSON_FILE}")
    httpd.serve_forever()
```

## File: `services/go-importer/test_data/flagids.json`
```json
{
  "availableTeams": [
    "10.10.3.1"
  ],

  "services": {
    "cc_market": {
      "10.10.3.1": {
        "7": [
          [ "CletusAlbion" ]

        ],
        "8": [
          [ "KailaAlpha" ]
        ]
      },
      "10.10.4.1": {
        "7": [
          [ "Never" ]

        ],
        "8": [
          [ "Gonna" ]
        ]
      },
      "10.10.5.1": {
        "7": [
          [ "Give" ]

        ],
        "8": [
          [ "You" ]
        ]
      },
      "10.10.6.1": {
        "7": [
          [ "Up" ]

        ],
        "8": [
          [ "..." ]
        ]
      }
    }
  }
}
```

## File: `services/go-importer/test_data/generate.py`
```python
from pwn import *
import threading

l = listen(1337)
r = remote("localhost", 1337)

r.sendline(b"This should be searchable")
l.sendlineafter(b"This should be searchable", b"And so should this line")

def listen(p):
    p.recvall()
def send(p):
    g = cyclic_gen(n=8)
    payload = g.get(6*1024*1024)
    p.sendlineafter(b"line", payload)

sender   = threading.Thread(target=send, args=(r,))
listener = threading.Thread(target=listen, args=(l,))
sender.start()
listener.start()


print("sent")


sender.join()
listener.join()

```

## File: `services/schema/functions.sql`
```sql
-- Helper function to convert number to bytes (big-endian)
CREATE FUNCTION int_big_endian(num bigint, len int)
RETURNS bytea LANGUAGE plpgsql IMMUTABLE PARALLEL SAFE AS $$
DECLARE
	result bytea = '';
	index int = 0;
BEGIN
	WHILE index < len LOOP
		result := set_byte('\x00', 0, (num % 256)::int) || result;
		num := (num - num % 256) / 256;
		index := index + 1;
	END LOOP;

	return result;
END; $$;

-- Helper function to convert bytes to number (big-endian)
CREATE FUNCTION big_endian_int(bytes bytea)
RETURNS bigint LANGUAGE plpgsql IMMUTABLE PARALLEL SAFE AS $$
DECLARE
	result bigint = 0;
	index int = 0;
BEGIN
	WHILE index < octet_length(bytes) LOOP
		result := result * 256 + get_byte(bytes, index);
		index := index + 1;
	END LOOP;

	return result;
END; $$;

-- Function to create UUID based on timestamp and random bytes
CREATE FUNCTION fid_pack("time" timestamptz, random bytea)
RETURNS uuid LANGUAGE plpgsql IMMUTABLE PARALLEL SAFE AS $$
DECLARE
	time_int bigint = extract(epoch FROM "time" AT TIME ZONE 'UTC') * 1000000;
	time_hex text = encode(int_big_endian(time_int, 8), 'hex');
	random_hex text = substring(encode(random, 'hex') FOR 14);
BEGIN
	RETURN substring(time_hex FOR 12)
		|| '8' || substring(time_hex FROM 13 FOR 3)
		|| '8' || substring(time_hex FROM 16 FOR 1)
		|| random_hex;
END; $$;

CREATE FUNCTION fid_pack_low("time" timestamptz)
RETURNS uuid LANGUAGE plpgsql IMMUTABLE PARALLEL SAFE AS $$
BEGIN
	RETURN fid_pack("time", '\x00000000000000');
END; $$;

CREATE FUNCTION fid_pack_high("time" timestamptz)
RETURNS uuid LANGUAGE plpgsql IMMUTABLE PARALLEL SAFE AS $$
BEGIN
	RETURN fid_pack("time", '\xffffffffffffff');
END; $$;

-- Functions to extract UUID values
CREATE FUNCTION fid_unpack_time(id uuid)
RETURNS timestamptz LANGUAGE plpgsql IMMUTABLE PARALLEL SAFE AS $$
DECLARE
	hex text := replace(id::text, '-', '');
	time_hex text := substring(hex FOR 12) || substring(hex FROM 14 FOR 3) || substring(hex FROM 18 FOR 1);
BEGIN
	RETURN to_timestamp(big_endian_int(decode(time_hex, 'hex'))::float / 1000000)::timestamptz;
END; $$;

CREATE FUNCTION fid_unpack_random(id uuid)
RETURNS bytea LANGUAGE plpgsql IMMUTABLE PARALLEL SAFE AS $$
DECLARE
	hex text := replace(id::text, '-', '');
	random_hex text := substring(hex FROM 19 FOR 14);
BEGIN
	RETURN decode(random_hex, 'hex');
END; $$;

CREATE FUNCTION fid_create("time" timestamptz)
RETURNS uuid LANGUAGE plpgsql VOLATILE PARALLEL SAFE AS $$
BEGIN
	RETURN fid_pack("time", gen_random_bytes(7));
END; $$;

-- Min / Max functions
CREATE FUNCTION fid_max()
RETURNS uuid LANGUAGE SQL IMMUTABLE PARALLEL SAFE STRICT
AS 'SELECT ''7fffffff-ffff-ffff-ffff-ffffffffffff''::uuid';

CREATE FUNCTION fid_min()
RETURNS uuid LANGUAGE SQL IMMUTABLE PARALLEL SAFE STRICT
AS 'SELECT ''00000000-0000-0000-0000-000000000000''::uuid';

-- Distance and index functions
CREATE FUNCTION fid_distance(uuid, uuid)
RETURNS int8 LANGUAGE SQL IMMUTABLE PARALLEL SAFE STRICT
AS 'SELECT (extract(epoch FROM fid_unpack_time($1) <-> fid_unpack_time($2)) * 1000000)::int8';

CREATE OPERATOR <-> (
	LEFTARG = uuid,
	RIGHTARG = uuid,
	PROCEDURE = fid_distance,
	COMMUTATOR = '<->'
);

CREATE FUNCTION fid_distance_op(internal, uuid, int2, oid, internal)
RETURNS float8 LANGUAGE C IMMUTABLE PARALLEL SAFE STRICT
AS 'tulip';

CREATE OPERATOR CLASS gist_fid_ops
FOR TYPE uuid USING gist AS
	OPERATOR 1  <,
	OPERATOR 2  <=,
	OPERATOR 3  =,
	OPERATOR 4  >=,
	OPERATOR 5  >,
	OPERATOR 6  <>,
	OPERATOR 15 <-> FOR ORDER BY pg_catalog.integer_ops,
	FUNCTION 1  gbt_uuid_consistent (internal, uuid, int2, oid, internal),
	FUNCTION 2  gbt_uuid_union (internal, internal),
	FUNCTION 3  gbt_uuid_compress (internal),
	FUNCTION 4  gbt_decompress (internal),
	FUNCTION 5  gbt_uuid_penalty (internal, internal, internal),
	FUNCTION 6  gbt_uuid_picksplit (internal, internal),
	FUNCTION 7  gbt_uuid_same (gbtreekey32, gbtreekey32, internal),
	FUNCTION 9  gbt_uuid_fetch (internal),
	FUNCTION 8  fid_distance_op(internal, uuid, int2, oid, internal),
	STORAGE gbtreekey32;

-- Ranking functions
-- This is used for GiST index sorting
CREATE FUNCTION fid_rank_desc(uuid)
RETURNS int8 LANGUAGE SQL IMMUTABLE PARALLEL SAFE STRICT
AS 'SELECT $1 <-> fid_max()';

CREATE FUNCTION fid_rank_asc(uuid)
RETURNS int8 LANGUAGE SQL IMMUTABLE PARALLEL SAFE STRICT
AS 'SELECT $1 <-> fid_min()';

-- Json helper functions
CREATE FUNCTION jsonb_unique(data jsonb)
RETURNS jsonb LANGUAGE plpgsql VOLATILE PARALLEL SAFE AS $$
BEGIN
	RETURN (SELECT jsonb_agg(DISTINCT value) FROM jsonb_array_elements(data));
END; $$;

-- Tick helper functions
CREATE FUNCTION tick_time_bucket(tick_first timestamptz, tick_length interval, "time" timestamptz)
RETURNS timestamptz LANGUAGE plpgsql IMMUTABLE PARALLEL SAFE AS $$
BEGIN
	RETURN time_bucket(tick_length, "time", origin => tick_first);
END; $$;

CREATE FUNCTION tick_number_bucket(tick_first timestamptz, tick_length interval, "time" timestamptz)
RETURNS int LANGUAGE plpgsql IMMUTABLE PARALLEL SAFE AS $$
BEGIN
	RETURN extract(epoch from (tick_time_bucket(tick_first, tick_length, "time") - tick_first)) / extract(epoch from tick_length);
END; $$;
```

## File: `services/schema/schema.sql`
```sql
CREATE TABLE tag (
	name text PRIMARY KEY,
	sort serial NOT NULL
);

-- This is the order in which tags should be displayed
-- Change it hare if it should be different
-- Newly encountered tags will be automaticcaly
-- added to the end of this list
INSERT INTO tag (name) VALUES
	('tcp'),
	('udp'),
	('http'),
	('flag-in'),
	('flag-out'),
	('flagid-in'),
	('flagid-out'),
	('blocked'),
	('suricata'),
	('starred');

-- Flag ids
CREATE TABLE flag_id (
	id serial NOT NULL PRIMARY KEY,
	content text NOT NULL,
	time timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX ON flag_id USING btree (content);

-- Pcaps
CREATE TABLE pcap (
	id uuid PRIMARY KEY,
	name text NOT NULL UNIQUE,
	position bigint NOT NULL DEFAULT 0
);

CREATE TABLE fingerprint (
	id int PRIMARY KEY,
	grp int NOT NULL
);

-- Fingerprint matching during assembly
CREATE INDEX ON fingerprint (grp);

CREATE TABLE flow (
	id uuid NOT NULL PRIMARY KEY,
	time timestamptz GENERATED ALWAYS AS (fid_unpack_time(id)) STORED,
	port_src int NOT NULL,
	port_dst int NOT NULL,
	ip_src inet NOT NULL,
	ip_dst inet NOT NULL,
	duration interval NOT NULL,
	pcap_id uuid NOT NULL,
	link_parent_id uuid,
	link_child_id uuid,
	tags jsonb NOT NULL DEFAULT '[]',
	flags jsonb NOT NULL DEFAULT '[]',
	flagids jsonb NOT NULL DEFAULT '[]',
	fingerprints int[] NOT NULL DEFAULT '{}',
	signatures jsonb NOT NULL DEFAULT '[]',
	packets_count int NOT NULL DEFAULT 0,
	packets_size int NOT NULL DEFAULT 0,
	flags_in int NOT NULL DEFAULT 0,
	flags_out int NOT NULL DEFAULT 0
);

-- Suricata id lookup, see Database::SuricataIdFindFlow
CREATE INDEX ON flow (id, port_src, port_dst, ip_src, ip_dst);
-- Tag search
CREATE INDEX ON flow USING gin (tags);
-- Fingerprint matching during assembly
CREATE INDEX ON flow USING gin (fingerprints);

SELECT create_hypertable(
	'flow',
	'id',
	chunk_time_interval => INTERVAL '1 hour',
	time_partitioning_func => 'fid_unpack_time'
);

CREATE TABLE flow_item (
	id uuid NOT NULL PRIMARY KEY,
	flow_id uuid NOT NULL,
	kind text NOT NULL,
	time timestamptz GENERATED ALWAYS AS (fid_unpack_time(id)) STORED,
	direction text NOT NULL,
	data bytea NOT NULL
);

SELECT create_hypertable(
	'flow_item',
	'id',
	chunk_time_interval => INTERVAL '1 hour',
	time_partitioning_func => 'fid_unpack_time'
);

-- Table for quick indexed regex search on utf8 data
-- The data in this table is chunked to 1028 characters
-- with 64 character overlap
CREATE TABLE flow_index (
	flow_id uuid NOT NULL,
	text text NOT NULL
);

-- Regex search, this one is chonky
-- This is a GiST rather than GIN since GIN does not support sorting
-- In the future we could use something like RUM (https://github.com/postgrespro/rum)
-- Sadly, RUM does not support fast update like GIN does, so ingestion takes ages
CREATE INDEX ON flow_index USING gist (text gist_trgm_ops(siglen=2024), flow_id gist_fid_ops);
```

## File: `services/schema/statistics.sql`
```sql
SELECT
	(SELECT count(*) FROM fingerprint) AS fingerprint_count,
	pg_size_pretty(pg_total_relation_size('fingerprint')) AS fingerprint_table_size,
	(SELECT count(*) FROM flow) AS flow_count,
	(SELECT pg_size_pretty(total_bytes) FROM hypertable_detailed_size('flow')) AS flow_total_size,
	(SELECT pg_size_pretty(index_bytes) FROM hypertable_detailed_size('flow')) AS flow_index_size,
	(SELECT count(*) FROM flow_item) AS flow_item_count,
	(SELECT pg_size_pretty(total_bytes) FROM hypertable_detailed_size('flow_item')) AS flow_item_total_size,
	(SELECT pg_size_pretty(index_bytes) FROM hypertable_detailed_size('flow_item')) AS flow_item_index_size,
	(SELECT count(*) FROM flow_index) AS flow_index_count,
	pg_size_pretty(pg_total_relation_size('flow_index')) AS flow_index_total_size,
	pg_size_pretty(pg_indexes_size('flow_index')) AS flow_index_index_size,
	(SELECT count(*) FROM pcap) AS pcap_count,
	pg_size_pretty(pg_total_relation_size('pcap')) AS pcap_table_size,
	(SELECT count(*) FROM tag) AS tag_count,
	pg_size_pretty(pg_total_relation_size('tag')) AS tag_table_size,
	pg_size_pretty(pg_database_size('tulip')) AS database_size;
```

## File: `services/schema/system.sql`
```sql
CREATE EXTENSION pgcrypto;
CREATE EXTENSION intarray;
CREATE EXTENSION "uuid-ossp";
CREATE EXTENSION pg_trgm;
CREATE EXTENSION btree_gin;
CREATE EXTENSION btree_gist;

ALTER SYSTEM SET shared_preload_libraries = 'timescaledb', 'pg_hint_plan', 'pg_prewarm', 'auto_explain', 'tulip';
ALTER SYSTEM SET timescaledb.telemetry_level = off;

LOAD 'auto_explain';
ALTER SYSTEM SET auto_explain.log_min_duration = 5000;
ALTER SYSTEM SET auto_explain.log_analyze = true;
ALTER SYSTEM SET auto_explain.log_timing = false;

-- These settings provide ingest speed boost at cost
-- of disabling replication and possible loss of any uncommited data
ALTER SYSTEM SET synchronous_commit = off;
ALTER SYSTEM SET wal_level = minimal;
ALTER SYSTEM SET max_wal_senders = 0;
ALTER SYSTEM SET max_wal_size = '10GB';

-- These settings provide ingest speed boost at cost
-- of data consistency
-- Be prepared to loose ALL data on crash when using these
--ALTER SYSTEM SET fsync = off;
--ALTER SYSTEM SET full_page_writes = off;
```

## File: `services/test_pcap/eve.json`
```json
{"timestamp":"2018-06-27T13:25:32.730991+0200","flow_id":2069435303860030,"pcap_cnt":1053,"event_type":"alert","src_ip":"10.10.3.126","src_port":56318,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":22,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":478,"bytes_toclient":4113,"start":"2018-06-27T13:25:32.726846+0200"}}
{"timestamp":"2018-06-27T13:25:32.765278+0200","flow_id":1927400735416114,"pcap_cnt":1101,"event_type":"alert","src_ip":"10.10.3.126","src_port":56338,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:25:32.761650+0200"}}
{"timestamp":"2018-06-27T13:25:32.775379+0200","flow_id":2097973214102936,"pcap_cnt":1113,"event_type":"alert","src_ip":"10.10.3.126","src_port":56340,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:25:32.771480+0200"}}
{"timestamp":"2018-06-27T13:25:32.863536+0200","flow_id":1898723238747734,"pcap_cnt":1187,"event_type":"alert","src_ip":"10.10.3.126","src_port":56368,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:25:32.859734+0200"}}
{"timestamp":"2018-06-27T13:25:32.813865+0200","flow_id":1411583753082899,"pcap_cnt":1125,"event_type":"alert","src_ip":"10.10.3.126","src_port":56342,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:25:32.808979+0200"}}
{"timestamp":"2018-06-27T13:25:34.407695+0200","flow_id":747418600481573,"pcap_cnt":2381,"event_type":"alert","src_ip":"10.10.3.126","src_port":56664,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:25:34.402213+0200"}}
{"timestamp":"2018-06-27T13:25:34.529182+0200","flow_id":2125248403997853,"pcap_cnt":2455,"event_type":"alert","src_ip":"10.10.3.126","src_port":56676,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:25:34.525469+0200"}}
{"timestamp":"2018-06-27T13:25:34.420240+0200","flow_id":2133726669461986,"pcap_cnt":2393,"event_type":"alert","src_ip":"10.10.3.126","src_port":56666,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:25:34.416226+0200"}}
{"timestamp":"2018-06-27T13:25:34.357527+0200","flow_id":1103645335512403,"pcap_cnt":2368,"event_type":"alert","src_ip":"10.10.3.126","src_port":56662,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:25:34.353619+0200"}}
{"timestamp":"2018-06-27T13:25:34.321335+0200","flow_id":1761322940160278,"pcap_cnt":2320,"event_type":"alert","src_ip":"10.10.3.126","src_port":56654,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":22,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":478,"bytes_toclient":4113,"start":"2018-06-27T13:25:34.317718+0200"}}
{"timestamp":"2018-06-27T13:26:02.712247+0200","flow_id":961464740003431,"pcap_cnt":5111,"event_type":"alert","src_ip":"10.10.3.126","src_port":56816,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:26:02.704103+0200"}}
{"timestamp":"2018-06-27T13:26:02.650619+0200","flow_id":239392690724429,"pcap_cnt":5086,"event_type":"alert","src_ip":"10.10.3.126","src_port":56812,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:26:02.646733+0200"}}
{"timestamp":"2018-06-27T13:26:02.613070+0200","flow_id":2069096003421829,"pcap_cnt":5035,"event_type":"alert","src_ip":"10.10.3.126","src_port":56804,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":22,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":478,"bytes_toclient":4113,"start":"2018-06-27T13:26:02.607877+0200"}}
{"timestamp":"2018-06-27T13:26:02.874624+0200","flow_id":1493039957295662,"pcap_cnt":5218,"event_type":"alert","src_ip":"10.10.3.126","src_port":56826,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:26:02.868910+0200"}}
{"timestamp":"2018-06-27T13:26:02.659710+0200","flow_id":1918050593538319,"pcap_cnt":5098,"event_type":"alert","src_ip":"10.10.3.126","src_port":56814,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:26:02.655631+0200"}}
{"timestamp":"2018-06-27T13:26:04.365438+0200","flow_id":849226507256712,"pcap_cnt":6479,"event_type":"alert","src_ip":"10.10.3.126","src_port":57010,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":22,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":478,"bytes_toclient":4113,"start":"2018-06-27T13:26:04.361352+0200"}}
{"timestamp":"2018-06-27T13:26:04.444369+0200","flow_id":198886854277507,"pcap_cnt":6528,"event_type":"alert","src_ip":"10.10.3.126","src_port":57018,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:26:04.440707+0200"}}
{"timestamp":"2018-06-27T13:26:04.453926+0200","flow_id":1750302056046457,"pcap_cnt":6540,"event_type":"alert","src_ip":"10.10.3.126","src_port":57020,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:26:04.450425+0200"}}
{"timestamp":"2018-06-27T13:26:04.520356+0200","flow_id":526496222207011,"pcap_cnt":6554,"event_type":"alert","src_ip":"10.10.3.126","src_port":57022,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:26:04.515107+0200"}}
{"timestamp":"2018-06-27T13:26:04.619382+0200","flow_id":1830967984283982,"pcap_cnt":6615,"event_type":"alert","src_ip":"10.10.3.126","src_port":57032,"dest_ip":"10.10.3.1","dest_port":5000,"proto":"TCP","tx_id":0,"alert":{"action":"allowed","gid":1,"signature_id":1001200,"rev":1,"signature":"Example - single character password","category":"","severity":3,"metadata":{"tag":["enemy"]}},"http":{"hostname":"10.10.3.1","http_port":5000,"url":"/login","http_user_agent":"python-requests/2.19.1","http_content_type":"text/html","http_method":"POST","protocol":"HTTP/1.1","status":200,"length":3684},"files":[{"filename":"/login","sid":[],"gaps":false,"state":"CLOSED","stored":false,"size":24,"tx_id":0}],"app_proto":"http","flow":{"pkts_toserver":4,"pkts_toclient":3,"bytes_toserver":480,"bytes_toclient":4113,"start":"2018-06-27T13:26:04.614734+0200"}}
```

## File: `services/test_pcap/example.rule`
```
# Just as an example, this suricata rule tags every single-character password in the starchaser service
# that is included as a test pcap.

alert tcp any any -> any 5000 (msg: "Example - single character password"; flow:to_server; \
	content:"POST"; http_method; content:"/login"; http_uri; \
	content: "password"; http_client_body; pcre:"/password=[A-Za-z0-9]&/"; \
	metadata: tag enemy; \
	sid:1001200; rev: 1;)
```

## File: `services/timescale/Dockerfile`
```
FROM timescale/timescaledb:latest-pg15

RUN apk add build-base make clang15 llvm15 git
COPY tulip /tulip
RUN cd /tulip && make USE_PGXS=1 install && cd / && \
	git clone https://github.com/ossc-db/pg_hint_plan --branch PG15 && \
	cd pg_hint_plan && make USE_PGXS=1 install
```

## File: `services/timescale/tulip/Makefile`
```
EXTENSION = tulip
MODULE_big = tulip
OBJS = tulip.o
PG_CONFIG = pg_config
PGXS := $(shell $(PG_CONFIG) --pgxs)
include $(PGXS)
```

## File: `services/timescale/tulip/tulip.c`
```c
#include "postgres.h"
#include "access/gist.h"
#include "executor/executor.h"
#include "utils/uuid.h"

PG_MODULE_MAGIC;

PG_FUNCTION_INFO_V1(fid_distance_op);

typedef struct {
	pg_uuid_t lower, upper;
} uuidKEY;

uint64_t fid_unpack_uint(pg_uuid_t* uuid);
Datum fid_distance_op(PG_FUNCTION_ARGS);

uint64_t fid_unpack_uint(pg_uuid_t* uuid) {
	return
		((uint64_t)uuid->data[0] << 56) |
		((uint64_t)uuid->data[1] << 48) |
		((uint64_t)uuid->data[2] << 40) |
		((uint64_t)uuid->data[3] << 32) |
		((uint64_t)uuid->data[4] << 24) |
		((uint64_t)uuid->data[5] << 16) |
		((uint64_t)uuid->data[6] << 8) |
		(uint64_t)uuid->data[7];
}

Datum fid_distance_op(PG_FUNCTION_ARGS) {
	GISTENTRY* entry = (GISTENTRY *) PG_GETARG_POINTER(0);
	pg_uuid_t* uuid = PG_GETARG_UUID_P(1);
	uuidKEY* key = (uuidKEY *)DatumGetPointer(entry->key);

	uint64_t query = fid_unpack_uint(uuid);
	uint64_t lower = fid_unpack_uint(&key->lower);
	uint64_t upper = fid_unpack_uint(&key->upper);

	if(query <= lower)
		PG_RETURN_FLOAT8((float8)(lower - query));
	if(query >= upper)
		PG_RETURN_FLOAT8((float8)(query - upper));
	PG_RETURN_FLOAT8(0);
}
```

## File: `services/timescale/tulip/tulip.control`
```
comment = 'Tulip'
default_version = '0.1'
relocatable = true
module_pathname = '$libdir/tulip'
```

