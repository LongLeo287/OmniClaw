---
id: luau
type: knowledge
owner: OA_Triage
---
# luau
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
Luau ![CI](https://github.com/luau-lang/luau/actions/workflows/build.yml/badge.svg) [![codecov](https://codecov.io/gh/luau-lang/luau/branch/master/graph/badge.svg)](https://codecov.io/gh/luau-lang/luau)
====

Luau (lowercase u, /ˈlu.aʊ/) is a fast, small, safe, gradually typed embeddable scripting language derived from [Lua](https://lua.org).

It is designed to be backwards compatible with Lua 5.1, as well as incorporating [some features](https://luau.org/compatibility) from future Lua releases, but also expands the feature set (most notably with type annotations and a state-of-the-art type inference system). Luau is largely implemented from scratch, with the language runtime being a very heavily modified version of Lua 5.1 runtime, with completely rewritten interpreter and other [performance innovations](https://luau.org/performance). The runtime mostly preserves Lua 5.1 API, so existing bindings should be more or less compatible with a few caveats.

Luau is used by Roblox game developers to write game code, and by Roblox engineers to implement large parts of the user-facing application code as well as portions of the editor (Roblox Studio) as plugins. Roblox chose to open-source Luau to foster collaboration within the Roblox community as well as to allow other companies and communities to benefit from the ongoing language and runtime innovation. More recently, Luau has seen adoption in games like Alan Wake 2, Farming Simulator 2025, Second Life, and Warframe.

This repository hosts source code for the language implementation and associated tooling. Documentation for the language is available at https://luau.org/ and accepts contributions via [site repository](https://github.com/luau-lang/site); the language is evolved through RFCs that are located in [rfcs repository](https://github.com/luau-lang/rfcs).

# Usage

Luau is an embeddable programming language, but it also comes with two command-line tools by default, `luau` and `luau-analyze`.

`luau` is a command-line REPL and can also run input files. Note that REPL runs in a sandboxed environment and as such doesn't have access to the underlying file system except for ability to `require` modules.

`luau-analyze` is a command-line type checker and linter; given a set of input files, it produces errors/warnings according to the file configuration, which can be customized by using `--!` comments in the files or [`.luaurc`](https://rfcs.luau.org/config-luaurc) files. For details, please refer to our [type checking](https://luau.org/typecheck) and [linting](https://luau.org/lint) documentation. Our community maintains a language server frontend for `luau-analyze` called [luau-lsp](https://github.com/JohnnyMorganz/luau-lsp) for use with text editors.

# Installation

You can install and run Luau by downloading the compiled binaries from [a recent release](https://github.com/luau-lang/luau/releases); note that `luau` and `luau-analyze` binaries from the archives will need to be added to PATH or copied to a directory like `/usr/local/bin` on Linux/macOS.

Alternatively, you can use one of the packaged distributions (note that these are not maintained by Luau development team):

- macOS: [Install Homebrew](https://docs.brew.sh/Installation) and run `brew install luau`
- Arch Linux: Luau has been added to the official Arch Linux packages repository under the extras repository (see [``luau``](https://archlinux.org/packages/extra/x86_64/luau/)), simply install using ``pacman``: ``pacman -Syu luau``
- Alpine Linux: [Enable community repositories](https://wiki.alpinelinux.org/w/index.php?title=Enable_Community_Repository) and run `apk add luau`
- Gentoo Linux: Luau is [officially packaged by Gentoo](https://packages.gentoo.org/packages/dev-lang/luau) and can be installed using `emerge dev-lang/luau`. You may have to unmask the package first before installing it (which can be done by including the `--autounmask=y` option in the `emerge` command).

After installing, you will want to validate the installation was successful by running the test case [here](https://luau.org/getting-started).

## Building

On all platforms, you can use CMake to run the following commands to build Luau binaries from source:

```sh
mkdir cmake && cd cmake
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build . --target Luau.Repl.CLI --config RelWithDebInfo
cmake --build . --target Luau.Analyze.CLI --config RelWithDebInfo
```

Alternatively, on Linux and macOS, you can also use `make`:

```sh
make config=release luau luau-analyze
```

To integrate Luau into your CMake application projects as a library, at the minimum, you'll need to depend on `Luau.Compiler` and `Luau.VM` projects. From there you need to create a new Luau state (using Lua 5.x API such as `lua_newstate`), compile source to bytecode and load it into the VM like this:

```cpp
// needs lua.h and luacode.h
size_t bytecodeSize = 0;
char* bytecode = luau_compile(source, strlen(source), NULL, &bytecodeSize);
int result = luau_load(L, chunkname, bytecode, bytecodeSize, 0);
free(bytecode);

if (result == 0)
    return 1; /* return chunk main function */
```

For more details about the use of the host API, you currently need to consult [Lua 5.x API](https://www.lua.org/manual/5.1/manual.html#3). Luau closely tracks that API but has a few deviations, such as the need to compile source separately (which is important to be able to deploy VM without a compiler), and the lack of `__gc` support (use `lua_newuserdatadtor` instead).

To gain advantage of many performance improvements, it's highly recommended to use the `safeenv` feature, which sandboxes individual scripts' global tables from each other, and protects builtin libraries from monkey-patching. For this to work, you must call `luaL_sandbox` on the global state and `luaL_sandboxthread` for each new script's execution thread.

# Testing

Luau has an internal test suite; in CMake builds, it is split into two targets, `Luau.UnitTest` (for the bytecode compiler and type checker/linter tests) and `Luau.Conformance` (for the VM tests). The unit tests are written in C++, whereas the conformance tests are largely written in Luau (see `tests/conformance`).

Makefile builds combine both into a single target that can be run via `make test`.

# Dependencies

Luau uses C++ as its implementation language. The runtime requires C++11, while the compiler and analysis components require C++17. It should build without issues using Microsoft Visual Studio 2017 or later, or gcc-7 or clang-7 or later.

Other than the STL/CRT, Luau library components don't have external dependencies. The test suite depends on the [doctest](https://github.com/onqtam/doctest) testing framework, and the REPL command-line depends on [isocline](https://github.com/daanx/isocline).

# License

Luau implementation is distributed under the terms of [MIT License](https://github.com/luau-lang/luau/blob/master/LICENSE.txt). It is based on the Lua 5.x implementation, also under the MIT License.

When Luau is integrated into external projects, we ask that you honor the license agreement and include Luau attribution into the user-facing product documentation. Attribution making use of the [Luau logo](https://github.com/luau-lang/site/blob/master/logo.svg) is also encouraged when reasonable.

```

### File: tools\fuzz\requirements.txt
```txt
Jinja2==3.1.5
MarkupSafe==2.1.3

```

### File: CMakeLists.txt
```txt
# This file is part of the Luau programming language and is licensed under MIT License; see LICENSE.txt for details
if(EXT_PLATFORM_STRING)
    include(EXTLuau.cmake)
    return()
endif()

cmake_minimum_required(VERSION 3.10)

option(LUAU_BUILD_CLI "Build CLI" ON)
option(LUAU_BUILD_TESTS "Build tests" ON)
option(LUAU_BUILD_WEB "Build Web module" OFF)
option(LUAU_WERROR "Warnings as errors" OFF)
option(LUAU_STATIC_CRT "Link with the static CRT (/MT)" OFF)
option(LUAU_EXTERN_C "Use extern C for all APIs" OFF)
option(LUAU_BUILD_SHARED "Build as a shared library" OFF)

if(LUAU_BUILD_SHARED AND NOT LUAU_EXTERN_C)
    message(FATAL_ERROR "LUAU_BUILD_SHARED requires LUAU_EXTERN_C to be ON")
endif()

cmake_policy(SET CMP0054 NEW)
cmake_policy(SET CMP0091 NEW)

if(LUAU_STATIC_CRT)
    cmake_minimum_required(VERSION 3.15)
    set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
endif()

project(Luau LANGUAGES CXX C)

if (LUAU_BUILD_SHARED)
    add_library(Luau.Common SHARED)
    add_library(Luau.CLI.lib SHARED)
    add_library(Luau.Ast SHARED)
    add_library(Luau.Compiler SHARED)
    add_library(Luau.Config SHARED)
    add_library(Luau.Analysis SHARED)
    add_library(Luau.CodeGen SHARED)
    add_library(Luau.VM SHARED)
    add_library(Luau.Require SHARED)
    add_library(isocline SHARED)
else()
    add_library(Luau.Common STATIC)
    add_library(Luau.CLI.lib STATIC)
    add_library(Luau.Ast STATIC)
    add_library(Luau.Compiler STATIC)
    add_library(Luau.Config STATIC)
    add_library(Luau.Analysis STATIC)
    add_library(Luau.CodeGen STATIC)
    add_library(Luau.VM STATIC)
    add_library(Luau.Require STATIC)
    add_library(isocline STATIC)
endif()

if(LUAU_BUILD_CLI)
    add_executable(Luau.Repl.CLI)
    add_executable(Luau.Analyze.CLI)
    add_executable(Luau.Ast.CLI)
    add_executable(Luau.Reduce.CLI)
    add_executable(Luau.Compile.CLI)
    add_executable(Luau.Bytecode.CLI)

    # This also adds target `name` on Linux/macOS and `name.exe` on Windows
    set_target_properties(Luau.Repl.CLI PROPERTIES OUTPUT_NAME luau)
    set_target_properties(Luau.Analyze.CLI PROPERTIES OUTPUT_NAME luau-analyze)
    set_target_properties(Luau.Ast.CLI PROPERTIES OUTPUT_NAME luau-ast)
    set_target_properties(Luau.Reduce.CLI PROPERTIES OUTPUT_NAME luau-reduce)
    set_target_properties(Luau.Compile.CLI PROPERTIES OUTPUT_NAME luau-compile)
    set_target_properties(Luau.Bytecode.CLI PROPERTIES OUTPUT_NAME luau-bytecode)
endif()

if(LUAU_BUILD_TESTS)
    add_executable(Luau.UnitTest)
    add_executable(Luau.Conformance)
    add_executable(Luau.CLI.Test)
endif()

if(LUAU_BUILD_WEB)
    add_executable(Luau.Web)
endif()

# Proxy target to make it possible to depend on private VM headers
add_library(Luau.VM.Internals INTERFACE)

include(Sources.cmake)

target_compile_features(Luau.Common PUBLIC cxx_std_17)
target_include_directories(Luau.Common PUBLIC Common/include)

target_compile_features(Luau.CLI.lib PUBLIC cxx_std_17)
target_include_directories(Luau.CLI.lib PUBLIC CLI/include)
target_link_libraries(Luau.CLI.lib PRIVATE Luau.Common Luau.Config)

target_compile_features(Luau.Ast PUBLIC cxx_std_17)
target_include_directories(Luau.Ast PUBLIC Ast/include)
target_link_libraries(Luau.Ast PUBLIC Luau.Common)

target_compile_features(Luau.Compiler PUBLIC cxx_std_17)
target_include_directories(Luau.Compiler PUBLIC Compiler/include)
target_link_libraries(Luau.Compiler PUBLIC Luau.Ast)

target_compile_features(Luau.Config PUBLIC cxx_std_17)
target_include_directories(Luau.Config PUBLIC Config/include)
target_link_libraries(Luau.Config PUBLIC Luau.Ast)
target_link_libraries(Luau.Config PRIVATE Luau.Compiler Luau.VM)

target_compile_features(Luau.Analysis PUBLIC cxx_std_17)
target_include_directories(Luau.Analysis PUBLIC Analysis/include)
target_link_libraries(Luau.Analysis PUBLIC Luau.Ast Luau.Config)
target_link_libraries(Luau.Analysis PRIVATE Luau.Compiler Luau.VM)

target_compile_features(Luau.CodeGen PRIVATE cxx_std_17)
target_include_directories(Luau.CodeGen PUBLIC CodeGen/include)
target_link_libraries(Luau.CodeGen PRIVATE Luau.VM Luau.VM.Internals) # Code generation needs VM internals
target_link_libraries(Luau.CodeGen PUBLIC Luau.Common)

target_compile_features(Luau.VM PRIVATE cxx_std_11)
target_include_directories(Luau.VM PUBLIC VM/include)
target_link_libraries(Luau.VM PUBLIC Luau.Common)

target_compile_features(Luau.Require PUBLIC cxx_std_17)
target_include_directories(Luau.Require PUBLIC Require/include)
target_link_libraries(Luau.Require PUBLIC Luau.Config Luau.VM)

target_include_directories(isocline PUBLIC extern/isocline/include)

target_include_directories(Luau.VM.Internals INTERFACE VM/src)

set(LUAU_OPTIONS)

if(MSVC)
    list(APPEND LUAU_OPTIONS /D_CRT_SECURE_NO_WARNINGS) # We need to use the portable CRT functions.
    list(APPEND LUAU_OPTIONS "/we4018") # Signed/unsigned mismatch
    list(APPEND LUAU_OPTIONS "/we4388") # Also signed/unsigned mismatch
else()
    list(APPEND LUAU_OPTIONS -Wall) # All warnings
    list(APPEND LUAU_OPTIONS -Wimplicit-fallthrough)
    list(APPEND LUAU_OPTIONS -Wsign-compare) # This looks to be included in -Wall for GCC but not clang
endif()

if (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    list(APPEND LUAU_OPTIONS /MP) # Distribute single project compilation across multiple cores
endif()

if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    # Some gcc versions treat var in `if (type var = val)` as unused
    # Some gcc versions treat variables used in constexpr if blocks as unused
    list(APPEND LUAU_OPTIONS -Wno-unused)
    # some gcc versions warn maybe uninitialized on optional<string> members on structs
    list(APPEND LUAU_OPTIONS -Wno-maybe-uninitialized)
endif()

# Enabled in CI; we should be warning free on our main compiler versions but don't guarantee being warning free everywhere
if(LUAU_WERROR)
    if(MSVC)
        list(APPEND LUAU_OPTIONS /WX) # Warnings are errors
    else()
        list(APPEND LUAU_OPTIONS -Werror) # Warnings are errors
    endif()
endif()

if(LUAU_BUILD_WEB)
    # add -fexceptions for emscripten to allow exceptions to be caught in C++
    list(APPEND LUAU_OPTIONS -fexceptions)
endif()

set(ISOCLINE_OPTIONS)

if (NOT CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    list(APPEND ISOCLINE_OPTIONS -Wno-unused-function)
endif()

target_compile_options(Luau.Ast PRIVATE ${LUAU_OPTIONS})
target_compile_options(Luau.Analysis PRIVATE ${LUAU_OPTIONS})
target_compile_options(Luau.CLI.lib PRIVATE ${LUAU_OPTIONS})
target_compile_options(Luau.CodeGen PRIVATE ${LUAU_OPTIONS})
target_compile_options(Luau.VM PRIVATE ${LUAU_OPTIONS})
target_compile_options(isocline PRIVATE ${LUAU_OPTIONS} ${ISOCLINE_OPTIONS})

if(LUAU_EXTERN_C)
    # enable extern "C" for VM (lua.h, lualib.h) and Compiler (luacode.h) to make Luau friendlier to use from non-C++ languages
    # note that we enable LUA_USE_LONGJMP=1 as well; otherwise functions like luaL_error will throw C++ exceptions, which can't be done from extern "C" functions
    target_compile_definitions(Luau.VM PUBLIC LUA_USE_LONGJMP=1)

    if(LUAU_BUILD_SHARED)
        if(MSVC)
            target_compile_definitions(Luau.VM PUBLIC "LUA_API=extern \"C\" __declspec(dllexport)")
            target_compile_definitions(Luau.Compiler PUBLIC "LUACODE_API=extern \"C\" __declspec(dllexport)")
            target_compile_definitions(Luau.CodeGen PUBLIC "LUACODEGEN_API=extern \"C\" __declspec(dllexport)")
        else()
            # GCC/Clang
            target_compile_definitions(Luau.VM PUBLIC "LUA_API=extern \"C\" __attribute__((visibility(\"default\")))")
            target_compile_definitions(Luau.Compiler PUBLIC "LUACODE_API=extern \"C\" __attribute__((visibility(\"default\")))")
            target_compile_definitions(Luau.CodeGen PUBLIC "LUACODEGEN_API=extern \"C\" __attribute__((visibility(\"default\")))")
        endif()
    else()
        # For static builds (or if not exporting) just use extern "C"
        target_compile_definitions(Luau.VM PUBLIC "LUA_API=extern \"C\"")
        target_compile_definitions(Luau.Compiler PUBLIC "LUACODE_API=extern \"C\"")
        target_compile_definitions(Luau.CodeGen PUBLIC "LUACODEGEN_API=extern \"C\"")
    endif()
endif()

if (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC" AND MSVC_VERSION GREATER_EQUAL 1924)
    # disable partial redundancy elimination which regresses interpreter codegen substantially in VS2022:
    # https://developercommunity.visualstudio.com/t/performance-regression-on-a-complex-interpreter-lo/1631863
    set_source_files_properties(VM/src/lvmexecute.cpp PROPERTIES COMPILE_FLAGS /d2ssa-pre-)
endif()

if (NOT MSVC)
    # disable support for math_errno which allows compilers to lower sqrt() into a single CPU instruction
    target_compile_options(Luau.VM PRIVATE -fno-math-errno)
endif()

if(MSVC AND LUAU_BUILD_CLI)
    # the default stack size that MSVC linker uses is 1 MB; we need more stack space in Debug because stack frames are larger
    set_target_properties(Luau.Analyze.CLI PROPERTIES LINK_FLAGS_DEBUG /STACK:2097152)
    set_target_properties(Luau.Repl.CLI PROPERTIES LINK_FLAGS_DEBUG /STACK:2097152)
    set_target_properties(Luau.UnitTest PROPERTIES LINK_FLAGS_DEBUG /STACK:2097152)
endif()

if(MSVC AND LUAU_BUILD_TESTS)
    # the default stack size that MSVC linker uses is 1 MB; we need more stack space in Debug because stack frames are larger
    set_target_properties(Luau.CLI.Test PROPERTIES LINK_FLAGS_DEBUG /STACK:2097152)
endif()

# embed .natvis inside the library debug information
if(MSVC)
    target_link_options(Luau.Ast INTERFACE /NATVIS:${CMAKE_CURRENT_SOURCE_DIR}/tools/natvis/Ast.natvis)
    target_link_options(Luau.Analysis INTERFACE /NATVIS:${CMAKE_CURRENT_SOURCE_DIR}/tools/natvis/Analysis.natvis)
    target_link_options(Luau.CodeGen INTERFACE /NATVIS:${CMAKE_CURRENT_SOURCE_DIR}/tools/natvis/CodeGen.natvis)
    target_link_options(Luau.VM INTERFACE /NATVIS:${CMAKE_CURRENT_SOURCE_DIR}/tools/natvis/VM.natvis)
endif()

# make .natvis visible inside the solution
if(MSVC_IDE)
    target_sources(Luau.Ast PRIVATE tools/natvis/Ast.natvis)
    target_sources(Luau.Analysis PRIVATE tools/natvis/Analysis.natvis)
    target_sources(Luau.CodeGen PRIVATE tools/natvis/CodeGen.natvis)
    target_sources(Luau.VM PRIVATE tools/natvis/VM.natvis)
endif()

# On Windows and Android threads are provided, on Linux/Mac/iOS we use pthreads
add_library(osthreads INTERFACE)
if(CMAKE_SYSTEM_NAME MATCHES "Linux|Darwin|iOS")
    target_link_libraries(osthreads INTERFACE "-lpthread")
endif ()

if(LUAU_BUILD_CLI)
    target_compile_options(Luau.Repl.CLI PRIVATE ${LUAU_OPTIONS})
    target_compile_options(Luau.Reduce.CLI PRIVATE ${LUAU_OPTIONS})
    target_compile_options(Luau.Analyze.CLI PRIVATE ${LUAU_OPTIONS})
    target_compile_options(Luau.Ast.CLI PRIVATE ${LUAU_OPTIONS})
    target_compile_options(Luau.Compile.CLI PRIVATE ${LUAU_OPTIONS})
    target_compile_options(Luau.Bytecode.CLI PRIVATE ${LUAU_OPTIONS})

    target_include_directories(Luau.Repl.CLI PRIVATE extern extern/isocline/include)

    target_link_libraries(Luau.Repl.CLI PRIVATE Luau.Compiler Luau.Config Luau.CodeGen Luau.VM Luau.Require Luau.CLI.lib isocline)

    target_link_libraries(Luau.Repl.CLI PRIVATE osthreads)
    target_link_libraries(Luau.Reduce.CLI PRIVATE osthreads)
    target_link_libraries(Luau.Analyze.CLI PRIVATE osthreads)
    target_link_libraries(Luau.Ast.CLI PRIVATE osthreads)
    target_link_libraries(Luau.Compile.CLI PRIVATE osthreads)
    target_link_libraries(Luau.Bytecode.CLI PRIVATE osthreads)

    target_link_libraries(Luau.Analyze.CLI PRIVATE Luau.Analysis Luau.CLI.lib Luau.Require)

    target_link_libraries(Luau.Ast.CLI PRIVATE Luau.Ast Luau.Analysis Luau.CLI.lib)

    target_compile_features(Luau.Reduce.CLI PRIVATE cxx_std_17)
    target_include_directories(Luau.Reduce.CLI PUBLIC Reduce/include)
    target_link_libraries(Luau.Reduce.CLI PRIVATE Luau.Common Luau.Ast Luau.Analysis Luau.CLI.lib)

    target_link_libraries(Luau.Compile.CLI PRIVATE Luau.Compiler Luau.VM Luau.CodeGen Luau.CLI.lib)

    target_link_libraries(Luau.Bytecode.CLI PRIVATE Luau.Compiler Luau.VM Luau.CodeGen Luau.CLI.lib)
endif()

if(LUAU_BUILD_TESTS)
    target_compile_options(Luau.UnitTest PRIVATE ${LUAU_OPTIONS})
    target_compile_definitions(Luau.UnitTest PRIVATE DOCTEST_CONFIG_DOUBLE_STRINGIFY)
    target_include_directories(Luau.UnitTest PRIVATE extern)
    target_link_libraries(Luau.UnitTest PRIVATE Luau.Analysis Luau.Compiler Luau.CodeGen)

    target_compile_options(Luau.Conformance PRIVATE ${LUAU_OPTIONS})
    target_compile_definitions(Luau.Conformance PRIVATE DOCTEST_CONFIG_DOUBLE_STRINGIFY)
    target_include_directories(Luau.Conformance PRIVATE extern)
    target_link_libraries(Luau.Conformance PRIVATE Luau.Analysis Luau.Compiler Luau.CodeGen Luau.VM)
    if(CMAKE_SYSTEM_NAME MATCHES "Android|iOS")
        set(LUAU_CONFORMANCE_SOURCE_DIR "Client/Luau/tests/conformance")
    else ()
        file(REAL_PATH "tests/conformance" LUAU_CONFORMANCE_SOURCE_DIR)
    endif ()
    target_compile_definitions(Luau.Conformance PRIVATE LUAU_CONFORMANCE_SOURCE_DIR="${LUAU_CONFORMANCE_SOURCE_DIR}")

    target_compile_options(Luau.CLI.Test PRIVATE ${LUAU_OPTIONS})
    target_include_directories(Luau.CLI.Test PRIVATE extern CLI)
    target_link_libraries(Luau.CLI.Test PRIVATE Luau.Compiler Luau.Config Luau.CodeGen Luau.VM Luau.Require Luau.CLI.lib isocline)
    target_link_libraries(Luau.CLI.Test PRIVATE osthreads)

    add_subdirectory(fuzz)
endif()

if(LUAU_BUILD_WEB)
    target_compile_options(Luau.Web PRIVATE ${LUAU_OPTIONS})
    target_link_libraries(Luau.Web PRIVATE Luau.Compiler Luau.VM Luau.Analysis)

    # declare exported functions to emscripten
    target_link_options(Luau.Web PRIVATE -sEXPORTED_FUNCTIONS=["_executeScript","_checkScript"] -sEXPORTED_RUNTIME_METHODS=["ccall","cwrap"])

    # add -fexceptions for emscripten to allow exceptions to be caught in C++
    target_link_options(Luau.Web PRIVATE -fexceptions)

    # the output is a single .js file with an embedded wasm blob
    target_link_options(Luau.Web PRIVATE -sSINGLE_FILE=1)
endif()

# validate dependencies for internal libraries
foreach(LIB Luau.Ast Luau.Compiler Luau.Config Luau.Analysis Luau.CodeGen Luau.VM)
    if(TARGET ${LIB})
        get_target_property(DEPENDS ${LIB} LINK_LIBRARIES)
        if(LIB MATCHES "CodeGen|VM" AND DEPENDS MATCHES "Ast|Analysis|Config|Compiler")
            message(FATAL_ERROR ${LIB} " is a runtime component but it depends on one of the offline components")
        endif()
        if(LIB MATCHES "Ast|Compiler" AND DEPENDS MATCHES "CodeGen|VM")
            message(FATAL_ERROR ${LIB} " is an offline component but it depends on one of the runtime components")
        endif()
        if(LIB MATCHES "Ast|Compiler" AND DEPENDS MATCHES "Analysis|Config")
            message(FATAL_ERROR ${LIB} " is a compiler component but it depends on one of the analysis components")
        endif()
    endif()
endforeach()

```

### File: CMakePresets.json
```json
{
    "version": 6,
    "configurePresets": [
        {
            "name": "fuzz",
            "displayName": "Fuzz",
            "description": "Configures required fuzzer settings.",
            "binaryDir": "build",
            "condition": {
                "type": "anyOf",
                "conditions": [
                    {
                        "type": "equals",
                        "lhs": "${hostSystemName}",
                        "rhs": "Darwin"
                    },
                    {
                        "type": "equals",
                        "lhs": "${hostSystemName}",
                        "rhs": "Linux"
                    }
                ]
            },
            "cacheVariables": {
                "CMAKE_OSX_ARCHITECTURES": "x86_64",
                "CMAKE_BUILD_TYPE": "Release",
                "CMAKE_CXX_STANDARD": "17",
                "CMAKE_CXX_EXTENSIONS": false
            },
            "warnings": {
                "dev": false
            }
        }
    ],
    "buildPresets": [
        {
            "name": "fuzz-proto",
            "displayName": "Protobuf Fuzzer",
            "description": "Builds the protobuf-based fuzzer and transpiler tools.",
            "configurePreset": "fuzz",
            "targets": [
                "Luau.Fuzz.Proto",
                "Luau.Fuzz.ProtoTest"
            ]
        }
    ]
}

```

### File: CONTRIBUTING.md
```md
Thanks for deciding to contribute to Luau! These guidelines will try to help make the process painless and efficient.

## Questions

If you have a question regarding the language usage/implementation, please [use GitHub discussions](https://github.com/luau-lang/luau/discussions).
Some questions just need answers, but it's nice to keep them for future reference in case other people want to know the same thing.
Some questions help improve the language, implementation or documentation by inspiring future changes.

## Documentation

A [separate site repository](https://github.com/luau-lang/site) hosts the language documentation, which is accessible on https://luau.org.
Changes to this documentation that improve clarity, fix grammatical issues, explain aspects that haven't been explained before and the like are warmly welcomed.

Please feel free to [create a pull request](https://help.github.com/articles/about-pull-requests/) to improve our documentation. Note that at this point the documentation is English-only.

## Bugs

If the language implementation doesn't compile on your system, compiles with warnings, doesn't seem to run correctly for your code or if anything else is amiss, please [open a GitHub issue](https://github.com/luau-lang/luau/issues/new).
It helps if you note the Git revision issue happens in, the version of your compiler for compilation issues, and a reproduction case for runtime bugs.

Of course, feel free to [create a pull request](https://help.github.com/articles/about-pull-requests/) to fix the bug yourself.

## Features

If you're thinking of adding a new feature to the language, library, analysis tools, etc., please *don't* start by submitting a pull request.
The Luau team has internal priorities and a roadmap that may or may not align with specific features, so before starting to work on a feature, please submit an issue describing the missing feature that you'd like to add.

For features that result in an observable change to the language's syntax or semantics, you'll need to [create an RFC](https://github.com/luau-lang/rfcs/blob/master/README.md) to make sure that the feature is needed and well-designed.

Finally, please note that Luau tries to carry a minimal feature set. All features must be evaluated not just for the benefits that they provide, but also for the downsides/costs in terms of language simplicity, maintainability, cross-feature interaction, etc.
As such, feature requests may not be accepted even if a comprehensive RFC is written - don't expect Luau to gain a feature just because another programming language has it.
We generally apply a standard similar to the C\# team's famous [Minus 100 Points](https://learn.microsoft.com/en-us/archive/blogs/ericgu/minus-100-points).

## Code style

Contributions to this project are expected to follow the existing code style.
`.clang-format` file mostly defines syntactic styling rules (you can run `make format` to format the code accordingly).

As for naming conventions, most Luau components use `lowerCamelCase` for variables and functions, `UpperCamelCase` for types and enums, `kCamelCase` for global constants and `SCARY_CASE` for macros.

Within the VM component, the code style is different - we expect `lua_` or `luaX_` prefix for functions that are public or used across different VM files, camel case isn't used and macros are often using lowercase.

## Testing

All pull requests will run through a continuous integration pipeline using GitHub Actions that will run the built-in unit tests and integration tests on Windows, macOS and Linux.
You can run the tests yourself using `make test` or using `cmake` to build `Luau.UnitTest` and `Luau.Conformance` and run them.

When making code changes please try to make sure they are covered by an existing test or add a new test accordingly.

## Performance

One of the central features of Luau is performance; our runtime in particular is heavily optimized for high performance and low memory consumption, and code is generally carefully tuned to result in close-to-optimal assembly for x64 and AArch64 architectures. The analysis code is not optimized to the same level of detail, but performance is still very important to make sure that we can support interactive IDE features.

As such, it's important to make sure that the changes, including bug fixes, improve (or at least do not regress) performance. For the VM, this can be validated by running `bench/bench.py` on two binaries built in Release mode, before and after the changes. Note that our benchmark coverage is not complete, and in some cases, additional performance testing will be necessary to determine if the change can be merged.

## Feature flags

For large bug fixes or features that apply to the Luau components and not just the CLI tools, we may ask that you introduce a feature flag to gate your changes. The feature flags use `LUAU_FASTFLAG` macro family defined in `Luau/Common.h` and allow us to ensure that the change can be safely shipped, enabled, and rolled back on the Roblox platform when the change makes it into our production codebase. The tests run the code with flags in their default state and enabled state as well to ensure correctness.

## Licensing

By contributing changes to this repository, you license your contribution under the MIT License, and you agree that you have the right to license your contribution under those terms.

```

### File: LICENSE.txt
```txt
MIT License

Copyright (c) 2019-2025 Roblox Corporation
Copyright (c) 1994–2019 Lua.org, PUC-Rio.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

### File: lua_LICENSE.txt
```txt
Copyright © 1994–2019 Lua.org, PUC-Rio.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 

```

### File: SECURITY.md
```md
# Security Guarantees

Luau provides a safe sandbox that scripts can not escape from, short of vulnerabilities in custom C functions exposed by the host. This includes the virtual machine, builtin libraries and native code generation facilities.

Any source code can not result in memory safety errors or crashes during its compilation or execution. Violations of memory safety are considered vulnerabilities.

Note that Luau does not provide termination guarantees - some code may exhaust CPU or RAM resources on the system during compilation or execution.

The runtime expects valid bytecode as an input. Feeding bytecode that was not produced by Luau compiler into the VM is not supported, and
doesn't come with any security guarantees; make sure to sign and/or encrypt the bytecode when it crosses a network or file system boundary to avoid tampering.

# Reporting a Vulnerability

You can report security bugs via [HackerOne](https://hackerone.com/roblox). Please refer to the linked page for rules of the bounty program.

```

### File: bench\bench.py
```py
#!/usr/bin/python3
# This file is part of the Luau programming language and is licensed under MIT License; see LICENSE.txt for details
import argparse
import os
import subprocess
import math
import sys
import re
import json

# Taken from rotest
from color import colored, Color
from tabulate import TablePrinter, Alignment

try:
    import matplotlib
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    matplotlib = None

try:
    import scipy
    from scipy import stats
except ModuleNotFoundError:
    print("Warning: scipy package is not installed, confidence values will not be available")
    stats = None

scriptdir = os.path.dirname(os.path.realpath(__file__))
defaultVm = 'luau.exe' if os.name == "nt" else './luau'

argumentParser = argparse.ArgumentParser(description='Benchmark Lua script execution with an option to compare different VMs')

argumentParser.add_argument('--vm', dest='vm',default=defaultVm,help='Lua executable to test (' + defaultVm + ' by default)')
argumentParser.add_argument('--folder', dest='folder',default=os.path.join(scriptdir, 'tests'),help='Folder with tests (tests by default)')
argumentParser.add_argument('--compare', dest='vmNext',type=str,nargs='*',help='List of Lua executables to compare against')
argumentParser.add_argument('--results', dest='results',type=str,nargs='*',help='List of json result files to compare and graph')
argumentParser.add_argument('--run-test', action='store', default=None, help='Regex test filter')
argumentParser.add_argument('--extra-loops', action='store',type=int,default=0, help='Amount of times to loop over one test (one test already performs multiple runs)')
argumentParser.add_argument('--filename', action='store',type=str,default='bench', help='File name for graph and results file')
argumentParser.add_argument('--callgrind', dest='callgrind',action='store_const',const=1,default=0,help='Use callgrind to run benchmarks')
argumentParser.add_argument('--show-commands', dest='show_commands',action='store_const',const=1,default=0,help='Show the command line used to launch the VM and tests')

if matplotlib != None:
    argumentParser.add_argument('--absolute', dest='absolute',action='store_const',const=1,default=0,help='Display absolute values instead of relative (enabled by default when benchmarking a single VM)')
    argumentParser.add_argument('--speedup', dest='speedup',action='store_const',const=1,default=0,help='Draw a speedup graph')
    argumentParser.add_argument('--sort', dest='sort',action='store_const',const=1,default=0,help='Sort values from worst to best improvements, ignoring conf. int. (disabled by default)')
    argumentParser.add_argument('--window', dest='window',action='store_const',const=1,default=0,help='Display window with resulting plot (disabled by default)')
    argumentParser.add_argument('--graph-vertical', action='store_true',dest='graph_vertical', help="Draw graph with vertical bars instead of horizontal")

argumentParser.add_argument('--report-metrics', dest='report_metrics', help="Send metrics about this session to InfluxDB URL upon completion.")

argumentParser.add_argument('--print-influx-debugging', action='store_true', dest='print_influx_debugging', help="Print output to aid in debugging of influx metrics reporting.")
argumentParser.add_argument('--no-print-influx-debugging', action='store_false', dest='print_influx_debugging', help="Don't print output to aid in debugging of influx metrics reporting.")

argumentParser.add_argument('--no-print-final-summary', action='store_false', dest='print_final_summary', help="Don't print a table summarizing the results after all tests are run")

# Assume 2.5 IPC on a 4 GHz CPU; this is obviously incorrect but it allows us to display simulated instruction counts using regular time units
CALLGRIND_INSN_PER_SEC = 2.5 * 4e9

def arrayRange(count):
    result = []

    for i in range(count):
        result.append(i)

    return result

def arrayRangeOffset(count, offset):
    result = []

    for i in range(count):
        result.append(i + offset)

    return result

def getCallgrindOutput(stdout, lines):
    result = []
    name = None

    for l in lines:
        if l.startswith("desc: Trigger: Client Request: "):
            name = l[31:].strip()
        elif l.startswith("summary: ") and name != None:
            insn = int(l[9:])
            # Note: we only run each bench once under callgrind so we only report a single time per run; callgrind instruction count variance is ~0.01% so it might as well be zero
            result += "|><|" + name + "|><|" + str(insn / CALLGRIND_INSN_PER_SEC * 1000.0) + "||_||"
            name = None

    # If no results were found above, this may indicate the native executable running
    # the benchmark doesn't have support for callgrind builtin.  In that case just
    # report the "totals" from the output file.
    if len(result) == 0:
        elements = stdout.decode('utf8').split("|><|")
        if len(elements) >= 2:
            name = elements[1]

            for l in lines:
                if l.startswith("totals: "):
                    insn = int(l[8:])
                    # Note: we only run each bench once under callgrind so we only report a single time per run; callgrind instruction count variance is ~0.01% so it might as well be zero
                    result += "|><|" + name + "|><|" + str(insn / CALLGRIND_INSN_PER_SEC * 1000.0) + "||_||"

    return "".join(result)

def conditionallyShowCommand(cmd):
    if arguments.show_commands:
        print(f'{colored(Color.BLUE, "EXECUTING")}: {cmd}')

def checkValgrindExecutable():
    """Return true if valgrind can be successfully spawned"""
    try:
        subprocess.check_call("valgrind --version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        print(f"{colored(Color.YELLOW, 'WARNING')}: Unable to spawn 'valgrind'.  Please ensure valgrind is installed when using '--callgrind'.")
        return False
    
    return True

def getVmOutput(cmd):
    if os.name == "nt":
        try:
            fullCmd = "start /realtime /affinity 1 /b /wait cmd /C \"" + cmd + "\""
            conditionallyShowCommand(fullCmd)
            return subprocess.check_output(fullCmd, shell=True, cwd=scriptdir).decode()
        except KeyboardInterrupt:
            exit(1)
        except:
            return ""
    elif arguments.callgrind:
        if not checkValgrindExecutable():
            return ""
        output_path = os.path.join(scriptdir, "callgrind.out")
        try:
            os.unlink(output_path)  # Remove stale output
        except:
            pass
        fullCmd = "valgrind --tool=callgrind --callgrind-out-file=callgrind.out --combine-dumps=yes --dump-line=no " + cmd
        conditionallyShowCommand(fullCmd)
        try:
            output = subprocess.check_output(fullCmd, shell=True, stderr=subprocess.DEVNULL, cwd=scriptdir)
        except subprocess.CalledProcessError as e:
            print(f"{colored(Color.YELLOW, 'WARNING')}: Valgrind returned error code {e.returncode}")
            output = e.output
        with open(output_path, "r") as file:
            lines = file.readlines()
        os.unlink(output_path)
        return getCallgrindOutput(output, lines)
    else:
        conditionallyShowCommand(cmd)
        with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=scriptdir) as p:
            # Try to lock to a single processor
            if sys.platform != "darwin":
                os.sched_setaffinity(p.pid, { 0 })

            # Try to set high priority (requires sudo)
            try:
                os.nice(-10)
            except:
                pass

            return p.communicate()[0]

def getShortVmName(name):
    # Hope that the path to executable doesn't contain spaces
    argumentPos = name.find(" ")

    if argumentPos != -1:
        executableName = name[0:argumentPos]
        arguments = name[argumentPos+1:]

        pathPos = executableName.rfind("\\")

        if pathPos == -1:
            pathPos = executableName.rfind("/")

        if pathPos != -1:
            executableName = executableName[pathPos+1:]

        return executableName + " " + arguments

    pathPos = name.rfind("\\")

    if pathPos == -1:
        pathPos = name.rfind("/")

    if pathPos != -1:
        return name[pathPos+1:]

    return name

class TestResult:
    filename = ""
    vm = ""
    shortVm = ""
    name = ""

    values = []
    count = 0
    min = None
    avg = 0
    max = None

    sampleStdDev = 0
    unbiasedEst = 0
    sampleConfidenceInterval = 0

def extractResult(filename, vm, output):
    elements = output.split("|><|")

    # Remove test output
    elements.remove(elements[0])

    result = TestResult()

    result.filename = filename
    result.vm = vm
    result.shortVm = getShortVmName(vm)

    result.name = elements[0]
    elements.remove(elements[0])

    timeTable = []

    for el in elements:
        timeTable.append(float(el))

    result.values = timeTable
    result.count = len(timeTable)

    return result

def mergeResult(lhs, rhs):
    for value in rhs.values:
        lhs.values.append(value)

    lhs.count = len(lhs.values)

def mergeResults(lhs, rhs):
    for a, b in zip(lhs, rhs):
        mergeResult(a, b)

def finalizeResult(result):
    total = 0.0

    # Compute basic parameters
    for v in result.values:
        if result.min == None or v < result.min:
            result.min = v

        if result.max == None or v > result.max:
            result.max = v

        total = total + v

    if result.count > 0:
        result.avg = total / result.count
    else:
        result.avg = 0

    # Compute standard deviation
    sumOfSquares = 0

    for v in result.values:
        sumOfSquares = sumOfSquares + (v - result.avg) ** 2

    if result.count > 1:
        result.sampleStdDev = math.sqrt(sumOfSquares / (result.count - 1))
        result.unbiasedEst = result.sampleStdDev * result.sampleStdDev

        if stats:
            # Two-tailed distribution with 95% conf.
            tValue = stats.t.ppf(1 - 0.05 / 2, result.count - 1)

            # Compute confidence interval
            result.sampleConfidenceInterval = tValue * result.sampleStdDev / math.sqrt(result.count)
        else:
            result.sampleConfidenceInterval = result.sampleStdDev
    else:
        result.sampleStdDev = 0
        result.unbiasedEst = 0
        result.sampleConfidenceInterval = 0

    return result

# Full result set
allResults = []


# Data for the graph
plotLegend = []

plotLabels = []

plotValueLists = []
plotConfIntLists = []

# Totals
vmTotalMin = []
vmTotalAverage = []
vmTotalImprovement = []
vmTotalResults = []

# Data for Telegraf report
mainTotalMin = 0
mainTotalAverage = 0
mainTotalMax = 0

def getExtraArguments(filepath):
    try:
        with open(filepath) as f:
            for i in f.readlines():
                pos = i.find("--bench-args:")
                if pos != -1:
                    return i[pos + 13:].strip()
    except:
        pass

    return ""

def substituteArguments(cmd, extra):
    if argumentSubstituionCallback != None:
        cmd = argumentSubstituionCallback(cmd)

    if cmd.find("@EXTRA") != -1:
        cmd = cmd.replace("@EXTRA", extra)
    else:
        cmd = cmd + " " + extra

    return cmd

def extractResults(filename, vm, output, allowFailure):
    results = []

    splitOutput = output.split("||_||")

    if len(splitOutput) <= 1:
        if allowFailure:
            result = TestResult()

            result.filename = filename
            result.vm = vm
            result.shortVm = getShortVmName(vm)

            results.append(result)

        return results

    splitOutput.remove(splitOutput[len(splitOutput) - 1])

    for el in splitOutput:
        results.append(extractResult(filename, vm, el))

    return results

def analyzeResult(subdir, main, comparisons):
    # Aggregate statistics
    global mainTotalMin, mainTotalAverage, mainTotalMax

    mainTotalMin = mainTotalMin + main.min
    mainTotalAverage = mainTotalAverage + main.avg
    mainTotalMax = mainTotalMax + main.max

    if arguments.vmNext != None:
        resultPrinter.add_row({
            'Test': main.name,
            'Min': '{:8.3f}ms'.format(main.min),
            'Average': '{:8.3f}ms'.format(main.avg),
            'StdDev%': '{:8.3f}%'.format(main.sampleConfidenceInterval / main.avg * 100),
            'Driver': main.shortVm,
            'Speedup': "",
            'Significance': "",
            'P(T<=t)': ""
        })
    else:
        resultPrinter.add_row({
            'Test': main.name,
            'Min': '{:8.3f}ms'.format(main.min),
            'Average': '{:8.3f}ms'.format(main.avg),
            'StdDev%': '{:8.3f}%'.format(main.sampleConfidenceInterval / main.avg * 100),
            'Driver': main.shortVm
        })

    if influxReporter != None:
        influxReporter.report_result(subdir, main.name, main.filename, "SUCCESS", main.min, main.avg, main.max, main.sampleConfidenceInterval, main.shortVm, main.vm)

    print(colored(Color.GREEN, 'SUCCESS') + ': {:<40}'.format(main.name) + ": " + '{:8.3f}'.format(main.avg) + "ms +/- " +
        '{:6.3f}'.format(main.sampleConfidenceInterval / main.avg * 100) + "% on " + main.shortVm)

    plotLabels.append(main.name)

    index = 0

    if len(plotValueLists) < index + 1:
        plotValueLists.append([])
        plotConfIntLists.append([])

        vmTotalMin.append(0.0)
        vmTotalAverage.append(0.0)
        vmTotalImprovement.append(0.0)
        vmTotalResults.append(0)

    if arguments.absolute or arguments.speedup:
        scale = 1
    else:
        scale = 100 / main.avg

    plotValueLists[index].append(main.avg * scale)
    plotConfIntLists[index].append(main.sampleConfidenceInterval * scale)

    vmTotalMin[index] += main.min
    vmTotalAverage[index] += main.avg

    for compare in comparisons:
        index = index + 1

        if len(plotValueLists) < index + 1 and not arguments.speedup:
            plotValueLists.append([])
            plotConfIntLists.append([])

            vmTotalMin.append(0.0)
            vmTotalAverage.append(0.0)
            vmTotalImprovement.append(0.0)
            vmTotalResults.append(0)

        if compare.min == None:
            print(colored(Color.RED, 'FAILED') + ":  '" + main.name + "' on '" + compare.vm +  "'")

            resultPrinter.add_row({ 'Test': main.name, 'Min': "", 'Average': "FAILED", 'StdDev%': "", 'Driver': compare.shortVm, 'Speedup': "", 'Significance': "", 'P(T<=t)': "" })

            if influxReporter != None:
                influxReporter.report_result(subdir, main.filename, main.filename, "FAILED", 0.0, 0.0, 0.0, 0.0, compare.shortVm, compare.vm)

            if arguments.speedup:
                plotValueLists[0].pop()
                plotValueLists[0].append(0)

                plotConfIntLists[0].pop()
                plotConfIntLists[0
... [TRUNCATED]
```

### File: bench\color.py
```py
# This file is part of the Luau programming language and is licensed under MIT License; see LICENSE.txt for details
from enum import Enum
import sys

class Color(Enum):
    DEFAULT = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    WHITE = 5

def colored_on(color:Color, message:str):
    from colorama import Fore, Style
    color_mappings = {
        Color.DEFAULT: (Fore.WHITE, Style.NORMAL),
        Color.RED: (Fore.RED, Style.NORMAL),
        Color.GREEN: (Fore.GREEN, Style.NORMAL),
        Color.BLUE: (Fore.BLUE, Style.BRIGHT),
        Color.YELLOW: (Fore.YELLOW, Style.NORMAL),
        Color.WHITE: (Fore.WHITE, Style.BRIGHT)
    }
    fore, style = color_mappings[color]
    return fore + style + message + Style.RESET_ALL

def colored_off(color:Color, message:str):
    return message

try:
    if sys.stdout.isatty():
        import colorama
        colorama.init()
        colored = colored_on
    else:
        colored = colored_off
except:
    colored = colored_off

```

### File: bench\influxbench.py
```py
# This file is part of the Luau programming language and is licensed under MIT License; see LICENSE.txt for details
import os
import platform
import shlex
import socket
import sys
import requests

_hostname = socket.gethostname()

def tag_value(value):
    value = str(value)
    for escape in [',', '=', ' ']:
        value = value.replace(escape, '\\' + escape)
    return value

def field_value(value):
    # Line protocol requires all strings to be quoted
    if not isinstance(value, str):
        return str(value).lower()

    # String values must always be surrounded in unescaped double quotes, while escaping inner quotes with a
    # backslash.
    return '"' + value.replace('"', '\\"') + '"'

class InfluxReporter:
    def __init__(self, args):
        self.args = args
        self.lines = []

    def _send_line_message(self, tags, fields):
        tags_str = ','.join(sorted(tags))
        fields_str = ','.join(fields)
        line_message = '{},{} {}'.format('robench', tags_str, fields_str)

        self.lines.append(line_message)
        if self.args.print_influx_debugging:
            print('[influx] ' + line_message)

    def flush(self, process_exit_code):
        if self.args.report_metrics:
            print('Reporting results to Influx.')
            request = '\n'.join(self.lines)
            try:
                # We don't want a failure to report metrics to influx to result in a failed test suite.
                # Just log a warning instead.
                response = requests.post(url=self.args.report_metrics, data=request)
            except Exception as e:
                print("Unable to report metrics to influx.  Reason: " + str(e))
                print('Request content (for debugging): ')
                print(request)
                pass

    def report_result(self, testFolder, testName, testPath, status, timeMin, timeAvg, timeMax, confInt, vmName, vmPath):
        is_teamcity = 'TEAMCITY_PROJECT_NAME' in os.environ
        tags = [
            'hostname={}'.format(tag_value(_hostname)),
            'is_teamcity={}'.format(tag_value(is_teamcity)),
            'platform={}'.format(tag_value(sys.platform)),
            'type=event',

            # Necessary in order for ElasticSearch to accept this line
            'priority=high',

            'test_folder={}'.format(tag_value(testFolder)),
            'test_name={}'.format(tag_value(testName)),
            'test_path={}'.format(tag_value(testPath)),

            'vm_name={}'.format(tag_value(vmName)),
            'vm_path={}'.format(tag_value(vmPath))
        ]
        fields = [
            'status={}'.format(field_value(status)),
            'time_min={}'.format(timeMin),
            'time_avg={}'.format(timeAvg),
            'time_max={}'.format(timeMax),
            'time_conf_int={}'.format(confInt)
        ]

        self._send_line_message(tags, fields)

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
