---
id: repo-fetched-champollion-082958
type: knowledge
owner: OA
registered_at: 2026-04-05T04:07:34.667408
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_Champollion_082958

## Assimilation Report
Auto-cloned repository: FETCHED_Champollion_082958

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### File: CHANGELOG.txt
```txt
0.0.1
 - Comandeered to support Fallout 4.

1.0.1
 - Fixed two missing opcodes for array_findelement and array_rfindelement
 
1.0.0
 - Initial release

```

### File: CMakeLists.txt
```txt
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

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for champollion
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

