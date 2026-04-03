---
id: github.com-angelod2022-jsxer-f00ff500-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:30.467453
---

# KNOWLEDGE EXTRACT: github.com_AngeloD2022_jsxer_f00ff500
> **Extracted on:** 2026-04-01 16:50:17
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007525359/github.com_AngeloD2022_jsxer_f00ff500

---

## File: `.gitignore`
```
/.vs/
/.vscode/
/.idea/
/.history/
/bin/
/dist/
/node_modules/
/build/
/cmake-build-debug/
/cmake-build-release/
/cmake-build-*/

node_modules/

.DS_Store
```

## File: `CMakeLists.txt`
```
cmake_minimum_required(VERSION 3.26)

project(Jsxer)

# using c++17 to use some modern features of c++
set(CMAKE_CXX_STANDARD 17)

include(FetchContent)

# Needed to print downloading progress
Set(FETCHCONTENT_QUIET FALSE)

# string formatting
FetchContent_Declare(fmt
    GIT_REPOSITORY https://github.com/fmtlib/fmt.git
    GIT_TAG 9.1.0
    GIT_PROGRESS TRUE
)
FetchContent_MakeAvailable(fmt)

# logger
FetchContent_Declare(plog
    GIT_REPOSITORY https://github.com/SergiusTheBest/plog.git
    GIT_TAG 1.1.9
    GIT_PROGRESS TRUE
)
FetchContent_MakeAvailable(plog)

# cli parser
FetchContent_Declare(cli11
    GIT_REPOSITORY https://github.com/CLIUtils/CLI11.git
    GIT_TAG v2.3.2
    GIT_PROGRESS TRUE
)
FetchContent_MakeAvailable(cli11)

# utils

file(STRINGS "VERSION" JSXER_VERSION)

message("${PROJECT_NAME} v${JSXER_VERSION}")

set(JSXER_SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/src)
set(JSXER_INCLUDE_DIR ${CMAKE_CURRENT_LIST_DIR}/include)

string(TOLOWER "${CMAKE_BUILD_TYPE}" BUILD_TYPE)

message("Build: " "${CMAKE_BUILD_TYPE}")

if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    set(BUILD_ARCH "64-bit")
else()
    set(BUILD_ARCH "32-bit")
endif()

message("System Architecture: " "${CMAKE_SYSTEM_PROCESSOR}")
message("System Bitness: " "${BUILD_ARCH}")

if(MSVC OR MSYS OR MINGW)
    # for detecting Windows compilers
    set(BUILD_PLATFORM "Windows")

    set(BIN_CLI_EXT ".exe")
    set(BIN_DLL_EXT ".dll")
    set(BIN_LIB_EXT ".lib")
elseif(UNIX AND NOT APPLE)
    # for Linux, BSD, Solaris, Minix
    set(BUILD_PLATFORM "Linux")

    set(BIN_CLI_EXT "")
    set(BIN_DLL_EXT ".so")
    set(BIN_LIB_EXT ".a")
elseif(APPLE)
    # for MacOS X or iOS, watchOS, tvOS (since 3.10.3)
    set(BUILD_PLATFORM "Darwin")

    set(BIN_CLI_EXT "")
    set(BIN_DLL_EXT ".dylib")
    set(BIN_LIB_EXT ".a")
else()
    message(FATAL_ERROR "Unknown platform!, CMake will exit.")
endif()

message("Platform: " "${BUILD_PLATFORM}")

if(BUILD_TYPE STREQUAL "debug")
    set(BIN_OUT_DIR ${PROJECT_SOURCE_DIR}/bin/debug)
else()
    set(BIN_OUT_DIR ${PROJECT_SOURCE_DIR}/bin/release)
endif()

set(LIB_OUT_DIR ${BIN_OUT_DIR}/static)
set(DLL_OUT_DIR ${BIN_OUT_DIR}/dll)

message("Bin directory: " "${BIN_OUT_DIR}")
message("Lib directory: " "${LIB_OUT_DIR}")
message("Dll directory: " "${DLL_OUT_DIR}")

set(BIN_CLI_NAME "jsxer")
set(BIN_DLL_NAME "lib-jsxer")
set(BIN_LIB_NAME "libjsxer")

# Static lib
set(JSXER_CORE_TARGET jsxer-core)

file(GLOB_RECURSE JSXER_CORE_HEADERS
    ${JSXER_SOURCE_DIR}/jsxer/*.h
    ${JSXER_SOURCE_DIR}/jsxer/*.hpp
)

file(GLOB_RECURSE JSXER_CORE_SOURCES
    ${JSXER_SOURCE_DIR}/jsxer/*.c
    ${JSXER_SOURCE_DIR}/jsxer/*.cpp
)

add_library(${JSXER_CORE_TARGET} STATIC ${JSXER_CORE_HEADERS} ${JSXER_CORE_SOURCES})

target_include_directories(${JSXER_CORE_TARGET} PUBLIC ${JSXER_INCLUDE_DIR})

target_link_libraries(${JSXER_CORE_TARGET} PRIVATE
        fmt::fmt
        plog::plog
        )

target_compile_definitions(${JSXER_CORE_TARGET} PUBLIC
    CONFIG_VERSION="${JSXER_VERSION}"
)

set_target_properties(${JSXER_CORE_TARGET} PROPERTIES
    PREFIX ""
    SUFFIX "${BIN_LIB_EXT}"
    OUTPUT_NAME "${BIN_LIB_NAME}"
    LIBRARY_OUTPUT_DIRECTORY ${LIB_OUT_DIR}
    ARCHIVE_OUTPUT_DIRECTORY ${LIB_OUT_DIR}
    RUNTIME_OUTPUT_DIRECTORY ${LIB_OUT_DIR}
)

# Dynamic link library
set(JSXER_DLL_TARGET jsxer-dll)

file(GLOB_RECURSE JSXER_DLL_HEADERS
    ${JSXER_SOURCE_DIR}/dll/*.h
    ${JSXER_SOURCE_DIR}/dll/*.hpp
)

file(GLOB_RECURSE JSXER_DLL_SOURCES
    ${JSXER_SOURCE_DIR}/dll/*.c
    ${JSXER_SOURCE_DIR}/dll/*.cpp
)

add_library(${JSXER_DLL_TARGET} SHARED ${JSXER_DLL_HEADERS} ${JSXER_DLL_SOURCES})

target_link_libraries(${JSXER_DLL_TARGET} PRIVATE ${JSXER_CORE_TARGET}
        fmt::fmt
        plog::plog)

target_compile_definitions(${JSXER_DLL_TARGET} PUBLIC
    CONFIG_VERSION="${JSXER_VERSION}"
)

set_target_properties(${JSXER_DLL_TARGET} PROPERTIES
    PREFIX ""
    SUFFIX "${BIN_DLL_EXT}"
    OUTPUT_NAME "${BIN_DLL_NAME}"
    RUNTIME_OUTPUT_DIRECTORY ${DLL_OUT_DIR}
    ARCHIVE_OUTPUT_DIRECTORY ${DLL_OUT_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${DLL_OUT_DIR}
)

# CLI
set(JSXER_CLI_TARGET jsxer-cli)

file(GLOB_RECURSE JSXER_CLI_HEADERS
    ${JSXER_SOURCE_DIR}/cli/*.h
    ${JSXER_SOURCE_DIR}/cli/*.hpp
)

file(GLOB_RECURSE JSXER_CLI_SOURCES
    ${JSXER_SOURCE_DIR}/cli/*.c
    ${JSXER_SOURCE_DIR}/cli/*.cpp
)

add_executable(${JSXER_CLI_TARGET} ${JSXER_CLI_HEADERS} ${JSXER_CLI_SOURCES})

target_link_libraries(${JSXER_CLI_TARGET} PRIVATE ${JSXER_CORE_TARGET}
        fmt::fmt
        plog::plog
        CLI11::CLI11
        )

target_compile_definitions(${JSXER_CLI_TARGET} PUBLIC
    CONFIG_VERSION="${JSXER_VERSION}"
)

set_target_properties(${JSXER_CLI_TARGET} PROPERTIES
    PREFIX ""
    SUFFIX "${BIN_CLI_EXT}"
    OUTPUT_NAME "${BIN_CLI_NAME}"
    RUNTIME_OUTPUT_DIRECTORY ${BIN_OUT_DIR}
    ARCHIVE_OUTPUT_DIRECTORY ${BIN_OUT_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${BIN_OUT_DIR}
)

enable_testing()

set(JSXER_TESTS_DIR ${CMAKE_CURRENT_LIST_DIR}/tests)

set(JSXER_TESTS_SRC_DIR ${JSXER_TESTS_DIR}/src)
set(JSXER_TESTS_DATA_DIR ${JSXER_TESTS_DIR}/data)

add_executable(jsxer-test-array-expr ${JSXER_TESTS_SRC_DIR}/array-expr.cpp)
target_link_libraries(jsxer-test-array-expr PRIVATE ${JSXER_CORE_TARGET})

add_test("ArrayExpression" jsxer-test-array-expr)

add_executable(jsxer-test-obj-expr ${JSXER_TESTS_SRC_DIR}/obj-expr.cpp)
target_link_libraries(jsxer-test-obj-expr PRIVATE ${JSXER_CORE_TARGET})

add_test("ObjectExpression" jsxer-test-obj-expr)

add_executable(jsxer-test-member-expr ${JSXER_TESTS_SRC_DIR}/member-expr.cpp)
target_link_libraries(jsxer-test-member-expr PRIVATE ${JSXER_CORE_TARGET})

add_test("MemberExpression" jsxer-test-member-expr)

add_executable(jsxer-test-for-stmt ${JSXER_TESTS_SRC_DIR}/for-stmt.cpp)
target_link_libraries(jsxer-test-for-stmt PRIVATE ${JSXER_CORE_TARGET})

add_test("ForStatement" jsxer-test-for-stmt)
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing

Please ensure that your code is tested comprehensively with many inputs before merging or submitting a pull request. 

**Decompilers are intricate software; please be mindful of the changes you make! :)**

Thanks!
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

## File: `README.md`
```markdown
# Jsxer
A faster decompiler for Adobe's (Legacy) ExtendScript binary format (*.jsxbin).

> [!WARNING]
> This project is currently being rewritten in Rust. Development is occurring on the `rust-rewrite` branch.

## Features
* [x] Lifts JSXBIN back to JavaScript code.
* [x] Jsxblind deobfuscation (experimental).
* [x] Python bindings.
* [x] Dynamic library.
* [x] **Fast as hell.**

## What is ExtendScript?
ExtendScript is a scripting language and an associated toolkit developed by Adobe Systems, intended for use with Creative Suite and Technical Communication Suite products. It is a dialect of the ECMAScript 3 standard and therefore similar to JavaScript and ActionScript. The toolkit comes bundled with Creative Suite and Technical Communication Suite editions and can access tools within applications like Photoshop, FrameMaker, InDesign or After Effects for batch-processing projects.

## Please, do not use this project unethically.

#### yo, pirates, hear me out...

Look, I get that it's tempting– money doesn't grow on trees.

Many script authors are independent developers, and by stealing their work you make what they do unsustainable and their lives harder. Without income, they are not able to create and maintain what many people may depend on.  

Jsxer (in addition to simply being a fun and educational project to develop) was made for source code recovery and security research purposes. It is free and open-source software– and as such, I won't try to control what you can and can't do with it. 

Just remember that script authors are real humans! So if you like their work, show some love and fork over the dough. :)

Appreciate ya!

## Build (MacOS)

### [Video Tutorial](https://www.youtube.com/watch?v=939Bo5iTxo0)

Open the Terminal app to run the following commands. If you are unfamiliar with Terminal, you can find it in /Applications/Utilities/Terminal.app.

*Install CMake:*
```bash
brew install cmake
```

*Configure and build the project:*
```bash
cmake .
cmake --build . --config release 
```

*After a successful build, navigate to the folder with the executable:*
```bash
cd ./bin/release/
```

## Usage

> [!IMPORTANT]
> Make sure that the input file only contains the JSXBIN literal itself.<sup><a href="https://youtu.be/939Bo5iTxo0?lc=UgyPDxgsuRmbfd8MI-F4AaABAg.9gIEl4rxFVa9gIFW1EPzqO">\[1\]</a></sup>&ensp;(Usually starting with `@JSXBIN@`)

```bash
jsxer <jsxbin path>
```

The `--unblind` flag enables the experimental deobfuscation.

