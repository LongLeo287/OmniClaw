---
id: innoextract
type: knowledge
owner: OA_Triage
---
# innoextract
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md

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

### File: CMakeLists.txt
```txt
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

install(TARG
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md

Contributions of all kinds are welcome as [GitHub pull requests](https://github.com/dscharrer/innoextract/pulls) or as patches mailed to daniel@constexpr.org.

If you are planning to implement a larger feature and intend to get it merged, please contact me **first** at daniel@constexpr.org or on the [GitHub issue tracker](https://github.com/dscharrer/innoextract/issues) to discuss the planned changes in order to avoid duplicating work or having to re-do the changes in a way that fits with the project.

There is no official code style guide, but please try to match the style of the existing code and git commit messages.

All contributions must be licensed under the zlib license detailed in the LICENSE file.

```

### File: src\cli\debug.cpp
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
                 
... [TRUNCATED]
```

### File: src\cli\extract.cpp
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
		require_
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
