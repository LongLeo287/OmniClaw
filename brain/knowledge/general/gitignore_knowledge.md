---
id: gitignore-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.248729
---

# KNOWLEDGE EXTRACT: gitignore
> **Extracted on:** 2026-03-30 17:37:58
> **Source:** gitignore

---

## File: `Actionscript.gitignore`
```
# Build and Release Folders
bin-debug/
bin-release/
[Oo]bj/
[Bb]in/

# Other files and folders
.settings/

# Executables
*.swf
*.air
*.ipa
*.apk

# Project files, i.e. `.project`, `.actionScriptProperties` and `.flexProperties`
# should NOT be excluded as they contain compiler settings and other important
# information for Eclipse / Flash Builder.
```

## File: `Ada.gitignore`
```
# Object file
*.o

# Ada Library Information
*.ali
```

## File: `AdventureGameStudio.gitignore`
```
# Built things
_Debug/
Compiled/

# AudioCache can be rebuilt from sources
AudioCache/

# Lockfile
_OpenInEditor.lock

# User settings
Game.agf.user
*.crm.user

# Backups
Game.agf.bak
backup_acsprset.spr

# Memory dumps
*.dmp

# Temporary files
# temporarily created during sprite or room background compression
~aclzw.tmp
# temporary, main game data, before getting packed into exe
game28.dta
# temporary build of the game before being moved to Compiled/ folder
*.exe

# Log files
warnings.log
```

## File: `Agda.gitignore`
```
*.agdai
MAlonzo/**
```

## File: `AL.gitignore`
```
### AL ###
#Template for AL projects for Dynamics 365 Business Central
#launch.json folder
.vscode/
#Cache folder
.alcache/
#Symbols folder
.alpackages/
#Snapshots folder
.snapshots/
#Testing Output folder
.output/
#Extension App-file
*.app
#Rapid Application Development File
rad.json
#Translation Base-file
*.g.xlf
#License-file
*.flf
#Test results file
TestResults.xml
```

## File: `Android.gitignore`
```
# Gradle files
.gradle/
build/

# Local configuration file (sdk path, etc)
local.properties

# Log/OS Files
*.log

# Android Studio generated files and folders
captures/
.externalNativeBuild/
.cxx/
*.aab
*.apk
output-metadata.json

# IntelliJ
*.iml
.idea/
misc.xml
deploymentTargetDropDown.xml
render.experimental.xml

# Keystore files
*.jks
*.keystore

# Google Services (e.g. APIs or Firebase)
google-services.json

# Android Profiling
*.hprof
```

## File: `Angular.gitignore`
```
# Angular specific
/dist/
/out-tsc/
/tmp/
/coverage/
/e2e/test-output/
/.angular/
.angular/

# Node modules and dependency files
/node_modules/
/package-lock.json
/yarn.lock

# Environment files
/.env

# Angular CLI and build artefacts
/.angular-cli.json
/.ng/

# TypeScript cache
*.tsbuildinfo

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

## File: `AppceleratorTitanium.gitignore`
```
# Build folder and log file
build/
build.log
```

## File: `AppEngine.gitignore`
```
# Google App Engine generated folder
appengine-generated/
```

## File: `ArchLinuxPackages.gitignore`
```
*.tar
*.tar.*
*.jar
*.exe
*.msi
*.deb
*.zip
*.tgz
*.log
*.log.*
*.sig

pkg/
src/
```

## File: `Autotools.gitignore`
```
# http://www.gnu.org/software/automake

Makefile.in
/ar-lib
/mdate-sh
/py-compile
/test-driver
/ylwrap
.deps/
.dirstamp

# http://www.gnu.org/software/autoconf

autom4te.cache
/autoscan.log
/autoscan-*.log
/aclocal.m4
/compile
/config.cache
/config.guess
/config.h.in
/config.log
/config.status
/config.sub
/configure
/configure.scan
/depcomp
/install-sh
/missing
/stamp-h1

# https://www.gnu.org/software/libtool/

/libtool
/ltmain.sh
.libs/

# http://www.gnu.org/software/texinfo

/texinfo.tex

# http://www.gnu.org/software/m4/

m4/libtool.m4
m4/ltoptions.m4
m4/ltsugar.m4
m4/ltversion.m4
m4/lt~obsolete.m4

# Generated Makefile
# (meta build system like autotools,
# can automatically generate from config.status script
# (which is called by configure script))
Makefile
```

## File: `Ballerina.gitignore`
```
# generated files
target/
generated/

# dependencies
Dependencies.toml

# config files
Config.toml
# the config files used for testing, Uncomment the following line if you want to commit the test config files
#!**/tests/Config.toml
```

## File: `C++.gitignore`
```
# Prerequisites
*.d

# Compiled Object files
*.slo
*.lo
*.o
*.obj

# Precompiled Headers
*.gch
*.pch

# Linker files
*.ilk

# Debugger Files
*.pdb

# Compiled Dynamic libraries
*.so
*.dylib
*.dll
*.so.*


# Fortran module files
*.mod
*.smod

# Compiled Static libraries
*.lai
*.la
*.a
*.lib

# Executables
*.exe
*.out
*.app

# Build directories
build/
Build/
build-*/

# CMake generated files
CMakeFiles/
CMakeCache.txt
cmake_install.cmake
Makefile
install_manifest.txt 
compile_commands.json

# Temporary files
*.tmp 
*.log 
*.bak 
*.swp 

# vcpkg
vcpkg_installed/

# debug information files
*.dwo

# test output & cache
Testing/
.cache/
```

## File: `C.gitignore`
```
# Prerequisites
*.d

# Object files
*.o
*.ko
*.obj
*.elf

# Linker output
*.ilk
*.map
*.exp

# Precompiled Headers
*.gch
*.pch

# Libraries
*.lib
*.a
*.la
*.lo

# Shared objects (inc. Windows DLLs)
*.dll
*.so
*.so.*
*.dylib

# Executables
*.exe
*.out
*.app
*.i*86
*.x86_64
*.hex

# Debug files
*.dSYM/
*.su
*.idb
*.pdb

# Kernel Module Compile Results
*.mod*
*.cmd
.tmp_versions/
modules.order
Module.symvers
Mkfile.old
dkms.conf

# debug information files
*.dwo
```

## File: `CakePHP.gitignore`
```
# CakePHP 3

/vendor/*
/config/app.php

/tmp/cache/models/*
!/tmp/cache/models/empty
/tmp/cache/persistent/*
!/tmp/cache/persistent/empty
/tmp/cache/views/*
!/tmp/cache/views/empty
/tmp/sessions/*
!/tmp/sessions/empty
/tmp/tests/*
!/tmp/tests/empty

/logs/*
!/logs/empty

# CakePHP 2

/app/tmp/*
/app/Config/core.php
/app/Config/database.php
/vendors/*
```

## File: `CFWheels.gitignore`
```
# unpacked plugin folders
plugins/**/*

# files directory where uploads go
files

# DBMigrate plugin: generated SQL
db/sql

# AssetBundler plugin: generated bundles
javascripts/bundles
stylesheets/bundles
```

## File: `ChefCookbook.gitignore`
```
.vagrant
/cookbooks

# Bundler
bin/*
.bundle/*

.kitchen/
.kitchen.local.yml
```

## File: `Clojure.gitignore`
```
pom.xml
pom.xml.asc
*.jar
*.class
/lib/
/classes/
/target/
/checkouts/
.lein-deps-sum
.lein-repl-history
.lein-plugins/
.lein-failures
.nrepl-port
.cpcache/
```

## File: `CMake.gitignore`
```
CMakeLists.txt.user
CMakeCache.txt
CMakeFiles
CMakeScripts
Testing
Makefile
cmake_install.cmake
install_manifest.txt
compile_commands.json
CTestTestfile.cmake
_deps
CMakeUserPresets.json

# CLion
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#cmake-build-*
```

## File: `CodeIgniter.gitignore`
```
*/config/development
*/logs/log-*.php
!*/logs/index.html
*/cache/*
!system/cache/*
!*/cache/index.html
!*/cache/.htaccess

user_guide_src/build/*
user_guide_src/cilexer/build/*
user_guide_src/cilexer/dist/*
user_guide_src/cilexer/pycilexer.egg-info/*

#codeigniter 3
application/logs/*
!application/logs/index.html
!application/logs/.htaccess
/vendor/
```

## File: `CommonLisp.gitignore`
```
*.FASL
*.fasl
*.lisp-temp
*.dfsl
*.pfsl
*.d64fsl
*.p64fsl
*.lx64fsl
*.lx32fsl
*.dx64fsl
*.dx32fsl
*.fx64fsl
*.fx32fsl
*.sx64fsl
*.sx32fsl
*.wx64fsl
*.wx32fsl
```

## File: `Composer.gitignore`
```
composer.phar
/vendor/

# Commit your application's lock file https://getcomposer.org/doc/01-basic-usage.md#commit-your-composer-lock-file-to-version-control
# You may choose to ignore a library lock file http://getcomposer.org/doc/02-libraries.md#lock-file
# composer.lock
```

## File: `Concrete5.gitignore`
```
# ignore the error log and .htaccess and others
error_log
.htaccess

# concrete5 5.6 specific

config/site.php
files/cache/*
files/tmp/*

# concrete5 5.7 specific

# ignore everything but the index.html
/application/files/*
!/application/files/index.html

# ignore updates folder
/updates/*

# ignore sitemap.xml
/sitemap.xml
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing guidelines

We’d love you to help us improve this project. To help us keep this collection
high quality, we request that contributions adhere to the following guidelines.

- **Provide a link to the application or project’s homepage**. Unless it’s
  extremely popular, there’s a chance the maintainers don’t know about or use
  the language, framework, editor, app, or project your change applies to.

- **Provide links to documentation** supporting the change you’re making.
  Current, canonical documentation mentioning the files being ignored is best.
  If documentation isn’t available to support your change, do the best you can
  to explain what the files being ignored are for.

- **Explain why you’re making a change**. Even if it seems self-evident, please
  take a sentence or two to tell us why your change or addition should happen.
  It’s especially helpful to articulate why this change applies to *everyone*
  who works with the applicable technology, rather than just you or your team.

- **Please consider the scope of your change**. If your change specific to a
  certain language or framework, then make sure the change is made to the
  template for that language or framework, rather than to the template for an
  editor, tool, or operating system.

- **Please only modify *one template* per pull request**. This helps keep pull
  requests and feedback focused on a specific project or technology.

In general, the more you can do to help us understand the change you’re making,
the more likely we’ll be to accept your contribution quickly.

If a template is mostly a list of files installed by a particular version of
some software (e.g. a PHP framework) then it's brittle and probably no more
helpful than a simple `ls`. If it's not possible to curate a small set of
useful rules, then the template might not be a good fit for this collection.

Please also understand that we can’t list every tool that ever existed.
Our aim is to curate a collection of the *most common and helpful* templates,
not to make sure we cover every project possible. If we choose not to
include your language, tool, or project, it’s not because it’s not awesome.
```

## File: `Coq.gitignore`
```
.*.aux
.*.d
*.a
*.cma
*.cmi
*.cmo
*.cmx
*.cmxa
*.cmxs
*.glob
*.ml.d
*.ml4.d
*.mlg.d
*.mli.d
*.mllib.d
*.mlpack.d
*.native
*.o
*.v.d
*.vio
*.vo
*.vok
*.vos
.coq-native
.csdp.cache
.lia.cache
.nia.cache
.nlia.cache
.nra.cache
csdp.cache
lia.cache
nia.cache
nlia.cache
nra.cache
native_compute_profile_*.data

# generated timing files
*.timing.diff
*.v.after-timing
*.v.before-timing
*.v.timing
time-of-build-after.log
time-of-build-before.log
time-of-build-both.log
time-of-build-pretty.log
```

## File: `CraftCMS.gitignore`
```
# Craft 2 Storage (https://craftcms.com/support/craft-storage-gitignore)
# not necessary for Craft 3 (https://github.com/craftcms/craft/issues/26)
/craft/storage/*
!/craft/storage/rebrand
```

## File: `CUDA.gitignore`
```
*.i
*.ii
*.gpu
*.ptx
*.cubin
*.fatbin
```

## File: `D.gitignore`
```
# Compiled Object files
*.o
*.obj

# Compiled Dynamic libraries
*.so
*.dylib
*.dll

# Compiled Static libraries
*.a
*.lib

# Executables
*.exe

# DUB
.dub
docs.json
__dummy.html
docs/

# Code coverage
*.lst
```

## File: `Dart.gitignore`
```
# See https://www.dartlang.org/guides/libraries/private-files

# Files and directories created by pub
.dart_tool/
.packages
build/
# If you're building an application, you may want to check-in your pubspec.lock
pubspec.lock

# Directory created by dartdoc
# If you don't generate documentation locally you can remove this line.
doc/api/

# dotenv environment variables file
.env*

# Avoid committing generated Javascript files:
*.dart.js
# Produced by the --dump-info flag.
*.info.json
# When generated by dart2js. Don't specify *.js if your
# project includes source files written in JavaScript.
*.js
*.js_
*.js.deps
*.js.map

.flutter-plugins
.flutter-plugins-dependencies
```

## File: `Delphi.gitignore`
```
# Uncomment these types if you want even more clean repository. But be careful.
# It can make harm to an existing project source. Read explanations below.
#
# Resource files are binaries containing manifest, project icon and version info.
# They can not be viewed as text or compared by diff-tools. Consider replacing them with .rc files.
#*.res
#
# Type library file (binary). In old Delphi versions it should be stored.
# Since Delphi 2009 it is produced from .ridl file and can safely be ignored.
#*.tlb
#
# Diagram Portfolio file. Used by the diagram editor up to Delphi 7.
# Uncomment this if you are not using diagrams or use newer Delphi version.
#*.ddp
#
# Visual LiveBindings file. Added in Delphi XE2.
# Uncomment this if you are not using LiveBindings Designer.
#*.vlb
#
# Deployment Manager configuration file for your project. Added in Delphi XE2.
# Uncomment this if it is not mobile development and you do not use remote debug feature.
#*.deployproj
#
# C++ object files produced when C/C++ Output file generation is configured.
# Uncomment this if you are not using external objects (zlib library for example).
#*.obj
#

# Default Delphi compiler directories
# Content of this directories are generated with each Compile/Construct of a project.
# Most of the time, files here have not there place in a code repository.
#Win32/
#Win64/
#OSX64/
#OSXARM64/
#Android/
#Android64/
#iOSDevice64/
#Linux64/

# Delphi compiler-generated binaries (safe to delete)
*.exe
*.dll
*.bpl
*.bpi
*.dcp
*.so
*.apk
*.drc
*.map
*.dres
*.rsm
*.tds
*.dcu
*.lib
*.a
*.o
*.ocx

# Delphi autogenerated files (duplicated info)
*.cfg
*.hpp
*Resource.rc

# Delphi local files (user-specific info)
*.local
*.identcache
*.projdata
*.tvsconfig
*.dsk
*.dsv

# Delphi history and backups
__history/
__recovery/
*.~*

# Castalia statistics file (since XE7 Castalia is distributed with Delphi)
*.stat

# Boss dependency manager vendor folder https://github.com/HashLoad/boss
modules/
```

## File: `DM.gitignore`
```
*.dmb
*.rsc
*.int
*.lk
*.zip
```

## File: `Dotnet.gitignore`
```
## A streamlined .gitignore for modern .NET projects
## including temporary files, build results, and
## files generated by popular .NET tools. If you are
## developing with Visual Studio, the VS .gitignore
## https://github.com/github/gitignore/blob/main/VisualStudio.gitignore
## has more thorough IDE-specific entries.
##
## Get latest from https://github.com/github/gitignore/blob/main/Dotnet.gitignore

# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
[Ww][Ii][Nn]32/
[Aa][Rr][Mm]/
[Aa][Rr][Mm]64/
bld/
[Bb]in/
[Oo]bj/
[Ll]og/
[Ll]ogs/

# .NET Core
project.lock.json
project.fragment.lock.json
artifacts/

# ASP.NET Scaffolding
ScaffoldingReadMe.txt

# NuGet Packages
*.nupkg
# NuGet Symbol Packages
*.snupkg

# dotenv environment variables file
.env

# Others
~$*
*~
CodeCoverage/

# MSBuild Binary and Structured Log
*.binlog

# MSTest test Results
[Tt]est[Rr]esult*/
[Bb]uild[Ll]og.*

# NUnit
*.VisualState.xml
TestResult.xml
nunit-*.xml
```

## File: `Drupal.gitignore`
```
# gitignore template for Drupal 8 projects
#
# earlier versions of Drupal are tracked in `community/PHP/`
#
# follows official upstream conventions:
# https://www.drupal.org/docs/develop/using-composer

# Ignore configuration files that may contain sensitive information
/web/sites/*/*settings*.php
/web/sites/*/*services*.yml

# Ignore paths that may contain user-generated content
/web/sites/*/files
/web/sites/*/public
/web/sites/*/private
/web/sites/*/files-public
/web/sites/*/files-private

# Ignore paths that may contain temporary files
/web/sites/*/translations
/web/sites/*/tmp
/web/sites/*/cache

# Ignore drupal core (if not versioning drupal sources)
/web/vendor
/web/core
/web/modules/README.txt
/web/modules/contrib
/web/profiles/README.txt
/web/profiles/contrib
/web/sites/development.services.yml
/web/sites/example.settings.local.php
/web/sites/example.sites.php
/web/sites/README.txt
/web/themes/README.txt
/web/themes/contrib
/web/.csslintrc
/web/.editorconfig
/web/.eslintignore
/web/.eslintrc.json
/web/.gitattributes
/web/.htaccess
/web/.ht.router.php
/web/autoload.php
/web/composer.json
/web/composer.lock
/web/example.gitignore
/web/index.php
/web/INSTALL.txt
/web/LICENSE.txt
/web/README.txt
/web/robots.txt
/web/update.php
/web/web.config

# Ignore vendor dependencies and scripts
/vendor
/composer.phar
/composer
/robo.phar
/robo
/drush.phar
/drush
/drupal.phar
/drupal
```

## File: `Eagle.gitignore`
```
# Ignore list for Eagle, a PCB layout tool

# Backup files
*.s#?
*.b#?
*.l#?
*.b$?
*.s$?
*.l$?

# Eagle project file
# It contains a serial number and references to the file structure
# on your computer.
# comment the following line if you want to have your project file included.
eagle.epf

# Autorouter files
*.pro
*.job

# CAM files
*.$$$
*.cmp
*.ly2
*.l15
*.sol
*.plc
*.stc
*.sts
*.crc
*.crs

*.dri
*.drl
*.gpi
*.pls
*.ger
*.xln

*.drd
*.drd.*

*.s#*
*.b#*

*.info

*.eps

# file locks introduced since 7.x
*.lck
```

## File: `ecu.test.gitignore`
```
# gitignore template for ecu.test workspaces - by tracetronic https://tracetronic.com
# website: https://www.ecu-test.com
#   * all directories are related to the default directories, please adapt the .gitignore if you use customized directories

# Dynamic workspace settings
#   * We don't recommend to ignore the .workspace directory, because of important
#     * project specific settings
#     * local user settings
.workspace/ETdrive.xml
.workspace/favorites.xml
.workspace/filters.xml
.workspace/generators.xml
.workspace/history.xml
.workspace/parallelExecution.xml
.workspace/signalviewer.xml
.workspace/signalViewerHistory.json
.workspace/signalviewer2layout.xml
.workspace/testeditor.xml
.workspace/tooladapter.xml
.workspace/view.xml
# optional, if your process depends on this file remove exclusion
.workspace/attributeLists.xml
.workspace/interactiveexecution.xml
.workspace/protocol.xml
.workspace/pythonlibrary.xml
# deprecated, support for older versions
.workspace/traceexplorer.xml

# Custom file formats and test dependencies
#  * you can manage your artifacts also with test.guide (https://www.test-guide.info) and reference them via Playbooks
*.arxml
*.a2l
*.dbc
*.hex
*.s19
[tT]estdata
[tT]estdaten

# Test results and test execution related content
#   * Git is not intended to store and provide test results for all iterations
#   * We recommend to use test.guide (https://www.test-guide.info) for the test report management
TestReports

# Report generators and templates
#   * if you want to provide (f.e.) your own report generators exclude the directory here and ignore only the unnecessary subdirectories
Templates

# optional, default for external Python libraries
PyLibs

# Exclude large binary artifacts
#  * you can manage your artifacts also with test.guide (https://www.test-guide.info) and reference them via Playbooks
Offline-FIUs
Offline-Models
Offline-SGBDs
*.exe
*.msi
*.zip
*.7z

# Exclude default and custom temporary directories
Backup_*

# Python bytecode and cache files
__pycache__/
*.py[cod]
```

## File: `Elisp.gitignore`
```
# Compiled
*.elc

# Packaging
.cask/
.eask/
.eldev/
.keg/

# Built distribution
dist/

# Backup files
*~

# Undo-tree save-files
*.~undo-tree
```

## File: `Elixir.gitignore`
```
/_build
/cover
/deps
/doc
/.fetch
erl_crash.dump
*.ez
*.beam
/config/*.secret.exs
.elixir_ls/
```

## File: `Elm.gitignore`
```
# elm-package generated files
elm-stuff
# elm-repl generated files
repl-temp-*
```

## File: `EPiServer.gitignore`
```
######################
## EPiServer Files
######################
*License.config
```

## File: `Erlang.gitignore`
```
.eunit
*.o
*.beam
*.plt
erl_crash.dump
.concrete/DEV_MODE

# rebar 2.x
.rebar
rel/example_project
ebin/*.beam
deps

# rebar 3
.rebar3
_build/
_checkouts/
```

## File: `ExpressionEngine.gitignore`
```
.DS_Store

# Images
images/avatars/
images/captchas/
images/smileys/
images/member_photos/
images/signature_attachments/
images/pm_attachments/

# For security do not publish the following files
system/expressionengine/config/database.php
system/expressionengine/config/config.php

# Caches
sized/
thumbs/
_thumbs/
*/expressionengine/cache/*
```

## File: `ExtJs.gitignore`
```
.architect
bootstrap.css
bootstrap.js
bootstrap.json
bootstrap.jsonp
build/
classic.json
classic.jsonp
ext/
modern.json
modern.jsonp
resources/sass/.sass-cache/
resources/.arch-internal-preview.css
.arch-internal-preview.css
```

## File: `Fancy.gitignore`
```
*.rbc
*.fyc
```

## File: `Finale.gitignore`
```
*.bak
*.db
*.avi
*.pdf
*.ps
*.mid
*.midi
*.mp3
*.aif
*.wav
# Some versions of Finale have a bug and randomly save extra copies of
# the music source as "<Filename> copy.mus"
*copy.mus
```

## File: `Firebase.gitignore`
```
# Firebase build and deployment files
/firebase-debug.log
/firebase-debug.*.log
.firebaserc

# Firebase Hosting
/firebase.json
*.cache
hosting/.cache

# Firebase Functions
/functions/node_modules/
/functions/.env
/functions/package-lock.json

# Firebase Emulators
/firebase-*.zip
/.firebase/
/emulator-ui/

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Environment files (local configs)
/.env.*
```

## File: `FlaxEngine.gitignore`
```
# Ignore Flax project files
Binaries/
Cache/
Logs/
Output/
Screenshots/
*.HotReload.*

# Ignore Visual Studio project files (generated locally)
*.csproj
*.sln

# Ignore thumbnails created by Windows
Thumbs.db

# Ignore files built by Visual Studio
*.obj
*.exe
*.pdb
*.user
*.aps
*.pch
*.vspscc
*_i.c
*_p.c
*.ncb
*.suo
*.tlb
*.tlh
*.bak
*.cache
*.ilk
*.log
[Bb]in
[Dd]ebug*/
*.lib
*.sbr
obj/
[Rr]elease*/
_ReSharper*/
[Tt]est[Rr]esult*
.vs/

# Ignore Nuget packages folder
packages/
```

## File: `Flutter.gitignore`
```
# Miscellaneous
*.class
*.lock
*.log
*.pyc
*.swp
.buildlog/
.history



# Flutter repo-specific
/bin/cache/
/bin/internal/bootstrap.bat
/bin/internal/bootstrap.sh
/bin/mingit/
/dev/benchmarks/mega_gallery/
/dev/bots/.recipe_deps
/dev/bots/android_tools/
/dev/devicelab/ABresults*.json
/dev/docs/doc/
/dev/docs/flutter.docs.zip
/dev/docs/lib/
/dev/docs/pubspec.yaml
/dev/integration_tests/**/xcuserdata
/dev/integration_tests/**/Pods
/packages/flutter/coverage/
version
analysis_benchmark.json

# packages file containing multi-root paths
.packages.generated

# Flutter/Dart/Pub related
**/doc/api/
.dart_tool/
.flutter-plugins
.flutter-plugins-dependencies
**/generated_plugin_registrant.dart
.packages
.pub-preload-cache/
.pub/
build/
flutter_*.png
linked_*.ds
unlinked.ds
unlinked_spec.ds

# Android related
**/android/**/gradle-wrapper.jar
.gradle/
**/android/captures/
**/android/gradlew
**/android/gradlew.bat
**/android/local.properties
**/android/**/GeneratedPluginRegistrant.java
**/android/key.properties
*.jks

# iOS/XCode related
**/ios/**/*.mode1v3
**/ios/**/*.mode2v3
**/ios/**/*.moved-aside
**/ios/**/*.pbxuser
**/ios/**/*.perspectivev3
**/ios/**/*sync/
**/ios/**/.sconsign.dblite
**/ios/**/.tags*
**/ios/**/.vagrant/
**/ios/**/DerivedData/
**/ios/**/Icon?
**/ios/**/Pods/
**/ios/**/.symlinks/
**/ios/**/profile
**/ios/**/xcuserdata
**/ios/.generated/
**/ios/Flutter/.last_build_id
**/ios/Flutter/App.framework
**/ios/Flutter/Flutter.framework
**/ios/Flutter/Flutter.podspec
**/ios/Flutter/Generated.xcconfig
**/ios/Flutter/ephemeral
**/ios/Flutter/app.flx
**/ios/Flutter/app.zip
**/ios/Flutter/flutter_assets/
**/ios/Flutter/flutter_export_environment.sh
**/ios/ServiceDefinitions.json
**/ios/Runner/GeneratedPluginRegistrant.*

# macOS
**/Flutter/ephemeral/
**/Pods/
**/macos/Flutter/GeneratedPluginRegistrant.swift
**/macos/Flutter/ephemeral
**/xcuserdata/