## Credits
  - Thanks to Andrin Meier ([@andrinpricemeier](https://github.com/andrinpricemeier), formerly `@autoboosh`) for his research on the format, and his project [jsxbin-to-jsx-converter](https://github.com/autoboosh/jsxbin-to-jsx-converter).
  - Thanks to [@codecopy](https://github.com/codecopy) for keeping a [fork](https://github.com/codecopy/jsxbin-to-jsx-converter) of `@autoboosh`'s project, where the original vanished as a consequence of a DMCA takedown from Adobe.


## Contributions
Contributions are welcome. Open an issue if you have a problem. Check contribution guidelines [here](CONTRIBUTING.md).

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AngeloD2022/jsxer&type=Date)](https://star-history.com/#AngeloD2022/jsxer&Date)

```

## File: `TODO.md`
```markdown
## TODO

- [ ] Implement an Utf-16 ES native String class (Currently it has a temporary u16 vector solution).
- [ ] Fix function argument list sequence.
- [ ] Fix declarations using comma expressions.
- [ ] Fix Number printer (double dumping as exactly in es/js).
- [ ] Add test data and tests (ctest or google test).
- [ ] Better error handling and cross-platform support.
- [ ] Use operators for ast parsing.
- [ ] CodeGen with proper syntax and formatting.
- [ ] Add code documentation and setup wiki page.
- [ ] Add GitHub actions for building, testing and releases (CI/CD).
- [ ] Research the XML nodes a bit more, as some of them are producing improper code.
```

## File: `VERSION`
```
1.7.4
```

## File: `bindings/python/decompiler.py`
```python
import logging
import platform
from os import path
from ctypes import CDLL, POINTER, c_int, c_char_p, c_size_t, c_bool, byref, create_string_buffer

logger = logging.getLogger(__file__)


def _get_binding_path():
    pf = platform.system().lower()

    for build_type in ('release', 'debug',):
        _binding_base_path = path.realpath(
            path.join(
                path.dirname(__file__),
                '..',
                '..',
                'bin',
                build_type,
                'dll',
            )
        )

        if pf == 'windows':
            _binding_lib_path = path.join(_binding_base_path, 'lib-jsxer.dll')
        elif pf == 'linux':
            _binding_lib_path = path.join(_binding_base_path, 'lib-jsxer.so')
        elif pf == 'darwin':
            _binding_lib_path = path.join(_binding_base_path, 'lib-jsxer.dylib')
        else:
            raise EnvironmentError(f'Unknown platform: {pf}')

        logger.debug(f'Searching for Backend lib at: {_binding_lib_path}')

        if path.isfile(_binding_lib_path):
            logger.debug(f'Backend lib found at: {_binding_lib_path}')
            return _binding_lib_path
    else:
        raise FileNotFoundError(f'Backend lib not found!')


"""
int decompile(const char* input, size_t in_len, char* output, size_t* out_len, bool unblind = false)
"""
_backend = CDLL(_get_binding_path())
_decompile = _backend.decompile
_decompile.argtypes = [
    c_char_p,
    c_size_t,
    c_char_p,
    POINTER(c_size_t),
    c_bool
]
_decompile.restype = c_int


def decompile(compiled: str, unblind=False):
    out_size = c_size_t(0)

    # determine the output buffer size
    ec = _decompile(
        compiled.encode('utf-8'),
        len(compiled),
        c_char_p(0),
        byref(out_size),
        c_bool(unblind)
    )

    if ec == 0:
        if out_size.value > 0:
            out_size = c_size_t(int(out_size.value) + 1)
            out_str = create_string_buffer(out_size.value)

            # now decompile with enough allocated output buffer
            ec = _decompile(
                compiled.encode('utf-8'),
                len(compiled),
                out_str,
                byref(out_size),
                c_bool(unblind)
            )

            if ec != 0:
                raise Exception(f'decompile() failed with code: {ec}')

            return out_str.value.decode('utf-8')
        return ''

    raise Exception(f'decompile() failed with code: {ec}')


if __name__ == '__main__':
    print(
        decompile("""@JSXBIN@ES@2.0@MyBbyBn0ACJAnABjzBjYBfneB2nfnffJBnAEXzIjUjPiTjUjSjJjOjHCfEXzKjDjI
jBjSiDjPjEjFiBjUDfjBfRBFdAffRBFdQff0DzAEByB""")
    )
```

## File: `include/jsxer.h`
```c
#pragma once

#include <string>
#include <cstdint>

#ifndef CONFIG_VERSION
    #define CONFIG_VERSION "0.0.0"
#endif

using std::string;

enum class JsxbinVersion : uint16_t {
    Invalid = (uint16_t) -1,

    v10 = 0x0100,
    v20 = 0x0200,
    v21 = 0x0201,
};

namespace jsxer {
    int decompile(const string& input, string& output, bool unblind = false);

    int decompile_test(const string& input, string& output, bool unblind = false);
}
```

## File: `src/cli/main.cpp`
```cpp
#include <string>
#include <iostream>
#include <filesystem>

#include <CLI/App.hpp>
#include <CLI/Formatter.hpp>    // DON'T remove
#include <CLI/Config.hpp>       // DON'T remove

#include <jsxer.h>

#include "./utils.h"

namespace fs = std::filesystem;

int main(int argc, char* argv[]) {
    CLI::App cli{
        "JSXER - A fast and accurate JSXBIN decompiler.\n"
        "Written by Angelo DeLuca and contributors.\n",
    };
    cli.set_version_flag("-v,--version", CONFIG_VERSION);

    // cli flag variables
    bool unblind = false;
//    bool verbose = false;
    std::string input;
    std::string output;

    // cli building
    auto output_option = cli.add_option("-o,--output",
                   output,
                   "Output path for the decompiled file");
    cli.add_flag("-b,--unblind",
                   unblind,
                   "Try renaming symbols which are obfuscated by 'JsxBlind' (experimental)");
//    cli.add_flag("-v,--verbose",
//                   verbose,
//                   "Display verbose log");

    cli.add_option("input",
                   input,
                   "Name of file to read"
    )->check(CLI::ExistingFile)->required();

    // cli parsing
    try {
        cli.parse(argc, argv);
    } catch(const CLI::ParseError &e) {
        return cli.exit(e);
    }

    // process
    auto input_path = fs::path(input);

    fs::path output_path = !bool(*output_option)
        ? input_path.parent_path() / (input_path.stem().string() + ".jsx")
        : fs::path(output);

    if (!bool(*output_option) && fs::exists(output_path.parent_path())) {
        fs::create_directories(output_path.parent_path());
    }

    // read in the JSXBIN file contents...
    auto contents = utils::ReadFileContents(input_path);
    auto contents_str = std::string(contents.begin(), contents.end());

    // begin de-compilation...
    std::string decompiled;
    std::cout << "[i] Decompiling..." << std::endl;
    jsxer::decompile(contents_str, decompiled, unblind);
    std::cout << "[i] Finished." << std::endl;

    utils::WriteFileContents(output_path, decompiled);

    return 0;
}
```

## File: `src/cli/utils.h`
```c
#include <filesystem>
#include <fstream>
#include <string>
#include <iterator>

namespace fs = std::filesystem;

namespace utils {
    std::vector<unsigned char> ReadFileContents(const fs::path& path) {
        //  std::ios::binary    -> makes it read as binary
        std::ifstream f(path, std::ios::binary);

        // Stop eating new lines in binary mode!!!
        f.unsetf(std::ios::skipws);

        // move cursor to start
        f.seekg(0, std::ios::beg);

        return {
            std::istream_iterator<unsigned char>(f),
            std::istream_iterator<unsigned char>()
        };
    }

    size_t WriteFileContents(const fs::path& path, const std::string& contents) {
        //  std::ios::binary    -> makes it read as binary
        std::ofstream f(path);

        // move cursor to start
        f << contents;
        f.close();

        return contents.size();
    }
}
```

## File: `src/dll/library.cpp`
```cpp
#include "library.h"

#include <cstring>

int decompile(const char* input, size_t in_len, char* output, size_t* out_len, bool unblind) {
    std::string compiled(input, in_len), decompiled;

    int err = jsxer::decompile(compiled, decompiled, unblind);

    if (err != 0) {
        if (output) {
            *output = '\0';
        }
        if (out_len) {
            *out_len = 0;
        }
        return err;
    }

    if (out_len) {
        if (output) {
            if ((decompiled.length() + 1) > *out_len) {
                return 1;
            }

            memset(output, '\0', *out_len);
            memcpy(output, decompiled.c_str(), decompiled.length());
        }

        *out_len = decompiled.length();
    }

    return 0;
}
```

## File: `src/dll/library.h`
```c
#pragma once

#include "jsxer.h"

#include <string>

#ifdef _WIN32
    #define ESD_PUBLIC_API __declspec(dllexport)
#elif defined(__GNUC__)
    #if __GNUC__ >= 4
        #define ESD_PUBLIC_API __attribute__ ((visibility ("default")))
    #else
        #define ESD_PUBLIC_API __attribute__ ((dllexport))
    #endif
#endif

#ifdef __cplusplus
extern "C" {
#endif

ESD_PUBLIC_API int decompile(const char* input, size_t in_len, char* output, size_t* out_len, bool unblind = false);

#ifdef __cplusplus
};
#endif
```

## File: `src/jsxer/common.h`
```c
#pragma once

#include <vector>

#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

#define BEGIN_NS(ns) namespace ns {

#define END_NS(ns) }

#define _in_range(min,max,x) \
    (((x) - (min)) * ((max) - (x)) > 0)

#define _in_range_i(min,max,x) \
    (((x) - (min)) * ((max) - (x)) >= 0)

#define in_range(min,max,x) \
    (((x) > (min)) && ((x) < (max)))

#define in_range_i(min,max,x) \
    (((x) >= (min)) && ((x) <= (max)))

#if ((defined(_MSVC_LANG) && _MSVC_LANG >= 201703L) || __cplusplus >= 201703L)
    #define CPP_17_PLUS
#endif


typedef uint8_t Token;

typedef uint8_t Byte;
typedef double Number;

using String = std::string;
using Bytes = std::vector<uint8_t>;
using ByteString = std::vector<uint16_t>;
```

## File: `src/jsxer/decoders.cpp`
```cpp
///
/// High-Level Decoding Procedures
///

#include "util.h"
#include "decoders.h"
#include "nodes/nodes.h"

#include <fmt/format.h>

enum LiteralType {
    NUMBER,
};

enum NumberType : int {
    kDouble = 8,
    kInteger = 4,
    kShort = 2,
};

string d_number_primitive(jsxer::Reader& reader, int length, bool negative) {
     vector<byte> buffer(length);

    for (int i = 0; i < length; ++i) {
        buffer[i] = jsxer::decoders::d_byte(reader);
    }

    short sign = negative ? -1 : 1;

    // using the length, return the appropriate interpretation of the value...
    switch (length) {
        case kDouble:
            // result is a double...
            return fmt::to_string(*((double *) buffer.data()) * sign);
        case kInteger:
            // result is an integer...
            return fmt::to_string(*((uint32_t *) buffer.data()) * sign);
        case kShort:
            // result is a short...
            return fmt::to_string(*((uint16_t *) buffer.data()) * sign);
        default:
            return "";
    }
}

string d_literal_primitive(jsxer::Reader& reader, LiteralType literalType) {
    // TODO: fix decoding (not decoding js string entirely)
    if (reader.decrement_node_depth()) {
        return "";
    }

    bool negative = false;
    if (reader.peek() == 'y') {
        negative = true;
        reader.step();
    }

    Token marker = reader.peek();

    if (marker == '4') {
        reader.step();
        string number = d_number_primitive(reader, 4, negative);
        return number;
    } else if (marker == '2') {
        reader.step();
        string number = d_number_primitive(reader, 2, negative);
        return number;
    } else {
        byte num = jsxer::decoders::d_byte(reader);

        if (negative) {
            return fmt::to_string(-1 * (int) num);
        } else {
            if (literalType == LiteralType::NUMBER) {
                return fmt::to_string((unsigned char) num);
            } else {
                return jsxer::utils::string_literal_escape(num);
            }
        }
    }
}

int jsxer::decoders::d_literal_num(Reader& reader) {
    string value = d_literal_primitive(reader, LiteralType::NUMBER);
    return value.empty() ? 0 : stoi(value);
}

jsxer::nodes::AstOpNode jsxer::decoders::d_node(Reader& reader) {
    Token marker = reader.get();

    auto node = nodes::get((jsxer::nodes::NodeType) marker, reader);

    if (node != nullptr) {
        node->parse();

        return node;
    }

    // TODO: handle this
    return nullptr;
}

string jsxer::decoders::d_number(Reader& reader) {
    string num;

    // if the marker suggests
    if (reader.get() == '8') {
        num = d_number_primitive(reader, 8, false);
    } else {
        reader.step(-1);
        num = d_literal_primitive(reader, LiteralType::NUMBER);
    }

    return num.empty() ? "0" : num;
}

byte jsxer::decoders::d_byte(Reader& reader) {
    return reader.getByte();
}

string jsxer::decoders::d_variant(Reader& reader) {
    auto var = reader.getVariant();
    if (var != nullptr) {
        string result = var->toString();
        return result;
    }

    // TODO: check
    return "";
}

jsxer::decoders::Reference jsxer::decoders::d_id_ref(Reader& reader) {
    auto id = reader.readSID();
    bool flag = false;

    if (reader.version() >= JsxbinVersion::v20) {
        flag = reader.getBoolean();
    }

    return Reference{ id, flag };
}

jsxer::decoders::Reference jsxer::decoders::d_literal_ref(Reader& reader) {
    auto id = reader.readLiteral();
    bool flag = false;

    if (reader.version() >= JsxbinVersion::v20) {
        flag = reader.getBoolean();
    }

    return Reference{ id, flag };
}

size_t jsxer::decoders::d_length(Reader& reader) {
    string value = d_literal_primitive(reader, LiteralType::NUMBER);

    if (!value.empty()) {
        if (value[0] == '-') {
            value.erase(0,1);
        }
        return stoul(value);
    }

    return 0;
}

string jsxer::decoders::d_sid(Reader& reader) {
    return utils::to_string(reader.readSID());
}

string jsxer::decoders::d_operator(Reader& reader) {
    return utils::to_string(reader.readSID(true));
}

vector<jsxer::nodes::AstOpNode> jsxer::decoders::d_children(Reader& reader) {
    size_t length = d_length(reader);

    vector<AstOpNode> result;
    for (int i = 0; i < length; ++i) {
        auto child = d_node(reader);
        if (child != nullptr) {
            result.push_back(child);
        }
    }

    return result;
}

// jsOpStatement
jsxer::decoders::LineInfo jsxer::decoders::d_line_info(Reader& reader) {
    LineInfo result;

    result.line_number = d_length(reader);
    result.child = d_node(reader);

    size_t length = d_length(reader);

    for (int i = 0; i < length; ++i) {
        result.labels.push_back(d_sid(reader));
    }

    return result;
}

jsxer::decoders::FunctionSignature jsxer::decoders::d_fn_sig(Reader& reader) {
    FunctionSignature result;

    // identifiers/variables in func scope
    size_t n_vars = d_length(reader); // readInt
    for (int i = 0; i < n_vars; ++i) {
        string sid = d_sid(reader);
        size_t id_seq = d_length(reader); // readInt

        // 0x20000000 ... | args
        // 0x40000000 ... | vars
        // 0x60000000 ... | consts
        result.variables[id_seq] = sid;
    }

    // num of normal func args
    result.num_args = d_length(reader); // readInt

    // num of vars
    result.num_vars = d_length(reader); // readInt

    // num of func local const variables
    result.num_consts = d_length(reader); // readInt

    // name of the function or closure
    // if type == 3,
    //      Script name => #script name
    result.name = d_sid(reader); // readSID

    // v1 = (short | 4) << 16
    // 0 - normal func
    // 1 - Script Closure
    auto sf = decoders::d_literal_num(reader); // readShort
    result.flags = (sf | 4) << 16;

    return result;
}

inline
bool is_capital_alpha(uint32_t value) {
    return in_range_i('A', 'Z', value);
}

inline
bool is_small_alpha(uint32_t value) {
    return in_range_i('a', 'z', value);
}

inline
bool is_numerical_digit(uint32_t value) {
    return in_range_i('0', '9', value);
}

/* Validator for an id's first character */
inline
bool valid_id_0(uint32_t value) {
    return is_small_alpha(value) ||
        is_capital_alpha(value) ||
        ('_' == value) || ('$' == value);
}

/* Validator for an id's after first characters */
inline
bool valid_id_x(uint32_t value) {
    return valid_id_0(value) || is_numerical_digit(value);
}

// decoding utilities...
bool jsxer::decoders::valid_id(const string& value) {
    // ^[a-zA-Z_$][0-9a-zA-Z_$]*$
    size_t len = value.length();

    if (len > 0) {
        if (valid_id_0(value[0])) {
            for (int i = 1; i < len; ++i) {
                if (!valid_id_x(value[i])) {
                    return false;
                }
            }
        } else {
            return false;
        }
    } else {
        return false;
    }

    return true;
}

bool jsxer::decoders::valid_id(const ByteString& value) {
    // ^[a-zA-Z_$][0-9a-zA-Z_$]*$
    size_t len = value.size();

    if (len > 0) {
        if (valid_id_0(value[0])) {
            for (int i = 1; i < len; ++i) {
                if (!valid_id_x(value[i])) {
                    return false;
                }
            }
        } else {
            return false;
        }
    } else {
        return false;
    }

    return true;
}

bool jsxer::decoders::valid_xml_attribute(const ByteString& value) {

    if (value.size() <= 1 && value[0] != '@')
        return false;

    ByteString id(&value[1], &value[value.size() - 1]);

    if (!valid_id(id))
        return false;

    return true;
}

bool jsxer::decoders::is_integer(const string& value) {
    size_t len = value.length();

    for (int i = 0; i < len; ++i) {
        if (!is_numerical_digit(value[i])) {
            return false;
        }
    }

    return true;
}

bool jsxer::decoders::is_integer(const ByteString& value) {
    size_t len = value.size();

    for (int i = 0; i < len; ++i) {
        if (!is_numerical_digit(value[i])) {
            return false;
        }
    }

    return true;
}
```

## File: `src/jsxer/decoders.h`
```c
#pragma once

#include "jsxer.h"

#include "reader.h"
#include "nodes/AstNode.h"

#include <string>
#include <vector>
#include <algorithm>

typedef uint8_t byte;

namespace jsxer::decoders {
    using jsxer::nodes::AstOpNode;

    struct Reference {
        ByteString id;
        bool flag;
    };

    struct LineInfo {
        size_t line_number;
        AstOpNode child;
        vector<string> labels;

        string lbl_statement() {
            string result;

            for (auto& label : labels) {
                result += label + ": \n";
            }

            return result;
        }

        [[nodiscard]]
        string create_body() const {
            return child == nullptr ? "" : child->to_string();
        }
    };

    enum FunctionType {
        NORMAL = 0,
        SCRIPT_CLOSURE = 1
    };

    struct FunctionSignature {
        string name;
        size_t num_args;
        size_t num_vars;
        size_t num_consts;
        map<size_t, string> variables;
        int flags = 0x10000;
    };

    AstOpNode d_node(Reader& reader);
    LineInfo d_line_info(Reader& reader);
    int d_literal_num(Reader& reader);
    string d_variant(Reader& reader);
    string d_number(Reader& reader);
    string d_sid(Reader& reader);
    string d_operator(Reader& reader);
    size_t d_length(Reader& reader);
    Reference d_id_ref(Reader& reader);
    Reference d_literal_ref(Reader& reader);
    byte d_byte(Reader& reader);
    vector<AstOpNode> d_children(Reader& reader);
    FunctionSignature d_fn_sig(Reader& reader);

    // decoding utilities...
    bool valid_id(const string& value);
    bool valid_id(const ByteString& value);
    bool valid_xml_attribute(const ByteString &value);
    bool is_integer(const string& value);
    bool is_integer(const ByteString& value);

}
```

## File: `src/jsxer/deobfuscation.cpp`
```cpp
#include "util.h"
#include "deobfuscation.h"
#include "common.h"

#include <algorithm>

using namespace jsxer::deob;

BEGIN_NS(jsxer)
BEGIN_NS(deob)

static const std::vector<string> OPERATORS {
        "=", "==", "!=", "!==", "===", "<=", ">=", ">", "<",
        "|=", "||=", "&&=", "&=", "^=", "\?\?=",
        "|", "||", "&", "&&", "^", "??", "!", "?", ":",
        "instanceof", "typeof", "delete",
        "+", "+=",
        "-", "-=",
        "*", "*=",
        "%", "%=",
        "/", "/=",
        "**", "**=",
        "<<", "<<=",
        ">>", ">>=",
        ">>>", ">>>=",
        "~"
};

static const vector<char> PROHIBITED_CHARS {
    '=', '+', '<', '>', '-', '.', '*', '/', '|', '&', '?', '!', ':', '@', '~', '%', '^'
};

static const std::vector<uint16_t> PUNCT_CONNECTORS {
    0xFE33, 0xFE34, 0xFE4D, 0xFE4E, 0xFE4F, 0xFF3F, 0x203F, 0x2040, 0x2054
};

bool is_ECMA3_operator(const ByteString &symbol) {

    // if a symbol name is equivalent to an operator in ECMAScript 3, return true.
    string symstr = jsxer::utils::to_string(symbol);

    // check if the symbol name is contained within the list of operators...
    bool result = std::any_of(
            OPERATORS.begin(),
            OPERATORS.end(),
            [symstr](const string &op) {
                return symstr == op;
            }
    );

    return result;
}

bool is_ecma3_compliant_name(const ByteString &symbol) {
    // check for anomalies in symbol naming that should only be possible with post-compilation binary changes.
    // see https://www-archive.mozilla.org/js/language/e262-3.pdf, section 7.6 (page 30)

    uint16_t first = symbol[0];

    // check if first character is numeric
    if (in_range_i(0x29, 0x40, first))
        return false;

    // check if the first character is a unicode combining diacritical mark
    if (in_range_i(0x0300, 0x036F, first))
        return false;

    // check if the first character is a unicode punctuation connector
    if (std::any_of(PUNCT_CONNECTORS.begin(), PUNCT_CONNECTORS.end(), [first](uint16_t p) {return first == p;}))
        return false;

    bool ok_chars = std::any_of(PROHIBITED_CHARS.begin(), PROHIBITED_CHARS.end(), [symbol] (char p) {
        return (bool) std::count(symbol.begin(), symbol.end(), (uint16_t)p);
    });

    return !ok_chars;
}

bool jsxblind_should_substitute(DeobfuscationContext& context, const ByteString &symbol, bool operator_ctx) {

    // if a symbol name is empty, return false.
    if (symbol.empty()) {
        if (context.empty_id_reserved)
            return true;

        context.empty_id_reserved = true;
        return false;
    }

    bool ecma_operator = is_ECMA3_operator(symbol);

    // Check whether the symbol is an operator being used in the appropriate context...
    if (ecma_operator) {
        if (!operator_ctx)
            return true;
        return false;
    }

    // if it's not ECMA3 compliant, trash it.
    if (!is_ecma3_compliant_name(symbol))
        return true;

    // this seems like a bad solution, but it appears to work for JsxBlind.
    if (std::any_of(symbol.begin(), symbol.end(), [](uint16_t character){return character > 126;}))
        return true;

    return false;
}

END_NS(deob)
END_NS(jsxer)
```

## File: `src/jsxer/deobfuscation.h`
```c
#pragma once

#include "common.h"
#include "util.h"

#include <map>

BEGIN_NS(jsxer)
BEGIN_NS(deob)

struct DeobfuscationContext {
    // making this a struct in an attempt to future-proof, but maybe this should be a class?
    bool empty_id_reserved = false;
};

/// Determines if renaming is appropriate with symbols in JSXBIN files that are obfuscated with Jsxblind...
/// \param symbol the symbol name
/// \return
bool jsxblind_should_substitute(DeobfuscationContext& context, const ByteString& symbol, bool operator_ctx);

END_NS(deob)
END_NS(jsxer)
```

## File: `src/jsxer/jsxer.cpp`
```cpp
#include "jsxer.h"
#include "util.h"
#include "nodes/Program.h"

#include <string>

void prepend_header(string& code, JsxbinVersion jsxbin_version, bool unblind) {
    string version;

    switch (jsxbin_version){
        case JsxbinVersion::v10:
            version = "1.0";
            break;
        case JsxbinVersion::v20:
            version = "2.0";
            break;
        case JsxbinVersion::v21:
            version = "2.1";
            break;
        default:
            version = "VERSION UNKNOWN";
    }

    string header = "/*\n"
                    "* Decompiled with Jsxer\n"
                    "* Version: " CONFIG_VERSION
                    "\n"
                    "* JSXBIN " + version + "\n";

    if (unblind) {
        header += "* Jsxblind Deobfuscation Enabled (EXPERIMENTAL)\n";
    }

    header += "*/\n\n";

    code = header + code;
}

int jsxer::decompile(const string& input, string& output, bool unblind) {
    auto reader = std::make_unique<Reader>(input, unblind);

    if (!reader->verifySignature()) {
        // TODO: Handle this properly
        printf("[!]: %s\n", "The input file has an invalid signature.");
        fprintf(stderr, "JSXBIN signature verification failed!");
        output = "";
        return -3;
    }

    // Parse into an Ast
    auto ast = std::make_unique<jsxer::nodes::Program>(*reader);
    ast->parse();

    // Generate code from the ast
    output = ast->to_string();
    prepend_header(output, reader->version(), unblind);

    return 0;
}

// for testing
int jsxer::decompile_test(const string& input, string& output, bool unblind) {
    auto reader = std::make_unique<Reader>(input, unblind);

    if (!reader->verifySignature()) {
        // TODO: Handle this properly
        fprintf(stderr, "JSXBIN signature verification failed!");
        output = "";
        return -3;
    }

    // Parse into an Ast
    auto ast = std::make_unique<jsxer::nodes::Program>(*reader);
    ast->parse();

    // Generate code from the ast
    output = ast->to_string();

    return 0;
}
```

## File: `src/jsxer/reader.cpp`
```cpp
#include <memory>
#include "reader.h"
#include "util.h"

#include <fmt/format.h>


using namespace jsxer;
#define perror(msg) printf("[!] " msg ", POS: %lu\n", this->_cursor)

Reader::Reader(const string& jsxbin, bool unblind) {
    string _input = jsxbin;

    utils::string_strip_char(_input, ' ');
    utils::string_strip_char(_input, '\t');
    utils::string_strip_char(_input, '\r');
    utils::string_strip_char(_input, '\n');
    utils::string_strip_char(_input, '\\');

    size_t input_len = _input.length();

    _data.resize(input_len);
    memcpy(_data.data(), _input.data(), input_len);

    _start = _cursor = 0;
    _end = input_len - 1;
    _depth = 0;

    _error = ParseError::None;
    _version = JsxbinVersion::Invalid;
    _unblind = unblind;
}

JsxbinVersion Reader::version() const {
    return _version;
}

ParseError Reader::error() const {
    return _error;
}

size_t Reader::depth() const {
    return _depth;
}

bool Reader::should_unblind() const {
    return _unblind;
}

void Reader::step(int offset) {
    _cursor += offset;
}

Token Reader::peek(int offset) {
    return _data[_cursor + offset];
}

size_t Reader::get_node_depth() {
    if (_depth == 0){
        update_node_depth();
    }

    return _depth;
}

int Reader::parse_node_depth() {
    Token current = peek();

    if (current == 'A') {
        step();
        return 1;

    } else if (current == '0') {
        step();
        int levels = get() - 0x3f;

        if (levels > 0x1b) {
            return levels + parse_node_depth();
        }
        return levels;

    }

    return 0;
}

void Reader::update_node_depth() {
    _depth = parse_node_depth();
}

bool Reader::decrement_node_depth() {
    if (get_node_depth() == 0)
        return false;

    _depth--;
    return true;
}

bool Reader::verifySignature() {
    if (_data.empty()) {
        _error = ParseError::NoData;
        return false;
    }

    if (_data.size() < JSXBIN_SIGNATURE_LEN) {
        _error = ParseError::InvalidVersion;
        return false;
    }

    if ( utils::bytes_eq((uint8_t*) _data.data(), (uint8_t*) JSXBIN_SIGNATURE_V10, JSXBIN_SIGNATURE_LEN) ) {
        _version = JsxbinVersion::v10;
    } else if ( utils::bytes_eq((uint8_t*) _data.data(), (uint8_t*) JSXBIN_SIGNATURE_V20, JSXBIN_SIGNATURE_LEN) ) {
        _version = JsxbinVersion::v20;
    } else if ( utils::bytes_eq((uint8_t*) _data.data(), (uint8_t*) JSXBIN_SIGNATURE_V21, JSXBIN_SIGNATURE_LEN) ) {
        _version = JsxbinVersion::v21;
    } else {
        _error = ParseError::InvalidVersion;
        return false;
    }

    _start = _cursor += JSXBIN_SIGNATURE_LEN;

    return true;
}

Token Reader::get() {
    Token token = _next();

    while (_ignorable(token)) {
        token = _next();
    }

    return token;
}

Byte Reader::getByte() {
    if (_depth > 0) {
        --_depth;
        return 0;
    }

    Token m = get();

    if (m == '0') {
        Token n = get();

        if (n > 0x5A) {
            goto error8;
        } else {
            _depth = n - 0x40;
            return 0;
        }
    } else if (m > 0x5A) {
        if (m > 0x6E) {
            goto error8;
        } else {
            Token z = get();
            uint8_t l, r = 32 * (m + 1);

            if (z > 0x5A) {
                if (z > 0x66) {
                    goto error8;
                } else {
                    l = z - 0x47;
                }
            } else {
                l = z - 0x41;
            }

            return (l | r);
        }
    }

    return m - 0x41;

error8:
    _error = ParseError::DecodeError;
    perror("Parse Error at getByte()");
    return 0;
}

Number Reader::getNumber() {
    if (_depth > 0) {
        --_depth;
        return 0.0;
    }

    Token t = get();
    Number res = 0, sign = (t != 'y') ? 1.0 : (t = get(), -1.0);

    switch (t) {
        case '2':
        case '4':
        case '8': {
            for (int i = 0; i < t - 48; ++i) {
                ((Byte*) &res)[i] = getByte();
            }
            break;
        }
        default: {
            step(-1);
            res = getByte();
            break;
        }
    }

    return sign * res;
}

ByteString Reader::getString() {
    ByteString result;

    auto length = utils::number_as_int<size_t>(getNumber());

    for (int i = 0; i < length; ++i) {
        // Each char is a unicode (utf-16) codepoint.
        auto u16_ch = utils::number_as_int<uint16_t>(getNumber());
        result.push_back(u16_ch);
    }

    return result;
}

bool Reader::getBoolean() {
    Token t = get();

    if (t == 't') {
        return true;
    } else if (t == 'f') {
        return false;
    } else {
        _error = ParseError::DecodeError;
        perror("Parse Error at getBoolean()");
    }

    return false;
}

ByteString Reader::readSID(bool operator_context) {
    ByteString symbol;
    Number id;

    if (get() == 'z') {
        symbol = getString();
        id = getNumber();

        int id_int = utils::number_as_int<int>(id);

        // if a symbol name is obfuscated, rename it to something more sensible...
        if (_unblind && jsxer::deob::jsxblind_should_substitute(deobfuscationContext, symbol, operator_context)) {
            string deobfuscated = "symbol_" + fmt::to_string(id_int);
            symbol = utils::to_byte_string(deobfuscated);
        }

        addSymbol(id, symbol);
    } else {
        step(-1);
        id = getNumber();
        symbol = getSymbol(id);
    }

    return symbol;
}

ByteString Reader::readLiteral() {
    ByteString symbol;
    Number id;

    if (get() == 'z') {
        symbol = getString();
        id = getNumber();
        addSymbol(id, symbol);
    } else {
        step(-1);
        id = getNumber();
        symbol = getSymbol(id);
    }

    return symbol;
}

OpVariant Reader::getVariant() {
    if (get() == 'n') {
        return nullptr;
    } else {
        step(-1);
    }

    uint8_t type = get() - 'a';

    OpVariant result = std::make_shared<Variant>();
    switch (type) {
        case 0: // 'a' - also recognized as a null at runtime.
            // looks like it's meant for undefined, but not utilized.
            result->doErase();

            // TODO: find a better way for this
            result->setNull();
            break;
        case 1: // 'b' - null always encoded to 'b'
            // null type
            result->setNull();
            break;
        case 2: // 'c'
            // Boolean type
            result->setBool(getBoolean());
            break;
        case 3: // 'd'
            // Number type
            result->setDouble(getNumber());
            break;
        case 4: // 'e'
            // String type
            result->setString(getString());
            break;

        default:
            _error = ParseError::DecodeError;
            perror("Parse Error at getVariant()");
            break;
    }

    return result;
}

Token Reader::_next() {
    if (_cursor < _end) {
        return _data[_cursor++];
    }

    _error = ParseError::ReachedEnd;

    return _data[_end];
}

bool Reader::_ignorable(Token value) {
    switch (static_cast<char>(value)) {
        case ' ':
        case '\t':
        case '\r':
        case '\n':
            return true;
        default:
            return false;
    }
}

ByteString Reader::getSymbol(Number id) {
    return _symbols[id];
}

void Reader::addSymbol(Number id, const ByteString& symbol) {
    _symbols[id] = symbol;
}

int Reader::getInt() {
    Number val = getNumber();
    return int(val);
}

short Reader::getShort() {
    Number val = getNumber();
    return short(val);
}

Variant::Variant() {
    _type = VariantType::None;
    doErase();
}

void Variant::setNull() {
    _type = VariantType::Null;
    doErase();
}

void Variant::setBool(bool value) {
    _type = VariantType::Boolean;
    doErase();
    _value._bool = value;
}

void Variant::setDouble(double value) {
    _type = VariantType::Number;
    doErase();
    _value._double = value;
}

void Variant::setString(const ByteString& value) {
    _type = VariantType::String;
    doErase();
    _value._string = value;
}

void Variant::doErase() {
    if (_type == VariantType::String) {
        _value._string.clear();
    }

    utils::zero_mem(&_value, sizeof(ValueType));
}

String Variant::toString() {
    switch (_type) {
        case VariantType::Undefined: return "undefined";
        case VariantType::Null: return "null";
        case VariantType::Boolean:
            return _value._bool ? "true" : "false";
        case VariantType::Number:
            return utils::number_to_string(_value._double);
        case VariantType::String:
            return utils::to_string_literal(_value._string);
        default:
            return "";
    }
}
```

## File: `src/jsxer/reader.h`
```c
#pragma once

#include "jsxer.h"
#include "common.h"
#include "deobfuscation.h"

#include <map>
#include <string>
#include <vector>
#include <memory>

using std::string;
using std::vector;
using std::map;

BEGIN_NS(jsxer)

#define JSXBIN_SIGNATURE_V10 "@JSXBIN@ES@1.0@"
#define JSXBIN_SIGNATURE_V20 "@JSXBIN@ES@2.0@"
#define JSXBIN_SIGNATURE_V21 "@JSXBIN@ES@2.1@"

#define JSXBIN_SIGNATURE_LEN 15

enum class ParseError : int {
    None = 0,

    InvalidVersion,
    ReachedEnd,
    DecodeError,
    NoData,
};

enum class VariantType : int {
    None = -1,

    Undefined = 0,
    Null = 1,
    Boolean = 2,
    Number = 3,
    String = 4,
};

class Variant {
public:
    Variant();

    void doErase();

    void setNull();

    void setString(const ByteString& value);

    void setBool(bool value);

    void setDouble(double value);

    String toString();

private:
    VariantType _type;
    struct ValueType {
        bool _bool;
        double _double;
        ByteString _string;
    } _value;
};

using OpVariant = std::shared_ptr<Variant>;

class Reader {
public:
    explicit Reader(const string& jsxbin, bool unblind);

    [[nodiscard]] JsxbinVersion version() const;
    [[nodiscard]] ParseError error() const;
    [[nodiscard]] size_t depth() const;
    [[nodiscard]] bool should_unblind() const;
    bool verifySignature();

    Token get();
    Token peek(int offset = 0);
    void step(int offset = 1);

    Byte getByte();
    int getInt();
    short getShort();
    Number getNumber();
    ByteString getString();
    bool getBoolean();

    OpVariant getVariant();
    ByteString readSID(bool operator_context = false);
    ByteString readLiteral();

    void addSymbol(Number id, const ByteString& symbol);
    ByteString getSymbol(Number id);

    size_t get_node_depth();
    bool decrement_node_depth();

private:
    vector<Token> _data;
    size_t _start;
    size_t _end;
    size_t _cursor;
    size_t _depth;
    ParseError _error;
    JsxbinVersion _version;

    bool _unblind;
    deob::DeobfuscationContext deobfuscationContext;

    map<Number, ByteString> _symbols;

    void update_node_depth();
    int parse_node_depth();

    Token _next();
    static bool _ignorable(Token value);

};

END_NS(jsxbin)
```

## File: `src/jsxer/util.cpp`
```cpp
#include "util.h"

#include <cstring>
#include <algorithm>
#include <cmath>

#include <fmt/format.h>

BEGIN_NS(jsxer) BEGIN_NS(utils)

bool string_equal(const string &str1, const string &str2) {
    return strncmp(str1.c_str(), str2.c_str(), MIN(str1.length(), str2.length())) == 0;
}

void string_replace_char(string &str, char search, char replace) {
    std::replace(str.begin(), str.end(), search, replace);
}

void string_strip_char(string &str, char search) {
    str.erase(remove(str.begin(), str.end(), search), str.end());
}

void replace_str_inplace(string &subject, const string &search, const string &replace) {
    size_t pos = 0;

    while ((pos = subject.find(search, pos)) != string::npos) {
        subject.replace(pos, search.length(), replace);
        pos += replace.length();
    }
}

#define HEX_CHARSET_CAPITAL ("0123456789" "ABCDEF")
#define HEX_CHARSET_SMALL   ("0123456789" "abcdef")

string unicode_escape(uint16_t value, bool capital = false) {
    auto *cs = capital ? HEX_CHARSET_CAPITAL : HEX_CHARSET_SMALL;
    char result[] = {'\\', 'u', '0', '0', '0', '0', '\0'};

    for (int i = 0; i < 4; ++i) {
        auto hc = cs[(value >> (4 * i)) & 0xF];
        result[sizeof(result) - (i + 2)] = hc;
    }

    return result;
}

string hex_escape(uint8_t value, bool capital = false) {
    auto *cs = capital ? HEX_CHARSET_CAPITAL : HEX_CHARSET_SMALL;
    char result[] = {'\\', 'x', '0', '0', '\0'};

    for (int i = 0; i < 2; ++i) {
        auto hc = cs[(value >> (4 * i)) & 0xF];
        result[sizeof(result) - (i + 2)] = hc;
    }

    return result;
}

bool is_non_printable_ascii(uint32_t value) {
    // ([\x00-\x07\x0E-\x1F\x7F])
    return in_range_i(0, 7, value) ||
           in_range_i(0x0E, 0x1F, value) || (value == 0x7F);
}

bool is_non_printable_utf8(uint32_t value) {
    // ([\x00-\x07\x0E-\x1F\x7F\x80-\xFF])
    return is_non_printable_ascii(value) || in_range_i(0x80, 0xFF, value);
}

bool is_non_printable_utf16(uint32_t value) {
    return is_non_printable_ascii(value) || in_range_i(0x80, 0xFF, value) || (value > 0xFF);
}

string escape_hex_or_unicode(uint16_t value, bool capital = false) {
    if (in_range_i(0x00, 0xFF, value)) {
        return hex_escape((uint8_t) value, capital);
    }

    return unicode_escape(value, capital);
}

string string_join(vector<string> strings, const string& delimiter) {
    string result;

    for (int i = 0; i < strings.size(); ++i) {
        result += strings[i];

        if (i + 1 != strings.size()) {
            result += delimiter;
        }
    }

    return result;
}

string string_literal_escape(uint16_t value, bool capital) {
    switch (value) {
        case '\b':
            return "\\b";
        case '\f':
            return "\\f";
        case '\n':
            return "\\n";
        case '\r':
            return "\\r";
        case '\v':
            return "\\v";
        case '\t':
            return "\\t";
        case '\"':
            return "\\\"";
        case '\'':
            return "\\\'";
        case '\\':
            return "\\\\";
        default:
            return is_non_printable_utf16(value)
                   ? escape_hex_or_unicode(value, capital)
                   : string(1, (char) value);
    }
}

string string_literal_escape(const ByteString &value, bool capital) {
    string res;

    for (const auto &c: value) {
        res += string_literal_escape(c, capital);
    }

    return res;
}

string string_literal_unescape(const string& value) {

    string result;

    for (int i = 0; i < value.size(); ++i) {
        if (value[i] != '\\' || i + 1 == value.size()) {
            result += value[i];
            continue;
        }

        i++;
        switch(value[i]) {
            case 'b':
                result += "\b";
                break;
            case 'f':
                result += "\f";
                break;
            case 'n':
                result += "\n";
                break;
            case 'r':
                result += "\r";
                break;
            case 'v':
                result += "\v";
                break;
            case 't':
                result += "\t";
                break;
            case '"':
                result += "\"";
                break;
            case '\'':
                result += "\'";
                break;
            default:
                result += '\\';
                result += value[i];
                break;
        }
    }

    return result;
}

string from_string_literal(const string &value) {

    string x = value;
    x.erase(0, 1);
    x.erase(x.size() - 1, 1);
    x = string_literal_unescape(x);

    return x;
}

string to_string_literal(const ByteString &value, bool capital) {
    string res = "\"";

    for (auto &c: value) {
        res += string_literal_escape(c, capital);
    }

    return res + "\"";
}

string to_string_literal(const string &value, bool capital) {
    string res = "\"";

    for (auto &c: value) {
        res += string_literal_escape(c, capital);
    }

    return res + "\"";
}

string to_string(const ByteString &value) {
    string res;

    for (auto &c: value) {
        res += (char) c;
    }

    return res;
}

ByteString to_byte_string(const string &value) {
    ByteString res;

    for (auto &c: value) {
        res.push_back((uint16_t) c);
    }

    return res;
}

vector<string> string_split(const string &str, const string &delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    string token;
    vector<string> res;

    while ((pos_end = str.find(delimiter, pos_start)) != string::npos) {
        token = str.substr(pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back(token);
    }

    res.push_back(str.substr(pos_start));
    return res;
}

int byte_length(uint64_t value) {
    int len = sizeof(uint64_t);
    auto *p = (uint8_t *) &value;

    while ((p[len - 1] == 0) && len) {
        len--;
    }

    return len;
}

string ltrim(const string &s, char target = ' ') {
    size_t start = s.find_first_not_of(target);
    return (start == string::npos) ? "" : s.substr(start);
}

string rtrim(const string &s, char target = ' ') {
    size_t end = s.find_last_not_of(target);
    return (end == string::npos) ? "" : s.substr(0, end + 1);
}

string trim(const string &s, char target = ' ') {
    return rtrim(ltrim(s, target), target);
}

#define NUMBER_SIGN_BIT_MASK (1LL << 63) // 0x8000_0000_0000_0000

bool is_number_negative(double value) {
    // is the sign(63rd) bit is set
    return number_raw_cast<uint64_t>(value) & NUMBER_SIGN_BIT_MASK;
}

// Returns positive integer
uint64_t number_to_integer(double value) {
    // ignore the sign(63rd) bit
    return number_raw_cast<uint64_t>(value) & ~NUMBER_SIGN_BIT_MASK;
}

// Returns positive double
double number_to_double(double value) {
    // ignore the sign(63rd) bit
    return number_raw_cast<double>(number_to_integer(value));
}

bool is_number_integer(double value) {
    return byte_length(number_to_integer(value)) < 8;
}

bool is_number_double(double value) {
    return !is_number_integer(value);
}

string simplify_number_literal(const string &value) {
    string result = value;

    auto es = string_split(result, "e");
    if (es.size() > 1) {
        auto e2 = es[1];
        if (e2.length()) {
            char sign = e2[0];
            for (char i: e2.substr(1)) {
                if (i != '0') {
                    goto skip_e_sfy;
                }
            }
            result = es[0];
        }
    }

skip_e_sfy:
    auto ds = string_split(result, ".");

    // trim prefix zeroes
    auto d1 = ds[0];
    for (int i = 0; i < d1.length(); ++i) {
        if (d1[i] != '0') {
            d1 = d1.substr(i, d1.length() - i);
            break;
        }
    }
    result = d1;

    // trim suffix zeroes
    if (ds.size() > 1) {
        auto d2 = ds[1];

        if (d2.length()) {
            for (size_t i = d2.length() - 1; i >= 0; --i) {
                if (d2[i] != '0') {
                    d2 = d2.substr(0, i + 1);
                    break;
                }
            }
        }

        if (d2.length()) {
            result += '.' + d2;
        }
    }

    return result;
}

string number_to_string(double value) {
    // let's try fmt to do all the dirty works
    // TODO:
    //  Write a full NumberToString test to confirm
    //  if it's okay for us to keep fmt for this job
    {
        string result;

        // integer        -> 1-7 bytes
        // double         -> 8 bytes
        // sign           -> 63rd bit
        if (is_number_negative(value)) { // is the sign(63rd) bit is set
            result += '-';
        }

        if (is_number_integer(value)) { // is byte_length < 8
            auto i = number_to_integer(value);
            result += fmt::format("{}", i);
        } else {
            auto d = number_to_double(value);
            result += fmt::format("{}", d);
        }

        return result;
    }

    // our dirty impl
    {
        char _buff[40] = {0};
        int _fmt_len;
        string result;

        // integer        -> 1-7 bytes in memory
        // double         -> 8 bytes in memory
        // 63rd bit       -> sign
        if (is_number_negative(value)) {
            result += '-';
        }

        if (is_number_integer(value)) {
            // Integer
            _fmt_len = snprintf(
                    _buff, sizeof(_buff),
                    "%llu", number_to_integer(value)
            );
        } else {
            // Double
            int precision = 15;
            const char *fmt;

            switch (number_raw_cast<uint64_t>(value)) {
                case 0x7FEFFFFFFFFFFFFF:
                    return "1.7976931348623157e+308";
                case 0xFFEFFFFFFFFFFFFF:
                    return "-1.7976931348623157e+308";
                default: {
                    if ((value >= 1.0e21) || (floor(value) != value)) {
                        if ((value < 1.0e21) && (value >= 0.000001)) {
                            int l10 = (int) log10(value);
                            int fpn = (l10 >= 0) ? l10 : 0;

                            precision = 15 - (value >= 1.0) - fpn;
                            if (precision > 15) {
                                precision = 15;
                            }

                            fmt = "%20.*f";
                        } else {
                            fmt = "%20.*e";
                            precision -= 1;
                        }
                    } else if (value >= 1000000000.0) {
                        fmt = "%*.0f";
                    } else {
                        fmt = "%*.f";
                    }
                }
            }

            _fmt_len = snprintf(
                    _buff, sizeof(_buff),
                    fmt, precision, number_to_double(value)
            );
        }

        _buff[_fmt_len] = '\0';
        result += trim(_buff, ' ');

        return simplify_number_literal(result);
    }
}

bool bytes_eq(const uint8_t *b1, const uint8_t *b2, size_t size) {
    for (size_t i = 0; i < size; ++i) {
        if (b1[i] != b2[i]) {
            return false;
        }
    }

    return true;
}

void zero_mem(const void *buff, size_t size) {
    for (int i = 0; i < size; ++i) {
        ((uint8_t *) buff)[i] = '\0';
    }
}

END_NS(utils) END_NS(jsxbin)
```

## File: `src/jsxer/util.h`
```c
#pragma once

#include <string>

#include "common.h"

using std::string;
using std::vector;

BEGIN_NS(jsxer) BEGIN_NS(utils)

bool string_equal(const string &str1, const string &str2);

void string_replace_char(string& str, char search, char replace);

void string_strip_char(string& str, char search);

void replace_str_inplace(string& subject, const string& search, const string& replace);

string string_join(vector<string> strings, const string& delimiter);

string string_literal_escape(uint16_t value, bool capital = false);

string string_literal_escape(const ByteString& value, bool capital = false);

string to_string_literal(const ByteString& value, bool capital = false);

string to_string_literal(const string& value, bool capital = false);

string from_string_literal(const string &value);

string to_string(const ByteString& value);

ByteString to_byte_string(const string& value);

int byte_length(uint64_t value);

bool is_number_integer(double value);

bool is_number_double(double value);

string number_to_string(double value);

bool bytes_eq(const uint8_t* b1, const uint8_t* b2, size_t size);

void zero_mem(const void* buff, size_t size);

template<typename T, typename F>
T number_raw_cast(F value) {
    return *((T*) &value);
}

// returns an int repr of the number
// floating points are not expected here (not 2.1436 but 2.0)
template<typename T, typename F>
T number_as_int(F value) {
    if (utils::is_number_double(value)) {
        return static_cast<T>(value);
    } else {
        return number_raw_cast<T>(value);
    }
}

END_NS(utils) END_NS(jsxbin)
```

## File: `src/jsxer/nodes/ArrayExpression.cpp`
```cpp
#include "ArrayExpression.h"

namespace jsxer::nodes {
    void ArrayExpression::parse() {
        argumentList = std::dynamic_pointer_cast<ListExpression>(decoders::d_node(reader));
    }

    string ArrayExpression::to_string() {
        if (!argumentList) {
            return "[]";
        }

        return '[' + argumentList->to_string() + ']';
    }
}
```

## File: `src/jsxer/nodes/ArrayExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "ListExpression.h"
#include "../decoders.h"
#include <vector>

namespace jsxer::nodes {
    class ArrayExpression : public AstNode {
    public:
        explicit ArrayExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ArrayExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        OpListExpression argumentList;
    };
}
```

## File: `src/jsxer/nodes/AssignmentExpression.cpp`
```cpp
#include "AssignmentExpression.h"

namespace jsxer::nodes {
    void AssignmentExpression::parse() {
        variable = decoders::d_node(reader);
        expression = decoders::d_node(reader);
        literal = decoders::d_variant(reader);
        shorthand = reader.getBoolean();
    }

    string AssignmentExpression::to_string() {
        if (shorthand) {
            auto expr = std::dynamic_pointer_cast<BinaryExpression>(expression);
            string value_assigned = literal.empty() ? expr->get_op() : literal;

            return variable->to_string() + ' ' + expr->get_op_name() + "= " + value_assigned;
        }

        string value_assigned = literal.empty() ? expression->to_string() : literal;
        return variable->to_string() + " = " + value_assigned;

    }
}
```

## File: `src/jsxer/nodes/AssignmentExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"
#include "BinaryExpression.h"

namespace jsxer::nodes {
    class AssignmentExpression : public AstNode {
    public:
        explicit AssignmentExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::AssignmentExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        AstOpNode variable;
        AstOpNode expression;
        string literal;
        bool shorthand{};
    };
}
```

## File: `src/jsxer/nodes/AstNode.h`
```c
#pragma once

#include <memory>

#include "../reader.h"
#include "node-types.h"

namespace jsxer::nodes {
    class AstNode {
    public:
        explicit AstNode(Reader &reader) : reader(reader) {};

        virtual NodeType type() = 0;

        virtual string to_string() = 0;

        virtual void parse() = 0;

    protected:
        Reader &reader;
    };

    using AstOpNode = std::shared_ptr<AstNode>;
}
```

## File: `src/jsxer/nodes/BinaryExpression.cpp`
```cpp
#include "BinaryExpression.h"

#include <cstring>

namespace jsxer::nodes {
    string BinaryExpression::create_expr(const string &literal, const AstOpNode& exprNode) {
        bool parenthesis = false;
        string expression;

        if (exprNode != nullptr && exprNode->type() == NodeType::BinaryExpression) {
            auto binExpr = std::dynamic_pointer_cast<BinaryExpression>(exprNode);
            expression = binExpr->get_op();

            bool associative = (strcmp(binExpr->get_op_name().c_str(), "*") == 0
                                && strcmp(op_name.c_str(), "*") == 0) ||
                               (strcmp(binExpr->get_op_name().c_str(), "+") == 0
                                && strcmp(op_name.c_str(), "+") == 0);

            parenthesis = !associative;
        } else if (exprNode != nullptr && (exprNode->type() == NodeType::LocalAssignmentExpression || exprNode->type() == NodeType::AssignmentExpression)){
            parenthesis = true;
            expression = exprNode->to_string();
        } else {
            expression = exprNode == nullptr ? literal : exprNode->to_string();
        }

        return parenthesis ? "(" + expression + ")" : expression;
    }

    void BinaryExpression::parse() {
        op_name = decoders::d_operator(reader);
        left = decoders::d_node(reader);
        right = decoders::d_node(reader);
        literalLeft = decoders::d_variant(reader);
        literalRight = decoders::d_variant(reader);

        string leftExp = create_expr(literalLeft, left);
        string rightExp = create_expr(literalRight, right);

        if ((!leftExp.empty() && rightExp.empty()) || (leftExp.empty() && !rightExp.empty())) {
            op = leftExp + rightExp;
        } else {
            op = leftExp + ' ' + op_name + ' ' + rightExp;
        }
    }

    string BinaryExpression::to_string() {
        return op;
    }
}
```

## File: `src/jsxer/nodes/BinaryExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class BinaryExpression : public AstNode {
    public:
        explicit BinaryExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::BinaryExpression;
        }

        void parse() override;

        string to_string() override;

        string get_op(){
            return this->op;
        }

        string get_op_name() {
            return this->op_name;
        }

    private:
        string op_name;
        string op;
        AstOpNode left;
        AstOpNode right;
        string literalLeft;
        string literalRight;

        string create_expr(const string &literal, const AstOpNode& exprNode);
    };
}
```

## File: `src/jsxer/nodes/BreakStatement.cpp`
```cpp
#include "BreakStatement.h"

namespace jsxer::nodes {
    void BreakStatement::parse() {
        labelInfo = decoders::d_line_info(reader);
        jmpLocation = decoders::d_sid(reader);
        breakStatement = reader.getBoolean();
    }

    string BreakStatement::to_string() {
        string result = labelInfo.lbl_statement();

        if (breakStatement)
            result += "break ";
        else
            result += "continue ";

        result += jmpLocation + ';';

        return result;
    }
}
```

## File: `src/jsxer/nodes/BreakStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class BreakStatement : public AstNode {
    public:
        explicit BreakStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::BreakStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo labelInfo;
        string jmpLocation;
        bool breakStatement = false;
    };
}
```

## File: `src/jsxer/nodes/CallExpression.cpp`
```cpp
#include "CallExpression.h"
#include "Program.h"

