---
id: piper
type: knowledge
owner: OA_Triage
---
# piper
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <img src="/promo/Icon-512.png" alt="PiPer logo" width="200" />
</p>

<h1 align="center">
  PiPer
</h1>

<p align="center">
  PiPer is the browser extension to watch video Picture in Picture.
</p>

<p align="center">
  <a href="#installation">Install</a> · 
  <a href="https://paypal.me/adampmarcus">Donate</a> · 
  <a href="https://github.com/amarcu5/PiPer/issues">Report an issue</a>
</p>

***

## Contents
- [Features](#features)
- [Installation](#installation)
  * [Safari](#safari)
  * [Chrome](#chrome)
- [Supported sites](#supported-sites)
- [Changelog](#changelog)
- [Development](#development)
  * [Building](#building)
    + [Prerequisites](#prerequisites)
    + [Build tools](#build-tools)
    + [Steps](#steps)
  * [Supporting a new site](#supporting-a-new-site)
- [Acknowledgements](#acknowledgements)

## Features
* Adds a dedicated Picture in Picture button to the video player of [supported sites](#supported-sites)
* Button integrates seamlessly with the player including hover effects and tooltips
* Supports closed captions in Picture and Picture mode (Safari only)
* Supports Safari and Chrome
* Free and open source

## Installation
### Safari
Install from the [Mac App Store](https://itunes.apple.com/app/id1421915518?mt=12&ls=1) by clicking "Get"  
<sub>(The [Safari Extension Gallery](https://safari-extensions.apple.com/details/?id=com.amarcus.safari.piper-BQ6Q24MF9X) is now [deprecated](https://developer.apple.com/documentation/safariextensions))</sub>
### Chrome
Install from the [Chrome Web Store](https://chrome.google.com/webstore/detail/piper/jbjleapidaddpbncgofepljddfeoghkc) by clicking "Add to Chrome"
  
<sub>...or live life on the edge with the latest [development build](https://github.com/amarcu5/PiPer/tree/develop-1.0.x/out) (IMPORTANT: these builds do not update automatically!)</sub>

## Supported sites
* [9Now](http://www.9now.com.au)
* [Apple TV+](http://tv.apple.com)
* [Amazon Video](http://www.amazon.com/PrimeVideo)
* [Česká televize](http://www.ceskatelevize.cz)
* [CollegeHumor](http://www.collegehumor.com)
* [Crunchyroll](http://www.crunchyroll.com)
* [CuriosityStream](http://www.curiositystream.com)
* [DAZN](https://www.dazn.com)
* [Disney+](http://www.disneyplus.com)
* [Eurosport player](http://www.eurosportplayer.com)
* [FuboTV](http://www.fubo.tv)
* [Giant Bomb](http://www.giantbomb.com)
* [Hulu](http://www.hulu.com)
* [LittleThings](http://www.littlethings.com)
* [Mashable](http://www.mashable.com)
* [Metacafe](http://www.metacafe.com)
* [Mixer](http://mixer.com)
* [MLB](http://www.mlb.tv)
* [Netflix](http://www.netflix.com)
* [OCS](http://www.ocs.fr)
* [Openload](http://www.openload.co)
* [PBS](http://www.pbs.org)
* [Periscope](http://www.periscope.tv)
* [Plex](http://www.plex.tv)
* [Seznam Zprávy](http://www.seznam.cz/zpravy)
* [Stream.cz](http://www.stream.cz)
* [Streamable](http://streamable.com)
* [TED](http://www.ted.com)
* [The Onion](http://www.theonion.com)
* [Twitch](http://www.twitch.tv)
* [Udemy](http://www.udemy.com)
* [Vevo](http://www.vevo.com)
* [Vice](http://www.vice.com)
* [Vid.me](http://www.vid.me)
* [Video Aktálně](http://video.aktualne.cz)
* [Vier](http://www.vier.be)
* [Vijf](http://www.vijf.be)
* [VK](http://www.vk.com)
* [VRV](http://www.vrv.co)
* [VRT NU](http://www.vrt.be/vrtnu/)
* [Yelo Play](http://www.yeloplay.be)
* [YouTube](http://www.youtube.com)
* [Zes](http://www.zes.be)

## Changelog
You can find information about releases [here](https://github.com/amarcu5/PiPer/releases)

## Development

### Building

#### Prerequisites
* Operating system
  * macOS: 10.12 Sierra or newer (required to build Safari extension)
  * Windows: Vista or newer using [Cygwin](https://cygwin.com/install.html)
  * Linux: 64-bit Ubuntu 14.04+, Debian 8+, openSUSE 13.3+, or Fedora Linux 24+
* Software
  * [Node.js](https://nodejs.org)
  * [Java](https://www.java.com/en/download/) (Windows only)


#### Build tools
The following build tools are used to build the extension:
* [csso](https://github.com/css/csso) for compressing CSS
* [svgo](https://github.com/svg/svgo) for compressing SVG images
* [xarjs](https://github.com/robertknight/xar-js) for packaging Safari legacy extension
* [google-closure-compiler](https://github.com/google/closure-compiler) for compiling JavaScript

These can be installed by executing the following command:
```Shell
npm install -g csso-cli svgo xar-js google-closure-compiler
```

#### Steps
1. Clone the repository
2. Run `make.sh` 
    1. By default this builds the unoptimized and unpackaged development version for all targets into the `./out/` directory
    2. Alternatively:
       * `./make.sh -p release` to build the optimized release versions for all targets
       * `./make.sh -p release -t chrome` to build the optimized release version for the Chrome browser
       * `./make.sh -h` to see the full list of options

### Supporting a new site
If we wanted to support `example.com` with the source:
```HTML
<div class="video-container">
  <video src="blob:http://example.com/342b3a13-c892-54ec-84f6-281579de03ab"></video>
  <div class="video-captions">
    Example caption
  </div>
  <div class="video-controls">
    <button class="control button-play">Play</button>
    <button class="control button-fullscreen">Fullscreen</button>
  </div>
</div>
```
We would start by adding a new file `example.js`  in the [resources directory](https://github.com/amarcu5/PiPer/tree/master/src/common/scripts/resources):
```JavaScript
export const domain = 'example';

export const resource = {
  buttonParent: function() {
    // Returns the element that will contain the button
    return document.querySelector('.video-controls');
  },
  videoElement: function() {
    // Returns the video element
    return document.querySelector('.video-container video');
  },
  
  // Optional
  captionElement: function() {
    // Returns the element that contains the video captions
    return document.querySelector('.video-captions');
  },
};
```
We might want to style the button so that it integrates with the page better:
```JavaScript
export const resource = {
  ...
  // Assign a CSS class
  buttonClassName: 'control',
  // Scale the button
  buttonScale: 0.5,
  // Apply custom CSS styles
  buttonStyle: /** CSS */ (`
    /* Declaring CSS this way ensures it gets optimized when the extension is built */
    cursor: pointer;
    opacity: 0.5;
  `),
  // Apply a custom CSS hover style
  buttonHoverStyle: /** CSS */ (`opacity: 1 !important`),
};
```
For more examples, please see the [source](https://github.com/amarcu5/PiPer/tree/master/src/)

## Acknowledgements
* [Pied PíPer](https://github.com/JoeKuhns/PiedPiPer.safariextension) for the original inspiration

```

### File: LICENSE.txt
```txt
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
from the Corresponding Source
... [TRUNCATED]
```

### File: make.sh
```sh
#!/bin/bash
#
# Make the PiPer Safari extension

EXTENSION_NAME="PiPer"

SOURCE_FILES=("main.js" "fix.js" "background.js" "install.js" "localization-bridge.js" "legacy.js")

# Certifcate paths
LEAF_CERT_PATH="../certs/cert.pem"
INTERMEDIATE_CERT_PATH="../certs/apple-intermediate.pem"
ROOT_CERT_PATH="../certs/apple-root.pem"
PRIVATE_KEY_PATH="../certs/privatekey.pem"


# Display help then exit
show_help() {
  cat << EOF
Usage: make.sh [options]

Options:
  -h -? --help                                  Show this screen
  -t --target (all|safari|safari-legacy|chrome) Make extension for target browser [default: all]
  -p --profile (release|debug|distribute)       Set settings according to profile [default: debug]
  -c --compress-css                             Compress CSS
  -j --compress-js                              Compress JavaScript
  -s --compress-svg                             Compress SVG
  -l --logging-level <number>                   Set logging level (0=all 10=trace 20=info 30=warning 40=error)
  -o --optimize-strings                         Remove unused localized strings by static program analysis
  -i --development-team <id>                    Set development team ID
  -a --archive-to-xcode                         Archive Safari extension to Xcode for Mac App Store distribution
  -e --package-extension                        Package extension for distribution (safari-legacy requires private key)
  -d --no-debug-js                              Remove JavaScript source maps to prevent debugging
  -v --no-version-increment                     Disable automatic version incrementing

EOF
  exit 0
}

arguments=("$@")

# First pass processing arguments
while :; do
  case $1 in
    -h|-\?|--help) show_help ;;
    -p|--profile) [[ "$2" ]] && profile=$2 ;;
    --profile=?*) profile=${1#*=} ;;
    -l|-t|-i|--logging-level|--target|--development-team) shift ;;
    -?*) ;;
    *) break
  esac
  shift
done

# Set default settings as per profile
case $profile in
  distribute)
    compress_svg=1
    compress_css=1
    compress_js=1
    debug_js=0
    package_ext=1
    logging_level=100
    optimize_strings=1
    ;;
  release)
    compress_svg=1
    compress_css=1
    compress_js=1
    debug_js=1
    package_ext=0
    logging_level=40
    optimize_strings=1
    ;;
  *)
    compress_svg=0
    compress_css=0
    compress_js=0
    debug_js=1
    package_ext=0
    logging_level=0
    optimize_strings=0
    profile="debug"
    ;;
esac
update_version=1
archive_xcode=0
development_team=""
targets="all"

set -- "${arguments[@]}"

# Second pass processing arguments
while :; do
  case $1 in
    -c|--compress-css) compress_css=1 ;;
    -j|--compress-js) compress_js=1 ;;
    -s|--compress-svg) compress_svg=1 ;;
    -e|--package-extension) package_ext=1 ;;
    -o|--optimize-localizations) optimize_strings=1 ;;
    -d|--no-debug-js) debug_js=0 ;;
    -v|--no-version-increment) update_version=0 ;;
    -t|--target) [[ "$2" ]] && targets=$2 && shift ;;
    --target=?*) targets=${1#*=} ;;
    -l|--logging-level) [[ "$2" ]] && logging_level=$2 && shift ;;
    --logging-level=?*) logging_level=${1#*=} ;;
    -i|--development-team) [[ "$2" ]] && development_team=$2 && shift ;;
    --development-team=?*) development_team=${1#*=} ;;
    -a|--archive-to-xcode) archive_xcode=1 ;;
    -p|--profile) shift ;;
    -?*) ;;
    *) break ;;
  esac
  shift
done

# Highlight selected build profile 
echo "Setting '${profile}' profile"

# Validate targets
case $targets in
  safari) targets=("safari") ;;
  safari-legacy) targets=("safari-legacy") ;;
  chrome) targets=("chrome") ;;
  *) targets=("safari" "safari-legacy" "chrome")
esac

# Validate logging level
logging_level="${logging_level//[!0-9]/}"
[[ -z "$logging_level" ]] && logging_level=0

# Helper checks for build tool dependency and falls back to 'npx' if possible
function get_node_command() {
  if type "$1" &>/dev/null; then
    echo "$1"
  elif type "npx" &>/dev/null; then
    npx_package=$([[ -z "$2" ]] && echo "$1" || echo "$2")
    echo "npx --quiet --package ${npx_package} $1"
    echo "Info: '$1' command not found therefore falling back to 'npx'; performance may suffer (avoid this by installing package with 'npm install ${npx_package} -g')" >&2
  else
    echo "Error: '$1' command not found and neither fallback 'npx'" >&2
    echo "Please install the latest version of Node.js (see https://nodejs.org/en/download/package-manager/)" >&2
    return 1
  fi
  return 0
}

# Target specific build checks
for i in "${!targets[@]}"; do
  
  if [[ "${targets[$i]}" = "safari" ]]; then
    
    # Only build 'safari' extension target when running under macOS
    if [[ "$(uname)" != "Darwin" ]]; then
      echo "Warning: Building 'safari' extension skipped as requires macOS" >&2
      unset "targets[$i]"
      continue
    fi
    
    # Ensure with have Xcode command line tools installed
    if [[ -z $(xcode-select --print-path) ]]; then
      echo "Installing Xcode Command Line Tools (expect a GUI popup)"
      xcode-select --install &>/dev/null
      echo "Press any key after installation has completed"
      read -rsn1
      if [[ -z $(xcode-select --print-path) ]]; then
        echo "Unable to find Xcode Command Line Tools"
        exit 1
      fi
    fi
  
  elif [[ "${targets[$i]}" = "safari-legacy" ]]; then
    
    # Get 'safari-legacy' specific build tool path and exit if not found
    [[ "${package_ext}" -eq 1 ]] && { XARJS_PATH=$(get_node_command "xarjs" "xar-js") || exit 1; }
  fi
  
done

# Check for google closure compiler requirements and exit if not found
CCJS_PATH=$(get_node_command "google-closure-compiler") || exit 1;
if ${CCJS_PATH} --platform native --version &>/dev/null; then
  CCJS_PATH="${CCJS_PATH} --platform native";
elif ${CCJS_PATH} --platform java --version &>/dev/null; then
  CCJS_PATH="${CCJS_PATH} --platform java";
else
  echo "Error: Java runtime required by 'google-closure-compiler' not found" >&2
  echo "Please install the latest version of Java (see https://www.java.com/en/download/)" >&2
  exit 1
fi

# Check for csso and exit if not found 
[[ "${compress_css}" -eq 1 ]] && { CSSO_PATH=$(get_node_command "csso" "csso-cli") || exit 1; }

# Check for svgo and exit if not found 
[[ "${compress_svg}" -eq 1 ]] && { SVGO_PATH=$(get_node_command "svgo") || exit 1; }

# Check for git and exit if not found
if [[ "${update_version}" -eq 1 ]] && { ! type "git" &>/dev/null; }; then
  echo "Error: 'git' command not found" >&2
  echo "Please install the latest version of git (see https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)" >&2
  exit 1
else
  GIT_PATH=$(sh /etc/profile; which git)
fi


#
# Build script
#

# Set working directory to project root
cd "${BASH_SOURCE[0]%/*}"

# Remove output folder
rm -rf out

# Make common output folder
mkdir -p "out/${EXTENSION_NAME}"

# Copy common items into common output folder
cp -r "src/common"/* "out/${EXTENSION_NAME}/"

# Compress all supported images with SVGO
if [[ "${compress_svg}" -eq 1 ]]; then
  ${SVGO_PATH} -q -f "out/${EXTENSION_NAME}/images"
fi

# Get current version from git if automatic versioning enabled
if [[ "${update_version}" -eq 1 ]]; then

  # Check we're inside a git work tree
  inside_git_repo="$(git rev-parse --is-inside-work-tree 2>/dev/null)"
  if [[ "${inside_git_repo}" ]]; then

    # Get number of commits and release version from most recent tag
    number_of_commits=$(($("${GIT_PATH}" rev-list HEAD --count) + 1))
    git_release_version=$("${GIT_PATH}" describe --tags --always --abbrev=0)
    git_release_version=${git_release_version%%-*};
    git_release_version=${git_release_version#*v};    

  # Otherwise issue warning and set blank version
  else
    echo "Warning: Unable to set version automatically as cannot find 'git' repository (ensure repository has been cloned to fix this)" >&2
    number_of_commits="0"
    git_release_version="0.0.0"
  fi
  
  # Helper performs multiline sed regular expression
  function multiline_sed_regex() {
    mv "$1" "$1.bak"
    echo -n "$(cat "$1.bak")" | tr "\n" "\f" | sed -E "$2" | tr "\f" "\n" > "$1"
    rm -rf "$1.bak"
  }
fi

# Make resources index file
import_list=""
resource_list=""
alias_list=""
resource_count=0
for path in "out/${EXTENSION_NAME}/scripts/resources"/*.js; do
  path="${path##*/}"
  [[ $path == "index.js" ]] && continue
  resource_count=$((resource_count+1))
  import_list="${import_list}"$'\n'"import * as r${resource_count} from \"./${path}\";"
  resource=$(<"out/${EXTENSION_NAME}/scripts/resources/${path}")
  regex_arr="(^|[ "$'\n'"])(const|let|var)[ "$'\n'"]+domain[ "$'\n'"]*=[ "$'\n'"]*\[([^]]+)\]"
  regex_val="(^|[ "$'\n'"])(const|let|var)[ "$'\n'"]+domain[ "$'\n'"]*="
  if [[ "$resource" =~ $regex_arr ]]; then
    IFS=", " read -a arr <<< "${BASH_REMATCH[3]}"
    resource_list="${resource_list}"$'\n'"resources[${arr[0]}] = r${resource_count}.resource;"
    for ((i=1;i<${#arr[@]};i++)); do
      alias_list="${alias_list}"$'\n'"resources[${arr[$i]}] = resources[${arr[0]}];"
    done
  elif [[ "$resource" =~ $regex_val ]]; then
    resource_list="${resource_list}"$'\n'"resources[r${resource_count}.domain] = r${resource_count}.resource;"
  else
    echo "Warning: No domain's listed for resource '${path}'" >&2
  fi
done

{
cat <<EOF
/** Auto-generated file **/
${import_list}

export const resources = {};
${resource_list}
${alias_list}
EOF
} >"out/${EXTENSION_NAME}/scripts/resources/index.js"



for target in "${targets[@]}"; do
  
  echo "Building '${target}' extension"
  
  # Set target specific flags
  case $target in
    safari)
      browser=1
      target_extension=""
      common_file_path="/Extension/Resources"
      ;;
    safari-legacy)
      browser=1
      target_extension=".safariextension"
      common_file_path=""
      ;;
    chrome) 
      browser=2
      target_extension=""
      common_file_path=""
      ;;
    *) exit 1
  esac
  
  # Make target folder
  mkdir -p "out/${EXTENSION_NAME}-${target}${target_extension}${common_file_path}"
  
  # Copy items from common output folder to target folder
  cp -r "out/${EXTENSION_NAME}"/* "out/${EXTENSION_NAME}-${target}${target_extension}${common_file_path}/"

  # Copy target specific items to target output folder
  cp -r "src/${target}"/* "out/${EXTENSION_NAME}-${target}${target_extension}/" 2>/dev/null
  
  # Compress all inline CSS with CSSO
  if [[ "${compress_css}" -eq 1 ]]; then
    function minify_css() { 
      echo "$@" | sed -e 's/\\"/"/g' -e 's/\\\$/$/g' | ${CSSO_PATH} --declaration-list
    }
    export -f minify_css
    export CSSO_PATH
    for path in "out/${EXTENSION_NAME}-${target}${target_extension}${common_file_path}/scripts"/{*,**/*}.js; do
      [[ ! -f "${path}" ]] && continue
      source=$(cat "${path}")
      echo "echo \"$(sed -e 's/\\/\\\\/g' -e 's/\$/\\$/g' -e 's/`/\\`/g' -e 's/\"/\\\"/g' -e 's/\\n/\\\\n/g' <<< "$source" \
        | tr '\n' '\f' \
        | sed -E 's/\/\*\*[[:space:]]+CSS[[:space:]]+\*\/[[:space:]]*\([[:space:]]*\\`([^`]*)\\`[[:space:]]*\)/\\`\$(minify_css '\''\1'\'')\\`/g' \
        | tr '\f' '\n')\"" \
        | sh > "${path}"
    done
  fi
  
  # Use closure compiler to compress javascript
  function remove_element() {
    for i in "${!files[@]}"; do
      if [[ ${files[$i]} = "$1" ]]; then
        unset "files[$i]"
      fi
    done
  }
  
  function add_element() {
    remove_element "$1"
    files+=("$1")
  }
  
  function get_absolute_path() {
    local dirname="${1%/*}"
    local basename="${1##*/}"
    
    echo "$(cd "$dirname" 2>/dev/null; pwd)/$basename"
  }
  
  # Convert absolute paths to platform native path on Windows 
  function fix_absolute_path() {
    case "$(uname -s)" in
      CYGWIN*|MINGW32*|MSYS*)
        echo "$(cygpath -wa ${1})"
        ;;
      *) echo "$1"
    esac
  }
  
  function process_file() {
    local dirname="${1%/*}"
    local imports=()
    
    if [[ ! -f "$1" ]]; then
      remove_element "$1"
      return
    fi
    
    local source=$(<"$1")
    regex="(^| |"$'\n'")(import|export)["$'\n'" ]+(([*a-zA-Z0-9_,{}"$'\n'" $]+)from["$'\n'" ]+)?['\"]([^'\"]+)['\"][ "$'\n'";]"
    while true; do
      if [[ "$source" =~ $regex ]]; then
        source="${source##*${BASH_REMATCH[0]}}"
        imports+=("${BASH_REMATCH[5]}")
      else
        break
      fi
    done
  
    for i in "${!imports[@]}"; do
      imports[$i]=$(cd "$dirname"; get_absolute_path "${imports[$i]}")
      add_element "${imports[$i]}"
    done
    
    for i in "${!imports[@]}"; do
      process_file "${imports[$i]}"
    done
  }


  scripts_path=$(get_absolute_path "out/${EXTENSION_NAME}-${target}${target_extension}${common_file_path}/scripts")
  defines_path="${scripts_path}/defines.js"
  extern_path=$(fix_absolute_path "${scripts_path}/externs.js")

  defines_processed_path=$(echo "${defines_path%.*}" | sed -E 's|[/@\]|$|g' | sed -E 's/[-. ]/_/g' | sed -e 's/\[/%5B/g' -e 's/]/%5D/g' -e 's/>/%3E/g' -e 's/</%3C/g')
  browser_flag="BROWSER$\$module${defines_processed_path}=${browser}"
  logging_flag="LOGGING_LEVEL$\$module${defines_processed_path}=${logging_level}"


  if [[ "$optimize_strings" -eq 1 ]]; then
    localization_path="${scripts_path}/localization.js"
    localization_source=$(<"$localization_path")
  fi

  for entry in "${SOURCE_FILES[@]}"; do
    files=()

    absolute_entry="${scripts_path}/${entry}"
    [[ ! -f "$absolute_entry" ]] && continue

    add_element "$absolute_entry"
    process_file "$absolute_entry"


    # Statically analyze javascript and remove unused localized strings
    if [[ "$optimize_strings" -eq 1 ]]; then
      locale_keys=()
      regex="(=[ \t"$'\n'"]*localizedString(WithReplacements)?[ \t"$'\n'";,])|(localizedString(WithReplacements)?\([ \t"$'\n'"]*(\"([^\"]+)\"|'([^']+)'|([^'\",)]+))[ \t"$'\n'"]*[,)])"
      dynamic_access=0
      for path in "${files[@]}"; do
        [[ "$path" == "$localization_path" ]] && continue
        source=$(<"$path")
        while true; do
          if [[ "$source" =~ $regex ]]; then
            source="${source##*${BASH_REMATCH[0]}}"
            locale_key="${BASH_REMATCH[6]:-${BASH_REMATCH[7]}}"
            if [[ ! -z "$locale_key" ]]; then
              locale_keys+=("$locale_key")
            else
              dynamic_access=1
              break
            fi
          else
            break
          fi
        done
      done
      source="$localization_source"
      if [[ "$dynamic_access" -eq 0 ]]; then
        processing="$localization_source"
        regex="localizations\[[ \t"$'\n'"]*('([^']+)'|\"([^\"]+)\")[ \t"$'\n'"]*\][^=]+=[ "$'\n'"]*{([^}'\"]*('([^'\\]|\\.)*'|\"([^\"\\]|\\.)*\")?)*}[ \t"$'\n'"]*;?"
        while true; do
          if [[ "$processing" =~ $regex ]]; then
            processing=${processing##*"${BASH_REMATCH[0]}"}
            locale_key="${BASH_REMATCH[2]:-${BASH_REMATCH[3]}}"
            found=0
            for key in "${locale_keys[@]}"; do
              if [[ "$key" == "$locale_key" ]]; then
                found=1
              
... [TRUNCATED]
```

### File: src\common\scripts\button.js
```js
import { info, error } from './logger.js'
import { getResource, getExtensionURL } from './common.js'
import { togglePictureInPicture, addPictureInPictureEventListener } from './video.js'
import { localizedString } from './localization.js'

const BUTTON_ID = 'PiPer_button';

let /** ?HTMLElement */ button = null;

/**
 * Injects Picture in Picture button into webpage
 *
 * @param {Element} parent - Element button will be inserted into
 */
export const addButton = function(parent) {

  // Create button if needed
  if (!button) {
    const buttonElementType = getResource().buttonElementType || 'button';
    button = /** @type {HTMLElement} */ (document.createElement(buttonElementType));

    // Set button properties
    button.id = BUTTON_ID;
    button.title = localizedString('button-title');
    const buttonStyle = getResource().buttonStyle;
    if (buttonStyle) button.style.cssText = buttonStyle;
    const buttonClassName = getResource().buttonClassName;
    if (buttonClassName) button.className = buttonClassName;

    // Add scaled image to button
    const image = /** @type {HTMLImageElement} */ (document.createElement('img'));
    image.style.width = image.style.height = '100%';
    const buttonScale = getResource().buttonScale;
    if (buttonScale) image.style.transform = `scale(${buttonScale})`;
    button.appendChild(image);

    // Set image paths
    let buttonImage = getResource().buttonImage;
    let buttonExitImage = getResource().buttonExitImage;
    if (!buttonImage) {
      buttonImage = 'default';
      buttonExitImage = 'default-exit';
    }
    const buttonImageURL = getExtensionURL(`images/${buttonImage}.svg`);
    image.src = buttonImageURL;
    if (buttonExitImage) {
      const buttonExitImageURL = getExtensionURL(`images/${buttonExitImage}.svg`);
      addPictureInPictureEventListener(function(video, isPlayingPictureInPicture) {
        image.src = (isPlayingPictureInPicture) ? buttonExitImageURL : buttonImageURL;
      });
    }

    // Add hover style to button (a nested stylesheet is used to avoid tracking another element)
    const buttonHoverStyle = getResource().buttonHoverStyle;
    if (buttonHoverStyle) {
      const style = document.createElement('style');
      const css = `#${BUTTON_ID}:hover{${buttonHoverStyle}}`;
      style.appendChild(document.createTextNode(css));
      button.appendChild(style);
    }

    // Toggle Picture in Picture mode when button is clicked
    button.addEventListener('click', function(event) {
      event.preventDefault();

      // Get the video element and bypass caching to accomodate for the underlying video changing (e.g. pre-roll adverts) 
      const video = /** @type {?HTMLVideoElement} */ (getResource().videoElement(true));
      if (!video) {
        error('Unable to find video');
        return;
      }

      togglePictureInPicture(video);
    });

    info('Picture in Picture button created');
  }

  // Inject button into correct place
  const referenceNode = getResource().buttonInsertBefore ? getResource().buttonInsertBefore(parent) : null;
  parent.insertBefore(button, referenceNode);
};

/**
 * Returns the Picture in Picture button element
 *
 * @return {?HTMLElement}
 */
export const getButton = function() {
  return button;
};

/**
 * Checks if Picture in Picture button is injected into page
 *
 * @return {boolean}
 */
export const checkButton = function() {
  return !!document.getElementById(BUTTON_ID);
};

```

### File: src\common\scripts\cache.js
```js
import { getResource } from './common.js'

/**
 * Initialises caching for button, video, and caption elements
 */
export const initialiseCaches = function() {

  // Return a unique id
  let uniqueIdCounter = 0;
  const /** function():string */ uniqueId = function() {
    return 'PiPer_' + uniqueIdCounter++;
  };

  /**
   * Wraps a function that returns an element to provide faster lookups by id
   *
   * @param {function(boolean=):?Element} elementFunction
   * @return {function(boolean=):?Element} 
   */
  const cacheElementWrapper = function(elementFunction) {
    let /** ?string */ cachedElementId = null;

    return /** function():?Element */ function(/** boolean= */ bypassCache) {

      // Return element by id if possible
      const cachedElement = cachedElementId ? 
          document.getElementById(cachedElementId) : null;
      if (cachedElement && !bypassCache) return cachedElement;

      // Call the underlying function to get the element
      const uncachedElement = elementFunction();
      if (uncachedElement) {

        // Save the native id otherwise assign a unique id
        if (!uncachedElement.id) uncachedElement.id = uniqueId();
        cachedElementId = uncachedElement.id;
      }
      return uncachedElement;
    };
  };

  // Wrap the button, video, and caption elements
  const currentResource = getResource();
  currentResource.buttonParent = cacheElementWrapper(currentResource.buttonParent);
  currentResource.videoElement = cacheElementWrapper(currentResource.videoElement);
  if (currentResource.captionElement) {
    currentResource.captionElement = cacheElementWrapper(currentResource.captionElement);
  }
};
```

### File: src\common\scripts\captions.js
```js
import { info } from './logger.js'
import { Browser, getBrowser, getResource } from './common.js'
import { videoPlayingPictureInPicture, addPictureInPictureEventListener, removePictureInPictureEventListener } from './video.js'

const TRACK_ID = 'PiPer_track';

let /** ?TextTrack */ track = null;
let /** boolean */ captionsEnabled = false;
let /** boolean */ showingCaptions = false;
let /** boolean */ showingEmptyCaption = false;
let /** string */ lastUnprocessedCaption = '';

/**
 * Disable closed caption support in Picture in Picture mode
 */
export const disableCaptions = function() {
  captionsEnabled = false;
  showingCaptions = false;
  processCaptions();
  removePictureInPictureEventListener(pictureInPictureEventListener);

  info('Closed caption support disabled');
};

/**
 * Enable closed caption support in Picture in Picture mode
 *
 * @param {boolean=} ignoreNowPlayingCheck - assumes video isn't already playing Picture in Picture
 */
export const enableCaptions = function(ignoreNowPlayingCheck) {  

  if (!getResource().captionElement) return;

  captionsEnabled = true;
  addPictureInPictureEventListener(pictureInPictureEventListener);
  
  info('Closed caption support enabled');

  if (ignoreNowPlayingCheck) return;

  const video = /** @type {?HTMLVideoElement} */ (getResource().videoElement(true));
  if (!video) return;
  showingCaptions = videoPlayingPictureInPicture(video);
  track = getCaptionTrack(video);
  processCaptions();
};

/**
 * Checks whether processing closed captions is required
 *
 * @return {boolean}
 */
export const shouldProcessCaptions = function() {
  return captionsEnabled && showingCaptions;
};

/**
 * Gets caption track for video (creates or returns existing track as needed)
 *
 * @param {HTMLVideoElement} video - video element that will display captions
 * @return {TextTrack}
 */
const getCaptionTrack = function(video) {

  // Find existing caption track
  const allTracks = video.textTracks;
  for (let trackId = allTracks.length; trackId--;) {
    if (allTracks[trackId].label === TRACK_ID) {
      info('Existing caption track found');
      return allTracks[trackId];
    }
  }

  // Otherwise create new caption track
  info('Caption track created');
  return video.addTextTrack('captions', TRACK_ID, 'en');
};

/**
 * Adds caption tracks to all video elements
 */
export const addVideoCaptionTracks = function() {
  const elements = document.getElementsByTagName('video');
  for (let index = 0, element; element = elements[index]; index++) {
    getCaptionTrack(/** @type {?HTMLVideoElement} */ (element));
  }
};

/**
 * Toggles captions when video enters or exits Picture in Picture mode
 *
 * @param {HTMLVideoElement} video - target video element
 * @param {boolean} isPlayingPictureInPicture - true if video playing Picture in Picture
 */
const pictureInPictureEventListener = function(video, isPlayingPictureInPicture) {
  
  // Toggle display of the captions and prepare video if needed
  showingCaptions = isPlayingPictureInPicture;
  if (showingCaptions) {
    track = getCaptionTrack(video);
    track.mode = 'showing';
  }
  lastUnprocessedCaption = '';
  processCaptions();

  info(`Video presentation mode changed (showingCaptions: ${showingCaptions})`);
};

/**
 * Removes visible Picture in Picture mode captions
 *
 * @param {HTMLVideoElement} video - video element showing captions
 * @param {boolean=} workaround - apply Safari bug workaround
 */
const removeCaptions = function(video, workaround = true) {

  while (track.activeCues.length) {
    track.removeCue(track.activeCues[0]);
  }

  // Workaround Safari bug; 'removeCue' doesn't immediately remove captions shown in Picture in Picture mode
  if (getBrowser() == Browser.SAFARI && workaround && video && !showingEmptyCaption) {
    track.addCue(new VTTCue(video.currentTime, video.currentTime + 60, ''));
    showingEmptyCaption = true;
  }
};

/**
 * Displays Picture in Picture mode caption
 *
 * @param {HTMLVideoElement} video - video element showing captions
 * @param {string} caption - a caption to display
 */
const addCaption = function(video, caption) {

  info(`Showing caption '${caption}'`);
  track.mode = 'showing';
  track.addCue(new VTTCue(video.currentTime, video.currentTime + 60, caption));

  if (getBrowser() == Browser.SAFARI) {
    showingEmptyCaption = false;
  }
};

/**
 * Updates visible captions
 */
export const processCaptions = function() {

  // Get handles to caption and video elements
  const captionElement = getResource().captionElement();
  const video = /** @type {?HTMLVideoElement} */ (getResource().videoElement());
  
  // Remove Picture in Picture mode captions and show native captions if no longer showing captions or encountered an error
  if (!showingCaptions || !captionElement) {
    removeCaptions(video);
    if (captionElement) captionElement.style.visibility = '';
    return;
  }

  // Otherwise ensure native captions remain hidden
  captionElement.style.visibility = 'hidden';

  // Check if a new native caption needs to be processed
  const unprocessedCaption = captionElement.textContent;
  if (unprocessedCaption == lastUnprocessedCaption) return;
  lastUnprocessedCaption = unprocessedCaption;
  
  // Remove old captions and apply Safari bug fix if caption has no content as otherwise causes flicker
  removeCaptions(video, !unprocessedCaption);

  // Performance optimisation - early exit if caption has no content
  if (!unprocessedCaption) return;

  // Show correctly spaced and formatted Picture in Picture mode caption
  let caption = '';
  const walk = document.createTreeWalker(captionElement, NodeFilter.SHOW_TEXT, null, false);
  while (walk.nextNode()) {
    const segment = walk.currentNode.nodeValue.trim();
    if (segment) {
      const style = window.getComputedStyle(walk.currentNode.parentElement);
      if (style.fontStyle == 'italic') {
        caption += `<i>${segment}</i>`;
      } else if (style.textDecoration == 'underline') {
        caption += `<u>${segment}</u>`;
      } else {
        caption += segment;
      }
      caption += ' ';
    } else if (caption.charAt(caption.length - 1) != '\n') {
      caption += '\n';
    }
  }
  caption = caption.trim();
  addCaption(video, caption);
};
```

### File: src\common\scripts\common.js
```js
import { BROWSER } from './defines.js'
import { warn } from './logger.js'

/** @enum {number} - Enum for browser */
export const Browser = {
  UNKNOWN: 0,
  SAFARI: 1,
  CHROME: 2,
};

/**
 * Returns current web browser
 *
 * @return {Browser} 
 */
export const getBrowser = function() {
  if (BROWSER != Browser.UNKNOWN) {
    return /** @type {Browser} */ (BROWSER);
  }
  if (/Safari/.test(navigator.userAgent) && /Apple/.test(navigator.vendor)) {
    return Browser.SAFARI;
  }
  if (/Chrome/.test(navigator.userAgent) && /Google/.test(navigator.vendor)) {
    return Browser.CHROME;
  }
  return Browser.UNKNOWN;
};

/**
 * @typedef {{
 *   buttonClassName: (string|undefined),
 *   buttonDidAppear: (function():undefined|undefined),
 *   buttonElementType: (string|undefined),
 *   buttonExitImage: (string|undefined),
 *   buttonHoverStyle: (string|undefined),
 *   buttonImage: (string|undefined),
 *   buttonInsertBefore: (function(Element):?Node|undefined),
 *   buttonParent: function(boolean=):?Element,
 *   buttonScale: (number|undefined),
 *   buttonStyle: (string|undefined),
 *   captionElement: (function(boolean=):?Element|undefined),
 *   videoElement: function(boolean=):?Element,
 * }}
 */
let PiperResource;

let /** ?PiperResource */ currentResource = null;

/**
 * Returns the current resource
 *
 * @return {?PiperResource}
 */
export const getResource = function() {
  return currentResource;
};

/**
 * Sets the current resource
 *
 * @param {?PiperResource} resource - a resource to set as current resource
 */
export const setResource = function(resource) {
  currentResource = resource;
};

/**
 * Converts a relative path within an extension to a fully-qualified URL
 *
 * @param {string} path - a path to a resource
 * @return {string} 
 */
export const getExtensionURL = function(path) {
  switch (getBrowser()) {
    case Browser.SAFARI:
      return safari.extension.baseURI + path;
    case Browser.CHROME:
      return chrome.runtime.getURL(path);
    case Browser.UNKNOWN:
    default:
      return path;
  }
};

/**
 * Applies fix to bypass background DOM timer throttling
 */
export const bypassBackgroundTimerThrottling = function() {

  // Issue warning for unnecessary use of background timer throttling
  if (!currentResource.captionElement) {
    warn('Unnecessary bypassing of background timer throttling on page without caption support');
  }

  const request = new XMLHttpRequest();
  request.open('GET', getExtensionURL('scripts/fix.js'));
  request.onload = function() {
    const script = document.createElement('script');
    script.setAttribute('type', 'module');
    script.appendChild(document.createTextNode(request.responseText));
    document.head.appendChild(script);
  };
  request.send();
};
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