# Windows
**/windows/flutter/generated_plugin_registrant.cc
**/windows/flutter/generated_plugin_registrant.h
**/windows/flutter/generated_plugins.cmake

# Linux
**/linux/flutter/generated_plugin_registrant.cc
**/linux/flutter/generated_plugin_registrant.h
**/linux/flutter/generated_plugins.cmake

# Coverage
coverage/

# Symbols
app.*.symbols

# Exceptions to above rules.
!**/ios/**/default.mode1v3
!**/ios/**/default.mode2v3
!**/ios/**/default.pbxuser
!**/ios/**/default.perspectivev3
!/packages/flutter_tools/test/data/dart_dependencies_test/**/.packages
!/dev/ci/**/Gemfile.lock
```

## File: `ForceDotCom.gitignore`
```
.project
.settings
salesforce.schema
Referenced Packages
```

## File: `Fortran.gitignore`
```
# Prerequisites
*.d

# Compiled Object files
*.slo
*.lo
*.o
*.obj

# Precompiled Headers
*.gch
*.pch

# Linker files
*.ilk

# Debugger Files
*.pdb

# Compiled Dynamic libraries
*.so
*.dylib
*.dll
*.so.*


# Fortran module files
*.mod
*.smod

# Compiled Static libraries
*.lai
*.la
*.a
*.lib

# Executables
*.exe
*.out
*.app

# Build directories
build/
Build/
build-*/

# CMake generated files
CMakeFiles/
CMakeCache.txt
cmake_install.cmake
Makefile
install_manifest.txt 
compile_commands.json

# Temporary files
*.tmp 
*.log 
*.bak 
*.swp 

# vcpkg
vcpkg_installed/

# debug information files
*.dwo

# test output & cache
Testing/
.cache/
```

## File: `FuelPHP.gitignore`
```
# the composer package lock file and install directory
# Commit your application's lock file http://getcomposer.org/doc/01-basic-usage.md#composer-lock-the-lock-file
# You may choose to ignore a library lock file http://getcomposer.org/doc/02-libraries.md#lock-file
# /composer.lock
/fuel/vendor

# the fuelphp document
/docs/

# you may install these packages with `oil package`.
# http://fuelphp.com/docs/packages/oil/package.html
# /fuel/packages/auth/
# /fuel/packages/email/
# /fuel/packages/oil/
# /fuel/packages/orm/
# /fuel/packages/parser/

# dynamically generated files
/fuel/app/logs/*/*/*
/fuel/app/cache/*/*
/fuel/app/config/crypt.php
```

## File: `Gcov.gitignore`
```
# gcc coverage testing tool files

*.gcno
*.gcda
*.gcov
```

## File: `GitBook.gitignore`
```
# Node rules:
## Grunt intermediate storage (http://gruntjs.com/creating-plugins#storing-task-files)
.grunt

## Dependency directory
## Commenting this out is preferred by some people, see
## https://docs.npmjs.com/misc/faq#should-i-check-my-node_modules-folder-into-git
node_modules

# Book build output
_book

# eBook build output
*.epub
*.mobi
*.pdf
```

## File: `GitHubPages.gitignore`
```
# This .gitignore is appropriate for repositories deployed to GitHub Pages and using
# a Gemfile as specified at https://github.com/github/pages-gem#conventional

# Basic Jekyll gitignores (synchronize to Jekyll.gitignore)
_site/
.sass-cache/
.jekyll-cache/
.jekyll-metadata

# Additional Ruby/bundler ignore for when you run: bundle install
/vendor

# Specific ignore for GitHub Pages
# GitHub Pages will always use its own deployed version of pages-gem
# This means GitHub Pages will NOT use your Gemfile.lock and therefore it is
# counterproductive to check this file into the repository.
# Details at https://github.com/github/pages-gem/issues/768
Gemfile.lock
```

## File: `Gleam.gitignore`
```
*.beam
*.ez
/build
erl_crash.dump
```

## File: `Go.gitignore`
```
# If you prefer the allow list template instead of the deny list, see community template:
# https://github.com/github/gitignore/blob/main/community/Golang/Go.AllowList.gitignore
#
# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary, built with `go test -c`
*.test

# Code coverage profiles and other test artifacts
*.out
coverage.*
*.coverprofile
profile.cov

# Dependency directories (remove the comment below to include it)
# vendor/

# Go workspace file
go.work
go.work.sum

# env file
.env

# Editor/IDE
# .idea/
# .vscode/
```

## File: `Godot.gitignore`
```
# Godot 4+ specific ignores
.godot/
.nomedia

# Godot-specific ignores
.import/
export.cfg
export_credentials.cfg
*.tmp

# Imported translations (automatically generated from CSV files)
*.translation

# Mono-specific ignores
.mono/
data_*/
mono_crash.*.json
```

## File: `Gradle.gitignore`
```
.gradle
**/build/
!**/src/**/build/

# Ignore Gradle GUI config
gradle-app.setting

# Avoid ignoring Gradle wrapper jar file (.jar files are usually ignored)
!gradle-wrapper.jar

# Avoid ignore Gradle wrappper properties
!gradle-wrapper.properties

# Cache of project
.gradletasknamecache

# Eclipse Gradle plugin generated files
# Eclipse Core
.project
# JDT-specific (Eclipse Java Development Tools)
.classpath
```

## File: `Grails.gitignore`
```
# .gitignore for Grails 1.2 and 1.3
# Although this should work for most versions of grails, it is
# suggested that you use the "grails integrate-with --git" command
# to generate your .gitignore file.

# web application files
/web-app/WEB-INF/classes

# default HSQL database files for production mode
/prodDb.*

# general HSQL database files
*Db.properties
*Db.script

# logs
/stacktrace.log
/test/reports
/logs

# project release file
/*.war

# plugin release files
/*.zip
/plugin.xml

# older plugin install locations
/plugins
/web-app/plugins

# "temporary" build files
/target
```

## File: `GWT.gitignore`
```
*.class

# Package Files #
*.jar
*.war

# gwt caches and compiled units #
war/gwt_bree/
gwt-unitCache/

# boilerplate generated classes #
.apt_generated/

# more caches and things from deploy #
war/WEB-INF/deploy/
war/WEB-INF/classes/

#compilation logs
.gwt/

#gwt junit compilation files
www-test/

#old GWT (1.5) created this dir
.gwt-tmp/
```

## File: `Haskell.gitignore`
```
dist
dist-*
cabal-dev
*.o
*.hi
*.hie
*.chi
*.chs.h
*.dyn_o
*.dyn_hi
.hpc
.hsenv
.cabal-sandbox/
cabal.sandbox.config
*.prof
*.aux
*.hp
*.eventlog
.stack-work/
cabal.project.local
cabal.project.local~
.HTF/
.ghc.environment.*
```

## File: `Haxe.gitignore`
```
.haxelib/
.haxelsp/recording/
dump/
```

## File: `HIP.gitignore`
```
# HIP.gitignore
# GitHub gitignore template for AMD HIP (ROCm) projects
#
# Reference:
#   Official AMD ROCm HIP .gitignore: https://github.com/ROCm/hip/blob/amd-staging/.gitignore

# 1. Build directories and files
/build/                          # common build directory
/CMakeFiles/                     # CMake internal files
/CMakeCache.txt                  # CMake cache file
/Makefile                        # autogenerated Makefile
/cmake_install.cmake             # install script
/install_manifest.txt            # install manifest list
*.ninja-dep                      # Ninja dependency files
*.ninja_log                      # Ninja log files
meson-logs/                      # Meson log directory

# 2. Compilation outputs and intermediates
*.o                              # object files
*.obj                            # Windows object files
*.so                             # shared libraries
*.a                              # static librarie
*.d                              # dependency files
*.gch                            # precompiled headers
*.ii                             # preprocessed output
*.ii.cpp                         # C++ preprocessed output
*.out                            # generic executable outputs
*.exe                            # Windows executables

# 3. HIP/ROCm specific binaries and intermediates
*.hsaco                          # ROCm compiled binary
*.s                              # assembly output
*.kernels.cpp                    # autogenerated kernel sources
*.hip.cpp.*                      # hipcc intermediate outputs

# 4. Official sample binaries and tutorial outputs
bin/hipInfo                      # sample binary
bin/hipBusBandwidth              # sample binary
bin/hipDispatchLatency           # sample binary
bin/hipify-clang                 # sample tool
samples/**/*.out                 # tutorial outputs
samples/**/*.code                # ISA/code dumps
samples/**/*.hsaco               # compiled binaries
samples/**/*.co                  # kernel code outputs

# 5. Tags, logs and test outputs
tags                             # ctags index
*.log                            # log files
/tests_output/                   # custom test output directory
/samples_output/                 # custom sample output directory
```

## File: `IAR.gitignore`
```
# Compiled binaries
*.o
*.bin
*.elf
*.hex
*.map
*.out
*.obj

# Trash
*.bak
thumbs.db
*.~*

# IAR Settings
**/settings/*.crun
**/settings/*.dbgdt
**/settings/*.cspy
**/settings/*.cspy.*
**/settings/*.xcl
**/settings/*.dni
**/settings/*.wsdt
**/settings/*.wspos

# IAR Debug Exe
**/Exe/*.sim

# IAR Debug Obj
**/Obj/*.pbd
**/Obj/*.pbd.*
**/Obj/*.pbi
**/Obj/*.pbi.*

# IAR project "Debug" directory
Debug/

# IAR project "Release" directory
Release/

# IAR project settings directory
settings/

# IAR backup files
Backup*

# IAR .dep files
*.dep
```

## File: `Idris.gitignore`
```
# Idris 2
*.ttc
*.ttm

# Idris 1
*.ibc
*.o
```

## File: `IGORPro.gitignore`
```
# Avoid including Experiment files: they can be created and edited locally to test the ipf files
*.pxp
*.pxt
*.uxp
*.uxt
```

## File: `Java.gitignore`
```
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*
replay_pid*
```

## File: `JBoss.gitignore`
```
jboss/server/all/deploy/project.ext
jboss/server/default/deploy/project.ext
jboss/server/minimal/deploy/project.ext
jboss/server/all/log/*.log
jboss/server/all/tmp/**/*
jboss/server/all/data/**/*
jboss/server/all/work/**/*
jboss/server/default/log/*.log
jboss/server/default/tmp/**/*
jboss/server/default/data/**/*
jboss/server/default/work/**/*
jboss/server/minimal/log/*.log
jboss/server/minimal/tmp/**/*
jboss/server/minimal/data/**/*
jboss/server/minimal/work/**/*

# deployed package files #

*.DEPLOYED
```

## File: `Jekyll.gitignore`
```
_site/
.sass-cache/
.jekyll-cache/
.jekyll-metadata
# Ignore folders generated by Bundler
.bundle/
vendor/
```

## File: `JENKINS_HOME.gitignore`
```
# Learn more about Jenkins and JENKINS_HOME directory for which this file is
# intended.
#
#  http://jenkins-ci.org/
#  https://wiki.jenkins-ci.org/display/JENKINS/Administering+Jenkins
#
# Note: secret.key is purposefully not tracked by git. This should be backed up
# separately because configs may contain secrets which were encrypted using the
# secret.key.  To back up secrets use 'tar -czf /tmp/secrets.tgz secret*' and
# save the file separate from your repository.  If you want secrets backed up
# with configuration, then see the bottom of this file for an example.

# Ignore all JENKINS_HOME except jobs directory, root xml config, and
# .gitignore file.
/*
!/jobs
!/.gitignore
!/*.xml

# Ignore all files in jobs subdirectories except for folders.
# Note: git doesn't track folders, only file content.
jobs/**
!jobs/**/

# Uncomment the following line to save next build numbers with config.

#!jobs/**/nextBuildNumber

# For performance reasons, we want to ignore builds in Jenkins jobs because it
# contains many tiny files on large installations.  This can impact git
# performance when running even basic commands like 'git status'.
builds
indexing

# Exclude only config.xml files in repository subdirectories.
!config.xml

# Don't track workspaces (when users build on the master).
jobs/**/*workspace

# Security warning: If secrets are included with your configuration, then an
# adversary will be able to decrypt all encrypted secrets within Jenkins
# config.  Including secrets is a bad practice, but the example is included in
# case someone still wants it for convenience.  Uncomment the following line to
# include secrets for decryption with repository configuration in Git.

#!/secret*