#include <fmt/format.h>

namespace jsxer::nodes {
    void CallExpression::parse() {
        function = decoders::d_node(reader);
        args = decoders::d_node(reader);
        constructorCall = reader.getBoolean();
    }

    string CallExpression::to_string() {
        auto function_name = function->to_string();
        auto arguments = std::dynamic_pointer_cast<ListExpression>(args);
        bool needWrap = function->type() == NodeType::FunctionExpression;
        // {new }{funcName|funcBody}({args})

        if (function_name == "eval" && arguments->arguments.size() == 1 && !constructorCall) {
            // Check if it has a JSXBIN signature.

            string payload = utils::from_string_literal(arguments->arguments[0]->to_string());
            auto internal_reader = std::make_unique<Reader>(payload, reader.should_unblind());

            if (internal_reader->verifySignature()) {
                // If we've confirmed it to be a nested JSXBIN eval call, decompile and inline the results.

                auto internal_ast = std::make_unique<Program>(*internal_reader);
                internal_ast->parse();
                string result = internal_ast->to_string();

                if (result.back() == ';') {
                    result.pop_back();
                }

                return result;
            }

        }

        string result = (constructorCall ? "new " : "");
        result += (needWrap ? "(" : "")
                + function->to_string()
                + (needWrap ? ")" : "")
                + (arguments ? '(' + arguments->to_string() + ')' : "()");

        return result;
    }
}
```

## File: `src/jsxer/nodes/CallExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"
#include "ListExpression.h"

