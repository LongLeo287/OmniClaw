---
id: neko
type: knowledge
owner: OA_Triage
---
# neko
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
![NekoVM](https://cloud.githubusercontent.com/assets/576184/14234981/10528a0e-f9f1-11e5-8922-894569b2feea.png)

[![CI](https://github.com/HaxeFoundation/neko/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/HaxeFoundation/neko/actions/workflows/main.yml)

# Deprecated as of 2021-09-09

**Neko is not actively maintained anymore.**

We keep it compatible with existing Haxe standard library and Haxe language features. But don't expect any new features in Neko itself and don't expect implementation of any new Haxe standard library API.

# Neko Virtual Machine

See https://nekovm.org/

## Snapshot Builds

Compiled binaries can be found in the "artifacts" section in the summary of each [Github Actions build](https://github.com/HaxeFoundation/neko/actions?query=branch%3Amaster+is%3Asuccess).

For macOS, Neko snapshot of the latest master branch can be built using [homebrew](https://brew.sh/) in a single command: `brew install neko --HEAD`. It will install required dependencies, build, and install Neko to the system. The binaries can be found at `brew --prefix neko`. Use `brew reinstall neko --HEAD` to upgrade in the future.

## Build instruction

Neko can be built using CMake (version 3.x is recommended) and one of the C compilers listed as follows:

 * Windows: Visual Studio 2010 / 2013 / 2015 / 2017
 * Mac: XCode (with its "Command line tools")
 * Linux: gcc (can be obtained by installing the "build-essential" Debian/Ubuntu package)

Neko needs to link with various third-party libraries, which are summarized as follows:

| library / tool                          | OS          | Debian/Ubuntu package                                     |
|-----------------------------------------|-------------|-----------------------------------------------------------|
| Boehm GC                                | all         | libgc-dev                                                 |
| OpenSSL                                 | all         | libssl-dev                                                |
| pcre2                                   | all         | libpcre2-dev                                              |
| zlib                                    | all         | zlib1g-dev                                                |
| Apache 2.2 / 2.4, with apr and apr-util | all         | apache2-dev                                               |
| MariaDB / MySQL (Connector/C)           | all         | libmariadb-client-lgpl-dev-compat (or libmysqlclient-dev) |
| SQLite                                  | all         | libsqlite3-dev                                            |
| mbed TLS                                | all         | libmbedtls-dev                                            |
| GTK+3                                   | Linux       | libgtk-3-dev                                              |

On Windows, CMake will automatically download and build the libraries in the build folder during the build process. However, you need to install [Perl](https://www.activestate.com/activeperl) manually because OpenSSL needs it for configuration. On Mac/Linux, you should install the libraries manually to your system before building Neko, or use the `STATIC_DEPS` CMake option, which will be explained in [CMake options](#cmake-options).

### Building on Mac/Linux

```shell
# make a build directory, and change to it
mkdir build
cd build

# run cmake
cmake ..

# let's build, the outputs can be located in the "bin" directory
make

# install it if you want
# default installation prefix is /usr/local
make install
```

### Building on Windows

Below is the instructions of building Neko in a Visual Studio command prompt.
You may use the CMake GUI and Visual Studio to build it instead.

```shell
# make a build directory, and change to it
mkdir build
cd build

# run cmake specifying the visual studio version you need
# Visual Studio 12 2013, Visual Studio 14 2015, Visual Studio 15 2017
# you can additionally specify platform via -A switch (x86, x64)
cmake -G "Visual Studio 12 2013" ..

# let's build, the outputs can be located in the "bin" directory
msbuild ALL_BUILD.vcxproj /p:Configuration=Release

# install it if you want
# default installation location is C:\HaxeToolkit\neko
msbuild INSTALL.vcxproj /p:Configuration=Release
```

### CMake options

A number of options can be used to customize the build. They can be specified in the CMake GUI, or passed to `cmake` in command line as follows:

```shell
cmake "-Doption=value" ..
```

#### NDLLs

Settings that allow to exclude libraries and their dependencies from the build; available on all platforms. By default all are `ON`:

- `WITH_REGEXP` - Build Perl-compatible regex support
- `WITH_UI` - Build GTK-3 UI support
- `WITH_SSL` - Build SSL support
- `WITH_MYSQL` - Build MySQL support
- `WITH_SQLITE` - Build Sqlite support
- `WITH_APACHE` - Build Apache modules

#### `STATIC_DEPS`

Default value: `all` for Windows, `none` otherwise

It defines the dependencies that should be linked statically. Can be `all`, `none`, or a list of library names (e.g. `BoehmGC;Zlib;OpenSSL;MariaDBConnector;pcre2;SQLite3;APR;APRutil;Apache;MbedTLS`).

CMake will automatically download and build the specified dependencies into the build folder. If a library is not present in this list, it should be installed manually, and it will be linked dynamically.

All third-party libraries, except GTK+3 (Linux) and BoehmGC on Windows, can be linked statically. We do not support statically linking GTK+3 due to the difficulty of building it and its own dependencies. Additionally, we do not support statically linking the BoehmGC library on Windows systems.

#### `RELOCATABLE`

Available on Mac/Linux. Default value: `ON`

Set RPATH to `$ORIGIN` (Linux) / `@executable_path` (Mac). It allows the resulting Neko VM executable to locate libraries (e.g. "libneko" and ndll files) in its local directory, such that the libraries need not be installed to "/usr/lib" or "/usr/local/lib".

#### `NEKO_JIT_DISABLE`

Default `OFF`.

Disable Neko JIT. By default, Neko JIT will be enabled for platforms it supports. Setting this to `ON` disable JIT for all platforms.

#### `NEKO_JIT_DEBUG`

Default `OFF`.

Debug Neko JIT.

#### `RUN_LDCONFIG`

Available on Linux. Default value: `ON`

Whether to run `ldconfig` automatically after `make install`. It is for refreshing the shared library cache such that "libneko" can be located correctly by the Neko VM.

```

### File: CMakeLists.txt
```txt
cmake_minimum_required(VERSION 3.10.2)

if (${CMAKE_VERSION} VERSION_GREATER_EQUAL 3.24)
	cmake_policy(VERSION 3.24)
elseif (${CMAKE_VERSION} VERSION_GREATER_EQUAL 3.19)
	cmake_policy(VERSION 3.19)
endif()

project(Neko C)

include(GNUInstallDirs)
include(CheckCCompilerFlag)
include(CheckIncludeFile)
include(TestBigEndian)

set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake ${CMAKE_MODULE_PATH})

if (${CMAKE_SYSTEM_NAME} STREQUAL "FreeBSD")
  # FreeBSD puts all thirdparty libraries in /usr/local
  link_directories(/usr/local/lib)
endif()

# put output in "bin"

set(OUTPUT_DIR ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${OUTPUT_DIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${OUTPUT_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${OUTPUT_DIR})

# avoid the extra "Debug", "Release" directories
# https://stackoverflow.com/questions/7747857/in-cmake-how-do-i-work-around-the-debug-and-release-directories-visual-studio-2
foreach( OUTPUTCONFIG ${CMAKE_CONFIGURATION_TYPES} )
	string( TOUPPER ${OUTPUTCONFIG} OUTPUTCONFIG )
	set( CMAKE_RUNTIME_OUTPUT_DIRECTORY_${OUTPUTCONFIG} ${OUTPUT_DIR} )
	set( CMAKE_LIBRARY_OUTPUT_DIRECTORY_${OUTPUTCONFIG} ${OUTPUT_DIR} )
	set( CMAKE_ARCHIVE_OUTPUT_DIRECTORY_${OUTPUTCONFIG} ${OUTPUT_DIR} )
endforeach( OUTPUTCONFIG CMAKE_CONFIGURATION_TYPES )

# Make sure CMAKE_INSTALL_LIBDIR is relative
if(IS_ABSOLUTE ${CMAKE_INSTALL_LIBDIR})
	file(RELATIVE_PATH CMAKE_INSTALL_LIBDIR ${CMAKE_INSTALL_PREFIX} ${CMAKE_INSTALL_LIBDIR})
endif()

set(NEKO_VERSION_MAJOR 2)
set(NEKO_VERSION_MINOR 4)
set(NEKO_VERSION_PATCH 1)

string(TIMESTAMP NEKO_BUILD_YEAR "%Y")

# NEKO_VERSION is cached such that we can query it by `cmake -L -N -B . | grep NEKO_VERSION`
set(NEKO_VERSION ${NEKO_VERSION_MAJOR}.${NEKO_VERSION_MINOR}.${NEKO_VERSION_PATCH} CACHE STRING INTERNAL)

# Determine target endianness
TEST_BIG_ENDIAN(NEKO_BIG_ENDIAN)

option(WITH_REGEXP "Build with Perl-compatible regex support." ON)
option(WITH_UI "Build with GTK-3 UI support." ON)
option(WITH_SSL "Build with SSL support." ON)
option(WITH_MYSQL "Build with MySQL support." ON)
option(WITH_SQLITE "Build with SQLite support." ON)
option(WITH_APACHE "Build with Apache modules." ON)
option(WITH_NEKOML "Build NekoML." ON)

# Process common headers in libraries
# TODO libraries should not be built from this file, but rather by traversing the tree using add_subdirectory
#add_subdirectory(libs)

if(CMAKE_SIZEOF_VOID_P EQUAL 8)
	set(arch_64 "64")
else()
	set(arch_64 "")
endif()

if(WIN32)
	if (CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
		set (CMAKE_INSTALL_PREFIX "C:/HaxeToolkit/neko" CACHE PATH "default install path" FORCE)
	endif()
	set(NEKO_MODULE_PATH ${CMAKE_INSTALL_PREFIX})
else()
	set(NEKO_MODULE_PATH ${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/neko)
endif()

if(APPLE AND STATIC_DEPS STREQUAL "all")
	if(NOT CMAKE_OSX_DEPLOYMENT_TARGET)
		set(CMAKE_OSX_DEPLOYMENT_TARGET "11" CACHE STRING "CMAKE_OSX_DEPLOYMENT_TARGET" FORCE)
	endif()
endif()

check_include_file(xlocale.h NEKO_XLOCALE_H)

option(NEKO_JIT_DISABLE "Disable Neko JIT." OFF)
option(NEKO_JIT_DEBUG "Debug Neko JIT." OFF)

configure_file (
	"${CMAKE_SOURCE_DIR}/vm/neko.h.in"
	"${CMAKE_BINARY_DIR}/neko.h"
)

set(external_deps
	BoehmGC
	Zlib
	OpenSSL
	MariaDBConnector
	pcre2
	SQLite3
	APR
	APRutil
	Apache
	MbedTLS
)

if (WIN32)
	set(STATIC_DEPS_DEFAULT "all")
else()
	set(STATIC_DEPS_DEFAULT "none")

	option(RELOCATABLE "Set RPATH to $ORIGIN (Linux) / @executable_path (Mac)." ON)

	if (NOT APPLE)
		option(RUN_LDCONFIG "Run ldconfig after install." ON)
	endif()
endif()

set(STATIC_DEPS_DOC "Dependencies that should be linked statically. Can be \"all\", \"none\", or a list of library names (e.g. \"${external_deps}\").")
set(STATIC_DEPS ${STATIC_DEPS_DEFAULT} CACHE STRING "${STATIC_DEPS_DOC}")

# Validate STATIC_DEPS
if (STATIC_DEPS STREQUAL "all")
	set(STATIC_DEPS_ALL ${external_deps})
	if (WIN32)
		list(REMOVE_ITEM STATIC_DEPS_ALL BoehmGC)
	endif()
	set(STATIC_DEPS ${STATIC_DEPS_ALL} CACHE STRING "${STATIC_DEPS_DOC}" FORCE)
elseif (STATIC_DEPS STREQUAL "none")
	message(STATUS "set STATIC_DEPS to nothing")
	set(STATIC_DEPS CACHE STRING "${STATIC_DEPS_DOC}" FORCE)
else()
	foreach(dep ${STATIC_DEPS})
		list(FIND external_deps ${dep} idx)
		if(idx EQUAL -1)
			message(FATAL_ERROR "Invalid STATIC_DEPS. There is no ${dep} in the list of ${external_deps}")
		elseif(WIN32 AND dep STREQUAL "BoehmGC")
			message(FATAL_ERROR "Cannot link ${dep} statically on Windows")
		endif()
	endforeach()
endif()

# Set STATIC_* variables according to STATIC_DEPS.
foreach(dep ${external_deps})
	string(TOUPPER ${dep} var)
	list(FIND STATIC_DEPS ${dep} static_idx)
	if (static_idx EQUAL -1)
		set(STATIC_${var} FALSE)
	else()
		set(STATIC_${var} TRUE)
	endif()
endforeach()

include(ExternalProject)

if (RELOCATABLE)
	# https://gitlab.kitware.com/cmake/community/-/wikis/doc/cmake/RPATH-handling
	# Set this to true, otherwise the binaries won't be relocatable until after installation:
	set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
	if(APPLE)
		set(CMAKE_INSTALL_RPATH @executable_path/)
	elseif(UNIX)
		set(CMAKE_INSTALL_RPATH \$ORIGIN)
	endif()
endif()

list(APPEND CMAKE_INSTALL_RPATH ${CMAKE_INSTALL_FULL_LIBDIR})

if(UNIX AND NOT APPLE)
	add_definitions(-DABI_ELF)
endif()

if(UNIX)
	add_definitions(-D_GNU_SOURCE)
	add_compile_options(-fno-omit-frame-pointer)

	set(CMAKE_POSITION_INDEPENDENT_CODE TRUE)
	set(ARG_PIC -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE)

	# https://github.com/HaxeFoundation/neko/pull/17
	if(CMAKE_SIZEOF_VOID_P EQUAL 4)
		check_c_compiler_flag(-mincoming-stack-boundary=2 HAS_MINCOMING_STACK_BOUNDARY)
		check_c_compiler_flag(-mstack-alignment=2 HAS_MSTACK_ALIGNMENT)
		if(HAS_MINCOMING_STACK_BOUNDARY)
			add_compile_options(-mincoming-stack-boundary=2)
		elseif(HAS_MSTACK_ALIGNMENT)
			add_compile_options(-mstack-alignment=2)
		endif()
	endif()

	find_package(PkgConfig REQUIRED)
endif()

# git is used for source_archive and for applying patch
find_package(Git REQUIRED)

# copy the lib/src folder to build directory
# (if it is a fat archive, there will be external libraries)
if(EXISTS ${CMAKE_SOURCE_DIR}/libs/src)
	file(COPY ${CMAKE_SOURCE_DIR}/libs/src DESTINATION ${CMAKE_BINARY_DIR}/libs)
endif()

# ExternalProject configs
set(EP_CONFIGS
	PREFIX ${CMAKE_BINARY_DIR}/libs
	DOWNLOAD_DIR ${CMAKE_BINARY_DIR}/libs/download
)
list(APPEND EP_CONFIGS
	DOWNLOAD_NO_PROGRESS 1
)
if (${CMAKE_VERSION} VERSION_LESS 3.19)
	list(APPEND EP_CONFIGS
		INDEPENDENT_STEP_TARGETS download
	)
else()
	# download is independent by default in 3.19
	list(APPEND EP_CONFIGS
		STEP_TARGETS download
	)
endif()
set(EP_PROPS
	EXCLUDE_FROM_ALL 1
)


include_directories(
	${CMAKE_BINARY_DIR}
	vm
	libs/common
)

file(GLOB libneko_public_headers
	vm/neko*.h
)
list(APPEND libneko_public_headers
	${CMAKE_BINARY_DIR}/neko.h
)

add_library(libneko SHARED
	vm/alloc.c
	vm/builtins.c
	vm/callback.c
	vm/elf.c
	vm/interp.c
	vm/load.c
	vm/objtable.c
	vm/others.c
	vm/hash.c
	vm/module.c
	vm/jit_x86.c
	vm/threads.c
)

add_executable(nekovm
	vm/stats.c
	vm/main.c
)

# We need to build from source on Windows regardless
if (STATIC_BOEHMGC OR WIN32)
	ExternalProject_Add(libatomic_ops
		${EP_CONFIGS}
		URL https://github.com/bdwgc/libatomic_ops/releases/download/v7.10.0/libatomic_ops-7.10.0.tar.gz
		URL_HASH SHA256=0db3ebff755db170f65e74a64ec4511812e9ee3185c232eeffeacd274190dfb0
		CONFIGURE_COMMAND echo skip config
		BUILD_COMMAND echo skip build
		INSTALL_COMMAND echo skip install
	)
	set_target_properties(libatomic_ops PROPERTIES ${EP_PROPS})

	set (
		BoehmGC_CONFIGS
		DEPENDS libatomic_ops
		URL https://github.com/ivmai/bdwgc/releases/download/v7.6.26/gc-7.6.26.tar.gz
		URL_HASH SHA256=d38e306efa54e1aebaf283b462a6396849e88b80c350f40a2e9715519374ff0b
	)

	set(GC_INCLUDE_DIR ${CMAKE_BINARY_DIR}/libs/src/BoehmGC-build/include)

	if (WIN32)
		set(GC_LIBRARIES
			${CMAKE_BINARY_DIR}/libs/src/BoehmGC-build/${CMAKE_CFG_INTDIR}/gcmt-dll.lib
		)
		ExternalProject_Add(BoehmGC
			${EP_CONFIGS}
			${BoehmGC_CONFIGS}
			CMAKE_ARGS
				-Wno-dev
				-Denable_threads=ON
				-Denable_parallel_mark=OFF
				-DCMAKE_USE_WIN32_THREADS_INIT=ON
				-DCMAKE_CXX_STANDARD=14
			PATCH_COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_BINARY_DIR}/libs/src/libatomic_ops ${CMAKE_BINARY_DIR}/libs/src/BoehmGC/libatomic_ops
			INSTALL_COMMAND
				${CMAKE_COMMAND} -E copy_directory
					${CMAKE_BINARY_DIR}/libs/src/BoehmGC/include
					${CMAKE_BINARY_DIR}/libs/src/BoehmGC-build/include/gc
		)
		add_custom_command(OUTPUT ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/gcmt-dll.dll
			DEPENDS BoehmGC
			COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_BINARY_DIR}/libs/src/BoehmGC-build/${CMAKE_CFG_INTDIR}/gcmt-dll.dll ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}
		)
		add_custom_target(gcmt-dll.dll ALL
			DEPENDS ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/gcmt-dll.dll
		)
		add_dependencies(nekovm gcmt-dll.dll)
	else()
		if (APPLE)
			set(GC_CFLAGS "-w -mmacosx-version-min=${CMAKE_OSX_DEPLOYMENT_TARGET}")
		else()
			set(GC_CFLAGS "-w")
		endif()

		set(GC_LIBRARIES
			${CMAKE_BINARY_DIR}/libs/src/BoehmGC-build/lib/libgc.a
		)

		ExternalProject_Add(BoehmGC
			${EP_CONFIGS}
			${BoehmGC_CONFIGS}
			PATCH_COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_BINARY_DIR}/libs/src/libatomic_ops ${CMAKE_BINARY_DIR}/libs/src/BoehmGC/libatomic_ops
			CONFIGURE_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/BoehmGC &&
				./configure
					--prefix=${CMAKE_BINARY_DIR}/libs/src/BoehmGC-build
					--enable-threads=posix
					--with-pic
					--enable-shared=no
					--enable-static=yes
					--enable-silent-rules
					--silent
			BUILD_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/BoehmGC &&
				make "CFLAGS=${GC_CFLAGS}"
			INSTALL_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/BoehmGC &&
				make install
			BYPRODUCTS
				${GC_LIBRARIES}
		)
	endif()

	set_target_properties(BoehmGC PROPERTIES ${EP_PROPS})
	add_dependencies(libneko BoehmGC)
else()
	find_package(BoehmGC REQUIRED)
endif()

add_custom_target(download_deps)
if (STATIC_BOEHMGC OR WIN32)
	add_dependencies(download_deps libatomic_ops-download)
	add_dependencies(download_deps BoehmGC-download)
endif()

target_include_directories(libneko PRIVATE ${GC_INCLUDE_DIR})

target_link_libraries(libneko ${GC_LIBRARIES})
target_link_libraries(nekovm libneko)

if(UNIX)
	find_package(Threads)
	target_link_libraries(libneko ${CMAKE_DL_LIBS} m ${CMAKE_THREAD_LIBS_INIT})
endif()

set_target_properties(nekovm libneko
	PROPERTIES
	OUTPUT_NAME neko
)

set_target_properties(libneko
	PROPERTIES
	VERSION ${NEKO_VERSION}
	SOVERSION ${NEKO_VERSION_MAJOR}
	COMPILE_DEFINITIONS "_USRDLL;NEKOVM_DLL_EXPORTS;NEKO_SOURCES"
	PUBLIC_HEADER "${libneko_public_headers}"
	PDB_NAME libneko
)

#######################

# compilers
# nekoc, nekoml, nekotools, and test.n

if (CMAKE_HOST_WIN32)
	set(set_neko_env set NEKOPATH=${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
	set(neko_exec $<TARGET_FILE:nekovm>)
else()
	set(set_neko_env "")
	set(neko_exec NEKOPATH=${CMAKE_RUNTIME_OUTPUT_DIRECTORY} $<TARGET_FILE:nekovm>)
endif()

file(GLOB compilers_src
	src/neko/*.nml
	src/nekoml/*.nml
	boot/*.n
)

if (RECOMPILE_NEKOC_NEKOML)
	add_custom_command(OUTPUT ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoml.n
		COMMAND ${set_neko_env}

		COMMAND ${neko_exec} ../boot/nekoml.n -nostd neko/Main.nml nekoml/Main.nml
		COMMAND ${neko_exec} ../boot/nekoc.n -link ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n neko/Main
		COMMAND ${neko_exec} ../boot/nekoc.n -link ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoml.n nekoml/Main

		VERBATIM
		DEPENDS nekovm std.ndll ${compilers_src}
		WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/src
	)
else()
	add_custom_command(OUTPUT ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoml.n
		COMMAND ${CMAKE_COMMAND} -E copy ../boot/nekoc.n ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}
		COMMAND ${CMAKE_COMMAND} -E copy ../boot/nekoml.n ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}

		DEPENDS std.ndll
		VERBATIM
		WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/src
	)
endif()

add_custom_command(OUTPUT ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/test.n
	COMMAND ${set_neko_env}
	COMMAND ${neko_exec} ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n tools/test.neko
	COMMAND ${CMAKE_COMMAND} -E copy tools/test.n ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}
	COMMAND ${CMAKE_COMMAND} -E remove tools/test.n
	VERBATIM
	DEPENDS nekovm std.ndll ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n ${CMAKE_SOURCE_DIR}/src/tools/test.neko
	WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/src
)
add_custom_target(test.n ALL DEPENDS ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/test.n)

add_custom_command(OUTPUT ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoboot.n
	COMMAND ${set_neko_env}
	COMMAND ${neko_exec} ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n tools/nekoboot.neko
	COMMAND ${CMAKE_COMMAND} -E copy tools/nekoboot.n ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}
	# COMMAND ${CMAKE_COMMAND} -E remove tools/nekoboot.n
	VERBATIM
	DEPENDS nekovm std.ndll ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n ${CMAKE_SOURCE_DIR}/src/tools/nekoboot.neko
	WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/src
)

file(GLOB nekotools_src
	src/tools/*.nml
)

add_custom_command(OUTPUT ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekotools.n
	COMMAND ${set_neko_env}
	COMMAND ${neko_exec} ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoml.n -nostd -p tools Tools.nml
	COMMAND ${neko_exec} ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n -link ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekotools.n Tools
	VERBATIM
	DEPENDS nekovm std.ndll
		${nekotools_src}
		${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n
		${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoml.n
		${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoboot.n
	WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/src
)

add_custom_command(OUTPUT ${CMAKE_BINARY_DIR}/nekoc.c
	COMMAND ${set_neko_env}
	COMMAND ${neko_exec} ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoboot -c ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n
	COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.c ${CMAKE_BINARY_DIR}
	COMMAND ${CMAKE_COMMAND} -E remove ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.c
	VERBATIM
	DEPENDS nekovm std.ndll ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoboot.n ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoc.n
	WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)
add_executable(nekoc ${CMAKE_BINARY_DIR}/nekoc.c)
target_link_libraries(nekoc libneko)

if (WITH_NEKOML)
	add_custom_command(OUTPUT ${CMAKE_BINARY_DIR}/nekoml.c
		COMMAND ${set_neko_env}
		COMMAND ${neko_exec} ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoboot -c ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoml.n
		COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoml.c ${CMAKE_BINARY_DIR}
		COMMAND ${CMAKE_COMMAND} -E remove ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoml.c
		VERBATIM
		DEPENDS nekovm std.ndll ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoboot.n ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/nekoml.n
		WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
	)
	add_executable(nekoml ${CMAKE_BINARY_DIR}/nekoml.c)
	target_link_libraries(nekoml libneko)
endif()

add_custom_command(OUTPUT ${CMAKE_BINARY_DIR}/nekotools.c
	COMMAND ${set_neko_env}
	COMMAND ${neko_exec} ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ne
... [TRUNCATED]
```

### File: deploy.sh
```sh
#!/bin/bash 

set -ex

if [ -z $haxeci_decrypt ]; then
    echo "haxeci_decrypt is unset, skip deploy"
    exit
fi

openssl aes-256-cbc -k "$haxeci_decrypt" -in haxeci_ssh.enc -out haxeci_ssh -d
chmod 600 haxeci_ssh
eval `ssh-agent -s`
ssh-add haxeci_ssh
openssl aes-256-cbc -k "$haxeci_decrypt" -in haxeci_sec.gpg.enc -out haxeci_sec.gpg -d
gpg --allow-secret-key-import --import haxeci_sec.gpg
sudo apt-get install devscripts git-buildpackage ubuntu-dev-tools dh-make dh-apache2 -y
git config --global user.name "${DEBFULLNAME}"
git config --global user.email "${DEBEMAIL}"

pushd build
    make upload_to_ppa
popd

```

### File: .github\pull_request_template.md
```md
**DEPRECATION NOTICE: Neko is not actively maintained anymore. You can open a PR anyway, but don't expect it to get merged.**

```

### File: libs\CMakeLists.txt
```txt
add_subdirectory(common)
add_subdirectory(std)

if (STATIC_ZLIB)
	set(ZLIB_CMAKE_ARGS
		-DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/libs/src/install-prefix
		-Wno-dev
	)
	if (UNIX)
		list(APPEND ZLIB_CMAKE_ARGS
			-DCMAKE_OSX_ARCHITECTURES=${CMAKE_OSX_ARCHITECTURES}
			-DCMAKE_OSX_DEPLOYMENT_TARGET=${CMAKE_OSX_DEPLOYMENT_TARGET}
			${ARG_PIC}
		)
	endif()
	if (WIN32)
		set(ZLIB_LIBRARIES
			optimized ${CMAKE_BINARY_DIR}/libs/src/install-prefix/lib/zlibstatic.lib
			debug ${CMAKE_BINARY_DIR}/libs/src/install-prefix/lib/zlibstaticd.lib
		)
	else()
		set(ZLIB_LIBRARIES ${CMAKE_BINARY_DIR}/libs/src/install-prefix/lib/libz.a)
	endif()

	# Get the current config. Borrowed from
	# https://github.com/Kitware/CMake/blob/bc7d64f896d6e180970cb404cc7699732db34adc/Modules/ExternalProject.cmake
	if (CMAKE_CFG_INTDIR AND
		NOT CMAKE_CFG_INTDIR STREQUAL "." AND
		NOT CMAKE_CFG_INTDIR MATCHES "\\$")
		set(config ${CMAKE_CFG_INTDIR})
	else()
		set(config $<CONFIG>)
	endif()

	ExternalProject_Add(Zlib
		${EP_CONFIGS}
		URL
			https://zlib.net/zlib-1.3.1.tar.gz
			https://github.com/madler/zlib/releases/download/v1.3.1/zlib-1.3.1.tar.gz
		URL_HASH SHA256=9a93b2b7dfdac77ceba5a558a580e74667dd6fede4585b91eefb60f03b72df23
		CMAKE_ARGS ${ZLIB_CMAKE_ARGS}
		INSTALL_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/Zlib-build &&
			${CMAKE_COMMAND} --build . --target install --config ${config}
		BYPRODUCTS ${ZLIB_LIBRARIES}
	)
	set_target_properties(Zlib PROPERTIES ${EP_PROPS})
	set(ZLIB_INCLUDE_DIRS ${CMAKE_BINARY_DIR}/libs/src/install-prefix/include)
	# Download project for fat source archive
	add_dependencies(download_deps Zlib-download)
else()
	find_package(ZLIB REQUIRED)
endif()

add_subdirectory(zlib)
if (WITH_MYSQL)
	add_subdirectory(mysql)
endif()
if (WITH_REGEXP)
	add_subdirectory(regexp)
endif()
if (WITH_SQLITE)
	add_subdirectory(sqlite)
endif()
if (WITH_SSL)
	add_subdirectory(ssl)
endif()
if (WITH_UI)
	add_subdirectory(ui)
endif()

if (WITH_APACHE)
	# Locate Apache
	if (STATIC_APACHE)
		if (STATIC_OPENSSL)
			set(OPENSSL_CONF --with-openssl=${CMAKE_BINARY_DIR}/libs/src/install-prefix)
			set(OPENSSL_DEP OpenSSL)
		else()
			set(OPENSSL_CONF "")
			set(OPENSSL_DEP "")
		endif()
		if (STATIC_APR)
			set(APR_CONF --with-apr=${CMAKE_BINARY_DIR}/libs/src/install-prefix)
			set(APR_DEP APR)
		else()
			set(APR_CONF "")
			set(APR_DEP "")
		endif()
		if (STATIC_APRUTIL)
			set(APRUTIL_CONF --with-apr-util=${CMAKE_BINARY_DIR}/libs/src/install-prefix)
			set(APRUTIL_DEP APRutil)
		else()
			set(APRUTIL_CONF "")
			set(APRUTIL_DEP "")
		endif()
		if (STATIC_PCRE2)
			set(PCRE_CONF --with-pcre=${CMAKE_BINARY_DIR}/libs/src/install-prefix/bin/pcre2-config)
			set(PCRE_DEP pcre2)
		else()
			set(PCRE_CONF "")
			set(PCRE_DEP "")
		endif()
		if (STATIC_ZLIB)
			set(ZLIB_CONF --with-z=${CMAKE_BINARY_DIR}/libs/src/install-prefix)
			set(ZLIB_DEP Zlib)
		else()
			set(ZLIB_CONF "")
			set(ZLIB_DEP "")
		endif()
		if (WIN32)
			set(EXPAT_CONF
				-DCMAKE_POLICY_DEFAULT_CMP0074=NEW
				-DEXPAT_ROOT=${CMAKE_BINARY_DIR}/libs/src/install-prefix
			)
			if (${CMAKE_VERSION} VERSION_LESS 3.12)
				message(WARNING "CMake 3.12 or above is required for building APRutil on Windows")
			endif()
			if (${CMAKE_VERSION} VERSION_LESS 3.27)
				# we need to make sure cmake finds the correct library build
				# see: https://gitlab.kitware.com/cmake/cmake/-/merge_requests/8225
				# this monstrosity is necessary because semicolons have to be escaped for each time the string variable is used
				string(REPLACE ";" "\\\\\\\\\\\\\;" EXPAT_LIBRARY_SUFFIXES_ESCAPED "${CMAKE_FIND_LIBRARY_SUFFIXES};dMD.lib;MD.lib;dMT.lib;MT.lib;d.lib")
				list(APPEND EXPAT_CONF "-DCMAKE_FIND_LIBRARY_SUFFIXES=${EXPAT_LIBRARY_SUFFIXES_ESCAPED}")
			endif()
			set(EXPAT_DEP EXPAT)
		else()
			set(EXPAT_CONF "")
			set(EXPAT_DEP "")
		endif()

		if (APPLE)
			set(APACHE_CFLAGS "-w -mmacosx-version-min=${CMAKE_OSX_DEPLOYMENT_TARGET}")
		else()
			set(APACHE_CFLAGS "-w")
		endif()

		if(WIN32)
			set(APR_CONFIGS
				CMAKE_ARGS
					-DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/libs/src/install-prefix
					-Wno-dev
					-DAPR_INSTALL_PRIVATE_H=ON
					-DINSTALL_PDB=OFF
			)
		else()
			set(APR_CONFIGS
				CONFIGURE_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/APR &&
					./configure --prefix=${CMAKE_BINARY_DIR}/libs/src/install-prefix
					--enable-shared=no
					--enable-static=yes
					--silent
				BUILD_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/APR &&
					make "CFLAGS=${APACHE_CFLAGS}"
				INSTALL_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/APR &&
					make install
			)
		endif()

		ExternalProject_Add(APR
			${EP_CONFIGS}
			URL https://archive.apache.org/dist/apr/apr-1.7.2.tar.gz
			URL_HASH SHA256=3d8999b216f7b6235343a4e3d456ce9379aa9a380ffb308512f133f0c5eb2db9
			${APR_CONFIGS}
		)
		set_target_properties(APR PROPERTIES ${EP_PROPS})

		if(WIN32)
			ExternalProject_Add(EXPAT
				${EP_CONFIGS}
				URL https://github.com/libexpat/libexpat/releases/download/R_2_5_0/expat-2.5.0.tar.gz
				URL_HASH SHA256=6b902ab103843592be5e99504f846ec109c1abb692e85347587f237a4ffa1033
				CMAKE_ARGS
					-DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/libs/src/install-prefix
					-Wno-dev
					-DEXPAT_SHARED_LIBS=OFF
			)
			set_target_properties(EXPAT PROPERTIES ${EP_PROPS})
			set(APRutil_CONFIGS
				CMAKE_ARGS
					-DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/libs/src/install-prefix
					-Wno-dev
					-DINSTALL_PDB=OFF
					${EXPAT_CONF}
				PATCH_COMMAND ${CMAKE_COMMAND} -Dapr-util_source=${CMAKE_BINARY_DIR}/libs/src/APRutil -P ${CMAKE_SOURCE_DIR}/cmake/patch_apr-util.cmake
			)
		else()
			set(APRutil_CONFIGS
				CONFIGURE_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/APRutil &&
					./configure
						--prefix=${CMAKE_BINARY_DIR}/libs/src/install-prefix
						--silent
						${APR_CONF}
				BUILD_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/APRutil &&
					make "CFLAGS=${APACHE_CFLAGS}"
				INSTALL_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/APRutil &&
					make install
			)
		endif()

		ExternalProject_Add(APRutil
			${EP_CONFIGS}
			DEPENDS ${APR_DEP} ${EXPAT_DEP}
			URL https://archive.apache.org/dist/apr/apr-util-1.6.3.tar.gz
			URL_HASH SHA256=2b74d8932703826862ca305b094eef2983c27b39d5c9414442e9976a9acf1983
			${APRutil_CONFIGS}
		)
		set_target_properties(APRutil PROPERTIES ${EP_PROPS})

		if(WIN32)
			set(Apache_CONFIGS
				CMAKE_ARGS
					-DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/libs/src/install-prefix
					-Wno-dev
					-DOPENSSL_ROOT_DIR=${CMAKE_BINARY_DIR}/libs/src/install-prefix
					-DEXTRA_LIBS=Ws2_32
				PATCH_COMMAND PATCH_COMMAND ${CMAKE_COMMAND} -Dapache_source=${CMAKE_BINARY_DIR}/libs/src/Apache -P ${CMAKE_SOURCE_DIR}/cmake/patch_apache.cmake
				BUILD_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/Apache-build &&
					${CMAKE_COMMAND} --build . --target libhttpd --config ${CMAKE_CFG_INTDIR}
				INSTALL_COMMAND echo skip install
			)
			set(APACHE_INCLUDE_DIRS
				${CMAKE_BINARY_DIR}/libs/src/install-prefix/include
				${CMAKE_BINARY_DIR}/libs/src/Apache/include
				${CMAKE_BINARY_DIR}/libs/src/Apache/os/win32
				${CMAKE_BINARY_DIR}/libs/src/Apache-build
			)
			set(APACHE_LIBRARIES
				${CMAKE_BINARY_DIR}/libs/src/install-prefix/lib/libapr-1.lib
				${CMAKE_BINARY_DIR}/libs/src/Apache-build/${CMAKE_CFG_INTDIR}/libhttpd.lib
			)
		else()
			set(Apache_CONFIGS
				CONFIGURE_COMMAND cd ${CMAKE_BINARY_DIR}/libs/src/Apache &&
					./configure
						--prefix=${CMAKE_BINARY_DIR}/libs/src/Apache-build
						--silent
						${APR_CONF}
						${OPENSSL_CONF}
						${PCRE_CONF}
						${ZLIB_CONF}
						${APRUTIL_CONF}
				BUILD_COMMAND echo skip build
				INSTALL_COMMAND echo skip install
			)
			set(APACHE_INCLUDE_DIRS
				${CMAKE_BINARY_DIR}/libs/src/install-prefix/include/apr-1
				${CMAKE_BINARY_DIR}/libs/src/Apache/include
				${CMAKE_BINARY_DIR}/libs/src/Apache/os/unix
			)
			set(APACHE_LIBRARIES

			)
		endif()
		ExternalProject_Add(Apache
			${EP_CONFIGS}
			DEPENDS ${APR_DEP} ${APRUTIL_DEP} ${OPENSSL_DEP} ${PCRE_DEP} ${ZLIB_DEP}
			URL
				https://archive.apache.org/dist/httpd/httpd-2.4.55.tar.gz
				https://github.com/HaxeFoundation/neko/files/10745746/httpd-2.4.55.tar.gz
			URL_HASH SHA256=5276ea8bc6fff31eed5c82132ae51a0b2ee05f9e6b61a00fa877f6cadab3b638
			${Apache_CONFIGS}
		)
		set_target_properties(Apache PROPERTIES ${EP_PROPS})
		# Download sources for fat source archive
		if (WIN32)
			add_dependencies(download_deps EXPAT-download)
		endif()
		add_dependencies(download_deps Apache-download)
		add_dependencies(download_deps APR-download)
		add_dependencies(download_deps APRutil-download)
	else()
		find_package(APACHE REQUIRED)
		find_package(APR REQUIRED)
		set(APACHE_LIBRARIES ${APR_LIBRARIES} ${APRUTIL_LIBRARIES})
		if(HTTPD_LIBRARIES)
			list(APPEND APACHE_LIBRARIES ${HTTPD_LIBRARIES})
		endif()
		set(APACHE_INCLUDE_DIRS ${APACHE_INCLUDE_DIR} ${APR_INCLUDE_DIR} ${APRUTIL_INCLUDE_DIR})
	endif()

	add_subdirectory(mod_neko)
	add_subdirectory(mod_tora)
endif()

```

### File: .github\ISSUE_TEMPLATE\new-issue.md
```md
---
name: New issue
about: Neko is not actively maintained anymore. You can open an issue anyway, but
  don't expect to get response from developers.
title: ''
labels: ''
assignees: ''

---

*DEPRECATION NOTICE: Neko is not actively maintained anymore. You can open an issue anyway, but don't expect to get response from developers.*

```

### File: libs\common\CMakeLists.txt
```txt
configure_file (
	"${CMAKE_CURRENT_SOURCE_DIR}/osdef.h.in"
	"${CMAKE_BINARY_DIR}/osdef.h"
)

add_library(socket STATIC socket.c)
add_library(sha1 STATIC sha1.c)

```

### File: libs\common\sha1.c
```c
/*
 * Copyright (C)2005-2022 Haxe Foundation
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 */
#include "osdef.h"
#include "sha1.h"
#include <stdio.h>
#include <string.h>

// original code by Steve Reid

#define rol(value, bits) (((value) << (bits)) | ((value) >> (32 - (bits))))
#ifdef NEKO_BIG_ENDIAN
#	define blk0(i) block[i]
#else
#	define blk0(i) (block[i] = (rol(block[i],24)&0xFF00FF00) \
		|(rol(block[i],8)&0x00FF00FF))
#endif
#define blk(i) (block[i&15] = rol(block[(i+13)&15]^block[(i+8)&15] \
    ^block[(i+2)&15]^block[i&15],1))
/* (R0+R1), R2, R3, R4 are the different operations used in SHA1 */
#define R0(v,w,x,y,z,i) z+=((w&(x^y))^y)+blk0(i)+0x5A827999+rol(v,5);w=rol(w,30);
#define R1(v,w,x,y,z,i) z+=((w&(x^y))^y)+blk(i)+0x5A827999+rol(v,5);w=rol(w,30);
#define R2(v,w,x,y,z,i) z+=(w^x^y)+blk(i)+0x6ED9EBA1+rol(v,5);w=rol(w,30);
#define R3(v,w,x,y,z,i) z+=(((w|x)&y)|(w&x))+blk(i)+0x8F1BBCDC+rol(v,5);w=rol(w,30);
#define R4(v,w,x,y,z,i) z+=(w^x^y)+blk(i)+0xCA62C1D6+rol(v,5);w=rol(w,30);

static void sha1_transform( unsigned int state[5], unsigned char buffer[64] ) {
	unsigned int a, b, c, d, e;
	unsigned int block[16];
	memcpy(block, buffer, 64);
	/* Copy context->state[] to working vars */
	a = state[0];
	b = state[1];
	c = state[2];
	d = state[3];
	e = state[4];
	/* 4 rounds of 20 operations each. Loop unrolled. */
	R0(a,b,c,d,e, 0); R0(e,a,b,c,d, 1); R0(d,e,a,b,c, 2); R0(c,d,e,a,b, 3);
	R0(b,c,d,e,a, 4); R0(a,b,c,d,e, 5); R0(e,a,b,c,d, 6); R0(d,e,a,b,c, 7);
	R0(c,d,e,a,b, 8); R0(b,c,d,e,a, 9); R0(a,b,c,d,e,10); R0(e,a,b,c,d,11);
	R0(d,e,a,b,c,12); R0(c,d,e,a,b,13); R0(b,c,d,e,a,14); R0(a,b,c,d,e,15);
	R1(e,a,b,c,d,16); R1(d,e,a,b,c,17); R1(c,d,e,a,b,18); R1(b,c,d,e,a,19);
	R2(a,b,c,d,e,20); R2(e,a,b,c,d,21); R2(d,e,a,b,c,22); R2(c,d,e,a,b,23);
	R2(b,c,d,e,a,24); R2(a,b,c,d,e,25); R2(e,a,b,c,d,26); R2(d,e,a,b,c,27);
	R2(c,d,e,a,b,28); R2(b,c,d,e,a,29); R2(a,b,c,d,e,30); R2(e,a,b,c,d,31);
	R2(d,e,a,b,c,32); R2(c,d,e,a,b,33); R2(b,c,d,e,a,34); R2(a,b,c,d,e,35);
	R2(e,a,b,c,d,36); R2(d,e,a,b,c,37); R2(c,d,e,a,b,38); R2(b,c,d,e,a,39);
	R3(a,b,c,d,e,40); R3(e,a,b,c,d,41); R3(d,e,a,b,c,42); R3(c,d,e,a,b,43);
	R3(b,c,d,e,a,44); R3(a,b,c,d,e,45); R3(e,a,b,c,d,46); R3(d,e,a,b,c,47);
	R3(c,d,e,a,b,48); R3(b,c,d,e,a,49); R3(a,b,c,d,e,50); R3(e,a,b,c,d,51);
	R3(d,e,a,b,c,52); R3(c,d,e,a,b,53); R3(b,c,d,e,a,54); R3(a,b,c,d,e,55);
	R3(e,a,b,c,d,56); R3(d,e,a,b,c,57); R3(c,d,e,a,b,58); R3(b,c,d,e,a,59);
	R4(a,b,c,d,e,60); R4(e,a,b,c,d,61); R4(d,e,a,b,c,62); R4(c,d,e,a,b,63);
	R4(b,c,d,e,a,64); R4(a,b,c,d,e,65); R4(e,a,b,c,d,66); R4(d,e,a,b,c,67);
	R4(c,d,e,a,b,68); R4(b,c,d,e,a,69); R4(a,b,c,d,e,70); R4(e,a,b,c,d,71);
	R4(d,e,a,b,c,72); R4(c,d,e,a,b,73); R4(b,c,d,e,a,74); R4(a,b,c,d,e,75);
	R4(e,a,b,c,d,76); R4(d,e,a,b,c,77); R4(c,d,e,a,b,78); R4(b,c,d,e,a,79);
	/* Add the working vars back into context.state[] */
	state[0] += a;
	state[1] += b;
	state[2] += c;
	state[3] += d;
	state[4] += e;
}

void sha1_init( SHA1_CTX *context ) {
	/* SHA1 initialization constants */
	context->state[0] = 0x67452301;
	context->state[1] = 0xEFCDAB89;
	context->state[2] = 0x98BADCFE;
	context->state[3] = 0x10325476;
	context->state[4] = 0xC3D2E1F0;
	context->count[0] = context->count[1] = 0;
}

void sha1_update( SHA1_CTX *context, const unsigned char *data, unsigned int len ) {
	unsigned int i, j;
	j = (context->count[0] >> 3) & 63;
	if ((context->count[0] += len << 3) < (len << 3)) context->count[1]++;
	context->count[1] += (len >> 29);
	if ((j + len) > 63) {
		memcpy(&context->buffer[j], data, (i = 64-j));
		sha1_transform(context->state, context->buffer);
		for ( ; i + 63 < len; i += 64 )
			sha1_transform(context->state, (unsigned char *)&data[i]);
		j = 0;
	} else
		i = 0;
	memcpy(&context->buffer[j], &data[i], len - i);
}

void sha1_final( SHA1_CTX *context, unsigned char digest[SHA1_SIZE] ) {
	unsigned int i;
	unsigned char finalcount[8];
	for (i = 0; i < 8; i++) {
		finalcount[i] = (unsigned char)((context->count[(i >= 4 ? 0 : 1)]
			>> ((3-(i & 3)) * 8) ) & 255);  /* Endian independent */
	}
	sha1_update(context, (unsigned char *)"\200", 1);
	while ((context->count[0] & 504) != 448) {
		sha1_update(context, (unsigned char *)"\0", 1);
	}
	sha1_update(context, finalcount, 8);
	for (i = 0; i < SHA1_SIZE; i++) {
		digest[i] = (unsigned char)
			((context->state[i>>2] >> ((3-(i & 3)) * 8) ) & 255);
	}
	sha1_transform(context->state, context->buffer);
}


```

### File: libs\common\socket.c
```c
/*
 * Copyright (C)2005-2022 Haxe Foundation
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 */
#include "socket.h"
#include <string.h>

#ifdef OS_WINDOWS
	static int init_done = 0;
	static WSADATA init_data;
#	define POSIX_LABEL(x)
#	define HANDLE_EINTR(x)

#else
#	include <sys/types.h>
#	include <sys/socket.h>
#	include <sys/time.h>
#	include <netinet/in.h>
#	include <netinet/tcp.h>
#	include <arpa/inet.h>
#	include <unistd.h>
#	include <netdb.h>
#	include <fcntl.h>
#	include <errno.h>
#	include <stdio.h>
#	include <poll.h>
#	define closesocket close
#	define SOCKET_ERROR (-1)
#	define POSIX_LABEL(x)	x:
#	define HANDLE_EINTR(x)	if( errno == EINTR ) goto x
#endif

#ifndef MSG_NOSIGNAL
#	define MSG_NOSIGNAL 0
#endif

static int block_error() {
#ifdef OS_WINDOWS
	int err = WSAGetLastError();
	if( err == WSAEWOULDBLOCK || err == WSAEALREADY )
#else
	if( errno == EAGAIN || errno == EWOULDBLOCK || errno == EINPROGRESS || errno == EALREADY )
#endif
		return PS_BLOCK;
	return PS_ERROR;
}

void psock_init() {
#ifdef OS_WINDOWS
	if( !init_done ) {
		WSAStartup(MAKEWORD(2,0),&init_data);
		init_done = 1;
	}
#endif
}

PSOCK psock_create() {
	PSOCK s = socket(AF_INET,SOCK_STREAM,0);
#	if defined(OS_MAC) || (defined(OS_BSD) && defined(SO_NOSIGPIPE))
	if( s != INVALID_SOCKET )
		setsockopt(s,SOL_SOCKET,SO_NOSIGPIPE,NULL,0);
#	endif
#	ifdef OS_POSIX
	// we don't want sockets to be inherited in case of exec
	{
		int old = fcntl(s,F_GETFD,0);
		if( old >= 0 ) fcntl(s,F_SETFD,old|FD_CLOEXEC);
	}
#	endif
	return s;
}

void psock_close( PSOCK s ) {
	POSIX_LABEL(close_again);
	if( closesocket(s) ) {
		HANDLE_EINTR(close_again);
	}
}

int psock_send( PSOCK s, const char *buf, int size ) {
	int ret;
	POSIX_LABEL(send_again);
	ret = send(s,buf,size,MSG_NOSIGNAL);
	if( ret == SOCKET_ERROR ) {
		HANDLE_EINTR(send_again);
		return block_error();
	}
	return ret;
}

int psock_recv( PSOCK s, char *buf, int size ) {
	int ret;
	POSIX_LABEL(recv_again);
	ret = recv(s,buf,size,MSG_NOSIGNAL);
	if( ret == SOCKET_ERROR ) {
		HANDLE_EINTR(recv_again);
		return block_error();
	}
	return ret;
}

PHOST phost_resolve( const char *host ) {
	PHOST ip = inet_addr(host);
	if( ip == INADDR_NONE ) {
		struct hostent *h;
#	if defined(OS_WINDOWS) || defined(OS_MAC) || defined(OS_CYGWIN) || defined(__NetBSD__) || defined(__OpenBSD__)
		h = gethostbyname(host);
#	else
		struct hostent hbase;
		char buf[1024];
		int errcode;
		gethostbyname_r(host,&hbase,buf,1024,&h,&errcode);
#	endif
		if( h == NULL )
			return UNRESOLVED_HOST;
		ip = *((unsigned int*)h->h_addr);
	}
	return ip;
}

SERR psock_connect( PSOCK s, PHOST host, int port ) {
	struct sockaddr_in addr;
	memset(&addr,0,sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = htons(port);
	*(int*)&addr.sin_addr.s_addr = host;
	if( connect(s,(struct sockaddr*)&addr,sizeof(addr)) != 0 )
		return block_error();
	return PS_OK;
}

SERR psock_set_timeout( PSOCK s, double t ) {
#ifdef OS_WINDOWS
	int time = (int)(t * 1000);
#else
	struct timeval time;
	time.tv_usec = (int)((t - (int)t)*1000000);
	time.tv_sec = (int)t;
#endif
	if( setsockopt(s,SOL_SOCKET,SO_SNDTIMEO,(char*)&time,sizeof(time)) != 0 )
		return PS_ERROR;
	if( setsockopt(s,SOL_SOCKET,SO_RCVTIMEO,(char*)&time,sizeof(time)) != 0 )
		return PS_ERROR;
	return PS_OK;
}


SERR psock_set_blocking( PSOCK s, int block ) {
#ifdef OS_WINDOWS
	{
		unsigned long arg = !block;
		if( ioctlsocket(s,FIONBIO,&arg) != 0 )
			return PS_ERROR;
	}
#else
	{
		int rights = fcntl(s,F_GETFL);
		if( rights == -1 )
			return PS_ERROR;
		if( block )
			rights &= ~O_NONBLOCK;
		else
			rights |= O_NONBLOCK;
		if( fcntl(s,F_SETFL,rights) == -1 )
			return PS_ERROR;
	}
#endif
	return PS_OK;
}

SERR psock_set_fastsend( PSOCK s, int fast ) {
	if( setsockopt(s,IPPROTO_TCP,TCP_NODELAY,(char*)&fast,sizeof(fast)) )
		return block_error();
	return PS_OK;
}

void psock_wait( PSOCK s ) {
#	ifdef OS_WINDOWS
	fd_set set;
	FD_ZERO(&set);
	FD_SET(s,&set);
	select((int)s+1,&set,NULL,NULL,NULL);
#	else
	struct pollfd fds;
	POSIX_LABEL(poll_again);
	fds.fd = s;
	fds.events = POLLIN;
	fds.revents = 0;
	if( poll(&fds,1,-1) < 0 ) {
		HANDLE_EINTR(poll_again);
	}
#	endif
}

/* ************************************************************************ */

```

### File: libs\ui\CMakeLists.txt
```txt
include(FindPkgConfig)

######################
# ui.ndll

add_library(ui.ndll MODULE ui.c)

target_link_libraries(ui.ndll libneko)

if(APPLE)
	find_library(CARBON_LIBRARY Carbon REQUIRED)
	target_link_libraries(ui.ndll ${CARBON_LIBRARY})
elseif(UNIX)
	pkg_check_modules(GTK3 REQUIRED gtk+-3.0)
	target_include_directories(ui.ndll PRIVATE
		${GTK3_INCLUDEDIR}
		${GTK3_INCLUDE_DIRS}
	)
	target_link_libraries(ui.ndll ${GTK3_LIBRARIES})
endif()

set_target_properties(ui.ndll
	PROPERTIES
	PREFIX ""
	OUTPUT_NAME ui
	SUFFIX .ndll
)

install (
	TARGETS ui.ndll
	DESTINATION ${DEST_NDLL}
)

install(SCRIPT ${NEKO_FLATTEN_SCRIPT})

```

### File: libs\ui\ui.c
```c
/*
 * Copyright (C)2005-2022 Haxe Foundation
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 */
#define HEADER_IMPORTS
#include <neko_vm.h>
#include <stdio.h>

#if defined(NEKO_WINDOWS)
#	include <windows.h>
#	define CLASS_NAME "Neko_UI_wnd_class"
#	define WM_SYNC_CALL	(WM_USER + 101)
#elif defined(NEKO_MAC)
#	undef lock_acquire
#	undef lock_release
#	undef lock_try
#	include <Carbon/Carbon.h>
#	include <pthread.h>
#	define UIEvent		0xFFFFAA00
#	define eCall		0x0
enum { pFunc = 'func' };
extern void RunApplicationEventLoop(void);
extern void QuitApplicationEventLoop(void);
#else
#	include <gtk/gtk.h>
#	include <glib.h>
#	include <pthread.h>
#	include <locale.h>
#endif

/**
	<doc>
	<h1>UI</h1>
	<p>
	Core native User Interface support. This API uses native WIN32 API on Windows,
	Carbon API on OSX, and GTK3 on Linux.
	</p>
	</doc>
**/

typedef struct {
	int init_done;
#if defined(NEKO_WINDOWS)
	DWORD tid;
	HWND wnd;
#elif defined(NEKO_MAC)
	pthread_t tid;
#else
	pthread_t tid;
	pthread_mutex_t lock;
#endif

} ui_data;

static ui_data data = { 0 };

#if defined(NEKO_WINDOWS)

static LRESULT CALLBACK WindowProc( HWND hwnd, UINT msg, WPARAM wparam, LPARAM lparam ) {
	switch( msg ) {
	case WM_SYNC_CALL: {
		value *r = (value*)lparam;
		value f = *r;
		free_root(r);
		// There are some GC issues here when having a lot of threads
		// It seems that somehow the function is not called, it might
		// also trigger some crashes.
		val_call0(f);
		return 0;
	}}
	return DefWindowProc(hwnd,msg,wparam,lparam);
}

#elif defined(NEKO_MAC)

static OSStatus nothing() {
	return 0;
}

static OSStatus handleEvents( EventHandlerCallRef ref, EventRef e, void *data ) {
	switch( GetEventKind(e) ) {
	case eCall: {
		value *r;
		value f;
		GetEventParameter(e,pFunc,typeVoidPtr,0,sizeof(void*),0,&r);
		f = *r;
		free_root(r);
		val_call0(f);
		break;
	}}
	return 0;
}

#elif defined(NEKO_LINUX)

static gint onSyncCall( gpointer data ) {
	value *r = (value*)data;
	value f = *r;
	free_root(r);
	val_call0(f);
	return FALSE;
}

#endif

DEFINE_ENTRY_POINT(ui_main);

void ui_main() {
	if( data.init_done )
		return;
	data.init_done = 1;
#	if defined(NEKO_WINDOWS)
	{
		WNDCLASSEX wcl;
		HINSTANCE hinst = GetModuleHandle(NULL);
		memset(&wcl,0,sizeof(wcl));
		wcl.cbSize			= sizeof(WNDCLASSEX);
		wcl.style			= CS_HREDRAW | CS_VREDRAW | CS_OWNDC;
		wcl.lpfnWndProc		= WindowProc;
		wcl.cbClsExtra		= 0;
		wcl.cbWndExtra		= 0;
		wcl.hInstance		= hinst;
		wcl.hIcon			= NULL;
		wcl.hCursor			= LoadCursor(NULL, IDC_ARROW);
		wcl.hbrBackground	= (HBRUSH)(COLOR_BTNFACE+1);
		wcl.lpszMenuName	= "";
		wcl.lpszClassName	= CLASS_NAME;
		wcl.hIconSm			= 0;
		RegisterClassEx(&wcl);
	}
	data.tid = GetCurrentThreadId();
	data.wnd = CreateWindow(CLASS_NAME,"",0,0,0,0,0,NULL,NULL,NULL,NULL);
#	elif defined(NEKO_MAC)
	MPCreateTask(nothing,NULL,0,0,0,0,0,NULL); // creates a MPTask that will enable Carbon MT
	data.tid = pthread_self();
	EventTypeSpec ets = { UIEvent, eCall };
	InstallEventHandler(GetApplicationEventTarget(),NewEventHandlerUPP(handleEvents),1,&ets,0,0);
#	elif defined(NEKO_LINUX)
	gdk_threads_init();
	gtk_init(NULL,NULL);
	setlocale(LC_NUMERIC,"POSIX"); // prevent broking atof()
	data.tid = pthread_self();
	pthread_mutex_init(&data.lock,NULL);
#	endif
}

/**
	ui_is_main : void -> bool
	<doc>
	Tells if the current thread is the main loop thread or not. The main loop thread is the one
	in which the first "ui" library primitive has been loaded.
	</doc>
**/
static value ui_is_main() {
#	ifdef NEKO_WINDOWS
	return alloc_bool(data.tid == GetCurrentThreadId());
#	else
	return alloc_bool(pthread_equal(data.tid,pthread_self()));
#	endif
}

/**
	ui_loop : void -> void
	<doc>
	Starts the native UI event loop. This method can only be called from the main thread.
	</doc>
**/
static value ui_loop() {
	if( !val_bool(ui_is_main()) )
		neko_error();
#	if defined(NEKO_WINDOWS)
	{
		MSG msg;
		while( GetMessage(&msg,NULL,0,0) ) {
			TranslateMessage(&msg);
			DispatchMessage(&msg);
			if( msg.message == WM_QUIT )
				break;
		}
	}
#	elif defined(NEKO_MAC)
	RunApplicationEventLoop();
#	else
	gtk_main();
#	endif
	return val_null;
}

/**
	ui_stop_loop : void -> void
	<doc>
	Stop the native UI event loop. This method can only be called from the main thread.
	</doc>
**/
static value ui_stop_loop() {
	if( !val_bool(ui_is_main()) )
		neko_error();
#	if defined(NEKO_WINDOWS)
	while( !PostMessage(data.wnd,WM_QUIT,0,0) )
		Sleep(100);
#	elif defined(NEKO_MAC)
	QuitApplicationEventLoop();
#	else
	gtk_main_quit();
#	endif
	return val_null;
}

/**
	ui_sync : callb:(void -> void) -> void
	<doc>
	Queue a method call [callb] to be executed by the main thread while running the UI event
	loop. This can be used to perform UI updates in the UI thread using results processed by
	another thread.
	</doc>
**/
static value ui_sync( value f ) {
	value *r;
	val_check_function(f,0);
	r = alloc_root(1);
	*r = f;
#	if defined(NEKO_WINDOWS)
	while( !PostMessage(data.wnd,WM_SYNC_CALL,0,(LPARAM)r) )
		Sleep(100);
#	elif defined(NEKO_MAC)
	EventRef e;
	CreateEvent(NULL,UIEvent,eCall,GetCurrentEventTime(),kEventAttributeUserEvent,&e);
	SetEventParameter(e,pFunc,typeVoidPtr,sizeof(void*),&r);
	PostEventToQueue(GetMainEventQueue(),e,kEventPriorityStandard);
	ReleaseEvent(e);
#	elif defined(NEKO_LINUX)
	// the lock should not be needed because GTK is MT-safe
	// however the GTK lock mechanism is a LOT slower than
	// using a pthread_mutex
	pthread_mutex_lock(&data.lock);
	gdk_threads_add_timeout( 0, onSyncCall, (gpointer)r );
	pthread_mutex_unlock(&data.lock);
#	endif
	return val_null;
}

DEFINE_PRIM(ui_loop,0);
DEFINE_PRIM(ui_stop_loop,0);
DEFINE_PRIM(ui_is_main,0);
DEFINE_PRIM(ui_sync,1);

/* ************************************************************************ */

```