# As a result, only Jenkins settings and job config.xml files in JENKINS_HOME
# will be tracked by git.
```

## File: `Joomla.gitignore`
```
/.htaccess
/administrator/cache/*
/administrator/components/com_actionlogs/*
/administrator/components/com_admin/*
/administrator/components/com_ajax/*
/administrator/components/com_associations/*
/administrator/components/com_banners/*
/administrator/components/com_cache/*
/administrator/components/com_categories/*
/administrator/components/com_checkin/*
/administrator/components/com_config/*
/administrator/components/com_contact/*
/administrator/components/com_content/*
/administrator/components/com_contenthistory/*
/administrator/components/com_cpanel/*
/administrator/components/com_fields/*
/administrator/components/com_finder/*
/administrator/components/com_installer/*
/administrator/components/com_joomlaupdate/*
/administrator/components/com_languages/*
/administrator/components/com_login/*
/administrator/components/com_media/*
/administrator/components/com_menus/*
/administrator/components/com_messages/*
/administrator/components/com_modules/*
/administrator/components/com_newsfeeds/*
/administrator/components/com_plugins/*
/administrator/components/com_postinstall/*
/administrator/components/com_privacy/*
/administrator/components/com_redirect/*
/administrator/components/com_search/*
/administrator/components/com_tags/*
/administrator/components/com_templates/*
/administrator/components/com_users/*
/administrator/help/*
/administrator/includes/*
/administrator/index.php
/administrator/language/en-GB/en-GB.com_actionlogs.ini
/administrator/language/en-GB/en-GB.com_actionlogs.sys.ini
/administrator/language/en-GB/en-GB.com_admin.ini
/administrator/language/en-GB/en-GB.com_admin.sys.ini
/administrator/language/en-GB/en-GB.com_ajax.ini
/administrator/language/en-GB/en-GB.com_ajax.sys.ini
/administrator/language/en-GB/en-GB.com_associations.ini
/administrator/language/en-GB/en-GB.com_associations.sys.ini
/administrator/language/en-GB/en-GB.com_banners.ini
/administrator/language/en-GB/en-GB.com_banners.sys.ini
/administrator/language/en-GB/en-GB.com_cache.ini
/administrator/language/en-GB/en-GB.com_cache.sys.ini
/administrator/language/en-GB/en-GB.com_categories.ini
/administrator/language/en-GB/en-GB.com_categories.sys.ini
/administrator/language/en-GB/en-GB.com_checkin.ini
/administrator/language/en-GB/en-GB.com_checkin.sys.ini
/administrator/language/en-GB/en-GB.com_config.ini
/administrator/language/en-GB/en-GB.com_config.sys.ini
/administrator/language/en-GB/en-GB.com_contact.ini
/administrator/language/en-GB/en-GB.com_contact.sys.ini
/administrator/language/en-GB/en-GB.com_content.ini
/administrator/language/en-GB/en-GB.com_content.sys.ini
/administrator/language/en-GB/en-GB.com_contenthistory.ini
/administrator/language/en-GB/en-GB.com_contenthistory.sys.ini
/administrator/language/en-GB/en-GB.com_cpanel.ini
/administrator/language/en-GB/en-GB.com_cpanel.sys.ini
/administrator/language/en-GB/en-GB.com_fields.ini
/administrator/language/en-GB/en-GB.com_fields.sys.ini
/administrator/language/en-GB/en-GB.com_finder.ini
/administrator/language/en-GB/en-GB.com_finder.sys.ini
/administrator/language/en-GB/en-GB.com_installer.ini
/administrator/language/en-GB/en-GB.com_installer.sys.ini
/administrator/language/en-GB/en-GB.com_joomlaupdate.ini
/administrator/language/en-GB/en-GB.com_joomlaupdate.sys.ini
/administrator/language/en-GB/en-GB.com_languages.ini
/administrator/language/en-GB/en-GB.com_languages.sys.ini
/administrator/language/en-GB/en-GB.com_login.ini
/administrator/language/en-GB/en-GB.com_login.sys.ini
/administrator/language/en-GB/en-GB.com_mailto.sys.ini
/administrator/language/en-GB/en-GB.com_media.ini
/administrator/language/en-GB/en-GB.com_media.sys.ini
/administrator/language/en-GB/en-GB.com_menus.ini
/administrator/language/en-GB/en-GB.com_menus.sys.ini
/administrator/language/en-GB/en-GB.com_messages.ini
/administrator/language/en-GB/en-GB.com_messages.sys.ini
/administrator/language/en-GB/en-GB.com_modules.ini
/administrator/language/en-GB/en-GB.com_modules.sys.ini
/administrator/language/en-GB/en-GB.com_newsfeeds.ini
/administrator/language/en-GB/en-GB.com_newsfeeds.sys.ini
/administrator/language/en-GB/en-GB.com_plugins.ini
/administrator/language/en-GB/en-GB.com_plugins.sys.ini
/administrator/language/en-GB/en-GB.com_postinstall.ini
/administrator/language/en-GB/en-GB.com_postinstall.sys.ini
/administrator/language/en-GB/en-GB.com_privacy.ini
/administrator/language/en-GB/en-GB.com_privacy.sys.ini
/administrator/language/en-GB/en-GB.com_redirect.ini
/administrator/language/en-GB/en-GB.com_redirect.sys.ini
/administrator/language/en-GB/en-GB.com_search.ini
/administrator/language/en-GB/en-GB.com_search.sys.ini
/administrator/language/en-GB/en-GB.com_tags.ini
/administrator/language/en-GB/en-GB.com_tags.sys.ini
/administrator/language/en-GB/en-GB.com_templates.ini
/administrator/language/en-GB/en-GB.com_templates.sys.ini
/administrator/language/en-GB/en-GB.com_users.ini
/administrator/language/en-GB/en-GB.com_users.sys.ini
/administrator/language/en-GB/en-GB.com_weblinks.ini
/administrator/language/en-GB/en-GB.com_weblinks.sys.ini
/administrator/language/en-GB/en-GB.com_wrapper.ini
/administrator/language/en-GB/en-GB.com_wrapper.sys.ini
/administrator/language/en-GB/en-GB.ini
/administrator/language/en-GB/en-GB.lib_joomla.ini
/administrator/language/en-GB/en-GB.localise.php
/administrator/language/en-GB/en-GB.mod_custom.ini
/administrator/language/en-GB/en-GB.mod_custom.sys.ini
/administrator/language/en-GB/en-GB.mod_feed.ini
/administrator/language/en-GB/en-GB.mod_feed.sys.ini
/administrator/language/en-GB/en-GB.mod_latest.ini
/administrator/language/en-GB/en-GB.mod_latest.sys.ini
/administrator/language/en-GB/en-GB.mod_latestactions.ini
/administrator/language/en-GB/en-GB.mod_latestactions.sys.ini
/administrator/language/en-GB/en-GB.mod_logged.ini
/administrator/language/en-GB/en-GB.mod_logged.sys.ini
/administrator/language/en-GB/en-GB.mod_login.ini
/administrator/language/en-GB/en-GB.mod_login.sys.ini
/administrator/language/en-GB/en-GB.mod_menu.ini
/administrator/language/en-GB/en-GB.mod_menu.sys.ini
/administrator/language/en-GB/en-GB.mod_multilangstatus.ini
/administrator/language/en-GB/en-GB.mod_multilangstatus.sys.ini
/administrator/language/en-GB/en-GB.mod_online.ini
/administrator/language/en-GB/en-GB.mod_online.sys.ini
/administrator/language/en-GB/en-GB.mod_popular.ini
/administrator/language/en-GB/en-GB.mod_popular.sys.ini
/administrator/language/en-GB/en-GB.mod_privacy_dashboard.ini
/administrator/language/en-GB/en-GB.mod_privacy_dashboard.sys.ini
/administrator/language/en-GB/en-GB.mod_quickicon.ini
/administrator/language/en-GB/en-GB.mod_quickicon.sys.ini
/administrator/language/en-GB/en-GB.mod_sampledata.ini
/administrator/language/en-GB/en-GB.mod_sampledata.sys.ini
/administrator/language/en-GB/en-GB.mod_stats_admin.ini
/administrator/language/en-GB/en-GB.mod_stats_admin.sys.ini
/administrator/language/en-GB/en-GB.mod_status.ini
/administrator/language/en-GB/en-GB.mod_status.sys.ini
/administrator/language/en-GB/en-GB.mod_submenu.ini
/administrator/language/en-GB/en-GB.mod_submenu.sys.ini
/administrator/language/en-GB/en-GB.mod_title.ini
/administrator/language/en-GB/en-GB.mod_title.sys.ini
/administrator/language/en-GB/en-GB.mod_toolbar.ini
/administrator/language/en-GB/en-GB.mod_toolbar.sys.ini
/administrator/language/en-GB/en-GB.mod_unread.ini
/administrator/language/en-GB/en-GB.mod_unread.sys.ini
/administrator/language/en-GB/en-GB.mod_version.ini
/administrator/language/en-GB/en-GB.mod_version.sys.ini
/administrator/language/en-GB/en-GB.plg_actionlog_joomla.ini
/administrator/language/en-GB/en-GB.plg_actionlog_joomla.sys.ini
/administrator/language/en-GB/en-GB.plg_authentication_cookie.ini
/administrator/language/en-GB/en-GB.plg_authentication_cookie.sys.ini
/administrator/language/en-GB/en-GB.plg_authentication_example.ini
/administrator/language/en-GB/en-GB.plg_authentication_example.sys.ini
/administrator/language/en-GB/en-GB.plg_authentication_gmail.ini
/administrator/language/en-GB/en-GB.plg_authentication_gmail.sys.ini
/administrator/language/en-GB/en-GB.plg_authentication_joomla.ini
/administrator/language/en-GB/en-GB.plg_authentication_joomla.sys.ini
/administrator/language/en-GB/en-GB.plg_authentication_ldap.ini
/administrator/language/en-GB/en-GB.plg_authentication_ldap.sys.ini
/administrator/language/en-GB/en-GB.plg_captcha_recaptcha.ini
/administrator/language/en-GB/en-GB.plg_captcha_recaptcha.sys.ini
/administrator/language/en-GB/en-GB.plg_captcha_recaptcha_invisible.ini
/administrator/language/en-GB/en-GB.plg_captcha_recaptcha_invisible.sys.ini
/administrator/language/en-GB/en-GB.plg_content_confirmconsent.ini
/administrator/language/en-GB/en-GB.plg_content_confirmconsent.sys.ini
/administrator/language/en-GB/en-GB.plg_content_contact.ini
/administrator/language/en-GB/en-GB.plg_content_contact.sys.ini
/administrator/language/en-GB/en-GB.plg_content_emailcloak.ini
/administrator/language/en-GB/en-GB.plg_content_emailcloak.sys.ini
/administrator/language/en-GB/en-GB.plg_content_fields.ini
/administrator/language/en-GB/en-GB.plg_content_fields.sys.ini
/administrator/language/en-GB/en-GB.plg_content_finder.ini
/administrator/language/en-GB/en-GB.plg_content_finder.sys.ini
/administrator/language/en-GB/en-GB.plg_content_geshi.ini
/administrator/language/en-GB/en-GB.plg_content_geshi.sys.ini
/administrator/language/en-GB/en-GB.plg_content_joomla.ini
/administrator/language/en-GB/en-GB.plg_content_joomla.sys.ini
/administrator/language/en-GB/en-GB.plg_content_loadmodule.ini
/administrator/language/en-GB/en-GB.plg_content_loadmodule.sys.ini
/administrator/language/en-GB/en-GB.plg_content_pagebreak.ini
/administrator/language/en-GB/en-GB.plg_content_pagebreak.sys.ini
/administrator/language/en-GB/en-GB.plg_content_pagenavigation.ini
/administrator/language/en-GB/en-GB.plg_content_pagenavigation.sys.ini
/administrator/language/en-GB/en-GB.plg_content_vote.ini
/administrator/language/en-GB/en-GB.plg_content_vote.sys.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_article.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_article.sys.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_contact.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_contact.sys.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_fields.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_fields.sys.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_image.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_image.sys.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_menu.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_menu.sys.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_module.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_module.sys.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_pagebreak.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_pagebreak.sys.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_readmore.ini
/administrator/language/en-GB/en-GB.plg_editors-xtd_readmore.sys.ini
/administrator/language/en-GB/en-GB.plg_editors_codemirror.ini
/administrator/language/en-GB/en-GB.plg_editors_codemirror.sys.ini
/administrator/language/en-GB/en-GB.plg_editors_none.ini
/administrator/language/en-GB/en-GB.plg_editors_none.sys.ini
/administrator/language/en-GB/en-GB.plg_editors_tinymce.ini
/administrator/language/en-GB/en-GB.plg_editors_tinymce.sys.ini
/administrator/language/en-GB/en-GB.plg_extension_joomla.ini
/administrator/language/en-GB/en-GB.plg_extension_joomla.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_calendar.ini
/administrator/language/en-GB/en-GB.plg_fields_calendar.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_checkboxes.ini
/administrator/language/en-GB/en-GB.plg_fields_checkboxes.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_color.ini
/administrator/language/en-GB/en-GB.plg_fields_color.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_editor.ini
/administrator/language/en-GB/en-GB.plg_fields_editor.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_image.ini
/administrator/language/en-GB/en-GB.plg_fields_image.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_imagelist.ini
/administrator/language/en-GB/en-GB.plg_fields_imagelist.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_integer.ini
/administrator/language/en-GB/en-GB.plg_fields_integer.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_list.ini
/administrator/language/en-GB/en-GB.plg_fields_list.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_media.ini
/administrator/language/en-GB/en-GB.plg_fields_media.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_radio.ini
/administrator/language/en-GB/en-GB.plg_fields_radio.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_repeatable.ini
/administrator/language/en-GB/en-GB.plg_fields_repeatable.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_sql.ini
/administrator/language/en-GB/en-GB.plg_fields_sql.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_text.ini
/administrator/language/en-GB/en-GB.plg_fields_text.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_textarea.ini
/administrator/language/en-GB/en-GB.plg_fields_textarea.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_url.ini
/administrator/language/en-GB/en-GB.plg_fields_url.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_user.ini
/administrator/language/en-GB/en-GB.plg_fields_user.sys.ini
/administrator/language/en-GB/en-GB.plg_fields_usergrouplist.ini
/administrator/language/en-GB/en-GB.plg_fields_usergrouplist.sys.ini
/administrator/language/en-GB/en-GB.plg_finder_categories.ini
/administrator/language/en-GB/en-GB.plg_finder_categories.sys.ini
/administrator/language/en-GB/en-GB.plg_finder_contacts.ini
/administrator/language/en-GB/en-GB.plg_finder_contacts.sys.ini
/administrator/language/en-GB/en-GB.plg_finder_content.ini
/administrator/language/en-GB/en-GB.plg_finder_content.sys.ini
/administrator/language/en-GB/en-GB.plg_finder_newsfeeds.ini
/administrator/language/en-GB/en-GB.plg_finder_newsfeeds.sys.ini
/administrator/language/en-GB/en-GB.plg_finder_tags.ini
/administrator/language/en-GB/en-GB.plg_finder_tags.sys.ini
/administrator/language/en-GB/en-GB.plg_finder_weblinks.ini
/administrator/language/en-GB/en-GB.plg_finder_weblinks.sys.ini
/administrator/language/en-GB/en-GB.plg_installer_folderinstaller.ini
/administrator/language/en-GB/en-GB.plg_installer_folderinstaller.sys.ini
/administrator/language/en-GB/en-GB.plg_installer_packageinstaller.ini
/administrator/language/en-GB/en-GB.plg_installer_packageinstaller.sys.ini
/administrator/language/en-GB/en-GB.plg_installer_urlinstaller.ini
/administrator/language/en-GB/en-GB.plg_installer_urlinstaller.sys.ini
/administrator/language/en-GB/en-GB.plg_installer_webinstaller.ini
/administrator/language/en-GB/en-GB.plg_installer_webinstaller.sys.ini
/administrator/language/en-GB/en-GB.plg_privacy_actionlogs.ini
/administrator/language/en-GB/en-GB.plg_privacy_actionlogs.sys.ini
/administrator/language/en-GB/en-GB.plg_privacy_consents.ini
/administrator/language/en-GB/en-GB.plg_privacy_consents.sys.ini
/administrator/language/en-GB/en-GB.plg_privacy_contact.ini
/administrator/language/en-GB/en-GB.plg_privacy_contact.sys.ini
/administrator/language/en-GB/en-GB.plg_privacy_content.ini
/administrator/language/en-GB/en-GB.plg_privacy_content.sys.ini
/administrator/language/en-GB/en-GB.plg_privacy_message.ini
/administrator/language/en-GB/en-GB.plg_privacy_message.sys.ini
/administrator/language/en-GB/en-GB.plg_privacy_user.ini
/administrator/language/en-GB/en-GB.plg_privacy_user.sys.ini
/administrator/language/en-GB/en-GB.plg_quickicon_extensionupdate.ini
/administrator/language/en-GB/en-GB.plg_quickicon_extensionupdate.sys.ini
/administrator/language/en-GB/en-GB.plg_quickicon_joomlaupdate.ini
/administrator/language/en-GB/en-GB.plg_quickicon_joomlaupdate.sys.ini
/administrator/language/en-GB/en-GB.plg_quickicon_phpversioncheck.ini
/administrator/language/en-GB/en-GB.plg_quickicon_phpversioncheck.sys.ini
/administrator/language/en-GB/en-GB.plg_quickicon_privacycheck.ini
/administrator/language/en-GB/en-GB.plg_quickicon_privacycheck.sys.ini
/administrator/language/en-GB/en-GB.plg_sampledata_blog.ini
/administrator/language/en-GB/en-GB.plg_sampledata_blog.sys.ini
/administrator/language/en-GB/en-GB.plg_search_categories.ini
/administrator/language/en-GB/en-GB.plg_search_categories.sys.ini
/administrator/language/en-GB/en-GB.plg_search_contacts.ini
/administrator/language/en-GB/en-GB.plg_search_contacts.sys.ini
/administrator/language/en-GB/en-GB.plg_search_content.ini
/administrator/language/en-GB/en-GB.plg_search_content.sys.ini
/administrator/language/en-GB/en-GB.plg_search_newsfeeds.ini
/administrator/language/en-GB/en-GB.plg_search_newsfeeds.sys.ini
/administrator/language/en-GB/en-GB.plg_search_tags.ini
/administrator/language/en-GB/en-GB.plg_search_tags.sys.ini
/administrator/language/en-GB/en-GB.plg_search_weblinks.ini
/administrator/language/en-GB/en-GB.plg_search_weblinks.sys.ini
/administrator/language/en-GB/en-GB.plg_system_actionlogs.ini
/administrator/language/en-GB/en-GB.plg_system_actionlogs.sys.ini
/administrator/language/en-GB/en-GB.plg_system_cache.ini
/administrator/language/en-GB/en-GB.plg_system_cache.sys.ini
/administrator/language/en-GB/en-GB.plg_system_debug.ini
/administrator/language/en-GB/en-GB.plg_system_debug.sys.ini
/administrator/language/en-GB/en-GB.plg_system_fields.ini
/administrator/language/en-GB/en-GB.plg_system_fields.sys.ini
/administrator/language/en-GB/en-GB.plg_system_highlight.ini
/administrator/language/en-GB/en-GB.plg_system_highlight.sys.ini
/administrator/language/en-GB/en-GB.plg_system_languagecode.ini
/administrator/language/en-GB/en-GB.plg_system_languagecode.sys.ini
/administrator/language/en-GB/en-GB.plg_system_languagefilter.ini
/administrator/language/en-GB/en-GB.plg_system_languagefilter.sys.ini
/administrator/language/en-GB/en-GB.plg_system_log.ini
/administrator/language/en-GB/en-GB.plg_system_log.sys.ini
/administrator/language/en-GB/en-GB.plg_system_logout.ini
/administrator/language/en-GB/en-GB.plg_system_logout.sys.ini
/administrator/language/en-GB/en-GB.plg_system_logrotation.ini
/administrator/language/en-GB/en-GB.plg_system_logrotation.sys.ini
/administrator/language/en-GB/en-GB.plg_system_p3p.ini
/administrator/language/en-GB/en-GB.plg_system_p3p.sys.ini
/administrator/language/en-GB/en-GB.plg_system_privacyconsent.ini
/administrator/language/en-GB/en-GB.plg_system_privacyconsent.sys.ini
/administrator/language/en-GB/en-GB.plg_system_redirect.ini
/administrator/language/en-GB/en-GB.plg_system_redirect.sys.ini
/administrator/language/en-GB/en-GB.plg_system_remember.ini
/administrator/language/en-GB/en-GB.plg_system_remember.sys.ini
/administrator/language/en-GB/en-GB.plg_system_sef.ini
/administrator/language/en-GB/en-GB.plg_system_sef.sys.ini
/administrator/language/en-GB/en-GB.plg_system_sessiongc.ini
/administrator/language/en-GB/en-GB.plg_system_sessiongc.sys.ini
/administrator/language/en-GB/en-GB.plg_system_stats.ini
/administrator/language/en-GB/en-GB.plg_system_stats.sys.ini
/administrator/language/en-GB/en-GB.plg_system_updatenotification.ini
/administrator/language/en-GB/en-GB.plg_system_updatenotification.sys.ini
/administrator/language/en-GB/en-GB.plg_twofactorauth_totp.ini
/administrator/language/en-GB/en-GB.plg_twofactorauth_totp.sys.ini
/administrator/language/en-GB/en-GB.plg_twofactorauth_yubikey.ini
/administrator/language/en-GB/en-GB.plg_twofactorauth_yubikey.sys.ini
/administrator/language/en-GB/en-GB.plg_user_contactcreator.ini
/administrator/language/en-GB/en-GB.plg_user_contactcreator.sys.ini
/administrator/language/en-GB/en-GB.plg_user_joomla.ini
/administrator/language/en-GB/en-GB.plg_user_joomla.sys.ini
/administrator/language/en-GB/en-GB.plg_user_profile.ini
/administrator/language/en-GB/en-GB.plg_user_profile.sys.ini
/administrator/language/en-GB/en-GB.plg_user_terms.ini
/administrator/language/en-GB/en-GB.plg_user_terms.sys.ini
/administrator/language/en-GB/en-GB.tpl_hathor.ini
/administrator/language/en-GB/en-GB.tpl_hathor.sys.ini
/administrator/language/en-GB/en-GB.tpl_isis.ini
/administrator/language/en-GB/en-GB.tpl_isis.sys.ini
/administrator/language/en-GB/en-GB.xml
/administrator/language/en-GB/install.xml
/administrator/language/overrides/*
/administrator/language/index.html
/administrator/logs/*
/administrator/manifests/files/joomla.xml
/administrator/manifests/libraries/fof.xml
/administrator/manifests/libraries/idna_convert.xml
/administrator/manifests/libraries/joomla.xml
/administrator/manifests/libraries/phpass.xml
/administrator/manifests/libraries/phputf8.xml
/administrator/manifests/packages/pkg_en-GB.xml
/administrator/manifests/packages/index.html
/administrator/modules/mod_custom/*
/administrator/modules/mod_feed/*
/administrator/modules/mod_latest/*
/administrator/modules/mod_latestactions/*
/administrator/modules/mod_logged/*
/administrator/modules/mod_login/*
/administrator/modules/mod_menu/*
/administrator/modules/mod_multilangstatus/*
/administrator/modules/mod_online/*
/administrator/modules/mod_popular/*
/administrator/modules/mod_privacy_dashboard/*
/administrator/modules/mod_quickicon/*
/administrator/modules/mod_sampledata/*
/administrator/modules/mod_stats_admin/*
/administrator/modules/mod_status/*
/administrator/modules/mod_submenu/*
/administrator/modules/mod_title/*
/administrator/modules/mod_toolbar/*
/administrator/modules/mod_unread/*
/administrator/modules/mod_version/*
/administrator/templates/hathor/*
/administrator/templates/isis/*
/administrator/templates/system/*
/bin/*
/cache/*
/cli/*
/components/com_ajax/*
/components/com_banners/*
/components/com_config/*
/components/com_contact/*
/components/com_content/*
/components/com_contenthistory/*
/components/com_fields/*
/components/com_finder/*
/components/com_mailto/*
/components/com_media/*
/components/com_menus/*
/components/com_modules/*
/components/com_newsfeeds/*
/components/com_privacy/*
/components/com_search/*
/components/com_tags/*
/components/com_users/*
/components/com_wrapper/*
/components/index.html
/images/banners/*
/images/headers/*
/images/sampledata/*
/images/index.html
/images/joomla*
/images/powered_by.png
/includes/*
/installation/*
/language/en-GB/en-GB.com_ajax.ini
/language/en-GB/en-GB.com_config.ini
/language/en-GB/en-GB.com_contact.ini
/language/en-GB/en-GB.com_content.ini
/language/en-GB/en-GB.com_finder.ini
/language/en-GB/en-GB.com_mailto.ini
/language/en-GB/en-GB.com_media.ini
/language/en-GB/en-GB.com_messages.ini
/language/en-GB/en-GB.com_newsfeeds.ini
/language/en-GB/en-GB.com_privacy.ini
/language/en-GB/en-GB.com_search.ini
/language/en-GB/en-GB.com_tags.ini
/language/en-GB/en-GB.com_users.ini
/language/en-GB/en-GB.com_weblinks.ini
/language/en-GB/en-GB.com_wrapper.ini
/language/en-GB/en-GB.files_joomla.sys.ini
/language/en-GB/en-GB.finder_cli.ini
/language/en-GB/en-GB.ini
/language/en-GB/en-GB.lib_fof.ini
/language/en-GB/en-GB.lib_fof.sys.ini
/language/en-GB/en-GB.lib_idna_convert.sys.ini
/language/en-GB/en-GB.lib_joomla.ini
/language/en-GB/en-GB.lib_joomla.sys.ini
/language/en-GB/en-GB.lib_phpass.sys.ini
/language/en-GB/en-GB.lib_phpmailer.sys.ini
/language/en-GB/en-GB.lib_phputf8.sys.ini
/language/en-GB/en-GB.lib_simplepie.sys.ini
/language/en-GB/en-GB.localise.php
/language/en-GB/en-GB.mod_articles_archive.ini
/language/en-GB/en-GB.mod_articles_archive.sys.ini
/language/en-GB/en-GB.mod_articles_categories.ini
/language/en-GB/en-GB.mod_articles_categories.sys.ini
/language/en-GB/en-GB.mod_articles_category.ini
/language/en-GB/en-GB.mod_articles_category.sys.ini
/language/en-GB/en-GB.mod_articles_latest.ini
/language/en-GB/en-GB.mod_articles_latest.sys.ini
/language/en-GB/en-GB.mod_articles_news.ini
/language/en-GB/en-GB.mod_articles_news.sys.ini
/language/en-GB/en-GB.mod_articles_popular.ini
/language/en-GB/en-GB.mod_articles_popular.sys.ini
/language/en-GB/en-GB.mod_banners.ini
/language/en-GB/en-GB.mod_banners.sys.ini
/language/en-GB/en-GB.mod_breadcrumbs.ini
/language/en-GB/en-GB.mod_breadcrumbs.sys.ini
/language/en-GB/en-GB.mod_custom.ini
/language/en-GB/en-GB.mod_custom.sys.ini
/language/en-GB/en-GB.mod_feed.ini
/language/en-GB/en-GB.mod_feed.sys.ini
/language/en-GB/en-GB.mod_finder.ini
/language/en-GB/en-GB.mod_finder.sys.ini
/language/en-GB/en-GB.mod_footer.ini
/language/en-GB/en-GB.mod_footer.sys.ini
/language/en-GB/en-GB.mod_languages.ini
/language/en-GB/en-GB.mod_languages.sys.ini
/language/en-GB/en-GB.mod_login.ini
/language/en-GB/en-GB.mod_login.sys.ini
/language/en-GB/en-GB.mod_menu.ini
/language/en-GB/en-GB.mod_menu.sys.ini
/language/en-GB/en-GB.mod_random_image.ini
/language/en-GB/en-GB.mod_random_image.sys.ini
/language/en-GB/en-GB.mod_related_items.ini
/language/en-GB/en-GB.mod_related_items.sys.ini
/language/en-GB/en-GB.mod_search.ini
/language/en-GB/en-GB.mod_search.sys.ini
/language/en-GB/en-GB.mod_stats.ini
/language/en-GB/en-GB.mod_stats.sys.ini
/language/en-GB/en-GB.mod_syndicate.ini
/language/en-GB/en-GB.mod_syndicate.sys.ini
/language/en-GB/en-GB.mod_tags_popular.ini
/language/en-GB/en-GB.mod_tags_popular.sys.ini
/language/en-GB/en-GB.mod_tags_similar.ini
/language/en-GB/en-GB.mod_tags_similar.sys.ini
/language/en-GB/en-GB.mod_users_latest.ini
/language/en-GB/en-GB.mod_users_latest.sys.ini
/language/en-GB/en-GB.mod_weblinks.ini
/language/en-GB/en-GB.mod_weblinks.sys.ini
/language/en-GB/en-GB.mod_whosonline.ini
/language/en-GB/en-GB.mod_whosonline.sys.ini
/language/en-GB/en-GB.mod_wrapper.ini
/language/en-GB/en-GB.mod_wrapper.sys.ini
/language/en-GB/en-GB.tpl_atomic.ini
/language/en-GB/en-GB.tpl_atomic.sys.ini
/language/en-GB/en-GB.tpl_beez3.ini
/language/en-GB/en-GB.tpl_beez3.sys.ini
/language/en-GB/en-GB.tpl_beez5.ini
/language/en-GB/en-GB.tpl_beez5.sys.ini
/language/en-GB/en-GB.tpl_beez_20.ini
/language/en-GB/en-GB.tpl_beez_20.sys.ini
/language/en-GB/en-GB.tpl_protostar.ini
/language/en-GB/en-GB.tpl_protostar.sys.ini
/language/en-GB/en-GB.xml
/language/en-GB/install.xml
/language/overrides/*
/language/index.html
/layouts/joomla/*
/layouts/libraries/*
/layouts/plugins/*
/layouts/index.html
/libraries/cms/*
/libraries/fof/*
/libraries/idna_convert/*
/libraries/joomla/*
/libraries/legacy/*
/libraries/php-encryption/*
/libraries/phpass/*
/libraries/phpmailer/*
/libraries/phputf8/*
/libraries/simplepie/*
/libraries/src/*
/libraries/vendor/*
/libraries/classmap.php
/libraries/cms.php
/libraries/import.legacy.php
/libraries/import.php
/libraries/index.html
/libraries/loader.php
/media/cms/*
/media/com_associations/*
/media/com_contact/*
/media/com_content/*
/media/com_contenthistory/*
/media/com_fields/*
/media/com_finder/*
/media/com_joomlaupdate/*
/media/com_menus/*
/media/com_modules/*
/media/com_wrapper/*
/media/contacts/*
/media/editors/*
/media/jui/*
/media/mailto/*
/media/media/*
/media/mod_languages/*
/media/mod_sampledata/*
/media/overrider/*
/media/plg_captcha_recaptcha/*
/media/plg_captcha_recaptcha_invisible/*
/media/plg_quickicon_extensionupdate/*
/media/plg_quickicon_joomlaupdate/*
/media/plg_quickicon_privacycheck/*
/media/plg_system_highlight/*
/media/plg_system_stats/*
/media/plg_twofactorauth_totp/*
/media/system/*
/media/index.html
/modules/mod_articles_archive/*
/modules/mod_articles_categories/*
/modules/mod_articles_category/*
/modules/mod_articles_latest/*
/modules/mod_articles_news/*
/modules/mod_articles_popular/*
/modules/mod_banners/*
/modules/mod_breadcrumbs/*
/modules/mod_custom/*
/modules/mod_feed/*
/modules/mod_finder/*
/modules/mod_footer/*
/modules/mod_languages/*
/modules/mod_login/*
/modules/mod_menu/*
/modules/mod_random_image/*
/modules/mod_related_items/*
/modules/mod_search/*
/modules/mod_stats/*
/modules/mod_syndicate/*
/modules/mod_tags_popular/*
/modules/mod_tags_similar/*
/modules/mod_users_latest/*
/modules/mod_whosonline/*
/modules/mod_wrapper/*
/modules/index.html
/plugins/actionlog/joomla/*
/plugins/authentication/cookie/*
/plugins/authentication/example/*
/plugins/authentication/gmail/*
/plugins/authentication/joomla/*
/plugins/authentication/ldap/*
/plugins/captcha/recaptcha/*
/plugins/captcha/recaptcha_invisible/*
/plugins/content/confirmconsent/*
/plugins/content/contact/*
/plugins/content/emailcloak/*
/plugins/content/example/*
/plugins/content/fields/*
/plugins/content/finder/*
/plugins/content/geshi/*
/plugins/content/joomla/*
/plugins/content/loadmodule/*
/plugins/content/pagebreak/*
/plugins/content/pagenavigation/*
/plugins/content/vote/*
/plugins/editors/codemirror/*
/plugins/editors/none/*
/plugins/editors/tinymce/*
/plugins/editors-xtd/article/*
/plugins/editors-xtd/contact/*
/plugins/editors-xtd/fields/*
/plugins/editors-xtd/image/*
/plugins/editors-xtd/menu/*
/plugins/editors-xtd/module/*
/plugins/editors-xtd/pagebreak/*
/plugins/editors-xtd/readmore/*
/plugins/extension/example/*
/plugins/extension/joomla/*
/plugins/fields/calendar/*
/plugins/fields/checkboxes/*
/plugins/fields/color/*
/plugins/fields/editor/*
/plugins/fields/imagelist/*
/plugins/fields/integer/*
/plugins/fields/list/*
/plugins/fields/media/*
/plugins/fields/radio/*
/plugins/fields/repeatable/*
/plugins/fields/sql/*
/plugins/fields/text/*
/plugins/fields/textarea/*
/plugins/fields/url/*
/plugins/fields/user/*
/plugins/fields/usergrouplist/*
/plugins/finder/categories/*
/plugins/finder/contacts/*
/plugins/finder/content/*
/plugins/finder/newsfeeds/*
/plugins/finder/tags/*
/plugins/installer/folderinstaller/*
/plugins/installer/packageinstaller/*
/plugins/installer/urlinstaller/*
/plugins/privacy/actionlogs/*
/plugins/privacy/consents/*
/plugins/privacy/contact/*
/plugins/privacy/content/*
/plugins/privacy/message/*
/plugins/privacy/user/*
/plugins/quickicon/extensionupdate/*
/plugins/quickicon/joomlaupdate/*
/plugins/quickicon/phpversioncheck/*
/plugins/quickicon/privacycheck/*
/plugins/quickicon/index.html
/plugins/sampledata/blog/*
/plugins/search/categories/*
/plugins/search/contacts/*
/plugins/search/content/*
/plugins/search/newsfeeds/*
/plugins/search/tags/*
/plugins/search/weblinks/*
/plugins/search/index.html
/plugins/system/actionlogs/*
/plugins/system/cache/*
/plugins/system/debug/*
/plugins/system/fields/*
/plugins/system/highlight/*
/plugins/system/languagecode/*
/plugins/system/languagefilter/*
/plugins/system/log/*
/plugins/system/logout/*
/plugins/system/logrotation/*
/plugins/system/p3p/*
/plugins/system/privacyconsent/*
/plugins/system/redirect/*
/plugins/system/remember/*
/plugins/system/sef/*
/plugins/system/sessiongc/*
/plugins/system/stats/*
/plugins/system/updatenotification/*
/plugins/system/index.html
/plugins/twofactorauth/totp/*
/plugins/twofactorauth/yubikey/*
/plugins/user/contactcreator/*
/plugins/user/example/*
/plugins/user/joomla/*
/plugins/user/profile/*
/plugins/user/terms/*
/plugins/user/index.html
/plugins/index.html
/templates/beez3/*
/templates/protostar/*
/templates/system/*
/templates/index.html
/tmp/*
/configuration.php
/htaccess.txt
/index.php
/joomla.xml
/LICENSE.txt
/README.txt
/robots.txt.dist
/web.config.txt
```

## File: `Julia.gitignore`
```
# Files generated by invoking Julia with --code-coverage
*.jl.cov
*.jl.*.cov

# Files generated by invoking Julia with --track-allocation
*.jl.mem

# System-specific files and directories generated by the BinaryProvider and BinDeps packages
# They contain absolute paths specific to the host computer, and so should not be committed
deps/deps.jl
deps/build.log
deps/downloads/
deps/usr/
deps/src/

# Build artifacts for creating documentation generated by the Documenter package
docs/build/
docs/site/

# File generated by Pkg, the package manager, based on a corresponding Project.toml
# It records a fixed state of all packages used by the project. As such, it should not be
# committed for packages, but should be committed for applications that require a static
# environment.
Manifest*.toml

# File generated by the Preferences package to store local preferences
LocalPreferences.toml
JuliaLocalPreferences.toml
```

## File: `Katalon.gitignore`
```
# Katalon Test Suite
# Compiled class file
*.class
*.swp
output
!output/.gitkeep
build

Libs/TempTestCase*
Libs/TempTestSuite*
bin/lib/TempTestCase*
Reports/
\.classpath
\.project
\.settings/
bin/lib/
Libs/
.svn/
.gradle


# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*
```

## File: `KiCad.gitignore`
```
# For PCBs designed using KiCad: https://www.kicad.org/
# Format documentation: https://kicad.org/help/file-formats/

# Temporary files
*.000
*.bak
*.bck
*.kicad_pcb-bak
*.kicad_sch-bak
*-backups
*-cache*
*-bak
*-bak*
*~
~*
_autosave-*
\#auto_saved_files\#
*.tmp
*-save.pro
*-save.kicad_pcb
fp-info-cache
~*.lck
\#auto_saved_files#

# Netlist files (exported from Eeschema)
*.net

# Autorouter files (exported from Pcbnew)
*.dsn
*.ses

# Exported BOM files
*.xml
*.csv

# Archived Backups (KiCad 6.0)
**/*-backups/*.zip

# Local project settings
*.kicad_prl
```

## File: `Kohana.gitignore`
```
application/cache/*
application/logs/*
```

## File: `Kotlin.gitignore`
```
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*
replay_pid*

# Kotlin Gradle plugin data, see https://kotlinlang.org/docs/whatsnew20.html#new-directory-for-kotlin-data-in-gradle-projects
.kotlin/
```

## File: `LabVIEW.gitignore`
```
# Libraries
*.lvlibp
*.llb

# Shared objects (inc. Windows DLLs)
*.dll
*.so
*.so.*
*.dylib

# Executables
*.exe

# Metadata
*.aliases
*.lvlps
.cache/
```

## File: `LangChain.gitignore`
```
# gitignore template for LangChain products, e.g., LangGraph, LangSmith
# website: https://www.langchain.com/
# website: https://www.langchain.com/langgraph

# LangGraph
.langgraph_api/
```

## File: `Laravel.gitignore`
```
/vendor/
node_modules/
npm-debug.log
yarn-error.log

# Laravel 4 specific
bootstrap/compiled.php
app/storage/

# Laravel 5 & Lumen specific
public/storage
public/hot

# Laravel 5 & Lumen specific with changed public path
public_html/storage
public_html/hot

storage/*.key
.env
Homestead.yaml
Homestead.json
/.vagrant
.phpunit.result.cache

/public/build
/storage/pail
.env.backup
.env.production
.phpactor.json
auth.json
```

## File: `Leiningen.gitignore`
```
pom.xml
pom.xml.asc
*.jar
*.class
/lib/
/classes/
/target/
/checkouts/
.lein-deps-sum
.lein-repl-history
.lein-plugins/
.lein-failures
.nrepl-port
.cpcache/
```

## File: `LemonStand.gitignore`
```
boot.php
index.php
install.php
/config/*
!/config/config.php
/controllers/*
/init/*
/logs/*
/phproad/*
/temp/*
/uploaded/*
/installer_files/*
/modules/backend/*
/modules/blog/*
/modules/cms/*
/modules/core/*
/modules/session/*
/modules/shop/*
/modules/system/*
/modules/users/*
# add content_*.php if you don't want erase client changes to content
```

## File: `LICENSE`
```
CC0 1.0 Universal

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator and
subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for the
purpose of contributing to a commons of creative, cultural and scientific
works ("Commons") that the public can reliably and without fear of later
claims of infringement build upon, modify, incorporate in other works, reuse
and redistribute as freely as possible in any form whatsoever and for any
purposes, including without limitation commercial purposes. These owners may
contribute to the Commons to promote the ideal of a free culture and the
further production of creative, cultural and scientific works, or to gain
reputation or greater distribution for their Work in part through the use and
efforts of others.

For these and/or other purposes and motivations, and without any expectation
of additional consideration or compensation, the person associating CC0 with a
Work (the "Affirmer"), to the extent that he or she is an owner of Copyright
and Related Rights in the Work, voluntarily elects to apply CC0 to the Work
and publicly distribute the Work under its terms, with knowledge of his or her
Copyright and Related Rights in the Work and the meaning and intended legal
effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not limited
to, the following:

  i. the right to reproduce, adapt, distribute, perform, display, communicate,
  and translate a Work;

  ii. moral rights retained by the original author(s) and/or performer(s);

  iii. publicity and privacy rights pertaining to a person's image or likeness
  depicted in a Work;

  iv. rights protecting against unfair competition in regards to a Work,
  subject to the limitations in paragraph 4(a), below;

  v. rights protecting the extraction, dissemination, use and reuse of data in
  a Work;

  vi. database rights (such as those arising under Directive 96/9/EC of the
  European Parliament and of the Council of 11 March 1996 on the legal
  protection of databases, and under any national implementation thereof,
  including any amended or successor version of such directive); and

  vii. other similar, equivalent or corresponding rights throughout the world
  based on applicable law or treaty, and any national implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention of,
applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and
unconditionally waives, abandons, and surrenders all of Affirmer's Copyright
and Related Rights and associated claims and causes of action, whether now
known or unknown (including existing as well as future claims and causes of
action), in the Work (i) in all territories worldwide, (ii) for the maximum
duration provided by applicable law or treaty (including future time
extensions), (iii) in any current or future medium and for any number of
copies, and (iv) for any purpose whatsoever, including without limitation
commercial, advertising or promotional purposes (the "Waiver"). Affirmer makes
the Waiver for the benefit of each member of the public at large and to the
detriment of Affirmer's heirs and successors, fully intending that such Waiver
shall not be subject to revocation, rescission, cancellation, termination, or
any other legal or equitable action to disrupt the quiet enjoyment of the Work
by the public as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason be
judged legally invalid or ineffective under applicable law, then the Waiver
shall be preserved to the maximum extent permitted taking into account
Affirmer's express Statement of Purpose. In addition, to the extent the Waiver
is so judged Affirmer hereby grants to each affected person a royalty-free,
non transferable, non sublicensable, non exclusive, irrevocable and
unconditional license to exercise Affirmer's Copyright and Related Rights in
the Work (i) in all territories worldwide, (ii) for the maximum duration
provided by applicable law or treaty (including future time extensions), (iii)
in any current or future medium and for any number of copies, and (iv) for any
purpose whatsoever, including without limitation commercial, advertising or
promotional purposes (the "License"). The License shall be deemed effective as
of the date CC0 was applied by Affirmer to the Work. Should any part of the
License for any reason be judged legally invalid or ineffective under
applicable law, such partial invalidity or ineffectiveness shall not
invalidate the remainder of the License, and in such case Affirmer hereby
affirms that he or she will not (i) exercise any of his or her remaining
Copyright and Related Rights in the Work or (ii) assert any associated claims
and causes of action with respect to the Work, in either case contrary to
Affirmer's express Statement of Purpose.

4. Limitations and Disclaimers.

  a. No trademark or patent rights held by Affirmer are waived, abandoned,
  surrendered, licensed or otherwise affected by this document.

  b. Affirmer offers the Work as-is and makes no representations or warranties
  of any kind concerning the Work, express, implied, statutory or otherwise,
  including without limitation warranties of title, merchantability, fitness
  for a particular purpose, non infringement, or the absence of latent or
  other defects, accuracy, or the present or absence of errors, whether or not
  discoverable, all to the greatest extent permissible under applicable law.

  c. Affirmer disclaims responsibility for clearing rights of other persons
  that may apply to the Work or any use thereof, including without limitation
  any person's Copyright and Related Rights in the Work. Further, Affirmer
  disclaims responsibility for obtaining any necessary consents, permissions
  or other rights required for any use of the Work.

  d. Affirmer understands and acknowledges that Creative Commons is not a
  party to this document and has no duty or obligation with respect to this
  CC0 or use of the Work.

For more information, please see
<http://creativecommons.org/publicdomain/zero/1.0/>
```

## File: `Lilypond.gitignore`
```
*.pdf
*.ps
*.midi
*.mid
*.log
*~
```

## File: `Lithium.gitignore`
```
libraries/*
resources/tmp/*
```

## File: `Lua.gitignore`
```
# Compiled Lua sources
luac.out

# luarocks build files
*.src.rock
*.zip
*.tar.gz

# Object files
*.o
*.os
*.ko
*.obj
*.elf

# Precompiled Headers
*.gch
*.pch

# Libraries
*.lib
*.a
*.la
*.lo
*.def
*.exp

# Shared objects (inc. Windows DLLs)
*.dll
*.so
*.so.*
*.dylib

# Executables
*.exe
*.out
*.app
*.i*86
*.x86_64
*.hex

```

## File: `Luau.gitignore`
```
# A fast, small, safe, gradually typed embeddable scripting language derived from Lua
#
# https://github.com/luau-lang/luau
# https://luau.org/

# Code coverage
coverage.out

# Profiling
profile.out
profile.svg

# Time trace
trace.json
```

## File: `Magento.gitignore`
```
#--------------------------#
# Magento Default Files    #
#--------------------------#

/PATCH_*.sh

/app/etc/local.xml

/media/*
!/media/.htaccess

!/media/customer
/media/customer/*
!/media/customer/.htaccess

!/media/dhl
/media/dhl/*
!/media/dhl/logo.jpg

!/media/downloadable
/media/downloadable/*
!/media/downloadable/.htaccess

!/media/xmlconnect
/media/xmlconnect/*

!/media/xmlconnect/custom
/media/xmlconnect/custom/*
!/media/xmlconnect/custom/ok.gif

!/media/xmlconnect/original
/media/xmlconnect/original/*
!/media/xmlconnect/original/ok.gif

!/media/xmlconnect/system
/media/xmlconnect/system/*
!/media/xmlconnect/system/ok.gif

/var/*
!/var/.htaccess

!/var/package
/var/package/*
!/var/package/*.xml

```

## File: `Maven.gitignore`
```
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
# https://maven.apache.org/wrapper/#usage-without-binary-jar
.mvn/wrapper/maven-wrapper.jar

# Eclipse m2e generated files
# Eclipse Core
.project
# JDT-specific (Eclipse Java Development Tools)
.classpath
```

## File: `Mercury.gitignore`
```
Mercury/
Mercury.modules
*.mh
*.err
*.init
*.dll
*.exe
*.a
*.so
*.dylib
*.beams
*.d
*.c_date
```

## File: `MetaProgrammingSystem.gitignore`
```
workspace.xml
junitvmwatcher*.properties
build.properties

# generated java classes and java source files
#   manually add any custom artifacts that can't be generated from the models
#   http://confluence.jetbrains.com/display/MPSD25/HowTo+--+MPS+and+Git
classes_gen
source_gen
source_gen.caches

# generated test code and test results
test_gen
test_gen.caches
TEST-*.xml
junit*.properties
```

## File: `Modelica.gitignore`
```
# Modelica - an object-oriented language for modeling of cyber-physical systems
# https://modelica.org/
# Ignore temporary files, build results, simulation files

## Modelica-specific files
*~
*.bak
*.bak-mo
*.mof
\#*\#
*.moe
*.mol

## Build artefacts
*.exe
*.exp
*.o
*.pyc

## Simulation files
*.mat

## Package files
*.gz
*.rar
*.tar
*.zip

## Dymola-specific files
buildlog.txt
dsfinal.txt
dsin.txt
dslog.txt
dsmodel*
dsres.txt
dymosim*
request
stat
status
stop
success
*.
```

## File: `ModelSim.gitignore`
```
# ignore ModelSim generated files and directories (temp files and so on)
[_@]*

# ignore compilation output of ModelSim
*.mti
*.dat
*.dbs
*.psm
*.bak
*.cmp
*.jpg
*.html
*.bsf

# ignore simulation output of ModelSim
wlf*
*.wlf
*.vstf
*.ucdb
cov*/
transcript*
sc_dpiheader.h
vsim.dbg
```

## File: `Nanoc.gitignore`
```
# For projects using Nanoc (http://nanoc.ws/)