namespace jsxer::nodes {
    class CallExpression : public AstNode {
    public:
        explicit CallExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::CallExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        AstOpNode function;
        AstOpNode args;
        bool constructorCall{};
    };
}
```

## File: `src/jsxer/nodes/ConstAssignment.cpp`
```cpp
#include "ConstAssignment.h"

namespace jsxer::nodes {
    void ConstAssignment::parse() {
        name = decoders::d_sid(reader);
        length = decoders::d_length(reader);
        expression = decoders::d_node(reader);
        literal = decoders::d_variant(reader);
        boolean_1 = reader.getBoolean();
        boolean_2 = reader.getBoolean();
    }

    string ConstAssignment::to_string() {
        return "const " + name + " = "
               + (expression == nullptr ? literal : expression->to_string());
    }
}
```

## File: `src/jsxer/nodes/ConstAssignment.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class ConstAssignment : public AstNode {
    public:
        explicit ConstAssignment(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ConstAssignment;
        }

        void parse() override;

        string to_string() override;

    private:
        string name;
        size_t length{};
        AstOpNode expression;
        string literal;
        bool boolean_1{};
        bool boolean_2{};
    };
}
```

## File: `src/jsxer/nodes/ConstantLiteral.cpp`
```cpp
#include "ConstantLiteral.h"

