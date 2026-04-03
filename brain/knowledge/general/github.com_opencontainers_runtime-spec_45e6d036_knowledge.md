---
id: github.com-opencontainers-runtime-spec-45e6d036-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:09.380280
---

# KNOWLEDGE EXTRACT: github.com_opencontainers_runtime-spec_45e6d036
> **Extracted on:** 2026-04-01 16:50:41
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525364/github.com_opencontainers_runtime-spec_45e6d036

---

## File: `.codespellrc`
```
[codespell]
# Those should always be in lowercase!
ignore-words-list = clos
```

## File: `.gitattributes`
```
# https://tools.ietf.org/html/rfc5545#section-3.1
*.ics text eol=crlf
```

## File: `.gitignore`
```
output
schema/validate
version.md
```

## File: `.mailmap`
```
Aleksa Sarai <cyphar@cyphar.com> <asarai@suse.de>
Alexander Morozov <lk4d4math@gmail.com> <lk4d4@docker.com>
Amit Saha <amitsaha.in@gmail.com> <amitsaha@users.noreply.github.com>
Antonio Murdaca <runcom@linux.com> <runcom@redhat.com>
Brandon Philips <brandon@ifup.org> <brandon.philips@coreos.com>
Brandon Philips <brandon@ifup.org> <brandon@ifup.co>
ChengTiesheng <chengtiesheng@huawei.com>
Daniel, Dao Quang Minh <dqminh89@gmail.com>
Doug Davis <dug@us.ibm.com> <duglin@users.noreply.github.com>
James O. D. Hunt <james.o.hunt@intel.com>
John Howard <jhoward@microsoft.com> <John.Howard@microsoft.com>
LinZhinan(Zen Lin) <linzhinan@huawei.com>
Mrunal Patel <mrunalp@gmail.com> <mrunal@Mrunals-iMac.local>
Mrunal Patel <mrunalp@gmail.com> <mrunal@dhcp-16-185.sjc.redhat.com>
Mrunal Patel <mrunalp@gmail.com> <mrunal@me.com>
Vincent Batts <vbatts@hashbangbash.com> <vbatts@hashbangbash.com>
Vincent Batts <vbatts@hashbangbash.com> <vbatts@redhat.com>
Vishnu Kannan <vishnuk@google.com>
Vishnu Kannan <vishnuk@google.com> <vishh@users.noreply.github.com>
Zefan Li <lizefan@huawei.com> <lizf1984@hotmail.com>
梁辰晔 (Liang Chenye) <liangchenye@huawei.com>
```

## File: `CODEOWNERS`
```
* @AkihiroSuda @crosbymichael @cyphar @dqminh @giuseppe @hqhq @kolyshkin @mrunalp @thaJeztah @tianon @utam0k
```

## File: `ChangeLog`
```
OpenContainers Specifications

Changes with v1.3.0:

	Additions:

	* config-vm: add hwConfig object (#1209)
	* config-linux: add intelRdt.schemata field (#1230)
	* config-linux: add netDevices object (#1271)
	* config-linux: add memoryPolicy object (#1282)
	* config-freebsd: add the spec for FreeBSD (#1286)
	* config-linux: add intelRdt.enableMonitoring field (#1287)

	Minor fixes:

	* config-linux: clarify intelRdt configuration (#1196)
	* runtime: fail when a poststart hook fails (#1262)
	* config-linux: clarify pids cgroup settings (#1279)
	* config-linux: define default clos for intelRdt (#1289)
	* features-linux: add intelRdt.enableMonitoring field (#1290)
	* features-linux: add intelRdt.schemata field (#1291)
	* config-linux: fix and elaborate memoryPolicy.nodes field (#1294)
	* config-linux, schema: fix FileMode description (#1298)

	Documentation, CI & Governance:

	* add systemd-nspawn to implementations.md (#1272)
	* CI: add codespell, bump golangci-lint (#1281)
	* docs: add missing backticks for code formatting  (#1284)
	* docs: fix typo (#1285)
	* principles: fix typo (#1288)
	* schema: fix json (#1297)
	* ci: use supported Go versions (#1300)
	* Add minimum supported Go version to CI (#1303)
	* Mention FreeBSD platform (#1304)

Changes with v1.2.1:

	Additions:

	* zos updates (#1273)
	* Add support for windows CPU affinity (#1258)
	* specs-go: sync SCMP_ARCH_* constants with libseccomp main (#1229)
	* Add CPU affinity to executed processes (#1253, #1261)
	* config-linux: describe the format of cpus and mems (#1253)

	Minor fixes:

	* Fix description of errnoRet in Seccomp (#1277)
	* config-linux: update for libseccomp v2.6.0 (#1276)
	* Correct `prestart` hook description in summary (#1275)

	Documentation, CI & Governance:

	* ci: Add a github actions workflow for lint (#1257)
	* update http links to https (#1269)
	* doc: fix the invalid hyperlink naming-a-volume (#1268)
	* ci: remove redundunt actions (#1256)
	* chore: format JSON file `make -C schema fmt` (#1255)
	* CODEOWNERS: remove vbatts (#1248)
	* MAINTAINERS: move vbatts to EMERITUS (#1248)
	* Update golangci-lint to v1.56.1 in CI (#1245)
	* Add Go v1.21 and v1.22 to GitHub Actions CI matrix (#1245)
	* Update GitHub Actions packages to resolve warnings in CI (#1244)

Changes with v1.2.0:

	Additions:

	* config: add idmap and ridmap mount options (#1222)
	* config.md: allow empty mappings for [r]idmap (#1224)
	* features-linux: Expose idmap information (#1219)
	* mount: Allow relative mount destinations on Linux (#1225)
	* features: add potentiallyUnsafeConfigAnnotations (#1205)
	* config: add support for org.opencontainers.image annotations #1197

	Minor fixes:

	* config: improve bind mount and propagation doc (#1228)

	Documentation, CI & Governance:

	* fix link to hooks in features (#1226)
	* specs-go: add missing deprecation comment for Hooks.Prestart (#1232)
	* specs-go: mark LinuxMemory.Kernel as deprecated ()#1233)

Changes with v1.1.0:

	Breaking changes (but rather conforms to the existing runc implementation):

	* config: change prestart hook spec to match reality (#1169)

	Deprecations:

	* config-linux: mark memory.kernel[TCP] as NOT RECOMMENDED (#1093)

	Additions:

	* cgroup: add cgroup v2 support (#1040)
	* seccomp: allow to override errno return code (#1041)
	* seccomp: Add support for SCMP_ACT_KILL_PROCESS (#1044)
	* Update seccomp architectures to support RISCV64 (#1059)
	* Add support for SCMP_ACT_KILL_THREAD (#1064)
	* Add Seccomp Notify support using UNIX sockets and container metadata (#1074)
	* config-linux: Add Intel RDT CMT and MBM Linux support (#1076)
	* seccomp: allow to override default errno return code (#1087)
	* Introduce zos as platform (#1095)
	* config-linux: add idle option for container cgroup (#1136)
	* config-linux: add CFS bandwidth burst (#1120)
	* IDMapping field for mount point (#1143)
	* schema: add cpu idle (#1145)
	* add domainname spec entity (#1156)
	* config-linux: add memory.checkBeforeUpdate (#1158)
	* seccomp: Add flag SECCOMP_FILTER_FLAG_WAIT_KILLABLE_RECV (#1161)
	* config-linux: add support for rsvd hugetlb cgroup (#1116)
	* features: add `features.md` to formalize the `runc features` JSON (#1130)
	* config-linux: add support for time namespace (#1151)
	* config: add scheduler entity (#1188)
	* config: Add I/O Priority Configuration for process group in Linux Containers (#1191)

	Minor fixes:

	* seccomp: fix go-specs for errnoRet (#1042)
	* Define State for container and runtime namespace (#1045)
	* Add State status constants to spec-go (#1046)
	* config.go: make umask a pointer (#1058)
	* Update State structure to use the new ContainerState type (#1056)
	* Fix int64 and uint64 type value ranges (#1060)
	* Fix seccomp notify inconsistencies (#1096)
	* runtime should WARN / ignore capabilities that cannot be granted (#1094)
	* config-linux: clarify the handling of ClosID RDT parameter (#1104)
	* defs-zos: [Fix] prevent schema parsers from hitting recursion-loop while resolving types. (#1117)
	* fix the lifecycle reference in the states listing (#1118)
	* specify cgroup ownership semantics (#1123)
	* config-linux: MAY reject an unfit cgroup (#1125)
	* cgroup ownership: clarify that some files may not exist (#1137)
	* schema: update README.md (#1083)
	* schema: make with golang 1.16 (#1084)
	* Update Windows CPU comments (#1144)
	* specs-go: export LinuxBlockIODevice (#1103)
	* config-linux: update type of LinuxCPU.Idle to *int64 (#1146)
	* Add available LinuxSeccompFlags (#1138)
	* config-linux: clarify where device nodes can be created (#1148)
	* runtime: remove `When serialized in JSON, the format MUST adhere to the following pattern` (#1178)
	* config: clarify Linux mount options (#1181)
	* schema: fix schema for timeOffsets (#1193)
	* schema: remove duplicate keys (#1195)
	* config-linux: clarify I/O throttling differences between cgroup v1 and v2 (#1194)
	* releases: use +dev as in-development suffix (#1198)
	* features: update Example (#1204)
	* schema: fix definition for ioPriority (#1206)
	* features: add a note to avoid confusion about annotations (#1212)

	Documentation, CI & Governance:

	* MAINTAINERS: Add @cyphar as maintainer (#1043)
	* Add Giuseppe Scrivano as a runtime spec maintainer (#1048)
	* Remove superfluous 'an' (#1049)
	* docs: Added enclave OCI runtime rune to implementations (#1055)
	* Change all references from whitelist to allowlist (#1054)
	* MAINTAINERS: update vbatts email (#1065)
	* travis: fix go_import_path (#1072)
	* Makefile: Fix golint URL used in go get (#1075)
	* config-linux: fix personality link (#1086)
	* README: Fix broken link for charter (#1091)
	* add youki to implementations.md (#1126)
	* Switch to GitHub Actions, CODEOWNERS, etc. (#1128)
	* typo: seccompFD -> seccompFd (#1133)
	* fix RFC link (#1153)
	* maintainer updates as per #1101 (#1150)
	* GOVERNANCE: correct the Charter URL (#1157)
	* CODEOWNERS: sync with MAINTAINERS (#1160)
	* Update CI to Go 1.20 (#1179)
	* config-linux: fix url error (#1184)
	* config-linux: chore: Update `ociVersion` in example (#1199)
	* MAINTAINERS: add Toru Komatsu (utam0k) (#1201)
	* glossary: `s/features document/Features structure/g` (#1203)
	* CODEOWNER: Add Toru Komatsu(@utam0k) to sync with MAINTAINERS (#1207)
	* README.md: update chat information (#1210)
	* Remove outdated meeting.ics (#1211)

Changes with v1.0.2:

	Additions:

	* Add create-container, create-runtime and start-container hooks (#1008)
	* config-linux: add Intel RDT CLOS name sharing support (#988)
	* config-linux: Add Intel RDT/MBA Linux support (#932)
	* config-linux: Add Memory cgroup's use_hierarchy (#985)
	* Add Linux personality support (#1012)
	* config: Add Windows Devices to Schema (#976)
	* Add support for SCMP_ACT_LOG (#1019)
	* config-linux: support seccomp flags (#1018)

	Minor fixes and documentation:

	* Makefile: avoid SELinux for making docs
	* Clarify case with pre-configured Intel RDT closID (#1034)
	* config-linux: describe more about rootfs mount propagation (#1035)
	* config-linux: add SHOULD to linux.namespaces.type (#1025)
	* Reduce DCO checks per PR from 3 to 1 (#1029)
	* Fix typo in RELEASES.md (#1033)
	* Remove some unneeded indent (#1031)
	* Add documentation how to do releases (#1027)
	* Removed Vishnu Kannan & Brandon Philips from maintainers (#1030 & #1028)
	* schema: drop id from umask (#1024)
	* implementations.md: fix repository for crun (#1017)
	* Update meeting info section to point to "org" repo (#1016)
	* Fix markdown escape in config-linux (#1013)
	* config-linux: add more info about hugetlb page size (#1011)
	* Fix ociVersion of Configuration Schema Example to support ambient capability (#1009)
	* Fix Namespaces to use LinuxNamespaceType (#1007)
	* change new pid namespace description (#1006)
	* updating link to code of conduct in org repository (#1001)
	* Update Windows LayerFolder docs (#999)
	* Windows:Have native CommandLine in Process (#998)
	* vm: fix parameters field (#994)
	* config-linux: documentation change for Intel RDT/MBA Software Controller support (#992)
	* Bump Go versions (#993)
	* Support for network namespace in windows (#989)
	* config: clarify source mount (#981)
	* Fix camelCasing on idType to align with other Windows spec conventions (#976)
	* meeting: Bump July meeting from the 4th to the 11th (#977)
	* docs: Added kata-runtime to implementations (#969)
	* Add gVisor to the implementations list (#970)
	* .travis.yml: Get schema dependencies in before_install (#968)
	* config: Clarify execution environment for hooks (#953)
	* config-linux: Drop console(4) reference (#965)
	* Linux devices: uid/gid relative to container (#959)
	* config: Add VM-based container configuration section (#949)
	* uidMappings: change order of fields for clarity (#956)
	* specs-go/config: Define RDMA cgroup (#942)
	* schema/Makefile: fix test (#947)
	* config: Fix Linux mount options links (#952)
	* glossary: Bump JSON spec to RFC 8259 (#951)
	* schema: Completely drop our JSON Schema 'id' properties (#945)
	* meeting: Bump January meeting from the 3rd to the 10th (#943)
	* config: add "umask" field to POSIX "user" section (#941)
	* schema: add allowed values for defaultAction (#940)
	* config: Dedent root paragraphs, since they aren't a list entry (#936)
	* fix the link to hook (#933)
	* config: Collapse extensibility to a single MUST (#916)
	* schema/defs-linux: change weight type to uint16 (#898)
	* runtime: Clarify ociVersion as based on the state schema (#903)

Changes with v1.0.1:

	Minor fixes and documentation:

	* spec: Expand "OCI" in spec-title reference and add "Initiative"
	  (#900)
	* config: Simplify title to "Configuration" (#901)
	* config: Fix "procfs_2" -> "proc_2" link label (#906)
	* config: Fix IEEE Std 1003.1-2008 exec link markup (#913)
	* config: Add a trailing period to the "cannot be mapped" rlimits
	  line (#915)
	* config-linux: RFC 2119 MUST for absolute linux.namespaces[].path
	  (#925).  This is technically a breaking change, because a config
	  with a relative namespace path would have been compliant before,
	  but will be non compliant with this change. However, the previous
	  "an absolute path to namespace file" wording was clear enough that
	  config authors are unlikely to be relying on relative namespace
	  paths in configs.
	* config-linux: More specific documentation for weightDevice and
	  throttle* (#825)
	* config-linux: Modify procfs to proc (#905)
	* config-linux: Fix a typo (#921)
	* config-windows: Make maximum a uint16 (was a uint) (#891)
	* runtime: Change "process in the container" -> "container
	  process" (#907)
	* schema/config-schema: Use ArrayOfStrings in capabilities
	  properties. (#886)
	* schema/config-linux:
	  s/throttleWriteIopsDevice/throttleWriteIOPSDevice/ (#899)
	* schema/config-linux: add intelRdt field (#889)
	* schema/config-solaris: Replaced refs with some fields
	  (cappedCPU.ncpus, etc.) (#892)

Changes with v1.0.0:

	Breaking changes:

	* config: Shift disableOOMKiller from linux.resources to
	  linux.resources.memory (#896)

	Decreased restrictions:

	* runtime: Make the state JSON's pid optional on non-Linux platforms
	  (#897)

	Minor fixes and documentation:

	* schema/defs-linux: Require Syscall.action (#885)
	* specs-go/config: Fix 'omiempty' -> 'omitempty' typo for
	  LinuxSeccompArg.ValueTwo (#884)
	* ROAMAP: remove the pre-v1.0.0 roadmap (#890)

Changes with v1.0.0-rc6:

	Breaking changes:

	* config: Shift oomScoreAdj to process and add RFC 2119 requirements
	  for the runtime (#781, #789, #836)
	* config: Forbid 'root' on Hyper-V (#820, #838).
	* config: process.capabilities and process.noNewPrivileges are
	  Linux-only again (#880).  This partially reverses #673, which had
	  landed in v1.0.0-rc5.
	* config: Remove process.rlimits from Windows (#880).  It is now
	  POSIX-only, while in v1.0.0-rc5 it was cross-platform (because of
	  #673).  Before #673 (in v1.0.0-rc4 and earlier), it was
	  Linux-only.
	* config-linux: Drop redundant 'blkio' prefix from blockIO
	  properties (#860)
	* config-linux: Make memory limits int64 instead of uint64 (#876).
	  This partially reverses #704, which had landed in v1.0.0-rc5.
	* config-windows: Change CPU 'percent' to 'maximum' (#777)
	* config-windows: Remove memory 'reservation' (#788)
	* config-windows: Remove 'resources.network' and add 'network' (#801)

	Additions:

	* config: Windows runtimes MUST support the 'ro' mount option (#868)
	* config-linux: Add Intel RDT/CAT Linux support (#630, #787)
	* config-linux: Add Markdown specification for syscalls (#706)
	* config-linux: Add 'unbindable' rootfsPropagation value (#770, #775)
	* config-windows: Add 'credentialSpec' (#814, #859)
	* config-windows: Add 'servicing' (#815)
	* config-windows: Add 'ignoreFlushesDuringBoot' (#816, #859)
	* config-windows: Add 'hyperv' (#818, #849, #859)
	* config-windows: Add 'layerFolders' (#828)

	Removals and increased restrictions:

	* config: Remove 'platform' (#850)
	* config: Require strictly-postitive 'timeout' values (#764)
	* config: Strengthen punt to kernel for valid capabilities strings
	  (#766, #790)
	* config: Require volume GUID paths for root.path (#849)
	* config: Forbid setting 'readonly' true on Windows (#819)
	* config: Forbid setting mount 'type' entirely on Windows and forbid
	  UNC paths and mapped drives in 'source' on Windows (#821)
	* config: Remove 'hooks' from Windows spec (#855, #869, #870)
	* config-linux: Clearly require absolute path for namespace (#720)
	* config-linux: RFC 2119 tightening for namespaces (#767)
	* config-linux: Require at least one entry in
	  linux.seccomp.syscalls[].names (#769)
	* config-linux: Remove syscall.comment (#714)
	* config-linux: Use MUST and MAY for weight and leafWeight (#751)
	* config-linux: Remove explicit 'null' from device cgroup values
	  (#804)
	* runtime: Remove "features the runtime chooses to support" (#732)
	* runtime: Drop "not supported by the base OS" loophole (#733)
	* runtime-linux: Condition /proc/self/fd symlinks on source
	  existence (#736)

	Decreased restrictions:

	* config: Make 'process' optional (#701, #805)
	* config-linux: Make linux.seccomp.syscalls optional (#768)
	* config-linux: valueTwo is now optional in
	  `linux.seccomp.syscalls[].args` entries (#877)
	* config-linux: Remove local range restrictions for blkioWeight,
	  blkioLeafWeight, weight, leafWeight, and shares (#780)
	* config-linux: Explicitly allow symlinks for providing devices (#873)

	Minor fixes and documentation:

	* config: Remove "MAY support any valid values" sentence (#851)
	* config: Remove the previously-forbidden mounts[].type from the
	  Windows spec (#854)
	* config: Clarify mounts[].source relative path anchor (#735)
	* config: Explicitly make consoleSize ignored if terminal is false or
	  unset (#863)
	* config: Specify height/width units (characters) for consoleSize (#761)
	* config: Use "POSIX platforms" instead of "Linux and Solaris" (#838)
	* config-linux: Explicit namespace for interface names (#713)
	* config-linux: Explicitly list cgroupsPath as optional (#823)
	* runtime: Clarify valid container states for 'start', 'kill', and
	  'delete' (#875)
	* runtime: Explicitly make process.* timing implementation-defined (#700)
	* specs-go/config: Remove range restrictions from Windows comments (#783)
	* specs-go/config: Add omitempty to LinuxSyscall.Args (#763)
	* specs-go/config: Use a pointer for Process.ConsoleSize (#792)
	* schema/README: Use v1.0.0 URL in examples to prepare for the 1.0.0
	  release (#881)
	* schema/Makefile: Make 'validate' the default target (#750)
	* schema/Makefile: Add 'clean' target (#774)
	* schema: Add 'test' target to the Makefile (#785)
	* *: Remove unnecessary .PHONY entries (#750, #778, #802)
	* *: Typo fixes and polishing (#681, #708, #702, #703, #709, #711,
	  #712, #721, #722, #723, #724, #730, #737, #738, #741, #744, #749,
	  #753, #756, #765, #773, #776, #784, #786, #793, #794, #796, #798,
	  #799, #800, #803, #807, #809, #811, #812, #822, #824, #826, #827,
	  #832, #839, #840, #846, #847, #848, #852, #856, #858, #862, #865,
	  #871, #874)

Changes with v1.0.0-rc5:

	Breaking changes:

	* config: Explicitly require `platform` (#695).
	* config: The platform-specific sections (`linux`, `solaris`, and
	  `windows`) MUST NOT be set unless they match `platform.os` (#673).
	* config: `process.capabilities` is now an object instead of an
	  array of strings (#675).
	* config-linux: No longer allow negative values for some resources,
	  partially reversing #648 from v1.0.0-rc4 (#704).
	* config-linux: `linux.seccomp.syscalls` entries have `names`
	  instead of `name` (#657).
	* runtime: Rename the state `bundlePath` property to `bundle`
	  (#674).

	Additions:

	* config: `process.capabilities` is no longer Linux-only (#673).
	* config-linux: `linux.seccomp.syscalls` entries have a new
	  `comment` property (#657).
	* config-linux: Add new architectures from libseccomp 2.3.2 (#705)
	* runtime: Add a `creating` state `status` (#507, #694).

	Removals and increased restrictions:

	* runtime: Document hook timing and exit code handling (#532).
	* schema/config-linux: Explicit `null` values are no longer
	  compliant (#662).

	Decreased restrictions:

	* config: `type` and `source` properties are now optional for
	  `mounts` entries (#699).
	* config: `args` property is now optional for hooks (#685).
	* config-linux: Runtimes no longer need to provide `/proc` and
	  other filesystems unless they are explicitly requested in the
	  configuration JSON (#666).

	Minor fixes and documentation:

	* spec: Add OCI Runtime Abstract (#691).
	* config: Document the Go `platform` tag (#570).
	* config-linux: Remove local uid/gid mapping limit and punt to the
	  kernel (#693).
	* schema: Fix broken `string` and similar `$ref`s (#684).
	* schema: Remove `mounts` from required properties (#696).
	* schema: Remove `major` and `minor` from `linux.devices` entries
	  (#688).
	* schema: Check for the required `type`, `hard`, and `soft` in
	  `process.rlimits` entries (#696).
	* schema/validate: Gained usage documentation and fixed
	  `schemaPath` logic when the argument did not contain `://` (#552).
	* *: Add anchor tags to a number of spec locations (#707).
	* *: Consistent link syntax (#687).
        * *: Minor cleanup and rewording (#697).

Changes with v1.0.0-rc4:
	Additions:

	* config-linux: Allow negative values for some resources (#648)
	* config-linux: Lift no-tweaking namespace restriction (#649)

	Removals and increased restrictions:

	* config: Rlimit types must be unique (#607)
	* config: Forbid empty-string keys in 'annotations' (#645, #654)
	* config-linux: Require runtime errors for pre-existing devices
	  (#647)
	* runtime: Only require 'pid' in the state for created/running
	  statuses (#664)
	* schema: Add 'consoleSize' and update requirements (#646)
	* schema: Remove string pointers (#656)
	* schema/config-linux: Remove blockIODeviceThrottle and other
	  pointers (#545)

	Breaking Go changes:

	* specs-go/config: Remove string pointers (#653)
	* specs-go/config: Make Spec.Hooks a pointer (#427)
	* specs-go/config: Convert some resources from unsigned integers
	  to signed integers (#648)

	Minor fixes and documentation:

	* config: Explicitly list 'hooks' as optional and cite POSIX for
	  'env' and 'args' (#427)
	* runtime: Replace "process is stopped" with "process exits"
	  (#465)
	* schema/config-linux: Add missing kernelTCP (#655)
	* schema/validate: Allow schema identifiers to contain a URL
	  scheme (#490)
	* .travis: Fix git-validation commit ranges (#216)
	* *: Add anchor tags to a number of spec locations (#612, #636,
	  #637, #638, #639, #640)
	* *: Typo fixes and polishing (#643, #650, #652, #656, #660, #665)

Changes with v1.0.0-rc3:
	Additions:

	* config: Add support for Windows-based containers (#565, #573)
	* config: Add process.consoleSize (#563)
	* config: Explicitly allow unknown extensions and document
	  annotations key conventions (#510)
	* config: Define mounts entries for Solaris (#588)

	Removals and increased restrictions:

	* config: Require absolute paths for mount destinations (#609)
	* config-linux: Require absolute path for maskedPaths and
	  readonlyPaths (#587)
	* config-linux: Only require /dev/console when process.terminal is
	  true.  Also require /dev/console to be provided by a bind mount
	  (#518)
	* runtime: Require runtimes to generate errors when the container
	  specified in config.json cannot be created (#559)

	Breaking Go changes:

	* specs-go/config: Aggressive namespacing (#567)
	* specs-go/config: Remove pointers from LinuxHugepageLimit,
	  LinuxInterfacePriority, and LinuxPids properties (#586)
	* specs-go/state: Rename version to ociVersion (#633)
	  LinuxInterfacePriority, and LinuxPids properties (#586)

	Minor fixes and documentation:

	* spec: Separate the spec from project scaffolding (#626)
	* README: Define "unspecified", "undefined", and
	 "implementation-defined" (#575)
	* config: Clarify absolute and relative values for root.path (#558)
	* config: Clarify ociVersion covering the configuration <->
	  runtime API (#523)
	* config-linux: Forbid duplicated namespaces with same `type`
	  (#597)
	* glossary: Make objects explicitly unordered and forbid duplicate
	  names (#584)
	* specs-go/config: Add platform tags to Rlimits and
	  NoNewPRivileges (#564)
	* schema/defs-linux: Use int64 for major/minor types (#610)
	* Makefile: Add support for Go 1.7 (#547)
	* Makefile: Require Go >= 1.6 for golint (#589)
	* Makefile: Use a POSIX-compatible test ('==' -> '=') (#542)
	* implementations: Rename ocitools -> runtime-tools (#585)
	* *: Typo fixes and polishing (#556, #566, #568, #569, #571, #572,
	  #574, #595, #596, #599, #600, #601, #603, #605, #608, #613, #617,
	  #619, #621, #622, #623, #624, #625, #627, #629)

Changes with v1.0.0-rc2:
	Additions:

	* config-linux: Add new architectures from libseccomp 2.3.0 (#505)
	* schema: Add JSON Schema for state JSON and move schema.json to
	  config-schema.json and similar (#481, #498, #519)

	Minor fixes and documentation:

	* Add compliance language for platforms and architectures (#527)
	* Remove "unconditionally compliant" language (#553)
	* bundle: Remove distribution references (#487)
	* runtime: Fix sub-bullet indentation (#495)
	* config: Replace Arch fstab reference with mount(8) (#443)
	* config: Synchronize comments between Markdown and Go (#525)
	* config: Drop v0.x compatibility statement (#488)
	* config-linux: RFC 2119 wording for cgroupsPath (#493)
	* config-linux: Make linux.devices and linux.resources.devices
	  optional (#526)
	* config-linux: Extend no-tweak requirement to runtime namespaces (#538)
	* schema: Add hook.timeout (#544)
	* schema: Add missing '"type": "object"' (#528)
	* schema: Run 'make fmt' and remove duplicates (#546, #551)
	* schema/config: Make 'hostname' optional (#491)
	* schema/config-linux: Add linux.resources.devices (#550)
	* specs-go/config: Add Solaris tags to User properties (#496)
	* specs-go/config: Make Linux and Solaris omitempty again (#502)
	* specs-go/config: Make KernelTCP and ClassID omitempty (#531)
	* specs-go/config: Fix "specified" typo for ApparmorProfile (#503)
	* Makefile: Remove code-of-conduct.md and version.md when clean (#541)
	* implementations: Mention cc-oci-runtime (#539)
	* Use filesystem instead of file system (#529)
	* .pullapprove: Add DCO check via PullApprove
	* GOVERNANCE: Add governance and release process docs (#521)
	* README: Change meeting time from 10am to 2pm Pacific (#524)
	* README: Update conference-call phone number (#512, #515)

Changes with v1.0.0-rc1:
	Breaking changes:

	* runtime: Split create and start, #384, #450, #463, #464, #467,
	  #468
	* runtime: Remove exec, #388
	* runtime: Environment MUST match the configuration, #397
	* config: Runtime MUST generate errors for unsupported platforms,
	  #441
	* config: Windows mount destinations MUST NOT be nested, #437

	Additions:

	* solaris: Added platform-specific configuration, #411, #424, #431,
	  #436
	* runtime: Add 'annotations' and 'status' to the state structure,
	  #462, #484, #485
	* runtime: State no longer needs to be serialized as JSON, #446
	* runtime-linux: Add /dev symbolic links, #449
	* config: Allow absolute paths for root.path (which previously
	  required relative paths), #394
	* config-linux: Add linux.mountLabel, #393
	* config-linux: Add support for cgroup namespace, #397
	* config-linux: Runtime SHOULD NOT modify ownership of any
	  referenced filesystem (previously the restriction only applied to
	  the root filesystem), #452
	* specs-go/seccomp: Add ppc and s390x to specs-go/config.go, #475

	Minor fixes and documentation:

	* README: Add project.md to the Table of Contents, #376
	* README: Consistently indent the Table of Contents, #400
	* README: Link to LICENSE, #442
	* README: Weekly call is OCI-wide, #378
	* config: Explicit runtime namespace for hooks, #415
	* config: Explicit container namespace for uid, gid, and
	  additionalGids, #412
	* config: Fix 'string' -> 'array of strings' typo for process.args,
	  #416
	* runtime: The runtime MAY validate config.json, #418
	* runtime: Move errors section out of operations, #445
	* runtime: MAY -> SHOULD for post-stop error logging, #410
	* schema/README: Document JSON Schema usage, #360, #385
	* schema: Minor description updates, #456, #461
	* schema/validate: Support reading documents via stdin, #482
	* .pullapprove: Automate review approval, #458, #474
	* .gitignore: Hide more auto-generated files, #386, #392
	* .travis: git-validation detects Travis now, #366
	* .travis: Regress on failure to produce docs, #479
	* Makefile: Filename docs.* -> oci-runtime-spec.*, #478
	* Makefile: Add install.tools target, #349
	* Makefile: Allow native pandoc implementations, #428, #448
	* Makefile: Prefer Bash, #455
	* Makefile: Travis support for .gitvalidation, #422
	* specs-go/config: Add missing omitempties for Process.Terminal,
	  Root.Readonly, Spec.Linux, and Spec.Mounts, #408, #429, #430, #431
	* specs-go/config: Remove incorrect omitempties for User.UID and
	  User.GID, #425
	* specs-go/config: Drop platform-independent comment, #451
	* version: Include version in generated documentation, #406
	* *: Anchor examples, #348
	* *: Fix remnants from SelinuxProcessLabel to SelinuxLabel rename,
	   #396
	* *: Outsource code-of-conduct to TOB repository, #375, #413
	* *: RFC 2119 consistency, #407, #409, #438, #444, #449
	* *: Typo fixes, #390, #401
	* *: Whitespace fixes and validation, #380, #381, #426
	* ROADMAP: Remove stale targets, #435

Changes with v0.5.0:
	Breaking changes:

	* specs-go: Renamed the repository from opencontainers/specs to
	  opencontainers/runtime-spec, #365

	Additions:

	* config: Add 'timeout' for hooks, #346
	* config-linux: Add 'maskedPaths' and 'readonlyPaths', #364

	Minor fixes and documentation:

	* JSON Schema bug-fixes and improved examples, #370
	* README: Define "unconditionally compliant", #374
	* config: Make Markdown canonical, #342
	* config: Explicitly list mapping from symbolic names to UID/GIDs as
	  out-of-scope, #347
	* config-linux: Require the runtime mount namespace for namespace
	  'path' values, #275
	* config-linux: Reword kernelTCP docs, #377
	* specs-go: Add omitempty to 'Device' and 'Namespace', #340
	* .travis.yml: Use built-in 'go vet' and current 'go lint', dropping
	  Go < 1.5, #372, #352
	* implementations: Expand ocitools scope to include testing, #328
	* style: Move one-sentence-per-line rule from the README, #369
	* style: Remove dangling parenthesis, #359
	* README: Add a link to the IRC logs, #358
	* Fix typos, #353, #354

Changes with v0.4.0:
	Breaking changes:

	* config: Move capabilities, selinuxProcessLabel, apparmorProfile,
	  and noNewPrivileges from the linux setting to the process setting
	  and make them optional, renaming selinuxProcessLabel to
	  selinuxLabel, #329, #330, #339
	* runtime: Rename version to ociVerison in the state JSON, #225
	* runtime: Remove the directory requirement for storing state, now
	  that there is a 'state' operation, #225, #334
	* go: Shift *.go to specs-go/*.go, #276
	* config: Move rlimits to process, #341
	* go: Move config_linux.go content into config.go, removing
	  LinuxSpec, #310

	Additions:

	* schema: Add JSON Schema (and validator) for `config.json`, #313
	* config: Add annotations for opaque-to-the-runtime data, #331
	* config-linux: Make seccomp optional, #333
	* runtime: Added additional operations: state, stop, and exec.
	  #225

	Minor fixes and documentation:

	* config-linux: Change mount type from *rune to *string and fix
	  octal fileMode examples, #323
	* runtime: RFC 2119 phrasing for the lifecycle, #225
	* README: Add a full example of config.json, #276
	* README: Replace BlueJeans with UberConference, #326, #338
	* style: Document Go-pointer exceptions, #317

Changes with v0.3.0:
	Breaking changes:

	* config: Single, unified config file, #284
	* config: cwd is a required default, and must be absolute, #286,
	  #307, #308, #312
	* config: qualify the name of the version field, #309
	* config-linux: Convert classID from hex to uint32, #296
	* config-linux: Separate mknod from cgroups, #298

	Additions:

	* config-linux: Add NoNewPrivileges setting for linux, #290

	Minor fixes and documentation:

	* config-linux: clarify oom_score_adj, #236, #292
	* config-linux: Update links to cgroups documentation, #318
	* config-linux: Remove pointers for slices preferring omitempty
	  tag instead, #316
	* README: add runtime, bundle, and hook author user, #280
	* ROADMAP: reshuffled and split into GitHub issues, #300, #301,
	  #304, #306
	* style: Collect established styles in a discoverable location, #287, #311

Changes with v0.2.0:
	* Add Apparmor, Selinux and Seccomp
	* Add Apparmor, Selinux and Seccomp sections
	* Add bind mount example
	* Add fd section for linux container process
	* Add Go types for specification
	* *: adding a code of conduct
	* Adding cgroups path to the Spec.
	* .: Adding listing of implementations
	* .: adding travis file for future CI
	* Add license and DCO information for contributions
	* Add linux spec description
	* Add MAINTAINERS file
	* Add memory swappiness to linux spec
	* Add runtime state configuration and structs
	* Adds a section for user namespace mappings
	* Adds link to kernel cgroups documentation
	* Adds section for Linux Rlimits
	* Adds section for Linux Sysctl.
	* Adds user namespace to the list of namespaces
	* bundle: add initial run use case
	* bundle: Fix 'and any number of   and other related' typo
	* bundle.md: clarify arbitrary/conventional dirnames
	* bundle.md: fix link formatting
	* bundle.md: fix off-by-one error
	* bundle.md: various updates to latest spec
	* bundle: Move 'Linux sysctl' header to its own line
	* Fix a typo
	* Change Device field order in spec_linux.go, 'Path' should be top of the 'Type' field, according to the different of the config-linux.md, 'Path' field is the unique key.
	* Change layout of mountpoints and mounts
	* Change the rlimit type to string instead of int
	* Clarify behavior around namespaces paths.
	* config: Add example additionalGids
	* config: Add example cwd
	* config: cleanup language on readonly parameter
	* config: fix links to go files
	* config-linux: specify the default devices/filesystems available
	* config.md: clarify destination for mounts
	* config.md: make the version a semver
	* config.md: make the version field example a semver
	* config.md: minor clean up of process specification
	* config.md: reformat into a standard style
	* config.md: update links to spec schema code
	* config.md: various cleanup/consistency fixes
	* config: minor cleanup
	* Deduplicate the field of RootfsPropagation
	* Define constants for Linux Namespace names
	* Fix LinuxRuntime field
	* Fix root object keys
	* Fix typos in config.md
	* Fix typos in the "Namespace types" section
	* Fix typos in the rlimits section
	* Fix Windows path escaping in example mount JSON
	* JSON objects are easier to parse/manipulate
	* made repo public. Added warning in README
	* Make namespaces match runc
	* make rootfs mount propagation mode settable
	* Makes namespaces description linux specific
	* *.md: markdown formatting
	* Modify the capabilities constants to match header files like other constants
	* Move linux specific options to linux spec
	* README: add a rule for paragraph formatting in markdown
	* README: Document BlueJeans and wiki archive for meetings
	* README: Document pre-meeting agenda alteration
	* README: Document YouTube and IRC backchannel for meetings
	* README: Focus on local runtime (create/start/stop)
	* README.md: Add a git commit style guide
	* README.md: contribution about discussion
	* README: releases section
	* README: Remove blank line from infrastructure-agnostic paragraph
	* removed boilerplate file
	* *: remove superfluous comma in code-of-conduct
	* Remove trailing whitespace
	* Rename SystemProperties to Sysctl
	* Rename the header "Access to devices" to "Devices" to fit with the config
	* *: re-org the spec
	* Replace Linux.Device with more specific config
	* restore formatting
	* Return golang compliant names for UID and GID in User
	* Return golint-compliant naming for mappings
	* runtime: Add prestart/poststop hooks
	* runtime_config: comments for golint
	* runtime-config-linux: Drop 'Linux' from headers
	* runtime_config_linux: Fix 'LinuxSpec' -> 'LinuxRuntimeSpec' in comment
	* runtime-config-linux: One sentence per line for opening two paragraphs
	* runtime-config: Remove blank lines from the end of files
	* runtime-config: Remove 'destination' docs from mounts
	* runtime.md: convert oc to runc
	* runtime: use opencontainer vs oci
	* *: small spelling fixes
	* Specific platform specific user struct for spec
	* spec: linux: add support for the PIDs cgroup
	* spec_linux: conform to `golint`
	* spec_linux.go: Rename IDMapping fields to follow syscall.SysProcIDMap
	* spec_linux: remove ending periods on one-line comments
	* spec: rename ocp to oci and add a link
	* specs: add json notation
	* specs: align the ascii graph
	* specs: fix the description for the [ug]idMappings
	* specs: introduce the concept of a runtime.json
	* .tools: cleanup the commit entry
	* .tools: repo validation tool
	* travis: fix DCO validation for merges
	* typo: containers -> container's
	* typo: the -> for
	* Update config-linux for better formatting on values
	* Update README.md
	* Update readme with weekly call and mailing list
	* Update runtime.md
	* Update runtime.md
	* Update runtime.md
	* version: more explicit version for comparison

Changes with v0.1.0:
	* Add Architecture field to Seccomp configuration in Linux runtime
	* Add @hqhq as maintainer
	* Add hyphen for host specific
	* Adding Vishnu Kannan as a Maintainer.
	* Add initial roadmap
	* Add lifecycle for containers
	* Add oom_score_adj to the runtime Spec.
	* Add post-start hooks
	* Add Seccomp constants to description of Linux runtime spec
	* Add Seccomp constants to Linux runtime config
	* Add some clarity around the state.json file
	* adds text describing the upper-case keywords used in the spec
	* add testing framework to ROADMAP
	* Appropriately mark optional fields as omitempty
	* cgroup: Add support for memory.kmem.tcp.limit_in_bytes
	* Change HugepageLimit.Limit type to uint64
	* Change the behavior when cgroupsPath is absent
	* Change version from 0.1.0 to 0.2.0
	* Clarify the semantics of hook elements
	* Cleanup bundle.md
	* Cleanup principles
	* config: linux: update description of PidsLimit
	* config: Require a new UTS namespace for config.json's hostname
	* config: Require the runtime to mount Spec.Mounts in order
	* convert **name** to **`name`**
	* Example lists "root' but text mentions "bundlePath"
	* Fix an extra space in VersionMinor
	* Fix golint warnings
	* Fix typo in BlockIO struct comment
	* Fix typo in Filesystem Bundle
	* Fix value of swappiness
	* glossary: Provide a quick overview of important terms
	* glossary: Specify UTF-8 for all our JSON
	* hooks: deduplicate the hooks docs
	* implementations: Link to kunalkushwaha/octool
	* implementations: Link to mrunalp/ocitools
	* lifecycle: Don't require /run/opencontainer/<runtime>/containers
	* lifecycle: Mention runtime.json
	* lifecycle: no hyphens
	* MAINTAINERS: add tianon per the charter
	* MAINTAINERS: correct Vish's github account
	* Makefile: Add glossary to DOC_FILES
	* Make optional Cgroup related config params pointers along with `omitempty` json tag.
	* Mark RootfsPropagation as omitempty
	* *.md: update TOC and links
	* move the description of Rlimits before example
	* move the description of user ns mapping to proper file
	* principles: Give principles their own home
	* *: printable documents
	* Project: document release process
	* README: Fix some headers
	* README: make header more concise
	* remove blank char from blank line
	* Remove the unneeded build tag from the config_linux.go
	* Remove trailing comma in hooks json example
	* Rename State's Root to Bundle
	* ROADMAP.md: remove the tail spaces
	* roadmap: update links and add wiki reference
	* runtime: Add 'version' to the state.json example
	* runtime-config: add example label before json example
	* runtime-config: add section about Hooks
	* runtime: config: linux: add cgroups information
	* runtime: config: linux: Edit BlockIO struct
	* runtime: config: linux: Fix typo and trailing commas in json example
	* runtime_config_linux.go: add missing pointer
	* runtime-config-linux.md: fix the type of cpus and mems
	* runtime.md: fix spacing
	* Talk about host specific/independent instead of mutability
	* .tools: commit validator is a separate project
	* .tools: make GetFetchHeadCommit do what it says
	* .travis.yml: add go 1.5.1, update from 1.4.2 to 1.4.3
	* Update readme with wiki link to minutes
	* Update Typo in ROADMAP.md
	* Use unsigned for IDs
	* version: introduce a string for dev indication
```

## File: `EMERITUS.md`
```markdown
# Emeritus

We would like to acknowledge previous OCI runtime spec maintainers and their huge contributions to our collective success:

- Rohit Jnagal (@rjnagal)
- Victor Marmol (@vmarmol)
- Alexander Morozov (@LK4D4)
- Vishnu Kannan (@vishh)
- Brandon Philips (@philips)
- Vincent Batts (@vbatts)

We thank these members for their service to the OCI community.
```

## File: `GOVERNANCE.md`
```markdown
# Project governance

The [OCI charter][charter] §5.b.viii tasks an OCI Project's maintainers (listed in the repository's MAINTAINERS file and sometimes referred to as "the TDC", [§5.e][charter]) with:

> Creating, maintaining and enforcing governance guidelines for the TDC, approved by the maintainers, and which shall be posted visibly for the TDC.

This section describes generic rules and procedures for fulfilling that mandate.

## Proposing a motion

A maintainer SHOULD propose a motion on the dev@opencontainers.org mailing list (except [security issues](#security-issues)) with another maintainer as a co-sponsor.

## Voting

Voting on a proposed motion SHOULD happen on the dev@opencontainers.org mailing list (except [security issues](#security-issues)) with maintainers posting LGTM or REJECT.
Maintainers MAY also explicitly not vote by posting ABSTAIN (which is useful to revert a previous vote).
Maintainers MAY post multiple times (e.g. as they revise their position based on feedback), but only their final post counts in the tally.
A proposed motion is adopted if two-thirds of votes cast, a quorum having voted, are in favor of the release.

Voting SHOULD remain open for a week to collect feedback from the wider community and allow the maintainers to digest the proposed motion.
Under exceptional conditions (e.g. non-major security fix releases) proposals which reach quorum with unanimous support MAY be adopted earlier.

A maintainer MAY choose to reply with REJECT.
A maintainer posting a REJECT MUST include a list of concerns or links to written documentation for those concerns (e.g. GitHub issues or mailing-list threads).
The maintainers SHOULD try to resolve the concerns and wait for the rejecting maintainer to change their opinion to LGTM.
However, a motion MAY be adopted with REJECTs, as outlined in the previous paragraphs.

## Quorum

A quorum is established when at least two-thirds of maintainers have voted.

For projects that are not specifications, a [motion to release](#release-approval) MAY be adopted if the tally is at least three LGTMs and no REJECTs, even if three votes does not meet the usual two-thirds quorum.

## Security issues

Motions with sensitive security implications MUST be proposed on the security@opencontainers.org mailing list instead of dev@opencontainers.org, but should otherwise follow the standard [proposal](#proposing-a-motion) process.
The security@opencontainers.org mailing list includes all members of the TOB.
The TOB will contact the project maintainers and provide a channel for discussing and voting on the motion, but voting will otherwise follow the standard [voting](#voting) and [quorum](#quorum) rules.
The TOB and project maintainers will work together to notify affected parties before making an adopted motion public.

## Amendments

The [project governance](#project-governance) rules and procedures MAY be amended or replaced using the procedures themselves.
The MAINTAINERS of this project governance document is the total set of MAINTAINERS from all Open Containers projects (runC, runtime-spec, and image-spec).

## Subject templates

Maintainers are busy and get lots of email.
To make project proposals recognizable, proposed motions SHOULD use the following subject templates.

### Proposing a motion

> [{project} VOTE]: {motion description} (closes {end of voting window})

For example:

> [runtime-spec VOTE]: Tag 0647920 as 1.0.0-rc (closes 2016-06-03 20:00 UTC)

### Tallying results

After voting closes, a maintainer SHOULD post a tally to the motion thread with a subject template like:

> [{project} {status}]: {motion description} (+{LGTMs} -{REJECTs} #{ABSTAINs})

Where `{status}` is either `adopted` or `rejected`.
For example:

> [runtime-spec adopted]: Tag 0647920 as 1.0.0-rc (+6 -0 #3)

[charter]: https://github.com/opencontainers/tob/blob/main/CHARTER.md
```

## File: `LICENSE`
```

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   Copyright 2015 The Linux Foundation.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `MAINTAINERS`
```
Michael Crosby <michael@docker.com> (@crosbymichael)
Mrunal Patel <mpatel@redhat.com> (@mrunalp)
Daniel, Dao Quang Minh <dqminh89@gmail.com> (@dqminh)
Tianon Gravi <admwiggin@gmail.com> (@tianon)
Qiang Huang <h.huangqiang@huawei.com> (@hqhq)
Aleksa Sarai <asarai@suse.de> (@cyphar)
Giuseppe Scrivano <gscrivan@redhat.com> (@giuseppe)
Akihiro Suda <akihiro.suda.cz@hco.ntt.co.jp> (@AkihiroSuda)
Kir Kolyshkin <kolyshkin@gmail.com> (@kolyshkin)
Sebastiaan van Stijn <github@gone.nl> (@thaJeztah)
Toru Komatsu <k0ma@utam0k.jp> (@utam0k)
```

## File: `Makefile`
```

EPOCH_TEST_COMMIT := 78e6667ae2d67aad100b28ee9580b41b7a24e667
OUTPUT_DIRNAME    ?= output
DOC_FILENAME      ?= oci-runtime-spec
DOCKER            ?= $(shell command -v docker 2>/dev/null)
PANDOC            ?= $(shell command -v pandoc 2>/dev/null)
PANDOC_IMAGE      ?= ghcr.io/opencontainers/pandoc:2.9.2.1-9.fc34.x86_64@sha256:590c5c7aaa6e8e7a4debae7e9102c837daa0c8a76f8f5b5c9831ea5f755e3e95
ifeq "$(strip $(PANDOC))" ''
	ifneq "$(strip $(DOCKER))" ''
		PANDOC = $(DOCKER) run \
			--security-opt label=disable \
			--rm \
			-v $(shell pwd)/:/input/:ro \
			-v $(shell pwd)/$(OUTPUT_DIRNAME)/:/$(OUTPUT_DIRNAME)/ \
			-u $(shell id -u) \
			$(PANDOC_IMAGE)
		PANDOC_SRC := /input/
		PANDOC_DST := /
	endif
endif

# These docs are in an order that determines how they show up in the PDF/HTML docs.
DOC_FILES := \
	version.md \
	spec.md \
	principles.md \
	bundle.md \
	runtime.md \
	runtime-linux.md \
	config.md \
	config-linux.md \
	config-solaris.md \
	features.md \
	features-linux.md \
	glossary.md

default: docs

docs: $(OUTPUT_DIRNAME)/$(DOC_FILENAME).pdf $(OUTPUT_DIRNAME)/$(DOC_FILENAME).html

ifeq "$(strip $(PANDOC))" ''
$(OUTPUT_DIRNAME)/$(DOC_FILENAME).pdf $(OUTPUT_DIRNAME)/$(DOC_FILENAME).html:
	$(error cannot build $@ without either pandoc or docker)
else
$(OUTPUT_DIRNAME)/$(DOC_FILENAME).pdf: $(DOC_FILES)
	mkdir -p $(OUTPUT_DIRNAME)/ && \
	$(PANDOC) -f markdown_github -t latex -o $(PANDOC_DST)$@ $(patsubst %,$(PANDOC_SRC)%,$(DOC_FILES))

$(OUTPUT_DIRNAME)/$(DOC_FILENAME).html: $(DOC_FILES)
	mkdir -p $(OUTPUT_DIRNAME)/ && \
	$(PANDOC) -f markdown_github -t html5 -o $(PANDOC_DST)$@ $(patsubst %,$(PANDOC_SRC)%,$(DOC_FILES))
endif

version.md: ./specs-go/version.go
	go run ./.tool/version-doc.go > $@

HOST_GOLANG_VERSION	= $(shell go version | cut -d ' ' -f3 | cut -c 3-)
# this variable is used like a function. First arg is the minimum version, Second arg is the version to be checked.
ALLOWED_GO_VERSION	= $(shell test '$(shell /bin/echo -e "$(1)\n$(2)" | sort -V | head -n1)' = '$(1)' && echo 'true')

test: .govet .golint .gitvalidation

.govet:
	go vet -x ./...

# When this is running in GitHub, it will only check the GitHub commit range
.gitvalidation:
	@which git-validation > /dev/null 2>/dev/null || (echo "ERROR: git-validation not found. Consider 'make install.tools' target" && false)
ifdef GITHUB_SHA
	git-validation -q -run DCO,short-subject,dangling-whitespace -range $(GITHUB_SHA)..HEAD
else
	git-validation -v -run DCO,short-subject,dangling-whitespace -range $(EPOCH_TEST_COMMIT)..HEAD
endif

install.tools: .install.gitvalidation

.install.gitvalidation:
	go install github.com/vbatts/git-validation@v1.2.0

clean:
	rm -rf $(OUTPUT_DIRNAME) *~
	rm -f version.md

```

## File: `README.md`
```markdown
# Open Container Initiative Runtime Specification

[![GitHub Actions status](https://github.com/opencontainers/runtime-spec/workflows/build/badge.svg)](https://github.com/opencontainers/runtime-spec/actions?query=workflow%3Abuild)

The [Open Container Initiative][oci] develops specifications for standards on Operating System process and application containers.

The specification can be found [here](spec.md).

## Table of Contents

Additional documentation about how this group operates:

- [Code of Conduct][code-of-conduct]
- [Style and Conventions](../../../core/security/QUARANTINE/vetted/repos/openclaw/apps/android/style.md)
- [Implementations](implementations.md)
- [Releases](../../../core/security/QUARANTINE/incoming/repos/alasql/RELEASES.md)
- [charter][charter]

## Use Cases

To provide context for users the following section gives example use cases for each part of the spec.

### Application Bundle Builders

Application bundle builders can create a [bundle](bundle.md) directory that includes all of the files required for launching an application as a container.
The bundle contains an OCI [configuration file](config.md) where the builder can specify host-independent details such as [which executable to launch](config.md#process) and host-specific settings such as [mount](config.md#mounts) locations, [hook](config.md#posix-platform-hooks) paths, Linux [namespaces](config-linux.md#namespaces) and [cgroups](config-linux.md#control-groups).
Because the configuration includes host-specific settings, application bundle directories copied between two hosts may require configuration adjustments.

### Hook Developers

[Hook](config.md#posix-platform-hooks) developers can extend the functionality of an OCI-compliant runtime by hooking into a container's lifecycle with an external application.
Example use cases include sophisticated network configuration, volume garbage collection, etc.

### Runtime Developers

Runtime developers can build runtime implementations that run OCI-compliant bundles and container configuration, containing low-level OS and host-specific details, on a particular platform.

## Contributing

Development happens on GitHub for the spec.
Issues are used for bugs and actionable items and longer discussions can happen on the [mailing list](#mailing-list).

The specification and code is licensed under the Apache 2.0 license found in the [LICENSE](./LICENSE) file.

### Discuss your design

The project welcomes submissions, but please let everyone know what you are working on.

Before undertaking a nontrivial change to this specification, send mail to the [mailing list](#mailing-list) to discuss what you plan to do.
This gives everyone a chance to validate the design, helps prevent duplication of effort, and ensures that the idea fits.
It also guarantees that the design is sound before code is written; a GitHub pull-request is not the place for high-level discussions.

Typos and grammatical errors can go straight to a pull-request.
When in doubt, start on the [mailing-list](#mailing-list).

### Meetings

Please see the [OCI org repository README](https://github.com/opencontainers/org#meetings) for the most up-to-date
information on OCI contributor and maintainer meeting schedules. You can also find links to meeting agendas and
minutes for all prior meetings.

### Mailing List

You can subscribe and join the mailing list on [Google Groups][dev-list].

### Chat

OCI discussion happens in the following chat rooms, which are all bridged together:

- #general channel on [OCI Slack](https://opencontainers.org/community/overview/#chat)
- #opencontainers:matrix.org

### Git commit

#### Sign your work

The sign-off is a simple line at the end of the explanation for the patch, which certifies that you wrote it or otherwise have the right to pass it on as an open-source patch.
The rules are pretty simple: if you can certify the below (from https://developercertificate.org):

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
660 York Street, Suite 102,
San Francisco, CA 94110 USA

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

then you just add a line to every git commit message:

    Signed-off-by: Joe Smith <joe@gmail.com>

using your real name (sorry, no pseudonyms or anonymous contributions.)

You can add the sign off when creating the git commit via `git commit -s`.

#### Commit Style

Simple house-keeping for clean git history.
Read more on [How to Write a Git Commit Message][how-to-git-commit] or the Discussion section of [git-commit(1)][git-commit.1].

1. Separate the subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how
    * If there was important/useful/essential conversation or information, copy or include a reference
8. When possible, one keyword to scope the change in the subject (i.e. "README: ...", "runtime: ...")


[charter]: https://github.com/opencontainers/tob/blob/master/CHARTER.md
[code-of-conduct]: https://github.com/opencontainers/org/blob/master/CODE_OF_CONDUCT.md
[dev-list]: https://groups.google.com/a/opencontainers.org/forum/#!forum/dev
[how-to-git-commit]: https://cbea.ms/git-commit/
[iso-week]: https://en.wikipedia.org/wiki/ISO_week_date#Calculating_the_week_number_of_a_given_date
[minutes]: https://ircbot.wl.linuxfoundation.org/meetings/opencontainers/
[oci]: https://www.opencontainers.org
[rfc5545]: https://tools.ietf.org/html/rfc5545
[runtime-wiki]: https://github.com/opencontainers/runtime-spec/wiki
[uberconference]: https://www.uberconference.com/opencontainers

[git-commit.1]: https://git-scm.com/docs/git-commit
```

## File: `RELEASES.md`
```markdown
# Releases

The release process hopes to encourage early, consistent consensus-building during project development.
The mechanisms used are regular community communication on the mailing list about progress, scheduled meetings for issue resolution and release triage, and regularly paced and communicated releases.
Releases are proposed and adopted or rejected using the usual [project governance](GOVERNANCE.md) rules and procedures.

An anti-pattern that we want to avoid is heavy development or discussions "late cycle" around major releases.
We want to build a community that is involved and communicates consistently through all releases instead of relying on "silent periods" as a judge of stability.

## Parallel releases

A single project MAY consider several motions to release in parallel.
However each motion to release after the initial 0.1.0 MUST be based on a previous release that has already landed.

For example, runtime-spec maintainers may propose a v1.0.0-rc2 on the 1st of the month and a v0.9.1 bugfix on the 2nd of the month.
They may not propose a v1.0.0-rc3 until the v1.0.0-rc2 is accepted (on the 7th if the vote initiated on the 1st passes).

## Specifications

The OCI maintains three categories of projects: specifications, applications, and conformance-testing tools.
However, specification releases have special restrictions in the [OCI charter][charter]:

* They are the target of backwards compatibility (§7.g), and
* They are subject to the OFWa patent grant (§8.d and e).

To avoid unfortunate side effects (onerous backwards compatibility requirements or Member resignations), the following additional procedures apply to specification releases:

### Planning a release

Every OCI specification project SHOULD hold meetings that involve maintainers reviewing pull requests, debating outstanding issues, and planning releases.
This meeting MUST be advertised on the project README and MAY happen on a phone call, video conference, or on IRC.
Maintainers MUST send updates to the dev@opencontainers.org with results of these meetings.

Before the specification reaches v1.0.0, the meetings SHOULD be weekly.
Once a specification has reached v1.0.0, the maintainers may alter the cadence, but a meeting MUST be held within four weeks of the previous meeting.

The release plans, corresponding milestones and estimated due dates MUST be published on GitHub (e.g. https://github.com/opencontainers/runtime-spec/milestones).
GitHub milestones and issues are only used for community organization and all releases MUST follow the [project governance](GOVERNANCE.md) rules and procedures.

### Timelines

Specifications have a variety of different timelines in their lifecycle.

* Pre-v1.0.0 specifications SHOULD release on a monthly cadence to garner feedback.
* Major specification releases MUST release at least three release candidates spaced a minimum of one week apart.
    This means a major release like a v1.0.0 or v2.0.0 release will take 1 month at minimum: one week for rc1, one week for rc2, one week for rc3, and one week for the major release itself.
    Maintainers SHOULD strive to make zero breaking changes during this cycle of release candidates and SHOULD restart the three-candidate count when a breaking change is introduced.
    For example if a breaking change is introduced in v1.0.0-rc2 then the series would end with v1.0.0-rc4 and v1.0.0.
* Minor and patch releases SHOULD be made on an as-needed basis.

[charter]: https://github.com/opencontainers/tob/blob/main/CHARTER.md

## Checklist

Releases usually follow a few steps:

* [ ] prepare a pull-request for the release
  * [ ] a commit updating `./ChangeLog`
    * [ ] `git log --oneline --no-merges --decorate --name-status v1.0.1..HEAD | vim -`
    * [ ] `:% s/(pr\/\(\d*\))\(.*\)/\2 (#\1)/` to move the PR to the end of line and match previous formatting
    * [ ] review `(^M|^A|^D)` for impact of the commit
    * [ ] group commits to `Additions:`, `Minor fixes and documentation:`, `Breaking changes:`
    * [ ] delete the `(^M|^A|^D)` lines, `:%!grep -vE '(^M|^A|^D)'`
    * [ ] merge multi-commit PRs (so each line has a `(#num)` suffix)
    * [ ] drop hash and indent, `:'<,'> s/^\w*  /^I* /`
  * [ ] a commit bumping `./specs-go/version.go` to next version and empty the `VersionDev` variable
  * [ ] a commit adding back the "+dev" to `VersionDev`
* [ ] send email to dev@opencontainers.org
  * [ ] copy the exact commit hash for bumping the version from the pull-request (since master always stays as "-dev")
  * [ ] count the PRs since last release (that this version is tracking, in the cases of multiple branching), like `git log --pretty=oneline --no-merges --decorate $priorTag..$versionBumpCommit  | grep \(pr\/ | wc -l`
  * [ ] get the date for a week from now, like `TZ=UTC date --date='next week'`
  * [ ] OPTIONAL find a cute animal gif to attach to the email, and subsequently the release description
  * [ ] subject line like `[runtime-spec VOTE] tag $versionBumpCommit as $version (closes $dateWeekFromNowUTC)`
  * [ ] email body like
```
Hey everyone,

There have been $numPRs PRs merged since $priorTag release (https://github.com/opencontainers/runtime-spec/compare/$priorTag...$versionBumpCommit).

$linkToPullRequest

Please respond LGTM or REJECT (with reasoning).

$sig
```
* [ ] edit/update the pull-request to link to the VOTE thread, from https://groups.google.com/a/opencontainers.org/forum/#!forum/dev
* [ ] a week later, if the vote passes, merge the PR
  * [ ] `git tag -s $version $versionBumpCommit`
  * [ ] `git push --tags`
* [ ] produce release documents
  * [ ] git checkout the release tag, like `git checkout $version`
  * [ ] `make docs`
  * [ ] rename the output PDF and HTML file to include version, like `mv output/oci-runtime-spec.pdf output/oci-runtime-spec-$version.pdf``
  * [ ] attach these docs to the release on https://github.com/opencontainers/runtime-spec/releases
  * [ ] link to the the VOTE thread and include the passing vote count
  * [ ] link to the pull request that merged the release
```

## File: `bundle.md`
```markdown
# <a name="filesystemBundle" />Filesystem Bundle

## <a name="containerFormat" />Container Format

This section defines a format for encoding a container as a *filesystem bundle* - a set of files organized in a certain way, and containing all the necessary data and metadata for any compliant runtime to perform all standard operations against it.
See also [MacOS application bundles][macos_bundle] for a similar use of the term *bundle*.

The definition of a bundle is only concerned with how a container, and its configuration data, are stored on a local filesystem so that it can be consumed by a compliant runtime.

A Standard Container bundle contains all the information needed to load and run a container.
This includes the following artifacts:

1. <a name="containerFormat01" />`config.json`: contains configuration data.
    This REQUIRED file MUST reside in the root of the bundle directory and MUST be named `config.json`.
    See [`config.json`](config.md) for more details.

2. <a name="containerFormat02" />container's root filesystem: the directory referenced by [`root.path`](config.md#root), if that property is set in `config.json`.

When supplied, while these artifacts MUST all be present in a single directory on the local filesystem, that directory itself is not part of the bundle.
In other words, a tar archive of a *bundle* will have these artifacts at the root of the archive, not nested within a top-level directory.

[macos_bundle]: https://en.wikipedia.org/wiki/Bundle_%28macOS%29
```

## File: `config-freebsd.md`
```markdown
# <a name="FreeBSDContainerConfiguration" />FreeBSD Container Configuration

This document describes the schema for the [FreeBSD-specific section](config.md#platform-specific-configuration) of the [container configuration](config.md).

## <a name="configFreeBSDDevices" />Devices

Devices in FreeBSD are accessed via the `devfs` filesystem. Each container SHOULD have a `devfs` filesystem mounted into its `/dev` directory. Often, a minimal set of devices is exposed to the container using ruleset 4 from `/etc/defaults/devfs.rules` - the ruleset is specified as a mount option.

Optionally, additional devices can be exposed to the container using an array of entries inside the `devices` root field:

* **`path`** _(string, REQUIRED)_ - the device path relative to `/dev`
* **`mode`** _(uint32, OPTIONAL)_ - file mode for the device.

Note that JSON numbers must be represented in decimal. The value `448` below is the decimal representation of octal `0700` and this is used to request file mode `rwx------` for the device.

### Example
```json
"devices": [
	{
        "path": "pf",
        "mode": 448
    }
]
```

## <a name="configFreeBSDJail" />Jail

On FreeBSD, containers are implemented using the platform's jail subsystem.
Each jail is configured using a set of name/value pairs passed to the kernel using the `jail(2)` system calls.
The `jail` root field contains values which are passed to the kernel when the container is created.

* **`parent`** _(string, OPTIONAL)_ - parent jail.
    If set, the value is the name of a jail which should be this container's parent, otherwise the container's parent is the host. This can be used to share namespaces such as `vnet` with another container.
* **`host`** _(string, OPTIONAL)_ - allow overriding hostname, domainname, hostuuid and hostid.
    The value can be "new" which allows these values to be overridden in the container or "inherit" to use the host values (or parent container values). If set to "new", the values for hostname and domainname are taken from the base config, if present.
* **`ip4`** _(string, OPTIONAL)_ - control the availability of IPv4 addresses.
    Set to "inherit" to allow access to host (or parent container) addresses or set to "disable" to stop use of IPv4 entirely. This is typically left unset when **`vnet`** is used (see below).
* **`ip4Addr`** _(array of strings, OPTIONAL)_ - restrict the set of IPv4 addresses which the container can use. These addresses should be in numeric form (e.g. `"10.11.12.13"`). This can be used to allow restricted use of the host network. A common pattern with FreeBSD jails is to add alias addresses to a loopback interface and restrict each jail to a subset of addresses.
* **`ip6`** _(string, OPTIONAL)_ - control the availability of IPv6 addresses.
    Set to "inherit" to allow access to host (or parent container) addresses or set to "disable" to stop use of IPv6 entirely. This is typically left unset when **`vnet`** is used (see below).
* **`ip6Addr`** _(array of strings, OPTIONAL)_ - restrict the set of IPv6 addresses which the container can use. These addresses should be in numeric form (e.g. `"fd10::11:12:13"`). This can be used to allow restricted use of the host network. A common pattern with FreeBSD jails is to add alias addresses to a loopback interface and restrict each jail to a subset of addresses.
* **`vnet`** _(string, OPTIONAL)_ - control the vnet used for this container.
    The value can be "new" which causes a new vnet to be created for the container or "inherit" which shares the vnet for the parent container (or host if there is no parent).
* **`interface`** _(string, OPTIONAL)_ A network interface to add the container's IP addresses (**`ip4Addr`** and **`ip6Addr`**) to.  An alias for each address will be added to the interface when the container is created, and will be removed from the interface after the container is stopped. This is typically used when **`vnet`** is not set.
* **`vnetInterfaces`** _(array of strings, OPTIONAL)_ - a set of network interfaces which are added to the container's vnet during its lifetime.
* **`sysvmsg`** _(string, OPTIONAL)_ - allow access to SYSV IPC message primitives.
    If set to "inherit", all IPC objects in the host (or parent container) are visible to this container, whether they were created by the container itself, the base system, or other containers.  If set to "new", the container will have its own key namespace, and can only see the objects that it has created; the system (or parent container) has access to the container's objects, but not to its keys.  If set to "disable", the container cannot perform any sysvmsg-related system calls. Defaults to "new".
* **`sysvsem`** _(string, OPTIONAL)_ - allow access to SYSV IPC semaphore primitives, in the same manner as sysvmsg. Defaults to "new".
* **`sysvshm`** _(string, OPTIONAL)_ - allow access to SYSV IPC shared memory primitives, in the same manner as sysvmsg. Defaults to "new".
* **`enforceStatfs`** _(integer, OPTIONAL)_ - control visibility of mounts in the container.
    A value of 0 allows visibility of all host mounts, 1 allows visibility of mounts nested under the container's root and 2 only allows the container root to be visible. If unset, the default value is 2.
* **`allow`** _(object, OPTIONAL)_ - Some restrictions of the container environment may be set on a per-container basis.  With the exception of **`setHostname`** and **`reservedPorts`**, these boolean parameters are off by default.
  - **`setHostname`** _(bool, OPTIONAL)_ - Allow the container's hostname to be changed. Defaults to `false`.
  - **`rawSockets`** _(bool, OPTIONAL)_ - Allow the container to use raw sockets to support network utilities such as ping and traceroute. Defaults to `false`.
  - **`chflags`** _(bool, OPTIONAL)_ - Allow the system file flags to be changed. Defaults to `false`.
  - **`mount`** _(array of strings, OPTIONAL)_ - Allow the listed filesystem types to be mounted and unmounted in the container.
  - **`quotas`** _(bool, OPTIONAL)_ - Allow the filesystem quotas to be changed in the container. Defaults to `false`.
  - **`socketAf`** _(bool, OPTIONAL)_ - Allow socket types other than IPv4, IPv6 and unix. Defaults to `false`.
  - **`mlock`** _(bool, OPTIONAL)_ - Allow the container to use `mlock(2)` and `munlock(2)` system calls. Defaults to `false`.
  - **`reservedPorts`** _(bool, OPTIONAL)_ - Allow the jail to bind to ports lower than 1024. Defaults to `false`.
  - **`suser`** _(bool, OPTIONAL)_ - The value of the jail's security.bsd.suser_enabled sysctl. The super-user will be disabled automatically if its parent system has it disabled.  The super-user is enabled by default.

These fields SHOULD be mapped to a corresponding set of `jail(8)` parameters which can be used to create the container jail.
A typical jail-based OCI implementation on FreeBSD MAY use the following mapping:

| Jail parameter   | JSON equivalent      |
| --------------   | -------------------- |
| `jid`            | -                    |
| `name`           | see below            |
| `path`           | `root.path`          |
| `ip4.addr`       | `freebsd.jail.ip4Addr` |
| `ip4.saddrsel`   | -                    |
| `ip4`            | `freebsd.jail.ip4`   |
| `ip6.addr`       | `freebsd.jail.ip6Addr` |
| `ip6.saddrsel`   | -                    |
| `ip6`            | `freebsd.jail.ip6`   |
| `vnet`           | `freebsd.jail.vnet`  |
| `interface`      | `freebsd.jail.interface` |
| `vnet.interface` | see below            |
| `host.hostname`  | `hostname`           |
| `host`           | `freebsd.jail.host`  |
| `sysvmsg`        | `freebsd.jail.sysvmsg` |
| `sysvsem`        | `freebsd.jail.sysvsem` |
| `sysvshm`        | `freebsd.jail.sysvshm` |
| `securelevel`    | -                    |
| `devfs_ruleset`  | see below            |
| `children.max`   | see below            |
| `enforce_statfs` | `freebsd.jail.enforceStatfs` |
| `persist`        | -                    |
| `parent`         | `freebsd.jail.parent`  |
| `osrelease`      | -                    |
| `osreldate`      | -                    |
| `allow.set_hostname` | `freebsd.jail.allow.setHostname` |
| `allow.sysvipc`  | `freebsd.jail.allow.sysvipc` |
| `allow.raw_sockets`  | `freebsd.jail.allow.rawSockets` |
| `allow.chflags`  | `freebsd.jail.allow.chflags` |
| `allow.mount`    | `freebsd.jail.allow.mount` |
| `allow.quotas`    | `freebsd.jail.allow.quotas` |
| `allow.read_msgbuf` | -                       |
| `allow.socket_af` | `freebsd.jail.allow.socketAf` |
| `allow.mlock`    | `freebsd.jail.allow.mlock` |
| `allow.nfsd`     | - |
| `allow.reserved_ports` | `freebsd.jail.allow.reservedPorts` |
| `allow.unprivileged_proc_debug` | - |
| `allow.suser`    | `freebsd.jail.allow.suser` |
| `allow.mount.*`  | see below            |

The jail name SHOULD be set to the create command's `container-id` argument.

The `vnet.interface` jail pseudo parameter is not handled in the kernel but rather is implemented in user space (e.g. in `jail(8)`). In traditional jail configs, this parameter can be repeated several times and each instance specifies a network interface which is moved into the jail's vnet during the lifetime of the jail using the `ifconfig(8)` utility on the host. For OCI containers, this is managed using the `freebsd.jail.vnetInterfaces` field which is an array of interface names.

A container which needs its own network namespace SHOULD set `"vnet"` to `"new"` and leave `"ip4"` and `"ip6"` unchanged.
A container which shares the parent/host vnet SHOULD leave `"vnet"` unchanged and set `"ip4"` and `"ip6"` to `"inherit"`.

The `devfs_ruleset` parameter is only required for jails which create new `devfs` mounts - typically OCI runtimes will mount `devfs` on the host. The value is a rule set number - these rule sets are defined on the host, typically via `/etc/defaults/devfs.rules` or using the `devfs` command line utility.

The `children.max` parameter SHOULD be managed by the OCI runtime e.g. when a new container shares namespaces with an existing container.

The `allow.mount.*` parameter set is extensible - allowed mount types are listed as an array. As with `devfs`, typically the OCI runtime will manage mounts for the container by performing mount operations on the host.

Jail parameters not supported by this runtime extension are marked with "-". These parameters will have their default values - see the `jail(8)` man page for details.

### Example
```json
"jail": {
    "host": "new",
    "vnet": "new",
    "enforceStatfs": 1,
	"allow": {
		"rawSockets": true,
		"chflags": true,
		"mount": [
			"tmpfs"
		]
	}
}
```
```

## File: `config-linux.md`
```markdown
# <a name="linuxContainerConfiguration" />Linux Container Configuration

This document describes the schema for the [Linux-specific section](config.md#platform-specific-configuration) of the [container configuration](config.md).
The Linux container specification uses various kernel features like namespaces, cgroups, capabilities, LSM, and filesystem jails to fulfill the spec.

## <a name="configLinuxDefaultFilesystems" />Default Filesystems

The Linux ABI includes both syscalls and several special file paths.
Applications expecting a Linux environment will very likely expect these file paths to be set up correctly.

The following filesystems SHOULD be made available in each container's filesystem:

| Path     | Type   |
| -------- | ------ |
| /proc    | [proc][] |
| /sys     | [sysfs][]  |
| /dev/pts | [devpts][] |
| /dev/shm | [tmpfs][]  |

## <a name="configLinuxNamespaces" />Namespaces

A namespace wraps a global system resource in an abstraction that makes it appear to the processes within the namespace that they have their own isolated instance of the global resource.
Changes to the global resource are visible to other processes that are members of the namespace, but are invisible to other processes.
For more information, see the [namespaces(7)][namespaces.7_2] man page.

Namespaces are specified as an array of entries inside the `namespaces` root field.
The following parameters can be specified to set up namespaces:

* **`type`** *(string, REQUIRED)* - namespace type. The following namespace types SHOULD be supported:
    * **`pid`** processes inside the container will only be able to see other processes inside the same container or inside the same pid namespace.
    * **`network`** the container will have its own network stack.
    * **`mount`** the container will have an isolated mount table.
    * **`ipc`** processes inside the container will only be able to communicate to other processes inside the same container via system level IPC.
    * **`uts`** the container will be able to have its own hostname and domain name.
    * **`user`** the container will be able to remap user and group IDs from the host to local users and groups within the container.
    * **`cgroup`** the container will have an isolated view of the cgroup hierarchy.
    * **`time`** the container will be able to have its own clocks.
* **`path`** *(string, OPTIONAL)* - namespace file.
    This value MUST be an absolute path in the [runtime mount namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
    The runtime MUST place the container process in the namespace associated with that `path`.
    The runtime MUST [generate an error](runtime.md#errors) if `path` is not associated with a namespace of type `type`.

    If `path` is not specified, the runtime MUST create a new [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace) of type `type`.

If a namespace type is not specified in the `namespaces` array, the container MUST inherit the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace) of that type.
If a `namespaces` field contains duplicated namespaces with same `type`, the runtime MUST [generate an error](runtime.md#errors).

### Example

```json
"namespaces": [
    {
        "type": "pid",
        "path": "/proc/1234/ns/pid"
    },
    {
        "type": "network",
        "path": "/var/run/netns/neta"
    },
    {
        "type": "mount"
    },
    {
        "type": "ipc"
    },
    {
        "type": "uts"
    },
    {
        "type": "user"
    },
    {
        "type": "cgroup"
    },
    {
        "type": "time"
    }
]
```

## <a name="configLinuxUserNamespaceMappings" />User namespace mappings

**`uidMappings`** (array of objects, OPTIONAL) describes the user namespace uid mappings from the host to the container.
**`gidMappings`** (array of objects, OPTIONAL) describes the user namespace gid mappings from the host to the container.

Each entry has the following structure:

* **`containerID`** *(uint32, REQUIRED)* - is the starting uid/gid in the container.
* **`hostID`** *(uint32, REQUIRED)* - is the starting uid/gid on the host to be mapped to *containerID*.
* **`size`** *(uint32, REQUIRED)* - is the number of ids to be mapped.

The runtime SHOULD NOT modify the ownership of referenced filesystems to realize the mapping.
Note that the number of mapping entries MAY be limited by the [kernel][user-namespaces].

### Example

```json
"uidMappings": [
    {
        "containerID": 0,
        "hostID": 1000,
        "size": 32000
    }
],
"gidMappings": [
    {
        "containerID": 0,
        "hostID": 1000,
        "size": 32000
    }
]
```

## <a name="configLinuxTimeOffset" />Offset for Time Namespace

**`timeOffsets`** (object, OPTIONAL) sets the offset for Time Namespace. For more information
see the [time_namespaces][time_namespaces.7].

The name of the clock is the entry key.
Entry values are objects with the following properties:

* **`secs`** *(int64, OPTIONAL)* - is the offset of clock (in seconds) in the container.
* **`nanosecs`** *(uint32, OPTIONAL)* - is the offset of clock (in nanoseconds) in the container.

## <a name="configLinuxDevices" />Devices

**`devices`** (array of objects, OPTIONAL) lists devices that MUST be available in the container.
The runtime MAY supply them however it likes (with [`mknod`][mknod.2], by bind mounting from the runtime mount namespace, using symlinks, etc.).

Each entry has the following structure:

* **`type`** *(string, REQUIRED)* - type of device: `c`, `b`, `u` or `p`.
    More info in [mknod(1)][mknod.1].
* **`path`** *(string, REQUIRED)* - full path to device inside container.
    If a [file][] already exists at `path` that does not match the requested device, the runtime MUST generate an error.
    The path MAY be anywhere in the container filesystem, notably outside of `/dev`.
* **`major, minor`** *(int64, REQUIRED unless `type` is `p`)* - [major, minor numbers][devices] for the device.
* **`fileMode`** *(uint32, OPTIONAL)* - file mode for the device. Note it is a decimal (not an octal) number.
    You can also control access to devices [with cgroups](#configLinuxDeviceAllowedlist).
* **`uid`** *(uint32, OPTIONAL)* - id of device owner in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).
* **`gid`** *(uint32, OPTIONAL)* - id of device group in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).

The same `type`, `major` and `minor` SHOULD NOT be used for multiple devices.

Containers MAY NOT access any device node that is not either explicitly
referenced in the **`devices`** array or listed as being part of the
[default devices](#configLinuxDefaultDevices).
Rationale: runtimes based on virtual machines need to be able to adjust the node
devices, and accessing device nodes that were not adjusted could have undefined
behaviour.


### Example

```json
"devices": [
    {
        "path": "/dev/fuse",
        "type": "c",
        "major": 10,
        "minor": 229,
        "fileMode": 438,
        "uid": 0,
        "gid": 0
    },
    {
        "path": "/dev/sda",
        "type": "b",
        "major": 8,
        "minor": 0,
        "fileMode": 432,
        "uid": 0,
        "gid": 0
    }
]
```

### <a name="configLinuxDefaultDevices" />Default Devices

In addition to any devices configured with this setting, the runtime MUST also supply:

* [`/dev/null`][null.4]
* [`/dev/zero`][zero.4]
* [`/dev/full`][full.4]
* [`/dev/random`][random.4]
* [`/dev/urandom`][random.4]
* [`/dev/tty`][tty.4]
* `/dev/console` is set up if [`terminal`](config.md#process) is enabled in the config by bind mounting the pseudoterminal pty to `/dev/console`.
* [`/dev/ptmx`][pts.4].
  A [bind-mount or symlink of the container's `/dev/pts/ptmx`][devpts].

## <a name="configLinuxNetworkDevices" />Network Devices

Linux network devices are entities that send and receive data packets. They are
not represented as files in the `/dev` directory. Instead, they are represented
by the [`net_device`][net_device] data structure in the Linux kernel. Network
devices can belong to only one network namespace and use a set of operations
distinct from regular file operations. Network devices can be categorized as
**physical** or **virtual**:

* **Physical network devices** correspond to hardware interfaces, such as
    Ethernet cards (e.g., `eth0`, `enp0s3`). They are directly associated with
    physical network hardware.
* **Virtual network devices** are software-defined interfaces, such as loopback
    devices (`lo`), virtual Ethernet pairs (`veth`), bridges (`br0`), VLANs, and
    MACVLANs. They are created and managed by the kernel and do not correspond
    to physical hardware.

This schema focuses solely on moving existing network devices identified by name
from the host network namespace into the container network namespace. It does
not cover the complexities of network device creation or network configuration,
such as IP address assignment, routing, and DNS setup.

**`netDevices`** (object, OPTIONAL) - A set of network devices that MUST be made
available in the container. The runtime is responsible for moving these devices;
the underlying mechanism is implementation-defined.

The name of the network device is the entry key. Entry values are objects with
the following properties:

* **`name`** *(string, OPTIONAL)* - the name of the network device inside the
    container namespace. If not specified, the host name is used.

The runtime MUST check if moving the network interface to the container
namespace is possible. If a network device with the specified name already
exists in the container namespace, the runtime MUST [generate an error](runtime.md#errors),
unless the user has provided a template by appending
`%d` to the new name. In that case, the runtime MUST allow the move, and the
kernel will generate a unique name for the interface within the container's
network namespace.

The runtime MUST preserve existing network interface attributes, including all
permanent IP addresses (IFA_F_PERMANENT flag) of any family with global scope
(RT_SCOPE_UNIVERSE value) as defined in [`RFC 3549 Section 2.3.3.2`][rfc3549].
This ensures that only addresses intended for persistent, external communication
are transferred.

The runtime MUST set the network device state to "up" after moving it to the
network namespace to allow the container to send and receive network traffic
through that device.

### Namespace Lifecycle and Container Termination

The runtime MUST NOT actively manage the interface's lifecycle and configuration
*within* the container's network namespace. This is because network interfaces
are inherently tied to the network namespace itself, and their lifecycle is
therefore managed by the owner of the network namespace. Typically, this
ownership and management are handled by higher-level container runtime
orchestrators, rather than the processes running directly within the container.

The runtime **MUST NOT** attempt to move the interface out of the namespace
before deletion. This design decision is based on the following:

* **Namespace Ownership:** Network interfaces are tied to the network namespace,
    which may not always be directly managed by the runtime.
* **Abrupt Termination:** Even when the runtime manages the namespace, it cannot
    reliably participate in its deletion if the container's processes terminate
    abruptly (e.g., due to a crash) or run until completion.

During the network namespace deletion the kernel's built-in namespace cleanup
mechanisms take over, as described in [network_namespaces(7)][net_namespaces.7]:
"When a network namespace is freed (i.e., when the last process in the namespace
terminates), its physical network devices are moved back to the initial network
namespace." All the network namespace migratable physical network devices are
moved to the default network namespace, while virtual devices (veth, macvlan,
...) are destroyed.

If users require custom handling of interface lifecycle during namespace
deletion, they can utilize existing features within the namespace orchestrator
or employ post-stop hooks.

**Physical Interface Renaming and Systemd**

When a physical interface is renamed within a container and the container's
network namespace is later deleted, the kernel will move the interface back to
the root namespace with its renamed name. In case of a name conflict in the root
namespace, the kernel will rename it to `dev%d`. To ensure predictable interface
names in the root namespace, users can utilize systemd's `udevd` and `networkd`
rules. Refer to [systemd Predictable Network Interface Names][predictable-network-interfaces-names]
for more information on configuring predictable names.

### Example

#### Moving a device with a renamed interface inside the container:

```json
"netDevices": {
    "eth0" : {
        "name": "container_eth0"
    }
}
```

## <a name="configLinuxControlGroups" />Control groups

Also known as cgroups, they are used to restrict resource usage for a container and handle device access.
cgroups provide controls (through controllers) to restrict cpu, memory, IO, pids, network and RDMA resources for the container.
For more information, see the [kernel cgroups documentation][cgroup-v1].

A runtime MAY, during a particular [container operation](runtime.md#operation),
such as [create](runtime.md#create), [start](runtime.md#start), or
[exec](runtime.md#exec), check if the container cgroup is fit for purpose,
and MUST [generate an error](runtime.md#errors) if such a check fails.
For example, a frozen cgroup or (for [create](runtime.md#create) operation)
a non-empty cgroup. The reason for this is that accepting such configurations
could cause container operation outcomes that users may not anticipate or
understand, such as operation on one container inadvertently affecting other
containers.

### <a name="configLinuxCgroupsPath" />Cgroups Path

**`cgroupsPath`** (string, OPTIONAL) path to the cgroups.
It can be used to either control the cgroups hierarchy for containers or to run a new process in an existing container.

The value of `cgroupsPath` MUST be either an absolute path or a relative path.

* In the case of an absolute path (starting with `/`), the runtime MUST take the path to be relative to the cgroups mount point.
* In the case of a relative path (not starting with `/`), the runtime MAY interpret the path relative to a runtime-determined location in the cgroups hierarchy.

If the value is specified, the runtime MUST consistently attach to the same place in the cgroups hierarchy given the same value of `cgroupsPath`.
If the value is not specified, the runtime MAY define the default cgroups path.
Runtimes MAY consider certain `cgroupsPath` values to be invalid, and MUST generate an error if this is the case.

Implementations of the Spec can choose to name cgroups in any manner.
The Spec does not include naming schema for cgroups.
The Spec does not support per-controller paths for the reasons discussed in the [cgroupv2 documentation][cgroup-v2].
The cgroups will be created if they don't exist.

You can configure a container's cgroups via the `resources` field of the Linux configuration.
Do not specify `resources` unless limits have to be updated.
For example, to run a new process in an existing container without updating limits, `resources` need not be specified.

Runtimes MAY attach the container process to additional cgroup controllers beyond those necessary to fulfill the `resources` settings.

### Cgroup ownership

Runtimes MAY, according to the following rules, change (or cause to
be changed) the owner of the container's cgroup to the host uid that
maps to the value of `process.user.uid` in the [container
namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace); that is, the user that
will execute the container process.

Runtimes SHOULD NOT change the ownership of container cgroups when
cgroups v1 is in use.  Cgroup delegation is not secure in cgroups
v1.

A runtime SHOULD NOT change the ownership of a container cgroup
unless it will also create a new cgroup namespace for the container.
Typically this occurs when the `linux.namespaces` array contains an
object with `type` equal to `"cgroup"` and `path` unset.

Runtimes SHOULD change the cgroup ownership if and only if the
cgroup filesystem is to be mounted read/write; that is, when the
configuration's `mounts` array contains an object where:

- The `source` field is equal to `"cgroup"`
- The `destination` field is equal to `"/sys/fs/cgroup"`
- The `options` field does not contain the value `"ro"`

If the configuration does not specify such a mount, the runtime
SHOULD NOT change the cgroup ownership.

A runtime that changes the cgroup ownership SHOULD only change the
ownership of the container's cgroup directory and files within that
directory that are listed in `/sys/kernel/cgroup/delegate`.  See
`cgroups(7)` for details about this file.  Note that not all files
listed in `/sys/kernel/cgroup/delegate` necessarily exist in every
cgroup.  Runtimes MUST NOT fail in this scenario, and SHOULD change
the ownership of the listed files that do exist in the cgroup.

If the `/sys/kernel/cgroup/delegate` file does not exist, the
runtime MUST fall back to using the following list of files:

```
cgroup.procs
cgroup.subtree_control
cgroup.threads
```

The runtime SHOULD NOT change the ownership of any other files.
Changing other files may allow the container to elevate its own
resource limits or perform other unwanted behaviour.

### Example

```json
"cgroupsPath": "/myRuntime/myContainer",
"resources": {
    "memory": {
    "limit": 100000,
    "reservation": 200000
    },
    "devices": [
        {
            "allow": false,
            "access": "rwm"
        }
    ]
}
```

### <a name="configLinuxDeviceAllowedlist" />Allowed Device list

**`devices`** (array of objects, OPTIONAL) configures the [allowed device list][cgroup-v1-devices].
The runtime MUST apply entries in the listed order.

Each entry has the following structure:

* **`allow`** *(boolean, REQUIRED)* - whether the entry is allowed or denied.
* **`type`** *(string, OPTIONAL)* - type of device: `a` (all), `c` (char), or `b` (block).
    Unset values mean "all", mapping to `a`.
* **`major, minor`** *(int64, OPTIONAL)* - [major, minor numbers][devices] for the device.
    Unset values mean "all", mapping to [`*` in the filesystem API][cgroup-v1-devices].
* **`access`** *(string, OPTIONAL)* - cgroup permissions for device.
    A composition of `r` (read), `w` (write), and `m` (mknod).

#### Example

```json
"devices": [
    {
        "allow": false,
        "access": "rwm"
    },
    {
        "allow": true,
        "type": "c",
        "major": 10,
        "minor": 229,
        "access": "rw"
    },
    {
        "allow": true,
        "type": "b",
        "major": 8,
        "minor": 0,
        "access": "r"
    }
]
```

### <a name="configLinuxMemory" />Memory

**`memory`** (object, OPTIONAL) represents the cgroup subsystem `memory` and it's used to set limits on the container's memory usage.
For more information, see the kernel cgroups documentation about [memory][cgroup-v1-memory].

Values for memory specify the limit in bytes, or `-1` for unlimited memory.

* **`limit`** *(int64, OPTIONAL)* - sets limit of memory usage
* **`reservation`** *(int64, OPTIONAL)* - sets soft limit of memory usage
* **`swap`** *(int64, OPTIONAL)* - sets limit of memory+Swap usage
* **`kernel`** *(int64, OPTIONAL, NOT RECOMMENDED)* - sets hard limit for kernel memory
* **`kernelTCP`** *(int64, OPTIONAL, NOT RECOMMENDED)* - sets hard limit for kernel TCP buffer memory

The following properties do not specify memory limits, but are covered by the `memory` controller:

* **`swappiness`** *(uint64, OPTIONAL)* - sets swappiness parameter of vmscan (See sysctl's vm.swappiness)
    The values are from 0 to 100. Higher means more swappy.
* **`disableOOMKiller`** *(bool, OPTIONAL)* - enables or disables the OOM killer.
    If enabled (`false`), tasks that attempt to consume more memory than they are allowed are immediately killed by the OOM killer.
    The OOM killer is enabled by default in every cgroup using the `memory` subsystem.
    To disable it, specify a value of `true`.
* **`useHierarchy`** *(bool, OPTIONAL)* - enables or disables hierarchical memory accounting.
    If enabled (`true`), child cgroups will share the memory limits of this cgroup.
* **`checkBeforeUpdate`** *(bool, OPTIONAL)* - enables container memory usage check before setting a new limit.
    If enabled (`true`), runtime MAY check if a new memory limit is lower than the current usage, and MUST
    reject the new limit. Practically, when cgroup v1 is used, the kernel rejects the limit lower than the
    current usage, and when cgroup v2 is used, an OOM killer is invoked. This setting can be used on
    cgroup v2 to mimic the cgroup v1 behavior.

#### Example

```json
"memory": {
    "limit": 536870912,
    "reservation": 536870912,
    "swap": 536870912,
    "kernel": -1,
    "kernelTCP": -1,
    "swappiness": 0,
    "disableOOMKiller": false
}
```

### <a name="configLinuxCPU" />CPU

**`cpu`** (object, OPTIONAL) represents the cgroup subsystems `cpu` and `cpusets`.
For more information, see the kernel cgroups documentation about [cpusets][cgroup-v1-cpusets].

The following parameters can be specified to set up the controller:

* **`shares`** *(uint64, OPTIONAL)* - specifies a relative share of CPU time available to the tasks in a cgroup
* **`quota`** *(int64, OPTIONAL)* - specifies the total amount of time in microseconds for which all tasks in a cgroup can run during one period (as defined by **`period`** below)
    If specified with any (valid) positive value, it MUST be no smaller than `burst` (runtimes MAY generate an error).
* **`burst`** *(uint64, OPTIONAL)* - specifies the maximum amount of accumulated time in microseconds for which all tasks in a cgroup can run additionally for burst during one period (as defined by **`period`** below)
    If specified, this value MUST be no larger than any positive `quota` (runtimes MAY generate an error).
* **`period`** *(uint64, OPTIONAL)* - specifies a period of time in microseconds for how regularly a cgroup's access to CPU resources should be reallocated (CFS scheduler only)
* **`realtimeRuntime`** *(int64, OPTIONAL)* - specifies a period of time in microseconds for the longest continuous period in which the tasks in a cgroup have access to CPU resources
* **`realtimePeriod`** *(uint64, OPTIONAL)* - same as **`period`** but applies to realtime scheduler only
* **`cpus`** *(string, OPTIONAL)* - list of CPUs the container will run on. This is a comma-separated list, with dashes to represent ranges. For example, `0-3,7` represents CPUs 0,1,2,3, and 7.
* **`mems`** *(string, OPTIONAL)* - list of memory nodes the container will run on. This is a comma-separated list, with dashes to represent ranges. For example, `0-3,7` represents memory nodes 0,1,2,3, and 7.
* **`idle`** *(int64, OPTIONAL)* - cgroups are configured with minimum weight, 0: default behavior, 1: SCHED_IDLE.

#### Example

```json
"cpu": {
    "shares": 1024,
    "quota": 1000000,
    "burst": 1000000,
    "period": 500000,
    "realtimeRuntime": 950000,
    "realtimePeriod": 1000000,
    "cpus": "2-3",
    "mems": "0-7",
    "idle": 0
}
```

### <a name="configLinuxBlockIO" />Block IO

**`blockIO`** (object, OPTIONAL) represents the cgroup subsystem `blkio` which implements the block IO controller.
For more information, see the kernel cgroups documentation about [blkio][cgroup-v1-blkio] of cgroup v1 or [io][cgroup-v2-io] of cgroup v2, .

Note that I/O throttling settings in cgroup v1 apply only to Direct I/O due to kernel implementation constraints, while this limitation does not exist in cgroup v2.

The following parameters can be specified to set up the controller:

* **`weight`** *(uint16, OPTIONAL)* - specifies per-cgroup weight. This is default weight of the group on all devices until and unless overridden by per-device rules.
* **`leafWeight`** *(uint16, OPTIONAL)* - equivalents of `weight` for the purpose of deciding how much weight tasks in the given cgroup has while competing with the cgroup's child cgroups.
* **`weightDevice`** *(array of objects, OPTIONAL)* - an array of per-device bandwidth weights.
    Each entry has the following structure:
    * **`major, minor`** *(int64, REQUIRED)* - major, minor numbers for device.
        For more information, see the [mknod(1)][mknod.1] man page.
    * **`weight`** *(uint16, OPTIONAL)* - bandwidth weight for the device.
    * **`leafWeight`** *(uint16, OPTIONAL)* - bandwidth weight for the device while competing with the cgroup's child cgroups, CFQ scheduler only

    You MUST specify at least one of `weight` or `leafWeight` in a given entry, and MAY specify both.

* **`throttleReadBpsDevice`**, **`throttleWriteBpsDevice`** *(array of objects, OPTIONAL)* - an array of per-device bandwidth rate limits.
    Each entry has the following structure:
    * **`major, minor`** *(int64, REQUIRED)* - major, minor numbers for device.
        For more information, see the [mknod(1)][mknod.1] man page.
    * **`rate`** *(uint64, REQUIRED)* - bandwidth rate limit in bytes per second for the device

* **`throttleReadIOPSDevice`**, **`throttleWriteIOPSDevice`** *(array of objects, OPTIONAL)* - an array of per-device IO rate limits.
    Each entry has the following structure:
    * **`major, minor`** *(int64, REQUIRED)* - major, minor numbers for device.
        For more information, see the [mknod(1)][mknod.1] man page.
    * **`rate`** *(uint64, REQUIRED)* - IO rate limit for the device

#### Example

```json
"blockIO": {
    "weight": 10,
    "leafWeight": 10,
    "weightDevice": [
        {
            "major": 8,
            "minor": 0,
            "weight": 500,
            "leafWeight": 300
        },
        {
            "major": 8,
            "minor": 16,
            "weight": 500
        }
    ],
    "throttleReadBpsDevice": [
        {
            "major": 8,
            "minor": 0,
            "rate": 600
        }
    ],
    "throttleWriteIOPSDevice": [
        {
            "major": 8,
            "minor": 16,
            "rate": 300
        }
    ]
}
```

### <a name="configLinuxHugePageLimits" />Huge page limits

**`hugepageLimits`** (array of objects, OPTIONAL) represents the `hugetlb` controller which allows to limit the HugeTLB reservations (if supported) or usage (page fault).
By default if supported by the kernel, `hugepageLimits` defines the hugepage sizes and limits for HugeTLB controller
reservation accounting, which allows to limit the HugeTLB reservations per control group and enforces the controller
limit at reservation time and at the fault of HugeTLB memory for which no reservation exists.
Otherwise if not supported by the kernel, this should fallback to the page fault accounting, which allows users to limit
the HugeTLB usage (page fault) per control group and enforces the limit during page fault.

Note that reservation limits are superior to page fault limits, since reservation limits are enforced at reservation
time (on mmap or shget), and never causes the application to get SIGBUS signal if the memory was reserved before hand.
This allows for easier fallback to alternatives such as non-HugeTLB memory for example. In the case of page fault
accounting, it's very hard to avoid processes getting SIGBUS since the sysadmin needs precisely know the HugeTLB usage
of all the tasks in the system and make sure there is enough pages to satisfy all requests. Avoiding tasks getting
SIGBUS on overcommited systems is practically impossible with page fault accounting.

For more information, see the kernel cgroups documentation about [HugeTLB][cgroup-v1-hugetlb].

Each entry has the following structure:

* **`pageSize`** *(string, REQUIRED)* - hugepage size.
    The value has the format `<size><unit-prefix>B` (64KB, 2MB, 1GB), and must match the `<hugepagesize>` of the
    corresponding control file found in `/sys/fs/cgroup/hugetlb/hugetlb.<hugepagesize>.rsvd.limit_in_bytes` (if
    hugetlb_cgroup reservation is supported) or `/sys/fs/cgroup/hugetlb/hugetlb.<hugepagesize>.limit_in_bytes` (if not
    supported).
    Values of `<unit-prefix>` are intended to be parsed using base 1024 ("1KB" = 1024, "1MB" = 1048576, etc).
* **`limit`** *(uint64, REQUIRED)* - limit in bytes of *hugepagesize* HugeTLB reservations (if supported) or usage.

#### Example

```json
"hugepageLimits": [
    {
        "pageSize": "2MB",
        "limit": 209715200
    },
    {
        "pageSize": "64KB",
        "limit": 1000000
    }
]
```

### <a name="configLinuxNetwork" />Network

**`network`** (object, OPTIONAL) represents the cgroup subsystems `net_cls` and `net_prio`.
For more information, see the kernel cgroups documentations about [net\_cls cgroup][cgroup-v1-net-cls] and [net\_prio cgroup][cgroup-v1-net-prio].

The following parameters can be specified to set up the controller:

* **`classID`** *(uint32, OPTIONAL)* - is the network class identifier the cgroup's network packets will be tagged with
* **`priorities`** *(array of objects, OPTIONAL)* - specifies a list of objects of the priorities assigned to traffic originating from processes in the group and egressing the system on various interfaces.
    The following parameters can be specified per-priority:
    * **`name`** *(string, REQUIRED)* - interface name in [runtime network namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace)
    * **`priority`** *(uint32, REQUIRED)* - priority applied to the interface

#### Example

```json
"network": {
    "classID": 1048577,
    "priorities": [
        {
            "name": "eth0",
            "priority": 500
        },
        {
            "name": "eth1",
            "priority": 1000
        }
    ]
}
```

### <a name="configLinuxPIDS" />PIDs

**`pids`** (object, OPTIONAL) represents the cgroup subsystem `pids`.
For more information, see the kernel cgroups documentation about [pids][cgroup-v1-pids].

The following parameters can be specified to set up the controller:

* **`limit`** *(int64, OPTIONAL)* - specifies the maximum number of tasks in the cgroup, with `-1` indicating no limit (`max`).

> Note: Even though it may superficially seem redundant, `0` is a valid limit value for the `pids` cgroup controller from the kernel's perspective and SHOULD be treated as such by runtimes.

#### Example

```json
"pids": {
    "limit": 32771
}
```

### <a name="configLinuxRDMA" />RDMA

**`rdma`** (object, OPTIONAL) represents the cgroup subsystem `rdma`.
For more information, see the kernel cgroups documentation about [rdma][cgroup-v1-rdma].

The name of the device to limit is the entry key.
Entry values are objects with the following properties:

* **`hcaHandles`** *(uint32, OPTIONAL)* - specifies the maximum number of hca_handles in the cgroup
* **`hcaObjects`** *(uint32, OPTIONAL)* - specifies the maximum number of hca_objects in the cgroup

You MUST specify at least one of the `hcaHandles` or `hcaObjects` in a given entry, and MAY specify both.

#### Example

```json
"rdma": {
    "mlx5_1": {
        "hcaHandles": 3,
        "hcaObjects": 10000
    },
    "mlx4_0": {
        "hcaObjects": 1000
    },
    "rxe3": {
        "hcaObjects": 10000
    }
}
```

## <a name="configLinuxUnified" />Unified

**`unified`** (object, OPTIONAL) allows cgroup v2 parameters to be to be set and modified for the container.

Each key in the map refers to a file in the cgroup unified hierarchy.

The OCI runtime MUST ensure that the needed cgroup controllers are enabled for the cgroup.

Configuration unknown to the runtime MUST still be written to the relevant file.

The runtime MUST generate an error when the configuration refers to a cgroup controller that is not present or that cannot be enabled.

### Example

```json
"unified": {
    "io.max": "259:0 rbps=2097152 wiops=120\n253:0 rbps=2097152 wiops=120",
    "hugetlb.1GB.max": "1073741824"
}
```

If a controller is enabled on the cgroup v2 hierarchy but the configuration is provided for the cgroup v1 equivalent controller, the runtime MAY attempt a conversion.

If the conversion is not possible the runtime MUST generate an error.

## <a name="configLinuxIntelRdt" />IntelRdt

**`intelRdt`** (object, OPTIONAL) represents the [Intel Resource Director Technology][intel-rdt-cat-kernel-interface].
If `intelRdt` is set, the runtime MUST write the container process ID to the `tasks` file in a proper sub-directory in a mounted `resctrl` pseudo-filesystem. That sub-directory name is specified by `closID` parameter.
If no mounted `resctrl` pseudo-filesystem is available in the [runtime mount namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace), the runtime MUST [generate an error](runtime.md#errors).

If `intelRdt` is not set, the runtime MUST NOT manipulate any `resctrl` pseudo-filesystems.

The following parameters can be specified for the container:

* **`closID`** *(string, OPTIONAL)* - specifies the identity for RDT Class of Service (CLOS).
  As a special case, value `/` means that the container MUST be assigned to the default CLOS (the
  root of the resctrl filesystem).

* **`l3CacheSchema`** *(string, OPTIONAL)* - specifies the schema for L3 cache id and capacity bitmask (CBM).
    The value SHOULD start with `L3:` and SHOULD NOT contain newlines.
* **`memBwSchema`** *(string, OPTIONAL)* - specifies the schema of memory bandwidth per L3 cache id.
    The value MUST start with `MB:` and MUST NOT contain newlines.
* **`schemata`** *(array of strings, OPTIONAL)* - specifies the schemata to be written to the `schemata` file in resctrlfs. Each element represents one line in the `schemata` file. The value MUST NOT contain newlines.
* **`enableMonitoring`** *(boolean, OPTIONAL)* - enables resctrl monitoring for the container.

The following rules on parameters MUST be applied:

* If both `l3CacheSchema` and `memBwSchema` are set, runtimes MUST write the values to the `schemata` file in that sub-directory discussed in `closID`. The runtimes MUST write `l3CacheSchema` first and `memBwSchema` last.

* If either `l3CacheSchema` or `memBwSchema` is set, runtimes MUST write the value to the `schemata` file in the that sub-directory discussed in `closID`.

* If `schemata` field is set, runtimes MUST write the value to the `schemata` file in the that sub-directory discussed in `closID`. If also `l3CacheSchema` or `memBwSchema` is set the value of `schemata` field must be written last, after the values from `l3CacheSchema` and `memBwSchema` has been written.

* If none of `l3CacheSchema`, `memBwSchema` or `schemata` is set, runtimes MUST NOT write to `schemata` files in any `resctrl` pseudo-filesystems.

* If `closID` is not set, runtimes MUST use the container ID from [`start`](runtime.md#start) and create the `<container-id>` directory.

* If `closID` is set, `l3CacheSchema` and/or `memBwSchema` and/or `schemata` is set
  * if `closID` directory in a mounted `resctrl` pseudo-filesystem doesn't exist, the runtimes MUST create it.
  * if `closID` directory in a mounted `resctrl` pseudo-filesystem exists, runtimes MUST compare `l3CacheSchema` and/or `memBwSchema` value with `schemata` file, and [generate an error](runtime.md#errors) if doesn't match.

* If `closID` is set, and none of `l3CacheSchema`, `memBwSchema` or `schemata` are set, runtime MUST check if corresponding pre-configured directory `closID` is present in mounted `resctrl`. If such pre-configured directory `closID` exists, runtime MUST assign container to this `closID` and [generate an error](runtime.md#errors) if directory does not exist.

* If `closID` is not set and the runtime has created the sub-directory, the runtime MUST remove the sub-directory when the container is deleted.

* If `closID` is set or the runtime has not created the sub-directory, the runtime MUST NOT remove the sub-directory when the container is deleted.

* If `enableMonitoring` is set, the runtime MUST create a dedicated MON group
  for the container. The runtime MUST use the container ID from
  [`start`](runtime.md#start) as the name of the MON group, i.e. create
  `mon_groups/<container-id>/` subdirectory under the top-level CTRL_MON group
  (named after `closID` or `<container-id>`, see above). The runtime MUST
  delete the MON group after the container is deleted. If creation of the MON
  group fails (e.g. the maximum number of MON groups is reached) the runtime MUST
  return an error.

> **NOTE:** The `enableCMT` and `enableMBM` parameters, available in runtime-spec versions v1.1.0 through v1.2.1, were
> replaced with a unified `enableMonitoring` parameter in v1.3.0. Their semantics were loosely defined and there were
> no known implementations. More critically, these parameters were problematic as hardware does not support selective
> enabling of individual monitoring features. This scheme also made it unnecessarily complex to add support for new
> monitoring features, without providing any recognized benefits.

### Example

Consider a two-socket machine with:

- two L3 caches where the default CBM is 0x7ff (11 bits)
- eight L2 caches where the default CBM is 0xFF (8 bits)
- minimum memory bandwidth of 10% with a memory bandwidth granularity of 10%

Tasks inside the container:

- have access to the "upper" 7/11 of L3 cache on socket 0 and the "lower" 5/11 L3 cache on socket 1
- have access to the "lower" 4/8 of L2 cache on socket 0 (socket 1 is left out from this example)
- may use a maximum memory bandwidth of 20% on socket 0 and 70% on socket 1.

```json
"linux": {
    "intelRdt": {
        "closID": "guaranteed_group",
        "schemata": [
            "L3:0=7f0;1=1f",
            "L2:0=f;1=f;2=f;3=f",
            "MB:0=20;1=70"
        ]
    }
}
```

## <a name="configLinuxMemoryPolicy" />Memory policy

**`memoryPolicy`** (object, OPTIONAL) sets the NUMA memory policy for the container.
For more information see the [set_mempolicy(2)][set_mempolicy.2] man page.

* **`mode`** *(string, REQUIRED)* -

    A valid list of constants is shown below.

    * `MPOL_DEFAULT`
    * `MPOL_BIND`
    * `MPOL_INTERLEAVE`
    * `MPOL_WEIGHTED_INTERLEAVE`
    * `MPOL_PREFERRED`
    * `MPOL_PREFERRED_MANY`
    * `MPOL_LOCAL`

* **`nodes`** *(string, OPTIONAL)* - list of memory nodes from which nodemask is constructed to set_mempolicy(2). This is a comma-separated list, with dashes to represent ranges. For example, `0-3,7` represents memory nodes 0,1,2,3, and 7. Some modes require that there are no nodes, e.g. `MPOL_DEFAULT` and `MPOL_LOCAL`. Others that there is at least one node, e.g. `MPOL_BIND` and `MPOL_INTERLEAVE`. See set_mempolicy(2) for details.

* **`flags`** *(array of strings, OPTIONAL)* - list of flags to use with set_mempolicy(2).

    A valid list of constants is shown below.

    * `MPOL_F_NUMA_BALANCING`
    * `MPOL_F_RELATIVE_NODES`
    * `MPOL_F_STATIC_NODES`

### Example

```json
"linux": {
    "memoryPolicy": {
        "mode": "MPOL_INTERLEAVE",
        "nodes": "2-3"
        "flags": ["MPOL_F_STATIC_NODES"],
    }
}
```

## <a name="configLinuxSysctl" />Sysctl

**`sysctl`** (object, OPTIONAL) allows kernel parameters to be modified at runtime for the container.
For more information, see the [sysctl(8)][sysctl.8] man page.

### Example

```json
"sysctl": {
    "net.ipv4.ip_forward": "1",
    "net.core.somaxconn": "256"
}
```

## <a name="configLinuxSeccomp" />Seccomp

Seccomp provides application sandboxing mechanism in the Linux kernel.
Seccomp configuration allows one to configure actions to take for matched syscalls and furthermore also allows matching on values passed as arguments to syscalls.
For more information about Seccomp, see [Seccomp][seccomp] kernel documentation.
The actions, architectures, and operators are strings that match the definitions in seccomp.h from [libseccomp][] and are translated to corresponding values.

**`seccomp`** (object, OPTIONAL)

The following parameters can be specified to set up seccomp:

* **`defaultAction`** *(string, REQUIRED)* - the default action for seccomp. Allowed values are the same as `syscalls[].action`.
* **`defaultErrnoRet`** *(uint, OPTIONAL)* - the errno return code to use.
    Some actions like `SCMP_ACT_ERRNO` and `SCMP_ACT_TRACE` allow to specify the errno code to return.
    When the action doesn't support an errno, the runtime MUST print and error and fail.
    The default is `EPERM`.
* **`architectures`** *(array of strings, OPTIONAL)* - the architecture used for system calls.
    A valid list of constants as of libseccomp v2.6.0 is shown below.

    * `SCMP_ARCH_X86`
    * `SCMP_ARCH_X86_64`
    * `SCMP_ARCH_X32`
    * `SCMP_ARCH_ARM`
    * `SCMP_ARCH_AARCH64`
    * `SCMP_ARCH_MIPS`
    * `SCMP_ARCH_MIPS64`
    * `SCMP_ARCH_MIPS64N32`
    * `SCMP_ARCH_MIPSEL`
    * `SCMP_ARCH_MIPSEL64`
    * `SCMP_ARCH_MIPSEL64N32`
    * `SCMP_ARCH_PPC`
    * `SCMP_ARCH_PPC64`
    * `SCMP_ARCH_PPC64LE`
    * `SCMP_ARCH_S390`
    * `SCMP_ARCH_S390X`
    * `SCMP_ARCH_PARISC`
    * `SCMP_ARCH_PARISC64`
    * `SCMP_ARCH_RISCV64`
    * `SCMP_ARCH_LOONGARCH64`
    * `SCMP_ARCH_M68K`
    * `SCMP_ARCH_SH`
    * `SCMP_ARCH_SHEB`

* **`flags`** *(array of strings, OPTIONAL)* - list of flags to use with seccomp(2).

    A valid list of constants is shown below.

    * `SECCOMP_FILTER_FLAG_TSYNC`
    * `SECCOMP_FILTER_FLAG_LOG`
    * `SECCOMP_FILTER_FLAG_SPEC_ALLOW`
    * `SECCOMP_FILTER_FLAG_WAIT_KILLABLE_RECV`

* **`listenerPath`** *(string, OPTIONAL)* - specifies the path of UNIX domain socket over which the runtime will send the [container process state](#containerprocessstate) data structure when the `SCMP_ACT_NOTIFY` action is used.
    This socket MUST use `AF_UNIX` domain and `SOCK_STREAM` type.
    The runtime MUST send exactly one [container process state](#containerprocessstate) per connection.
    The connection MUST NOT be reused and it MUST be closed after sending a seccomp state.
    If sending to this socket fails, the runtime MUST [generate an error](runtime.md#errors).
    If the `SCMP_ACT_NOTIFY` action is not used this value is ignored.

    The runtime sends the following file descriptors using `SCM_RIGHTS` and set their names in the `fds` array of the [container process state](#containerprocessstate):

    * **`seccompFd`** (string, REQUIRED) is the seccomp file descriptor returned by the seccomp syscall.

* **`listenerMetadata`** *(string, OPTIONAL)* - specifies an opaque data to pass to the seccomp agent.
    This string will be sent as the `metadata` field in the [container process state](#containerprocessstate).
    This field MUST NOT be set if `listenerPath` is not set.

* **`syscalls`** *(array of objects, OPTIONAL)* - match a syscall in seccomp.
    While this property is OPTIONAL, some values of `defaultAction` are not useful without `syscalls` entries.
    For example, if `defaultAction` is `SCMP_ACT_KILL` and `syscalls` is empty or unset, the kernel will kill the container process on its first syscall.
    Each entry has the following structure:

    * **`names`** *(array of strings, REQUIRED)* - the names of the syscalls.
        `names` MUST contain at least one entry.
    * **`action`** *(string, REQUIRED)* - the action for seccomp rules.
        A valid list of constants as of libseccomp v2.6.0 is shown below.

        * `SCMP_ACT_KILL`
        * `SCMP_ACT_KILL_PROCESS`
        * `SCMP_ACT_KILL_THREAD`
        * `SCMP_ACT_TRAP`
        * `SCMP_ACT_ERRNO`
        * `SCMP_ACT_TRACE`
        * `SCMP_ACT_ALLOW`
        * `SCMP_ACT_LOG`
        * `SCMP_ACT_NOTIFY`

    * **`errnoRet`** *(uint, OPTIONAL)* - the errno return code to use.
        Some actions like `SCMP_ACT_ERRNO` and `SCMP_ACT_TRACE` allow to specify the errno code to return.
        When the action doesn't support an errno, the runtime MUST print and error and fail.
        The default is `EPERM`.

    * **`args`** *(array of objects, OPTIONAL)* - the specific syscall in seccomp.
        Each entry has the following structure:

        * **`index`** *(uint, REQUIRED)* - the index for syscall arguments in seccomp.
        * **`value`** *(uint64, REQUIRED)* - the value for syscall arguments in seccomp.
        * **`valueTwo`** *(uint64, OPTIONAL)* - the value for syscall arguments in seccomp.
        * **`op`** *(string, REQUIRED)* - the operator for syscall arguments in seccomp.
            A valid list of constants as of libseccomp v2.6.0 is shown below.

            * `SCMP_CMP_NE`
            * `SCMP_CMP_LT`
            * `SCMP_CMP_LE`
            * `SCMP_CMP_EQ`
            * `SCMP_CMP_GE`
            * `SCMP_CMP_GT`
            * `SCMP_CMP_MASKED_EQ`

### Example

```json
"seccomp": {
    "defaultAction": "SCMP_ACT_ALLOW",
    "architectures": [
        "SCMP_ARCH_X86",
        "SCMP_ARCH_X32"
    ],
    "syscalls": [
        {
            "names": [
                "getcwd",
                "chmod"
            ],
            "action": "SCMP_ACT_ERRNO"
        }
    ]
}
```

### <a name="containerprocessstate" />The Container Process State

The container process state is a data structure passed via a UNIX socket.
The container runtime MUST send the container process state over the UNIX socket as regular payload serialized in JSON and file descriptors MUST be sent using `SCM_RIGHTS`.
The container runtime MAY use several `sendmsg(2)` calls to send the aforementioned data.
If more than one `sendmsg(2)` is used, the file descriptors MUST be sent only in the first call.

The container process state includes the following properties:

* **`ociVersion`** (string, REQUIRED) is version of the Open Container Initiative Runtime Specification with which the container process state complies.
* **`fds`** (array, OPTIONAL) is a string array containing the names of the file descriptors passed.
    The index of the name in this array corresponds to index of the file descriptors in the `SCM_RIGHTS` array.
* **`pid`** (int, REQUIRED) is the container process ID, as seen by the runtime.
* **`metadata`** (string, OPTIONAL) opaque metadata.
* **`state`** ([state](runtime.md#state), REQUIRED) is the state of the container.

Example sending a single `seccompFd` file descriptor in the `SCM_RIGHTS` array:

```json
{
    "ociVersion": "1.0.2",
    "fds": [
        "seccompFd"
    ],
    "pid": 4422,
    "metadata": "MKNOD=/dev/null,/dev/net/tun;BPF_MAP_TYPES=hash,array",
    "state": {
        "ociVersion": "1.0.2",
        "id": "oci-container1",
        "status": "creating",
        "pid": 4422,
        "bundle": "/containers/redis",
        "annotations": {
            "myKey": "myValue"
        }
    }
}
```

## <a name="configLinuxRootfsMountPropagation" />Rootfs Mount Propagation

**`rootfsPropagation`** (string, OPTIONAL) sets the rootfs's mount propagation.
Its value is either `shared`, `slave`, `private` or `unbindable`.
It's worth noting that a peer group is defined as a group of VFS mounts that propagate events to each other.
A nested container is defined as a container launched inside an existing container.

* **`shared`**: the rootfs mount belongs to a new peer group.
    This means that further mounts (e.g. nested containers) will also belong to that peer group and will propagate events to the rootfs.
    Note this does not mean that it's shared with the host.
* **`slave`**: the rootfs mount receives propagation events from the host (e.g. if something is mounted on the host it will also appear in the container) but not the other way around.
* **`private`**: the rootfs mount doesn't receive mount propagation events from the host and further mounts in nested containers will be isolated from the host and from the rootfs (even if the nested container `rootfsPropagation` option is shared).
* **`unbindable`**: the rootfs mount is a private mount that cannot be bind-mounted.

The [Shared Subtrees][sharedsubtree] article in the kernel documentation has more information about mount propagation.

### Example

```json
"rootfsPropagation": "slave",
```

## <a name="configLinuxMaskedPaths" />Masked Paths

**`maskedPaths`** (array of strings, OPTIONAL) will mask over the provided paths inside the container so that they cannot be read.
The values MUST be absolute paths in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container_namespace).

### Example

```json
"maskedPaths": [
    "/proc/kcore"
]
```

## <a name="configLinuxReadonlyPaths" />Readonly Paths

**`readonlyPaths`** (array of strings, OPTIONAL) will set the provided paths as readonly inside the container.
The values MUST be absolute paths in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).

### Example

```json
"readonlyPaths": [
    "/proc/sys"
]
```

## <a name="configLinuxMountLabel" />Mount Label

**`mountLabel`** (string, OPTIONAL) will set the Selinux context for the mounts in the container.

### Example

```json
"mountLabel": "system_u:object_r:svirt_sandbox_file_t:s0:c715,c811"
```

## <a name="configLinuxPersonality" />Personality

**`personality`** (object, OPTIONAL) sets the Linux execution personality. For more information
see the [personality][personality.2] syscall documentation. As most of the options are
obsolete and rarely used, and some reduce security, the currently supported set is a small
subset of the available options.

* **`domain`** *(string, REQUIRED)* - the execution domain.
    The valid list of constants is shown below. `LINUX32` will set the `uname` system call to show
    a 32 bit CPU type, such as `i686`.

    * `LINUX`
    * `LINUX32`

* **`flags`** *(array of strings, OPTIONAL)* - the additional flags to apply.
    Currently no flag values are supported.


[cgroup-v1]: https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt
[cgroup-v1-blkio]: https://www.kernel.org/doc/Documentation/cgroup-v1/blkio-controller.txt
[cgroup-v1-cpusets]: https://www.kernel.org/doc/Documentation/cgroup-v1/cpusets.txt
[cgroup-v1-devices]: https://www.kernel.org/doc/Documentation/cgroup-v1/devices.txt
[cgroup-v1-hugetlb]: https://www.kernel.org/doc/Documentation/cgroup-v1/hugetlb.txt
[cgroup-v1-memory]: https://www.kernel.org/doc/Documentation/cgroup-v1/memory.txt
[cgroup-v1-net-cls]: https://www.kernel.org/doc/Documentation/cgroup-v1/net_cls.txt
[cgroup-v1-net-prio]: https://www.kernel.org/doc/Documentation/cgroup-v1/net_prio.txt
[cgroup-v1-pids]: https://www.kernel.org/doc/Documentation/cgroup-v1/pids.txt
[cgroup-v1-rdma]: https://www.kernel.org/doc/Documentation/cgroup-v1/rdma.txt
[cgroup-v2]: https://www.kernel.org/doc/Documentation/cgroup-v2.txt
[cgroup-v2-io]: https://docs.kernel.org/admin-guide/cgroup-v2.html#io
[devices]: https://www.kernel.org/doc/Documentation/admin-guide/devices.txt
[devpts]: https://www.kernel.org/doc/Documentation/filesystems/devpts.txt
[file]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_164
[libseccomp]: https://github.com/seccomp/libseccomp
[proc]: https://www.kernel.org/doc/Documentation/filesystems/proc.txt
[seccomp]: https://www.kernel.org/doc/Documentation/prctl/seccomp_filter.txt
[sharedsubtree]: https://www.kernel.org/doc/Documentation/filesystems/sharedsubtree.txt
[sysfs]: https://www.kernel.org/doc/Documentation/filesystems/sysfs.txt
[tmpfs]: https://www.kernel.org/doc/Documentation/filesystems/tmpfs.txt

[full.4]: https://man7.org/linux/man-pages/man4/full.4.html
[set_mempolicy.2]: https://man7.org/linux/man-pages/man2/set_mempolicy.2.html
[mknod.1]: https://man7.org/linux/man-pages/man1/mknod.1.html
[mknod.2]: https://man7.org/linux/man-pages/man2/mknod.2.html
[namespaces.7_2]: https://man7.org/linux/man-pages/man7/namespaces.7.html
[net_device]: https://docs.kernel.org/networking/netdevices.html
[net_namespaces.7]: https://man7.org/linux/man-pages/man7/network_namespaces.7.html
[predictable-network-interfaces-names]: https://systemd.io/PREDICTABLE_INTERFACE_NAMES
[rfc3549]: https://www.ietf.org/rfc/rfc3549.txt
[null.4]: https://man7.org/linux/man-pages/man4/null.4.html
[personality.2]: https://man7.org/linux/man-pages/man2/personality.2.html
[pts.4]: https://man7.org/linux/man-pages/man4/pts.4.html
[random.4]: https://man7.org/linux/man-pages/man4/random.4.html
[sysctl.8]: https://man7.org/linux/man-pages/man8/sysctl.8.html
[tty.4]: https://man7.org/linux/man-pages/man4/tty.4.html
[zero.4]: https://man7.org/linux/man-pages/man4/zero.4.html
[user-namespaces]: https://man7.org/linux/man-pages/man7/user_namespaces.7.html
[intel-rdt-cat-kernel-interface]: https://www.kernel.org/doc/Documentation/x86/intel_rdt_ui.txt
[time_namespaces.7]: https://man7.org/linux/man-pages/man7/time_namespaces.7.html
```

## File: `config-solaris.md`
```markdown
# <a name="solarisApplicationContainerConfiguration" />Solaris Application Container Configuration

Solaris application containers can be configured using the following properties, all of the below properties have mappings to properties specified under [zonecfg(1M)][zonecfg.1m_2] man page, except milestone.

## <a name="configSolarisMilestone" />milestone
The SMF(Service Management Facility) FMRI which should go to "online" state before we start the desired process within the container.

**`milestone`** *(string, OPTIONAL)*

### Example
```json
"milestone": "svc:/milestone/container:default"
```

## <a name="configSolarisLimitpriv" />limitpriv
The maximum set of privileges any process in this container can obtain.
The property should consist of a comma-separated privilege set specification as described in [priv_str_to_set(3C)][priv-str-to-set.3c] man page for the respective release of Solaris.

**`limitpriv`** *(string, OPTIONAL)*

### Example
```json
"limitpriv": "default"
```

## <a name="configSolarisMaxShmMemory" />maxShmMemory
The maximum amount of shared memory allowed for this application container.
A scale (K, M, G, T) can be applied to the value for each of these numbers (for example, 1M is one megabyte).
Mapped to `max-shm-memory` in [zonecfg(1M)][zonecfg.1m_2] man page.

**`maxShmMemory`** *(string, OPTIONAL)*

### Example
```json
"maxShmMemory": "512m"
```

## <a name="configSolarisCappedCpu" />cappedCPU
Sets a limit on the amount of CPU time that can be used by a container.
The unit used translates to the percentage of a single CPU that can be used by all user threads in a container, expressed as a fraction (for example, .75) or a mixed number (whole number and fraction, for example, 1.25).
An ncpu value of 1 means 100% of a CPU, a value of 1.25 means 125%, .75 mean 75%, and so forth.
When projects within a capped container have their own caps, the minimum value takes precedence.
cappedCPU is mapped to `capped-cpu` in [zonecfg(1M)][zonecfg.1m_2] man page.

* **`ncpus`** *(string, OPTIONAL)*

### Example
```json
"cappedCPU": {
    "ncpus": "8"
}
```

## <a name="configSolarisCappedMemory" />cappedMemory
The physical and swap caps on the memory that can be used by this application container.
A scale (K, M, G, T) can be applied to the value for each of these numbers (for example, 1M is one megabyte).
cappedMemory is mapped to `capped-memory` in [zonecfg(1M)][zonecfg.1m_2] man page.

* **`physical`** *(string, OPTIONAL)*
* **`swap`** *(string, OPTIONAL)*

### Example
```json
"cappedMemory": {
    "physical": "512m",
    "swap": "512m"
}
```

## <a name="configSolarisNetwork" />Network

### <a name="configSolarisAutomaticNetwork" />Automatic Network (anet)
anet is specified as an array that is used to set up networking for Solaris application containers.
The anet resource represents the automatic creation of a network resource for an application container.
The zones administration daemon, zoneadmd, is the primary process for managing the container's virtual platform.
One of the daemon's responsibilities is creation and teardown of the networks for the container.
For more information on the daemon see the [zoneadmd(1M)][zoneadmd.1m] man page.
When such a container is started, a temporary VNIC(Virtual NIC) is automatically created for the container.
The VNIC is deleted when the container is torn down.
The following properties can be used to set up automatic networks.
For additional information on properties, check the [zonecfg(1M)][zonecfg.1m_2] man page for the respective release of Solaris.

* **`linkname`** *(string, OPTIONAL)* Specify a name for the automatically created VNIC datalink.
* **`lowerLink`** *(string, OPTIONAL)* Specify the link over which the VNIC will be created.
Mapped to `lower-link` in the [zonecfg(1M)][zonecfg.1m_2] man page.
* **`allowedAddress`** *(string, OPTIONAL)* The set of IP addresses that the container can use might be constrained by specifying the `allowedAddress` property.
    If `allowedAddress` has not been specified, then they can use any IP address on the associated physical interface for the network resource.
    Otherwise, when `allowedAddress` is specified, the container cannot use IP addresses that are not in the `allowedAddress` list for the physical address.
    Mapped to `allowed-address` in the [zonecfg(1M)][zonecfg.1m_2] man page.
* **`configureAllowedAddress`** *(string, OPTIONAL)* If `configureAllowedAddress` is set to true, the addresses specified by `allowedAddress` are automatically configured on the interface each time the container starts.
    When it is set to false, the `allowedAddress` will not be configured on container start.
    Mapped to `configure-allowed-address` in the [zonecfg(1M)][zonecfg.1m_2] man page.
* **`defrouter`** *(string, OPTIONAL)* The value for the OPTIONAL default router.
* **`macAddress`** *(string, OPTIONAL)* Set the VNIC's MAC addresses based on the specified value or keyword.
    If not a keyword, it is interpreted as a unicast MAC address.
    For a list of the supported keywords please refer to the [zonecfg(1M)][zonecfg.1m_2] man page of the respective Solaris release.
    Mapped to `mac-address` in the [zonecfg(1M)][zonecfg.1m_2] man page.
* **`linkProtection`** *(string, OPTIONAL)* Enables one or more types of link protection using comma-separated values.
    See the protection property in dladm(8) for supported values in respective release of Solaris.
    Mapped to `link-protection` in the [zonecfg(1M)][zonecfg.1m_2] man page.

#### Example
```json
"anet": [
    {
        "allowedAddress": "172.17.0.2/16",
        "configureAllowedAddress": "true",
        "defrouter": "172.17.0.1/16",
        "linkProtection": "mac-nospoof, ip-nospoof",
        "linkname": "net0",
        "lowerLink": "net2",
        "macAddress": "02:42:f8:52:c7:16"
    }
]
```


[priv-str-to-set.3c]: https://docs.oracle.com/cd/E86824_01/html/E54766/priv-str-to-set-3c.html
[zoneadmd.1m]: https://docs.oracle.com/cd/E86824_01/html/E54764/zoneadmd-1m.html
[zonecfg.1m_2]: https://docs.oracle.com/cd/E86824_01/html/E54764/zonecfg-1m.html
```

## File: `config-vm.md`
```markdown
# <a name="VirtualMachineSpecificContainerConfiguration" /> Virtual-machine-specific Container Configuration

This section describes the schema for the [virtual-machine-specific section](config.md#platform-specific-configuration) of the [container configuration](config.md).
The virtual-machine container specification provides additional configuration for the hypervisor, kernel, and image.

## <a name="HypervisorObject" /> Hypervisor Object

**`hypervisor`** (object, OPTIONAL) specifies details of the hypervisor that manages the container virtual machine.
* **`path`** (string, REQUIRED) path to the hypervisor binary that manages the container virtual machine.
    This value MUST be an absolute path in the [runtime mount namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
* **`parameters`** (array of strings, OPTIONAL) specifies an array of parameters to pass to the hypervisor.

### Example

```json
    "hypervisor": {
        "path": "/path/to/vmm",
        "parameters": ["opts1=foo", "opts2=bar"]
    }
```

## <a name="KernelObject" /> Kernel Object

**`kernel`** (object, REQUIRED) specifies details of the kernel to boot the container virtual machine with.
* **`path`** (string, REQUIRED) path to the kernel used to boot the container virtual machine.
    This value MUST be an absolute path in the [runtime mount namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
* **`parameters`** (array of strings, OPTIONAL) specifies an array of parameters to pass to the kernel.
* **`initrd`** (string, OPTIONAL) path to an initial ramdisk to be used by the container virtual machine.
    This value MUST be an absolute path in the [runtime mount namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).

### Example

```json
    "kernel": {
        "path": "/path/to/vmlinuz",
        "parameters": ["foo=bar", "hello world"],
        "initrd": "/path/to/initrd.img"
    }
```

## <a name="ImageObject" /> Image Object

**`image`** (object, OPTIONAL) specifies details of the image that contains the root filesystem for the container virtual machine.
* **`path`** (string, REQUIRED) path to the container virtual machine root image.
    This value MUST be an absolute path in the [runtime mount namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
* **`format`** (string, REQUIRED) format of the container virtual machine root image. Commonly supported formats are:
    * **`raw`** [raw disk image format][raw-image-format]. Unset values for `format` will default to that format.
    * **`qcow2`** [QEMU image format][qcow2-image-format].
    * **`vdi`** [VirtualBox 1.1 compatible image format][vdi-image-format].
    * **`vmdk`** [VMware compatible image format][vmdk-image-format].
    * **`vhd`** [Virtual Hard Disk image format][vhd-image-format].

This image contains the root filesystem that the virtual machine **`kernel`** will boot into, not to be confused with the container root filesystem itself. The latter, as specified by **`path`** from the [Root Configuration](config.md#Root-Configuration) section, will be mounted inside the virtual machine at a location chosen by the virtual-machine-based runtime.

### Example

```json
    "image": {
        "path": "/path/to/vm/rootfs.img",
	"format": "raw"
    }
```

## <a name="HwConfigObject" /> HWConfig Object

**`hwConfig`** (object OPTIONAL) Specifies the hardware configuration that should be passed to the VM.
* **`deviceTree`** (string OPTIONAL) Path to the container device-tree file that should be passed to the VM.
* **`vcpus`** (int OPTIONAL) Number of virtual cpus for the VM.
* **`memory`** (int OPTIONAL) Maximum memory in bytes allocated to the VM.
* **`dtdevs`** (array OPTIONAL) Host device tree nodes to passthrough to the VM, see [Xen Config][xl-config-format] for the details.
* **`iomems`** (array OPTIONAL) Allow auto-translated domains to access specific hardware I/O memory pages, see [Xen Config][xl-config-format].
    * **`firstGFN`** (int OPTIONAL) Guest Frame Number to map the iomem range.
        If GFN is not specified, the mapping will be done to the same Frame Number as was provided in firstMFN, see [Xen Config][xl-config-format] for the details.
    * **`firstMFN`** (int REQUIRED) Physical page number of iomem regions, see [Xen Config][xl-config-format] for the details.
    * **`nrMFNs`** (int REQUIRED) Number of pages to be mapped, see [Xen Config][xl-config-format] for the details.
* **`irqs`** (array OPTIONAL) Allows VM to access specific physical IRQs, see [Xen Config][xl-config-format] for the details.

This hwConfig object contains the description of the hardware that can be safely passed through to the VM. Where **`deviceTree`** is the path to the device-tree blob, which contains description of the isolated hardware and paravirtualized hardware that should be used by VM. **`dtdevs`**, **`iomems`** and **`irqs`** parameters describing the minimal set of the parameters, needed for VM to access the hardware.

### Example

```json
    "hwConfig": {
        "deviceTree": "/path/to/vm/devicetree.dtb",
        "vcpus": 1,
        "memory": 4194304,
        "dtdevs": [
            "path/to/dev1_node",
            "path/to/dev2_node"
        ],
        "iomems": [
            {
                "firstMFN": 12288,
                "nrMFNs": 1
            },
            {
                "firstGFN": 12544,
                "firstMFN": 33024,
                "nrMFNs": 2
            }
        ],
        "irqs": [
            11,
            22
        ]
    }
```

[raw-image-format]: https://en.wikipedia.org/wiki/IMG_(file_format)
[qcow2-image-format]: https://git.qemu.org/?p=qemu.git;a=blob_plain;f=docs/interop/qcow2.txt;hb=HEAD
[vdi-image-format]: https://forensicswiki.org/wiki/Virtual_Disk_Image_(VDI)
[vmdk-image-format]: http://www.vmware.com/app/vmdk/?src=vmdk
[vhd-image-format]: https://github.com/libyal/libvhdi/blob/master/documentation/Virtual%20Hard%20Disk%20(VHD)%20image%20format.asciidoc
[xl-config-format]: https://xenbits.xen.org/docs/4.10-testing/man/xl.cfg.5.html
```

## File: `config-windows.md`
```markdown
# <a name="windowsSpecificContainerConfiguration" />Windows-specific Container Configuration

This document describes the schema for the [Windows-specific section](config.md#platform-specific-configuration) of the [container configuration](config.md).
The Windows container specification uses APIs provided by the Windows Host Compute Service (HCS) to fulfill the spec.

## <a name="configWindowsLayerFolders" />LayerFolders

**`layerFolders`** (array of strings, REQUIRED) specifies a list of layer folders the container image relies on. The list is ordered from topmost layer to base layer with the last entry being the scratch.
`layerFolders` MUST contain at least one entry.

### Example

```json
"windows": {
    "layerFolders": [
        "C:\\Layers\\layer2",
        "C:\\Layers\\layer1",
        "C:\\Layers\\layer-base",
        "C:\\scratch",
    ]
}
```

## <a name="configWindowsDevices" />Devices

**`devices`** (array of objects, OPTIONAL) lists devices that MUST be available in the container.

Each entry has the following structure:

* **`id`** *(string, REQUIRED)* - specifies the device which the runtime MUST make available in the container.
* **`idType`** *(string, REQUIRED)* - tells the runtime how to interpret `id`. Today, Windows only supports a value of `class`, which identifies `id` as a [device interface class GUID][interfaceGUID].

[interfaceGUID]: https://docs.microsoft.com/en-us/windows-hardware/drivers/install/overview-of-device-interface-classes

### Example

```json
"windows": {
    "devices": [
        {
            "id": "24E552D7-6523-47F7-A647-D3465BF1F5CA",
            "idType": "class"
        },
        {
            "id": "5175d334-c371-4806-b3ba-71fd53c9258d",
            "idType": "class"
        }
    ]
}
```

## <a name="configWindowsResources" />Resources

You can configure a container's resource limits via the OPTIONAL `resources` field of the Windows configuration.

### <a name="configWindowsMemory" />Memory

`memory` is an OPTIONAL configuration for the container's memory usage.

The following parameters can be specified:

* **`limit`** *(uint64, OPTIONAL)* - sets limit of memory usage in bytes.

#### Example

```json
"windows": {
    "resources": {
        "memory": {
            "limit": 2097152
        }
    }
}
```

### <a name="configWindowsCpu" />CPU

`cpu` is an OPTIONAL configuration for the container's CPU usage.

The following parameters can be specified (mutually exclusive):

* **`count`** *(uint64, OPTIONAL)* - specifies the number of CPUs available to the container. It represents the fraction of the configured processor `count` in a container in relation to the processors available in the host. The fraction ultimately determines the portion of processor cycles that the threads in a container can use during each scheduling interval, as the number of cycles per 10,000 cycles.
* **`shares`** *(uint16, OPTIONAL)* - limits the share of processor time given to the container relative to other workloads on the processor. The processor `shares` (`weight` at the platform level) is a value between 0 and 10,000.
* **`maximum`** *(uint16, OPTIONAL)* - determines the portion of processor cycles that the threads in a container can use during each scheduling interval, as the number of cycles per 10,000 cycles. Set processor `maximum` to a percentage times 100.
* **`affinity`** *(array of objects, OPTIONAL)* - specifies the set of CPU to affinitize for this container.

  Each entry has the following structure:

  Ref: https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/miniport/ns-miniport-_group_affinity

  * **`mask`** *(uint64, REQUIRED)* - specifies the CPU mask relative to this CPU group.
  * **`group`** *(uint32, REQUIRED)* - specifies the processor group this mask refers to, as returned by GetLogicalProcessorInformationEx.

Ref: https://docs.microsoft.com/en-us/virtualization/api/hcs/schemareference#Container_Processor

#### Example

```json
"windows": {
    "resources": {
        "cpu": {
            "maximum": 5000
        }
    }
}
```

### <a name="configWindowsStorage" />Storage

`storage` is an OPTIONAL configuration for the container's storage usage.

The following parameters can be specified:

* **`iops`** *(uint64, OPTIONAL)* - specifies the maximum IO operations per second for the system drive of the container.
* **`bps`** *(uint64, OPTIONAL)* - specifies the maximum bytes per second for the system drive of the container.
* **`sandboxSize`** *(uint64, OPTIONAL)* - specifies the minimum size of the system drive in bytes.

#### Example

```json
"windows": {
    "resources": {
        "storage": {
            "iops": 50
        }
    }
}
```

## <a name="configWindowsNetwork" />Network

You can configure a container's networking options via the OPTIONAL `network` field of the Windows configuration.

The following parameters can be specified:

* **`endpointList`** *(array of strings, OPTIONAL)* - list of HNS (Host Network Service) endpoints that the container should connect to.
* **`allowUnqualifiedDNSQuery`** *(bool, OPTIONAL)* - specifies if unqualified DNS name resolution is allowed.
* **`DNSSearchList`** *(array of strings, OPTIONAL)* - comma separated list of DNS suffixes to use for name resolution.
* **`networkSharedContainerName`** *(string, OPTIONAL)* - name (ID) of the container that we will share with the network stack.
* **`networkNamespace`** *(string, OPTIONAL)* - name (ID) of the network namespace that will be used for the container. If a network namespace is specified no other parameter must be specified.

### Example

```json
"windows": {
    "network": {
        "endpointList": [
            "7a010682-17e0-4455-a838-02e5d9655fe6"
        ],
        "allowUnqualifiedDNSQuery": true,
        "DNSSearchList": [
            "a.com",
            "b.com"
        ],
        "networkSharedContainerName": "containerName",
        "networkNamespace": "168f3daf-efc6-4377-b20a-2c86764ba892"
    }
}
```

## <a name="configWindowsCredentialSpec" />Credential Spec

You can configure a container's group Managed Service Account (gMSA) via the OPTIONAL `credentialSpec` field of the Windows configuration.
The `credentialSpec` is a JSON object whose properties are implementation-defined.
For more information about gMSAs, see [Active Directory Service Accounts for Windows Containers][gMSAOverview].
For more information about tooling to generate a gMSA, see [Deployment Overview][gMSATooling].


[gMSAOverview]: https://aka.ms/windowscontainers/manage-serviceaccounts
[gMSATooling]: https://aka.ms/windowscontainers/credentialspec-tools

## <a name="configWindowsServicing" />Servicing

When a container terminates, the Host Compute Service indicates if a Windows update servicing operation is pending.
You can indicate that a container should be started in a mode to apply pending servicing operations via the OPTIONAL `servicing` field of the Windows configuration.

### Example

```json
"windows": {
    "servicing": true
}
```

## <a name="configWindowsIgnoreFlushesDuringBoot" />IgnoreFlushesDuringBoot

You can indicate that a container should be started in a mode where disk flushes are not performed during container boot via the OPTIONAL `ignoreFlushesDuringBoot` field of the Windows configuration.

### Example

```json
"windows": {
    "ignoreFlushesDuringBoot": true
}
```

## <a name="configWindowsHyperV" />HyperV

`hyperv` is an OPTIONAL field of the Windows configuration.
If present, the container MUST be run with Hyper-V isolation.
If omitted, the container MUST be run as a Windows Server container.

The following parameters can be specified:

* **`utilityVMPath`** *(string, OPTIONAL)* - specifies the path to the image used for the utility VM.
    This would be specified if using a base image which does not contain a utility VM image.
    If not supplied, the runtime will search the container filesystem layers from the bottom-most layer upwards, until it locates "UtilityVM", and default to that path.

### Example

```json
"windows": {
    "hyperv": {
        "utilityVMPath": "C:\\path\\to\\utilityvm"
    }
}
```
```

## File: `config-zos.md`
```markdown
# <a name="ZOSContainerConfiguration" />z/OS Container Configuration

This document describes the schema for the [z/OS-specific section](config.md#platform-specific-configuration) of the [container configuration](config.md).
The z/OS container specification uses z/OS UNIX kernel features like namespaces and filesystem jails to fulfill the spec.

Applications expecting a z/OS environment will very likely expect these file paths to be set up correctly.

The following filesystems SHOULD be made available in each container's filesystem:

| Path     | Type   |
| -------- | ------ |
| /proc    | [proc][] |

## <a name="configZOSNamespaces" />Namespaces

A namespace wraps a global system resource in an abstraction that makes it appear to the processes within the namespace that they have their own isolated instance of the global resource.
Changes to the global resource are visible to other processes that are members of the namespace, but are invisible to other processes.
For more information, see https://www.ibm.com/docs/zos/latest?topic=planning-namespaces-zos-unix.

Namespaces are specified as an array of entries inside the `namespaces` root field.
The following parameters can be specified to set up namespaces:

* **`type`** *(string, REQUIRED)* - namespace type. The following namespace types SHOULD be supported:
    * **`pid`** processes inside the container will only be able to see other processes inside the same container or inside the same pid namespace.
    * **`mount`** the container will have an isolated mount table.
    * **`ipc`** processes inside the container will only be able to communicate to other processes inside the same container via system level IPC.
    * **`uts`** the container will be able to have its own hostname and domain name.
* **`path`** *(string, OPTIONAL)* - namespace file.
    This value MUST be an absolute path in the [runtime mount namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
    The runtime MUST place the container process in the namespace associated with that `path`.
    The runtime MUST [generate an error](runtime.md#errors) if `path` is not associated with a namespace of type `type`.

    If `path` is not specified, the runtime MUST create a new [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace) of type `type`.

If a namespace type is not specified in the `namespaces` array, the container MUST inherit the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace) of that type.
If a `namespaces` field contains duplicated namespaces with same `type`, the runtime MUST [generate an error](runtime.md#errors).

### Example

```json
"namespaces": [
    {
        "type": "pid",
        "path": "/proc/1234/ns/pid"
    },
    {
        "type": "mount"
    },
    {
        "type": "ipc"
    },
    {
        "type": "uts"
    }
]
```
```

## File: `config.md`
```markdown
# <a name="configuration" />Configuration

This configuration file contains metadata necessary to implement [standard operations](runtime.md#operations) against the container.
This includes the process to run, environment variables to inject, sandboxing features to use, etc.

The canonical schema is defined in this document, but there is a JSON Schema in [`schema/config-schema.json`](schema/config-schema.json) and Go bindings in [`specs-go/config.go`](specs-go/config.go).
[Platform](spec.md#platforms)-specific configuration schema are defined in the [platform-specific documents](#platform-specific-configuration) linked below.
For properties that are only defined for some [platforms](spec.md#platforms), the Go property has a `platform` tag listing those protocols (e.g. `platform:"linux,solaris"`).

Below is a detailed description of each field defined in the configuration format and valid values are specified.
Platform-specific fields are identified as such.
For all platform-specific configuration values, the scope defined below in the [Platform-specific configuration](#platform-specific-configuration) section applies.


## <a name="configSpecificationVersion" />Specification version

* **`ociVersion`** (string, REQUIRED) MUST be in [SemVer v2.0.0][semver-v2.0.0] format and specifies the version of the Open Container Initiative Runtime Specification with which the bundle complies.
    The Open Container Initiative Runtime Specification follows semantic versioning and retains forward and backward compatibility within major versions.
    For example, if a configuration is compliant with version 1.1 of this specification, it is compatible with all runtimes that support any 1.1 or later release of this specification, but is not compatible with a runtime that supports 1.0 and not 1.1.

### Example

```json
"ociVersion": "0.1.0"
```

## <a name="configRoot" />Root

**`root`** (object, OPTIONAL) specifies the container's root filesystem.
On Windows, for Windows Server Containers, this field is REQUIRED.
For [Hyper-V Containers](config-windows.md#hyperv), this field MUST NOT be set.

On all other platforms, this field is REQUIRED.

* **`path`** (string, REQUIRED) Specifies the path to the root filesystem for the container.
    * On Windows, `path` MUST be a [volume GUID path][naming-a-volume].
    * On POSIX platforms, `path` is either an absolute path or a relative path to the bundle.
        For example, with a bundle at `/to/bundle` and a root filesystem at `/to/bundle/rootfs`, the `path` value can be either `/to/bundle/rootfs` or `rootfs`.
        The value SHOULD be the conventional `rootfs`.

    A directory MUST exist at the path declared by the field.

* **`readonly`** (bool, OPTIONAL) If true then the root filesystem MUST be read-only inside the container, defaults to false.
    * On Windows, this field MUST be omitted or false.

### Example (POSIX platforms)

```json
"root": {
    "path": "rootfs",
    "readonly": true
}
```

### Example (Windows)

```json
"root": {
    "path": "\\\\?\\Volume{ec84d99e-3f02-11e7-ac6c-00155d7682cf}\\"
}
```

## <a name="configMounts" />Mounts

**`mounts`** (array of objects, OPTIONAL) specifies additional mounts beyond [`root`](#root).
The runtime MUST mount entries in the listed order.
For Linux, the parameters are as documented in [mount(2)][mount.2] system call man page.
For Solaris, the mount entry corresponds to the 'fs' resource in the [zonecfg(1M)][zonecfg.1m] man page.

* **`destination`** (string, REQUIRED) Destination of mount point: path inside container.
    * Linux: This value SHOULD be an absolute path.
      For compatibility with old tools and configurations, it MAY be a relative path, in which case it MUST be interpreted as relative to "/".
      Relative paths are **deprecated**.
    * Windows: This value MUST be an absolute path.
      One mount destination MUST NOT be nested within another mount (e.g., c:\\foo and c:\\foo\\bar).
    * Solaris: This value MUST be an absolute path.
      Corresponds to "dir" of the fs resource in [zonecfg(1M)][zonecfg.1m].
    * For all other platforms: This value MUST be an absolute path.
* **`source`** (string, OPTIONAL) A device name, but can also be a file or directory name for bind mounts or a dummy.
    Path values for bind mounts are either absolute or relative to the bundle.
    A mount is a bind mount if it has either `bind` or `rbind` in the options.
    * Windows: a local directory on the filesystem of the container host. UNC paths and mapped drives are not supported.
    * Solaris: corresponds to "special" of the fs resource in [zonecfg(1M)][zonecfg.1m].
* **`options`** (array of strings, OPTIONAL) Mount options of the filesystem to be used.
    * Linux: See [Linux mount options](#configLinuxMountOptions) below.
    * Solaris: corresponds to "options" of the fs resource in [zonecfg(1M)][zonecfg.1m].
    * Windows: runtimes MUST support `ro`, mounting the filesystem read-only when `ro` is given.

### <a name="configLinuxMountOptions" />Linux mount options

Runtimes MUST/SHOULD/MAY implement the following option strings for Linux:

 Option name      | Requirement | Description
------------------|-------------|-----------------------------------------------------
 `async`          | MUST        | [^1]
 `atime`          | MUST        | [^1]
 `bind`           | MUST        | Bind mount [^2]
 `defaults`       | MUST        | [^1]
 `dev`            | MUST        | [^1]
 `diratime`       | MUST        | [^1]
 `dirsync`        | MUST        | [^1]
 `exec`           | MUST        | [^1]
 `iversion`       | MUST        | [^1]
 `lazytime`       | MUST        | [^1]
 `loud`           | MUST        | [^1]
 `mand`           | MAY         | [^1] (Deprecated in kernel 5.15, util-linux 2.38)
 `noatime`        | MUST        | [^1]
 `nodev`          | MUST        | [^1]
 `nodiratime`     | MUST        | [^1]
 `noexec`         | MUST        | [^1]
 `noiversion`     | MUST        | [^1]
 `nolazytime`     | MUST        | [^1]
 `nomand`         | MAY         | [^1]
 `norelatime`     | MUST        | [^1]
 `nostrictatime`  | MUST        | [^1]
 `nosuid`         | MUST        | [^1]
 `nosymfollow`    | SHOULD      | [^1] (Introduced in kernel 5.10, util-linux 2.38)
 `private`        | MUST        | Bind mount propagation [^2]
 `ratime`         | SHOULD      | Recursive `atime` [^3]
 `rbind`          | MUST        | Recursive bind mount [^2]
 `rdev`           | SHOULD      | Recursive `dev` [^3]
 `rdiratime`      | SHOULD      | Recursive `diratime` [^3]
 `relatime`       | MUST        | [^1]
 `remount`        | MUST        | [^1]
 `rexec`          | SHOULD      | Recursive `dev` [^3]
 `rnoatime`       | SHOULD      | Recursive `noatime` [^3]
 `rnodiratime`    | SHOULD      | Recursive `nodiratime` [^3]
 `rnoexec`        | SHOULD      | Recursive `noexec` [^3]
 `rnorelatime`    | SHOULD      | Recursive `norelatime` [^3]
 `rnostrictatime` | SHOULD      | Recursive `nostrictatime` [^3]
 `rnosuid`        | SHOULD      | Recursive `nosuid` [^3]
 `rnosymfollow`   | SHOULD      | Recursive `nosymfollow` [^3]
 `ro`             | MUST        | [^1]
 `rprivate`       | MUST        | Bind mount propagation [^2]
 `rrelatime  `    | SHOULD      | Recursive `relatime` [^3]
 `rro`            | SHOULD      | Recursive `ro` [^3]
 `rrw`            | SHOULD      | Recursive `rw` [^3]
 `rshared`        | MUST        | Bind mount propagation [^2]
 `rslave`         | MUST        | Bind mount propagation [^2]
 `rstrictatime`   | SHOULD      | Recursive `strictatime` [^3]
 `rsuid`          | SHOULD      | Recursive `suid` [^3]
 `rsymfollow`     | SHOULD      | Recursive `symfollow` [^3]
 `runbindable`    | MUST        | Bind mount propagation [^2]
 `rw`             | MUST        | [^1]
 `shared`         | MUST        | [^1]
 `silent`         | MUST        | [^1]
 `slave`          | MUST        | Bind mount propagation [^2]
 `strictatime`    | MUST        | [^1]
 `suid`           | MUST        | [^1]
 `symfollow`      | SHOULD      | Opposite of `nosymfollow`
 `sync`           | MUST        | [^1]
 `tmpcopyup`      | MAY         | copy up the contents to a tmpfs
 `unbindable`     | MUST        | Bind mount propagation [^2]
 `idmap`          | SHOULD      | Indicates that the mount MUST have an idmapping applied. This option SHOULD NOT be passed to the underlying [`mount(2)`][mount.2] call. If `uidMappings` or `gidMappings` are specified for the mount, the runtime MUST use those values for the mount's mapping. If they are not specified, the runtime MAY use the container's user namespace mapping, otherwise an [error MUST be returned](runtime.md#errors).  If there are no `uidMappings` and `gidMappings` specified and the container isn't using user namespaces, an [error MUST be returned](runtime.md#errors). This SHOULD be implemented using [`mount_setattr(MOUNT_ATTR_IDMAP)`][mount_setattr.2], available since Linux 5.12.
 `ridmap`         | SHOULD      | Indicates that the mount MUST have an idmapping applied, and the mapping is applied recursively [^3]. This option SHOULD NOT be passed to the underlying [`mount(2)`][mount.2] call. If `uidMappings` or `gidMappings` are specified for the mount, the runtime MUST use those values for the mount's mapping. If they are not specified, the runtime MAY use the container's user namespace mapping, otherwise an [error MUST be returned](runtime.md#errors).  If there are no `uidMappings` and `gidMappings` specified and the container isn't using user namespaces, an [error MUST be returned](runtime.md#errors). This SHOULD be implemented using [`mount_setattr(MOUNT_ATTR_IDMAP)`][mount_setattr.2], available since Linux 5.12.

[^1]: Corresponds to [`mount(8)` (filesystem-independent)][mount.8-filesystem-independent].
[^2]: Corresponds to [bind mounts and shared subtrees][mount-bind].
[^3]: These `AT_RECURSIVE` options need kernel 5.12 or later. See [`mount_setattr(2)`][mount_setattr.2]

The "MUST" options correspond to [`mount(8)`][mount.8].

Runtimes MAY also implement custom option strings that are not listed in the table above.
If a custom option string is already recognized by [`mount(8)`][mount.8], the runtime SHOULD follow the behavior of [`mount(8)`][mount.8].

Runtimes SHOULD treat unknown options as [filesystem-specific ones][mount.8-filesystem-specific])
and pass those as a comma-separated string to the fifth (`const void *data`) argument of [`mount(2)`][mount.2].

### Example (Windows)

```json
"mounts": [
    {
        "destination": "C:\\folder-inside-container",
        "source": "C:\\folder-on-host",
        "options": ["ro"]
    }
]
```

### <a name="configPOSIXMounts" />POSIX-platform Mounts

For POSIX platforms the `mounts` structure has the following fields:

* **`type`** (string, OPTIONAL) The type of the filesystem to be mounted.
    * Linux: filesystem types supported by the kernel as listed in */proc/filesystems* (e.g., "minix", "ext2", "ext3", "jfs", "xfs", "reiserfs", "msdos", "proc", "nfs", "iso9660"). For bind mounts (when `options` include either `bind` or `rbind`), the type is a dummy, often "none" (not listed in */proc/filesystems*).
    * Solaris: corresponds to "type" of the fs resource in [zonecfg(1M)][zonecfg.1m].
* **`uidMappings`** (array of type LinuxIDMapping, OPTIONAL) The mapping to convert UIDs from the source file system to the destination mount point.
  This SHOULD be implemented using [`mount_setattr(MOUNT_ATTR_IDMAP)`][mount_setattr.2], available since Linux 5.12.
  If specified, the `options` field of the `mounts` structure SHOULD contain either `idmap` or `ridmap` to specify whether the mapping should be applied recursively for `rbind` mounts, as well as to ensure that older runtimes will not silently ignore this field.
  The format is the same as [user namespace mappings](config-linux.md#user-namespace-mappings).
  If specified, it MUST be specified along with `gidMappings`.
* **`gidMappings`** (array of type LinuxIDMapping, OPTIONAL) The mapping to convert GIDs from the source file system to the destination mount point.
  This SHOULD be implemented using [`mount_setattr(MOUNT_ATTR_IDMAP)`][mount_setattr.2], available since Linux 5.12.
  If specified, the `options` field of the `mounts` structure SHOULD contain either `idmap` or `ridmap` to specify whether the mapping should be applied recursively for `rbind` mounts, as well as to ensure that older runtimes will not silently ignore this field.
  For more details see `uidMappings`.
  If specified, it MUST be specified along with `uidMappings`.


### Example (Linux)

```json
"mounts": [
    {
        "destination": "/tmp",
        "type": "tmpfs",
        "source": "tmpfs",
        "options": ["nosuid","strictatime","mode=755","size=65536k"]
    },
    {
        "destination": "/data",
        "type": "none",
        "source": "/volumes/testing",
        "options": ["rbind","rw"]
    }
]
```

### Example (Solaris)

```json
"mounts": [
    {
        "destination": "/opt/local",
        "type": "lofs",
        "source": "/usr/local",
        "options": ["ro","nodevices"]
    },
    {
        "destination": "/opt/sfw",
        "type": "lofs",
        "source": "/opt/sfw"
    }
]
```

## <a name="configProcess" />Process

**`process`** (object, OPTIONAL) specifies the container process.
This property is REQUIRED when [`start`](runtime.md#start) is called.

* **`terminal`** (bool, OPTIONAL) specifies whether a terminal is attached to the process, defaults to false.
    As an example, if set to true on Linux a pseudoterminal pair is allocated for the process and the pseudoterminal pty is duplicated on the process's [standard streams][stdin.3].
* **`consoleSize`** (object, OPTIONAL) specifies the console size in characters of the terminal.
    Runtimes MUST ignore `consoleSize` if `terminal` is `false` or unset.
    * **`height`** (uint, REQUIRED)
    * **`width`** (uint, REQUIRED)
* **`cwd`** (string, REQUIRED) is the working directory that will be set for the executable.
    This value MUST be an absolute path.
* **`env`** (array of strings, OPTIONAL) with the same semantics as [IEEE Std 1003.1-2008's `environ`][ieee-1003.1-2008-xbd-c8.1].
* **`args`** (array of strings, OPTIONAL) with similar semantics to [IEEE Std 1003.1-2008 `execvp`'s *argv*][ieee-1003.1-2008-functions-exec].
    This specification extends the IEEE standard in that at least one entry is REQUIRED (non-Windows), and that entry is used with the same semantics as `execvp`'s *file*. This field is OPTIONAL on Windows, and `commandLine` is REQUIRED if this field is omitted.
* **`commandLine`** (string, OPTIONAL) specifies the full command line to be executed on Windows.
    This is the preferred means of supplying the command line on Windows. If omitted, the runtime will fall back to escaping and concatenating fields from `args` before making the system call into Windows.


### <a name="configPOSIXProcess" />POSIX process

For systems that support POSIX rlimits (for example Linux and Solaris), the `process` object supports the following process-specific properties:

* **`rlimits`** (array of objects, OPTIONAL) allows setting resource limits for the process.
    Each entry has the following structure:

    * **`type`** (string, REQUIRED) the platform resource being limited.
        * Linux: valid values are defined in the [`getrlimit(2)`][getrlimit.2] man page, such as `RLIMIT_MSGQUEUE`.
        * Solaris: valid values are defined in the [`getrlimit(3)`][getrlimit.3] man page, such as `RLIMIT_CORE`.

        The runtime MUST [generate an error](runtime.md#errors) for any values which cannot be mapped to a relevant kernel interface.
        For each entry in `rlimits`, a [`getrlimit(3)`][getrlimit.3] on `type` MUST succeed.
        For the following properties, `rlim` refers to the status returned by the `getrlimit(3)` call.

    * **`soft`** (uint64, REQUIRED) the value of the limit enforced for the corresponding resource.
        `rlim.rlim_cur` MUST match the configured value.
    * **`hard`** (uint64, REQUIRED) the ceiling for the soft limit that could be set by an unprivileged process.
        `rlim.rlim_max` MUST match the configured value.
        Only a privileged process (e.g. one with the `CAP_SYS_RESOURCE` capability) can raise a hard limit.

    If `rlimits` contains duplicated entries with same `type`, the runtime MUST [generate an error](runtime.md#errors).

### <a name="configLinuxProcess" />Linux Process

For Linux-based systems, the `process` object supports the following process-specific properties.

* **`apparmorProfile`** (string, OPTIONAL) specifies the name of the AppArmor profile for the process.
    For more information about AppArmor, see [AppArmor documentation][apparmor].
* **`capabilities`** (object, OPTIONAL) is an object containing arrays that specifies the sets of capabilities for the process.
    Valid values are defined in the [capabilities(7)][capabilities.7] man page, such as `CAP_CHOWN`.
    Any value which cannot be mapped to a relevant kernel interface, or cannot
    be granted otherwise MUST be [logged as a warning](runtime.md#warnings) by
    the runtime. Runtimes SHOULD NOT fail if the container configuration requests
    capabilities that cannot be granted, for example, if the runtime operates in
    a restricted environment with a limited set of capabilities.
    `capabilities` contains the following properties:

    * **`effective`** (array of strings, OPTIONAL) the `effective` field is an array of effective capabilities that are kept for the process.
    * **`bounding`** (array of strings, OPTIONAL) the `bounding` field is an array of bounding capabilities that are kept for the process.
    * **`inheritable`** (array of strings, OPTIONAL) the `inheritable` field is an array of inheritable capabilities that are kept for the process.
    * **`permitted`** (array of strings, OPTIONAL) the `permitted` field is an array of permitted capabilities that are kept for the process.
    * **`ambient`** (array of strings, OPTIONAL) the `ambient` field is an array of ambient capabilities that are kept for the process.
* **`noNewPrivileges`** (bool, OPTIONAL) setting `noNewPrivileges` to true prevents the process from gaining additional privileges.
    As an example, the [`no_new_privs`][no-new-privs] article in the kernel documentation has information on how this is achieved using a `prctl` system call on Linux.
* **`oomScoreAdj`** *(int, OPTIONAL)* adjusts the oom-killer score in `[pid]/oom_score_adj` for the process's `[pid]` in a [proc pseudo-filesystem][proc_2].
    If `oomScoreAdj` is set, the runtime MUST set `oom_score_adj` to the given value.
    If `oomScoreAdj` is not set, the runtime MUST NOT change the value of `oom_score_adj`.

    This is a per-process setting, where as [`disableOOMKiller`](config-linux.md#memory) is scoped for a memory cgroup.
    For more information on how these two settings work together, see [the memory cgroup documentation section 10. OOM Control][cgroup-v1-memory_2].
* **`scheduler`** (object, OPTIONAL) is an object describing the scheduler properties for the process.  The `scheduler` contains the following properties:

    * **`policy`** (string, REQUIRED) represents the scheduling policy.  A valid list of values is:

        * `SCHED_OTHER`
        * `SCHED_FIFO`
        * `SCHED_RR`
        * `SCHED_BATCH`
        * `SCHED_ISO`
        * `SCHED_IDLE`
        * `SCHED_DEADLINE`

    * **`nice`** (int32, OPTIONAL) is the nice value for the process, affecting its priority. A lower nice value corresponds to a higher priority. If not set, the runtime must use the value 0.
    * **`priority`** (int32, OPTIONAL) represents the static priority of the process, used by real-time policies like SCHED_FIFO and SCHED_RR. If not set, the runtime must use the value 0.
    * **`flags`** (array of strings, OPTIONAL) is an array of strings representing scheduling flags.  A valid list of values is:

        * `SCHED_FLAG_RESET_ON_FORK`
        * `SCHED_FLAG_RECLAIM`
        * `SCHED_FLAG_DL_OVERRUN`
        * `SCHED_FLAG_KEEP_POLICY`
        * `SCHED_FLAG_KEEP_PARAMS`
        * `SCHED_FLAG_UTIL_CLAMP_MIN`
        * `SCHED_FLAG_UTIL_CLAMP_MAX`

    * **`runtime`** (uint64, OPTIONAL) represents the amount of time in nanoseconds during which the process is allowed to run in a given period, used by the deadline scheduler. If not set, the runtime must use the value 0.
    * **`deadline`** (uint64, OPTIONAL) represents the absolute deadline for the process to complete its execution, used by the deadline scheduler. If not set, the runtime must use the value 0.
    * **`period`** (uint64, OPTIONAL) represents the length of the period in nanoseconds used for determining the process runtime, used by the deadline scheduler. If not set, the runtime must use the value 0.
* **`selinuxLabel`** (string, OPTIONAL) specifies the SELinux label for the process.
    For more information about SELinux, see  [SELinux documentation][selinux].
* **`ioPriority`** (object, OPTIONAL) configures the I/O priority settings for the container's processes within the process group.
    The I/O priority settings will be automatically applied to the entire process group, affecting all processes within the container.
    The following properties are available:

    * **`class`** (string, REQUIRED) specifies the I/O scheduling class. Possible values are `IOPRIO_CLASS_RT`, `IOPRIO_CLASS_BE`, and `IOPRIO_CLASS_IDLE`.
    * **`priority`** (int, REQUIRED) specifies the priority level within the class. The value should be an integer ranging from 0 (highest) to 7 (lowest).
* **`execCPUAffinity`** (object, OPTIONAL) specifies CPU affinity used to execute the process.
    This setting is not applicable to the container's init process.
    The following properties are available:
    * **`initial`** (string, OPTIONAL) is a list of CPUs a runtime parent
      process to be run on initially, before the transition to container's
      cgroup. This is a a comma-separated list, with dashes to represent
      ranges. For example, `0-3,7` represents CPUs 0,1,2,3, and 7.
    * **`final`** (string, OPTIONAL) is a list of CPUs the process will be run
      on after the transition to container's cgroup. The format is the same as
      for `initial`. If omitted or empty, runtime SHOULD NOT change process'
      CPU affinity after the process is moved to container's cgroup, and the
      final affinity is determined by the Linux kernel.

### <a name="configZOSProcess" />z/OS Process

For z/OS-based systems, the `process` object supports the following process-specific properties.

* **`noNewPrivileges`** (bool, OPTIONAL) setting `noNewPrivileges` to true prevents the process from gaining additional privileges.

### <a name="configUser" />User

The user for the process is a platform-specific structure that allows specific control over which user the process runs as.

#### <a name="configPOSIXUser" />POSIX-platform User

For POSIX platforms the `user` structure has the following fields:

* **`uid`** (int, REQUIRED) specifies the user ID in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).
* **`gid`** (int, REQUIRED) specifies the group ID in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).
* **`umask`** (int, OPTIONAL) specifies the [umask][umask_2] of the user. If unspecified, the umask should not be changed from the calling process' umask.
* **`additionalGids`** (array of ints, OPTIONAL) specifies additional group IDs in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace) to be added to the process.

_Note: symbolic name for uid and gid, such as uname and gname respectively, are left to upper levels to derive (i.e. `/etc/passwd` parsing, NSS, etc)_

### Example (Linux)

```json
"process": {
    "terminal": true,
    "consoleSize": {
        "height": 25,
        "width": 80
    },
    "user": {
        "uid": 1,
        "gid": 1,
        "umask": 63,
        "additionalGids": [5, 6]
    },
    "env": [
        "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "TERM=xterm"
    ],
    "cwd": "/root",
    "args": [
        "sh"
    ],
    "apparmorProfile": "acme_secure_profile",
    "selinuxLabel": "system_u:system_r:svirt_lxc_net_t:s0:c124,c675",
    "ioPriority": {
        "class": "IOPRIO_CLASS_IDLE",
        "priority": 4
    },
    "noNewPrivileges": true,
    "capabilities": {
        "bounding": [
            "CAP_AUDIT_WRITE",
            "CAP_KILL",
            "CAP_NET_BIND_SERVICE"
        ],
       "permitted": [
            "CAP_AUDIT_WRITE",
            "CAP_KILL",
            "CAP_NET_BIND_SERVICE"
        ],
       "inheritable": [
            "CAP_AUDIT_WRITE",
            "CAP_KILL",
            "CAP_NET_BIND_SERVICE"
        ],
        "effective": [
            "CAP_AUDIT_WRITE",
            "CAP_KILL"
        ],
        "ambient": [
            "CAP_NET_BIND_SERVICE"
        ]
    },
    "rlimits": [
        {
            "type": "RLIMIT_NOFILE",
            "hard": 1024,
            "soft": 1024
        }
    ],
    "execCPUAffinity": {
        "initial": "7",
        "final": "0-3,7"
    }
}
```
### Example (Solaris)

```json
"process": {
    "terminal": true,
    "consoleSize": {
        "height": 25,
        "width": 80
    },
    "user": {
        "uid": 1,
        "gid": 1,
        "umask": 7,
        "additionalGids": [2, 8]
    },
    "env": [
        "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "TERM=xterm"
    ],
    "cwd": "/root",
    "args": [
        "/usr/bin/bash"
    ]
}
```

#### <a name="configWindowsUser" />Windows User

For Windows based systems the user structure has the following fields:

* **`username`** (string, OPTIONAL) specifies the user name for the process.

### Example (Windows)

```json
"process": {
    "terminal": true,
    "user": {
        "username": "containeradministrator"
    },
    "env": [
        "VARIABLE=1"
    ],
    "cwd": "c:\\foo",
    "args": [
        "someapp.exe",
    ]
}
```


## <a name="configHostname" />Hostname

* **`hostname`** (string, OPTIONAL) specifies the container's hostname as seen by processes running inside the container.
    On Linux, for example, this will change the hostname in the [container](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace) [UTS namespace][uts-namespace.7].
    Depending on your [namespace configuration](config-linux.md#namespaces), the container UTS namespace may be the [runtime](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace) [UTS namespace][uts-namespace.7].

### Example

```json
"hostname": "mrsdalloway"
```

## <a name="configDomainname" />Domainname

* **`domainname`** (string, OPTIONAL) specifies the container's domainname as seen by processes running inside the container.
    On Linux, for example, this will change the domainname in the [container](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace) [UTS namespace][uts-namespace.7].
    Depending on your [namespace configuration](config-linux.md#namespaces), the container UTS namespace may be the [runtime](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace) [UTS namespace][uts-namespace.7].

### Example

```json
"domainname": "foobarbaz.test"
```

## <a name="configPlatformSpecificConfiguration" />Platform-specific configuration

* **`freebsd`** (object, OPTIONAL) [FreeBSD-specific configuration](config-freebsd.md).
    This MAY be set if the target platform of this spec is `freebsd`.
* **`linux`** (object, OPTIONAL) [Linux-specific configuration](config-linux.md).
    This MAY be set if the target platform of this spec is `linux`.
* **`solaris`** (object, OPTIONAL) [Solaris-specific configuration](config-solaris.md).
    This MAY be set if the target platform of this spec is `solaris`.
* **`vm`** (object, OPTIONAL) [Virtual-machine-specific configuration](config-vm.md).
    This MAY be set if the target platform and architecture of this spec support hardware virtualization.
* **`windows`** (object, OPTIONAL) [Windows-specific configuration](config-windows.md).
    This MUST be set if the target platform of this spec is `windows`.
* **`zos`** (object, OPTIONAL) [z/OS-specific configuration](config-zos.md).
    This MAY be set if the target platform of this spec is `zos`.

### Example (Linux)

```json
{
    "linux": {
        "namespaces": [
            {
                "type": "pid"
            }
        ]
    }
}
```

## <a name="configHooks" />POSIX-platform Hooks

For POSIX platforms, the configuration structure supports `hooks` for configuring custom actions related to the [lifecycle](runtime.md#lifecycle) of the container.

* **`hooks`** (object, OPTIONAL) MAY contain any of the following properties:
    * **`prestart`** (array of objects, OPTIONAL, **DEPRECATED**) is an array of [`prestart` hooks](#prestart).
        * Entries in the array contain the following properties:
            * **`path`** (string, REQUIRED) with similar semantics to [IEEE Std 1003.1-2008 `execv`'s *path*][ieee-1003.1-2008-functions-exec].
                This specification extends the IEEE standard in that **`path`** MUST be absolute.
            * **`args`** (array of strings, OPTIONAL) with the same semantics as [IEEE Std 1003.1-2008 `execv`'s *argv*][ieee-1003.1-2008-functions-exec].
            * **`env`** (array of strings, OPTIONAL) with the same semantics as [IEEE Std 1003.1-2008's `environ`][ieee-1003.1-2008-xbd-c8.1].
            * **`timeout`** (int, OPTIONAL) is the number of seconds before aborting the hook.
                If set, `timeout` MUST be greater than zero.
        * The value of `path` MUST resolve in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
        * The `prestart` hooks MUST be executed in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
    * **`createRuntime`** (array of objects, OPTIONAL) is an array of [`createRuntime` hooks](#createRuntime-hooks).
        * Entries in the array contain the following properties (the entries are identical to the entries in the deprecated `prestart` hooks):
            * **`path`** (string, REQUIRED) with similar semantics to [IEEE Std 1003.1-2008 `execv`'s *path*][ieee-1003.1-2008-functions-exec].
                This specification extends the IEEE standard in that **`path`** MUST be absolute.
            * **`args`** (array of strings, OPTIONAL) with the same semantics as [IEEE Std 1003.1-2008 `execv`'s *argv*][ieee-1003.1-2008-functions-exec].
            * **`env`** (array of strings, OPTIONAL) with the same semantics as [IEEE Std 1003.1-2008's `environ`][ieee-1003.1-2008-xbd-c8.1].
            * **`timeout`** (int, OPTIONAL) is the number of seconds before aborting the hook.
                If set, `timeout` MUST be greater than zero.
        * The value of `path` MUST resolve in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
        * The `createRuntime` hooks MUST be executed in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
    * **`createContainer`** (array of objects, OPTIONAL) is an array of [`createContainer` hooks](#createContainer-hooks).
        * Entries in the array have the same schema as `createRuntime` entries.
        * The value of `path` MUST resolve in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
        * The `createContainer` hooks MUST be executed in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).
    * **`startContainer`** (array of objects, OPTIONAL) is an array of [`startContainer` hooks](#startContainer-hooks).
        * Entries in the array have the same schema as `createRuntime` entries.
        * The value of `path` MUST resolve in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).
        * The `startContainer` hooks MUST be executed in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).
    * **`poststart`** (array of objects, OPTIONAL) is an array of [`poststart` hooks](#poststart).
        * Entries in the array have the same schema as `createRuntime` entries.
        * The value of `path` MUST resolve in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
        * The `poststart` hooks MUST be executed in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
    * **`poststop`** (array of objects, OPTIONAL) is an array of [`poststop` hooks](#poststop).
        * Entries in the array have the same schema as `createRuntime` entries.
        * The value of `path` MUST resolve in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
        * The `poststop` hooks MUST be executed in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).

Hooks allow users to specify programs to run before or after various lifecycle events.
Hooks MUST be called in the listed order.
The [state](runtime.md#state) of the container MUST be passed to hooks over stdin so that they may do work appropriate to the current state of the container.

### <a name="configHooksPrestart" />Prestart

The `prestart` hooks MUST be called as part of the [`create`](runtime.md#create) operation after the runtime environment has been created (according to the configuration in config.json) but before the `pivot_root` or any equivalent operation has been executed.
On Linux, for example, they are called after the container namespaces are created, so they provide an opportunity to customize the container (e.g. the network namespace could be specified in this hook).
The `prestart` hooks MUST be called before the `createRuntime` hooks.

Note: `prestart` hooks were deprecated in favor of `createRuntime`, `createContainer` and `startContainer` hooks, which allow more granular hook control during the create and start phase.

The `prestart` hooks' path MUST resolve in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
The `prestart` hooks MUST be executed in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).

### <a name="configHooksCreateRuntime" />CreateRuntime Hooks

The `createRuntime` hooks MUST be called as part of the [`create`](runtime.md#create) operation after the runtime environment has been created (according to the configuration in config.json) but before the `pivot_root` or any equivalent operation has been executed.

The `createRuntime` hooks' path MUST resolve in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
The `createRuntime` hooks MUST be executed in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).

On Linux, for example, they are called after the container namespaces are created, so they provide an opportunity to customize the container (e.g. the network namespace could be specified in this hook).

The definition of `createRuntime` hooks is currently underspecified and hooks authors, should only expect from the runtime that the mount namespace have been created and the mount operations performed. Other operations such as cgroups and SELinux/AppArmor labels might not have been performed by the runtime.

### <a name="configHooksCreateContainer" />CreateContainer Hooks

The `createContainer` hooks MUST be called as part of the [`create`](runtime.md#create) operation after the runtime environment has been created (according to the configuration in config.json) but before the `pivot_root` or any equivalent operation has been executed.
The `createContainer` hooks MUST be called after the `createRuntime` hooks.

The `createContainer` hooks' path MUST resolve in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
The `createContainer` hooks MUST be executed in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).

For example, on Linux this would happen before the `pivot_root` operation is executed but after the mount namespace was created and setup.

The definition of `createContainer` hooks is currently underspecified and hooks authors, should only expect from the runtime that the mount namespace and different mounts will be setup. Other operations such as cgroups and SELinux/AppArmor labels might not have been performed by the runtime.

### <a name="configHooksStartContainer" />StartContainer Hooks

The `startContainer` hooks MUST be called [before the user-specified process is executed](runtime.md#lifecycle) as part of the [`start`](runtime.md#start) operation.
This hook can be used to execute some operations in the container, for example running the `ldconfig` binary on linux before the container process is spawned.

The `startContainer` hooks' path MUST resolve in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).
The `startContainer` hooks MUST be executed in the [container namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#container-namespace).

### <a name="configHooksPoststart" />Poststart

The `poststart` hooks MUST be called [after the user-specified process is executed](runtime.md#lifecycle) but before the [`start`](runtime.md#start) operation returns.
For example, this hook can notify the user that the container process is spawned.

The `poststart` hooks' path MUST resolve in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
The `poststart` hooks MUST be executed in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).

### <a name="configHooksPoststop" />Poststop

The `poststop` hooks MUST be called [after the container is deleted](runtime.md#lifecycle) but before the [`delete`](runtime.md#delete) operation returns.
Cleanup or debugging functions are examples of such a hook.

The `poststop` hooks' path MUST resolve in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).
The `poststop` hooks MUST be executed in the [runtime namespace](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-namespace).

### Summary

See the below table for a summary of hooks and when they are called:

|           Name          | Namespace |                                                            When                                                                    |
| ----------------------- | --------- | -----------------------------------------------------------------------------------------------------------------------------------|
| `prestart` (Deprecated) | runtime   | During the create operation, after the runtime environment has been created and before the pivot root or any equivalent operation. |
| `createRuntime`         | runtime   | During the create operation, after the runtime environment has been created and before the pivot root or any equivalent operation. |
| `createContainer`       | container | During the create operation, after the runtime environment has been created and before the pivot root or any equivalent operation. |
| `startContainer`        | container | After the start operation is called but before the user-specified program command is executed.                                     |
| `poststart`             | runtime   | After the user-specified process is executed but before the start operation returns.                                               |
| `poststop`              | runtime   | After the container is deleted but before the delete operation returns.                                                            |

### Example

```json
"hooks": {
    "prestart": [
        {
            "path": "/usr/bin/fix-mounts",
            "args": ["fix-mounts", "arg1", "arg2"],
            "env":  [ "key1=value1"]
        },
        {
            "path": "/usr/bin/setup-network"
        }
    ],
    "createRuntime": [
        {
            "path": "/usr/bin/fix-mounts",
            "args": ["fix-mounts", "arg1", "arg2"],
            "env":  [ "key1=value1"]
        },
        {
            "path": "/usr/bin/setup-network"
        }
    ],
    "createContainer": [
        {
            "path": "/usr/bin/mount-hook",
            "args": ["-mount", "arg1", "arg2"],
            "env":  [ "key1=value1"]
        }
    ],
    "startContainer": [
        {
            "path": "/usr/bin/refresh-ldcache"
        }
    ],
    "poststart": [
        {
            "path": "/usr/bin/notify-start",
            "timeout": 5
        }
    ],
    "poststop": [
        {
            "path": "/usr/sbin/cleanup.sh",
            "args": ["cleanup.sh", "-f"]
        }
    ]
}
```

## <a name="configAnnotations" />Annotations

**`annotations`** (object, OPTIONAL) contains arbitrary metadata for the container.
This information MAY be structured or unstructured.
Annotations MUST be a key-value map.
If there are no annotations then this property MAY either be absent or an empty map.

Keys MUST be strings.
Keys MUST NOT be an empty string.
Keys SHOULD be named using a reverse domain notation - e.g. `com.example.myKey`.

The `org.opencontainers` namespace for keys is reserved for use by this specification, annotations using keys in this namespace MUST be as described in this section.
The following keys in the `org.opencontainers` namespaces MAY be used:
|                   Key                   | Definition                                                         |
| --------------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------|
| `org.opencontainers.image.os`           | Indicates the operating system the container image was built to run on. The annotation value MUST have a valid value for the `os` property as defined in [the OCI image specification][oci-image-config-properties]. This annotation SHOULD only be used in accordance with the [OCI image specification's runtime conversion specification][oci-image-conversion]. |
| `org.opencontainers.image.os.version`   | Indicates the operating system version targeted by the container image. The annotation value MUST have a valid value for the `os.version` property as defined in [the OCI image specification][oci-image-config-properties]. This annotation SHOULD only be used in accordance with the [OCI image specification's runtime conversion specification][oci-image-conversion]. |
| `org.opencontainers.image.os.features`  | Indicates mandatory operating system features required by the container image. The annotation value MUST have a valid value for the `os.features` property as defined in [the OCI image specification][oci-image-config-properties]. This annotation SHOULD only be used in accordance with the [OCI image specification's runtime conversion specification][oci-image-conversion]. |
| `org.opencontainers.image.architecture` | Indicates the architecture that binaries in the container image are built to run on. The annotation value MUST have a valid value for the `architecture` property as defined in [the OCI image specification][oci-image-config-properties]. This annotation SHOULD only be used in accordance with the [OCI image specification's runtime conversion specification][oci-image-conversion]. |
| `org.opencontainers.image.variant`      | Indicates the variant of the architecture that binaries in the container image are built to run on. The annotation value MUST have a valid value for the `variant` property as defined in [the OCI image specification][oci-image-config-properties]. This annotation SHOULD only be used in accordance with the [OCI image specification's runtime conversion specification][oci-image-conversion]. |
| `org.opencontainers.image.author`       | Indicates the author of the container image. The annotation value MUST have a valid value for the `author` property as defined in [the OCI image specification][oci-image-config-properties]. This annotation SHOULD only be used in accordance with the [OCI image specification's runtime conversion specification][oci-image-conversion]. |
| `org.opencontainers.image.created`      | Indicates the date and time when the container image was created. The annotation value MUST have a valid value for the `created` property as defined in [the OCIimage specification][oci-image-config-properties]. This annotation SHOULD only be used in accordance with the [OCI image specification's runtime conversion specification][oci-image-conversion]. |
| `org.opencontainers.image.stopSignal`   | Indicates signal that SHOULD be sent by the container runtimes to [kill the container](runtime.md#kill). The annotation value MUST have a valid value for the `config.StopSignal` property as defined in [the OCI image specification][oci-image-config-properties]. This annotation SHOULD only be used in accordance with the [OCI image specification's runtime conversion specification][oci-image-conversion]. |

All other keys in the `org.opencontainers` namespace not specified in this above table are reserved and MUST NOT be used by subsequent specifications.
Runtimes MUST handle unknown annotation keys like any other [unknown property](#extensibility).

Values MUST be strings.
Values MAY be an empty string.

```json
"annotations": {
    "com.example.gpu-cores": "2"
}
```

## <a name="configExtensibility" />Extensibility

Runtimes MAY [log](runtime.md#warnings) unknown properties but MUST otherwise ignore them.
That includes not [generating errors](runtime.md#errors) if they encounter an unknown property.

## Valid values

Runtimes MUST generate an error when invalid or unsupported values are encountered.
Unless support for a valid value is explicitly required, runtimes MAY choose which subset of the valid values it will support.

## Configuration Schema Example

Here is a full example `config.json` for reference.

```json
{
    "ociVersion": "1.0.1",
    "process": {
        "terminal": true,
        "user": {
            "uid": 1,
            "gid": 1,
            "additionalGids": [
                5,
                6
            ]
        },
        "args": [
            "sh"
        ],
        "env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "TERM=xterm"
        ],
        "cwd": "/",
        "capabilities": {
            "bounding": [
                "CAP_AUDIT_WRITE",
                "CAP_KILL",
                "CAP_NET_BIND_SERVICE"
            ],
            "permitted": [
                "CAP_AUDIT_WRITE",
                "CAP_KILL",
                "CAP_NET_BIND_SERVICE"
            ],
            "inheritable": [
                "CAP_AUDIT_WRITE",
                "CAP_KILL",
                "CAP_NET_BIND_SERVICE"
            ],
            "effective": [
                "CAP_AUDIT_WRITE",
                "CAP_KILL"
            ],
            "ambient": [
                "CAP_NET_BIND_SERVICE"
            ]
        },
        "rlimits": [
            {
                "type": "RLIMIT_CORE",
                "hard": 1024,
                "soft": 1024
            },
            {
                "type": "RLIMIT_NOFILE",
                "hard": 1024,
                "soft": 1024
            }
        ],
        "apparmorProfile": "acme_secure_profile",
        "oomScoreAdj": 100,
        "selinuxLabel": "system_u:system_r:svirt_lxc_net_t:s0:c124,c675",
        "ioPriority": {
            "class": "IOPRIO_CLASS_IDLE",
            "priority": 4
        },
        "noNewPrivileges": true
    },
    "root": {
        "path": "rootfs",
        "readonly": true
    },
    "hostname": "slartibartfast",
    "mounts": [
        {
            "destination": "/proc",
            "type": "proc",
            "source": "proc"
        },
        {
            "destination": "/dev",
            "type": "tmpfs",
            "source": "tmpfs",
            "options": [
                "nosuid",
                "strictatime",
                "mode=755",
                "size=65536k"
            ]
        },
        {
            "destination": "/dev/pts",
            "type": "devpts",
            "source": "devpts",
            "options": [
                "nosuid",
                "noexec",
                "newinstance",
                "ptmxmode=0666",
                "mode=0620",
                "gid=5"
            ]
        },
        {
            "destination": "/dev/shm",
            "type": "tmpfs",
            "source": "shm",
            "options": [
                "nosuid",
                "noexec",
                "nodev",
                "mode=1777",
                "size=65536k"
            ]
        },
        {
            "destination": "/dev/mqueue",
            "type": "mqueue",
            "source": "mqueue",
            "options": [
                "nosuid",
                "noexec",
                "nodev"
            ]
        },
        {
            "destination": "/sys",
            "type": "sysfs",
            "source": "sysfs",
            "options": [
                "nosuid",
                "noexec",
                "nodev"
            ]
        },
        {
            "destination": "/sys/fs/cgroup",
            "type": "cgroup",
            "source": "cgroup",
            "options": [
                "nosuid",
                "noexec",
                "nodev",
                "relatime",
                "ro"
            ]
        }
    ],
    "hooks": {
        "prestart": [
            {
                "path": "/usr/bin/fix-mounts",
                "args": [
                    "fix-mounts",
                    "arg1",
                    "arg2"
                ],
                "env": [
                    "key1=value1"
                ]
            },
            {
                "path": "/usr/bin/setup-network"
            }
        ],
        "poststart": [
            {
                "path": "/usr/bin/notify-start",
                "timeout": 5
            }
        ],
        "poststop": [
            {
                "path": "/usr/sbin/cleanup.sh",
                "args": [
                    "cleanup.sh",
                    "-f"
                ]
            }
        ]
    },
    "linux": {
        "devices": [
            {
                "path": "/dev/fuse",
                "type": "c",
                "major": 10,
                "minor": 229,
                "fileMode": 438,
                "uid": 0,
                "gid": 0
            },
            {
                "path": "/dev/sda",
                "type": "b",
                "major": 8,
                "minor": 0,
                "fileMode": 432,
                "uid": 0,
                "gid": 0
            }
        ],
        "uidMappings": [
            {
                "containerID": 0,
                "hostID": 1000,
                "size": 32000
            }
        ],
        "gidMappings": [
            {
                "containerID": 0,
                "hostID": 1000,
                "size": 32000
            }
        ],
        "sysctl": {
            "net.ipv4.ip_forward": "1",
            "net.core.somaxconn": "256"
        },
        "cgroupsPath": "/myRuntime/myContainer",
        "resources": {
            "network": {
                "classID": 1048577,
                "priorities": [
                    {
                        "name": "eth0",
                        "priority": 500
                    },
                    {
                        "name": "eth1",
                        "priority": 1000
                    }
                ]
            },
            "pids": {
                "limit": 32771
            },
            "hugepageLimits": [
                {
                    "pageSize": "2MB",
                    "limit": 9223372036854772000
                },
                {
                    "pageSize": "64KB",
                    "limit": 1000000
                }
            ],
            "memory": {
                "limit": 536870912,
                "reservation": 536870912,
                "swap": 536870912,
                "kernel": -1,
                "kernelTCP": -1,
                "swappiness": 0,
                "disableOOMKiller": false
            },
            "cpu": {
                "shares": 1024,
                "quota": 1000000,
                "period": 500000,
                "realtimeRuntime": 950000,
                "realtimePeriod": 1000000,
                "cpus": "2-3",
                "idle": 1,
                "mems": "0-7"
            },
            "devices": [
                {
                    "allow": false,
                    "access": "rwm"
                },
                {
                    "allow": true,
                    "type": "c",
                    "major": 10,
                    "minor": 229,
                    "access": "rw"
                },
                {
                    "allow": true,
                    "type": "b",
                    "major": 8,
                    "minor": 0,
                    "access": "r"
                }
            ],
            "blockIO": {
                "weight": 10,
                "leafWeight": 10,
                "weightDevice": [
                    {
                        "major": 8,
                        "minor": 0,
                        "weight": 500,
                        "leafWeight": 300
                    },
                    {
                        "major": 8,
                        "minor": 16,
                        "weight": 500
                    }
                ],
                "throttleReadBpsDevice": [
                    {
                        "major": 8,
                        "minor": 0,
                        "rate": 600
                    }
                ],
                "throttleWriteIOPSDevice": [
                    {
                        "major": 8,
                        "minor": 16,
                        "rate": 300
                    }
                ]
            }
        },
        "rootfsPropagation": "slave",
        "seccomp": {
            "defaultAction": "SCMP_ACT_ALLOW",
            "architectures": [
                "SCMP_ARCH_X86",
                "SCMP_ARCH_X32"
            ],
            "syscalls": [
                {
                    "names": [
                        "getcwd",
                        "chmod"
                    ],
                    "action": "SCMP_ACT_ERRNO"
                }
            ]
        },
        "timeOffsets": {
            "monotonic": {
                "secs": 172800,
                "nanosecs": 0
            },
            "boottime": {
                "secs": 604800,
                "nanosecs": 0
            }
        },
        "namespaces": [
            {
                "type": "pid"
            },
            {
                "type": "network"
            },
            {
                "type": "ipc"
            },
            {
                "type": "uts"
            },
            {
                "type": "mount"
            },
            {
                "type": "user"
            },
            {
                "type": "cgroup"
            },
            {
                "type": "time"
            }
        ],
        "maskedPaths": [
            "/proc/kcore",
            "/proc/latency_stats",
            "/proc/timer_stats",
            "/proc/sched_debug"
        ],
        "readonlyPaths": [
            "/proc/asound",
            "/proc/bus",
            "/proc/fs",
            "/proc/irq",
            "/proc/sys",
            "/proc/sysrq-trigger"
        ],
        "mountLabel": "system_u:object_r:svirt_sandbox_file_t:s0:c715,c811"
    },
    "annotations": {
        "com.example.key1": "value1",
        "com.example.key2": "value2"
    }
}
```


[apparmor]: https://wiki.ubuntu.com/AppArmor
[cgroup-v1-memory_2]: https://www.kernel.org/doc/Documentation/cgroup-v1/memory.txt
[selinux]:https://selinuxproject.org/page/Main_Page
[no-new-privs]: https://www.kernel.org/doc/Documentation/prctl/no_new_privs.txt
[proc_2]: https://www.kernel.org/doc/Documentation/filesystems/proc.txt
[umask.2]: https://pubs.opengroup.org/onlinepubs/009695399/functions/umask.html
[semver-v2.0.0]: https://semver.org/spec/v2.0.0.html
[ieee-1003.1-2008-xbd-c8.1]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap08.html#tag_08_01
[ieee-1003.1-2008-functions-exec]: https://pubs.opengroup.org/onlinepubs/9699919799/functions/exec.html
[naming-a-volume]: https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-volume
[oci-image-config-properties]: https://github.com/opencontainers/image-spec/blob/v1.1.0-rc2/config.md#properties
[oci-image-conversion]: https://github.com/opencontainers/image-spec/blob/v1.1.0-rc2/conversion.md

[capabilities.7]: https://man7.org/linux/man-pages/man7/capabilities.7.html
[mount.2]: https://man7.org/linux/man-pages/man2/mount.2.html
[mount.8]: https://man7.org/linux/man-pages/man8/mount.8.html
[mount.8-filesystem-independent]: https://man7.org/linux/man-pages/man8/mount.8.html#FILESYSTEM-INDEPENDENT_MOUNT_OPTIONS
[mount.8-filesystem-specific]: https://man7.org/linux/man-pages/man8/mount.8.html#FILESYSTEM-SPECIFIC_MOUNT_OPTIONS
[mount_setattr.2]: https://man7.org/linux/man-pages/man2/mount_setattr.2.html
[mount-bind]: https://docs.kernel.org/filesystems/sharedsubtree.html
[getrlimit.2]: https://man7.org/linux/man-pages/man2/getrlimit.2.html
[getrlimit.3]: https://pubs.opengroup.org/onlinepubs/9699919799/functions/getrlimit.html
[stdin.3]: https://man7.org/linux/man-pages/man3/stdin.3.html
[uts-namespace.7]: https://man7.org/linux/man-pages/man7/namespaces.7.html
[zonecfg.1m]: https://docs.oracle.com/cd/E86824_01/html/E54764/zonecfg-1m.html
```

## File: `features-linux.md`
```markdown
# <a name="linuxFeatures" />Linux Features Structure

This document describes the [Linux-specific section](features.md#platform-specific-features) of the [Features structure](features.md).

## <a name="linuxFeaturesNamespaces" />Namespaces

* **`namespaces`** (array of strings, OPTIONAL) The recognized names of the namespaces, including namespaces that might not be supported by the host operating system.
  The runtime MUST recognize the elements in this array as the [`type` of `linux.namespaces` objects in `config.json`](config-linux.md#namespaces).

### Example

```json
"namespaces": [
  "cgroup",
  "ipc",
  "mount",
  "network",
  "pid",
  "user",
  "uts"
]
```

## <a name="linuxFeaturesCapabilities" />Capabilities

* **`capabilities`** (array of strings, OPTIONAL) The recognized names of the capabilities, including capabilities that might not be supported by the host operating system.
  The runtime MUST recognize the elements in this array in the [`process.capabilities` object of `config.json`](config.md#linux-process).

### Example

```json
"capabilities": [
  "CAP_CHOWN",
  "CAP_DAC_OVERRIDE",
  "CAP_DAC_READ_SEARCH",
  "CAP_FOWNER",
  "CAP_FSETID",
  "CAP_KILL",
  "CAP_SETGID",
  "CAP_SETUID",
  "CAP_SETPCAP",
  "CAP_LINUX_IMMUTABLE",
  "CAP_NET_BIND_SERVICE",
  "CAP_NET_BROADCAST",
  "CAP_NET_ADMIN",
  "CAP_NET_RAW",
  "CAP_IPC_LOCK",
  "CAP_IPC_OWNER",
  "CAP_SYS_MODULE",
  "CAP_SYS_RAWIO",
  "CAP_SYS_CHROOT",
  "CAP_SYS_PTRACE",
  "CAP_SYS_PACCT",
  "CAP_SYS_ADMIN",
  "CAP_SYS_BOOT",
  "CAP_SYS_NICE",
  "CAP_SYS_RESOURCE",
  "CAP_SYS_TIME",
  "CAP_SYS_TTY_CONFIG",
  "CAP_MKNOD",
  "CAP_LEASE",
  "CAP_AUDIT_WRITE",
  "CAP_AUDIT_CONTROL",
  "CAP_SETFCAP",
  "CAP_MAC_OVERRIDE",
  "CAP_MAC_ADMIN",
  "CAP_SYSLOG",
  "CAP_WAKE_ALARM",
  "CAP_BLOCK_SUSPEND",
  "CAP_AUDIT_READ",
  "CAP_PERFMON",
  "CAP_BPF",
  "CAP_CHECKPOINT_RESTORE"
]
```

## <a name="linuxFeaturesCgroup" />Cgroup

**`cgroup`** (object, OPTIONAL) represents the runtime's implementation status of cgroup managers.
Irrelevant to the cgroup version of the host operating system.

* **`v1`** (bool, OPTIONAL) represents whether the runtime supports cgroup v1.
* **`v2`** (bool, OPTIONAL) represents whether the runtime supports cgroup v2.
* **`systemd`** (bool, OPTIONAL) represents whether the runtime supports system-wide systemd cgroup manager.
* **`systemdUser`** (bool, OPTIONAL) represents whether the runtime supports user-scoped systemd cgroup manager.
* **`rdma`** (bool, OPTIONAL) represents whether the runtime supports RDMA cgroup controller.

### Example

```json
"cgroup": {
  "v1": true,
  "v2": true,
  "systemd": true,
  "systemdUser": true,
  "rdma": false
}
```

## <a name="linuxFeaturesSeccomp" />Seccomp

**`seccomp`** (object, OPTIONAL) represents the runtime's implementation status of seccomp.
Irrelevant to the kernel version of the host operating system.

* **`enabled`** (bool, OPTIONAL) represents whether the runtime supports seccomp.
* **`actions`** (array of strings, OPTIONAL) The recognized names of the seccomp actions.
  The runtime MUST recognize the elements in this array in the [`syscalls[].action` property of the `linux.seccomp` object in `config.json`](config-linux.md#seccomp).
* **`operators`** (array of strings, OPTIONAL) The recognized names of the seccomp operators.
  The runtime MUST recognize the elements in this array in the [`syscalls[].args[].op` property of the `linux.seccomp` object in `config.json`](config-linux.md#seccomp).
* **`archs`** (array of strings, OPTIONAL) The recognized names of the seccomp architectures.
  The runtime MUST recognize the elements in this array in the [`architectures` property of the `linux.seccomp` object in `config.json`](config-linux.md#seccomp).
* **`knownFlags`** (array of strings, OPTIONAL) The recognized names of the seccomp flags.
  The runtime MUST recognize the elements in this array in the [`flags` property of the `linux.seccomp` object in `config.json`](config-linux.md#seccomp).
* **`supportedFlags`** (array of strings, OPTIONAL) The recognized and supported names of the seccomp flags.
  This list may be a subset of `knownFlags` due to some flags not supported by the current kernel and/or libseccomp.
  The runtime MUST recognize and support the elements in this array in the [`flags` property of the `linux.seccomp` object in `config.json`](config-linux.md#seccomp).

### Example

```json
"seccomp": {
  "enabled": true,
  "actions": [
    "SCMP_ACT_ALLOW",
    "SCMP_ACT_ERRNO",
    "SCMP_ACT_KILL",
    "SCMP_ACT_LOG",
    "SCMP_ACT_NOTIFY",
    "SCMP_ACT_TRACE",
    "SCMP_ACT_TRAP"
  ],
  "operators": [
    "SCMP_CMP_EQ",
    "SCMP_CMP_GE",
    "SCMP_CMP_GT",
    "SCMP_CMP_LE",
    "SCMP_CMP_LT",
    "SCMP_CMP_MASKED_EQ",
    "SCMP_CMP_NE"
  ],
  "archs": [
    "SCMP_ARCH_AARCH64",
    "SCMP_ARCH_ARM",
    "SCMP_ARCH_MIPS",
    "SCMP_ARCH_MIPS64",
    "SCMP_ARCH_MIPS64N32",
    "SCMP_ARCH_MIPSEL",
    "SCMP_ARCH_MIPSEL64",
    "SCMP_ARCH_MIPSEL64N32",
    "SCMP_ARCH_PPC",
    "SCMP_ARCH_PPC64",
    "SCMP_ARCH_PPC64LE",
    "SCMP_ARCH_S390",
    "SCMP_ARCH_S390X",
    "SCMP_ARCH_X32",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X86_64"
  ],
  "knownFlags": [
    "SECCOMP_FILTER_FLAG_LOG"
  ],
  "supportedFlags": [
    "SECCOMP_FILTER_FLAG_LOG"
  ]
}
```

## <a name="linuxFeaturesApparmor" />AppArmor

**`apparmor`** (object, OPTIONAL) represents the runtime's implementation status of AppArmor.
Irrelevant to the availability of AppArmor on the host operating system.

* **`enabled`** (bool, OPTIONAL) represents whether the runtime supports AppArmor.

### Example

```json
"apparmor": {
  "enabled": true
}
```

## <a name="linuxFeaturesApparmor" />SELinux

**`selinux`** (object, OPTIONAL) represents the runtime's implementation status of SELinux.
Irrelevant to the availability of SELinux on the host operating system.

* **`enabled`** (bool, OPTIONAL) represents whether the runtime supports SELinux.

### Example

```json
"selinux": {
  "enabled": true
}
```

## <a name="linuxFeaturesMemoryPolicy" />MemoryPolicy

**`memoryPolicy`** (object, OPTIONAL) represents the runtime's implementation status of memoryPolicy.

* **`modes`** (array of strings, OPTIONAL). Recognized memory policies. Includes policies that may not be supported by the host operating system.
  The runtime MUST recognize the elements in this array as the [`mode` of `linux.memoryPolicy` objects in `config.json`](config-linux.md#memory-policy).

* **`flags`** (array of strings, OPTIONAL). Recognized flags for memory policies. Includes flags that may not be supported by the host operating system.
  The runtime MUST recognize the elements in this in the [`flags` property of the `linux.memoryPolicy` object in `config.json`](config-linux.md#memory-policy)

### Example

```json
"memoryPolicy": {
  "modes": [
    "MPOL_DEFAULT",
    "MPOL_BIND",
    "MPOL_INTERLEAVE",
    "MPOL_WEIGHTED_INTERLEAVE",
    "MPOL_PREFERRED",
    "MPOL_PREFERRED_MANY",
    "MPOL_LOCAL"
  ],
  "flags": [
    "MPOL_F_NUMA_BALANCING",
    "MPOL_F_RELATIVE_NODES",
    "MPOL_F_STATIC_NODES"
  ]
}
```

## <a name="linuxFeaturesIntelRdt" />Intel RDT

**`intelRdt`** (object, OPTIONAL) represents the runtime's implementation status of Intel RDT.
Irrelevant to the availability of Intel RDT on the host operating system.

* **`enabled`** (bool, OPTIONAL) represents whether the runtime supports Intel RDT.
* **`schemata`** (bool, OPTIONAL) represents whether the
  (`schemata` field of `linux.intelRdt` in `config.json`)[config-linux.md#intelrdt] is supported.
* **`monitoring`** (bool, OPTIONAL) represents whether the
  (`enableMonitoring` field of `linux.intelRdt` in `config.json`)[config-linux.md#intelrdt] is supported.

### Example

```json
"intelRdt": {
  "enabled": true,
  "schemata": true,
  "monitoring": true
}
```

## <a name="linuxFeaturesMountExtensions" />MountExtensions

**`mountExtensions`** (object, OPTIONAL) represents whether the runtime supports certain mount features, irrespective of the availability of the features on the host operating system.

* **`idmap`** (object, OPTIONAL) represents whether the runtime supports idmap mounts using the `uidMappings` and `gidMappings` properties of the mount.
  * **`enabled`** (bool, OPTIONAL) represents whether the runtime parses and attempts to use the `uidMappings` and `gidMappings` properties of mounts if provided.
    Note that it is possible for runtimes to have partial implementations of id-mapped mounts support (such as only allowing mounts which have mappings matching the container's user namespace, or only allowing the id-mapped bind-mounts).
    In such cases, runtimes MUST still set this value to `true`, to indicate that the runtime recognises the `uidMappings` and `gidMappings` properties.

### Example

```json
"mountExtensions": {
  "idmap":{
    "enabled": true
  }
}
```

## <a name="linuxFeaturesNetDevices" />NetDevices

**`netDevices`** (object, OPTIONAL) represents the runtime's implementation status of Linux network devices.

* **`enabled`** (bool, OPTIONAL) represents whether the runtime supports the capability to move Linux network devices into the container's network namespace.

### Example

```json
"netDevices": {
  "enabled": true
}
```
```

## File: `features.md`
```markdown
# <a name="features" />Features Structure

A [runtime](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime) MAY provide a JSON structure about its implemented features to [runtime callers](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-caller).
This JSON structure is called ["Features structure"](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#features-structure).

The Features structure is irrelevant to the actual availability of the features in the host operating system.
Hence, the content of the Features structure SHOULD be determined on the compilation time of the runtime, not on the execution time.

All properties in the Features structure except `ociVersionMin` and `ociVersionMax` MAY either be absent or have the `null` value.
The `null` value MUST NOT be confused with an empty value such as `0`, `false`, `""`, `[]`, and `{}`.

## <a name="featuresSpecificationVersion" />Specification version

* **`ociVersionMin`** (string, REQUIRED) The minimum recognized version of the Open Container Initiative Runtime Specification.
  The runtime MUST accept this value as the [`ociVersion` property of `config.json`](config.md#specification-version).

* **`ociVersionMax`** (string, REQUIRED) The maximum recognized version of the Open Container Initiative Runtime Specification.
  The runtime MUST accept this value as the [`ociVersion` property of `config.json`](config.md#specification-version).
  The value MUST NOT be less than the value of the `ociVersionMin` property.
  The Features structure MUST NOT contain properties that are not defined in this version of the Open Container Initiative Runtime Specification.

### Example
```json
{
  "ociVersionMin": "1.0.0",
  "ociVersionMax": "1.1.0"
}
```

## <a name="featuresHooks" />Hooks
* **`hooks`** (array of strings, OPTIONAL) The recognized names of the [hooks](config.md#posix-platform-hooks).
  The runtime MUST support the elements in this array as the [`hooks` property of `config.json`](config.md#posix-platform-hooks).

### Example
```json
"hooks": [
  "prestart",
  "createRuntime",
  "createContainer",
  "startContainer",
  "poststart",
  "poststop"
]
```

## <a name="featuresMountOptions" />Mount Options

* **`mountOptions`** (array of strings, OPTIONAL) The recognized names of the mount options, including options that might not be supported by the host operating system.
  The runtime MUST recognize the elements in this array as the [`options` of `mounts` objects in `config.json`](config.md#mounts).
  * Linux: this array SHOULD NOT contain filesystem-specific mount options that are passed to the [mount(2)][mount.2] syscall as `const void *data`.

### Example

```json
"mountOptions": [
  "acl",
  "async",
  "atime",
  "bind",
  "defaults",
  "dev",
  "diratime",
  "dirsync",
  "exec",
  "iversion",
  "lazytime",
  "loud",
  "mand",
  "noacl",
  "noatime",
  "nodev",
  "nodiratime",
  "noexec",
  "noiversion",
  "nolazytime",
  "nomand",
  "norelatime",
  "nostrictatime",
  "nosuid",
  "nosymfollow",
  "private",
  "ratime",
  "rbind",
  "rdev",
  "rdiratime",
  "relatime",
  "remount",
  "rexec",
  "rnoatime",
  "rnodev",
  "rnodiratime",
  "rnoexec",
  "rnorelatime",
  "rnostrictatime",
  "rnosuid",
  "rnosymfollow",
  "ro",
  "rprivate",
  "rrelatime",
  "rro",
  "rrw",
  "rshared",
  "rslave",
  "rstrictatime",
  "rsuid",
  "rsymfollow",
  "runbindable",
  "rw",
  "shared",
  "silent",
  "slave",
  "strictatime",
  "suid",
  "symfollow",
  "sync",
  "tmpcopyup",
  "unbindable"
]
```


## <a name="featuresPlatformSpecificFeatures" />Platform-specific features

* **`linux`** (object, OPTIONAL) [Linux-specific features](features-linux.md).
  This MAY be set if the runtime supports `linux` platform.

## <a name="featuresAnnotations" />Annotations

**`annotations`** (object, OPTIONAL) contains arbitrary metadata of the runtime.
This information MAY be structured or unstructured.
Annotations MUST be a key-value map that follows the same convention as the Key and Values of the [`annotations` property of `config.json`](config.md#annotations).
However, annotations do not need to contain the possible values of the [`annotations` property of `config.json`](config.md#annotations).
The current version of the spec do not provide a way to enumerate the possible values of the [`annotations` property of `config.json`](config.md#annotations).

### Example
```json
"annotations": {
  "org.opencontainers.runc.checkpoint.enabled": "true",
  "org.opencontainers.runc.version": "1.1.0"
}
```

## <a name="featuresPotentiallyUnsafeConfigAnnotations" />Unsafe annotations in `config.json`

**`potentiallyUnsafeConfigAnnotations`** (array of strings, OPTIONAL) contains values of [`annotations` property of `config.json`](config.md#annotations)
that may potentially change the behavior of the runtime.

A value that ends with "." is interpreted as a prefix of annotations.

### Example
```json
"potentiallyUnsafeConfigAnnotations": [
  "com.example.foo.bar",
  "org.systemd.property."
]
```

The example above matches `com.example.foo.bar`, `org.systemd.property.ExecStartPre`, etc.
The example does not match `com.example.foo.bar.baz`.

# Example

Here is a full example for reference.

```json
{
  "ociVersionMin": "1.0.0",
  "ociVersionMax": "1.1.0-rc.2",
  "hooks": [
    "prestart",
    "createRuntime",
    "createContainer",
    "startContainer",
    "poststart",
    "poststop"
  ],
  "mountOptions": [
    "async",
    "atime",
    "bind",
    "defaults",
    "dev",
    "diratime",
    "dirsync",
    "exec",
    "iversion",
    "lazytime",
    "loud",
    "mand",
    "noatime",
    "nodev",
    "nodiratime",
    "noexec",
    "noiversion",
    "nolazytime",
    "nomand",
    "norelatime",
    "nostrictatime",
    "nosuid",
    "nosymfollow",
    "private",
    "ratime",
    "rbind",
    "rdev",
    "rdiratime",
    "relatime",
    "remount",
    "rexec",
    "rnoatime",
    "rnodev",
    "rnodiratime",
    "rnoexec",
    "rnorelatime",
    "rnostrictatime",
    "rnosuid",
    "rnosymfollow",
    "ro",
    "rprivate",
    "rrelatime",
    "rro",
    "rrw",
    "rshared",
    "rslave",
    "rstrictatime",
    "rsuid",
    "rsymfollow",
    "runbindable",
    "rw",
    "shared",
    "silent",
    "slave",
    "strictatime",
    "suid",
    "symfollow",
    "sync",
    "tmpcopyup",
    "unbindable"
  ],
  "linux": {
    "namespaces": [
      "cgroup",
      "ipc",
      "mount",
      "network",
      "pid",
      "user",
      "uts"
    ],
    "capabilities": [
      "CAP_CHOWN",
      "CAP_DAC_OVERRIDE",
      "CAP_DAC_READ_SEARCH",
      "CAP_FOWNER",
      "CAP_FSETID",
      "CAP_KILL",
      "CAP_SETGID",
      "CAP_SETUID",
      "CAP_SETPCAP",
      "CAP_LINUX_IMMUTABLE",
      "CAP_NET_BIND_SERVICE",
      "CAP_NET_BROADCAST",
      "CAP_NET_ADMIN",
      "CAP_NET_RAW",
      "CAP_IPC_LOCK",
      "CAP_IPC_OWNER",
      "CAP_SYS_MODULE",
      "CAP_SYS_RAWIO",
      "CAP_SYS_CHROOT",
      "CAP_SYS_PTRACE",
      "CAP_SYS_PACCT",
      "CAP_SYS_ADMIN",
      "CAP_SYS_BOOT",
      "CAP_SYS_NICE",
      "CAP_SYS_RESOURCE",
      "CAP_SYS_TIME",
      "CAP_SYS_TTY_CONFIG",
      "CAP_MKNOD",
      "CAP_LEASE",
      "CAP_AUDIT_WRITE",
      "CAP_AUDIT_CONTROL",
      "CAP_SETFCAP",
      "CAP_MAC_OVERRIDE",
      "CAP_MAC_ADMIN",
      "CAP_SYSLOG",
      "CAP_WAKE_ALARM",
      "CAP_BLOCK_SUSPEND",
      "CAP_AUDIT_READ",
      "CAP_PERFMON",
      "CAP_BPF",
      "CAP_CHECKPOINT_RESTORE"
    ],
    "cgroup": {
      "v1": true,
      "v2": true,
      "systemd": true,
      "systemdUser": true,
      "rdma": true
    },
    "seccomp": {
      "enabled": true,
      "actions": [
        "SCMP_ACT_ALLOW",
        "SCMP_ACT_ERRNO",
        "SCMP_ACT_KILL",
        "SCMP_ACT_KILL_PROCESS",
        "SCMP_ACT_KILL_THREAD",
        "SCMP_ACT_LOG",
        "SCMP_ACT_NOTIFY",
        "SCMP_ACT_TRACE",
        "SCMP_ACT_TRAP"
      ],
      "operators": [
        "SCMP_CMP_EQ",
        "SCMP_CMP_GE",
        "SCMP_CMP_GT",
        "SCMP_CMP_LE",
        "SCMP_CMP_LT",
        "SCMP_CMP_MASKED_EQ",
        "SCMP_CMP_NE"
      ],
      "archs": [
        "SCMP_ARCH_AARCH64",
        "SCMP_ARCH_ARM",
        "SCMP_ARCH_MIPS",
        "SCMP_ARCH_MIPS64",
        "SCMP_ARCH_MIPS64N32",
        "SCMP_ARCH_MIPSEL",
        "SCMP_ARCH_MIPSEL64",
        "SCMP_ARCH_MIPSEL64N32",
        "SCMP_ARCH_PPC",
        "SCMP_ARCH_PPC64",
        "SCMP_ARCH_PPC64LE",
        "SCMP_ARCH_RISCV64",
        "SCMP_ARCH_S390",
        "SCMP_ARCH_S390X",
        "SCMP_ARCH_X32",
        "SCMP_ARCH_X86",
        "SCMP_ARCH_X86_64"
      ],
      "knownFlags": [
        "SECCOMP_FILTER_FLAG_TSYNC",
        "SECCOMP_FILTER_FLAG_SPEC_ALLOW",
        "SECCOMP_FILTER_FLAG_LOG"
      ],
      "supportedFlags": [
        "SECCOMP_FILTER_FLAG_TSYNC",
        "SECCOMP_FILTER_FLAG_SPEC_ALLOW",
        "SECCOMP_FILTER_FLAG_LOG"
      ]
    },
    "apparmor": {
      "enabled": true
    },
    "selinux": {
      "enabled": true
    },
    "memoryPolicy": {
      "modes": [
        "MPOL_DEFAULT",
        "MPOL_BIND",
        "MPOL_INTERLEAVE",
        "MPOL_WEIGHTED_INTERLEAVE",
        "MPOL_PREFERRED",
        "MPOL_PREFERRED_MANY",
        "MPOL_LOCAL"
      ],
      "flags": [
        "MPOL_F_NUMA_BALANCING",
        "MPOL_F_RELATIVE_NODES",
        "MPOL_F_STATIC_NODES"
      ]
    },
    "intelRdt": {
      "enabled": true,
      "schemata": true,
      "monitoring": true
    }
  },
  "annotations": {
    "io.github.seccomp.libseccomp.version": "2.5.4",
    "org.opencontainers.runc.checkpoint.enabled": "true",
    "org.opencontainers.runc.commit": "v1.1.0-534-g26851168",
    "org.opencontainers.runc.version": "1.1.0+dev"
  }
}
```

[mount.2]: https://man7.org/linux/man-pages/man2/mount.2.html
```

## File: `glossary.md`
```markdown
# <a name="glossary" />Glossary

## <a name="glossaryBundle" />Bundle

A [directory structure](bundle.md) that is written ahead of time, distributed, and used to seed the runtime for creating a [container](#container) and launching a process within it.

## <a name="glossaryConfiguration" />Configuration

The [`config.json`](config.md) file in a [bundle](#bundle) which defines the intended [container](#container) and container process.

## <a name="glossaryContainer" />Container

An environment for executing processes with configurable isolation and resource limitations.
For example, namespaces, resource limits, and mounts are all part of the container environment.

## <a name="glossaryContainerNamespace" />Container namespace

On Linux,the [namespaces][namespaces.7] in which the [configured process](config.md#process) executes.

## <a name="glossaryFeaturesDocument" />Features Structure

A [JSON][] structure that represents [the implemented features](#features.md) of the [runtime](#runtime).
Irrelevant to the actual availability of the features in the host operating system.

## <a name="glossaryJson" />JSON

All configuration [JSON][] MUST be encoded in [UTF-8][].
JSON objects MUST NOT include duplicate names.
The order of entries in JSON objects is not significant.

## <a name="glossaryRuntime" />Runtime

An implementation of this specification.
It reads the [configuration files](#configuration) from a [bundle](#bundle), uses that information to create a [container](#container), launches a process inside the container, and performs other [lifecycle actions](runtime.md).

## <a name="glossaryRuntimeCaller" />Runtime caller
An external program to execute a [runtime](#runtime), directly or indirectly.

Examples of direct callers include containerd, CRI-O, and Podman.
Examples of indirect callers include Docker/Moby and Kubernetes.

Runtime callers often execute a runtime via [runc][]-compatible command line interface, however, its interaction interface is currently out of the scope of the Open Container Initiative Runtime Specification.

## <a name="glossaryRuntimeNamespace" />Runtime namespace

On Linux, the namespaces from which new [container namespaces](#container-namespace) are [created](config-linux.md#namespaces) and from which some configured resources are accessed.

[JSON]: https://tools.ietf.org/html/rfc8259
[UTF-8]: https://www.unicode.org/versions/Unicode8.0.0/ch03.pdf
[runc]: https://github.com/opencontainers/runc

[namespaces.7]: https://man7.org/linux/man-pages/man7/namespaces.7.html
```

## File: `implementations.md`
```markdown
# <a name="implementations" />Implementations

The following sections link to associated projects, some of which are maintained by the OCI and some of which are maintained by external organizations.
If you know of any associated projects that are not listed here, please file a pull request adding a link to that project.

## <a name="implementationsRuntimeContainer" />Runtime (Container)

* [alibaba/inclavare-containers][rune] - Enclave OCI runtime for confidential computing
* [containers/crun][crun] - Runtime implementation in C
* [containers/youki][youki] - Runtime implementation in Rust
* [opencontainers/runc][runc] - Reference implementation of OCI runtime
* [projectatomic/bwrap-oci][bwrap-oci] - Convert the OCI spec file to a command line for [bubblewrap][bubblewrap]
* [systemd/systemd][systemd] - Contains [systemd-nspawn][nspawn], runtime implementation in C (via `--oci-bundle` option since systemd v242)

## <a name="implementationsRuntimeVirtualMachine" />Runtime (Virtual Machine)

* [clearcontainers/runtime][cc-runtime] - Hypervisor-based OCI runtime utilising [virtcontainers][virtcontainers] by Intel®.
* [google/gvisor][gvisor] - gVisor is a user-space kernel, contains runsc to run sandboxed containers.
* [hyperhq/runv][runv] - Hypervisor-based runtime for OCI
* [kata-containers/runtime][kata-runtime] - Hypervisor-based OCI runtime combining technology from [clearcontainers/runtime][cc-runtime] and [hyperhq/runv][runv].

## <a name="implementationsTestingTools" />Testing & Tools

* [huawei-openlab/oct][oct] - Open Container Testing framework for OCI configuration and runtime
* [kunalkushwaha/octool][octool] - A config linter and validator.
* [opencontainers/runtime-tools][runtime-tools] - A config generator and runtime/bundle testing framework.

[bubblewrap]: https://github.com/projectatomic/bubblewrap
[bwrap-oci]: https://github.com/projectatomic/bwrap-oci
[cc-runtime]: https://github.com/clearcontainers/runtime
[crun]: https://github.com/containers/crun
[gvisor]: https://github.com/google/gvisor
[kata-runtime]: https://github.com/kata-containers/runtime
[nspawn]: https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html
[oct]: https://github.com/huawei-openlab/oct
[octool]: https://github.com/kunalkushwaha/octool
[runc]: https://github.com/opencontainers/runc
[rune]: https://github.com/alibaba/inclavare-containers
[runtime-tools]: https://github.com/opencontainers/runtime-tools
[runv]: https://github.com/hyperhq/runv
[systemd]: https://github.com/systemd/systemd
[virtcontainers]: https://github.com/containers/virtcontainers
[youki]: https://github.com/containers/youki
```

## File: `principles.md`
```markdown
# <a name="the5PrinciplesOfStandardContainers" />The 5 principles of Standard Containers

Define a unit of software delivery called a Standard Container.
The goal of a Standard Container is to encapsulate a software component and all its dependencies in a format that is self-describing and portable, so that any compliant runtime can run it without extra dependencies, regardless of the underlying machine and the contents of the container.

The specification for Standard Containers defines:

1. configuration file formats
2. a set of standard operations
3. an execution environment.

A great analogy for this is the physical shipping container used by the transportation industry.
Shipping containers are a fundamental unit of delivery, they can be lifted, stacked, locked, loaded, unloaded and labelled.
Irrespective of their contents, by standardizing the container itself it allowed for a consistent, more streamlined and efficient set of processes to be defined.
For software Standard Containers offer similar functionality by being the fundamental, standardized, unit of delivery for a software package.

## <a name="standardOperations" />1. Standard operations

Standard Containers define a set of STANDARD OPERATIONS.
They can be created, started, and stopped using standard container tools; copied and snapshotted using standard filesystem tools; and downloaded and uploaded using standard network tools.

## <a name="contentAgnostic" />2. Content-agnostic

Standard Containers are CONTENT-AGNOSTIC: all standard operations have the same effect regardless of the contents.
They are started in the same way whether they contain a postgres database, a php application with its dependencies and application server, or Java build artifacts.

## <a name="infrastructureAgnostic" />3. Infrastructure-agnostic

Standard Containers are INFRASTRUCTURE-AGNOSTIC: they can be run in any OCI supported infrastructure.
For example, a standard container can be bundled on a laptop, uploaded to cloud storage, downloaded, run and snapshotted by a build server at a fiber hotel in Virginia, uploaded to 10 staging servers in a home-made private cloud cluster, then sent to 30 production instances across 3 public cloud regions.

## <a name="designedForAutomation" />4. Designed for automation

Standard Containers are DESIGNED FOR AUTOMATION: because they offer the same standard operations regardless of content and infrastructure, Standard Containers, are extremely well-suited for automation.
In fact, you could say automation is their secret weapon.

Many things that once required time-consuming and error-prone human effort can now be programmed.
Before Standard Containers, by the time a software component ran in production, it had been individually built, configured, bundled, documented, patched, vendored, templated, tweaked and instrumented by 10 different people on 10 different computers.
Builds failed, libraries conflicted, mirrors crashed, post-it notes were lost, logs were misplaced, cluster updates were half-broken.
The process was slow, inefficient and cost a fortune - and was entirely different depending on the language and infrastructure provider.

## <a name="industrialGradeDelivery" />5. Industrial-grade delivery

Standard Containers make INDUSTRIAL-GRADE DELIVERY of software a reality.
Leveraging all of the properties listed above, Standard Containers are enabling large and small enterprises to streamline and automate their software delivery pipelines.
Whether it is in-house DevOps flows, or external customer-based software delivery mechanisms, Standard Containers are changing the way the community thinks about software packaging and delivery.
```

## File: `runtime-linux.md`
```markdown
# <a name="linuxRuntime" />Linux Runtime

## <a name="runtimeLinuxFileDescriptors" />File descriptors

By default, only the `stdin`, `stdout` and `stderr` file descriptors are kept open for the application by the runtime.
The runtime MAY pass additional file descriptors to the application to support features such as [socket activation][socket-activated-containers].
Some of the file descriptors MAY be redirected to `/dev/null` even though they are open.

## <a name="runtimeLinuxDevSymbolicLinks" /> Dev symbolic links

While creating the container (step 2 in the [lifecycle](runtime.md#lifecycle)), runtimes MUST create the following symlinks if the source file exists after processing [`mounts`](config.md#mounts):

|    Source       | Destination |
| --------------- | ----------- |
| /proc/self/fd   | /dev/fd     |
| /proc/self/fd/0 | /dev/stdin  |
| /proc/self/fd/1 | /dev/stdout |
| /proc/self/fd/2 | /dev/stderr |


[socket-activated-containers]: https://0pointer.de/blog/projects/socket-activated-containers.html
```

## File: `runtime.md`
```markdown
# <a name="runtimeAndLifecycle" />Runtime and Lifecycle

## <a name="runtimeScopeContainer" />Scope of a Container

The entity using a runtime to create a container MUST be able to use the operations defined in this specification against that same container.
Whether other entities using the same, or other, instance of the runtime can see that container is out of scope of this specification.

## <a name="runtimeState" />State

The state of a container includes the following properties:

* **`ociVersion`** (string, REQUIRED) is version of the Open Container Initiative Runtime Specification with which the state complies.
* **`id`** (string, REQUIRED) is the container's ID.
    This MUST be unique across all containers on this host.
    There is no requirement that it be unique across hosts.
* **`status`** (string, REQUIRED) is the runtime state of the container.
    The value MAY be one of:

    * `creating`: the container is being created (step 2 in the [lifecycle](#lifecycle))
    * `created`: the runtime has finished the [create operation](#create) (after step 2 in the [lifecycle](#lifecycle)), and the container process has neither exited nor executed the user-specified program
    * `running`: the container process has executed the user-specified program but has not exited (after step 8 in the [lifecycle](#lifecycle))
    * `stopped`: the container process has exited (step 10 in the [lifecycle](#lifecycle))

    Additional values MAY be defined by the runtime, however, they MUST be used to represent new runtime states not defined above.
* **`pid`** (int, REQUIRED when `status` is `created` or `running` on Linux, OPTIONAL on other platforms) is the ID of the container process.
  For hooks executed in the runtime namespace, it is the pid as seen by the runtime.
  For hooks executed in the container namespace, it is the pid as seen by the container.
* **`bundle`** (string, REQUIRED) is the absolute path to the container's bundle directory.
    This is provided so that consumers can find the container's configuration and root filesystem on the host.
* **`annotations`** (map, OPTIONAL) contains the list of annotations associated with the container.
    If no annotations were provided then this property MAY either be absent or an empty map.

The state MAY include additional properties.

When serialized in JSON, the format MUST adhere to the JSON Schema [`schema/state-schema.json`](schema/state-schema.json).

See [Query State](#query-state) for information on retrieving the state of a container.

### Example

```json
{
    "ociVersion": "0.2.0",
    "id": "oci-container1",
    "status": "running",
    "pid": 4422,
    "bundle": "/containers/redis",
    "annotations": {
        "myKey": "myValue"
    }
}
```

## <a name="runtimeLifecycle" />Lifecycle
The lifecycle describes the timeline of events that happen from when a container is created to when it ceases to exist.

1. OCI compliant runtime's [`create`](runtime.md#create) command is invoked with a reference to the location of the bundle and a unique identifier.
2. The container's runtime environment MUST be created according to the configuration in [`config.json`](config.md).
    If the runtime is unable to create the environment specified in the [`config.json`](config.md), it MUST [generate an error](#errors).
    While the resources requested in the [`config.json`](config.md) MUST be created, the user-specified program (from [`process`](config.md#process)) MUST NOT be run at this time.
    Any updates to [`config.json`](config.md) after this step MUST NOT affect the container.
3. The [`prestart` hooks](config.md#prestart) MUST be invoked by the runtime.
    If any `prestart` hook fails, the runtime MUST [generate an error](#errors), stop the container, and continue the lifecycle at step 12.
4. The [`createRuntime` hooks](config.md#createRuntime-hooks) MUST be invoked by the runtime.
    If any `createRuntime` hook fails, the runtime MUST [generate an error](#errors), stop the container, and continue the lifecycle at step 12.
5. The [`createContainer` hooks](config.md#createContainer-hooks) MUST be invoked by the runtime.
    If any `createContainer` hook fails, the runtime MUST [generate an error](#errors), stop the container, and continue the lifecycle at step 12.
6. Runtime's [`start`](runtime.md#start) command is invoked with the unique identifier of the container.
7. The [`startContainer` hooks](config.md#startContainer-hooks) MUST be invoked by the runtime.
    If any `startContainer` hook fails, the runtime MUST [generate an error](#errors), stop the container, and continue the lifecycle at step 12.
8. The runtime MUST run the user-specified program, as specified by [`process`](config.md#process).
9. The [`poststart` hooks](config.md#poststart) MUST be invoked by the runtime.
    If any `poststart` hook fails, the runtime MUST [generate an error](#errors), stop the container, and continue the lifecycle at step 12.
10. The container process exits.
    This MAY happen due to erroring out, exiting, crashing or the runtime's [`kill`](runtime.md#kill) operation being invoked.
11. Runtime's [`delete`](runtime.md#delete) command is invoked with the unique identifier of the container.
12. The container MUST be destroyed by undoing the steps performed during create phase (step 2).
13. The [`poststop` hooks](config.md#poststop) MUST be invoked by the runtime.
    If any `poststop` hook fails, the runtime MUST [log a warning](#warnings), but the remaining hooks and lifecycle continue as if the hook had succeeded.

## <a name="runtimeErrors" />Errors

In cases where the specified operation generates an error, this specification does not mandate how, or even if, that error is returned or exposed to the user of an implementation.
Unless otherwise stated, generating an error MUST leave the state of the environment as if the operation were never attempted - modulo any possible trivial ancillary changes such as logging.

## <a name="runtimeWarnings" />Warnings

In cases where the specified operation logs a warning, this specification does not mandate how, or even if, that warning is returned or exposed to the user of an implementation.
Unless otherwise stated, logging a warning does not change the flow of the operation; it MUST continue as if the warning had not been logged.

## <a name="runtimeOperations" />Operations

Unless otherwise stated, runtimes MUST support the following operations.

Note: these operations are not specifying any command-line APIs, and the parameters are inputs for general operations.

### <a name="runtimeQueryState" />Query State

`state <container-id>`

This operation MUST [generate an error](#errors) if it is not provided the ID of a container.
Attempting to query a container that does not exist MUST [generate an error](#errors).
This operation MUST return the state of a container as specified in the [State](#state) section.

### <a name="runtimeCreate" />Create

`create <container-id> <path-to-bundle>`

This operation MUST [generate an error](#errors) if it is not provided a path to the bundle and the container ID to associate with the container.
If the ID provided is not unique across all containers within the scope of the runtime, or is not valid in any other way, the implementation MUST [generate an error](#errors) and a new container MUST NOT be created.
This operation MUST create a new container.

All of the properties configured in [`config.json`](config.md) except for [`process`](config.md#process) MUST be applied.
[`process.args`](config.md#process) MUST NOT be applied until triggered by the [`start`](#start) operation.
The remaining `process` properties MAY be applied by this operation.
If the runtime cannot apply a property as specified in the [configuration](config.md), it MUST [generate an error](#errors) and a new container MUST NOT be created.

The runtime MAY validate `config.json` against this spec, either generically or with respect to the local system capabilities, before creating the container ([step 2](#lifecycle)).
[Runtime callers](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md#runtime-caller) who are interested in pre-create validation can run [bundle-validation tools](implementations.md#testing--tools) before invoking the create operation.

Any changes made to the [`config.json`](config.md) file after this operation will not have an effect on the container.

### <a name="runtimeStart" />Start
`start <container-id>`

This operation MUST [generate an error](#errors) if it is not provided the container ID.
Attempting to `start` a container that is not [`created`](#state) MUST have no effect on the container and MUST [generate an error](#errors).
This operation MUST run the user-specified program as specified by [`process`](config.md#process).
This operation MUST generate an error if `process` was not set.

### <a name="runtimeKill" />Kill
`kill <container-id> <signal>`

This operation MUST [generate an error](#errors) if it is not provided the container ID.
Attempting to send a signal to a container that is neither [`created` nor `running`](#state) MUST have no effect on the container and MUST [generate an error](#errors).
This operation MUST send the specified signal to the container process.

### <a name="runtimeDelete" />Delete
`delete <container-id>`

This operation MUST [generate an error](#errors) if it is not provided the container ID.
Attempting to `delete` a container that is not [`stopped`](#state) MUST have no effect on the container and MUST [generate an error](#errors).
Deleting a container MUST delete the resources that were created during the `create` step.
Note that resources associated with the container, but not created by this container, MUST NOT be deleted.
Once a container is deleted its ID MAY be used by a subsequent container.


## <a name="runtimeHooks" />Hooks
Many of the operations specified in this specification have "hooks" that allow for additional actions to be taken before or after each operation.
See [runtime configuration for hooks](./config.md#posix-platform-hooks) for more information.
```

## File: `spec.md`
```markdown
# <a name="openContainerInitiativeRuntimeSpecification" />Open Container Initiative Runtime Specification

The [Open Container Initiative][oci] develops specifications for standards on Operating System process and application containers.

# <a name="ociRuntimeSpecAbstract" />Abstract

The Open Container Initiative Runtime Specification aims to specify the configuration, execution environment, and lifecycle of a container.

A container's configuration is specified as the `config.json` for the supported platforms and details the fields that enable the creation of a container.
The execution environment is specified to ensure that applications running inside a container have a consistent environment between runtimes along with common actions defined for the container's lifecycle.

# <a name="ociRuntimeSpecPlatforms" />Platforms

Platforms defined by this specification are:

* `freebsd`: [runtime.md](runtime.md), [config.md](config.md), [features.md](features.md), and [config-freebsd.md](config-freebsd.md).
* `linux`: [runtime.md](runtime.md), [config.md](config.md), [features.md](features.md), [config-linux.md](config-linux.md), [runtime-linux.md](runtime-linux.md), and [features-linux.md](features-linux.md).
* `solaris`: [runtime.md](runtime.md), [config.md](config.md), [features.md](features.md), and [config-solaris.md](config-solaris.md).
* `windows`: [runtime.md](runtime.md), [config.md](config.md), [features.md](features.md), and [config-windows.md](config-windows.md).
* `vm`: [runtime.md](runtime.md), [config.md](config.md), [features.md](features.md), and [config-vm.md](config-vm.md).
* `zos`: [runtime.md](runtime.md), [config.md](config.md), [features.md](features.md), and [config-zos.md](config-zos.md).

# <a name="ociRuntimeSpecTOC" />Table of Contents

- [Introduction](spec.md)
    - [Notational Conventions](#notational-conventions)
    - [Container Principles](../../../core/security/QUARANTINE/vetted/repos/trivy/docs/community/principles.md)
- [Filesystem Bundle](bundle.md)
- [Runtime and Lifecycle](runtime.md)
    - [Linux-specific Runtime and Lifecycle](runtime-linux.md)
- [Configuration](config.md)
    - [FreeBSD-specific Configuration](config-freebsd.md)
    - [Linux-specific Configuration](config-linux.md)
    - [Solaris-specific Configuration](config-solaris.md)
    - [Windows-specific Configuration](config-windows.md)
    - [Virtual-Machine-specific Configuration](config-vm.md)
    - [z/OS-specific Configuration](config-zos.md)
- [Features Structure](features.md)
    - [Linux-specific Features Structure](features-linux.md)
- [Glossary](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md)

# <a name="ociRuntimeSpecNotationalConventions" />Notational Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [RFC 2119][rfc2119].

The key words "unspecified", "undefined", and "implementation-defined" are to be interpreted as described in the [rationale for the C99 standard][c99-unspecified].

An implementation is not compliant for a given CPU architecture if it fails to satisfy one or more of the MUST, REQUIRED, or SHALL requirements for the [platforms](#platforms) it implements.
An implementation is compliant for a given CPU architecture if it satisfies all the MUST, REQUIRED, and SHALL requirements for the [platforms](#platforms) it implements.


[c99-unspecified]: https://www.open-std.org/jtc1/sc22/wg14/www/C99RationaleV5.10.pdf#page=18
[oci]: https://opencontainers.org
[rfc2119]: https://www.rfc-editor.org/rfc/rfc2119.html
```

## File: `style.md`
```markdown
# <a name="styleAndConventions" />Style and conventions

## <a name="styleOneSentence" />One sentence per line

To keep consistency throughout the Markdown files in the Open Container spec all files should be formatted one sentence per line.
This fixes two things: it makes diffing easier with git and it resolves fights about line wrapping length.
For example, this paragraph will span three lines in the Markdown source.

## <a name="styleHex" />Traditionally hex settings should use JSON integers, not JSON strings

For example, [`"classID": 1048577`](config-linux.md#network) instead of `"classID": "0x100001"`.
The config JSON isn't enough of a UI to be worth jumping through string <-> integer hoops to support an 0x… form ([source][integer-over-hex]).

## <a name="styleConstantNames" />Constant names should keep redundant prefixes

For example, `CAP_KILL` instead of `KILL` in [**`process.capabilities`**](config.md#process).
The redundancy reduction from removing the namespacing prefix is not useful enough to be worth trimming the upstream identifier ([source][keep-prefix]).

## <a name="styleOptionalSettings" />Optional settings should not have pointer Go types

Because in many cases the Go default for the type is a no-op in the spec (sources [here][no-pointer-for-strings], [here][no-pointer-for-slices], and [here][no-pointer-for-boolean]).
The exceptions are entries where we need to distinguish between “not set” and “set to the Go default for that type” ([source][pointer-when-updates-require-changes]), and this decision should be made on a per-setting case.

## Links

Internal links should be [relative links][markdown-relative-links] when linking to content within the repository.
Internal links should be used inline.

External links should be collected at the bottom of a markdown file and used as referenced links.
See 'Referenced Links' in this [markdown quick reference][markdown-quick-reference].
The use of referenced links in the markdown body helps to keep files clean and organized.
This also facilitates updates of external link targets on a per-file basis.

Referenced links should be kept in two alphabetically sorted sets, a general reference section followed by a man page section.
To keep Pandoc happy, duplicate naming of links within pages listed in the Makefile's `DOC_FILES` variable should be avoided by appending an `_N` to the link tagname, where `N` is some number not currently in use.
The organization and style of an existing reference section should be maintained unless it violates these style guidelines.

An exception to these rules is when a URL is needed contextually, for example when showing an explicit link to the reader.

## Examples

### <a name="styleAnchoring" />Anchoring

For any given section that provides a notable example, it is ideal to have it denoted with [markdown headers][markdown-headers].
The level of header should be such that it is a subheader of the header it is an example of.

#### Example

```markdown
## Some Topic

### Some Subheader

#### Further Subheader

##### Example

To use Further Subheader, ...

### Example

To use Some Topic, ...

```

### <a name="styleContent" />Content

Where necessary, the values in the example can be empty or unset, but accommodate with comments regarding this intention.

Where feasible, the content and values used in an example should convey the fullest use of the data structures concerned.
Most commonly onlookers will intend to copy-and-paste a "working example".
If the intention of the example is to be a fully utilized example, rather than a copy-and-paste example, perhaps add a comment as such.

```markdown
### Example
```
```json
{
    "foo": null,
    "bar": ""
}
```

**vs.**

```markdown
### Example

Following is a fully populated example (not necessarily for copy/paste use)
```
```json
{
    "foo": [
        1,
        2,
        3
    ],
    "bar": "waffles",
    "bif": {
        "baz": "potatoes"
    }
}
```

### Links

The following is an example of different types of links.
This is shown as a complete markdown file, where the referenced links are at the bottom.

```markdown
The specification repository's [glossary](../../../core/security/QUARANTINE/vetted/repos/PUAClaw/docs/GLOSSARY.md) is where readers can find definitions of commonly used terms.

Readers may click through to the [Open Containers namespace][open-containers] on [GitHub][github].

The URL for the Open Containers link above is: https://github.com/opencontainers


[github]: https://github.com
[open-containers]: https://github.com/opencontainers
```


[integer-over-hex]: https://github.com/opencontainers/runtime-spec/pull/267#r48360013
[keep-prefix]: https://github.com/opencontainers/runtime-spec/pull/159#issuecomment-138728337
[no-pointer-for-boolean]: https://github.com/opencontainers/runtime-spec/pull/290#r50296396
[no-pointer-for-slices]: https://github.com/opencontainers/runtime-spec/pull/316#r50782982
[no-pointer-for-strings]: https://github.com/opencontainers/runtime-spec/pull/653#issue-200439192
[pointer-when-updates-require-changes]: https://github.com/opencontainers/runtime-spec/pull/317#r50932706
[markdown-headers]: https://help.github.com/articles/basic-writing-and-formatting-syntax/#headings
[markdown-quick-reference]: https://en.support.wordpress.com/markdown-quick-reference
[markdown-relative-links]: https://help.github.com/articles/basic-writing-and-formatting-syntax/#relative-links
```

## File: `schema/Makefile`
```
GOOD_TESTS = $(wildcard test/good/*.json)
BAD_TESTS = $(wildcard test/bad/*.json)

default: validate

help:
	@echo "Usage: make [target]"
	@echo
	@echo " * 'fmt' - format the json with indentation"
	@echo " * 'help' - show this help information"
	@echo " * 'validate' - build the validation tool"

fmt:
	find . -name '*.json' -exec bash -c 'jq --indent 4 -M . {} > xx && mv xx {} || echo "skipping invalid {}"' \;

.PHONY: validate
validate: validate.go
	GO111MODULE=auto go get github.com/xeipuuv/gojsonschema
	GO111MODULE=auto go build ./validate.go

test: validate $(TESTS)
	for TYPE in $$(ls test); \
	do \
		echo "testing $${TYPE}"; \
		for FILE in $$(ls "test/$${TYPE}/good"); \
		do \
			echo "  testing test/$${TYPE}/good/$${FILE}"; \
			if ./validate "$${TYPE}-schema.json" "test/$${TYPE}/good/$${FILE}" ; \
			then \
				echo "    received expected validation success" ; \
			else \
				echo "    received unexpected validation failure" ; \
				exit 1; \
			fi \
		done; \
		for FILE in $$(ls "test/$${TYPE}/bad"); \
		do \
			echo "  testing test/$${TYPE}/bad/$${FILE}"; \
			if ./validate "$${TYPE}-schema.json" "test/$${TYPE}/bad/$${FILE}" ; \
			then \
				echo "    received unexpected validation success" ; \
				exit 1; \
			else \
				echo "    received expected validation failure" ; \
			fi \
		done; \
	done

clean:
	rm -f validate
```

## File: `schema/README.md`
```markdown
# JSON schema

## Overview

This directory contains the [JSON Schema](https://json-schema.org) for validating JSON covered by this specification.

The layout of the files is as follows:

* [config-schema.json](config-schema.json) - the primary entrypoint for the [configuration](config.md) schema
* [config-linux.json](config-linux.json) - the [Linux-specific configuration sub-structure](../config-linux.md)
* [config-solaris.json](config-solaris.json) - the [Solaris-specific configuration sub-structure](../config-solaris.md)
* [config-windows.json](config-windows.json) - the [Windows-specific configuration sub-structure](../config-windows.md)
* [config-freebsd.json](config-freebsd.json) - the [FreeBSD-specific configuration sub-structure](../config-freebsd.md)
* [state-schema.json](state-schema.json) - the primary entrypoint for the [state JSON](../runtime.md#state) schema
* [defs.json](defs.json) - definitions for general types
* [defs-linux.json](defs-linux.json) - definitions for Linux-specific types
* [defs-windows.json](defs-windows.json) - definitions for Windows-specific types
* [validate.go](validate.go) - validation utility source code


## Utility

There is also included a simple utility for facilitating validation.
To build it:

```bash
go get github.com/xeipuuv/gojsonschema
go build ./validate.go
```

Or you can just use make command to create the utility:

```bash
make validate
```

Then use it like:

```bash
./validate config-schema.json <yourpath>/config.json
```

Or like:

```bash
./validate https://raw.githubusercontent.com/opencontainers/runtime-spec/<runtime-spec-version>/schema/config-schema.json <yourpath>/config.json
```
```

## File: `schema/config-freebsd.json`
```json
{
    "freebsd": {
        "description": "FreeBSD platform-specific configurations",
        "type": "object",
        "properties": {
            "devices": {
                "type": "array",
                "items": {
                    "$ref": "defs-freebsd.json#/definitions/Device"
                }
            },
            "jail": {
                "type": "object",
                "properties": {
                    "parent": {
                        "type": "string"
                    },
                    "host": {
                        "$ref": "defs-freebsd.json#/definitions/SharingModeNoDisable"
                    },
                    "ip4": {
                        "$ref": "defs-freebsd.json#/definitions/SharingMode"
                    },
                    "ip4Addr": {
                        "$ref": "defs.json#/definitions/ArrayOfStrings"
                    },
                    "ip6": {
                        "$ref": "defs-freebsd.json#/definitions/SharingMode"
                    },
                    "ip6Addr": {
                        "$ref": "defs.json#/definitions/ArrayOfStrings"
                    },
                    "vnet": {
                        "$ref": "defs-freebsd.json#/definitions/SharingModeNoDisable"
                    },
                    "interface": {
                        "type": "string"
                    },
                    "vnetInterfaces": {
                        "$ref": "defs.json#/definitions/ArrayOfStrings"
                    },
                    "sysvmsg": {
                        "$ref": "defs-freebsd.json#/definitions/SharingMode"
                    },
                    "sysvsem": {
                        "$ref": "defs-freebsd.json#/definitions/SharingMode"
                    },
                    "sysvshm": {
                        "$ref": "defs-freebsd.json#/definitions/SharingMode"
                    },
                    "enforceStatfs": {
                        "$ref": "defs.json#/definitions/uint8"
                    },
                    "allow": {
                        "type": "object",
                        "properties": {
                            "setHostname": {
                                "type": "boolean"
                            },
                            "rawSockets": {
                                "type": "boolean"
                            },
                            "chflags": {
                                "type": "boolean"
                            },
                            "mount": {
                                "$ref": "defs.json#/definitions/ArrayOfStrings"
                            },
                            "quotas": {
                                "type": "boolean"
                            },
                            "socketAf": {
                                "type": "boolean"
                            },
                            "mlock": {
                                "type": "boolean"
                            },
                            "reservedPorts": {
                                "type": "boolean"
                            },
                            "suser": {
                                "type": "boolean"
                            }
                        }
                    }
                }
            }
        }
    }
}
```

## File: `schema/config-linux.json`
```json
{
    "linux": {
        "description": "Linux platform-specific configurations",
        "type": "object",
        "properties": {
            "devices": {
                "type": "array",
                "items": {
                    "$ref": "defs-linux.json#/definitions/Device"
                }
            },
            "netDevices": {
                "type": "object",
                "additionalProperties": {
                    "$ref": "defs-linux.json#/definitions/NetDevice"
                }
            },
            "uidMappings": {
                "type": "array",
                "items": {
                    "$ref": "defs.json#/definitions/IDMapping"
                }
            },
            "gidMappings": {
                "type": "array",
                "items": {
                    "$ref": "defs.json#/definitions/IDMapping"
                }
            },
            "namespaces": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {
                            "$ref": "defs-linux.json#/definitions/NamespaceReference"
                        }
                    ]
                }
            },
            "resources": {
                "type": "object",
                "properties": {
                    "unified": {
                        "$ref": "defs.json#/definitions/mapStringString"
                    },
                    "devices": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-linux.json#/definitions/DeviceCgroup"
                        }
                    },
                    "pids": {
                        "type": "object",
                        "properties": {
                            "limit": {
                                "$ref": "defs.json#/definitions/int64"
                            }
                        },
                        "required": [
                            "limit"
                        ]
                    },
                    "blockIO": {
                        "type": "object",
                        "properties": {
                            "weight": {
                                "$ref": "defs-linux.json#/definitions/weight"
                            },
                            "leafWeight": {
                                "$ref": "defs-linux.json#/definitions/weight"
                            },
                            "throttleReadBpsDevice": {
                                "type": "array",
                                "items": {
                                    "$ref": "defs-linux.json#/definitions/blockIODeviceThrottle"
                                }
                            },
                            "throttleWriteBpsDevice": {
                                "type": "array",
                                "items": {
                                    "$ref": "defs-linux.json#/definitions/blockIODeviceThrottle"
                                }
                            },
                            "throttleReadIOPSDevice": {
                                "type": "array",
                                "items": {
                                    "$ref": "defs-linux.json#/definitions/blockIODeviceThrottle"
                                }
                            },
                            "throttleWriteIOPSDevice": {
                                "type": "array",
                                "items": {
                                    "$ref": "defs-linux.json#/definitions/blockIODeviceThrottle"
                                }
                            },
                            "weightDevice": {
                                "type": "array",
                                "items": {
                                    "$ref": "defs-linux.json#/definitions/blockIODeviceWeight"
                                }
                            }
                        }
                    },
                    "cpu": {
                        "type": "object",
                        "properties": {
                            "cpus": {
                                "type": "string"
                            },
                            "mems": {
                                "type": "string"
                            },
                            "period": {
                                "$ref": "defs.json#/definitions/uint64"
                            },
                            "quota": {
                                "$ref": "defs.json#/definitions/int64"
                            },
                            "burst": {
                                "$ref": "defs.json#/definitions/uint64"
                            },
                            "realtimePeriod": {
                                "$ref": "defs.json#/definitions/uint64"
                            },
                            "realtimeRuntime": {
                                "$ref": "defs.json#/definitions/int64"
                            },
                            "shares": {
                                "$ref": "defs.json#/definitions/uint64"
                            },
                            "idle": {
                                "$ref": "defs.json#/definitions/int64"
                            }
                        }
                    },
                    "hugepageLimits": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "pageSize": {
                                    "type": "string",
                                    "pattern": "^[1-9][0-9]*[KMG]B$"
                                },
                                "limit": {
                                    "$ref": "defs.json#/definitions/uint64"
                                }
                            },
                            "required": [
                                "pageSize",
                                "limit"
                            ]
                        }
                    },
                    "memory": {
                        "type": "object",
                        "properties": {
                            "kernel": {
                                "$ref": "defs.json#/definitions/int64"
                            },
                            "kernelTCP": {
                                "$ref": "defs.json#/definitions/int64"
                            },
                            "limit": {
                                "$ref": "defs.json#/definitions/int64"
                            },
                            "reservation": {
                                "$ref": "defs.json#/definitions/int64"
                            },
                            "swap": {
                                "$ref": "defs.json#/definitions/int64"
                            },
                            "swappiness": {
                                "$ref": "defs.json#/definitions/uint64"
                            },
                            "disableOOMKiller": {
                                "type": "boolean"
                            },
                            "useHierarchy": {
                                "type": "boolean"
                            },
                            "checkBeforeUpdate": {
                                "type": "boolean"
                            }
                        }
                    },
                    "network": {
                        "type": "object",
                        "properties": {
                            "classID": {
                                "$ref": "defs.json#/definitions/uint32"
                            },
                            "priorities": {
                                "type": "array",
                                "items": {
                                    "$ref": "defs-linux.json#/definitions/NetworkInterfacePriority"
                                }
                            }
                        }
                    },
                    "rdma": {
                        "type": "object",
                        "additionalProperties": {
                            "$ref": "defs-linux.json#/definitions/Rdma"
                        }
                    }
                }
            },
            "cgroupsPath": {
                "type": "string"
            },
            "rootfsPropagation": {
                "$ref": "defs-linux.json#/definitions/RootfsPropagation"
            },
            "seccomp": {
                "type": "object",
                "properties": {
                    "defaultAction": {
                        "$ref": "defs-linux.json#/definitions/SeccompAction"
                    },
                    "defaultErrnoRet": {
                        "$ref": "defs.json#/definitions/uint32"
                    },
                    "flags": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-linux.json#/definitions/SeccompFlag"
                        }
                    },
                    "listenerPath": {
                        "type": "string"
                    },
                    "listenerMetadata": {
                        "type": "string"
                    },
                    "architectures": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-linux.json#/definitions/SeccompArch"
                        }
                    },
                    "syscalls": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-linux.json#/definitions/Syscall"
                        }
                    }
                },
                "required": [
                    "defaultAction"
                ]
            },
            "sysctl": {
                "$ref": "defs.json#/definitions/mapStringString"
            },
            "maskedPaths": {
                "$ref": "defs.json#/definitions/ArrayOfStrings"
            },
            "readonlyPaths": {
                "$ref": "defs.json#/definitions/ArrayOfStrings"
            },
            "mountLabel": {
                "type": "string"
            },
            "intelRdt": {
                "type": "object",
                "properties": {
                    "closID": {
                        "type": "string"
                    },
                    "schemata": {
                        "$ref": "defs.json#/definitions/ArrayOfStrings"
                    },
                    "l3CacheSchema": {
                        "type": "string"
                    },
                    "memBwSchema": {
                        "type": "string",
                        "pattern": "^MB:[^\\n]*$"
                    },
                    "enableMonitoring": {
                        "type": "boolean"
                    }
                }
            },
            "memoryPolicy": {
                "type": "object",
                "properties": {
                    "mode": {
                        "$ref": "defs-linux.json#/definitions/MemoryPolicyMode"
                    },
                    "nodes": {
                        "type": "string"
                    },
                    "flags": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-linux.json#/definitions/MemoryPolicyFlag"
                        }
                    }
                }
            },
            "personality": {
                "type": "object",
                "$ref": "defs-linux.json#/definitions/Personality"
            },
            "timeOffsets": {
                "type": "object",
                "properties": {
                    "boottime": {
                        "$ref": "defs-linux.json#/definitions/TimeOffsets"
                    },
                    "monotonic": {
                        "$ref": "defs-linux.json#/definitions/TimeOffsets"
                    }
                }
            }
        }
    }
}
```

## File: `schema/config-schema.json`
```json
{
    "description": "Open Container Initiative Runtime Specification Container Configuration Schema",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "ociVersion": {
            "$ref": "defs.json#/definitions/ociVersion"
        },
        "hooks": {
            "type": "object",
            "properties": {
                "prestart": {
                    "$ref": "defs.json#/definitions/ArrayOfHooks"
                },
                "createRuntime": {
                    "$ref": "defs.json#/definitions/ArrayOfHooks"
                },
                "createContainer": {
                    "$ref": "defs.json#/definitions/ArrayOfHooks"
                },
                "startContainer": {
                    "$ref": "defs.json#/definitions/ArrayOfHooks"
                },
                "poststart": {
                    "$ref": "defs.json#/definitions/ArrayOfHooks"
                },
                "poststop": {
                    "$ref": "defs.json#/definitions/ArrayOfHooks"
                }
            }
        },
        "annotations": {
            "$ref": "defs.json#/definitions/annotations"
        },
        "hostname": {
            "type": "string"
        },
        "domainname": {
            "type": "string"
        },
        "mounts": {
            "type": "array",
            "items": {
                "$ref": "defs.json#/definitions/Mount"
            }
        },
        "root": {
            "description": "Configures the container's root filesystem.",
            "type": "object",
            "required": [
                "path"
            ],
            "properties": {
                "path": {
                    "$ref": "defs.json#/definitions/FilePath"
                },
                "readonly": {
                    "type": "boolean"
                }
            }
        },
        "process": {
            "type": "object",
            "required": [
                "cwd"
            ],
            "properties": {
                "args": {
                    "$ref": "defs.json#/definitions/ArrayOfStrings"
                },
                "commandLine": {
                    "type": "string"
                },
                "consoleSize": {
                    "type": "object",
                    "required": [
                        "height",
                        "width"
                    ],
                    "properties": {
                        "height": {
                            "$ref": "defs.json#/definitions/uint64"
                        },
                        "width": {
                            "$ref": "defs.json#/definitions/uint64"
                        }
                    }
                },
                "cwd": {
                    "type": "string"
                },
                "env": {
                    "$ref": "defs.json#/definitions/Env"
                },
                "terminal": {
                    "type": "boolean"
                },
                "user": {
                    "type": "object",
                    "properties": {
                        "uid": {
                            "$ref": "defs.json#/definitions/UID"
                        },
                        "gid": {
                            "$ref": "defs.json#/definitions/GID"
                        },
                        "umask": {
                            "$ref": "defs.json#/definitions/Umask"
                        },
                        "additionalGids": {
                            "$ref": "defs.json#/definitions/ArrayOfGIDs"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                },
                "capabilities": {
                    "type": "object",
                    "properties": {
                        "bounding": {
                            "$ref": "defs.json#/definitions/ArrayOfStrings"
                        },
                        "permitted": {
                            "$ref": "defs.json#/definitions/ArrayOfStrings"
                        },
                        "effective": {
                            "$ref": "defs.json#/definitions/ArrayOfStrings"
                        },
                        "inheritable": {
                            "$ref": "defs.json#/definitions/ArrayOfStrings"
                        },
                        "ambient": {
                            "$ref": "defs.json#/definitions/ArrayOfStrings"
                        }
                    }
                },
                "apparmorProfile": {
                    "type": "string"
                },
                "oomScoreAdj": {
                    "type": "integer"
                },
                "selinuxLabel": {
                    "type": "string"
                },
                "ioPriority": {
                    "type": "object",
                    "required": [
                        "class"
                    ],
                    "properties": {
                        "class": {
                            "type": "string",
                            "enum": [
                                "IOPRIO_CLASS_RT",
                                "IOPRIO_CLASS_BE",
                                "IOPRIO_CLASS_IDLE"
                            ]
                        },
                        "priority": {
                            "$ref": "defs.json#/definitions/int32"
                        }
                    }
                },
                "noNewPrivileges": {
                    "type": "boolean"
                },
                "scheduler": {
                    "type": "object",
                    "required": [
                        "policy"
                    ],
                    "properties": {
                        "policy": {
                            "$ref": "defs-linux.json#/definitions/SchedulerPolicy"
                        },
                        "nice": {
                            "$ref": "defs.json#/definitions/int32"
                        },
                        "priority": {
                            "$ref": "defs.json#/definitions/int32"
                        },
                        "flags": {
                            "type": "array",
                            "items": {
                                "$ref": "defs-linux.json#/definitions/SchedulerFlag"
                            }
                        },
                        "runtime": {
                            "$ref": "defs.json#/definitions/uint64"
                        },
                        "deadline": {
                            "$ref": "defs.json#/definitions/uint64"
                        },
                        "period": {
                            "$ref": "defs.json#/definitions/uint64"
                        }
                    }
                },
                "rlimits": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "type",
                            "soft",
                            "hard"
                        ],
                        "properties": {
                            "hard": {
                                "$ref": "defs.json#/definitions/uint64"
                            },
                            "soft": {
                                "$ref": "defs.json#/definitions/uint64"
                            },
                            "type": {
                                "type": "string",
                                "pattern": "^RLIMIT_[A-Z]+$"
                            }
                        }
                    }
                },
                "execCPUAffinity": {
                    "type": "object",
                    "properties": {
                        "initial": {
                            "type": "string",
                            "pattern": "^[0-9, -]*$"
                        },
                        "final": {
                            "type": "string",
                            "pattern": "^[0-9, -]*$"
                        }
                    }
                }
            }
        },
        "linux": {
            "$ref": "config-linux.json#/linux"
        },
        "solaris": {
            "$ref": "config-solaris.json#/solaris"
        },
        "windows": {
            "$ref": "config-windows.json#/windows"
        },
        "vm": {
            "$ref": "config-vm.json#/vm"
        },
        "zos": {
            "$ref": "config-zos.json#/zos"
        },
        "freebsd": {
            "$ref": "config-freebsd.json#/freebsd"
        }
    },
    "required": [
        "ociVersion"
    ]
}
```

## File: `schema/config-solaris.json`
```json
{
    "solaris": {
        "description": "Solaris platform-specific configurations",
        "type": "object",
        "properties": {
            "milestone": {
                "type": "string"
            },
            "limitpriv": {
                "type": "string"
            },
            "maxShmMemory": {
                "type": "string"
            },
            "cappedCPU": {
                "type": "object",
                "properties": {
                    "ncpus": {
                        "type": "string"
                    }
                }
            },
            "cappedMemory": {
                "type": "object",
                "properties": {
                    "physical": {
                        "type": "string"
                    },
                    "swap": {
                        "type": "string"
                    }
                }
            },
            "anet": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "linkname": {
                            "type": "string"
                        },
                        "lowerLink": {
                            "type": "string"
                        },
                        "allowedAddress": {
                            "type": "string"
                        },
                        "configureAllowedAddress": {
                            "type": "string"
                        },
                        "defrouter": {
                            "type": "string"
                        },
                        "macAddress": {
                            "type": "string"
                        },
                        "linkProtection": {
                            "type": "string"
                        }
                    }
                }
            }
        }
    }
}
```

## File: `schema/config-vm.json`
```json
{
    "vm": {
        "description": "configuration for virtual-machine-based containers",
        "type": "object",
        "required": [
            "kernel"
        ],
        "properties": {
            "hypervisor": {
                "description": "hypervisor config used by VM-based containers",
                "type": "object",
                "required": [
                    "path"
                ],
                "properties": {
                    "path": {
                        "$ref": "defs.json#/definitions/FilePath"
                    },
                    "parameters": {
                        "$ref": "defs.json#/definitions/ArrayOfStrings"
                    }
                }
            },
            "kernel": {
                "description": "kernel config used by VM-based containers",
                "type": "object",
                "required": [
                    "path"
                ],
                "properties": {
                    "path": {
                        "$ref": "defs.json#/definitions/FilePath"
                    },
                    "parameters": {
                        "$ref": "defs.json#/definitions/ArrayOfStrings"
                    },
                    "initrd": {
                        "$ref": "defs.json#/definitions/FilePath"
                    }
                }
            },
            "image": {
                "description": "root image config used by VM-based containers",
                "type": "object",
                "required": [
                    "path",
                    "format"
                ],
                "properties": {
                    "path": {
                        "$ref": "defs.json#/definitions/FilePath"
                    },
                    "format": {
                        "$ref": "defs-vm.json#/definitions/RootImageFormat"
                    }
                }
            },
            "hwConfig": {
                "description": "hardware configuration for the VM image",
                "type": "object",
                "properties": {
                    "deviceTree": {
                        "$ref": "defs.json#/definitions/FilePath"
                    },
                    "vcpus": {
                        "$ref": "defs.json#/definitions/uint32"
                    },
                    "memory": {
                        "$ref": "defs.json#/definitions/uint64"
                    },
                    "dtdevs": {
                        "$ref": "defs.json#/definitions/ArrayOfStrings"
                    },
                    "iomems": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-vm.json#/definitions/IOMemEntryFormat"
                        }
                    },
                    "irqs": {
                        "$ref": "defs.json#/definitions/ArrayOfUint32"
                    }
                }
            }
        }
    }
}
```

## File: `schema/config-windows.json`
```json
{
    "windows": {
        "description": "Windows platform-specific configurations",
        "type": "object",
        "properties": {
            "layerFolders": {
                "type": "array",
                "items": {
                    "$ref": "defs.json#/definitions/FilePath"
                },
                "minItems": 1
            },
            "devices": {
                "type": "array",
                "items": {
                    "$ref": "defs-windows.json#/definitions/Device"
                }
            },
            "resources": {
                "type": "object",
                "properties": {
                    "memory": {
                        "type": "object",
                        "properties": {
                            "limit": {
                                "$ref": "defs.json#/definitions/uint64"
                            }
                        }
                    },
                    "cpu": {
                        "type": "object",
                        "properties": {
                            "count": {
                                "$ref": "defs.json#/definitions/uint64"
                            },
                            "shares": {
                                "$ref": "defs.json#/definitions/uint16"
                            },
                            "maximum": {
                                "$ref": "defs.json#/definitions/uint16"
                            },
                            "affinity": {
                                "type": "object",
                                "properties": {
                                    "mask": {
                                        "$ref": "defs.json#/definitions/uint64"
                                    },
                                    "group": {
                                        "$ref": "defs.json#/definitions/uint32"
                                    }
                                }
                            }
                        }
                    },
                    "storage": {
                        "type": "object",
                        "properties": {
                            "iops": {
                                "$ref": "defs.json#/definitions/uint64"
                            },
                            "bps": {
                                "$ref": "defs.json#/definitions/uint64"
                            },
                            "sandboxSize": {
                                "$ref": "defs.json#/definitions/uint64"
                            }
                        }
                    }
                }
            },
            "network": {
                "type": "object",
                "properties": {
                    "endpointList": {
                        "$ref": "defs.json#/definitions/ArrayOfStrings"
                    },
                    "allowUnqualifiedDNSQuery": {
                        "type": "boolean"
                    },
                    "DNSSearchList": {
                        "$ref": "defs.json#/definitions/ArrayOfStrings"
                    },
                    "networkSharedContainerName": {
                        "type": "string"
                    },
                    "networkNamespace": {
                        "type": "string"
                    }
                }
            },
            "credentialSpec": {
                "type": "object"
            },
            "servicing": {
                "type": "boolean"
            },
            "ignoreFlushesDuringBoot": {
                "type": "boolean"
            },
            "hyperv": {
                "type": "object",
                "properties": {
                    "utilityVMPath": {
                        "type": "string"
                    }
                }
            }
        },
        "required": [
            "layerFolders"
        ]
    }
}
```

## File: `schema/config-zos.json`
```json
{
    "zos": {
        "description": "z/OS platform-specific configurations",
        "type": "object",
        "properties": {
            "namespaces": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {
                            "$ref": "defs-zos.json#/definitions/NamespaceReference"
                        }
                    ]
                }
            }
        }
    }
}
```

## File: `schema/defs-freebsd.json`
```json
{
    "definitions": {
        "Device": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string"
                },
                "mode": {
                    "$ref": "defs.json#/definitions/FileMode"
                }
            }
        },
        "SharingMode": {
            "type": "string",
            "enum": [
                "disable",
                "new",
                "inherit"
            ]
        },
        "SharingModeNoDisable": {
            "type": "string",
            "enum": [
                "new",
                "inherit"
            ]
        }
    }
}
```

## File: `schema/defs-linux.json`
```json
{
    "definitions": {
        "PersonalityDomain": {
            "type": "string",
            "enum": [
                "LINUX",
                "LINUX32"
            ]
        },
        "Personality": {
            "type": "object",
            "properties": {
                "domain": {
                    "$ref": "#/definitions/PersonalityDomain"
                },
                "flags": {
                    "$ref": "defs.json#/definitions/ArrayOfStrings"
                }
            }
        },
        "RootfsPropagation": {
            "type": "string",
            "enum": [
                "private",
                "shared",
                "slave",
                "unbindable"
            ]
        },
        "SeccompArch": {
            "type": "string",
            "enum": [
                "SCMP_ARCH_X86",
                "SCMP_ARCH_X86_64",
                "SCMP_ARCH_X32",
                "SCMP_ARCH_ARM",
                "SCMP_ARCH_AARCH64",
                "SCMP_ARCH_LOONGARCH64",
                "SCMP_ARCH_M68K",
                "SCMP_ARCH_MIPS",
                "SCMP_ARCH_MIPS64",
                "SCMP_ARCH_MIPS64N32",
                "SCMP_ARCH_MIPSEL",
                "SCMP_ARCH_MIPSEL64",
                "SCMP_ARCH_MIPSEL64N32",
                "SCMP_ARCH_PPC",
                "SCMP_ARCH_PPC64",
                "SCMP_ARCH_PPC64LE",
                "SCMP_ARCH_S390",
                "SCMP_ARCH_S390X",
                "SCMP_ARCH_SH",
                "SCMP_ARCH_SHEB",
                "SCMP_ARCH_PARISC",
                "SCMP_ARCH_PARISC64",
                "SCMP_ARCH_RISCV64"
            ]
        },
        "SeccompAction": {
            "type": "string",
            "enum": [
                "SCMP_ACT_KILL",
                "SCMP_ACT_KILL_PROCESS",
                "SCMP_ACT_KILL_THREAD",
                "SCMP_ACT_TRAP",
                "SCMP_ACT_ERRNO",
                "SCMP_ACT_TRACE",
                "SCMP_ACT_ALLOW",
                "SCMP_ACT_LOG",
                "SCMP_ACT_NOTIFY"
            ]
        },
        "SeccompFlag": {
            "type": "string",
            "enum": [
                "SECCOMP_FILTER_FLAG_TSYNC",
                "SECCOMP_FILTER_FLAG_LOG",
                "SECCOMP_FILTER_FLAG_SPEC_ALLOW",
                "SECCOMP_FILTER_FLAG_WAIT_KILLABLE_RECV"
            ]
        },
        "SeccompOperators": {
            "type": "string",
            "enum": [
                "SCMP_CMP_NE",
                "SCMP_CMP_LT",
                "SCMP_CMP_LE",
                "SCMP_CMP_EQ",
                "SCMP_CMP_GE",
                "SCMP_CMP_GT",
                "SCMP_CMP_MASKED_EQ"
            ]
        },
        "SyscallArg": {
            "type": "object",
            "properties": {
                "index": {
                    "$ref": "defs.json#/definitions/uint32"
                },
                "value": {
                    "$ref": "defs.json#/definitions/uint64"
                },
                "valueTwo": {
                    "$ref": "defs.json#/definitions/uint64"
                },
                "op": {
                    "$ref": "#/definitions/SeccompOperators"
                }
            },
            "required": [
                "index",
                "value",
                "op"
            ]
        },
        "Syscall": {
            "type": "object",
            "properties": {
                "names": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "minItems": 1
                },
                "action": {
                    "$ref": "#/definitions/SeccompAction"
                },
                "errnoRet": {
                    "$ref": "defs.json#/definitions/uint32"
                },
                "args": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/SyscallArg"
                    }
                }
            },
            "required": [
                "names",
                "action"
            ]
        },
        "Major": {
            "description": "major device number",
            "$ref": "defs.json#/definitions/int64"
        },
        "Minor": {
            "description": "minor device number",
            "$ref": "defs.json#/definitions/int64"
        },
        "FileType": {
            "description": "Type of a block or special character device",
            "type": "string",
            "pattern": "^[cbup]$"
        },
        "Device": {
            "type": "object",
            "required": [
                "type",
                "path"
            ],
            "properties": {
                "type": {
                    "$ref": "#/definitions/FileType"
                },
                "path": {
                    "$ref": "defs.json#/definitions/FilePath"
                },
                "fileMode": {
                    "$ref": "defs.json#/definitions/FileMode"
                },
                "major": {
                    "$ref": "#/definitions/Major"
                },
                "minor": {
                    "$ref": "#/definitions/Minor"
                },
                "uid": {
                    "$ref": "defs.json#/definitions/UID"
                },
                "gid": {
                    "$ref": "defs.json#/definitions/GID"
                }
            }
        },
        "NetDevice": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                }
            }
        },
        "weight": {
            "$ref": "defs.json#/definitions/uint16"
        },
        "blockIODevice": {
            "type": "object",
            "properties": {
                "major": {
                    "$ref": "#/definitions/Major"
                },
                "minor": {
                    "$ref": "#/definitions/Minor"
                }
            },
            "required": [
                "major",
                "minor"
            ]
        },
        "blockIODeviceWeight": {
            "type": "object",
            "allOf": [
                {
                    "$ref": "#/definitions/blockIODevice"
                },
                {
                    "type": "object",
                    "properties": {
                        "weight": {
                            "$ref": "#/definitions/weight"
                        },
                        "leafWeight": {
                            "$ref": "#/definitions/weight"
                        }
                    }
                }
            ]
        },
        "blockIODeviceThrottle": {
            "allOf": [
                {
                    "$ref": "#/definitions/blockIODevice"
                },
                {
                    "type": "object",
                    "properties": {
                        "rate": {
                            "$ref": "defs.json#/definitions/uint64"
                        }
                    }
                }
            ]
        },
        "DeviceCgroup": {
            "type": "object",
            "properties": {
                "allow": {
                    "type": "boolean"
                },
                "type": {
                    "type": "string"
                },
                "major": {
                    "$ref": "#/definitions/Major"
                },
                "minor": {
                    "$ref": "#/definitions/Minor"
                },
                "access": {
                    "type": "string"
                }
            },
            "required": [
                "allow"
            ]
        },
        "MemoryPolicyMode": {
            "type": "string",
            "enum": [
                "MPOL_DEFAULT",
                "MPOL_BIND",
                "MPOL_INTERLEAVE",
                "MPOL_WEIGHTED_INTERLEAVE",
                "MPOL_PREFERRED",
                "MPOL_PREFERRED_MANY",
                "MPOL_LOCAL"
            ]
        },
        "MemoryPolicyFlag": {
            "type": "string",
            "enum": [
                "MPOL_F_NUMA_BALANCING",
                "MPOL_F_RELATIVE_NODES",
                "MPOL_F_STATIC_NODES"
            ]
        },
        "NetworkInterfacePriority": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "priority": {
                    "$ref": "defs.json#/definitions/uint32"
                }
            },
            "required": [
                "name",
                "priority"
            ]
        },
        "Rdma": {
            "type": "object",
            "properties": {
                "hcaHandles": {
                    "$ref": "defs.json#/definitions/uint32"
                },
                "hcaObjects": {
                    "$ref": "defs.json#/definitions/uint32"
                }
            }
        },
        "NamespaceType": {
            "type": "string",
            "enum": [
                "mount",
                "pid",
                "network",
                "uts",
                "ipc",
                "user",
                "cgroup",
                "time"
            ]
        },
        "NamespaceReference": {
            "type": "object",
            "properties": {
                "type": {
                    "$ref": "#/definitions/NamespaceType"
                },
                "path": {
                    "$ref": "defs.json#/definitions/FilePath"
                }
            },
            "required": [
                "type"
            ]
        },
        "TimeOffsets": {
            "type": "object",
            "properties": {
                "secs": {
                    "$ref": "defs.json#/definitions/int64"
                },
                "nanosecs": {
                    "$ref": "defs.json#/definitions/uint32"
                }
            }
        },
        "SchedulerPolicy": {
            "type": "string",
            "enum": [
                "SCHED_OTHER",
                "SCHED_FIFO",
                "SCHED_RR",
                "SCHED_BATCH",
                "SCHED_ISO",
                "SCHED_IDLE",
                "SCHED_DEADLINE"
            ]
        },
        "SchedulerFlag": {
            "type": "string",
            "enum": [
                "SCHED_FLAG_RESET_ON_FORK",
                "SCHED_FLAG_RECLAIM",
                "SCHED_FLAG_DL_OVERRUN",
                "SCHED_FLAG_KEEP_POLICY",
                "SCHED_FLAG_KEEP_PARAMS",
                "SCHED_FLAG_UTIL_CLAMP_MIN",
                "SCHED_FLAG_UTIL_CLAMP_MAX"
            ]
        }
    }
}
```

## File: `schema/defs-vm.json`
```json
{
    "definitions": {
        "RootImageFormat": {
            "type": "string",
            "enum": [
                "raw",
                "qcow2",
                "vdi",
                "vmdk",
                "vhd"
            ]
        },
        "IOMemEntryFormat": {
            "type": "object",
            "properties": {
                "firstGFN": {
                    "$ref": "defs.json#/definitions/uint64"
                },
                "firstMFN": {
                    "$ref": "defs.json#/definitions/uint64"
                },
                "nrMFNs": {
                    "$ref": "defs.json#/definitions/uint64"
                }
            },
            "required": [
                "firstMFN",
                "nrMFNs"
            ]
        }
    }
}
```

## File: `schema/defs-windows.json`
```json
{
    "definitions": {
        "Device": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "idType": {
                    "type": "string",
                    "enum": [
                        "class"
                    ]
                }
            },
            "required": [
                "id",
                "idType"
            ]
        }
    }
}
```

## File: `schema/defs-zos.json`
```json
{
    "definitions": {
        "NamespaceType": {
            "type": "string",
            "enum": [
                "mount",
                "pid",
                "uts",
                "ipc"
            ]
        },
        "NamespaceReference": {
            "type": "object",
            "properties": {
                "type": {
                    "$ref": "#/definitions/NamespaceType"
                },
                "path": {
                    "$ref": "defs.json#/definitions/FilePath"
                }
            },
            "required": [
                "type"
            ]
        }
    }
}
```

## File: `schema/defs.json`
```json
{
    "description": "Definitions used throughout the Open Container Initiative Runtime Specification",
    "definitions": {
        "int8": {
            "type": "integer",
            "minimum": -128,
            "maximum": 127
        },
        "int16": {
            "type": "integer",
            "minimum": -32768,
            "maximum": 32767
        },
        "int32": {
            "type": "integer",
            "minimum": -2147483648,
            "maximum": 2147483647
        },
        "int64": {
            "type": "integer",
            "minimum": -9223372036854775808,
            "maximum": 9223372036854775807
        },
        "uint8": {
            "type": "integer",
            "minimum": 0,
            "maximum": 255
        },
        "uint16": {
            "type": "integer",
            "minimum": 0,
            "maximum": 65535
        },
        "uint32": {
            "type": "integer",
            "minimum": 0,
            "maximum": 4294967295
        },
        "uint64": {
            "type": "integer",
            "minimum": 0,
            "maximum": 18446744073709551615
        },
        "percent": {
            "type": "integer",
            "minimum": 0,
            "maximum": 100
        },
        "mapStringString": {
            "type": "object",
            "patternProperties": {
                ".{1,}": {
                    "type": "string"
                }
            }
        },
        "UID": {
            "$ref": "#/definitions/uint32"
        },
        "GID": {
            "$ref": "#/definitions/uint32"
        },
        "Umask": {
            "$ref": "#/definitions/uint32"
        },
        "ArrayOfGIDs": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/GID"
            }
        },
        "ArrayOfStrings": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "ArrayOfUint32": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/uint32"
            }
        },
        "FileMode": {
            "description": "File permissions mode (in decimal, not octal)",
            "type": "integer",
            "minimum": 0,
            "maximum": 511
        },
        "FilePath": {
            "type": "string"
        },
        "Env": {
            "$ref": "#/definitions/ArrayOfStrings"
        },
        "Hook": {
            "type": "object",
            "properties": {
                "path": {
                    "$ref": "#/definitions/FilePath"
                },
                "args": {
                    "$ref": "#/definitions/ArrayOfStrings"
                },
                "env": {
                    "$ref": "#/definitions/Env"
                },
                "timeout": {
                    "type": "integer",
                    "minimum": 1
                }
            },
            "required": [
                "path"
            ]
        },
        "ArrayOfHooks": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Hook"
            }
        },
        "IDMapping": {
            "type": "object",
            "properties": {
                "containerID": {
                    "$ref": "#/definitions/uint32"
                },
                "hostID": {
                    "$ref": "#/definitions/uint32"
                },
                "size": {
                    "$ref": "#/definitions/uint32"
                }
            },
            "required": [
                "containerID",
                "hostID",
                "size"
            ]
        },
        "Mount": {
            "type": "object",
            "properties": {
                "source": {
                    "$ref": "#/definitions/FilePath"
                },
                "destination": {
                    "$ref": "#/definitions/FilePath"
                },
                "options": {
                    "$ref": "#/definitions/ArrayOfStrings"
                },
                "type": {
                    "type": "string"
                },
                "uidMappings": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/IDMapping"
                    }
                },
                "gidMappings": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/IDMapping"
                    }
                }
            },
            "required": [
                "destination"
            ]
        },
        "ociVersion": {
            "description": "The version of Open Container Initiative Runtime Specification that the document complies with",
            "type": "string"
        },
        "annotations": {
            "$ref": "#/definitions/mapStringString"
        }
    }
}
```

## File: `schema/features-linux.json`
```json
{
    "linux": {
        "description": "Linux platform-specific features",
        "type": "object",
        "properties": {
            "namespaces": {
                "type": "array",
                "items": {
                    "$ref": "defs-linux.json#/definitions/NamespaceType"
                }
            },
            "capabilities": {
                "type": "array",
                "items": {
                    "type": "string",
                    "pattern": "^CAP_[A-Z_]+$"
                }
            },
            "cgroup": {
                "type": "object",
                "properties": {
                    "v1": {
                        "type": "boolean"
                    },
                    "v2": {
                        "type": "boolean"
                    },
                    "systemd": {
                        "type": "boolean"
                    },
                    "systemdUser": {
                        "type": "boolean"
                    },
                    "rdma": {
                        "type": "boolean"
                    }
                }
            },
            "seccomp": {
                "type": "object",
                "properties": {
                    "enabled": {
                        "type": "boolean"
                    },
                    "actions": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-linux.json#/definitions/SeccompAction"
                        }
                    },
                    "operators": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-linux.json#/definitions/SeccompOperators"
                        }
                    },
                    "archs": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-linux.json#/definitions/SeccompArch"
                        }
                    },
                    "knownFlags": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-linux.json#/definitions/SeccompFlag"
                        }
                    },
                    "supportedFlags": {
                        "type": "array",
                        "items": {
                            "$ref": "defs-linux.json#/definitions/SeccompFlag"
                        }
                    }
                }
            },
            "apparmor": {
                "type": "object",
                "properties": {
                    "enabled": {
                        "type": "boolean"
                    }
                }
            },
            "selinux": {
                "type": "object",
                "properties": {
                    "enabled": {
                        "type": "boolean"
                    }
                }
            },
            "intelRdt": {
                "type": "object",
                "properties": {
                    "enabled": {
                        "type": "boolean"
                    }
                }
            },
            "mountExtensions": {
                "type": "object",
                "properties": {
                    "idmap": {
                        "type": "object",
                        "properties": {
                            "enabled": {
                                "type": "boolean"
                            }
                        }
                    }
                }
            },
            "netDevices": {
                "type": "object",
                "properties": {
                    "enabled": {
                        "type": "boolean"
                    }
                }
            }
        }
    }
}
```

## File: `schema/features-schema.json`
```json
{
    "description": "Open Container Initiative Runtime Specification Runtime Features Schema",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "ociVersionMin": {
            "$ref": "defs.json#/definitions/ociVersion"
        },
        "ociVersionMax": {
            "$ref": "defs.json#/definitions/ociVersion"
        },
        "hooks": {
            "$ref": "defs.json#/definitions/ArrayOfStrings"
        },
        "mountOptions": {
            "$ref": "defs.json#/definitions/ArrayOfStrings"
        },
        "annotations": {
            "$ref": "defs.json#/definitions/annotations"
        },
        "potentiallyUnsafeConfigAnnotations": {
            "$ref": "defs.json#/definitions/ArrayOfStrings"
        },
        "linux": {
            "$ref": "features-linux.json#/linux"
        }
    },
    "required": [
        "ociVersionMin",
        "ociVersionMax"
    ]
}
```

## File: `schema/state-schema.json`
```json
{
    "description": "Open Container Runtime State Schema",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "ociVersion": {
            "$ref": "defs.json#/definitions/ociVersion"
        },
        "id": {
            "description": "the container's ID",
            "type": "string"
        },
        "status": {
            "type": "string",
            "enum": [
                "creating",
                "created",
                "running",
                "stopped"
            ]
        },
        "pid": {
            "type": "integer",
            "minimum": 0
        },
        "bundle": {
            "type": "string"
        },
        "annotations": {
            "$ref": "defs.json#/definitions/annotations"
        }
    },
    "required": [
        "ociVersion",
        "id",
        "status",
        "bundle"
    ]
}
```

## File: `schema/validate.go`
```go
package main

import (
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"

	"github.com/xeipuuv/gojsonschema"
)

const usage = `Validate is used to check document with specified schema.
You can use validate in following ways:

   1.specify document file as an argument
      validate <schema.json> <document.json>

   2.pass document content through a pipe
      cat <document.json> | validate <schema.json>

   3.input document content manually, ended with ctrl+d(or your self-defined EOF keys)
      validate <schema.json>
      [INPUT DOCUMENT CONTENT HERE]
`

func main() {
	nargs := len(os.Args[1:])
	if nargs == 0 || nargs > 2 {
		fmt.Printf("ERROR: invalid arguments number\n\n%s\n", usage)
		os.Exit(1)
	}

	if os.Args[1] == "help" ||
		os.Args[1] == "--help" ||
		os.Args[1] == "-h" {
		fmt.Printf("%s\n", usage)
		os.Exit(1)
	}

	schemaPath := os.Args[1]
	if !strings.Contains(schemaPath, "://") {
		var err error
		schemaPath, err = formatFilePath(schemaPath)
		if err != nil {
			fmt.Printf("ERROR: invalid schema-file path: %s\n", err)
			os.Exit(1)
		}
		schemaPath = "file://" + schemaPath
	}

	schemaLoader := gojsonschema.NewReferenceLoader(schemaPath)

	var documentLoader gojsonschema.JSONLoader

	if nargs > 1 {
		documentPath, err := formatFilePath(os.Args[2])
		if err != nil {
			fmt.Printf("ERROR: invalid document-file path: %s\n", err)
			os.Exit(1)
		}
		documentLoader = gojsonschema.NewReferenceLoader("file://" + documentPath)
	} else {
		documentBytes, err := io.ReadAll(os.Stdin)
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
		documentString := string(documentBytes)
		documentLoader = gojsonschema.NewStringLoader(documentString)
	}

	result, err := gojsonschema.Validate(schemaLoader, documentLoader)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	if result.Valid() {
		fmt.Printf("The document is valid\n")
	} else {
		fmt.Printf("The document is not valid. see errors :\n")
		for _, desc := range result.Errors() {
			fmt.Printf("- %s\n", desc)
		}
		os.Exit(1)
	}
}

func formatFilePath(path string) (string, error) {
	if _, err := os.Stat(path); err != nil {
		return "", err
	}

	absPath, err := filepath.Abs(path)
	if err != nil {
		return "", err
	}
	return absPath, nil
}
```

## File: `schema/test/config/bad/freebsd-vnet-disable.json`
```json
{
    "ociVersion": "1.3.0",
    "root": {
        "path": "rootfs"
    },
    "freebsd": {
        "jail": {
            "vnet": "disable"
        }
    }
}
```

## File: `schema/test/config/bad/invalid-json.json`
```json
{]
```

## File: `schema/test/config/bad/linux-hugepage.json`
```json
{
    "ociVersion": "1.0.0",
    "root": {
        "path": "rootfs"
    },
    "linux": {
        "resources": {
            "hugepageLimits": [
                {
                    "limit": 1234123,
                    "pageSize": "64kB"
                }
            ]
        }
    }
}
```

## File: `schema/test/config/bad/linux-netdevice.json`
```json
{
    "ociVersion": "1.0.0",
    "root": {
        "path": "rootfs"
    },
    "linux": {
        "netDevices": {
            "eth0": {
                "name": 23
            }
        }
    }
}
```

## File: `schema/test/config/bad/linux-rdma.json`
```json
{
    "ociVersion": "1.0.0",
    "root": {
        "path": "rootfs"
    },
    "linux": {
        "resources": {
            "rdma": {
                "mlx5_1": {
                    "hcaHandles": "not a uint32"
                }
            }
        }
    }
}
```

## File: `schema/test/config/good/freebsd-example.json`
```json
{
    "ociVersion": "1.3.0",
    "process": {
        "terminal": true,
        "args": [
            "sh"
        ],
        "env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "TERM=xterm"
        ],
        "cwd": "/"
    },
    "root": {
        "path": "rootfs"
    },
    "hostname": "slartibartfast",
    "mounts": [
        {
            "destination": "/dev",
            "type": "devfs",
            "source": "devfs",
            "options": [
                "ruleset=4"
            ]
        },
        {
            "destination": "/dev/fd",
            "type": "fdescfs",
            "source": "fdescfs",
            "options": []
        }
    ],
    "freebsd": {
        "devices": [
            {
                "path": "pf",
                "mode": 448
            }
        ],
        "jail": {
            "host": "new",
            "vnet": "new",
            "enforceStatfs": 1,
            "allow": {
                "rawSockets": true,
                "chflags": true,
                "mount": [
                    "tmpfs"
                ]
            }
        }
    }
}
```

## File: `schema/test/config/good/freebsd-minimal.json`
```json
{
    "ociVersion": "1.3.0",
    "root": {
        "path": "rootfs"
    },
    "freebsd": {}
}
```

## File: `schema/test/config/good/linux-netdevice.json`
```json
{
    "ociVersion": "1.0.0",
    "root": {
        "path": "rootfs"
    },
    "linux": {
        "netDevices": {
            "eth0": {
                "name": "container_eth0"
            },
            "ens4": {},
            "ens5": {}
        }
    }
}
```

## File: `schema/test/config/good/linux-rdma.json`
```json
{
    "ociVersion": "1.0.0",
    "root": {
        "path": "rootfs"
    },
    "linux": {
        "resources": {
            "rdma": {
                "mlx5_1": {
                    "hcaHandles": 3,
                    "hcaObjects": 10000
                },
                "mlx4_0": {
                    "hcaObjects": 1000
                },
                "rxe3": {
                    "hcaObjects": 10000
                }
            }
        }
    }
}
```

## File: `schema/test/config/good/minimal-for-start.json`
```json
{
    "ociVersion": "1.0.0",
    "root": {
        "path": "rootfs"
    },
    "process": {
        "cwd": "/",
        "args": [
            "sh"
        ],
        "user": {
            "uid": 0,
            "gid": 0
        }
    }
}
```

## File: `schema/test/config/good/minimal.json`
```json
{
    "ociVersion": "1.0.0",
    "root": {
        "path": "rootfs"
    }
}
```

## File: `schema/test/config/good/spec-example.json`
```json
{
    "ociVersion": "0.5.0-dev",
    "process": {
        "terminal": true,
        "user": {
            "uid": 1,
            "gid": 1,
            "additionalGids": [
                5,
                6
            ]
        },
        "args": [
            "sh"
        ],
        "env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "TERM=xterm"
        ],
        "cwd": "/",
        "capabilities": {
            "bounding": [
                "CAP_AUDIT_WRITE",
                "CAP_KILL",
                "CAP_NET_BIND_SERVICE"
            ],
            "permitted": [
                "CAP_AUDIT_WRITE",
                "CAP_KILL",
                "CAP_NET_BIND_SERVICE"
            ],
            "inheritable": [
                "CAP_AUDIT_WRITE",
                "CAP_KILL",
                "CAP_NET_BIND_SERVICE"
            ],
            "effective": [
                "CAP_AUDIT_WRITE",
                "CAP_KILL"
            ],
            "ambient": [
                "CAP_NET_BIND_SERVICE"
            ]
        },
        "rlimits": [
            {
                "type": "RLIMIT_CORE",
                "hard": 1024,
                "soft": 1024
            },
            {
                "type": "RLIMIT_NOFILE",
                "hard": 1024,
                "soft": 1024
            }
        ],
        "apparmorProfile": "acme_secure_profile",
        "selinuxLabel": "system_u:system_r:svirt_lxc_net_t:s0:c124,c675",
        "noNewPrivileges": true
    },
    "root": {
        "path": "rootfs",
        "readonly": true
    },
    "hostname": "slartibartfast",
    "domainname": "foobarbaz.test",
    "mounts": [
        {
            "destination": "/proc",
            "type": "proc",
            "source": "proc"
        },
        {
            "destination": "/dev",
            "type": "tmpfs",
            "source": "tmpfs",
            "options": [
                "nosuid",
                "strictatime",
                "mode=755",
                "size=65536k"
            ]
        },
        {
            "destination": "/dev/pts",
            "type": "devpts",
            "source": "devpts",
            "options": [
                "nosuid",
                "noexec",
                "newinstance",
                "ptmxmode=0666",
                "mode=0620",
                "gid=5"
            ]
        },
        {
            "destination": "/dev/shm",
            "type": "tmpfs",
            "source": "shm",
            "options": [
                "nosuid",
                "noexec",
                "nodev",
                "mode=1777",
                "size=65536k"
            ]
        },
        {
            "destination": "/dev/mqueue",
            "type": "mqueue",
            "source": "mqueue",
            "options": [
                "nosuid",
                "noexec",
                "nodev"
            ]
        },
        {
            "destination": "/sys",
            "type": "sysfs",
            "source": "sysfs",
            "options": [
                "nosuid",
                "noexec",
                "nodev"
            ]
        },
        {
            "destination": "/sys/fs/cgroup",
            "type": "cgroup",
            "source": "cgroup",
            "options": [
                "nosuid",
                "noexec",
                "nodev",
                "relatime",
                "ro"
            ]
        }
    ],
    "hooks": {
        "prestart": [
            {
                "path": "/usr/bin/fix-mounts",
                "args": [
                    "fix-mounts",
                    "arg1",
                    "arg2"
                ],
                "env": [
                    "key1=value1"
                ]
            },
            {
                "path": "/usr/bin/setup-network"
            }
        ],
        "createRuntime": [
            {
                "path": "/usr/bin/fix-mounts",
                "args": [
                    "fix-mounts",
                    "arg1",
                    "arg2"
                ],
                "env": [
                    "key1=value1"
                ]
            },
            {
                "path": "/usr/bin/setup-network"
            }
        ],
        "createContainer": [
            {
                "path": "/usr/bin/mount-hook",
                "args": [
                    "-mount",
                    "arg1",
                    "arg2"
                ],
                "env": [
                    "key1=value1"
                ]
            }
        ],
        "startContainer": [
            {
                "path": "/usr/bin/refresh-ldcache"
            }
        ],
        "poststart": [
            {
                "path": "/usr/bin/notify-start",
                "timeout": 5
            }
        ],
        "poststop": [
            {
                "path": "/usr/sbin/cleanup.sh",
                "args": [
                    "cleanup.sh",
                    "-f"
                ]
            }
        ]
    },
    "linux": {
        "devices": [
            {
                "path": "/dev/fuse",
                "type": "c",
                "major": 10,
                "minor": 229,
                "fileMode": 438,
                "uid": 0,
                "gid": 0
            },
            {
                "path": "/dev/sda",
                "type": "b",
                "major": 8,
                "minor": 0,
                "fileMode": 432,
                "uid": 0,
                "gid": 0
            }
        ],
        "uidMappings": [
            {
                "containerID": 0,
                "hostID": 1000,
                "size": 32000
            }
        ],
        "gidMappings": [
            {
                "containerID": 0,
                "hostID": 1000,
                "size": 32000
            }
        ],
        "sysctl": {
            "net.ipv4.ip_forward": "1",
            "net.core.somaxconn": "256"
        },
        "cgroupsPath": "/myRuntime/myContainer",
        "resources": {
            "network": {
                "classID": 1048577,
                "priorities": [
                    {
                        "name": "eth0",
                        "priority": 500
                    },
                    {
                        "name": "eth1",
                        "priority": 1000
                    }
                ]
            },
            "pids": {
                "limit": 32771
            },
            "hugepageLimits": [
                {
                    "pageSize": "2MB",
                    "limit": 9223372036854772000
                },
                {
                    "pageSize": "64KB",
                    "limit": 1000000
                }
            ],
            "oomScoreAdj": 100,
            "memory": {
                "limit": 536870912,
                "reservation": 536870912,
                "swap": 536870912,
                "kernel": -1,
                "kernelTCP": -1,
                "swappiness": 0,
                "disableOOMKiller": false,
                "useHierarchy": false,
                "checkBeforeUpdate": false
            },
            "cpu": {
                "shares": 1024,
                "quota": 1000000,
                "burst": 1000000,
                "period": 500000,
                "realtimeRuntime": 950000,
                "realtimePeriod": 1000000,
                "cpus": "2-3",
                "mems": "0-7"
            },
            "devices": [
                {
                    "allow": false,
                    "access": "rwm"
                },
                {
                    "allow": true,
                    "type": "c",
                    "major": 10,
                    "minor": 229,
                    "access": "rw"
                },
                {
                    "allow": true,
                    "type": "b",
                    "major": 8,
                    "minor": 0,
                    "access": "r"
                }
            ],
            "blockIO": {
                "weight": 10,
                "leafWeight": 10,
                "weightDevice": [
                    {
                        "major": 8,
                        "minor": 0,
                        "weight": 500,
                        "leafWeight": 300
                    },
                    {
                        "major": 8,
                        "minor": 16,
                        "weight": 500
                    }
                ],
                "throttleReadBpsDevice": [
                    {
                        "major": 8,
                        "minor": 0,
                        "rate": 600
                    }
                ],
                "throttleWriteIOPSDevice": [
                    {
                        "major": 8,
                        "minor": 16,
                        "rate": 300
                    }
                ]
            }
        },
        "rootfsPropagation": "slave",
        "seccomp": {
            "defaultAction": "SCMP_ACT_ALLOW",
            "architectures": [
                "SCMP_ARCH_X86",
                "SCMP_ARCH_X32"
            ],
            "syscalls": [
                {
                    "names": [
                        "getcwd",
                        "chmod"
                    ],
                    "action": "SCMP_ACT_ERRNO"
                }
            ]
        },
        "timeOffsets": {
            "monotonic": {
                "secs": 172800,
                "nanosecs": 0
            },
            "boottime": {
                "secs": 604800,
                "nanosecs": 0
            }
        },
        "namespaces": [
            {
                "type": "pid"
            },
            {
                "type": "network"
            },
            {
                "type": "ipc"
            },
            {
                "type": "uts"
            },
            {
                "type": "mount"
            },
            {
                "type": "user"
            },
            {
                "type": "cgroup"
            },
            {
                "type": "time"
            }
        ],
        "maskedPaths": [
            "/proc/kcore",
            "/proc/latency_stats",
            "/proc/timer_stats",
            "/proc/sched_debug"
        ],
        "readonlyPaths": [
            "/proc/asound",
            "/proc/bus",
            "/proc/fs",
            "/proc/irq",
            "/proc/sys",
            "/proc/sysrq-trigger"
        ],
        "mountLabel": "system_u:object_r:svirt_sandbox_file_t:s0:c715,c811"
    },
    "annotations": {
        "com.example.key1": "value1",
        "com.example.key2": "value2"
    }
}
```

## File: `schema/test/config/good/zos-example.json`
```json
{
    "ociVersion": "0.5.0-dev",
    "process": {
        "terminal": true,
        "user": {
            "uid": 1,
            "gid": 1,
            "additionalGids": [
                5,
                6
            ]
        },
        "args": [
            "sh"
        ],
        "env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/bin",
            "TERM=xterm"
        ],
        "cwd": "/",
        "rlimits": [
            {
                "type": "RLIMIT_NOFILE",
                "hard": 1024,
                "soft": 1024
            }
        ],
        "noNewPrivileges": true
    },
    "root": {
        "path": "rootfs"
    },
    "hostname": "slartibartfast",
    "mounts": [
        {
            "destination": "/proc",
            "type": "proc",
            "source": "proc"
        },
        {
            "destination": "/dev",
            "type": "tfs",
            "source": "tmpfs",
            "options": [
                "nosuid",
                "-p 1755",
                "-s 64"
            ]
        }
    ],
    "hooks": {
        "prestart": [
            {
                "path": "/usr/bin/fix-mounts",
                "args": [
                    "fix-mounts",
                    "arg1",
                    "arg2"
                ],
                "env": [
                    "key1=value1"
                ]
            },
            {
                "path": "/usr/bin/setup-network"
            }
        ],
        "createRuntime": [
            {
                "path": "/usr/bin/fix-mounts",
                "args": [
                    "fix-mounts",
                    "arg1",
                    "arg2"
                ],
                "env": [
                    "key1=value1"
                ]
            },
            {
                "path": "/usr/bin/setup-network"
            }
        ],
        "createContainer": [
            {
                "path": "/usr/bin/mount-hook",
                "args": [
                    "-mount",
                    "arg1",
                    "arg2"
                ],
                "env": [
                    "key1=value1"
                ]
            }
        ],
        "startContainer": [
            {
                "path": "/usr/bin/refresh-ldcache"
            }
        ],
        "poststart": [
            {
                "path": "/usr/bin/notify-start",
                "timeout": 5
            }
        ],
        "poststop": [
            {
                "path": "/usr/sbin/cleanup.sh",
                "args": [
                    "cleanup.sh",
                    "-f"
                ]
            }
        ]
    },
    "zos": {
        "namespaces": [
            {
                "type": "pid"
            },
            {
                "type": "ipc"
            },
            {
                "type": "uts"
            },
            {
                "type": "mount"
            }
        ]
    },
    "annotations": {
        "com.example.key1": "value1",
        "com.example.key2": "value2"
    }
}
```

## File: `schema/test/config/good/zos-minimal.json`
```json
{
    "ociVersion": "1.0.0",
    "root": {
        "path": "rootfs"
    },
    "zos": {}
}
```

## File: `schema/test/features/bad/missing-ociVersionMax.json`
```json
{
    "ociVersionMin": "1.1.0"
}
```

## File: `schema/test/features/good/minimal.json`
```json
{
    "ociVersionMin": "1.0.0",
    "ociVersionMax": "1.1.0"
}
```

## File: `schema/test/features/good/runc.json`
```json
{
    "ociVersionMin": "1.0.0",
    "ociVersionMax": "1.0.2-dev",
    "hooks": [
        "prestart",
        "createRuntime",
        "createContainer",
        "startContainer",
        "poststart",
        "poststop"
    ],
    "mountOptions": [
        "acl",
        "async",
        "atime",
        "bind",
        "defaults",
        "dev",
        "diratime",
        "dirsync",
        "exec",
        "iversion",
        "lazytime",
        "loud",
        "mand",
        "noacl",
        "noatime",
        "nodev",
        "nodiratime",
        "noexec",
        "noiversion",
        "nolazytime",
        "nomand",
        "norelatime",
        "nostrictatime",
        "nosuid",
        "nosymfollow",
        "private",
        "ratime",
        "rbind",
        "rdev",
        "rdiratime",
        "relatime",
        "remount",
        "rexec",
        "rnoatime",
        "rnodev",
        "rnodiratime",
        "rnoexec",
        "rnorelatime",
        "rnostrictatime",
        "rnosuid",
        "rnosymfollow",
        "ro",
        "rprivate",
        "rrelatime",
        "rro",
        "rrw",
        "rshared",
        "rslave",
        "rstrictatime",
        "rsuid",
        "rsymfollow",
        "runbindable",
        "rw",
        "shared",
        "silent",
        "slave",
        "strictatime",
        "suid",
        "symfollow",
        "sync",
        "tmpcopyup",
        "unbindable"
    ],
    "linux": {
        "namespaces": [
            "cgroup",
            "ipc",
            "mount",
            "network",
            "pid",
            "user",
            "uts"
        ],
        "capabilities": [
            "CAP_CHOWN",
            "CAP_DAC_OVERRIDE",
            "CAP_DAC_READ_SEARCH",
            "CAP_FOWNER",
            "CAP_FSETID",
            "CAP_KILL",
            "CAP_SETGID",
            "CAP_SETUID",
            "CAP_SETPCAP",
            "CAP_LINUX_IMMUTABLE",
            "CAP_NET_BIND_SERVICE",
            "CAP_NET_BROADCAST",
            "CAP_NET_ADMIN",
            "CAP_NET_RAW",
            "CAP_IPC_LOCK",
            "CAP_IPC_OWNER",
            "CAP_SYS_MODULE",
            "CAP_SYS_RAWIO",
            "CAP_SYS_CHROOT",
            "CAP_SYS_PTRACE",
            "CAP_SYS_PACCT",
            "CAP_SYS_ADMIN",
            "CAP_SYS_BOOT",
            "CAP_SYS_NICE",
            "CAP_SYS_RESOURCE",
            "CAP_SYS_TIME",
            "CAP_SYS_TTY_CONFIG",
            "CAP_MKNOD",
            "CAP_LEASE",
            "CAP_AUDIT_WRITE",
            "CAP_AUDIT_CONTROL",
            "CAP_SETFCAP",
            "CAP_MAC_OVERRIDE",
            "CAP_MAC_ADMIN",
            "CAP_SYSLOG",
            "CAP_WAKE_ALARM",
            "CAP_BLOCK_SUSPEND",
            "CAP_AUDIT_READ",
            "CAP_PERFMON",
            "CAP_BPF",
            "CAP_CHECKPOINT_RESTORE"
        ],
        "cgroup": {
            "v1": true,
            "v2": true,
            "systemd": true,
            "systemdUser": true
        },
        "seccomp": {
            "enabled": true,
            "actions": [
                "SCMP_ACT_ALLOW",
                "SCMP_ACT_ERRNO",
                "SCMP_ACT_KILL",
                "SCMP_ACT_LOG",
                "SCMP_ACT_NOTIFY",
                "SCMP_ACT_TRACE",
                "SCMP_ACT_TRAP"
            ],
            "operators": [
                "SCMP_CMP_EQ",
                "SCMP_CMP_GE",
                "SCMP_CMP_GT",
                "SCMP_CMP_LE",
                "SCMP_CMP_LT",
                "SCMP_CMP_MASKED_EQ",
                "SCMP_CMP_NE"
            ],
            "archs": [
                "SCMP_ARCH_AARCH64",
                "SCMP_ARCH_ARM",
                "SCMP_ARCH_MIPS",
                "SCMP_ARCH_MIPS64",
                "SCMP_ARCH_MIPS64N32",
                "SCMP_ARCH_MIPSEL",
                "SCMP_ARCH_MIPSEL64",
                "SCMP_ARCH_MIPSEL64N32",
                "SCMP_ARCH_PPC",
                "SCMP_ARCH_PPC64",
                "SCMP_ARCH_PPC64LE",
                "SCMP_ARCH_S390",
                "SCMP_ARCH_S390X",
                "SCMP_ARCH_X32",
                "SCMP_ARCH_X86",
                "SCMP_ARCH_X86_64"
            ],
            "knownFlags": [
                "SECCOMP_FILTER_FLAG_LOG"
            ],
            "supportedFlags": [
                "SECCOMP_FILTER_FLAG_LOG"
            ]
        },
        "apparmor": {
            "enabled": true
        },
        "selinux": {
            "enabled": true
        },
        "netDevices": {
            "enabled": true
        }
    },
    "annotations": {
        "io.github.seccomp.libseccomp.version": "2.5.4",
        "org.opencontainers.runc.checkpoint.enabled": "true",
        "org.opencontainers.runc.commit": "v1.1.0-368-ga1c51c56",
        "org.opencontainers.runc.version": "1.1.0+dev"
    }
}
```

## File: `schema/test/state/bad/invalid-json.json`
```json
{]
```

## File: `schema/test/state/good/spec-example.json`
```json
{
    "ociVersion": "0.2.0",
    "id": "oci-container1",
    "status": "running",
    "pid": 4422,
    "bundle": "/containers/redis",
    "annotations": {
        "myKey": "myValue"
    }
}
```

## File: `specs-go/config.go`
```go
package specs

import "os"

// Spec is the base configuration for the container.
type Spec struct {
	// Version of the Open Container Initiative Runtime Specification with which the bundle complies.
	Version string `json:"ociVersion"`
	// Process configures the container process.
	Process *Process `json:"process,omitempty"`
	// Root configures the container's root filesystem.
	Root *Root `json:"root,omitempty"`
	// Hostname configures the container's hostname.
	Hostname string `json:"hostname,omitempty"`
	// Domainname configures the container's domainname.
	Domainname string `json:"domainname,omitempty"`
	// Mounts configures additional mounts (on top of Root).
	Mounts []Mount `json:"mounts,omitempty"`
	// Hooks configures callbacks for container lifecycle events.
	Hooks *Hooks `json:"hooks,omitempty" platform:"linux,solaris,zos"`
	// Annotations contains arbitrary metadata for the container.
	Annotations map[string]string `json:"annotations,omitempty"`

	// Linux is platform-specific configuration for Linux based containers.
	Linux *Linux `json:"linux,omitempty" platform:"linux"`
	// Solaris is platform-specific configuration for Solaris based containers.
	Solaris *Solaris `json:"solaris,omitempty" platform:"solaris"`
	// Windows is platform-specific configuration for Windows based containers.
	Windows *Windows `json:"windows,omitempty" platform:"windows"`
	// VM specifies configuration for virtual-machine-based containers.
	VM *VM `json:"vm,omitempty" platform:"vm"`
	// ZOS is platform-specific configuration for z/OS based containers.
	ZOS *ZOS `json:"zos,omitempty" platform:"zos"`
	// FreeBSD is platform-specific configuration for FreeBSD based containers.
	FreeBSD *FreeBSD `json:"freebsd,omitempty" platform:"freebsd"`
}

// Scheduler represents the scheduling attributes for a process. It is based on
// the Linux sched_setattr(2) syscall.
type Scheduler struct {
	// Policy represents the scheduling policy (e.g., SCHED_FIFO, SCHED_RR, SCHED_OTHER).
	Policy LinuxSchedulerPolicy `json:"policy"`

	// Nice is the nice value for the process, which affects its priority.
	Nice int32 `json:"nice,omitempty"`

	// Priority represents the static priority of the process.
	Priority int32 `json:"priority,omitempty"`

	// Flags is an array of scheduling flags.
	Flags []LinuxSchedulerFlag `json:"flags,omitempty"`

	// The following ones are used by the DEADLINE scheduler.

	// Runtime is the amount of time in nanoseconds during which the process
	// is allowed to run in a given period.
	Runtime uint64 `json:"runtime,omitempty"`

	// Deadline is the absolute deadline for the process to complete its execution.
	Deadline uint64 `json:"deadline,omitempty"`

	// Period is the length of the period in nanoseconds used for determining the process runtime.
	Period uint64 `json:"period,omitempty"`
}

// Process contains information to start a specific application inside the container.
type Process struct {
	// Terminal creates an interactive terminal for the container.
	Terminal bool `json:"terminal,omitempty"`
	// ConsoleSize specifies the size of the console.
	ConsoleSize *Box `json:"consoleSize,omitempty"`
	// User specifies user information for the process.
	User User `json:"user"`
	// Args specifies the binary and arguments for the application to execute.
	Args []string `json:"args,omitempty"`
	// CommandLine specifies the full command line for the application to execute on Windows.
	CommandLine string `json:"commandLine,omitempty" platform:"windows"`
	// Env populates the process environment for the process.
	Env []string `json:"env,omitempty"`
	// Cwd is the current working directory for the process and must be
	// relative to the container's root.
	Cwd string `json:"cwd"`
	// Capabilities are Linux capabilities that are kept for the process.
	Capabilities *LinuxCapabilities `json:"capabilities,omitempty" platform:"linux"`
	// Rlimits specifies rlimit options to apply to the process.
	Rlimits []POSIXRlimit `json:"rlimits,omitempty" platform:"linux,solaris,zos"`
	// NoNewPrivileges controls whether additional privileges could be gained by processes in the container.
	NoNewPrivileges bool `json:"noNewPrivileges,omitempty" platform:"linux,zos"`
	// ApparmorProfile specifies the apparmor profile for the container.
	ApparmorProfile string `json:"apparmorProfile,omitempty" platform:"linux"`
	// Specify an oom_score_adj for the container.
	OOMScoreAdj *int `json:"oomScoreAdj,omitempty" platform:"linux"`
	// Scheduler specifies the scheduling attributes for a process
	Scheduler *Scheduler `json:"scheduler,omitempty" platform:"linux"`
	// SelinuxLabel specifies the selinux context that the container process is run as.
	SelinuxLabel string `json:"selinuxLabel,omitempty" platform:"linux"`
	// IOPriority contains the I/O priority settings for the cgroup.
	IOPriority *LinuxIOPriority `json:"ioPriority,omitempty" platform:"linux"`
	// ExecCPUAffinity specifies CPU affinity for exec processes.
	ExecCPUAffinity *CPUAffinity `json:"execCPUAffinity,omitempty" platform:"linux"`
}

// LinuxCapabilities specifies the list of allowed capabilities that are kept for a process.
// https://man7.org/linux/man-pages/man7/capabilities.7.html
type LinuxCapabilities struct {
	// Bounding is the set of capabilities checked by the kernel.
	Bounding []string `json:"bounding,omitempty" platform:"linux"`
	// Effective is the set of capabilities checked by the kernel.
	Effective []string `json:"effective,omitempty" platform:"linux"`
	// Inheritable is the capabilities preserved across execve.
	Inheritable []string `json:"inheritable,omitempty" platform:"linux"`
	// Permitted is the limiting superset for effective capabilities.
	Permitted []string `json:"permitted,omitempty" platform:"linux"`
	// Ambient is the ambient set of capabilities that are kept.
	Ambient []string `json:"ambient,omitempty" platform:"linux"`
}

// IOPriority represents I/O priority settings for the container's processes within the process group.
type LinuxIOPriority struct {
	Class    IOPriorityClass `json:"class"`
	Priority int             `json:"priority"`
}

// IOPriorityClass represents an I/O scheduling class.
type IOPriorityClass string

// Possible values for IOPriorityClass.
const (
	IOPRIO_CLASS_RT   IOPriorityClass = "IOPRIO_CLASS_RT"
	IOPRIO_CLASS_BE   IOPriorityClass = "IOPRIO_CLASS_BE"
	IOPRIO_CLASS_IDLE IOPriorityClass = "IOPRIO_CLASS_IDLE"
)

// CPUAffinity specifies process' CPU affinity.
type CPUAffinity struct {
	Initial string `json:"initial,omitempty"`
	Final   string `json:"final,omitempty"`
}

// Box specifies dimensions of a rectangle. Used for specifying the size of a console.
type Box struct {
	// Height is the vertical dimension of a box.
	Height uint `json:"height"`
	// Width is the horizontal dimension of a box.
	Width uint `json:"width"`
}

// User specifies specific user (and group) information for the container process.
type User struct {
	// UID is the user id.
	UID uint32 `json:"uid" platform:"linux,solaris,zos"`
	// GID is the group id.
	GID uint32 `json:"gid" platform:"linux,solaris,zos"`
	// Umask is the umask for the init process.
	Umask *uint32 `json:"umask,omitempty" platform:"linux,solaris,zos"`
	// AdditionalGids are additional group ids set for the container's process.
	AdditionalGids []uint32 `json:"additionalGids,omitempty" platform:"linux,solaris"`
	// Username is the user name.
	Username string `json:"username,omitempty" platform:"windows"`
}

// Root contains information about the container's root filesystem on the host.
type Root struct {
	// Path is the absolute path to the container's root filesystem.
	Path string `json:"path"`
	// Readonly makes the root filesystem for the container readonly before the process is executed.
	Readonly bool `json:"readonly,omitempty"`
}

// Mount specifies a mount for a container.
type Mount struct {
	// Destination is the absolute path where the mount will be placed in the container.
	Destination string `json:"destination"`
	// Type specifies the mount kind.
	Type string `json:"type,omitempty" platform:"linux,solaris,zos,freebsd"`
	// Source specifies the source path of the mount.
	Source string `json:"source,omitempty"`
	// Options are fstab style mount options.
	Options []string `json:"options,omitempty"`

	// UID/GID mappings used for changing file owners w/o calling chown, fs should support it.
	// Every mount point could have its own mapping.
	UIDMappings []LinuxIDMapping `json:"uidMappings,omitempty" platform:"linux"`
	GIDMappings []LinuxIDMapping `json:"gidMappings,omitempty" platform:"linux"`
}

// Hook specifies a command that is run at a particular event in the lifecycle of a container
type Hook struct {
	Path    string   `json:"path"`
	Args    []string `json:"args,omitempty"`
	Env     []string `json:"env,omitempty"`
	Timeout *int     `json:"timeout,omitempty"`
}

// Hooks specifies a command that is run in the container at a particular event in the lifecycle of a container
// Hooks for container setup and teardown
type Hooks struct {
	// Prestart is Deprecated. Prestart is a list of hooks to be run before the container process is executed.
	// It is called in the Runtime Namespace
	//
	// Deprecated: use [Hooks.CreateRuntime], [Hooks.CreateContainer], and
	// [Hooks.StartContainer] instead, which allow more granular hook control
	// during the create and start phase.
	Prestart []Hook `json:"prestart,omitempty"`
	// CreateRuntime is a list of hooks to be run after the container has been created but before pivot_root or any equivalent operation has been called
	// It is called in the Runtime Namespace
	CreateRuntime []Hook `json:"createRuntime,omitempty"`
	// CreateContainer is a list of hooks to be run after the container has been created but before pivot_root or any equivalent operation has been called
	// It is called in the Container Namespace
	CreateContainer []Hook `json:"createContainer,omitempty"`
	// StartContainer is a list of hooks to be run after the start operation is called but before the container process is started
	// It is called in the Container Namespace
	StartContainer []Hook `json:"startContainer,omitempty"`
	// Poststart is a list of hooks to be run after the container process is started.
	// It is called in the Runtime Namespace
	Poststart []Hook `json:"poststart,omitempty"`
	// Poststop is a list of hooks to be run after the container process exits.
	// It is called in the Runtime Namespace
	Poststop []Hook `json:"poststop,omitempty"`
}

// Linux contains platform-specific configuration for Linux based containers.
type Linux struct {
	// UIDMapping specifies user mappings for supporting user namespaces.
	UIDMappings []LinuxIDMapping `json:"uidMappings,omitempty"`
	// GIDMapping specifies group mappings for supporting user namespaces.
	GIDMappings []LinuxIDMapping `json:"gidMappings,omitempty"`
	// Sysctl are a set of key value pairs that are set for the container on start
	Sysctl map[string]string `json:"sysctl,omitempty"`
	// Resources contain cgroup information for handling resource constraints
	// for the container
	Resources *LinuxResources `json:"resources,omitempty"`
	// CgroupsPath specifies the path to cgroups that are created and/or joined by the container.
	// The path is expected to be relative to the cgroups mountpoint.
	// If resources are specified, the cgroups at CgroupsPath will be updated based on resources.
	CgroupsPath string `json:"cgroupsPath,omitempty"`
	// Namespaces contains the namespaces that are created and/or joined by the container
	Namespaces []LinuxNamespace `json:"namespaces,omitempty"`
	// Devices are a list of device nodes that are created for the container
	Devices []LinuxDevice `json:"devices,omitempty"`
	// NetDevices are key-value pairs, keyed by network device name on the host, moved to the container's network namespace.
	NetDevices map[string]LinuxNetDevice `json:"netDevices,omitempty"`
	// Seccomp specifies the seccomp security settings for the container.
	Seccomp *LinuxSeccomp `json:"seccomp,omitempty"`
	// RootfsPropagation is the rootfs mount propagation mode for the container.
	RootfsPropagation string `json:"rootfsPropagation,omitempty"`
	// MaskedPaths masks over the provided paths inside the container.
	MaskedPaths []string `json:"maskedPaths,omitempty"`
	// ReadonlyPaths sets the provided paths as RO inside the container.
	ReadonlyPaths []string `json:"readonlyPaths,omitempty"`
	// MountLabel specifies the selinux context for the mounts in the container.
	MountLabel string `json:"mountLabel,omitempty"`
	// IntelRdt contains Intel Resource Director Technology (RDT) information for
	// handling resource constraints and monitoring metrics (e.g., L3 cache, memory bandwidth) for the container
	IntelRdt *LinuxIntelRdt `json:"intelRdt,omitempty"`
	// MemoryPolicy contains NUMA memory policy for the container.
	MemoryPolicy *LinuxMemoryPolicy `json:"memoryPolicy,omitempty"`
	// Personality contains configuration for the Linux personality syscall
	Personality *LinuxPersonality `json:"personality,omitempty"`
	// TimeOffsets specifies the offset for supporting time namespaces.
	TimeOffsets map[string]LinuxTimeOffset `json:"timeOffsets,omitempty"`
}

// LinuxNamespace is the configuration for a Linux namespace
type LinuxNamespace struct {
	// Type is the type of namespace
	Type LinuxNamespaceType `json:"type"`
	// Path is a path to an existing namespace persisted on disk that can be joined
	// and is of the same type
	Path string `json:"path,omitempty"`
}

// LinuxNamespaceType is one of the Linux namespaces
type LinuxNamespaceType string

const (
	// PIDNamespace for isolating process IDs
	PIDNamespace LinuxNamespaceType = "pid"
	// NetworkNamespace for isolating network devices, stacks, ports, etc
	NetworkNamespace LinuxNamespaceType = "network"
	// MountNamespace for isolating mount points
	MountNamespace LinuxNamespaceType = "mount"
	// IPCNamespace for isolating System V IPC, POSIX message queues
	IPCNamespace LinuxNamespaceType = "ipc"
	// UTSNamespace for isolating hostname and NIS domain name
	UTSNamespace LinuxNamespaceType = "uts"
	// UserNamespace for isolating user and group IDs
	UserNamespace LinuxNamespaceType = "user"
	// CgroupNamespace for isolating cgroup hierarchies
	CgroupNamespace LinuxNamespaceType = "cgroup"
	// TimeNamespace for isolating the clocks
	TimeNamespace LinuxNamespaceType = "time"
)

// LinuxIDMapping specifies UID/GID mappings
type LinuxIDMapping struct {
	// ContainerID is the starting UID/GID in the container
	ContainerID uint32 `json:"containerID"`
	// HostID is the starting UID/GID on the host to be mapped to 'ContainerID'
	HostID uint32 `json:"hostID"`
	// Size is the number of IDs to be mapped
	Size uint32 `json:"size"`
}

// LinuxTimeOffset specifies the offset for Time Namespace
type LinuxTimeOffset struct {
	// Secs is the offset of clock (in secs) in the container
	Secs int64 `json:"secs,omitempty"`
	// Nanosecs is the additional offset for Secs (in nanosecs)
	Nanosecs uint32 `json:"nanosecs,omitempty"`
}

// POSIXRlimit type and restrictions
type POSIXRlimit struct {
	// Type of the rlimit to set
	Type string `json:"type"`
	// Hard is the hard limit for the specified type
	Hard uint64 `json:"hard"`
	// Soft is the soft limit for the specified type
	Soft uint64 `json:"soft"`
}

// LinuxHugepageLimit structure corresponds to limiting kernel hugepages.
// Default to reservation limits if supported. Otherwise fallback to page fault limits.
type LinuxHugepageLimit struct {
	// Pagesize is the hugepage size.
	// Format: "<size><unit-prefix>B' (e.g. 64KB, 2MB, 1GB, etc.).
	Pagesize string `json:"pageSize"`
	// Limit is the limit of "hugepagesize" hugetlb reservations (if supported) or usage.
	Limit uint64 `json:"limit"`
}

// LinuxInterfacePriority for network interfaces
type LinuxInterfacePriority struct {
	// Name is the name of the network interface
	Name string `json:"name"`
	// Priority for the interface
	Priority uint32 `json:"priority"`
}

// LinuxBlockIODevice holds major:minor format supported in blkio cgroup
type LinuxBlockIODevice struct {
	// Major is the device's major number.
	Major int64 `json:"major"`
	// Minor is the device's minor number.
	Minor int64 `json:"minor"`
}

// LinuxWeightDevice struct holds a `major:minor weight` pair for weightDevice
type LinuxWeightDevice struct {
	LinuxBlockIODevice
	// Weight is the bandwidth rate for the device.
	Weight *uint16 `json:"weight,omitempty"`
	// LeafWeight is the bandwidth rate for the device while competing with the cgroup's child cgroups, CFQ scheduler only
	LeafWeight *uint16 `json:"leafWeight,omitempty"`
}

// LinuxThrottleDevice struct holds a `major:minor rate_per_second` pair
type LinuxThrottleDevice struct {
	LinuxBlockIODevice
	// Rate is the IO rate limit per cgroup per device
	Rate uint64 `json:"rate"`
}

// LinuxBlockIO for Linux cgroup 'blkio' resource management
type LinuxBlockIO struct {
	// Specifies per cgroup weight
	Weight *uint16 `json:"weight,omitempty"`
	// Specifies tasks' weight in the given cgroup while competing with the cgroup's child cgroups, CFQ scheduler only
	LeafWeight *uint16 `json:"leafWeight,omitempty"`
	// Weight per cgroup per device, can override BlkioWeight
	WeightDevice []LinuxWeightDevice `json:"weightDevice,omitempty"`
	// IO read rate limit per cgroup per device, bytes per second
	ThrottleReadBpsDevice []LinuxThrottleDevice `json:"throttleReadBpsDevice,omitempty"`
	// IO write rate limit per cgroup per device, bytes per second
	ThrottleWriteBpsDevice []LinuxThrottleDevice `json:"throttleWriteBpsDevice,omitempty"`
	// IO read rate limit per cgroup per device, IO per second
	ThrottleReadIOPSDevice []LinuxThrottleDevice `json:"throttleReadIOPSDevice,omitempty"`
	// IO write rate limit per cgroup per device, IO per second
	ThrottleWriteIOPSDevice []LinuxThrottleDevice `json:"throttleWriteIOPSDevice,omitempty"`
}

// LinuxMemory for Linux cgroup 'memory' resource management
type LinuxMemory struct {
	// Memory limit (in bytes).
	Limit *int64 `json:"limit,omitempty"`
	// Memory reservation or soft_limit (in bytes).
	Reservation *int64 `json:"reservation,omitempty"`
	// Total memory limit (memory + swap).
	Swap *int64 `json:"swap,omitempty"`
	// Kernel memory limit (in bytes).
	//
	// Deprecated: kernel-memory limits are not supported in cgroups v2, and
	// were obsoleted in [kernel v5.4]. This field should no longer be used,
	// as it may be ignored by runtimes.
	//
	// [kernel v5.4]: https://github.com/torvalds/linux/commit/0158115f702b0ba208ab0
	Kernel *int64 `json:"kernel,omitempty"`
	// Kernel memory limit for tcp (in bytes)
	KernelTCP *int64 `json:"kernelTCP,omitempty"`
	// How aggressive the kernel will swap memory pages.
	Swappiness *uint64 `json:"swappiness,omitempty"`
	// DisableOOMKiller disables the OOM killer for out of memory conditions
	DisableOOMKiller *bool `json:"disableOOMKiller,omitempty"`
	// Enables hierarchical memory accounting
	UseHierarchy *bool `json:"useHierarchy,omitempty"`
	// CheckBeforeUpdate enables checking if a new memory limit is lower
	// than the current usage during update, and if so, rejecting the new
	// limit.
	CheckBeforeUpdate *bool `json:"checkBeforeUpdate,omitempty"`
}

// LinuxCPU for Linux cgroup 'cpu' resource management
type LinuxCPU struct {
	// CPU shares (relative weight (ratio) vs. other cgroups with cpu shares).
	Shares *uint64 `json:"shares,omitempty"`
	// CPU hardcap limit (in usecs). Allowed cpu time in a given period.
	Quota *int64 `json:"quota,omitempty"`
	// CPU hardcap burst limit (in usecs). Allowed accumulated cpu time additionally for burst in a
	// given period.
	Burst *uint64 `json:"burst,omitempty"`
	// CPU period to be used for hardcapping (in usecs).
	Period *uint64 `json:"period,omitempty"`
	// How much time realtime scheduling may use (in usecs).
	RealtimeRuntime *int64 `json:"realtimeRuntime,omitempty"`
	// CPU period to be used for realtime scheduling (in usecs).
	RealtimePeriod *uint64 `json:"realtimePeriod,omitempty"`
	// CPUs to use within the cpuset. Default is to use any CPU available.
	Cpus string `json:"cpus,omitempty"`
	// List of memory nodes in the cpuset. Default is to use any available memory node.
	Mems string `json:"mems,omitempty"`
	// cgroups are configured with minimum weight, 0: default behavior, 1: SCHED_IDLE.
	Idle *int64 `json:"idle,omitempty"`
}

// LinuxPids for Linux cgroup 'pids' resource management (Linux 4.3)
type LinuxPids struct {
	// Maximum number of PIDs. Default is "no limit".
	Limit *int64 `json:"limit,omitempty"`
}

// LinuxNetwork identification and priority configuration
type LinuxNetwork struct {
	// Set class identifier for container's network packets
	ClassID *uint32 `json:"classID,omitempty"`
	// Set priority of network traffic for container
	Priorities []LinuxInterfacePriority `json:"priorities,omitempty"`
}

// LinuxRdma for Linux cgroup 'rdma' resource management (Linux 4.11)
type LinuxRdma struct {
	// Maximum number of HCA handles that can be opened. Default is "no limit".
	HcaHandles *uint32 `json:"hcaHandles,omitempty"`
	// Maximum number of HCA objects that can be created. Default is "no limit".
	HcaObjects *uint32 `json:"hcaObjects,omitempty"`
}

// LinuxResources has container runtime resource constraints
type LinuxResources struct {
	// Devices configures the device allowlist.
	Devices []LinuxDeviceCgroup `json:"devices,omitempty"`
	// Memory restriction configuration
	Memory *LinuxMemory `json:"memory,omitempty"`
	// CPU resource restriction configuration
	CPU *LinuxCPU `json:"cpu,omitempty"`
	// Task resource restriction configuration.
	Pids *LinuxPids `json:"pids,omitempty"`
	// BlockIO restriction configuration
	BlockIO *LinuxBlockIO `json:"blockIO,omitempty"`
	// Hugetlb limits (in bytes). Default to reservation limits if supported.
	HugepageLimits []LinuxHugepageLimit `json:"hugepageLimits,omitempty"`
	// Network restriction configuration
	Network *LinuxNetwork `json:"network,omitempty"`
	// Rdma resource restriction configuration.
	// Limits are a set of key value pairs that define RDMA resource limits,
	// where the key is device name and value is resource limits.
	Rdma map[string]LinuxRdma `json:"rdma,omitempty"`
	// Unified resources.
	Unified map[string]string `json:"unified,omitempty"`
}

// LinuxDevice represents the mknod information for a Linux special device file
type LinuxDevice struct {
	// Path to the device.
	Path string `json:"path"`
	// Device type, block, char, etc.
	Type string `json:"type"`
	// Major is the device's major number.
	Major int64 `json:"major"`
	// Minor is the device's minor number.
	Minor int64 `json:"minor"`
	// FileMode permission bits for the device.
	FileMode *os.FileMode `json:"fileMode,omitempty"`
	// UID of the device.
	UID *uint32 `json:"uid,omitempty"`
	// Gid of the device.
	GID *uint32 `json:"gid,omitempty"`
}

// LinuxNetDevice represents a single network device to be added to the container's network namespace
type LinuxNetDevice struct {
	// Name of the device in the container namespace
	Name string `json:"name,omitempty"`
}

// LinuxDeviceCgroup represents a device rule for the devices specified to
// the device controller
type LinuxDeviceCgroup struct {
	// Allow or deny
	Allow bool `json:"allow"`
	// Device type, block, char, etc.
	Type string `json:"type,omitempty"`
	// Major is the device's major number.
	Major *int64 `json:"major,omitempty"`
	// Minor is the device's minor number.
	Minor *int64 `json:"minor,omitempty"`
	// Cgroup access permissions format, rwm.
	Access string `json:"access,omitempty"`
}

// LinuxPersonalityDomain refers to a personality domain.
type LinuxPersonalityDomain string

// LinuxPersonalityFlag refers to an additional personality flag. None are currently defined.
type LinuxPersonalityFlag string

// Define domain and flags for Personality
const (
	// PerLinux is the standard Linux personality
	PerLinux LinuxPersonalityDomain = "LINUX"
	// PerLinux32 sets personality to 32 bit
	PerLinux32 LinuxPersonalityDomain = "LINUX32"
)

// LinuxPersonality represents the Linux personality syscall input
type LinuxPersonality struct {
	// Domain for the personality
	Domain LinuxPersonalityDomain `json:"domain"`
	// Additional flags
	Flags []LinuxPersonalityFlag `json:"flags,omitempty"`
}

// Solaris contains platform-specific configuration for Solaris application containers.
type Solaris struct {
	// SMF FMRI which should go "online" before we start the container process.
	Milestone string `json:"milestone,omitempty"`
	// Maximum set of privileges any process in this container can obtain.
	LimitPriv string `json:"limitpriv,omitempty"`
	// The maximum amount of shared memory allowed for this container.
	MaxShmMemory string `json:"maxShmMemory,omitempty"`
	// Specification for automatic creation of network resources for this container.
	Anet []SolarisAnet `json:"anet,omitempty"`
	// Set limit on the amount of CPU time that can be used by container.
	CappedCPU *SolarisCappedCPU `json:"cappedCPU,omitempty"`
	// The physical and swap caps on the memory that can be used by this container.
	CappedMemory *SolarisCappedMemory `json:"cappedMemory,omitempty"`
}

// SolarisCappedCPU allows users to set limit on the amount of CPU time that can be used by container.
type SolarisCappedCPU struct {
	Ncpus string `json:"ncpus,omitempty"`
}

// SolarisCappedMemory allows users to set the physical and swap caps on the memory that can be used by this container.
type SolarisCappedMemory struct {
	Physical string `json:"physical,omitempty"`
	Swap     string `json:"swap,omitempty"`
}

// SolarisAnet provides the specification for automatic creation of network resources for this container.
type SolarisAnet struct {
	// Specify a name for the automatically created VNIC datalink.
	Linkname string `json:"linkname,omitempty"`
	// Specify the link over which the VNIC will be created.
	Lowerlink string `json:"lowerLink,omitempty"`
	// The set of IP addresses that the container can use.
	Allowedaddr string `json:"allowedAddress,omitempty"`
	// Specifies whether allowedAddress limitation is to be applied to the VNIC.
	Configallowedaddr string `json:"configureAllowedAddress,omitempty"`
	// The value of the optional default router.
	Defrouter string `json:"defrouter,omitempty"`
	// Enable one or more types of link protection.
	Linkprotection string `json:"linkProtection,omitempty"`
	// Set the VNIC's macAddress
	Macaddress string `json:"macAddress,omitempty"`
}

// Windows defines the runtime configuration for Windows based containers, including Hyper-V containers.
type Windows struct {
	// LayerFolders contains a list of absolute paths to directories containing image layers.
	LayerFolders []string `json:"layerFolders"`
	// Devices are the list of devices to be mapped into the container.
	Devices []WindowsDevice `json:"devices,omitempty"`
	// Resources contains information for handling resource constraints for the container.
	Resources *WindowsResources `json:"resources,omitempty"`
	// CredentialSpec contains a JSON object describing a group Managed Service Account (gMSA) specification.
	CredentialSpec interface{} `json:"credentialSpec,omitempty"`
	// Servicing indicates if the container is being started in a mode to apply a Windows Update servicing operation.
	Servicing bool `json:"servicing,omitempty"`
	// IgnoreFlushesDuringBoot indicates if the container is being started in a mode where disk writes are not flushed during its boot process.
	IgnoreFlushesDuringBoot bool `json:"ignoreFlushesDuringBoot,omitempty"`
	// HyperV contains information for running a container with Hyper-V isolation.
	HyperV *WindowsHyperV `json:"hyperv,omitempty"`
	// Network restriction configuration.
	Network *WindowsNetwork `json:"network,omitempty"`
}

// WindowsDevice represents information about a host device to be mapped into the container.
type WindowsDevice struct {
	// Device identifier: interface class GUID, etc.
	ID string `json:"id"`
	// Device identifier type: "class", etc.
	IDType string `json:"idType"`
}

// WindowsResources has container runtime resource constraints for containers running on Windows.
type WindowsResources struct {
	// Memory restriction configuration.
	Memory *WindowsMemoryResources `json:"memory,omitempty"`
	// CPU resource restriction configuration.
	CPU *WindowsCPUResources `json:"cpu,omitempty"`
	// Storage restriction configuration.
	Storage *WindowsStorageResources `json:"storage,omitempty"`
}

// WindowsMemoryResources contains memory resource management settings.
type WindowsMemoryResources struct {
	// Memory limit in bytes.
	Limit *uint64 `json:"limit,omitempty"`
}

// WindowsCPUResources contains CPU resource management settings.
type WindowsCPUResources struct {
	// Count is the number of CPUs available to the container. It represents the
	// fraction of the configured processor `count` in a container in relation
	// to the processors available in the host. The fraction ultimately
	// determines the portion of processor cycles that the threads in a
	// container can use during each scheduling interval, as the number of
	// cycles per 10,000 cycles.
	Count *uint64 `json:"count,omitempty"`
	// Shares limits the share of processor time given to the container relative
	// to other workloads on the processor. The processor `shares` (`weight` at
	// the platform level) is a value between 0 and 10000.
	Shares *uint16 `json:"shares,omitempty"`
	// Maximum determines the portion of processor cycles that the threads in a
	// container can use during each scheduling interval, as the number of
	// cycles per 10,000 cycles. Set processor `maximum` to a percentage times
	// 100.
	Maximum *uint16 `json:"maximum,omitempty"`
	// Set of CPUs to affinitize for this container.
	Affinity []WindowsCPUGroupAffinity `json:"affinity,omitempty"`
}

// Similar to _GROUP_AFFINITY struct defined in
// https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/miniport/ns-miniport-_group_affinity
type WindowsCPUGroupAffinity struct {
	// CPU mask relative to this CPU group.
	Mask uint64 `json:"mask,omitempty"`
	// Processor group the mask refers to, as returned by GetLogicalProcessorInformationEx.
	Group uint32 `json:"group,omitempty"`
}

// WindowsStorageResources contains storage resource management settings.
type WindowsStorageResources struct {
	// Specifies maximum Iops for the system drive.
	Iops *uint64 `json:"iops,omitempty"`
	// Specifies maximum bytes per second for the system drive.
	Bps *uint64 `json:"bps,omitempty"`
	// Sandbox size specifies the minimum size of the system drive in bytes.
	SandboxSize *uint64 `json:"sandboxSize,omitempty"`
}

// WindowsNetwork contains network settings for Windows containers.
type WindowsNetwork struct {
	// List of HNS endpoints that the container should connect to.
	EndpointList []string `json:"endpointList,omitempty"`
	// Specifies if unqualified DNS name resolution is allowed.
	AllowUnqualifiedDNSQuery bool `json:"allowUnqualifiedDNSQuery,omitempty"`
	// Comma separated list of DNS suffixes to use for name resolution.
	DNSSearchList []string `json:"DNSSearchList,omitempty"`
	// Name (ID) of the container that we will share with the network stack.
	NetworkSharedContainerName string `json:"networkSharedContainerName,omitempty"`
	// name (ID) of the network namespace that will be used for the container.
	NetworkNamespace string `json:"networkNamespace,omitempty"`
}

// WindowsHyperV contains information for configuring a container to run with Hyper-V isolation.
type WindowsHyperV struct {
	// UtilityVMPath is an optional path to the image used for the Utility VM.
	UtilityVMPath string `json:"utilityVMPath,omitempty"`
}

// IOMems contains information about iomem addresses that should be passed to the VM.
type IOMems struct {
	// Guest Frame Number to map the iomem range. If GFN is not specified, the mapping will be done to the same Frame Number as was provided in FirstMFN.
	FirstGFN *uint64 `json:"firstGFN,omitempty"`
	// Physical page number of iomem regions.
	FirstMFN *uint64 `json:"firstMFN"`
	// Number of pages to be mapped.
	NrMFNs *uint64 `json:"nrMFNs"`
}

// Hardware configuration for the VM image
type HWConfig struct {
	// Path to the container device-tree file that should be passed to the VM configuration.
	DeviceTree string `json:"deviceTree,omitempty"`
	// Number of virtual cpus for the VM.
	VCPUs *uint32 `json:"vcpus,omitempty"`
	// Maximum memory in bytes allocated to the VM.
	Memory *uint64 `json:"memory,omitempty"`
	// Host device tree nodes to passthrough to the VM.
	DtDevs []string `json:"dtdevs,omitempty"`
	// Allow auto-translated domains to access specific hardware I/O memory pages.
	IOMems []IOMems `json:"iomems,omitempty"`
	// Allows VM to access specific physical IRQs.
	Irqs []uint32 `json:"irqs,omitempty"`
}

// VM contains information for virtual-machine-based containers.
type VM struct {
	// Hypervisor specifies hypervisor-related configuration for virtual-machine-based containers.
	Hypervisor VMHypervisor `json:"hypervisor,omitempty"`
	// Kernel specifies kernel-related configuration for virtual-machine-based containers.
	Kernel VMKernel `json:"kernel"`
	// Image specifies guest image related configuration for virtual-machine-based containers.
	Image VMImage `json:"image,omitempty"`
	// Hardware configuration that should be passed to the VM.
	HwConfig *HWConfig `json:"hwconfig,omitempty"`
}

// VMHypervisor contains information about the hypervisor to use for a virtual machine.
type VMHypervisor struct {
	// Path is the host path to the hypervisor used to manage the virtual machine.
	Path string `json:"path"`
	// Parameters specifies parameters to pass to the hypervisor.
	Parameters []string `json:"parameters,omitempty"`
}

// VMKernel contains information about the kernel to use for a virtual machine.
type VMKernel struct {
	// Path is the host path to the kernel used to boot the virtual machine.
	Path string `json:"path"`
	// Parameters specifies parameters to pass to the kernel.
	Parameters []string `json:"parameters,omitempty"`
	// InitRD is the host path to an initial ramdisk to be used by the kernel.
	InitRD string `json:"initrd,omitempty"`
}

// VMImage contains information about the virtual machine root image.
type VMImage struct {
	// Path is the host path to the root image that the VM kernel would boot into.
	Path string `json:"path"`
	// Format is the root image format type (e.g. "qcow2", "raw", "vhd", etc).
	Format string `json:"format"`
}

// LinuxSeccomp represents syscall restrictions
type LinuxSeccomp struct {
	DefaultAction    LinuxSeccompAction `json:"defaultAction"`
	DefaultErrnoRet  *uint              `json:"defaultErrnoRet,omitempty"`
	Architectures    []Arch             `json:"architectures,omitempty"`
	Flags            []LinuxSeccompFlag `json:"flags,omitempty"`
	ListenerPath     string             `json:"listenerPath,omitempty"`
	ListenerMetadata string             `json:"listenerMetadata,omitempty"`
	Syscalls         []LinuxSyscall     `json:"syscalls,omitempty"`
}

// Arch used for additional architectures
type Arch string

// LinuxSeccompFlag is a flag to pass to seccomp(2).
type LinuxSeccompFlag string

const (
	// LinuxSeccompFlagLog is a seccomp flag to request all returned
	// actions except SECCOMP_RET_ALLOW to be logged. An administrator may
	// override this filter flag by preventing specific actions from being
	// logged via the /proc/sys/kernel/seccomp/actions_logged file. (since
	// Linux 4.14)
	LinuxSeccompFlagLog LinuxSeccompFlag = "SECCOMP_FILTER_FLAG_LOG"

	// LinuxSeccompFlagSpecAllow can be used to disable Speculative Store
	// Bypass mitigation. (since Linux 4.17)
	LinuxSeccompFlagSpecAllow LinuxSeccompFlag = "SECCOMP_FILTER_FLAG_SPEC_ALLOW"

	// LinuxSeccompFlagWaitKillableRecv can be used to switch to the wait
	// killable semantics. (since Linux 5.19)
	LinuxSeccompFlagWaitKillableRecv LinuxSeccompFlag = "SECCOMP_FILTER_FLAG_WAIT_KILLABLE_RECV"
)

// Additional architectures permitted to be used for system calls
// By default only the native architecture of the kernel is permitted
const (
	ArchX86         Arch = "SCMP_ARCH_X86"
	ArchX86_64      Arch = "SCMP_ARCH_X86_64"
	ArchX32         Arch = "SCMP_ARCH_X32"
	ArchARM         Arch = "SCMP_ARCH_ARM"
	ArchAARCH64     Arch = "SCMP_ARCH_AARCH64"
	ArchMIPS        Arch = "SCMP_ARCH_MIPS"
	ArchMIPS64      Arch = "SCMP_ARCH_MIPS64"
	ArchMIPS64N32   Arch = "SCMP_ARCH_MIPS64N32"
	ArchMIPSEL      Arch = "SCMP_ARCH_MIPSEL"
	ArchMIPSEL64    Arch = "SCMP_ARCH_MIPSEL64"
	ArchMIPSEL64N32 Arch = "SCMP_ARCH_MIPSEL64N32"
	ArchPPC         Arch = "SCMP_ARCH_PPC"
	ArchPPC64       Arch = "SCMP_ARCH_PPC64"
	ArchPPC64LE     Arch = "SCMP_ARCH_PPC64LE"
	ArchS390        Arch = "SCMP_ARCH_S390"
	ArchS390X       Arch = "SCMP_ARCH_S390X"
	ArchPARISC      Arch = "SCMP_ARCH_PARISC"
	ArchPARISC64    Arch = "SCMP_ARCH_PARISC64"
	ArchRISCV64     Arch = "SCMP_ARCH_RISCV64"
	ArchLOONGARCH64 Arch = "SCMP_ARCH_LOONGARCH64"
	ArchM68K        Arch = "SCMP_ARCH_M68K"
	ArchSH          Arch = "SCMP_ARCH_SH"
	ArchSHEB        Arch = "SCMP_ARCH_SHEB"
)

// LinuxSeccompAction taken upon Seccomp rule match
type LinuxSeccompAction string

// Define actions for Seccomp rules
const (
	ActKill        LinuxSeccompAction = "SCMP_ACT_KILL"
	ActKillProcess LinuxSeccompAction = "SCMP_ACT_KILL_PROCESS"
	ActKillThread  LinuxSeccompAction = "SCMP_ACT_KILL_THREAD"
	ActTrap        LinuxSeccompAction = "SCMP_ACT_TRAP"
	ActErrno       LinuxSeccompAction = "SCMP_ACT_ERRNO"
	ActTrace       LinuxSeccompAction = "SCMP_ACT_TRACE"
	ActAllow       LinuxSeccompAction = "SCMP_ACT_ALLOW"
	ActLog         LinuxSeccompAction = "SCMP_ACT_LOG"
	ActNotify      LinuxSeccompAction = "SCMP_ACT_NOTIFY"
)

// LinuxSeccompOperator used to match syscall arguments in Seccomp
type LinuxSeccompOperator string

// Define operators for syscall arguments in Seccomp
const (
	OpNotEqual     LinuxSeccompOperator = "SCMP_CMP_NE"
	OpLessThan     LinuxSeccompOperator = "SCMP_CMP_LT"
	OpLessEqual    LinuxSeccompOperator = "SCMP_CMP_LE"
	OpEqualTo      LinuxSeccompOperator = "SCMP_CMP_EQ"
	OpGreaterEqual LinuxSeccompOperator = "SCMP_CMP_GE"
	OpGreaterThan  LinuxSeccompOperator = "SCMP_CMP_GT"
	OpMaskedEqual  LinuxSeccompOperator = "SCMP_CMP_MASKED_EQ"
)

// LinuxSeccompArg used for matching specific syscall arguments in Seccomp
type LinuxSeccompArg struct {
	Index    uint                 `json:"index"`
	Value    uint64               `json:"value"`
	ValueTwo uint64               `json:"valueTwo,omitempty"`
	Op       LinuxSeccompOperator `json:"op"`
}

// LinuxSyscall is used to match a syscall in Seccomp
type LinuxSyscall struct {
	Names    []string           `json:"names"`
	Action   LinuxSeccompAction `json:"action"`
	ErrnoRet *uint              `json:"errnoRet,omitempty"`
	Args     []LinuxSeccompArg  `json:"args,omitempty"`
}

// LinuxIntelRdt has container runtime resource constraints for Intel RDT CAT and MBA
// features and flags enabling Intel RDT CMT and MBM features.
// Intel RDT features are available in Linux 4.14 and newer kernel versions.
type LinuxIntelRdt struct {
	// The identity for RDT Class of Service
	ClosID string `json:"closID,omitempty"`

	// Schemata specifies the complete schemata to be written as is to the
	// schemata file in resctrl fs. Each element represents a single line in the schemata file.
	// NOTE: This will overwrite schemas specified in the L3CacheSchema and/or
	// MemBwSchema fields.
	Schemata []string `json:"schemata,omitempty"`

	// The schema for L3 cache id and capacity bitmask (CBM)
	// Format: "L3:<cache_id0>=<cbm0>;<cache_id1>=<cbm1>;..."
	// NOTE: Should not be specified if Schemata is non-empty.
	L3CacheSchema string `json:"l3CacheSchema,omitempty"`

	// The schema of memory bandwidth per L3 cache id
	// Format: "MB:<cache_id0>=bandwidth0;<cache_id1>=bandwidth1;..."
	// The unit of memory bandwidth is specified in "percentages" by
	// default, and in "MBps" if MBA Software Controller is enabled.
	// NOTE: Should not be specified if Schemata is non-empty.
	MemBwSchema string `json:"memBwSchema,omitempty"`

	// EnableMonitoring enables resctrl monitoring for the container. This will
	// create a dedicated resctrl monitoring group for the container.
	EnableMonitoring bool `json:"enableMonitoring,omitempty"`
}

// LinuxMemoryPolicy represents input for the set_mempolicy syscall.
type LinuxMemoryPolicy struct {
	// Mode for the set_mempolicy syscall.
	Mode MemoryPolicyModeType `json:"mode"`

	// Nodes representing the nodemask for the set_mempolicy syscall in comma separated ranges format.
	// Format: "<node0>-<node1>,<node2>,<node3>-<node4>,..."
	Nodes string `json:"nodes,omitempty"`

	// Flags for the set_mempolicy syscall.
	Flags []MemoryPolicyFlagType `json:"flags,omitempty"`
}

// ZOS contains platform-specific configuration for z/OS based containers.
type ZOS struct {
	// Namespaces contains the namespaces that are created and/or joined by the container
	Namespaces []ZOSNamespace `json:"namespaces,omitempty"`
}

// ZOSNamespace is the configuration for a z/OS namespace
type ZOSNamespace struct {
	// Type is the type of namespace
	Type ZOSNamespaceType `json:"type"`
	// Path is a path to an existing namespace persisted on disk that can be joined
	// and is of the same type
	Path string `json:"path,omitempty"`
}

// ZOSNamespaceType is one of the z/OS namespaces
type ZOSNamespaceType string

const (
	// PIDNamespace for isolating process IDs
	ZOSPIDNamespace ZOSNamespaceType = "pid"
	// MountNamespace for isolating mount points
	ZOSMountNamespace ZOSNamespaceType = "mount"
	// IPCNamespace for isolating System V IPC, POSIX message queues
	ZOSIPCNamespace ZOSNamespaceType = "ipc"
	// UTSNamespace for isolating hostname and NIS domain name
	ZOSUTSNamespace ZOSNamespaceType = "uts"
)

type MemoryPolicyModeType string

const (
	MpolDefault            MemoryPolicyModeType = "MPOL_DEFAULT"
	MpolBind               MemoryPolicyModeType = "MPOL_BIND"
	MpolInterleave         MemoryPolicyModeType = "MPOL_INTERLEAVE"
	MpolWeightedInterleave MemoryPolicyModeType = "MPOL_WEIGHTED_INTERLEAVE"
	MpolPreferred          MemoryPolicyModeType = "MPOL_PREFERRED"
	MpolPreferredMany      MemoryPolicyModeType = "MPOL_PREFERRED_MANY"
	MpolLocal              MemoryPolicyModeType = "MPOL_LOCAL"
)

type MemoryPolicyFlagType string

const (
	MpolFNumaBalancing MemoryPolicyFlagType = "MPOL_F_NUMA_BALANCING"
	MpolFRelativeNodes MemoryPolicyFlagType = "MPOL_F_RELATIVE_NODES"
	MpolFStaticNodes   MemoryPolicyFlagType = "MPOL_F_STATIC_NODES"
)

// LinuxSchedulerPolicy represents different scheduling policies used with the Linux Scheduler
type LinuxSchedulerPolicy string

const (
	// SchedOther is the default scheduling policy
	SchedOther LinuxSchedulerPolicy = "SCHED_OTHER"
	// SchedFIFO is the First-In-First-Out scheduling policy
	SchedFIFO LinuxSchedulerPolicy = "SCHED_FIFO"
	// SchedRR is the Round-Robin scheduling policy
	SchedRR LinuxSchedulerPolicy = "SCHED_RR"
	// SchedBatch is the Batch scheduling policy
	SchedBatch LinuxSchedulerPolicy = "SCHED_BATCH"
	// SchedISO is the Isolation scheduling policy
	SchedISO LinuxSchedulerPolicy = "SCHED_ISO"
	// SchedIdle is the Idle scheduling policy
	SchedIdle LinuxSchedulerPolicy = "SCHED_IDLE"
	// SchedDeadline is the Deadline scheduling policy
	SchedDeadline LinuxSchedulerPolicy = "SCHED_DEADLINE"
)

// LinuxSchedulerFlag represents the flags used by the Linux Scheduler.
type LinuxSchedulerFlag string

const (
	// SchedFlagResetOnFork represents the reset on fork scheduling flag
	SchedFlagResetOnFork LinuxSchedulerFlag = "SCHED_FLAG_RESET_ON_FORK"
	// SchedFlagReclaim represents the reclaim scheduling flag
	SchedFlagReclaim LinuxSchedulerFlag = "SCHED_FLAG_RECLAIM"
	// SchedFlagDLOverrun represents the deadline overrun scheduling flag
	SchedFlagDLOverrun LinuxSchedulerFlag = "SCHED_FLAG_DL_OVERRUN"
	// SchedFlagKeepPolicy represents the keep policy scheduling flag
	SchedFlagKeepPolicy LinuxSchedulerFlag = "SCHED_FLAG_KEEP_POLICY"
	// SchedFlagKeepParams represents the keep parameters scheduling flag
	SchedFlagKeepParams LinuxSchedulerFlag = "SCHED_FLAG_KEEP_PARAMS"
	// SchedFlagUtilClampMin represents the utilization clamp minimum scheduling flag
	SchedFlagUtilClampMin LinuxSchedulerFlag = "SCHED_FLAG_UTIL_CLAMP_MIN"
	// SchedFlagUtilClampMax represents the utilization clamp maximum scheduling flag
	SchedFlagUtilClampMax LinuxSchedulerFlag = "SCHED_FLAG_UTIL_CLAMP_MAX"
)

// FreeBSD contains platform-specific configuration for FreeBSD based containers.
type FreeBSD struct {
	// Devices which are accessible in the container
	Devices []FreeBSDDevice `json:"devices,omitempty"`
	// Jail definition for this container
	Jail *FreeBSDJail `json:"jail,omitempty"`
}

type FreeBSDDevice struct {
	// Path to the device, relative to /dev.
	Path string `json:"path"`
	// FileMode permission bits for the device.
	Mode *os.FileMode `json:"mode,omitempty"`
}

// FreeBSDJail describes how to configure the container's jail
type FreeBSDJail struct {
	// Parent jail name - this can be used to share a single vnet
	// across several containers
	Parent string `json:"parent,omitempty"`
	// Whether to use parent UTS names or override in the container
	Host FreeBSDSharing `json:"host,omitempty"`
	// IPv4 address sharing for the container
	Ip4 FreeBSDSharing `json:"ip4,omitempty"`
	// IPv4 addresses for the container
	Ip4Addr []string `json:"ip4Addr,omitempty"`
	// IPv6 address sharing for the container
	Ip6 FreeBSDSharing `json:"ip6,omitempty"`
	// IPv6 addresses for the container
	Ip6Addr []string `json:"ip6Addr,omitempty"`
	// Which network stack to use for the container
	Vnet FreeBSDSharing `json:"vnet,omitempty"`
	// If set, Ip4Addr and Ip6Addr addresses will be added to this interface
	Interface string `json:"interface,omitempty"`
	// List interfaces to be moved to the container's vnet
	VnetInterfaces []string `json:"vnetInterfaces,omitempty"`
	// SystemV IPC message sharing for the container
	SysVMsg FreeBSDSharing `json:"sysvmsg,omitempty"`
	// SystemV semaphore message sharing for the container
	SysVSem FreeBSDSharing `json:"sysvsem,omitempty"`
	// SystemV memory sharing for the container
	SysVShm FreeBSDSharing `json:"sysvshm,omitempty"`
	// Mount visibility (see jail(8) for details)
	EnforceStatfs *int `json:"enforceStatfs,omitempty"`
	// Jail capabilities
	Allow *FreeBSDJailAllow `json:"allow,omitempty"`
}

// These values are used to control access to features in the container, either
// disabling the feature, sharing state with the parent or creating new private
// state in the container.
type FreeBSDSharing string

const (
	FreeBSDShareDisable FreeBSDSharing = "disable"
	FreeBSDShareNew     FreeBSDSharing = "new"
	FreeBSDShareInherit FreeBSDSharing = "inherit"
)

// FreeBSDJailAllow describes jail capabilities
type FreeBSDJailAllow struct {
	SetHostname   bool     `json:"setHostname,omitempty"`
	RawSockets    bool     `json:"rawSockets,omitempty"`
	Chflags       bool     `json:"chflags,omitempty"`
	Mount         []string `json:"mount,omitempty"`
	Quotas        bool     `json:"quotas,omitempty"`
	SocketAf      bool     `json:"socketAf,omitempty"`
	Mlock         bool     `json:"mlock,omitempty"`
	ReservedPorts bool     `json:"reservedPorts,omitempty"`
	Suser         bool     `json:"suser,omitempty"`
}
```

## File: `specs-go/state.go`
```go
package specs

// ContainerState represents the state of a container.
type ContainerState string

const (
	// StateCreating indicates that the container is being created
	StateCreating ContainerState = "creating"

	// StateCreated indicates that the runtime has finished the create operation
	StateCreated ContainerState = "created"

	// StateRunning indicates that the container process has executed the
	// user-specified program but has not exited
	StateRunning ContainerState = "running"

	// StateStopped indicates that the container process has exited
	StateStopped ContainerState = "stopped"
)

// State holds information about the runtime state of the container.
type State struct {
	// Version is the version of the specification that is supported.
	Version string `json:"ociVersion"`
	// ID is the container ID
	ID string `json:"id"`
	// Status is the runtime status of the container.
	Status ContainerState `json:"status"`
	// Pid is the process ID for the container process.
	Pid int `json:"pid,omitempty"`
	// Bundle is the path to the container's bundle directory.
	Bundle string `json:"bundle"`
	// Annotations are key values associated with the container.
	Annotations map[string]string `json:"annotations,omitempty"`
}

const (
	// SeccompFdName is the name of the seccomp notify file descriptor.
	SeccompFdName string = "seccompFd"
)

// ContainerProcessState holds information about the state of a container process.
type ContainerProcessState struct {
	// Version is the version of the specification that is supported.
	Version string `json:"ociVersion"`
	// Fds is a string array containing the names of the file descriptors passed.
	// The index of the name in this array corresponds to index of the file
	// descriptor in the `SCM_RIGHTS` array.
	Fds []string `json:"fds"`
	// Pid is the process ID as seen by the runtime.
	Pid int `json:"pid"`
	// Opaque metadata.
	Metadata string `json:"metadata,omitempty"`
	// State of the container.
	State State `json:"state"`
}
```

## File: `specs-go/version.go`
```go
package specs

import "fmt"

const (
	// VersionMajor is for an API incompatible changes
	VersionMajor = 1
	// VersionMinor is for functionality in a backwards-compatible manner
	VersionMinor = 3
	// VersionPatch is for backwards-compatible bug fixes
	VersionPatch = 0

	// VersionDev indicates development branch. Releases will be empty string.
	VersionDev = "+dev"
)

// Version is the specification version that the package types support.
var Version = fmt.Sprintf("%d.%d.%d%s", VersionMajor, VersionMinor, VersionPatch, VersionDev)
```

## File: `specs-go/features/features.go`
```go
// Package features provides the Features struct.
package features

// Features represents the supported features of the runtime.
type Features struct {
	// OCIVersionMin is the minimum OCI Runtime Spec version recognized by the runtime, e.g., "1.0.0".
	OCIVersionMin string `json:"ociVersionMin,omitempty"`

	// OCIVersionMax is the maximum OCI Runtime Spec version recognized by the runtime, e.g., "1.0.2-dev".
	OCIVersionMax string `json:"ociVersionMax,omitempty"`

	// Hooks is the list of the recognized hook names, e.g., "createRuntime".
	// Nil value means "unknown", not "no support for any hook".
	Hooks []string `json:"hooks,omitempty"`

	// MountOptions is the list of the recognized mount options, e.g., "ro".
	// Nil value means "unknown", not "no support for any mount option".
	// This list does not contain filesystem-specific options passed to mount(2) syscall as (const void *).
	MountOptions []string `json:"mountOptions,omitempty"`

	// Linux is specific to Linux.
	Linux *Linux `json:"linux,omitempty"`

	// Annotations contains implementation-specific annotation strings,
	// such as the implementation version, and third-party extensions.
	Annotations map[string]string `json:"annotations,omitempty"`

	// PotentiallyUnsafeConfigAnnotations the list of the potential unsafe annotations
	// that may appear in `config.json`.
	//
	// A value that ends with "." is interpreted as a prefix of annotations.
	PotentiallyUnsafeConfigAnnotations []string `json:"potentiallyUnsafeConfigAnnotations,omitempty"`
}

// Linux is specific to Linux.
type Linux struct {
	// Namespaces is the list of the recognized namespaces, e.g., "mount".
	// Nil value means "unknown", not "no support for any namespace".
	Namespaces []string `json:"namespaces,omitempty"`

	// Capabilities is the list of the recognized capabilities , e.g., "CAP_SYS_ADMIN".
	// Nil value means "unknown", not "no support for any capability".
	Capabilities []string `json:"capabilities,omitempty"`

	Cgroup          *Cgroup          `json:"cgroup,omitempty"`
	Seccomp         *Seccomp         `json:"seccomp,omitempty"`
	Apparmor        *Apparmor        `json:"apparmor,omitempty"`
	Selinux         *Selinux         `json:"selinux,omitempty"`
	IntelRdt        *IntelRdt        `json:"intelRdt,omitempty"`
	MemoryPolicy    *MemoryPolicy    `json:"memoryPolicy,omitempty"`
	MountExtensions *MountExtensions `json:"mountExtensions,omitempty"`
	NetDevices      *NetDevices      `json:"netDevices,omitempty"`
}

// Cgroup represents the "cgroup" field.
type Cgroup struct {
	// V1 represents whether Cgroup v1 support is compiled in.
	// Unrelated to whether the host uses cgroup v1 or not.
	// Nil value means "unknown", not "false".
	V1 *bool `json:"v1,omitempty"`

	// V2 represents whether Cgroup v2 support is compiled in.
	// Unrelated to whether the host uses cgroup v2 or not.
	// Nil value means "unknown", not "false".
	V2 *bool `json:"v2,omitempty"`

	// Systemd represents whether systemd-cgroup support is compiled in.
	// Unrelated to whether the host uses systemd or not.
	// Nil value means "unknown", not "false".
	Systemd *bool `json:"systemd,omitempty"`

	// SystemdUser represents whether user-scoped systemd-cgroup support is compiled in.
	// Unrelated to whether the host uses systemd or not.
	// Nil value means "unknown", not "false".
	SystemdUser *bool `json:"systemdUser,omitempty"`

	// Rdma represents whether RDMA cgroup support is compiled in.
	// Unrelated to whether the host supports RDMA or not.
	// Nil value means "unknown", not "false".
	Rdma *bool `json:"rdma,omitempty"`
}

// Seccomp represents the "seccomp" field.
type Seccomp struct {
	// Enabled is true if seccomp support is compiled in.
	// Nil value means "unknown", not "false".
	Enabled *bool `json:"enabled,omitempty"`

	// Actions is the list of the recognized actions, e.g., "SCMP_ACT_NOTIFY".
	// Nil value means "unknown", not "no support for any action".
	Actions []string `json:"actions,omitempty"`

	// Operators is the list of the recognized operators, e.g., "SCMP_CMP_NE".
	// Nil value means "unknown", not "no support for any operator".
	Operators []string `json:"operators,omitempty"`

	// Archs is the list of the recognized archs, e.g., "SCMP_ARCH_X86_64".
	// Nil value means "unknown", not "no support for any arch".
	Archs []string `json:"archs,omitempty"`

	// KnownFlags is the list of the recognized filter flags, e.g., "SECCOMP_FILTER_FLAG_LOG".
	// Nil value means "unknown", not "no flags are recognized".
	KnownFlags []string `json:"knownFlags,omitempty"`

	// SupportedFlags is the list of the supported filter flags, e.g., "SECCOMP_FILTER_FLAG_LOG".
	// This list may be a subset of KnownFlags due to some flags
	// not supported by the current kernel and/or libseccomp.
	// Nil value means "unknown", not "no flags are supported".
	SupportedFlags []string `json:"supportedFlags,omitempty"`
}

// Apparmor represents the "apparmor" field.
type Apparmor struct {
	// Enabled is true if AppArmor support is compiled in.
	// Unrelated to whether the host supports AppArmor or not.
	// Nil value means "unknown", not "false".
	Enabled *bool `json:"enabled,omitempty"`
}

// Selinux represents the "selinux" field.
type Selinux struct {
	// Enabled is true if SELinux support is compiled in.
	// Unrelated to whether the host supports SELinux or not.
	// Nil value means "unknown", not "false".
	Enabled *bool `json:"enabled,omitempty"`
}

// IntelRdt represents the "intelRdt" field.
type IntelRdt struct {
	// Enabled is true if Intel RDT support is compiled in.
	// Unrelated to whether the host supports Intel RDT or not.
	// Nil value means "unknown", not "false".
	Enabled *bool `json:"enabled,omitempty"`
	// Schemata is true if the "linux.intelRdt.enableMonitoring" field of the
	// spec is implemented.
	Schemata *bool `json:"schemata,omitempty"`
	// Monitoring is true if the "linux.intelRdt.enableMonitoring" field of the
	// spec is implemented.
	// Nil value means "unknown", not "false".
	Monitoring *bool `json:"monitoring,omitempty"`
}

// MemoryPolicy represents the "memoryPolicy" field.
type MemoryPolicy struct {
	// modes is the list of known memory policy modes, e.g., "MPOL_INTERLEAVE".
	Modes []string `json:"modes,omitempty"`
	// flags is the list of known memory policy mode flags, e.g., "MPOL_F_STATIC_NODES".
	Flags []string `json:"flags,omitempty"`
}

// MountExtensions represents the "mountExtensions" field.
type MountExtensions struct {
	// IDMap represents the status of idmap mounts support.
	IDMap *IDMap `json:"idmap,omitempty"`
}

type IDMap struct {
	// Enabled represents whether idmap mounts supports is compiled in.
	// Unrelated to whether the host supports it or not.
	// Nil value means "unknown", not "false".
	Enabled *bool `json:"enabled,omitempty"`
}

// NetDevices represents the "netDevices" field.
type NetDevices struct {
	// Enabled is true if network devices support is compiled in.
	// Nil value means "unknown", not "false".
	Enabled *bool `json:"enabled,omitempty"`
}
```

