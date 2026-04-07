---
id: polyfill
type: knowledge
owner: OA_Triage
---
# polyfill
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
## polyfill-glibc

How often have you compiled a C/C++ program on a recent Linux system, tried to run that compiled program on an older Linux system, and then hit a GLIBC version error?
Concretely, perhaps you're seeing something like this:

```
new-system$ gcc my-program.c -o my-program
old-system$ scp new-system:my-program .
old-system$ ./my-program
./my-program: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.28' not found (required by ./my-program)
```

The motivating idea behind polyfill-glibc is that an extra post-compilation step can prevent these errors from happening:

```
new-system$ gcc my-program.c -o my-program
new-system$ polyfill-glibc --target-glibc=2.17 my-program
old-system$ scp new-system:my-program .
old-system$ ./my-program
It works!
```

## Build and run instructions

To build polyfill-glibc, you'll need a git client, a C11 compiler (such as `gcc`), and [`ninja`](https://github.com/ninja-build/ninja/wiki/Pre-built-Ninja-packages). With these tools present, the build process is:

```
$ git clone https://github.com/corsix/polyfill-glibc.git
$ cd polyfill-glibc
$ ninja polyfill-glibc
```

Once built, running it is intended to be as simple as passing the oldest version of glibc you want to support, along with the path to the program (or shared library) to modify, as in:
```
$ ./polyfill-glibc --target-glibc=2.17 /path/to/my-program
```

If running it _isn't_ this simple, then open a GitHub issue describing why not, and we'll try to improve things.

Note that at present, the `--target-glibc` operation of polyfill-glibc is only implemented for x86_64 and aarch64. If other architectures are of interest to you, open a GitHub issue so that we can gauge demand.

If distributing shared libraries, polyfill-glibc can also be used to inspect dependencies (with the `--print-imports` and `--print-exports` operations), and to modify how shared libraries are loaded (with the `--set-rpath`, `--set-runpath`, and `--set-soname` operations). Consult [the documentation](docs/Command_line_options.md) for a full list of command line options.

## License