namespace jsxer::nodes {
    void ConstantLiteral::parse() {
        value = decoders::d_variant(reader);
    }

    string ConstantLiteral::to_string() {
        return value;
    }
}
```

## File: `src/jsxer/nodes/ConstantLiteral.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class ConstantLiteral : public AstNode {
    public:
        explicit ConstantLiteral(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ConstantLiteral;
        }

        void parse() override;

        string to_string() override;

    private:
        string value;
    };
}
```

## File: `src/jsxer/nodes/DebuggerStatement.cpp`
```cpp
#include "DebuggerStatement.h"

namespace jsxer::nodes {
    void DebuggerStatement::parse() {
        lineInfo = decoders::d_line_info(reader);
    }

    string DebuggerStatement::to_string() {
        return lineInfo.lbl_statement() + "debugger";
    }
}
```

## File: `src/jsxer/nodes/DebuggerStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class DebuggerStatement : public AstNode {
    public:
        explicit DebuggerStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::DebuggerStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo lineInfo;
    };
}
```

## File: `src/jsxer/nodes/DoWhileStatement.cpp`
```cpp
#include "DoWhileStatement.h"

namespace jsxer::nodes {
    void DoWhileStatement::parse() {
        body = decoders::d_line_info(reader);
        condition = decoders::d_node(reader);
    }

    string DoWhileStatement::to_string() {
        string label = body.lbl_statement();
        string inner = body.create_body();
        string result;

        result += label + "do {\n";
        result += "  " + inner + '\n';
        result += "} while (" + condition->to_string() + ')';

        return result;
    }
}
```

## File: `src/jsxer/nodes/DoWhileStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class DoWhileStatement : public AstNode {
    public:
        explicit DoWhileStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::DoWhileStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo body;
        AstOpNode condition;
    };
}
```

## File: `src/jsxer/nodes/ExpressionStatement.cpp`
```cpp
#include "ExpressionStatement.h"

namespace jsxer::nodes {
    void ExpressionStatement::parse() {
        lineInfo = decoders::d_line_info(reader);
        expression = decoders::d_node(reader);
    }

    string ExpressionStatement::to_string() {
        return lineInfo.lbl_statement() + expression->to_string() + ';';
    }
}
```

## File: `src/jsxer/nodes/ExpressionStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class ExpressionStatement : public AstNode {
    public:
        explicit ExpressionStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ExpressionStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo lineInfo;
        AstOpNode expression;
    };
}
```

## File: `src/jsxer/nodes/ForInStatement.cpp`
```cpp
#include "ForInStatement.h"

namespace jsxer::nodes {
    void ForInStatement::parse() {
        bodyInfo = decoders::d_line_info(reader);
        loopVariable = decoders::d_node(reader);
        objExpression = decoders::d_node(reader);
        length = decoders::d_length(reader);
        id = decoders::d_sid(reader);

        if (reader.version() >= JsxbinVersion::v20)
            // strange, because a "for-each" statement is not described in the ECMAScript3 standard.
            forEach = reader.getBoolean();
    }

    string ForInStatement::to_string() {
        string result;
        result += bodyInfo.lbl_statement();

        result += forEach ? "for each (var " : "for (var ";
        result += loopVariable->to_string();
        result += " in ";
        result += objExpression->to_string();
        result += ") { \n" + bodyInfo.create_body() + "\n}";

        return result;
    }
}
```

## File: `src/jsxer/nodes/ForInStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class ForInStatement : public AstNode {
    public:
        explicit ForInStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ForInStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo bodyInfo;
        AstOpNode loopVariable;
        AstOpNode objExpression;
        unsigned long length{};
        string id;
        bool forEach = false;
    };
}
```

## File: `src/jsxer/nodes/ForStatement.cpp`
```cpp
#include "ForStatement.h"
#include "ListExpression.h"

namespace jsxer::nodes {
    void ForStatement::parse() {
        bodyInfo = decoders::d_line_info(reader);
        initial = decoders::d_node(reader);

        if (initial && initial->type() == NodeType::ListExpression) {
            (std::dynamic_pointer_cast<ListExpression>(initial))->set_for_loop(true);
        }

        test = decoders::d_node(reader);
        update = decoders::d_node(reader);
    }

    string ForStatement::to_string() {
        string result;
        result += bodyInfo.lbl_statement();
        result += "for (" + (initial == nullptr ? "" : initial->to_string());
        result += "; " + (test == nullptr ? "" : test->to_string());
        result += "; " + (update == nullptr ? "" : update->to_string());
        result += ") { \n" + bodyInfo.create_body() + '}';
        return result;
    }
}
```

## File: `src/jsxer/nodes/ForStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class ForStatement : public AstNode {
    public:
        explicit ForStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ForStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo bodyInfo;
        AstOpNode initial;
        AstOpNode test;
        AstOpNode update;
    };
}
```

## File: `src/jsxer/nodes/FunctionDeclaration.cpp`
```cpp
#include "FunctionDeclaration.h"

#include <fmt/printf.h>

namespace jsxer::nodes {
    enum VariableTypeRange : int {
        kArguments = 0x20000000,
        kVars = 0x40000000,
        kConsts = 0x60000000,
    };

    void FunctionDeclaration::parse() {
        bodyInfo = decoders::d_line_info(reader);
        signature = decoders::d_fn_sig(reader);
        flags = decoders::d_literal_num(reader);
    }

    string FunctionDeclaration::to_string() {

        string body = bodyInfo.create_body();

        vector<string> args;
        vector<string> vars;
        vector<string> consts;

        for (int i = 0; i < signature.num_args; ++i) {
            uint32_t k = kArguments + i;
            auto v = signature.variables[k];
            args.push_back(v);
        }

        // not used for de-compilation
//        for (int i = 0; i < signature.num_vars; ++i) {
//            uint32_t k = kVars + i;
//            auto v = signature.variables[k];
//            vars.push_back(v);
//        }

        // not used for de-compilation
//        for (int i = 0; i < signature.num_consts; ++i) {
//            uint32_t k = kConsts + i;
//            auto v = signature.variables[k];
//            consts.push_back(v);
//        }

        // If a "script closure"
        if (signature.flags & 0x10000) {

            if (!signature.name.empty()) {
                string q = decoders::valid_id(signature.name) ? "" : "\"";

                body = "#script " + q + signature.name + q + '\n' + body;
            }

            return body;
        }

        string args_string = utils::string_join(args, ", ");
        string result = "function " + signature.name + '(' + args_string + ") {\n" + body + "\n}";

//        if (signature.name.empty()) {
//            result = '(' + result + ')';
//        }

        return result;
    }
}
```

## File: `src/jsxer/nodes/FunctionDeclaration.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class FunctionDeclaration : public AstNode {
    public:
        explicit FunctionDeclaration(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::FunctionDeclaration;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo bodyInfo;
        decoders::FunctionSignature signature;
        int flags = 0;
    };
}
```

## File: `src/jsxer/nodes/FunctionExpression.cpp`
```cpp
#include "FunctionExpression.h"

