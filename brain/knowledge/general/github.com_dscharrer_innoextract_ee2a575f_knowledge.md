---
id: github.com-dscharrer-innoextract-ee2a575f-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.294600
---

# KNOWLEDGE EXTRACT: github.com_dscharrer_innoextract_ee2a575f
> **Extracted on:** 2026-04-01 11:37:23
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521398/github.com_dscharrer_innoextract_ee2a575f

---

## File: `.mailmap`
```
#
# This list is used by git-shortlog to fix a few botched name translations
# in the git archive, either because the author's full name was messed up
# and/or not always written the same way, making contributions from the
# same person appearing not to be so.
#

Daniel Scharrer <daniel@constexpr.org> <dscharrer@gmail.com>
```

## File: `.travis.yml`
```yaml
language: cpp
matrix:
  include:
    - os: linux
      sudo: required
      compiler: gcc
    - os: osx
      compiler: clang
addons:
  apt:
    packages:
      - build-essential
      - cmake
      - libboost-all-dev
      - liblzma-dev
before_install:
  - if [ "$TRAVIS_OS_NAME" = osx ] ; then brew update ; fi
  - if [ "$TRAVIS_OS_NAME" = osx ] ; then brew unlink python@2 ; fi
  - if [ "$TRAVIS_OS_NAME" = osx ] ; then brew upgrade cmake boost ; fi
  - if [ "$TRAVIS_OS_NAME" = osx ] ; then brew install xz ; fi
script:
  - mkdir build
  - cd build
  - cmake --version
  - cmake .. -Werror=dev -Werror=deprecated -DCONTINUOUS_INTEGRATION=1
  - make -j1
branches:
  only:
    - master
notifications:
  email:
    recipients:
      - daniel@constexpr.org
    on_success: change
    on_failure: always
```

## File: `CHANGELOG`
```

innoextract 1.10 (TBD)
 - Added support for Inno Setup 6.3.x installers
 - Added support for Inno Setup 6.4.0 installers
 - Added support for a modified Inno Setup 5.3.10 variant
 - Added unit tests, enable with BUILD_TESTS
 - Replaced USE_ARC4 build option with BUILD_DECRYPTION
 - Linking will be done using Mold or LLD if available

innoextract 1.9 (2020-08-09)
 - Added preliminary support for Inno Setup 6.1.0
 - Added support for a modified Inno Setup 5.4.2 variant
 - Fixed output directory being created for unsupported installers
 - Fixed some safe non-ASCII characters being stripped from filenames
 - Fixed handling of path separators in Japanese and Korean installers
 - Fixed build with newer Boost versions
 - Windows: Fixed heap corruption
 - Windows: Fixed garbled output

innoextract 1.8 (2019-09-15)
 - Added support for Inno Setup 6.0.0 installers
 - Added support for pre-release Inno Setup 5.6.2 installers used by GOG
 - Added support for two modified Inno Setup 5.5.7 variants
 - Added support for Inno Setup 1.3.0 to 1.3.23
 - Added support for My Inno Setup Extensions installers older than 3.0.6.1
 - Added support for modified Inno Setup variants using an alternative setup loader magic
 - Added support for using boost_{zlib,bzip2} when statically linking Boost
 - Added support for automatically reading external setup.0 files
 - Encoding for non-Unicode installers is now determined from the languages supported by the installer, overridable using the --codepage option
 - Implemented parsing of GOG Galaxy architecture constraints
 - The architecture-specific suffixes @32bit and @64bit are now used to disambiguate colliding files
 - Fixed extracting files from slices larger than 2 GiB with 32-bit builds
 - Fixed output path for files with absolute paths (canonicalization now strips all unsafe characters)
 - Fixed output directory being created even when not extracting files
 - Fixed a hang when using the --language option
 - Improved checksum verification for files reconstructed from GOG Galaxy file parts
 - Changed header parsing to select the first version without warnings and failing that the first without errors
 - Changed filesystem and output encoding to WTF-8 (extended UTF-8) to represent broken UTF-16 data

innoextract 1.7 (2018-06-12)
 - Added support for Inno Setup 5.6.0 installers
 - Added support for new GOG installers with GOG Galaxy file parts
 - Added support for encrypted installers with the --password (-P) and --password-file options
 - Added a --show-password option to print password check information
 - Added a --check-password option to abort if the provided password does not match the stored checksum
 - Added a --info (-i) convenience option to print information about the installer
 - Added a --list-sizes option to print file sizes even with --quiet or --silent
 - Added a --list-checksums option to print file checksums
 - Added a --data-version (-V) option to print the data version and exit
 - Added a --no-extract-unknown (-n) option to abort on unknown Inno Setup data versions
 - Fixed building in paths that contain regex expressions
 - Fixed case-sensitivity in parent directory when creating subdirectories
 - Fixed .bin slice file names used with Inno Setup versions older than 4.1.7
 - Fixed build with newer libc++ versions
 - Made loading of .bin slice files case-insensitive
 - The --test option can now be combined with --extract to abort on file checksum errors
 - Now compiles in C++17 mode if supported

innoextract 1.6 (2016-03-24)
 - Added support for Inno Setup 5.5.7 (and 5.5.8) installers
 - Added a --collisions=rename-all option
 - Changed --collisions=rename to omit the suffix for the file that would have been extracted with --collisions=overwrite instead of the first encountered file
 - Fixed @lang suffix sometimes missing for the first file with the --collisions=rename option
 - Fixed build error with CMake 3.5
 - Now compiles in C++14 mode if supported
 - Unsafe characters in special constant strings (ie ':' in {code:…}) are now replaced with '$'
 - Windows: Fixed error message if the source file could not be opened
 - Windows: Fixed progress bar flickering while printing extracted filenames
 - Windows binaries: Fixed crash on platforms without AVX support

innoextract 1.5 (2015-09-24)
 - Added support for Inno Setup 5.5.6 installers
 - Added support for a modified Inno Setup 5.5.0 variant
 - Added support for building without iconv (Windows-1252 and UTF-16LE only)
 - Added warnings for .bin files that are not part of the installer
 - Added a simple --include (-I) option to filter files thanks to Alexandre Detiste
 - Added a --list-languages option to list available languages
 - Added a --exclude-temp (-m) option to not extract temporary files
 - Added a --language-only option to skip language-independent files
 - Added a --collisions option to abort or rename files on collision
 - Added a --default-language option to prefer a language in case of file collisions
 - Added a --gog-game-id option to print the GOG.com game ID for Galaxy-ready installers
 - Added a --gog (-g) option to extract additional .bin files using unrar or unar
 - Fixed handling of spaces in the --data-dir option
 - Fixed an infinite loop with truncated LZMA streams
 - Fixed handling of forward slashes in stored file paths
 - Fixed size display for powers of 1024
 - Fixed loading headers if there are encrypted chunks
 - Fixed file collisions not being handled case-insensitively
 - Files will now be extracted into the same directory even if the stored case differs
 - Empty directories are now created correctly when extracting
 - Skipped files in encrypted chunks are now listed individually
 - Temporary files are now marked in file listings
 - Error summary is now written to stderr when using --quiet
 - Colors are now only enabled automatically if $TERM is set to something other than "dumb"
 - Improved error and warning messages
 - Build system improvements
 - Debug output can now be enabled separately from debug builds
 - Windows: Added support for using the Win32 API for string encoding conversion
 - Windows: Fixed unicode console output

innoextract 1.4-windows-r2 (2014-04-17)
 - This is a Windows-specific hotfix release, no other platforms are affected
 - Fixed running innoextract under Windows XP

innoextract 1.4-windows-r1 (2013-05-14)
 - This is a Windows-specific hotfix release, no other platforms are affected
 - Fixed a crash on startup under Windows
 - Reduced progress bar flickering under Windows
 - Fixed original console text color not being restored under Windows

innoextract 1.4 (2013-03-11)
 - Fixed build on non-Linux platforms with a separate libiconv (Windows™, macOS)
 - Fixed build on systems with non-standard iconv function prototypes (FreeBSD)
 - Fixed MSVC build
 - Fixed build with older glibc versions
 - Fixed issues with the progress bar in sandbox environments
 - Fixed string conversion on systems where libiconv defaults to big-endian variants
 - Fixed extracting very large installers with 32-bit innoextract builds
 - Improved handling of invalid encoded strings
 - Improved error messages when input or output files could not be opened
 - The --list command-line option can now combined with --test or --extract
 - The --version command-line option can now be modified with --quiet or --silent
 - Added color output and progress bar support for Windows™
 - Added support for Unicode filenames under Windows™
 - Added support for preserving timestamps of extracted files (enabled by default)
 - Added a --timestamps (-T) command-line options to control or disable file timestamps
 - Added an --output-dir (-d) command-line option to control where files are extracted
 - Added various CMake options to fine-tune the build process
 - Various bug fixes and tweaks

innoextract 1.3 (2012-07-03)
 - Fixed --quiet and --silent flags being ignored for some multi-file installers output
 - Now compiles in C++11 mode if supported
 - Added a warning when extracting unsupported setup data versions
 - Added support for Inno Setup 5.5.0 installers

innoextract 1.2 (2012-04-01)
 - Fixed compile errors with older versions of Boost or GCC.
 - Prevented linking against libraries that aren't actually needed.

innoextract 1.1 (2012-03-19)
 - Added support to extract files for a specific language.
 - Fixed a bug in the setup header parsing code.

innoextract 1.0 (2012-03-01)
 - Initial release.
 - Can list and extract files but not much more.
```

## File: `CMakeLists.txt`
```
cmake_minimum_required(VERSION 2.8...3.31)

if(CMAKE_VERSION VERSION_LESS 3.12)
	cmake_policy(VERSION ${CMAKE_VERSION})
endif()

if(DEFINED CMAKE_POLICY_DEFAULT_CMP0167 AND POLICY CMP0167)
	cmake_policy(SET CMP0167 ${CMAKE_POLICY_DEFAULT_CMP0167})
endif()

project(innoextract)


# Define configuration options

if(CMAKE_SYSTEM_NAME MATCHES "Darwin")
	set(MACOS 1)
else()
	set(MACOS 0)
endif()

macro(suboption _var _comment _type _default)
	if(NOT DEFINED ${_var})
		set(${_var} "${_default}")
	else()
		set(${_var} "${${_var}}" CACHE ${_type} "${_comment}")
	endif()
endmacro()

option(DEVELOPER "Use build settings suitable for developers" OFF)
option(CONTINUOUS_INTEGRATION "Use build settings suitable for CI" OFF)

# Components
set(default_BUILD_TESTS OFF)
if(CONTINUOUS_INTEGRATION OR DEVELOPER)
	set(default_BUILD_TESTS ON)
endif()
suboption(BUILD_TESTS "Build tests" BOOL ${default_BUILD_TESTS})
option(BUILD_DECRYPTION "Build decryption support" ON)

# Optional dependencies
option(USE_LZMA "Build LZMA decompression support" ON)
option(USE_DYNAMIC_UTIMENSAT "Dynamically load utimensat if not available at compile time" OFF)

# Alternative dependencies
set(WITH_CONV CACHE STRING "The library to use for charset conversions")

# Build types
option(DEBUG_EXTRA "Expensive debug options" OFF)
option(SET_WARNING_FLAGS "Adjust compiler warning flags" ON)
option(SET_NOISY_WARNING_FLAGS "Enable noisy compiler warnings" OFF)
option(SET_OPTIMIZATION_FLAGS "Adjust compiler optimization flags" ON)
set(default_FASTLINK OFF)
if(DEVELOPER OR CONTINUOUS_INTEGRATION)
	set(default_FASTLINK ON)
endif()
suboption(FASTLINK "Optimize (incremental) linking speed" BOOL ${default_FASTLINK})
set(default_USE_LD "default")
if(SET_OPTIMIZATION_FLAGS OR FASTLINK)
	set(default_USE_LD "best")
endif()
suboption(USE_LD "The linker to use (mold, lld, gold, bfd, best or default)" STRING "${default_USE_LD}")
set(default_USE_LTO OFF)
if(SET_OPTIMIZATION_FLAGS AND NOT FASTLINK)
	set(default_USE_LTO ON)
endif()
suboption(USE_LTO "Use link-time code generation" BOOL ${default_USE_LTO})
suboption(WERROR "Turn warnings into errors" BOOL ${CONTINUOUS_INTEGRATION})
suboption(CXX_STD_VERSION "Maximum C++ standard version to enable" STRING 2017)
if(DEVELOPER OR CMAKE_BUILD_TYPE STREQUAL "Debug")
	set(default_DEBUG ON)
else()
	set(default_DEBUG OFF)
endif()
suboption(DEBUG "Build with debug output" BOOL ${default_DEBUG})
if(DEBUG)
	add_definitions(-DDEBUG=1)
endif()

set(default_USE_STATIC_LIBS OFF)
if(WIN32)
	set(default_USE_STATIC_LIBS ON)
endif()
option(USE_STATIC_LIBS       "Statically link libraries" ${default_USE_STATIC_LIBS})
option(LZMA_USE_STATIC_LIBS  "Statically link liblzma"   ${USE_STATIC_LIBS})
option(ZLIB_USE_STATIC_LIBS  "Statically link libz"      ${USE_STATIC_LIBS})
option(BZip2_USE_STATIC_LIBS "Statically link libbz2"    ${USE_STATIC_LIBS})
option(Boost_USE_STATIC_LIBS "Statically link Boost"     ${USE_STATIC_LIBS})
option(iconv_USE_STATIC_LIBS "Statically link libiconv"  ${USE_STATIC_LIBS})

# Make optional dependencies required
suboption(STRICT_USE "Abort if there are missing optional dependencies" BOOL ${CONTINUOUS_INTEGRATION})
if(STRICT_USE)
	set(OPTIONAL_DEPENDENCY REQUIRED)
else()
	set(OPTIONAL_DEPENDENCY)
endif()

# Test configuration
set(RUN_TARGET CACHE STRING "Wrapper to run built targets")
mark_as_advanced(RUN_TARGET)
set(default_RUN_TESTS OFF)
if((DEVELOPER OR CONTINUOUS_INTEGRATION) AND (NOT CMAKE_CROSSCOMPILING OR NOT RUN_TARGET STREQUAL ""))
	set(default_RUN_TESTS ON)
endif()
suboption(RUN_TESTS "Run tests as part of the default build target" BOOL ${default_RUN_TESTS})

# Install destinations
if(CMAKE_VERSION VERSION_LESS 2.8.5)
	set(CMAKE_INSTALL_DATAROOTDIR "share" CACHE
	    STRING "read-only architecture-independent data root (share) (relative to prefix).")
	set(CMAKE_INSTALL_BINDIR "bin" CACHE
	    STRING "user executables (bin) (relative to prefix).")
	set(CMAKE_INSTALL_MANDIR "${CMAKE_INSTALL_DATAROOTDIR}/man" CACHE
	    STRING "man documentation (DATAROOTDIR/man) (relative to prefix).")
	mark_as_advanced(
		CMAKE_INSTALL_DATAROOTDIR
		CMAKE_INSTALL_BINDIR
		CMAKE_INSTALL_MANDIR
	)
else()
	include(GNUInstallDirs)
endif()


# Helper scrips

include(CheckSymbolExists)

set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake") # For custom cmake modules
include(BuildType)
include(CompileCheck)
include(CreateSourceGroups)
include(CXXVersionCheck)
include(Doxygen)
include(FilterList)
include(PrintConfiguration)
include(StyleCheck)
include(UseStaticLibs)
include(VersionString)


# Find required libraries

# Win32 API
if(WIN32)
	# Ensure we aren't using functionalities not found under Window XP SP1
	add_definitions(-D_WIN32_WINNT=0x0502)
	add_definitions(-DNOMINMAX)
	add_definitions(-DWIN32_LEAN_AND_MEAN)
endif()

if(USE_STATIC_LIBS AND NOT MSVC)
	add_ldflag("-static-libstdc++")
	add_ldflag("-static-libgcc")
endif()

unset(LIBRARIES)

if(BUILD_DECRYPTION)
	set(INNOEXTRACT_HAVE_DECRYPTION 1)
endif()

if(USE_LZMA)
	find_package(LZMA REQUIRED)
	list(APPEND LIBRARIES ${LZMA_LIBRARIES})
	include_directories(SYSTEM ${LZMA_INCLUDE_DIR})
	add_definitions(${LZMA_DEFINITIONS})
	set(INNOEXTRACT_HAVE_LZMA 1)
else()
	message(WARNING "\nDisabling LZMA decompression support.\n"
	                "You won't be able to extract most newer Inno Setup installers.")
	set(INNOEXTRACT_HAVE_LZMA 0)
endif()

find_package(Boost REQUIRED COMPONENTS
	iostreams
	filesystem
	date_time
	system
	program_options
)
list(APPEND LIBRARIES ${Boost_LIBRARIES})
link_directories(${Boost_LIBRARY_DIRS})
include_directories(SYSTEM ${Boost_INCLUDE_DIR})
if(NOT Boost_VERSION_MACRO)
	# CMP0093 changed Boost_VERSION to x.y.z format and provide the old format in Boost_VERSION_MACRO
	set(Boost_VERSION_MACRO ${Boost_VERSION})
endif()
add_definitions(-DBOOST_SYSTEM_DISABLE_THREADS)
if(win32)
	add_definitions(-DBOOST_SYSTEM_USE_UTF8)
endif()

has_static_libs(Boost Boost_LIBRARIES)
if(Boost_HAS_STATIC_LIBS)
	foreach(Lib IN ITEMS ZLIB BZip2)
		string(TOUPPER ${Lib} LIB)
		string(TOLOWER ${Lib} lib)
		foreach(static IN ITEMS 1 0)
			if(static)
				use_static_libs(${Lib})
			endif()
			if(WIN32)
				find_package(Boost COMPONENTS ${lib} QUIET)
			endif()
			if(Boost_${LIB}_FOUND)
				message (STATUS "Found boost_${lib}")
				set(${LIB}_LIBRARIES ${Boost_${LIB}_LIBRARY})
			else()
				find_package(${Lib} REQUIRED)
			endif()
			if(static)
				use_static_libs_restore()
			endif()
			if(${LIB}_LIBRARIES OR STRICT_USE)
				break()
			endif()
		endforeach()
		list(APPEND LIBRARIES ${${LIB}_LIBRARIES})
	endforeach()
endif()

set(INNOEXTRACT_HAVE_ICONV 0)
set(INNOEXTRACT_HAVE_WIN32_CONV 0)
if(WIN32 AND (NOT WITH_CONV OR WITH_CONV STREQUAL "win32"))
	set(INNOEXTRACT_HAVE_WIN32_CONV 1)
elseif(NOT WITH_CONV OR WITH_CONV STREQUAL "iconv")
	if(STRICT_USE)
		set(ICONV_REQUIRED REQUIRED)
	else()
		set(ICONV_REQUIRED)
	endif()
	find_package(iconv ${ICONV_REQUIRED})
	if(ICONV_FOUND)
		list(APPEND LIBRARIES ${iconv_LIBRARIES})
		include_directories(SYSTEM ${iconv_INCLUDE_DIR})
		add_definitions(${iconv_DEFINITIONS})
		set(INNOEXTRACT_HAVE_ICONV 1)
	endif()
elseif(WITH_CONV AND NOT WITH_CONV STREQUAL "builtin")
	message(FATAL_ERROR "Invalid WITH_CONV option: ${WITH_CONV}")
endif()


# Set compiler flags

if(Boost_VERSION_MACRO LESS 104800)
	# Older Boost versions don't work with C++11
elseif(NOT CXX_STD_VERSION LESS 2011)
	enable_cxx_version(${CXX_STD_VERSION})
	check_cxx11("alignof" INNOEXTRACT_HAVE_ALIGNOF)
	if(WIN32)
		check_cxx11("std::codecvt_utf8_utf16" INNOEXTRACT_HAVE_STD_CODECVT_UTF8_UTF16 1600)
	endif()
	check_cxx11("std::unique_ptr" INNOEXTRACT_HAVE_STD_UNIQUE_PTR 1600)
endif()

# Don't expose internal symbols to the outside world by default
if(NOT MSVC)
	add_cxxflag("-fvisibility=hidden")
	add_cxxflag("-fvisibility-inlines-hidden")
endif()

# Older glibc versions won't provide some useful symbols by default - request them
# This flag is currently also set by gcc when compiling C++, but not for plain C
if(NOT WIN32)
	check_symbol_exists(__GLIBC__ "features.h" HAVE_GLIBC)
	if(HAVE_GLIBC)
		set(CMAKE_REQUIRED_DEFINITIONS "-D_GNU_SOURCE=1")
		add_definitions(-D_GNU_SOURCE=1)
	endif()
endif()

if(WIN32)
	# Define this so that we don't accitenally use ANSI functions
	add_definitions(-DUNICODE)
	add_definitions(-D_UNICODE)
endif()


# Check for optional functionality and system configuration

if(NOT WIN32)
	
	check_symbol_exists(isatty "unistd.h" INNOEXTRACT_HAVE_ISATTY)
	check_symbol_exists(ioctl "sys/ioctl.h" INNOEXTRACT_HAVE_IOCTL)
	check_symbol_exists(timegm "time.h" INNOEXTRACT_HAVE_TIMEGM)
	check_symbol_exists(gmtime_r "time.h" INNOEXTRACT_HAVE_GMTIME_R)
	check_symbol_exists(AT_FDCWD "fcntl.h" INNOEXTRACT_HAVE_AT_FDCWD)
	if(INNOEXTRACT_HAVE_AT_FDCWD)
		check_symbol_exists(utimensat "sys/stat.h" INNOEXTRACT_HAVE_UTIMENSAT)
	endif()
	if(INNOEXTRACT_HAVE_UTIMENSAT AND INNOEXTRACT_HAVE_AT_FDCWD)
		set(INNOEXTRACT_HAVE_UTIMENSAT_d 1)
	else()
		if(USE_DYNAMIC_UTIMENSAT AND INNOEXTRACT_HAVE_AT_FDCWD)
			set(CMAKE_REQUIRED_LIBRARIES ${CMAKE_DL_LIBS})
			check_symbol_exists(dlsym "dlfcn.h" INNOEXTRACT_HAVE_DLSYM)
			check_symbol_exists(RTLD_DEFAULT "dlfcn.h" INNOEXTRACT_HAVE_RTLD_DEFAULT)
			unset(CMAKE_REQUIRED_LIBRARIES)
			if(INNOEXTRACT_HAVE_DLSYM AND INNOEXTRACT_HAVE_RTLD_DEFAULT)
				set(INNOEXTRACT_HAVE_DYNAMIC_UTIMENSAT 1)
				if(CMAKE_DL_LIBS)
					list(APPEND LIBRARIES ${CMAKE_DL_LIBS})
				endif()
			endif()
		endif()
		check_symbol_exists(utimes "sys/time.h" INNOEXTRACT_HAVE_UTIMES)
	endif()
	check_symbol_exists(posix_spawnp "spawn.h" INNOEXTRACT_HAVE_POSIX_SPAWNP)
	if(INNOEXTRACT_HAVE_POSIX_SPAWNP)
		check_symbol_exists(environ "unistd.h" INNOEXTRACT_HAVE_UNISTD_ENVIRON)
	else()
		check_symbol_exists(fork "unistd.h" INNOEXTRACT_HAVE_FORK)
		check_symbol_exists(execvp "unistd.h" INNOEXTRACT_HAVE_EXECVP)
	endif()
	if(INNOEXTRACT_HAVE_POSIX_SPAWNP OR (INNOEXTRACT_HAVE_FORK AND INNOEXTRACT_HAVE_EXECVP))
		check_symbol_exists(waitpid "sys/wait.h" INNOEXTRACT_HAVE_WAITPID)
	endif()
	
endif()

if(NOT MSVC)
	
	if(CMAKE_CXX_COMPILER_ID STREQUAL "PathScale")
		# EKOPath recognizes these but then fails to link
	else()
		check_builtin(INNOEXTRACT_HAVE_BUILTIN_BSWAP16 "__builtin_bswap16(0)")
		check_builtin(INNOEXTRACT_HAVE_BUILTIN_BSWAP32 "__builtin_bswap32(0)")
		check_builtin(INNOEXTRACT_HAVE_BUILTIN_BSWAP64 "__builtin_bswap64(0)")
	endif()
	if(NOT INNOEXTRACT_HAVE_BUILTIN_BSWAP16)
		check_symbol_exists(bswap_16 "byteswap.h" INNOEXTRACT_HAVE_BSWAP_16)
	endif()
	if(NOT INNOEXTRACT_HAVE_BUILTIN_BSWAP32)
		check_symbol_exists(bswap_32 "byteswap.h" INNOEXTRACT_HAVE_BSWAP_32)
	endif()
	if(NOT INNOEXTRACT_HAVE_BUILTIN_BSWAP64)
		check_symbol_exists(bswap_64 "byteswap.h" INNOEXTRACT_HAVE_BSWAP_64)
	endif()
	
endif()

if($ENV{PORTAGE_REPO_NAME} MATCHES "gentoo")
	# Meh
	unset(LIBRARIES)
endif()


# All sources:

set(DOCUMENTATION 0) # never build these

set(INNOEXTRACT_SOURCES
	
	src/index.hpp if DOCUMENTATION
	src/release.hpp
	
	src/cli/debug.hpp
	src/cli/debug.cpp if DEBUG
	src/cli/extract.hpp
	src/cli/extract.cpp
	src/cli/gog.hpp
	src/cli/gog.cpp
	src/cli/goggalaxy.hpp
	src/cli/goggalaxy.cpp
	src/cli/main.cpp
	
	src/crypto/adler32.hpp
	src/crypto/adler32.cpp
	src/crypto/arc4.hpp if INNOEXTRACT_HAVE_DECRYPTION
	src/crypto/arc4.cpp if INNOEXTRACT_HAVE_DECRYPTION
	src/crypto/checksum.hpp
	src/crypto/checksum.cpp
	src/crypto/crc32.hpp
	src/crypto/crc32.cpp
	src/crypto/hasher.cpp
	src/crypto/hasher.cpp
	src/crypto/iteratedhash.hpp
	src/crypto/md5.hpp
	src/crypto/md5.cpp
	src/crypto/pbkdf2.hpp if INNOEXTRACT_HAVE_DECRYPTION
	src/crypto/pbkdf2.cpp if INNOEXTRACT_HAVE_DECRYPTION
	src/crypto/sha1.hpp
	src/crypto/sha1.cpp
	src/crypto/sha256.hpp
	src/crypto/sha256.cpp
	src/crypto/xchacha20.hpp if INNOEXTRACT_HAVE_DECRYPTION
	src/crypto/xchacha20.cpp if INNOEXTRACT_HAVE_DECRYPTION
	
	src/loader/exereader.hpp
	src/loader/exereader.cpp
	src/loader/offsets.hpp
	src/loader/offsets.cpp
	
	src/setup/component.hpp
	src/setup/component.cpp
	src/setup/data.hpp
	src/setup/data.cpp
	src/setup/delete.hpp
	src/setup/delete.cpp
	src/setup/directory.hpp
	src/setup/directory.cpp
	src/setup/expression.hpp
	src/setup/expression.cpp
	src/setup/file.hpp
	src/setup/file.cpp
	src/setup/filename.hpp
	src/setup/filename.cpp
	src/setup/header.hpp
	src/setup/header.cpp
	src/setup/icon.hpp
	src/setup/icon.cpp
	src/setup/info.hpp
	src/setup/info.cpp
	src/setup/ini.hpp
	src/setup/ini.cpp
	src/setup/item.hpp
	src/setup/item.cpp
	src/setup/language.hpp
	src/setup/language.cpp
	src/setup/message.hpp
	src/setup/message.cpp
	src/setup/permission.hpp
	src/setup/permission.cpp
	src/setup/registry.hpp
	src/setup/registry.cpp
	src/setup/run.hpp
	src/setup/run.cpp
	src/setup/task.hpp
	src/setup/task.cpp
	src/setup/type.hpp
	src/setup/type.cpp
	src/setup/version.hpp
	src/setup/version.cpp
	src/setup/windows.hpp
	src/setup/windows.cpp
	
	src/stream/block.hpp
	src/stream/block.cpp
	src/stream/checksum.hpp
	src/stream/chunk.hpp
	src/stream/chunk.cpp
	src/stream/exefilter.hpp
	src/stream/file.hpp
	src/stream/file.cpp
	src/stream/lzma.hpp
	src/stream/lzma.cpp if INNOEXTRACT_HAVE_LZMA
	src/stream/restrict.hpp
	src/stream/slice.hpp
	src/stream/slice.cpp
	
	src/util/align.hpp
	src/util/ansi.hpp
	src/util/boostfs_compat.hpp
	src/util/console.hpp
	src/util/console.cpp
	src/util/encoding.hpp
	src/util/encoding.cpp
	src/util/endian.hpp
	src/util/enum.hpp
	src/util/flags.hpp
	src/util/fstream.hpp
	src/util/load.hpp
	src/util/load.cpp
	src/util/log.hpp
	src/util/log.cpp
	src/util/math.hpp
	src/util/output.hpp
	src/util/process.hpp
	src/util/process.cpp
	src/util/storedenum.hpp
	src/util/time.hpp
	src/util/time.cpp
	src/util/test.hpp
	src/util/types.hpp
	src/util/unique_ptr.hpp
	src/util/windows.hpp
	src/util/windows.cpp if WIN32
	
)

set(UNITTEST_SOURCES
	
	src/crypto/adler32.cpp
	src/crypto/arc4.cpp if INNOEXTRACT_HAVE_DECRYPTION
	src/crypto/crc32.cpp
	src/crypto/md5.cpp
	src/crypto/pbkdf2.cpp if INNOEXTRACT_HAVE_DECRYPTION
	src/crypto/sha1.cpp
	src/crypto/sha256.cpp
	src/crypto/xchacha20.cpp if INNOEXTRACT_HAVE_DECRYPTION
	
	src/util/test.hpp
	src/util/test.cpp
	
)

filter_list(INNOEXTRACT_SOURCES ALL_INNOEXTRACT_SOURCES)
filter_list(UNITTEST_SOURCES ALL_UNITTEST_SOURCES)

create_source_groups(ALL_INNOEXTRACT_SOURCES)


# Prepare generated files

include_directories(src ${CMAKE_CURRENT_BINARY_DIR})

configure_file("src/configure.hpp.in" "configure.hpp")

set(VERSION_FILE "${PROJECT_BINARY_DIR}/release.cpp")
set(VERSION_SOURCES VERSION "VERSION" LICENSE "LICENSE")
version_file("src/release.cpp.in" ${VERSION_FILE} "${VERSION_SOURCES}" ".git")
list(APPEND INNOEXTRACT_SOURCES ${VERSION_FILE})

set(MAN_INPUT "doc/innoextract.1.in")
set(MAN_FILE "${PROJECT_BINARY_DIR}/innoextract.1")
set(MAN_SOURCES VERSION "VERSION" CHANGELOG "CHANGELOG")
version_file(${MAN_INPUT} ${MAN_FILE} "${MAN_SOURCES}" ".git")
add_custom_target(manpage ALL DEPENDS ${MAN_FILE})


# Main targets

add_executable(innoextract ${INNOEXTRACT_SOURCES})
target_link_libraries(innoextract ${LIBRARIES})

install(TARGETS innoextract RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})

install(FILES ${MAN_FILE} DESTINATION ${CMAKE_INSTALL_MANDIR}/man1 OPTIONAL)


# Test target

if(BUILD_TESTS)
	
	enable_testing()
	
	set(run_tests)
	if(RUN_TESTS)
		set(run_tests ALL)
	endif()
	
	add_executable(unittest ${UNITTEST_SOURCES})
	target_link_libraries(unittest ${LIBRARIES})
	
	if(CMAKE_VERSION VERSION_LESS 3.0)
		set_target_properties(unittest PROPERTIES COMPILE_DEFINITIONS INNOEXTRACT_BUILD_TESTS)
		get_property(unittest_binary TARGET unittest PROPERTY LOCATION)
	else()
		target_compile_definitions(unittest PRIVATE INNOEXTRACT_BUILD_TESTS)
		set(unittest_binary "$<TARGET_FILE:unittest>")
	endif()
	
	add_test(NAME "unittest"
		COMMAND ${RUN_TARGET} "${unittest_binary}" --verbose
		WORKING_DIRECTORY "${PROJECT_BINARY_DIR}"
	)
	
	add_custom_command(
		OUTPUT "${PROJECT_BINARY_DIR}/unittest.check"
		COMMAND ${RUN_TARGET} "${unittest_binary}"
		COMMAND ${CMAKE_COMMAND} -E touch "${PROJECT_BINARY_DIR}/unittest.check"
		DEPENDS unittest
		WORKING_DIRECTORY "${PROJECT_BINARY_DIR}"
		COMMENT "Running unit tests" VERBATIM
	)
	
	add_custom_target(check ${run_tests}
		DEPENDS "${PROJECT_BINARY_DIR}/unittest.check"
	)
	
endif()


# Additional targets.

add_style_check_target(style "${ALL_INNOEXTRACT_SOURCES}" innoextract)

add_doxygen_target(doc "doc/Doxyfile.in" "VERSION" ".git" "${PROJECT_BINARY_DIR}/doc")


# Print a configuration summary

message("")
message("Configuration:")
set(BUILD_TYPE_SUFFIX "")
if(DEBUG AND NOT CMAKE_BUILD_TYPE STREQUAL "Debug")
	set(BUILD_TYPE_SUFFIX "${BUILD_TYPE_SUFFIX} with debug output")
elseif(NOT DEBUG AND NOT CMAKE_BUILD_TYPE STREQUAL "Release")
	set(BUILD_TYPE_SUFFIX "${BUILD_TYPE_SUFFIX} without debug output")
endif()
message(" - Build type: ${CMAKE_BUILD_TYPE}${BUILD_TYPE_SUFFIX}")
print_configuration("Decryption support" FIRST
	INNOEXTRACT_HAVE_DECRYPTION "enabled"
	1                           "disabled"
)
print_configuration("LZMA decompression" FIRST
	INNOEXTRACT_HAVE_LZMA "enabled"
	1                     "disabled"
)
if(INNOEXTRACT_HAVE_DYNAMIC_UTIMENSAT)
	set(time_prefix "nanoseconds if supported, ")
	set(time_suffix " otherwise")
endif()
print_configuration("File time precision" FIRST
	INNOEXTRACT_HAVE_UTIMENSAT_d "nanoseconds"
	WIN32                        "100-nanoseconds"
	INNOEXTRACT_HAVE_UTIMES      "${time_prefix}microseconds${time_suffix}"
	1                            "${time_prefix}seconds${time_suffix}"
)
print_configuration("Charset conversion"
	INNOEXTRACT_HAVE_ICONV        "iconv"
	INNOEXTRACT_HAVE_WIN32_CONV   "Win32"
	1                             "builtin"
)
message("")

if(DEVELOPER)
	
	file(READ "README.md" readme)
	parse_version_file("VERSION" "VERSION")
	string(REPLACE "${VERSION_2}" "" readme_without_version "${readme}")
	if(readme_without_version STREQUAL readme)
		message(WARNING "Could not find '${VERSION_2}' in README.md.")
	endif()
	
	foreach(file IN LISTS ALL_INNOEXTRACT_SOURCES)
		file(READ "${file}" source)
		if(source MATCHES ".*INNOEXTRACT_TEST.*")
			list(FIND ALL_UNITTEST_SOURCES ${file} result)
			if(result EQUAL -1)
				message(WARNING "Could not find '${file}' in UNITTEST_SOURCES")
			endif()
		endif()
	endforeach()
	
endif()
```

## File: `CONTRIBUTING.md`
```markdown

Contributions of all kinds are welcome as [GitHub pull requests](https://github.com/dscharrer/innoextract/pulls) or as patches mailed to daniel@constexpr.org.

If you are planning to implement a larger feature and intend to get it merged, please contact me **first** at daniel@constexpr.org or on the [GitHub issue tracker](https://github.com/dscharrer/innoextract/issues) to discuss the planned changes in order to avoid duplicating work or having to re-do the changes in a way that fits with the project.

There is no official code style guide, but please try to match the style of the existing code and git commit messages.

All contributions must be licensed under the zlib license detailed in the LICENSE file.
```

## File: `LICENSE`
```

Copyright (C) 2011-2020 Daniel Scharrer <daniel@constexpr.org>

This software is provided 'as-is', without any express or implied
warranty.  In no event will the author(s) be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.
```

## File: `README.md`
```markdown

# innoextract - A tool to unpack installers created by Inno Setup

[Inno Setup](https://jrsoftware.org/isinfo.php) is a tool to create installers for Microsoft Windows applications. innoextract allows to extract such installers under non-Windows systems without running the actual installer using wine. innoextract currently supports installers created by Inno Setup 1.2.10 to 6.3.3.

In addition to standard Inno Setup installers, innoextract also supports some modified Inno Setup variants including Martijn Laan's My Inno Setup Extensions 1.3.10 to 3.0.6.1 as well as GOG.com's Inno Setup-based game installers. innoextract is able to unpack Wadjet Eye Games installers (to play with AGS), Arx Fatalis patches (for use with Arx Libertatis) as well as various other Inno Setup executables.

innoextract is available under the ZLIB license - see the LICENSE file.

See the website for [Linux packages](https://constexpr.org/innoextract/#packages).

## Contact

[Website](https://constexpr.org/innoextract/)

Author: [Daniel Scharrer](https://constexpr.org/)

## Dependencies

* **[Boost](https://www.boost.org/) 1.37** or newer
* **liblzma** from [xz-utils](https://tukaani.org/xz/) *(optional)*
* **iconv** (*optional*, either as part of the system libc, as is the case with [glibc](https://www.gnu.org/software/libc/) and [uClibc](https://uclibc.org/), or as a separate [libiconv](https://www.gnu.org/software/libiconv/))

For Boost you will need the headers as well as the `iostreams`, `filesystem`, `date_time`, `system` and `program_options` libraries. Older Boost version may work but are not actively supported. The boost `iostreams` library needs to be build with zlib and bzip2 support.

While innoextract can be built without liblzma by manually setting `-DUSE_LZMA=OFF`, it is highly recommended and you won't be able to extract most installers created by newer Inno Setup versions without it.

To build innoextract you will also need **[CMake](https://cmake.org/) 2.8** and a working C++ compiler, as well as the development headers for liblzma and boost.

See the Website for [operating system-specific instructions](https://constexpr.org/innoextract/install).

## Compile and install

To compile innoextract, run:

    $ mkdir -p build && cd build
    $ cmake ..
    $ make

To install the binaries system-wide, run as root:

    # make install

The default build settings are tuned for users - if you plan to make changes to Arx Libertatis you should append the `-DDEVELOPER=1` option to the `cmake` command to enable debug output and fast incremental builds.

### Build options:

| Option                    | Default   | Description |
|:------------------------- |:---------:|:----------- |
| `BUILD_DECRYPTION`        | `ON`      | Build decryption support.
| `USE_LZMA`                | `ON`      | Use `liblzma`.
| `WITH_CONV`               | *not set* | The charset conversion library to use. Valid values are `iconv`, `win32` and `builtin`¹. If not set, a library appropriate for the target platform will be chosen.
| `CMAKE_BUILD_TYPE`        | `Release` | Set to `Debug` to enable debug output.
| `DEBUG`                   | `OFF`²    | Enable debug output and runtime checks.
| `DEBUG_EXTRA`             | `OFF`     | Expensive debug options.
| `SET_WARNING_FLAGS`       | `ON`      | Adjust compiler warning flags. This should not affect the produced binaries but is useful to catch potential problems.
| `SET_NOISY_WARNING_FLAGS` | `OFF`     | Enable warnings with false positives many cases that still need to be fixed.
| `SET_OPTIMIZATION_FLAGS`  | `ON`      | Adjust compiler optimization flags.
| `CXX_STD_VERSION`         | `2017`    | Maximum C++ standard version to enable.
| `USE_DYNAMIC_UTIMENSAT`   | `OFF`     | Dynamically load utimensat(2) if not available at compile time.
| `USE_STATIC_LIBS`         | `OFF`³    | Turns on static linking for all libraries, including `-static-libgcc` and `-static-libstdc++`. You can also use the individual options below:
| `LZMA_USE_STATIC_LIBS`    | `OFF`⁴    | Statically link `liblzma`.
| `Boost_USE_STATIC_LIBS`   | `OFF`⁴    | Statically link Boost. See also `FindBoost.cmake`.
| `ZLIB_USE_STATIC_LIBS`    | `OFF`⁴    | Statically link `libz`. (used via Boost)
| `BZip2_USE_STATIC_LIBS`   | `OFF`⁴    | Statically link `libbz2`. (used via Boost)
| `iconv_USE_STATIC_LIBS`   | `OFF`⁴    | Statically link `libiconv`.
| `STRICT_USE`              | `OFF`     | Abort if there are missing optional dependencies.
| `DEVELOPER`               | `OFF`     | Enable build options suitable for developers⁵.
| `FASTLINK`                | `OFF`⁶    | Optimize for link speed.
| `USE_LTO`                 | `ON`²     | Use link-time code generation.
| `USE_LD`                  | `best`⁸   | Linker to use - `default`, `mold`, `lld`, `gold`, `bfd` or `best`
| `BUILD_TESTS`             | `OFF`⁶    | Build unit tests that can be run using `make check`
| `RUN_TESTS`               | `OFF`⁷    | Automatically run tests
| `RUN_TARGET`              | (none)    | Wrapper to run binaries produced in the build process
1. The builtin charset conversion only supports Windows-1252 and UTF-16LE. This is normally enough for filenames, but custom message strings (which can be included in filenames) may use arbitrary encodings.
2. Enabled automatically if `CMAKE_BUILD_TYPE` is set to `Debug`.
3. Under Windows, the default is `ON`.
4. Default is `ON` if `USE_STATIC_LIBS` is enabled.
5. Currently this and enables `DEBUG`, `BUILD_TESTS`, `RUN_TESTS` and `FASTLINK` for faster incremental builds and improved debug output, unless those options have been explicitly specified by the user.
6. Enabled automatically if `DEVELOPER` is enabled.
7. Enabled automatically if `DEVELOPER` is enabled unless cross-compiling without `RUN_TARGET` set
8. Disabled automatically (set to `default`) if both `SET_OPTIMIZATION_FLAGS` and `FASTLINK` are disabled. `best` will select the most suited linker based on availability and other settings such as `USE_LTO`.

Install options:

| Option                      | Default              | Description |
|:--------------------------- |:--------------------:|:----------- |
| `CMAKE_INSTALL_PREFIX`      | `/usr/local`         | Where to install innoextract.
| `CMAKE_INSTALL_BINDIR`      | `bin`                | Location for binaries (relative to prefix).
| `CMAKE_INSTALL_DATAROOTDIR` | `share`              | Location for data files (relative to prefix).
| `CMAKE_INSTALL_MANDIR`      | `${DATAROOTDIR}/man` | Location for man pages (relative to prefix).

Set options by passing `-D<option>=<value>` to cmake.

## Run

To extract a setup file to the current directory run:

    $ innoextract <file>

A list of available options can be retrieved using

    $ innoextract --help

Documentation is also available as a man page:

    $ man 1 innoextract

## Limitations

* There is no support for extracting individual components and limited support for filtering by name.

* Included scripts and checks are not executed.

* The mapping from Inno Setup variables like the application directory to subdirectories is hard-coded.

* Names for data slice/disk files in multi-file installers must follow the standard naming scheme.

A perhaps more complete, but Windows-only, tool to extract Inno Setup files is [innounp](http://innounp.sourceforge.net/).

Extracting Windows installer executables created by programs other than Inno Setup is out of the scope of this project. Some of these can be unpacked by the following programs:

* [cabextract](https://cabextract.org.uk/)

* [unshield](https://github.com/twogood/unshield)

## Disclaimer

This project is in no way associated with Inno Setup or [jrsoftware.org](https://jrsoftware.org/).
```

## File: `VERSION`
```
innoextract 1.10-dev

Known working Inno Setup versions:
Inno Setup 1.2.10 to 6.3.3

Bug tracker:
https://innoextract.constexpr.org/issues
```

## File: `cmake/BuildType.cmake`
```

include(CompileCheck)

if(NOT MSVC AND NOT CMAKE_VERSION VERSION_LESS 2.8.6)
	include(CheckCXXSymbolExists)
	check_cxx_symbol_exists(_LIBCPP_VERSION "cstddef" IS_LIBCXX)
	if(IS_LIBCXX AND (DEBUG OR DEBUG_EXTRA))
		check_cxx_symbol_exists(_LIBCPP_HARDENING_MODE "version" ARX_HAVE_LIBCPP_HARDENING_MODE)
		if(NOT ARX_HAVE_LIBCPP_HARDENING_MODE)
			check_cxx_symbol_exists(_LIBCPP_ENABLE_HARDENED_MODE "version" ARX_HAVE_LIBCPP_ENABLE_HARDENED_MODE)
			if(NOT ARX_HAVE_LIBCPP_ENABLE_HARDENED_MODE)
				check_cxx_symbol_exists(_LIBCPP_ENABLE_ASSERTIONS "version" ARX_HAVE_LIBCPP_ENABLE_ASSERTIONS)
			endif()
		endif()
	endif()
else()
	set(IS_LIBCXX OFF)
endif()


option(DEBUG_EXTRA "Expensive debug options" OFF)
option(SET_WARNING_FLAGS "Adjust compiler warning flags" ON)
option(SET_NOISY_WARNING_FLAGS "Enable noisy compiler warnings" OFF)
option(SET_OPTIMIZATION_FLAGS "Adjust compiler optimization flags" ON)

if(MSVC)
	
	if(USE_LTO)
		set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /GL")
		set(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} /LTCG")
		set(CMAKE_SHARED_LINKER_FLAGS_RELEASE "${CMAKE_SHARED_LINKER_FLAGS_RELEASE} /LTCG")
		set(CMAKE_STATIC_LINKER_FLAGS_RELEASE "${CMAKE_STATIC_LINKER_FLAGS_RELEASE} /LTCG")
	endif()
	
	if(FASTLINK)
		
		# Optimize for link speed in developer builds
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /DEBUG:FASTLINK")
		
	elseif(SET_OPTIMIZATION_FLAGS)
		
		# Merge symbols and discard unused symbols
		set(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} /OPT:REF /OPT:ICF")
		set(CMAKE_SHARED_LINKER_FLAGS_RELEASE "${CMAKE_SHARED_LINKER_FLAGS_RELEASE} /OPT:REF /OPT:ICF")
		
	endif()
	
	if(SET_WARNING_FLAGS AND NOT SET_NOISY_WARNING_FLAGS)
		
		# TODO TEMP - disable very noisy warning
		# Conversion from 'A' to 'B', possible loss of data
		add_definitions(/wd4244)
		# warning C4245: 'return': conversion from 'A' to 'B', signed/unsigned mismatch
		add_definitions(/wd4245)
		# warning C4456: declaration of 'xxx' hides previous local declaration
		add_definitions(/wd4456) # triggers on nested BOOST_FOREACH
		# warning C4457: declaration of 'xxx' hides function parameter
		add_definitions(/wd4457)
		# warning C4458: declaration of 'xxx' hides class member
		add_definitions(/wd4458)
		# warning C4459: declaration of 'xxx' hides global declaration
		add_definitions(/wd4459)
		
		# warning C4127: conditional expression is constant
		add_definitions(/wd4127)
		if(MSVC_VERSION LESS 1900)
			# warning C4250: 'xxx': inherits 'std::basic_{i,o}stream::...' via dominance
			add_definitions(/wd4250) # harasses you when inheriting from std::basic_{i,o}stream
			# warning C4510: 'enum_names<const char *>' : default constructor could not be generated
			add_definitions(/wd4510)
			# warning C4512: 'xxx' : assignment operator could not be generated
			add_definitions(/wd4512) # not all classes need an assignment operator...
			# warning C4610: struct 'xxx' can never be instantiated - user defined constructor required
			add_definitions(/wd4610)
		endif()
		add_definitions(/wd4702) # warns in Boost
		add_definitions(/wd4706) # warns in Boost
		add_definitions(/wd4996) # 'unsafe' stdlib functions used by Boost
		
	endif()
	
	if(WERROR)
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /WX")
	endif()
	
	if(SET_OPTIMIZATION_FLAGS)
		
		# Enable exceptions
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /EHsc")
		
		# Enable linker optimization in release
		set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /Ox /Oi /Os")
		
	endif()
	
	foreach(flag_var CMAKE_CXX_FLAGS CMAKE_CXX_FLAGS_DEBUG CMAKE_CXX_FLAGS_RELEASE)
		
		# Disable Run time checks
		if(NOT DEBUG_EXTRA)
			string(REGEX REPLACE "(^| )/RTC1( |$)" "\\1" ${flag_var} "${${flag_var}}")
		endif()
		
		# Remove definition of _DEBUG as it might conflict with libs we're linking with
		string(REGEX REPLACE "(^| )/D_DEBUG( |$)" "\\1" ${flag_var} "${${flag_var}}")
		set(${flag_var} "${${flag_var}} /DNDEBUG")
		
		# Force compiler warning level
		if(SET_WARNING_FLAGS)
			string(REGEX REPLACE "(^| )/W[0-4]( |$)" "\\1" ${flag_var} "${${flag_var}}")
			set(${flag_var} "${${flag_var}} /W4")
		endif()
		
	endforeach(flag_var)
	
	if(NOT MSVC_VERSION LESS 1900)
		add_definitions(/utf-8)
	endif()
	
	# Turn on standards compliant mode
	# /Za is not compatible with /fp:fast, leave it off
	if(NOT MSVC_VERSION LESS 1910)
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /permissive-")
		# /permissive- enables /Zc:twoPhase wich would be good if two phase lookup wasn't still broken in VS 2017
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Zc:twoPhase-")
	endif()
	if(NOT MSVC_VERSION LESS 1900)
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Zc:inline")
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Zc:throwingNew")
	endif()
	if(NOT MSVC_VERSION LESS 1914)
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Zc:__cplusplus")
	endif()
	
	# Always build with debug information
	if(NOT MSVC_VERSION LESS 1700)
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Zi")
		set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /DEBUG")
	endif()
	
else(MSVC)
	
	set(linker_used)
	if(NOT linker_used AND (USE_LD STREQUAL "mold" OR USE_LD STREQUAL "best"))
		# Old versions are unstable or don't support LTO
		if(USE_LD STREQUAL "best")
			execute_process(COMMAND ${CMAKE_CXX_COMPILER} "-fuse-ld=mold" "-Wl,-version"
			                OUTPUT_VARIABLE _Mold_Version ERROR_QUIET)
		endif()
		if(USE_LD STREQUAL "best" AND _Mold_Version MATCHES "mold [0-1]\\.*")
			message(STATUS "Not using ancient ${CMAKE_MATCH_0}")
		else()
			add_ldflag("-fuse-ld=mold")
			if(FLAG_FOUND)
				set(linker_used "mold")
			elseif(STRICT_USE AND NOT USE_LD STREQUAL "best")
				message(FATAL_ERROR "Requested linker is not available")
			endif()
		endif()
	endif()
	if(NOT linker_used AND (USE_LD STREQUAL "lld" OR
	                        (USE_LD STREQUAL "best" AND (NOT USE_LTO OR CMAKE_CXX_COMPILER_ID MATCHES "Clang"))))
		# Only supports LTO with LLVM-based compilers and old versions are unstable
		if(USE_LD STREQUAL "best")
			execute_process(COMMAND ${CMAKE_CXX_COMPILER} "-fuse-ld=lld" "-Wl,-version"
			                OUTPUT_VARIABLE _LLD_Version ERROR_QUIET)
		endif()
		if(USE_LD STREQUAL "best" AND _LLD_Version MATCHES "LLD [0-8]\\.[0-9\\.]*")
			message(STATUS "Not using ancient ${CMAKE_MATCH_0}")
		elseif(USE_LD STREQUAL "best" AND CMAKE_CXX_COMPILER_ID MATCHES "Clang" AND
		       CMAKE_CXX_COMPILER_VERSION VERSION_LESS 9)
			message(STATUS "Not using ancient Clang ${CMAKE_CXX_COMPILER_VERSION}")
		else()
			add_ldflag("-fuse-ld=lld")
			if(FLAG_FOUND)
				set(linker_used "lld")
			elseif(STRICT_USE AND NOT USE_LD STREQUAL "best")
				message(FATAL_ERROR "Requested linker is not available")
			endif()
		endif()
	endif()
	if(NOT linker_used AND (USE_LD STREQUAL "gold" OR USE_LD STREQUAL "best"))
		add_ldflag("-fuse-ld=gold")
		if(FLAG_FOUND)
			set(linker_used "gold")
		elseif(STRICT_USE AND NOT USE_LD STREQUAL "best")
			message(FATAL_ERROR "Requested linker is not available")
		endif()
	endif()
	if(NOT linker_used AND (USE_LD STREQUAL "bfd"))
		add_ldflag("-fuse-ld=bfd")
		if(FLAG_FOUND)
			set(linker_used "bfd")
		elseif(STRICT_USE AND NOT USE_LD STREQUAL "best")
			message(FATAL_ERROR "Requested linker is not available")
		endif()
	endif()
	
	if(USE_LTO)
		add_cxxflag("-flto=auto")
		if(NOT FLAG_FOUND)
			add_cxxflag("-flto")
		endif()
		# TODO set CMAKE_INTERPROCEDURAL_OPTIMIZATION instead
		add_ldflag("-fuse-linker-plugin")
	endif()
	
	if(FASTLINK)
		
		# Optimize for link speed in developer builds
		if(linker_used STREQUAL "mold" OR linker_used STREQUAL "lld")
			# mold and lld are fast enough without -gsplit-dwarf that we don't need to deal with its issues
		else()
			add_cxxflag("-gsplit-dwarf")
			add_cxxflag("-gdwarf-4") # -gsplit-dwarf is broken with DWARF 5
		endif()
		
	elseif(SET_OPTIMIZATION_FLAGS)
		
		# Merge symbols and discard unused symbols
		add_ldflag("-Wl,--gc-sections")
		add_ldflag("-Wl,--icf=all")
		add_cxxflag("-fmerge-all-constants")
		
	endif()
	
	if(SET_WARNING_FLAGS)
		
		# GCC or Clang (and compatible)
		
		add_cxxflag("-Wall")
		add_cxxflag("-Wextra")
		
		add_cxxflag("-Warray-bounds=2")
		add_cxxflag("-Wbool-conversions")
		add_cxxflag("-Wcast-qual")
		add_cxxflag("-Wcatch-value=3")
		add_cxxflag("-Wconversion")
		add_cxxflag("-Wdocumentation")
		add_cxxflag("-Wdouble-promotion")
		add_cxxflag("-Wduplicated-cond")
		add_cxxflag("-Wextra-semi")
		add_cxxflag("-Wformat=2")
		add_cxxflag("-Wheader-guard")
		add_cxxflag("-Wheader-hygiene")
		add_cxxflag("-Winit-self")
		add_cxxflag("-Wkeyword-macro")
		add_cxxflag("-Wliteral-conversion")
		add_cxxflag("-Wlogical-op")
		add_cxxflag("-Wmissing-declarations")
		add_cxxflag("-Wnoexcept")
		add_cxxflag("-Woverflow")
		add_cxxflag("-Woverloaded-virtual")
		add_cxxflag("-Wpessimizing-move")
		add_cxxflag("-Wpointer-arith")
		add_cxxflag("-Wredundant-decls")
		add_cxxflag("-Wreserved-id-macro")
		add_cxxflag("-Wshift-overflow")
		add_cxxflag("-Wsign-conversion")
		add_cxxflag("-Wstrict-null-sentinel")
		add_cxxflag("-Wstringop-overflow=4")
		add_cxxflag("-Wundef")
		add_cxxflag("-Wunused-const-variable=1")
		add_cxxflag("-Wunused-macros")
		add_cxxflag("-Wvla")
		
		if(NOT CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR NOT CMAKE_CXX_COMPILER_VERSION VERSION_LESS 4.8)
			add_cxxflag("-Wold-style-cast")
		endif()
		
		if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" AND CMAKE_CXX_COMPILER_VERSION VERSION_LESS 5
		   AND NOT SET_NOISY_WARNING_FLAGS)
			# In older GCC versions this warning is too strict
		elseif(CMAKE_CXX_COMPILER_ID MATCHES "Clang" AND CMAKE_CXX_COMPILER_VERSION VERSION_LESS 5
		       AND NOT SET_NOISY_WARNING_FLAGS)
			# In older Clang verstions this warns on BOOST_SCOPE_EXIT
		elseif(CMAKE_CXX_COMPILER_ID STREQUAL "Intel" AND NOT SET_NOISY_WARNING_FLAGS)
			# For icc this warning is too strict
		else()
			add_cxxflag("-Wshadow")
		endif()
		
		add_ldflag("-Wl,--no-undefined")
		
		if(SET_NOISY_WARNING_FLAGS)
			
			# These are too noisy to enable right now but we still want to track new warnings.
			# TODO enable by default as soon as most are silenced
			add_cxxflag("-Wconditionally-supported") # warns on casting from pointer to function pointer
			add_cxxflag("-Wduplicated-branches")
			add_cxxflag("-Wstrict-aliasing=1") # has false positives
			add_cxxflag("-Wuseless-cast") # has false positives
			add_cxxflag("-Wsign-promo")
			# add_cxxflag("-Wnull-dereference") not that useful without deduction path
			
			# Possible optimization opportunities
			add_cxxflag("-Wdisabled-optimization")
			add_cxxflag("-Wpadded")
			add_cxxflag("-Wunsafe-loop-optimizations")
			
			if(NOT DEBUG_EXTRA OR NOT CMAKE_CXX_COMPILER_ID MATCHES "Clang")
				add_ldflag("-Wl,--detect-odr-violations")
			endif()
			
		else()
			
			# icc
			if(CMAKE_CXX_COMPILER_ID STREQUAL "Intel")
				# '... was declared but never referenced'
				# While normally a sensible warning, it also fires when a member isn't used for
				# *all* instantiations of a template class, making the warning too annoying to
				# be useful
				add_cxxflag("-wd177")
				# 'external function definition with no prior declaration'
				# This gets annoying fast with small inline/template functions.
				add_cxxflag("-wd1418")
				# 'non-pointer conversion from "int" to "…" may lose significant bits'
				add_cxxflag("-wd2259")
			endif()
			
			# -Wuninitialized causes too many false positives in older gcc versions
			if(CMAKE_COMPILER_IS_GNUCXX)
				# GCC is 'clever' and silently accepts -Wno-*  - check for the non-negated variant
				check_compiler_flag(FLAG_FOUND "-Wmaybe-uninitialized")
				if(FLAG_FOUND)
					add_cxxflag("-Wno-maybe-uninitialized")
				else()
					add_cxxflag("-Wno-uninitialized")
				endif()
			endif()
			
			# Xcode does not support -isystem yet
			if(MACOS)
				add_cxxflag("-Wno-undef")
			endif()
			
		endif()
		
		if(IS_LIBCXX)
			add_definitions(-D_LIBCPP_ENABLE_NODISCARD)
			add_definitions(-D_LIBCPP_ENABLE_THREAD_SAFETY_ANNOTATIONS)
		endif()
		
	endif(SET_WARNING_FLAGS)
	
	if(WERROR)
		add_cxxflag("-Werror")
	endif()
	
	if(DEBUG_EXTRA)
		add_cxxflag("-ftrapv") # to add checks for (undefined) signed integer overflow
		add_cxxflag("-fbounds-checking")
		add_cxxflag("-fcatch-undefined-behavior")
		add_cxxflag("-fstack-protector-all")
		add_cxxflag("-fsanitize=address")
		# add_cxxflag("-fsanitize=thread") does not work together with -fsanitize=address
		add_cxxflag("-fsanitize=leak")
		add_cxxflag("-fsanitize=undefined")
		if(ARX_HAVE_LIBCPP_HARDENING_MODE)
			# libc++ 18+
			add_definitions(-D_LIBCPP_HARDENING_MODE=_LIBCPP_HARDENING_MODE_DEBUG)
		elseif(ARX_HAVE_LIBCPP_ENABLE_HARDENED_MODE)
			# libc++ 17 - Full debug mode is now a compile-time option and all -D_LIBCPP_DEBUG=1 does is
			# generate an #error if the library was not built in debug mode :|
			add_definitions(-D_LIBCPP_ENABLE_HARDENED_MODE=1)
		elseif(ARX_HAVE_LIBCPP_ENABLE_ASSERTIONS)
			# libc++ 15-16 - Full debug mode is now a compile-time option and all -D_LIBCPP_DEBUG=1 does is
			# generate an #error if the library was not built in debug mode :|
			add_definitions(-D_LIBCPP_ENABLE_ASSERTIONS=1)
		elseif(IS_LIBCXX)
			# older libc++
			add_definitions(-D_LIBCPP_DEBUG=1)
		else()
			# libstdc++
			add_definitions(-D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC -D_GLIBCXX_SANITIZE_VECTOR)
			set(disable_libstdcxx_debug "-U_GLIBCXX_DEBUG -U_GLIBCXX_DEBUG_PEDANTIC")
		endif()
	elseif(DEBUG)
		if(ARX_HAVE_LIBCPP_HARDENING_MODE)
			#libc++ 18+
			add_definitions(-D_LIBCPP_HARDENING_MODE=_LIBCPP_HARDENING_MODE_EXTENSIVE)
		elseif(ARX_HAVE_LIBCPP_ENABLE_HARDENED_MODE)
			# libc++ 17
			add_definitions(-D_LIBCPP_ENABLE_HARDENED_MODE=1)
		elseif(ARX_HAVE_LIBCPP_ENABLE_ASSERTIONS)
			# libc++ 15-16
			add_definitions(-D_LIBCPP_ENABLE_ASSERTIONS=1)
		elseif(IS_LIBCXX)
			# older libc++ - 0 means light checks only, it does not mean no checks
			add_definitions(-D_LIBCPP_DEBUG=0)
		else()
			# libstdc++
			add_definitions(-D_GLIBCXX_ASSERTIONS=1)
		endif()
	endif()
	
	if(CMAKE_BUILD_TYPE STREQUAL "")
		set(CMAKE_BUILD_TYPE "Release")
	endif()
	
	if(SET_OPTIMIZATION_FLAGS)
		
		if(MACOS)
			# TODO For some reason this check succeeds on macOS, but then
			# flag causes the actual build to fail :(
		else()
			# Link as few libraries as possible
			# This is much easier than trying to decide which libraries are needed for each
			# system
			add_ldflag("-Wl,--as-needed")
		endif()
		
		if(CMAKE_BUILD_TYPE STREQUAL "Debug")
			
			# set debug symbol level to -g3
			check_compiler_flag(RESULT "-g3")
			if(NOT RESULT STREQUAL "")
				string(REGEX REPLACE "(^| )-g(|[0-9]|gdb)" "\\1" CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
				set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} ${RESULT}")
			endif()
			
			# disable optimizations
			check_compiler_flag(RESULT "-Og")
			if(NOT RESULT)
				check_compiler_flag(RESULT "-O0")
			endif()
			string(REGEX REPLACE "-O[0-9]" "" CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
			set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} ${RESULT}")
			
		elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
			
			if((NOT CMAKE_CXX_FLAGS MATCHES "-g(|[0-9]|gdb)")
			   AND (NOT CMAKE_CXX_FLAGS_RELEASE MATCHES "-g(|[0-9]|gdb)"))
				add_cxxflag("-g2")
			endif()
			
			add_cxxflag("-ffast-math")
			
		endif()
		
	endif(SET_OPTIMIZATION_FLAGS)
	
endif(MSVC)
```

## File: `cmake/CXXVersionCheck.cmake`
```

# Copyright (C) 2013-2020 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

include(CheckCXXSourceCompiles)
include(CompileCheck)

set(CXX_VERSION 2003)
get_filename_component(CXX_CHECK_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)
set(CXX_CHECK_DIR "${CXX_CHECK_DIR}/check")

function(enable_cxx_version version)
	
	set(versions 17 14 11)
	
	if(MSVC)
		if(NOT version LESS 2011 AND NOT MSVC_VERSION LESS 1600)
			set(CXX_VERSION 2011)
			if(NOT version LESS 2017 AND NOT MSVC_VERSION LESS 1911)
				set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /std:c++17")
				set(CXX_VERSION 2017)
			elseif(NOT version LESS 2014 AND NOT MSVC_VERSION LESS 1910)
				set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /std:c++14")
				set(CXX_VERSION 2014)
			elseif(NOT version LESS 2014 AND NOT MSVC_VERSION LESS 1900)
				# Only introduced with update 3 of MSVC 2015
				add_cxxflag("/std:c++14")
				if(FLAG_FOUND)
					set(CXX_VERSION 2014)
				endif()
			endif()
		endif()
	else()
		set(FLAG_FOUND 0)
		foreach(ver IN LISTS versions)
			if(NOT version LESS 20${ver} AND NOT FLAG_FOUND)
				add_cxxflag("-std=c++${ver}")
				if(FLAG_FOUND)
					set(CXX_VERSION 20${ver})
					break()
				endif()
			endif()
		endforeach()
		if(NOT FLAG_FOUND)
			# Check if the compiler supports the -std flag at all
			# Don't actually use the flag to allow for compiler extensions a la -sdt=gnu++03
			check_compiler_flag(FLAG_FOUND "-std=c++03")
			if(NOT FLAG_FOUND)
				check_compiler_flag(FLAG_FOUND "-std=c++98")
			endif()
		endif()
		if(NOT FLAG_FOUND)
			# Compiler does not support he -std flag, assume the highest supported C++ version is available
			# by default or can be enabled by CMake and rely on tests for individual features.
			foreach(ver IN LISTS versions)
				if(NOT version LESS 20${ver})
					set(CXX_VERSION 20${ver})
					break()
				endif()
			endforeach()
		endif()
		if(SET_WARNING_FLAGS AND NOT CXX_VERSION LESS 2011)
			add_cxxflag("-pedantic")
		endif()
	endif()
	
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}" PARENT_SCOPE)
	set(CXX_VERSION ${CXX_VERSION} PARENT_SCOPE)
	
	# Tell CMake about our desired C++ version so that it doesn't override our value with a lower version.
	# We check -std ourselves first because
	# - This feature is new in CMake 3.1
	# - Not all CMake versions know how to check for all C++ versions
	# - CMake doesn't tell us what versions are available
	if(NOT CMAKE_VERSION VERSION_LESS 3.12)
		set(max_cxx_standard 20)
	elseif(NOT CMAKE_VERSION VERSION_LESS 3.8)
		set(max_cxx_standard 17)
	else()
		set(max_cxx_standard 14)
	endif()
	foreach(ver IN LISTS versions)
		if(NOT CXX_VERSION LESS 20${ver} AND NOT max_cxx_standard LESS ver)
			set(CMAKE_CXX_STANDARD ${ver} PARENT_SCOPE)
			set(CMAKE_CXX_STANDARD_REQUIRED OFF PARENT_SCOPE)
			set(CMAKE_CXX_EXTENSIONS OFF PARENT_SCOPE)
			break()
		endif()
	endforeach()
	
endfunction(enable_cxx_version)

function(check_cxx version feature resultvar)
	set(result)
	if(NOT CXX_VERSION LESS 20${version} OR (ARGC GREATER 3 AND ARGV3 STREQUAL "ALWAYS"))
		if(MSVC AND ARGC GREATER 3)
			if(NOT MSVC_VERSION LESS ARGV3)
				set(result 1)
			endif()
		else()
			string(REGEX REPLACE "[^a-zA-Z0-9_][^a-zA-Z0-9_]*" "-" check "${feature}")
			string(REGEX REPLACE "^--*" "" check "${check}")
			string(REGEX REPLACE "--*$" "" check "${check}")
			set(file "${CXX_CHECK_DIR}/cxx${version}-${check}.cpp")
			set(old_CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
			set(old_CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")
			strip_warning_flags(CMAKE_CXX_FLAGS)
			strip_warning_flags(CMAKE_EXE_LINKER_FLAGS)
			check_compile(result "${file}" "${feature}" "C++${version} feature")
			set(CMAKE_CXX_FLAGS "${old_CMAKE_CXX_FLAGS}")
			set(CMAKE_EXE_LINKER_FLAGS "${old_CMAKE_EXE_LINKER_FLAGS}")
		endif()
	endif()
	if(NOT DEFINED result OR result STREQUAL "")
		set(${resultvar} OFF PARENT_SCOPE)
	else()
		set(${resultvar} ON PARENT_SCOPE)
	endif()
endfunction()

macro(check_cxx11 feature resultvar)
	check_cxx(11 ${ARGV})
endmacro()

macro(check_cxx14 feature resultvar)
	check_cxx(14 ${ARGV})
endmacro()

macro(check_cxx17 feature resultvar)
	check_cxx(17 ${ARGV})
endmacro()
```

## File: `cmake/CompileCheck.cmake`
```

# Copyright (C) 2011-2020 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

# Note: In CMake before 3.0 set(var "" PARENT_SCOPE) *unsets* the variable in the
# parent scope instead of setting it to the empty string.
# This means if(var STREQUAL "") will be false since var is not defined and thus not expanded.

function(check_compile RESULT FILE FLAG TYPE)
	
	string(REGEX REPLACE "[^a-zA-Z0-9_][^a-zA-Z0-9_]*" "-" cachevar "${TYPE}-${FLAG}")
	set(cahevar "CHECK_COMPILE_${cahevar}")
	
	if(DEFINED ${cachevar})
		if(${cachevar})
			set(${RESULT} "${FLAG}" PARENT_SCOPE)
		else()
			set(${RESULT} "" PARENT_SCOPE)
		endif()
		return()
	endif()
	
	string(REGEX REPLACE "[^a-zA-Z0-9]" "\\\\\\0" escaped_flag ${FLAG} )
	
	# CMake already has a check_cxx_compiler_flag macro in CheckCXXCompilerFlag, but
	# it prints the result variable in the output (which is ugly!) and also uses it
	# as a key to cache checks - so it would need to be unique for each flag.
	# Unfortunately it also naively pastes the variable name inside a regexp so
	# if we tried to use the flag itself in the variable name it will fail for -std=c++11.
	# But we can at least use the expressions for warnings from that macro (and more):
	set(fail_regexps
		"warning:"                                     # general
		"unrecognized .*option"                        # GNU
		"${escaped_flag}.* not supported"              # GNU
		"unknown .*option"                             # Clang
		"ignoring unknown option"                      # MSVC
		"warning D9002"                                # MSVC, any lang
		"warning #[0-9]*:"                             # Intel
		"option.*not supported"                        # Intel
		"invalid argument .*option"                    # Intel
		"ignoring option .*argument required"          # Intel
		"command line warning"                         # Intel
		"[Uu]nknown option"                            # HP
		"[Ww]arning: [Oo]ption"                        # SunPro
		"command option .* is not recognized"          # XL
		"not supported in this configuration; ignored" # AIX
		"File with unknown suffix passed to linker"    # PGI
		"WARNING: unknown flag:"                       # Open64
	)
	
	# Set the flags to check
	set(old_CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
	set(old_CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")
	set(old_CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS}")
	set(old_CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS}")
	if(TYPE STREQUAL "linker flag")
		set(CMAKE_EXE_LINKER_FLAGS "${old_CMAKE_EXE_LINKER_FLAGS} ${FLAG}")
		set(CMAKE_SHARED_LINKER_FLAGS "${old_CMAKE_SHARED_LINKER_FLAGS} ${FLAG}")
		set(CMAKE_MODULE_LINKER_FLAGS "${old_CMAKE_MODULE_LINKER_FLAGS} ${FLAG}")
	elseif(TYPE STREQUAL "compiler flag")
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${FLAG}")
	endif()
	
	# Check if we can compile and link a simple file with the new flags
	try_compile(
		check_compiler_flag ${PROJECT_BINARY_DIR} ${FILE}
		CMAKE_FLAGS "-DCMAKE_CXX_FLAGS:STRING=${CMAKE_CXX_FLAGS}"
		            "-DCMAKE_EXE_LINKER_FLAGS:STRING=${CMAKE_EXE_LINKER_FLAGS}"
		            "-DCMAKE_SHARED_LINKER_FLAGS:STRING=${CMAKE_SHARED_LINKER_FLAGS}"
		            "-DCMAKE_MODULE_LINKER_FLAGS:STRING=${CMAKE_MODULE_LINKER_FLAGS}"
		OUTPUT_VARIABLE ERRORLOG
	)
	
	# Restore the old flags
	set(CMAKE_CXX_FLAGS "${old_CMAKE_CXX_FLAGS}")
	set(CMAKE_EXE_LINKER_FLAGS "${old_CMAKE_EXE_LINKER_FLAGS}")
	set(CMAKE_SHARED_LINKER_FLAGS "${old_CMAKE_SHARED_LINKER_FLAGS}")
	set(CMAKE_MODULE_LINKER_FLAGS "${old_CMAKE_MODULE_LINKER_FLAGS}")
	
	if(NOT check_compiler_flag)
		message(STATUS "Checking ${TYPE}: ${FLAG} - unsupported")
		set(${RESULT} "" PARENT_SCOPE)
		set("${cachevar}" 0 CACHE INTERNAL "...")
	else()
		
		set(has_warning 0)
		foreach(expr IN LISTS fail_regexps)
			if("${ERRORLOG}" MATCHES "${expr}")
				set(has_warning 1)
			endif()
		endforeach()
		
		if(has_warning)
			message(STATUS "Checking ${TYPE}: ${FLAG} - unsupported (warning)")
			set(${RESULT} "" PARENT_SCOPE)
			set("${cachevar}" 0 CACHE INTERNAL "...")
		else()
			message(STATUS "Checking ${TYPE}: ${FLAG}")
			set(${RESULT} "${FLAG}" PARENT_SCOPE)
			set("${cachevar}" 1 CACHE INTERNAL "...")
		endif()
		
	endif()
	
endfunction(check_compile)

function(check_flag RESULT FLAG TYPE)
	set(compile_test_file "${CMAKE_CURRENT_BINARY_DIR}/compile_flag_test.cpp")
	if(MSVC)
		file(WRITE ${compile_test_file} "int main(){ return 0; }\n")
	else()
		file(WRITE ${compile_test_file} "__attribute__((const)) int main(){ return 0; }\n")
	endif()
	check_compile(result "${compile_test_file}" "${FLAG}" "${TYPE} flag")
	set(${RESULT} "${result}" PARENT_SCOPE)
endfunction(check_flag)

macro(strip_warning_flags VAR)
	string(REGEX REPLACE "(^| )\\-(W[^ l][^ ]*|Wl[^,][^ ]*|pedantic)" "" ${VAR} "${${VAR}}")
endmacro()

function(check_builtin RESULT EXPR)
	string(REGEX REPLACE "[^a-zA-Z0-9_][^a-zA-Z0-9_]*" "-" check "${EXPR}")
	string(REGEX REPLACE "_*\\-_*" "-" check "${check}")
	string(REGEX REPLACE "^[_\\-]+" "" check "${check}")
	string(REGEX REPLACE "[_\\-]+$" "" check "${check}")
	set(compile_test_file "${CMAKE_CURRENT_BINARY_DIR}/check-builtin-${check}.cpp")
	string(REGEX MATCH "[a-zA-Z_][a-zA-Z_0-9]*" type "${EXPR}")
	file(WRITE ${compile_test_file} "__attribute__((const)) int main(){ (void)(${EXPR}); return 0; }\n")
	set(old_CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
	set(old_CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")
	strip_warning_flags(CMAKE_CXX_FLAGS)
	strip_warning_flags(CMAKE_EXE_LINKER_FLAGS)
	check_compile(result "${compile_test_file}" "${type}" "compiler builtin")
	set(CMAKE_CXX_FLAGS "${old_CMAKE_CXX_FLAGS}")
	set(CMAKE_EXE_LINKER_FLAGS "${old_CMAKE_EXE_LINKER_FLAGS}")
	set(${RESULT} "${result}" PARENT_SCOPE)
endfunction(check_builtin)

function(check_compiler_flag RESULT FLAG)
	check_flag(result "${FLAG}" compiler)
	set(${RESULT} "${result}" PARENT_SCOPE)
endfunction(check_compiler_flag)

function(check_linker_flag RESULT FLAG)
	check_flag(result "${FLAG}" linker)
	set(${RESULT} "${result}" PARENT_SCOPE)
endfunction(check_linker_flag)

function(add_cxxflag FLAG)
	
	check_compiler_flag(RESULT "${FLAG}")
	
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${RESULT}" PARENT_SCOPE)
	
	if(NOT DEFINED RESULT OR RESULT STREQUAL "")
		set(FLAG_FOUND 0 PARENT_SCOPE)
	else()
		set(FLAG_FOUND 1 PARENT_SCOPE)
	endif()
	
endfunction(add_cxxflag)

function(add_ldflag FLAG)
	
	check_linker_flag(RESULT "${FLAG}")
	
	set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${RESULT}" PARENT_SCOPE)
	set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} ${RESULT}" PARENT_SCOPE)
	set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} ${RESULT}" PARENT_SCOPE)
	
	if(NOT DEFINED RESULT OR RESULT STREQUAL "")
		set(FLAG_FOUND 0 PARENT_SCOPE)
	else()
		set(FLAG_FOUND 1 PARENT_SCOPE)
	endif()
	
endfunction(add_ldflag)
```

## File: `cmake/CreateSourceGroups.cmake`
```

# Accepts a variable holding the source files
# and creates source groups (for VS, Xcode etc)
# that replicate the folder hierarchy on disk
function(create_source_groups source_files_variable)
	foreach(source_file ${${source_files_variable}})
		string( REPLACE ${CMAKE_CURRENT_SOURCE_DIR} "" relative_directory "${source_file}")
		string( REGEX REPLACE "[\\\\/][^\\\\/]*$" "" relative_directory "${relative_directory}")
		string( REGEX REPLACE "^[\\\\/]" "" relative_directory "${relative_directory}")
		if( WIN32 )
			string( REGEX REPLACE "/" "\\\\" relative_directory "${relative_directory}" )
		endif( WIN32 )
		source_group( "${relative_directory}" FILES ${source_file} )
	endforeach()
endfunction()
```

## File: `cmake/Doxygen.cmake`
```

# Copyright (C) 2011-2017 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

find_package(Doxygen)

include(VersionString)

# Add a target that runs Doxygen on a configured Doxyfile
#
# Parameters:
# - TARGET_NAME the name of the target to add
# - DOXYFILE_IN the raw Doxyfile
# - VERSION_FILE VERSION file to be used by version_file()
# - GIT_DIR .git directory to be used by version_file()
# - OUT_DIR Doxygen output directory
#
# For the exact syntax of config options in DOXYFILE_IN see the documentation of the
# configure_file() cmake command.
#
# Available variables are those provided by version_file() as well as
# DOXYGEN_OUTPUT_DIR, which is set to OUT_DIR.
#
function(add_doxygen_target TARGET_NAME DOXYFILE_IN VERSION_FILE GIT_DIR OUT_DIR)
	
	if(NOT DOXYGEN_EXECUTABLE)
		return()
	endif()
	
	set(doxyfile "${PROJECT_BINARY_DIR}/Doxyfile.${TARGET_NAME}")
	set(defines "-DDOXYGEN_OUTPUT_DIR=${OUT_DIR}")
	
	version_file("${DOXYFILE_IN}" "${doxyfile}" "${VERSION_FILE}" "${GIT_DIR}" "${defines}")
	
	add_custom_target(${TARGET_NAME}
		COMMAND "${CMAKE_COMMAND}" -E make_directory "${OUT_DIR}"
		COMMAND ${DOXYGEN_EXECUTABLE} "${doxyfile}"
		DEPENDS "${doxyfile}"
		WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
		COMMENT "Building doxygen documentation."
		VERBATIM
		SOURCES "${DOXYFILE_IN}"
	)
	
endfunction(add_doxygen_target)
```

## File: `cmake/FilterList.cmake`
```

# Copyright (C) 2013-2016 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

# Filter a list with conditional ites
#
# Supported syntax:
#
#  item
#
#  item if CONDITION_VARIABLE
#
#  CONDITION_VARIABLE {
#    item1
#    item2
#  }
#
# Conditions cannot be nested.
#
# The list specified by LIST_NAM Ewill be modifed in place.
# An optional second parameter can be given to specify the name of a list that
# should receive all items, even those whose conditions evaluated to false,
# but not syntactic elements such as 'if', '{', '}' and condition variables.
#
function(filter_list LIST_NAME)
	
	set(TOKEN_IF "if")
	set(TOKEN_GROUP_BEGIN "{")
	set(TOKEN_GROUP_END "}")
	
	set(filtered)
	set(all)
	
	# the item from the previous iteration
	set(last_item "")
	
	# current syntax state:
	# 0 - start
	# 1 - after 'if', expected condition variable
	# 2 - inside block (true)
	# 3 - inside block (false)
	set(mode 0)
	
	foreach(item IN LISTS ${LIST_NAME})
		
		if(mode EQUAL 1)
			
			# Handle condition variables
			set(condition ${${item}})
			if(condition)
				list(APPEND filtered ${last_item})
			endif()
			set(mode 0)
			set(last_item "")
			
		elseif(item STREQUAL TOKEN_IF)
			
			if(NOT mode EQUAL 0)
				message(FATAL_ERROR "bad filter_list syntax: IF inside { } block is forbidden")
			endif()
			
			# Handle condition start
			if(last_item STREQUAL "")
				message(FATAL_ERROR "bad filter_list syntax: IF without preceding item")
			endif()
			set(mode 1)
			
		elseif(item STREQUAL TOKEN_GROUP_BEGIN)
			
			if(NOT mode EQUAL 0)
				message(FATAL_ERROR "bad filter_list syntax: cannot nest { } blocks")
			endif()
			
			if(last_item STREQUAL "")
				message(FATAL_ERROR "bad filter_list syntax: { without preceding item")
			endif()
			
			set(condition ${${last_item}})
			if(condition)
				set(mode 2)
			else()
				set(mode 3)
			endif()
			set(last_item "")
			
		else()
			
			# Handle unconditional items
			if(NOT last_item STREQUAL "" AND NOT mode EQUAL 3)
				list(APPEND filtered ${last_item})
			endif()
			
			if(item STREQUAL TOKEN_GROUP_END)
				
				if(mode EQUAL 0)
					message(FATAL_ERROR "bad filter_list syntax: } without open block")
				endif()
				
				set(mode 0)
				set(last_item)
				
			else()
				
				list(APPEND all ${item})
				set(last_item ${item})
				
			endif()
			
		endif()
		
	endforeach()
	
	if(mode EQUAL 1)
		message(FATAL_ERROR "bad filter_list syntax: unexpected end, expected condition")
	elseif(mode EQUAL 2 OR mode EQUAL 3)
		message(FATAL_ERROR "bad filter_list syntax: unexpected end, expected }")
	endif()
	
	if(last_item)
		list(APPEND filtered ${last_item})
	endif()
	
	list(SORT filtered)
	list(REMOVE_DUPLICATES filtered)
	set(${LIST_NAME} ${filtered} PARENT_SCOPE)
	
	if(ARGC GREATER 1)
		list(SORT all)
		list(REMOVE_DUPLICATES all)
		set(${ARGV1} ${all} PARENT_SCOPE)
	endif()
	
endfunction()
```

## File: `cmake/FindLZMA.cmake`
```

# Copyright (C) 2011-2019 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

# Try to find the LZMA library and include path for lzma.h from xz-utils.
# Once done this will define
#
# LZMA_FOUND
# LZMA_INCLUDE_DIR   Where to find lzma.h
# LZMA_LIBRARIES     The liblzma library
# LZMA_DEFINITIONS   Definitions to use when compiling code that uses liblzma
#
# Typical usage could be something like:
#   find_package(LZMA REQUIRED)
#   include_directories(SYSTEM ${LZMA_INCLUDE_DIR})
#   add_definitions(${LZMA_DEFINITIONS})
#   ...
#   target_link_libraries(myexe ${LZMA_LIBRARIES})
#
# The following additional options can be defined before the find_package() call:
# LZMA_USE_STATIC_LIBS  Statically link against liblzma (default: OFF)

if(UNIX)
	find_package(PkgConfig QUIET)
	pkg_check_modules(_PC_LZMA liblzma)
endif()

include(UseStaticLibs)

foreach(static IN ITEMS 1 0)
	
	if(static)
		use_static_libs(LZMA _PC_LZMA)
	endif()
	
	find_path(LZMA_INCLUDE_DIR lzma.h
		HINTS
			${_PC_LZMA_INCLUDE_DIRS}
		DOC "The directory where lzma.h resides"
	)
	mark_as_advanced(LZMA_INCLUDE_DIR)
	
	# Prefer libraries in the same prefix as the include files
	string(REGEX REPLACE "(.*)/include/?" "\\1" LZMA_BASE_DIR ${LZMA_INCLUDE_DIR})
	
	find_library(LZMA_LIBRARY lzma liblzma
		PATHS
			${_PC_LZMA_LIBRARY_DIRS}
			"${LZMA_BASE_DIR}/lib"
		DOC "The LZMA library"
	)
	mark_as_advanced(LZMA_LIBRARY)
	
	if(static)
		use_static_libs_restore()
	endif()
	
	if(LZMA_LIBRARY OR STRICT_USE)
		break()
	endif()
	
endforeach()

set(LZMA_DEFINITIONS)
if(WIN32 AND LZMA_USE_STATIC_LIBS)
	set(LZMA_DEFINITIONS -DLZMA_API_STATIC)
endif()

# handle the QUIETLY and REQUIRED arguments and set LZMA_FOUND to TRUE if 
# all listed variables are TRUE
include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(LZMA DEFAULT_MSG LZMA_LIBRARY LZMA_INCLUDE_DIR)

if(LZMA_FOUND)
	set(LZMA_LIBRARIES ${LZMA_LIBRARY})
endif(LZMA_FOUND)
```

## File: `cmake/Findiconv.cmake`
```

# Copyright (C) 2012-2019 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

# Try to find the iconv library and include path for iconv.h.
# Once done this will define
#
# ICONV_FOUND
# iconv_INCLUDE_DIR   Where to find iconv.h
# iconv_LIBRARIES     The libiconv library or empty if none was found
# iconv_DEFINITIONS   Definitions to use when compiling code that uses iconv
#
# An empty iconv_LIBRARIES is not an error as iconv is often included in the system libc.
#
# Typical usage could be something like:
#   find_package(iconv REQUIRED)
#   include_directories(SYSTEM ${iconv_INCLUDE_DIR})
#   add_definitions(${iconv_DEFINITIONS})
#   ...
#   target_link_libraries(myexe ${iconv_LIBRARIES})
#
# The following additional options can be defined before the find_package() call:
# iconv_USE_STATIC_LIBS  Statically link against libiconv (default: OFF)

include(UseStaticLibs)

foreach(static IN ITEMS 1 0)
	
	if(static)
		use_static_libs(iconv)
	endif()
	
	if(APPLE)
		# Prefer local iconv.h location over the system iconv.h location as /opt/local/include
		# may be added to the include path by other libraries, resulting in the #include
		# statements finding the local copy while we will link agains the system lib.
		# This way we always find both include file and library in /opt/local/ if there is one.
		find_path(iconv_INCLUDE_DIR iconv.h
			PATHS /opt/local/include
			DOC "The directory where iconv.h resides"
			NO_CMAKE_SYSTEM_PATH
		)
	endif(APPLE)
	
	find_path(iconv_INCLUDE_DIR iconv.h
		PATHS /opt/local/include
		DOC "The directory where iconv.h resides"
	)
	mark_as_advanced(iconv_INCLUDE_DIR)
	
	# Prefer libraries in the same prefix as the include files
	string(REGEX REPLACE "(.*)/include/?" "\\1" iconv_BASE_DIR ${iconv_INCLUDE_DIR})
	
	find_library(iconv_LIBRARY iconv libiconv
		HINTS "${iconv_BASE_DIR}/lib"
		PATHS /opt/local/lib
		DOC "The iconv library"
	)
	mark_as_advanced(iconv_LIBRARY)
	
	if(static)
		use_static_libs_restore()
	endif()
	
	if(iconv_LIBRARY OR STRICT_USE)
		break()
	endif()
	
endforeach()

set(iconv_DEFINITIONS)
if(WIN32 AND iconv_USE_STATIC_LIBS)
	set(iconv_DEFINITIONS -DLIBICONV_STATIC -DUSING_STATIC_LIBICONV)
endif()

# handle the QUIETLY and REQUIRED arguments and set iconv_FOUND to TRUE if 
# all listed variables are TRUE
include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(iconv DEFAULT_MSG iconv_INCLUDE_DIR)

# For some reason, find_package_... uppercases it's first argument. Nice!
if(ICONV_FOUND)
	set(iconv_LIBRARIES)
	if(iconv_LIBRARY)
		list(APPEND iconv_LIBRARIES ${iconv_LIBRARY})
	endif()
endif(ICONV_FOUND)
```

## File: `cmake/PrintConfiguration.cmake`
```

# Copyright (C) 2013 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

function(print_configuration TITLE)
	
	set(str "")
	
	set(print_first 0)
	
	set(mode 0)
	
	foreach(arg IN LISTS ARGN)
		
		if(arg STREQUAL "FIRST")
			set(print_first 1)
		else()
			
			if(mode EQUAL 0)
				
				if(${arg})
					set(mode 1)
				else()
					set(mode 2)
				endif()
				
			else()
				
				if(mode EQUAL 1 AND NOT arg STREQUAL "")
					
					if(str STREQUAL "")
						set(str "${arg}")
					else()
						set(str "${str}, ${arg}")
					endif()
					
					if(print_first)
						break()
					endif()
					
				endif()
				
				set(mode 0)
				
			endif()
			
		endif()
		
	endforeach()
	
	if(str STREQUAL "")
		set(str "(none)")
	endif()
	
	message(" - ${TITLE}: ${str}")
	
endfunction()
```

## File: `cmake/StyleCheck.cmake`
```

# Copyright (C) 2013-2018 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

if(CMAKE_VERSION VERSION_LESS 3.12)
	find_package(PythonInterp)
	set(Python_Interpreter_FOUND ${PYTHONINTERP_FOUND})
	set(Python_EXECUTABLE ${PYTHON_EXECUTABLE})
else()
	find_package(Python COMPONENTS Interpreter)
endif()

set(STYLE_FILTER)

# Complains about any c-style cast -> too annoying.
set(STYLE_FILTER ${STYLE_FILTER},-readability/casting)

# Insists on including evrything in the .cpp file even if it is included in the header.
set(STYLE_FILTER ${STYLE_FILTER},-build/include_what_you_use)

# Too many false positives and not very helpful error messages.
set(STYLE_FILTER ${STYLE_FILTER},-build/include_order)

# No thanks.
set(STYLE_FILTER ${STYLE_FILTER},-readability/streams)

# Ugh!
set(STYLE_FILTER ${STYLE_FILTER},-whitespace/tab)

# Yes it is!
set(STYLE_FILTER ${STYLE_FILTER},-whitespace/blank_line)

# Suggessts excessive indentation.
set(STYLE_FILTER ${STYLE_FILTER},-whitespace/labels)

# Disallows brace on new line after long class memeber init list
set(STYLE_FILTER ${STYLE_FILTER},-whitespace/braces)

# Don't tell me how to name my variables.
set(STYLE_FILTER ${STYLE_FILTER},-runtime/arrays)

# Why?
set(STYLE_FILTER ${STYLE_FILTER},-whitespace/todo)
set(STYLE_FILTER ${STYLE_FILTER},-readability/todo)

# Annoyting to use with boost::program_options
set(STYLE_FILTER ${STYLE_FILTER},-whitespace/semicolon)

get_filename_component(STYLE_CHECK_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)
set(STYLE_CHECK_SCRIPT "${STYLE_CHECK_DIR}/cpplint.py")

# Add a target that runs cpplint.py
#
# Parameters:
# - TARGET_NAME the name of the target to add
# - SOURCES_LIST a complete list of source and include files to check
function(add_style_check_target TARGET_NAME SOURCES_LIST PROJECT)
	
	if(NOT Python_Interpreter_FOUND)
		return()
	endif()
	
	list(SORT SOURCES_LIST)
	list(REMOVE_DUPLICATES SOURCES_LIST)
	
	add_custom_target(${TARGET_NAME}
		COMMAND "${CMAKE_COMMAND}" -E chdir
			"${PROJECT_SOURCE_DIR}"
			"${Python_EXECUTABLE}"
			"${STYLE_CHECK_SCRIPT}"
			"--filter=${STYLE_FILTER}"
			"--project=${PROJECT}"
			${SOURCES_LIST}
		DEPENDS ${SOURCES_LIST} ${STYLE_CHECK_SCRIPT}
		COMMENT "Checking code style."
		VERBATIM
	)
	
endfunction(add_style_check_target)
```

## File: `cmake/UseStaticLibs.cmake`
```

# Copyright (C) 2013-2019 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

macro(use_static_libs ID)
	if(${ID}_USE_STATIC_LIBS)
		set(_UseStaticLibs_ORIG_CMAKE_FIND_LIBRARY_SUFFIXES ${CMAKE_FIND_LIBRARY_SUFFIXES})
		if(WIN32)
			set(CMAKE_FIND_LIBRARY_SUFFIXES _a.lib .lib .a)
		else()
			set(CMAKE_FIND_LIBRARY_SUFFIXES .a)
		endif()
		if(ARGC GREATER 1)
			set(prefix "${ARGV1}")
			set(${prefix}_LIBRARIES     "${${prefix}_STATIC_LIBRARIES}")
			set(${prefix}_LIBRARY_DIRS  "${${prefix}_STATIC_LIBRARY_DIRS}")
			set(${prefix}_LDFLAGS       "${${prefix}_STATIC_LDFLAGS}")
			set(${prefix}_LDFLAGS_OTHER "${${prefix}_STATIC_LDFLAGS_OTHER}")
			set(${prefix}_INCLUDE_DIRS  "${${prefix}_STATIC_INCLUDE_DIRS}")
			set(${prefix}_CFLAGS        "${${prefix}_STATIC_CFLAGS}")
			set(${prefix}_CFLAGS_OTHER  "${${prefix}_STATIC_CFLAGS_OTHER}")
		endif()
	endif()
endmacro()

macro(use_static_libs_restore)
	if(DEFINED _UseStaticLibs_ORIG_CMAKE_FIND_LIBRARY_SUFFIXES)
		set(CMAKE_FIND_LIBRARY_SUFFIXES ${_UseStaticLibs_ORIG_CMAKE_FIND_LIBRARY_SUFFIXES})
		unset(_UseStaticLibs_ORIG_CMAKE_FIND_LIBRARY_SUFFIXES)
	endif()
endmacro()

macro(has_static_libs PREFIX LIBS)
	if(WIN32)
		# On Windows we can't really tell import libraries from proper static libraries.
		set(${PREFIX}_HAS_STATIC_LIBS ${${PREFIX}_USE_STATIC_LIBS})
	else()
		set(${PREFIX}_HAS_STATIC_LIBS 0)
		foreach(lib IN LISTS ${LIBS})
			if(TARGET ${lib})
				get_target_property(target_type ${lib} TYPE)
				if(target_type STREQUAL STATIC_LIBRARY)
					set(${PREFIX}_HAS_STATIC_LIBS 1)
					break()
				endif()
			endif()
			if(lib MATCHES "\\.a$")
				set(${PREFIX}_HAS_STATIC_LIBS 1)
				break()
			endif()
		endforeach()
	endif()
endmacro()
```

## File: `cmake/VersionScript.cmake`
```

# Copyright (C) 2011-2020 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

cmake_minimum_required(VERSION 2.8...3.19)

# CMake script that reads a VERSION file and the current git history and the calls configure_file().
# This is used by version_file() in VersionString.cmake

if((NOT DEFINED INPUT) OR (NOT DEFINED OUTPUT) OR (NOT DEFINED VERSION_SOURCES) OR (NOT DEFINED GIT_DIR))
	message(SEND_ERROR "Invalid arguments.")
endif()

get_filename_component(VERSION_SCRIPT_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)
include("${VERSION_SCRIPT_DIR}/VersionString.cmake")

# configure_file doesn't handle newlines correctly - pre-escape variables
macro(_version_escape var string)
	# Escape the escape character and quotes
	string(REGEX REPLACE "([\\\\\"])" "\\\\\\1" ${var} "${string}")
	# Pull newlines out of string
	string(REGEX REPLACE "\n" "\\\\n\"\n\t\"" ${var} "${${var}}")
endmacro()

set(var "")
foreach(arg IN LISTS VERSION_SOURCES)
	if(var STREQUAL "")
		set(var ${arg})
	else()
		parse_version_file(${var} "${arg}" ON)
		set(var "")
	endif()
endforeach()

# Check for a git directory and fill in the git commit hash if one exists.
unset(GIT_COMMIT)
if(NOT GIT_DIR STREQUAL "")
	
	unset(git_head)
	
	if(GIT_COMMAND)
		execute_process(
			COMMAND "${GIT_COMMAND}" "--git-dir=${GIT_DIR}" "rev-parse" "HEAD"
			RESULT_VARIABLE result
			OUTPUT_VARIABLE git_head
		)
		if(NOT "${result}" EQUAL 0)
			unset(git_head)
		endif()
	endif()
	
	if(NOT git_head AND EXISTS "${GIT_DIR}/HEAD")
		
		file(READ "${GIT_DIR}/HEAD" git_head)
		
		if(git_head MATCHES "^[ \t\r\n]*ref\\:(.*)$")
			
			# Remove the first for characters from git_head to get git_ref.
			# We can't use a length of -1 for string(SUBSTRING) as cmake < 2.8.5 doesn't support it.
			string(LENGTH "${git_head}" git_head_length)
			math(EXPR git_ref_length "${git_head_length} - 4")
			string(SUBSTRING "${git_head}" 4 ${git_ref_length} git_ref)
			string(STRIP "${git_ref}" git_ref)
			
			unset(git_head)
			if(EXISTS "${GIT_DIR}/${git_ref}")
				file(READ "${GIT_DIR}/${git_ref}" git_head)
			elseif(EXISTS "${GIT_DIR}/packed-refs")
				file(READ "${GIT_DIR}/packed-refs" git_refs)
				string(REGEX REPLACE "[^0-9A-Za-z]" "\\\\\\0" git_ref "${git_ref}")
				string(REGEX MATCH "[^\r\n]* ${git_ref}( [^\r\n])?" git_head "${git_refs}")
			endif()
			
		endif()
		
	endif()
	
	# Create variables for all prefixes of the git comit ID.
	string(REGEX MATCH "[0-9A-Za-z]+" git_commit "${git_head}")
	string(LENGTH "${git_commit}" git_commit_length)
	if(NOT git_commit_length LESS 40)
		string(TOLOWER "${git_commit}" GIT_COMMIT)
		foreach(i RANGE 20)
			string(SUBSTRING "${GIT_COMMIT}" 0 ${i} GIT_COMMIT_PREFIX_${i})
			set(GIT_SUFFIX_${i} " + ${GIT_COMMIT_PREFIX_${i}}")
		endforeach()
	else()
		message(WARNING "Git repository detected, but could not determine HEAD")
	endif()
	
endif()

configure_file("${INPUT}" "${OUTPUT}")
```

## File: `cmake/VersionString.cmake`
```

# Copyright (C) 2011-2020 Daniel Scharrer
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the author(s) be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

get_filename_component(VERSION_SCRIPT_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)
set(VERSION_STRING_SCRIPT "${VERSION_SCRIPT_DIR}/VersionScript.cmake")

# Create a rule to generate a version string at compile time.
#
# An optional fifth argument can be used to add additional cmake defines.
#
# SRC is processed using the configure_file() cmake command
# at build to produce DST with the following variable available:
#
# VERSION_SOURCES:
#  List of (${var} ${file}) pairs.
#
# for each variable ${var}
# - ${var}: The contents of the associated file
# - ${var}_COUNT: Number of lines in the associated file
# - For each line ${i}:
#   - ${var}_${i}: The ${i}-th line of the associated file
#    - ${var}_${i}_PREFIX: The first component in the line
#    - ${var}_${i}_LINE: Everything except the first component of the line
#    - ${var}_${i}_NAME: Everything except the last component of the line
#    - ${var}_${i}_STRING: The last component (excluding optional suffix) of the line
#    - ${var}_${i}_SUFFIX: Suffix (separated by " + ") of the line
#    - ${var}_${i}_MAJOR: First version component in ${var}_${i}_STRING
#    - ${var}_${i}_MINOR: Second version component in ${var}_${i}_STRING
#    - ${var}_${i}_PATCH: Third version component in ${var}_${i}_STRING
#    - ${var}_${i}_BUILD: Fourth version component in ${var}_${i}_STRING
#    - ${var}_${i}_NUMBER: Reassembled verion components
#    - ${var}_${i}_PRERELEASE: If the version indicates a prerelease build
#    - ${var}_${i}_PRIVATE: If the version indicates a private build
# - ${var}_HEAD: The first paragraph of the associated file
# - ${var}_TAIL: The remaining paragraphs of the associated file
#
# - GIT_COMMIT: The current git commit. (not defined if there is no GIT_DIR directory)
# - GIT_COMMIT_PREFIX_${i}: The first ${i} characters of GIT_COMMIT (i=0..39)
# For the exact syntax of SRC see the documentation of the configure_file() cmake command.
# The version file is regenerated whenever VERSION_FILE or the current commit changes.
function(version_file SRC DST VERSION_SOURCES GIT_DIR)
	
	set(MODE_VARIABLE 0)
	set(MODE_FILE 1)
	
	set(mode ${MODE_VARIABLE})
	
	set(args)
	set(dependencies "${VERSION_STRING_SCRIPT}")
	
	foreach(arg IN LISTS VERSION_SOURCES)
		
		if(mode EQUAL MODE_VARIABLE)
			set(mode ${MODE_FILE})
		else()
			get_filename_component(arg "${arg}" ABSOLUTE)
			list(APPEND dependencies ${arg})
			set(mode ${MODE_VARIABLE})
		endif()
		
		list(APPEND args ${arg})
		
	endforeach()
	
	get_filename_component(abs_src "${SRC}" ABSOLUTE)
	get_filename_component(abs_dst "${DST}" ABSOLUTE)
	get_filename_component(abs_git_dir "${GIT_DIR}" ABSOLUTE)
	
	set(defines)
	if(ARGC GREATER 4)
		set(defines ${ARGV4})
	endif()
	
	if(EXISTS "${abs_git_dir}")
		find_program(GIT_COMMAND git)
		if(GIT_COMMAND)
			list(APPEND dependencies "${GIT_COMMAND}")
		endif()
		if(EXISTS "${abs_git_dir}/HEAD")
			list(APPEND dependencies "${abs_git_dir}/HEAD")
		endif()
		if(EXISTS "${abs_git_dir}/packed-refs")
			list(APPEND dependencies "${abs_git_dir}/packed-refs")
		endif()
		if(EXISTS "${abs_git_dir}/logs/HEAD")
			list(APPEND dependencies "${abs_git_dir}/logs/HEAD")
		endif()
	else()
		set(abs_git_dir "")
	endif()
	
	add_custom_command(
		OUTPUT
			"${abs_dst}"
		COMMAND
			${CMAKE_COMMAND}
			"-DINPUT=${abs_src}"
			"-DOUTPUT=${abs_dst}"
			"-DVERSION_SOURCES=${args}"
			"-DGIT_DIR=${abs_git_dir}"
			"-DGIT_COMMAND=${GIT_COMMAND}"
			${defines}
			-P "${VERSION_STRING_SCRIPT}"
		COMMAND
			${CMAKE_COMMAND} -E touch "${abs_dst}"
		MAIN_DEPENDENCY
			"${abs_src}"
		DEPENDS
			${dependencies}
		COMMENT ""
		VERBATIM
	)
	
endfunction()

macro(_version_escape var string)
	set(${var} "${string}")
endmacro()

macro(_define_version_var_nostrip suffix contents)
	_version_escape(${var}_${suffix} "${${contents}}")
	list(APPEND variables ${var}_${suffix})
endmacro()

macro(_define_version_var suffix contents)
	string(STRIP "${${contents}}" tmp)
	_define_version_var_nostrip(${suffix} tmp)
endmacro()

macro(_define_version_line_var_nostrip suffix contents)
	_define_version_var_nostrip(${i}_${suffix} ${contents})
	if(line_name)
		set(${line_name}_${suffix} "${${var}_${i}_${suffix}}")
		list(APPEND variables ${line_name}_${suffix})
	endif()
endmacro()

macro(_define_version_line_var suffix contents)
	string(STRIP "${${contents}}" tmp)
	_define_version_line_var_nostrip(${suffix} tmp)
endmacro()

function(parse_version_file names file)
	
	list(GET names 0 var)
	
	list(LENGTH names names_count)
	
	set(variables)
	
	file(READ "${file}" contents)
	string(STRIP "${contents}" contents)
	string(REGEX REPLACE "\r\n" "\n" contents "${contents}")
	string(REGEX REPLACE "\r" "\n" contents "${contents}")
	_version_escape(${var} "${contents}")
	list(APPEND variables ${var})
	
	# Split the version file into lines.
	string(REGEX MATCHALL "[^\r\n]+" lines "${contents}")
	set(i 0)
	foreach(line IN LISTS lines)
		
		if(i LESS names_count)
			list(GET names ${i} line_name)
		else()
			set(line_name)
		endif()
		
		_define_version_var(${i} line)
		
		if(line MATCHES "^([^ ]*) (.*)$")
			set(prefix "${CMAKE_MATCH_1}")
			set(notprefix "${CMAKE_MATCH_2}")
			_define_version_line_var(PREFIX prefix)
			_define_version_line_var(LINE notprefix)
		else()
			_define_version_line_var(PREFIX line)
		endif()
		
		if(line MATCHES "^(.*[^+] )?([^ ]+)( \\+ [^ ]+)?$")
			
			set(name "${CMAKE_MATCH_1}")
			set(string "${CMAKE_MATCH_2}")
			set(suffix "${CMAKE_MATCH_3}")
			
			_define_version_line_var(NAME name)
			_define_version_line_var(STRING string)
			_define_version_line_var_nostrip(SUFFIX suffix)
			
			if(i GREATER 0 AND line_name)
				set(${line_name} "${${var}_${i}_STRING}")
				list(APPEND variables ${line_name})
			endif()
			
			if(string MATCHES "^([0-9]+)(\\.([0-9]+)(\\.([0-9]+)(\\.([0-9]+))?)?)?(.*)?$")
				
				set(major "${CMAKE_MATCH_1}")
				set(minor "${CMAKE_MATCH_3}")
				set(patch "${CMAKE_MATCH_5}")
				set(build "${CMAKE_MATCH_7}")
				set(release "${CMAKE_MATCH_8}")
				
				set(error 0)
				set(newpatch)
				set(newbuild)
				set(prerelease 0)
				set(private 0)
				if(release MATCHES "^\\-dev\\-([2-9][0-9][0-9][0-9]+)\\-([0-9][0-9])\\-([0-9][0-9])$")
					set(prerelease 1)
					set(newpatch "${CMAKE_MATCH_1}")
					set(newbuild "${CMAKE_MATCH_2}${CMAKE_MATCH_3}")
				elseif(release MATCHES "^\\-rc([0-9]+)$")
					set(prerelease 1)
					set(newpatch "9999")
					set(newbuild "${CMAKE_MATCH_1}")
				elseif(release MATCHES "^\\-r([0-9]+)$")
					if(build STREQUAL "")
						set(build "${CMAKE_MATCH_1}")
					else()
						set(error 1)
					endif()
				elseif(release OR suffix)
					set(prerelease 1)
					set(private 1)
					set(newpatch 9999)
					set(newbuild 9999)
				endif()
				
				foreach(component IN ITEMS major minor patch build newpatch newbuild)
					string(REGEX REPLACE "^0+" "" ${component} "${${component}}")
					if(NOT ${component})
						set(${component} 0)
					endif()
				endforeach()
				
				if(newpatch)
					set(prerelease 1)
					if(build)
						set(error 1)
					else()
						if(patch)
							if(newpatch EQUAL 9999)
								math(EXPR patch "${patch} - 1")
								if(newbuild EQUAL 9999)
									set(build 9999)
								else()
									math(EXPR build "${newbuild} + 1000")
								endif()
							else()
								set(error 1)
							endif()
						else()
							if(minor)
								math(EXPR minor "${minor} - 1")
							else()
								if(major)
									math(EXPR major "${major} - 1")
								else()
									set(error 1)
								endif()
								set(minor 9999)
							endif()
							set(patch "${newpatch}")
							set(build "${newbuild}")
						endif()
					endif()
				endif()
				
				set(number "${major}")
				if(minor OR patch OR build)
					set(number "${number}.${minor}")
					if(patch OR build)
						set(number "${number}.${patch}")
						if(build)
							set(number "${number}.${build}")
						endif()
					endif()
				endif()
				
				_define_version_line_var(MAJOR major)
				_define_version_line_var(MINOR minor)
				_define_version_line_var(PATCH patch)
				_define_version_line_var(BUILD build)
				_define_version_line_var(PRERELEASE prerelease)
				_define_version_line_var(PRIVATE private)
				_define_version_line_var(NUMBER number)
				_define_version_line_var(ERROR error)
				
			endif()
			
		endif()
		
		math(EXPR i "${i} + 1")
	endforeach()
	
	set(${var}_COUNT ${i} PARENT_SCOPE)
	
	string(REGEX REPLACE "\n\n.*$" "" head "${contents}")
	_define_version_var(HEAD head)
	
	string(REGEX MATCH "\n\n.*" tail "${contents}")
	_define_version_var(TAIL tail)
	
	foreach(var IN LISTS variables)
		set(${var} "${${var}}" PARENT_SCOPE)
	endforeach()
	
endfunction()
```

## File: `cmake/cpplint.py`
```python
#!/usr/bin/env python
#
# Note: this file has been adjusted to fit the innoextract project:
#  - adjusted include guard style
#  - hacked so that build/include doesn't complain about #include "Configure.h" lines
#  - Allow lines that are only whitespace.
#  - Remove 80-char line limit, keep 100 char limit.
#  - No space after if et al.
#  - Warn if a tab follows a non-tab character.
#  - Don't require two spaces between code and comments
#  - Warn if spaces are used for identation.
#  - Allow //! and //!< comments
#  - Allow struct name { typedef a type; }; one-liners
#  - Allow #ifdef BOOST_PP_IS_ITERATING + #endif in place of header guards
#  - C++ source files are named .cpp, not .cc
#
# Copyright (c) 2011-2018 Daniel Scharrer
# Copyright (c) 2009 Google Inc. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#    * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Here are some issues that I've had people identify in my code during reviews,
# that I think are possible to flag automatically in a lint tool.  If these were
# caught by lint, it would save time both for myself and that of my reviewers.
# Most likely, some of these are beyond the scope of the current lint framework,
# but I think it is valuable to retain these wish-list items even if they cannot
# be immediately implemented.
#
#  Suggestions
#  -----------
#  - Check for no 'explicit' for multi-arg ctor
#  - Check for boolean assign RHS in parens
#  - Check for ctor initializer-list colon position and spacing
#  - Check that if there's a ctor, there should be a dtor
#  - Check accessors that return non-pointer member variables are
#    declared const
#  - Check accessors that return non-const pointer member vars are
#    *not* declared const
#  - Check for using public includes for testing
#  - Check for spaces between brackets in one-line inline method
#  - Check for no assert()
#  - Check for spaces surrounding operators
#  - Check for 0 in pointer context (should be NULL)
#  - Check for 0 in char context (should be '\0')
#  - Check for camel-case method name conventions for methods
#    that are not simple inline getters and setters
#  - Check that base classes have virtual destructors
#    put "  // namespace" after } that closes a namespace, with
#    namespace's name after 'namespace' if it is named.
#  - Do not indent namespace contents
#  - Avoid inlining non-trivial constructors in header files
#    include base/basictypes.h if DISALLOW_EVIL_CONSTRUCTORS is used
#  - Check for old-school (void) cast for call-sites of functions
#    ignored return value
#  - Check gUnit usage of anonymous namespace
#  - Check for class declaration order (typedefs, consts, enums,
#    ctor(s?), dtor, friend declarations, methods, member vars)
#

"""Does google-lint on c++ files.

The goal of this script is to identify places in the code that *may*
be in non-compliance with google style.  It does not attempt to fix
up these problems -- the point is to educate.  It does also not
attempt to find all problems, or to ensure that everything it does
find is legitimately a problem.

In particular, we can get very confused by /* and // inside strings!
We do a small hack, which is to ignore //'s with "'s after them on the
same line, but it is far from perfect (in either direction).
"""

import codecs
import getopt
import math  # for log
import os
import re
import string
import sys
import unicodedata

try:
    import re._compiler as sre_compile
except ImportError:  # Python < 3.11
    import sre_compile

EXTENSIONS = ['c', 'cc', 'cpp', 'cxx', 'c++',
              'h', 'hpp', 'hxx', 'h++']

HEADER_EXTENSIONS = ['h', 'hpp', 'hxx', 'h++']

_USAGE = """
Syntax: cpplint.py [--verbose=#] [--output=vs7] [--filter=-x,+y,...]
                   [--counting=total|toplevel|detailed]
                   [--project=name]
        <file> [file] ...

  The style guidelines this tries to follow are those in
    http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml

  Every problem is given a confidence score from 1-5, with 5 meaning we are
  certain of the problem, and 1 meaning it could be a legitimate construct.
  This will miss some errors, and is not a substitute for a code review.

  To suppress false-positive errors of a certain category, add a
  'NOLINT(category)' comment to the line.  NOLINT or NOLINT(*)
  suppresses errors of all categories on that line.

  The files passed in will be linted; at least one file must be provided.
  Linted extensions are %s.  Other file types will be ignored.

  Flags:

    output=vs7
      By default, the output is formatted to ease emacs parsing.  Visual Studio
      compatible output (vs7) may also be used.  Other formats are unsupported.

    project=name
      Project name to use as include guard prefix.

    verbose=#
      Specify a number 0-5 to restrict errors to certain verbosity levels.

    filter=-x,+y,...
      Specify a comma-separated list of category-filters to apply: only
      error messages whose category names pass the filters will be printed.
      (Category names are printed with the message and look like
      "[whitespace/indent]".)  Filters are evaluated left to right.
      "-FOO" and "FOO" means "do not print categories that start with FOO".
      "+FOO" means "do print categories that start with FOO".

      Examples: --filter=-whitespace,+whitespace/braces
                --filter=whitespace,runtime/printf,+runtime/printf_format
                --filter=-,+build/include_what_you_use

      To see a list of all the categories used in cpplint, pass no arg:
         --filter=

    counting=total|toplevel|detailed
      The total number of errors found is always printed. If
      'toplevel' is provided, then the count of errors in each of
      the top-level categories like 'build' and 'whitespace' will
      also be printed. If 'detailed' is provided, then a count
      is provided for each category like 'build/class'.
""" % (EXTENSIONS)

# We categorize each error message we print.  Here are the categories.
# We want an explicit list so we can list them all in cpplint --filter=.
# If you add a new error message with a new category, add it to the list
# here!  cpplint_unittest.py should tell you if you forget to do this.
# \ used for clearer layout -- pylint: disable-msg=C6013
_ERROR_CATEGORIES = [
  'build/class',
  'build/deprecated',
  'build/endif_comment',
  'build/explicit_make_pair',
  'build/forward_decl',
  'build/header_guard',
  'build/include',
  'build/include_alpha',
  'build/include_order',
  'build/include_what_you_use',
  'build/namespaces',
  'build/printf_format',
  'build/storage_class',
  'legal/copyright',
  'readability/braces',
  'readability/casting',
  'readability/check',
  'readability/constructors',
  'readability/fn_size',
  'readability/function',
  'readability/multiline_comment',
  'readability/multiline_string',
  'readability/nolint',
  'readability/streams',
  'readability/todo',
  'readability/utf8',
  'runtime/arrays',
  'runtime/casting',
  'runtime/explicit',
  'runtime/int',
  'runtime/init',
  'runtime/invalid_increment',
  'runtime/member_string_references',
  'runtime/memset',
  'runtime/operator',
  'runtime/printf',
  'runtime/printf_format',
  'runtime/references',
  'runtime/rtti',
  'runtime/sizeof',
  'runtime/string',
  'runtime/threadsafe_fn',
  'runtime/virtual',
  'whitespace/align_tab'
  'whitespace/blank_line',
  'whitespace/braces',
  'whitespace/carriage-return',
  'whitespace/comma',
  'whitespace/comments',
  'whitespace/end_of_line',
  'whitespace/ending_newline',
  'whitespace/indent',
  'whitespace/ident_space',
  'whitespace/labels',
  'whitespace/line_length',
  'whitespace/newline',
  'whitespace/operators',
  'whitespace/templates',
  'whitespace/parens',
  'whitespace/semicolon',
  'whitespace/tab',
  'whitespace/todo'
  ]

# The default state of the category filter. This is overrided by the --filter=
# flag. By default all errors are on, so only add here categories that should be
# off by default (i.e., categories that must be enabled by the --filter= flags).
# All entries here should start with a '-' or '+', as in the --filter= flag.
_DEFAULT_FILTERS = ['-build/include_alpha']

# We used to check for high-bit characters, but after much discussion we
# decided those were OK, as long as they were in UTF-8 and didn't represent
# hard-coded international strings, which belong in a separate i18n file.

# Headers that we consider STL headers.
_STL_HEADERS = frozenset([
    'algobase.h', 'algorithm', 'alloc.h', 'bitset', 'deque', 'exception',
    'function.h', 'functional', 'hash_map', 'hash_map.h', 'hash_set',
    'hash_set.h', 'iterator', 'list', 'list.h', 'map', 'memory', 'new',
    'pair.h', 'pthread_alloc', 'queue', 'set', 'set.h', 'sstream', 'stack',
    'stl_alloc.h', 'stl_relops.h', 'type_traits.h',
    'utility', 'vector', 'vector.h',
    ])


# Non-STL C++ system headers.
_CPP_HEADERS = frozenset([
    'algo.h', 'builtinbuf.h', 'bvector.h', 'cassert', 'cctype',
    'cerrno', 'cfloat', 'ciso646', 'climits', 'clocale', 'cmath',
    'complex', 'complex.h', 'csetjmp', 'csignal', 'cstdarg', 'cstddef',
    'cstdio', 'cstdlib', 'cstring', 'ctime', 'cwchar', 'cwctype',
    'defalloc.h', 'deque.h', 'editbuf.h', 'exception', 'fstream',
    'fstream.h', 'hashtable.h', 'heap.h', 'indstream.h', 'iomanip',
    'iomanip.h', 'ios', 'iosfwd', 'iostream', 'iostream.h', 'istream',
    'istream.h', 'iterator.h', 'limits', 'map.h', 'multimap.h', 'multiset.h',
    'numeric', 'ostream', 'ostream.h', 'parsestream.h', 'pfstream.h',
    'PlotFile.h', 'procbuf.h', 'pthread_alloc.h', 'rope', 'rope.h',
    'ropeimpl.h', 'SFile.h', 'slist', 'slist.h', 'stack.h', 'stdexcept',
    'stdiostream.h', 'streambuf.h', 'stream.h', 'strfile.h', 'string',
    'strstream', 'strstream.h', 'tempbuf.h', 'tree.h', 'typeinfo', 'valarray',
    ])


# Assertion macros.  These are defined in base/logging.h and
# testing/base/gunit.h.  Note that the _M versions need to come first
# for substring matching to work.
_CHECK_MACROS = [
    'DCHECK', 'CHECK',
    'EXPECT_TRUE_M', 'EXPECT_TRUE',
    'ASSERT_TRUE_M', 'ASSERT_TRUE',
    'EXPECT_FALSE_M', 'EXPECT_FALSE',
    'ASSERT_FALSE_M', 'ASSERT_FALSE',
    ]

# Replacement macros for CHECK/DCHECK/EXPECT_TRUE/EXPECT_FALSE
_CHECK_REPLACEMENT = dict([(m, {}) for m in _CHECK_MACROS])

for op, replacement in [('==', 'EQ'), ('!=', 'NE'),
                        ('>=', 'GE'), ('>', 'GT'),
                        ('<=', 'LE'), ('<', 'LT')]:
  _CHECK_REPLACEMENT['DCHECK'][op] = 'DCHECK_%s' % replacement
  _CHECK_REPLACEMENT['CHECK'][op] = 'CHECK_%s' % replacement
  _CHECK_REPLACEMENT['EXPECT_TRUE'][op] = 'EXPECT_%s' % replacement
  _CHECK_REPLACEMENT['ASSERT_TRUE'][op] = 'ASSERT_%s' % replacement
  _CHECK_REPLACEMENT['EXPECT_TRUE_M'][op] = 'EXPECT_%s_M' % replacement
  _CHECK_REPLACEMENT['ASSERT_TRUE_M'][op] = 'ASSERT_%s_M' % replacement

for op, inv_replacement in [('==', 'NE'), ('!=', 'EQ'),
                            ('>=', 'LT'), ('>', 'LE'),
                            ('<=', 'GT'), ('<', 'GE')]:
  _CHECK_REPLACEMENT['EXPECT_FALSE'][op] = 'EXPECT_%s' % inv_replacement
  _CHECK_REPLACEMENT['ASSERT_FALSE'][op] = 'ASSERT_%s' % inv_replacement
  _CHECK_REPLACEMENT['EXPECT_FALSE_M'][op] = 'EXPECT_%s_M' % inv_replacement
  _CHECK_REPLACEMENT['ASSERT_FALSE_M'][op] = 'ASSERT_%s_M' % inv_replacement


# These constants define types of headers for use with
# _IncludeState.CheckNextIncludeOrder().
_C_SYS_HEADER = 1
_CPP_SYS_HEADER = 2
_LIKELY_MY_HEADER = 3
_POSSIBLE_MY_HEADER = 4
_OTHER_HEADER = 5


_regexp_compile_cache = {}

# Finds occurrences of NOLINT or NOLINT(...).
_RE_SUPPRESSION = re.compile(r'\bNOLINT\b(\([^)]*\))?')

# {str, set(int)}: a map from error categories to sets of linenumbers
# on which those errors are expected and should be suppressed.
_error_suppressions = {}


if sys.version_info < (3,):
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
    TEXT_TYPE = unicode
    # BINARY_TYPE = str
    range = xrange
    itervalues = dict.itervalues
    iteritems = dict.iteritems
else:
    def u(x):
        return x
    TEXT_TYPE = str
    # BINARY_TYPE = bytes
    itervalues = dict.values
    iteritems = dict.items

def ParseNolintSuppressions(filename, raw_line, linenum, error):
  """Updates the global list of error-suppressions.

  Parses any NOLINT comments on the current line, updating the global
  error_suppressions store.  Reports an error if the NOLINT comment
  was malformed.

  Args:
    filename: str, the name of the input file.
    raw_line: str, the line of input text, with comments.
    linenum: int, the number of the current line.
    error: function, an error handler.
  """
  # FIXME(adonovan): "NOLINT(" is misparsed as NOLINT(*).
  matched = _RE_SUPPRESSION.search(raw_line)
  if matched:
    category = matched.group(1)
    if category in (None, '(*)'):  # => "suppress all"
      _error_suppressions.setdefault(None, set()).add(linenum)
    else:
      if category.startswith('(') and category.endswith(')'):
        category = category[1:-1]
        if category in _ERROR_CATEGORIES:
          _error_suppressions.setdefault(category, set()).add(linenum)
        else:
          error(filename, linenum, 'readability/nolint', 5,
                'Unknown NOLINT error category: %s' % category)


def ResetNolintSuppressions():
  "Resets the set of NOLINT suppressions to empty."
  _error_suppressions.clear()


def IsErrorSuppressedByNolint(category, linenum):
  """Returns true if the specified error category is suppressed on this line.

  Consults the global error_suppressions map populated by
  ParseNolintSuppressions/ResetNolintSuppressions.

  Args:
    category: str, the category of the error.
    linenum: int, the current line number.
  Returns:
    bool, True iff the error should be suppressed due to a NOLINT comment.
  """
  return (linenum in _error_suppressions.get(category, set()) or
          linenum in _error_suppressions.get(None, set()))

def Match(pattern, s):
  """Matches the string with the pattern, caching the compiled regexp."""
  # The regexp compilation caching is inlined in both Match and Search for
  # performance reasons; factoring it out into a separate function turns out
  # to be noticeably expensive.
  if not pattern in _regexp_compile_cache:
    _regexp_compile_cache[pattern] = sre_compile.compile(pattern)
  return _regexp_compile_cache[pattern].match(s)


def Search(pattern, s):
  """Searches the string for the pattern, caching the compiled regexp."""
  if not pattern in _regexp_compile_cache:
    _regexp_compile_cache[pattern] = sre_compile.compile(pattern)
  return _regexp_compile_cache[pattern].search(s)


class _IncludeState(dict):
  """Tracks line numbers for includes, and the order in which includes appear.

  As a dict, an _IncludeState object serves as a mapping between include
  filename and line number on which that file was included.

  Call CheckNextIncludeOrder() once for each header in the file, passing
  in the type constants defined above. Calls in an illegal order will
  raise an _IncludeError with an appropriate error message.

  """
  # self._section will move monotonically through this set. If it ever
  # needs to move backwards, CheckNextIncludeOrder will raise an error.
  _INITIAL_SECTION = 0
  _MY_H_SECTION = 1
  _C_SECTION = 2
  _CPP_SECTION = 3
  _OTHER_H_SECTION = 4

  _TYPE_NAMES = {
      _C_SYS_HEADER: 'C system header',
      _CPP_SYS_HEADER: 'C++ system header',
      _LIKELY_MY_HEADER: 'header this file implements',
      _POSSIBLE_MY_HEADER: 'header this file may implement',
      _OTHER_HEADER: 'other header',
      }
  _SECTION_NAMES = {
      _INITIAL_SECTION: "... nothing. (This can't be an error.)",
      _MY_H_SECTION: 'a header this file implements',
      _C_SECTION: 'C system header',
      _CPP_SECTION: 'C++ system header',
      _OTHER_H_SECTION: 'other header',
      }

  def __init__(self):
    dict.__init__(self)
    # The name of the current section.
    self._section = self._INITIAL_SECTION
    # The path of last found header.
    self._last_header = ''

  def CanonicalizeAlphabeticalOrder(self, header_path):
    """Returns a path canonicalized for alphabetical comparison.

    - replaces "-" with "_" so they both cmp the same.
    - removes '-inl' since we don't require them to be after the main header.
    - lowercase everything, just in case.

    Args:
      header_path: Path to be canonicalized.

    Returns:
      Canonicalized path.
    """
    return header_path.replace('-inl.h', '.h').replace('-', '_').lower()

  def IsInAlphabeticalOrder(self, header_path):
    """Check if a header is in alphabetical order with the previous header.

    Args:
      header_path: Header to be checked.

    Returns:
      Returns true if the header is in alphabetical order.
    """
    canonical_header = self.CanonicalizeAlphabeticalOrder(header_path)
    if self._last_header > canonical_header:
      return False
    self._last_header = canonical_header
    return True

  def CheckNextIncludeOrder(self, header_type):
    """Returns a non-empty error message if the next header is out of order.

    This function also updates the internal state to be ready to check
    the next include.

    Args:
      header_type: One of the _XXX_HEADER constants defined above.

    Returns:
      The empty string if the header is in the right order, or an
      error message describing what's wrong.

    """
    error_message = ('Found %s after %s' %
                     (self._TYPE_NAMES[header_type],
                      self._SECTION_NAMES[self._section]))

    last_section = self._section

    if header_type == _C_SYS_HEADER:
      if self._section <= self._C_SECTION:
        self._section = self._C_SECTION
      else:
        self._last_header = ''
        return error_message
    elif header_type == _CPP_SYS_HEADER:
      if self._section <= self._CPP_SECTION:
        self._section = self._CPP_SECTION
      else:
        self._last_header = ''
        return error_message
    elif header_type == _LIKELY_MY_HEADER:
      if self._section <= self._MY_H_SECTION:
        self._section = self._MY_H_SECTION
      else:
        self._section = self._OTHER_H_SECTION
    elif header_type == _POSSIBLE_MY_HEADER:
      if self._section <= self._MY_H_SECTION:
        self._section = self._MY_H_SECTION
      else:
        # This will always be the fallback because we're not sure
        # enough that the header is associated with this file.
        self._section = self._OTHER_H_SECTION
    else:
      assert header_type == _OTHER_HEADER
      self._section = self._OTHER_H_SECTION

    if last_section != self._section:
      self._last_header = ''

    return ''


class _CppLintState(object):
  """Maintains module-wide state.."""

  def __init__(self):
    self.project_name = 'src'
    self.verbose_level = 1  # global setting.
    self.error_count = 0    # global count of reported errors
    # filters to apply when emitting error messages
    self.filters = _DEFAULT_FILTERS[:]
    self.counting = 'total'  # In what way are we counting errors?
    self.errors_by_category = {}  # string to int dict storing error counts

    # output format:
    # "emacs" - format that emacs can parse (default)
    # "vs7" - format that Microsoft Visual Studio 7 can parse
    self.output_format = 'emacs'

  def SetOutputFormat(self, output_format):
    """Sets the output format for errors."""
    self.output_format = output_format

  def SetVerboseLevel(self, level):
    """Sets the module's verbosity, and returns the previous setting."""
    last_verbose_level = self.verbose_level
    self.verbose_level = level
    return last_verbose_level

  def SetProjectName(self, name):
    """Sets the module's verbosity, and returns the previous setting."""
    last_project_name = self.project_name
    self.project_name = name
    return last_project_name

  def SetCountingStyle(self, counting_style):
    """Sets the module's counting options."""
    self.counting = counting_style

  def SetFilters(self, filters):
    """Sets the error-message filters.

    These filters are applied when deciding whether to emit a given
    error message.

    Args:
      filters: A string of comma-separated filters (eg "+whitespace/indent").
               Each filter should start with + or -; else we die.

    Raises:
      ValueError: The comma-separated filters did not all start with '+' or '-'.
                  E.g. "-,+whitespace,-whitespace/indent,whitespace/badfilter"
    """
    # Default filters always have less priority than the flag ones.
    self.filters = _DEFAULT_FILTERS[:]
    for filt in filters.split(','):
      clean_filt = filt.strip()
      if clean_filt:
        self.filters.append(clean_filt)
    for filt in self.filters:
      if not (filt.startswith('+') or filt.startswith('-')):
        raise ValueError('Every filter in --filters must start with + or -'
                         ' (%s does not)' % filt)

  def ResetErrorCounts(self):
    """Sets the module's error statistic back to zero."""
    self.error_count = 0
    self.errors_by_category = {}

  def IncrementErrorCount(self, category):
    """Bumps the module's error statistic."""
    self.error_count += 1
    if self.counting in ('toplevel', 'detailed'):
      if self.counting != 'detailed':
        category = category.split('/')[0]
      if category not in self.errors_by_category:
        self.errors_by_category[category] = 0
      self.errors_by_category[category] += 1

  def PrintErrorCounts(self):
    """Print a summary of errors by category, and the total."""
    for category, count in iteritems(self.errors_by_category):
      sys.stderr.write('Category \'%s\' errors found: %d\n' %
                       (category, count))
    sys.stderr.write('Total errors found: %d\n' % self.error_count)

_cpplint_state = _CppLintState()


def _OutputFormat():
  """Gets the module's output format."""
  return _cpplint_state.output_format


def _SetOutputFormat(output_format):
  """Sets the module's output format."""
  _cpplint_state.SetOutputFormat(output_format)


def _VerboseLevel():
  """Returns the module's verbosity setting."""
  return _cpplint_state.verbose_level


def _SetVerboseLevel(level):
  """Sets the module's verbosity, and returns the previous setting."""
  return _cpplint_state.SetVerboseLevel(level)


def _ProjectName():
  """Returns the module's project name setting."""
  return _cpplint_state.project_name


def _SetProjectName(name):
  """Sets the module's project name, and returns the previous setting."""
  return _cpplint_state.SetProjectName(name)


def _SetCountingStyle(level):
  """Sets the module's counting options."""
  _cpplint_state.SetCountingStyle(level)


def _Filters():
  """Returns the module's list of output filters, as a list."""
  return _cpplint_state.filters


def _SetFilters(filters):
  """Sets the module's error-message filters.

  These filters are applied when deciding whether to emit a given
  error message.

  Args:
    filters: A string of comma-separated filters (eg "whitespace/indent").
             Each filter should start with + or -; else we die.
  """
  _cpplint_state.SetFilters(filters)


class _FunctionState(object):
  """Tracks current function name and the number of lines in its body."""

  _NORMAL_TRIGGER = 260  # for --v=0, 500 for --v=1, etc.
  _TEST_TRIGGER = 400    # about 50% more than _NORMAL_TRIGGER.

  def __init__(self):
    self.in_a_function = False
    self.lines_in_function = 0
    self.current_function = ''

  def Begin(self, function_name):
    """Start analyzing function body.

    Args:
      function_name: The name of the function being tracked.
    """
    self.in_a_function = True
    self.lines_in_function = 0
    self.current_function = function_name

  def Count(self):
    """Count line in current function body."""
    if self.in_a_function:
      self.lines_in_function += 1

  def Check(self, error, filename, linenum):
    """Report if too many lines in function body.

    Args:
      error: The function to call with any errors found.
      filename: The name of the current file.
      linenum: The number of the line to check.
    """
    if Match(r'T(EST|est)', self.current_function):
      base_trigger = self._TEST_TRIGGER
    else:
      base_trigger = self._NORMAL_TRIGGER
    trigger = base_trigger * 2**_VerboseLevel()

    if self.lines_in_function > trigger:
      error_level = int(math.log(self.lines_in_function / base_trigger, 2))
      # 50 => 0, 100 => 1, 200 => 2, 400 => 3, 800 => 4, 1600 => 5, ...
      if error_level > 5:
        error_level = 5
      error(filename, linenum, 'readability/fn_size', error_level,
            'Small and focused functions are preferred:'
            ' %s has %d non-comment lines'
            ' (error triggered by exceeding %d lines).'  % (
                self.current_function, self.lines_in_function, trigger))

  def End(self):
    """Stop analyzing function body."""
    self.in_a_function = False


class _IncludeError(Exception):
  """Indicates a problem with the include order in a file."""
  pass


class FileInfo:
  """Provides utility functions for filenames.

  FileInfo provides easy access to the components of a file's path
  relative to the project root.
  """

  def __init__(self, filename):
    self._filename = filename

  def FullName(self):
    """Make Windows paths like Unix."""
    return os.path.abspath(self._filename).replace('\\', '/')

  def RepositoryName(self):
    """FullName after removing the local path to the repository.

    If we have a real absolute path name here we can try to do something smart:
    detecting the root of the checkout and truncating /path/to/checkout from
    the name so that we get header guards that don't include things like
    "C:\\Documents and Settings\\..." or "/home/username/..." in them and thus
    people on different computers who have checked the source out to different
    locations won't see bogus errors.
    """
    fullname = self.FullName()

    if os.path.exists(fullname):
      project_dir = os.path.dirname(fullname)

      if os.path.exists(os.path.join(project_dir, ".svn")):
        # If there's a .svn file in the current directory, we recursively look
        # up the directory tree for the top of the SVN checkout
        root_dir = project_dir
        one_up_dir = os.path.dirname(root_dir)
        while os.path.exists(os.path.join(one_up_dir, ".svn")):
          root_dir = os.path.dirname(root_dir)
          one_up_dir = os.path.dirname(one_up_dir)

        prefix = os.path.commonprefix([root_dir, project_dir])
        return fullname[len(prefix) + 1:]

      # Not SVN <= 1.6? Try to find a git, hg, or svn top level directory by
      # searching up from the current path.
      root_dir = os.path.dirname(fullname)
      while (root_dir != os.path.dirname(root_dir) and
             os.path.basename(root_dir) != "src" and
             not os.path.exists(os.path.join(root_dir, ".git")) and
             not os.path.exists(os.path.join(root_dir, ".hg")) and
             not os.path.exists(os.path.join(root_dir, ".svn"))):
        root_dir = os.path.dirname(root_dir)

      if (os.path.basename(root_dir) == "src" or
          os.path.exists(os.path.join(root_dir, ".git")) or
          os.path.exists(os.path.join(root_dir, ".hg")) or
          os.path.exists(os.path.join(root_dir, ".svn"))):
        prefix = os.path.commonprefix([root_dir, project_dir])
        return fullname[len(prefix) + 1:]

    # Don't know what to do; header guard warnings may be wrong...
    return fullname

  def Split(self):
    """Splits the file into the directory, basename, and extension.

    For 'chrome/browser/browser.cpp', Split() would
    return ('chrome/browser', 'browser', '.cpp')

    Returns:
      A tuple of (directory, basename, extension).
    """

    googlename = self.RepositoryName()
    project, rest = os.path.split(googlename)
    return (project,) + os.path.splitext(rest)

  def BaseName(self):
    """File base name - text after the final slash, before the final period."""
    return self.Split()[1]

  def Extension(self):
    """File extension - text following the final period."""
    return self.Split()[2]

  def NoExtension(self):
    """File has no source file extension."""
    return '/'.join(self.Split()[0:2])

  def IsSource(self):
    """File has a source file extension."""
    return self.Extension()[1:] in EXTENSIONS


def _ShouldPrintError(category, confidence, linenum):
  """If confidence >= verbose, category passes filter and is not suppressed."""

  # There are three ways we might decide not to print an error message:
  # a "NOLINT(category)" comment appears in the source,
  # the verbosity level isn't high enough, or the filters filter it out.
  if IsErrorSuppressedByNolint(category, linenum):
    return False
  if confidence < _cpplint_state.verbose_level:
    return False

  is_filtered = False
  for one_filter in _Filters():
    if one_filter.startswith('-'):
      if category.startswith(one_filter[1:]):
        is_filtered = True
    elif one_filter.startswith('+'):
      if category.startswith(one_filter[1:]):
        is_filtered = False
    else:
      assert False  # should have been checked for in SetFilter.
  if is_filtered:
    return False

  return True


def Error(filename, linenum, category, confidence, message):
  """Logs the fact we've found a lint error.

  We log where the error was found, and also our confidence in the error,
  that is, how certain we are this is a legitimate style regression, and
  not a misidentification or a use that's sometimes justified.

  False positives can be suppressed by the use of
  "cpplint(category)"  comments on the offending line.  These are
  parsed into _error_suppressions.

  Args:
    filename: The name of the file containing the error.
    linenum: The number of the line containing the error.
    category: A string used to describe the "category" this bug
      falls under: "whitespace", say, or "runtime".  Categories
      may have a hierarchy separated by slashes: "whitespace/indent".
    confidence: A number from 1-5 representing a confidence score for
      the error, with 5 meaning that we are certain of the problem,
      and 1 meaning that it could be a legitimate construct.
    message: The error message.
  """
  if _ShouldPrintError(category, confidence, linenum):
    _cpplint_state.IncrementErrorCount(category)
    if _cpplint_state.output_format == 'vs7':
      sys.stderr.write('%s(%s):  %s  [%s] [%d]\n' % (
          filename, linenum, message, category, confidence))
    else:
      m = '%s:%s:  %s  [%s] [%d]\n' % (
          filename, linenum, message, category, confidence)
      sys.stderr.write(m)

# Matches standard C++ escape esequences per 2.13.2.3 of the C++ standard.
_RE_PATTERN_CLEANSE_LINE_ESCAPES = re.compile(
    r'\\([abfnrtv?"\\\']|\d+|x[0-9a-fA-F]+)')
# Matches strings.  Escape codes should already be removed by ESCAPES.
_RE_PATTERN_CLEANSE_LINE_DOUBLE_QUOTES = re.compile(r'"[^"]*"')
# Matches characters.  Escape codes should already be removed by ESCAPES.
_RE_PATTERN_CLEANSE_LINE_SINGLE_QUOTES = re.compile(r"'.'")
# Matches multi-line C++ comments.
# This RE is a little bit more complicated than one might expect, because we
# have to take care of space removals tools so we can handle comments inside
# statements better.
# The current rule is: We only clear spaces from both sides when we're at the
# end of the line. Otherwise, we try to remove spaces from the right side,
# if this doesn't work we try on left side but only if there's a non-character
# on the right.
_RE_PATTERN_CLEANSE_LINE_C_COMMENTS = re.compile(
    r"""(\s*/\*.*\*/\s*$|
            /\*.*\*/\s+|
         \s+/\*.*\*/(?=\W)|
            /\*.*\*/)""", re.VERBOSE)


def IsCppString(line):
  """Does line terminate so, that the next symbol is in string constant.

  This function does not consider single-line nor multi-line comments.

  Args:
    line: is a partial line of code starting from the 0..n.

  Returns:
    True, if next character appended to 'line' is inside a
    string constant.
  """

  line = line.replace(r'\\', 'XX')  # after this, \\" does not match to \"
  return ((line.count('"') - line.count(r'\"') - line.count("'\"'")) & 1) == 1


def FindNextMultiLineCommentStart(lines, lineix):
  """Find the beginning marker for a multiline comment."""
  while lineix < len(lines):
    if lines[lineix].strip().startswith('/*'):
      # Only return this marker if the comment goes beyond this line
      if lines[lineix].strip().find('*/', 2) < 0:
        return lineix
    lineix += 1
  return len(lines)


def FindNextMultiLineCommentEnd(lines, lineix):
  """We are inside a comment, find the end marker."""
  while lineix < len(lines):
    if lines[lineix].strip().endswith('*/'):
      return lineix
    lineix += 1
  return len(lines)


def RemoveMultiLineCommentsFromRange(lines, begin, end):
  """Clears a range of lines for multi-line comments."""
  # Having // dummy comments makes the lines non-empty, so we will not get
  # unnecessary blank line warnings later in the code.
  for i in range(begin, end):
    lines[i] = re.search('^\t*', lines[i]).group(0) + '// dummy'


def RemoveMultiLineComments(filename, lines, error):
  """Removes multiline (c-style) comments from lines."""
  lineix = 0
  while lineix < len(lines):
    lineix_begin = FindNextMultiLineCommentStart(lines, lineix)
    if lineix_begin >= len(lines):
      return
    lineix_end = FindNextMultiLineCommentEnd(lines, lineix_begin)
    if lineix_end >= len(lines):
      error(filename, lineix_begin + 1, 'readability/multiline_comment', 5,
            'Could not find end of multi-line comment')
      return
    RemoveMultiLineCommentsFromRange(lines, lineix_begin, lineix_end + 1)
    lineix = lineix_end + 1


def CleanseComments(line):
  """Removes //-comments and single-line C-style /* */ comments.

  Args:
    line: A line of C++ source.

  Returns:
    The line with single-line comments removed.
  """
  commentpos = line.find('//')
  if commentpos != -1 and not IsCppString(line[:commentpos]):
    line = line[:commentpos].rstrip()
  # get rid of /* ... */
  return _RE_PATTERN_CLEANSE_LINE_C_COMMENTS.sub('', line)


class CleansedLines(object):
  """Holds 3 copies of all lines with different preprocessing applied to them.

  1) elided member contains lines without strings and comments,
  2) lines member contains lines without comments, and
  3) raw member contains all the lines without processing.
  All these three members are of <type 'list'>, and of the same length.
  """

  def __init__(self, lines):
    self.elided = []
    self.lines = []
    self.raw_lines = lines
    self.num_lines = len(lines)
    for linenum in range(len(lines)):
      self.lines.append(CleanseComments(lines[linenum]))
      elided = self._CollapseStrings(lines[linenum])
      self.elided.append(CleanseComments(elided))

  def NumLines(self):
    """Returns the number of lines represented."""
    return self.num_lines

  @staticmethod
  def _CollapseStrings(elided):
    """Collapses strings and chars on a line to simple "" or '' blocks.

    We nix strings first so we're not fooled by text like '"http://"'

    Args:
      elided: The line being processed.

    Returns:
      The line with collapsed strings.
    """
    if not _RE_PATTERN_INCLUDE.match(elided):
      # Remove escaped characters first to make quote/single quote collapsing
      # basic.  Things that look like escaped characters shouldn't occur
      # outside of strings and chars.
      elided = _RE_PATTERN_CLEANSE_LINE_ESCAPES.sub('', elided)
      elided = _RE_PATTERN_CLEANSE_LINE_SINGLE_QUOTES.sub("''", elided)
      elided = _RE_PATTERN_CLEANSE_LINE_DOUBLE_QUOTES.sub('""', elided)
    return elided


def CloseExpression(clean_lines, linenum, pos):
  """If input points to ( or { or [, finds the position that closes it.

  If lines[linenum][pos] points to a '(' or '{' or '[', finds the
  linenum/pos that correspond to the closing of the expression.

  Args:
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    pos: A position on the line.

  Returns:
    A tuple (line, linenum, pos) pointer *past* the closing brace, or
    (line, len(lines), -1) if we never find a close.  Note we ignore
    strings and comments when matching; and the line we return is the
    'cleansed' line at linenum.
  """

  line = clean_lines.elided[linenum]
  startchar = line[pos]
  if startchar not in '({[':
    return (line, clean_lines.NumLines(), -1)
  if startchar == '(': endchar = ')'
  if startchar == '[': endchar = ']'
  if startchar == '{': endchar = '}'

  num_open = line.count(startchar) - line.count(endchar)
  while linenum < clean_lines.NumLines() and num_open > 0:
    linenum += 1
    line = clean_lines.elided[linenum]
    num_open += line.count(startchar) - line.count(endchar)
  # OK, now find the endchar that actually got us back to even
  endpos = len(line)
  while num_open >= 0:
    endpos = line.rfind(')', 0, endpos)
    num_open -= 1                 # chopped off another )
  return (line, linenum, endpos + 1)


def CheckForCopyright(filename, lines, error):
  """Logs an error if no Copyright message appears at the top of the file."""

  # We'll say it should occur by line 10. Don't forget there's a
  # dummy line at the front.
  for line in range(1, min(len(lines), 11)):
    if re.search(r'Copyright', lines[line], re.I):
      break
  else:                       # means no copyright line was found
    error(filename, 0, 'legal/copyright', 5,
          'No copyright message found.  '
          'You should have a line: "Copyright [year] <Copyright Owner>"')


def GetHeaderGuardCPPVariable(filename):
  """Returns the CPP variable that should be used as a header guard.

  Args:
    filename: The name of a C++ header file.

  Returns:
    The CPP variable that should be used as a header guard in the
    named file.

  """

  # Restores original filename in case that cpplint is invoked from Emacs's
  # flymake.
  filename = re.sub(r'_flymake\.h$', '.h', filename)

  fileinfo = FileInfo(filename)
  return (_ProjectName() + '_' + re.sub(r'[-./\s]', '_', fileinfo.RepositoryName())).upper()


def CheckForHeaderGuard(filename, lines, error):
  """Checks that the file contains a header guard.

  Logs an error if no #ifndef header guard is present.  For other
  headers, checks that the full pathname is used.

  Args:
    filename: The name of the C++ header file.
    lines: An array of strings, each representing a line of the file.
    error: The function to call with any errors found.
  """

  cppvar = GetHeaderGuardCPPVariable(filename)

  ifndef = None
  ifndef_linenum = 0
  define = None
  endif = None
  endif_linenum = 0
  boostppiterating = None
  for linenum, line in enumerate(lines):
    linesplit = line.split()
    if len(linesplit) >= 2:
      if not ifndef and linesplit[0] == '#ifdef' and linesplit[1] == 'BOOST_PP_IS_ITERATING':
        boostppiterating = linesplit[1]
      # find the first occurrence of #ifndef and #define, save arg
      if not boostppiterating and not ifndef and linesplit[0] == '#ifndef':
        # set ifndef to the header guard presented on the #ifndef line.
        ifndef = linesplit[1]
        ifndef_linenum = linenum
      if not boostppiterating and not define and linesplit[0] == '#define':
        define = linesplit[1]
    # find the last occurrence of #endif, save entire line
    if line.startswith('#endif'):
      endif = line
      endif_linenum = linenum

  if not boostppiterating and not ifndef:
    error(filename, 0, 'build/header_guard', 5,
          'No #ifndef header guard found, suggested CPP variable is: %s' %
          cppvar)
    return

  if not boostppiterating and not define:
    error(filename, 0, 'build/header_guard', 5,
          'No #define header guard found, suggested CPP variable is: %s' %
          cppvar)
    return

  # The guard should be PATH_FILE_H_, but we also allow PATH_FILE_H__
  # for backward compatibility.
  if not boostppiterating and ifndef != cppvar:
    error_level = 0
    if ifndef != cppvar + '_':
      error_level = 5

    ParseNolintSuppressions(filename, lines[ifndef_linenum], ifndef_linenum,
                            error)
    error(filename, ifndef_linenum, 'build/header_guard', error_level,
          '#ifndef header guard has wrong style, please use: %s' % cppvar)

  if not boostppiterating and define != ifndef:
    error(filename, 0, 'build/header_guard', 5,
          '#ifndef and #define don\'t match, suggested CPP variable is: %s' %
          cppvar)
    return

  if not boostppiterating and endif != ('#endif // %s' % cppvar):
    error_level = 0
    if endif != ('#endif // %s' % (cppvar + '_')):
      error_level = 5

    ParseNolintSuppressions(filename, lines[endif_linenum], endif_linenum,
                            error)
    error(filename, endif_linenum, 'build/header_guard', error_level,
          '#endif line should be "#endif // %s"' % cppvar)

  if boostppiterating and endif != ('#endif // %s' % boostppiterating):
    error_level = 5

    ParseNolintSuppressions(filename, lines[endif_linenum], endif_linenum,
                            error)
    error(filename, endif_linenum, 'build/header_guard', error_level,
          '#endif line should be "#endif // %s"' % boostppiterating)


def CheckForUnicodeReplacementCharacters(filename, lines, error):
  """Logs an error for each line containing Unicode replacement characters.

  These indicate that either the file contained invalid UTF-8 (likely)
  or Unicode replacement characters (which it shouldn't).  Note that
  it's possible for this to throw off line numbering if the invalid
  UTF-8 occurred adjacent to a newline.

  Args:
    filename: The name of the current file.
    lines: An array of strings, each representing a line of the file.
    error: The function to call with any errors found.
  """
  for linenum, line in enumerate(lines):
    if u('\ufffd') in line:
      error(filename, linenum, 'readability/utf8', 5,
            'Line contains invalid UTF-8 (or Unicode replacement character).')


def CheckForNewlineAtEOF(filename, lines, error):
  """Logs an error if there is no newline char at the end of the file.

  Args:
    filename: The name of the current file.
    lines: An array of strings, each representing a line of the file.
    error: The function to call with any errors found.
  """

  # The array lines() was created by adding two newlines to the
  # original file (go figure), then splitting on \n.
  # To verify that the file ends in \n, we just have to make sure the
  # last-but-two element of lines() exists and is empty.
  if len(lines) < 3 or lines[-2]:
    error(filename, len(lines) - 2, 'whitespace/ending_newline', 5,
          'Could not find a newline character at the end of the file.')


def CheckForMultilineCommentsAndStrings(filename, clean_lines, linenum, error):
  """Logs an error if we see /* ... */ or "..." that extend past one line.

  /* ... */ comments are legit inside macros, for one line.
  Otherwise, we prefer // comments, so it's ok to warn about the
  other.  Likewise, it's ok for strings to extend across multiple
  lines, as long as a line continuation character (backslash)
  terminates each line. Although not currently prohibited by the C++
  style guide, it's ugly and unnecessary. We don't do well with either
  in this lint program, so we warn about both.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    error: The function to call with any errors found.
  """
  line = clean_lines.elided[linenum]

  # Remove all \\ (escaped backslashes) from the line. They are OK, and the
  # second (escaped) slash may trigger later \" detection erroneously.
  line = line.replace('\\\\', '')

  if line.count('/*') > line.count('*/'):
    error(filename, linenum, 'readability/multiline_comment', 5,
          'Complex multi-line /*...*/-style comment found. '
          'Lint may give bogus warnings.  '
          'Consider replacing these with //-style comments, '
          'with #if 0...#endif, '
          'or with more clearly structured multi-line comments.')

  if (line.count('"') - line.count('\\"')) % 2:
    error(filename, linenum, 'readability/multiline_string', 5,
          'Multi-line string ("...") found.  This lint script doesn\'t '
          'do well with such strings, and may give bogus warnings.  They\'re '
          'ugly and unnecessary, and you should use concatenation instead".')


threading_list = (
    ('asctime(', 'asctime_r('),
    ('ctime(', 'ctime_r('),
    ('getgrgid(', 'getgrgid_r('),
    ('getgrnam(', 'getgrnam_r('),
    ('getlogin(', 'getlogin_r('),
    ('getpwnam(', 'getpwnam_r('),
    ('getpwuid(', 'getpwuid_r('),
    ('gmtime(', 'gmtime_r('),
    ('localtime(', 'localtime_r('),
    ('rand(', 'rand_r('),
    ('readdir(', 'readdir_r('),
    ('strtok(', 'strtok_r('),
    ('ttyname(', 'ttyname_r('),
    )


def CheckPosixThreading(filename, clean_lines, linenum, error):
  """Checks for calls to thread-unsafe functions.

  Much code has been originally written without consideration of
  multi-threading. Also, engineers are relying on their old experience;
  they have learned posix before threading extensions were added. These
  tests guide the engineers to use thread-safe functions (when using
  posix directly).

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    error: The function to call with any errors found.
  """
  if '/* not thread-safe */' in clean_lines.raw_lines[linenum]:
    return
  line = clean_lines.elided[linenum]
  for single_thread_function, multithread_safe_function in threading_list:
    ix = line.find(single_thread_function)
    # Comparisons made explicit for clarity -- pylint: disable-msg=C6403
    if ix >= 0 and (ix == 0 or (not line[ix - 1].isalnum() and
                                line[ix - 1] not in ('_', '.', '>'))):
      error(filename, linenum, 'runtime/threadsafe_fn', 2,
            'Consider using ' + multithread_safe_function +
            '...) instead of ' + single_thread_function +
            '...) for improved thread safety.')


# Matches invalid increment: *count++, which moves pointer instead of
# incrementing a value.
_RE_PATTERN_INVALID_INCREMENT = re.compile(
    r'^\s*\*\w+(\+\+|--);')


def CheckInvalidIncrement(filename, clean_lines, linenum, error):
  """Checks for invalid increment *count++.

  For example following function:
  void increment_counter(int* count) {
    *count++;
  }
  is invalid, because it effectively does count++, moving pointer, and should
  be replaced with ++*count, (*count)++ or *count += 1.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    error: The function to call with any errors found.
  """
  line = clean_lines.elided[linenum]
  if _RE_PATTERN_INVALID_INCREMENT.match(line):
    error(filename, linenum, 'runtime/invalid_increment', 5,
          'Changing pointer instead of value (or unused value of operator*).')


class _ClassInfo(object):
  """Stores information about a class."""

  def __init__(self, name, clean_lines, linenum):
    self.name = name
    self.linenum = linenum
    self.seen_open_brace = False
    self.is_derived = False
    self.virtual_method_linenumber = None
    self.has_virtual_destructor = False
    self.brace_depth = 0

    # Try to find the end of the class.  This will be confused by things like:
    #   class A {
    #   } *x = { ...
    #
    # But it's still good enough for CheckSectionSpacing.
    self.last_line = 0
    depth = 0
    for i in range(linenum, clean_lines.NumLines()):
      line = clean_lines.lines[i]
      depth += line.count('{') - line.count('}')
      if not depth:
        self.last_line = i
        break


class _ClassState(object):
  """Holds the current state of the parse relating to class declarations.

  It maintains a stack of _ClassInfos representing the parser's guess
  as to the current nesting of class declarations. The innermost class
  is at the top (back) of the stack. Typically, the stack will either
  be empty or have exactly one entry.
  """

  def __init__(self):
    self.classinfo_stack = []

  def CheckFinished(self, filename, error):
    """Checks that all classes have been completely parsed.

    Call this when all lines in a file have been processed.
    Args:
      filename: The name of the current file.
      error: The function to call with any errors found.
    """
    if self.classinfo_stack:
      # Note: This test can result in false positives if #ifdef constructs
      # get in the way of brace matching. See the testBuildClass test in
      # cpplint_unittest.py for an example of this.
      error(filename, self.classinfo_stack[0].linenum, 'build/class', 5,
            'Failed to find complete declaration of class %s' %
            self.classinfo_stack[0].name)


def CheckForNonStandardConstructs(filename, clean_lines, linenum,
                                  class_state, error):
  """Logs an error if we see certain non-ANSI constructs ignored by gcc-2.

  Complain about several constructs which gcc-2 accepts, but which are
  not standard C++.  Warning about these in lint is one way to ease the
  transition to new compilers.
  - put storage class first (e.g. "static const" instead of "const static").
  - "%lld" instead of %qd" in printf-type functions.
  - "%1$d" is non-standard in printf-type functions.
  - "\\%" is an undefined character escape sequence.
  - text after #endif is not allowed.
  - invalid inner-style forward declaration.
  - >? and <? operators, and their >?= and <?= cousins.
  - classes with virtual methods need virtual destructors (compiler warning
    available, but not turned on yet.)

  Additionally, check for constructor/destructor style violations and reference
  members, as it is very convenient to do so while checking for
  gcc-2 compliance.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    class_state: A _ClassState instance which maintains information about
                 the current stack of nested class declarations being parsed.
    error: A callable to which errors are reported, which takes 4 arguments:
           filename, line number, error level, and message
  """

  # Remove comments from the line, but leave in strings for now.
  line = clean_lines.lines[linenum]

  if Search(r'printf\s*\(.*".*%[-+ ]?\d*q', line):
    error(filename, linenum, 'runtime/printf_format', 3,
          '%q in format strings is deprecated.  Use %ll instead.')

  if Search(r'printf\s*\(.*".*%\d+\$', line):
    error(filename, linenum, 'runtime/printf_format', 2,
          '%N$ formats are unconventional.  Try rewriting to avoid them.')

  # Remove escaped backslashes before looking for undefined escapes.
  line = line.replace('\\\\', '')

  if Search(r'("|\').*\\(%|\[|\(|{)', line):
    error(filename, linenum, 'build/printf_format', 3,
          '%, [, (, and { are undefined character escapes.  Unescape them.')

  # For the rest, work with both comments and strings removed.
  line = clean_lines.elided[linenum]

  if Search(r'\b(const|volatile|void|char|short|int|long'
            r'|float|double|signed|unsigned'
            r'|schar|u?int8|u?int16|u?int32|u?int64)'
            r'\s+(auto|register|static|extern|typedef)\b',
            line):
    error(filename, linenum, 'build/storage_class', 5,
          'Storage class (static, extern, typedef, etc) should be first.')

  if Match(r'\s*#\s*endif\s*[^/\s]+', line):
    error(filename, linenum, 'build/endif_comment', 5,
          'Uncommented text after #endif is non-standard.  Use a comment.')

  if Match(r'\s*class\s+(\w+\s*::\s*)+\w+\s*;', line):
    error(filename, linenum, 'build/forward_decl', 5,
          'Inner-style forward declarations are invalid.  Remove this line.')

  if Search(r'(\w+|[+-]?\d+(\.\d*)?)\s*(<|>)\?=?\s*(\w+|[+-]?\d+)(\.\d*)?',
            line):
    error(filename, linenum, 'build/deprecated', 3,
          '>? and <? (max and min) operators are non-standard and deprecated.')

  if Search(r'^\s*const\s*string\s*&\s*\w+\s*;', line):
    # TODO(unknown): Could it be expanded safely to arbitrary references,
    # without triggering too many false positives? The first
    # attempt triggered 5 warnings for mostly benign code in the regtest, hence
    # the restriction.
    # Here's the original regexp, for the reference:
    # type_name = r'\w+((\s*::\s*\w+)|(\s*<\s*\w+?\s*>))?'
    # r'\s*const\s*' + type_name + '\s*&\s*\w+\s*;'
    error(filename, linenum, 'runtime/member_string_references', 2,
          'const string& members are dangerous. It is much better to use '
          'alternatives, such as pointers or simple constants.')

  # Track class entry and exit, and attempt to find cases within the
  # class declaration that don't meet the C++ style
  # guidelines. Tracking is very dependent on the code matching Google
  # style guidelines, but it seems to perform well enough in testing
  # to be a worthwhile addition to the checks.
  classinfo_stack = class_state.classinfo_stack
  # Look for a class declaration. The regexp accounts for decorated classes
  # such as in:
  # class LOCKABLE API Object {
  # };
  class_decl_match = Match(
      r'\s*(template\s*<[\w\s<>,:]*>\s*)?'
      r'(class|struct)\s+([A-Z_]+\s+)*(\w+(::\w+)*)', line)
  if class_decl_match:
    classinfo_stack.append(_ClassInfo(
        class_decl_match.group(4), clean_lines, linenum))

  # Everything else in this function uses the top of the stack if it's
  # not empty.
  if not classinfo_stack:
    return

  classinfo = classinfo_stack[-1]

  # If the opening brace hasn't been seen look for it and also
  # parent class declarations.
  if not classinfo.seen_open_brace:
    # If the line has a ';' in it, assume it's a forward declaration or
    # a single-line class declaration, which we won't process.
    if line.find(';') != -1:
      classinfo_stack.pop()
      return
    classinfo.seen_open_brace = (line.find('{') != -1)
    # Look for a bare ':'
    if Search('(^|[^:]):($|[^:])', line):
      classinfo.is_derived = True
    if not classinfo.seen_open_brace:
      return  # Everything else in this function is for after open brace

  # The class may have been declared with namespace or classname qualifiers.
  # The constructor and destructor will not have those qualifiers.
  base_classname = classinfo.name.split('::')[-1]

  # Look for single-argument constructors that aren't marked explicit.
  # Technically a valid construct, but against style.
  args = Match(r'\s+(?:inline\s+)?%s\s*\(([^,()]+)\)'
               % re.escape(base_classname),
               line)
  if (args and
      args.group(1) != 'void' and
      clean_lines.raw_lines[linenum].find('/* implicit */') < 0 and
      not Match(r'(const\s+)?%s\s*(?:<\w+>\s*)?&' % re.escape(base_classname),
                args.group(1).strip())):
    error(filename, linenum, 'runtime/explicit', 5,
          'Single-argument constructors should be marked explicit.')

  # Look for methods declared virtual.
  if Search(r'\bvirtual\b', line):
    classinfo.virtual_method_linenumber = linenum
    # Only look for a destructor declaration on the same line. It would
    # be extremely unlikely for the destructor declaration to occupy
    # more than one line.
    if Search(r'~%s\s*\(' % base_classname, line):
      classinfo.has_virtual_destructor = True

  # Look for class end.
  brace_depth = classinfo.brace_depth
  brace_depth = brace_depth + line.count('{') - line.count('}')
  if brace_depth <= 0:
    classinfo = classinfo_stack.pop()
    # Try to detect missing virtual destructor declarations.
    # For now, only warn if a non-derived class with virtual methods lacks
    # a virtual destructor. This is to make it less likely that people will
    # declare derived virtual destructors without declaring the base
    # destructor virtual.
    if ((classinfo.virtual_method_linenumber is not None) and
        (not classinfo.has_virtual_destructor) and
        (not classinfo.is_derived)):  # Only warn for base classes
      error(filename, classinfo.linenum, 'runtime/virtual', 4,
            'The class %s probably needs a virtual destructor due to '
            'having virtual method(s), one declared at line %d.'
            % (classinfo.name, classinfo.virtual_method_linenumber))
  else:
    classinfo.brace_depth = brace_depth


def CheckSpacingForFunctionCall(filename, line, linenum, error):
  """Checks for the correctness of various spacing around function calls.

  Args:
    filename: The name of the current file.
    line: The text of the line to check.
    linenum: The number of the line to check.
    error: The function to call with any errors found.
  """

  # Since function calls often occur inside if/for/while/switch
  # expressions - which have their own, more liberal conventions - we
  # first see if we should be looking inside such an expression for a
  # function call, to which we can apply more strict standards.
  fncall = line    # if there's no control flow construct, look at whole line
  for pattern in (r'\bif\s*\((.*)\)\s*{',
                  r'\bfor\s*\((.*)\)\s*{',
                  r'\bwhile\s*\((.*)\)\s*[{;]',
                  r'\bswitch\s*\((.*)\)\s*{'):
    match = Search(pattern, line)
    if match:
      fncall = match.group(1)    # look inside the parens for function calls
      break

  # Except in if/for/while/switch, there should never be space
  # immediately inside parens (eg "f( 3, 4 )").  We make an exception
  # for nested parens ( (a+b) + c ).  Likewise, there should never be
  # a space before a ( when it's a function argument.  I assume it's a
  # function argument when the char before the whitespace is legal in
  # a function name (alnum + _) and we're not starting a macro. Also ignore
  # pointers and references to arrays and functions coz they're too tricky:
  # we use a very simple way to recognize these:
  # " (something)(maybe-something)" or
  # " (something)(maybe-something," or
  # " (something)[something]"
  # Note that we assume the contents of [] to be short enough that
  # they'll never need to wrap.
  if (  # Ignore control structures.
      not Search(r'\b(if|for|while|switch|return|delete)\b', fncall) and
      # Ignore pointers/references to functions.
      not Search(r' \([^)]+\)\([^)]*(\)|,$)', fncall) and
      # Ignore pointers/references to arrays.
      not Search(r' \([^)]+\)\[[^\]]+\]', fncall)):
    if Search(r'\w\s*\(\s(?!\s*\\$)', fncall):      # a ( used for a fn call
      error(filename, linenum, 'whitespace/parens', 4,
            'Extra space after ( in function call')
    elif Search(r'\(\s+(?!(\s*\\)|\()', fncall):
      error(filename, linenum, 'whitespace/parens', 2,
            'Extra space after (')
    if (Search(r'\w\s+\(', fncall) and
        not Search(r'#\s*define|typedef', fncall)):
      error(filename, linenum, 'whitespace/parens', 4,
            'Extra space before ( in function call')
    # If the ) is followed only by a newline or a { + newline, assume it's
    # part of a control statement (if/while/etc), and don't complain
    if Search(r'[^)]\s+\)\s*[^{\s]', fncall):
      # If the closing parenthesis is preceded by only whitespaces,
      # try to give a more descriptive error message.
      if not Search(r'^\s+\)', fncall):
        error(filename, linenum, 'whitespace/parens', 2,
              'Extra space before )')


def IsBlankLine(line):
  """Returns true if the given line is blank.

  We consider a line to be blank if the line is empty or consists of
  only white spaces.

  Args:
    line: A line of a string.

  Returns:
    True, if the given line is blank.
  """
  return not line or line.isspace()


def CheckForFunctionLengths(filename, clean_lines, linenum,
                            function_state, error):
  """Reports for long function bodies.

  For an overview why this is done, see:
  http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Write_Short_Functions

  Uses a simplistic algorithm assuming other style guidelines
  (especially spacing) are followed.
  Only checks unindented functions, so class members are unchecked.
  Trivial bodies are unchecked, so constructors with huge initializer lists
  may be missed.
  Blank/comment lines are not counted so as to avoid encouraging the removal
  of vertical space and comments just to get through a lint check.
  NOLINT *on the last line of a function* disables this check.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    function_state: Current function name and lines in body so far.
    error: The function to call with any errors found.
  """
  lines = clean_lines.lines
  line = lines[linenum]
  raw = clean_lines.raw_lines
  raw_line = raw[linenum]
  joined_line = ''

  starting_func = False
  regexp = r'(\w(\w|::|\*|\&|\s)*)\('  # decls * & space::name( ...
  match_result = Match(regexp, line)
  if match_result:
    # If the name is all caps and underscores, figure it's a macro and
    # ignore it, unless it's TEST or TEST_F.
    function_name = match_result.group(1).split()[-1]
    if function_name == 'TEST' or function_name == 'TEST_F' or (
        not Match(r'[A-Z_]+$', function_name)):
      starting_func = True

  if starting_func:
    body_found = False
    for start_linenum in range(linenum, clean_lines.NumLines()):
      start_line = lines[start_linenum]
      joined_line += ' ' + start_line.lstrip()
      if Search(r'(;|})', start_line):  # Declarations and trivial functions
        body_found = True
        break                              # ... ignore
      elif Search(r'{', start_line):
        body_found = True
        function = Search(r'((\w|:)*)\(', line).group(1)
        if Match(r'TEST', function):    # Handle TEST... macros
          parameter_regexp = Search(r'(\(.*\))', joined_line)
          if parameter_regexp:             # Ignore bad syntax
            function += parameter_regexp.group(1)
        else:
          function += '()'
        function_state.Begin(function)
        break
    if not body_found:
      # No body for the function (or evidence of a non-function) was found.
      error(filename, linenum, 'readability/fn_size', 5,
            'Lint failed to find start of function body.')
  elif Match(r'^\}\s*$', line):  # function end
    function_state.Check(error, filename, linenum)
    function_state.End()
  elif not Match(r'^\s*$', line):
    function_state.Count()  # Count non-blank/non-comment lines.


_RE_PATTERN_TODO = re.compile(r'^//(\s*)TODO(\(.+?\))?:?(\s|$)?')


def CheckComment(comment, filename, linenum, error):
  """Checks for common mistakes in TODO comments.

  Args:
    comment: The text of the comment from the line in question.
    filename: The name of the current file.
    linenum: The number of the line to check.
    error: The function to call with any errors found.
  """
  match = _RE_PATTERN_TODO.match(comment)
  if match:
    # One whitespace is correct; zero whitespace is handled elsewhere.
    leading_whitespace = match.group(1)
    if len(leading_whitespace) > 1:
      error(filename, linenum, 'whitespace/todo', 2,
            'Too many spaces before TODO')

    username = match.group(2)
    if not username:
      error(filename, linenum, 'readability/todo', 2,
            'Missing username in TODO; it should look like '
            '"// TODO(my_username): Stuff."')

    middle_whitespace = match.group(3)
    # Comparisons made explicit for correctness -- pylint: disable-msg=C6403
    if middle_whitespace != ' ' and middle_whitespace != '':
      error(filename, linenum, 'whitespace/todo', 2,
            'TODO(my_username) should be followed by a space')


def CheckSpacing(filename, clean_lines, linenum, error):
  """Checks for the correctness of various spacing issues in the code.

  Things we check for: spaces around operators, spaces after
  if/for/while/switch, no spaces around parens in function calls, two
  spaces between code and comment, don't start a block with a blank
  line, don't end a function with a blank line, don't add a blank line
  after public/protected/private, don't have too many blank lines in a row.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    error: The function to call with any errors found.
  """

  raw = clean_lines.raw_lines
  line = raw[linenum]

  # Before nixing comments, check if the line is blank for no good
  # reason.  This includes the first line after a block is opened, and
  # blank lines at the end of a function (ie, right before a line like '}'
  if IsBlankLine(line):
    elided = clean_lines.elided
    prev_line = elided[linenum - 1]
    prevbrace = prev_line.rfind('{')
    # TODO(unknown): Don't complain if line before blank line, and line after,
    #                both start with alnums and are indented the same amount.
    #                This ignores whitespace at the start of a namespace block
    #                because those are not usually indented.
    if (prevbrace != -1 and prev_line[prevbrace:].find('}') == -1
        and prev_line[:prevbrace].find('namespace') == -1):
      # OK, we have a blank line at the start of a code block.  Before we
      # complain, we check if it is an exception to the rule: The previous
      # non-empty line has the parameters of a function header that are indented
      # 4 spaces (because they did not fit in a 80 column line when placed on
      # the same line as the function name).  We also check for the case where
      # the previous line is indented 6 spaces, which may happen when the
      # initializers of a constructor do not fit into a 80 column line.
      exception = False
      if Match(r' {6}\w', prev_line):  # Initializer list?
        # We are looking for the opening column of initializer list, which
        # should be indented 4 spaces to cause 6 space indentation afterwards.
        search_position = linenum-2
        while (search_position >= 0
               and Match(r' {6}\w', elided[search_position])):
          search_position -= 1
        exception = (search_position >= 0
                     and elided[search_position][:5] == '    :')
      else:
        # Search for the function arguments or an initializer list.  We use a
        # simple heuristic here: If the line is indented 4 spaces; and we have a
        # closing paren, without the opening paren, followed by an opening brace
        # or colon (for initializer lists) we assume that it is the last line of
        # a function header.  If we have a colon indented 4 spaces, it is an
        # initializer list.
        exception = (Match(r' {4}\w[^\(]*\)\s*(const\s*)?(\{\s*$|:)',
                           prev_line)
                     or Match(r' {4}:', prev_line))

      if not exception:
        error(filename, linenum, 'whitespace/blank_line', 2,
              'Blank line at the start of a code block.  Is this needed?')
    # This doesn't ignore whitespace at the end of a namespace block
    # because that is too hard without pairing open/close braces;
    # however, a special exception is made for namespace closing
    # brackets which have a comment containing "namespace".
    #
    # Also, ignore blank lines at the end of a block in a long if-else
    # chain, like this:
    #   if (condition1) {
    #     // Something followed by a blank line
    #
    #   } else if (condition2) {
    #     // Something else
    #   }
    if linenum + 1 < clean_lines.NumLines():
      next_line = raw[linenum + 1]
      if (next_line
          and Match(r'\s*}', next_line)
          and next_line.find('namespace') == -1
          and next_line.find('} else ') == -1):
        error(filename, linenum, 'whitespace/blank_line', 3,
              'Blank line at the end of a code block.  Is this needed?')

    matched = Match(r'\s*(public|protected|private):', prev_line)
    if matched:
      error(filename, linenum, 'whitespace/blank_line', 3,
            'Do not leave a blank line after "%s:"' % matched.group(1))

  # Next, we complain if there's a comment too near the text
  commentpos = line.find('//')
  if commentpos != -1:
    # Check if the // may be in quotes.  If so, ignore it
    # Comparisons made explicit for clarity -- pylint: disable-msg=C6403
    if (line.count('"', 0, commentpos) -
        line.count('\\"', 0, commentpos)) % 2 == 0:   # not in quotes
      # Allow one space for new scopes, two spaces otherwise:
      #if (not Match(r'^\s*{ //', line) and
      #    ((commentpos >= 1 and
      #      line[commentpos-1] not in string.whitespace) or
      #     (commentpos >= 2 and
      #      line[commentpos-2] not in string.whitespace))):
      #  error(filename, linenum, 'whitespace/comments', 2,
      #        'At least two spaces is best between code and comments')
      # There should always be a space between the // and the comment
      commentend = commentpos + 2
      if commentend < len(line) and not line[commentend] == ' ':
        # but some lines are exceptions -- e.g. if they're big
        # comment delimiters like:
        # //----------------------------------------------------------
        # or are an empty C++ style Doxygen comment, like:
        # ///
        # or they begin with multiple slashes followed by a space:
        # //////// Header comment
        match = (Search(r'[=/-]{4,}\s*$', line[commentend:]) or
                 Search(r'^/$', line[commentend:]) or
                 Search(r'^! ', line[commentend:]) or
                 Search(r'^!< ', line[commentend:]) or
                 Search(r'^/+ ', line[commentend:]))
        if not match:
          error(filename, linenum, 'whitespace/comments', 4,
                'Should have a space between // and comment')
      CheckComment(line[commentpos:], filename, linenum, error)

  line = clean_lines.elided[linenum]  # get rid of comments and strings

  # Don't try to do spacing checks for operator methods
  line = re.sub(r'operator(==|!=|<|<<|<=|>=|>>|>)\(', 'operator(', line)

  if Search(r'template\<', line):
    error(filename, linenum, 'whitespace/templates', 4,
          'Missing space beteen template and <')

  # We allow no-spaces around = within an if: "if ( (a=Foo()) == 0 )".
  # Otherwise not.  Note we only check for non-spaces on *both* sides;
  # sometimes people put non-spaces on one side when aligning ='s among
  # many lines (not that this is behavior that I approve of...)
  if Search(r'[\w.]=[\w.]', line) and not Search(r'\b(if|while) ', line):
    error(filename, linenum, 'whitespace/operators', 4,
          'Missing spaces around =')

  # It's ok not to have spaces around binary operators like + - * /, but if
  # there's too little whitespace, we get concerned.  It's hard to tell,
  # though, so we punt on this one for now.  TODO.

  # You should always have whitespace around binary operators.
  # Alas, we can't test < or > because they're legitimately used sans spaces
  # (a->b, vector<int> a).  The only time we can tell is a < with no >, and
  # only if it's not template params list spilling into the next line.
  match = Search(r'[^<>=!\s](==|!=|<=|>=)[^<>=!\s]', line)
  if not match:
    # Note that while it seems that the '<[^<]*' term in the following
    # regexp could be simplified to '<.*', which would indeed match
    # the same class of strings, the [^<] means that searching for the
    # regexp takes linear rather than quadratic time.
    if not Search(r'<[^<]*,\s*$', line):  # template params spill
      match = Search(r'[^<>=!\s](<)[^<>=!\s]([^>]|->)*$', line)
  if match:
    error(filename, linenum, 'whitespace/operators', 3,
          'Missing spaces around %s' % match.group(1))
  # We allow no-spaces around << and >> when used like this: 10<<20, but
  # not otherwise (particularly, not when used as streams)
  match = Search(r'[^0-9\s](<<|>>)[^0-9\s]', line)
  if match:
    error(filename, linenum, 'whitespace/operators', 3,
          'Missing spaces around %s' % match.group(1))

  # There shouldn't be space around unary operators
  match = Search(r'(!\s|~\s|[\s]--[\s;]|[\s]\+\+[\s;])', line)
  if match:
    error(filename, linenum, 'whitespace/operators', 4,
          'Extra space for operator %s' % match.group(1))

  # A pet peeve of mine: no spaces after an if, while, switch, or for
  match = Search(r'\s(if\s\(|for\s\(|while\s\(|switch\s\()', line)
  if match:
    error(filename, linenum, 'whitespace/parens', 5,
          'Extra space before ( in %s' % match.group(1))

  # For if/for/while/switch, the left and right parens should be
  # consistent about how many spaces are inside the parens, and
  # there should either be zero or one spaces inside the parens.
  # We don't want: "if ( foo)" or "if ( foo   )".
  # Exception: "for ( ; foo; bar)" and "for (foo; bar; )" are allowed.
  match = Search(r'\b(if|for|while|switch)\s*'
                 r'\(([ ]*)(.).*[^ ]+([ ]*)\)\s*{\s*$',
                 line)
  if match:
    if len(match.group(2)) != len(match.group(4)):
      if not (match.group(3) == ';' and
              len(match.group(2)) == 1 + len(match.group(4)) or
              not match.group(2) and Search(r'\bfor\s*\(.*; \)', line)):
        error(filename, linenum, 'whitespace/parens', 5,
              'Mismatching spaces inside () in %s' % match.group(1))
    if not len(match.group(2)) in [0, 1]:
      error(filename, linenum, 'whitespace/parens', 5,
            'Should have zero or one spaces inside ( and ) in %s' %
            match.group(1))

  # You should always have a space after a comma (either as fn arg or operator)
  if Search(r',[^\s]', line):
    error(filename, linenum, 'whitespace/comma', 3,
          'Missing space after ,')

  # You should always have a space after a semicolon
  # except for few corner cases
  # TODO(unknown): clarify if 'if (1) { return 1;}' is requires one more
  # space after ;
  if Search(r';[^\s};\\)/]', line):
    error(filename, linenum, 'whitespace/semicolon', 3,
          'Missing space after ;')

  # Next we will look for issues with function calls.
  CheckSpacingForFunctionCall(filename, line, linenum, error)

  # Except after an opening paren, or after another opening brace (in case of
  # an initializer list, for instance), you should have spaces before your
  # braces. And since you should never have braces at the beginning of a line,
  # this is an easy test.
  if Search(r'[^ (\t{]{', line):
    error(filename, linenum, 'whitespace/braces', 5,
          'Missing space before {')

  # Make sure '} else {' has spaces.
  if Search(r'}else', line):
    error(filename, linenum, 'whitespace/braces', 5,
          'Missing space before else')

  # You shouldn't have spaces before your brackets, except maybe after
  # 'delete []' or 'new char * []'.
  if Search(r'\w\s+\[', line) and not Search(r'delete\s+\[', line):
    error(filename, linenum, 'whitespace/braces', 5,
          'Extra space before [')

  # You shouldn't have a space before a semicolon at the end of the line.
  # There's a special case for "for" since the style guide allows space before
  # the semicolon there.
  if Search(r':\s*;\s*$', line):
    error(filename, linenum, 'whitespace/semicolon', 5,
          'Semicolon defining empty statement. Use { } instead.')
  elif Search(r'^\s*;\s*$', line):
    error(filename, linenum, 'whitespace/semicolon', 5,
          'Line contains only semicolon. If this should be an empty statement, '
          'use { } instead.')
  elif (Search(r'\s+;\s*$', line) and
        not Search(r'\bfor\b', line)):
    error(filename, linenum, 'whitespace/semicolon', 5,
          'Extra space before last semicolon. If this should be an empty '
          'statement, use { } instead.')


def CheckSectionSpacing(filename, clean_lines, class_info, linenum, error):
  """Checks for additional blank line issues related to sections.

  Currently the only thing checked here is blank line before protected/private.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    class_info: A _ClassInfo objects.
    linenum: The number of the line to check.
    error: The function to call with any errors found.
  """
  # Skip checks if the class is small, where small means 25 lines or less.
  # 25 lines seems like a good cutoff since that's the usual height of
  # terminals, and any class that can't fit in one screen can't really
  # be considered "small".
  #
  # Also skip checks if we are on the first line.  This accounts for
  # classes that look like
  #   class Foo { public: ... };
  #
  # If we didn't find the end of the class, last_line would be zero,
  # and the check will be skipped by the first condition.
  if (class_info.last_line - class_info.linenum <= 24 or
      linenum <= class_info.linenum):
    return

  matched = Match(r'\s*(public|protected|private):', clean_lines.lines[linenum])
  if matched:
    # Issue warning if the line before public/protected/private was
    # not a blank line, but don't do this if the previous line contains
    # "class" or "struct".  This can happen two ways:
    #  - We are at the beginning of the class.
    #  - We are forward-declaring an inner class that is semantically
    #    private, but needed to be public for implementation reasons.
    prev_line = clean_lines.lines[linenum - 1]
    if (not IsBlankLine(prev_line) and
        not Search(r'\b(class|struct)\b', prev_line)):
      # Try a bit harder to find the beginning of the class.  This is to
      # account for multi-line base-specifier lists, e.g.:
      #   class Derived
      #       : public Base {
      end_class_head = class_info.linenum
      for i in range(class_info.linenum, linenum):
        if Search(r'\{\s*$', clean_lines.lines[i]):
          end_class_head = i
          break
      if end_class_head < linenum - 1:
        error(filename, linenum, 'whitespace/blank_line', 3,
              '"%s:" should be preceded by a blank line' % matched.group(1))


def GetPreviousNonBlankLine(clean_lines, linenum):
  """Return the most recent non-blank line and its line number.

  Args:
    clean_lines: A CleansedLines instance containing the file contents.
    linenum: The number of the line to check.

  Returns:
    A tuple with two elements.  The first element is the contents of the last
    non-blank line before the current line, or the empty string if this is the
    first non-blank line.  The second is the line number of that line, or -1
    if this is the first non-blank line.
  """

  prevlinenum = linenum - 1
  while prevlinenum >= 0:
    prevline = clean_lines.elided[prevlinenum]
    if not IsBlankLine(prevline):     # if not a blank line...
      return (prevline, prevlinenum)
    prevlinenum -= 1
  return ('', -1)


def CheckBraces(filename, clean_lines, linenum, error):
  """Looks for misplaced braces (e.g. at the end of line).

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    error: The function to call with any errors found.
  """

  line = clean_lines.elided[linenum]        # get rid of comments and strings

  if Match(r'\s*{\s*$', line):
    # We allow an open brace to start a line in the case where someone
    # is using braces in a block to explicitly create a new scope,
    # which is commonly used to control the lifetime of
    # stack-allocated variables.  We don't detect this perfectly: we
    # just don't complain if the last non-whitespace character on the
    # previous non-blank line is ';', ':', '{', or '}'.
    prevline = GetPreviousNonBlankLine(clean_lines, linenum)[0]
    if not Search(r'[;:}{]\s*$', prevline):
      error(filename, linenum, 'whitespace/braces', 4,
            '{ should almost always be at the end of the previous line')

  # An else clause should be on the same line as the preceding closing brace.
  if Match(r'\s*else\s*', line):
    prevline = GetPreviousNonBlankLine(clean_lines, linenum)[0]
    if Match(r'\s*}\s*$', prevline):
      error(filename, linenum, 'whitespace/newline', 4,
            'An else should appear on the same line as the preceding }')

  # If braces come on one side of an else, they should be on both.
  # However, we have to worry about "else if" that spans multiple lines!
  if Search(r'}\s*else[^{]*$', line) or Match(r'[^}]*else\s*{', line):
    if Search(r'}\s*else if([^{]*)$', line):       # could be multi-line if
      # find the ( after the if
      pos = line.find('else if')
      pos = line.find('(', pos)
      if pos > 0:
        (endline, _, endpos) = CloseExpression(clean_lines, linenum, pos)
        if endline[endpos:].find('{') == -1:    # must be brace after if
          error(filename, linenum, 'readability/braces', 5,
                'If an else has a brace on one side, it should have it on both')
    else:            # common case: else not followed by a multi-line if
      error(filename, linenum, 'readability/braces', 5,
            'If an else has a brace on one side, it should have it on both')

  # Likewise, an else should never have the else clause on the same line
  if Search(r'\belse [^\s{]', line) and not Search(r'\belse if\b', line):
    error(filename, linenum, 'whitespace/newline', 4,
          'Else clause should never be on same line as else (use 2 lines)')

  # In the same way, a do/while should never be on one line
  if Match(r'\s*do [^\s{]', line):
    error(filename, linenum, 'whitespace/newline', 4,
          'do/while clauses should not be on a single line')

  # Braces shouldn't be followed by a ; unless they're defining a struct
  # or initializing an array.
  # We can't tell in general, but we can for some common cases.
  prevlinenum = linenum
  while True:
    (prevline, prevlinenum) = GetPreviousNonBlankLine(clean_lines, prevlinenum)
    if Match(r'\s+{.*}\s*;', line) and not prevline.count(';'):
      line = prevline + line
    else:
      break
  if (Search(r'{.*}\s*;', line) and
      line.count('{') == line.count('}') and
      not Search(r'struct|class|enum|\s*=\s*{', line)):
    error(filename, linenum, 'readability/braces', 4,
          "You don't need a ; after a }")


def ReplaceableCheck(operator, macro, line):
  """Determine whether a basic CHECK can be replaced with a more specific one.

  For example suggest using CHECK_EQ instead of CHECK(a == b) and
  similarly for CHECK_GE, CHECK_GT, CHECK_LE, CHECK_LT, CHECK_NE.

  Args:
    operator: The C++ operator used in the CHECK.
    macro: The CHECK or EXPECT macro being called.
    line: The current source line.

  Returns:
    True if the CHECK can be replaced with a more specific one.
  """

  # This matches decimal and hex integers, strings, and chars (in that order).
  match_constant = r'([-+]?(\d+|0[xX][0-9a-fA-F]+)[lLuU]{0,3}|".*"|\'.*\')'

  # Expression to match two sides of the operator with something that
  # looks like a literal, since CHECK(x == iterator) won't compile.
  # This means we can't catch all the cases where a more specific
  # CHECK is possible, but it's less annoying than dealing with
  # extraneous warnings.
  match_this = (r'\s*' + macro + r'\((\s*' +
                match_constant + r'\s*' + operator + r'[^<>].*|'
                r'.*[^<>]' + operator + r'\s*' + match_constant +
                r'\s*\))')

  # Don't complain about CHECK(x == NULL) or similar because
  # CHECK_EQ(x, NULL) won't compile (requires a cast).
  # Also, don't complain about more complex boolean expressions
  # involving && or || such as CHECK(a == b || c == d).
  return Match(match_this, line) and not Search(r'NULL|&&|\|\|', line)


def CheckCheck(filename, clean_lines, linenum, error):
  """Checks the use of CHECK and EXPECT macros.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    error: The function to call with any errors found.
  """

  # Decide the set of replacement macros that should be suggested
  raw_lines = clean_lines.raw_lines
  current_macro = ''
  for macro in _CHECK_MACROS:
    if raw_lines[linenum].find(macro) >= 0:
      current_macro = macro
      break
  if not current_macro:
    # Don't waste time here if line doesn't contain 'CHECK' or 'EXPECT'
    return

  line = clean_lines.elided[linenum]        # get rid of comments and strings

  # Encourage replacing plain CHECKs with CHECK_EQ/CHECK_NE/etc.
  for operator in ['==', '!=', '>=', '>', '<=', '<']:
    if ReplaceableCheck(operator, current_macro, line):
      error(filename, linenum, 'readability/check', 2,
            'Consider using %s instead of %s(a %s b)' % (
                _CHECK_REPLACEMENT[current_macro][operator],
                current_macro, operator))
      break


def GetLineWidth(line):
  """Determines the width of the line in column positions.

  Args:
    line: A string, which may be a Unicode string.

  Returns:
    The width of the line in column positions, accounting for Unicode
    combining characters and wide characters.
  """
  if isinstance(line, TEXT_TYPE):
    width = 0
    for uc in unicodedata.normalize('NFC', line):
      if unicodedata.east_asian_width(uc) in ('W', 'F'):
        width += 2
      elif not unicodedata.combining(uc):
        width += 1
    return width
  else:
    return len(line)


def CheckStyle(filename, clean_lines, linenum, file_extension, class_state,
               error):
  """Checks rules from the 'C++ style rules' section of cppguide.html.

  Most of these rules are hard to test (naming, comment style), but we
  do what we can.  In particular we check for 2-space indents, line lengths,
  tab usage, spaces inside code, etc.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    file_extension: The extension (without the dot) of the filename.
    error: The function to call with any errors found.
  """

  raw_lines = clean_lines.raw_lines
  line = raw_lines[linenum]

  if line.find('\t') != -1:
    error(filename, linenum, 'whitespace/tab', 1,
          'Tab found; better to use spaces')

  if linenum > 0:
    last_line  = raw_lines[linenum - 1]
    lasttabs = 0
    while lasttabs < len(last_line) and last_line[lasttabs] == '\t':
      lasttabs += 1
    for char in line:
      if not char.isspace():
        break
      if lasttabs == 0 and char != '\t':
        break
      if lasttabs == -1:
        if char == '\t' and last_line != '':
          error(filename, linenum, 'whitespace/align_tab', 4,
                'Too much indentation or tab used as alignment.')
        break
      if lasttabs > 0 and char != '\t':
        error(filename, linenum, 'whitespace/ident_space', 4,
                'Space used for identation, use tabs instead.')
        break
      lasttabs -= 1

  foundntab = 0
  for char in line:
    if char != '\t':
      foundntab = 1
    if foundntab and char == '\t':
      error(filename, linenum, 'whitespace/align_tab', 4,
                'Tab used for alignment, use spaces instead.')
      break

  # One or three blank spaces at the beginning of the line is weird; it's
  # hard to reconcile that with 2-space indents.
  # NOTE: here are the conditions rob pike used for his tests.  Mine aren't
  # as sophisticated, but it may be worth becoming so:  RLENGTH==initial_spaces
  # if(RLENGTH > 20) complain = 0;
  # if(match($0, " +(error|private|public|protected):")) complain = 0;
  # if(match(prev, "&& *$")) complain = 0;
  # if(match(prev, "\\|\\| *$")) complain = 0;
  # if(match(prev, "[\",=><] *$")) complain = 0;
  # if(match($0, " <<")) complain = 0;
  # if(match(prev, " +for \\(")) complain = 0;
  # if(prevodd && match(prevprev, " +for \\(")) complain = 0;
  cleansed_line = clean_lines.elided[linenum]
  if line and line[-1].isspace() and not line.isspace():
    error(filename, linenum, 'whitespace/end_of_line', 4,
          'Line ends in whitespace.  Consider deleting these extra spaces.')


  # Check if the line is a header guard.
  is_header_guard = False
  if file_extension in HEADER_EXTENSIONS:
    cppvar = GetHeaderGuardCPPVariable(filename)
    if (line.startswith('#ifndef %s' % cppvar) or
        line.startswith('#define %s' % cppvar) or
        line.startswith('#endif  // %s' % cppvar)):
      is_header_guard = True
  # #include lines and header guards can be long, since there's no clean way to
  # split them.
  #
  # URLs can be long too.  It's possible to split these, but it makes them
  # harder to cut&paste.
  #
  # The "$Id:...$" comment may also get very long without it being the
  # developers fault.
  if (not line.startswith('#include') and not is_header_guard and
      not Match(r'^\s*//.*http(s?)://\S*$', line) and
      not Match(r'^// \$Id:.*#[0-9]+ \$$', line)):
    line_width = GetLineWidth(line)
    if line_width > 120:
      error(filename, linenum, 'whitespace/line_length', 4,
            'Lines should very rarely be longer than 120 characters')

  if (cleansed_line.count(';') > 1 and
      # allow one-line definitions for small structs or classes
      not ((cleansed_line.find('struct ') != -1 or
            cleansed_line.find('class ') != -1) and
           cleansed_line.find('};') != -1) and
      # for loops are allowed two ;'s (and may run over two lines).
      cleansed_line.find('for') == -1 and
      (GetPreviousNonBlankLine(clean_lines, linenum)[0].find('for') == -1 or
       GetPreviousNonBlankLine(clean_lines, linenum)[0].find(';') != -1) and
      # It's ok to have many commands in a switch case that fits in 1 line
      not ((cleansed_line.find('case ') != -1 or
            cleansed_line.find('default:') != -1) and
           (cleansed_line.find('break;') != -1 or
            cleansed_line.find('return;') or
            cleansed_line.find('return ')))):
    error(filename, linenum, 'whitespace/newline', 4,
          'More than one command on the same line')

  # Some more style checks
  CheckBraces(filename, clean_lines, linenum, error)
  CheckSpacing(filename, clean_lines, linenum, error)
  CheckCheck(filename, clean_lines, linenum, error)
  if class_state and class_state.classinfo_stack:
    CheckSectionSpacing(filename, clean_lines,
                        class_state.classinfo_stack[-1], linenum, error)


_RE_PATTERN_INCLUDE_DUPLICATE = re.compile('// +duplicate-include')
_RE_PATTERN_INCLUDE_NEW_STYLE = re.compile(r'#include +"[^/]+\.h"')
_RE_PATTERN_INCLUDE_QT = re.compile(r'#include +"(ui_|moc_)[^/]+\.h"')
_RE_PATTERN_INCLUDE = re.compile(r'^\s*#\s*include\s*([<"])([^>"]*)[>"].*$')
# Matches the first component of a filename delimited by -s and _s. That is:
#  _RE_FIRST_COMPONENT.match('foo').group(0) == 'foo'
#  _RE_FIRST_COMPONENT.match('foo.cpp').group(0) == 'foo'
#  _RE_FIRST_COMPONENT.match('foo-bar_baz.cpp').group(0) == 'foo'
#  _RE_FIRST_COMPONENT.match('foo_bar-baz.cpp').group(0) == 'foo'
_RE_FIRST_COMPONENT = re.compile(r'^[^-_.]+')


def _DropCommonSuffixes(filename):
  """Drops common suffixes like _test.cpp or -inl.h from filename.

  For example:
    >>> _DropCommonSuffixes('foo/foo-inl.h')
    'foo/foo'
    >>> _DropCommonSuffixes('foo/bar/foo.cpp')
    'foo/bar/foo'
    >>> _DropCommonSuffixes('foo/foo_internal.h')
    'foo/foo'
    >>> _DropCommonSuffixes('foo/foo_unusualinternal.h')
    'foo/foo_unusualinternal'

  Args:
    filename: The input filename.

  Returns:
    The filename with the common suffix removed.
  """
  for suffix in ('test.cpp', 'regtest.cpp', 'unittest.cpp',
                 'inl.h', 'impl.h', 'internal.h'):
    if (filename.endswith(suffix) and len(filename) > len(suffix) and
        filename[-len(suffix) - 1] in ('-', '_')):
      return filename[:-len(suffix) - 1]
  return os.path.splitext(filename)[0]


def _IsTestFilename(filename):
  """Determines if the given filename has a suffix that identifies it as a test.

  Args:
    filename: The input filename.

  Returns:
    True if 'filename' looks like a test, False otherwise.
  """
  if (filename.endswith('_test.cpp') or
      filename.endswith('_unittest.cpp') or
      filename.endswith('_regtest.cpp')):
    return True
  else:
    return False


def _ClassifyInclude(fileinfo, include, is_system):
  """Figures out what kind of header 'include' is.

  Args:
    fileinfo: The current file cpplint is running over. A FileInfo instance.
    include: The path to a #included file.
    is_system: True if the #include used <> rather than "".

  Returns:
    One of the _XXX_HEADER constants.

  For example:
    >>> _ClassifyInclude(FileInfo('foo/foo.cpp'), 'stdio.h', True)
    _C_SYS_HEADER
    >>> _ClassifyInclude(FileInfo('foo/foo.cpp'), 'string', True)
    _CPP_SYS_HEADER
    >>> _ClassifyInclude(FileInfo('foo/foo.cpp'), 'foo/foo.h', False)
    _LIKELY_MY_HEADER
    >>> _ClassifyInclude(FileInfo('foo/foo_unknown_extension.cpp'),
    ...                  'bar/foo_other_ext.h', False)
    _POSSIBLE_MY_HEADER
    >>> _ClassifyInclude(FileInfo('foo/foo.cpp'), 'foo/bar.h', False)
    _OTHER_HEADER
  """
  # This is a list of all standard c++ header files, except
  # those already checked for above.
  is_stl_h = include in _STL_HEADERS
  is_cpp_h = is_stl_h or include in _CPP_HEADERS

  if is_system:
    if is_cpp_h:
      return _CPP_SYS_HEADER
    else:
      return _C_SYS_HEADER

  # If the target file and the include we're checking share a
  # basename when we drop common extensions, and the include
  # lives in . , then it's likely to be owned by the target file.
  target_dir, target_base = (
      os.path.split(_DropCommonSuffixes(fileinfo.RepositoryName())))
  include_dir, include_base = os.path.split(_DropCommonSuffixes(include))
  if target_base == include_base and (
      include_dir == target_dir or
      include_dir == os.path.normpath(target_dir + '/../public')):
    return _LIKELY_MY_HEADER

  # If the target and include share some initial basename
  # component, it's possible the target is implementing the
  # include, so it's allowed to be first, but we'll never
  # complain if it's not there.
  target_first_component = _RE_FIRST_COMPONENT.match(target_base)
  include_first_component = _RE_FIRST_COMPONENT.match(include_base)
  if (target_first_component and include_first_component and
      target_first_component.group(0) ==
      include_first_component.group(0)):
    return _POSSIBLE_MY_HEADER

  return _OTHER_HEADER



def CheckIncludeLine(filename, clean_lines, linenum, include_state, error):
  """Check rules that are applicable to #include lines.

  Strings on #include lines are NOT removed from elided line, to make
  certain tasks easier. However, to prevent false positives, checks
  applicable to #include lines in CheckLanguage must be put here.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    include_state: An _IncludeState instance in which the headers are inserted.
    error: The function to call with any errors found.
  """
  fileinfo = FileInfo(filename)

  line = clean_lines.lines[linenum]

  # "include" should use the new style "foo/bar.h" instead of just "bar.h"
  if _RE_PATTERN_INCLUDE_NEW_STYLE.search(line) and line != "#include \"Configure.h\"" and not  _RE_PATTERN_INCLUDE_QT.search(line):
    error(filename, linenum, 'build/include', 4,
          'Include the directory when naming .h files')

  # we shouldn't include a file more than once. actually, there are a
  # handful of instances where doing so is okay, but in general it's
  # not.
  match = _RE_PATTERN_INCLUDE.search(line)
  if match:
    include = match.group(2)
    is_system = (match.group(1) == '<')
    if include in include_state and not _RE_PATTERN_INCLUDE_DUPLICATE.search(clean_lines.raw_lines[linenum]):
      error(filename, linenum, 'build/include', 4,
            '"%s" already included at %s:%s' %
            (include, filename, include_state[include]))
    else:
      include_state[include] = linenum

      # We want to ensure that headers appear in the right order:
      # 1) for foo.cpp, foo.h  (preferred location)
      # 2) c system files
      # 3) cpp system files
      # 4) for foo.cpp, foo.h  (deprecated location)
      # 5) other google headers
      #
      # We classify each include statement as one of those 5 types
      # using a number of techniques. The include_state object keeps
      # track of the highest type seen, and complains if we see a
      # lower type after that.
      error_message = include_state.CheckNextIncludeOrder(
          _ClassifyInclude(fileinfo, include, is_system))
      if error_message:
        error(filename, linenum, 'build/include_order', 4,
              '%s. Should be: %s.h, c system, c++ system, other.' %
              (error_message, fileinfo.BaseName()))
      if not include_state.IsInAlphabeticalOrder(include):
        error(filename, linenum, 'build/include_alpha', 4,
              'Include "%s" not in alphabetical order' % include)

  # Look for any of the stream classes that are part of standard C++.
  match = _RE_PATTERN_INCLUDE.match(line)
  if match:
    include = match.group(2)
    if Match(r'(f|ind|io|i|o|parse|pf|stdio|str|)?stream$', include):
      # Many unit tests use cout, so we exempt them.
      if not _IsTestFilename(filename):
        error(filename, linenum, 'readability/streams', 3,
              'Streams are highly discouraged.')


def _GetTextInside(text, start_pattern):
  """Retrieves all the text between matching open and close parentheses.

  Given a string of lines and a regular expression string, retrieve all the text
  following the expression and between opening punctuation symbols like
  (, [, or {, and the matching close-punctuation symbol. This properly nested
  occurrences of the punctuations, so for the text like
    printf(a(), b(c()));
  a call to _GetTextInside(text, r'printf\\(') will return 'a(), b(c())'.
  start_pattern must match string having an open punctuation symbol at the end.

  Args:
    text: The lines to extract text. Its comments and strings must be elided.
           It can be single line and can span multiple lines.
    start_pattern: The regexp string indicating where to start extracting
                   the text.
  Returns:
    The extracted text.
    None if either the opening string or ending punctuation could not be found.
  """
  # TODO(sugawarayu): Audit cpplint.py to see what places could be profitably
  # rewritten to use _GetTextInside (and use inferior regexp matching today).

  # Give opening punctuations to get the matching close-punctuations.
  matching_punctuation = {'(': ')', '{': '}', '[': ']'}
  closing_punctuation = set(itervalues(matching_punctuation))

  # Find the position to start extracting text.
  match = re.search(start_pattern, text, re.M)
  if not match:  # start_pattern not found in text.
    return None
  start_position = match.end(0)

  assert start_position > 0, (
      'start_pattern must ends with an opening punctuation.')
  assert text[start_position - 1] in matching_punctuation, (
      'start_pattern must ends with an opening punctuation.')
  # Stack of closing punctuations we expect to have in text after position.
  punctuation_stack = [matching_punctuation[text[start_position - 1]]]
  position = start_position
  while punctuation_stack and position < len(text):
    if text[position] == punctuation_stack[-1]:
      punctuation_stack.pop()
    elif text[position] in closing_punctuation:
      # A closing punctuation without matching opening punctuations.
      return None
    elif text[position] in matching_punctuation:
      punctuation_stack.append(matching_punctuation[text[position]])
    position += 1
  if punctuation_stack:
    # Opening punctuations left without matching close-punctuations.
    return None
  # punctuations match.
  return text[start_position:position - 1]


def CheckLanguage(filename, clean_lines, linenum, file_extension, include_state,
                  error):
  """Checks rules from the 'C++ language rules' section of cppguide.html.

  Some of these rules are hard to test (function overloading, using
  uint32 inappropriately), but we do the best we can.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    file_extension: The extension (without the dot) of the filename.
    include_state: An _IncludeState instance in which the headers are inserted.
    error: The function to call with any errors found.
  """
  # If the line is empty or consists of entirely a comment, no need to
  # check it.
  line = clean_lines.elided[linenum]
  if not line:
    return

  match = _RE_PATTERN_INCLUDE.search(line)
  if match:
    CheckIncludeLine(filename, clean_lines, linenum, include_state, error)
    return

  # Create an extended_line, which is the concatenation of the current and
  # next lines, for more effective checking of code that may span more than one
  # line.
  if linenum + 1 < clean_lines.NumLines():
    extended_line = line + clean_lines.elided[linenum + 1]
  else:
    extended_line = line

  # Make Windows paths like Unix.
  fullname = os.path.abspath(filename).replace('\\', '/')

  # TODO(unknown): figure out if they're using default arguments in fn proto.

  # Check for non-const references in functions.  This is tricky because &
  # is also used to take the address of something.  We allow <> for templates,
  # (ignoring whatever is between the braces) and : for classes.
  # These are complicated re's.  They try to capture the following:
  # paren (for fn-prototype start), typename, &, varname.  For the const
  # version, we're willing for const to be before typename or after
  # Don't check the implementation on same line.
  fnline = line.split('{', 1)[0]
  if (len(re.findall(r'\([^()]*\b(?:[\w:]|<[^()]*>)+(\s?&|&\s?)\w+', fnline)) >
      len(re.findall(r'\([^()]*\bconst\s+(?:typename\s+)?(?:struct\s+)?'
                     r'(?:[\w:]|<[^()]*>)+(\s?&|&\s?)\w+', fnline)) +
      len(re.findall(r'\([^()]*\b(?:[\w:]|<[^()]*>)+\s+const(\s?&|&\s?)[\w]+',
                     fnline))):

    # We allow non-const references in a few standard places, like functions
    # called "swap()" or iostream operators like "<<" or ">>".
    if not Search(
        r'(swap|Swap|operator[<>][<>])\s*\(\s*(?:[\w:]|<.*>)+\s*&',
        fnline):
      error(filename, linenum, 'runtime/references', 2,
            'Is this a non-const reference? '
            'If so, make const or use a pointer.')

  # Check to see if they're using an conversion function cast.
  # I just try to capture the most common basic types, though there are more.
  # Parameterless conversion functions, such as bool(), are allowed as they are
  # probably a member operator declaration or default constructor.
  match = Search(
      r'(\bnew\s+)?\b'  # Grab 'new' operator, if it's there
      r'(int|float|double|bool|char|int32|uint32|int64|uint64)\([^)]', line)
  if match:
    # gMock methods are defined using some variant of MOCK_METHODx(name, type)
    # where type may be float(), int(string), etc.  Without context they are
    # virtually indistinguishable from int(x) casts. Likewise, gMock's
    # MockCallback takes a template parameter of the form return_type(arg_type),
    # which looks much like the cast we're trying to detect.
    if (match.group(1) is None and  # If new operator, then this isn't a cast
        not (Match(r'^\s*MOCK_(CONST_)?METHOD\d+(_T)?\(', line) or
             Match(r'^\s*MockCallback<.*>', line))):
      error(filename, linenum, 'readability/casting', 4,
            'Using deprecated casting style.  '
            'Use static_cast<%s>(...) instead' %
            match.group(2))

  CheckCStyleCast(filename, linenum, line, clean_lines.raw_lines[linenum],
                  'static_cast',
                  r'\((int|float|double|bool|char|u?int(16|32|64))\)', error)

  # This doesn't catch all cases. Consider (const char * const)"hello".
  #
  # (char *) "foo" should always be a const_cast (reinterpret_cast won't
  # compile).
  if CheckCStyleCast(filename, linenum, line, clean_lines.raw_lines[linenum],
                     'const_cast', r'\((char\s?\*+\s?)\)\s*"', error):
    pass
  else:
    # Check pointer casts for other than string constants
    CheckCStyleCast(filename, linenum, line, clean_lines.raw_lines[linenum],
                    'reinterpret_cast', r'\((\w+\s?\*+\s?)\)', error)

  # In addition, we look for people taking the address of a cast.  This
  # is dangerous -- casts can assign to temporaries, so the pointer doesn't
  # point where you think.
  if Search(
      r'(&\([^)]+\)[\w(])|(&(static|dynamic|reinterpret)_cast\b)', line):
    error(filename, linenum, 'runtime/casting', 4,
          ('Are you taking an address of a cast?  '
           'This is dangerous: could be a temp var.  '
           'Take the address before doing the cast, rather than after'))

  # Check for people declaring static/global STL strings at the top level.
  # This is dangerous because the C++ language does not guarantee that
  # globals with constructors are initialized before the first access.
  match = Match(
      r'((?:|static +)(?:|const +))string +([a-zA-Z0-9_:]+)\b(.*)',
      line)
  # Make sure it's not a function.
  # Function template specialization looks like: "string foo<Type>(...".
  # Class template definitions look like: "string Foo<Type>::Method(...".
  if match and not Match(r'\s*(<.*>)?(::[a-zA-Z0-9_]+)?\s*\(([^"]|$)',
                         match.group(3)):
    error(filename, linenum, 'runtime/string', 4,
          'For a static/global string constant, use a C style string instead: '
          '"%schar %s[]".' %
          (match.group(1), match.group(2)))

  # Check that we're not using RTTI outside of testing code.
  if Search(r'\bdynamic_cast<', line) and not _IsTestFilename(filename):
    error(filename, linenum, 'runtime/rtti', 5,
          'Do not use dynamic_cast<>.  If you need to cast within a class '
          "hierarchy, use static_cast<> to upcast.  Google doesn't support "
          'RTTI.')

  if Search(r'\b([A-Za-z0-9_]*_)\(\1\)', line):
    error(filename, linenum, 'runtime/init', 4,
          'You seem to be initializing a member variable with itself.')

  if file_extension in HEADER_EXTENSIONS:
    # TODO(unknown): check that 1-arg constructors are explicit.
    #                How to tell it's a constructor?
    #                (handled in CheckForNonStandardConstructs for now)
    # TODO(unknown): check that classes have DISALLOW_EVIL_CONSTRUCTORS
    #                (level 1 error)
    pass

  # Check if people are using the verboten C basic types.  The only exception
  # we regularly allow is "unsigned short port" for port.
  if Search(r'\bshort port\b', line):
    if not Search(r'\bunsigned short port\b', line):
      error(filename, linenum, 'runtime/int', 4,
            'Use "unsigned short" for ports, not "short"')
  else:
    match = Search(r'\b(short|long(?! +double)|long long)\b', line)
    if match:
      error(filename, linenum, 'runtime/int', 4,
            'Use int16/int64/etc, rather than the C type %s' % match.group(1))

  # When snprintf is used, the second argument shouldn't be a literal.
  match = Search(r'snprintf\s*\(([^,]*),\s*([0-9]*)\s*,', line)
  if match and match.group(2) != '0':
    # If 2nd arg is zero, snprintf is used to calculate size.
    error(filename, linenum, 'runtime/printf', 3,
          'If you can, use sizeof(%s) instead of %s as the 2nd arg '
          'to snprintf.' % (match.group(1), match.group(2)))

  # Check if some verboten C functions are being used.
  if Search(r'\bsprintf\b', line):
    error(filename, linenum, 'runtime/printf', 5,
          'Never use sprintf.  Use snprintf instead.')
  match = Search(r'\b(strcpy|strcat)\b', line)
  if match:
    error(filename, linenum, 'runtime/printf', 4,
          'Almost always, snprintf is better than %s' % match.group(1))

  if Search(r'\bsscanf\b', line):
    error(filename, linenum, 'runtime/printf', 1,
          'sscanf can be ok, but is slow and can overflow buffers.')

  # Check if some verboten operator overloading is going on
  # TODO(unknown): catch out-of-line unary operator&:
  #   class X {};
  #   int operator&(const X& x) { return 42; }  // unary operator&
  # The trick is it's hard to tell apart from binary operator&:
  #   class Y { int operator&(const Y& x) { return 23; } }; // binary operator&
  if Search(r'\boperator\s*&\s*\(\s*\)', line):
    error(filename, linenum, 'runtime/operator', 4,
          'Unary operator& is dangerous.  Do not use it.')

  # Check for suspicious usage of "if" like
  # } if (a == b) {
  if Search(r'\}\s*if\s*\(', line):
    error(filename, linenum, 'readability/braces', 4,
          'Did you mean "else if"? If not, start a new line for "if".')

  # Check for potential format string bugs like printf(foo).
  # We constrain the pattern not to pick things like DocidForPrintf(foo).
  # Not perfect but it can catch printf(foo.c_str()) and printf(foo->c_str())
  # TODO(sugawarayu): Catch the following case. Need to change the calling
  # convention of the whole function to process multiple line to handle it.
  #   printf(
  #       boy_this_is_a_really_long_variable_that_cannot_fit_on_the_prev_line);
  printf_args = _GetTextInside(line, r'(?i)\b(string)?printf\s*\(')
  if printf_args:
    match = Match(r'([\w.\->()]+)$', printf_args)
    if match:
      function_name = re.search(r'\b((?:string)?printf)\s*\(',
                                line, re.I).group(1)
      error(filename, linenum, 'runtime/printf', 4,
            'Potential format string bug. Do %s("%%s", %s) instead.'
            % (function_name, match.group(1)))

  # Check for potential memset bugs like memset(buf, sizeof(buf), 0).
  match = Search(r'memset\s*\(([^,]*),\s*([^,]*),\s*0\s*\)', line)
  if match and not Match(r"^''|-?[0-9]+|0x[0-9A-Fa-f]$", match.group(2)):
    error(filename, linenum, 'runtime/memset', 4,
          'Did you mean "memset(%s, 0, %s)"?'
          % (match.group(1), match.group(2)))

  if Search(r'\busing namespace\b', line):
    error(filename, linenum, 'build/namespaces', 5,
          'Do not use namespace using-directives.  '
          'Use using-declarations instead.')

  # Detect variable-length arrays.
  match = Match(r'\s*(.+::)?(\w+) [a-z]\w*\[(.+)];', line)
  if (match and match.group(2) != 'return' and match.group(2) != 'delete' and
      match.group(3).find(']') == -1):
    # Split the size using space and arithmetic operators as delimiters.
    # If any of the resulting tokens are not compile time constants then
    # report the error.
    tokens = re.split(r'\s|\+|\-|\*|\/|<<|>>]', match.group(3))
    is_const = True
    skip_next = False
    for tok in tokens:
      if skip_next:
        skip_next = False
        continue

      if Search(r'sizeof\(.+\)', tok): continue
      if Search(r'arraysize\(\w+\)', tok): continue

      tok = tok.lstrip('(')
      tok = tok.rstrip(')')
      if not tok: continue
      if Match(r'\d+', tok): continue
      if Match(r'0[xX][0-9a-fA-F]+', tok): continue
      if Match(r'k[A-Z0-9]\w*', tok): continue
      if Match(r'(.+::)?k[A-Z0-9]\w*', tok): continue
      if Match(r'(.+::)?[A-Z][A-Z0-9_]*', tok): continue
      # A catch all for tricky sizeof cases, including 'sizeof expression',
      # 'sizeof(*type)', 'sizeof(const type)', 'sizeof(struct StructName)'
      # requires skipping the next token because we split on ' ' and '*'.
      if tok.startswith('sizeof'):
        skip_next = True
        continue
      is_const = False
      break
    if not is_const:
      error(filename, linenum, 'runtime/arrays', 1,
            'Do not use variable-length arrays.  Use an appropriately named '
            "('k' followed by CamelCase) compile-time constant for the size.")

  # If DISALLOW_EVIL_CONSTRUCTORS, DISALLOW_COPY_AND_ASSIGN, or
  # DISALLOW_IMPLICIT_CONSTRUCTORS is present, then it should be the last thing
  # in the class declaration.
  match = Match(
      (r'\s*'
       r'(DISALLOW_(EVIL_CONSTRUCTORS|COPY_AND_ASSIGN|IMPLICIT_CONSTRUCTORS))'
       r'\(.*\);$'),
      line)
  if match and linenum + 1 < clean_lines.NumLines():
    next_line = clean_lines.elided[linenum + 1]
    # We allow some, but not all, declarations of variables to be present
    # in the statement that defines the class.  The [\w\*,\s]* fragment of
    # the regular expression below allows users to declare instances of
    # the class or pointers to instances, but not less common types such
    # as function pointers or arrays.  It's a tradeoff between allowing
    # reasonable code and avoiding trying to parse more C++ using regexps.
    if not Search(r'^\s*}[\w\*,\s]*;', next_line):
      error(filename, linenum, 'readability/constructors', 3,
            match.group(1) + ' should be the last thing in the class')

  # Check for use of unnamed namespaces in header files.  Registration
  # macros are typically OK, so we allow use of "namespace {" on lines
  # that end with backslashes.
  if (file_extension in HEADER_EXTENSIONS
      and Search(r'\bnamespace\s*{', line)
      and line[-1] != '\\'):
    error(filename, linenum, 'build/namespaces', 4,
          'Do not use unnamed namespaces in header files.  See '
          'http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Namespaces'
          ' for more information.')


def CheckCStyleCast(filename, linenum, line, raw_line, cast_type, pattern,
                    error):
  """Checks for a C-style cast by looking for the pattern.

  This also handles sizeof(type) warnings, due to similarity of content.

  Args:
    filename: The name of the current file.
    linenum: The number of the line to check.
    line: The line of code to check.
    raw_line: The raw line of code to check, with comments.
    cast_type: The string for the C++ cast to recommend.  This is either
      reinterpret_cast, static_cast, or const_cast, depending.
    pattern: The regular expression used to find C-style casts.
    error: The function to call with any errors found.

  Returns:
    True if an error was emitted.
    False otherwise.
  """
  match = Search(pattern, line)
  if not match:
    return False

  # e.g., sizeof(int)
  sizeof_match = Match(r'.*sizeof\s*$', line[0:match.start(1) - 1])
  if sizeof_match:
    error(filename, linenum, 'runtime/sizeof', 1,
          'Using sizeof(type).  Use sizeof(varname) instead if possible')
    return True

  remainder = line[match.end(0):]

  # The close paren is for function pointers as arguments to a function.
  # eg, void foo(void (*bar)(int));
  # The semicolon check is a more basic function check; also possibly a
  # function pointer typedef.
  # eg, void foo(int); or void foo(int) const;
  # The equals check is for function pointer assignment.
  # eg, void *(*foo)(int) = ...
  # The > is for MockCallback<...> ...
  #
  # Right now, this will only catch cases where there's a single argument, and
  # it's unnamed.  It should probably be expanded to check for multiple
  # arguments with some unnamed.
  function_match = Match(r'\s*(\)|=|(const)?\s*(;|\{|throw\(\)|>))', remainder)
  if function_match:
    if ((not function_match.group(3) or
        function_match.group(3) == ';' or
        ('MockCallback<' not in raw_line and
         '/*' not in raw_line)) and
        'SIGNAL' not in raw_line and
        'SLOT' not in raw_line):
      error(filename, linenum, 'readability/function', 3,
            'All parameters should be named in a function')
    return True

  # At this point, all that should be left is actual casts.
  error(filename, linenum, 'readability/casting', 4,
        'Using C-style cast.  Use %s<%s>(...) instead' %
        (cast_type, match.group(1)))

  return True


_HEADERS_CONTAINING_TEMPLATES = (
    ('<deque>', ('deque',)),
    ('<functional>', ('unary_function', 'binary_function',
                      'plus', 'minus', 'multiplies', 'divides', 'modulus',
                      'negate',
                      'equal_to', 'not_equal_to', 'greater', 'less',
                      'greater_equal', 'less_equal',
                      'logical_and', 'logical_or', 'logical_not',
                      'unary_negate', 'not1', 'binary_negate', 'not2',
                      'bind1st', 'bind2nd',
                      'pointer_to_unary_function',
                      'pointer_to_binary_function',
                      'ptr_fun',
                      'mem_fun_t', 'mem_fun', 'mem_fun1_t', 'mem_fun1_ref_t',
                      'mem_fun_ref_t',
                      'const_mem_fun_t', 'const_mem_fun1_t',
                      'const_mem_fun_ref_t', 'const_mem_fun1_ref_t',
                      'mem_fun_ref',
                     )),
    ('<limits>', ('numeric_limits',)),
    ('<list>', ('list',)),
    ('<map>', ('map', 'multimap',)),
    ('<memory>', ('allocator',)),
    ('<queue>', ('queue', 'priority_queue',)),
    ('<set>', ('set', 'multiset',)),
    ('<stack>', ('stack',)),
    ('<string>', ('char_traits', 'basic_string',)),
    ('<utility>', ('pair',)),
    ('<vector>', ('vector',)),

    # gcc extensions.
    # Note: std::hash is their hash, ::hash is our hash
    ('<hash_map>', ('hash_map', 'hash_multimap',)),
    ('<hash_set>', ('hash_set', 'hash_multiset',)),
    ('<slist>', ('slist',)),
    )

_RE_PATTERN_STRING = re.compile(r'\bstring\b')

_re_pattern_algorithm_header = []
for _template in ('copy', 'max', 'min', 'min_element', 'sort', 'swap',
                  'transform'):
  # Match max<type>(..., ...), max(..., ...), but not foo->max, foo.max or
  # type::max().
  _re_pattern_algorithm_header.append(
      (re.compile(r'[^>.]\b' + _template + r'(<.*?>)?\([^\)]'),
       _template,
       '<algorithm>'))

_re_pattern_templates = []
for _header, _templates in _HEADERS_CONTAINING_TEMPLATES:
  for _template in _templates:
    _re_pattern_templates.append(
        (re.compile(r'(\<|\b)' + _template + r'\s*\<'),
         _template + '<>',
         _header))


def FilesBelongToSameModule(filename_cc, filename_h):
  """Check if these two filenames belong to the same module.

  The concept of a 'module' here is a as follows:
  foo.h, foo-inl.h, foo.cpp, foo_test.cpp and foo_unittest.cpp belong to the
  same 'module' if they are in the same directory.
  some/path/public/xyzzy and some/path/internal/xyzzy are also considered
  to belong to the same module here.

  If the filename_cc contains a longer path than the filename_h, for example,
  '/absolute/path/to/base/sysinfo.cpp', and this file would include
  'base/sysinfo.h', this function also produces the prefix needed to open the
  header. This is used by the caller of this function to more robustly open the
  header file. We don't have access to the real include paths in this context,
  so we need this guesswork here.

  Known bugs: tools/base/bar.cpp and base/bar.h belong to the same module
  according to this implementation. Because of this, this function gives
  some false positives. This should be sufficiently rare in practice.

  Args:
    filename_cc: is the path for the .cpp file
    filename_h: is the path for the header path

  Returns:
    Tuple with a bool and a string:
    bool: True if filename_cc and filename_h belong to the same module.
    string: the additional prefix needed to open the header file.
  """

  if not filename_cc.endswith('.cpp'):
    return (False, '')
  filename_cc = filename_cc[:-len('.cpp')]
  if filename_cc.endswith('_unittest'):
    filename_cc = filename_cc[:-len('_unittest')]
  elif filename_cc.endswith('_test'):
    filename_cc = filename_cc[:-len('_test')]
  filename_cc = filename_cc.replace('/public/', '/')
  filename_cc = filename_cc.replace('/internal/', '/')

  if not filename_h.endswith('.h'):
    return (False, '')
  filename_h = filename_h[:-len('.h')]
  if filename_h.endswith('-inl'):
    filename_h = filename_h[:-len('-inl')]
  filename_h = filename_h.replace('/public/', '/')
  filename_h = filename_h.replace('/internal/', '/')

  files_belong_to_same_module = filename_cc.endswith(filename_h)
  common_path = ''
  if files_belong_to_same_module:
    common_path = filename_cc[:-len(filename_h)]
  return files_belong_to_same_module, common_path


def UpdateIncludeState(filename, include_state, io=codecs):
  """Fill up the include_state with new includes found from the file.

  Args:
    filename: the name of the header to read.
    include_state: an _IncludeState instance in which the headers are inserted.
    io: The io factory to use to read the file. Provided for testability.

  Returns:
    True if a header was succesfully added. False otherwise.
  """
  headerfile = None
  try:
    headerfile = io.open(filename, 'r', 'utf8', 'replace')
  except IOError:
    return False
  linenum = 0
  for line in headerfile:
    linenum += 1
    clean_line = CleanseComments(line)
    match = _RE_PATTERN_INCLUDE.search(clean_line)
    if match:
      include = match.group(2)
      # The value formatting is cute, but not really used right now.
      # What matters here is that the key is in include_state.
      include_state.setdefault(include, '%s:%d' % (filename, linenum))
  return True


def CheckForIncludeWhatYouUse(filename, clean_lines, include_state, error,
                              io=codecs):
  """Reports for missing stl includes.

  This function will output warnings to make sure you are including the headers
  necessary for the stl containers and functions that you use. We only give one
  reason to include a header. For example, if you use both equal_to<> and
  less<> in a .h file, only one (the latter in the file) of these will be
  reported as a reason to include the <functional>.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    include_state: An _IncludeState instance.
    error: The function to call with any errors found.
    io: The IO factory to use to read the header file. Provided for unittest
        injection.
  """
  required = {}  # A map of header name to linenumber and the template entity.
                 # Example of required: { '<functional>': (1219, 'less<>') }

  for linenum in range(clean_lines.NumLines()):
    line = clean_lines.elided[linenum]
    if not line or line[0] == '#':
      continue

    # String is special -- it is a non-templatized type in STL.
    matched = _RE_PATTERN_STRING.search(line)
    if matched:
      # Don't warn about strings in non-STL namespaces:
      # (We check only the first match per line; good enough.)
      prefix = line[:matched.start()]
      if prefix.endswith('std::') or not prefix.endswith('::'):
        required['<string>'] = (linenum, 'string')

    for pattern, template, header in _re_pattern_algorithm_header:
      if pattern.search(line):
        required[header] = (linenum, template)

    # The following function is just a speed up, no semantics are changed.
    if not '<' in line:  # Reduces the cpu time usage by skipping lines.
      continue

    for pattern, template, header in _re_pattern_templates:
      if pattern.search(line):
        required[header] = (linenum, template)

  # The policy is that if you #include something in foo.h you don't need to
  # include it again in foo.cpp. Here, we will look at possible includes.
  # Let's copy the include_state so it is only messed up within this function.
  include_state = include_state.copy()

  # Did we find the header for this file (if any) and succesfully load it?
  header_found = False

  # Use the absolute path so that matching works properly.
  abs_filename = FileInfo(filename).FullName()

  # For Emacs's flymake.
  # If cpplint is invoked from Emacs's flymake, a temporary file is generated
  # by flymake and that file name might end with '_flymake.cpp'. In that case,
  # restore original file name here so that the corresponding header file can be
  # found.
  # e.g. If the file name is 'foo_flymake.cpp', we should search for 'foo.h'
  # instead of 'foo_flymake.h'
  abs_filename = re.sub(r'_flymake\.cpp$', '.cpp', abs_filename)

  # include_state is modified during iteration, so we iterate over a copy of
  # the keys.
  header_keys = list(include_state.keys())
  for header in header_keys:
    (same_module, common_path) = FilesBelongToSameModule(abs_filename, header)
    fullpath = common_path + header
    if same_module and UpdateIncludeState(fullpath, include_state, io):
      header_found = True

  # If we can't find the header file for a .cpp, assume it's because we don't
  # know where to look. In that case we'll give up as we're not sure they
  # didn't include it in the .h file.
  # TODO(unknown): Do a better job of finding .h files so we are confident that
  # not having the .h file means there isn't one.
  if filename.endswith('.cpp') and not header_found:
    return

  # All the lines have been processed, report the errors found.
  for required_header_unstripped in required:
    template = required[required_header_unstripped][1]
    if required_header_unstripped.strip('<>"') not in include_state:
      error(filename, required[required_header_unstripped][0],
            'build/include_what_you_use', 4,
            'Add #include ' + required_header_unstripped + ' for ' + template)


_RE_PATTERN_EXPLICIT_MAKEPAIR = re.compile(r'\bmake_pair\s*<')


def CheckMakePairUsesDeduction(filename, clean_lines, linenum, error):
  """Check that make_pair's template arguments are deduced.

  G++ 4.6 in C++0x mode fails badly if make_pair's template arguments are
  specified explicitly, and such use isn't intended in any case.

  Args:
    filename: The name of the current file.
    clean_lines: A CleansedLines instance containing the file.
    linenum: The number of the line to check.
    error: The function to call with any errors found.
  """
  raw = clean_lines.raw_lines
  line = raw[linenum]
  match = _RE_PATTERN_EXPLICIT_MAKEPAIR.search(line)
  if match:
    error(filename, linenum, 'build/explicit_make_pair',
          4,  # 4 = high confidence
          'Omit template arguments from make_pair OR use pair directly OR'
          ' if appropriate, construct a pair directly')


def ProcessLine(filename, file_extension,
                clean_lines, line, include_state, function_state,
                class_state, error, extra_check_functions=[]):
  """Processes a single line in the file.

  Args:
    filename: Filename of the file that is being processed.
    file_extension: The extension (dot not included) of the file.
    clean_lines: An array of strings, each representing a line of the file,
                 with comments stripped.
    line: Number of line being processed.
    include_state: An _IncludeState instance in which the headers are inserted.
    function_state: A _FunctionState instance which counts function lines, etc.
    class_state: A _ClassState instance which maintains information about
                 the current stack of nested class declarations being parsed.
    error: A callable to which errors are reported, which takes 4 arguments:
           filename, line number, error level, and message
    extra_check_functions: An array of additional check functions that will be
                           run on each source line. Each function takes 4
                           arguments: filename, clean_lines, line, error
  """
  raw_lines = clean_lines.raw_lines
  ParseNolintSuppressions(filename, raw_lines[line], line, error)
  CheckForFunctionLengths(filename, clean_lines, line, function_state, error)
  CheckForMultilineCommentsAndStrings(filename, clean_lines, line, error)
  CheckStyle(filename, clean_lines, line, file_extension, class_state, error)
  CheckLanguage(filename, clean_lines, line, file_extension, include_state,
                error)
  CheckForNonStandardConstructs(filename, clean_lines, line,
                                class_state, error)
  CheckPosixThreading(filename, clean_lines, line, error)
  CheckInvalidIncrement(filename, clean_lines, line, error)
  CheckMakePairUsesDeduction(filename, clean_lines, line, error)
  for check_fn in extra_check_functions:
    check_fn(filename, clean_lines, line, error)

def ProcessFileData(filename, file_extension, lines, error,
                    extra_check_functions=[]):
  """Performs lint checks and reports any errors to the given error function.

  Args:
    filename: Filename of the file that is being processed.
    file_extension: The extension (dot not included) of the file.
    lines: An array of strings, each representing a line of the file, with the
           last element being empty if the file is terminated with a newline.
    error: A callable to which errors are reported, which takes 4 arguments:
           filename, line number, error level, and message
    extra_check_functions: An array of additional check functions that will be
                           run on each source line. Each function takes 4
                           arguments: filename, clean_lines, line, error
  """
  lines = (['// marker so line numbers and indices both start at 1'] + lines +
           ['// marker so line numbers end in a known way'])

  include_state = _IncludeState()
  function_state = _FunctionState()
  class_state = _ClassState()

  ResetNolintSuppressions()

  CheckForCopyright(filename, lines, error)

  if file_extension in HEADER_EXTENSIONS:
    CheckForHeaderGuard(filename, lines, error)

  RemoveMultiLineComments(filename, lines, error)
  clean_lines = CleansedLines(lines)
  for line in range(clean_lines.NumLines()):
    ProcessLine(filename, file_extension, clean_lines, line,
                include_state, function_state, class_state, error,
                extra_check_functions)
  class_state.CheckFinished(filename, error)

  CheckForIncludeWhatYouUse(filename, clean_lines, include_state, error)

  # We check here rather than inside ProcessLine so that we see raw
  # lines rather than "cleaned" lines.
  CheckForUnicodeReplacementCharacters(filename, lines, error)

  CheckForNewlineAtEOF(filename, lines, error)

def ProcessFile(filename, vlevel, extra_check_functions=[]):
  """Does google-lint on a single file.

  Args:
    filename: The name of the file to parse.

    vlevel: The level of errors to report.  Every error of confidence
    >= verbose_level will be reported.  0 is a good default.

    extra_check_functions: An array of additional check functions that will be
                           run on each source line. Each function takes 4
                           arguments: filename, clean_lines, line, error
  """

  _SetVerboseLevel(vlevel)

  try:
    # Support the UNIX convention of using "-" for stdin.  Note that
    # we are not opening the file with universal newline support
    # (which codecs doesn't support anyway), so the resulting lines do
    # contain trailing '\r' characters if we are reading a file that
    # has CRLF endings.
    # If after the split a trailing '\r' is present, it is removed
    # and a a warning is issued below if this file is processed.

    if filename == '-':
      lines = codecs.StreamReaderWriter(sys.stdin,
                                        codecs.getreader('utf8'),
                                        codecs.getwriter('utf8'),
                                        'replace').read().split('\n')
    else:
      lines = codecs.open(filename, 'r', 'utf8', 'replace').read().split('\n')

    carriage_return_found = False
    # Remove trailing '\r'.
    for linenum in range(len(lines)):
      if lines[linenum].endswith('\r'):
        lines[linenum] = lines[linenum].rstrip('\r')
        carriage_return_found = True

  except IOError:
    sys.stderr.write(
        "Skipping input '%s': Can't open for reading\n" % filename)
    return

  # Note, if no dot is found, this will give the entire filename as the ext.
  file_extension = filename[filename.rfind('.') + 1:]

  # When reading from stdin, the extension is unknown, so no cpplint tests
  # should rely on the extension.
  if (filename != '-' and file_extension not in EXTENSIONS):
    sys.stderr.write('Ignoring %s; extension not in %s\n' % (filename, EXTENSIONS))
  else:
    ProcessFileData(filename, file_extension, lines, Error,
                    extra_check_functions)
    if carriage_return_found:
      # Use 0 for linenum since outputting only one error for potentially
      # several lines.
      Error(filename, 0, 'whitespace/carriage-return', 1,
            'One or more unexpected \\r (^M) found;'
            'better to use only a \\n')

  sys.stderr.write('Done processing %s\n' % filename)


def PrintUsage(message):
  """Prints a brief usage string and exits, optionally with an error message.

  Args:
    message: The optional error message.
  """
  sys.stderr.write(_USAGE)

  if message:
    sys.exit('\nFATAL ERROR: ' + message)
  else:
    sys.exit(1)


def PrintCategories():
  """Prints a list of all the error-categories used by error messages.

  These are the categories used to filter messages via --filter.
  """
  sys.stderr.write(''.join('  %s\n' % cat for cat in _ERROR_CATEGORIES))
  sys.exit(0)


def ParseArguments(args):
  """Parses the command line arguments.

  This may set the output format and verbosity level as side-effects.

  Args:
    args: The command line arguments:

  Returns:
    The list of filenames to lint.
  """
  try:
    (opts, filenames) = getopt.getopt(args, '', ['help', 'output=', 'verbose=',
                                                 'project=',
                                                 'counting=',
                                                 'filter='])
  except getopt.GetoptError:
    PrintUsage('Invalid arguments.')

  project_name = _ProjectName()
  verbosity = _VerboseLevel()
  output_format = _OutputFormat()
  filters = ''
  counting_style = ''

  for (opt, val) in opts:
    if opt == '--help':
      PrintUsage(None)
    elif opt == '--output':
      if not val in ('emacs', 'vs7'):
        PrintUsage('The only allowed output formats are emacs and vs7.')
      output_format = val
    elif opt == '--project':
      project_name = val
    elif opt == '--verbose':
      verbosity = int(val)
    elif opt == '--filter':
      filters = val
      if not filters:
        PrintCategories()
    elif opt == '--counting':
      if val not in ('total', 'toplevel', 'detailed'):
        PrintUsage('Valid counting options are total, toplevel, and detailed')
      counting_style = val

  if not filenames:
    PrintUsage('No files were specified.')

  _SetOutputFormat(output_format)
  _SetProjectName(project_name)
  _SetVerboseLevel(verbosity)
  _SetFilters(filters)
  _SetCountingStyle(counting_style)

  return filenames


def main():
  filenames = ParseArguments(sys.argv[1:])
  backup_err = sys.stderr
  try:
    # Change stderr to write with replacement characters so we don't die
    # if we try to print something containing non-ASCII characters.
    sys.stderr = codecs.StreamReader(sys.stderr,
                                     'replace')
    _cpplint_state.ResetErrorCounts()
    for filename in filenames:
      ProcessFile(filename, _cpplint_state.verbose_level)
    _cpplint_state.PrintErrorCounts()
  finally:
    sys.stderr = backup_err

  sys.exit(_cpplint_state.error_count > 0)


if __name__ == '__main__':
  main()
```

## File: `cmake/check/cxx11-alignof.cpp`
```cpp
int main() {
	return alignof(int) != 1;
}
```

## File: `cmake/check/cxx11-std-codecvt_utf8_utf16.cpp`
```cpp
#include <codecvt>

int main() {
	std::codecvt_utf8_utf16<wchar_t> codecvt;
	return 0;
}
```

## File: `cmake/check/cxx11-std-unique_ptr.cpp`
```cpp
#include <memory>

int main() {
	std::unique_ptr<char> ptr(new char);
	return !ptr;
}
```

## File: `doc/Doxyfile.in`
```
# Doxyfile 1.8.1

# This file describes the settings to be used by the documentation system
# doxygen (www.doxygen.org) for a project.
#
# All text after a hash (#) is considered a comment and will be ignored.
# The format is:
#       TAG = value [value, ...]
# For lists items can also be appended using:
#       TAG += value [value, ...]
# Values that contain spaces should be placed between quotes (" ").

#---------------------------------------------------------------------------
# Project related configuration options
#---------------------------------------------------------------------------

# This tag specifies the encoding used for all characters in the config file
# that follow. The default is UTF-8 which is also the encoding used for all
# text before the first occurrence of this tag. Doxygen uses libiconv (or the
# iconv built into libc) for the transcoding. See
# http://www.gnu.org/software/libiconv for the list of possible encodings.

DOXYFILE_ENCODING      = UTF-8

# The PROJECT_NAME tag is a single word (or sequence of words) that should
# identify the project. Note that if you do not use Doxywizard you need
# to put quotes around the project name if it contains spaces.

PROJECT_NAME           = "${BASE_NAME_0}"

# The PROJECT_NUMBER tag can be used to enter a project or revision number.
# This could be handy for archiving the generated documentation or
# if some version control system is used.

PROJECT_NUMBER         = "${BASE_NUMBER_0}${GIT_SUFFIX_5}"

# Using the PROJECT_BRIEF tag one can provide an optional one line description
# for a project that appears at the top of each page and should give viewer
# a quick idea about the purpose of the project. Keep the description short.

PROJECT_BRIEF          =

# With the PROJECT_LOGO tag one can specify an logo or icon that is
# included in the documentation. The maximum height of the logo should not
# exceed 55 pixels and the maximum width should not exceed 200 pixels.
# Doxygen will copy the logo to the output directory.

PROJECT_LOGO           =

# The OUTPUT_DIRECTORY tag is used to specify the (relative or absolute)
# base path where the generated documentation will be put.
# If a relative path is entered, it will be relative to the location
# where doxygen was started. If left blank the current directory will be used.

OUTPUT_DIRECTORY       = "${DOXYGEN_OUTPUT_DIR}"

# If the CREATE_SUBDIRS tag is set to YES, then doxygen will create
# 4096 sub-directories (in 2 levels) under the output directory of each output
# format and will distribute the generated files over these directories.
# Enabling this option can be useful when feeding doxygen a huge amount of
# source files, where putting all generated files in the same directory would
# otherwise cause performance problems for the file system.

CREATE_SUBDIRS         = NO

# The OUTPUT_LANGUAGE tag is used to specify the language in which all
# documentation generated by doxygen is written. Doxygen will use this
# information to generate all constant output in the proper language.
# The default language is English, other supported languages are:
# Afrikaans, Arabic, Brazilian, Catalan, Chinese, Chinese-Traditional,
# Croatian, Czech, Danish, Dutch, Esperanto, Farsi, Finnish, French, German,
# Greek, Hungarian, Italian, Japanese, Japanese-en (Japanese with English
# messages), Korean, Korean-en, Lithuanian, Norwegian, Macedonian, Persian,
# Polish, Portuguese, Romanian, Russian, Serbian, Serbian-Cyrillic, Slovak,
# Slovene, Spanish, Swedish, Ukrainian, and Vietnamese.

OUTPUT_LANGUAGE        = English

# If the BRIEF_MEMBER_DESC tag is set to YES (the default) Doxygen will
# include brief member descriptions after the members that are listed in
# the file and class documentation (similar to JavaDoc).
# Set to NO to disable this.

BRIEF_MEMBER_DESC      = YES

# If the REPEAT_BRIEF tag is set to YES (the default) Doxygen will prepend
# the brief description of a member or function before the detailed description.
# Note: if both HIDE_UNDOC_MEMBERS and BRIEF_MEMBER_DESC are set to NO, the
# brief descriptions will be completely suppressed.

REPEAT_BRIEF           = YES

# This tag implements a quasi-intelligent brief description abbreviator
# that is used to form the text in various listings. Each string
# in this list, if found as the leading text of the brief description, will be
# stripped from the text and the result after processing the whole list, is
# used as the annotated text. Otherwise, the brief description is used as-is.
# If left blank, the following values are used ("$name" is automatically
# replaced with the name of the entity): "The $name class" "The $name widget"
# "The $name file" "is" "provides" "specifies" "contains"
# "represents" "a" "an" "the"

ABBREVIATE_BRIEF       = "The $name class" \
                         "The $name widget" \
                         "The $name file" \
                         is \
                         provides \
                         specifies \
                         contains \
                         represents \
                         a \
                         an \
                         the

# If the ALWAYS_DETAILED_SEC and REPEAT_BRIEF tags are both set to YES then
# Doxygen will generate a detailed section even if there is only a brief
# description.

ALWAYS_DETAILED_SEC    = NO

# If the INLINE_INHERITED_MEMB tag is set to YES, doxygen will show all
# inherited members of a class in the documentation of that class as if those
# members were ordinary class members. Constructors, destructors and assignment
# operators of the base classes will not be shown.

INLINE_INHERITED_MEMB  = NO

# If the FULL_PATH_NAMES tag is set to YES then Doxygen will prepend the full
# path before files name in the file list and in the header files. If set
# to NO the shortest path that makes the file name unique will be used.

FULL_PATH_NAMES        = YES

# If the FULL_PATH_NAMES tag is set to YES then the STRIP_FROM_PATH tag
# can be used to strip a user-defined part of the path. Stripping is
# only done if one of the specified strings matches the left-hand part of
# the path. The tag can be used to show relative paths in the file list.
# If left blank the directory from which doxygen is run is used as the
# path to strip.

STRIP_FROM_PATH        = src

# The STRIP_FROM_INC_PATH tag can be used to strip a user-defined part of
# the path mentioned in the documentation of a class, which tells
# the reader which header file to include in order to use a class.
# If left blank only the name of the header file containing the class
# definition is used. Otherwise one should specify the include paths that
# are normally passed to the compiler using the -I flag.

STRIP_FROM_INC_PATH    = src

# If the SHORT_NAMES tag is set to YES, doxygen will generate much shorter
# (but less readable) file names. This can be useful if your file system
# doesn't support long names like on DOS, Mac, or CD-ROM.

SHORT_NAMES            = NO

# If the JAVADOC_AUTOBRIEF tag is set to YES then Doxygen
# will interpret the first line (until the first dot) of a JavaDoc-style
# comment as the brief description. If set to NO, the JavaDoc
# comments will behave just like regular Qt-style comments
# (thus requiring an explicit @brief command for a brief description.)

JAVADOC_AUTOBRIEF      = YES

# If the QT_AUTOBRIEF tag is set to YES then Doxygen will
# interpret the first line (until the first dot) of a Qt-style
# comment as the brief description. If set to NO, the comments
# will behave just like regular Qt-style comments (thus requiring
# an explicit \brief command for a brief description.)

QT_AUTOBRIEF           = YES

# The MULTILINE_CPP_IS_BRIEF tag can be set to YES to make Doxygen
# treat a multi-line C++ special comment block (i.e. a block of //! or ///
# comments) as a brief description. This used to be the default behaviour.
# The new default is to treat a multi-line C++ comment block as a detailed
# description. Set this tag to YES if you prefer the old behaviour instead.

MULTILINE_CPP_IS_BRIEF = NO

# If the INHERIT_DOCS tag is set to YES (the default) then an undocumented
# member inherits the documentation from any documented member that it
# re-implements.

INHERIT_DOCS           = YES

# If the SEPARATE_MEMBER_PAGES tag is set to YES, then doxygen will produce
# a new page for each member. If set to NO, the documentation of a member will
# be part of the file/class/namespace that contains it.

SEPARATE_MEMBER_PAGES  = NO

# The TAB_SIZE tag can be used to set the number of spaces in a tab.
# Doxygen uses this value to replace tabs by spaces in code fragments.

TAB_SIZE               = 2

# This tag can be used to specify a number of aliases that acts
# as commands in the documentation. An alias has the form "name=value".
# For example adding "sideeffect=\par Side Effects:\n" will allow you to
# put the command \sideeffect (or @sideeffect) in the documentation, which
# will result in a user-defined paragraph with heading "Side Effects:".
# You can put \n's in the value part of an alias to insert newlines.

ALIASES                = 

# Set the OPTIMIZE_OUTPUT_FOR_C tag to YES if your project consists of C
# sources only. Doxygen will then generate output that is more tailored for C.
# For instance, some of the names that are used will be different. The list
# of all members will be omitted, etc.

OPTIMIZE_OUTPUT_FOR_C  = NO

# Set the OPTIMIZE_OUTPUT_JAVA tag to YES if your project consists of Java
# sources only. Doxygen will then generate output that is more tailored for
# Java. For instance, namespaces will be presented as packages, qualified
# scopes will look different, etc.

OPTIMIZE_OUTPUT_JAVA   = NO

# Set the OPTIMIZE_FOR_FORTRAN tag to YES if your project consists of Fortran
# sources only. Doxygen will then generate output that is more tailored for
# Fortran.

OPTIMIZE_FOR_FORTRAN   = NO

# Set the OPTIMIZE_OUTPUT_VHDL tag to YES if your project consists of VHDL
# sources. Doxygen will then generate output that is tailored for
# VHDL.

OPTIMIZE_OUTPUT_VHDL   = NO

# Doxygen selects the parser to use depending on the extension of the files it
# parses. With this tag you can assign which parser to use for a given extension.
# Doxygen has a built-in mapping, but you can override or extend it using this
# tag. The format is ext=language, where ext is a file extension, and language
# is one of the parsers supported by doxygen: IDL, Java, Javascript, CSharp, C,
# C++, D, PHP, Objective-C, Python, Fortran, VHDL, C, C++. For instance to make
# doxygen treat .inc files as Fortran files (default is PHP), and .f files as C
# (default is Fortran), use: inc=Fortran f=C. Note that for custom extensions
# you also need to set FILE_PATTERNS otherwise the files are not read by doxygen.

EXTENSION_MAPPING      = h=C++ cpp.in=C++ hpp.in=C++

# If MARKDOWN_SUPPORT is enabled (the default) then doxygen pre-processes all
# comments according to the Markdown format, which allows for more readable
# documentation. See http://daringfireball.net/projects/markdown/ for details.
# The output of markdown processing is further processed by doxygen, so you
# can mix doxygen, HTML, and XML commands with Markdown formatting.
# Disable only in case of backward compatibilities issues.

MARKDOWN_SUPPORT       = YES

# If you use STL classes (i.e. std::string, std::vector, etc.) but do not want
# to include (a tag file for) the STL sources as input, then you should
# set this tag to YES in order to let doxygen match functions declarations and
# definitions whose arguments contain STL classes (e.g. func(std::string); v.s.
# func(std::string) {}). This also makes the inheritance and collaboration
# diagrams that involve STL classes more complete and accurate.

BUILTIN_STL_SUPPORT    = YES

# If you use Microsoft's C++/CLI language, you should set this option to YES to
# enable parsing support.

CPP_CLI_SUPPORT        = NO

# Set the SIP_SUPPORT tag to YES if your project consists of sip sources only.
# Doxygen will parse them like normal C++ but will assume all classes use public
# instead of private inheritance when no explicit protection keyword is present.

SIP_SUPPORT            = NO

# For Microsoft's IDL there are propget and propput attributes to indicate getter
# and setter methods for a property. Setting this option to YES (the default)
# will make doxygen replace the get and set methods by a property in the
# documentation. This will only work if the methods are indeed getting or
# setting a simple type. If this is not the case, or you want to show the
# methods anyway, you should set this option to NO.

IDL_PROPERTY_SUPPORT   = YES

# If member grouping is used in the documentation and the DISTRIBUTE_GROUP_DOC
# tag is set to YES, then doxygen will reuse the documentation of the first
# member in the group (if any) for the other members of the group. By default
# all members of a group must be documented explicitly.

DISTRIBUTE_GROUP_DOC   = NO

# Set the SUBGROUPING tag to YES (the default) to allow class member groups of
# the same type (for instance a group of public functions) to be put as a
# subgroup of that type (e.g. under the Public Functions section). Set it to
# NO to prevent subgrouping. Alternatively, this can be done per class using
# the \nosubgrouping command.

SUBGROUPING            = YES

# When the INLINE_GROUPED_CLASSES tag is set to YES, classes, structs and
# unions are shown inside the group in which they are included (e.g. using
# @ingroup) instead of on a separate page (for HTML and Man pages) or
# section (for LaTeX and RTF).

INLINE_GROUPED_CLASSES = NO

# When the INLINE_SIMPLE_STRUCTS tag is set to YES, structs, classes, and
# unions with only public data fields will be shown inline in the documentation
# of the scope in which they are defined (i.e. file, namespace, or group
# documentation), provided this scope is documented. If set to NO (the default),
# structs, classes, and unions are shown on a separate page (for HTML and Man
# pages) or section (for LaTeX and RTF).

INLINE_SIMPLE_STRUCTS  = NO

# When TYPEDEF_HIDES_STRUCT is enabled, a typedef of a struct, union, or enum
# is documented as struct, union, or enum with the name of the typedef. So
# typedef struct TypeS {} TypeT, will appear in the documentation as a struct
# with name TypeT. When disabled the typedef will appear as a member of a file,
# namespace, or class. And the struct will be named TypeS. This can typically
# be useful for C code in case the coding convention dictates that all compound
# types are typedef'ed and only the typedef is referenced, never the tag name.

TYPEDEF_HIDES_STRUCT   = NO

#---------------------------------------------------------------------------
# Build related configuration options
#---------------------------------------------------------------------------

# If the EXTRACT_ALL tag is set to YES doxygen will assume all entities in
# documentation are documented, even if no documentation was available.
# Private class members and static file members will be hidden unless
# the EXTRACT_PRIVATE and EXTRACT_STATIC tags are set to YES

EXTRACT_ALL            = YES

# If the EXTRACT_PRIVATE tag is set to YES all private members of a class
# will be included in the documentation.

EXTRACT_PRIVATE        = NO

# If the EXTRACT_PACKAGE tag is set to YES all members with package or internal scope will be included in the documentation.

EXTRACT_PACKAGE        = NO

# If the EXTRACT_STATIC tag is set to YES all static members of a file
# will be included in the documentation.

EXTRACT_STATIC         = NO

# If the EXTRACT_LOCAL_CLASSES tag is set to YES classes (and structs)
# defined locally in source files will be included in the documentation.
# If set to NO only classes defined in header files are included.

EXTRACT_LOCAL_CLASSES  = YES

# This flag is only useful for Objective-C code. When set to YES local
# methods, which are defined in the implementation section but not in
# the interface are included in the documentation.
# If set to NO (the default) only methods in the interface are included.

EXTRACT_LOCAL_METHODS  = NO

# If this flag is set to YES, the members of anonymous namespaces will be
# extracted and appear in the documentation as a namespace called
# 'anonymous_namespace{file}', where file will be replaced with the base
# name of the file that contains the anonymous namespace. By default
# anonymous namespaces are hidden.

EXTRACT_ANON_NSPACES   = NO

# If the HIDE_UNDOC_MEMBERS tag is set to YES, Doxygen will hide all
# undocumented members of documented classes, files or namespaces.
# If set to NO (the default) these members will be included in the
# various overviews, but no documentation section is generated.
# This option has no effect if EXTRACT_ALL is enabled.

HIDE_UNDOC_MEMBERS     = NO

# If the HIDE_UNDOC_CLASSES tag is set to YES, Doxygen will hide all
# undocumented classes that are normally visible in the class hierarchy.
# If set to NO (the default) these classes will be included in the various
# overviews. This option has no effect if EXTRACT_ALL is enabled.

HIDE_UNDOC_CLASSES     = NO

# If the HIDE_FRIEND_COMPOUNDS tag is set to YES, Doxygen will hide all
# friend (class|struct|union) declarations.
# If set to NO (the default) these declarations will be included in the
# documentation.

HIDE_FRIEND_COMPOUNDS  = NO

# If the HIDE_IN_BODY_DOCS tag is set to YES, Doxygen will hide any
# documentation blocks found inside the body of a function.
# If set to NO (the default) these blocks will be appended to the
# function's detailed documentation block.

HIDE_IN_BODY_DOCS      = NO

# The INTERNAL_DOCS tag determines if documentation
# that is typed after a \internal command is included. If the tag is set
# to NO (the default) then the documentation will be excluded.
# Set it to YES to include the internal documentation.

INTERNAL_DOCS          = NO

# If the CASE_SENSE_NAMES tag is set to NO then Doxygen will only generate
# file names in lower-case letters. If set to YES upper-case letters are also
# allowed. This is useful if you have classes or files whose names only differ
# in case and if your file system supports case sensitive file names. Windows
# and Mac users are advised to set this option to NO.

CASE_SENSE_NAMES       = YES

# If the HIDE_SCOPE_NAMES tag is set to NO (the default) then Doxygen
# will show members with their full class and namespace scopes in the
# documentation. If set to YES the scope will be hidden.

HIDE_SCOPE_NAMES       = NO

# If the SHOW_INCLUDE_FILES tag is set to YES (the default) then Doxygen
# will put a list of the files that are included by a file in the documentation
# of that file.

SHOW_INCLUDE_FILES     = YES

# If the FORCE_LOCAL_INCLUDES tag is set to YES then Doxygen
# will list include files with double quotes in the documentation
# rather than with sharp brackets.

FORCE_LOCAL_INCLUDES   = YES

# If the INLINE_INFO tag is set to YES (the default) then a tag [inline]
# is inserted in the documentation for inline members.

INLINE_INFO            = YES

# If the SORT_MEMBER_DOCS tag is set to YES (the default) then doxygen
# will sort the (detailed) documentation of file and class members
# alphabetically by member name. If set to NO the members will appear in
# declaration order.

SORT_MEMBER_DOCS       = NO

# If the SORT_BRIEF_DOCS tag is set to YES then doxygen will sort the
# brief documentation of file, namespace and class members alphabetically
# by member name. If set to NO (the default) the members will appear in
# declaration order.

SORT_BRIEF_DOCS        = NO

# If the SORT_MEMBERS_CTORS_1ST tag is set to YES then doxygen
# will sort the (brief and detailed) documentation of class members so that
# constructors and destructors are listed first. If set to NO (the default)
# the constructors will appear in the respective orders defined by
# SORT_MEMBER_DOCS and SORT_BRIEF_DOCS.
# This tag will be ignored for brief docs if SORT_BRIEF_DOCS is set to NO
# and ignored for detailed docs if SORT_MEMBER_DOCS is set to NO.

SORT_MEMBERS_CTORS_1ST = NO

# If the SORT_GROUP_NAMES tag is set to YES then doxygen will sort the
# hierarchy of group names into alphabetical order. If set to NO (the default)
# the group names will appear in their defined order.

SORT_GROUP_NAMES       = NO

# If the SORT_BY_SCOPE_NAME tag is set to YES, the class list will be
# sorted by fully-qualified names, including namespaces. If set to
# NO (the default), the class list will be sorted only by class name,
# not including the namespace part.
# Note: This option is not very useful if HIDE_SCOPE_NAMES is set to YES.
# Note: This option applies only to the class list, not to the
# alphabetical list.

SORT_BY_SCOPE_NAME     = NO

# If the STRICT_PROTO_MATCHING option is enabled and doxygen fails to
# do proper type resolution of all parameters of a function it will reject a
# match between the prototype and the implementation of a member function even
# if there is only one candidate or it is obvious which candidate to choose
# by doing a simple string match. By disabling STRICT_PROTO_MATCHING doxygen
# will still accept a match between prototype and implementation in such cases.

STRICT_PROTO_MATCHING  = NO

# The GENERATE_TODOLIST tag can be used to enable (YES) or
# disable (NO) the todo list. This list is created by putting \todo
# commands in the documentation.

GENERATE_TODOLIST      = YES

# The GENERATE_TESTLIST tag can be used to enable (YES) or
# disable (NO) the test list. This list is created by putting \test
# commands in the documentation.

GENERATE_TESTLIST      = YES

# The GENERATE_BUGLIST tag can be used to enable (YES) or
# disable (NO) the bug list. This list is created by putting \bug
# commands in the documentation.

GENERATE_BUGLIST       = YES

# The GENERATE_DEPRECATEDLIST tag can be used to enable (YES) or
# disable (NO) the deprecated list. This list is created by putting
# \deprecated commands in the documentation.

GENERATE_DEPRECATEDLIST= YES

# The ENABLED_SECTIONS tag can be used to enable conditional
# documentation sections, marked by \if sectionname ... \endif.

ENABLED_SECTIONS       =

# The MAX_INITIALIZER_LINES tag determines the maximum number of lines
# the initial value of a variable or macro consists of for it to appear in
# the documentation. If the initializer consists of more lines than specified
# here it will be hidden. Use a value of 0 to hide initializers completely.
# The appearance of the initializer of individual variables and macros in the
# documentation can be controlled using \showinitializer or \hideinitializer
# command in the documentation regardless of this setting.

MAX_INITIALIZER_LINES  = 30

# Set the SHOW_USED_FILES tag to NO to disable the list of files generated
# at the bottom of the documentation of classes and structs. If set to YES the
# list will mention the files that were used to generate the documentation.

SHOW_USED_FILES        = YES

# Set the SHOW_FILES tag to NO to disable the generation of the Files page.
# This will remove the Files entry from the Quick Index and from the
# Folder Tree View (if specified). The default is YES.

SHOW_FILES             = YES

# Set the SHOW_NAMESPACES tag to NO to disable the generation of the
# Namespaces page.
# This will remove the Namespaces entry from the Quick Index
# and from the Folder Tree View (if specified). The default is YES.

SHOW_NAMESPACES        = YES

# The FILE_VERSION_FILTER tag can be used to specify a program or script that
# doxygen should invoke to get the current version for each file (typically from
# the version control system). Doxygen will invoke the program by executing (via
# popen()) the command <command> <input-file>, where <command> is the value of
# the FILE_VERSION_FILTER tag, and <input-file> is the name of an input file
# provided by doxygen. Whatever the program writes to standard output
# is used as the file version. See the manual for examples.

FILE_VERSION_FILTER    =

# The LAYOUT_FILE tag can be used to specify a layout file which will be parsed
# by doxygen. The layout file controls the global structure of the generated
# output files in an output format independent way. The create the layout file
# that represents doxygen's defaults, run doxygen with the -l option.
# You can optionally specify a file name after the option, if omitted
# DoxygenLayout.xml will be used as the name of the layout file.

LAYOUT_FILE            =

# The CITE_BIB_FILES tag can be used to specify one or more bib files
# containing the references data. This must be a list of .bib files. The
# .bib extension is automatically appended if omitted. Using this command
# requires the bibtex tool to be installed. See also
# http://en.wikipedia.org/wiki/BibTeX for more info. For LaTeX the style
# of the bibliography can be controlled using LATEX_BIB_STYLE. To use this
# feature you need bibtex and perl available in the search path.

CITE_BIB_FILES         =

#---------------------------------------------------------------------------
# configuration options related to warning and progress messages
#---------------------------------------------------------------------------

# The QUIET tag can be used to turn on/off the messages that are generated
# by doxygen. Possible values are YES and NO. If left blank NO is used.

QUIET                  = YES

# The WARNINGS tag can be used to turn on/off the warning messages that are
# generated by doxygen. Possible values are YES and NO. If left blank
# NO is used.

WARNINGS               = YES

# If WARN_IF_UNDOCUMENTED is set to YES, then doxygen will generate warnings
# for undocumented members. If EXTRACT_ALL is set to YES then this flag will
# automatically be disabled.

WARN_IF_UNDOCUMENTED   = YES

# If WARN_IF_DOC_ERROR is set to YES, doxygen will generate warnings for
# potential errors in the documentation, such as not documenting some
# parameters in a documented function, or documenting parameters that
# don't exist or using markup commands wrongly.

WARN_IF_DOC_ERROR      = YES

# The WARN_NO_PARAMDOC option can be enabled to get warnings for
# functions that are documented, but have no documentation for their parameters
# or return value. If set to NO (the default) doxygen will only warn about
# wrong or incomplete parameter documentation, but not about the absence of
# documentation.

WARN_NO_PARAMDOC       = YES

# The WARN_FORMAT tag determines the format of the warning messages that
# doxygen can produce. The string should contain the $file, $line, and $text
# tags, which will be replaced by the file and line number from which the
# warning originated and the warning text. Optionally the format may contain
# $version, which will be replaced by the version of the file (if it could
# be obtained via FILE_VERSION_FILTER)

WARN_FORMAT            = "$file:$line: $text"

# The WARN_LOGFILE tag can be used to specify a file to which warning
# and error messages should be written. If left blank the output is written
# to stderr.

WARN_LOGFILE           =

#---------------------------------------------------------------------------
# configuration options related to the input files
#---------------------------------------------------------------------------

# The INPUT tag can be used to specify the files and/or directories that contain
# documented source files. You may enter file names like "myfile.cpp" or
# directories like "/usr/src/myproject". Separate the files or directories
# with spaces.

INPUT                  = src

# This tag can be used to specify the character encoding of the source files
# that doxygen parses. Internally doxygen uses the UTF-8 encoding, which is
# also the default input encoding. Doxygen uses libiconv (or the iconv built
# into libc) for the transcoding. See http://www.gnu.org/software/libiconv for
# the list of possible encodings.

INPUT_ENCODING         = UTF-8

# If the value of the INPUT tag contains directories, you can use the
# FILE_PATTERNS tag to specify one or more wildcard pattern (like *.cpp
# and *.h) to filter out the source-files in the directories. If left
# blank the following patterns are tested:
# *.c *.cc *.cxx *.cpp *.c++ *.d *.java *.ii *.ixx *.ipp *.i++ *.inl *.h *.hh
# *.hxx *.hpp *.h++ *.idl *.odl *.cs *.php *.php3 *.inc *.m *.mm *.dox *.py
# *.f90 *.f *.for *.vhd *.vhdl

FILE_PATTERNS          = *.c \
                         *.cc \
                         *.cxx \
                         *.cpp \
                         *.c++ \
                         *.d \
                         *.java \
                         *.ii \
                         *.ixx \
                         *.ipp \
                         *.i++ \
                         *.inl \
                         *.h \
                         *.hh \
                         *.hxx \
                         *.hpp \
                         *.h++ \
                         *.idl \
                         *.odl \
                         *.cs \
                         *.php \
                         *.php3 \
                         *.inc \
                         *.m \
                         *.mm \
                         *.dox \
                         *.py \
                         *.f90 \
                         *.f \
                         *.vhd \
                         *.vhdl \
                         *.hpp.in \
                         *.cpp.in

# The RECURSIVE tag can be used to turn specify whether or not subdirectories
# should be searched for input files as well. Possible values are YES and NO.
# If left blank NO is used.

RECURSIVE              = YES

# The EXCLUDE tag can be used to specify files and/or directories that should be
# excluded from the INPUT source files. This way you can easily exclude a
# subdirectory from a directory tree whose root is specified with the INPUT tag.
# Note that relative paths are relative to the directory from which doxygen is
# run.

EXCLUDE                =

# The EXCLUDE_SYMLINKS tag can be used to select whether or not files or
# directories that are symbolic links (a Unix file system feature) are excluded
# from the input.

EXCLUDE_SYMLINKS       = NO

# If the value of the INPUT tag contains directories, you can use the
# EXCLUDE_PATTERNS tag to specify one or more wildcard patterns to exclude
# certain files from those directories. Note that the wildcards are matched
# against the file with absolute path, so to exclude all test directories
# for example use the pattern */test/*

EXCLUDE_PATTERNS       =

# The EXCLUDE_SYMBOLS tag can be used to specify one or more symbol names
# (namespaces, classes, functions, etc.) that should be excluded from the
# output. The symbol name can be a fully qualified name, a word, or if the
# wildcard * is used, a substring. Examples: ANamespace, AClass,
# AClass::ANamespace, ANamespace::*Test

EXCLUDE_SYMBOLS        = boost

# The EXAMPLE_PATH tag can be used to specify one or more files or
# directories that contain example code fragments that are included (see
# the \include command).

EXAMPLE_PATH           =

# If the value of the EXAMPLE_PATH tag contains directories, you can use the
# EXAMPLE_PATTERNS tag to specify one or more wildcard pattern (like *.cpp
# and *.h) to filter out the source-files in the directories. If left
# blank all files are included.

EXAMPLE_PATTERNS       = *

# If the EXAMPLE_RECURSIVE tag is set to YES then subdirectories will be
# searched for input files to be used with the \include or \dontinclude
# commands irrespective of the value of the RECURSIVE tag.
# Possible values are YES and NO. If left blank NO is used.

EXAMPLE_RECURSIVE      = NO

# The IMAGE_PATH tag can be used to specify one or more files or
# directories that contain image that are included in the documentation (see
# the \image command).

IMAGE_PATH             =

# The INPUT_FILTER tag can be used to specify a program that doxygen should
# invoke to filter for each input file. Doxygen will invoke the filter program
# by executing (via popen()) the command <filter> <input-file>, where <filter>
# is the value of the INPUT_FILTER tag, and <input-file> is the name of an
# input file. Doxygen will then use the output that the filter program writes
# to standard output.
# If FILTER_PATTERNS is specified, this tag will be
# ignored.

INPUT_FILTER           =

# The FILTER_PATTERNS tag can be used to specify filters on a per file pattern
# basis.
# Doxygen will compare the file name with each pattern and apply the
# filter if there is a match.
# The filters are a list of the form:
# pattern=filter (like *.cpp=my_cpp_filter). See INPUT_FILTER for further
# info on how filters are used. If FILTER_PATTERNS is empty or if
# non of the patterns match the file name, INPUT_FILTER is applied.

FILTER_PATTERNS        =

# If the FILTER_SOURCE_FILES tag is set to YES, the input filter (if set using
# INPUT_FILTER) will be used to filter the input files when producing source
# files to browse (i.e. when SOURCE_BROWSER is set to YES).

FILTER_SOURCE_FILES    = NO

# The FILTER_SOURCE_PATTERNS tag can be used to specify source filters per file
# pattern. A pattern will override the setting for FILTER_PATTERN (if any)
# and it is also possible to disable source filtering for a specific pattern
# using *.ext= (so without naming a filter). This option only has effect when
# FILTER_SOURCE_FILES is enabled.

FILTER_SOURCE_PATTERNS =

#---------------------------------------------------------------------------
# configuration options related to source browsing
#---------------------------------------------------------------------------

# If the SOURCE_BROWSER tag is set to YES then a list of source files will
# be generated. Documented entities will be cross-referenced with these sources.
# Note: To get rid of all source code in the generated output, make sure also
# VERBATIM_HEADERS is set to NO.

SOURCE_BROWSER         = YES

# Setting the INLINE_SOURCES tag to YES will include the body
# of functions and classes directly in the documentation.

INLINE_SOURCES         = NO

# Setting the STRIP_CODE_COMMENTS tag to YES (the default) will instruct
# doxygen to hide any special comment blocks from generated source code
# fragments. Normal C and C++ comments will always remain visible.

STRIP_CODE_COMMENTS    = YES

# If the REFERENCED_BY_RELATION tag is set to YES
# then for each documented function all documented
# functions referencing it will be listed.

REFERENCED_BY_RELATION = NO

# If the REFERENCES_RELATION tag is set to YES
# then for each documented function all documented entities
# called/used by that function will be listed.

REFERENCES_RELATION    = NO

# If the REFERENCES_LINK_SOURCE tag is set to YES (the default)
# and SOURCE_BROWSER tag is set to YES, then the hyperlinks from
# functions in REFERENCES_RELATION and REFERENCED_BY_RELATION lists will
# link to the source code.
# Otherwise they will link to the documentation.

REFERENCES_LINK_SOURCE = YES

# If the USE_HTAGS tag is set to YES then the references to source code
# will point to the HTML generated by the htags(1) tool instead of doxygen
# built-in source browser. The htags tool is part of GNU's global source
# tagging system (see http://www.gnu.org/software/global/global.html). You
# will need version 4.8.6 or higher.

USE_HTAGS              = NO

# If the VERBATIM_HEADERS tag is set to YES (the default) then Doxygen
# will generate a verbatim copy of the header file for each class for
# which an include is specified. Set to NO to disable this.

VERBATIM_HEADERS       = YES

#---------------------------------------------------------------------------
# configuration options related to the alphabetical class index
#---------------------------------------------------------------------------

# If the ALPHABETICAL_INDEX tag is set to YES, an alphabetical index
# of all compounds will be generated. Enable this if the project
# contains a lot of classes, structs, unions or interfaces.

ALPHABETICAL_INDEX     = YES

# In case all classes in a project start with a common prefix, all
# classes will be put under the same header in the alphabetical index.
# The IGNORE_PREFIX tag can be used to specify one or more prefixes that
# should be ignored while generating the index headers.

IGNORE_PREFIX          =

#---------------------------------------------------------------------------
# configuration options related to the HTML output
#---------------------------------------------------------------------------

# If the GENERATE_HTML tag is set to YES (the default) Doxygen will
# generate HTML output.

GENERATE_HTML          = YES

# The HTML_OUTPUT tag is used to specify where the HTML docs will be put.
# If a relative path is entered the value of OUTPUT_DIRECTORY will be
# put in front of it. If left blank `html' will be used as the default path.

HTML_OUTPUT            = html

# The HTML_FILE_EXTENSION tag can be used to specify the file extension for
# each generated HTML page (for example: .htm,.php,.asp). If it is left blank
# doxygen will generate files with .html extension.

HTML_FILE_EXTENSION    = .html

# The HTML_HEADER tag can be used to specify a personal HTML header for
# each generated HTML page. If it is left blank doxygen will generate a
# standard header. Note that when using a custom header you are responsible
#  for the proper inclusion of any scripts and style sheets that doxygen
# needs, which is dependent on the configuration options used.
# It is advised to generate a default header using "doxygen -w html
# header.html footer.html stylesheet.css YourConfigFile" and then modify
# that header. Note that the header is subject to change so you typically
# have to redo this when upgrading to a newer version of doxygen or when
# changing the value of configuration settings such as GENERATE_TREEVIEW!

HTML_HEADER            =

# The HTML_FOOTER tag can be used to specify a personal HTML footer for
# each generated HTML page. If it is left blank doxygen will generate a
# standard footer.

HTML_FOOTER            =

# The HTML_STYLESHEET tag can be used to specify a user-defined cascading
# style sheet that is used by each HTML page. It can be used to
# fine-tune the look of the HTML output. If the tag is left blank doxygen
# will generate a default style sheet. Note that doxygen will try to copy
# the style sheet file to the HTML output directory, so don't put your own
# style sheet in the HTML output directory as well, or it will be erased!

HTML_STYLESHEET        =

# The HTML_EXTRA_FILES tag can be used to specify one or more extra images or
# other source files which should be copied to the HTML output directory. Note
# that these files will be copied to the base HTML output directory. Use the
# $relpath$ marker in the HTML_HEADER and/or HTML_FOOTER files to load these
# files. In the HTML_STYLESHEET file, use the file name only. Also note that
# the files will be copied as-is; there are no commands or markers available.

HTML_EXTRA_FILES       =

# The HTML_COLORSTYLE_HUE tag controls the color of the HTML output.
# Doxygen will adjust the colors in the style sheet and background images
# according to this color. Hue is specified as an angle on a colorwheel,
# see http://en.wikipedia.org/wiki/Hue for more information.
# For instance the value 0 represents red, 60 is yellow, 120 is green,
# 180 is cyan, 240 is blue, 300 purple, and 360 is red again.
# The allowed range is 0 to 359.

HTML_COLORSTYLE_HUE    = 220

# The HTML_COLORSTYLE_SAT tag controls the purity (or saturation) of
# the colors in the HTML output. For a value of 0 the output will use
# grayscales only. A value of 255 will produce the most vivid colors.

HTML_COLORSTYLE_SAT    = 100

# The HTML_COLORSTYLE_GAMMA tag controls the gamma correction applied to
# the luminance component of the colors in the HTML output. Values below
# 100 gradually make the output lighter, whereas values above 100 make
# the output darker. The value divided by 100 is the actual gamma applied,
# so 80 represents a gamma of 0.8, The value 220 represents a gamma of 2.2,
# and 100 does not change the gamma.

HTML_COLORSTYLE_GAMMA  = 80

# If the HTML_DYNAMIC_SECTIONS tag is set to YES then the generated HTML
# documentation will contain sections that can be hidden and shown after the
# page has loaded.

HTML_DYNAMIC_SECTIONS  = NO

# With HTML_INDEX_NUM_ENTRIES one can control the preferred number of
# entries shown in the various tree structured indices initially; the user
# can expand and collapse entries dynamically later on. Doxygen will expand
# the tree to such a level that at most the specified number of entries are
# visible (unless a fully collapsed tree already exceeds this amount).
# So setting the number of entries 1 will produce a full collapsed tree by
# default. 0 is a special value representing an infinite number of entries
# and will result in a full expanded tree by default.

HTML_INDEX_NUM_ENTRIES = 100

# If the GENERATE_DOCSET tag is set to YES, additional index files
# will be generated that can be used as input for Apple's Xcode 3
# integrated development environment, introduced with OSX 10.5 (Leopard).
# To create a documentation set, doxygen will generate a Makefile in the
# HTML output directory. Running make will produce the docset in that
# directory and running "make install" will install the docset in
# ~/Library/Developer/Shared/Documentation/DocSets so that Xcode will find
# it at startup.
# See http://developer.apple.com/tools/creatingdocsetswithdoxygen.html
# for more information.

GENERATE_DOCSET        = NO

# When GENERATE_DOCSET tag is set to YES, this tag determines the name of the
# feed. A documentation feed provides an umbrella under which multiple
# documentation sets from a single provider (such as a company or product suite)
# can be grouped.

DOCSET_FEEDNAME        = "Doxygen generated docs"

# When GENERATE_DOCSET tag is set to YES, this tag specifies a string that
# should uniquely identify the documentation set bundle. This should be a
# reverse domain-name style string, e.g. com.mycompany.MyDocSet. Doxygen
# will append .docset to the name.

DOCSET_BUNDLE_ID       = org.doxygen.Project

# When GENERATE_PUBLISHER_ID tag specifies a string that should uniquely identify
# the documentation publisher. This should be a reverse domain-name style
# string, e.g. com.mycompany.MyDocSet.documentation.

DOCSET_PUBLISHER_ID    = org.doxygen.Publisher

# The GENERATE_PUBLISHER_NAME tag identifies the documentation publisher.

DOCSET_PUBLISHER_NAME  = Publisher

# If the GENERATE_HTMLHELP tag is set to YES, additional index files
# will be generated that can be used as input for tools like the
# Microsoft HTML help workshop to generate a compiled HTML help file (.chm)
# of the generated HTML documentation.

GENERATE_HTMLHELP      = NO

# If the GENERATE_HTMLHELP tag is set to YES, the CHM_FILE tag can
# be used to specify the file name of the resulting .chm file. You
# can add a path in front of the file if the result should not be
# written to the html output directory.

CHM_FILE               =

# If the GENERATE_HTMLHELP tag is set to YES, the HHC_LOCATION tag can
# be used to specify the location (absolute path including file name) of
# the HTML help compiler (hhc.exe). If non-empty doxygen will try to run
# the HTML help compiler on the generated index.hhp.

HHC_LOCATION           =

# If the GENERATE_HTMLHELP tag is set to YES, the GENERATE_CHI flag
# controls if a separate .chi index file is generated (YES) or that
# it should be included in the master .chm file (NO).

GENERATE_CHI           = NO

# If the GENERATE_HTMLHELP tag is set to YES, the CHM_INDEX_ENCODING
# is used to encode HtmlHelp index (hhk), content (hhc) and project file
# content.

CHM_INDEX_ENCODING     =

# If the GENERATE_HTMLHELP tag is set to YES, the BINARY_TOC flag
# controls whether a binary table of contents is generated (YES) or a
# normal table of contents (NO) in the .chm file.

BINARY_TOC             = NO

# The TOC_EXPAND flag can be set to YES to add extra items for group members
# to the contents of the HTML help documentation and to the tree view.

TOC_EXPAND             = NO

# If the GENERATE_QHP tag is set to YES and both QHP_NAMESPACE and
# QHP_VIRTUAL_FOLDER are set, an additional index file will be generated
# that can be used as input for Qt's qhelpgenerator to generate a
# Qt Compressed Help (.qch) of the generated HTML documentation.

GENERATE_QHP           = NO

# If the QHG_LOCATION tag is specified, the QCH_FILE tag can
# be used to specify the file name of the resulting .qch file.
# The path specified is relative to the HTML output folder.

QCH_FILE               =

# The QHP_NAMESPACE tag specifies the namespace to use when generating
# Qt Help Project output. For more information please see
# http://doc.trolltech.com/qthelpproject.html#namespace

QHP_NAMESPACE          = org.doxygen.Project

# The QHP_VIRTUAL_FOLDER tag specifies the namespace to use when generating
# Qt Help Project output. For more information please see
# http://doc.trolltech.com/qthelpproject.html#virtual-folders

QHP_VIRTUAL_FOLDER     = doc

# If QHP_CUST_FILTER_NAME is set, it specifies the name of a custom filter to
# add. For more information please see
# http://doc.trolltech.com/qthelpproject.html#custom-filters

QHP_CUST_FILTER_NAME   =

# The QHP_CUST_FILT_ATTRS tag specifies the list of the attributes of the
# custom filter to add. For more information please see
# <a href="http://doc.trolltech.com/qthelpproject.html#custom-filters">
# Qt Help Project / Custom Filters</a>.

QHP_CUST_FILTER_ATTRS  =

# The QHP_SECT_FILTER_ATTRS tag specifies the list of the attributes this
# project's
# filter section matches.
# <a href="http://doc.trolltech.com/qthelpproject.html#filter-attributes">
# Qt Help Project / Filter Attributes</a>.

QHP_SECT_FILTER_ATTRS  =

# If the GENERATE_QHP tag is set to YES, the QHG_LOCATION tag can
# be used to specify the location of Qt's qhelpgenerator.
# If non-empty doxygen will try to run qhelpgenerator on the generated
# .qhp file.

QHG_LOCATION           =

# If the GENERATE_ECLIPSEHELP tag is set to YES, additional index files
#  will be generated, which together with the HTML files, form an Eclipse help
# plugin. To install this plugin and make it available under the help contents
# menu in Eclipse, the contents of the directory containing the HTML and XML
# files needs to be copied into the plugins directory of eclipse. The name of
# the directory within the plugins directory should be the same as
# the ECLIPSE_DOC_ID value. After copying Eclipse needs to be restarted before
# the help appears.

GENERATE_ECLIPSEHELP   = NO

# A unique identifier for the eclipse help plugin. When installing the plugin
# the directory name containing the HTML and XML files should also have
# this name.

ECLIPSE_DOC_ID         = org.doxygen.Project

# The DISABLE_INDEX tag can be used to turn on/off the condensed index (tabs)
# at top of each HTML page. The value NO (the default) enables the index and
# the value YES disables it. Since the tabs have the same information as the
# navigation tree you can set this option to NO if you already set
# GENERATE_TREEVIEW to YES.

DISABLE_INDEX          = NO

# The GENERATE_TREEVIEW tag is used to specify whether a tree-like index
# structure should be generated to display hierarchical information.
# If the tag value is set to YES, a side panel will be generated
# containing a tree-like index structure (just like the one that
# is generated for HTML Help). For this to work a browser that supports
# JavaScript, DHTML, CSS and frames is required (i.e. any modern browser).
# Windows users are probably better off using the HTML help feature.
# Since the tree basically has the same information as the tab index you
# could consider to set DISABLE_INDEX to NO when enabling this option.

GENERATE_TREEVIEW      = NO

# The ENUM_VALUES_PER_LINE tag can be used to set the number of enum values
# (range [0,1..20]) that doxygen will group on one line in the generated HTML
# documentation. Note that a value of 0 will completely suppress the enum
# values from appearing in the overview section.

ENUM_VALUES_PER_LINE   = 4

# If the treeview is enabled (see GENERATE_TREEVIEW) then this tag can be
# used to set the initial width (in pixels) of the frame in which the tree
# is shown.

TREEVIEW_WIDTH         = 250

# When the EXT_LINKS_IN_WINDOW option is set to YES doxygen will open
# links to external symbols imported via tag files in a separate window.

EXT_LINKS_IN_WINDOW    = NO

# Use this tag to change the font size of Latex formulas included
# as images in the HTML documentation. The default is 10. Note that
# when you change the font size after a successful doxygen run you need
# to manually remove any form_*.png images from the HTML output directory
# to force them to be regenerated.

FORMULA_FONTSIZE       = 10

# Enable the USE_MATHJAX option to render LaTeX formulas using MathJax
# (see http://www.mathjax.org) which uses client side Javascript for the
# rendering instead of using prerendered bitmaps. Use this if you do not
# have LaTeX installed or if you want to formulas look prettier in the HTML
# output. When enabled you may also need to install MathJax separately and
# configure the path to it using the MATHJAX_RELPATH option.

USE_MATHJAX            = NO

# When MathJax is enabled you need to specify the location relative to the
# HTML output directory using the MATHJAX_RELPATH option. The destination
# directory should contain the MathJax.js script. For instance, if the mathjax
# directory is located at the same level as the HTML output directory, then
# MATHJAX_RELPATH should be ../mathjax. The default value points to
# the MathJax Content Delivery Network so you can quickly see the result without
# installing MathJax.
# However, it is strongly recommended to install a local
# copy of MathJax from http://www.mathjax.org before deployment.

MATHJAX_RELPATH        = http://www.mathjax.org/mathjax

# The MATHJAX_EXTENSIONS tag can be used to specify one or MathJax extension
# names that should be enabled during MathJax rendering.

MATHJAX_EXTENSIONS     =

# When the SEARCHENGINE tag is enabled doxygen will generate a search box
# for the HTML output. The underlying search engine uses javascript
# and DHTML and should work on any modern browser. Note that when using
# HTML help (GENERATE_HTMLHELP), Qt help (GENERATE_QHP), or docsets
# (GENERATE_DOCSET) there is already a search function so this one should
# typically be disabled. For large projects the javascript based search engine
# can be slow, then enabling SERVER_BASED_SEARCH may provide a better solution.

SEARCHENGINE           = YES

# When the SERVER_BASED_SEARCH tag is enabled the search engine will be
# implemented using a PHP enabled web server instead of at the web client
# using Javascript. Doxygen will generate the search PHP script and index
# file to put on the web server. The advantage of the server
# based approach is that it scales better to large projects and allows
# full text search. The disadvantages are that it is more difficult to setup
# and does not have live searching capabilities.

SERVER_BASED_SEARCH    = NO

#---------------------------------------------------------------------------
# configuration options related to the RTF output
#---------------------------------------------------------------------------

# If the GENERATE_RTF tag is set to YES Doxygen will generate RTF output
# The RTF output is optimized for Word 97 and may not look very pretty with
# other RTF readers or editors.

GENERATE_RTF           = NO

# The RTF_OUTPUT tag is used to specify where the RTF docs will be put.
# If a relative path is entered the value of OUTPUT_DIRECTORY will be
# put in front of it. If left blank `rtf' will be used as the default path.

RTF_OUTPUT             = rtf

# If the COMPACT_RTF tag is set to YES Doxygen generates more compact
# RTF documents. This may be useful for small projects and may help to
# save some trees in general.

COMPACT_RTF            = NO

# If the RTF_HYPERLINKS tag is set to YES, the RTF that is generated
# will contain hyperlink fields. The RTF file will
# contain links (just like the HTML output) instead of page references.
# This makes the output suitable for online browsing using WORD or other
# programs which support those fields.
# Note: wordpad (write) and others do not support links.

RTF_HYPERLINKS         = NO

# Load style sheet definitions from file. Syntax is similar to doxygen's
# config file, i.e. a series of assignments. You only have to provide
# replacements, missing definitions are set to their default value.

RTF_STYLESHEET_FILE    =

# Set optional variables used in the generation of an rtf document.
# Syntax is similar to doxygen's config file.

RTF_EXTENSIONS_FILE    =

#---------------------------------------------------------------------------
# configuration options related to the man page output
#---------------------------------------------------------------------------

# If the GENERATE_MAN tag is set to YES (the default) Doxygen will
# generate man pages

GENERATE_MAN           = NO

# The MAN_OUTPUT tag is used to specify where the man pages will be put.
# If a relative path is entered the value of OUTPUT_DIRECTORY will be
# put in front of it. If left blank `man' will be used as the default path.

MAN_OUTPUT             = man

# The MAN_EXTENSION tag determines the extension that is added to
# the generated man pages (default is the subroutine's section .3)

MAN_EXTENSION          = .3

# If the MAN_LINKS tag is set to YES and Doxygen generates man output,
# then it will generate one additional man file for each entity
# documented in the real man page(s). These additional files
# only source the real man page, but without them the man command
# would be unable to find the correct page. The default is NO.

MAN_LINKS              = NO

#---------------------------------------------------------------------------
# configuration options related to the XML output
#---------------------------------------------------------------------------

# If the GENERATE_XML tag is set to YES Doxygen will
# generate an XML file that captures the structure of
# the code including all documentation.

GENERATE_XML           = NO

# The XML_OUTPUT tag is used to specify where the XML pages will be put.
# If a relative path is entered the value of OUTPUT_DIRECTORY will be
# put in front of it. If left blank `xml' will be used as the default path.

XML_OUTPUT             = xml

# If the XML_PROGRAMLISTING tag is set to YES Doxygen will
# dump the program listings (including syntax highlighting
# and cross-referencing information) to the XML output. Note that
# enabling this will significantly increase the size of the XML output.

XML_PROGRAMLISTING     = YES

#---------------------------------------------------------------------------
# configuration options for the AutoGen Definitions output
#---------------------------------------------------------------------------

# If the GENERATE_AUTOGEN_DEF tag is set to YES Doxygen will
# generate an AutoGen Definitions (see autogen.sf.net) file
# that captures the structure of the code including all
# documentation. Note that this feature is still experimental
# and incomplete at the moment.

GENERATE_AUTOGEN_DEF   = NO

#---------------------------------------------------------------------------
# configuration options related to the Perl module output
#---------------------------------------------------------------------------

# If the GENERATE_PERLMOD tag is set to YES Doxygen will
# generate a Perl module file that captures the structure of
# the code including all documentation. Note that this
# feature is still experimental and incomplete at the
# moment.

GENERATE_PERLMOD       = NO

# If the PERLMOD_LATEX tag is set to YES Doxygen will generate
# the necessary Makefile rules, Perl scripts and LaTeX code to be able
# to generate PDF and DVI output from the Perl module output.

PERLMOD_LATEX          = NO

# If the PERLMOD_PRETTY tag is set to YES the Perl module output will be
# nicely formatted so it can be parsed by a human reader.
# This is useful
# if you want to understand what is going on.
# On the other hand, if this
# tag is set to NO the size of the Perl module output will be much smaller
# and Perl will parse it just the same.

PERLMOD_PRETTY         = YES

# The names of the make variables in the generated doxyrules.make file
# are prefixed with the string contained in PERLMOD_MAKEVAR_PREFIX.
# This is useful so different doxyrules.make files included by the same
# Makefile don't overwrite each other's variables.

PERLMOD_MAKEVAR_PREFIX =

#---------------------------------------------------------------------------
# Configuration options related to the preprocessor
#---------------------------------------------------------------------------

# If the ENABLE_PREPROCESSING tag is set to YES (the default) Doxygen will
# evaluate all C-preprocessor directives found in the sources and include
# files.

ENABLE_PREPROCESSING   = YES

# If the MACRO_EXPANSION tag is set to YES Doxygen will expand all macro
# names in the source code. If set to NO (the default) only conditional
# compilation will be performed. Macro expansion can be done in a controlled
# way by setting EXPAND_ONLY_PREDEF to YES.

MACRO_EXPANSION        = NO

# If the EXPAND_ONLY_PREDEF and MACRO_EXPANSION tags are both set to YES
# then the macro expansion is limited to the macros specified with the
# PREDEFINED and EXPAND_AS_DEFINED tags.

EXPAND_ONLY_PREDEF     = NO

# If the SEARCH_INCLUDES tag is set to YES (the default) the includes files
# pointed to by INCLUDE_PATH will be searched when a #include is found.

SEARCH_INCLUDES        = YES

# The INCLUDE_PATH tag can be used to specify one or more directories that
# contain include files that are not input files but should be processed by
# the preprocessor.

INCLUDE_PATH           = 

# You can use the INCLUDE_FILE_PATTERNS tag to specify one or more wildcard
# patterns (like *.h and *.hpp) to filter out the header-files in the
# directories. If left blank, the patterns specified with FILE_PATTERNS will
# be used.

INCLUDE_FILE_PATTERNS  =

# The PREDEFINED tag can be used to specify one or more macro names that
# are defined before the preprocessor is started (similar to the -D option of
# gcc). The argument of the tag is a list of macros of the form: name
# or name=definition (no spaces). If the definition and the = are
# omitted =1 is assumed. To prevent a macro definition from being
# undefined via #undef or recursively expanded use the := operator
# instead of the = operator.

PREDEFINED             = INNOEXTRACT_HAVE_DECRYPTION INNOEXTRACT_HAVE_LZMA INNOEXTRACT_BUILD_TESTS

# If the MACRO_EXPANSION and EXPAND_ONLY_PREDEF tags are set to YES then
# this tag can be used to specify a list of macro names that should be expanded.
# The macro definition that is found in the sources will be used.
# Use the PREDEFINED tag if you want to use a different macro definition that
# overrules the definition found in the source code.

EXPAND_AS_DEFINED      =

# If the SKIP_FUNCTION_MACROS tag is set to YES (the default) then
# doxygen's preprocessor will remove all references to function-like macros
# that are alone on a line, have an all uppercase name, and do not end with a
# semicolon, because these will confuse the parser if not removed.

SKIP_FUNCTION_MACROS   = YES

#---------------------------------------------------------------------------
# Configuration::additions related to external references
#---------------------------------------------------------------------------

# The TAGFILES option can be used to specify one or more tagfiles. For each
# tag file the location of the external documentation should be added. The
# format of a tag file without this location is as follows:
#
# TAGFILES = file1 file2 ...
# Adding location for the tag files is done as follows:
#
# TAGFILES = file1=loc1 "file2 = loc2" ...
# where "loc1" and "loc2" can be relative or absolute paths
# or URLs. Note that each tag file must have a unique name (where the name does
# NOT include the path). If a tag file is not located in the directory in which
# doxygen is run, you must also specify the path to the tagfile here.

TAGFILES               =

# When a file name is specified after GENERATE_TAGFILE, doxygen will create
# a tag file that is based on the input files it reads.

GENERATE_TAGFILE       =

# If the ALLEXTERNALS tag is set to YES all external classes will be listed
# in the class index. If set to NO only the inherited external classes
# will be listed.

ALLEXTERNALS           = NO

# If the EXTERNAL_GROUPS tag is set to YES all external groups will be listed
# in the modules index. If set to NO, only the current project's groups will
# be listed.

EXTERNAL_GROUPS        = YES

#---------------------------------------------------------------------------
# Configuration options related to the dot tool
#---------------------------------------------------------------------------

# If set to YES, the inheritance and collaboration graphs will hide
# inheritance and usage relations if the target is undocumented
# or is not a class.

HIDE_UNDOC_RELATIONS   = YES

# If you set the HAVE_DOT tag to YES then doxygen will assume the dot tool is
# available from the path. This tool is part of Graphviz, a graph visualization
# toolkit from AT&T and Lucent Bell Labs. The other options in this section
# have no effect if this option is set to NO (the default)

HAVE_DOT               = YES

# The DOT_NUM_THREADS specifies the number of dot invocations doxygen is
# allowed to run in parallel. When set to 0 (the default) doxygen will
# base this on the number of processors available in the system. You can set it
# explicitly to a value larger than 0 to get control over the balance
# between CPU load and processing speed.

DOT_NUM_THREADS        = 0

# If the CLASS_GRAPH and HAVE_DOT tags are set to YES then doxygen
# will generate a graph for each documented class showing the direct and
# indirect inheritance relations. Setting this tag to YES will force the
# CLASS_DIAGRAMS tag to NO.

CLASS_GRAPH            = YES

# If the COLLABORATION_GRAPH and HAVE_DOT tags are set to YES then doxygen
# will generate a graph for each documented class showing the direct and
# indirect implementation dependencies (inheritance, containment, and
# class references variables) of the class with other documented classes.

COLLABORATION_GRAPH    = YES

# If the GROUP_GRAPHS and HAVE_DOT tags are set to YES then doxygen
# will generate a graph for groups, showing the direct groups dependencies

GROUP_GRAPHS           = YES

# If the UML_LOOK tag is set to YES doxygen will generate inheritance and
# collaboration diagrams in a style similar to the OMG's Unified Modeling
# Language.

UML_LOOK               = NO

# If the UML_LOOK tag is enabled, the fields and methods are shown inside
# the class node. If there are many fields or methods and many nodes the
# graph may become too big to be useful. The UML_LIMIT_NUM_FIELDS
# threshold limits the number of items for each type to make the size more
# managable. Set this to 0 for no limit. Note that the threshold may be
# exceeded by 50% before the limit is enforced.

UML_LIMIT_NUM_FIELDS   = 10

# If set to YES, the inheritance and collaboration graphs will show the
# relations between templates and their instances.

TEMPLATE_RELATIONS     = NO

# If the ENABLE_PREPROCESSING, SEARCH_INCLUDES, INCLUDE_GRAPH, and HAVE_DOT
# tags are set to YES then doxygen will generate a graph for each documented
# file showing the direct and indirect include dependencies of the file with
# other documented files.

INCLUDE_GRAPH          = YES

# If the ENABLE_PREPROCESSING, SEARCH_INCLUDES, INCLUDED_BY_GRAPH, and
# HAVE_DOT tags are set to YES then doxygen will generate a graph for each
# documented header file showing the documented files that directly or
# indirectly include this file.

INCLUDED_BY_GRAPH      = YES

# If the CALL_GRAPH and HAVE_DOT options are set to YES then
# doxygen will generate a call dependency graph for every global function
# or class method. Note that enabling this option will significantly increase
# the time of a run. So in most cases it will be better to enable call graphs
# for selected functions only using the \callgraph command.

CALL_GRAPH             = YES

# If the CALLER_GRAPH and HAVE_DOT tags are set to YES then
# doxygen will generate a caller dependency graph for every global function
# or class method. Note that enabling this option will significantly increase
# the time of a run. So in most cases it will be better to enable caller
# graphs for selected functions only using the \callergraph command.

CALLER_GRAPH           = YES

# If the GRAPHICAL_HIERARCHY and HAVE_DOT tags are set to YES then doxygen
# will generate a graphical hierarchy of all classes instead of a textual one.

GRAPHICAL_HIERARCHY    = YES

# If the DIRECTORY_GRAPH and HAVE_DOT tags are set to YES
# then doxygen will show the dependencies a directory has on other directories
# in a graphical way. The dependency relations are determined by the #include
# relations between the files in the directories.

DIRECTORY_GRAPH        = YES

# The DOT_IMAGE_FORMAT tag can be used to set the image format of the images
# generated by dot. Possible values are svg, png, jpg, or gif.
# If left blank png will be used. If you choose svg you need to set
# HTML_FILE_EXTENSION to xhtml in order to make the SVG files
# visible in IE 9+ (other browsers do not have this requirement).

DOT_IMAGE_FORMAT       = svg

# If DOT_IMAGE_FORMAT is set to svg, then this option can be set to YES to
# enable generation of interactive SVG images that allow zooming and panning.
# Note that this requires a modern browser other than Internet Explorer.
# Tested and working are Firefox, Chrome, Safari, and Opera. For IE 9+ you
# need to set HTML_FILE_EXTENSION to xhtml in order to make the SVG files
# visible. Older versions of IE do not have SVG support.

INTERACTIVE_SVG        = NO

# The tag DOT_PATH can be used to specify the path where the dot tool can be
# found. If left blank, it is assumed the dot tool can be found in the path.

DOT_PATH               =

# The DOTFILE_DIRS tag can be used to specify one or more directories that
# contain dot files that are included in the documentation (see the
# \dotfile command).

DOTFILE_DIRS           =

# The MSCFILE_DIRS tag can be used to specify one or more directories that
# contain msc files that are included in the documentation (see the
# \mscfile command).

MSCFILE_DIRS           =

# The DOT_GRAPH_MAX_NODES tag can be used to set the maximum number of
# nodes that will be shown in the graph. If the number of nodes in a graph
# becomes larger than this value, doxygen will truncate the graph, which is
# visualized by representing a node as a red box. Note that doxygen if the
# number of direct children of the root node in a graph is already larger than
# DOT_GRAPH_MAX_NODES then the graph will not be shown at all. Also note
# that the size of a graph can be further restricted by MAX_DOT_GRAPH_DEPTH.

DOT_GRAPH_MAX_NODES    = 50

# The MAX_DOT_GRAPH_DEPTH tag can be used to set the maximum depth of the
# graphs generated by dot. A depth value of 3 means that only nodes reachable
# from the root by following a path via at most 3 edges will be shown. Nodes
# that lay further from the root node will be omitted. Note that setting this
# option to 1 or 2 may greatly reduce the computation time needed for large
# code bases. Also note that the size of a graph can be further restricted by
# DOT_GRAPH_MAX_NODES. Using a depth of 0 means no depth restriction.

MAX_DOT_GRAPH_DEPTH    = 0

# Set the DOT_MULTI_TARGETS tag to YES allow dot to generate multiple output
# files in one run (i.e. multiple -o and -T options on the command line). This
# makes dot run faster, but since only newer versions of dot (>1.8.10)
# support this, this feature is disabled by default.

DOT_MULTI_TARGETS      = YES

# If the GENERATE_LEGEND tag is set to YES (the default) Doxygen will
# generate a legend page explaining the meaning of the various boxes and
# arrows in the dot generated graphs.

GENERATE_LEGEND        = YES

# If the DOT_CLEANUP tag is set to YES (the default) Doxygen will
# remove the intermediate dot files that are used to generate
# the various graphs.

DOT_CLEANUP            = YES
```

## File: `doc/innoextract.1.in`
```
.\" Manpage for innoextract.
.\" Contact daniel@constexpr.org to correct errors or typos.
.TH innoextract 1 "@CHANGELOG_0_STRING@" "@VERSION_0_STRING@@VERSION_SUFFIX@@GIT_SUFFIX_7@"
.SH NAME
innoextract - tool to extract installers created by Inno Setup
.SH SYNOPSIS
.B innoextract
.RB [ \-\-extract ]
.RB [ \-\-lowercase ]
[options] [\fB\-\-\fP] \fIinstallers\fP ...

\fBinnoextract \-\-list\fP [options] [\fB\-\-\fP] \fIinstallers\fP ...

\fBinnoextract \-\-test\fP [options] [\fB\-\-\fP] \fIinstallers\fP ...
.SH DESCRIPTION
\fBinnoextract\fP is a tool that can extract installer executables created by Inno Setup.
.PP
\fBinnoextract\fP will extract files from installers specified on the command line.
.PP
To extract a multi-part installer with external data files, only the executable (.exe) file needs to be given as an argument to \fBinnoextract\fP.
.SH OPTIONS SUMMARY
.PP
Here is a short summary of the options available in innoextract. Please refer to the detailed  documentation below for a complete description.
.TP
.B Generic options:
.nf
 \-h \-\-help               Show supported options
 \-v \-\-version            Print version information
    \-\-license            Show license information
.fi
.TP
.B Actions:
.nf
 \-t \-\-test               Only verify checksums, don't write anything
 \-e \-\-extract            Extract files (default action)
 \-l \-\-list               Only list files, don't write anything
    \-\-list\-sizes         List file sizes
    \-\-list\-checksums     List file checksums
 \-i \-\-info               Print information about the installer
    \-\-list\-languages     List languages supported by the installer
    \-\-gog\-game\-id        Determine the GOG.com game ID for this installer
    \-\-show\-password      Show password check information
    \-\-check\-password     Abort if the password is incorrect
 \-V \-\-data\-version       Only print the data version
.fi
.TP
.B Modifiers:
.nf
    \-\-codepage \fICODEPAGE\fP  Encoding for ANSI strings
    \-\-collisions \fIACTION\fP  How to handle duplicate files
    \-\-default\-language   Default language for renaming
    \-\-dump               Dump contents without converting filenames
 \-L \-\-lowercase          Convert extracted filenames to lower-case
 \-T \-\-timestamps \fITZ\fP      Timezone for file times or "local" or "none"
 \-d \-\-output\-dir \fIDIR\fP     Extract files into the given directory
 \-P \-\-password \fIPASSWORD\fP  Password for encrypted files
    \-\-password\-file \fIFILE\fP File to load password from
 \-g \-\-gog                Process additional archives from GOG.com installers
    \-\-no\-gog\-galaxy      Don't re-assemble GOG Galaxy file parts
 \-n \-\-no\-extract\-unknown Don't extract unknown Inno Setup versions
.fi
.TP
.B Filters:
.nf
 \-m \-\-exclude\-temp       Don't extract temporary files
    \-\-language \fILANG\fP      Extract only files for this language
    \-\-language\-only      Only extract language-specific files
 \-I \-\-include \fIEXPR\fP       Extract only files that match this path
.fi
.TP
.B Display options:
.nf
 \-q \-\-quiet              Output less information
 \-s \-\-silent             Output only error/warning information
    \-\-no\-warn\-unused     Don't warn on unused \fI.bin\fP files
 \-c \-\-color[=\fIENABLE\fP]     Enable/disable color output
 \-p \-\-progress[=\fIENABLE\fP]  Enable/disable the progress bar
.fi
.SH OPTIONS
.TP
\fB--\fP
Treat all arguments after this one as files, even if they begin with a dash.
.TP
\fB\-\-check\-password\fB
Abort processing if the password provided using the \fB\-\-password\fP or \fB\-\-password\-file\fP option does not match the checksum stored in the installer.

The password checksum used for this check can be retrieved using the \fB\-\-show\-password\fP option.
.TP
\fB\-\-codepage\fP \fICODEPAGE\fP
Non-Unicode versions of Inno Setup store strings in an unspecified encoding. By default, \fBinnoextract\fP will guess the encoding from the installer's language list, falling back to Windows-1252. This option can be used to override that guess by specifying a non-zero Windows codepage number to use.

On non-Windows platforms, \fBinnoextract\fP will ignore the system locale and always use UTF-8 as the filesystem and standard output encoding - the \fB\-\-codepage\fP option only changes the input encoding. However, using codepage number "\fB65001\fP" instructs \fBinnoextract\fP to assume all strings are already encoded as UTF-8 and to output them without conversion.

This option has no effect with Unicode-enabled installers, which always use UTF-16LE. Invalid UTF-16 data is represented using the WTF-8 encoding which is a straightforward extension of UTF-8 to represent unpaired UTF-16 surrogate code units.
.TP
\fB\-\-collisions\fP \fIACTION\fP
Inno Setup installers can contain duplicate files with the same name. This option tells innoextract what to do when such a collisions is encountered. Valid actions are:

.RS
.TP
"\fBoverwrite\fP"
Extract only one of the colliding files. The choice is done similar to how Inno Setup overwrites files during installation. This is the default.
.TP
"\fBrename\fP"
Rename files that would be overwritten using the "\fBoverwrite\fP" action by appending a suffix comprised of the file's language, its architecture, the component it belongs to and/or a number to make the filename unique. The language suffix (if applicable) is also appended to the \fIdefault\fP file that would have been extracted with the "\fBoverwrite\fP" action.
.TP
"\fBrename-all\fP"
Rename all colliding files by appending a suffix comprised of the file's language, its architecture, the component it belongs to and/or a number to make the filename unique. The complete suffix is appended to both files that would have been overwritten using the "\fBoverwrite\fP" action and to those that would have overwritten other files.
.TP
"\fBerror\fP"
Exit when a collision is detected.
.RE
.IP
.B Rename rules:

1. If the \fBcomponent\fP is not the same for all files in the collision set (all files with the same filename), "\fB#\fP" (without quotes) followed by the component id is appended to all files that are specific to a single component.

2. If the \fBlanguage\fP is not the same for all files in the collision set, "\fB@\fP" (without quotes) followed by the language id is appended to all files that are specific to a single language unless that language matches the default language specified by the \fB--default-language\fP. While the suffix is omitted for the default language, no numbered suffix is added in it's place unless needed to make the filename unique.

3. If the \fBarchitecture\fP is not the same for all files in the collision set, "\fB@32bit\fP" or "\fB@64bit\fP" (without quotes) is appended to all files that are specific to a single architecture.

4. If no suffix was added by the previous steps, or if the filename is not yet unique, "\fB$\fP" (without quotes) followed by the lowest integer (starting at 0) to make the filename unique is appended.

With the "\fBrename\fP" action, steps 1 and 3 are only applied to files that would have been overwritten by the "\fBoverwrite\fP" action while "\fBrename-all\fP" applies them to all files in the collision set.
.TP
\fB\-c\fP, \fB\-\-color\fP[=\fIENABLE\fP]
By default
.B innoextract
will try to detect if the terminal supports shell escape codes and enable or disable color output accordingly. Specifically, colors will be enabled if both \fBstdout\fP and \fBstderr\fP point to a TTY, the \fBTERM\fP environment variable is not set to "\fBdumb\fP" and the \fBNO_COLOR\fP environment variable is unset. Pass \fB1\fP or \fBtrue\fP to \fB\-\-color\fP to force color output. Pass \fB0\fP or \fBfalse\fP to never output color codes.
.TP
\fB\-V\FP, \fB\-\-data\-version\fP
Print the Inno Setup data version of the installer and exit immediately.

The version printed using this option is the one stored in the setup file and can differ from the version printed with other actions as the stored data version is not always correct.

This option can be used to determine if a file is an Inno Setup installer without loading any compressed headers.

This option cannot be combined with any other action.
.TP
\fB\-\-default\-language\fP \fILANG\fP
Set a language as the default.

With \fB\-\-collisions\=overwrite\fP (the default) this will change the choice of which file to keep to always prefer the given language. In effect, \fB\-\-default\-language\fP behaves almost like \fB\-\-language\fP, except that files are extracted for all languages if they have different names.

When using the \fB\-\-collisions\=rename\fP option, \fB\-\-default\-language\fP chooses a language for which the files should keep the original name if possible.
.TP
\fB\-\-dump\fP
Don't convert Windows paths to UNIX paths and don't substitute constants in paths.

When combining \fB\-\-dump\fP with \fB\-\-extract\fP innoextract will \fInot\fP ensure that the paths don't point outside the destination directory. Use this option with caution when handling untrusted files.
.TP
\fB\-m\fP, \fB\-\-exclude\-temp\fP
Don't extract files that would have been deleted at the end of the install process. Such files are marked with [temp] in the file listing.

This option takes precedence over \fB\-\-include\fP and \fB\-\-language\fP: temporary files are never extracted when using the \fB\-\-exclude\-temp\fP, even if they match the selected language or include expressions.
.TP
\fB\-e\fP, \fB\-\-extract\fP
Extract all files to the current directory. This action is enabled by default, unless one or more of the \fB\-\-list\fP, \fB\-\-list\-sizes\fP, \fB\-\-list\-checksums\fP, \fB\-\-test\fP, \fB\-\-list\-languages\fP, \fB\-\-gog\-game\-id\fP, \fB\-\-show\-password\fP or \fB\-\-check\-password\fP actions are specified.

By default innoextract will continue after encountering file checksum errors. The \fB\-\-extract\fP option can be combined with \fB\-\-test\fP to abort on checksum errors.
.TP
\fB\-n\fP, \fB\-\-no\-extract\-unknown\fP
By default innoextract will try to extract installers with an unknown Inno Setup data version by treating it as the closest known version. This option tells innoextract to abort instead.
.TP
\fB\-g\fP, \fB\-\-gog\fP
Try to process additional .bin files that have the same basename as the setup but are not actually part of the Inno Setup installer. This is the case for newer multi-part GOG.com installers where these .bin files are RAR archives, potential encrypted with the MD5 checksum of the game ID (see the \fB\-\-gog\-game\-id\fP option).

Extracting these RAR archives requires rar, unrar or lsar/unar command-line utilities to be in the PATH.

The \fB\-\-list\fP, \fB\-\-test\fP, \fB\-\-extract\fP and \fB\-\-output\-dir\fP options are passed along to unrar/unar, but other options may be ignored for the RAR files. For multi-part RAR archives, the \fB\-\-test\fP requires a writable output directory for temporary files which can be specified using the \fB\-\-output\-dir\fP option. If the output directory does not exist it will be created and then removed after testing is done. Parent directories are not created. Temporary files created inside the directory are always removed.

Note that is option is geared towards GOG.com installers. Other installers may come be bundled with different extraneous \fI.bin\fP which this option might not be able to handle.

This option also forces re-assembly of GOG Galaxy file parts. See the \fB\-\-no\-gog\-galaxy\fP option for details.
.TP
\fB\-\-no\-gog\-galaxy\fP
Some GOG.com installers contain files in GOG Galaxy format (split into multiple parts that are individually compressed) which are re-assembled using post-install scripts. By default \fBinnoextract\fP will try to re\-assemble such files if it detects a GOG.com installer. This option disables that.

GOG.com installers are detected using the publisher and URL fields in the setup headers. Use the \fB\-\-gog\fP option to force reassembly for all installers.
.TP
\fB\-\-gog\-game\-id\fP
Determine the ID used by GOG.com for the game contained in this installer. This will only work with Galaxy-ready GOG.com installers.

This option can be combined with \fB\-\-silent\fP to print only the game ID without additional syntax that would make consumption by other scripts harder.

The \fB\-\-gog\-game\-id\fP action can be combined with \fB\-\-list\fP, \fB\-\-test\fP, \fB\-\-extract\fP and/or \fB\-\-list\-languages\fP. If \fB\-\-silent\fP and \fB\-\-gog\-game\-id\fP are combined with \fB\-\-list\fP and/or \fB\-\-list\-languages\fP, the game ID (or an empty line) will be printed on it's own line before the file list but after the language list.

For newer multi-part GOG.com installers the \fI.bin\fP files are not part of the Inno Setup installer but instead are RAR archives. Some of these RAR files are encrypted, with the password being the MD5 checksum of the game ID:

  \fBinnoextract \-\-gog\-game\-id --silent\fP \fIsetup_....exe\fP | \fBmd5sum\fP | \fBcut \-d\fP ' ' \fB\-f\fP 1
.TP
\fB\-h\fP, \fB\-\-help\fP
Show a list of the supported options.
.TP
\fB\-I\fP, \fB\-\-include\fP \fIEXPR\fP
If this option is specified, innoextract will only process files whose path matches \fIEXPR\fP. The expression can be either a single path component (a file or directory name) or a series of successive path components joined by the OS path separator (\\ on Windows, / elsewhere).

The expression is always matched against one or more full path components. Filtering by parts of filenames is currently not supported. Matching is done case-insensitively.

\fIEXPR\fP may contain one leading path separator, in which case the rest of the expression is matched against the start of the path. Otherwise, the expression is matched against any part of the path.

The \fB\-\-include\fP option may be repeated in order allow files matching against one of multiple patterns. If \fB\-\-include\fP is not used, all files are processed.
.TP
\fB\-i\fP \fB\-\-info\fP
This is a convenience option to enable all actions that print information about the installer.

Scrips should not rely on the output format with this option and should instead enable the individual actions instead.

Currently this option enables \fB\-\-list\-languages\fP, \fB\-\-gog\-game\-id\fP and \fB\-\-show\-password\fP.
.TP
\fB\-\-language\fP \fILANG\fP
Extract only language-independent files and files for the given language. By default all files are extracted.

To also skip language-independent files, combine this option with \fB\-\-language\-only\fP.
.TP
\fB\-\-language\-only\fP
Only extract files that are language-specific.

This option can be combined with \fB\-\-language\fP to only extract the files of a specific language.
.TP
\fB\-\-license\fP
Show license information.
.TP
\fB\-l\fP, \fB\-\-list\fP
List files contained in the installer but don't extract anything.

This action also enables the \fB\-\-list\-sizes\fP action unless either \fB\-\-quiet\fP or \fB\-\-silent\fP is specified.

This option can be combined with \fB\-\-silent\fP to print only the names of the contained files (one per line) without additional syntax that would make consumption by other scripts harder.

The \fB\-\-list\fP action can be combined with \fB\-\-test\fP, \fB\-\-extract\fP, \fB\-\-list\-languages\fP and/or \fB\-\-gog\-game\-id\fP to display the names of the files as they are extracted even with \fB\-\-silent\fP.
.TP
\fB\-\-list\-checksums\fP
List checksums for files contained in the installer.

This option implies the \fB\-\-list\fP action and can be combined with the \fB\-\-list\-sizes\fP option to print both the size and checksum for each file.

With \fB\-\-silent\fP the file checksum will be printed at the start of the line (but after the file size if enabled with the \fB\-\-list\-sizes\fP option) followed by a space. Otherwise the checksum is printed after the file name.

The checksum type can be one of \fBAdler32\fP, \fBCRC32\fP, \fBMD5\fP or \fBSHA-1\fP and is printed in fron of the checksum hash followed by a space. \fBAdler32\fP and \fBCRC32\fP checksums are printed as "\fB0x\fP" followed by the 32-bit hexadecimal value.

Different files in the same installer can have different checksum types if GOG Galaxy file part reassembly is not disabled using the \fB\-\-no\-gog\-galaxy\fP option.
.TP
\fB\-\-list\-languages\fP
List languages supported by the installer.

This option can be combined with \fB\-\-silent\fP to print only the identifiers of the languages (one per line) followed by a space and then the language name, without additional syntax that would make consumption by other scripts harder.

The \fB\-\-list\-languages\fP action can be combined with \fB\-\-list\fP, \fB\-\-test\fP, \fB\-\-extract\fP and/or \fB\-\-gog\-game\-id\fP to display the available languages before doing anything else. If \fB\-\-silent\fP and \fB\-\-list\-languages\fP are combined with \fB\-\-list\fP and/or \fB\-\-gog\-game\-id\fP, the languages list will be terminated with an empty line and will precede both the game ID and files list.
.TP
\fB\-\-list\-sizes\fP
List uncompressed sizes for files contained in the installer.

This option implies the \fB\-\-list\fP action and can be combined with the \fB\-\-list\-checksums\fP option to print both the size and checksum for each file.

With \fB\-\-silent\fP the file size in bytes will be printed at the start of the line followed by a space. Otherwise the size is printed after the file name in a human-friendly format.
.TP
\fB\-L\fP, \fB\-\-lowercase\fP
Convert filenames stored in the installer to lower-case before extracting.
.TP
\fB\-d\fP, \fB\-\-output\-dir\fP \fIDIR\fP
Extract all files into the given directory. By default, \fBinnoextract\fP will extract all files to the current directory.

If the specified directory does not exist, it will be created. However, the parent directory must exist or extracting will fail.
.TP
\fB\-P\fP, \fB\-\-password \fIPASSWORD\fP
Specifies the password to decrypt encrypted files. The password is assumed to be encoded as UTF-8 and converted the internal encoding according used in the installer as needed.

Use the \fB\-\-password-file\fP option to load the password from a file or standard input instead. This option cannot be combined with \fB\-\-password-file\fP.

If this password does not match the checksum stored in the installer, encrypted files will be skipped but unencrypted files will still be extracted. Use the \fB\-\-check\-password\fP option to abort processing entirely if the password is incorrect.
.TP
\fB\-\-password-file\fP \fIFILE\fP
Load a password form the specified file. Only the first line excluding the terminating carriage return and/or line break is used as the password. The password is assumed to be encoded as UTF-8 and converted the internal encoding according used in the installer as needed.

If the special file name "\fB-\fP" is used, the password will be read from standard input.

Use the \fB\-\-password\fP option to specify the password on the command\-line instead. This option cannot be combined with \fB\-\-password\fP.

If this password does not match the checksum stored in the installer, encrypted files will be skipped but unencrypted files will still be extracted. Use the \fB\-\-check\-password\fP option to abort processing entirely if the password is incorrect.
.TP
\fB\-p\fP, \fB\-\-progress\fP[=\fIENABLE\fP]
By default \fBinnoextract\fP will try to detect if the terminal supports shell escape codes and enable or disable progress bar output accordingly. Pass \fB1\fP or \fBtrue\fP to \fB\-\-progress\fP to force progress bar output. Pass \fB0\fP or \fBfalse\fP to never show a progress bar.
.TP
\fB\-q\fP, \fB\-\-quiet\fP
Less verbose output.
.TP
\fB\-\-show\-password\fP
Show checksum \fB$c\fP and salt \fB$s\fP used for the password \fB$p\fP check as well as encoding of the password. The checksum is calculated from the salt concatenated with the password:

 \fB$c = hash($s . $p)\fP

With the \fB\-\-silent\fP option, the checksum name and hash is printed on one line separated by a space followed by the salt encoded as hex bytes and password encoding on separate lines.

Checksum types can be \fBCRC32\fP, \fBMD5\fP or \fBSHA-1\fP although \fBCRC32\fP is not used in installers with encryption.

Use the \fB\-\-password\fP or \fB\-\-password\-file\fP option together with \fB\-\-check\-password\fP to check if a password matches this checksum.
.TP
\fB\-s\fP, \fB\-\-silent\fP
Don't output anything except errors and warnings unless explicitly requested and use a machine-readable output format.

This option can be combined with \fB\-\-list\fP to print only the names of the contained files (one per line) without additional syntax that would make consumption by other scripts harder.
.TP
\fB\-t\fP, \fB\-\-test\fP
Test archive integrity but don't write any output files.

This option can be combined with \fB\-\-extract\fP to abort on file checksum errors.
.TP
\fB\-T\fP, \fB\-\-timestamps\fP \fITZ\fP
Inno Setup installers can contain timestamps in both UTC and 'local' timezones.

The \fB\-\-timestamps\fP option specifies what timezone should be used to adjust these 'local' file times.

Valid values are those accepted by \fBtzset\fP in the \fBTZ\fP environment variable, except with the direction of the time offset reversed: both \fB\-T CET\fP and \fB\-T GMT+1\fP will (when DST is in effect) give the same result.

Besides timezones, two special values are accepted:

.RS
.HP
"\fBnone\fP"
Don't preserve file times for extracted files, both for UTC and 'local' timestamps. The file times will be left the way the OS set them when creating the output files.
.HP
"\fBlocal\fP"
Use the system timezone for 'local' timestamps. This is the normal Inno Setup behavior, and can be used together with the \fBTZ\fP environment variable.
.RE
.IP

The default value for this option is \fBUTC\fP, causing innoextract to not adjust 'local' file times. File times marked as UTC in the Inno Setup file will never be adjusted no matter what \fB\-\-timestamps\fP is set to.
.TP
\fB\-v\fP, \fB\-\-version\fP
Print the \fBinnoextract\fP version number and supported Inno Setup versions.

If combined with the \fB\-\-silent\fP option, only the version \fInumber\fP is printed. Otherwise, the output will contain the name (innoextract) followed by the version number on the first line, and, unless the \fB\-\-quiet\fP options is specified, the range of supported Inno Setup installer versions on the second line.
.TP
\fB\-\-no\-warn\-unused\fP
By default, innoextract will print a warning if it encounters \fI.bin\fP files that look like they could be part of the setup but are not used. This option disables that warning.
.SH PATH CONSTANTS
Paths in Inno Setup installers can contain constants (variable or code references) that are expanded at install time. innoextract expands all such constants to their name  and replaces unsafe characters with \fB$\fP. For example \fB{app}\fP is expanded to \fBapp\fP while \fB{code:Example}\fP is expanded to \fBcode$Example\fP.

There is currently no way to configure this expansion except for disabling it with the \fB\-\-dump\fP option.
.SH EXIT VALUES
.PP
.IP \fB0\fP
Success
.IP \fB1\fP
Syntax or usage error
.IP \fB2+\fP
Broken or unsupported setup file, or input/output error
.SH LIMITATIONS
There is no support for extracting individual components and limited support for filtering by name.

Included scripts and checks are not executed.

The mapping from Inno Setup constants like the application directory to subdirectories is hard-coded.

Names for data slice/disk files in multi-file installers must follow the standard naming scheme.
.SH SEE ALSO
\fBcabextract\fP(1), \fBunar\fP(1), \fBunrar\fP(1), \fBunshield\fP(1), \fBtzset\fP(3)
.SH BUGS
.PP
Please report bugs to https://innoextract.constexpr.org/issues.
.SH CREDITS
.PP
\fBinnoextract\fP is distributed under the zlib/libpng license.  See the LICENSE file for details.
.PP
A website is available at https://constexpr.org/innoextract/.
.PP
This program uses the excellent lzma/xz decompression library written by Lasse Collin.
.SH AUTHOR
Daniel Scharrer (daniel@constexpr.org)
```

## File: `doc/update-copyright-years`
```
#!/bin/sh

copyright='Daniel Scharrer'

die() {
	printf '%s\n' "$1"
	exit 1
}

if [ -z "$1" ] || [ ! -d "$1" ]
	then repo="$(git rev-parse --show-toplevel)"
	else repo="$1" ; shift
fi
[ -d "$repo/.git" ] || die "$1 is not a git repository"

if [ -z "$1" ]
	then last_tag="$(git --git-dir="$repo/.git" rev-list --tags --max-count=1)"
	else last_tag="$1"
fi
[ -z "$last_tag" ] && die "Could not determine last tag"
last_tag_name="$(git --git-dir="$repo/.git" describe --tags "$last_tag")"
printf 'Updating files modified since %s\n' "$last_tag_name"

files="$(git --git-dir="$repo/.git" diff --name-only "$last_tag" HEAD | tr '\n' ' ')"
eval "set -- LICENSE COPYING $files"

for file ; do
	path="$repo/$file"
	[ -f "$path" ] || continue # File was deleted
	
	case "$file" in
		*.yml|.*)
			# Never try to update the copyright year for these files
			continue ;;
	esac
	
	c="$(grep -P "(^|[^a-zA-Z0-9_])Copyright( \\([cC]\\))? (\\d{4}\\-)?\\d{4} $copyright" "$path")"
	
	if [ -z "$c" ] ; then
		case "$file" in
			cmake/*.cpp|*CMakeLists.txt|*.md|*.1|*.in|LICENSE.*)
				# These files don't have to contain copyright information
				;;
			*.*|scripts/*)
				c="$(grep -P "(^|[^a-zA-Z0-9_])Copyright( \([cC]\))?[ \:].*public domain" "$path")"
				[ -z "$c" ] && printf 'No copyright info found in %s, skipping\n' "$file" ;;
		esac
		continue
	fi
	
	if [ "$(printf '%s\n' "$c" | wc -l)" -gt 1 ] ; then
		printf 'Multiple copyright lines found in %s, skipping\n' "$file"
		continue
	fi
	
	s='\(^.*Copyright\( ([cC])\)\? \([0-9]\{4\}\-\)\?\)\([0-9]\{4\}\)\( '"$copyright"'.*$\)'
	old_year="$(printf '%s\n' "$c" | sed "s/$s/\\4/")"
	if [ -z "$old_year" ] || printf '%s\n' "$old_year" | grep -P '[^0-9]' > /dev/null ; then
		printf 'Could not determine new copyright year for %s, skipping\n' "$file"
		continue
	fi
	
	case "$file" in
		COPYING|LICENSE)
			new_year="$(git --git-dir="$repo/.git" log -1 --format=%cd --date=short)" ;;
		*)
			new_year="$(git --git-dir="$repo/.git" log -1 --format=%cd --date=short -- "$file")"
	esac
	new_year="${new_year%%-*}"
	if [ -z "$new_year" ] || printf '%s\n' "$new_year" | grep -P '[^0-9]' > /dev/null ; then
		printf 'Could not determine new copyright year for %s, skipping\n' "$file"
		continue
	fi
	
	[ "$new_year" = "$old_year" ] && continue
	
	if [ ! "$new_year" -gt "$old_year" ] ; then
		printf 'Copyright downgrade in %s: %s→%s, skipping\n' "$file" "$old_year" "$new_year"
		continue
	fi
	
	first_year="$(printf '%s\n' "$c" | sed "s/$s/\\3/")"
	if [ -z "$first_year" ] ; then
		replacement="$old_year-$new_year"
		old="$old_year"
		new="$old_year-$new_year"
	else
		replacement="$new_year"
		old="$first_year$old_year"
		new="$first_year$new_year"
	fi
	
	printf '%s: %s → %s\n' "$file" "$old" "$new"
	sed -i "s/$s/\\1$replacement\\5/" "$path"
	
done
```

## File: `src/configure.hpp.in`
```

#ifndef INNOEXTRACT_CONFIGURE_HPP
#define INNOEXTRACT_CONFIGURE_HPP

// Console functions
#cmakedefine01 INNOEXTRACT_HAVE_ISATTY
#cmakedefine01 INNOEXTRACT_HAVE_IOCTL

// Time functions
#cmakedefine01 INNOEXTRACT_HAVE_TIMEGM
#cmakedefine01 INNOEXTRACT_HAVE_GMTIME_R

// File functions
#cmakedefine01 INNOEXTRACT_HAVE_UTIMENSAT
#cmakedefine01 INNOEXTRACT_HAVE_DYNAMIC_UTIMENSAT
#cmakedefine01 INNOEXTRACT_HAVE_AT_FDCWD
#cmakedefine01 INNOEXTRACT_HAVE_UTIMES

// Shared functions
#cmakedefine01 INNOEXTRACT_HAVE_DLSYM

// Endianness
#cmakedefine01 INNOEXTRACT_HAVE_BUILTIN_BSWAP16
#cmakedefine01 INNOEXTRACT_HAVE_BUILTIN_BSWAP32
#cmakedefine01 INNOEXTRACT_HAVE_BUILTIN_BSWAP64
#cmakedefine01 INNOEXTRACT_HAVE_BSWAP_16
#cmakedefine01 INNOEXTRACT_HAVE_BSWAP_32
#cmakedefine01 INNOEXTRACT_HAVE_BSWAP_64

// C++11 functionality
#cmakedefine01 INNOEXTRACT_HAVE_ALIGNOF
#cmakedefine01 INNOEXTRACT_HAVE_STD_CODECVT_UTF8_UTF16
#cmakedefine01 INNOEXTRACT_HAVE_STD_UNIQUE_PTR

// Optional dependencies
#cmakedefine01 INNOEXTRACT_HAVE_DECRYPTION
#cmakedefine01 INNOEXTRACT_HAVE_LZMA
#cmakedefine01 INNOEXTRACT_HAVE_ICONV
#cmakedefine01 INNOEXTRACT_HAVE_WIN32_CONV
#cmakedefine01 INNOEXTRACT_HAVE_BUILTIN_CONV

// Process functions
#cmakedefine01 INNOEXTRACT_HAVE_POSIX_SPAWNP
#cmakedefine01 INNOEXTRACT_HAVE_UNISTD_ENVIRON
#cmakedefine01 INNOEXTRACT_HAVE_FORK
#cmakedefine01 INNOEXTRACT_HAVE_EXECVP
#cmakedefine01 INNOEXTRACT_HAVE_WAITPID

#endif // INNOEXTRACT_CONFIGURE_HPP
```

## File: `src/index.hpp`
```
/*
 * Copyright (C) 2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#ifndef INNOEXTRACT_INDEX_HPP
#define INNOEXTRACT_INDEX_HPP

/*!
 * \mainpage innoextract Developer Documentation
 *
 * To find out about how Inno Setup files are structured, start at \ref loader::offsets.
 *
 */

#endif // INNOEXTRACT_INDEX_HPP
```

## File: `src/release.cpp.in`
```
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "release.hpp"

/*
 * \file
 *
 * This file is automatically processed by cmake if the version or commit id changes.
 * For the exact syntax see the documentation of the configure_file() cmake command.
 * For available variables see cmake/VersionString.cmake.
 */

#if ${VERSION_COUNT} != 5
#error "Configure error - the VERSION file should specify exactly two lines!"
#endif

#if ${LICENSE_COUNT} < 3
#error "Configure error - the LICENSE file should specify at least three lines!"
#endif

const char innoextract_name[] = "${VERSION_0_NAME}";

const char innoextract_version[] = "${VERSION_0_STRING}${VERSION_SUFFIX}${GIT_SUFFIX_7}";

const char innosetup_versions[] = "${VERSION_2}";

const char innoextract_bugs[] = "${VERSION_4}";

const char innoextract_copyright[] = "${LICENSE_0_LINE}";

const char innoextract_license[] = "${LICENSE_TAIL}";
```

## File: `src/release.hpp`
```
/*
 * Copyright (C) 2011-2015 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Strings describing the innoextract version.
 */
#ifndef INNOEXTRACT_RELEASE_HPP
#define INNOEXTRACT_RELEASE_HPP

//! Name of the program being built
extern const char innoextract_name[];

//! Name + version of the program being built
extern const char innoextract_version[];

//! Range of supported Inno Setup versions
extern const char innosetup_versions[];

//! Bug tracker URL
extern const char innoextract_bugs[];

//! Copyright line for the current program
extern const char innoextract_copyright[];

//! License text for the current program
extern const char innoextract_license[];

#endif // INNOEXTRACT_RELEASE_HPP
```

## File: `src/cli/debug.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "cli/debug.hpp"

#include <ctime>
#include <iostream>

#include <boost/foreach.hpp>
#include <boost/filesystem/operations.hpp>
#include <boost/range/size.hpp>

#include "loader/offsets.hpp"

#include "setup/component.hpp"
#include "setup/data.hpp"
#include "setup/delete.hpp"
#include "setup/directory.hpp"
#include "setup/file.hpp"
#include "setup/header.hpp"
#include "setup/icon.hpp"
#include "setup/info.hpp"
#include "setup/ini.hpp"
#include "setup/item.hpp"
#include "setup/language.hpp"
#include "setup/message.hpp"
#include "setup/permission.hpp"
#include "setup/registry.hpp"
#include "setup/run.hpp"
#include "setup/task.hpp"
#include "setup/type.hpp"
#include "setup/version.hpp"

#include "stream/block.hpp"

#include "util/fstream.hpp"
#include "util/load.hpp"
#include "util/log.hpp"
#include "util/output.hpp"
#include "util/time.hpp"

namespace fs = boost::filesystem;

void print_offsets(const loader::offsets & offsets) {
	
	std::cout << "loaded offsets:" << '\n';
	if(offsets.exe_offset) {
		std::cout << "- exe: @ " << color::cyan << print_hex(offsets.exe_offset)
		          << color::reset;
		if(offsets.exe_compressed_size) {
			std::cout << "  compressed: " << color::cyan
			          << print_hex(offsets.exe_compressed_size) << color::reset;
		}
		std::cout << "  uncompressed: " << color::cyan
		          << print_bytes(offsets.exe_uncompressed_size) << color::reset;
		std::cout << "  checksum: " << color::cyan << offsets.exe_checksum
		          << color::reset << '\n';
	}
	std::cout << if_not_zero("- message offset", print_hex(offsets.message_offset));
	std::cout << "- header offset: " << color::cyan << print_hex(offsets.header_offset)
	          << color::reset << '\n';
	std::cout << if_not_zero("- data offset", print_hex(offsets.data_offset));
}

static void print(std::ostream & os, const setup::windows_version_range & winver,
                  const setup::header & header) {
	
	const setup::windows_version_range & def = header.winver;
	
	os << if_not_equal("  Min version", winver.begin, def.begin);
	os << if_not_equal("  Only below version", winver.end, def.end);
}

static void print(std::ostream & os, const setup::item & item,
                 const setup::header & header) {
	
	os << if_not_empty("  Componenets", item.components);
	os << if_not_empty("  Tasks", item.tasks);
	os << if_not_empty("  Languages", item.languages);
	os << if_not_empty("  Check", item.check);
	os << if_not_empty("  After install", item.after_install);
	os << if_not_empty("  Before install", item.before_install);
	
	print(os, item.winver, header);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::language_entry & entry) {
	
	(void)info, (void)i;
	
	std::cout << " - " << quoted(entry.name) << ':' << '\n';
	std::cout << if_not_empty("  Language name", entry.language_name);
	std::cout << if_not_empty("  Dialog font", entry.dialog_font);
	std::cout << if_not_empty("  Title font", entry.title_font);
	std::cout << if_not_empty("  Welcome font", entry.welcome_font);
	std::cout << if_not_empty("  Copyright font", entry.copyright_font);
	std::cout << if_not_empty("  Data", entry.data);
	std::cout << if_not_empty("  License", entry.license_text);
	std::cout << if_not_empty("  Info before text", entry.info_before);
	std::cout << if_not_empty("  Info after text", entry.info_after);
	
	std::cout << "  Language id: " << color::cyan << std::hex << entry.language_id
	          << std::dec << color::reset << '\n';
	
	std::cout << if_not_zero("  Codepage", entry.codepage);
	std::cout << if_not_zero("  Dialog font size", entry.dialog_font_size);
	std::cout << if_not_zero("  Dialog font standard height",
	                         entry.dialog_font_standard_height);
	std::cout << if_not_zero("  Title font size", entry.title_font_size);
	std::cout << if_not_zero("  Welcome font size", entry.welcome_font_size);
	std::cout << if_not_zero("  Copyright font size", entry.copyright_font_size);
	std::cout << if_not_equal("  Right to left", entry.right_to_left, false);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::message_entry & entry) {
	
	(void)i;
	
	std::cout << " - " << quoted(entry.name);
	if(entry.language < 0) {
		std::cout << " (default) = ";
	} else if(size_t(entry.language) >= info.languages.size()) {
		std::cout << " [" << color::red << size_t(entry.language) << color::reset << "] = ";
	} else {
		std::cout << " (" << color::cyan << info.languages[size_t(entry.language)].name
		          << color::reset << ") = ";
	}
	std::cout << quoted(entry.value) << '\n';
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::permission_entry & entry) {
	
	(void)info, (void)i;
	
	std::cout << " - " << print_bytes(entry.permissions.length()) << '\n';
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::type_entry & entry) {
	
	(void)i;
	
	std::cout << " - " << quoted(entry.name) << ':' << '\n';
	std::cout << if_not_empty("  Description", entry.description);
	std::cout << if_not_empty("  Languages", entry.languages);
	std::cout << if_not_empty("  Check", entry.check);
	
	print(std::cout, entry.winver, info.header);
	
	std::cout << if_not_equal("  Custom setup type", entry.custom_type, false);
	std::cout << if_not_equal("  Type", entry.type, setup::type_entry::User);
	std::cout << if_not_zero("  Size", entry.size);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::component_entry & entry) {
	
	(void)i;
	
	std::cout << " - " << quoted(entry.name) << ':' << '\n';
	std::cout << if_not_empty("  Types", entry.types);
	std::cout << if_not_empty("  Description", entry.description);
	std::cout << if_not_empty("  Languages", entry.languages);
	std::cout << if_not_empty("  Check", entry.check);
	std::cout << if_not_zero("  Extra disk space required", entry.extra_disk_pace_required);
	std::cout << if_not_zero("  Level", entry.level);
	std::cout << if_not_equal("  Used", entry.used, true);
	
	print(std::cout, entry.winver, info.header);
	
	std::cout << if_not_zero("  Options", entry.options);
	std::cout << if_not_zero("  Size", entry.size);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::task_entry & entry) {
	
	(void)i;
	
	std::cout << " - " << quoted(entry.name) << ':' << '\n';
	std::cout << if_not_empty("  Description", entry.description);
	std::cout << if_not_empty("  Group description", entry.group_description);
	std::cout << if_not_empty("  Components", entry.components);
	std::cout << if_not_empty("  Languages", entry.languages);
	std::cout << if_not_empty("  Check", entry.check);
	std::cout << if_not_zero("  Level", entry.level);
	std::cout << if_not_equal("  Used", entry.used, true);
	
	print(std::cout, entry.winver, info.header);
	
	std::cout << if_not_zero("  Options", entry.options);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::directory_entry & entry) {
	
	(void)i;
	
	std::cout << " - " << quoted(entry.name) << ':' << '\n';
	
	print(std::cout, entry, info.header);
	
	if(!entry.permissions.empty()) {
		std::cout << "  Permissions: " << entry.permissions.length() << " bytes";
	}
	
	std::cout << if_not_zero("  Attributes", entry.attributes);
	std::cout << if_not_equal("  Permission entry", entry.permission, boost::int16_t(-1));
	std::cout << if_not_zero("  Options", entry.options);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::file_entry & entry) {
	
	if(entry.destination.empty()) {
		std::cout << " - File #" << i;
	} else {
		std::cout << " - " << quoted(entry.destination);
	}
	if(entry.location != boost::uint32_t(-1)) {
		std::cout << " (location: " << color::cyan << entry.location << color::reset << ')';
	}
	std::cout  << '\n';
	
	std::cout << if_not_empty("  Source", entry.source);
	std::cout << if_not_empty("  Install font name", entry.install_font_name);
	std::cout << if_not_empty("  Strong assembly name", entry.strong_assembly_name);
	
	print(std::cout, entry, info.header);
	
	std::cout << if_not_zero("  Attributes", entry.attributes);
	std::cout << if_not_zero("  Size", entry.external_size);
	std::cout << if_not_equal("  Permission entry", entry.permission, boost::int16_t(-1));
	std::cout << if_not_zero("  Options", entry.options);
	std::cout << if_not_equal("  Type", entry.type, setup::file_entry::UserFile);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::icon_entry & entry) {
	
	(void)i;
	
	std::cout << " - " << quoted(entry.name) << " -> " << quoted(entry.filename) << '\n';
	std::cout << if_not_empty("  Parameters", entry.parameters);
	std::cout << if_not_empty("  Working directory", entry.working_dir);
	std::cout << if_not_empty("  Icon file", entry.icon_file);
	std::cout << if_not_empty("  Comment", entry.comment);
	std::cout << if_not_empty("  App user model id", entry.app_user_model_id);
	
	print(std::cout, entry, info.header);
	
	std::cout << if_not_zero("  Icon index", entry.icon_index);
	std::cout << if_not_equal("  Show command", entry.show_command, 1);
	std::cout << if_not_equal("  Close on exit", entry.close_on_exit,
	                          setup::icon_entry::NoSetting);
	std::cout << if_not_zero("  Hotkey", entry.hotkey);
	std::cout << if_not_zero("  Options", entry.options);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::ini_entry & entry) {
	
	(void)i;
	
	std::cout << " - in " << quoted(entry.inifile);
	std::cout << " set [" << quoted(entry.section) << "] ";
	std::cout << quoted(entry.key) << " = " << quoted(entry.value) << '\n';
	
	print(std::cout, entry, info.header);
	
	std::cout << if_not_zero("  Options", entry.options);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::registry_entry & entry) {
	
	(void)i;
	
	std::cout << " - ";
	if(entry.hive != setup::registry_entry::Unset) {
		std::cout << entry.hive << '\\';
	}
	std::cout << quoted(entry.key);
	std::cout << '\n' << "  ";
	if(entry.name.empty()) {
		std::cout << "(default)";
	} else {
		std::cout << quoted(entry.name);
	}
	if(!entry.value.empty()) {
		std::cout << " = " << quoted(entry.value);
	}
	if(entry.type != setup::registry_entry::None) {
		std::cout << " (" << color::cyan << entry.type << color::reset << ')';
	}
	std::cout << '\n';
	
	print(std::cout, entry, info.header);
	
	if(!entry.permissions.empty()) {
		std::cout << "  Permissions: " << entry.permissions.length() << " bytes";
	}
	std::cout << if_not_equal("  Permission entry", entry.permission, -1);
	std::cout << if_not_zero("  Options", entry.options);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::delete_entry & entry) {
	
	(void)i;
	
	std::cout << " - " << quoted(entry.name)
	     << " (" << color::cyan << entry.type << color::reset << ')' << '\n';
	
	print(std::cout, entry, info.header);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::run_entry & entry) {
	
	(void)i;
	
	std::cout << " - " << quoted(entry.name) << ':' << '\n';
	std::cout << if_not_empty("  Parameters", entry.parameters);
	std::cout << if_not_empty("  Working directory", entry.working_dir);
	std::cout << if_not_empty("  Run once id", entry.run_once_id);
	std::cout << if_not_empty("  Status message", entry.status_message);
	std::cout << if_not_empty("  Verb", entry.verb);
	std::cout << if_not_empty("  Description", entry.verb);
	
	print(std::cout, entry, info.header);
	
	std::cout << if_not_equal("  Show command", entry.show_command, 1);
	std::cout << if_not_equal("  Wait", entry.wait, setup::run_entry::WaitUntilTerminated);
	std::cout << if_not_zero("  Options", entry.options);
}

static void print_entry(const setup::info & info, size_t i,
                        const setup::data_entry & entry) {
	
	(void)info;
	
	std::cout << " - " << "File location #" << i << ':' << '\n';
	std::cout << if_not_zero("  First slice", entry.chunk.first_slice);
	std::cout << if_not_equal("  Last slice", entry.chunk.last_slice,
	                          entry.chunk.first_slice);
	std::cout << "  Chunk: offset " << color::cyan << print_hex(entry.chunk.offset)
	          << color::reset << " size " << color::cyan << print_hex(entry.chunk.size)
	          << color::reset << '\n';
	std::cout << if_not_zero("  File offset", print_hex(entry.file.offset));
	std::cout << if_not_zero("  File size", print_bytes(entry.file.size));
	
	std::cout << "  Checksum: " << entry.file.checksum << '\n';
	
	std::tm t = util::format_time(entry.timestamp);
	
	bool isUTC = ((entry.options & setup::data_entry::TimeStampInUTC) != 0);
	std::cout << "  Timestamp: " << color::cyan << (t.tm_year + 1900)
	          << '-' << std::setfill('0') << std::setw(2) << (t.tm_mon + 1)
	          << '-' << std::setfill('0') << std::setw(2) << t.tm_mday
	          << ' ' << std::setfill(' ') << std::setw(2) << t.tm_hour
	          << ':' << std::setfill('0') << std::setw(2) << t.tm_min
	          << ':' << std::setfill('0') << std::setw(2) << t.tm_sec
	          << color::reset << " +" << entry.timestamp_nsec
	          << (isUTC ? " (UTC)" : " (local)")
	          << '\n';
	
	setup::data_entry::flags options = entry.options;
	options &= ~setup::data_entry::VersionInfoNotValid;
	std::cout << if_not_zero("  Options", options);
	
	if(entry.options & setup::data_entry::VersionInfoValid) {
		std::cout << "  File version: " << ((entry.file_version >> 48) & 0xffff) << '.'
		                                << ((entry.file_version >> 32) & 0xffff) << '.'
		                                << ((entry.file_version >> 16) & 0xffff) << '.'
		                                << ((entry.file_version >>  0) & 0xffff) << '\n';
	}
}

template <class Entry>
static void print_entries(const setup::info & info, const std::vector<Entry> & entries,
                          const std::string & name) {
	
	if(entries.empty()) {
		return;
	}
	
	std::cout << '\n' << name << ":\n";
	for(size_t i = 0; i < entries.size(); i++) {
		print_entry(info, i, entries[i]);
	}
}

static void print_header(const setup::header & header) {
	
	std::cout << if_not_empty("App name", header.app_name);
	std::cout << if_not_empty("App ver name", header.app_versioned_name);
	std::cout << if_not_empty("App id", header.app_id);
	std::cout << if_not_empty("Copyright", header.app_copyright);
	std::cout << if_not_empty("Publisher", header.app_publisher);
	std::cout << if_not_empty("Publisher URL", header.app_publisher_url);
	std::cout << if_not_empty("Support phone", header.app_support_phone);
	std::cout << if_not_empty("Support URL", header.app_support_url);
	std::cout << if_not_empty("Updates URL", header.app_updates_url);
	std::cout << if_not_empty("Version", header.app_version);
	std::cout << if_not_empty("Default dir name", header.default_dir_name);
	std::cout << if_not_empty("Default group name", header.default_group_name);
	std::cout << if_not_empty("Uninstall icon name", header.uninstall_icon_name);
	std::cout << if_not_empty("Base filename", header.base_filename);
	std::cout << if_not_empty("Uninstall files dir", header.uninstall_files_dir);
	std::cout << if_not_empty("Uninstall display name", header.uninstall_name);
	std::cout << if_not_empty("Uninstall display icon", header.uninstall_icon);
	std::cout << if_not_empty("App mutex", header.app_mutex);
	std::cout << if_not_empty("Default user name", header.default_user_name);
	std::cout << if_not_empty("Default user org", header.default_user_organisation);
	std::cout << if_not_empty("Default user serial", header.default_serial);
	std::cout << if_not_empty("Readme", header.app_readme_file);
	std::cout << if_not_empty("Contact", header.app_contact);
	std::cout << if_not_empty("Comments", header.app_comments);
	std::cout << if_not_empty("Modify path", header.app_modify_path);
	std::cout << if_not_empty("Uninstall reg key", header.create_uninstall_registry_key);
	std::cout << if_not_empty("Uninstallable", header.uninstallable);
	std::cout << if_not_empty("License", header.license_text);
	std::cout << if_not_empty("Info before text", header.info_before);
	std::cout << if_not_empty("Info after text", header.info_after);
	std::cout << if_not_empty("Uninstaller signature", header.uninstaller_signature);
	std::cout << if_not_empty("Compiled code", header.compiled_code);
	
	std::cout << if_not_zero("Lead bytes", header.lead_bytes);
	
	std::cout << if_not_zero("Language entries", header.language_count);
	std::cout << if_not_zero("Custom message entries", header.message_count);
	std::cout << if_not_zero("Permission entries", header.permission_count);
	std::cout << if_not_zero("Type entries", header.type_count);
	std::cout << if_not_zero("Component entries", header.component_count);
	std::cout << if_not_zero("Task entries", header.task_count);
	std::cout << if_not_zero("Dir entries", header.directory_count);
	std::cout << if_not_zero("File entries", header.file_count);
	std::cout << if_not_zero("File location entries", header.data_entry_count);
	std::cout << if_not_zero("Icon entries", header.icon_count);
	std::cout << if_not_zero("Ini entries", header.ini_entry_count);
	std::cout << if_not_zero("Registry entries", header.registry_entry_count);
	std::cout << if_not_zero("Delete entries", header.delete_entry_count);
	std::cout << if_not_zero("Uninstall delete entries", header.uninstall_delete_entry_count);
	std::cout << if_not_zero("Run entries", header.run_entry_count);
	std::cout << if_not_zero("Uninstall run entries", header.uninstall_run_entry_count);
	
	std::cout << if_not_equal("Min version", header.winver.begin,
	                          setup::windows_version::none);
	std::cout << if_not_equal("Only below version", header.winver.end,
	                          setup::windows_version::none);
	
	std::cout << std::hex;
	std::cout << if_not_zero("Back color", header.back_color);
	std::cout << if_not_zero("Back color2", header.back_color2);
	std::cout << if_not_zero("Wizard image back color", header.image_back_color);
	std::cout << if_not_zero("Wizard small image back color",
	                         header.small_image_back_color);
	std::cout << std::dec;
	
	if(header.options & (setup::header::Password | setup::header::EncryptionUsed)) {
		std::cout << "Password hash: " << color::cyan << header.password << color::reset << '\n';
		if(!header.password_salt.empty()) {
			std::cout << "Password salt: " << color::cyan
			          << print_hex(header.password_salt) << color::reset << '\n';
		}
	}
	
	std::cout << if_not_zero("Extra disk space required", header.extra_disk_space_required);
	std::cout << if_not_zero("Slices per disk", header.slices_per_disk);
	
	std::cout << if_not_equal("Install mode", header.install_mode,
	                          setup::header::NormalInstallMode);
	std::cout << "Uninstall log mode: " << color::cyan << header.uninstall_log_mode
	          << color::reset << '\n';
	std::cout << "Uninstall style: " << color::cyan << header.uninstall_style
	          << color::reset << '\n';
	std::cout << "Dir exists warning: " << color::cyan << header.dir_exists_warning
	          << color::reset << '\n';
	std::cout << if_not_equal("Privileges required", header.privileges_required,
	                                                 setup::header::NoPrivileges);
	std::cout << "Show language dialog: " << color::cyan << header.show_language_dialog
	          << color::reset << '\n';
	std::cout << if_not_equal("Language detection", header.language_detection,
	                          setup::header::NoLanguageDetection);
	std::cout << "Compression: " << color::cyan << header.compression
	          << color::reset << '\n';
	std::cout << "Architectures allowed: " << color::cyan << header.architectures_allowed
	          << color::reset << '\n';
	std::cout << "Architectures installed in 64-bit mode: " << color::cyan
	          << header.architectures_installed_in_64bit_mode << color::reset << '\n';
	
	if(header.options & setup::header::SignedUninstaller) {
		std::cout << if_not_zero("Size before signing uninstaller",
		                         header.signed_uninstaller_original_size);
		std::cout << if_not_zero("Uninstaller header checksum",
		                         header.signed_uninstaller_header_checksum);
	}
	
	std::cout << "Disable dir page: " << color::cyan << header.disable_dir_page
	          << color::reset << '\n';
	std::cout << "Disable program group page: " << color::cyan
	          << header.disable_program_group_page << color::reset << '\n';
	
	std::cout << if_not_zero("Uninstall display size", header.uninstall_display_size);
	
	std::cout << "Options: " << color::green << header.options << color::reset << '\n';
	
	std::cout << color::reset;
}

static const char * magic_numbers[][2] = {
	{ "GIF89a", "gif" },
	{ "GIF87a", "gif" },
	{ "\xFF\xD8", "jpg" },
	{ "\x89PNG\r\n\x1A\n", "png" },
	{ "%PDF", "pdf" },
	{ "MZ", "dll" },
	{ "BM", "bmp" },
};

static const char * guess_extension(const std::string & data) {
	
	for(size_t i = 0; i < size_t(boost::size(magic_numbers)); i++) {
		
		size_t n = strlen(magic_numbers[i][0]);
		
		if(!data.compare(0, n, magic_numbers[i][0], n)) {
			return magic_numbers[i][1];
		}
	}
	
	return "bin";
}

static void print_aux(const setup::info & info) {
	
	if(info.wizard_images.empty() && info.wizard_images_small.empty()
	   && info.decompressor_dll.empty()) {
		return;
	}
	
	std::cout << '\n';
	
	for(size_t i = 0; i < info.wizard_images.size(); i++) {
		std::cout << "Wizard image #" << (i + 1) << ": " << print_bytes(info.wizard_images[i].length())
		          << " (" << guess_extension(info.wizard_images[i]) << ")\n";
	}
	
	for(size_t i = 0; i < info.wizard_images_small.size(); i++) {
		std::cout << "Wizard small image #" << (i + 1) << ": "
		          << print_bytes(info.wizard_images_small[i].length())
		          << " (" << guess_extension(info.wizard_images_small[i]) << ")\n";
	}
	
	if(!info.decompressor_dll.empty()) {
		std::cout << "Decompressor dll: " << print_bytes(info.decompressor_dll.length())
		          << " (" << guess_extension(info.decompressor_dll) << ")\n";
	}
	
}

void print_info(const setup::info & info) {
	
	std::ios_base::fmtflags old = std::cout.flags();
	std::cout << std::boolalpha;
	
	print_header(info.header);
	
	print_entries(info, info.languages, "Languages");
	print_entries(info, info.messages, "Messages");
	print_entries(info, info.permissions, "Permissions");
	print_entries(info, info.types, "Types");
	print_entries(info, info.components, "Components");
	print_entries(info, info.tasks, "Tasks");
	print_entries(info, info.directories, "Directories");
	print_entries(info, info.files, "Files");
	print_entries(info, info.icons, "Icons");
	print_entries(info, info.ini_entries, "INI entries");
	print_entries(info, info.registry_entries, "Registry entries");
	print_entries(info, info.delete_entries, "Delete entries");
	print_entries(info, info.uninstall_delete_entries, "Uninstall delete entries");
	print_entries(info, info.run_entries, "Run entries");
	print_entries(info, info.uninstall_run_entries, "Uninstall run entries");
	print_entries(info, info.data_entries, "Data entries");
	
	print_aux(info);
	
	std::cout.setf(old, std::ios_base::boolalpha);
}

static void dump_headers(std::istream & is, const setup::version & version, const extract_options & o, int i) {
	
	std::string filename;
	{
		std::ostringstream oss;
		oss << "headers" << i << ".bin";
		filename = oss.str();
	}
	
	const char * type = (i == 0 ? "primary" : "secondary");
	if(!o.quiet) {
		std::cout << "Dumping " << type << " setup headers to \""
		          << color::white << filename << color::reset << "\"\n";
	} else if(!o.silent) {
		std::cout << filename << '\n';
	}
	
	fs::path path = o.output_dir / filename;
	util::ofstream ofs;
	try {
		ofs.open(path, std::ios_base::out | std::ios_base::trunc | std::ios_base::binary);
		if(!ofs.is_open()) {
			throw std::exception();
		}
	} catch(...) {
		throw std::runtime_error("Could not open output file \"" + path.string() + '"');
	}
	
	try {
		ofs << stream::block_reader::get(is, version)->rdbuf();
	} catch(const std::exception & e) {
		std::ostringstream oss;
		oss << "Stream error while dumping " << type << " setup headers!\n";
		oss << " ├─ detected setup version: " << version << '\n';
		oss << " └─ error reason: " << e.what();
		throw format_error(oss.str());
	}
	
}

void dump_headers(std::istream & is, const loader::offsets & offsets, const extract_options & o) {
	
	setup::version version;
	is.seekg(offsets.header_offset);
	version.load(is);
	
	dump_headers(is, version, o, 0);
	dump_headers(is, version, o, 1);
	
}
```

## File: `src/cli/debug.hpp`
```
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Debug output functions.
 */
#ifndef INNOEXTRACT_CLI_DEBUG_HPP
#define INNOEXTRACT_CLI_DEBUG_HPP

#include <iosfwd>

#include "configure.hpp"

#include "cli/extract.hpp"

#ifdef DEBUG

namespace loader { struct offsets; }
namespace setup { struct info; }

void print_offsets(const loader::offsets & offsets);
void print_info(const setup::info & info);

void dump_headers(std::istream & is, const loader::offsets & offsets, const extract_options & o);

#endif // DEBUG

#endif // INNOEXTRACT_CLI_DEBUG_HPP
```

## File: `src/cli/extract.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "cli/extract.hpp"

#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>
#include <limits>

#include <boost/foreach.hpp>
#include <boost/noncopyable.hpp>
#include <boost/scoped_ptr.hpp>
#include <boost/unordered_map.hpp>
#include <boost/algorithm/string/case_conv.hpp>
#include <boost/filesystem/operations.hpp>
#include <boost/ptr_container/ptr_map.hpp>
#include <boost/ptr_container/ptr_vector.hpp>
#include <boost/range/size.hpp>

#include <boost/version.hpp>
#if BOOST_VERSION >= 104800
#include <boost/container/flat_map.hpp>
#endif

#include "cli/debug.hpp"
#include "cli/gog.hpp"
#include "cli/goggalaxy.hpp"

#include "crypto/checksum.hpp"
#include "crypto/hasher.hpp"

#include "loader/offsets.hpp"

#include "setup/data.hpp"
#include "setup/directory.hpp"
#include "setup/expression.hpp"
#include "setup/file.hpp"
#include "setup/info.hpp"
#include "setup/language.hpp"

#include "stream/chunk.hpp"
#include "stream/file.hpp"
#include "stream/slice.hpp"

#include "util/boostfs_compat.hpp"
#include "util/console.hpp"
#include "util/encoding.hpp"
#include "util/fstream.hpp"
#include "util/load.hpp"
#include "util/log.hpp"
#include "util/output.hpp"
#include "util/time.hpp"

namespace fs = boost::filesystem;

namespace {

template <typename Entry>
class processed_item {
	
	std::string path_;
	const Entry * entry_;
	
public:
	
	processed_item(const std::string & path, const Entry * entry)
		: path_(path), entry_(entry) { }
	
	bool has_entry() const { return entry_ != NULL; }
	const Entry & entry() const { return *entry_; }
	const std::string & path() const { return path_; }
	
	void set_entry(const Entry * entry) { entry_ = entry; }
	void set_path(const std::string & path) { path_ = path; }
	
};

class processed_file : public processed_item<setup::file_entry> {
	
public:
	
	processed_file(const setup::file_entry * entry, const std::string & path)
		: processed_item<setup::file_entry>(path, entry) { }
	
	bool is_multipart() const { return !entry().additional_locations.empty(); }
	
};

class processed_directory : public processed_item<setup::directory_entry> {
	
	bool implied_;
	
public:
	
	explicit processed_directory(const std::string & path)
		: processed_item<setup::directory_entry>(path, NULL), implied_(false) { }
	
	bool implied() const { return implied_; }
	
	void set_implied(bool implied) { implied_ = implied; }
	
};

class file_output : private boost::noncopyable {
	
	fs::path path_;
	const processed_file * file_;
	util::fstream stream_;
	
	crypto::hasher checksum_;
	boost::uint64_t checksum_position_;
	
	boost::uint64_t position_;
	boost::uint64_t total_written_;
	
	bool write_;
	
public:
	
	explicit file_output(const fs::path & dir, const processed_file * f, bool write)
		: path_(dir / f->path())
		, file_(f)
		, checksum_(f->entry().checksum.type)
		, checksum_position_(f->entry().checksum.type == crypto::None ? boost::uint64_t(-1) : 0)
		, position_(0)
		, total_written_(0)
		, write_(write)
	{
		if(write_) {
			try {
				std::ios_base::openmode flags = std::ios_base::out | std::ios_base::binary | std::ios_base::trunc;
				if(file_->is_multipart()) {
					flags |= std::ios_base::in;
				}
				stream_.open(path_, flags);
				if(!stream_.is_open()) {
					throw std::exception();
				}
			} catch(...) {
				throw std::runtime_error("Could not open output file \"" + path_.string() + '"');
			}
		}
	}
	
	bool write(const char * data, size_t n) {
		
		if(write_) {
			stream_.write(data, std::streamsize(n));
		}
		
		if(checksum_position_ == position_) {
			checksum_.update(data, n);
			checksum_position_ += n;
		}
		
		position_ += n;
		total_written_ += n;
		
		return !write_ || !stream_.fail();
	}
	
	void seek(boost::uint64_t new_position) {
		
		if(new_position == position_) {
			return;
		}
		
		debug("seeking output from " << print_hex(position_) << " to " << print_hex(new_position));
		
		if(!write_) {
			position_ = new_position;
			return;
		}
		
		const boost::uint64_t max = boost::uint64_t(std::numeric_limits<util::fstream::off_type>::max() / 4);
		
		if(new_position <= max) {
			stream_.seekp(util::fstream::off_type(new_position), std::ios_base::beg);
		} else {
			util::fstream::off_type sign = (new_position > position_) ? 1 : -1;
			boost::uint64_t diff = (new_position > position_) ? new_position - position_ : position_ - new_position;
			while(diff > 0) {
				stream_.seekp(sign * util::fstream::off_type(std::min(diff, max)), std::ios_base::cur);
				diff -= std::min(diff, max);
			}
		}
		
		position_ = new_position;
		
	}
	
	void close() {
		
		if(write_) {
			stream_.close();
		}
		
	}
	
	const fs::path & path() const { return path_; }
	const processed_file * file() const { return file_; }
	
	bool is_complete() const {
		return total_written_ == file_->entry().size;
	}
	
	bool has_checksum() const {
		return checksum_position_ == file_->entry().size;
	}
	
	bool calculate_checksum() {
		
		if(has_checksum()) {
			return true;
		}
		
		if(!write_) {
			return false;
		}
		
		debug("calculating output checksum for " << path_);
		
		const boost::uint64_t max = boost::uint64_t(std::numeric_limits<util::fstream::off_type>::max() / 4);
		
		boost::uint64_t diff = checksum_position_;
		stream_.seekg(util::fstream::off_type(std::min(diff, max)), std::ios_base::beg);
		diff -= std::min(diff, max);
		while(diff > 0) {
			stream_.seekg(util::fstream::off_type(std::min(diff, max)), std::ios_base::cur);
			diff -= std::min(diff, max);
		}
		
		while(!stream_.eof()) {
			char buffer[8192];
			std::streamsize n = stream_.read(buffer, sizeof(buffer)).gcount();
			checksum_.update(buffer, size_t(n));
			checksum_position_ += boost::uint64_t(n);
		}
		
		if(!has_checksum()) {
			log_warning << "Could not read back " << path_ << " to calculate output checksum for multi-part file";
			return false;
		}
		
		return true;
	}
	
	crypto::checksum checksum() {
		return checksum_.finalize();
	}
	
};

class path_filter {
	
	typedef std::pair<bool, std::string> Filter;
	std::vector<Filter> includes;
	
public:
	
	explicit path_filter(const extract_options & o) {
		BOOST_FOREACH(const std::string & include, o.include) {
			if(!include.empty() && include[0] == setup::path_sep) {
				includes.push_back(Filter(true, boost::to_lower_copy(include) + setup::path_sep));
			} else {
				includes.push_back(Filter(false, setup::path_sep + boost::to_lower_copy(include)
				                                 + setup::path_sep));
			}
		}
	}
	
	bool match(const std::string & path) const {
		
		if(includes.empty()) {
			return true;
		}
		
		BOOST_FOREACH(const Filter & i, includes) {
			if(i.first) {
				if(!i.second.compare(1, i.second.size() - 1,
				                     path + setup::path_sep, 0, i.second.size() - 1)) {
					return true;
				}
			} else {
				if((setup::path_sep + path + setup::path_sep).find(i.second) != std::string::npos) {
					return true;
				}
			}
		}
		
		return false;
	}
	
};

void print_filter_info(const setup::item & item, bool temp) {
	
	bool first = true;
	
	if(!item.languages.empty()) {
		std::cout << " [";
		first = false;
		std::cout << color::green << item.languages << color::reset;
	}
	
	if(temp) {
		std::cout << (first ? " [" : ", ");
		first = false;
		std::cout << color::cyan << "temp" << color::reset;
		
	}
	
	if(!first) {
		std::cout << "]";
	}
	
}

void print_filter_info(const setup::file_entry & file) {
	bool is_temp = !!(file.options & setup::file_entry::DeleteAfterInstall);
	print_filter_info(file, is_temp);
}

void print_filter_info(const setup::directory_entry & dir) {
	bool is_temp = !!(dir.options & setup::directory_entry::DeleteAfterInstall);
	print_filter_info(dir, is_temp);
}

void print_size_info(const stream::file & file, boost::uint64_t size) {
	
	if(logger::debug) {
		std::cout << " @ " << print_hex(file.offset);
	}
	
	std::cout << " (" << color::dim_cyan << print_bytes(size ? size : file.size) << color::reset << ")";
}

void print_checksum_info(const stream::file & file, const crypto::checksum * checksum) {
	
	if(!checksum || checksum->type == crypto::None) {
		checksum = &file.checksum;
	}
	
	std::cout << color::dim_magenta << *checksum << color::reset;
}

void print_file_details(const extract_options & o, const stream::file & file, const stream::chunk & chunk,
                        boost::uint64_t size, const crypto::checksum * checksum, const std::string & key) {
	
	if(o.list_sizes) {
		print_size_info(file, size);
	}
	if(o.list_checksums) {
		std::cout << ' ';
		print_checksum_info(file, checksum);
	}
	if(chunk.encryption != stream::Plaintext && key.empty()) {
		std::cout << " - encrypted";
	}
	std::cout << '\n';
	
}

bool prompt_overwrite() {
	return true; // TODO the user always overwrites
}

const char * handle_collision(const setup::file_entry & oldfile, const setup::data_entry & olddata,
                              const setup::file_entry & newfile, const setup::data_entry & newdata) {
	
	bool allow_timestamp = true;
	
	if(!(newfile.options & setup::file_entry::IgnoreVersion)) {
		
		bool version_info_valid = !!(newdata.options & setup::data_entry::VersionInfoValid);
		
		if(olddata.options & setup::data_entry::VersionInfoValid) {
			allow_timestamp = false;
			
			if(!version_info_valid || olddata.file_version > newdata.file_version) {
				if(!(newfile.options & setup::file_entry::PromptIfOlder) || !prompt_overwrite()) {
					return "old version";
				}
			} else if(newdata.file_version == olddata.file_version
				   && !(newfile.options & setup::file_entry::OverwriteSameVersion)) {
				
				if((newfile.options & setup::file_entry::ReplaceSameVersionIfContentsDiffer)
				   && olddata.file.checksum == newdata.file.checksum) {
					return "duplicate (checksum)";
				}
				
				if(!(newfile.options & setup::file_entry::CompareTimeStamp)) {
					return "duplicate (version)";
				}
				
				allow_timestamp = true;
			}
			
		} else if(version_info_valid) {
			allow_timestamp = false;
		}
		
	}
	
	if(allow_timestamp && (newfile.options & setup::file_entry::CompareTimeStamp)) {
		
		if(newdata.timestamp == olddata.timestamp
		   && newdata.timestamp_nsec == olddata.timestamp_nsec) {
			return "duplicate (modification time)";
		}
		
		
		if(newdata.timestamp < olddata.timestamp
		   || (newdata.timestamp == olddata.timestamp
		       && newdata.timestamp_nsec < olddata.timestamp_nsec)) {
			if(!(newfile.options & setup::file_entry::PromptIfOlder) || !prompt_overwrite()) {
				return "old version (modification time)";
			}
		}
		
	}
	
	if((newfile.options & setup::file_entry::ConfirmOverwrite) && !prompt_overwrite()) {
		return "user chose not to overwrite";
	}
	
	if(oldfile.attributes != boost::uint32_t(-1)
	   && (oldfile.attributes & setup::file_entry::ReadOnly) != 0) {
		if(!(newfile.options & setup::file_entry::OverwriteReadOnly) && !prompt_overwrite()) {
			return "user chose not to overwrite read-only file";
		}
	}
	
	return NULL; // overwrite old file
}

typedef boost::unordered_map<std::string, processed_file> FilesMap;
#if BOOST_VERSION >= 104800
typedef boost::container::flat_map<std::string, processed_directory> DirectoriesMap;
#else
typedef std::map<std::string, processed_directory> DirectoriesMap;
#endif
typedef boost::unordered_map<std::string, std::vector<processed_file> > CollisionMap;

std::string parent_dir(const std::string & path) {
	
	size_t pos = path.find_last_of(setup::path_sep);
	if(pos == std::string::npos) {
		return std::string();
	}
	
	return path.substr(0, pos);
}

bool insert_dirs(DirectoriesMap & processed_directories, const path_filter & includes,
                 const std::string & internal_path, std::string & path, bool implied) {
	
	std::string dir = parent_dir(path);
	std::string internal_dir = parent_dir(internal_path);
	
	if(internal_dir.empty()) {
		return false;
	}
	
	if(implied || includes.match(internal_dir)) {
		
		std::pair<DirectoriesMap::iterator, bool> existing = processed_directories.insert(
			std::make_pair(internal_dir, processed_directory(dir))
		);
		
		if(implied) {
			existing.first->second.set_implied(true);
		}
		
		if(!existing.second) {
			if(existing.first->second.path() != dir) {
				// Existing dir case differs, fix path
				if(existing.first->second.path().length() == dir.length()) {
					path.replace(0, dir.length(), existing.first->second.path());
				} else {
					path = existing.first->second.path() + path.substr(dir.length());
				}
				return true;
			} else {
				return false;
			}
		}
		
		implied = true;
	}
	
	size_t oldlength = dir.length();
	if(insert_dirs(processed_directories, includes, internal_dir, dir, implied)) {
		// Existing dir case differs, fix path
		if(dir.length() == oldlength) {
			path.replace(0, dir.length(), dir);
		} else {
			path = dir + path.substr(oldlength);
		}
		// Also fix previously inserted directory
		DirectoriesMap::iterator inserted = processed_directories.find(internal_dir);
		if(inserted != processed_directories.end()) {
			inserted->second.set_path(dir);
		}
		return true;
	}
	
	return false;
}

bool rename_collision(const extract_options & o, FilesMap & processed_files, const std::string & path,
                      const processed_file & other, bool common_component, bool common_language,
                      bool common_arch, bool first) {
	
	const setup::file_entry & file = other.entry();
	
	bool require_number_suffix = !first || (o.collisions == RenameAllCollisions);
	std::ostringstream oss;
	const setup::file_entry::flags arch_flags = setup::file_entry::Bits32 | setup::file_entry::Bits64;
	
	if(!common_component && !file.components.empty()) {
		if(setup::is_simple_expression(file.components)) {
			require_number_suffix = false;
			oss << '#' << file.components;
		}
	}
	if(!common_language && !file.languages.empty()) {
		if(setup::is_simple_expression(file.languages)) {
			require_number_suffix = false;
			if(file.languages != o.default_language) {
				oss << '@' << file.languages;
			}
		}
	}
	if(!common_arch && (file.options & arch_flags) == setup::file_entry::Bits32) {
		require_number_suffix = false;
		oss << "@32bit";
	} else if(!common_arch && (file.options & arch_flags) == setup::file_entry::Bits64) {
		require_number_suffix = false;
		oss << "@64bit";
	}
	
	size_t i = 0;
	std::string suffix = oss.str();
	if(require_number_suffix) {
		oss << '$' << i++;
	}
	for(;;) {
		std::pair<FilesMap::iterator, bool> insertion = processed_files.insert(std::make_pair(
			path + oss.str(), processed_file(&file, other.path() + oss.str())
		));
		if(insertion.second) {
			// Found an available name and inserted
			return true;
		}
		if(&insertion.first->second.entry() == &file) {
			// File already has the desired name, abort
			return false;
		}
		oss.str(suffix);
		oss << '$' << i++;
	}
	
}

void rename_collisions(const extract_options & o, FilesMap & processed_files,
                       const CollisionMap & collisions) {
	
	BOOST_FOREACH(const CollisionMap::value_type & collision, collisions) {
		
		const std::string & path = collision.first;
		
		const processed_file & base = processed_files.find(path)->second;
		const setup::file_entry & file = base.entry();
		const setup::file_entry::flags arch_flags = setup::file_entry::Bits32 | setup::file_entry::Bits64;
		
		bool common_component = true;
		bool common_language = true;
		bool common_arch = true;
		BOOST_FOREACH(const processed_file & other, collision.second) {
			common_component = common_component && other.entry().components == file.components;
			common_language = common_language && other.entry().languages == file.languages;
			common_arch = common_arch && (other.entry().options & arch_flags) == (file.options & arch_flags);
		}
		
		bool ignore_component = common_component || o.collisions != RenameAllCollisions;
		if(rename_collision(o, processed_files, path, base,
		                    ignore_component, common_language, common_arch, true)) {
			processed_files.erase(path);
		}
		
		BOOST_FOREACH(const processed_file & other, collision.second) {
			rename_collision(o, processed_files, path, other,
			                 common_component, common_language, common_arch, false);
		}
		
	}
}

bool print_file_info(const extract_options & o, const setup::info & info) {
	
	if(!o.quiet) {
		const std::string & name = info.header.app_versioned_name.empty()
		                           ? info.header.app_name : info.header.app_versioned_name;
		const char * verb = "Inspecting";
		if(o.extract) {
			verb = "Extracting";
		} else if(o.test) {
			verb = "Testing";
		} else if(o.list) {
			verb = "Listing";
		}
		std::cout << verb << " \"" << color::green << name << color::reset
		          << "\" - setup data version " << color::white << info.version << color::reset
		          << std::endl;
	}
	
	#ifdef DEBUG
	if(logger::debug) {
		std::cout << '\n';
		print_info(info);
		std::cout << '\n';
	}
	#endif
	
	bool multiple_sections = (o.list_languages + o.gog_game_id + o.list + o.show_password > 1);
	if(!o.quiet && multiple_sections) {
		std::cout << '\n';
	}
	
	if(o.list_languages) {
		if(o.silent) {
			BOOST_FOREACH(const setup::language_entry & language, info.languages) {
				std::cout << language.name <<' ' << language.language_name << '\n';
			}
		} else {
			if(multiple_sections) {
				std::cout << "Languages:\n";
			}
			BOOST_FOREACH(const setup::language_entry & language, info.languages) {
				std::cout << " - " << color::green << language.name << color::reset;
				if(!language.language_name.empty()) {
					std::cout << ": " << color::white << language.language_name << color::reset;
				}
				std::cout << '\n';
			}
			if(info.languages.empty()) {
				std::cout << " (none)\n";
			}
		}
		if((o.silent || !o.quiet) && multiple_sections) {
			std::cout << '\n';
		}
	}
	
	if(o.gog_game_id) {
		std::string id = gog::get_game_id(info);
		if(id.empty()) {
			if(!o.quiet) {
				std::cout << "No GOG.com game ID found!\n";
			}
		} else if(!o.silent) {
			std::cout << "GOG.com game ID is " << color::cyan << id << color::reset << '\n';
		} else {
			std::cout << id << '\n';
		}
		if((o.silent || !o.quiet) && multiple_sections) {
			std::cout << '\n';
		}
	}
	
	if(o.show_password) {
		if(info.header.options & setup::header::Password) {
			if(o.silent) {
				std::cout << info.header.password << '\n';
			} else {
				std::cout << "Password hash: " << color::yellow << info.header.password << color::reset << '\n';
			}
			if(o.silent) {
				std::cout << print_hex(info.header.password_salt) << '\n';
			} else if(!info.header.password_salt.empty()) {
				std::cout << "Password salt: " << color::yellow
				          << print_hex(info.header.password_salt) << color::reset;
				if(!o.quiet) {
					if(info.header.password.type == crypto::PBKDF2_SHA256_XChaCha20) {
						std::cout << " (PBKDF2 salt, iteration count and XChaCha base nonce)";
					} else {
						std::cout << " (hex bytes, prepended to password)";
					}
				}
				std::cout << '\n';
			}
			if(o.silent) {
				std::cout << util::encoding_name(info.codepage) << '\n';
			} else {
				std::cout << "Password encoding: " << color::yellow
				          << util::encoding_name(info.codepage) << color::reset << '\n';
			}
		} else if(!o.quiet) {
			std::cout << "Setup is not passworded!\n";
		}
		if((o.silent || !o.quiet) && multiple_sections) {
			std::cout << '\n';
		}
	}
	
	return multiple_sections;
}

struct processed_entries {
	
	FilesMap files;
	
	DirectoriesMap directories;
	
};

processed_entries filter_entries(const extract_options & o, const setup::info & info) {
	
	processed_entries processed;
	
	#if BOOST_VERSION >= 105000
	processed.files.reserve(info.files.size());
	#endif
	
	#if BOOST_VERSION >= 104800
	processed.directories.reserve(info.directories.size()
	                              + size_t(std::log(double(info.files.size()))));
	#endif
	
	CollisionMap collisions;
	
	path_filter includes(o);
	
	// Filter the directories to be created
	BOOST_FOREACH(const setup::directory_entry & directory, info.directories) {
		
		if(!o.extract_temp && (directory.options & setup::directory_entry::DeleteAfterInstall)) {
			continue; // Ignore temporary dirs
		}
		
		if(!directory.languages.empty()) {
			if(!o.language.empty() && !setup::expression_match(o.language, directory.languages)) {
				continue; // Ignore other languages
			}
		} else if(o.language_only) {
			continue; // Ignore language-agnostic dirs
		}
		
		std::string path = o.filenames.convert(directory.name);
		if(path.empty()) {
			continue; // Don't know what to do with this
		}
		std::string internal_path = boost::algorithm::to_lower_copy(path);
		
		bool path_included = includes.match(internal_path);
		
		insert_dirs(processed.directories, includes, internal_path, path, path_included);
		
		DirectoriesMap::iterator it;
		if(path_included) {
			std::pair<DirectoriesMap::iterator, bool> existing = processed.directories.insert(
				std::make_pair(internal_path, processed_directory(path))
			);
			it = existing.first;
		} else {
			it = processed.directories.find(internal_path);
			if(it == processed.directories.end()) {
				continue;
			}
		}
		
		it->second.set_entry(&directory);
	}
	
	// Filter the files to be extracted
	BOOST_FOREACH(const setup::file_entry & file, info.files) {
		
		if(file.location >= info.data_entries.size()) {
			continue; // Ignore external files (copy commands)
		}
		
		if(!o.extract_temp && (file.options & setup::file_entry::DeleteAfterInstall)) {
			continue; // Ignore temporary files
		}
		
		if(!file.languages.empty()) {
			if(!o.language.empty() && !setup::expression_match(o.language, file.languages)) {
				continue; // Ignore other languages
			}
		} else if(o.language_only) {
			continue; // Ignore language-agnostic files
		}
		
		std::string path = o.filenames.convert(file.destination);
		if(path.empty()) {
			continue; // Internal file, not extracted
		}
		std::string internal_path = boost::algorithm::to_lower_copy(path);
		
		bool path_included = includes.match(internal_path);
		
		insert_dirs(processed.directories, includes, internal_path, path, path_included);
		
		if(!path_included) {
			continue; // Ignore excluded file
		}
		
		std::pair<FilesMap::iterator, bool> insertion = processed.files.insert(std::make_pair(
			internal_path, processed_file(&file, path)
		));
		
		if(!insertion.second) {
			// Collision!
			processed_file & existing = insertion.first->second;
			
			if(o.collisions == ErrorOnCollisions) {
				throw std::runtime_error("Collision: " + path);
			} else if(o.collisions == RenameAllCollisions) {
				collisions[internal_path].push_back(processed_file(&file, path));
			} else {
				
				const setup::data_entry & newdata = info.data_entries[file.location];
				const setup::data_entry & olddata = info.data_entries[existing.entry().location];
				const char * skip = handle_collision(existing.entry(), olddata, file, newdata);
				
				if(!o.default_language.empty()) {
					bool oldlang = setup::expression_match(o.default_language, file.languages);
					bool newlang = setup::expression_match(o.default_language, existing.entry().languages);
					if(oldlang && !newlang) {
						skip = NULL;
					} else if(!oldlang && newlang) {
						skip = "overwritten";
					}
				}
				
				if(o.collisions == RenameCollisions) {
					const setup::file_entry & clobberedfile = skip ? file : existing.entry();
					const std::string & clobberedpath = skip ? path : existing.path();
					collisions[internal_path].push_back(processed_file(&clobberedfile, clobberedpath));
				} else if(!o.silent) {
					std::cout << " - ";
					const std::string & clobberedpath = skip ? path : existing.path();
					std::cout << '"' << color::dim_yellow << clobberedpath << color::reset << '"';
					print_filter_info(skip ? file : existing.entry());
					if(o.list_sizes) {
						print_size_info(skip ? newdata.file : olddata.file, skip ? file.size : existing.entry().size);
					}
					if(o.list_checksums) {
						std::cout << ' ';
						print_checksum_info(skip ? newdata.file : olddata.file,
						                    skip ? &file.checksum : &existing.entry().checksum);
					}
					std::cout << " - " << (skip ? skip : "overwritten") << '\n';
				}
				
				if(!skip) {
					existing.set_entry(&file);
					if(file.type != setup::file_entry::UninstExe) {
						// Old file is "deleted" first → use case from new file
						existing.set_path(path);
					}
				}
				
			}
			
		}
		
	}
	
	if(o.collisions == RenameCollisions || o.collisions == RenameAllCollisions) {
		rename_collisions(o, processed.files, collisions);
	}
	
	return processed;
}

void create_output_directory(const extract_options & o) {
	
	try {
		if(!o.output_dir.empty() && !fs::exists(o.output_dir)) {
			fs::create_directory(o.output_dir);
		}
	} catch(...) {
		throw std::runtime_error("Could not create output directory \"" + o.output_dir.string() + '"');
	}
	
}

} // anonymous namespace

void process_file(const fs::path & installer, const extract_options & o) {
	
	bool is_directory;
	try {
		is_directory = fs::is_directory(installer);
	} catch(...) {
		throw std::runtime_error("Could not open file \"" + installer.string()
		                         + "\": access denied");
	}
	if(is_directory) {
		throw std::runtime_error("Input file \"" + installer.string() + "\" is a directory!");
	}
	
	util::ifstream ifs;
	try {
		ifs.open(installer, std::ios_base::in | std::ios_base::binary);
		if(!ifs.is_open()) {
			throw std::exception();
		}
	} catch(...) {
		throw std::runtime_error("Could not open file \"" + installer.string() + '"');
	}
	
	loader::offsets offsets;
	offsets.load(ifs);
	
	#ifdef DEBUG
	if(logger::debug) {
		print_offsets(offsets);
		std::cout << '\n';
	}
	#endif
	
	if(o.data_version)  {
		setup::version version;
		ifs.seekg(offsets.header_offset);
		version.load(ifs);
		if(o.silent) {
			std::cout << version << '\n';
		} else {
			std::cout << color::white << version << color::reset << '\n';
		}
		return;
	}
	
	#ifdef DEBUG
	if(o.dump_headers)  {
		create_output_directory(o);
		dump_headers(ifs, offsets, o);
		return;
	}
	#endif
	
	setup::info::entry_types entries = 0;
	if(o.list || o.test || o.extract || (o.gog_galaxy && o.list_languages)) {
		entries |= setup::info::Files;
		entries |= setup::info::Directories;
		entries |= setup::info::DataEntries;
	}
	if(o.list_languages) {
		entries |= setup::info::Languages;
	}
	if(o.gog_game_id || o.gog) {
		entries |= setup::info::RegistryEntries;
	}
	if(!o.extract_unknown) {
		entries |= setup::info::NoUnknownVersion;
	}
#ifdef DEBUG
	if(logger::debug) {
		entries = setup::info::entry_types::all();
	}
#endif
	
	ifs.seekg(offsets.header_offset);
	setup::info info;
	try {
		info.load(ifs, entries, o.codepage);
	} catch(const setup::version_error &) {
		fs::path headerfile = installer;
		headerfile.replace_extension(".0");
		if(offsets.header_offset == 0 && headerfile != installer && fs::exists(headerfile)) {
			log_info << "Opening \"" << color::cyan << headerfile.string() << color::reset << '"';
			process_file(headerfile, o);
			return;
		}
		if(offsets.found_magic) {
			if(offsets.header_offset == 0) {
				throw format_error("Could not determine location of setup headers!");
			} else {
				throw format_error("Could not determine setup data version!");
			}
		}
		throw;
	} catch(const std::exception & e) {
		std::ostringstream oss;
		oss << "Stream error while parsing setup headers!\n";
		oss << " ├─ detected setup version: " << info.version << '\n';
		oss << " └─ error reason: " << e.what();
		throw format_error(oss.str());
	}
	
	if(o.gog_galaxy && (o.list || o.test || o.extract || o.list_languages)) {
		gog::parse_galaxy_files(info, o.gog);
	}
	
	bool multiple_sections = print_file_info(o, info);
	
	std::string key;
	if(o.password.empty()) {
		if(!o.quiet && (o.list || o.test || o.extract) && (info.header.options & setup::header::EncryptionUsed)) {
			log_warning << "Setup contains encrypted files, use the --password option to extract them";
		}
	} else {
		key = info.get_key(o.password);
		if((info.header.options & setup::header::Password) && !info.check_key(key)) {
			if(o.check_password) {
				throw std::runtime_error("Incorrect password provided");
			}
			log_error << "Incorrect password provided";
			key.clear();
		}
		#if !INNOEXTRACT_HAVE_DECRYPTION
		if((o.extract || o.test) && (info.header.options & setup::header::EncryptionUsed)) {
			log_warning << "Decryption not supported in this build, skipping compressed chunks";
		}
		key.clear();
		#endif
	}
	
	if(!o.list && !o.test && !o.extract) {
		return;
	}
	
	if(!o.silent && multiple_sections) {
		std::cout << "Files:\n";
	}
	
	processed_entries processed = filter_entries(o, info);
	
	if(o.extract) {
		create_output_directory(o);
	}
	
	if(o.list || o.extract) {
		
		BOOST_FOREACH(const DirectoriesMap::value_type & i, processed.directories) {
			
			const std::string & path = i.second.path();
			
			if(o.list && !i.second.implied()) {
				
				if(!o.silent) {
					
					std::cout << " - ";
					std::cout << '"' << color::dim_white << path << setup::path_sep << color::reset << '"';
					if(i.second.has_entry()) {
						print_filter_info(i.second.entry());
					}
					std::cout << '\n';
					
				} else {
					std::cout << color::dim_white << path << setup::path_sep << color::reset << '\n';
				}
				
			}
			
			if(o.extract) {
				fs::path dir = o.output_dir / path;
				try {
					fs::create_directory(dir);
				} catch(...) {
					throw std::runtime_error("Could not create directory \"" + dir.string() + '"');
				}
			}
			
		}
		
	}
	
	typedef std::pair<const processed_file *, boost::uint64_t> output_location;
	std::vector< std::vector<output_location> > files_for_location;
	files_for_location.resize(info.data_entries.size());
	BOOST_FOREACH(const FilesMap::value_type & i, processed.files) {
		const processed_file & file = i.second;
		files_for_location[file.entry().location].push_back(output_location(&file, 0));
		if(o.test || o.extract) {
			boost::uint64_t offset = info.data_entries[file.entry().location].uncompressed_size;
			boost::uint32_t sort_slice = info.data_entries[file.entry().location].chunk.first_slice;
			boost::uint32_t sort_offset = info.data_entries[file.entry().location].chunk.sort_offset;
			BOOST_FOREACH(boost::uint32_t location, file.entry().additional_locations) {
				setup::data_entry & data = info.data_entries[location];
				files_for_location[location].push_back(output_location(&file, offset));
				offset += data.uncompressed_size;
				if(data.chunk.first_slice > sort_slice ||
				   (data.chunk.first_slice == sort_slice && data.chunk.sort_offset > sort_offset)) {
					sort_slice = data.chunk.first_slice;
					sort_offset = data.chunk.sort_offset;
				} else if(data.chunk.first_slice == sort_slice && data.chunk.sort_offset == data.chunk.offset) {
					data.chunk.sort_offset = ++sort_offset;
				} else {
					// Could not reorder chunk - no point in trying to reordder the remaining chunks
					sort_slice = boost::uint32_t(-1);
				}
			}
		}
	}
	
	boost::uint64_t total_size = 0;
	
	typedef std::map<stream::file, size_t> Files;
	typedef std::map<stream::chunk, Files> Chunks;
	Chunks chunks;
	for(size_t i = 0; i < info.data_entries.size(); i++) {
		if(!files_for_location[i].empty()) {
			setup::data_entry & location = info.data_entries[i];
			chunks[location.chunk][location.file] = i;
			total_size += location.uncompressed_size;
		}
	}
	
	boost::scoped_ptr<stream::slice_reader> slice_reader;
	if(o.extract || o.test) {
		if(offsets.data_offset) {
			slice_reader.reset(new stream::slice_reader(&ifs, offsets.data_offset));
		} else {
			fs::path dir = installer.parent_path();
			std::string basename = util::as_string(installer.stem());
			std::string basename2 = info.header.base_filename;
			// Prevent access to unexpected files
			std::replace(basename2.begin(), basename2.end(), '/', '_');
			std::replace(basename2.begin(), basename2.end(), '\\', '_');
			// Older Inno Setup versions used the basename stored in the headers, change our default accordingly
			if(info.version < INNO_VERSION(4, 1, 7) && !basename2.empty()) {
				std::swap(basename2, basename);
			}
			slice_reader.reset(new stream::slice_reader(dir, basename, basename2, info.header.slices_per_disk));
		}
	}
	
	progress extract_progress(total_size);
	
	typedef boost::ptr_map<const processed_file *, file_output> multi_part_outputs;
	multi_part_outputs multi_outputs;
	
	BOOST_FOREACH(const Chunks::value_type & chunk, chunks) {
		
		debug("[starting " << chunk.first.compression << " chunk @ slice " << chunk.first.first_slice
		      << " + " << print_hex(offsets.data_offset) << " + " << print_hex(chunk.first.offset)
		      << ']');
		
		stream::chunk_reader::pointer chunk_source;
		if((o.extract || o.test) && (chunk.first.encryption == stream::Plaintext || !key.empty())) {
			chunk_source = stream::chunk_reader::get(*slice_reader, chunk.first, key);
		}
		boost::uint64_t offset = 0;
		
		BOOST_FOREACH(const Files::value_type & location, chunk.second) {
			const stream::file & file = location.first;
			const std::vector<output_location> & output_locations = files_for_location[location.second];
			
			if(file.offset > offset) {
				debug("discarding " << print_bytes(file.offset - offset)
				      << " @ " << print_hex(offset));
				if(chunk_source.get()) {
					util::discard(*chunk_source, file.offset - offset);
				}
			}
			
			// Print filename and size
			if(o.list) {
				
				extract_progress.clear(DeferredClear);
				
				if(!o.silent) {
					
					bool named = false;
					boost::uint64_t size = 0;
					const crypto::checksum * checksum = NULL;
					BOOST_FOREACH(const output_location & output, output_locations) {
						if(output.second != 0) {
							continue;
						}
						bool mismatch = false;
						if(output.first->entry().size != 0) {
							if(size != 0 && size != output.first->entry().size) {
								mismatch = true;
							}
							size = output.first->entry().size;
						}
						if(output.first->entry().checksum.type != crypto::None) {
							if(checksum && *checksum != output.first->entry().checksum) {
								mismatch = true;
							}
							checksum = &output.first->entry().checksum;
						}
						if(mismatch) {
							// Different file even though the starting location is the same
							if(named) {
								print_file_details(o, file, chunk.first, size, checksum, key);
								named = false;
							}
						}
						if(named) {
							std::cout << ", ";
						} else {
							std::cout << " - ";
							named = true;
						}
						if(chunk.first.encryption != stream::Plaintext) {
							if(key.empty()) {
								std::cout << '"' << color::dim_yellow << output.first->path() << color::reset << '"';
							} else {
								std::cout << '"' << color::yellow << output.first->path() << color::reset << '"';
							}
						} else {
							std::cout << '"' << color::white << output.first->path() << color::reset << '"';
						}
						print_filter_info(output.first->entry());
					}
					
					if(named) {
						print_file_details(o, file, chunk.first, size, checksum, key);
					}
					
				} else {
					BOOST_FOREACH(const output_location & output, output_locations) {
						if(output.second == 0) {
							const processed_file * fileinfo = output.first;
							if(o.list_sizes) {
								boost::uint64_t size = fileinfo->entry().size;
								std::cout << color::dim_cyan << (size != 0 ? size : file.size) << color::reset << ' ';
							}
							if(o.list_checksums) {
								print_checksum_info(file, &fileinfo->entry().checksum);
								std::cout << ' ';
							}
							std::cout << color::white << fileinfo->path() << color::reset << '\n';
						}
					}
				}
				
				bool updated = extract_progress.update(0, true);
				if(!updated && (o.extract || o.test)) {
					std::cout.flush();
				}
				
			}
			
			// Seek to the correct position within the chunk
			if(chunk_source.get() && file.offset < offset) {
				std::ostringstream oss;
				oss << "Bad offset while extracting files: file start (" << file.offset
				    << ") is before end of previous file (" << offset << ")!";
				throw format_error(oss.str());
			}
			offset = file.offset + file.size;
			
			if(!chunk_source.get()) {
				continue; // Not extracting/testing this file
			}
			
			crypto::checksum checksum;
			
			// Open input file
			stream::file_reader::pointer file_source;
			file_source = stream::file_reader::get(*chunk_source, file, &checksum);
			
			// Open output files
			boost::ptr_vector<file_output> single_outputs;
			typedef std::pair<file_output *, boost::uint64_t> file_output_location;
			std::vector<file_output_location> outputs;
			BOOST_FOREACH(const output_location & output_loc, output_locations) {
				const processed_file * fileinfo = output_loc.first;
				try {
					
					if(!o.extract && fileinfo->entry().checksum.type == crypto::None) {
						continue;
					}
					
					// Re-use existing file output for multi-part files
					file_output * output = NULL;
					if(fileinfo->is_multipart()) {
						multi_part_outputs::iterator it = multi_outputs.find(fileinfo);
						if(it != multi_outputs.end()) {
							output = it->second;
						}
					}
					
					if(!output) {
						output = new file_output(o.output_dir, fileinfo, o.extract);
						if(fileinfo->is_multipart()) {
							multi_outputs.insert(fileinfo, output);
						} else {
							single_outputs.push_back(output);
						}
					}
					
					outputs.push_back(file_output_location(output, output_loc.second));
					
				} catch(boost::bad_pointer &) {
					// should never happen
					std::terminate();
				}
			}
			
			// Copy data
			boost::uint64_t output_size = 0;
			while(!file_source->eof()) {
				char buffer[8192 * 10];
				std::streamsize buffer_size = std::streamsize(boost::size(buffer));
				std::streamsize n = file_source->read(buffer, buffer_size).gcount();
				if(n > 0) {
					BOOST_FOREACH(file_output_location & out, outputs) {
						file_output * output = out.first;
						output->seek(out.second + output_size);
						bool success = output->write(buffer, size_t(n));
						if(!success) {
							throw std::runtime_error("Error writing file \"" + output->path().string() + '"');
						}
					}
					extract_progress.update(boost::uint64_t(n));
					output_size += boost::uint64_t(n);
				}
			}
			
			const setup::data_entry & data = info.data_entries[location.second];
			
			if(output_size != data.uncompressed_size) {
				log_warning << "Unexpected output file size: " << output_size << " != " << data.uncompressed_size;
			}
			
			util::time filetime = data.timestamp;
			if(o.extract && o.preserve_file_times && o.local_timestamps && !(data.options & data.TimeStampInUTC)) {
				filetime = util::to_local_time(filetime);
			}
			
			BOOST_FOREACH(file_output_location & out, outputs) {
				file_output * output = out.first;
				
				if(!output || (output->file()->is_multipart() && !output->is_complete())) {
					continue;
				}
				
				// Verify output checksum if available
				if(output->file()->entry().checksum.type != crypto::None && output->calculate_checksum()) {
					crypto::checksum output_checksum = output->checksum();
					if(output_checksum != output->file()->entry().checksum) {
						log_warning << "Output checksum mismatch for " << output->file()->path() << ":\n"
						            << " ├─ actual:   " << output_checksum << '\n'
						            << " └─ expected: " << output->file()->entry().checksum;
						if(o.test) {
							throw std::runtime_error("Integrity test failed!");
						}
					}
				}
				
				// Adjust file timestamps
				if(o.extract && o.preserve_file_times) {
					output->close();
					if(!util::set_file_time(output->path(), filetime, data.timestamp_nsec)) {
						log_warning << "Error setting timestamp on file " << output->path();
					}
				}
				
				BOOST_FOREACH(file_output_location & other, outputs) {
					if(other.first == output) {
						other.first = NULL;
					}
				}
				
				if(output->file()->is_multipart()) {
					debug("[finalizing multi-part file]");
					multi_outputs.erase(output->file());
				}
				
			}
			
			// Verify checksums
			if(checksum != file.checksum) {
				log_warning << "Checksum mismatch:\n"
				            << " ├─ actual:   " << checksum << '\n'
				            << " └─ expected: " << file.checksum;
				if(o.test) {
					throw std::runtime_error("Integrity test failed!");
				}
			}
			
		}
		
		#ifdef DEBUG
		if(offset < chunk.first.size) {
			debug("discarding " << print_bytes(chunk.first.size - offset)
			      << " at end of chunk @ " << print_hex(offset));
		}
		#endif
	}
	
	extract_progress.clear();
	
	if(!multi_outputs.empty()) {
		log_warning << "Incomplete multi-part files";
	}
	
	if(o.warn_unused || o.gog) {
		gog::probe_bin_files(o, info, installer, offsets.data_offset == 0);
	}
	
}
```

## File: `src/cli/extract.hpp`
```
/*
 * Copyright (C) 2014-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Routines to extract/list files from an Inno Setup archive.
 */
#ifndef INNOEXTRACT_CLI_EXTRACT_HPP
#define INNOEXTRACT_CLI_EXTRACT_HPP

#include <stdexcept>
#include <string>
#include <vector>

#include <boost/cstdint.hpp>
#include <boost/filesystem/path.hpp>

#include "setup/filename.hpp"

struct format_error : public std::runtime_error {
	explicit format_error(const std::string & reason) : std::runtime_error(reason) { }
};

enum CollisionAction {
	OverwriteCollisions,
	RenameCollisions,
	RenameAllCollisions,
	ErrorOnCollisions
};

struct extract_options {
	
	bool quiet;
	bool silent;
	
	bool warn_unused; //!< Warn if there are unused files
	
	bool list_sizes; //!< Show size information for files
	bool list_checksums; //!< Show checksum information for files
	
	bool data_version; //!< Print the data version
	#ifdef DEBUG
	bool dump_headers; //!< Dump setup headers
	#endif
	bool list; //!< List files
	bool test; //!< Test files (but don't extract)
	bool extract; //!< Extract files
	bool list_languages; //!< List available languages
	bool gog_game_id; //!< Show the GOG.com game id
	bool show_password; //!< Show password check information
	bool check_password; //!< Abort if the provided password is incorrect
	
	bool preserve_file_times; //!< Set timestamps of extracted files
	bool local_timestamps; //!< Use local timezone for setting timestamps
	
	bool gog; //!< Try to extract additional archives used in GOG.com installers
	bool gog_galaxy; //!< Try to re-assemble GOG Galaxy files
	
	bool extract_unknown; //!< Try to extract unknown Inno Setup versions
	
	bool extract_temp; //!< Extract temporary files
	bool language_only; //!< Extract files not associated with any language
	std::string language; //!< Extract only files for this language
	std::vector<std::string> include; //!< Extract only files matching these patterns
	
	boost::uint32_t codepage;
	
	setup::filename_map filenames;
	CollisionAction collisions;
	std::string default_language;
	
	std::string password;
	
	boost::filesystem::path output_dir;
	
	extract_options()
		: quiet(false)
		, silent(false)
		, warn_unused(false)
		, list_sizes(false)
		, list_checksums(false)
		, data_version(false)
		, list(false)
		, test(false)
		, extract(false)
		, list_languages(false)
		, gog_game_id(false)
		, show_password(false)
		, check_password(false)
		, preserve_file_times(false)
		, local_timestamps(false)
		, gog(false)
		, gog_galaxy(false)
		, extract_unknown(false)
		, extract_temp(false)
		, language_only(false)
		, collisions(OverwriteCollisions)
	{ }
	
};

void process_file(const boost::filesystem::path & installer, const extract_options & o);

#endif // INNOEXTRACT_CLI_EXTRACT_HPP
```

## File: `src/cli/gog.cpp`
```cpp
/*
 * Copyright (C) 2014-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "cli/gog.hpp"

#include <stddef.h>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <signal.h>

#include <boost/cstdint.hpp>
#include <boost/foreach.hpp>
#include <boost/noncopyable.hpp>
#include <boost/algorithm/string/predicate.hpp>
#include <boost/filesystem/operations.hpp>

#include "cli/extract.hpp"

#include "crypto/md5.hpp"

#include "loader/offsets.hpp"

#include "setup/data.hpp"
#include "setup/info.hpp"
#include "setup/registry.hpp"

#include "stream/slice.hpp"

#include "util/boostfs_compat.hpp"
#include "util/console.hpp"
#include "util/encoding.hpp"
#include "util/fstream.hpp"
#include "util/log.hpp"
#include "util/process.hpp"

namespace fs = boost::filesystem;

namespace gog {

std::string get_game_id(const setup::info & info) {
	
	std::string id;
	
	const char * prefix = "SOFTWARE\\GOG.com\\Games\\";
	size_t prefix_length = std::strlen(prefix);
	
	BOOST_FOREACH(const setup::registry_entry & entry, info.registry_entries) {
		
		if(!boost::istarts_with(entry.key, prefix)) {
			continue;
		}
		
		if(entry.key.find('\\', prefix_length) != std::string::npos) {
			continue;
		}
		
		if(boost::iequals(entry.name, "gameID")) {
			id = entry.value;
			util::to_utf8(id, info.codepage);
			break;
		}
		
		if(id.empty()) {
			id = entry.key.substr(prefix_length);
		}
		
	}
	
	return id;
}

namespace {

std::string get_verb(const extract_options & o) {
	const char * verb = "inspect";
	if(o.extract) {
		verb = "extract";
	} else if(o.test) {
		verb = "test";
	} else if(o.list) {
		verb = "list the contents of";
	}
	return verb;
}

volatile sig_atomic_t quit_requested = 0;
void quit_handler(int /* ignored */) {
	quit_requested = 1;
}

bool process_file_unrar(const std::string & file, const extract_options & o, const std::string & password) {
	
	std::vector<const char *> args;
	args.push_back("unrar");
	
	if(o.extract) {
		args.push_back("x");
	} else if(o.test) {
		args.push_back("t");
	} else if(o.silent) {
		args.push_back("lb");
	} else {
		args.push_back("l");
	}
	
	args.push_back("-p-");
	std::string pwarg;
	if(!password.empty()) {
		pwarg = "-p" + password;
		args.push_back(pwarg.c_str());
	}
	
	args.push_back("-idc"); // Disable copyright header
	
	if(!progress::is_enabled()) {
		args.push_back("-idp"); // Disable progress display
	}
	
	if(o.filenames.is_lowercase()) {
		args.push_back("-cl"); // Connvert filenames to lowercase
	}
	
	if(!o.list) {
		args.push_back("-idq"); // Disable file list
	}
	
	args.push_back("-o+"); // Overwrite existing files
	
	if(o.preserve_file_times) {
		args.push_back("-tsmca"); // Restore file times
	} else {
		args.push_back("-tsm0c0a0"); // Don't restore file times
	}
	
	args.push_back("-y"); // Enable batch mode
	
	args.push_back("--");
	
	args.push_back(file.c_str());
	
	std::string dir = o.output_dir.string();
	if(!dir.empty()) {
		if(dir[dir.length() - 1] != '/' && dir[dir.length() - 1] != '\\') {
			#if defined(_WIN32)
			dir += '\\';
			#else
			dir += '/';
			#endif
		}
		args.push_back(dir.c_str());
	}
	
	args.push_back(NULL);
	
	int ret = util::run(&args.front());
	if(ret < 0 && !quit_requested) {
		args[0] = "rar";
		ret = util::run(&args.front());
		if(ret < 0 && !quit_requested) {
			return false;
		}
	}
	
	if(ret > 0) {
		throw std::runtime_error("Could not " + get_verb(o) + " \"" + file + "\": unrar failed");
	}
	
	return true;
}

bool process_file_unar(const std::string & file, const extract_options & o, const std::string & password) {
	
	std::string dir = o.output_dir.string();
	
	std::vector<const char *> args;
	if(o.extract) {
		args.push_back("unar");
		
		args.push_back("-f"); // Overwrite existing files
		
		args.push_back("-D"); // Don't create directory
		
		if(!dir.empty()) {
			args.push_back("-o");
			args.push_back(dir.c_str());
		}
		
		if(!o.list) {
			args.push_back("-q"); // Disable file list
		}
		
	} else {
		args.push_back("lsar");
		
		if(o.test) {
			args.push_back("-t");
		}
	}
	
	if(!password.empty()) {
		args.push_back("-p");
		args.push_back(password.c_str());
	}
	
	args.push_back("--");
	
	args.push_back(file.c_str());
	
	args.push_back(NULL);
	
	int ret = util::run(&args.front());
	if(ret < 0 && !quit_requested) {
		return false;
	}
	
	if(ret > 0) {
		throw std::runtime_error("Could not " + get_verb(o) + " \"" + file + "\": unar failed");
	}
	
	return true;
}

bool process_rar_file(const std::string & file, const extract_options & o, const std::string & password) {
	return process_file_unrar(file, o, password) || process_file_unar(file, o, password);
}

char hex_char(int c) {
	if(c < 10) {
		return char('0' + c);
	} else {
		return char('a' + (c - 10));
	}
}

class temporary_directory : private boost::noncopyable {
	
	fs::path parent;
	fs::path path;
	
public:
	
	explicit temporary_directory(const fs::path & base) {
		try {
			if(!base.empty() && !fs::exists(base)) {
				fs::create_directory(base);
				parent = base;
			}
			size_t tmpnum = 0;
			std::ostringstream oss;
			do {
				oss.str(std::string());
				oss << "innoextract-tmp-" << tmpnum++;
				path = base / oss.str();
			} while(fs::exists(path));
			fs::create_directory(path);
		} catch(...) {
			path = fs::path();
			throw std::runtime_error("Could not create temporary directory!");
		}
	}
	
	~temporary_directory() {
		if(!path.empty()) {
			try {
				fs::remove_all(path);
				if(!parent.empty()) {
					fs::remove(parent);
				}
			} catch(...) {
				log_error << "Could not remove temporary directory " << path << '!';
			}
		}
	}
	
	const fs::path & get() { return path; }
	
};

void process_rar_files(const std::vector<fs::path> & files,
                       const extract_options & o, const setup::info & info) {
	
	if((!o.list && !o.test && !o.extract) || files.empty()) {
		return;
	}
	
	// Calculate password from the GOG.com game ID
	std::string password = get_game_id(info);
	if(!password.empty()) {
		crypto::md5 md5;
		md5.init();
		md5.update(password.c_str(), password.length());
		char hash[16];
		md5.finalize(hash);
		password.resize(size_t(boost::size(hash) * 2));
		for(size_t i = 0; i < size_t(boost::size(hash)); i++) {
			password[2 * i + 0] = hex_char(boost::uint8_t(hash[i]) / 16);
			password[2 * i + 1] = hex_char(boost::uint8_t(hash[i]) % 16);
		}
	}
	
	if((!o.extract && !o.test && o.list) || files.size() == 1) {
		
		// When listing contents or for single-file archives, pass the bin file to unrar
		
		bool ok = true;
		BOOST_FOREACH(const fs::path & file, files) {
			if(!process_rar_file(file.string(), o, password)) {
				ok = false;
			}
		}
		
		if(ok) {
			return;
		}
		
	} else {
		
		/*
		 * When extracting multi-part archives we need to create symlinks with special
		 * names so that unrar will find all the parts of the archive.
		 */
		
		typedef void(*signal_handler /* … */)(int /* … */);
		#ifdef SIGINT
		signal_handler old_sigint_handler = signal(SIGINT, quit_handler);
		#endif
		#ifdef SIGTERM
		signal_handler old_sigterm_handler = signal(SIGTERM, quit_handler);
		#endif
		#ifdef SIGHUP
		signal_handler old_sighup_handler = signal(SIGHUP, quit_handler);
		#endif
		
		temporary_directory tmpdir(o.output_dir);
		
		fs::path first_file;
		try {
			
			fs::path here = fs::current_path();
			
			std::string basename = util::as_string(files.front().stem());
			if(boost::ends_with(basename, "-1")) {
				basename.resize(basename.length() - 2);
			}
			
			size_t i = 0;
			std::ostringstream oss;
			BOOST_FOREACH(const fs::path & file, files) {
				
				oss.str(std::string());
				oss << basename << ".r" << std::setfill('0') << std::setw(2) << i;
				fs::path symlink = tmpdir.get() / oss.str();
				
				if(file.root_path().empty()) {
					fs::create_symlink(here / file, symlink);
				} else {
					fs::create_symlink(file, symlink);
				}
				
				if(i == 0) {
					first_file = symlink;
				}
				
				i++;
			}
			
		} catch(...) {
			throw std::runtime_error("Could not " + get_verb(o)
			                         + " \"" + files.front().string()
			                         + "\": unable to create .r?? symlinks");
		}
		
		if(process_rar_file(first_file.string(), o, password)) {
			return;
		}
		
		#ifdef SIGHUP
		signal(SIGHUP, old_sighup_handler);
		#endif
		#ifdef SIGTERM
		signal(SIGTERM, old_sigterm_handler);
		#endif
		#ifdef SIGINT
		signal(SIGINT, old_sigint_handler);
		#endif
		if(quit_requested) {
			throw std::runtime_error("Aborted!");
		}
		
	}
	
	throw std::runtime_error("Could not " + get_verb(o) + " \"" + files.front().string()
	                         + "\": install `unrar` or `unar`");
}

void process_bin_files(const std::vector<fs::path> & files, const extract_options & o,
                      const setup::info & info) {
	
	util::ifstream ifs(files.front(), std::ios_base::in | std::ios_base::binary);
	if(!ifs.is_open()) {
		throw std::runtime_error("Could not open file \"" + files.front().string() + '"');
	}
	
	char magic[4];
	if(!ifs.read(magic, std::streamsize(boost::size(magic))).fail()) {
		
		if(std::memcmp(magic, "Rar!", 4) == 0) {
			ifs.close();
			process_rar_files(files, o, info);
			return;
		}
		
		if(std::memcmp(magic, "MZ", 2) == 0) {
			loader::offsets offsets;
			offsets.load(ifs);
			if(offsets.header_offset != 0) {
				ifs.close();
				extract_options new_options = o;
				new_options.gog = false;
				new_options.warn_unused = false;
				std::cout << '\n';
				process_file(files.front(), new_options);
				return;
			}
		}
		
	}
	
	throw std::runtime_error("Could not " + get_verb(o) + " \"" + files.front().string()
	                         + "\": unknown filetype");
}

size_t probe_bin_file_series(const extract_options & o, const setup::info & info, const fs::path & dir,
                             const std::string & basename, size_t format = 0, size_t start = 0) {
	
	size_t count = 0;
	
	std::vector<fs::path> files;
	
	for(size_t i = start;; i++) {
		
		fs::path file;
		if(format == 0) {
			file = dir / basename;
		} else {
			file = dir / stream::slice_reader::slice_filename(basename, i, format);
		}
		
		try {
			if(!fs::is_regular_file(file)) {
				break;
			}
		} catch(...) {
			break;
		}
		
		if(o.gog) {
			files.push_back(file);
		} else {
			log_warning << file.filename() << " is not part of the installer!";
			count++;
		}
		
		if(format == 0) {
			break;
		}
		
	}
	
	if(!files.empty()) {
		process_bin_files(files, o, info);
	}
	
	return count;
}

} // anonymous namespace

void probe_bin_files(const extract_options & o, const setup::info & info,
                     const fs::path & setup_file, bool external) {
	
	boost::filesystem::path dir = setup_file.parent_path();
	std::string basename = util::as_string(setup_file.stem());
	
	size_t bin_count = 0;
	bin_count += probe_bin_file_series(o, info, dir, basename + ".bin");
	bin_count += probe_bin_file_series(o, info, dir, basename + "-0" + ".bin");
	

	boost::uint32_t max_slice = 0;
	if(external) {
		BOOST_FOREACH(const setup::data_entry & location, info.data_entries) {
			max_slice = std::max(max_slice, location.chunk.first_slice);
			max_slice = std::max(max_slice, location.chunk.last_slice);
		}
	}
	
	size_t slice =  0;
	size_t format = 1;
	if(external && info.header.slices_per_disk == 1) {
		slice = size_t(max_slice) + 1;
	}
	bin_count += probe_bin_file_series(o, info, dir, basename, format, slice);
	
	slice = 0;
	format = 2;
	if(external && info.header.slices_per_disk != 1) {
		slice = size_t(max_slice) + 1;
		format = info.header.slices_per_disk;
	}
	bin_count += probe_bin_file_series(o, info, dir, basename, format, slice);
	
	if(bin_count) {
		const char * verb = "inspecting";
		if(o.extract) {
			verb = "extracting";
		} else if(o.test) {
			verb = "testing";
		} else if(o.list) {
			verb = "listing the contents of";
		}
		std::cerr << color::yellow << "Use the --gog option to try " << verb << " "
		          << (bin_count > 1 ? "these files" : "this file") << ".\n" << color::reset;
	}
	
}

} // namespace gog
```

## File: `src/cli/gog.hpp`
```
/*
 * Copyright (C) 2014-2018 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * GOG.com-specific extensions.
 */
#ifndef INNOEXTRACT_CLI_GOG_HPP
#define INNOEXTRACT_CLI_GOG_HPP

#include <string>
#include <vector>

#include <boost/filesystem/path.hpp>

namespace setup { struct info; }

struct extract_options;

namespace gog {

//! \return the GOG.com game ID for this installer or an empty string
std::string get_game_id(const setup::info & info);

void probe_bin_files(const extract_options & o, const setup::info & info,
                     const boost::filesystem::path & setup_file, bool external);

} // namespace gog

#endif // INNOEXTRACT_CLI_GOG_HPP
```

## File: `src/cli/goggalaxy.cpp`
```cpp
/*
 * Copyright (C) 2018-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "cli/goggalaxy.hpp"

#include <set>
#include <string>
#include <vector>

#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string/predicate.hpp>
#include <boost/algorithm/string/trim.hpp>

#include "crypto/checksum.hpp"

#include "setup/data.hpp"
#include "setup/file.hpp"
#include "setup/info.hpp"
#include "setup/language.hpp"

#include "util/log.hpp"

namespace gog {

namespace {

std::vector<std::string> parse_function_call(const std::string & code, const std::string & name) {
	
	std::vector<std::string> arguments;
	if(code.empty()) {
		return arguments;
	}
	
	const char whitespace[] = " \t\r\n";
	const char separator[] = " \t\r\n(),'";
	
	size_t start = code.find_first_not_of(whitespace);
	if(start == std::string::npos) {
		return arguments;
	}
	
	size_t end = code.find_first_of(separator, start);
	if(end == std::string::npos) {
		return arguments;
	}
	
	size_t parenthesis = code.find_first_not_of(whitespace, end);
	if(parenthesis == std::string::npos || code[parenthesis] != '(') {
		return arguments;
	}
	
	if(end - start != name.length() || code.compare(start, end - start, name) != 0) {
		return arguments;
	}
	
	size_t p = parenthesis + 1;
	while(true) {
		
		p = code.find_first_not_of(whitespace, p);
		if(p == std::string::npos) {
			log_warning << "Error parsing function call: " << code;
			return arguments;
		}
		
		arguments.resize(arguments.size() + 1);
		
		if(code[p] == '\'') {
			p++;
			while(true) {
				size_t string_end = code.find('\'', p);
				arguments.back() += code.substr(p, string_end - p);
				if(string_end == std::string::npos || string_end + 1 == code.size()) {
					log_warning << "Error parsing function call: " << code;
					return arguments;
				}
				p = string_end + 1;
				if(code[p] == '\'') {
					arguments.back() += '\'';
					p++;
				} else {
					break;
				}
			}
		} else {
			size_t token_end = code.find_first_of(separator, p);
			arguments.back() = code.substr(p, token_end - p);
			if(token_end == std::string::npos || token_end == code.size()) {
				log_warning << "Error parsing function call: " << code;
				return arguments;
			}
			p = token_end;
		}
		
		p = code.find_first_not_of(whitespace, p);
		if(p == std::string::npos) {
			log_warning << "Error parsing function call: " << code;
			return arguments;
		}
		
		if(code[p] == ')') {
			break;
		} else if(code[p] == ',') {
			p++;
		} else {
			log_warning << "Error parsing function call: " << code;
			return arguments;
		}
		
	}
	
	p++;
	if(p != code.size()) {
		p = code.find_first_not_of(whitespace, p);
		if(p != std::string::npos) {
			if(code[p] != ';' || code.find_first_not_of(whitespace, p + 1) != std::string::npos) {
				log_warning << "Error parsing function call: " << code;
			}
		}
	}
	
	return arguments;
}

int parse_hex(char c) {
	if(c >= '0' && c <= '9') {
		return c - '0';
	} else if(c >= 'a' && c <= 'f') {
		return c - 'a' + 10;
	} else if(c >= 'A' && c <= 'F') {
		return c - 'a' + 10;
	} else {
		return -1;
	}
}

crypto::checksum parse_checksum(const std::string & string) {
	
	crypto::checksum checksum;
	checksum.type = crypto::MD5;
	
	if(string.length() != 32) {
		// Unknown checksum type
		checksum.type = crypto::None;
		return checksum;
	}
	
	for(size_t i = 0; i < 16; i++) {
		int a = parse_hex(string[2 * i]);
		int b = parse_hex(string[2 * i + 1]);
		if(a < 0 || b < 0) {
			checksum.type = crypto::None;
			break;
		}
		checksum.md5[i] = char((a << 4) | b);
	}
	
	return checksum;
}

struct constraint {
	
	std::string name;
	bool negated;
	
	explicit constraint(const std::string & constraint_name, bool is_negated = false)
		: name(constraint_name), negated(is_negated) { }
	
};

std::vector<constraint> parse_constraints(const std::string & input) {
	
	std::vector<constraint> result;
	
	size_t start = 0;
	
	while(start < input.length()) {
		
		start = input.find_first_not_of(" \t\r\n", start);
		if(start == std::string::npos) {
			break;
		}
		
		bool negated = false;
		if(input[start] == '!') {
			negated = true;
			start++;
		}
		
		size_t end = input.find('#', start);
		if(end == std::string::npos) {
			end = input.length();
		}
		
		if(end != start) {
			std::string token = input.substr(start, end - start);
			boost::trim(token);
			result.push_back(constraint(token, negated));
		}
		
		if(end == std::string::npos) {
			end = input.length();
		}
		
		start = end + 1;
	}
	
	return result;
}

std::string create_constraint_expression(std::vector<constraint> & constraints) {
	
	std::string result;
	
	BOOST_FOREACH(const constraint & entry, constraints) {
		
		if(!result.empty()) {
			result += " or ";
		}
		
		if(entry.negated) {
			result += " not ";
		}
		
		result += entry.name;
		
	}
	
	return result;
}

} // anonymous namespace

void parse_galaxy_files(setup::info & info, bool force) {
	
	if(!force) {
		bool is_gog = boost::icontains(info.header.app_publisher, "GOG.com");
		is_gog = is_gog || boost::icontains(info.header.app_publisher_url, "www.gog.com");
		is_gog = is_gog || boost::icontains(info.header.app_support_url, "www.gog.com");
		is_gog = is_gog || boost::icontains(info.header.app_updates_url, "www.gog.com");
		if(!is_gog) {
			return;
		}
	}
	
	setup::file_entry * file_start = NULL;
	size_t remaining_parts = 0;
	
	bool has_language_constraints = false;
	std::set<std::string> all_languages;
	
	BOOST_FOREACH(setup::file_entry & file, info.files) {
		
		// Multi-part file info: file checksum, filename, part count
		std::vector<std::string> start_info = parse_function_call(file.before_install, "before_install");
		if(start_info.empty()) {
			start_info = parse_function_call(file.before_install, "before_install_dependency");
		}
		if(!start_info.empty()) {
			
			if(remaining_parts != 0) {
				log_warning << "Incomplete GOG Galaxy file " << file_start->destination;
				remaining_parts = 0;
			}
			
			// Recover the original filename - parts are named after the MD5 hash of their contents
			if(start_info.size() >= 2 && !start_info[1].empty()) {
				file.destination = start_info[1];
			}
			
			file.checksum = parse_checksum(start_info[0]);
			file.size = 0;
			if(file.checksum.type == crypto::None) {
				log_warning << "Could not parse checksum for GOG Galaxy file " << file.destination
				            << ": " << start_info[0];
			}
			
			if(start_info.size() < 3) {
				log_warning << "Missing part count for GOG Galaxy file " << file.destination;
				remaining_parts = 1;
			} else {
				try {
					remaining_parts = boost::lexical_cast<size_t>(start_info[2]);
					if(remaining_parts == 0) {
						remaining_parts = 1;
					}
					file_start = &file;
				} catch(...) {
					log_warning << "Could not parse part count for GOG Galaxy file " << file.destination
					            << ": " << start_info[2];
				}
			}
			
		}
		
		// File part ifo: part checksum, compressed part size, uncompressed part size
		std::vector<std::string> part_info = parse_function_call(file.after_install, "after_install");
		if(part_info.empty()) {
			part_info = parse_function_call(file.after_install, "after_install_dependency");
		}
		if(!part_info.empty()) {
			if(remaining_parts == 0) {
				log_warning << "Missing file start for GOG Galaxy file part " << file.destination;
			} else if(file.location > info.data_entries.size()) {
				log_warning << "Invalid data location for GOG Galaxy file part " << file.destination;
				remaining_parts = 0;
			} else if(part_info.size() < 3) {
				log_warning << "Missing size for GOG Galaxy file part " << file.destination;
				remaining_parts = 0;
			} else {
				
				remaining_parts--;
				
				setup::data_entry & data = info.data_entries[file.location];
				
				// Ignore file part MD5 checksum, setup already contains a better one for the deflated data
				
				try {
					boost::uint64_t compressed_size = boost::lexical_cast<boost::uint64_t>(part_info[1]);
					if(data.file.size != compressed_size) {
						log_warning << "Unexpected compressed size for GOG Galaxy file part " << file.destination
						            << ": " << compressed_size << " != " << data.file.size;
					}
				} catch(...) {
					log_warning << "Could not parse compressed size for GOG Galaxy file part " << file.destination
					            << ": " << part_info[1];
				}
				
				try {
					
					// GOG Galaxy file parts are deflated, inflate them while extracting
					data.uncompressed_size = boost::lexical_cast<boost::uint64_t>(part_info[2]);
					data.file.filter = stream::ZlibFilter;
					
					file_start->size += data.uncompressed_size;
					
					if(&file != file_start) {
						
						// Ignore this file entry and instead add the data location to the start file
						file.destination.clear();
						file_start->additional_locations.push_back(file.location);
						
						if(file.components != file_start->components || file.tasks != file_start->tasks
						   || file.languages != file_start->languages || file.check != file_start->check
						   || file.options != file_start->options) {
							log_warning << "Mismatched constraints for different parts of GOG Galaxy file "
							            << file_start->destination << ": " << file.destination;
						}
						
					}
					
				} catch(...) {
					log_warning << "Could not parse size for GOG Galaxy file part " << file.destination
					            << ": " << part_info[1];
					remaining_parts = 0;
				}
				
			}
		} else if(!start_info.empty()) {
			log_warning << "Missing part info for GOG Galaxy file " << file.destination;
			remaining_parts = 0;
		} else if(remaining_parts != 0) {
			log_warning << "Incomplete GOG Galaxy file " << file_start->destination;
			remaining_parts = 0;
		}
		
		if(!file.destination.empty()) {
			// languages, architectures, winversions
			std::vector<std::string> check = parse_function_call(file.check, "check_if_install");
			if(!check.empty() && !check[0].empty()) {
				std::vector<constraint> languages = parse_constraints(check[0]);
				BOOST_FOREACH(const constraint & language, languages) {
					all_languages.insert(language.name);
				}
			}
		}
		
		has_language_constraints = has_language_constraints || !file.languages.empty();
		
	}
	
	if(remaining_parts != 0) {
		log_warning << "Incomplete GOG Galaxy file " << file_start->destination;
	}
	
	/*
	 * GOG Galaxy multi-part files also have their own constraints, convert these to standard
	 * Inno Setup ones.
	 *
	 * Do this in a separate loop to not break constraint checks above.
	 */
	
	BOOST_FOREACH(setup::file_entry & file, info.files) {
		
		if(file.destination.empty()) {
			continue;
		}
		
		// languages, architectures, winversions
		std::vector<std::string> check = parse_function_call(file.check, "check_if_install");
		if(!check.empty()) {
			
			if(!check[0].empty()) {
				
				std::vector<constraint> languages = parse_constraints(check[0]);
				
				// Ignore constraints that just contain all languages
				bool has_all_languages = false;
				if(languages.size() >= all_languages.size() && all_languages.size() > 1) {
					has_all_languages = true;
					BOOST_FOREACH(const std::string & known_language, all_languages) {
						bool has_language = false;
						BOOST_FOREACH(const constraint & language, languages) {
							if(!language.negated && language.name == known_language) {
								has_language = true;
								break;
							}
						}
						if(!has_language) {
							has_all_languages = false;
							break;
						}
					}
				}
				
				if(!languages.empty() && !has_all_languages) {
					if(!file.languages.empty()) {
						log_warning << "Overwriting language constraints for GOG Galaxy file " << file.destination;
					}
					file.languages = create_constraint_expression(languages);
				}
				
			}
			
			if(check.size() >= 2 && !check[1].empty()) {
				const setup::file_entry::flags all_arch = setup::file_entry::Bits32 | setup::file_entry::Bits64;
				setup::file_entry::flags arch = 0;
				if(check[1] != "32#64#") {
					std::vector<constraint> architectures = parse_constraints(check[1]);
					BOOST_FOREACH(const constraint & architecture, architectures) {
						if(architecture.negated && architectures.size() > 1) {
							log_warning << "Ignoring architecture for GOG Galaxy file " << file.destination
							            << ": !" << architecture.name;
						} else if(architecture.name == "32") {
							arch |= setup::file_entry::Bits32;
						} else if(architecture.name == "64") {
							arch |= setup::file_entry::Bits64;
						} else {
							log_warning << "Unknown architecture for GOG Galaxy file " << file.destination
							            << ": " << architecture.name;
						}
						if(architecture.negated && architectures.size() <= 1) {
							arch = all_arch & ~arch;
						}
					}
					if(arch == all_arch) {
						arch = 0;
					}
				}
				if((file.options & all_arch) && (file.options & all_arch) != arch) {
					log_warning << "Overwriting architecture constraints for GOG Galaxy file " << file.destination;
				}
				file.options = (file.options & ~all_arch) | arch;
			}
			
			if(check.size() >= 3 && !check[2].empty()) {
				log_warning << "Ignoring OS constraint for GOG Galaxy file " << file.destination
				            << ": " << check[2];
			}
			
			if(file.components.empty()) {
				file.components = "game";
			}
			
		}
		
		// component id, ?
		std::vector<std::string> dependency = parse_function_call(file.check, "check_if_install_dependency");
		if(!dependency.empty()) {
			if(file.components.empty() && !dependency[0].empty()) {
				file.components = dependency[0];
			}
		}
		
	}
	
	if(!all_languages.empty()) {
		if(!has_language_constraints) {
			info.languages.clear();
		}
		info.languages.reserve(all_languages.size());
		BOOST_FOREACH(const std::string & name, all_languages) {
			setup::language_entry language;
			language.name = name;
			language.dialog_font_size = 0;
			language.dialog_font_standard_height = 0;
			language.title_font_size = 0;
			language.welcome_font_size = 0;
			language.copyright_font_size = 0;
			language.right_to_left = false;
			info.languages.push_back(language);
		}
	}
	
}

} // namespace gog
```

## File: `src/cli/goggalaxy.hpp`
```
/*
 * Copyright (C) 2018 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * GOG.com-specific extensions.
 */
#ifndef INNOEXTRACT_CLI_GOGGALAXY_HPP
#define INNOEXTRACT_CLI_GOGGALAXY_HPP

namespace setup { struct info; }

namespace gog {

/*!
 * For some GOG installers, some application files are shipped in GOG Galaxy format:
 * Thse files are split into one or more parts and then individually compressed.
 * The parts are decompressed and reassembled by pre-/post-install scripts.
 * This function parses the arguments to those scripts so that we can re-assemble them ourselves.
 *
 * The first part of a multi-part file has a before_install script that configures the output filename
 * as well as the number of parts in the file and a checksum for the whole file.
 *
 * Each part (including the first) has an after_install script with a checksum for the decompressed
 * part as well as compressed and decompressed sizes.
 *
 * Additionally, language constrained are also parsed from check scripts and added to the language list.
 */
void parse_galaxy_files(setup::info & info, bool force);

} // namespace gog

#endif // INNOEXTRACT_CLI_GOGGALAXY_HPP

```

## File: `src/cli/main.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

#include <boost/foreach.hpp>
#include <boost/program_options.hpp>
#include <boost/algorithm/string/predicate.hpp>
#include <boost/filesystem/path.hpp>
#include <boost/filesystem/operations.hpp>

#include "release.hpp"

#include "cli/extract.hpp"

#include "setup/version.hpp"

#include "util/console.hpp"
#include "util/fstream.hpp"
#include "util/log.hpp"
#include "util/time.hpp"
#include "util/windows.hpp"

namespace fs = boost::filesystem;
namespace po = boost::program_options;

enum ExitValues {
	ExitSuccess = 0,
	ExitUserError = 1,
	ExitDataError = 2
};

static const char * get_command(const char * argv0) {
	
	if(!argv0) {
		argv0 = innoextract_name;
	}
	std::string var = argv0;
	
#ifdef _WIN32
	size_t pos = var.find_last_of("/\\");
#else
	size_t pos = var.find_last_of('/');
#endif
	if(pos != std::string::npos) {
		var = var.substr(pos + 1);
	}
	
	var += "_COMMAND";
	
	const char * env = std::getenv(var.c_str());
	if(env) {
		return env;
	} else {
		return argv0;
	}
}

static void print_version(const extract_options & o) {
	if(o.silent) {
		std::cout << innoextract_version << '\n';
		return;
	}
	std::cout << color::white << innoextract_name
	          << ' ' << innoextract_version << color::reset
#ifdef DEBUG
	          << " (with debug output)"
#endif
	          << '\n';
	if(!o.quiet) {
		std::cout << "Extracts installers created by " << color::cyan
		          << innosetup_versions << color::reset << '\n';
	}
}

static void print_help(const char * name, const po::options_description & visible) {
	std::cout << color::white << "Usage: " << name << " [options] <setup file(s)>\n\n"
	          << color::reset;
	std::cout << "Extract files from an Inno Setup installer.\n";
	std::cout << "For multi-part installers only specify the exe file.\n";
	std::cout << visible << '\n';
	std::cout << "Extracts installers created by " << color::cyan
	          << innosetup_versions << color::reset << '\n';
	std::cout << '\n';
	std::cout << color::white << innoextract_name
	          << ' ' << innoextract_version << color::reset
	          << ' ' << innoextract_copyright << '\n';
	std::cout << "This is free software with absolutely no warranty.\n";
}

static void print_license() {
	
	std::cout << color::white << innoextract_name
	          << ' ' << innoextract_version << color::reset
	          << ' ' << innoextract_copyright << '\n';
	std::cout << '\n'<< innoextract_license << '\n';
	;
}

int main(int argc, char * argv[]) {
	
	po::options_description generic("Generic options");
	generic.add_options()
		("help,h", "Show supported options")
		("version,v", "Print version information")
		("license", "Show license information")
	;
	
	po::options_description action("Actions");
	action.add_options()
		("test,t", "Only verify checksums, don't write anything")
		("extract,e", "Extract files (default action)")
		("list,l", "Only list files, don't write anything")
		("list-sizes", "List file sizes")
		("list-checksums", "List file checksums")
		("info,i", "Print information about the installer")
		("list-languages", "List languages supported by the installer")
		("gog-game-id", "Determine the installer's GOG.com game ID")
		("show-password", "Show password check information")
		("check-password", "Abort if the password is incorrect")
		("data-version,V", "Only print the data version")
		#ifdef DEBUG
		("dump-headers", "Dump decompressed setup headers")
		#endif
	;
	
	po::options_description modifiers("Modifiers");
	modifiers.add_options()
		("codepage", po::value<boost::uint32_t>(), "Encoding for ANSI strings")
		("collisions", po::value<std::string>(), "How to handle duplicate files")
		("default-language", po::value<std::string>(), "Default language for renaming")
		("dump", "Dump contents without converting filenames")
		("lowercase,L", "Convert extracted filenames to lower-case")
		("timestamps,T", po::value<std::string>(), "Timezone for file times or \"local\" or \"none\"")
		("output-dir,d", po::value<std::string>(), "Extract files into the given directory")
		("password,P", po::value<std::string>(), "Password for encrypted files")
		("password-file", po::value<std::string>(), "File to load password from")
		("gog,g", "Extract additional archives from GOG.com installers")
		("no-gog-galaxy", "Don't re-assemble GOG Galaxy file parts")
		("no-extract-unknown,n", "Don't extract unknown Inno Setup versions")
	;
	
	po::options_description filter("Filters");
	filter.add_options()
		("exclude-temp,m", "Don't extract temporary files")
		("language", po::value<std::string>(), "Extract only files for this language")
		("language-only", "Only extract language-specific files")
		("include,I", po::value< std::vector<std::string> >(), "Extract only files that match this path")
	;
	
	po::options_description io("Display options");
	io.add_options()
		("quiet,q", "Output less information")
		("silent,s", "Output only error/warning information")
		("no-warn-unused", "Don't warn on unused .bin files")
		("color,c", po::value<bool>()->implicit_value(true), "Enable/disable color output")
		("progress,p", po::value<bool>()->implicit_value(true), "Enable/disable the progress bar")
		#ifdef DEBUG
		("debug", "Output debug information")
		#endif
	;
	
	po::options_description hidden("Hidden options");
	hidden.add_options()
		("setup-files", po::value< std::vector<std::string> >(), "Setup files to be extracted")
		/**/;
	
	po::options_description options_desc;
	options_desc.add(generic).add(action).add(modifiers).add(filter).add(io).add(hidden);
	
	po::options_description visible;
	visible.add(generic).add(action).add(modifiers).add(filter).add(io);
	
	po::positional_options_description p;
	p.add("setup-files", -1);
	
	po::variables_map options;
	
	// Parse the command-line.
	try {
		po::store(po::command_line_parser(argc, argv).options(options_desc).positional(p).run(),
		          options);
		po::notify(options);
	} catch(std::exception & e) {
		color::init(color::disable, color::disable); // Be conservative
		std::cerr << "Error parsing command-line: " << e.what() << "\n\n";
		print_help(get_command(argv[0]), visible);
		return ExitUserError;
	}
	
	::extract_options o;
	
	// Verbosity settings.
	o.silent = (options.count("silent") != 0);
	o.quiet = o.silent || options.count("quiet");
	logger::quiet = o.quiet;
#ifdef DEBUG
	if(options.count("debug")) {
		logger::debug = true;
	}
#endif
	
	o.warn_unused = (options.count("no-warn-unused") == 0);
	
	// Color / progress bar settings.
	color::is_enabled color_e;
	po::variables_map::const_iterator color_i = options.find("color");
	if(color_i == options.end()) {
		color_e = o.silent ? color::disable : color::automatic;
	} else {
		color_e = color_i->second.as<bool>() ? color::enable : color::disable;
	}
	color::is_enabled progress_e;
	po::variables_map::const_iterator progress_i = options.find("progress");
	if(progress_i == options.end()) {
		progress_e = o.silent ? color::disable : color::automatic;
	} else {
		progress_e = progress_i->second.as<bool>() ? color::enable : color::disable;
	}
	color::init(color_e, progress_e);
	
	// Help output.
	if(options.count("help") != 0) {
		print_help(get_command(argv[0]), visible);
		return ExitSuccess;
	}
	
	// License output
	if(options.count("license") != 0) {
		print_license();
		return ExitSuccess;
	}
	
	// Main action.
	o.list_sizes = (options.count("list-sizes") != 0);
	o.list_checksums = (options.count("list-checksums") != 0);
	bool explicit_list = (options.count("list") != 0);
	o.list = explicit_list || o.list_sizes || o.list_checksums;
	o.extract = (options.count("extract") != 0);
	o.test = (options.count("test") != 0);
	o.list_languages = (options.count("list-languages") != 0);
	o.gog_game_id = (options.count("gog-game-id") != 0);
	o.show_password = (options.count("show-password") != 0);
	o.check_password = (options.count("check-password") != 0);
	if(options.count("info") != 0) {
		o.list_languages = true;
		o.gog_game_id = true;
		o.show_password = true;
	}
	bool explicit_action = o.list || o.test || o.extract || o.list_languages
	                       || o.gog_game_id || o.show_password || o.check_password;
	if(!explicit_action) {
		o.extract = true;
	}
	if(!o.extract && !o.test) {
		progress::set_enabled(false);
	}
	if(!o.silent && (o.test || o.extract)) {
		o.list = true;
	}
	if(!o.quiet && explicit_list) {
		o.list_sizes = true;
	}
	
	// Additional actions.
	o.filenames.set_expand(options.count("dump") == 0);
	o.filenames.set_lowercase(options.count("lowercase") != 0);
	
	// File timestamps
	{
		o.preserve_file_times = true, o.local_timestamps = false;
		po::variables_map::const_iterator i = options.find("timestamps");
		if(i != options.end()) {
			std::string timezone_name = i->second.as<std::string>();
			if(boost::iequals(timezone_name, "none")) {
				o.preserve_file_times = false;
			} else if(!boost::iequals(timezone_name, "UTC")) {
				o.local_timestamps = true;
				if(!boost::iequals(timezone_name, "local")) {
					util::set_local_timezone(timezone_name);
				}
			}
		}
	}
	
	// List version.
	if(options.count("version") != 0) {
		print_version(o);
		if(!explicit_action) {
			return ExitSuccess;
		}
	}
	
	{
		po::variables_map::const_iterator i = options.find("codepage");
		o.codepage = (i != options.end()) ? i->second.as<boost::uint32_t>() : 0;
	}
	{
		o.collisions = OverwriteCollisions;
		po::variables_map::const_iterator i = options.find("collisions");
		if(i != options.end()) {
			std::string collisions = i->second.as<std::string>();
			if(collisions == "overwrite")  {
				o.collisions = OverwriteCollisions;
			} else if(collisions == "rename") {
				o.collisions = RenameCollisions;
			} else if(collisions == "rename-all") {
				o.collisions = RenameAllCollisions;
			} else if(collisions == "error") {
				o.collisions = ErrorOnCollisions;
			} else {
				log_error << "Unsupported --collisions value: " << collisions;
				return ExitUserError;
			}
		}
	}
	{
		po::variables_map::const_iterator i = options.find("default-language");
		if(i != options.end()) {
			o.default_language = i->second.as<std::string>();
		}
	}
	
	o.extract_temp = (options.count("exclude-temp") == 0);
	{
		po::variables_map::const_iterator i = options.find("language");
		if(i != options.end()) {
			o.language = i->second.as<std::string>();
		}
		o.language_only = (options.count("language-only") != 0);
	}
	{
		po::variables_map::const_iterator i = options.find("include");
		if(i != options.end()) {
			o.include = i->second.as<std::vector <std::string> >();
		}
	}
	
	if(options.count("setup-files") == 0) {
		if(!o.silent) {
			std::cout << get_command(argv[0]) << ": no input files specified\n";
			std::cout << "Try the --help (-h) option for usage information.\n";
		}
		return ExitSuccess;
	}
	
	{
		po::variables_map::const_iterator i = options.find("output-dir");
		if(i != options.end()) {
			/*
			 * We can't use fs::path directly with boost::program_options as fs::path's
			 * operator>> expects paths to be quoted if they contain spaces, breaking
			 * lexical casts.
			 * Instead, do the conversion in the assignment operator.
			 * See https://svn.boost.org/trac/boost/ticket/8535
			 */
			o.output_dir = i->second.as<std::string>();
		}
	}
	
	{
		po::variables_map::const_iterator password = options.find("password");
		po::variables_map::const_iterator password_file = options.find("password-file");
		if(password != options.end() && password_file != options.end()) {
			log_error << "Combining --password and --password-file is not allowed";
			return ExitUserError;
		}
		if(password != options.end()) {
			o.password = password->second.as<std::string>();
		}
		if(password_file != options.end()) {
			std::istream * is = &std::cin;
			fs::path file = password_file->second.as<std::string>();
			util::ifstream ifs;
			if(file != "-") {
				ifs.open(file);
				if(!ifs.is_open()) {
					log_error << "Could not open password file " << file;
					return ExitDataError;
				}
				is = &ifs;
			}
			std::getline(*is, o.password);
			if(!o.password.empty() && o.password[o.password.size() - 1] == '\n') {
				o.password.resize(o.password.size() - 1);
			}
			if(!o.password.empty() && o.password[o.password.size() - 1] == '\r') {
				o.password.resize(o.password.size() - 1);
			}
			if(!*is) {
				log_error << "Could not read password file " << file;
				return ExitDataError;
			}
		}
		if(o.check_password && o.password.empty()) {
			log_error << "Combining --check-password requires a password";
			return ExitUserError;
		}
	}
	
	o.gog = (options.count("gog") != 0);
	o.gog_galaxy = (options.count("no-gog-galaxy") == 0);
	
	o.data_version = (options.count("data-version") != 0);
	if(o.data_version) {
		logger::quiet = true;
		if(explicit_action) {
			log_error << "Combining --data-version with other options is not allowed";
			return ExitUserError;
		}
	}
	
	#ifdef DEBUG
	o.dump_headers = (options.count("dump-headers") != 0);
	if(o.dump_headers) {
		if(explicit_action || o.data_version) {
			log_error << "Combining --dump-headers with other options is not allowed";
			return ExitUserError;
		}
	}
	#endif
	
	o.extract_unknown = (options.count("no-extract-unknown") == 0);
	
	const std::vector<std::string> & files = options["setup-files"]
	                                         .as< std::vector<std::string> >();
	
	bool suggest_bug_report = false;
	try {
		BOOST_FOREACH(const std::string & file, files) {
			process_file(file, o);
			if(!o.data_version && files.size() > 1) {
				std::cout << '\n';
			}
		}
	} catch(const std::ios_base::failure & e) {
		log_error << "Stream error while extracting files!\n"
		          << " └─ error reason: " << e.what();
		suggest_bug_report = true;
	} catch(const format_error & e) {
		log_error << e.what();
		suggest_bug_report = true;
	} catch(const std::runtime_error & e) {
		log_error << e.what();
	} catch(const setup::version_error &) {
		log_error << "Not a supported Inno Setup installer!";
	}
	
	if(suggest_bug_report) {
		std::cerr << color::blue << "If you are sure the setup file is not corrupted,"
		          << " consider \nfiling a bug report at "
		          << color::dim_cyan << innoextract_bugs << color::reset << '\n';
	}
	
	if(!logger::quiet || logger::total_errors || logger::total_warnings) {
		progress::clear();
		std::ostream & os = logger::quiet ? std::cerr : std::cout;
		os << color::green << "Done" << color::reset << std::dec;
		if(logger::total_errors || logger::total_warnings) {
			os << " with ";
			if(logger::total_errors) {
				os << color::red << logger::total_errors
				   << ((logger::total_errors == 1) ? " error" : " errors")
				   << color::reset;
			}
			if(logger::total_errors && logger::total_warnings) {
				os << " and ";
			}
			if(logger::total_warnings) {
				os << color::yellow << logger::total_warnings
				   << ((logger::total_warnings == 1) ? " warning" : " warnings")
				   << color::reset;
			}
		}
		os << '.' << std::endl;
	}
	
	return logger::total_errors == 0 ? ExitSuccess : ExitDataError;
}
```

## File: `src/crypto/adler32.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

// Taken from Crypto++ and modified to fit the project.
// adler32.cpp - written and placed in the public domain by Wei Dai

#include "crypto/adler32.hpp"

#include "util/test.hpp"

namespace crypto {

void adler32::update(const char * data, size_t length) {
	
	const boost::uint_fast32_t base = 65521;
	
	boost::uint_fast32_t s1 = boost::uint16_t(state);
	boost::uint_fast32_t s2 = boost::uint16_t(state >> 16);
	
	if(length % 8 != 0) {
		
		do {
			s1 += boost::uint8_t(*data++);
			s2 += s1;
			length--;
		} while(length % 8 != 0);
		
		if(s1 >= base) {
			s1 -= base;
		}
		
		s2 %= base;
	}
	
	while(length > 0) {
		
		s1 += boost::uint8_t(data[0]), s2 += s1;
		s1 += boost::uint8_t(data[1]), s2 += s1;
		s1 += boost::uint8_t(data[2]), s2 += s1;
		s1 += boost::uint8_t(data[3]), s2 += s1;
		s1 += boost::uint8_t(data[4]), s2 += s1;
		s1 += boost::uint8_t(data[5]), s2 += s1;
		s1 += boost::uint8_t(data[6]), s2 += s1;
		s1 += boost::uint8_t(data[7]), s2 += s1;
		
		length -= 8;
		data += 8;
		
		if(s1 >= base) {
			s1 -= base;
		}
		
		if(length % 0x8000 == 0) {
			s2 %= base;
		}
	}
	
	state  = (boost::uint32_t(s2) << 16) | boost::uint16_t(s1);
	
}

INNOEXTRACT_TEST(adler32,
	
	adler32 checksum;
	checksum.init();
	checksum.update(testdata, testlen);
	test("checksum", checksum.finalize() == 0xb8a36c4a);
	
)

} // namespace crypto
```

## File: `src/crypto/adler32.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Adler-32 checksum routines.
 */
#ifndef INNOEXTRACT_CRYPTO_ADLER32_HPP
#define INNOEXTRACT_CRYPTO_ADLER32_HPP

#include <stddef.h>

#include <boost/cstdint.hpp>

#include "crypto/checksum.hpp"

namespace crypto {

//! Adler-32 checksum calculations
struct adler32 : public checksum_base<adler32> {
	
	void init() { state = 1; }
	
	void update(const char * data, size_t length);
	
	boost::uint32_t finalize() const { return state; }
	
private:
	
	boost::uint32_t state;
	
};

} // namespace crypto

#endif // INNOEXTRACT_CRYPTO_ADLER32_HPP
```

## File: `src/crypto/arc4.cpp`
```cpp
/*
 * Copyright (C) 2018 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "crypto/arc4.hpp"

#include <algorithm>

#include "util/endian.hpp"
#include "util/test.hpp"

namespace crypto {

void arc4::init(const char * key, size_t length) {
	
	a = b = 0;
	
	for(size_t i = 0; i < sizeof(state); i++){
		state[i] = boost::uint8_t(i);
	}
	
	size_t j = 0;
	for(size_t i = 0; i < sizeof(state); i++) {
		j = (j + state[i] + boost::uint8_t(key[i % length])) % sizeof(state);
		std::swap(state[i], state[j]);
	}
	
}

void arc4::update() {
	
	a = (a + 1) % sizeof(state);
	b = (b + state[a]) % sizeof(state);
	
	std::swap(state[a], state[b]);
	
}

void arc4::discard(size_t length) {
	
	for(size_t i = 0; i < length; i++) {
		update();
	}
	
}

void arc4::crypt(const char * in, char * out, size_t length) {
	
	for(size_t i = 0; i < length; i++) {
		update();
		out[i] = char(state[size_t(state[a] + state[b]) % sizeof(state)] ^ boost::uint8_t(in[i]));
	}
	
}

INNOEXTRACT_TEST(arc4,
	
	const boost::uint8_t key[] = {
		0x7f, 0xe5, 0x54, 0xd3, 0x47, 0x1e, 0xc7, 0xba, 0xb3, 0x37,
		0x4f, 0xfd, 0x46, 0xb3, 0x88, 0x85, 0x12, 0x2b, 0x13, 0x14
	};
	
	const boost::uint8_t ciphertext[] = {
		0x06, 0x58, 0x8c, 0x39, 0xf8, 0xc7, 0xf3, 0xbd, 0x17, 0x74, 0x7c, 0x84, 0xd1, 0xaf, 0x6c, 0xcf,
		0x51, 0x98, 0x8a, 0x32, 0xe5, 0x25, 0x4a, 0xae, 0x04, 0xda, 0x18, 0xa7, 0x02, 0xd7, 0xe5, 0x34,
		0x0a, 0x34, 0x3a, 0x7c, 0xc1, 0x9c, 0x9c, 0xb4, 0x07, 0xf6, 0x52, 0x31, 0x49, 0x21, 0x7f, 0xc2,
		0x9a, 0x18, 0x25, 0xa1, 0x86, 0x37, 0x9c, 0x47, 0x8b, 0x61, 0x72, 0x9c, 0x93, 0x8a, 0x72, 0xbd,
		0x99, 0xc9, 0xc4, 0x5f, 0x44, 0x28, 0xcf, 0x28, 0xe6, 0x9a, 0x0b, 0x2d, 0xad, 0x33, 0xf1, 0x8c,
		0x3b, 0x51, 0xa6, 0x72, 0x9c, 0x0a, 0x97, 0x73, 0xe6, 0x6d, 0xd1, 0xb6, 0xed, 0xb1, 0x2f, 0xb9,
		0x1c, 0x68, 0x7c, 0x64, 0xf4, 0x57, 0x54, 0xaa, 0x70, 0xb2, 0x2a, 0x6a, 0x7f, 0xa8, 0xac, 0x55,
		0x6e, 0xc2, 0x9c, 0x6f, 0x7f, 0xc6, 0x80, 0xb4, 0xe3, 0xf2, 0xe2, 0xfd, 0x4b, 0x0c, 0x46, 0x51,
		0xbf, 0xbd, 0xd2, 0x51, 0x93, 0x4d, 0x20, 0x22, 0x7e, 0xdb, 0x84, 0xbb, 0xd8, 0x3f, 0x6a, 0x91,
		0x72, 0x03, 0x3a, 0x4f, 0x0b, 0x91, 0xc8, 0xae, 0xb4, 0x27, 0xd9, 0xc7, 0x55, 0x27, 0x7f, 0xa6,
		0x5a, 0x73, 0xe6, 0xa1, 0x0f, 0x81, 0xe0, 0x51, 0xa1, 0x5c, 0xe8, 0xfd, 0x89, 0xa5, 0x55, 0xb5,
		0x7a, 0x67, 0xa9, 0x5d, 0x1b, 0xff, 0x0a, 0x3d, 0x34, 0xc1, 0x08, 0xe7, 0x06, 0xd6, 0x03, 0xb8,
		0x6f, 0x5e, 0xb8, 0x88, 0x4c, 0x66, 0x7a, 0xa4, 0x77, 0x0b, 0x03, 0x9c, 0xad, 0xef, 0x43, 0x5b,
		0xff, 0x23, 0x92, 0x2d, 0xf9, 0x84, 0x1d, 0xa6, 0x0a, 0x1e, 0x1f, 0xfe, 0x22, 0xaf, 0x6f, 0x87,
		0x95, 0xf7, 0x17, 0xaa, 0x49, 0xc4, 0x35, 0xb3, 0xdd, 0xcc, 0x8d, 0x76, 0x17, 0x93, 0xa3, 0xaa,
		0x7b, 0x02, 0x45, 0x9d, 0xb2, 0x65, 0xb7, 0x9f, 0x96, 0xd8, 0xbe, 0xd6, 0xef, 0x46, 0xdb, 0x94,
		0xb2, 0x15, 0xd6, 0x71, 0x26, 0x1e, 0xc8, 0xed, 0xd8, 0x0e, 0x18, 0xca, 0x23, 0xba, 0x78, 0x56,
		0x98, 0xec, 0x10, 0x6d, 0x5b, 0xdb, 0x7a, 0xcf, 0x43, 0x19, 0x68, 0x7f, 0xdd, 0xb0, 0x15, 0x42,
		0x50, 0xb3, 0x04, 0xc4, 0x6c, 0x11, 0x95, 0xed, 0xe8, 0x1c, 0xb6, 0xcd, 0x23, 0x3d, 0x5a, 0x0f
	};
	
	arc4 cipher;
	
	cipher.init(reinterpret_cast<const char *>(key), sizeof(key));
	char buffer0[sizeof(ciphertext)];
	cipher.crypt(testdata, buffer0, sizeof(ciphertext));
	test_equals("crypt", buffer0, ciphertext, sizeof(ciphertext));
	
	cipher.init(reinterpret_cast<const char *>(key), sizeof(key));
	cipher.crypt(testdata, buffer0, 3);
	cipher.discard(129);
	char buffer1[sizeof(ciphertext) - 132];
	cipher.crypt(testdata + 132, buffer1, sizeof(ciphertext) - 132);
	test_equals("discard", buffer1, ciphertext + 132, sizeof(ciphertext) - 132);
	
)

} // namespace crypto
```

## File: `src/crypto/arc4.hpp`
```
/*
 * Copyright (C) 2018 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Alledged RC4 en-/decryption routines.
 */
#ifndef INNOEXTRACT_CRYPTO_ARC4_HPP
#define INNOEXTRACT_CRYPTO_ARC4_HPP

#include <stddef.h>

#include <boost/cstdint.hpp>

#include "configure.hpp"

#if INNOEXTRACT_HAVE_DECRYPTION

namespace crypto {

//! Alledged RC4 en-/decryption calculation
struct arc4 {
	
	void init(const char * key, size_t length);
	
	void discard(size_t length);
	
	void crypt(const char * in, char * out, size_t length);
	
private:
	
	void update();
	
	boost::uint8_t state[256];
	size_t a, b;
	
};

} // namespace crypto

#endif // INNOEXTRACT_HAVE_DECRYPTION

#endif // INNOEXTRACT_CRYPTO_ARC4_HPP
```

## File: `src/crypto/checksum.cpp`
```cpp
/*
 * Copyright (C) 2011-2018 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "crypto/checksum.hpp"

#include <ios>
#include <cstring>
#include <ostream>
#include <iomanip>

#include <boost/range/size.hpp>

namespace crypto {

bool checksum::operator==(const checksum & other) const {
	
	if(other.type != type) {
		return false;
	}
	
	switch(type) {
		case None: return true;
		case Adler32: return (adler32 == other.adler32);
		case CRC32: return (crc32 == other.crc32);
		case MD5: return !memcmp(md5, other.md5, sizeof(md5));
		case SHA1: return !memcmp(sha1, other.sha1, sizeof(sha1));
		case SHA256: return !memcmp(sha256, other.sha256, sizeof(sha256));
		default: return false;
	};
}

} // namespace crypto

NAMES(crypto::checksum_type, "Checksum Type",
	"None",
	"Adler32",
	"CRC32",
	"MD5",
	"SHA-1",
	"SHA-256",
	"PBKDF2-SHA256+XChaCha20"
)

std::ostream & operator<<(std::ostream & os, const crypto::checksum & checksum) {
	
	std::ios_base::fmtflags old_fmtflags = os.flags();
	
	os << checksum.type << ' ';
	
	switch(checksum.type) {
		case crypto::None: {
			os << "(no checksum)";
			break;
		}
		case crypto::Adler32: {
			os << "0x" << std::hex << std::setw(8) << checksum.adler32;
			break;
		}
		case crypto::CRC32: {
			os << "0x" << std::hex << std::setw(8) << checksum.crc32;
			break;
		}
		case crypto::MD5: {
			for(size_t i = 0; i < size_t(boost::size(checksum.md5)); i++) {
				os << std::setfill('0') << std::hex << std::setw(2) << int(boost::uint8_t(checksum.md5[i]));
			}
			break;
		}
		case crypto::SHA1: {
			for(size_t i = 0; i < size_t(boost::size(checksum.sha1)); i++) {
				os << std::setfill('0') << std::hex << std::setw(2) << int(boost::uint8_t(checksum.sha1[i]));
			}
			break;
		}
		case crypto::SHA256: {
			for(size_t i = 0; i < size_t(boost::size(checksum.sha1)); i++) {
				os << std::setfill('0') << std::hex << std::setw(2) << int(boost::uint8_t(checksum.sha1[i]));
			}
			break;
		}
		case crypto::PBKDF2_SHA256_XChaCha20: {
			for(size_t i = 0; i < size_t(boost::size(checksum.check)); i++) {
				os << std::setfill('0') << std::hex << std::setw(2) << int(boost::uint8_t(checksum.check[i]));
			}
			break;
		}
	}
	
	os.setf(old_fmtflags, std::ios_base::basefield);
	
	return os;
}
```

## File: `src/crypto/checksum.hpp`
```
/*
 * Copyright (C) 2011-2018 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Checksum structures and utilities.
 */
#ifndef INNOEXTRACT_CRYPTO_CHECKSUM_HPP
#define INNOEXTRACT_CRYPTO_CHECKSUM_HPP

#include <cstring>
#include <iosfwd>
#include <istream>

#include <boost/cstdint.hpp>

#include "util/endian.hpp"
#include "util/enum.hpp"
#include "util/types.hpp"

namespace crypto {

enum checksum_type {
	None,
	Adler32,
	CRC32,
	MD5,
	SHA1,
	SHA256,
	PBKDF2_SHA256_XChaCha20
};

struct checksum {
	
	union {
		boost::uint32_t adler32;
		boost::uint32_t crc32;
		char md5[16];
		char sha1[20];
		char sha256[32];
		char check[4];
	};
	
	checksum_type type;
	
	bool operator==(const checksum & other) const;
	bool operator!=(const checksum & other) const { return !(*this == other); }
	
};

template <class Impl>
class checksum_base : public util::static_polymorphic<Impl> {
	
public:
	
	/*!
	 * Load the data and process it.
	 * Data is processed as-is and then converted according to Endianness.
	 */
	template <class T, class Endianness>
	T load(std::istream & is) {
		char buffer[sizeof(T)];
		is.read(buffer, std::streamsize(sizeof(buffer)));
		this->impl().update(buffer, sizeof(buffer));
		return Endianness::template load<T>(buffer);
	}
	
	/*!
	 * Load the data and process it.
	 * Data is processed as-is and then converted if the host endianness is not little_endian.
	 */
	template <class T>
	T load(std::istream & is) {
		return load<T, util::little_endian>(is);
	}
	
};

} // namespace crypto

NAMED_ENUM(crypto::checksum_type)

std::ostream & operator<<(std::ostream & os, const crypto::checksum & checksum);

#endif // INNOEXTRACT_CRYPTO_CHECKSUM_HPP
```

## File: `src/crypto/crc32.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

// Taken from Crypto++ and modified to fit the project.
// crc.cpp - written and placed in the public domain by Wei Dai

#include "crypto/crc32.hpp"

#include "util/endian.hpp"
#include "util/test.hpp"

namespace crypto {

/* Table of CRC-32's of all single byte values (made by makecrc.c) */
static const boost::uint32_t crc32_table[] = {
	0x00000000l, 0x77073096l, 0xee0e612cl, 0x990951bal, 0x076dc419l,
	0x706af48fl, 0xe963a535l, 0x9e6495a3l, 0x0edb8832l, 0x79dcb8a4l,
	0xe0d5e91el, 0x97d2d988l, 0x09b64c2bl, 0x7eb17cbdl, 0xe7b82d07l,
	0x90bf1d91l, 0x1db71064l, 0x6ab020f2l, 0xf3b97148l, 0x84be41del,
	0x1adad47dl, 0x6ddde4ebl, 0xf4d4b551l, 0x83d385c7l, 0x136c9856l,
	0x646ba8c0l, 0xfd62f97al, 0x8a65c9ecl, 0x14015c4fl, 0x63066cd9l,
	0xfa0f3d63l, 0x8d080df5l, 0x3b6e20c8l, 0x4c69105el, 0xd56041e4l,
	0xa2677172l, 0x3c03e4d1l, 0x4b04d447l, 0xd20d85fdl, 0xa50ab56bl,
	0x35b5a8fal, 0x42b2986cl, 0xdbbbc9d6l, 0xacbcf940l, 0x32d86ce3l,
	0x45df5c75l, 0xdcd60dcfl, 0xabd13d59l, 0x26d930acl, 0x51de003al,
	0xc8d75180l, 0xbfd06116l, 0x21b4f4b5l, 0x56b3c423l, 0xcfba9599l,
	0xb8bda50fl, 0x2802b89el, 0x5f058808l, 0xc60cd9b2l, 0xb10be924l,
	0x2f6f7c87l, 0x58684c11l, 0xc1611dabl, 0xb6662d3dl, 0x76dc4190l,
	0x01db7106l, 0x98d220bcl, 0xefd5102al, 0x71b18589l, 0x06b6b51fl,
	0x9fbfe4a5l, 0xe8b8d433l, 0x7807c9a2l, 0x0f00f934l, 0x9609a88el,
	0xe10e9818l, 0x7f6a0dbbl, 0x086d3d2dl, 0x91646c97l, 0xe6635c01l,
	0x6b6b51f4l, 0x1c6c6162l, 0x856530d8l, 0xf262004el, 0x6c0695edl,
	0x1b01a57bl, 0x8208f4c1l, 0xf50fc457l, 0x65b0d9c6l, 0x12b7e950l,
	0x8bbeb8eal, 0xfcb9887cl, 0x62dd1ddfl, 0x15da2d49l, 0x8cd37cf3l,
	0xfbd44c65l, 0x4db26158l, 0x3ab551cel, 0xa3bc0074l, 0xd4bb30e2l,
	0x4adfa541l, 0x3dd895d7l, 0xa4d1c46dl, 0xd3d6f4fbl, 0x4369e96al,
	0x346ed9fcl, 0xad678846l, 0xda60b8d0l, 0x44042d73l, 0x33031de5l,
	0xaa0a4c5fl, 0xdd0d7cc9l, 0x5005713cl, 0x270241aal, 0xbe0b1010l,
	0xc90c2086l, 0x5768b525l, 0x206f85b3l, 0xb966d409l, 0xce61e49fl,
	0x5edef90el, 0x29d9c998l, 0xb0d09822l, 0xc7d7a8b4l, 0x59b33d17l,
	0x2eb40d81l, 0xb7bd5c3bl, 0xc0ba6cadl, 0xedb88320l, 0x9abfb3b6l,
	0x03b6e20cl, 0x74b1d29al, 0xead54739l, 0x9dd277afl, 0x04db2615l,
	0x73dc1683l, 0xe3630b12l, 0x94643b84l, 0x0d6d6a3el, 0x7a6a5aa8l,
	0xe40ecf0bl, 0x9309ff9dl, 0x0a00ae27l, 0x7d079eb1l, 0xf00f9344l,
	0x8708a3d2l, 0x1e01f268l, 0x6906c2fel, 0xf762575dl, 0x806567cbl,
	0x196c3671l, 0x6e6b06e7l, 0xfed41b76l, 0x89d32be0l, 0x10da7a5al,
	0x67dd4accl, 0xf9b9df6fl, 0x8ebeeff9l, 0x17b7be43l, 0x60b08ed5l,
	0xd6d6a3e8l, 0xa1d1937el, 0x38d8c2c4l, 0x4fdff252l, 0xd1bb67f1l,
	0xa6bc5767l, 0x3fb506ddl, 0x48b2364bl, 0xd80d2bdal, 0xaf0a1b4cl,
	0x36034af6l, 0x41047a60l, 0xdf60efc3l, 0xa867df55l, 0x316e8eefl,
	0x4669be79l, 0xcb61b38cl, 0xbc66831al, 0x256fd2a0l, 0x5268e236l,
	0xcc0c7795l, 0xbb0b4703l, 0x220216b9l, 0x5505262fl, 0xc5ba3bbel,
	0xb2bd0b28l, 0x2bb45a92l, 0x5cb36a04l, 0xc2d7ffa7l, 0xb5d0cf31l,
	0x2cd99e8bl, 0x5bdeae1dl, 0x9b64c2b0l, 0xec63f226l, 0x756aa39cl,
	0x026d930al, 0x9c0906a9l, 0xeb0e363fl, 0x72076785l, 0x05005713l,
	0x95bf4a82l, 0xe2b87a14l, 0x7bb12bael, 0x0cb61b38l, 0x92d28e9bl,
	0xe5d5be0dl, 0x7cdcefb7l, 0x0bdbdf21l, 0x86d3d2d4l, 0xf1d4e242l,
	0x68ddb3f8l, 0x1fda836el, 0x81be16cdl, 0xf6b9265bl, 0x6fb077e1l,
	0x18b74777l, 0x88085ae6l, 0xff0f6a70l, 0x66063bcal, 0x11010b5cl,
	0x8f659effl, 0xf862ae69l, 0x616bffd3l, 0x166ccf45l, 0xa00ae278l,
	0xd70dd2eel, 0x4e048354l, 0x3903b3c2l, 0xa7672661l, 0xd06016f7l,
	0x4969474dl, 0x3e6e77dbl, 0xaed16a4al, 0xd9d65adcl, 0x40df0b66l,
	0x37d83bf0l, 0xa9bcae53l, 0xdebb9ec5l, 0x47b2cf7fl, 0x30b5ffe9l,
	0xbdbdf21cl, 0xcabac28al, 0x53b39330l, 0x24b4a3a6l, 0xbad03605l,
	0xcdd70693l, 0x54de5729l, 0x23d967bfl, 0xb3667a2el, 0xc4614ab8l,
	0x5d681b02l, 0x2a6f2b94l, 0xb40bbe37l, 0xc30c8ea1l, 0x5a05df1bl,
	0x2d02ef8dl
};

static boost::uint8_t crc32_index(boost::uint32_t crc) {
	return boost::uint8_t(crc & 0xff);
}

static boost::uint32_t crc32_shifted(boost::uint32_t crc) {
	return crc >> 8;
}

void crc32::update(const char * data, size_t length) {
	
	for(; (size_t(data) % 4 != 0) && length > 0; length--) {
		crc = crc32_table[crc32_index(crc) ^ boost::uint8_t(*data++)] ^ crc32_shifted(crc);
	}
	
	while(length >= 4) {
		crc ^= util::little_endian::load<boost::uint32_t>(data);
		crc = crc32_table[crc32_index(crc)] ^ crc32_shifted(crc);
		crc = crc32_table[crc32_index(crc)] ^ crc32_shifted(crc);
		crc = crc32_table[crc32_index(crc)] ^ crc32_shifted(crc);
		crc = crc32_table[crc32_index(crc)] ^ crc32_shifted(crc);
		length -= 4;
		data += 4;
	}
	
	while(length--) {
		crc = crc32_table[crc32_index(crc) ^ boost::uint8_t(*data++)] ^ crc32_shifted(crc);
	}
	
}

INNOEXTRACT_TEST(crc32,
	
	crc32 checksum;
	checksum.init();
	checksum.update(testdata, testlen);
	test("checksum", checksum.finalize() == 0x01f29e81);
	
)

} // namespace crypto
```

## File: `src/crypto/crc32.hpp`
```
/*
 * Copyright (C) 2011-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * CRC32 checksum routines.
 */
#ifndef INNOEXTRACT_CRYPTO_CRC32_HPP
#define INNOEXTRACT_CRYPTO_CRC32_HPP

#include <boost/cstdint.hpp>

#include "crypto/checksum.hpp"

namespace crypto {

//! CRC32 checksum calculation
struct crc32 : public checksum_base<crc32> {
	
	void init() { crc = CRC32_NEGL; }
	
	void update(const char * data, size_t length);
	
	boost::uint32_t finalize() const { return crc ^ CRC32_NEGL; }
	
private:
	
	static const boost::uint32_t CRC32_NEGL = 0xffffffffl;
	
	boost::uint32_t crc;
};

} // namespace crypto

#endif // INNOEXTRACT_CRYPTO_CRC32_HPP
```

## File: `src/crypto/hasher.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "crypto/hasher.hpp"

namespace crypto {

hasher::hasher(checksum_type type) : active_type(type) {
	
	switch(active_type) {
		case crypto::None: break;
		case crypto::Adler32: adler32.init(); break;
		case crypto::CRC32: crc32.init(); break;
		case crypto::MD5: md5.init(); break;
		case crypto::SHA1: sha1.init(); break;
		case crypto::SHA256: sha256.init(); break;
		case crypto::PBKDF2_SHA256_XChaCha20: break;
	};
	
}

void hasher::update(const char * data, size_t size) {
	
	switch(active_type) {
		case crypto::None: break;
		case crypto::Adler32: adler32.update(data, size); break;
		case crypto::CRC32: crc32.update(data, size); break;
		case crypto::MD5: md5.update(data, size); break;
		case crypto::SHA1: sha1.update(data, size); break;
		case crypto::SHA256: sha256.update(data, size); break;
		case crypto::PBKDF2_SHA256_XChaCha20: break;
	};
	
}

checksum hasher::finalize() {
	
	checksum result;
	
	result.type = active_type;
	
	switch(active_type) {
		case crypto::None: break;
		case crypto::Adler32: result.adler32 = adler32.finalize(); break;
		case crypto::CRC32: result.crc32 = crc32.finalize(); break;
		case crypto::MD5: md5.finalize(result.md5); break;
		case crypto::SHA1: sha1.finalize(result.sha1); break;
		case crypto::SHA256: sha256.finalize(result.sha256); break;
		case crypto::PBKDF2_SHA256_XChaCha20: break;
	};
	
	return result;
}

} // namespace crypto
```

## File: `src/crypto/hasher.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Utility to hash data with a configurable hash function.
 */
#ifndef INNOEXTRACT_CRYPTO_HASHER_HPP
#define INNOEXTRACT_CRYPTO_HASHER_HPP

#include "crypto/adler32.hpp"
#include "crypto/checksum.hpp"
#include "crypto/crc32.hpp"
#include "crypto/md5.hpp"
#include "crypto/sha1.hpp"
#include "crypto/sha256.hpp"
#include "util/enum.hpp"

struct checksum_uninitialized_error { };

namespace crypto {

class hasher : checksum_base<hasher> {
	
public:
	
	explicit hasher(checksum_type type);
	
	void update(const char * data, size_t size);
	
	checksum finalize();
	
private:
	
	checksum_type active_type;
	
	union {
		crypto::adler32 adler32;
		crypto::crc32 crc32;
		crypto::md5 md5;
		crypto::sha1 sha1;
		crypto::sha256 sha256;
	};
	
};

} // namespace crypto

#endif // INNOEXTRACT_CRYPTO_HASHER_HPP;
```

## File: `src/crypto/iteratedhash.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Generic hashing utilities.
 */
#ifndef INNOEXTRACT_CRYPTO_ITERATEDHASH_HPP
#define INNOEXTRACT_CRYPTO_ITERATEDHASH_HPP

// Taken from Crypto++ and modified to fit the project.

#include <cstring>

#include <boost/cstdint.hpp>
#include <boost/range/size.hpp>

#include "crypto/checksum.hpp"
#include "util/align.hpp"
#include "util/endian.hpp"
#include "util/math.hpp"
#include "util/types.hpp"

namespace crypto {

template <class T>
class iterated_hash : public checksum_base< iterated_hash<T> > {
	
public:
	
	typedef T transform;
	typedef typename transform::hash_word hash_word;
	typedef typename transform::byte_order byte_order;
	enum constants {
		block_size = transform::block_size,
		hash_size = transform::hash_size / sizeof(hash_word),
	};
	typedef hash_word state_t[hash_size];
	
	void init() { count_lo = count_hi = 0; transform::init(state); }
	
	void update(const char * data, size_t length);
	
	void finalize(char * result);
	
	static void prepare_state(const char * data, size_t count, state_t state) {
		transform::init(state);
		hash(state, data, count * block_size);
	}
	
	void init(const state_t init_state, size_t init_count) {
		count_lo = hash_word(init_count * block_size);
		count_hi = hash_word(util::safe_right_shift<8 * sizeof(hash_word)>(init_count * block_size));
		std::memcpy(state, init_state, sizeof(state));
	}
	
private:

	static size_t hash(state_t state, const char * input, size_t length);
	void pad(size_t last_block_size, char pad_first = '\x80');
	
	hash_word bit_count_hi() const {
		return (count_lo >> (8 * sizeof(hash_word) - 3)) + (count_hi << 3);
	}
	hash_word bit_count_lo() const { return count_lo << 3; }
	
	char buffer[block_size];
	state_t state;
	
	hash_word count_lo, count_hi;
	
};

template <class T>
void iterated_hash<T>::update(const char * data, size_t length) {
	
	hash_word old_count_lo = count_lo;
	
	if((count_lo = old_count_lo + hash_word(length)) < old_count_lo) {
		count_hi++; // carry from low to high
	}
	
	count_hi += hash_word(util::safe_right_shift<8 * sizeof(hash_word)>(length));
	
	size_t num = util::mod_power_of_2(old_count_lo, size_t(block_size));
	
	if(num != 0) { // process left over data
		if(num + length >= block_size) {
			std::memcpy(buffer + num, data, block_size - num);
			hash(state, buffer, block_size);
			data += (block_size - num);
			length -= (block_size - num);
			// drop through and do the rest
		} else {
			std::memcpy(buffer + num, data, length);
			return;
		}
	}
	
	// now process the input data in blocks of BlockSize bytes and save the leftovers to m_data
	if(length >= block_size) {
		size_t left_over = hash(state, data, length);
		data += (length - left_over);
		length = left_over;
	}
	
	if(length) {
		memcpy(buffer, data, length);
	}
}

template <class T>
size_t iterated_hash<T>::hash(hash_word state[hash_size], const char * input, size_t length) {
	
	if(byte_order::native() && util::is_aligned<hash_word>(input)) {
		
		do {
			
			transform::transform(state, reinterpret_cast<const hash_word *>(input));
			
			input += block_size;
			length -= block_size;
			
		} while(length >= block_size);
		
	} else {
		
		do {
			
			hash_word aligned_buffer[block_size / sizeof(hash_word)];
			byte_order::load(input, aligned_buffer, size_t(boost::size(aligned_buffer)));
			
			transform::transform(state, aligned_buffer);
			
			input += block_size;
			length -= block_size;
			
		} while(length >= block_size);
		
	}
	
	return length;
}

template <class T>
void iterated_hash<T>::pad(size_t last_block_size, char pad_first) {
	
	size_t num = util::mod_power_of_2(count_lo, size_t(block_size));
	
	buffer[num++] = pad_first;
	
	if(num <= last_block_size) {
		memset(buffer + num, 0, last_block_size - num);
	} else {
		memset(buffer + num, 0, block_size - num);
		hash(state, buffer, block_size);
		memset(buffer, 0, last_block_size);
	}
}

template <class T>
void iterated_hash<T>::finalize(char * result) {
	
	size_t order = transform::offset * sizeof(hash_word);
	
	size_t size = block_size - 2 * sizeof(hash_word);
	pad(size);
	byte_order::store(bit_count_lo(), buffer + size + order);
	byte_order::store(bit_count_hi(), buffer + size + sizeof(hash_word) - order);
	
	hash(state, buffer, block_size);
	
	byte_order::store(state, hash_size, result);
	
}

} // namespace crypto

#endif // INNOEXTRACT_CRYPTO_ITERATEDHASH_HPP
```

## File: `src/crypto/md5.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

// Taken from Crypto++ and modified to fit the project.
// md5.cpp - modified by Wei Dai from Colin Plumb's public domain md5.c
// any modifications are placed in the public domain

#include "crypto/md5.hpp"

#include "util/math.hpp"
#include "util/test.hpp"

namespace crypto {

void md5_transform::init(hash_word * state) {
	state[0] = 0x67452301l;
	state[1] = 0xefcdab89l;
	state[2] = 0x98badcfel;
	state[3] = 0x10325476l;
}

void md5_transform::transform(hash_word * state, const hash_word * data) {
	
	#define F1(x, y, z) (z ^ (x & (y ^ z)))
	#define F2(x, y, z) F1(z, x, y)
	#define F3(x, y, z) (x ^ y ^ z)
	#define F4(x, y, z) (y ^ (x | ~z))
	
	#define MD5STEP(f, w, x, y, z, word, s) \
		w = util::rotl_fixed(w + f(x, y, z) + word, s) + x
	
	hash_word a, b, c, d;
	
	a = state[0];
	b = state[1];
	c = state[2];
	d = state[3];
	
	MD5STEP(F1, a, b, c, d, data[0] + 0xd76aa478, 7);
	MD5STEP(F1, d, a, b, c, data[1] + 0xe8c7b756, 12);
	MD5STEP(F1, c, d, a, b, data[2] + 0x242070db, 17);
	MD5STEP(F1, b, c, d, a, data[3] + 0xc1bdceee, 22);
	MD5STEP(F1, a, b, c, d, data[4] + 0xf57c0faf, 7);
	MD5STEP(F1, d, a, b, c, data[5] + 0x4787c62a, 12);
	MD5STEP(F1, c, d, a, b, data[6] + 0xa8304613, 17);
	MD5STEP(F1, b, c, d, a, data[7] + 0xfd469501, 22);
	MD5STEP(F1, a, b, c, d, data[8] + 0x698098d8, 7);
	MD5STEP(F1, d, a, b, c, data[9] + 0x8b44f7af, 12);
	MD5STEP(F1, c, d, a, b, data[10] + 0xffff5bb1, 17);
	MD5STEP(F1, b, c, d, a, data[11] + 0x895cd7be, 22);
	MD5STEP(F1, a, b, c, d, data[12] + 0x6b901122, 7);
	MD5STEP(F1, d, a, b, c, data[13] + 0xfd987193, 12);
	MD5STEP(F1, c, d, a, b, data[14] + 0xa679438e, 17);
	MD5STEP(F1, b, c, d, a, data[15] + 0x49b40821, 22);
	
	MD5STEP(F2, a, b, c, d, data[1] + 0xf61e2562, 5);
	MD5STEP(F2, d, a, b, c, data[6] + 0xc040b340, 9);
	MD5STEP(F2, c, d, a, b, data[11] + 0x265e5a51, 14);
	MD5STEP(F2, b, c, d, a, data[0] + 0xe9b6c7aa, 20);
	MD5STEP(F2, a, b, c, d, data[5] + 0xd62f105d, 5);
	MD5STEP(F2, d, a, b, c, data[10] + 0x02441453, 9);
	MD5STEP(F2, c, d, a, b, data[15] + 0xd8a1e681, 14);
	MD5STEP(F2, b, c, d, a, data[4] + 0xe7d3fbc8, 20);
	MD5STEP(F2, a, b, c, d, data[9] + 0x21e1cde6, 5);
	MD5STEP(F2, d, a, b, c, data[14] + 0xc33707d6, 9);
	MD5STEP(F2, c, d, a, b, data[3] + 0xf4d50d87, 14);
	MD5STEP(F2, b, c, d, a, data[8] + 0x455a14ed, 20);
	MD5STEP(F2, a, b, c, d, data[13] + 0xa9e3e905, 5);
	MD5STEP(F2, d, a, b, c, data[2] + 0xfcefa3f8, 9);
	MD5STEP(F2, c, d, a, b, data[7] + 0x676f02d9, 14);
	MD5STEP(F2, b, c, d, a, data[12] + 0x8d2a4c8a, 20);
	
	MD5STEP(F3, a, b, c, d, data[5] + 0xfffa3942, 4);
	MD5STEP(F3, d, a, b, c, data[8] + 0x8771f681, 11);
	MD5STEP(F3, c, d, a, b, data[11] + 0x6d9d6122, 16);
	MD5STEP(F3, b, c, d, a, data[14] + 0xfde5380c, 23);
	MD5STEP(F3, a, b, c, d, data[1] + 0xa4beea44, 4);
	MD5STEP(F3, d, a, b, c, data[4] + 0x4bdecfa9, 11);
	MD5STEP(F3, c, d, a, b, data[7] + 0xf6bb4b60, 16);
	MD5STEP(F3, b, c, d, a, data[10] + 0xbebfbc70, 23);
	MD5STEP(F3, a, b, c, d, data[13] + 0x289b7ec6, 4);
	MD5STEP(F3, d, a, b, c, data[0] + 0xeaa127fa, 11);
	MD5STEP(F3, c, d, a, b, data[3] + 0xd4ef3085, 16);
	MD5STEP(F3, b, c, d, a, data[6] + 0x04881d05, 23);
	MD5STEP(F3, a, b, c, d, data[9] + 0xd9d4d039, 4);
	MD5STEP(F3, d, a, b, c, data[12] + 0xe6db99e5, 11);
	MD5STEP(F3, c, d, a, b, data[15] + 0x1fa27cf8, 16);
	MD5STEP(F3, b, c, d, a, data[2] + 0xc4ac5665, 23);
	
	MD5STEP(F4, a, b, c, d, data[0] + 0xf4292244, 6);
	MD5STEP(F4, d, a, b, c, data[7] + 0x432aff97, 10);
	MD5STEP(F4, c, d, a, b, data[14] + 0xab9423a7, 15);
	MD5STEP(F4, b, c, d, a, data[5] + 0xfc93a039, 21);
	MD5STEP(F4, a, b, c, d, data[12] + 0x655b59c3, 6);
	MD5STEP(F4, d, a, b, c, data[3] + 0x8f0ccc92, 10);
	MD5STEP(F4, c, d, a, b, data[10] + 0xffeff47d, 15);
	MD5STEP(F4, b, c, d, a, data[1] + 0x85845dd1, 21);
	MD5STEP(F4, a, b, c, d, data[8] + 0x6fa87e4f, 6);
	MD5STEP(F4, d, a, b, c, data[15] + 0xfe2ce6e0, 10);
	MD5STEP(F4, c, d, a, b, data[6] + 0xa3014314, 15);
	MD5STEP(F4, b, c, d, a, data[13] + 0x4e0811a1, 21);
	MD5STEP(F4, a, b, c, d, data[4] + 0xf7537e82, 6);
	MD5STEP(F4, d, a, b, c, data[11] + 0xbd3af235, 10);
	MD5STEP(F4, c, d, a, b, data[2] + 0x2ad7d2bb, 15);
	MD5STEP(F4, b, c, d, a, data[9] + 0xeb86d391, 21);
	
	state[0] += a;
	state[1] += b;
	state[2] += c;
	state[3] += d;
	
	#undef MD5STEP
	#undef F4
	#undef F3
	#undef F2
	#undef F1
	
}

INNOEXTRACT_TEST(md5,
	
	const boost::uint8_t expected[] = {
		0x6f, 0x6f, 0xfc, 0xc7, 0xb5, 0x85, 0x7d, 0xaf, 0x00, 0x6b, 0x9f, 0xcb, 0x13, 0x5c, 0xaa, 0x07
	};
	
	md5 checksum;
	checksum.init();
	checksum.update(testdata, testlen);
	char buffer[16];
	checksum.finalize(buffer);
	test_equals("checksum", buffer, expected, sizeof(expected));
	
)

} // namespace crypto
```

## File: `src/crypto/md5.hpp`
```
/*
 * Copyright (C) 2011-2015 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * MD5 hashing routines.
 */
#ifndef INNOEXTRACT_CRYPTO_MD5_HPP
#define INNOEXTRACT_CRYPTO_MD5_HPP

#include <boost/cstdint.hpp>

#include "crypto/iteratedhash.hpp"
#include "util/endian.hpp"

namespace crypto {

class md5_transform {
	
public:
	
	typedef boost::uint32_t hash_word;
	typedef util::little_endian byte_order;
	enum constants {
		offset = 0,
		block_size = 64,
		hash_size = 16,
	};
	
	static void init(hash_word * state);
	
	static void transform(hash_word * state, const hash_word * data);
	
};

typedef iterated_hash<md5_transform> md5;

} // namespace crypto

#endif // INNOEXTRACT_CRYPTO_MD5_HPP
```

## File: `src/crypto/pbkdf2.cpp`
```cpp
/*
 * Copyright (C) 2024 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

// Based on Inno Setup's PBKDF2.pas

#include "crypto/pbkdf2.hpp"

#include <cstring>

#include "crypto/sha1.hpp"
#include "crypto/sha256.hpp"
#include "util/test.hpp"

namespace crypto {

INNOEXTRACT_TEST(pbkdf2,
	
	// Testcase from Inno Setup's TestPBKDF2SHA256
	// which is based on https://stackoverflow.com/a/5136918/301485 and https://en.wikipedia.org/wiki/PBKDF2
	
	char buffer[40];
	
	const char * password0 = "password";
	const char * salt0 = "salt";
	const boost::uint8_t key0[] = {
		0x12, 0x0f, 0xb6, 0xcf, 0xfc, 0xf8, 0xb3, 0x2c, 0x43, 0xe7, 0x22, 0x52, 0x56, 0xc4, 0xf8, 0x37,
		0xa8, 0x65, 0x48, 0xc9, 0x2c, 0xcc, 0x35, 0x48, 0x08, 0x05, 0x98, 0x7c, 0xb7, 0x0b, 0xe1, 0x7b
	};
	pbkdf2<sha256>::derive(password0, std::strlen(password0), salt0, std::strlen(salt0), 1, buffer, 32);
	test_equals("sha256.single", buffer, key0, sizeof(key0));
	const boost::uint8_t key1[] = {
		0xc5, 0xe4, 0x78, 0xd5, 0x92, 0x88, 0xc8, 0x41, 0xaa, 0x53, 0x0d, 0xb6, 0x84, 0x5c, 0x4c, 0x8d,
		0x96, 0x28, 0x93, 0xa0, 0x01, 0xce, 0x4e, 0x11, 0xa4, 0x96, 0x38, 0x73, 0xaa, 0x98, 0x13, 0x4a
	};
	pbkdf2<sha256>::derive(password0, std::strlen(password0), salt0, std::strlen(salt0), 4096, buffer, 32);
	test_equals("sha256.multiple", buffer, key1, sizeof(key1));
	
	const char * password1 = "passwordPASSWORDpassword";
	const char * salt1 = "saltSALTsaltSALTsaltSALTsaltSALTsalt";
	const boost::uint8_t key2[] = {
		0x34, 0x8c, 0x89, 0xdb, 0xcb, 0xd3, 0x2b, 0x2f, 0x32, 0xd8,
		0x14, 0xb8, 0x11, 0x6e, 0x84, 0xcf, 0x2b, 0x17, 0x34, 0x7e,
		0xbc, 0x18, 0x00, 0x18, 0x1c, 0x4e, 0x2a, 0x1f, 0xb8, 0xdd,
		0x53, 0xe1, 0xc6, 0x35, 0x51, 0x8c, 0x7d, 0xac, 0x47, 0xe9
	};
	pbkdf2<sha256>::derive(password1, std::strlen(password1), salt1, std::strlen(salt1), 4096, buffer, 40);
	test_equals("sha256.longkey", buffer, key2, sizeof(key2));
	
	const char * password2 = "pass\0word";
	const char * salt2 = "sa\0lt";
	const boost::uint8_t key3[] = {
		0x89, 0xb6, 0x9d, 0x05, 0x16, 0xf8, 0x29, 0x89, 0x3c, 0x69, 0x62, 0x26, 0x65, 0x0a, 0x86, 0x87
	};
	pbkdf2<sha256>::derive(password2, 9, salt2, 5, 4096, buffer, 16);
	test_equals("sha256.evilpassword", buffer, key3, sizeof(key3));
	
	const char * password3 = "plnlrtfpijpuhqylxbgqiiyipieyxvfsavzgxbbcfusqkozwpngsyejqlmjsytrmd";
	const boost::uint8_t  salt3[] = {
		0xa0, 0x09, 0xc1, 0xa4, 0x85, 0x91, 0x2c, 0x6a, 0xe6, 0x30, 0xd3, 0xe7, 0x44, 0x24, 0x0b, 0x04
	};
	const boost::uint8_t key4[] = {
		0x28, 0x86, 0x9b, 0x5f, 0x31, 0xae, 0x29, 0x23, 0x6f, 0x16, 0x4c, 0x5c, 0xb3, 0x3e, 0x2e, 0x3b
	};
	pbkdf2<sha256>::derive(password3, std::strlen(password3), reinterpret_cast<const char *>(salt3),
	                       sizeof(salt3), 1000, buffer, 16);
	test_equals("sha256.longpassword", buffer, key4, sizeof(key4));
	
)

} // namespace crypto
```

## File: `src/crypto/pbkdf2.hpp`
```
/*
 * Copyright (C) 2024 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * PBKDF2 key derivationroutines.
 */
#ifndef INNOEXTRACT_CRYPTO_PBKDF2_HPP
#define INNOEXTRACT_CRYPTO_PBKDF2_HPP

#include "configure.hpp"

#if INNOEXTRACT_HAVE_DECRYPTION

#include <stddef.h>

#include <algorithm>
#include <cstring>

#include <boost/cstdint.hpp>

namespace crypto {
	
//! HMAC calculation
template <typename T>
struct hmac {
	
	typedef typename T::state_t state_t;
	enum constants {
		block_size = T::block_size,
		hash_size = T::hash_size * sizeof(typename T::hash_word),
	};
	
	void init(const state_t istate) {
		inner.init(istate, 1);
	}
	
	void update(const char * data, size_t length) {
		inner.update(data, length);
	}
	
	void finalize(const state_t ostate, char mac[hash_size]) {
		
		char buffer[hash_size];
		inner.finalize(buffer);
		
		T outer;
		outer.init(ostate, 1);
		outer.update(buffer, hash_size);
		outer.finalize(mac);
		
	}
	
	static void prepare_state(const char * password, size_t length, state_t istate, state_t ostate) {
		
		char ikey[block_size], okey[block_size];
		if(length > block_size) {
			T hash;
			hash.init();
			hash.update(password, length);
			hash.finalize(ikey);
			length = hash_size;
		} else {
			std::memcpy(ikey, password, length);
		}
		std::memset(ikey + length, 0, block_size - length);
		
		for(size_t i = 0; i < block_size; i++) {
			okey[i] = char(boost::uint8_t(ikey[i]) ^ boost::uint8_t(0x5c));
			ikey[i] = char(boost::uint8_t(ikey[i]) ^ boost::uint8_t(0x36));
		}
		
		T::prepare_state(ikey, 1, istate);
		T::prepare_state(okey, 1, ostate);
		
	}
	
private:
	
	T inner;
	
};

//! PBKDF2 key derivation calculation
template <typename T>
struct pbkdf2 {
	
	typedef hmac<T> hmac_t;
	enum constants {
		block_size = hmac_t::block_size,
		hash_size = hmac_t::hash_size,
	};
	
	static void derive(const char * password, size_t password_length, const char * salt, size_t salt_length,
	                   size_t iterations, char * key, size_t key_length) {
		
		typename hmac_t::state_t istate, ostate;
		hmac_t::prepare_state(password, password_length, istate, ostate);
		
		for(size_t block = 1; key_length > 0; block++) {
			
			char u[hash_size];
			{
				char b[4] = { char(block >> 24), char(block >> 16), char(block >> 8), char(block) };
				hmac_t mac;
				mac.init(istate);
				mac.update(salt, salt_length);
				mac.update(b, sizeof(b));
				mac.finalize(ostate, u);
			}
			char f[hash_size];
			std::memcpy(f, u, hash_size);
			
			for(size_t i = 1; i < iterations; i++) {
				hmac_t mac;
				mac.init(istate);
				mac.update(u, hash_size);
				mac.finalize(ostate, u);
				for(size_t j = 0; j < hash_size; j++) {
					f[j] = char(boost::uint8_t(f[j]) ^ boost::uint8_t(u[j]));
				}
			}
			
			size_t n = std::min(size_t(hash_size), key_length);
			std::memcpy(key, f, n);
			key += n;
			key_length -= n;
		}
		
	}
	
};

} // namespace crypto

#endif // INNOEXTRACT_HAVE_DECRYPTION

#endif // INNOEXTRACT_CRYPTO_PBKDF2_HPP

```

## File: `src/crypto/sha1.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

// Taken from Crypto++ and modified to fit the project.
// sha.cpp - modified by Wei Dai from Steve Reid's public domain sha1.c

#include "crypto/sha1.hpp"

#include "util/math.hpp"
#include "util/test.hpp"

namespace crypto {

void sha1_transform::init(hash_word * state) {
	state[0] = 0x67452301l;
	state[1] = 0xefcdab89l;
	state[2] = 0x98badcfel;
	state[3] = 0x10325476l;
	state[4] = 0xc3d2e1f0l;
}

void sha1_transform::transform(hash_word * state, const hash_word * data) {
	
	#define blk0(i) (W[i] = data[i])
	#define blk1(i) (W[i & 15] = util::rotl_fixed(W[(i + 13) & 15] ^ W[(i + 8) & 15] \
	                                              ^ W[(i + 2) & 15] ^ W[i & 15], 1))
	
	#define f1(x, y, z) (z ^ (x & (y ^ z)))
	#define f2(x, y, z) (x ^ y ^ z)
	#define f3(x, y, z) ((x & y) | (z & (x | y)))
	#define f4(x, y, z) (x ^ y ^ z)
	
	/* (R0+R1), R2, R3, R4 are the different operations used in SHA1 */
	#define R0(v, w, x, y, z, i) \
		z += f1(w, x, y) + blk0(i) + 0x5A827999 + util::rotl_fixed(v, 5); \
		w = util::rotl_fixed(w, 30);
	#define R1(v, w, x, y, z, i) \
		z += f1(w, x, y) + blk1(i) + 0x5A827999 + util::rotl_fixed(v, 5); \
		w = util::rotl_fixed(w, 30);
	#define R2(v, w, x, y, z, i) \
		z += f2(w, x, y) + blk1(i) + 0x6ED9EBA1 + util::rotl_fixed(v, 5); \
		w = util::rotl_fixed(w, 30);
	#define R3(v, w, x, y, z, i) \
		z += f3(w, x, y) + blk1(i) + 0x8F1BBCDC + util::rotl_fixed(v, 5); \
		w = util::rotl_fixed(w, 30);
	#define R4(v, w, x, y, z, i) \
		z += f4(w, x, y) + blk1(i) + 0xCA62C1D6 + util::rotl_fixed(v, 5); \
		w = util::rotl_fixed(w, 30);
	
	hash_word W[16];
	
	/* Copy context->state[] to working vars */
	hash_word a = state[0];
	hash_word b = state[1];
	hash_word c = state[2];
	hash_word d = state[3];
	hash_word e = state[4];
	
	/* 4 rounds of 20 operations each. Loop unrolled. */
	
	R0(a, b, c, d, e,  0);
	R0(e, a, b, c, d,  1);
	R0(d, e, a, b, c,  2);
	R0(c, d, e, a, b,  3);
	
	R0(b, c, d, e, a,  4);
	R0(a, b, c, d, e,  5);
	R0(e, a, b, c, d,  6);
	R0(d, e, a, b, c,  7);
	
	R0(c, d, e, a, b,  8);
	R0(b, c, d, e, a,  9);
	R0(a, b, c, d, e, 10);
	R0(e, a, b, c, d, 11);
	
	R0(d, e, a, b, c, 12);
	R0(c, d, e, a, b, 13);
	R0(b, c, d, e, a, 14);
	R0(a, b, c, d, e, 15);
	
	R1(e, a, b, c, d, 16);
	R1(d, e, a, b, c, 17);
	R1(c, d, e, a, b, 18);
	R1(b, c, d, e, a, 19);
	
	R2(a, b, c, d, e, 20);
	R2(e, a, b, c, d, 21);
	R2(d, e, a, b, c, 22);
	R2(c, d, e, a, b, 23);
	
	R2(b, c, d, e, a, 24);
	R2(a, b, c, d, e, 25);
	R2(e, a, b, c, d, 26);
	R2(d, e, a, b, c, 27);
	
	R2(c, d, e, a, b, 28);
	R2(b, c, d, e, a, 29);
	R2(a, b, c, d, e, 30);
	R2(e, a, b, c, d, 31);
	
	R2(d, e, a, b, c, 32);
	R2(c, d, e, a, b, 33);
	R2(b, c, d, e, a, 34);
	R2(a, b, c, d, e, 35);
	
	R2(e, a, b, c, d, 36);
	R2(d, e, a, b, c, 37);
	R2(c, d, e, a, b, 38);
	R2(b, c, d, e, a, 39);
	
	R3(a, b, c, d, e, 40);
	R3(e, a, b, c, d, 41);
	R3(d, e, a, b, c, 42);
	R3(c, d, e, a, b, 43);
	
	R3(b, c, d, e, a, 44);
	R3(a, b, c, d, e, 45);
	R3(e, a, b, c, d, 46);
	R3(d, e, a, b, c, 47);
	
	R3(c, d, e, a, b, 48);
	R3(b, c, d, e, a, 49);
	R3(a, b, c, d, e, 50);
	R3(e, a, b, c, d, 51);
	
	R3(d, e, a, b, c, 52);
	R3(c, d, e, a, b, 53);
	R3(b, c, d, e, a, 54);
	R3(a, b, c, d, e, 55);
	
	R3(e, a, b, c, d, 56);
	R3(d, e, a, b, c, 57);
	R3(c, d, e, a, b, 58);
	R3(b, c, d, e, a, 59);
	
	R4(a, b, c, d, e, 60);
	R4(e, a, b, c, d, 61);
	R4(d, e, a, b, c, 62);
	R4(c, d, e, a, b, 63);
	
	R4(b, c, d, e, a, 64);
	R4(a, b, c, d, e, 65);
	R4(e, a, b, c, d, 66);
	R4(d, e, a, b, c, 67);
	
	R4(c, d, e, a, b, 68);
	R4(b, c, d, e, a, 69);
	R4(a, b, c, d, e, 70);
	R4(e, a, b, c, d, 71);
	
	R4(d, e, a, b, c, 72);
	R4(c, d, e, a, b, 73);
	R4(b, c, d, e, a, 74);
	R4(a, b, c, d, e, 75);
	
	R4(e, a, b, c, d, 76);
	R4(d, e, a, b, c, 77);
	R4(c, d, e, a, b, 78);
	R4(b, c, d, e, a, 79);
	
	/* Add the working vars back into context.state[] */
	state[0] += a;
	state[1] += b;
	state[2] += c;
	state[3] += d;
	state[4] += e;
	
	#undef R4
	#undef R3
	#undef R2
	#undef R1
	#undef R0
	
	#undef f4
	#undef f3
	#undef f2
	#undef f1
	
	#undef blk1
	#undef blk0
	
}

INNOEXTRACT_TEST(sha1,
	
	const boost::uint8_t expected[] = {
		0x7f, 0xe5, 0x54, 0xd3, 0x47, 0x1e, 0xc7, 0xba, 0xb3, 0x37,
		0x4f, 0xfd, 0x46, 0xb3, 0x88, 0x85, 0x12, 0x2b, 0x13, 0x14
	};
	
	sha1 checksum;
	checksum.init();
	checksum.update(testdata, testlen);
	char buffer[20];
	checksum.finalize(buffer);
	test_equals("checksum", buffer, expected, sizeof(expected));
	
)

} // namespace crypto
```

## File: `src/crypto/sha1.hpp`
```
/*
 * Copyright (C) 2011-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * SHA-1 hashing routines.
 */
#ifndef INNOEXTRACT_CRYPTO_SHA1_HPP
#define INNOEXTRACT_CRYPTO_SHA1_HPP

#include <boost/cstdint.hpp>

#include "crypto/iteratedhash.hpp"
#include "util/endian.hpp"

namespace crypto {

class sha1_transform {
	
public:
	
	typedef boost::uint32_t hash_word;
	typedef util::big_endian byte_order;
	enum constants {
		offset = 1,
		block_size = 64,
		hash_size = 20,
	};
	
	static void init(hash_word * state);
	
	static void transform(hash_word * state, const hash_word * data);
};

typedef iterated_hash<sha1_transform> sha1;

} // namespace crypto

#endif // INNOEXTRACT_CRYPTO_SHA1_HPP
```

## File: `src/crypto/sha256.cpp`
```cpp
/*
 * Copyright (C) 2024 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

// Taken from Crypto++ and modified to fit the project.
// Wei Dai implemented SHA-2.

#include "crypto/sha256.hpp"

#include "util/math.hpp"
#include "util/test.hpp"

namespace crypto {

static const boost::uint32_t sha256_k[] = {
	0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
	0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
	0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
	0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
	0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
	0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
	0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
	0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
};

void sha256_transform::init(hash_word * state) {
	state[0] = 0x6a09e667;
	state[1] = 0xbb67ae85;
	state[2] = 0x3c6ef372;
	state[3] = 0xa54ff53a;
	state[4] = 0x510e527f;
	state[5] = 0x9b05688c;
	state[6] = 0x1f83d9ab;
	state[7] = 0x5be0cd19;
}

void sha256_transform::transform(hash_word * state, const hash_word * data) {
	
	#define a(i) T[(0 - i) & 7]
	#define b(i) T[(1 - i) & 7]
	#define c(i) T[(2 - i) & 7]
	#define d(i) T[(3 - i) & 7]
	#define e(i) T[(4 - i) & 7]
	#define f(i) T[(5 - i) & 7]
	#define g(i) T[(6 - i) & 7]
	#define h(i) T[(7 - i) & 7]
	
	#define blk0(i) (W[i] = data[i])
	#define blk2(i) (W[i & 15] += s1(W[(i - 2) & 15]) + W[(i - 7) & 15] + s0(W[(i - 15) & 15]))
	
	#define Ch(x, y, z) (z ^ (x & (y ^ z)))
	#define Maj(x, y, z) (y ^ ((x ^ y) & (y ^ z)))
	
	#define R(i) \
		h(i) += S1(e(i)) + Ch(e(i), f(i), g(i)) + sha256_k[i + j] + (j ? blk2(i) : blk0(i)); \
		d(i) += h(i); \
		h(i) += S0(a(i)) + Maj(a(i), b(i), c(i))
	
	#define s0(x) (util::rotr_fixed(x, 7) ^ util::rotr_fixed(x, 18) ^ (x >> 3))
	#define s1(x) (util::rotr_fixed(x, 17) ^ util::rotr_fixed(x, 19) ^ (x >> 10))
	#define S0(x) (util::rotr_fixed(x, 2) ^ util::rotr_fixed(x, 13) ^ util::rotr_fixed(x, 22))
	#define S1(x) (util::rotr_fixed(x, 6) ^ util::rotr_fixed(x, 11) ^ util::rotr_fixed(x, 25))
	
	hash_word W[16] = {0}, T[8];
	
	/* Copy context->state to working vars */
	std::memcpy(T, state, sizeof(T));
	
	/* 64 operations, partially loop unrolled */
	for(size_t j = 0; j < 64; j += 16) {
		R(0);
		R(1);
		R(2);
		R(3);
		R(4);
		R(5);
		R(6);
		R(7);
		R(8);
		R(9);
		R(10);
		R(11);
		R(12);
		R(13);
		R(14);
		R(15);
	}
	
	/* Add the working vars back into context.state[] */
	state[0] += a(0);
	state[1] += b(0);
	state[2] += c(0);
	state[3] += d(0);
	state[4] += e(0);
	state[5] += f(0);
	state[6] += g(0);
	state[7] += h(0);
	
	#undef Ch
	#undef Maj
	#undef s0
	#undef s1
	#undef S0
	#undef S1
	#undef blk0
	#undef blk1
	#undef blk2
	#undef R
	
	#undef a
	#undef b
	#undef c
	#undef d
	#undef e
	#undef f
	#undef g
	#undef h
	
}

INNOEXTRACT_TEST(sha256,
	
	const boost::uint8_t expected[] = {
		0x20, 0x95, 0xa0, 0x2a, 0x36, 0x55, 0x64, 0x28, 0xa4, 0x50, 0xe7, 0x7a, 0xbf, 0x44, 0x96, 0x1e,
		0x8a, 0xf1, 0xee, 0xb2, 0x0b, 0x92, 0xc3, 0x8b, 0xbd, 0x7b, 0x83, 0xd0, 0x08, 0xd7, 0xe1, 0xfa
	};
	
	sha256 checksum;
	checksum.init();
	checksum.update(testdata, testlen);
	char buffer[32];
	checksum.finalize(buffer);
	test_equals("checksum", buffer, expected, sizeof(expected));
	
)

} // namespace crypto
```

## File: `src/crypto/sha256.hpp`
```
/*
 * Copyright (C) 2024 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * SHA-256 hashing routines.
 */
#ifndef INNOEXTRACT_CRYPTO_SHA256_HPP
#define INNOEXTRACT_CRYPTO_SHA256_HPP

#include <boost/cstdint.hpp>

#include "crypto/iteratedhash.hpp"
#include "util/endian.hpp"

namespace crypto {

class sha256_transform {
	
public:
	
	typedef boost::uint32_t hash_word;
	typedef util::big_endian byte_order;
	enum constants {
		offset = 1,
		block_size = 64,
		hash_size = 32,
	};
	
	static void init(hash_word * state);
	
	static void transform(hash_word * state, const hash_word * data);
};

typedef iterated_hash<sha256_transform> sha256;

} // namespace crypto

#endif // INNOEXTRACT_CRYPTO_SHA256_HPP
```

## File: `src/crypto/xchacha20.cpp`
```cpp
/*
 * Copyright (C) 2024 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

// Based on Inno Setup's ChaCha20.pas which is in turn based on https://github.com/Ginurx/chacha20-c

#include "crypto/xchacha20.hpp"

#include <algorithm>
#include <cstring>

#include "util/endian.hpp"
#include "util/math.hpp"
#include "util/test.hpp"

namespace crypto {

void xchacha20::init(const char key[key_size], const char nonce[nonce_size]) {
	
	char subkey[key_size];
	derive_subkey(key, nonce, subkey);
	init_state(state, subkey);
	state[12] = 0;
	state[13] = 0;
	state[14] = util::little_endian::load<word>(nonce + 16);
	state[15] = util::little_endian::load<word>(nonce + 20);
	pos = sizeof(keystream);
	
}

void xchacha20::discard(size_t length) {
	
	// asume pos > 0 && pos <= sizeof(keystream)
	
	if(pos != sizeof(keystream)) {
		size_t remaining = std::min(length, size_t(64) - size_t(pos));
		pos = boost::uint8_t(pos + remaining);
		length -= remaining;
	}
	
	// assert length == 0 || pos == sizeof(keystream)
	
	increment_count(state, length / sizeof(keystream));
	
	if(length % sizeof(keystream)) {
		update();
		pos = boost::uint8_t(length % sizeof(keystream));
	}
	
}

void xchacha20::crypt(const char * in, char * out, size_t length) {
	
	// asume pos > 0 && pos <= 64
	
	for(size_t i = 0; i < length; i++, pos++) {
		if(pos == sizeof(keystream)) {
			update();
			pos = 0;
		}
		boost::uint8_t key = boost::uint8_t(keystream[pos / sizeof(word)] >> ((pos % sizeof(word)) * 8));
		out[i] = char(boost::uint8_t(in[i]) ^ key);
	}
	
}


void xchacha20::update() {
	
	std::memcpy(keystream, state, sizeof(state));
	run_rounds(keystream);
	
	for(size_t i = 0; i < 16; i++) {
		keystream[i] += state[i];
	}
	
	increment_count(state);
	
}

void xchacha20::derive_subkey(const char key[key_size], const char nonce[16], char subkey[key_size]) {
	
	word state[16];
	init_state(state, key);
	state[12] = util::little_endian::load<word>(nonce);
	state[13] = util::little_endian::load<word>(nonce + 4);
	state[14] = util::little_endian::load<word>(nonce + 8);
	state[15] = util::little_endian::load<word>(nonce + 12);
	run_rounds(state);
	util::little_endian::store<word>(state[0], subkey);
	util::little_endian::store<word>(state[1], subkey + 4);
	util::little_endian::store<word>(state[2], subkey + 8);
	util::little_endian::store<word>(state[3], subkey + 12);
	util::little_endian::store<word>(state[12], subkey + 16);
	util::little_endian::store<word>(state[13], subkey + 20);
	util::little_endian::store<word>(state[14], subkey + 24);
	util::little_endian::store<word>(state[15], subkey + 28);
	
}


void xchacha20::init_state(word state[16], const char key[key_size]) {
	
	state[0] = 0x61707865;
	state[1] = 0x3320646e;
	state[2] = 0x79622d32;
	state[3] = 0x6b206574;
	for(size_t i = 0; i < 8; i++) {
		state[4 + i] = util::little_endian::load<word>(key + i * sizeof(word));
	}
	
}

void xchacha20::run_rounds(word keystream[16]) {
	
	#define CHACHA20_QR(a, b, c, d) \
		a += b; \
		d = d ^ a; \
		d = util::rotl_fixed(d, 16); \
		c += d; \
		b = b ^ c; \
		b = util::rotl_fixed(b, 12); \
		a += b; \
		d = d ^ a; \
		d = util::rotl_fixed(d, 8); \
		c += d; \
		b = b ^ c; \
		b = util::rotl_fixed(b, 7);
	
	for(size_t i = 0; i < 10; i++) {
		CHACHA20_QR(keystream[0], keystream[4], keystream[8], keystream[12]);  // column 0
		CHACHA20_QR(keystream[1], keystream[5], keystream[9], keystream[13]);  // column 1
		CHACHA20_QR(keystream[2], keystream[6], keystream[10], keystream[14]); // column 2
		CHACHA20_QR(keystream[3], keystream[7], keystream[11], keystream[15]); // column 3
		CHACHA20_QR(keystream[0], keystream[5], keystream[10], keystream[15]); // diagonal 1 (main diagonal)
		CHACHA20_QR(keystream[1], keystream[6], keystream[11], keystream[12]); // diagonal 2
		CHACHA20_QR(keystream[2], keystream[7], keystream[8], keystream[13]);  // diagonal 3
		CHACHA20_QR(keystream[3], keystream[4], keystream[9], keystream[14]);  // diagonal 4
	}
	
	#undef CHACHA20_QR
	
}

void xchacha20::increment_count(word state[16], size_t increment) {
	
	boost::uint64_t count = (boost::uint64_t(state[13]) << (sizeof(word) * 8)) + state[12];
	count += increment;
	state[12] = word(count);
	state[13] = word(count >> (sizeof(word) * 8));
	
}

INNOEXTRACT_TEST(xchacha20,
	
	// Testcase from Inno Setup's TestHChaCha20
	
	const boost::uint8_t hkey[] = {
		0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
		0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f
	};
	const boost::uint8_t hnonce[] = {
		0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x4a, 0x00, 0x00, 0x00, 0x00, 0x31, 0x41, 0x59, 0x27
	};
	const boost::uint8_t subkey[] = {
		0x82, 0x41, 0x3b, 0x42, 0x27, 0xb2, 0x7b, 0xfe, 0xd3, 0x0e, 0x42, 0x50, 0x8a, 0x87, 0x7d, 0x73,
		0xa0, 0xf9, 0xe4, 0xd5, 0x8a, 0x74, 0xa8, 0x53, 0xc1, 0x2e, 0xc4, 0x13, 0x26, 0xd3, 0xec, 0xdc
	};
	
	char buffer[xchacha20::key_size];
	xchacha20::derive_subkey(reinterpret_cast<const char *>(hkey), reinterpret_cast<const char*>(hnonce), buffer);
	test_equals("derive_subkey", buffer, subkey, sizeof(subkey));
	
	// Testcase from Inno Setup's TestXChaCha20
	
	const boost::uint8_t key[] = {
		0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8a, 0x8b, 0x8c, 0x8d, 0x8e, 0x8f,
		0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9a, 0x9b, 0x9c, 0x9d, 0x9e, 0x9f
	};
	const boost::uint8_t nonce[] = {
		0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4a, 0x4b,
		0x4c, 0x4d, 0x4e, 0x4f, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x58
	};
	
	const boost::uint8_t ciphertext[] = {
		0x45, 0x59, 0xab, 0xba, 0x4e, 0x48, 0xc1, 0x61, 0x02, 0xe8, 0xbb, 0x2c, 0x05, 0xe6, 0x94, 0x7f,
		0x50, 0xa7, 0x86, 0xde, 0x16, 0x2f, 0x9b, 0x0b, 0x7e, 0x59, 0x2a, 0x9b, 0x53, 0xd0, 0xd4, 0xe9,
		0x8d, 0x8d, 0x64, 0x10, 0xd5, 0x40, 0xa1, 0xa6, 0x37, 0x5b, 0x26, 0xd8, 0x0d, 0xac, 0xe4, 0xfa,
		0xb5, 0x23, 0x84, 0xc7, 0x31, 0xac, 0xbf, 0x16, 0xa5, 0x92, 0x3c, 0x0c, 0x48, 0xd3, 0x57, 0x5d,
		0x4d, 0x0d, 0x2c, 0x67, 0x3b, 0x66, 0x6f, 0xaa, 0x73, 0x10, 0x61, 0x27, 0x77, 0x01, 0x09, 0x3a,
		0x6b, 0xf7, 0xa1, 0x58, 0xa8, 0x86, 0x42, 0x92, 0xa4, 0x1c, 0x48, 0xe3, 0xa9, 0xb4, 0xc0, 0xda,
		0xec, 0xe0, 0xf8, 0xd9, 0x8d, 0x0d, 0x7e, 0x05, 0xb3, 0x7a, 0x30, 0x7b, 0xbb, 0x66, 0x33, 0x31,
		0x64, 0xec, 0x9e, 0x1b, 0x24, 0xea, 0x0d, 0x6c, 0x3f, 0xfd, 0xdc, 0xec, 0x4f, 0x68, 0xe7, 0x44,
		0x30, 0x56, 0x19, 0x3a, 0x03, 0xc8, 0x10, 0xe1, 0x13, 0x44, 0xca, 0x06, 0xd8, 0xed, 0x8a, 0x2b,
		0xfb, 0x1e, 0x8d, 0x48, 0xcf, 0xa6, 0xbc, 0x0e, 0xb4, 0xe2, 0x46, 0x4b, 0x74, 0x81, 0x42, 0x40,
		0x7c, 0x9f, 0x43, 0x1a, 0xee, 0x76, 0x99, 0x60, 0xe1, 0x5b, 0xa8, 0xb9, 0x68, 0x90, 0x46, 0x6e,
		0xf2, 0x45, 0x75, 0x99, 0x85, 0x23, 0x85, 0xc6, 0x61, 0xf7, 0x52, 0xce, 0x20, 0xf9, 0xda, 0x0c,
		0x09, 0xab, 0x6b, 0x19, 0xdf, 0x74, 0xe7, 0x6a, 0x95, 0x96, 0x74, 0x46, 0xf8, 0xd0, 0xfd, 0x41,
		0x5e, 0x7b, 0xee, 0x2a, 0x12, 0xa1, 0x14, 0xc2, 0x0e, 0xb5, 0x29, 0x2a, 0xe7, 0xa3, 0x49, 0xae,
		0x57, 0x78, 0x20, 0xd5, 0x52, 0x0a, 0x1f, 0x3f, 0xb6, 0x2a, 0x17, 0xce, 0x6a, 0x7e, 0x68, 0xfa,
		0x7c, 0x79, 0x11, 0x1d, 0x88, 0x60, 0x92, 0x0b, 0xc0, 0x48, 0xef, 0x43, 0xfe, 0x84, 0x48, 0x6c,
		0xcb, 0x87, 0xc2, 0x5f, 0x0a, 0xe0, 0x45, 0xf0, 0xcc, 0xe1, 0xe7, 0x98, 0x9a, 0x9a, 0xa2, 0x20,
		0xa2, 0x8b, 0xdd, 0x48, 0x27, 0xe7, 0x51, 0xa2, 0x4a, 0x6d, 0x5c, 0x62, 0xd7, 0x90, 0xa6, 0x63,
		0x93, 0xb9, 0x31, 0x11, 0xc1, 0xa5, 0x5d, 0xd7, 0x42, 0x1a, 0x10, 0x18, 0x49, 0x74, 0xc7, 0xc5
	};
	
	xchacha20 cipher;
	
	cipher.init(reinterpret_cast<const char*>(key), reinterpret_cast<const char *>(nonce));
	char buffer0[sizeof(ciphertext)];
	cipher.crypt(testdata, buffer0, sizeof(ciphertext));
	test_equals("crypt", buffer0, ciphertext, sizeof(ciphertext));
	
	cipher.init(reinterpret_cast<const char*>(key), reinterpret_cast<const char *>(nonce));
	cipher.crypt(testdata, buffer0, 3);
	cipher.discard(129);
	char buffer1[sizeof(ciphertext) - 132];
	cipher.crypt(testdata + 132, buffer1, sizeof(ciphertext) - 132);
	test_equals("discard", buffer1, ciphertext + 132, sizeof(ciphertext) - 132);
	
)

} // namespace crypto
```

## File: `src/crypto/xchacha20.hpp`
```
/*
 * Copyright (C) 2024 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * ChaCha20 en-/decryption routines.
 */
#ifndef INNOEXTRACT_CRYPTO_XCHACHA20_HPP
#define INNOEXTRACT_CRYPTO_XCHACHA20_HPP

#include <stddef.h>

#include <boost/cstdint.hpp>

#include "configure.hpp"

#if INNOEXTRACT_HAVE_DECRYPTION

namespace crypto {

//! ChaCha20 en-/decryption calculation
struct xchacha20 {
	
	enum constants {
		key_size = 32,
		nonce_size = 24,
	};
	
	typedef boost::uint32_t word;
	
	void init(const char key[key_size], const char nonce[nonce_size]);
	
	void discard(size_t length);
	
	void crypt(const char * in, char * out, size_t length);
	
private:
	
	void update();
	
	static void derive_subkey(const char key[key_size], const char nonce[16], char subkey[key_size]);
	
	static void init_state(word state[16], const char key[key_size]);
	
	static void run_rounds(word keystream[16]);
	
	static void increment_count(word state[16], size_t increment = 1);
	
	word state[16];
	word keystream[16];
	boost::uint8_t pos;
	
	#ifdef INNOEXTRACT_BUILD_TESTS
	friend struct xchacha20_test;
	#endif
};

} // namespace crypto

#endif // INNOEXTRACT_HAVE_DECRYPTION

#endif // INNOEXTRACT_CRYPTO_XCHACHA20_HPP
```

## File: `src/loader/exereader.cpp`
```cpp
/*
 * Copyright (C) 2011-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "loader/exereader.hpp"

#include <iomanip>
#include <ios>
#include <istream>
#include <algorithm>
#include <cstring>
#include <vector>

#include <boost/cstdint.hpp>
#include <boost/foreach.hpp>

#include "util/load.hpp"

namespace loader {

namespace {

enum BinaryType {
	UnknownBinary = 0,
	DOSMagic = 0x5a4d, // "MZ"
	OS2Magic = 0x454E, // "NE"
	VXDMagic = 0x454C, // "LE"
	PEMagic  = 0x4550, // "PE"
	PEMagic2 = 0x0000, // "\0\0"
};

BinaryType determine_binary_type(std::istream & is) {
	
	boost::uint16_t dos_magic = util::load<boost::uint16_t>(is.seekg(0));
	if(is.fail() || dos_magic != DOSMagic) {
		return UnknownBinary; // Not a DOS file
	}
	
	// Skip the DOS stub
	boost::uint16_t new_offset = util::load<boost::uint16_t>(is.seekg(0x3c));
	if(is.fail()) {
		return DOSMagic;
	}
	
	boost::uint16_t new_magic = util::load<boost::uint16_t>(is.seekg(new_offset));
	if(is.fail()) {
		return DOSMagic;
	}
	
	if(new_magic == PEMagic) {
		boost::uint16_t pe2_magic = util::load<boost::uint16_t>(is);
		if(is.fail() || pe2_magic != PEMagic2) {
			return DOSMagic;
		}
	}
	
	return BinaryType(new_magic);
}

template <typename T>
bool skip_to_fixed_file_info(std::istream & is, boost::uint32_t resource_offset,
                             boost::uint32_t offset) {
	
	is.seekg(resource_offset + offset);
	T key;
	do {
		key = util::load<T>(is);
		if(is.fail()) {
			return false;
		}
		offset += boost::uint32_t(sizeof(key));
	} while(key != 0);
	
	// Align to DWORD
	offset = (offset + 3) & ~boost::uint32_t(3);
	
	is.seekg(resource_offset + offset);
	
	return true;
}

// Reader for OS2 binaries
struct ne_reader : public exe_reader {
	
	static resource find_resource(std::istream & is, boost::uint32_t name,
	                              boost::uint32_t type = TypeData);
	
	static bool get_file_version(std::istream & is);
	
};

exe_reader::resource ne_reader::find_resource(std::istream & is, boost::uint32_t name,
                                              boost::uint32_t type) {
	
	resource result;
	result.offset = result.size = 0;
	
	is.seekg(0x24 - 2, std::ios_base::cur); // Already read the magic
	boost::uint16_t resources_offset = util::load<boost::uint16_t>(is);
	boost::uint16_t resources_end = util::load<boost::uint16_t>(is);
	if(is.fail()) {
		return result;
	}
	
	if(resources_end == resources_offset) {
		return result;
	}
	
	is.seekg(std::streamoff(resources_offset) - 0x28, std::ios_base::cur);
	
	boost::uint16_t shift = util::load<boost::uint16_t>(is);
	if(is.fail() || shift >= 32) {
		return result;
	}
	
	boost::uint16_t name_count;
	for(;;) {
		
		boost::uint16_t type_id = util::load<boost::uint16_t>(is);
		name_count = util::load<boost::uint16_t>(is);
		is.seekg(4, std::ios_base::cur);
		if(is.fail() || type_id == 0) {
			return result;
		}
		
		if(type_id == boost::uint16_t(type | 0x8000)) {
			break;
		}
		
		is.seekg(name_count * 12, std::ios_base::cur);
		
	}
	
	for(boost::uint16_t i = 0; i < name_count; i++) {
		
		boost::uint16_t offset = util::load<boost::uint16_t>(is);
		boost::uint16_t size   = util::load<boost::uint16_t>(is);
		is.seekg(2, std::ios_base::cur);
		boost::uint16_t name_id = util::load<boost::uint16_t>(is);
		is.seekg(4, std::ios_base::cur);
		if(is.fail()) {
			return result;
		}
		
		if(name_id == boost::uint16_t(name | 0x8000)) {
			result.offset = boost::uint32_t(offset) << shift;
			result.size   = boost::uint32_t(size)   << shift;
			break;
		}
		
	}
	
	return result;
}

bool ne_reader::get_file_version(std::istream & is) {
	
	resource res = find_resource(is, NameVersionInfo, TypeVersion);
	if(!res) {
		return false;
	}
	
	return skip_to_fixed_file_info<boost::int8_t>(is, res.offset, 4);
}

// Reader for VXD binaries
struct le_reader : public exe_reader {
	
	static bool get_file_version(std::istream & is);
	
};

bool le_reader::get_file_version(std::istream & is) {
	
	is.seekg(0xb8 - 2, std::ios_base::cur);  // Already read the magic
	boost::uint32_t resources_offset = util::load<boost::uint32_t>(is);
	boost::uint32_t resources_size = util::load<boost::uint32_t>(is);
	if(is.fail()) {
		return false;
	}
	
	if(resources_size <= 12) {
		return false;
	}
	
	is.seekg(resources_offset);
	boost::uint8_t type = util::load<boost::uint8_t>(is);
	boost::uint16_t id = util::load<boost::uint16_t>(is);
	boost::uint8_t name = util::load<boost::uint8_t>(is);
	is.seekg(4, std::ios_base::cur); // skip ordinal + flags
	boost::uint32_t size = util::load<boost::uint32_t>(is);
	if(is.fail() || type != 0xff || id != 16 || name != 0xff || size <= 20 + 52) {
		return false;
	}
	
	boost::uint16_t node = util::load<boost::uint16_t>(is);
	boost::uint16_t data = util::load<boost::uint16_t>(is);
	is.seekg(16, std::ios_base::cur); // skip key
	if(is.fail() || node < 20 + 52 || data < 52) {
		return false;
	}
	
	return true;
}

// Reader for Win32 binaries
struct pe_reader : public exe_reader {
	
	struct header {
		
		//! Number of CoffSection structures following this header after optionalHeaderSize bytes
		boost::uint16_t nsections;
		
		//! Offset of the section table in the file
		boost::uint32_t section_table_offset;
		
		//! Virtual memory address of the resource root table
		boost::uint32_t resource_table_address;
		
		bool load(std::istream & is);
		
	};
	
	struct section {
		
		boost::uint32_t virtual_size; //!< Section size in virtual memory
		boost::uint32_t virtual_address; //!< Base virtual memory address
		
		boost::uint32_t raw_address; //!< Base file offset
		
	};
	
	struct section_table {
		
		std::vector<section> sections;
		
		bool load(std::istream & is, const header & coff);
		
		/*!
		 * Convert a memory address to a file offset according to the given section list.
		 */
		boost::uint32_t to_file_offset(boost::uint32_t address);
		
	};
	
	static bool get_resource_table(boost::uint32_t & entry, boost::uint32_t offset);
	
	/*!
	 * Find the entry in a resource table with a given ID.
	 * The input stream is expected to be positioned at the start of the table.
	 * The position if the stream after the function call is undefined.
	 *
	 * \return:
	 *   Highest order bit: 1 = points to another resource table
	 *                      0 = points to a resource leaf
	 *   Remaining 31 bits: Offset to the resource table / leaf relative to
	 *                      the directory start.
	 */
	static boost::uint32_t find_resource_entry(std::istream & is, boost::uint32_t id);
	
	static resource find_resource(std::istream & is, boost::uint32_t name,
	                              boost::uint32_t type = TypeData,
	                              boost::uint32_t language = Default);
	
	static bool get_file_version(std::istream & is);
	
};

bool pe_reader::header::load(std::istream & is) {
	
	is.seekg(2, std::ios_base::cur); // machine
	nsections = util::load<boost::uint16_t>(is);
	is.seekg(4 + 4 + 4, std::ios_base::cur); // creation time + symbol table offset + nbsymbols
	boost::uint16_t optional_header_size = util::load<boost::uint16_t>(is);
	is.seekg(2, std::ios_base::cur); // characteristics
	
	section_table_offset = boost::uint32_t(is.tellg()) + optional_header_size;
	
	// Skip the optional header.
	boost::uint16_t optional_header_magic = util::load<boost::uint16_t>(is);
	if(is.fail()) {
		return false;
	}
	if(optional_header_magic == 0x20b) { // PE32+
		is.seekg(106, std::ios_base::cur);
	} else {
		is.seekg(90, std::ios_base::cur);
	}
	
	boost::uint32_t ndirectories = util::load<boost::uint32_t>(is);
	if(is.fail() || ndirectories < 3) {
		return false;
	}
	const boost::uint32_t directory_header_size = 4 + 4; // address + size
	is.seekg(2 * directory_header_size, std::ios_base::cur);
	
	// Virtual memory address and size of the start of resource directory.
	resource_table_address = util::load<boost::uint32_t>(is);
	boost::uint32_t resource_size = util::load<boost::uint32_t>(is);
	if(is.fail() || !resource_table_address || !resource_size) {
		return false;
	}
	
	return true;
}

bool pe_reader::section_table::load(std::istream & is, const header & coff) {
	
	is.seekg(coff.section_table_offset);
	
	sections.resize(coff.nsections);
	
	BOOST_FOREACH(section & s, sections) {
		
		is.seekg(8, std::ios_base::cur); // name
		
		s.virtual_size = util::load<boost::uint32_t>(is);
		s.virtual_address = util::load<boost::uint32_t>(is);
		
		is.seekg(4, std::ios_base::cur); // raw size
		s.raw_address = util::load<boost::uint32_t>(is);
		
		// relocation addr + line number addr + relocation count
		// + line number count + characteristics
		is.seekg(4 + 4 + 2 + 2 + 4, std::ios_base::cur);
		
	}
	
	return !is.fail();
}

boost::uint32_t pe_reader::section_table::to_file_offset(boost::uint32_t address) {
	
	BOOST_FOREACH(const section & s, sections) {
		if(address >= s.virtual_address && address < s.virtual_address + s.virtual_size) {
			return address + s.raw_address - s.virtual_address;
		}
	}
	
	return 0;
}

bool pe_reader::get_resource_table(boost::uint32_t & entry, boost::uint32_t offset) {
	
	bool is_table = ((entry & (boost::uint32_t(1) << 31)) != 0);
	
	entry &= ~(1 << 31), entry += offset;
	
	return is_table;
}

boost::uint32_t pe_reader::find_resource_entry(std::istream & is, boost::uint32_t id) {
	
	// skip: characteristics + timestamp + major version + minor version
	if(is.seekg(4 + 4 + 2 + 2, std::ios_base::cur).fail()) {
		return 0;
	}
	
	// Number of named resource entries.
	boost::uint16_t nbnames = util::load<boost::uint16_t>(is);
	
	// Number of id resource entries.
	boost::uint16_t nbids = util::load<boost::uint16_t>(is);
	
	if(id == Default) {
		boost::uint32_t offset = util::load<boost::uint32_t>(is.seekg(4, std::ios_base::cur));
		return is.fail() ? 0 : offset;
	}
	
	// Ignore named resource entries.
	const boost::uint32_t entry_size = 4 + 4; // id / string address + offset
	if(is.seekg(nbnames * entry_size, std::ios_base::cur).fail()) {
		return 0;
	}
	
	for(size_t i = 0; i < nbids; i++) {
		
		boost::uint32_t entry_id = util::load<boost::uint32_t>(is);
		boost::uint32_t entry_offset = util::load<boost::uint32_t>(is);
		if(is.fail()) {
			return 0;
		}
		
		if(entry_id == id) {
			return entry_offset;
		}
		
	}
	
	return 0;
}

pe_reader::resource pe_reader::find_resource(std::istream & is, boost::uint32_t name,
                                             boost::uint32_t type,
                                             boost::uint32_t language) {
	
	resource result;
	result.offset = result.size = 0;
	
	header coff;
	if(!coff.load(is)) {
		return result;
	}
	
	section_table sections;
	if(!sections.load(is, coff)) {
		return result;
	}
	
	boost::uint32_t resource_offset = sections.to_file_offset(coff.resource_table_address);
	if(!resource_offset) {
		return result;
	}
	
	is.seekg(resource_offset);
	boost::uint32_t type_offset = find_resource_entry(is, type);
	if(!get_resource_table(type_offset, resource_offset)) {
		return result;
	}
	
	is.seekg(type_offset);
	boost::uint32_t name_offset = find_resource_entry(is, name);
	if(!get_resource_table(name_offset, resource_offset)) {
		return result;
	}
	
	is.seekg(name_offset);
	boost::uint32_t leaf_offset = find_resource_entry(is, language);
	if(!leaf_offset || get_resource_table(leaf_offset, resource_offset)) {
		return result;
	}
	
	// Virtual memory address and size of the resource data.
	is.seekg(leaf_offset);
	boost::uint32_t data_address = util::load<boost::uint32_t>(is);
	boost::uint32_t data_size = util::load<boost::uint32_t>(is);
	// ignore codepage and reserved word
	if(is.fail()) {
		return result;
	}
	
	boost::uint32_t data_offset = sections.to_file_offset(data_address);
	if(!data_offset) {
		return result;
	}
	
	result.offset = data_offset;
	result.size = data_size;
	
	return result;
}

bool pe_reader::get_file_version(std::istream & is) {
	
	resource res = find_resource(is, NameVersionInfo, TypeVersion);
	if(!res) {
		return false;
	}
	
	return skip_to_fixed_file_info<boost::uint16_t>(is, res.offset, 6);
}

} // anonymous namespace

exe_reader::resource exe_reader::find_resource(std::istream & is, boost::uint32_t name,
                                               boost::uint32_t type,
                                               boost::uint32_t language) {
	
	BinaryType bintype = determine_binary_type(is);
	switch(bintype) {
		case OS2Magic: return ne_reader::find_resource(is, name, type);
		case PEMagic:  return pe_reader::find_resource(is, name, type, language);
		default: {
			resource result;
			result.offset = result.size = 0;
			return result;
		}
	}
	
}

boost::uint64_t exe_reader::get_file_version(std::istream & is) {
	
	bool found = false;
	BinaryType bintype = determine_binary_type(is);
	switch(bintype) {
		case OS2Magic: found = ne_reader::get_file_version(is); break;
		case VXDMagic: found = le_reader::get_file_version(is); break;
		case PEMagic:  found = pe_reader::get_file_version(is); break;
		default: break;
	}
	if(!found) {
		return FileVersionUnknown;
	}
	
	boost::uint32_t magic = util::load<boost::uint32_t>(is);
	if(is.fail() || magic != 0xfeef04bd) {
		return FileVersionUnknown;
	}
	
	is.seekg(4, std::ios_base::cur); // skip struct version
	boost::uint32_t file_version_ms = util::load<boost::uint32_t>(is);
	boost::uint32_t file_version_ls = util::load<boost::uint32_t>(is);
	if(is.fail()) {
		return FileVersionUnknown;
	}
	
	return (boost::uint64_t(file_version_ms) << 32) | boost::uint64_t(file_version_ls);
}

} // namespace loader
```

## File: `src/loader/exereader.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Functions to find resources in Windows executables.
 */
#ifndef INNOEXTRACT_LOADER_EXEREADER_HPP
#define INNOEXTRACT_LOADER_EXEREADER_HPP

#include <istream>

#include <boost/cstdint.hpp>

namespace loader {

/*!
 * \brief Minimal NE/LE/PE parser that can find resources by ID in binary (exe/dll) files
 *
 * This implementation is optimized to look for exactly one resource.
 */
class exe_reader {
	
public:
	
	//! Position and size of a resource entry
	struct resource {
		
		boost::uint32_t offset; //!< File offset of the resource data in bytes
		
		boost::uint32_t size; //!< Size of the resource data in bytes
		
		operator bool() { return offset != 0; }
		bool operator!() { return offset == 0; }
		
	};
	
	enum resource_id {
		NameVersionInfo = 1,
		TypeCursor = 1,
		TypeBitmap = 2,
		TypeIcon = 3,
		TypeMenu = 4,
		TypeDialog = 5,
		TypeString = 6,
		TypeFontDir = 7,
		TypeFont = 8,
		TypeAccelerator = 9,
		TypeData = 10,
		TypeMessageTable = 11,
		TypeGroupCursor = 12,
		TypeGroupIcon = 14,
		TypeVersion = 16,
		TypeDlgInclude = 17,
		TypePlugPlay = 19,
		TypeVXD = 20,
		TypeAniCursor = 21,
		TypeAniIcon = 22,
		TypeHTML = 23,
		Default = boost::uint32_t(-1)
	};
	
	/*!
	 * \brief Find where a resource with a given ID is stored in a NE or PE binary.
	 *
	 * Resources are addressed using a (name, type, language) tuple.
	 *
	 * \param is       a seekable stream of the binary containing the resource
	 * \param name     the user-defined name of the resource
	 * \param type     the type of the resource
	 * \param language the localised variant of the resource
	 *
	 * \return the location of the resource or `(0, 0)` if the requested resource does not exist.
	 */
	static resource find_resource(std::istream & is, boost::uint32_t name,
	                              boost::uint32_t type = TypeData,
	                              boost::uint32_t language = Default);
	
	enum file_version {
		FileVersionUnknown = boost::uint64_t(-1)
	};
	
	/*!
	 * \brief Get the file version number of a NE, LE or PE binary.
	 *
	 * \param is a seekable stream of the binary file containing the resource
	 *
	 * \return the file version number or FileVersionUnknown.
	 */
	static boost::uint64_t get_file_version(std::istream & is);
	
};

} // namespace loader

#endif // INNOEXTRACT_LOADER_EXEREADER_HPP
```

## File: `src/loader/offsets.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "loader/offsets.hpp"

#include <cstring>
#include <limits>

#include <boost/cstdint.hpp>
#include <boost/static_assert.hpp>
#include <boost/range/size.hpp>

#include <stddef.h>

#include "crypto/crc32.hpp"
#include "loader/exereader.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/log.hpp"
#include "util/output.hpp"

namespace loader {

namespace {

struct setup_loader_version {
	
	unsigned char magic[12];
	
	// Earliest known version with that ID
	setup::version_constant version;
	
};

const setup_loader_version known_setup_loader_versions[] = {
	{ { 'r', 'D', 'l', 'P', 't', 'S', '0', '2', 0x87, 'e', 'V', 'x' },    INNO_VERSION(1, 2, 10) },
	{ { 'r', 'D', 'l', 'P', 't', 'S', '0', '4', 0x87, 'e', 'V', 'x' },    INNO_VERSION(4, 0,  0) },
	{ { 'r', 'D', 'l', 'P', 't', 'S', '0', '5', 0x87, 'e', 'V', 'x' },    INNO_VERSION(4, 0,  3) },
	{ { 'r', 'D', 'l', 'P', 't', 'S', '0', '6', 0x87, 'e', 'V', 'x' },    INNO_VERSION(4, 0, 10) },
	{ { 'r', 'D', 'l', 'P', 't', 'S', '0', '7', 0x87, 'e', 'V', 'x' },    INNO_VERSION(4, 1,  6) },
	{ { 'r', 'D', 'l', 'P', 't', 'S', 0xcd, 0xe6, 0xd7, '{', 0x0b, '*' }, INNO_VERSION(5, 1,  5) },
	{ { 'n', 'S', '5', 'W', '7', 'd', 'T', 0x83, 0xaa, 0x1b, 0x0f, 'j' }, INNO_VERSION(5, 1,  5) },
};

const int ResourceNameInstaller = 11111;

const boost::uint32_t SetupLoaderHeaderOffset = 0x30;
const boost::uint32_t SetupLoaderHeaderMagic = 0x6f6e6e49; // "Inno"

} // anonymous namespace

bool offsets::load_from_exe_file(std::istream & is) {
	
	is.seekg(SetupLoaderHeaderOffset);
	
	boost::uint32_t magic = util::load<boost::uint32_t>(is);
	if(is.fail() || magic != SetupLoaderHeaderMagic) {
		is.clear();
		return false;
	}
	
	debug("found Inno magic at " << print_hex(SetupLoaderHeaderOffset));
	
	found_magic = true;
	
	boost::uint32_t offset_table_offset = util::load<boost::uint32_t>(is);
	boost::uint32_t not_offset_table_offset = util::load<boost::uint32_t>(is);
	if(is.fail() || offset_table_offset != ~not_offset_table_offset) {
		is.clear();
		debug("header offset checksum: " << print_hex(not_offset_table_offset) << " != ~"
		                                 << print_hex(offset_table_offset));
		return false;
	}
	
	debug("found loader header at " << print_hex(offset_table_offset));
	
	return load_offsets_at(is, offset_table_offset);
}

bool offsets::load_from_exe_resource(std::istream & is) {
	
	exe_reader::resource resource = exe_reader::find_resource(is, ResourceNameInstaller);
	if(!resource) {
		is.clear();
		return false;
	}
	
	debug("found loader header resource at " << print_hex(resource.offset));
	
	found_magic = true;
	
	return load_offsets_at(is, resource.offset);
}

bool offsets::load_offsets_at(std::istream & is, boost::uint32_t pos) {
	
	if(is.seekg(pos).fail()) {
		is.clear();
		debug("could not seek to loader header");
		return false;
	}
	
	char magic[12];
	if(is.read(magic, std::streamsize(sizeof(magic))).fail()) {
		is.clear();
		debug("could not read loader header magic");
		return false;
	}
	
	setup::version_constant version = 0;
	for(size_t i = 0; i < size_t(boost::size(known_setup_loader_versions)); i++) {
		BOOST_STATIC_ASSERT(sizeof(known_setup_loader_versions[i].magic) == sizeof(magic));
		if(!memcmp(magic, known_setup_loader_versions[i].magic, sizeof(magic))) {
			version = known_setup_loader_versions[i].version;
			debug("found loader header magic version " << setup::version(version));
			break;
		}
	}
	if(!version) {
		log_warning << "Unexpected setup loader magic: " << print_hex(magic);
		version = std::numeric_limits<setup::version_constant>::max();
	}
	
	crypto::crc32 checksum;
	checksum.init();
	checksum.update(magic, sizeof(magic));
	
	if(version >= INNO_VERSION(5, 1,  5)) {
		boost::uint32_t revision = checksum.load<boost::uint32_t>(is);
		if(is.fail()) {
			is.clear();
			debug("could not read loader header revision");
			return false;
		} else if(revision != 1) {
			log_warning << "Unexpected setup loader revision: " << revision;
		}
	}
	
	(void)checksum.load<boost::uint32_t>(is);
	exe_offset = checksum.load<boost::uint32_t>(is);
	
	if(version >= INNO_VERSION(4, 1, 6)) {
		exe_compressed_size = 0;
	} else {
		exe_compressed_size = checksum.load<boost::uint32_t>(is);
	}
	
	exe_uncompressed_size = checksum.load<boost::uint32_t>(is);
	
	if(version >= INNO_VERSION(4, 0, 3)) {
		exe_checksum.type = crypto::CRC32;
		exe_checksum.crc32 = checksum.load<boost::uint32_t>(is);
	} else {
		exe_checksum.type = crypto::Adler32;
		exe_checksum.adler32 = checksum.load<boost::uint32_t>(is);
	}
	
	if(version >= INNO_VERSION(4, 0, 0)) {
		message_offset = 0;
	} else {
		message_offset = util::load<boost::uint32_t>(is);
	}
	
	header_offset = checksum.load<boost::uint32_t>(is);
	data_offset = checksum.load<boost::uint32_t>(is);
	
	if(is.fail()) {
		is.clear();
		debug("could not read loader header");
		return false;
	}
	
	if(version >= INNO_VERSION(4, 0, 10)) {
		boost::uint32_t expected = util::load<boost::uint32_t>(is);
		if(is.fail()) {
			is.clear();
			debug("could not read loader header checksum");
			return false;
		}
		if(checksum.finalize() != expected) {
			log_warning << "Setup loader checksum mismatch!";
		}
	}
	
	return true;
}

void offsets::load(std::istream & is) {
	
	found_magic = false;
	
	/*
	 * Try to load the offset table by following a pointer at a constant offset.
	 * This method of storing the offset table is used in versions before 5.1.5
	 */
	if(load_from_exe_file(is)) {
		return;
	}
	
	/*
	 * Try to load an offset table located in a PE/COFF (.exe) resource entry.
	 * This method of storing the offset table was introduced in version 5.1.5
	 */
	if(load_from_exe_resource(is)) {
		return;
	}
	
	/*
	 * If no offset table has been found, this must be an external setup-0.bin file.
	 * In that case, the setup headers start at the beginning of the file.
	 */
	
	exe_compressed_size = exe_uncompressed_size = exe_offset = 0; // No embedded setup exe.
	
	message_offset = 0; // No embedded messages.
	
	header_offset = 0; // Whole file contains just the setup headers.
	
	data_offset = 0; // No embedded setup data.
}

} // namespace loader
```

## File: `src/loader/offsets.hpp`
```
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Functions to find Inno Setup data inside an executable.
 */
#ifndef INNOEXTRACT_LOADER_OFFSETS_HPP
#define INNOEXTRACT_LOADER_OFFSETS_HPP

#include <iosfwd>

#include <boost/cstdint.hpp>

#include "crypto/checksum.hpp"

namespace loader {

/*!
 * Bootstrap data for Inno Setup installers
 *
 * This struct contains information used by the Inno Setup loader to bootstrap the installer.
 * Some of these values are not available for all Inno Setup versions
 *
 * Inno Setup versions before \c 5.1.5 simply stored a magic number and offset to this bootstrap
 * data at a fixed position (\c 0x30) in the .exe file.
 *
 * Alternatively, there is no stored bootstrap information and data is stored in external files
 * while the main setup files contains only the version and headers (header_offset is \c 0).
 *
 * Newer versions use a PE/COFF resource entry to store this bootstrap information.
 */
struct offsets {
	
	/*!
	 * True if we have some indication that this is an Inno Setup file
	 */
	bool found_magic;
	
	/*!
	 * Offset of compressed `setup.e32` (the actual installer code)
	 *
	 * A value of \c 0 means there is no setup.e32 embedded in this file
	 */
	boost::uint32_t exe_offset;
	
	/*!
	 * Size of `setup.e32` after compression, in bytes
	 *
	 * A value of \c 0 means the executable size is not known
	 */
	boost::uint32_t exe_compressed_size;
	
	//! Size of `setup.e32` before compression, in bytes
	boost::uint32_t exe_uncompressed_size;
	
	/*!
	 * Checksum of `setup.e32` before compression
	 *
	 * Currently this is either a \ref crypto::CRC32 or \ref crypto::Adler32 checksum.
	 */
	crypto::checksum exe_checksum;
	
	//! Offset of embedded setup messages
	boost::uint32_t message_offset;
	
	/*!
	 * Offset of embedded `setup-0.bin` data (the setup headers)
	 *
	 * This points to a \ref setup::version followed by two compressed blocks of
	 * headers (see \ref stream::block_reader).
	 *
	 * The headers are described by various structs in the \ref setup namespace.
	 * The first header is always \ref setup::header.
	 *
	 * Loading the version and headers is done in \ref setup::info.
	 */
	boost::uint32_t header_offset;
	
	/*!
	 * Offset of embedded `setup-1.bin` data
	 *
	 * A value of \c 0 means that the setup data is stored in seprarate files.
	 *
	 * \ref stream::slice_reader provides a uniform interface to this data, no matter if it
	 * is embedded or split into multiple external files (called slices).
	 *
	 * The data is made up of one or more compressed or uncompressed chunks
	 * (read by \ref stream::chunk_reader) which in turn each contain the raw data for one or more file.
	 *
	 * The layout of the chunks and files is stored in the \ref setup::data_entry headers
	 * while the \ref setup::file_entry headers provide the filenames and meta information.
	 */
	boost::uint32_t data_offset;
	
	/*!
	 * \brief Find the setup loader offsets in a file
	 *
	 * Finding the headers always works - if there is no bootstrap information we assume that
	 * this is a file containing only the version and headers.
	 *
	 * \param is a seekable stream of the main installer file. This should be the file
	 *           containing the headers, which is almost always the .exe file.
	 */
	void load(std::istream & is);
	
private:
	
	bool load_from_exe_file(std::istream & is);
	
	bool load_from_exe_resource(std::istream & is);
	
	bool load_offsets_at(std::istream & is, boost::uint32_t pos);
	
};

} // namespace loader

#endif // INNOEXTRACT_LOADER_OFFSETS_HPP
```

## File: `src/setup/component.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/component.hpp"

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/storedenum.hpp"

namespace setup {

namespace {

STORED_FLAGS_MAP(stored_component_flags_0,
	component_entry::Fixed,
	component_entry::Restart,
	component_entry::DisableNoUninstallWarning,
);

// starting with version 3.0.8
STORED_FLAGS_MAP(stored_component_flags_1,
	component_entry::Fixed,
	component_entry::Restart,
	component_entry::DisableNoUninstallWarning,
	component_entry::Exclusive,
);

// starting with version 4.2.3
STORED_FLAGS_MAP(stored_component_flags_2,
	component_entry::Fixed,
	component_entry::Restart,
	component_entry::DisableNoUninstallWarning,
	component_entry::Exclusive,
	component_entry::DontInheritCheck,
);

} // anonymous namespace

void component_entry::load(std::istream & is, const info & i) {
	
	is >> util::encoded_string(name, i.codepage);
	is >> util::encoded_string(description, i.codepage);
	is >> util::encoded_string(types, i.codepage);
	if(i.version >= INNO_VERSION(4, 0, 1)) {
		is >> util::encoded_string(languages, i.codepage);
	} else {
		languages.clear();
	}
	if(i.version >= INNO_VERSION(4, 0, 0) || (i.version.is_isx() && i.version >= INNO_VERSION(1, 3, 24))) {
		is >> util::encoded_string(check, i.codepage);
	} else {
		check.clear();
	}
	if(i.version >= INNO_VERSION(4, 0, 0)) {
		extra_disk_pace_required = util::load<boost::uint64_t>(is);
	} else {
		extra_disk_pace_required = util::load<boost::uint32_t>(is);
	}
	if(i.version >= INNO_VERSION(4, 0, 0) || (i.version.is_isx() && i.version >= INNO_VERSION(3, 0, 3))) {
		level = util::load<boost::int32_t>(is);
	} else {
		level = 0;
	}
	if(i.version >= INNO_VERSION(4, 0, 0) || (i.version.is_isx() && i.version >= INNO_VERSION(3, 0, 4))) {
		used = util::load_bool(is);
	} else {
		used = true;
	}
	
	winver.load(is, i.version);
	
	if(i.version >= INNO_VERSION(4, 2, 3)) {
		options = stored_flags<stored_component_flags_2>(is).get();
	} else if(i.version >= INNO_VERSION(3, 0, 8) ||
		        (i.version.is_isx() && i.version >= INNO_VERSION_EXT(3, 0, 6, 1))) {
		options = stored_flags<stored_component_flags_1>(is).get();
	} else {
		options = stored_flags<stored_component_flags_0>(is).get();
	}
	
	if(i.version >= INNO_VERSION(4, 0, 0)) {
		size = util::load<boost::uint64_t>(is);
	} else if(i.version >= INNO_VERSION(2, 0, 0) ||
		        (i.version.is_isx() && i.version >= INNO_VERSION(1, 3, 24))) {
		size = util::load<boost::uint32_t>(is);
	}
}

} // namespace setup

NAMES(setup::component_entry::flags, "Setup Component Option",
	"fixed",
	"restart",
	"disable no uninstall warning",
	"exclusive",
	"don't inherit check",
)
```

## File: `src/setup/component.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for setup components stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_COMPONENT_HPP
#define INNOEXTRACT_SETUP_COMPONENT_HPP

#include <string>
#include <iosfwd>

#include <boost/cstdint.hpp>

#include "setup/windows.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct info;

struct component_entry {
	
	// introduced in 2.0.0
	
	FLAGS(flags,
		Fixed,
		Restart,
		DisableNoUninstallWarning,
		Exclusive,
		DontInheritCheck
	);
	
	std::string name;
	std::string description;
	std::string types;
	std::string languages;
	std::string check;
	
	boost::uint64_t extra_disk_pace_required;
	
	int level;
	bool used;
	
	windows_version_range winver;
	
	flags options;
	
	boost::uint64_t size;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_FLAGS(setup::component_entry::flags)

#endif // INNOEXTRACT_SETUP_COMPONENT_HPP
```

## File: `src/setup/data.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/data.hpp"

#include <cstring>

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/log.hpp"
#include "util/output.hpp"
#include "util/storedenum.hpp"
#include "util/time.hpp"

namespace setup {

namespace {

STORED_ENUM_MAP(stored_sign_mode, data_entry::NoSetting,
	data_entry::NoSetting,
	data_entry::Yes,
	data_entry::Once,
	data_entry::Check,
);

} // anonymous namespace

void data_entry::load(std::istream & is, const info & i) {
	
	chunk.first_slice = util::load<boost::uint32_t>(is, i.version.bits());
	chunk.last_slice = util::load<boost::uint32_t>(is, i.version.bits());
	if(i.version < INNO_VERSION(4, 0, 0)) {
		if(chunk.first_slice < 1 || chunk.last_slice < 1) {
			log_warning << "Unexpected slice number: " << chunk.first_slice
			            << " to " << chunk.last_slice;
		} else {
			chunk.first_slice--, chunk.last_slice--;
		}
	}
	
	chunk.sort_offset = chunk.offset = util::load<boost::uint32_t>(is);
	
	if(i.version >= INNO_VERSION(4, 0, 1)) {
		file.offset = util::load<boost::uint64_t>(is);
	} else {
		file.offset = 0;
	}
	
	if(i.version >= INNO_VERSION(4, 0, 0)) {
		file.size = util::load<boost::uint64_t>(is);
		chunk.size = util::load<boost::uint64_t>(is);
	} else {
		file.size = util::load<boost::uint32_t>(is);
		chunk.size = util::load<boost::uint32_t>(is);
	}
	uncompressed_size = file.size;
	
	if(i.version >= INNO_VERSION(6, 4, 0)) {
		is.read(file.checksum.sha256, std::streamsize(sizeof(file.checksum.sha256)));
		file.checksum.type = crypto::SHA256;
	} else if(i.version >= INNO_VERSION(5, 3, 9)) {
		is.read(file.checksum.sha1, std::streamsize(sizeof(file.checksum.sha1)));
		file.checksum.type = crypto::SHA1;
	} else if(i.version >= INNO_VERSION(4, 2, 0)) {
		is.read(file.checksum.md5, std::streamsize(sizeof(file.checksum.md5)));
		file.checksum.type = crypto::MD5;
	} else if(i.version >= INNO_VERSION(4, 0, 1)) {
		file.checksum.crc32 = util::load<boost::uint32_t>(is);
		file.checksum.type = crypto::CRC32;
	} else {
		file.checksum.adler32 = util::load<boost::uint32_t>(is);
		file.checksum.type = crypto::Adler32;
	}
	
	if(i.version.bits() == 16) {
		
		// 16-bit installers use the FAT filetime format
		
		boost::uint16_t time = util::load<boost::uint16_t>(is);
		boost::uint16_t date = util::load<boost::uint16_t>(is);
		
		struct tm t;
		std::memset(&t, 0, sizeof(t));
		t.tm_sec  = util::get_bits(time,  0,  4) * 2;           // [0, 58]
		t.tm_min  = util::get_bits(time,  5, 10);               // [0, 59]
		t.tm_hour = util::get_bits(time, 11, 15);               // [0, 23]
		t.tm_mday = util::get_bits(date,  0,  4);               // [1, 31]
		t.tm_mon  = util::get_bits(date,  5,  8) - 1;           // [0, 11]
		t.tm_year = util::get_bits(date,  9, 15) + 1980 - 1900; // [80, 199]
		
		timestamp = util::parse_time(t);
		timestamp_nsec = 0;
		
	} else {
		
		// 32-bit installers use the Win32 FILETIME format
		
		boost::int64_t filetime = util::load<boost::int64_t>(is);
		
		static const boost::int64_t FiletimeOffset = 0x19DB1DED53E8000ll;
		if(filetime < FiletimeOffset) {
			log_warning << "Unexpected filetime: " << filetime;
		}
		filetime -= FiletimeOffset;
		
		timestamp = filetime / 10000000;
		timestamp_nsec = boost::uint32_t(filetime % 10000000) * 100;
		
	}
	
	boost::uint32_t file_version_ms = util::load<boost::uint32_t>(is);
	boost::uint32_t file_version_ls = util::load<boost::uint32_t>(is);
	file_version = (boost::uint64_t(file_version_ms) << 32)
	             |  boost::uint64_t(file_version_ls);
	
	options = 0;
	
	stored_flag_reader<flags> flagreader(is, i.version.bits());
	
	flagreader.add(VersionInfoValid);
	flagreader.add(VersionInfoNotValid);
	if(i.version >= INNO_VERSION(2, 0, 17) && i.version < INNO_VERSION(4, 0, 1)) {
		flagreader.add(BZipped);
	}
	if(i.version >= INNO_VERSION(4, 0, 10)) {
		flagreader.add(TimeStampInUTC);
	}
	if(i.version >= INNO_VERSION(4, 1, 0)) {
		flagreader.add(IsUninstallerExe);
	}
	if(i.version >= INNO_VERSION(4, 1, 8)) {
		flagreader.add(CallInstructionOptimized);
	}
	if(i.version >= INNO_VERSION(4, 2, 0)) {
		flagreader.add(Touch);
	}
	if(i.version >= INNO_VERSION(4, 2, 2)) {
		flagreader.add(ChunkEncrypted);
	}
	if(i.version >= INNO_VERSION(4, 2, 5)) {
		flagreader.add(ChunkCompressed);
	} else {
		options |= ChunkCompressed;
	}
	if(i.version >= INNO_VERSION(5, 1, 13)) {
		flagreader.add(SolidBreak);
	}
	if(i.version >= INNO_VERSION(5, 5, 7) && i.version < INNO_VERSION(6, 3, 0)) {
		// Actually added in Inno Setup 5.5.9 but the data version was not bumped
		flagreader.add(Sign);
		flagreader.add(SignOnce);
	}
	
	options |= flagreader.finalize();
	
	if(i.version >= INNO_VERSION(6, 3, 0)) {
		sign = stored_enum<stored_sign_mode>(is).get();
	} else if(options & SignOnce) {
		sign = Once;
	} else if(options & Sign) {
		sign = Yes;
	} else {
		sign = NoSetting;
	}
	
	if(options & ChunkCompressed) {
		chunk.compression = i.header.compression;
	} else {
		chunk.compression = stream::Stored;
	}
	if(options & BZipped) {
		options |= ChunkCompressed;
		chunk.compression = stream::BZip2;
	}
	
	if(options & ChunkEncrypted) {
		if(i.version >= INNO_VERSION(6, 4, 0)) {
			chunk.encryption = stream::XChaCha20;
		} else if(i.version >= INNO_VERSION(5, 3, 9)) {
			chunk.encryption = stream::ARC4_SHA1;
		} else {
			chunk.encryption = stream::ARC4_MD5;
		}
	} else {
		chunk.encryption = stream::Plaintext;
	}
	
	if(options & CallInstructionOptimized) {
		if(i.version < INNO_VERSION(5, 2, 0)) {
			file.filter = stream::InstructionFilter4108;
		} else if(i.version < INNO_VERSION(5, 3, 9)) {
			file.filter = stream::InstructionFilter5200;
		} else {
			file.filter = stream::InstructionFilter5309;
		}
	} else {
		file.filter = stream::NoFilter;
	}
}

} // namespace setup

NAMES(setup::data_entry::flags, "File Location Option",
	"version info valid",
	"version info not valid",
	"timestamp in UTC",
	"is uninstaller exe",
	"call instruction optimized",
	"touch",
	"chunk encrypted",
	"chunk compressed",
	"solid break",
	"sign",
	"sign once",
	"bzipped",
)

NAMES(setup::data_entry::sign_mode, "Sign Mode",
	"no setting",
	"yes",
	"once",
	"check",
)
```

## File: `src/setup/data.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for file content entries stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_DATA_HPP
#define INNOEXTRACT_SETUP_DATA_HPP

#include <stddef.h>
#include <iosfwd>

#include <boost/cstdint.hpp>

#include "crypto/checksum.hpp"
#include "stream/chunk.hpp"
#include "stream/file.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct info;

struct data_entry {
	
	FLAGS(flags,
		
		VersionInfoValid,
		VersionInfoNotValid,
		TimeStampInUTC,
		IsUninstallerExe,
		CallInstructionOptimized,
		Touch,
		ChunkEncrypted,
		ChunkCompressed,
		SolidBreak,
		Sign,
		SignOnce,
		
		// obsolete:
		BZipped
	);
	
	stream::chunk chunk;
	
	stream::file file;
	
	boost::uint64_t uncompressed_size;
	
	boost::int64_t timestamp;
	boost::uint32_t timestamp_nsec;
	
	boost::uint64_t file_version;
	
	flags options;
	
	enum sign_mode {
		NoSetting,
		Yes,
		Once,
		Check
	};
	sign_mode sign;
	
	/*!
	 * Load one data entry.
	 *
	 * \note This function may not be thread-safe on all operating systems.
	 */
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_FLAGS(setup::data_entry::flags)
NAMED_ENUM(setup::data_entry::sign_mode)

#endif // INNOEXTRACT_SETUP_DATA_HPP
```

## File: `src/setup/delete.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/delete.hpp"

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/storedenum.hpp"

namespace setup {

namespace {

STORED_ENUM_MAP(delete_target_type_map, delete_entry::Files,
	delete_entry::Files,
	delete_entry::FilesAndSubdirs,
	delete_entry::DirIfEmpty,
);

} // anonymous namespace

void delete_entry::load(std::istream & is, const info & i) {
	
	if(i.version < INNO_VERSION(1, 3, 0)) {
		(void)util::load<boost::uint32_t>(is); // uncompressed size of the entry
	}
	
	is >> util::encoded_string(name, i.codepage, i.header.lead_bytes);
	
	load_condition_data(is, i);
	
	load_version_data(is, i.version);
	
	type = stored_enum<delete_target_type_map>(is).get();
}

} // namespace setup

NAMES(setup::delete_entry::target_type, "Delete Type",
	"files",
	"files and subdirs",
	"dir if empty",
)
```

## File: `src/setup/delete.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for deletion entries stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_DELETE_HPP
#define INNOEXTRACT_SETUP_DELETE_HPP

#include <string>
#include <iosfwd>

#include "setup/item.hpp"
#include "util/enum.hpp"

namespace setup {

struct info;

struct delete_entry : public item {
	
	enum target_type {
		Files,
		FilesAndSubdirs,
		DirIfEmpty,
	};
	
	std::string name;
	
	target_type type;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_ENUM(setup::delete_entry::target_type)

#endif // INNOEXTRACT_SETUP_DELETE_HPP
```

## File: `src/setup/directory.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/directory.hpp"

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/storedenum.hpp"

namespace setup {

namespace {

STORED_FLAGS_MAP(stored_inno_directory_options_0,
	directory_entry::NeverUninstall,
	directory_entry::DeleteAfterInstall,
	directory_entry::AlwaysUninstall,
);

// starting with version 5.2.0
STORED_FLAGS_MAP(stored_inno_directory_options_1,
	directory_entry::NeverUninstall,
	directory_entry::DeleteAfterInstall,
	directory_entry::AlwaysUninstall,
	directory_entry::SetNtfsCompression,
	directory_entry::UnsetNtfsCompression,
);

} // anonymous namespace

void directory_entry::load(std::istream & is, const info & i) {
	
	if(i.version < INNO_VERSION(1, 3, 0)) {
		(void)util::load<boost::uint32_t>(is); // uncompressed size of the entry
	}
	
	is >> util::encoded_string(name, i.codepage, i.header.lead_bytes);
	
	load_condition_data(is, i);
	
	if(i.version >= INNO_VERSION(4, 0, 11) && i.version < INNO_VERSION(4, 1, 0)) {
		is >> util::binary_string(permissions);
	} else {
		permissions.clear();
	}
	
	if(i.version >= INNO_VERSION(2, 0, 11)) {
		attributes = util::load<boost::uint32_t>(is);
	} else {
		attributes = 0;
	}
	
	load_version_data(is, i.version);
	
	if(i.version >= INNO_VERSION(4, 1, 0)) {
		permission = util::load<boost::int16_t>(is);
	} else {
		permission = boost::int16_t(-1);
	}
	
	if(i.version >= INNO_VERSION(5, 2, 0)) {
		options = stored_flags<stored_inno_directory_options_1>(is).get();
	} else if(i.version.bits() != 16) {
		options = stored_flags<stored_inno_directory_options_0>(is).get();
	} else {
		options = stored_flags<stored_inno_directory_options_0, 16>(is).get();
	}
	
}

} // namespace setup

NAMES(setup::directory_entry::flags, "Directory Option",
	"never uninstall",
	"delete after install",
	"always uninstall",
	"set NTFS compression",
	"unset NTFS compression",
)
```

## File: `src/setup/directory.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for directory entries stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_DIRECTORY_HPP
#define INNOEXTRACT_SETUP_DIRECTORY_HPP

#include <string>
#include <iosfwd>

#include <boost/cstdint.hpp>

#include "setup/item.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct info;

struct directory_entry : public item {
	
	FLAGS(flags,
		NeverUninstall,
		DeleteAfterInstall,
		AlwaysUninstall,
		SetNtfsCompression,
		UnsetNtfsCompression
	);
	
	std::string name;
	std::string permissions;
	
	boost::uint32_t attributes;
	
	boost::int16_t permission; //!< index into the permission entry list
	
	flags options;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_FLAGS(setup::directory_entry::flags)

#endif // INNOEXTRACT_SETUP_DIRECTORY_HPP
```

## File: `src/setup/expression.cpp`
```cpp
/*
 * Copyright (C) 2012-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/expression.hpp"

#include <stddef.h>
#include <cstring>
#include <vector>
#include <stdexcept>

#include "util/log.hpp"

namespace setup {

namespace {

bool is_identifier_start(char c) {
	return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || c == '_' || c == '-';
}

bool is_identifier(char c) {
	return is_identifier_start(c) || (c >= '0' && c <= '9') || c == '\\';
}

struct evaluator {
	
	const std::string & test;
	const char * expr;
	
	enum token_type {
		end,
		op_or,
		op_and,
		op_not,
		paren_left,
		paren_right,
		identifier
	} token;
	const char * token_start;
	size_t token_length;
	
	evaluator(const std::string & expression, const std::string & variable)
		: test(variable), expr(expression.c_str()), token(end) { }
	
	token_type next() {
		
		// Ignore whitespace
		while(*expr > 0 && *expr <= 32) {
			expr++;
		}
		
		if(!*expr) {
			return (token = end);
			
		} else if(*expr == '(') {
			return (expr++, token = paren_left);
			
		} else if(*expr == ')') {
			return (expr++, token = paren_right);
			
		} else if(is_identifier_start(*expr)) {
			
			const char * start = expr++;
			while(is_identifier(*expr)) {
				expr++;
			}
			
			if(expr - start == 3 && !memcmp(start, "not", 3)) {
				return (token = op_not);
			} else if(expr - start == 3 && !memcmp(start, "and", 3)) {
				return (token = op_and);
			} else if(expr - start == 2 && !memcmp(start, "or", 2)) {
				return (token = op_or);
			}
			
			token_start = start;
			token_length = size_t(expr - start);
			return (token = identifier);
			
		} else {
			throw std::runtime_error(std::string("unexpected symbol: ") + *expr);
		}
	}
	
	bool eval_identifier(bool lazy) {
		bool result = lazy || test.compare(0, std::string::npos, token_start, token_length) == 0;
		next();
		return result;
	}
	
	bool eval_factor(bool lazy) {
		if(token == paren_left) {
			next();
			bool result = eval_expression(lazy);
			if(token != paren_right) {
				throw std::runtime_error("expected closing parenthesis");
			}
			next();
			return result;
		} else if(token == op_not) {
			next();
			return !eval_factor(lazy);
		} else if(token == identifier) {
			return eval_identifier(lazy);
		} else {
			throw std::runtime_error("unexpected token");
		}
	}
	
	bool eval_term(bool lazy) {
		bool result = eval_factor(lazy);
		while(token == op_and) {
			next();
			result = eval_factor(lazy || !result) && result;
		}
		return result;
	}
	
	bool eval_expression(bool lazy, bool inner = true) {
		bool result = eval_term(lazy);
		if(result && !inner) {
			return result;
		}
		while(token == op_or || token == identifier) {
			if(token == op_or) {
				next();
			}
			result = eval_term(lazy || result) || result;
			if(result && !inner) {
				return result;
			}
		}
		return result;
	}
	
	bool eval() {
		next();
		return eval_expression(false, false);
	}
	
};

} // anonymous namespace

bool expression_match(const std::string & test, const std::string & expression) {
	try {
		return evaluator(expression, test).eval();
	} catch(const std::runtime_error & error) {
		log_warning << "Error evaluating \"" << expression << "\": " << error.what();
		return true;
	}
}

bool is_simple_expression(const std::string & expression) {
	if(expression.empty()) {
		return true;
	}
	const char * c = expression.c_str();
	if(!is_identifier_start(*c)) {
		return false;
	}
	while(*c) {
		if(!is_identifier(*c)) {
			return false;
		}
		c++;
	}
	return true;
}

} // namespace setup
```

## File: `src/setup/expression.hpp`
```
/*
 * Copyright (C) 2012-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Functions to evaluation Inno Setup boolean expressions.
 */
#ifndef INNOEXTRACT_SETUP_EXPRESSION_HPP
#define INNOEXTRACT_SETUP_EXPRESSION_HPP

#include <string>

namespace setup {

/*
 * Determine if the given expression is satisfied with (only) the given test variable set to true
 */
bool expression_match(const std::string & test, const std::string & expression);

bool is_simple_expression(const std::string & expression);

} // namespace setup

#endif // INNOEXTRACT_SETUP_EXPRESSION_HPP
```

## File: `src/setup/file.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/file.hpp"

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/log.hpp"
#include "util/storedenum.hpp"

namespace setup {

namespace {

enum file_copy_mode {
	cmNormal,
	cmIfDoesntExist,
	cmAlwaysOverwrite,
	cmAlwaysSkipIfSameOrOlder,
};

STORED_ENUM_MAP(stored_file_copy_mode, cmNormal,
	cmNormal,
	cmIfDoesntExist,
	cmAlwaysOverwrite,
	cmAlwaysSkipIfSameOrOlder,
);

STORED_ENUM_MAP(stored_file_type_0, file_entry::UserFile,
	file_entry::UserFile,
	file_entry::UninstExe,
);

// win32, before 5.0.0
STORED_ENUM_MAP(stored_file_type_1, file_entry::UserFile,
	file_entry::UserFile,
	file_entry::UninstExe,
	file_entry::RegSvrExe,
);

} // anonymous namespace

} // namespace setup

NAMED_ENUM(setup::file_copy_mode)

NAMES(setup::file_copy_mode, "File Copy Mode",
	"normal",
	"if doesn't exist",
	"always overwrite",
	"always skip if same or older",
)

namespace setup {

void file_entry::load(std::istream & is, const info & i) {
	
	USE_ENUM_NAMES(file_copy_mode)
	
	options = 0;
	
	if(i.version < INNO_VERSION(1, 3, 0)) {
		(void)util::load<boost::uint32_t>(is); // uncompressed size of the entry
	}
	
	is >> util::encoded_string(source, i.codepage, i.header.lead_bytes);
	is >> util::encoded_string(destination, i.codepage, i.header.lead_bytes);
	is >> util::encoded_string(install_font_name, i.codepage, i.header.lead_bytes);
	if(i.version >= INNO_VERSION(5, 2, 5)) {
		is >> util::encoded_string(strong_assembly_name, i.codepage, i.header.lead_bytes);
	} else {
		strong_assembly_name.clear();
	}
	
	load_condition_data(is, i);
	
	load_version_data(is, i.version);
	
	location = util::load<boost::uint32_t>(is, i.version.bits());
	attributes = util::load<boost::uint32_t>(is, i.version.bits());
	external_size = (i.version >= INNO_VERSION(4, 0, 0)) ? util::load<boost::uint64_t>(is)
	                                                     : util::load<boost::uint32_t>(is);
	
	if(i.version < INNO_VERSION(3, 0, 5)) {
		file_copy_mode copyMode = stored_enum<stored_file_copy_mode>(is).get();
		switch(copyMode) {
			case cmNormal: options |= PromptIfOlder; break;
			case cmIfDoesntExist: options |= OnlyIfDoesntExist | PromptIfOlder; break;
			case cmAlwaysOverwrite: options |= IgnoreVersion | PromptIfOlder; break;
			case cmAlwaysSkipIfSameOrOlder: break;
		}
	}
	
	if(i.version >= INNO_VERSION(4, 1, 0)) {
		permission = util::load<boost::int16_t>(is);
	} else {
		permission = boost::int16_t(-1);
	}
	
	stored_flag_reader<flags> flagreader(is, i.version.bits());
	
	flagreader.add(ConfirmOverwrite);
	flagreader.add(NeverUninstall);
	flagreader.add(RestartReplace);
	flagreader.add(DeleteAfterInstall);
	if(i.version.bits() != 16) {
		flagreader.add(RegisterServer);
		flagreader.add(RegisterTypeLib);
		flagreader.add(SharedFile);
	}
	if(i.version < INNO_VERSION(2, 0, 0) && !i.version.is_isx()) {
		flagreader.add(IsReadmeFile);
	}
	flagreader.add(CompareTimeStamp);
	flagreader.add(FontIsNotTrueType);
	if(i.version >= INNO_VERSION(1, 2, 5)) {
		flagreader.add(SkipIfSourceDoesntExist);
	}
	if(i.version >= INNO_VERSION(1, 2, 6)) {
		flagreader.add(OverwriteReadOnly);
	}
	if(i.version >= INNO_VERSION(1, 3, 21)) {
		flagreader.add(OverwriteSameVersion);
		flagreader.add(CustomDestName);
	}
	if(i.version >= INNO_VERSION(1, 3, 25)) {
		flagreader.add(OnlyIfDestFileExists);
	}
	if(i.version >= INNO_VERSION(2, 0, 5)) {
		flagreader.add(NoRegError);
	}
	if(i.version >= INNO_VERSION(3, 0, 1)) {
		flagreader.add(UninsRestartDelete);
	}
	if(i.version >= INNO_VERSION(3, 0, 5)) {
		flagreader.add(OnlyIfDoesntExist);
		flagreader.add(IgnoreVersion);
		flagreader.add(PromptIfOlder);
	}
	if(i.version >= INNO_VERSION(4, 0, 0) ||
	   (i.version.is_isx() && i.version >= INNO_VERSION_EXT(3, 0, 6, 1))) {
		flagreader.add(DontCopy);
	}
	if(i.version >= INNO_VERSION(4, 0, 5)) {
		flagreader.add(UninsRemoveReadOnly);
	}
	if(i.version >= INNO_VERSION(4, 1, 8)) {
		flagreader.add(RecurseSubDirsExternal);
	}
	if(i.version >= INNO_VERSION(4, 2, 1)) {
		flagreader.add(ReplaceSameVersionIfContentsDiffer);
	}
	if(i.version >= INNO_VERSION(4, 2, 5)) {
		flagreader.add(DontVerifyChecksum);
	}
	if(i.version >= INNO_VERSION(5, 0, 3)) {
		flagreader.add(UninsNoSharedFilePrompt);
	}
	if(i.version >= INNO_VERSION(5, 1, 0)) {
		flagreader.add(CreateAllSubDirs);
	}
	if(i.version >= INNO_VERSION(5, 1, 2)) {
		flagreader.add(Bits32);
		flagreader.add(Bits64);
	}
	if(i.version >= INNO_VERSION(5, 2, 0)) {
		flagreader.add(ExternalSizePreset);
		flagreader.add(SetNtfsCompression);
		flagreader.add(UnsetNtfsCompression);
	}
	if(i.version >= INNO_VERSION(5, 2, 5)) {
		flagreader.add(GacInstall);
	}
	
	options |= flagreader.finalize();
	
	if(i.version.bits() == 16 || i.version >= INNO_VERSION(5, 0, 0)) {
		type = stored_enum<stored_file_type_0>(is).get();
	} else {
		type = stored_enum<stored_file_type_1>(is).get();
	}
	
	additional_locations.clear();
	checksum.type = crypto::None;
	size = 0;
	
}

} // namespace setup

NAMES(setup::file_entry::flags, "File Option",
	"confirm overwrite",
	"never uninstall",
	"restart replace",
	"delete after install",
	"register server",
	"register type lib",
	"shared file",
	"compare timestamp",
	"font isn't truetype",
	"skip if source doesn't exist",
	"overwrite readonly",
	"overwrite same version",
	"custom destination name",
	"only if destination exists",
	"no reg error",
	"uninstall restart delete",
	"only if doesn't exist",
	"ignore version",
	"prompt if older",
	"don't copy",
	"uninstall remove readonly",
	"recurse subdirectories external",
	"replace same version if contents differ",
	"don't verify checksum",
	"uninstall no shared file prompt",
	"create all sub dirs",
	"32 bit",
	"64 bit",
	"external size preset",
	"set ntfs compression",
	"unset ntfs compression",
	"gac install",
	"readme",
)

NAMES(setup::file_entry::file_type, "File Entry Type",
	"user file",
	"uninstaller exe",
	"reg server exe",
)
```

## File: `src/setup/file.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for file entries stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_FILE_HPP
#define INNOEXTRACT_SETUP_FILE_HPP

#include <string>
#include <iosfwd>
#include <vector>

#include <boost/cstdint.hpp>

#include "crypto/checksum.hpp"
#include "setup/item.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct info;

struct file_entry : public item {
	
	FLAGS(flags,
		
		ConfirmOverwrite,
		NeverUninstall,
		RestartReplace,
		DeleteAfterInstall,
		RegisterServer,
		RegisterTypeLib,
		SharedFile,
		CompareTimeStamp,
		FontIsNotTrueType,
		SkipIfSourceDoesntExist,
		OverwriteReadOnly,
		OverwriteSameVersion,
		CustomDestName,
		OnlyIfDestFileExists,
		NoRegError,
		UninsRestartDelete,
		OnlyIfDoesntExist,
		IgnoreVersion,
		PromptIfOlder,
		DontCopy,
		UninsRemoveReadOnly,
		RecurseSubDirsExternal,
		ReplaceSameVersionIfContentsDiffer,
		DontVerifyChecksum,
		UninsNoSharedFilePrompt,
		CreateAllSubDirs,
		Bits32,
		Bits64,
		ExternalSizePreset,
		SetNtfsCompression,
		UnsetNtfsCompression,
		GacInstall,
		
		// obsolete options:
		IsReadmeFile
	);
	
	enum file_type {
		UserFile,
		UninstExe,
		RegSvrExe,
	};
	
	enum file_attributes {
		ReadOnly = 0x1
	};
	
	std::string source;
	std::string destination;
	std::string install_font_name;
	std::string strong_assembly_name;
	
	boost::uint32_t location; //!< index into the data entry list
	boost::uint32_t attributes;
	boost::uint64_t external_size;
	
	boost::int16_t permission; //!< index into the permission entry list
	
	flags options;
	
	file_type type;
	
	// Information about GOG Galaxy multi-part files
	// These are not used in normal Inno Setup installers
	std::vector<boost::uint32_t> additional_locations;
	crypto::checksum checksum;
	boost::uint64_t size;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_FLAGS(setup::file_entry::flags)
NAMED_ENUM(setup::file_entry::file_type)

#endif // INNOEXTRACT_SETUP_FILE_HPP
```

## File: `src/setup/filename.cpp`
```cpp
/*
 * Copyright (C) 2012-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/filename.hpp"

#include <stddef.h>
#include <algorithm>
#include <cctype>

namespace setup {

namespace {

//! Check for separators in input paths.
struct is_path_separator {
	bool operator()(char c) {
		return (c == '\\' || c == '/');
	}
};

struct is_unsafe_path_char {
	bool operator()(char c) {
		if(static_cast<unsigned char>(c) < 32) {
			return true;
		}
		switch(c) {
			case '<': return true;
			case '>': return true;
			case ':': return true;
			case '"': return true;
			case '|': return true;
			case '?': return true;
			case '*': return true;
			default:  return false;
		}
	}
};

std::string replace_unsafe_chars(const std::string & str) {
	std::string result;
	result.resize(str.size());
	std::replace_copy_if(str.begin(), str.end(), result.begin(), is_unsafe_path_char(), '$');
	return result;
}

} // anonymous namespace

std::string filename_map::lookup(const std::string & key) const {
	std::map<std::string, std::string>::const_iterator i = find(key);
	return (i == end()) ? replace_unsafe_chars(key) : i->second;
}

std::string filename_map::expand_variables(it & begin, it end, bool close) const {
	
	std::string result;
	result.reserve(size_t(end - begin));
	
	while(begin != end) {
		
		// Flush everything before the next bracket
		it pos = begin;
		while(pos != end && *pos != '{' && *pos != '}') {
			++pos;
		}
		ptrdiff_t obegin = ptrdiff_t(result.size());
		result.append(begin, pos);
		std::replace_copy_if(result.begin() + obegin, result.end(), result.begin() + obegin,
		                     is_unsafe_path_char(), '$');
		begin = pos;
		
		if(pos == end) {
			// No more variables or escape sequences
			break;
		}
		
		begin++;
		
		if(close && *pos == '}') {
			// Current context closed
			break;
		}
		
		if(!close && *pos == '}') {
			// literal '}' character
			result.push_back('}');
			continue;
		}
		
		// '{{' escape sequence
		if(begin != end && *begin == '{') {
			result.push_back('{');
			begin++;
			continue;
		}
		
		// Recursively expand variables until we reach the end of this context
		result.append(lookup(expand_variables(begin, end, true)));
	}
	
	return result;
}

std::string filename_map::shorten_path(const std::string & path) {
	
	std::string result;
	result.reserve(path.size());
	
	it begin = path.begin();
	it end = path.end();
	while(begin != end) {
		
		it s_begin = begin;
		it s_end = std::find_if(begin, end, is_path_separator());
		begin = (s_end == end) ? end : (s_end + 1);
		
		size_t segment_length = size_t(s_end - s_begin);
		
		// Empty segment - ignore
		if(segment_length == 0) {
			continue;
		}
		
		// '.' segment - ignore
		if(segment_length == 1 && *s_begin == '.') {
			continue;
		}
		
		// '..' segment - backtrace in result path
		if(segment_length == 2 && *s_begin == '.' && *(s_begin + 1) == '.') {
			size_t last_sep = result.find_last_of(path_sep);
			if(last_sep == std::string::npos) {
				last_sep = 0;
			}
			result.resize(last_sep);
			continue;
		}
		
		// Normal segment - append to the result path
		if(!result.empty()) {
			result.push_back(path_sep);
		}
		result.append(s_begin, s_end);
		
	}
	
	return result;
}

std::string filename_map::convert(std::string path) const {
	
	// Convert paths to lower-case if requested
	if(lowercase) {
		std::transform(path.begin(), path.end(), path.begin(), ::tolower);
	}
	
	// Don't expand variables if requested
	if(!expand) {
		return path;
	}
	
	it begin = path.begin();
	std::string expanded = expand_variables(begin, path.end());
	
	return shorten_path(expanded);
}

} // namespace setup
```

## File: `src/setup/filename.hpp`
```
/*
 * Copyright (C) 2012-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Map for converting between stored filenames and output filenames.
 */
#ifndef INNOEXTRACT_SETUP_FILENAME_HPP
#define INNOEXTRACT_SETUP_FILENAME_HPP

#include <string>
#include <map>

namespace setup {

//! Separator to use for output paths.
#if defined(_WIN32)
static const char path_sep = '\\';
#else
static const char path_sep = '/';
#endif

/*!
 * Map to convert between raw windows file paths stored in the setup file (which can
 * contain variables) and output filenames.
 */
class filename_map : public std::map<std::string, std::string> {
	
	std::string lookup(const std::string & key) const;
	
	bool lowercase;
	bool expand;
	
	typedef std::string::const_iterator it;
	
	std::string expand_variables(it & begin, it end, bool close = false) const;
	static std::string shorten_path(const std::string & path);
	
public:
	
	filename_map() : lowercase(false), expand(false) { }
	
	std::string convert(std::string path) const;
	
	//! Set if paths should be converted to lower-case.
	void set_lowercase(bool enable) { lowercase = enable; }
	
	//! Set if paths should be converted to lower-case.
	bool is_lowercase() const { return lowercase; }
	
	//! Set if variables should be expanded and path separators converted.
	void set_expand(bool enable) { expand = enable; }
	
};

} // namespace setup

#endif // INNOEXTRACT_SETUP_FILENAME_HPP
```

## File: `src/setup/header.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/header.hpp"

#include <cstdio>
#include <cstring>

#include <boost/static_assert.hpp>

#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/storedenum.hpp"

namespace setup {

namespace {

STORED_ENUM_MAP(stored_alpha_format, header::AlphaIgnored,
	header::AlphaIgnored,
	header::AlphaDefined,
	header::AlphaPremultiplied
);

STORED_ENUM_MAP(stored_install_verbosity, header::NormalInstallMode,
	header::NormalInstallMode,
	header::SilentInstallMode,
	header::VerySilentInstallMode
);

STORED_ENUM_MAP(stored_log_mode, header::AppendLog,
	header::AppendLog,
	header::NewLog,
	header::OverwriteLog
);

STORED_ENUM_MAP(stored_setup_style, header::ClassicStyle,
	header::ClassicStyle,
	header::ModernStyle
);

STORED_ENUM_MAP(stored_bool_auto_no_yes, header::Auto,
	header::Auto,
	header::No,
	header::Yes
);

// pre- 5.3.7
STORED_ENUM_MAP(stored_privileges_0, header::NoPrivileges,
	header::NoPrivileges,
	header::PowerUserPrivileges,
	header::AdminPriviliges,
);

// post- 5.3.7
STORED_ENUM_MAP(stored_privileges_1, header::NoPrivileges,
	header::NoPrivileges,
	header::PowerUserPrivileges,
	header::AdminPriviliges,
	header::LowestPrivileges
);

STORED_ENUM_MAP(stored_bool_yes_no_auto, header::Yes,
	header::Yes,
	header::No,
	header::Auto
);

STORED_ENUM_MAP(stored_language_detection_method, header::UILanguage,
	header::UILanguage,
	header::LocaleLanguage,
	header::NoLanguageDetection
);

STORED_FLAGS_MAP(stored_architectures_0,
	header::ArchitectureUnknown,
	header::X86,
	header::Amd64,
	header::IA64
);

STORED_FLAGS_MAP(stored_architectures_1,
	header::ArchitectureUnknown,
	header::X86,
	header::Amd64,
	header::IA64,
	header::ARM64,
);

// pre-4.2.5
STORED_ENUM_MAP(stored_compression_method_0, stream::UnknownCompression,
	stream::Zlib,
	stream::BZip2,
	stream::LZMA1
);

// 4.2.5
STORED_ENUM_MAP(stored_compression_method_1, stream::UnknownCompression,
	stream::Stored,
	stream::BZip2,
	stream::LZMA1
);

// [4.2.6 5.3.9)
STORED_ENUM_MAP(stored_compression_method_2, stream::UnknownCompression,
	stream::Stored,
	stream::Zlib,
	stream::BZip2,
	stream::LZMA1
);

// 5.3.9+
STORED_ENUM_MAP(stored_compression_method_3, stream::UnknownCompression,
	stream::Stored,
	stream::Zlib,
	stream::BZip2,
	stream::LZMA1,
	stream::LZMA2
);

// 6.0.0+
STORED_FLAGS_MAP(stored_privileges_required_overrides,
	header::Commandline,
	header::Dialog
);

} // anonymous namespace

void header::load(std::istream & is, const version & version) {
	
	options = 0;
	
	if(version < INNO_VERSION(1, 3, 0)) {
		(void)util::load<boost::uint32_t>(is); // uncompressed size of the setup header
	}
	
	is >> util::binary_string(app_name);
	is >> util::binary_string(app_versioned_name);
	if(version >= INNO_VERSION(1, 3, 0)) {
		is >> util::binary_string(app_id);
	} else {
		app_id.clear();
	}
	is >> util::binary_string(app_copyright);
	if(version >= INNO_VERSION(1, 3, 0)) {
		is >> util::binary_string(app_publisher);
		is >> util::binary_string(app_publisher_url);
	} else {
		app_publisher.clear(), app_publisher_url.clear();
	}
	if(version >= INNO_VERSION(5, 1, 13)) {
		is >> util::binary_string(app_support_phone);
	} else {
		app_support_phone.clear();
	}
	if(version >= INNO_VERSION(1, 3, 0)) {
		is >> util::binary_string(app_support_url);
		is >> util::binary_string(app_updates_url);
		is >> util::binary_string(app_version);
	} else {
		app_support_url.clear(), app_updates_url.clear(), app_version.clear();
	}
	is >> util::binary_string(default_dir_name);
	is >> util::binary_string(default_group_name);
	if(version < INNO_VERSION(3, 0, 0)) {
		is >> util::ansi_string(uninstall_icon_name);
	} else {
		uninstall_icon_name.clear();
	}
	is >> util::binary_string(base_filename);
	if(version >= INNO_VERSION(1, 3, 0) && version < INNO_VERSION(5, 2, 5)) {
		is >> util::ansi_string(license_text);
		is >> util::ansi_string(info_before);
		is >> util::ansi_string(info_after);
	} else {
		license_text.clear(), info_before.clear(), info_after.clear();
	}
	if(version >= INNO_VERSION(1, 3, 3)) {
		is >> util::binary_string(uninstall_files_dir);
	} else {
		uninstall_files_dir.clear();
	}
	if(version >= INNO_VERSION(1, 3, 6)) {
		is >> util::binary_string(uninstall_name);
		is >> util::binary_string(uninstall_icon);
	} else {
		uninstall_name.clear(), uninstall_icon.clear();
	}
	if(version >= INNO_VERSION(1, 3, 14)) {
		is >> util::binary_string(app_mutex);
	} else {
		app_mutex.clear();
	}
	if(version >= INNO_VERSION(3, 0, 0)) {
		is >> util::binary_string(default_user_name);
		is >> util::binary_string(default_user_organisation);
	} else {
		default_user_name.clear(), default_user_organisation.clear();
	}
	if(version >= INNO_VERSION(4, 0, 0) || (version.is_isx() && version >= INNO_VERSION_EXT(3, 0, 6, 1))) {
		is >> util::binary_string(default_serial);
	} else {
		default_serial.clear();
	}
	if((version >= INNO_VERSION(4, 0, 0) && version < INNO_VERSION(5, 2, 5)) ||
	   (version.is_isx() && version >= INNO_VERSION(1, 3, 24))) {
		is >> util::binary_string(compiled_code);
	} else {
		compiled_code.clear();
	}
	if(version >= INNO_VERSION(4, 2, 4)) {
		is >> util::binary_string(app_readme_file);
		is >> util::binary_string(app_contact);
		is >> util::binary_string(app_comments);
		is >> util::binary_string(app_modify_path);
	} else {
		app_readme_file.clear(), app_contact.clear();
		app_comments.clear(), app_modify_path.clear();
	}
	if(version >= INNO_VERSION(5, 3, 8)) {
		is >> util::binary_string(create_uninstall_registry_key);
	} else {
		create_uninstall_registry_key.clear();
	}
	if(version >= INNO_VERSION(5, 3, 10)) {
		is >> util::binary_string(uninstallable);
	} else {
		uninstallable.clear();
	}
	if(version >= INNO_VERSION(5, 5, 0)) {
		is >> util::binary_string(close_applications_filter);
	} else {
		close_applications_filter.clear();
	}
	if(version >= INNO_VERSION(5, 5, 6)) {
		is >> util::binary_string(setup_mutex);
	} else {
		setup_mutex.clear();
	}
	if(version >= INNO_VERSION(5, 6, 1)) {
		is >> util::binary_string(changes_environment);
		is >> util::binary_string(changes_associations);
	} else {
		changes_environment.clear();
		changes_associations.clear();
	}
	if(version >= INNO_VERSION(6, 3, 0)) {
		// Valid architectures: 'Unknown', 'x86', 'x64', 'Arm32', 'Arm64'
		is >> util::binary_string(architectures_allowed_expr);
		is >> util::binary_string(architectures_installed_in_64bit_mode_expr);
	}
	if(version >= INNO_VERSION(5, 2, 5)) {
		is >> util::ansi_string(license_text);
		is >> util::ansi_string(info_before);
		is >> util::ansi_string(info_after);
	}
	if(version >= INNO_VERSION(5, 2, 1) && version < INNO_VERSION(5, 3, 10)) {
		is >> util::binary_string(uninstaller_signature);
	} else {
		uninstaller_signature.clear();
	}
	if(version >= INNO_VERSION(5, 2, 5)) {
		is >> util::binary_string(compiled_code);
	}
	
	if(version >= INNO_VERSION(2, 0, 6) && !version.is_unicode()) {
		lead_bytes = stored_char_set(is);
	} else {
		lead_bytes = 0;
	}
	
	if(version >= INNO_VERSION(4, 0, 0)) {
		language_count = util::load<boost::uint32_t>(is);
	} else if(version >= INNO_VERSION(2, 0, 1)) {
		language_count = 1;
	} else {
		language_count = 0;
	}
	
	if(version >= INNO_VERSION(4, 2, 1)) {
		message_count = util::load<boost::uint32_t>(is);
	} else {
		message_count = 0;
	}
	
	if(version >= INNO_VERSION(4, 1, 0)) {
		permission_count = util::load<boost::uint32_t>(is);
	} else {
		permission_count = 0;
	}
	
	if(version >= INNO_VERSION(2, 0, 0) || version.is_isx()) {
		type_count = util::load<boost::uint32_t>(is);
		component_count = util::load<boost::uint32_t>(is);
	} else {
		type_count = 0, component_count = 0;
	}
	if(version >= INNO_VERSION(2, 0, 0) || (version.is_isx() && version >= INNO_VERSION(1, 3, 17))) {
		task_count = util::load<boost::uint32_t>(is);
	} else {
		task_count = 0;
	}
	
	directory_count = util::load<boost::uint32_t>(is, version.bits());
	file_count = util::load<boost::uint32_t>(is, version.bits());
	data_entry_count = util::load<boost::uint32_t>(is, version.bits());
	icon_count = util::load<boost::uint32_t>(is, version.bits());
	ini_entry_count = util::load<boost::uint32_t>(is, version.bits());
	registry_entry_count = util::load<boost::uint32_t>(is, version.bits());
	delete_entry_count = util::load<boost::uint32_t>(is, version.bits());
	uninstall_delete_entry_count = util::load<boost::uint32_t>(is, version.bits());
	run_entry_count = util::load<boost::uint32_t>(is, version.bits());
	uninstall_run_entry_count = util::load<boost::uint32_t>(is, version.bits());
	
	boost::int32_t license_size = 0;
	boost::int32_t info_before_size = 0;
	boost::int32_t info_after_size = 0;
	if(version < INNO_VERSION(1, 3, 0)) {
		license_size = util::load<boost::int32_t>(is, version.bits());
		info_before_size = util::load<boost::int32_t>(is, version.bits());
		info_after_size = util::load<boost::int32_t>(is, version.bits());
	}
	
	winver.load(is, version);
	
	if(version < INNO_VERSION_EXT(6, 4, 0, 1)) {
		back_color = util::load<boost::uint32_t>(is);
	} else {
		back_color = 0;
	}
	if(version >= INNO_VERSION(1, 3, 3) && version < INNO_VERSION_EXT(6, 4, 0, 1)) {
		back_color2 = util::load<boost::uint32_t>(is);
	} else {
		back_color2 = 0;
	}
	if(version < INNO_VERSION(5, 5, 7)) {
		image_back_color = util::load<boost::uint32_t>(is);
	} else {
		image_back_color = 0;
	}
	if((version >= INNO_VERSION(2, 0, 0) && version < INNO_VERSION(5, 0, 4)) || version.is_isx()) {
		small_image_back_color = util::load<boost::uint32_t>(is);
	} else {
		small_image_back_color = 0;
	}
	
	if(version >= INNO_VERSION(6, 0, 0)) {
		wizard_style = stored_enum<stored_setup_style>(is).get();
		wizard_resize_percent_x = util::load<boost::uint32_t>(is);
		wizard_resize_percent_y = util::load<boost::uint32_t>(is);
	} else {
		wizard_style = ClassicStyle;
		wizard_resize_percent_x = 0;
		wizard_resize_percent_y = 0;
	}
	
	if(version >= INNO_VERSION(5, 5, 7)) {
		image_alpha_format = stored_enum<stored_alpha_format>(is).get();
	} else {
		image_alpha_format = AlphaIgnored;
	}
	
	if(version >= INNO_VERSION(6, 4, 0)) {
		is.read(password.sha256, 4);
		password.type = crypto::PBKDF2_SHA256_XChaCha20;
	} else if(version >= INNO_VERSION(5, 3, 9)) {
		is.read(password.sha1, std::streamsize(sizeof(password.sha1)));
		password.type = crypto::SHA1;
	} else if(version >= INNO_VERSION(4, 2, 0)) {
		is.read(password.md5, std::streamsize(sizeof(password.md5)));
		password.type = crypto::MD5;
	} else {
		password.crc32 = util::load<boost::uint32_t>(is);
		password.type = crypto::CRC32;
	}
	if(version >= INNO_VERSION(6, 4, 0)) {
		password_salt.resize(44); // PBKDF2 salt + iteration count + ChaCha2 base nonce
		is.read(&password_salt[0], std::streamsize(password_salt.length()));
	} else if(version >= INNO_VERSION(4, 2, 2)) {
		password_salt.resize(8);
		is.read(&password_salt[0], std::streamsize(password_salt.length()));
		password_salt.insert(0, "PasswordCheckHash");
	} else {
		password_salt.clear();
	}
	
	if(version >= INNO_VERSION(4, 0, 0)) {
		extra_disk_space_required = util::load<boost::int64_t>(is);
		slices_per_disk = util::load<boost::uint32_t>(is);
	} else {
		extra_disk_space_required = util::load<boost::int32_t>(is);
		slices_per_disk = 1;
	}
	
	if((version >= INNO_VERSION(2, 0, 0) && version < INNO_VERSION(5, 0, 0)) ||
	   (version.is_isx() && version >= INNO_VERSION(1, 3, 4))) {
		install_mode = stored_enum<stored_install_verbosity>(is).get();
	} else {
		install_mode = NormalInstallMode;
	}
	
	if(version >= INNO_VERSION(1, 3, 0)) {
		uninstall_log_mode = stored_enum<stored_log_mode>(is).get();
	} else {
		uninstall_log_mode = NewLog;
	}
	
	if(version >= INNO_VERSION(5, 0, 0)) {
		uninstall_style = ModernStyle;
	} else if(version >= INNO_VERSION(2, 0, 0) || (version.is_isx() && version >= INNO_VERSION(1, 3, 13))) {
		uninstall_style = stored_enum<stored_setup_style>(is).get();
	} else {
		uninstall_style = ClassicStyle;
	}
	
	if(version >= INNO_VERSION(1, 3, 6)) {
		dir_exists_warning = stored_enum<stored_bool_auto_no_yes>(is).get();
	} else {
		dir_exists_warning = Auto;
	}
	
	if(version.is_isx() && version >= INNO_VERSION(2, 0, 10) && version < INNO_VERSION(3, 0, 0)) {
		boost::int32_t code_line_offset = util::load<boost::int32_t>(is);
		(void)code_line_offset;
	}
	
	if(version >= INNO_VERSION(3, 0, 0) && version < INNO_VERSION(3, 0, 3)) {
		auto_bool val = stored_enum<stored_bool_auto_no_yes>(is).get();
		switch(val) {
			case Yes: options |= AlwaysRestart; break;
			case Auto: options |= RestartIfNeededByRun; break;
			case No: break;
		}
	}
	
	if(version >= INNO_VERSION(5, 3, 7)) {
		privileges_required = stored_enum<stored_privileges_1>(is).get();
	} else if(version >= INNO_VERSION(3, 0, 4) || (version.is_isx() && version >= INNO_VERSION(3, 0, 3))) {
		privileges_required = stored_enum<stored_privileges_0>(is).get();
	}
	
	if(version >= INNO_VERSION(5, 7, 0)) {
		privileges_required_override_allowed = stored_flags<stored_privileges_required_overrides>(is).get();
	} else {
		privileges_required_override_allowed = 0;
	}
	
	if(version >= INNO_VERSION(4, 0, 10)) {
		show_language_dialog = stored_enum<stored_bool_yes_no_auto>(is).get();
		language_detection = stored_enum<stored_language_detection_method>(is).get();
	}
	
	if(version >= INNO_VERSION(5, 3, 9)) {
		compression = stored_enum<stored_compression_method_3>(is).get();
	} else if(version >= INNO_VERSION(4, 2, 6)) {
		compression = stored_enum<stored_compression_method_2>(is).get();
	} else if(version >= INNO_VERSION(4, 2, 5)) {
		compression = stored_enum<stored_compression_method_1>(is).get();
	} else if(version >= INNO_VERSION(4, 1, 5)) {
		compression = stored_enum<stored_compression_method_0>(is).get();
	}
	
	if(version >= INNO_VERSION(6, 3, 0)) {
		architectures_allowed = 0; // see architectures_allowed_expr
		architectures_installed_in_64bit_mode = 0; // see architectures_installed_in_64bit_mode_expr
	} else if(version >= INNO_VERSION(5, 6, 0)) {
		architectures_allowed = stored_flags<stored_architectures_1>(is).get();
		architectures_installed_in_64bit_mode = stored_flags<stored_architectures_1>(is).get();
	} else if(version >= INNO_VERSION(5, 1, 0)) {
		architectures_allowed = stored_flags<stored_architectures_0>(is).get();
		architectures_installed_in_64bit_mode = stored_flags<stored_architectures_0>(is).get();
	} else {
		architectures_allowed = architecture_types::all();
		architectures_installed_in_64bit_mode = architecture_types::all();
	}
	
	if(version >= INNO_VERSION(5, 2, 1) && version < INNO_VERSION(5, 3, 10)) {
		signed_uninstaller_original_size = util::load<boost::uint32_t>(is);
		signed_uninstaller_header_checksum = util::load<boost::uint32_t>(is);
	} else {
		signed_uninstaller_original_size = signed_uninstaller_header_checksum = 0;
	}
	
	if(version >= INNO_VERSION(5, 3, 3)) {
		disable_dir_page = stored_enum<stored_bool_auto_no_yes>(is).get();
		disable_program_group_page = stored_enum<stored_bool_auto_no_yes>(is).get();
	}
	
	if(version >= INNO_VERSION(5, 5, 0)) {
		uninstall_display_size = util::load<boost::uint64_t>(is);
	} else if(version >= INNO_VERSION(5, 3, 6)) {
		uninstall_display_size = util::load<boost::uint32_t>(is);
	} else {
		uninstall_display_size = 0;
	}
	
	if(version == INNO_VERSION_EXT(5, 3, 10, 1) ||
	   version == INNO_VERSION_EXT(5, 4,  2, 1) ||
	   version == INNO_VERSION_EXT(5, 5, 0, 1)) {
		/*
		 * This is needed to extract an Inno Setup variant (BlackBox v2?) that uses
		 * the 5.3.10, 5.4.2 or 5.5.0 (unicode) data version string while the format differs:
		 * The language entries are off by one byte and the EncryptionUsed flag
		 * gets set while there is no decrypt_dll.
		 * I'm not sure where exactly this byte goes, but it's after the compression
		 * type and before EncryptionUsed flag.
		 * The other values/flags between here and there look sane (mostly default).
		 */
		(void)util::load<boost::uint8_t>(is);
	}
	
	options |= load_flags(is, version);
	
	if(version < INNO_VERSION(3, 0, 4)) {
		privileges_required = (options & AdminPrivilegesRequired) ? AdminPriviliges : NoPrivileges;
	}
	
	if(version < INNO_VERSION(4, 0, 10)) {
		show_language_dialog = (options & ShowLanguageDialog) ? Yes : No;
		language_detection = (options & DetectLanguageUsingLocale) ? LocaleLanguage : UILanguage;
	}
	
	if(version < INNO_VERSION(4, 1, 5)) {
		compression = (options & BzipUsed) ? stream::BZip2 : stream::Zlib;
	}
	
	if(version < INNO_VERSION(5, 3, 3)) {
		disable_dir_page = (options & DisableDirPage) ? Yes : No;
		disable_program_group_page = (options & DisableProgramGroupPage) ? Yes : No;
	}
	
	if(version < INNO_VERSION(1, 3, 0)) {
		if(license_size > 0) {
			license_text.resize(size_t(license_size));
			is.read(&license_text[0], license_size);
			util::to_utf8(license_text);
		}
		if(info_before_size > 0) {
			info_before.resize(size_t(info_before_size));
			is.read(&info_before[0], info_before_size);
			util::to_utf8(info_before);
		}
		if(info_after_size > 0) {
			info_after.resize(size_t(info_after_size));
			is.read(&info_after[0], info_after_size);
			util::to_utf8(info_after);
		}
	}
	
}

header::flags header::load_flags(std::istream & is, const version & version) {
	
	stored_flag_reader<flags> flagreader(is, version.bits());
	
	flagreader.add(DisableStartupPrompt);
	if(version < INNO_VERSION(5, 3, 10)) {
		flagreader.add(Uninstallable);
	}
	flagreader.add(CreateAppDir);
	if(version < INNO_VERSION(5, 3, 3)) {
		flagreader.add(DisableDirPage);
	}
	if(version < INNO_VERSION(1, 3, 6)) {
		flagreader.add(DisableDirExistsWarning);
	}
	if(version < INNO_VERSION(5, 3, 3)) {
		flagreader.add(DisableProgramGroupPage);
	}
	flagreader.add(AllowNoIcons);
	if(version < INNO_VERSION(3, 0, 0) || version >= INNO_VERSION(3, 0, 3)) {
		flagreader.add(AlwaysRestart);
	}
	if(version < INNO_VERSION(1, 3, 3)) {
		flagreader.add(BackSolid);
	}
	flagreader.add(AlwaysUsePersonalGroup);
	if(version < INNO_VERSION_EXT(6, 4, 0, 1)) {
		flagreader.add(WindowVisible);
		flagreader.add(WindowShowCaption);
		flagreader.add(WindowResizable);
		flagreader.add(WindowStartMaximized);
	}
	flagreader.add(EnableDirDoesntExistWarning);
	if(version < INNO_VERSION(4, 1, 2)) {
		flagreader.add(DisableAppendDir);
	}
	flagreader.add(Password);
	if(version >= INNO_VERSION(1, 2, 6)) {
		flagreader.add(AllowRootDirectory);
	}
	if(version >= INNO_VERSION(1, 2, 14)) {
		flagreader.add(DisableFinishedPage);
	}
	if(version.bits() != 16) {
		if(version < INNO_VERSION(3, 0, 4)) {
			flagreader.add(AdminPrivilegesRequired);
		}
		if(version < INNO_VERSION(3, 0, 0)) {
			flagreader.add(AlwaysCreateUninstallIcon);
		}
		if(version < INNO_VERSION(1, 3, 6)) {
			flagreader.add(OverwriteUninstRegEntries);
		}
		if(version < INNO_VERSION(5, 6, 1)) {
			flagreader.add(ChangesAssociations);
		}
	}
	if(version >= INNO_VERSION(1, 3, 0) && version < INNO_VERSION(5, 3, 8)) {
		flagreader.add(CreateUninstallRegKey);
	}
	if(version >= INNO_VERSION(1, 3, 1)) {
		flagreader.add(UsePreviousAppDir);
	}
	if(version >= INNO_VERSION(1, 3, 3) && version < INNO_VERSION_EXT(6, 4, 0, 1)) {
		flagreader.add(BackColorHorizontal);
	}
	if(version >= INNO_VERSION(1, 3, 10)) {
		flagreader.add(UsePreviousGroup);
	}
	if(version >= INNO_VERSION(1, 3, 20)) {
		flagreader.add(UpdateUninstallLogAppName);
	}
	if(version >= INNO_VERSION(2, 0, 0) || (version.is_isx() && version >= INNO_VERSION(1, 3, 10))) {
		flagreader.add(UsePreviousSetupType);
	}
	if(version >= INNO_VERSION(2, 0, 0)) {
		flagreader.add(DisableReadyMemo);
		flagreader.add(AlwaysShowComponentsList);
		flagreader.add(FlatComponentsList);
		flagreader.add(ShowComponentSizes);
		flagreader.add(UsePreviousTasks);
		flagreader.add(DisableReadyPage);
	}
	if(version >= INNO_VERSION(2, 0, 7)) {
		flagreader.add(AlwaysShowDirOnReadyPage);
		flagreader.add(AlwaysShowGroupOnReadyPage);
	}
	if(version >= INNO_VERSION(2, 0, 17) && version < INNO_VERSION(4, 1, 5)) {
		flagreader.add(BzipUsed);
	}
	if(version >= INNO_VERSION(2, 0, 18)) {
		flagreader.add(AllowUNCPath);
	}
	if(version >= INNO_VERSION(3, 0, 0)) {
		flagreader.add(UserInfoPage);
		flagreader.add(UsePreviousUserInfo);
	}
	if(version >= INNO_VERSION(3, 0, 1)) {
		flagreader.add(UninstallRestartComputer);
	}
	if(version >= INNO_VERSION(3, 0, 3)) {
		flagreader.add(RestartIfNeededByRun);
	}
	if(version >= INNO_VERSION(4, 0, 0) || (version.is_isx() && version >= INNO_VERSION(3, 0, 3))) {
		flagreader.add(ShowTasksTreeLines);
	}
	if(version >= INNO_VERSION(4, 0, 0) && version < INNO_VERSION(4, 0, 10)) {
		flagreader.add(ShowLanguageDialog);
	}
	if(version >= INNO_VERSION(4, 0, 1) && version < INNO_VERSION(4, 0, 10)) {
		flagreader.add(DetectLanguageUsingLocale);
	}
	if(version >= INNO_VERSION(4, 0, 9)) {
		flagreader.add(AllowCancelDuringInstall);
	} else {
		options |= AllowCancelDuringInstall;
	}
	if(version >= INNO_VERSION(4, 1, 3)) {
		flagreader.add(WizardImageStretch);
	}
	if(version >= INNO_VERSION(4, 1, 8)) {
		flagreader.add(AppendDefaultDirName);
		flagreader.add(AppendDefaultGroupName);
	}
	if(version >= INNO_VERSION(4, 2, 2)) {
		flagreader.add(EncryptionUsed);
	}
	if(version >= INNO_VERSION(5, 0, 4) && version < INNO_VERSION(5, 6, 1)) {
		flagreader.add(ChangesEnvironment);
	}
	if(version >= INNO_VERSION(5, 1, 7) && !version.is_unicode()) {
		flagreader.add(ShowUndisplayableLanguages);
	}
	if(version >= INNO_VERSION(5, 1, 13)) {
		flagreader.add(SetupLogging);
	}
	if(version >= INNO_VERSION(5, 2, 1)) {
		flagreader.add(SignedUninstaller);
	}
	if(version >= INNO_VERSION(5, 3, 8)) {
		flagreader.add(UsePreviousLanguage);
	}
	if(version >= INNO_VERSION(5, 3, 9)) {
		flagreader.add(DisableWelcomePage);
	}
	if(version >= INNO_VERSION(5, 5, 0)) {
		flagreader.add(CloseApplications);
		flagreader.add(RestartApplications);
		flagreader.add(AllowNetworkDrive);
	} else {
		options |= AllowNetworkDrive;
	}
	if(version >= INNO_VERSION(5, 5, 7)) {
		flagreader.add(ForceCloseApplications);
	}
	if(version >= INNO_VERSION(6, 0, 0)) {
		flagreader.add(AppNameHasConsts);
		flagreader.add(UsePreviousPrivileges);
		flagreader.add(WizardResizable);
	}
	if(version >= INNO_VERSION(6, 3, 0)) {
		flagreader.add(UninstallLogging);
	}
	
	return flagreader.finalize();
}

void header::decode(util::codepage_id codepage) {
	
	util::to_utf8(app_name, codepage);
	util::to_utf8(app_versioned_name, codepage);
	util::to_utf8(app_id, codepage);
	util::to_utf8(app_copyright, codepage);
	util::to_utf8(app_publisher, codepage);
	util::to_utf8(app_publisher_url, codepage);
	util::to_utf8(app_support_phone, codepage);
	util::to_utf8(app_support_url, codepage);
	util::to_utf8(app_updates_url, codepage);
	util::to_utf8(app_version, codepage);
	util::to_utf8(default_dir_name, codepage, &lead_bytes);
	util::to_utf8(default_group_name, codepage);
	util::to_utf8(base_filename, codepage, &lead_bytes);
	util::to_utf8(uninstall_files_dir, codepage, &lead_bytes);
	util::to_utf8(uninstall_name, codepage, &lead_bytes);
	util::to_utf8(uninstall_icon, codepage, &lead_bytes);
	util::to_utf8(app_mutex, codepage, &lead_bytes);
	util::to_utf8(default_user_name, codepage);
	util::to_utf8(default_user_organisation, codepage);
	util::to_utf8(default_serial, codepage);
	util::to_utf8(app_readme_file, codepage, &lead_bytes);
	util::to_utf8(app_contact, codepage);
	util::to_utf8(app_comments, codepage);
	util::to_utf8(app_modify_path, codepage, &lead_bytes);
	util::to_utf8(create_uninstall_registry_key, codepage, &lead_bytes);
	util::to_utf8(uninstallable, codepage);
	util::to_utf8(close_applications_filter, codepage);
	util::to_utf8(setup_mutex, codepage, &lead_bytes);
	util::to_utf8(changes_environment, codepage);
	util::to_utf8(changes_associations, codepage);
	
}

} // namespace setup

NAMES(setup::header::flags, "Setup Option",
	"disable startup prompt",
	"create app dir",
	"allow no icons",
	"always restart",
	"always use personal group",
	"window visible",
	"window show caption",
	"window resizable",
	"window start maximized",
	"enable dir doesn't exist warning",
	"password",
	"allow root directory",
	"disable finished page",
	"changes associations",
	"use previous app dir",
	"back color horizontal",
	"use previous group",
	"update uninstall log app name",
	"use previous setup type",
	"disable ready memo",
	"always show components list",
	"flat components list",
	"show component sizes",
	"use previous tasks",
	"disable ready page",
	"always show dir on ready page",
	"always show group on ready page",
	"allow unc path",
	"user info page",
	"use previous user info",
	"uninstall restart computer",
	"restart if needed by run",
	"show tasks tree lines",
	"allow cancel during install",
	"wizard image stretch",
	"append default dir name",
	"append default group name",
	"encrypted",
	"changes environment",
	"show undisplayable languages",
	"setup logging",
	"signed uninstaller",
	"use previous language",
	"disable welcome page",
	"close applications",
	"restart applications",
	"allow network drive",
	"force close applications",
	"app name_has_consts",
	"use_previous_privileges",
	"wizard_resizable",
	"uninstall_logging",
	"uninstallable",
	"disable dir page",
	"disable program group page",
	"disable append dir",
	"admin privilegesrequired",
	"always create uninstall icon",
	"create uninstall reg key",
	"bzip used",
	"show language dialog",
	"detect language using locale",
	"disable dir exists warning",
	"back solid",
	"overwrite uninst reg entries",
)

NAMES(setup::header::architecture_types, "Architecture",
	"unknown",
	"x86",
	"x64",
	"Itanium",
	"Arm32",
	"Arm64",
)

NAMES(setup::header::privileges_required_overrides, "Privilege Override"
	"commandline",
	"dialog",
)

NAMES(setup::header::alpha_format, "Alpha Format",
	"ignored",
	"defined",
	"premultiplied",
)

NAMES(setup::header::install_verbosity, "Install Mode",
	"normal",
	"silent",
	"very silent",
)

NAMES(setup::header::log_mode, "Uninstall Log Mode",
	"append",
	"new log",
	"overwrite",
)

NAMES(setup::header::style, "Style",
	"classic",
	"modern",
)

NAMES(setup::header::auto_bool, "Auto Boolean",
	"auto",
	"no",
	"yes",
)

NAMES(setup::header::privilege_level, "Privileges",
	"none",
	"power user",
	"admin",
	"lowest",
)

NAMES(setup::header::language_detection_method, "Language Detection",
	"ui language",
	"locale",
	"none",
)
```

## File: `src/setup/header.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for the main setup header in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_HEADER_HPP
#define INNOEXTRACT_SETUP_HEADER_HPP

#include <stddef.h>
#include <bitset>
#include <string>
#include <iosfwd>

#include <boost/cstdint.hpp>

#include "crypto/checksum.hpp"
#include "setup/windows.hpp"
#include "stream/chunk.hpp"
#include "util/encoding.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct version;

struct header {
	
	// Setup data header.
	
	FLAGS(flags,
		
		DisableStartupPrompt,
		CreateAppDir,
		AllowNoIcons,
		AlwaysRestart,
		AlwaysUsePersonalGroup,
		WindowVisible,
		WindowShowCaption,
		WindowResizable,
		WindowStartMaximized,
		EnableDirDoesntExistWarning,
		Password,
		AllowRootDirectory,
		DisableFinishedPage,
		ChangesAssociations,
		UsePreviousAppDir,
		BackColorHorizontal,
		UsePreviousGroup,
		UpdateUninstallLogAppName,
		UsePreviousSetupType,
		DisableReadyMemo,
		AlwaysShowComponentsList,
		FlatComponentsList,
		ShowComponentSizes,
		UsePreviousTasks,
		DisableReadyPage,
		AlwaysShowDirOnReadyPage,
		AlwaysShowGroupOnReadyPage,
		AllowUNCPath,
		UserInfoPage,
		UsePreviousUserInfo,
		UninstallRestartComputer,
		RestartIfNeededByRun,
		ShowTasksTreeLines,
		AllowCancelDuringInstall,
		WizardImageStretch,
		AppendDefaultDirName,
		AppendDefaultGroupName,
		EncryptionUsed,
		ChangesEnvironment,
		ShowUndisplayableLanguages,
		SetupLogging,
		SignedUninstaller,
		UsePreviousLanguage,
		DisableWelcomePage,
		CloseApplications,
		RestartApplications,
		AllowNetworkDrive,
		ForceCloseApplications,
		AppNameHasConsts,
		UsePreviousPrivileges,
		WizardResizable,
		UninstallLogging,
		
		// Obsolete flags
		Uninstallable,
		DisableDirPage,
		DisableProgramGroupPage,
		DisableAppendDir,
		AdminPrivilegesRequired,
		AlwaysCreateUninstallIcon,
		CreateUninstallRegKey,
		BzipUsed,
		ShowLanguageDialog,
		DetectLanguageUsingLocale,
		DisableDirExistsWarning,
		BackSolid,
		OverwriteUninstRegEntries
		
	);
	
	FLAGS(architecture_types,
		ArchitectureUnknown,
		X86,
		Amd64,
		IA64,
		ARM32,
		ARM64
	);
	
	FLAGS(privileges_required_overrides,
		Commandline,
		Dialog
	);
	
	std::string app_name;
	std::string app_versioned_name;
	std::string app_id;
	std::string app_copyright;
	std::string app_publisher;
	std::string app_publisher_url;
	std::string app_support_phone;
	std::string app_support_url;
	std::string app_updates_url;
	std::string app_version;
	std::string default_dir_name;
	std::string default_group_name;
	std::string uninstall_icon_name;
	std::string base_filename;
	std::string uninstall_files_dir;
	std::string uninstall_name;
	std::string uninstall_icon;
	std::string app_mutex;
	std::string default_user_name;
	std::string default_user_organisation;
	std::string default_serial;
	std::string app_readme_file;
	std::string app_contact;
	std::string app_comments;
	std::string app_modify_path;
	std::string create_uninstall_registry_key;
	std::string uninstallable;
	std::string close_applications_filter;
	std::string setup_mutex;
	std::string changes_environment;
	std::string changes_associations;
	std::string architectures_allowed_expr;
	std::string architectures_installed_in_64bit_mode_expr;
	std::string license_text;
	std::string info_before;
	std::string info_after;
	std::string uninstaller_signature;
	std::string compiled_code;
	
	std::bitset<256> lead_bytes;
	
	size_t language_count;
	size_t message_count;
	size_t permission_count;
	size_t type_count;
	size_t component_count;
	size_t task_count;
	size_t directory_count;
	size_t file_count;
	size_t data_entry_count;
	size_t icon_count;
	size_t ini_entry_count;
	size_t registry_entry_count;
	size_t delete_entry_count;
	size_t uninstall_delete_entry_count;
	size_t run_entry_count;
	size_t uninstall_run_entry_count;
	
	windows_version_range winver;
	
	typedef boost::uint32_t Color;
	Color back_color;
	Color back_color2;
	Color image_back_color;
	Color small_image_back_color;
	
	enum style {
		ClassicStyle,
		ModernStyle
	};
	style wizard_style;
	boost::uint32_t wizard_resize_percent_x;
	boost::uint32_t wizard_resize_percent_y;
	
	enum alpha_format {
		AlphaIgnored,
		AlphaDefined,
		AlphaPremultiplied
	};
	alpha_format image_alpha_format;
	
	crypto::checksum password;
	std::string password_salt;
	
	boost::int64_t extra_disk_space_required;
	size_t slices_per_disk;
	
	enum install_verbosity {
		NormalInstallMode,
		SilentInstallMode,
		VerySilentInstallMode,
	};
	install_verbosity install_mode;
	
	enum log_mode {
		AppendLog,
		NewLog,
		OverwriteLog
	};
	log_mode uninstall_log_mode;
	
	style uninstall_style;
	
	enum auto_bool {
		Auto,
		No,
		Yes
	};
	
	auto_bool dir_exists_warning;
	
	enum privilege_level {
		NoPrivileges,
		PowerUserPrivileges,
		AdminPriviliges,
		LowestPrivileges
	};
	privilege_level privileges_required;
	
	privileges_required_overrides privileges_required_override_allowed;
	
	auto_bool show_language_dialog;
	
	enum language_detection_method {
		UILanguage,
		LocaleLanguage,
		NoLanguageDetection
	};
	language_detection_method language_detection;
	
	stream::compression_method compression;
	
	architecture_types architectures_allowed;
	architecture_types architectures_installed_in_64bit_mode;
	
	boost::uint32_t signed_uninstaller_original_size;
	boost::uint32_t signed_uninstaller_header_checksum;
	
	auto_bool disable_dir_page;
	auto_bool disable_program_group_page;
	
	boost::uint64_t uninstall_display_size;
	
	flags options;
	
	void load(std::istream & is, const version & version);
	
	void decode(util::codepage_id codepage);
	
private:
	
	flags load_flags(std::istream & is, const version & version);
	
};

} // namespace setup

NAMED_FLAGS(setup::header::flags)
NAMED_FLAGS(setup::header::architecture_types)
NAMED_FLAGS(setup::header::privileges_required_overrides)
NAMED_ENUM(setup::header::alpha_format)
NAMED_ENUM(setup::header::install_verbosity)
NAMED_ENUM(setup::header::log_mode)
NAMED_ENUM(setup::header::style)
NAMED_ENUM(setup::header::auto_bool)
NAMED_ENUM(setup::header::privilege_level)
NAMED_ENUM(setup::header::language_detection_method)

#endif // INNOEXTRACT_SETUP_HEADER_HPP
```

## File: `src/setup/icon.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/icon.hpp"

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/storedenum.hpp"

namespace setup {

namespace {

STORED_ENUM_MAP(stored_close_setting, icon_entry::NoSetting,
	icon_entry::NoSetting,
	icon_entry::CloseOnExit,
	icon_entry::DontCloseOnExit,
);

} // anonymous namespace

void icon_entry::load(std::istream & is, const info & i) {
	
	if(i.version < INNO_VERSION(1, 3, 0)) {
		(void)util::load<boost::uint32_t>(is); // uncompressed size of the entry
	}
	
	is >> util::encoded_string(name, i.codepage, i.header.lead_bytes);
	is >> util::encoded_string(filename, i.codepage, i.header.lead_bytes);
	is >> util::encoded_string(parameters, i.codepage, i.header.lead_bytes);
	is >> util::encoded_string(working_dir, i.codepage, i.header.lead_bytes);
	is >> util::encoded_string(icon_file, i.codepage, i.header.lead_bytes);
	is >> util::encoded_string(comment, i.codepage);
	
	load_condition_data(is, i);
	
	if(i.version >= INNO_VERSION(5, 3, 5)) {
		is >> util::encoded_string(app_user_model_id, i.codepage);
	} else {
		app_user_model_id.clear();
	}
	
	if(i.version >= INNO_VERSION(6, 1, 0)) {
		const size_t guid_size = 16;
		app_user_model_toast_activator_clsid.resize(guid_size);
		is.read(&app_user_model_toast_activator_clsid[0], std::streamsize(guid_size));
	} else {
		app_user_model_toast_activator_clsid.clear();
	}
	
	load_version_data(is, i.version);
	
	icon_index = util::load<boost::int32_t>(is, i.version.bits());
	
	if(i.version >= INNO_VERSION(1, 3, 24)) {
		show_command = util::load<boost::int32_t>(is);
	} else {
		show_command = 1;
	}
	if(i.version >= INNO_VERSION(1, 3, 15)) {
		close_on_exit = stored_enum<stored_close_setting>(is).get();
	} else {
		close_on_exit = NoSetting;
	}
	
	if(i.version >= INNO_VERSION(2, 0, 7)) {
		hotkey = util::load<boost::uint16_t>(is);
	} else {
		hotkey = 0;
	}
	
	stored_flag_reader<flags> flagreader(is, i.version.bits());
	
	flagreader.add(NeverUninstall);
	if(i.version < INNO_VERSION(1, 3, 26)) {
		flagreader.add(RunMinimized);
	}
	flagreader.add(CreateOnlyIfFileExists);
	if(i.version.bits() != 16) {
		flagreader.add(UseAppPaths);
	}
	if(i.version >= INNO_VERSION(5, 0, 3) && i.version < INNO_VERSION(6, 3, 0)) {
		flagreader.add(FolderShortcut);
	}
	if(i.version >= INNO_VERSION(5, 4, 2)) {
		flagreader.add(ExcludeFromShowInNewInstall);
	}
	if(i.version >= INNO_VERSION(5, 5, 0)) {
		flagreader.add(PreventPinning);
	}
	if(i.version >= INNO_VERSION(6, 1, 0)) {
		flagreader.add(HasAppUserModelToastActivatorCLSID);
	}
	
	options = flagreader.finalize();
}

} // namespace setup

NAMES(setup::icon_entry::flags, "Icon Option",
	"never uninstall",
	"create only if file exists",
	"use app paths",
	"folder shortcut",
	"exclude from show in new install",
	"prevent pinning",
	"run minimized",
)

NAMES(setup::icon_entry::close_setting, "Close on Exit",
	"no setting",
	"close on exit",
	"don't close on exit",
)
```

## File: `src/setup/icon.hpp`
```
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for menu/desktop shortcuts stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_ICON_HPP
#define INNOEXTRACT_SETUP_ICON_HPP

#include <string>
#include <iosfwd>

#include <boost/cstdint.hpp>

#include "setup/item.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct info;

struct icon_entry : public item {
	
	FLAGS(flags,
		NeverUninstall,
		CreateOnlyIfFileExists,
		UseAppPaths,
		FolderShortcut,
		ExcludeFromShowInNewInstall,
		PreventPinning,
		HasAppUserModelToastActivatorCLSID,
		// obsolete options:
		RunMinimized
	);
	
	enum close_setting {
		NoSetting,
		CloseOnExit,
		DontCloseOnExit,
	};
	
	std::string name;
	std::string filename;
	std::string parameters;
	std::string working_dir;
	std::string icon_file;
	std::string comment;
	std::string app_user_model_id;
	std::string app_user_model_toast_activator_clsid;
	
	int icon_index;
	
	int show_command;
	
	close_setting close_on_exit;
	
	boost::uint16_t hotkey;
	
	flags options;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_FLAGS(setup::icon_entry::flags)
NAMED_ENUM(setup::icon_entry::close_setting)

#endif // INNOEXTRACT_SETUP_ICON_HPP
```

## File: `src/setup/info.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/info.hpp"

#include <cassert>
#include <istream>
#include <sstream>

#include <boost/foreach.hpp>

#include "crypto/hasher.hpp"
#include "crypto/pbkdf2.hpp"
#include "crypto/sha256.hpp"
#include "crypto/xchacha20.hpp"
#include "setup/component.hpp"
#include "setup/data.hpp"
#include "setup/delete.hpp"
#include "setup/directory.hpp"
#include "setup/file.hpp"
#include "setup/icon.hpp"
#include "setup/ini.hpp"
#include "setup/item.hpp"
#include "setup/language.hpp"
#include "setup/message.hpp"
#include "setup/permission.hpp"
#include "setup/registry.hpp"
#include "setup/run.hpp"
#include "setup/task.hpp"
#include "setup/type.hpp"
#include "stream/block.hpp"
#include "util/endian.hpp"
#include "util/fstream.hpp"
#include "util/load.hpp"
#include "util/log.hpp"
#include "util/output.hpp"

namespace setup {

template <class Entry>
void info::load_entries(std::istream & is, entry_types entries, size_t count,
                        std::vector<Entry> & result, entry_types::enum_type entry_type) {
	
	result.clear();
	if(entries & entry_type) {
		result.resize(count);
		for(size_t i = 0; i < count; i++) {
			result[i].load(is, *this);
		}
	} else {
		for(size_t i = 0; i < count; i++) {
			Entry entry;
			entry.load(is, *this);
		}
	}
}

namespace {

void load_wizard_images(std::istream & is, const setup::version & version,
                        std::vector<std::string> & images, info::entry_types entries) {
	
	size_t count = 1;
	if(version >= INNO_VERSION(5, 6, 0)) {
		count = util::load<boost::uint32_t>(is);
	}
	
	if(entries & (info::WizardImages | info::NoSkip)) {
		images.resize(count);
		for(size_t i = 0; i < count; i++) {
			is >> util::binary_string(images[i]);
		}
		if(version < INNO_VERSION(5, 6, 0) && images[0].empty()) {
			images.clear();
		}
	} else {
		for(size_t i = 0; i < count; i++) {
			util::binary_string::skip(is);
		}
	}
	
}

void load_wizard_and_decompressor(std::istream & is, const setup::version & version,
                                  const setup::header & header,
                                  setup::info & info, info::entry_types entries) {
	
	info.wizard_images.clear();
	info.wizard_images_small.clear();
	
	load_wizard_images(is, version, info.wizard_images, entries);
	
	if(version >= INNO_VERSION(2, 0, 0) || version.is_isx()) {
		load_wizard_images(is, version, info.wizard_images_small, entries);
	}
	
	info.decompressor_dll.clear();
	if(header.compression == stream::BZip2
	   || (header.compression == stream::LZMA1 && version == INNO_VERSION(4, 1, 5))
	   || (header.compression == stream::Zlib && version >= INNO_VERSION(4, 2, 6))) {
		if(entries & (info::DecompressorDll | info::NoSkip)) {
			is >> util::binary_string(info.decompressor_dll);
		} else {
			// decompressor dll - we don't need this
			util::binary_string::skip(is);
		}
	}
	
	info.decrypt_dll.clear();
	if((header.options & header::EncryptionUsed) && version < INNO_VERSION(6, 4, 0)) {
		if(entries & (info::DecryptDll | info::NoSkip)) {
			is >> util::binary_string(info.decrypt_dll);
		} else {
			// decrypt dll - we don't need this
			util::binary_string::skip(is);
		}
	}
	
}

void check_is_end(stream::block_reader::pointer & is, const char * what) {
	is->exceptions(std::ios_base::goodbit);
	char dummy;
	if(!is->get(dummy).eof()) {
		throw std::ios_base::failure(what);
	}
}

} // anonymous namespace

void info::try_load(std::istream & is, entry_types entries, util::codepage_id force_codepage) {
	
	debug("trying to load setup headers for version " << version);
	
	if((entries & (Messages | NoSkip)) || (!version.is_unicode() && !force_codepage)) {
		entries |= Languages;
	}
	
	stream::block_reader::pointer reader = stream::block_reader::get(is, version);
	
	debug("loading main header");
	header.load(*reader, version);
	
	debug("loading languages");
	load_entries(*reader, entries, header.language_count, languages, Languages);
	
	debug("determining encoding");
	if(version.is_unicode()) {
		// Unicode installers are always UTF16-LE, do not allow users to override that.
		codepage = util::cp_utf16le;
	} else if(force_codepage) {
		codepage = force_codepage;
	} else if(languages.empty()) {
		codepage = util::cp_windows1252;
	} else {
		// Non-Unicode installers do not have a defined codepage but instead just assume the
		// codepage of the system the installer is run on.
		// Look at the list of available languages to guess a suitable codepage.
		codepage = languages[0].codepage;
		BOOST_FOREACH(const language_entry & language, languages) {
			if(language.codepage == util::cp_windows1252) {
				codepage = util::cp_windows1252;
				break;
			}
		}
	}
	
	header.decode(codepage);
	BOOST_FOREACH(language_entry & language, languages) {
		language.decode(codepage);
	}
	
	if(version < INNO_VERSION(4, 0, 0)) {
		debug("loading images and plugins");
		load_wizard_and_decompressor(*reader, version, header, *this, entries);
	}
	
	debug("loading messages");
	load_entries(*reader, entries, header.message_count, messages, Messages);
	debug("loading permissions");
	load_entries(*reader, entries, header.permission_count, permissions, Permissions);
	debug("loading types");
	load_entries(*reader, entries, header.type_count, types, Types);
	debug("loading components");
	load_entries(*reader, entries, header.component_count, components, Components);
	debug("loading tasks");
	load_entries(*reader, entries, header.task_count, tasks, Tasks);
	debug("loading directories");
	load_entries(*reader, entries, header.directory_count, directories, Directories);
	debug("loading files");
	load_entries(*reader, entries, header.file_count, files, Files);
	debug("loading icons");
	load_entries(*reader, entries, header.icon_count, icons, Icons);
	debug("loading ini entries");
	load_entries(*reader, entries, header.ini_entry_count, ini_entries, IniEntries);
	debug("loading registry entries");
	load_entries(*reader, entries, header.registry_entry_count, registry_entries, RegistryEntries);
	debug("loading delete entries");
	load_entries(*reader, entries, header.delete_entry_count, delete_entries, DeleteEntries);
	debug("loading uninstall delete entries");
	load_entries(*reader, entries, header.uninstall_delete_entry_count, uninstall_delete_entries,
	             UninstallDeleteEntries);
	debug("loading run entries");
	load_entries(*reader, entries, header.run_entry_count, run_entries, RunEntries);
	debug("loading uninstall run entries");
	load_entries(*reader, entries, header.uninstall_run_entry_count, uninstall_run_entries,
	             UninstallRunEntries);
	
	if(version >= INNO_VERSION(4, 0, 0)) {
		debug("loading images and plugins");
		load_wizard_and_decompressor(*reader, version, header, *this, entries);
	}
	
	// restart the compression stream
	check_is_end(reader, "unknown data at end of primary header stream");
	reader = stream::block_reader::get(is, version);
	
	debug("loading data entries");
	load_entries(*reader, entries, header.data_entry_count, data_entries, DataEntries);
	
	check_is_end(reader, "unknown data at end of secondary header stream");
}

void info::load(std::istream & is, entry_types entries, util::codepage_id force_codepage) {
	
	version.load(is);
	
	if(!version.known) {
		if(entries & NoUnknownVersion) {
			std::ostringstream oss;
			oss << "Unexpected setup data version: " << version;
			throw std::runtime_error(oss.str());
		}
		log_warning << "Unexpected setup data version: "
		            << color::white << version << color::reset;
	}
	
	version_constant listed_version = version.value;
	
	// Some setup versions didn't increment the data version number when they should have.
	// To work around this, we try to parse the headers for all data versions and use the first
	// version that parses without warnings or errors.
	bool ambiguous = !version.known || version.is_ambiguous();
	if(version.is_ambiguous()) {
		// Force parsing all headers so that we don't miss any errors.
		entries |= NoSkip;
	}
	
	bool parsed_without_errors = false;
	std::streampos start = is.tellg();
	for(;;) {
		
		warning_suppressor warnings;
		
		try {
			
			// Try to parse headers for this version
			try_load(is, entries, force_codepage);
			
			if(warnings) {
				// Parsed without errors but with warnings - try other versions first
				if(!parsed_without_errors) {
					listed_version = version.value;
					parsed_without_errors = true;
				}
				throw std::exception();
			}
			
			warnings.flush();
			return;
			
		} catch(...) {
			
			is.clear();
			is.seekg(start);
			
			version_constant next_version = version.next();
			
			if(!ambiguous || !next_version) {
				if(version.value != listed_version) {
					// Rewind to a previous version that had better results and report those
					version.value = listed_version;
					warnings.restore();
					try_load(is, entries, force_codepage);
				} else {
					// Otherwise. report results for the current version
					warnings.flush();
					if(!parsed_without_errors) {
						throw;
					}
				}
				return;
			}
			
			// Retry with the next version
			version.value = next_version;
			ambiguous = version.is_ambiguous();
			
		}
		
	}
	
}

std::string info::get_key(const std::string & password) {
	
	std::string encoded_password;
	util::from_utf8(password, encoded_password, codepage);
	
	if(header.password.type == crypto::PBKDF2_SHA256_XChaCha20) {
		
		#if INNOEXTRACT_HAVE_DECRYPTION
		
		// 16 bytes PBKDF2 salt + 4 bytes PBKDF2 iterations + 24 bytes ChaCha20 base nonce
		if(header.password_salt.length() != 20 + crypto::xchacha20::nonce_size) {
			throw std::runtime_error("unexpected password salt size");
		}
		
		std::string result;
		result.resize(crypto::xchacha20::key_size + crypto::xchacha20::nonce_size);
		typedef crypto::pbkdf2<crypto::sha256> pbkdf2;
		pbkdf2::derive(encoded_password.c_str(), encoded_password.length(), &header.password_salt[0], 16,
		               util::little_endian::load<boost::uint32_t>(&header.password_salt[16]), &result[0],
		               crypto::xchacha20::key_size);
		
		std::memcpy(&result[crypto::xchacha20::key_size], &header.password_salt[20],
		            crypto::xchacha20::nonce_size);
		
		return result;
		
		#endif
		
	}
	
	return encoded_password;
}

bool info::check_key(const std::string & key) {
	
	if(header.password.type == crypto::PBKDF2_SHA256_XChaCha20) {
		
		#if INNOEXTRACT_HAVE_DECRYPTION
		
		if(key.length() != crypto::xchacha20::key_size + crypto::xchacha20::nonce_size) {
			throw std::runtime_error("unexpected key size");
		}
		
		crypto::xchacha20 cipher;
		
		char nonce[crypto::xchacha20::nonce_size];
		std::memcpy(nonce, key.c_str() + crypto::xchacha20::key_size, crypto::xchacha20::nonce_size);
		*reinterpret_cast<boost::uint32_t *>(nonce + 8) = ~*reinterpret_cast<boost::uint32_t *>(nonce + 8);
		cipher.init(key.c_str(), nonce);
		
		char buffer[] = { 0, 0, 0, 0 };
		cipher.crypt(buffer, buffer, sizeof(buffer));
		
		return (std::memcmp(buffer, header.password.check, sizeof(buffer)) == 0);
		
		#else
		throw std::runtime_error("XChaCha20 decryption not supported in this build");
		#endif
		
	} else {
		
		crypto::hasher checksum(header.password.type);
		checksum.update(header.password_salt.c_str(), header.password_salt.length());
		checksum.update(key.c_str(), key.length());
		return (checksum.finalize() == header.password);
		
	}
	
}

info::info() : codepage(0) { }
info::~info() { }

} // namespace setup
```

## File: `src/setup/info.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Central point to load all the different headers in the correct order.
 */
#ifndef INNOEXTRACT_SETUP_INFO_HPP
#define INNOEXTRACT_SETUP_INFO_HPP

#include <vector>
#include <iosfwd>

#include "setup/header.hpp"
#include "setup/version.hpp"
#include "util/encoding.hpp"
#include "util/flags.hpp"

namespace setup {

struct component_entry;
struct data_entry;
struct delete_entry;
struct directory_entry;
struct file_entry;
struct icon_entry;
struct ini_entry;
struct language_entry;
struct message_entry;
struct permission_entry;
struct registry_entry;
struct run_entry;
struct task_entry;
struct type_entry;

/*!
 * Class used to hold and load the various \ref setup headers.
 */
struct info {
	
	// Explicit constructor/destructor required to allow forward-declaring entry types
	info();
	~info();
	
	FLAGS(entry_types,
		Components,
		DataEntries,
		DeleteEntries,
		UninstallDeleteEntries,
		Directories,
		Files,
		Icons,
		IniEntries,
		Languages,
		Messages,
		Permissions,
		RegistryEntries,
		RunEntries,
		UninstallRunEntries,
		Tasks,
		Types,
		WizardImages,
		DecompressorDll,
		DecryptDll,
		NoSkip,
		NoUnknownVersion
	);
	
	setup::version version;
	
	util::codepage_id codepage;
	
	setup::header header;
	
	std::vector<component_entry>  components;               //! \c Components
	std::vector<data_entry>       data_entries;             //! \c DataEntries
	std::vector<delete_entry>     delete_entries;           //! \c DeleteEntries
	std::vector<delete_entry>     uninstall_delete_entries; //! \c UninstallDeleteEntries
	std::vector<directory_entry>  directories;              //! \c Directories
	std::vector<file_entry>       files;                    //! \c Files
	std::vector<icon_entry>       icons;                    //! \c Icons
	std::vector<ini_entry>        ini_entries;              //! \c IniEntries
	std::vector<language_entry>   languages;                //! \c Languages
	std::vector<message_entry>    messages;                 //! \c Messages
	std::vector<permission_entry> permissions;              //! \c Permissions
	std::vector<registry_entry>   registry_entries;         //! \c RegistryEntries
	std::vector<run_entry>        run_entries;              //! \c RunEntries
	std::vector<run_entry>        uninstall_run_entries;    //! \c UninstallRunEntries
	std::vector<task_entry>       tasks;                    //! \c Tasks
	std::vector<type_entry>       types;                    //! \c Types
	
	//! Images displayed in the installer UI.
	//! Loading enabled by \c WizardImages
	std::vector<std::string> wizard_images;
	std::vector<std::string> wizard_images_small;
	
	//! Contents of the helper DLL used to decompress setup data in some versions.
	//! Loading enabled by \c DecompressorDll
	std::string decompressor_dll;
	
	//! Contents of the helper DLL used to decrypt setup data.
	//! Loading enabled by \c DecryptDll
	std::string decrypt_dll;
	
	/*!
	 * Load setup headers.
	 *
	 * \param is      The input stream to load the setup headers from.
	 *                It must already be positioned at start of \ref setup::version
	 *                identifier whose position is given by
	 *                \ref loader::offsets::header_offset.
	 * \param entries What kinds of entries to load.
	 * \param force_codepage Windows codepage to use for strings in ANSI installers.
	 */
	void load(std::istream & is, entry_types entries, util::codepage_id force_codepage = 0);
	
	std::string get_key(const std::string & password);
	
	bool check_key(const std::string & key);
	
private:
	
	/*!
	 * Load setup headers for a specific version.
	 *
	 * \param is      The input stream to load the setup headers from.
	 *                It must already be positioned at start of the compressed headers.
	 *                The compressed headers start directly after the \ref setup::version
	 *                identifier whose position is given by
	 *                \ref loader::offsets::header_offset.
	 * \param entries What kinds of entries to load.
	 * \param force_codepage Windows codepage to use for strings in ANSI installers.
	 *
	 * This function does not set the \ref version member.
	 */
	void try_load(std::istream & is, entry_types entries, util::codepage_id force_codepage);
	
	template <class Entry>
	void load_entries(std::istream & is, entry_types entries, size_t count,
	                  std::vector<Entry> & result, entry_types::enum_type entry_type);
	
};

} // namespace setup

FLAGS_OVERLOADS(setup::info::entry_types)

#endif // INNOEXTRACT_SETUP_INFO_HPP
```

## File: `src/setup/ini.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/ini.hpp"

#include <boost/cstdint.hpp>

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/storedenum.hpp"

namespace setup {

namespace {

STORED_FLAGS_MAP(stored_ini_flags,
	ini_entry::CreateKeyIfDoesntExist,
	ini_entry::UninsDeleteEntry,
	ini_entry::UninsDeleteEntireSection,
	ini_entry::UninsDeleteSectionIfEmpty,
	ini_entry::HasValue,
);

} // anonymous namespace

void ini_entry::load(std::istream & is, const info & i) {
	
	if(i.version < INNO_VERSION(1, 3, 0)) {
		(void)util::load<boost::uint32_t>(is); // uncompressed size of the entry
	}
	
	is >> util::encoded_string(inifile, i.codepage, i.header.lead_bytes);
	if(inifile.empty()) {
		inifile = "{windows}/WIN.INI";
	}
	is >> util::encoded_string(section, i.codepage, i.header.lead_bytes);
	is >> util::encoded_string(key, i.codepage);
	is >> util::encoded_string(value, i.codepage, i.header.lead_bytes);
	
	load_condition_data(is, i);
	
	load_version_data(is, i.version);
	
	if(i.version.bits() != 16) {
		options = stored_flags<stored_ini_flags>(is).get();
	} else {
		options = stored_flags<stored_ini_flags, 16>(is).get();
	}
}

} // namespace setup

NAMES(setup::ini_entry::flags, "Ini Option",
	"create key if doesn't exist",
	"uninstall delete entry",
	"uninstall delete section",
	"uninstall delete section if empty",
	"has value",
)
```

## File: `src/setup/ini.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for .ini entries stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_INI_HPP
#define INNOEXTRACT_SETUP_INI_HPP

#include <string>
#include <iosfwd>

#include "setup/item.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct info;

struct ini_entry : public item {
	
	FLAGS(flags,
		CreateKeyIfDoesntExist,
		UninsDeleteEntry,
		UninsDeleteEntireSection,
		UninsDeleteSectionIfEmpty,
		HasValue
	);
	
	std::string inifile;
	std::string section;
	std::string key;
	std::string value;
	
	flags options;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_FLAGS(setup::ini_entry::flags)

#endif // INNOEXTRACT_SETUP_INI_HPP
```

## File: `src/setup/item.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/item.hpp"

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"

namespace setup {

void item::load_condition_data(std::istream & is, const info & i) {
	
	if(i.version >= INNO_VERSION(2, 0, 0) || (i.version.is_isx() && i.version >= INNO_VERSION(1, 3, 8))) {
		is >> util::encoded_string(components, i.codepage);
	} else {
		components.clear();
	}
	if(i.version >= INNO_VERSION(2, 0, 0) || (i.version.is_isx() && i.version >= INNO_VERSION(1, 3, 17))) {
		is >> util::encoded_string(tasks, i.codepage);
	} else {
		tasks.clear();
	}
	if(i.version >= INNO_VERSION(4, 0, 1)) {
		is >> util::encoded_string(languages, i.codepage);
	} else {
		languages.clear();
	}
	if(i.version >= INNO_VERSION(4, 0, 0) || (i.version.is_isx() && i.version >= INNO_VERSION(1, 3, 24))) {
		is >> util::encoded_string(check, i.codepage);
	} else {
		check.clear();
	}
	
	if(i.version >= INNO_VERSION(4, 1, 0)) {
		is >> util::encoded_string(after_install, i.codepage);
		is >> util::encoded_string(before_install, i.codepage);
	} else {
		after_install.clear(), before_install.clear();
	}
	
}

} // namespace setup
```

## File: `src/setup/item.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for setup items stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_ITEM_HPP
#define INNOEXTRACT_SETUP_ITEM_HPP

#include <string>
#include <iosfwd>

#include "setup/windows.hpp"

namespace setup {

struct info;
struct version;

struct item {
	
	std::string components;
	std::string tasks;
	std::string languages;
	std::string check;
	
	std::string after_install;
	std::string before_install;
	
	windows_version_range winver;
	
protected:
	
	void load_condition_data(std::istream & is, const info & i);
	
	void load_version_data(std::istream & is, const version & version) {
		winver.load(is, version);
	}
	
};

} // namespace setup

#endif // INNOEXTRACT_SETUP_ITEM_HPP
```

## File: `src/setup/language.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/language.hpp"

#include <algorithm>

#include "boost/range/begin.hpp"
#include "boost/range/end.hpp"

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"

namespace setup {

namespace {

struct windows_language {
	
	boost::uint16_t language_id;
	boost::uint16_t codepage;
	
};

bool operator<(windows_language language, boost::uint32_t language_id) {
	return language.language_id < language_id;
}

#if defined(__clang_major__) && __clang_major__ < 8 && defined(_LIBCPP_DEBUG)
// Required for debug builds with Clang < 8
bool operator<(boost::uint32_t language_id, windows_language language) {
	return language_id < language.language_id;
}
#endif

/*
 * Sorted list of Windows language IDs with their default ANSI codepages.
 * This list omits Unicode-only languages and languages using the default Windows-1252 codepage.
 */
const windows_language languages[] = {
	{ 0x0401, util::cp_windows1256 },
	{ 0x0402, util::cp_windows1251 },
	{ 0x0404, util::cp_big5 },
	{ 0x0405, util::cp_windows1250 },
	{ 0x0408, util::cp_windows1253 },
	{ 0x040d, util::cp_windows1255 },
	{ 0x040e, util::cp_windows1250 },
	{ 0x0411, util::cp_shift_jis },
	{ 0x0412, util::cp_uhc },
	{ 0x0415, util::cp_windows1250 },
	{ 0x0418, util::cp_windows1250 },
	{ 0x0419, util::cp_windows1251 },
	{ 0x041a, util::cp_windows1250 },
	{ 0x041b, util::cp_windows1250 },
	{ 0x041c, util::cp_windows1250 },
	{ 0x041e, util::cp_windows874 },
	{ 0x041f, util::cp_windows1254 },
	{ 0x0420, util::cp_windows1256 },
	{ 0x0422, util::cp_windows1251 },
	{ 0x0423, util::cp_windows1251 },
	{ 0x0424, util::cp_windows1250 },
	{ 0x0425, util::cp_windows1257 },
	{ 0x0426, util::cp_windows1257 },
	{ 0x0427, util::cp_windows1257 },
	{ 0x0429, util::cp_windows1256 },
	{ 0x042a, util::cp_windows1258 },
	{ 0x042c, util::cp_windows1254 },
	{ 0x042f, util::cp_windows1251 },
	{ 0x043f, util::cp_windows1251 },
	{ 0x0440, util::cp_windows1251 },
	{ 0x0443, util::cp_windows1254 },
	{ 0x0444, util::cp_windows1251 },
	{ 0x0450, util::cp_windows1251 },
	{ 0x0492, util::cp_iso_8859_14 },
	{ 0x0801, util::cp_windows1256 },
	{ 0x0804, util::cp_gbk },
	{ 0x081a, util::cp_windows1250 },
	{ 0x082c, util::cp_windows1251 },
	{ 0x0843, util::cp_windows1251 },
	{ 0x0c01, util::cp_windows1256 },
	{ 0x0c04, util::cp_big5 },
	{ 0x0c1a, util::cp_windows1251 },
	{ 0x1001, util::cp_windows1256 },
	{ 0x1004, util::cp_gbk },
	{ 0x1401, util::cp_windows1256 },
	{ 0x1404, util::cp_big5 },
	{ 0x1801, util::cp_windows1256 },
	{ 0x1c01, util::cp_windows1256 },
	{ 0x2001, util::cp_windows1256 },
	{ 0x2401, util::cp_windows1256 },
	{ 0x2801, util::cp_windows1256 },
	{ 0x2c01, util::cp_windows1256 },
	{ 0x3001, util::cp_windows1256 },
	{ 0x3401, util::cp_windows1256 },
	{ 0x3801, util::cp_windows1256 },
	{ 0x3c01, util::cp_windows1256 },
	{ 0x4001, util::cp_windows1256 },
};

util::codepage_id default_codepage_for_language(boost::uint32_t language) {
	
	const windows_language * entry = std::lower_bound(boost::begin(languages), boost::end(languages), language);
	if(entry != boost::end(languages) && entry->language_id == language) {
		return entry->codepage;
	}
	
	return util::cp_windows1252;
}

} // anonymous namespace

void language_entry::load(std::istream & is, const info & i) {
	
	if(i.version >= INNO_VERSION(4, 0, 0)) {
		is >> util::binary_string(name);
	}
	
	is >> util::binary_string(language_name);
	
	if(i.version == INNO_VERSION_EXT(5, 5, 7, 1)) {
		util::binary_string::skip(is);
	}
	
	is >> util::binary_string(dialog_font);
	is >> util::binary_string(title_font);
	is >> util::binary_string(welcome_font);
	is >> util::binary_string(copyright_font);
	
	if(i.version >= INNO_VERSION(4, 0, 0)) {
		is >> util::binary_string(data);
	}
	
	if(i.version >= INNO_VERSION(4, 0, 1)) {
		is >> util::binary_string(license_text);
		is >> util::binary_string(info_before);
		is >> util::binary_string(info_after);
	} else {
		license_text.clear(), info_before.clear(), info_after.clear();
	}
	
	language_id = util::load<boost::uint32_t>(is);
	
	if(i.version < INNO_VERSION(4, 2, 2)) {
		codepage = default_codepage_for_language(language_id);
	} else if(!i.version.is_unicode()) {
		codepage = util::load<boost::uint32_t>(is);
		if(!codepage) {
			codepage = util::cp_windows1252;
		}
	} else {
		if(i.version < INNO_VERSION(5, 3, 0)) {
			(void)util::load<boost::uint32_t>(is);
		}
		codepage = util::cp_utf16le;
	}
	
	if(i.version >= INNO_VERSION(4, 2, 2)) {
		util::to_utf8(language_name, util::cp_utf16le);
	} else {
		util::to_utf8(language_name, codepage);
	}
	
	dialog_font_size = util::load<boost::uint32_t>(is);
	
	if(i.version < INNO_VERSION(4, 1, 0)) {
		dialog_font_standard_height = util::load<boost::uint32_t>(is);
	} else {
		dialog_font_standard_height = 0;
	}
	
	title_font_size = util::load<boost::uint32_t>(is);
	welcome_font_size = util::load<boost::uint32_t>(is);
	copyright_font_size = util::load<boost::uint32_t>(is);
	
	if(i.version == INNO_VERSION_EXT(5, 5, 7, 1)) {
		util::load<boost::uint32_t>(is); // always 8 or 9?
	}
	
	if(i.version >= INNO_VERSION(5, 2, 3)) {
		right_to_left = util::load_bool(is);
	} else {
		right_to_left = false;
	}
	
}

void language_entry::decode(util::codepage_id cp) {
	
	util::to_utf8(name, cp);
	if(name.empty()) {
		name = "default";
	}
	
}

} // namespace setup
```

## File: `src/setup/language.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for language entries stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_LANGUAGE_HPP
#define INNOEXTRACT_SETUP_LANGUAGE_HPP

#include <string>
#include <iosfwd>

#include <boost/cstdint.hpp>

#include "util/encoding.hpp"

namespace setup {

struct info;

struct language_entry {
	
	// introduced in 2.0.1
	
	std::string name;
	std::string language_name;
	std::string dialog_font;
	std::string title_font;
	std::string welcome_font;
	std::string copyright_font;
	std::string data;
	std::string license_text;
	std::string info_before;
	std::string info_after;
	
	boost::uint32_t language_id;
	boost::uint32_t codepage;
	size_t dialog_font_size;
	size_t dialog_font_standard_height;
	size_t title_font_size;
	size_t welcome_font_size;
	size_t copyright_font_size;
	
	bool right_to_left;
	
	void load(std::istream & is, const info & i);
	
	void decode(util::codepage_id cp);
	
};

} // namespace setup

#endif // INNOEXTRACT_SETUP_LANGUAGE_HPP
```

## File: `src/setup/message.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/message.hpp"

#include <boost/cstdint.hpp>

#include "setup/info.hpp"
#include "setup/language.hpp"
#include "setup/version.hpp"
#include "util/encoding.hpp"
#include "util/load.hpp"
#include "util/log.hpp"

namespace setup {

void message_entry::load(std::istream & is, const info & i) {
	
	is >> util::encoded_string(name, i.codepage);
	is >> util::binary_string(value);
	
	language = util::load<boost::int32_t>(is);
	
	boost::uint32_t codepage;
	if(language < 0) {
		codepage = i.codepage;
	} else if(size_t(language) >= i.languages.size()) {
		if(!i.languages.empty()) {
			log_warning << "Language index out of bounds: " << language;
		}
		value.clear();
		return;
	} else {
		codepage = i.languages[size_t(language)].codepage;
	}
	
	util::to_utf8(value, codepage);
}

} // namespace setup
```

## File: `src/setup/message.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for custom localized messages stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_MESSAGE_HPP
#define INNOEXTRACT_SETUP_MESSAGE_HPP

#include <string>
#include <iosfwd>

namespace setup {

struct info;

struct message_entry {
	
	// introduced in 4.2.1
	
	// UTF-8 encoded name.
	std::string name;
	
	// Value encoded in the codepage specified at language index.
	std::string value;
	
	// Index into the default language entry list or -1.
	int language;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

#endif // INNOEXTRACT_SETUP_MESSAGE_HPP
```

## File: `src/setup/permission.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/permission.hpp"

#include "util/load.hpp"

namespace setup {

void permission_entry::load(std::istream & is, const info & /* i */) {
	
	is >> util::binary_string(permissions); // an array of TGrantPermissionEntry's
	
}

} // namespace setup
```

## File: `src/setup/permission.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for permission entries stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_PERMISSION_HPP
#define INNOEXTRACT_SETUP_PERMISSION_HPP

#include <string>
#include <iosfwd>

namespace setup {

struct info;

struct permission_entry {
	
	// introduced in 4.1.0
	
	std::string permissions;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

#endif // INNOEXTRACT_SETUP_PERMISSION_HPP
```

## File: `src/setup/registry.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/registry.hpp"

#include <boost/cstdint.hpp>

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/storedenum.hpp"

namespace setup {

namespace {

// 16-bit
STORED_ENUM_MAP(stored_registry_entry_type_0, registry_entry::None,
	registry_entry::None,
	registry_entry::String,
);

STORED_ENUM_MAP(stored_registry_entry_type_1, registry_entry::None,
	registry_entry::None,
	registry_entry::String,
	registry_entry::ExpandString,
	registry_entry::DWord,
	registry_entry::Binary,
	registry_entry::MultiString,
);

// starting with version 5.2.5
STORED_ENUM_MAP(stored_registry_entry_type_2, registry_entry::None,
	registry_entry::None,
	registry_entry::String,
	registry_entry::ExpandString,
	registry_entry::DWord,
	registry_entry::Binary,
	registry_entry::MultiString,
	registry_entry::QWord,
);

} // anonymous namespace

void registry_entry::load(std::istream & is, const info & i) {
	
	if(i.version < INNO_VERSION(1, 3, 0)) {
		(void)util::load<boost::uint32_t>(is); // uncompressed size of the entry
	}
	
	is >> util::encoded_string(key, i.codepage, i.header.lead_bytes);
	if(i.version.bits() != 16) {
		is >> util::encoded_string(name, i.codepage);
	} else {
		name.clear();
	}
	is >> util::binary_string(value);
	
	load_condition_data(is, i);
	
	if(i.version >= INNO_VERSION(4, 0, 11) && i.version < INNO_VERSION(4, 1, 0)) {
		is >> util::binary_string(permissions);
	} else {
		permissions.clear();
	}
	
	load_version_data(is, i.version);
	
	if(i.version.bits() != 16) {
		hive = hive_name(util::load<boost::uint32_t>(is) & ~0x80000000);
	} else {
		hive = Unset;
	}
	
	if(i.version >= INNO_VERSION(4, 1, 0)) {
		permission = util::load<boost::int16_t>(is);
	} else {
		permission = -1;
	}
	
	if(i.version >= INNO_VERSION(5, 2, 5)) {
		type = stored_enum<stored_registry_entry_type_2>(is).get();
	} else if(i.version.bits() != 16) {
		type = stored_enum<stored_registry_entry_type_1>(is).get();
	} else {
		type = stored_enum<stored_registry_entry_type_0>(is).get();
	}
	
	stored_flag_reader<flags> flagreader(is, i.version.bits());
	
	if(i.version.bits() != 16) {
		flagreader.add(CreateValueIfDoesntExist);
		flagreader.add(UninsDeleteValue);
	}
	flagreader.add(UninsClearValue);
	flagreader.add(UninsDeleteEntireKey);
	flagreader.add(UninsDeleteEntireKeyIfEmpty);
	if(i.version >= INNO_VERSION(1, 2, 6)) {
		flagreader.add(PreserveStringType);
	}
	if(i.version >= INNO_VERSION(1, 3, 9)) {
		flagreader.add(DeleteKey);
		flagreader.add(DeleteValue);
	}
	if(i.version >= INNO_VERSION(1, 3, 12)) {
		flagreader.add(NoError);
	}
	if(i.version >= INNO_VERSION(1, 3, 16)) {
		flagreader.add(DontCreateKey);
	}
	if(i.version >= INNO_VERSION(5, 1, 0)) {
		flagreader.add(Bits32);
		flagreader.add(Bits64);
	}
	
	options = flagreader.finalize();
}

} // namespace setup

NAMES(setup::registry_entry::flags, "Registry Option",
	"create value if doesn't exist",
	"uninstall delete value",
	"uninstall clear value",
	"uninstall delete key",
	"uninstall delete key if empty",
	"preserve string type",
	"delete key",
	"delete value",
	"no error",
	"don't create key",
	"32 bit",
	"64 bit",
)

NAMES(setup::registry_entry::hive_name, "Registry Hive",
	"HKCR",
	"HKCU",
	"HKLM",
	"HKU",
	"HKPD",
	"HKCC",
	"HKDD",
	"Unset",
)

NAMES(setup::registry_entry::value_type, "Registry Entry Type",
	"none",
	"string",
	"expand string",
	"dword",
	"binary",
	"multi string",
	"qword",
)
```

## File: `src/setup/registry.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for Windows registry entries stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_REGISTRY_HPP
#define INNOEXTRACT_SETUP_REGISTRY_HPP

#include <string>
#include <iosfwd>

#include "setup/item.hpp"
#include "setup/windows.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct info;

struct registry_entry : public item {
	
	FLAGS(flags,
		CreateValueIfDoesntExist,
		UninsDeleteValue,
		UninsClearValue,
		UninsDeleteEntireKey,
		UninsDeleteEntireKeyIfEmpty,
		PreserveStringType,
		DeleteKey,
		DeleteValue,
		NoError,
		DontCreateKey,
		Bits32,
		Bits64
	);
	
	enum hive_name {
		HKCR,
		HKCU,
		HKLM,
		HKU,
		HKPD,
		HKCC,
		HKDD,
		Unset,
	};
	
	enum value_type {
		None,
		String,
		ExpandString,
		DWord,
		Binary,
		MultiString,
		QWord,
	};
	
	std::string key;
	std::string name; // empty string means (Default) key
	std::string value;
	
	std::string permissions;
	
	hive_name hive;
	
	int permission; //!< index into the permission entry list
	
	value_type type;
	
	flags options;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_FLAGS(setup::registry_entry::flags)
NAMED_ENUM(setup::registry_entry::hive_name)
NAMED_ENUM(setup::registry_entry::value_type)

#endif // INNOEXTRACT_SETUP_REGISTRY_HPP
```

## File: `src/setup/run.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/run.hpp"

#include <boost/cstdint.hpp>

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/storedenum.hpp"

namespace setup {

namespace {

STORED_ENUM_MAP(stored_run_wait_condition, run_entry::WaitUntilTerminated,
	run_entry::WaitUntilTerminated,
	run_entry::NoWait,
	run_entry::WaitUntilIdle,
);

} // anonymous namespace

void run_entry::load(std::istream & is, const info & i) {
	
	if(i.version < INNO_VERSION(1, 3, 0)) {
		(void)util::load<boost::uint32_t>(is); // uncompressed size of the entry
	}
	
	is >> util::encoded_string(name, i.codepage, i.header.lead_bytes);
	is >> util::encoded_string(parameters, i.codepage, i.header.lead_bytes);
	is >> util::encoded_string(working_dir, i.codepage, i.header.lead_bytes);
	if(i.version >= INNO_VERSION(1, 3, 9)) {
		is >> util::encoded_string(run_once_id, i.codepage);
	} else {
		run_once_id.clear();
	}
	if(i.version >= INNO_VERSION(2, 0, 2)) {
		is >> util::encoded_string(status_message, i.codepage);
	} else {
		status_message.clear();
	}
	if(i.version >= INNO_VERSION(5, 1, 13)) {
		is >> util::encoded_string(verb, i.codepage);
	} else {
		verb.clear();
	}
	if(i.version >= INNO_VERSION(2, 0, 0) || i.version.is_isx()) {
		is >> util::encoded_string(description, i.codepage);
	}
	
	load_condition_data(is, i);
	
	load_version_data(is, i.version);
	
	if(i.version >= INNO_VERSION(1, 3, 24)) {
		show_command = util::load<boost::int32_t>(is);
	} else {
		show_command = 0;
	}
	
	wait = stored_enum<stored_run_wait_condition>(is).get();
	
	stored_flag_reader<flags> flagreader(is, i.version.bits());
	
	if(i.version >= INNO_VERSION(1, 2, 3)) {
		flagreader.add(ShellExec);
	}
	if(i.version >= INNO_VERSION(1, 3, 9) || (i.version.is_isx() && i.version >= INNO_VERSION(1, 3, 8))) {
		flagreader.add(SkipIfDoesntExist);
	}
	if(i.version >= INNO_VERSION(2, 0, 0)) {
		flagreader.add(PostInstall);
		flagreader.add(Unchecked);
		flagreader.add(SkipIfSilent);
		flagreader.add(SkipIfNotSilent);
	}
	if(i.version >= INNO_VERSION(2, 0, 8)) {
		flagreader.add(HideWizard);
	}
	if(i.version >= INNO_VERSION(5, 1, 10)) {
		flagreader.add(Bits32);
		flagreader.add(Bits64);
	}
	if(i.version >= INNO_VERSION(5, 2, 0)) {
		flagreader.add(RunAsOriginalUser);
	}
	if(i.version >= INNO_VERSION(6, 1, 0)) {
		flagreader.add(DontLogParameters);
	}
	if(i.version >= INNO_VERSION(6, 3, 0)) {
		flagreader.add(LogOutput);
	}
	
	options = flagreader.finalize();
}

} // namespace setup

NAMES(setup::run_entry::flags, "Run Option",
	"shell exec",
	"skip if doesn't exist",
	"post install",
	"unchecked",
	"skip if silent",
	"skip if not silent",
	"hide wizard",
	"32 bit",
	"64 bit",
	"run as original user",
	"don't log parameters",
	"log output",
)

NAMES(setup::run_entry::wait_condition, "Run Wait Type",
	"wait until terminated",
	"no wait",
	"wait until idle",
)
```

## File: `src/setup/run.hpp`
```
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for custom command entries stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_RUN_HPP
#define INNOEXTRACT_SETUP_RUN_HPP

#include <string>
#include <iosfwd>

#include "setup/item.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct info;

struct run_entry : public item {
	
	FLAGS(flags,
		ShellExec,
		SkipIfDoesntExist,
		PostInstall,
		Unchecked,
		SkipIfSilent,
		SkipIfNotSilent,
		HideWizard,
		Bits32,
		Bits64,
		RunAsOriginalUser,
		DontLogParameters,
		LogOutput
	);
	
	enum wait_condition {
		WaitUntilTerminated,
		NoWait,
		WaitUntilIdle,
	};
	
	std::string name;
	std::string parameters;
	std::string working_dir;
	std::string run_once_id;
	std::string status_message;
	std::string verb;
	std::string description;
	
	int show_command;
	
	wait_condition wait;
	
	flags options;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_FLAGS(setup::run_entry::flags)
NAMED_ENUM(setup::run_entry::wait_condition)

#endif // INNOEXTRACT_SETUP_RUN_HPP
```

## File: `src/setup/task.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/task.hpp"

#include <boost/cstdint.hpp>

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/storedenum.hpp"

namespace setup {

void task_entry::load(std::istream & is, const info & i) {
	
	is >> util::encoded_string(name, i.codepage);
	is >> util::encoded_string(description, i.codepage);
	is >> util::encoded_string(group_description, i.codepage);
	is >> util::encoded_string(components, i.codepage);
	if(i.version >= INNO_VERSION(4, 0, 1)) {
		is >> util::encoded_string(languages, i.codepage);
	} else {
		languages.clear();
	}
	if(i.version >= INNO_VERSION(4, 0, 0) || (i.version.is_isx() && i.version >= INNO_VERSION(1, 3, 24))) {
		is >> util::encoded_string(check, i.codepage);
	} else {
		check.clear();
	}
	if(i.version >= INNO_VERSION(4, 0, 0) || (i.version.is_isx() && i.version >= INNO_VERSION(3, 0, 3))) {
		level = util::load<boost::int32_t>(is);
	} else {
		level = 0;
	}
	if(i.version >= INNO_VERSION(4, 0, 0) || (i.version.is_isx() && i.version >= INNO_VERSION(3, 0, 4))) {
		used = util::load_bool(is);
	} else {
		used = true;
	}
	
	winver.load(is, i.version);
	
	stored_flag_reader<flags> flagreader(is);
	
	flagreader.add(Exclusive);
	flagreader.add(Unchecked);
	if(i.version >= INNO_VERSION(2, 0, 5)) {
		flagreader.add(Restart);
	}
	if(i.version >= INNO_VERSION(2, 0, 6)) {
		flagreader.add(CheckedOnce);
	}
	if(i.version >= INNO_VERSION(4, 2, 3)) {
		flagreader.add(DontInheritCheck);
	}
	
	options = flagreader.finalize();
}

} // namespace setup

NAMES(setup::task_entry::flags, "Setup Task Option",
	"exclusive",
	"unchecked",
	"restart",
	"checked once",
	"don't inherit check",
)
```

## File: `src/setup/task.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for setup tasks stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_TASK_HPP
#define INNOEXTRACT_SETUP_TASK_HPP

#include <string>
#include <iosfwd>

#include "setup/windows.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct info;

struct task_entry {
	
	// introduced in 2.0.0
	
	FLAGS(flags,
		Exclusive,
		Unchecked,
		Restart,
		CheckedOnce,
		DontInheritCheck
	);
	
	std::string name;
	std::string description;
	std::string group_description;
	std::string components;
	std::string languages;
	std::string check;
	
	int level;
	bool used;
	
	windows_version_range winver;
	
	flags options;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_FLAGS(setup::task_entry::flags)

#endif // INNOEXTRACT_SETUP_TASK_HPP
```

## File: `src/setup/type.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/type.hpp"

#include "setup/info.hpp"
#include "setup/version.hpp"
#include "util/load.hpp"
#include "util/storedenum.hpp"

namespace setup {

namespace {

FLAGS(type_flags,
	CustomSetupType
);

STORED_FLAGS_MAP(stored_type_flags,
	CustomSetupType,
);

STORED_ENUM_MAP(stored_setup_type, type_entry::User,
	type_entry::User,
	type_entry::DefaultFull,
	type_entry::DefaultCompact,
	type_entry::DefaultCustom,
);

} // anonymous namespace

} // namespace setup

NAMED_FLAGS(setup::type_flags)

namespace setup {

void type_entry::load(std::istream & is, const info & i) {
	
	USE_FLAG_NAMES(setup::type_flags)
	
	is >> util::encoded_string(name, i.codepage);
	is >> util::encoded_string(description, i.codepage);
	if(i.version >= INNO_VERSION(4, 0, 1)) {
		is >> util::encoded_string(languages, i.codepage);
	} else {
		languages.clear();
	}
	if(i.version >= INNO_VERSION(4, 0, 0) || (i.version.is_isx() && i.version >= INNO_VERSION(1, 3, 24))) {
		is >> util::encoded_string(check, i.codepage);
	} else {
		check.clear();
	}
	
	winver.load(is, i.version);
	
	type_flags options = stored_flags<stored_type_flags>(is).get();
	custom_type = ((options & CustomSetupType) != 0);
	
	if(i.version >= INNO_VERSION(4, 0, 3)) {
		type = stored_enum<stored_setup_type>(is).get();
	} else {
		type = User;
	}
	
	if(i.version >= INNO_VERSION(4, 0, 0)) {
		size = util::load<boost::uint64_t>(is);
	} else {
		size = util::load<boost::uint32_t>(is);
	}
}

} // namespace setup

NAMES(setup::type_flags, "Setyp Type Option",
	"is custom",
)

NAMES(setup::type_entry::setup_type, "Setyp Type",
	"user",
	"default full",
	"default compact",
	"default custom",
)
```

## File: `src/setup/type.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for setup types stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_TYPE_HPP
#define INNOEXTRACT_SETUP_TYPE_HPP

#include <string>
#include <iosfwd>

#include <boost/cstdint.hpp>

#include "setup/windows.hpp"
#include "util/enum.hpp"
#include "util/flags.hpp"

namespace setup {

struct info;

struct type_entry {
	
	// introduced in 2.0.0
	
	enum setup_type {
		User,
		DefaultFull,
		DefaultCompact,
		DefaultCustom
	};
	
	std::string name;
	std::string description;
	std::string languages;
	std::string check;
	
	windows_version_range winver;
	
	bool custom_type;
	
	setup_type type;
	
	boost::uint64_t size;
	
	void load(std::istream & is, const info & i);
	
};

} // namespace setup

NAMED_ENUM(setup::type_entry::setup_type)

#endif // INNOEXTRACT_SETUP_TYPE_HPP
```

## File: `src/setup/version.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/version.hpp"

#include <cstring>
#include <algorithm>
#include <istream>
#include <ostream>

#include <boost/version.hpp>
#include <boost/static_assert.hpp>
#include <boost/lexical_cast.hpp>
#include "boost/algorithm/string.hpp"
#include <boost/range/begin.hpp>
#include <boost/range/end.hpp>
#include <boost/range/size.hpp>

#include "util/load.hpp"
#include "util/log.hpp"

namespace setup {

namespace {

typedef char stored_legacy_version[12];

struct known_legacy_version {
	
	char name[13]; // terminating 0 byte is ignored
	
	version_constant version;
	version::flags variant;
	
	operator version_constant() const { return version; }
	
};

const known_legacy_version legacy_versions[] = {
	{ "i1.2.10--16\x1a", INNO_VERSION(1, 2, 10), version::Bits16 },
	{ "i1.2.10--32\x1a", INNO_VERSION(1, 2, 10), 0 },
};

typedef char stored_version[64];

struct known_version {
	
	stored_version name;
	
	version_constant version;
	version::flags variant;
	
	operator version_constant() const { return version; }
	
};

const known_version versions[] = {
	{ "Inno Setup Setup Data (1.3.3)",                      INNO_VERSION_EXT(1, 3,  3, 0), 0 },
	{ "Inno Setup Setup Data (1.3.9)",                      INNO_VERSION_EXT(1, 3,  9, 0), 0 },
	{ "Inno Setup Setup Data (1.3.10)",                     INNO_VERSION_EXT(1, 3, 10, 0), 0 },
	{ "Inno Setup Setup Data (1.3.10) with ISX (1.3.10)",   INNO_VERSION_EXT(1, 3, 10, 0), version::ISX },
	{ "Inno Setup Setup Data (1.3.12) with ISX (1.3.12.1)", INNO_VERSION_EXT(1, 3, 12, 1), version::ISX },
	{ "Inno Setup Setup Data (1.3.21)",     /* ambiguous */ INNO_VERSION_EXT(1, 3, 21, 0), 0 },
	{ "Inno Setup Setup Data (1.3.21) with ISX (1.3.17)",   INNO_VERSION_EXT(1, 3, 21, 0), version::ISX },
	{ "Inno Setup Setup Data (1.3.24)",                     INNO_VERSION_EXT(1, 3, 24, 0), 0 },
	{ "Inno Setup Setup Data (1.3.21) with ISX (1.3.24)",   INNO_VERSION_EXT(1, 3, 24, 0), version::ISX },
	{ "Inno Setup Setup Data (1.3.25)",                     INNO_VERSION_EXT(1, 3, 25, 0), 0 },
	{ "Inno Setup Setup Data (1.3.25) with ISX (1.3.25)",   INNO_VERSION_EXT(1, 3, 25, 0), version::ISX },
	{ "Inno Setup Setup Data (2.0.0)",                      INNO_VERSION_EXT(2, 0,  0, 0), 0 },
	{ "Inno Setup Setup Data (2.0.1)",      /* ambiguous */ INNO_VERSION_EXT(2, 0,  1, 0), 0 },
	{ "Inno Setup Setup Data (2.0.2)",                      INNO_VERSION_EXT(2, 0,  2, 0), 0 },
	{ "Inno Setup Setup Data (2.0.5)",                      INNO_VERSION_EXT(2, 0,  5, 0), 0 },
	{ "Inno Setup Setup Data (2.0.6a)",                     INNO_VERSION_EXT(2, 0,  6, 0), 0 },
	{ "Inno Setup Setup Data (2.0.6a) with ISX (2.0.3)",    INNO_VERSION_EXT(2, 0,  6, 0), version::ISX },
	{ "Inno Setup Setup Data (2.0.7)",                      INNO_VERSION_EXT(2, 0,  7, 0), 0 },
	{ "Inno Setup Setup Data (2.0.8)",                      INNO_VERSION_EXT(2, 0,  8, 0), 0 },
	{ "Inno Setup Setup Data (2.0.8) with ISX (2.0.3)",     INNO_VERSION_EXT(2, 0,  8, 0), version::ISX },
	{ "Inno Setup Setup Data (2.0.8) with ISX (2.0.10)",    INNO_VERSION_EXT(2, 0, 10, 0), version::ISX },
	{ "Inno Setup Setup Data (2.0.11)",                     INNO_VERSION_EXT(2, 0, 11, 0), 0 },
	{ "Inno Setup Setup Data (2.0.11) with ISX (2.0.11)",   INNO_VERSION_EXT(2, 0, 11, 0), version::ISX },
	{ "Inno Setup Setup Data (2.0.17)",                     INNO_VERSION_EXT(2, 0, 17, 0), 0 },
	{ "Inno Setup Setup Data (2.0.17) with ISX (2.0.11)",   INNO_VERSION_EXT(2, 0, 17, 0), version::ISX },
	{ "Inno Setup Setup Data (2.0.18)",                     INNO_VERSION_EXT(2, 0, 18, 0), 0 },
	{ "Inno Setup Setup Data (2.0.18) with ISX (2.0.11)",   INNO_VERSION_EXT(2, 0, 18, 0), version::ISX },
	{ "Inno Setup Setup Data (3.0.0a)",                     INNO_VERSION_EXT(3, 0,  0, 0), 0 },
	{ "Inno Setup Setup Data (3.0.1)",                      INNO_VERSION_EXT(3, 0,  1, 0), 0 },
	{ "Inno Setup Setup Data (3.0.1) with ISX (3.0.0)",     INNO_VERSION_EXT(3, 0,  1, 0), version::ISX },
	{ "Inno Setup Setup Data (3.0.3)",      /* ambiguous */ INNO_VERSION_EXT(3, 0,  3, 0), 0 },
	{ "Inno Setup Setup Data (3.0.3) with ISX (3.0.3)",     INNO_VERSION_EXT(3, 0,  3, 0), version::ISX },
	{ "Inno Setup Setup Data (3.0.4)",                      INNO_VERSION_EXT(3, 0,  4, 0), 0 },
	{ "My Inno Setup Extensions Setup Data (3.0.4)",        INNO_VERSION_EXT(3, 0,  4, 0), version::ISX },
	{ "Inno Setup Setup Data (3.0.5)",                      INNO_VERSION_EXT(3, 0,  5, 0), 0 },
	{ "My Inno Setup Extensions Setup Data (3.0.6.1)",      INNO_VERSION_EXT(3, 0,  6, 1), version::ISX },
	{ "Inno Setup Setup Data (4.0.0a)",                     INNO_VERSION_EXT(4, 0,  0, 0), 0 },
	{ "Inno Setup Setup Data (4.0.1)",                      INNO_VERSION_EXT(4, 0,  1, 0), 0 },
	{ "Inno Setup Setup Data (4.0.3)",                      INNO_VERSION_EXT(4, 0,  3, 0), 0 },
	{ "Inno Setup Setup Data (4.0.5)",                      INNO_VERSION_EXT(4, 0,  5, 0), 0 },
	{ "Inno Setup Setup Data (4.0.9)",                      INNO_VERSION_EXT(4, 0,  9, 0), 0 },
	{ "Inno Setup Setup Data (4.0.10)",                     INNO_VERSION_EXT(4, 0, 10, 0), 0 },
	{ "Inno Setup Setup Data (4.0.11)",                     INNO_VERSION_EXT(4, 0, 11, 0), 0 },
	{ "Inno Setup Setup Data (4.1.0)",                      INNO_VERSION_EXT(4, 1,  0, 0), 0 },
	{ "Inno Setup Setup Data (4.1.2)",                      INNO_VERSION_EXT(4, 1,  2, 0), 0 },
	{ "Inno Setup Setup Data (4.1.3)",                      INNO_VERSION_EXT(4, 1,  3, 0), 0 },
	{ "Inno Setup Setup Data (4.1.4)",                      INNO_VERSION_EXT(4, 1,  4, 0), 0 },
	{ "Inno Setup Setup Data (4.1.5)",                      INNO_VERSION_EXT(4, 1,  5, 0), 0 },
	{ "Inno Setup Setup Data (4.1.6)",                      INNO_VERSION_EXT(4, 1,  6, 0), 0 },
	{ "Inno Setup Setup Data (4.1.8)",                      INNO_VERSION_EXT(4, 1,  8, 0), 0 },
	{ "Inno Setup Setup Data (4.2.0)",                      INNO_VERSION_EXT(4, 2,  0, 0), 0 },
	{ "Inno Setup Setup Data (4.2.1)",                      INNO_VERSION_EXT(4, 2,  1, 0), 0 },
	{ "Inno Setup Setup Data (4.2.2)",                      INNO_VERSION_EXT(4, 2,  2, 0), 0 },
	{ "Inno Setup Setup Data (4.2.3)",      /* ambiguous */ INNO_VERSION_EXT(4, 2,  3, 0), 0 },
	{ "Inno Setup Setup Data (4.2.4)",                      INNO_VERSION_EXT(4, 2,  4, 0), 0 },
	{ "Inno Setup Setup Data (4.2.5)",                      INNO_VERSION_EXT(4, 2,  5, 0), 0 },
	{ "Inno Setup Setup Data (4.2.6)",                      INNO_VERSION_EXT(4, 2,  6, 0), 0 },
	{ "Inno Setup Setup Data (5.0.0)",                      INNO_VERSION_EXT(5, 0,  0, 0), 0 },
	{ "Inno Setup Setup Data (5.0.1)",                      INNO_VERSION_EXT(5, 0,  1, 0), 0 },
	{ "Inno Setup Setup Data (5.0.3)",                      INNO_VERSION_EXT(5, 0,  3, 0), 0 },
	{ "Inno Setup Setup Data (5.0.4)",                      INNO_VERSION_EXT(5, 0,  4, 0), 0 },
	{ "Inno Setup Setup Data (5.1.0)",                      INNO_VERSION_EXT(5, 1,  0, 0), 0 },
	{ "Inno Setup Setup Data (5.1.2)",                      INNO_VERSION_EXT(5, 1,  2, 0), 0 },
	{ "Inno Setup Setup Data (5.1.7)",                      INNO_VERSION_EXT(5, 1,  7, 0), 0 },
	{ "Inno Setup Setup Data (5.1.10)",                     INNO_VERSION_EXT(5, 1, 10, 0), 0 },
	{ "Inno Setup Setup Data (5.1.13)",                     INNO_VERSION_EXT(5, 1, 13, 0), 0 },
	{ "Inno Setup Setup Data (5.2.0)",                      INNO_VERSION_EXT(5, 2,  0, 0), 0 },
	{ "Inno Setup Setup Data (5.2.1)",                      INNO_VERSION_EXT(5, 2,  1, 0), 0 },
	{ "Inno Setup Setup Data (5.2.3)",                      INNO_VERSION_EXT(5, 2,  3, 0), 0 },
	{ "Inno Setup Setup Data (5.2.5)",                      INNO_VERSION_EXT(5, 2,  5, 0), 0 },
	{ "Inno Setup Setup Data (5.2.5) (u)",                  INNO_VERSION_EXT(5, 2,  5, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.3.0)",                      INNO_VERSION_EXT(5, 3,  0, 0), 0 },
	{ "Inno Setup Setup Data (5.3.0) (u)",                  INNO_VERSION_EXT(5, 3,  0, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.3.3)",                      INNO_VERSION_EXT(5, 3,  3, 0), 0 },
	{ "Inno Setup Setup Data (5.3.3) (u)",                  INNO_VERSION_EXT(5, 3,  3, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.3.5)",                      INNO_VERSION_EXT(5, 3,  5, 0), 0 },
	{ "Inno Setup Setup Data (5.3.5) (u)",                  INNO_VERSION_EXT(5, 3,  5, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.3.6)",                      INNO_VERSION_EXT(5, 3,  6, 0), 0 },
	{ "Inno Setup Setup Data (5.3.6) (u)",                  INNO_VERSION_EXT(5, 3,  6, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.3.7)",                      INNO_VERSION_EXT(5, 3,  7, 0), 0 },
	{ "Inno Setup Setup Data (5.3.7) (u)",                  INNO_VERSION_EXT(5, 3,  7, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.3.8)",                      INNO_VERSION_EXT(5, 3,  8, 0), 0 },
	{ "Inno Setup Setup Data (5.3.8) (u)",                  INNO_VERSION_EXT(5, 3,  8, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.3.9)",                      INNO_VERSION_EXT(5, 3,  9, 0), 0 },
	{ "Inno Setup Setup Data (5.3.9) (u)",                  INNO_VERSION_EXT(5, 3,  9, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.3.10)",                     INNO_VERSION_EXT(5, 3, 10, 0), 0 },
	{ "Inno Setup Setup Data (5.3.10) (u)", /* ambiguous */ INNO_VERSION_EXT(5, 3, 10, 0), version::Unicode },
	{ "" /* BlackBox v1? */,                                INNO_VERSION_EXT(5, 3, 10, 1), 0 },
	{ "" /* BlackBox v1? */,                                INNO_VERSION_EXT(5, 3, 10, 1), version::Unicode },
	{ "Inno Setup Setup Data (5.4.2)",                      INNO_VERSION_EXT(5, 4,  2, 0), 0 },
	{ "Inno Setup Setup Data (5.4.2) (u)",  /* ambiguous */ INNO_VERSION_EXT(5, 4,  2, 0), version::Unicode },
	{ "" /* BlackBox v1? */,                                INNO_VERSION_EXT(5, 4,  2, 1), 0 },
	{ "" /* BlackBox v1? */,                                INNO_VERSION_EXT(5, 4,  2, 1), version::Unicode },
	{ "Inno Setup Setup Data (5.5.0)",                      INNO_VERSION_EXT(5, 5,  0, 0), 0 },
	{ "Inno Setup Setup Data (5.5.0) (u)",  /* ambiguous */ INNO_VERSION_EXT(5, 5,  0, 0), version::Unicode },
	{ "" /* BlackBox v2 / Inno Setup Ultra */,              INNO_VERSION_EXT(5, 5,  0, 1), 0 },
	{ "" /* BlackBox v2 / Inno Setup Ultra */,              INNO_VERSION_EXT(5, 5,  0, 1), version::Unicode },
	{ "Inno Setup Setup Data (5.5.6)",                      INNO_VERSION_EXT(5, 5,  6, 0), 0 },
	{ "Inno Setup Setup Data (5.5.6) (u)",                  INNO_VERSION_EXT(5, 5,  6, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.5.7)",      /* ambiguous */ INNO_VERSION_EXT(5, 5,  7, 0), 0 },
	{ "Inno Setup Setup Data (5.5.7) (u)",  /* ambiguous */ INNO_VERSION_EXT(5, 5,  7, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.5.7) (U)",  /* ambiguous */ INNO_VERSION_EXT(5, 5,  7, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.5.8) (u)", /* unofficial */ INNO_VERSION_EXT(5, 5,  7, 0), version::Unicode },
	{ "" /* unknown 5.5.7 (u) variant */,   /* ambiguous */ INNO_VERSION_EXT(5, 5,  7, 1), 0 },
	{ "" /* unknown 5.5.7 (u) variant */,   /* ambiguous */ INNO_VERSION_EXT(5, 5,  7, 1), version::Unicode },
	{ "Inno Setup Setup Data (5.6.0)",                      INNO_VERSION_EXT(5, 6,  0, 0), 0 },
	{ "Inno Setup Setup Data (5.6.0) (u)",                  INNO_VERSION_EXT(5, 6,  0, 0), version::Unicode },
	{ "Inno Setup Setup Data (5.6.2)",     /* prerelease */ INNO_VERSION_EXT(5, 6,  2, 0), 0 },
	{ "Inno Setup Setup Data (5.6.2) (u)", /* prerelease */ INNO_VERSION_EXT(5, 6,  2, 0), version::Unicode },
	{ "Inno Setup Setup Data (6.0.0) (u)",                  INNO_VERSION_EXT(6, 0,  0, 0), version::Unicode },
	{ "Inno Setup Setup Data (6.1.0) (u)",                  INNO_VERSION_EXT(6, 1,  0, 0), version::Unicode },
	{ "Inno Setup Setup Data (6.3.0)",                      INNO_VERSION_EXT(6, 3,  0, 0), version::Unicode },
	{ "Inno Setup Setup Data (6.4.0)",     /* prerelease */ INNO_VERSION_EXT(6, 4,  0, 0), version::Unicode },
	{ "Inno Setup Setup Data (6.4.0.1)",        /* 6.4.0 */ INNO_VERSION_EXT(6, 4,  0, 1), version::Unicode },
};

} // anonymous namespace

std::ostream & operator<<(std::ostream & os, const version & version) {
	
	os << version.a() << '.' << version.b() << '.' << version.c();
	if(version.d()) {
		os << '.' << version.d();
	}
	
	if(version.is_unicode()) {
		os << " (unicode)";
	}
	
	if(version.bits() != 32) {
		os << " (" << int(version.bits()) << "-bit)";
	}
	
	if(version.is_isx()) {
		os << " (isx)";
	}
	
	return os;
}

void version::load(std::istream & is) {
	
	static const char digits[] = "0123456789";
	
	BOOST_STATIC_ASSERT(sizeof(stored_legacy_version) <= sizeof(stored_version));
	
	stored_legacy_version legacy_version;
	is.read(legacy_version, std::streamsize(sizeof(legacy_version)));
	
	if(legacy_version[0] == 'i' && legacy_version[sizeof(legacy_version) - 1] == '\x1a') {
		
		for(size_t i = 0; i < size_t(boost::size(legacy_versions)); i++) {
			if(!memcmp(legacy_version, legacy_versions[i].name, sizeof(legacy_version))) {
				value = legacy_versions[i].version;
				variant = legacy_versions[i].variant;
				known = true;
				debug("known legacy version: \"" << versions[i].name << '"');
				return;
			}
		}
		
		debug("unknown legacy version: \""
		      << std::string(legacy_version, sizeof(legacy_version)) << '"');
		
		if(legacy_version[0] != 'i' || legacy_version[2] != '.' || legacy_version[4] != '.'
		   || legacy_version[7] != '-' || legacy_version[8] != '-') {
			throw version_error();
		}
		
		if(legacy_version[9] == '1' && legacy_version[10] == '6') {
			variant = Bits16;
		} else if(legacy_version[9] == '3' && legacy_version[10] == '2') {
			variant = 0;
		} else {
			throw version_error();
		}
		
		std::string version_str(legacy_version, sizeof(legacy_version));
		
		try {
			unsigned a = util::to_unsigned(version_str.data() + 1, 1);
			unsigned b = util::to_unsigned(version_str.data() + 3, 1);
			unsigned c = util::to_unsigned(version_str.data() + 5, 2);
			value = INNO_VERSION(a, b, c);
		} catch(const boost::bad_lexical_cast &) {
			throw version_error();
		}
		
		known = false;
		
		return;
	}
	
	stored_version version_string;
	BOOST_STATIC_ASSERT(sizeof(legacy_version) <= sizeof(version_string));
	memcpy(version_string, legacy_version, sizeof(legacy_version));
	is.read(version_string + sizeof(legacy_version),
	        std::streamsize(sizeof(version_string) - sizeof(legacy_version)));
	
	
	for(size_t i = 0; i < size_t(boost::size(versions)); i++) {
		if(versions[i].name[0] != '\0' && !memcmp(version_string, versions[i].name, sizeof(version_string))) {
			value = versions[i].version;
			variant = versions[i].variant;
			known = true;
			debug("known version: \"" << versions[i].name << '"');
			return;
		}
	}
	
	char * end = std::find(version_string, version_string + boost::size(version_string), '\0');
	std::string version_str(version_string, end);
	debug("unknown version: \"" << version_str << '"');
	if(!boost::contains(version_str, "Inno Setup")) {
		throw version_error();
	}
	
	value = 0;
	size_t bracket = version_str.find('(');
	for(; bracket != std::string::npos; bracket = version_str.find('(', bracket + 1)) {
		
		if(version_str.length() - bracket < 6) {
			continue;
		}
		
		try {
			
			size_t a_start = bracket + 1;
			size_t a_end = version_str.find_first_not_of(digits, a_start);
			if(a_end == std::string::npos || version_str[a_end] != '.') {
				continue;
			}
			unsigned a = util::to_unsigned(version_str.data() + a_start, a_end - a_start);
			
			size_t b_start = a_end + 1;
			size_t b_end = version_str.find_first_not_of(digits, b_start);
			if(b_end == std::string::npos || version_str[b_end] != '.') {
				continue;
			}
			unsigned b = util::to_unsigned(version_str.data() + b_start, b_end - b_start);
			
			size_t c_start = b_end + 1;
			size_t c_end = version_str.find_first_not_of(digits, c_start);
			if(c_end == std::string::npos) {
				continue;
			}
			unsigned c = util::to_unsigned(version_str.data() + c_start, c_end - c_start);
			
			size_t d_start = c_end;
			if(version_str[d_start] == 'a') {
				if(d_start + 1 >= version_str.length()) {
					continue;
				}
				d_start++;
			}
			
			unsigned d = 0;
			if(version_str[d_start] == '.') {
				d_start++;
				size_t d_end = version_str.find_first_not_of(digits, d_start);
				if(d_end != std::string::npos && d_end != d_start) {
					d = util::to_unsigned(version_str.data() + d_start, d_end - d_start);
				}
			}
			
			value = std::max(value, INNO_VERSION_EXT(a, b, c, d));
			
		} catch(const boost::bad_lexical_cast &) {
			continue;
		}
	}
	if(!value) {
		throw version_error();
	}
	
	variant = 0;
	if(value >= INNO_VERSION(6, 3, 0) ||
	   boost::contains(version_str, "(u)") || boost::contains(version_str, "(U)")) {
		variant |= Unicode;
	}
	if(boost::contains(version_str, "My Inno Setup Extensions") || boost::contains(version_str, "with ISX")) {
		variant |= ISX;
	}
	
	known = false;
}

bool version::is_ambiguous() const {
	
	if(value == INNO_VERSION(1, 3, 21)) {
		// might be either 1.3.21 or 1.3.24
		return true;
	}
	
	if(value == INNO_VERSION(2, 0, 1)) {
		// might be either 2.0.1 or 2.0.2
		return true;
	}
	
	if(value == INNO_VERSION(3, 0, 3)) {
		// might be either 3.0.3 or 3.0.4
		return true;
	}
	
	if(value == INNO_VERSION(4, 2, 3)) {
		// might be either 4.2.3 or 4.2.4
		return true;
	}
	
	if(value == INNO_VERSION(5, 3, 10)) {
		// might be either 5.3.10 or 5.3.10.1
		return true;
	}
	
	if(value == INNO_VERSION(5, 4, 2)) {
		// might be either 5.4.2 or 5.4.2.1
		return true;
	}
	
	if(value == INNO_VERSION(5, 5, 0)) {
		// might be either 5.5.0 or 5.5.0.1
		return true;
	}
	
	if(value == INNO_VERSION(5, 5, 7) || value == INNO_VERSION_EXT(5, 5, 7, 1)) {
		// might be either 5.5.7, an unknown modification of 5.5.7, or 5.6.0
		return true;
	}
	
	return false;
}

version_constant version::next() {
	
	const known_legacy_version * legacy_end = boost::end(legacy_versions);
	const known_legacy_version * legacy_result;
	legacy_result = std::upper_bound(boost::begin(legacy_versions), legacy_end, value);
	while(legacy_result != legacy_end && legacy_result->variant != variant) {
		legacy_result++;
	}
	if(legacy_result != legacy_end) {
		return legacy_result->version;
	}
	 
	const known_version * end = boost::end(versions);
	const known_version * result = std::upper_bound(boost::begin(versions), end, value);
	while(result != end && result->variant != variant) {
		result++;
	}
	if(result != end) {
		return result->version;
	}
	
	return 0;
}

} // namespace setup
```

## File: `src/setup/version.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Inno Setup version number utilities.
 */
#ifndef INNOEXTRACT_SETUP_VERSION_HPP
#define INNOEXTRACT_SETUP_VERSION_HPP

#include <iosfwd>
#include <exception>

#include <boost/cstdint.hpp>

#include "util/flags.hpp"

namespace setup {

struct version_error : public std::exception { };

typedef boost::uint32_t version_constant;
#define INNO_VERSION_EXT(a, b, c, d) ( \
	  (::setup::version_constant(a) << 24) \
	| (::setup::version_constant(b) << 16) \
	| (::setup::version_constant(c) <<  8) \
	| (::setup::version_constant(d) <<  0) \
)
#define INNO_VERSION(a, b, c) INNO_VERSION_EXT(a, b, c, 0)

struct version {
	
	FLAGS(flags,
		Bits16,
		Unicode,
		ISX
	);
	
	version_constant value;
	
	flags variant;
	
	bool known;
	
	version() : value(0), variant(0), known(false) { }
	
	version(version_constant v, flags type = 0, bool is_known = false)
		: value(v), variant(type), known(is_known) { }
	
	
	version(boost::uint8_t a, boost::uint8_t b, boost::uint8_t c, boost::uint8_t d = 0,
	        flags type = 0, bool is_known = false)
		: value(INNO_VERSION_EXT(a, b, c, d)), variant(type), known(is_known) { }
	
	unsigned int a() const { return  value >> 24;         }
	unsigned int b() const { return (value >> 16) & 0xff; }
	unsigned int c() const { return (value >>  8) & 0xff; }
	unsigned int d() const { return  value        & 0xff; }
	
	void load(std::istream & is);
	
	boost::uint16_t bits() const { return (variant & Bits16) ? 16 : 32; }
	bool is_unicode() const { return (variant & Unicode) != 0; }
	bool is_isx() const { return (variant & ISX) != 0; }
	
	//! \return true if the version stored might not be correct
	bool is_ambiguous() const;
	
	operator version_constant() const {
		return value;
	}
	
	version_constant next();
	
};

std::ostream & operator<<(std::ostream & os, const version & version);

} // namespace setup

#endif // INNOEXTRACT_SETUP_VERSION_HPP
```

## File: `src/setup/windows.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "setup/windows.hpp"

#include <ostream>

#include <boost/cstdint.hpp>
#include <boost/range/size.hpp>

#include "setup/version.hpp"
#include "util/load.hpp"

namespace setup {

const windows_version windows_version::none = { { 0, 0, 0 }, { 0, 0, 0 }, { 0, 0 } };

void windows_version::data::load(std::istream & is, const version & version) {
	
	if(version >= INNO_VERSION(1, 3, 19)) {
		build = util::load<boost::uint16_t>(is);
	} else {
		build = 0;
	}
	
	minor = util::load<boost::uint8_t>(is);
	major = util::load<boost::uint8_t>(is);
	
}

void windows_version::load(std::istream & is, const version & version) {
	
	win_version.load(is, version);
	nt_version.load(is, version);
	
	if(version >= INNO_VERSION(1, 3, 19)) {
		nt_service_pack.minor = util::load<boost::uint8_t>(is);
		nt_service_pack.major = util::load<boost::uint8_t>(is);
	} else {
		nt_service_pack.major = 0, nt_service_pack.minor = 0;
	}
	
}

void windows_version_range::load(std::istream & is, const version & version) {
	begin.load(is, version);
	end.load(is, version);
}


namespace {

struct windows_version_name {
	
	const char * name;
	
	windows_version::data version;
	
};

windows_version_name windows_version_names[] = {
	{ "Windows 1.0", { 1, 4, 0 } },
	{ "Windows 2.0", { 2, 11, 0 } },
	{ "Windows 3.0", { 3, 0, 0 } },
	{ "Windows for Workgroups 3.11", { 3, 11, 0 } },
	{ "Windows 95", { 4, 0, 950 } },
	{ "Windows 98", { 4, 1, 1998 } },
	{ "Windows 98 Second Edition", { 4, 1, 2222 } },
	{ "Windows ME", { 4, 90, 3000 } },
};

windows_version_name windows_nt_version_names[] = {
	{ "Windows NT Workstation 3.5", { 3, 5, 807 } },
	{ "Windows NT 3.1", { 3, 10, 528 } },
	{ "Windows NT Workstation 3.51", { 3, 51, 1057 } },
	{ "Windows NT Workstation 4.0", { 4, 0, 1381 } },
	{ "Windows 2000", { 5, 0, 2195 } },
	{ "Windows XP", { 5, 1, 2600 } },
	{ "Windows XP x64", { 5, 2, 3790 } },
	{ "Windows Vista", { 6, 0, 6000 } },
	{ "Windows 7", { 6, 1, 7600 } },
	{ "Windows 8", { 6, 2, 0 } },
	{ "Windows 8.1", { 6, 3, 0 } },
	{ "Windows 10", { 10, 0, 0 } },
};

const char * get_version_name(const windows_version::data & version, bool nt = false) {
	
	if(nt && version.major == 10 && version.minor == 0 && version.build >= 22000) {
		return "Windows 11";
	}
	
	windows_version_name * names;
	size_t count;
	if(nt) {
		names = windows_nt_version_names, count = size_t(boost::size(windows_nt_version_names));
	} else {
		names = windows_version_names, count = size_t(boost::size(windows_version_names));
	}
	
	for(size_t i = 0; i < count; i++) {
		const windows_version_name & v = names[i];
		if(v.version.major != version.major || v.version.minor < version.minor) {
			continue;
		}
		return v.name;
	};
	
	return NULL;
}

} // anonymous namespace

std::ostream & operator<<(std::ostream & os, const windows_version::data & version) {
	os << version.major << '.' << version.minor;
	if(version.build) {
		os << version.build;
	}
	return os;
}

std::ostream & operator<<(std::ostream & os, const windows_version & version) {
	
	os << version.win_version;
	if(version.nt_version != version.win_version) {
		os << "  nt " << version.nt_version;
	}
	
	const char * win_name = get_version_name(version.win_version);
	const char * nt_name = get_version_name(version.nt_version, true);
	
	if(win_name || nt_name) {
		os << " (";
		if(win_name) {
			os << win_name;
		}
		if(nt_name && nt_name != win_name) {
			if(win_name) {
				os << " / ";
			}
			os << nt_name;
		}
		os << ')';
	}
	
	if(version.nt_service_pack.major || version.nt_service_pack.minor) {
		os << " service pack " << version.nt_service_pack.major;
		if(version.nt_service_pack.minor) {
			os << '.' << version.nt_service_pack.minor;
		}
	}
	
	return os;
}

} // namespace setup
```

## File: `src/setup/windows.hpp`
```
/*
 * Copyright (C) 2011-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Structures for Windows version numbers stored in Inno Setup files.
 */
#ifndef INNOEXTRACT_SETUP_WINDOWS_HPP
#define INNOEXTRACT_SETUP_WINDOWS_HPP

#include <iosfwd>

namespace setup {

struct version;

struct windows_version {
	
	struct data {
		
		unsigned major;
		unsigned minor;
		unsigned build;
		
		bool operator==(const data & o) const {
			return (build == o.build && major == o.major && minor == o.minor);
		}
		
		bool operator!=(const data & o) const {
			return !(*this == o);
		}
		
		void load(std::istream & is, const version & version);
		
	};
	
	data win_version;
	data nt_version;
	
	struct service_pack {
		
		unsigned major;
		unsigned minor;
	
		bool operator==(const service_pack & o) const {
			return (major == o.major && minor == o.minor);
		}
		
		bool operator!=(const service_pack & o) const {
			return !(*this == o);
		}
		
	};
	
	service_pack nt_service_pack;
	
	void load(std::istream & is, const version & version);
	
	bool operator==(const windows_version & o) const {
		return (win_version == o.win_version
		        && nt_version == o.nt_version
		        && nt_service_pack == o.nt_service_pack);
	}
	
	bool operator!=(const windows_version & o) const {
		return !(*this == o);
	}
	
	static const windows_version none;
	
};

struct windows_version_range {
	
	windows_version begin;
	windows_version end;
	
	void load(std::istream & is, const version & version);
	
};

std::ostream & operator<<(std::ostream & os, const windows_version::data & version);
std::ostream & operator<<(std::ostream & os, const windows_version & version);

} // namespace setup

#endif // INNOEXTRACT_SETUP_WINDOWS_HPP
```

## File: `src/stream/block.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "stream/block.hpp"

#include <cstring>
#include <string>
#include <istream>
#include <algorithm>

#include <boost/cstdint.hpp>
#include <boost/iostreams/filtering_stream.hpp>
#include <boost/iostreams/restrict.hpp>
#include <boost/iostreams/filter/zlib.hpp>
#include <boost/iostreams/char_traits.hpp>
#include <boost/iostreams/concepts.hpp>
#include <boost/iostreams/read.hpp>
#include <boost/make_shared.hpp>

#include "release.hpp"
#include "crypto/crc32.hpp"
#include "setup/version.hpp"
#include "stream/lzma.hpp"
#include "util/endian.hpp"
#include "util/enum.hpp"
#include "util/load.hpp"
#include "util/log.hpp"
#include "util/math.hpp"

namespace io = boost::iostreams;

namespace stream {

namespace {

enum block_compression {
	Stored,
	Zlib,
	LZMA1,
};

/*!
 * A filter that reads a block of 4096-byte chunks where each chunk is preceeded by
 * a CRC32 checksum. The last chunk can be shorter than 4096 bytes.
 *
 * If chunk checksum is wrong a block_error is thrown before any data of that
 * chunk is returned.
 *
 * block_error is also thrown if there is trailing data: 0 < (total size % (4096 + 4)) < 5
 */
class inno_block_filter : public boost::iostreams::multichar_input_filter {
	
private:
	
	typedef boost::iostreams::multichar_input_filter base_type;
	
public:
	
	typedef base_type::char_type char_type;
	typedef base_type::category category;
	
	inno_block_filter() : pos(0), length(0) { }
	
	template <typename Source>
	bool read_chunk(Source & src) {
		
		char temp[sizeof(boost::uint32_t)];
		std::streamsize temp_size = std::streamsize(sizeof(temp));
		std::streamsize nread = boost::iostreams::read(src, temp, temp_size);
		if(nread == EOF) {
			return false;
		} else if(size_t(nread) != sizeof(temp)) {
			throw block_error("unexpected block end");
		}
		boost::uint32_t block_crc32 = util::little_endian::load<boost::uint32_t>(temp);
		
		length = size_t(boost::iostreams::read(src, buffer, std::streamsize(sizeof(buffer))));
		if(length == size_t(EOF)) {
			throw block_error("unexpected block end");
		}
		
		crypto::crc32 actual;
		actual.init();
		actual.update(buffer, length);
		if(actual.finalize() != block_crc32) {
			throw block_error("block CRC32 mismatch");
		}
		
		pos = 0;
		
		return true;
	}
	
	template <typename Source>
	std::streamsize read(Source & src, char * dest, std::streamsize n) {
		
		std::streamsize nread = 0;
		while(n) {
			
			if(pos == length && !read_chunk(src)) {
				return nread ? nread : EOF;
			}
			
			std::streamsize size = std::min(n, std::streamsize(length - pos));
			
			std::copy(buffer + pos, buffer + pos + size, dest + nread);
			
			pos += size_t(size), n -= size, nread += size;
		}
		
		return nread;
	}
	
private:
	
	size_t pos; //! Current read position in the buffer.
	size_t length; //! Length of the buffer. This is always 4096 except for the last chunk.
	char buffer[4096];
	
};

} // anonymous namespace

} // namespace stream

NAMED_ENUM(stream::block_compression)

NAMES(stream::block_compression, "Compression",
	"stored",
	"zlib",
	"lzma1",
)

namespace stream {

block_reader::pointer block_reader::get(std::istream & base, const setup::version & version) {
	
	USE_ENUM_NAMES(block_compression)
	
	boost::uint32_t expected_checksum = util::load<boost::uint32_t>(base);
	crypto::crc32 actual_checksum;
	actual_checksum.init();
	
	boost::uint32_t stored_size;
	block_compression compression;
	
	if(version >= INNO_VERSION(4, 0, 9)) {
		
		stored_size = actual_checksum.load<boost::uint32_t>(base);
		boost::uint8_t compressed = actual_checksum.load<boost::uint8_t>(base);
		
		compression = compressed ? (version >= INNO_VERSION(4, 1, 6) ? LZMA1 : Zlib) : Stored;
		
	} else {
		
		boost::uint32_t compressed_size = actual_checksum.load<boost::uint32_t>(base);
		boost::uint32_t uncompressed_size = actual_checksum.load<boost::uint32_t>(base);
		
		if(compressed_size == boost::uint32_t(-1)) {
			stored_size = uncompressed_size, compression = Stored;
		} else {
			stored_size = compressed_size, compression = Zlib;
		}
		
		// Add the size of a CRC32 checksum for each 4KiB subblock.
		stored_size += boost::uint32_t(util::ceildiv<boost::uint64_t>(stored_size, 4096) * 4);
	}
	
	if(actual_checksum.finalize() != expected_checksum) {
		throw block_error("block header CRC32 mismatch");
	}
	
	debug("[block] size: " << stored_size << "  compression: " << compression);
	
	util::unique_ptr<io::filtering_istream>::type fis(new io::filtering_istream);
	
	switch(compression) {
		case Stored: break;
		case Zlib: fis->push(io::zlib_decompressor(), 8192); break;
	#if INNOEXTRACT_HAVE_LZMA
		case LZMA1: fis->push(inno_lzma1_decompressor(), 8192); break;
	#else
		case LZMA1: throw block_error("LZMA decompression not supported by this "
			                  + std::string(innoextract_name) + " build");
	#endif
	}
	
	fis->push(inno_block_filter(), 4096);
	
	fis->push(io::restrict(base, 0, stored_size));
	
	fis->exceptions(std::ios_base::badbit | std::ios_base::failbit);
	
	return pointer(fis.release());
}

} // namespace stream
```

## File: `src/stream/block.hpp`
```
/*
 * Copyright (C) 2011-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Wrapper to read, checksum and decompress header blocks.
 *
 * Thse blocks are used to store the setup headers (\ref setup).
 */
#ifndef INNOEXTRACT_STREAM_BLOCK_HPP
#define INNOEXTRACT_STREAM_BLOCK_HPP

#include <ios>
#include <istream>
#include <string>

#include "util/unique_ptr.hpp"

namespace setup { struct version; }

namespace stream {

//! Error thrown by \ref chunk_reader::get or the returned stream if there was a problem.
struct block_error : public std::ios_base::failure {
	
	explicit block_error(const std::string & msg) : std::ios_base::failure(msg) { }
	
};

/*!
 * Wrapper to read compressed and checksumed block of data used to store setup headers.
 *
 * The decompressed headers are parsed in \ref setup::info, which also uses this class.
 */
class block_reader {
	
public:
	
	typedef std::istream                 type;
	typedef util::unique_ptr<type>::type pointer;
	
	/*!
	 * Wrap an input stream to read and decompress setup header blocks.
	 *
	 * Only one wrapper can be used at the same time for each \c base.
	 *
	 * \param base     The input stream for the main setup files.
	 *                 It must already be positioned at start of the block stream.
	 *                 The first block stream starts directly after the \ref setup::version
	 *                 identifier whose position is given by
	 *                 \ref loader::offsets::header_offset.
	 *                 A second block stream directly follows the first one and contains
	 *                 the \ref setup::data_entry "data entries".
	 * \param version  The version of the setup data.
	 *
	 * \throws block_error if the block stream header checksum was invalid,
	 *                     or if the block compression is not supported by this build.
	 *
	 * \return a pointer to a non-seekable input stream for the uncompressed headers.
	 *         Reading from this stream may throw a \ref block_error if a block checksum
	 *         was invalid.
	 */
	static pointer get(std::istream & base, const setup::version & version);
	
};

} // namespace stream

#endif // INNOEXTRACT_STREAM_BLOCK_HPP
```

## File: `src/stream/checksum.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Filter to be used with boost::iostreams for calculating a \ref crypto::checksum.
 */
#ifndef INNOEXTRACT_STREAM_CHECKSUM_HPP
#define INNOEXTRACT_STREAM_CHECKSUM_HPP

#include <boost/iostreams/concepts.hpp>
#include <boost/iostreams/read.hpp>

#include "crypto/checksum.hpp"
#include "crypto/hasher.hpp"

namespace stream {

/*!
 * Filters to be used with boost::iostreams for calculating a \ref crypto::checksum.
 *
 * An internal checksum state is updated as bytes are read and the final checksum is
 * written to the given checksum object when the end of the source stream is reached.
 */
class checksum_filter : public boost::iostreams::multichar_input_filter {
	
private:
	
	typedef boost::iostreams::multichar_input_filter base_type;
	
public:
	
	typedef base_type::char_type char_type;
	typedef base_type::category category;
	
	/*!
	 * \param dest Location to store the final checksum at.
	 * \param type The type of checksum to calculate.
	 */
	checksum_filter(crypto::checksum * dest, crypto::checksum_type type)
		: hasher(type)
		, output(dest)
	{ }
	
	template <typename Source>
	std::streamsize read(Source & src, char * dest, std::streamsize n) {
		
		std::streamsize nread = boost::iostreams::read(src, dest, n);
		
		if(nread > 0) {
			hasher.update(dest, size_t(nread));
		} else if(output) {
			*output = hasher.finalize();
			output = NULL;
		}
		
		return nread;
	}
	
private:
	
	crypto::hasher hasher;
	
	crypto::checksum * output;
	
};

} // namespace stream

#endif // INNOEXTRACT_STREAM_CHECKSUM_HPP
```

## File: `src/stream/chunk.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "chunk.hpp"

#include <cstring>

#include <boost/iostreams/char_traits.hpp>
#include <boost/iostreams/concepts.hpp>
#include <boost/iostreams/read.hpp>
#include <boost/iostreams/filter/bzip2.hpp>
#include <boost/iostreams/filter/zlib.hpp>
#include <boost/make_shared.hpp>
#include <boost/range/size.hpp>

#include "release.hpp"
#include "crypto/arc4.hpp"
#include "crypto/checksum.hpp"
#include "crypto/hasher.hpp"
#include "crypto/xchacha20.hpp"
#include "stream/lzma.hpp"
#include "stream/restrict.hpp"
#include "stream/slice.hpp"
#include "util/endian.hpp"
#include "util/log.hpp"


namespace io = boost::iostreams;

namespace stream {

namespace {

const char chunk_id[4] = { 'z', 'l', 'b', 0x1a };

#if INNOEXTRACT_HAVE_DECRYPTION

/*!
 * Filter to en-/decrypt files files stored by Inno Setup.
 */
class inno_arc4_crypter : public boost::iostreams::multichar_input_filter {
	
private:
	
	typedef boost::iostreams::multichar_input_filter base_type;
	
public:
	
	typedef base_type::char_type char_type;
	typedef base_type::category category;
	
	inno_arc4_crypter(const char * key, size_t length) {
		
		arc4.init(key, length);
		arc4.discard(1000);
		
	}
	
	template <typename Source>
	std::streamsize read(Source & src, char * dest, std::streamsize n) {
		
		std::streamsize length = boost::iostreams::read(src, dest, n);
		if(length != EOF) {
			arc4.crypt(dest, dest, size_t(n));
		}
		
		return length;
	}
	
private:
	
	crypto::arc4 arc4;
	
	
};
/*!
 * Filter to en-/decrypt files files stored by Inno Setup.
 */
class inno_xchacha20_crypter : public boost::iostreams::multichar_input_filter {
	
private:
	
	typedef boost::iostreams::multichar_input_filter base_type;
	
public:
	
	typedef base_type::char_type char_type;
	typedef base_type::category category;
	
	inno_xchacha20_crypter(const char key[32], const char nonce[24]) {
		
		xchacha20.init(key, nonce);
		
	}
	
	template <typename Source>
	std::streamsize read(Source & src, char * dest, std::streamsize n) {
		
		std::streamsize length = boost::iostreams::read(src, dest, n);
		if(length != EOF) {
			xchacha20.crypt(dest, dest, size_t(n));
		}
		
		return length;
	}
	
private:
	
	crypto::xchacha20 xchacha20;
	
};

#endif // INNOEXTRACT_HAVE_DECRYPTION

} // anonymous namespace

bool chunk::operator<(const chunk & o) const {
	
	if(first_slice != o.first_slice) {
		return (first_slice < o.first_slice);
	} else if(sort_offset != o.sort_offset) {
		return (sort_offset < o.sort_offset);
	} else if(size != o.size) {
		return (size < o.size);
	} else if(compression != o.compression) {
		return (compression < o.compression);
	} else if(encryption != o.encryption) {
		return (encryption < o.encryption);
	}
	
	return false;
}

bool chunk::operator==(const chunk & o) const {
	return (first_slice == o.first_slice
	        && sort_offset == o.sort_offset
	        && size == o.size
	        && compression == o.compression
	        && encryption == o.encryption);
}

chunk_reader::pointer chunk_reader::get(slice_reader & base, const chunk & chunk , const std::string & key) {
	
	if(!base.seek(chunk.first_slice, chunk.offset)) {
		throw chunk_error("could not seek to chunk start");
	}
	
	char magic[sizeof(chunk_id)];
	if(base.read(magic, 4) != 4 || std::memcmp(magic, chunk_id, sizeof(chunk_id)) != 0) {
		throw chunk_error("bad chunk magic");
	}
	
	pointer result(new boost::iostreams::chain<boost::iostreams::input>);
	
	switch(chunk.compression) {
		case Stored: break;
		case Zlib:   result->push(io::zlib_decompressor(), 8192); break;
		case BZip2:  result->push(io::bzip2_decompressor(), 8192); break;
	#if INNOEXTRACT_HAVE_LZMA
		case LZMA1:  result->push(inno_lzma1_decompressor(), 8192); break;
		case LZMA2:  result->push(inno_lzma2_decompressor(), 8192); break;
	#else
		case LZMA1: case LZMA2:
			throw chunk_error("LZMA decompression not supported by this "
			                  + std::string(innoextract_name) + " build");
	#endif
		default: throw chunk_error("unknown chunk compression");
	}
	
	switch(chunk.encryption) {
		case Plaintext: break;
		#if INNOEXTRACT_HAVE_DECRYPTION
		case ARC4_MD5: /* fall-through */
		case ARC4_SHA1: {
			char salt[8];
			if(base.read(salt, 8) != 8) {
				throw chunk_error("could not read chunk salt");
			}
			crypto::hasher hasher(chunk.encryption == ARC4_SHA1 ? crypto::SHA1 : crypto::MD5);
			hasher.update(salt, sizeof(salt));
			hasher.update(key.c_str(), key.length());
			crypto::checksum checksum = hasher.finalize();
			const char * salted_key = chunk.encryption == ARC4_SHA1 ? checksum.sha1 : checksum.md5;
			size_t key_length = chunk.encryption == ARC4_SHA1 ? sizeof(checksum.sha1) : sizeof(checksum.md5);
			result->push(inno_arc4_crypter(salted_key, key_length), 8192);
			break;
		}
		case XChaCha20: {
			if(key.length() != crypto::xchacha20::key_size + crypto::xchacha20::nonce_size) {
				throw chunk_error("unexpected key size");
			}
			char nonce[crypto::xchacha20::nonce_size];
			std::memcpy(nonce, key.c_str() + crypto::xchacha20::key_size, crypto::xchacha20::nonce_size);
			util::little_endian::store(util::little_endian::load<boost::uint64_t>(nonce) ^ chunk.offset, nonce);
			util::little_endian::store(util::little_endian::load<boost::uint32_t>(nonce + 8) ^ chunk.first_slice, nonce + 8);
			result->push(inno_xchacha20_crypter(key.c_str(), nonce), 8192);
			break;
		}
		#else
		default: (void)key, throw chunk_error("XChaCha20 decryption not supported in this build");
		#endif
	}
	
	result->push(restrict(base, chunk.size));
	
	return result;
}

} // namespace stream

NAMES(stream::compression_method, "Compression Method",
	"stored",
	"zlib",
	"bzip2",
	"lzma1",
	"lzma2",
	"unknown",
)

NAMES(stream::encryption_method, "Encryption Method",
	"plaintext",
	"rc4 + md5",
	"rc4 + sha1",
	"xchacha20",
)
```

## File: `src/stream/chunk.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Wrapper to read and decompress a chunk from a \ref stream::slice_reader.
 *
 * A chunk consists of one compression stream (one of \ref stream::compression_method) and
 * contains one or more \ref stream::file "files".
 * Files may also have additional filters managed by \ref stream::file_reader.
 */
#ifndef INNOEXTRACT_STREAM_CHUNK_HPP
#define INNOEXTRACT_STREAM_CHUNK_HPP

#include <stddef.h>
#include <ios>
#include <string>

#include <boost/cstdint.hpp>
#include <boost/iostreams/chain.hpp>

#include "util/enum.hpp"
#include "util/unique_ptr.hpp"

namespace stream {

class slice_reader;

//! Error thrown by \ref chunk_reader::get if there was a problem.
struct chunk_error : public std::ios_base::failure {
	
	explicit chunk_error(const std::string & msg) : std::ios_base::failure(msg) { }
	
};

//! Compression methods supported by chunks.
enum compression_method {
	Stored,
	Zlib,
	BZip2,
	LZMA1,
	LZMA2,
	UnknownCompression
};

//! Encryption methods supported by chunks.
enum encryption_method {
	Plaintext,
	ARC4_MD5,
	ARC4_SHA1,
	XChaCha20,
};

/*!
 * Information specifying a compressed chunk.
 *
 * This data is stored in \ref setup::data_entry "data entries".
 *
 * Chunks specified by this struct can be read using \ref chunk_reader.
 */
struct chunk {
	
	boost::uint32_t first_slice;    //!< Slice where the chunk starts.
	boost::uint32_t last_slice;     //!< Slice where the chunk ends.
	
	boost::uint32_t sort_offset;
	
	boost::uint32_t offset;         //!< Offset of the compressed chunk in firstSlice.
	boost::uint64_t size;           //! Total compressed size of the chunk.
	
	compression_method compression; //!< Compression method used by the chunk.
	encryption_method encryption;   //!< Encryption method used by the chunk.
	
	bool operator<(const chunk & o) const;
	bool operator==(const chunk & o) const;
	
};

class silce_source;

/*!
 * Wrapper to read and decompress a chunk from a \ref slice_reader.
 * Restrics the stream to the chunk size and applies the appropriate decompression.
 */
class chunk_reader {
	
public:
	
	typedef boost::iostreams::chain<boost::iostreams::input> type;
	typedef util::unique_ptr<type>::type                     pointer;
	
	/*!
	 * Wrap a \ref slice_reader to read and decompress a single chunk.
	 *
	 * Only one wrapper can be used at the same time for each \c base.
	 *
	 * \param base  The slice reader for the setup file(s).
	 * \param chunk Information specifying the chunk to read.
	 * \param key   Key used for encrypted chunks.
	 *
	 * \throws chunk_error if the chunk header could not be read or was invalid,
	 *                     or if the chunk compression is not supported by this build.
	 *
	 * \return a pointer to a non-seekable input filter chain for the requested file.
	 */
	static pointer get(slice_reader & base, const ::stream::chunk & chunk, const std::string & key);
	
};

} // namespace stream

NAMED_ENUM(stream::compression_method)

NAMED_ENUM(stream::encryption_method)

#endif // INNOEXTRACT_STREAM_CHUNK_HPP
```

## File: `src/stream/exefilter.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Filters to be used with boost::iostreams for undoing transformations Inno Setup applies
 * to stored executable files to make them more compressible.
 */
#ifndef INNOEXTRACT_STREAM_EXEFILTER_HPP
#define INNOEXTRACT_STREAM_EXEFILTER_HPP

#include <stddef.h>
#include <iosfwd>
#include <cassert>

#include <boost/cstdint.hpp>
#include <boost/iostreams/char_traits.hpp>
#include <boost/iostreams/concepts.hpp>
#include <boost/iostreams/get.hpp>
#include <boost/iostreams/read.hpp>

namespace stream {

/*!
 * Filter to decode executable files stored by Inno Setup versions before 5.2.0.
 *
 * Essentially, it tries to change the addresses stored for x86 CALL and JMP instructions
 * to be relative to the instruction's position.
 */
class inno_exe_decoder_4108 : public boost::iostreams::multichar_input_filter {
	
private:
	
	typedef boost::iostreams::multichar_input_filter base_type;
	
public:
	
	typedef base_type::char_type char_type;
	typedef base_type::category category;
	
	inno_exe_decoder_4108() { close(0); }
	
	template <typename Source>
	std::streamsize read(Source & src, char * dest, std::streamsize n);
	
	
	template <typename Source>
	void close(const Source & /* source */) {
		addr = 0, addr_bytes_left = 0, addr_offset = 5;
	}
	
private:
	
	boost::uint32_t addr;
	size_t addr_bytes_left;
	boost::uint32_t addr_offset;
	
};

/*!
 * Filter to decode executable files stored by Inno Setup versions after 5.2.0.
 *
 * It tries to change the addresses stored for x86 CALL and JMP instructions to be
 * relative to the instruction's position, plus a few other tweaks.
 */
class inno_exe_decoder_5200 : public boost::iostreams::multichar_input_filter {
	
private:
	
	typedef boost::iostreams::multichar_input_filter base_type;
	
public:
	
	typedef base_type::char_type char_type;
	typedef base_type::category category;
	
	/*!
	 * \param flip_high_bytes true if the high byte of addresses is flipped if bit 23 is set.
	 *                        This optimization is used in Inno Setup 5.3.9 and later.
	 */
	explicit inno_exe_decoder_5200(bool flip_high_bytes)
		: flip_high_byte(flip_high_bytes) { close(0); }
	
	template <typename Source>
	std::streamsize read(Source & src, char * dest, std::streamsize n);
	
	template <typename Source>
	void close(const Source & /* source */) {
		offset = 0, flush_bytes = 0;
	}
	
private:
	
	/*
	 * call_instruction_decoder_5200 has three states:
	 *
	 * "initial" (flush_bytes == 0)
	 *  - Read individual bytes and write them directly to output.
	 *  - If the byte could be the start of a CALL or JMP instruction that doesn't span blocks,
	 *    set addr_bytes_left to -4.
	 *
	 * "address" (flush_bytes < 0 && flush_bytes >= -4)
	 *  - Read all four address bytes into buffer, incrementing flush_bytes for each byte read.
	 *  - Once the last byte has been read, transform the address and set flush_bytes to 4.
	 *  - If an EOF is encountered before all four bytes have been read, set flush_bytes to
	 *    4 + flush_bytes.
	 *
	 * "flush" (flush_bytes > 0 && flush_bytes <= 4)
	 *  - Write the first flush_bytes bytes of buffer to output.
	 *  - If there is not enough output space, write as much as possible and move to rest to
	 *    the start of buffer.
	 */
	
	static const size_t block_size = 0x10000;
	const bool flip_high_byte;
	
	boost::uint32_t offset; //! Total number of bytes read from the source.
	
	boost::int8_t flush_bytes;
	boost::uint8_t buffer[4];
	
};

// Implementation:

template <typename Source>
std::streamsize inno_exe_decoder_4108::read(Source & src, char * dest, std::streamsize n) {
	
	for(std::streamsize i = 0; i < n; i++, addr_offset++) {
		
		int byte = boost::iostreams::get(src);
		if(byte == EOF) { return i ? i : EOF; }
		if(byte == boost::iostreams::WOULD_BLOCK) { return i; }
		
		if(addr_bytes_left == 0) {
			
			// Check if this is a CALL or JMP instruction.
			if(byte == 0xe8 || byte == 0xe9) {
				addr = ~addr_offset + 1;
				addr_bytes_left = 4;
			}
			
		} else {
			addr += boost::uint8_t(byte);
			byte = boost::uint8_t(addr);
			addr >>= 8;
			addr_bytes_left--;
		}
		
		*dest++ = char(boost::uint8_t(byte));
	}
	
	return n;
}

template <typename Source>
std::streamsize inno_exe_decoder_5200::read(Source & src, char * dest, std::streamsize n) {
	
	char * end = dest + n;
	
	//! Total number of filtered bytes read and written to dest.
#define total_read     (n - (end - dest))
	
#define flush(N) \
	{ \
		if((N) > 0) { \
			flush_bytes = (N); \
			size_t buffer_i = 0; \
			do { \
				if(dest == end) { \
					memmove(buffer, buffer + buffer_i, size_t(flush_bytes)); \
					return total_read; \
				} \
				*dest++ = char(buffer[buffer_i++]); \
			} while(--flush_bytes); \
		} \
	} (void)0
	
	
	// Flush already processed address bytes.
	flush(flush_bytes);
	
	while(dest != end) {
		
		if(!flush_bytes) {
			
			// Check if this is a CALL or JMP instruction.
			int byte = boost::iostreams::get(src);
			if(byte == EOF) { return total_read ? total_read : EOF; }
			if(byte == boost::iostreams::WOULD_BLOCK) { return total_read; }
			*dest++ = char(byte);
			offset++;
			if(byte != 0xe8 && byte != 0xe9) {
				// Not a CALL or JMP instruction.
				continue;
			}
			
			const size_t block_size_left = block_size - ((offset - 1) % block_size);
			if(block_size_left < 5) {
				// Ignore instructions that span blocks.
				continue;
			}
			
			flush_bytes = -4;
		}
		
		assert(flush_bytes < 0);
		
		// Read all four address bytes.
		char * dst = reinterpret_cast<char *>(buffer + 4 + flush_bytes);
		std::streamsize nread = boost::iostreams::read(src, dst, -flush_bytes);
		if(nread == EOF) {
			flush(boost::int8_t(4 + flush_bytes));
			return total_read ? total_read : EOF;
		}
		flush_bytes = boost::int8_t(flush_bytes + nread), offset += boost::uint32_t(nread);
		if(flush_bytes) { return total_read; }
		
		// Verify that the high byte of the address is 0x00 or 00xff.
		if(buffer[3] == 0x00 || buffer[3] == 0xff) {
			
			boost::uint32_t addr = offset & 0xffffff; // may wrap, but OK
			
			boost::uint32_t rel = buffer[0] | (boost::uint32_t(buffer[1]) << 8)
			                                | (boost::uint32_t(buffer[2]) << 16);
			rel -= addr;
			buffer[0] = boost::uint8_t(rel);
			buffer[1] = boost::uint8_t(rel >> 8);
			buffer[2] = boost::uint8_t(rel >> 16);
			
			if(flip_high_byte) {
				// For a slightly higher compression ratio, we want the resulting high
				// byte to be 0x00 for both forward and backward jumps. The high byte
				// of the original relative address is likely to be the sign extension
				// of bit 23, so if bit 23 is set, toggle all bits in the high byte.
				if(rel & 0x800000) {
					buffer[3] = boost::uint8_t(~buffer[3]);
				}
			}
			
		} else {
			// This is most likely not a CALL or JUMP.
		}
		
		flush(4);
	}
	
	return total_read;
	
#undef flush
#undef total_read
	
}

} // namespace stream

#endif // INNOEXTRACT_STREAM_EXEFILTER_HPP
```

## File: `src/stream/file.cpp`
```cpp
/*
 * Copyright (C) 2011-2018 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "stream/file.hpp"

#include <boost/iostreams/filtering_stream.hpp>
#include <boost/iostreams/filter/zlib.hpp>

#include "stream/checksum.hpp"
#include "stream/exefilter.hpp"
#include "stream/restrict.hpp"

namespace io = boost::iostreams;

namespace stream {

bool file::operator<(const stream::file & o) const {
	
	if(offset != o.offset) {
		return (offset < o.offset);
	} else if(size != o.size) {
		return (size < o.size);
	} else if(filter != o.filter) {
		return (filter < o.filter);
	}
	
	return false;
}

bool file::operator==(const file & o) const {
	return (offset == o.offset
	        && size == o.size
	        && filter == o.filter);
}


file_reader::pointer file_reader::get(base_type & base, const file & file,
                                      crypto::checksum * checksum) {
	
	util::unique_ptr<io::filtering_istream>::type result(new io::filtering_istream);
	
	if(file.filter == ZlibFilter) {
		result->push(io::zlib_decompressor(), 8192);
	}
	
	if(checksum) {
		result->push(stream::checksum_filter(checksum, file.checksum.type), 8192);
	}
	
	switch(file.filter) {
		case NoFilter: break;
		case InstructionFilter4108: result->push(stream::inno_exe_decoder_4108(), 8192); break;
		case InstructionFilter5200: result->push(stream::inno_exe_decoder_5200(false), 8192); break;
		case InstructionFilter5309: result->push(stream::inno_exe_decoder_5200(true), 8192); break;
		case ZlibFilter: /* applied *after* calculating the checksum */ break;
	}
	
	result->push(stream::restrict(base, file.size));
	
	result->exceptions(std::ios_base::badbit);
	
	return pointer(result.release());
}

} // namespace stream
```

## File: `src/stream/file.hpp`
```
/*
 * Copyright (C) 2011-2018 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Wrapper to read a single file from a chunk (\ref stream::chunk_reader).
 */
#ifndef INNOEXTRACT_STREAM_FILE_HPP
#define INNOEXTRACT_STREAM_FILE_HPP

#include <istream>

#include <boost/iostreams/chain.hpp>

#include "crypto/checksum.hpp"
#include "util/unique_ptr.hpp"

namespace stream {

enum compression_filter {
	NoFilter,
	InstructionFilter4108,
	InstructionFilter5200,
	InstructionFilter5309,
	ZlibFilter,
};

/*!
 * Information specifying a single file inside a compressed chunk.
 *
 * This data is stored in \ref setup::data_entry "data entries".
 *
 * Files specified by this struct can be read using \ref file_reader.
 */
struct file {
	
	boost::uint64_t    offset;   //!< Offset of this file within the decompressed chunk.
	boost::uint64_t    size;     //!< Pre-filter size of this file in the decompressed chunk.
	
	crypto::checksum   checksum; //!< Checksum for the file.
	
	compression_filter filter;   //!< Additional filter used before compression.
	
	bool operator<(const file & o) const;
	bool operator==(const file & o) const;
	
};

/*!
 * Wrapper to read a single file from a \ref chunk_reader.
 * Restrics the stream to the file size and applies the appropriate filters.
 */
class file_reader {
	
	typedef boost::iostreams::chain<boost::iostreams::input> base_type;
	
public:
	
	typedef std::istream                 type;
	typedef util::unique_ptr<type>::type pointer;
	typedef file                         file_t;
	
	/*!
	 * Wrap a \ref chunk_reader to read a single file.
	 *
	 * Only one wrapper can be used at the same time for each \c base.
	 *
	 * \param base     The chunk reader containing the file.
	 *                 It must already be positioned at the file's offset.
	 * \param file     Information specifying the file to read.
	 * \param checksum Optional pointer to a checksum that is updated as the file is read.
	 *                 The type of the checksum will be the same as that stored in the file
	 *                 struct.
	 *
	 * \return a pointer to a non-seekable input stream for the requested file.
	 */
	static pointer get(base_type & base, const file_t & file, crypto::checksum * checksum);
	
};

} // namespace stream

#endif // INNOEXTRACT_STREAM_FILE_HPP
```

## File: `src/stream/lzma.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "stream/lzma.hpp"

#include <boost/cstdint.hpp>

#include <lzma.h>

#include "util/endian.hpp"
#include "util/load.hpp"

namespace stream {

static lzma_stream * init_raw_lzma_stream(lzma_vli filter, lzma_options_lzma & options) {
	
	options.preset_dict = NULL;
	
	lzma_stream * strm = new lzma_stream;
	lzma_stream tmp = LZMA_STREAM_INIT;
	*strm = tmp;
	strm->allocator = NULL;
	
	const lzma_filter filters[2] = { { filter,  &options }, { LZMA_VLI_UNKNOWN, NULL } };
	lzma_ret ret = lzma_raw_decoder(strm, filters);
	if(ret != LZMA_OK) {
		delete strm;
		throw lzma_error("inno lzma init error", ret);
	}
	
	return strm;
}

bool lzma_decompressor_impl_base::filter(const char * & begin_in, const char * end_in,
                                         char * & begin_out, char * end_out, bool flush) {
	
	lzma_stream * strm = static_cast<lzma_stream *>(stream);
	
	strm->next_in = reinterpret_cast<const boost::uint8_t *>(begin_in);
	strm->avail_in = size_t(end_in - begin_in);
	
	strm->next_out = reinterpret_cast<boost::uint8_t *>(begin_out);
	strm->avail_out = size_t(end_out - begin_out);
	
	lzma_ret ret = lzma_code(strm, LZMA_RUN);
	
	if(flush && ret == LZMA_BUF_ERROR && strm->avail_out > 0) {
		throw lzma_error("truncated lzma stream", ret);
	}
	
	begin_in = reinterpret_cast<const char *>(strm->next_in);
	begin_out = reinterpret_cast<char *>(strm->next_out);
	
	if(ret != LZMA_OK && ret != LZMA_STREAM_END && ret != LZMA_BUF_ERROR) {
		throw lzma_error("lzma decrompression error", ret);
	}
	
	return (ret != LZMA_STREAM_END);
}

void lzma_decompressor_impl_base::close() {
	
	if(stream) {
		lzma_stream * strm = static_cast<lzma_stream *>(stream);
		lzma_end(strm);
		delete strm, stream = NULL;
	}
}

bool inno_lzma1_decompressor_impl::filter(const char * & begin_in, const char * end_in,
                                          char * & begin_out, char * end_out, bool flush) {
	
	// Decode the header.
	if(!stream) {
		
		// Read enough bytes to decode the header.
		while(nread != 5) {
			if(begin_in == end_in) {
				return true;
			}
			header[nread++] = *begin_in++;
		}
		
		lzma_options_lzma options;
		
		boost::uint8_t properties = boost::uint8_t(header[0]);
		if(properties > (9 * 5 * 5)) {
			throw lzma_error("inno lzma1 property error", LZMA_FORMAT_ERROR);
		}
		options.pb = boost::uint32_t(properties / (9 * 5));
		options.lp = boost::uint32_t((properties % (9 * 5)) / 9);
		options.lc = boost::uint32_t(properties % 9);
		
		options.dict_size = util::little_endian::load<boost::uint32_t>(header + 1);
		
		stream = init_raw_lzma_stream(LZMA_FILTER_LZMA1, options);
	}
	
	return lzma_decompressor_impl_base::filter(begin_in, end_in, begin_out, end_out, flush);
}

bool inno_lzma2_decompressor_impl::filter(const char * & begin_in, const char * end_in,
                                          char * & begin_out, char * end_out, bool flush) {
	
	// Decode the header.
	if(!stream) {
		
		if(begin_in == end_in) {
			return true;
		}
		
		lzma_options_lzma options;
		
		boost::uint8_t prop = boost::uint8_t(*begin_in++);
		if(prop > 40) {
			throw lzma_error("inno lzma2 property error", LZMA_FORMAT_ERROR);
		}
		
		if(prop == 40) {
			options.dict_size = 0xffffffff;
		} else {
			options.dict_size = ((boost::uint32_t(2) | boost::uint32_t((prop) & 1)) << ((prop) / 2 + 11));
		}
		
		stream = init_raw_lzma_stream(LZMA_FILTER_LZMA2, options);
	}
	
	return lzma_decompressor_impl_base::filter(begin_in, end_in, begin_out, end_out, flush);
}

} // namespace stream
```

## File: `src/stream/lzma.hpp`
```
/*
 * Copyright (C) 2011-2018 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * LZMA 1 and 2 (aka xz) descompression filters to be used with boost::iostreams.
 */
#ifndef INNOEXTRACT_STREAM_LZMA_HPP
#define INNOEXTRACT_STREAM_LZMA_HPP

#include "configure.hpp"

#if INNOEXTRACT_HAVE_LZMA

#include <stddef.h>
#include <iosfwd>

#include <boost/iostreams/filter/symmetric.hpp>
#include <boost/noncopyable.hpp>

namespace stream {

//! Error thrown if there was en error in an LZMA stream
struct lzma_error : public std::ios_base::failure {
	
	lzma_error(const std::string & msg, int code)
		: std::ios_base::failure(msg), error_code(code) { }
	
	//! \return the liblzma code for the error.
	int error() const { return error_code; }
	
private:
	
	int error_code;
};

class lzma_decompressor_impl_base : private boost::noncopyable {
	
public:
	
	typedef char char_type;
	
	~lzma_decompressor_impl_base() { close(); }
	
	bool filter(const char * & begin_in, const char * end_in,
	            char * & begin_out, char * end_out, bool flush);
	
	void close();
	
protected:
	
	//! Abstract base class, subclasses need to intialize stream.
	lzma_decompressor_impl_base() : stream(NULL) { }
	
	void * stream;
	
};

class inno_lzma1_decompressor_impl : public lzma_decompressor_impl_base {
	
public:
	
	inno_lzma1_decompressor_impl() : nread(0) { }
	
	bool filter(const char * & begin_in, const char * end_in,
	            char * & begin_out, char * end_out, bool flush);
	
	void close() { lzma_decompressor_impl_base::close(), nread = 0; }
	
private:
	
	size_t nread; //! Number of bytes read into header.
	char header[5];
	
};

class inno_lzma2_decompressor_impl : public lzma_decompressor_impl_base {
	
public:
	
	bool filter(const char * & begin_in, const char * end_in,
	            char * & begin_out, char * end_out, bool flush);
	
};

template <class Impl, class Allocator = std::allocator<typename Impl::char_type> >
class lzma_decompressor : public boost::iostreams::symmetric_filter<Impl, Allocator> {
	
public:
	
	explicit lzma_decompressor(int buffer_size = boost::iostreams::default_device_buffer_size)
		: boost::iostreams::symmetric_filter<Impl, Allocator>(buffer_size) { }
	
};

/*!
 * A filter that decompressess LZMA1 streams found in Inno Setup installers,
 * to be used with boost::iostreams.
 *
 * The LZMA1 streams used by Inno Setup differ slightly from the LZMA Alone file format:
 * The stream header only stores the properties (lc, lp, pb) and the dictionary size and
 * is missing the uncompressed size field. The fiels that are present are encoded
 * identically.
 */
typedef lzma_decompressor<inno_lzma1_decompressor_impl> inno_lzma1_decompressor;

/*!
 * A filter that decompressess LZMA2 streams found in Inno Setup installers,
 * to be used with boost::iostreams.
 *
 * Inno Setup uses raw LZMA2 streams.
 * (preceded only by the dictionary size encoded as one byte)
 */
typedef lzma_decompressor<inno_lzma2_decompressor_impl> inno_lzma2_decompressor;

} // namespace stream

#endif // INNOEXTRACT_HAVE_LZMA

#endif // INNOEXTRACT_STREAM_LZMA_HPP
```

## File: `src/stream/restrict.hpp`
```
/*
 * Copyright (C) 2013-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Wrapper class for a boost::iostreams-compatible source that can be used to restrict
 * sources to appear smaller than they really are.
 */
#ifndef INNOEXTRACT_STREAM_RESTRICT_HPP
#define INNOEXTRACT_STREAM_RESTRICT_HPP

#include <boost/cstdint.hpp>
#include <boost/iostreams/concepts.hpp>
#include <boost/iostreams/read.hpp>

namespace stream {

//! Like boost::iostreams::restriction, but always has a 64-bit counter.
template <typename BaseSource>
class restricted_source : public boost::iostreams::source {
	
	BaseSource &    base;      //!< The base source to read from.
	boost::uint64_t remaining; //!< Number of bytes remaining in the restricted source.
	
public:
	
	restricted_source(const restricted_source & o)
		: base(o.base), remaining(o.remaining) { }
	
	restricted_source(BaseSource & source, boost::uint64_t size)
		: base(source), remaining(size) { }
	
	std::streamsize read(char * buffer, std::streamsize bytes) {
		
		if(bytes <= 0) {
			return 0;
		}
		
		// Restrict the number of bytes to read
		bytes = std::streamsize(std::min(boost::uint64_t(bytes), remaining));
		if(bytes == 0) {
			return -1; // End of the restricted source reached
		}
		
		std::streamsize nread = boost::iostreams::read(base, buffer, bytes);
		
		// Remember how many bytes were read so far
		if(nread > 0) {
			remaining -= std::min(boost::uint64_t(nread), remaining);
		}
		
		return nread;
	}
	
};

/*!
 * Restricts a source to a specific size from the current position and makes
 * it non-seekable.
 *
 * Like boost::iostreams::restrict, but always has a 64-bit counter.
 */
template <typename BaseSource>
restricted_source<BaseSource> restrict(BaseSource & source, boost::uint64_t size) {
	return restricted_source<BaseSource>(source, size);
}

} // namespace stream

#endif // INNOEXTRACT_STREAM_RESTRICT_HPP
```

## File: `src/stream/slice.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "stream/slice.hpp"

#include <sstream>
#include <cstring>
#include <limits>


#include <boost/cstdint.hpp>
#include <boost/algorithm/string/predicate.hpp>
#include <boost/filesystem/operations.hpp>
#include <boost/range/size.hpp>

#include <boost/version.hpp>
#if BOOST_VERSION >= 107200
#include <boost/filesystem/directory.hpp>
#endif

#include "util/console.hpp"
#include "util/load.hpp"
#include "util/log.hpp"

namespace stream {

namespace {

const char slice_ids[][8] = {
	{ 'i', 'd', 's', 'k', 'a', '1', '6', 0x1a },
	{ 'i', 'd', 's', 'k', 'a', '3', '2', 0x1a },
};

} // anonymous namespace

slice_reader::slice_reader(std::istream * istream, boost::uint32_t offset)
	: data_offset(offset),
	  slices_per_disk(1), current_slice(0), slice_size(0),
	  is(istream) {
	
	std::streampos max_size = std::streampos(std::numeric_limits<boost::int32_t>::max());
	
	std::streampos file_size = is->seekg(0, std::ios_base::end).tellg();
	
	slice_size = boost::uint32_t(std::min(file_size, max_size));
	if(is->seekg(data_offset).fail()) {
		throw slice_error("could not seek to data");
	}
}

slice_reader::slice_reader(const path_type & dirname, const std::string & basename,
                           const std::string & basename2, size_t disk_slice_count)
	: data_offset(0),
	  dir(dirname), base_file(basename), base_file2(basename2),
	  slices_per_disk(disk_slice_count), current_slice(0), slice_size(0),
	  is(&ifs) { }

void slice_reader::seek(size_t slice) {
	
	if(slice == current_slice && is_open()) {
		return;
	}
	
	if(data_offset != 0) {
		throw slice_error("cannot change slices in single-file setup");
	}
	
	open(slice);
}

bool slice_reader::open_file(const path_type & file) {
	
	if(!boost::filesystem::exists(file)) {
		return false;
	}
	
	log_info << "Opening \"" << color::cyan << file.string() << color::reset << '"';
	
	ifs.close();
	ifs.clear();
	
	ifs.open(file, std::ios_base::in | std::ios_base::binary | std::ios_base::ate);
	if(ifs.fail()) {
		return false;
	}
	
	std::streampos file_size = ifs.tellg();
	ifs.seekg(0);
	
	char magic[8];
	if(ifs.read(magic, 8).fail()) {
		ifs.close();
		throw slice_error("could not read slice magic number in \"" + file.string() + "\"");
	}
	bool found = false;
	for(size_t i = 0; boost::size(slice_ids); i++) {
		if(!std::memcmp(magic, slice_ids[i], 8)) {
			found = true;
			break;
		}
	}
	if(!found) {
		ifs.close();
		throw slice_error("bad slice magic number in \"" + file.string() + "\"");
	}
	
	slice_size = util::load<boost::uint32_t>(ifs);
	if(ifs.fail()) {
		ifs.close();
		throw slice_error("could not read slice size in \"" + file.string() + "\"");
	} else if(std::streampos(slice_size) > file_size) {
		ifs.close();
		std::ostringstream oss;
		oss << "bad slice size in " << file << ": " << slice_size << " > " << file_size;
		throw slice_error(oss.str());
	} else if(std::streampos(slice_size) < ifs.tellg()) {
		ifs.close();
		std::ostringstream oss;
		oss << "bad slice size in " << file << ": " << slice_size << " < " << ifs.tellg();
		throw slice_error(oss.str());
	}
	
	return true;
}

std::string slice_reader::slice_filename(const std::string & basename, size_t slice,
                                         size_t slices_per_disk) {
	
	std::ostringstream oss;
	oss << basename << '-';
	
	if(slices_per_disk == 0) {
		throw slice_error("slices per disk must not be zero");
	}
	
	if(slices_per_disk == 1) {
		oss << (slice + 1);
	} else {
		size_t major = (slice / slices_per_disk) + 1;
		size_t minor = slice % slices_per_disk;
		oss << major << char(boost::uint8_t('a') + minor);
	}
	
	oss << ".bin";
	
	return oss.str();
}

bool slice_reader::open_file_case_insensitive(const path_type & dirname, const path_type & filename) {
	
	boost::filesystem::directory_iterator end;
	for(boost::filesystem::directory_iterator i(dirname); i != end; ++i) {
		path_type actual_filename = i->path().filename();
		if(boost::iequals(actual_filename.string(), filename.string()) && open_file(dirname / actual_filename)) {
			return true;
		}
	}
	
	return false;
}

void slice_reader::open(size_t slice) {
	
	current_slice = slice;
	is = &ifs;
	ifs.close();
	
	path_type slice_file = slice_filename(base_file, slice, slices_per_disk);
	if(open_file(dir / slice_file)) {
		return;
	}
	
	path_type slice_file2 = slice_filename(base_file2, slice, slices_per_disk);
	if(!base_file2.empty() && slice_file2 != slice_file && open_file(dir / slice_file2)) {
		return;
	}
	
	if(open_file_case_insensitive(dir, slice_file)) {
		return;
	}
	
	if(!base_file2.empty() && slice_file2 != slice_file && open_file_case_insensitive(dir, slice_file2)) {
		return;
	}
	
	std::ostringstream oss;
	oss << "could not open slice " << slice << ": " << slice_file;
	if(!base_file2.empty() && slice_file2 != slice_file) {
		oss << " or " << slice_file2;
	}
	throw slice_error(oss.str());
}

bool slice_reader::seek(size_t slice, boost::uint32_t offset) {
	
	seek(slice);
	
	offset += data_offset;
	
	if(offset > slice_size) {
		return false;
	}
	
	if(is->seekg(offset).fail()) {
		return false;
	}
	
	return true;
}

std::streamsize slice_reader::read(char * buffer, std::streamsize bytes) {
	
	seek(current_slice);
	
	std::streamsize nread = 0;
	
	while(bytes > 0) {
		
		boost::uint32_t read_pos = boost::uint32_t(is->tellg());
		if(read_pos > slice_size) {
			break;
		}
		boost::uint32_t remaining = slice_size - read_pos;
		if(!remaining) {
			seek(current_slice + 1);
			read_pos = boost::uint32_t(is->tellg());
			if(read_pos > slice_size) {
				break;
			}
			remaining = slice_size - read_pos;
		}
		
		boost::uint64_t toread = std::min(boost::uint64_t(remaining), boost::uint64_t(bytes));
		toread = std::min(toread, boost::uint64_t(std::numeric_limits<std::streamsize>::max()));
		if(is->read(buffer, std::streamsize(toread)).fail()) {
			break;
		}
		
		std::streamsize read = is->gcount();
		nread += read, buffer += read, bytes -= read;
	}
	
	return (nread != 0 || bytes == 0) ? nread : -1;
}

} // namespace stream
```

## File: `src/stream/slice.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Abstraction for reading the embedded or external raw setup data.
 */
#ifndef INNOEXTRACT_STREAM_SLICE_HPP
#define INNOEXTRACT_STREAM_SLICE_HPP

#include <ios>
#include <string>

#include <boost/iostreams/concepts.hpp>
#include <boost/filesystem/path.hpp>

#include "util/fstream.hpp"

namespace stream {

//! Error thrown by \ref slice_reader if there was a problem.
struct slice_error : public std::ios_base::failure {
	
	explicit slice_error(const std::string & msg) : std::ios_base::failure(msg) { }
	
};

/*!
 * Abstraction for reading either data embedded inside the setup executable or from
 * multiple external slices.
 *
 * Setup data contained in the executable is located by a non-zeore
 * \ref loader::offsets::data_offset.
 *
 * The contained data is made up of one or more \ref chunk "chunks"
 * (read by \ref chunk_reader), which in turn contain one or more  \ref file "files"
 * (read by \ref file_reader).
 */
class slice_reader : public boost::iostreams::source {
	
	typedef boost::filesystem::path path_type;
	
	// Information for reading embedded setup data
	const boost::uint32_t data_offset;
	
	// Information for eading external setup data
	path_type    dir;             //!< Slice directory specified at construction.
	std::string  base_file;       //!< Base file name for slices.
	std::string  base_file2;      //!< Fallback base filename for slices.
	const size_t slices_per_disk; //!< Number of slices grouped into each disk (for names).
	
	// Information about the current slice
	size_t          current_slice; //!< Number of the currently opened slice.
	boost::uint32_t slice_size;    //!< Size in bytes of the currently opened slice.
	
	// Streams
	util::ifstream ifs; //!< File input stream used when reading from external slices.
	std::istream * is;  //!< Input stream to read from.
	
	void seek(size_t slice);
	bool open_file(const path_type & file);
	bool open_file_case_insensitive(const path_type & dirname, const path_type & filename);
	void open(size_t slice);
	
public:
	
	static std::string slice_filename(const std::string & basename, size_t slice,
	                                  size_t slices_per_disk = 1);
	
	/*!
	 * Construct a \ref slice_reader to read from data inside the setup file.
	 * Seeking to anything except the zeroeth slice is not allowed.
	 *
	 * \param istream A seekable input stream for the setup executable.
	 *                The initial read position of the stream is ignored.
	 * \param offset  The offset within the given stream where the setup data starts.
	 *                This offset is given by \ref loader::offsets::data_offset.
	 *
	 * The constructed reader will allow reading the byte range [data_offset, file end)
	 * from the setup executable and provide this as the range [0, file end - data_offset).
	 */
	slice_reader(std::istream * istream, boost::uint32_t offset);
	
	/*!
	 * Construct a \ref slice_reader to read from external data slices (aka disks).
	 *
	 * Slice files must be located at \c $dir/$base_file-$disk.bin
	 * or \c $dir/$base_file-$disk$sliceletter.bin if \c slices_per_disk is greater
	 * than \c 1.
	 *
	 * The disk number is given by \code slice / slices_per_disk + 1 \endcode while
	 * the sliceletter is the ASCII char \code 'a' + (slice % slices_per_disk) \endcode.
	 *
	 * \param dirname          The directory containing the slice files.
	 * \param basename         The base name for slice files.
	 * \param basename2        Alternative base name for slice files.
	 * \param disk_slice_count How many slices are grouped into one disk. Must not be \c 0.
	 */
	slice_reader(const path_type & dirname, const std::string & basename, const std::string & basename2,
	             size_t disk_slice_count);
	
	/*!
	 * Attempt to seek to an offset within a slice.
	 *
	 * \param slice  The slice to seek to.
	 * \param offset The byte offset to seek to within the given slice.
	 *
	 * \return \c false if the requested slice could not be opened, or if the requested
	 *         offset is not a valid position in that slice - \c true otherwise.
	 */
	bool seek(size_t slice, boost::uint32_t offset);
	
	/*!
	 * Read a number of bytes starting at the current slice and offset within that slice.
	 *
	 * \param buffer Buffer to receive the bytes read.
	 * \param bytes  Number of bytes to read.
	 *
	 * The current offset will be advanced by the number of bytes read. It is not an error
	 * to read past the end of the current slice (unless it is the last slice). Doing so
	 * will automatically seek to the start of the next slice and continue reading from
	 * there.
	 *
	 * \return The number of bytes read or \c -1 if there was an error. Unless we are at the
	 *         end of the last slice, this function blocks until the number of requested
	 *         bytes have been read.
	 */
	std::streamsize read(char * buffer, std::streamsize bytes);
	
	//! \return the number currently opened slice.
	size_t slice() { return current_slice; }
	
	//! \return true a slice is currently open.
	bool is_open() { return (is != &ifs || ifs.is_open()); }
	
};

} // namespace stream

#endif // INNOEXTRACT_STREAM_SLICE_HPP
```

## File: `src/util/align.hpp`
```
/*
 * Copyright (C) 2011-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Utility functions for dealing with alignment of objects.
 */
#ifndef INNOEXTRACT_UTIL_ALIGN_HPP
#define INNOEXTRACT_UTIL_ALIGN_HPP

#include <limits>

#include "util/math.hpp"

#include "configure.hpp"

namespace util {

//! Get the alignment of a type.
template <class T>
unsigned int alignment_of() {
#if INNOEXTRACT_HAVE_ALIGNOF
	return alignof(T);
#elif defined(_MSC_VER) && _MSC_VER >= 1300
	return __alignof(T);
#elif defined(__GNUC__)
	return __alignof__(T);
#else
	return sizeof(T);
#endif
}

//! Check if a pointer has aparticular alignment.
inline bool is_aligned_on(const void * p, size_t alignment) {
	return alignment == 1
	       || (is_power_of_2(alignment) ? mod_power_of_2(size_t(p), alignment) == 0
	                                    : size_t(p) % alignment == 0);
}

//! Check if a pointer is aligned for a specific type.
template <class T>
bool is_aligned(const void * p) {
	return is_aligned_on(p, alignment_of<T>());
}

} // namespace util

#endif // INNOEXTRACT_UTIL_ALIGN_HPP
```

## File: `src/util/ansi.hpp`
```
/*
 * Copyright (C) 2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Parser for ANSI escape code sequences
 */
#ifndef INNOEXTRACT_UTIL_ANSI_HPP
#define INNOEXTRACT_UTIL_ANSI_HPP

#include <stddef.h>

#include <algorithm>
#include <iosfwd>
#include <sstream>
#include <string>
#include <vector>

#include <boost/iostreams/categories.hpp>

#include "util/load.hpp"
#include "util/types.hpp"

namespace util {

/*!
 * \brief CRTP base class that parses ANSI escape sequences
 *
 * Currently only supports parsing CSI sequences.
 *
 * This class cannot be instantiated by itself. Instead create a derivec class
 * \code class derived : public util::ansi_console_parser<derived>; \endcode
 * that re-implements \ref handle_command() and \ref handle_text().
 */
template <typename Impl>
class ansi_console_parser : public util::static_polymorphic<Impl> {
	
	//! Character that started the current control sequence, or \c 0
	char in_command;
	
	//! Buffer for control sequences if they span more than one flush
	std::vector<char> command;
	
protected:
	
	enum {
		ESC = '\x1b',
		CSI = '[', //!< Control Sequence Indicator (preceded by \ref ESC)
		UTF8CSI0 = '\xc2', //!< UTF-8 Control Sequence Indicator, first byte
		UTF8CSI1 = '\x9b', //!< UTF-8 Control Sequence Indicator, second byte
		Separator = ';' //! Separator for codes in CSI control sequences
	};
	
	enum CommandType {
		CUU = 'A', //!< Cursor Up
		CUD = 'B', //!< Cursor Down
		CUF = 'C', //!< Cursor Forward
		CUB = 'D', //!< Cursor Back
		CNL = 'E', //!< Cursor Next Line
		CPL = 'F', //!< Cursor Previous Line
		CHA = 'G', //!< Cursor Horizontal Absolute
		CUP = 'H', //!< Cursor Position
		ED  = 'J', //!< Erase Display
		EL  = 'K', //!< Erase in Line
		SU  = 'S', //!< Scroll Up
		SD  = 'T', //!< Scroll Down
		HVP = 'f', //!< Horizontal and Vertical Position
		SGR = 'm', //!< Select Graphic Rendition
		DSR = 'n', //!< Device Status Report
		SCP = 's', //!< Save Cursor Position
		RCP = 'u', //!< Restore Cursor Position
	};
	
private:
	
	struct is_start_char {
		bool operator()(char c) {
			return (c == ESC /* escape */ || c == UTF8CSI0 /* first byte of UTF-8 CSI */);
		}
	};
	
	struct is_end_char {
		bool operator()(char c) {
			return (c >= 64 && c < 127);
		}
	};
	
protected:
	
	#ifdef DEBUG
	void error(const std::string & str) {
		this->impl().handle_text(str.data(), str.length());
	}
	#endif
	
	/*!
	 * \brief Read one code form a command sequence
	 *
	 * \param s   Current position in the command sequence.
	 * \param end End of the command sequence.
	 *
	 * Each command sequence contains contains at least one code. Once there are no more
	 * commands in the command sequence, \c s will be set to \c NULL. After that has
	 * happened \ref read_code() should must not be called with the (\c s, \c end) pair.
	 *
	 * The meaning of th returned code depends on the type of the command sequence.
	 *
	 * \return the next code in the command sequence or unsigned(-1) if there was an error.
	 */
	unsigned read_code(const char * & s, const char * end) {
		
		const char * sep = std::find(s, end, Separator);
		
		unsigned code = unsigned(-1);
		try {
			code = (s == sep) ? 0u : util::to_unsigned(s, size_t(sep - s));
		} catch(...) {
			#ifdef DEBUG
			std::ostringstream oss;
			oss << "(bad command code: \"";
			oss.write(s, sep - s);
			oss << "\")";
			error(oss.str());
			#endif
		}
		
		if(sep == end) {
			s = NULL;
		} else {
			s = sep + 1;
		}
		
		return code;
	}
	
private:
	
	const char * read_command(const char * s, const char * end) {
		
		if(s == end) {
			return end; // Need to be able to read something
		}
		
		if(command.empty() && *s != (in_command == ESC ? CSI : UTF8CSI1)) {
			switch(in_command) {
				case ESC: /* escaped char */ break;
				default: {
					char utf8[] = { in_command, *s };
					this->impl().handle_text(utf8, 2);
				}
			}
			return s + 1; // Not a Control Sequence Initiator
		}
		
		const char * cmd = std::find_if(command.empty() ? s + 1 : s, end, is_end_char());
		
		const char * cs = s;
		const char * ce = cmd;
		
		if(!command.empty() || cmd == end) {
			command.insert(command.end(), s, cmd);
			cs = &command.front();
			ce = cs + command.size();
		}
		
		if(cmd == end) {
			return end; // Command not over yet
		}
		
		// Extract the command type
		CommandType type = CommandType(*cmd);
		
		// Skip starting character (part of the CSI sequence)
		cs++;
		
		this->impl().handle_command(type, cs, ce);
		
		in_command = 0;
		command.clear();
		
		return cmd + 1;
	}
	
public:
	
	ansi_console_parser() : in_command(0) { }
	
	typedef char char_type;
	typedef boost::iostreams::sink_tag category;
	
	/*!
	 * \brief Will be called when an ANSI escape sequence has been found
	 *
	 * Derived classes must override this.
	 *
	 * \param type  The type of command. This is the last character of the escape sequence.
	 * \param codes Start of the code sequence. Use \ref read_code() to read codes.
	 * \param end   End of the code sequence.
	 */
	void handle_command(CommandType type, const char * codes, const char * end);
	
	/*!
	 * \brief Will be called when plain text has been found
	 *
	 * Derived classes must override this.
	 *
	 * \param s Pointer to the text.
	 * \param n length of the text in bytes.
	 */
	void handle_text(const char * s, size_t n);
	
	/*!
	 * \brief Parse \c n characters from \c s
	 *
	 * The string may contain multiple escape sequences and escape sequences may span
	 * multiple calls to write().
	 *
	 * All escape sequences are passed to \ref handle_command() while plain text segments
	 * are passed to \ref handle_text().
	 *
	 * \return n
	 */
	std::streamsize write(const char * s, std::streamsize n) {
		
		const char * begin = s;
		const char * end = s + n;
		
		if(in_command) {
			s = read_command(s, end);
		}
		
		while(s != end) {
			
			const char * cmd = std::find_if(s, end, is_start_char());
			
			// Output the non-escaped text
			this->impl().handle_text(s, size_t(cmd - s));
			
			if(cmd == end) {
				s = end;
				break;
			}
			
			// A command possibly starts here
			in_command = *cmd;
			s = read_command(cmd + 1, end);
			
		}
		
		return s - begin;
	}
	
};

} // namespace util

#endif // INNOEXTRACT_UTIL_ANSI_HPP
```

## File: `src/util/boostfs_compat.hpp`
```
/*
 * Copyright (C) 2012-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Compatibility functions for older Boost.Filesystem versions.
 */
#ifndef INNOEXTRACT_UTIL_BOOSTFS_COMPAT_HPP
#define INNOEXTRACT_UTIL_BOOSTFS_COMPAT_HPP

#include <string>

#include <boost/filesystem/path.hpp>
#include <boost/filesystem/operations.hpp>

namespace util {

inline const std::string & as_string(const std::string & path) {
	return path;
}

inline const std::string as_string(const boost::filesystem::path & path) {
	return path.string();
}

} // namespace util

#endif // INNOEXTRACT_UTIL_BOOSTFS_COMPAT_HPP
```

## File: `src/util/console.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "util/console.hpp"

#include <algorithm>
#include <cmath>
#include <signal.h>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

#include "configure.hpp"

#if INNOEXTRACT_HAVE_ISATTY
#include <unistd.h>
#endif

#if INNOEXTRACT_HAVE_IOCTL
#include <sys/ioctl.h>
#endif

#include <boost/date_time/posix_time/posix_time_types.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/foreach.hpp>

#include "util/output.hpp"
#include "util/windows.hpp"

static bool show_progress = true;

#if defined(SIGWINCH)

// The last known screen width.
static int screen_width;

// A flag that signals that the console may have been resized
static volatile sig_atomic_t screen_resized;

static void sigwinch_handler(int sig) {
	(void)sig;
	screen_resized = 1;
	signal(SIGWINCH, sigwinch_handler);
}

#endif

namespace color {

shell_command black =       { "\x1b[1;30m" };
shell_command red =         { "\x1b[1;31m" };
shell_command green =       { "\x1b[1;32m" };
shell_command yellow =      { "\x1b[1;33m" };
shell_command blue =        { "\x1b[1;34m" };
shell_command magenta =     { "\x1b[1;35m" };
shell_command cyan =        { "\x1b[1;36m" };
shell_command white =       { "\x1b[1;37m" };

shell_command dim_black =   { "\x1b[;30m" };
shell_command dim_red =     { "\x1b[;31m" };
shell_command dim_green =   { "\x1b[;32m" };
shell_command dim_yellow =  { "\x1b[;33m" };
shell_command dim_blue =    { "\x1b[;34m" };
shell_command dim_magenta = { "\x1b[;35m" };
shell_command dim_cyan =    { "\x1b[;36m" };
shell_command dim_white =   { "\x1b[;37m" };

shell_command reset =       { "\x1b[m" };

shell_command current = reset;

void init(is_enabled color, is_enabled progress) {
	
	bool is_tty;
	#if defined(_WIN32) || INNOEXTRACT_HAVE_ISATTY
	is_tty = isatty(1) && isatty(2);
	#else
	// Since we can't check if stdout is a terminal,
	// don't automatically enable color output and progress bar
	is_tty = false;
	#endif
	
	#if !defined(_WIN32)
	if(is_tty) {
		char * term = std::getenv("TERM");
		if(!term || !std::strcmp(term, "dumb")) {
			is_tty = false; // Terminal does not support escape sequences
		}
	}
	#endif
	
	// Initialize the progress bar
	
	#if defined(SIGWINCH)
	sigwinch_handler(0);
	#endif
	
	show_progress = (progress == enable);
	#if defined(_WIN32) || (INNOEXTRACT_HAVE_IOCTL && defined(TIOCGWINSZ))
	// Only automatically enable the progress bar if we have a way to determine the width
	if(progress == automatic && is_tty) {
		show_progress = true;
	}
	#endif
	
	// Initialize color output
	
	if(color == disable || (color == automatic && (!is_tty || std::getenv("NO_COLOR") != NULL))) {
		
		reset.command = "";
		current.command = "";
		black.command = "";
		red.command = "";
		green.command = "";
		yellow.command = "";
		blue.command = "";
		magenta.command = "";
		cyan.command = "";
		white.command = "";
		dim_black.command = "";
		dim_red.command = "";
		dim_green.command = "";
		dim_yellow.command = "";
		dim_blue.command = "";
		dim_magenta.command = "";
		dim_cyan.command = "";
		dim_white.command = "";
		
	} else {
		
		#if defined(_WIN32)
		// For our Windows abstraction, the default color might differ from the initial one
		std::cout << reset;
		std::cerr << reset;
		#endif
		
	}
	
}

} // namespace color

static int query_screen_width() {
	
	#if defined(_WIN32)
	
	int width = util::console_width();
	if(width) {
		return width;
	}
	
	#endif
	
	#if INNOEXTRACT_HAVE_IOCTL && defined(TIOCGWINSZ)
	
	struct winsize w;
	if(ioctl(0, TIOCGWINSZ, &w) >= 0) {
		return w.ws_col;
	}
	
	#endif
	
	#if !defined(_WIN32)
	try {
		char * columns = std::getenv("COLUMNS");
		if(columns) {
			return boost::lexical_cast<int>(columns);
		}
	} catch(...) { /* ignore bad values */ }
	#endif
	
	// Assume a default screen width of 80 columns
	return 80;
	
}

static int get_screen_width() {
	
	#if defined(SIGWINCH)
	
	if(screen_resized) {
		screen_resized = 0;
		screen_width = query_screen_width();
	}
	
	return screen_width;
	
	#else
	return query_screen_width();
	#endif
	
}

static bool progress_cleared = true;

void progress::clear(ClearMode mode) {
	
	if(!show_progress) {
		return;
	}
	
	progress_cleared = true;
	
	#if defined(_WIN32)
	
	if(mode == FastClear) {
		
		/*
		 * If we overwrite the whole line with spaces, windows console likes to draw
		 * the empty line, even if it will be overwritten in the same flush(),
		 * causing the progress bar to flicker when updated.
		 * To work around this, don't actually clear the line if we are just going to
		 * overwrite it anyway.
		 * The progress bar still flickers when there is other output printed, but
		 * it seems there is no way around that without using the console API to manually
		 * scroll the output.
		 */
		
		std::cout << '\r';
		
		return;
		
	} else if(mode == DeferredClear && isatty(1)) {
		
		/*
		 * Special clear mode that leaves the original line but insert new lines before it
		 * until the next carriage return.
		 */
		
		std::cout << "\r\x1b[3K";
		
		return;
		
	}
	
	#else
	
	(void)mode;
	
	#endif
	
	// Use the ANSI/VT100 control sequence to clear the current line
	
	std::cout << "\r\x1b[K";
	
}

void progress::show(float value, const std::string & label) {
	
	if(!show_progress) {
		return;
	}
	
	clear(FastClear);
	
	int width = get_screen_width();
	
	std::ios_base::fmtflags flags = std::cout.flags();
	
	int progress_length = width - int(label.length()) - 6 - 2 - 2 - 1;
	
	if(progress_length > 10) {
		
		size_t progress = size_t(std::ceil(float(progress_length) * value));
		
		std::cout << '[';
		for(size_t i = 0; i < progress; i++) {
			std::cout << '=';
		}
		std::cout << '>';
		for(size_t i = progress; i < size_t(progress_length); i++) {
			std::cout << ' ';
		}
		std::cout << ']';
		
	}
	
	std::cout << std::right << std::fixed << std::setprecision(1) << std::setfill(' ')
	          << std::setw(5) << (value * 100) << "% " << label;
	std::cout.flush();
	
	std::cout.flags(flags);
	
	progress_cleared = false;
}

void progress::show_unbounded(float value, const std::string & label) {
	
	if(!show_progress) {
		return;
	}
	
	clear(FastClear);
	
	int width = get_screen_width();
	
	std::ios_base::fmtflags flags = std::cout.flags();
	
	int progress_length = width - int(label.length()) - 2 - 2 - 6;
	
	if(progress_length > 10) {
		
		size_t progress = std::min(size_t(std::ceil(float(progress_length) * value)),
		                  size_t(progress_length - 1));
		
		std::cout << '[';
		for(size_t i = 0; i < progress; i++) {
			std::cout << ' ';
		}
		std::cout << "<===>";
		for(size_t i = progress; i < size_t(progress_length); i++) {
			std::cout << ' ';
		}
		std::cout << ']';
		
	}
	
	std::cout << ' ' << label;
	std::cout.flush();
	
	std::cout.flags(flags);
	
	progress_cleared = false;
}

progress::progress(boost::uint64_t max_value, bool show_value_rate)
	: max(max_value), value(0), show_rate(show_value_rate),
	  start_time(boost::posix_time::microsec_clock::universal_time()),
	  last_status(-1.f), last_time(0), last_rate(0.f) { }

bool progress::update(boost::uint64_t delta, bool force) {
	
	if(!show_progress) {
		return false;
	}
	
	force = force || progress_cleared;
	
	value += delta;
	
	float status = 0.f;
	if(max) {
		status = float(std::min(value, max)) / float(max);
		status = float(size_t(1000.f * status)) * (1.f / 1000.f);
		if(!force && status == last_status) {
			return false;
		}
	}
	
	boost::uint64_t time;
	try {
		boost::posix_time::ptime now(boost::posix_time::microsec_clock::universal_time());
		time = boost::uint64_t((now - start_time).total_microseconds());
	} catch(...) {
		// this shouldn't happen, assume no time has passed
		time = last_time;
	}
	
	#if defined(_WIN32)
	const boost::uint64_t update_interval = 100000;
	#else
	const boost::uint64_t update_interval = 50000;
	#endif
	if(!force && time - last_time < update_interval) {
		return false;
	}
	
	last_time = time;
	last_status = status;
	
	if(!max) {
		status = std::fmod(float(time) * (1.f / 5000000.f), 2.f);
		if(status > 1.f) {
			status = 2.f - status;
		}
	}
	
	if(show_rate) {
		if(value >= 10 * 1024 && time > 0) {
			float rate = 1000000.f * float(value) / float(time);
			if(rate != last_rate) {
				last_rate = rate;
				label.str(std::string()); // clear the buffer
				label << std::right << std::fixed << std::setfill(' ') << std::setw(5)
				      << print_bytes(rate, 1) << "/s";
			}
		}
	}
	
	if(max) {
		show(status, label.str());
	} else {
		show_unbounded(status, label.str());
	}
	
	return true;
}

void progress::set_enabled(bool enable) {
	show_progress = enable;
}

bool progress::is_enabled() {
	return show_progress;
}

```

## File: `src/util/console.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Terminal output functions: colors, progress bar.
 */
#ifndef INNOEXTRACT_UTIL_CONSOLE_HPP
#define INNOEXTRACT_UTIL_CONSOLE_HPP

#include <stddef.h>
#include <ostream>
#include <iomanip>
#include <sstream>

#include <boost/date_time/posix_time/ptime.hpp>
#include <boost/cstdint.hpp>

namespace color {

/*!
 * Object that can be written to the console to change the output color.
 */
struct shell_command {
	const char * command;
};

//! Reset the output color to the original value.
extern shell_command reset;

extern shell_command black;
extern shell_command red;
extern shell_command green;
extern shell_command yellow;
extern shell_command blue;
extern shell_command magenta;
extern shell_command cyan;
extern shell_command white;

extern shell_command dim_black;
extern shell_command dim_red;
extern shell_command dim_green;
extern shell_command dim_yellow;
extern shell_command dim_blue;
extern shell_command dim_magenta;
extern shell_command dim_cyan;
extern shell_command dim_white;

//! The last set output color.
extern shell_command current;

inline std::ostream & operator<<(std::ostream & os, shell_command command) {
	color::current = command;
	return os << command.command;
}

enum is_enabled {
	enable,
	disable,
	automatic
};

/*!
 * Initilize console output functions.
 *
 * \param color    Enable or disable color output.
 * \param progress Enable or disable progress bar output.
 */
void init(is_enabled color = automatic, is_enabled progress = automatic);

} // namespace color

enum ClearMode {
	FullClear,    //!< Perform a full clear.
	FastClear,    //!< Perform a full clear if it is cheap, otherwise only reset the cursor.
	DeferredClear //!< Perform a full clear if it is cheap, otherwise leave the line as-is,
	              //!< but insert new writes before it until the next full/fast clear.
};

//! A text-based progress bar for terminals.
class progress {
	
	boost::uint64_t max;
	boost::uint64_t value;
	bool show_rate;
	
	boost::posix_time::ptime start_time;
	
	float last_status;
	boost::uint64_t last_time;
	
	float last_rate;
	std::ostringstream label;
	
public:
	
	/*!
	 * \param max_value       Maximumum progress values.
	 *                        If this value is \c 0, the progress bar will be unbounded.
	 * \param show_value_rate Display the rate at which the progress changes.
	 */
	progress(boost::uint64_t max_value = 0, bool show_value_rate = true);
	
	/*!
	 * Update the progress bar.
	 *
	 * \param delta Value to add to the progress. When the total progress value reaches the
	 *              maximum set in the constructor, the bar will be full.
	 * \param force Force updating the progress bar. Normally, the progress bar. Otherwise,
	 *              updates are rate-limited and small deltas are not displayed immediately.
	 *
	 * \return true if the progres bar was updated
	 */
	bool update(boost::uint64_t delta = 0, bool force = false);
	
	/*!
	 * Draw a bounded progress bar (with a maximum).
	 *
	 * \param value The progress value, between \c 0.f and \c 1.f.
	 * \param label A label to draw next to the progress bar.
	 */
	static void show(float value, const std::string & label = std::string());
	
	/*!
	 * Draw an unbounded progress bar (without a maximum).
	 *
	 * \param value The progress value, between \c 0.f and \c 1.f.
	 * \param label A label to draw next to the progress bar.
	 */
	static void show_unbounded(float value, const std::string & label = std::string());
	
	/*!
	 * Clear any progress bar to make way for other output.
	 *
	 * \param mode The clear mode to perform.
	 */
	static void clear(ClearMode mode = FullClear);
	
	//! Enable or disable the progress bar.
	static void set_enabled(bool enable);
	
	static bool is_enabled();
	
};

#endif // INNOEXTRACT_UTIL_CONSOLE_HPP
```

## File: `src/util/encoding.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */
// Parts based on:
////////////////////////////////////////////////////////////
//
// SFML - Simple and Fast Multimedia Library
// Copyright (C) 2007-2009 Laurent Gomila (laurent.gom@gmail.com)
//
// This software is provided 'as-is', without any express or implied warranty.
// In no event will the authors be held liable for any damages arising from the
// use of this software.
//
// Permission is granted to anyone to use this software for any purpose,
// including commercial applications, and to alter it and redistribute it freely,
// subject to the following restrictions:
//
// 1. The origin of this software must not be misrepresented;
//    you must not claim that you wrote the original software.
//    If you use this software in a product, an acknowledgment
//    in the product documentation would be appreciated but is not required.
//
// 2. Altered source versions must be plainly marked as such,
//    and must not be misrepresented as being the original software.
//
// 3. This notice may not be removed or altered from any source distribution.
//
////////////////////////////////////////////////////////////
//
// This code has been taken from SFML and altered to fit the project's needs.
//
////////////////////////////////////////////////////////////

#include "util/encoding.hpp"

#include <stddef.h>

#include <algorithm>
#include <iomanip>
#include <iterator>
#include <sstream>
#include <vector>

#include "configure.hpp"

#if INNOEXTRACT_HAVE_ICONV
#include <iconv.h>
#include <errno.h>
#endif

#if INNOEXTRACT_HAVE_WIN32_CONV
#include <windows.h>
#endif

#include <boost/foreach.hpp>
#include <boost/static_assert.hpp>
#include <boost/unordered_map.hpp>
#include <boost/range/size.hpp>

#include "util/log.hpp"
#include "util/math.hpp"

namespace util {

namespace {

//! Get names for encodings where iconv doesn't have the codepage alias
const char * get_encoding_name(codepage_id codepage) {
	switch(codepage) {
		case cp_ascii:        return "US-ASCII";
		case cp_big5:         return "BIG5";
		case cp_big5_eten:    return "BIG5";
		case cp_big5_hkscs:   return "BIG5-HKSCS";
		case cp_cns:          return "EUC-TW";
		case cp_dos708:       return "ISO-8859-6";
		case cp_euc_cn:       return "EUC-CN";
		case cp_euc_jp:       return "EUC-JP";
		case cp_euc_jp_ms:    return "EUC-JP-MS";
		case cp_euc_kr:       return "EUC-KR";
		case cp_euc_tw:       return "EUC-TW";
		case cp_gb2312_80:    return "GB2312";
		case cp_gb2312_hz:    return "GB2312";
		case cp_gb18030:      return "GB18030";
		case cp_gbk:          return "GBK";
		case cp_ia5:          return "ISO_646.IRV:1991";
		case cp_ia5_de:       return "ISO646-DE";
		case cp_ia5_no2:      return "ISO646-NO2";
		case cp_ia5_se2:      return "ISO646-SE2";
		case cp_ibm273:       return "IBM273";
		case cp_ibm277:       return "IBM277";
		case cp_ibm278:       return "IBM278";
		case cp_ibm280:       return "IBM280";
		case cp_ibm284:       return "IBM284";
		case cp_ibm285:       return "IBM285";
		case cp_ibm290:       return "IBM290";
		case cp_ibm297:       return "IBM297";
		case cp_ibm420:       return "IBM420";
		case cp_ibm423:       return "IBM423";
		case cp_ibm424:       return "IBM424";
		case cp_ibm833:       return "IBM833";
		case cp_ibm838:       return "IBM1160";
		case cp_ibm871:       return "IBM871";
		case cp_ibm880:       return "IBM880";
		case cp_ibm905:       return "IBM905";
		case cp_ibm924:       return "IBM1047";
		case cp_ibm930:       return "IBM930";
		case cp_ibm931:       return "IBM931";
		case cp_ibm933:       return "IBM933";
		case cp_ibm935:       return "IBM935";
		case cp_ibm936:       return "IBM936";
		case cp_ibm937:       return "IBM937";
		case cp_ibm939:       return "IBM939";
		case cp_ibm1025:      return "IBM1025";
		case cp_iso_2022_cn:  return "ISO-2022-CN";
		case cp_iso_2022_cn2: return "ISO-2022-CN-EXT";
		case cp_iso_2022_jp:  return "ISO-2022-JP";
		case cp_iso_2022_jp2: return "ISO-2022-JP-2";
		case cp_iso_2022_jp3: return "ISO-2022-JP-3";
		case cp_iso_2022_kr:  return "ISO-2022-KR";
		case cp_iso_6937:     return "ISO_6937";
		case cp_iso_8859_10:  return "ISO-8859-10";
		case cp_iso_8859_11:  return "ISO-8859-11";
		case cp_iso_8859_13:  return "ISO-8859-13";
		case cp_iso_8859_14:  return "ISO-8859-14";
		case cp_iso_8859_15:  return "ISO-8859-15";
		case cp_iso_8859_1:   return "ISO-8859-1";
		case cp_iso_8859_2:   return "ISO-8859-2";
		case cp_iso_8859_3:   return "ISO-8859-3";
		case cp_iso_8859_4:   return "ISO-8859-4";
		case cp_iso_8859_5:   return "ISO-8859-5";
		case cp_iso_8859_6:   return "ISO-8859-6";
		case cp_iso_8859_6i:  return "ISO-8859-6";
		case cp_iso_8859_7:   return "ISO-8859-7";
		case cp_iso_8859_8:   return "ISO-8859-8";
		case cp_iso_8859_8i:  return "ISO-8859-8";
		case cp_iso_8859_9:   return "ISO-8859-9";
		case cp_johab:        return "JOHAB";
		case cp_koi8_r:       return "KOI8-R";
		case cp_koi8_u:       return "KOI8-U";
		case cp_macarabic:    return "MACARABIC";
		case cp_macchinese1:  return "BIG5";
		case cp_macchinese2:  return "EUC-CN";
		case cp_maccroatian:  return "MACCROATIAN";
		case cp_maccyrillic:  return "MACCYRILLIC";
		case cp_macgreek:     return "MACGREEK";
		case cp_machebrew:    return "MACHEBREW";
		case cp_maciceland:   return "MACICELAND";
		case cp_macjapanese:  return "SHIFT-JIS";
		case cp_mackorean:    return "EUC-KR";
		case cp_macroman2:    return "MACCENTRALEUROPE";
		case cp_macroman:     return "MACINTOSH";
		case cp_macromania:   return "MACROMANIA";
		case cp_macthai:      return "MACTHAI";
		case cp_macturkish:   return "MACTURKISH";
		case cp_macukraine:   return "MACUKRAINE";
		case cp_shift_jis:    return "SHIFT-JIS";
		case cp_t61:          return "T.61";
		case cp_uhc:          return "UHC";
		case cp_utf7:         return "UTF-7";
		case cp_utf8:         return "UTF-8";
		case cp_utf16be:      return "UTF-16BE";
		case cp_utf16le:      return "UTF-16LE"; // "UTF-16" is platform-dependent without a BOM
		case cp_utf32be:      return "UTF-32BE";
		case cp_utf32le:      return "UTF-32LE";
		case cp_wansung:      return "EUC-KR";
		case cp_windows1250:  return "MS-EE";
		case cp_windows1251:  return "MS-CYRL";
		case cp_windows1252:  return "MS-ANSI";
		case cp_windows1253:  return "MS-GREEK";
		case cp_windows1254:  return "MS-TURK";
		case cp_windows1255:  return "MS-HEBR";
		case cp_windows1256:  return "MS-ARAB";
		default: return NULL;
	}
}

//! Check if a codepage is known to be a superset of ASCII - used for optimization only
bool is_extended_ascii(codepage_id codepage) {
	
	// cp_utf8 is handled separately
	
	if(codepage >= cp_windows1250 && codepage <= cp_windows1270) {
		return true;
	}
	
	if(codepage >= cp_iso_8859_1 && codepage <= cp_iso_8859_15) {
		return true;
	}
	
	switch(codepage) {
		case cp_ascii:
		case cp_big5:
		case cp_big5_eten:
		case cp_big5_hkscs:
		case cp_cns:
		case cp_dos708:
		case cp_euc_cn:
		case cp_euc_tw:
		case cp_gb18030:
		case cp_gbk:
		case cp_iso_6937:
		case cp_iso_8859_6i:
		case cp_iso_8859_8i:
		case cp_koi8_r:
		case cp_koi8_u:
		case cp_macarabic:
		case cp_macchinese1:
		case cp_macchinese2:
		case cp_maccyrillic:
		case cp_macgreek:
		case cp_maciceland:
		case cp_macroman:
		case cp_uhc:
		case cp_windows874:
			return true;
		default:
			return false;
	}
	
}

bool is_ascii(const std::string & data) {
	// String in an extended ASCII encoding contains only ASCII characters
	BOOST_FOREACH(char c, data) {
		if(boost::uint8_t(c) >= 128) {
			return false;
		}
	}
	return true;
}

//! Check if a string is compatible with UTF-8
bool is_utf8(const std::string & data, codepage_id codepage) {
	
	if(codepage == cp_utf8 || codepage == cp_ascii) {
		return true;
	}
	
	if(is_extended_ascii(codepage) && is_ascii(data)) {
		return true;
	}
	
	return false;
}

typedef boost::uint32_t unicode_char;

const unicode_char replacement_char = '_';

size_t get_code_unit_size(codepage_id codepage) {
	switch(codepage) {
		case cp_utf16le: return 2u;
		case cp_utf16be: return 2u;
		case cp_utf32le: return 4u;
		case cp_utf32be: return 4u;
		default:    return 1u;
	}
}

//! Fallback conversion that will at least work for ASCII characters
void to_utf8_fallback(const std::string & from, std::string & to, codepage_id codepage) {
	
	size_t skip = get_code_unit_size(codepage);
	
	size_t shift = 0;
	switch(codepage) {
		case cp_utf16be: shift = 1u * 8u; break;
		case cp_utf32be: shift = 3u * 8u; break;
		default: break;
	}
	
	to.clear();
	to.reserve(ceildiv(from.size(), skip));
	
	bool warn = false;
	
	for(std::string::const_iterator it = from.begin(); it != from.end();) {
		
		unicode_char unicode = 0;
		for(size_t i = 0; i < skip; i++) {
			unicode |= unicode_char(boost::uint8_t(*it++)) << (i * 8);
		}
		
		char ascii = char((unicode >> shift) & 0x7f);
		
		// replace non-ASCII characters with underscores
		if((unicode_char(ascii) << shift) != unicode) {
			warn = true;
			ascii = char(replacement_char);
		}
		
		to.push_back(ascii);
	}
	
	if(warn) {
		log_warning << "Unknown data while converting from CP" << codepage << " to UTF-8.";
	}
	
}

bool is_utf8_continuation_byte(unicode_char chr) {
	return (chr & 0xc0) == 0x80;
}

template <typename In>
unicode_char utf8_read(In & it, In end, unicode_char replacement = replacement_char) {
	
	if(it == end) {
		return unicode_char(-1);
	}
	unicode_char chr = boost::uint8_t(*it++);
	
	// For multi-byte characters, read the remaining bytes
	if(chr & (1 << 7)) {
		
		if(is_utf8_continuation_byte(chr)) {
			// Bad start position
			return replacement;
		}
		
		if(it == end || !is_utf8_continuation_byte(boost::uint8_t(*it))) {
			// Unexpected end of multi-byte sequence
			return replacement;
		}
		chr &= 0x3f, chr <<= 6, chr |= unicode_char(boost::uint8_t(*it++) & 0x3f);
		
		if(chr & (1 << (5 + 6))) {
			
			if(it == end || !is_utf8_continuation_byte(boost::uint8_t(*it))) {
				// Unexpected end of multi-byte sequence
				return replacement;
			}
			chr &= ~unicode_char(1 << (5 + 6)), chr <<= 6, chr |= unicode_char(boost::uint8_t(*it++) & 0x3f);
			
			if(chr & (1 << (4 + 6 + 6))) {
				
				if(it == end || !is_utf8_continuation_byte(boost::uint8_t(*it))) {
					// Unexpected end of multi-byte sequence
					return replacement;
				}
				chr &= ~unicode_char(1 << (4 + 6 + 6)), chr <<= 6, chr |= unicode_char(boost::uint8_t(*it++) & 0x3f);
				
				if(chr & (1 << (3 + 6 + 6 + 6))) {
					// Illegal UTF-8 byte
					return replacement;
				}
				
			}
		}
	}
	
	return chr;
}

size_t utf8_length(unicode_char chr) {
	if(chr < 0x80) {
		return 1;
	} else if(chr < 0x800) {
		return 2;
	} else if(chr < 0x10000) {
		return 3;
	} else if(chr <= 0x0010ffff) {
		return 4;
	}
	return 1;
}

void utf8_write(std::string & to, unicode_char chr) {
	
	static const boost::uint8_t first_bytes[7] = {
		0x00, 0x00, 0xc0, 0xe0, 0xf0, 0xf8, 0xfc
	};
	
	// Get number of bytes to write
	size_t length = utf8_length(chr);
	
	// Extract bytes to write
	boost::uint8_t bytes[4];
	switch(length) {
		case 4: bytes[3] = static_cast<boost::uint8_t>((chr | 0x80) & 0xBF), chr >>= 6; /* fall-through */
		case 3: bytes[2] = static_cast<boost::uint8_t>((chr | 0x80) & 0xBF), chr >>= 6; /* fall-through */
		case 2: bytes[1] = static_cast<boost::uint8_t>((chr | 0x80) & 0xBF), chr >>= 6; /* fall-through */
		case 1: bytes[0] = static_cast<boost::uint8_t>(chr | first_bytes[length]);
		default: break;
	}
	
	// Add them to the output
	const boost::uint8_t * cur_byte = bytes;
	switch(length) {
		case 4: to.push_back(char(*cur_byte++)); /* fall-through */
		case 3: to.push_back(char(*cur_byte++)); /* fall-through */
		case 2: to.push_back(char(*cur_byte++)); /* fall-through */
		case 1: to.push_back(char(*cur_byte++));
		default: break;
	}
	
}

//! \return true c is is the first part of an UTF-16 surrogate pair
bool is_utf16_high_surrogate(unicode_char chr) {
	return chr >= 0xd800 && chr <= 0xdbff;
}

//! \return true c is is the second part of an UTF-16 surrogate pair
bool is_utf16_low_surrogate(unicode_char chr) {
	return chr >= 0xdc00 && chr <= 0xdfff;
}

} // anonymous namespace

void utf16le_to_wtf8(const std::string & from, std::string & to) {
	
	if(from.size() % 2 != 0) {
		log_warning << "Unexpected trailing byte in UTF-16 string.";
	}
	
	to.clear();
	to.reserve(from.size() / 2); // optimistically, most strings only have ASCII characters
	
	bool warn = false;
	
	std::string::const_iterator it = from.begin();
	std::string::const_iterator end = from.end();
	if(from.size() % 2 != 0) {
		--end;
	}
	while(it != end) {
		
		unicode_char chr = boost::uint8_t(*it++);
		chr |= unicode_char(boost::uint8_t(*it++)) << 8;
		
		// If it's a surrogate pair, convert to a single UTF-32 character
		if(is_utf16_high_surrogate(chr) && it != end) {
			unicode_char d = boost::uint8_t(*it);
			d |= unicode_char(boost::uint8_t(*(it + 1))) << 8;
			if(is_utf16_low_surrogate(d)) {
				chr = ((chr - 0xd800) << 10) + (d - 0xdc00) + 0x0010000;
				it += 2;
			}
		}
		
		utf8_write(to, chr);
	}
	if(end != from.end()) {
		warn = true;
		utf8_write(to, replacement_char);
	}
	
	if(warn) {
		log_warning << "Unexpected data while converting from UTF-16LE to UTF-8.";
	}
	
}

const char * wtf8_find_end(const char * begin, const char * end) {
	
	const char * i = end;
	while(i != begin && is_utf8_continuation_byte(boost::uint8_t(*(i - 1)))) {
		i--;
	}
	
	if(i != begin) {
		unicode_char chr = boost::uint8_t(*(i - 1));
		size_t expected = 0;
		if(chr & (1 << 7)) {
			expected++;
			if(chr & (1 << (5 + 6))) {
				expected++;
				if(chr & (1 << (4 + 6 + 6))) {
					expected++;
				}
			}
		}
		if(expected > size_t(end - i)) {
			return i - 1;
		}
	}
	
	return end;
}

void wtf8_to_utf16le(const char * begin, const char * end, std::string & to) {
	
	to.clear();
	to.reserve(size_t(end - begin) * 2); // optimistically, most strings only have ASCII characters
	
	for(const char * i = begin; i != end; ) {
		
		unicode_char chr = utf8_read(i, end);
		
		if(chr >= 0x10000) {
			chr -= 0x10000;
			unicode_char high_surrogate = 0xd800 + (chr >> 10);
			to.push_back(char(boost::uint8_t(high_surrogate)));
			to.push_back(char(boost::uint8_t(high_surrogate >> 8)));
			chr = 0xdc00 + (chr & 0x3ff);
		}
		
		to.push_back(char(boost::uint8_t(chr)));
		to.push_back(char(boost::uint8_t(chr >> 8)));
	}
	
}

void wtf8_to_utf16le(const std::string & from, std::string & to) {
	return wtf8_to_utf16le(from.c_str(), from.c_str() + from.size(), to);
}

namespace {

unicode_char windows1252_replacements[] = {
	0x20ac, replacement_char, 0x201a, 0x192, 0x201e, 0x2026, 0x2020, 0x2021, 0x2c6,
	0x2030, 0x160, 0x2039, 0x152, replacement_char, 0x17d, replacement_char,
	replacement_char, 0x2018, 0x2019, 0x201c, 0x201d, 0x2022, 0x2013, 0x2014, 0x2dc,
	0x2122, 0x161, 0x203a, 0x153, replacement_char, 0x17e, 0x178
};

BOOST_STATIC_ASSERT(sizeof(windows1252_replacements) == (160 - 128) * sizeof(*windows1252_replacements));

void windows1252_to_utf8(const std::string & from, std::string & to) {
	
	to.clear();
	to.reserve(from.size()); // optimistically, most strings only have ASCII characters
	
	bool warn = false;
	
	BOOST_FOREACH(char c, from) {
		
		// Windows-1252 maps almost directly to Unicode - yay!
		unicode_char chr = boost::uint8_t(c);
		if(chr >= 128 && chr < 160) {
			chr = windows1252_replacements[chr - 128];
			warn = warn || chr == replacement_char;
		}
		
		utf8_write(to, chr);
	}
	
	if(warn) {
		log_warning << "Unexpected data while converting from Windows-1252 to UTF-8.";
	}
	
}

void utf8_to_windows1252(const std::string & from, std::string & to) {
	
	to.clear();
	to.reserve(from.size()); // optimistically, most strings only have ASCII characters
	
	bool warn = false;
	
	for(std::string::const_iterator i = from.begin(); i != from.end(); ) {
		
		unicode_char chr = utf8_read(i, from.end());
		
		// Windows-1252 maps almost directly to Unicode - yay!
		if(chr >= 256 || (chr >= 128 && chr < 160)) {
			size_t j = 0;
			for(; j < size_t(boost::size(windows1252_replacements)); j++) {
				if(chr == windows1252_replacements[j] && windows1252_replacements[j] != replacement_char) {
					break;
				}
			}
			if(j < size_t(boost::size(windows1252_replacements))) {
				chr = unicode_char(128 + j);
			} else {
				chr = replacement_char;
				warn = true;
			}
		}
		
		to.push_back(char(boost::uint8_t(chr)));
	}
	
	if(warn) {
		log_warning << "Unsupported character while converting from UTF-8 to Windows-1252.";
	}
	
}

#if INNOEXTRACT_HAVE_ICONV

typedef boost::unordered_map<codepage_id, iconv_t> converter_map;
converter_map converters;

iconv_t get_converter(codepage_id codepage, bool reverse) {
	
	boost::uint32_t key = codepage | (reverse ? 0x80000000 : 0);
	
	// Try to reuse an existing converter if possible
	converter_map::const_iterator i = converters.find(key);
	if(i != converters.end()) {
		return i->second;
	}
	
	iconv_t handle = iconv_t(-1);
	
	const char * encoding = get_encoding_name(codepage);
	if(encoding) {
		handle = reverse ? iconv_open(encoding, "UTF-8") : iconv_open("UTF-8", encoding);
	}
	
	// Otherwise, try a few different codepage name prefixes
	if(handle == iconv_t(-1)) {
		const char * prefixes[] = { "MSCP", "CP", "WINDOWS-", "MS", "IBM", "IBM-", "" };
		BOOST_FOREACH(const char * prefix, prefixes) {
			std::ostringstream oss;
			oss << prefix << std::setfill('0') << std::setw(3) << codepage;
			handle = reverse ? iconv_open(oss.str().c_str(), "UTF-8") : iconv_open("UTF-8", oss.str().c_str());
			if(handle != iconv_t(-1)) {
				break;
			}
		}
	}
	
	if(handle == iconv_t(-1)) {
		log_warning << "Could not get codepage " << codepage << " -> UTF-8 converter.";
	}
	
	return converters[key] = handle;
}

bool utf8_iconv(const std::string & from, std::string & to, codepage_id codepage, bool reverse) {
	
	iconv_t converter = get_converter(codepage, reverse);
	if(converter == iconv_t(-1)) {
		return false;
	}
	
	/*
	 * Some iconv implementations declare the second parameter of iconv() as
	 * const char **, others as char **.
	 * Use this little hack to compile with both variants.
	 */
	struct inbuf_ {
		const char * buf;
		explicit inbuf_(const char * data) : buf(data) { }
		operator const char **() { return &buf; }
		operator char **() { return const_cast<char **>(&buf); }
	} inbuf(from.data());
	
	size_t insize = from.size();
	
	size_t outbase = 0;
	
	iconv(converter, NULL, NULL, NULL, NULL);
	
	size_t skip = get_code_unit_size(codepage);
	
	bool warn = false;
	
	while(insize) {
		
		to.resize(outbase + ceildiv(insize, skip) + 4);
		
		char * outbuf = &to[0] + outbase;
		size_t outsize = to.size() - outbase;
		
		size_t ret = iconv(converter, inbuf, &insize, &outbuf, &outsize);
		if(ret == size_t(-1)) {
			if(errno == E2BIG) {
				// not enough output space - we'll allocate more in the next loop
			} else if(/*errno == EILSEQ &&*/ insize >= 2) {
				// invalid byte (sequence) - add a replacement char and try the next byte
				if(outsize == 0) {
					to.push_back(char(replacement_char));
				} else {
					*outbuf = char(replacement_char);
					outsize--;
				}
				inbuf.buf += skip;
				insize -= skip;
				warn = true;
			} else {
				// something else went wrong - return what we have so far
				insize = 0;
				warn = true;
			}
		}
		
		outbase = to.size() - outsize;
	}
	
	if(warn) {
		if(reverse) {
			log_warning << "Unexpected data while converting from UTF-8 to CP" << codepage << ".";
		} else {
			log_warning << "Unexpected data while converting from CP" << codepage << " to UTF-8.";
		}
	}
	
	to.resize(outbase);
	
	return true;
}

bool to_utf8_iconv(const std::string & from, std::string & to, codepage_id codepage) {
	return utf8_iconv(from, to, codepage, false);
}

bool from_utf8_iconv(const std::string & from, std::string & to, codepage_id codepage) {
	return utf8_iconv(from, to, codepage, true);
}

#endif // INNOEXTRACT_HAVE_ICONV

#if INNOEXTRACT_HAVE_WIN32_CONV

std::string windows_error_string(DWORD code) {
	char * error;
	DWORD n = FormatMessageA(FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_ALLOCATE_BUFFER,
	                         NULL, code, 0, reinterpret_cast<char *>(&error), 0, NULL);
	if(n == 0) {
		return "unknown";
	} else {
		std::string ret(error, size_t(n));
		LocalFree(error);
		if(!ret.empty() && ret[ret.size() - 1] == '\n') {
			ret.resize(ret.size() - 1);
		}
		return ret;
	}
}

bool to_utf8_win32(const std::string & from, std::string & to, codepage_id codepage) {
	 
	// Convert from the source codepage to UTF-16LE
	std::string buffer;
	int ret = MultiByteToWideChar(codepage, 0, from.data(), int(from.length()), NULL, 0);
	if(ret > 0) {
		buffer.resize(size_t(ret) * 2);
		ret = MultiByteToWideChar(codepage, 0, from.data(), int(from.length()),
		                          reinterpret_cast<LPWSTR>(&buffer[0]), ret);
	}
	if(ret <= 0) {
		log_warning << "Error while converting from CP" << codepage << " to UTF-16: "
		            << windows_error_string(GetLastError());
		return false;
	}
	
	utf16le_to_wtf8(buffer, to);
	
	return true;
}

bool from_utf8_win32(const std::string & from, std::string & to, codepage_id codepage) {
	
	std::string buffer;
	wtf8_to_utf16le(from, buffer);
	
	// Convert from UTF-16LE to the target codepage
	LPCWSTR data = reinterpret_cast<LPCWSTR>(buffer.c_str());
	int size = int(buffer.size() / 2);
	int ret = WideCharToMultiByte(codepage, 0, data, size, NULL, 0,  NULL, NULL);
	if(ret > 0) {
		to.resize(size_t(ret));
		ret = WideCharToMultiByte(codepage, 0, data, size, &to[0], ret, NULL, NULL);
	}
	if(ret <= 0) {
		log_warning << "Error while converting from UTF-16 to CP" << codepage << ": "
		            << windows_error_string(GetLastError());
		return false;
	}
	
	return true;
}

#endif // INNOEXTRACT_HAVE_WIN32_CONV

void to_utf8(const std::string & from, std::string & to, codepage_id codepage,
             const std::bitset<256> * lead_bytes) {
	
	switch(codepage) {
		case cp_utf16le:     utf16le_to_wtf8(from, to); return;
		case cp_windows1252: windows1252_to_utf8(from, to); return;
		case cp_iso_8859_1:  windows1252_to_utf8(from, to); return;
		default: break;
	}
	
	if(lead_bytes) {
		std::string buffer;
		for(size_t start = 0; start < from.length();) {
			size_t end = start;
			while(end < from.length()) {
				if(lead_bytes->test(static_cast<unsigned char>(from[end]))) {
					end = std::min(from.length(), end + 2);
				} else if(from[end] != 0x5C) {
					end++;
				} else {
					break;
				}
			}
			buffer = from.substr(start, end - start);
			util::to_utf8(buffer, codepage, NULL);
			to.append(buffer);
			if(end < from.length()) {
				to.push_back('\\');
			}
			start = end + 1;
		}
		return;
	}
	
	#if INNOEXTRACT_HAVE_ICONV
	if(to_utf8_iconv(from, to, codepage)) {
		return;
	}
	#endif
	
	#if INNOEXTRACT_HAVE_WIN32_CONV
	if(to_utf8_win32(from, to, codepage)) {
		return;
	}
	#endif
	
	to_utf8_fallback(from, to, codepage);
	
}

} // anonymous namespace

void to_utf8(std::string & data, codepage_id codepage, const std::bitset<256> * lead_bytes) {
	
	if(data.empty() || is_utf8(data, codepage)) {
		// Already UTF-8
		return;
	}
	
	std::string buffer;
	to_utf8(data, buffer, codepage, lead_bytes);
	std::swap(data, buffer);
}

void from_utf8(const std::string & from, std::string & to, codepage_id codepage) {
	
	if(from.empty()) {
		to.clear();
		return;
	}
	
	if(codepage == cp_utf8 || (is_extended_ascii(codepage) && is_ascii(from))) {
		to = from;
		return;
	}
	
	switch(codepage) {
		case cp_utf16le:     wtf8_to_utf16le(from, to); return;
		case cp_windows1252: utf8_to_windows1252(from, to); return;
		default: break;
	}
	
	#if INNOEXTRACT_HAVE_ICONV
	if(from_utf8_iconv(from, to, codepage)) {
		return;
	}
	#endif
	
	#if INNOEXTRACT_HAVE_WIN32_CONV
	if(from_utf8_win32(from, to, codepage)) {
		return;
	}
	#endif
	
	log_warning << "Unsupported output codepage: " << codepage;
	to = from;
	
}

std::string encoding_name(codepage_id codepage) {
	
	const char * name = get_encoding_name(codepage);
	if(name) {
		return name;
	}
	
	std::ostringstream oss;
	oss << "Windows-" << codepage;
	
	return oss.str();
}

} // namespace util
```

## File: `src/util/encoding.hpp`
```
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Utility function to convert strings to UTF-8.
 */
#ifndef INNOEXTRACT_UTIL_ENCODING_HPP
#define INNOEXTRACT_UTIL_ENCODING_HPP

#include <bitset>
#include <string>

#include <boost/cstdint.hpp>

namespace util {

enum known_codepages {
	cp_dos708       =   708, // arabic
	cp_windows874   =   874, // thai
	cp_shift_jis    =   932, // japanese
	cp_gbk          =   936, // chinese
	cp_uhc          =   949, // korean
	cp_big5         =   950, // chinese
	cp_big5_hkscs   =   951, // chinese
	cp_utf16le      =  1200,
	cp_utf16be      =  1201,
	cp_windows1250  =  1250, // latin
	cp_windows1251  =  1251, // cyrillic
	cp_windows1252  =  1252, // latin
	cp_windows1253  =  1253, // greek
	cp_windows1254  =  1254, // turkish
	cp_windows1255  =  1255, // hebrew
	cp_windows1256  =  1256, // arabic
	cp_windows1257  =  1257, // baltic
	cp_windows1258  =  1258, // vietnamese
	cp_windows1270  =  1270, // sami
	cp_johab        =  1361, // korean
	cp_macroman     = 10000, // latin
	cp_macjapanese  = 10001, // japanese
	cp_macchinese1  = 10002, // chinese
	cp_mackorean    = 10003, // korean
	cp_macarabic    = 10004, // arabic
	cp_machebrew    = 10005, // hebrew
	cp_macgreek     = 10006, // greek
	cp_maccyrillic  = 10007, // cyrillic
	cp_macchinese2  = 10008, // chinese
	cp_macromania   = 10010, // latin
	cp_macukraine   = 10017, // cyrillic
	cp_macthai      = 10021, // thai
	cp_macroman2    = 10029, // latin
	cp_maciceland   = 10079, // latin
	cp_macturkish   = 10081, // turkish
	cp_maccroatian  = 10082, // latin
	cp_utf32le      = 12000,
	cp_utf32be      = 12001,
	cp_cns          = 20000, // chinese
	cp_big5_eten    = 20002, // chinese
	cp_ia5          = 20105, // latin
	cp_ia5_de       = 20106, // latin
	cp_ia5_se2      = 20107, // latin
	cp_ia5_no2      = 20108, // latin
	cp_ascii        = 20127, // latin
	cp_t61          = 20261, // latin
	cp_iso_6937     = 20269, // latin
	cp_ibm273       = 20273, // latin
	cp_ibm277       = 20277, // latin
	cp_ibm278       = 20278, // latin
	cp_ibm280       = 20280, // latin
	cp_ibm284       = 20284, // latin
	cp_ibm285       = 20285, // latin
	cp_ibm290       = 20290, // japanese
	cp_ibm297       = 20297, // latin
	cp_ibm420       = 20420, // arabic
	cp_ibm423       = 20423, // greek
	cp_ibm424       = 20424, // hebrew
	cp_ibm833       = 20833, // korean
	cp_ibm838       = 20838, // thai
	cp_koi8_r       = 20866, // cyrillic
	cp_ibm871       = 20871, // latin
	cp_ibm880       = 20880, // cyrillic
	cp_ibm905       = 20905, // turkish
	cp_ibm924       = 20924, // latin
	cp_euc_jp_ms    = 20932, // japanese
	cp_gb2312_80    = 20936, // chinese
	cp_wansung      = 20949, // korean
	cp_ibm1025      = 21025, // cyrillic
	cp_koi8_u       = 21866, // cyrillic
	cp_iso_8859_1   = 28591, // latin
	cp_iso_8859_2   = 28592, // latin
	cp_iso_8859_3   = 28593, // latin
	cp_iso_8859_4   = 28594, // latin
	cp_iso_8859_5   = 28595, // cyrillic
	cp_iso_8859_6   = 28596, // arabic
	cp_iso_8859_7   = 28597, // greek
	cp_iso_8859_8   = 28598, // hebrew
	cp_iso_8859_9   = 28599, // turkish
	cp_iso_8859_10  = 28600, // latin
	cp_iso_8859_11  = 28601, // thai
	cp_iso_8859_13  = 28603, // baltic
	cp_iso_8859_14  = 28604, // celtic
	cp_iso_8859_15  = 28605, // latin
	cp_europa3      = 29001, // latin
	cp_iso_8859_6i  = 38596, // hebrew
	cp_iso_8859_8i  = 38598, // hebrew
	cp_iso_2022_jp  = 50220, // japanese
	cp_iso_2022_jp2 = 50221, // japanese
	cp_iso_2022_jp3 = 50222, // japanese
	cp_iso_2022_kr  = 50225, // korean
	cp_iso_2022_cn  = 50227, // chinese
	cp_iso_2022_cn2 = 50229, // chinese
	cp_ibm930       = 50930, // japanese
	cp_ibm931       = 50931, // japanese
	cp_ibm933       = 50933, // korean
	cp_ibm935       = 50935, // chinese
	cp_ibm936       = 50936, // chinese
	cp_ibm937       = 50937, // chinese
	cp_ibm939       = 50939, // japanese
	cp_euc_jp       = 51932, // japanese
	cp_euc_cn       = 51936, // chinese
	cp_euc_kr       = 51949, // korean
	cp_euc_tw       = 51950, // chinese
	cp_gb2312_hz    = 52936, // chinese
	cp_gb18030      = 54936, // chinese
	cp_utf7         = 65000,
	cp_utf8         = 65001,
};

typedef boost::uint32_t codepage_id;

/*!
 * Convert a possibly broken UTF-16 string to WTF-8, an extension of UTF-8.
 */
void utf16le_to_wtf8(const std::string & from, std::string & to);

/*!
 * Find the end of the last complete WTF-8 character in a string.
 */
const char * wtf8_find_end(const char * begin, const char * end);

/*!
 * Convert WTF-8 to UTF-16 while preserving unpaired surrogates.
 */
void wtf8_to_utf16le(const char * begin, const char * end, std::string & to);

/*!
 * Convert WTF-8 to UTF-16 while preserving unpaired surrogates.
 */
void wtf8_to_utf16le(const std::string & from, std::string & to);

/*!
 * Convert a string in place to UTF-8 from a specified encoding.
 * \param data       The input string to convert.
 * \param codepage   The Windows codepage number for the input string encoding.
 * \param lead_bytes Preserve 0x5C path separators.
 *
 * \note This function is not thread-safe.
 */
void to_utf8(std::string & data, codepage_id codepage = cp_windows1252,
             const std::bitset<256> * lead_bytes = NULL);

/*!
 * Convert a string from UTF-8 to a specified encoding.
 * \param from     The input string to convert.
 * \param to       The output for the converted string.
 * \param codepage The Windows codepage number for the input string encoding.
 *
 * \note This function is not thread-safe.
 */
void from_utf8(const std::string & from, std::string & to, codepage_id codepage = cp_windows1252);

std::string encoding_name(codepage_id codepage);

} // namespace util

#endif // INNOEXTRACT_UTIL_ENCODING_HPP
```

## File: `src/util/endian.hpp`
```
/*
 * Copyright (C) 2011-2017 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Utility functions for dealing with different endiannesses.
 */
#ifndef INNOEXTRACT_UTIL_ENDIAN_HPP
#define INNOEXTRACT_UTIL_ENDIAN_HPP

#include <cstdlib>
#include <cstring>

#include "configure.hpp"

#if INNOEXTRACT_HAVE_BSWAP_16 || INNOEXTRACT_HAVE_BSWAP_32 || INNOEXTRACT_HAVE_BSWAP_64
#include <byteswap.h>
#endif

#include <boost/cstdint.hpp>

namespace util {

namespace detail {

inline boost::uint8_t byteswap(boost::uint8_t value) {
	return value;
}

inline boost::int8_t byteswap(boost::int8_t value) {
	return boost::int8_t(byteswap(boost::uint8_t(value)));
}

inline boost::uint16_t byteswap(boost::uint16_t value) {
#if INNOEXTRACT_HAVE_BUILTIN_BSWAP16
	return __builtin_bswap16(value);
#elif defined(_MSC_VER) && _MSC_VER >= 1300
	return _byteswap_ushort(value);
#elif INNOEXTRACT_HAVE_BSWAP_16 \
	&& (!defined(__GLIBC__) || !defined(__GLIBC_MINOR__) \
	    || (__GLIBC__ << 16) + __GLIBC_MINOR__ >= (2 << 16) + 16) \
	    // prevent conversion warnings
	return bswap_16(value);
#else
	return boost::uint16_t((boost::uint16_t(boost::uint8_t(value)) << 8)
	                       | boost::uint8_t(value >> 8));
#endif
}

inline boost::int16_t byteswap(boost::int16_t value) {
	return boost::int16_t(byteswap(boost::uint16_t(value)));
}

inline boost::uint32_t byteswap(boost::uint32_t value) {
#if INNOEXTRACT_HAVE_BUILTIN_BSWAP32
	return __builtin_bswap32(value);
#elif defined(_MSC_VER) && (_MSC_VER >= 1400 || (_MSC_VER >= 1300 && !defined(_DLL)))
	return _byteswap_ulong(value);
#elif INNOEXTRACT_HAVE_BSWAP_32
	return bswap_32(value);
#else
	return (boost::uint32_t(byteswap(boost::uint16_t(value))) << 16)
	       | byteswap(boost::uint16_t(value >> 16));
#endif
}

inline boost::int32_t byteswap(boost::int32_t value) {
	return boost::int32_t(byteswap(boost::uint32_t(value)));
}

inline boost::uint64_t byteswap(boost::uint64_t value) {
#if INNOEXTRACT_HAVE_BUILTIN_BSWAP64
	return __builtin_bswap64(value);
#elif defined(_MSC_VER) && _MSC_VER >= 1300
	return _byteswap_uint64(value);
#elif INNOEXTRACT_HAVE_BSWAP_64
	return bswap_64(value);
#else
	return (boost::uint64_t(byteswap(boost::uint32_t(value))) << 32)
	       | byteswap(boost::uint32_t(value >> 32));
#endif
}

inline boost::int64_t byteswap(boost::int64_t value) {
	return boost::int64_t(byteswap(boost::uint64_t(value)));
}

} // namespace detail

//! Load/store functions for a specific endianness.
template <typename Endianness>
struct endianness {
	
	/*!
	 * Load a single integer.
	 *
	 * \param buffer Memory location containing the integer. Will read sizeof(T) bytes.
	 * \return the loaded integer.
	 */
	template <typename T>
	static T load(const char * buffer) {
		if(Endianness::native()) {
			T value;
			std::memcpy(&value, buffer, sizeof(value));
			return value;
		} else {
			return load_alien<T>(buffer);
		}
	}
	
	/*!
	 * Load an array of integers.
	 *
	 * \param buffer Memory location containing the integers (without padding).
	 *               Will read <code>sizeof(T) * count</code> bytes.
	 * \param values Output array for the loaded integers.
	 * \param count  How many integers to load.
	 */
	template <typename T>
	static void load(const char * buffer, T * values, size_t count) {
		if(Endianness::native() || sizeof(*values) == 1) {
			std::memcpy(values, buffer, sizeof(*values) * count);
		} else {
			for(size_t i = 0; i < count; i++, buffer += sizeof(*values)) {
				values[i] = load_alien<T>(buffer);
			}
		}
	}
	
	/*!
	 * Store a single integer.
	 *
	 * \param value  The integer to store.
	 * \param buffer Memory location to receive the integer. Will write sizeof(T) bytes.
	 */
	template <typename T>
	static void store(T value, char * buffer) {
		if(Endianness::native()) {
			std::memcpy(buffer, &value, sizeof(value));
		} else {
			return store_alien(value, buffer);
		}
	}
	
	/*!
	 * Store an array of integers.
	 *
	 * \param values The integers to store.
	 * \param count  How many integers to store.
	 * \param buffer Memory location to receive the integers (without padding).
	 *               Will write <code>sizeof(T) * count</code> bytes.
	 */
	template <typename T>
	static void store(T * values, size_t count, char * buffer) {
		if(Endianness::native() || sizeof(*values) == 1) {
			std::memcpy(buffer, values, sizeof(*values) * count);
		} else {
			for(size_t i = 0; i < count; i++, buffer += sizeof(*values)) {
				store_alien(values[i], buffer);
			}
		}
	}
	
private:
	
	bool reversed() { return false; }
	
	template <typename T>
	static T load_alien(const char * buffer) {
		if(Endianness::reversed()) {
			T value;
			std::memcpy(&value, buffer, sizeof(value));
			return detail::byteswap(value);
		} else {
			return Endianness::template decode<T>(buffer);
		}
	}
	
	template <typename T>
	static void store_alien(T value, char * buffer) {
		if(Endianness::reversed()) {
			value = detail::byteswap(value);
			std::memcpy(buffer, &value, sizeof(value));
		} else {
			Endianness::template encode<T>(value, buffer);
		}
	}
	
};

namespace detail {

inline bool is_little_endian() {
	boost::uint32_t signature = 0x04030201;
	return (*reinterpret_cast<char *>(&signature) == 1);
}

inline bool is_big_endian() {
	boost::uint32_t signature = 0x04030201;
	return (*reinterpret_cast<char *>(&signature) == 4);
}

} // namespace detail


//! Load and store little-endian integers.
struct little_endian : endianness<little_endian> {
	
	//! \return true if we are running on a little-endian machine.
	static bool native() { return detail::is_little_endian(); }
	
private:
	
	static bool reversed() { return detail::is_big_endian(); }
	
	template <typename T>
	static T decode(const char * buffer) {
		T value = 0;
		for(size_t i = 0; i < sizeof(T); i++) {
			value = T(value | (T(buffer[i]) << (i * 8)));
		}
		return value;
	}
	
	template <typename T>
	static void encode(T value, char * buffer) {
		for(size_t i = 0; i < sizeof(T); i++) {
			buffer[i] = char((value >> (i * 8)) & 0xff);
		}
	}
	
	friend struct endianness<little_endian>;
};

//! Load and store big-endian integers.
struct big_endian : endianness<big_endian> {
	
	//! \return true if we are running on a big-endian machine.
	static bool native() { return detail::is_big_endian(); }
	
private:
	
	static bool reversed() { return detail::is_little_endian(); }
	
	template <typename T>
	static T decode(const char * buffer) {
		T value = 0;
		for(size_t i = 0; i < sizeof(T); i++) {
			value = T(value | T(buffer[i]) << ((sizeof(T) - i - 1) * 8));
		}
		return value;
	}
	
	template <typename T>
	static void encode(T value, char * buffer) {
		for(size_t i = 0; i < sizeof(T); i++) {
			buffer[i] = char((value >> ((sizeof(T) - i - 1) * 8)) & 0xff);
		}
	}
	
	friend struct endianness<big_endian>;
};

} // namespace util

#endif // INNOEXTRACT_UTIL_ENDIAN_HPP
```

## File: `src/util/enum.hpp`
```
/*
 * Copyright (C) 2011-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Utilities to associate strings with enum values.
 */
#ifndef INNOEXTRACT_UTIL_ENUM_HPP
#define INNOEXTRACT_UTIL_ENUM_HPP

#include <stddef.h>
#include <ostream>

#include <boost/range/size.hpp>
#include <boost/utility/enable_if.hpp>

#include "util/console.hpp"
#include "util/flags.hpp"

template <class Enum>
struct get_enum {
	typedef Enum type;
};
template <class Enum>
struct get_enum< flags<Enum> > {
	typedef Enum type;
};

template <class Enum>
struct enum_names {
	
	const size_t count;
	
	const char * name;
	
	const char * names[1];
	
};

#define NAMED_ENUM(Enum) \
	template <> struct enum_names<get_enum<Enum>::type> { \
		enum { named = 1 }; \
		static const char * name; \
		static const char * names[]; \
		static const size_t count; \
	};
	
#define NAMED_FLAGS(Flags) \
	FLAGS_OVERLOADS(Flags) \
	NAMED_ENUM(Flags)

#define NAMES(Enum, Name, ...) \
	const char * enum_names<get_enum<Enum>::type>::name = (Name); \
	const char * enum_names<get_enum<Enum>::type>::names[] = { __VA_ARGS__ }; \
	const size_t enum_names<get_enum<Enum>::type>::count \
	 = size_t(boost::size(enum_names<get_enum<Enum>::type>::names));

#define USE_ENUM_NAMES(Enum) \
	(void)enum_names<get_enum<Enum>::type>::count; \
	(void)enum_names<get_enum<Enum>::type>::name; \
	(void)enum_names<get_enum<Enum>::type>::names;

#define USE_FLAG_NAMES(Flags) \
	USE_FLAGS_OVERLOADS(Flags) \
	USE_ENUM_NAMES(Flags)

template <class Enum>
typename boost::enable_if_c<enum_names<Enum>::named, std::ostream &>::type
operator<<(std::ostream & os, Enum value) {
	if(value >= Enum(0)) {
		size_t i = size_t(value);
		if(i < enum_names<Enum>::count) {
			return os << enum_names<Enum>::names[value];
		}
	}
	return os << "(unknown:" << int(value) << ')';
}

template <class Enum>
std::ostream & operator<<(std::ostream & os, flags<Enum> _flags) {
	color::shell_command prev = color::current;
	if(_flags) {
		bool first = true;
		for(size_t i = 0; i < flags<Enum>::bits; i++) {
			if(_flags & Enum(i)) {
				if(first) {
					first = false;
				} else {
					os << color::dim_white << ", " << prev;
				}
				os << Enum(i);
			}
		}
		return os;
	} else {
		return os << color::dim_white << "(none)" << prev;
	}
}

#endif // INNOEXTRACT_UTIL_ENUM_HPP
```

## File: `src/util/flags.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Typesafe flags.
 */
#ifndef INNOEXTRACT_UTIL_FLAGS_HPP
#define INNOEXTRACT_UTIL_FLAGS_HPP

#include <stddef.h>
#include <bitset>

// loosely based on Qflags from Qt

template <typename Enum>
struct enum_size {
	static const size_t value;
};

/*!
 * A typesafe way to define flags as a combination of enum values.
 * 
 * This type should not be used directly, only through DECLARE_FLAGS.
 */
template <typename Enum, size_t Bits = enum_size<Enum>::value>
class flags {
	
public:
	
	typedef Enum enum_type;
	static const size_t bits = Bits;
	typedef std::bitset<bits> Type;
	
private:
	
	typedef void ** Zero;
	typedef void(*TypesafeBoolean)();
	
	Type _flags;
	
	explicit flags(Type flag) : _flags(flag) { }
	
public:
	
	/* implicit */ inline flags(enum_type flag) : _flags(Type().set(size_t(flag))) { }
	
	/* implicit */ inline flags(Zero /* zero */ = 0) : _flags() { }
	
	static flags load(Type _flags) {
		return flags(_flags, true);
	}
	
	//! Test if a specific flag is set.
	bool has(enum_type flag) const {
		return _flags.test(size_t(flag));
	}
	
	//! Test if a collection of flags are all set.
	bool hasAll(flags o) const {
		return (_flags & o._flags) == o._flags;
	}
	
	operator TypesafeBoolean() const {
		return reinterpret_cast<TypesafeBoolean>(_flags.any());
	}
	
	bool operator==(flags o) const {
		return _flags == o._flags;
	}
	
	bool operator!=(flags o) const {
		return _flags != o._flags;
	}
	
	bool operator==(Zero /* zero */) const {
		return _flags == 0;
	}
	
	bool operator!=(Zero /* zero */) const {
		return _flags != 0;
	}
	
	flags operator~() const {
		return flags(~_flags);
	}
	
	bool operator!() const {
		return _flags.none();
	}
	
	flags operator&(flags o) const {
		return flags(_flags & o._flags);
	}
	
	flags operator|(flags o) const {
		return flags(_flags | o._flags);
	}
	
	flags operator^(flags o) const {
		return flags(_flags ^ o._flags);
	}
	
	flags & operator&=(const flags & o) {
		_flags &= o._flags;
		return *this;
	}
	
	flags & operator|=(flags o) {
		_flags |= o._flags;
		return *this;
	}
	
	flags & operator^=(flags o) {
		_flags ^= o._flags;
		return *this;
	}
	
	flags operator&(enum_type flag) const {
		return operator&(flags(flag));
	}
	
	flags operator|(enum_type flag) const {
		return operator|(flags(flag));
	}
	
	flags operator^(enum_type flag) const {
		return operator^(flags(flag));
	}
	
	flags & operator&=(enum_type flag) {
		return operator&=(flags(flag));
	}
	
	flags & operator|=(enum_type flag) {
		return operator|=(flags(flag));
	}
	
	flags & operator^=(enum_type flag) {
		return operator^=(flag);
	}
	
	//! Get a set of flags with all possible values set.
	static flags all() {
		return flags(Type().flip());
	}
	
};

template <typename Enum, size_t Bits>
flags<Enum, Bits> operator|(Enum a, flags<Enum, Bits> b) {
	return b | a;
}

#define DECLARE_ENUM_SIZE(Enum, Size) \
	template <> \
	struct enum_size<Enum> { \
		static const size_t value = (Size); \
	};
#define FLAGS_ENUM_END_HELPER(Enum) Enum ## _End_
#define FLAGS_ENUM_END(Enum) FLAGS_ENUM_END_HELPER(Enum)

/*!
 * Declare overloaded operators for a flag type
 *
 * \param Flagname the flag to declare operators for
 */
#define DECLARE_FLAGS_OPERATORS(Flagname) \
	inline Flagname operator|(Flagname::enum_type a, Flagname::enum_type b) { \
		return Flagname(a) | b; \
	} \
	inline Flagname operator~(Flagname::enum_type a) { \
		return ~Flagname(a); \
	}

//! Get the enum name for a set of flags
#define FLAGS_ENUM(Flagname) Flagname ## _Enum_

/*!
 * Declare a set of flags
 *
 * \param Flagname the name for the flags
 * \param ... the flags to declare
 */
#define FLAGS(Flagname, ...) \
	enum FLAGS_ENUM(Flagname) { \
		__VA_ARGS__, \
		FLAGS_ENUM_END(Flagname) \
	}; \
	typedef ::flags<FLAGS_ENUM(Flagname), FLAGS_ENUM_END(Flagname)> Flagname

/*!
 * Declare overloaded operators and enum_size for a flag type
 *
 * \param Flagname the flag to declare operators for
 */
#define FLAGS_OVERLOADS(Flagname) \
	DECLARE_ENUM_SIZE(FLAGS_ENUM(Flagname), FLAGS_ENUM_END(Flagname)) \
	DECLARE_FLAGS_OPERATORS(Flagname)

#define USE_FLAGS_OVERLOADS(Flagname) \
	(void)(~Flagname::enum_type(0)); \
	(void)(Flagname::enum_type(0) | Flagname::enum_type(0));

#endif // INNOEXTRACT_UTIL_FLAGS_HPP
```

## File: `src/util/fstream.hpp`
```
/*
 * Copyright (C) 2013-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * boost::filesystem::{i,o,}fstream doesn't support unicode names on windows
 * Implement our own wrapper using boost::iostreams.
 */
#ifndef INNOEXTRACT_UTIL_FSTREAM_HPP
#define INNOEXTRACT_UTIL_FSTREAM_HPP

#if !defined(_WIN32)

#include <boost/filesystem/fstream.hpp>

namespace util {

typedef boost::filesystem::ifstream ifstream;
typedef boost::filesystem::ofstream ofstream;
typedef boost::filesystem::fstream  fstream;

} // namespace util

#else // if defined(_WIN32)

#include <boost/filesystem/path.hpp>
#include <boost/iostreams/device/file_descriptor.hpp>
#include <boost/iostreams/stream.hpp>

namespace util {

/*!
 * {i,o,}fstream implementation with support for Unicode filenames.
 * Create a subclass instead of a typedef to force boost::filesystem::path parameters.
 */
template <typename Device>
class path_fstream : public boost::iostreams::stream<Device> {
	
private: // disallow copying
	
	path_fstream(const path_fstream &);
	const path_fstream & operator=(const path_fstream &);
	
	typedef boost::filesystem::path path;
	typedef boost::iostreams::stream<Device> base;
	
	Device & device() { return **this; }
	
	void fix_open_mode(std::ios_base::openmode mode);
	
public:
	
	path_fstream() : base(Device()) { }
	
	explicit path_fstream(const path & p) : base(p) { }
	
	path_fstream(const path & p, std::ios_base::openmode mode) : base(p, mode) {
		fix_open_mode(mode);
	}
	
	void open(const path & p) {
		base::close();
		base::open(p);
	}

	void open(const path & p, std::ios_base::openmode mode) {
		base::close();
		base::open(p, mode);
		fix_open_mode(mode);
	}
	
	bool is_open() {
		return device().is_open(); // return the real open state, not base::is_open()
	}
	
	virtual ~path_fstream() { }
};

template <>
inline void path_fstream<boost::iostreams::file_descriptor_source>
	::fix_open_mode(std::ios_base::openmode mode) {
	if((mode & std::ios_base::ate) && is_open()) {
		seekg(0, std::ios_base::end);
	}
}

template <>
inline void path_fstream<boost::iostreams::file_descriptor_sink>
	::fix_open_mode(std::ios_base::openmode mode) {
	if((mode & std::ios_base::ate) && is_open()) {
		seekp(0, std::ios_base::end);
	}
}

template <>
inline void path_fstream<boost::iostreams::file_descriptor>
	::fix_open_mode(std::ios_base::openmode mode) {
	if((mode & std::ios_base::ate) && is_open()) {
		seekg(0, std::ios_base::end);
		seekp(0, std::ios_base::end);
	}
}

typedef path_fstream<boost::iostreams::file_descriptor_source> ifstream;
typedef path_fstream<boost::iostreams::file_descriptor_sink>   ofstream;
typedef path_fstream<boost::iostreams::file_descriptor>        fstream;

} // namespace util

#endif // defined(_WIN32)

#endif // INNOEXTRACT_UTIL_FSTREAM_HPP
```

## File: `src/util/load.cpp`
```cpp
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "util/load.hpp"

#include <algorithm>

#include <boost/lexical_cast.hpp>

namespace util {

void binary_string::load(std::istream & is, std::string & target) {
	
	boost::uint32_t length = util::load<boost::uint32_t>(is);
	if(is.fail()) {
		return;
	}
	
	target.clear();
	
	while(length) {
		char buffer[10 * 1024];
		boost::uint32_t buf_size = std::min(length, boost::uint32_t(sizeof(buffer)));
		is.read(buffer, std::streamsize(buf_size));
		target.append(buffer, buf_size);
		length -= buf_size;
	}
}

void binary_string::skip(std::istream & is) {
	
	boost::uint32_t length = util::load<boost::uint32_t>(is);
	if(is.fail()) {
		return;
	}
	
	discard(is, length);
}

void encoded_string::load(std::istream & is, std::string & target, codepage_id codepage,
                          const std::bitset<256> * lead_bytes) {
	binary_string::load(is, target);
	to_utf8(target, codepage, lead_bytes);
}

unsigned to_unsigned(const char * chars, size_t count) {
#if BOOST_VERSION < 105200
	return boost::lexical_cast<unsigned>(std::string(chars, count));
#else
	return boost::lexical_cast<unsigned>(chars, count);
#endif
}

} // namespace util
```

## File: `src/util/load.hpp`
```
/*
 * Copyright (C) 2011-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Utility function to load stored data while properly handling encodings and endianness.
 */
#ifndef INNOEXTRACT_UTIL_LOAD_HPP
#define INNOEXTRACT_UTIL_LOAD_HPP

#include <bitset>
#include <cstring>
#include <istream>
#include <string>

#include <boost/cstdint.hpp>
#include <boost/range/size.hpp>

#include "util/encoding.hpp"
#include "util/endian.hpp"
#include "util/types.hpp"

namespace util {

/*!
 * Wrapper to load a length-prefixed string from an input stream into a std::string.
 * The string length is stored as 32-bit integer.
 *
 * Usage: <code>is >> binary_string(str)</code>
 *
 * Use \ref encoded_string to also convert the string to UTF-8.
 */
struct binary_string {
	
	std::string & data;
	
	/*!
	 * \param target The std::string object to receive the loaded string.
	 */
	explicit binary_string(std::string & target) : data(target) { }
	
	//! Load a length-prefixed string
	static void load(std::istream & is, std::string & target);
	
	static void skip(std::istream & is);
	
	//! Load a length-prefixed string
	static std::string load(std::istream & is) {
		std::string target;
		load(is, target);
		return target;
	}
	
};
inline std::istream & operator>>(std::istream & is, const binary_string & str) {
	binary_string::load(is, str.data);
	return is;
}

/*!
 * Wrapper to load a length-prefixed string with a specified encoding from an input stream
 * into a UTF-8 encoded std::string.
 * The string length is stored as 32-bit integer.
 *
 * Usage: <code>is >> encoded_string(str, codepage)</code>
 *
 * You can also use the \ref ansi_string convenience wrapper for Windows-1252 strings.
 *
 * \note This wrapper is not thread-safe.
 */
struct encoded_string {
	
	std::string & data;
	codepage_id codepage;
	const std::bitset<256> * lead_byte_set;
	
	/*!
	 * \param target     The std::string object to receive the loaded UTF-8 string.
	 * \param cp         The Windows codepage for the encoding of the stored string.
	 */
	encoded_string(std::string & target, codepage_id cp)
		: data(target), codepage(cp), lead_byte_set(NULL) { }
	
	/*!
	 * \param target     The std::string object to receive the loaded UTF-8 string.
	 * \param cp         The Windows codepage for the encoding of the stored string.
	 * \param lead_bytes Preserve 0x5C path separators.
	 */
	encoded_string(std::string & target, codepage_id cp, const std::bitset<256> & lead_bytes)
		: data(target), codepage(cp), lead_byte_set(&lead_bytes) { }
	
	/*!
	 * Load and convert a length-prefixed string
	 *
	 * \note This function is not thread-safe.
	 */
	static void load(std::istream & is, std::string & target, codepage_id codepage,
	                 const std::bitset<256> * lead_bytes = NULL);
	
	/*!
	 * Load and convert a length-prefixed string
	 *
	 * \note This function is not thread-safe.
	 */
	static std::string load(std::istream & is, codepage_id codepage,
	                        const std::bitset<256> * lead_bytes = NULL) {
		std::string target;
		load(is, target, codepage, lead_bytes);
		return target;
	}
	
};
inline std::istream & operator>>(std::istream & is, const encoded_string & str) {
	encoded_string::load(is, str.data, str.codepage, str.lead_byte_set);
	return is;
}

/*!
 * Convenience specialization of \ref encoded_string for loading Windows-1252 strings
 *
 * \note This function is not thread-safe.
 */
struct ansi_string : encoded_string {
	
	explicit ansi_string(std::string & target) : encoded_string(target, 1252) { }
	
};

//! Load a value of type T that is stored with a specific endianness.
template <class T, class Endianness>
T load(std::istream & is) {
	char buffer[sizeof(T)];
	is.read(buffer, std::streamsize(sizeof(buffer)));
	return Endianness::template load<T>(buffer);
}
//! Load a value of type T that is stored as little endian.
template <class T>
T load(std::istream & is) { return load<T, little_endian>(is); }

//! Load a bool value
inline bool load_bool(std::istream & is) {
	return !!load<boost::uint8_t>(is);
}

/*!
 * Load a value of type T that is stored with a specific endianness.
 * \param is   Input stream to load from.
 * \param bits The number of bits used to store the number.
 */
template <class T, class Endianness>
T load(std::istream & is, size_t bits) {
	if(bits == 8) {
		return load<typename compatible_integer<T, 8>::type, Endianness>(is);
	} else if(bits == 16) {
		return load<typename compatible_integer<T, 16>::type, Endianness>(is);
	} else if(bits == 32) {
		return load<typename compatible_integer<T, 32>::type, Endianness>(is);
	} else {
		return load<typename compatible_integer<T, 64>::type, Endianness>(is);
	}
}
/*!
 * Load a value of type T that is stored as little endian.
 * \param is   Input stream to load from.
 * \param bits The number of bits used to store the number.
 */
template <class T>
T load(std::istream & is, size_t bits) { return load<T, little_endian>(is, bits); }

/*!
 * Discard a number of bytes from a non-seekable input stream or stream-like object
 * \param is    The stream to "seek"
 * \param bytes Number of bytes to skip ahead
 */
template <class T>
void discard(T & is, boost::uint64_t bytes) {
	char buf[1024];
	while(bytes) {
		std::streamsize n = std::streamsize(std::min<boost::uint64_t>(bytes, sizeof(buf)));
		is.read(buf, n);
		bytes -= boost::uint64_t(n);
	}
}

/*!
 * Get the number represented by a specific range of bits of another number.
 * All other bis are masked and the requested bits are shifted to position 0.
 * \param number The number containing the desired bits.
 * \param first  Index of the first desired bit.
 * \param last   Index of the last desired bit (inclusive).
 */
template <typename T>
T get_bits(T number, unsigned first, unsigned last) {
	typedef typename uint_t<int(sizeof(T) * 8)>::exact UT;
	UT data = UT(number);
	data = UT(data >> first), last -= first;
	UT mask = UT(((last + 1 == sizeof(T) * 8) ? UT(0) : UT(UT(1) << (last + 1))) - 1);
	return T(data & mask);
}

/*!
 * Parse an ASCII representation of an unsigned integer
 * \throws boost::bad_lexical_cast on error
 */
unsigned to_unsigned(const char * chars, size_t count);

} // namespace util

#endif // INNOEXTRACT_UTIL_LOAD_HPP
```

## File: `src/util/log.cpp`
```cpp
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "util/log.hpp"

#include <iostream>

#include "util/console.hpp"

bool logger::debug = false;
bool logger::quiet = false;

size_t logger::total_errors = 0;
size_t logger::total_warnings = 0;

logger::~logger() {
	
	color::shell_command previous = color::current;
	progress::clear();
	
	switch(level) {
		case Debug:   std::cout << color::cyan   << buffer.str() << previous << "\n"; break;
		case Info:    std::cout << color::white  << buffer.str() << previous << "\n"; break;
		case Warning: {
			std::cerr << color::yellow << "Warning: " << buffer.str() << previous << "\n";
			total_warnings++;
			break;
		}
		case Error: {
			std::cerr << color::red << buffer.str() << previous << "\n";
			total_errors++;
			break;
		}
	}
	
}

std::streambuf * warning_suppressor::set_streambuf(std::streambuf * streambuf) {
	return std::cerr.rdbuf(streambuf);
}

void warning_suppressor::flush() {
	restore();
	std::cerr << buffer.str();
	logger::total_warnings += warnings;
	logger::total_errors += errors;
}
```

## File: `src/util/log.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Logging functions.
 */
#ifndef INNOEXTRACT_UTIL_LOG_HPP
#define INNOEXTRACT_UTIL_LOG_HPP

#include <sstream>
#include <string>

#include <boost/noncopyable.hpp>

#ifdef DEBUG
#define debug(...) \
	if(::logger::debug) \
		::logger(::logger::Debug) << __VA_ARGS__
#else
#define debug(...)
#endif

#define log_info \
	if(!::logger::quiet) \
		::logger(::logger::Info)
#define log_warning ::logger(::logger::Warning)
#define log_error   ::logger(::logger::Error)

/*!
 * logger class that allows longging via the stream operator.
 */
class logger : private boost::noncopyable {
	
public:
	
	enum log_level {
		Debug,
		Info,
		Warning,
		Error
	};
	
private:
	
	const log_level level;
	
	std::ostringstream buffer; //! Buffer for the log message excluding level, file and line.
	
public:
	
	static size_t total_warnings; //! Total number of \ref log_warning uses so far.
	static size_t total_errors;   //! Total number of \ref log_error uses so far.
	
	static bool debug; //! Is \ref debug output enabled?
	static bool quiet; //! Is \ref log_info disabled?
	
	/*!
	 * Construct a log line output stream.
	 *
	 * You probably don't want to use this directly - use \ref debug, \ref log_info,
	 * \ref log_warning and \ref log_error instead.
	 */
	explicit logger(log_level _level) : level(_level) { }
	
	template <class T>
	logger & operator<<(const T & i) {
		buffer << i;
		return *this;
	}
	
	~logger();
	
};

class warning_storage {
	
protected:
	
	
public:
	
};

class warning_suppressor : public warning_storage {
	
	std::ostringstream buffer;
	std::streambuf * streambuf;
	size_t warnings;
	size_t errors;
	
	static std::streambuf * set_streambuf(std::streambuf * streambuf);
	
public:
	
	warning_suppressor()
		: streambuf(set_streambuf(buffer.rdbuf()))
		, warnings(logger::total_warnings)
		, errors(logger::total_errors)
	{ }
	
	~warning_suppressor() {
		restore();
	}
	
	void restore() {
		
		if(!streambuf) {
			return;
		}
		
		set_streambuf(streambuf);
		streambuf = NULL;
		
		size_t new_warnings = logger::total_warnings - warnings;
		size_t new_errors = logger::total_errors - errors;
		logger::total_warnings = warnings;
		logger::total_errors = errors;
		warnings = new_warnings;
		errors = new_errors;
		
	}
	
	void flush();
	
	operator bool() {
		return buffer.tellp() != std::ostringstream::pos_type(0);
	}
	
};

#endif // INNOEXTRACT_UTIL_LOG_HPP
```

## File: `src/util/math.hpp`
```
/*
 * Copyright (C) 2011-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Math helper functions.
 */
#ifndef INNOEXTRACT_UTIL_MATH_HPP
#define INNOEXTRACT_UTIL_MATH_HPP

#ifdef _MSC_VER
#include <intrin.h>
#endif

namespace util {

//! Divide by a number and round up the result.
template <typename T>
T ceildiv(T num, T denom) {
	return (num + (denom - T(1))) / denom;
}

//! Check if an integer is a power of two.
template <class T>
bool is_power_of_2(const T & n) {
	return n > 0 && (n & (n - 1)) == 0;
}

//! Calculate <code>a % b</code> where b is always a power of two.
template <class T1, class T2>
T2 mod_power_of_2(const T1 & a, const T2 & b) {
	return T2(a) & (b - 1);
}

namespace detail {

template <bool overflow>
struct safe_shifter {
	
	template <class T>
	static T right_shift(T /* value */, unsigned int /* bits */) {
		return 0;
	}

	template <class T>
	static T left_shift(T /* value */, unsigned int /* bits */) {
		return 0;
	}
	
};

template <>
struct safe_shifter<false> {
	
	template <class T>
	static T right_shift(T value, unsigned int bits) {
		return value >> bits;
	}

	template <class T>
	static T left_shift(T value, unsigned int bits) {
		return value << bits;
	}
	
};

} // namespace detail

//! Right-shift a value without shifting past the size of the type or return 0.
template <unsigned int bits, class T>
T safe_right_shift(T value) {
	return detail::safe_shifter<(bits >= (8 * sizeof(T)))>::right_shift(value, bits);
}

//! Left-shift a value without shifting past the size of the type or return 0.
template <unsigned int bits, class T>
T safe_left_shift(T value) {
	return detail::safe_shifter<(bits >= (8 * sizeof(T)))>::left_shift(value, bits);
}

//! Rotate left.
template <class T> T rotl_fixed(T x, unsigned int y) {
	return T((x << y) | (x >> (sizeof(T) * 8 - y)));
}

//! Rotate right.
template <class T> T rotr_fixed(T x, unsigned int y) {
	return T((x >> y) | (x << (sizeof(T) * 8 - y)));
}

#if defined(_MSC_VER) && _MSC_VER >= 1400 && !defined(__INTEL_COMPILER)

template <>
inline boost::uint8_t rotl_fixed<boost::uint8_t>(boost::uint8_t x, unsigned int y) {
	return y ? _rotl8(x, y) : x;
}

template <>
inline boost::uint16_t rotl_fixed<boost::uint16_t>(boost::uint16_t x, unsigned int y) {
	return y ? _rotl16(x, y) : x;
}

#endif

#ifdef _MSC_VER
template <>
inline boost::uint32_t rotl_fixed<boost::uint32_t>(boost::uint32_t x, unsigned int y) {
	return y ? _lrotl(x, y) : x;
}
#endif

#if defined(_MSC_VER) && _MSC_VER >= 1300 && !defined(__INTEL_COMPILER)
template <>
inline boost::uint64_t rotl_fixed<boost::uint64_t>(boost::uint64_t x, unsigned int y) {
	return y ? _rotl64(x, y) : x;
}
#endif

} // namespace util

#endif // INNOEXTRACT_UTIL_MATH_HPP
```

## File: `src/util/output.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Output utility functions.
 */
#ifndef INNOEXTRACT_UTIL_OUTPUT_HPP
#define INNOEXTRACT_UTIL_OUTPUT_HPP

#include <ostream>
#include <string>

#include <boost/cstdint.hpp>
#include <boost/range/size.hpp>

#include "util/console.hpp"

struct quoted {
	
	const std::string & str;
	
	explicit quoted(const std::string & _str) : str(_str) { }
	
};

inline std::ostream & operator<<(std::ostream & os, const quoted & q) {
	color::shell_command prev = color::current;
	os << '"' << color::green;
	for(std::string::const_iterator i = q.str.begin(); i != q.str.end(); ++i) {
		boost::uint8_t c = boost::uint8_t(*i);
		if(c < ' ' && c != '\t' && c != '\r' && c != '\n') {
			std::ios_base::fmtflags old = os.flags();
			os << color::red << '<' << std::hex << std::setfill('0') << std::setw(2)
			   << int(c) << '>' << color::green;
			os.setf(old, std::ios_base::basefield);
		} else {
			os << *i;
		}
	}
	return os << prev << '"';
}

struct if_not_empty {
	
	const std::string & name;
	const std::string & value;
	
	if_not_empty(const std::string & _name, const std::string & _value)
		: name(_name), value(_value) { }
	
};

inline std::ostream & operator<<(std::ostream & os, const if_not_empty & s) {
	if(s.value.length() > 100) {
		color::shell_command prev = color::current;
		return os << s.name << ": " << color::white << s.value.length() << prev
		          << " bytes" << '\n';
	} else if(!s.value.empty()) {
		return os << s.name << ": " << quoted(s.value) << '\n';
	} else {
		return os;
	}
}

namespace detail {

template <class T>
struct if_not {
	
	const std::string & name;
	const T value;
	const T excluded;
	
	if_not(const std::string & _name, T _value, T _excluded)
		: name(_name), value(_value), excluded(_excluded) { }
	
};

template <class T>
std::ostream & operator<<(std::ostream & os, const if_not<T> & s) {
	if(s.value != s.excluded) {
		color::shell_command prev = color::current;
		return os << s.name << ": " << color::cyan << s.value << prev << '\n';
	} else {
		return os;
	}
}

} // namespace detail


template <class T>
detail::if_not<T> if_not_equal(const std::string & name, T value, T excluded) {
	return detail::if_not<T>(name, value, excluded);
}

template <class T>
detail::if_not<T> if_not_zero(const std::string & name, T value) {
	return detail::if_not<T>(name, value, T(0));
}

namespace detail {

template <class T>
struct print_hex {
	
	T value;
	
	explicit print_hex(T data) : value(data) { }
	
	bool operator==(const print_hex & o) const { return value == o.value; }
	bool operator!=(const print_hex & o) const { return value != o.value; }
	
};

template <class T>
std::ostream & operator<<(std::ostream & os, const print_hex<T> & s) {
	
	std::ios_base::fmtflags old = os.flags();
	
	os << "0x" << std::hex << s.value;
	
	os.setf(old, std::ios_base::basefield);
	return os;
}

struct print_hex_string {
	
	const char * data;
	size_t size;
	
	explicit print_hex_string(const char * string, size_t length) : data(string), size(length) { }
	
};

inline std::ostream & operator<<(std::ostream & os, const print_hex_string & s) {
	
	std::ios_base::fmtflags old = os.flags();
	char oldfill = os.fill('0');
	
	os << std::hex;
	for(size_t i = 0; i < s.size; i++) {
		os << std::setw(2) << int(boost::uint8_t(s.data[i]));
	}
	
	os.fill(oldfill);
	os.setf(old, std::ios_base::basefield);
	return os;
}

} // namespace detail

template <class T>
detail::print_hex<T> print_hex(T value) {
	return detail::print_hex<T>(value);
}

inline detail::print_hex_string print_hex(const char * data, size_t size) {
	return detail::print_hex_string(data, size);
}

inline detail::print_hex_string print_hex(const std::string & data) {
	return print_hex(data.c_str(), data.size());
}

const char * const byte_size_units[] = {
	"B",
	"KiB",
	"MiB",
	"GiB",
	"TiB",
	"PiB",
	"EiB",
	"ZiB",
	"YiB",
};

namespace detail {

template <class T>
struct print_bytes {
	
	T value;
	int precision;
	
	explicit print_bytes(T data, int min_digits = 3) : value(data), precision(min_digits) { }
	
	bool operator==(const print_bytes & o) const { return value == o.value; }
	bool operator!=(const print_bytes & o) const { return value != o.value; }
	
};

template <class T>
std::ostream & operator<<(std::ostream & os, const print_bytes<T> & s) {
	
	size_t frac = size_t(1024 * (s.value - T(boost::uint64_t(s.value))));
	boost::uint64_t whole = boost::uint64_t(s.value);
	
	size_t i = 0;
	
	while(whole >= 1024 && i < size_t(boost::size(byte_size_units)) - 1) {
		frac = whole % 1024, whole /= 1024;
		i++;
	}
	
	if((whole >= 100 && s.precision <= 3) || (whole >= 10 && s.precision <= 2) || s.precision <= 1) {
		os << whole;
	} else {
		float num = float(whole) + (float(frac) / 1024.f);
		std::streamsize old_precision = os.precision(s.precision);
		os << num;
		os.precision(old_precision);
	}
	
	return os << ' ' << byte_size_units[i];
}

} // namespace detail

template <class T>
detail::print_bytes<T> print_bytes(T value, int precision = 3) {
	return detail::print_bytes<T>(value, precision);
}

#endif // INNOEXTRACT_UTIL_OUTPUT_HPP
```

## File: `src/util/process.cpp`
```cpp
/*
 * Copyright (C) 2013-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "util/process.hpp"

#include <sstream>
#include <iostream>

#include "configure.hpp"

#if defined(_WIN32)

#include <string.h>
#include <windows.h>

#include <boost/format.hpp>
#include <boost/algorithm/string.hpp>

#elif INNOEXTRACT_HAVE_POSIX_SPAWNP || (INNOEXTRACT_HAVE_FORK && INNOEXTRACT_HAVE_EXECVP)

#if INNOEXTRACT_HAVE_POSIX_SPAWNP
#include <spawn.h>
#if !INNOEXTRACT_HAVE_UNISTD_ENVIRON
extern "C" {
#if defined(__FreeBSD__) && defined(__GNUC__) && __GNUC__ >= 4
/*
 * When combining -flto and -fvisibility=hidden we and up with a hidden
 * 'environ' symbol in crt1.o on FreeBSD 9, which causes the link to fail.
 */
extern char ** environ __attribute__((visibility("default")));
#else
extern char ** environ;
#endif
}
#endif
#endif

#if INNOEXTRACT_HAVE_UNISTD_ENVIRON || (INNOEXTRACT_HAVE_FORK && INNOEXTRACT_HAVE_EXECVP)
#include <unistd.h>
#endif

#if INNOEXTRACT_HAVE_WAITPID
#include <sys/wait.h>
#endif

#else

#include <cstdlib>

#endif

#include "util/encoding.hpp"

namespace util {

#if defined(_WIN32) || !(INNOEXTRACT_HAVE_POSIX_SPAWNP \
                         || (INNOEXTRACT_HAVE_FORK && INNOEXTRACT_HAVE_EXECVP))
static std::string format_command_line(const char * const args[]) {
	
	std::ostringstream oss;
	
	for(size_t i = 0; args[i]; i++) {
		if(i != 0) {
			oss << ' ';
		}
		oss << '"';
		for(const char * arg = args[i]; *arg; arg++) {
			char c = *arg;
			if(c == '\\' || c == '\"' || c == ' ' || c == '\'' || c == '$' || c == '!') {
				oss << '\\';
			}
			oss << c;
		}
		oss << '"';
	}
	
	return oss.str();
}
#endif

int run(const char * const args[]) {
	
	std::cout.flush();
	std::cerr.flush();
	
#if defined(_WIN32)
	
	// Format the command line arguments
	std::string exe;
	wtf8_to_utf16le(args[0], exe);
	exe.push_back('\0');
	std::string cmdline;
	wtf8_to_utf16le(format_command_line(args + 1), exe);
	cmdline.push_back('\0');
	
	STARTUPINFO si;
	memset(&si, 0, sizeof(STARTUPINFO));
	si.cb = sizeof(STARTUPINFO);

	PROCESS_INFORMATION pi;
	memset(&pi, 0, sizeof(PROCESS_INFORMATION));
	
	bool success = (CreateProcessW(reinterpret_cast<LPCWSTR>(exe.c_str()),
	                               reinterpret_cast<LPWSTR>(&cmdline[0]), 0, 0, 0, 0, 0, 0, &si, &pi) != 0);
	
	if(!success) {
		return -1; // Could not start process
	}
	
	int status = int(WaitForSingleObject(pi.hProcess, INFINITE));
	
	CloseHandle(pi.hProcess);
	CloseHandle(pi.hThread);
	
	return status;
	
#elif INNOEXTRACT_HAVE_POSIX_SPAWNP || (INNOEXTRACT_HAVE_FORK && INNOEXTRACT_HAVE_EXECVP)
	
	char ** argv = const_cast<char **>(args);
	
	pid_t pid = -1;
	
	#if INNOEXTRACT_HAVE_POSIX_SPAWNP
	
	// Fast POSIX implementation: posix_spawnp avoids unnecessary vm copies
	
	// Run the executable in a new process
	(void)posix_spawnp(&pid, argv[0], NULL, NULL, argv, environ);
	
	#else
	
	// Compatibility POSIX implementation
	
	// Start a new process
	pid = fork();
	if(pid == 0) {
		
		// Run the executable
		(void)execvp(argv[0], argv);
		
		exit(-1);
	}
	
	#endif
	
	if(pid < 0) {
		return -1;
	}
	
	#if INNOEXTRACT_HAVE_WAITPID
	int status;
	(void)waitpid(pid, &status, 0);
	if(WIFEXITED(status) && WEXITSTATUS(status) < 127) {
		return WEXITSTATUS(status);
	} else if(WIFSIGNALED(status)) {
		return -WTERMSIG(status);
	} else {
		return -1;
	}
	#else
	# warning "Waiting for processes not supported on this system."
	#endif
	
	return 0;
	
#else
	return std::system(format_command_line(args).c_str());
#endif
	
}

} // namespace util
```

## File: `src/util/process.hpp`
```
/*
 * Copyright (C) 2013-2015 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#ifndef INNOEXTRACT_UTIL_PROCESS_HPP
#define INNOEXTRACT_UTIL_PROCESS_HPP

#include <string>

namespace util {

/*!
 * \brief Start a program and wait for it to finish
 *
 * The executable's standard output/error is discarded.
 *
 * \param args program arguments. The first argument is the program name/path and
 *             the last argument must be NULL.
 *
 * \return the programs exit code or a negative value on error.
 */
int run(const char * const args[]);

} // namespace util

#endif // INNOEXTRACT_UTIL_PROCESS_HPP
```

## File: `src/util/storedenum.hpp`
```
/*
 * Copyright (C) 2011-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Utilities for decoding stored enum values into run-time values.
 */
#ifndef INNOEXTRACT_UTIL_STOREDENUM_HPP
#define INNOEXTRACT_UTIL_STOREDENUM_HPP

#include <stddef.h>
#include <vector>
#include <bitset>
#include <ios>

#include <boost/cstdint.hpp>
#include <boost/static_assert.hpp>
#include <boost/typeof/typeof.hpp>
#include <boost/utility/enable_if.hpp>

#include "util/enum.hpp"
#include "util/load.hpp"
#include "util/log.hpp"

// Shared info for enums and flags
#define STORED_MAP_HELPER(MapName, TypeRep, DefaultDecl, ...) \
struct MapName { \
	typedef BOOST_TYPEOF(TypeRep) enum_type; \
	DefaultDecl \
	static const enum_type values[]; \
	static const size_t count; \
}; \
const MapName::enum_type MapName::values[] = { __VA_ARGS__ }; \
const size_t MapName::count = (sizeof(MapName::values)/sizeof(*(MapName::values)))

//! Declare a mapping from integers to enum elements to be used for \ref stored_enum
#define STORED_ENUM_MAP(MapName, Default, /* elements */ ...) \
	STORED_MAP_HELPER(MapName, Default, \
	static const enum_type default_value;, \
	__VA_ARGS__); \
const MapName::enum_type MapName::default_value = Default

//! Declare a mapping from bits to flag enum elements to be used for \ref stored_flags
#define STORED_FLAGS_MAP(MapName, Flag0, /* additional flags */ ...) \
	STORED_MAP_HELPER(MapName, Flag0, , Flag0, __VA_ARGS__)

template <class Mapping>
struct stored_enum {
	
	size_t value;
	
public:
	
	typedef Mapping mapping_type;
	typedef typename Mapping::enum_type enum_type;
	
	static const size_t size = Mapping::count;
	
	explicit stored_enum(std::istream & is) {
		BOOST_STATIC_ASSERT(size <= (1 << 8));
		value = util::load<boost::uint8_t>(is);
	}
	
	enum_type get() {
		
		if(value < size) {
			return Mapping::values[value];
		}
		
		log_warning << "Unexpected " << enum_names<enum_type>::name << " value: " << value;
		
		return Mapping::default_value;
	}
	
};

/*!
 * Load a packed bitfield: 1 byte for every 8 bits
 * The only exception is that 3-byte bitfields are padded to 4 bytes for non-16-bit builds.
 */
template <size_t Bits, size_t PadBits = 32>
class stored_bitfield {
	
	typedef boost::uint8_t base_type;
	
	static const size_t base_size = sizeof(base_type) * 8;
	static const size_t count = (Bits + (base_size - 1)) / base_size; // ceildiv
	
	base_type bits[count];
	
public:
	
	static const size_t size = Bits;
	
	explicit stored_bitfield(std::istream & is) {
		for(size_t i = 0; i < count; i++) {
			bits[i] = util::load<base_type>(is);
		}
		if(count == 3 && PadBits == 32) {
			// 3-byte sets are padded to 4 bytes
			(void)util::load<base_type>(is);
		}
	}
	
	boost::uint64_t lower_bits() const {
		
		BOOST_STATIC_ASSERT(sizeof(boost::uint64_t) % sizeof(base_type) == 0);
		
		boost::uint64_t result = 0;
		
		for(size_t i = 0; i < std::min(sizeof(boost::uint64_t) / sizeof(base_type), size_t(count)); i++) {
			result |= (boost::uint64_t(bits[i]) << (i * base_size));
		}
		
		return result;
	}
	
	operator std::bitset<size>() const {
		
		#define concat(a, b) a##b
		BOOST_STATIC_ASSERT(sizeof(base_type) <= sizeof(concat(unsi, gned) concat(lo, ng)));
		#undef concat
		
		std::bitset<size> result(0);
		for(size_t i = 0; i < count; i++) {
			result |= std::bitset<size>(bits[i]) << (i * base_size);
		}
		return result;
	}
	
};

/*!
 * Load a flag set where the possible flags are known at compile-time.
 * Inno Setup stores flag sets as packed bitfields: 1 byte for every 8 flags
 * The only exception is that 3-byte bitfields are padded to 4 bytes for non-16-bit builds.
 */
template <class Mapping, size_t PadBits = 32>
class stored_flags : private stored_bitfield<Mapping::count, PadBits> {
	
public:
	
	typedef Mapping mapping_type;
	typedef typename Mapping::enum_type enum_type;
	typedef flags<enum_type> flag_type;
	
	explicit stored_flags(std::istream & is)
		: stored_bitfield<Mapping::count, PadBits>(is) { }
	
	flag_type get() {
		
		boost::uint64_t set_bits = this->lower_bits();
		flag_type result = 0;
		
		for(size_t i = 0; i < this->size; i++) {
			if(set_bits & (boost::uint64_t(1) << i)) {
				result |= Mapping::values[i];
				set_bits &= ~(boost::uint64_t(1) << i);
			}
		}
		
		if(set_bits) {
			log_warning << "Unexpected " << enum_names<enum_type>::name << " flags: "
			            << std::hex << set_bits << std::dec;
		}
		
		return result;
	}
	
};

/*!
 * Load a flag set where the possible flags are not known at compile-time.
 * Inno Setup stores flag sets as packed bitfields: 1 byte for every 8 flags
 * The only exception is that 3-byte bitfields are padded to 4 bytes for non-16-bit builds.
 */
template <class Enum>
class stored_flag_reader {
	
public:
	
	typedef Enum enum_type;
	typedef flags<enum_type> flag_type;
	
private:
	
	const size_t pad_bits;
	
	std::istream & stream;
	
	typedef boost::uint8_t stored_type;
	static const size_t stored_bits = sizeof(stored_type) * 8;
	
	size_t pos;
	stored_type buffer;
	
	flag_type result;
	
	size_t bytes;
	
public:
	
	explicit stored_flag_reader(std::istream & is, size_t padding_bits = 32)
		: pad_bits(padding_bits), stream(is), pos(0), buffer(0), result(0), bytes(0) { }
	
	//! Declare the next possible flag.
	void add(enum_type flag) {
		
		if(pos == 0) {
			bytes++;
			buffer = util::load<stored_type>(stream);
		}
		
		if(buffer & (stored_type(1) << pos)) {
			result |= flag;
		}
		
		pos = (pos + 1) % stored_bits;
	}
	
	flag_type finalize() const {
		if(bytes == 3 && pad_bits == 32) {
			// 3-byte sets are padded to 4 bytes
			(void)util::load<stored_type>(stream);
		}
		return result;
	}
	
};

template <class Enum>
class stored_flag_reader<flags<Enum> > : public stored_flag_reader<Enum> {
	
public:
	
	explicit stored_flag_reader(std::istream & is, size_t padding_bits = 32)
		: stored_flag_reader<Enum>(is, padding_bits) { }
	
};

typedef stored_bitfield<256> stored_char_set;

#endif // INNOEXTRACT_UTIL_STOREDENUM_HPP
```

## File: `src/util/test.cpp`
```cpp
/*
 * Copyright (C) 2024 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "util/test.hpp"

#include "configure.hpp"

#if INNOEXTRACT_HAVE_ISATTY
#include <unistd.h>
#endif

namespace {

bool test_verbose = false;
bool test_progress = false;
int test_failed = 0;

} // anonymous namewspace

Testsuite * Testsuite::tests = NULL;

Testsuite::Testsuite(const char * suitename) : name(suitename) {
	next = tests;
	tests = this;
}

int Testsuite::run_all() {
	
	int count = 0;
	for(Testsuite * test = tests; test; test = test->next) {
		count++;
	}
	int len = 2;
	int r = count;
	while(r >= 10) {
		len++;
		r /= 10;
	}
	
	int i = 0;
	for(Testsuite * test = tests; test; test = test->next) {
		i++;
		if(test_verbose || test_progress) {
			std::printf("%*d/%d [%s]", len, i, count, test->name);
			if(test_verbose) {
				std::printf("\n");
			}
		}
		try {
			test->run();
		} catch(...) {
			test_failed++;
			if(test_progress) {
				std::printf("\r\x1b[K");
			}
			std::fprintf(stderr, "%s: EXCEPTION\n", test->name);
		}
	}
	
	if(test_progress) {
		std::printf("\r\x1b[K");
	}
	if(test_failed == 0) {
		std::printf("all %d test suites passed\n", count);
	}
	
	return test_failed > 0 ? 1 : 0;
}

void Testsuite::test(const char * testcase, bool ok) {
	if(!ok) {
		test_failed++;
	}
	if(test_progress) {
		std::printf("\r\x1b[K");
	}
	if(!ok || test_verbose) {
		std::fprintf(ok ? stdout : stderr, "%s.%s: %s\n", name, testcase, ok ? "ok" : "FAILED");
	}
}

int main(int argc, const char * argv[]) {
	
	(void)testdata, (void)testlen;
	
	if((argc > 1 && std::strcmp(argv[1], "--verbose") == 0) || \
	   (argc > 1 && argv[1][0] == '-' && argv[1][1] != '-' && std::strchr(argv[1], 'v')) || \
	   (std::getenv("VERBOSE") && std::strcmp(std::getenv("VERBOSE"), "0") != 0)) {
		test_verbose = true;
	} else {
		#if INNOEXTRACT_HAVE_ISATTY
		test_progress = isatty(1) && isatty(2);
		#endif
		if(test_progress) {
			char * term = std::getenv("TERM");
			if(!term || !std::strcmp(term, "dumb")) {
				test_progress = false; // Terminal does not support escape sequences
			}
		}
	}
	
	return Testsuite::run_all();
}
```

## File: `src/util/test.hpp`
```
/*
 * Copyright (C) 2024 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Test utility functions.
 */
#ifndef INNOEXTRACT_UTIL_TEST_HPP
#define INNOEXTRACT_UTIL_TEST_HPP

#ifdef INNOEXTRACT_BUILD_TESTS

#include <stddef.h>
#include <cstdio>
#include <cstring>
#include <cstdlib>

static const char * testdata = "The dhole (pronounced \"dole\") is also known as the Asiatic wild dog,"
                               " red dog, and whistling dog. It is about the size of a German shepherd but"
                               " looks more like a long-legged fox. This highly elusive and skilled jumper"
                               " is classified with wolves, coyotes, jackals, and foxes in the taxonomic"
                               " family Canidae.";
static const size_t testlen = std::strlen(testdata);

struct Testsuite {
	
	explicit Testsuite(const char * suitename);
	virtual ~Testsuite() { }
	
	static int run_all();
	
	void test(const char * testcase, bool ok);
	
	inline void test_equals(const char * testcase, const void * a, const void * b, size_t count) {
		test(testcase, std::memcmp(a, b, count) == 0);
	}
	
	virtual void run() = 0;
	
private:
	
	static Testsuite * tests;
	Testsuite * next;
	
protected:
	
	const char * name;
	
};

#define INNOEXTRACT_TEST(Name, ...) \
	struct Name ## _test : public Testsuite { \
		Name ## _test() : Testsuite(# Name) { (void)testdata, (void)testlen; } \
		void run(); \
	} test_ ## Name; \
	void Name ## _test::run() { __VA_ARGS__ }

#else

#define INNOEXTRACT_TEST(Name, ...)

#endif // INNOEXTRACT_BUILD_TESTS

#endif // INNOEXTRACT_UTIL_TEST_HPP
```

## File: `src/util/time.cpp`
```cpp
/*
 * Copyright (C) 2013-2019 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#include "util/time.hpp"

#include "configure.hpp"

#if INNOEXTRACT_HAVE_TIMEGM || INNOEXTRACT_HAVE_GMTIME_R || defined(_WIN32)
#include <time.h>
#endif

#include <stdlib.h>

#if defined(_WIN32)
#include <windows.h>
#endif

#if INNOEXTRACT_HAVE_DLSYM
#include <dlfcn.h>
#endif

#if INNOEXTRACT_HAVE_AT_FDCWD
#include <fcntl.h>
#endif

#if INNOEXTRACT_HAVE_UTIMENSAT && INNOEXTRACT_HAVE_AT_FDCWD
#include <sys/stat.h>
#elif !defined(_WIN32) && INNOEXTRACT_HAVE_UTIMES
#include <sys/time.h>
#elif !defined(_WIN32)
#include <boost/filesystem/operations.hpp>
#endif

#include "util/log.hpp"

namespace util {

#if defined(_WIN32)

static const boost::int64_t FiletimeOffset = 0x19DB1DED53E8000ll;

static time from_filetime(FILETIME ft) {
	
	boost::int64_t filetime = boost::int64_t(ft.dwHighDateTime) << 32;
	filetime += boost::int64_t(ft.dwLowDateTime);
	
	filetime -= FiletimeOffset;
	
	return filetime / 10000000;
}

static FILETIME to_filetime(time t, boost::uint32_t nsec = 0) {
	
	boost::int64_t filetime64 = boost::int64_t(t) * 10000000 + boost::int64_t(nsec) / 100 + FiletimeOffset;
	
	FILETIME filetime;
	filetime.dwLowDateTime = DWORD(filetime64);
	filetime.dwHighDateTime = DWORD(filetime64 >> 32);
	return filetime;
}

#endif

static void set_timezone(const char * value) {
	
	const char * variable = "TZ";
	
	#if defined(_WIN32)
	
	SetEnvironmentVariableA(variable, value);
	_tzset();
	
	#else
	
	if(value) {
		setenv(variable, value, 1);
	} else {
		unsetenv(variable);
	}
	tzset();
	
	#endif
	
}

time parse_time(std::tm tm) {
	
	tm.tm_isdst = 0;
	
	#if defined(_WIN32)
	
	// Windows
	
	SYSTEMTIME st;
	st.wYear         = WORD(tm.tm_year + 1900);
	st.wMonth        = WORD(tm.tm_mon + 1);
	st.wDay          = WORD(tm.tm_mday);
	st.wHour         = WORD(tm.tm_hour);
	st.wMinute       = WORD(tm.tm_min);
	st.wSecond       = WORD(tm.tm_sec);
	st.wMilliseconds = 0;
	
	FILETIME ft;
	if(!SystemTimeToFileTime(&st, &ft)) {
		return 0;
	}
	return from_filetime(ft);
	
	#elif INNOEXTRACT_HAVE_TIMEGM
	
	// GNU / BSD extension
	
	return timegm(&tm);
	
	#else
	
	// Standard, but not thread-safe - should be OK for our use though
	
	char * tz = getenv("TZ");
	
	set_timezone("UTC");
	
	time ret = std::mktime(&tm);
	
	set_timezone(tz);
	
	return ret;
	
	#endif
	
}

template <typename Time>
static Time to_time_t(time t, const char * file = "conversion") {
	
	Time ret = Time(t);
	
	if(time(ret) != t) {
		log_warning << "Truncating timestamp " << t << " to " << ret << " for " << file;
	}
	
	return ret;
}

std::tm format_time(time t) {
	
	std::tm ret;
	
	#if defined(_WIN32)
	
	// Windows
	
	FILETIME ft = to_filetime(t);
	
	SYSTEMTIME st;
	if(FileTimeToSystemTime(&ft, &st)) {
		ret.tm_year = int(st.wYear) - 1900;
		ret.tm_mon  = int(st.wMonth) - 1;
		ret.tm_wday = int(st.wDayOfWeek);
		ret.tm_mday = int(st.wDay);
		ret.tm_hour = int(st.wHour);
		ret.tm_min  = int(st.wMinute);
		ret.tm_sec  = int(st.wSecond);
	} else {
		ret.tm_year = ret.tm_mon = ret.tm_mday = -1;
		ret.tm_hour = ret.tm_min = ret.tm_sec = -1;
	}
	ret.tm_isdst = -1;
	
	#elif INNOEXTRACT_HAVE_GMTIME_R
	
	// POSIX.1
	
	time_t tt = to_time_t<time_t>(t);
	gmtime_r(&tt, &ret);
	
	#else
	
	// Standard C++
	
	std::time_t tt = to_time_t<std::time_t>(t);
	std::tm * tmp = std::gmtime(&tt); /* not thread-safe */
	if(tmp) {
		ret = *tmp;
	} else {
		ret.tm_year = ret.tm_mon = ret.tm_mday = -1;
		ret.tm_hour = ret.tm_min = ret.tm_sec = -1;
		ret.tm_isdst = -1;
	}
	
	#endif
	
	return ret;
}

time to_local_time(time t) {
	
	// Format time as UTC ...
	std::tm datetime = format_time(t);
	
	// ... and interpret it as local time
	datetime.tm_isdst = 0;
	#if defined(_WIN32)
	return _mktime64(&datetime);
	#else
	return std::mktime(&datetime);
	#endif
}

void set_local_timezone(std::string timezone) {
	
	/*
	 * The TZ variable interprets the offset as the change from local time 
	 * to UTC while everyone else does the opposite.
	 * We flip the direction so that timezone strings such as GMT+1 work as expected.
	 */
	for(size_t i = 0; i < timezone.length(); i++) {
		if(timezone[i] == '+') {
			timezone[i] = '-';
		} else if(timezone[i] == '-') {
			timezone[i] = '+';
		}
	}
	
	set_timezone(timezone.c_str());
}

#if defined(_WIN32)

static HANDLE open_file(LPCSTR name) {
	return CreateFileA(name, GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, NULL);
}

static HANDLE open_file(LPCWSTR name) {
	return CreateFileW(name, GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, NULL);
}

#endif

#if INNOEXTRACT_HAVE_DYNAMIC_UTIMENSAT
extern "C" typedef int (*utimensat_proc)
	(int fd, const char *path, const struct timespec times[2], int flag);
#endif

bool set_file_time(const boost::filesystem::path & path, time sec, boost::uint32_t nsec) {
	
	#if (INNOEXTRACT_HAVE_DYNAMIC_UTIMENSAT || INNOEXTRACT_HAVE_UTIMENSAT) \
	    && INNOEXTRACT_HAVE_AT_FDCWD
	
	// nanosecond precision, for Linux and POSIX.1-2008+ systems
	
	struct timespec timens[2];
	timens[0].tv_sec = to_time_t<time_t>(sec, path.string().c_str());
	timens[0].tv_nsec = boost::int32_t(nsec);
	timens[1] = timens[0];
	
	#endif
	
	#if INNOEXTRACT_HAVE_DYNAMIC_UTIMENSAT && INNOEXTRACT_HAVE_AT_FDCWD
	
	static utimensat_proc utimensat_func = reinterpret_cast<utimensat_proc>(dlsym(RTLD_DEFAULT, "utimensat"));
	if(utimensat_func) {
		return (utimensat_func(AT_FDCWD, path.string().c_str(), timens, 0) == 0);
	}
	
	#endif
	
	#if INNOEXTRACT_HAVE_UTIMENSAT && INNOEXTRACT_HAVE_AT_FDCWD
	
	return (utimensat(AT_FDCWD, path.string().c_str(), timens, 0) == 0);
	
	#elif defined(_WIN32)
	
	// 100-nanosecond precision, for Windows
	
	// Prevent unused function warnings
	(void)static_cast<HANDLE(*)(LPCSTR)>(open_file);
	(void)static_cast<HANDLE(*)(LPCWSTR)>(open_file);
	
	HANDLE handle = open_file(path.c_str());
	if(handle == INVALID_HANDLE_VALUE) {
		return false;
	}
	
	FILETIME filetime = to_filetime(sec, nsec);
	
	bool ret = (SetFileTime(handle, &filetime, &filetime, &filetime) != 0);
	CloseHandle(handle);
	
	return ret;
	
	#elif INNOEXTRACT_HAVE_UTIMES
	
	// microsecond precision, for older POSIX systems (4.3BSD, POSIX.1-2001)
	
	struct timeval times[2];
	times[0].tv_sec = to_time_t<time_t>(sec, path.string().c_str());
	times[0].tv_usec = boost::int32_t(nsec / 1000);
	times[1] = times[0];
	
	return (utimes(path.string().c_str(), times) == 0);
	
	#else
	
	// fallback with second precision or worse
	
	try {
		(void)nsec; // sub-second precision not supported by Boost
		std::time_t tt = to_time_t<std::time_t>(sec, path.string().c_str());
		boost::filesystem::last_write_time(path, tt);
		return true;
	} catch(...) {
		return false;
	}
	
	#endif
	
}

} // namespace util
```

## File: `src/util/time.hpp`
```
/*
 * Copyright (C) 2013-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Time parsing, formatting, onversion and filetime manipulation functions.
 */
#ifndef INNOEXTRACT_UTIL_TIME_HPP
#define INNOEXTRACT_UTIL_TIME_HPP

#include <ctime>
#include <string>

#include <boost/cstdint.hpp>
#include <boost/filesystem/path.hpp>

namespace util {

typedef boost::int64_t time;

/*!
 * Convert UTC clock time to a timestamp
 *
 * \note This function may not be thread-safe on all operating systems.
 */
time parse_time(std::tm tm);

/*!
 * Convert a timestamp to UTC clock time
 *
 * \note This function may not be thread-safe on all operating systems.
 */
std::tm format_time(time t);

/*!
 * Convert a timestamp to local time
 *
 * \note This function may not be thread-safe on all operating systems.
 */
time to_local_time(time t);

/*!
 * Set the local timezone used by to_local_time
 *
 * \note This function is not thread-safe.
 */
void set_local_timezone(std::string timezone);

/*!
 * Set a file's access, creation and modification times.
 *
 * \note Not all operating systems support file creation times.
 *
 * \param path The file to the file to set the times for.
 *             This file will <b>not</b> be created if it doesn't exist already.
 * \param sec  File time to set (in seconds).
 * \param nsec Sub-second component of the file time to set (in nanoseconds).
 *
 * \note The actual file time precision depends on the operating system and filesystem.
 *       If the available file time precision is too low to represent the given timestamp,
 *       it will be silently truncated to the available precision.
 *
 * \return \c true if the file time was changed, \c false otherwise.
 */
bool set_file_time(const boost::filesystem::path & path, time sec, boost::uint32_t nsec);

} // namespace util

#endif // INNOEXTRACT_UTIL_TIME_HPP
```

## File: `src/util/types.hpp`
```
/*
 * Copyright (C) 2011-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Utility functions for dealing with types.
 */
#ifndef INNOEXTRACT_UTIL_TYPES_HPP
#define INNOEXTRACT_UTIL_TYPES_HPP

#include <limits>

#include <boost/version.hpp>
#include <boost/integer/static_min_max.hpp>
#include <boost/integer.hpp>

namespace util {

#if BOOST_VERSION < 104200

template <int Bits>
struct uint_t { };
template <>
struct uint_t<8>  : public boost::uint_t<8>  { typedef boost::uint8_t exact; };
template <>
struct uint_t<16> : public boost::uint_t<16> { typedef boost::uint16_t exact; };
template <>
struct uint_t<32> : public boost::uint_t<32> { typedef boost::uint32_t exact; };
template <>
struct uint_t<64>                            { typedef boost::uint64_t exact; };

template <int Bits>
struct int_t { };
template <>
struct int_t<8>  : public boost::int_t<8>  { typedef boost::int8_t exact; };
template <>
struct int_t<16> : public boost::int_t<16> { typedef boost::int16_t exact; };
template <>
struct int_t<32> : public boost::int_t<32> { typedef boost::int32_t exact; };
template <>
struct int_t<64>                           { typedef boost::int64_t exact; };

#else

using boost::uint_t;
using boost::int_t;

#endif

/*!
 * Get an with a specific bit size and signedness,
 * but with no more bits than the original.
 */
template <class Base, size_t Bits,
          bool Signed = std::numeric_limits<Base>::is_signed>
struct compatible_integer {
	typedef void type;
};
template <class Base, size_t Bits>
struct compatible_integer<Base, Bits, false> {
	typedef typename uint_t<
		boost::static_unsigned_min<Bits, sizeof(Base) * 8>::value
	>::exact type;
};
template <class Base, size_t Bits>
struct compatible_integer<Base, Bits, true> {
	typedef typename int_t<
		boost::static_unsigned_min<Bits, sizeof(Base) * 8>::value
	>::exact type;
};

//! CRTP helper class to hide the ugly static casts needed to get to the derived class.
template <class Impl>
class static_polymorphic {
	
protected:
	
	typedef Impl impl_type;
	
	impl_type & impl() { return *static_cast<impl_type *>(this); }
	
	const impl_type & impl() const { return *static_cast<const impl_type *>(this); }
	
};

} // namespace util

#endif // INNOEXTRACT_UTIL_TYPES_HPP
```

## File: `src/util/unique_ptr.hpp`
```
/*
 * Copyright (C) 2013-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Wrapper to select std::unique_ptr if available, std::auto_ptr otherwise.
 */
#ifndef INNOEXTRACT_UTIL_UNIQUE_PTR_HPP
#define INNOEXTRACT_UTIL_UNIQUE_PTR_HPP

#include <memory>

#include "configure.hpp"

namespace util {

//! Get a std::unique_ptr or std::auto_ptr for the given type.
template <typename T>
struct unique_ptr {
#if INNOEXTRACT_HAVE_STD_UNIQUE_PTR
	typedef std::unique_ptr<T> type;
#else
	typedef std::auto_ptr<T> type;
#endif
};

} // namespace util

#endif // INNOEXTRACT_UTIL_UNIQUE_PTR_HPP
```

## File: `src/util/windows.cpp`
```cpp
/*
 * Copyright (C) 2013-2020 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#ifndef _WIN32
#define _WIN32
#endif
#include "util/windows.hpp"

#include <stddef.h>

#include <algorithm>
#include <cstdlib>
#include <clocale>
#include <iostream>
#include <locale>
#include <sstream>
#include <stdexcept>
#include <vector>

#include <wchar.h>
#include <windows.h>
#include <shellapi.h>

#include <boost/filesystem/path.hpp>
#include <boost/iostreams/stream_buffer.hpp>

#include "configure.hpp"

#if INNOEXTRACT_HAVE_STD_CODECVT_UTF8_UTF16
// C++11
#include <codecvt>
namespace { typedef std::codecvt_utf8_utf16<wchar_t> utf8_codecvt; }
#else
// Using private Boost stuff - bad, but meh.
#include <boost/filesystem/detail/utf8_codecvt_facet.hpp>
namespace { typedef boost::filesystem::detail::utf8_codecvt_facet utf8_codecvt; }
#endif

#include "util/ansi.hpp"
#include "util/encoding.hpp"

// Disable telemetry added in Visual Studio 2015
#if defined(_MSC_VER) && _MSC_VER >= 1900
extern "C" {
	void _cdecl __vcrt_initialize_telemetry_provider() { }
	void _cdecl __telemetry_main_invoke_trigger() { }
	void _cdecl __telemetry_main_return_trigger() { }
	void _cdecl __vcrt_uninitialize_telemetry_provider() { }
};
#endif

namespace util {

class windows_console_sink : public util::ansi_console_parser<windows_console_sink> {
	
	friend class util::ansi_console_parser<windows_console_sink>;
	
	const HANDLE handle;
	
	//! Buffer for charset conversions
	std::string in_buffer;
	std::string out_buffer;
	
	//! Initial console display attributes
	WORD initial_attributes;
	//! Default console display attributes
	WORD default_attributes;
	//! Current console display attributes
	WORD attributes;
	
	bool deferred_clear;
	SHORT clear_line;
	WORD clear_attributes;
	
	void clear_deferred(const CONSOLE_SCREEN_BUFFER_INFO & info, SHORT offset = 0) {
		COORD pos = { offset, clear_line };
		DWORD count = DWORD(info.dwSize.X - offset);
		DWORD ignored;
		FillConsoleOutputCharacterW(handle, L' ', count, pos, &ignored);
		FillConsoleOutputAttribute(handle, clear_attributes, count, pos, &ignored);
		deferred_clear = false;
	}
	
	void erase_in_line(const char * codes, const char * end) {
		
		bool left = false, right = false;
		bool deferred = false;
		
		do {
			unsigned code = read_code(codes, end);
			switch(code) {
				case 0:              right = true; break;
				case 1: left = true;               break;
				case 2: left = true, right = true; break;
				case 3: deferred = true;           break;
				default: {
					#ifdef DEBUG
					std::ostringstream oss;
					oss << "(unsupported EL code: " << code << ")";
					error(oss.str());
					#endif
				}
			}
		} while(codes);
		
		CONSOLE_SCREEN_BUFFER_INFO info;
		if(!GetConsoleScreenBufferInfo(handle, &info)) {
			return;
		}
		
		if(deferred_clear && (!deferred
		   || clear_line != info.dwCursorPosition.Y || clear_attributes != attributes)) {
			clear_deferred(info);
		}
		
		if(deferred) {
			deferred_clear = true;
			clear_line = info.dwCursorPosition.Y;
			clear_attributes = attributes;
			return;
		}
		
		SHORT cbegin = left ? SHORT(0) : info.dwCursorPosition.X;
		SHORT cend = right ? info.dwSize.X : info.dwCursorPosition.X;
		
		COORD pos = { cbegin, info.dwCursorPosition.Y };
		DWORD count = DWORD(cend - cbegin);
		
		DWORD ignored;
		FillConsoleOutputCharacterW(handle, L' ', count, pos, &ignored);
		FillConsoleOutputAttribute(handle, attributes, count, pos, &ignored);
	}
	
	void set_attributes(WORD attr) {
		if(attributes != attr) {
			attributes = attr;
			SetConsoleTextAttribute(handle, attributes);
		}
	}
	
	WORD get_attributes() {
		
		CONSOLE_SCREEN_BUFFER_INFO info;
		if(!GetConsoleScreenBufferInfo(handle, &info)) {
			return FOREGROUND_BLUE | FOREGROUND_GREEN | FOREGROUND_RED | FOREGROUND_INTENSITY;
		}
		
		return info.wAttributes;
	}
	
	WORD get_default_attributes() {
		
		int a = initial_attributes;
		
		// Unset onderscore and negative states
		a &= ~(COMMON_LVB_REVERSE_VIDEO | COMMON_LVB_UNDERSCORE);
		
		// Set dim white text, otherwise the default color might clash with other colors
		a |= FOREGROUND_BLUE | FOREGROUND_GREEN | FOREGROUND_RED;
		a &= ~FOREGROUND_INTENSITY;
		
		// Try to preserve the existing background color if it is dark enough
		const WORD bg = BACKGROUND_BLUE | BACKGROUND_GREEN | BACKGROUND_RED;
		a &= ~BACKGROUND_INTENSITY;
		if((a & bg) == bg) {
			a &= ~bg; // Prevent white text on white background
		}
		
		return WORD(a);
	}
	
	void select_graphic_rendition(const char * codes, const char * end) {
		
		const WORD fg = FOREGROUND_BLUE | FOREGROUND_GREEN | FOREGROUND_RED;
		const WORD bg = BACKGROUND_BLUE | BACKGROUND_GREEN | BACKGROUND_RED;
		
		int a = attributes;
		
		do {
			unsigned code = read_code(codes, end);
			switch(code) {
				case 0: a = default_attributes; break;
				case 1: a |= FOREGROUND_INTENSITY; break;
				case 4: a |= COMMON_LVB_UNDERSCORE; break;
				case 7: a |= COMMON_LVB_REVERSE_VIDEO; break;
				case 22: a &= ~FOREGROUND_INTENSITY; break;
				case 24: a &= ~COMMON_LVB_UNDERSCORE; break;
				case 27: a &= ~COMMON_LVB_REVERSE_VIDEO; break;
				case 30: a &= ~fg; break;
				case 31: a &= ~fg, a |= FOREGROUND_RED; break;
				case 32: a &= ~fg, a |= FOREGROUND_GREEN; break;
				case 33: a &= ~fg, a |= FOREGROUND_RED | FOREGROUND_GREEN; break;
				case 34: a &= ~fg, a |= FOREGROUND_BLUE; break;
				case 35: a &= ~fg, a |= FOREGROUND_RED | FOREGROUND_BLUE; break;
				case 36: a &= ~fg, a |= FOREGROUND_BLUE | FOREGROUND_GREEN; break;
				case 37: a &= ~fg, a |= FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE; break;
				case 39: a &= ~fg, a |= (default_attributes & fg); break;
				case 40: a &= ~bg; break;
				case 41: a &= ~bg, a |= BACKGROUND_RED; break;
				case 42: a &= ~bg, a |= BACKGROUND_GREEN; break;
				case 43: a &= ~bg, a |= BACKGROUND_RED | BACKGROUND_GREEN; break;
				case 44: a &= ~bg, a |= BACKGROUND_BLUE; break;
				case 45: a &= ~bg, a |= BACKGROUND_RED | BACKGROUND_BLUE; break;
				case 46: a &= ~bg, a |= BACKGROUND_BLUE | BACKGROUND_GREEN; break;
				case 47: a &= ~bg, a |= BACKGROUND_RED | BACKGROUND_GREEN | BACKGROUND_BLUE; break;
				case 49: a &= ~bg, a |= (default_attributes & bg); break;
				default: {
					#ifdef DEBUG
					std::ostringstream oss;
					oss << "(unsupported SGR code: " << code << ")";
					error(oss.str());
					#endif
				}
			}
		} while(codes);
		
		set_attributes(WORD(a));
	}
	
	void handle_command(CommandType type, const char * codes, const char * end) {
		if(!in_buffer.empty()) {
			output_text(in_buffer.c_str(), in_buffer.c_str() + in_buffer.size());
			in_buffer.clear();
		}
		switch(type) {
			case EL:  erase_in_line(codes, end); break;
			case SGR: select_graphic_rendition(codes, end); break;
			default: {
				#ifdef DEBUG
				std::ostringstream oss;
				oss << "(unknown command type: " << char(type) << ")";
				error(oss.str());
				#endif
			}
		}
	}
	
	void handle_deferred_clear(LPCWSTR & begin, LPCWSTR end) {
		
		CONSOLE_SCREEN_BUFFER_INFO info;
		if(!GetConsoleScreenBufferInfo(handle, &info)) {
			deferred_clear = false;
			return;
		}
		
		while(begin != end) {
			
			if(*begin == L'\r') {
				// End deferred clear mode
				deferred_clear = false;
				break;
			}
			
			LPCWSTR cr = std::find(begin, end, L'\r');
			LPCWSTR ln = std::find(begin, cr, L'\n');
			
			// Insert an empty line before the "cleared" line
			if(clear_line == info.dwCursorPosition.Y) {
				
				if(info.dwCursorPosition.Y == info.dwSize.Y - 1) {
					// Cursor is at the end of the buffer
					// Move buffer contents up one line except for the last line
					SMALL_RECT source = { 0, 1, SHORT(info.dwSize.X), SHORT(info.dwSize.Y - 2) };
					COORD dest = { 0, 0 };
					CHAR_INFO fill;
					fill.Char.UnicodeChar = L' ';
					fill.Attributes = clear_attributes;
					ScrollConsoleScreenBufferW(handle, &source, NULL, dest, &fill);
					COORD cursor = { 0, SHORT(info.dwCursorPosition.Y - 1) };
					SetConsoleCursorPosition(handle, cursor);
				} else {
					// Move cleared line down one line
					SMALL_RECT source = { 0, SHORT(info.dwCursorPosition.Y),
					                      SHORT(info.dwSize.X), SHORT(info.dwCursorPosition.Y + 1) };
					SMALL_RECT clip = { 0, SHORT(info.dwCursorPosition.Y + 1),
					                    SHORT(info.dwSize.X), SHORT(info.dwCursorPosition.Y + 2) };
					COORD dest = { 0, SHORT(info.dwCursorPosition.Y + 1) };
					CHAR_INFO fill;
					fill.Char.UnicodeChar = L' ';
					fill.Attributes = clear_attributes;
					ScrollConsoleScreenBufferW(handle, &source, &clip, dest, &fill);
					clear_line = SHORT(info.dwCursorPosition.Y + 1);
					if(info.dwCursorPosition.Y == info.srWindow.Bottom) {
						// Cursor is at the end of the window
						// Scroll up before overwriting the cleared line
						SMALL_RECT window = { 0, 1, 0, 1 };
						SetConsoleWindowInfo(handle, FALSE, &window);
					}
					COORD pos = { 0, info.dwCursorPosition.Y };
					DWORD count = DWORD(info.dwSize.X);
					DWORD ignored;
					FillConsoleOutputCharacterW(handle, L' ', count, pos, &ignored);
					FillConsoleOutputAttribute(handle, clear_attributes, count, pos, &ignored);
				}
				
				info.dwCursorPosition.X = 0;
				
			}
			
			// Write at most one line!
			DWORD len = DWORD(std::min(ln + 1 - begin, cr - begin));
			len = std::min(len, DWORD(info.dwSize.X - info.dwCursorPosition.X));
			
			DWORD count;
			WriteConsoleW(handle, begin, len, &count, NULL);
			begin += len;
			
			if(!GetConsoleScreenBufferInfo(handle, &info)) {
				deferred_clear = false;
				break;
			}
			
			if(info.dwCursorPosition.Y > clear_line) {
				// Line completely overwritten with text
				deferred_clear = false;
				break;
			} else if(info.dwCursorPosition.Y == clear_line && info.dwCursorPosition.X > 0) {
				// Line partially overwritten with text - clear the rest
				clear_deferred(info, info.dwCursorPosition.X);
				break;
			}
			
		}
		
	}
	
	void output_text(const char * begin, const char * end) {
		
		wtf8_to_utf16le(begin, end, out_buffer);
		
		LPCWSTR obegin = reinterpret_cast<LPCWSTR>(out_buffer.c_str());
		LPCWSTR oend = obegin + out_buffer.size() / 2;
		
		if(deferred_clear) {
			handle_deferred_clear(obegin, oend);
		}
		
		DWORD count;
		WriteConsoleW(handle, obegin, DWORD(oend - obegin), &count, NULL);
		
	}
	
	void handle_text(const char * s, size_t n) {
		
		if(!in_buffer.empty()) {
			in_buffer.append(s, n);
			s = in_buffer.c_str();
			n = in_buffer.size();
		}
		
		const char * end = s + n;
		
		if(s == end) {
			return;
		}
		
		const char * e = wtf8_find_end(s, end);
		
		output_text(s, e);
		
		in_buffer.assign(e, end);
		
	}
	
public:
	
	explicit windows_console_sink(HANDLE console_handle)
		: handle(console_handle)
		, initial_attributes(get_attributes())
		, default_attributes(get_default_attributes())
		, attributes(initial_attributes)
		, deferred_clear(false)
		, clear_line(0)
		, clear_attributes(0)
	{ }
	
	~windows_console_sink() {
		if(!in_buffer.empty()) {
			output_text(in_buffer.c_str(), in_buffer.c_str() + in_buffer.size());
		}
		if(deferred_clear) {
			CONSOLE_SCREEN_BUFFER_INFO info;
			if(GetConsoleScreenBufferInfo(handle, &info)) {
				clear_deferred(info);
			}
		}
		set_attributes(initial_attributes);
	}
	
};

typedef boost::iostreams::stream_buffer<windows_console_sink> console_buffer;
struct console_buffer_info {
	HANDLE handle;
	console_buffer * buf;
	std::streambuf * orig_buf;
};
static console_buffer_info stdout_info = { NULL, NULL, NULL };
static console_buffer_info stderr_info = { NULL, NULL, NULL };

static void cleanup_console(std::ostream & os, console_buffer_info & info) {
	if(info.buf) {
		os.flush();
		os.rdbuf(info.orig_buf);
		delete info.buf;
		info.buf = NULL, info.handle = NULL;
	}
}

static void cleanup_console() {
	cleanup_console(std::cout, stdout_info);
	cleanup_console(std::cerr, stderr_info);
}

static BOOL WINAPI cleanup_console_handler(DWORD type) {
	(void)type;
	cleanup_console();
	return FALSE;
}

static bool is_console(HANDLE handle) {
	DWORD mode;
	return GetConsoleMode(handle, &mode) != 0;
}

static void init_console(std::ostream & os, console_buffer_info & info, DWORD n) {
	info.handle = GetStdHandle(n);
	if(is_console(info.handle)) {
		info.buf = new console_buffer(info.handle);
		info.orig_buf = os.rdbuf(info.buf);
	} else {
		info.handle = NULL;
	}
}

static void init_console() {
	init_console(std::cout, stdout_info, STD_OUTPUT_HANDLE);
	init_console(std::cerr, stderr_info, STD_ERROR_HANDLE);
	if(stdout_info.buf || stderr_info.buf) {
		std::atexit(cleanup_console);
		SetConsoleCtrlHandler(cleanup_console_handler, TRUE);
	}
}

struct console_wrapper {
	
	console_wrapper() {
		init_console();
	}
	
	~console_wrapper() {
		cleanup_console();
	}
	
};

int isatty(int fd) {
	switch(fd) {
		case 0: return is_console(GetStdHandle(STD_INPUT_HANDLE)) ? 1 : 0;
		case 1: return (stdout_info.buf != NULL) ? 1 : 0;
		case 2: return (stderr_info.buf != NULL) ? 1 : 0;
		default: return 0;
	}
}

int console_width() {
	
	if(!stdout_info.handle) {
		return 0;
	}
	
	CONSOLE_SCREEN_BUFFER_INFO info;
	if(!GetConsoleScreenBufferInfo(stdout_info.handle, &info)) {
		return 0;
	}
	
	return int(info.dwSize.X);
}

} // namespace util

// We really want main here, not utf8_main.
#undef main
int main() {
	
	// We use UTF-8 for everything internally, as almost all modern operating systems
	// have standardized on that. However, as usual, Windows has to do its own thing
	// and only supports Unicode input/output via UCS-2^H^H^H^H^HUTF-16.
	
	std::setlocale(LC_ALL, "");
	
	// Emulate wmain() as it's nonstandard and not supported by MinGW
	// Convert the UTF-16 command-line parameters to UTF-8
	int argc = 0;
	char ** argv = NULL;
	std::vector<std::string> args;
	{
		wchar_t ** wargv = CommandLineToArgvW(GetCommandLineW(), &argc);
		args.resize(size_t(argc));
		argv = new char *[argc + 1];
		argv[argc] = NULL;
		for(size_t i = 0; i < args.size(); i++) {
			util::utf16le_to_wtf8(std::string(reinterpret_cast<char *>(wargv[i]), wcslen(wargv[i]) * 2), args[i]);
			argv[i] = &args[i][0];
		}
		LocalFree(wargv);
	}
	
	// Tell boost::filesystem to interpret our path strings as UTF-8
	boost::filesystem::path::imbue(std::locale(std::locale(), new utf8_codecvt()));
	
	// Enable UTF-8 output and ANSI escape sequences
	util::console_wrapper wrapped;
	
	return utf8_main(argc, argv);
}
```

## File: `src/util/windows.hpp`
```
/*
 * Copyright (C) 2013-2014 Daniel Scharrer
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the author(s) be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

/*!
 * \file
 *
 * Compatibility wrapper to work around deficiencies in Microsoft® Windows™.
 * Mostly deals with converting between UTF-8 and UTF-16 input/output.
 * More precisely:
 *  - Converts wide char command-line arguments to UTF-8 and calls utf8_main().
 *  - Sets an UTF-8 locale for boost::filesystem::path.
 *    This makes everything in boost::filesystem UTF-8 aware, except for {i,o,}fstream.
 *    For those, there are UTF-8 aware implementations in util/fstream.hpp
 *  - Converts UTF-8 to UTF-16 in std::cout and std::cerr if attached to a console
 *  - Interprets ANSI escape sequences in std::cout and std::cerr if attached to a console
 *  - Provides a Windows implementation of \c isatty()
 */
#ifndef INNOEXTRACT_UTIL_WINDOWS_HPP
#define INNOEXTRACT_UTIL_WINDOWS_HPP

#if defined(_WIN32)

//! Program entry point that will always receive UTF-8 encoded arguments
int utf8_main(int argc, char * argv[]);

//! We define our own wrapper main(), so rename the real one
#define main utf8_main

namespace util {

//! isatty() replacement (only works for fd 0, 1 and 2)
int isatty(int fd);

//! Determine the buffer width of the current console - replacement for ioctl(TIOCGWINSZ)
int console_width();

} // namespace util

using util::isatty;

#endif // defined(_WIN32)

#endif // INNOEXTRACT_UTIL_WINDOWS_HPP
```

