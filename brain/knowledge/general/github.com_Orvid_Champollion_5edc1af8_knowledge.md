---
id: github.com-orvid-champollion-5edc1af8-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:09.907992
---

# KNOWLEDGE EXTRACT: github.com_Orvid_Champollion_5edc1af8
> **Extracted on:** 2026-04-01 09:32:28
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520247/github.com_Orvid_Champollion_5edc1af8

---

## File: `.gitattributes`
```
# Auto detect text files and perform LF normalization
* text=auto
```

## File: `.gitignore`
```
# Created by https://www.toptal.com/developers/gitignore/api/cmake
# Edit at https://www.toptal.com/developers/gitignore?templates=cmake

### CMake ###
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

### CMake Patch ###
# External projects
*-prefix/

# End of https://www.toptal.com/developers/gitignore/api/cmake

# Visual Studio
.vs/

# Visual Studio Code
.vscode/

# vcpkg
vcpkg_installed/
vcpkg_installed/**
vcpkg-manifest-install.log
# Default build directory
build

# Jetbrains IDEs
.idea/
cmake-build-*

ALL_BUILD.vcxproj
ALL_BUILD.vcxproj.filters
ALL_BUILD.vcxproj.user
INSTALL.vcxproj
INSTALL.vcxproj.filters
ZERO_CHECK.vcxproj
ZERO_CHECK.vcxproj.filters
Champollion.sln
Champollion/Champollion.dir/
Champollion/Champollion.vcxproj
Champollion/Champollion.vcxproj.filters
Champollion/Champollion.vcxproj.user
Champollion/Debug/
Champollion/Release/
Champollion/INSTALL.vcxproj
Champollion/INSTALL.vcxproj.filters
Decompiler/Debug/
Decompiler/Release/
Decompiler/Decompiler.dir/
Decompiler/Decompiler.vcxproj
Decompiler/Decompiler.vcxproj.filters
Decompiler/INSTALL.vcxproj
Decompiler/INSTALL.vcxproj.filters
Pex/Debug/
Pex/Release/
Pex/Pex.dir/
Pex/Pex.vcxproj
Pex/Pex.vcxproj.filters
Pex/Pex.vcxproj.user
Pex/INSTALL.vcxproj
Pex/INSTALL.vcxproj.filters
x64/
```

## File: `CHANGELOG.txt`
```
0.0.1
 - Comandeered to support Fallout 4.

1.0.1
 - Fixed two missing opcodes for array_findelement and array_rfindelement
 
1.0.0
 - Initial release
```

## File: `CMakeLists.txt`
```
cmake_minimum_required(VERSION 3.15 FATAL_ERROR)
cmake_policy(SET CMP0048 NEW) # VERSION variables
cmake_policy(SET CMP0091 NEW) # CMAKE_MSVC_RUNTIME_LIBRARY

# Get the version number from Decompiler/Version.hpp
file(READ "${CMAKE_CURRENT_SOURCE_DIR}/Decompiler/Version.hpp" CHAMPOLLION_VERSION_FILE)
string(REGEX MATCH "define CHAMPOLLION_VERSION_MAJOR ([0-9]*)" _ ${CHAMPOLLION_VERSION_FILE})
math(EXPR CHAMPOLLION_VERSION_MAJOR "${CMAKE_MATCH_1}")
string(REGEX MATCH "define CHAMPOLLION_VERSION_MINOR ([0-9]*)" _ ${CHAMPOLLION_VERSION_FILE})
math(EXPR CHAMPOLLION_VERSION_MINOR "${CMAKE_MATCH_1}")
string(REGEX MATCH "define CHAMPOLLION_VERSION_PATCH ([0-9]*)" _ ${CHAMPOLLION_VERSION_FILE})
math(EXPR CHAMPOLLION_VERSION_PATCH "${CMAKE_MATCH_1}")
#Get the Champollion version as a semver number literal, not as a string
set(CHAMPOLLION_VERSION ${CHAMPOLLION_VERSION_MAJOR}.${CHAMPOLLION_VERSION_MINOR}.${CHAMPOLLION_VERSION_PATCH})

message(STATUS "Champollion version: ${CHAMPOLLION_VERSION}")

# package information
set(PACKAGE_NAME      "Champollion")
set(PACKAGE_VERSION   "${CHAMPOLLION_VERSION}")
set(PACKAGE_STRING    "${PACKAGE_NAME} ${PACKAGE_VERSION}")
set(PACKAGE_TARNAME   "${PACKAGE_NAME}-${PACKAGE_VERSION}")
set(PACKAGE_BUGREPORT "https://github.com/Orvid/champollion/issues")

if(DEFINED ENV{VCPKG_ROOT} AND NOT DEFINED CMAKE_TOOLCHAIN_FILE)
  set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
      CACHE STRING "")
endif()

project(${PACKAGE_NAME} VERSION ${PACKAGE_VERSION} LANGUAGES CXX)
include(GNUInstallDirs)


option(CHAMPOLLION_STATIC_LIBRARY "Build Champollion as a static library" OFF)
option(CHAMPOLLION_USE_STATIC_RUNTIME "Compile Champollion with static runtime" OFF)

if (NOT CHAMPOLLION_STATIC_LIBRARY)
  set(CMAKE_CXX_STANDARD 20)
else()
  set(CMAKE_CXX_STANDARD 17)
endif()


# Automatically create source_group directives for the sources passed in.
function(auto_source_group rootName rootDir)
  file(TO_CMAKE_PATH "${rootDir}" rootDir)
  string(LENGTH "${rootDir}" rootDirLength)
  set(sourceGroups)
  foreach (fil ${ARGN})
    file(TO_CMAKE_PATH "${fil}" filePath)
    string(FIND "${filePath}" "/" rIdx REVERSE)
    if (rIdx EQUAL -1)
      message(FATAL_ERROR "Unable to locate the final forward slash in '${filePath}'!")
    endif()
    string(SUBSTRING "${filePath}" 0 ${rIdx} filePath)
    
    string(LENGTH "${filePath}" filePathLength)
    string(FIND "${filePath}" "${rootDir}" rIdx)
    if (NOT rIdx EQUAL 0)
      continue()
      #message(FATAL_ERROR "Source '${fil}' is outside of the root directory, '${rootDir}', that was passed to auto_source_group!")
    endif()
    math(EXPR filePathLength "${filePathLength} - ${rootDirLength}")
    string(SUBSTRING "${filePath}" ${rootDirLength} ${filePathLength} fileGroup)
    
    string(REPLACE "/" "\\" fileGroup "${fileGroup}")
    set(fileGroup "\\${rootName}${fileGroup}")
    
    list(FIND sourceGroups "${fileGroup}" rIdx)
    if (rIdx EQUAL -1)
      list(APPEND sourceGroups "${fileGroup}")
      source_group("${fileGroup}" REGULAR_EXPRESSION "${filePath}/[^/.]+(.(idl|tab|yy))?.(c|cc|cpp|h|hpp|json|ll|php|tcc|y)$")
    endif()
  endforeach()
endfunction()


if (CHAMPOLLION_USE_STATIC_RUNTIME)
  if (MSVC)
    set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
    set(MSVC_RUNTIME_LIBRARY ${CMAKE_MSVC_RUNTIME_LIBRARY})
  else()
    set(USE_STATIC_RUNTIME ON)
  endif()
endif()

add_definitions(-D_CRT_SECURE_NO_WARNINGS)
set(CHAMPOLLION_TARGET_NAME               ${PROJECT_NAME})
set(CHAMPOLLION_CONFIG_INSTALL_DIR        "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}" CACHE INTERNAL "")
set(CHAMPOLLION_INCLUDE_INSTALL_DIR       "${CMAKE_INSTALL_INCLUDEDIR}/Champollion")
set(CHAMPOLLION_TARGETS_EXPORT_NAME       "${PROJECT_NAME}-targets")
set(CHAMPOLLION_CMAKE_CONFIG_TEMPLATE     "cmake/Config.cmake.in")
set(CHAMPOLLION_CMAKE_CONFIG_DIR          "${CMAKE_CURRENT_BINARY_DIR}")
set(CHAMPOLLION_CMAKE_VERSION_CONFIG_FILE "${CHAMPOLLION_CMAKE_CONFIG_DIR}/${PROJECT_NAME}ConfigVersion.cmake")
set(CHAMPOLLION_CMAKE_PROJECT_CONFIG_FILE "${CHAMPOLLION_CMAKE_CONFIG_DIR}/${PROJECT_NAME}Config.cmake")
set(CHAMPOLLION_CMAKE_PROJECT_TARGETS_FILE "${CHAMPOLLION_CMAKE_CONFIG_DIR}/${PROJECT_NAME}-targets.cmake")

if(CHAMPOLLION_STATIC_LIBRARY)

  file(GLOB DECOMPILER_HEADER_FILES "Decompiler/*.hpp")
  file(GLOB PEX_HEADER_FILES "Pex/*.hpp")
  file(GLOB NODE_HEADER_FILES "Decompiler/Node/*.hpp")
  list(APPEND ALL_HEADERS ${DECOMPILER_HEADER_FILES} ${PEX_HEADER_FILES} ${NODE_HEADER_FILES})

  file(GLOB SOURCE_FILES "Pex/*.cpp" "Decompiler/*.cpp" "Decompiler/Node/*.cpp")

  add_library("${PROJECT_NAME}" STATIC ${ALL_HEADERS} ${SOURCE_FILES})

  target_include_directories(
    "${PROJECT_NAME}"
    PUBLIC
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}>
    $<INSTALL_INTERFACE:${CHAMPOLLION_INCLUDE_INSTALL_DIR}>
  )
  include(CMakePackageConfigHelpers)
  write_basic_package_version_file(
      ${CHAMPOLLION_CMAKE_VERSION_CONFIG_FILE} COMPATIBILITY SameMinorVersion
  )
  configure_package_config_file(
    ${CHAMPOLLION_CMAKE_CONFIG_TEMPLATE}
    "${CHAMPOLLION_CMAKE_PROJECT_CONFIG_FILE}" 
    INSTALL_DESTINATION ${CHAMPOLLION_CONFIG_INSTALL_DIR}
  )

  install(
    TARGETS "${CHAMPOLLION_TARGET_NAME}"
    EXPORT "${CHAMPOLLION_TARGETS_EXPORT_NAME}"
  )

  install(
    EXPORT "${CHAMPOLLION_TARGETS_EXPORT_NAME}"
    NAMESPACE "${CHAMPOLLION_TARGET_NAME}::"
    DESTINATION "${CHAMPOLLION_CONFIG_INSTALL_DIR}"
  )
  install(
    FILES ${DECOMPILER_HEADER_FILES}
    DESTINATION "${CHAMPOLLION_INCLUDE_INSTALL_DIR}/Decompiler"
  )
  install(
    FILES ${PEX_HEADER_FILES}
    DESTINATION "${CHAMPOLLION_INCLUDE_INSTALL_DIR}/Pex"
  )
  install(
    FILES ${NODE_HEADER_FILES}
    DESTINATION "${CHAMPOLLION_INCLUDE_INSTALL_DIR}/Decompiler/Node"
  )
  install(FILES ${CHAMPOLLION_CMAKE_VERSION_CONFIG_FILE} ${CHAMPOLLION_CMAKE_PROJECT_CONFIG_FILE}
  DESTINATION ${CHAMPOLLION_CONFIG_INSTALL_DIR})
else()
  if (VCPKG_TARGET_TRIPLET MATCHES "static")
    if(NOT MSVC)
      set(Boost_USE_STATIC_LIBS ON)
      set(Boost_USE_STATIC_RUNTIME ON)
    endif()
  endif()
  find_package(Boost REQUIRED COMPONENTS program_options)
  find_package(fmt CONFIG REQUIRED)

  include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${Boost_INCLUDE_DIRS}
  )
  add_subdirectory(Decompiler)
  add_subdirectory(Pex)
  add_subdirectory(Champollion)
  target_link_libraries(Champollion fmt::fmt)
  install(
    TARGETS Champollion
  )
endif()
```

## File: `LICENSE`
```
                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  2. Conveying Modified Versions.

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  4. Combined Works.

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

   e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  6. Revised Versions of the GNU Lesser General Public License.

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library.
```

## File: `README.md`
```markdown
# Champollion

Champollion is a decompiler for the Papyrus script language used in Skyrim, Fallout 4, Fallout 76, and Starfield. It aims to produce a Papyrus Script file (.psc) from a .pex binary file. The decompiled script should recompile to a functionally equivalent PEX binary.

## Usage

Champollion is a CLI-only program.

### Parameters

`Champollion <files or directories> [-p <output directory>] [-a [<assembly directory>]] [-c] [-t]`

| Short                     | Long                         | Description                                                  |
| ------------------------- | ---------------------------- | ------------------------------------------------------------ |
| -p *output directory*     | --psc *output directory*     | Set the output directory, where Champollion will write the decompiled files |
| -a [*assembly directory*] | --asm [*assembly directory*] | Champollion will write an assembly version of the PEX file in the given directory, if one. The assembly file is an human readable version of the content of the PEX file |
| -c                        | --comment                    | The decompiled file will be annotated with the assembly instruction corresponding to the decompiled code lines. |
| -t                        | --threaded                   | Champollion will parallelize the decompilation. It is useful when decompiling a directory containing many PEX files. |
| -r                        | --recursive                  | Recursively scan specified directory(s) for pex files to decompile|
| -s                        | --recreate-subdirs           | Recreates directory structure for script in root of output directory (Fallout 4 only, default false) |
| -e                        | --header                     | Write header to decompiled psc file                          |
| -g                        | --trace                      | Trace the decompilation and output results to rebuild log    |
|                           | --no-dump-tree               | Do not dump tree for each node during decompilation tracing (requires --trace) |
|                           | --debug-funcs                | Decompile inoperative debug and compiler-generated functions (default false) |
|                           | --no-debug-line              | Do not comment with debug info line numbers on script lines (default false) |
| -i                        | --print-info                 | Print header info from the specified PEX file(s) and exit    |
|                           | --print-compile-time         | Print the compile time of the script in format of {filename}: {time_integer} and exit |
| -v                        | --verbose                    | Verbose output                                               |
| -V                        | --version                    | Output version number                                        |
| -h                        | --help                       | Print help message                                           |


## Build Dependencies

* Boost (installable through vcpkg)
* CMake
* A C++17 compiler (for Windows you need at least Visual Studio 2019)

## Copyright

Copyright (c) 2022 Nikita Lita

Copyright (c) 2015 Orvid King

Copyright (c) 2013 Paul-Henry Perrin

See LICENSE for the LGPL V3 license.
```

## File: `vcpkg.json`
```json
{
  "$schema": "https://raw.githubusercontent.com/microsoft/vcpkg-tool/master/docs/vcpkg.schema.json",
  "name": "champollion",
  "version-semver": "1.3.2",
  "port-version": 0,
  "description": "Papyrus Script Decompiler.",
  "homepage": "https://github.com/Orvid/Champollion",
  "license": "LGPL-3.0-only",
  "supports": "windows & x64",
  "features": {
    "standalone": {
      "description": "Build as a standalone program",
      "dependencies": [
        "boost-program-options", "fmt"
      ]
    }
  },
  "default-features": ["standalone"],
  "overrides": [
    {
      "name": "boost-program-options",
      "version": "1.80.0"
    }
  ],
  "builtin-baseline": "4cb4a5c5ddcb9de0c83c85837ee6974c8333f032"
}
```

## File: `Champollion/CMakeLists.txt`
```

add_executable(Champollion main.cpp)
add_dependencies(Champollion Decompiler Pex)
target_link_libraries(Champollion Decompiler Pex ${Boost_LIBRARIES})
```

## File: `Champollion/CaselessCompare.h`
```c
#include <string>
inline int caselessCompare(const char *a, const char *b, size_t len) {
#ifdef _WIN32
  return _strnicmp(a, b, len);
#else
  return strncasecmp(a, b, len);
#endif
}

inline int caselessCompare(const char *a, const char *b) {
#ifdef _WIN32
  return _stricmp(a, b);
#else
  return strcasecmp(a, b);
#endif
}
```

## File: `Champollion/glob.hpp`
```
/**************************************************************************
 * MIT License
 * 
 * Copyright (c) 2019 Pranav
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 * **************************************************************************
*/
#pragma once
#include <cassert>
#include <functional>
#include <iostream>
#include <map>
#include <regex>
#include <string>
#include <vector>

#ifdef GLOB_USE_GHC_FILESYSTEM
#include <ghc/filesystem.hpp>
#else
#include <filesystem>
#endif

namespace glob {

#ifdef GLOB_USE_GHC_FILESYSTEM
namespace fs = ghc::filesystem;
#else
namespace fs = std::filesystem;
#endif

namespace {

static inline 
bool string_replace(std::string &str, const std::string &from, const std::string &to) {
  std::size_t start_pos = str.find(from);
  if (start_pos == std::string::npos)
    return false;
  str.replace(start_pos, from.length(), to);
  return true;
}

static inline 
std::string translate(const std::string &pattern) {
  std::size_t i = 0, n = pattern.size();
  std::string result_string;

  while (i < n) {
    auto c = pattern[i];
    i += 1;
    if (c == '*') {
      result_string += ".*";
    } else if (c == '?') {
      result_string += ".";
    } else if (c == '[') {
      auto j = i;
      if (j < n && pattern[j] == '!') {
        j += 1;
      }
      if (j < n && pattern[j] == ']') {
        j += 1;
      }
      while (j < n && pattern[j] != ']') {
        j += 1;
      }
      if (j >= n) {
        result_string += "\\[";
      } else {
        auto stuff = std::string(pattern.begin() + i, pattern.begin() + j);
        if (stuff.find("--") == std::string::npos) {
          string_replace(stuff, std::string{"\\"}, std::string{R"(\\)"});
        } else {
          std::vector<std::string> chunks;
          std::size_t k = 0;
          if (pattern[i] == '!') {
            k = i + 2;
          } else {
            k = i + 1;
          }

          while (true) {
            k = pattern.find("-", k, j);
            if (k == std::string::npos) {
              break;
            }
            chunks.push_back(std::string(pattern.begin() + i, pattern.begin() + k));
            i = k + 1;
            k = k + 3;
          }

          chunks.push_back(std::string(pattern.begin() + i, pattern.begin() + j));
          // Escape backslashes and hyphens for set difference (--).
          // Hyphens that create ranges shouldn't be escaped.
          bool first = false;
          for (auto &s : chunks) {
            string_replace(s, std::string{"\\"}, std::string{R"(\\)"});
            string_replace(s, std::string{"-"}, std::string{R"(\-)"});
            if (first) {
              stuff += s;
              first = false;
            } else {
              stuff += "-" + s;
            }
          }
        }

        // Escape set operations (&&, ~~ and ||).
        std::string result;
        std::regex_replace(std::back_inserter(result),          // result
                           stuff.begin(), stuff.end(),          // string
                           std::regex(std::string{R"([&~|])"}), // pattern
                           std::string{R"(\\\1)"});             // repl
        stuff = result;
        i = j + 1;
        if (stuff[0] == '!') {
          stuff = "^" + std::string(stuff.begin() + 1, stuff.end());
        } else if (stuff[0] == '^' || stuff[0] == '[') {
          stuff = "\\\\" + stuff;
        }
        result_string = result_string + "[" + stuff + "]";
      }
    } else {
      // SPECIAL_CHARS
      // closing ')', '}' and ']'
      // '-' (a range in character set)
      // '&', '~', (extended character set operations)
      // '#' (comment) and WHITESPACE (ignored) in verbose mode
      static std::string special_characters = "()[]{}?*+-|^$\\.&~# \t\n\r\v\f";
      static std::map<int, std::string> special_characters_map;
      if (special_characters_map.empty()) {
        for (auto &sc : special_characters) {
          special_characters_map.insert(
              std::make_pair(static_cast<int>(sc), std::string{"\\"} + std::string(1, sc)));
        }
      }

      if (special_characters.find(c) != std::string::npos) {
        result_string += special_characters_map[static_cast<int>(c)];
      } else {
        result_string += c;
      }
    }
  }
  return std::string{"(("} + result_string + std::string{R"()|[\r\n])$)"};
}

static inline 
std::regex compile_pattern(const std::string &pattern) {
  return std::regex(translate(pattern), std::regex::ECMAScript);
}

static inline 
bool fnmatch(const fs::path &name, const std::string &pattern) {
  return std::regex_match(name.string(), compile_pattern(pattern));
}

static inline 
std::vector<fs::path> filter(const std::vector<fs::path> &names,
                             const std::string &pattern) {
  // std::cout << "Pattern: " << pattern << "\n";
  std::vector<fs::path> result;
  for (auto &name : names) {
    // std::cout << "Checking for " << name.string() << "\n";
    if (fnmatch(name, pattern)) {
      result.push_back(name);
    }
  }
  return result;
}

static inline 
fs::path expand_tilde(fs::path path) {
  if (path.empty()) return path;

#ifdef _WIN32
  const char * home_variable = "USERNAME";
#else
  const char * home_variable = "USER";
#endif
  const char * home = std::getenv(home_variable);
  if (home == nullptr) {
    throw std::invalid_argument("error: Unable to expand `~` - HOME environment variable not set.");
  }

  std::string s = path.string();
  if (s[0] == '~') {
    s = std::string(home) + s.substr(1, s.size() - 1);
    return fs::path(s);
  } else {
    return path;
  }
}

static inline 
bool has_magic(const std::string &pathname) {
  static const auto magic_check = std::regex("([*?[])");
  return std::regex_search(pathname, magic_check);
}

static inline 
bool is_hidden(const std::string &pathname) {
  return std::regex_match(pathname, std::regex("^(.*\\/)*\\.[^\\.\\/]+\\/*$"));
}

static inline 
bool is_recursive(const std::string &pattern) { return pattern == "**"; }

static inline 
std::vector<fs::path> iter_directory(const fs::path &dirname, bool dironly) {
  std::vector<fs::path> result;

  auto current_directory = dirname;
  if (current_directory.empty()) {
    current_directory = fs::current_path();
  }

  if (fs::exists(current_directory)) {
    try {
      for (auto &entry : fs::directory_iterator(
              current_directory, fs::directory_options::follow_directory_symlink |
                                      fs::directory_options::skip_permission_denied)) {
        if (!dironly || entry.is_directory()) {
          if (dirname.is_absolute()) {
            result.push_back(entry.path());
          } else {
            result.push_back(fs::relative(entry.path()));
          }
        }
      }
    } catch (std::exception&) {
      // not a directory
      // do nothing
    }
  }

  return result;
}

// Recursively yields relative pathnames inside a literal directory.
static inline 
std::vector<fs::path> rlistdir(const fs::path &dirname, bool dironly) {
  std::vector<fs::path> result;
  auto names = iter_directory(dirname, dironly);
  for (auto &x : names) {
    if (!is_hidden(x.string())) {
      result.push_back(x);
      for (auto &y : rlistdir(x, dironly)) {
        result.push_back(y);
      }
    }
  }
  return result;
}

// This helper function recursively yields relative pathnames inside a literal
// directory.
static inline 
std::vector<fs::path> glob2(const fs::path &dirname, [[maybe_unused]] const std::string &pattern,
                            bool dironly) {
  // std::cout << "In glob2\n";
  std::vector<fs::path> result;
  assert(is_recursive(pattern));
  for (auto &dir : rlistdir(dirname, dironly)) {
    result.push_back(dir);
  }
  return result;
}

// These 2 helper functions non-recursively glob inside a literal directory.
// They return a list of basenames.  _glob1 accepts a pattern while _glob0
// takes a literal basename (so it only has to check for its existence).
static inline 
std::vector<fs::path> glob1(const fs::path &dirname, const std::string &pattern,
                            bool dironly) {
  // std::cout << "In glob1\n";
  auto names = iter_directory(dirname, dironly);
  std::vector<fs::path> filtered_names;
  for (auto &n : names) {
    if (!is_hidden(n.string())) {
      filtered_names.push_back(n.filename());
      // if (n.is_relative()) {
      //   // std::cout << "Filtered (Relative): " << n << "\n";
      //   filtered_names.push_back(fs::relative(n));
      // } else {
      //   // std::cout << "Filtered (Absolute): " << n << "\n";
      //   filtered_names.push_back(n.filename());
      // }
    }
  }
  return filter(filtered_names, pattern);
}

static inline 
std::vector<fs::path> glob0(const fs::path &dirname, const fs::path &basename,
                            bool /*dironly*/) {
  // std::cout << "In glob0\n";
  std::vector<fs::path> result;
  if (basename.empty()) {
    // 'q*x/' should match only directories.
    if (fs::is_directory(dirname)) {
      result = {basename};
    }
  } else {
    if (fs::exists(dirname / basename)) {
      result = {basename};
    }
  }
  return result;
}

static inline 
std::vector<fs::path> glob(const std::string &pathname, bool recursive = false,
                           bool dironly = false) {
  std::vector<fs::path> result;

  auto path = fs::path(pathname);

  if (pathname[0] == '~') {
    // expand tilde
    path = expand_tilde(path);
  }

  auto dirname = path.parent_path();
  const auto basename = path.filename();

  if (!has_magic(pathname)) {
    assert(!dironly);
    if (!basename.empty()) {
      if (fs::exists(path)) {
        result.push_back(path);
      }
    } else {
      // Patterns ending with a slash should match only directories
      if (fs::is_directory(dirname)) {
        result.push_back(path);
      }
    }
    return result;
  }

  if (dirname.empty()) {
    if (recursive && is_recursive(basename.string())) {
      return glob2(dirname, basename.string(), dironly);
    } else {
      return glob1(dirname, basename.string(), dironly);
    }
  }

  std::vector<fs::path> dirs;
  if (dirname != fs::path(pathname) && has_magic(dirname.string())) {
    dirs = glob(dirname.string(), recursive, true);
  } else {
    dirs = {dirname};
  }

  std::function<std::vector<fs::path>(const fs::path &, const std::string &, bool)>
      glob_in_dir;
  if (has_magic(basename.string())) {
    if (recursive && is_recursive(basename.string())) {
      glob_in_dir = glob2;
    } else {
      glob_in_dir = glob1;
    }
  } else {
    glob_in_dir = glob0;
  }

  for (auto &d : dirs) {
    for (auto &name : glob_in_dir(d, basename.string(), dironly)) {
      fs::path subresult = name;
      if (name.parent_path().empty()) {
        subresult = d / name;
      }
      result.push_back(subresult);
    }
  }

  return result;
}

} // namespace end

static inline 
std::vector<fs::path> glob(const std::string &pathname) {
  return glob(pathname, false);
}

static inline 
std::vector<fs::path> rglob(const std::string &pathname) {
  return glob(pathname, true);
}

static inline 
std::vector<fs::path> glob(const std::vector<std::string> &pathnames) {
  std::vector<fs::path> result;
  for (auto &pathname : pathnames) {
    for (auto &match : glob(pathname, false)) {
      result.push_back(std::move(match));
    }
  }
  return result;
}

static inline 
std::vector<fs::path> rglob(const std::vector<std::string> &pathnames) {
  std::vector<fs::path> result;
  for (auto &pathname : pathnames) {
    for (auto &match : glob(pathname, true)) {
      result.push_back(std::move(match));
    }
  }
  return result;
}

static inline 
std::vector<fs::path>
glob(const std::initializer_list<std::string> &pathnames) {
  return glob(std::vector<std::string>(pathnames));
}

static inline 
std::vector<fs::path>
rglob(const std::initializer_list<std::string> &pathnames) {
  return rglob(std::vector<std::string>(pathnames));
}

} // namespace glob
```

## File: `Champollion/main.cpp`
```cpp
#include <iostream>

#include <boost/program_options.hpp>
namespace options = boost::program_options;


#include <fmt/format.h>

#include <filesystem>
namespace fs = std::filesystem;

#include <chrono>
#include <future>
#include <ctime>

#include "Pex/Binary.hpp"
#include "Pex/FileReader.hpp"

#include "Decompiler/AsmCoder.hpp"
#include "Decompiler/PscCoder.hpp"

#include "Decompiler/StreamWriter.hpp"
#include "Decompiler/Version.hpp"
#include "glob.hpp"
#include "CaselessCompare.h"

struct Params
{
    bool outputAssembly;
    bool outputComment;
    bool writeHeader;
    bool parallel;
    bool traceDecompilation;
    bool dumpTree;
    bool recreateDirStructure;
    bool decompileDebugFuncs;
    bool recursive;
    bool verbose;
    bool printInfo;
    bool printCompileTime;
    bool debugLineComment;

    fs::path assemblyDir;
    fs::path papyrusDir;

    fs::path parentDir{};

    std::vector<fs::path> inputs;
};

enum OptionsResult{
    Invalid = -1,
    HelpOrVersion,
    Good
};

OptionsResult getProgramOptions(int argc, char* argv[], Params& params)
{
    params.outputAssembly = false;
    params.outputComment = false;
    params.writeHeader = false;
    params.parallel = false;
    params.traceDecompilation = false;
    params.dumpTree = true;
    params.recreateDirStructure = false;
    params.decompileDebugFuncs = false;
    params.verbose = false;
    params.printInfo = false;
    params.printCompileTime = false;
    params.debugLineComment = true;

    params.assemblyDir = fs::current_path();
    params.papyrusDir = fs::current_path();

    std::string version_string = "Champollion PEX decompiler " + std::string(CHAMPOLLION_VERSION_STRING);
    options::options_description desc(version_string);
    desc.add_options()
            ("help,h", "Display the help message")
            ("asm,a", options::value<std::string>()->implicit_value(""), "If defined, output assembly file(s) to this directory")
            ("psc,p", options::value<std::string>(), "Name of the output dir for psc decompilation")
            ("recursive,r", "Recursively scan directories for pex files")
            ("recreate-subdirs,s", "Recreates directory structure for script in root of output directory (Fallout 4 only, default false)")
            ("comment,c", "Output assembly in comments of the decompiled psc file")
            ("header,e", "Write header to decompiled psc file")
            ("threaded,t", "Run decompilation in parallel mode")
            ("trace,g", "Trace the decompilation and output results to rebuild log")
            ("no-dump-tree", "Do not dump tree for each node during decompilation tracing (requires --trace)")
            ("debug-funcs,d", "Decompile debug and compiler-generated functions (default false)")
            ("no-debug-line", "Do not comment with debug info line numbers on script lines (default false)")
            ("print-info,i", "Print header info from the specified PEX file(s) and exit")
            ("print-compile-time", "Print the compile time of the script in format of {filename}: {time_integer} and exit")
            ("verbose,v", "Verbose output")
            ("version,V", "Output version number")
    ;
    options::options_description files;
    files.add_options()
            ("input", options::value< std::vector<std::string> >(), "Name of the input file");

    options::positional_options_description pdesc;
    pdesc.add("input", -1);

    options::variables_map args;

    try
    {
        options::store(options::basic_command_line_parser<char>(argc, argv).options(
                           options::options_description().add(desc).add(files)
                      ).positional(pdesc).run(), args);
        options::notify(args);
    }
    catch (const std::exception& ex)
    {
        std::cout << ex.what() << std::endl;
        std::cout << desc << std::endl;
        return Invalid;
    }

    if (args.count("help"))
    {
        std::cout << desc;
        return HelpOrVersion;
    }
    if (args.count("version"))
    {
        std::cout << version_string << std::endl;
        return HelpOrVersion;
    }

    params.outputComment = (args.count("comment") != 0);
    params.writeHeader = (args.count("header") != 0);
    params.parallel = (args.count("threaded") != 0);
    params.traceDecompilation = (args.count("trace") != 0);
    params.dumpTree = params.traceDecompilation && args.count("no-dump-tree") == 0;
    params.recursive = (args.count("recursive") != 0);
    params.recreateDirStructure = (args.count("recreate-subdirs") != 0);
    params.decompileDebugFuncs = (args.count("debug-funcs") != 0);
    params.printInfo = (args.count("print-info") != 0);
    params.printCompileTime = (args.count("print-compile-time") != 0);
    params.debugLineComment = !(args.count("no-debug-line") != 0);
    params.verbose = (args.count("verbose") != 0);
    if (!params.printInfo) {
      try {
        if (args.count("asm")) {
          params.outputAssembly = true;
          auto dir = args["asm"].as<std::string>();
          if (!dir.empty()) {
            params.assemblyDir = fs::path(dir);
            if (!fs::exists(params.assemblyDir)) {
              fs::create_directories(params.assemblyDir);
            } else if (!fs::is_directory(params.assemblyDir)) {
              std::cout << params.assemblyDir << " is not a directory" << std::endl;
              return Invalid;
            }
          }
        }
        if (args.count("psc")) {
          auto dir = args["psc"].as<std::string>();

          params.papyrusDir = fs::path(dir);
          if (!fs::exists(params.papyrusDir)) {
            fs::create_directories(params.papyrusDir);
          } else if (!fs::is_directory(params.papyrusDir)) {
            std::cout << params.papyrusDir << " is not a directory" << std::endl;
            return Invalid;
          }
        }
      }
      catch (const std::exception &ex) {
        std::cout << ex.what();
        return Invalid;
      }
    }

    if(args.count("input"))
    {
        auto input_args = args["input"].as<std::vector<std::string>>();
        auto globbed_files = glob::rglob(input_args);
        for (auto in : globbed_files)
        {
            fs::path file(in);
            if (fs::exists(file))
            {
                params.inputs.push_back(file);
            }
            else
            {
                std::cout << file << " doesn't exists, skipping" << std::endl;
            }
        }
    }
    if (params.inputs.empty())
    {
        std::cout << "No input file given" << std::endl;
        return Invalid;
    }
    return Good;
}

struct _ProcessResults{
    std::vector<std::string> output;
    bool isStarfield = false;
    bool failed = false;
};

typedef _ProcessResults ProcessResults;
ProcessResults processFile(fs::path file, Params params)
{
    ProcessResults result;
    Pex::Binary pex;
    try
    {
        Pex::FileReader reader(file.string());
        reader.read(pex);
        pex.sort();
    }
    catch(std::exception& ex)
    {
       result.output.push_back(fmt::format("ERROR: {} : {}", file.string(), ex.what()));
       result.failed = true;
       return result;
    }
    pex.getGameType() == Pex::Binary::StarfieldScript ? result.isStarfield = true : result.isStarfield = false;
    if (params.printInfo)
    {
        std::string gameType;
        switch(pex.getGameType())
        {
        case Pex::Binary::SkyrimScript:
            gameType = "Skyrim";
            break;
        case Pex::Binary::Fallout4Script:
            gameType = "Fallout 4";
            break;
        case Pex::Binary::StarfieldScript:
            gameType = "Starfield";
            break;
        default:
            gameType = "Unknown";
            break;
        }

        result.output.push_back(fmt::format("Script:             {}", file.string() ));
        // print out all the info contained in the header and exit
        result.output.push_back(fmt::format("  Game:             {}", gameType));
        auto header = pex.getHeader();
        result.output.push_back(fmt::format("  Game Version:     {}.{}", header.getMajorVersion(), header.getMinorVersion()));
        result.output.push_back(fmt::format("  GameID:           {}", header.getGameID()));
        auto time = header.getCompilationTime();
        std::string hrtime = ctime(&time);
        // trim trailing line break
        hrtime.erase(hrtime.find_last_not_of("\n") + 1);
        result.output.push_back(fmt::format("  Compilation Time: {} ({}) ", time, hrtime));
        result.output.push_back(fmt::format("  Source File:      {}", header.getSourceFileName()));
        result.output.push_back(fmt::format("  User Name:        {}", header.getUserName()));
        result.output.push_back(fmt::format("  Computer Name:    {}\n", header.getComputerName()));
        return result;
    }
    if (params.printCompileTime)
    {
        auto header = pex.getHeader();
        auto time = header.getCompilationTime();
        result.output.push_back(fmt::format("{}: {}", file.string(), time));
        return result;
    }
    if (params.outputAssembly)
    {
        fs::path asmFile = params.assemblyDir / file.filename().replace_extension(".pas");
        try
        {
            std::ofstream asmStream(asmFile.string());
            Decompiler::AsmCoder asmCoder(new Decompiler::StreamWriter(asmStream));

            asmCoder.code(pex);
            result.output.push_back(fmt::format("{} dissassembled to {}", file.string(), asmFile.string()));
        }
        catch(std::exception& ex)
        {
            result.output.push_back(fmt::format("ERROR: {} : {}", file.string(), ex.what()));
            result.failed = true;
            fs::remove(asmFile);
        }
    }
    fs::path dir_structure;
    if (params.recreateDirStructure && (pex.getGameType() == Pex::Binary::Fallout4Script || pex.getGameType() == Pex::Binary::StarfieldScript) && pex.getObjects().size() > 0){
        std::string script_path = pex.getObjects()[0].getName().asString();
        std::replace(script_path.begin(), script_path.end(), ':', '/');
        dir_structure = fs::path(script_path).remove_filename();
    } else if (!params.parentDir.empty()) {
      dir_structure = fs::relative(file, params.parentDir).remove_filename();
    }
    fs::path basedir = !dir_structure.empty() ? (params.papyrusDir / dir_structure) : params.papyrusDir;
    if (!dir_structure.empty()){
        fs::create_directories(basedir);
    }
    fs::path fileName = file.filename().replace_extension(".psc");
    fs::path pscFile = basedir / fileName;
    try
    {   
        std::ofstream pscStream(pscFile);
        if (pscStream.fail()){
            throw std::runtime_error(fmt::format("Failed to open {} for writing", pscFile.string()));
        }
        Decompiler::PscCoder pscCoder(
                new Decompiler::StreamWriter(pscStream),
                params.outputComment,
                params.writeHeader,
                params.traceDecompilation,
                params.dumpTree,
                params.decompileDebugFuncs,
                params.debugLineComment,
                params.papyrusDir.string()); // using string instead of path here for C++14 compatability for staticlib targets

        pscCoder.code(pex);
        result.output.push_back(fmt::format("{} decompiled to {}", file.string(), pscFile.string()));
    }
    catch(std::exception& ex)
    {
        result.output.push_back(fmt::format("ERROR: {} : {}", file.string() , ex.what()));
        result.failed = true;
        fs::remove(pscFile);
    }
    return result;

}
size_t countFiles = 0;
size_t failedFiles = 0;
bool printStarfieldWarning = false;

void processResult(const ProcessResults &result, const Params& params)
{
    countFiles++;
    if (!printStarfieldWarning && result.isStarfield){
      printStarfieldWarning = true;
    }
    if (result.failed){
      ++failedFiles;
      for (auto line : result.output)
      {
        std::cerr << line << '\n';
      }
    } else if (params.verbose || params.printInfo || params.printCompileTime) { // only output each individual successful result if `verbose` is on
      for (auto line : result.output)
      {
        std::cout << line << '\n';
      }
    }
}


int main(int argc, char* argv[])
{

    Params args;
    auto result = getProgramOptions(argc, argv, args);
    if (result == Good)
    {
        auto start = std::chrono::steady_clock::now();
        // ignore parallel if we are printing info
        if(!args.parallel || args.printInfo || args.printCompileTime)
        {
            for (auto path : args.inputs)
            {
                if (args.recursive && fs::is_directory(path)){
                    args.parentDir = path;
                    // recursively get all files in the directory
                    for (auto& entry : fs::recursive_directory_iterator(path)){
                        if (fs::is_regular_file(entry) && caselessCompare(entry.path().extension().string().c_str(), ".pex") == 0){
                            processResult(processFile(entry, args), args);
                        }
                    }
                } else if (fs::is_directory(path)){
                    args.parentDir = fs::path();
                    fs::directory_iterator end;
                    fs::directory_iterator entry(path);
                    while(entry != end)
                    {
                        if (caselessCompare(entry->path().extension().string().c_str(), ".pex") == 0)
                        {
                            processResult(processFile(path, args), args);
                        }
                        entry++;
                    }
                }
                else
                {
                  args.parentDir = fs::path();
                  processResult(processFile(path, args), args);
                }
            }
        }
        else
        {
            std::vector<std::future<ProcessResults>> results;
            for (auto& path : args.inputs)
            {

                if (args.recursive && fs::is_directory(path)){
                  args.parentDir = path;
                  // recursively get all files in the directory
                  for (auto& entry : fs::recursive_directory_iterator(path)){
                    if (fs::is_regular_file(entry) && caselessCompare(entry.path().extension().string().c_str(), ".pex") == 0){
                        results.push_back(std::move(std::async(std::launch::async, processFile, fs::path(entry.path()), args)));
                    }
                  }
                }
                else if (fs::is_directory(path))
                {
                    args.parentDir = fs::path();
                    fs::directory_iterator end;
                    fs::directory_iterator entry(path);
                    while(entry != end)
                    {
                        if (caselessCompare(entry->path().extension().string().c_str(), ".pex") == 0)
                        {

                            results.push_back(std::move(std::async(std::launch::async, processFile, fs::path(entry->path()), args)));
                        }
                        entry++;
                    }
                }
                else
                {
                    args.parentDir = fs::path();
                    results.push_back(std::move(std::async(std::launch::async, processFile, path, args)));
                }
            }

            for (auto& result : results)
            {
                auto pResult = result.get();
                processResult(pResult, args);
            }
            countFiles = results.size();

        }
        auto end = std::chrono::steady_clock::now();
        auto diff = end - start;

        std::cout << countFiles << " files processed in " << std::chrono::duration <double> (diff).count() << " s" << std::endl;
        if (failedFiles > 0){
            std::cout << failedFiles << " files failed to decompile." << std::endl;
        }
        if (countFiles > 0 && countFiles != failedFiles){
          if (args.outputAssembly){
            std::cout << "Disassembled scripts written to " << args.assemblyDir.string() << std::endl;
          }
          std::cout << "Decompiled scripts written to " << args.papyrusDir.string() << std::endl << std::endl;
        }

        if (printStarfieldWarning){
          // TODO: Remove this warning when the CK comes out
          std::cout << "********************* STARFIELD PRELIMINARY SYNTAX WARNING *********************" << std::endl;
          std::cout << "The syntax for new features in Starfield (Guard, TryGuard, GetMatchingStructs) is not yet known." << std::endl;
          std::cout << "Decompiled Starfield scripts use guessed-at syntax for these features." << std::endl;
          std::cout << "This syntax should be considered as experimental, unstable, and subject to change." << std::endl << std::endl;
          std::cout << "The proper syntax will only be known when the Creation Kit comes out in early 2024." << std::endl;
          std::cout << "If you are using decompiled scripts as the basis for mods, please be aware of this," << std::endl;
          std::cout << "and be prepared to update your scripts when the final syntax is known." << std::endl << std::endl;
          std::cout << "The lines in the decompiled scripts which contain this guessed-at syntax are" << std::endl;
          std::cout << "marked with a comment beginning with '" << Decompiler::WARNING_COMMENT_PREFIX << "'." << std::endl;
          std::cout << "********************* STARFIELD PRELIMINARY SYNTAX WARNING *********************" << std::endl;
        }
        return 0;
    }
    if (result == HelpOrVersion){
        return 0;
    }
    return 1;
}

```

## File: `Decompiler/AsmCoder.cpp`
```cpp
#include "AsmCoder.hpp"

#include <cassert>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <ctime>
#include <map>

/**
 * @brief Constructor
 * Builds an object associated with an output writer.
 *
 * @param writer Pointer to the output writer. The ownership is transferred.
 */
Decompiler::AsmCoder::AsmCoder(Decompiler::OutputWriter *writer) :
    Coder(writer)
{
}

/**
 * @brief Default destructor.
 */
Decompiler::AsmCoder::~AsmCoder()
{
}

/**
 * @brief Disassemble a PEX binary.
 * The assembly is written to the output writer defined in the constructor.
 *
 * @param pex The binary to dissassemble.
 */
void Decompiler::AsmCoder::code(const Pex::Binary &pex)
{
    writeInfo(pex);
    writeUserFlagsRef(pex);
    writeObjectTable(pex);
}

/**
 * @brief Writes the header.
 * This function writes the content of the PEX header as an info block.
 * @param pex The source binary.
 */
void Decompiler::AsmCoder::writeInfo(const Pex::Binary &pex)
{
    auto& header = pex.getHeader();
    auto& debug  = pex.getDebugInfo();
    write(".info");
    write(indent(1) << ".source \"" << header.getSourceFileName() << "\"");
    if (debug.getModificationTime() != 0)
    {
        write(indent(1) << ".modifyTime " << debug.getModificationTime() << " ;" << std::put_time(std::localtime(&debug.getModificationTime()), "%Y-%m-%d %H:%M:%S"));
    }
    write(indent(1) << ".compileTime " << header.getCompilationTime() << " ;" << std::put_time(std::localtime(&header.getCompilationTime()), "%Y-%m-%d %H:%M:%S"));

    write(indent(1) << ".user \"" << header.getUserName() << "\"");
    write(indent(1) << ".computer \"" << header.getComputerName() << "\"");
    write(".endInfo");
}

/**
 * @brief Writes the user flag definition.
 * @param pex The source binary.
 */
void Decompiler::AsmCoder::writeUserFlagsRef(const Pex::Binary &pex)
{
    auto& flags   = pex.getUserFlags();
    write(".userFlagsRef");
    for (auto& flag : flags)
    {
        write(indent(1) << ".flag " << flag.getName().asString() << " " << (int)flag.getFlagIndex()
              << " ;0x" << std::setw(8) << std::setfill('0') << std::hex << std::uppercase << (1 << flag.getFlagIndex()));
    }
    write(".endUserFlagsRef");
}

/**
 * @brief Writes the objects definitions.
 * @param pex The source binary.
 */
void Decompiler::AsmCoder::writeObjectTable(const Pex::Binary &pex)
{
    write(".objectTable");
    for (auto& object : pex.getObjects())
    {
        write(indent(1) << ".object " << object.getName().asString() << " " << object.getParentClassName().asString());
        writeUserFlags(indent(2), object, pex);
        write(indent(2) << ".docString \"" << object.getDocString().asString() << '"');
        write(indent(2) << ".autoState " << object.getAutoStateName().asString());
        writeVariableTable(2, object, pex);
        writePropertyTable(2, object, pex);
        writeStateTable(2, object, pex);
        write(indent(1) << ".endObject");
    }
    write(".endObjectTable");
}

/**
 * @brief Writes the variable table of an object
 * @param i The indentation level.
 * @param object The object containing the variables.
 * @param pex The source binary.
 */
void Decompiler::AsmCoder::writeVariableTable(int i, const Pex::Object &object, const Pex::Binary &pex)
{
    write(indent(i) << ".variableTable");
    for (auto& var : object.getVariables())
    {
        write(indent(i+1) << ".variable " << var.getName().asString() << " " << var.getTypeName().asString());
        writeUserFlags(indent(i+2), var, pex);
        write(indent(i+2) << ".initialValue " << var.getDefaultValue().toString());
        write(indent(i+1) << ".endVariable");
    }
    write(indent(i) << ".endVariableTable");
}

/**
 * @brief Writes the properties table of an object
 * @param i The indentation level.
 * @param object The object containing the properties.
 * @param pex The source binary.
 */
void Decompiler::AsmCoder::writePropertyTable(int i, const Pex::Object &object, const Pex::Binary &pex)
{
    write(indent(i) << ".propertyTable");
    for (auto& property : object.getProperties())
    {
        //TODO:Check for auto read only
        write(indent(i+1) << ".property " << property.getName().asString() << " " << property.getTypeName().asString() << (property.hasAutoVar()?" auto":""));
        writeUserFlags(indent(i+2), property, pex);
        write(indent(i+2) << ".docString \"" << property.getDocString().asString() << '"');

        if(property.hasAutoVar())
        {
            write(indent(i+2) << ".autovar " << property.getAutoVarName().asString());
        }
        else
        {
            const auto noState = pex.getStringTable().findIdentifier("");

            if (property.isReadable())
            {
                writeFunction(i+2, property.getReadFunction(), pex, pex.getDebugInfo().getFunctionInfo(object.getName(),noState, property.getName(), Pex::DebugInfo::FunctionType::Getter), "get");
            }
            if (property.isWritable())
            {
                writeFunction(i+2, property.getWriteFunction(), pex, pex.getDebugInfo().getFunctionInfo(object.getName(), noState, property.getName(), Pex::DebugInfo::FunctionType::Setter), "set");
            }
        }
        write(indent(i+1) << ".endProperty");
    }
    write(indent(i) << ".endPropertyTable");
}

/**
 * @brief Writes the states table of an object
 * @param i The indentation level.
 * @param object The object containing the properties.
 * @param pex The source binary.
 */
void Decompiler::AsmCoder::writeStateTable(int i, const Pex::Object &object, const Pex::Binary &pex)
{
    write(indent(i) << ".stateTable");
    for (auto& state : object.getStates())
    {
        write(indent(i+1) << ".state " << state.getName().asString());
        for (auto& function : state.getFunctions())
        {
            writeFunction(i+2, function, pex, pex.getDebugInfo().getFunctionInfo(object.getName(), state.getName(), function.getName()));
        }
        write(indent(i+1) << ".endState");
    }
    write(indent(i) << ".endStateTable");
}

/**
 * @brief Writes a function
 * @param i The indentation level.
 * @param function The function to write.
 * @param pex The source binary.
 * @param info A pointer to the debug information of the function. The pointer can be null.
 * @param name Name of the function. This name overrides the name defined in the function object.
 */
void Decompiler::AsmCoder::writeFunction(int i, const Pex::Function &function, const Pex::Binary &pex, const Pex::DebugInfo::FunctionInfo *info, const std::string &name)
{
    std::string functionName(name);
    if (functionName.empty())
    {
        functionName = function.getName().asString();
    }

    write(indent(i) << ".function " << functionName);
    if (info)
    {
        write(indent(i+1) << " ; function type " << (int)info->getFunctionType());
    }
    writeUserFlags(indent(i+1), function, pex);
    write(indent(i+1) << ".docString \"" << function.getDocString().asString() << '"');

    write(indent(i+1) << ".return " << function.getReturnTypeName().asString());

    write(indent(i+1) << ".paramTable");
    for (auto& param : function.getParams())
    {
        write(indent(i+2) << ".param " << param.getName().asString() << " " << param.getTypeName().asString());
    }
    write(indent(i+1) << ".endParamTable");

    write(indent(i+1) << ".localTable");
    for (auto& local : function.getLocals())
    {
        write(indent(i+2) << ".local " << local.getName().asString() << " " << local.getTypeName().asString());
    }
    write(indent(i+1) << ".endLocalTable");

    write(indent(i+1) << ".code");
    writeCode(i+1, function.getInstructions(), info);
    write(indent(i+1) << ".endCode");


    write(indent(i) << ".endFunction " << ";" << functionName);

}

/**
 * @brief Writes the instructions of a function.
 * @param i The indentation level.
 * @param instructions The instructions list.
 * @param pex The source binary.
 * @param info A pointer to the debug information of the function. The pointer can be null.
 */
void Decompiler::AsmCoder::writeCode(int i, const Pex::Instructions &instructions, const Pex::DebugInfo::FunctionInfo *info)
{
    std::map<std::uint32_t, std::uint32_t> label;
    std::uint32_t nextLabel = 0;

    auto currentLine = -1;

    // Loop through the instruction list to find jumps
    // And compute the labels positions.
    std::uint32_t ip = 0;
    for (auto& ins : instructions)
    {
        switch(ins.getOpCode())
        {
        case Pex::OpCode::JMP:
        {
            assert(ins.getArgs().size() == 1);
            assert(ins.getArgs()[0].getType() == Pex::ValueType::Integer);

            auto target = ip + ins.getArgs()[0].getInteger();
            if (label.find(target) == label.end())
            {
                label[target] = nextLabel;
                ++nextLabel;
            }
        }
            break;
        case Pex::OpCode::JMPF:
        case Pex::OpCode::JMPT:
        {
            assert(ins.getArgs().size() == 2);
            assert(ins.getArgs()[1].getType() == Pex::ValueType::Integer);

            auto target = ip + ins.getArgs()[1].getInteger();
            if (label.find(target) == label.end())
            {
                label[target] = nextLabel;
                ++nextLabel;
            }
        }
            break;
        default:
            break;
        }

        ++ip;
    }

    // Loop through the instruction list and writes the opcodes.
    ip = 0;
    for (auto& ins : instructions)
    {
        // Check the current source line number according to the debug informations.
        if (info && ip < info->getLineNumbers().size() && info->getLineNumbers()[ip] != currentLine )
        {
            currentLine = info->getLineNumbers()[ip];
            write(indent(i+1) << "; line " << currentLine);
        }
        // Check if a label must be emitted.
        if (label.find(ip) != label.end())
        {
            write(indent(i) << "_label" << label[ip] << ':');
        }
        auto stream = indent(i + 1);
        stream << ins.getOpCodeName() << " ";
        switch(ins.getOpCode())
        {
        case Pex::OpCode::JMP:
        {
            assert(ins.getArgs().size() == 1);
            assert(ins.getArgs()[0].getType() == Pex::ValueType::Integer);

            auto target = ip + ins.getArgs()[0].getInteger();

            stream << "_label" << label[target];
        }
            break;
        case Pex::OpCode::JMPF:
        case Pex::OpCode::JMPT:
        {
            assert(ins.getArgs().size() == 2);
            assert(ins.getArgs()[1].getType() == Pex::ValueType::Integer);

            stream << ins.getArgs()[0].toString() << " ";
            auto target = ip + ins.getArgs()[1].getInteger();

            stream << "_label" << label[target];

        }
            break;
        default:
        {
            for (auto& arg : ins.getArgs())
            {
                stream << arg.toString() << " ";
            }

            if (ins.hasVarArgs())
            {
                for (auto& arg : ins.getVarArgs())
                {
                    stream << arg.toString() << " ";
                }
                stream << ";" << ins.getVarArgs().size() << " variable args";
            }
        }
            break;
        }


        write(stream.str());
        ++ip;
    }
    // Write the last label, if one.
    if (label.find(ip) != label.end())
    {
        write(indent(i) << "_label" << label[ip]);
    }
}

/**
 * @brief Writes the User Flags associated with an element to a stream.
 * @param stream The stream to write.
 * @param flagged The flagged element.
 * @param pex The source binary.
 */
void Decompiler::AsmCoder::writeUserFlags(std::ostream&& stream, const Pex::UserFlagged &flagged, const Pex::Binary &pex)
{
    auto& flagsref = pex.getUserFlags();

    auto flags = flagged.getUserFlags();

    stream << ".userFlags " << (int)flags << " ;";

    if (flags != 0x0000)
    {
        for (auto& flagref : flagsref)
        {
            if (flags & (1 << flagref.getFlagIndex()))
            {
                stream << flagref.getName().asString() << " ";
            }
        }
    }
    else
    {
        stream << "none";
    }
    auto& sstream = static_cast<std::ostringstream&>(stream);
    write(sstream.str());
}
```

## File: `Decompiler/AsmCoder.hpp`
```
#pragma once

#include "Coder.hpp"

namespace Decompiler {

/**
 * @brief Write a PEX file as an ASM file.
 */
class AsmCoder :
        public Coder
{
public:
    AsmCoder(OutputWriter* writer);
    ~AsmCoder();

    virtual void code(const Pex::Binary& pex);

protected:


    void writeInfo(const Pex::Binary& pex);
    void writeUserFlagsRef(const Pex::Binary& pex);
    void writeObjectTable(const Pex::Binary& pex);

    void writeVariableTable(int i, const Pex::Object& object, const Pex::Binary& pex);
    void writePropertyTable(int i, const Pex::Object& object, const Pex::Binary& pex);
    void writeStateTable(int i, const Pex::Object& object, const Pex::Binary& pex);

    void writeFunction(int i, const Pex::Function& function, const Pex::Binary& pex, const Pex::DebugInfo::FunctionInfo* info, const std::string& name="");
    void writeCode(int i, const Pex::Instructions& instructions, const Pex::DebugInfo::FunctionInfo *info);

    void writeUserFlags(std::ostream&& stream, const Pex::UserFlagged& flagged, const Pex::Binary& pex);

};
}
```

## File: `Decompiler/CMakeLists.txt`
```
file(GLOB HEADER_FILES "*.hpp")
file(GLOB SOURCE_FILES "*.cpp")

file(GLOB NODE_HEADER_FILES "Node/*.hpp")
file(GLOB NODE_SOURCE_FILES "Node/*.cpp")

add_library(Decompiler STATIC ${HEADER_FILES} ${SOURCE_FILES} ${NODE_HEADER_FILES} ${NODE_SOURCE_FILES})
add_dependencies(Decompiler Pex)
auto_source_group("Decompiler" ${CMAKE_CURRENT_SOURCE_DIR} ${HEADER_FILES} ${SOURCE_FILES} ${NODE_HEADER_FILES} ${NODE_SOURCE_FILES})
```

## File: `Decompiler/Coder.cpp`
```cpp
#include "Coder.hpp"
#include <cassert>


/**
 * @brief Constructor
 * Builds an coder associated with an output writer.
 *
 * @param writer Pointer to the writer managing the output. The ownership is transferred.
 */
Decompiler::Coder::Coder(Decompiler::OutputWriter *writer) :
    m_Writer(writer)
{
    assert(writer != nullptr);
}

/**
 * @brief Default destructor.
 */
Decompiler::Coder::~Coder()
{
}

/**
 * @brief Write a string to the output
 * @param line String to write.
 */
void Decompiler::Coder::write(const std::string &line)
{
    m_Writer->writeLine(line);
}
template<class T> static constexpr bool IsAnOstream = std::is_base_of<std::decay_t<T>, std::ostream>::value;
template<class T> static constexpr bool IsAnOStringstream = std::is_base_of<std::decay_t<T>, std::ostringstream>::value;

/**
 * @brief Write the content of a ostringstream.
 * The ostringstream is passed as an ostream. This is intended
 * to write output in the form
 *  write(indent(i) << "line data");
 * @param stream The stream as an ostream.
 */
void Decompiler::Coder::write(std::ostream&& stream)
{
    auto& sstream = static_cast<std::ostringstream&>(stream);
    m_Writer->writeLine(sstream.str());
}

/**
 * @brief Creates an ostringstream and prepare it with identation.
 * @param i Indentation level to apply.
 * @return
 */
std::ostringstream Decompiler::Coder::indent(int i)
{
    std::ostringstream result;
    for(; i != 0; --i)
    {
        result << ' ' << ' ';
    }
    return result;
}
```

## File: `Decompiler/Coder.hpp`
```
#pragma once

#include <memory>
#include <sstream>

#include "OutputWriter.hpp"
#include "Pex/Binary.hpp"

namespace Decompiler {
/**
 * @brief Base class for program writer
 *
 * This base class handles the low level writing procedure
 * for class rewriting programs.
 */
class Coder
{
public:
    Coder(OutputWriter* writer);
    virtual ~Coder();

    virtual void code(const Pex::Binary& pex) = 0;

protected:
    void write(const std::string& line);
    void write(std::ostream&& stream);


    std::ostringstream indent(int i);

    std::unique_ptr<OutputWriter> m_Writer;
};
}
```

## File: `Decompiler/DumpTree.hpp`
```
#pragma once

#include <cassert>
#include <functional>
#include <sstream>

#include "Node/Nodes.hpp"

namespace Decompiler
{
/**
 * @brief Inline node visitor dumping the tree for debug purposes.
 *
 * The output is made using a callback function taking a ostring stream as it's input.
 */
class DumpTree : public Node::VisitorBase
{
private:
    std::function<void (std::ostringstream stream)> m_Callback;
    std::uint32_t m_Indent;
public:
    DumpTree(decltype(m_Callback) callback) :
        m_Callback(callback),
        m_Indent(0)
    {
        assert(callback);
    }

    virtual ~DumpTree()
    {

    }
    std::ostringstream indent()
    {
        std::ostringstream result;
        result << ";";
        for (uint32_t i = 0; i < m_Indent; ++i)
        {
            result << " ";
        }
        return result;
    }

    void enter(const char* text, Node::Base* node)
    {
        m_Callback((indent() << text << "<" << node << "> (" << node->getBegin() << "," << node->getEnd() << ")"));
        ++m_Indent;
    }
    void leave()
    {
        --m_Indent;
        m_Callback(indent() << "]");
    }

    virtual void visit(Node::Scope* node)
    {
        enter("Scope", node);
        VisitorBase::visit(node);
        leave();
    }

    virtual void visit(Node::BinaryOperator* node)
    {
        enter("Binary", node);
        m_Callback(indent() << "In:" << node->getResult()) ;
        m_Callback(indent() << "Left:");
        node->getLeft()->visit(this);
        m_Callback(indent() << "Op:" << node->getOperator() << " P:" << (int)node->getPrecedence());
        m_Callback(indent() << "Right:");
        node->getRight()->visit(this);
        leave();
    }

    virtual void visit(Node::UnaryOperator* node)
    {
        enter("Unary", node);
        m_Callback(indent() << "Op:" << node->getOperator() << " P:" << (int)node->getPrecedence());
        m_Callback(indent() << "Value:");
        node->getValue()->visit(this);
        leave();
    }
    virtual void visit(Node::Assign* node)
    {
        enter("Assign", node);
        m_Callback(indent() << "In:");
        node->getDestination()->visit(this);
        m_Callback(indent() << "Value:");
        node->getValue()->visit(this);
        leave();
    }

    virtual void visit(Node::AssignOperator* node)
    {
        enter("AssignOperator", node);
        m_Callback(indent() << "In:");
        node->getDestination()->visit(this);
        m_Callback(indent() << "Operator:" << node->getOperator());
        m_Callback(indent() << "Value:");
        node->getValue()->visit(this);
        leave();
    }
    virtual void visit(Node::Copy* node)
    {
        enter("Copy", node);
        m_Callback(indent() << "In:" << node->getResult());
        m_Callback(indent() << "Value:");
        node->getValue()->visit(this);
        leave();
    }
    virtual void visit(Node::Cast* node)
    {
        enter("Cast", node);
        m_Callback(indent() << "In:" << node->getResult());
        m_Callback(indent() << "As:" << node->getType());
        m_Callback(indent() << "Value:");
        node->getValue()->visit(this);
        leave();
    }

    virtual void visit(Node::CallMethod* node)
    {
        enter("Call", node);
        m_Callback(indent() << "In:" << node->getResult());
        m_Callback(indent() << "Method:" << node->getMethod());
        m_Callback(indent() << "On:");
        node->getObject()->visit(this);
        for (auto param : *node->getParameters())
        {
            m_Callback(indent() << "Param:");
            param->visit(this);
        }
        leave();
    }

    virtual void visit(Node::Params* node)
    {
        enter("Params", node);
        VisitorBase::visit(node);
        leave();
    }

    virtual void visit(Node::Return* node)
    {
        enter("Return", node);
        m_Callback(indent() << "Value:");
        if (node->getValue()) {
            node->getValue()->visit(this);
        } else {
            m_Callback(indent() << "<NONE>");
        }
        leave();
    }

    virtual void visit(Node::PropertyAccess* node)
    {
        enter("PropertyAccess", node);
        m_Callback(indent() << "In:" << node->getResult());
        m_Callback(indent() << "Property:" << node->getProperty());
        m_Callback(indent() << "On:");
        node->getObject()->visit(this);
        leave();
    }

    virtual void visit(Node::ArrayCreate* node)
    {
        enter("ArrayCreate", node);
        m_Callback(indent() << "Type:" << node->getType());
        //m_Callback(indent() << "Size:" << node->getSize()); // TODO: Add size back to ArrayCreate?
        leave();
    }

    virtual void visit(Node::ArrayLength* node)
    {
        enter("ArrayLength", node);
        m_Callback(indent() << "Array:");
        node->getArray()->visit(this);
        leave();
    }

    virtual void visit(Node::ArrayAccess* node)
    {
        enter("ArrayAccess", node);
        m_Callback(indent() << "In:" << node->getResult());
        m_Callback(indent() << "Array:");
        node->getArray()->visit(this);
        m_Callback(indent() << "Index:");
        node->getIndex()->visit(this);
        leave();
    }

    virtual void visit(Node::Constant* node)
    {
        auto& value = node->getConstant();
        enter("Constant", node);

        switch(value.getType())
        {
        case Pex::ValueType::None:
        {
           m_Callback(indent() << "None:none");
        }
            break;
        case Pex::ValueType::Identifier:
        {
            m_Callback(indent() << "Identifier:" << value.getId());
        }
            break;
        case Pex::ValueType::String:
        {
            m_Callback(indent() << "String:" << value.getString());
        }
            break;
        case Pex::ValueType::Integer:
        {
            m_Callback(indent() << "Integer:" << value.getInteger());
        }
            break;
        case Pex::ValueType::Float:
        {
            m_Callback(indent() << "Float:" <<  std::showpoint << value.getFloat());
        }
            break;
        case Pex::ValueType::Bool:
        {
            m_Callback(indent() << "Bool:" << (value.getBool()?"true":"false"));
        }
            break;
        }
        leave();
    }

    virtual void visit(Node::IdentifierString* node)
    {
        enter("IdentifierString", node);
        m_Callback(indent() << "Id:" << node->getIdentifier());
        leave();
    }

    virtual void visit(Node::While* node)
    {
        enter("While", node);
        m_Callback(indent() << "Condition:");
        node->getCondition()->visit(this);
        m_Callback(indent() << "Body:");
        node->getBody()->visit(this);
        leave();
    }

    virtual void visit(Node::IfElse* node)
    {
        enter("If", node);
        m_Callback(indent() << "Condition:");
        node->getCondition()->visit(this);
        m_Callback(indent() << "Body:");
        node->getBody()->visit(this);
        m_Callback(indent() << "ElseIf:");
        node->getElseIf()->visit(this);
        m_Callback(indent() << "Else:");
        node->getElse()->visit(this);
        leave();
    }

    virtual void visit(Node::Declare* node)
    {
        enter("Declare", node);
        m_Callback(indent() << "Type:" << node->getType());
        m_Callback(indent() << "Name:");
        node->getObject()->visit(this);
        leave();
    }

    virtual void visit(Node::GuardStatement* node)
    {
        enter("Guard", node);
        for (auto param : *node->getParameters())
        {
            m_Callback(indent() << "Param:");
            param->visit(this);
        }
        m_Callback(indent() << "Body:");
        node->getBody()->visit(this);
        leave();
    }
    virtual void visit(Node::TryGuard* node)
    {
        enter("TryGuard", node);
        for (auto param : *node->getParameters())
        {
            m_Callback(indent() << "Param:");
            param->visit(this);
        }
        m_Callback(indent() << "Body:");
        node->getBody()->visit(this);
        leave();
    }
    virtual void visit(Node::EndGuard* node)
    {
        enter("EndGuard", node);
        for (auto param : *node->getParameters())
        {
            m_Callback(indent() << "Param:");
            param->visit(this);
        }
        leave();
    }
};

}
```

## File: `Decompiler/EventNames.hpp`
```
#pragma once
#include <vector>
#include <string>

namespace Decompiler{
	namespace Skyrim {
        static const std::vector<std::string> NativeClasses ={};
		static const std::vector<std::string> EventNames = {
			"OnAnimationEvent", // ActiveMagicEffect
			"OnAnimationEventUnregistered", // ActiveMagicEffect
			"OnEffectFinish", // ActiveMagicEffect
			"OnEffectStart", // ActiveMagicEffect
			"OnGainLOS", // ActiveMagicEffect
			"OnLostLOS", // ActiveMagicEffect
			"OnUpdate", // ActiveMagicEffect
			"OnCombatStateChanged", // Actor
			"OnDeath", // Actor
			"OnDying", // Actor
			"OnEnterBleedout", // Actor
			"OnGetUp", // Actor
			"OnLocationChange", // Actor
			"OnLycanthropyStateChanged", // Actor
			"OnObjectEquipped", // Actor
			"OnObjectUnequipped", // Actor
			"OnPackageChange", // Actor
			"OnPackageEnd", // Actor
			"OnPackageStart", // Actor
			"OnPlayerBowShot", // Actor
			"OnPlayerFastTravelEnd", // Actor
			"OnPlayerLoadGame", // Actor
			"OnRaceSwitchComplete", // Actor
			"OnSit", // Actor
			"OnVampireFeed", // Actor
			"OnVampirismStateChanged", // Actor
			"OnAnimationEvent", // Alias
			"OnAnimationEventUnregistered", // Alias
			"OnGainLOS", // Alias
			"OnLostLOS", // Alias
			"OnReset", // Alias
			"OnUpdate", // Alias
			"OnAnimationEvent", // Form
			"OnAnimationEventUnregistered", // Form
			"OnGainLOS", // Form
			"OnLostLOS", // Form
			"OnSleepStart", // Form
			"OnSleepStop", // Form
			"OnTrackedStatsEvent", // Form
			"OnUpdate", // Form
			"OnUpdateGameTime", // Form
			"OnActivate", // ObjectReference
			"OnAttachedToCell", // ObjectReference
			"OnCellAttach", // ObjectReference
			"OnCellDetach", // ObjectReference
			"OnCellLoad", // ObjectReference
			"OnClose", // ObjectReference
			"OnContainerChanged", // ObjectReference
			"OnDestructionStageChanged", // ObjectReference
			"OnDetachedFromCell", // ObjectReference
			"OnEquipped", // ObjectReference
			"OnGrab", // ObjectReference
			"OnHit", // ObjectReference
			"OnItemAdded", // ObjectReference
			"OnItemRemoved", // ObjectReference
			"OnLoad", // ObjectReference
			"OnLockStateChanged", // ObjectReference
			"OnMagicEffectApply", // ObjectReference
			"OnOpen", // ObjectReference
			"OnRead", // ObjectReference
			"OnRelease", // ObjectReference
			"OnReset", // ObjectReference
			"OnSell", // ObjectReference
			"OnSpellCast", // ObjectReference
			"OnTranslationAlmostComplete", // ObjectReference
			"OnTranslationComplete", // ObjectReference
			"OnTranslationFailed", // ObjectReference
			"OnTrapHit", // ObjectReference
			"OnTrapHitStart", // ObjectReference
			"OnTrapHitStop", // ObjectReference
			"OnTrigger", // ObjectReference
			"OnTriggerEnter", // ObjectReference
			"OnTriggerLeave", // ObjectReference
			"OnUnequipped", // ObjectReference
			"OnUnload", // ObjectReference
			"OnWardHit", // ObjectReference
			"OnReset", // Quest
			"OnStoryActivateActor", // Quest
			"OnStoryAddToPlayer", // Quest
			"OnStoryArrest", // Quest
			"OnStoryAssaultActor", // Quest
			"OnStoryBribeNPC", // Quest
			"OnStoryCastMagic", // Quest
			"OnStoryChangeLocation", // Quest
			"OnStoryCraftItem", // Quest
			"OnStoryCrimeGold", // Quest
			"OnStoryCure", // Quest
			"OnStoryDialogue", // Quest
			"OnStoryDiscoverDeadBody", // Quest
			"OnStoryEscapeJail", // Quest
			"OnStoryFlatterNPC", // Quest
			"OnStoryHello", // Quest
			"OnStoryIncreaseLevel", // Quest
			"OnStoryIncreaseSkill", // Quest
			"OnStoryInfection", // Quest
			"OnStoryIntimidateNPC", // Quest
			"OnStoryJail", // Quest
			"OnStoryKillActor", // Quest
			"OnStoryNewVoicePower", // Quest
			"OnStoryPayFine", // Quest
			"OnStoryPickLock", // Quest
			"OnStoryPlayerGetsFavor", // Quest
			"OnStoryRelationshipChange", // Quest
			"OnStoryRemoveFromPlayer", // Quest
			"OnStoryScript", // Quest
			"OnStoryServedTime", // Quest
			"OnStoryTrespass", // Quest
			"OnBeginState",
			"OnEndState",
			"OnInit"
		};
        static const std::vector<std::string> EventNamesLowerCase = {
			"onanimationevent", // ActiveMagicEffect
			"onanimationeventunregistered", // ActiveMagicEffect
			"oneffectfinish", // ActiveMagicEffect
			"oneffectstart", // ActiveMagicEffect
			"ongainlos", // ActiveMagicEffect
			"onlostlos", // ActiveMagicEffect
			"onupdate", // ActiveMagicEffect
			"oncombatstatechanged", // Actor
			"ondeath", // Actor
			"ondying", // Actor
			"onenterbleedout", // Actor
			"ongetup", // Actor
			"onlocationchange", // Actor
			"onlycanthropystatechanged", // Actor
			"onobjectequipped", // Actor
			"onobjectunequipped", // Actor
			"onpackagechange", // Actor
			"onpackageend", // Actor
			"onpackagestart", // Actor
			"onplayerbowshot", // Actor
			"onplayerfasttravelend", // Actor
			"onplayerloadgame", // Actor
			"onraceswitchcomplete", // Actor
			"onsit", // Actor
			"onvampirefeed", // Actor
			"onvampirismstatechanged", // Actor
			"onanimationevent", // Alias
			"onanimationeventunregistered", // Alias
			"ongainlos", // Alias
			"onlostlos", // Alias
			"onreset", // Alias
			"onupdate", // Alias
			"onanimationevent", // Form
			"onanimationeventunregistered", // Form
			"ongainlos", // Form
			"onlostlos", // Form
			"onsleepstart", // Form
			"onsleepstop", // Form
			"ontrackedstatsevent", // Form
			"onupdate", // Form
			"onupdategametime", // Form
			"onactivate", // ObjectReference
			"onattachedtocell", // ObjectReference
			"oncellattach", // ObjectReference
			"oncelldetach", // ObjectReference
			"oncellload", // ObjectReference
			"onclose", // ObjectReference
			"oncontainerchanged", // ObjectReference
			"ondestructionstagechanged", // ObjectReference
			"ondetachedfromcell", // ObjectReference
			"onequipped", // ObjectReference
			"ongrab", // ObjectReference
			"onhit", // ObjectReference
			"onitemadded", // ObjectReference
			"onitemremoved", // ObjectReference
			"onload", // ObjectReference
			"onlockstatechanged", // ObjectReference
			"onmagiceffectapply", // ObjectReference
			"onopen", // ObjectReference
			"onread", // ObjectReference
			"onrelease", // ObjectReference
			"onreset", // ObjectReference
			"onsell", // ObjectReference
			"onspellcast", // ObjectReference
			"ontranslationalmostcomplete", // ObjectReference
			"ontranslationcomplete", // ObjectReference
			"ontranslationfailed", // ObjectReference
			"ontraphit", // ObjectReference
			"ontraphitstart", // ObjectReference
			"ontraphitstop", // ObjectReference
			"ontrigger", // ObjectReference
			"ontriggerenter", // ObjectReference
			"ontriggerleave", // ObjectReference
			"onunequipped", // ObjectReference
			"onunload", // ObjectReference
			"onwardhit", // ObjectReference
			"onreset", // Quest
			"onstoryactivateactor", // Quest
			"onstoryaddtoplayer", // Quest
			"onstoryarrest", // Quest
			"onstoryassaultactor", // Quest
			"onstorybribenpc", // Quest
			"onstorycastmagic", // Quest
			"onstorychangelocation", // Quest
			"onstorycraftitem", // Quest
			"onstorycrimegold", // Quest
			"onstorycure", // Quest
			"onstorydialogue", // Quest
			"onstorydiscoverdeadbody", // Quest
			"onstoryescapejail", // Quest
			"onstoryflatternpc", // Quest
			"onstoryhello", // Quest
			"onstoryincreaselevel", // Quest
			"onstoryincreaseskill", // Quest
			"onstoryinfection", // Quest
			"onstoryintimidatenpc", // Quest
			"onstoryjail", // Quest
			"onstorykillactor", // Quest
			"onstorynewvoicepower", // Quest
			"onstorypayfine", // Quest
			"onstorypicklock", // Quest
			"onstoryplayergetsfavor", // Quest
			"onstoryrelationshipchange", // Quest
			"onstoryremovefromplayer", // Quest
			"onstoryscript", // Quest
			"onstoryservedtime", // Quest
			"onstorytrespass", // Quest
			"onbeginstate",
			"onendstate",
			"oninit"
		};
	}
	namespace Fallout4{
        static const std::vector<std::string> NativeClasses ={
                "Action",
                "Activator",
                "ActiveMagicEffect",
                "Actor",
                "ActorBase",
                "ActorValue",
                "Alias",
                "Ammo",
                "Armor",
                "AssociationType",
                "Book",
                "CameraShot",
                "Cell",
                "Class",
                "CombatStyle",
                "Component",
                "ConstructibleObject",
                "Container",
                "Debug",
                "Door",
                "EffectShader",
                "Enchantment",
                "EncounterZone",
                "Explosion",
                "Faction",
                "Flora",
                "Form",
                "FormList",
                "Furniture",
                "Game",
                "GlobalVariable",
                "Hazard",
                "HeadPart",
                "Holotape",
                "Idle",
                "IdleMarker",
                "ImageSpaceModifier",
                "ImpactDataSet",
                "Ingredient",
                "InputEnableLayer",
                "InstanceNamingRules",
                "Key",
                "Keyword",
                "LeveledActor",
                "LeveledItem",
                "LeveledSpell",
                "Light",
                "Location",
                "LocationAlias",
                "LocationRefType",
                "MagicEffect",
                "Math",
                "Message",
                "MiscObject",
                "MovableStatic",
                "MusicType",
                "ObjectMod",
                "ObjectReference",
                "Outfit",
                "OutputModel",
                "Package",
                "Perk",
                "Potion",
                "Projectile",
                "Quest",
                "Race",
                "RefCollectionAlias",
                "ReferenceAlias",
                "Scene",
                "ScriptObject",
                "Scroll",
                "ShaderParticleGeometry",
                "Shout",
                "SoulGem",
                "Sound",
                "SoundCategory",
                "SoundCategorySnapshot",
                "Spell",
                "Static",
                "TalkingActivator",
                "Terminal",
                "TextureSet",
                "Topic",
                "TopicInfo",
                "Utility",
                "VisualEffect",
                "VoiceType",
                "Weapon",
                "Weather",
                "WordOfPower",
                "WorldSpace",
        };
		static const std::vector<std::string> EventNames = {
			"OnEffectFinish", // ActiveMagicEffect
			"OnEffectStart", // ActiveMagicEffect
			"OnCombatStateChanged", // Actor
			"OnCommandModeCompleteCommand", // Actor
			"OnCommandModeEnter", // Actor
			"OnCommandModeExit", // Actor
			"OnCommandModeGiveCommand", // Actor
			"OnCompanionDismiss", // Actor
			"OnConsciousnessStateChanged", // Actor
			"OnCripple", // Actor
			"OnDeath", // Actor
			"OnDeferredKill", // Actor
			"OnDifficultyChanged", // Actor
			"OnDying", // Actor
			"OnEnterBleedout", // Actor
			"OnEnterSneaking", // Actor
			"OnEscortWaitStart", // Actor
			"OnEscortWaitStop", // Actor
			"OnGetUp", // Actor
			"OnItemEquipped", // Actor
			"OnItemUnequipped", // Actor
			"OnKill", // Actor
			"OnLocationChange", // Actor
			"OnPackageChange", // Actor
			"OnPackageEnd", // Actor
			"OnPackageStart", // Actor
			"OnPartialCripple", // Actor
			"OnPickpocketFailed", // Actor
			"OnPlayerCreateRobot", // Actor
			"OnPlayerEnterVertibird", // Actor
			"OnPlayerFallLongDistance", // Actor
			"OnPlayerFireWeapon", // Actor
			"OnPlayerHealTeammate", // Actor
			"OnPlayerLoadGame", // Actor
			"OnPlayerModArmorWeapon", // Actor
			"OnPlayerModRobot", // Actor
			"OnPlayerSwimming", // Actor
			"OnPlayerUseWorkBench", // Actor
			"OnRaceSwitchComplete", // Actor
			"OnSit", // Actor
			"OnSpeechChallengeAvailable", // Actor
			"OnAliasInit", // Alias
			"OnAliasReset", // Alias
			"OnAliasShutdown", // Alias
			"OnLocationCleared", // Location
			"OnLocationLoaded", // Location
			"OnActivate", // ObjectReference
			"OnCellAttach", // ObjectReference
			"OnCellDetach", // ObjectReference
			"OnCellLoad", // ObjectReference
			"OnClose", // ObjectReference
			"OnContainerChanged", // ObjectReference
			"OnDestructionStageChanged", // ObjectReference
			"OnEquipped", // ObjectReference
			"OnExitFurniture", // ObjectReference
			"OnGrab", // ObjectReference
			"OnHolotapeChatter", // ObjectReference
			"OnHolotapePlay", // ObjectReference
			"OnItemAdded", // ObjectReference
			"OnItemRemoved", // ObjectReference
			"OnLoad", // ObjectReference
			"OnLockStateChanged", // ObjectReference
			"OnOpen", // ObjectReference
			"OnPipboyRadioDetection", // ObjectReference
			"OnPlayerDialogueTarget", // ObjectReference
			"OnPowerOff", // ObjectReference
			"OnPowerOn", // ObjectReference
			"OnRead", // ObjectReference
			"OnRelease", // ObjectReference
			"OnReset", // ObjectReference
			"OnSell", // ObjectReference
			"OnSpellCast", // ObjectReference
			"OnTranslationAlmostComplete", // ObjectReference
			"OnTranslationComplete", // ObjectReference
			"OnTranslationFailed", // ObjectReference
			"OnTrapHitStart", // ObjectReference
			"OnTrapHitStop", // ObjectReference
			"OnTriggerEnter", // ObjectReference
			"OnTriggerLeave", // ObjectReference
			"OnUnequipped", // ObjectReference
			"OnUnload", // ObjectReference
			"OnWorkshopMode", // ObjectReference
			"OnWorkshopNPCTransfer", // ObjectReference
			"OnWorkshopObjectDestroyed", // ObjectReference
			"OnWorkshopObjectGrabbed", // ObjectReference
			"OnWorkshopObjectMoved", // ObjectReference
			"OnWorkshopObjectPlaced", // ObjectReference
			"OnWorkshopObjectRepaired", // ObjectReference
			"OnChange", // Package
			"OnEnd", // Package
			"OnStart", // Package
			"OnEntryRun", // Perk
			"OnQuestInit", // Quest
			"OnQuestShutdown", // Quest
			"OnStageSet", // Quest
			"OnStoryIncreaseLevel", // Quest
			"OnAction", // Scene
			"OnBegin", // Scene
			"OnEnd", // Scene
			"OnPhaseBegin", // Scene
			"OnPhaseEnd", // Scene
			"OnAnimationEvent", // ScriptObject
			"OnAnimationEventUnregistered", // ScriptObject
			"OnBeginState", // ScriptObject
			"OnControlDown", // ScriptObject
			"OnControlUp", // ScriptObject
			"OnDistanceGreaterThan", // ScriptObject
			"OnDistanceLessThan", // ScriptObject
			"OnEndState", // ScriptObject
			"OnFurnitureEvent", // ScriptObject
			"OnGainLOS", // ScriptObject
			"OnHit", // ScriptObject
			"OnInit", // ScriptObject
			"OnKeyDown", // ScriptObject
			"OnKeyUp", // ScriptObject
			"OnLooksMenuEvent", // ScriptObject
			"OnLostLOS", // ScriptObject
			"OnMagicEffectApply", // ScriptObject
			"OnMenuOpenCloseEvent", // ScriptObject
			"OnPlayerCameraState", // ScriptObject
			"OnPlayerSleepStart", // ScriptObject
			"OnPlayerSleepStop", // ScriptObject
			"OnPlayerTeleport", // ScriptObject
			"OnPlayerWaitStart", // ScriptObject
			"OnPlayerWaitStop", // ScriptObject
			"OnRadiationDamage", // ScriptObject
			"OnTimer", // ScriptObject
			"OnTimerGameTime", // ScriptObject
			"OnTrackedStatsEvent", // ScriptObject
			"OnTutorialEvent", // ScriptObject
			"OnMenuItemRun", // Terminal
			"OnBegin", // TopicInfo
			"OnEnd", // TopicInfo
        };

		static const std::vector<std::string> EventNamesLowerCase = {
			"oneffectfinish", // ActiveMagicEffect
			"oneffectstart", // ActiveMagicEffect
			"oncombatstatechanged", // Actor
			"oncommandmodecompletecommand", // Actor
			"oncommandmodeenter", // Actor
			"oncommandmodeexit", // Actor
			"oncommandmodegivecommand", // Actor
			"oncompaniondismiss", // Actor
			"onconsciousnessstatechanged", // Actor
			"oncripple", // Actor
			"ondeath", // Actor
			"ondeferredkill", // Actor
			"ondifficultychanged", // Actor
			"ondying", // Actor
			"onenterbleedout", // Actor
			"onentersneaking", // Actor
			"onescortwaitstart", // Actor
			"onescortwaitstop", // Actor
			"ongetup", // Actor
			"onitemequipped", // Actor
			"onitemunequipped", // Actor
			"onkill", // Actor
			"onlocationchange", // Actor
			"onpackagechange", // Actor
			"onpackageend", // Actor
			"onpackagestart", // Actor
			"onpartialcripple", // Actor
			"onpickpocketfailed", // Actor
			"onplayercreaterobot", // Actor
			"onplayerentervertibird", // Actor
			"onplayerfalllongdistance", // Actor
			"onplayerfireweapon", // Actor
			"onplayerhealteammate", // Actor
			"onplayerloadgame", // Actor
			"onplayermodarmorweapon", // Actor
			"onplayermodrobot", // Actor
			"onplayerswimming", // Actor
			"onplayeruseworkbench", // Actor
			"onraceswitchcomplete", // Actor
			"onsit", // Actor
			"onspeechchallengeavailable", // Actor
			"onaliasinit", // Alias
			"onaliasreset", // Alias
			"onaliasshutdown", // Alias
			"onlocationcleared", // Location
			"onlocationloaded", // Location
			"onactivate", // ObjectReference
			"oncellattach", // ObjectReference
			"oncelldetach", // ObjectReference
			"oncellload", // ObjectReference
			"onclose", // ObjectReference
			"oncontainerchanged", // ObjectReference
			"ondestructionstagechanged", // ObjectReference
			"onequipped", // ObjectReference
			"onexitfurniture", // ObjectReference
			"ongrab", // ObjectReference
			"onholotapechatter", // ObjectReference
			"onholotapeplay", // ObjectReference
			"onitemadded", // ObjectReference
			"onitemremoved", // ObjectReference
			"onload", // ObjectReference
			"onlockstatechanged", // ObjectReference
			"onopen", // ObjectReference
			"onpipboyradiodetection", // ObjectReference
			"onplayerdialoguetarget", // ObjectReference
			"onpoweroff", // ObjectReference
			"onpoweron", // ObjectReference
			"onread", // ObjectReference
			"onrelease", // ObjectReference
			"onreset", // ObjectReference
			"onsell", // ObjectReference
			"onspellcast", // ObjectReference
			"ontranslationalmostcomplete", // ObjectReference
			"ontranslationcomplete", // ObjectReference
			"ontranslationfailed", // ObjectReference
			"ontraphitstart", // ObjectReference
			"ontraphitstop", // ObjectReference
			"ontriggerenter", // ObjectReference
			"ontriggerleave", // ObjectReference
			"onunequipped", // ObjectReference
			"onunload", // ObjectReference
			"onworkshopmode", // ObjectReference
			"onworkshopnpctransfer", // ObjectReference
			"onworkshopobjectdestroyed", // ObjectReference
			"onworkshopobjectgrabbed", // ObjectReference
			"onworkshopobjectmoved", // ObjectReference
			"onworkshopobjectplaced", // ObjectReference
			"onworkshopobjectrepaired", // ObjectReference
			"onchange", // Package
			"onend", // Package
			"onstart", // Package
			"onentryrun", // Perk
			"onquestinit", // Quest
			"onquestshutdown", // Quest
			"onstageset", // Quest
			"onstoryincreaselevel", // Quest
			"onaction", // Scene
			"onbegin", // Scene
			"onend", // Scene
			"onphasebegin", // Scene
			"onphaseend", // Scene
			"onanimationevent", // ScriptObject
			"onanimationeventunregistered", // ScriptObject
			"onbeginstate", // ScriptObject
			"oncontroldown", // ScriptObject
			"oncontrolup", // ScriptObject
			"ondistancegreaterthan", // ScriptObject
			"ondistancelessthan", // ScriptObject
			"onendstate", // ScriptObject
			"onfurnitureevent", // ScriptObject
			"ongainlos", // ScriptObject
			"onhit", // ScriptObject
			"oninit", // ScriptObject
			"onkeydown", // ScriptObject
			"onkeyup", // ScriptObject
			"onlooksmenuevent", // ScriptObject
			"onlostlos", // ScriptObject
			"onmagiceffectapply", // ScriptObject
			"onmenuopencloseevent", // ScriptObject
			"onplayercamerastate", // ScriptObject
			"onplayersleepstart", // ScriptObject
			"onplayersleepstop", // ScriptObject
			"onplayerteleport", // ScriptObject
			"onplayerwaitstart", // ScriptObject
			"onplayerwaitstop", // ScriptObject
			"onradiationdamage", // ScriptObject
			"ontimer", // ScriptObject
			"ontimergametime", // ScriptObject
			"ontrackedstatsevent", // ScriptObject
			"ontutorialevent", // ScriptObject
			"onmenuitemrun", // Terminal
			"onbegin", // TopicInfo
			"onend", // TopicInfo
		};
	}
    namespace Starfield {
        static const std::vector<std::string> NativeClasses = {
                //Forms
                "Action",
                "Activator",
                "ActiveMagicEffect",
                "Actor",
                "ActorBase",
                "ActorValue",
                "AffinityEvent",
                "Alias",
                "Ammo",
                "Armor",
                "AssociationType",
                "Book",
                "CameraShot",
                "Cell",
                "Challenge",
                "Class",
                "CombatStyle",
                "ConditionForm",
                "ConstructibleObject",
                "Container",
                "Curve",
                "Debug",
                "Door",
                "EffectShader",
                "Enchantment",
                "Explosion",
                "Faction",
                "Flora",
                "Form",
                "FormList",
                "Furniture",
                "GlobalVariable",
                "Hazard",
                "HeadPart",
                "Idle",
                "IdleMarker",
                "ImageSpaceModifier",
                "ImpactDataSet",
                "Ingredient",
                "InputEnableLayer",
                "InstanceNamingRules",
                "Key",
                "Keyword",
                "LegendaryItem",
                "LeveledActor",
                "LeveledItem",
                "LeveledSpaceshipBase",
                "LeveledSpell",
                "Light",
                "Location",
                "LocationAlias",
                "LocationRefType",
                "MagicEffect",
                "Message",
                "MiscObject",
                "MovableStatic",
                "MusicType",
                "Note",
                "ObjectMod",
                "ObjectReference",
                "Outfit",
                "Package",
                "PackIn",
                "Perk",
                "Planet",
                "Potion",
                "Projectile",
                "Quest",
                "Race",
                "RefCollectionAlias",
                "ReferenceAlias",
                "ResearchProject",
                "Resource",
                "Scene",
                "Scroll",
                "ShaderParticleGeometry",
                "Shout",
                "SoulGem",
                "SpaceshipBase",
                "SpaceshipReference",
                "Spell",
                "Static",
                "TalkingActivator",
                "Terminal",
                "TerminalMenu",
                "TextureSet",
                "Topic",
                "TopicInfo",
                "VisualEffect",
                "VoiceType",
                "Weapon",
                "Weather",
                "WordOfPower",
                "WorldSpace",
                "WwiseEvent",
                // Non Form Natives
                "SpeechChallengeObject",
                "Game",
                "Math",
                "ScriptObject",
                "Utility",
        };
        static const std::vector<std::string> EventNames = {
                "OnAction",
                "OnActivate",
                "OnActorActivatedRef",
                "OnActorValueChanged",
                "OnActorValueGreaterThan",
                "OnActorValueLessThan",
                "OnAffinityEvent",
                "OnAffinityEventSent",
                "OnAliasChanged",
                "OnAliasInit",
                "OnAliasReset",
                "OnAliasShutdown",
                "OnAliasStarted",
                "OnAnimationEvent",
                "OnAnimationEventUnregistered",
                "OnBegin",
                "OnBeginState",
                "OnBuilderMenuSelect",
                "OnCellAttach",
                "OnCellDetach",
                "OnCellLoad",
                "OnChallengeCompleted",
                "OnChange",
                "OnClose",
                "OnCombatListAdded",
                "OnCombatListRemoved",
                "OnCombatStateChanged",
                "OnCommandModeCompleteCommand",
                "OnCommandModeEnter",
                "OnCommandModeExit",
                "OnCommandModeGiveCommand",
                "OnCompanionDismiss",
                "OnConsciousnessStateChanged",
                "OnContainerChanged",
                "OnCrewAssigned",
                "OnCrewDismissed",
                "OnCripple",
                "OnDeath",
                "OnDeferredKill",
                "OnDestroyed",
                "OnDestructionStageChanged",
                "OnDifficultyChanged",
                "OnDistanceGreaterThan",
                "OnDistanceLessThan",
                "OnDying",
                "OnEffectFinish",
                "OnEffectStart",
                "OnEnd",
                "OnEndState",
                "OnEnterBleedout",
                "OnEnterFurniture",
                "OnEnterOutpostBeaconMode",
                "OnEnterShipInterior",
                "OnEnterSneaking",
                "OnEntryRun",
                "OnEquipped",
                "OnEscortWaitStart",
                "OnEscortWaitStop",
                "OnExitFurniture",
                "OnExitShipInterior",
                "OnGainLOS",
                "OnGetUp",
                "OnGrab",
                "OnHit",
                "OnHomeShipSet",
                "OnInit",
                "OnItemAdded",
                "OnItemEquipped",
                "OnItemRemoved",
                "OnItemUnequipped",
                "OnKill",
                "OnLoad",
                "OnLocationChange",
                "OnLocationExplored",
                "OnLocationLoaded",
                "OnLockStateChanged",
                "OnLostLOS",
                "OnMagicEffectApply",
                "OnMapMarkerDiscovered",
                "OnMenuOpenCloseEvent",
                "OnMissionAccepted",
                "OnObjectDestroyed",
                "OnObjectRepaired",
                "OnOpen",
                "OnOutpostItemPowerOff",
                "OnOutpostItemPowerOn",
                "OnOutpostPlaced",
                "OnPackageChange",
                "OnPackageEnd",
                "OnPackageStart",
                "OnPartialCripple",
                "OnPhaseBegin",
                "OnPhaseEnd",
                "OnPickLock",
                "OnPickpocketFailed",
                "OnPipboyRadioDetection",
                "OnPlanetSiteSelectEvent",
                "OnPlayerArrested",
                "OnPlayerAssaultActor",
                "OnPlayerBuyShip",
                "OnPlayerCompleteResearch",
                "OnPlayerCraftItem",
                "OnPlayerCreateRobot",
                "OnPlayerCrimeGold",
                "OnPlayerDialogueTarget",
                "OnPlayerEnterVertibird",
                "OnPlayerFailedPlotRoute",
                "OnPlayerFallLongDistance",
                "OnPlayerFireWeapon",
                "OnPlayerFollowerWarp",
                "OnPlayerHealTeammate",
                "OnPlayerItemAdded",
                "OnPlayerJail",
                "OnPlayerLoadGame",
                "OnPlayerLoiteringBegin",
                "OnPlayerLoiteringEnd",
                "OnPlayerModArmorWeapon",
                "OnPlayerModifiedShip",
                "OnPlayerModRobot",
                "OnPlayerMurderActor",
                "OnPlayerPayFine",
                "OnPlayerPlanetSurveyComplete",
                "OnPlayerScannedObject",
                "OnPlayerSellShip",
                "OnPlayerSleepStart",
                "OnPlayerSleepStop",
                "OnPlayerSwimming",
                "OnPlayerTeleport",
                "OnPlayerTrespass",
                "OnPlayerUseWorkBench",
                "OnPlayerWaitStart",
                "OnPlayerWaitStop",
                "OnPowerOff",
                "OnPowerOn",
                "OnQuestInit",
                "OnQuestRejected",
                "OnQuestShutdown",
                "OnQuestStarted",
                "OnQuestTimerEnd",
                "OnQuestTimerMod",
                "OnQuestTimerPause",
                "OnQuestTimerResume",
                "OnQuestTimerStart",
                "OnQuickContainerOpened",
                "OnRaceSwitchComplete",
                "OnRadiationDamage",
                "OnRead",
                "OnRecoverFromBleedout",
                "OnRelease",
                "OnReset",
                "OnScanned",
                "OnSell",
                "OnShipBought",
                "OnShipDock",
                "OnShipFarTravel",
                "OnShipGravJump",
                "OnShipLanding",
                "OnShipRampDown",
                "OnShipRefueled",
                "OnShipScan",
                "OnShipSold",
                "OnShipSystemDamaged",
                "OnShipSystemPowerChange",
                "OnShipSystemRepaired",
                "OnShipTakeOff",
                "OnShipUndock",
                "OnSit",
                "OnSpeechChallengeAvailable",
                "OnSpeechChallengeCompletion",
                "OnSpellCast",
                "OnStageSet",
                "OnStarmapTargetSelectEvent",
                "OnStart",
                "OnStoryActivateActor",
                "OnStoryActorAttach",
                "OnStoryAddToPlayer",
                "OnStoryArrest",
                "OnStoryAssaultActor",
                "OnStoryAttractionObject",
                "OnStoryBribeNPC",
                "OnStoryCastMagic",
                "OnStoryChangeLocation",
                "OnStoryCraftItem",
                "OnStoryCrimeGold",
                "OnStoryCure",
                "OnStoryDialogue",
                "OnStoryDiscoverDeadBody",
                "OnStoryEscapeJail",
                "OnStoryExploredLocation",
                "OnStoryFlatterNPC",
                "OnStoryHackTerminal",
                "OnStoryHello",
                "OnStoryIncreaseLevel",
                "OnStoryInfection",
                "OnStoryIntimidateNPC",
                "OnStoryIronSights",
                "OnStoryJail",
                "OnStoryKillActor",
                "OnStoryLocationLoaded",
                "OnStoryMineExplosion",
                "OnStoryNewVoicePower",
                "OnStoryPayFine",
                "OnStoryPickLock",
                "OnStoryPickPocket",
                "OnStoryPiracyActor",
                "OnStoryPlayerGetsFavor",
                "OnStoryRelationshipChange",
                "OnStoryRemoveFromPlayer",
                "OnStoryScript",
                "OnStoryServedTime",
                "OnStoryShipDock",
                "OnStoryShipLanding",
                "OnStoryTrespass",
                "OnTerminalMenuEnter",
                "OnTerminalMenuItemRun",
                "OnTimer",
                "OnTimerGameTime",
                "OnTrackedStatsEvent",
                "OnTranslationAlmostComplete",
                "OnTranslationComplete",
                "OnTranslationFailed",
                "OnTrapHitStart",
                "OnTrapHitStop",
                "OnTriggerEnter",
                "OnTriggerLeave",
                "OnTutorialEvent",
                "OnUnequipped",
                "OnUnload",
                "OnWorkshopCargoLinkChanged",
                "OnWorkshopFlyCam",
                "OnWorkshopMode",
                "OnWorkshopNPCTransfer",
                "OnWorkshopObjectGrabbed",
                "OnWorkshopObjectMoved",
                "OnWorkshopObjectPlaced",
                "OnWorkshopObjectRemoved",
                "OnWorkshopOutputLink",
        };
        static const std::vector<std::string> EventNamesLowerCase = {
                "onaction",
                "onactivate",
                "onactoractivatedref",
                "onactorvaluechanged",
                "onactorvaluegreaterthan",
                "onactorvaluelessthan",
                "onaffinityevent",
                "onaffinityeventsent",
                "onaliaschanged",
                "onaliasinit",
                "onaliasreset",
                "onaliasshutdown",
                "onaliasstarted",
                "onanimationevent",
                "onanimationeventunregistered",
                "onbegin",
                "onbeginstate",
                "onbuildermenuselect",
                "oncellattach",
                "oncelldetach",
                "oncellload",
                "onchallengecompleted",
                "onchange",
                "onclose",
                "oncombatlistadded",
                "oncombatlistremoved",
                "oncombatstatechanged",
                "oncommandmodecompletecommand",
                "oncommandmodeenter",
                "oncommandmodeexit",
                "oncommandmodegivecommand",
                "oncompaniondismiss",
                "onconsciousnessstatechanged",
                "oncontainerchanged",
                "oncrewassigned",
                "oncrewdismissed",
                "oncripple",
                "ondeath",
                "ondeferredkill",
                "ondestroyed",
                "ondestructionstagechanged",
                "ondifficultychanged",
                "ondistancegreaterthan",
                "ondistancelessthan",
                "ondying",
                "oneffectfinish",
                "oneffectstart",
                "onend",
                "onendstate",
                "onenterbleedout",
                "onenterfurniture",
                "onenteroutpostbeaconmode",
                "onentershipinterior",
                "onentersneaking",
                "onentryrun",
                "onequipped",
                "onescortwaitstart",
                "onescortwaitstop",
                "onexitfurniture",
                "onexitshipinterior",
                "ongainlos",
                "ongetup",
                "ongrab",
                "onhit",
                "onhomeshipset",
                "oninit",
                "onitemadded",
                "onitemequipped",
                "onitemremoved",
                "onitemunequipped",
                "onkill",
                "onload",
                "onlocationchange",
                "onlocationexplored",
                "onlocationloaded",
                "onlockstatechanged",
                "onlostlos",
                "onmagiceffectapply",
                "onmapmarkerdiscovered",
                "onmenuopencloseevent",
                "onmissionaccepted",
                "onobjectdestroyed",
                "onobjectrepaired",
                "onopen",
                "onoutpostitempoweroff",
                "onoutpostitempoweron",
                "onoutpostplaced",
                "onpackagechange",
                "onpackageend",
                "onpackagestart",
                "onpartialcripple",
                "onphasebegin",
                "onphaseend",
                "onpicklock",
                "onpickpocketfailed",
                "onpipboyradiodetection",
                "onplanetsiteselectevent",
                "onplayerarrested",
                "onplayerassaultactor",
                "onplayerbuyship",
                "onplayercompleteresearch",
                "onplayercraftitem",
                "onplayercreaterobot",
                "onplayercrimegold",
                "onplayerdialoguetarget",
                "onplayerentervertibird",
                "onplayerfailedplotroute",
                "onplayerfalllongdistance",
                "onplayerfireweapon",
                "onplayerfollowerwarp",
                "onplayerhealteammate",
                "onplayeritemadded",
                "onplayerjail",
                "onplayerloadgame",
                "onplayerloiteringbegin",
                "onplayerloiteringend",
                "onplayermodarmorweapon",
                "onplayermodifiedship",
                "onplayermodrobot",
                "onplayermurderactor",
                "onplayerpayfine",
                "onplayerplanetsurveycomplete",
                "onplayerscannedobject",
                "onplayersellship",
                "onplayersleepstart",
                "onplayersleepstop",
                "onplayerswimming",
                "onplayerteleport",
                "onplayertrespass",
                "onplayeruseworkbench",
                "onplayerwaitstart",
                "onplayerwaitstop",
                "onpoweroff",
                "onpoweron",
                "onquestinit",
                "onquestrejected",
                "onquestshutdown",
                "onqueststarted",
                "onquesttimerend",
                "onquesttimermod",
                "onquesttimerpause",
                "onquesttimerresume",
                "onquesttimerstart",
                "onquickcontaineropened",
                "onraceswitchcomplete",
                "onradiationdamage",
                "onread",
                "onrecoverfrombleedout",
                "onrelease",
                "onreset",
                "onscanned",
                "onsell",
                "onshipbought",
                "onshipdock",
                "onshipfartravel",
                "onshipgravjump",
                "onshiplanding",
                "onshiprampdown",
                "onshiprefueled",
                "onshipscan",
                "onshipsold",
                "onshipsystemdamaged",
                "onshipsystempowerchange",
                "onshipsystemrepaired",
                "onshiptakeoff",
                "onshipundock",
                "onsit",
                "onspeechchallengeavailable",
                "onspeechchallengecompletion",
                "onspellcast",
                "onstageset",
                "onstarmaptargetselectevent",
                "onstart",
                "onstoryactivateactor",
                "onstoryactorattach",
                "onstoryaddtoplayer",
                "onstoryarrest",
                "onstoryassaultactor",
                "onstoryattractionobject",
                "onstorybribenpc",
                "onstorycastmagic",
                "onstorychangelocation",
                "onstorycraftitem",
                "onstorycrimegold",
                "onstorycure",
                "onstorydialogue",
                "onstorydiscoverdeadbody",
                "onstoryescapejail",
                "onstoryexploredlocation",
                "onstoryflatternpc",
                "onstoryhackterminal",
                "onstoryhello",
                "onstoryincreaselevel",
                "onstoryinfection",
                "onstoryintimidatenpc",
                "onstoryironsights",
                "onstoryjail",
                "onstorykillactor",
                "onstorylocationloaded",
                "onstorymineexplosion",
                "onstorynewvoicepower",
                "onstorypayfine",
                "onstorypicklock",
                "onstorypickpocket",
                "onstorypiracyactor",
                "onstoryplayergetsfavor",
                "onstoryrelationshipchange",
                "onstoryremovefromplayer",
                "onstoryscript",
                "onstoryservedtime",
                "onstoryshipdock",
                "onstoryshiplanding",
                "onstorytrespass",
                "onterminalmenuenter",
                "onterminalmenuitemrun",
                "ontimer",
                "ontimergametime",
                "ontrackedstatsevent",
                "ontranslationalmostcomplete",
                "ontranslationcomplete",
                "ontranslationfailed",
                "ontraphitstart",
                "ontraphitstop",
                "ontriggerenter",
                "ontriggerleave",
                "ontutorialevent",
                "onunequipped",
                "onunload",
                "onworkshopcargolinkchanged",
                "onworkshopflycam",
                "onworkshopmode",
                "onworkshopnpctransfer",
                "onworkshopobjectgrabbed",
                "onworkshopobjectmoved",
                "onworkshopobjectplaced",
                "onworkshopobjectremoved",
                "onworkshopoutputlink",
        };
    }
}
```

## File: `Decompiler/OutputWriter.hpp`
```
#pragma once

#include <string>

namespace Decompiler {

/**
 * @brief Interface for output writer.
 *
 * This interface insert an abstraction layer between the output file/buffer and the
 * code generation objects.
 *
 */
class OutputWriter
{
public:
    OutputWriter() = default;
    virtual ~OutputWriter() = default;

    virtual void writeLine(const std::string& line) = 0;
};
}
```

## File: `Decompiler/PscCodeBlock.cpp`
```cpp
#include "PscCodeBlock.hpp"

#include <cassert>


/**
 * @brief Constructor.
 * This constructor builds a blocks containing instructions from ranging from begin to end, inclusive.
 * @param begin Indice of the first instruction of the block
 * @param end Indice of the last instruction of the block.
 */
Decompiler::PscCodeBlock::PscCodeBlock(size_t begin, size_t end) :
    m_Begin(begin),
    m_End(end),
    m_Next(END),
    m_OnFalse(END),
    m_Scope(std::make_shared<Node::Scope>())
{
}

/**
 * @brief Default destructor
 */
Decompiler::PscCodeBlock::~PscCodeBlock()
{
}

/**
 * @brief Get the indice of the first instruction of the block
 * @return The indice of the first instruction.
 */
size_t Decompiler::PscCodeBlock::getBegin() const
{
    return m_Begin;
}

/**
 * @brief Get the indice of the last instruction of the block.
 * @return The indice of the last instruction.
 */
size_t Decompiler::PscCodeBlock::getEnd() const
{
    return m_End;
}

/**
 * @brief Get the indice of the next block for inconditional jump.
 * @return The indice of the next block.
 */
size_t Decompiler::PscCodeBlock::getNext() const
{
    return m_Next;
}

/**
 * @brief Get the indice of the block for the true condition.
 * @return The indice of the true block.
 */
size_t Decompiler::PscCodeBlock::onTrue() const
{
    return m_Next;
}

/**
 * @brief Get the indice of the block for the false condition.
 * @return The indice of the false block.
 */
size_t Decompiler::PscCodeBlock::onFalse() const
{
    return m_OnFalse;
}

/**
 * @brief Get the name of variable holding the value for the true/false block selection.
 * @return The name of the variable.
 */
const Pex::StringTable::Index &Decompiler::PscCodeBlock::getCondition() const
{
    return m_Condition;
}


/**
 * @brief Check if the block is conditional.
 * @return True if the block has a condition variable.
 */
bool Decompiler::PscCodeBlock::isConditional() const
{
    return m_Condition.isValid() && !m_Condition.isUndefined();
}

/**
 * @brief Set the end indice of the block.
 * @param end The new end of the block.
 */
void Decompiler::PscCodeBlock::setEnd(size_t end)
{
    m_End = end;
}

/**
 * @brief Set the next block for unconditional block.
 * @param next The next block.
 */
void Decompiler::PscCodeBlock::setNext(size_t next)
{
    m_Next = next;
}

/**
 * @brief Set the condition variable and the two destination blocks.
 * @param condition The name index of the condition variable.
 * @param ontrue The indice of the block for the true branch.
 * @param onfalse The indice of the block for the false branch.
 */
void Decompiler::PscCodeBlock::setCondition(const Pex::StringTable::Index &condition, size_t ontrue, size_t onfalse)
{
    m_Condition = condition;
    m_Next = ontrue;
    m_OnFalse = onfalse;
}

/**
 * @brief Split the block in two blocks and return the second one.
 * @param split Indice of the instruction starting the new block
 * @return A pointer to the new block. The ownership is transferred.
 */
Decompiler::PscCodeBlock *Decompiler::PscCodeBlock::split(size_t split)
{
    //assert(m_Begin < split && split <= m_End);
    auto* result = new PscCodeBlock(split, m_End);
    result->m_Next = m_Next;
    result->m_Condition = m_Condition;
    result->m_OnFalse = m_OnFalse;

    m_End = split - 1;
    m_Next = split;
    m_Condition = Pex::StringTable::Index();
    m_OnFalse = END;
    return result;
}

/**
 * @brief Get the scope node associated with the block.
 * @return A pointer to the scope block.
 */
Node::Scope *Decompiler::PscCodeBlock::getScope() const
{
    return static_cast<Node::Scope*>(m_Scope.get());
}

void Decompiler::PscCodeBlock::addLockGuard(Pex::StringTable::Index index) {
    m_Guards.push_back(index);
}

bool Decompiler::PscCodeBlock::isLock() const {
    return !m_Guards.empty();
}
```

## File: `Decompiler/PscCodeBlock.hpp`
```
#pragma once

#include <vector>

#include "Pex/StringTable.hpp"

#include "Node/Scope.hpp"

namespace Decompiler {

/**
 * @brief Code block data.
 *
 * The code block represent a direct sequence of instructions. A block ends with a jump, conditional or not,
 * and begins at the target of another jump. The obvious exceptions are the first and last block, which begins at the first instruction
 * and ends at the last instruction respectively.
 *
 * A block can be linked with another block which will be executed after it, or attached to a condition variable and two other blocks run if wether the
 * condition is true or false. The blocks sequence reflect the program instructions flow.
 *
 * Finally each block contains a Scope node which contains the statements and expression nodes computed by the block.
 *
 * The instructions and blocks are identified by their indices in the instruction array.
 */
class PscCodeBlock
{
public:
    static const size_t END = 0xFFFFFFFF;

    void addLockGuard(Pex::StringTable::Index index);

public:
    PscCodeBlock(size_t getBegin, size_t getEnd);
    ~PscCodeBlock();


    size_t getBegin() const;
    size_t getEnd() const;
    size_t getNext() const;
    size_t onTrue() const;
    size_t onFalse() const;
    const Pex::StringTable::Index& getCondition() const;

    bool isConditional() const;
    bool isLock() const;

    void setEnd(size_t getEnd);
    void setNext(size_t getNext);
    void setCondition(const Pex::StringTable::Index& getCondition, size_t ontrue, size_t onfalse);

    PscCodeBlock* split(size_t split);

    Node::Scope* getScope() const;

protected:
    size_t m_Begin;
    size_t m_End;

    size_t m_Next;
    size_t m_OnFalse;
    Pex::StringTable::Index m_Condition;
    std::vector<Pex::StringTable::Index> m_Guards;

    Node::BasePtr m_Scope;

};

}
```

## File: `Decompiler/PscCodeGenerator.cpp`
```cpp
#include "PscCodeGenerator.hpp"

#include <cassert>

#include "Node/Nodes.hpp"
#include "PscCoder.hpp"

static bool isTempVar(const Pex::StringTable::Index& var)
{
    auto& name = var.asString();
    return name.length() > 6 && name.substr(0, 6) == "::temp" && name.substr(name.length() - 4, 4) != "_var";
}

static std::string getVarName(const Pex::StringTable::Index& var)
{
    auto& name = var.asString();
    if (name.length() > 6 && name.substr(0, 2) == "::" && name.substr(name.length() - 4, 4) == "_var")
    {
        return name.substr(2, name.length() - 6);
    }

    return name;
}


Decompiler::PscCodeGenerator::PscCodeGenerator(Decompiler::PscDecompiler* decompiler) :
    m_Decompiler(decompiler)
{
    assert(decompiler);
}


void Decompiler::PscCodeGenerator::newLine()
{

    if (!m_ExperimentalSyntaxWarning.empty()) {
        m_Result << " " << Decompiler::WARNING_COMMENT_PREFIX << " WARNING: Experimental syntax, may be incorrect: ";
        for (auto warn: m_ExperimentalSyntaxWarning){
            m_Result << warn << " ";
        }
        m_ExperimentalSyntaxWarning.clear();
    }
    auto nums = getDebugInfoLineNumbers(minIpForCurrentLine, maxIpForCurrentLine);
    resetIpsForCurrentLine();
    m_Decompiler->push_back(m_Result.str());
    m_Decompiler->addLineMapping(m_Decompiler->size() - 1, nums);

    m_Result = std::ostringstream();
    for (auto i = 0; i < m_Level; ++i)
    {
        m_Result << ' ' << ' ';
    }
}

void Decompiler::PscCodeGenerator::visit(Node::Scope* node)
{
    auto not_first = false;
    for(auto statement : *node)
    {
        if(not_first)
        {
            newLine();
        }
        else
        {
            not_first = true;
        }
        if (statement->getBegin() != -1 &&  statement->getEnd() != -1)
        {
            m_Decompiler->decodeToAsm(m_Level, statement->getBegin(), statement->getEnd());
        }
        statement->visit(this);
    }
    if (node->getParent() == nullptr)
    {
        newLine();
    }
}

void Decompiler::PscCodeGenerator::visit(Node::BinaryOperator* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    bool parenOnLeft = node->getPrecedence() < node->getLeft()->getPrecedence();
    if (node->getLeft()->is<Node::BinaryOperator>()) {
        auto l = node->getLeft()->as<Node::BinaryOperator>();
        if (l->getLeft()->is<Node::Cast>() || l->getRight()->is<Node::Cast>()) {
            parenOnLeft = true;
        }
    }
    bool parenOnRight = node->getPrecedence() < node->getRight()->getPrecedence();
    if (node->getRight()->is<Node::BinaryOperator>()) {
        auto r = node->getRight()->as<Node::BinaryOperator>();
        if (r->getLeft()->is<Node::Cast>() || r->getRight()->is<Node::Cast>()) {
            parenOnRight = true;
        }
    }
    if (parenOnLeft)
    {
        m_Result << "(";
    }
    node->getLeft()->visit(this);
    if (parenOnLeft)
    {
        m_Result << ")";
    }
    m_Result << " " << node->getOperator() << " ";
    if (parenOnRight)
    {
        m_Result << "(";
    }
    if (node->getOperator() == "is" && node->getRight()->is<Node::IdentifierString>()) {
      m_Result << PscCoder::mapType(node->getRight()->as<Node::IdentifierString>()->getIdentifier());
    } else {
      node->getRight()->visit(this);
    }
    if (parenOnRight)
    {
        m_Result << ")";
    }
}

void Decompiler::PscCodeGenerator::visit(Node::UnaryOperator* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    bool paren = node->getPrecedence() < node->getValue()->getPrecedence();

    m_Result << node->getOperator();
    if (paren)
    {
        m_Result << "(";
    }
    node->getValue()->visit(this);
    if (paren)
    {
        m_Result << ")";
    }
}
void Decompiler::PscCodeGenerator::visit(Node::Assign* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    node->getDestination()->visit(this);
    m_Result << " = ";
    node->getValue()->visit(this);
}

void Decompiler::PscCodeGenerator::visit(Node::AssignOperator* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    node->getDestination()->visit(this);
    m_Result << " " << node->getOperator() << " ";
    node->getValue()->visit(this);
}

void Decompiler::PscCodeGenerator::visit(Node::Copy *node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    node->getValue()->visit(this);
}

void Decompiler::PscCodeGenerator::visit(Node::Cast* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    bool paren = node->getPrecedence() < node->getValue()->getPrecedence() || node->getValue()->is<Node::Cast>();

    if (paren)
    {
        m_Result << "(";
    }
    node->getValue()->visit(this);
    if (paren)
    {
        m_Result << ")";
    }
    m_Result << " as " << PscCoder::mapType(node->getType().asString());
}

void Decompiler::PscCodeGenerator::visit(Node::CallMethod* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    bool paren = node->getPrecedence() < node->getObject()->getPrecedence();

    if (paren)
    {
        m_Result << "(";
    }
    if (node->getObject()->is<Node::IdentifierString>()) {
        m_Result << PscCoder::mapType(node->getObject()->as<Node::IdentifierString>()->getIdentifier());
    } else {
        node->getObject()->visit(this);
    }
    if (paren)
    {
        m_Result << ")";
    }
    m_Result << "." << node->getMethod() << "(";
    node->getParameters()->visit(this);
    m_Result << ")";
    if (node->isExperimentalSyntax()) {
        m_ExperimentalSyntaxWarning.push_back(node->getMethod().asString());
    }
}

void Decompiler::PscCodeGenerator::visit(Node::Params *node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    bool not_first = false;
    for (auto param : *node)
    {
        if (not_first)
        {
            m_Result << ", ";
        }
        else
        {
            not_first = true;
        }
        param->visit(this);
    }
}

void Decompiler::PscCodeGenerator::visit(Node::Return* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    m_Result << "Return ";
    if (node->getValue())
    {
        node->getValue()->visit(this);
    }
}

void Decompiler::PscCodeGenerator::visit(Node::PropertyAccess *node) {
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    bool paren = node->getPrecedence() < node->getObject()->getPrecedence();

    if (paren) {
        m_Result << "(";
    }
    node->getObject()->visit(this);
    if (paren)
    {
        m_Result << ")";
    }
    m_Result << "." << node->getProperty();
}

void Decompiler::PscCodeGenerator::visit(Node::StructCreate* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    m_Result << "new " << PscCoder::mapType(node->getType().asString());
}

void Decompiler::PscCodeGenerator::visit(Node::ArrayCreate* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    std::string type = PscCoder::mapType(node->getType().asString());
    m_Result << "new " << type.substr(0, type.length() - 2) << "[";

    node->getIndex()->visit(this);
    m_Result << "]";
}

void Decompiler::PscCodeGenerator::visit(Node::ArrayLength* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    bool paren = node->getPrecedence() < node->getArray()->getPrecedence();

    if (paren)
    {
        m_Result << "(";
    }
    node->getArray()->visit(this);
    if (paren)
    {
        m_Result << ")";
    }
    m_Result << ".Length";
}

void Decompiler::PscCodeGenerator::visit(Node::ArrayAccess *node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    bool paren = node->getPrecedence() < node->getArray()->getPrecedence();

    if (paren)
    {
        m_Result << "(";
    }
    node->getArray()->visit(this);
    if (paren)
    {
        m_Result << ")";
    }
    m_Result << "[";
    node->getIndex()->visit(this);
    m_Result << "]";
}

void Decompiler::PscCodeGenerator::visit(Node::Constant* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    auto& value = node->getConstant();

    m_Result << value.toString();
}

void Decompiler::PscCodeGenerator::visit(Node::IdentifierString *node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    if (node->getIdentifier() == "self")
        m_Result << "Self";
    else
        m_Result << node->getIdentifier();
}

void Decompiler::PscCodeGenerator::visit(Node::While* node)
{
    m_Result << "While ";
    node->getCondition()->visit(this);
    m_Level++;
    newLine();
    node->getBody()->visit(this);
    m_Level--;
    newLine();
    if (node->getBody()->size() != 0)
    {
        m_Decompiler->decodeToAsm(m_Level, node->getBody()->back()->getEnd() + 1, node->getBody()->back()->getEnd() + 1);
    }
    // EndWhile does not have valid debug line numbers, reset minIpForCurrentLine and maxIpForCurrentLine
    resetIpsForCurrentLine();
    m_Result << "EndWhile";
}

void Decompiler::PscCodeGenerator::visit(Node::IfElse* node)
{
    addIpRangeForCurrentLine(node->getBegin(), node->getEnd());
    auto cond = node->getCondition();
    m_Result << "If ";
    node->getCondition()->visit(this);
    m_Level++;
    newLine();
    node->getBody()->visit(this);
    m_Level--;
    newLine();
    auto lastBody = node->getBody();

    for (auto childNode : *(node->getElseIf()))
    {
        m_Decompiler->decodeToAsm(m_Level, childNode->getBegin()-1, childNode->getEnd());
        auto elseIf = childNode->as<Node::IfElse>();
        m_Result << "ElseIf ";
        elseIf->getCondition()->visit(this);
        m_Level++;
        newLine();
        elseIf->getBody()->visit(this);
        m_Level--;
        newLine();
        lastBody = elseIf->getBody();
    }
    m_Decompiler->decodeToAsm(m_Level, lastBody->getEnd() + 1, lastBody->getEnd() + 1);
    if (node->getElse()->size() != 0)
    {
        m_Result << "Else";
        m_Level++;
        // Else do not have valid debug line numbers, reset minIpForCurrentLine and maxIpForCurrentLine
        resetIpsForCurrentLine();
        newLine();
        node->getElse()->visit(this);
        m_Level--;
        newLine();
    }
    // Endif does not have valid debug line numbers, reset minIpForCurrentLine and maxIpForCurrentLine
    resetIpsForCurrentLine();
    m_Result << "EndIf";
}

void Decompiler::PscCodeGenerator::visit(Node::Declare *node)
{
    addIpRangeForCurrentLine(node->getEnd(), node->getEnd());
    m_Result << PscCoder::mapType(node->getType().asString()) << " ";
    node->getObject()->visit(this);
}

void Decompiler::PscCodeGenerator::visit(Node::GuardStatement *node) {
    m_Result << "Guard ";
    addIpRangeForCurrentLine(node->getBegin(), node->getBegin());
    node->getParameters()->visit(this);
    m_Level++;
    // TODO: VERIFY: Remove this when syntax is verified
    m_ExperimentalSyntaxWarning.push_back("Guard");
    newLine();
    node->getBody()->visit(this);
    m_Level--;
    newLine();
    m_Result << "EndGuard";
    m_ExperimentalSyntaxWarning.push_back("EndGuard");
}

void Decompiler::PscCodeGenerator::visit(Node::TryGuard *node) {
    m_Result << "TryGuard ";
    addIpRangeForCurrentLine(node->getBegin(), node->getBegin());
    node->getParameters()->visit(this);
    m_Level++;
    // TODO: VERIFY: Remove this when syntax is verified
    m_ExperimentalSyntaxWarning.push_back("TryGuard");
    newLine();
    node->getBody()->visit(this);
    m_Level--;
    newLine();
    m_Result << "EndGuard";
    m_ExperimentalSyntaxWarning.push_back("EndGuard");

}

void Decompiler::PscCodeGenerator::visit(Node::EndGuard *node) {
    // NONE
}

void Decompiler::PscCodeGenerator::addIpRangeForCurrentLine(int64_t begin, int64_t end) {
    if (begin <= -1 || end <= -1) {
        return;
    }
    if (minIpForCurrentLine <= -1 || begin < minIpForCurrentLine) {
        minIpForCurrentLine = begin;
    }
    if (maxIpForCurrentLine <= -1 || end > maxIpForCurrentLine) {
        maxIpForCurrentLine = end;
    }
}

void Decompiler::PscCodeGenerator::resetIpsForCurrentLine() {
    minIpForCurrentLine = -1;
    maxIpForCurrentLine = -1;
}

std::vector<uint16_t> Decompiler::PscCodeGenerator::getDebugInfoLineNumbers(int64_t begin, int64_t end) {
    return m_Decompiler->getDebugInfo().getLineNumbersForIpRange(begin, end);
}

```

## File: `Decompiler/PscCodeGenerator.hpp`
```
#pragma once

#include "Node/Visitor.hpp"
#include "PscDecompiler.hpp"

#include <sstream>

namespace Decompiler
{

/**
 * @brief Write a tree as Papyrus statements.
 *
 * This visitor outputs the expression nodes and writes them
 * as Papyrus statements.
 *
 */
class PscCodeGenerator : public Node::Visitor
{
public:
    PscCodeGenerator(Decompiler::PscDecompiler* decompiler);
    virtual ~PscCodeGenerator() = default;


    virtual void visit(Node::Scope* node);
    virtual void visit(Node::BinaryOperator* node);
    virtual void visit(Node::UnaryOperator* node);
    virtual void visit(Node::Assign* node);
    virtual void visit(Node::AssignOperator* node);
    virtual void visit(Node::Copy* node);
    virtual void visit(Node::Cast* node);
    virtual void visit(Node::CallMethod* node);
    virtual void visit(Node::Params* node);
    virtual void visit(Node::Return* node);
    virtual void visit(Node::PropertyAccess* node);
    virtual void visit(Node::StructCreate* node);
    virtual void visit(Node::ArrayCreate* node);
    virtual void visit(Node::ArrayLength* node);
    virtual void visit(Node::ArrayAccess* node);
    virtual void visit(Node::Constant* node);
    virtual void visit(Node::IdentifierString* node);
    virtual void visit(Node::While* node);
    virtual void visit(Node::IfElse* node);
    virtual void visit(Node::Declare* node);
    virtual void visit(Node::GuardStatement* node);
    virtual void visit(Node::TryGuard* node);
    virtual void visit(Node::EndGuard* node);


protected:    
    void newLine();
    void addIpRangeForCurrentLine(int64_t begin, int64_t end);
    std::ostringstream m_Result;
    int64_t minIpForCurrentLine{ -1 };
    int64_t maxIpForCurrentLine{ -1 };
    std::uint8_t m_Level{ 0 };
    std::vector<std::string> m_ExperimentalSyntaxWarning{};
    Decompiler::PscDecompiler* m_Decompiler;

    std::vector<uint16_t> getDebugInfoLineNumbers(int64_t begin, int64_t end);
    void resetIpsForCurrentLine();
};

}
```

## File: `Decompiler/PscCoder.cpp`
```cpp
#include "PscCoder.hpp"

#include <algorithm>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <locale>
#include <map>
#include <string>
#include <regex>

#include "PscDecompiler.hpp"
#include "Version.hpp"
#include "EventNames.hpp"
#include "Champollion/CaselessCompare.h"

/**
 * @brief Constructor
 * Builds an object associated with an output writer.
 *
 * @param writer Pointer to the output writer. The ownership is transferred.
 * @param commentAsm True to output assembly instruction comments (default: false).
 * @param writeHeader True to write the header (default: false).
 * @param traceDecompilation True to output decompilation tracing to the rebuild log (default: false).
 * @param dumpTree True to output the entire tree for each block (true by default if traceDecompilation is true).
 * @param traceDir If tracing is enabled, write rebuild logs to this dir (default is cwd)
 */
Decompiler::PscCoder::PscCoder( OutputWriter* writer,
                                bool commentAsm = false,
                                bool writeHeader = false,
                                bool traceDecompilation = false,
                                bool dumpTree = true,   
                                bool writeDebugFuncs = false,
                                bool printDebugLineNo = false,
                                std::string traceDir = ""):
    Coder(writer),
    m_CommentAsm(commentAsm),
    m_WriteHeader(writeHeader),
    m_TraceDecompilation(traceDecompilation),
    m_DumpTree(dumpTree), // Note that while dumpTree is true by default, it will not do anything unless traceDecompilation is true
    m_WriteDebugFuncs(writeDebugFuncs),
    m_OutputDir(traceDir),
    m_PrintDebugLineNo(printDebugLineNo)
{
    
}

/**
 * @brief Constructor
 * Builds an object associated with an output writer.
 *
 * @param writer Pointer to the output writer. The ownership is transferred.
 */
Decompiler::PscCoder::PscCoder(Decompiler::OutputWriter *writer)  :
    Coder(writer),
    m_CommentAsm(false),
    m_WriteHeader(false),
    m_TraceDecompilation(false),
    m_DumpTree(true),
    m_WriteDebugFuncs(false),
    m_PrintDebugLineNo(false),
    m_OutputDir("")
{
}

/**
 * @brief Default desctructor
 */
Decompiler::PscCoder::~PscCoder()
{
}

/**
 * @brief Decompile a PEX binary to a Papyrus file.
 * @param pex
 */
void Decompiler::PscCoder::code(const Pex::Binary &pex)
{
    if (m_WriteHeader) 
    {
        writeHeader(pex);
    }
    for(auto& object : pex.getObjects())
    {
        writeObject(object, pex);
    }

}

/**
 * @brief Set the option to output Assembly instruction in comments
 * @param commentAsm True to write the comments.
 * @return A reference to this.
 */
Decompiler::PscCoder &Decompiler::PscCoder::outputAsmComment(bool commentAsm)
{
    m_CommentAsm = commentAsm;
    return *this;
}

/**
 * @brief Set the option to write decompilation trace information to the rebuild log
 * @param traceDecompilation True to trace decompilation.
 * @return A reference to this.
 */
Decompiler::PscCoder &Decompiler::PscCoder::outputDecompilationTrace(bool traceDecompilation)
{
    m_TraceDecompilation = traceDecompilation;
    return *this;
}

/**
 * @brief Set the option to output the tree for each node during decompilation tracing
 * @param dumpTree True to dump node trees during decompilation tracing.
 * @return A reference to this.
 */
Decompiler::PscCoder &Decompiler::PscCoder::outputDumpTree(bool dumpTree)
{
    m_DumpTree = dumpTree;
    return *this;
}

/**
 * @brief Set the option to add a header to the decompiled script.
 * @param writeHeader True to write the header.
 * @return A reference to this.
 */
Decompiler::PscCoder &Decompiler::PscCoder::outputWriteHeader(bool writeHeader)
{
    m_WriteHeader = writeHeader;
    return *this;
}

/**
 * @brief Write the content of the PEX header as a block comment.
 * @param pex Binary to decompile.
 */
void Decompiler::PscCoder::writeHeader(const Pex::Binary &pex)
{
    auto& header = pex.getHeader();
    auto& debug  = pex.getDebugInfo();
    write(";/ Decompiled by Champollion " + std::string(CHAMPOLLION_VERSION_STRING));
    write(indent(0) << "PEX format v" << (int)header.getMajorVersion() << "." << (int)header.getMinorVersion() << " GameID: " << header.getGameID());
    write(indent(0) << "Source   : " << header.getSourceFileName());
    if (debug.getModificationTime() != 0)
    {
        write(indent(0) << "Modified : " << std::put_time(std::localtime(&debug.getModificationTime()), "%Y-%m-%d %H:%M:%S"));
        //for (auto& f : debug.getFunctionInfos()) {
        //  write(indent(0) << f.getObjectName().asString() << ":" << f.getStateName().asString() << ":" << f.getFunctionName().asString() << " type: " << (int)f.getFunctionType());
        //  for (auto& l : f.getLineNumbers())
        //    write(indent(1) << "Line: " << l);
        //}
    }
    write(indent(0) << "Compiled : " << std::put_time(std::localtime(&header.getCompilationTime()), "%Y-%m-%d %H:%M:%S"));
    write(indent(0) << "User     : " << header.getUserName());
    write(indent(0) << "Computer : " << header.getComputerName());
    write("/;");
}

bool Decompiler::PscCoder::isNativeObject(const Pex::Object &object, const Pex::Binary::ScriptType &scriptType) const {
    if (scriptType == Pex::Binary::ScriptType::Fallout4Script)
    {
        for (auto& native : Fallout4::NativeClasses)
        {
            if (caselessCompare(object.getName().asString().c_str(), native.c_str()) == 0){
                return true;
            }
        }
    }
    else if (scriptType == Pex::Binary::ScriptType::StarfieldScript)
    {
        for (auto& native : Starfield::NativeClasses)
        {
            if (caselessCompare(object.getName().asString().c_str(), native.c_str()) == 0){
                return true;
            }
        }
    }
    return false;
}

/**
 * @brief Write an object contained in the binary.
 * @param object Object to decompile
 * @param pex Binary to decompile.
 */
void Decompiler::PscCoder::writeObject(const Pex::Object &object, const Pex::Binary &pex)
{
    auto stream = indent(0);
    stream <<"ScriptName " << object.getName().asString();
    if (! object.getParentClassName().asString().empty())
    {
        stream << " Extends " << object.getParentClassName().asString();
    }

    if (isNativeObject(object, pex.getGameType()))
        stream << " Native";

    if (object.getConstFlag())
      stream << " Const";

    writeUserFlag(stream, object, pex);
    write(stream.str());

    writeDocString(0, object);

    if (object.getStructInfos().size()) {
        write("");
        write(";-- Structs -----------------------------------------");
        writeStructs(object, pex);
    }

    if (object.getVariables().size()) {
        write("");
        write(";-- Variables ---------------------------------------");
        writeVariables(object, pex);
    }

    if (object.getGuards().size()) {
        write("");
        write(";-- Guards ------------------------------------------");
        write(std::string(Decompiler::WARNING_COMMENT_PREFIX) + " WARNING: Guard declaration syntax is EXPERIMENTAL, subject to change");
        writeGuards(object, pex);
    }

    if (object.getProperties().size()) {
        write("");
        write(";-- Properties --------------------------------------");
        writeProperties(object, pex);
    }

    writeStates(object, pex);
}

/**
* @brief Write the struct definitions stored in the object.
* @param object Object containing the struct definitions.
* @param pex Binary to decompile.
*/
void Decompiler::PscCoder::writeStructs(const Pex::Object& object, const Pex::Binary& pex) {
    for (auto& sInfo : object.getStructInfos()) {
        write(indent(0) << "Struct " << sInfo.getName().asString());

        bool foundInfo = false;
        if (pex.getDebugInfo().getStructOrders().size()) {
            // If we have debug info, we have information on the order
            // they were in the original source file, so use that order.
            for (auto& sOrder : pex.getDebugInfo().getStructOrders()) {
                if (sOrder.getObjectName() == object.getName() && sOrder.getOrderName() == sInfo.getName()) {
                    if (sOrder.getNames().size() == sInfo.getMembers().size()) {
                        foundInfo = true;
                        for (auto& orderName : sOrder.getNames()) {
                            for (auto& member : sInfo.getMembers()) {
                                if (member.getName() == orderName) {
                                    writeStructMember(member, pex);
                                    goto ContinueOrder;
                                }
                            }
                            // If we get here, then we failed to find the struct
                            // member in the debug info :(
                            throw std::runtime_error("Unable to locate the struct member by the name of '" + orderName.asString() + "'");
                        ContinueOrder:
                            continue;
                        }
                    } else {
                        // This shouldn't happen, but it's possible that the
                        // debug info doesn't include all members of the struct,
                        // so write them in whatever order they are in the file.
                        break;
                    }
                }
            }
        }

        if (!foundInfo) {
            for (auto& mem : sInfo.getMembers())
                writeStructMember(mem, pex);
        }

        write(indent(0) << "EndStruct");
        write("");
    }
}

/**
* @brief Write the struct member passed in.
* @param member The member to output.
* @param pex Binary to decompile.
*/
void Decompiler::PscCoder::writeStructMember(const Pex::StructInfo::Member& member, const Pex::Binary& pex)
{
    auto stream = indent(1);
    stream << mapType(member.getTypeName().asString()) << " " << member.getName().asString();

    if (member.getValue().getType() != Pex::ValueType::None) {
        stream << " = " << member.getValue().toString();
    }
    writeUserFlag(stream, member, pex);
    if (member.getConstFlag())
      stream << " Const";
    write(stream.str());
    writeDocString(1, member);
}

/**
 * @brief Write the properties definitions stored in the object.
 * @param object Object containing the properties definitions.
 * @param pex Binary to decompile.
 */
void Decompiler::PscCoder::writeProperties(const Pex::Object &object, const Pex::Binary &pex)
{
    bool foundInfo = false;
    if (pex.getDebugInfo().getPropertyGroups().size()) {
        size_t totalProperties = 0;
        // If we have debug info, we have information on the order
        // they were in the original source file, so use that order.
        for (auto& propGroup : pex.getDebugInfo().getPropertyGroups()) {
            if (propGroup.getObjectName() == object.getName()) {
                totalProperties += propGroup.getNames().size();
            }
        }

        if (totalProperties == object.getProperties().size()) {
            foundInfo = true;

            for (auto& propGroup : pex.getDebugInfo().getPropertyGroups()) {
                if (propGroup.getObjectName() == object.getName()) {
                    int propertyIndent = 0;
                    if (!propGroup.getGroupName().asString().empty()) {
                        auto stream = indent(0);
                        stream << "Group " << propGroup.getGroupName();
                        writeUserFlag(stream, propGroup, pex);
                        write(stream.str());
                        writeDocString(0, propGroup);
                        propertyIndent = 1;
                    }

                    for (auto& propName : propGroup.getNames()) {
                        for (auto& prop : object.getProperties()) {
                            if (prop.getName() == propName) {
                                writeProperty(propertyIndent, prop, object, pex);
                                goto ContinueOrder;
                            }
                        }
                        // If we get here, then we failed to find the struct
                        // member in the debug info :(
                        throw std::runtime_error("Unable to locate the property by the name of '" + propName.asString() + "' referenced in the debug info");
                    ContinueOrder:
                        continue;
                    }

                    if (!propGroup.getGroupName().asString().empty()) {
                        write(indent(0) << "EndGroup");
                        write("");
                    }
                }
            }
        }
    }

    if (!foundInfo) {
        for (auto& prop : object.getProperties())
            writeProperty(0, prop, object, pex);
    }
}

/**
* @brief Write the property definition.
* @param i The indent level.
* @param prop The property to write.
* @param object Object containing the properties definitions.
* @param pex Binary to decompile.
*/
void Decompiler::PscCoder::writeProperty(int i, const Pex::Property& prop, const Pex::Object &object, const Pex::Binary& pex)
{
    const auto noState = pex.getStringTable().findIdentifier("");
    auto stream = indent(i);
    auto isAutoReadOnly = !prop.hasAutoVar() &&
                           prop.isReadable() &&
                          !prop.isWritable() &&
                           prop.getReadFunction().getInstructions().size() == 1 &&
                           prop.getReadFunction().getInstructions()[0].getOpCode() == Pex::OpCode::RETURN &&
                           prop.getReadFunction().getInstructions()[0].getArgs().size() == 1 &&
                           prop.getReadFunction().getInstructions()[0].getArgs()[0].getType() != Pex::ValueType::Identifier;
    stream << mapType(prop.getTypeName().asString()) << " Property " << prop.getName().asString();
    if (prop.hasAutoVar()) {
        auto var = object.getVariables().findByName(prop.getAutoVarName());
        if (var == nullptr)
            throw std::runtime_error("Auto variable for property not found");

        auto initialValue = var->getDefaultValue();
        if (initialValue.getType() != Pex::ValueType::None)
            stream << " = " << initialValue.toString();
        stream << " Auto";

        // The flags defined on the variable must be set on the property
        writeUserFlag(stream, *var, pex);
        if (var->getConstFlag())
          stream << " Const";
    } else if (isAutoReadOnly) {
      stream << " = " << prop.getReadFunction().getInstructions()[0].getArgs()[0].toString();
      stream << " AutoReadOnly";
    }
    writeUserFlag(stream, prop, pex);
    write(stream.str());
    writeDocString(i, prop);

    if (!prop.hasAutoVar() && !isAutoReadOnly) {
        if (prop.isReadable())
            writeFunction(i + 1, prop.getReadFunction(), object, pex, pex.getDebugInfo().getFunctionInfo(object.getName(),noState, prop.getName(), Pex::DebugInfo::FunctionType::Getter), "Get");
        if (prop.isWritable())
            writeFunction(i + 1, prop.getWriteFunction(), object, pex, pex.getDebugInfo().getFunctionInfo(object.getName(),noState, prop.getName(), Pex::DebugInfo::FunctionType::Setter), "Set");
        write(indent(i) << "EndProperty");
    }
}

/**
 * @brief Write the variables stored in the object.
 * @param object Object containing the variables.
 * @param pex Binary to decompile.
 */
void Decompiler::PscCoder::writeVariables(const Pex::Object &object, const Pex::Binary &pex)
{
    for (auto& var : object.getVariables())
    {
        auto name = var.getName().asString();
        bool compilerGenerated = (name.size() > 2 && name[0] == ':' && name[1] == ':');
        auto stream = indent(0);

        if (compilerGenerated)
            stream << "; ";

        stream << mapType(var.getTypeName().asString()) << " " << name;
        auto initialValue = var.getDefaultValue();
        if (initialValue.getType() != Pex::ValueType::None)
        {
            stream << " = " << initialValue.toString();
        }
        writeUserFlag(stream, var, pex);
        if (var.getConstFlag())
          stream << " Const";

        if (m_CommentAsm || !compilerGenerated)
        {
            write(stream.str());
        }
    }
}

/**
 * @brief Write the guards contained in the object.
 * @param object Object containing the guards.
 * @param pex Binary to decompile.
 */
void Decompiler::PscCoder::writeGuards(const Pex::Object& object, const Pex::Binary& pex) {
    for (auto& guard : object.getGuards()) {
        auto name = guard.getName().asString();
        write("Guard " + name);
    }
}

/**
 * @brief Write the states contained in the object.
 * @param object Object containing the states.
 * @param pex Binary to decompile.
 */
void Decompiler::PscCoder::writeStates(const Pex::Object &object, const Pex::Binary &pex)
{
    for (auto& state : object.getStates())
    {
        auto name = state.getName().asString();
        if (name.empty())
        {
            if (state.getFunctions().size()) {
                write("");
                write(";-- Functions ---------------------------------------");
                writeFunctions(0, state, object, pex);
            }
        }
        else
        {
            write("");
            write(";-- State -------------------------------------------");
            auto stream = indent(0);

            // The auto state name canbe a different index than the state name, event if it is the same value.
            if (caselessCompare(state.getName().asString().c_str(), object.getAutoStateName().asString().c_str()) == 0)
            {
                stream << "Auto ";
            }
            write(stream.str() + "State " + state.getName().asString());
            writeFunctions(1, state, object, pex);
            write(indent(0) << "EndState");
        }
    }
}

/**
 * @brief Writes the functions associated with a state.
 * @param i The indentation level.
 * @param state State containing the functions.
 * @param object Object Containing the states.
 * @param pex Binary to decompile.
 */
void Decompiler::PscCoder::writeFunctions(int i, const Pex::State &state, const Pex::Object& object, const Pex::Binary &pex)
{
    for (auto& func : state.getFunctions())
    {
        write("");
        writeFunction(i, func, object, pex, pex.getDebugInfo().getFunctionInfo(object.getName(), state.getName(), func.getName()));
    }
}
static const std::regex tempRegex = std::regex("::temp\\d+");

/**
 * @brief Decompile a function.
 * @param i The indentation level.
 * @param function The function to decompile.
 * @param object The Object containing the function.
 * @param pex Binary to decompile.
 * @param name Name of the function. This parameter override the name stored in the function object.
 */
void Decompiler::PscCoder::writeFunction(int i, const Pex::Function &function, const Pex::Object &object,
                                         const Pex::Binary &pex, const Pex::DebugInfo::FunctionInfo *functionInfo,
                                         const std::string &name)
{
    std::string functionName = name;

    if (functionName.empty())
    {
        functionName = function.getName().asString();
    }

    bool isEvent = false;
    
    if (functionName.size() > 2 && !caselessCompare(functionName.substr(0, 2).c_str(), "on")) {
        // We'd have to check for full inheritence to do this by object type
        // Right now, we're just seeing if matches all the built-in event names.
        std::string functionLower = functionName;
        std::transform(functionLower.begin(), functionLower.end(), functionLower.begin(), ::tolower);
        if (pex.getGameType() == Pex::Binary::ScriptType::SkyrimScript){
            if (std::find(Skyrim::EventNamesLowerCase.begin(), Skyrim::EventNamesLowerCase.end(), functionLower) != Skyrim::EventNamesLowerCase.end()) {
                isEvent = true;
            }
        } else if (pex.getGameType() == Pex::Binary::ScriptType::Fallout4Script){
            if (std::find(Fallout4::EventNamesLowerCase.begin(), Fallout4::EventNamesLowerCase.end(), functionLower) != Fallout4::EventNamesLowerCase.end()) {
                isEvent = true;
            }
        } else if (pex.getGameType() == Pex::Binary::ScriptType::StarfieldScript) {
            if (std::find(Starfield::EventNamesLowerCase.begin(), Starfield::EventNamesLowerCase.end(), functionLower) != Starfield::EventNamesLowerCase.end()) {
                isEvent = true;
            }
        }
    }

    if (functionName.size() > 9 && !caselessCompare(functionName.substr(0, 9).c_str(), "::remote_")) {
      isEvent = true;
      functionName = functionName.substr(9);
      functionName[function.getParams()[0].getTypeName().asString().size()] = '.';
    }

    if (isCompilerGeneratedFunc(functionName, object, pex.getGameType())) {
        write(indent(i) << "; Skipped compiler generated " << functionName);
        return;
    }

    auto stream = indent(i);
    if (caselessCompare(function.getReturnTypeName().asString().c_str(), "none") != 0)
        stream << mapType(function.getReturnTypeName().asString()) << " ";

    if (isEvent)
      stream << "Event ";
    else
      stream << "Function ";
    stream << functionName << "(";

    auto first = true;
    for (auto& param : function.getParams())
    {
        if (first)
        {
            first = false;
        }
        else
        {
            stream << ", ";
        }
        stream << mapType(param.getTypeName().asString()) << " " << param.getName();
    }
    stream << ")";


    if (function.isGlobal())
    {
        stream << " Global";
    }
    if (function.isNative())
    {
        stream << " Native";
        writeUserFlag(stream, function, pex);
        write(stream.str());
        writeDocString(i, function);
    } else {
        auto decomp = PscDecompiler(function, object, functionInfo, m_CommentAsm, m_TraceDecompilation, m_DumpTree,
                                    m_OutputDir);
        if (decomp.isDebugFunction()) {
            // Starfield debug function fixup hacks
            // These functions were supposed to have been compiled out of the pex, but the compiler left it in without restoring whatever the temp variable pointed to
            // This causes the recompilation to fail, so we need to replace the temp variable with false

            bool fixed = false;
            if (pex.getGameType() == Pex::Binary::ScriptType::StarfieldScript) {
                if (functionName == "warning" ||
                    (caselessCompare(object.getName().asString().c_str(), "ENV_Hazard_ParentScript") == 0 &&
                     functionName == "GlobalWarning") || // only present on this script
                    (caselessCompare(object.getName().asString().c_str(), "ENV_AfflictionScript") == 0 &&
                     functionName == "TraceStats")) { // Only present on this script
                  // find the `::temp\d+` variable in the lines with regex
                  // replace it with `false`
                  fixed = true;
                  for (auto &line: decomp) {
                    if (std::regex_search(line, tempRegex)) {
                      line = std::regex_replace(line, tempRegex, "false");
                    }
                  }
                } else if ((caselessCompare(object.getName().asString().c_str(), "RobotQuestRunner") == 0)) {
                    if (functionName == "UpdateState") {
                      fixed = true;
                      for (auto &line: decomp) {
                        if (std::regex_search(line, tempRegex)) {
                          line = std::regex_replace(line, tempRegex, "None");
                        }
                      }
                    } else if (functionName == "MakeQuestNameSave") {
                      fixed = true;
                      for (auto &line: decomp) {
                        if (std::regex_search(line, tempRegex)) {
                          line = std::regex_replace(line, tempRegex, "questName");
                        }
                      }
                    }
                }

            }
            if (fixed){
              write(indent(i) << "; Fixup hacks for debug-only function: " << functionName);
            } else if (m_WriteDebugFuncs) {
              write(indent(i) << "; WARNING: possibly inoperative debug function " << functionName << "");
            } else {
              write(indent(i) << "; Skipped inoperative debug function " << functionName);
              return;
            }
        } else if (caselessCompare(functionName.c_str(), "GotoState") == 0 || caselessCompare(functionName.c_str(), "GetState") == 0) {
            // Starfield GotoState/GetState function fixup hacks
            if (caselessCompare(object.getName().asString().c_str(), "ScriptObject") == 0) {
                // find the `::State` variable in the lines
                // replace it with `__state`
                write(indent(i) << "; Fixup hacks for native ScriptObject::GotoState/GetState");
                for (auto &line : decomp){
                    if (line.find("::State") != std::string::npos)
                    {
                        line = std::regex_replace(line, std::regex("::State"), "__state");
                    }
                }
            }
        }


        writeUserFlag(stream, function, pex);
        write(stream.str());
        writeDocString(i, function);
        auto index = 0;
        for (auto &line: decomp) {
            auto & linemap = decomp.getLineMap();
            if (m_PrintDebugLineNo){
              // get index of line
              auto result = linemap[index];
              if (result.size() > 0){
                line += " ; #DEBUG_LINE_NO:";
                for (auto i = 0; i < result.size(); ++i)
                {
                    if (i > 0){
                    line += ",";
                    }
                    line += std::to_string(result[i]);
                }
              }
            }
            write(indent(i+1) << line);
            index++;
        }
        if (isEvent)
          write(indent(i) << "EndEvent");
        else
          write(indent(i) << "EndFunction");
    }

}

/**
 * @brief Write the user flags associated with an item.
 * @param stream Stream to write the flags to.
 * @param flagged Flagged item.
 * @param pex Binary to decompile.
 */
void Decompiler::PscCoder::writeUserFlag(std::ostream& stream, const Pex::UserFlagged &flagged, const Pex::Binary &pex)
{
    auto flags = flagged.getUserFlags();
    for (auto& flag : pex.getUserFlags())
    {
        if (flags & flag.getFlagMask())
        {
            stream << " " << flag.getName().asString();
        }
    }
}

/**
 * @brief Write the documentation string of an item.
 * @param i Indentation level.
 * @param item Documented item.
 */
void Decompiler::PscCoder::writeDocString(int i, const Pex::DocumentedItem &item)
{
    if (! item.getDocString().asString().empty())
    {
        write(indent(i) << "{ " << item.getDocString().asString() << " }");
    }
}

static const std::map<std::string, std::string> prettyTypeNameMap {
    // Builtin Types
    { "bool", "Bool" },
    { "float", "Float" },
    { "int", "Int" },
    { "string", "String" },
    { "var", "Var" },

    // Special
    { "self", "Self" },

    // General Types
    { "action", "Action" },
    { "activator", "Activator" },
    { "activemagiceffect", "ActiveMagicEffect" },
    { "actor", "Actor" },
    { "actorbase", "ActorBase" },
    { "actorvalue", "ActorValue" },
    { "alias", "Alias" },
    { "ammo", "Ammo" },
    { "apparatus", "Apparatus" },
    { "armor", "Armor" },
    { "associationtype", "AssociationType" },
    { "book", "Book" },
    { "cell", "Cell" },
    { "class", "Class" },
    { "constructibleobject", "ConstructibleObject" },
    { "container", "Container" },
    { "debug", "Debug" },
    { "door", "Door" },
    { "effectshader", "EffectShader" },
    { "enchantment", "Enchantment" },
    { "encounterzone", "EncounterZone" },
    { "explosion", "Explosion" },
    { "faction", "Faction" },
    { "flora", "Flora" },
    { "form", "Form" },
    { "formlist", "FormList" },
    { "furniture", "Furniture" },
    { "game", "Game" },
    { "globalvariable", "GlobalVariable" },
    { "hazard", "Hazard" },
    { "idle", "Idle" },
    { "imagespacemodifier", "ImageSpaceModifier" },
    { "impactdataset", "ImpactDataSet" },
    { "ingredient", "Ingredient" },
    { "key", "Key" },
    { "keyword", "Keyword" },
    { "leveledactor", "LeveledActor" },
    { "leveleditem", "LeveledItem" },
    { "leveledspell", "LeveledSpell" },
    { "light", "Light" },
    { "location", "Location" },
    { "locationalias", "LocationAlias" },
    { "locationreftype", "LocationRefType" },
    { "magiceffect", "MagicEffect" },
    { "math", "Math" },
    { "message", "Message" },
    { "miscobject", "MiscObject" },
    { "musictype", "MusicType" },
    { "objectreference", "ObjectReference" },
    { "outfit", "Outfit" },
    { "package", "Package" },
    { "perk", "Perk" },
    { "potion", "Potion" },
    { "projectile", "Projectile" },
    { "quest", "Quest" },
    { "race", "Race" },
    { "referencealias", "ReferenceAlias" },
    { "refcollectionalias", "RefCollectionAlias" },
    { "scene", "Scene" },
    { "scroll", "Scroll" },
    { "scriptobject", "ScriptObject" },
    { "shout", "Shout" },
    { "soulgem", "SoulGem" },
    { "sound", "Sound" },
    { "soundcategory", "SoundCategory" },
    { "spell", "Spell" },
    { "static", "Static" },
    { "talkingactivator", "TalkingActivator" },
    { "topic", "Topic" },
    { "topicinfo", "TopicInfo" },
    { "utility", "Utility" },
    { "visualeffect", "VisualEffect" },
    { "voicetype", "VoiceType" },
    { "weapon", "Weapon" },
    { "weather", "Weather" },
    { "wordofpower", "WordOfPower" },
    { "worldspace", "WorldSpace" },
};

void str_to_lower(std::string &p_str){
    for (int i = 0; i < p_str.size(); i++){
        p_str[i] = tolower(p_str[i]);
    }
}
/**
* @brief Map the type name used by the compiler to the form most used by people.
* @param type The type to map.
*/
std::string Decompiler::PscCoder::mapType(std::string type)
{
    std::replace(type.begin(), type.end(), '#', ':');
    if (type.length() > 2 && type[type.length() - 2] == '[' && type[type.length() - 1] == ']')
        return mapType(type.substr(0, type.length() - 2)) + "[]";
    auto lowerType = type;
    str_to_lower(lowerType);
    auto a = prettyTypeNameMap.find(lowerType);
    if (a != prettyTypeNameMap.end())
        return a->second;
    return type;
}

bool Decompiler::PscCoder::isCompilerGeneratedFunc(const std::string &name, const Pex::Object &object, Pex::Binary::ScriptType scriptType) const {
    static const std::vector<std::string> globalCompilerGeneratedFuncs = {
            "getstate",
            "gotostate",
    };
    static const std::vector<std::string> starfieldCompilerGeneratedFuncs = {
    };
    // Do not remove these for the actual `scriptobject` script which is the base class for all scripts
    if (caselessCompare(object.getName().asString().c_str(), "ScriptObject") == 0){
        return false;
    }
    std::string nameLower = name;
    str_to_lower(nameLower);
    if (std::find(globalCompilerGeneratedFuncs.begin(), globalCompilerGeneratedFuncs.end(), nameLower) != globalCompilerGeneratedFuncs.end())
        return true;
    if (scriptType == Pex::Binary::ScriptType::StarfieldScript && std::find(starfieldCompilerGeneratedFuncs.begin(), starfieldCompilerGeneratedFuncs.end(), name) != starfieldCompilerGeneratedFuncs.end())
        return true;
    return false;
}
```

## File: `Decompiler/PscCoder.hpp`
```
#pragma once
#include "Coder.hpp"


namespace Decompiler {
static const char* WARNING_COMMENT_PREFIX = ";***";
/**
 * @brief Write a PEX file as a PSC file.
 */
class PscCoder :
        public Coder
{
public:
    PscCoder(OutputWriter *writer, bool commentAsm, bool writeHeader, bool traceDecompilation, bool dumpTree,
             bool writeDebugFuncs, bool printDebugLineNo, std::string traceDir);
    PscCoder(OutputWriter* writer);
    ~PscCoder();

    virtual void code(const Pex::Binary& pex);

    PscCoder& outputDecompilationTrace(bool traceDecompilation);
    PscCoder& outputDumpTree(bool dumpTree);
    PscCoder& outputAsmComment(bool commentAsm);
    PscCoder& outputWriteHeader(bool writeHeader);
    static std::string mapType(std::string type);
protected:

    void writeHeader(const Pex::Binary& pex);
    void writeObject(const Pex::Object& object, const Pex::Binary& pex);
    void writeStructs(const Pex::Object& object, const Pex::Binary& pex);
    void writeStructMember(const Pex::StructInfo::Member& member, const Pex::Binary& pex);
    void writeProperties(const Pex::Object& object, const Pex::Binary& pex);
    void writeProperty(int i, const Pex::Property& prop, const Pex::Object &object, const Pex::Binary& pex);
    void writeVariables(const Pex::Object& object, const Pex::Binary& pex);
    void writeGuards(const Pex::Object& object, const Pex::Binary& pex);
    void writeStates(const Pex::Object& object, const Pex::Binary& pex);
    void writeFunctions(int i, const Pex::State& state, const Pex::Object &object, const Pex::Binary& pex);
    void writeFunction(int i, const Pex::Function &function, const Pex::Object &object,
                       const Pex::Binary &pex, const Pex::DebugInfo::FunctionInfo *functionInfo,
                       const std::string &name = "");

    void writeUserFlag(std::ostream &stream, const Pex::UserFlagged& flagged, const Pex::Binary& pex);
    void writeDocString(int i, const Pex::DocumentedItem& item);

protected:
    bool m_CommentAsm;
    bool m_WriteHeader;
    bool m_TraceDecompilation;
    bool m_DumpTree;
    bool m_WriteDebugFuncs;
    bool m_PrintDebugLineNo;
    std::string m_OutputDir;



    bool isNativeObject(const Pex::Object &object, const Pex::Binary::ScriptType &scriptType) const;

    bool isCompilerGeneratedFunc(const std::string &name, const Pex::Object &object,
                                 Pex::Binary::ScriptType scriptType) const;
};
}
```

## File: `Decompiler/PscDecompiler.cpp`
```cpp
#include "PscDecompiler.hpp"

#include <cassert>
#include <cstdint>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <atomic>
#include <mutex>

#include "Node/Nodes.hpp"
#include "Node/WithNode.hpp"
#include "Node/NodeComparer.hpp"

#include "PscCodeGenerator.hpp"
#include <Champollion/CaselessCompare.h>


static inline
bool isTempVar(const Pex::StringTable::Index& var)
{
    auto& name = var.asString();
    return (name.length() > 6 && name.substr(0, 6) == "::temp" && name.substr(name.length() - 4, 4) != "_var") || caselessCompare(name.c_str(), "::nonevar") == 0;
}
static inline
bool isMangledVar(const Pex::StringTable::Index& var)
{
    auto& name = var.asString();
    return name.length() > 12 && name.substr(0, 10) == "::mangled_";
}

static inline
std::string getVarName(const Pex::StringTable::Index& var)
{
    auto& name = var.asString();
    if (name.length() > 6 && name.substr(0, 2) == "::" && name.substr(name.length() - 4, 4) == "_var")
    {
        return name.substr(2, name.length() - 6);
    }
    else if (name.length() > 12 && name.substr(0, 10) == "::mangled_")
    {
        auto index = name.rfind('_');
        return name.substr(10, index - 10);
    }

    return name;
}

static std::atomic_size_t unnamed_num{0};

/**
 * @brief Constructor.
 * The constructor associate the function and object to the decompiler.
 *
 * @param function Function to decompile.
 * @param object Object containing the function.
 * @param commentAsm True to output assembly instruction comments.
 * @param traceDecompilation True to output decompilation tracing to the rebuild log.
 * @param dumpTree True to output the entire tree for each block (true by default if traceDecompilation is true).
 */
Decompiler::PscDecompiler::PscDecompiler(const Pex::Function &function, const Pex::Object &object,
                                         const Pex::DebugInfo::FunctionInfo *debugInfo, bool commentAsm = false,
                                         bool traceDecompilation = false, bool dumpTree = true,
                                         std::string outputDir = "") :
    m_Function(function),
    m_Object(object),
    m_CommentAsm(commentAsm),
    m_TraceDecompilation(traceDecompilation),
    m_DumpTree(dumpTree), // Note that while dumpTree is true by default, it will not do anything unless traceDecompilation is true
    m_DebugInfo(debugInfo ? *debugInfo : Pex::DebugInfo::FunctionInfo()),
    m_OutputDir(outputDir)
{
    if (m_TraceDecompilation)
    {
        auto fileprefix = std::string("rebuild-") + object.getName()
                + "-";     
        std::string filename;
        if (function.getName().isValid()){
            filename = fileprefix + function.getName() + ".txt";
        } else {
            fileprefix += "unnamed";
            // in case of parallel execution
            static std::mutex unnamed_num_mutex;
            std::lock_guard m(unnamed_num_mutex);
            filename = fileprefix + std::to_string(++unnamed_num) + ".txt";
        }
        std::replace(filename.begin(), filename.end(), '#', '_');
        std::replace(filename.begin(), filename.end(), ':', '_');
        std::string filepath = !m_OutputDir.empty() ? m_OutputDir + "/" + filename : filename;
        m_Log.open(filepath);
        if (m_Log.fail())
        {
            m_TraceDecompilation = false;
            static std::mutex cerr_mutex;
            std::lock_guard m(cerr_mutex);
            std::cerr << "Failed to open " << filepath << ", tracing disabled." << std::endl;
        }
    }
    if (m_Function.getInstructions().size() == 0)
    {
        push_back("; Empty function");
    }
    else
    {
        m_ReturnNone = (m_Function.getReturnTypeName() == m_Object.getName().getTable()->findIdentifier("NONE"));
        m_TempTable.push_back("true");
        m_TempTable.push_back("false");

        m_TempTable.push_back("find");
        m_TempTable.push_back("findstruct");
        m_TempTable.push_back("rfind");
        m_TempTable.push_back("rfindstruct");
        m_TempTable.push_back("add");
        m_TempTable.push_back("insert");
        m_TempTable.push_back("removelast");
        m_TempTable.push_back("remove");
        m_TempTable.push_back("clear");
        m_TempTable.push_back("GetMatchingStructs"); // TODO: VERIFY: Need to verify syntax when CK for Starfield comes out

        //findReplacedVars();
        findVarTypes();

        createFlowBlocks();

        rebuildExpressionsInBlocks();

        rebuildBooleanOperators(0, m_Function.getInstructions().size());


        Node::BasePtr programTree = rebuildControlFlow(0, m_Function.getInstructions().size());

        declareVariables(programTree);

        rebuildLocks(programTree);

        cleanUpTree(programTree);

        generateCode(programTree);

    }
}

/**
 * @brief Destructor
 */
Decompiler::PscDecompiler::~PscDecompiler()
{
    for (auto& bloc_kv : m_CodeBlocs)
    {
        auto& bloc = bloc_kv.second;
        delete bloc;
    }
}

/**
 * @brief Output a range of instruction as assembly comment.
 * @param level Indentation level.
 * @param begin First instruction to output.
 * @param end Last instruction to output.
 */

void Decompiler::PscDecompiler::decodeToAsm(std::uint8_t level, size_t begin, size_t end)
{
    if (m_CommentAsm)
    {
        auto& instructions = m_Function.getInstructions();

        if (begin >= instructions.size() || end >= instructions.size())
        {
            return;
        }

        for (auto ip = begin; ip <= end; ++ip)
        {
            auto& ins = instructions[ip];
            std::ostringstream stream;
            for (auto i = 0; i < level; ++i)
            {
                stream << ' ' << ' ';
            }
            stream << "; " << std::setw(3) << std::setfill('0') << ip << " : " << ins.getOpCodeName() << " ";
            switch(ins.getOpCode())
            {
            case Pex::OpCode::JMP:
            {
                assert(ins.getArgs().size() == 1);
                assert(ins.getArgs()[0].getType() == Pex::ValueType::Integer);

                auto target = ip + ins.getArgs()[0].getInteger();
                stream << std::setw(3) << std::setfill('0') << target;
            }
                break;
            case Pex::OpCode::JMPF:
            case Pex::OpCode::JMPT:
            {
                assert(ins.getArgs().size() == 2);
                assert(ins.getArgs()[1].getType() == Pex::ValueType::Integer);

                stream << ins.getArgs()[0].toString() << " ";
                auto target = ip + ins.getArgs()[1].getInteger();
                stream << std::setw(3) << std::setfill('0') << target;

            }
                break;
            default:
            {
                for (auto& arg : ins.getArgs())
                {
                    stream << arg.toString() << " ";
                }

                if (ins.hasVarArgs())
                {
                    for (auto& arg : ins.getVarArgs())
                    {
                        stream << arg.toString() << " ";
                    }
                }
            }
                break;
            }


            push_back(stream.str());
        }
    }
}

/**
 * @brief Finds the type of the variables.
 *
 * This function finds the type of the local variables and parameters accessible in the function's scope.
 * The types are stored in m_VarTypes.
 */
void Decompiler::PscDecompiler::findVarTypes()
{
    for (auto& var : m_Object.getVariables())
        m_VarTypes[var.getName().asIndex()] = var.getTypeName();
    for (auto& var : m_Function.getParams())
        m_VarTypes[var.getName().asIndex()] = var.getTypeName();
    for (auto& var : m_Function.getLocals())
        m_VarTypes[var.getName().asIndex()] = var.getTypeName();

    m_NoneVar = m_Object.getName().getTable()->findIdentifier("::nonevar");
}

/**
 * @brief Get the type of a variable.
 * @param var Name index of the variable.
 * @return The name index of the type.
 */
const Pex::StringTable::Index& Decompiler::PscDecompiler::typeOfVar(const Pex::StringTable::Index &var) const
{
    static const Pex::StringTable::Index UNDEFINED;
    auto it = m_VarTypes.find(var.asIndex());
    if (it == m_VarTypes.end())
    {
        return UNDEFINED;
    }
    else
    {
        assert(it->second.isValid());
        return it->second;
    }
}

/**
 * @brief Creates the code blocks graph.
 *
 * This function goes through the instruction list and creates the code block representation
 * to allow further flow analysis. Each block contains an uninterrupted sequence of instruction which will be
 * reconstructed as statements sequence. A blocks ends at a jump, conditional or not. The target of the jump
 * will mark the beginning of a new block.
 */
void Decompiler::PscDecompiler::createFlowBlocks()
{
    auto& instructions = m_Function.getInstructions();
    auto full = new PscCodeBlock(0, instructions.size() - 1);
    full->setNext(instructions.size());

    m_CodeBlocs[full->getBegin()] = full;
    m_CodeBlocs[instructions.size()] = new PscCodeBlock(instructions.size(), PscCodeBlock::END);

    auto ip = 0;
    for (auto& ins : instructions)
    {
        auto block = findBlockForInstruction(ip);
        switch(ins.getOpCode())
        {
//        case Pex::OpCode::LOCK_GUARDS:
//        {
//            assert(ins.getArgs().size() >= 1);
//            for (auto& arg : ins.getArgs())
//            {
//                assert(arg.getType() == Pex::ValueType::Identifier);
//                auto var = arg.getId();
//                auto& varName = var.asString();
//                if (varName.length() > 6 && varName.substr(0, 6) == "::temp")
//                {
//                    auto& block = m_CodeBlocs[ip];
//                    block->addLockGuard(var);
//                }
//            }
//        }
        case Pex::OpCode::JMP:
        {
            assert(ins.getArgs().size() == 1);
            assert(ins.getArgs()[0].getType() == Pex::ValueType::Integer);

            auto target = ip + ins.getArgs()[0].getInteger();

            // Unconditional jump
            // Split the block at the jump and set the next block to the target of the jump.
            if (m_CodeBlocs.find(ip+1) == m_CodeBlocs.end())
            {
                auto newBlock = m_CodeBlocs[block]->split(ip+1);
                m_CodeBlocs[newBlock->getBegin()] = newBlock;

            }
            m_CodeBlocs[block]->setNext(target);

            if (m_CodeBlocs.find(target) == m_CodeBlocs.end())
            {
                auto containingBlock = m_CodeBlocs[findBlockForInstruction(target)];
                auto targetBlock = containingBlock->split(target);
                m_CodeBlocs[targetBlock->getBegin()] = targetBlock;
            }


        }
            break;
        case Pex::OpCode::JMPF:
        case Pex::OpCode::JMPT:
        {
            assert(ins.getArgs().size() == 2);
            assert(ins.getArgs()[0].getType() == Pex::ValueType::Identifier || ins.getArgs()[0].getType() == Pex::ValueType::Bool || ins.getArgs()[0].getType() == Pex::ValueType::Integer);
            assert(ins.getArgs()[1].getType() == Pex::ValueType::Integer);

            // Conditional jump
            // The block is split at the jump.
            // The block condition is set to the condition of the jump,
            // The true and false block are set to the target of the jump, and the instruction following the jump.
            // The true or false order is decided from the kind of jump (jmpf/jmpt).
            auto target = ip + ins.getArgs()[1].getInteger();
            if (m_CodeBlocs.find(ip+1) == m_CodeBlocs.end())
            {
                auto newBlock = m_CodeBlocs[block]->split(ip+1);
                m_CodeBlocs[newBlock->getBegin()] = newBlock;
            }

            if (m_CodeBlocs.find(target) == m_CodeBlocs.end())
            {
                auto containingBlock = m_CodeBlocs[findBlockForInstruction(target)];
                auto targetBlock = containingBlock->split(target);
                m_CodeBlocs[targetBlock->getBegin()] = targetBlock;
            }

            Pex::StringTable::Index condition;
            if (ins.getArgs()[0].getType() == Pex::ValueType::Identifier)
            {
                condition = ins.getArgs()[0].getId();
            }
            else if (ins.getArgs()[0].getType() == Pex::ValueType::Bool)
            {
                if(ins.getArgs()[0].getBool())
                {
                    condition = m_TempTable.findIdentifier("true");
                }
                else
                {
                    condition = m_TempTable.findIdentifier("false");
                }
            }
            else {
                condition = m_TempTable.get(ins.getArgs()[0].getInteger());
            }

            if (ins.getOpCode() == Pex::OpCode::JMPF)
            {
                m_CodeBlocs[block]->setCondition(condition, ip + 1, target);
            }
            else
            {
                m_CodeBlocs[block]->setCondition(condition, target, ip + 1);
            }
        }
            break;
        default:
            break;
        }

        ++ip;
    }

    // Creates the nodes for the blocs.
    for (auto& bloc_kv : m_CodeBlocs)
    {
        createNodesForBlocks(bloc_kv.first);
    }
}

/**
 * @brief Create the statement nodes for the block.
 *
 * This function creates the statement nodes for each instruction of the blocks.
 * From each instruction, a set of nodes representing the corresponding Papyrus statement.
 *
 * @param block Indice of the block.
 */
void Decompiler::PscDecompiler::createNodesForBlocks(size_t block)
{
    auto code = m_CodeBlocs[block];
    auto& instructions = m_Function.getInstructions();
    auto scope = code->getScope();
    if (code->getBegin() < instructions.size())
    {
        for(auto ip = code->getBegin(); ip <= code->getEnd(); ++ip)
        {
            auto& ins = instructions[ip];

            auto& args = ins.getArgs();
            auto& varargs = ins.getVarArgs();

            Node::BasePtr node;
            switch (ins.getOpCode()) {
                case Pex::OpCode::NOP:
                    //do nothing
                    break;
                case Pex::OpCode::IADD:
                case Pex::OpCode::FADD:
                case Pex::OpCode::STRCAT:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 5, args[0].getId(), fromValue(ip, args[1]), "+", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::ISUB:
                case Pex::OpCode::FSUB:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 5, args[0].getId(), fromValue(ip, args[1]), "-", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::IMUL:
                case Pex::OpCode::FMUL:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 4, args[0].getId(), fromValue(ip, args[1]), "*", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::IDIV:
                case Pex::OpCode::FDIV:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 4, args[0].getId(), fromValue(ip, args[1]), "/", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::IMOD:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 4, args[0].getId(), fromValue(ip, args[1]), "%", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::NOT:
                {
                    node = std::make_shared<Node::UnaryOperator>(ip, 3, args[0].getId(), "!", fromValue(ip, args[1]));
                    break;
                }
                case Pex::OpCode::INEG:
                case Pex::OpCode::FNEG:
                {
                    node = std::make_shared<Node::UnaryOperator>(ip, 3, args[0].getId(), "-", fromValue(ip, args[1]));
                    break;
                }
                case Pex::OpCode::ASSIGN:
                {
                    node = std::make_shared<Node::Copy>(ip, args[0].getId(), fromValue(ip, args[1]));
                    break;
                }
                case Pex::OpCode::CAST:
                {
                    if (args[1].getType() == Pex::ValueType::None) {
                        node = std::make_shared<Node::Copy>(ip, args[0].getId(), fromValue(ip, args[1]));
                    } else if (args[1].getType() != Pex::ValueType::Identifier || (typeOfVar(args[0].getId()) != typeOfVar(args[1].getId()) && args[1].getId() != m_NoneVar)) {
                        node = std::make_shared<Node::Cast>(ip, args[0].getId(), fromValue(ip, args[1]), typeOfVar(args[0].getId()));
                    } else // two variables of the same type, equivalent to an assign
                    {
                        node = std::make_shared<Node::Copy>(ip, args[0].getId(), fromValue(ip, args[1]));
                    }
                    break;
                }
                case Pex::OpCode::CMP_EQ:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 5, args[0].getId(), fromValue(ip, args[1]), "==", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::CMP_LT:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 5, args[0].getId(), fromValue(ip, args[1]), "<", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::CMP_LTE:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 5, args[0].getId(), fromValue(ip, args[1]), "<=", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::CMP_GT:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 5, args[0].getId(), fromValue(ip, args[1]), ">", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::CMP_GTE:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 5, args[0].getId(), fromValue(ip, args[1]), ">=", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::JMP:
                case Pex::OpCode::JMPT:
                case Pex::OpCode::JMPF:
                    //do nothing
                    break;
                case Pex::OpCode::CALLMETHOD:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(ip, args[2].getId(), fromValue(ip, args[1]), args[0].getId());
                    auto argNode = callNode->getParameters();
                    for (auto varg : varargs) {
                        *argNode << fromValue(ip, varg);
                    }
                    node = callNode;
                    break;
                }
                case Pex::OpCode::CALLPARENT:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(ip, args[1].getId(), std::make_shared<Node::IdentifierString>(ip, "Parent"), args[0].getId());
                    auto argNode = callNode->getParameters();
                    for (auto varg : varargs) {
                        *argNode << fromValue(ip, varg);
                    }
                    node = callNode;
                    break;
                }
                case Pex::OpCode::CALLSTATIC:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(ip, args[2].getId(), fromValue(ip, args[0]), args[1].getId());
                    auto argNode = callNode->getParameters();
                    for (auto varg : varargs) {
                        *argNode << fromValue(ip, varg);
                    }
                    node = callNode;
                    break;
                }
                case Pex::OpCode::RETURN:
                {
                    if (m_ReturnNone) {
                        node = std::make_shared<Node::Return>(ip, nullptr);
                    } else {
                        node = std::make_shared<Node::Return>(ip, fromValue(ip, args[0]));
                    }
                    break;
                }

                case Pex::OpCode::PROPGET:
                {
                    node = std::make_shared<Node::PropertyAccess>(ip, args[2].getId(), fromValue(ip, args[1]), args[0].getId());
                    break;
                }
                case Pex::OpCode::PROPSET:
                {
                    node = std::make_shared<Node::PropertyAccess>(ip, Pex::StringTable::Index(), fromValue(ip, args[1]), args[0].getId());
                    node = std::make_shared<Node::Assign>(ip, node, fromValue(ip, args[2]));
                    break;
                }

                case Pex::OpCode::ARRAY_CREATE:
                {
                    node = std::make_shared<Node::ArrayCreate>(ip, args[0].getId(), typeOfVar(args[0].getId()), fromValue(ip, args[1]));
                    break;
                }
                case Pex::OpCode::ARRAY_LENGTH:
                {
                    node = std::make_shared<Node::ArrayLength>(ip, args[0].getId(), fromValue(ip, args[1]));
                    break;
                }
                case Pex::OpCode::ARRAY_GETELEMENT:
                {
                    node = std::make_shared<Node::ArrayAccess>(ip, args[0].getId(), fromValue(ip, args[1]), fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::ARRAY_SETELEMENT:
                {
                    node = std::make_shared<Node::ArrayAccess>(ip, Pex::StringTable::Index(), fromValue(ip, args[0]), fromValue(ip, args[1]));
                    node = std::make_shared<Node::Assign>(ip, node, fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::ARRAY_FINDELEMENT:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(ip, args[1].getId(), fromValue(ip, args[0]), m_TempTable.findIdentifier(("find")));
                    auto argNode = callNode->getParameters();
                    *argNode << fromValue(ip, args[2]);
                    *argNode << fromValue(ip, args[3]);
                    node = callNode;
                    break;
                }
                case Pex::OpCode::ARRAY_RFINDELEMENT:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(ip, args[1].getId(), fromValue(ip, args[0]), m_TempTable.findIdentifier(("rfind")));
                    auto argNode = callNode->getParameters();
                    *argNode << fromValue(ip, args[2]);
                    *argNode << fromValue(ip, args[3]);

                    node = callNode;
                    break;
                }
                case Pex::OpCode::IS:
                {
                    node = std::make_shared<Node::BinaryOperator>(ip, 0, args[0].getId(), fromValue(ip, args[1]), "is", fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::STRUCT_CREATE:
                {
                    node = std::make_shared<Node::StructCreate>(ip, args[0].getId(), typeOfVar(args[0].getId()));
                    break;
                }
                case Pex::OpCode::STRUCT_GET:
                {
                    node = std::make_shared<Node::PropertyAccess>(ip, args[0].getId(), fromValue(ip, args[1]), args[2].getId());
                    break;
                }
                case Pex::OpCode::STRUCT_SET:
                {
                    node = std::make_shared<Node::PropertyAccess>(ip, Pex::StringTable::Index(), fromValue(ip, args[0]), args[1].getId());
                    node = std::make_shared<Node::Assign>(ip, node, fromValue(ip, args[2]));
                    break;
                }
                case Pex::OpCode::ARRAY_FINDSTRUCT:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(ip, args[1].getId(), fromValue(ip, args[0]), m_TempTable.findIdentifier("findstruct"));
                    auto argNode = callNode->getParameters();
                    *argNode << fromValue(ip, args[2]);
                    *argNode << fromValue(ip, args[3]);
                    *argNode << fromValue(ip, args[4]);

                    node = callNode;
                    break;
                }
                case Pex::OpCode::ARRAY_RFINDSTRUCT:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(ip, args[1].getId(), fromValue(ip, args[0]), m_TempTable.findIdentifier("rfindstruct"));
                    auto argNode = callNode->getParameters();
                    *argNode << fromValue(ip, args[2]);
                    *argNode << fromValue(ip, args[3]);
                    *argNode << fromValue(ip, args[4]);

                    node = callNode;
                    break;
                }
                case Pex::OpCode::ARRAY_ADD:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(ip, Pex::StringTable::Index(), fromValue(ip, args[0]), m_TempTable.findIdentifier("add"));
                    auto argNode = callNode->getParameters();
                    *argNode << fromValue(ip, args[1]);
                    *argNode << fromValue(ip, args[2]);

                    node = callNode;
                    break;
                }
                case Pex::OpCode::ARRAY_INSERT:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(ip, Pex::StringTable::Index(), fromValue(ip, args[0]), m_TempTable.findIdentifier("insert"));
                    auto argNode = callNode->getParameters();
                    *argNode << fromValue(ip, args[1]);
                    *argNode << fromValue(ip, args[2]);

                    node = callNode;
                    break;
                }
                case Pex::OpCode::ARRAY_REMOVELAST:
                {
                    node = std::make_shared<Node::CallMethod>(ip, Pex::StringTable::Index(), fromValue(ip, args[0]), m_TempTable.findIdentifier("removelast"));
                    break;
                }
                case Pex::OpCode::ARRAY_REMOVE:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(ip, Pex::StringTable::Index(), fromValue(ip, args[0]), m_TempTable.findIdentifier("remove"));
                    auto argNode = callNode->getParameters();
                    *argNode << fromValue(ip, args[1]);
                    *argNode << fromValue(ip, args[2]);

                    node = callNode;
                    break;
                }
                case Pex::OpCode::ARRAY_CLEAR:
                {
                    node = std::make_shared<Node::CallMethod>(ip, Pex::StringTable::Index(), fromValue(ip, args[0]), m_TempTable.findIdentifier("clear"));
                    break;
                }
                case Pex::OpCode::ARRAY_GETALLMATCHINGSTRUCTS:
                {
                    auto callNode = std::make_shared<Node::CallMethod>(
                            ip,
                            args[1].getId(),
                            fromValue(ip, args[0]),
                            m_TempTable.findIdentifier("GetMatchingStructs"),
                            true); // TODO: VERIFY: remove this after verifying syntax when CK for Starfield comes out
                    auto argNode = callNode->getParameters();
                    *argNode << fromValue(ip, args[2]);
                    *argNode << fromValue(ip, args[3]);
                    *argNode << fromValue(ip, args[4]);
                    *argNode << fromValue(ip, args[5]);

                    node = callNode;
                    break;
                }
                case Pex::OpCode::LOCK_GUARDS:
                {
                    Node::BasePtr newscope = std::make_shared<Node::Scope>();

                    auto lockNode = std::make_shared<Node::GuardStatement>(ip, newscope);
                    auto argNode = lockNode->getParameters();
                    for (auto varg : varargs) {
                        *argNode << fromValue(ip, varg);
                    }
                    node = lockNode;
                    break;
                }
                case Pex::OpCode::UNLOCK_GUARDS:
                {
                    auto unlockNode = std::make_shared<Node::EndGuard>(ip);
                    auto argNode = unlockNode->getParameters();
                    for (auto varg : varargs) {
                        *argNode << fromValue(ip, varg);
                    }
                    node = unlockNode;
                    break;
                }
                case Pex::OpCode::TRY_LOCK_GUARDS:
                {
                    Node::BasePtr newscope = std::make_shared<Node::Scope>();
                    auto trylockNode = std::make_shared<Node::TryGuard>(ip, args[0].getId(), newscope);
                    auto argNode = trylockNode->getParameters();
                    for (auto varg : varargs) {
                        *argNode << fromValue(ip, varg);
                    }
                    node = trylockNode;
                    break;
                }
                default:
                {
                    throw std::runtime_error("Unknown opcode " + std::to_string(static_cast<int>(ins.getOpCode())));
                }
            }
            if (node)
            {                
                *scope << checkAssign(node);
            }
        }
    }
}

/**
 * @brief Find the block containing a given instruction.
 * @param ip Indice of the instruction.
 * @return The indice of the containing block.
 */
size_t Decompiler::PscDecompiler::findBlockForInstruction(size_t ip)
{
    for (auto& bloc_kv : m_CodeBlocs)
    {
        auto& bloc = bloc_kv.second;
        if (bloc->getBegin() <= ip && ip <= bloc->getEnd())
        {
            return bloc->getBegin();
        }
    }
    return PscCodeBlock::END;
}

/**
 * @brief Rebuild the statement for each block.
 */
void Decompiler::PscDecompiler::rebuildExpressionsInBlocks()
{

    for (auto& bloc_kv : m_CodeBlocs)
    {
        auto& bloc = bloc_kv.second;

        auto scope = bloc->getScope();
        rebuildExpression(scope->shared_from_this());
    }
}

/**
 * @brief Rebuild statement in one block.
 *
 * The statements are reconstructed by propagating the first node
 * where the result computed by this node is used in the following
 * instructions.
 * @param scope Scope which will receive the nodes.
 */
void Decompiler::PscDecompiler::rebuildExpression(Node::BasePtr scope)
{
    auto it = scope->begin();
    while (it != scope->end())
    {
        auto nextIt = std::next(it);
        auto expressionGeneration = *it;
        if (! expressionGeneration->isFinal() && nextIt != scope->end())
        {
            auto expressionUse = *nextIt;
            auto thing = expressionGeneration->getResult();
            // Check if an identifier in expressionUse references the result of expressionGeneration
            // If so, perform a replacement
            // At this steps of the decompilation, there should be only one replacement.
            auto modified = Node::WithNode<Node::Constant>()
                    .select([&] (Node::Constant* node) {
                        auto& value = node->getConstant();
                        return value.getType() == Pex::ValueType::Identifier && value.getId() == expressionGeneration->getResult();
                    })
                    .transform([&] (Node::Constant* node) {
                        (void)node;
                        return expressionGeneration;
                    })
                    .on(expressionUse);
            if (modified == 0)
            {
                std::advance(it, 1);
            }
            else if (modified == 1)
            {
                it = scope->begin();
            }
            else
            {
              auto funcname = m_Function.getName().isValid() ? m_Function.getName().asString() : "unknown function";
              throw std::runtime_error("Failed to rebuild expression in " + funcname + " at instruction " + std::to_string(expressionUse->getBegin()));
            }
        }
        else
        {
            std::advance(it, 1);
        }
    }
}

/**
 * @brief Rebuilds the boolean operations.
 *
 * This pass detects the patterns of the "or" and "and" operation generated by the
 * Papyrus compiler. The detection is performed from the startBlock until the endBlock is reached.
 * The endBlock is not processed.
 *
 * @param startBlock Indice of the first block to check
 * @param endBlock Indice of the block where to stop the detection.
 */
void Decompiler::PscDecompiler::rebuildBooleanOperators(size_t startBlock, size_t endBlock)
{
    bool debugSigil = false;
    if (m_Function.getName().isValid() && m_Function.getName().asString() == "OnTrackedStatsEvent"){
        debugSigil = true;
    }
    if (m_TraceDecompilation)
    {
        m_Log << "--- BEGIN REBUILD : " << startBlock << " " << endBlock << std::endl;
        dumpBlock(startBlock, endBlock);
    }
    auto begin = m_CodeBlocs.find(startBlock);
    auto end = m_CodeBlocs.find(endBlock);
    auto it = begin;
    while (it != end)
    {
        auto& source = it->second;
        int advance = 1;
        bool parentIsAssign = false;
        if (m_TraceDecompilation)
        {
            m_Log << "?" << source->getBegin() << " source->isConditional()=" << source->isConditional() <<" "
                << "source->getScope()->size()=" << source->getScope()->size() <<" "
                << '\n';
        }
        // Process only conditional block with at least one statement.
        if (source->isConditional() && source->getScope()->size() != 0)
        {
            if (m_TraceDecompilation)
            {
                m_Log << "??"             << "source->getCondition()=" << source->getCondition() << " "
                    << "source->getScope()->back()->getResult()=" << source->getScope()->back()->getResult() << " "
                    << '\n';
            }
            auto result = source->getScope()->back()->getResult();
            if (source->getScope()->back()->is<Node::Assign>()){
                auto destnode = source->getScope()->back()->as<Node::Assign>()->getDestination();
                if (destnode->is<Node::Constant>()){
                    result = destnode->as<Node::Constant>()->getConstant().getId();
                    parentIsAssign = true;
                    // if (result == source->getCondition()){
                    //   source->getScope()->back() = source->getScope()->back()->as<Node::Assign>()->getValue();
                    //
                    // }
                }

            }

            // Ensure that the last statement computes the value of the condition variable.
            if (source->getCondition() == result)
            {
                if (m_TraceDecompilation)
                {
                    // AND ?
                    m_Log << "AND? "
                        << "source->onTrue() == source->getEnd() + 1:" << (source->onTrue() == source->getEnd() + 1) << " "
                        << '\n';
                    m_Log << "OR? "
                        << "source->onFalse() == source->getEnd() + 1:" << (source->onFalse() == source->getEnd() + 1) << " "
                        << '\n';
                }
                // If the true block is the block directly following this one, it is a potential and
                bool maybeAnd = (source->onTrue() == source->getEnd() + 1);
                // If the false block is the block directly following this one, it is a potential or
                bool maybeOr = (source->onFalse() == source->getEnd() + 1);
                assert(!(maybeAnd && maybeOr));

                auto next = maybeAnd ? source->onTrue() : source->onFalse();
                auto jumpnext = maybeAnd ? source->onFalse() : source->onTrue();

              // check debug info


                if (!m_DebugInfo.getLineNumbers().empty() && m_CodeBlocs[next]->getEnd() != PscCodeBlock::END){
                  auto nextBlock = m_CodeBlocs[next];
                  auto jumpBlock = m_CodeBlocs[jumpnext];
                  auto srcNode = source->getScope()->back();
                  auto sourceLines = m_DebugInfo.getLineNumbersForIpRange(srcNode->getBegin(), srcNode->getEnd());
                  auto nextNode = nextBlock->getScope()->size() > 0 ? nextBlock->getScope()->front() : nextBlock->getScope()->shared_from_this();
                  auto nextLines = m_DebugInfo.getLineNumbersForIpRange(nextNode->getBegin(), nextNode->getEnd());
                  auto jumpLines = m_DebugInfo.getLineNumbersForIpRange(jumpBlock->getBegin(), jumpBlock->getEnd());

                  // If the last source line is the same as the first next line, it is a potential and/or
                  // otherwise, don't attempt to squeeze these together.
                  if (sourceLines.empty() || nextLines.empty()){
                    auto thing = 1;
                  }
                  else
                  {
                    if (*sourceLines.rbegin() != *nextLines.begin()){
                      if (*nextLines.begin() - *sourceLines.rbegin() == 1) {
                        // if the possible boolean is on the next line,
                        // check if the next statement is an assign; if so, then this is probably not a boolean
                        if (nextNode->is<Node::Assign>()){
                          maybeAnd = false;
                          maybeOr = false;
                        }
                      } else {
                        maybeAnd = false;
                        maybeOr = false;
                      }
                    }
                  }
                }


                if (maybeAnd)
                {
                    // Rebuild the boolean operators between the true and false block.
                    rebuildBooleanOperators(source->onTrue(), source->onFalse());
                    auto & onTrue  = m_CodeBlocs[source->onTrue()];
                    auto & onFalse = m_CodeBlocs[source->onFalse()];
                    if (onTrue->getScope()->size() == 1)
                    {
                        if (m_TraceDecompilation)
                        {
                            m_Log << "AND@" << source->getBegin() << " "
                                << "onTrue->getScope()->size() == 1:" << (onTrue->getScope()->size() == 1) << " "
                                << "onTrue->getScope()->back()->getResult() == source->getCondition():" << (onTrue->getScope()->back()->getResult() == source->getCondition()) << " "
                                << "\n";
                        }
                        // The true block computes the same value as the current block, and it is the condition variable
                        // This is a "and" operator
                        auto andResult = onTrue->getScope()->back()->getResult();
                        if (onTrue->getScope()->back()->is<Node::Assign>() && source->getScope()->back()->is<Node::Assign>()){
                            auto ontrueassign = onTrue->getScope()->back()->as<Node::Assign>();
                            auto destnode = ontrueassign->getDestination();
                            if (destnode->is<Node::Constant>()){
                                andResult = destnode->as<Node::Constant>()->getConstant().getId();
                                if (onTrue->getScope()->size() == 1 && andResult == source->getCondition()) {
                                    auto val = ontrueassign->getValue();
                                    onTrue->getScope()->removeChild(onTrue->getScope()->back());
                                    *(onTrue->getScope()) << val;
                                }
                            }
                        }

                        if(onTrue->getScope()->size() == 1 && andResult == source->getCondition())
                        {
                            // Create the binary "&&" operator.
                            auto left = source->getScope()->back();
                            auto leftval = left;
                            bool fixassign = false;
                            if (left->is<Node::Assign>()) {
                                auto destnode = left->as<Node::Assign>()->getValue();
                                leftval = destnode;
                                fixassign = true;
                            } else {
                                source->getScope()->removeChild(left);
                            }

                            auto right = onTrue->getScope()->front();
                            onTrue->getScope()->removeChild(right);

                            auto andOperator = std::make_shared<Node::BinaryOperator>(-1, 7, source->getCondition(), leftval, "&&", right);
                            if (fixassign) {
                                left->as<Node::Assign>()->setValue(andOperator);
                            } else {
                                *(source->getScope()) << andOperator;
                            }
                            // Remove the true block now that the expression is rebuild
                            m_CodeBlocs.erase(onTrue->getBegin());

                            // Merge the false block.
                            source->getScope()->mergeChildren(onFalse->getScope()->shared_from_this());
                            rebuildExpression(source->getScope()->shared_from_this());
                            if(onFalse->getEnd() != PscCodeBlock::END){
                                source->setEnd(onFalse->getEnd());
                                source->setCondition(onFalse->getCondition(), onFalse->onTrue(), onFalse->onFalse());
                                m_CodeBlocs.erase(onFalse->getBegin());
                                advance = 0;
                            } else {
                                // we've reached the end, no longer conditional
                                auto end = onFalse->getBegin();
                                source->setEnd(end);
                                source->setCondition(onFalse->getCondition(), end, end);
                                if (m_TraceDecompilation)
                                {
                                    m_Log << "OR? " << "detected" << std::endl;
                                    dumpBlock(source->getBegin(), source->getEnd()+1);
                                }
                            }

                            if (m_TraceDecompilation)
                            {
                                m_Log << "AND? " << "detected" << std::endl;
                                dumpBlock(source->getBegin(), source->getEnd()+1);
                            }
//                            andOperator->includeInstruction(right->getBegin());
//                            andOperator->includeInstruction(left->getEnd());
                        }
                    }
                    it = m_CodeBlocs.find(source->getBegin());

                }
                else if (maybeOr)
                {
                    // Rebuild the boolean operators between the false and true block.
                    rebuildBooleanOperators(source->onFalse(), source->onTrue());
                    auto & onTrue  = m_CodeBlocs[source->onTrue()];
                    auto & onFalse = m_CodeBlocs[source->onFalse()];
                        if (m_TraceDecompilation)
                        {
                            m_Log << "OR@"  << source->getBegin() << " "
                                << "onFalse->getScope()->size() == 1:" << (onFalse->getScope()->size() == 1) << " "
                                << "onFalse->getScope()->back()->getResult() == source->getCondition():" << (onFalse->getScope()->back()->getResult() == source->getCondition()) << " "
                                << "\n";
                        }
                    // The false block computes the same value as the current block, and it is the condition variable
                    // This is a "or operator
                    auto orResult = onFalse->getScope()->back()->getResult();
                    if (onFalse->getScope()->back()->is<Node::Assign>()){
                        auto destnode = onFalse->getScope()->back()->as<Node::Assign>()->getDestination();
                        if (destnode->is<Node::Constant>()){
                            orResult = destnode->as<Node::Constant>()->getConstant().getId();
                            if (onFalse->getScope()->size() == 1 && orResult == source->getCondition()) {
                                auto val = onFalse->getScope()->back()->as<Node::Assign>()->getValue();
                                onFalse->getScope()->removeChild(onFalse->getScope()->back());
                                *(onFalse->getScope()) << val;
                            }
                        }
                    }

                    if(onFalse->getScope()->size() == 1 && orResult == source->getCondition())
                    {
                        //Create the "||" operator
                        auto left = source->getScope()->back();
                        auto leftval = left;
                        bool fixassign = false;
                        if (left->is<Node::Assign>()) {
                            auto destnode = left->as<Node::Assign>()->getValue();
                            leftval = destnode;
                            fixassign = true;
                        } else {
                            source->getScope()->removeChild(left);
                        }

                        auto right = onFalse->getScope()->front();
                        onFalse->getScope()->removeChild(right);

                        auto orOperator = std::make_shared<Node::BinaryOperator>(-1, 8, source->getCondition(), leftval, "||", right);
                        if (fixassign) {
                            left->as<Node::Assign>()->setValue(orOperator);
                        } else {
                            *(source->getScope()) << orOperator;
                        }

                        //Remove the false block now that the expression is rebuild
                        m_CodeBlocs.erase(onFalse->getBegin());

                        //Merge the true block.
                        source->getScope()->mergeChildren(onTrue->getScope()->shared_from_this());
                        rebuildExpression(source->getScope()->shared_from_this());
                        if (onTrue->getEnd() != PscCodeBlock::END){
                            source->setEnd(onTrue->getEnd());
                            source->setCondition(onTrue->getCondition(), onTrue->onTrue(), onTrue->onFalse());
                            m_CodeBlocs.erase(onTrue->getBegin());
                            advance = 0;
                        } else {
                            // we've reached the end, no longer conditional
                            auto end = onTrue->getBegin();
                            source->setEnd(end);
                            source->setCondition(onTrue->getCondition(), end, end);
                            if (m_TraceDecompilation)
                            {
                                m_Log << "OR? " << "detected" << std::endl;
                                dumpBlock(source->getBegin(), source->getEnd()+1);
                            }
                        }
                        if (m_TraceDecompilation)
                        {
                            m_Log << "OR? " << "detected" << std::endl;
                            dumpBlock(source->getBegin(), source->getEnd()+1);
                        }

//                        orOperator->includeInstruction(right->getBegin());
//                        orOperator->includeInstruction(left->getEnd());
                    }
                    it = m_CodeBlocs.find(source->getBegin());
                    advance = 0;
                }
            }
        }
        std::advance(it, advance);
    }
    if (m_TraceDecompilation)
    {
        m_Log << "--- END REBUILD : " << startBlock << " " << endBlock << std::endl;
        dumpBlock(startBlock, endBlock);
    }
}

/**
 * @brief Rebuild the flow control statements
 *
 * This pass detects the pattern of the if and while statements. Once a pattern
 * has been detected, the nodes are recreated.
 *
 * @param startBlock Indice of the first block to check
 * @param endBlock Indice of the block where to stop the detection.
 * @return The statement tree representing the statements between the boundaries.
 */
Node::BasePtr Decompiler::PscDecompiler::rebuildControlFlow(size_t startBlock, size_t endBlock)
{
    if (endBlock < startBlock)
    {
      auto funcname = m_Function.getName().isValid() ? m_Function.getName().asString() : "unknown function";
      throw std::runtime_error("Failed to rebuild control flow for " + funcname + ".");
    }
    auto begin = m_CodeBlocs.find(startBlock);
    auto end = m_CodeBlocs.find(endBlock);
    auto it = begin;

    Node::BasePtr result = std::make_shared<Node::Scope>();
    while (it != end)
    {
        auto current = it->first;
        auto& source = it->second;
        int advance = 1;
        // Check conditional blocks.
        if (source->isConditional())
        {
            auto exit = source->onFalse();
            // Find the block before the false block.
            auto beforeExit = findBlockForInstruction(exit-1);
            if (beforeExit == PscCodeBlock::END)
            {
                // Decompilation failed
                auto funcname = m_Function.getName().isValid() ? m_Function.getName().asString() : "unknown function";
                throw std::runtime_error("Failed to rebuild control flow for " + funcname + ".");
            }
            //Node::BasePtr condition = std::make_shared<Node::Constant>(source->getEnd(), Pex::Value(source->getCondition(), true));
            Node::BasePtr condition = std::make_shared<Node::Constant>(-1, Pex::Value(source->getCondition(), true));

            if (m_CodeBlocs[beforeExit] == source) {
                assert(source->onFalse() < source->onTrue());
                auto scope = source->getScope();
                //condition = std::make_shared<Node::UnaryOperator>(source->getEnd(), 10, source->getCondition(), "!", condition);
                condition = std::make_shared<Node::UnaryOperator>(-1, 10, source->getCondition(), "!", condition);
                source->setCondition(source->getCondition(), source->onFalse(), source->onTrue());
                exit = source->onFalse();
                beforeExit = findBlockForInstruction(exit-1);
              }
              auto& lastBlock = m_CodeBlocs[beforeExit];

            // The last block is an unconditional jump to the current block
            // This is a while.
            if (! lastBlock->isConditional() && lastBlock->getNext() == current)
            {
                // while loop
                auto whileStartBlock = source->onTrue();
                auto whileEndBlock = source->onFalse();

                result->mergeChildren(source->getScope()->shared_from_this());

                // Rebuild the statements in the while loop.
                auto whileBody = rebuildControlFlow(whileStartBlock, whileEndBlock);

                *result << std::make_shared<Node::While>(-1, condition, whileBody);

                advance = 0;
                it = m_CodeBlocs.find(whileEndBlock);
            }
            else if (!lastBlock->isConditional())
            {
                // The last block exits to the false block
                // This is a simple if
                if (lastBlock->getNext() == exit)
                {
                    // Simple If
                    auto ifStartBlock = source->onTrue();
                    auto ifEndBlock = source->onFalse();

                    result->mergeChildren(source->getScope()->shared_from_this());

                    // Rebuild the statements of the if body
                    auto ifBody = rebuildControlFlow(ifStartBlock, ifEndBlock);

                    *result << std::make_shared<Node::IfElse>(-1, condition, ifBody, nullptr);

                    advance = 0;
                    it = m_CodeBlocs.find(ifEndBlock);
                }
                else // This is an if-else statement/
                {
                    auto ifStartBlock = source->onTrue();
                    auto elseStartBlock = source->onFalse();
                    auto endElseBlock = lastBlock->getNext();


                    result->mergeChildren(source->getScope()->shared_from_this());

                    // Rebuilds the statements in the if body.
                    auto ifBody = rebuildControlFlow(ifStartBlock, elseStartBlock);
                    // Rebuilds the statements in the else body.
                    auto elseBody = rebuildControlFlow(elseStartBlock, endElseBlock);

                    *result << std::make_shared<Node::IfElse>(-1, condition, ifBody, elseBody);

                    advance = 0;
                    it = m_CodeBlocs.find(endElseBlock);
                }

            }

        }
        else
        {
            //On unconditional jump, merge the current block statements to the result scope.
            result->mergeChildren(source->getScope()->shared_from_this());
        }
        std::advance(it, advance);
    }
    rebuildExpression(result);
    return result;
}

/**
 * @brief Finds the lowest common scope for a variable's references.
 * @param var Name of the variable.
 * @param scope Initial enclosing scope.
 * @return The lowest common scope.
 */
Node::BasePtr Decompiler::PscDecompiler::findScopeForVariable(const Pex::StringTable::Index &var, Node::BasePtr scope)
{
    // Default result is the initial scope.
    Node::BasePtr result = scope;

    // Find all references to the variable.
    auto references = Node::WithNode<Node::Constant>()
            .select([&] (Node::Constant* node) {
                auto& val = node->getConstant();
                return val.getType() == Pex::ValueType::Identifier && val.getId() == var;
            })
            .from(scope);

    // If there are some references, we perform the scope detection
    if (references.size() != 0)
    {
        // List of scope in the hierarchycal order.
        std::deque<Node::BasePtr> commonScopes;

        // Initialize the scope hierarchy list with the first reference.
        auto initial = references.front();
        references.pop_front();
        while(initial)
        {
            // Find the scope hierarchy for this node by goin up,
            // collecting scope as we go.
            if (initial->is<Node::Scope>())
            {
                commonScopes.push_front(initial);
            }
            initial = initial->getParent();
        }

        // For each remaining reference, we look for a common scope
        for (auto ref : references)
        {
            auto it = commonScopes.end();
            // Exit if the scope was found in the current hierarchy
            while (ref && it == commonScopes.end())
            {
                // Find the enclosing scope of the reference.
                while(ref && !ref->is<Node::Scope>())
                {
                    ref = ref->getParent();
                }

                // Search the scope in the current hierarchy
                it = std::find(commonScopes.begin(), commonScopes.end(), ref);
                ref = ref->getParent();
            }

            // At least the initial scope should be common to all reference
            assert(it != commonScopes.end());

            // If the found scope is not the last of the hierarchy, we delete from this scope to the end.
            if (std::next(it) != commonScopes.end())
            {
                commonScopes.erase(std::next(it), commonScopes.end());
            }
        }
        // At least the initial scope should be common to all reference
        assert(commonScopes.size() > 0);
        // The result scop is the last from the hierarchy.
        result = commonScopes.back();
    }

    return result;
}

/**
 * @brief Handle the variable declaration.
 *
 * This pass finds the lowest common scope for a variable and adds a it's declaration
 * either on top, or on the first assignement if possible.
 *
 * @param program The program tree.
 */
void Decompiler::PscDecompiler::declareVariables(Node::BasePtr program)
{
    // For each variable declared in the function
    for (auto& local : m_Function.getLocals())
    {
        // Avoid temporary variables
        if(!isTempVar(local.getName()))
        {
            // Find the scope common to all reference of the variable
            auto scope = findScopeForVariable(local.getName(), program);
            assert(scope);

            auto declare = std::make_shared<Node::Declare>(-1, std::make_shared<Node::Constant>(-1, Pex::Value(local.getName(), true)), local.getTypeName());

            // Find all assignment to the variable
            auto assignments = Node::WithNode<Node::Assign>()
                    .select([&] (Node::Assign* node) {
                        if(node->getDestination()->is<Node::Constant>())
                        {
                            auto& value = node->getDestination()->as<Node::Constant>()->getConstant();

                            return value.getType() == Pex::ValueType::Identifier && value.getId() == local.getName();
                        }
                        return  false;
                    })
                    .from(scope);
            // The first assignment is in the upper level scope
            if (assignments.size() > 0 && assignments.front()->getParent() == scope)
            {
                // Declare and assign at the same time
                auto assign = assignments.front()->as<Node::Assign>();
                assign->setDestination(declare);
            }
            else
            {
                // Declare at the top of the scope
                scope->push_front(declare);
            }
        }
    }
}



/**
 * @brief Clean the reconstructed tree.
 *
 * This pass perform a cleanup of the reconstructed tree to remove superfluous statement
 * and to rebuild higher level statement not directly inferred from the instruction flow.
 * This include the != operator, or the if-elseif-else program structure.
 *
 * @param program The root node of the program tree.
 */
void Decompiler::PscDecompiler::cleanUpTree(Node::BasePtr program)
{    
    program->computeInstructionBounds();


    // Remove the copy node, which was used to assign to temporary variables.;
    Node::WithNode<Node::Copy>()
        .transform([&] (Node::Copy* node) {
            auto val = node->getValue();
//            val->includeInstruction(node->getEnd());
            return val;
        })
        .on(program);

    // Remove casting a variable as it's own type as they are useless
    Node::WithNode<Node::Cast>()
        .select([&] (Node::Cast* node) {
            if (node->getValue()->is<Node::Constant>())
            {
                auto value = node->getValue()->as<Node::Constant>()->getConstant();
                if (value.getType() == Pex::ValueType::Identifier)
                {
                    return typeOfVar(value.getId()) == node->getType();
                }
            }
            return false;
        })
        .transform([&] (Node::Cast* node) {
            return node->getValue();
        })
        .on(program);

    // Remove casting none as Something as they are invalid
    Node::WithNode<Node::Cast>()
        .select([&] (Node::Cast* node) {
            if (node->getValue()->is<Node::Constant>())
            {
                auto value = node->getValue()->as<Node::Constant>()->getConstant();
                return value.getType() == Pex::ValueType::None;
            }
            return false;
        })
        .transform([&] (Node::Cast* node) {
            return node->getValue();
        })
        .on(program);


    // Replace the identifiers name index with a string value, unmangling names and property autovar
    Node::WithNode<Node::Constant>()
            .select([&] (Node::Constant* node) {
                return node->getConstant().getType() == Pex::ValueType::Identifier;
            })
            .transform([&] (Node::Constant* node) {
                return std::make_shared<Node::IdentifierString>(node->getBegin(), getVarName(node->getConstant().getId()));
            })
            .on(program);


    // Apply ! operator on == comparison
    Node::WithNode<Node::UnaryOperator>()
        .select([&] (Node::UnaryOperator* node) {
            if (node->getOperator() == "!" && node->getValue()->is<Node::BinaryOperator>())
            {
                auto op = node->getValue()->as<Node::BinaryOperator>();
                return op->getOperator() == "==";
            }
            return false;
        })
        .transform([&] (Node::UnaryOperator* node) {
            auto op = node->getValue()->as<Node::BinaryOperator>();
            auto result = std::make_shared<Node::BinaryOperator>(op->getBegin(), op->getPrecedence(), op->getResult(), op->getLeft(), "!=", op->getRight());
            result->includeInstruction(node->getEnd());
            return result;
        })
        .on(program);

    // Rebuild ElseIf structures
    Node::WithNode<Node::IfElse>()
        .select([&] (Node::IfElse* node) {
            auto elseNode = node->getElse();
            return elseNode->size() == 1 && elseNode->operator[](0)->is<Node::IfElse>();
        })
        .transform([&] (Node::IfElse* node) {
            auto childIfNode = node->getElse()->operator[](0);            

            node->setElse(childIfNode->as<Node::IfElse>()->getElse());
            childIfNode->as<Node::IfElse>()->setElse(std::make_shared<Node::Scope>());

            *node->getElseIf() << childIfNode;
            node->getElseIf()->mergeChildren(childIfNode->as<Node::IfElse>()->getElseIf());

            return node->shared_from_this();
        })
    .on(program);

    // Extract assign operator ( x = x + 1 => x += 1)
    Node::WithNode<Node::Assign>()
        .select([&] (Node::Assign* node) {
            auto result = false;
            auto destination = node->getDestination();
            if (node->getValue()->is<Node::BinaryOperator>())
            {
                auto binaryOp = node->getValue()->as<Node::BinaryOperator>();
                // ||= and &&= are not valid operators
                // a.b.c += 1 doesn't seems to compile.
                // so is array[x] += 1
                if (binaryOp->getOperator() != "||" && binaryOp->getOperator() != "&&"
                    && !node->getDestination()->is<Node::PropertyAccess>()
                    && !node->getDestination()->is<Node::ArrayAccess>()
                )
                {
                    auto left = binaryOp->getLeft();
                    return Node::isSameTree(destination, left);
                }
            }
            return result;
        })
        .transform([&] (Node::Assign* node) {
            auto binaryOp = node->getValue()->as<Node::BinaryOperator>();
            return std::make_shared<Node::AssignOperator>(node->getBegin(), node->getDestination(), binaryOp->getOperator() + "=", binaryOp->getRight());
        })
        .on(program);

    program->computeInstructionBounds();

    // check for orphaned nodes on m_CodeBlocs
    for (auto& bloc_kv : m_CodeBlocs)
    {
        auto& bloc = bloc_kv.second;
        auto scope = bloc->getScope();
        if (scope->size() > 0) {
          auto funcname = m_Function.getName().isValid() ? m_Function.getName().asString() : "unknown function";
          throw std::runtime_error("Orphaned nodes in " + funcname + " from instruction " + std::to_string(scope->front()->getBegin()) + " to " + std::to_string(scope->back()->getEnd()) + ".");
        }
    }

}





// Guard node body building
// This is a bit of a hack to avoid messing with the current codeblocks processing
// Instead of creating these bodies during `rebuildControlFlow`, we create them after the fact
// This is because we have to determine the scope of each of guard/tryGuard/endguard nodes and
// it's a lot easier if we know the existing scopes beforehand
// TODO: Verify and clean this up
void Decompiler::PscDecompiler::rebuildLocks(Node::BasePtr &program) {

    // Lift TryLocks
    // We are making the assumption (based on the limited `TryGuard`s present in the vanilla game)
    // that all TryLocks will always be the condition of an IfElse node.
    // All we do is replace the IfElse node with a TryGuard node
    // TODO: Verify that this is always what PCompiler produces
    Node::WithNode<Node::IfElse>()
            .select([&] (Node::IfElse* node) {
                // If the condition is a TryGuard
                return node->getCondition()->is<Node::TryGuard>();
            })
            .transform([&] (Node::IfElse* node) {
                //replace with tryguard
                auto tryguard = node->getCondition()->as<Node::TryGuard>();
                auto body = node->getBody();
                tryguard->setBody(body);
                RemoveUnlocksFromBody(body, tryguard->shared_from_this());
                return tryguard->shared_from_this();
            })
            .on(program);

    // create guard bodies
    auto lockNodes = Node::WithNode<Node::GuardStatement>()
            .select([&] (Node::GuardStatement* node) {
                return true;
            }).from(program);
    for (auto nodeptr: lockNodes){
        LiftLockBody(nodeptr);
    }

    // Find remaining endguard nodes
    auto unlockNodes = Node::WithNode<Node::EndGuard>()
            .select([&] (Node::EndGuard* node) {
                return true;
            }).from(program);
    // We should have removed all the remaining endguard nodes at this point
    assert(unlockNodes.size() == 0);
}

void Decompiler::PscDecompiler::LiftLockBody(std::shared_ptr<Node::Base> &guard) {
    // Find all the unlocks statements within the current scope
    auto node = guard->as<Node::GuardStatement>();
    auto parentScope = node->getParent();
    auto unlocks = Node::WithNode<Node::EndGuard>()
            .select([&] (Node::EndGuard* unode) {
                // check that the parameters for node and unode match
                return Node::isSameTree(node->getParameters(), unode->getParameters());
            })
            .from(parentScope);

    auto lockScope = node->getBody();

    // We are going to iterate along all the children on the parentScope node in order until we find the matching endguard
    auto it = parentScope->begin();

    // iterate on parentScope's children until we get to this guard node
    while (it != parentScope->end()) {
        if ((*it)->as<Node::GuardStatement>() == node){
            std::advance(it, 1);
            break;
        }
        std::advance(it, 1);
    }
    // If there's no more nodes after the `guard` node, we have a problem...
    assert(it != parentScope->end());

    bool foundMatchingUnlock = false;
    std::deque<Node::BasePtr> toLift;
    // Find the matching `endguard` node
    // The matching `endguard` node should be in the same scope as the `guard` node
    while (it != parentScope->end())
    {
        toLift.push_back(*it);
        // check if this is an endguard node in `unlocks`
        if (std::find(unlocks.begin(), unlocks.end(), *it) != unlocks.end()){
            if (unlocks.size() == 1){
                foundMatchingUnlock = true;
                break;
            }
            // check if the very next statement is a return node
            auto next = std::next(it);
            // The compiler will insert an endguard right before a return statement if that statement is within a guard body
            // in addition to the matching endguard statement at the end of the scope
            if (next != parentScope->end() && ((*next)->is<Node::Return>())){
                // check the next statement to see if it's the end of this scope; if so, this is the matching endguard
                if (std::next(next) == parentScope->end()){
                    foundMatchingUnlock = true;
                    break;
                }
            } else {
                foundMatchingUnlock = true;
                break;
            }
        }
        std::advance(it, 1);
    }
    assert(foundMatchingUnlock);
    // Lift the statements between the guard statements to the body
    for (auto& n : toLift){
        *lockScope << n;
    }

    // Remove the matching unlocks
    RemoveUnlocksFromBody(lockScope, node->shared_from_this());

    // Now that we've lifted the guard body and removed the extraneous `endguard` nodes, we have to rebuild the expressions
    // in case some `::temp` variables were still used in the guard body
    rebuildExpression(lockScope);
}

void Decompiler::PscDecompiler::RemoveUnlocksFromBody(Node::BasePtr &body, const Node::BasePtr &matchingLock) {
    // Remove matching endguard nodes
    assert(matchingLock->as<Node::GuardStatement>() || matchingLock->as<Node::TryGuard>());
    auto unlockNodes = Node::WithNode<Node::EndGuard>()
            .select([&] (Node::EndGuard* unode) {
                auto lockparams = matchingLock->as<Node::GuardStatement>() ?
                        matchingLock->as<Node::GuardStatement>()->getParameters() :
                        matchingLock->as<Node::TryGuard>()->getParameters();
                return Node::isSameTree(lockparams, unode->getParameters());
            }).from(body);
    for (auto nodeptr: unlockNodes){
        // remove the endguard node
        nodeptr->getParent()->removeChild(nodeptr);
    }
}

#include "DumpTree.hpp"

/**
 * @brief Generate the code from the program tree.
 *
 * @param program The tree to output as code.
 */
void Decompiler::PscDecompiler::generateCode(Node::BasePtr program)
{
    if (m_TraceDecompilation && m_DumpTree)
    {
        
        //DumpTree tree([&] (std::string&& line)
        DumpTree tree([&] (std::ostringstream stream)
        {
            push_back(stream.str());
            //push_back(line);
        });
        program->visit(&tree);
    }

    if (m_CommentAsm)
    {
        for (auto& local : m_Function.getLocals())
        {
            if(isTempVar(local.getName()))
            {
                std::ostringstream stream;
                stream << ";" << local.getTypeName() << " " << local.getName();
                push_back(stream.str());
            }
        }
        push_back("");
    }

    PscCodeGenerator codegen(this);
    program->visit(&codegen);
}

/**
 * @brief Extract the identifier from a value.
 * @param value The value containing the identifier.
 * @return The identifier.
 */
Pex::StringTable::Index Decompiler::PscDecompiler::toIdentifier(const Pex::Value &value) const
{
    assert(value.getType() == Pex::ValueType::Identifier);
    return value.getId();
}

/**
 * @brief Create a tree node from a value.
 * @param ip Indice of the instruction using the value.
 * @param value Value used as constant.
 * @return The constant node.
 */
Node::BasePtr Decompiler::PscDecompiler::fromValue(size_t ip, const Pex::Value &value) const
{
    return std::make_shared<Node::Constant>(ip, value);
}

/**
 * @brief Put an assign statement if needed by an expression
 * If the result of an expression is not assigned to a temporary variable, then an assign statement
 * must assign the result to the variable.
 * @param expression Expression to check
 * @return The node with an assign or the expression node.
 */
Node::BasePtr Decompiler::PscDecompiler::checkAssign(Node::BasePtr expression) const
{
    assert(expression);
    auto& result = expression->getResult();
    if (result.isValid() && !isTempVar(result))
    {
        return std::make_shared<Node::Assign>(expression->getBegin(), std::make_shared<Node::Constant>(expression->getBegin(), Pex::Value(result, true)), expression);
    }
    return expression;
}

void Decompiler::PscDecompiler::dumpBlock(size_t startBlock, size_t endBlock)
{
    auto begin = m_CodeBlocs.find(startBlock);
    auto end = m_CodeBlocs.find(endBlock);
    auto it = begin;
    while(it != end)
    {

        auto& b = it->second;

        m_Log << "-------" << it->first << ": " << b->getBegin() << " " << b->getEnd() << '\n';

        for (auto i = b->getBegin(); i <= b->getEnd() && i <m_Function.getInstructions().size(); ++i)
        {
            auto& ins = m_Function.getInstructions()[i];
            m_Log << std::dec << std::setw(3) << std::setfill('0') << i << ":" << ins.getOpCodeName();
            for (auto& a : ins.getArgs())
            {
                m_Log << " " << a.toString();
            }
            for (auto& a : ins.getVarArgs())
            {
                m_Log << " " <<a.toString();
            }
            m_Log << '\n';
        }
        if (m_DumpTree)
        {
            //DumpTree tree([&] (std::string&& line)
            
            DumpTree tree([&] (std::ostringstream line)
            {
                m_Log << line.str() << '\n';
                // m_Log << line << '\n';
            });
            b->getScope()->visit(&tree);
        }
        m_Log << "------- cond:" << b->getCondition() << " true:" << b->onTrue() << " false:" << b->onFalse() << std::endl;
        ++it;
    }
}

bool Decompiler::PscDecompiler::isDebugFunction() {
    // TODO: Actually walk the tree instead of doing dump string comparisons
    // We need to check if there are still ::temp variables in the tree.
    // If there are, then this indicates that this read from debug variables that
    // were not actually initialized because they were marked DebugOnly
    // and weren't properly poisoned by the Papyrus debugger.
    for (auto& line : *this) {
        int64_t i = line.find("::temp");
        int64_t comment = line.find(";");
        if (i != std::string::npos && (comment == std::string::npos || i < comment)) {
            return true;
        }
    }
    return false;
}

const Pex::DebugInfo::FunctionInfo & Decompiler::PscDecompiler::getDebugInfo() {
    return m_DebugInfo;
}

void Decompiler::PscDecompiler::addLineMapping(size_t decompiledLine, std::vector<uint16_t> &originalLines) {
    m_LineMap[decompiledLine] = std::move(originalLines);
}

Decompiler::PscDecompiler::DebugLineMap &Decompiler::PscDecompiler::getLineMap() {
  return m_LineMap;
}
```

## File: `Decompiler/PscDecompiler.hpp`
```
#pragma once

#include <vector>
#include <string>
#include <fstream>

#include <map>

#include "Pex/Object.hpp"
#include "PscCodeBlock.hpp"

#include "Node/Base.hpp"
#include "Pex/DebugInfo.hpp"

namespace Decompiler {

/**
 * @brief Decompiler class.
 *
 * This class contains the core process of the decompilation sequence.
 * The result is stored as string in the vector part of the class.
 */
class PscDecompiler :
        public std::vector<std::string>
{
public:
    typedef std::map<size_t, std::vector<uint16_t>> DebugLineMap;

    PscDecompiler(const Pex::Function &function, const Pex::Object &object,
                  const Pex::DebugInfo::FunctionInfo *debugInfo, bool commentAsm, bool traceDecompilation,
                  bool dumpTree, std::string outputDir);
    ~PscDecompiler();

    void decodeToAsm(std::uint8_t level, size_t begin, size_t end);
    bool isDebugFunction();
    const Pex::DebugInfo::FunctionInfo & getDebugInfo();
    void addLineMapping(size_t decompiledLine, std::vector<uint16_t> &originalLines);
    DebugLineMap &getLineMap();
protected:


    void findVarTypes();
    const Pex::StringTable::Index& typeOfVar(const Pex::StringTable::Index& var) const;
    void createFlowBlocks();

    void createNodesForBlocks(size_t bloc);
    size_t findBlockForInstruction(size_t ip);


    void rebuildExpressionsInBlocks();
    void rebuildExpression(Node::BasePtr scope);

    void rebuildBooleanOperators(size_t startBlock, size_t endBlock);
    Node::BasePtr rebuildControlFlow(size_t startBlock, size_t endBlock);

    Node::BasePtr findScopeForVariable(const Pex::StringTable::Index& var, Node::BasePtr enclosingScope);

    void declareVariables(Node::BasePtr program);
    void cleanUpTree(Node::BasePtr program);

    void generateCode(Node::BasePtr program);
    Pex::StringTable::Index toIdentifier(const Pex::Value& value) const;
    Node::BasePtr fromValue(size_t ip, const Pex::Value& value) const;
    Node::BasePtr checkAssign(Node::BasePtr expression) const;

    void dumpBlock(size_t startBlock, size_t endBlock);
protected:
    typedef std::map<size_t, PscCodeBlock*> CodeBlocs;
    CodeBlocs m_CodeBlocs;

    typedef std::map<std::uint16_t, Pex::StringTable::Index> VarToProperties;
    VarToProperties m_VarToProperties;

    typedef std::map<std::uint16_t, Pex::StringTable::Index> VarTypes;
    VarTypes m_VarTypes;

    Pex::StringTable::Index m_NoneVar;

    const Pex::Function& m_Function;
    const Pex::Object&   m_Object;
    bool m_ReturnNone;

    bool m_CommentAsm;
    bool m_TraceDecompilation;
    bool m_DumpTree;
    const Pex::DebugInfo::FunctionInfo m_DebugInfo;
    std::string m_OutputDir;
    std::ofstream m_Log;
    Pex::StringTable m_TempTable;

    // Map of decompiled lines to the range of (potentially multiple) original lines that were in the debug info
    DebugLineMap m_LineMap;

    void rebuildLocks(Node::BasePtr &program);
    void RemoveUnlocksFromBody(Node::BasePtr &body, const Node::BasePtr &matchingLock);
    void LiftLockBody(std::shared_ptr<Node::Base> &guard);

};
}
```

## File: `Decompiler/StreamWriter.hpp`
```
#pragma once

#include <iostream>

#include "OutputWriter.hpp"

namespace Decompiler {

class StreamWriter : public OutputWriter
{
public:
    StreamWriter(std::ostream& stream) : m_Stream(stream) { }
    virtual ~StreamWriter() = default;

    virtual void writeLine(const std::string& line)
    {
        m_Stream << line << '\n';
    }

protected:
    std::ostream& m_Stream;
};

}
```

## File: `Decompiler/Version.hpp`
```
#pragma once

#define CHAMPOLLION_VERSION_MAJOR 1
#define CHAMPOLLION_VERSION_MINOR 3
#define CHAMPOLLION_VERSION_PATCH 2

#define MAKE_STR_HELPER(a_str) #a_str
#define MAKE_STR(a_str) MAKE_STR_HELPER(a_str)

#define CHAMPOLLION_VERSION_STRING "v" MAKE_STR(CHAMPOLLION_VERSION_MAJOR) "." MAKE_STR(CHAMPOLLION_VERSION_MINOR) "." MAKE_STR(CHAMPOLLION_VERSION_PATCH)
```

## File: `Decompiler/Node/ArrayAccess.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class ArrayAccess final :
    public Base,
    public FieldArrayNodeMixin<0>,
    public FieldIndexNodeMixin<1>
{
public:
    ArrayAccess(size_t ip, const Pex::StringTable::Index& result, BasePtr object, BasePtr index) :
        Base(2, ip, 0, result),
        FieldArrayNodeMixin(this, object),
        FieldIndexNodeMixin(this, index)
    {
    }
    virtual ~ArrayAccess() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }
};

}
```

## File: `Decompiler/Node/ArrayCreate.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class ArrayCreate final :
    public Base,
    public FieldIndexNodeMixin<0>
{
public:
    ArrayCreate(size_t ip, const Pex::StringTable::Index& result, const Pex::StringTable::Index& type, BasePtr size) :
        Base(1, ip, 0, result),
        m_Type(type),
        FieldIndexNodeMixin(this, size)
    {
    }
    virtual ~ArrayCreate() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    const Pex::StringTable::Index& getType() const { return m_Type; }

private:
    const Pex::StringTable::Index& m_Type;
};

}
```

## File: `Decompiler/Node/ArrayLength.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>
#include <string>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class ArrayLength final :
    public Base,
    public FieldArrayNodeMixin<0>
{
public:
    ArrayLength(size_t ip, const Pex::StringTable::Index& result, BasePtr object) :
        Base(1, ip, 0, result),
        FieldArrayNodeMixin(this, object)
    {
    }
    virtual ~ArrayLength() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }
};

}
```

## File: `Decompiler/Node/Assign.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class Assign final :
    public Base,
    public FieldValueNodeMixin<0>,
    public FieldDestinationNodeMixin<1>
{
public:
    Assign(size_t ip, BasePtr destination, BasePtr value) :
        Base(2, ip, 10),
        FieldValueNodeMixin(this, value),
        FieldDestinationNodeMixin(this, destination)
    {
    }
    virtual ~Assign() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }
};

}
```

## File: `Decompiler/Node/AssignOperator.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>
#include <string>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class AssignOperator final :
    public Base,
    public FieldValueNodeMixin<0>,
    public FieldDestinationNodeMixin<1>
{
public:
    AssignOperator(size_t ip, BasePtr destination, const std::string& op, BasePtr expr) :
        Base(2, ip, 10),
        FieldValueNodeMixin(this, expr),
        FieldDestinationNodeMixin(this, destination),
        m_Operator(op)
    {
    }
    virtual ~AssignOperator() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    const std::string& getOperator() const { return m_Operator; }

private:
    std::string m_Operator;
};

}
```

## File: `Decompiler/Node/Base.cpp`
```cpp
#include "Base.hpp"
#include <Champollion/CaselessCompare.h>

#include <algorithm>
#include <cassert>

Node::Base::Base(size_t childs, size_t ip, uint8_t precedence, const Pex::StringTable::Index &result) :
    std::deque<BasePtr>(childs),
    m_Begin(ip),
    m_End(ip),
    m_FixedSize(childs != 0),
    m_Precedence(precedence),
    m_Result(result)
{
}

Node::Base::~Base()
{
    for (auto child : *this)
    {
        if (child)
            child->m_Parent = nullptr;
    }
}

bool Node::Base::isFinal() const
{
    if (m_Result.isValid() && !m_Result.isUndefined())
    {
        auto& id = m_Result.asString();
        return id.substr(0, 6) != "::temp" && caselessCompare(id.c_str(), "::nonevar") != 0;
    }
    return true;

}

Node::Base &Node::Base::operator <<(Node::BasePtr child)
{
    assert(!m_FixedSize);

    if (child->getParent())
        child->getParent()->removeChild(child);

    push_back(child);
    child->m_Parent = this;
    return *this;
}

void Node::Base::setChild(size_t c, Node::BasePtr child)
{
    assert(c < size());

    if (child)
    {
        if (child->getParent())
            child->getParent()->removeChild(child);

        if (operator[](c))
            operator[](c)->m_Parent = nullptr;

        operator[](c) = child;
        child->m_Parent = this;
    }
    else
    {
        operator[](c) = child;
    }
}

void Node::Base::mergeChildren(Node::BasePtr source)
{
    for (auto child : *source)
    {
        push_back(child);
        child->m_Parent = this;
    }
    source->clear();
}

Node::BasePtr Node::Base::getParent() const
{
    if (m_Parent)
        return m_Parent->shared_from_this();
    else
        return nullptr;
}

void Node::Base::removeChild(Node::BasePtr child)
{
    auto it = std::find(begin(), end(), child);
    if (it != end())
    {
        (*it)->m_Parent = nullptr;

        if (m_FixedSize)
            *it = nullptr;
        else
            erase(it);
    }
}

void Node::Base::replaceChild(Node::BasePtr child, Node::BasePtr newChild)
{
    assert(child->m_Parent == this && child != newChild);

    if (newChild->m_Parent)
        newChild->m_Parent->removeChild(newChild);

    auto childPosition = std::find(begin(), end(), child);

    child->m_Parent = nullptr;
    newChild->m_Parent = this;
    *childPosition = newChild;
}

void Node::Base::computeInstructionBounds()
{
    for (auto child : *this)
    {
        if (child)
        {
            child->computeInstructionBounds();

            if (m_Begin == -1)
                m_Begin = child->getBegin();
            else if (child->getBegin() != -1)
                m_Begin = std::min(m_Begin, child->getBegin());

            if (m_End == -1)
                m_End = child->getEnd();
            else if (child->getEnd() != -1)
                m_End = std::max(m_End, child->getEnd());
        }
    }
}

void Node::Base::includeInstruction(size_t ip)
{
    if (m_Begin == -1)
        m_End = m_Begin = ip;
    else if (ip < m_Begin)
        m_Begin = ip;
    else if (ip > m_End)
        m_End = ip;
}
```

## File: `Decompiler/Node/Base.hpp`
```
#pragma once

#include <cstdint>
#include <deque>
#include <memory>

#include "Pex/Value.hpp"

namespace Node {

class Visitor;

class Base;
typedef std::shared_ptr<Base> BasePtr;

class Base :
    public std::deque<BasePtr>,
    public std::enable_shared_from_this<Base>
{
public:
    Base(size_t childs, size_t ip, uint8_t precedence, const Pex::StringTable::Index& result = Pex::StringTable::Index());
    virtual ~Base();

    template<typename T>
    bool is() const
    {
        return dynamic_cast<const T*>(this) != nullptr;
    }

    template<typename T>
    T* as()
    {
        return dynamic_cast<T*>(this);
    }

    size_t getBegin() const { return m_Begin; }
    size_t getEnd() const { return m_End; }
    uint8_t getPrecedence() const { return m_Precedence; }
    const Pex::StringTable::Index& getResult() const { return m_Result; }
    void clearResult() { m_Result = Pex::StringTable::Index(); }

    bool isFinal() const;

    virtual void visit(Visitor* visitor) = 0;

    Base& operator << (BasePtr child);
    void setChild(size_t c, BasePtr child);
    void mergeChildren(BasePtr source);

    BasePtr getParent() const;
    void removeChild(BasePtr child);
    void replaceChild(BasePtr child, BasePtr newChild);

    virtual void computeInstructionBounds();
    void includeInstruction(size_t ip);

protected:
    size_t m_Begin;
    size_t m_End;
    bool m_FixedSize;
    uint8_t m_Precedence;
    Pex::StringTable::Index m_Result;
    Base* m_Parent{ nullptr };
};

}
```

## File: `Decompiler/Node/BinaryOperator.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>
#include <string>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class BinaryOperator final :
    public Base,
    public FieldLeftNodeMixin<0>,
    public FieldRightNodeMixin<1>
{
public:
    BinaryOperator(size_t ip, std::uint8_t precedence, const Pex::StringTable::Index& result, BasePtr left, const std::string& op, BasePtr right) :
        Base(2, ip, precedence, result),
        FieldLeftNodeMixin(this, left),
        FieldRightNodeMixin(this, right),
        m_Op(op)
    {
    }
    virtual ~BinaryOperator() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    const std::string& getOperator() const { return m_Op; }

private:
    std::string m_Op;
};

}
```

## File: `Decompiler/Node/CallMethod.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>
#include <memory>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Params.hpp"
#include "Visitor.hpp"

namespace Node {
class CallMethod final :
    public Base,
    public FieldObjectNodeMixin<0>,
    public FieldParametersNodeMixin<1>
{
public:
    CallMethod(size_t ip, const Pex::StringTable::Index& result, BasePtr object, const Pex::StringTable::Index& method, const bool experimental = false) :
        Base(2, ip, 0, result),
        FieldObjectNodeMixin(this, object),
        FieldParametersNodeMixin(this, std::make_shared<Params>()),
        m_Method(method),
        m_Experimental(experimental)
    {
    }
    virtual ~CallMethod() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    bool isExperimentalSyntax(){
        return m_Experimental;
    }

    const Pex::StringTable::Index& getMethod() const { return m_Method; }

private:
    Pex::StringTable::Index m_Method;
    bool m_Experimental;
};

}
```

## File: `Decompiler/Node/Cast.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class Cast final :
    public Base,
    public FieldValueNodeMixin<0>
{
public:
    Cast(size_t ip, const Pex::StringTable::Index& result, BasePtr value, const Pex::StringTable::Index& type) :
        Base(1, ip, 1, result),
        FieldValueNodeMixin(this, value),
        m_Type(type)
    {
    }
    virtual ~Cast() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    const Pex::StringTable::Index& getType() { return m_Type; }

private:
    Pex::StringTable::Index m_Type;
};

}
```

## File: `Decompiler/Node/Constant.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "Visitor.hpp"
#include "Pex/Value.hpp"

namespace Node {

class Constant final : public Base
{
public:
    Constant(size_t ip, const Pex::Value& constant) :
        Base(0, ip, 0),
        m_Constant(constant)
    {
    }
    virtual ~Constant() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    const Pex::Value& getConstant() const { return m_Constant; }

private:
    Pex::Value m_Constant;
};

}
```

## File: `Decompiler/Node/Copy.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class Copy final :
    public Base,
    public FieldValueNodeMixin<0>
{
public:
    Copy(size_t ip, const Pex::StringTable::Index& result, BasePtr value) :
        Base(1, ip, 10, result),
        FieldValueNodeMixin(this, value)
    {
    }
    virtual ~Copy() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }
};

}
```

## File: `Decompiler/Node/Declare.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class Declare final :
    public Base,
    public FieldObjectNodeMixin<0>
{
public:
    Declare(size_t ip, BasePtr identifier, const Pex::StringTable::Index& type) :
        Base(1, ip, 0),
        FieldObjectNodeMixin(this, identifier),
        m_Type(type)
    {
    }
    virtual ~Declare() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    const Pex::StringTable::Index& getType() const { return m_Type; }

private:
    Pex::StringTable::Index m_Type;
};

}
```

## File: `Decompiler/Node/EndGuard.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>
#include <memory>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Scope.hpp"
#include "Visitor.hpp"

namespace Node {

    class EndGuard final :
            public Base,
            public FieldParametersNodeMixin<0>
    {
    public:
        EndGuard(size_t ip) :
                Base(1, ip, 10),
                FieldParametersNodeMixin(this, std::make_shared<Params>())
        {
        }
        virtual ~EndGuard() = default;

        void visit(Visitor* visitor) override
        {
            assert(visitor);
            visitor->visit(this);
        }

        void computeInstructionBounds() override
        {
            Base::computeInstructionBounds();
        }
    };

}
```

## File: `Decompiler/Node/FieldNodeMixin.hpp`
```
#ifndef FIELDNODEMIXIN_HPP
#define FIELDNODEMIXIN_HPP

#include <cstdint>
#include <cassert>

#include "Base.hpp"

namespace Node {

#define DECLARE_FIELD(NAME)                         \
template<size_t N>                                  \
class Field##NAME##NodeMixin                        \
{                                                   \
   protected:                                       \
    Base* m_This;                                   \
    Field##NAME##NodeMixin (Base* _this, BasePtr init) : \
        m_This(_this)                               \
    {                                               \
        set##NAME(init);                            \
    };                                              \
   public:                                          \
    BasePtr get##NAME() const                       \
    {                                               \
        assert(N < m_This->size());                 \
        return m_This->operator [](N);              \
    }                                               \
    void    set##NAME(BasePtr value)                \
    {                                               \
        assert(N < m_This->size());                 \
        m_This->setChild(N, value);                 \
    }                                               \
};                                                  \


DECLARE_FIELD(Value)
DECLARE_FIELD(Parameters)
DECLARE_FIELD(Object)
DECLARE_FIELD(Left)
DECLARE_FIELD(Right)
DECLARE_FIELD(Array)
DECLARE_FIELD(Index)
DECLARE_FIELD(Condition)
DECLARE_FIELD(Body)
DECLARE_FIELD(Else)
DECLARE_FIELD(ElseIf)
DECLARE_FIELD(Destination)

}
#endif // FIELDNODEMIXIN_HPP
```

## File: `Decompiler/Node/GuardStatement.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>
#include <memory>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Scope.hpp"
#include "Visitor.hpp"

namespace Node {

    class GuardStatement final :
            public Base,
            public FieldParametersNodeMixin<0>,
            public FieldBodyNodeMixin<1>
    {
    public:
        GuardStatement(size_t ip, BasePtr body) :
                Base(2, ip, 10),
                FieldParametersNodeMixin(this, std::make_shared<Params>()),
                FieldBodyNodeMixin(this, body)
        {
        }
        virtual ~GuardStatement() = default;

        void visit(Visitor* visitor) override
        {
            assert(visitor);
            visitor->visit(this);
        }

        void computeInstructionBounds() override
        {
            Base::computeInstructionBounds();
        }
    };

}
```

## File: `Decompiler/Node/IdentifierString.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>
#include <algorithm>
#include <string>

#include "Base.hpp"
#include "Visitor.hpp"

namespace Node {

class IdentifierString final : public Base
{
public:
    IdentifierString(size_t ip, const std::string& identifier) :
        Base(0, ip, 0),
        m_Identifier(identifier)
    {
      std::replace(m_Identifier.begin(), m_Identifier.end(), '#', ':');
    }
    virtual ~IdentifierString() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    const std::string& getIdentifier() const { return m_Identifier; }

private:
    std::string m_Identifier;
};

}
```

## File: `Decompiler/Node/IfElse.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>
#include <memory>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Scope.hpp"
#include "Visitor.hpp"

namespace Node {

class IfElse final :
    public Base,
    public FieldConditionNodeMixin<0>,
    public FieldBodyNodeMixin<1>,
    public FieldElseNodeMixin<2>,
    public FieldElseIfNodeMixin<3>
{
public:
    IfElse(size_t ip, BasePtr condition, BasePtr body, BasePtr elseBody) :
        Base(4, ip, 10),
        FieldConditionNodeMixin(this, condition),
        FieldBodyNodeMixin(this, body),
        FieldElseNodeMixin(this, elseBody ? elseBody : std::make_shared<Scope>()),
        FieldElseIfNodeMixin(this, std::make_shared<Scope>())
    {
    }
    virtual ~IfElse() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    void computeInstructionBounds() override
    {
        Base::computeInstructionBounds();
        if (getCondition()->getBegin() == -1)
        {
            m_Begin = getBody()->getBegin() - 1;
            m_End = m_Begin;
        }
        else
        {
            m_Begin = getCondition()->getBegin();
            m_End = getCondition()->getEnd() + 1;
        }
    }
};

}
```

## File: `Decompiler/Node/NodeComparer.cpp`
```cpp
#include "NodeComparer.hpp"

#include <cassert>

static bool isSameChildren(Node::Base* ref, Node::Base* node)
{
    if (ref->size() == node->size())
    {
        for (auto i = 0; i < ref->size(); ++i)
        {
            if (ref->operator[](i) != node->operator [](i) && !isSameTree(ref->operator[](i), node->operator [](i)))
            {
                return false;
            }
        }
        return true;
    }
    return false;
}

void Node::NodeComparer::visit(Node::Scope *node)
{
    m_Visitor << (DynamicVisitor::LambdaScope)[&](Scope* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::BinaryOperator *node)
{
    m_Visitor << (DynamicVisitor::LambdaBinaryOperator)[&](BinaryOperator* ref, DynamicVisitor*) {
        if (ref->getOperator() == node->getOperator())
        {
            m_Result = isSameChildren(ref, node);
        }
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::UnaryOperator *node)
{
    m_Visitor << (DynamicVisitor::LambdaUnaryOperator)[&](UnaryOperator* ref, DynamicVisitor*) {
        if(ref->getOperator() == node->getOperator())
        {
            m_Result = isSameChildren(ref, node);
        }
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::Assign *node)
{
    m_Visitor << (DynamicVisitor::LambdaAssign)[&](Assign* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::AssignOperator *node)
{
    m_Visitor << (DynamicVisitor::LambdaAssignOperator) [&](AssignOperator* ref, DynamicVisitor*) {
        if(ref->getOperator() == node->getOperator())
        {
            m_Result = isSameChildren(ref, node);
        }
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::Copy *node)
{
    m_Visitor << (DynamicVisitor::LambdaCopy)[&](Copy* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::Cast *node)
{
    m_Visitor << (DynamicVisitor::LambdaCast)[&](Cast* ref, DynamicVisitor*) {
        if(ref->getType() == node->getType())
        {
            m_Result = isSameChildren(ref, node);
        }
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::CallMethod *node)
{
    m_Visitor << (DynamicVisitor::LambdaCallMethod)[&](CallMethod* ref, DynamicVisitor*) {
        if (ref->getMethod() == node->getMethod())
        {
            m_Result = isSameChildren(ref, node);
        }
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::Params *node)
{
    m_Visitor << (DynamicVisitor::LambdaParams)[&](Params* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::Return *node)
{
    m_Visitor << (DynamicVisitor::LambdaReturn)[&](Return* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::PropertyAccess *node)
{
    m_Visitor << (DynamicVisitor::LambdaPropertyAccess)[&](PropertyAccess* ref, DynamicVisitor*) {
        if(ref->getProperty() == node->getProperty())
        {
            m_Result = isSameChildren(ref, node);
        }
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::StructCreate *node)
{
    m_Visitor << (DynamicVisitor::LambdaArrayCreate)[&](ArrayCreate* ref, DynamicVisitor*) {
        m_Result = ref->getType() == node->getType();
    };
    m_Reference->visit(&m_Visitor);
}

void Node::NodeComparer::visit(Node::ArrayCreate *node)
{
    m_Visitor << (DynamicVisitor::LambdaArrayCreate)[&](ArrayCreate* ref, DynamicVisitor*) {
        if (ref->getType() == node->getType())
        {
            m_Result = isSameChildren(ref, node);
        }
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::ArrayLength *node)
{
    m_Visitor << (DynamicVisitor::LambdaArrayLength)[&](ArrayLength* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::ArrayAccess *node)
{
    m_Visitor << (DynamicVisitor::LambdaArrayAccess)[&](ArrayAccess* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::Constant *node)
{
    m_Visitor << (DynamicVisitor::LambdaConstant)[&](Constant* ref, DynamicVisitor*) {
        m_Result = ref->getConstant() == node->getConstant();
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::IdentifierString *node)
{
    m_Visitor << (DynamicVisitor::LambdaIdentifierString)[&](IdentifierString* ref, DynamicVisitor*) {
        m_Result = ref->getIdentifier() == node->getIdentifier();
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::While *node)
{
    m_Visitor << (DynamicVisitor::LambdaWhile)[&](While* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}
void Node::NodeComparer::visit(Node::IfElse *node)
{
    m_Visitor << (DynamicVisitor::LambdaIfElse)[&](IfElse* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::Declare *node)
{
    m_Visitor << (DynamicVisitor::LambdaDeclare)[&](Declare* ref, DynamicVisitor*) {
        m_Result = ref->getType() == node->getType() && isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::GuardStatement *node)
{
    m_Visitor << (DynamicVisitor::LambdaGuardStatement)[&](GuardStatement* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::TryGuard *node)
{
    m_Visitor << (DynamicVisitor::LambdaTryGuard)[&](TryGuard* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

void Node::NodeComparer::visit(Node::EndGuard *node)
{
    m_Visitor << (DynamicVisitor::LambdaEndGuard)[&](EndGuard* ref, DynamicVisitor*) {
        m_Result = isSameChildren(ref, node);
    };
    m_Reference->visit(& m_Visitor);
}

bool Node::isSameTree(Node::BasePtr left, Node::BasePtr right)
{
    NodeComparer comparer(left);
    right->visit(&comparer);
    return comparer.getResult();
}
```

## File: `Decompiler/Node/NodeComparer.hpp`
```
#pragma once

#include "Base.hpp"
#include "Nodes.hpp"
#include "Visitor.hpp"

namespace Node {

class NodeComparer final : public Visitor
{
public:
    NodeComparer(BasePtr reference) :
        m_Reference(reference),
        m_Result(false)
    {
        m_Visitor.common([&](Base*, DynamicVisitor*) {});
    }
    virtual ~NodeComparer() = default;

    bool getResult() const { return m_Result; }

    void visit(Node::Scope* node) override;
    void visit(Node::BinaryOperator* node) override;
    void visit(Node::UnaryOperator* node) override;
    void visit(Node::Assign* node) override;
    void visit(Node::AssignOperator* node) override;
    void visit(Node::Copy* node) override;
    void visit(Node::Cast* node) override;
    void visit(Node::CallMethod* node) override;
    void visit(Node::Params* node) override;
    void visit(Node::Return* node) override;
    void visit(Node::PropertyAccess* node) override;
    void visit(Node::StructCreate* node) override;
    void visit(Node::ArrayCreate* node) override;
    void visit(Node::ArrayLength* node) override;
    void visit(Node::ArrayAccess* node) override;
    void visit(Node::Constant* node) override;
    void visit(Node::IdentifierString* node) override;
    void visit(Node::While* node) override;
    void visit(Node::IfElse* node) override;
    void visit(Node::Declare* node) override;
    void visit(Node::GuardStatement *node) override;
    void visit(Node::TryGuard *node) override;

private:
    BasePtr m_Reference;
    DynamicVisitor m_Visitor;
    bool m_Result;

    void visit(EndGuard *node) override;
};

bool isSameTree(BasePtr left, BasePtr right);

}
```

## File: `Decompiler/Node/Nodes.hpp`
```
#ifndef NODES_HPP
#define NODES_HPP

#include "Scope.hpp"
#include "BinaryOperator.hpp"
#include "UnaryOperator.hpp"
#include "Assign.hpp"
#include "AssignOperator.hpp"
#include "Copy.hpp"
#include "Cast.hpp"

#include "CallMethod.hpp"
#include "Params.hpp"

#include "Return.hpp"

#include "PropertyAccess.hpp"

#include "ArrayCreate.hpp"
#include "ArrayLength.hpp"
#include "ArrayAccess.hpp"

#include "StructCreate.hpp"

#include "Constant.hpp"
#include "IdentifierString.hpp"


#include "While.hpp"
#include "IfElse.hpp"

#include "Declare.hpp"

#include "GuardStatement.hpp"
#include "TryGuard.hpp"
#include "EndGuard.hpp"


#endif // NODES_HPP
```

## File: `Decompiler/Node/Params.hpp`
```
#pragma once

#include <cassert>

#include "Base.hpp"
#include "Visitor.hpp"

namespace Node {

class Params final : public Base
{
public:
    Params() : Base(0, -1, 10) { }
    virtual ~Params() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }
};

}
```

## File: `Decompiler/Node/PropertyAccess.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class PropertyAccess final :
    public Base,
    public FieldObjectNodeMixin<0>
{
public:
    PropertyAccess(size_t ip, const Pex::StringTable::Index& result, BasePtr object, const Pex::StringTable::Index& property) :
        Base(1, ip, 0, result),
        FieldObjectNodeMixin(this, object),
        m_Property(property)
    {
    }
    virtual ~PropertyAccess() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    const Pex::StringTable::Index& getProperty() const { return m_Property; }

private:
    Pex::StringTable::Index m_Property;
};

}
```

## File: `Decompiler/Node/Return.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class Return final :
    public Base,
    public FieldValueNodeMixin<0>
{
public:
    Return(size_t ip, BasePtr expr) :
        Base(1, ip, 10),
        FieldValueNodeMixin(this, expr)
    {
    }
    virtual ~Return() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }
};

}
```

## File: `Decompiler/Node/Scope.hpp`
```
#pragma once

#include <cassert>

#include "Base.hpp"
#include "Visitor.hpp"

namespace Node {

class Scope final : public Base
{
public:
    Scope() : Base(0, -1, 10) { }
    virtual ~Scope() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }
};

}
```

## File: `Decompiler/Node/StructCreate.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "Visitor.hpp"

namespace Node {

class StructCreate final : public Base
{
public:
    StructCreate(size_t ip, const Pex::StringTable::Index& result, const Pex::StringTable::Index& type) :
        Base(0, ip, 0, result),
        m_Type(type)
    {
    }
    virtual ~StructCreate() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    const Pex::StringTable::Index& getType() const { return m_Type; }

private:
    const Pex::StringTable::Index& m_Type;
};

}
```

## File: `Decompiler/Node/TryGuard.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>
#include <memory>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Scope.hpp"
#include "Visitor.hpp"

namespace Node {

    class TryGuard final :
            public Base,
            public FieldParametersNodeMixin<0>,
            public FieldBodyNodeMixin<1>
    {
    public:
        TryGuard(size_t ip, const Pex::StringTable::Index& result, BasePtr body) :
                Base(2, ip, 10, result),
                FieldParametersNodeMixin(this, std::make_shared<Params>()),
                FieldBodyNodeMixin(this, body)
        {
        }
        virtual ~TryGuard() = default;

        void visit(Visitor* visitor) override
        {
            assert(visitor);
            visitor->visit(this);
        }

        void computeInstructionBounds() override
        {
            Base::computeInstructionBounds();
        }
    };

}
```

## File: `Decompiler/Node/UnaryOperator.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>
#include <string>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class UnaryOperator final :
    public Base,
    public FieldValueNodeMixin<0>
{
public:
    UnaryOperator(size_t ip, std::uint8_t precedence, const Pex::StringTable::Index& result, const std::string& op, BasePtr value) :
        Base(1, ip, precedence, result),
        FieldValueNodeMixin(this, value),
        m_Op(op)
    {
    }
    virtual ~UnaryOperator() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    const std::string& getOperator() const { return m_Op; }

private:
    std::string m_Op;
};

}
```

## File: `Decompiler/Node/Visitor.cpp`
```cpp
#include "Visitor.hpp"

#include <cassert>

#include "Nodes.hpp"

void Node::Visitor::visitChildren(Node::Base *node)
{
    assert(node);
    for (auto child : *node)
    {
        if (child)
        {
            child->visit(this);
        }
    }
}

#define DO_NODE(NODE) \
void Node::VisitorBase::visit(Node::NODE *node) \
{ \
    assert(node); \
    visitChildren(node); \
}

FOR_EACH_NODE_CLASS()
#undef DO_NODE

Node::DynamicVisitor::DynamicVisitor()
{
    /*
    m_OnCommon = [&] (Base* node, DynamicVisitor* visitor)
    {
        visitor->VisitorBase::visit(node);
    };
    */
}

Node::DynamicVisitor &Node::DynamicVisitor::common(Node::DynamicVisitor::LambdaCommon common)
{
    m_OnCommon = common;
    return *this;
}


#define DO_NODE(NODE) \
void Node::DynamicVisitor::visit(Node::NODE *node) \
{ \
    assert(node); \
    if (m_On##NODE) \
        m_On##NODE(node, this); \
    else if (m_OnCommon) \
        m_OnCommon(node, this); \
    else \
        VisitorBase::visit(node); \
}

FOR_EACH_NODE_CLASS()
#undef DO_NODE


#define DO_NODE(NODE) \
Node::DynamicVisitor& Node::DynamicVisitor::operator<<(Lambda##NODE function) \
{ \
    m_On##NODE = function; \
    return *this; \
}

FOR_EACH_NODE_CLASS()
#undef DO_NODE
```

## File: `Decompiler/Node/Visitor.hpp`
```
#pragma once

#include <memory>
#include <functional>

#include "Base.hpp"

namespace Node {

#define FOR_EACH_NODE_CLASS() \
    DO_NODE(Scope) \
    DO_NODE(BinaryOperator) \
    DO_NODE(UnaryOperator) \
    DO_NODE(Assign) \
    DO_NODE(AssignOperator) \
    DO_NODE(Cast) \
    DO_NODE(CallMethod) \
    DO_NODE(Params) \
    DO_NODE(Copy) \
    DO_NODE(Return) \
    DO_NODE(PropertyAccess) \
    DO_NODE(ArrayCreate) \
    DO_NODE(ArrayLength) \
    DO_NODE(ArrayAccess) \
    DO_NODE(Constant) \
    DO_NODE(IdentifierString) \
    DO_NODE(While) \
    DO_NODE(IfElse) \
    DO_NODE(Declare) \
    DO_NODE(StructCreate)     \
    DO_NODE(GuardStatement)   \
    DO_NODE(TryGuard)          \
    DO_NODE(EndGuard)

#define DO_NODE(NODE) class NODE;
FOR_EACH_NODE_CLASS()
#undef DO_NODE

class Visitor
{
public:
    Visitor() = default;
    virtual ~Visitor() = default;

#define DO_NODE(NODE) virtual void visit(NODE* node) = 0;
    FOR_EACH_NODE_CLASS()
#undef DO_NODE

public:
    void visitChildren(Base* node);
};

class VisitorBase : public Visitor
{
public:
    VisitorBase() = default;
    virtual ~VisitorBase() = default;

#define DO_NODE(NODE) virtual void visit(NODE* node);
    FOR_EACH_NODE_CLASS()
#undef DO_NODE
};

class DynamicVisitor : public VisitorBase
{
public:    
#define DO_NODE(NODE) \
    typedef std::function<void (NODE* node, DynamicVisitor* visitor)> Lambda##NODE;

    FOR_EACH_NODE_CLASS()
#undef DO_NODE

    typedef std::function<void (Base* node, DynamicVisitor* visitor)> LambdaCommon;

public:
    DynamicVisitor();
    virtual ~DynamicVisitor() = default;

    DynamicVisitor& common(LambdaCommon common);

#define DO_NODE(NODE) virtual void visit(NODE* node);
    FOR_EACH_NODE_CLASS()
#undef DO_NODE

#define DO_NODE(NODE) DynamicVisitor& operator<<(Lambda##NODE function);
    FOR_EACH_NODE_CLASS()
#undef DO_NODE

#define DO_NODE(NODE) static const Lambda##NODE Clear##NODE;
    FOR_EACH_NODE_CLASS()
#undef DO_NODE

protected:
#define DO_NODE(NODE) Lambda##NODE m_On##NODE;
    FOR_EACH_NODE_CLASS()
#undef DO_NODE

    LambdaCommon m_OnCommon;
};

}
```

## File: `Decompiler/Node/While.hpp`
```
#pragma once

#include <cassert>
#include <cstdint>

#include "Base.hpp"
#include "FieldNodeMixin.hpp"
#include "Visitor.hpp"

namespace Node {

class While final :
    public Base,
    public FieldConditionNodeMixin<0>,
    public FieldBodyNodeMixin<1>
{
public:
    While(size_t ip, BasePtr condition, BasePtr body) :
        Base(2, ip, 10),
        FieldConditionNodeMixin(this, condition),
        FieldBodyNodeMixin(this, body)
    {
    }
    virtual ~While() = default;

    void visit(Visitor* visitor) override
    {
        assert(visitor);
        visitor->visit(this);
    }

    void computeInstructionBounds() override
    {
        Base::computeInstructionBounds();
        if (getCondition()->getBegin() == -1 && getCondition()->getEnd() == -1 && getBody()->size() != 0)
        {
            m_Begin = getBody()->getBegin() - 1;
            m_End = m_Begin;
        }
        else
        {
            m_Begin = getCondition()->getBegin();
            m_End = getCondition()->getEnd() + 1;
        }
    }
};

}
```

## File: `Decompiler/Node/WithNode.hpp`
```
#pragma once

#include <cassert>
#include <cstddef>
#include <deque>
#include <functional>

#include "Base.hpp"
#include "Visitor.hpp"

namespace Node {

template<typename T>
class WithNodeImplementation
{
    typedef std::function<bool (T*)> FilterFunction;
    typedef std::function<Node::BasePtr (T*)> TransformFunction;

    typedef std::deque<Node::BasePtr> ResultData;

public:
    WithNodeImplementation()
    {
        static_assert(std::is_base_of<Base, T>::value, "Only use on Base derived classes");

        m_FilterFunction = [=] (T*) {return true;};
    }
    ~WithNodeImplementation() = default;

    WithNodeImplementation& select(FilterFunction selector)
    {
        m_FilterFunction = selector;
        return *this;
    }

    WithNodeImplementation& transform(TransformFunction transform)
    {
        m_TransformFunction = transform;
        return *this;
    }

    ResultData from(BasePtr tree)
    {
        ResultData result;
        Node::DynamicVisitor nodeSelector;
        nodeSelector << (std::function<void (T*,  Node::DynamicVisitor*)>)[&] (T* node, Node::DynamicVisitor* visitor)
        {
            if (m_FilterFunction(node))
            {
                result.push_back(node->shared_from_this());
            }
            visitor->visitChildren(node);
        };

        tree->visit(&nodeSelector);

        return result;
    }

    int on(BasePtr tree)
    {
        assert(m_TransformFunction);

        int result = 0;
        Node::DynamicVisitor nodeSelector;
        nodeSelector << (std::function<void (T*,  Node::DynamicVisitor*)>)[&] (T* node, Node::DynamicVisitor* visitor)
        {
            visitor->visitChildren(node);
            if (m_FilterFunction(node))
            {
                assert(node->getParent());
                auto transformedNode = m_TransformFunction(node);
                if (transformedNode.get() != node)
                {
                    node->getParent()->replaceChild(node->shared_from_this(), transformedNode);
                }
                ++result;
            }
        };

        tree->visit(&nodeSelector);

        return result;
    }

protected:
    FilterFunction    m_FilterFunction;
    TransformFunction m_TransformFunction;
};

template<typename T>
WithNodeImplementation<T> WithNode()
{
    return WithNodeImplementation<T>();
}

}
```

## File: `Doc/Readme.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Champollion V1.1.3 Readme</title>
	<link rel="stylesheet" type="text/css" href="readme.css">
</head>

<body>
<h1>What's this ?</h1>
<p>Champollion is a decompiler for the Papyrus script language used in Skyrim. 
It aims to produce a Papyrus Script file (.psc) from a .pex binary file. 
The decompiled script should (hopefully) recompile to a functionally equivalent PEX binary.
</p>
<p>The source code is available at <a href="http://skyrim.nexusmods.com/mods/35307/">Skyrim NexusMod</a> under the LGPL V3 license</p>
<p>Copyright &copy; 2013 Paul-Henry Perrin</p>

<h1>Dependencies</h1>
Champollion needs the  <a href="http://www.microsoft.com/en-us/download/details.aspx?id=30679">runtime libraries for Visual C++ 11</a>

<h1>Usage</h1>
<p>The decompilation is driven by the Champollion.exe file</p>
<h2>Parameters</h2>
<div class="command-line">Champollion <span class="file">&lt;file or directory&gt;</span>
[-p <span class="file">&lt;output directory&gt;</span>] 
[-a [<span class="file">&lt;assembly directory&gt;</span>]] 
[-c] [-t]</div>
<br>
<table class="parameter">
<thead> 
	<tr>
		<th>Short</th>
		<th>Long</th>
		<th>Description</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>-p <span class="file">output directory</span></td>
		<td>--psc <span class="file">output directory</span></td>
		<td>Set the output directory, where Champollion will write the decompiled files</td>
	</tr>
	<tr>
		<td>-a [<span class="file">assembly directory</span>]</td>
		<td>--asm [<span class="file">assembly directory</span>]</td>
		<td>Champollion will write an assembly version of the PEX file in the given directory, if one. The assembly file is an human readable version of the content of the PEX file</td>
	</tr>
	<tr>
		<td>-c</td>
		<td>--comment</td>
		<td>The decompiled file will be annotated with the assembly instruction corresponding to the decompiled code lines.</td>
	</tr>
	<tr>
		<td>-t</td>
		<td>--threaded</td>
		<td>Champollion will parallelize the decompilation. It is usefull when decompiling a directory containing many PEX file.<br>
			To get the maximum speed, the output must be redirected to a file via the &gt; operator to avoid writing many lines to the console.
		</td>
	</tr>		
</tbody>
</table>

<h2>Examples</h2>

<p>Decompiling a file</p>
<div class="command-line">Champollion.exe bsa\out\scripts\arenascript.pex</div>
<div class="output">
<pre> 
bsa\out\scripts\arenascript.pex decompiled to .\arenascript.psc
1 files processed in 0.0160009 s
</pre>
</div>
<div class="psc-sample">
<span class="sample">arenascript.psc</span>
<pre>
;/ Decompiled by Champollion V1.0.0
Source   : ArenaScript.psc
Modified : 2012-02-12 00:06:16
Compiled : 2013-02-13 20:15:01
User     : builds
Computer : BUILDFARM09
/;
scriptName ArenaScript extends Quest conditional

;-- Properties --------------------------------------
int property WagerAmount auto
ArenaCombatQuest property SpecialFightDB auto
Armor property LoanerShield auto
bool property NextWagerFightIsPeople auto conditional
Faction property ArenaFaction auto
Faction property EastmarchCrimeFaction auto
ObjectReference property Gate1 auto
ReferenceAlias property PitDoor auto
Quest property EastmarchJail auto
bool property CombatOngoing auto conditional
Quest property DB03 auto
ArenaCombatQuest property Fight13 auto
ArenaCombatQuest property TransitionFight auto
Faction property SelfLoathing auto
ReferenceAlias property Combatant10 auto
ObjectReference property Gate2 auto
ArenaCombatQuest property Fight12 auto
Keyword property Wave4Keyword auto
Keyword property Wave2Keyword auto
bool property NextWagerFightIsEasyAnimals auto conditional
ObjectReference property Gate3 auto
bool property NextWagerFightIsExotic auto conditional
int property Level0Fights auto
int property NumberOfPlayerFights auto
ArenaCombatQuest property NextWagerFight auto
ArenaCombatQuest property Fight04 auto
ReferenceAlias property Combatant02 auto
ReferenceAlias property Combatant07 auto
ArenaCombatQuest property Fight01 auto
bool property PlayerChoseTheField auto conditional
ReferenceAlias property Combatant09 auto
ArenaCombatQuest property Fight05 auto
ReferenceAlias property Combatant03 auto
ArenaCombatQuest property SpecialFightJail auto
ArenaCombatQuest property CurrentFight auto
Keyword property Wave1Keyword auto
ReferenceAlias property Combatant08 auto
bool property RewardDue auto conditional
ReferenceAlias property TransitionCombatant auto
int property Level3Fights auto
ReferenceAlias property Combatant06 auto
bool property WagerResolutionRequired auto conditional
ArenaCombatQuest property Fight11 auto
ReferenceAlias property Combatant05 auto
ArenaCombatQuest property Fight03 auto
ArenaCombatQuest property Fight10 auto
ArenaCombatQuest property Fight09 auto
Faction property PacifyFaction auto
int property Level2Fights auto
ArenaCombatQuest property Fight06 auto
bool property NextWagerFightIsToughAnimals auto conditional
ReferenceAlias property Combatant04 auto
ArenaCombatQuest property Fight08 auto
Quest property ArenaWagerFighterQuest auto
Weapon property LoanerSword auto
bool property PlayerWonWager auto conditional
Keyword property Wave5Keyword auto
bool property PlayerGotTheSkinny auto conditional
ArenaCombatQuest property Fight02 auto
int property Level1Fights auto
bool property DBFightWentAwry = false auto conditional
Keyword property Wave3Keyword auto
int property ArrestOffset auto
bool property CombatPreSet auto
MiscObject property Gold auto
bool property WagerOngoing auto conditional
int property FightsToNextLevel auto conditional
ArenaCombatQuest property Fight07 auto
ReferenceAlias property Combatant01 auto
Quest property PointerQuest auto
Keyword property LinkedDoorKeyword auto

;-- Variables ---------------------------------------
int _maxFights = 13
ObjectReference _spawnPoint02
ObjectReference _spawnPoint03
ObjectReference _spawnPoint05
ObjectReference _spawnPoint04
ObjectReference _spawnPoint01

;-- Functions ---------------------------------------

function RegisterCombatant(ObjectReference fighter)

	(fighter as actor).AddToFaction(PacifyFaction)
	if CurrentFight != none && (CurrentFight as arenacombatquest).IsTransitionFight
		self.RegisterTransitionCombatant(fighter)
		return 
	endIf
	if Combatant01.ForceRefIfEmpty(fighter)
		
	elseIf Combatant02.ForceRefIfEmpty(fighter)
		
	elseIf Combatant03.ForceRefIfEmpty(fighter)
		
	elseIf Combatant04.ForceRefIfEmpty(fighter)
		
	elseIf Combatant05.ForceRefIfEmpty(fighter)
		
	elseIf Combatant06.ForceRefIfEmpty(fighter)
		
	elseIf Combatant07.ForceRefIfEmpty(fighter)
		
	elseIf Combatant08.ForceRefIfEmpty(fighter)
		
	elseIf Combatant09.ForceRefIfEmpty(fighter)
		
	elseIf Combatant10.ForceRefIfEmpty(fighter)
		
	endIf
endFunction

function Promote()

	game.GetPlayer().ModFactionRank(ArenaFaction, 1)
	int rank = game.GetPlayer().GetFactionRank(ArenaFaction)
	if rank == 1
		FightsToNextLevel = Level1Fights
	elseIf rank == 2
		FightsToNextLevel = Level2Fights
	elseIf rank == 3
		FightsToNextLevel = Level3Fights
	elseIf rank == 4
		FightsToNextLevel = 2147483647
	endIf
endFunction

function RegisterTransitionCombatant(ObjectReference fighter)

	if TransitionCombatant.GetReference() != none
		return 
	endIf
	TransitionCombatant.ForceRefTo(fighter)
	TransitionCombatant.GetActorReference().SetNoBleedoutRecovery(true)
endFunction

function EndWagerFight()

	bool fieldWon = (ArenaWagerFighterQuest as arenawagerfighterquestscript).fighter.GetActorReference().IsDead()
	NextWagerFight.Stop()
	if PlayerChoseTheField == fieldWon
		PlayerWonWager = true
	else
		PlayerWonWager = false
	endIf
	WagerResolutionRequired = true
endFunction

; Skipped compiler generated GotoState

keyword function GetKeywordForWave(int wave)

	if wave == 1
		return Wave1Keyword
	elseIf wave == 2
		return Wave2Keyword
	elseIf wave == 3
		return Wave3Keyword
	elseIf wave == 4
		return Wave4Keyword
	elseIf wave == 5
		return Wave5Keyword
	else
		return none
	endIf
endFunction

function PlayerJoin()

	if PointerQuest.IsRunning()
		PointerQuest.SetStage(20)
	endIf
	game.GetPlayer().AddToFaction(ArenaFaction)
	NumberOfPlayerFights = 0
	FightsToNextLevel = Level0Fights
endFunction

function PlayerAvoidedWager()

	PlayerChoseTheField = false
	WagerOngoing = false
endFunction

function CombatOver()

	if WagerOngoing
		self.EndWagerFight()
		return 
	endIf
	CurrentFight.Stop()
	PitDoor.GetReference().Lock(false, false)
	CombatOngoing = false
	RewardDue = true
	NumberOfPlayerFights += 1
endFunction

function ResolveWager()

	if PlayerWonWager
		game.GetPlayer().AddItem(Gold as form, WagerAmount * 2, false)
	endIf
	self.CleanupBodies()
	WagerOngoing = false
	WagerResolutionRequired = false
	ArenaWagerFighterQuest.Stop()
	self.PickNextWagerFight(NextWagerFight)
endFunction

function StartWagerFight()

	NextWagerFight.Start()
	ArenaWagerFighterQuest.Start()
	CombatPreSet = true
endFunction

function StartCombat()

	if 20 <= DB03.GetStage() && 40 > DB03.GetStage()
		CurrentFight = SpecialFightDB
		if game.GetPlayer().GetItemCount(LoanerSword as form) < 1
			game.GetPlayer().AddItem(LoanerSword as form, 1, false)
		endIf
		if game.GetPlayer().GetItemCount(LoanerShield as form) < 1
			game.GetPlayer().AddItem(LoanerShield as form, 1, false)
		endIf
		game.GetPlayer().EquipItem(LoanerSword as form, false, false)
		game.GetPlayer().EquipItem(LoanerShield as form, false, false)
	elseIf 20 == EastmarchJail.GetStage() && EastmarchJail.IsRunning()
		CurrentFight = SpecialFightJail
		game.GetPlayer().AddItem(LoanerSword as form, 1, false)
		game.GetPlayer().AddItem(LoanerShield as form, 1, false)
		game.GetPlayer().EquipItem(LoanerSword as form, false, false)
		game.GetPlayer().EquipItem(LoanerShield as form, false, false)
	else
		CurrentFight = self.PickNextFight(0)
	endIf
	CurrentFight.Start()
	CombatPreSet = true
	PitDoor.GetReference().Lock(false, false)
	CombatOngoing = true
endFunction

arenacombatquest function GetFightQuestFromIndex(int questIndex)

	if questIndex == 1
		return Fight01
	elseIf questIndex == 2
		return Fight02
	elseIf questIndex == 3
		return Fight03
	elseIf questIndex == 4
		return Fight04
	elseIf questIndex == 5
		return Fight05
	elseIf questIndex == 6
		return Fight06
	elseIf questIndex == 7
		return Fight07
	elseIf questIndex == 8
		return Fight08
	elseIf questIndex == 9
		return Fight09
	elseIf questIndex == 10
		return Fight10
	elseIf questIndex == 11
		return Fight11
	elseIf questIndex == 12
		return Fight12
	elseIf questIndex == 13
		return Fight13
	else
		return none
	endIf
endFunction

function CleanupBodies()

	if self._CleanupBody(Combatant01)
		
	endIf
	if self._CleanupBody(Combatant02)
		
	endIf
	if self._CleanupBody(Combatant03)
		
	endIf
	if self._CleanupBody(Combatant04)
		
	endIf
	if self._CleanupBody(Combatant05)
		
	endIf
	if self._CleanupBody(Combatant06)
		
	endIf
	if self._CleanupBody(Combatant07)
		
	endIf
	if self._CleanupBody(Combatant08)
		
	endIf
	if self._CleanupBody(Combatant09)
		
	endIf
	if self._CleanupBody(Combatant10)
		
	endIf
	if TransitionCombatant.GetReference() != none
		actor ref = TransitionCombatant.GetActorReference()
		game.GetPlayer().RemoveFromFaction(SelfLoathing)
		ref.RemoveFromFaction(SelfLoathing)
		ref.SetFactionRank(ArenaFaction, 4)
		ref.SetNoBleedoutRecovery(false)
		TransitionCombatant.Clear()
	endIf
	_spawnPoint01 = none
	_spawnPoint02 = none
	_spawnPoint03 = none
	_spawnPoint04 = none
	_spawnPoint05 = none
	Gate1.SetOpen(false)
	Gate2.SetOpen(false)
	Gate3.SetOpen(false)
endFunction

bool function _CleanupBody(referencealias combatant)

	if combatant.GetReference() != none
		actor ref = combatant.GetActorReference()
		combatant.Clear()
		if WagerOngoing
			ref.Delete()
		elseIf ref.IsDead()
			ref.Delete()
		else
			ref.MoveToMyEditorLocation()
			ref.ResetHealthAndLimbs()
		endIf
		return true
	else
		return false
	endIf
endFunction

function Reward()

	PitDoor.GetReference().Lock(true, false)
	self.CleanupBodies()
	if 20 == EastmarchJail.GetStage() && EastmarchJail.IsRunning()
		game.GetPlayer().UnequipItem(LoanerSword as form, false, false)
		game.GetPlayer().UnequipItem(LoanerShield as form, false, false)
		game.GetPlayer().RemoveItem(LoanerSword as form, 1, false, none)
		game.GetPlayer().RemoveItem(LoanerShield as form, 1, false, none)
		EastmarchCrimeFaction.SetCrimeGold(0)
		EastmarchCrimeFaction.SetCrimeGoldViolent(0)
		EastmarchJail.SetStage(200)
	elseIf game.GetPlayer().GetFactionRank(ArenaFaction) >= 4
		game.GetPlayer().AddItem(Gold as form, 100, false)
	elseIf FightsToNextLevel <= 0
		self.Promote()
	else
		game.GetPlayer().AddItem(Gold as form, 100, false)
		FightsToNextLevel -= 1
	endIf
	RewardDue = false
endFunction

function PlaceBet(int amount)

	WagerOngoing = true
	WagerAmount = amount
	game.GetPlayer().RemoveItem(Gold as form, WagerAmount, false, none)
endFunction

function RegisterSpawnPoint(ObjectReference spawnMarker)

	if _spawnPoint01 == none
		_spawnPoint01 = spawnMarker
	elseIf _spawnPoint02 == none
		_spawnPoint02 = spawnMarker
	elseIf _spawnPoint03 == none
		_spawnPoint03 = spawnMarker
	elseIf _spawnPoint04 == none
		_spawnPoint04 = spawnMarker
	elseIf _spawnPoint05 == none
		_spawnPoint05 = spawnMarker
	endIf
endFunction

int function GetIndexFromFightQuest(arenacombatquest rQuest)

	if rQuest == Fight01
		return 1
	elseIf rQuest == Fight02
		return 2
	elseIf rQuest == Fight03
		return 3
	elseIf rQuest == Fight04
		return 4
	elseIf rQuest == Fight05
		return 5
	elseIf rQuest == Fight06
		return 6
	elseIf rQuest == Fight07
		return 7
	elseIf rQuest == Fight08
		return 8
	elseIf rQuest == Fight09
		return 9
	elseIf rQuest == Fight10
		return 10
	elseIf rQuest == Fight11
		return 11
	elseIf rQuest == Fight12
		return 12
	elseIf rQuest == Fight13
		return 13
	else
		return 0
	endIf
endFunction

ObjectReference function GetDoorForWave(int wave)

	keyword toMatch = self.GetKeywordForWave(wave)
	if _spawnPoint01.HasKeyword(toMatch)
		return _spawnPoint01.GetLinkedRef(LinkedDoorKeyword)
	elseIf _spawnPoint02.HasKeyword(toMatch)
		return _spawnPoint02.GetLinkedRef(LinkedDoorKeyword)
	elseIf _spawnPoint03.HasKeyword(toMatch)
		return _spawnPoint03.GetLinkedRef(LinkedDoorKeyword)
	elseIf _spawnPoint04.HasKeyword(toMatch)
		return _spawnPoint04.GetLinkedRef(LinkedDoorKeyword)
	elseIf _spawnPoint05.HasKeyword(toMatch)
		return _spawnPoint05.GetLinkedRef(LinkedDoorKeyword)
	else
		return none
	endIf
endFunction

function PickNextWagerFight(arenacombatquest lastFight)

	int lastFightIndex = -1
	if lastFight != none
		lastFightIndex = self.GetIndexFromFightQuest(lastFight)
	endIf
	int fightIndex = lastFightIndex
	while fightIndex == lastFightIndex
		fightIndex = utility.RandomInt(1, _maxFights)
	endWhile
	NextWagerFight = self.GetFightQuestFromIndex(fightIndex)
	NextWagerFightIsToughAnimals = false
	NextWagerFightIsEasyAnimals = false
	NextWagerFightIsPeople = false
	NextWagerFightIsExotic = false
	if NextWagerFight == Fight01
		NextWagerFightIsEasyAnimals = true
	elseIf NextWagerFight == Fight02
		NextWagerFightIsEasyAnimals = true
	elseIf NextWagerFight == Fight03
		NextWagerFightIsEasyAnimals = true
	elseIf NextWagerFight == Fight04
		NextWagerFightIsPeople = true
	elseIf NextWagerFight == Fight05
		NextWagerFightIsToughAnimals = true
	elseIf NextWagerFight == Fight06
		NextWagerFightIsToughAnimals = true
	elseIf NextWagerFight == Fight07
		NextWagerFightIsToughAnimals = true
	elseIf NextWagerFight == Fight08
		NextWagerFightIsToughAnimals = true
	elseIf NextWagerFight == Fight09
		NextWagerFightIsPeople = true
	elseIf NextWagerFight == Fight10
		NextWagerFightIsExotic = true
	elseIf NextWagerFight == Fight11
		NextWagerFightIsPeople = true
	elseIf NextWagerFight == Fight12
		NextWagerFightIsExotic = true
	elseIf NextWagerFight == Fight13
		NextWagerFightIsPeople = true
	endIf
endFunction

referencealias function GetCombatantAlias(int index)

	if index == 1
		return Combatant01
	elseIf index == 2
		return Combatant02
	elseIf index == 3
		return Combatant03
	elseIf index == 4
		return Combatant04
	elseIf index == 5
		return Combatant05
	elseIf index == 6
		return Combatant06
	elseIf index == 7
		return Combatant07
	elseIf index == 8
		return Combatant08
	elseIf index == 9
		return Combatant09
	elseIf index == 10
		return Combatant10
	else
		return none
	endIf
endFunction

; Skipped compiler generated GetState

function Setup()

	WagerOngoing = false
	self.PickNextWagerFight(none)
endFunction

arenacombatquest function PickNextFight(int offset)

	int minFight = -1
	int maxFight = -1
	int playerRank = game.GetPlayer().GetFactionRank(ArenaFaction)
	if FightsToNextLevel <= 0
		return TransitionFight
	endIf
	if playerRank == 0
		minFight = 1
		maxFight = 3
		int fightIndex = utility.RandomInt(minFight, maxFight)
		return self.GetFightQuestFromIndex(fightIndex)
	elseIf playerRank == 1
		bool humanFight = utility.RandomInt(0, 2) as bool
		if !humanFight
			minFight = 2
			maxFight = 3
			int fightindex = utility.RandomInt(minFight, maxFight)
			return self.GetFightQuestFromIndex(fightindex)
		else
			return Fight04
		endIf
	elseIf playerRank == 2
		minFight = 5
		maxFight = 9
		int fightindex = utility.RandomInt(minFight, maxFight)
		return self.GetFightQuestFromIndex(fightindex)
	elseIf playerRank == 3
		int animalFight = utility.RandomInt(0, 2)
		if animalFight == 0
			minFight = 7
			maxFight = 9
			int fightindex = utility.RandomInt(minFight, maxFight)
			if fightindex == 9
				fightindex = 10
			endIf
			return self.GetFightQuestFromIndex(fightindex)
		else
			return Fight11
		endIf
	else
		int fightRoll = utility.RandomInt(1, 10)
		if fightRoll <= 3
			if utility.RandomInt(0, 1)
				return Fight08
			else
				return Fight10
			endIf
		elseIf fightRoll <= 9
			return Fight13
		else
			return Fight12
		endIf
	endIf
	return none
endFunction
</pre>
</div>

<p>Decompiling a file in a subdirectory, with the assembly file in another</p>
<div class="command-line">Champollion.exe bsa\out\scripts\arenascript.pex -p decompiled -a asm</div>
<div class="output">
<pre>
bsa\out\scripts\arenascript.pex dissassembled to asm\arenascript.pas
bsa\out\scripts\arenascript.pex decompiled to decompiled\arenascript.psc
1 files processed in 0.0290016 s
</pre>
</div>
<div class="psc-sample">
<span class="sample">decompiled\arenascript.psc</span>
<pre>
;/ Decompiled by Champollion V1.0.0
Source   : ArenaScript.psc
Modified : 2012-02-12 00:06:16
Compiled : 2013-02-13 20:15:01
User     : builds
Computer : BUILDFARM09
/;
scriptName ArenaScript extends Quest conditional

;-- Properties --------------------------------------
int property WagerAmount auto
ArenaCombatQuest property SpecialFightDB auto
Armor property LoanerShield auto
bool property NextWagerFightIsPeople auto conditional
Faction property ArenaFaction auto
Faction property EastmarchCrimeFaction auto
ObjectReference property Gate1 auto
ReferenceAlias property PitDoor auto
Quest property EastmarchJail auto
bool property CombatOngoing auto conditional
Quest property DB03 auto
ArenaCombatQuest property Fight13 auto
ArenaCombatQuest property TransitionFight auto
Faction property SelfLoathing auto
ReferenceAlias property Combatant10 auto
ObjectReference property Gate2 auto
ArenaCombatQuest property Fight12 auto
Keyword property Wave4Keyword auto
Keyword property Wave2Keyword auto
bool property NextWagerFightIsEasyAnimals auto conditional
ObjectReference property Gate3 auto
bool property NextWagerFightIsExotic auto conditional
int property Level0Fights auto
int property NumberOfPlayerFights auto
ArenaCombatQuest property NextWagerFight auto
ArenaCombatQuest property Fight04 auto
ReferenceAlias property Combatant02 auto
ReferenceAlias property Combatant07 auto
ArenaCombatQuest property Fight01 auto
bool property PlayerChoseTheField auto conditional
ReferenceAlias property Combatant09 auto
ArenaCombatQuest property Fight05 auto
ReferenceAlias property Combatant03 auto
ArenaCombatQuest property SpecialFightJail auto
ArenaCombatQuest property CurrentFight auto
Keyword property Wave1Keyword auto
ReferenceAlias property Combatant08 auto
bool property RewardDue auto conditional
ReferenceAlias property TransitionCombatant auto
int property Level3Fights auto
ReferenceAlias property Combatant06 auto
bool property WagerResolutionRequired auto conditional
ArenaCombatQuest property Fight11 auto
ReferenceAlias property Combatant05 auto
ArenaCombatQuest property Fight03 auto
ArenaCombatQuest property Fight10 auto
ArenaCombatQuest property Fight09 auto
Faction property PacifyFaction auto
int property Level2Fights auto
ArenaCombatQuest property Fight06 auto
bool property NextWagerFightIsToughAnimals auto conditional
ReferenceAlias property Combatant04 auto
ArenaCombatQuest property Fight08 auto
Quest property ArenaWagerFighterQuest auto
Weapon property LoanerSword auto
bool property PlayerWonWager auto conditional
Keyword property Wave5Keyword auto
bool property PlayerGotTheSkinny auto conditional
ArenaCombatQuest property Fight02 auto
int property Level1Fights auto
bool property DBFightWentAwry = false auto conditional
Keyword property Wave3Keyword auto
int property ArrestOffset auto
bool property CombatPreSet auto
MiscObject property Gold auto
bool property WagerOngoing auto conditional
int property FightsToNextLevel auto conditional
ArenaCombatQuest property Fight07 auto
ReferenceAlias property Combatant01 auto
Quest property PointerQuest auto
Keyword property LinkedDoorKeyword auto

;-- Variables ---------------------------------------
int _maxFights = 13
ObjectReference _spawnPoint02
ObjectReference _spawnPoint03
ObjectReference _spawnPoint05
ObjectReference _spawnPoint04
ObjectReference _spawnPoint01

;-- Functions ---------------------------------------

function RegisterCombatant(ObjectReference fighter)

	(fighter as actor).AddToFaction(PacifyFaction)
	if CurrentFight != none && (CurrentFight as arenacombatquest).IsTransitionFight
		self.RegisterTransitionCombatant(fighter)
		return 
	endIf
	if Combatant01.ForceRefIfEmpty(fighter)
		
	elseIf Combatant02.ForceRefIfEmpty(fighter)
		
	elseIf Combatant03.ForceRefIfEmpty(fighter)
		
	elseIf Combatant04.ForceRefIfEmpty(fighter)
		
	elseIf Combatant05.ForceRefIfEmpty(fighter)
		
	elseIf Combatant06.ForceRefIfEmpty(fighter)
		
	elseIf Combatant07.ForceRefIfEmpty(fighter)
		
	elseIf Combatant08.ForceRefIfEmpty(fighter)
		
	elseIf Combatant09.ForceRefIfEmpty(fighter)
		
	elseIf Combatant10.ForceRefIfEmpty(fighter)
		
	endIf
endFunction

function Promote()

	game.GetPlayer().ModFactionRank(ArenaFaction, 1)
	int rank = game.GetPlayer().GetFactionRank(ArenaFaction)
	if rank == 1
		FightsToNextLevel = Level1Fights
	elseIf rank == 2
		FightsToNextLevel = Level2Fights
	elseIf rank == 3
		FightsToNextLevel = Level3Fights
	elseIf rank == 4
		FightsToNextLevel = 2147483647
	endIf
endFunction

function RegisterTransitionCombatant(ObjectReference fighter)

	if TransitionCombatant.GetReference() != none
		return 
	endIf
	TransitionCombatant.ForceRefTo(fighter)
	TransitionCombatant.GetActorReference().SetNoBleedoutRecovery(true)
endFunction

function EndWagerFight()

	bool fieldWon = (ArenaWagerFighterQuest as arenawagerfighterquestscript).fighter.GetActorReference().IsDead()
	NextWagerFight.Stop()
	if PlayerChoseTheField == fieldWon
		PlayerWonWager = true
	else
		PlayerWonWager = false
	endIf
	WagerResolutionRequired = true
endFunction

; Skipped compiler generated GotoState

keyword function GetKeywordForWave(int wave)

	if wave == 1
		return Wave1Keyword
	elseIf wave == 2
		return Wave2Keyword
	elseIf wave == 3
		return Wave3Keyword
	elseIf wave == 4
		return Wave4Keyword
	elseIf wave == 5
		return Wave5Keyword
	else
		return none
	endIf
endFunction

function PlayerJoin()

	if PointerQuest.IsRunning()
		PointerQuest.SetStage(20)
	endIf
	game.GetPlayer().AddToFaction(ArenaFaction)
	NumberOfPlayerFights = 0
	FightsToNextLevel = Level0Fights
endFunction

function PlayerAvoidedWager()

	PlayerChoseTheField = false
	WagerOngoing = false
endFunction

function CombatOver()

	if WagerOngoing
		self.EndWagerFight()
		return 
	endIf
	CurrentFight.Stop()
	PitDoor.GetReference().Lock(false, false)
	CombatOngoing = false
	RewardDue = true
	NumberOfPlayerFights += 1
endFunction

function ResolveWager()

	if PlayerWonWager
		game.GetPlayer().AddItem(Gold as form, WagerAmount * 2, false)
	endIf
	self.CleanupBodies()
	WagerOngoing = false
	WagerResolutionRequired = false
	ArenaWagerFighterQuest.Stop()
	self.PickNextWagerFight(NextWagerFight)
endFunction

function StartWagerFight()

	NextWagerFight.Start()
	ArenaWagerFighterQuest.Start()
	CombatPreSet = true
endFunction

function StartCombat()

	if 20 <= DB03.GetStage() && 40 > DB03.GetStage()
		CurrentFight = SpecialFightDB
		if game.GetPlayer().GetItemCount(LoanerSword as form) < 1
			game.GetPlayer().AddItem(LoanerSword as form, 1, false)
		endIf
		if game.GetPlayer().GetItemCount(LoanerShield as form) < 1
			game.GetPlayer().AddItem(LoanerShield as form, 1, false)
		endIf
		game.GetPlayer().EquipItem(LoanerSword as form, false, false)
		game.GetPlayer().EquipItem(LoanerShield as form, false, false)
	elseIf 20 == EastmarchJail.GetStage() && EastmarchJail.IsRunning()
		CurrentFight = SpecialFightJail
		game.GetPlayer().AddItem(LoanerSword as form, 1, false)
		game.GetPlayer().AddItem(LoanerShield as form, 1, false)
		game.GetPlayer().EquipItem(LoanerSword as form, false, false)
		game.GetPlayer().EquipItem(LoanerShield as form, false, false)
	else
		CurrentFight = self.PickNextFight(0)
	endIf
	CurrentFight.Start()
	CombatPreSet = true
	PitDoor.GetReference().Lock(false, false)
	CombatOngoing = true
endFunction

arenacombatquest function GetFightQuestFromIndex(int questIndex)

	if questIndex == 1
		return Fight01
	elseIf questIndex == 2
		return Fight02
	elseIf questIndex == 3
		return Fight03
	elseIf questIndex == 4
		return Fight04
	elseIf questIndex == 5
		return Fight05
	elseIf questIndex == 6
		return Fight06
	elseIf questIndex == 7
		return Fight07
	elseIf questIndex == 8
		return Fight08
	elseIf questIndex == 9
		return Fight09
	elseIf questIndex == 10
		return Fight10
	elseIf questIndex == 11
		return Fight11
	elseIf questIndex == 12
		return Fight12
	elseIf questIndex == 13
		return Fight13
	else
		return none
	endIf
endFunction

function CleanupBodies()

	if self._CleanupBody(Combatant01)
		
	endIf
	if self._CleanupBody(Combatant02)
		
	endIf
	if self._CleanupBody(Combatant03)
		
	endIf
	if self._CleanupBody(Combatant04)
		
	endIf
	if self._CleanupBody(Combatant05)
		
	endIf
	if self._CleanupBody(Combatant06)
		
	endIf
	if self._CleanupBody(Combatant07)
		
	endIf
	if self._CleanupBody(Combatant08)
		
	endIf
	if self._CleanupBody(Combatant09)
		
	endIf
	if self._CleanupBody(Combatant10)
		
	endIf
	if TransitionCombatant.GetReference() != none
		actor ref = TransitionCombatant.GetActorReference()
		game.GetPlayer().RemoveFromFaction(SelfLoathing)
		ref.RemoveFromFaction(SelfLoathing)
		ref.SetFactionRank(ArenaFaction, 4)
		ref.SetNoBleedoutRecovery(false)
		TransitionCombatant.Clear()
	endIf
	_spawnPoint01 = none
	_spawnPoint02 = none
	_spawnPoint03 = none
	_spawnPoint04 = none
	_spawnPoint05 = none
	Gate1.SetOpen(false)
	Gate2.SetOpen(false)
	Gate3.SetOpen(false)
endFunction

bool function _CleanupBody(referencealias combatant)

	if combatant.GetReference() != none
		actor ref = combatant.GetActorReference()
		combatant.Clear()
		if WagerOngoing
			ref.Delete()
		elseIf ref.IsDead()
			ref.Delete()
		else
			ref.MoveToMyEditorLocation()
			ref.ResetHealthAndLimbs()
		endIf
		return true
	else
		return false
	endIf
endFunction

function Reward()

	PitDoor.GetReference().Lock(true, false)
	self.CleanupBodies()
	if 20 == EastmarchJail.GetStage() && EastmarchJail.IsRunning()
		game.GetPlayer().UnequipItem(LoanerSword as form, false, false)
		game.GetPlayer().UnequipItem(LoanerShield as form, false, false)
		game.GetPlayer().RemoveItem(LoanerSword as form, 1, false, none)
		game.GetPlayer().RemoveItem(LoanerShield as form, 1, false, none)
		EastmarchCrimeFaction.SetCrimeGold(0)
		EastmarchCrimeFaction.SetCrimeGoldViolent(0)
		EastmarchJail.SetStage(200)
	elseIf game.GetPlayer().GetFactionRank(ArenaFaction) >= 4
		game.GetPlayer().AddItem(Gold as form, 100, false)
	elseIf FightsToNextLevel <= 0
		self.Promote()
	else
		game.GetPlayer().AddItem(Gold as form, 100, false)
		FightsToNextLevel -= 1
	endIf
	RewardDue = false
endFunction

function PlaceBet(int amount)

	WagerOngoing = true
	WagerAmount = amount
	game.GetPlayer().RemoveItem(Gold as form, WagerAmount, false, none)
endFunction

function RegisterSpawnPoint(ObjectReference spawnMarker)

	if _spawnPoint01 == none
		_spawnPoint01 = spawnMarker
	elseIf _spawnPoint02 == none
		_spawnPoint02 = spawnMarker
	elseIf _spawnPoint03 == none
		_spawnPoint03 = spawnMarker
	elseIf _spawnPoint04 == none
		_spawnPoint04 = spawnMarker
	elseIf _spawnPoint05 == none
		_spawnPoint05 = spawnMarker
	endIf
endFunction

int function GetIndexFromFightQuest(arenacombatquest rQuest)

	if rQuest == Fight01
		return 1
	elseIf rQuest == Fight02
		return 2
	elseIf rQuest == Fight03
		return 3
	elseIf rQuest == Fight04
		return 4
	elseIf rQuest == Fight05
		return 5
	elseIf rQuest == Fight06
		return 6
	elseIf rQuest == Fight07
		return 7
	elseIf rQuest == Fight08
		return 8
	elseIf rQuest == Fight09
		return 9
	elseIf rQuest == Fight10
		return 10
	elseIf rQuest == Fight11
		return 11
	elseIf rQuest == Fight12
		return 12
	elseIf rQuest == Fight13
		return 13
	else
		return 0
	endIf
endFunction

ObjectReference function GetDoorForWave(int wave)

	keyword toMatch = self.GetKeywordForWave(wave)
	if _spawnPoint01.HasKeyword(toMatch)
		return _spawnPoint01.GetLinkedRef(LinkedDoorKeyword)
	elseIf _spawnPoint02.HasKeyword(toMatch)
		return _spawnPoint02.GetLinkedRef(LinkedDoorKeyword)
	elseIf _spawnPoint03.HasKeyword(toMatch)
		return _spawnPoint03.GetLinkedRef(LinkedDoorKeyword)
	elseIf _spawnPoint04.HasKeyword(toMatch)
		return _spawnPoint04.GetLinkedRef(LinkedDoorKeyword)
	elseIf _spawnPoint05.HasKeyword(toMatch)
		return _spawnPoint05.GetLinkedRef(LinkedDoorKeyword)
	else
		return none
	endIf
endFunction

function PickNextWagerFight(arenacombatquest lastFight)

	int lastFightIndex = -1
	if lastFight != none
		lastFightIndex = self.GetIndexFromFightQuest(lastFight)
	endIf
	int fightIndex = lastFightIndex
	while fightIndex == lastFightIndex
		fightIndex = utility.RandomInt(1, _maxFights)
	endWhile
	NextWagerFight = self.GetFightQuestFromIndex(fightIndex)
	NextWagerFightIsToughAnimals = false
	NextWagerFightIsEasyAnimals = false
	NextWagerFightIsPeople = false
	NextWagerFightIsExotic = false
	if NextWagerFight == Fight01
		NextWagerFightIsEasyAnimals = true
	elseIf NextWagerFight == Fight02
		NextWagerFightIsEasyAnimals = true
	elseIf NextWagerFight == Fight03
		NextWagerFightIsEasyAnimals = true
	elseIf NextWagerFight == Fight04
		NextWagerFightIsPeople = true
	elseIf NextWagerFight == Fight05
		NextWagerFightIsToughAnimals = true
	elseIf NextWagerFight == Fight06
		NextWagerFightIsToughAnimals = true
	elseIf NextWagerFight == Fight07
		NextWagerFightIsToughAnimals = true
	elseIf NextWagerFight == Fight08
		NextWagerFightIsToughAnimals = true
	elseIf NextWagerFight == Fight09
		NextWagerFightIsPeople = true
	elseIf NextWagerFight == Fight10
		NextWagerFightIsExotic = true
	elseIf NextWagerFight == Fight11
		NextWagerFightIsPeople = true
	elseIf NextWagerFight == Fight12
		NextWagerFightIsExotic = true
	elseIf NextWagerFight == Fight13
		NextWagerFightIsPeople = true
	endIf
endFunction

referencealias function GetCombatantAlias(int index)

	if index == 1
		return Combatant01
	elseIf index == 2
		return Combatant02
	elseIf index == 3
		return Combatant03
	elseIf index == 4
		return Combatant04
	elseIf index == 5
		return Combatant05
	elseIf index == 6
		return Combatant06
	elseIf index == 7
		return Combatant07
	elseIf index == 8
		return Combatant08
	elseIf index == 9
		return Combatant09
	elseIf index == 10
		return Combatant10
	else
		return none
	endIf
endFunction

; Skipped compiler generated GetState

function Setup()

	WagerOngoing = false
	self.PickNextWagerFight(none)
endFunction

arenacombatquest function PickNextFight(int offset)

	int minFight = -1
	int maxFight = -1
	int playerRank = game.GetPlayer().GetFactionRank(ArenaFaction)
	if FightsToNextLevel <= 0
		return TransitionFight
	endIf
	if playerRank == 0
		minFight = 1
		maxFight = 3
		int fightIndex = utility.RandomInt(minFight, maxFight)
		return self.GetFightQuestFromIndex(fightIndex)
	elseIf playerRank == 1
		bool humanFight = utility.RandomInt(0, 2) as bool
		if !humanFight
			minFight = 2
			maxFight = 3
			int fightindex = utility.RandomInt(minFight, maxFight)
			return self.GetFightQuestFromIndex(fightindex)
		else
			return Fight04
		endIf
	elseIf playerRank == 2
		minFight = 5
		maxFight = 9
		int fightindex = utility.RandomInt(minFight, maxFight)
		return self.GetFightQuestFromIndex(fightindex)
	elseIf playerRank == 3
		int animalFight = utility.RandomInt(0, 2)
		if animalFight == 0
			minFight = 7
			maxFight = 9
			int fightindex = utility.RandomInt(minFight, maxFight)
			if fightindex == 9
				fightindex = 10
			endIf
			return self.GetFightQuestFromIndex(fightindex)
		else
			return Fight11
		endIf
	else
		int fightRoll = utility.RandomInt(1, 10)
		if fightRoll <= 3
			if utility.RandomInt(0, 1)
				return Fight08
			else
				return Fight10
			endIf
		elseIf fightRoll <= 9
			return Fight13
		else
			return Fight12
		endIf
	endIf
	return none
endFunction

</pre>
</div>

<div class="psc-sample">
<span class="sample">asm\arenascript.pas</span>
<pre>
.info
	.source "ArenaScript.psc"
	.modifyTime 1329001576 ;2012-02-12 00:06:16
	.compileTime 1360782901 ;2013-02-13 20:15:01
	.user "builds"
	.computer "BUILDFARM09"
.endInfo
.userFlagsRef
	.flag hidden 0 ;0x00000001
	.flag conditional 1 ;0x00000002
.endUserFlagsRef
.objectTable
	.object ArenaScript Quest
		.userFlags 2 ;conditional 
		.docString ""
		.autoState 
		.variableTable
			.variable ::Level0Fights_var int
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Level3Fights_var int
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::FightsToNextLevel_var int
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::NextWagerFightIsExotic_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::Fight03_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Combatant08_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Combatant04_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::PointerQuest_var quest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::RewardDue_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::ArenaWagerFighterQuest_var quest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Fight08_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::NextWagerFight_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Combatant03_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Fight12_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable _maxFights int
				.userFlags 0 ;none
				.initialValue 13
			.endVariable
			.variable ::NumberOfPlayerFights_var int
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::SpecialFightDB_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::PlayerGotTheSkinny_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::CurrentFight_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Wave4Keyword_var keyword
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Wave3Keyword_var keyword
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Fight05_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::WagerAmount_var int
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::PlayerWonWager_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::Fight13_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Gold_var miscobject
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::ArenaFaction_var faction
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Wave1Keyword_var keyword
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::DBFightWentAwry_var bool
				.userFlags 2 ;conditional 
				.initialValue false
			.endVariable
			.variable ::Fight02_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Combatant09_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Combatant05_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::CombatOngoing_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::Level1Fights_var int
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Level2Fights_var int
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable _spawnPoint02 ObjectReference
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::SpecialFightJail_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Wave5Keyword_var keyword
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Fight07_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Fight11_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::EastmarchCrimeFaction_var faction
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::SelfLoathing_var faction
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable _spawnPoint03 ObjectReference
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::LinkedDoorKeyword_var keyword
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::WagerOngoing_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::Combatant07_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::NextWagerFightIsToughAnimals_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::PlayerChoseTheField_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::NextWagerFightIsEasyAnimals_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::Fight09_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Combatant02_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable _spawnPoint05 ObjectReference
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Fight04_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::TransitionFight_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Fight01_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::CombatPreSet_var bool
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::DB03_var quest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::PacifyFaction_var faction
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Combatant06_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::EastmarchJail_var quest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::ArrestOffset_var int
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable _spawnPoint04 ObjectReference
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Wave2Keyword_var keyword
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::LoanerShield_var armor
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Gate1_var objectreference
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::LoanerSword_var weapon
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::TransitionCombatant_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Gate2_var objectreference
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Gate3_var objectreference
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Combatant10_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Fight06_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::PitDoor_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Combatant01_var referencealias
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::Fight10_var arenacombatquest
				.userFlags 0 ;none
				.initialValue none
			.endVariable
			.variable ::WagerResolutionRequired_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable ::NextWagerFightIsPeople_var bool
				.userFlags 2 ;conditional 
				.initialValue none
			.endVariable
			.variable _spawnPoint01 ObjectReference
				.userFlags 0 ;none
				.initialValue none
			.endVariable
		.endVariableTable
		.propertyTable
			.property WagerAmount int auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::WagerAmount_var
			.endProperty
			.property SpecialFightDB ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::SpecialFightDB_var
			.endProperty
			.property LoanerShield Armor auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::LoanerShield_var
			.endProperty
			.property NextWagerFightIsPeople bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::NextWagerFightIsPeople_var
			.endProperty
			.property ArenaFaction Faction auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::ArenaFaction_var
			.endProperty
			.property EastmarchCrimeFaction Faction auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::EastmarchCrimeFaction_var
			.endProperty
			.property Gate1 ObjectReference auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Gate1_var
			.endProperty
			.property PitDoor ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::PitDoor_var
			.endProperty
			.property EastmarchJail Quest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::EastmarchJail_var
			.endProperty
			.property CombatOngoing bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::CombatOngoing_var
			.endProperty
			.property DB03 Quest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::DB03_var
			.endProperty
			.property Fight13 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight13_var
			.endProperty
			.property TransitionFight ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::TransitionFight_var
			.endProperty
			.property SelfLoathing Faction auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::SelfLoathing_var
			.endProperty
			.property Combatant10 ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Combatant10_var
			.endProperty
			.property Gate2 ObjectReference auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Gate2_var
			.endProperty
			.property Fight12 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight12_var
			.endProperty
			.property Wave4Keyword Keyword auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Wave4Keyword_var
			.endProperty
			.property Wave2Keyword Keyword auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Wave2Keyword_var
			.endProperty
			.property NextWagerFightIsEasyAnimals bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::NextWagerFightIsEasyAnimals_var
			.endProperty
			.property Gate3 ObjectReference auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Gate3_var
			.endProperty
			.property NextWagerFightIsExotic bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::NextWagerFightIsExotic_var
			.endProperty
			.property Level0Fights int auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Level0Fights_var
			.endProperty
			.property NumberOfPlayerFights int auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::NumberOfPlayerFights_var
			.endProperty
			.property NextWagerFight ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::NextWagerFight_var
			.endProperty
			.property Fight04 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight04_var
			.endProperty
			.property Combatant02 ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Combatant02_var
			.endProperty
			.property Combatant07 ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Combatant07_var
			.endProperty
			.property Fight01 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight01_var
			.endProperty
			.property PlayerChoseTheField bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::PlayerChoseTheField_var
			.endProperty
			.property Combatant09 ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Combatant09_var
			.endProperty
			.property Fight05 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight05_var
			.endProperty
			.property Combatant03 ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Combatant03_var
			.endProperty
			.property SpecialFightJail ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::SpecialFightJail_var
			.endProperty
			.property CurrentFight ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::CurrentFight_var
			.endProperty
			.property Wave1Keyword Keyword auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Wave1Keyword_var
			.endProperty
			.property Combatant08 ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Combatant08_var
			.endProperty
			.property RewardDue bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::RewardDue_var
			.endProperty
			.property TransitionCombatant ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::TransitionCombatant_var
			.endProperty
			.property Level3Fights int auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Level3Fights_var
			.endProperty
			.property Combatant06 ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Combatant06_var
			.endProperty
			.property WagerResolutionRequired bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::WagerResolutionRequired_var
			.endProperty
			.property Fight11 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight11_var
			.endProperty
			.property Combatant05 ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Combatant05_var
			.endProperty
			.property Fight03 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight03_var
			.endProperty
			.property Fight10 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight10_var
			.endProperty
			.property Fight09 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight09_var
			.endProperty
			.property PacifyFaction Faction auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::PacifyFaction_var
			.endProperty
			.property Level2Fights int auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Level2Fights_var
			.endProperty
			.property Fight06 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight06_var
			.endProperty
			.property NextWagerFightIsToughAnimals bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::NextWagerFightIsToughAnimals_var
			.endProperty
			.property Combatant04 ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Combatant04_var
			.endProperty
			.property Fight08 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight08_var
			.endProperty
			.property ArenaWagerFighterQuest Quest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::ArenaWagerFighterQuest_var
			.endProperty
			.property LoanerSword Weapon auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::LoanerSword_var
			.endProperty
			.property PlayerWonWager bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::PlayerWonWager_var
			.endProperty
			.property Wave5Keyword Keyword auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Wave5Keyword_var
			.endProperty
			.property PlayerGotTheSkinny bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::PlayerGotTheSkinny_var
			.endProperty
			.property Fight02 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight02_var
			.endProperty
			.property Level1Fights int auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Level1Fights_var
			.endProperty
			.property DBFightWentAwry bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::DBFightWentAwry_var
			.endProperty
			.property Wave3Keyword Keyword auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Wave3Keyword_var
			.endProperty
			.property ArrestOffset int auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::ArrestOffset_var
			.endProperty
			.property CombatPreSet bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::CombatPreSet_var
			.endProperty
			.property Gold MiscObject auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Gold_var
			.endProperty
			.property WagerOngoing bool auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::WagerOngoing_var
			.endProperty
			.property FightsToNextLevel int auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::FightsToNextLevel_var
			.endProperty
			.property Fight07 ArenaCombatQuest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Fight07_var
			.endProperty
			.property Combatant01 ReferenceAlias auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::Combatant01_var
			.endProperty
			.property PointerQuest Quest auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::PointerQuest_var
			.endProperty
			.property LinkedDoorKeyword Keyword auto
				.userFlags 0 ;none
				.docString ""
				.autovar ::LinkedDoorKeyword_var
			.endProperty
		.endPropertyTable
		.stateTable
			.state 
				.function RegisterCombatant
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
						.param fighter ObjectReference
					.endParamTable
					.localTable
						.local ::temp76 actor
						.local ::nonevar NONE
						.local ::temp77 arenacombatquest
						.local ::temp78 bool
						.local ::temp79 bool
					.endLocalTable
					.code
						; line 528
						cast ::temp76 fighter 
						callmethod AddToFaction ::temp76 ::nonevar ::PacifyFaction_var ;1 variable args
						; line 530
						cast ::temp77 none 
						cmp_eq ::temp78 ::CurrentFight_var ::temp77 
						not ::temp78 ::temp78 
						cast ::temp78 ::temp78 
						jmpf ::temp78 _label0
						cast ::temp77 ::CurrentFight_var 
						propget IsTransitionFight ::temp77 ::temp79 
						cast ::temp78 ::temp79 
					_label0:
						jmpf ::temp78 _label1
						; line 531
						callmethod RegisterTransitionCombatant self ::nonevar fighter ;1 variable args
						; line 532
						return none 
						jmp _label1
						; line 535
					_label1:
						callmethod ForceRefIfEmpty ::Combatant01_var ::temp79 fighter ;1 variable args
						jmpf ::temp79 _label2
						jmp _label3
						; line 537
					_label2:
						callmethod ForceRefIfEmpty ::Combatant02_var ::temp78 fighter ;1 variable args
						jmpf ::temp78 _label4
						jmp _label3
						; line 539
					_label4:
						callmethod ForceRefIfEmpty ::Combatant03_var ::temp78 fighter ;1 variable args
						jmpf ::temp78 _label5
						jmp _label3
						; line 541
					_label5:
						callmethod ForceRefIfEmpty ::Combatant04_var ::temp78 fighter ;1 variable args
						jmpf ::temp78 _label6
						jmp _label3
						; line 543
					_label6:
						callmethod ForceRefIfEmpty ::Combatant05_var ::temp78 fighter ;1 variable args
						jmpf ::temp78 _label7
						jmp _label3
						; line 545
					_label7:
						callmethod ForceRefIfEmpty ::Combatant06_var ::temp78 fighter ;1 variable args
						jmpf ::temp78 _label8
						jmp _label3
						; line 547
					_label8:
						callmethod ForceRefIfEmpty ::Combatant07_var ::temp78 fighter ;1 variable args
						jmpf ::temp78 _label9
						jmp _label3
						; line 549
					_label9:
						callmethod ForceRefIfEmpty ::Combatant08_var ::temp78 fighter ;1 variable args
						jmpf ::temp78 _label10
						jmp _label3
						; line 551
					_label10:
						callmethod ForceRefIfEmpty ::Combatant09_var ::temp78 fighter ;1 variable args
						jmpf ::temp78 _label11
						jmp _label3
						; line 553
					_label11:
						callmethod ForceRefIfEmpty ::Combatant10_var ::temp78 fighter ;1 variable args
						jmpf ::temp78 _label3
						jmp _label3
					_label3
					.endCode
				.endFunction ;RegisterCombatant
				.function Promote
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
						.local ::temp26 actor
						.local ::nonevar NONE
						.local ::temp27 int
						.local ::temp28 bool
						.local ::temp29 bool
						.local rank int
					.endLocalTable
					.code
						; line 310
						callstatic game GetPlayer ::temp26 ;0 variable args
						callmethod ModFactionRank ::temp26 ::nonevar ::ArenaFaction_var 1 ;2 variable args
						; line 311
						callstatic game GetPlayer ::temp26 ;0 variable args
						callmethod GetFactionRank ::temp26 ::temp27 ::ArenaFaction_var ;1 variable args
						assign rank ::temp27 
						; line 312
						cmp_eq ::temp28 rank 1 
						jmpf ::temp28 _label0
						; line 313
						assign ::FightsToNextLevel_var ::Level1Fights_var 
						jmp _label1
						; line 314
					_label0:
						cmp_eq ::temp29 rank 2 
						jmpf ::temp29 _label2
						; line 315
						assign ::FightsToNextLevel_var ::Level2Fights_var 
						jmp _label1
						; line 316
					_label2:
						cmp_eq ::temp29 rank 3 
						jmpf ::temp29 _label3
						; line 317
						assign ::FightsToNextLevel_var ::Level3Fights_var 
						jmp _label1
						; line 318
					_label3:
						cmp_eq ::temp29 rank 4 
						jmpf ::temp29 _label1
						; line 319
						assign ::FightsToNextLevel_var 2147483647 
						jmp _label1
					_label1
					.endCode
				.endFunction ;Promote
				.function RegisterTransitionCombatant
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
						.param fighter ObjectReference
					.endParamTable
					.localTable
						.local ::temp57 ObjectReference
						.local ::temp58 ObjectReference
						.local ::temp59 bool
						.local ::nonevar NONE
						.local ::temp60 actor
					.endLocalTable
					.code
						; line 466
						callmethod GetReference ::TransitionCombatant_var ::temp57 ;0 variable args
						cast ::temp58 none 
						cmp_eq ::temp59 ::temp57 ::temp58 
						not ::temp59 ::temp59 
						jmpf ::temp59 _label0
						; line 468
						return none 
						jmp _label0
						; line 471
					_label0:
						callmethod ForceRefTo ::TransitionCombatant_var ::nonevar fighter ;1 variable args
						; line 472
						callmethod GetActorReference ::TransitionCombatant_var ::temp60 ;0 variable args
						callmethod SetNoBleedoutRecovery ::temp60 ::nonevar true ;1 variable args
					.endCode
				.endFunction ;RegisterTransitionCombatant
				.function EndWagerFight
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
						.local ::temp14 arenawagerfighterquestscript
						.local ::temp15 referencealias
						.local ::temp16 actor
						.local ::temp17 bool
						.local ::nonevar NONE
						.local fieldWon bool
					.endLocalTable
					.code
						; line 225
						cast ::temp14 ::ArenaWagerFighterQuest_var 
						propget fighter ::temp14 ::temp15 
						callmethod GetActorReference ::temp15 ::temp16 ;0 variable args
						callmethod IsDead ::temp16 ::temp17 ;0 variable args
						assign fieldWon ::temp17 
						; line 226
						callmethod Stop ::NextWagerFight_var ::nonevar ;0 variable args
						; line 228
						cmp_eq ::temp17 ::PlayerChoseTheField_var fieldWon 
						jmpf ::temp17 _label0
						; line 229
						assign ::PlayerWonWager_var true 
						jmp _label1
						; line 232
					_label0:
						assign ::PlayerWonWager_var false 
						; line 236
					_label1:
						assign ::WagerResolutionRequired_var true 
					.endCode
				.endFunction ;EndWagerFight
				.function GotoState
					 ; function type 0
					.userFlags 0 ;none
					.docString "Function that switches this object to the specified state"
					.return NONE
					.paramTable
						.param newState String
					.endParamTable
					.localTable
						.local ::nonevar NONE
					.endLocalTable
					.code
						callmethod onEndState self ::nonevar ;0 variable args
						assign ::state newState 
						callmethod onBeginState self ::nonevar ;0 variable args
					.endCode
				.endFunction ;GotoState
				.function GetKeywordForWave
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return keyword
					.paramTable
						.param wave int
					.endParamTable
					.localTable
						.local ::temp61 bool
						.local ::temp62 bool
						.local ::temp63 keyword
					.endLocalTable
					.code
						; line 476
						cmp_eq ::temp61 wave 1 
						jmpf ::temp61 _label0
						; line 477
						return ::Wave1Keyword_var 
						jmp _label1
						; line 478
					_label0:
						cmp_eq ::temp62 wave 2 
						jmpf ::temp62 _label2
						; line 479
						return ::Wave2Keyword_var 
						jmp _label1
						; line 480
					_label2:
						cmp_eq ::temp62 wave 3 
						jmpf ::temp62 _label3
						; line 481
						return ::Wave3Keyword_var 
						jmp _label1
						; line 482
					_label3:
						cmp_eq ::temp62 wave 4 
						jmpf ::temp62 _label4
						; line 483
						return ::Wave4Keyword_var 
						jmp _label1
						; line 484
					_label4:
						cmp_eq ::temp62 wave 5 
						jmpf ::temp62 _label5
						; line 485
						return ::Wave5Keyword_var 
						jmp _label1
						; line 487
					_label5:
						cast ::temp63 none 
						return ::temp63 
					_label1
					.endCode
				.endFunction ;GetKeywordForWave
				.function PlayerJoin
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
						.local ::temp9 bool
						.local ::temp11 actor
						.local ::nonevar NONE
						.local ::temp10 bool
					.endLocalTable
					.code
						; line 209
						callmethod IsRunning ::PointerQuest_var ::temp9 ;0 variable args
						jmpf ::temp9 _label0
						; line 210
						callmethod SetStage ::PointerQuest_var ::temp10 20 ;1 variable args
						jmp _label0
						; line 212
					_label0:
						callstatic game GetPlayer ::temp11 ;0 variable args
						callmethod AddToFaction ::temp11 ::nonevar ::ArenaFaction_var ;1 variable args
						; line 213
						assign ::NumberOfPlayerFights_var 0 
						; line 214
						assign ::FightsToNextLevel_var ::Level0Fights_var 
					.endCode
				.endFunction ;PlayerJoin
				.function PlayerAvoidedWager
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
					.endLocalTable
					.code
						; line 253
						assign ::PlayerChoseTheField_var false 
						; line 254
						assign ::WagerOngoing_var false 
					.endCode
				.endFunction ;PlayerAvoidedWager
				.function CombatOver
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
						.local ::temp49 ObjectReference
						.local ::temp50 int
						.local ::nonevar NONE
					.endLocalTable
					.code
						; line 426
						jmpf ::WagerOngoing_var _label0
						; line 427
						callmethod EndWagerFight self ::nonevar ;0 variable args
						; line 428
						return none 
						jmp _label0
						; line 430
					_label0:
						callmethod Stop ::CurrentFight_var ::nonevar ;0 variable args
						; line 431
						callmethod GetReference ::PitDoor_var ::temp49 ;0 variable args
						callmethod Lock ::temp49 ::nonevar false false ;2 variable args
						; line 432
						assign ::CombatOngoing_var false 
						; line 433
						assign ::RewardDue_var true 
						; line 434
						iadd ::temp50 ::NumberOfPlayerFights_var 1 
						assign ::NumberOfPlayerFights_var ::temp50 
					.endCode
				.endFunction ;CombatOver
				.function ResolveWager
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
						.local ::temp18 actor
						.local ::temp19 int
						.local ::temp20 form
						.local ::nonevar NONE
					.endLocalTable
					.code
						; line 241
						jmpf ::PlayerWonWager_var _label0
						; line 242
						callstatic game GetPlayer ::temp18 ;0 variable args
						imul ::temp19 ::WagerAmount_var 2 
						cast ::temp20 ::Gold_var 
						callmethod AddItem ::temp18 ::nonevar ::temp20 ::temp19 false ;3 variable args
						jmp _label0
						; line 245
					_label0:
						callmethod CleanupBodies self ::nonevar ;0 variable args
						; line 246
						assign ::WagerOngoing_var false 
						; line 247
						assign ::WagerResolutionRequired_var false 
						; line 248
						callmethod Stop ::ArenaWagerFighterQuest_var ::nonevar ;0 variable args
						; line 249
						callmethod PickNextWagerFight self ::nonevar ::NextWagerFight_var ;1 variable args
					.endCode
				.endFunction ;ResolveWager
				.function StartWagerFight
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
						.local ::temp21 bool
					.endLocalTable
					.code
						; line 258
						callmethod Start ::NextWagerFight_var ::temp21 ;0 variable args
						; line 259
						callmethod Start ::ArenaWagerFighterQuest_var ::temp21 ;0 variable args
						; line 260
						assign ::CombatPreSet_var true 
					.endCode
				.endFunction ;StartWagerFight
				.function StartCombat
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
						.local ::temp30 int
						.local ::temp31 bool
						.local ::temp32 bool
						.local ::temp35 bool
						.local ::temp37 ObjectReference
						.local ::temp33 actor
						.local ::temp34 form
						.local ::nonevar NONE
						.local ::temp36 arenacombatquest
					.endLocalTable
					.code
						; line 325
						callmethod GetStage ::DB03_var ::temp30 ;0 variable args
						cmp_lte ::temp31 20 ::temp30 
						cast ::temp31 ::temp31 
						jmpf ::temp31 _label0
						callmethod GetStage ::DB03_var ::temp30 ;0 variable args
						cmp_gt ::temp32 40 ::temp30 
						cast ::temp31 ::temp32 
					_label0:
						jmpf ::temp31 _label1
						; line 326
						assign ::CurrentFight_var ::SpecialFightDB_var 
						; line 327
						callstatic game GetPlayer ::temp33 ;0 variable args
						cast ::temp34 ::LoanerSword_var 
						callmethod GetItemCount ::temp33 ::temp30 ::temp34 ;1 variable args
						cmp_lt ::temp32 ::temp30 1 
						jmpf ::temp32 _label2
						; line 328
						callstatic game GetPlayer ::temp33 ;0 variable args
						cast ::temp34 ::LoanerSword_var 
						callmethod AddItem ::temp33 ::nonevar ::temp34 1 false ;3 variable args
						jmp _label2
						; line 330
					_label2:
						callstatic game GetPlayer ::temp33 ;0 variable args
						cast ::temp34 ::LoanerShield_var 
						callmethod GetItemCount ::temp33 ::temp30 ::temp34 ;1 variable args
						cmp_lt ::temp32 ::temp30 1 
						jmpf ::temp32 _label3
						; line 331
						callstatic game GetPlayer ::temp33 ;0 variable args
						cast ::temp34 ::LoanerShield_var 
						callmethod AddItem ::temp33 ::nonevar ::temp34 1 false ;3 variable args
						jmp _label3
						; line 333
					_label3:
						callstatic game GetPlayer ::temp33 ;0 variable args
						cast ::temp34 ::LoanerSword_var 
						callmethod EquipItem ::temp33 ::nonevar ::temp34 false false ;3 variable args
						; line 334
						callstatic game GetPlayer ::temp33 ;0 variable args
						cast ::temp34 ::LoanerShield_var 
						callmethod EquipItem ::temp33 ::nonevar ::temp34 false false ;3 variable args
						jmp _label4
						; line 335
					_label1:
						callmethod GetStage ::EastmarchJail_var ::temp30 ;0 variable args
						cmp_eq ::temp32 20 ::temp30 
						cast ::temp32 ::temp32 
						jmpf ::temp32 _label5
						callmethod IsRunning ::EastmarchJail_var ::temp35 ;0 variable args
						cast ::temp32 ::temp35 
					_label5:
						jmpf ::temp32 _label6
						; line 337
						assign ::CurrentFight_var ::SpecialFightJail_var 
						; line 338
						callstatic game GetPlayer ::temp33 ;0 variable args
						cast ::temp34 ::LoanerSword_var 
						callmethod AddItem ::temp33 ::nonevar ::temp34 1 false ;3 variable args
						; line 339
						callstatic game GetPlayer ::temp33 ;0 variable args
						cast ::temp34 ::LoanerShield_var 
						callmethod AddItem ::temp33 ::nonevar ::temp34 1 false ;3 variable args
						; line 340
						callstatic game GetPlayer ::temp33 ;0 variable args
						cast ::temp34 ::LoanerSword_var 
						callmethod EquipItem ::temp33 ::nonevar ::temp34 false false ;3 variable args
						; line 341
						callstatic game GetPlayer ::temp33 ;0 variable args
						cast ::temp34 ::LoanerShield_var 
						callmethod EquipItem ::temp33 ::nonevar ::temp34 false false ;3 variable args
						jmp _label4
						; line 343
					_label6:
						callmethod PickNextFight self ::temp36 0 ;1 variable args
						assign ::CurrentFight_var ::temp36 
						; line 346
					_label4:
						callmethod Start ::CurrentFight_var ::temp35 ;0 variable args
						; line 347
						assign ::CombatPreSet_var true 
						; line 348
						callmethod GetReference ::PitDoor_var ::temp37 ;0 variable args
						callmethod Lock ::temp37 ::nonevar false false ;2 variable args
						; line 349
						assign ::CombatOngoing_var true 
					.endCode
				.endFunction ;StartCombat
				.function GetFightQuestFromIndex
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return arenacombatquest
					.paramTable
						.param questIndex int
					.endParamTable
					.localTable
						.local ::temp0 bool
						.local ::temp1 bool
						.local ::temp2 arenacombatquest
					.endLocalTable
					.code
						; line 113
						cmp_eq ::temp0 questIndex 1 
						jmpf ::temp0 _label0
						; line 114
						return ::Fight01_var 
						jmp _label1
						; line 115
					_label0:
						cmp_eq ::temp1 questIndex 2 
						jmpf ::temp1 _label2
						; line 116
						return ::Fight02_var 
						jmp _label1
						; line 117
					_label2:
						cmp_eq ::temp1 questIndex 3 
						jmpf ::temp1 _label3
						; line 118
						return ::Fight03_var 
						jmp _label1
						; line 119
					_label3:
						cmp_eq ::temp1 questIndex 4 
						jmpf ::temp1 _label4
						; line 120
						return ::Fight04_var 
						jmp _label1
						; line 121
					_label4:
						cmp_eq ::temp1 questIndex 5 
						jmpf ::temp1 _label5
						; line 122
						return ::Fight05_var 
						jmp _label1
						; line 123
					_label5:
						cmp_eq ::temp1 questIndex 6 
						jmpf ::temp1 _label6
						; line 124
						return ::Fight06_var 
						jmp _label1
						; line 125
					_label6:
						cmp_eq ::temp1 questIndex 7 
						jmpf ::temp1 _label7
						; line 126
						return ::Fight07_var 
						jmp _label1
						; line 127
					_label7:
						cmp_eq ::temp1 questIndex 8 
						jmpf ::temp1 _label8
						; line 128
						return ::Fight08_var 
						jmp _label1
						; line 129
					_label8:
						cmp_eq ::temp1 questIndex 9 
						jmpf ::temp1 _label9
						; line 130
						return ::Fight09_var 
						jmp _label1
						; line 131
					_label9:
						cmp_eq ::temp1 questIndex 10 
						jmpf ::temp1 _label10
						; line 132
						return ::Fight10_var 
						jmp _label1
						; line 133
					_label10:
						cmp_eq ::temp1 questIndex 11 
						jmpf ::temp1 _label11
						; line 134
						return ::Fight11_var 
						jmp _label1
						; line 135
					_label11:
						cmp_eq ::temp1 questIndex 12 
						jmpf ::temp1 _label12
						; line 136
						return ::Fight12_var 
						jmp _label1
						; line 137
					_label12:
						cmp_eq ::temp1 questIndex 13 
						jmpf ::temp1 _label13
						; line 138
						return ::Fight13_var 
						jmp _label1
						; line 140
					_label13:
						cast ::temp2 none 
						return ::temp2 
					_label1
					.endCode
				.endFunction ;GetFightQuestFromIndex
				.function CleanupBodies
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
						.local ::temp80 bool
						.local ::temp81 ObjectReference
						.local ::temp82 ObjectReference
						.local ::temp83 actor
						.local ::nonevar NONE
						.local ref actor
					.endLocalTable
					.code
						; line 562
						callmethod _CleanupBody self ::temp80 ::Combatant01_var ;1 variable args
						jmpf ::temp80 _label0
						jmp _label0
						; line 565
					_label0:
						callmethod _CleanupBody self ::temp80 ::Combatant02_var ;1 variable args
						jmpf ::temp80 _label1
						jmp _label1
						; line 568
					_label1:
						callmethod _CleanupBody self ::temp80 ::Combatant03_var ;1 variable args
						jmpf ::temp80 _label2
						jmp _label2
						; line 571
					_label2:
						callmethod _CleanupBody self ::temp80 ::Combatant04_var ;1 variable args
						jmpf ::temp80 _label3
						jmp _label3
						; line 574
					_label3:
						callmethod _CleanupBody self ::temp80 ::Combatant05_var ;1 variable args
						jmpf ::temp80 _label4
						jmp _label4
						; line 577
					_label4:
						callmethod _CleanupBody self ::temp80 ::Combatant06_var ;1 variable args
						jmpf ::temp80 _label5
						jmp _label5
						; line 580
					_label5:
						callmethod _CleanupBody self ::temp80 ::Combatant07_var ;1 variable args
						jmpf ::temp80 _label6
						jmp _label6
						; line 583
					_label6:
						callmethod _CleanupBody self ::temp80 ::Combatant08_var ;1 variable args
						jmpf ::temp80 _label7
						jmp _label7
						; line 586
					_label7:
						callmethod _CleanupBody self ::temp80 ::Combatant09_var ;1 variable args
						jmpf ::temp80 _label8
						jmp _label8
						; line 589
					_label8:
						callmethod _CleanupBody self ::temp80 ::Combatant10_var ;1 variable args
						jmpf ::temp80 _label9
						jmp _label9
						; line 594
					_label9:
						callmethod GetReference ::TransitionCombatant_var ::temp81 ;0 variable args
						cast ::temp82 none 
						cmp_eq ::temp80 ::temp81 ::temp82 
						not ::temp80 ::temp80 
						jmpf ::temp80 _label10
						; line 596
						callmethod GetActorReference ::TransitionCombatant_var ::temp83 ;0 variable args
						assign ref ::temp83 
						; line 597
						callstatic game GetPlayer ::temp83 ;0 variable args
						callmethod RemoveFromFaction ::temp83 ::nonevar ::SelfLoathing_var ;1 variable args
						; line 598
						callmethod RemoveFromFaction ref ::nonevar ::SelfLoathing_var ;1 variable args
						; line 599
						callmethod SetFactionRank ref ::nonevar ::ArenaFaction_var 4 ;2 variable args
						; line 600
						callmethod SetNoBleedoutRecovery ref ::nonevar false ;1 variable args
						; line 601
						callmethod Clear ::TransitionCombatant_var ::nonevar ;0 variable args
						jmp _label10
						; line 605
					_label10:
						cast ::temp82 none 
						assign _spawnPoint01 ::temp82 
						; line 606
						cast ::temp81 none 
						assign _spawnPoint02 ::temp81 
						; line 607
						cast ::temp82 none 
						assign _spawnPoint03 ::temp82 
						; line 608
						cast ::temp81 none 
						assign _spawnPoint04 ::temp81 
						; line 609
						cast ::temp82 none 
						assign _spawnPoint05 ::temp82 
						; line 612
						callmethod SetOpen ::Gate1_var ::nonevar false ;1 variable args
						; line 613
						callmethod SetOpen ::Gate2_var ::nonevar false ;1 variable args
						; line 614
						callmethod SetOpen ::Gate3_var ::nonevar false ;1 variable args
					.endCode
				.endFunction ;CleanupBodies
				.function _CleanupBody
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return bool
					.paramTable
						.param combatant referencealias
					.endParamTable
					.localTable
						.local ::temp84 ObjectReference
						.local ::temp85 ObjectReference
						.local ::temp86 bool
						.local ::temp87 actor
						.local ::nonevar NONE
						.local ref actor
						.local ::temp88 bool
					.endLocalTable
					.code
						; line 618
						callmethod GetReference combatant ::temp84 ;0 variable args
						cast ::temp85 none 
						cmp_eq ::temp86 ::temp84 ::temp85 
						not ::temp86 ::temp86 
						jmpf ::temp86 _label0
						; line 619
						callmethod GetActorReference combatant ::temp87 ;0 variable args
						assign ref ::temp87 
						; line 620
						callmethod Clear combatant ::nonevar ;0 variable args
						; line 622
						jmpf ::WagerOngoing_var _label1
						; line 624
						callmethod Delete ref ::nonevar ;0 variable args
						jmp _label2
						; line 627
					_label1:
						callmethod IsDead ref ::temp88 ;0 variable args
						jmpf ::temp88 _label3
						; line 628
						callmethod Delete ref ::nonevar ;0 variable args
						jmp _label2
						; line 630
					_label3:
						callmethod MoveToMyEditorLocation ref ::nonevar ;0 variable args
						; line 631
						callmethod ResetHealthAndLimbs ref ::nonevar ;0 variable args
						; line 634
					_label2:
						return true 
						jmp _label4
						; line 636
					_label0:
						return false 
					_label4
					.endCode
				.endFunction ;_CleanupBody
				.function Reward
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
						.local ::temp51 ObjectReference
						.local ::nonevar NONE
						.local ::temp52 int
						.local ::temp53 bool
						.local ::temp54 bool
						.local ::temp55 actor
						.local ::temp56 form
					.endLocalTable
					.code
						; line 438
						callmethod GetReference ::PitDoor_var ::temp51 ;0 variable args
						callmethod Lock ::temp51 ::nonevar true false ;2 variable args
						; line 439
						callmethod CleanupBodies self ::nonevar ;0 variable args
						; line 441
						callmethod GetStage ::EastmarchJail_var ::temp52 ;0 variable args
						cmp_eq ::temp53 20 ::temp52 
						cast ::temp53 ::temp53 
						jmpf ::temp53 _label0
						callmethod IsRunning ::EastmarchJail_var ::temp54 ;0 variable args
						cast ::temp53 ::temp54 
					_label0:
						jmpf ::temp53 _label1
						; line 443
						callstatic game GetPlayer ::temp55 ;0 variable args
						cast ::temp56 ::LoanerSword_var 
						callmethod UnequipItem ::temp55 ::nonevar ::temp56 false false ;3 variable args
						; line 444
						callstatic game GetPlayer ::temp55 ;0 variable args
						cast ::temp56 ::LoanerShield_var 
						callmethod UnequipItem ::temp55 ::nonevar ::temp56 false false ;3 variable args
						; line 445
						callstatic game GetPlayer ::temp55 ;0 variable args
						cast ::temp56 ::LoanerSword_var 
						callmethod RemoveItem ::temp55 ::nonevar ::temp56 1 false none ;4 variable args
						; line 446
						callstatic game GetPlayer ::temp55 ;0 variable args
						cast ::temp56 ::LoanerShield_var 
						callmethod RemoveItem ::temp55 ::nonevar ::temp56 1 false none ;4 variable args
						; line 447
						callmethod SetCrimeGold ::EastmarchCrimeFaction_var ::nonevar 0 ;1 variable args
						; line 448
						callmethod SetCrimeGoldViolent ::EastmarchCrimeFaction_var ::nonevar 0 ;1 variable args
						; line 450
						callmethod SetStage ::EastmarchJail_var ::temp54 200 ;1 variable args
						jmp _label2
						; line 451
					_label1:
						callstatic game GetPlayer ::temp55 ;0 variable args
						callmethod GetFactionRank ::temp55 ::temp52 ::ArenaFaction_var ;1 variable args
						comp_gte ::temp54 ::temp52 4 
						jmpf ::temp54 _label3
						; line 453
						callstatic game GetPlayer ::temp55 ;0 variable args
						cast ::temp56 ::Gold_var 
						callmethod AddItem ::temp55 ::nonevar ::temp56 100 false ;3 variable args
						jmp _label2
						; line 454
					_label3:
						cmp_lte ::temp54 ::FightsToNextLevel_var 0 
						jmpf ::temp54 _label4
						; line 456
						callmethod Promote self ::nonevar ;0 variable args
						jmp _label2
						; line 459
					_label4:
						callstatic game GetPlayer ::temp55 ;0 variable args
						cast ::temp56 ::Gold_var 
						callmethod AddItem ::temp55 ::nonevar ::temp56 100 false ;3 variable args
						; line 460
						isub ::temp52 ::FightsToNextLevel_var 1 
						assign ::FightsToNextLevel_var ::temp52 
						; line 462
					_label2:
						assign ::RewardDue_var false 
					.endCode
				.endFunction ;Reward
				.function PlaceBet
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
						.param amount int
					.endParamTable
					.localTable
						.local ::temp12 actor
						.local ::temp13 form
						.local ::nonevar NONE
					.endLocalTable
					.code
						; line 218
						assign ::WagerOngoing_var true 
						; line 219
						assign ::WagerAmount_var amount 
						; line 220
						callstatic game GetPlayer ::temp12 ;0 variable args
						cast ::temp13 ::Gold_var 
						callmethod RemoveItem ::temp12 ::nonevar ::temp13 ::WagerAmount_var false none ;4 variable args
					.endCode
				.endFunction ;PlaceBet
				.function RegisterSpawnPoint
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
						.param spawnMarker ObjectReference
					.endParamTable
					.localTable
						.local ::temp73 ObjectReference
						.local ::temp74 bool
						.local ::temp75 bool
					.endLocalTable
					.code
						; line 511
						cast ::temp73 none 
						cmp_eq ::temp74 _spawnPoint01 ::temp73 
						jmpf ::temp74 _label0
						; line 512
						assign _spawnPoint01 spawnMarker 
						jmp _label1
						; line 513
					_label0:
						cast ::temp73 none 
						cmp_eq ::temp75 _spawnPoint02 ::temp73 
						jmpf ::temp75 _label2
						; line 514
						assign _spawnPoint02 spawnMarker 
						jmp _label1
						; line 515
					_label2:
						cast ::temp73 none 
						cmp_eq ::temp75 _spawnPoint03 ::temp73 
						jmpf ::temp75 _label3
						; line 516
						assign _spawnPoint03 spawnMarker 
						jmp _label1
						; line 517
					_label3:
						cast ::temp73 none 
						cmp_eq ::temp75 _spawnPoint04 ::temp73 
						jmpf ::temp75 _label4
						; line 518
						assign _spawnPoint04 spawnMarker 
						jmp _label1
						; line 519
					_label4:
						cast ::temp73 none 
						cmp_eq ::temp75 _spawnPoint05 ::temp73 
						jmpf ::temp75 _label1
						; line 520
						assign _spawnPoint05 spawnMarker 
						jmp _label1
					_label1
					.endCode
				.endFunction ;RegisterSpawnPoint
				.function GetIndexFromFightQuest
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return int
					.paramTable
						.param rQuest arenacombatquest
					.endParamTable
					.localTable
						.local ::temp3 bool
						.local ::temp4 bool
					.endLocalTable
					.code
						; line 145
						cmp_eq ::temp3 rQuest ::Fight01_var 
						jmpf ::temp3 _label0
						; line 146
						return 1 
						jmp _label1
						; line 147
					_label0:
						cmp_eq ::temp4 rQuest ::Fight02_var 
						jmpf ::temp4 _label2
						; line 148
						return 2 
						jmp _label1
						; line 149
					_label2:
						cmp_eq ::temp4 rQuest ::Fight03_var 
						jmpf ::temp4 _label3
						; line 150
						return 3 
						jmp _label1
						; line 151
					_label3:
						cmp_eq ::temp4 rQuest ::Fight04_var 
						jmpf ::temp4 _label4
						; line 152
						return 4 
						jmp _label1
						; line 153
					_label4:
						cmp_eq ::temp4 rQuest ::Fight05_var 
						jmpf ::temp4 _label5
						; line 154
						return 5 
						jmp _label1
						; line 155
					_label5:
						cmp_eq ::temp4 rQuest ::Fight06_var 
						jmpf ::temp4 _label6
						; line 156
						return 6 
						jmp _label1
						; line 157
					_label6:
						cmp_eq ::temp4 rQuest ::Fight07_var 
						jmpf ::temp4 _label7
						; line 158
						return 7 
						jmp _label1
						; line 159
					_label7:
						cmp_eq ::temp4 rQuest ::Fight08_var 
						jmpf ::temp4 _label8
						; line 160
						return 8 
						jmp _label1
						; line 161
					_label8:
						cmp_eq ::temp4 rQuest ::Fight09_var 
						jmpf ::temp4 _label9
						; line 162
						return 9 
						jmp _label1
						; line 163
					_label9:
						cmp_eq ::temp4 rQuest ::Fight10_var 
						jmpf ::temp4 _label10
						; line 164
						return 10 
						jmp _label1
						; line 165
					_label10:
						cmp_eq ::temp4 rQuest ::Fight11_var 
						jmpf ::temp4 _label11
						; line 166
						return 11 
						jmp _label1
						; line 167
					_label11:
						cmp_eq ::temp4 rQuest ::Fight12_var 
						jmpf ::temp4 _label12
						; line 168
						return 12 
						jmp _label1
						; line 169
					_label12:
						cmp_eq ::temp4 rQuest ::Fight13_var 
						jmpf ::temp4 _label13
						; line 170
						return 13 
						jmp _label1
						; line 172
					_label13:
						return 0 
					_label1
					.endCode
				.endFunction ;GetIndexFromFightQuest
				.function GetDoorForWave
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return ObjectReference
					.paramTable
						.param wave int
					.endParamTable
					.localTable
						.local ::temp64 keyword
						.local ::temp65 bool
						.local ::temp67 bool
						.local toMatch keyword
						.local ::temp66 ObjectReference
						.local ::temp68 ObjectReference
						.local ::temp69 ObjectReference
						.local ::temp70 ObjectReference
						.local ::temp71 ObjectReference
						.local ::temp72 ObjectReference
					.endLocalTable
					.code
						; line 492
						callmethod GetKeywordForWave self ::temp64 wave ;1 variable args
						assign toMatch ::temp64 
						; line 494
						callmethod HasKeyword _spawnPoint01 ::temp65 toMatch ;1 variable args
						jmpf ::temp65 _label0
						; line 495
						callmethod GetLinkedRef _spawnPoint01 ::temp66 ::LinkedDoorKeyword_var ;1 variable args
						return ::temp66 
						jmp _label1
						; line 496
					_label0:
						callmethod HasKeyword _spawnPoint02 ::temp67 toMatch ;1 variable args
						jmpf ::temp67 _label2
						; line 497
						callmethod GetLinkedRef _spawnPoint02 ::temp68 ::LinkedDoorKeyword_var ;1 variable args
						return ::temp68 
						jmp _label1
						; line 498
					_label2:
						callmethod HasKeyword _spawnPoint03 ::temp67 toMatch ;1 variable args
						jmpf ::temp67 _label3
						; line 499
						callmethod GetLinkedRef _spawnPoint03 ::temp69 ::LinkedDoorKeyword_var ;1 variable args
						return ::temp69 
						jmp _label1
						; line 500
					_label3:
						callmethod HasKeyword _spawnPoint04 ::temp67 toMatch ;1 variable args
						jmpf ::temp67 _label4
						; line 501
						callmethod GetLinkedRef _spawnPoint04 ::temp70 ::LinkedDoorKeyword_var ;1 variable args
						return ::temp70 
						jmp _label1
						; line 502
					_label4:
						callmethod HasKeyword _spawnPoint05 ::temp67 toMatch ;1 variable args
						jmpf ::temp67 _label5
						; line 503
						callmethod GetLinkedRef _spawnPoint05 ::temp71 ::LinkedDoorKeyword_var ;1 variable args
						return ::temp71 
						jmp _label1
						; line 505
					_label5:
						cast ::temp72 none 
						return ::temp72 
					_label1
					.endCode
				.endFunction ;GetDoorForWave
				.function PickNextWagerFight
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
						.param lastFight arenacombatquest
					.endParamTable
					.localTable
						.local ::temp22 arenacombatquest
						.local ::temp23 bool
						.local ::temp25 bool
						.local lastFightIndex int
						.local ::temp24 int
						.local fightIndex int
					.endLocalTable
					.code
						; line 264
						assign lastFightIndex -1 
						; line 265
						cast ::temp22 none 
						cmp_eq ::temp23 lastFight ::temp22 
						not ::temp23 ::temp23 
						jmpf ::temp23 _label0
						; line 266
						callmethod GetIndexFromFightQuest self ::temp24 lastFight ;1 variable args
						assign lastFightIndex ::temp24 
						jmp _label0
						; line 268
					_label0:
						assign fightIndex lastFightIndex 
						; line 269
					_label2:
						cmp_eq ::temp23 fightIndex lastFightIndex 
						jmpf ::temp23 _label1
						; line 270
						callstatic utility RandomInt ::temp24 1 _maxFights ;2 variable args
						assign fightIndex ::temp24 
						jmp _label2
						; line 272
					_label1:
						callmethod GetFightQuestFromIndex self ::temp22 fightIndex ;1 variable args
						assign ::NextWagerFight_var ::temp22 
						; line 274
						assign ::NextWagerFightIsToughAnimals_var false 
						; line 275
						assign ::NextWagerFightIsEasyAnimals_var false 
						; line 276
						assign ::NextWagerFightIsPeople_var false 
						; line 277
						assign ::NextWagerFightIsExotic_var false 
						; line 279
						cmp_eq ::temp23 ::NextWagerFight_var ::Fight01_var 
						jmpf ::temp23 _label3
						; line 280
						assign ::NextWagerFightIsEasyAnimals_var true 
						jmp _label4
						; line 281
					_label3:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight02_var 
						jmpf ::temp25 _label5
						; line 282
						assign ::NextWagerFightIsEasyAnimals_var true 
						jmp _label4
						; line 283
					_label5:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight03_var 
						jmpf ::temp25 _label6
						; line 284
						assign ::NextWagerFightIsEasyAnimals_var true 
						jmp _label4
						; line 285
					_label6:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight04_var 
						jmpf ::temp25 _label7
						; line 286
						assign ::NextWagerFightIsPeople_var true 
						jmp _label4
						; line 287
					_label7:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight05_var 
						jmpf ::temp25 _label8
						; line 288
						assign ::NextWagerFightIsToughAnimals_var true 
						jmp _label4
						; line 289
					_label8:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight06_var 
						jmpf ::temp25 _label9
						; line 290
						assign ::NextWagerFightIsToughAnimals_var true 
						jmp _label4
						; line 291
					_label9:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight07_var 
						jmpf ::temp25 _label10
						; line 292
						assign ::NextWagerFightIsToughAnimals_var true 
						jmp _label4
						; line 293
					_label10:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight08_var 
						jmpf ::temp25 _label11
						; line 294
						assign ::NextWagerFightIsToughAnimals_var true 
						jmp _label4
						; line 295
					_label11:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight09_var 
						jmpf ::temp25 _label12
						; line 296
						assign ::NextWagerFightIsPeople_var true 
						jmp _label4
						; line 297
					_label12:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight10_var 
						jmpf ::temp25 _label13
						; line 298
						assign ::NextWagerFightIsExotic_var true 
						jmp _label4
						; line 299
					_label13:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight11_var 
						jmpf ::temp25 _label14
						; line 300
						assign ::NextWagerFightIsPeople_var true 
						jmp _label4
						; line 301
					_label14:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight12_var 
						jmpf ::temp25 _label15
						; line 302
						assign ::NextWagerFightIsExotic_var true 
						jmp _label4
						; line 303
					_label15:
						cmp_eq ::temp25 ::NextWagerFight_var ::Fight13_var 
						jmpf ::temp25 _label4
						; line 304
						assign ::NextWagerFightIsPeople_var true 
						jmp _label4
					_label4
					.endCode
				.endFunction ;PickNextWagerFight
				.function GetCombatantAlias
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return referencealias
					.paramTable
						.param index int
					.endParamTable
					.localTable
						.local ::temp5 bool
						.local ::temp6 bool
						.local ::temp7 referencealias
					.endLocalTable
					.code
						; line 177
						cmp_eq ::temp5 index 1 
						jmpf ::temp5 _label0
						; line 178
						return ::Combatant01_var 
						jmp _label1
						; line 179
					_label0:
						cmp_eq ::temp6 index 2 
						jmpf ::temp6 _label2
						; line 180
						return ::Combatant02_var 
						jmp _label1
						; line 181
					_label2:
						cmp_eq ::temp6 index 3 
						jmpf ::temp6 _label3
						; line 182
						return ::Combatant03_var 
						jmp _label1
						; line 183
					_label3:
						cmp_eq ::temp6 index 4 
						jmpf ::temp6 _label4
						; line 184
						return ::Combatant04_var 
						jmp _label1
						; line 185
					_label4:
						cmp_eq ::temp6 index 5 
						jmpf ::temp6 _label5
						; line 186
						return ::Combatant05_var 
						jmp _label1
						; line 187
					_label5:
						cmp_eq ::temp6 index 6 
						jmpf ::temp6 _label6
						; line 188
						return ::Combatant06_var 
						jmp _label1
						; line 189
					_label6:
						cmp_eq ::temp6 index 7 
						jmpf ::temp6 _label7
						; line 190
						return ::Combatant07_var 
						jmp _label1
						; line 191
					_label7:
						cmp_eq ::temp6 index 8 
						jmpf ::temp6 _label8
						; line 192
						return ::Combatant08_var 
						jmp _label1
						; line 193
					_label8:
						cmp_eq ::temp6 index 9 
						jmpf ::temp6 _label9
						; line 194
						return ::Combatant09_var 
						jmp _label1
						; line 195
					_label9:
						cmp_eq ::temp6 index 10 
						jmpf ::temp6 _label10
						; line 196
						return ::Combatant10_var 
						jmp _label1
						; line 198
					_label10:
						cast ::temp7 none 
						return ::temp7 
					_label1
					.endCode
				.endFunction ;GetCombatantAlias
				.function GetState
					 ; function type 0
					.userFlags 0 ;none
					.docString "Function that returns the current state"
					.return String
					.paramTable
					.endParamTable
					.localTable
					.endLocalTable
					.code
						return ::state 
					.endCode
				.endFunction ;GetState
				.function Setup
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return NONE
					.paramTable
					.endParamTable
					.localTable
						.local ::temp8 arenacombatquest
						.local ::nonevar NONE
					.endLocalTable
					.code
						; line 204
						assign ::WagerOngoing_var false 
						; line 205
						cast ::temp8 none 
						callmethod PickNextWagerFight self ::nonevar ::temp8 ;1 variable args
					.endCode
				.endFunction ;Setup
				.function PickNextFight
					 ; function type 0
					.userFlags 0 ;none
					.docString ""
					.return arenacombatquest
					.paramTable
						.param offset int
					.endParamTable
					.localTable
						.local ::temp38 actor
						.local ::temp39 int
						.local ::temp40 bool
						.local ::temp42 bool
						.local ::temp48 arenacombatquest
						.local minFight int
						.local maxFight int
						.local playerRank int
						.local ::temp41 arenacombatquest
						.local fightIndex int
						.local ::temp43 bool
						.local humanFight bool
						.local ::temp44 arenacombatquest
						.local ::mangled_fightindex_0 int
						.local ::temp45 arenacombatquest
						.local ::mangled_fightindex_1 int
						.local animalFight int
						.local ::temp46 bool
						.local ::temp47 arenacombatquest
						.local ::mangled_fightindex_2 int
						.local fightRoll int
					.endLocalTable
					.code
						; line 353
						assign minFight -1 
						; line 354
						assign maxFight -1 
						; line 355
						callstatic game GetPlayer ::temp38 ;0 variable args
						callmethod GetFactionRank ::temp38 ::temp39 ::ArenaFaction_var ;1 variable args
						assign playerRank ::temp39 
						; line 357
						cmp_lte ::temp40 ::FightsToNextLevel_var 0 
						jmpf ::temp40 _label0
						; line 360
						return ::TransitionFight_var 
						jmp _label0
						; line 363
					_label0:
						cmp_eq ::temp40 playerRank 0 
						jmpf ::temp40 _label1
						; line 365
						assign minFight 1 
						; line 366
						assign maxFight 3 
						; line 367
						callstatic utility RandomInt ::temp39 minFight maxFight ;2 variable args
						assign fightIndex ::temp39 
						; line 369
						callmethod GetFightQuestFromIndex self ::temp41 fightIndex ;1 variable args
						return ::temp41 
						jmp _label2
						; line 370
					_label1:
						cmp_eq ::temp42 playerRank 1 
						jmpf ::temp42 _label3
						; line 372
						callstatic utility RandomInt ::temp39 0 2 ;2 variable args
						cast ::temp43 ::temp39 
						assign humanFight ::temp43 
						; line 373
						not ::temp43 humanFight 
						jmpf ::temp43 _label4
						; line 374
						assign minFight 2 
						; line 375
						assign maxFight 3 
						; line 376
						callstatic utility RandomInt ::temp39 minFight maxFight ;2 variable args
						assign ::mangled_fightindex_0 ::temp39 
						; line 378
						callmethod GetFightQuestFromIndex self ::temp44 ::mangled_fightindex_0 ;1 variable args
						return ::temp44 
						jmp _label5
						; line 381
					_label4:
						return ::Fight04_var 
					_label5:
						jmp _label2
						; line 383
					_label3:
						cmp_eq ::temp43 playerRank 2 
						jmpf ::temp43 _label6
						; line 385
						assign minFight 5 
						; line 386
						assign maxFight 9 
						; line 387
						callstatic utility RandomInt ::temp39 minFight maxFight ;2 variable args
						assign ::mangled_fightindex_1 ::temp39 
						; line 389
						callmethod GetFightQuestFromIndex self ::temp45 ::mangled_fightindex_1 ;1 variable args
						return ::temp45 
						jmp _label2
						; line 390
					_label6:
						cmp_eq ::temp42 playerRank 3 
						jmpf ::temp42 _label7
						; line 392
						callstatic utility RandomInt ::temp39 0 2 ;2 variable args
						assign animalFight ::temp39 
						; line 393
						cmp_eq ::temp43 animalFight 0 
						jmpf ::temp43 _label8
						; line 394
						assign minFight 7 
						; line 395
						assign maxFight 9 
						; line 396
						callstatic utility RandomInt ::temp39 minFight maxFight ;2 variable args
						assign ::mangled_fightindex_2 ::temp39 
						; line 397
						cmp_eq ::temp46 ::mangled_fightindex_2 9 
						jmpf ::temp46 _label9
						; line 398
						assign ::mangled_fightindex_2 10 
						jmp _label9
						; line 401
					_label9:
						callmethod GetFightQuestFromIndex self ::temp47 ::mangled_fightindex_2 ;1 variable args
						return ::temp47 
						jmp _label10
						; line 404
					_label8:
						return ::Fight11_var 
					_label10:
						jmp _label2
						; line 408
					_label7:
						callstatic utility RandomInt ::temp39 1 10 ;2 variable args
						assign fightRoll ::temp39 
						; line 409
						cmp_lte ::temp46 fightRoll 3 
						jmpf ::temp46 _label11
						; line 410
						callstatic utility RandomInt ::temp39 0 1 ;2 variable args
						jmpf ::temp39 _label12
						; line 411
						return ::Fight08_var 
						jmp _label13
						; line 413
					_label12:
						return ::Fight10_var 
					_label13:
						jmp _label2
						; line 415
					_label11:
						cmp_lte ::temp43 fightRoll 9 
						jmpf ::temp43 _label14
						; line 416
						return ::Fight13_var 
						jmp _label2
						; line 418
					_label14:
						return ::Fight12_var 
						; line 422
					_label2:
						cast ::temp48 none 
						return ::temp48 
					.endCode
				.endFunction ;PickNextFight
			.endState
		.endStateTable
	.endObject
.endObjectTable
</pre>
</div>

<p>Decompiling a file with assembly comments</p>
<div class="command-line">Champollion.exe bsa\out\scripts\arenascript.pex -c</div>
<div class="output">
<pre>
bsa\out\scripts\arenascript.pex decompiled to .\arenascript.psc
1 files processed in 0.0190011 s
</pre>
</div>
<div class="psc-sample">
<span class="sample">arenascript.psc</span>
<pre>
;/ Decompiled by Champollion V1.0.0
Source   : ArenaScript.psc
Modified : 2012-02-12 00:06:16
Compiled : 2013-02-13 20:15:01
User     : builds
Computer : BUILDFARM09
/;
scriptName ArenaScript extends Quest conditional

;-- Properties --------------------------------------
int property WagerAmount auto
ArenaCombatQuest property SpecialFightDB auto
Armor property LoanerShield auto
bool property NextWagerFightIsPeople auto conditional
Faction property ArenaFaction auto
Faction property EastmarchCrimeFaction auto
ObjectReference property Gate1 auto
ReferenceAlias property PitDoor auto
Quest property EastmarchJail auto
bool property CombatOngoing auto conditional
Quest property DB03 auto
ArenaCombatQuest property Fight13 auto
ArenaCombatQuest property TransitionFight auto
Faction property SelfLoathing auto
ReferenceAlias property Combatant10 auto
ObjectReference property Gate2 auto
ArenaCombatQuest property Fight12 auto
Keyword property Wave4Keyword auto
Keyword property Wave2Keyword auto
bool property NextWagerFightIsEasyAnimals auto conditional
ObjectReference property Gate3 auto
bool property NextWagerFightIsExotic auto conditional
int property Level0Fights auto
int property NumberOfPlayerFights auto
ArenaCombatQuest property NextWagerFight auto
ArenaCombatQuest property Fight04 auto
ReferenceAlias property Combatant02 auto
ReferenceAlias property Combatant07 auto
ArenaCombatQuest property Fight01 auto
bool property PlayerChoseTheField auto conditional
ReferenceAlias property Combatant09 auto
ArenaCombatQuest property Fight05 auto
ReferenceAlias property Combatant03 auto
ArenaCombatQuest property SpecialFightJail auto
ArenaCombatQuest property CurrentFight auto
Keyword property Wave1Keyword auto
ReferenceAlias property Combatant08 auto
bool property RewardDue auto conditional
ReferenceAlias property TransitionCombatant auto
int property Level3Fights auto
ReferenceAlias property Combatant06 auto
bool property WagerResolutionRequired auto conditional
ArenaCombatQuest property Fight11 auto
ReferenceAlias property Combatant05 auto
ArenaCombatQuest property Fight03 auto
ArenaCombatQuest property Fight10 auto
ArenaCombatQuest property Fight09 auto
Faction property PacifyFaction auto
int property Level2Fights auto
ArenaCombatQuest property Fight06 auto
bool property NextWagerFightIsToughAnimals auto conditional
ReferenceAlias property Combatant04 auto
ArenaCombatQuest property Fight08 auto
Quest property ArenaWagerFighterQuest auto
Weapon property LoanerSword auto
bool property PlayerWonWager auto conditional
Keyword property Wave5Keyword auto
bool property PlayerGotTheSkinny auto conditional
ArenaCombatQuest property Fight02 auto
int property Level1Fights auto
bool property DBFightWentAwry = false auto conditional
Keyword property Wave3Keyword auto
int property ArrestOffset auto
bool property CombatPreSet auto
MiscObject property Gold auto
bool property WagerOngoing auto conditional
int property FightsToNextLevel auto conditional
ArenaCombatQuest property Fight07 auto
ReferenceAlias property Combatant01 auto
Quest property PointerQuest auto
Keyword property LinkedDoorKeyword auto

;-- Variables ---------------------------------------
; int ::Level0Fights_var
; int ::Level3Fights_var
; int ::FightsToNextLevel_var conditional
; bool ::NextWagerFightIsExotic_var conditional
; arenacombatquest ::Fight03_var
; referencealias ::Combatant08_var
; referencealias ::Combatant04_var
; quest ::PointerQuest_var
; bool ::RewardDue_var conditional
; quest ::ArenaWagerFighterQuest_var
; arenacombatquest ::Fight08_var
; arenacombatquest ::NextWagerFight_var
; referencealias ::Combatant03_var
; arenacombatquest ::Fight12_var
int _maxFights = 13
; int ::NumberOfPlayerFights_var
; arenacombatquest ::SpecialFightDB_var
; bool ::PlayerGotTheSkinny_var conditional
; arenacombatquest ::CurrentFight_var
; keyword ::Wave4Keyword_var
; keyword ::Wave3Keyword_var
; arenacombatquest ::Fight05_var
; int ::WagerAmount_var
; bool ::PlayerWonWager_var conditional
; arenacombatquest ::Fight13_var
; miscobject ::Gold_var
; faction ::ArenaFaction_var
; keyword ::Wave1Keyword_var
; bool ::DBFightWentAwry_var = false conditional
; arenacombatquest ::Fight02_var
; referencealias ::Combatant09_var
; referencealias ::Combatant05_var
; bool ::CombatOngoing_var conditional
; int ::Level1Fights_var
; int ::Level2Fights_var
ObjectReference _spawnPoint02
; arenacombatquest ::SpecialFightJail_var
; keyword ::Wave5Keyword_var
; arenacombatquest ::Fight07_var
; arenacombatquest ::Fight11_var
; faction ::EastmarchCrimeFaction_var
; faction ::SelfLoathing_var
ObjectReference _spawnPoint03
; keyword ::LinkedDoorKeyword_var
; bool ::WagerOngoing_var conditional
; referencealias ::Combatant07_var
; bool ::NextWagerFightIsToughAnimals_var conditional
; bool ::PlayerChoseTheField_var conditional
; bool ::NextWagerFightIsEasyAnimals_var conditional
; arenacombatquest ::Fight09_var
; referencealias ::Combatant02_var
ObjectReference _spawnPoint05
; arenacombatquest ::Fight04_var
; arenacombatquest ::TransitionFight_var
; arenacombatquest ::Fight01_var
; bool ::CombatPreSet_var
; quest ::DB03_var
; faction ::PacifyFaction_var
; referencealias ::Combatant06_var
; quest ::EastmarchJail_var
; int ::ArrestOffset_var
ObjectReference _spawnPoint04
; keyword ::Wave2Keyword_var
; armor ::LoanerShield_var
; objectreference ::Gate1_var
; weapon ::LoanerSword_var
; referencealias ::TransitionCombatant_var
; objectreference ::Gate2_var
; objectreference ::Gate3_var
; referencealias ::Combatant10_var
; arenacombatquest ::Fight06_var
; referencealias ::PitDoor_var
; referencealias ::Combatant01_var
; arenacombatquest ::Fight10_var
; bool ::WagerResolutionRequired_var conditional
; bool ::NextWagerFightIsPeople_var conditional
ObjectReference _spawnPoint01

;-- Functions ---------------------------------------

function RegisterCombatant(ObjectReference fighter)

	;actor ::temp76
	;NONE ::nonevar
	;arenacombatquest ::temp77
	;bool ::temp78
	;bool ::temp79
	
	; 000 : cast ::temp76 fighter 
	; 001 : callmethod AddToFaction ::temp76 ::nonevar ::PacifyFaction_var 
	(fighter as actor).AddToFaction(PacifyFaction)
	; 002 : cast ::temp77 none 
	; 003 : cmp_eq ::temp78 ::CurrentFight_var ::temp77 
	; 004 : not ::temp78 ::temp78 
	; 005 : cast ::temp78 ::temp78 
	; 006 : jmpf ::temp78 010
	; 007 : cast ::temp77 ::CurrentFight_var 
	; 008 : propget IsTransitionFight ::temp77 ::temp79 
	; 009 : cast ::temp78 ::temp79 
	; 010 : jmpf ::temp78 014
	if CurrentFight != none && (CurrentFight as arenacombatquest).IsTransitionFight
		; 011 : callmethod RegisterTransitionCombatant self ::nonevar fighter 
		self.RegisterTransitionCombatant(fighter)
		; 012 : return none 
		return 
	; 013 : jmp 014
	endIf
	; 014 : callmethod ForceRefIfEmpty ::Combatant01_var ::temp79 fighter 
	; 015 : jmpf ::temp79 017
	if Combatant01.ForceRefIfEmpty(fighter)
		
	; 016 : jmp 044
	; 017 : callmethod ForceRefIfEmpty ::Combatant02_var ::temp78 fighter 
	; 018 : jmpf ::temp78 020
	elseIf Combatant02.ForceRefIfEmpty(fighter)
		
	; 019 : jmp 044
	; 020 : callmethod ForceRefIfEmpty ::Combatant03_var ::temp78 fighter 
	; 021 : jmpf ::temp78 023
	elseIf Combatant03.ForceRefIfEmpty(fighter)
		
	; 022 : jmp 044
	; 023 : callmethod ForceRefIfEmpty ::Combatant04_var ::temp78 fighter 
	; 024 : jmpf ::temp78 026
	elseIf Combatant04.ForceRefIfEmpty(fighter)
		
	; 025 : jmp 044
	; 026 : callmethod ForceRefIfEmpty ::Combatant05_var ::temp78 fighter 
	; 027 : jmpf ::temp78 029
	elseIf Combatant05.ForceRefIfEmpty(fighter)
		
	; 028 : jmp 044
	; 029 : callmethod ForceRefIfEmpty ::Combatant06_var ::temp78 fighter 
	; 030 : jmpf ::temp78 032
	elseIf Combatant06.ForceRefIfEmpty(fighter)
		
	; 031 : jmp 044
	; 032 : callmethod ForceRefIfEmpty ::Combatant07_var ::temp78 fighter 
	; 033 : jmpf ::temp78 035
	elseIf Combatant07.ForceRefIfEmpty(fighter)
		
	; 034 : jmp 044
	; 035 : callmethod ForceRefIfEmpty ::Combatant08_var ::temp78 fighter 
	; 036 : jmpf ::temp78 038
	elseIf Combatant08.ForceRefIfEmpty(fighter)
		
	; 037 : jmp 044
	; 038 : callmethod ForceRefIfEmpty ::Combatant09_var ::temp78 fighter 
	; 039 : jmpf ::temp78 041
	elseIf Combatant09.ForceRefIfEmpty(fighter)
		
	; 040 : jmp 044
	; 041 : callmethod ForceRefIfEmpty ::Combatant10_var ::temp78 fighter 
	; 042 : jmpf ::temp78 044
	elseIf Combatant10.ForceRefIfEmpty(fighter)
		
	; 000 : cast ::temp76 fighter 
	endIf
endFunction

function Promote()

	;actor ::temp26
	;NONE ::nonevar
	;int ::temp27
	;bool ::temp28
	;bool ::temp29
	
	; 000 : callstatic game GetPlayer ::temp26 
	; 001 : callmethod ModFactionRank ::temp26 ::nonevar ::ArenaFaction_var 1 
	game.GetPlayer().ModFactionRank(ArenaFaction, 1)
	; 002 : callstatic game GetPlayer ::temp26 
	; 003 : callmethod GetFactionRank ::temp26 ::temp27 ::ArenaFaction_var 
	; 004 : assign rank ::temp27 
	int rank = game.GetPlayer().GetFactionRank(ArenaFaction)
	; 005 : cmp_eq ::temp28 rank 1 
	; 006 : jmpf ::temp28 009
	if rank == 1
		; 007 : assign ::FightsToNextLevel_var ::Level1Fights_var 
		FightsToNextLevel = Level1Fights
	; 008 : jmp 021
	; 009 : cmp_eq ::temp29 rank 2 
	; 010 : jmpf ::temp29 013
	elseIf rank == 2
		; 011 : assign ::FightsToNextLevel_var ::Level2Fights_var 
		FightsToNextLevel = Level2Fights
	; 012 : jmp 021
	; 013 : cmp_eq ::temp29 rank 3 
	; 014 : jmpf ::temp29 017
	elseIf rank == 3
		; 015 : assign ::FightsToNextLevel_var ::Level3Fights_var 
		FightsToNextLevel = Level3Fights
	; 016 : jmp 021
	; 017 : cmp_eq ::temp29 rank 4 
	; 018 : jmpf ::temp29 021
	elseIf rank == 4
		; 019 : assign ::FightsToNextLevel_var 2147483647 
		FightsToNextLevel = 2147483647
	; 020 : jmp 021
	endIf
endFunction

function RegisterTransitionCombatant(ObjectReference fighter)

	;ObjectReference ::temp57
	;ObjectReference ::temp58
	;bool ::temp59
	;NONE ::nonevar
	;actor ::temp60
	
	; 000 : callmethod GetReference ::TransitionCombatant_var ::temp57 
	; 001 : cast ::temp58 none 
	; 002 : cmp_eq ::temp59 ::temp57 ::temp58 
	; 003 : not ::temp59 ::temp59 
	; 004 : jmpf ::temp59 007
	if TransitionCombatant.GetReference() != none
		; 005 : return none 
		return 
	; 006 : jmp 007
	endIf
	; 007 : callmethod ForceRefTo ::TransitionCombatant_var ::nonevar fighter 
	TransitionCombatant.ForceRefTo(fighter)
	; 008 : callmethod GetActorReference ::TransitionCombatant_var ::temp60 
	; 009 : callmethod SetNoBleedoutRecovery ::temp60 ::nonevar true 
	TransitionCombatant.GetActorReference().SetNoBleedoutRecovery(true)
endFunction

function EndWagerFight()

	;arenawagerfighterquestscript ::temp14
	;referencealias ::temp15
	;actor ::temp16
	;bool ::temp17
	;NONE ::nonevar
	
	; 000 : cast ::temp14 ::ArenaWagerFighterQuest_var 
	; 001 : propget fighter ::temp14 ::temp15 
	; 002 : callmethod GetActorReference ::temp15 ::temp16 
	; 003 : callmethod IsDead ::temp16 ::temp17 
	; 004 : assign fieldWon ::temp17 
	bool fieldWon = (ArenaWagerFighterQuest as arenawagerfighterquestscript).fighter.GetActorReference().IsDead()
	; 005 : callmethod Stop ::NextWagerFight_var ::nonevar 
	NextWagerFight.Stop()
	; 006 : cmp_eq ::temp17 ::PlayerChoseTheField_var fieldWon 
	; 007 : jmpf ::temp17 010
	if PlayerChoseTheField == fieldWon
		; 008 : assign ::PlayerWonWager_var true 
		PlayerWonWager = true
	; 009 : jmp 011
	else
		; 010 : assign ::PlayerWonWager_var false 
		PlayerWonWager = false
	endIf
	; 011 : assign ::WagerResolutionRequired_var true 
	WagerResolutionRequired = true
endFunction

; Skipped compiler generated GotoState

keyword function GetKeywordForWave(int wave)

	;bool ::temp61
	;bool ::temp62
	;keyword ::temp63
	
	; 000 : cmp_eq ::temp61 wave 1 
	; 001 : jmpf ::temp61 004
	if wave == 1
		; 002 : return ::Wave1Keyword_var 
		return Wave1Keyword
	; 003 : jmp 022
	; 004 : cmp_eq ::temp62 wave 2 
	; 005 : jmpf ::temp62 008
	elseIf wave == 2
		; 006 : return ::Wave2Keyword_var 
		return Wave2Keyword
	; 007 : jmp 022
	; 008 : cmp_eq ::temp62 wave 3 
	; 009 : jmpf ::temp62 012
	elseIf wave == 3
		; 010 : return ::Wave3Keyword_var 
		return Wave3Keyword
	; 011 : jmp 022
	; 012 : cmp_eq ::temp62 wave 4 
	; 013 : jmpf ::temp62 016
	elseIf wave == 4
		; 014 : return ::Wave4Keyword_var 
		return Wave4Keyword
	; 015 : jmp 022
	; 016 : cmp_eq ::temp62 wave 5 
	; 017 : jmpf ::temp62 020
	elseIf wave == 5
		; 018 : return ::Wave5Keyword_var 
		return Wave5Keyword
	; 019 : jmp 022
	else
		; 020 : cast ::temp63 none 
		; 021 : return ::temp63 
		return none
	endIf
endFunction

function PlayerJoin()

	;bool ::temp9
	;actor ::temp11
	;NONE ::nonevar
	;bool ::temp10
	
	; 000 : callmethod IsRunning ::PointerQuest_var ::temp9 
	; 001 : jmpf ::temp9 004
	if PointerQuest.IsRunning()
		; 002 : callmethod SetStage ::PointerQuest_var ::temp10 20 
		PointerQuest.SetStage(20)
	; 003 : jmp 004
	endIf
	; 004 : callstatic game GetPlayer ::temp11 
	; 005 : callmethod AddToFaction ::temp11 ::nonevar ::ArenaFaction_var 
	game.GetPlayer().AddToFaction(ArenaFaction)
	; 006 : assign ::NumberOfPlayerFights_var 0 
	NumberOfPlayerFights = 0
	; 007 : assign ::FightsToNextLevel_var ::Level0Fights_var 
	FightsToNextLevel = Level0Fights
endFunction

function PlayerAvoidedWager()

	
	; 000 : assign ::PlayerChoseTheField_var false 
	PlayerChoseTheField = false
	; 001 : assign ::WagerOngoing_var false 
	WagerOngoing = false
endFunction

function CombatOver()

	;ObjectReference ::temp49
	;int ::temp50
	;NONE ::nonevar
	
	; 000 : jmpf ::WagerOngoing_var 004
	if WagerOngoing
		; 001 : callmethod EndWagerFight self ::nonevar 
		self.EndWagerFight()
		; 002 : return none 
		return 
	; 003 : jmp 004
	endIf
	; 004 : callmethod Stop ::CurrentFight_var ::nonevar 
	CurrentFight.Stop()
	; 005 : callmethod GetReference ::PitDoor_var ::temp49 
	; 006 : callmethod Lock ::temp49 ::nonevar false false 
	PitDoor.GetReference().Lock(false, false)
	; 007 : assign ::CombatOngoing_var false 
	CombatOngoing = false
	; 008 : assign ::RewardDue_var true 
	RewardDue = true
	; 009 : iadd ::temp50 ::NumberOfPlayerFights_var 1 
	; 010 : assign ::NumberOfPlayerFights_var ::temp50 
	NumberOfPlayerFights += 1
endFunction

function ResolveWager()

	;actor ::temp18
	;int ::temp19
	;form ::temp20
	;NONE ::nonevar
	
	; 000 : jmpf ::PlayerWonWager_var 006
	if PlayerWonWager
		; 001 : callstatic game GetPlayer ::temp18 
		; 002 : imul ::temp19 ::WagerAmount_var 2 
		; 003 : cast ::temp20 ::Gold_var 
		; 004 : callmethod AddItem ::temp18 ::nonevar ::temp20 ::temp19 false 
		game.GetPlayer().AddItem(Gold as form, WagerAmount * 2, false)
	; 005 : jmp 006
	endIf
	; 006 : callmethod CleanupBodies self ::nonevar 
	self.CleanupBodies()
	; 007 : assign ::WagerOngoing_var false 
	WagerOngoing = false
	; 008 : assign ::WagerResolutionRequired_var false 
	WagerResolutionRequired = false
	; 009 : callmethod Stop ::ArenaWagerFighterQuest_var ::nonevar 
	ArenaWagerFighterQuest.Stop()
	; 010 : callmethod PickNextWagerFight self ::nonevar ::NextWagerFight_var 
	self.PickNextWagerFight(NextWagerFight)
endFunction

function StartWagerFight()

	;bool ::temp21
	
	; 000 : callmethod Start ::NextWagerFight_var ::temp21 
	NextWagerFight.Start()
	; 001 : callmethod Start ::ArenaWagerFighterQuest_var ::temp21 
	ArenaWagerFighterQuest.Start()
	; 002 : assign ::CombatPreSet_var true 
	CombatPreSet = true
endFunction

function StartCombat()

	;int ::temp30
	;bool ::temp31
	;bool ::temp32
	;bool ::temp35
	;ObjectReference ::temp37
	;actor ::temp33
	;form ::temp34
	;NONE ::nonevar
	;arenacombatquest ::temp36
	
	; 000 : callmethod GetStage ::DB03_var ::temp30 
	; 001 : cmp_lte ::temp31 20 ::temp30 
	; 002 : cast ::temp31 ::temp31 
	; 003 : jmpf ::temp31 007
	; 004 : callmethod GetStage ::DB03_var ::temp30 
	; 005 : cmp_gt ::temp32 40 ::temp30 
	; 006 : cast ::temp31 ::temp32 
	; 007 : jmpf ::temp31 034
	if 20 <= DB03.GetStage() && 40 > DB03.GetStage()
		; 008 : assign ::CurrentFight_var ::SpecialFightDB_var 
		CurrentFight = SpecialFightDB
		; 009 : callstatic game GetPlayer ::temp33 
		; 010 : cast ::temp34 ::LoanerSword_var 
		; 011 : callmethod GetItemCount ::temp33 ::temp30 ::temp34 
		; 012 : cmp_lt ::temp32 ::temp30 1 
		; 013 : jmpf ::temp32 018
		if game.GetPlayer().GetItemCount(LoanerSword as form) < 1
			; 014 : callstatic game GetPlayer ::temp33 
			; 015 : cast ::temp34 ::LoanerSword_var 
			; 016 : callmethod AddItem ::temp33 ::nonevar ::temp34 1 false 
			game.GetPlayer().AddItem(LoanerSword as form, 1, false)
		; 017 : jmp 018
		endIf
		; 018 : callstatic game GetPlayer ::temp33 
		; 019 : cast ::temp34 ::LoanerShield_var 
		; 020 : callmethod GetItemCount ::temp33 ::temp30 ::temp34 
		; 021 : cmp_lt ::temp32 ::temp30 1 
		; 022 : jmpf ::temp32 027
		if game.GetPlayer().GetItemCount(LoanerShield as form) < 1
			; 023 : callstatic game GetPlayer ::temp33 
			; 024 : cast ::temp34 ::LoanerShield_var 
			; 025 : callmethod AddItem ::temp33 ::nonevar ::temp34 1 false 
			game.GetPlayer().AddItem(LoanerShield as form, 1, false)
		; 026 : jmp 027
		endIf
		; 027 : callstatic game GetPlayer ::temp33 
		; 028 : cast ::temp34 ::LoanerSword_var 
		; 029 : callmethod EquipItem ::temp33 ::nonevar ::temp34 false false 
		game.GetPlayer().EquipItem(LoanerSword as form, false, false)
		; 030 : callstatic game GetPlayer ::temp33 
		; 031 : cast ::temp34 ::LoanerShield_var 
		; 032 : callmethod EquipItem ::temp33 ::nonevar ::temp34 false false 
		game.GetPlayer().EquipItem(LoanerShield as form, false, false)
	; 033 : jmp 057
	; 034 : callmethod GetStage ::EastmarchJail_var ::temp30 
	; 035 : cmp_eq ::temp32 20 ::temp30 
	; 036 : cast ::temp32 ::temp32 
	; 037 : jmpf ::temp32 040
	; 038 : callmethod IsRunning ::EastmarchJail_var ::temp35 
	; 039 : cast ::temp32 ::temp35 
	; 040 : jmpf ::temp32 055
	elseIf 20 == EastmarchJail.GetStage() && EastmarchJail.IsRunning()
		; 041 : assign ::CurrentFight_var ::SpecialFightJail_var 
		CurrentFight = SpecialFightJail
		; 042 : callstatic game GetPlayer ::temp33 
		; 043 : cast ::temp34 ::LoanerSword_var 
		; 044 : callmethod AddItem ::temp33 ::nonevar ::temp34 1 false 
		game.GetPlayer().AddItem(LoanerSword as form, 1, false)
		; 045 : callstatic game GetPlayer ::temp33 
		; 046 : cast ::temp34 ::LoanerShield_var 
		; 047 : callmethod AddItem ::temp33 ::nonevar ::temp34 1 false 
		game.GetPlayer().AddItem(LoanerShield as form, 1, false)
		; 048 : callstatic game GetPlayer ::temp33 
		; 049 : cast ::temp34 ::LoanerSword_var 
		; 050 : callmethod EquipItem ::temp33 ::nonevar ::temp34 false false 
		game.GetPlayer().EquipItem(LoanerSword as form, false, false)
		; 051 : callstatic game GetPlayer ::temp33 
		; 052 : cast ::temp34 ::LoanerShield_var 
		; 053 : callmethod EquipItem ::temp33 ::nonevar ::temp34 false false 
		game.GetPlayer().EquipItem(LoanerShield as form, false, false)
	; 054 : jmp 057
	else
		; 055 : callmethod PickNextFight self ::temp36 0 
		; 056 : assign ::CurrentFight_var ::temp36 
		CurrentFight = self.PickNextFight(0)
	endIf
	; 057 : callmethod Start ::CurrentFight_var ::temp35 
	CurrentFight.Start()
	; 058 : assign ::CombatPreSet_var true 
	CombatPreSet = true
	; 059 : callmethod GetReference ::PitDoor_var ::temp37 
	; 060 : callmethod Lock ::temp37 ::nonevar false false 
	PitDoor.GetReference().Lock(false, false)
	; 061 : assign ::CombatOngoing_var true 
	CombatOngoing = true
endFunction

arenacombatquest function GetFightQuestFromIndex(int questIndex)

	;bool ::temp0
	;bool ::temp1
	;arenacombatquest ::temp2
	
	; 000 : cmp_eq ::temp0 questIndex 1 
	; 001 : jmpf ::temp0 004
	if questIndex == 1
		; 002 : return ::Fight01_var 
		return Fight01
	; 003 : jmp 054
	; 004 : cmp_eq ::temp1 questIndex 2 
	; 005 : jmpf ::temp1 008
	elseIf questIndex == 2
		; 006 : return ::Fight02_var 
		return Fight02
	; 007 : jmp 054
	; 008 : cmp_eq ::temp1 questIndex 3 
	; 009 : jmpf ::temp1 012
	elseIf questIndex == 3
		; 010 : return ::Fight03_var 
		return Fight03
	; 011 : jmp 054
	; 012 : cmp_eq ::temp1 questIndex 4 
	; 013 : jmpf ::temp1 016
	elseIf questIndex == 4
		; 014 : return ::Fight04_var 
		return Fight04
	; 015 : jmp 054
	; 016 : cmp_eq ::temp1 questIndex 5 
	; 017 : jmpf ::temp1 020
	elseIf questIndex == 5
		; 018 : return ::Fight05_var 
		return Fight05
	; 019 : jmp 054
	; 020 : cmp_eq ::temp1 questIndex 6 
	; 021 : jmpf ::temp1 024
	elseIf questIndex == 6
		; 022 : return ::Fight06_var 
		return Fight06
	; 023 : jmp 054
	; 024 : cmp_eq ::temp1 questIndex 7 
	; 025 : jmpf ::temp1 028
	elseIf questIndex == 7
		; 026 : return ::Fight07_var 
		return Fight07
	; 027 : jmp 054
	; 028 : cmp_eq ::temp1 questIndex 8 
	; 029 : jmpf ::temp1 032
	elseIf questIndex == 8
		; 030 : return ::Fight08_var 
		return Fight08
	; 031 : jmp 054
	; 032 : cmp_eq ::temp1 questIndex 9 
	; 033 : jmpf ::temp1 036
	elseIf questIndex == 9
		; 034 : return ::Fight09_var 
		return Fight09
	; 035 : jmp 054
	; 036 : cmp_eq ::temp1 questIndex 10 
	; 037 : jmpf ::temp1 040
	elseIf questIndex == 10
		; 038 : return ::Fight10_var 
		return Fight10
	; 039 : jmp 054
	; 040 : cmp_eq ::temp1 questIndex 11 
	; 041 : jmpf ::temp1 044
	elseIf questIndex == 11
		; 042 : return ::Fight11_var 
		return Fight11
	; 043 : jmp 054
	; 044 : cmp_eq ::temp1 questIndex 12 
	; 045 : jmpf ::temp1 048
	elseIf questIndex == 12
		; 046 : return ::Fight12_var 
		return Fight12
	; 047 : jmp 054
	; 048 : cmp_eq ::temp1 questIndex 13 
	; 049 : jmpf ::temp1 052
	elseIf questIndex == 13
		; 050 : return ::Fight13_var 
		return Fight13
	; 051 : jmp 054
	else
		; 052 : cast ::temp2 none 
		; 053 : return ::temp2 
		return none
	endIf
endFunction

function CleanupBodies()

	;bool ::temp80
	;ObjectReference ::temp81
	;ObjectReference ::temp82
	;actor ::temp83
	;NONE ::nonevar
	
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	; 001 : jmpf ::temp80 003
	if self._CleanupBody(Combatant01)
		
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	endIf
	; 003 : callmethod _CleanupBody self ::temp80 ::Combatant02_var 
	; 004 : jmpf ::temp80 006
	if self._CleanupBody(Combatant02)
		
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	endIf
	; 006 : callmethod _CleanupBody self ::temp80 ::Combatant03_var 
	; 007 : jmpf ::temp80 009
	if self._CleanupBody(Combatant03)
		
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	endIf
	; 009 : callmethod _CleanupBody self ::temp80 ::Combatant04_var 
	; 010 : jmpf ::temp80 012
	if self._CleanupBody(Combatant04)
		
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	endIf
	; 012 : callmethod _CleanupBody self ::temp80 ::Combatant05_var 
	; 013 : jmpf ::temp80 015
	if self._CleanupBody(Combatant05)
		
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	endIf
	; 015 : callmethod _CleanupBody self ::temp80 ::Combatant06_var 
	; 016 : jmpf ::temp80 018
	if self._CleanupBody(Combatant06)
		
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	endIf
	; 018 : callmethod _CleanupBody self ::temp80 ::Combatant07_var 
	; 019 : jmpf ::temp80 021
	if self._CleanupBody(Combatant07)
		
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	endIf
	; 021 : callmethod _CleanupBody self ::temp80 ::Combatant08_var 
	; 022 : jmpf ::temp80 024
	if self._CleanupBody(Combatant08)
		
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	endIf
	; 024 : callmethod _CleanupBody self ::temp80 ::Combatant09_var 
	; 025 : jmpf ::temp80 027
	if self._CleanupBody(Combatant09)
		
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	endIf
	; 027 : callmethod _CleanupBody self ::temp80 ::Combatant10_var 
	; 028 : jmpf ::temp80 030
	if self._CleanupBody(Combatant10)
		
	; 000 : callmethod _CleanupBody self ::temp80 ::Combatant01_var 
	endIf
	; 030 : callmethod GetReference ::TransitionCombatant_var ::temp81 
	; 031 : cast ::temp82 none 
	; 032 : cmp_eq ::temp80 ::temp81 ::temp82 
	; 033 : not ::temp80 ::temp80 
	; 034 : jmpf ::temp80 044
	if TransitionCombatant.GetReference() != none
		; 035 : callmethod GetActorReference ::TransitionCombatant_var ::temp83 
		; 036 : assign ref ::temp83 
		actor ref = TransitionCombatant.GetActorReference()
		; 037 : callstatic game GetPlayer ::temp83 
		; 038 : callmethod RemoveFromFaction ::temp83 ::nonevar ::SelfLoathing_var 
		game.GetPlayer().RemoveFromFaction(SelfLoathing)
		; 039 : callmethod RemoveFromFaction ref ::nonevar ::SelfLoathing_var 
		ref.RemoveFromFaction(SelfLoathing)
		; 040 : callmethod SetFactionRank ref ::nonevar ::ArenaFaction_var 4 
		ref.SetFactionRank(ArenaFaction, 4)
		; 041 : callmethod SetNoBleedoutRecovery ref ::nonevar false 
		ref.SetNoBleedoutRecovery(false)
		; 042 : callmethod Clear ::TransitionCombatant_var ::nonevar 
		TransitionCombatant.Clear()
	; 043 : jmp 044
	endIf
	; 044 : cast ::temp82 none 
	; 045 : assign _spawnPoint01 ::temp82 
	_spawnPoint01 = none
	; 046 : cast ::temp81 none 
	; 047 : assign _spawnPoint02 ::temp81 
	_spawnPoint02 = none
	; 048 : cast ::temp82 none 
	; 049 : assign _spawnPoint03 ::temp82 
	_spawnPoint03 = none
	; 050 : cast ::temp81 none 
	; 051 : assign _spawnPoint04 ::temp81 
	_spawnPoint04 = none
	; 052 : cast ::temp82 none 
	; 053 : assign _spawnPoint05 ::temp82 
	_spawnPoint05 = none
	; 054 : callmethod SetOpen ::Gate1_var ::nonevar false 
	Gate1.SetOpen(false)
	; 055 : callmethod SetOpen ::Gate2_var ::nonevar false 
	Gate2.SetOpen(false)
	; 056 : callmethod SetOpen ::Gate3_var ::nonevar false 
	Gate3.SetOpen(false)
endFunction

bool function _CleanupBody(referencealias combatant)

	;ObjectReference ::temp84
	;ObjectReference ::temp85
	;bool ::temp86
	;actor ::temp87
	;NONE ::nonevar
	;bool ::temp88
	
	; 000 : callmethod GetReference combatant ::temp84 
	; 001 : cast ::temp85 none 
	; 002 : cmp_eq ::temp86 ::temp84 ::temp85 
	; 003 : not ::temp86 ::temp86 
	; 004 : jmpf ::temp86 019
	if combatant.GetReference() != none
		; 005 : callmethod GetActorReference combatant ::temp87 
		; 006 : assign ref ::temp87 
		actor ref = combatant.GetActorReference()
		; 007 : callmethod Clear combatant ::nonevar 
		combatant.Clear()
		; 008 : jmpf ::WagerOngoing_var 011
		if WagerOngoing
			; 009 : callmethod Delete ref ::nonevar 
			ref.Delete()
		; 010 : jmp 017
		; 011 : callmethod IsDead ref ::temp88 
		; 012 : jmpf ::temp88 015
		elseIf ref.IsDead()
			; 013 : callmethod Delete ref ::nonevar 
			ref.Delete()
		; 014 : jmp 017
		else
			; 015 : callmethod MoveToMyEditorLocation ref ::nonevar 
			ref.MoveToMyEditorLocation()
			; 016 : callmethod ResetHealthAndLimbs ref ::nonevar 
			ref.ResetHealthAndLimbs()
		endIf
		; 017 : return true 
		return true
	; 018 : jmp 020
	else
		; 019 : return false 
		return false
	endIf
endFunction

function Reward()

	;ObjectReference ::temp51
	;NONE ::nonevar
	;int ::temp52
	;bool ::temp53
	;bool ::temp54
	;actor ::temp55
	;form ::temp56
	
	; 000 : callmethod GetReference ::PitDoor_var ::temp51 
	; 001 : callmethod Lock ::temp51 ::nonevar true false 
	PitDoor.GetReference().Lock(true, false)
	; 002 : callmethod CleanupBodies self ::nonevar 
	self.CleanupBodies()
	; 003 : callmethod GetStage ::EastmarchJail_var ::temp52 
	; 004 : cmp_eq ::temp53 20 ::temp52 
	; 005 : cast ::temp53 ::temp53 
	; 006 : jmpf ::temp53 009
	; 007 : callmethod IsRunning ::EastmarchJail_var ::temp54 
	; 008 : cast ::temp53 ::temp54 
	; 009 : jmpf ::temp53 026
	if 20 == EastmarchJail.GetStage() && EastmarchJail.IsRunning()
		; 010 : callstatic game GetPlayer ::temp55 
		; 011 : cast ::temp56 ::LoanerSword_var 
		; 012 : callmethod UnequipItem ::temp55 ::nonevar ::temp56 false false 
		game.GetPlayer().UnequipItem(LoanerSword as form, false, false)
		; 013 : callstatic game GetPlayer ::temp55 
		; 014 : cast ::temp56 ::LoanerShield_var 
		; 015 : callmethod UnequipItem ::temp55 ::nonevar ::temp56 false false 
		game.GetPlayer().UnequipItem(LoanerShield as form, false, false)
		; 016 : callstatic game GetPlayer ::temp55 
		; 017 : cast ::temp56 ::LoanerSword_var 
		; 018 : callmethod RemoveItem ::temp55 ::nonevar ::temp56 1 false none 
		game.GetPlayer().RemoveItem(LoanerSword as form, 1, false, none)
		; 019 : callstatic game GetPlayer ::temp55 
		; 020 : cast ::temp56 ::LoanerShield_var 
		; 021 : callmethod RemoveItem ::temp55 ::nonevar ::temp56 1 false none 
		game.GetPlayer().RemoveItem(LoanerShield as form, 1, false, none)
		; 022 : callmethod SetCrimeGold ::EastmarchCrimeFaction_var ::nonevar 0 
		EastmarchCrimeFaction.SetCrimeGold(0)
		; 023 : callmethod SetCrimeGoldViolent ::EastmarchCrimeFaction_var ::nonevar 0 
		EastmarchCrimeFaction.SetCrimeGoldViolent(0)
		; 024 : callmethod SetStage ::EastmarchJail_var ::temp54 200 
		EastmarchJail.SetStage(200)
	; 025 : jmp 043
	; 026 : callstatic game GetPlayer ::temp55 
	; 027 : callmethod GetFactionRank ::temp55 ::temp52 ::ArenaFaction_var 
	; 028 : comp_gte ::temp54 ::temp52 4 
	; 029 : jmpf ::temp54 034
	elseIf game.GetPlayer().GetFactionRank(ArenaFaction) >= 4
		; 030 : callstatic game GetPlayer ::temp55 
		; 031 : cast ::temp56 ::Gold_var 
		; 032 : callmethod AddItem ::temp55 ::nonevar ::temp56 100 false 
		game.GetPlayer().AddItem(Gold as form, 100, false)
	; 033 : jmp 043
	; 034 : cmp_lte ::temp54 ::FightsToNextLevel_var 0 
	; 035 : jmpf ::temp54 038
	elseIf FightsToNextLevel <= 0
		; 036 : callmethod Promote self ::nonevar 
		self.Promote()
	; 037 : jmp 043
	else
		; 038 : callstatic game GetPlayer ::temp55 
		; 039 : cast ::temp56 ::Gold_var 
		; 040 : callmethod AddItem ::temp55 ::nonevar ::temp56 100 false 
		game.GetPlayer().AddItem(Gold as form, 100, false)
		; 041 : isub ::temp52 ::FightsToNextLevel_var 1 
		; 042 : assign ::FightsToNextLevel_var ::temp52 
		FightsToNextLevel -= 1
	endIf
	; 043 : assign ::RewardDue_var false 
	RewardDue = false
endFunction

function PlaceBet(int amount)

	;actor ::temp12
	;form ::temp13
	;NONE ::nonevar
	
	; 000 : assign ::WagerOngoing_var true 
	WagerOngoing = true
	; 001 : assign ::WagerAmount_var amount 
	WagerAmount = amount
	; 002 : callstatic game GetPlayer ::temp12 
	; 003 : cast ::temp13 ::Gold_var 
	; 004 : callmethod RemoveItem ::temp12 ::nonevar ::temp13 ::WagerAmount_var false none 
	game.GetPlayer().RemoveItem(Gold as form, WagerAmount, false, none)
endFunction

function RegisterSpawnPoint(ObjectReference spawnMarker)

	;ObjectReference ::temp73
	;bool ::temp74
	;bool ::temp75
	
	; 000 : cast ::temp73 none 
	; 001 : cmp_eq ::temp74 _spawnPoint01 ::temp73 
	; 002 : jmpf ::temp74 005
	if _spawnPoint01 == none
		; 003 : assign _spawnPoint01 spawnMarker 
		_spawnPoint01 = spawnMarker
	; 004 : jmp 025
	; 005 : cast ::temp73 none 
	; 006 : cmp_eq ::temp75 _spawnPoint02 ::temp73 
	; 007 : jmpf ::temp75 010
	elseIf _spawnPoint02 == none
		; 008 : assign _spawnPoint02 spawnMarker 
		_spawnPoint02 = spawnMarker
	; 009 : jmp 025
	; 010 : cast ::temp73 none 
	; 011 : cmp_eq ::temp75 _spawnPoint03 ::temp73 
	; 012 : jmpf ::temp75 015
	elseIf _spawnPoint03 == none
		; 013 : assign _spawnPoint03 spawnMarker 
		_spawnPoint03 = spawnMarker
	; 014 : jmp 025
	; 015 : cast ::temp73 none 
	; 016 : cmp_eq ::temp75 _spawnPoint04 ::temp73 
	; 017 : jmpf ::temp75 020
	elseIf _spawnPoint04 == none
		; 018 : assign _spawnPoint04 spawnMarker 
		_spawnPoint04 = spawnMarker
	; 019 : jmp 025
	; 020 : cast ::temp73 none 
	; 021 : cmp_eq ::temp75 _spawnPoint05 ::temp73 
	; 022 : jmpf ::temp75 025
	elseIf _spawnPoint05 == none
		; 023 : assign _spawnPoint05 spawnMarker 
		_spawnPoint05 = spawnMarker
	; 024 : jmp 025
	endIf
endFunction

int function GetIndexFromFightQuest(arenacombatquest rQuest)

	;bool ::temp3
	;bool ::temp4
	
	; 000 : cmp_eq ::temp3 rQuest ::Fight01_var 
	; 001 : jmpf ::temp3 004
	if rQuest == Fight01
		; 002 : return 1 
		return 1
	; 003 : jmp 053
	; 004 : cmp_eq ::temp4 rQuest ::Fight02_var 
	; 005 : jmpf ::temp4 008
	elseIf rQuest == Fight02
		; 006 : return 2 
		return 2
	; 007 : jmp 053
	; 008 : cmp_eq ::temp4 rQuest ::Fight03_var 
	; 009 : jmpf ::temp4 012
	elseIf rQuest == Fight03
		; 010 : return 3 
		return 3
	; 011 : jmp 053
	; 012 : cmp_eq ::temp4 rQuest ::Fight04_var 
	; 013 : jmpf ::temp4 016
	elseIf rQuest == Fight04
		; 014 : return 4 
		return 4
	; 015 : jmp 053
	; 016 : cmp_eq ::temp4 rQuest ::Fight05_var 
	; 017 : jmpf ::temp4 020
	elseIf rQuest == Fight05
		; 018 : return 5 
		return 5
	; 019 : jmp 053
	; 020 : cmp_eq ::temp4 rQuest ::Fight06_var 
	; 021 : jmpf ::temp4 024
	elseIf rQuest == Fight06
		; 022 : return 6 
		return 6
	; 023 : jmp 053
	; 024 : cmp_eq ::temp4 rQuest ::Fight07_var 
	; 025 : jmpf ::temp4 028
	elseIf rQuest == Fight07
		; 026 : return 7 
		return 7
	; 027 : jmp 053
	; 028 : cmp_eq ::temp4 rQuest ::Fight08_var 
	; 029 : jmpf ::temp4 032
	elseIf rQuest == Fight08
		; 030 : return 8 
		return 8
	; 031 : jmp 053
	; 032 : cmp_eq ::temp4 rQuest ::Fight09_var 
	; 033 : jmpf ::temp4 036
	elseIf rQuest == Fight09
		; 034 : return 9 
		return 9
	; 035 : jmp 053
	; 036 : cmp_eq ::temp4 rQuest ::Fight10_var 
	; 037 : jmpf ::temp4 040
	elseIf rQuest == Fight10
		; 038 : return 10 
		return 10
	; 039 : jmp 053
	; 040 : cmp_eq ::temp4 rQuest ::Fight11_var 
	; 041 : jmpf ::temp4 044
	elseIf rQuest == Fight11
		; 042 : return 11 
		return 11
	; 043 : jmp 053
	; 044 : cmp_eq ::temp4 rQuest ::Fight12_var 
	; 045 : jmpf ::temp4 048
	elseIf rQuest == Fight12
		; 046 : return 12 
		return 12
	; 047 : jmp 053
	; 048 : cmp_eq ::temp4 rQuest ::Fight13_var 
	; 049 : jmpf ::temp4 052
	elseIf rQuest == Fight13
		; 050 : return 13 
		return 13
	; 051 : jmp 053
	else
		; 052 : return 0 
		return 0
	endIf
endFunction

ObjectReference function GetDoorForWave(int wave)

	;keyword ::temp64
	;bool ::temp65
	;bool ::temp67
	;ObjectReference ::temp66
	;ObjectReference ::temp68
	;ObjectReference ::temp69
	;ObjectReference ::temp70
	;ObjectReference ::temp71
	;ObjectReference ::temp72
	
	; 000 : callmethod GetKeywordForWave self ::temp64 wave 
	; 001 : assign toMatch ::temp64 
	keyword toMatch = self.GetKeywordForWave(wave)
	; 002 : callmethod HasKeyword _spawnPoint01 ::temp65 toMatch 
	; 003 : jmpf ::temp65 007
	if _spawnPoint01.HasKeyword(toMatch)
		; 004 : callmethod GetLinkedRef _spawnPoint01 ::temp66 ::LinkedDoorKeyword_var 
		; 005 : return ::temp66 
		return _spawnPoint01.GetLinkedRef(LinkedDoorKeyword)
	; 006 : jmp 029
	; 007 : callmethod HasKeyword _spawnPoint02 ::temp67 toMatch 
	; 008 : jmpf ::temp67 012
	elseIf _spawnPoint02.HasKeyword(toMatch)
		; 009 : callmethod GetLinkedRef _spawnPoint02 ::temp68 ::LinkedDoorKeyword_var 
		; 010 : return ::temp68 
		return _spawnPoint02.GetLinkedRef(LinkedDoorKeyword)
	; 011 : jmp 029
	; 012 : callmethod HasKeyword _spawnPoint03 ::temp67 toMatch 
	; 013 : jmpf ::temp67 017
	elseIf _spawnPoint03.HasKeyword(toMatch)
		; 014 : callmethod GetLinkedRef _spawnPoint03 ::temp69 ::LinkedDoorKeyword_var 
		; 015 : return ::temp69 
		return _spawnPoint03.GetLinkedRef(LinkedDoorKeyword)
	; 016 : jmp 029
	; 017 : callmethod HasKeyword _spawnPoint04 ::temp67 toMatch 
	; 018 : jmpf ::temp67 022
	elseIf _spawnPoint04.HasKeyword(toMatch)
		; 019 : callmethod GetLinkedRef _spawnPoint04 ::temp70 ::LinkedDoorKeyword_var 
		; 020 : return ::temp70 
		return _spawnPoint04.GetLinkedRef(LinkedDoorKeyword)
	; 021 : jmp 029
	; 022 : callmethod HasKeyword _spawnPoint05 ::temp67 toMatch 
	; 023 : jmpf ::temp67 027
	elseIf _spawnPoint05.HasKeyword(toMatch)
		; 024 : callmethod GetLinkedRef _spawnPoint05 ::temp71 ::LinkedDoorKeyword_var 
		; 025 : return ::temp71 
		return _spawnPoint05.GetLinkedRef(LinkedDoorKeyword)
	; 026 : jmp 029
	else
		; 027 : cast ::temp72 none 
		; 028 : return ::temp72 
		return none
	endIf
endFunction

function PickNextWagerFight(arenacombatquest lastFight)

	;arenacombatquest ::temp22
	;bool ::temp23
	;bool ::temp25
	;int ::temp24
	
	; 000 : assign lastFightIndex -1 
	int lastFightIndex = -1
	; 001 : cast ::temp22 none 
	; 002 : cmp_eq ::temp23 lastFight ::temp22 
	; 003 : not ::temp23 ::temp23 
	; 004 : jmpf ::temp23 008
	if lastFight != none
		; 005 : callmethod GetIndexFromFightQuest self ::temp24 lastFight 
		; 006 : assign lastFightIndex ::temp24 
		lastFightIndex = self.GetIndexFromFightQuest(lastFight)
	; 007 : jmp 008
	endIf
	; 008 : assign fightIndex lastFightIndex 
	int fightIndex = lastFightIndex
	; 009 : cmp_eq ::temp23 fightIndex lastFightIndex 
	; 010 : jmpf ::temp23 014
	while fightIndex == lastFightIndex
		; 011 : callstatic utility RandomInt ::temp24 1 _maxFights 
		; 012 : assign fightIndex ::temp24 
		fightIndex = utility.RandomInt(1, _maxFights)
	; 013 : jmp 009
	endWhile
	; 014 : callmethod GetFightQuestFromIndex self ::temp22 fightIndex 
	; 015 : assign ::NextWagerFight_var ::temp22 
	NextWagerFight = self.GetFightQuestFromIndex(fightIndex)
	; 016 : assign ::NextWagerFightIsToughAnimals_var false 
	NextWagerFightIsToughAnimals = false
	; 017 : assign ::NextWagerFightIsEasyAnimals_var false 
	NextWagerFightIsEasyAnimals = false
	; 018 : assign ::NextWagerFightIsPeople_var false 
	NextWagerFightIsPeople = false
	; 019 : assign ::NextWagerFightIsExotic_var false 
	NextWagerFightIsExotic = false
	; 020 : cmp_eq ::temp23 ::NextWagerFight_var ::Fight01_var 
	; 021 : jmpf ::temp23 024
	if NextWagerFight == Fight01
		; 022 : assign ::NextWagerFightIsEasyAnimals_var true 
		NextWagerFightIsEasyAnimals = true
	; 023 : jmp 072
	; 024 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight02_var 
	; 025 : jmpf ::temp25 028
	elseIf NextWagerFight == Fight02
		; 026 : assign ::NextWagerFightIsEasyAnimals_var true 
		NextWagerFightIsEasyAnimals = true
	; 027 : jmp 072
	; 028 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight03_var 
	; 029 : jmpf ::temp25 032
	elseIf NextWagerFight == Fight03
		; 030 : assign ::NextWagerFightIsEasyAnimals_var true 
		NextWagerFightIsEasyAnimals = true
	; 031 : jmp 072
	; 032 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight04_var 
	; 033 : jmpf ::temp25 036
	elseIf NextWagerFight == Fight04
		; 034 : assign ::NextWagerFightIsPeople_var true 
		NextWagerFightIsPeople = true
	; 035 : jmp 072
	; 036 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight05_var 
	; 037 : jmpf ::temp25 040
	elseIf NextWagerFight == Fight05
		; 038 : assign ::NextWagerFightIsToughAnimals_var true 
		NextWagerFightIsToughAnimals = true
	; 039 : jmp 072
	; 040 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight06_var 
	; 041 : jmpf ::temp25 044
	elseIf NextWagerFight == Fight06
		; 042 : assign ::NextWagerFightIsToughAnimals_var true 
		NextWagerFightIsToughAnimals = true
	; 043 : jmp 072
	; 044 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight07_var 
	; 045 : jmpf ::temp25 048
	elseIf NextWagerFight == Fight07
		; 046 : assign ::NextWagerFightIsToughAnimals_var true 
		NextWagerFightIsToughAnimals = true
	; 047 : jmp 072
	; 048 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight08_var 
	; 049 : jmpf ::temp25 052
	elseIf NextWagerFight == Fight08
		; 050 : assign ::NextWagerFightIsToughAnimals_var true 
		NextWagerFightIsToughAnimals = true
	; 051 : jmp 072
	; 052 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight09_var 
	; 053 : jmpf ::temp25 056
	elseIf NextWagerFight == Fight09
		; 054 : assign ::NextWagerFightIsPeople_var true 
		NextWagerFightIsPeople = true
	; 055 : jmp 072
	; 056 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight10_var 
	; 057 : jmpf ::temp25 060
	elseIf NextWagerFight == Fight10
		; 058 : assign ::NextWagerFightIsExotic_var true 
		NextWagerFightIsExotic = true
	; 059 : jmp 072
	; 060 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight11_var 
	; 061 : jmpf ::temp25 064
	elseIf NextWagerFight == Fight11
		; 062 : assign ::NextWagerFightIsPeople_var true 
		NextWagerFightIsPeople = true
	; 063 : jmp 072
	; 064 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight12_var 
	; 065 : jmpf ::temp25 068
	elseIf NextWagerFight == Fight12
		; 066 : assign ::NextWagerFightIsExotic_var true 
		NextWagerFightIsExotic = true
	; 067 : jmp 072
	; 068 : cmp_eq ::temp25 ::NextWagerFight_var ::Fight13_var 
	; 069 : jmpf ::temp25 072
	elseIf NextWagerFight == Fight13
		; 070 : assign ::NextWagerFightIsPeople_var true 
		NextWagerFightIsPeople = true
	; 071 : jmp 072
	endIf
endFunction

referencealias function GetCombatantAlias(int index)

	;bool ::temp5
	;bool ::temp6
	;referencealias ::temp7
	
	; 000 : cmp_eq ::temp5 index 1 
	; 001 : jmpf ::temp5 004
	if index == 1
		; 002 : return ::Combatant01_var 
		return Combatant01
	; 003 : jmp 042
	; 004 : cmp_eq ::temp6 index 2 
	; 005 : jmpf ::temp6 008
	elseIf index == 2
		; 006 : return ::Combatant02_var 
		return Combatant02
	; 007 : jmp 042
	; 008 : cmp_eq ::temp6 index 3 
	; 009 : jmpf ::temp6 012
	elseIf index == 3
		; 010 : return ::Combatant03_var 
		return Combatant03
	; 011 : jmp 042
	; 012 : cmp_eq ::temp6 index 4 
	; 013 : jmpf ::temp6 016
	elseIf index == 4
		; 014 : return ::Combatant04_var 
		return Combatant04
	; 015 : jmp 042
	; 016 : cmp_eq ::temp6 index 5 
	; 017 : jmpf ::temp6 020
	elseIf index == 5
		; 018 : return ::Combatant05_var 
		return Combatant05
	; 019 : jmp 042
	; 020 : cmp_eq ::temp6 index 6 
	; 021 : jmpf ::temp6 024
	elseIf index == 6
		; 022 : return ::Combatant06_var 
		return Combatant06
	; 023 : jmp 042
	; 024 : cmp_eq ::temp6 index 7 
	; 025 : jmpf ::temp6 028
	elseIf index == 7
		; 026 : return ::Combatant07_var 
		return Combatant07
	; 027 : jmp 042
	; 028 : cmp_eq ::temp6 index 8 
	; 029 : jmpf ::temp6 032
	elseIf index == 8
		; 030 : return ::Combatant08_var 
		return Combatant08
	; 031 : jmp 042
	; 032 : cmp_eq ::temp6 index 9 
	; 033 : jmpf ::temp6 036
	elseIf index == 9
		; 034 : return ::Combatant09_var 
		return Combatant09
	; 035 : jmp 042
	; 036 : cmp_eq ::temp6 index 10 
	; 037 : jmpf ::temp6 040
	elseIf index == 10
		; 038 : return ::Combatant10_var 
		return Combatant10
	; 039 : jmp 042
	else
		; 040 : cast ::temp7 none 
		; 041 : return ::temp7 
		return none
	endIf
endFunction

; Skipped compiler generated GetState

function Setup()

	;arenacombatquest ::temp8
	;NONE ::nonevar
	
	; 000 : assign ::WagerOngoing_var false 
	WagerOngoing = false
	; 001 : cast ::temp8 none 
	; 002 : callmethod PickNextWagerFight self ::nonevar ::temp8 
	self.PickNextWagerFight(none)
endFunction

arenacombatquest function PickNextFight(int offset)

	;actor ::temp38
	;int ::temp39
	;bool ::temp40
	;bool ::temp42
	;arenacombatquest ::temp48
	;arenacombatquest ::temp41
	;bool ::temp43
	;arenacombatquest ::temp44
	;arenacombatquest ::temp45
	;bool ::temp46
	;arenacombatquest ::temp47
	
	; 000 : assign minFight -1 
	int minFight = -1
	; 001 : assign maxFight -1 
	int maxFight = -1
	; 002 : callstatic game GetPlayer ::temp38 
	; 003 : callmethod GetFactionRank ::temp38 ::temp39 ::ArenaFaction_var 
	; 004 : assign playerRank ::temp39 
	int playerRank = game.GetPlayer().GetFactionRank(ArenaFaction)
	; 005 : cmp_lte ::temp40 ::FightsToNextLevel_var 0 
	; 006 : jmpf ::temp40 009
	if FightsToNextLevel <= 0
		; 007 : return ::TransitionFight_var 
		return TransitionFight
	; 008 : jmp 009
	endIf
	; 009 : cmp_eq ::temp40 playerRank 0 
	; 010 : jmpf ::temp40 018
	if playerRank == 0
		; 011 : assign minFight 1 
		minFight = 1
		; 012 : assign maxFight 3 
		maxFight = 3
		; 013 : callstatic utility RandomInt ::temp39 minFight maxFight 
		; 014 : assign fightIndex ::temp39 
		int fightIndex = utility.RandomInt(minFight, maxFight)
		; 015 : callmethod GetFightQuestFromIndex self ::temp41 fightIndex 
		; 016 : return ::temp41 
		return self.GetFightQuestFromIndex(fightIndex)
	; 017 : jmp 077
	; 018 : cmp_eq ::temp42 playerRank 1 
	; 019 : jmpf ::temp42 034
	elseIf playerRank == 1
		; 020 : callstatic utility RandomInt ::temp39 0 2 
		; 021 : cast ::temp43 ::temp39 
		; 022 : assign humanFight ::temp43 
		bool humanFight = utility.RandomInt(0, 2) as bool
		; 023 : not ::temp43 humanFight 
		; 024 : jmpf ::temp43 032
		if !humanFight
			; 025 : assign minFight 2 
			minFight = 2
			; 026 : assign maxFight 3 
			maxFight = 3
			; 027 : callstatic utility RandomInt ::temp39 minFight maxFight 
			; 028 : assign ::mangled_fightindex_0 ::temp39 
			int fightindex = utility.RandomInt(minFight, maxFight)
			; 029 : callmethod GetFightQuestFromIndex self ::temp44 ::mangled_fightindex_0 
			; 030 : return ::temp44 
			return self.GetFightQuestFromIndex(fightindex)
		; 031 : jmp 033
		else
			; 032 : return ::Fight04_var 
			return Fight04
		endIf
	; 033 : jmp 077
	; 034 : cmp_eq ::temp43 playerRank 2 
	; 035 : jmpf ::temp43 043
	elseIf playerRank == 2
		; 036 : assign minFight 5 
		minFight = 5
		; 037 : assign maxFight 9 
		maxFight = 9
		; 038 : callstatic utility RandomInt ::temp39 minFight maxFight 
		; 039 : assign ::mangled_fightindex_1 ::temp39 
		int fightindex = utility.RandomInt(minFight, maxFight)
		; 040 : callmethod GetFightQuestFromIndex self ::temp45 ::mangled_fightindex_1 
		; 041 : return ::temp45 
		return self.GetFightQuestFromIndex(fightindex)
	; 042 : jmp 077
	; 043 : cmp_eq ::temp42 playerRank 3 
	; 044 : jmpf ::temp42 062
	elseIf playerRank == 3
		; 045 : callstatic utility RandomInt ::temp39 0 2 
		; 046 : assign animalFight ::temp39 
		int animalFight = utility.RandomInt(0, 2)
		; 047 : cmp_eq ::temp43 animalFight 0 
		; 048 : jmpf ::temp43 060
		if animalFight == 0
			; 049 : assign minFight 7 
			minFight = 7
			; 050 : assign maxFight 9 
			maxFight = 9
			; 051 : callstatic utility RandomInt ::temp39 minFight maxFight 
			; 052 : assign ::mangled_fightindex_2 ::temp39 
			int fightindex = utility.RandomInt(minFight, maxFight)
			; 053 : cmp_eq ::temp46 ::mangled_fightindex_2 9 
			; 054 : jmpf ::temp46 057
			if fightindex == 9
				; 055 : assign ::mangled_fightindex_2 10 
				fightindex = 10
			; 056 : jmp 057
			endIf
			; 057 : callmethod GetFightQuestFromIndex self ::temp47 ::mangled_fightindex_2 
			; 058 : return ::temp47 
			return self.GetFightQuestFromIndex(fightindex)
		; 059 : jmp 061
		else
			; 060 : return ::Fight11_var 
			return Fight11
		endIf
	; 049 : assign minFight 7 
	else
		; 062 : callstatic utility RandomInt ::temp39 1 10 
		; 063 : assign fightRoll ::temp39 
		int fightRoll = utility.RandomInt(1, 10)
		; 064 : cmp_lte ::temp46 fightRoll 3 
		; 065 : jmpf ::temp46 072
		if fightRoll <= 3
			; 066 : callstatic utility RandomInt ::temp39 0 1 
			; 067 : jmpf ::temp39 070
			if utility.RandomInt(0, 1)
				; 068 : return ::Fight08_var 
				return Fight08
			; 069 : jmp 071
			else
				; 070 : return ::Fight10_var 
				return Fight10
			endIf
		; 071 : jmp 077
		; 072 : cmp_lte ::temp43 fightRoll 9 
		; 073 : jmpf ::temp43 076
		elseIf fightRoll <= 9
			; 074 : return ::Fight13_var 
			return Fight13
		; 075 : jmp 077
		else
			; 076 : return ::Fight12_var 
			return Fight12
		endIf
	endIf
	; 077 : cast ::temp48 none 
	; 078 : return ::temp48 
	return none
endFunction
</pre>
</div>

<p>Decompiling a whole directory in a subdirectory, in parallel mode</p>
<div class="command-line">Champollion.exe bsa\out\scripts -p decompiled -t &gt; output.txt</div>
<div class="psc-sample">
<span class="sample">Extract of output.txt</span>
<pre>
...
bsa\out\scripts\wiremoveitem01script.pex decompiled to decompiled\wiremoveitem01script.psc
bsa\out\scripts\wiremoveitem02itemscript.pex decompiled to decompiled\wiremoveitem02itemscript.psc
bsa\out\scripts\wiremoveitem02script.pex decompiled to decompiled\wiremoveitem02script.psc
bsa\out\scripts\wiremoveitem03bystanderscript.pex decompiled to decompiled\wiremoveitem03bystanderscript.psc
bsa\out\scripts\wiremoveitem03script.pex decompiled to decompiled\wiremoveitem03script.psc
bsa\out\scripts\wiremoveitem04script.pex decompiled to decompiled\wiremoveitem04script.psc
bsa\out\scripts\wiremoveitem05itemscript.pex decompiled to decompiled\wiremoveitem05itemscript.psc
bsa\out\scripts\wiremoveitem05script.pex decompiled to decompiled\wiremoveitem05script.psc
bsa\out\scripts\wisabotage.pex decompiled to decompiled\wisabotage.psc
bsa\out\scripts\wiskillincrease02.pex decompiled to decompiled\wiskillincrease02.psc
bsa\out\scripts\wispactorscript.pex decompiled to decompiled\wispactorscript.psc
bsa\out\scripts\wispcorescript.pex decompiled to decompiled\wispcorescript.psc
bsa\out\scripts\wispshadeactorscript.pex decompiled to decompiled\wispshadeactorscript.psc
bsa\out\scripts\witavernplayerscript.pex decompiled to decompiled\witavernplayerscript.psc
bsa\out\scripts\witavernscript.pex decompiled to decompiled\witavernscript.psc
bsa\out\scripts\witchlightactorscript.pex decompiled to decompiled\witchlightactorscript.psc
bsa\out\scripts\witestscript.pex decompiled to decompiled\witestscript.psc
bsa\out\scripts\withief01script.pex decompiled to decompiled\withief01script.psc
bsa\out\scripts\withief01thiefscript.pex decompiled to decompiled\withief01thiefscript.psc
bsa\out\scripts\withiefscript.pex decompiled to decompiled\withiefscript.psc
bsa\out\scripts\woodchoppingscript.pex decompiled to decompiled\woodchoppingscript.psc
bsa\out\scripts\woodpilescript.pex decompiled to decompiled\woodpilescript.psc
bsa\out\scripts\wordofpower.pex decompiled to decompiled\wordofpower.psc
bsa\out\scripts\wordwalllistenerquestscript.pex decompiled to decompiled\wordwalllistenerquestscript.psc
bsa\out\scripts\wordwalltrigger02script.pex decompiled to decompiled\wordwalltrigger02script.psc
bsa\out\scripts\wordwalltriggerbleakfallsscript.pex decompiled to decompiled\wordwalltriggerbleakfallsscript.psc
bsa\out\scripts\wordwalltriggerscript.pex decompiled to decompiled\wordwalltriggerscript.psc
bsa\out\scripts\worldinteractionsscript.pex decompiled to decompiled\worldinteractionsscript.psc
bsa\out\scripts\worldspace.pex decompiled to decompiled\worldspace.psc
bsa\out\scripts\woundrefonload.pex decompiled to decompiled\woundrefonload.psc
bsa\out\scripts\wrdrawbridge01script.pex decompiled to decompiled\wrdrawbridge01script.psc
bsa\out\scripts\wuuthradscript.pex decompiled to decompiled\wuuthradscript.psc
10026 files processed in 2.49614 s
</pre>
</div>

<h1>Limitations</h1>
<p>Champollion works by detecting the pattern used by the Papyrus compiler in the compilation process.
So it only works correctly with files produced by the compiler provided by Bethesda (Not that there are others out there).</p>
<p>The Event and Function are not distinguished in the PEX binary, so all Event are decompiled as Function. It doesn't seem to be a problem to recompile correctly the script.</p>
<p>The assembly produced by the -a flag is only intended to serve as references, and will not work with the PapyrusAssembler tool.</p>

<h1>Thanks</h1>
<ul>
<li>Bethesda for game as fun to play as to mod and tweak.</li>
<li>The folks at <a href="http://www.uesp.net">The UESPWiki</a> for the PEX binary format description</li>
<li>The people of <a href="http://http://skyrim.nexusmods.com">NexusMod</a> for giving me a lot of new mods to play with.</li>
<li>steklok for pointing out a problem with the array.find and array.rfind functions</li>
</ul>

<h1>Further reading</h1>
<ul>
<li><a href="http://www.creationkit.com/Category:Papyrus">Papyrus Reference</a></li>
<li><a href="http://www.uesp.net/wiki/Tes5Mod:Compiled_Script_File_Format">Tes5Mod:Compiled Script File Format</a></li>
</body>

</html>
```

## File: `Doc/readme.css`
```css


body {
	font-size: 14px;
}


h1 {
	font-size: 18px;
}

h2 {
	font-size: 16px;
	margin-left: 4ex;
}

.command-line {
	background-color: lightgrey;
	border: 2px solid black;
	padding: 3px;
}

.file {
	font-style: italic;
}

table {
	border: 2px solid black;
	border-collapse: collapse;
}

td {
	border: 1px solid black;
}

th {
	border: 1px solid black;
}

.psc-sample {
	border: 2px solid black;
	background-color: lightyellow;
	margin-top: 2px;
	margin-bottom: 2px;	
}

.psc-sample .sample {
	text-align: center;
	font-weight: bold;
}
.psc-sample pre{
	overflow: auto;
	height: 20em;
}

.output {
	border: 1px solid black;
	background-color: lightgray;
	margin-top: 2px;
	margin-bottom: 2px;
}

```

## File: `Pex/Binary.cpp`
```cpp
#include "Binary.hpp"

#include <algorithm>
#include <iostream>

#include "FileReader.hpp"
/**
 * @brief Default constructor.
 *
 * This constructor provides a Binary file with empty elements.
 */
Pex::Binary::Binary():
    m_ScriptType(Unknown)
{
}

/**
 * @brief Default destructor.
 *
 */
Pex::Binary::~Binary()
{
}

/**
 * @brief Retrieve the Header part of the Binary
 *
 * @return a const Header.
 */
const Pex::Header &Pex::Binary::getHeader() const
{
    return m_Header;
}

/**
 * @brief Retrieve the Header part of the Binary
 *
 * @return a modifiable Header.
 */
Pex::Header &Pex::Binary::getHeader()
{
    return m_Header;
}

/**
 * @brief Retrieve the StringTable associated with the Binary
 *
 * @return a const string table.
 */
const Pex::StringTable &Pex::Binary::getStringTable() const
{
    return m_StringTable;
}

/**
 * @brief Retrieve the StringTable associated with the Binary
 *
 * @return a modifiable string table.
 */
Pex::StringTable &Pex::Binary::getStringTable()
{
    return m_StringTable;
}

/**
 * @brief Retrieve the debug info associated with the Binary.
 *
 * @return a const DebugInfo
 */
const Pex::DebugInfo &Pex::Binary::getDebugInfo() const
{
    return m_DebugInfo;
}

/**
 * @brief Retrieve the debug info associated with the Binary.
 *
 * @return a modifiable DebugInfo
 */
Pex::DebugInfo &Pex::Binary::getDebugInfo()
{
    return m_DebugInfo;
}

/**
 * @brief Retrieve the user flags definition stored in the Binary
 *
 * @return a const UserFlags;
 */
const Pex::UserFlags &Pex::Binary::getUserFlags() const
{
    return m_UserFlags;
}

/**
 * @brief Retrieve the user flags definition stored in the Binary
 *
 * @return a modifiable UserFlags;
 */
Pex::UserFlags &Pex::Binary::getUserFlags()
{
    return m_UserFlags;
}

/**
 * @brief Retrieve the list of Objects defined in the Binary
 *
 * @return a const Objects.
 */
const Pex::Objects &Pex::Binary::getObjects() const
{
    return m_Objects;
}

/**
 * @brief Retrieve the list of Objects defined in the Binary
 *
 * @return a modifiable Objects.
 */
Pex::Objects &Pex::Binary::getObjects()
{
    return m_Objects;
}

Pex::Binary::ScriptType Pex::Binary::getGameType() const
{
    return m_ScriptType;
}

void Pex::Binary::setScriptType(Pex::Binary::ScriptType game_type)
{
    m_ScriptType = game_type;
}

static bool namedLessThan(const Pex::NamedItem& a, const Pex::NamedItem& b) {
    return a.getName().asString() < b.getName().asString();
}

void Pex::Binary::sort() {
    std::sort(m_Objects.begin(), m_Objects.end(), namedLessThan);
    std::sort(m_UserFlags.begin(), m_UserFlags.end(), namedLessThan);
    for (auto& obj : m_Objects) {
        std::sort(obj.getGuards().begin(), obj.getGuards().end(), namedLessThan);
        std::sort(obj.getProperties().begin(), obj.getProperties().end(), namedLessThan);
        std::sort(obj.getStates().begin(), obj.getStates().end(), namedLessThan);
        std::sort(obj.getStructInfos().begin(), obj.getStructInfos().end(), namedLessThan);
        std::sort(obj.getVariables().begin(), obj.getVariables().end(), namedLessThan);

        for (auto& state : obj.getStates()) {
            std::sort(state.getFunctions().begin(), state.getFunctions().end(), [this, obj, state](const Pex::Function& a, const Pex::Function& b) {
                auto linesA = this->getDebugInfo().getFunctionInfo(obj.getName(), state.getName(), a.getName());
                auto lA = !linesA || linesA->getLineNumbers().empty() ? 0 : linesA->getLineNumbers()[0];
                auto linesB = this->getDebugInfo().getFunctionInfo(obj.getName(), state.getName(), b.getName());
                auto lB = !linesB || linesB->getLineNumbers().empty() ? 0 : linesB->getLineNumbers()[0];
                if (lA == lB) {
                    return a.getName().asString() < b.getName().asString();
                }
                return lA < lB;
            });
        }
    }
}
```

## File: `Pex/Binary.hpp`
```
#pragma once

#include <string>

#include "Header.hpp"
#include "StringTable.hpp"
#include "DebugInfo.hpp"
#include "UserFlag.hpp"
#include "Object.hpp"

namespace Pex {

/**
 * @brief Pex main data structure
 *
 * The Binary class reflect the content of a PEX file.
 *
 */
class FileReader;
class Binary
{
public:
    enum ScriptType {
        Unknown = -1,
        SkyrimScript,
        Fallout4Script,
        Fallout76Script,
        StarfieldScript
    };
    Binary();
    virtual ~Binary();

    const Header& getHeader() const;
    Header& getHeader();

    const StringTable& getStringTable() const;
    StringTable& getStringTable();

    const DebugInfo& getDebugInfo() const;
    DebugInfo& getDebugInfo();

    const UserFlags& getUserFlags() const;
    UserFlags& getUserFlags();

    const Objects& getObjects() const;
    Objects& getObjects();

    ScriptType getGameType() const;

    void sort();
    
protected:
    friend FileReader;
    void setScriptType(ScriptType game_type);
    Header m_Header;
    StringTable m_StringTable;
    DebugInfo m_DebugInfo;
    UserFlags m_UserFlags;
    Objects m_Objects;
    ScriptType m_ScriptType;
};
}
```

## File: `Pex/ByteSwap.hpp`
```
#include <type_traits>
#include <cassert>
// These are backported from STL C++23

constexpr uint16_t _Byteswap_ushort(const uint16_t _Val) noexcept {
        return static_cast<unsigned short>((_Val << 8) | (_Val >> 8));
}

constexpr uint32_t _Byteswap_ulong(const uint32_t _Val) noexcept {
        return (_Val << 24) | ((_Val << 8) & 0x00FF'0000) | ((_Val >> 8) & 0x0000'FF00) | (_Val >> 24);
}

constexpr uint64_t _Byteswap_uint64(const uint64_t _Val) noexcept {
        return (_Val << 56) | ((_Val << 40) & 0x00FF'0000'0000'0000) | ((_Val << 24) & 0x0000'FF00'0000'0000)
             | ((_Val << 8) & 0x0000'00FF'0000'0000) | ((_Val >> 8) & 0x0000'0000'FF00'0000)
             | ((_Val >> 24) & 0x0000'0000'00FF'0000) | ((_Val >> 40) & 0x0000'0000'0000'FF00) | (_Val >> 56);
}

template <class... T>
constexpr bool _always_false_assert = false;

template <typename Integer, typename = std::enable_if_t<std::is_integral<Integer>::value>>
constexpr Integer byteswap(const Integer _Val) noexcept {
    if constexpr (sizeof(Integer) == 1) {
        return _Val;
    } else if constexpr (sizeof(Integer) == 2) {
        return static_cast<Integer>(_Byteswap_ushort(static_cast<uint16_t>(_Val)));
    } else if constexpr (sizeof(Integer) == 4) {
        return static_cast<Integer>(_Byteswap_ulong(static_cast<uint32_t>(_Val)));
    } else if constexpr (sizeof(Integer) == 8) {
        return static_cast<Integer>(_Byteswap_uint64(static_cast<uint64_t>(_Val)));
    } else {
        static_assert(_always_false_assert<Integer>, "Unexpected integer size");
    }
}

float byteswap_float(const float _Val) noexcept {
    float retVal;
    const auto pVal = reinterpret_cast<const char*>(& _Val);
    const auto pRetVal = reinterpret_cast<char*>(& retVal);
    const std::size_t size = sizeof(float);
    assert(size == 4);
    for (std::size_t i = 0; i < size; i++)
    {
        pRetVal[size - 1 - i] = pVal[i];
    }
    return retVal;
}
```

## File: `Pex/CMakeLists.txt`
```
file(GLOB HEADER_FILES "*.hpp")
file(GLOB SOURCE_FILES "*.cpp")

add_library(Pex STATIC ${HEADER_FILES} ${SOURCE_FILES})
auto_source_group("Pex" ${CMAKE_CURRENT_SOURCE_DIR} ${HEADER_FILES} ${SOURCE_FILES})
```

## File: `Pex/DebugInfo.cpp`
```cpp
#include "DebugInfo.hpp"

#include <algorithm>

/**
 * @brief Default constructor
 *
 * Creates an empty debug info object
 */
Pex::DebugInfo::DebugInfo() :
    m_ModificationTime(0)
{
}

/**
 * @brief Default desctrutor
 *
 */
Pex::DebugInfo::~DebugInfo()
{
}

/**
 * @brief Retrieve the modification time of the original source file.
 *
 * The modification time is 0 if no debug information are defined in the PEX file.
 *
 * @return the original modification time.
 */
const std::time_t &Pex::DebugInfo::getModificationTime() const
{
    return m_ModificationTime;
}

/**
 * @brief Sets the modification time of the original source file.
 *
 * @param[in] value Modification time to set.
 */
void Pex::DebugInfo::setModificationTime(const std::time_t &value)
{
    m_ModificationTime = value;
}

/**
 * @brief Retrieve the function info list.
 *
 * @return a const FunctionInfo collection.
 */
const Pex::DebugInfo::FunctionInfos &Pex::DebugInfo::getFunctionInfos() const
{
    return m_FunctionInfo;
}

/**
 * @brief Retrieve the function info list.
 *
 * @return a modifiable FunctionInfo collection.
 */
Pex::DebugInfo::FunctionInfos &Pex::DebugInfo::getFunctionInfos()
{
    return m_FunctionInfo;
}

/**
 * @brief Get the function info for a given function.
 * @param object Name of the object containing the function.
 * @param state Name of the state containing the function.
 * @param name Name of the function.
 * @param type Type of the function (0 normal function, 1 for property getter, 2 for property setter)
 * @return A pointer to the function infos, nulltpr if not found.
 */
const Pex::DebugInfo::FunctionInfo* Pex::DebugInfo::getFunctionInfo(const Pex::StringTable::Index &object, const Pex::StringTable::Index &state, const Pex::StringTable::Index &name, FunctionType type) const
{
    auto it = std::find_if(m_FunctionInfo.begin(), m_FunctionInfo.end(), [&] (FunctionInfos::const_reference item) {
            return item.getObjectName() == object && item.getStateName() == state && item.getFunctionName() == name && item.getFunctionType() == type;
    });
    if (it == m_FunctionInfo.end())
    {
        return nullptr;
    }
    return &(*it);
}



/**
 * @brief Default constructor
 */
Pex::DebugInfo::FunctionInfo::FunctionInfo()
{
}

/**
 * @brief Default Destructor.
 */
Pex::DebugInfo::FunctionInfo::~FunctionInfo()
{
}

/**
 * @brief Retrieve the object name associated with this function debug info
 * @return the string index of the object's name
 */
Pex::StringTable::Index Pex::DebugInfo::FunctionInfo::getObjectName() const
{
    return m_ObjectName;
}

/**
 * @brief Sets the name of the object associated with this function debug info
 *
 * @param[in] value String index of the object's name.
 */
void Pex::DebugInfo::FunctionInfo::setObjectName(StringTable::Index value)
{
    m_ObjectName = value;
}

/**
 * @brief Retrieve the state name associated with this function debug info
 * @return the string index of the state's name
 */
Pex::StringTable::Index Pex::DebugInfo::FunctionInfo::getStateName() const
{
    return m_StateName;
}

/**
 * @brief Sets the name of the state associated with this function debug info
 *
 * @param[in] value String index of the state's name.
 */
void Pex::DebugInfo::FunctionInfo::setStateName(StringTable::Index value)
{
    m_StateName = value;
}

/**
 * @brief Retrieve the function name associated with this function debug info
 * @return the string index of the function's name
 */
Pex::StringTable::Index Pex::DebugInfo::FunctionInfo::getFunctionName() const
{
    return m_FunctionName;
}

/**
 * @brief Sets the name of the function associated with this function debug info
 *
 * @param[in] value String index of the function's name.
 */
void Pex::DebugInfo::FunctionInfo::setFunctionName(StringTable::Index value)
{
    m_FunctionName = value;
}

/**
 * @brief Retrieve the type of the function
 *
 * @return the type of the function
 */
Pex::DebugInfo::FunctionType Pex::DebugInfo::FunctionInfo::getFunctionType() const
{
    return m_FunctionType;
}

/**
 * @brief Sets the type of the function
 *
 * @param[in] value Type of the function
 *
 * @todo extract an enum
 */
void Pex::DebugInfo::FunctionInfo::setFunctionType(FunctionType value)
{
    m_FunctionType  = value;
}

/**
 * @brief Retrieve the line number array
 * Each entry match a bytecode instruction in the function body.
 *
 * @return the const line number array;
 */
const Pex::DebugInfo::FunctionInfo::LineNumbers &Pex::DebugInfo::FunctionInfo::getLineNumbers() const
{
    return m_LineNumbers;
}
/**
 * @brief Retrieve the line number array
 * Each entry match a bytecode instruction in the function body.
 *
 * @return the modifiable line number array;
 */
Pex::DebugInfo::FunctionInfo::LineNumbers &Pex::DebugInfo::FunctionInfo::getLineNumbers()
{
    return m_LineNumbers;
}

std::vector<uint16_t> Pex::DebugInfo::FunctionInfo::getLineNumbersForIpRange(int64_t begin, int64_t end) const {
  if (begin < 0 || end < 0){
    return {};
  }
  // no debug info
  if (m_LineNumbers.empty() || begin > m_LineNumbers.size() - 1) {
    return {};
  }
  std::vector<uint16_t> result;
  int64_t line = -1;
  for (auto i = begin; i <= end; ++i)
  {
    if (i < m_LineNumbers.size() && std::find(result.begin(), result.end(), m_LineNumbers[i]) == result.end())
    {
      result.push_back(m_LineNumbers[i]);
    }
  }
  return result;
}


```

## File: `Pex/DebugInfo.hpp`
```
#pragma once

#include <ctime>
#include <cstdint>
#include <vector>

#include "DocumentedItem.hpp"
#include "StringTable.hpp"
#include "UserFlagged.hpp"

namespace Pex {

/**
 * @brief Debug Information
 *
 * The DebugInfo class describe the debug information associated with objects and function.
 * For the file, the only data is the source file modification time.
 * For each function available in the object, the original source line number are also available.
 *
 */
class DebugInfo
{
public:

    /**
     * @brief Function type
     *
     */
    enum class FunctionType : std::uint8_t
    {
        /// Standard method
        Method = 0,
        /// Property getter function
        Getter = 1,
        /// Property setter function
        Setter = 2
    };

    /**
     * @brief Debug information subset
     *
     * The FunctionInfo describer the debug information associated with a specific
     * function, referenced by objet, state and name.
     *
     */
    class FunctionInfo
    {
    public:
        typedef std::vector<std::uint16_t> LineNumbers;

    public:
        FunctionInfo();
        ~FunctionInfo();

        StringTable::Index getObjectName() const;
        void setObjectName(StringTable::Index value);

        StringTable::Index getStateName() const;
        void setStateName(StringTable::Index value);

        StringTable::Index getFunctionName() const;
        void setFunctionName(StringTable::Index value);

        FunctionType getFunctionType() const;
        void setFunctionType(FunctionType);

        const LineNumbers& getLineNumbers() const;
        LineNumbers& getLineNumbers();
        std::vector<uint16_t> getLineNumbersForIpRange(int64_t begin, int64_t end) const;

     private:
        StringTable::Index m_ObjectName;
        StringTable::Index m_StateName;
        StringTable::Index m_FunctionName;
        FunctionType m_FunctionType;

        LineNumbers m_LineNumbers;
    };

    class PropertyGroup :
            public DocumentedItem,
            public UserFlagged
    {
    public:
        typedef std::vector<StringTable::Index> Names;

    public:
        PropertyGroup() = default;
        ~PropertyGroup() = default;

        StringTable::Index getObjectName() const { return m_ObjectName; }
        void setObjectName(StringTable::Index value) { m_ObjectName = value; }

        StringTable::Index getGroupName() const { return m_GroupName; }
        void setGroupName(StringTable::Index value) { m_GroupName = value; }

        const Names& getNames() const { return m_Names; }
        Names& getNames() { return m_Names; }

     private:
        StringTable::Index m_ObjectName;
        StringTable::Index m_GroupName;

        Names m_Names;
    };

    class StructOrder
    {
    public:
        typedef std::vector<StringTable::Index> Names;

    public:
        StructOrder() = default;
        ~StructOrder() = default;

        StringTable::Index getObjectName() const { return m_ObjectName; }
        void setObjectName(StringTable::Index value) { m_ObjectName = value; }

        StringTable::Index getOrderName() const { return m_OrderName; }
        void setOrderName(StringTable::Index value) { m_OrderName = value; }

        const Names& getNames() const { return m_Names; }
        Names& getNames() { return m_Names; }

     private:
        StringTable::Index m_ObjectName;
        StringTable::Index m_OrderName;

        Names m_Names;
    };

    typedef std::vector<FunctionInfo> FunctionInfos;
    typedef std::vector<PropertyGroup> PropertyGroups;
    typedef std::vector<StructOrder> StructOrders;
public:
    DebugInfo();
    ~DebugInfo();

    const std::time_t& getModificationTime() const;
    void setModificationTime(const std::time_t& value);

    const FunctionInfos& getFunctionInfos() const;
    FunctionInfos& getFunctionInfos();

    const PropertyGroups& getPropertyGroups() const { return m_PropertyGroup; }
    PropertyGroups& getPropertyGroups() { return m_PropertyGroup; }

    const StructOrders& getStructOrders() const { return m_StructOrder; }
    StructOrders& getStructOrders() { return m_StructOrder; }

    const FunctionInfo *getFunctionInfo(const StringTable::Index& object, const StringTable::Index& state, const StringTable::Index& name, FunctionType type = FunctionType::Method) const;

private:
    std::time_t m_ModificationTime;
    FunctionInfos m_FunctionInfo;
    PropertyGroups m_PropertyGroup;
    StructOrders m_StructOrder;
};
}
```

## File: `Pex/DocumentedItem.cpp`
```cpp
#include "DocumentedItem.hpp"

#include <cassert>

/**
 * @brief Default constructor
 *
 */
Pex::DocumentedItem::DocumentedItem()
{
}

/**
 * @brief Default destructor
 *
 */
Pex::DocumentedItem::~DocumentedItem()
{
}

/**
 * @brief Retrieve the document string describing the item.
 *
 * @return the docstring index.
 */
Pex::StringTable::Index Pex::DocumentedItem::getDocString() const
{
    return m_DocString;
}

/**
 * @brief Sets the document string describing the item.
 * @param[in] value Index of the docstring
 */
void Pex::DocumentedItem::setDocString(Pex::StringTable::Index value)
{
    assert(value.isValid());
    m_DocString = value;
}
```

## File: `Pex/DocumentedItem.hpp`
```
#pragma once

#include <cstdint>

#include "StringTable.hpp"

namespace Pex {
/**
 * @brief Base mixin for documented items, such as property or functions
 *
 */
class DocumentedItem
{
public:
    DocumentedItem();
    virtual ~DocumentedItem();

    StringTable::Index getDocString() const;
    void setDocString(StringTable::Index value);

protected:
    StringTable::Index m_DocString;
};
}
```

## File: `Pex/FileReader.cpp`
```cpp
#include "FileReader.hpp"
#include "ByteSwap.hpp"

#include <iostream>
#include <sstream>
#include <iomanip>

#include <cassert>

/**
 * @brief Construct from file name
 * @param[in] fileName name of the pex file.
 *
 * @throws runtime_error if the file can't be openened
 */
Pex::FileReader::FileReader(const std::string &fileName) :
    m_fileStream(fileName, std::ifstream::binary),
    m_StringTable(nullptr)
{    
    m_iStream = &m_fileStream;
    if (m_iStream->fail())
    {
        throw std::runtime_error("Unable to open file");
    }
}

/**
 * @brief Construct from istream
 * @param[in] stream pointer to istream.
 *
 * @throws runtime_error if the istream is bad
 */
Pex::FileReader::FileReader(std::istream *stream):
    m_iStream(stream),
    m_StringTable(nullptr),
    m_fileStream()
{
    if (m_iStream->fail())
    {
        throw std::runtime_error("istream is bad");
    }
}

/**
 * @brief Default destructor
 */
Pex::FileReader::~FileReader()
{
}

/**
 * @brief Fills in the binary structure with the data read from the associated file input.
 * @param[out] binary Structure to be filed in
 *
 * @throws runtime_error if the structure of the file is incorrect.
 */
void Pex::FileReader::read(Pex::Binary &binary)
{
    readHeader(binary.getHeader());
    if (m_endianness == Big) {
        binary.setScriptType(Pex::Binary::ScriptType::SkyrimScript);
    } else { // Little
        auto header = binary.getHeader();
        if (header.getGameID() == 4) {
            binary.setScriptType(Pex::Binary::ScriptType::StarfieldScript);
        } else if(header.getGameID() == 3) {
            binary.setScriptType(Pex::Binary::ScriptType::Fallout76Script);
        } else {
            binary.setScriptType(Pex::Binary::ScriptType::Fallout4Script);
        }
    }
    read(binary.getStringTable());
    m_StringTable = & binary.getStringTable();
    read(binary.getDebugInfo());
    read(binary.getUserFlags());
    std::vector<std::string> userFlagsstrs;
    for (auto &flag : binary.getUserFlags())
    {
        userFlagsstrs.push_back(flag.getName().asString());
    }
    read(binary.getGameType(), binary.getObjects());
}

/**
 * @brief Reads the Header from the file
 * @param[in] header Header to fill in
 *
 */
void Pex::FileReader::readHeader(Pex::Header &header)
{
    // read magic as little endian to determine what endianness to set
    auto magic = getUint32(true);

    // Little Endian = Fallout 4
    // Has new PEX format with const, struct info, more debug info
    if (magic != LE_MAGIC_NUMBER)
    {
        // Big Endian = Skyrim scripts
        // Has old Skyrim PEX format
        if (magic != BE_MAGIC_NUMBER) {
            throw std::runtime_error("Invalid file magic");
        }
        m_endianness = Big;
    } else {
        m_endianness = Little;
    }
    header.setMajorVersion(getUint8());
    header.setMinorVersion(getUint8());
    header.setGameID(getUint16());
    header.setCompilationTime(getTime());
    header.setSourceFileName(getString());
    header.setUserName(getString());
    header.setComputerName(getString());

}

/**
 * @brief Reads the string table from the file.
 * @param[in] stringTable table to fill in
 */
void Pex::FileReader::read(Pex::StringTable &stringTable)
{
    auto len = getUint16();
    stringTable.reserve(len);

    for(auto i = 0; i < len; ++i)
    {
        stringTable.push_back(getString());
    }

}
/**
 * @brief Reads the debug info package
 * @param[in] debugInfo DebugInfo object to fill in.
 */
void Pex::FileReader::read(Pex::DebugInfo &debugInfo)
{
    auto hasDebugInfo = getUint8();
    if(hasDebugInfo)
    {
        debugInfo.setModificationTime(getTime());

        auto functionCount = getUint16();
        auto& functionInfos = debugInfo.getFunctionInfos();
        functionInfos.resize(functionCount);
        for (auto& functionInfo : functionInfos)
        {
            functionInfo.setObjectName(getStringIndex());
            functionInfo.setStateName(getStringIndex());
            functionInfo.setFunctionName(getStringIndex());
            functionInfo.setFunctionType(static_cast<DebugInfo::FunctionType>(getUint8()));
            auto instructionCount = getUint16();
            auto& lineNumbers = functionInfo.getLineNumbers();
            lineNumbers.reserve(instructionCount);
            for (auto l  = 0; l < instructionCount; ++l)
            {
                lineNumbers.push_back(getUint16());
            }
        }
        // Skyrim scripts do not have the following info
        if (m_endianness == Big){
            return;
        }
        auto groupCount = getUint16();
        auto& propertyGroups = debugInfo.getPropertyGroups();
        propertyGroups.resize(groupCount);
        for (auto& propertyGroup : propertyGroups)
        {
            propertyGroup.setObjectName(getStringIndex());
            propertyGroup.setGroupName(getStringIndex());
            propertyGroup.setDocString(getStringIndex());
            propertyGroup.setUserFlags(getUint32());
            auto nameCount = getUint16();
            auto& names = propertyGroup.getNames();
            names.reserve(nameCount);
            for (auto l  = 0; l < nameCount; ++l)
            {
                names.push_back(getStringIndex());
            }
        }

        auto orderCount = getUint16();
        auto& structOrders = debugInfo.getStructOrders();
        structOrders.resize(orderCount);
        for (auto& structOrder : structOrders)
        {
            structOrder.setObjectName(getStringIndex());
            structOrder.setOrderName(getStringIndex());
            auto nameCount = getUint16();
            auto& names = structOrder.getNames();
            names.reserve(nameCount);
            for (auto l  = 0; l < nameCount; ++l)
            {
                names.push_back(getStringIndex());
            }
        }
    }
}

/**
 * @brief Reads the User Flags definition from the file.
 * @param[in] userFlags UserFlag collection to fill in.
 */
void Pex::FileReader::read(Pex::UserFlags &userFlags)
{
    auto count = getUint16();
    userFlags.resize(count);
    for (auto& userFlag : userFlags)
    {
        userFlag.setName(getStringIndex());
        userFlag.setFlagIndex(getUint8());
    }
}

/**
 * @brief Reads the Objects definitions from the file.
 * @param[in] script_type The type of script being decompiled.
 * @param[in] objects Object collection to fill in.
 */
void Pex::FileReader::read(const Pex::Binary::ScriptType script_type, Pex::Objects &objects)
{
    auto count = getUint16();
    objects.resize(count);

    for(auto& object : objects)
    {
        object.setName(getStringIndex());
        (void)getUint32();

        object.setParentClassName(getStringIndex());
        object.setDocString(getStringIndex());
        // Skyrim scripts do not have this info 
        if (m_endianness == Little) {
            object.setConstFlag(getUint8());
        }
        object.setUserFlags(getUint32());
        object.setAutoStateName(getStringIndex());
        // Skyrim scripts do not have this info 
        if (m_endianness == Little) {
            read(object.getStructInfos());
        }
        read(object.getVariables());
        if (script_type == Pex::Binary::ScriptType::StarfieldScript) {
            read(object.getGuards());
        }
        read(object.getProperties());
        read(object.getStates());
    }
}

/**
 * @brief Reads the StructInfos definition for an object
 * @param[in] struct info collection to fill in.
 */
void Pex::FileReader::read(Pex::StructInfos &structInfos)
{
    auto infoCount = getUint16();
    structInfos.resize(infoCount);
    for(auto& info : structInfos)
    {
        info.setName(getStringIndex());

        auto memberCount = getUint16();
        auto& members = info.getMembers();
        members.resize(memberCount);
        for (auto& member : members)
        {
            member.setName(getStringIndex());
            member.setTypeName(getStringIndex());
            member.setUserFlags(getUint32());
            member.setValue(getValue());
            member.setConstFlag(getUint8());
            member.setDocString(getStringIndex());
        }
    }
}

/**
 * @brief Reads the Variables definition for an object
 * @param[in] variables collection to fill in.
 */
void Pex::FileReader::read(Pex::Variables &variables)
{
    auto variableCount = getUint16();
    variables.resize(variableCount);
    for(auto& variable : variables)
    {
        variable.setName(getStringIndex());
        variable.setTypeName(getStringIndex());
        variable.setUserFlags(getUint32());

        variable.setDefaultValue(getValue());
        // Skyrim scripts do not have this info 
        if (m_endianness == Little) {
            variable.setConstFlag(getUint8());
        }
    }
}

/**
 * @brief Reads the Properties definition for an object
 * @param[in] properties collection to fill in.
 */
void Pex::FileReader::read(Pex::Properties &properties)
{
    auto propertyCount = getUint16();
    properties.resize(propertyCount);
    for(auto& property : properties)
    {
        property.setName(getStringIndex());
        property.setTypeName(getStringIndex());
        property.setDocString(getStringIndex());
        property.setUserFlags(getUint32());
        property.setFlags(static_cast<PropertyFlag>(getUint8()));
        if(property.hasAutoVar())
        {
            property.setAutoVarName(getStringIndex());
        }
        else
        {
            if (property.isReadable())
            {
                read(property.getReadFunction());
            }
            if(property.isWritable())
            {
                read(property.getWriteFunction());
            }
        }
    }
}

/**
 * @brief Reads the States definition for an object
 * @param[in] states collection to fill in.
 */
void Pex::FileReader::read(Pex::States &states)
{
    auto stateCount = getUint16();
    states.resize(stateCount);
    for(auto& state : states)
    {
        state.setName(getStringIndex());
        read(state.getFunctions());
    }
}

/**
 * @brief Reads the Guards definition for an object
 * @param[in] guards collection to fill in.
 */
void Pex::FileReader::read(Pex::Guards& guards) {
    auto guardCount = getUint16();
    guards.resize(guardCount);
    for (auto& guard : guards) {
        guard.setName(getStringIndex());
    }
}

/**
 * @brief Reads the Functions definition for a state
 * @param[in] functions collection to fill in.
 */
void Pex::FileReader::read(Pex::Functions &functions)
{
    auto functionCount = getUint16();
    functions.resize(functionCount);
    for(auto& function : functions)
    {
        function.setName(getStringIndex());
        read(function);
    }
}

/**
 * @brief Reads a body function
 * @param[in] function Function structure to fill in.
 */
void Pex::FileReader::read(Pex::Function &function)
{
    function.setReturnTypeName(getStringIndex());
    function.setDocString(getStringIndex());
    function.setUserFlags(getUint32());
    function.setFlags(getUint8());
    read(function.getParams());
    read(function.getLocals());
    read(function.getInstructions());
}

/**
 * @brief Reads the local variable definition for a function body
 * @param[in] typednames collection to fill in.
 */
void Pex::FileReader::read(Pex::TypedNames &typednames)
{
    auto nameCount = getUint16();
    typednames.resize(nameCount);
    for(auto& typedname : typednames)
    {
        typedname.setName(getStringIndex());
        typedname.setTypeName(getStringIndex());
    }
}

/**
 * @brief Reads the instruction list for a function body
 * @param[in] instructions collection to fill in.
 */
void Pex::FileReader::read(Pex::Instructions &instructions)
{
    auto instructionCount = getUint16();
    instructions.resize(instructionCount);
    for(auto& instruction : instructions)
    {
        auto opcode = getUint8();
        if (opcode >= static_cast<std::uint8_t>(OpCode::MAX_OPCODE))
        {
            std::stringstream error;
            error << "Invalid opcode 0x" << std::hex << std::setfill('0') << std::setw(2) << (int)opcode;
            throw std::runtime_error(error.str());
        }
        instruction.setOpCode(static_cast<OpCode>(opcode));
        auto& args = instruction.getArgs();
        args.resize(instruction.getOpCodeArgCount());
        for(auto& arg : args)
        {
            arg = getValue();
        }
        if (instruction.hasVarArgs())
        {
            auto argcount = getValue();
            if (argcount.getType() != ValueType::Integer)
            {
                throw std::runtime_error("Invalid value for varargs");
            }
            auto& varargs = instruction.getVarArgs();
            varargs.resize(argcount.getInteger());
            for(auto& arg : varargs)
            {
                arg = getValue();
            }
        }
    }
}

/**
 * @brief Reads a byte from the file.
 * @return a byte read from the stream
 */
std::uint8_t Pex::FileReader::getUint8()
{
    std::uint8_t value;
    m_iStream->read(reinterpret_cast<char*>(&value), sizeof(value));
    if(m_iStream->fail() || m_iStream->eof())
    {
        throw std::runtime_error("Error reading file");
    }
    return value;
}

/**
 * @brief Reads a 16 bit unsigned int from the file.
 * If file is big endian, byteswaps to little endian
 * @return a short read from the file.
 */
std::uint16_t Pex::FileReader::getUint16()
{
    std::uint16_t value;
    m_iStream->read(reinterpret_cast<char*>(&value), sizeof(value));
    if(m_iStream->fail() || m_iStream->eof())
    {
        throw std::runtime_error("Error reading file");
    }
    if (m_endianness == Big){
        return byteswap(value);
    }
    return value;
}

/**
 * @brief Reads a 32 bit unsigned int from the file.
 * If file is big endian, byteswaps to little endian
 * @return a long read from the file.
 */
std::uint32_t Pex::FileReader::getUint32(bool le_override)
{
    std::uint32_t value = 0;
    m_iStream->read(reinterpret_cast<char*>(&value), sizeof(value));
    if(m_iStream->gcount() != sizeof(value))
    {
        throw std::runtime_error("Error reading file");
    }
    if (!le_override && m_endianness == Big){
        return byteswap(value);
    }
    return value;
}

/**
 * @brief Read a string index from the file.
 * The string table used is the one already read from the file.
 * @return a String Index.
 */
Pex::StringTable::Index Pex::FileReader::getStringIndex()
{
    assert(m_StringTable != nullptr);
    auto index = getUint16();
    if (index >= m_StringTable->size())
    {
        throw std::runtime_error("Invalid string index");
    }

    return m_StringTable->get(index);
}

/**
 * @brief Reads a 16 bit signed int from the file.
 * If file is big endian, byteswaps to little endian
 * @return a short read from the file.
 */
std::int16_t Pex::FileReader::getInt16()
{
    std::int16_t value;
    m_iStream->read(reinterpret_cast<char*>(&value), sizeof(value));
    if(m_iStream->fail() || m_iStream->eof())
    {
        throw std::runtime_error("Error reading file");
    }
    if (m_endianness == Big){
        return byteswap(value);
    }
    return value;
}

/**
 * @brief Reads a 32 bit float from the file.
 * If file is big endian, byteswaps to little endian
 * @return a float read from the file.
 */
float Pex::FileReader::getFloat()
{
    float value;
    m_iStream->read(reinterpret_cast<char*>(&value), sizeof(value));
    if(m_iStream->fail() || m_iStream->eof())
    {
        throw std::runtime_error("Error reading file");
    }
    if (m_endianness == Big){
       value = byteswap_float(value);
    }
    return value;
}

/**
 * @brief Reads a 64 bit time_t from the file.
 * If file is big endian, byteswaps to little endian
 * @return a time_t read from the file.
 */
std::time_t Pex::FileReader::getTime()
{
    static_assert(sizeof(std::time_t) == 8, "time_t is not 64 bits");
    std::time_t value;
    m_iStream->read(reinterpret_cast<char*>(&value), sizeof(value));
    if(m_iStream->fail() || m_iStream->eof())
    {
        throw std::runtime_error("Error reading file");
    }
    if (m_endianness == Big){
        return byteswap(value);
    }
    return value;
}

/**
 * @brief Reads a variable sized string from the file.
 * @return a string.
 */
std::string Pex::FileReader::getString()
{
    auto len = getUint16();
    auto data = new char[len];
    memset(data, 0, len);
    m_iStream->read(data, len);
    if (m_iStream->gcount() != len)
    {
        throw std::runtime_error("Unable to read string");
    }
    std::string value(data, data + len);
    delete[] data;
    return value;
}

/**
 * @brief Reads a variant typed value from the file.
 * @return a Pew::Value.
 */
Pex::Value Pex::FileReader::getValue()
{
    Pex::ValueType valueType = Pex::ValueType(getUint8());
    switch(valueType)
    {
    case Pex::ValueType::None:
        return Value();
        break;
    case Pex::ValueType::Identifier:
    {
        auto value = getStringIndex();
        return Value(value, true);
    }
        break;
    case Pex::ValueType::String:
    {
        auto value = getStringIndex();
        return Value(value);
    }
        break;
    case Pex::ValueType::Integer:
    {
        auto value = static_cast<std::int32_t>(getUint32());
        return Value(value);
    }
        break;
    case Pex::ValueType::Float:
    {
        auto value = getFloat();
        return Value(value);
    }
        break;
    case Pex::ValueType::Bool:
    {
        auto value = (getUint8() != 0);
        return Value(value);
    }
        break;
    default:
        std::stringstream error;
        error << "Invalid value type " << (uint8_t)valueType;
        throw std::runtime_error(error.str());

    }
}
```

## File: `Pex/FileReader.hpp`
```
#pragma once

#include <cstdint>
#include <ctime>
#include <fstream>

#include "Binary.hpp"

namespace Pex {

/**
 * @brief Binary structure file reading.
 *
 * The FileReader class provides a function to read a PEX file into a Binary structure.
 * The filename is provided as a parameter of the constructor.
 */
class FileReader
{
public:
    FileReader(std::istream *stream);
    FileReader(const std::string& fileName);
    ~FileReader();

    void read(Binary& binary);
    enum Endianness{
        Big,
        Little
    };
    static constexpr std::uint32_t LE_MAGIC_NUMBER = 0xFA57C0DE;
    static constexpr std::uint32_t BE_MAGIC_NUMBER = 0xDEC057FA;

protected:

    void readHeader(Header& header);
    void read(StringTable& stringTable);
    void read(DebugInfo& debugInfo);
    void read(UserFlags& userFlags);
    void read(Pex::Binary::ScriptType script_type, Objects& objects);
    void read(StructInfos& structInfos);
    void read(Variables& variables);
    void read(Properties& properties);
    void read(States& states);
    void read(Guards& guards);
    void read(Functions& functions);
    void read(Function& function);
    void read(TypedNames& typednames);
    void read(Instructions& instructions);


    std::uint8_t getUint8();
    std::uint16_t getUint16();
    std::uint32_t getUint32(bool le_override = false);
    StringTable::Index getStringIndex();

    std::int16_t getInt16();
    float getFloat();
    std::time_t getTime();
    std::string getString();
    Value getValue();

    const StringTable* m_StringTable;

private:
    Endianness m_endianness;
    std::istream* m_iStream;
    std::ifstream m_fileStream;
};
}
```

## File: `Pex/Function.cpp`
```cpp
#include "Function.hpp"

/**
 * @brief Default constructor.
 */
Pex::Function::Function() :
    m_Flags(0)
{
}

/**
 * @brief Default destructor
 */
Pex::Function::~Function()
{
}

/**
 * @brief Retrieve the return type of the function.
 *
 * @return the index of the type name.
 */
Pex::StringTable::Index Pex::Function::getReturnTypeName() const
{
    return m_ReturnTypeName;
}

/**
 * @brief Sets the return type of the function
 *
 * @param[in] value Index of the return type.
 */
void Pex::Function::setReturnTypeName(Pex::StringTable::Index value)
{
    m_ReturnTypeName = value;
}

/**
 * @brief Sets the function flags byte.
 * @param[in] value Flag byte.
 */
void Pex::Function::setFlags(std::uint8_t value)
{
    m_Flags = value;
}

/**
 * @brief Check if the function is global
 *
 * @return true if the global flag is set
 */
bool Pex::Function::isGlobal() const
{
    return m_Flags & 0x01;
}

/**
 * @brief Check if the function is native
 * @return true if the native flag is set
 */
bool Pex::Function::isNative() const
{
    return m_Flags & 0x02;
}

/**
 * @brief Retrieve the list of parameters
 * @return the const list of parameters
 */
const Pex::TypedNames &Pex::Function::getParams() const
{
    return m_Params;
}

/**
 * @brief Retrieve the list of parameters
 * @return the modifiable list of parameters
 */
Pex::TypedNames &Pex::Function::getParams()
{
    return m_Params;
}

/**
 * @brief Retrieve the list of local variables
 * @return the const list of local variables
 */
const Pex::TypedNames &Pex::Function::getLocals() const
{
    return m_Locals;
}


/**
 * @brief Retrieve the list of local variables
 * @return the modifiable list of local variables
 */
Pex::TypedNames &Pex::Function::getLocals()
{
    return m_Locals;
}

/**
 * @brief Retrieve the list of bytecode instructions
 * @return the const list of instructions
 */
const Pex::Instructions &Pex::Function::getInstructions() const
{
    return m_Instructions;
}

/**
 * @brief Retrieve the list of bytecode instructions
 * @return the modifiable list of instructions
 */
Pex::Instructions &Pex::Function::getInstructions()
{
    return m_Instructions;
}
```

## File: `Pex/Function.hpp`
```
#pragma once

#include <vector>

#include "StringTable.hpp"
#include "NamedItem.hpp"
#include "UserFlagged.hpp"
#include "DocumentedItem.hpp"

#include "TypedName.hpp"
#include "Instruction.hpp"

namespace Pex {
/**
 * @brief Function definition
 *
 * The Function class contains all elements needed to define a function in a given object.
 * It contains the function signature and the associated body.
 *
 */
class Function :
        public NamedItem,
        public UserFlagged,
        public DocumentedItem
{
public:
    Function();
    virtual ~Function();

    StringTable::Index getReturnTypeName() const;
    void setReturnTypeName(StringTable::Index value);

    void setFlags(std::uint8_t value);
    bool isGlobal() const;
    bool isNative() const;

    const TypedNames& getParams() const;
    TypedNames& getParams();

    const TypedNames& getLocals() const;
    TypedNames& getLocals();

    const Instructions& getInstructions() const;
    Instructions& getInstructions();
protected:
    StringTable::Index m_ReturnTypeName;
    std::uint8_t m_Flags;
    TypedNames m_Params;
    TypedNames m_Locals;
    Instructions m_Instructions;

};

typedef std::vector<Function> Functions;
}
```

## File: `Pex/Guard.hpp`
```
#pragma once

#include <cstdint>
#include <vector>

#include "StringTable.hpp"
#include "NamedItem.hpp"

namespace Pex {

/**
 * @brief Guard definition
 *
 * This class contains the names guard.
 *
 */
class Guard :
    public NamedItem {
public:
    Guard() = default;
    ~Guard() = default;
};

typedef std::vector<Guard> Guards;
}
```

## File: `Pex/Header.cpp`
```cpp
#include "Header.hpp"

#include <iostream>

/**
 * @brief Default constructor
 */
Pex::Header::Header() :
    m_MajorVersion(0),
    m_MinorVersion(0),
    m_CompilationTime(0),
    m_GameID(0)
{
}

/**
 * @brief Retrieve the major version number of the file
 * @return the major version number
 */
std::uint8_t Pex::Header::getMajorVersion() const
{
    return m_MajorVersion;
}

/**
 * @brief Sets the major version number
 * @param value minor version number
 */
void Pex::Header::setMajorVersion(std::uint8_t value)
{
    m_MajorVersion = value;
}


/**
 * @brief Retrieve the minor version number of the file
 * @return the minor version number
 */
std::uint8_t Pex::Header::getMinorVersion() const
{
    return m_MinorVersion;
}

/**
 * @brief Sets the minor version number
 * @param value minor version number
 */
void Pex::Header::setMinorVersion(std::uint8_t value)
{
    m_MinorVersion = value;
}

/**
 * @brief Retrieve the compilation date/time.
 * @return the compilation date.
 */
const std::time_t& Pex::Header::getCompilationTime() const
{
    return m_CompilationTime;
}

/**
 * @brief Set the compilation date/time
 * @param value The compilation date.
 */
void Pex::Header::setCompilationTime(const std::time_t& value)
{
    m_CompilationTime = value;
}

/**
 * @brief Get the game id
 * @return the game id;
 */
std::uint16_t Pex::Header::getGameID() const
{
    return m_GameID;
}

/**
 * @brief Set the game id;
 * @param value the new game id;
 */
void Pex::Header::setGameID(std::uint16_t value)
{
    m_GameID = value;
}

/**
 * @brief Retrieve the name of the original source file.
 * @return the name of the file
 */
std::string Pex::Header::getSourceFileName() const
{
    return m_SourceFileName;
}

/**
 * @brief Set the name of the original source file.
 * @param value The name of the file.
 */
void Pex::Header::setSourceFileName(const std::string &value)
{
    m_SourceFileName = value;
}

/**
 * @brief Retrieve the name of the user which compiled the source.
 * @return the user name
 */
std::string Pex::Header::getUserName() const
{
    return m_UserName;
}

/**
 * @brief Set the name of the user which compiled the source.
 * @param value the user name
 */
void Pex::Header::setUserName(const std::string &value)
{
    m_UserName = value;
}

/**
 * @brief Retrieve the name of the computer which compiled the source
 * @return the computer name
 */
std::string Pex::Header::getComputerName() const
{
    return m_ComputerName;
}

/**
 * @brief Set the name of the computer which compiled the source
 * @param value the computer name
 */
void Pex::Header::setComputerName(const std::string &value)
{
    m_ComputerName = value;
}

```

## File: `Pex/Header.hpp`
```
#pragma once

#include <cstdint>
#include <ctime>
#include <string>

namespace Pex {
/**
 * @brief Header file content.
 *
 * The Header class contains the data found in the header of a PEX file, such as compilation date
 * or user/computer which compiled the binary
 *
 */
class Header
{
public:
    Header();

    std::uint8_t getMajorVersion() const;
    void setMajorVersion(std::uint8_t value);

    std::uint8_t getMinorVersion() const;
    void setMinorVersion(std::uint8_t value);

    const std::time_t& getCompilationTime() const;
    void setCompilationTime(const std::time_t& value);

    std::uint16_t getGameID() const;
    void setGameID(std::uint16_t value);

    std::string getSourceFileName() const;
    void setSourceFileName(const std::string& value);

    std::string getUserName() const;
    void setUserName(const std::string& value);

    std::string getComputerName() const;
    void setComputerName(const std::string& value);


protected:
    std::uint8_t m_MajorVersion;
    std::uint8_t m_MinorVersion;
    std::time_t m_CompilationTime;
    std::uint16_t m_GameID;
    std::string m_SourceFileName;
    std::string m_UserName;
    std::string m_ComputerName;
};
}
```

## File: `Pex/Instruction.cpp`
```cpp
#include "Instruction.hpp"

#include <cassert>

/**
 * @brief Opcode information structure
 *
 * Contains the data about the opcodes
 */
struct OpCodeInfo {
    /**
     * @brief OpCode name
     */
    const char* name;
    /**
     * @brief number of fixed arguments
     */
    int         args;
    /**
     * @brief Use variable args
     */
    bool        varargs;
};

/**
 * Opcode definition table
 */
static const OpCodeInfo OPCODES[int(Pex::OpCode::MAX_OPCODE)] = {
    {"nop", 0, false},
    {"iadd", 3, false},
    {"fadd", 3, false},
    {"isub", 3, false},
    {"fsub", 3, false},
    {"imul", 3, false},
    {"fmul", 3, false},
    {"idiv", 3, false},
    {"fdiv", 3, false},
    {"imod", 3, false},
    {"not",  2, false},
    {"ineg", 2, false},
    {"fneg", 2, false},
    {"assign", 2, false},
    {"cast", 2, false},
    {"cmp_eq", 3, false},
    {"cmp_lt", 3, false},
    {"cmp_lte", 3, false},
    {"cmp_gt", 3, false},
    {"comp_gte", 3, false},
    {"jmp", 1, false},
    {"jmpt", 2, false},
    {"jmpf", 2, false},
    {"callmethod", 3, true},
    {"callparent", 2, true},
    {"callstatic", 3, true},
    {"return", 1, false},
    {"strcat", 3, false},
    {"propget", 3, false},
    {"propset", 3, false},
    {"array_create", 2, false},
    {"array_length", 2, false},
    {"array_getlement", 3, false},
    {"array_setelement", 3, false},
    {"array_findelement", 4, false},
    {"array_rfindelement", 4, false},
    {"is", 3, false},
    {"struct_create", 1, false},
    {"struct_get", 3, false},
    {"struct_set", 3, false},
    {"array_findstruct", 5, false},
    {"array_rfindstruct", 5, false},
    {"array_add", 3, false},
    {"array_insert", 3, false},
    {"array_removelast", 1, false},
    {"array_remove", 3, false},
    {"array_clear", 1, false},
    {"array_getallmatchingstructs", 6, false},
    {"lock_guards", 0, true},
    {"unlock_guards", 0, true},
    {"try_lock_guards", 1, true},
};

/**
 * @brief Default constructor
 *
 * Create a NOP instruction
 */
Pex::Instruction::Instruction() :
    m_OpCode(OpCode::NOP)
{
}

/**
 * @brief Default desctructor
 */
Pex::Instruction::~Instruction()
{
}

/**
 * @brief Get the opcode of the instruction
 * @return the OpCode
 */
Pex::OpCode Pex::Instruction::getOpCode() const
{
    return m_OpCode;
}

/**
 * @brief Get the opcode name
 * @return the opcode name
 */
const char *Pex::Instruction::getOpCodeName() const
{
    return OPCODES[static_cast<int>(m_OpCode)].name;
}

/**
 * @brief Get the number of mandatory arguments needed by the instruction
 * @return the number of arguments
 */
int Pex::Instruction::getOpCodeArgCount() const
{
    return OPCODES[static_cast<int>(m_OpCode)].args;
}

/**
 * @brief Set the opcode of the instruction
 * @param value The new opcode
 */
void Pex::Instruction::setOpCode(Pex::OpCode value)
{
    assert(value < OpCode::MAX_OPCODE);
    m_OpCode = value;
    m_Args.clear();
    m_VarArgs.clear();
}

/**
 * @brief Get the mandatory arguments list
 * @return the const list of arguments
 */
const Pex::Instruction::Args &Pex::Instruction::getArgs() const
{
    return m_Args;
}

/**
 * @brief Get the mandatory arguments list
 * @return the modifiable list of arguments;
 */
Pex::Instruction::Args &Pex::Instruction::getArgs()
{
    return m_Args;
}

/**
 * @brief Check if the instruction allows a list of variable arguments
 * @return true if the opcode allow variable arguments
 */
bool Pex::Instruction::hasVarArgs() const
{
    return OPCODES[static_cast<int>(m_OpCode)].varargs;
}

/**
 * @brief Get the list of variable arguments
 * @return the const list of variable arguments
 */
const Pex::Instruction::Args &Pex::Instruction::getVarArgs() const
{
    return m_VarArgs;
}

/**
 * @brief Get the list of variable arguments
 * @return the modifiable list of variable arguments
 */
Pex::Instruction::Args &Pex::Instruction::getVarArgs()
{
    return m_VarArgs;
}
```

## File: `Pex/Instruction.hpp`
```
#pragma once

#include <vector>

#include "Value.hpp"

namespace Pex{

/**
 * @brief List of available opcodes
 */
enum class OpCode {
    NOP,
    IADD,
    FADD,
    ISUB,
    FSUB,
    IMUL,
    FMUL,
    IDIV,
    FDIV,
    IMOD,
    NOT,
    INEG,
    FNEG,
    ASSIGN,
    CAST,
    CMP_EQ,
    CMP_LT,
    CMP_LTE,
    CMP_GT,
    CMP_GTE,
    JMP,
    JMPT,
    JMPF,
    CALLMETHOD,
    CALLPARENT,
    CALLSTATIC,
    RETURN,
    STRCAT,
    PROPGET,
    PROPSET,
    ARRAY_CREATE,
    ARRAY_LENGTH,
    ARRAY_GETELEMENT,
    ARRAY_SETELEMENT,
    ARRAY_FINDELEMENT,
    ARRAY_RFINDELEMENT,
    // New in Fallout 4
    IS,
    STRUCT_CREATE,
    STRUCT_GET,
    STRUCT_SET,
    ARRAY_FINDSTRUCT,
    ARRAY_RFINDSTRUCT,
    ARRAY_ADD,
    ARRAY_INSERT,
    ARRAY_REMOVELAST,
    ARRAY_REMOVE,
    ARRAY_CLEAR,
    // New in Fallout 76
    ARRAY_GETALLMATCHINGSTRUCTS,
    // New in Starfield
    LOCK_GUARDS,
    UNLOCK_GUARDS,
    TRY_LOCK_GUARDS,
    MAX_OPCODE
};


/**
 * @brief ByteCode Instruction.
 *
 */
class Instruction
{
public:
    typedef std::vector<Value> Args;
public:
    Instruction();
    ~Instruction();

    OpCode getOpCode() const;
    void setOpCode(OpCode value);

    const char* getOpCodeName() const;
    int getOpCodeArgCount() const;

    const Args& getArgs() const;
    Args& getArgs();

    bool hasVarArgs() const;

    const Args& getVarArgs() const;
    Args& getVarArgs();
protected:
    OpCode m_OpCode;
    Args m_Args;
    Args m_VarArgs;
};

typedef std::vector<Instruction> Instructions;
}
```

## File: `Pex/NamedItem.cpp`
```cpp
#include "NamedItem.hpp"

#include <cassert>

/**
 * @brief Default constructor
 */
Pex::NamedItem::NamedItem()
{
}

/**
 * @brief Default destructor
 */
Pex::NamedItem::~NamedItem()
{
}

/**
 * @brief Get the name of the item
 * @return a name index
 */
Pex::StringTable::Index Pex::NamedItem::getName() const
{
    return m_Name;
}

/**
 * @brief Sets the name of the item
 * @param value The new name index
 */
void Pex::NamedItem::setName(Pex::StringTable::Index value)
{
    assert(value.isValid());
    m_Name = value;
}
```

## File: `Pex/NamedItem.hpp`
```
#pragma once

#include <cstdint>

#include "StringTable.hpp"

namespace Pex {

/**
 * @brief Base Mixin for named item.
 *
 * This mixin defines the name field for named elements
 */
class NamedItem
{
public:
    NamedItem();
    virtual ~NamedItem();

    StringTable::Index getName() const;
    void setName(StringTable::Index value);

protected:
    StringTable::Index m_Name;
};
}
```

## File: `Pex/Object.cpp`
```cpp
#include "Object.hpp"
#include <cassert>

/**
 * @brief Default constructor
 *
 * Creates an empty object.
 */
Pex::Object::Object()
{
    // set to false at first due to on-disk Skyrim scripts not having this flag
    m_ConstFlag = false; 
}

/**
 * @brief Deafaul destructor
 */
Pex::Object::~Object()
{
}

/**
 * @brief Get the name of the parent class, if one.
 * @return the name index of the class
 */
Pex::StringTable::Index Pex::Object::getParentClassName() const
{
    return m_ParentClassName;
}

/**
 * @brief Set the name of the parent class
 * @param value The new parent class name index.
 */
void Pex::Object::setParentClassName(StringTable::Index value)
{
    assert(value.isValid());
    m_ParentClassName = value;
}

/**
 * @brief Get the name of the default state.
 * @return The default name index
 */
Pex::StringTable::Index Pex::Object::getAutoStateName() const
{
    return m_AutoStateName;
}

/**
 * @brief Set the name of the default state
 * @param value The default state name index
 */
void Pex::Object::setAutoStateName(StringTable::Index value)
{
    assert(value.isValid());
    m_AutoStateName = value;
}

/**
 * @brief Get the variables list
 * @return The const variables list
 */
const Pex::Variables &Pex::Object::getVariables() const
{
    return m_Variables;
}

/**
 * @brief Get the variables list
 * @return The modifiable variables list
 */
Pex::Variables &Pex::Object::getVariables()
{
    return m_Variables;
}

/**
 * @brief Get the properties list
 * @return The const properties list
 */
const Pex::Properties &Pex::Object::getProperties() const
{
    return m_Properties;
}

/**
 * @brief Get the properties list
 * @return The modifiable properties list
 */
Pex::Properties &Pex::Object::getProperties()
{
    return m_Properties;
}


/**
 * @brief Get the states list
 * @return The const states list
 */
const Pex::States &Pex::Object::getStates() const
{
    return m_States;
}

/**
 * @brief Get the states list
 * @return The const states list
 */
Pex::States &Pex::Object::getStates()
{
    return m_States;
}

/**
 * @brief Get the guards list
 * @return The const guards list
 */
const Pex::Guards& Pex::Object::getGuards() const {
    return m_Guards;
}

/**
 * @brief Get the guards list
 * @return The const guards list
 */
Pex::Guards& Pex::Object::getGuards() {
    return m_Guards;
}
```

## File: `Pex/Object.hpp`
```
#pragma once

#include <vector>
#include <cstdint>


#include "StringTable.hpp"
#include "NamedItem.hpp"
#include "DocumentedItem.hpp"
#include "StructInfo.hpp"
#include "Variable.hpp"
#include "Property.hpp"
#include "State.hpp"
#include "Guard.hpp"

namespace Pex {

/**
 * @brief Object definition
 *
 * This class contains the elements defined in a pex script.
 *
 *
 */
class Object :
        public NamedItem,
        public UserFlagged,
        public DocumentedItem
{
public:
    Object();
    virtual ~Object();

    StringTable::Index getParentClassName() const;
    void setParentClassName(StringTable::Index value);


    StringTable::Index getAutoStateName() const;
    void setAutoStateName(StringTable::Index value);

    std::uint8_t getConstFlag() const { return m_ConstFlag; }
    void setConstFlag(std::uint8_t value) { m_ConstFlag = value; }

    const StructInfos& getStructInfos() const { return m_StructInfos; }
    StructInfos& getStructInfos() { return m_StructInfos; }

    const Variables& getVariables() const;
    Variables& getVariables();

    const Properties& getProperties() const;
    Properties& getProperties();

    const States& getStates() const;
    States& getStates();

    const Guards& getGuards() const;
    Guards& getGuards();

private:
    StringTable::Index m_ParentClassName;
    StringTable::Index m_AutoStateName;
    std::uint8_t m_ConstFlag;

    StructInfos m_StructInfos;
    Variables m_Variables;
    Properties m_Properties;
    States m_States;
    Guards m_Guards;
};

typedef std::vector<Object> Objects;
}
```

## File: `Pex/Property.cpp`
```cpp
#include "Property.hpp"

#include <cassert>

/**
 * @brief Default constructor
 *
 * Creates an empty property
 */
Pex::Property::Property() :
    m_Flags(PropertyFlag::NO_FLAGS)
{
}
/**
 * @brief Default destructor
 */
Pex::Property::~Property()
{
}

/**
 * @brief Get the name of the associated variable, if one
 * @return the name index of the auto variable
 */
Pex::StringTable::Index Pex::Property::getAutoVarName() const
{
    return m_AutoVarName;
}

/**
 * @brief Set the name of the associated auto variable.
 * @param value The name index of the assoiated variable.
 */
void Pex::Property::setAutoVarName(Pex::StringTable::Index value)
{
    assert(value.isValid());
    m_AutoVarName = value;
}

/**
 * @brief Sets the flags associated with the property
 * @param value The new flag value.
 */
void Pex::Property::setFlags(Pex::PropertyFlag value)
{
    m_Flags = value;
}

/**
 * @brief Check if the property is readable
 * @return true if the property is readable
 */
bool Pex::Property::isReadable() const
{
    return (m_Flags & PropertyFlag::READ) != PropertyFlag::NO_FLAGS;
}

/**
 * @brief Check if the property is writable
 * @return true if the property is writable
 */
bool Pex::Property::isWritable() const
{
    return (m_Flags & PropertyFlag::WRITE) != PropertyFlag::NO_FLAGS;
}

/**
 * @brief Check if the property is auto
 * @return true if the property is auto
 */
bool Pex::Property::hasAutoVar() const
{
    return (m_Flags & PropertyFlag::AUTOVAR) != PropertyFlag::NO_FLAGS;
}

/**
 * @brief Get the getter function.
 * @return a const function.
 */
const Pex::Function &Pex::Property::getReadFunction() const
{
    assert(isReadable() && !hasAutoVar());
    return m_ReadFunction;
}

/**
 * @brief Get the getter function.
 * @return a modifiable function.
 */
Pex::Function &Pex::Property::getReadFunction()
{
    assert(isReadable() && !hasAutoVar());
    return m_ReadFunction;
}

/**
 * @brief Get the setter function.
 * @return a const function.
 */
const Pex::Function &Pex::Property::getWriteFunction() const
{
    assert(isWritable() && !hasAutoVar());
    return m_WriteFunction;
}

/**
 * @brief Get the setter function.
 * @return a modifiable function.
 */
Pex::Function &Pex::Property::getWriteFunction()
{
    assert(isWritable() && !hasAutoVar());
    return m_WriteFunction;
}
```

## File: `Pex/Property.hpp`
```
#pragma once

#include <cstdint>
#include <vector>

#include "StringTable.hpp"
#include "NamedItem.hpp"
#include "TypedItem.hpp"
#include "DocumentedItem.hpp"
#include "UserFlagged.hpp"
#include "Function.hpp"

namespace Pex {

enum class PropertyFlag : std::uint8_t {
    NO_FLAGS = 0,
    READ     = 1 << 0,
    WRITE    = 1 << 1,
    AUTOVAR  = 1 << 2
};

inline PropertyFlag operator|(PropertyFlag a, PropertyFlag b)
{
  typedef std::underlying_type<PropertyFlag>::type enum_type;
  return static_cast<PropertyFlag>(static_cast<enum_type>(a) | static_cast<enum_type>(b));
}
inline PropertyFlag operator&(PropertyFlag a, PropertyFlag b)
{
  typedef std::underlying_type<PropertyFlag>::type enum_type;
  return static_cast<PropertyFlag>(static_cast<enum_type>(a) & static_cast<enum_type>(b));
}

/**
 * @brief Property definition
 *
 * This class contains the type, names and associated flags of a property.
 *
 * The getter and stter function are also stored here if they exists.
 *
 */
class Property :
        public NamedItem,
        public TypedItem,
        public UserFlagged,
        public DocumentedItem
{
public:
    Property();
    ~Property();

    StringTable::Index getAutoVarName() const;
    void setAutoVarName(StringTable::Index value);

    void setFlags(PropertyFlag value);
    bool isReadable() const;
    bool isWritable() const;
    bool hasAutoVar() const;

    const Function& getReadFunction() const;
    Function& getReadFunction();

    const Function& getWriteFunction() const;
    Function& getWriteFunction();

protected:
    StringTable::Index m_DocString;
    PropertyFlag m_Flags;
    StringTable::Index m_AutoVarName;

    Function m_ReadFunction;
    Function m_WriteFunction;

};

typedef std::vector<Property> Properties;
}
```

## File: `Pex/State.cpp`
```cpp
#include "State.hpp"

/**
 * @brief Default constructor
 *
 */
Pex::State::State()
{
}

/**
 * @brief Default destructor state
 */
Pex::State::~State()
{
}

/**
 * @brief Get the function list
 * @return the const function list
 */
const Pex::Functions &Pex::State::getFunctions() const
{
    return m_Functions;
}

/**
 * @brief Get the function list
 * @return the modifiable function list
 */
Pex::Functions &Pex::State::getFunctions()
{
    return m_Functions;
}
```

## File: `Pex/State.hpp`
```
#pragma once

#include <vector>

#include "StringTable.hpp"
#include "NamedItem.hpp"
#include "Function.hpp"

namespace Pex {
/**
 * @brief State definition
 *
 * This class contains the elements for a state.
 */
class State :
        public NamedItem
{
public:
    State();
    virtual ~State();

    const Functions& getFunctions() const;
    Functions& getFunctions();

protected:
    Functions m_Functions;
};

typedef std::vector<State> States;

}
```

## File: `Pex/StringTable.cpp`
```cpp
#include "StringTable.hpp"
#include <Champollion/CaselessCompare.h>

#include <algorithm>
#include <stdexcept>
#include <sstream>
#include <cassert>

/**
 * @brief Default constructor
 *
 * Builds an empty table.
 *
 */
Pex::StringTable::StringTable()
{
}

/**
 * @brief Default destructor
 */
Pex::StringTable::~StringTable()
{
}

/**
 * @brief Get the string using the index
 * @param index The index of the string to retrieve
 *
 * @return a const reference to the string
 */
const std::string &Pex::StringTable::operator [](std::uint16_t index) const
{
    return m_Table[index];
}

/**
 * @brief Get the string using the index
 * @param index The index of the string to retrieve
 *
 * @return a modifiable reference to the string
 */
std::string &Pex::StringTable::operator [](std::uint16_t index)
{
    return m_Table[index];
}

/**
 * @brief Get the Index object for the given indice
 * @param index The Indice to wrap
 *
 * @return a new Index pointing to the string.
 * @throws a std::runtime_error if the indice is outside the bounds.
 */
Pex::StringTable::Index Pex::StringTable::get(std::uint16_t index) const
{
    if( index < size())
    {
        return Index(this, index);
    }
    else if (index == Index::UNDEFINED)
    {
        return Index();
    }
    else
    {
        throw std::runtime_error("Invalid string index");
    }
}

/**
 * @brief Find a given string in the table
 *
 * The string is considered as an identifier, meaning that the search is case-insensitive.
 *
 * @param id Identifier to find
 * @return The index of the indentifier. The Index may be invalid if the string is not found.
 */
Pex::StringTable::Index Pex::StringTable::findIdentifier(const std::string &id) const
{
    auto it = std::find_if(m_Table.begin(), m_Table.end(), [&] (const std::string& item) {
        return caselessCompare(item.c_str(), id.c_str()) == 0;
    });
    if (it == m_Table.end())
    {
        return Index();
    }
    else
    {
        return Index(this, uint16_t(it - begin()));
    }
}

/**
 * @brief Get the begin iterator
 * @return the begin iterator
 */
Pex::StringTable::Table::iterator Pex::StringTable::begin()
{
    return m_Table.begin();
}

/**
 * @brief Get the begin iterator
 * @return the begin iterator
 */
Pex::StringTable::Table::const_iterator Pex::StringTable::begin() const
{
    return m_Table.begin();
}

/**
 * @brief Get the end iterator
 * @return the end iterator
 */
Pex::StringTable::Table::iterator Pex::StringTable::end()
{
    return m_Table.end();
}

/**
 * @brief Get the end iterator
 * @return the end iterator
 */
Pex::StringTable::Table::const_iterator Pex::StringTable::end() const
{
    return m_Table.end();
}

/**
 * @brief Insert a value at the end of the table
 * @param value The string to insert
 */
void Pex::StringTable::push_back(const std::string &value)
{
    m_Table.push_back(value);
}

/**
 * @brief Get the size of the table
 * @return teh size of the table
 */
size_t Pex::StringTable::size() const
{
    return m_Table.size();
}

/**
 * @brief Prepare the table for multiple insertion
 * @param size The expected size of the table after the insertions.
 */
void Pex::StringTable::reserve(size_t size)
{
    return m_Table.reserve(size);
}


/**
 * @brief Constructor
 * Build an index from the table and the index.
 * Only a StringTable object is able to build an index using this constructor.
 *
 * @param table
 * @param index
 */
Pex::StringTable::Index::Index(const Pex::StringTable *table, std::uint16_t index) :
    m_Table(table),
    m_Index(index)
{
    assert(isValid());
}

/**
 * @brief Default constructor
 *
 * Builds a default invalid index.
 */
Pex::StringTable::Index::Index() :
    m_Table(nullptr),
    m_Index()
{
}

/**
 * @brief Default destructor.
 */
Pex::StringTable::Index::~Index()
{
}

/**
 * @brief Default value for undefined indexes
 *
 */
static std::string UNDEFINED_STRING = "undefined";

/**
 * @brief Get the string associated with the index.
 *
 * @return the string.
 */
const std::string &Pex::StringTable::Index::asString() const
{
    assert(isValid());
    if (m_Index != UNDEFINED)
    {
        return m_Table->operator [](m_Index);
    }
    else
    {
        return UNDEFINED_STRING;
    }
}

/**
 * @brief Get string contatenated with the index
 * This function is mainly used for debugging purposes.
 *
 * @return the string and index.
 */

std::string Pex::StringTable::Index::asStringWithIndex() const
{
    assert(isValid());
    std::ostringstream stream;
    stream << asString();
    stream  << "[" << m_Index << "]";
    return stream.str();
}

/**
 * @brief Get the numeric value of the index
 * @return the value of the index.
 */
std::uint16_t Pex::StringTable::Index::asIndex() const
{
    assert(isValid());
    return m_Index;
}

/**
 * @brief Get the table associated with the index
 * @return a pointer to the table. nullptr if the index is invalid.
 */
const Pex::StringTable* Pex::StringTable::Index::getTable() const
{
    return m_Table;
}

/**
 * @brief Check if the index is a valid one
 * @return True if the index can be used to get a string.
 */
bool Pex::StringTable::Index::isValid() const
{
    return (m_Index == UNDEFINED) || (m_Table != nullptr && m_Index < m_Table->size());
}

/**
 * @brief Check if the index is undefined.
 * An index is undefined if it point to a table but not to a string.
 * @return True if the index
 */
bool Pex::StringTable::Index::isUndefined() const
{
    return isValid() && m_Index == UNDEFINED;
}

/**
 * @brief Check if two indexes are equals.
 * @param rhs The index to compare to.
 * @return True is both indexes points to the same string
 */
bool Pex::StringTable::Index::operator ==(const Pex::StringTable::Index &rhs) const
{
    return m_Table == rhs.m_Table && m_Index == rhs.m_Index;
}

/**
 * @brief Check if two indexes are differents.
 * @param rhs The index to compare to.
 * @return True is the indexes points to different strings.
 */
bool Pex::StringTable::Index::operator !=(const Pex::StringTable::Index &rhs) const
{
    return m_Table != rhs.m_Table || m_Index != rhs.m_Index;
}

```

## File: `Pex/StringTable.hpp`
```
#pragma once

#include <vector>
#include <string>
#include <iostream>
#include <cstdint>
#include <sstream>

namespace Pex {

/**
 * @brief String table
 *
 * The String Table can be used as a vector for the insertion.
 * It is accessed throught the StringTable::Index classes
 * which references the table and the numeric index.
 *
 */
class StringTable
{
protected:
    typedef std::vector<std::string> Table;

public:
    StringTable();
    ~StringTable();

    /**
     * @brief Index to a string in a StringTable
     *
     * The Index class provides access to a string in the string table.
     * It contains both a pointer to the table and the value of the numeric index.
     *
     */
    class Index
    {
    public:
        static const std::uint16_t UNDEFINED  = 0xFFFF;
    public:
        Index();
        ~Index();

        const std::string& asString() const;
        std::string asStringWithIndex() const;
        std::uint16_t asIndex() const;
        const StringTable* getTable() const;

        bool isValid() const;
        bool isUndefined() const;

        bool operator == (const Index& rhs) const;
        bool operator != (const Index& rhs) const;

    protected:
        Index(const StringTable* table, std::uint16_t asIndex);
        std::uint16_t m_Index;
        const StringTable*  m_Table;

        friend class StringTable;
    };

    const std::string& operator[] (std::uint16_t index) const;
    std::string& operator[] (std::uint16_t index);

    Index get(std::uint16_t index) const;
    Index findIdentifier(const std::string& id) const;

    Table::iterator begin();
    Table::iterator end();
    Table::const_iterator begin() const;
    Table::const_iterator end() const;

    void push_back(const std::string& value);
    size_t size() const;
    void reserve(size_t size);
protected:
    Table m_Table;

};
}

[[nodiscard]] inline std::string operator + (std::string str, const Pex::StringTable::Index& index)
{
    if(index.isValid())
    {
        return str + index.asString();
    }
    else
    {
        return str + "";
    }
}

inline std::ostream& operator << (std::ostream& stream, const Pex::StringTable::Index& index)
{
    if(index.isValid())
    {
        stream << index.asString();
    }
    else
    {
        stream << "*invalid*";
    }
    return stream;
}

inline std::ostringstream operator << (std::ostringstream stream, const Pex::StringTable::Index& index)
{
    if(index.isValid())
    {
        stream << index.asString();
    }
    else
    {
        stream << "*invalid*";
    }
    return stream;
}
```

## File: `Pex/StructInfo.hpp`
```
#pragma once

#include <vector>

#include "DocumentedItem.hpp"
#include "NamedItem.hpp"
#include "StringTable.hpp"
#include "TypedItem.hpp"
#include "UserFlagged.hpp"
#include "Value.hpp"

namespace Pex {

class StructInfo :
        public NamedItem
{
public:
    class Member :
            public DocumentedItem,
            public NamedItem,
            public TypedItem,
            public UserFlagged
    {
    public:
        Member() = default;
        ~Member() = default;

        std::uint8_t getConstFlag() const { return m_ConstFlag; }
        void setConstFlag(std::uint8_t value) { m_ConstFlag = value; }

        const Value& getValue() const { return m_Value; }
        void setValue(const Value& value) { m_Value = value; }

    private:
        std::uint8_t m_ConstFlag;
        Value m_Value;
    };

    typedef std::vector<Member> Members;
public:
    StructInfo() = default;
    ~StructInfo() = default;

    const Members& getMembers() const { return m_Members; }
    Members& getMembers() { return m_Members; }

private:
    Members m_Members;

};

typedef std::vector<StructInfo> StructInfos;

}
```

## File: `Pex/TypedItem.cpp`
```cpp
#include "TypedItem.hpp"
#include <cassert>


/**
 * @brief Default constructor
 */
Pex::TypedItem::TypedItem()
{
}

/**
 * @brief Default destructor
 */
Pex::TypedItem::~TypedItem()
{
}

/**
 * @brief Get the type name
 * @return The type name index
 */
Pex::StringTable::Index Pex::TypedItem::getTypeName() const
{
    return m_TypeName;
}

/**
 * @brief Set the type name
 * @param value The new type name.
 */
void Pex::TypedItem::setTypeName(Pex::StringTable::Index value)
{
    assert(value.isValid());
    m_TypeName = value;
}
```

## File: `Pex/TypedItem.hpp`
```
#pragma once

#include <cstdint>

#include "StringTable.hpp"

namespace Pex {
/**
 * @brief Base Mixin for typed item.
 *
 * This mixin defines the type name name field for typed elements
 */
class TypedItem
{
public:
    TypedItem();
    virtual ~TypedItem();

    StringTable::Index getTypeName() const;
    void setTypeName(StringTable::Index value);

protected:
    StringTable::Index m_TypeName;
};
}
```

## File: `Pex/TypedName.cpp`
```cpp
#include "TypedName.hpp"


/**
 * @brief Default constructor
 */
Pex::TypedName::TypedName()
{
}

/**
 * @brief Default destructor
 */
Pex::TypedName::~TypedName()
{
}
```

## File: `Pex/TypedName.hpp`
```
#pragma once

#include <vector>

#include "NamedItem.hpp"
#include "TypedItem.hpp"

namespace Pex {
/**
 * @brief Typed name information
 *
 * This class associated a name and a type. Its can be used to declare variable or parameters.
 *
 */
class TypedName :
        public NamedItem,
        public TypedItem
{
public:
    TypedName();
    virtual ~TypedName();
};

typedef std::vector<TypedName> TypedNames;
}
```

## File: `Pex/UserFlag.cpp`
```cpp
#include "UserFlag.hpp"

#include <cassert>

/**
 * @brief Default constructor
 *
 */
Pex::UserFlag::UserFlag() :
    m_FlagIndex(0)
{
}

/**
 * @brief Default destructor
 */
Pex::UserFlag::~UserFlag()
{
}

/**
 * @brief Get the bit number associated with the flag
 * @return the bit number
 */
std::uint8_t Pex::UserFlag::getFlagIndex() const
{
    return m_FlagIndex;
}

/**
 * @brief Set the bit number of the flag
 * @param value the bit number, between 0 and 31
 */
void Pex::UserFlag::setFlagIndex(std::uint8_t value)
{
    assert(0<= value && value < 32);
    m_FlagIndex = value;
    m_FlagMask  = 1 << value;
}

/**
 * @brief Get the flag mask of the flag
 * The flag mask can be used with | and & operations.
 * @return
 */
std::uint32_t Pex::UserFlag::getFlagMask() const
{
    return m_FlagMask;
}
```

## File: `Pex/UserFlag.hpp`
```
#pragma once

#include <vector>
#include <cstdint>

#include "StringTable.hpp"
#include "NamedItem.hpp"

namespace Pex {
/**
 * @brief User flag definition
 *
 * The User flag definition associate a name to a flag mask.
 * It can be used to decode user flags sets on items.
 */
class UserFlag :
        public NamedItem
{
public:
    UserFlag();
    ~UserFlag();

    std::uint8_t getFlagIndex() const;
    void setFlagIndex(std::uint8_t value);

    std::uint32_t getFlagMask() const;

private:
    std::uint8_t m_FlagIndex;
    std::uint32_t m_FlagMask;
};

typedef std::vector<UserFlag> UserFlags;

}
```

## File: `Pex/UserFlagged.cpp`
```cpp
#include "UserFlagged.hpp"

/**
 * @brief Default constructor
 */
Pex::UserFlagged::UserFlagged() :
    m_UserFlags(0)
{
}

/**
 * @brief Default destructor.
 */
Pex::UserFlagged::~UserFlagged()
{
}

/**
 * @brief Get the user flags byte.
 * The flags can be decoded using the data defined in UserFlag classes.
 * @return
 */
std::uint32_t Pex::UserFlagged::getUserFlags() const
{
    return m_UserFlags;
}

/**
 * @brief Set the user flags byte.
 * @param value
 */
void Pex::UserFlagged::setUserFlags(std::uint32_t value)
{
    m_UserFlags = value;
}
```

## File: `Pex/UserFlagged.hpp`
```
#pragma once

#include <cstdint>

namespace Pex {
/**
 * @brief Base mixin for elements with User Flag.
 *
 */
class UserFlagged
{
public:
    UserFlagged();
    virtual ~UserFlagged();

    std::uint32_t      getUserFlags() const;
    void               setUserFlags(std::uint32_t value);

protected:
    std::uint32_t m_UserFlags;
};
}
```

## File: `Pex/Value.cpp`
```cpp
#include "Value.hpp"

#include <stdexcept>
#include <cassert>
#include <sstream>
#include <iomanip>


/**
 * @brief Constructor for None value.
 *
 * Builds a value object containing the None value.
 */
Pex::Value::Value() :
    m_Type(ValueType::None)
{
}

/**
 * @brief Constructor for string or identifier value
 *
 * Builds a value object containing a string or an identifier.
 *
 * @param value Index of the string in the String Table.
 * @param id True specifying if the string is an identifier.
 */
Pex::Value::Value(const StringTable::Index& value, bool id)
{
    m_Type = (id)? ValueType::Identifier : ValueType::String;
    m_Value.string.table = value.getTable();
    m_Value.string.index = value.asIndex();
}

/**
 * @brief Constructor for an integer value.
 * @param value Value to store in the object.
 */
Pex::Value::Value(std::int32_t value) :
    m_Type(ValueType::Integer)
{
    m_Value.integer = value;
}

/**
 * @brief Constructor for a real value.
 * @param value Value to store in the object
 */
Pex::Value::Value(float value) :
    m_Type(ValueType::Float)
{
    m_Value.real = value;
}

/**
 * @brief Constructor for a bool value.
 * @param value Value to store in the object
 */

Pex::Value::Value(bool value) :
    m_Type(ValueType::Bool)
{
    m_Value.boolean = value;
}

/**
 * @brief Default destructor
 */
Pex::Value::~Value()
{
}

/**
 * @brief Get the type of the value.
 * @return The enum value defining the type contained in the value.
 */
Pex::ValueType Pex::Value::getType() const
{
    return m_Type;
}

/**
 * @brief Check if the value is None.
 * @return True of the value is None.
 */
bool Pex::Value::isNone() const
{
    return m_Type == ValueType::None;
}

/**
 * @brief Set the value to None.
 */
void Pex::Value::clear()
{
    m_Type = ValueType::None;
}

/**
 * @brief Get the value as an identifier.
 * @return The identifier string index.
 */
Pex::StringTable::Index Pex::Value::getId() const
{
    ensureType(ValueType::Identifier);
    return (m_Value.string.table)?m_Value.string.table->get(m_Value.string.index): StringTable::Index();
}

/**
 * @brief Set the value to an identifier
 * @param value The value to store
 */
void Pex::Value::setId(const StringTable::Index &value)
{
    assert(value.isValid());
    m_Type = ValueType::Identifier;
    m_Value.string.table = value.getTable();
    m_Value.string.index = value.asIndex();
}

/**
 * @brief Get the value as a string.
 * @return The string index.
 */
Pex::StringTable::Index Pex::Value::getString() const
{
    ensureType(ValueType::String);
    return (m_Value.string.table)?m_Value.string.table->get(m_Value.string.index): StringTable::Index();
}

/**
 * @brief Set the value to a string.
 * @param value The value to store.
 */
void Pex::Value::set(const StringTable::Index& value)
{
    assert(value.isValid());
    m_Type = ValueType::String;
    m_Value.string.table = value.getTable();
    m_Value.string.index = value.asIndex();
}

/**
 * @brief Get the value as an integer.
 * @return The integer value.
 */
std::int32_t Pex::Value::getInteger() const
{
    ensureType(ValueType::Integer);
    return m_Value.integer;
}

/**
 * @brief Set the value to an integer.
 * @param value The value to store.
 */
void Pex::Value::set(std::int32_t value)
{
    m_Type = ValueType::Integer;
    m_Value.integer = value;
}

/**
 * @brief Get the value as a float.
 * @return The float value.
 */
float Pex::Value::getFloat() const
{
    ensureType(ValueType::Float);
    return m_Value.real;
}

/**
 * @brief Set the value to a float.
 * @param value The value to store.
 */
void Pex::Value::set(float value)
{
    m_Type = ValueType::Float;
    m_Value.real = value;
}

/**
 * @brief Get the value as a boolean.
 * @return The boolean value.
 */
bool Pex::Value::getBool() const
{
    ensureType(ValueType::Bool);
    return m_Value.boolean;
}

/**
 * @brief Set the value as a boolean.
 * @param value The value to store.
 */
void Pex::Value::set(bool value)
{
    m_Type = ValueType::Bool;
    m_Value.boolean = value;
}

/**
 * @brief Check if two value are equals.
 * @param rhs The value to compare to.
 * @return True if the two values are equals.
 */
bool Pex::Value::operator ==(const Pex::Value &rhs) const
{
    if(m_Type != rhs.m_Type)
    {
        return false;
    }
    else
    {
        switch (m_Type) {
        case ValueType::None:
            return true;
        case ValueType::Identifier:
            return m_Value.string.table == rhs.m_Value.string.table && m_Value.string.index == rhs.m_Value.string.index;
        case ValueType::String:
            return m_Value.string.table == rhs.m_Value.string.table && m_Value.string.index == rhs.m_Value.string.index;
        case ValueType::Float:
            return m_Value.real == rhs.m_Value.real;
        case ValueType::Integer:
            return m_Value.integer == rhs.m_Value.integer;
        case ValueType::Bool:
            return m_Value.boolean == rhs.m_Value.boolean;
        default:
            return false;
        }
    }
}

/**
 * @brief Convert the value to a string.
 * @return the value as a Papyrus literal.
 */
std::string Pex::Value::toString() const
{
    std::ostringstream result;
    auto type = getType();
    switch(type)
    {
        case Pex::ValueType::None:
        {
            result << "None";
            break;
        }
        case Pex::ValueType::Identifier:
        {
            result << getId().asString();
            break;
        }
        case Pex::ValueType::String:
        {
            result << '"';
            for (auto c : getString().asString())
            {
                switch(c)
                {
                case '\n':
                    result << "\\n";
                    break;
                case '\t':
                    result << "\\t";
                    break;
                case '\\':
                    result << "\\\\";
                    break;
                case '\"':
                    result << "\\\"";
                    break;
                default:
                    result << c;
                    break;
                }
            }
            result << '"';
            break;
        }
        case Pex::ValueType::Integer:
        {
            result << getInteger();
            break;
        }
        case Pex::ValueType::Float:
        {
            result << std::showpoint << std::fixed << std::setprecision(9) << getFloat();

            // Prevent a point to be the last character.
            if (result.str().back() == '.') {
                result << "0";
            }

            auto str = result.str();
            size_t i = str.length() - 1;
            for (; i >= 0; i--) {
                if (str[i] != '0') {
                    if (str[i] == '.')
                        i++;
                    break;
                }
            }
            return str.substr(0, i + 1);
        }
        case Pex::ValueType::Bool:
            result << (getBool() ? "True" : "False");
            break;
        default:
            result << "*error invalid value type #" << (uint8_t) type << "*";
            break;
    }

    return result.str();
}

/**
 * @brief Ensure the type of the value.
 * Check if the value is of the given type or throw an exception if not.
 * @param type The type enum
 */
void Pex::Value::ensureType(Pex::ValueType type) const
{
    if (m_Type != type)
    {
        throw std::runtime_error("Invalid type");
    }
}
```

## File: `Pex/Value.hpp`
```
#pragma once

#include <cstdint>

#include "StringTable.hpp"

namespace Pex {

/**
 * @brief Types managed in the Value class.
 */
enum class ValueType : std::uint8_t
{
    None = 0,
    Identifier = 1,
    String = 2,
    Integer = 3,
    Float = 4,
    Bool = 5
};

/**
 * @brief Variant class managing value.
 */
class Value
{
public:
    Value();
    explicit Value(const StringTable::Index& value, bool id = false);
    explicit Value(std::int32_t value);
    explicit Value(float value);
    explicit Value(bool value);
    ~Value();

    ValueType          getType() const;

    bool               isNone() const;
    void               clear();

    StringTable::Index getId() const;
    void               setId(const StringTable::Index& value);

    StringTable::Index getString() const;
    void               set(const StringTable::Index& value);

    std::int32_t       getInteger() const;
    void               set(std::int32_t value);

    float              getFloat() const;
    void               set(float value);

    bool               getBool() const;
    void               set(bool value);

    bool               operator==(const Value& rhs) const;

    std::string        toString() const;

protected:
    ValueType m_Type;
    union {
        struct {
            const StringTable* table;
            std::uint16_t      index;
        }                  string;
        std::int32_t       integer;
        float              real;
        bool               boolean;
    } m_Value;

    void ensureType(ValueType type) const;
};

}
```

## File: `Pex/Variable.cpp`
```cpp
#include "Variable.hpp"

#include <algorithm>
#include <assert.h>


/**
 * @brief Default constructor
 */
Pex::Variable::Variable()
{
    // set to false at first due to on-disk Skyrim scripts not having this flag
    m_ConstFlag = false;
}

/**
 * @brief Default destructor
 */
Pex::Variable::~Variable()
{
}

/**
 * @brief Get the default value of the variable.
 * @return The default value.
 */
const Pex::Value& Pex::Variable::getDefaultValue() const
{
    return m_DefaultValue;
}

/**
 * @brief Set the default a value of the variable.
 * @param value The new default value.
 */
void Pex::Variable::setDefaultValue(const Value &value)
{
    m_DefaultValue = value;
}


const Pex::Variable *Pex::Variables::findByName(const Pex::StringTable::Index &name) const
{
    auto nameIndex = name.asIndex();
    auto it = std::find_if(begin(), end(), [&] (const value_type& item) {return item.getName().asIndex() == nameIndex;});
    if (it == end())
    {
        return nullptr;
    }
    return & (*it);
}
```

## File: `Pex/Variable.hpp`
```
#pragma once

#include <vector>

#include "StringTable.hpp"
#include "NamedItem.hpp"
#include "TypedItem.hpp"
#include "UserFlagged.hpp"
#include "Value.hpp"

namespace Pex {

/**
 * @brief Variable definition.
 *
 * The variable are defined at the object level.
 */
class Variable :
        public NamedItem,
        public TypedItem,
        public UserFlagged
{
public:
    Variable();
    virtual ~Variable();

    const Value&       getDefaultValue() const;
    void               setDefaultValue(const Value& value);

    std::uint8_t getConstFlag() const { return m_ConstFlag; }
    void setConstFlag(std::uint8_t value) { m_ConstFlag = value; }

protected:
    Value              m_DefaultValue;
    std::uint8_t m_ConstFlag;

};

class Variables : public std::vector<Variable>
{
public:
    const Variable* findByName(const StringTable::Index& name) const;
};

}
```

## File: `Test/bin.cmd`
```

SETLOCAL

copy ..\build\Champollion.exe .
copy ..\build\Decompiler.dll .
copy ..\build\Pex.dll .

ENDLOCAL
```

## File: `Test/compile.cmd`
```
SETLOCAL
SET SKYRIM=E:\Games\JustCause\SteamApps\common\Skyrim

SET IN=%1
if [%1]==[] SET IN=decompiled -a

"%SKYRIM%\Papyrus compiler\PapyrusCompiler.exe" %IN% -f="%SKYRIM%\Data\Scripts\Source\TESV_Papyrus_Flags.flg" -i="decompiled" -o="Output" -keepasm

ENDLOCAL
```

## File: `Test/test_all.cmd`
```

SETLOCAL
SET SKYRIM=E:\Games\JustCause\SteamApps\common\Skyrim
SET BSAOUT=I:\Patches\Skyrim\BSAopt-247-1-6-3\out

Champollion.exe -p decompiled -t %BSAOUT%\scripts > output.txt
"%SKYRIM%\Papyrus compiler\PapyrusCompiler.exe" decompiled -a -f="%SKYRIM%\Data\Scripts\Source\TESV_Papyrus_Flags.flg" -i="decompiled" -o="Output" -keepasm > compile.txt

ENDLOCAL
```

## File: `Test/test_small.cmd`
```

SETLOCAL
SET SKYRIM=E:\Games\JustCause\SteamApps\common\Skyrim
SET BSAOUT=I:\Patches\Skyrim\BSAopt-247-1-6-3\out

DEL /Q Output\*.pex
DEL /Q *.psc
DEL /Q *.pex
DEL /Q *.pas
DEL /S *.pasm

ECHO "Failed recompilation" > failed.txt
IF [%1] == [] GOTO all
CALL :test %1
GOTO end

:all
FOR %%f IN (
	ArenaScript
	GlobalVariable
	AltarofMolagBalScript
	barreddoor
	bwclightdamagescript
	AbTGTrapsightScript
	BladeTrap
	CompanionsBladeFragmentTracking
	BFBdragonFlyoverSCRIPT
	ASX_Potions_drinkale01
	qf_mq101_0003372b
	ArenaExitDoorScript
	ActivateAgainAfterDelay
	cwarrowvolleyparentscript
) DO (
	call :test %%f
)
goto end


:test 
COPY %BSAOUT%\Scripts\%1.pex .
Champollion.exe -p decompiled -a asm %BSAOUT%\scripts\%1.pex 
"%SKYRIM%\Papyrus compiler\PapyrusCompiler.exe" decompiled\%1.psc -f="TESV_Papyrus_Flags.flg" -i="%SKYRIM%\Data\Scripts\Source" -o="Output"
IF NOT EXIST Output\%1.pex ECHO %1 >> failed.txt
goto :eof
:end
ENDLOCAL
```

## File: `cmake/Config.cmake.in`
```
@PACKAGE_INIT@
include(CMakeFindDependencyMacro)

include("${CMAKE_CURRENT_LIST_DIR}/@CHAMPOLLION_TARGETS_EXPORT_NAME@.cmake")
check_required_components("@CHAMPOLLION_TARGETS_EXPORT_NAME@")
```