namespace jsxer::nodes {
    void FunctionExpression::parse() {
        lineInfo = decoders::d_line_info(reader);
        expression = decoders::d_node(reader);
    }

    string FunctionExpression::to_string() {
        return expression->to_string();
    }
}
```

## File: `src/jsxer/nodes/FunctionExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class FunctionExpression : public AstNode {
    public:
        explicit FunctionExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::FunctionExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo lineInfo;
        AstOpNode expression;
    };
}
```

## File: `src/jsxer/nodes/Identifier.cpp`
```cpp
#include "Identifier.h"

namespace jsxer::nodes {
    void Identifier::parse() {
        id = decoders::d_sid(reader);

        if (reader.version() >= JsxbinVersion::v20)
            unknown = reader.getBoolean();
    }

    string Identifier::to_string() {
        return id;
    }
}
```

## File: `src/jsxer/nodes/Identifier.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class Identifier : public AstNode {
    public:
        explicit Identifier(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::Identifier;
        }

        void parse() override;

        string to_string() override;

    private:
        string id;
        bool unknown = false;
    };
}
```

## File: `src/jsxer/nodes/IfStatement.cpp`
```cpp
#include "IfStatement.h"

namespace jsxer::nodes {
    void IfStatement::parse() {
        bodyInfo = decoders::d_line_info(reader);
        test = decoders::d_node(reader);
        otherwise = decoders::d_node(reader);
    }

    string IfStatement::to_string() {
        string result = bodyInfo.lbl_statement() + "if (" + test->to_string() + ") { \n"
                        + bodyInfo.create_body() + "\n}";

        if (otherwise == nullptr) {
            return result;
        }

        auto current = otherwise;

        while ((current->type() == NodeType::IfStatement) && std::dynamic_pointer_cast<IfStatement>(current)->otherwise != nullptr) {
            auto elif = std::dynamic_pointer_cast<IfStatement>(current);
            result += '\n' + elif->bodyInfo.lbl_statement() + "else if (" + elif->test->to_string() + ") {\n"
                      + elif->bodyInfo.create_body() + "\n}";

            current = elif->otherwise;
        }

        // WARN_ME: something feels wrong here...
        result += "\nelse {\n" + current->to_string() + "\n}";

        return result;
    }
}
```

## File: `src/jsxer/nodes/IfStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class IfStatement : public AstNode {
    public:
        explicit IfStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::IfStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo bodyInfo;
        AstOpNode test;
        AstOpNode otherwise;
    };
}
```

## File: `src/jsxer/nodes/IndexingExpression.cpp`
```cpp
#include "IndexingExpression.h"

namespace jsxer::nodes {
    void IndexingExpression::parse() {
        auto ref = decoders::d_literal_ref(reader); // <str, bool>
        auto name = decoders::d_node(reader);
        auto expr = decoders::d_node(reader);

        arrayName = name->to_string();
        expression = expr->to_string();
    }

    string IndexingExpression::to_string() {
        return arrayName + '[' + expression + ']';
    }
}
```

## File: `src/jsxer/nodes/IndexingExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class IndexingExpression : public AstNode {
    public:
        explicit IndexingExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::IndexingExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        string arrayName;
        string expression;
    };
}
```

## File: `src/jsxer/nodes/ListExpression.cpp`
```cpp
#include "ListExpression.h"
#include "LocalAssignmentExpression.h"

namespace jsxer::nodes {
    void ListExpression::parse() {
        arguments = decoders::d_children(reader);
        sequence_expr = reader.getBoolean();
    }

    void ListExpression::set_for_loop(bool x) {
        this->for_loop = x;
    }

    string ListExpression::to_string() {
        string result;

        string delimiter = ", ";

        // TODO: fix declarations
        for (int i = 0; i < arguments.size(); ++i) {
            if (for_loop && i > 0 && arguments[i]->type() == NodeType::LocalAssignmentExpression) {
                std::dynamic_pointer_cast<LocalAssignmentExpression>(arguments[i])->suppress_declarative_keyword(true);
            }

            result += arguments[i]->to_string() + (i + 1 == arguments.size() ? "" : delimiter);
        }

        if (sequence_expr && !for_loop) {
            result = '(' + result + ')';
        }

        return result;
    }
}
```

## File: `src/jsxer/nodes/ListExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"
#include <vector>

namespace jsxer::nodes {
    class ListExpression : public AstNode {
    public:
        explicit ListExpression(Reader &reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ListExpression;
        }

        void parse() override;

        void set_for_loop(bool x);

        string to_string() override;

        vector<AstOpNode> arguments;

    private:
        bool for_loop = false;
        bool sequence_expr = false;
    };

    using OpListExpression = std::shared_ptr<ListExpression>;
}
```

## File: `src/jsxer/nodes/LocalAssignmentExpression.cpp`
```cpp
#include "LocalAssignmentExpression.h"


namespace jsxer::nodes {
    void LocalAssignmentExpression::parse() {
        var_name = decoders::d_sid(reader);
        unsigned int type = (unsigned int) decoders::d_length(reader);
        expression = decoders::d_node(reader);
        literal = decoders::d_variant(reader);
        shorthand = reader.getBoolean();
        declaration = reader.getBoolean();
    }

    string LocalAssignmentExpression::to_string() {
        string result = (declaration && !declarative_suppress) ? "var " : "";

        if (shorthand) {
            auto b = std::dynamic_pointer_cast<BinaryExpression>(expression);

            string value_assigned = literal.empty() ? b->get_op() : literal;
            result += var_name + ' ' + b->get_op_name() + "= " + value_assigned;

            return result;
        }

        string value_assigned = literal.empty() ? expression->to_string() : literal;
        result += var_name + " = " + value_assigned;

        return result;
    }

    void LocalAssignmentExpression::suppress_declarative_keyword(bool value) {
        declarative_suppress = value;
    }
}
```

## File: `src/jsxer/nodes/LocalAssignmentExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "BinaryExpression.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class LocalAssignmentExpression : public AstNode {
    public:
        explicit LocalAssignmentExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::LocalAssignmentExpression;
        }

        void parse() override;

        string to_string() override;

        void suppress_declarative_keyword(bool value);

    private:
        string var_name;
        string literal;
        AstOpNode expression;
        bool declarative_suppress = false;
        bool shorthand = false;
        bool declaration = false;
    };
}
```

## File: `src/jsxer/nodes/LocalIdentifier.cpp`
```cpp
#include "LocalIdentifier.h"
#include "../util.h"

namespace jsxer::nodes {
    void LocalIdentifier::parse() {
        reference = decoders::d_id_ref(reader);
        _type = decoders::d_length(reader);
    }

    string LocalIdentifier::to_string() {
        return utils::to_string(reference.id);
    }
}
```

## File: `src/jsxer/nodes/LocalIdentifier.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class LocalIdentifier : public AstNode {
    public:
        explicit LocalIdentifier(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::LocalIdentifier;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::Reference reference;
        int _type = 0;
    };
}
```

## File: `src/jsxer/nodes/LocalUpdateExpression.cpp`
```cpp
#include "LocalUpdateExpression.h"


namespace jsxer::nodes {
    void LocalUpdateExpression::parse() {
        id = decoders::d_sid(reader);
        length = decoders::d_length(reader);
        operation = decoders::d_number(reader);
        postfix = reader.getBoolean();
    }

    string LocalUpdateExpression::to_string() {
        string op = operation == "1" ? "++" : "--";
        return postfix ? id + op : op + id;
    }
}
```

## File: `src/jsxer/nodes/LocalUpdateExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class LocalUpdateExpression : public AstNode {
    public:
        explicit LocalUpdateExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::LocalUpdateExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        string id;
        size_t length = 0;
        string operation;
        bool postfix = false;
    };
}
```

## File: `src/jsxer/nodes/LogicalExpression.cpp`
```cpp
#include "LogicalExpression.h"

namespace jsxer::nodes {
    string get_expr(const AstOpNode& node, const string &literal) {
        return '(' + (node == nullptr ? literal : node->to_string()) + ')';
    }

    void LogicalExpression::parse() {
        // opName is either "&&" or "||"
        opName = decoders::d_operator(reader);
        leftExpr = decoders::d_node(reader);
        rightExpr = decoders::d_node(reader);
        leftLiteral = decoders::d_variant(reader);
        rightLiteral = decoders::d_variant(reader);
    }

    string LogicalExpression::to_string() {
        return get_expr(leftExpr, leftLiteral) + ' ' + opName + ' ' + get_expr(rightExpr, rightLiteral);
    }
}
```

## File: `src/jsxer/nodes/LogicalExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class LogicalExpression : public AstNode {
    public:
        explicit LogicalExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::LogicalExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        string opName;
        AstOpNode leftExpr;
        AstOpNode rightExpr;
        string leftLiteral;
        string rightLiteral;
    };
}
```

## File: `src/jsxer/nodes/MemberExpression.cpp`
```cpp
#include "MemberExpression.h"
#include "../util.h"

namespace jsxer::nodes {
    void MemberExpression::parse() {
        memberInfo = decoders::d_literal_ref(reader);
        objInfo = decoders::d_node(reader);
    }

    string MemberExpression::to_string() {
        string result = (objInfo == nullptr ? "" : objInfo->to_string());

        if (decoders::is_integer(result) || (objInfo->type() == NodeType::BinaryExpression)) {
            result = '(' + result + ')';
        }

        if (objInfo->type() == NodeType::AssignmentExpression || objInfo->type() == NodeType::LocalAssignmentExpression)
            result = '(' + result + ')';

        // Check member validity...
        if (decoders::valid_id(memberInfo.id)) {
            result += '.' + utils::to_string(memberInfo.id);
            return result;
        }

        if (decoders::valid_xml_attribute(memberInfo.id)) {
            result += '.' + utils::to_string(memberInfo.id);
            return result;
        }

        result += '[';
        // check if ID can be converted to an integer...
        if (decoders::is_integer(memberInfo.id)) {
            result += utils::to_string(memberInfo.id);
        } else {
            result += utils::to_string_literal(memberInfo.id);
        }
        result += ']';


        return result;
    }
}
```

## File: `src/jsxer/nodes/MemberExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

#include <cstdlib>

namespace jsxer::nodes {
    class MemberExpression : public AstNode {
    public:
        explicit MemberExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::MemberExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::Reference memberInfo;
        AstOpNode objInfo;
    };
}
```

## File: `src/jsxer/nodes/ObjectExpression.cpp`
```cpp
#include "ObjectExpression.h"
#include "../util.h"


namespace jsxer::nodes {
    void ObjectExpression::parse() {
        objectId = decoders::d_sid(reader);

        size_t child_count = decoders::d_length(reader);

        for (int i = 0; i < child_count; ++i) {
            string id = decoders::d_sid(reader);
            AstOpNode node = decoders::d_node(reader);
            properties[id] = node;
        }
    }

    string ObjectExpression::to_string() {
        string result = "{";

        if (!properties.empty()) {
            int i = 0;
            for (std::pair<string, AstOpNode> entry: properties) {
                if (!decoders::valid_id(entry.first)) {
                    result += utils::to_string_literal(entry.first);
                } else {
                    result += entry.first;
                }

                result += ": " + entry.second->to_string();

                if ((i + 1) < properties.size())
                    result += ", ";

                i++;
            }
        }

        return result + '}';
    }
}
```

## File: `src/jsxer/nodes/ObjectExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"
#include <algorithm>

namespace jsxer::nodes {
    class ObjectExpression : public AstNode {
    public:
        explicit ObjectExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ObjectExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        string objectId;
        map<string, AstOpNode> properties;
    };
}
```

## File: `src/jsxer/nodes/Program.cpp`
```cpp
#include "Program.h"

namespace jsxer::nodes {
    void Program::parse() {
        body = decoders::d_node(reader);
    }

    string Program::to_string() {
        return body->to_string();
    }
}
```

## File: `src/jsxer/nodes/Program.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class Program : AstNode {
    public:
        explicit Program(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::Program;
        }

        void parse() override;

        string to_string() override;

    private:
        AstOpNode body;
    };
}
```

## File: `src/jsxer/nodes/RegExpLiteral.cpp`
```cpp
#include "RegExpLiteral.h"
#include "../util.h"


namespace jsxer::nodes {
    void RegExpLiteral::parse() {
        regex = utils::to_string(reader.getString());
        flags = utils::to_string(reader.getString());
    }

    string RegExpLiteral::to_string() {
        return '/' + regex + '/' + flags;
    }
}
```

## File: `src/jsxer/nodes/RegExpLiteral.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class RegExpLiteral : public AstNode {
    public:
        explicit RegExpLiteral(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::RegExpLiteral;
        }

        void parse() override;

        string to_string() override;

    private:
        string regex;
        string flags;
    };
}
```

## File: `src/jsxer/nodes/ReturnStatement.cpp`
```cpp
#include "ReturnStatement.h"

namespace jsxer::nodes {
    void ReturnStatement::parse() {
        lineInfo = decoders::d_line_info(reader);
        expression = decoders::d_node(reader);
    }

    string ReturnStatement::to_string() {
        string result = expression == nullptr ? "" : ' ' + expression->to_string();
        result = lineInfo.lbl_statement() + "return" + result + ';';

        return result;
    }
}
```

## File: `src/jsxer/nodes/ReturnStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class ReturnStatement : public AstNode {
    public:
        explicit ReturnStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ReturnStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo lineInfo;
        AstOpNode expression;
    };
}
```

## File: `src/jsxer/nodes/SimpleForStatement.cpp`
```cpp
#include "SimpleForStatement.h"

namespace jsxer::nodes {
    void SimpleForStatement::parse() {
        bodyInfo = decoders::d_line_info(reader);
        loopVar = decoders::d_node(reader);
        iteratorInitial = decoders::d_number(reader);
        upperBound = decoders::d_node(reader);
        stepSize = decoders::d_number(reader);
        length = decoders::d_length(reader);
        comparisonOperator = decoders::d_sid(reader);
    }

    string SimpleForStatement::to_string() {
        string result;
        string varname = loopVar->to_string();
        result += bodyInfo.lbl_statement();
        result += "for (var ";
        result += varname + " = " + iteratorInitial + "; ";
        result += varname + ' ' + comparisonOperator + ' ' + upperBound->to_string() + "; ";

        result += varname + " += " + stepSize;
        result += ") { \n" + bodyInfo.create_body() + '}';

        return result;
    }
}
```

## File: `src/jsxer/nodes/SimpleForStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class SimpleForStatement : public AstNode {
    public:
        explicit SimpleForStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::SimpleForStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo bodyInfo;
        AstOpNode loopVar;
        string iteratorInitial;
        AstOpNode upperBound;
        string stepSize;
        size_t length{};
        string comparisonOperator;
    };
}
```

## File: `src/jsxer/nodes/StatementList.cpp`
```cpp
#include "StatementList.h"


namespace jsxer::nodes {
    void StatementList::parse() {
        body = decoders::d_line_info(reader);

        length = decoders::d_length(reader);
        for (int i = 0; i < length; ++i) {
            statements.push_back(decoders::d_node(reader));
        }

        auto children = decoders::d_children(reader);
        statements.insert(statements.end(), children.begin(), children.end());
    }