polyfill-glibc itself is made available under the [MIT license](https://opensource.org/license/mit). The polyfilling procedure can sometimes involve linking small pieces of polyfill-glibc into the file being modified; the "the above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software" clause of the MIT license is explicitly waived for any such pieces.

```

### File: docs\Asynchronous_cancellation.md
```md
## Asynchronous cancellation

The [`pthread_cancel`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cancel.html) function is defective by design and should not be used. See [How to stop Linux threads cleanly](https://mazzo.li/posts/stopping-linux-threads.html) for a tour of the problem and various better solutions. That said, some applications still (misguidedly) make use of `pthread_cancel`, and some special caveats apply when polyfilling said applications.

## What does `pthread_cancel` do?

Every thread has three pieces of state:

|Variable name|Possible values|Initial value|Changed by|
|-------------|---------------|-------------|----------|
|Cancel state|ENABLE, DISABLE|ENABLE|[`pthread_setcancelstate`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_setcancelstate.html)|
|Cancel type|DEFERRED, ASYNCHRONOUS|DEFERRED|[`pthread_setcanceltype`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_setcancelstate.html)|
|Cancel requested|NO, YES|NO|[`pthread_cancel`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cancel.html) (always changes to YES)|

A thread will be terminated (possibly with cleanup functions / destructors being called), if either of the following state combinations occur:
1. _Cancel requested_ is YES, _Cancel state_ is ENABLE, _Cancel type_ is ASYNCHRONOUS.
2. _Cancel requested_ is YES, _Cancel state_ is ENABLE, _Cancel type_ is DEFERRED, and the thread calls a libc function defined as a cancellation point.

Roughly speaking, every libc function that _could_ block execution for a non-trivial amount of time is defined as a cancellation point. This includes, but is not limited to, the following functions:
* `accept`
* `close`
* `connect`
* `copy_file_range`
* `epoll_wait` / `epoll_pwait` / `epoll_pwait2`
* `fcntl` (when called with `F_SETLKW` or `F_OFD_SETLKW`)
* `fsync` / `fdatasync` / `sync_file_range` / `msync`
* `getrandom`
* `open` / `openat` / `open_by_handle_at`
* `pause` / `sigpause` / `sigsuspend`
* `pthread_testcancel`
* `read` / `readv` / `pread`
* `recv` / `recvfrom` / `recvmsg` / `recvmmsg` / `msgrcv` / `mq_receive` / `mq_timedreceive`
* `send` / `sendto` / `sendmsg` / `sendmmsg` / `msgsnd` / `mq_send` / `mq_timedsend`
* `sigwait` / `sigwaitinfo` / `sigtimedwait`
* `sleep` / `usleep` / `nanosleep` / `clock_nanosleep`
* `write` / `writev` / `pwrite`

## glibc semantics of cancellation points

Taking `epoll_pwait2` as an example, at the time of writing, the glibc implementation of `epoll_pwait2` is roughly:

```c
old_type = pthread_setcanceltype(ASYNCHRONOUS);
result = syscall(epoll_pwait2, ...);
pthread_setcanceltype(old_type);
check_for_pthread_cancel_race();
return result;
```

When `pthread_cancel` is called, if the target thread has _Cancel state_ of ENABLE and _Cancel type_ of ASYNCHRONOUS, then a signal is sent to the target thread. Shortly thereafter, the signal will be received by the target thread, wherein the signal handler confirms that _Cancel state_ is still ENABLE and _Cancel type_ is still ASYNCHRONOUS. If so, the thread will be terminated. If not, the signal handler will do nothing (though delivery of the signal might cause an `EINTR` result from an unrelated syscall that was being made at the time of delivery).

There are (at least) two issues with this implementation:
1. `pthread_cancel` could send the signal _before_ `pthread_setcanceltype(old_type)`, but the signal might arrive _after_ `pthread_setcanceltype(old_type)`.
2. A signal (unrelated to cancellation) could be delivered during the `syscall`, and the handler for that signal could perform a `longjmp`, thereby causing `pthread_setcanceltype(old_type)` to not be called.

The 1<sup>st</sup> point is addressed by the `check_for_pthread_cancel_race` call: yet another piece of per-thread state tracks whether a `pthread_cancel` call is in the middle of sending a signal, and if so, `check_for_pthread_cancel_race` waits for the signal delivery, thereby avoiding it from causing `EINTR` on an unrelated syscall.

The 2<sup>nd</sup> point is unaddressed. It is tracked as part of [glibc bug 12683](https://sourceware.org/bugzilla/show_bug.cgi?id=12683), where a solution has been proposed, but not yet implemented.

## Polyfilled semantics of cancellation points

For functions that don't meaningfully block in practice, such as `open_by_handle_at` and `getrandom`, the polyfill implementation of these functions inserts a `pthread_testcancel` call, as in:
```c
pthread_testcancel();
return syscall(open_by_handle_at, ...);
```

For functions that really can block, the polyfill implementation takes a two-pronged strategy:
1. If the ambient glibc provides the function being polyfilled, call that.
2. Otherwise, implement it similarly to how glibc currently does, albeit without the `check_for_pthread_cancel_race` call:

   ```c
   old_type = pthread_setcanceltype(ASYNCHRONOUS);
   result = syscall(epoll_pwait2, ...);
   pthread_setcanceltype(old_type);
   return result;
   ```

If glibc one day fixes [bug 12683](https://sourceware.org/bugzilla/show_bug.cgi?id=12683), then using the ambient glibc implementation will give bug-free behaviour (when running with a sufficiently new glibc). On older glibc versions, the polyfill implementation is only marginally worse than the glibc implementation: the lack of a `check_for_pthread_cancel_race` call is unfortunate, but applications should be prepared to handle `EINTR` anyway.

```

### File: docs\Command_line_options.md
```md
## polyfill-glibc command line options

The general syntax of `polyfill-glibc` is:
```
polyfill-glibc FLAG... FILENAME...
```
At least one flag and one filename must be specified. Most flags indicate some kind of action (either printing information from a file, or modifying a file). These actions are performed one at a time, from left to right. If multiple filenames are specified, then every action will be performed against every file.

The flagship action is `--target-glibc`.

Files are modified in-place, unless `--output` is used to specify a different output filename.

Actions that print information about a file: `--print-imports`, `--print-exports`, `--print-kernel-version`, `--print-interpreter`, `--print-flags`, `--print-rpath`, `--print-runpath`, `--print-soname`.

Actions that modify files: `--target-glibc`, `--remove-kernel-version`, `--rename-dynamic-symbols`, `--clear-symbol-version`, `--weak-verneed`, `--remove-verneed`,  `--set-rpath`, `--set-runpath`, `--set-soname`, `--add-early-needed`, `--add-late-needed`, `--add-hash`, `--add-gnu-hash`, `--add-debug`, `--add-flags`, `--add-rpath`, `--add-runpath`, `--set-interpreter`, `--remove-debug`, `--remove-flags`, `--remove-needed`, `--remove-relro`, `--remove-rpath`, `--remove-runpath`, `--remove-soname`.

Flags that change the effect of other actions: `--output`, `--dry`, `--page-size`, `--use-polyfill-so`, `--create-polyfill-so`, `--polyfill-cfi`.

## --target-glibc

Takes as an argument a glibc version, for example `--target-glibc=2.17`. The action identifies all dependencies that the file has on glibc functions and variables newer than the specified version, and employs [various strategies](How_does_polyfill_glibc_work.md) to remove those dependencies.

Note that `--target-glibc` is currently only implemented for x86_64 files and aarch64 files. If other architectures are of interest to you, open a GitHub issue so that we can gauge interest.

If there are any strong dependencies that `--target-glibc` cannot remove, then it'll fail and report the problematic dependencies, for example:

```
Cannot change target version of FILENAME to 2.3.4 (x86_64) due to missing knowledge about how to handle:
  faccessat@GLIBC_2.4
  fchmodat@GLIBC_2.4
  fdopendir@GLIBC_2.4
  __isoc23_sscanf@GLIBC_2.38
  openat64@GLIBC_2.4
  __realpath_chk@GLIBC_2.4
  splice@GLIBC_2.5
  __syslog_chk@GLIBC_2.4
```

If you are hitting this, then some options are:
  * Open a GitHub issue requesting that `--target-glibc` be taught how to handle the problematic symbols.
  * Specify a different value for `--target-glibc`. For example, given the above, `--target-glibc=2.38` would succeed, and `--target-glibc=2.5` would succeed if it weren't for `__isoc23_sscanf@GLIBC_2.38`.
  * Use `--rename-dynamic-symbols` or `--clear-symbol-version` prior to `--target-glibc` to manually resolve problematic dependencies. For example, given the above, if you know that the C23 version of `sscanf` isn't required, and that the C99 version of `sscanf` would suffice, then `--rename-dynamic-symbols` could be used to rename `__isoc23_sscanf@GLIBC_2.38` to `__isoc99_sscanf@GLIBC_2.7`.

One of the strategies employed by `--target-glibc` involves statically linking new pieces of executable code in to the file. If you'd prefer to keep said pieces of executable code in a separate shared object, see `--create-polyfill-so` and `--use-polyfill-so`. The `--polyfill-cfi` flag can also be used to control whether unwind information is provided for said statically linked code.

## --output and --dry

By default, polyfill-glibc modifies files in-place. If this is not desirable, then `--output` can be specified, which takes a filename as an argument, as in `polyfill-glibc --target-glibc=2.17 --output=output_filename input_filename`. If `--output` is specified multiple times, then the last occurrence takes effect. Note that it rarely makes sense to use `--output` with multiple input filenames, as `--output` cannot be specified per input.

The `--dry` flag is shorthand for `--output=/dev/null`: polyfill-glibc will try to perform the requested actions, and will fail if it cannot perform them, but won't write out a modified file in case of success.

## --rename-dynamic-symbols

Takes as an argument the name of a file, for example `--rename-dynamic-symbols=my_renames.txt`. Said file should be a UTF-8 text file, with a pair of symbol names per line: the symbol to rename, followed by the symbol to rename to. `//` comments are supported.

As a small example, `my_renames.txt` could contain: 
```
memcpy@GLIBC_2.14 memcpy
clock_settime@GLIBC_2.17 librt.so.1::clock_settime@GLIBC_2.2.5
__isoc23_sscanf@GLIBC_2.38 __isoc99_sscanf@GLIBC_2.7
```
As a much larger example, see [the file used by `--target-glibc`](../src/x86_64/renames.txt).

The symbol to rename should either be a plain identifier, or two identifiers with an `@` sign between them. If a plain identifier is used, then it'll only match against unversioned symbols (this is different to PatchELF's `--rename-dynamic-symbols`).

The symbol to rename to should similarly be a plain identifier, or two identifiers with an `@` sign between them. All of this can be optionally prefixed with `LIBRARY_NAME::`, the presence of which has three effects:
  1. If the rename is applied, ensures that the file has a dependency on `LIBRARY_NAME` (similar to `--add-late-needed LIBRARY_NAME`).
  2. If the rename is applied, and the symbol to rename to ends with `@VERSION`, then the dependency on `LIBRARY_NAME` will additionally require that `VERSION` is present in said library.
  3. The rename will not be applied to exported symbols (i.e. it'll only be applied to imported symbols), as it makes no sense to rename an export to a different library.

As a special case, the symbol to rename to can be specified as `polyfill::NAME`, where `NAME` must be one of public functions or variables that polyfill-glibc can statically link into other files. In this case, if the rename is applied, then said function or variable will be statically linked into the file, and the symbol will be repointed to this statically linked function or variable. As a special case on top of a special case, if `--use-polyfill-so=LIB` is specified, then occurrences of `polyfill::NAME` are changed to `LIB::NAME@POLYFILL`, and then no static linking occurs.

If all symbols with a particular `@VERSION` suffix are renamed away, then the dependency on `VERSION` is automatically removed too. The dependency on the original shared library will remain though; use `--remove-needed=LIB` _after_ `--rename-dynamic-symbols` to remove any such dependencies that are no longer required.

## --print-kernel-version and --remove-kernel-version

An ELF file can specify the minimum operating system kernel version it requires to run (this is the `.note.ABI-tag` section), however this functionality is of decreasing utility: the kernel itself ignores this requirement when launching programs, and the glibc dynamic loader has also started [ignoring it for shared libraries since glibc 2.36](https://github.com/microsoft/WSL/issues/3023#issuecomment-1179796349). In other words, `.note.ABI-tag` has no effect on modern systems, and exists merely as a footgun for older systems.

The `--print-kernel-version` flag will print the required kernel version, for example:
```
Linux 3.2.0
```
Or:
```
No minimum kernel version specified.
```

The `--remove-kernel-version` flag will remove any kernel version requirement from a file, thereby giving the modern glibc behaviour even on older systems. Note that removing the requirement is just skipping a check at shared object load time; if the shared object requires a recent kernel for some functionality, it'll likely fail when it tries to exercise said functionality. The flag is similar in effect to running `strip` with `--remove-section=.note.ABI-tag`.

## rpath and runpath (--print-rpath, --print-runpath, --set-rpath, --set-runpath, --add-rpath, --add-runpath, --remove-rpath, --remove-runpath)

An ELF file can specify where to find the shared objects it depends upon. There are two different mechanisms for this, which have the very similar names _rpath_ and _runpath_:
  1. _rpath_ is a list of directories, which are searched before any directories in `LD_LIBRARY_PATH`, and are searched for both direct and transitive dependencies.
  2. _runpath_ is a list of directories, which are searched after any directories in `LD_LIBRARY_PATH`, and are searched only for direct dependencies.

Notably, both _rpath_ and _runpath_ support the `$ORIGIN` placeholder, which will be expanded by the dynamic linker to the directory of the ELF file in which `$ORIGIN` is used. This allows an ELF file's dependencies to be packaged alongside or nearby in the file system. For example, _rpath_ of `$ORIGIN` will look in the same directory for dependencies, and an _rpath_ of `$ORIGIN/lib` will look in the `lib` subdirectory. If making use of this, either set an _rpath_ on the root file in the dependency tree, or set _runpath_ on all non-leaf files in the dependency tree.

If an ELF file contains both _rpath_ and _runpath_, then _runpath_ takes priority and _rpath_ is ignored.

See [the Linux loading process](The_Linux_loading_process.md) for a full description of where _rpath_ and _runpath_ fit in.

The `--print-runpath` flag will print the _runpath_, if any. Meanwhile, the `--print-rpath` flag will print the _rpath_, if any.

The `--remove-runpath` flag will remove the _runpath_, if any. Meanwhile, the `--remove-rpath` flag will remove the _rpath_, if any.

The `--set-runpath` flag takes a colon-separated list of directories as an argument, and sets _runpath_ to that list. Meanwhile, `--set-rpath` flag is simiar, but for _rpath_. If `--set-rpath` is specified, then it also has the effect of `--remove-runpath`.

The `--add-runpath` flag takes a colon-separated list of directories as an argument, and _appends_ that list to _runpath_. Meanwhile, `--add-rpath` flag is simiar, but for _rpath_. If `--add-rpath` is specified, then it also has the effect of `--remove-runpath`.

## soname (--print-soname, --set-soname, --remove-soname)

An ELF shared library can specify a _soname_, which has two effects:
  1. `ldconfig` will create a symlink from the _soname_ to the actual file name of the shared library.
  2. Once a shared library has been loaded via its actual file name, any subsequent attempt (within the same process) to load its _soname_ will immediately resolve to said shared library rather than searching the filesystem.

The `--print-soname` flag will print the _soname_, if any.

The `--set-soname` flag takes an argument, and sets the _soname_ to that.

The `--remove-soname` flag will remove the _soname_, if any.

## ELF load flags (--print-flags, --add-flags, --remove-flags)

An ELF file can specify various flags that tweak the behaviour of the dynamic linker:

| Flag | Behaviour |
|---|---|
| `execstack` | If set, then the main thread is given an executable stack (as are all subsequent threads created by glibc functions). This is generally considered to be a major security problem. |
| `df_bind_now` or `df_1_now` | If neither flag is set, then imported functions can be imported lazily: said functions will be looked up when they are first called. If either flag is set, then lazy importing is disabled: all imported functions are looked up when the ELF file is loaded. This can make loading slower, and also means that problems get detected early. Note that setting the `LD_BIND_NOW` environment variable also disables lazy importing. Lazy importing requires that the GOT exist in writable memory rather than read-only memory; if removing `df_bind_now` and `df_1_now`, then `--remove-relro` might also be required to keep the GOT in writable memory. |
| `df_1_pie` | If set, marks the ELF file as an executable rather than a shared library, and means that the ELF file cannot - by any means - be loaded as library. |
| `df_1_noopen` | If set, then the ELF file cannot be loaded by an explicit call to `dlopen` (but it can still be loaded by any other means; most notably by being listed as a dependency of some other ELF file, or by being named in `LD_PRELOAD`). |
| `df_1_nodeflib` | If set, then the system default search path (e.g. `/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:/lib:/usr/lib`) is _not_ searched when trying to locate dependencies of the ELF file. Accordingly, if it has any non-absolute dependencies, _rpath_ or _runpath_ or `LD_LIBRARY_PATH` needs to be used to specify the directory in which to find them. |
| `df_1_nodelete` | If set, implicit and explicit `dlclose` calls against this file have no effect: once loaded, the ELF file remains loaded until the process exits. Note that this has no effect on musl, as `dlclose` is already a no-op there. |
| `df_1_initfirst` | If any ELF shared library specifies this flag, then the _last_ such shared library to be loaded has its init functions called before those of other shared libraries. See [the Linux loading process](The_Linux_loading_process.md) for a full description. Note this flag was reserved for `libpthread.so.0` in glibc versions prior to 2.34. |
| `df_symbolic` | If set in an ELF file that both imports and exports symbols, then the import search order is tweaked slightly: the file's own exports will be used to satisfy its imports, and only if that fails will the default search order be employed. |
| `df_textrel` | If set, all virtual memory mapped in for the ELF file is made writable while relocations are being applied, thereby allowing relocations to modify "read-only" memory. |

Many other flags also exist, but they have no effect.

The `--print-flags` flag to polyfill-glibc will print all the set flags. 

The `--add-flags` flag to polyfill-glibc takes as an argument a list of flags (separated by spaces, commas, pipes, or colons), and sets all of them. For example, `--add-flags=df_bind_now,df_1_nodelete` sets the `df_bind_now` and `df_1_nodelete` flags.

The `--remove-flags` flag to polyfill-glibc takes as an argument a list of flags (separated by spaces, commas, pipes, or colons), and unsets all of them. For example, `--remove-flags=execstack,df_noopen` unsets the `execstack` and `df_noopen` flags.

## ELF hash tables (--add-hash and --add-gnu-hash)

If an ELF file exports symbols, said symbols need to be listed in _some_ hash table. That hash table can either be a traditional ELF hash table, or a GNU hash table. For maximum compatibility (though at the cost of increased file size), a file can have both styles of hash table.

The `--add-hash` flag causes a traditional ELF hash table to be added, if not already present. This hash table gives maximum compatibility, in particular giving compatibility with glibc dynamic loader versions prior to 2.5 (which was released in September 2006).

The `--add-gnu-hash` flag causes a GNU hash table to be added, if not already present. This hash table has better performance charact
... [TRUNCATED]
```

### File: docs\Comparison_with_PatchELF.md
```md
## Comparing polyfill-glibc with PatchELF

NixOS's [PatchELF](https://github.com/NixOS/patchelf) tool is similar to polyfill-glibc, in that both are designed for modifying ELF executables and shared libraries after they have been built.

The flagship feature of polyfill-glibc is the `--target-glibc` operation, which has no direct equivalent in PatchELF (though a limited subset of the functionality can be achieved via PatchELF's `--rename-dynamic-symbols` and `--clear-symbol-version`). A lot of lower level operations have equivalents between polyfill-glibc and PatchELF:

| polyfill-glibc operation | PatchELF operation |
| ----------- | -------- |
| `--add-debug` | `--add-debug-tag` |
| `--add-flags execstack` | `--set-execstack` |
| `--add-flags nodeflib` | `--no-default-lib` |
| `--add-hash` / `--add-gnu-hash` | N/A |
| `--add-early-needed` / `--add-late-needed` | `--add-needed` |
| `--add-rpath` / `--add-runpath` | `--add-rpath` |
| `--clear-symbol-version` | `--clear-symbol-version` |
| `--print-exports` | N/A |
| `--print-flags` then `grep execstack` | `--print-execstack` |
| `--print-imports` then `grep '^library '` | `--print-needed` |
| `--print-interpreter` | `--print-interpreter` |
| `--print-kernel-version` | N/A |
| `--print-os-abi` | `--print-os-abi` |
| `--print-runpath` / `--print-rpath` | `--print-rpath` |
| `--print-soname` | `--print-soname` |
| `--rename-dynamic-symbols` | `--rename-dynamic-symbols` |
| `--remove-debug` | N/A |
| `--remove-flags execstack` | `--clear-execstack` |
| `--remove-kernel-version` | N/A |
| `--remove-needed` | `--remove-needed` |
| `--remove-relro` | N/A |
| `--remove-runpath` / `--remove-rpath` | `--remove-rpath` |
| `--remove-soname` | N/A |
| `--remove-verneed` | N/A |
| N/A | `--replace-needed` |
| `--set-interpreter` | `--set-interpreter` |
| N/A | `--set-os-abi` |
| `--set-runpath` / `--set-rpath` | `--set-rpath` |
| `--set-soname` | `--set-soname` |
| N/A | `--shrink-rpath` |
| `--target-glibc` | N/A |
| `--weak-verneed` | N/A |

Behind the scenes, one notable difference between polyfill-glibc and PatchELF is that PatchELF requires the file being modified to have ELF section headers, whereas polyfill-glibc does not. In turn, this influences how the two tools work around [the kernel's `AT_PHDR` bug](Kernel_AT_PHDR_bug.md): PatchELF can leave the program headers in their original location and move sections as neccessary to make space for the enlarged program headers, whereas polyfill-glibc moves the program headers to a new location and inserts a zero-length `PT_LOAD` as a workaround.

```

### File: docs\How_does_polyfill_glibc_work.md
```md
## How does polyfill-glibc work?

polyfill-glibc interprets the metadata within an ELF file to determine its dependencies (you can run `polyfill-glibc --print-imports FILE` to see these). Dependencies on a particular version of glibc come in the form of functions or variables with a `@GLIBC_2.X` suffix. polyfill-glibc has various strategies for reworking these dependencies.

### Stripping the version suffix

The simplest strategy is to remove the `@GLIBC_2.X` suffix from the function or variable name. The most common example of this is the `memcpy@GLIBC_2.14` function, which polyfill-glibc reworks to instead be a dependency on plain `memcpy`. If there is a `@GLIBC_2.2.5` variant of the function, then the plain name will bind to that; otherwise the plain name will bind to the most recent version of the function.

This strategy can only be employed when the exact version of the function doesn't matter. In the case of `memcpy`, it is undefined behaviour if the source and destination regions overlap, and the `memcpy@GLIBC_2.14` version was introduced so that glibc could become more aggressive in exploiting that undefined behaviour. Well-written programs should not be invoking undefined behaviour in the first place, so the exact version of `memcpy` shouldn't matter.

### Changing the function name

Sometimes glibc will introduce a new name for a function, or otherwise introduce a function that is behaviourally identical to an existing function. One example of this is `stdc_first_trailing_one_ui@GLIBC_2.39`, which is behaviourally identical to `ffs@GLIBC_2.2.5`, so polyfill-glibc can replace a dependency on `stdc_first_trailing_one_ui@GLIBC_2.39` with one on `ffs@GLIBC_2.2.5`.

### Changing the library

Version 2.34 of glibc merged `libdl.so`, `libpthread.so`, `librt.so`, `libanl.so`, and `libutil.so` in to `libc.so`. For example, `dlsym@GLIBC_2.34` comes from `libc.so`, but polyfill-glibc can replace it with a dependency on `dlsym@GLIBC_2.2.5`, provided that polyfill-glibc ensures `libdl.so` is loaded.

### Statically linking a standalone implementation

polyfill-glibc contains its own implementations of various glibc functions, and can statically link these implementations into other files. For example, `thrd_yield@GLIBC_2.28` can be implemented in 12 bytes of x86-64 machine code; polyfill-glibc can add these 12 bytes of executable code to a file, and then replace a `thrd_yield@GLIBC_2.28` dependency with a direct local reference to the added bytes.

### Statically linking an implementation built atop older glibc functions

Per the previous strategy, polyfill-glibc contains its own implementations of various glibc functions, and can statically link these implementations into other files. Sometimes these implementations call into older glibc functions; for example the polyfill-glibc implementation of `thrd_sleep@GLIBC_2.28` calls `clock_nanosleep@GLIBC_2.17`. A particularly common pattern is for the polyfill-glibc implementation of a function to call `__errno_location@GLIBC_2.2.5` when it needs to set `errno`.

### Adding a traditional ELF hash table

If an ELF file exports symbols, said symbols need to be listed in _some_ hash table. That hash table can either be a traditional ELF hash table, or a GNU hash table. Support for GNU hash tables was added to glibc's dynamic linker in version 2.5, so if `--target-glibc=2.4` or older is requested, then polyfill-glibc will add a traditional ELF hash table with the same contents as the GNU hash table.

Note that this can also be explicitly requested via `--add-hash`.

### Expanding or interpreting DT_RELR

Version 2.36 of glibc's dynamic loader added support for `DT_RELR`, which is a compressed format for representing certain types of relocation. polyfill-glibc contains two strategies for dealing with this: it can decompress `DT_RELR` to a format understood by older versions of glibc's dynamic loader, or it can statically link a little piece of code that understands `DT_RELR` and hook up said code to run during relocation processing by means of a dummy `IRELATIVE` relocation.

### Removing PLT-rewriting support

Version 2.39 of glibc's dynamic loader added support for PLT rewriting. This required extra metadata on `R_X86_64_JUMP_SLOT` relocations, and the `r_addend` field was appropriated for this purpose. This field was previously ignored by versions 2.36 through 2.38, but _was_ used by versions prior to 2.36, so if `--target-glibc=2.35` or older is requested, then the `r_addend` field of `R_X86_64_JUMP_SLOT` relocations needs changing to contain zero. As this removes the metadata required for PLT rewriting, PLT rewriting gets disabled at the same time (by removing the `DT_X86_64_PLTENT` tag).

```

### File: docs\Kernel_AT_PHDR_bug.md
```md
## Linux Kernel AT_PHDR bug
As part of [the loading process](The_Linux_loading_process.md), the kernel supplies an `AT_PHDR` value to userspace, which is meant to contain the _virtual address_ of the main executable's program headers. The `e_phoff` field of the ELF header contains the _file offset_ of the main executable's program headers, which the kernel needs to translate into a virtual address.

As a reminder, there are three relevant address spaces in ELF files:
1. File offsets (e.g. `e_phoff` in ELF header, `p_offset` in program headers).
2. Ideal virtual adresses (e.g. `e_entry` in ELF header, `p_vaddr` in program headers).
3. Actual virtual addresses.

The mapping between (1) and (2) is potentially non-linear; the `PT_LOAD` program headers can set up an arbitrarily complex mapping if so desired. In contrast, the mapping between (2) and (3) is very simple, and consists of a single offset value (randomly) chosen by the kernel at load-time.

To translate `e_phoff` from (1) to (2), the correct approach is to find the particular `PT_LOAD` header whose `p_offset` / `p_filesz` range covers `e_phoff`, and then compute `e_phoff + p_vaddr - p_offset` using _that_ `PT_LOAD` header. Unfortunately, before kernel commit [0da1d50027](https://github.com/torvalds/linux/commit/0da1d5002745cdc721bc018b582a8a9704d56c42) in March 2022 (released in 5.17.2, backported to 5.16.19 / 5.15.33 / 5.10.110), the kernel took the _first_ `PT_LOAD` header and used that for doing `e_phoff + p_vaddr - p_offset`. This bug is benign if the first `PT_LOAD` header has a `p_offset` / `p_filesz` range which covers `e_phoff`, and this happens to be the case for most ELF files produced by most compilers. This bug is also benign if `p_vaddr - p_offset` as computed for the first `PT_LOAD` equals `p_vaddr - p_offset` as for the `PT_LOAD` whose file range covers `e_phoff`.

In cases where the bug _isn't_ benign, its consequences are bad: an incorrect `AT_PHDR` value will cause the dynamic linker to either segfault or fail to properly perform dynamic linking of the target executable (which in turn will likely cause a segfault fairly quickly).

In cases where polyfill-glibc needs to change `e_phoff`, this bug presents a problem. It can't re-order `PT_LOAD` commands to put the `PT_LOAD` covering `e_phoff` at the start of the list, as `PT_LOAD` commands need to be in ascending `p_vaddr` order (per the ELF specification, "Loadable segment entries in the program header table appear in ascending order, sorted on the p_vaddr member", and most loaders rely on this). If the first `PT_LOAD` command specified a non-zero `p_vaddr`, then polyfill-glibc _could_ carve out some new virtual address space before the first `PT_LOAD` command. Unfortunately, it is common for dynamic libraries and position-independent executables to have `p_vaddr` of their first `PT_LOAD` be equal to zero, which leaves no space before it. Instead, polyfill-glibc will insert a new `PT_LOAD` at the start of the list, with `p_vaddr` equal to whatever was previously first (to maintain the sorted order), `p_filesz` equal to zero (so that `p_offset` is not used for anything ‡), and `p_offset` set such that `p_vaddr - p_offset` of this new `PT_LOAD` equals `p_vaddr - p_offset` of the `PT_LOAD` covering the program headers.

(‡) Except that glibc's dynamic loader always passes `p_offset` of the first `PT_LOAD` as the offset value to `mmap` when establishing the base address of dynamic libraries and position-independent executables, even if `p_filesz` of that `PT_LOAD` is zero. Accordingly, polyfill-glibc needs to keep the `p_offset` value within the range of allowable values for an `mmap` offset.

## Similar ldconfig bug

A [similar bug](https://sourceware.org/bugzilla/show_bug.cgi?id=25087) exists in `ldconfig` in glibc versions prior to 2.31 (released February 2020), albeit translating `d_un.d_val` of `DT_STRTAB` from address space (2) to address space (1), rather than translating `e_phoff` from address space (1) to address space (2), but the summary is the same: it uses `p_vaddr - p_offset` of the first `PT_LOAD` rather than using `p_vaddr - p_offset` of the `PT_LOAD` covering `DT_STRTAB`. To work around this, if polyfill-glibc needs to move _either_ the program headers or the dynamic string table, then it'll move _both_, ensuring that the same new `PT_LOAD` command covers both, and then the workaround for the kernel also fixes things for `ldconfig`.

```

### File: docs\Limitations.md
```md
## Limitations of polyfill-glibc

Currently, the `--target-glibc` operation of polyfill-glibc is only implemented for x86_64 and aarch64. If other architectures are of interest to you, open a GitHub issue so that we can gauge interest. Note that lower level operations, for example `--set-rpath`, are implemented for all architectures.

Polyfills have not yet been written for every glibc function. If you're hitting such a case, open a GitHub issue so that we can gauge interest.

Some glibc functions are system call wrappers. Even if the function itself is polyfilled, the underlying system call might not be present on older kernels. In such cases the wrapper function will return `-1` and set `errno` to `ENOSYS`. User code needs to detect and handle this scenario.

Only glibc functions are polyfilled by polyfill-glibc; functions from other libraries are not. In particular, libstdc++ uses symbol versions starting with `GLIBCXX_3.`, but these are libstdc++ functions rather than glibc functions.

Sometimes even a small amount of polyfilling can result in a noticable increase in binary size. This is because resizing the string table (or the symbol table, or the relocation table, or the export hash table) of an existing binary from N entries to N+1 entries requires copying the entire table to a new location and allocating N+1 entries at that new location, rather than just adding 1 entry at the old location.

As a concession to ease to implementation, polyfill-glibc needs to be able to map the entire file being edited into memory. This is rarely a problem on 64-bit systems, but can prevent editing files larger than 1-2GB on 32-bit systems.

## Limitations of particular polyfilled functions

|Function|Limitations|
|--------|-----------|
|`accept4`|See [asynchronous cancellation](Asynchronous_cancellation.md).|
|`arc4random`, `arc4random_buf`, `arc4random_uniform`|Some glibc versions of these functions contain buggy handling of `EINTR` and/or `ENOSYS` results from the `getrandom` system call (see for example [BZ#29624](https://sourceware.org/bugzilla/show_bug.cgi?id=29624) and [BZ#31612](https://sourceware.org/bugzilla/show_bug.cgi?id=31612)). The polyfill implementation does not have these bugs.|
|`copy_file_range`|See [asynchronous cancellation](Asynchronous_cancellation.md).|
|`__cxa_thread_atexit_impl`|If this function is polyfilled, then the `df_1_nodelete` flag will be applied to the file, thereby causing the file to remain in memory once loaded, even if `dlclose` is called against it. If you are confident that any destructor logic for `thread_local` variables residing in the file will not need to be called after `dlclose`, then you can specify `--remove-flags df_1_nodelete` after `--target-glibc`.|
|`epoll_pwait2`|See [asynchronous cancellation](Asynchronous_cancellation.md).|
|`fcntl64`|See [asynchronous cancellation](Asynchronous_cancellation.md).|
|`getrandom`|See [asynchronous cancellation](Asynchronous_cancellation.md).|
|`__isoc23_fscanf`, `__isoc23_fwscanf`, `__isoc23_scanf`, `__isoc23_sscanf`, `__isoc23_swscanf`, `__isoc23_vfscanf`, `__isoc23_vfwscanf`, `__isoc23_vscanf`, `__isoc23_vsscanf`, `__isoc23_vswscanf`, `__isoc23_vwscanf`, `__isoc23_wscanf`|These functions are polyfilled to their C99 equivalent. The sole consequence of this is that the `%i` format will no longer recognise binary numbers starting with `0b` or `0B`.|
|`open_by_handle_at`|See [asynchronous cancellation](Asynchronous_cancellation.md).|
|`pidfd_spawn`, `pidfd_spawnp`|Some glibc versions of these functions contain a bug that leaks an fd in some failure scenarios (see [BZ#31695](https://sourceware.org/bugzilla/show_bug.cgi?id=31695)). The polyfill implementation does not have this bug.|
|`posix_spawn_file_actions_addchdir_np`|If the polyfill implementation is used, then `posix_spawn_file_actions_destroy` will also be replaced with a polyfill implementation, even if the `--target-glibc` version would not otherwise require this.|
|`posix_spawn_file_actions_addchdir_np`, `posix_spawn_file_actions_addclosefrom_np`, `posix_spawn_file_actions_addfchdir_np`, `posix_spawn_file_actions_addtcsetpgrp_np`, `posix_spawnattr_setcgroup_np`|If the polyfill implementation is used, then `posix_spawn` and `posix_spawnp` will also be replaced with a polyfill implementation, even if the `--target-glibc` version would not otherwise require this.|
|`preadv2`, `preadv64v2`|See [asynchronous cancellation](Asynchronous_cancellation.md).|
|`pwritev2`, `pwritev64v2`|See [asynchronous cancellation](Asynchronous_cancellation.md).|
|`quick_exit`|If the ambient glibc is version 2.18 through 2.23 (inclusive), then destructors for `thread_local` variables (of the calling thread) will be called by `quick_exit`. They will not be called in other cases.|
|`qsort_r`|The polyfill implementation is _some_ in-place non-stable comparison-based sort with O(n log n) worst-case behaviour. The exact sequence of element-wise compares and swaps may differ to that of any particular glibc version. If the comparison function does not define a strict total order on the elements being sorted, then the result may differ to that of any particular glibc version (notably, this includes the case where the array being sorted contains elements that compare equal but are not bitwise identical).|
|`sem_clockwait`|If the ambient glibc lacks `sem_clockwait`, then the polyfill silently remaps `sem_clockwait` to `sem_timedwait`, thereby always waiting against `CLOCK_REALTIME`.|
|`stdc_bit_ceil_uc`, `stdc_bit_ceil_us`|The standard leaves the return value undefined if it does not fit in the return type. The polyfill implementation follows the glibc approach of returning the correct result as an int (which will become zero if truncated to the return type).|
|`stdc_bit_ceil_ui`, `stdc_bit_ceil_ul`, `stdc_bit_ceil_ull`|The standard leaves the return value undefined if it does not fit in the return type. The polyfill implementation follows the glibc approach of returning zero.|

```

### File: docs\Relative_interpreter.md
```md
## Relative interpreter

A dynamically linked ELF executable normally has to specify the absolute path of the dynamic loader that it expects to use. This path will typically be something like `/lib64/ld-linux-x86-64.so.2`, though it can be set to something else at link time via `-Wl,--dynamic-linker=`, or after the fact via `polyfill-glibc --set-interpreter=`.

It is not normally possible to use the `$ORIGIN` placeholder as part of the path to the dynamic linker, however an experimental tool in the polyfill-glibc repository makes this possible. The tool can be built using the command:

```
$ ninja build/x86_64/set_relative_interp
```

> [!NOTE]
> The tool is currently only available for x86_64. If other architectures are of interest to you, open a GitHub issue so that we can gauge demand.

Once built, the tool takes two command line arguments: the path of an executable to modify, and an interpreter path starting with `$ORIGIN`, for example:

```
$ build/x86_64/set_relative_interp a.out '$ORIGIN/libs/ld-linux-x86-64.so.2'
```

> [!WARNING]
> Be careful to avoid having your shell expand `$ORIGIN`.

The modified executable will look for a dynamic loader in two places:
1. The `LD_SO_PATH` environment variable, if set.
2. The path specified as the 2<sup>nd</sup> argument to `set_relative_interp`.

If the modified executable does not have an rpath or runpath attribute, then it'll gain an rpath equal to the directory containing the dynamic loader.

```

### File: docs\The_Linux_loading_process.md
```md
## Stage 1: execve in the kernel

When `execve` is called, control flow eventually reaches the [`load_elf_binary` function in `binfmt_elf.c`](https://github.com/torvalds/linux/blob/8d025e2092e29bfd13e56c78e22af25fac83c8ec/fs/binfmt_elf.c#L819), which does the following:
1. Read the ELF header of the target executable into temporary memory, and check that it looks sane.
2. Read the program headers of the target executable into temporary memory.
3. Allocate a range of virtual memory for the initial thread's stack, honouring `p_flags & PF_X` of the `PT_GNU_STACK` program header (if present).
4. Allocate a range of virtual memory for the target executable's code and data, and call `mmap` once for each `PT_LOAD` program header to populate that virtual memory.
5. If there is a `PT_INTERP` header:
    1. Open the file named by `PT_INTERP` (which must be an absolute path, or relative to the current working directory, with no support for placeholders). This is often something like `/lib64/ld-linux-x86-64.so.2`, i.e. [glibc's dynamic loader](What_is_glibc.md).
    2. Read its ELF header into temporary memory, and check that it looks sane.
    3. Read its program headers into temporary memory.
    4. Allocate a range of virtual memory for its code and data, and call `mmap` once for each `PT_LOAD` program header to populate that virtual memory.
6. Allocate a range of virtual memory for the vDSO's code and data, and populate it.
7. Construct the auxiliary information vector, keep a copy of it in `/proc/self/auxv`, and also push it on to the stack. Amongst other things, this contains:
   
   | Key | Contents |
   | --- | -------- |
   | `AT_PHDR` | The virtual address of the target executable's program headers (as mapped in during step 4, not the temporary copy from step 2). This is [potentially buggy in older kernels](Kernel_AT_PHDR_bug.md). |
   | `AT_PHENT` | `e_phentsize` from the target executable's ELF header. |
   | `AT_PHNUM` | `e_phnum` from the target executable's ELF header. |
   | `AT_ENTRY` | `e_entry` from the target executable's ELF header, adjusted by the load offset from step 4. |
   | `AT_BASE` | The load offset of the interpreter from step 5iv (0 if there was no `PT_INTERP` in step 5). |
   | `AT_SYSINFO_EHDR` | The virtual address of the ELF header of the vDSO (from step 6). |
   | `AT_RANDOM` | The virtual address of 16 bytes of random data (for seeding libc's PRNG). |
   | `AT_EXECFN` | The virtual address of the filename passed to `execve` (usually similar to `argv[0]`). |
   | `AT_SECURE` | A boolean indicating whether the target executable was setuid / setgid / setcap. |

8. Push `argc`, `argv[]`, and `envp[]` on to the stack.
9. Free the temporary memory from steps 2, 3, 5ii, and 5iii.
10. Transfer control to userspace. If there was a `PT_INTERP` in step 5, control will go to `e_entry` from the interpreter's ELF header, adjusted by the load offset from step 5iv. Otherwise, control will go to `e_entry` from the target executable's ELF header, adjusted by the load offset from step 4.

At this point, the kernel considers its work to be done. Note that it completely ignores `PT_PHDR`, `PT_DYNAMIC`, `PT_GNU_RELRO`, `PT_GNU_EH_FRAME`, `PT_TLS`, along with any other program headers. ELF section headers (if present) are also ignored. If there was no `PT_INTERP` in step 5, then the target executable's `e_entry` takes over from here.

## Stage 2: libc's dynamic loader

If there was a `PT_INTERP` in step 5, then the interpreter's `e_entry` takes over from here. If the interpreter is glibc's dynamic linker, then some of what it does is:
1. Load any shared libraries named in the `LD_PRELOAD` environment variable (` ` or `:` separated list of names. If `AT_SECURE`, any names with `/` in are ignored).
2. Load any shared libraries named in the `/etc/ld.so.preload` file.
3. Load any shared libraries named in the target executable's `DT_NEEDED` / `DT_AUXILIARY` / `DT_FILTER` entries. Note that `AT_PHDR` is crucial in allowing the dynamic loader to find these entries in the target executable.
4. For every shared library loaded so far, also load any shared libraries named in its `DT_NEEDED` / `DT_AUXILIARY` / `DT_FILTER` entries. Skip any entries referring to libraries already loaded. Repeat until there is nothing more to load.
5. For every shared library loaded so far, plus the target executable, if it has `DT_VERNEED`, then for every entry in `DT_VERNEED`, check that the shared library named therein has been loaded and has a matching entry in its `DT_VERDEF`. This is where errors like ``version `GLIBC_2.28' not found`` come from.
6. For every shared library loaded so far, if it has non-empty `PT_TLS`, assign it a TLS module index, and assign it some space in the static TLS region.
7. For every shared library loaded so far, in reverse dependency order, apply the relocations from its `DT_RELR` / `DT_REL` / `DT_RELA` / `DT_JMPREL` entries. This can involve doing symbol lookups against the list of loaded libraries.
8. Apply the relocations from the target executable's `DT_RELR` / `DT_REL` / `DT_RELA` / `DT_JMPREL` entries. Note that `AT_PHDR` is crucial in allowing the dynamic loader to find these entries in the target executable.
9. Initialise the values of all per-thread variables for the main thread based on the contents of `PT_TLS` regions, and take a copy of this to be used for initialising any subsequently launched threads.
10. If `libc.so.6` has been loaded, call the `__libc_early_init@GLIBC_PRIVATE` function therein.
11. If any shared library specified `DF_1_INITFIRST`, then the _last_ such shared library to be loaded has its `DT_INIT` / `DT_INIT_ARRAY` functions called. Note this flag was reserved for `libpthread.so.0` in glibc versions prior to 2.34.
12. Call functions listed in the target executable's `DT_PREINIT_ARRAY`.
13. For every shared library loaded so far, in reverse dependency order, call its `DT_INIT` / `DT_INIT_ARRAY` functions.
14. Transfer control to the target executable's `e_entry` (adjusted by its load offset).

### Searching for shared libraries

When loading shared libraries in steps 1-4 above, library names need to be converted into file paths. If the library name starts with or otherwise contains the `/` character, then any `$ORIGIN` / `$PLATFORM` / `$LIB` placeholders are expanded, and the result is treated either as an absolute path (if it starts with `/`) or as relative to the current working directory (if it contains `/` anywhere else). Otherwise, if the library name does not contain the `/` character, then a search procedure is initiated:
1. If any shared library loaded so far has `DT_SONAME` equal to the name being looked up, the name resolves to said library.
2. If the immediately referencing shared library or executable does _not_ have `DT_RUNPATH`:
    1. Search the `DT_RPATH` of the immediately referencing shared library or executable (`:` separated list of paths, `$ORIGIN` / `$PLATFORM` / `$LIB` placeholders supported).
    2. Search the `DT_RPATH` of _that_ shared library's immediately referencing shared library or executable. Repeat until the executable is reached (search that too).
3. Search the `LD_LIBRARY_PATH` environment variable (`:` or `;` separated list of paths, `$ORIGIN` / `$PLATFORM` / `$LIB` placeholders supported). This is skipped if `AT_SECURE`.
4. If the immediately referencing shared library or executable has `DT_RUNPATH`, search that `DT_RUNPATH` (`:` separated list of paths, `$ORIGIN` / `$PLATFORM` / `$LIB` placeholders supported).
5. Do a lookup against `/etc/ld.so.cache` (a file maintained by the `ldconfig` program).
6. If the immediately referencing shared library or executable has `DF_1_NODEFLIB`, fail rather than proceeding.
7. Search the system default path. On an x86_64 system, this might for example be `/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:/lib:/usr/lib`.

### Placeholders

Three placeholders are supported in shared library names and in shared library search paths: `$ORIGIN`, `$PLATFORM`, and `$LIB`. The most interesting of these is `$ORIGIN`, which expands to the absolute path of the directory of the file in which `$ORIGIN` appears. For example, if `$ORIGIN` appears in `/home/corsix/mylib.so`, then `$ORIGIN` expands to `/home/corsix`. If `mylib.so` was subsequently moved to `/home/corsix/libs/mylib.so`, then `$ORIGIN` would expand to `/home/corsix/libs`.

The `$PLATFORM` placeholder is _meant_ to expand to a string naming the current processor architecture, for example `x86_64` on x86-64 systems. However, at some point glibc decided to change this, meaning that `$PLATFORM` now expands to `haswell` on recent x86-64 systems.

The `$LIB` placeholder expands to a string generally similar to part of the system default search path for shared libraries. On an x86_64 system, `$LIB` might for example expand to `lib/x86_64-linux-gnu`.

Note that placeholders are _not_ supported in ELF interpreter paths.

To see what `$PLATFORM` and `$LIB` expand to on your system, one option is something like:
```
$ LD_PRELOAD='/$LIB/xyz/$PLATFORM/xyz' strace true 2>&1 | grep xyz.*RDONLY
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/xyz/haswell/xyz", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
```

## Stage 3: entry point of target executable

The target executable's `e_entry` takes over at this point. In practice, for dynamically linked executables, the entry point aligns the stack and then jumps to glibc's `__libc_start_main` function, which does a few things:

1. Call functions listed in the target executable's `DT_INIT` / `DT_INIT_ARRAY`.
2. Call the target executable's `main` function (i.e. the `int main(int argc, const char** argv)` that C programmers are familiar with).
3. Call `exit`, passing along the return value from `main`.

The dynamic loader's job isn't over when `main` is called though, as the program could call back into it via functions such as `dlopen` or `dlsym`.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
