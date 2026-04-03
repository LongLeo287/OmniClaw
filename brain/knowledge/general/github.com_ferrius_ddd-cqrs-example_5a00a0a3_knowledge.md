---
id: github.com-ferrius-ddd-cqrs-example-5a00a0a3-knowl
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:49.784036
---

# KNOWLEDGE EXTRACT: github.com_ferrius_ddd-cqrs-example_5a00a0a3
> **Extracted on:** 2026-04-01 10:39:11
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521017/github.com_ferrius_ddd-cqrs-example_5a00a0a3

---

## File: `.env`
```
# In all environments, the following files are loaded if they exist,
# the latter taking precedence over the former:
#
#  * .env                contains default values for the environment variables needed by the app
#  * .env.local          uncommitted file with local overrides
#  * .env.$APP_ENV       committed environment-specific defaults
#  * .env.$APP_ENV.local uncommitted environment-specific overrides
#
# Real environment variables win over .env files.
#
# DO NOT DEFINE PRODUCTION SECRETS IN THIS FILE NOR IN ANY OTHER COMMITTED FILES.
#
# Run "composer dump-env prod" to compile .env files for production use (requires symfony/flex >=1.2).
# https://symfony.com/doc/current/best_practices.html#use-environment-variables-for-infrastructure-configuration

###> symfony/framework-bundle ###
APP_ENV=
APP_SECRET=
#TRUSTED_PROXIES=127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16
#TRUSTED_HOSTS='^(localhost|example\.com)$'
###< symfony/framework-bundle ###

###> doctrine/doctrine-bundle ###
# Format described at https://www.doctrine-project.org/projects/doctrine-dbal/en/latest/reference/configuration.html#connecting-using-a-url
# For an SQLite database, use: "sqlite:///%kernel.project_dir%/var/data.db"
# For a PostgreSQL database, use: "postgresql://db_user:db_password@127.0.0.1:5432/db_name?serverVersion=11&charset=utf8"
# IMPORTANT: You MUST configure your server version, either here or in config/packages/doctrine.yaml
DATABASE_URL=
###< doctrine/doctrine-bundle ###
###> symfony/messenger ###
# Choose one of the transports below
# MESSENGER_TRANSPORT_DSN=amqp://guest:guest@localhost:5672/%2f/messages
# MESSENGER_TRANSPORT_DSN=doctrine://default
# MESSENGER_TRANSPORT_DSN=redis://localhost:6379/messages
###< symfony/messenger ###

###> lexik/jwt-authentication-bundle ###
JWT_SECRET_KEY=%kernel.project_dir%/config/jwt/private.pem
JWT_PUBLIC_KEY=%kernel.project_dir%/config/jwt/public.pem
JWT_PASSPHRASE=532342fc598e3f18af81096bcbdef713
###< lexik/jwt-authentication-bundle ###
```

## File: `.env.test`
```
# define your env variables for the test env here
KERNEL_CLASS='App\Kernel'
APP_SECRET='$ecretf0rt3st'
SYMFONY_DEPRECATIONS_HELPER=999999
PANTHER_APP_ENV=panther
```

## File: `.gitignore`
```
###> symfony/framework-bundle ###
/.env.local
/.env.local.php
/.env.*.local
/config/secrets/prod/prod.decrypt.private.php
/public/bundles/
/var/
/vendor/
###< symfony/framework-bundle ###
###> symfony/phpunit-bridge ###
.phpunit
.phpunit.result.cache
/phpunit.xml
###< symfony/phpunit-bridge ###

###> JetBrains ##
# User-specific stuff
.idea/
###< JetBrains ###

.php_cs.cache
docker/.env

###> sensiolabs-de/deptrac-shim ###
/.deptrac.cache
###< sensiolabs-de/deptrac-shim ###

###> lexik/jwt-authentication-bundle ###
/config/jwt/*.pem
###< lexik/jwt-authentication-bundle ###
```

## File: `.php_cs`
```
<?php

$finder = \PhpCsFixer\Finder::create()
    ->in(['src'])
;
return \PhpCsFixer\Config::create()
    ->setRules([
        '@Symfony' => true,
        '@PHP71Migration' => true,
        'concat_space' => ['spacing' => 'one'],
        'phpdoc_summary' => false,
        'phpdoc_align' => false,
        'no_short_echo_tag' => true,
        'no_useless_else' => true,
        'is_null' => true,
        'multiline_whitespace_before_semicolons' => true,
        'list_syntax' => ['syntax' => 'short'],
        'array_syntax' => ['syntax' => 'short'],
        'php_unit_strict' => false,
        'strict_comparison' => true,
        'strict_param' => true,
        'declare_strict_types' => true,
        'yoda_style' => false,
        'ordered_class_elements' => true,
        'date_time_immutable' => true,
        'no_unused_imports' => true,
        'ordered_imports' => ['sort_algorithm' => 'alpha'],
        'native_function_invocation' => [
            'include' => ['@compiler_optimized']
        ],
        'method_argument_space' => [
            'on_multiline' => 'ensure_fully_multiline'
        ],
        'fully_qualified_strict_types' => true,
        'no_unreachable_default_argument_value' => true,
        'static_lambda' => true,
        'no_superfluous_phpdoc_tags' => false,
        'single_line_throw' => false,
    ])
    ->setFinder($finder)
;
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

## File: `Makefile`
```
.PHONY: run
run:
	@cd docker && docker-compose run -u dev workplace $(filter-out $@,$(MAKECMDGOALS))

.PHONY: dev
dev:
	@cd docker && docker-compose exec -u dev workplace bash

##################
# Docker compose
##################

.PHONY: dc_start
dc_start:
	@cd docker && docker-compose start

.PHONY: dc_stop
dc_stop:
	@cd docker && docker-compose stop

.PHONY: dc_up
dc_up:
	@cd docker && docker-compose up -d

.PHONY: dc_ps
dc_ps:
	@cd docker && docker-compose ps

.PHONY: dc_down
dc_down:
	@cd docker && docker-compose down -v --rmi=all --remove-orphans

##################
# Setup
##################

.PHONY: setup_dev
setup_dev:
	cd docker && docker-compose run -u dev workplace composer install
	cd docker && docker-compose run -u dev workplace php bin/console doctrine:migrations:migrate --no-interaction
	cd docker && docker-compose run -u dev workplace php bin/console cache:clear

##################
# CI (workplace container)
##################

.PHONY: analyze
analyze: deptrac cs_check phpmnd phpcpd phpstan security_check schema_validate phpunit

.PHONY: cs_check
cs_check:
	php-cs-fixer fix --config=.php_cs -v --allow-risky=yes --dry-run --diff --stop-on-violation

.PHONY: cs_fix
cs_fix:
	php-cs-fixer fix --config=.php_cs -v --allow-risky=yes --diff

.PHONY: schema_validate
schema_validate:
	php bin/console doctrine:cache:clear-metadata
	php bin/console doctrine:schema:validate

.PHONY: phpmnd
phpmnd:
	/home/dev/.composer/vendor/bin/phpmnd src -v --progress --extensions=all --non-zero-exit-on-violation

.PHONY: phpcpd
phpcpd:
	./vendor/bin/phpcpd src --exclude=Entity

.PHONY: security_check
security_check:
	php bin/console security:check

.PHONY: phpstan
phpstan:
	php ./vendor/bin/phpstan analyse src -c phpstan.neon

.PHONY: deptrac
deptrac:
	php ./vendor/bin/deptrac analyze depfile.yaml

.PHONY: phpunit
phpunit:
	php ./vendor/bin/phpunit

```

## File: `Readme.md`
```markdown
### About
This is an example of implementation and my vision of **practical** CQRS, DDD, ADR, hexagonal architecture and directory structure.
Project has entities `Task` and `User`.
All UI is the REST endpoints.

### What is done
* Hexagonal Architecture (`Ports` directory for external endpoints)
* CQRS (based on symfony messenger component command/query buses with middlewares)
* DDD: directory structure (used sensiolabs-de/deptrac to control layers dependencies)
* DDD: core bounded context
* DDD: domain events implementation
* DDD: example of specification in User entity that requires a db query

### To do
* Add another bounded context
* Add anti-corruption layer for interaction between contexts

### My assumptions
* I placed entities public getters and private setters into the traits with *GS suffix to make entities a little bit clear (phpstorm tracks fine all references to entity classes) anyway you can put getters with setters in the same class
* Unfortunately mysql has a poor performance with primary uuids. Of course prefer application generated uuid if database supports them.

### How to install the project
* `bash setup_env.sh dev` - to setup .env.local docker/.env
* `make dc_up` - docker-compose up 
* `make setup_dev` - composer install, migrations and so on
* `make run php bin/console app:create-user` - create a user
* `http://127.0.0.1:888/api/doc` `https://127.0.0.1:444/api/doc` - api doc

### Some words about docker
In project is used workplace container for code manipulations, CI or building. It was created for preventing of pollution
of working containers (php-fpm) of unused in request, building tools like nodejs, composer, dev libs and so on.
Also was created a local user based on host machine user PUID PGID to resolve conflicts with file permissions.

`make dev` - jump into workplace container

### CI
```
make dev
//in container execute
make analyze
```

### Implementation
Used symfony messenger component to create transactional command bus, query bus and event bus.
Query model represented by DTOs. Domain and Command layers are covered by unit tests. 

```
├── Core (Core bounded context)
│   ├── Application
│   │   ├── Command
│   │   │   ├── AuthToken
│   │   │   ├── Task
│   │   │   └── User
│   │   ├── Query
│   │       └── Task
│   ├── Domain
│   │   └── Model
│   │       ├── Task
│   │       └── User
│   ├── Infrastructure
│   │   └── Repository
│   └── Ports
│       ├── Cli
│       └── Rest
└── Shared
    ├── Domain
    └── Infrastructure

```


```

## File: `composer.json`
```json
{
    "type": "project",
    "license": "proprietary",
    "require": {
        "php": "7.4.*",
        "ext-ctype": "*",
        "ext-iconv": "*",
        "ext-json": "*",
        "ext-pdo": "*",
        "lexik/jwt-authentication-bundle": "^2.10",
        "nelmio/api-doc-bundle": "^4.1",
        "sensiolabs/security-checker": "^6.0",
        "symfony/asset": "5.0.*",
        "symfony/console": "5.0.*",
        "symfony/dotenv": "5.0.*",
        "symfony/flex": "^1.3.1",
        "symfony/framework-bundle": "5.0.*",
        "symfony/messenger": "5.0.*",
        "symfony/orm-pack": "^1.0",
        "symfony/security-bundle": "5.0.*",
        "symfony/serializer-pack": "^1.0",
        "symfony/twig-pack": "^1.0",
        "symfony/yaml": "5.0.*",
        "webmozart/assert": "^1.8"
    },
    "require-dev": {
        "phpstan/phpstan": "^0.12.25",
        "phpstan/phpstan-doctrine": "^0.12.13",
        "phpstan/phpstan-phpunit": "^0.12.8",
        "phpstan/phpstan-strict-rules": "^0.12.2",
        "phpstan/phpstan-symfony": "^0.12.6",
        "phpstan/phpstan-webmozart-assert": "^0.12.4",
        "phpunit/phpunit": "^9.1",
        "sebastian/phpcpd": "^5.0",
        "sensiolabs-de/deptrac-shim": "^0.7.1",
        "symfony/debug-pack": "^1.0",
        "symfony/maker-bundle": "^1.18",
        "symfony/test-pack": "^1.0"
    },
    "config": {
        "preferred-install": {
            "*": "dist"
        },
        "sort-packages": true
    },
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "App\\Tests\\": "tests/"
        }
    },
    "replace": {
        "paragonie/random_compat": "2.*",
        "symfony/polyfill-ctype": "*",
        "symfony/polyfill-iconv": "*",
        "symfony/polyfill-php72": "*",
        "symfony/polyfill-php71": "*",
        "symfony/polyfill-php70": "*",
        "symfony/polyfill-php56": "*"
    },
    "scripts": {
        "auto-scripts": {
            "cache:clear": "symfony-cmd",
            "assets:install %PUBLIC_DIR%": "symfony-cmd",
            "security-checker security:check": "script"
        },
        "post-install-cmd": [
            "@auto-scripts"
        ],
        "post-update-cmd": [
            "@auto-scripts"
        ]
    },
    "conflict": {
        "symfony/symfony": "*"
    },
    "extra": {
        "symfony": {
            "allow-contrib": false,
            "require": "5.0.*"
        }
    }
}
```

## File: `composer.lock`
```
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#installing-dependencies",
        "This file is @generated automatically"
    ],
    "content-hash": "d9d171bb3749b3cd3233398eaa30038b",
    "packages": [
        {
            "name": "composer/package-versions-deprecated",
            "version": "1.11.99.1",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/package-versions-deprecated.git",
                "reference": "7413f0b55a051e89485c5cb9f765fe24bb02a7b6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/package-versions-deprecated/zipball/7413f0b55a051e89485c5cb9f765fe24bb02a7b6",
                "reference": "7413f0b55a051e89485c5cb9f765fe24bb02a7b6",
                "shasum": ""
            },
            "require": {
                "composer-plugin-api": "^1.1.0 || ^2.0",
                "php": "^7 || ^8"
            },
            "replace": {
                "ocramius/package-versions": "1.11.99"
            },
            "require-dev": {
                "composer/composer": "^1.9.3 || ^2.0@dev",
                "ext-zip": "^1.13",
                "phpunit/phpunit": "^6.5 || ^7"
            },
            "type": "composer-plugin",
            "extra": {
                "class": "PackageVersions\\Installer",
                "branch-alias": {
                    "dev-master": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PackageVersions\\": "src/PackageVersions"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                },
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be"
                }
            ],
            "description": "Composer plugin that provides efficient querying for installed package versions (no runtime IO)",
            "support": {
                "issues": "https://github.com/composer/package-versions-deprecated/issues",
                "source": "https://github.com/composer/package-versions-deprecated/tree/1.11.99.1"
            },
            "funding": [
                {
                    "url": "https://packagist.com",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/composer",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/composer/composer",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-11T10:22:58+00:00"
        },
        {
            "name": "doctrine/annotations",
            "version": "1.11.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/annotations.git",
                "reference": "ce77a7ba1770462cd705a91a151b6c3746f9c6ad"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/annotations/zipball/ce77a7ba1770462cd705a91a151b6c3746f9c6ad",
                "reference": "ce77a7ba1770462cd705a91a151b6c3746f9c6ad",
                "shasum": ""
            },
            "require": {
                "doctrine/lexer": "1.*",
                "ext-tokenizer": "*",
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "doctrine/cache": "1.*",
                "doctrine/coding-standard": "^6.0 || ^8.1",
                "phpstan/phpstan": "^0.12.20",
                "phpunit/phpunit": "^7.5 || ^9.1.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.11.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Annotations\\": "lib/Doctrine/Common/Annotations"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "Docblock Annotations Parser",
            "homepage": "https://www.doctrine-project.org/projects/annotations.html",
            "keywords": [
                "annotations",
                "docblock",
                "parser"
            ],
            "support": {
                "issues": "https://github.com/doctrine/annotations/issues",
                "source": "https://github.com/doctrine/annotations/tree/1.11.1"
            },
            "time": "2020-10-26T10:28:16+00:00"
        },
        {
            "name": "doctrine/cache",
            "version": "1.10.2",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/cache.git",
                "reference": "13e3381b25847283a91948d04640543941309727"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/cache/zipball/13e3381b25847283a91948d04640543941309727",
                "reference": "13e3381b25847283a91948d04640543941309727",
                "shasum": ""
            },
            "require": {
                "php": "~7.1 || ^8.0"
            },
            "conflict": {
                "doctrine/common": ">2.2,<2.4"
            },
            "require-dev": {
                "alcaeus/mongo-php-adapter": "^1.1",
                "doctrine/coding-standard": "^6.0",
                "mongodb/mongodb": "^1.1",
                "phpunit/phpunit": "^7.0",
                "predis/predis": "~1.0"
            },
            "suggest": {
                "alcaeus/mongo-php-adapter": "Required to use legacy MongoDB driver"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.9.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Cache\\": "lib/Doctrine/Common/Cache"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Cache library is a popular cache implementation that supports many different drivers such as redis, memcache, apc, mongodb and others.",
            "homepage": "https://www.doctrine-project.org/projects/cache.html",
            "keywords": [
                "abstraction",
                "apcu",
                "cache",
                "caching",
                "couchdb",
                "memcached",
                "php",
                "redis",
                "xcache"
            ],
            "support": {
                "issues": "https://github.com/doctrine/cache/issues",
                "source": "https://github.com/doctrine/cache/tree/1.10.x"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fcache",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-07T18:54:01+00:00"
        },
        {
            "name": "doctrine/collections",
            "version": "1.6.7",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/collections.git",
                "reference": "55f8b799269a1a472457bd1a41b4f379d4cfba4a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/collections/zipball/55f8b799269a1a472457bd1a41b4f379d4cfba4a",
                "reference": "55f8b799269a1a472457bd1a41b4f379d4cfba4a",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^6.0",
                "phpstan/phpstan-shim": "^0.9.2",
                "phpunit/phpunit": "^7.0",
                "vimeo/psalm": "^3.8.1"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Collections\\": "lib/Doctrine/Common/Collections"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Collections library that adds additional functionality on top of PHP arrays.",
            "homepage": "https://www.doctrine-project.org/projects/collections.html",
            "keywords": [
                "array",
                "collections",
                "iterators",
                "php"
            ],
            "support": {
                "issues": "https://github.com/doctrine/collections/issues",
                "source": "https://github.com/doctrine/collections/tree/1.6.7"
            },
            "time": "2020-07-27T17:53:49+00:00"
        },
        {
            "name": "doctrine/common",
            "version": "2.13.3",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/common.git",
                "reference": "f3812c026e557892c34ef37f6ab808a6b567da7f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/common/zipball/f3812c026e557892c34ef37f6ab808a6b567da7f",
                "reference": "f3812c026e557892c34ef37f6ab808a6b567da7f",
                "shasum": ""
            },
            "require": {
                "doctrine/annotations": "^1.0",
                "doctrine/cache": "^1.0",
                "doctrine/collections": "^1.0",
                "doctrine/event-manager": "^1.0",
                "doctrine/inflector": "^1.0",
                "doctrine/lexer": "^1.0",
                "doctrine/persistence": "^1.3.3",
                "doctrine/reflection": "^1.0",
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^1.0",
                "phpstan/phpstan": "^0.11",
                "phpstan/phpstan-phpunit": "^0.11",
                "phpunit/phpunit": "^7.0",
                "squizlabs/php_codesniffer": "^3.0",
                "symfony/phpunit-bridge": "^4.0.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.11.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\": "lib/Doctrine/Common"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                },
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                }
            ],
            "description": "PHP Doctrine Common project is a library that provides additional functionality that other Doctrine projects depend on such as better reflection support, persistence interfaces, proxies, event system and much more.",
            "homepage": "https://www.doctrine-project.org/projects/common.html",
            "keywords": [
                "common",
                "doctrine",
                "php"
            ],
            "support": {
                "issues": "https://github.com/doctrine/common/issues",
                "source": "https://github.com/doctrine/common/tree/2.13.x"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fcommon",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-05T16:46:05+00:00"
        },
        {
            "name": "doctrine/dbal",
            "version": "2.12.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/dbal.git",
                "reference": "adce7a954a1c2f14f85e94aed90c8489af204086"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/dbal/zipball/adce7a954a1c2f14f85e94aed90c8489af204086",
                "reference": "adce7a954a1c2f14f85e94aed90c8489af204086",
                "shasum": ""
            },
            "require": {
                "doctrine/cache": "^1.0",
                "doctrine/event-manager": "^1.0",
                "ext-pdo": "*",
                "php": "^7.3 || ^8"
            },
            "require-dev": {
                "doctrine/coding-standard": "^8.1",
                "jetbrains/phpstorm-stubs": "^2019.1",
                "phpstan/phpstan": "^0.12.40",
                "phpunit/phpunit": "^9.4",
                "psalm/plugin-phpunit": "^0.10.0",
                "symfony/console": "^2.0.5|^3.0|^4.0|^5.0",
                "vimeo/psalm": "^3.17.2"
            },
            "suggest": {
                "symfony/console": "For helpful console commands such as SQL execution and import of files."
            },
            "bin": [
                "bin/doctrine-dbal"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\DBAL\\": "lib/Doctrine/DBAL"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                }
            ],
            "description": "Powerful PHP database abstraction layer (DBAL) with many features for database schema introspection and management.",
            "homepage": "https://www.doctrine-project.org/projects/dbal.html",
            "keywords": [
                "abstraction",
                "database",
                "db2",
                "dbal",
                "mariadb",
                "mssql",
                "mysql",
                "oci8",
                "oracle",
                "pdo",
                "pgsql",
                "postgresql",
                "queryobject",
                "sasql",
                "sql",
                "sqlanywhere",
                "sqlite",
                "sqlserver",
                "sqlsrv"
            ],
            "support": {
                "issues": "https://github.com/doctrine/dbal/issues",
                "source": "https://github.com/doctrine/dbal/tree/2.12.1"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fdbal",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-14T20:26:58+00:00"
        },
        {
            "name": "doctrine/doctrine-bundle",
            "version": "2.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/DoctrineBundle.git",
                "reference": "015fdd490074d4daa891e2d1df998dc35ba54924"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/DoctrineBundle/zipball/015fdd490074d4daa891e2d1df998dc35ba54924",
                "reference": "015fdd490074d4daa891e2d1df998dc35ba54924",
                "shasum": ""
            },
            "require": {
                "doctrine/dbal": "^2.9.0|^3.0",
                "doctrine/persistence": "^1.3.3|^2.0",
                "doctrine/sql-formatter": "^1.0.1",
                "php": "^7.1 || ^8.0",
                "symfony/cache": "^4.3.3|^5.0",
                "symfony/config": "^4.3.3|^5.0",
                "symfony/console": "^3.4.30|^4.3.3|^5.0",
                "symfony/dependency-injection": "^4.3.3|^5.0",
                "symfony/doctrine-bridge": "^4.3.7|^5.0",
                "symfony/framework-bundle": "^3.4.30|^4.3.3|^5.0",
                "symfony/service-contracts": "^1.1.1|^2.0"
            },
            "conflict": {
                "doctrine/orm": "<2.6",
                "twig/twig": "<1.34|>=2.0,<2.4"
            },
            "require-dev": {
                "doctrine/coding-standard": "^8.0",
                "doctrine/orm": "^2.6",
                "friendsofphp/proxy-manager-lts": "^1.0",
                "phpunit/phpunit": "^7.5 || ^8.0 || ^9.3",
                "symfony/phpunit-bridge": "^4.2",
                "symfony/property-info": "^4.3.3|^5.0",
                "symfony/proxy-manager-bridge": "^3.4|^4.3.3|^5.0",
                "symfony/twig-bridge": "^3.4.30|^4.3.3|^5.0",
                "symfony/validator": "^3.4.30|^4.3.3|^5.0",
                "symfony/web-profiler-bundle": "^3.4.30|^4.3.3|^5.0",
                "symfony/yaml": "^3.4.30|^4.3.3|^5.0",
                "twig/twig": "^1.34|^2.12|^3.0"
            },
            "suggest": {
                "doctrine/orm": "The Doctrine ORM integration is optional in the bundle.",
                "symfony/web-profiler-bundle": "To use the data collector."
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Bundle\\DoctrineBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "http://symfony.com/contributors"
                },
                {
                    "name": "Doctrine Project",
                    "homepage": "http://www.doctrine-project.org/"
                }
            ],
            "description": "Symfony DoctrineBundle",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "database",
                "dbal",
                "orm",
                "persistence"
            ],
            "support": {
                "issues": "https://github.com/doctrine/DoctrineBundle/issues",
                "source": "https://github.com/doctrine/DoctrineBundle/tree/2.2.3"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fdoctrine-bundle",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-19T20:29:53+00:00"
        },
        {
            "name": "doctrine/doctrine-migrations-bundle",
            "version": "2.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/DoctrineMigrationsBundle.git",
                "reference": "85f0b847174daf243362c7da80efe1539be64f47"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/DoctrineMigrationsBundle/zipball/85f0b847174daf243362c7da80efe1539be64f47",
                "reference": "85f0b847174daf243362c7da80efe1539be64f47",
                "shasum": ""
            },
            "require": {
                "doctrine/doctrine-bundle": "~1.0|~2.0",
                "doctrine/migrations": "^2.2",
                "php": "^7.1|^8.0",
                "symfony/framework-bundle": "~3.4|~4.0|~5.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^8.0",
                "mikey179/vfsstream": "^1.6",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-strict-rules": "^0.12",
                "phpunit/phpunit": "^7.0|^8.0|^9.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Bundle\\MigrationsBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Doctrine Project",
                    "homepage": "http://www.doctrine-project.org"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "http://symfony.com/contributors"
                }
            ],
            "description": "Symfony DoctrineMigrationsBundle",
            "homepage": "https://www.doctrine-project.org",
            "keywords": [
                "dbal",
                "migrations",
                "schema"
            ],
            "support": {
                "issues": "https://github.com/doctrine/DoctrineMigrationsBundle/issues",
                "source": "https://github.com/doctrine/DoctrineMigrationsBundle/tree/2.2.2"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fdoctrine-migrations-bundle",
                    "type": "tidelift"
                }
            ],
            "time": "2020-12-23T15:06:17+00:00"
        },
        {
            "name": "doctrine/event-manager",
            "version": "1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/event-manager.git",
                "reference": "41370af6a30faa9dc0368c4a6814d596e81aba7f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/event-manager/zipball/41370af6a30faa9dc0368c4a6814d596e81aba7f",
                "reference": "41370af6a30faa9dc0368c4a6814d596e81aba7f",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
            },
            "conflict": {
                "doctrine/common": "<2.9@dev"
            },
            "require-dev": {
                "doctrine/coding-standard": "^6.0",
                "phpunit/phpunit": "^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\": "lib/Doctrine/Common"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                },
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                }
            ],
            "description": "The Doctrine Event Manager is a simple PHP event system that was built to be used with the various Doctrine projects.",
            "homepage": "https://www.doctrine-project.org/projects/event-manager.html",
            "keywords": [
                "event",
                "event dispatcher",
                "event manager",
                "event system",
                "events"
            ],
            "support": {
                "issues": "https://github.com/doctrine/event-manager/issues",
                "source": "https://github.com/doctrine/event-manager/tree/1.1.x"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fevent-manager",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-29T18:28:51+00:00"
        },
        {
            "name": "doctrine/inflector",
            "version": "1.4.3",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/inflector.git",
                "reference": "4650c8b30c753a76bf44fb2ed00117d6f367490c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/inflector/zipball/4650c8b30c753a76bf44fb2ed00117d6f367490c",
                "reference": "4650c8b30c753a76bf44fb2ed00117d6f367490c",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^7.0",
                "phpstan/phpstan": "^0.11",
                "phpstan/phpstan-phpunit": "^0.11",
                "phpstan/phpstan-strict-rules": "^0.11",
                "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Inflector\\": "lib/Doctrine/Common/Inflector",
                    "Doctrine\\Inflector\\": "lib/Doctrine/Inflector"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Inflector is a small library that can perform string manipulations with regard to upper/lowercase and singular/plural forms of words.",
            "homepage": "https://www.doctrine-project.org/projects/inflector.html",
            "keywords": [
                "inflection",
                "inflector",
                "lowercase",
                "manipulation",
                "php",
                "plural",
                "singular",
                "strings",
                "uppercase",
                "words"
            ],
            "support": {
                "issues": "https://github.com/doctrine/inflector/issues",
                "source": "https://github.com/doctrine/inflector/tree/1.4.x"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Finflector",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-29T07:19:59+00:00"
        },
        {
            "name": "doctrine/instantiator",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/instantiator.git",
                "reference": "d56bf6102915de5702778fe20f2de3b2fe570b5b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/instantiator/zipball/d56bf6102915de5702778fe20f2de3b2fe570b5b",
                "reference": "d56bf6102915de5702778fe20f2de3b2fe570b5b",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^8.0",
                "ext-pdo": "*",
                "ext-phar": "*",
                "phpbench/phpbench": "^0.13 || 1.0.0-alpha2",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-phpunit": "^0.12",
                "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Instantiator\\": "src/Doctrine/Instantiator/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com",
                    "homepage": "https://ocramius.github.io/"
                }
            ],
            "description": "A small, lightweight utility to instantiate objects in PHP without invoking their constructors",
            "homepage": "https://www.doctrine-project.org/projects/instantiator.html",
            "keywords": [
                "constructor",
                "instantiate"
            ],
            "support": {
                "issues": "https://github.com/doctrine/instantiator/issues",
                "source": "https://github.com/doctrine/instantiator/tree/1.4.0"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Finstantiator",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-10T18:47:58+00:00"
        },
        {
            "name": "doctrine/lexer",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/lexer.git",
                "reference": "e864bbf5904cb8f5bb334f99209b48018522f042"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/lexer/zipball/e864bbf5904cb8f5bb334f99209b48018522f042",
                "reference": "e864bbf5904cb8f5bb334f99209b48018522f042",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^6.0",
                "phpstan/phpstan": "^0.11.8",
                "phpunit/phpunit": "^8.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Lexer\\": "lib/Doctrine/Common/Lexer"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Lexer parser library that can be used in Top-Down, Recursive Descent Parsers.",
            "homepage": "https://www.doctrine-project.org/projects/lexer.html",
            "keywords": [
                "annotations",
                "docblock",
                "lexer",
                "parser",
                "php"
            ],
            "support": {
                "issues": "https://github.com/doctrine/lexer/issues",
                "source": "https://github.com/doctrine/lexer/tree/1.2.1"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Flexer",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-25T17:44:05+00:00"
        },
        {
            "name": "doctrine/migrations",
            "version": "2.3.2",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/migrations.git",
                "reference": "39520699043d9bfaaebeb81fa026bf2b02a8f735"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/migrations/zipball/39520699043d9bfaaebeb81fa026bf2b02a8f735",
                "reference": "39520699043d9bfaaebeb81fa026bf2b02a8f735",
                "shasum": ""
            },
            "require": {
                "composer/package-versions-deprecated": "^1.8",
                "doctrine/dbal": "^2.9",
                "friendsofphp/proxy-manager-lts": "^1.0",
                "php": "^7.1 || ^8.0",
                "symfony/console": "^3.4||^4.4.16||^5.0",
                "symfony/stopwatch": "^3.4||^4.0||^5.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^8.2",
                "doctrine/orm": "^2.6",
                "ext-pdo_sqlite": "*",
                "jdorn/sql-formatter": "^1.1",
                "mikey179/vfsstream": "^1.6",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-deprecation-rules": "^0.12",
                "phpstan/phpstan-phpunit": "^0.12",
                "phpstan/phpstan-strict-rules": "^0.12",
                "phpunit/phpunit": "^7.5 || ^8.5 || ^9.4",
                "symfony/process": "^3.4||^4.0||^5.0",
                "symfony/yaml": "^3.4||^4.0||^5.0"
            },
            "suggest": {
                "jdorn/sql-formatter": "Allows to generate formatted SQL with the diff command.",
                "symfony/yaml": "Allows the use of yaml for migration configuration files."
            },
            "bin": [
                "bin/doctrine-migrations"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Migrations\\": "lib/Doctrine/Migrations"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Michael Simonson",
                    "email": "contact@mikesimonson.com"
                }
            ],
            "description": "PHP Doctrine Migrations project offer additional functionality on top of the database abstraction layer (DBAL) for versioning your database schema and easily deploying changes to it. It is a very easy to use and a powerful tool.",
            "homepage": "https://www.doctrine-project.org/projects/migrations.html",
            "keywords": [
                "database",
                "dbal",
                "migrations",
                "php"
            ],
            "support": {
                "issues": "https://github.com/doctrine/migrations/issues",
                "source": "https://github.com/doctrine/migrations/tree/2.3.2"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fmigrations",
                    "type": "tidelift"
                }
            ],
            "time": "2020-12-23T14:06:04+00:00"
        },
        {
            "name": "doctrine/orm",
            "version": "2.7.5",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/orm.git",
                "reference": "01187c9260cd085529ddd1273665217cae659640"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/orm/zipball/01187c9260cd085529ddd1273665217cae659640",
                "reference": "01187c9260cd085529ddd1273665217cae659640",
                "shasum": ""
            },
            "require": {
                "composer/package-versions-deprecated": "^1.8",
                "doctrine/annotations": "^1.11.1",
                "doctrine/cache": "^1.9.1",
                "doctrine/collections": "^1.5",
                "doctrine/common": "^2.11 || ^3.0",
                "doctrine/dbal": "^2.9.3",
                "doctrine/event-manager": "^1.1",
                "doctrine/inflector": "^1.0",
                "doctrine/instantiator": "^1.3",
                "doctrine/lexer": "^1.0",
                "doctrine/persistence": "^1.3.3 || ^2.0",
                "ext-pdo": "*",
                "php": "^7.1",
                "symfony/console": "^3.0|^4.0|^5.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^6.0",
                "phpstan/phpstan": "^0.12.18",
                "phpunit/phpunit": "^8.0",
                "symfony/yaml": "^3.4|^4.0|^5.0",
                "vimeo/psalm": "^3.11"
            },
            "suggest": {
                "symfony/yaml": "If you want to use YAML Metadata Mapping Driver"
            },
            "bin": [
                "bin/doctrine"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.7.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\ORM\\": "lib/Doctrine/ORM"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                }
            ],
            "description": "Object-Relational-Mapper for PHP",
            "homepage": "https://www.doctrine-project.org/projects/orm.html",
            "keywords": [
                "database",
                "orm"
            ],
            "support": {
                "issues": "https://github.com/doctrine/orm/issues",
                "source": "https://github.com/doctrine/orm/tree/2.7.5"
            },
            "time": "2020-12-03T08:52:14+00:00"
        },
        {
            "name": "doctrine/persistence",
            "version": "1.3.8",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/persistence.git",
                "reference": "7a6eac9fb6f61bba91328f15aa7547f4806ca288"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/persistence/zipball/7a6eac9fb6f61bba91328f15aa7547f4806ca288",
                "reference": "7a6eac9fb6f61bba91328f15aa7547f4806ca288",
                "shasum": ""
            },
            "require": {
                "doctrine/annotations": "^1.0",
                "doctrine/cache": "^1.0",
                "doctrine/collections": "^1.0",
                "doctrine/event-manager": "^1.0",
                "doctrine/reflection": "^1.2",
                "php": "^7.1 || ^8.0"
            },
            "conflict": {
                "doctrine/common": "<2.10@dev"
            },
            "require-dev": {
                "doctrine/coding-standard": "^6.0",
                "phpstan/phpstan": "^0.11",
                "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0",
                "vimeo/psalm": "^3.11"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\": "lib/Doctrine/Common",
                    "Doctrine\\Persistence\\": "lib/Doctrine/Persistence"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                },
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                }
            ],
            "description": "The Doctrine Persistence project is a set of shared interfaces and functionality that the different Doctrine object mappers share.",
            "homepage": "https://doctrine-project.org/projects/persistence.html",
            "keywords": [
                "mapper",
                "object",
                "odm",
                "orm",
                "persistence"
            ],
            "support": {
                "issues": "https://github.com/doctrine/persistence/issues",
                "source": "https://github.com/doctrine/persistence/tree/1.3.x"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fpersistence",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-20T12:56:16+00:00"
        },
        {
            "name": "doctrine/reflection",
            "version": "1.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/reflection.git",
                "reference": "fa587178be682efe90d005e3a322590d6ebb59a5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/reflection/zipball/fa587178be682efe90d005e3a322590d6ebb59a5",
                "reference": "fa587178be682efe90d005e3a322590d6ebb59a5",
                "shasum": ""
            },
            "require": {
                "doctrine/annotations": "^1.0",
                "ext-tokenizer": "*",
                "php": "^7.1 || ^8.0"
            },
            "conflict": {
                "doctrine/common": "<2.9"
            },
            "require-dev": {
                "doctrine/coding-standard": "^6.0 || ^8.2.0",
                "doctrine/common": "^2.10",
                "phpstan/phpstan": "^0.11.0 || ^0.12.20",
                "phpstan/phpstan-phpunit": "^0.11.0 || ^0.12.16",
                "phpunit/phpunit": "^7.5 || ^9.1.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\": "lib/Doctrine/Common"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                },
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                }
            ],
            "description": "The Doctrine Reflection project is a simple library used by the various Doctrine projects which adds some additional functionality on top of the reflection functionality that comes with PHP. It allows you to get the reflection information about classes, methods and properties statically.",
            "homepage": "https://www.doctrine-project.org/projects/reflection.html",
            "keywords": [
                "reflection",
                "static"
            ],
            "support": {
                "issues": "https://github.com/doctrine/reflection/issues",
                "source": "https://github.com/doctrine/reflection/tree/1.2.2"
            },
            "abandoned": "roave/better-reflection",
            "time": "2020-10-27T21:46:55+00:00"
        },
        {
            "name": "doctrine/sql-formatter",
            "version": "1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/sql-formatter.git",
                "reference": "56070bebac6e77230ed7d306ad13528e60732871"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/sql-formatter/zipball/56070bebac6e77230ed7d306ad13528e60732871",
                "reference": "56070bebac6e77230ed7d306ad13528e60732871",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4"
            },
            "bin": [
                "bin/sql-formatter"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\SqlFormatter\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jeremy Dorn",
                    "email": "jeremy@jeremydorn.com",
                    "homepage": "http://jeremydorn.com/"
                }
            ],
            "description": "a PHP SQL highlighting library",
            "homepage": "https://github.com/doctrine/sql-formatter/",
            "keywords": [
                "highlight",
                "sql"
            ],
            "support": {
                "issues": "https://github.com/doctrine/sql-formatter/issues",
                "source": "https://github.com/doctrine/sql-formatter/tree/1.1.x"
            },
            "time": "2020-07-30T16:57:33+00:00"
        },
        {
            "name": "friendsofphp/proxy-manager-lts",
            "version": "v1.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/FriendsOfPHP/proxy-manager-lts.git",
                "reference": "121af47c9aee9c03031bdeca3fac0540f59aa5c3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/FriendsOfPHP/proxy-manager-lts/zipball/121af47c9aee9c03031bdeca3fac0540f59aa5c3",
                "reference": "121af47c9aee9c03031bdeca3fac0540f59aa5c3",
                "shasum": ""
            },
            "require": {
                "laminas/laminas-code": "~3.4.1|^4.0",
                "php": ">=7.1",
                "symfony/filesystem": "^4.4.17|^5.0"
            },
            "conflict": {
                "laminas/laminas-stdlib": "<3.2.1",
                "zendframework/zend-stdlib": "<3.2.1"
            },
            "replace": {
                "ocramius/proxy-manager": "^2.1"
            },
            "require-dev": {
                "ext-phar": "*",
                "symfony/phpunit-bridge": "^5.2"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "name": "ocramius/proxy-manager",
                    "url": "https://github.com/Ocramius/ProxyManager"
                }
            },
            "autoload": {
                "psr-4": {
                    "ProxyManager\\": "src/ProxyManager"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com",
                    "homepage": "http://ocramius.github.io/"
                },
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                }
            ],
            "description": "Adding support for a wider range of PHP versions to ocramius/proxy-manager",
            "homepage": "https://github.com/FriendsOfPHP/proxy-manager-lts",
            "keywords": [
                "aop",
                "lazy loading",
                "proxy",
                "proxy pattern",
                "service proxies"
            ],
            "support": {
                "issues": "https://github.com/FriendsOfPHP/proxy-manager-lts/issues",
                "source": "https://github.com/FriendsOfPHP/proxy-manager-lts/tree/v1.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/Ocramius",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/ocramius/proxy-manager",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-14T21:52:44+00:00"
        },
        {
            "name": "laminas/laminas-code",
            "version": "4.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/laminas/laminas-code.git",
                "reference": "28a6d70ea8b8bca687d7163300e611ae33baf82a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laminas/laminas-code/zipball/28a6d70ea8b8bca687d7163300e611ae33baf82a",
                "reference": "28a6d70ea8b8bca687d7163300e611ae33baf82a",
                "shasum": ""
            },
            "require": {
                "laminas/laminas-eventmanager": "^3.3",
                "php": "^7.4 || ~8.0.0"
            },
            "conflict": {
                "phpspec/prophecy": "<1.9.0"
            },
            "replace": {
                "zendframework/zend-code": "self.version"
            },
            "require-dev": {
                "doctrine/annotations": "^1.10.4",
                "ext-phar": "*",
                "laminas/laminas-coding-standard": "^2.1.4",
                "laminas/laminas-stdlib": "^3.3.0",
                "phpunit/phpunit": "^9.4.2",
                "psalm/plugin-phpunit": "^0.14.0",
                "vimeo/psalm": "^4.3.1"
            },
            "suggest": {
                "doctrine/annotations": "Doctrine\\Common\\Annotations >=1.0 for annotation features",
                "laminas/laminas-stdlib": "Laminas\\Stdlib component",
                "laminas/laminas-zendframework-bridge": "A bridge with Zend Framework"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Laminas\\Code\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "Extensions to the PHP Reflection API, static code scanning, and code generation",
            "homepage": "https://laminas.dev",
            "keywords": [
                "code",
                "laminas",
                "laminasframework"
            ],
            "support": {
                "chat": "https://laminas.dev/chat",
                "docs": "https://docs.laminas.dev/laminas-code/",
                "forum": "https://discourse.laminas.dev",
                "issues": "https://github.com/laminas/laminas-code/issues",
                "rss": "https://github.com/laminas/laminas-code/releases.atom",
                "source": "https://github.com/laminas/laminas-code"
            },
            "funding": [
                {
                    "url": "https://funding.communitybridge.org/projects/laminas-project",
                    "type": "community_bridge"
                }
            ],
            "time": "2020-12-30T16:16:14+00:00"
        },
        {
            "name": "laminas/laminas-eventmanager",
            "version": "3.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/laminas/laminas-eventmanager.git",
                "reference": "1940ccf30e058b2fd66f5a9d696f1b5e0027b082"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laminas/laminas-eventmanager/zipball/1940ccf30e058b2fd66f5a9d696f1b5e0027b082",
                "reference": "1940ccf30e058b2fd66f5a9d696f1b5e0027b082",
                "shasum": ""
            },
            "require": {
                "laminas/laminas-zendframework-bridge": "^1.0",
                "php": "^7.3 || ^8.0"
            },
            "replace": {
                "zendframework/zend-eventmanager": "^3.2.1"
            },
            "require-dev": {
                "container-interop/container-interop": "^1.1",
                "laminas/laminas-coding-standard": "~1.0.0",
                "laminas/laminas-stdlib": "^2.7.3 || ^3.0",
                "phpbench/phpbench": "^0.17.1",
                "phpunit/phpunit": "^8.5.8"
            },
            "suggest": {
                "container-interop/container-interop": "^1.1, to use the lazy listeners feature",
                "laminas/laminas-stdlib": "^2.7.3 || ^3.0, to use the FilterChain feature"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.3.x-dev",
                    "dev-develop": "3.4.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Laminas\\EventManager\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "Trigger and listen to events within a PHP application",
            "homepage": "https://laminas.dev",
            "keywords": [
                "event",
                "eventmanager",
                "events",
                "laminas"
            ],
            "support": {
                "chat": "https://laminas.dev/chat",
                "docs": "https://docs.laminas.dev/laminas-eventmanager/",
                "forum": "https://discourse.laminas.dev",
                "issues": "https://github.com/laminas/laminas-eventmanager/issues",
                "rss": "https://github.com/laminas/laminas-eventmanager/releases.atom",
                "source": "https://github.com/laminas/laminas-eventmanager"
            },
            "funding": [
                {
                    "url": "https://funding.communitybridge.org/projects/laminas-project",
                    "type": "community_bridge"
                }
            ],
            "time": "2020-08-25T11:10:44+00:00"
        },
        {
            "name": "laminas/laminas-zendframework-bridge",
            "version": "1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/laminas/laminas-zendframework-bridge.git",
                "reference": "6ede70583e101030bcace4dcddd648f760ddf642"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laminas/laminas-zendframework-bridge/zipball/6ede70583e101030bcace4dcddd648f760ddf642",
                "reference": "6ede70583e101030bcace4dcddd648f760ddf642",
                "shasum": ""
            },
            "require": {
                "php": "^5.6 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^5.7 || ^6.5 || ^7.5 || ^8.1 || ^9.3",
                "squizlabs/php_codesniffer": "^3.5"
            },
            "type": "library",
            "extra": {
                "laminas": {
                    "module": "Laminas\\ZendFrameworkBridge"
                }
            },
            "autoload": {
                "files": [
                    "src/autoload.php"
                ],
                "psr-4": {
                    "Laminas\\ZendFrameworkBridge\\": "src//"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "Alias legacy ZF class names to Laminas Project equivalents.",
            "keywords": [
                "ZendFramework",
                "autoloading",
                "laminas",
                "zf"
            ],
            "support": {
                "forum": "https://discourse.laminas.dev/",
                "issues": "https://github.com/laminas/laminas-zendframework-bridge/issues",
                "rss": "https://github.com/laminas/laminas-zendframework-bridge/releases.atom",
                "source": "https://github.com/laminas/laminas-zendframework-bridge"
            },
            "funding": [
                {
                    "url": "https://funding.communitybridge.org/projects/laminas-project",
                    "type": "community_bridge"
                }
            ],
            "time": "2020-09-14T14:23:00+00:00"
        },
        {
            "name": "lcobucci/clock",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/lcobucci/clock.git",
                "reference": "353d83fe2e6ae95745b16b3d911813df6a05bfb3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/lcobucci/clock/zipball/353d83fe2e6ae95745b16b3d911813df6a05bfb3",
                "reference": "353d83fe2e6ae95745b16b3d911813df6a05bfb3",
                "shasum": ""
            },
            "require": {
                "php": "^7.4 || ^8.0"
            },
            "require-dev": {
                "infection/infection": "^0.17",
                "lcobucci/coding-standard": "^6.0",
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-deprecation-rules": "^0.12",
                "phpstan/phpstan-phpunit": "^0.12",
                "phpstan/phpstan-strict-rules": "^0.12",
                "phpunit/php-code-coverage": "9.1.4",
                "phpunit/phpunit": "9.3.7"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Lcobucci\\Clock\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Luís Cobucci",
                    "email": "lcobucci@gmail.com"
                }
            ],
            "description": "Yet another clock abstraction",
            "support": {
                "issues": "https://github.com/lcobucci/clock/issues",
                "source": "https://github.com/lcobucci/clock/tree/2.0.x"
            },
            "funding": [
                {
                    "url": "https://github.com/lcobucci",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/lcobucci",
                    "type": "patreon"
                }
            ],
            "time": "2020-08-27T18:56:02+00:00"
        },
        {
            "name": "lcobucci/jwt",
            "version": "4.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/lcobucci/jwt.git",
                "reference": "2f533837091d0b76a89a059e7ed2b2732b2f459e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/lcobucci/jwt/zipball/2f533837091d0b76a89a059e7ed2b2732b2f459e",
                "reference": "2f533837091d0b76a89a059e7ed2b2732b2f459e",
                "shasum": ""
            },
            "require": {
                "ext-hash": "*",
                "ext-json": "*",
                "ext-mbstring": "*",
                "ext-openssl": "*",
                "ext-sodium": "*",
                "lcobucci/clock": "^2.0",
                "php": "^7.4 || ^8.0"
            },
            "require-dev": {
                "infection/infection": "^0.21",
                "lcobucci/coding-standard": "^6.0",
                "mikey179/vfsstream": "^1.6.7",
                "phpbench/phpbench": "^1.0@alpha",
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-deprecation-rules": "^0.12",
                "phpstan/phpstan-phpunit": "^0.12",
                "phpstan/phpstan-strict-rules": "^0.12",
                "phpunit/php-invoker": "^3.1",
                "phpunit/phpunit": "^9.5"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Lcobucci\\JWT\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Luís Cobucci",
                    "email": "lcobucci@gmail.com",
                    "role": "Developer"
                }
            ],
            "description": "A simple library to work with JSON Web Token and JSON Web Signature",
            "keywords": [
                "JWS",
                "jwt"
            ],
            "support": {
                "issues": "https://github.com/lcobucci/jwt/issues",
                "source": "https://github.com/lcobucci/jwt/tree/4.1.0"
            },
            "funding": [
                {
                    "url": "https://github.com/lcobucci",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/lcobucci",
                    "type": "patreon"
                }
            ],
            "time": "2021-01-28T00:57:26+00:00"
        },
        {
            "name": "lexik/jwt-authentication-bundle",
            "version": "v2.10.6",
            "source": {
                "type": "git",
                "url": "https://github.com/lexik/LexikJWTAuthenticationBundle.git",
                "reference": "dc472dd55d6a7bc374306e3df8e6202bc95f76e9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/lexik/LexikJWTAuthenticationBundle/zipball/dc472dd55d6a7bc374306e3df8e6202bc95f76e9",
                "reference": "dc472dd55d6a7bc374306e3df8e6202bc95f76e9",
                "shasum": ""
            },
            "require": {
                "ext-openssl": "*",
                "lcobucci/jwt": "^3.2|^4.0",
                "namshi/jose": "^7.2",
                "php": ">=5.6",
                "symfony/framework-bundle": "^3.4|^4.0|^5.0",
                "symfony/security-bundle": "^3.4|^4.0|^5.0"
            },
            "require-dev": {
                "symfony/browser-kit": "^3.4|^4.0|^5.0",
                "symfony/console": "^3.4|^4.0|^5.0",
                "symfony/dom-crawler": "^3.4|^4.0|^5.0",
                "symfony/phpunit-bridge": "^3.4|^4.0|^5.0",
                "symfony/var-dumper": "^3.4|^4.0|^5.0",
                "symfony/yaml": "^3.4|^4.0|^5.0"
            },
            "suggest": {
                "gesdinet/jwt-refresh-token-bundle": "Implements a refresh token system over Json Web Tokens in Symfony",
                "spomky-labs/lexik-jose-bridge": "Provides a JWT Token encoder with encryption support"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Lexik\\Bundle\\JWTAuthenticationBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jeremy Barthe",
                    "email": "j.barthe@lexik.fr",
                    "homepage": "https://github.com/jeremyb"
                },
                {
                    "name": "Nicolas Cabot",
                    "email": "n.cabot@lexik.fr",
                    "homepage": "https://github.com/slashfan"
                },
                {
                    "name": "Cedric Girard",
                    "email": "c.girard@lexik.fr",
                    "homepage": "https://github.com/cedric-g"
                },
                {
                    "name": "Dev Lexik",
                    "email": "dev@lexik.fr",
                    "homepage": "https://github.com/lexik"
                },
                {
                    "name": "Robin Chalas",
                    "email": "robin.chalas@gmail.com",
                    "homepage": "https://github.com/chalasr"
                },
                {
                    "name": "Lexik Community",
                    "homepage": "https://github.com/lexik/LexikJWTAuthenticationBundle/graphs/contributors"
                }
            ],
            "description": "This bundle provides JWT authentication for your Symfony REST API",
            "homepage": "https://github.com/lexik/LexikJWTAuthenticationBundle",
            "keywords": [
                "Authentication",
                "JWS",
                "api",
                "bundle",
                "jwt",
                "rest",
                "symfony"
            ],
            "support": {
                "issues": "https://github.com/lexik/LexikJWTAuthenticationBundle/issues",
                "source": "https://github.com/lexik/LexikJWTAuthenticationBundle/tree/v2.10.6"
            },
            "funding": [
                {
                    "url": "https://github.com/chalasr",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/lexik/jwt-authentication-bundle",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-20T18:11:13+00:00"
        },
        {
            "name": "namshi/jose",
            "version": "7.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/namshi/jose.git",
                "reference": "89a24d7eb3040e285dd5925fcad992378b82bcff"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/namshi/jose/zipball/89a24d7eb3040e285dd5925fcad992378b82bcff",
                "reference": "89a24d7eb3040e285dd5925fcad992378b82bcff",
                "shasum": ""
            },
            "require": {
                "ext-date": "*",
                "ext-hash": "*",
                "ext-json": "*",
                "ext-pcre": "*",
                "ext-spl": "*",
                "php": ">=5.5",
                "symfony/polyfill-php56": "^1.0"
            },
            "require-dev": {
                "phpseclib/phpseclib": "^2.0",
                "phpunit/phpunit": "^4.5|^5.0",
                "satooshi/php-coveralls": "^1.0"
            },
            "suggest": {
                "ext-openssl": "Allows to use OpenSSL as crypto engine.",
                "phpseclib/phpseclib": "Allows to use Phpseclib as crypto engine, use version ^2.0."
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Namshi\\JOSE\\": "src/Namshi/JOSE/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Alessandro Nadalin",
                    "email": "alessandro.nadalin@gmail.com"
                },
                {
                    "name": "Alessandro Cinelli (cirpo)",
                    "email": "alessandro.cinelli@gmail.com"
                }
            ],
            "description": "JSON Object Signing and Encryption library for PHP.",
            "keywords": [
                "JSON Web Signature",
                "JSON Web Token",
                "JWS",
                "json",
                "jwt",
                "token"
            ],
            "support": {
                "issues": "https://github.com/namshi/jose/issues",
                "source": "https://github.com/namshi/jose/tree/master"
            },
            "time": "2016-12-05T07:27:31+00:00"
        },
        {
            "name": "nelmio/api-doc-bundle",
            "version": "v4.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/nelmio/NelmioApiDocBundle.git",
                "reference": "42365c71ccce25b3ab722fb736e1c733b26beb8c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nelmio/NelmioApiDocBundle/zipball/42365c71ccce25b3ab722fb736e1c733b26beb8c",
                "reference": "42365c71ccce25b3ab722fb736e1c733b26beb8c",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": ">=7.1.3",
                "phpdocumentor/reflection-docblock": "^3.1|^4.4|^5.0",
                "symfony/framework-bundle": "^4.4|^5.0",
                "symfony/options-resolver": "^4.4|^5.0",
                "symfony/property-info": "^4.4|^5.0",
                "zircote/swagger-php": "^3.0"
            },
            "conflict": {
                "symfony/framework-bundle": "4.2.7"
            },
            "require-dev": {
                "api-platform/core": "^2.4",
                "doctrine/annotations": "^1.11",
                "doctrine/common": "^2.4",
                "friendsofsymfony/rest-bundle": "^2.8|^3.0",
                "jms/serializer": "^1.14|^3.0",
                "jms/serializer-bundle": "^2.3|^3.0",
                "sensio/framework-extra-bundle": "^4.4|^5.0",
                "symfony/asset": "^4.4|^5.0",
                "symfony/browser-kit": "^4.4|^5.0",
                "symfony/cache": "^4.4|^5.0",
                "symfony/config": "^4.4|^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/dom-crawler": "^4.4|^5.0",
                "symfony/form": "^4.4|^5.0",
                "symfony/phpunit-bridge": "^5.2",
                "symfony/property-access": "^4.4|^5.0",
                "symfony/routing": "^4.4|^5.0",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/templating": "^4.4|^5.0",
                "symfony/twig-bundle": "^4.4|^5.0",
                "symfony/validator": "^4.4|^5.0",
                "willdurand/hateoas-bundle": "^1.0|^2.0"
            },
            "suggest": {
                "api-platform/core": "For using an API oriented framework.",
                "friendsofsymfony/rest-bundle": "For using the parameters annotations."
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Nelmio\\ApiDocBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nelmio",
                    "homepage": "http://nelm.io"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://github.com/nelmio/NelmioApiDocBundle/contributors"
                }
            ],
            "description": "Generates documentation for your REST API from annotations",
            "keywords": [
                "api",
                "doc",
                "documentation",
                "rest"
            ],
            "support": {
                "issues": "https://github.com/nelmio/NelmioApiDocBundle/issues",
                "source": "https://github.com/nelmio/NelmioApiDocBundle/tree/v4.1.1"
            },
            "time": "2020-12-27T18:14:14+00:00"
        },
        {
            "name": "phpdocumentor/reflection-common",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionCommon.git",
                "reference": "1d01c49d4ed62f25aa84a747ad35d5a16924662b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionCommon/zipball/1d01c49d4ed62f25aa84a747ad35d5a16924662b",
                "reference": "1d01c49d4ed62f25aa84a747ad35d5a16924662b",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-2.x": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jaap van Otterdijk",
                    "email": "opensource@ijaap.nl"
                }
            ],
            "description": "Common reflection classes used by phpdocumentor to reflect the code structure",
            "homepage": "http://www.phpdoc.org",
            "keywords": [
                "FQSEN",
                "phpDocumentor",
                "phpdoc",
                "reflection",
                "static analysis"
            ],
            "support": {
                "issues": "https://github.com/phpDocumentor/ReflectionCommon/issues",
                "source": "https://github.com/phpDocumentor/ReflectionCommon/tree/2.x"
            },
            "time": "2020-06-27T09:03:43+00:00"
        },
        {
            "name": "phpdocumentor/reflection-docblock",
            "version": "5.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionDocBlock.git",
                "reference": "069a785b2141f5bcf49f3e353548dc1cce6df556"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionDocBlock/zipball/069a785b2141f5bcf49f3e353548dc1cce6df556",
                "reference": "069a785b2141f5bcf49f3e353548dc1cce6df556",
                "shasum": ""
            },
            "require": {
                "ext-filter": "*",
                "php": "^7.2 || ^8.0",
                "phpdocumentor/reflection-common": "^2.2",
                "phpdocumentor/type-resolver": "^1.3",
                "webmozart/assert": "^1.9.1"
            },
            "require-dev": {
                "mockery/mockery": "~1.3.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Mike van Riel",
                    "email": "me@mikevanriel.com"
                },
                {
                    "name": "Jaap van Otterdijk",
                    "email": "account@ijaap.nl"
                }
            ],
            "description": "With this component, a library can provide support for annotations via DocBlocks or otherwise retrieve information that is embedded in a DocBlock.",
            "support": {
                "issues": "https://github.com/phpDocumentor/ReflectionDocBlock/issues",
                "source": "https://github.com/phpDocumentor/ReflectionDocBlock/tree/master"
            },
            "time": "2020-09-03T19:13:55+00:00"
        },
        {
            "name": "phpdocumentor/type-resolver",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/TypeResolver.git",
                "reference": "6a467b8989322d92aa1c8bf2bebcc6e5c2ba55c0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/TypeResolver/zipball/6a467b8989322d92aa1c8bf2bebcc6e5c2ba55c0",
                "reference": "6a467b8989322d92aa1c8bf2bebcc6e5c2ba55c0",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0",
                "phpdocumentor/reflection-common": "^2.0"
            },
            "require-dev": {
                "ext-tokenizer": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-1.x": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Mike van Riel",
                    "email": "me@mikevanriel.com"
                }
            ],
            "description": "A PSR-5 based resolver of Class names, Types and Structural Element Names",
            "support": {
                "issues": "https://github.com/phpDocumentor/TypeResolver/issues",
                "source": "https://github.com/phpDocumentor/TypeResolver/tree/1.4.0"
            },
            "time": "2020-09-17T18:55:26+00:00"
        },
        {
            "name": "psr/cache",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/cache.git",
                "reference": "d11b50ad223250cf17b86e38383413f5a6764bf8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/cache/zipball/d11b50ad223250cf17b86e38383413f5a6764bf8",
                "reference": "d11b50ad223250cf17b86e38383413f5a6764bf8",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Cache\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common interface for caching libraries",
            "keywords": [
                "cache",
                "psr",
                "psr-6"
            ],
            "support": {
                "source": "https://github.com/php-fig/cache/tree/master"
            },
            "time": "2016-08-06T20:24:11+00:00"
        },
        {
            "name": "psr/container",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/container.git",
                "reference": "b7ce3b176482dbbc1245ebf52b181af44c2cf55f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/container/zipball/b7ce3b176482dbbc1245ebf52b181af44c2cf55f",
                "reference": "b7ce3b176482dbbc1245ebf52b181af44c2cf55f",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Container\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common Container Interface (PHP FIG PSR-11)",
            "homepage": "https://github.com/php-fig/container",
            "keywords": [
                "PSR-11",
                "container",
                "container-interface",
                "container-interop",
                "psr"
            ],
            "support": {
                "issues": "https://github.com/php-fig/container/issues",
                "source": "https://github.com/php-fig/container/tree/master"
            },
            "time": "2017-02-14T16:28:37+00:00"
        },
        {
            "name": "psr/event-dispatcher",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/event-dispatcher.git",
                "reference": "dbefd12671e8a14ec7f180cab83036ed26714bb0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/event-dispatcher/zipball/dbefd12671e8a14ec7f180cab83036ed26714bb0",
                "reference": "dbefd12671e8a14ec7f180cab83036ed26714bb0",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\EventDispatcher\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Standard interfaces for event handling.",
            "keywords": [
                "events",
                "psr",
                "psr-14"
            ],
            "support": {
                "issues": "https://github.com/php-fig/event-dispatcher/issues",
                "source": "https://github.com/php-fig/event-dispatcher/tree/1.0.0"
            },
            "time": "2019-01-08T18:20:26+00:00"
        },
        {
            "name": "psr/log",
            "version": "1.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/log.git",
                "reference": "0f73288fd15629204f9d42b7055f72dacbe811fc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/log/zipball/0f73288fd15629204f9d42b7055f72dacbe811fc",
                "reference": "0f73288fd15629204f9d42b7055f72dacbe811fc",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Log\\": "Psr/Log/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common interface for logging libraries",
            "homepage": "https://github.com/php-fig/log",
            "keywords": [
                "log",
                "psr",
                "psr-3"
            ],
            "support": {
                "source": "https://github.com/php-fig/log/tree/1.1.3"
            },
            "time": "2020-03-23T09:12:05+00:00"
        },
        {
            "name": "sensiolabs/security-checker",
            "version": "v6.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sensiolabs/security-checker.git",
                "reference": "a576c01520d9761901f269c4934ba55448be4a54"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sensiolabs/security-checker/zipball/a576c01520d9761901f269c4934ba55448be4a54",
                "reference": "a576c01520d9761901f269c4934ba55448be4a54",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1.3",
                "symfony/console": "^2.8|^3.4|^4.2|^5.0",
                "symfony/http-client": "^4.3|^5.0",
                "symfony/mime": "^4.3|^5.0",
                "symfony/polyfill-ctype": "^1.11"
            },
            "bin": [
                "security-checker"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "6.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "SensioLabs\\Security\\": "SensioLabs/Security"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien.potencier@gmail.com"
                }
            ],
            "description": "A security checker for your composer.lock",
            "support": {
                "issues": "https://github.com/sensiolabs/security-checker/issues",
                "source": "https://github.com/sensiolabs/security-checker/tree/master"
            },
            "abandoned": "https://github.com/fabpot/local-php-security-checker",
            "time": "2019-11-01T13:20:14+00:00"
        },
        {
            "name": "symfony/asset",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/asset.git",
                "reference": "aaf4ba865c02f6df999166a0148d56f2b11b11fb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/vault/assets/zipball/aaf4ba865c02f6df999166a0148d56f2b11b11fb",
                "reference": "aaf4ba865c02f6df999166a0148d56f2b11b11fb",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "require-dev": {
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/http-kernel": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/http-foundation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Asset\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Asset Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/vault/assets/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-30T20:12:43+00:00"
        },
        {
            "name": "symfony/cache",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/cache.git",
                "reference": "5da40a385c8182d18f4cca960bce7191c8f24e07"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/cache/zipball/5da40a385c8182d18f4cca960bce7191c8f24e07",
                "reference": "5da40a385c8182d18f4cca960bce7191c8f24e07",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/cache": "~1.0",
                "psr/log": "~1.0",
                "symfony/cache-contracts": "^1.1.7|^2",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/var-exporter": "^4.4|^5.0"
            },
            "conflict": {
                "doctrine/dbal": "<2.5",
                "symfony/dependency-injection": "<4.4",
                "symfony/http-kernel": "<4.4",
                "symfony/var-dumper": "<4.4"
            },
            "provide": {
                "psr/cache-implementation": "1.0",
                "psr/simple-cache-implementation": "1.0",
                "symfony/cache-implementation": "1.0"
            },
            "require-dev": {
                "cache/integration-tests": "dev-master",
                "doctrine/cache": "^1.6",
                "doctrine/dbal": "^2.5|^3.0",
                "predis/predis": "^1.1",
                "psr/simple-cache": "^1.0",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Cache\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Cache component with PSR-6, PSR-16, and tags",
            "homepage": "https://symfony.com",
            "keywords": [
                "caching",
                "psr6"
            ],
            "support": {
                "source": "https://github.com/symfony/cache/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T17:20:42+00:00"
        },
        {
            "name": "symfony/cache-contracts",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/cache-contracts.git",
                "reference": "8034ca0b61d4dd967f3698aaa1da2507b631d0cb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/cache-contracts/zipball/8034ca0b61d4dd967f3698aaa1da2507b631d0cb",
                "reference": "8034ca0b61d4dd967f3698aaa1da2507b631d0cb",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/cache": "^1.0"
            },
            "suggest": {
                "symfony/cache-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Cache\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to caching",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/cache-contracts/tree/v2.2.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-09-07T11:33:47+00:00"
        },
        {
            "name": "symfony/config",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/config.git",
                "reference": "2306321ef6a21a0de51a139774b6b7b38804815b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/config/zipball/2306321ef6a21a0de51a139774b6b7b38804815b",
                "reference": "2306321ef6a21a0de51a139774b6b7b38804815b",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/filesystem": "^4.4|^5.0",
                "symfony/polyfill-ctype": "~1.8"
            },
            "conflict": {
                "symfony/finder": "<4.4"
            },
            "require-dev": {
                "symfony/event-dispatcher": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/messenger": "^4.4|^5.0",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/yaml": "To use the yaml reference dumper"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Config\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Config Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/config/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-15T10:53:08+00:00"
        },
        {
            "name": "symfony/console",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/console.git",
                "reference": "95794074741645473221fb126d5cb4057ad25bf1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/console/zipball/95794074741645473221fb126d5cb4057ad25bf1",
                "reference": "95794074741645473221fb126d5cb4057ad25bf1",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php73": "^1.8",
                "symfony/polyfill-php80": "^1.15",
                "symfony/service-contracts": "^1.1|^2"
            },
            "conflict": {
                "symfony/dependency-injection": "<4.4",
                "symfony/event-dispatcher": "<4.4",
                "symfony/lock": "<4.4",
                "symfony/process": "<4.4"
            },
            "provide": {
                "psr/log-implementation": "1.0"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/event-dispatcher": "^4.4|^5.0",
                "symfony/lock": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "suggest": {
                "psr/log": "For using the console logger",
                "symfony/event-dispatcher": "",
                "symfony/lock": "",
                "symfony/process": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Console\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Console Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/console/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-06T13:22:03+00:00"
        },
        {
            "name": "symfony/dependency-injection",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dependency-injection.git",
                "reference": "9263d52372205c57823bf983bc4f413378830757"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dependency-injection/zipball/9263d52372205c57823bf983bc4f413378830757",
                "reference": "9263d52372205c57823bf983bc4f413378830757",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/container": "^1.0",
                "symfony/service-contracts": "^1.1.6|^2"
            },
            "conflict": {
                "symfony/config": "<5.0",
                "symfony/finder": "<4.4",
                "symfony/proxy-manager-bridge": "<4.4",
                "symfony/yaml": "<4.4"
            },
            "provide": {
                "psr/container-implementation": "1.0",
                "symfony/service-implementation": "1.0"
            },
            "require-dev": {
                "symfony/config": "^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/config": "",
                "symfony/expression-language": "For using expressions in service container configuration",
                "symfony/finder": "For using double-star glob patterns or when GLOB_BRACE portability is required",
                "symfony/proxy-manager-bridge": "Generate service proxies to lazy load them",
                "symfony/yaml": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\DependencyInjection\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony DependencyInjection Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/dependency-injection/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T08:36:09+00:00"
        },
        {
            "name": "symfony/doctrine-bridge",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/doctrine-bridge.git",
                "reference": "e2ab3fe26133c5d997684f1b961acbd6b04e2805"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/doctrine-bridge/zipball/e2ab3fe26133c5d997684f1b961acbd6b04e2805",
                "reference": "e2ab3fe26133c5d997684f1b961acbd6b04e2805",
                "shasum": ""
            },
            "require": {
                "doctrine/event-manager": "~1.0",
                "doctrine/persistence": "^1.3|^2",
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/service-contracts": "^1.1|^2"
            },
            "conflict": {
                "phpunit/phpunit": "<5.4.3",
                "symfony/dependency-injection": "<4.4",
                "symfony/form": "<5",
                "symfony/http-kernel": "<5",
                "symfony/messenger": "<4.4",
                "symfony/property-info": "<5",
                "symfony/security-bundle": "<5",
                "symfony/security-core": "<5",
                "symfony/validator": "<5.0.2"
            },
            "require-dev": {
                "composer/package-versions-deprecated": "^1.8",
                "doctrine/annotations": "~1.7",
                "doctrine/cache": "~1.6",
                "doctrine/collections": "~1.0",
                "doctrine/data-fixtures": "^1.1",
                "doctrine/dbal": "~2.4",
                "doctrine/orm": "^2.6.3",
                "doctrine/reflection": "~1.0",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/form": "^5.0",
                "symfony/http-kernel": "^5.0",
                "symfony/messenger": "^4.4|^5.0",
                "symfony/property-access": "^4.4|^5.0",
                "symfony/property-info": "^5.0",
                "symfony/proxy-manager-bridge": "^4.4|^5.0",
                "symfony/security-core": "^5.0",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/translation": "^4.4|^5.0",
                "symfony/validator": "^5.0.2",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "suggest": {
                "doctrine/data-fixtures": "",
                "doctrine/dbal": "",
                "doctrine/orm": "",
                "symfony/form": "",
                "symfony/property-info": "",
                "symfony/validator": ""
            },
            "type": "symfony-bridge",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bridge\\Doctrine\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Doctrine Bridge",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/doctrine-bridge/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T16:54:02+00:00"
        },
        {
            "name": "symfony/dotenv",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dotenv.git",
                "reference": "efd887f012127acad22325d109fe8ddf635f1f97"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dotenv/zipball/efd887f012127acad22325d109fe8ddf635f1f97",
                "reference": "efd887f012127acad22325d109fe8ddf635f1f97",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "require-dev": {
                "symfony/process": "^4.4|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Dotenv\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Registers environment variables from a .env file",
            "homepage": "https://symfony.com",
            "keywords": [
                "dotenv",
                "env",
                "environment"
            ],
            "support": {
                "source": "https://github.com/symfony/dotenv/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-28T08:20:26+00:00"
        },
        {
            "name": "symfony/error-handler",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/error-handler.git",
                "reference": "d01fba9a55614a1addb0d52d6a9566560b2a2af8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/error-handler/zipball/d01fba9a55614a1addb0d52d6a9566560b2a2af8",
                "reference": "d01fba9a55614a1addb0d52d6a9566560b2a2af8",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/log": "^1.0",
                "symfony/polyfill-php80": "^1.15",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "require-dev": {
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/serializer": "^4.4|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\ErrorHandler\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony ErrorHandler Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/error-handler/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T08:36:09+00:00"
        },
        {
            "name": "symfony/event-dispatcher",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher.git",
                "reference": "5c5dd86c7a7962d28c48351c7dd83c9266e4d19d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher/zipball/5c5dd86c7a7962d28c48351c7dd83c9266e4d19d",
                "reference": "5c5dd86c7a7962d28c48351c7dd83c9266e4d19d",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/event-dispatcher-contracts": "^2"
            },
            "conflict": {
                "symfony/dependency-injection": "<4.4"
            },
            "provide": {
                "psr/event-dispatcher-implementation": "1.0",
                "symfony/event-dispatcher-implementation": "2.0"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/stopwatch": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/dependency-injection": "",
                "symfony/http-kernel": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\EventDispatcher\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony EventDispatcher Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/event-dispatcher/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-18T18:18:56+00:00"
        },
        {
            "name": "symfony/event-dispatcher-contracts",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher-contracts.git",
                "reference": "0ba7d54483095a198fa51781bc608d17e84dffa2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher-contracts/zipball/0ba7d54483095a198fa51781bc608d17e84dffa2",
                "reference": "0ba7d54483095a198fa51781bc608d17e84dffa2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/event-dispatcher": "^1"
            },
            "suggest": {
                "symfony/event-dispatcher-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\EventDispatcher\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to dispatching event",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/event-dispatcher-contracts/tree/v2.2.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-09-07T11:33:47+00:00"
        },
        {
            "name": "symfony/filesystem",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/filesystem.git",
                "reference": "6edf8b9e64e662fcde20ee3ee2ec46fdcc8c3214"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/filesystem/zipball/6edf8b9e64e662fcde20ee3ee2ec46fdcc8c3214",
                "reference": "6edf8b9e64e662fcde20ee3ee2ec46fdcc8c3214",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Filesystem\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Filesystem Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/filesystem/tree/v5.0.9"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-30T20:12:43+00:00"
        },
        {
            "name": "symfony/finder",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/finder.git",
                "reference": "127bccabf3c854625af9c0162779cf06bc1dd352"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/finder/zipball/127bccabf3c854625af9c0162779cf06bc1dd352",
                "reference": "127bccabf3c854625af9c0162779cf06bc1dd352",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Finder\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Finder Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/finder/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-20T17:38:26+00:00"
        },
        {
            "name": "symfony/flex",
            "version": "v1.12.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/flex.git",
                "reference": "394f3e4dc03ea2a5448aeedc9658c8b596b1d39f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/flex/zipball/394f3e4dc03ea2a5448aeedc9658c8b596b1d39f",
                "reference": "394f3e4dc03ea2a5448aeedc9658c8b596b1d39f",
                "shasum": ""
            },
            "require": {
                "composer-plugin-api": "^1.0|^2.0",
                "php": ">=7.1"
            },
            "require-dev": {
                "composer/composer": "^1.0.2|^2.0",
                "symfony/dotenv": "^4.4|^5.0",
                "symfony/filesystem": "^4.4|^5.0",
                "symfony/phpunit-bridge": "^4.4|^5.0",
                "symfony/process": "^3.4|^4.4|^5.0"
            },
            "type": "composer-plugin",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.9-dev"
                },
                "class": "Symfony\\Flex\\Flex"
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Flex\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien.potencier@gmail.com"
                }
            ],
            "description": "Composer plugin for Symfony",
            "support": {
                "issues": "https://github.com/symfony/flex/issues",
                "source": "https://github.com/symfony/flex/tree/v1.12.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-02T16:29:45+00:00"
        },
        {
            "name": "symfony/framework-bundle",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/framework-bundle.git",
                "reference": "0fc0a93f8bbe465d0b483e21b087d432baa92c16"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/framework-bundle/zipball/0fc0a93f8bbe465d0b483e21b087d432baa92c16",
                "reference": "0fc0a93f8bbe465d0b483e21b087d432baa92c16",
                "shasum": ""
            },
            "require": {
                "ext-xml": "*",
                "php": ">=7.2.5",
                "symfony/cache": "^4.4|^5.0",
                "symfony/config": "^5.0",
                "symfony/dependency-injection": "^5.0.1",
                "symfony/error-handler": "^4.4.1|^5.0.1",
                "symfony/filesystem": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/http-kernel": "^5.0",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/routing": "^5.0"
            },
            "conflict": {
                "doctrine/persistence": "<1.3",
                "phpdocumentor/reflection-docblock": "<3.0",
                "phpdocumentor/type-resolver": "<0.2.1",
                "phpunit/phpunit": "<5.4.3",
                "symfony/asset": "<4.4",
                "symfony/browser-kit": "<4.4",
                "symfony/console": "<4.4",
                "symfony/dom-crawler": "<4.4",
                "symfony/dotenv": "<4.4",
                "symfony/form": "<4.4",
                "symfony/http-client": "<4.4",
                "symfony/lock": "<4.4",
                "symfony/mailer": "<4.4",
                "symfony/messenger": "<4.4",
                "symfony/mime": "<4.4",
                "symfony/property-info": "<4.4",
                "symfony/serializer": "<4.4",
                "symfony/stopwatch": "<4.4",
                "symfony/translation": "<5.0",
                "symfony/twig-bridge": "<4.4",
                "symfony/twig-bundle": "<4.4",
                "symfony/validator": "<4.4",
                "symfony/web-profiler-bundle": "<4.4",
                "symfony/workflow": "<4.4"
            },
            "require-dev": {
                "doctrine/annotations": "~1.7",
                "doctrine/cache": "~1.0",
                "paragonie/sodium_compat": "^1.8",
                "phpdocumentor/reflection-docblock": "^3.0|^4.0",
                "symfony/asset": "^4.4|^5.0",
                "symfony/browser-kit": "^4.4|^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/css-selector": "^4.4|^5.0",
                "symfony/dom-crawler": "^4.4|^5.0",
                "symfony/dotenv": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/form": "^4.4|^5.0",
                "symfony/http-client": "^4.4|^5.0",
                "symfony/lock": "^4.4|^5.0",
                "symfony/mailer": "^4.4|^5.0",
                "symfony/messenger": "^4.4|^5.0",
                "symfony/mime": "^4.4|^5.0",
                "symfony/polyfill-intl-icu": "~1.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/property-info": "^4.4|^5.0",
                "symfony/security-csrf": "^4.4|^5.0",
                "symfony/security-http": "^4.4|^5.0",
                "symfony/serializer": "^4.4|^5.0",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/string": "~5.0.0",
                "symfony/translation": "^5.0",
                "symfony/twig-bundle": "^4.4|^5.0",
                "symfony/validator": "^4.4|^5.0",
                "symfony/web-link": "^4.4|^5.0",
                "symfony/workflow": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0",
                "twig/twig": "^2.10|^3.0"
            },
            "suggest": {
                "ext-apcu": "For best performance of the system caches",
                "symfony/console": "For using the console commands",
                "symfony/form": "For using forms",
                "symfony/property-info": "For using the property_info service",
                "symfony/serializer": "For using the serializer service",
                "symfony/validator": "For using validation",
                "symfony/web-link": "For using web links, features such as preloading, prefetching or prerendering",
                "symfony/yaml": "For using the debug:config and lint:yaml commands"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\FrameworkBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony FrameworkBundle",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/framework-bundle/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T08:36:09+00:00"
        },
        {
            "name": "symfony/http-client",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-client.git",
                "reference": "9eec6ed50ea38f562ce0a1fc8a7d96a010d58509"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-client/zipball/9eec6ed50ea38f562ce0a1fc8a7d96a010d58509",
                "reference": "9eec6ed50ea38f562ce0a1fc8a7d96a010d58509",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/log": "^1.0",
                "symfony/http-client-contracts": "^1.1.8|^2",
                "symfony/polyfill-php73": "^1.11",
                "symfony/service-contracts": "^1.0|^2"
            },
            "provide": {
                "php-http/async-client-implementation": "*",
                "php-http/client-implementation": "*",
                "psr/http-client-implementation": "1.0",
                "symfony/http-client-implementation": "1.1"
            },
            "require-dev": {
                "guzzlehttp/promises": "^1.3.1",
                "nyholm/psr7": "^1.0",
                "php-http/httplug": "^1.0|^2.0",
                "psr/http-client": "^1.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpClient\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony HttpClient component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-client/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-05T09:43:09+00:00"
        },
        {
            "name": "symfony/http-client-contracts",
            "version": "v2.3.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-client-contracts.git",
                "reference": "41db680a15018f9c1d4b23516059633ce280ca33"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-client-contracts/zipball/41db680a15018f9c1d4b23516059633ce280ca33",
                "reference": "41db680a15018f9c1d4b23516059633ce280ca33",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "suggest": {
                "symfony/http-client-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-version": "2.3",
                "branch-alias": {
                    "dev-main": "2.3-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\HttpClient\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to HTTP clients",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/http-client-contracts/tree/v2.3.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-10-14T17:08:19+00:00"
        },
        {
            "name": "symfony/http-foundation",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-foundation.git",
                "reference": "7ad89bbacd90f7bee1a57e61ed5ecaeaba430706"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-foundation/zipball/7ad89bbacd90f7bee1a57e61ed5ecaeaba430706",
                "reference": "7ad89bbacd90f7bee1a57e61ed5ecaeaba430706",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/mime": "^4.4|^5.0",
                "symfony/polyfill-mbstring": "~1.1"
            },
            "require-dev": {
                "predis/predis": "~1.0",
                "symfony/expression-language": "^4.4|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpFoundation\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony HttpFoundation Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-foundation/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T10:04:24+00:00"
        },
        {
            "name": "symfony/http-kernel",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-kernel.git",
                "reference": "410ce82fbbb06fb926ecaacea8b0af86bc3e7ef2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-kernel/zipball/410ce82fbbb06fb926ecaacea8b0af86bc3e7ef2",
                "reference": "410ce82fbbb06fb926ecaacea8b0af86bc3e7ef2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/log": "~1.0",
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/event-dispatcher": "^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/polyfill-ctype": "^1.8",
                "symfony/polyfill-php73": "^1.9",
                "symfony/polyfill-php80": "^1.15"
            },
            "conflict": {
                "symfony/browser-kit": "<4.4",
                "symfony/cache": "<5.0",
                "symfony/config": "<5.0",
                "symfony/console": "<4.4",
                "symfony/dependency-injection": "<4.4",
                "symfony/doctrine-bridge": "<5.0",
                "symfony/form": "<5.0",
                "symfony/http-client": "<5.0",
                "symfony/mailer": "<5.0",
                "symfony/messenger": "<5.0",
                "symfony/translation": "<5.0",
                "symfony/twig-bridge": "<5.0",
                "symfony/validator": "<5.0",
                "twig/twig": "<2.4"
            },
            "provide": {
                "psr/log-implementation": "1.0"
            },
            "require-dev": {
                "psr/cache": "~1.0",
                "symfony/browser-kit": "^4.4|^5.0",
                "symfony/config": "^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/css-selector": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/dom-crawler": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/routing": "^4.4|^5.0",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/translation": "^4.4|^5.0",
                "symfony/translation-contracts": "^1.1|^2",
                "twig/twig": "^2.4|^3.0"
            },
            "suggest": {
                "symfony/browser-kit": "",
                "symfony/config": "",
                "symfony/console": "",
                "symfony/dependency-injection": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpKernel\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony HttpKernel Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-kernel/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-24T04:14:59+00:00"
        },
        {
            "name": "symfony/inflector",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/inflector.git",
                "reference": "7eff2643934179cd0e5a6609a583fc22fc495fc4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/inflector/zipball/7eff2643934179cd0e5a6609a583fc22fc495fc4",
                "reference": "7eff2643934179cd0e5a6609a583fc22fc495fc4",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Inflector\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Inflector Component",
            "homepage": "https://symfony.com",
            "keywords": [
                "inflection",
                "pluralize",
                "singularize",
                "string",
                "symfony",
                "words"
            ],
            "support": {
                "source": "https://github.com/symfony/inflector/tree/v5.0.9"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-20T17:38:26+00:00"
        },
        {
            "name": "symfony/messenger",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/messenger.git",
                "reference": "171fa0b6a95a96664bece9e1f9e914ea699ff79f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/messenger/zipball/171fa0b6a95a96664bece9e1f9e914ea699ff79f",
                "reference": "171fa0b6a95a96664bece9e1f9e914ea699ff79f",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/log": "^1.0",
                "symfony/polyfill-php80": "^1.15"
            },
            "conflict": {
                "doctrine/persistence": "<1.3",
                "symfony/event-dispatcher": "<4.4",
                "symfony/framework-bundle": "<4.4",
                "symfony/http-kernel": "<4.4"
            },
            "require-dev": {
                "doctrine/dbal": "^2.6|^3.0",
                "doctrine/persistence": "^1.3|^2",
                "psr/cache": "~1.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/event-dispatcher": "^4.4|^5.0",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/property-access": "^4.4|^5.0",
                "symfony/serializer": "^4.4|^5.0",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/validator": "^4.4|^5.0"
            },
            "suggest": {
                "enqueue/messenger-adapter": "For using the php-enqueue library as a transport."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Messenger\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Samuel Roze",
                    "email": "samuel.roze@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Messenger Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/messenger/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T16:54:02+00:00"
        },
        {
            "name": "symfony/mime",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/mime.git",
                "reference": "aa2b2013a8d380e3980a29a79cc0fbcfb02fb920"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/mime/zipball/aa2b2013a8d380e3980a29a79cc0fbcfb02fb920",
                "reference": "aa2b2013a8d380e3980a29a79cc0fbcfb02fb920",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-intl-idn": "^1.10",
                "symfony/polyfill-mbstring": "^1.0"
            },
            "conflict": {
                "symfony/mailer": "<4.4"
            },
            "require-dev": {
                "egulias/email-validator": "^2.1.10",
                "symfony/dependency-injection": "^4.4|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Mime\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "A library to manipulate MIME messages",
            "homepage": "https://symfony.com",
            "keywords": [
                "mime",
                "mime-type"
            ],
            "support": {
                "source": "https://github.com/symfony/mime/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T10:04:24+00:00"
        },
        {
            "name": "symfony/options-resolver",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/options-resolver.git",
                "reference": "9f39c468be4b6dae1bad2422f98bab65734055e2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/options-resolver/zipball/9f39c468be4b6dae1bad2422f98bab65734055e2",
                "reference": "9f39c468be4b6dae1bad2422f98bab65734055e2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\OptionsResolver\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony OptionsResolver Component",
            "homepage": "https://symfony.com",
            "keywords": [
                "config",
                "configuration",
                "options"
            ],
            "support": {
                "source": "https://github.com/symfony/options-resolver/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-12T12:51:51+00:00"
        },
        {
            "name": "symfony/orm-pack",
            "version": "v1.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/orm-pack.git",
                "reference": "21ac491414b5815e5ebb7425908c1d1568d2e775"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/orm-pack/zipball/21ac491414b5815e5ebb7425908c1d1568d2e775",
                "reference": "21ac491414b5815e5ebb7425908c1d1568d2e775",
                "shasum": ""
            },
            "require": {
                "composer/package-versions-deprecated": "*",
                "doctrine/common": "^2",
                "doctrine/doctrine-bundle": "^2",
                "doctrine/doctrine-migrations-bundle": "^2",
                "doctrine/orm": "^2"
            },
            "type": "symfony-pack",
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A pack for the Doctrine ORM",
            "support": {
                "issues": "https://github.com/symfony/orm-pack/issues",
                "source": "https://github.com/symfony/orm-pack/tree/v1.2.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-08-31T10:20:18+00:00"
        },
        {
            "name": "symfony/polyfill-intl-idn",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-idn.git",
                "reference": "0eb8293dbbcd6ef6bf81404c9ce7d95bcdf34f44"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-idn/zipball/0eb8293dbbcd6ef6bf81404c9ce7d95bcdf34f44",
                "reference": "0eb8293dbbcd6ef6bf81404c9ce7d95bcdf34f44",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1",
                "symfony/polyfill-intl-normalizer": "^1.10",
                "symfony/polyfill-php72": "^1.10"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Idn\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Laurent Bassin",
                    "email": "laurent@bassin.info"
                },
                {
                    "name": "Trevor Rowbotham",
                    "email": "trevor.rowbotham@pm.me"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for intl's idn_to_ascii and idn_to_utf8 functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "idn",
                "intl",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-idn/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/polyfill-intl-normalizer",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-normalizer.git",
                "reference": "6e971c891537eb617a00bb07a43d182a6915faba"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-normalizer/zipball/6e971c891537eb617a00bb07a43d182a6915faba",
                "reference": "6e971c891537eb617a00bb07a43d182a6915faba",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Normalizer\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for intl's Normalizer class and related functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "intl",
                "normalizer",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-normalizer/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T17:09:11+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "f377a3dd1fde44d37b9831d68dc8dea3ffd28e13"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/f377a3dd1fde44d37b9831d68dc8dea3ffd28e13",
                "reference": "f377a3dd1fde44d37b9831d68dc8dea3ffd28e13",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-mbstring": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Mbstring\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for the Mbstring extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "mbstring",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-mbstring/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/polyfill-php73",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php73.git",
                "reference": "a678b42e92f86eca04b7fa4c0f6f19d097fb69e2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php73/zipball/a678b42e92f86eca04b7fa4c0f6f19d097fb69e2",
                "reference": "a678b42e92f86eca04b7fa4c0f6f19d097fb69e2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php73\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 7.3+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php73/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/polyfill-php80",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php80.git",
                "reference": "dc3063ba22c2a1fd2f45ed856374d79114998f91"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php80/zipball/dc3063ba22c2a1fd2f45ed856374d79114998f91",
                "reference": "dc3063ba22c2a1fd2f45ed856374d79114998f91",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php80\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ion Bazan",
                    "email": "ion.bazan@gmail.com"
                },
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 8.0+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php80/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/property-access",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/property-access.git",
                "reference": "fdc47c3780ebb29077c3421c6253ccc91040c24a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/property-access/zipball/fdc47c3780ebb29077c3421c6253ccc91040c24a",
                "reference": "fdc47c3780ebb29077c3421c6253ccc91040c24a",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/inflector": "^4.4|^5.0"
            },
            "require-dev": {
                "symfony/cache": "^4.4|^5.0"
            },
            "suggest": {
                "psr/cache-implementation": "To cache access methods."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\PropertyAccess\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony PropertyAccess Component",
            "homepage": "https://symfony.com",
            "keywords": [
                "access",
                "array",
                "extraction",
                "index",
                "injection",
                "object",
                "property",
                "property path",
                "reflection"
            ],
            "support": {
                "source": "https://github.com/symfony/property-access/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-18T18:18:56+00:00"
        },
        {
            "name": "symfony/property-info",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/property-info.git",
                "reference": "ab2210c90e8038ffaad09fe10cf635ad31bebb62"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/property-info/zipball/ab2210c90e8038ffaad09fe10cf635ad31bebb62",
                "reference": "ab2210c90e8038ffaad09fe10cf635ad31bebb62",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/inflector": "^4.4|^5.0"
            },
            "conflict": {
                "phpdocumentor/reflection-docblock": "<3.2.2",
                "phpdocumentor/type-resolver": "<0.3.0",
                "symfony/dependency-injection": "<4.4"
            },
            "require-dev": {
                "doctrine/annotations": "~1.7",
                "phpdocumentor/reflection-docblock": "^3.0|^4.0|^5.0",
                "symfony/cache": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/serializer": "^4.4|^5.0"
            },
            "suggest": {
                "phpdocumentor/reflection-docblock": "To use the PHPDoc",
                "psr/cache-implementation": "To cache results",
                "symfony/doctrine-bridge": "To use Doctrine metadata",
                "symfony/serializer": "To use Serializer metadata"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\PropertyInfo\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Kévin Dunglas",
                    "email": "dunglas@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Property Info Component",
            "homepage": "https://symfony.com",
            "keywords": [
                "doctrine",
                "phpdoc",
                "property",
                "symfony",
                "type",
                "validator"
            ],
            "support": {
                "source": "https://github.com/symfony/property-info/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-18T21:17:00+00:00"
        },
        {
            "name": "symfony/routing",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/routing.git",
                "reference": "1369ee6823074c406815b65a40d47fd5ee48e517"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/routing/zipball/1369ee6823074c406815b65a40d47fd5ee48e517",
                "reference": "1369ee6823074c406815b65a40d47fd5ee48e517",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "conflict": {
                "symfony/config": "<5.0",
                "symfony/dependency-injection": "<4.4",
                "symfony/yaml": "<4.4"
            },
            "require-dev": {
                "doctrine/annotations": "~1.2",
                "psr/log": "~1.0",
                "symfony/config": "^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "doctrine/annotations": "For using the annotation loader",
                "symfony/config": "For using the all-in-one router or any loader",
                "symfony/expression-language": "For using expression matching",
                "symfony/http-foundation": "For using a Symfony Request object",
                "symfony/yaml": "For using the YAML loader"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Routing\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Routing Component",
            "homepage": "https://symfony.com",
            "keywords": [
                "router",
                "routing",
                "uri",
                "url"
            ],
            "support": {
                "source": "https://github.com/symfony/routing/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-18T18:18:56+00:00"
        },
        {
            "name": "symfony/security-bundle",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/security-bundle.git",
                "reference": "8e8b20291be3b4f9aed4da706450dc355ee036ac"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/security-bundle/zipball/8e8b20291be3b4f9aed4da706450dc355ee036ac",
                "reference": "8e8b20291be3b4f9aed4da706450dc355ee036ac",
                "shasum": ""
            },
            "require": {
                "ext-xml": "*",
                "php": ">=7.2.5",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/http-kernel": "^5.0",
                "symfony/security-core": "^4.4|^5.0",
                "symfony/security-csrf": "^4.4|^5.0",
                "symfony/security-guard": "^4.4|^5.0",
                "symfony/security-http": "^4.4.5|^5.0.5"
            },
            "conflict": {
                "symfony/browser-kit": "<4.4",
                "symfony/console": "<4.4",
                "symfony/framework-bundle": "<4.4",
                "symfony/ldap": "<4.4",
                "symfony/twig-bundle": "<4.4"
            },
            "require-dev": {
                "doctrine/doctrine-bundle": "^2.0",
                "symfony/asset": "^4.4|^5.0",
                "symfony/browser-kit": "^4.4|^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/css-selector": "^4.4|^5.0",
                "symfony/dom-crawler": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/form": "^4.4|^5.0",
                "symfony/framework-bundle": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/serializer": "^4.4|^5.0",
                "symfony/translation": "^4.4|^5.0",
                "symfony/twig-bridge": "^4.4|^5.0",
                "symfony/twig-bundle": "^4.4|^5.0",
                "symfony/validator": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0",
                "twig/twig": "^2.10|^3.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\SecurityBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony SecurityBundle",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/security-bundle/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T08:36:09+00:00"
        },
        {
            "name": "symfony/security-core",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/security-core.git",
                "reference": "4e4c76fcb091e35aca0601fc337f0c2cf76885ab"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/security-core/zipball/4e4c76fcb091e35aca0601fc337f0c2cf76885ab",
                "reference": "4e4c76fcb091e35aca0601fc337f0c2cf76885ab",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/event-dispatcher-contracts": "^1.1|^2",
                "symfony/service-contracts": "^1.1.6|^2"
            },
            "conflict": {
                "symfony/event-dispatcher": "<4.4",
                "symfony/ldap": "<4.4",
                "symfony/security-guard": "<4.4"
            },
            "require-dev": {
                "psr/container": "^1.0",
                "psr/log": "~1.0",
                "symfony/event-dispatcher": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/ldap": "^4.4|^5.0",
                "symfony/validator": "^4.4|^5.0"
            },
            "suggest": {
                "psr/container-implementation": "To instantiate the Security class",
                "symfony/event-dispatcher": "",
                "symfony/expression-language": "For using the expression voter",
                "symfony/http-foundation": "",
                "symfony/ldap": "For using LDAP integration",
                "symfony/validator": "For using the user password constraint"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Security\\Core\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Security Component - Core Library",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/security-core/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-25T09:01:55+00:00"
        },
        {
            "name": "symfony/security-csrf",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/security-csrf.git",
                "reference": "155a413dc29400e74d2c06f5581da795200386c1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/security-csrf/zipball/155a413dc29400e74d2c06f5581da795200386c1",
                "reference": "155a413dc29400e74d2c06f5581da795200386c1",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/security-core": "^4.4|^5.0"
            },
            "conflict": {
                "symfony/http-foundation": "<4.4"
            },
            "require-dev": {
                "symfony/http-foundation": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/http-foundation": "For using the class SessionTokenStorage."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Security\\Csrf\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Security Component - CSRF Library",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/security-csrf/tree/v5.0.9"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-20T17:38:26+00:00"
        },
        {
            "name": "symfony/security-guard",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/security-guard.git",
                "reference": "4d920d91fa44be8ebfe1a101dadde48181d8a4fb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/security-guard/zipball/4d920d91fa44be8ebfe1a101dadde48181d8a4fb",
                "reference": "4d920d91fa44be8ebfe1a101dadde48181d8a4fb",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/security-core": "^5.0",
                "symfony/security-http": "^4.4.1|^5.0.1"
            },
            "require-dev": {
                "psr/log": "~1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Security\\Guard\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Security Component - Guard",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/security-guard/tree/v5.0.9"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-20T17:38:26+00:00"
        },
        {
            "name": "symfony/security-http",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/security-http.git",
                "reference": "e18913e3663dde1d4712c921211d12185c323c6e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/security-http/zipball/e18913e3663dde1d4712c921211d12185c323c6e",
                "reference": "e18913e3663dde1d4712c921211d12185c323c6e",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/http-foundation": "^4.4.7|^5.0.7",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/property-access": "^4.4|^5.0",
                "symfony/security-core": "^4.4.8|^5.0.8"
            },
            "conflict": {
                "symfony/security-csrf": "<4.4"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/routing": "^4.4|^5.0",
                "symfony/security-csrf": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/routing": "For using the HttpUtils class to create sub-requests, redirect the user, and match URLs",
                "symfony/security-csrf": "For using tokens to protect authentication/logout attempts"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Security\\Http\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Security Component - HTTP Integration",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/security-http/tree/v5.0.10"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-28T12:17:48+00:00"
        },
        {
            "name": "symfony/serializer",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/serializer.git",
                "reference": "825b66f545da95e9bb1626d5655be6693376d52a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/serializer/zipball/825b66f545da95e9bb1626d5655be6693376d52a",
                "reference": "825b66f545da95e9bb1626d5655be6693376d52a",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8"
            },
            "conflict": {
                "phpdocumentor/type-resolver": "<0.2.1",
                "symfony/dependency-injection": "<4.4",
                "symfony/property-access": "<4.4",
                "symfony/property-info": "<4.4",
                "symfony/yaml": "<4.4"
            },
            "require-dev": {
                "doctrine/annotations": "~1.0",
                "doctrine/cache": "~1.0",
                "phpdocumentor/reflection-docblock": "^3.2|^4.0",
                "symfony/cache": "^4.4|^5.0",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/mime": "^4.4|^5.0",
                "symfony/property-access": "^4.4|^5.0",
                "symfony/property-info": "^4.4|^5.0",
                "symfony/validator": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "doctrine/annotations": "For using the annotation mapping. You will also need doctrine/cache.",
                "doctrine/cache": "For using the default cached annotation reader and metadata cache.",
                "psr/cache-implementation": "For using the metadata cache.",
                "symfony/config": "For using the XML mapping loader.",
                "symfony/mime": "For using a MIME type guesser within the DataUriNormalizer.",
                "symfony/property-access": "For using the ObjectNormalizer.",
                "symfony/property-info": "To deserialize relations.",
                "symfony/yaml": "For using the default YAML mapping loader."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Serializer\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Serializer Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/serializer/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T08:36:09+00:00"
        },
        {
            "name": "symfony/serializer-pack",
            "version": "v1.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/serializer-pack.git",
                "reference": "61173947057d5e1bf1c79e2a6ab6a8430be0602e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/serializer-pack/zipball/61173947057d5e1bf1c79e2a6ab6a8430be0602e",
                "reference": "61173947057d5e1bf1c79e2a6ab6a8430be0602e",
                "shasum": ""
            },
            "require": {
                "doctrine/annotations": "^1.0",
                "phpdocumentor/reflection-docblock": "*",
                "symfony/property-access": "*",
                "symfony/property-info": "*",
                "symfony/serializer": "*"
            },
            "type": "symfony-pack",
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A pack for the Symfony serializer",
            "support": {
                "issues": "https://github.com/symfony/serializer-pack/issues",
                "source": "https://github.com/symfony/serializer-pack/tree/v1.0.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-10-19T08:52:16+00:00"
        },
        {
            "name": "symfony/service-contracts",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/service-contracts.git",
                "reference": "d15da7ba4957ffb8f1747218be9e1a121fd298a1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/service-contracts/zipball/d15da7ba4957ffb8f1747218be9e1a121fd298a1",
                "reference": "d15da7ba4957ffb8f1747218be9e1a121fd298a1",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/container": "^1.0"
            },
            "suggest": {
                "symfony/service-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Service\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to writing services",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/service-contracts/tree/master"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-09-07T11:33:47+00:00"
        },
        {
            "name": "symfony/stopwatch",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/stopwatch.git",
                "reference": "fbc3084469450c6f6616f5436a00e180ea9ff118"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/stopwatch/zipball/fbc3084469450c6f6616f5436a00e180ea9ff118",
                "reference": "fbc3084469450c6f6616f5436a00e180ea9ff118",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/service-contracts": "^1.0|^2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Stopwatch\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Stopwatch Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/stopwatch/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-20T17:38:26+00:00"
        },
        {
            "name": "symfony/translation-contracts",
            "version": "v2.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation-contracts.git",
                "reference": "e2eaa60b558f26a4b0354e1bbb25636efaaad105"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation-contracts/zipball/e2eaa60b558f26a4b0354e1bbb25636efaaad105",
                "reference": "e2eaa60b558f26a4b0354e1bbb25636efaaad105",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "suggest": {
                "symfony/translation-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.3-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Translation\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to translation",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/translation-contracts/tree/v2.3.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-09-28T13:05:58+00:00"
        },
        {
            "name": "symfony/twig-bridge",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/twig-bridge.git",
                "reference": "293e5f04eee4da963686beab20960b45e4db68ad"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/twig-bridge/zipball/293e5f04eee4da963686beab20960b45e4db68ad",
                "reference": "293e5f04eee4da963686beab20960b45e4db68ad",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/translation-contracts": "^1.1|^2",
                "twig/twig": "^2.10|^3.0"
            },
            "conflict": {
                "symfony/console": "<4.4",
                "symfony/form": "<5.0",
                "symfony/http-foundation": "<4.4",
                "symfony/http-kernel": "<4.4",
                "symfony/translation": "<5.0",
                "symfony/workflow": "<4.4"
            },
            "require-dev": {
                "egulias/email-validator": "^2.1.10",
                "symfony/asset": "^4.4|^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/form": "^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/mime": "^4.4|^5.0",
                "symfony/polyfill-intl-icu": "~1.0",
                "symfony/routing": "^4.4|^5.0",
                "symfony/security-acl": "^2.8|^3.0",
                "symfony/security-core": "^4.4|^5.0",
                "symfony/security-csrf": "^4.4|^5.0",
                "symfony/security-http": "^4.4|^5.0",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/translation": "^5.0",
                "symfony/web-link": "^4.4|^5.0",
                "symfony/workflow": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0",
                "twig/cssinliner-extra": "^2.12",
                "twig/inky-extra": "^2.12",
                "twig/markdown-extra": "^2.12"
            },
            "suggest": {
                "symfony/asset": "For using the AssetExtension",
                "symfony/expression-language": "For using the ExpressionExtension",
                "symfony/finder": "",
                "symfony/form": "For using the FormExtension",
                "symfony/http-kernel": "For using the HttpKernelExtension",
                "symfony/routing": "For using the RoutingExtension",
                "symfony/security-core": "For using the SecurityExtension",
                "symfony/security-csrf": "For using the CsrfExtension",
                "symfony/security-http": "For using the LogoutUrlExtension",
                "symfony/stopwatch": "For using the StopwatchExtension",
                "symfony/translation": "For using the TranslationExtension",
                "symfony/var-dumper": "For using the DumpExtension",
                "symfony/web-link": "For using the WebLinkExtension",
                "symfony/yaml": "For using the YamlExtension"
            },
            "type": "symfony-bridge",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bridge\\Twig\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Twig Bridge",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/twig-bridge/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-30T17:59:45+00:00"
        },
        {
            "name": "symfony/twig-bundle",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/twig-bundle.git",
                "reference": "348863cd784b10ea7e1485dc3003c738c6cdf547"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/twig-bundle/zipball/348863cd784b10ea7e1485dc3003c738c6cdf547",
                "reference": "348863cd784b10ea7e1485dc3003c738c6cdf547",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/config": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/http-kernel": "^5.0",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/twig-bridge": "^5.0",
                "twig/twig": "^2.10|^3.0"
            },
            "conflict": {
                "symfony/dependency-injection": "<4.4",
                "symfony/framework-bundle": "<5.0",
                "symfony/translation": "<5.0"
            },
            "require-dev": {
                "doctrine/annotations": "~1.7",
                "doctrine/cache": "~1.0",
                "symfony/asset": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/form": "^4.4|^5.0",
                "symfony/framework-bundle": "^5.0",
                "symfony/routing": "^4.4|^5.0",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/translation": "^5.0",
                "symfony/web-link": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\TwigBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony TwigBundle",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/twig-bundle/tree/v5.0.9"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-20T17:38:26+00:00"
        },
        {
            "name": "symfony/twig-pack",
            "version": "v1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/twig-pack.git",
                "reference": "08a73e833e07921c464336deb7630f93e85ef930"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/twig-pack/zipball/08a73e833e07921c464336deb7630f93e85ef930",
                "reference": "08a73e833e07921c464336deb7630f93e85ef930",
                "shasum": ""
            },
            "require": {
                "symfony/twig-bundle": "*",
                "twig/extra-bundle": "^2.12|^3.0",
                "twig/twig": "^2.12|^3.0"
            },
            "type": "symfony-pack",
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A Twig pack for Symfony projects",
            "support": {
                "issues": "https://github.com/symfony/twig-pack/issues",
                "source": "https://github.com/symfony/twig-pack/tree/v1.0.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-10-19T08:46:41+00:00"
        },
        {
            "name": "symfony/var-dumper",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-dumper.git",
                "reference": "36d19dbb4b377273dddb820adcdf0cc9dcf57731"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-dumper/zipball/36d19dbb4b377273dddb820adcdf0cc9dcf57731",
                "reference": "36d19dbb4b377273dddb820adcdf0cc9dcf57731",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "^1.15"
            },
            "conflict": {
                "phpunit/phpunit": "<5.4.3",
                "symfony/console": "<4.4"
            },
            "require-dev": {
                "ext-iconv": "*",
                "symfony/console": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "twig/twig": "^2.4|^3.0"
            },
            "suggest": {
                "ext-iconv": "To convert non-UTF-8 strings to UTF-8 (or symfony/polyfill-iconv in case ext-iconv cannot be used).",
                "ext-intl": "To show region name in time zone dump",
                "symfony/console": "To use the ServerDumpCommand and/or the bin/var-dump-server script"
            },
            "bin": [
                "Resources/bin/var-dump-server"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "files": [
                    "Resources/functions/dump.php"
                ],
                "psr-4": {
                    "Symfony\\Component\\VarDumper\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony mechanism for exploring and dumping PHP variables",
            "homepage": "https://symfony.com",
            "keywords": [
                "debug",
                "dump"
            ],
            "support": {
                "source": "https://github.com/symfony/var-dumper/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-24T13:36:01+00:00"
        },
        {
            "name": "symfony/var-exporter",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-exporter.git",
                "reference": "b87e3aeedb74ee2694932d04153df9d804954cc3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-exporter/zipball/b87e3aeedb74ee2694932d04153df9d804954cc3",
                "reference": "b87e3aeedb74ee2694932d04153df9d804954cc3",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "require-dev": {
                "symfony/var-dumper": "^4.4.9|^5.0.9"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\VarExporter\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "A blend of var_export() + serialize() to turn any serializable data structure to plain PHP code",
            "homepage": "https://symfony.com",
            "keywords": [
                "clone",
                "construct",
                "export",
                "hydrate",
                "instantiate",
                "serialize"
            ],
            "support": {
                "source": "https://github.com/symfony/var-exporter/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-07T15:38:39+00:00"
        },
        {
            "name": "symfony/yaml",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/yaml.git",
                "reference": "29b60e88ff11a45b708115004fdeacab1ee3dd5d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/yaml/zipball/29b60e88ff11a45b708115004fdeacab1ee3dd5d",
                "reference": "29b60e88ff11a45b708115004fdeacab1ee3dd5d",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8"
            },
            "conflict": {
                "symfony/console": "<4.4"
            },
            "require-dev": {
                "symfony/console": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/console": "For validating YAML files using the lint command"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Yaml\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Yaml Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/yaml/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-20T17:38:26+00:00"
        },
        {
            "name": "twig/extra-bundle",
            "version": "v3.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/twigphp/twig-extra-bundle.git",
                "reference": "07c94c7dcfe7e49abd45d4083ca5544a34969714"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/twigphp/twig-extra-bundle/zipball/07c94c7dcfe7e49abd45d4083ca5544a34969714",
                "reference": "07c94c7dcfe7e49abd45d4083ca5544a34969714",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3|^8.0",
                "symfony/framework-bundle": "^4.3|^5.0",
                "symfony/twig-bundle": "^4.3|^5.0",
                "twig/twig": "^3.2"
            },
            "require-dev": {
                "symfony/phpunit-bridge": "^4.4.9|^5.0.9",
                "twig/cache-extra": "^3.0",
                "twig/cssinliner-extra": "^2.12|^3.0",
                "twig/html-extra": "^2.12|^3.0",
                "twig/inky-extra": "^2.12|^3.0",
                "twig/intl-extra": "^2.12|^3.0",
                "twig/markdown-extra": "^2.12|^3.0",
                "twig/string-extra": "^2.12|^3.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.2-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Twig\\Extra\\TwigExtraBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com",
                    "homepage": "http://fabien.potencier.org",
                    "role": "Lead Developer"
                }
            ],
            "description": "A Symfony bundle for extra Twig extensions",
            "homepage": "https://twig.symfony.com",
            "keywords": [
                "bundle",
                "extra",
                "twig"
            ],
            "support": {
                "source": "https://github.com/twigphp/twig-extra-bundle/tree/v3.2.1"
            },
            "funding": [
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/twig/twig",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-05T15:24:51+00:00"
        },
        {
            "name": "twig/twig",
            "version": "v3.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/twigphp/Twig.git",
                "reference": "f795ca686d38530045859b0350b5352f7d63447d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/twigphp/Twig/zipball/f795ca686d38530045859b0350b5352f7d63447d",
                "reference": "f795ca686d38530045859b0350b5352f7d63447d",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "^1.8",
                "symfony/polyfill-mbstring": "^1.3"
            },
            "require-dev": {
                "psr/container": "^1.0",
                "symfony/phpunit-bridge": "^4.4.9|^5.0.9"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.2-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Twig\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com",
                    "homepage": "http://fabien.potencier.org",
                    "role": "Lead Developer"
                },
                {
                    "name": "Twig Team",
                    "role": "Contributors"
                },
                {
                    "name": "Armin Ronacher",
                    "email": "armin.ronacher@active-4.com",
                    "role": "Project Founder"
                }
            ],
            "description": "Twig, the flexible, fast, and secure template language for PHP",
            "homepage": "https://twig.symfony.com",
            "keywords": [
                "templating"
            ],
            "support": {
                "issues": "https://github.com/twigphp/Twig/issues",
                "source": "https://github.com/twigphp/Twig/tree/v3.2.1"
            },
            "funding": [
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/twig/twig",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-05T15:40:36+00:00"
        },
        {
            "name": "webmozart/assert",
            "version": "1.9.1",
            "source": {
                "type": "git",
                "url": "https://github.com/webmozarts/assert.git",
                "reference": "bafc69caeb4d49c39fd0779086c03a3738cbb389"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/webmozarts/assert/zipball/bafc69caeb4d49c39fd0779086c03a3738cbb389",
                "reference": "bafc69caeb4d49c39fd0779086c03a3738cbb389",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.3 || ^7.0 || ^8.0",
                "symfony/polyfill-ctype": "^1.8"
            },
            "conflict": {
                "phpstan/phpstan": "<0.12.20",
                "vimeo/psalm": "<3.9.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.36 || ^7.5.13"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Webmozart\\Assert\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@gmail.com"
                }
            ],
            "description": "Assertions to validate method input/output with nice error messages.",
            "keywords": [
                "assert",
                "check",
                "validate"
            ],
            "support": {
                "issues": "https://github.com/webmozarts/assert/issues",
                "source": "https://github.com/webmozarts/assert/tree/1.9.1"
            },
            "time": "2020-07-08T17:02:28+00:00"
        },
        {
            "name": "zircote/swagger-php",
            "version": "3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/zircote/swagger-php.git",
                "reference": "9d172471e56433b5c7061006b9a766f262a3edfd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/zircote/swagger-php/zipball/9d172471e56433b5c7061006b9a766f262a3edfd",
                "reference": "9d172471e56433b5c7061006b9a766f262a3edfd",
                "shasum": ""
            },
            "require": {
                "doctrine/annotations": "*",
                "ext-json": "*",
                "php": ">=7.2",
                "symfony/finder": ">=2.2",
                "symfony/yaml": ">=3.3"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^2.16",
                "phpunit/phpunit": ">=8"
            },
            "bin": [
                "bin/openapi"
            ],
            "type": "library",
            "autoload": {
                "psr-4": {
                    "OpenApi\\": "src"
                },
                "files": [
                    "src/functions.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache-2.0"
            ],
            "authors": [
                {
                    "name": "Robert Allen",
                    "email": "zircote@gmail.com"
                },
                {
                    "name": "Bob Fanger",
                    "email": "bfanger@gmail.com",
                    "homepage": "https://bfanger.nl"
                },
                {
                    "name": "Martin Rademacher",
                    "email": "mano@radebatz.net",
                    "homepage": "https://radebatz.net"
                }
            ],
            "description": "swagger-php - Generate interactive documentation for your RESTful API using phpdoc annotations",
            "homepage": "https://github.com/zircote/swagger-php/",
            "keywords": [
                "api",
                "json",
                "rest",
                "service discovery"
            ],
            "support": {
                "issues": "https://github.com/zircote/swagger-php/issues",
                "source": "https://github.com/zircote/swagger-php/tree/3.1.0"
            },
            "time": "2020-09-03T20:18:43+00:00"
        }
    ],
    "packages-dev": [
        {
            "name": "monolog/monolog",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Seldaek/monolog.git",
                "reference": "1cb1cde8e8dd0f70cc0fe51354a59acad9302084"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Seldaek/monolog/zipball/1cb1cde8e8dd0f70cc0fe51354a59acad9302084",
                "reference": "1cb1cde8e8dd0f70cc0fe51354a59acad9302084",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2",
                "psr/log": "^1.0.1"
            },
            "provide": {
                "psr/log-implementation": "1.0.0"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^2.4.9 || ^3.0",
                "doctrine/couchdb": "~1.0@dev",
                "elasticsearch/elasticsearch": "^7",
                "graylog2/gelf-php": "^1.4.2",
                "mongodb/mongodb": "^1.8",
                "php-amqplib/php-amqplib": "~2.4",
                "php-console/php-console": "^3.1.3",
                "phpspec/prophecy": "^1.6.1",
                "phpstan/phpstan": "^0.12.59",
                "phpunit/phpunit": "^8.5",
                "predis/predis": "^1.1",
                "rollbar/rollbar": "^1.3",
                "ruflin/elastica": ">=0.90 <7.0.1",
                "swiftmailer/swiftmailer": "^5.3|^6.0"
            },
            "suggest": {
                "aws/aws-sdk-php": "Allow sending log messages to AWS services like DynamoDB",
                "doctrine/couchdb": "Allow sending log messages to a CouchDB server",
                "elasticsearch/elasticsearch": "Allow sending log messages to an Elasticsearch server via official client",
                "ext-amqp": "Allow sending log messages to an AMQP server (1.0+ required)",
                "ext-mbstring": "Allow to work properly with unicode symbols",
                "ext-mongodb": "Allow sending log messages to a MongoDB server (via driver)",
                "graylog2/gelf-php": "Allow sending log messages to a GrayLog2 server",
                "mongodb/mongodb": "Allow sending log messages to a MongoDB server (via library)",
                "php-amqplib/php-amqplib": "Allow sending log messages to an AMQP server using php-amqplib",
                "php-console/php-console": "Allow sending log messages to Google Chrome",
                "rollbar/rollbar": "Allow sending log messages to Rollbar",
                "ruflin/elastica": "Allow sending log messages to an Elastic Search server"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Monolog\\": "src/Monolog"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be",
                    "homepage": "https://seld.be"
                }
            ],
            "description": "Sends your logs to files, sockets, inboxes, databases and various web services",
            "homepage": "https://github.com/Seldaek/monolog",
            "keywords": [
                "log",
                "logging",
                "psr-3"
            ],
            "support": {
                "issues": "https://github.com/Seldaek/monolog/issues",
                "source": "https://github.com/Seldaek/monolog/tree/2.2.0"
            },
            "funding": [
                {
                    "url": "https://github.com/Seldaek",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/monolog/monolog",
                    "type": "tidelift"
                }
            ],
            "time": "2020-12-14T13:15:25+00:00"
        },
        {
            "name": "myclabs/deep-copy",
            "version": "1.10.2",
            "source": {
                "type": "git",
                "url": "https://github.com/myclabs/DeepCopy.git",
                "reference": "776f831124e9c62e1a2c601ecc52e776d8bb7220"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/myclabs/DeepCopy/zipball/776f831124e9c62e1a2c601ecc52e776d8bb7220",
                "reference": "776f831124e9c62e1a2c601ecc52e776d8bb7220",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
            },
            "replace": {
                "myclabs/deep-copy": "self.version"
            },
            "require-dev": {
                "doctrine/collections": "^1.0",
                "doctrine/common": "^2.6",
                "phpunit/phpunit": "^7.1"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "DeepCopy\\": "src/DeepCopy/"
                },
                "files": [
                    "src/DeepCopy/deep_copy.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Create deep copies (clones) of your objects",
            "keywords": [
                "clone",
                "copy",
                "duplicate",
                "object",
                "object graph"
            ],
            "support": {
                "issues": "https://github.com/myclabs/DeepCopy/issues",
                "source": "https://github.com/myclabs/DeepCopy/tree/1.10.2"
            },
            "funding": [
                {
                    "url": "https://tidelift.com/funding/github/packagist/myclabs/deep-copy",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-13T09:40:50+00:00"
        },
        {
            "name": "nikic/php-parser",
            "version": "v4.10.4",
            "source": {
                "type": "git",
                "url": "https://github.com/nikic/PHP-Parser.git",
                "reference": "c6d052fc58cb876152f89f532b95a8d7907e7f0e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nikic/PHP-Parser/zipball/c6d052fc58cb876152f89f532b95a8d7907e7f0e",
                "reference": "c6d052fc58cb876152f89f532b95a8d7907e7f0e",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": ">=7.0"
            },
            "require-dev": {
                "ircmaxell/php-yacc": "^0.0.7",
                "phpunit/phpunit": "^6.5 || ^7.0 || ^8.0 || ^9.0"
            },
            "bin": [
                "bin/php-parse"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.9-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PhpParser\\": "lib/PhpParser"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Nikita Popov"
                }
            ],
            "description": "A PHP parser written in PHP",
            "keywords": [
                "parser",
                "php"
            ],
            "support": {
                "issues": "https://github.com/nikic/PHP-Parser/issues",
                "source": "https://github.com/nikic/PHP-Parser/tree/v4.10.4"
            },
            "time": "2020-12-20T10:01:03+00:00"
        },
        {
            "name": "phar-io/manifest",
            "version": "1.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/manifest.git",
                "reference": "7761fcacf03b4d4f16e7ccb606d4879ca431fcf4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/manifest/zipball/7761fcacf03b4d4f16e7ccb606d4879ca431fcf4",
                "reference": "7761fcacf03b4d4f16e7ccb606d4879ca431fcf4",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-phar": "*",
                "phar-io/version": "^2.0",
                "php": "^5.6 || ^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Heuer",
                    "email": "sebastian@phpeople.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "Developer"
                }
            ],
            "description": "Component for reading phar.io manifest information from a PHP Archive (PHAR)",
            "support": {
                "issues": "https://github.com/phar-io/manifest/issues",
                "source": "https://github.com/phar-io/manifest/tree/master"
            },
            "time": "2018-07-08T19:23:20+00:00"
        },
        {
            "name": "phar-io/version",
            "version": "2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/version.git",
                "reference": "45a2ec53a73c70ce41d55cedef9063630abaf1b6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/version/zipball/45a2ec53a73c70ce41d55cedef9063630abaf1b6",
                "reference": "45a2ec53a73c70ce41d55cedef9063630abaf1b6",
                "shasum": ""
            },
            "require": {
                "php": "^5.6 || ^7.0"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Heuer",
                    "email": "sebastian@phpeople.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "Developer"
                }
            ],
            "description": "Library for handling version information and constraints",
            "support": {
                "issues": "https://github.com/phar-io/version/issues",
                "source": "https://github.com/phar-io/version/tree/master"
            },
            "time": "2018-07-08T19:19:57+00:00"
        },
        {
            "name": "phpspec/prophecy",
            "version": "1.12.2",
            "source": {
                "type": "git",
                "url": "https://github.com/phpspec/prophecy.git",
                "reference": "245710e971a030f42e08f4912863805570f23d39"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpspec/prophecy/zipball/245710e971a030f42e08f4912863805570f23d39",
                "reference": "245710e971a030f42e08f4912863805570f23d39",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.2",
                "php": "^7.2 || ~8.0, <8.1",
                "phpdocumentor/reflection-docblock": "^5.2",
                "sebastian/comparator": "^3.0 || ^4.0",
                "sebastian/recursion-context": "^3.0 || ^4.0"
            },
            "require-dev": {
                "phpspec/phpspec": "^6.0",
                "phpunit/phpunit": "^8.0 || ^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.11.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Prophecy\\": "src/Prophecy"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Konstantin Kudryashov",
                    "email": "ever.zet@gmail.com",
                    "homepage": "http://everzet.com"
                },
                {
                    "name": "Marcello Duarte",
                    "email": "marcello.duarte@gmail.com"
                }
            ],
            "description": "Highly opinionated mocking framework for PHP 5.3+",
            "homepage": "https://github.com/phpspec/prophecy",
            "keywords": [
                "Double",
                "Dummy",
                "fake",
                "mock",
                "spy",
                "stub"
            ],
            "support": {
                "issues": "https://github.com/phpspec/prophecy/issues",
                "source": "https://github.com/phpspec/prophecy/tree/1.12.2"
            },
            "time": "2020-12-19T10:15:11+00:00"
        },
        {
            "name": "phpstan/phpstan",
            "version": "0.12.72",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan.git",
                "reference": "ae32fb1c5e97979f424c3ccec4ee435a35754769"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan/zipball/ae32fb1c5e97979f424c3ccec4ee435a35754769",
                "reference": "ae32fb1c5e97979f424c3ccec4ee435a35754769",
                "shasum": ""
            },
            "require": {
                "php": "^7.1|^8.0"
            },
            "conflict": {
                "phpstan/phpstan-shim": "*"
            },
            "bin": [
                "phpstan",
                "phpstan.phar"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.12-dev"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHPStan - PHP Static Analysis Tool",
            "support": {
                "issues": "https://github.com/phpstan/phpstan/issues",
                "source": "https://github.com/phpstan/phpstan/tree/0.12.72"
            },
            "funding": [
                {
                    "url": "https://github.com/ondrejmirtes",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/phpstan",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/phpstan/phpstan",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-06T18:34:03+00:00"
        },
        {
            "name": "phpstan/phpstan-doctrine",
            "version": "0.12.30",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan-doctrine.git",
                "reference": "c4b910638ef416ad336aca596b4551a2db10b5f7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan-doctrine/zipball/c4b910638ef416ad336aca596b4551a2db10b5f7",
                "reference": "c4b910638ef416ad336aca596b4551a2db10b5f7",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0",
                "phpstan/phpstan": "^0.12.56"
            },
            "conflict": {
                "doctrine/collections": "<1.0",
                "doctrine/common": "<2.7",
                "doctrine/mongodb-odm": "<1.2",
                "doctrine/orm": "<2.5",
                "doctrine/persistence": "<1.3"
            },
            "require-dev": {
                "doctrine/annotations": "^1.11.0",
                "doctrine/collections": "^1.0",
                "doctrine/common": "^2.7 || ^3.0",
                "doctrine/dbal": "^2.11.0",
                "doctrine/mongodb-odm": "^1.3 || ^2.1",
                "doctrine/orm": "^2.5",
                "doctrine/persistence": "^1.1 || ^2.0",
                "phing/phing": "^2.16.3",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/phpstan-phpunit": "^0.12.16",
                "phpstan/phpstan-strict-rules": "^0.12.5",
                "phpunit/phpunit": "^7.5.20",
                "ramsey/uuid-doctrine": "^1.5.0"
            },
            "type": "phpstan-extension",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.12-dev"
                },
                "phpstan": {
                    "includes": [
                        "extension.neon",
                        "rules.neon"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Doctrine extensions for PHPStan",
            "support": {
                "issues": "https://github.com/phpstan/phpstan-doctrine/issues",
                "source": "https://github.com/phpstan/phpstan-doctrine/tree/0.12.30"
            },
            "time": "2021-01-18T13:00:10+00:00"
        },
        {
            "name": "phpstan/phpstan-phpunit",
            "version": "0.12.17",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan-phpunit.git",
                "reference": "432575b41cf2d4f44e460234acaf56119ed97d36"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan-phpunit/zipball/432575b41cf2d4f44e460234acaf56119ed97d36",
                "reference": "432575b41cf2d4f44e460234acaf56119ed97d36",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0",
                "phpstan/phpstan": "^0.12.60"
            },
            "conflict": {
                "phpunit/phpunit": "<7.0"
            },
            "require-dev": {
                "phing/phing": "^2.16.3",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/phpstan-strict-rules": "^0.12.6",
                "phpunit/phpunit": "^7.5.20"
            },
            "type": "phpstan-extension",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.12-dev"
                },
                "phpstan": {
                    "includes": [
                        "extension.neon",
                        "rules.neon"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHPUnit extensions and rules for PHPStan",
            "support": {
                "issues": "https://github.com/phpstan/phpstan-phpunit/issues",
                "source": "https://github.com/phpstan/phpstan-phpunit/tree/0.12.17"
            },
            "time": "2020-12-13T12:12:51+00:00"
        },
        {
            "name": "phpstan/phpstan-strict-rules",
            "version": "0.12.9",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan-strict-rules.git",
                "reference": "0705fefc7c9168529fd130e341428f5f10f4f01d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan-strict-rules/zipball/0705fefc7c9168529fd130e341428f5f10f4f01d",
                "reference": "0705fefc7c9168529fd130e341428f5f10f4f01d",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0",
                "phpstan/phpstan": "^0.12.66"
            },
            "require-dev": {
                "phing/phing": "^2.16.3",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/phpstan-phpunit": "^0.12.16",
                "phpunit/phpunit": "^7.5.20"
            },
            "type": "phpstan-extension",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.12-dev"
                },
                "phpstan": {
                    "includes": [
                        "rules.neon"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Extra strict and opinionated rules for PHPStan",
            "support": {
                "issues": "https://github.com/phpstan/phpstan-strict-rules/issues",
                "source": "https://github.com/phpstan/phpstan-strict-rules/tree/0.12.9"
            },
            "time": "2021-01-13T08:50:28+00:00"
        },
        {
            "name": "phpstan/phpstan-symfony",
            "version": "0.12.16",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan-symfony.git",
                "reference": "c50afb8f4e27d4ab3b47ac370838aefac3c15e9e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan-symfony/zipball/c50afb8f4e27d4ab3b47ac370838aefac3c15e9e",
                "reference": "c50afb8f4e27d4ab3b47ac370838aefac3c15e9e",
                "shasum": ""
            },
            "require": {
                "ext-simplexml": "*",
                "php": "^7.1 || ^8.0",
                "phpstan/phpstan": "^0.12.51"
            },
            "conflict": {
                "symfony/framework-bundle": "<3.0"
            },
            "require-dev": {
                "phing/phing": "^2.16.3",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/phpstan-phpunit": "^0.12.16",
                "phpstan/phpstan-strict-rules": "^0.12.5",
                "phpunit/phpunit": "^7.5.20",
                "symfony/console": "^4.0",
                "symfony/framework-bundle": "^4.0",
                "symfony/http-foundation": "^4.0",
                "symfony/messenger": "^4.2",
                "symfony/serializer": "^4.0"
            },
            "type": "phpstan-extension",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.12-dev"
                },
                "phpstan": {
                    "includes": [
                        "extension.neon",
                        "rules.neon"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Lukáš Unger",
                    "email": "looky.msc@gmail.com",
                    "homepage": "https://lookyman.net"
                }
            ],
            "description": "Symfony Framework extensions and rules for PHPStan",
            "support": {
                "issues": "https://github.com/phpstan/phpstan-symfony/issues",
                "source": "https://github.com/phpstan/phpstan-symfony/tree/0.12.16"
            },
            "time": "2021-01-25T12:30:55+00:00"
        },
        {
            "name": "phpstan/phpstan-webmozart-assert",
            "version": "0.12.12",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan-webmozart-assert.git",
                "reference": "1657403194a43f83b5355bd400aa7fc63f0e6857"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan-webmozart-assert/zipball/1657403194a43f83b5355bd400aa7fc63f0e6857",
                "reference": "1657403194a43f83b5355bd400aa7fc63f0e6857",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0",
                "phpstan/phpstan": "^0.12.49"
            },
            "require-dev": {
                "phing/phing": "^2.16.3",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/phpstan-phpunit": "^0.12.6",
                "phpstan/phpstan-strict-rules": "^0.12.1",
                "phpunit/phpunit": "^7.5.20",
                "webmozart/assert": "^1.9.1"
            },
            "type": "phpstan-extension",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.12-dev"
                },
                "phpstan": {
                    "includes": [
                        "extension.neon"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHPStan webmozart/assert extension",
            "support": {
                "issues": "https://github.com/phpstan/phpstan-webmozart-assert/issues",
                "source": "https://github.com/phpstan/phpstan-webmozart-assert/tree/0.12.12"
            },
            "time": "2021-01-31T12:24:28+00:00"
        },
        {
            "name": "phpunit/php-code-coverage",
            "version": "8.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-code-coverage.git",
                "reference": "ca6647ffddd2add025ab3f21644a441d7c146cdc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-code-coverage/zipball/ca6647ffddd2add025ab3f21644a441d7c146cdc",
                "reference": "ca6647ffddd2add025ab3f21644a441d7c146cdc",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-xmlwriter": "*",
                "php": "^7.3",
                "phpunit/php-file-iterator": "^3.0",
                "phpunit/php-text-template": "^2.0",
                "phpunit/php-token-stream": "^4.0",
                "sebastian/code-unit-reverse-lookup": "^2.0",
                "sebastian/environment": "^5.0",
                "sebastian/version": "^3.0",
                "theseer/tokenizer": "^1.1.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.0"
            },
            "suggest": {
                "ext-pcov": "*",
                "ext-xdebug": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "8.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library that provides collection, processing, and rendering functionality for PHP code coverage information.",
            "homepage": "https://github.com/sebastianbergmann/php-code-coverage",
            "keywords": [
                "coverage",
                "testing",
                "xunit"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-code-coverage/issues",
                "source": "https://github.com/sebastianbergmann/php-code-coverage/tree/8.0.2"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-05-23T08:02:54+00:00"
        },
        {
            "name": "phpunit/php-file-iterator",
            "version": "3.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-file-iterator.git",
                "reference": "aa4be8575f26070b100fccb67faabb28f21f66f8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-file-iterator/zipball/aa4be8575f26070b100fccb67faabb28f21f66f8",
                "reference": "aa4be8575f26070b100fccb67faabb28f21f66f8",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "FilterIterator implementation that filters files based on a list of suffixes.",
            "homepage": "https://github.com/sebastianbergmann/php-file-iterator/",
            "keywords": [
                "filesystem",
                "iterator"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-file-iterator/issues",
                "source": "https://github.com/sebastianbergmann/php-file-iterator/tree/3.0.5"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:57:25+00:00"
        },
        {
            "name": "phpunit/php-invoker",
            "version": "3.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-invoker.git",
                "reference": "5a10147d0aaf65b58940a0b72f71c9ac0423cc67"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-invoker/zipball/5a10147d0aaf65b58940a0b72f71c9ac0423cc67",
                "reference": "5a10147d0aaf65b58940a0b72f71c9ac0423cc67",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "ext-pcntl": "*",
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-pcntl": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Invoke callables with a timeout",
            "homepage": "https://github.com/sebastianbergmann/php-invoker/",
            "keywords": [
                "process"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-invoker/issues",
                "source": "https://github.com/sebastianbergmann/php-invoker/tree/3.1.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:58:55+00:00"
        },
        {
            "name": "phpunit/php-text-template",
            "version": "2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-text-template.git",
                "reference": "5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-text-template/zipball/5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28",
                "reference": "5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Simple template engine.",
            "homepage": "https://github.com/sebastianbergmann/php-text-template/",
            "keywords": [
                "template"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-text-template/issues",
                "source": "https://github.com/sebastianbergmann/php-text-template/tree/2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T05:33:50+00:00"
        },
        {
            "name": "phpunit/php-timer",
            "version": "3.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-timer.git",
                "reference": "dc9368fae6ef2ffa57eba80a7410bcef81df6258"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-timer/zipball/dc9368fae6ef2ffa57eba80a7410bcef81df6258",
                "reference": "dc9368fae6ef2ffa57eba80a7410bcef81df6258",
                "shasum": ""
            },
            "require": {
                "php": "^7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Utility class for timing",
            "homepage": "https://github.com/sebastianbergmann/php-timer/",
            "keywords": [
                "timer"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-timer/issues",
                "source": "https://github.com/sebastianbergmann/php-timer/tree/master"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-04-20T06:00:37+00:00"
        },
        {
            "name": "phpunit/php-token-stream",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-token-stream.git",
                "reference": "a853a0e183b9db7eed023d7933a858fa1c8d25a3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-token-stream/zipball/a853a0e183b9db7eed023d7933a858fa1c8d25a3",
                "reference": "a853a0e183b9db7eed023d7933a858fa1c8d25a3",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": "^7.3 || ^8.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Wrapper around PHP's tokenizer extension.",
            "homepage": "https://github.com/sebastianbergmann/php-token-stream/",
            "keywords": [
                "tokenizer"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-token-stream/issues",
                "source": "https://github.com/sebastianbergmann/php-token-stream/tree/master"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "abandoned": true,
            "time": "2020-08-04T08:28:15+00:00"
        },
        {
            "name": "phpunit/phpunit",
            "version": "9.1.5",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit.git",
                "reference": "1b570cd7edbe136055bf5f651857dc8af6b829d2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit/zipball/1b570cd7edbe136055bf5f651857dc8af6b829d2",
                "reference": "1b570cd7edbe136055bf5f651857dc8af6b829d2",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.2.0",
                "ext-dom": "*",
                "ext-json": "*",
                "ext-libxml": "*",
                "ext-mbstring": "*",
                "ext-xml": "*",
                "ext-xmlwriter": "*",
                "myclabs/deep-copy": "^1.9.1",
                "phar-io/manifest": "^1.0.3",
                "phar-io/version": "^2.0.1",
                "php": "^7.3",
                "phpspec/prophecy": "^1.8.1",
                "phpunit/php-code-coverage": "^8.0.1",
                "phpunit/php-file-iterator": "^3.0",
                "phpunit/php-invoker": "^3.0",
                "phpunit/php-text-template": "^2.0",
                "phpunit/php-timer": "^3.1.4",
                "sebastian/code-unit": "^1.0.2",
                "sebastian/comparator": "^4.0",
                "sebastian/diff": "^4.0",
                "sebastian/environment": "^5.0.1",
                "sebastian/exporter": "^4.0",
                "sebastian/global-state": "^4.0",
                "sebastian/object-enumerator": "^4.0",
                "sebastian/resource-operations": "^3.0",
                "sebastian/type": "^2.0",
                "sebastian/version": "^3.0"
            },
            "require-dev": {
                "ext-pdo": "*",
                "phpspec/prophecy-phpunit": "^2.0"
            },
            "suggest": {
                "ext-soap": "*",
                "ext-xdebug": "*"
            },
            "bin": [
                "phpunit"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "9.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ],
                "files": [
                    "src/Framework/Assert/Functions.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "The PHP Unit Testing framework.",
            "homepage": "https://phpunit.de/",
            "keywords": [
                "phpunit",
                "testing",
                "xunit"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/phpunit/issues",
                "source": "https://github.com/sebastianbergmann/phpunit/tree/9.1.5"
            },
            "funding": [
                {
                    "url": "https://phpunit.de/donate.html",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-05-22T13:54:05+00:00"
        },
        {
            "name": "sebastian/code-unit",
            "version": "1.0.8",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit.git",
                "reference": "1fc9f64c0927627ef78ba436c9b17d967e68e120"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit/zipball/1fc9f64c0927627ef78ba436c9b17d967e68e120",
                "reference": "1fc9f64c0927627ef78ba436c9b17d967e68e120",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Collection of value objects that represent the PHP code units",
            "homepage": "https://github.com/sebastianbergmann/code-unit",
            "support": {
                "issues": "https://github.com/sebastianbergmann/code-unit/issues",
                "source": "https://github.com/sebastianbergmann/code-unit/tree/1.0.8"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:08:54+00:00"
        },
        {
            "name": "sebastian/code-unit-reverse-lookup",
            "version": "2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit-reverse-lookup.git",
                "reference": "ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit-reverse-lookup/zipball/ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5",
                "reference": "ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Looks up which function or method a line of code belongs to",
            "homepage": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/issues",
                "source": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/tree/2.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:30:19+00:00"
        },
        {
            "name": "sebastian/comparator",
            "version": "4.0.6",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/comparator.git",
                "reference": "55f4261989e546dc112258c7a75935a81a7ce382"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/comparator/zipball/55f4261989e546dc112258c7a75935a81a7ce382",
                "reference": "55f4261989e546dc112258c7a75935a81a7ce382",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/diff": "^4.0",
                "sebastian/exporter": "^4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Volker Dusch",
                    "email": "github@wallbash.com"
                },
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@2bepublished.at"
                }
            ],
            "description": "Provides the functionality to compare PHP values for equality",
            "homepage": "https://github.com/sebastianbergmann/comparator",
            "keywords": [
                "comparator",
                "compare",
                "equality"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/comparator/issues",
                "source": "https://github.com/sebastianbergmann/comparator/tree/4.0.6"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T15:49:45+00:00"
        },
        {
            "name": "sebastian/diff",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/diff.git",
                "reference": "3461e3fccc7cfdfc2720be910d3bd73c69be590d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/diff/zipball/3461e3fccc7cfdfc2720be910d3bd73c69be590d",
                "reference": "3461e3fccc7cfdfc2720be910d3bd73c69be590d",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3",
                "symfony/process": "^4.2 || ^5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Kore Nordmann",
                    "email": "mail@kore-nordmann.de"
                }
            ],
            "description": "Diff implementation",
            "homepage": "https://github.com/sebastianbergmann/diff",
            "keywords": [
                "diff",
                "udiff",
                "unidiff",
                "unified diff"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/diff/issues",
                "source": "https://github.com/sebastianbergmann/diff/tree/4.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:10:38+00:00"
        },
        {
            "name": "sebastian/environment",
            "version": "5.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/environment.git",
                "reference": "388b6ced16caa751030f6a69e588299fa09200ac"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/environment/zipball/388b6ced16caa751030f6a69e588299fa09200ac",
                "reference": "388b6ced16caa751030f6a69e588299fa09200ac",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-posix": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides functionality to handle HHVM/PHP environments",
            "homepage": "http://www.github.com/sebastianbergmann/environment",
            "keywords": [
                "Xdebug",
                "environment",
                "hhvm"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/environment/issues",
                "source": "https://github.com/sebastianbergmann/environment/tree/5.1.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:52:38+00:00"
        },
        {
            "name": "sebastian/exporter",
            "version": "4.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/exporter.git",
                "reference": "d89cc98761b8cb5a1a235a6b703ae50d34080e65"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/exporter/zipball/d89cc98761b8cb5a1a235a6b703ae50d34080e65",
                "reference": "d89cc98761b8cb5a1a235a6b703ae50d34080e65",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "ext-mbstring": "*",
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Volker Dusch",
                    "email": "github@wallbash.com"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                },
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@gmail.com"
                }
            ],
            "description": "Provides the functionality to export PHP variables for visualization",
            "homepage": "http://www.github.com/sebastianbergmann/exporter",
            "keywords": [
                "export",
                "exporter"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/exporter/issues",
                "source": "https://github.com/sebastianbergmann/exporter/tree/4.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:24:23+00:00"
        },
        {
            "name": "sebastian/finder-facade",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/finder-facade.git",
                "reference": "9d3e74b845a2ce50e19b25b5f0c2718e153bee6c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/finder-facade/zipball/9d3e74b845a2ce50e19b25b5f0c2718e153bee6c",
                "reference": "9d3e74b845a2ce50e19b25b5f0c2718e153bee6c",
                "shasum": ""
            },
            "require": {
                "ext-ctype": "*",
                "php": "^7.3",
                "symfony/finder": "^4.1|^5.0",
                "theseer/fdomdocument": "^1.6"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "FinderFacade is a convenience wrapper for Symfony's Finder component.",
            "homepage": "https://github.com/sebastianbergmann/finder-facade",
            "support": {
                "issues": "https://github.com/sebastianbergmann/finder-facade/issues",
                "source": "https://github.com/sebastianbergmann/finder-facade/tree/2.0.0"
            },
            "abandoned": true,
            "time": "2020-02-08T06:07:58+00:00"
        },
        {
            "name": "sebastian/global-state",
            "version": "4.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/global-state.git",
                "reference": "bdb1e7c79e592b8c82cb1699be3c8743119b8a72"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/global-state/zipball/bdb1e7c79e592b8c82cb1699be3c8743119b8a72",
                "reference": "bdb1e7c79e592b8c82cb1699be3c8743119b8a72",
                "shasum": ""
            },
            "require": {
                "php": "^7.3",
                "sebastian/object-reflector": "^2.0",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "ext-dom": "*",
                "phpunit/phpunit": "^9.0"
            },
            "suggest": {
                "ext-uopz": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Snapshotting of global state",
            "homepage": "http://www.github.com/sebastianbergmann/global-state",
            "keywords": [
                "global state"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/global-state/issues",
                "source": "https://github.com/sebastianbergmann/global-state/tree/master"
            },
            "time": "2020-02-07T06:11:37+00:00"
        },
        {
            "name": "sebastian/object-enumerator",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-enumerator.git",
                "reference": "5c9eeac41b290a3712d88851518825ad78f45c71"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-enumerator/zipball/5c9eeac41b290a3712d88851518825ad78f45c71",
                "reference": "5c9eeac41b290a3712d88851518825ad78f45c71",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/object-reflector": "^2.0",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Traverses array structures and object graphs to enumerate all referenced objects",
            "homepage": "https://github.com/sebastianbergmann/object-enumerator/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/object-enumerator/issues",
                "source": "https://github.com/sebastianbergmann/object-enumerator/tree/4.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:12:34+00:00"
        },
        {
            "name": "sebastian/object-reflector",
            "version": "2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-reflector.git",
                "reference": "b4f479ebdbf63ac605d183ece17d8d7fe49c15c7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-reflector/zipball/b4f479ebdbf63ac605d183ece17d8d7fe49c15c7",
                "reference": "b4f479ebdbf63ac605d183ece17d8d7fe49c15c7",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Allows reflection of object attributes, including inherited and non-public ones",
            "homepage": "https://github.com/sebastianbergmann/object-reflector/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/object-reflector/issues",
                "source": "https://github.com/sebastianbergmann/object-reflector/tree/2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:14:26+00:00"
        },
        {
            "name": "sebastian/phpcpd",
            "version": "5.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpcpd.git",
                "reference": "8724382966b1861df4e12db915eaed2165e10bf3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpcpd/zipball/8724382966b1861df4e12db915eaed2165e10bf3",
                "reference": "8724382966b1861df4e12db915eaed2165e10bf3",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "php": "^7.3",
                "phpunit/php-timer": "^3.0",
                "sebastian/finder-facade": "^2.0",
                "sebastian/version": "^3.0",
                "symfony/console": "^4.0|^5.0"
            },
            "bin": [
                "phpcpd"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Copy/Paste Detector (CPD) for PHP code.",
            "homepage": "https://github.com/sebastianbergmann/phpcpd",
            "support": {
                "issues": "https://github.com/sebastianbergmann/phpcpd/issues",
                "source": "https://github.com/sebastianbergmann/phpcpd/tree/5.0.2"
            },
            "time": "2020-02-22T06:03:17+00:00"
        },
        {
            "name": "sebastian/recursion-context",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/recursion-context.git",
                "reference": "cd9d8cf3c5804de4341c283ed787f099f5506172"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/recursion-context/zipball/cd9d8cf3c5804de4341c283ed787f099f5506172",
                "reference": "cd9d8cf3c5804de4341c283ed787f099f5506172",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                }
            ],
            "description": "Provides functionality to recursively process PHP variables",
            "homepage": "http://www.github.com/sebastianbergmann/recursion-context",
            "support": {
                "issues": "https://github.com/sebastianbergmann/recursion-context/issues",
                "source": "https://github.com/sebastianbergmann/recursion-context/tree/4.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:17:30+00:00"
        },
        {
            "name": "sebastian/resource-operations",
            "version": "3.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/resource-operations.git",
                "reference": "0f4443cb3a1d92ce809899753bc0d5d5a8dd19a8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/resource-operations/zipball/0f4443cb3a1d92ce809899753bc0d5d5a8dd19a8",
                "reference": "0f4443cb3a1d92ce809899753bc0d5d5a8dd19a8",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides a list of PHP built-in functions that operate on resources",
            "homepage": "https://www.github.com/sebastianbergmann/resource-operations",
            "support": {
                "issues": "https://github.com/sebastianbergmann/resource-operations/issues",
                "source": "https://github.com/sebastianbergmann/resource-operations/tree/3.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T06:45:17+00:00"
        },
        {
            "name": "sebastian/type",
            "version": "2.3.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/type.git",
                "reference": "81cd61ab7bbf2de744aba0ea61fae32f721df3d2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/type/zipball/81cd61ab7bbf2de744aba0ea61fae32f721df3d2",
                "reference": "81cd61ab7bbf2de744aba0ea61fae32f721df3d2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.3-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Collection of value objects that represent the types of the PHP type system",
            "homepage": "https://github.com/sebastianbergmann/type",
            "support": {
                "issues": "https://github.com/sebastianbergmann/type/issues",
                "source": "https://github.com/sebastianbergmann/type/tree/2.3.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:18:59+00:00"
        },
        {
            "name": "sebastian/version",
            "version": "3.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/version.git",
                "reference": "c6c1022351a901512170118436c764e473f6de8c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/version/zipball/c6c1022351a901512170118436c764e473f6de8c",
                "reference": "c6c1022351a901512170118436c764e473f6de8c",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library that helps with managing the version number of Git-hosted PHP projects",
            "homepage": "https://github.com/sebastianbergmann/version",
            "support": {
                "issues": "https://github.com/sebastianbergmann/version/issues",
                "source": "https://github.com/sebastianbergmann/version/tree/3.0.2"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T06:39:44+00:00"
        },
        {
            "name": "sensiolabs-de/deptrac-shim",
            "version": "0.7.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sensiolabs-de/deptrac-shim.git",
                "reference": "868702d0626996bd41953ac7f28a8fcbcc4165ec"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sensiolabs-de/deptrac-shim/zipball/868702d0626996bd41953ac7f28a8fcbcc4165ec",
                "reference": "868702d0626996bd41953ac7f28a8fcbcc4165ec",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "ext-tokenizer": "*",
                "ext-zlib": "*",
                "php": "^7.2"
            },
            "replace": {
                "sensiolabs-de/astrunner": "^1.0",
                "sensiolabs-de/deptrac": "self.version"
            },
            "suggest": {
                "ext-dom": "For using the JUnit output formatter"
            },
            "bin": [
                "deptrac"
            ],
            "type": "library",
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Simon Mönch",
                    "email": "simon.moench@sensiolabs.de",
                    "role": "maintainer"
                }
            ],
            "description": "deptrac phar distribution",
            "support": {
                "issues": "https://github.com/sensiolabs-de/deptrac-shim/issues",
                "source": "https://github.com/sensiolabs-de/deptrac-shim/tree/master"
            },
            "abandoned": "qossmic/deptrac-shim",
            "time": "2020-05-04T10:24:43+00:00"
        },
        {
            "name": "symfony/browser-kit",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/browser-kit.git",
                "reference": "c46b676a993cc437bafe6fe0f30f074857cde2a6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/browser-kit/zipball/c46b676a993cc437bafe6fe0f30f074857cde2a6",
                "reference": "c46b676a993cc437bafe6fe0f30f074857cde2a6",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/dom-crawler": "^4.4|^5.0"
            },
            "require-dev": {
                "symfony/css-selector": "^4.4|^5.0",
                "symfony/http-client": "^4.4|^5.0",
                "symfony/mime": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/process": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\BrowserKit\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony BrowserKit Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/browser-kit/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-12T09:22:24+00:00"
        },
        {
            "name": "symfony/css-selector",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/css-selector.git",
                "reference": "79c224cdbfae58d54b257a8c684ad445042c90f2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/css-selector/zipball/79c224cdbfae58d54b257a8c684ad445042c90f2",
                "reference": "79c224cdbfae58d54b257a8c684ad445042c90f2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\CssSelector\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Jean-François Simon",
                    "email": "jeanfrancois.simon@sensiolabs.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony CssSelector Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/css-selector/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-20T17:38:26+00:00"
        },
        {
            "name": "symfony/debug-bundle",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/debug-bundle.git",
                "reference": "4bae28a913fa32ec123a37b3178b7b7d3a4ac323"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/debug-bundle/zipball/4bae28a913fa32ec123a37b3178b7b7d3a4ac323",
                "reference": "4bae28a913fa32ec123a37b3178b7b7d3a4ac323",
                "shasum": ""
            },
            "require": {
                "ext-xml": "*",
                "php": ">=7.2.5",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/twig-bridge": "^4.4|^5.0",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "conflict": {
                "symfony/config": "<4.4",
                "symfony/dependency-injection": "<4.4"
            },
            "require-dev": {
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/web-profiler-bundle": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/config": "For service container configuration",
                "symfony/dependency-injection": "For using as a service from the container"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\DebugBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony DebugBundle",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/debug-bundle/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-20T17:38:26+00:00"
        },
        {
            "name": "symfony/debug-pack",
            "version": "v1.0.9",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/debug-pack.git",
                "reference": "cfd5093378e9cafe500f05c777a22fe8a64a9342"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/debug-pack/zipball/cfd5093378e9cafe500f05c777a22fe8a64a9342",
                "reference": "cfd5093378e9cafe500f05c777a22fe8a64a9342",
                "shasum": ""
            },
            "require": {
                "symfony/debug-bundle": "*",
                "symfony/monolog-bundle": "^3.0",
                "symfony/profiler-pack": "*",
                "symfony/var-dumper": "*"
            },
            "type": "symfony-pack",
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A debug pack for Symfony projects",
            "support": {
                "issues": "https://github.com/symfony/debug-pack/issues",
                "source": "https://github.com/symfony/debug-pack/tree/v1.0.9"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-10-19T08:51:51+00:00"
        },
        {
            "name": "symfony/deprecation-contracts",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/deprecation-contracts.git",
                "reference": "5fa56b4074d1ae755beb55617ddafe6f5d78f665"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/deprecation-contracts/zipball/5fa56b4074d1ae755beb55617ddafe6f5d78f665",
                "reference": "5fa56b4074d1ae755beb55617ddafe6f5d78f665",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "files": [
                    "function.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "A generic function and convention to trigger deprecation notices",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/deprecation-contracts/tree/master"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-09-07T11:33:47+00:00"
        },
        {
            "name": "symfony/dom-crawler",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dom-crawler.git",
                "reference": "bbc756c0895d08a1e69a59d8541a647b47f5a732"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dom-crawler/zipball/bbc756c0895d08a1e69a59d8541a647b47f5a732",
                "reference": "bbc756c0895d08a1e69a59d8541a647b47f5a732",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "conflict": {
                "masterminds/html5": "<2.6"
            },
            "require-dev": {
                "masterminds/html5": "^2.6",
                "symfony/css-selector": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/css-selector": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\DomCrawler\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony DomCrawler Component",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/dom-crawler/tree/5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T08:36:09+00:00"
        },
        {
            "name": "symfony/maker-bundle",
            "version": "v1.29.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/maker-bundle.git",
                "reference": "9a9e3f4253ca0d923ad49b327db6f89a8f74fe4c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/maker-bundle/zipball/9a9e3f4253ca0d923ad49b327db6f89a8f74fe4c",
                "reference": "9a9e3f4253ca0d923ad49b327db6f89a8f74fe4c",
                "shasum": ""
            },
            "require": {
                "doctrine/inflector": "^1.2|^2.0",
                "nikic/php-parser": "^4.0",
                "php": ">=7.1.3",
                "symfony/config": "^3.4|^4.0|^5.0",
                "symfony/console": "^3.4|^4.0|^5.0",
                "symfony/dependency-injection": "^3.4|^4.0|^5.0",
                "symfony/deprecation-contracts": "^2.2",
                "symfony/filesystem": "^3.4|^4.0|^5.0",
                "symfony/finder": "^3.4|^4.0|^5.0",
                "symfony/framework-bundle": "^3.4|^4.0|^5.0",
                "symfony/http-kernel": "^3.4|^4.0|^5.0"
            },
            "require-dev": {
                "composer/semver": "^3.0@dev",
                "doctrine/doctrine-bundle": "^1.8|^2.0",
                "doctrine/orm": "^2.3",
                "friendsofphp/php-cs-fixer": "^2.8",
                "friendsoftwig/twigcs": "^3.1.2",
                "symfony/http-client": "^4.3|^5.0",
                "symfony/phpunit-bridge": "^4.3|^5.0",
                "symfony/process": "^3.4|^4.0|^5.0",
                "symfony/security-core": "^3.4|^4.0|^5.0",
                "symfony/yaml": "^3.4|^4.0|^5.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\MakerBundle\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Maker helps you create empty commands, controllers, form classes, tests and more so you can forget about writing boilerplate code.",
            "homepage": "https://symfony.com/doc/current/bundles/SymfonyMakerBundle/index.html",
            "keywords": [
                "code generator",
                "generator",
                "scaffold",
                "scaffolding"
            ],
            "support": {
                "issues": "https://github.com/symfony/maker-bundle/issues",
                "source": "https://github.com/symfony/maker-bundle/tree/v1.29.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-07T01:02:28+00:00"
        },
        {
            "name": "symfony/monolog-bridge",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/monolog-bridge.git",
                "reference": "d48bf711b47c6fa9a0df747a73ad4d45d8fc5409"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/monolog-bridge/zipball/d48bf711b47c6fa9a0df747a73ad4d45d8fc5409",
                "reference": "d48bf711b47c6fa9a0df747a73ad4d45d8fc5409",
                "shasum": ""
            },
            "require": {
                "monolog/monolog": "^1.25.1|^2",
                "php": ">=7.2.5",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/service-contracts": "^1.1|^2"
            },
            "conflict": {
                "symfony/console": "<4.4",
                "symfony/http-foundation": "<4.4"
            },
            "require-dev": {
                "symfony/console": "^4.4|^5.0",
                "symfony/http-client": "^4.4|^5.0",
                "symfony/security-core": "^4.4|^5.0",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/console": "For the possibility to show log messages in console commands depending on verbosity settings.",
                "symfony/http-kernel": "For using the debugging handlers together with the response life cycle of the HTTP kernel.",
                "symfony/var-dumper": "For using the debugging handlers like the console handler or the log server handler."
            },
            "type": "symfony-bridge",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bridge\\Monolog\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Monolog Bridge",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/monolog-bridge/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-06-18T18:18:56+00:00"
        },
        {
            "name": "symfony/monolog-bundle",
            "version": "v3.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/monolog-bundle.git",
                "reference": "e495f5c7e4e672ffef4357d4a4d85f010802f940"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/monolog-bundle/zipball/e495f5c7e4e672ffef4357d4a4d85f010802f940",
                "reference": "e495f5c7e4e672ffef4357d4a4d85f010802f940",
                "shasum": ""
            },
            "require": {
                "monolog/monolog": "~1.22 || ~2.0",
                "php": ">=5.6",
                "symfony/config": "~3.4 || ~4.0 || ^5.0",
                "symfony/dependency-injection": "~3.4.10 || ^4.0.10 || ^5.0",
                "symfony/http-kernel": "~3.4 || ~4.0 || ^5.0",
                "symfony/monolog-bridge": "~3.4 || ~4.0 || ^5.0"
            },
            "require-dev": {
                "symfony/console": "~3.4 || ~4.0 || ^5.0",
                "symfony/phpunit-bridge": "^4.4 || ^5.0",
                "symfony/yaml": "~3.4 || ~4.0 || ^5.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\MonologBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "http://symfony.com/contributors"
                }
            ],
            "description": "Symfony MonologBundle",
            "homepage": "http://symfony.com",
            "keywords": [
                "log",
                "logging"
            ],
            "support": {
                "issues": "https://github.com/symfony/monolog-bundle/issues",
                "source": "https://github.com/symfony/monolog-bundle/tree/v3.6.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-10-06T15:12:11+00:00"
        },
        {
            "name": "symfony/phpunit-bridge",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/phpunit-bridge.git",
                "reference": "587f2b6bbcda8c473b91c18165958ffbb8af3c4c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/phpunit-bridge/zipball/587f2b6bbcda8c473b91c18165958ffbb8af3c4c",
                "reference": "587f2b6bbcda8c473b91c18165958ffbb8af3c4c",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9"
            },
            "conflict": {
                "phpunit/phpunit": "<4.8.35|<5.4.3,>=5.0|<6.4,>=6.0|9.1.2"
            },
            "require-dev": {
                "symfony/deprecation-contracts": "^2.1",
                "symfony/error-handler": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/error-handler": "For tracking deprecated interfaces usages at runtime with DebugClassLoader"
            },
            "bin": [
                "bin/simple-phpunit"
            ],
            "type": "symfony-bridge",
            "extra": {
                "thanks": {
                    "name": "phpunit/phpunit",
                    "url": "https://github.com/sebastianbergmann/phpunit"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Bridge\\PhpUnit\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides utilities for PHPUnit, especially user deprecation notices management",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/phpunit-bridge/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-25T13:54:05+00:00"
        },
        {
            "name": "symfony/profiler-pack",
            "version": "v1.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/profiler-pack.git",
                "reference": "29ec66471082b4eb068db11eb4f0a48c277653f7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/profiler-pack/zipball/29ec66471082b4eb068db11eb4f0a48c277653f7",
                "reference": "29ec66471082b4eb068db11eb4f0a48c277653f7",
                "shasum": ""
            },
            "require": {
                "symfony/stopwatch": "*",
                "symfony/twig-bundle": "*",
                "symfony/web-profiler-bundle": "*"
            },
            "type": "symfony-pack",
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A pack for the Symfony web profiler",
            "support": {
                "issues": "https://github.com/symfony/profiler-pack/issues",
                "source": "https://github.com/symfony/profiler-pack/tree/v1.0.5"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-08-12T06:50:46+00:00"
        },
        {
            "name": "symfony/test-pack",
            "version": "v1.0.7",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/test-pack.git",
                "reference": "e61756c97cbedae00b7cf43b87abcfadfeb2746c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/test-pack/zipball/e61756c97cbedae00b7cf43b87abcfadfeb2746c",
                "reference": "e61756c97cbedae00b7cf43b87abcfadfeb2746c",
                "shasum": ""
            },
            "require": {
                "symfony/browser-kit": "*",
                "symfony/css-selector": "*",
                "symfony/phpunit-bridge": "*"
            },
            "type": "symfony-pack",
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A pack for functional and end-to-end testing within a Symfony app",
            "support": {
                "issues": "https://github.com/symfony/test-pack/issues",
                "source": "https://github.com/symfony/test-pack/tree/v1.0.7"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-10-19T08:52:28+00:00"
        },
        {
            "name": "symfony/web-profiler-bundle",
            "version": "v5.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/web-profiler-bundle.git",
                "reference": "3b6dbd2cc76275e117d5c55923c7f511ead22bae"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/web-profiler-bundle/zipball/3b6dbd2cc76275e117d5c55923c7f511ead22bae",
                "reference": "3b6dbd2cc76275e117d5c55923c7f511ead22bae",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/config": "^4.4|^5.0",
                "symfony/framework-bundle": "^4.4|^5.0",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/routing": "^4.4|^5.0",
                "symfony/twig-bundle": "^4.4|^5.0",
                "twig/twig": "^2.10|^3.0"
            },
            "conflict": {
                "symfony/form": "<4.4",
                "symfony/messenger": "<4.4"
            },
            "require-dev": {
                "symfony/browser-kit": "^4.4|^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/css-selector": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/stopwatch": "^4.4|^5.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\WebProfilerBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony WebProfilerBundle",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/web-profiler-bundle/tree/v5.0.11"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-23T08:36:09+00:00"
        },
        {
            "name": "theseer/fdomdocument",
            "version": "1.6.6",
            "source": {
                "type": "git",
                "url": "https://github.com/theseer/fDOMDocument.git",
                "reference": "6e8203e40a32a9c770bcb62fe37e68b948da6dca"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theseer/fDOMDocument/zipball/6e8203e40a32a9c770bcb62fe37e68b948da6dca",
                "reference": "6e8203e40a32a9c770bcb62fe37e68b948da6dca",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "lib-libxml": "*",
                "php": ">=5.3.3"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "lead"
                }
            ],
            "description": "The classes contained within this repository extend the standard DOM to use exceptions at all occasions of errors instead of PHP warnings or notices. They also add various custom methods and shortcuts for convenience and to simplify the usage of DOM.",
            "homepage": "https://github.com/theseer/fDOMDocument",
            "support": {
                "issues": "https://github.com/theseer/fDOMDocument/issues",
                "source": "https://github.com/theseer/fDOMDocument/tree/master"
            },
            "time": "2017-06-30T11:53:12+00:00"
        },
        {
            "name": "theseer/tokenizer",
            "version": "1.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/theseer/tokenizer.git",
                "reference": "75a63c33a8577608444246075ea0af0d052e452a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theseer/tokenizer/zipball/75a63c33a8577608444246075ea0af0d052e452a",
                "reference": "75a63c33a8577608444246075ea0af0d052e452a",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-tokenizer": "*",
                "ext-xmlwriter": "*",
                "php": "^7.2 || ^8.0"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                }
            ],
            "description": "A small library for converting tokenized PHP source code into XML and potentially other formats",
            "support": {
                "issues": "https://github.com/theseer/tokenizer/issues",
                "source": "https://github.com/theseer/tokenizer/tree/master"
            },
            "funding": [
                {
                    "url": "https://github.com/theseer",
                    "type": "github"
                }
            ],
            "time": "2020-07-12T23:59:07+00:00"
        }
    ],
    "aliases": [],
    "minimum-stability": "stable",
    "stability-flags": [],
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": {
        "php": "7.4.*",
        "ext-ctype": "*",
        "ext-iconv": "*",
        "ext-json": "*",
        "ext-pdo": "*"
    },
    "platform-dev": [],
    "plugin-api-version": "2.0.0"
}
```

## File: `depfile.yaml`
```yaml
paths:
  - ./src
exclude_files:
  - Kernel.php
layers:
  - name: CoreApplication
    collectors:
      - type: className
        regex: .*App\\Core\\Application\\(?!Query).*
  - name: CoreDomain
    collectors:
      - type: className
        regex: .*App\\Core\\Domain\\.*
  - name: CoreInfrastructure
    collectors:
      - type: className
        regex: .*App\\Core\\Infrastructure\\.*
  - name: CorePorts
    collectors:
      - type: className
        regex: .*App\\Core\\Ports\\.*
  - name: SharedDomain
    collectors:
      - type: className
        regex: .*App\\Shared\\Domain\\.*
  - name: SharedInfrastructure
    collectors:
      - type: className
        regex: .*App\\Shared\\Infrastructure\\.*
ruleset:
  CoreApplication:
    - CoreDomain
    - SharedDomain
  CoreDomain:
    - SharedDomain
  CorePorts:
    - CoreApplication
    - CoreInfrastructure
    - SharedInfrastructure
  CoreInfrastructure:
    - CoreDomain
  SharedDomain: ~
  SharedInfrastructure:
    - SharedDomain
```

## File: `phpstan.neon`
```
parameters:
    level: max
    excludes_analyse:
        - src/Shared/Infrastructure/Migration/*
includes:
    - vendor/phpstan/phpstan-webmozart-assert/extension.neon
    - vendor/phpstan/phpstan-doctrine/extension.neon
    - vendor/phpstan/phpstan-doctrine/rules.neon
    - vendor/phpstan/phpstan-strict-rules/rules.neon
```

## File: `phpunit.xml.dist`
```
<?xml version="1.0" encoding="UTF-8"?>

<!-- https://phpunit.de/manual/current/en/appendixes.configuration.html -->
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="http://schema.phpunit.de/6.1/phpunit.xsd"
         backupGlobals="false"
         colors="true"
         bootstrap="tests/bootstrap.php"
         defaultTestSuite="Unit"
         executionOrder="random"
>
    <testsuites>
        <testsuite name="Unit">
            <directory>./tests/Unit</directory>
        </testsuite>
    </testsuites>

    <filter>
        <whitelist>
            <directory>./src/</directory>
        </whitelist>
    </filter>
</phpunit>
```

## File: `setup_env`
```
#!/usr/bin/env bash

if [ -z "$1" ]
then
  echo 'Enter the environment by first argument [dev, prod, test]'
  exit 1
fi

#docker
PUID=$(id -u)
PGID=$(id -g)
DB_ROOT_PASSWORD=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 6 ; echo '')
DB_PASSWORD=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 6 ; echo '')

#app
APP_ENV=dev
APP_SECRET=$(xxd -l 16 -p /dev/random)
DATABASE_URL="mysql:\/\/task:${DB_PASSWORD}@db:3306\/task?serverVersion=8.0"

#docker
cp ./docker/.env.dist ./docker/.env && \
sed -i "s/^PUID=.*/PUID=${PUID}/g" ./docker/.env && \
sed -i "s/^PGID=.*/PGID=${PGID}/g" ./docker/.env && \
sed -i "s/^DB_ROOT_PASSWORD=.*/DB_ROOT_PASSWORD=${DB_ROOT_PASSWORD}/g" ./docker/.env && \
sed -i "s/^DB_PASSWORD=.*/DB_PASSWORD=${DB_PASSWORD}/g" ./docker/.env

#application
cp .env .env.local && \
sed -i "s/^APP_ENV=.*/APP_ENV=${APP_ENV}/g" .env.local && \
sed -i "s/^APP_SECRET=.*/APP_SECRET=${APP_SECRET}/g" .env.local && \
sed -i "s/^DATABASE_URL=.*/DATABASE_URL=${DATABASE_URL}/g" .env.local

#jwt keys
mkdir -p config/jwt && \
openssl genpkey -out config/jwt/private.pem -aes256 -algorithm rsa -pkeyopt rsa_keygen_bits:4096 && \
openssl pkey -in config/jwt/private.pem -out config/jwt/public.pem -pubout

echo -n "Enter PEM password to save in .env.local: "
read -s JWT_PASSPHRASE
sed -i "s/^JWT_PASSPHRASE=.*/JWT_PASSPHRASE=${JWT_PASSPHRASE}/g" .env.local
```

## File: `setup_env.sh`
```bash
#!/usr/bin/env bash

if [ -z "$1" ]
then
  echo 'Enter the environment by first argument [dev, prod, test]'
  exit 1
fi

#docker
PUID=$(id -u)
PGID=$(id -g)
DB_ROOT_PASSWORD=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 6 ; echo '')
DB_PASSWORD=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 6 ; echo '')

#app
APP_ENV=dev
APP_SECRET=$(xxd -l 16 -p /dev/random)
DATABASE_URL="mysql:\/\/task:${DB_PASSWORD}@db:3306\/task?serverVersion=8.0"

#docker
cp ./docker/.env.dist ./docker/.env && \
sed -i "s/^PUID=.*/PUID=${PUID}/g" ./docker/.env && \
sed -i "s/^PGID=.*/PGID=${PGID}/g" ./docker/.env && \
sed -i "s/^DB_ROOT_PASSWORD=.*/DB_ROOT_PASSWORD=${DB_ROOT_PASSWORD}/g" ./docker/.env && \
sed -i "s/^DB_PASSWORD=.*/DB_PASSWORD=${DB_PASSWORD}/g" ./docker/.env

#application
cp .env .env.local && \
sed -i "s/^APP_ENV=.*/APP_ENV=${APP_ENV}/g" .env.local && \
sed -i "s/^APP_SECRET=.*/APP_SECRET=${APP_SECRET}/g" .env.local && \
sed -i "s/^DATABASE_URL=.*/DATABASE_URL=${DATABASE_URL}/g" .env.local

#jwt keys
mkdir -p config/jwt && \
openssl genpkey -out config/jwt/private.pem -aes256 -algorithm rsa -pkeyopt rsa_keygen_bits:4096 && \
openssl pkey -in config/jwt/private.pem -out config/jwt/public.pem -pubout

echo -n "Enter PEM password to save in .env.local: "
read -s JWT_PASSPHRASE
sed -i "s/^JWT_PASSPHRASE=.*/JWT_PASSPHRASE=${JWT_PASSPHRASE}/g" .env.local
```

## File: `symfony.lock`
```
{
    "doctrine/annotations": {
        "version": "1.0",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "1.0",
            "ref": "a2759dd6123694c8d901d0ec80006e044c2e6457"
        },
        "files": [
            "config/routes/annotations.yaml"
        ]
    },
    "doctrine/cache": {
        "version": "1.10.0"
    },
    "doctrine/collections": {
        "version": "1.6.5"
    },
    "doctrine/common": {
        "version": "2.13.1"
    },
    "doctrine/dbal": {
        "version": "2.10.2"
    },
    "doctrine/doctrine-bundle": {
        "version": "2.0",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "2.0",
            "ref": "a9f2463b9f73efe74482f831f03a204a41328555"
        },
        "files": [
            "config/packages/doctrine.yaml",
            "config/packages/prod/doctrine.yaml",
            "src/Entity/.gitignore",
            "src/Repository/.gitignore"
        ]
    },
    "doctrine/doctrine-migrations-bundle": {
        "version": "1.2",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "1.2",
            "ref": "c1431086fec31f17fbcfe6d6d7e92059458facc1"
        },
        "files": [
            "config/packages/doctrine_migrations.yaml",
            "src/Migrations/.gitignore"
        ]
    },
    "doctrine/event-manager": {
        "version": "1.1.0"
    },
    "doctrine/inflector": {
        "version": "1.4.2"
    },
    "doctrine/instantiator": {
        "version": "1.3.0"
    },
    "doctrine/lexer": {
        "version": "1.2.1"
    },
    "doctrine/migrations": {
        "version": "2.2.1"
    },
    "doctrine/orm": {
        "version": "v2.7.2"
    },
    "doctrine/persistence": {
        "version": "1.3.7"
    },
    "doctrine/reflection": {
        "version": "1.2.1"
    },
    "doctrine/sql-formatter": {
        "version": "1.0.1"
    },
    "exsyst/swagger": {
        "version": "v0.4.1"
    },
    "laminas/laminas-code": {
        "version": "3.4.1"
    },
    "laminas/laminas-eventmanager": {
        "version": "3.2.1"
    },
    "laminas/laminas-zendframework-bridge": {
        "version": "1.0.4"
    },
    "lcobucci/clock": {
        "version": "2.0.0"
    },
    "lcobucci/jwt": {
        "version": "4.1.0"
    },
    "lexik/jwt-authentication-bundle": {
        "version": "2.5",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "2.5",
            "ref": "5b2157bcd5778166a5696e42f552ad36529a07a6"
        },
        "files": [
            "config/packages/lexik_jwt_authentication.yaml"
        ]
    },
    "monolog/monolog": {
        "version": "2.1.0"
    },
    "myclabs/deep-copy": {
        "version": "1.9.5"
    },
    "namshi/jose": {
        "version": "7.2.3"
    },
    "nelmio/api-doc-bundle": {
        "version": "3.0",
        "recipe": {
            "repo": "github.com/symfony/recipes-contrib",
            "branch": "master",
            "version": "3.0",
            "ref": "c8e0c38e1a280ab9e37587a8fa32b251d5bc1c94"
        },
        "files": [
            "config/packages/nelmio_api_doc.yaml",
            "config/routes/nelmio_api_doc.yaml"
        ]
    },
    "nikic/php-parser": {
        "version": "v4.4.0"
    },
    "ocramius/package-versions": {
        "version": "1.8.0"
    },
    "ocramius/proxy-manager": {
        "version": "2.8.0"
    },
    "phar-io/manifest": {
        "version": "1.0.3"
    },
    "phar-io/version": {
        "version": "2.0.1"
    },
    "php": {
        "version": "7.4"
    },
    "phpdocumentor/reflection-common": {
        "version": "2.1.0"
    },
    "phpdocumentor/reflection-docblock": {
        "version": "5.1.0"
    },
    "phpdocumentor/type-resolver": {
        "version": "1.1.0"
    },
    "phpspec/prophecy": {
        "version": "v1.10.3"
    },
    "phpstan/phpstan": {
        "version": "0.12.25"
    },
    "phpstan/phpstan-doctrine": {
        "version": "0.12.13"
    },
    "phpstan/phpstan-phpunit": {
        "version": "0.12.8"
    },
    "phpstan/phpstan-strict-rules": {
        "version": "0.12.2"
    },
    "phpstan/phpstan-symfony": {
        "version": "0.12.6"
    },
    "phpstan/phpstan-webmozart-assert": {
        "version": "0.12.4"
    },
    "phpunit/php-code-coverage": {
        "version": "8.0.2"
    },
    "phpunit/php-file-iterator": {
        "version": "3.0.1"
    },
    "phpunit/php-invoker": {
        "version": "3.0.0"
    },
    "phpunit/php-text-template": {
        "version": "2.0.0"
    },
    "phpunit/php-timer": {
        "version": "3.1.4"
    },
    "phpunit/php-token-stream": {
        "version": "4.0.1"
    },
    "phpunit/phpunit": {
        "version": "4.7",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "4.7",
            "ref": "00fdb38c318774cd39f475a753028a5e8d25d47c"
        },
        "files": [
            ".env.test",
            "phpunit.xml.dist",
            "tests/bootstrap.php"
        ]
    },
    "psr/cache": {
        "version": "1.0.1"
    },
    "psr/container": {
        "version": "1.0.0"
    },
    "psr/event-dispatcher": {
        "version": "1.0.0"
    },
    "psr/log": {
        "version": "1.1.3"
    },
    "sebastian/code-unit": {
        "version": "1.0.2"
    },
    "sebastian/code-unit-reverse-lookup": {
        "version": "2.0.0"
    },
    "sebastian/comparator": {
        "version": "4.0.0"
    },
    "sebastian/diff": {
        "version": "4.0.1"
    },
    "sebastian/environment": {
        "version": "5.1.0"
    },
    "sebastian/exporter": {
        "version": "4.0.0"
    },
    "sebastian/finder-facade": {
        "version": "2.0.0"
    },
    "sebastian/global-state": {
        "version": "4.0.0"
    },
    "sebastian/object-enumerator": {
        "version": "4.0.0"
    },
    "sebastian/object-reflector": {
        "version": "2.0.0"
    },
    "sebastian/phpcpd": {
        "version": "5.0.2"
    },
    "sebastian/recursion-context": {
        "version": "4.0.0"
    },
    "sebastian/resource-operations": {
        "version": "3.0.0"
    },
    "sebastian/type": {
        "version": "2.0.0"
    },
    "sebastian/version": {
        "version": "3.0.0"
    },
    "sensiolabs-de/deptrac-shim": {
        "version": "0.7",
        "recipe": {
            "repo": "github.com/symfony/recipes-contrib",
            "branch": "master",
            "version": "0.7",
            "ref": "1f7e6648916732a736466ccf2caa5b4b4e7f4968"
        },
        "files": [
            "depfile.yaml"
        ]
    },
    "sensiolabs/security-checker": {
        "version": "4.0",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "4.0",
            "ref": "160c9b600564faa1224e8f387d49ef13ceb8b793"
        },
        "files": [
            "config/packages/security_checker.yaml"
        ]
    },
    "symfony/asset": {
        "version": "v5.0.8"
    },
    "symfony/browser-kit": {
        "version": "v5.0.8"
    },
    "symfony/cache": {
        "version": "v5.0.8"
    },
    "symfony/cache-contracts": {
        "version": "v2.0.1"
    },
    "symfony/config": {
        "version": "v5.0.8"
    },
    "symfony/console": {
        "version": "4.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "4.4",
            "ref": "ea8c0eda34fda57e7d5cd8cbd889e2a387e3472c"
        },
        "files": [
            "bin/console",
            "config/bootstrap.php"
        ]
    },
    "symfony/css-selector": {
        "version": "v5.0.8"
    },
    "symfony/debug-bundle": {
        "version": "4.1",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "4.1",
            "ref": "f8863cbad2f2e58c4b65fa1eac892ab189971bea"
        },
        "files": [
            "config/packages/dev/debug.yaml"
        ]
    },
    "symfony/debug-pack": {
        "version": "v1.0.8"
    },
    "symfony/dependency-injection": {
        "version": "v5.0.8"
    },
    "symfony/doctrine-bridge": {
        "version": "v5.0.8"
    },
    "symfony/dom-crawler": {
        "version": "v5.0.8"
    },
    "symfony/dotenv": {
        "version": "v5.0.8"
    },
    "symfony/error-handler": {
        "version": "v5.0.8"
    },
    "symfony/event-dispatcher": {
        "version": "v5.0.8"
    },
    "symfony/event-dispatcher-contracts": {
        "version": "v2.0.1"
    },
    "symfony/filesystem": {
        "version": "v5.0.8"
    },
    "symfony/finder": {
        "version": "v5.0.8"
    },
    "symfony/flex": {
        "version": "1.0",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "1.0",
            "ref": "c0eeb50665f0f77226616b6038a9b06c03752d8e"
        },
        "files": [
            ".env"
        ]
    },
    "symfony/framework-bundle": {
        "version": "4.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "4.4",
            "ref": "36d3075b2b8e0c4de0e82356a86e4c4a4eb6681b"
        },
        "files": [
            "config/bootstrap.php",
            "config/packages/cache.yaml",
            "config/packages/framework.yaml",
            "config/packages/test/framework.yaml",
            "config/routes/dev/framework.yaml",
            "config/services.yaml",
            "public/index.php",
            "src/Controller/.gitignore",
            "src/Kernel.php"
        ]
    },
    "symfony/http-client": {
        "version": "v5.0.8"
    },
    "symfony/http-client-contracts": {
        "version": "v2.1.2"
    },
    "symfony/http-foundation": {
        "version": "v5.0.8"
    },
    "symfony/http-kernel": {
        "version": "v5.0.8"
    },
    "symfony/inflector": {
        "version": "v5.0.8"
    },
    "symfony/maker-bundle": {
        "version": "1.0",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "1.0",
            "ref": "fadbfe33303a76e25cb63401050439aa9b1a9c7f"
        }
    },
    "symfony/messenger": {
        "version": "4.3",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "4.3",
            "ref": "8a2675c061737658bed85102e9241c752620e575"
        },
        "files": [
            "config/packages/messenger.yaml"
        ]
    },
    "symfony/mime": {
        "version": "v5.0.8"
    },
    "symfony/monolog-bridge": {
        "version": "v5.0.8"
    },
    "symfony/monolog-bundle": {
        "version": "3.3",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "3.3",
            "ref": "a89f4cd8a232563707418eea6c2da36acd36a917"
        },
        "files": [
            "config/packages/dev/monolog.yaml",
            "config/packages/prod/monolog.yaml",
            "config/packages/test/monolog.yaml"
        ]
    },
    "symfony/options-resolver": {
        "version": "v5.0.11"
    },
    "symfony/orm-pack": {
        "version": "v1.0.8"
    },
    "symfony/phpunit-bridge": {
        "version": "4.3",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "4.3",
            "ref": "6d0e35f749d5f4bfe1f011762875275cd3f9874f"
        },
        "files": [
            ".env.test",
            "bin/phpunit",
            "phpunit.xml.dist",
            "tests/bootstrap.php"
        ]
    },
    "symfony/polyfill-intl-idn": {
        "version": "v1.17.0"
    },
    "symfony/polyfill-mbstring": {
        "version": "v1.17.0"
    },
    "symfony/polyfill-php73": {
        "version": "v1.17.0"
    },
    "symfony/profiler-pack": {
        "version": "v1.0.4"
    },
    "symfony/property-access": {
        "version": "v5.0.8"
    },
    "symfony/property-info": {
        "version": "v5.0.8"
    },
    "symfony/routing": {
        "version": "4.2",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "4.2",
            "ref": "683dcb08707ba8d41b7e34adb0344bfd68d248a7"
        },
        "files": [
            "config/packages/prod/routing.yaml",
            "config/packages/routing.yaml",
            "config/routes.yaml"
        ]
    },
    "symfony/security-bundle": {
        "version": "4.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "4.4",
            "ref": "7b4408dc203049666fe23fabed23cbadc6d8440f"
        },
        "files": [
            "config/packages/security.yaml"
        ]
    },
    "symfony/security-core": {
        "version": "v5.0.11"
    },
    "symfony/security-csrf": {
        "version": "v5.0.11"
    },
    "symfony/security-guard": {
        "version": "v5.0.11"
    },
    "symfony/security-http": {
        "version": "v5.0.11"
    },
    "symfony/serializer": {
        "version": "v5.0.8"
    },
    "symfony/serializer-pack": {
        "version": "v1.0.3"
    },
    "symfony/service-contracts": {
        "version": "v2.0.1"
    },
    "symfony/stopwatch": {
        "version": "v5.0.8"
    },
    "symfony/test-pack": {
        "version": "v1.0.6"
    },
    "symfony/translation-contracts": {
        "version": "v2.0.1"
    },
    "symfony/twig-bridge": {
        "version": "v5.0.8"
    },
    "symfony/twig-bundle": {
        "version": "5.0",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "5.0",
            "ref": "fab9149bbaa4d5eca054ed93f9e1b66cc500895d"
        },
        "files": [
            "config/packages/test/twig.yaml",
            "config/packages/twig.yaml",
            "templates/base.html.twig"
        ]
    },
    "symfony/twig-pack": {
        "version": "v1.0.0"
    },
    "symfony/var-dumper": {
        "version": "v5.0.8"
    },
    "symfony/var-exporter": {
        "version": "v5.0.8"
    },
    "symfony/web-profiler-bundle": {
        "version": "3.3",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "3.3",
            "ref": "6bdfa1a95f6b2e677ab985cd1af2eae35d62e0f6"
        },
        "files": [
            "config/packages/dev/web_profiler.yaml",
            "config/packages/test/web_profiler.yaml",
            "config/routes/dev/web_profiler.yaml"
        ]
    },
    "symfony/yaml": {
        "version": "v5.0.8"
    },
    "theseer/fdomdocument": {
        "version": "1.6.6"
    },
    "theseer/tokenizer": {
        "version": "1.1.3"
    },
    "twig/extra-bundle": {
        "version": "v3.0.3"
    },
    "twig/twig": {
        "version": "v3.0.3"
    },
    "webimpress/safe-writer": {
        "version": "2.0.1"
    },
    "webmozart/assert": {
        "version": "1.8.0"
    },
    "zircote/swagger-php": {
        "version": "3.1.0"
    }
}
```

## File: `config/bootstrap.php`
```php
<?php

use Symfony\Component\Dotenv\Dotenv;

require dirname(__DIR__).'/vendor/autoload.php';

if (!class_exists(Dotenv::class)) {
    throw new LogicException('Please run "composer require symfony/dotenv" to load the ".env" files configuring the application.');
}

// Load cached env vars if the .env.local.php file exists
// Run "composer dump-env prod" to create it (requires symfony/flex >=1.2)
if (is_array($env = @include dirname(__DIR__).'/.env.local.php') && (!isset($env['APP_ENV']) || ($_SERVER['APP_ENV'] ?? $_ENV['APP_ENV'] ?? $env['APP_ENV']) === $env['APP_ENV'])) {
    (new Dotenv(false))->populate($env);
} else {
    // load all the .env files
    (new Dotenv(false))->loadEnv(dirname(__DIR__).'/.env');
}

$_SERVER += $_ENV;
$_SERVER['APP_ENV'] = $_ENV['APP_ENV'] = ($_SERVER['APP_ENV'] ?? $_ENV['APP_ENV'] ?? null) ?: 'dev';
$_SERVER['APP_DEBUG'] = $_SERVER['APP_DEBUG'] ?? $_ENV['APP_DEBUG'] ?? 'prod' !== $_SERVER['APP_ENV'];
$_SERVER['APP_DEBUG'] = $_ENV['APP_DEBUG'] = (int) $_SERVER['APP_DEBUG'] || filter_var($_SERVER['APP_DEBUG'], FILTER_VALIDATE_BOOLEAN) ? '1' : '0';
```

## File: `config/bundles.php`
```php
<?php

return [
    Symfony\Bundle\FrameworkBundle\FrameworkBundle::class => ['all' => true],
    Doctrine\Bundle\DoctrineBundle\DoctrineBundle::class => ['all' => true],
    Doctrine\Bundle\MigrationsBundle\DoctrineMigrationsBundle::class => ['all' => true],
    Symfony\Bundle\MakerBundle\MakerBundle::class => ['dev' => true],
    Symfony\Bundle\TwigBundle\TwigBundle::class => ['all' => true],
    Twig\Extra\TwigExtraBundle\TwigExtraBundle::class => ['all' => true],
    Symfony\Bundle\WebProfilerBundle\WebProfilerBundle::class => ['dev' => true, 'test' => true],
    Symfony\Bundle\MonologBundle\MonologBundle::class => ['all' => true],
    Symfony\Bundle\DebugBundle\DebugBundle::class => ['dev' => true, 'test' => true],
    Symfony\Bundle\SecurityBundle\SecurityBundle::class => ['all' => true],
    Lexik\Bundle\JWTAuthenticationBundle\LexikJWTAuthenticationBundle::class => ['all' => true],
    Nelmio\ApiDocBundle\NelmioApiDocBundle::class => ['all' => true],
];
```

## File: `config/routes.yaml`
```yaml
api_login_check:
    path: /api/login_check
```

## File: `config/services.yaml`
```yaml
# This file is the entry point to configure your own services.
# Files in the packages/ subdirectory configure your dependencies.

# Put parameters here that don't need to change on each machine where the app is deployed
# https://symfony.com/doc/current/best_practices/configuration.html#application-related-configuration
parameters:

services:
    # default configuration for services in *this* file
    _defaults:
        autowire: true      # Automatically injects dependencies in your services.
        autoconfigure: true # Automatically registers your services as commands, event subscribers, etc.

    # makes classes in src/ available to be used as services
    # this creates a service per class whose id is the fully-qualified class name
    App\:
        resource: '../src/*'
        exclude:
            - '../src/Shared/Infrastructure/Migration'

    App\Core\Ports\Rest\:
        resource: '../src/Core/Ports/Rest'
        tags: ['controller.service_arguments']

    command_handlers:
        namespace: App\Core\Application\Command\
        resource: '%kernel.project_dir%/src/Core/Application/Command/*/*/*CommandHandler.php'
        autoconfigure: false
        tags:
            - { name: messenger.message_handler, bus: command.bus }

    query_handlers:
        namespace: App\Core\Application\Query\
        resource: '%kernel.project_dir%/src/Core/Application/Query/*/*/*QueryHandler.php'
        autoconfigure: false
        tags:
            - { name: messenger.message_handler, bus: query.bus }

    event_handlers:
        namespace: App\Core\Application\
        resource: '%kernel.project_dir%/src/Core/Application/**/*EventHandler.php'
        autoconfigure: false
        tags:
            - { name: messenger.message_handler, bus: event.bus }

    App\Shared\Infrastructure\Doctrine\DomainEventSubscriber:
        tags: [{name: 'doctrine.event_subscriber'}]
```

## File: `config/packages/cache.yaml`
```yaml
framework:
    cache:
        # Unique name of your app: used to compute stable namespaces for cache keys.
        #prefix_seed: your_vendor_name/app_name

        # The "app" cache stores to the filesystem by default.
        # The data in this cache should persist between deploys.
        # Other options include:

        # Redis
        #app: cache.adapter.redis
        #default_redis_provider: redis://localhost

        # APCu (not recommended with heavy random-write workloads as memory fragmentation can cause perf issues)
        #app: cache.adapter.apcu

        # Namespaced pools use the above "app" backend by default
        #pools:
            #my.dedicated.cache: null
```

## File: `config/packages/doctrine.yaml`
```yaml
doctrine:
    dbal:
        url: '%env(resolve:DATABASE_URL)%'
        mapping_types:
            enum: string
    orm:
        auto_generate_proxy_classes: true
        naming_strategy: doctrine.orm.naming_strategy.underscore_number_aware
        auto_mapping: true
        mappings:
            App:
                is_bundle: false
                type: annotation
                dir: '%kernel.project_dir%/src/Core/Domain/Model'
                prefix: 'App\Core\Domain\Model'
                alias: App
```

## File: `config/packages/doctrine_migrations.yaml`
```yaml
doctrine_migrations:
    dir_name: '%kernel.project_dir%/src/Shared/Infrastructure/Migration'
    # namespace is arbitrary but should be different from App\Migrations
    # as migrations classes should NOT be autoloaded
    namespace: DoctrineMigrations
```

## File: `config/packages/framework.yaml`
```yaml
framework:
    secret: '%env(APP_SECRET)%'
    #csrf_protection: true
    #http_method_override: true

    # Enables session support. Note that the session will ONLY be started if you read or write from it.
    # Remove or comment this section to explicitly disable session support.
    session:
        handler_id: null
        cookie_secure: auto
        cookie_samesite: lax

    #esi: true
    #fragments: true
    php_errors:
        log: true

    serializer:
        name_converter: 'serializer.name_converter.camel_case_to_snake_case'
        mapping:
            paths:
                - '%kernel.project_dir%/src/Core/Ports/Rest/SerializerMapping'
```

## File: `config/packages/lexik_jwt_authentication.yaml`
```yaml
lexik_jwt_authentication:
    secret_key: '%env(resolve:JWT_SECRET_KEY)%'
    public_key: '%env(resolve:JWT_PUBLIC_KEY)%'
    pass_phrase: '%env(JWT_PASSPHRASE)%'
```

## File: `config/packages/messenger.yaml`
```yaml
framework:
    messenger:
        default_bus: event.bus
        buses:
            command.bus:
                middleware:
                    - doctrine_transaction
            query.bus:
            event.bus:
                default_middleware: allow_no_handlers
```

## File: `config/packages/nelmio_api_doc.yaml`
```yaml
nelmio_api_doc:
    models: { use_jms: false }
    documentation:
        info:
            title: My App
            description: This is an awesome app!
            version: 1.0.0
        securityDefinitions:
            Bearer:
                type: apiKey
                description: 'Value: Bearer {jwt}'
                name: Authorization
                in: header
        security:
            - Bearer: []
    areas: # to filter documented areas
        path_patterns:
            - ^/api(?!/doc$) # Accepts routes under /api except /api/doc
```

## File: `config/packages/routing.yaml`
```yaml
framework:
    router:
        utf8: true
```

## File: `config/packages/security.yaml`
```yaml
security:
    encoders:
        App\Core\Domain\Model\User\User:
            algorithm: auto

    providers:
        app_user_provider:
            entity:
                class: App\Core\Domain\Model\User\User
                property: username
    firewalls:
        api_doc:
            pattern:  ^/api/doc
            stateless: true
            anonymous: true
        create_token:
            pattern:  ^/api/auth-token
            stateless: true
            anonymous: true
        login:
            pattern:  ^/api/login
            stateless: true
            anonymous: true
            json_login:
                check_path:               /api/login_check
                success_handler:          lexik_jwt_authentication.handler.authentication_success
                failure_handler:          lexik_jwt_authentication.handler.authentication_failure

        api:
            pattern:   ^/api
            stateless: true
            guard:
                authenticators:
                    - lexik_jwt_authentication.jwt_token_authenticator

    access_control:
        - { path: ^/api/login, roles: IS_AUTHENTICATED_ANONYMOUSLY }
        - { path: ^/api/auth-token, roles: IS_AUTHENTICATED_ANONYMOUSLY }
        - { path: ^/api/doc, roles: IS_AUTHENTICATED_ANONYMOUSLY }
        - { path: ^/api,       roles: IS_AUTHENTICATED_FULLY }
```

## File: `config/packages/security_checker.yaml`
```yaml
services:
    _defaults:
        autowire: true
        autoconfigure: true

    SensioLabs\Security\SecurityChecker: null

    SensioLabs\Security\Command\SecurityCheckerCommand: null
```

## File: `config/packages/twig.yaml`
```yaml
twig:
    default_path: '%kernel.project_dir%/templates'
```

## File: `config/packages/dev/debug.yaml`
```yaml
debug:
    # Forwards VarDumper Data clones to a centralized server allowing to inspect dumps on CLI or in your browser.
    # See the "server:dump" command to start a new server.
    dump_destination: "tcp://%env(VAR_DUMPER_SERVER)%"
```

## File: `config/packages/dev/monolog.yaml`
```yaml
monolog:
    handlers:
        main:
            type: stream
            path: "%kernel.logs_dir%/%kernel.environment%.log"
            level: debug
            channels: ["!event"]
        # uncomment to get logging in your browser
        # you may have to allow bigger header sizes in your Web server configuration
        #firephp:
        #    type: firephp
        #    level: info
        #chromephp:
        #    type: chromephp
        #    level: info
        console:
            type: console
            process_psr_3_messages: false
            channels: ["!event", "!doctrine", "!console"]
```

## File: `config/packages/dev/web_profiler.yaml`
```yaml
web_profiler:
    toolbar: true
    intercept_redirects: false

framework:
    profiler: { only_exceptions: false }
```

## File: `config/packages/prod/doctrine.yaml`
```yaml
doctrine:
    orm:
        auto_generate_proxy_classes: false
        metadata_cache_driver:
            type: pool
            pool: doctrine.system_cache_pool
        query_cache_driver:
            type: pool
            pool: doctrine.system_cache_pool
        result_cache_driver:
            type: pool
            pool: doctrine.result_cache_pool

framework:
    cache:
        pools:
            doctrine.result_cache_pool:
                adapter: cache.app
            doctrine.system_cache_pool:
                adapter: cache.system
```

## File: `config/packages/prod/monolog.yaml`
```yaml
monolog:
    handlers:
        main:
            type: fingers_crossed
            action_level: error
            handler: nested
            excluded_http_codes: [404, 405]
            buffer_size: 50 # How many messages should be saved? Prevent memory leaks
        nested:
            type: stream
            path: "%kernel.logs_dir%/%kernel.environment%.log"
            level: debug
        console:
            type: console
            process_psr_3_messages: false
            channels: ["!event", "!doctrine"]

        # Uncomment to log deprecations
        #deprecation:
        #    type: stream
        #    path: "%kernel.logs_dir%/%kernel.environment%.deprecations.log"
        #deprecation_filter:
        #    type: filter
        #    handler: deprecation
        #    max_level: info
        #    channels: ["php"]
```

## File: `config/packages/prod/routing.yaml`
```yaml
framework:
    router:
        strict_requirements: null
```

## File: `config/packages/test/framework.yaml`
```yaml
framework:
    test: true
    session:
        storage_id: session.storage.mock_file
```

## File: `config/packages/test/monolog.yaml`
```yaml
monolog:
    handlers:
        main:
            type: fingers_crossed
            action_level: error
            handler: nested
            excluded_http_codes: [404, 405]
            channels: ["!event"]
        nested:
            type: stream
            path: "%kernel.logs_dir%/%kernel.environment%.log"
            level: debug
```

## File: `config/packages/test/twig.yaml`
```yaml
twig:
    strict_variables: true
```

## File: `config/packages/test/web_profiler.yaml`
```yaml
web_profiler:
    toolbar: false
    intercept_redirects: false

framework:
    profiler: { collect: false }
```

## File: `config/routes/annotations.yaml`
```yaml
controllers:
    resource: ../../src/Core/Ports/Rest/
    type: annotation
kernel:
    resource: ../../src/Kernel.php
    type: annotation
```

## File: `config/routes/nelmio_api_doc.yaml`
```yaml
# Expose your documentation as JSON swagger compliant
app.swagger:
    path: /api/doc.json
    methods: GET
    defaults: { _controller: nelmio_api_doc.controller.swagger }

## Requires the Asset component and the Twig bundle
## $ composer require twig asset
#app.swagger_ui:
#    path: /api/doc
#    methods: GET
#    defaults: { _controller: nelmio_api_doc.controller.swagger_ui }
```

## File: `config/routes/dev/framework.yaml`
```yaml
_errors:
    resource: '@FrameworkBundle/Resources/config/routing/errors.xml'
    prefix: /_error
```

## File: `config/routes/dev/web_profiler.yaml`
```yaml
web_profiler_wdt:
    resource: '@WebProfilerBundle/Resources/config/routing/wdt.xml'
    prefix: /_wdt

web_profiler_profiler:
    resource: '@WebProfilerBundle/Resources/config/routing/profiler.xml'
    prefix: /_profiler
```

## File: `docker/.dockerignore`
```
../var/**
../vendor/**
../.env.local
../.env.*.local
../config/jwt
```

## File: `docker/.env.dist`
```
#users ids could retrieved by the command `id $USER`
PUID=1000
PGID=1000

#mysql
DB_ROOT_PASSWORD=
DB_DATABASE=task
DB_USER=task
DB_PASSWORD=

MYSQL_PORT=3377

#nginx
NGINX_HOST_HTTP_PORT=888
NGINX_HOST_HTTPS_PORT=444

COMPOSE_PROJECT_NAME=task
```

## File: `docker/docker-compose.yml`
```yaml
version: "3.4"

services:
  php-fpm:
    build:
      context: ./php-fpm
      args:
        - PUID=${PUID}
        - PGID=${PGID}
    volumes:
      - ..:/var/www/:rw
    depends_on:
      - db
    networks:
      - main

  db:
    build:
      context: ./mysql
    volumes:
      - db-data:/var/lib/mysql:rw
    environment:
      - MYSQL_ROOT_PASSWORD=${DB_ROOT_PASSWORD}
      - MYSQL_DATABASE=${DB_DATABASE}
      - MYSQL_USER=${DB_USER}
      - MYSQL_PASSWORD=${DB_PASSWORD}
    ports:
      - "${MYSQL_PORT}:3306"
    networks:
      - main

  nginx:
    build:
      context: ./nginx
    volumes:
      - ..:/var/www:rw
    ports:
      - "${NGINX_HOST_HTTP_PORT}:80"
      - "${NGINX_HOST_HTTPS_PORT}:443"
    depends_on:
      - php-fpm
    networks:
      - main

  workplace:
    build:
      context: ./workplace
      args:
        - PUID=${PUID}
        - PGID=${PGID}
    volumes:
      - ..:/var/www/:rw
    tty: true
    depends_on:
      - db
    networks:
      - main

volumes:
  db-data: {}

networks:
  main:
```

## File: `docker/mysql/Dockerfile`
```
FROM mysql:8.0

ARG TZ=UTC
ENV TZ ${TZ}
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && chown -R mysql:root /var/lib/mysql/

COPY my.cnf /etc/mysql/conf.d/my.cnf

RUN chmod 0444 /etc/mysql/conf.d/my.cnf

CMD ["mysqld"]

EXPOSE 3306
```

## File: `docker/mysql/my.cnf`
```

# The MySQL  Client configuration file.
#
# For explanations see
# http://dev.mysql.com/doc/mysql/en/server-system-variables.html

[mysql]

[mysqld]
sql-mode="STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION"
character-set-server=utf8
default-authentication-plugin=mysql_native_password
```

## File: `docker/nginx/Dockerfile`
```

FROM nginx:alpine

COPY nginx.conf /etc/nginx/
COPY default.conf /etc/nginx/conf.d/

RUN apk update \
    && apk upgrade \
    && apk add --no-cache openssl \
    && apk add --no-cache bash

RUN apk add --no-cache curl

RUN set -x ; \
    addgroup -g 82 -S www-data ; \
    adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

ARG PHP_UPSTREAM_CONTAINER=php-fpm
ARG PHP_UPSTREAM_PORT=9000


# Set upstream conf and remove the default conf
RUN echo "upstream php-upstream { server ${PHP_UPSTREAM_CONTAINER}:${PHP_UPSTREAM_PORT}; }" > /etc/nginx/conf.d/upstream.conf

RUN mkdir "/etc/nginx/ssl" \
    && openssl genrsa -out "/etc/nginx/ssl/default.key" 2048 \
    && openssl req -new -key "/etc/nginx/ssl/default.key" -out "/etc/nginx/ssl/default.csr" -subj "/CN=default/O=default/C=UK" \
    && openssl x509 -req -days 365 -in "/etc/nginx/ssl/default.csr" -signkey "/etc/nginx/ssl/default.key" -out "/etc/nginx/ssl/default.crt"

EXPOSE 80 443
```

## File: `docker/nginx/default.conf`
```
server {

    listen 80;
    listen [::]:80;

    listen 443 ssl;
    listen [::]:443 ssl ipv6only=on;
    ssl_certificate /etc/nginx/ssl/default.crt;
    ssl_certificate_key /etc/nginx/ssl/default.key;

    root /var/www/public;
    index index.php index.html index.htm;

    location / {
        try_files $uri /index.php$is_args$args;
    }

    location ~ ^/index\.php(/|$) {
        fastcgi_pass php-upstream;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
        internal;
    }

    location ~ \.php$ {
        return 404;
    }

    error_log /var/log/nginx/project_error.log;
    access_log /var/log/nginx/project_access.log;
}
```

## File: `docker/nginx/nginx.conf`
```
user www-data;
worker_processes 4;
pid /run/nginx.pid;

events {
  worker_connections  2048;
  multi_accept on;
  use epoll;
}

http {
  server_tokens off;
  sendfile on;
  tcp_nopush on;
  tcp_nodelay on;
  keepalive_timeout 15;
  types_hash_max_size 2048;
  client_max_body_size 20M;
  include /etc/nginx/mime.types;
  default_type application/octet-stream;
  access_log /dev/stdout;
  error_log /dev/stderr;
  gzip on;
  gzip_disable "msie6";

  ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
  ssl_ciphers 'ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDHE-ECDSA-DES-CBC3-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA:!DSS';

  include /etc/nginx/conf.d/*.conf;
  include /etc/nginx/sites-available/*.conf;
  open_file_cache off; # Disabled for issue 619
  charset UTF-8;
}
```

## File: `docker/php-fpm/Dockerfile`
```
FROM php:7.4-fpm

# Set Environment Variables
ENV DEBIAN_FRONTEND noninteractive

RUN set -eux; \
    apt-get update; \
    apt-get upgrade -y; \
    apt-get install -yqq apt-utils; \
    apt-get install -y --no-install-recommends \
            curl \
            libmemcached-dev \
            libz-dev \
            libpq-dev \
            libjpeg-dev \
            libpng-dev \
            libfreetype6-dev \
            libssl-dev \
            libmcrypt-dev \
            libonig-dev \
            libzip-dev zip unzip;

RUN set -eux; \
    docker-php-ext-install pdo_mysql; \
    docker-php-ext-configure gd \
            --prefix=/usr \
            --with-jpeg \
            --with-freetype; \
    docker-php-ext-install gd; \
    docker-php-ext-configure zip; \
    docker-php-ext-install zip; \
    php -r 'var_dump(gd_info());'


RUN set -xe; \
    pecl channel-update pecl.php.net

###########################################################################
# xDebug:
###########################################################################

ARG INSTALL_XDEBUG=true

RUN if [ ${INSTALL_XDEBUG} = true ]; then \
  pecl install xdebug; \
  docker-php-ext-enable xdebug \
;fi

# Copy xdebug configuration for remote debugging
COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini

###########################################################################
# bcmath:
###########################################################################

RUN docker-php-ext-install bcmath

###########################################################################
# LDAP:
###########################################################################

RUN apt-get install -y libldap2-dev && \
    docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \
    docker-php-ext-install ldap


COPY ./php7.4-dev.ini /usr/local/etc/php/php.ini

USER root

# Clean up
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm /var/log/lastlog /var/log/faillog

# Configure non-root user.
ARG PUID=1000
ENV PUID ${PUID}
ARG PGID=1000
ENV PGID ${PGID}

RUN groupmod -o -g ${PGID} www-data && \
    usermod -o -u ${PUID} -g www-data www-data

# Configure locale.
ARG LOCALE=POSIX
ENV LC_ALL ${LOCALE}

WORKDIR /var/www

CMD ["php-fpm"]

EXPOSE 9000




```

## File: `docker/php-fpm/php7.4-dev.ini`
```
[PHP]

;;;;;;;;;;;;;;;;;;;
; About php.ini   ;
;;;;;;;;;;;;;;;;;;;
; PHP's initialization file, generally called php.ini, is responsible for
; configuring many of the aspects of PHP's behavior.

; PHP attempts to find and load this configuration from a number of locations.
; The following is a summary of its search order:
; 1. SAPI module specific location.
; 2. The PHPRC environment variable. (As of PHP 5.2.0)
; 3. A number of predefined registry keys on Windows (As of PHP 5.2.0)
; 4. Current working directory (except CLI)
; 5. The web server's directory (for SAPI modules), or directory of PHP
; (otherwise in Windows)
; 6. The directory from the --with-config-file-path compile time option, or the
; Windows directory (C:\windows or C:\winnt)
; See the PHP docs for more specific information.
; http://php.net/configuration.file

; The syntax of the file is extremely simple.  Whitespace and lines
; beginning with a semicolon are silently ignored (as you probably guessed).
; Section headers (e.g. [Foo]) are also silently ignored, even though
; they might mean something in the future.

; Directives following the section heading [PATH=/www/mysite] only
; apply to PHP files in the /www/mysite directory.  Directives
; following the section heading [HOST=www.example.com] only apply to
; PHP files served from www.example.com.  Directives set in these
; special sections cannot be overridden by user-defined INI files or
; at runtime. Currently, [PATH=] and [HOST=] sections only work under
; CGI/FastCGI.
; http://php.net/ini.sections

; Directives are specified using the following syntax:
; directive = value
; Directive names are *case sensitive* - foo=bar is different from FOO=bar.
; Directives are variables used to configure PHP or PHP extensions.
; There is no name validation.  If PHP can't find an expected
; directive because it is not set or is mistyped, a default value will be used.

; The value can be a string, a number, a PHP constant (e.g. E_ALL or M_PI), one
; of the INI constants (On, Off, True, False, Yes, No and None) or an expression
; (e.g. E_ALL & ~E_NOTICE), a quoted string ("bar"), or a reference to a
; previously set variable or directive (e.g. ${foo})

; Expressions in the INI file are limited to bitwise operators and parentheses:
; |  bitwise OR
; ^  bitwise XOR
; &  bitwise AND
; ~  bitwise NOT
; !  boolean NOT

; Boolean flags can be turned on using the values 1, On, True or Yes.
; They can be turned off using the values 0, Off, False or No.

; An empty string can be denoted by simply not writing anything after the equal
; sign, or by using the None keyword:

;  foo =         ; sets foo to an empty string
;  foo = None    ; sets foo to an empty string
;  foo = "None"  ; sets foo to the string 'None'

; If you use constants in your value, and these constants belong to a
; dynamically loaded extension (either a PHP extension or a Zend extension),
; you may only use these constants *after* the line that loads the extension.

;;;;;;;;;;;;;;;;;;;
; About this file ;
;;;;;;;;;;;;;;;;;;;
; PHP comes packaged with two INI files. One that is recommended to be used
; in production environments and one that is recommended to be used in
; development environments.

; php.ini-production contains settings which hold security, performance and
; best practices at its core. But please be aware, these settings may break
; compatibility with older or less security conscience applications. We
; recommending using the production ini in production and testing environments.

; php.ini-development is very similar to its production variant, except it is
; much more verbose when it comes to errors. We recommend using the
; development version only in development environments, as errors shown to
; application users can inadvertently leak otherwise secure information.

; This is php.ini-production INI file.

;;;;;;;;;;;;;;;;;;;
; Quick Reference ;
;;;;;;;;;;;;;;;;;;;
; The following are all the settings which are different in either the production
; or development versions of the INIs with respect to PHP's default behavior.
; Please see the actual settings later in the document for more details as to why
; we recommend these changes in PHP's behavior.

; display_errors
;   Default Value: On
;   Development Value: On
;   Production Value: Off

; display_startup_errors
;   Default Value: Off
;   Development Value: On
;   Production Value: Off

; error_reporting
;   Default Value: E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED
;   Development Value: E_ALL
;   Production Value: E_ALL & ~E_DEPRECATED & ~E_STRICT

; html_errors
;   Default Value: On
;   Development Value: On
;   Production value: On

; log_errors
;   Default Value: Off
;   Development Value: On
;   Production Value: On

; max_input_time
;   Default Value: -1 (Unlimited)
;   Development Value: 60 (60 seconds)
;   Production Value: 60 (60 seconds)

; output_buffering
;   Default Value: Off
;   Development Value: 4096
;   Production Value: 4096

; register_argc_argv
;   Default Value: On
;   Development Value: Off
;   Production Value: Off

; request_order
;   Default Value: None
;   Development Value: "GP"
;   Production Value: "GP"

; session.gc_divisor
;   Default Value: 100
;   Development Value: 1000
;   Production Value: 1000

; session.sid_bits_per_character
;   Default Value: 4
;   Development Value: 5
;   Production Value: 5

; short_open_tag
;   Default Value: On
;   Development Value: Off
;   Production Value: Off

; track_errors
;   Default Value: Off
;   Development Value: On
;   Production Value: Off

; variables_order
;   Default Value: "EGPCS"
;   Development Value: "GPCS"
;   Production Value: "GPCS"

;;;;;;;;;;;;;;;;;;;;
; php.ini Options  ;
;;;;;;;;;;;;;;;;;;;;
; Name for user-defined php.ini (.htaccess) files. Default is ".user.ini"
;user_ini.filename = ".user.ini"

; To disable this feature set this option to empty value
;user_ini.filename =

; TTL for user-defined php.ini files (time-to-live) in seconds. Default is 300 seconds (5 minutes)
;user_ini.cache_ttl = 300

;;;;;;;;;;;;;;;;;;;;
; Language Options ;
;;;;;;;;;;;;;;;;;;;;

; Enable the PHP scripting language engine under Apache.
; http://php.net/engine
engine = On

; This directive determines whether or not PHP will recognize code between
; <? and ?> tags as PHP source which should be processed as such. It is
; generally recommended that <?php and ?> should be used and that this feature
; should be disabled, as enabling it may result in issues when generating XML
; documents, however this remains supported for backward compatibility reasons.
; Note that this directive does not control the <?= shorthand tag, which can be
; used regardless of this directive.
; Default Value: On
; Development Value: Off
; Production Value: Off
; http://php.net/short-open-tag
short_open_tag = Off

; The number of significant digits displayed in floating point numbers.
; http://php.net/precision
precision = 14

; Output buffering is a mechanism for controlling how much output data
; (excluding headers and cookies) PHP should keep internally before pushing that
; data to the client. If your application's output exceeds this setting, PHP
; will send that data in chunks of roughly the size you specify.
; Turning on this setting and managing its maximum buffer size can yield some
; interesting side-effects depending on your application and web server.
; You may be able to send headers and cookies after you've already sent output
; through print or echo. You also may see performance benefits if your server is
; emitting less packets due to buffered output versus PHP streaming the output
; as it gets it. On production servers, 4096 bytes is a good setting for performance
; reasons.
; Note: Output buffering can also be controlled via Output Buffering Control
;   functions.
; Possible Values:
;   On = Enabled and buffer is unlimited. (Use with caution)
;   Off = Disabled
;   Integer = Enables the buffer and sets its maximum size in bytes.
; Note: This directive is hardcoded to Off for the CLI SAPI
; Default Value: Off
; Development Value: 4096
; Production Value: 4096
; http://php.net/output-buffering
output_buffering = 4096

; You can redirect all of the output of your scripts to a function.  For
; example, if you set output_handler to "mb_output_handler", character
; encoding will be transparently converted to the specified encoding.
; Setting any output handler automatically turns on output buffering.
; Note: People who wrote portable scripts should not depend on this ini
;   directive. Instead, explicitly set the output handler using ob_start().
;   Using this ini directive may cause problems unless you know what script
;   is doing.
; Note: You cannot use both "mb_output_handler" with "ob_iconv_handler"
;   and you cannot use both "ob_gzhandler" and "zlib.output_compression".
; Note: output_handler must be empty if this is set 'On' !!!!
;   Instead you must use zlib.output_handler.
; http://php.net/output-handler
;output_handler =

; URL rewriter function rewrites URL on the fly by using
; output buffer. You can set target tags by this configuration.
; "form" tag is special tag. It will add hidden input tag to pass values.
; Refer to session.trans_sid_tags for usage.
; Default Value: "form="
; Development Value: "form="
; Production Value: "form="
;url_rewriter.tags

; URL rewriter will not rewrites absolute URL nor form by default. To enable
; absolute URL rewrite, allowed hosts must be defined at RUNTIME.
; Refer to session.trans_sid_hosts for more details.
; Default Value: ""
; Development Value: ""
; Production Value: ""
;url_rewriter.hosts

; Transparent output compression using the zlib library
; Valid values for this option are 'off', 'on', or a specific buffer size
; to be used for compression (default is 4KB)
; Note: Resulting chunk size may vary due to nature of compression. PHP
;   outputs chunks that are few hundreds bytes each as a result of
;   compression. If you prefer a larger chunk size for better
;   performance, enable output_buffering in addition.
; Note: You need to use zlib.output_handler instead of the standard
;   output_handler, or otherwise the output will be corrupted.
; http://php.net/zlib.output-compression
zlib.output_compression = Off

; http://php.net/zlib.output-compression-level
;zlib.output_compression_level = -1

; You cannot specify additional output handlers if zlib.output_compression
; is activated here. This setting does the same as output_handler but in
; a different order.
; http://php.net/zlib.output-handler
;zlib.output_handler =

; Implicit flush tells PHP to tell the output layer to flush itself
; automatically after every output block.  This is equivalent to calling the
; PHP function flush() after each and every call to print() or echo() and each
; and every HTML block.  Turning this option on has serious performance
; implications and is generally recommended for debugging purposes only.
; http://php.net/implicit-flush
; Note: This directive is hardcoded to On for the CLI SAPI
implicit_flush = Off

; The unserialize callback function will be called (with the undefined class'
; name as parameter), if the unserializer finds an undefined class
; which should be instantiated. A warning appears if the specified function is
; not defined, or if the function doesn't include/implement the missing class.
; So only set this entry, if you really want to implement such a
; callback-function.
unserialize_callback_func =

; When floats & doubles are serialized, store serialize_precision significant
; digits after the floating point. The default value ensures that when floats
; are decoded with unserialize, the data will remain the same.
; The value is also used for json_encode when encoding double values.
; If -1 is used, then dtoa mode 0 is used which automatically select the best
; precision.
serialize_precision = -1

; open_basedir, if set, limits all file operations to the defined directory
; and below.  This directive makes most sense if used in a per-directory
; or per-virtualhost web server configuration file.
; http://php.net/open-basedir
;open_basedir =

; This directive allows you to disable certain functions for security reasons.
; It receives a comma-delimited list of function names.
; http://php.net/disable-functions
disable_functions =

; This directive allows you to disable certain classes for security reasons.
; It receives a comma-delimited list of class names.
; http://php.net/disable-classes
disable_classes =

; Colors for Syntax Highlighting mode.  Anything that's acceptable in
; <span style="color: ???????"> would work.
; http://php.net/syntax-highlighting
;highlight.string  = #DD0000
;highlight.comment = #FF9900
;highlight.keyword = #007700
;highlight.default = #0000BB
;highlight.html    = #000000

; If enabled, the request will be allowed to complete even if the user aborts
; the request. Consider enabling it if executing long requests, which may end up
; being interrupted by the user or a browser timing out. PHP's default behavior
; is to disable this feature.
; http://php.net/ignore-user-abort
;ignore_user_abort = On

; Determines the size of the realpath cache to be used by PHP. This value should
; be increased on systems where PHP opens many files to reflect the quantity of
; the file operations performed.
; http://php.net/realpath-cache-size
;realpath_cache_size = 4096k

; Duration of time, in seconds for which to cache realpath information for a given
; file or directory. For systems with rarely changing files, consider increasing this
; value.
; http://php.net/realpath-cache-ttl
;realpath_cache_ttl = 120

; Enables or disables the circular reference collector.
; http://php.net/zend.enable-gc
zend.enable_gc = On

; If enabled, scripts may be written in encodings that are incompatible with
; the scanner.  CP936, Big5, CP949 and Shift_JIS are the examples of such
; encodings.  To use this feature, mbstring extension must be enabled.
; Default: Off
;zend.multibyte = Off

; Allows to set the default encoding for the scripts.  This value will be used
; unless "declare(encoding=...)" directive appears at the top of the script.
; Only affects if zend.multibyte is set.
; Default: ""
;zend.script_encoding =

;;;;;;;;;;;;;;;;;
; Miscellaneous ;
;;;;;;;;;;;;;;;;;

; Decides whether PHP may expose the fact that it is installed on the server
; (e.g. by adding its signature to the Web server header).  It is no security
; threat in any way, but it makes it possible to determine whether you use PHP
; on your server or not.
; http://php.net/expose-php
expose_php = On

;;;;;;;;;;;;;;;;;;;
; Resource Limits ;
;;;;;;;;;;;;;;;;;;;

; Maximum execution time of each script, in seconds
; http://php.net/max-execution-time
; Note: This directive is hardcoded to 0 for the CLI SAPI
max_execution_time = 600

; Maximum amount of time each script may spend parsing request data. It's a good
; idea to limit this time on productions servers in order to eliminate unexpectedly
; long running scripts.
; Note: This directive is hardcoded to -1 for the CLI SAPI
; Default Value: -1 (Unlimited)
; Development Value: 60 (60 seconds)
; Production Value: 60 (60 seconds)
; http://php.net/max-input-time
max_input_time = 120

; Maximum input variable nesting level
; http://php.net/max-input-nesting-level
;max_input_nesting_level = 64

; How many GET/POST/COOKIE input variables may be accepted
; max_input_vars = 1000

; Maximum amount of memory a script may consume (128MB)
; http://php.net/memory-limit
memory_limit = 256M

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Error handling and logging ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; This directive informs PHP of which errors, warnings and notices you would like
; it to take action for. The recommended way of setting values for this
; directive is through the use of the error level constants and bitwise
; operators. The error level constants are below here for convenience as well as
; some common settings and their meanings.
; By default, PHP is set to take action on all errors, notices and warnings EXCEPT
; those related to E_NOTICE and E_STRICT, which together cover best practices and
; recommended coding standards in PHP. For performance reasons, this is the
; recommend error reporting setting. Your production server shouldn't be wasting
; resources complaining about best practices and coding standards. That's what
; development servers and development settings are for.
; Note: The php.ini-development file has this setting as E_ALL. This
; means it pretty much reports everything which is exactly what you want during
; development and early testing.
;
; Error Level Constants:
; E_ALL             - All errors and warnings (includes E_STRICT as of PHP 5.4.0)
; E_ERROR           - fatal run-time errors
; E_RECOVERABLE_ERROR  - almost fatal run-time errors
; E_WARNING         - run-time warnings (non-fatal errors)
; E_PARSE           - compile-time parse errors
; E_NOTICE          - run-time notices (these are warnings which often result
;                     from a bug in your code, but it's possible that it was
;                     intentional (e.g., using an uninitialized variable and
;                     relying on the fact it is automatically initialized to an
;                     empty string)
; E_STRICT          - run-time notices, enable to have PHP suggest changes
;                     to your code which will ensure the best interoperability
;                     and forward compatibility of your code
; E_CORE_ERROR      - fatal errors that occur during PHP's initial startup
; E_CORE_WARNING    - warnings (non-fatal errors) that occur during PHP's
;                     initial startup
; E_COMPILE_ERROR   - fatal compile-time errors
; E_COMPILE_WARNING - compile-time warnings (non-fatal errors)
; E_USER_ERROR      - user-generated error message
; E_USER_WARNING    - user-generated warning message
; E_USER_NOTICE     - user-generated notice message
; E_DEPRECATED      - warn about code that will not work in future versions
;                     of PHP
; E_USER_DEPRECATED - user-generated deprecation warnings
;
; Common Values:
;   E_ALL (Show all errors, warnings and notices including coding standards.)
;   E_ALL & ~E_NOTICE  (Show all errors, except for notices)
;   E_ALL & ~E_NOTICE & ~E_STRICT  (Show all errors, except for notices and coding standards warnings.)
;   E_COMPILE_ERROR|E_RECOVERABLE_ERROR|E_ERROR|E_CORE_ERROR  (Show only errors)
; Default Value: E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED
; Development Value: E_ALL
; Production Value: E_ALL & ~E_DEPRECATED & ~E_STRICT
; http://php.net/error-reporting
error_reporting = E_ALL

; This directive controls whether or not and where PHP will output errors,
; notices and warnings too. Error output is very useful during development, but
; it could be very dangerous in production environments. Depending on the code
; which is triggering the error, sensitive information could potentially leak
; out of your application such as database usernames and passwords or worse.
; For production environments, we recommend logging errors rather than
; sending them to STDOUT.
; Possible Values:
;   Off = Do not display any errors
;   stderr = Display errors to STDERR (affects only CGI/CLI binaries!)
;   On or stdout = Display errors to STDOUT
; Default Value: On
; Development Value: On
; Production Value: Off
; http://php.net/display-errors
display_errors = On

; The display of errors which occur during PHP's startup sequence are handled
; separately from display_errors. PHP's default behavior is to suppress those
; errors from clients. Turning the display of startup errors on can be useful in
; debugging configuration problems. We strongly recommend you
; set this to 'off' for production servers.
; Default Value: Off
; Development Value: On
; Production Value: Off
; http://php.net/display-startup-errors
display_startup_errors = On

; Besides displaying errors, PHP can also log errors to locations such as a
; server-specific log, STDERR, or a location specified by the error_log
; directive found below. While errors should not be displayed on productions
; servers they should still be monitored and logging is a great way to do that.
; Default Value: Off
; Development Value: On
; Production Value: On
; http://php.net/log-errors
log_errors = On

; Set maximum length of log_errors. In error_log information about the source is
; added. The default is 1024 and 0 allows to not apply any maximum length at all.
; http://php.net/log-errors-max-len
log_errors_max_len = 1024

; Do not log repeated messages. Repeated errors must occur in same file on same
; line unless ignore_repeated_source is set true.
; http://php.net/ignore-repeated-errors
ignore_repeated_errors = Off

; Ignore source of message when ignoring repeated messages. When this setting
; is On you will not log errors with repeated messages from different files or
; source lines.
; http://php.net/ignore-repeated-source
ignore_repeated_source = Off

; If this parameter is set to Off, then memory leaks will not be shown (on
; stdout or in the log). This has only effect in a debug compile, and if
; error reporting includes E_WARNING in the allowed list
; http://php.net/report-memleaks
report_memleaks = On

; This setting is on by default.
;report_zend_debug = 0

; Store the last error/warning message in $php_errormsg (boolean). Setting this value
; to On can assist in debugging and is appropriate for development servers. It should
; however be disabled on production servers.
; Default Value: Off
; Development Value: On
; Production Value: Off
; http://php.net/track-errors
track_errors = Off

; Turn off normal error reporting and emit XML-RPC error XML
; http://php.net/xmlrpc-errors
;xmlrpc_errors = 0

; An XML-RPC faultCode
;xmlrpc_error_number = 0

; When PHP displays or logs an error, it has the capability of formatting the
; error message as HTML for easier reading. This directive controls whether
; the error message is formatted as HTML or not.
; Note: This directive is hardcoded to Off for the CLI SAPI
; Default Value: On
; Development Value: On
; Production value: On
; http://php.net/html-errors
html_errors = On

; If html_errors is set to On *and* docref_root is not empty, then PHP
; produces clickable error messages that direct to a page describing the error
; or function causing the error in detail.
; You can download a copy of the PHP manual from http://php.net/docs
; and change docref_root to the base URL of your local copy including the
; leading '/'. You must also specify the file extension being used including
; the dot. PHP's default behavior is to leave these settings empty, in which
; case no links to documentation are generated.
; Note: Never use this feature for production boxes.
; http://php.net/docref-root
; Examples
;docref_root = "/phpmanual/"

; http://php.net/docref-ext
;docref_ext = .html

; String to output before an error message. PHP's default behavior is to leave
; this setting blank.
; http://php.net/error-prepend-string
; Example:
;error_prepend_string = "<span style='color: #ff0000'>"

; String to output after an error message. PHP's default behavior is to leave
; this setting blank.
; http://php.net/error-append-string
; Example:
;error_append_string = "</span>"

; Log errors to specified file. PHP's default behavior is to leave this value
; empty.
; http://php.net/error-log
; Example:
;error_log = php_errors.log
; Log errors to syslog (Event Log on Windows).
;error_log = syslog

;windows.show_crt_warning
; Default value: 0
; Development value: 0
; Production value: 0

;;;;;;;;;;;;;;;;;
; Data Handling ;
;;;;;;;;;;;;;;;;;

; The separator used in PHP generated URLs to separate arguments.
; PHP's default setting is "&".
; http://php.net/arg-separator.output
; Example:
;arg_separator.output = "&amp;"

; List of separator(s) used by PHP to parse input URLs into variables.
; PHP's default setting is "&".
; NOTE: Every character in this directive is considered as separator!
; http://php.net/arg-separator.input
; Example:
;arg_separator.input = ";&"

; This directive determines which super global arrays are registered when PHP
; starts up. G,P,C,E & S are abbreviations for the following respective super
; globals: GET, POST, COOKIE, ENV and SERVER. There is a performance penalty
; paid for the registration of these arrays and because ENV is not as commonly
; used as the others, ENV is not recommended on productions servers. You
; can still get access to the environment variables through getenv() should you
; need to.
; Default Value: "EGPCS"
; Development Value: "GPCS"
; Production Value: "GPCS";
; http://php.net/variables-order
variables_order = "GPCS"

; This directive determines which super global data (G,P & C) should be
; registered into the super global array REQUEST. If so, it also determines
; the order in which that data is registered. The values for this directive
; are specified in the same manner as the variables_order directive,
; EXCEPT one. Leaving this value empty will cause PHP to use the value set
; in the variables_order directive. It does not mean it will leave the super
; globals array REQUEST empty.
; Default Value: None
; Development Value: "GP"
; Production Value: "GP"
; http://php.net/request-order
request_order = "GP"

; This directive determines whether PHP registers $argv & $argc each time it
; runs. $argv contains an array of all the arguments passed to PHP when a script
; is invoked. $argc contains an integer representing the number of arguments
; that were passed when the script was invoked. These arrays are extremely
; useful when running scripts from the command line. When this directive is
; enabled, registering these variables consumes CPU cycles and memory each time
; a script is executed. For performance reasons, this feature should be disabled
; on production servers.
; Note: This directive is hardcoded to On for the CLI SAPI
; Default Value: On
; Development Value: Off
; Production Value: Off
; http://php.net/register-argc-argv
register_argc_argv = Off

; When enabled, the ENV, REQUEST and SERVER variables are created when they're
; first used (Just In Time) instead of when the script starts. If these
; variables are not used within a script, having this directive on will result
; in a performance gain. The PHP directive register_argc_argv must be disabled
; for this directive to have any affect.
; http://php.net/auto-globals-jit
auto_globals_jit = On

; Whether PHP will read the POST data.
; This option is enabled by default.
; Most likely, you won't want to disable this option globally. It causes $_POST
; and $_FILES to always be empty; the only way you will be able to read the
; POST data will be through the php://input stream wrapper. This can be useful
; to proxy requests or to process the POST data in a memory efficient fashion.
; http://php.net/enable-post-data-reading
;enable_post_data_reading = Off

; Maximum size of POST data that PHP will accept.
; Its value may be 0 to disable the limit. It is ignored if POST data reading
; is disabled through enable_post_data_reading.
; http://php.net/post-max-size
post_max_size = 8M

; Automatically add files before PHP document.
; http://php.net/auto-prepend-file
auto_prepend_file =

; Automatically add files after PHP document.
; http://php.net/auto-append-file
auto_append_file =

; By default, PHP will output a media type using the Content-Type header. To
; disable this, simply set it to be empty.
;
; PHP's built-in default media type is set to text/html.
; http://php.net/default-mimetype
default_mimetype = "text/html"

; PHP's default character set is set to UTF-8.
; http://php.net/default-charset
default_charset = "UTF-8"

; PHP internal character encoding is set to empty.
; If empty, default_charset is used.
; http://php.net/internal-encoding
;internal_encoding =

; PHP input character encoding is set to empty.
; If empty, default_charset is used.
; http://php.net/input-encoding
;input_encoding =

; PHP output character encoding is set to empty.
; If empty, default_charset is used.
; See also output_buffer.
; http://php.net/output-encoding
;output_encoding =

;;;;;;;;;;;;;;;;;;;;;;;;;
; Paths and Directories ;
;;;;;;;;;;;;;;;;;;;;;;;;;

; UNIX: "/path1:/path2"
;include_path = ".:/php/includes"
;
; Windows: "\path1;\path2"
;include_path = ".;c:\php\includes"
;
; PHP's default setting for include_path is ".;/path/to/php/pear"
; http://php.net/include-path

; The root of the PHP pages, used only if nonempty.
; if PHP was not compiled with FORCE_REDIRECT, you SHOULD set doc_root
; if you are running php as a CGI under any web server (other than IIS)
; see documentation for security issues.  The alternate is to use the
; cgi.force_redirect configuration below
; http://php.net/doc-root
doc_root =

; The directory under which PHP opens the script using /~username used only
; if nonempty.
; http://php.net/user-dir
user_dir =

; Directory in which the loadable extensions (modules) reside.
; http://php.net/extension-dir
; extension_dir = "./"
; On windows:
; extension_dir = "ext"

; Directory where the temporary files should be placed.
; Defaults to the system default (see sys_get_temp_dir)
; sys_temp_dir = "/tmp"

; Whether or not to enable the dl() function.  The dl() function does NOT work
; properly in multithreaded servers, such as IIS or Zeus, and is automatically
; disabled on them.
; http://php.net/enable-dl
enable_dl = Off

; cgi.force_redirect is necessary to provide security running PHP as a CGI under
; most web servers.  Left undefined, PHP turns this on by default.  You can
; turn it off here AT YOUR OWN RISK
; **You CAN safely turn this off for IIS, in fact, you MUST.**
; http://php.net/cgi.force-redirect
;cgi.force_redirect = 1

; if cgi.nph is enabled it will force cgi to always sent Status: 200 with
; every request. PHP's default behavior is to disable this feature.
;cgi.nph = 1

; if cgi.force_redirect is turned on, and you are not running under Apache or Netscape
; (iPlanet) web servers, you MAY need to set an environment variable name that PHP
; will look for to know it is OK to continue execution.  Setting this variable MAY
; cause security issues, KNOW WHAT YOU ARE DOING FIRST.
; http://php.net/cgi.redirect-status-env
;cgi.redirect_status_env =

; cgi.fix_pathinfo provides *real* PATH_INFO/PATH_TRANSLATED support for CGI.  PHP's
; previous behaviour was to set PATH_TRANSLATED to SCRIPT_FILENAME, and to not grok
; what PATH_INFO is.  For more information on PATH_INFO, see the cgi specs.  Setting
; this to 1 will cause PHP CGI to fix its paths to conform to the spec.  A setting
; of zero causes PHP to behave as before.  Default is 1.  You should fix your scripts
; to use SCRIPT_FILENAME rather than PATH_TRANSLATED.
; http://php.net/cgi.fix-pathinfo
;cgi.fix_pathinfo=1

; if cgi.discard_path is enabled, the PHP CGI binary can safely be placed outside
; of the web tree and people will not be able to circumvent .htaccess security.
; http://php.net/cgi.dicard-path
;cgi.discard_path=1

; FastCGI under IIS (on WINNT based OS) supports the ability to impersonate
; security tokens of the calling client.  This allows IIS to define the
; security context that the request runs under.  mod_fastcgi under Apache
; does not currently support this feature (03/17/2002)
; Set to 1 if running under IIS.  Default is zero.
; http://php.net/fastcgi.impersonate
;fastcgi.impersonate = 1

; Disable logging through FastCGI connection. PHP's default behavior is to enable
; this feature.
;fastcgi.logging = 0

; cgi.rfc2616_headers configuration option tells PHP what type of headers to
; use when sending HTTP response code. If set to 0, PHP sends Status: header that
; is supported by Apache. When this option is set to 1, PHP will send
; RFC2616 compliant header.
; Default is zero.
; http://php.net/cgi.rfc2616-headers
;cgi.rfc2616_headers = 0

; cgi.check_shebang_line controls whether CGI PHP checks for line starting with #!
; (shebang) at the top of the running script. This line might be needed if the
; script support running both as stand-alone script and via PHP CGI<. PHP in CGI
; mode skips this line and ignores its content if this directive is turned on.
; http://php.net/cgi.check-shebang-line
;cgi.check_shebang_line=1

;;;;;;;;;;;;;;;;
; File Uploads ;
;;;;;;;;;;;;;;;;

; Whether to allow HTTP file uploads.
; http://php.net/file-uploads
file_uploads = On

; Temporary directory for HTTP uploaded files (will use system default if not
; specified).
; http://php.net/upload-tmp-dir
;upload_tmp_dir =

; Maximum allowed size for uploaded files.
; http://php.net/upload-max-filesize
upload_max_filesize = 20M

; Maximum number of files that can be uploaded via a single request
max_file_uploads = 20

;;;;;;;;;;;;;;;;;;
; Fopen wrappers ;
;;;;;;;;;;;;;;;;;;

; Whether to allow the treatment of URLs (like http:// or ftp://) as files.
; http://php.net/allow-url-fopen
allow_url_fopen = On

; Whether to allow include/require to open URLs (like http:// or ftp://) as files.
; http://php.net/allow-url-include
allow_url_include = Off

; Define the anonymous ftp password (your email address). PHP's default setting
; for this is empty.
; http://php.net/from
;from="john@doe.com"

; Define the User-Agent string. PHP's default setting for this is empty.
; http://php.net/user-agent
;user_agent="PHP"

; Default timeout for socket based streams (seconds)
; http://php.net/default-socket-timeout
default_socket_timeout = 60

; If your scripts have to deal with files from Macintosh systems,
; or you are running on a Mac and need to deal with files from
; unix or win32 systems, setting this flag will cause PHP to
; automatically detect the EOL character in those files so that
; fgets() and file() will work regardless of the source of the file.
; http://php.net/auto-detect-line-endings
;auto_detect_line_endings = Off

;;;;;;;;;;;;;;;;;;;;;;
; Dynamic Extensions ;
;;;;;;;;;;;;;;;;;;;;;;

; If you wish to have an extension loaded automatically, use the following
; syntax:
;
;   extension=modulename.extension
;
; For example, on Windows:
;
;   extension=mysqli.dll
;
; ... or under UNIX:
;
;   extension=mysqli.so
;
; ... or with a path:
;
;   extension=/path/to/extension/mysqli.so
;
; If you only provide the name of the extension, PHP will look for it in its
; default extension directory.
;
; Windows Extensions
; Note that ODBC support is built in, so no dll is needed for it.
; Note that many DLL files are located in the extensions/ (PHP 4) ext/ (PHP 5+)
; extension folders as well as the separate PECL DLL download (PHP 5+).
; Be sure to appropriately set the extension_dir directive.
;
;extension=php_bz2.dll
;extension=php_curl.dll
;extension=php_fileinfo.dll
;extension=php_ftp.dll
;extension=php_gd2.dll
;extension=php_gettext.dll
;extension=php_gmp.dll
;extension=php_intl.dll
;extension=php_imap.dll
;extension=php_interbase.dll
;extension=php_ldap.dll
;extension=php_mbstring.dll
;extension=php_exif.dll      ; Must be after mbstring as it depends on it
;extension=php_mysqli.dll
;extension=php_oci8_12c.dll  ; Use with Oracle Database 12c Instant Client
;extension=php_openssl.dll
;extension=php_pdo_firebird.dll
;extension=php_pdo_mysql.dll
;extension=php_pdo_oci.dll
;extension=php_pdo_odbc.dll
;extension=php_pdo_pgsql.dll
;extension=php_pdo_sqlite.dll
;extension=php_pgsql.dll
;extension=php_shmop.dll

; The MIBS data available in the PHP distribution must be installed.
; See http://www.php.net/manual/en/snmp.installation.php
;extension=php_snmp.dll

;extension=php_soap.dll
;extension=php_sockets.dll
;extension=php_sqlite3.dll
;extension=php_tidy.dll
;extension=php_xmlrpc.dll
;extension=php_xsl.dll

;;;;;;;;;;;;;;;;;;;
; Module Settings ;
;;;;;;;;;;;;;;;;;;;

[CLI Server]
; Whether the CLI web server uses ANSI color coding in its terminal output.
cli_server.color = On

[Date]
; Defines the default timezone used by the date functions
; http://php.net/date.timezone
;date.timezone =

; http://php.net/date.default-latitude
;date.default_latitude = 31.7667

; http://php.net/date.default-longitude
;date.default_longitude = 35.2333

; http://php.net/date.sunrise-zenith
;date.sunrise_zenith = 90.583333

; http://php.net/date.sunset-zenith
;date.sunset_zenith = 90.583333

[filter]
; http://php.net/filter.default
;filter.default = unsafe_raw

; http://php.net/filter.default-flags
;filter.default_flags =

[iconv]
; Use of this INI entry is deprecated, use global input_encoding instead.
; If empty, default_charset or input_encoding or iconv.input_encoding is used.
; The precedence is: default_charset < intput_encoding < iconv.input_encoding
;iconv.input_encoding =

; Use of this INI entry is deprecated, use global internal_encoding instead.
; If empty, default_charset or internal_encoding or iconv.internal_encoding is used.
; The precedence is: default_charset < internal_encoding < iconv.internal_encoding
;iconv.internal_encoding =

; Use of this INI entry is deprecated, use global output_encoding instead.
; If empty, default_charset or output_encoding or iconv.output_encoding is used.
; The precedence is: default_charset < output_encoding < iconv.output_encoding
; To use an output encoding conversion, iconv's output handler must be set
; otherwise output encoding conversion cannot be performed.
;iconv.output_encoding =

[intl]
;intl.default_locale =
; This directive allows you to produce PHP errors when some error
; happens within intl functions. The value is the level of the error produced.
; Default is 0, which does not produce any errors.
;intl.error_level = E_WARNING
;intl.use_exceptions = 0

[sqlite3]
;sqlite3.extension_dir =

[Pcre]
;PCRE library backtracking limit.
; http://php.net/pcre.backtrack-limit
;pcre.backtrack_limit=100000

;PCRE library recursion limit.
;Please note that if you set this value to a high number you may consume all
;the available process stack and eventually crash PHP (due to reaching the
;stack size limit imposed by the Operating System).
; http://php.net/pcre.recursion-limit
;pcre.recursion_limit=100000

;Enables or disables JIT compilation of patterns. This requires the PCRE
;library to be compiled with JIT support.
;pcre.jit=1

[Pdo]
; Whether to pool ODBC connections. Can be one of "strict", "relaxed" or "off"
; http://php.net/pdo-odbc.connection-pooling
;pdo_odbc.connection_pooling=strict

;pdo_odbc.db2_instance_name

[Pdo_mysql]
; If mysqlnd is used: Number of cache slots for the internal result set cache
; http://php.net/pdo_mysql.cache_size
pdo_mysql.cache_size = 2000

; Default socket name for local MySQL connects.  If empty, uses the built-in
; MySQL defaults.
; http://php.net/pdo_mysql.default-socket
pdo_mysql.default_socket=

[Phar]
; http://php.net/phar.readonly
;phar.readonly = On

; http://php.net/phar.require-hash
;phar.require_hash = On

;phar.cache_list =

[mail function]
; For Win32 only.
; http://php.net/smtp
SMTP = localhost
; http://php.net/smtp-port
smtp_port = 25

; For Win32 only.
; http://php.net/sendmail-from
;sendmail_from = me@example.com

; For Unix only.  You may supply arguments as well (default: "sendmail -t -i").
; http://php.net/sendmail-path
;sendmail_path =

; Force the addition of the specified parameters to be passed as extra parameters
; to the sendmail binary. These parameters will always replace the value of
; the 5th parameter to mail().
;mail.force_extra_parameters =

; Add X-PHP-Originating-Script: that will include uid of the script followed by the filename
mail.add_x_header = On

; The path to a log file that will log all mail() calls. Log entries include
; the full path of the script, line number, To address and headers.
;mail.log =
; Log mail to syslog (Event Log on Windows).
;mail.log = syslog

[ODBC]
; http://php.net/odbc.default-db
;odbc.default_db    =  Not yet implemented

; http://php.net/odbc.default-user
;odbc.default_user  =  Not yet implemented

; http://php.net/odbc.default-pw
;odbc.default_pw    =  Not yet implemented

; Controls the ODBC cursor model.
; Default: SQL_CURSOR_STATIC (default).
;odbc.default_cursortype

; Allow or prevent persistent links.
; http://php.net/odbc.allow-persistent
odbc.allow_persistent = On

; Check that a connection is still valid before reuse.
; http://php.net/odbc.check-persistent
odbc.check_persistent = On

; Maximum number of persistent links.  -1 means no limit.
; http://php.net/odbc.max-persistent
odbc.max_persistent = -1

; Maximum number of links (persistent + non-persistent).  -1 means no limit.
; http://php.net/odbc.max-links
odbc.max_links = -1

; Handling of LONG fields.  Returns number of bytes to variables.  0 means
; passthru.
; http://php.net/odbc.defaultlrl
odbc.defaultlrl = 4096

; Handling of binary data.  0 means passthru, 1 return as is, 2 convert to char.
; See the documentation on odbc_binmode and odbc_longreadlen for an explanation
; of odbc.defaultlrl and odbc.defaultbinmode
; http://php.net/odbc.defaultbinmode
odbc.defaultbinmode = 1

;birdstep.max_links = -1

[Interbase]
; Allow or prevent persistent links.
ibase.allow_persistent = 1

; Maximum number of persistent links.  -1 means no limit.
ibase.max_persistent = -1

; Maximum number of links (persistent + non-persistent).  -1 means no limit.
ibase.max_links = -1

; Default database name for ibase_connect().
;ibase.default_db =

; Default username for ibase_connect().
;ibase.default_user =

; Default password for ibase_connect().
;ibase.default_password =

; Default charset for ibase_connect().
;ibase.default_charset =

; Default timestamp format.
ibase.timestampformat = "%Y-%m-%d %H:%M:%S"

; Default date format.
ibase.dateformat = "%Y-%m-%d"

; Default time format.
ibase.timeformat = "%H:%M:%S"

[MySQLi]

; Maximum number of persistent links.  -1 means no limit.
; http://php.net/mysqli.max-persistent
mysqli.max_persistent = -1

; Allow accessing, from PHP's perspective, local files with LOAD DATA statements
; http://php.net/mysqli.allow_local_infile
;mysqli.allow_local_infile = On

; Allow or prevent persistent links.
; http://php.net/mysqli.allow-persistent
mysqli.allow_persistent = On

; Maximum number of links.  -1 means no limit.
; http://php.net/mysqli.max-links
mysqli.max_links = -1

; If mysqlnd is used: Number of cache slots for the internal result set cache
; http://php.net/mysqli.cache_size
mysqli.cache_size = 2000

; Default port number for mysqli_connect().  If unset, mysqli_connect() will use
; the $MYSQL_TCP_PORT or the mysql-tcp entry in /etc/services or the
; compile-time value defined MYSQL_PORT (in that order).  Win32 will only look
; at MYSQL_PORT.
; http://php.net/mysqli.default-port
mysqli.default_port = 3306

; Default socket name for local MySQL connects.  If empty, uses the built-in
; MySQL defaults.
; http://php.net/mysqli.default-socket
mysqli.default_socket =

; Default host for mysql_connect() (doesn't apply in safe mode).
; http://php.net/mysqli.default-host
mysqli.default_host =

; Default user for mysql_connect() (doesn't apply in safe mode).
; http://php.net/mysqli.default-user
mysqli.default_user =

; Default password for mysqli_connect() (doesn't apply in safe mode).
; Note that this is generally a *bad* idea to store passwords in this file.
; *Any* user with PHP access can run 'echo get_cfg_var("mysqli.default_pw")
; and reveal this password!  And of course, any users with read access to this
; file will be able to reveal the password as well.
; http://php.net/mysqli.default-pw
mysqli.default_pw =

; Allow or prevent reconnect
mysqli.reconnect = Off

[mysqlnd]
; Enable / Disable collection of general statistics by mysqlnd which can be
; used to tune and monitor MySQL operations.
; http://php.net/mysqlnd.collect_statistics
mysqlnd.collect_statistics = On

; Enable / Disable collection of memory usage statistics by mysqlnd which can be
; used to tune and monitor MySQL operations.
; http://php.net/mysqlnd.collect_memory_statistics
mysqlnd.collect_memory_statistics = Off

; Records communication from all extensions using mysqlnd to the specified log
; file.
; http://php.net/mysqlnd.debug
;mysqlnd.debug =

; Defines which queries will be logged.
; http://php.net/mysqlnd.log_mask
;mysqlnd.log_mask = 0

; Default size of the mysqlnd memory pool, which is used by result sets.
; http://php.net/mysqlnd.mempool_default_size
;mysqlnd.mempool_default_size = 16000

; Size of a pre-allocated buffer used when sending commands to MySQL in bytes.
; http://php.net/mysqlnd.net_cmd_buffer_size
;mysqlnd.net_cmd_buffer_size = 2048

; Size of a pre-allocated buffer used for reading data sent by the server in
; bytes.
; http://php.net/mysqlnd.net_read_buffer_size
;mysqlnd.net_read_buffer_size = 32768

; Timeout for network requests in seconds.
; http://php.net/mysqlnd.net_read_timeout
;mysqlnd.net_read_timeout = 31536000

; SHA-256 Authentication Plugin related. File with the MySQL server public RSA
; key.
; http://php.net/mysqlnd.sha256_server_public_key
;mysqlnd.sha256_server_public_key =

[OCI8]

; Connection: Enables privileged connections using external
; credentials (OCI_SYSOPER, OCI_SYSDBA)
; http://php.net/oci8.privileged-connect
;oci8.privileged_connect = Off

; Connection: The maximum number of persistent OCI8 connections per
; process. Using -1 means no limit.
; http://php.net/oci8.max-persistent
;oci8.max_persistent = -1

; Connection: The maximum number of seconds a process is allowed to
; maintain an idle persistent connection. Using -1 means idle
; persistent connections will be maintained forever.
; http://php.net/oci8.persistent-timeout
;oci8.persistent_timeout = -1

; Connection: The number of seconds that must pass before issuing a
; ping during oci_pconnect() to check the connection validity. When
; set to 0, each oci_pconnect() will cause a ping. Using -1 disables
; pings completely.
; http://php.net/oci8.ping-interval
;oci8.ping_interval = 60

; Connection: Set this to a user chosen connection class to be used
; for all pooled server requests with Oracle 11g Database Resident
; Connection Pooling (DRCP).  To use DRCP, this value should be set to
; the same string for all web servers running the same application,
; the database pool must be configured, and the connection string must
; specify to use a pooled server.
;oci8.connection_class =

; High Availability: Using On lets PHP receive Fast Application
; Notification (FAN) events generated when a database node fails. The
; database must also be configured to post FAN events.
;oci8.events = Off

; Tuning: This option enables statement caching, and specifies how
; many statements to cache. Using 0 disables statement caching.
; http://php.net/oci8.statement-cache-size
;oci8.statement_cache_size = 20

; Tuning: Enables statement prefetching and sets the default number of
; rows that will be fetched automatically after statement execution.
; http://php.net/oci8.default-prefetch
;oci8.default_prefetch = 100

; Compatibility. Using On means oci_close() will not close
; oci_connect() and oci_new_connect() connections.
; http://php.net/oci8.old-oci-close-semantics
;oci8.old_oci_close_semantics = Off

[PostgreSQL]
; Allow or prevent persistent links.
; http://php.net/pgsql.allow-persistent
pgsql.allow_persistent = On

; Detect broken persistent links always with pg_pconnect().
; Auto reset feature requires a little overheads.
; http://php.net/pgsql.auto-reset-persistent
pgsql.auto_reset_persistent = Off

; Maximum number of persistent links.  -1 means no limit.
; http://php.net/pgsql.max-persistent
pgsql.max_persistent = -1

; Maximum number of links (persistent+non persistent).  -1 means no limit.
; http://php.net/pgsql.max-links
pgsql.max_links = -1

; Ignore PostgreSQL backends Notice message or not.
; Notice message logging require a little overheads.
; http://php.net/pgsql.ignore-notice
pgsql.ignore_notice = 0

; Log PostgreSQL backends Notice message or not.
; Unless pgsql.ignore_notice=0, module cannot log notice message.
; http://php.net/pgsql.log-notice
pgsql.log_notice = 0

[bcmath]
; Number of decimal digits for all bcmath functions.
; http://php.net/bcmath.scale
bcmath.scale = 0

[browscap]
; http://php.net/browscap
;browscap = extra/browscap.ini

[Session]
; Handler used to store/retrieve data.
; http://php.net/session.save-handler
session.save_handler = files

; Argument passed to save_handler.  In the case of files, this is the path
; where data files are stored. Note: Windows users have to change this
; variable in order to use PHP's session functions.
;
; The path can be defined as:
;
;     session.save_path = "N;/path"
;
; where N is an integer.  Instead of storing all the session files in
; /path, what this will do is use subdirectories N-levels deep, and
; store the session data in those directories.  This is useful if
; your OS has problems with many files in one directory, and is
; a more efficient layout for servers that handle many sessions.
;
; NOTE 1: PHP will not create this directory structure automatically.
;         You can use the script in the ext/session dir for that purpose.
; NOTE 2: See the section on garbage collection below if you choose to
;         use subdirectories for session storage
;
; The file storage module creates files using mode 600 by default.
; You can change that by using
;
;     session.save_path = "N;MODE;/path"
;
; where MODE is the octal representation of the mode. Note that this
; does not overwrite the process's umask.
; http://php.net/session.save-path
session.save_path = "/tmp"

; Whether to use strict session mode.
; Strict session mode does not accept uninitialized session ID and regenerate
; session ID if browser sends uninitialized session ID. Strict mode protects
; applications from session fixation via session adoption vulnerability. It is
; disabled by default for maximum compatibility, but enabling it is encouraged.
; https://wiki.php.net/rfc/strict_sessions
session.use_strict_mode = 0

; Whether to use cookies.
; http://php.net/session.use-cookies
session.use_cookies = 1

; http://php.net/session.cookie-secure
;session.cookie_secure =

; This option forces PHP to fetch and use a cookie for storing and maintaining
; the session id. We encourage this operation as it's very helpful in combating
; session hijacking when not specifying and managing your own session id. It is
; not the be-all and end-all of session hijacking defense, but it's a good start.
; http://php.net/session.use-only-cookies
session.use_only_cookies = 1

; Name of the session (used as cookie name).
; http://php.net/session.name
session.name = PHPSESSID

; Initialize session on request startup.
; http://php.net/session.auto-start
session.auto_start = 0

; Lifetime in seconds of cookie or, if 0, until browser is restarted.
; http://php.net/session.cookie-lifetime
session.cookie_lifetime = 0

; The path for which the cookie is valid.
; http://php.net/session.cookie-path
session.cookie_path = /

; The domain for which the cookie is valid.
; http://php.net/session.cookie-domain
session.cookie_domain =

; Whether or not to add the httpOnly flag to the cookie, which makes it inaccessible to browser scripting languages such as JavaScript.
; http://php.net/session.cookie-httponly
session.cookie_httponly =

; Handler used to serialize data.  php is the standard serializer of PHP.
; http://php.net/session.serialize-handler
session.serialize_handler = php

; Defines the probability that the 'garbage collection' process is started
; on every session initialization. The probability is calculated by using
; gc_probability/gc_divisor. Where session.gc_probability is the numerator
; and gc_divisor is the denominator in the equation. Setting this value to 1
; when the session.gc_divisor value is 100 will give you approximately a 1% chance
; the gc will run on any give request.
; Default Value: 1
; Development Value: 1
; Production Value: 1
; http://php.net/session.gc-probability
session.gc_probability = 1

; Defines the probability that the 'garbage collection' process is started on every
; session initialization. The probability is calculated by using the following equation:
; gc_probability/gc_divisor. Where session.gc_probability is the numerator and
; session.gc_divisor is the denominator in the equation. Setting this value to 1
; when the session.gc_divisor value is 100 will give you approximately a 1% chance
; the gc will run on any give request. Increasing this value to 1000 will give you
; a 0.1% chance the gc will run on any give request. For high volume production servers,
; this is a more efficient approach.
; Default Value: 100
; Development Value: 1000
; Production Value: 1000
; http://php.net/session.gc-divisor
session.gc_divisor = 1000

; After this number of seconds, stored data will be seen as 'garbage' and
; cleaned up by the garbage collection process.
; http://php.net/session.gc-maxlifetime
session.gc_maxlifetime = 1440

; NOTE: If you are using the subdirectory option for storing session files
;       (see session.save_path above), then garbage collection does *not*
;       happen automatically.  You will need to do your own garbage
;       collection through a shell script, cron entry, or some other method.
;       For example, the following script would is the equivalent of
;       setting session.gc_maxlifetime to 1440 (1440 seconds = 24 minutes):
;          find /path/to/sessions -cmin +24 -type f | xargs rm

; Check HTTP Referer to invalidate externally stored URLs containing ids.
; HTTP_REFERER has to contain this substring for the session to be
; considered as valid.
; http://php.net/session.referer-check
session.referer_check =

; Set to {nocache,private,public,} to determine HTTP caching aspects
; or leave this empty to avoid sending anti-caching headers.
; http://php.net/session.cache-limiter
session.cache_limiter = nocache

; Document expires after n minutes.
; http://php.net/session.cache-expire
session.cache_expire = 180

; trans sid support is disabled by default.
; Use of trans sid may risk your users' security.
; Use this option with caution.
; - User may send URL contains active session ID
;   to other person via. email/irc/etc.
; - URL that contains active session ID may be stored
;   in publicly accessible computer.
; - User may access your site with the same session ID
;   always using URL stored in browser's history or bookmarks.
; http://php.net/session.use-trans-sid
session.use_trans_sid = 0

; Set session ID character length. This value could be between 22 to 256.
; Shorter length than default is supported only for compatibility reason.
; Users should use 32 or more chars.
; http://php.net/session.sid-length
; Default Value: 32
; Development Value: 26
; Production Value: 26
session.sid_length = 26

; The URL rewriter will look for URLs in a defined set of HTML tags.
; <form> is special; if you include them here, the rewriter will
; add a hidden <input> field with the info which is otherwise appended
; to URLs. <form> tag's action attribute URL will not be modified
; unless it is specified.
; Note that all valid entries require a "=", even if no value follows.
; Default Value: "a=href,area=href,frame=src,form="
; Development Value: "a=href,area=href,frame=src,form="
; Production Value: "a=href,area=href,frame=src,form="
; http://php.net/url-rewriter.tags
session.trans_sid_tags = "a=href,area=href,frame=src,form="

; URL rewriter does not rewrite absolute URLs by default.
; To enable rewrites for absolute pathes, target hosts must be specified
; at RUNTIME. i.e. use ini_set()
; <form> tags is special. PHP will check action attribute's URL regardless
; of session.trans_sid_tags setting.
; If no host is defined, HTTP_HOST will be used for allowed host.
; Example value: php.net,www.php.net,wiki.php.net
; Use "," for multiple hosts. No spaces are allowed.
; Default Value: ""
; Development Value: ""
; Production Value: ""
;session.trans_sid_hosts=""

; Define how many bits are stored in each character when converting
; the binary hash data to something readable.
; Possible values:
;   4  (4 bits: 0-9, a-f)
;   5  (5 bits: 0-9, a-v)
;   6  (6 bits: 0-9, a-z, A-Z, "-", ",")
; Default Value: 4
; Development Value: 5
; Production Value: 5
; http://php.net/session.hash-bits-per-character
session.sid_bits_per_character = 5

; Enable upload progress tracking in $_SESSION
; Default Value: On
; Development Value: On
; Production Value: On
; http://php.net/session.upload-progress.enabled
;session.upload_progress.enabled = On

; Cleanup the progress information as soon as all POST data has been read
; (i.e. upload completed).
; Default Value: On
; Development Value: On
; Production Value: On
; http://php.net/session.upload-progress.cleanup
;session.upload_progress.cleanup = On

; A prefix used for the upload progress key in $_SESSION
; Default Value: "upload_progress_"
; Development Value: "upload_progress_"
; Production Value: "upload_progress_"
; http://php.net/session.upload-progress.prefix
;session.upload_progress.prefix = "upload_progress_"

; The index name (concatenated with the prefix) in $_SESSION
; containing the upload progress information
; Default Value: "PHP_SESSION_UPLOAD_PROGRESS"
; Development Value: "PHP_SESSION_UPLOAD_PROGRESS"
; Production Value: "PHP_SESSION_UPLOAD_PROGRESS"
; http://php.net/session.upload-progress.name
;session.upload_progress.name = "PHP_SESSION_UPLOAD_PROGRESS"

; How frequently the upload progress should be updated.
; Given either in percentages (per-file), or in bytes
; Default Value: "1%"
; Development Value: "1%"
; Production Value: "1%"
; http://php.net/session.upload-progress.freq
;session.upload_progress.freq =  "1%"

; The minimum delay between updates, in seconds
; Default Value: 1
; Development Value: 1
; Production Value: 1
; http://php.net/session.upload-progress.min-freq
;session.upload_progress.min_freq = "1"

; Only write session data when session data is changed. Enabled by default.
; http://php.net/session.lazy-write
;session.lazy_write = On

[Assertion]
; Switch whether to compile assertions at all (to have no overhead at run-time)
; -1: Do not compile at all
;  0: Jump over assertion at run-time
;  1: Execute assertions
; Changing from or to a negative value is only possible in php.ini! (For turning assertions on and off at run-time, see assert.active, when zend.assertions = 1)
; Default Value: 1
; Development Value: 1
; Production Value: -1
; http://php.net/zend.assertions
zend.assertions = -1

; Assert(expr); active by default.
; http://php.net/assert.active
;assert.active = On

; Throw an AssertationException on failed assertions
; http://php.net/assert.exception
;assert.exception = On

; Issue a PHP warning for each failed assertion. (Overridden by assert.exception if active)
; http://php.net/assert.warning
;assert.warning = On

; Don't bail out by default.
; http://php.net/assert.bail
;assert.bail = Off

; User-function to be called if an assertion fails.
; http://php.net/assert.callback
;assert.callback = 0

; Eval the expression with current error_reporting().  Set to true if you want
; error_reporting(0) around the eval().
; http://php.net/assert.quiet-eval
;assert.quiet_eval = 0

[COM]
; path to a file containing GUIDs, IIDs or filenames of files with TypeLibs
; http://php.net/com.typelib-file
;com.typelib_file =

; allow Distributed-COM calls
; http://php.net/com.allow-dcom
;com.allow_dcom = true

; autoregister constants of a components typlib on com_load()
; http://php.net/com.autoregister-typelib
;com.autoregister_typelib = true

; register constants casesensitive
; http://php.net/com.autoregister-casesensitive
;com.autoregister_casesensitive = false

; show warnings on duplicate constant registrations
; http://php.net/com.autoregister-verbose
;com.autoregister_verbose = true

; The default character set code-page to use when passing strings to and from COM objects.
; Default: system ANSI code page
;com.code_page=

[mbstring]
; language for internal character representation.
; This affects mb_send_mail() and mbstring.detect_order.
; http://php.net/mbstring.language
;mbstring.language = Japanese

; Use of this INI entry is deprecated, use global internal_encoding instead.
; internal/script encoding.
; Some encoding cannot work as internal encoding. (e.g. SJIS, BIG5, ISO-2022-*)
; If empty, default_charset or internal_encoding or iconv.internal_encoding is used.
; The precedence is: default_charset < internal_encoding < iconv.internal_encoding
;mbstring.internal_encoding =

; Use of this INI entry is deprecated, use global input_encoding instead.
; http input encoding.
; mbstring.encoding_traslation = On is needed to use this setting.
; If empty, default_charset or input_encoding or mbstring.input is used.
; The precedence is: default_charset < intput_encoding < mbsting.http_input
; http://php.net/mbstring.http-input
;mbstring.http_input =

; Use of this INI entry is deprecated, use global output_encoding instead.
; http output encoding.
; mb_output_handler must be registered as output buffer to function.
; If empty, default_charset or output_encoding or mbstring.http_output is used.
; The precedence is: default_charset < output_encoding < mbstring.http_output
; To use an output encoding conversion, mbstring's output handler must be set
; otherwise output encoding conversion cannot be performed.
; http://php.net/mbstring.http-output
;mbstring.http_output =

; enable automatic encoding translation according to
; mbstring.internal_encoding setting. Input chars are
; converted to internal encoding by setting this to On.
; Note: Do _not_ use automatic encoding translation for
;       portable libs/applications.
; http://php.net/mbstring.encoding-translation
;mbstring.encoding_translation = Off

; automatic encoding detection order.
; "auto" detect order is changed according to mbstring.language
; http://php.net/mbstring.detect-order
;mbstring.detect_order = auto

; substitute_character used when character cannot be converted
; one from another
; http://php.net/mbstring.substitute-character
;mbstring.substitute_character = none

; overload(replace) single byte functions by mbstring functions.
; mail(), ereg(), etc are overloaded by mb_send_mail(), mb_ereg(),
; etc. Possible values are 0,1,2,4 or combination of them.
; For example, 7 for overload everything.
; 0: No overload
; 1: Overload mail() function
; 2: Overload str*() functions
; 4: Overload ereg*() functions
; http://php.net/mbstring.func-overload
;mbstring.func_overload = 0

; enable strict encoding detection.
; Default: Off
;mbstring.strict_detection = On

; This directive specifies the regex pattern of content types for which mb_output_handler()
; is activated.
; Default: mbstring.http_output_conv_mimetype=^(text/|application/xhtml\+xml)
;mbstring.http_output_conv_mimetype=

[gd]
; Tell the jpeg decode to ignore warnings and try to create
; a gd image. The warning will then be displayed as notices
; disabled by default
; http://php.net/gd.jpeg-ignore-warning
;gd.jpeg_ignore_warning = 1

[exif]
; Exif UNICODE user comments are handled as UCS-2BE/UCS-2LE and JIS as JIS.
; With mbstring support this will automatically be converted into the encoding
; given by corresponding encode setting. When empty mbstring.internal_encoding
; is used. For the decode settings you can distinguish between motorola and
; intel byte order. A decode setting cannot be empty.
; http://php.net/exif.encode-unicode
;exif.encode_unicode = ISO-8859-15

; http://php.net/exif.decode-unicode-motorola
;exif.decode_unicode_motorola = UCS-2BE

; http://php.net/exif.decode-unicode-intel
;exif.decode_unicode_intel    = UCS-2LE

; http://php.net/exif.encode-jis
;exif.encode_jis =

; http://php.net/exif.decode-jis-motorola
;exif.decode_jis_motorola = JIS

; http://php.net/exif.decode-jis-intel
;exif.decode_jis_intel    = JIS

[Tidy]
; The path to a default tidy configuration file to use when using tidy
; http://php.net/tidy.default-config
;tidy.default_config = /usr/local/lib/php/default.tcfg

; Should tidy clean and repair output automatically?
; WARNING: Do not use this option if you are generating non-html content
; such as dynamic images
; http://php.net/tidy.clean-output
tidy.clean_output = Off

[soap]
; Enables or disables WSDL caching feature.
; http://php.net/soap.wsdl-cache-enabled
soap.wsdl_cache_enabled=1

; Sets the directory name where SOAP extension will put cache files.
; http://php.net/soap.wsdl-cache-dir
soap.wsdl_cache_dir="/tmp"

; (time to live) Sets the number of second while cached file will be used
; instead of original one.
; http://php.net/soap.wsdl-cache-ttl
soap.wsdl_cache_ttl=86400

; Sets the size of the cache limit. (Max. number of WSDL files to cache)
soap.wsdl_cache_limit = 5

[sysvshm]
; A default size of the shared memory segment
;sysvshm.init_mem = 10000

[ldap]
; Sets the maximum number of open links or -1 for unlimited.
ldap.max_links = -1

[dba]
;dba.default_handler=

[opcache]
; Determines if Zend OPCache is enabled
;opcache.enable=1

; Determines if Zend OPCache is enabled for the CLI version of PHP
;opcache.enable_cli=1

; The OPcache shared memory storage size.
;opcache.memory_consumption=128

; The amount of memory for interned strings in Mbytes.
;opcache.interned_strings_buffer=8

; The maximum number of keys (scripts) in the OPcache hash table.
; Only numbers between 200 and 1000000 are allowed.
;opcache.max_accelerated_files=10000

; The maximum percentage of "wasted" memory until a restart is scheduled.
;opcache.max_wasted_percentage=5

; When this directive is enabled, the OPcache appends the current working
; directory to the script key, thus eliminating possible collisions between
; files with the same name (basename). Disabling the directive improves
; performance, but may break existing applications.
;opcache.use_cwd=1

; When disabled, you must reset the OPcache manually or restart the
; webserver for changes to the filesystem to take effect.
;opcache.validate_timestamps=1

; How often (in seconds) to check file timestamps for changes to the shared
; memory storage allocation. ("1" means validate once per second, but only
; once per request. "0" means always validate)
;opcache.revalidate_freq=2

; Enables or disables file search in include_path optimization
;opcache.revalidate_path=0

; If disabled, all PHPDoc comments are dropped from the code to reduce the
; size of the optimized code.
;opcache.save_comments=1

; If enabled, a fast shutdown sequence is used for the accelerated code
; Depending on the used Memory Manager this may cause some incompatibilities.
;opcache.fast_shutdown=0

; Allow file existence override (file_exists, etc.) performance feature.
;opcache.enable_file_override=0

; A bitmask, where each bit enables or disables the appropriate OPcache
; passes
;opcache.optimization_level=0xffffffff

;opcache.inherited_hack=1
;opcache.dups_fix=0

; The location of the OPcache blacklist file (wildcards allowed).
; Each OPcache blacklist file is a text file that holds the names of files
; that should not be accelerated. The file format is to add each filename
; to a new line. The filename may be a full path or just a file prefix
; (i.e., /var/www/x  blacklists all the files and directories in /var/www
; that start with 'x'). Line starting with a ; are ignored (comments).
;opcache.blacklist_filename=

; Allows exclusion of large files from being cached. By default all files
; are cached.
;opcache.max_file_size=0

; Check the cache checksum each N requests.
; The default value of "0" means that the checks are disabled.
;opcache.consistency_checks=0

; How long to wait (in seconds) for a scheduled restart to begin if the cache
; is not being accessed.
;opcache.force_restart_timeout=180

; OPcache error_log file name. Empty string assumes "stderr".
;opcache.error_log=

; All OPcache errors go to the Web server log.
; By default, only fatal errors (level 0) or errors (level 1) are logged.
; You can also enable warnings (level 2), info messages (level 3) or
; debug messages (level 4).
;opcache.log_verbosity_level=1

; Preferred Shared Memory back-end. Leave empty and let the system decide.
;opcache.preferred_memory_model=

; Protect the shared memory from unexpected writing during script execution.
; Useful for internal debugging only.
;opcache.protect_memory=0

; Allows calling OPcache API functions only from PHP scripts which path is
; started from specified string. The default "" means no restriction
;opcache.restrict_api=

; Mapping base of shared memory segments (for Windows only). All the PHP
; processes have to map shared memory into the same address space. This
; directive allows to manually fix the "Unable to reattach to base address"
; errors.
;opcache.mmap_base=

; Enables and sets the second level cache directory.
; It should improve performance when SHM memory is full, at server restart or
; SHM reset. The default "" disables file based caching.
;opcache.file_cache=

; Enables or disables opcode caching in shared memory.
;opcache.file_cache_only=0

; Enables or disables checksum validation when script loaded from file cache.
;opcache.file_cache_consistency_checks=1

; Implies opcache.file_cache_only=1 for a certain process that failed to
; reattach to the shared memory (for Windows only). Explicitly enabled file
; cache is required.
;opcache.file_cache_fallback=1

; Enables or disables copying of PHP code (text segment) into HUGE PAGES.
; This should improve performance, but requires appropriate OS configuration.
;opcache.huge_code_pages=1

; Validate cached file permissions.
;opcache.validate_permission=0

; Prevent name collisions in chroot'ed environment.
;opcache.validate_root=0

[curl]
; A default value for the CURLOPT_CAINFO option. This is required to be an
; absolute path.
;curl.cainfo =

[openssl]
; The location of a Certificate Authority (CA) file on the local filesystem
; to use when verifying the identity of SSL/TLS peers. Most users should
; not specify a value for this directive as PHP will attempt to use the
; OS-managed cert stores in its absence. If specified, this value may still
; be overridden on a per-stream basis via the "cafile" SSL stream context
; option.
;openssl.cafile=

; If openssl.cafile is not specified or if the CA file is not found, the
; directory pointed to by openssl.capath is searched for a suitable
; certificate. This value must be a correctly hashed certificate directory.
; Most users should not specify a value for this directive as PHP will
; attempt to use the OS-managed cert stores in its absence. If specified,
; this value may still be overridden on a per-stream basis via the "capath"
; SSL stream context option.
;openssl.capath=

; Local Variables:
; tab-width: 4
; End:
```

## File: `docker/php-fpm/xdebug`
```
#! /bin/bash

# NOTE: At the moment, this has only been confirmed to work with PHP 7


# Grab full name of php-fpm container
PHP_FPM_CONTAINER=$(docker ps | grep php-fpm | awk '{print $1}')


# Grab OS type
if [[ "$(uname)" == "Darwin" ]]; then
    OS_TYPE="OSX"
else
    OS_TYPE=$(expr substr $(uname -s) 1 5)
fi


xdebug_status ()
{
    echo 'xDebug status'

    # If running on Windows, need to prepend with winpty :(
    if [[ $OS_TYPE == "MINGW" ]]; then
        winpty docker exec -it $PHP_FPM_CONTAINER bash -c 'php -v'

    else
        docker exec -it $PHP_FPM_CONTAINER bash -c 'php -v'
    fi

}


xdebug_start ()
{
    echo 'Start xDebug'

    # And uncomment line with xdebug extension, thus enabling it
    ON_CMD="sed -i 's/^;zend_extension=/zend_extension=/g' \
                    /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini"


    # If running on Windows, need to prepend with winpty :(
    if [[ $OS_TYPE == "MINGW" ]]; then
        winpty docker exec -it $PHP_FPM_CONTAINER bash -c "${ON_CMD}"
        docker restart $PHP_FPM_CONTAINER
        winpty docker exec -it $PHP_FPM_CONTAINER bash -c 'php -v'

    else
        docker exec -it $PHP_FPM_CONTAINER bash -c "${ON_CMD}"
        docker restart $PHP_FPM_CONTAINER
        docker exec -it $PHP_FPM_CONTAINER bash -c 'php -v'
    fi
}


xdebug_stop ()
{
    echo 'Stop xDebug'

    # Comment out xdebug extension line
    OFF_CMD="sed -i 's/^zend_extension=/;zend_extension=/g' /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini"


    # If running on Windows, need to prepend with winpty :(
    if [[ $OS_TYPE == "MINGW" ]]; then
        # This is the equivalent of:
        # winpty docker exec -it laradock_php-fpm_1 bash -c 'bla bla bla'
        # Thanks to @michaelarnauts at https://github.com/docker/compose/issues/593
        winpty docker exec -it $PHP_FPM_CONTAINER bash -c "${OFF_CMD}"
        docker restart $PHP_FPM_CONTAINER
        #docker-compose restart php-fpm
        winpty docker exec -it $PHP_FPM_CONTAINER bash -c 'php -v'

    else
        docker exec -it $PHP_FPM_CONTAINER bash -c "${OFF_CMD}"
        # docker-compose restart php-fpm
        docker restart $PHP_FPM_CONTAINER
        docker exec -it $PHP_FPM_CONTAINER bash -c 'php -v'
    fi
}


case $@ in
    stop|STOP)
        xdebug_stop
        ;;
    start|START)
        xdebug_start
        ;;
    status|STATUS)
        xdebug_status
        ;;
    *)
        echo "xDebug [Stop | Start | Status] in the ${PHP_FPM_CONTAINER} container."
        echo "xDebug must have already been installed."
        echo "Usage:"
        echo "  .php-fpm/xdebug stop|start|status"

esac

exit 1
```

## File: `docker/php-fpm/xdebug.ini`
```
xdebug.remote_host="host.docker.internal"
xdebug.remote_connect_back=0
xdebug.remote_port=9000
xdebug.idekey=PHPSTORM

xdebug.remote_autostart=1
xdebug.remote_enable=1
xdebug.cli_color=1
xdebug.profiler_enable=0
xdebug.profiler_output_dir="~/xdebug/phpstorm/tmp/profiling"

xdebug.remote_handler=dbgp
xdebug.remote_mode=req

xdebug.var_display_max_children=-1
xdebug.var_display_max_data=-1
xdebug.var_display_max_depth=-1
```

## File: `docker/workplace/Dockerfile`
```
FROM phusion/baseimage:0.11

RUN DEBIAN_FRONTEND=noninteractive
RUN locale-gen en_US.UTF-8

ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LC_CTYPE=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV TERM xterm

# Add the "PHP 7" ppa
RUN apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:ondrej/php

RUN echo 'DPkg::options { "--force-confdef"; };' >> /etc/apt/apt.conf

# yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Install "PHP Extentions", "libraries", "Software's"
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --allow-downgrades --allow-remove-essential \
        --allow-change-held-packages \
        apt-utils \
        libldap2-dev \
        libzip-dev zip unzip \
        php7.4-cli \
        php7.4-common \
        php7.4-curl \
        php7.4-intl \
        php7.4-json \
        php7.4-xml \
        php7.4-mbstring \
        php7.4-mysql \
        php7.4-zip \
        php7.4-bcmath \
        php7.4-memcached \
        php7.4-gd \
        php7.4-dev \
        php7.4-ldap \
        php7.4-zip \
        php7.4-xdebug \
        pkg-config \
        libcurl4-openssl-dev \
        libedit-dev \
        libssl-dev \
        libxml2-dev \
        xz-utils \
        libsqlite3-dev \
        sqlite3 \
        git \
        curl \
        vim \
        nasm \
        nano

#####################################
# User
#####################################

ARG PUID=1000
ENV PUID ${PUID}
ARG PGID=1000
ENV PGID ${PGID}

RUN set -xe; \
    groupadd -g ${PGID} dev && \
    useradd -l -u ${PUID} -g dev -m dev -G docker_env && \
    usermod -p "*" dev -s /bin/bash

RUN pecl channel-update pecl.php.net

#####################################
# Composer:
#####################################

RUN curl -s http://getcomposer.org/installer | php && \
    echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \
    mv composer.phar /usr/local/bin/composer

RUN . ~/.bashrc

#####################################
# xDebug
#####################################

RUN sed -i 's/^;//g' /etc/php/7.4/cli/conf.d/20-xdebug.ini

# ADD for REMOTE debugging
COPY ./xdebug.ini /etc/php/7.4/cli/conf.d/xdebug.ini

######################################
# Node Yarn:
######################################

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y yarn

######################################
# CS Fixer
######################################

RUN curl -L https://cs.symfony.com/download/php-cs-fixer-v2.phar -o php-cs-fixer \
    && chmod a+x php-cs-fixer \
    && mv php-cs-fixer /usr/local/bin/php-cs-fixer

######################################
# Bash updates
######################################

# makefile autocomplete
RUN echo "complete -W \"\`grep -oE '^[a-zA-Z0-9_-]+:([^=]|$)' ?akefile | sed 's/[^a-zA-Z0-9_.-]*$//'\`\" make" >> ~/.bashrc && \
    echo "complete -W \"\`grep -oE '^[a-zA-Z0-9_-]+:([^=]|$)' ?akefile | sed 's/[^a-zA-Z0-9_.-]*$//'\`\" make" >> ~/.bash_profile && \
    echo "complete -W \"\`grep -oE '^[a-zA-Z0-9_-]+:([^=]|$)' ?akefile | sed 's/[^a-zA-Z0-9_.-]*$//'\`\" make" >> /home/dev/.bashrc && \
    echo "complete -W \"\`grep -oE '^[a-zA-Z0-9_-]+:([^=]|$)' ?akefile | sed 's/[^a-zA-Z0-9_.-]*$//'\`\" make" >> /home/dev/bash_profile

# Clean up
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm /var/log/lastlog /var/log/faillog

######################################
# PHP MND (conflicts with local repo)
######################################
USER dev

RUN composer global require povils/phpmnd && \
    echo "export PATH=${PATH}:${HOME}/.composer/vendor/bin" >> ~/.bashrc

USER root

# Set default work directory
WORKDIR /var/www
```

## File: `docker/workplace/xdebug.ini`
```
xdebug.remote_host="host.docker.internal"
xdebug.remote_connect_back=0
xdebug.remote_port=9000
xdebug.idekey=PHPSTORM

xdebug.remote_autostart=1
xdebug.remote_enable=1
xdebug.cli_color=1
xdebug.profiler_enable=0
xdebug.profiler_output_dir="~/xdebug/phpstorm/tmp/profiling"

xdebug.remote_handler=dbgp
xdebug.remote_mode=req

xdebug.var_display_max_children=-1
xdebug.var_display_max_data=-1
xdebug.var_display_max_depth=-1
```

## File: `public/index.php`
```php
<?php

use App\Kernel;
use Symfony\Component\ErrorHandler\Debug;
use Symfony\Component\HttpFoundation\Request;

require dirname(__DIR__).'/config/bootstrap.php';

if ($_SERVER['APP_DEBUG']) {
    umask(0000);

    Debug::enable();
}

if ($trustedProxies = $_SERVER['TRUSTED_PROXIES'] ?? false) {
    Request::setTrustedProxies(explode(',', $trustedProxies), Request::HEADER_X_FORWARDED_ALL ^ Request::HEADER_X_FORWARDED_HOST);
}

if ($trustedHosts = $_SERVER['TRUSTED_HOSTS'] ?? false) {
    Request::setTrustedHosts([$trustedHosts]);
}

$kernel = new Kernel($_SERVER['APP_ENV'], (bool) $_SERVER['APP_DEBUG']);
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);
```

## File: `src/Kernel.php`
```php
<?php

declare(strict_types=1);

namespace App;

use Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use Symfony\Component\Config\Loader\LoaderInterface;
use Symfony\Component\Config\Resource\FileResource;
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\HttpKernel\Kernel as BaseKernel;
use Symfony\Component\Routing\RouteCollectionBuilder;

class Kernel extends BaseKernel
{
    use MicroKernelTrait;

    private const CONFIG_EXTS = '.{php,xml,yaml,yml}';

    public function registerBundles(): iterable
    {
        $contents = require $this->getProjectDir() . '/config/bundles.php';
        foreach ($contents as $class => $envs) {
            if ($envs[$this->environment] ?? $envs['all'] ?? false) {
                yield new $class();
            }
        }
    }

    public function getProjectDir(): string
    {
        return \dirname(__DIR__);
    }

    protected function configureContainer(ContainerBuilder $container, LoaderInterface $loader): void
    {
        $container->addResource(new FileResource($this->getProjectDir() . '/config/bundles.php'));
        $container->setParameter('container.dumper.inline_class_loader', \PHP_VERSION_ID < 70400 || $this->debug);
        $container->setParameter('container.dumper.inline_factories', true);
        $confDir = $this->getProjectDir() . '/config';

        $loader->load($confDir . '/{packages}/*' . self::CONFIG_EXTS, 'glob');
        $loader->load($confDir . '/{packages}/' . $this->environment . '/*' . self::CONFIG_EXTS, 'glob');
        $loader->load($confDir . '/{services}' . self::CONFIG_EXTS, 'glob');
        $loader->load($confDir . '/{services}_' . $this->environment . self::CONFIG_EXTS, 'glob');
    }

    protected function configureRoutes(RouteCollectionBuilder $routes): void
    {
        $confDir = $this->getProjectDir() . '/config';

        $routes->import($confDir . '/{routes}/' . $this->environment . '/*' . self::CONFIG_EXTS, '/', 'glob');
        $routes->import($confDir . '/{routes}/*' . self::CONFIG_EXTS, '/', 'glob');
        $routes->import($confDir . '/{routes}' . self::CONFIG_EXTS, '/', 'glob');
    }
}
```

## File: `src/Core/Application/Command/AuthToken/CreateAuthToken/CreateAuthTokenCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\AuthToken\CreateAuthToken;

final class CreateAuthTokenCommand
{
    private string $username;

    private string $password;

    public function __construct(string $username, string $password)
    {
        $this->username = $username;
        $this->password = $password;
    }

    public function getUsername(): string
    {
        return $this->username;
    }

    public function getPassword(): string
    {
        return $this->password;
    }
}
```

## File: `src/Core/Application/Command/AuthToken/CreateAuthToken/CreateAuthTokenCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\AuthToken\CreateAuthToken;

use App\Core\Domain\Model\User\UserRepositoryInterface;
use App\Shared\Domain\Exception\InvalidInputDataException;
use Lexik\Bundle\JWTAuthenticationBundle\Services\JWTTokenManagerInterface;
use Symfony\Component\Security\Core\Encoder\UserPasswordEncoderInterface;

final class CreateAuthTokenCommandHandler
{
    private UserPasswordEncoderInterface $userPasswordEncoder;

    private UserRepositoryInterface $userRepository;

    private JWTTokenManagerInterface $JWTTokenManager;

    public function __construct(
        UserPasswordEncoderInterface $userPasswordEncoder,
        UserRepositoryInterface $userRepository,
        JWTTokenManagerInterface $JWTTokenManager
    ) {
        $this->userPasswordEncoder = $userPasswordEncoder;
        $this->userRepository = $userRepository;
        $this->JWTTokenManager = $JWTTokenManager;
    }

    public function __invoke(CreateAuthTokenCommand $command): string
    {
        $user = $this->userRepository->findUserByUserName($command->getUsername());

        if ($user === null) {
            throw new InvalidInputDataException('Invalid credentials');
        }

        if (!$this->userPasswordEncoder->isPasswordValid($user, $command->getPassword())) {
            throw new InvalidInputDataException('Invalid credentials');
        }

        return $this->JWTTokenManager->create($user);
    }
}
```

## File: `src/Core/Application/Command/Task/TaskCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task;

abstract class TaskCommand
{
    protected string $title;

    protected \DateTimeImmutable $executionDay;

    protected string $description;

    public function __construct(string $title, \DateTimeImmutable $executionDay, string $description = '')
    {
        $this->title = $title;
        $this->executionDay = $executionDay;
        $this->description = $description;
    }

    public function getTitle(): string
    {
        return $this->title;
    }

    public function getDescription(): string
    {
        return $this->description;
    }

    public function getExecutionDay(): \DateTimeImmutable
    {
        return $this->executionDay;
    }
}
```

## File: `src/Core/Application/Command/Task/CreateTask/CreateTaskCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task\CreateTask;

use App\Core\Application\Command\Task\TaskCommand;

class CreateTaskCommand extends TaskCommand
{
}
```

## File: `src/Core/Application/Command/Task/CreateTask/CreateTaskCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task\CreateTask;

use App\Core\Domain\Model\Task\Task;
use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use App\Core\Domain\Model\User\UserFetcherInterface;

final class CreateTaskCommandHandler
{
    private TaskRepositoryInterface $taskRepository;

    private UserFetcherInterface $userFetcher;

    public function __construct(TaskRepositoryInterface $taskRepository, UserFetcherInterface $userFetcher)
    {
        $this->taskRepository = $taskRepository;
        $this->userFetcher = $userFetcher;
    }

    public function __invoke(CreateTaskCommand $command): int
    {
        $user = $this->userFetcher->fetchRequiredUser();

        $task = new Task($command->getTitle(), $command->getExecutionDay(), $user, $command->getDescription());
        $this->taskRepository->add($task);

        return $task->getId();
    }
}
```

## File: `src/Core/Application/Command/Task/DeleteTask/DeleteTaskCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task\DeleteTask;

final class DeleteTaskCommand
{
    private int $id;

    public function __construct(int $id)
    {
        $this->id = $id;
    }

    public function getId(): int
    {
        return $this->id;
    }
}
```

## File: `src/Core/Application/Command/Task/DeleteTask/DeleteTaskCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task\DeleteTask;

use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use App\Core\Domain\Model\User\UserFetcherInterface;
use App\Shared\Domain\Exception\AccessForbiddenException;
use App\Shared\Domain\Exception\ResourceNotFoundException;

final class DeleteTaskCommandHandler
{
    private TaskRepositoryInterface $taskRepository;

    private UserFetcherInterface $userFetcher;

    public function __construct(TaskRepositoryInterface $taskRepository, UserFetcherInterface $userFetcher)
    {
        $this->taskRepository = $taskRepository;
        $this->userFetcher = $userFetcher;
    }

    public function __invoke(DeleteTaskCommand $command): void
    {
        $task = $this->taskRepository->find($command->getId());

        if ($task === null) {
            throw new ResourceNotFoundException(sprintf('Task with id "%s" is not found', $command->getId()));
        }

        $user = $this->userFetcher->fetchRequiredUser();

        if (!$task->getUser()->equals($user)) {
            throw new AccessForbiddenException('Access prohibited');
        }

        $this->taskRepository->remove($task);
    }
}
```

## File: `src/Core/Application/Command/Task/MakeTaskDeclined/MakeTaskDeclinedCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task\MakeTaskDeclined;

final class MakeTaskDeclinedCommand
{
    private int $id;

    public function __construct(int $id)
    {
        $this->id = $id;
    }

    public function getId(): int
    {
        return $this->id;
    }
}
```

## File: `src/Core/Application/Command/Task/MakeTaskDeclined/MakeTaskDeclinedCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task\MakeTaskDeclined;

use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use App\Core\Domain\Model\User\UserFetcherInterface;
use App\Shared\Domain\Exception\AccessForbiddenException;
use App\Shared\Domain\Exception\ResourceNotFoundException;

final class MakeTaskDeclinedCommandHandler
{
    private TaskRepositoryInterface $taskRepository;

    private UserFetcherInterface $userFetcher;

    public function __construct(TaskRepositoryInterface $taskRepository, UserFetcherInterface $userFetcher)
    {
        $this->taskRepository = $taskRepository;
        $this->userFetcher = $userFetcher;
    }

    public function __invoke(MakeTaskDeclinedCommand $command): void
    {
        $task = $this->taskRepository->find($command->getId());

        if ($task === null) {
            throw new ResourceNotFoundException(sprintf('Task with id "%s" is not found', $command->getId()));
        }

        $user = $this->userFetcher->fetchRequiredUser();

        if (!$task->getUser()->equals($user)) {
            throw new AccessForbiddenException('Access prohibited');
        }

        $task->decline();

        $this->taskRepository->add($task);
    }
}
```

## File: `src/Core/Application/Command/Task/MakeTaskDone/MakeTaskDoneCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task\MakeTaskDone;

final class MakeTaskDoneCommand
{
    private int $id;

    public function __construct(int $id)
    {
        $this->id = $id;
    }

    public function getId(): int
    {
        return $this->id;
    }
}
```

## File: `src/Core/Application/Command/Task/MakeTaskDone/MakeTaskDoneCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task\MakeTaskDone;

use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use App\Core\Domain\Model\User\UserFetcherInterface;
use App\Shared\Domain\Exception\AccessForbiddenException;
use App\Shared\Domain\Exception\ResourceNotFoundException;

final class MakeTaskDoneCommandHandler
{
    private TaskRepositoryInterface $taskRepository;

    private UserFetcherInterface $userFetcher;

    public function __construct(TaskRepositoryInterface $taskRepository, UserFetcherInterface $userFetcher)
    {
        $this->taskRepository = $taskRepository;
        $this->userFetcher = $userFetcher;
    }

    public function __invoke(MakeTaskDoneCommand $command): void
    {
        $task = $this->taskRepository->find($command->getId());

        if ($task === null) {
            throw new ResourceNotFoundException(sprintf('Task with id "%s" is not found', $command->getId()));
        }

        $user = $this->userFetcher->fetchRequiredUser();

        if (!$task->getUser()->equals($user)) {
            throw new AccessForbiddenException('Access prohibited');
        }

        $task->done();

        $this->taskRepository->add($task);
    }
}
```

## File: `src/Core/Application/Command/Task/UpdateTask/UpdateTaskCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task\UpdateTask;

use App\Core\Application\Command\Task\TaskCommand;

final class UpdateTaskCommand extends TaskCommand
{
    private int $id;

    public function __construct(int $id, string $title, \DateTimeImmutable $executionDay, string $description = '')
    {
        parent::__construct($title, $executionDay, $description);
        $this->id = $id;
    }

    public function getId(): int
    {
        return $this->id;
    }
}
```

## File: `src/Core/Application/Command/Task/UpdateTask/UpdateTaskCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\Task\UpdateTask;

use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use App\Core\Domain\Model\User\UserFetcherInterface;
use App\Shared\Domain\Exception\AccessForbiddenException;
use App\Shared\Domain\Exception\ResourceNotFoundException;

final class UpdateTaskCommandHandler
{
    private TaskRepositoryInterface $taskRepository;

    private UserFetcherInterface $userFetcher;

    public function __construct(TaskRepositoryInterface $taskRepository, UserFetcherInterface $userFetcher)
    {
        $this->taskRepository = $taskRepository;
        $this->userFetcher = $userFetcher;
    }

    public function __invoke(UpdateTaskCommand $command): void
    {
        $task = $this->taskRepository->find($command->getId());

        if ($task === null) {
            throw new ResourceNotFoundException(sprintf('Task with id "%s" is not found', $command->getId()));
        }

        $user = $this->userFetcher->fetchRequiredUser();

        if (!$task->getUser()->equals($user)) {
            throw new AccessForbiddenException('Access prohibited');
        }

        $task->changeTitle($command->getTitle());
        $task->changeDescription($command->getDescription());
        $task->changeExecutionDay($command->getExecutionDay());

        $this->taskRepository->add($task);
    }
}
```

## File: `src/Core/Application/Command/User/CreateUser/CreateUserCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\User\CreateUser;

final class CreateUserCommand
{
    private string $username;

    private string $password;

    public function __construct(string $username, string $password)
    {
        $this->username = $username;
        $this->password = $password;
    }

    public function getUsername(): string
    {
        return $this->username;
    }

    public function getPassword(): string
    {
        return $this->password;
    }
}
```

## File: `src/Core/Application/Command/User/CreateUser/CreateUserCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Command\User\CreateUser;

use App\Core\Domain\Model\User\UniqueUsernameSpecificationInterface;
use App\Core\Domain\Model\User\User;
use App\Core\Domain\Model\User\UserRepositoryInterface;
use Symfony\Component\Security\Core\Encoder\EncoderFactoryInterface;

final class CreateUserCommandHandler
{
    private EncoderFactoryInterface $encoderFactory;

    private UserRepositoryInterface $userRepository;

    private UniqueUsernameSpecificationInterface $uniqueUsernameSpecification;

    public function __construct(
        EncoderFactoryInterface $encoderFactory,
        UserRepositoryInterface $userRepository,
        UniqueUsernameSpecificationInterface $uniqueUsernameSpecification
    ) {
        $this->encoderFactory = $encoderFactory;
        $this->userRepository = $userRepository;
        $this->uniqueUsernameSpecification = $uniqueUsernameSpecification;
    }

    public function __invoke(CreateUserCommand $command): void
    {
        $encoder = $this->encoderFactory->getEncoder(User::class);
        $user = new User(
            $command->getUsername(),
            $encoder->encodePassword($command->getPassword(), null),
            $this->uniqueUsernameSpecification
        );
        $this->userRepository->add($user);
    }
}
```

## File: `src/Core/Application/EventHandler/Task/LogTaskLiveCycleChanges/TaskCreatedEventHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\EventHandler\Task\LogTaskLiveCycleChanges;

use App\Core\Domain\Model\Task\TaskCreatedEvent;
use Psr\Log\LoggerInterface;

final class TaskCreatedEventHandler
{
    private LoggerInterface $logger;

    public function __construct(LoggerInterface $logger)
    {
        $this->logger = $logger;
    }

    public function __invoke(TaskCreatedEvent $event): void
    {
        $this->logger->info(sprintf('Task %s was created', $event->getTask()->getId()));
    }
}
```

## File: `src/Core/Application/EventHandler/Task/LogTaskLiveCycleChanges/TaskDeclinedEventHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\EventHandler\Task\LogTaskLiveCycleChanges;

use App\Core\Domain\Model\Task\TaskDeclinedEvent;
use Psr\Log\LoggerInterface;

final class TaskDeclinedEventHandler
{
    private LoggerInterface $logger;

    public function __construct(LoggerInterface $logger)
    {
        $this->logger = $logger;
    }

    public function __invoke(TaskDeclinedEvent $event): void
    {
        $this->logger->info(sprintf('Task %s was declined', $event->getTask()->getId()));
    }
}
```

## File: `src/Core/Application/EventHandler/Task/LogTaskLiveCycleChanges/TaskDoneEventHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\EventHandler\Task\LogTaskLiveCycleChanges;

use App\Core\Domain\Model\Task\TaskDoneEvent;
use Psr\Log\LoggerInterface;

final class TaskDoneEventHandler
{
    private LoggerInterface $logger;

    public function __construct(LoggerInterface $logger)
    {
        $this->logger = $logger;
    }

    public function __invoke(TaskDoneEvent $event): void
    {
        $this->logger->info(sprintf('Task %s was done', $event->getTask()->getId()));
    }
}
```

## File: `src/Core/Application/Query/Task/DTO/TaskDTO.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Query\Task\DTO;

use App\Core\Domain\Model\Task\Task;

final class TaskDTO
{
    private int $id;

    private string $title;

    private string $description;

    private string $status;

    private \DateTimeImmutable $executionDay;

    private \DateTimeImmutable $createdAt;

    public static function fromEntity(Task $task): TaskDTO
    {
        $dto = new static();
        $dto->setId($task->getId());
        $dto->setTitle($task->getTitle());
        $dto->setDescription($task->getDescription());
        $dto->setStatus((string) $task->getStatus());
        $dto->setExecutionDay($task->getExecutionDay());
        $dto->setCreatedAt($task->getCreatedAt());

        return $dto;
    }

    /**
     * @param array<string, mixed> $data
     *
     * @return TaskDTO
     */
    public static function fromQueryArray(array $data): TaskDTO
    {
        if (!isset($data['id'], $data['title'], $data['description'], $data['status'], $data['execution_day'], $data['created_at'])) {
            throw new \InvalidArgumentException(sprintf('Not all keys are set or null %s', var_export($data, true)));
        }

        $dto = new static();
        $dto->setId((int) $data['id']);
        $dto->setTitle($data['title']);
        $dto->setDescription($data['description']);
        $dto->setStatus($data['status']);
        $dto->setExecutionDay(new \DateTimeImmutable($data['execution_day']));
        $dto->setCreatedAt(new \DateTimeImmutable($data['created_at']));

        return $dto;
    }

    public function getId(): int
    {
        return $this->id;
    }

    public function setId(int $id): void
    {
        $this->id = $id;
    }

    public function getTitle(): string
    {
        return $this->title;
    }

    public function setTitle(string $title): void
    {
        $this->title = $title;
    }

    public function getDescription(): string
    {
        return $this->description;
    }

    public function setDescription(string $description): void
    {
        $this->description = $description;
    }

    public function getStatus(): string
    {
        return $this->status;
    }

    public function setStatus(string $status): void
    {
        $this->status = $status;
    }

    public function getExecutionDay(): \DateTimeImmutable
    {
        return $this->executionDay;
    }

    public function setExecutionDay(\DateTimeImmutable $executionDay): void
    {
        $this->executionDay = $executionDay;
    }

    public function getCreatedAt(): \DateTimeImmutable
    {
        return $this->createdAt;
    }

    public function setCreatedAt(\DateTimeImmutable $createdAt): void
    {
        $this->createdAt = $createdAt;
    }
}
```

## File: `src/Core/Application/Query/Task/GetTask/GetTaskQuery.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Query\Task\GetTask;

final class GetTaskQuery
{
    private int $id;

    public function __construct(int $id)
    {
        $this->id = $id;
    }

    public function getId(): int
    {
        return $this->id;
    }
}
```

## File: `src/Core/Application/Query/Task/GetTask/GetTaskQueryHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Query\Task\GetTask;

use App\Core\Application\Query\Task\DTO\TaskDTO;
use App\Core\Domain\Model\Task\Task;
use App\Core\Domain\Model\User\UserFetcherInterface;
use App\Shared\Domain\Exception\AccessForbiddenException;
use App\Shared\Domain\Exception\ResourceNotFoundException;
use Doctrine\ORM\EntityManagerInterface;

final class GetTaskQueryHandler
{
    private EntityManagerInterface $em;

    private UserFetcherInterface $userFetcher;

    public function __construct(EntityManagerInterface $em, UserFetcherInterface $userFetcher)
    {
        $this->em = $em;
        $this->userFetcher = $userFetcher;
    }

    public function __invoke(GetTaskQuery $query): TaskDTO
    {
        $task = $this->em->find(Task::class, $query->getId());

        if ($task === null) {
            throw new ResourceNotFoundException(sprintf('Task with id "%s" is not found', $query->getId()));
        }

        $user = $this->userFetcher->fetchRequiredUser();

        if (!$task->getUser()->equals($user)) {
            throw new AccessForbiddenException('Access prohibited');
        }

        return TaskDTO::fromEntity($task);
    }
}
```

## File: `src/Core/Application/Query/Task/GetTasks/GetTasksQuery.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Query\Task\GetTasks;

use App\Shared\Infrastructure\ValueObject\Pagination;

final class GetTasksQuery
{
    private Pagination $pagination;

    private ?\DateTimeImmutable $executionDate;

    private ?string $searchText;

    public function __construct(Pagination $pagination, ?\DateTimeImmutable $executionDate = null, ?string $searchText = null)
    {
        $this->pagination = $pagination;
        $this->executionDate = $executionDate;
        $this->searchText = $searchText;
    }

    public function getPagination(): Pagination
    {
        return $this->pagination;
    }

    public function getExecutionDate(): ?\DateTimeImmutable
    {
        return $this->executionDate;
    }

    public function getSearchText(): ?string
    {
        return $this->searchText;
    }
}
```

## File: `src/Core/Application/Query/Task/GetTasks/GetTasksQueryHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Application\Query\Task\GetTasks;

use App\Core\Application\Query\Task\DTO\TaskDTO;
use App\Core\Domain\Model\Task\Task;
use App\Core\Domain\Model\User\UserFetcherInterface;
use App\Shared\Infrastructure\Type\DateTimeFormat;
use App\Shared\Infrastructure\ValueObject\PaginatedData;
use Doctrine\DBAL\Query\QueryBuilder;
use Doctrine\ORM\EntityManagerInterface;

final class GetTasksQueryHandler
{
    private EntityManagerInterface $em;

    private UserFetcherInterface $userFetcher;

    public function __construct(EntityManagerInterface $em, UserFetcherInterface $userFetcher)
    {
        $this->em = $em;
        $this->userFetcher = $userFetcher;
    }

    public function __invoke(GetTasksQuery $query): PaginatedData
    {
        $userId = $this->userFetcher->fetchRequiredUser()->getId();

        $qb = $this->buildQuery($query, $userId);
        $tasks = $this->em->getConnection()->executeQuery($qb->getSQL(), $qb->getParameters())->fetchAll(\PDO::FETCH_ASSOC);

        $taskDTOs = [];

        foreach ($tasks as $task) {
            $taskDTOs[] = TaskDTO::fromQueryArray($task);
        }

        $qb = $this->buildQuery($query, $userId)
            ->select('COUNT(*)')
            ->setMaxResults(null)
            ->setFirstResult(0);

        $count = (int) $this->em->getConnection()->executeQuery($qb->getSQL(), $qb->getParameters())->fetchColumn();

        return new PaginatedData($taskDTOs, $count);
    }

    private function buildQuery(GetTasksQuery $query, int $userId): QueryBuilder
    {
        $taskTable = $this->em->getClassMetadata(Task::class)->getTableName();

        $qb = $this->em->getConnection()->createQueryBuilder()
            ->select('t.*')
            ->from($taskTable, 't')
            ->innerJoin('t', 'user', 'u', 'u.id = t.user_id')
            ->where('u.id = :userId')
            ->orderBy('t.created_at')
            ->setFirstResult($query->getPagination()->getOffset())
            ->setMaxResults($query->getPagination()->getLimit())
            ->setParameter('userId', $userId);

        if ($query->getExecutionDate() !== null) {
            $executionDay = $query->getExecutionDate()->setTime(0, 0);
            $qb->andWhere('t.execution_day >= :fromTime')
                ->andWhere('t.execution_day < :toTime')
                ->setParameter('fromTime', $executionDay->format(DateTimeFormat::MYSQL_FORMAT))
                ->setParameter('toTime', $executionDay->modify('+1 day')->format(DateTimeFormat::MYSQL_FORMAT));
        }

        if ($query->getSearchText() !== null) {
            $qb->andWhere('t.title LIKE :searchText OR t.description LIKE :searchText')
                ->setParameter('searchText', "%{$query->getSearchText()}%");
        }

        return $qb;
    }
}
```

## File: `src/Core/Domain/Model/Task/Status.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\Task;

use App\Shared\Domain\Service\Assert\Assert;
use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Embeddable
 */
class Status
{
    public const NEW = 'new';
    public const DECLINED = 'declined';
    public const DONE = 'done';
    public const VALID_STATUSES = [self::NEW, self::DECLINED, self::DONE];

    /**
     * @ORM\Column(type="string", length=10, nullable=false)
     */
    private string $status;

    public function __construct(string $status)
    {
        Assert::inArray($status, self::VALID_STATUSES, 'Status value should be one of: %2$s. Got: %s');

        $this->status = $status;
    }

    public function __toString(): string
    {
        return $this->status;
    }

    public function getStatus(): string
    {
        return $this->status;
    }

    public static function NEW(): self
    {
        return new self(self::NEW);
    }

    public static function DECLINED(): self
    {
        return new self(self::DECLINED);
    }

    public static function DONE(): self
    {
        return new self(self::DONE);
    }

    public function is(string $status): bool
    {
        return $this->status === $status;
    }
}
```

## File: `src/Core/Domain/Model/Task/Task.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\Task;

use App\Core\Domain\Model\User\User;
use App\Shared\Domain\Exception\BusinessLogicViolationException;
use App\Shared\Domain\Model\Aggregate;
use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity()
 * @ORM\Table(indexes={@ORM\Index(name="task_status_idx", columns={"status"})})
 */
class Task extends Aggregate
{
    use TaskGS;

    public const MIN_TITLE_LENGTH = 5;
    public const MAX_TITLE_LENGTH = 100;
    public const MAX_DESCRIPTION_LENGTH = 100;

    /**
     * @ORM\Id()
     * @ORM\GeneratedValue()
     * @ORM\Column(type="integer", options={"unsigned"=true})
     */
    private int $id;

    /**
     * @ORM\Column(type="string", length=100, nullable=false)
     */
    private string $title;

    /**
     * @ORM\Column(type="string", length=255, nullable=false)
     */
    private string $description;

    /**
     * @ORM\Embedded(class="App\Core\Domain\Model\Task\Status", columnPrefix=false)
     */
    private Status $status;

    /**
     * @ORM\ManyToOne(targetEntity="App\Core\Domain\Model\User\User")
     * @ORM\JoinColumn(onDelete="cascade", nullable=false)
     */
    private User $user;

    /**
     * @ORM\Column(type="datetime_immutable", nullable=true)
     */
    private \DateTimeImmutable $executionDay;

    /**
     * @ORM\Column(type="datetime_immutable", nullable=true)
     */
    private \DateTimeImmutable $createdAt;

    public function __construct(string $title, \DateTimeImmutable $executionDay, User $user, string $description = '')
    {
        $this->setTitle($title);
        $this->setExecutionDay($executionDay);
        $this->setUser($user);
        $this->setDescription($description);
        $this->setStatus(Status::NEW());
        $this->setCreatedAt(new \DateTimeImmutable());

        $this->raise(new TaskCreatedEvent($this));
    }

    // API

    public function changeTitle(string $title): void
    {
        $this->setTitle($title);
    }

    public function changeDescription(string $description): void
    {
        $this->setDescription($description);
    }

    public function changeExecutionDay(\DateTimeImmutable $assignedDay): void
    {
        $this->setExecutionDay($assignedDay);
    }

    public function done(): void
    {
        if ($this->status->is(Status::DONE)) {
            return;
        }

        if ($this->status->is(Status::DECLINED)) {
            throw new BusinessLogicViolationException('Declined task can\'t be done');
        }

        $this->setStatus(Status::DONE());
        $this->raise(new TaskDoneEvent($this));
    }

    public function decline(): void
    {
        if ($this->status->is(Status::DECLINED)) {
            return;
        }

        if ($this->status->is(Status::DONE)) {
            throw new BusinessLogicViolationException('Done task can\'t be declined');
        }

        $this->setStatus(Status::DECLINED());
        $this->raise(new TaskDeclinedEvent($this));
    }
}
```

## File: `src/Core/Domain/Model/Task/TaskCreatedEvent.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\Task;

use App\Shared\Domain\Model\DomainEventInterface;

final class TaskCreatedEvent implements DomainEventInterface
{
    private Task $task;

    public function __construct(Task $task)
    {
        $this->task = $task;
    }

    public function getTask(): Task
    {
        return $this->task;
    }
}
```

## File: `src/Core/Domain/Model/Task/TaskDeclinedEvent.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\Task;

use App\Shared\Domain\Model\DomainEventInterface;

final class TaskDeclinedEvent implements DomainEventInterface
{
    private Task $task;

    public function __construct(Task $task)
    {
        $this->task = $task;
    }

    public function getTask(): Task
    {
        return $this->task;
    }
}
```

## File: `src/Core/Domain/Model/Task/TaskDoneEvent.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\Task;

use App\Shared\Domain\Model\DomainEventInterface;

final class TaskDoneEvent implements DomainEventInterface
{
    private Task $task;

    public function __construct(Task $task)
    {
        $this->task = $task;
    }

    public function getTask(): Task
    {
        return $this->task;
    }
}
```

## File: `src/Core/Domain/Model/Task/TaskGS.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\Task;

use App\Core\Domain\Model\User\User;
use App\Shared\Domain\Service\Assert\Assert;

trait TaskGS
{
    public function getId(): int
    {
        return $this->id;
    }

    public function getTitle(): string
    {
        return $this->title;
    }

    public function getExecutionDay(): \DateTimeImmutable
    {
        return $this->executionDay;
    }

    public function getUser(): User
    {
        return $this->user;
    }

    public function getDescription(): string
    {
        return $this->description;
    }

    public function getStatus(): Status
    {
        return $this->status;
    }

    public function getCreatedAt(): \DateTimeImmutable
    {
        return $this->createdAt;
    }

    private function setTitle(string $title): void
    {
        Assert::minLength($title, self::MIN_TITLE_LENGTH, 'Title should contain at least %2$s characters. Got: %s');
        Assert::maxLength($title, self::MAX_TITLE_LENGTH, 'Title should contain at most %2$s characters. Got: %s');
        $this->title = $title;
    }

    private function setDescription(string $description): void
    {
        Assert::maxLength($description, self::MAX_DESCRIPTION_LENGTH, 'Description should contain at most %2$s characters. Got: %s');
        $this->description = $description;
    }

    private function setUser(User $user): void
    {
        $this->user = $user;
    }

    private function setStatus(Status $status): void
    {
        $this->status = $status;
    }

    private function setExecutionDay(\DateTimeImmutable $executionDay): void
    {
        $executionDayNormalized = $executionDay->setTime(0, 0);
        $now = (new \DateTimeImmutable())->setTime(0, 0);

        Assert::greaterThanEq($executionDayNormalized, $now, 'Execution day should be not in past');

        $this->executionDay = $executionDayNormalized;
    }

    private function setCreatedAt(\DateTimeImmutable $createdAt): void
    {
        $this->createdAt = $createdAt;
    }
}
```

## File: `src/Core/Domain/Model/Task/TaskRepositoryInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\Task;

interface TaskRepositoryInterface
{
    public function find(int $id): ?Task;

    public function add(Task $task): void;

    public function remove(Task $task): void;
}
```

## File: `src/Core/Domain/Model/User/UniqueUsernameSpecificationInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\User;

interface UniqueUsernameSpecificationInterface
{
    public function isSatisfiedBy(string $userName): bool;
}
```

## File: `src/Core/Domain/Model/User/User.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\User;

use App\Shared\Domain\Exception\InvalidInputDataException;
use App\Shared\Domain\Model\Aggregate;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Security\Core\User\UserInterface;

/**
 * @ORM\Entity()
 */
class User extends Aggregate implements UserInterface
{
    use UserGS;

    public const DEFAULT_USER_ROLE = 'ROLE_USER';
    public const MAX_USER_NAME_LENGTH = 180;
    public const MAX_PASSWORD_LENGTH = 255;

    /**
     * @ORM\Id()
     * @ORM\GeneratedValue()
     * @ORM\Column(type="integer", options={"unsigned"=true})
     */
    private int $id;

    /**
     * @ORM\Column(type="string", length=180, unique=true)
     */
    private string $username;

    /**
     * @var array<int, string>
     *
     * @ORM\Column(type="json", nullable=false)
     */
    private array $roles = [];

    /**
     * @ORM\Column(type="string", nullable=false)
     */
    private string $password;

    /**
     * @ORM\Column(type="datetime_immutable", options={"default"="CURRENT_TIMESTAMP"}, nullable=false)
     */
    private \DateTimeImmutable $createdAt;

    /**
     * @param string $username
     * @param string $password
     * @param UniqueUsernameSpecificationInterface $uniqueUsernameSpecification
     * @param array|string[] $roles
     */
    public function __construct(
        string $username,
        string $password,
        UniqueUsernameSpecificationInterface $uniqueUsernameSpecification,
        array $roles = [self::DEFAULT_USER_ROLE]
    ) {
        if (!$uniqueUsernameSpecification->isSatisfiedBy($username)) {
            throw new InvalidInputDataException(sprintf('Username %s already exists', $username));
        }

        $this->setUsername($username);
        $this->setPassword($password);
        $this->setRoles($roles);
        $this->setCreatedAt(new \DateTimeImmutable());
    }

    public function eraseCredentials(): void
    {
        //dont need
    }

    public function equals(User $user): bool
    {
        return $user->getId() === $this->getId();
    }
}
```

## File: `src/Core/Domain/Model/User/UserFetcherInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\User;

interface UserFetcherInterface
{
    public function fetchRequiredUser(): User;

    public function fetchNullableUser(): ?User;
}
```

## File: `src/Core/Domain/Model/User/UserGS.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\User;

use App\Shared\Domain\Service\Assert\Assert;

trait UserGS
{
    public function getId(): int
    {
        return $this->id;
    }

    public function getUsername(): string
    {
        return $this->username;
    }

    /**
     * @return array<int, string>
     */
    public function getRoles(): array
    {
        return $this->roles;
    }

    public function getPassword(): string
    {
        return $this->password;
    }

    public function getSalt(): string
    {
        return '';
    }

    public function getCreatedAt(): \DateTimeImmutable
    {
        return $this->createdAt;
    }

    // Setters

    private function setPassword(string $password): void
    {
        Assert::maxLength($password, self::MAX_PASSWORD_LENGTH, 'Password should contain at most %2$s characters. Got: %s');
        $this->password = $password;
    }

    private function setUsername(string $username): void
    {
        Assert::maxLength($username, self::MAX_USER_NAME_LENGTH, 'Username should contain at most %2$s characters. Got: %s');
        $this->username = $username;
    }

    private function setCreatedAt(\DateTimeImmutable $createdAt): void
    {
        $this->createdAt = $createdAt;
    }

    /**
     * @param array<int, string> $roles
     */
    private function setRoles(array $roles): void
    {
        if (!\in_array(self::DEFAULT_USER_ROLE, $roles, true)) {
            $roles[] = self::DEFAULT_USER_ROLE;
        }

        $this->roles = array_unique($roles);
    }
}
```

## File: `src/Core/Domain/Model/User/UserRepositoryInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Domain\Model\User;

interface UserRepositoryInterface
{
    public function find(int $id): ?User;

    public function findUserByUserName(string $username): ?User;

    public function add(User $user): void;

    public function remove(User $user): void;
}
```

## File: `src/Core/Infrastructure/Repository/TaskRepository.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Infrastructure\Repository;

use App\Core\Domain\Model\Task\Task;
use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use Doctrine\ORM\EntityManagerInterface;

class TaskRepository implements TaskRepositoryInterface
{
    private EntityManagerInterface $em;

    public function __construct(EntityManagerInterface $em)
    {
        $this->em = $em;
    }

    public function find(int $id): ?Task
    {
        return $this->em->find(Task::class, $id);
    }

    public function add(Task $task): void
    {
        $this->em->persist($task);
        $this->em->flush();
    }

    public function remove(Task $task): void
    {
        $this->em->remove($task);
        $this->em->flush();
    }
}
```

## File: `src/Core/Infrastructure/Repository/UserRepository.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Infrastructure\Repository;

use App\Core\Domain\Model\User\User;
use App\Core\Domain\Model\User\UserRepositoryInterface;
use Doctrine\ORM\EntityManagerInterface;

class UserRepository implements UserRepositoryInterface
{
    private EntityManagerInterface $em;

    public function __construct(EntityManagerInterface $em)
    {
        $this->em = $em;
    }

    public function find(int $id): ?User
    {
        return $this->em->find(User::class, $id);
    }

    public function findUserByUserName(string $username): ?User
    {
        return $this->em->createQueryBuilder()
            ->select('u')
            ->from(User::class, 'u')
            ->where('u.username = :username')
            ->setParameters(['username' => $username])
            ->getQuery()->getOneOrNullResult();
    }

    public function add(User $user): void
    {
        $this->em->persist($user);
        $this->em->flush();
    }

    public function remove(User $user): void
    {
        $this->em->remove($user);
        $this->em->flush();
    }
}
```

## File: `src/Core/Infrastructure/Security/UserFetcher.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Infrastructure\Security;

use App\Core\Domain\Model\User\User;
use App\Core\Domain\Model\User\UserFetcherInterface;
use Symfony\Component\Security\Core\Security;

final class UserFetcher implements UserFetcherInterface
{
    private Security $security;

    public function __construct(Security $security)
    {
        $this->security = $security;
    }

    public function fetchRequiredUser(): User
    {
        $user = $this->security->getUser();

        if ($user === null) {
            throw new \InvalidArgumentException('Current user not found check security access list');
        }

        if (!($user instanceof User)) {
            throw new \InvalidArgumentException(sprintf('Invalid user type %s', \get_class($user)));
        }

        return $user;
    }

    public function fetchNullableUser(): ?user
    {
        $user = $this->security->getUser();

        if ($user === null) {
            return null;
        }

        if (!($user instanceof User)) {
            throw new \InvalidArgumentException(sprintf('Invalid user type %s', \get_class($user)));
        }

        return $user;
    }
}
```

## File: `src/Core/Infrastructure/Specification/User/UniqueUsernameSpecification.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Infrastructure\Specification\User;

use App\Core\Domain\Model\User\UniqueUsernameSpecificationInterface;
use App\Core\Domain\Model\User\User;
use Doctrine\ORM\EntityManagerInterface;

final class UniqueUsernameSpecification implements UniqueUsernameSpecificationInterface
{
    private EntityManagerInterface $em;

    public function __construct(EntityManagerInterface $em)
    {
        $this->em = $em;
    }

    public function isSatisfiedBy(string $username): bool
    {
        return $this->em->createQueryBuilder()
            ->select('u')
            ->from(User::class, 'u')
            ->where('u.username = :username')
            ->setParameters(['username' => $username])
            ->getQuery()->getOneOrNullResult() === null;
    }
}
```

## File: `src/Core/Ports/Cli/AddUserCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Ports\Cli;

use App\Core\Application\Command\User\CreateUser\CreateUserCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Question\Question;
use Symfony\Component\Messenger\HandleTrait;
use Symfony\Component\Messenger\MessageBusInterface;

/**
 * For internal usage
 */
final class AddUserCommand extends Command
{
    use HandleTrait;

    public const MIN_PASSWORD_LENGTH = 5;

    protected static $defaultName = 'app:create-user';

    public function __construct(MessageBusInterface $commandBus)
    {
        $this->messageBus = $commandBus;
        parent::__construct();
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $helper = $this->getHelper('question');

        $question = new Question('Please enter the username [admin] : ', 'admin');
        $userName = (string) $helper->ask($input, $output, $question);

        if ($userName === '') {
            $output->writeln('<error>User name should be not blank</error>');
        }

        $question = new Question('Please enter the password : ');
        $question->setHidden(true);
        $password = (string) $helper->ask($input, $output, $question);

        if (\strlen($password) < self::MIN_PASSWORD_LENGTH) {
            $output->writeln('<error>Password is to short, need more than 4 symbols (bytes)</error>');
        }

        $question = new Question('Please repeat the password : ');
        $question->setHidden(true);
        $passwordRepeat = (string) $helper->ask($input, $output, $question);

        if ($password !== $passwordRepeat) {
            $output->writeln('<error>Passwords dont match</error>');
        }

        $this->handle(new CreateUserCommand($userName, $password));

        $output->writeln('<info>User created</info>');

        return 0;
    }
}
```

## File: `src/Core/Ports/Rest/AuthToken/CreateAuthTokenAction.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Ports\Rest\AuthToken;

use App\Core\Application\Command\AuthToken\CreateAuthToken\CreateAuthTokenCommand;
use App\Shared\Infrastructure\Http\HttpSpec;
use App\Shared\Infrastructure\Http\ParamFetcher;
use OpenApi\Annotations as OA;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Messenger\HandleTrait;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Routing\Annotation\Route;

final class CreateAuthTokenAction
{
    use HandleTrait;

    public function __construct(MessageBusInterface $commandBus)
    {
        $this->messageBus = $commandBus;
    }

    /**
     * @Route("/api/auth-token", methods={"POST"})
     *
     * @param Request $request
     *
     * @return Response
     *
     * @OA\Parameter(
     *          name="body",
     *          in="body",
     *          description="JSON Payload",
     *          required=true,
     *          content="application/json",
     *          @OA\Schema(
     *              type="object",
     *              @OA\Property(property="username", type="string"),
     *              @OA\Property(property="password", type="string"),
     *          )
     * )
     *
     * @OA\Response(
     *     response=Response::HTTP_CREATED,
     *     description=HttpSpec::STR_HTTP_CREATED,
     *     @OA\Schema(@OA\Property(property="token", type="string"))
     * )
     * @OA\Response(response=Response::HTTP_BAD_REQUEST, description=HttpSpec::STR_HTTP_BAD_REQUEST)
     * @OA\Response(response=Response::HTTP_UNAUTHORIZED, description=HttpSpec::STR_HTTP_UNAUTHORIZED)
     *
     * @OA\Tag(name="Auth token")
     */
    public function __invoke(Request $request): Response
    {
        $paramFetcher = ParamFetcher::fromRequestBody($request);

        $token = $this->handle(new CreateAuthTokenCommand(
            $paramFetcher->getRequiredString('username'),
            $paramFetcher->getRequiredString('password')
        ));

        return new JsonResponse(['token' => $token], Response::HTTP_CREATED);
    }
}
```

## File: `src/Core/Ports/Rest/SerializerMapping/TaskDTO.yaml`
```yaml
App\Core\Application\Query\Task\DTO\TaskDTO:
  attributes:
    id:
      groups: ['task_view']
    title:
      groups: ['task_view']
    description:
      groups: ['task_view']
    status:
      groups: ['task_view']
    executionDay:
      groups: ['task_view']
    createdAt:
      groups: ['task_view']
```

## File: `src/Core/Ports/Rest/Task/CreateTaskAction.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Ports\Rest\Task;

use App\Core\Application\Command\Task\CreateTask\CreateTaskCommand;
use App\Shared\Infrastructure\Http\HttpSpec;
use App\Shared\Infrastructure\Http\ParamFetcher;
use OpenApi\Annotations as OA;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Messenger\HandleTrait;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Routing\RouterInterface;

final class CreateTaskAction
{
    use HandleTrait;

    private RouterInterface $router;

    public function __construct(MessageBusInterface $commandBus, RouterInterface $router)
    {
        $this->messageBus = $commandBus;
        $this->router = $router;
    }

    /**
     * @Route("/api/tasks", methods={"POST"})
     *
     * @param Request $request
     *
     * @return Response
     *
     * @OA\Parameter(
     *          name="body",
     *          in="body",
     *          description="JSON Payload",
     *          required=true,
     *          content="application/json",
     *          @OA\Schema(
     *              type="object",
     *              @OA\Property(property="title", type="string"),
     *              @OA\Property(property="execution_day", type="string"),
     *              @OA\Property(property="description", type="string"),
     *          )
     * )
     *
     * @OA\Response(response=Response::HTTP_CREATED, description=HttpSpec::STR_HTTP_CREATED)
     * @OA\Response(response=Response::HTTP_BAD_REQUEST, description=HttpSpec::STR_HTTP_BAD_REQUEST)
     * @OA\Response(response=Response::HTTP_UNAUTHORIZED, description=HttpSpec::STR_HTTP_UNAUTHORIZED)
     *
     * @OA\Tag(name="Task")
     */
    public function __invoke(Request $request): Response
    {
        $paramFetcher = ParamFetcher::fromRequestBody($request);

        $command = new CreateTaskCommand(
            $paramFetcher->getRequiredString('title'),
            $paramFetcher->getRequiredDate('execution_day'),
            $paramFetcher->getNullableString('description') ?? '',
        );

        $id = $this->handle($command);
        $resourceUrl = $this->router->generate('api_get_task', ['id' => $id]);

        return new JsonResponse(null, Response::HTTP_CREATED, [HttpSpec::HEADER_LOCATION => $resourceUrl]);
    }
}
```

## File: `src/Core/Ports/Rest/Task/DeleteTaskAction.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Ports\Rest\Task;

use App\Core\Application\Command\Task\DeleteTask\DeleteTaskCommand;
use App\Shared\Infrastructure\Http\HttpSpec;
use App\Shared\Infrastructure\Http\ParamFetcher;
use OpenApi\Annotations as OA;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Messenger\HandleTrait;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Routing\Annotation\Route;

final class DeleteTaskAction
{
    use HandleTrait;

    public function __construct(MessageBusInterface $commandBus)
    {
        $this->messageBus = $commandBus;
    }

    /**
     * @Route("/api/tasks/{id}", methods={"DELETE"}, requirements={"id": "\d+"})
     *
     * @param Request $request
     *
     * @return Response
     *
     * @OA\Response(response=Response::HTTP_NO_CONTENT, description=HttpSpec::STR_HTTP_NO_CONTENT)
     * @OA\Response(response=Response::HTTP_NOT_FOUND, description=HttpSpec::STR_HTTP_NOT_FOUND)
     * @OA\Response(response=Response::HTTP_UNAUTHORIZED, description=HttpSpec::STR_HTTP_UNAUTHORIZED)
     *
     * @OA\Tag(name="Task")
     */
    public function __invoke(Request $request): Response
    {
        $route = ParamFetcher::fromRequestAttributes($request);

        $this->handle(new DeleteTaskCommand($route->getRequiredInt('id')));

        return new JsonResponse(null, Response::HTTP_NO_CONTENT);
    }
}
```

## File: `src/Core/Ports/Rest/Task/GetTaskAction.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Ports\Rest\Task;

use App\Core\Application\Query\Task\DTO\TaskDTO;
use App\Core\Application\Query\Task\GetTask\GetTaskQuery;
use App\Shared\Infrastructure\Http\HttpSpec;
use App\Shared\Infrastructure\Http\ParamFetcher;
use Nelmio\ApiDocBundle\Annotation\Model;
use OpenApi\Annotations as OA;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Messenger\HandleTrait;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Serializer\Normalizer\NormalizerInterface;

final class GetTaskAction
{
    use HandleTrait;

    private NormalizerInterface $normalizer;

    public function __construct(MessageBusInterface $queryBus, NormalizerInterface $normalizer)
    {
        $this->messageBus = $queryBus;
        $this->normalizer = $normalizer;
    }

    /**
     * @Route("/api/tasks/{id}", methods={"GET"}, requirements={"id": "\d+"}, name="api_get_task")
     *
     * @param Request $request
     *
     * @return Response
     *
     * @OA\Response(
     *     response=Response::HTTP_OK,
     *     description=HttpSpec::STR_HTTP_OK,
     *     @OA\Schema(ref=@Model(type=TaskDTO::class, groups={"task_view"}))
     * )
     * @OA\Response(response=Response::HTTP_NOT_FOUND, description=HttpSpec::STR_HTTP_NOT_FOUND)
     * @OA\Response(response=Response::HTTP_UNAUTHORIZED, description=HttpSpec::STR_HTTP_UNAUTHORIZED)
     *
     * @OA\Tag(name="Task")
     */
    public function __invoke(Request $request): Response
    {
        $route = ParamFetcher::fromRequestAttributes($request);

        $task = $this->handle(new GetTaskQuery($route->getRequiredInt('id')));

        return new JsonResponse(
            $this->normalizer->normalize($task, '', ['groups' => 'task_view']),
        );
    }
}
```

## File: `src/Core/Ports/Rest/Task/GetTasksAction.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Ports\Rest\Task;

use App\Core\Application\Query\Task\DTO\TaskDTO;
use App\Core\Application\Query\Task\GetTasks\GetTasksQuery;
use App\Shared\Infrastructure\Http\HttpSpec;
use App\Shared\Infrastructure\Http\ParamFetcher;
use App\Shared\Infrastructure\ValueObject\PaginatedData;
use App\Shared\Infrastructure\ValueObject\Pagination;
use Nelmio\ApiDocBundle\Annotation\Model;
use OpenApi\Annotations as OA;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Messenger\HandleTrait;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Serializer\Normalizer\NormalizerInterface;

final class GetTasksAction
{
    use HandleTrait;

    private NormalizerInterface $normalizer;

    public function __construct(MessageBusInterface $queryBus, NormalizerInterface $normalizer)
    {
        $this->messageBus = $queryBus;
        $this->normalizer = $normalizer;
    }

    /**
     * @Route("/api/tasks", methods={"GET"})
     *
     * @param Request $request
     *
     * @return Response
     *
     * @OA\Parameter(
     *     name="execution_day",
     *     in="query",
     *     description="Search phrase text",
     *     @OA\Schema(type="string")
     * )
     * @OA\Parameter(
     *     name="search",
     *     in="query",
     *     description="Search phrase text",
     *     @OA\Schema(type="string")
     * )
     * @OA\Parameter(
     *     name="limit",
     *     in="query",
     *     description="Number of result items",
     *     @OA\Schema(type="integer", default=Pagination::DEFAULT_LIMIT)
     * )
     * @OA\Parameter(
     *     name="offset",
     *     in="query",
     *     description="First result offset",
     *     @OA\Schema(type="integer", default=Pagination::DEFAULT_OFFSET)
     * )
     * @OA\Response(
     *     response=Response::HTTP_OK,
     *     description=HttpSpec::STR_HTTP_OK,
     *     @OA\Schema(type="array", @OA\Items(ref=@Model(type=TaskDTO::class, groups={"task_view"})))
     * )
     * @OA\Response(response=Response::HTTP_BAD_REQUEST, description=HttpSpec::STR_HTTP_BAD_REQUEST)
     * @OA\Response(response=Response::HTTP_UNAUTHORIZED, description=HttpSpec::STR_HTTP_UNAUTHORIZED)
     *
     * @OA\Tag(name="Task")
     */
    public function __invoke(Request $request): Response
    {
        $query = ParamFetcher::fromRequestQuery($request);

        $query = new GetTasksQuery(
            Pagination::fromRequest($request),
            $query->getNullableDate('execution_day'),
            $query->getNullableString('search')
        );

        /** @var PaginatedData $paginatedData */
        $paginatedData = $this->handle($query);

        return new JsonResponse(
            $this->normalizer->normalize($paginatedData->getData(), '', ['groups' => 'task_view']),
            Response::HTTP_OK,
            [HttpSpec::HEADER_X_ITEMS_COUNT => $paginatedData->getCount()]
        );
    }
}
```

## File: `src/Core/Ports/Rest/Task/MakeTaskDeclinedAction.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Ports\Rest\Task;

use App\Core\Application\Command\Task\MakeTaskDeclined\MakeTaskDeclinedCommand;
use App\Shared\Infrastructure\Http\HttpSpec;
use App\Shared\Infrastructure\Http\ParamFetcher;
use OpenApi\Annotations as OA;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Messenger\HandleTrait;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Routing\Annotation\Route;

final class MakeTaskDeclinedAction
{
    use HandleTrait;

    public function __construct(MessageBusInterface $commandBus)
    {
        $this->messageBus = $commandBus;
    }

    /**
     * @Route("/api/tasks/{id}/status/declined", methods={"PATCH"})
     *
     * @OA\Patch(description="Make task declined")
     *
     * @param Request $request
     *
     * @return Response
     *
     * @OA\Response(response=Response::HTTP_NO_CONTENT, description=HttpSpec::STR_HTTP_NO_CONTENT)
     * @OA\Response(response=Response::HTTP_NOT_FOUND, description=HttpSpec::STR_HTTP_NOT_FOUND)
     * @OA\Response(response=Response::HTTP_UNAUTHORIZED, description=HttpSpec::STR_HTTP_UNAUTHORIZED)
     *
     * @OA\Tag(name="Task")
     */
    public function __invoke(Request $request): Response
    {
        $route = ParamFetcher::fromRequestAttributes($request);

        $this->handle(new MakeTaskDeclinedCommand($route->getRequiredInt('id')));

        return new JsonResponse(null, Response::HTTP_NO_CONTENT);
    }
}
```

## File: `src/Core/Ports/Rest/Task/MakeTaskDoneAction.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Ports\Rest\Task;

use App\Core\Application\Command\Task\MakeTaskDone\MakeTaskDoneCommand;
use App\Shared\Infrastructure\Http\HttpSpec;
use App\Shared\Infrastructure\Http\ParamFetcher;
use OpenApi\Annotations as OA;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Messenger\HandleTrait;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Routing\Annotation\Route;

final class MakeTaskDoneAction
{
    use HandleTrait;

    public function __construct(MessageBusInterface $commandBus)
    {
        $this->messageBus = $commandBus;
    }

    /**
     * @Route("/api/tasks/{id}/status/done", methods={"PATCH"})
     *
     * @OA\Patch(description="Make task done")
     *
     * @param Request $request
     *
     * @return Response
     *
     * @OA\Response(response=Response::HTTP_NO_CONTENT, description=HttpSpec::STR_HTTP_NO_CONTENT)
     * @OA\Response(response=Response::HTTP_NOT_FOUND, description=HttpSpec::STR_HTTP_NOT_FOUND)
     * @OA\Response(response=Response::HTTP_UNAUTHORIZED, description=HttpSpec::STR_HTTP_UNAUTHORIZED)
     *
     * @OA\Tag(name="Task")
     */
    public function __invoke(Request $request): Response
    {
        $route = ParamFetcher::fromRequestAttributes($request);

        $this->handle(new MakeTaskDoneCommand($route->getRequiredInt('id')));

        return new JsonResponse(null, Response::HTTP_NO_CONTENT);
    }
}
```

## File: `src/Core/Ports/Rest/Task/UpdateTaskAction.php`
```php
<?php

declare(strict_types=1);

namespace App\Core\Ports\Rest\Task;

use App\Core\Application\Command\Task\UpdateTask\UpdateTaskCommand;
use App\Shared\Infrastructure\Http\HttpSpec;
use App\Shared\Infrastructure\Http\ParamFetcher;
use OpenApi\Annotations as OA;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Messenger\HandleTrait;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Routing\Annotation\Route;

final class UpdateTaskAction
{
    use HandleTrait;

    public function __construct(MessageBusInterface $commandBus)
    {
        $this->messageBus = $commandBus;
    }

    /**
     * @Route("/api/tasks/{id}", methods={"PUT"}, requirements={"id": "\d+"})
     *
     * @param Request $request
     *
     * @return Response
     *
     * @OA\Parameter(
     *          name="body",
     *          in="body",
     *          description="JSON Payload",
     *          required=true,
     *          content="application/json",
     *          @OA\Schema(
     *              type="object",
     *              @OA\Property(property="title", type="string"),
     *              @OA\Property(property="execution_day", type="string"),
     *              @OA\Property(property="description", type="string"),
     *          )
     * )
     *
     * @OA\Response(response=Response::HTTP_NO_CONTENT, description=HttpSpec::STR_HTTP_NO_CONTENT)
     * @OA\Response(response=Response::HTTP_NOT_FOUND, description=HttpSpec::STR_HTTP_NOT_FOUND)
     * @OA\Response(response=Response::HTTP_BAD_REQUEST, description=HttpSpec::STR_HTTP_BAD_REQUEST)
     * @OA\Response(response=Response::HTTP_UNAUTHORIZED, description=HttpSpec::STR_HTTP_UNAUTHORIZED)
     *
     * @OA\Tag(name="Task")
     */
    public function __invoke(Request $request): Response
    {
        $route = ParamFetcher::fromRequestAttributes($request);
        $body = ParamFetcher::fromRequestBody($request);

        $command = new UpdateTaskCommand(
            $route->getRequiredInt('id'),
            $body->getRequiredString('title'),
            $body->getRequiredDate('execution_day'),
            $body->getNullableString('description') ?? '',
        );

        $this->handle($command);

        return new JsonResponse(null, Response::HTTP_NO_CONTENT);
    }
}
```

## File: `src/Shared/Domain/Exception/AccessForbiddenException.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Exception;

final class AccessForbiddenException extends InvalidInputDataException
{
}
```

## File: `src/Shared/Domain/Exception/BusinessLogicViolationException.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Exception;

final class BusinessLogicViolationException extends InvalidInputDataException
{
}
```

## File: `src/Shared/Domain/Exception/InvalidInputDataException.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Exception;

class InvalidInputDataException extends \Exception
{
}
```

## File: `src/Shared/Domain/Exception/ResourceNotFoundException.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Exception;

final class ResourceNotFoundException extends InvalidInputDataException
{
}
```

## File: `src/Shared/Domain/Model/Aggregate.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Model;

abstract class Aggregate implements EntityInterface
{
    /**
     * @var DomainEventInterface[]
     */
    private array $events = [];

    abstract public function getId(): int;

    /**
     * @return DomainEventInterface[]
     */
    public function popEvents(): array
    {
        $events = $this->events;
        $this->events = [];

        return $events;
    }

    protected function raise(DomainEventInterface $event): void
    {
        $this->events[] = $event;
    }
}
```

## File: `src/Shared/Domain/Model/DomainEventInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Model;

interface DomainEventInterface
{
}
```

## File: `src/Shared/Domain/Model/EntityInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Model;

interface EntityInterface
{
    public function getId(): int;
}
```

## File: `src/Shared/Domain/Service/Assert/Assert.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Service\Assert;

use App\Shared\Domain\Exception\InvalidInputDataException;
use Webmozart\Assert\Assert as WebmozartAssert;

final class Assert extends WebmozartAssert
{
    public static function dateTimeString(string $value, string $format, string $message = ''): void
    {
        $date = \DateTimeImmutable::createFromFormat($format, $value);

        if ($date === false) {
            static::reportInvalidArgument(sprintf(
                $message === '' ? 'Date time string "%s" should be like "%s"' : $message,
                $value,
                $format
            ));
        }
    }

    /**
     * @param string $message
     *
     * @throws InvalidInputDataException
     */
    protected static function reportInvalidArgument($message): void
    {
        throw new InvalidInputDataException($message);
    }
}
```

## File: `src/Shared/Infrastructure/Doctrine/DomainEventSubscriber.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Doctrine;

use App\Shared\Domain\Model\Aggregate;
use Doctrine\Common\EventSubscriber;
use Doctrine\ORM\Event\LifecycleEventArgs;
use Doctrine\ORM\Event\PostFlushEventArgs;
use Doctrine\ORM\Events;
use Symfony\Component\Messenger\MessageBusInterface;

final class DomainEventSubscriber implements EventSubscriber
{
    /**
     * @var Aggregate[]
     */
    private array $entities = [];

    private MessageBusInterface $eventBus;

    public function __construct(MessageBusInterface $eventBus)
    {
        $this->eventBus = $eventBus;
    }

    public function getSubscribedEvents(): array
    {
        return [
            Events::postPersist,
            Events::postUpdate,
            Events::postRemove,
            Events::postFlush,
        ];
    }

    public function postPersist(LifecycleEventArgs $args): void
    {
        $this->keepAggregateRoots($args);
    }

    public function postUpdate(LifecycleEventArgs $args): void
    {
        $this->keepAggregateRoots($args);
    }

    public function postRemove(LifecycleEventArgs $args): void
    {
        $this->keepAggregateRoots($args);
    }

    public function postFlush(PostFlushEventArgs $args): void
    {
        foreach ($this->entities as $entity) {
            foreach ($entity->popEvents() as $event) {
                $this->eventBus->dispatch($event);
            }
        }
    }

    private function keepAggregateRoots(LifecycleEventArgs $args): void
    {
        $entity = $args->getEntity();

        if (!($entity instanceof Aggregate)) {
            return;
        }

        $this->entities[] = $entity;
    }
}
```

## File: `src/Shared/Infrastructure/Http/ApiExceptionSubscriber.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Http;

use App\Shared\Domain\Exception\AccessForbiddenException;
use App\Shared\Domain\Exception\InvalidInputDataException;
use App\Shared\Domain\Exception\ResourceNotFoundException;
use Symfony\Component\EventDispatcher\EventSubscriberInterface;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\ExceptionEvent;
use Symfony\Component\HttpKernel\KernelEvents;
use Symfony\Component\Messenger\Exception\HandlerFailedException;

final class ApiExceptionSubscriber implements EventSubscriberInterface
{
    /**
     * @return array<string, string>
     */
    public static function getSubscribedEvents(): array
    {
        return [
            KernelEvents::EXCEPTION => 'onException',
        ];
    }

    public function onException(ExceptionEvent $event): void
    {
        if (!$event->isMasterRequest()) {
            return;
        }

        $request = $event->getRequest();

        if (strpos($request->getPathInfo(), '/api/doc') === 0
            || strpos($request->getPathInfo(), '/api/') !== 0) {
            return;
        }

        $throwable = $event->getThrowable();

        if ($throwable instanceof HandlerFailedException && \count($throwable->getNestedExceptions()) > 0) {
            $throwable = $throwable->getNestedExceptions()[0];
        }

        switch (true) {
            case $throwable instanceof ResourceNotFoundException:
                $event->setResponse(
                    new JsonResponse($event->getThrowable()->getMessage(), Response::HTTP_NOT_FOUND)
                );
                break;

            case $throwable instanceof AccessForbiddenException:
                $event->setResponse(
                    new JsonResponse($event->getThrowable()->getMessage(), Response::HTTP_FORBIDDEN)
                );
                break;

            case $throwable instanceof InvalidInputDataException:
                $event->setResponse(
                    new JsonResponse($event->getThrowable()->getMessage(), Response::HTTP_BAD_REQUEST)
                );
                break;
        }
    }
}
```

## File: `src/Shared/Infrastructure/Http/ApiRequestSubscriber.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Http;

use Symfony\Component\EventDispatcher\EventSubscriberInterface;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\RequestEvent;
use Symfony\Component\HttpKernel\KernelEvents;

final class ApiRequestSubscriber implements EventSubscriberInterface
{
    private const DEFAULT_JSON_DEPTH = 512;

    /**
     * @return array<string, string>
     */
    public static function getSubscribedEvents(): array
    {
        return [KernelEvents::REQUEST => 'onRequest'];
    }

    public function onRequest(RequestEvent $event): void
    {
        if (!$event->isMasterRequest()) {
            return;
        }

        $request = $event->getRequest();

        if (\is_resource($request->getContent())
            || $request->getContent() === ''
            || strpos($request->getPathInfo(), '/api/doc') === 0
            || strpos($request->getPathInfo(), '/api/') !== 0) {
            return;
        }

        if ($request->getContentType() !== 'json') {
            $event->setResponse(new JsonResponse('Invalid content type', Response::HTTP_BAD_REQUEST));

            return;
        }

        try {
            $requestContent = json_decode($request->getContent(), true, self::DEFAULT_JSON_DEPTH, JSON_THROW_ON_ERROR);
        } catch (\JsonException $e) {
            $event->setResponse(new JsonResponse('Invalid json string', Response::HTTP_BAD_REQUEST));

            return;
        }

        if (\is_array($requestContent)) {
            $request->request->replace($requestContent);
        }
    }
}
```

## File: `src/Shared/Infrastructure/Http/HttpSpec.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Http;

final class HttpSpec
{
    public const STR_HTTP_OK = 'OK';
    public const STR_HTTP_BAD_REQUEST = 'Bad request';
    public const STR_HTTP_UNAUTHORIZED = 'Unauthorized';
    public const STR_HTTP_NOT_FOUND = 'Not found';
    public const STR_HTTP_CREATED = 'Created';
    public const STR_HTTP_NO_CONTENT = 'No content';

    public const HEADER_X_ITEMS_COUNT = 'X-Items-Count';
    public const HEADER_LOCATION = 'Location';
}
```

## File: `src/Shared/Infrastructure/Http/ParamFetcher.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Http;

use App\Shared\Domain\Service\Assert\Assert;
use App\Shared\Infrastructure\Type\DateTimeFormat;
use Symfony\Component\HttpFoundation\Request;

final class ParamFetcher
{
    private const TYPE_STRING = 'string';
    private const TYPE_INT = 'int';
    private const TYPE_DATE = 'date';
    //TODO: need to add rest of scalar types

    private const SCALAR_TYPES = [self::TYPE_STRING, self::TYPE_INT];

    /**
     * @var array<string, mixed>
     */
    private array $data;

    private bool $testScalarType;

    /**
     * @param array<string, mixed> $data
     * @param bool $testScalarType
     */
    public function __construct(array $data, bool $testScalarType = true)
    {
        $this->data = $data;
        $this->testScalarType = $testScalarType;
    }

    public static function fromRequestAttributes(Request $request): self
    {
        return new self($request->attributes->all(), false);
    }

    public static function fromRequestBody(Request $request): self
    {
        return new self($request->request->all());
    }

    public static function fromRequestQuery(Request $request): self
    {
        return new self($request->query->all(), false);
    }

    public function getRequiredString(string $key): string
    {
        $this->assertRequired($key);
        $this->assertType($key, self::TYPE_STRING);

        return (string) $this->data[$key];
    }

    public function getNullableString(string $key): ?string
    {
        if (!isset($this->data[$key])) {
            return null;
        }
        $this->assertType($key, self::TYPE_STRING);

        return (string) $this->data[$key];
    }

    public function getRequiredInt(string $key): int
    {
        $this->assertRequired($key);
        $this->assertType($key, self::TYPE_INT);

        return (int) $this->data[$key];
    }

    public function getNullableInt(string $key): ?int
    {
        if (!isset($this->data[$key])) {
            return null;
        }
        $this->assertType($key, self::TYPE_INT);

        return (int) $this->data[$key];
    }

    public function getRequiredDate(string $key): \DateTimeImmutable
    {
        $this->assertRequired($key);
        $this->assertType($key, self::TYPE_DATE);

        return new \DateTimeImmutable($this->data[$key]);
    }

    public function getNullableDate(string $key): ?\DateTimeImmutable
    {
        if (!isset($this->data[$key])) {
            return null;
        }
        $this->assertType($key, self::TYPE_DATE);

        return new \DateTimeImmutable($this->data[$key]);
    }

    // .....
    // TODO:  Add additional required methods for every scalar type
    // .....

    private function assertRequired(string $key): void
    {
        Assert::keyExists($this->data, $key, sprintf('"%s" not found', $key));
        Assert::notNull($this->data[$key], sprintf('"%s" should be not null', $key));
    }

    private function assertType(string $key, string $type): void
    {
        if (!$this->testScalarType && \in_array($type, self::SCALAR_TYPES, true)) {
            return;
        }

        switch ($type) {
            case self::TYPE_STRING:
                Assert::string($this->data[$key], sprintf('"%s" should be a string. Got %%s', $key));
                break;

            case self::TYPE_INT:
                Assert::string($this->data[$key], sprintf('"%s" should be an integer. Got %%s', $key));
                break;

            case self::TYPE_DATE:
                Assert::dateTimeString($this->data[$key], DateTimeFormat::DATE_FORMAT, sprintf('"%s" should be a valid format "%s" date', $key, DateTimeFormat::DATE_FORMAT));
                break;
        }
    }
}
```

## File: `src/Shared/Infrastructure/Migration/Version20200601085854.php`
```php
<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20200601085854 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->abortIf($this->connection->getDatabasePlatform()->getName() !== 'mysql', 'Migration can only be executed safely on \'mysql\'.');

        $this->addSql('CREATE TABLE user (id INT UNSIGNED AUTO_INCREMENT NOT NULL, username VARCHAR(180) NOT NULL, roles JSON NOT NULL, password VARCHAR(255) NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL COMMENT \'(DC2Type:datetime_immutable)\', UNIQUE INDEX UNIQ_8D93D649F85E0677 (username), PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('CREATE TABLE task (id INT UNSIGNED AUTO_INCREMENT NOT NULL, user_id INT UNSIGNED NOT NULL, title VARCHAR(100) NOT NULL, description VARCHAR(255) NOT NULL, execution_day DATETIME DEFAULT NULL COMMENT \'(DC2Type:datetime_immutable)\', created_at DATETIME DEFAULT NULL COMMENT \'(DC2Type:datetime_immutable)\', status VARCHAR(10) NOT NULL CHECK ( status IN (\'new\',\'declined\',\'done\')), INDEX IDX_527EDB25A76ED395 (user_id), INDEX task_status_idx (status), PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('ALTER TABLE task ADD CONSTRAINT FK_527EDB25A76ED395 FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE');
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->abortIf($this->connection->getDatabasePlatform()->getName() !== 'mysql', 'Migration can only be executed safely on \'mysql\'.');

        $this->addSql('ALTER TABLE task DROP FOREIGN KEY FK_527EDB25A76ED395');
        $this->addSql('DROP TABLE user');
        $this->addSql('DROP TABLE task');
    }
}
```

## File: `src/Shared/Infrastructure/Type/DateTimeFormat.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Type;

interface DateTimeFormat
{
    public const DATE_FORMAT = 'Y-m-d';
    public const MYSQL_FORMAT = 'Y-m-d H:i:s';
}
```

## File: `src/Shared/Infrastructure/ValueObject/PaginatedData.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\ValueObject;

final class PaginatedData
{
    /**
     * @var array<int, mixed>
     */
    private array $data;

    private int $count;

    /**
     * @param array<int, mixed> $data
     * @param int $count
     */
    public function __construct(array $data, int $count)
    {
        $this->data = $data;
        $this->count = $count;
    }

    /**
     * @return array<int, mixed>
     */
    public function getData(): array
    {
        return $this->data;
    }

    public function getCount(): int
    {
        return $this->count;
    }
}
```

## File: `src/Shared/Infrastructure/ValueObject/Pagination.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\ValueObject;

use App\Shared\Domain\Service\Assert\Assert;
use Symfony\Component\HttpFoundation\Request;

final class Pagination
{
    public const DEFAULT_LIMIT = 50;
    public const DEFAULT_OFFSET = 0;

    public const LIMIT_NAME = 'limit';
    public const OFFSET_NAME = 'offset';

    private int $limit;

    private int $offset;

    public function __construct(int $limit = self::DEFAULT_LIMIT, int $offset = self::DEFAULT_OFFSET)
    {
        Assert::greaterThanEq($limit, 0);
        Assert::greaterThanEq($offset, 0);

        $this->limit = $limit;
        $this->offset = $offset;
    }

    public static function fromRequest(Request $request): self
    {
        $limit = $request->get(self::LIMIT_NAME, self::DEFAULT_LIMIT);
        Assert::integerish($limit);

        $offset = $request->get(self::OFFSET_NAME, self::DEFAULT_OFFSET);
        Assert::integerish($offset);

        return new self((int) $limit, (int) $offset);
    }

    public function getLimit(): int
    {
        return $this->limit;
    }

    public function getOffset(): int
    {
        return $this->offset;
    }
}
```

## File: `templates/base.html.twig`
```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}Welcome!{% endblock %}</title>
        {% block stylesheets %}{% endblock %}
    </head>
    <body>
        {% block body %}{% endblock %}
        {% block javascripts %}{% endblock %}
    </body>
</html>
```

## File: `tests/bootstrap.php`
```php
<?php

use Symfony\Component\Dotenv\Dotenv;

require dirname(__DIR__).'/vendor/autoload.php';

if (file_exists(dirname(__DIR__).'/config/bootstrap.php')) {
    require dirname(__DIR__).'/config/bootstrap.php';
} elseif (method_exists(Dotenv::class, 'bootEnv')) {
    (new Dotenv())->bootEnv(dirname(__DIR__).'/.env');
}
```

## File: `tests/Unit/Core/Application/Command/Task/CreateTask/CreateTaskCommandHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace App\Tests\Unit\Core\Application\Command\Task\CreateTask;

use App\Core\Application\Command\Task\CreateTask\CreateTaskCommand;
use App\Core\Application\Command\Task\CreateTask\CreateTaskCommandHandler;
use App\Core\Domain\Model\Task\Task;
use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use App\Core\Domain\Model\User\UniqueUsernameSpecificationInterface;
use App\Core\Domain\Model\User\User;
use App\Core\Domain\Model\User\UserFetcherInterface;
use PHPUnit\Framework\TestCase;

final class CreateTaskCommandHandlerTest extends TestCase
{
    public function test_it_creates_task_when_invoked(): void
    {
        $executionDay = (new \DateTimeImmutable())->setTime(0, 0);
        $title = 'Some title';
        $description = 'Some description';

        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->expects(self::once())
            ->method('add')
            ->with(self::callback(
                fn(Task $task): bool => $task->getTitle() === $title
                    && $task->getDescription() === $description
                    && $task->getExecutionDay() == $executionDay
            ));

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn(new User('name', 'pass_hash', $this->getUniqueUsernameSpecification()));

        $command = new CreateTaskCommand($title, $executionDay, $description);
        $handler = new CreateTaskCommandHandler($repository, $userFetcher);

        try {
            $handler($command);
        } catch (\Error $e) {
            // php7.4 fix
            if (strpos($e->getMessage(), 'id must not be accessed before initialization') === false) {
                throw $e;
            }
        }
    }

    private function getUniqueUsernameSpecification(): UniqueUsernameSpecificationInterface
    {
        $specification = $this->createMock(UniqueUsernameSpecificationInterface::class);
        $specification->method('isSatisfiedBy')->willReturn(true);

        return $specification;
    }
}
```

## File: `tests/Unit/Core/Application/Command/Task/DeleteTask/DeleteTaskCommandHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace App\Tests\Unit\Core\Application\Command\Task\DeleteTask;

use App\Core\Application\Command\Task\DeleteTask\DeleteTaskCommand;
use App\Core\Application\Command\Task\DeleteTask\DeleteTaskCommandHandler;
use App\Core\Domain\Model\Task\Task;
use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use App\Core\Domain\Model\User\User;
use App\Core\Domain\Model\User\UserFetcherInterface;
use App\Shared\Domain\Exception\AccessForbiddenException;
use App\Shared\Domain\Exception\ResourceNotFoundException;
use PHPUnit\Framework\MockObject\MockObject;
use PHPUnit\Framework\TestCase;

final class DeleteTaskCommandHandlerTest extends TestCase
{
    public function test_it_throws_exception_when_task_not_found(): void
    {
        $this->expectException(ResourceNotFoundException::class);

        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')->willReturn(null);

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($this->getUser());

        $command = new DeleteTaskCommand(1);
        $handler = new DeleteTaskCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    public function test_it_throws_exception_when_task_not_yours(): void
    {
        $this->expectException(AccessForbiddenException::class);

        $user = $this->createMock(User::class);
        $user->method('equals')->willReturn(false);

        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')->willReturn(new Task('title', new \DateTimeImmutable(), $user));

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($user);

        $command = new DeleteTaskCommand(1);
        $handler = new DeleteTaskCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    public function test_it_deletes_when_invoked(): void
    {
        $title = 'Some title';
        $executionDay = (new \DateTimeImmutable())->setTime(0, 0);
        $description = 'Some description';

        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')->willReturn(new Task($title, $executionDay, $this->getUser(), $description));
        $repository->expects(self::once())
            ->method('remove')
            ->with(self::callback(
                fn(Task $task): bool => $task->getTitle() === $title
                    && $task->getDescription() === $description
                    && $task->getExecutionDay() == $executionDay
            ));

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($this->getUser());

        $command = new DeleteTaskCommand(1);
        $handler = new DeleteTaskCommandHandler($repository, $userFetcher);
        $handler($command);
    }

    /**
     * @return User|MockObject
     */
    private function getUser(): MockObject
    {
        $user = $this->createMock(User::class);
        $user->method('equals')->willReturn(true);

        return $user;
    }
}
```

## File: `tests/Unit/Core/Application/Command/Task/MakeTaskDeclined/MakeTaskDeclinedCommandHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace App\Tests\Unit\Core\Application\Command\Task\MakeTaskDeclined;

use App\Core\Application\Command\Task\MakeTaskDeclined\MakeTaskDeclinedCommand;
use App\Core\Application\Command\Task\MakeTaskDeclined\MakeTaskDeclinedCommandHandler;
use App\Core\Domain\Model\Task\Status;
use App\Core\Domain\Model\Task\Task;
use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use App\Core\Domain\Model\User\User;
use App\Core\Domain\Model\User\UserFetcherInterface;
use App\Shared\Domain\Exception\AccessForbiddenException;
use App\Shared\Domain\Exception\ResourceNotFoundException;
use PHPUnit\Framework\MockObject\MockObject;
use PHPUnit\Framework\TestCase;

final class MakeTaskDeclinedCommandHandlerTest extends TestCase
{
    public function test_it_throws_exception_when_task_not_found(): void
    {
        $this->expectException(ResourceNotFoundException::class);

        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')->willReturn(null);

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($this->getUser());

        $command = new MakeTaskDeclinedCommand(1);
        $handler = new MakeTaskDeclinedCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    public function test_it_throws_exception_when_task_not_yours(): void
    {
        $this->expectException(AccessForbiddenException::class);

        $user = $this->createMock(User::class);
        $user->method('equals')->willReturn(false);

        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')->willReturn(new Task('title', new \DateTimeImmutable(), $user));

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($user);

        $command = new MakeTaskDeclinedCommand(1);
        $handler = new MakeTaskDeclinedCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    public function test_it_make_task_declined_when_invoked(): void
    {
        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')
            ->willReturn(new Task('title', new \DateTimeImmutable(), $this->getUser()));
        $repository->expects(self::once())
            ->method('add')
            ->with(self::callback(fn(Task $task): bool => $task->getStatus()->is(Status::DECLINED)));

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($this->getUser());

        $command = new MakeTaskDeclinedCommand(1);
        $handler = new MakeTaskDeclinedCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    /**
     * @return User|MockObject
     */
    private function getUser(): MockObject
    {
        $user = $this->createMock(User::class);
        $user->method('equals')->willReturn(true);

        return $user;
    }
}
```

## File: `tests/Unit/Core/Application/Command/Task/MakeTaskDone/MakeTaskDoneCommandHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace App\Tests\Unit\Core\Application\Command\Task\MakeTaskDone;

use App\Core\Application\Command\Task\MakeTaskDone\MakeTaskDoneCommand;
use App\Core\Application\Command\Task\MakeTaskDone\MakeTaskDoneCommandHandler;
use App\Core\Domain\Model\Task\Status;
use App\Core\Domain\Model\Task\Task;
use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use App\Core\Domain\Model\User\User;
use App\Core\Domain\Model\User\UserFetcherInterface;
use App\Shared\Domain\Exception\AccessForbiddenException;
use App\Shared\Domain\Exception\ResourceNotFoundException;
use PHPUnit\Framework\MockObject\MockObject;
use PHPUnit\Framework\TestCase;

final class MakeTaskDoneCommandHandlerTest extends TestCase
{
    public function test_it_throws_exception_when_task_not_found(): void
    {
        $this->expectException(ResourceNotFoundException::class);

        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')->willReturn(null);

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($this->getUser());

        $command = new MakeTaskDoneCommand(1);
        $handler = new MakeTaskDoneCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    public function test_it_throws_exception_when_task_not_yours(): void
    {
        $this->expectException(AccessForbiddenException::class);

        $user = $this->createMock(User::class);
        $user->method('equals')->willReturn(false);

        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')->willReturn(new Task('title', new \DateTimeImmutable(), $user));

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($user);

        $command = new MakeTaskDoneCommand(1);
        $handler = new MakeTaskDoneCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    public function test_it_make_task_declined_when_invoked(): void
    {
        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')
            ->willReturn(new Task('title', new \DateTimeImmutable(), $this->getUser()));
        $repository->expects(self::once())
            ->method('add')
            ->with(self::callback(fn(Task $task): bool => $task->getStatus()->is(Status::DONE)));

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($this->getUser());

        $command = new MakeTaskDoneCommand(1);
        $handler = new MakeTaskDoneCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    /**
     * @return User|MockObject
     */
    private function getUser(): MockObject
    {
        $user = $this->createMock(User::class);
        $user->method('equals')->willReturn(true);

        return $user;
    }
}
```

## File: `tests/Unit/Core/Application/Command/Task/UpdateTask/UpdateTaskCommandHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace App\Tests\Unit\Core\Application\Command\Task\UpdateTask;

use App\Core\Application\Command\Task\UpdateTask\UpdateTaskCommand;
use App\Core\Application\Command\Task\UpdateTask\UpdateTaskCommandHandler;
use App\Core\Domain\Model\Task\Task;
use App\Core\Domain\Model\Task\TaskRepositoryInterface;
use App\Core\Domain\Model\User\User;
use App\Core\Domain\Model\User\UserFetcherInterface;
use App\Shared\Domain\Exception\AccessForbiddenException;
use App\Shared\Domain\Exception\ResourceNotFoundException;
use PHPUnit\Framework\MockObject\MockObject;
use PHPUnit\Framework\TestCase;

final class UpdateTaskCommandHandlerTest extends TestCase
{
    public function test_it_throws_exception_when_task_not_found(): void
    {
        $this->expectException(ResourceNotFoundException::class);

        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')->willReturn(null);

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($this->getUser());

        $command = new UpdateTaskCommand(1, 'title', new \DateTimeImmutable());
        $handler = new UpdateTaskCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    public function test_it_throws_exception_when_task_not_yours(): void
    {
        $this->expectException(AccessForbiddenException::class);

        $user = $this->createMock(User::class);
        $user->method('equals')->willReturn(false);

        $repository = $this->createMock(TaskRepositoryInterface::class);
        $repository->method('find')->willReturn(new Task('title', new \DateTimeImmutable(), $user));

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($user);

        $command = new UpdateTaskCommand(1, 'title', new \DateTimeImmutable());
        $handler = new UpdateTaskCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    public function test_it_update_task_when_invoked(): void
    {
        $newTitle = 'new title';
        $newDescription = 'new description';
        $newExecutionDay = (new \DateTimeImmutable())->setTime(0, 0)->modify('+2 days');

        $repository = $this->createMock(TaskRepositoryInterface::class);

        $repository->method('find')
            ->willReturn(new Task('title', new \DateTimeImmutable(), $this->getUser()));

        $repository->expects(self::once())
            ->method('add')
            ->with(self::callback(fn(Task $task): bool =>
                $task->getTitle() === $newTitle
                && $task->getDescription() === $newDescription
                && $task->getExecutionDay() == $newExecutionDay
            ));

        $userFetcher = $this->createMock(UserFetcherInterface::class);
        $userFetcher->method('fetchRequiredUser')->willReturn($this->getUser());

        $command = new UpdateTaskCommand(1, $newTitle, $newExecutionDay, $newDescription);
        $handler = new UpdateTaskCommandHandler($repository, $userFetcher);

        $handler($command);
    }

    /**
     * @return User|MockObject
     */
    private function getUser(): MockObject
    {
        $user = $this->createMock(User::class);
        $user->method('equals')->willReturn(true);

        return $user;
    }
}
```

## File: `tests/Unit/Core/Domain/Model/Task/StatusTest.php`
```php
<?php

declare(strict_types=1);

namespace App\Tests\Unit\Core\Domain\Model\Task;

use App\Core\Domain\Model\Task\Status;
use App\Shared\Domain\Exception\InvalidInputDataException;
use PHPUnit\Framework\TestCase;

final class StatusTest extends TestCase
{
    public function test_it_throws_exception_when_invalid_value_set(): void
    {
        $this->expectException(InvalidInputDataException::class);
        $this->expectDeprecationMessageMatches('/Status value should be one of/');

        new Status('some_invalid_status');
    }

    /**
     * @doesNotPerformAssertions
     */
    public function test_it_ok_when_valid_value_set(): void
    {
        foreach (Status::VALID_STATUSES as $status) {
            new Status($status);
        }
    }
}
```

## File: `tests/Unit/Core/Domain/Model/Task/TaskTest.php`
```php
<?php

declare(strict_types=1);

namespace App\Tests\Unit\Core\Domain\Model\Task;

use App\Core\Domain\Model\Task\Status;
use App\Core\Domain\Model\Task\Task;
use App\Core\Domain\Model\Task\TaskCreatedEvent;
use App\Core\Domain\Model\Task\TaskDeclinedEvent;
use App\Core\Domain\Model\Task\TaskDoneEvent;
use App\Core\Domain\Model\User\UniqueUsernameSpecificationInterface;
use App\Core\Domain\Model\User\User;
use App\Shared\Domain\Exception\BusinessLogicViolationException;
use App\Shared\Domain\Exception\InvalidInputDataException;
use PHPUnit\Framework\TestCase;

final class TaskTest extends TestCase
{
    public function test_it_throws_exception_when_task_created_and_title_too_short(): void
    {
        new Task($this->getShortTitle(), new \DateTimeImmutable(), $this->getUser());
    }

    public function test_it_throws_exception_when_title_changed_and_title_too_short(): void
    {
        $task = $this->getTask();
        $task->changeTitle($this->getShortTitle());
    }

    public function test_it_throws_exception_when_task_created_and_title_too_long(): void
    {
        new Task($this->getLongTitle(), new \DateTimeImmutable(), $this->getUser());
    }

    public function test_it_throws_exception_when_title_changed_and_title_too_long(): void
    {
        $task = $this->getTask();
        $task->changeTitle($this->getLongTitle());
    }

    public function test_it_throws_exception_when_title_changed_and_description_too_long(): void
    {
        new Task(str_repeat('x', Task::MAX_TITLE_LENGTH), new \DateTimeImmutable(), $this->getUser(), $this->getLongDescription());
    }

    public function test_it_throws_exception_when_description_changed_and_description_too_long(): void
    {
        $task = $this->getTask();
        $task->changeDescription($this->getLongDescription());
    }

    public function test_it_throws_exception_when_created_and_execution_time_in_past(): void
    {
        $this->expectException(InvalidInputDataException::class);
        $this->expectExceptionMessage('Execution day should be not in past');

        new Task('title', (new \DateTimeImmutable())->modify('-1 day'), $this->getUser());
    }

    public function test_it_throws_exception_when_changed_and_execution_time_in_past(): void
    {
        $this->expectException(InvalidInputDataException::class);
        $this->expectExceptionMessage('Execution day should be not in past');

        $task = $this->getTask();
        $task->changeExecutionDay((new \DateTimeImmutable())->modify('-1 day'));
    }

    /**
     * @doesNotPerformAssertions
     */
    public function test_it_ok_when_valid_values_set(): void
    {
        $task = new Task(str_repeat('x', Task::MAX_TITLE_LENGTH), new \DateTimeImmutable(), $this->getUser(), str_repeat('x', Task::MAX_DESCRIPTION_LENGTH));

        $task->changeTitle(str_repeat('y', Task::MAX_TITLE_LENGTH));
        $task->changeDescription(str_repeat('y', Task::MAX_DESCRIPTION_LENGTH));
    }

    public function test_it_creates_new_status_when_task_is_created(): void
    {
        $task = $this->getTask();
        self::assertTrue($task->getStatus()->is(Status::NEW));
    }

    public function test_it_throws_exception_when_done_declined_task(): void
    {
        $this->expectException(BusinessLogicViolationException::class);
        $this->expectExceptionMessage('Declined task can\'t be done');

        $task = $this->getTask();
        $task->decline();
        self::assertTrue($task->getStatus()->is(Status::DECLINED));
        $task->done();
    }

    public function test_it_throws_exception_when_decline_done_task(): void
    {
        $this->expectException(BusinessLogicViolationException::class);
        $this->expectExceptionMessage('Done task can\'t be declined');

        $task = $this->getTask();
        $task->done();
        self::assertTrue($task->getStatus()->is(Status::DONE));
        $task->decline();
    }

    public function test_it_raises_event_when_task_created(): void
    {
        $task = $this->getTask();
        $events = $task->popEvents();

        self::assertContainsEquals(new TaskCreatedEvent($task), $events);
    }

    public function test_it_raises_event_when_task_becomes_done(): void
    {
        $task = $this->getTask();
        $task->done();
        $events = $task->popEvents();

        self::assertContainsEquals(new TaskDoneEvent($task), $events);
    }

    public function test_it_raises_event_when_task_becomes_declined(): void
    {
        $task = $this->getTask();
        $task->decline();
        $events = $task->popEvents();

        self::assertContainsEquals(new TaskDeclinedEvent($task), $events);
    }

    private function getTask(): Task
    {
        return new Task(str_repeat('x', Task::MAX_TITLE_LENGTH), new \DateTimeImmutable(), $this->getUser());
    }

    private function getShortTitle(): string
    {
        $this->expectException(InvalidInputDataException::class);
        $this->expectDeprecationMessageMatches('/Title should contain at least/');

        return str_repeat('x', Task::MIN_TITLE_LENGTH - 1);
    }

    private function getLongTitle(): string
    {
        $this->expectException(InvalidInputDataException::class);
        $this->expectDeprecationMessageMatches('/Title should contain at most/');

        return str_repeat('x', Task::MAX_TITLE_LENGTH +1);
    }

    private function getLongDescription(): string
    {
        $this->expectException(InvalidInputDataException::class);
        $this->expectDeprecationMessageMatches('/Description should contain at most/');

        return str_repeat('x', Task::MAX_DESCRIPTION_LENGTH + 1);
    }

    private function getUser(): User
    {
        $specification = $this->createMock(UniqueUsernameSpecificationInterface::class);
        $specification->method('isSatisfiedBy')->willReturn(true);

        return new User('Test', 'pass_hash', $specification);
    }
}
```

## File: `tests/Unit/Core/Domain/Model/User/UserTest.php`
```php
<?php

declare(strict_types=1);

namespace App\Tests\Unit\Core\Domain\Model\User;

use App\Core\Domain\Model\User\UniqueUsernameSpecificationInterface;
use App\Core\Domain\Model\User\User;
use App\Shared\Domain\Exception\InvalidInputDataException;
use PHPUnit\Framework\TestCase;

final class UserTest extends TestCase
{
    public function test_it_throws_exception_when_password_to_long(): void
    {
        $this->expectException(InvalidInputDataException::class);
        $this->expectDeprecationMessageMatches('/Password should contain at most/');

        new User('admin', str_repeat('x', User::MAX_PASSWORD_LENGTH + 1), $this->getUniqueUsernameSpecification());
    }

    public function test_it_return_false_when_users_are_not_equals(): void
    {
        $userOne = new User('admin', 'some_hash', $this->getUniqueUsernameSpecification());
        $userTwo = new User('admin', 'some_hash', $this->getUniqueUsernameSpecification());
        $userThree = new User('admin', 'some_hash', $this->getUniqueUsernameSpecification());

        $this->setUserId($userOne, 1);
        $this->setUserId($userTwo, 2);
        $this->setUserId($userThree, 1);

        self::assertFalse($userOne->equals($userTwo));
        self::assertTrue($userOne->equals($userThree));
    }

    public function test_it_throws_exception_when_username_to_long(): void
    {
        $this->expectException(InvalidInputDataException::class);
        $this->expectDeprecationMessageMatches('/Username should contain at most/');

        new User(str_repeat('x', User::MAX_USER_NAME_LENGTH + 1), 'some_hash', $this->getUniqueUsernameSpecification());
    }

    public function test_it_creates_default_role_user(): void
    {
        $user = new User('admin', 'some_hash', $this->getUniqueUsernameSpecification());

        self::assertContains(User::DEFAULT_USER_ROLE, $user->getRoles());

        $user = new User('admin', 'some_hash', $this->getUniqueUsernameSpecification(), ['ROLE_ADMIN']);

        self::assertContains(User::DEFAULT_USER_ROLE, $user->getRoles());
    }

    /**
     * @doesNotPerformAssertions
     */
    public function test_it_ok_when_valid_values_set(): void
    {
        new User(str_repeat('x', User::MAX_USER_NAME_LENGTH), str_repeat('x', User::MAX_PASSWORD_LENGTH), $this->getUniqueUsernameSpecification());
    }

    private function setUserId(User $user, int $id): void
    {
        $reflection = new \ReflectionClass($user);
        $property = $reflection->getProperty('id');
        $property->setAccessible(true);
        $property->setValue($user, $id);
    }

    private function getUniqueUsernameSpecification(): UniqueUsernameSpecificationInterface
    {
        $specification = $this->createMock(UniqueUsernameSpecificationInterface::class);
        $specification->method('isSatisfiedBy')->willReturn(true);

        return $specification;
    }
}
```