    string StatementList::to_string() {
        string result;

        // A seemingly useless sorting step (by line number of statements) happens here (where this comment is) in the original project,
        // but I removed it. We'll see what happens when I test it...

        for (int i = 0; i < statements.size(); ++i) {
            string expression = statements[i]->to_string();

//        if (statements[i]->type() == NodeType::ExpressionStatement)
//            expression += ';';

            result += expression;

            if ((i + 1) < statements.size())
                result += '\n';
        }

        return body.lbl_statement() + result;
    }
}
```

## File: `src/jsxer/nodes/StatementList.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"
#include <algorithm>

namespace jsxer::nodes {
    class StatementList : public AstNode {
    public:
        explicit StatementList(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::StatementList;
        }

        void parse() override;

        string to_string() override;

    private:
        size_t length{};
        decoders::LineInfo body;
        vector<AstOpNode> statements;
    };
}
```

## File: `src/jsxer/nodes/SwitchStatement.cpp`
```cpp
#include "SwitchStatement.h"

namespace jsxer::nodes {
    void SwitchStatement::parse() {
        lineInfo = decoders::d_line_info(reader);
        switchValue = decoders::d_node(reader);

        size_t len_cases = decoders::d_length(reader);
        for (int i = 0; i < len_cases; ++i) {
            auto node = decoders::d_node(reader);
            if (node != nullptr) {
                cases.push_back(node);
            }
        }

        size_t len_implementations = decoders::d_length(reader);
        for (int i = 0; i < len_implementations; ++i) {
            auto node = decoders::d_node(reader);
            if (node != nullptr) {
                implementations.push_back(node);
            }
        }

    }

    string SwitchStatement::to_string() {
        string result = "switch (" + switchValue->to_string() + ") { \n";

        for (int i = 0; i < cases.size(); ++i) {
            vector<AstOpNode> caseArgs = std::dynamic_pointer_cast<ListExpression>(cases[i])->arguments;
            if (!caseArgs.empty()) {
                for (const auto& arg: caseArgs) {
                    result += "case " + arg->to_string() + ":\n";
                }
            } else {
                result += "default:\n";
            }

            // now for each case implementation...
            if (i < implementations.size()) {
                result += implementations[i]->to_string() + '\n';
            }
        }
        result += '}';

        return result;
    }
}
```

## File: `src/jsxer/nodes/SwitchStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"
#include "ListExpression.h"

namespace jsxer::nodes {
    class SwitchStatement : public AstNode {
    public:
        explicit SwitchStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::SwitchStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo lineInfo;
        AstOpNode switchValue;
        vector<AstOpNode> cases;
        vector<AstOpNode> implementations;
    };
}
```

## File: `src/jsxer/nodes/TernaryExpression.cpp`
```cpp
#include "TernaryExpression.h"


namespace jsxer::nodes {
    bool parenthesis(const AstOpNode& node) {
        return (node->type() == NodeType::TernaryExpression) && (node->type() == NodeType::ListExpression);
    }

    void TernaryExpression::parse() {
        condition = decoders::d_node(reader);
        node_true = decoders::d_node(reader);
        node_false = decoders::d_node(reader);
    }

    string TernaryExpression::to_string() {
        return condition->to_string() + " ? " +
               (parenthesis(node_true) ? '(' + node_true->to_string() + ')' : node_true->to_string())
               + " : "
               + (parenthesis(node_false) ? '(' + node_false->to_string() + ')' : node_false->to_string());
    }
}
```

## File: `src/jsxer/nodes/TernaryExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class TernaryExpression : public AstNode {
    public:
        explicit TernaryExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::TernaryExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        AstOpNode condition;
        AstOpNode node_true;
        AstOpNode node_false;
    };
}
```

## File: `src/jsxer/nodes/ThisExpression.cpp`
```cpp
#include "ThisExpression.h"
#include "../util.h"

namespace jsxer::nodes {
    void ThisExpression::parse() {
        reference = decoders::d_literal_ref(reader);
    }

    string ThisExpression::to_string() {
        // return utils::to_string(reference.id);
        return "this";
    }
}
```

## File: `src/jsxer/nodes/ThisExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class ThisExpression : public AstNode {
    public:
        explicit ThisExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ThisExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::Reference reference;
    };
}
```

## File: `src/jsxer/nodes/ThrowStatement.cpp`
```cpp
#include "ThrowStatement.h"

namespace jsxer::nodes {
    void ThrowStatement::parse() {
        lineInfo = decoders::d_line_info(reader);
        expression = decoders::d_node(reader);
    }

    string ThrowStatement::to_string() {
        return "throw " + expression->to_string() + ';';
    }
}
```

## File: `src/jsxer/nodes/ThrowStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class ThrowStatement : public AstNode {
    public:
        explicit ThrowStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::ThrowStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo lineInfo;
        AstOpNode expression;
    };
}
```

## File: `src/jsxer/nodes/TryStatement.cpp`
```cpp
#include "TryStatement.h"

namespace jsxer::nodes {
    void TryStatement::parse() {
        tryBlock = decoders::d_line_info(reader);
        length = decoders::d_length(reader);
        finallyBlock = decoders::d_node(reader);

        for (int i = 0; i < length; ++i) {
            layers.push_back({decoders::d_sid(reader),
                              decoders::d_node(reader),
                              decoders::d_node(reader)});
        }
    }

    string TryStatement::to_string() {
        string result = tryBlock.lbl_statement() + "try {\n";
        result += tryBlock.create_body() + '\n';

        for (const auto& layer : layers) {
            result += "} catch (" + layer.arg;

            if (layer.exceptionFilter != nullptr)
                result += " if " + layer.exceptionFilter->to_string();

            result += ") {" + (layer.catchBlock == nullptr ? "" : layer.catchBlock->to_string()) + '\n';
        }

        if (finallyBlock != nullptr) {
            result += "} finally {\n";
            result += finallyBlock->to_string();
            result += '\n';
        }
        result += '}';

        return result;
    }
}
```

## File: `src/jsxer/nodes/TryStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class TryStatement : public AstNode {
    public:
        explicit TryStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::TryStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        struct TryCatchLayer {
            string arg;
            AstOpNode exceptionFilter;
            AstOpNode catchBlock;
        };

        decoders::LineInfo tryBlock;
        AstOpNode finallyBlock;
        vector<TryCatchLayer> layers;
        size_t length{};
    };
}
```

## File: `src/jsxer/nodes/UnaryExpression.cpp`
```cpp
#include "UnaryExpression.h"

namespace jsxer::nodes {
    void UnaryExpression::parse() {
        op = decoders::d_operator(reader);
        expression = decoders::d_node(reader);
    }

    string UnaryExpression::to_string() {
        bool parenthesis = expression->type() != NodeType::Identifier
                           && expression->type() != NodeType::LocalIdentifier
                           && expression->type() != NodeType::CallExpression
                           && expression->type() != NodeType::MemberExpression
                           && expression->type() != NodeType::IndexingExpression;

    // if plus ("+") is used as a unary operator, simply ignore it.
    if (op != "+")
        return op + (parenthesis ? '(' + expression->to_string() + ')' : expression->to_string());
    else
        return (parenthesis ? '(' + expression->to_string() + ')' : expression->to_string());
    }
}
```

## File: `src/jsxer/nodes/UnaryExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class UnaryExpression : public AstNode {
    public:
        explicit UnaryExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::UnaryExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        string op;
        AstOpNode expression;
    };
}
```

## File: `src/jsxer/nodes/UnaryRefExpression.cpp`
```cpp
#include "UnaryRefExpression.h"

namespace jsxer::nodes {
    void UnaryRefExpression::parse() {
        name = decoders::d_operator(reader);
        argument = decoders::d_node(reader);
    }

    string UnaryRefExpression::to_string() {
        return name + ' ' + argument->to_string();
    }
}
```

## File: `src/jsxer/nodes/UnaryRefExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class UnaryRefExpression : public AstNode {
    public:
        explicit UnaryRefExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::UnaryRefExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        string name;
        AstOpNode argument;
    };
}
```

## File: `src/jsxer/nodes/UpdateExpression.cpp`
```cpp
#include "UpdateExpression.h"

namespace jsxer::nodes {
    void UpdateExpression::parse() {
        variable = decoders::d_node(reader);
        operation = decoders::d_literal_num(reader);
        postfix = reader.getBoolean();
    }

    string UpdateExpression::to_string() {
        string op = operation == 1 ? "++" : "--";
        return postfix ? variable->to_string() + op : op + variable->to_string();
    }
}
```

## File: `src/jsxer/nodes/UpdateExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class UpdateExpression : public AstNode {
    public:
        explicit UpdateExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::UpdateExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        AstOpNode variable;
        int operation = 0;
        bool postfix = false;
    };
}
```

## File: `src/jsxer/nodes/VoidExpression.cpp`
```cpp
#include "VoidExpression.h"

namespace jsxer::nodes {
    void VoidExpression::parse() {
        defaultNamespaceFxnCall = decoders::d_node(reader);
    }

    string VoidExpression::to_string() {
        return defaultNamespaceFxnCall->to_string();
    }
}
```

## File: `src/jsxer/nodes/VoidExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class VoidExpression : public AstNode {
    public:
        explicit VoidExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::VoidExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        AstOpNode defaultNamespaceFxnCall;
    };
}
```

## File: `src/jsxer/nodes/WhileStatement.cpp`
```cpp
#include "WhileStatement.h"

namespace jsxer::nodes {
    void WhileStatement::parse() {
        bodyInfo = decoders::d_line_info(reader);
        condition = decoders::d_node(reader);
    }

    string WhileStatement::to_string() {
        string result = bodyInfo.lbl_statement() + "while (" +
                        (condition == nullptr ? "true" : condition->to_string()) + ") {\n";

        result += bodyInfo.create_body() + "\n}";

        return result;
    }
}
```

## File: `src/jsxer/nodes/WhileStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class WhileStatement : public AstNode {
    public:
        explicit WhileStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::WhileStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo bodyInfo;
        AstOpNode condition;
    };
}
```

## File: `src/jsxer/nodes/WithStatement.cpp`
```cpp
#include "WithStatement.h"

namespace jsxer::nodes {
    void WithStatement::parse() {
        bodyInfo = decoders::d_line_info(reader);
        object = decoders::d_node(reader);
    }

    string WithStatement::to_string() {
        return bodyInfo.lbl_statement() + "with (" + object->to_string() + ") {\n" + bodyInfo.create_body() + "\n}";
    }
}
```

## File: `src/jsxer/nodes/WithStatement.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class WithStatement : public AstNode {
    public:
        explicit WithStatement(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::WithStatement;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::LineInfo bodyInfo;
        AstOpNode object;
    };
}
```

## File: `src/jsxer/nodes/XMLConstantExpression.cpp`
```cpp
#include "XMLConstantExpression.h"

namespace jsxer::nodes {
    void XMLConstantExpression::parse() {
        size_t length = decoders::d_length(reader);

        for (int i = 0; i < length; ++i) {
            AstOpNode child_node = decoders::d_node(reader);
            size_t child_length = decoders::d_length(reader);
            children[child_node] = child_length;
        }
    }

    string XMLConstantExpression::to_string() {
        static const int TYPE_NORMAL = 0;
        static const int TYPE_ELEM_PLACEHOLDER = 1;
        static const int TYPE_ATTR_PLACEHOLDER = 2;
        static const int TYPE_VALUE_PLACEHOLDER = 3;

        string result;

        std::vector<AstOpNode> normals;
        std::vector<AstOpNode> placeholders;

        for (const auto &child: children){
            if (child.second == TYPE_NORMAL){
                normals.push_back(child.first);
                continue;
            }
            placeholders.push_back(child.first);
        }

        if (normals.size() != placeholders.size() + 1 && children.size() > 1)
            return "// Jsxer: XMLConstantExpression syntax recovery failed.";

        for (int i = 0; i < children.size(); ++i) {
            if (!(i & 1)) {
                AstOpNode normal = normals[i / 2];

                result += utils::from_string_literal(normal->to_string());
                continue;
            }
            string placeholder = placeholders[i / 2]->to_string();
            placeholder.erase(placeholder.size()-1, 1);
            result += '{' + placeholder + '}';
        }

        return result;
    }
}
```

## File: `src/jsxer/nodes/XMLConstantExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class XMLConstantExpression : public AstNode {
    public:
        explicit XMLConstantExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::XMLConstantExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        map<AstOpNode, unsigned long> children;
    };
}
```

## File: `src/jsxer/nodes/XMLDescendantsExpression.cpp`
```cpp
#include "XMLDescendantsExpression.h"
#include "../util.h"

namespace jsxer::nodes {
    void XMLDescendantsExpression::parse() {
        descendants = decoders::d_literal_ref(reader);
        object = decoders::d_node(reader);

        decoders::d_node(reader);
        decoders::d_node(reader);
    }

    string XMLDescendantsExpression::to_string() {
        return object->to_string() + ".." + utils::to_string(descendants.id);
    }
}
```

## File: `src/jsxer/nodes/XMLDescendantsExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class XMLDescendantsExpression : public AstNode {
    public:
        explicit XMLDescendantsExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::XMLDescendantsExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::Reference descendants;
        AstOpNode object;
    };
}
```

## File: `src/jsxer/nodes/XMLPredicateExpression.cpp`
```cpp
#include "XMLPredicateExpression.h"

namespace jsxer::nodes {
    void XMLPredicateExpression::parse() {
        reference = decoders::d_literal_ref(reader);
        object = decoders::d_node(reader);
        member = decoders::d_node(reader);
    }

    string XMLPredicateExpression::to_string() {

        bool parenthesis = member->type() == NodeType::BinaryExpression
                           || member->type() == NodeType::LogicalExpression
                           || member->type() == NodeType::UnaryExpression;

        return object->to_string() + '.'
               + (parenthesis ? '(' + member->to_string() + ')' : member->to_string());
    }
}
```

## File: `src/jsxer/nodes/XMLPredicateExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class XMLPredicateExpression : public AstNode {
    public:
        explicit XMLPredicateExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::XMLPredicateExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::Reference reference;
        AstOpNode object;
        AstOpNode member;
    };
}
```

## File: `src/jsxer/nodes/XMLQualifiedNameExpression.cpp`
```cpp
#include "XMLQualifiedNameExpression.h"
#include "../util.h"

namespace jsxer::nodes {
    void XMLQualifiedNameExpression::parse() {
        namespaceObject = decoders::d_literal_ref(reader);
        object = decoders::d_node(reader);
        decoders::d_node(reader);
        decoders::d_node(reader);
        xmlId = decoders::d_sid(reader);
    }

    string XMLQualifiedNameExpression::to_string() {
        auto ns_id = utils::to_string(namespaceObject.id);
        string ns = namespaceObject.flag ? '@' + ns_id : ns_id;
        return object->to_string() + '.' + ns + "::" + xmlId;
    }
}
```

## File: `src/jsxer/nodes/XMLQualifiedNameExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class XMLQualifiedNameExpression : public AstNode {
    public:
        explicit XMLQualifiedNameExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::XMLQualifiedNameExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        decoders::Reference namespaceObject;
        AstOpNode object;
        string xmlId;
    };
}
```

## File: `src/jsxer/nodes/XMLUnaryRefExpression.cpp`
```cpp
#include "XMLUnaryRefExpression.h"