# Default location for output (needs to match output_dir's value found in nanoc.yaml)
output/

# Temporary file directory
tmp/nanoc/

# Crash Log
crash.log
```

## File: `Nestjs.gitignore`
```
# Nestjs specific
/dist
/node_modules
/build
/tmp

# Logs
logs
*.log
npm-debug.log*
pnpm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# dotenv environment variable files
.env
.env.development
.env.test
.env.production

# temp directory
.temp
.tmp
```

## File: `Nextjs.gitignore`
```
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# local env files
.env*.local
.env

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
```

## File: `Nim.gitignore`
```
nimcache/
nimblecache/
htmldocs/
```

## File: `Nix.gitignore`
```
# Ignore build outputs from performing a nix-build or `nix build` command
result
result-*

# Ignore automatically generated direnv output
.direnv
```

## File: `Node.gitignore`
```
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Diagnostic reports (https://nodejs.org/api/report.html)
report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

# Coverage directory used by tools like istanbul
coverage
*.lcov

# nyc test coverage
.nyc_output

# Grunt intermediate storage (https://gruntjs.com/creating-plugins#storing-task-files)
.grunt

# Bower dependency directory (https://bower.io/)
bower_components

# node-waf configuration
.lock-wscript

# Compiled binary addons (https://nodejs.org/api/addons.html)
build/Release

# Dependency directories
node_modules/
jspm_packages/

# Snowpack dependency directory (https://snowpack.dev/)
web_modules/

# TypeScript cache
*.tsbuildinfo

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Optional stylelint cache
.stylelintcache

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# dotenv environment variable files
.env
.env.*
!.env.example

# parcel-bundler cache (https://parceljs.org/)
.cache
.parcel-cache

# Next.js build output
.next
out

# Nuxt.js build / generate output
.nuxt
dist
.output

# Gatsby files
.cache/
# Comment in the public line in if your project uses Gatsby and not Next.js
# https://nextjs.org/blog/next-9-1#public-directory-support
# public

# vuepress build output
.vuepress/dist

# vuepress v2.x temp and cache directory
.temp
.cache

# Sveltekit cache directory
.svelte-kit/

# vitepress build output
**/.vitepress/dist

# vitepress cache directory
**/.vitepress/cache

# Docusaurus cache and generated files
.docusaurus

# Serverless directories
.serverless/

# FuseBox cache
.fusebox/

# DynamoDB Local files
.dynamodb/

# Firebase cache directory
.firebase/

# TernJS port file
.tern-port

# Stores VSCode versions used for testing VSCode extensions
.vscode-test

# pnpm
.pnpm-store

# yarn v3
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/sdks
!.yarn/versions

# Vite files
vite.config.js.timestamp-*
vite.config.ts.timestamp-*
.vite/
```

## File: `Objective-C.gitignore`
```
# Xcode
#
# gitignore contributors: remember to update Global/Xcode.gitignore, Objective-C.gitignore & Swift.gitignore

## User settings
xcuserdata/

## Obj-C/Swift specific
*.hmap

## App packaging
*.ipa
*.dSYM.zip
*.dSYM

# CocoaPods
#
# We recommend against adding the Pods directory to your .gitignore. However
# you should judge for yourself, the pros and cons are mentioned at:
# https://guides.cocoapods.org/using/using-cocoapods.html#should-i-check-the-pods-directory-into-source-control
#
# Pods/
#
# Add this line if you want to avoid checking in source code from the Xcode workspace
# *.xcworkspace

# Carthage
#
# Add this line if you want to avoid checking in source code from Carthage dependencies.
# Carthage/Checkouts

Carthage/Build/

# fastlane
#
# It is recommended to not store the screenshots in the git repo.
# Instead, use fastlane to re-generate the screenshots whenever they are needed.
# For more information about the recommended setup visit:
# https://docs.fastlane.tools/best-practices/source-control/#source-control

fastlane/report.xml
fastlane/Preview.html
fastlane/screenshots/**/*.png
fastlane/test_output
```

## File: `OCaml.gitignore`
```
*.annot
*.cmo
*.cma
*.cmi
*.a
*.o
*.cmx
*.cmxs
*.cmxa

# Files containing detailed information about the compilation (generated
# by `ocamlc`/`ocamlopt` when invoked using the option `-bin-annot`).
# These files are typically useful for code inspection tools
# (e.g. Merlin).
*.cmt
*.cmti

# ocamlbuild and Dune default working directory
_build/

# ocamlbuild targets
*.byte
*.native

# oasis generated files
setup.data
setup.log

# Merlin configuring file for Vim and Emacs
.merlin

# Dune generated files
*.install

# Local OPAM switch
_opam/
```

## File: `Opa.gitignore`
```
_build
_tracks

opa-debug-js

*.opp
*.opx
*.opx.broken
*.dump
*.api
*.api-txt
*.exe
*.log
```

## File: `OpenCart.gitignore`
```
.htaccess
/config.php
admin/config.php

!index.html

download/
image/data/
image/cache/
system/cache/
system/logs/

system/storage/

# vQmod log files
vqmod/logs/*
# vQmod cache files
vqmod/vqcache/*
vqmod/checked.cache
vqmod/mods.cache
```

## File: `OracleForms.gitignore`
```
# Compiled Form Modules
*.fmx

# Compiled Menu Modules
*.mmx

# Compiled Pre-Linked Libraries
*.plx
```

## File: `Packer.gitignore`
```
# Cache objects
packer_cache/

# Crash log
crash.log

# https://www.packer.io/guides/hcl/variables
# Exclude all .pkrvars.hcl files, which are likely to contain sensitive data,
# such as password, private keys, and other secrets. These should not be part of
# version control as they are data points which are potentially sensitive and
# subject to change depending on the environment.
#
*.pkrvars.hcl

# For built boxes
*.box
```

## File: `Perl.gitignore`
```
!Build/
.last_cover_stats
/META.yml
/META.json
/MYMETA.*
*.o
*.pm.tdy
*.bs

# Devel::Cover
cover_db/

# Devel::NYTProf
nytprof.out

# Dist::Zilla
/.build/

# Module::Build
_build/
Build
Build.bat

# Module::Install
inc/

# ExtUtils::MakeMaker
/blib/
/_eumm/
/*.gz
/Makefile
/Makefile.old
/MANIFEST.bak
/pm_to_blib
/*.zip

# Carton/Carmel
/local/
/.carmel/
# cpanfile.snapshot should generally be ignored for library code, otherwise included
# cpanfile.snapshot
```

## File: `Phalcon.gitignore`
```
/cache/
/config/development/
```

## File: `PlayFramework.gitignore`
```
# Ignore Play! working directory #
bin/
/db
.eclipse
/lib/
/logs/
/modules
/project/project
/project/target
/target
tmp/
test-result
server.pid
*.eml
/dist/
.cache
```

## File: `Plone.gitignore`
```
*.pyc
*.pyo
*.tmp*
*.mo
*.egg
*.EGG
*.egg-info
*.EGG-INFO
.*.cfg
bin/
build/
develop-eggs/
downloads/
eggs/
fake-eggs/
parts/
dist/
var/
```

## File: `Prestashop.gitignore`
```
# Cache, temp and personal files

/.htaccess
*.log

# Cache
/cache/*
!/cache/.htaccess
!/cache/cachefs/index.php
!/cache/deprecated.txt
!/cache/index.php
!/cache/purifier/index.php
!/cache/push/activity
!/cache/push/index.php
!/cache/push/trends
!/cache/sandbox/index.php
!/cache/smarty/cache/index.php
!/cache/smarty/compile/index.php
!/cache/smarty/index.php
!/cache/tcpdf/index.php

# Download
/download/*
!/download/.htaccess
!/download/index.php

# Images
/img/*
!/img/.htaccess
!/img/index.php
!/img/404.gif
!/img/bg_500.png
!/img/bg_loader.png
!/img/favicon.ico
!/img/loader.gif
!/img/loadingAnimation.gif
!/img/logo.jpg
!/img/logo.png
!/img/logo_invoice.jpg
!/img/logo_stores.png
!/img/macFFBgHack.png
!/img/prestashop-avatar.png
!/img/prestashop@2x.png
!/img/preston-login-wink@2x.png
!/img/preston-login@2x.png
!/img/questionmark.png
!/img/genders/index.php
!/img/admin/index.php
!/img/c/index.php
!/img/cms/index.php
!/img/co/index.php
!/img/jquery-ui
!/img/l/index.php
!/img/m/index.php
!/img/os/index.php
!/img/p/index.php
!/img/s/index.php
!/img/scenes
!/img/st/index.php
!/img/su/index.php
!/img/t/index.php
!/img/tmp/index.php

# Upload
/upload/*
!/upload/.htaccess

/vendor/*
/docs/phpdoc-sf/
/composer.lock
*.hot-update.js
*.hot-update.json


/admin-dev/autoupgrade/*
!/admin-dev/autoupgrade/index.php
!/admin-dev/autoupgrade/backup/index.php

/admin-dev/backups/*
!/admin-dev/backups/.htaccess

/admin-dev/import/*
!/admin-dev/import/.htaccess
!/admin-dev/import/index.php

/admin-dev/export/*
!/admin-dev/export/.htaccess
!/admin-dev/export/index.php

# Downloaded RTL files
/admin-dev/themes/default/css/bundle/default_rtl.css
/admin-dev/themes/default/css/bundle/shared_rtl.css
/admin-dev/themes/default/css/font_rtl.css
/admin-dev/themes/default/css/overrides_rtl.css
/admin-dev/themes/default/css/vendor/font-awesome/font-awesome_rtl.css
/admin-dev/themes/default/css/vendor/nv.d3_rtl.css
/admin-dev/themes/default/css/vendor/titatoggle-min_rtl.css
/admin-dev/themes/default/public/theme_rtl.css
/admin-dev/themes/new-theme/css/module/drop_rtl.css
/admin-dev/themes/new-theme/css/right-sidebar_rtl.css

themes/*/cache/*

# Config

config/settings.inc.php
config/settings.old.php
config/xml/*
config/themes/*
!config/xml/themes/default.xml
themes/*/config/settings_*.json
app/config/parameters.old.yml
app/config/config.php

# Themes, modules and overrides

modules/*
override/*
themes/*/
!themes/classic
!themes/_core
!themes/_libraries

# Vendors and dependencies

bower_components/
node_modules/
composer.phar
php-cs-fixer
.grunt/*

# Translations and emails templates

translations/*
mails/*
!mails/themes/
!mails/_partials/
themes/default-bootstrap/lang/*
themes/default-bootstrap/modules/*/translations/*.php
themes/default-bootstrap/mails/*
!themes/default-bootstrap/mails/en/
themes/default-bootstrap/modules/*/mails/*
!themes/default-bootstrap/modules/*/mails/en

# MISC

*sitemap.xml
/robots.txt

# Symfony

/bin/
/app/Resources/geoip/GeoLite2-City.mmdb
/app/Resources/translations/*
!/app/Resources/translations/default
/app/config/parameters.yml
/app/config/parameters.php
/build/
/phpunit.xml
/var/*
!/var/cache
/var/cache/*
!var/cache/.gitkeep
!/var/logs
/var/logs/*
!var/logs/.gitkeep
!/var/sessions
/var/sessions/*
!var/sessions/.gitkeep
!var/SymfonyRequirements.php
/vendor/
/web/bundles/

```

## File: `Processing.gitignore`
```
.DS_Store
applet
application.linux-arm64
application.linux-armv6hf
application.linux32
application.linux64
application.windows32
application.windows64
application.macosx
out
```

## File: `PureScript.gitignore`
```
# Dependencies
.psci_modules
.spago
bower_components
node_modules

# Generated files
.psci
output
```

## File: `Python.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
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
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#   Usually these files are written by a python script from a template
#   before PyInstaller builds the exe, so as to inject date/other infos into it.
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
*.py.cover
.hypothesis/
.pytest_cache/
cover/

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
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
# Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
# uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
# poetry.lock
# poetry.toml

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
#   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
# pdm.lock
# pdm.toml
.pdm-python
.pdm-build/

# pixi
#   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
# pixi.lock
#   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
#   in the .venv directory. It is recommended not to include this directory in version control.
.pixi

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# Redis
*.rdb
*.aof
*.pid

# RabbitMQ
mnesia/
rabbitmq/
rabbitmq-data/

# ActiveMQ
activemq-data/

# SageMath parsed files
*.sage.py

# Environments
.env
.envrc
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
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#   JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#   be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#   and can be added to the global gitignore or merged into this file.  For a more nuclear
#   option (not recommended) you can uncomment the following to ignore the entire idea folder.
# .idea/

# Abstra
#   Abstra is an AI-powered process automation framework.
#   Ignore directories containing user credentials, local state, and settings.
#   Learn more at https://abstra.io/docs
.abstra/

# Visual Studio Code
#   Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore 
#   that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
#   and can be added to the global gitignore or merged into this file. However, if you prefer, 
#   you could uncomment the following to ignore the entire vscode folder
# .vscode/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

# Marimo
marimo/_static/
marimo/_lsp/
__marimo__/

# Streamlit
.streamlit/secrets.toml
```

## File: `Qooxdoo.gitignore`
```
cache
cache-downloads
inspector
api
source/inspector.html
```

## File: `Qt.gitignore`
```
# C++ objects and libs
*.slo
*.lo
*.o
*.a
*.la
*.lai
*.so
*.so.*
*.dll
*.dylib

# Qt-es
object_script.*.Release
object_script.*.Debug
*_plugin_import.cpp
/.qmake.cache
/.qmake.stash
*.pro.user
*.pro.user.*
*.qbs.user
*.qbs.user.*
*.moc
moc_*.cpp
moc_*.h
qrc_*.cpp
ui_*.h
*.qmlc
*.jsc
Makefile*
*build-*
*.qm
*.prl

# Qt unit tests
target_wrapper.*

# QtCreator
*.autosave

# QtCreator Qml
*.qmlproject.user
*.qmlproject.user.*

# QtCreator CMake
CMakeLists.txt.user*

# QtCreator 4.8< compilation database
compile_commands.json

# QtCreator local machine specific files for imported projects
*creator.user*

*_qmlcache.qrc
```

## File: `R.gitignore`
```
# History files
.Rhistory
.Rapp.history

# Session Data files
.RData
.RDataTmp

# User-specific files
.Ruserdata

# Example code in package build process
*-Ex.R

# Output files from R CMD build
/*.tar.gz

# Output files from R CMD check
/*.Rcheck/

# RStudio files
.Rproj.user/

# produced vignettes
vignettes/*.html
vignettes/*.pdf

# OAuth2 token, see https://github.com/hadley/httr/releases/tag/v0.3
.httr-oauth

# knitr and R markdown default cache directories
*_cache/
/cache/

# Temporary files created by R markdown
*.utf8.md
*.knit.md

# R Environment Variables
.Renviron

# pkgdown site
docs/

# translation temp files
po/*~

# RStudio Connect folder
rsconnect/
```

## File: `Racket.gitignore`
```
.DS_Store
compiled/
/doc/
*~
*.bak
\#*
.\#*
```

## File: `Rails.gitignore`
```
*.rbc
capybara-*.html
.rspec
/db/*.sqlite3
/db/*.sqlite3-journal
/db/*.sqlite3-[0-9]*
/public/system
/coverage/
/spec/tmp
*.orig
rerun.txt
pickle-email-*.html

# Ignore all logfiles and tempfiles.
/log/*
/tmp/*
!/log/.keep
!/tmp/.keep

# TODO Comment out this rule if you are OK with secrets being uploaded to the repo
config/initializers/secret_token.rb
config/master.key

# Only include if you have production secrets in this file, which is no longer a Rails default
# config/secrets.yml

# dotenv, dotenv-rails
# TODO Comment out these rules if environment variables can be committed
.env
.env*.local

## Environment normalization:
/.bundle
/vendor/bundle

# these should all be checked in to normalize the environment:
# Gemfile.lock, .ruby-version, .ruby-gemset

# unless supporting rvm < 1.11.0 or doing something fancy, ignore this:
.rvmrc

# if using bower-rails ignore default bower_components path bower.json files
/vendor/assets/bower_components
*.bowerrc
bower.json

# Ignore pow environment settings
.powenv

# Ignore Byebug command history file.
.byebug_history

# Ignore node_modules
node_modules/

# Ignore precompiled javascript packs
/public/packs
/public/packs-test
/public/assets

# Ignore yarn files
/yarn-error.log
yarn-debug.log*
.yarn-integrity

# Ignore uploaded files in development
/storage/*
!/storage/.keep
/public/uploads
```

## File: `Raku.gitignore`
```
# Gitignore for Raku (https://raku.org)
# As part of https://github.com/github/gitignore

# precompiled files
.precomp
lib/.precomp

```

## File: `README.md`
```markdown
# A collection of `.gitignore` templates

This is GitHub’s collection of [`.gitignore`][man] file templates.
We use this list to populate the `.gitignore` template choosers available
in the GitHub.com interface when creating new repositories and files.

For more information about how `.gitignore` files work, and how to use them,
the following resources are a great place to start:

- The [Ignoring Files chapter][chapter] of the [Pro Git][progit] book.
- The [Ignoring Files article][help] on the GitHub Help site.
- The [gitignore(5)][man] manual page.

[man]: https://git-scm.com/docs/gitignore
[help]: https://help.github.com/articles/ignoring-files
[chapter]: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring
[progit]: https://git-scm.com/book

## Folder structure

We support a collection of templates, organized in this way:

- The root folder contains templates in common use, to help people get started
  with popular programming languages and technologies. These define a meaningful
  set of rules to help get started, and ensure you are not committing
  unimportant files into your repository.
- [`Global`](./Global) contains templates for various editors, tools and
  operating systems that can be used in different situations. It is recommended
  that you either [add these to your global template](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files#configuring-ignored-files-for-all-repositories-on-your-computer)
  or merge these rules into your project-specific templates if you want to use
  them permanently.
- [`community`](./community) contains specialized templates for other popular
  languages, tools and project, which don't currently belong in the mainstream
  templates. These should be added to your project-specific templates when you
  decide to adopt the framework or tool.

## What makes a good template?

A template should contain a set of rules to help Git repositories work with a
specific programming language, framework, tool or environment.

If it's not possible to curate a small set of useful rules for this situation,
then the template is not a good fit for this collection.

If a template is mostly a list of files installed by a particular version of
some software (e.g. a PHP framework), it could live under the `community`
directory. See [versioned templates](#versioned-templates) for more details.

If you have a small set of rules, or want to support a technology that is not
widely in use, and still believe this will be helpful to others, please read the
section about [specialized templates](#specialized-templates) for more details.

Include details when opening pull request if the template is important and visible. We
may not accept it immediately, but we can promote it to the root at a later date
based on interest.

Please also understand that we can’t list every tool that ever existed.
Our aim is to curate a collection of the _most common and helpful_ templates,
not to make sure we cover every project possible. If we choose not to
include your language, tool, or project, it’s not because it’s not awesome.

## Contributing guidelines

We’d love for you to help us improve this project. To help us keep this collection
high quality, we request that contributions adhere to the following guidelines.

- **Provide a link to the application or project’s homepage**. Unless it’s
  extremely popular, there’s a chance the maintainers don’t know about or use
  the language, framework, editor, app, or project your change applies to.

- **Provide links to documentation** supporting the change you’re making.
  Current, canonical documentation mentioning the files being ignored is best.
  If documentation isn’t available to support your change, do the best you can
  to explain what the files being ignored are for.

- **Explain why you’re making a change**. Even if it seems self-evident, please
  take a sentence or two to tell us why your change or addition should happen.
  It’s especially helpful to articulate why this change applies to _everyone_
  who works with the applicable technology, rather than just you or your team.

- **Please consider the scope of your change**. If your change is specific to a
  certain language or framework, then make sure the change is made to the
  template for that language or framework, rather than to the template for an
  editor, tool, or operating system.

- **Please only modify _one template_ per pull request**. This helps keep pull
  requests and feedback focused on a specific project or technology.

In general, the more you can do to help us understand the change you’re making,
the more likely we’ll be to accept your contribution quickly.

## Versioned templates

Some templates can change greatly between versions, and if you wish to contribute
to this repository we need to follow this specific flow:

- the template at the root should be the current supported version
- the template at the root should not have a version in the filename (i.e.
  "evergreen")
- previous versions of templates should live under `community/`
- previous versions of the template should embed the version in the filename,
  for readability

This helps ensure users get the latest version (because they'll use whatever is
at the root) but helps maintainers support older versions still in the wild.

## Specialized templates

If you have a template that you would like to contribute, but it isn't quite
mainstream, please consider adding this to the `community` directory under a
folder that best suits where it belongs.

The rules in your specialized template should be specific to the framework or
tool, and any additional templates should be mentioned in a comment in the
header of the template.

For example, this template might live at `community/DotNet/InforCRM.gitignore`:

```gitignore
# gitignore template for InforCRM (formerly SalesLogix)
# website: https://www.infor.com/product-summary/cx/infor-crm/
#
# Recommended: VisualStudio.gitignore

# Ignore model files that are auto-generated
ModelIndex.xml
ExportedFiles.xml

# Ignore deployment files
[Mm]odel/[Dd]eployment

# Force include portal SupportFiles
!Model/Portal/*/SupportFiles/[Bb]in/
!Model/Portal/PortalTemplates/*/SupportFiles/[Bb]in
```

## Contributing workflow

Here’s how we suggest you go about proposing a change to this project:

1. [Fork this project][fork] to your account.
2. [Create a branch][branch] for the change you intend to make.
3. Make your changes to your fork.
4. [Send a pull request][pr] from your fork’s branch to our `main` branch.

Using the web-based interface to make changes is fine too, and will help you
by automatically forking the project and prompting to send a pull request too.

[fork]: https://help.github.com/articles/fork-a-repo/
[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[pr]: https://help.github.com/articles/using-pull-requests/

## License

[CC0-1.0](./LICENSE).
```

## File: `ReScript.gitignore`
```
/node_modules/
/lib/
.bsb.lock
```

## File: `RhodesRhomobile.gitignore`
```
rholog-*
sim-*
bin/libs
bin/RhoBundle
bin/tmp
bin/target
bin/*.ap_
*.o
*.jar
```

## File: `ROS.gitignore`
```
devel/
logs/
build/
bin/
lib/
msg_gen/
srv_gen/
msg/*Action.msg
msg/*ActionFeedback.msg
msg/*ActionGoal.msg
msg/*ActionResult.msg
msg/*Feedback.msg
msg/*Goal.msg
msg/*Result.msg
msg/_*.py
build_isolated/
devel_isolated/

# Generated by dynamic reconfigure
*.cfgc
/cfg/cpp/
/cfg/*.py

# Ignore generated docs
*.dox
*.wikidoc

# eclipse stuff
.project
.cproject

# qcreator stuff
CMakeLists.txt.user

srv/_*.py
*.pcd
*.pyc
qtcreator-*
*.user

/planning/cfg
/planning/docs
/planning/src

*~

# Emacs
.#*

# Catkin custom files
CATKIN_IGNORE
```

## File: `Ruby.gitignore`
```
*.gem
*.rbc
/.config
/coverage/
/InstalledFiles
/pkg/
/spec/reports/
/spec/examples.txt
/test/tmp/
/test/version_tmp/
/tmp/

# Used by dotenv library to load environment variables.
# .env

# Ignore Byebug command history file.
.byebug_history

## Specific to RubyMotion:
.dat*
.repl_history
build/
*.bridgesupport
build-iPhoneOS/
build-iPhoneSimulator/

## Specific to RubyMotion (use of CocoaPods):
#
# We recommend against adding the Pods directory to your .gitignore. However
# you should judge for yourself, the pros and cons are mentioned at:
# https://guides.cocoapods.org/using/using-cocoapods.html#should-i-check-the-pods-directory-into-source-control
#
# vendor/Pods/

## Documentation cache and generated files:
/.yardoc/
/_yardoc/
/doc/
/rdoc/

## Environment normalization:
/.bundle/
/vendor/bundle
/lib/bundler/man/

# for a library or gem, you might want to ignore these files since the code is
# intended to run in multiple environments; otherwise, check them in:
# Gemfile.lock
# .ruby-version
# .ruby-gemset

# unless supporting rvm < 1.11.0 or doing something fancy, ignore this:
.rvmrc

# Used by RuboCop. Remote config files pulled in from inherit_from directive.
# .rubocop-https?--*
```

## File: `Rust.gitignore`
```
# Generated by Cargo
# will have compiled files and executables
debug
target

# These are backup files generated by rustfmt
**/*.rs.bk

# MSVC Windows builds of rustc generate these, which store debugging information
*.pdb

# Generated by cargo mutants
# Contains mutation testing data
**/mutants.out*/

# RustRover
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```

## File: `Salesforce.gitignore`
```
# This file is used for Git repositories to specify intentionally untracked files that Git should ignore. 
# If you are not using git, you can delete this file. For more information see: https://git-scm.com/docs/gitignore
# For useful gitignore templates see: https://github.com/github/gitignore

# Salesforce cache
.sf/
.sfdx/
.localdevserver/
deploy-options.json
.localdev

# LWC VSCode autocomplete
**/lwc/jsconfig.json

# LWC Jest coverage reports
coverage/

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Eslint cache
.eslintcache

# Windows system files
Thumbs.db
ehthumbs.db
[Dd]esktop.ini
$RECYCLE.BIN/

# Salesforce Analyzer results
sca-results.csv
sfca_results.json

# Local environment variables
.env
```

## File: `Sass.gitignore`
```
.sass-cache/
*.css.map
*.sass.map
*.scss.map
```

## File: `Scala.gitignore`
```
*.class
*.log

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*
```

## File: `Scheme.gitignore`
```
*.ss~
*.ss#*
.#*.ss

*.scm~
*.scm#*
.#*.scm
```

## File: `SCons.gitignore`
```
# for projects that use SCons for building: http://http://www.scons.org/
.sconsign.dblite

# When configure fails, SCons outputs these
config.log
.sconf_temp
```

## File: `Scrivener.gitignore`
```
*/Files/binder.autosave
*/Files/binder.backup
*/Files/search.indexes
*/Files/user.lock
*/Files/Docs/docs.checksum
*/Files/Data/docs.checksum
*/QuickLook/
*/Settings/ui.plist
```

## File: `Sdcc.gitignore`
```
# SDCC stuff
*.lnk
*.lst
*.map
*.mem
*.rel
*.rst
*.sym
```

## File: `SeamGen.gitignore`
```
/bootstrap/data
/bootstrap/tmp
/classes/
/dist/
/exploded-archives/
/test-build/
/test-output/
/test-report/
/target/
temp-testng-customsuite.xml

# based on http://stackoverflow.com/a/8865858/422476 I am removing inline comments

#/classes/  		              all class files
#/dist/                       contains generated war files for deployment
#/exploded-archives/		      war content generation during deploy (or explode)
#/test-build/                 test compilation (ant target for Seam)
#/test-output/                test results
#/test-report/                test report generation for, e.g., Hudson
#/target/                     maven output folder
#temp-testng-customsuite.xml	generated when running test cases under Eclipse

# Thanks to @VonC and @kraftan for their helpful answers on a related question
# on StackOverflow.com:
# http://stackoverflow.com/questions/4176687
# /what-is-the-recommended-source-control-ignore-pattern-for-seam-projects
```

## File: `SketchUp.gitignore`
```
*.skb
```

## File: `Smalltalk.gitignore`
```
# changes file
*.changes
*.chg

# system image
*.image
*.img7
*.img

# Pharo Smalltalk Debug log file
PharoDebug.log

# Squeak Smalltalk Debug log file
SqueakDebug.log

# Dolphin Smalltalk source file
*.sml

# Dolphin Smalltalk error file
*.errors

# Monticello package cache
/package-cache

# playground cache
/play-cache
/play-stash

# Metacello-github cache
/github-cache
github-*.zip
```

## File: `Solidity-Remix.gitignore`
```
# Remix compiler artifacts
**/artifacts/
**/artifacts/**

# Remix plugin state folders
deps/
states/

# Debug info
*.dbg.json
*.tsbuildinfo

# Optional
.env
.env.local
```

## File: `SSDT-sqlproj.gitignore`
```
## Ignore Visual Studio SSDT sqlproj specific temporary files, build results, etc
##
##
## Get latest from https://github.com/github/gitignore/blob/master/SSDT-sqlproj.gitignore
# Build output
bin/
obj/

# DACPAC files
*.dacpac

# Publish profiles (optional, if environment-specific)
*.publish.xml

# SQL Server debug files
*.dbmdl
*.sqlcmdvars

# Visual Studio settings
.vs/

# User-specific files
*.user
*.suo
*.userosscache
*.sln.docstates

# Backup files
*.bak
*.log

```

## File: `Stella.gitignore`
```
# Atari 2600 (Stella) support for multiple assemblers
# - DASM
# - CC65

# Assembled binaries and object directories
obj/
a.out
*.bin
*.a26

# Add in special Atari 7800-based binaries for good measure
*.a78
```

## File: `SugarCRM.gitignore`
```
## SugarCRM
# Ignore custom .htaccess stuff.
/.htaccess
# Ignore the cache directory completely.
# This will break the current behaviour. Which was often leading to
# the misuse of the repository as backup replacement.
# For development the cache directory can be safely ignored and
# therefore it is ignored.
/cache/*
!/cache/index.html
# Ignore some files and directories from the custom directory.
/custom/history/
/custom/modulebuilder/
/custom/working/
/custom/modules/*/Ext/
/custom/application/Ext/
# Custom configuration should also be ignored.
/config.php
/config_override.php
# The silent upgrade scripts aren't needed.
/silentUpgrade*.php
# Logs files can safely be ignored.
*.log
# Ignore the new upload directories.
/upload/*
!/upload/index.html
/upload_backup/
```

## File: `Swift.gitignore`
```
# Xcode
#
# gitignore contributors: remember to update Global/Xcode.gitignore, Objective-C.gitignore & Swift.gitignore

## User settings
xcuserdata/

## Obj-C/Swift specific
*.hmap

## App packaging
*.ipa
*.dSYM.zip
*.dSYM

## Playgrounds
timeline.xctimeline
playground.xcworkspace

# Swift Package Manager
#
# Add this line if you want to avoid checking in source code from Swift Package Manager dependencies.
# Packages/
# Package.pins
# Package.resolved
# *.xcodeproj
#
# Xcode automatically generates this directory with a .xcworkspacedata file and xcuserdata
# hence it is not needed unless you have added a package configuration file to your project
# .swiftpm

.build/

# CocoaPods
#
# We recommend against adding the Pods directory to your .gitignore. However
# you should judge for yourself, the pros and cons are mentioned at:
# https://guides.cocoapods.org/using/using-cocoapods.html#should-i-check-the-pods-directory-into-source-control
#
# Pods/
#
# Add this line if you want to avoid checking in source code from the Xcode workspace
# *.xcworkspace

# Carthage
#
# Add this line if you want to avoid checking in source code from Carthage dependencies.
# Carthage/Checkouts

Carthage/Build/

# fastlane
#
# It is recommended to not store the screenshots in the git repo.
# Instead, use fastlane to re-generate the screenshots whenever they are needed.
# For more information about the recommended setup visit:
# https://docs.fastlane.tools/best-practices/source-control/#source-control

fastlane/report.xml
fastlane/Preview.html
fastlane/screenshots/**/*.png
fastlane/test_output
```

## File: `Symfony.gitignore`
```
# Cache and logs (Symfony2)
/app/cache/*
/app/logs/*
!app/cache/.gitkeep
!app/logs/.gitkeep

# Email spool folder
/app/spool/*

# Cache, session files and logs (Symfony3)
/var/cache/*
/var/logs/*
/var/sessions/*
!var/cache/.gitkeep
!var/logs/.gitkeep
!var/sessions/.gitkeep

# Logs (Symfony4)
/var/log/*
!var/log/.gitkeep

# Parameters
/app/config/parameters.yml
/app/config/parameters.ini

# Managed by Composer
/app/bootstrap.php.cache
/var/bootstrap.php.cache
/bin/*
!bin/console
!bin/symfony_requirements
/vendor/

# Assets and user uploads
/web/bundles/
/web/uploads/

# PHPUnit
/app/phpunit.xml
/phpunit.xml

# Build data
/build/

# Composer PHAR
/composer.phar

# Backup entities generated with doctrine:generate:entities command
**/Entity/*~

# Embedded web-server pid file
/.web-server-pid
```

## File: `SymphonyCMS.gitignore`
```
manifest/cache/
manifest/logs/
manifest/tmp/
symphony/
workspace/uploads/
install-log.txt
```

## File: `Terraform.gitignore`
```
# Local .terraform directories
.terraform/

# .tfstate files
*.tfstate
*.tfstate.*

# Crash log files
crash.log
crash.*.log

# Exclude all .tfvars files, which are likely to contain sensitive data, such as
# password, private keys, and other secrets. These should not be part of version
# control as they are data points which are potentially sensitive and subject
# to change depending on the environment.
*.tfvars
*.tfvars.json

# Ignore override files as they are usually used to override resources locally and so
# are not checked in
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# Ignore transient lock info files created by terraform apply
.terraform.tfstate.lock.info

# Include override files you do wish to add to version control using negated pattern
# !example_override.tf

# Include tfplan files to ignore the plan output of command: terraform plan -out=tfplan
# example: *tfplan*

# Ignore CLI configuration files
.terraformrc
terraform.rc

# Optional: ignore graph output files generated by `terraform graph`
# *.dot

# Optional: ignore plan files saved before destroying Terraform configuration
# Uncomment the line below if you want to ignore planout files.
# planout
```

## File: `TestComplete.gitignore`
```
# Test Complete ignore files: https://support.smartbear.com/viewarticle/68002/

# Tester-specific Settings
*.tcCFGExtender
*.tcLS

# Type library declarations
*.tlb

# Log files
*.tcLogs

# Backup files
*.bak
```

## File: `TeX.gitignore`
```
## Core latex/pdflatex auxiliary files:
*.aux
*.lof
*.log
*.lot
*.fls
*.out
*.toc
*.fmt
*.fot
*.cb
*.cb2
.*.lb

## Intermediate documents:
*.dvi
*.xdv
*-converted-to.*
# these rules might exclude image files for figures etc.
# *.ps
# *.eps
# *.pdf

## Generated if empty string is given at "Please type another file name for output:"
.pdf

## Bibliography auxiliary files (bibtex/biblatex/biber):
*.bbl
*.bbl-SAVE-ERROR
*.bcf
*.bcf-SAVE-ERROR
*.blg
*-blx.aux
*-blx.bib
*.run.xml

## Build tool auxiliary files:
*.fdb_latexmk
*.synctex
*.synctex(busy)
*.synctex.gz
*.synctex.gz(busy)
*.pdfsync
*.rubbercache
rubber.cache

## Build tool directories for auxiliary files
# latexrun
latex.out/

## Auxiliary and intermediate files from other packages:
# algorithms
*.alg
*.loa

# achemso
acs-*.bib

# amsthm
*.thm

# attachfile2
*.atfi

# beamer
*.nav
*.pre
*.snm
*.vrb

# changes
*.soc
*.loc

# comment
*.cut

# cprotect
*.cpt

# elsarticle (documentclass of Elsevier journals)
*.spl

# endnotes
*.ent

# fixme
*.lox

# feynmf/feynmp
*.mf
*.mp
*.t[1-9]
*.t[1-9][0-9]
*.tfm

#(r)(e)ledmac/(r)(e)ledpar
*.end
*.?end
*.[1-9]
*.[1-9][0-9]
*.[1-9][0-9][0-9]
*.[1-9]R
*.[1-9][0-9]R
*.[1-9][0-9][0-9]R
*.eledsec[1-9]
*.eledsec[1-9]R
*.eledsec[1-9][0-9]
*.eledsec[1-9][0-9]R
*.eledsec[1-9][0-9][0-9]
*.eledsec[1-9][0-9][0-9]R

# glossaries
*.acn
*.acr
*.glg
*.glg-abr
*.glo
*.glo-abr
*.gls
*.gls-abr
*.glsdefs
*.lzo
*.lzs
*.slg
*.slo
*.sls

# uncomment this for glossaries-extra (will ignore makeindex's style files!)
# *.ist

# gnuplot
*.gnuplot
*.table

# gnuplottex
*-gnuplottex-*

# gregoriotex
*.gaux
*.glog
*.gtex

# htlatex
*.4ct
*.4tc
*.idv
*.lg
*.trc
*.xref

# hypdoc
*.hd

# hyperref
*.brf

# knitr
*-concordance.tex
# TODO Uncomment the next line if you use knitr and want to ignore its generated tikz files
# *.tikz
*-tikzDictionary

# latexindent will create succesive backup files by default
#*.bak*

# listings
*.lol

# luatexja-ruby
*.ltjruby

# makeidx
*.idx
*.ilg
*.ind

# minitoc
*.maf
*.mlf
*.mlt
*.mtc[0-9]*
*.slf[0-9]*
*.slt[0-9]*
*.stc[0-9]*

# minted
_minted*
*.data.minted
*.pyg

# morewrites
*.mw

# newpax
*.newpax

# nomencl
*.nlg
*.nlo
*.nls

# pax
*.pax

# pdfpcnotes
*.pdfpc

# sagetex
*.sagetex.sage
*.sagetex.py
*.sagetex.scmd

# scrwfile
*.wrt

# spelling
*.spell.bad
*.spell.txt

# svg
svg-inkscape/

# sympy
*.sout
*.sympy
sympy-plots-for-*.tex/

# pdfcomment
*.upa
*.upb

# pythontex
*.pytxcode
pythontex-files-*/

# tcolorbox
*.listing

# thmtools
*.loe

# TikZ & PGF
*.dpth
*.md5
*.auxlock

# titletoc
*.ptc

# todonotes
*.tdo

# vhistory
*.hst
*.ver

# easy-todo
*.lod

# xcolor
*.xcp

# xmpincl
*.xmpi

# xindy
*.xdy

# xypic precompiled matrices and outlines
*.xyc
*.xyd

# endfloat
*.ttt
*.fff

# Latexian
TSWLatexianTemp*

## Editors:
# WinEdt
*.bak
*.sav

# latexindent.pl
*.bak[0-9]*

# Texpad
.texpadtmp

# LyX
*.lyx~

# Kile
*.backup

# gummi
.*.swp

# KBibTeX
*~[0-9]*

# TeXnicCenter
*.tps

# auto folder when using emacs and auctex
./auto/*
*.el

# expex forward references with \gathertags
*-tags.tex

# standalone packages
*.sta

# Makeindex log files
*.lpz

# xwatermark package
*.xwm

# REVTeX puts footnotes in the bibliography by default, unless the nofootinbib
# option is specified. Footnotes are the stored in a file with suffix Notes.bib.
# Uncomment the next line to have this generated file ignored.
#*Notes.bib
```

## File: `Textpattern.gitignore`
```
.htaccess
css.php
rpc/
sites/site*/admin/
sites/site*/private/
sites/site*/public/admin/
sites/site*/public/setup/
sites/site*/public/theme/
textpattern/
HISTORY.txt
README.txt
```

## File: `TurboGears2.gitignore`
```
*.py[co]

# Default development database
devdata.db

# Default data directory
data/*

# Packages
*.egg
*.egg-info
dist
build

# Installer logs
pip-log.txt

# Unit test / coverage reports
.coverage
.tox
```

## File: `TwinCAT3.gitignore`
```
### TwinCAT3 ###
# website: https://www.beckhoff.com/twincat3/

# TwinCAT PLC
*.plcproj.bak
*.plcproj.orig
*.tpy
*.tclrs
*.library
*.compiled-library
*.compileinfo
*.asm
*.core
LineIDs.dbg
LineIDs.dbg.bak

# TwinCAT C++ and shared types
# ignoring the TMC file is only useful for plain PLC programming
# as soon as shared data types (via tmc), C++ or in general TcCom-Module are used, the TMC file has to be part of the repository
*.tmc
*.tmcRefac

# TwinCAT project files
*.tsproj.bak
*.tsproj.b?k
*.tsproj.orig
*.tspproj.bak
*.xti.bak
*.xti.bk?
*.xti.orig
*.xtv
*.xtv.bak
*.xtv.bk?
*.xt?.bk?
*.xt?.orig

# Multiuser specific
**/.TcGit/

# exclude not required folders
**/_Boot/
**/_CompileInfo/
**/_Libraries/
**/_ModuleInstall/
**/_Deployment/
**/_Repository/


# To include a specific library directory (i.e. third party/custom libs),
# use pattern `!/**/_Libraries/<directory name>/` i.e. `!/**/_Libraries/www.tcunit.org/`
#

# VS Shell project specific files and folders
**/.vs/
*.~u
*.project.~u
*.suo
```

## File: `Typo3.gitignore`
```
## TYPO3 v6.2
# Ignore several upload and file directories.
/fileadmin/user_upload/
/fileadmin/_temp_/
/fileadmin/_processed_/
/uploads/
# Ignore cache
/typo3conf/temp_CACHED*
/typo3conf/temp_fieldInfo.php
/typo3conf/deprecation_*.log
/typo3conf/ENABLE_INSTALL_TOOL
/typo3conf/realurl_autoconf.php
/FIRST_INSTALL
# Ignore system folders, you should have them symlinked.
# If not comment out the following entries.
/typo3
/typo3_src
/typo3_src-*
/Packages
/.htaccess
/index.php
# Ignore temp directory.
/typo3temp/
```

## File: `Unity.gitignore`
```
# This .gitignore file should be placed at the root of your Unity project directory
#
# Get latest from https://github.com/github/gitignore/blob/main/Unity.gitignore
#
.utmp/
/[Ll]ibrary/
/[Tt]emp/
/[Oo]bj/
/[Bb]uild/
/[Bb]uilds/
/[Ll]ogs/
/[Uu]ser[Ss]ettings/
*.log

# By default unity supports Blender asset imports, *.blend1 blender files do not need to be commited to version control.
*.blend1
*.blend1.meta

# MemoryCaptures can get excessive in size.
# They also could contain extremely sensitive data
/[Mm]emoryCaptures/

# Recordings can get excessive in size
/[Rr]ecordings/

# Uncomment this line if you wish to ignore the asset store tools plugin
# /[Aa]ssets/AssetStoreTools*

# Autogenerated Jetbrains Rider plugin
/[Aa]ssets/Plugins/Editor/JetBrains*
# Jetbrains Rider personal-layer settings
*.DotSettings.user

# Visual Studio cache directory
.vs/

# Gradle cache directory
.gradle/

# Autogenerated VS/MD/Consulo solution and project files
ExportedObj/
.consulo/
*.csproj
*.unityproj
*.sln
*.suo
*.tmp
*.user
*.userprefs
*.pidb
*.booproj
*.svd
*.pdb
*.mdb
*.opendb
*.VC.db

# Unity3D generated meta files
*.pidb.meta
*.pdb.meta
*.mdb.meta

# Unity3D generated file on crash reports
sysinfo.txt

# Mono auto generated files
mono_crash.*

# Builds
*.apk
*.aab
*.unitypackage
*.unitypackage.meta
*.app

# Crashlytics generated file
crashlytics-build.properties

# TestRunner generated files
InitTestScene*.unity*

# Addressables default ignores, before user customizations
/ServerData
/[Aa]ssets/StreamingAssets/aa*
/[Aa]ssets/AddressableAssetsData/link.xml*
/[Aa]ssets/Addressables_Temp*
# By default, Addressables content builds will generate addressables_content_state.bin
# files in platform-specific subfolders, for example:
# /Assets/AddressableAssetsData/OSX/addressables_content_state.bin
/[Aa]ssets/AddressableAssetsData/*/*.bin*

# Visual Scripting auto-generated files
/[Aa]ssets/Unity.VisualScripting.Generated/VisualScripting.Flow/UnitOptions.db
/[Aa]ssets/Unity.VisualScripting.Generated/VisualScripting.Flow/UnitOptions.db.meta
/[Aa]ssets/Unity.VisualScripting.Generated/VisualScripting.Core/Property Providers
/[Aa]ssets/Unity.VisualScripting.Generated/VisualScripting.Core/Property Providers.meta

# Auto-generated scenes by play mode tests
/[Aa]ssets/[Ii]nit[Tt]est[Ss]cene*.unity*
```

## File: `UnrealEngine.gitignore`
```
# Visual Studio 2015 user specific files
.vs/

# Compiled Object files
*.slo
*.lo
*.o
*.obj

# Precompiled Headers
*.gch
*.pch

# Compiled Dynamic libraries
*.so
*.dylib
*.dll

# Fortran module files
*.mod

# Compiled Static libraries
*.lai
*.la
*.a
*.lib

# Executables
*.exe
*.out
*.app
*.ipa

# These project files can be generated by the engine
*.xcodeproj
*.xcworkspace
*.sln
*.suo
*.opensdf
*.sdf
*.VC.db
*.VC.opendb
.vsconfig

# Precompiled Assets
SourceArt/**/*.png
SourceArt/**/*.tga

# Binary Files
Binaries/*
Plugins/**/Binaries/*

# Builds
Build/*

# Whitelist PakBlacklist-<BuildConfiguration>.txt files
!Build/*/
Build/*/**
!Build/*/PakBlacklist*.txt

# Don't ignore icon files in Build
!Build/**/*.ico

# Built data for maps
*_BuiltData.uasset

# Configuration files generated by the Editor
Saved/*

# Compiled source files for the engine to use
Intermediate/*
Plugins/**/Intermediate/*

# Cache files for the editor to use
DerivedDataCache/*
```

## File: `VBA.gitignore`
```

# Office temporary files
~$*

# Access database lock files (laccdb, ldb)
*.[lL][aA][cC][cC][dD][bB]
*.[lL][dD][bB]

# The following sections constitute a list of Office file extensions that support VBA.
# If you want to exclude Office files from your repo, uncomment the corresponding file extensions.

# Excel (xls, xlsb, xlsm, xlt, xltm, xla, xlam)
#*.[xX][lL][sS]
#*.[xX][lL][sS][bB]
#*.[xX][lL][sS][mM]
#*.[xX][lL][tT]
#*.[xX][lL][tT][mM]
#*.[xX][lL][aA]
#*.[xX][lL][aA][mM]

# Word (doc, docm, dot, dotm)
#*.[dD][oO][cC]
#*.[dD][oO][cC][mM]
#*.[dD][oO][tT]
#*.[dD][oO][tT][mM]

# Access (accda, accdb, accde, mdb, mde)
#*.[aA][cC][cC][dD][aA]
#*.[aA][cC][cC][dD][bB]
#*.[aA][cC][cC][dD][eE]
#*.[mM][dD][bB]
#*.[mM][dD][eE]

# PowerPoint (ppt, pptm, pot, potm, pps, ppsm)
#*.[pP][pP][tT]
#*.[pP][pP][tT][mM]
#*.[pP][oO][tT]
#*.[pP][oO][tT][mM]
#*.[pP][pP][sS]
#*.[pP][pP][sS][mM]
```

## File: `VisualStudio.gitignore`
```
## Ignore Visual Studio temporary files, build results, and
## files generated by popular Visual Studio add-ons.
##
## Get latest from https://github.com/github/gitignore/blob/main/VisualStudio.gitignore

# User-specific files
*.rsuser
*.suo
*.user
*.userosscache
*.sln.docstates
*.env

# User-specific files (MonoDevelop/Xamarin Studio)
*.userprefs

# Mono auto generated files
mono_crash.*

# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/

[Dd]ebug/x64/
[Dd]ebugPublic/x64/
[Rr]elease/x64/
[Rr]eleases/x64/
bin/x64/
obj/x64/

[Dd]ebug/x86/
[Dd]ebugPublic/x86/
[Rr]elease/x86/
[Rr]eleases/x86/
bin/x86/
obj/x86/

[Ww][Ii][Nn]32/
[Aa][Rr][Mm]/
[Aa][Rr][Mm]64/
[Aa][Rr][Mm]64[Ee][Cc]/
bld/
[Oo]bj/
[Oo]ut/
[Ll]og/
[Ll]ogs/

# Build results on 'Bin' directories
**/[Bb]in/*
# Uncomment if you have tasks that rely on *.refresh files to move binaries
# (https://github.com/github/gitignore/pull/3736)
#!**/[Bb]in/*.refresh

# Visual Studio 2015/2017 cache/options directory
.vs/
# Uncomment if you have tasks that create the project's static files in wwwroot
#wwwroot/

# Visual Studio 2017 auto generated files
Generated\ Files/

# MSTest test Results
[Tt]est[Rr]esult*/
[Bb]uild[Ll]og.*
*.trx

# NUnit
*.VisualState.xml
TestResult.xml
nunit-*.xml

# Approval Tests result files
*.received.*

# Build Results of an ATL Project
[Dd]ebugPS/
[Rr]eleasePS/
dlldata.c

# Benchmark Results
BenchmarkDotNet.Artifacts/

# .NET Core
project.lock.json
project.fragment.lock.json
artifacts/

# ASP.NET Scaffolding
ScaffoldingReadMe.txt

# StyleCop
StyleCopReport.xml

# Files built by Visual Studio
*_i.c
*_p.c
*_h.h
*.ilk
*.meta
*.obj
*.idb
*.iobj
*.pch
*.pdb
*.ipdb
*.pgc
*.pgd
*.rsp
# but not Directory.Build.rsp, as it configures directory-level build defaults
!Directory.Build.rsp
*.sbr
*.tlb
*.tli
*.tlh
*.tmp
*.tmp_proj
*_wpftmp.csproj
*.log
*.tlog
*.vspscc
*.vssscc
.builds
*.pidb
*.svclog
*.scc

# Chutzpah Test files
_Chutzpah*

# Visual C++ cache files
ipch/
*.aps
*.ncb
*.opendb
*.opensdf
*.sdf
*.cachefile
*.VC.db
*.VC.VC.opendb

# Visual Studio profiler
*.psess
*.vsp
*.vspx
*.sap

# Visual Studio Trace Files
*.e2e

# TFS 2012 Local Workspace
$tf/

# Guidance Automation Toolkit
*.gpState

# ReSharper is a .NET coding add-in
_ReSharper*/
*.[Rr]e[Ss]harper
*.DotSettings.user

# TeamCity is a build add-in
_TeamCity*

# DotCover is a Code Coverage Tool
*.dotCover

# AxoCover is a Code Coverage Tool
.axoCover/*
!.axoCover/settings.json

# Coverlet is a free, cross platform Code Coverage Tool
coverage*.json
coverage*.xml
coverage*.info

# Visual Studio code coverage results
*.coverage
*.coveragexml

# NCrunch
_NCrunch_*
.NCrunch_*
.*crunch*.local.xml
nCrunchTemp_*

# MightyMoose
*.mm.*
AutoTest.Net/

# Web workbench (sass)
.sass-cache/

# Installshield output folder
[Ee]xpress/

# DocProject is a documentation generator add-in
DocProject/buildhelp/
DocProject/Help/*.HxT
DocProject/Help/*.HxC
DocProject/Help/*.hhc
DocProject/Help/*.hhk
DocProject/Help/*.hhp
DocProject/Help/Html2
DocProject/Help/html

# Click-Once directory
publish/

# Publish Web Output
*.[Pp]ublish.xml
*.azurePubxml
# Note: Comment the next line if you want to checkin your web deploy settings,
# but database connection strings (with potential passwords) will be unencrypted
*.pubxml
*.publishproj

# Microsoft Azure Web App publish settings. Comment the next line if you want to
# checkin your Azure Web App publish settings, but sensitive information contained
# in these scripts will be unencrypted
PublishScripts/

# NuGet Packages
*.nupkg
# NuGet Symbol Packages
*.snupkg
# The packages folder can be ignored because of Package Restore
**/[Pp]ackages/*
# except build/, which is used as an MSBuild target.
!**/[Pp]ackages/build/
# Uncomment if necessary however generally it will be regenerated when needed
#!**/[Pp]ackages/repositories.config
# NuGet v3's project.json files produces more ignorable files
*.nuget.props
*.nuget.targets

# Microsoft Azure Build Output
csx/
*.build.csdef

# Microsoft Azure Emulator
ecf/
rcf/

# Windows Store app package directories and files
AppPackages/
BundleArtifacts/
Package.StoreAssociation.xml
_pkginfo.txt
*.appx
*.appxbundle
*.appxupload

# Visual Studio cache files
# files ending in .cache can be ignored
*.[Cc]ache
# but keep track of directories ending in .cache
!?*.[Cc]ache/

# Others
ClientBin/
~$*
*~
*.dbmdl
*.dbproj.schemaview
*.jfm
*.pfx
*.publishsettings
orleans.codegen.cs

# Including strong name files can present a security risk
# (https://github.com/github/gitignore/pull/2483#issue-259490424)
#*.snk

# Since there are multiple workflows, uncomment next line to ignore bower_components
# (https://github.com/github/gitignore/pull/1529#issuecomment-104372622)
#bower_components/

# RIA/Silverlight projects
Generated_Code/

# Backup & report files from converting an old project file
# to a newer Visual Studio version. Backup files are not needed,
# because we have git ;-)
_UpgradeReport_Files/
Backup*/
UpgradeLog*.XML
UpgradeLog*.htm
ServiceFabricBackup/
*.rptproj.bak

# SQL Server files
*.mdf
*.ldf
*.ndf

# Business Intelligence projects
*.rdl.data
*.bim.layout
*.bim_*.settings
*.rptproj.rsuser
*- [Bb]ackup.rdl
*- [Bb]ackup ([0-9]).rdl
*- [Bb]ackup ([0-9][0-9]).rdl

# Microsoft Fakes
FakesAssemblies/

# GhostDoc plugin setting file
*.GhostDoc.xml

# Node.js Tools for Visual Studio
.ntvs_analysis.dat
node_modules/

# Visual Studio 6 build log
*.plg

# Visual Studio 6 workspace options file
*.opt

# Visual Studio 6 auto-generated workspace file (contains which files were open etc.)
*.vbw

# Visual Studio 6 workspace and project file (working project files containing files to include in project)
*.dsw
*.dsp

# Visual Studio 6 technical files
*.ncb
*.aps

# Visual Studio LightSwitch build output
**/*.HTMLClient/GeneratedArtifacts
**/*.DesktopClient/GeneratedArtifacts
**/*.DesktopClient/ModelManifest.xml
**/*.Server/GeneratedArtifacts
**/*.Server/ModelManifest.xml
_Pvt_Extensions

# Paket dependency manager
**/.paket/paket.exe
paket-files/

# FAKE - F# Make
**/.fake/

# CodeRush personal settings
**/.cr/personal

# Python Tools for Visual Studio (PTVS)
**/__pycache__/
*.pyc

# Cake - Uncomment if you are using it
#tools/**
#!tools/packages.config

# Tabs Studio
*.tss

# Telerik's JustMock configuration file
*.jmconfig

# BizTalk build output
*.btp.cs
*.btm.cs
*.odx.cs
*.xsd.cs

# OpenCover UI analysis results
OpenCover/

# Azure Stream Analytics local run output
ASALocalRun/

# MSBuild Binary and Structured Log
*.binlog
MSBuild_Logs/

# AWS SAM Build and Temporary Artifacts folder
.aws-sam

# NVidia Nsight GPU debugger configuration file
*.nvuser

# MFractors (Xamarin productivity tool) working folder
**/.mfractor/

# Local History for Visual Studio
**/.localhistory/

# Visual Studio History (VSHistory) files
.vshistory/

# BeatPulse healthcheck temp database
healthchecksdb

# Backup folder for Package Reference Convert tool in Visual Studio 2017
MigrationBackup/

# Ionide (cross platform F# VS Code tools) working folder
**/.ionide/

# Fody - auto-generated XML schema
FodyWeavers.xsd

# VS Code files for those working on multiple tools
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
!.vscode/*.code-snippets

# Local History for Visual Studio Code
.history/

# Built Visual Studio Code Extensions
*.vsix

# Windows Installer files from build outputs
*.cab
*.msi
*.msix
*.msm
*.msp
```

## File: `VVVV.gitignore`
```

# .v4p backup files
*~.xml

# Dynamic plugins .dll
bin/
```

## File: `Waf.gitignore`
```
# For projects that use the Waf build system: https://waf.io/
# Dot-hidden on Unix-like systems
.waf-*-*/
.waf3-*-*/
# Hidden directory on Windows (no dot)
waf-*-*/
waf3-*-*/
# Lockfile
.lock-waf_*_build
```

## File: `WordPress.gitignore`
```
# Wordpress - ignore core, configuration, examples, uploads and logs.
# https://github.com/github/gitignore/blob/main/WordPress.gitignore

# Core
#
# Note: if you want to stage/commit WP core files
# you can delete this whole section/until Configuration.
/wp-admin/
/wp-content/index.php
/wp-content/languages
/wp-content/plugins/index.php
/wp-content/themes/index.php
/wp-includes/
/index.php
/license.txt
/readme.html
/wp-*.php
/xmlrpc.php

# Configuration
wp-config.php

# Example themes
/wp-content/themes/twenty*/

# Example plugin
/wp-content/plugins/hello.php

# Uploads
/wp-content/uploads/

# Log files
*.log

# htaccess
/.htaccess

# All plugins
#
# Note: If you wish to whitelist plugins,
# uncomment the next line
#/wp-content/plugins

# All themes
#
# Note: If you wish to whitelist themes,
# uncomment the next line
#/wp-content/themes
```

## File: `Xojo.gitignore`
```
# Xojo (formerly REALbasic and Real Studio)

Builds*
*.debug
*.debug.app
Debug*.exe
Debug*/Debug*.exe
Debug*/Debug*\ Libs
*.rbuistate
*.xojo_uistate
*.obsolete*
```

## File: `Yeoman.gitignore`
```
node_modules/
bower_components/
*.log

build/
dist/
```

## File: `Yii.gitignore`
```
assets/*
!assets/.gitignore
protected/runtime/*
!protected/runtime/.gitignore
protected/data/*.db
themes/classic/views/
```

## File: `ZendFramework.gitignore`
```
# Composer files
composer.phar
vendor/

# Local configs
config/autoload/*.local.php

# Binary gettext files
*.mo

# Data
data/logs/
data/cache/
data/sessions/
data/tmp/
temp/

#Doctrine 2
data/DoctrineORMModule/Proxy/
data/DoctrineORMModule/cache/

# Legacy ZF1
demos/
extras/documentation
```

## File: `Zephir.gitignore`
```
# Cache files, generates by Zephir
.temp/
.libs/

# Object files, generates by linker
*.lo
*.la
*.o
*.loT

# Files generated by configure and Zephir,
# not required for extension compilation.
ext/build/
ext/modules/
ext/Makefile*
ext/config*
ext/acinclude.m4
ext/aclocal.m4
ext/autom4te*
ext/install-sh
ext/ltmain.sh
ext/missing
ext/mkinstalldirs
ext/run-tests.php
ext/.deps
ext/libtool
```

## File: `Zig.gitignore`
```
.zig-cache/
zig-out/
*.o
```

## File: `community/Alteryx.gitignore`
```
# gitignore template for Alteryx Designer
# website: https://www.alteryx.com/
# website: https://help.alteryx.com/current/designer/alteryx-file-types

# Alteryx Data Files
*.yxdb
*.cydb
*.cyidx
*.rptx
*.vvf
*.aws

# Alteryx Special Files
*.yxwv
*.yxft
*.yxbe
*.bak
*.pcxml
*.log
*.bin
*.yxlang
CASS.ini

# Alteryx License Files
*.yxlc
*.slc
*.cylc
*.alc
*.gzlc

## gitignore reference sites
# https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring
# https://git-scm.com/docs/gitignore
# https://help.github.com/articles/ignoring-files/

## Useful knowledge from stackoverflow
# Even if you haven't tracked the files so far, git seems to be able to "know" about them even after you add them to .gitignore.
# WARNING: First commit your current changes, or you will lose them.
# Then run the following commands from the top folder of your git repo:
# git rm -r --cached .
# git add .
# git commit -m "fixed untracked files"

# author: Kacper Ksieski
```

## File: `community/AltiumDesigner.gitignore`
```
# For PCBs designed using Altium Designer
# Website: https://www.altium.com/altium-designer/

# Directories containing cache data
History
__Previews

# Directories containing logs and generated outputs
Project\ Logs*
Project\ Outputs*

# Misc files generated by altium
debug.log
Status\ Report.txt
*.PcbDoc.htm
*.SchDocPreview
*.PcbDocPreview

# Lock files sometimes left behind
.~lock.*
```

## File: `community/AutoIt.gitignore`
```
# Compiled Scripts
*.a3x

# Tidy Auto-Generated Backups
Backup/*

# Au3Stripper Auto-Generated Files
*_stripped.au3
```

## File: `community/AutomationStudio.gitignore`
```
# gitignore template for B&R Automation Studio (AS) 4
# website: https://www.br-automation.com/en-us/products/software/automation-software/automation-studio/

# AS temporary directories
Binaries/
Diagnosis/
Temp/
TempObjects/

# AS transfer files
*artransfer.br
*arTrsfmode.nv

# 'ignored' directory
ignored/

# ARNC0ext
*arnc0ext.br

# AS File types
*.bak
*.isopen
*.orig
*.log
*.asar
*.csvlog*
*.set
!**/Physical/**/*.set

# RevInfo variables
*RevInfo.var
```

## File: `community/B4X.gitignore`
```
**/Objects
**/AutoBackups
*.meta
```

## File: `community/Bazel.gitignore`
```
# gitignore template for Bazel build system
# website: https://bazel.build/

# Ignore all bazel-* symlinks. There is no full list since this can change
# based on the name of the directory bazel is cloned into.
/bazel-*

# Directories for the Bazel IntelliJ plugin containing the generated
# IntelliJ project files and plugin configuration. Separate directories are
# for the IntelliJ, Android Studio and CLion versions of the plugin.
/.ijwb/
/.aswb/
/.clwb/
```

## File: `community/Beef.gitignore`
```
build/
recovery/
BeefSpace_User.toml
```

## File: `community/Dotter.gitignore`
```
# local files are for host-specific overrides
.dotter/local.toml

# ignore caches
.dotter/cache.toml
.dotter/cache
```

## File: `community/Exercism.gitignore`
```
# gitignore template for Exercism project
# website: https://exercism.io/

# Ignore .exercism folder which contain sensitive data
.exercism
```

## File: `community/Gretl.gitignore`
```
# gitignore template for Gretl
# website: http://gretl.sourceforge.net/

# Auto-generated log file is overwritten whenever you start a new session
session.inp

# Auto-generated temporary string code table
string_table.txt
```

## File: `community/Hexo.gitignore`
```
# gitignore template for Hexo sites
# website: https://hexo.io/
# Recommended: Node.gitignore

# Ignore generated directory
public/

# Ignore temp files
tmp/
.tmp*

# additional files
db.json
.deploy*/
```

## File: `community/LensStudio.gitignore`
```
# gitignore template for LensStudio
# website: https://lensstudio.snapchat.com/

# macOS/IDE #
.DS_Store
.idea

# js #
node_modules
yarn.lock

# Python #
__pycache__/
*.py[cod]
*$py.class
[Bb]ackup*
```

## File: `community/libogc.gitignore`
```
# Ignore build directories
build/

# Ignore Wii-specific metadata files
meta.xml
icon.png


# Ignore editor or IDE-specific files
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# Ignore backup or temporary files
*~
*.bak
*.swp
*.tmp

# Ignore log files
*.log

# Ignore libraries and dependencies
lib/
deps/
obj/

# Ignore operating system-specific files
$RECYCLE.BIN/
.Trash-1000/
.Spotlight-V100/
.fseventsd/
.DS_Store

# Prerequisites
*.d

# Object files
*.o
*.ko
*.obj
*.elf
*.o
*.bin

# Linker output
*.ilk
*.map
*.exp

# Precompiled Headers
*.gch
*.pch

# Libraries
*.lib
*.a
*.la
*.lo

# Shared objects (inc. Windows DLLs)
*.dll
*.so
*.so.*
*.dylib

# Executables
*.exe
*.out
*.app
*.i*86
*.x86_64
*.hex
*.dol
*.elf

# Debug files
*.dSYM/
*.su
*.idb
*.pdb

# Kernel Module Compile Results
*.mod*
*.cmd
.tmp_versions/
modules.order
Module.symvers
Mkfile.old
dkms.conf
```

## File: `community/Logtalk.gitignore`
```
# gitignore template for LogTalk, a programming language that builds upon Prolog
# website: https://logtalk.org/

# Logtalk temporary file directories
.lgt_tmp/
lgt_tmp/

# Logtalk default unit testing and doclet results and logs directories
logtalk_tester_logs/
logtalk_doclet_logs/

# backend Prolog compiler temporary files
.pl-history
*.out
*.xwam
*.qo
*.ql
*.itf
*.po
```

## File: `community/MetaTrader5.gitignore`
```
# MetaTrader 5 and MQL5 gitignore template
# Project homepage: https://www.metatrader5.com/en

# Compiled MQL5 executables (binaries)
# These are generated from .mq5 source files and should not be committed.
*.ex5
*.ex4 # For MQL4 compatibility if you also manage MT4 projects in a similar structure

# Log files
# Terminal logs, strategy tester logs, and custom logs from Print() functions.
*.log
*.slog # Strategy Tester logs

# Strategy Tester specific files
# History data, optimization results, and temporary files used by the tester.
*.fxt  # FXT files (history data for testing)
*.hst  # History data files (can be large)
*.ini  # Initialization files (often generated by tester or EAs)
*.dat  # Data files (various purposes, often temporary)
*.csv  # CSV export files (e.g., from tester reports)
*.jrn  # Journal files (tester journal)

# Market Watch sets and profiles
# User-specific lists of symbols in Market Watch, and terminal profiles.
*.set  # Market Watch symbol sets
*.tpl  # Chart templates
*.chr  # Chart settings files (can be generated when saving templates or profiles)

# External libraries (DLLs)
# If you use custom DLLs, you might want to ignore them if they are built separately
# and not part of your MQL5 source code repository.
*.dll

# User-specific configuration and credentials
# Files containing sensitive information or local user settings.
.env   # Environment variables (e.g., for Python integration credentials)
*.cfg  # Configuration files (if not meant to be shared)
*.json # Be careful: if you have config JSONs you *do* want to commit, add specific exceptions.
       # Example: !config.json (to include config.json but ignore other *.json)

# Temporary files and backup files generated by MetaEditor
*.~*   # Temporary files (e.g., ~MyScript.mq5)
*.bak  # Backup files (e.g., MyScript.mq5.bak)
*.mqh.bak
*.mq5.bak

# MetaEditor project files
# Project files for MetaEditor workspaces.
.mqproj

# Python specific ignores (if you also keep Python scripts or Jupyter notebooks in this repository)
# These are relevant if your Git repo root is higher up (e.g., the terminal folder itself)
# or if you mix Python code within your MQL5 structure.
__pycache__/       # Python compiled bytecode cache
.ipynb_checkpoints/ # Jupyter Notebook checkpoints
*.pyc              # Python compiled files
*.pyd              # Python dynamic modules
```

## File: `community/Move.gitignore`
```
# Generated by Move
# will have compiled files
build/

# Remove possibly saving credentials to the git repository
.aptos/
```

## File: `community/NasaSpecsIntact.gitignore`
```
# gitignore template for Nasa SpecsIntact (SI)
# Website: https://specsintact.ksc.nasa.gov/
#
# Recommended:
# MicrosoftOffice.gitignore
#

# SpecsIntact (SI) Locking file; this would lock everyone out.
*.se$

# SI Reports; auto-generated. They do not belong in the repository
# as they will be re-created exactly when using a specific checkout point.
*.RPT
ADDRVER.*
BRKTVER.*
DUPEREF.*
REFVER.*
SECTVER.*
SUBMVER.*
TTLDIFFS.*

# SpecsIntact files that change a lot and don't actually affect SI
# PULL.TBL is an auto-generated file to help speed SI loading.
PULL.TBL
pulltbl.bck

# Tailoring information.
# Keep tailor.tag; it is a list of tailoring options in SI.

# JOB.OTL informs SI where a spec section came from.
# Keeping the old one isn't useful in git.
JOB.OTL.OLD

# OneNote TOC Files; SI Work Directories may be installed in a location co-located with OneNote
# notebooks, and if so, OneNote will litter the SI folder with these.
*.onetoc*

# Log files, typically tagfix or other auto generated logs that aren't useful
# outside of the user that made them and clutter up the index.
*.log
```

## File: `community/OpenSSL.gitignore`
```
# OpenSSL-related files best not committed

## Certificate Authority
*.ca

## Certificate
*.crt

## Certificate Sign Request
*.csr

## Certificate
*.der

## Key database file
*.kdb

## OSCP request data
*.org

## PKCS #12
*.p12

## PEM-encoded certificate data
*.pem

## Random number seed
*.rnd

## SSLeay data
*.ssleay

## S/MIME message
*.smime
```

## File: `community/OpenTofu.gitignore`
```
# Local .terraform directories
**/.terraform/*

# .tfstate files
*.tfstate
*.tfstate.*

# Crash log files
crash.log
crash.*.log

# Exclude all .tfvars files, which are likely to contain sensitive data, such as
# password, private keys, and other secrets. These should not be part of version
# control as they are data points which are potentially sensitive and subject
# to change depending on the environment.
*.tfvars
*.tfvars.json

# Ignore override files as they are usually used to override resources locally and so
# are not checked in
override.tf
override.tofu
override.tf.json
override.tofu.json
*_override.tf
*_override.tofu
*_override.tf.json
*_override.tofu.json

# Ignore transient lock info files created by tofu apply
.terraform.tfstate.lock.info

# Include override files you do wish to add to version control using negated pattern
# !example_override.tf
# !example_override.tofu

# Include tfplan files to ignore the plan output of command: tofu plan -out=tfplan
# example: *tfplan*

# Ignore CLI configuration files
.terraformrc
terraform.rc
```

## File: `community/Puppet.gitignore`
```
# gitignore template for Puppet modules
# website: https://forge.puppet.com/

# Built packages
pkg/*

# Should run on multiple platforms so don't check in
Gemfile.lock

# Tests
spec/fixtures/*
coverage/*

# Third-party
vendor/*
.bundle/*
```

## File: `community/Racket.gitignore`
```
# gitignore template for the Racket language
# website: http://www.racket-lang.org/

# DrRacket autosave files
*.rkt~
*.rkt.bak
\#*.rkt#
\#*.rkt#*#

# Compiled racket bytecode
compiled/
*.zo

# Dependency tracking files
*.dep
```

## File: `community/Red.gitignore`
```
# gitignore template for Red programming language
# website: http://www.red-lang.org/

# Red Compiled code
*.red

# Libraries
crush.dll
crush.dylib
crush.so

# Files generated during test
quick-test/quick-test.log
quick-test/runnable/
system/tests/source/units/auto-tests/
tests/source/units/auto-tests/
```

## File: `community/ROS2.gitignore`
```
install/
log/
build/

# Ignore generated docs
*.dox
*.wikidoc

# eclipse stuff
.project
.cproject

# qcreator stuff
CMakeLists.txt.user

srv/_*.py
*.pcd
*.pyc
qtcreator-*
*.user

*~

# Emacs
.#*

# Colcon custom files
COLCON_IGNORE
AMENT_IGNORE
```

## File: `community/SPFx.gitignore`
```
#SharePoint Framework (SPFx)
# Logs
logs
*.log
npm-debug.log*

# Dependency directories
node_modules

# Build generated files
dist
lib
solution
temp
*.sppkg

# Coverage directory used by tools like istanbul
coverage

# OSX
.DS_Store

# Visual Studio files
.ntvs_analysis.dat
.vs
bin
obj

# Resx Generated Code
*.resx.ts

# Styles Generated Code
*.scss.ts
```

## File: `community/Splunk.gitignore`
```
# gitignore template for Splunk apps
# documentation: http://docs.splunk.com/Documentation/Splunk/6.2.3/admin/Defaultmetaconf

# Splunk local meta file
local.meta

# Splunk local folder
local
```

## File: `community/Strapi.gitignore`
```
############################
# OS X
############################

.DS_Store
.AppleDouble
.LSOverride
Icon
.Spotlight-V100
.Trashes
._*


############################
# Linux
############################

*~


############################
# Windows
############################

Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/
*.cab
*.msi
*.msm
*.msp


############################
# Packages
############################

*.7z
*.csv
*.dat
*.dmg
*.gz
*.iso
*.jar
*.rar
*.tar
*.zip
*.com
*.class
*.dll
*.exe
*.o
*.seed
*.so
*.swo
*.swp
*.swn
*.swm
*.out
*.pid


############################
# Logs and databases
############################

.tmp
*.log
*.sql
*.sqlite


############################
# Misc.
############################

*#
.idea
nbproject
.vscode/


############################
# Node.js
############################

lib-cov
lcov.info
pids
logs
results
build
node_modules
.node_history
package-lock.json
**/package-lock.json
!docs/package-lock.json
*.heapsnapshot


############################
# Tests
############################

testApp
coverage
cypress/screenshots
cypress/videos


############################
# Documentation
############################

dist

############################
# Builds
############################

packages/strapi-generate-new/files/public/

############################
# Example app
############################

.dev
# *.cache

############################
# Visual Studio Code
############################

front-workspace.code-workspace
```

## File: `community/Terragrunt.gitignore`
```
# Ignore the default terragrunt cache directory
# https://terragrunt.gruntwork.io/docs/features/caching/
.terragrunt-cache
```

## File: `community/Toit.gitignore`
```
.packages
*_pb.toit
```

## File: `community/UiPath.gitignore`
```
# gitignore template for RPA development using UiPath Studio
# website: https://www.uipath.com/product/studio
#
# Recommended: n/a

# Ignore folders that could cause issues if accidentally tracked
**/.local/**
**/.settings/**
**/.objects/**
**/.tmh/**
**/*.log
```

## File: `community/UTAU.gitignore`
```
# Adobe Audition
*.pkf

# UTAU Engines
*.ctspec
*.d4c
*.dio
*.frc
*.frt
*.frq
*.harvest
*.lessaudio
*.llsm
*.mrq
*.pitchtier
*.platinum
*.pmk
*.sc.npz
*.star
*.uspec
*.vs4ufrq

# UTAU related tools
$read
*.setParam-Scache
*.lbp
*.lbp.caches/*

# OpenUtau
errors.txt

# Deepvocal
*.DVModel
*-log.txt
SKC
SKI
SKC_1
SKC_2
*.sksd

# VocalSharp
*.scep
*.vssf
*.vsdx
*.vsdxindex

# Binary Archive
*.7z
*.zip
*.rar
*.exe

```

## File: `community/V.gitignore`
```
*.exe
*.o
*.so
*.tmp.c
*.exp
*.ilk
*.pdb
*.dll
*.lib
*.bak
*.out
```

## File: `community/Xilinx.gitignore`
```
# gitignore template for Xilinx Vivado Design Suite
# website: https://www.xilinx.com/support/download.html

# [home]
*.jou
*.log
*.debug
*.str
*.zip
*.tmp
*.rst
*.os
*.js
*.pb
*.dcp
*.hwdef
*.vds
*.veo
*.wdf
*.vdi
*.dmp
*.rpx
*.rpt
*_stub.v
*_stub.vhdl
*_funcsim.v
*_funcsim.vhdl
.project

# [dir]
*.cache
.metadata
*.data
*.ipdefs
.Xil
*.sdk
*.hw
*.ip_user_files

### IP synth
*_synth_*

.jobs

### project synth
*/*.runs/synth*/*.xml
*/*.runs/synth*/*.txt
*/*.runs/synth*/*.sh
*/*.runs/synth*/*.tcl
*/*.runs/synth*/*.bat
*/*.runs/synth*/*.xdc
!*/*.runs/synth*/*utilization*.rpt

*.runs/synth*/*.xml
*.runs/synth*/*.txt
*.runs/synth*/*.sh
*.runs/synth*/*.tcl
*.runs/synth*/*.bat
*.runs/synth*/*.xdc
!*.runs/synth*/*utilization*.rpt

### project impl
*/*.runs/impl*/*.xml
*/*.runs/impl*/*.html
*/*.runs/impl*/*.txt
*/*.runs/impl*/*.sh
*/*.runs/impl*/*.tcl
*/*.runs/impl*/*.bat
!*/*.runs/impl*/*utilization*.rpt

*.runs/impl*/*.xml
*.runs/impl*/*.html
*.runs/impl*/*.txt
*.runs/impl*/*.sh
*.runs/impl*/*.tcl
*.runs/impl*/*.bat
!*.runs/impl*/*utilization*.rpt

### block design
*/*/bd/*/hdl
*/*/*/bd/*/hdl

*/*/bd/*/*.xdc
*/*/*/bd/*/*.xdc

*/*/bd/*/ip/*/*.xdc
*/*/*/bd/*/ip/*/*.xdc

*/*/bd/*/ip/*/*/
*/*/*/bd/*/ip/*/*/

*/*/bd/*/ip/*/*.vhd
*/*/*/bd/*/ip/*/*.vhd

*/*/bd/*/ip/*/*.xml
*/*/*/bd/*/ip/*/*.xml

*.c
*.h
*.vho
*.html
*/*/bd/*/ip/*/*.tcl
*/*/*/bd/*/ip/*/*.tcl
hw_handoff
ipshared
```

## File: `community/AWS/CDK.gitignore`
```
# CDK asset staging directory.
# For more information about AWS-CDK, see  https://docs.aws.amazon.com/cdk/
.cdk.staging/
cdk.out/
```

## File: `community/AWS/SAM.gitignore`
```
# gitignore template for AWS Serverless Application Model project
# website: https://docs.aws.amazon.com/serverless-application-model

# Ignore build folder
.aws-sam/
```

## File: `community/BoxLang/ColdBox.gitignore`
```
# Servelet Ignores
WEB-INF

# Engines + Database + CBFS + Secrets
.tmp/**
.env
.engine/**
.cbfs/**

# Logs + Test Results
logs/**
tests/results/**

## Ignored Dependencies
/boxlang_modules/*
effective-pom.xml
/coldbox/**
/testbox/**
/modules/**
/lib/java/**

# NPM JS Assets (If applicable)
**/node_modules/*
npm-debug.log
yarn-error.log
```

## File: `community/CFML/ColdBox.gitignore`
```
# Servelet Ignores
WEB-INF

# Engines + Database + CBFS + Secrets
.tmp/**
.env
.engine/**
.cbfs/**

# Logs + Test Results
logs/**
tests/results/**

## Ignored Dependencies
effective-pom.xml
/coldbox/**
/testbox/**
/modules/**
/lib/java/**

# NPM JS Assets (If applicable)
**/node_modules/*
npm-debug.log
yarn-error.log
```

## File: `community/DotNet/core.gitignore`
```
*.swp
*.*~
project.lock.json
.DS_Store
*.pyc
nupkg/

# Visual Studio Code
.vscode

# Rider
.idea

# User-specific files
*.suo
*.user
*.userosscache
*.sln.docstates

# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
build/
bld/
[Bb]in/
[Oo]bj/
[Oo]ut/
msbuild.log
msbuild.err
msbuild.wrn

# Visual Studio 2015
.vs/

```

## File: `community/DotNet/InforCMS.gitignore`
```
# gitignore template for InforCRM (formerly SalesLogix)
# website: https://www.infor.com/product-summary/cx/infor-crm/
#
# Recommended: VisualStudio.gitignore

# Ignore model files that are auto-generated
ModelIndex.xml
ExportedFiles.xml

# Ignore deployment files
[Mm]odel/[Dd]eployment

# Force include portal SupportFiles
!Model/Portal/*/SupportFiles/[Bb]in/
!Model/Portal/PortalTemplates/*/SupportFiles/[Bb]in
```

## File: `community/DotNet/Kentico.gitignore`
```
# gitignore template for using Kentico CMS
# website: http://www.kentico.com/
#
# Recommended template: VisualStudio.gitignore

# Include some Kentico folders excluded by Visual Studio rules
!CMS/CMSAdminControls/*/
!CMS/CMSModules/System/*/
!CMS/App_Data/CIRepository/**

# Kentico temporary/environment files
CMS/App_Data/AzureCache
CMS/App_Data/AzureTemp
CMS/App_Data/CMSModules/DeviceProfile/logFiftyOne.txt
CMS/App_Data/CMSModules/DeviceProfiles/logFiftyOne.txt
CMS/App_Data/CMSModules/WebFarm/webfarm.sync
CMS/App_Data/CMSTemp
CMS/App_Data/Persistent
CMS/CMSSiteUtils/Export
CMS/CMSSiteUtils/Import

# Ignore all smart search indexes, but not the other system folder contents
CMS/App_Data/CMSModules/SmartSearch/**
!CMS/App_Data/CMSModules/SmartSearch/*/
!CMS/App_Data/CMSModules/SmartSearch/_StopWords/**
!CMS/App_Data/CMSModules/SmartSearch/_Synonyms/**

## Kentico Starter Sites
# Starter site resource Files
CMS/App_Data/DancingGoat

# Starter site web templates
CMS/App_Data/Templates/CommunitySite
CMS/App_Data/Templates/CorporateSite
CMS/App_Data/Templates/DancingGoat
CMS/App_Data/Templates/EcommerceSite
CMS/App_Data/Templates/IntranetPortal
CMS/App_Data/Templates/PersonalSite

# Starter site app themes
CMS/App_Themes/CommunitySite
CMS/App_Themes/CorporateSite
CMS/App_Themes/EcommerceSite
CMS/App_Themes/IntranetPortal*
CMS/App_Themes/PersonalSite

# Starter site ASPX templates
CMS/CMSTemplates/CorporateSite

# Starter site media libraries
CMS/CommunitySite
CMS/CorporateSite
CMS/DancingGoat
CMS/EcommerceSite
CMS/IntranetPortal
CMS/PersonalSite

## Project specific ignores
# Sensitive settings
AppSettings.config
ConnectionStrings.config

# Project media libraries (recommend shared file storage)
# e.g. CMS/{SiteCodeName}
```

## File: `community/DotNet/Umbraco.gitignore`
```
## Ignore Umbraco files/folders generated for each instance
##
## Get latest from https://github.com/github/gitignore/blob/main/Umbraco.gitignore

# Note: VisualStudio gitignore rules may also be relevant

# Umbraco
# Ignore unimportant folders generated by Umbraco
**/App_Data/Logs/
**/App_Data/[Pp]review/
**/App_Data/TEMP/
**/App_Data/NuGetBackup/

# Ignore Umbraco content cache file
**/App_Data/umbraco.config

## this [Uu]mbraco/ folder should be created by cmd like `Install-Package UmbracoCms -Version 8.5.3`
## you can find your Umbraco version in your Web.config. (i.e. <add key="Umbraco.Core.ConfigurationStatus" value="8.5.3" />)
## Uncomment this line if you think it fits the way you work on your project.
## **/[Uu]mbraco/

## The [Mm]edia/ folder contains content. Content may vary by environment and should therefore not be added to source control.
## Uncomment this line if you think it fits the way you work on your project.
## **/[Mm]edia/

# Don't ignore Umbraco packages (VisualStudio.gitignore mistakes this for a NuGet packages folder)
# Make sure to include details from VisualStudio.gitignore BEFORE this
!**/App_Data/[Pp]ackages/*
!**/[Uu]mbraco/[Dd]eveloper/[Pp]ackages/*
!**/[Uu]mbraco/[Vv]iews/[Pp]ackages/*

# ImageProcessor DiskCache
**/App_Data/cache/

# Ignore the Models Builder models out of date flag
**/ood.flag

# NEW for version 9 .Net 5 (Core)
#ignore umbraco backoffice assest from wwwroot
**/wwwroot/umbraco/

# SQLite files
*.sqlite.db*

#ignore umbraco data/views/settings
**/umbraco/*

#include default location for modelsbuilder output
!**/umbraco/models

#include default location for packages
!**/umbraco/Data/packages
```

## File: `community/Elixir/Phoenix.gitignore`
```
# gitignore template for Phoenix projects
# website: http://www.phoenixframework.org/
#
# Recommended template: Elixir.gitignore

# Temporary files
/tmp

# Static artifacts
/node_modules
/assets/node_modules

# Since we are building assets from web/static,
# we ignore priv/static. You may want to comment
# this depending on your deployment strategy.
/priv/static/

# Installer-related files
/installer/_build
/installer/tmp
/installer/doc
/installer/deps
```

## File: `community/embedded/AtmelStudio.gitignore`
```
## Ignore Atmel Studio temporary files and build results
# https://www.microchip.com/mplab/avr-support/atmel-studio-7

# Atmel Studio is powered by an older version of Visual Studio,
# so most of the project and solution files are the same as VS files,
# only prefixed by an `at`.

#Build Directories
[Dd]ebug/
[Rr]elease/

#Build Results
*.o
*.d
*.eep
*.elf
*.hex
*.map
*.srec

#User Specific Files
*.atsuo
```

## File: `community/embedded/esp-idf.gitignore`
```
# gitignore template for esp-idf, the official development framework for ESP32
# https://github.com/espressif/esp-idf

build/
sdkconfig
sdkconfig.old
```

## File: `community/embedded/IAR_EWARM.gitignore`
```
# gitignore template for the IAR EWARM
# website: https://www.iar.com/knowledge/support/technical-notes/ide/which-files-should-be-version-controlled/

# Some tools will put the EWARM files
# under a subdirectory with the same name
# as the configuration.
# Example
# EWARM/Config1/Obj /List /Exe
# EWARM/Config2/Obj /List /Exe
EWARM/**/Obj
EWARM/**/List
EWARM/**/Exe

# Autogenerated project files
*.dep
*.ewt

# Autogenerated folder for debugger
EWARM/settings
```

## File: `community/embedded/uVision.gitignore`
```
# git ignore file for Keil µVision Project

# µVision 5 and µVision 4 Project screen layout file
*.uvguix.*
*.uvgui.*

# Listing Files
*.i
*.lst
*.m51
*.m66
*.map

# Object Files
*.axf
*.b[0-2][0-9]
*.b3[0-1]
*.bak
*.build_log.htm
*.crf
*.d
*.dep
*.elf
*.htm
*.iex
*.lnp
*.o
*.obj
*.sbr

# Firmware Files
*.bin
*.h86
*.hex

# Build Files
.bat

# Debugger Files
.ini

# JLink Files
JLinkLog.txt

# Other Files
```

## File: `community/GNOME/GNOMEShellExtension.gitignore`
```
# Ignored files for GNOME extension git repository

*.zip
```

## File: `community/Golang/Go.AllowList.gitignore`
```
# Allowlisting gitignore template for GO projects prevents us
# from adding various unwanted local files, such as generated
# files, developer configurations or IDE-specific files etc.
#
# Recommended: Go.AllowList.gitignore

# Ignore everything
*

# But not these files...
!/.gitignore

!*.go
!go.sum
!go.mod

!README.md
!LICENSE

# !Makefile

# ...even if they are in subdirectories
!*/
```

## File: `community/Golang/Hugo.gitignore`
```
# Generated files by hugo
/public/
/resources/_gen/
/assets/jsconfig.json
hugo_stats.json

# Executable may be added to repository
hugo.exe
hugo.darwin
hugo.linux

# Temporary lock file while building
/.hugo_build.lock
```

## File: `community/Java/JBoss4.gitignore`
```
# gitignore for JBoss v4 projects

/server/all/data
/server/all/log
/server/all/tmp
/server/all/work
/server/default/data
/server/default/log
/server/default/tmp
/server/default/work
/server/minimal/data
/server/minimal/log
/server/minimal/tmp
/server/minimal/work

# Note:
# there may be other directories that contain *.xml.failed or *.war.failed files
/server/default/deploy/*.xml.failed
/server/default/deploy/*.war.failed
```

## File: `community/Java/JBoss6.gitignore`
```
# gitignore for JBoss v6 projects
#
# Note: to ensure empty directories remain part of the repository, like
# `/server/minimal/lib`, you should add an empty `.gitignore` or `.gitkeep` file
# to the directory - otherwise you may have issues when starting the service.

/server/all/data
/server/all/log
/server/all/tmp
/server/all/work
/server/default/data
/server/default/log
/server/default/tmp
/server/default/work
/server/minimal/data
/server/minimal/log
/server/minimal/tmp
/server/minimal/work
/server/jbossweb-standalone/data
/server/jbossweb-standalone/log
/server/jbossweb-standalone/tmp
/server/jbossweb-standalone/work
/server/standard/data
/server/standard/log
/server/standard/tmp
/server/standard/work
/server/default/deploy/*.jar.failed
/server/default/deploy/*.jar.dodeploy
/server/default/deploy/*.xml.failed
/server/default/deploy/*.xml.dodeploy
/server/default/deploy/*.war.failed
/server/default/deploy/*.war.dodeploy

```

## File: `community/JavaScript/Cordova.gitignore`
```
# gitignore template for the Cordova framework
# website: https://cordova.apache.org/
#
# Recommended template: Node.gitignore

# App platform binaries and built files
/platforms

# Optional to ignore plugin Git clones
#/plugins
```

## File: `community/JavaScript/Expo.gitignore`
```
# .gitignore template for Expo
# website: https://expo.dev/
# docs: https://docs.expo.dev/workflow/expo-cli/
#
# Rationale:
# node_modules/ is always ignored
# .expo/, .expo-shared/ are Expo’s local state and project-settings cache (see docs)
#  Metro caches/logs are *.expo, *.tunnel, *.cache, *.tmp, *.log

# Node modules
node_modules/

# Expo local state and caches
.expo/             # runtime state (Metro bundler, dev-client data, tunnels)
.expo-shared/      # shared project settings (app.json edits, etc.)

# Metro bundler caches/logs
*.expo             # generic Expo temp files
*.tunnel           # Expo DevTools tunnels
*.cache            # Metro cache folder
*.tmp              # temp files created during bundling
*.log              # build or Metro logs

# Environment variables
.env
.env.local
.env.*.local

# Package manager logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

## File: `community/JavaScript/Meteor.gitignore`
```
# gitignore template for the Meteor framework
# website: https://www.meteor.com/
#
# Recommended template: Node.gitignore

# protect api keys in setting json
settings-production.json
settings.json

# protect your mup.json settings
mup.json
mup.js
```

## File: `community/JavaScript/NWjs.gitignore`
```
# gitignore template for NW.js projects
# website: https://nwjs.io/

# Seen in standard and sdk versions
credits.html
locales/
libEGL.dll
libGLEv2.dll
node.dll
nw.dll
nw.exe
natives_blob.bin
nw_100_percent.pak
nw_200_percent.pak
nw_elf.dll
snapshot_blob.bin
resources.pak

# Seen only in standard
d3dcompiler_47.dll
ffmpeg.dll
icudtl.dat

# Seen only in sdk
pnacl/
chromedriver.exe
nacl_irt_x86_64.nexe
nwjc.exe
payload.exe
```

## File: `community/JavaScript/Vue.gitignore`
```
# gitignore template for Vue.js projects
#
# Recommended template: Node.gitignore

# TODO: where does this rule come from?
docs/_book

# TODO: where does this rule come from?
test/
```

## File: `community/Linux/Snap.gitignore`
```
# gitginore template for creating Snap packages
# website: https://snapcraft.io/

parts/
prime/
stage/
*.snap

# Snapcraft global state tracking data(automatically generated)
# https://forum.snapcraft.io/t/location-to-save-global-state/768
/snap/.snapcraft/

# Source archive packed by `snapcraft cleanbuild` before pushing to the LXD container
/*_source.tar.bz2
```

## File: `community/Obsidian/NotesAndCoreConfiguration.gitignore`
```
# Excludes Obsidian workspace cache and plugins. All notes and core obsidian
# configuration files are tracked by Git.

# The current application UI state (DOM layout, recently-opened files, etc.) is
# stored in these files (separate for desktop and mobile) so you can resume
# your session seamlessly after a restart. If you want to track UI state, use
# the Workspaces core plugin instead of relying on these files.
.obsidian/workspace.json
.obsidian/workspace-mobile.json

# Obsidian plugins are stored under .obsidian/plugins/$plugin_name. They
# contain metadata (manifest.json), application code (main.js), stylesheets
# (styles.css), and user-configuration data (data.json).
# We want to exclude all plugin-related files, so we can exclude everything
# under this directory.
.obsidian/plugins/**/*
```

## File: `community/Obsidian/NotesAndExtendedConfiguration.gitignore`
```
# Excludes Obsidian workspace cache and plugin code, but retains plugin
# configuration. All notes and user-controlled configuration files are tracked
# by Git.
#
# 				!!! WARNING !!!
#
# Community plugins may store sensitive secrets in their data.json files. By
# including these files, those secrets may be tracked in your Git repository.
#
# To ignore configurations for specific plugins, add a line like this after the
# contents of this file (order is important):
#     .obsidian/plugins/{{plugin_name}}/data.json
#
# Alternatively, ensure that you are treating your entire Git repository as
# sensitive data, since it may contain secrets, or may have contained them in
# past commits.  Understand your threat profile, and make the decision
# appropriate for yourself. If in doubt, err on the side of not including
# plugin configuration. Use one of the alternative gitignore files instead:
# * NotesOnly.gitignore
# * NotesAndCoreConfiguration.gitignore

# The current application UI state (DOM layout, recently-opened files, etc.) is
# stored in these files (separate for desktop and mobile) so you can resume
# your session seamlessly after a restart. If you want to track UI state, use
# the Workspaces core plugin instead of relying on these files.
.obsidian/workspace.json
.obsidian/workspace-mobile.json

# Obsidian plugins are stored under .obsidian/plugins/$plugin_name. They
# contain metadata (manifest.json), application code (main.js), stylesheets
# (styles.css), and user-configuration data (data.json).
# We only want to track data.json, so we:
# 1. exclude everything that the plugin folders contain,
# 2. unignore data.json in the plugin folders
.obsidian/plugins/*/**
!.obsidian/plugins/*/data.json
```

## File: `community/Obsidian/NotesOnly.gitignore`
```
# Excludes all Obsidian-related configuration. All notes are tracked by Git.

# All Obsidian configuration and runtime state is stored here
.obsidian/**/*
```

## File: `community/PHP/Bitrix.gitignore`
```
# gitignore template for 1C-Bitrix, a PHP-based CMS
# website: https://www.1c-bitrix.ru

#Exclude all of core files
/bitrix/*

#But not the templates and non bitrix components
!/bitrix/templates
!/bitrix/components
/bitrix/components/bitrix

#Exclude bitrix gadgets
!/bitrix/gadgets
/bitrix/gadgets/bitrix

#User can use that directory to store some stuff, but it's not really recommended, just use /local instead of this
!/bitrix/php_interface/

#Exclude database configs
/bitrix/php_interface/dbconn.php

#Exclude default file storage directory
/upload/
```

## File: `community/PHP/CodeSniffer.gitignore`
```
# gitignore for the PHP Codesniffer framework
# website: https://github.com/squizlabs/PHP_CodeSniffer
#
# Recommended template: PHP.gitignore

/wpcs/*
```

## File: `community/PHP/Drupal7.gitignore`
```
# gitignore template for Drupal 7 projects
#
# It is recommended that you use `Drupal.gitignore` as this is the latest version

# Ignore configuration files that may contain sensitive information.
sites/*/*settings*.php
sites/example.sites.php

# Ignore paths that contain generated content.
files/
sites/*/files
sites/*/private
sites/*/translations

# Ignore default text files
robots.txt
/CHANGELOG.txt
/COPYRIGHT.txt
/INSTALL*.txt
/LICENSE.txt
/MAINTAINERS.txt
/UPGRADE.txt
/README.txt
sites/README.txt
sites/all/libraries/README.txt
sites/all/modules/README.txt
sites/all/themes/README.txt

# Ignore everything but the "sites" folder ( for non core developer )
.htaccess
web.config
authorize.php
cron.php
index.php
install.php
update.php
xmlrpc.php
/includes
/misc
/modules
/profiles
/scripts
/themes
```

## File: `community/PHP/Jigsaw.gitignore`
```
# gitignore template for Jigsaw Static Site Generator
#
# website - https://jigsaw.tighten.co

# Ignore build folder
build_*
```

## File: `community/PHP/Magento1.gitignore`
```
# gitignore template for Magento v1 projects
#
# It is recommended that you use `Magento.gitignore` as this is the latest version

/PATCH_*.sh

/app/etc/local.xml

/media/*
!/media/.htaccess

!/media/customer
/media/customer/*
!/media/customer/.htaccess

!/media/dhl
/media/dhl/*
!/media/dhl/logo.jpg

!/media/downloadable
/media/downloadable/*
!/media/downloadable/.htaccess

!/media/xmlconnect
/media/xmlconnect/*

!/media/xmlconnect/custom
/media/xmlconnect/custom/*
!/media/xmlconnect/custom/ok.gif

!/media/xmlconnect/original
/media/xmlconnect/original/*
!/media/xmlconnect/original/ok.gif

!/media/xmlconnect/system
/media/xmlconnect/system/*
!/media/xmlconnect/system/ok.gif

/var/*
!/var/.htaccess

!/var/package
/var/package/*
!/var/package/*.xml

```

## File: `community/PHP/Magento2.gitignore`
```
/sitemap
/sitemap.xml
/pub/sitemap
/pub/sitemap.xml
/app/config_sandbox
/app/etc/config.php
/app/etc/env.php
/app/code/Magento/TestModule*
/lib/internal/flex/uploader/.actionScriptProperties
/lib/internal/flex/uploader/.flexProperties
/lib/internal/flex/uploader/.project
/lib/internal/flex/uploader/.settings
/lib/internal/flex/varien/.actionScriptProperties
/lib/internal/flex/varien/.flexLibProperties
/lib/internal/flex/varien/.project
/lib/internal/flex/varien/.settings
/.grunt
/.php_cs.cache
/grunt-config.json
/dev/tools/grunt/configs/local-themes.js

/pub/media/*.*
!/pub/media/.htaccess
/pub/media/attribute/*
!/pub/media/attribute/.htaccess
/pub/media/analytics/*
/pub/media/catalog/*
!/pub/media/catalog/.htaccess
/pub/media/customer/*
!/pub/media/customer/.htaccess
/pub/media/downloadable/*
!/pub/media/downloadable/.htaccess
/pub/media/favicon/*
/pub/media/import/*
!/pub/media/import/.htaccess
/pub/media/logo/*
/pub/media/theme/*
/pub/media/theme_customization/*
!/pub/media/theme_customization/.htaccess
/pub/media/wysiwyg/*
!/pub/media/wysiwyg/.htaccess
/pub/media/tmp/*
!/pub/media/tmp/.htaccess
/pub/media/captcha/*
!/pub/media/captcha/.htaccess
/pub/static/*
!/pub/static/.htaccess

/var/*
!/var/.htaccess
/vendor/*
!/vendor/.htaccess
/generated/*
!/generated/.htaccess
```

## File: `community/PHP/Pimcore.gitignore`
```
# gitignore template for Pimcore CMS

# pimcore source files
/pimcore

# asset files
/website/var/assets/*

# backups
/website/var/backup/*

# file cache
/website/var/cache/*

# generated PHP classes, keep definition files (.psf)
/website/var/classes/Object*
!/website/var/classes/objectbricks

# various configuration files
/website/var/config/system.xml
/website/var/config/cache.xml
/website/var/config/robots.txt
/website/var/config/Geo*
/website/var/config/object/*
/website/var/config/portal/*
/website/var/config/sqlreport/*

# sent e-mail log files
/website/var/email/*

# log files
/website/var/log/*.log

# serialized recyclebin files
/website/var/recyclebin/*

# search plugin
/website/var/search/*

# various temp files
/website/var/system/*
/website/var/tmp/*

# serialized version files
/website/var/versions/asset/*
/website/var/versions/document/*
/website/var/versions/object/*

# user profile images
/website/var/user-image/*

# keep .dummy files
!.dummy
```

## File: `community/PHP/ThinkPHP.gitignore`
```
# gitignore template for ThinkPHP v3.2.3
# website: http://www.thinkphp.cn/

# Logs and Cache files
/Application/Runtime/

# Common configure file
/Application/Common/Conf/config.php
```

## File: `community/Python/JupyterNotebooks.gitignore`
```
# gitignore template for Jupyter Notebooks
# website: http://jupyter.org/

.ipynb_checkpoints
*/.ipynb_checkpoints/*

# IPython
profile_default/
ipython_config.py

# Jupyter lab virtual documents
# https://jupyterlab-lsp.readthedocs.io/en/2.x/Configuring.html#virtual_documents_dir
.virtual_documents/

# Remove previous ipynb_checkpoints
#   git rm -r .ipynb_checkpoints/
```

## File: `community/Python/Nikola.gitignore`
```
# gitignore template for Nikola static site generator
# website: https://getnikola.com/

.doit.db
*.py[cod]
cache/
output/
```

## File: `Global/AL.gitignore`
```
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
*.code-workspace

# Local History for Visual Studio Code
.history/
*.app
.snapshots/*
```

## File: `Global/Anjuta.gitignore`
```
# Local configuration folder and symbol database
/.anjuta/
/.anjuta_sym_db.db
```

## File: `Global/Ansible.gitignore`
```
*.retry
.ansible/
```

## File: `Global/Archives.gitignore`
```
# It's better to unpack these files and commit the raw source because
# git has its own built in compression methods.
*.7z
*.jar
*.rar
*.zip
*.gz
*.gzip
*.tgz
*.bzip
*.bzip2
*.bz2
*.xz
*.lzma
*.cab
*.xar
*.zst
*.tzst

# Packing-only formats
*.iso
*.tar

# Package management formats
*.dmg
*.xpi
*.gem
*.egg
*.deb
*.rpm
*.msi
*.msm
*.msp
*.txz
```

## File: `Global/Backup.gitignore`
```
*.bak
*.gho
*.ori
*.orig
*.tmp
```

## File: `Global/Bazaar.gitignore`
```
.bzr/
.bzrignore
```

## File: `Global/BricxCC.gitignore`
```
# Bricx Command Center IDE
# http://bricxcc.sourceforge.net
*.bak
*.sym
```

## File: `Global/Calabash.gitignore`
```
# Calabash / Cucumber
rerun/
reports/
screenshots/
screenshot*.png
test-servers/

# bundler
.bundle
vendor
```

## File: `Global/Cloud9.gitignore`
```
# Cloud9 IDE - http://c9.io
.c9revisions
.c9
```

## File: `Global/CodeKit.gitignore`
```
# General CodeKit files to ignore
config.codekit
config.codekit3
/min
```

## File: `Global/Cursor.gitignore`
```
.cursorignore
.cursorindexingignore
```

## File: `Global/CVS.gitignore`
```
/CVS/*
**/CVS/*
.cvsignore
*/.cvsignore
```

## File: `Global/DartEditor.gitignore`
```
.project
.buildlog
```

## File: `Global/Diff.gitignore`
```
*.patch
*.diff
```

## File: `Global/Dreamweaver.gitignore`
```
# DW Dreamweaver added files
_notes
_compareTemp
configs/
dwsync.xml
dw_php_codehinting.config
*.mno
```

## File: `Global/Dropbox.gitignore`
```
# Dropbox settings and caches
.dropbox
.dropbox.attr
.dropbox.cache
```

## File: `Global/Eclipse.gitignore`
```
.metadata
bin/
tmp/
*.tmp
*.bak
*.swp
*~.nib
local.properties
.settings/
.loadpath
.recommenders

# External tool builders
.externalToolBuilders/

# Locally stored "Eclipse launch configurations"
*.launch

# PyDev specific (Python IDE for Eclipse)
*.pydevproject

# CDT-specific (C/C++ Development Tooling)
.cproject

# CDT- autotools
.autotools

# Java annotation processor (APT)
.factorypath

# PDT-specific (PHP Development Tools)
.buildpath

# sbteclipse plugin
.target

# Tern plugin
.tern-project

# TeXlipse plugin
.texlipse

# STS (Spring Tool Suite)
.springBeans

# Code Recommenders
.recommenders/

# Annotation Processing
.apt_generated/
.apt_generated_tests/

# Scala IDE specific (Scala & Java development for Eclipse)
.cache-main
.scala_dependencies
.worksheet

# Uncomment this line if you wish to ignore the project description file.
# Typically, this file would be tracked if it contains build/dependency configurations:
#.project
```

## File: `Global/EiffelStudio.gitignore`
```
# The compilation directory
EIFGENs
```

## File: `Global/Emacs.gitignore`
```
# -*- mode: gitignore; -*-
*~
\#*\#
/.emacs.desktop
/.emacs.desktop.lock
*.elc
auto-save-list
tramp
.\#*

# Org-mode
.org-id-locations
*_archive

# flymake-mode
*_flymake.*

# eshell files
/eshell/history
/eshell/lastdir

# elpa packages
/elpa/

# reftex files
*.rel

# AUCTeX auto folder
/auto/

# cask packages
.cask/
dist/

# Flycheck
flycheck_*.el

# server auth directory
/server/

# projectiles files
.projectile

# directory configuration
.dir-locals.el

# network security
/network-security.data

# undo-tree
*.~undo-tree~
```

## File: `Global/Ensime.gitignore`
```
# Ensime specific
.ensime
.ensime_cache/
.ensime_lucene/
```

## File: `Global/Espresso.gitignore`
```
*.esproj
```

## File: `Global/FlexBuilder.gitignore`
```
bin/
bin-debug/
bin-release/
```

## File: `Global/GPG.gitignore`
```
secring.*

```

## File: `Global/Images.gitignore`
```
# JPEG
*.jpg
*.jpeg
*.jpe
*.jif
*.jfif
*.jfi

# JPEG 2000
*.jp2
*.j2k
*.jpf
*.jpx
*.jpm
*.mj2

# JPEG XR
*.jxr
*.hdp
*.wdp

# Graphics Interchange Format
*.gif

# RAW
*.raw

# Web P
*.webp

# Portable Network Graphics
*.png

# Animated Portable Network Graphics
*.apng

# Multiple-image Network Graphics
*.mng

# Tagged Image File Format
*.tiff
*.tif

# Scalable Vector Graphics
*.svg
*.svgz

# Portable Document Format
*.pdf

# X BitMap
*.xbm

# BMP
*.bmp
*.dib

# ICO
*.ico

# 3D Images
*.3dm
*.max
```

## File: `Global/JDeveloper.gitignore`
```
# default application storage directory used by the IDE Performance Cache feature
.data/

# used for ADF styles caching
temp/

# default output directories
classes/
deploy/
javadoc/

# lock file, a part of Oracle Credential Store Framework
cwallet.sso.lck
```

## File: `Global/JEnv.gitignore`
```
# JEnv local Java version configuration file
.java-version

# Used by previous versions of JEnv
.jenv-version
```

## File: `Global/JetBrains.gitignore`
```
# Covers JetBrains IDEs: IntelliJ, GoLand, RubyMine, PhpStorm, AppCode, PyCharm, CLion, Android Studio, WebStorm and Rider
# Reference: https://intellij-support.jetbrains.com/hc/en-us/articles/206544839

# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# Gradle and Maven with auto-import
# When using Gradle or Maven with auto-import, you should exclude module files,
# since they will be recreated, and may cause churn.  Uncomment if using
# auto-import.
# .idea/artifacts
# .idea/compiler.xml
# .idea/jarRepositories.xml
# .idea/modules.xml
# .idea/*.iml
# .idea/modules
# *.iml
# *.ipr

# CMake
cmake-build-*/

# Mongo Explorer plugin
.idea/**/mongoSettings.xml

# File-based project format
*.iws

# IntelliJ
out/

# mpeltonen/sbt-idea plugin
.idea_modules/

# JIRA plugin
atlassian-ide-plugin.xml

# Cursive Clojure plugin
.idea/replstate.xml

# SonarLint plugin
.idea/sonarlint/
.idea/sonarlint.xml # see https://community.sonarsource.com/t/is-the-file-idea-idea-idea-sonarlint-xml-intended-to-be-under-source-control/121119

# Crashlytics plugin (for Android Studio and IntelliJ)
com_crashlytics_export_strings.xml
crashlytics.properties
crashlytics-build.properties
fabric.properties

# Editor-based HTTP Client
.idea/httpRequests
http-client.private.env.json

# Android studio 3.1+ serialized cache file
.idea/caches/build_file_checksums.ser

# Apifox Helper cache
.idea/.cache/.Apifox_Helper
.idea/ApifoxUploaderProjectSetting.xml

# Github Copilot persisted session migrations, see: https://github.com/microsoft/copilot-intellij-feedback/issues/712#issuecomment-3322062215
.idea/**/copilot.data.migration.*.xml
```

## File: `Global/Kate.gitignore`
```
# Swap Files #
.*.kate-swp
.swp.*
```

## File: `Global/KDevelop4.gitignore`
```
*.kdev4
.kdev4/
```

## File: `Global/Lazarus.gitignore`
```
# Lazarus compiler-generated binaries (safe to delete)
*.exe
*.dll
*.so
*.dylib
*.lrs
*.res
*.compiled
*.dbg
*.ppu
*.o
*.or
*.a

# Lazarus autogenerated files (duplicated info)
*.rst
*.rsj
*.lrt

# Lazarus local files (user-specific info)
*.lps

# Lazarus backups and unit output folders.
# These can be changed by user in Lazarus/project options.
backup/
*.bak
lib/

# Application bundle for Mac OS
*.app/
```

## File: `Global/Lefthook.gitignore`
```
# https://lefthook.dev/configuration/#config-file-name
/.lefthook-local.json
/.lefthook-local.toml
/.lefthook-local.yaml
/.lefthook-local.yml
/lefthook-local.json
/lefthook-local.toml
/lefthook-local.yaml
/lefthook-local.yml
/.config/lefthook-local.json
/.config/lefthook-local.toml
/.config/lefthook-local.yaml
/.config/lefthook-local.yml

# https://lefthook.dev/configuration/source_dir_local.html
/.lefthook-local/
```

## File: `Global/LibreOffice.gitignore`
```
# LibreOffice locks
.~lock.*#
```

## File: `Global/Linux.gitignore`
```
*~

# temporary files which can be created if a process still has a handle open of a deleted file
.fuse_hidden*

# Metadata left by Dolphin file manager, which comes with KDE Plasma
.directory

# Linux trash folder which might appear on any partition or disk
.Trash-*

# .nfs files are created when an open file is removed but is still being accessed
.nfs*

# Log files created by default by the nohup command
nohup.out
```

## File: `Global/LyX.gitignore`
```
# Ignore LyX backup and autosave files
# http://www.lyx.org/
*.lyx~
*.lyx#
```

## File: `Global/macOS.gitignore`
```
# General
.DS_Store
__MACOSX/
.AppleDouble
.LSOverride
Icon[
]

# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk
```

## File: `Global/MATLAB.gitignore`
```
# Autosave files
*.asv
*.m~
*.autosave
*.slx.r*
*.mdl.r*

# Derived content-obscured files
*.p

# Compiled MEX files
*.mex*

# Packaged app and toolbox files
*.mlappinstall
*.mltbx

# Deployable archives
*.ctf

# Generated helpsearch folders
helpsearch*/

# Code generation folders
slprj/
sccprj/
codegen/

# Cache files
*.slxc

# Cloud based storage dotfile
.MATLABDriveTag
```

## File: `Global/Mercurial.gitignore`
```
.hg/
.hgignore
.hgsigs
.hgsub
.hgsubstate
.hgtags
```

## File: `Global/Metals.gitignore`
```
# Metals (Scala Language Server)
# Reference: https://scalameta.org/metals/docs/editors/vscode#files-and-directories-to-include-in-your-gitignore
.metals/
.bloop/
.ammonite/
metals.sbt
```

## File: `Global/MicrosoftOffice.gitignore`
```
*.tmp

# Word temporary
~$*.doc*
~$*.dot*

# Word Auto Backup File
Backup of *.doc*

# Excel temporary
~$*.xls*

# Excel Backup File
*.xlk

# PowerPoint temporary
~$*.ppt*

# Visio autosave temporary files
*.~vsd*
```

## File: `Global/mise.gitignore`
```
# https://mise.jdx.dev/configuration.html
# https://mise.jdx.dev/configuration/environments.html
.mise.*.local.toml
.mise.local.toml
mise.*.local.toml
mise.local.toml
.mise/*.local.toml
mise/*.local.toml

# https://mise.jdx.dev/configuration.html#tool-versions
#.tool-versions
```

## File: `Global/Momentics.gitignore`
```
# Built files
x86/
arm/
arm-p/
translations/*.qm

# IDE settings
.settings/
```

## File: `Global/MonoDevelop.gitignore`
```
#User Specific
*.userprefs
*.usertasks

#Mono Project Files
*.pidb
*.resources
test-results/
```

## File: `Global/NetBeans.gitignore`
```
**/nbproject/private/
**/nbproject/Makefile-*.mk
**/nbproject/Package-*.bash
build/
nbbuild/
dist/
nbdist/
.nb-gradle/
```

## File: `Global/Ninja.gitignore`
```
.ninja_deps
.ninja_log
```

## File: `Global/NotepadPP.gitignore`
```
# Notepad++ backups #
*.bak
```

## File: `Global/Octave.gitignore`
```
# Autosave files
*.asv
*.m~
*.autosave
*.slx.r*
*.mdl.r*

# Derived content-obscured files
*.p

# Compiled MEX files
*.mex*

# Packaged app and toolbox files
*.mlappinstall
*.mltbx

# Deployable archives
*.ctf

# Generated helpsearch folders
helpsearch*/

# Code generation folders
slprj/
sccprj/
codegen/

# Cache files
*.slxc

# Cloud based storage dotfile
.MATLABDriveTag
```

## File: `Global/Otto.gitignore`
```
.otto/
```

## File: `Global/Patch.gitignore`
```
*.orig
*.rej
```

## File: `Global/PlatformIO.gitignore`
```
.pio
.pioenvs
.piolibdeps
.vscode/.browse.c_cpp.db*
.vscode/c_cpp_properties.json
.vscode/launch.json
```

## File: `Global/PSoCCreator.gitignore`
```
# Project Settings
*.cywrk.*
*.cyprj.*

# Generated Assets and Resources
Debug/
Release/
Export/
*/codegentemp
*/Generated_Source
*_datasheet.pdf
*_timing.html
*.cycdx
*.cyfit
*.rpt
*.svd
*.log
*.zip
```

## File: `Global/PuTTY.gitignore`
```
# Private key
*.ppk
```

## File: `Global/README.md`
```markdown
## Globally Useful gitignores

This directory contains globally useful gitignores,
e.g. OS-specific and editor specific.

For more on global gitignores:
<https://help.github.com/en/github/using-git/ignoring-files#configuring-ignored-files-for-all-repositories-on-your-computer>

And a good blog post about 'em:
<http://augustl.com/blog/2009/global_gitignores>
```

## File: `Global/Redcar.gitignore`
```
.redcar
```

## File: `Global/Redis.gitignore`
```
# Ignore redis binary dump (dump.rdb) files

*.rdb
```

## File: `Global/SBT.gitignore`
```
# Simple Build Tool
# http://www.scala-sbt.org/release/docs/Getting-Started/Directories.html#configuring-version-control

dist/*
target/
lib_managed/
src_managed/
project/boot/
project/plugins/project/
.history
.cache
.lib/
.bsp/
```

## File: `Global/SlickEdit.gitignore`
```
# SlickEdit workspace and project files are ignored by default because
# typically they are considered to be developer-specific and not part of a
# project.
*.vpw
*.vpj

# SlickEdit workspace history and tag files always contain user-specific
# data so they should not be stored in a repository.
*.vpwhistu
*.vpwhist
*.vtg
```

## File: `Global/Stata.gitignore`
```
# .gitignore file for git projects containing Stata files
# Commercial statistical software: http://www.stata.com

# Stata dataset and output files
*.dta
*.gph
*.log
*.smcl
*.stpr
*.stsem
~*.stswp

# Graphic export files from Stata
# Stata command graph export: http://www.stata.com/manuals14/g-2graphexport.pdf
#
# You may add graphic export files to your .gitignore. However you should be
# aware that this will exclude all image files from this main directory
# and subdirectories.
# *.ps
# *.eps
# *.wmf
# *.emf
# *.pdf
# *.png
# *.tif
```

## File: `Global/STM32CubeIDE.gitignore`
```
# STM32CubeIDE specific files

# Project-specific settings. Ignore it if developers have different preferences.
# However, if you want all team members to use the same code formatting and settings, 
# consider including the .settings folder in the repository.

# /.settings/

# Ignore Eclipse-based IDE launch configurations.
# Uncomment if you want each developer to have their own unique debug configurations.
#*.launch

# Ignore any JLink-related files (debug configurations).
# Uncomment if you want each developer to have their own unique debug configurations.
#*.jlink

# Ignore log files generated by the IDE.
# These are not necessary for version control.
*.log

# Build files

# Ignore build output directories.
# These are not needed in the repository as they are generated during the build process.
Debug/
Release/

# Ignore common binary and object files generated during compilation.
# They should not be included in the repository as they are build artifacts.
*.elf
*.map
*.bin
*.hex
*.srec
*.lst
*.o
*.d
*.a
*.su
*.crl

#TouchGFX files (in case your project has touchGFX)
TouchGFX/generated
TouchGFX/build
TouchGFX/simulator/msvs/.vs

# Backup files

# Ignore temporary and backup files generated by the operating system and editor.
# These are not needed in the repository.
*.bak
```

## File: `Global/SublimeText.gitignore`
```
# Cache files for Sublime Text
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache

# Workspace files are user-specific
*.sublime-workspace

# Project files should be checked into the repository, unless a significant
# proportion of contributors will probably not be using Sublime Text
# *.sublime-project

# SFTP configuration file
sftp-config.json
sftp-config-alt*.json

# Package control specific files
Package Control.last-run
Package Control.ca-list
Package Control.ca-bundle
Package Control.system-ca-bundle
Package Control.cache/
Package Control.ca-certs/
Package Control.merged-ca-bundle
Package Control.user-ca-bundle
oscrypto-ca-bundle.crt
bh_unicode_properties.cache

# Sublime-github package stores a github token in this file
# https://packagecontrol.io/packages/sublime-github
GitHub.sublime-settings
```

## File: `Global/SVN.gitignore`
```
.svn/
```

## File: `Global/Syncthing.gitignore`
```
# Syncthing caches
.stversions
```

## File: `Global/SynopsysVCS.gitignore`
```
# Waveform formats
*.vcd
*.vpd
*.evcd
*.fsdb

# Default name of the simulation executable.  A different name can be
# specified with this switch (the associated daidir database name is
# also taken from here):  -o <path>/<filename>
simv

# Generated for Verilog and VHDL top configs
simv.daidir/
simv.db.dir/

# Infrastructure necessary to co-simulate SystemC models with
# Verilog/VHDL models.  An alternate directory may be specified with this
# switch:  -Mdir=<directory_path>
csrc/

# Log file - the following switch allows to specify the file that will be
# used to write all messages from simulation:  -l <filename>
*.log

# Coverage results (generated with urg) and database location.  The
# following switch can also be used:  urg -dir <coverage_directory>.vdb
simv.vdb/
urgReport/

# DVE and UCLI related files.
DVEfiles/
ucli.key

# When the design is elaborated for DirectC, the following file is created
# with declarations for C/C++ functions.
vc_hdrs.h
```

## File: `Global/Tags.gitignore`
```
# Ignore tags created by etags, ctags, gtags (GNU global) and cscope
TAGS
.TAGS
!TAGS/
tags
.tags
!tags/
gtags.files
GTAGS
GRTAGS
GPATH
GSYMS
cscope.files
cscope.out
cscope.in.out
cscope.po.out

```

## File: `Global/TextMate.gitignore`
```
*.tmproj
*.tmproject
tmtags
```

## File: `Global/TortoiseGit.gitignore`
```
# Project-level settings
/.tgitconfig
```

## File: `Global/Vagrant.gitignore`
```
# General
.vagrant/

# Log files (if you are creating logs in debug mode, uncomment this)
# *.log
```

## File: `Global/Vim.gitignore`
```
# Swap
[._]*.s[a-v][a-z]
# comment out the next line if you don't need vector files
!*.svg
[._]*.sw[a-p]
[._]s[a-rt-v][a-z]
[._]ss[a-gi-z]
[._]sw[a-p]

# Session
Session.vim
Sessionx.vim

# Temporary
.netrwhist
*~
# Auto-generated tag files
tags
# Persistent undo
[._]*.un~
```

## File: `Global/VirtualEnv.gitignore`
```
# Virtualenv
# https://realpython.com/python-virtual-environments-a-primer/#the-virtualenv-project
.Python
[Bb]in
[Ii]nclude
[Ll]ib
[Ll]ib64
[Ll]ocal
[Ss]cripts
pyvenv.cfg
.venv
pip-selfcheck.json
```

## File: `Global/Virtuoso.gitignore`
```
# Gitignore for Cadence Virtuoso
################################################################

# Log files
*.log
panic*.log.*

# OpenAccess database lock files
*.cdslck*

# Run directories for layout vs. schematic and design rule check
lvsRunDir/*
drcRunDir/*

# Abstract generation tool
abstract.log*
abstract.record*

```

## File: `Global/VisualStudioCode.gitignore`
```
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
!.vscode/*.code-snippets
!*.code-workspace

# Built Visual Studio Code Extensions
*.vsix
```

## File: `Global/WebMethods.gitignore`
```
**/IntegrationServer/datastore/
**/IntegrationServer/db/
**/IntegrationServer/DocumentStore/
**/IntegrationServer/lib/
**/IntegrationServer/logs/
**/IntegrationServer/replicate/
**/IntegrationServer/sdk/
**/IntegrationServer/support/
**/IntegrationServer/update/
**/IntegrationServer/userFtpRoot/
**/IntegrationServer/web/
**/IntegrationServer/WmRepository4/
**/IntegrationServer/XAStore/
**/IntegrationServer/packages/Wm*/
```

## File: `Global/Windows.gitignore`
```
# Windows thumbnail cache files
Thumbs.db
Thumbs.db:encryptable
ehthumbs.db
ehthumbs_vista.db

# Dump file
*.stackdump

# Folder config file
[Dd]esktop.ini

# Recycle Bin used on file shares
$RECYCLE.BIN/

# Windows Installer files
*.cab
*.msi
*.msix
*.msm
*.msp

# Windows shortcuts
*.lnk
```

## File: `Global/Xcode.gitignore`
```
## User settings
xcuserdata/
```

## File: `Global/XilinxISE.gitignore`
```
# intermediate build files
*.bgn
*.bit
*.bld
*.cmd_log
*.drc
*.ll
*.lso
*.msd
*.msk
*.ncd
*.ngc
*.ngd
*.ngr
*.pad
*.par
*.pcf
*.prj
*.ptwx
*.rbb
*.rbd
*.stx
*.syr
*.twr
*.twx
*.unroutes
*.ut
*.xpi
*.xst
*_bitgen.xwbt
*_envsettings.html
*_map.map
*_map.mrp
*_map.ngm
*_map.xrpt
*_ngdbuild.xrpt
*_pad.csv
*_pad.txt
*_par.xrpt
*_summary.html
*_summary.xml
*_usage.xml
*_xst.xrpt

# iMPACT generated files
_impactbatch.log
impact.xsl
impact_impact.xwbt
ise_impact.cmd
webtalk_impact.xml

# Core Generator generated files
xaw2verilog.log

# project-wide generated files
*.gise
par_usage_statistics.html
usage_statistics_webtalk.html
webtalk.log
webtalk_pn.xml

# generated folders
iseconfig/
xlnx_auto_0_xdb/
xst/
_ngo/
_xmsgs/
```