namespace jsxer::nodes {
    void XMLUnaryRefExpression::parse() {
        id = decoders::d_sid(reader);
        node = decoders::d_node(reader);
    }

    string XMLUnaryRefExpression::to_string() {
        return "// XMLUnaryRefExpression has no known syntactic representation.\n"
               "// To help add this, please create an issue on the Jsxer GitHub repository with the binary version\n"
               "// of this script attached, so that it can be researched. Thank you! <3\n"
               "// Create an issue here: https://github.com/AngeloD2022/jsxer";
    }
}
```

## File: `src/jsxer/nodes/XMLUnaryRefExpression.h`
```c
#pragma once

#include "AstNode.h"
#include "../decoders.h"

namespace jsxer::nodes {
    class XMLUnaryRefExpression : public AstNode {
    public:
        explicit XMLUnaryRefExpression(Reader& reader) : AstNode(reader) {}

        NodeType type() override {
            return NodeType::XMLUnaryRefExpression;
        }

        void parse() override;

        string to_string() override;

    private:
        string id;
        AstOpNode node;
    };
}
```

## File: `src/jsxer/nodes/node-types.h`
```c
#pragma once

#include <cstdint>

#include "../common.h"

namespace jsxer::nodes {
    enum class NodeType : uint8_t {
        Invalid = (uint8_t) -1,

        Program = '\x00',

        ArrayExpression = 'A',
        AssignmentExpression = 'B',
        BinaryExpression = 'C',
        BreakStatement = 'D',
        CallExpression = 'E',
        ConstantLiteral = 'F',
        ConstAssignment = 'G',
        DebuggerStatement = 'H',
        DoWhileStatement = 'I',
        ExpressionStatement = 'J',
        ForStatement = 'K',
        ForInStatement = 'L',
        FunctionDeclaration = 'M',
        FunctionExpression = 'N',
        IfStatement = 'O',
        UpdateExpression = 'P',
        IndexingExpression = 'Q',
        ListExpression = 'R',
        LocalAssignmentExpression = 'S',
        LocalUpdateExpression = 'T',
        LogicalExpression = 'U',
        LocalIdentifier = 'V',
        ObjectExpression = 'W',
        MemberExpression = 'X',
        RegExpLiteral = 'Y',
        ReturnStatement = 'Z',

        SimpleForStatement = 'a',
        StatementList = 'b',
        SwitchStatement = 'c',
        TernaryExpression = 'd',
        ThisExpression = 'e',
        ThrowStatement = 'f',
        TryStatement = 'g',
        UnaryExpression = 'h',
        UnaryRefExpression = 'i',
        Identifier = 'j',
        VoidExpression = 'k',
        WhileStatement = 'l',
        WithStatement = 'm',

        EmptyExpression = 'n',

        XMLConstantExpression = 'o',
        XMLQualifiedNameExpression = 'p',
        XMLDescendantsExpression = 'q',
        XMLPredicateExpression = 'r',
        XMLUnaryRefExpression = 's',
    };
}
```

## File: `src/jsxer/nodes/nodes.h`
```c
#pragma once

#include "AstNode.h"

#include "ListExpression.h"
#include "ArrayExpression.h"
#include "IndexingExpression.h"
#include "LocalAssignmentExpression.h"
#include "BinaryExpression.h"
#include "TernaryExpression.h"
#include "ConstAssignment.h"
#include "DebuggerStatement.h"
#include "UnaryRefExpression.h"
#include "DoWhileStatement.h"
#include "ExpressionStatement.h"
#include "ForInStatement.h"
#include "SimpleForStatement.h"
#include "ForStatement.h"
#include "CallExpression.h"
#include "FunctionDeclaration.h"
#include "FunctionExpression.h"
#include "Identifier.h"
#include "LocalIdentifier.h"
#include "IfStatement.h"
#include "LocalUpdateExpression.h"
#include "UpdateExpression.h"
#include "BreakStatement.h"
#include "LogicalExpression.h"
#include "AssignmentExpression.h"
#include "MemberExpression.h"
#include "ObjectExpression.h"
#include "RegExpLiteral.h"
#include "ReturnStatement.h"
#include "VoidExpression.h"
#include "StatementList.h"
#include "SwitchStatement.h"
#include "ThisExpression.h"
#include "ThrowStatement.h"
#include "TryStatement.h"
#include "UnaryExpression.h"
#include "XMLUnaryRefExpression.h"
#include "ConstantLiteral.h"
#include "WhileStatement.h"
#include "WithStatement.h"
#include "XMLPredicateExpression.h"
#include "XMLConstantExpression.h"
#include "XMLDescendantsExpression.h"
#include "XMLQualifiedNameExpression.h"

namespace jsxer::nodes {
    AstOpNode get(NodeType type, Reader &reader) {
        switch (type) {
            case NodeType::ArrayExpression:
                return std::make_shared<ArrayExpression>(reader);
            case NodeType::AssignmentExpression:
                return std::make_shared<AssignmentExpression>(reader);
            case NodeType::BinaryExpression:
                return std::make_shared<BinaryExpression>(reader);
            case NodeType::BreakStatement:
                return std::make_shared<BreakStatement>(reader);
            case NodeType::CallExpression:
                return std::make_shared<CallExpression>(reader);
            case NodeType::ConstantLiteral:
                return std::make_shared<ConstantLiteral>(reader);
            case NodeType::ConstAssignment:
                return std::make_shared<ConstAssignment>(reader);
            case NodeType::DebuggerStatement:
                return std::make_shared<DebuggerStatement>(reader);
            case NodeType::DoWhileStatement:
                return std::make_shared<DoWhileStatement>(reader);
            case NodeType::ExpressionStatement:
                return std::make_shared<ExpressionStatement>(reader);
            case NodeType::ForStatement:
                return std::make_shared<ForStatement>(reader);
            case NodeType::ForInStatement:
                return std::make_shared<ForInStatement>(reader);
            case NodeType::FunctionDeclaration:
                return std::make_shared<FunctionDeclaration>(reader);
            case NodeType::FunctionExpression:
                return std::make_shared<FunctionExpression>(reader);
            case NodeType::IfStatement:
                return std::make_shared<IfStatement>(reader);
            case NodeType::UpdateExpression:
                return std::make_shared<UpdateExpression>(reader);
            case NodeType::IndexingExpression:
                return std::make_shared<IndexingExpression>(reader);
            case NodeType::ListExpression:
                return std::make_shared<ListExpression>(reader);
            case NodeType::LocalAssignmentExpression:
                return std::make_shared<LocalAssignmentExpression>(reader);
            case NodeType::LocalUpdateExpression:
                return std::make_shared<LocalUpdateExpression>(reader);
            case NodeType::LogicalExpression:
                return std::make_shared<LogicalExpression>(reader);
            case NodeType::LocalIdentifier:
                return std::make_shared<LocalIdentifier>(reader);
            case NodeType::ObjectExpression:
                return std::make_shared<ObjectExpression>(reader);
            case NodeType::MemberExpression:
                return std::make_shared<MemberExpression>(reader);
            case NodeType::RegExpLiteral:
                return std::make_shared<RegExpLiteral>(reader);
            case NodeType::ReturnStatement:
                return std::make_shared<ReturnStatement>(reader);

            case NodeType::SimpleForStatement:
                return std::make_shared<SimpleForStatement>(reader);
            case NodeType::StatementList:
                return std::make_shared<StatementList>(reader);
            case NodeType::SwitchStatement:
                return std::make_shared<SwitchStatement>(reader);
            case NodeType::TernaryExpression:
                return std::make_shared<TernaryExpression>(reader);
            case NodeType::ThisExpression:
                return std::make_shared<ThisExpression>(reader);
            case NodeType::ThrowStatement:
                return std::make_shared<ThrowStatement>(reader);
            case NodeType::TryStatement:
                return std::make_shared<TryStatement>(reader);
            case NodeType::UnaryExpression:
                return std::make_shared<UnaryExpression>(reader);
            case NodeType::UnaryRefExpression:
                return std::make_shared<UnaryRefExpression>(reader);
            case NodeType::Identifier:
                return std::make_shared<Identifier>(reader);
            case NodeType::VoidExpression:
                return std::make_shared<VoidExpression>(reader);
            case NodeType::WhileStatement:
                return std::make_shared<WhileStatement>(reader);
            case NodeType::WithStatement:
                return std::make_shared<WithStatement>(reader);

            // Note: need to do some empty expr tests before uncommenting this
            // case NodeType::EmptyExpression:
            //    return std::make_shared<EmptyExpression>(reader);

            case NodeType::XMLConstantExpression:
                return std::make_shared<XMLConstantExpression>(reader);
            case NodeType::XMLQualifiedNameExpression:
                return std::make_shared<XMLQualifiedNameExpression>(reader);
            case NodeType::XMLDescendantsExpression:
                return std::make_shared<XMLDescendantsExpression>(reader);
            case NodeType::XMLPredicateExpression:
                return std::make_shared<XMLPredicateExpression>(reader);
            case NodeType::XMLUnaryRefExpression:
                return std::make_shared<XMLUnaryRefExpression>(reader);
            default:
                return nullptr;
        }
    }
}
```

## File: `tests/data/jsx/README.txt`
```
Pre-compiled jsx files goes here.
```

## File: `tests/data/jsx/array-expr.jsx`
```jsx
[1, 2, 3, 4, 5];
```

## File: `tests/data/jsxbin/README.txt`
```
Compiled jsxbin and de-compiled jsx files goes here.
```

## File: `tests/src/array-expr.cpp`
```cpp
#include <jsxer.h>

const char compiled[] = "@JSXBIN@ES@2.0@MyBbyBn0ABJAnAARFFdBFdCFdDFdEFdFf0DzABByB";

int main() {
    string decompiled;
    int err = jsxer::decompile(compiled, decompiled);

    printf("--------------------------------------------------\n");
    printf("%s\n", decompiled.c_str());
    printf("--------------------------------------------------\n");

    return err;
}
```

## File: `tests/src/common.h`
```c
#pragma once

#include <string>

#include <jsxer.h>

namespace jsxer::test {
    int decompile(const std::string& compiled, std::string& decompiled, const std::string& source = "") {
        int err = jsxer::decompile_test(compiled, decompiled);

        if (!source.empty()) {
            printf("--------------------- Source ---------------------\n");
            printf("%s\n", source.c_str());
        }

        printf("------------------- Decompiled -------------------\n");
        printf("%s\n", decompiled.c_str());
        printf("--------------------------------------------------\n");

        return err;
    }
}
```

## File: `tests/src/exp.cpp`
```cpp
#include <jsxer.h>

const char compiled[] = "@JSXBIN@ES@2.1@MyBbyBn0ACJAnASzBjWByBnd8lYmNmRkUlLiRiXiAftJBnAEjzFjQjSjJjOjUCfRBVBfyBffABB40BiAABAzADByB";

int main() {
    string decompiled;
    int err = jsxer::decompile(compiled, decompiled);

    printf("--------------------------------------------------\n");
    printf("%s\n", decompiled.c_str());
    printf("--------------------------------------------------\n");

    return err;
}
```

## File: `tests/src/for-stmt.cpp`
```cpp
#include <jsxer.h>

const char compiled[] = "@JSXBIN@ES@2.0@MyBbyBn0ABKAbyCn0ABKCbyEn0ABOEbyFn0ABDFnAzEiMiCiMhRBfACzChdhdCQzA\n"
                        "DfjzBjSEfjzBjYFfQDfezEjUjIjJjTGfVzBjJHfyBnnbyIn0ABDInAzEiMiCiMhSIfBIRCSzBjKJyBn\n"
                        "dAftSzBjZKyBXzGjMjFjOjHjUjILfjzBjCMfnfttCzBhcNjFfVKfyBnnTJyBBtBBRCSHyBndAftSzBj\n"
                        "OOyBXLfjzBjBPfnfttCNVHfyBVOfyBnnTHyBBtAEH40BiAK4D0AiAJ4C0AiAO4B0AiAAEADByB";

int main() {
    string decompiled;
    int err = jsxer::decompile(compiled, decompiled);

    printf("--------------------------------------------------\n");
    printf("%s\n", decompiled.c_str());
    printf("--------------------------------------------------\n");

    return err;
}
```

## File: `tests/src/member-expr.cpp`
```cpp
#include <jsxer.h>

const char compiled[] = "@JSXBIN@ES@2.0@MyBbyBn0AIJBnAXzB2jEhHBfjzBjRCfJCnAXzB2lNmeDfjCfJDnAXzBhQEfjzBjBF\n"
                        "fJEnAXzHhShVhVhShThWjQGfjzBjCHfJFnAXzEjQjSjPjQIfjzBjYJfJGnAXzGhEjJjEjIjEjHKfjJf\n"
                        "JHnAXzGifjTjJjGjIjJLfjJfJInAEXzIjUjPiTjUjSjJjOjHMfFd2nIDnf0DzANByB";

int main() {
    string decompiled;
    int err = jsxer::decompile(compiled, decompiled);

    printf("--------------------------------------------------\n");
    printf("%s\n", decompiled.c_str());
    printf("--------------------------------------------------\n");

    return err;
}
```

## File: `tests/src/n2s-formatting.cpp`
```cpp
#include "./common.h"

const char source[] = R"(
var k = [
    0,
    123,
    -456,
    7.89,
    -0.123,
    1.23e6,
    -4.56e-7,

    1.7976931348623157e+308,
    -1.7976931348623157e+308,
];
)";

const char compiled[] = R"(
@JSXBIN@ES@2.0@MyBbyBn0ABJGnASzBjLByBARJFdAFdjbFdy2mIBFd8kPmCnVhIickPgfiAFd8lQjS
jIkRnNjclflfFd4lQmESAFd8hZhOkFhVFkakeleFd8nfnfnfnfnfnfnPjfFd8nfnfnfnfnfnfnPnffn
ftABB40BiAABAzACByB
)";

int main() {
    string decompiled;

    int err = jsxer::test::decompile(compiled, decompiled, source);

    return err;
}
```

## File: `tests/src/obj-expr.cpp`
```cpp
#include <jsxer.h>

const char compiled[] = "@JSXBIN@ES@2.0@MyBbyBn0ADJAnABjzDiHjJjYBfWzGiPjCjKjFjDjUCEzADFeFjXjCjFjUjWDARFFd\n"
                        "BFdCFdDFdEFdFfzBBEFeC2hdmY2kbmczBhQFFd2lRhAnfJGnAEXzJjTjUjSjJjOjHjJjGjZGfjzEiKi\n"
                        "TiPiOHfRBjBfffJHnAXEfjBf0DDByB";

int main() {
    string decompiled;
    int err = jsxer::decompile(compiled, decompiled);

    printf("--------------------------------------------------\n");
    printf("%s\n", decompiled.c_str());
    printf("--------------------------------------------------\n");

    return err;
}
```

## File: `tools/test-runner.js/.gitignore`
```
build
node_modules
dist/*
```

## File: `tools/test-runner.js/LICENSE`
```
BSD 3-Clause License

Copyright (c) 2023, psyirius
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## File: `tools/test-runner.js/package.json`
```json
{
  "name": "@jsxer/test-runner.js",
  "version": "0.1.0",
  "description": "ExtendScript decompiler test runner",
  "license" : "BSD-3-Clause",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
  },
  "bin": {
    "compile": "bin/cli.js"
  },
  "engines": {
    "node": ">=14"
  },
  "dependencies": {
    "jsxbin": "^2.2.0"
  },
  "devDependencies": {
    "@types/node": "^14.14.31"
  }
}
```

