---
id: github.com-pixlcore-xysat-353c0ea6-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:13.277866
---

# KNOWLEDGE EXTRACT: github.com_pixlcore_xysat_353c0ea6
> **Extracted on:** 2026-04-01 16:09:59
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524947/github.com_pixlcore_xysat_353c0ea6

---

## File: `CHANGELOG.md`
```markdown
# xySat Changelog

## Version v1.0.15

> March 31, 2026

- [`2fa2b96`](https://github.com/pixlcore/xysat/commit/2fa2b96b65828eef2ab3f74829582b0b45795989): Version 1.0.15
	- Bump pixl-server to v1.0.50 for more detailed crash logs.
	- Bump pixl-tools to v2.0.2 for upstream vuln fix in picomatch.
- [`05e9d3d`](https://github.com/pixlcore/xysat/commit/05e9d3dde698285f7e5998a22f50229441e535db): Add very basic config validation on startup.
- [`939dcee`](https://github.com/pixlcore/xysat/commit/939dcee0e22b7eb2f54b79d41cbf3f8dd96a9e5c): Improve container-start.sh to honor XYSAT_config_file env var.

## Version v1.0.14

> March 23, 2026

- [`56b23c1`](https://github.com/pixlcore/xysat/commit/56b23c129e151a867a1d6538c47076f1019ade44): Version 1.0.14
- [`fca55f8`](https://github.com/pixlcore/xysat/commit/fca55f8eaa9dd1db93db0635de65ed7372dcffc0): Allow user to specify which config keys can be updated by the conductor (managed_keys).
- [`dd84eb4`](https://github.com/pixlcore/xysat/commit/dd84eb4e4ec06f9e70803f65f21003ba0b61a58a): Security Hardening: HTTP Request Plugin: Redact secrets in diagnostic output detail (best effort).
- [`098750d`](https://github.com/pixlcore/xysat/commit/098750d560aeb9dd9eab6acd9306415f29ab7b73): Support optional XYSAT_config_file env var for custom config file location.
- [`8dc4b49`](https://github.com/pixlcore/xysat/commit/8dc4b49d321c3c7508462831255590e6a7b612d7): Shell Plugin: Use Satellite's official temp_dir instead of hard-coding one.  Fixes #5.

## Version v1.0.13

> March 20, 2026

- [`87b1019`](https://github.com/pixlcore/xysat/commit/87b1019355a87b099b3d2acee3dc9c0a1ba0985a): Version 1.0.13
	- Bump systeminformation to 5.31.5 for latest macOS updates.
- [`3d8195d`](https://github.com/pixlcore/xysat/commit/3d8195df61344f7f7095b8fe86e10bdbb1091ec5): Bug Fix: Use new socket secure flag from actual socket rather than config, when constructing HTTP URLs back to the conductor.  Ref: pixlcore/xyops#213

## Version v1.0.12

> March 6, 2026

- [`75148c9`](https://github.com/pixlcore/xysat/commit/75148c9ac8481a58315d168c4c13933ba7e4d9fc): Version 1.0.12
- [`2ec4316`](https://github.com/pixlcore/xysat/commit/2ec43169fc7546c9e6b22d03ec65e54fe6de9395): HTTP/Test Plugins: Stop trying to load xysat config.json file, use airgap config now present in job data.
- [`e3a38a2`](https://github.com/pixlcore/xysat/commit/e3a38a2dedadc52dde5446dafdce337946e3fc16): Pass airgap config to child processes if set.
- [`15d8fb0`](https://github.com/pixlcore/xysat/commit/15d8fb03768bb60cb69cff6f7c6295b4aa0a1bb9): Shell Plugin: Do not try to load the xysat config.json file, as this is not readable as a non-root users.
- [`3287fa3`](https://github.com/pixlcore/xysat/commit/3287fa3196141bb8a46a1eb0f222308c61048fb0): Set permissions of temp dir to 777 on startup, for plugins to run as non-root users.

## Version v1.0.11

> March 2, 2026

- [`72bbbd5`](https://github.com/pixlcore/xysat/commit/72bbbd5215f5734ca34fa325770e9fe5d270b28d): Version 1.0.11
	- Bump pixl-request to v2.6.1 for retryDelayMax feature.
- [`649a253`](https://github.com/pixlcore/xysat/commit/649a253f1929e084d81f10e7acee6acdb6bff7d8): Network Robustness: Big refactor of networking code in regards to finishing jobs and uploading files, to better handle unstable networks.
- [`63a646e`](https://github.com/pixlcore/xysat/commit/63a646eb63de388f3094ac718b9cbf37a17390be): Introduce separate `http_file_opts` config prop for file upload and download settings (timeouts / retries).  Add retryDelayMax.
- [`0330e4a`](https://github.com/pixlcore/xysat/commit/0330e4a315f70c21884588de207cd3bc4a25923c): Add SECURITY.md file.

## Version v1.0.10

> February 28, 2026

- [`a6d0296`](https://github.com/pixlcore/xysat/commit/a6d0296b04f7e59ad348952728c4013b10826f17): Allow job file upload retries and retryDelay to be configurable in socket_opts object.
- [`7d8b8cf`](https://github.com/pixlcore/xysat/commit/7d8b8cf71ee3d6314e5f0959c8c63b257c2bfca8): Version 1.0.10
- [`60f0e3f`](https://github.com/pixlcore/xysat/commit/60f0e3f21f2e4c91c932e64da8eaca410e9a44c3): Upload Job Files: Log perf metrics on HTTP error (debug level 9).
- [`e5dede2`](https://github.com/pixlcore/xysat/commit/e5dede2fec1c13934764c864fbf0621543d0d16a): Socket Ping Death: Ensure socket immediately closes by calling terminate() on the underlying WS handle.

## Version v1.0.9

> February 28, 2026

- [`548bda4`](https://github.com/pixlcore/xysat/commit/548bda460d51633a2ed960493cbf40380f50a2d1): Version 1.0.9
	- Bump pixl-request to v2.6.0 for new connectTimeout feature, as well as idleTimeout handling upstream data.
	- Add retries with exponential backoff to file upload requests.
- [`d8571ba`](https://github.com/pixlcore/xysat/commit/d8571ba241c6aefb4415416b92247fd9d21b99f4): Add comment that explains the high timeout setting on pixl-request
- [`0cea26f`](https://github.com/pixlcore/xysat/commit/0cea26f87634ea3fc0da3edb9c04e4d6e4d002ca): Network Robustness: If socket connection is closed during final job update, keep trying indefinitely, unless satellite is shutting down.

## Version v1.0.8

> February 26, 2026

- [`176f88d`](https://github.com/pixlcore/xysat/commit/176f88d15a58af0a90d87cb5e72f2dcd581dd0ef): Version 1.0.8
- [`fdbd5d4`](https://github.com/pixlcore/xysat/commit/fdbd5d47b82004654d83a5143429d14b882977dc): Revert /proc/loadavg change, as it was a red herring.
- [`d965304`](https://github.com/pixlcore/xysat/commit/d96530456150781359a615d7c6ff806550fc5f08): Shell Plugin: Remove inused "Interpret JSON" code leftover from Cronicle.

## Version v1.0.7

> February 26, 2026

- [`7923410`](https://github.com/pixlcore/xysat/commit/7923410396f7a915e82a887888101f10572924b3): Version 1.0.7
- [`90dad1d`](https://github.com/pixlcore/xysat/commit/90dad1d2d59707e33c8fa88f087622725f437f2f): use /proc/loadavg for load average on linux, as it's more accurate inside containers vs. Node's os.loadavg()
- [`0b02ba1`](https://github.com/pixlcore/xysat/commit/0b02ba127111f948b39f8d8f8b1fd2691e340f14): Add optional config prop: `disable_job_network_io`, which will prevent calling "ss" every second during job runs.  For servers with a very large amount of concurrent network connections.

## Version v1.0.6

> February 25, 2026

- [`099aa97`](https://github.com/pixlcore/xysat/commit/099aa97d45771670ee3cc44d507024a38da290cf): Version 1.0.6
- [`f94262f`](https://github.com/pixlcore/xysat/commit/f94262f20abb199a0bd1d8c466fd129aa25037da): Increase time and memory limit for "ss" call in getNetworkConnections (called every minute).
- [`2ef5f76`](https://github.com/pixlcore/xysat/commit/2ef5f76f6830e4bc3ff09238862dfbe8f312b04c): Bug Fix: Crasher if "ss" command failed (improperly handling error case).

## Version v1.0.5

> February 24, 2026

- [`9e4d910`](https://github.com/pixlcore/xysat/commit/9e4d9104c5c7a7d87641d13ed645cb075d9ed7e4): Version 1.0.5
	- Bump version to rebuild package-lock.json.

## Version v1.0.4

> February 24, 2026

- [`6e72eb0`](https://github.com/pixlcore/xysat/commit/6e72eb0c24e141e02c16abb7d558625eba7800dd): Version 1.0.4
	- Remove npm as direct dependency, and install it only as part of the GH actions standalone builds.

## Version v1.0.3

> February 24, 2026

- [`dd9e595`](https://github.com/pixlcore/xysat/commit/dd9e5958f3984fdb8cd4519fbf913bdb9ee3bdd4): Version 1.0.3
	- Bump systeminformation to v5.31.1 for various vuln fixes.
- [`759fa15`](https://github.com/pixlcore/xysat/commit/759fa159ec699501c4ad4cd2fcae9bc19b208287): Container Start Script: If config.json file exists but is zero bytes, still run the bootstrap.

## Version v1.0.2

> February 18, 2026

- [`054a0d4`](https://github.com/pixlcore/xysat/commit/054a0d4949db82bfe13d679571efae1ae395c6dd): Version 1.0.2
- [`8fac770`](https://github.com/pixlcore/xysat/commit/8fac7700b3c8b3a24281f3983aed7079763954b6): Add more verbose logging to test-monitors.js script.
- [`3f48bce`](https://github.com/pixlcore/xysat/commit/3f48bce43def99d693dd783f5bd0c30245d7084e): Fix crasher bug on Linux if `ps` binary is not installed.
- [`ee39b63`](https://github.com/pixlcore/xysat/commit/ee39b63831da6e822e9827a17a229114ddbfde24): Add retries to bootstrap setup request in container-start.sh

## Version v1.0.1

> February 16, 2026

- [`6c6c9e1`](https://github.com/pixlcore/xysat/commit/6c6c9e1283c9a2d3bd58f36a5434a36a3dbb9032): Version 1.0.1
- [`6b440f7`](https://github.com/pixlcore/xysat/commit/6b440f78191bdc8ea088cbd7078ff4aa2a214e4a): Handle rare case when plugin cannot be found (i.e. plugin deleted with jobs still scheduled).
- [`11bc7c7`](https://github.com/pixlcore/xysat/commit/11bc7c701ce999b59da93622b0878b51c486bc2d): Temp File Behavior: Use extensionless temp files for Plugins, for better compatibility.  Windows is still the exception.

## Version v1.0.0

> February 11, 2026

- [`6212eb6`](https://github.com/pixlcore/xysat/commit/6212eb6a310346490fca60e2b0aed80f408eb42a): Add delayedAutoStart property for Windows service settings.
- [`a0a92a9`](https://github.com/pixlcore/xysat/commit/a0a92a91c94f00f51acab79a581fe00ed7abe20f): Redesigned Windows self-deletion process so it actually removes the whole directory on uninstall.
- [`43ccfd5`](https://github.com/pixlcore/xysat/commit/43ccfd5883959b54927c50f731f4e883a65558bb): Version 1.0.0
	- Bump node-pty to v1.1.0
	- Bump npm to v10.9.4 (the stock node v22 version)
	- Bump systeminformation to v5.30.7
- [`4a72115`](https://github.com/pixlcore/xysat/commit/4a72115b39e5dcdb02c6c3de46089613ba20d127): Major Upgrade: Bump Node.js from v18 to v22, and bump macOS from v14 to v15.

## Version v0.9.79

> February 5, 2026

- [`6991dce`](https://github.com/pixlcore/xysat/commit/6991dce224c0e0500faf7b0df9aa9674a13917fb): Version 0.9.79
- [`4aefe72`](https://github.com/pixlcore/xysat/commit/4aefe727cb022e878f41be5ad477c721f33c3541): Add monitoring self-test script, for troubleshooting issues with SI, etc.
- [`ade7500`](https://github.com/pixlcore/xysat/commit/ade75009c44e69f7a246cce9baf059c3b2e26b94): Add lots of debug log calls at level 9, for troubleshooting stuck monitors on some systems.  Also, add callback support for monitoring calls, for test harness.

## Version v0.9.78

> February 3, 2026

- [`eb55f86`](https://github.com/pixlcore/xysat/commit/eb55f86867984f1fefb91e39c29b13c2b279d248): Version 0.9.78
- [`f058483`](https://github.com/pixlcore/xysat/commit/f05848351603d6d6470a873cbb7b8a6977734a20): Add support for new job.status string.

## Version v0.9.77

> February 1, 2026

- [`c1ab406`](https://github.com/pixlcore/xysat/commit/c1ab40677cfa2da9b378e9b97ba23c2e1fe48509): Version 0.9.77
- [`e171a87`](https://github.com/pixlcore/xysat/commit/e171a8745ab8925148a2afd83de493f9506f9bf2): HTTP Plugin: Scalability adjustments: Support sending JSON body data payloads up to 32 MB.  Do not display response body if over 1 MB.
- [`8ab68bd`](https://github.com/pixlcore/xysat/commit/8ab68bd9ab6adfcbed152fef18085b6d78da38e4): Scalability: Increase child STDIO JSON message limit from 1 MB to 32 MB.  Adjust debug logging to compensate.

## Version v0.9.76

> January 30, 2026

- [`d45df5e`](https://github.com/pixlcore/xysat/commit/d45df5e936c6cb2925c21e248a5e661cb7d26c19): Version 0.9.76
- [`f194a02`](https://github.com/pixlcore/xysat/commit/f194a027accb46d8dd3778a914cbcd1667bd6343): Job Data: Always populate `base_url` in job, and XYOPS_JOB_DATA env var as well.
- [`d614c69`](https://github.com/pixlcore/xysat/commit/d614c69141319971c77611cd6904b3e0c22aa632): Typo fix in README
- [`8b3c70e`](https://github.com/pixlcore/xysat/commit/8b3c70ee9b5f04ca0167928369e96e3a5713124b): Add manual installation instructions for Linux, macOS and Windows.

## Version v0.9.75

> January 27, 2026

- [`19f6f51`](https://github.com/pixlcore/xysat/commit/19f6f51399e876809cfae52099709830dae6438d): Version 0.9.75
- [`1fa00b2`](https://github.com/pixlcore/xysat/commit/1fa00b21c60bb9542a5607c23d8b2feb9322e7e4): Copy non-object workflow params into environment variables with `workflow_` key prefix.
- [`10d19d6`](https://github.com/pixlcore/xysat/commit/10d19d6f9092db595a03d1d8bfb029de1ad17001): Fix typo in error string.

## Version v0.9.74

> January 25, 2026

- [`6661904`](https://github.com/pixlcore/xysat/commit/6661904af10fd2c2d0a4a86d9cbf3f903c1b47a0): Version 0.9.74
	- Bump pixl-boot to v2.0.2 for improved systemd service behavior.
	- Bump systeminformation to v5.30.6 for all the latest bug fixes.

## Version v0.9.73

> January 25, 2026

- [`9a01619`](https://github.com/pixlcore/xysat/commit/9a0161986e85d4021a66c8e4da22e6177b391147): Version 0.9.73
- [`b77ef2f`](https://github.com/pixlcore/xysat/commit/b77ef2ff70c1c174ef81d991d5cb2e69f0c62736): Windows Bug Fix: Allow Plugins to use Powershell by using correct ".ps1" script file extension.

## Version v0.9.72

> January 24, 2026

- [`1b172ec`](https://github.com/pixlcore/xysat/commit/1b172ec48a5c163385e547ee985238630a423365): Version 0.9.72
- [`8c8f8f9`](https://github.com/pixlcore/xysat/commit/8c8f8f986ccae6b4efb4dee2c088ee0ba3ac8e35): Shell Plugin: New optional param: "pass" which will passthrough all input data to output.
- [`eec9e09`](https://github.com/pixlcore/xysat/commit/eec9e0959d579e3b60d1dae434b177aa21a08e34): HTTP Plugin: Improve handling and display of core errors (e.g. "Socket hang up").
- [`bedcfbf`](https://github.com/pixlcore/xysat/commit/bedcfbf0608c152698b0a51c55aebeea00f6db82): Job Input File Handing: Skip file download when "runner" is set, also strip file.path param after downloading (to avoid user confusion).

## Version v0.9.71

> January 20, 2026

- [`b2dfc3a`](https://github.com/pixlcore/xysat/commit/b2dfc3a299255d2f03b401209efa6a53d34243c1): Version 0.9.71
- [`930530f`](https://github.com/pixlcore/xysat/commit/930530f13573d86577b4a5cf32db74069e935452): Fix: detectVirtualization could hang indefinitely with Azure and DigitalOcean clouds.

## Version v0.9.70

> January 17, 2026

- [`792c0ab`](https://github.com/pixlcore/xysat/commit/792c0ab03b6cf9e9414782454f6093e8ca80c15a): Version 0.9.70
- [`ba0573a`](https://github.com/pixlcore/xysat/commit/ba0573a3c4ffbc7e8137db856dc36be6ca84b467): Fix: getDiskFast: Disk utilization numbers were inflated for some setups (disk partitions were counted twice).

## Version v0.9.69

> January 17, 2026

- [`a1e200f`](https://github.com/pixlcore/xysat/commit/a1e200ffada0fa71df455a361d941ccde63591bb): Version 0.9.69
- [`0d99c00`](https://github.com/pixlcore/xysat/commit/0d99c00ad647d1641332f25aef379d9673d85d47): Tweak debug levels of initial communication / auth challenge, and add some additional debug log entries.
- [`12aded5`](https://github.com/pixlcore/xysat/commit/12aded50e7d0ef36f97e5b5299ac7e0a77fcc27c): Add standard control.sh script for starting / stopping daemon (not for containers).

## Version v0.9.68

> January 14, 2026

- [`dffcfd3`](https://github.com/pixlcore/xysat/commit/dffcfd379e9a229e6e422d6be67879e0e8f61e9f): Version 0.9.68
- [`0817a61`](https://github.com/pixlcore/xysat/commit/0817a61731efe2b387f4e8f8431679ed6d2706fb): Upgrade Satellite: Remove "__daemon" environment variable, used by pixl-server.
- [`226b9c4`](https://github.com/pixlcore/xysat/commit/226b9c49277207d1b8b7545078a7c2313f9c6797): Startup Log File Check: Include hostname in notice/critical messages sent to conductor.

## Version v0.9.67

> January 14, 2026

- [`9e4fa37`](https://github.com/pixlcore/xysat/commit/9e4fa37353f3f1c24790e5db54758877d490c40d): Version 0.9.67
- [`5692f8f`](https://github.com/pixlcore/xysat/commit/5692f8fe7f0de2d5cfa0172233dea4e1d72dff60): Comm: Sanity check on socket in handleSocketMessage (race condition on shutdown)

## Version v0.9.66

> January 14, 2026

- [`c2c2fc0`](https://github.com/pixlcore/xysat/commit/c2c2fc0a3adfb3b68fd2031b1f8eac23e1022371): Version 0.9.66
- [`763a73a`](https://github.com/pixlcore/xysat/commit/763a73a016b8b9410729cce54d987304f51ae70d): Crasher Fix: Sending incorrect websocket data format for notice/critical messages.

## Version v0.9.65

> January 13, 2026

- [`0270765`](https://github.com/pixlcore/xysat/commit/0270765a12533c968ced2be98ca3d6924379eb81): Version 0.9.65
- [`518f9d7`](https://github.com/pixlcore/xysat/commit/518f9d7088f4df893f965efd726498d43d1dc7c1): New upgrade logic: Use background.log, check for stale log, etc.
- [`e535c33`](https://github.com/pixlcore/xysat/commit/e535c33ba3eebc8e2ae7587ded540fbd21d5c23e): On socket auth, check for background.log and crash.log.  If found, send notices/criticals to the primary conductor.

## Version v0.9.64

> January 10, 2026

- [`d139bc1`](https://github.com/pixlcore/xysat/commit/d139bc175471ef19e54600e28d712f21414db63f): Version 0.9.64
- [`4600d07`](https://github.com/pixlcore/xysat/commit/4600d07cc584f885bd1b1d981427e2634b032ca4): Fix: Export PATH in container-start.sh, so it properly propagates out

## Version v0.9.63

> January 10, 2026

- [`4dccb60`](https://github.com/pixlcore/xysat/commit/4dccb60fabde4f539380abb4e084e74e5ab2cbc1): Version 0.9.63
- [`e99bd7e`](https://github.com/pixlcore/xysat/commit/e99bd7e3b413c1232b515a2d14d41991e0197173): Add common PATH locations to container-start.sh

## Version v0.9.62

> January 10, 2026

- [`87a4a1c`](https://github.com/pixlcore/xysat/commit/87a4a1c1cc596c4803c1f10af6ec29c21875a1ef): Version 0.9.62
- [`80e0c29`](https://github.com/pixlcore/xysat/commit/80e0c29ef76a8ac736b3f29e8d5a96203d5de0b6): Fix: Move uv/uvx binaries to a standard PATH location

## Version v0.9.61

> January 10, 2026

- [`3b3c23a`](https://github.com/pixlcore/xysat/commit/3b3c23a0f1d18a82d547c2dfe6c70e7c5d18d458): Version 0.9.61
- [`3e360b6`](https://github.com/pixlcore/xysat/commit/3e360b6611d034096bb622026353fbb611cbb9c4): Refactor: Changes in monitor plugins and new features.
- [`6b021b6`](https://github.com/pixlcore/xysat/commit/6b021b6b67e513e7b611b8f0c23ece3e179cf1a5): Add new "features" object, which reports satellite features on connect
- [`ef38f37`](https://github.com/pixlcore/xysat/commit/ef38f37f9d9b24f6b42f7ca9a5d75ba50d32eee7): Drop default ping timeout from 120 to 60 seconds, and add support for new testMonitorPlugin command.
- [`7678659`](https://github.com/pixlcore/xysat/commit/7678659ca5ea52d73d0b2dc3276ae62019fed06e): Test Plugin: Add support for simulated "Abort" style response.
- [`bed1a7f`](https://github.com/pixlcore/xysat/commit/bed1a7faaf97be36451f7f23372da58075473284): HTTP Plugin: Report details in markdown format, and set idleTimeout to value of timeout.

## Version v0.9.60

> January 8, 2026

- [`824e6ea`](https://github.com/pixlcore/xysat/commit/824e6ea844d3a2dc2de7050b452d2946f0d28d43): Version 0.9.60
- [`dfefa9f`](https://github.com/pixlcore/xysat/commit/dfefa9fd44e21a3b2f3bda01dddfa7afe30065ed): Fix: Properly handle shutdown while jobs are still running.

## Version v0.9.59

> January 8, 2026

- [`8deef75`](https://github.com/pixlcore/xysat/commit/8deef75017305fec975844be07eeeb45d8657c00): Version 0.9.59
- [`75a6adc`](https://github.com/pixlcore/xysat/commit/75a6adc4794e8525957ec8109bb4e98a31d9564d): Fix: Crasher bug in detectVirtualization with public cloud VMs
- [`c393066`](https://github.com/pixlcore/xysat/commit/c393066a240bd9f542fe9a48877621c95cd6e7e5): Fix: Crasher bug on macOS when netstat doesn't return any interfaces.
- [`95a6d3f`](https://github.com/pixlcore/xysat/commit/95a6d3f8d03188817cd9759e9071469609202b3a): Changelog Script: Add smarts, tweak formatting.

## Version v0.9.58

> January 5, 2026

- [`4f00f79`](https://github.com/pixlcore/xysat/commit/4f00f79127e662aa9ff7b2decd77b396dfeb72cc): Version 0.9.58
- [`63d470e`](https://github.com/pixlcore/xysat/commit/63d470e9994c15cf28366f16e8d8c40e5c4b60d5): Add container sanity check in container-start.sh
- [`f3c8287`](https://github.com/pixlcore/xysat/commit/f3c82874bebff28e25ae8b2d5d5de86ee1e5d13a): If files failed to upload during job finish, clear out files array
- [`e54a0bb`](https://github.com/pixlcore/xysat/commit/e54a0bb4e64b742dc0abfbdff3449887c3bbb65e): Rename start.sh to container-start.sh (only for use as a docker container entrypoint)

## Version v0.9.57

> December 31, 2025

- [`3743d35`](https://github.com/pixlcore/xysat/commit/3743d35fa6f0ccb1aea37b0f318e80bb1585dc57): Version 0.9.57
- [`0fa6ab5`](https://github.com/pixlcore/xysat/commit/0fa6ab5094a358602af81d79ab6a78a229545de7): Add changelog generator script, and changelog itself.
- [`a23c985`](https://github.com/pixlcore/xysat/commit/a23c9854fe25fba29c5b3de66cd48b79d8ba3fdf): Add package-lock

## Version v0.9.56

> December 30, 2025

- [`9fa719a`](https://github.com/pixlcore/xysat/commit/9fa719ad271a3e19907c7f7d4ca656ea545fe497): Version 0.9.56
- [`d874422`](https://github.com/pixlcore/xysat/commit/d8744228bf59c6d975478c553b193dd8516ac943): Only add non-object params to ENV vars (i.e. skip JSON ones)
- [`e335bb2`](https://github.com/pixlcore/xysat/commit/e335bb2fbdbd4919a015f0a38a69ca4622d1c2e3): Test Plugin: Log incoming job params.

## Version v0.9.55

> December 29, 2025

- [`2101471`](https://github.com/pixlcore/xysat/commit/2101471f677dc4bc7e76944027e35ed6d8093092): Version 0.9.55
	- No longer mapping XYOPS_ env vars.  Instead, support XYSAT_ as an alias env var prefix.
	- This is so we can have satellite coexist inside the xyops container, and the env vars won't clash (i.e. XYOPS_foreground for example).

## Version v0.9.54

> December 24, 2025

- [`fa9bcd6`](https://github.com/pixlcore/xysat/commit/fa9bcd6080693ccf2e9da79271facd60709e68dd): Version 0.9.54
- [`f1d006c`](https://github.com/pixlcore/xysat/commit/f1d006c7b0a3be2102a29e293445d1637f730f3c): Multiple changes...
- [`38ac10d`](https://github.com/pixlcore/xysat/commit/38ac10d5926bbf73c620e0cdf567235fee1673a7): Remove pid check in main.js -- happens already in pixl-server

## Version v0.9.53

> December 16, 2025

- [`41efd6d`](https://github.com/pixlcore/xysat/commit/41efd6d6c480fc2e07abee5b4f0df73650f98196): Version 0.9.53
- [`6b147c9`](https://github.com/pixlcore/xysat/commit/6b147c9d011e07a4dd48088d281e85b9a8a0a661): Retire macos 13, move to 14...

## Version v0.9.52

> December 16, 2025

- [`97a45ba`](https://github.com/pixlcore/xysat/commit/97a45ba4d33eb125b33b10ca51215e021e5f93e6): Version 0.9.52
	- Bump pixl-tools to v2.0.0 for redesigned ID generation
	- Bump systeminformation to v5.27.14 for vuln fix on windows.
- [`95e6192`](https://github.com/pixlcore/xysat/commit/95e6192746950235a3e26155fcb8827fe36d81f0): Protection against event plugin printing the entire job object to STDOUT
- [`bacf4ee`](https://github.com/pixlcore/xysat/commit/bacf4ee15fe75968f06f922ab227e32633b0dd65): Remove debugging info
- [`083f518`](https://github.com/pixlcore/xysat/commit/083f5184c71ad2177519e44051ff1e0fc37d03c5): Remove unused "monitoring_only" flag

## Version v0.9.51

> December 6, 2025

- [`1bdb290`](https://github.com/pixlcore/xysat/commit/1bdb290b49b79e583484b4edf5789823913b166b): Version 0.9.51
- [`6dd4777`](https://github.com/pixlcore/xysat/commit/6dd477708cadbb59b30797acac81f770b523f6f6): Use exec to replace start.sh script process with node process
- [`430c2da`](https://github.com/pixlcore/xysat/commit/430c2daf9fa8a2431f09c044548d79671270e767): Startup config validation and debug logging (auth vs key methods)
- [`f0318fe`](https://github.com/pixlcore/xysat/commit/f0318feb28f5aea2076186e2529b0622676dbc06): Add level-9 debug logging for auth server negotiation
- [`696481d`](https://github.com/pixlcore/xysat/commit/696481dc70baae585853e7f70d5420cc44597492): Echo custom param in output data

## Version v0.9.50

> December 5, 2025

- [`8c1db57`](https://github.com/pixlcore/xysat/commit/8c1db573d88c110674eeb2cc835f9c0ebe323360): Version 0.9.50
- [`470e84e`](https://github.com/pixlcore/xysat/commit/470e84e08dd422d616f1ccd0cc2d700ca190efbb): Add protection against rare race condition, which could crash if socket was closed during the quickmon host delay.

## Version v0.9.49

> December 3, 2025

- [`d807722`](https://github.com/pixlcore/xysat/commit/d80772296f7d72a7997258046383390fab6e9d99): Version 0.9.49
- [`ed7b383`](https://github.com/pixlcore/xysat/commit/ed7b38358dc4d76366801855015ac39717640c2e): Always report job completion on process exit (copy shell plugin behavior)
- [`164f781`](https://github.com/pixlcore/xysat/commit/164f7811473675238edd3dc9612716037b9f1196): Fix issue with secrets getting clobbered by runner meta

## Version v0.9.48

> December 3, 2025

- [`c986f93`](https://github.com/pixlcore/xysat/commit/c986f93243fdbd65f0e3ff47e14bd3d6e524e18b): Version 0.9.48
	- Add some missing libraries (fallout from the switch to the slim image)

## Version v0.9.47

> December 2, 2025

- [`3c99af0`](https://github.com/pixlcore/xysat/commit/3c99af010c681f7dc16488837cec75f90a6cf333): Version 0.9.47
- [`f49e276`](https://github.com/pixlcore/xysat/commit/f49e2767e078a8e928899fb89d6f750e2577fe6d): Trying node:22-bookworm-slim again, also added labels

## Version v0.9.46

> December 2, 2025

- [`56914c7`](https://github.com/pixlcore/xysat/commit/56914c7d22f60bdd7e1d86b051e9b330ef600f2b): Version 0.9.46
- [`3751491`](https://github.com/pixlcore/xysat/commit/37514910cfc6819ae3263e79ea82c7c16e5eb7fc): Switch to node:22-bookworm, so we can build native addons (node-gyp, etc.)

## Version v0.9.45

> December 2, 2025

- [`19fdfdc`](https://github.com/pixlcore/xysat/commit/19fdfdc061246932ba4ac4fa141baaa62822986c): Version 0.9.45
- [`e03f111`](https://github.com/pixlcore/xysat/commit/e03f1111422b91bc05ad5acffbbc8ec26ea4a58e): Move to node:22-bookworm-slim
- [`158efa9`](https://github.com/pixlcore/xysat/commit/158efa9d2ba8f11c7f37a02af3da9c222bf45cfc): Pass secrets in job metadata as well as env vars
- [`8505d89`](https://github.com/pixlcore/xysat/commit/8505d895418e71dfcec900e6e7a1f1fb724a75f7): Add new docker plugin

## Version v0.0.44

> November 30, 2025

- [`bd4961f`](https://github.com/pixlcore/xysat/commit/bd4961f15f1025fb19838d54e5f5b2ff28c62cd6): Version 0.0.44
- [`04df82a`](https://github.com/pixlcore/xysat/commit/04df82a6f6827d397b7bb03a2303ca233ffd1554): Add support for remote jobs via a runner script (e.g. xyRun)
- [`379d9b9`](https://github.com/pixlcore/xysat/commit/379d9b9d24deae093d7fff84523719c1783929a0): Cleanup pid file from last run (i.e. from container hard restart)

## Version v0.0.43

> November 24, 2025

- [`c160844`](https://github.com/pixlcore/xysat/commit/c160844653478f3014f5ae4165b42bc89125411d): Version 0.0.43
- [`4be2c8b`](https://github.com/pixlcore/xysat/commit/4be2c8b1c44086948a032c837792fde6b530a18b): Fix doc links
- [`6811986`](https://github.com/pixlcore/xysat/commit/6811986838bd784db256c9a51c3dd1e14ff9fe88): Remove old secret_key default prop (not needed)
- [`556b5d8`](https://github.com/pixlcore/xysat/commit/556b5d82cfe2bce8cf0919bd4ff21444dfd32600): New start script with support for bootstrap config

## Version v0.0.42

> November 22, 2025

- [`edef85f`](https://github.com/pixlcore/xysat/commit/edef85fc9088172b5fbd680456ea2f3495906dd1): Version 0.0.42
- [`024cfe7`](https://github.com/pixlcore/xysat/commit/024cfe70924e8d74d413c18b59519106fc870243): Include command secrets in env, if any were provided
- [`92c9799`](https://github.com/pixlcore/xysat/commit/92c97999d4a5d268fe76921302d5a528d50fa375): Multiple changes...
- [`ef6ccd6`](https://github.com/pixlcore/xysat/commit/ef6ccd6f565fddc766ab19fd64eabe62394c382f): Add updateConfig WS command
- [`c3332c1`](https://github.com/pixlcore/xysat/commit/c3332c129b96d79e095e723411e1861e794f1c73): Re-lic to BSD-3

## Version v0.0.41

> October 24, 2025

- [`9fd2e91`](https://github.com/pixlcore/xysat/commit/9fd2e916f2e1c8105a5e40bdc6dd3f5773f30eb2): Version 0.0.41
- [`5d7510e`](https://github.com/pixlcore/xysat/commit/5d7510e63757e313551661c6f364ef4522b095d2): Support new "details" object sent alongside job.
- [`669eb7c`](https://github.com/pixlcore/xysat/commit/669eb7ce460f6185622cbe1f71f91a4360af44c8): Update LICENSE formatting so it (hopefully) triggers GitHub's auto-license detection

## Version v0.0.40

> October 23, 2025

- [`3e132f6`](https://github.com/pixlcore/xysat/commit/3e132f66926a56524047234deab54c57234b8d34): Version 0.0.40
- [`af91a45`](https://github.com/pixlcore/xysat/commit/af91a45af99640f9e485705a5ee04f58d6211924): Standardize on xy:1
- [`3ac5e2a`](https://github.com/pixlcore/xysat/commit/3ac5e2a3831b366e42279b9879ed959ffdeae330): Standardize on xy:1, also fix bug with error handling
- [`d9707bc`](https://github.com/pixlcore/xysat/commit/d9707bc56c12f231e2d8ed8a79454f72e26b177b): Standardize on STDIO API with xy and type props, sent into child

## Version v0.0.39

> October 11, 2025

- [`9adbd42`](https://github.com/pixlcore/xysat/commit/9adbd42efc5864d53880d002571932fecea4867b): Version 0.0.39
- [`75a2c83`](https://github.com/pixlcore/xysat/commit/75a2c831a8a2c844719863ab269eec1e598aea75): Still trying to get Docker CLI to install...

## Version v0.0.38

> October 11, 2025

- [`94ca6ba`](https://github.com/pixlcore/xysat/commit/94ca6ba3d5381438abbca9621734867094f88403): Version 0.0.38
- [`81f862c`](https://github.com/pixlcore/xysat/commit/81f862c174d9858a9c235ff3f7ff996ebcbda477): Typo

## Version v0.0.37

> October 11, 2025

- [`8bbceb9`](https://github.com/pixlcore/xysat/commit/8bbceb9dd8d73012b48c878b397983c2dacee371): Version 0.0.37
- [`bd22f4a`](https://github.com/pixlcore/xysat/commit/bd22f4a0d2ccd1f041dc3163fd18a435da064c42): Another attempt at getting docker CLI to install

## Version v0.0.36

> October 11, 2025

- [`4f25c15`](https://github.com/pixlcore/xysat/commit/4f25c15c33eb74e25d495c4d0d2db94750f8547c): Version 0.0.36
- [`703745f`](https://github.com/pixlcore/xysat/commit/703745fdc73694886e564723ddfee80e4e34add7): add some custom PATHs and set sane defaults (on linux/macos)
- [`f06c848`](https://github.com/pixlcore/xysat/commit/f06c8486458fbaa5c127e53db4e1707853fdb0d3): Multiple changes...
- [`b122d49`](https://github.com/pixlcore/xysat/commit/b122d49df84a8062018f780fb3c7281363cc5cb8): Add git and docker CLI

## Version v0.0.35

> October 7, 2025

- [`5995aa3`](https://github.com/pixlcore/xysat/commit/5995aa3b5a51c8e4c69958a8945ba16d2e9a739f): Version 0.0.35
- [`d36be08`](https://github.com/pixlcore/xysat/commit/d36be0825e9967515ee87c6744a6eae8b91b8f03): Fix issue where child emitting random (non-xy) JSON isn't echoed in output

## Version v0.0.34

> October 7, 2025

- [`21f9b41`](https://github.com/pixlcore/xysat/commit/21f9b41ef284b430bdddfb47e7eba10aee5345eb): Version 0.0.34
	- Add npm as dep, to test npx when installed this way
- [`596ea34`](https://github.com/pixlcore/xysat/commit/596ea340cf2efdc1b54cf3dd8c4a2390684f400a): Add section on included software (node.js)

## Version v0.0.33

> October 7, 2025

- [`08f3abf`](https://github.com/pixlcore/xysat/commit/08f3abf1becfed686a7cb8e548f53d92ab2928f4): Version 0.0.33
- [`9b14888`](https://github.com/pixlcore/xysat/commit/9b148887bf8ab14a27f0fa1e85b5b6b862b13613): Support new "host" param / env var to override hosts
- [`67a0ab9`](https://github.com/pixlcore/xysat/commit/67a0ab9563bb7864defd5af5b300cfacb0910e9c): Use perf.metrics() instead of the old summarize()
- [`d2feb2e`](https://github.com/pixlcore/xysat/commit/d2feb2e527ec1f0fa3d46b02fdcf3a5dc82f6a27): Rename legacy mode to cronicle mode

## Version v0.0.32

> September 12, 2025

- [`e2a4bae`](https://github.com/pixlcore/xysat/commit/e2a4bae3eefca6ee8d4ad899e7be4866c3317a86): Version 0.0.32
- [`45bc4f9`](https://github.com/pixlcore/xysat/commit/45bc4f9a0feb24ffb49ff6819fb3801650c9658c): Change job kill (abort policy) to string: none, parent, or all.

## Version v0.0.31

> September 11, 2025

- [`dddc3c5`](https://github.com/pixlcore/xysat/commit/dddc3c570abfa41e230e692eca0d94ee82fbc301): Version 0.0.31
- [`b40c7c1`](https://github.com/pixlcore/xysat/commit/b40c7c13e98f6fd96259288c037c8f7f06d09c54): Implement kill all children option (job.kill)
- [`1c247c3`](https://github.com/pixlcore/xysat/commit/1c247c30d7a47128864235377534c25abf3cc4cf): Implement cleanEnv

## Version v0.0.30

> September 6, 2025

- [`0872af9`](https://github.com/pixlcore/xysat/commit/0872af99df749898ba752cf277e09bc907ca0371): Version 0.0.30
- [`9d2ebaa`](https://github.com/pixlcore/xysat/commit/9d2ebaa45ad8f8e3406322ebc57b4bd4148e7652): Change startup msg log level back to 2 (race condition with windows)
- [`a41dd49`](https://github.com/pixlcore/xysat/commit/a41dd49ad8809a2c1402a499294484a3614452dd): Log startup message to windows event logger

## Version v0.0.29

> September 5, 2025

- [`47f924c`](https://github.com/pixlcore/xysat/commit/47f924c956f426d90ed6dd8da6dcbe2bda34c982): Version 0.0.29
- [`605eab0`](https://github.com/pixlcore/xysat/commit/605eab084e665c8fe5916e048711f77570e5cc57): Fix json stream parse on win
- [`20c9ac3`](https://github.com/pixlcore/xysat/commit/20c9ac3fc2d76c72a4b1cea3a05a6cd283be0004): Fix json stream parser on windows
- [`13e5ad8`](https://github.com/pixlcore/xysat/commit/13e5ad8cbb416dc1fcc3006ce25a1bf27ad0b5a8): Fix memRss and memVsz on windows
- [`53cc77a`](https://github.com/pixlcore/xysat/commit/53cc77ac0063c7ded4500ae4764ce85d5c06f59c): Better support for Windows line endings
- [`d2f4282`](https://github.com/pixlcore/xysat/commit/d2f42829337a57d33390973229bc74aecec475e9): Log startup and shutdown at level 1
- [`8fda581`](https://github.com/pixlcore/xysat/commit/8fda581060c8859445765196a4c72ce4da2af76e): Log ws connect at level 1

## Version v0.0.28

> September 5, 2025

- [`fb120e1`](https://github.com/pixlcore/xysat/commit/fb120e16897b60643e663a0def0fa3b94c9fc53a): Version 0.0.28
- [`05b001d`](https://github.com/pixlcore/xysat/commit/05b001d00f49b92d90310cf816ee13624e0274f4): Initial support for win32 (WIP)
- [`c66aeee`](https://github.com/pixlcore/xysat/commit/c66aeeef7b4ba62e4c7f1e6d38d547bbab567e0e): upgradeSatellite: Lots of changes for WIndows (OMG)

## Version v0.0.27

> September 5, 2025

- [`be064c5`](https://github.com/pixlcore/xysat/commit/be064c504dd0e4576c47ff0107f2aec49d9e4c68): Version 0.0.27
- [`c1473ee`](https://github.com/pixlcore/xysat/commit/c1473ee1cecbfc2a3a54d2cad19818ee1f368d50): Allow self-upgrades in foreground mode (docker)
- [`bae922f`](https://github.com/pixlcore/xysat/commit/bae922f5a7498be5118490a876f3289fb001c773): Start: early check for PID file, to prevent stompping on ourselves

## Version v0.0.26

> September 4, 2025

- [`6132b8a`](https://github.com/pixlcore/xysat/commit/6132b8a97c50f29f2f6d08f388e6fb987d19be46): Version 0.0.26
- [`cbf4903`](https://github.com/pixlcore/xysat/commit/cbf49034607678993dea265babf59fd00683999f): Multiple changes...
- [`394825b`](https://github.com/pixlcore/xysat/commit/394825b3dae5317f1bb24fe44bba4001550a3d50): Do not include uid or gid features for windows
- [`d5ac1c7`](https://github.com/pixlcore/xysat/commit/d5ac1c78cb5ff875bae2f2eaefd04e51c2b59a8d): Fix class name (Engine to Satellite)
- [`50caf4e`](https://github.com/pixlcore/xysat/commit/50caf4eb64107b41afb04b932b6f7bceb64f7e38): Multiple changes...

## Version v0.0.25

> September 3, 2025

- [`551d331`](https://github.com/pixlcore/xysat/commit/551d331fb32c990d26b7310abbf416d908c85b8e): Version 0.0.25
- [`9c567ea`](https://github.com/pixlcore/xysat/commit/9c567ea05dbe02c500eaf304926a94f024e587a9): Cleaner shutdown sequence

## Version v0.0.24

> September 2, 2025

- [`6f42f42`](https://github.com/pixlcore/xysat/commit/6f42f428452e21dc7771e6a4fc22c6a4acc18420): Version 0.0.24
- [`0c126e7`](https://github.com/pixlcore/xysat/commit/0c126e73c50d72fc6de1c5bf35f48e36ce23d4ef): Log errors to dedicated error log
- [`a3cc172`](https://github.com/pixlcore/xysat/commit/a3cc1729024fc81fa8423871ce7fbbcd66911836): Split logs into component logs, and move some utility functions to utils.js
- [`cb85184`](https://github.com/pixlcore/xysat/commit/cb85184984750cf55f3ea54e98d48ce3c035b65e): Split single log into component logs
- [`7871c83`](https://github.com/pixlcore/xysat/commit/7871c83c46e2b78bae66f162c73983c2bfc3322c): Check for upgradeRequest on jobFinish, call upgradeSatellite if pending
- [`0d84ac5`](https://github.com/pixlcore/xysat/commit/0d84ac51e2839a0cb199ed72b24015d60256520a): Copy debug and foreground from server, add curlBin and wgetBin on Linux/macOS
- [`be51ccc`](https://github.com/pixlcore/xysat/commit/be51ccc45f8a282957148df75e76e755bb1958da): Add support for self upgrades
- [`c19c2cb`](https://github.com/pixlcore/xysat/commit/c19c2cb0a361d81e8ed3b6e5f99c5442716822ee): Support for stopping service on windows via stop command
- [`e195441`](https://github.com/pixlcore/xysat/commit/e195441ae45d4cb302736a0fb31758690439d948): Buffer job log output (pipeline)

## Version v0.0.23

> August 30, 2025

- [`84a3ddc`](https://github.com/pixlcore/xysat/commit/84a3ddc52d82d185d4aee5044522eaf41a20d4a0): Version 0.0.23
	- Trying to fix docker build
- [`d551843`](https://github.com/pixlcore/xysat/commit/d55184366886a1113c9aaa6d259a1fa066d2897e): Fix uv/uvx install steps

## Version v0.0.22

> August 30, 2025

- [`319d5c5`](https://github.com/pixlcore/xysat/commit/319d5c522eedf37dec69f96ff95757a4dc87f637): Update README.
- [`844fd95`](https://github.com/pixlcore/xysat/commit/844fd95759b69d041a9fd5ca17ae4ca64805a6a4): Version 0.0.22
	- Relic to MIT
	- Bump pixl-request to 2.4.1
	- Bump sysinfo to 5.27.7
- [`38ace17`](https://github.com/pixlcore/xysat/commit/38ace1737044c3d055705c483b1fdbc0a4e6ab68): Support airgap mode
- [`4488cc2`](https://github.com/pixlcore/xysat/commit/4488cc2388e85c88f417f9add3bf0a3579b34182): Support for config updates on master connect, and airgap mode, relic to MIT
- [`14d0d5e`](https://github.com/pixlcore/xysat/commit/14d0d5eaf8576497afeb2ed9dd502079672d2795): Relicense to MIT
- [`1fc9982`](https://github.com/pixlcore/xysat/commit/1fc998299b13d674905c1a3a1324943e7d2a3da8): New Docker workflow
- [`3035ba0`](https://github.com/pixlcore/xysat/commit/3035ba037f520029ffbf84b1f0849febc0a6c029): Add info.process.pid
- [`8a003c5`](https://github.com/pixlcore/xysat/commit/8a003c5df1da2d7e2768af84281e1815a8fda1fa): Support for secrets
- [`c479249`](https://github.com/pixlcore/xysat/commit/c47924924614019df03aea0b639d3e20ee2697f7): Change boot name to "xysat" for easier use with systemd / systemctl

## Version v0.0.21

> August 8, 2025

- [`8e309f1`](https://github.com/pixlcore/xysat/commit/8e309f141fb3ca7aa83daf116762108e109d09ac): Version 0.0.21
	- Renamed to xySat!
- [`a238635`](https://github.com/pixlcore/xysat/commit/a2386357d79c95ad8338af7373f54c21eee2b35a): Rename to xyOps / xySat
- [`cddaf98`](https://github.com/pixlcore/xysat/commit/cddaf98a276057bb61944de8bf9db8b8d30ce7fb): Remove extra params, always spawn sleep proc and report progress, tweak sample data

## Version v0.0.20

> July 26, 2025

- [`970447b`](https://github.com/pixlcore/xysat/commit/970447b67ccf0df88fa664d3048a0da061cfcced): Version 0.0.20
- [`988ddf6`](https://github.com/pixlcore/xysat/commit/988ddf61f7aea8014637d9584a2809829fbcf97f): Big rename to opsrocket-satellite

## Version v0.0.19

> July 25, 2025

- [`b674239`](https://github.com/pixlcore/xysat/commit/b674239dedb2ee09b7dfa9919447666260c8cc51): Version 0.0.19
- [`986c542`](https://github.com/pixlcore/xysat/commit/986c542edee13e05920606bbe1215eaa3e80ef99): A bunch of changes...
- [`a793574`](https://github.com/pixlcore/xysat/commit/a793574936bf998b8251fd84dd65346f2e6ff438): Tweak dirs for new job.cwd overhaul
- [`11b8204`](https://github.com/pixlcore/xysat/commit/11b8204f914ad903d2ac50a941c0de4e2b4a3894): Now downloading to job cwd, and use Path.join for windows
- [`3aa4c93`](https://github.com/pixlcore/xysat/commit/3aa4c93b950ec2c33d85870b5e633756f4deefff): Typo fixes
- [`d8e5b30`](https://github.com/pixlcore/xysat/commit/d8e5b30afa7b3b6b703c62ac67204f7f5935bf6e): chdir fixes for new job temp dir layout
- [`34b0517`](https://github.com/pixlcore/xysat/commit/34b0517392bded7432e15d73453078a06ac28521): Create job temp dir parent on startup
- [`8b845d6`](https://github.com/pixlcore/xysat/commit/8b845d6c0e8a0054d2532bea754f0f073cc288cd): Call prepLaunchJob
- [`46f7ba4`](https://github.com/pixlcore/xysat/commit/46f7ba43d2a1d8092b15f0e39d86e414c6d36b5a): A number of changes...
- [`141b2d9`](https://github.com/pixlcore/xysat/commit/141b2d9687a90b52e1abe05b31293b08118ceaeb): Fix API URL for uploading job log (needs port now)

## Version v0.0.18

> May 31, 2025

- [`76b0982`](https://github.com/pixlcore/xysat/commit/76b09826d6e41e740226f3374cb2e65c1fbd5fc5): Version 0.0.18
- [`b62a734`](https://github.com/pixlcore/xysat/commit/b62a734e6379650fc67e446b60bd1e512bdf2eff): Typo fix, and timing delay tweak...
- [`b689fa9`](https://github.com/pixlcore/xysat/commit/b689fa99fb06fa33a2f30a55090e100a57111ed7): allow `masters` config param to override hosts, and split string if needed
- [`1e3a62c`](https://github.com/pixlcore/xysat/commit/1e3a62c50e1107aea811989cadefa403ceec5d7c): Port now stored separately from host array
- [`c5a7811`](https://github.com/pixlcore/xysat/commit/c5a7811e1f84242d77e65f5985a34c3db49d5617): Multiple changes...
- [`6a96167`](https://github.com/pixlcore/xysat/commit/6a96167e224e50cc550dc4c513e03d4430877162): Create sample config on startup if does not exist.

## Version v0.0.17

> May 30, 2025

- [`bf8e1b3`](https://github.com/pixlcore/xysat/commit/bf8e1b39d9f3e66ce08ee0b03011f44fb06bb7d9): Version 0.0.17
- [`8b5c9ce`](https://github.com/pixlcore/xysat/commit/8b5c9ce5243a44aa9f814282dc47a8f3b8bf92d6): New dynamic max sleep system for both monitors and quickmon
- [`72d956a`](https://github.com/pixlcore/xysat/commit/72d956a4a991934d1a1c71531913acfac5694385): Multiple changes...
- [`f713803`](https://github.com/pixlcore/xysat/commit/f713803eae96e67c27e9a4d42458a5f78f60eb7c): Handle "retry" ws response
- [`f3a73ae`](https://github.com/pixlcore/xysat/commit/f3a73aee28183a1db75545f8a38b76b0a24829e7): Add support for ORCHESTRA_masters env vars
- [`c9033e1`](https://github.com/pixlcore/xysat/commit/c9033e168157e4644d4070c00952038c28e7a745): Filter out our own ps spawn from proc list
- [`bfb21e7`](https://github.com/pixlcore/xysat/commit/bfb21e7d99fba4dcb8a6fc6fc88ec664b0c0565b): Change default socker_reconnect_delay_max to 30s
- [`7b8ba73`](https://github.com/pixlcore/xysat/commit/7b8ba736498c9952c90f5b1d0b9913b881adba8b): Drop node to version 18

## Version v0.0.16

> April 6, 2025

- [`5ed35a2`](https://github.com/pixlcore/xysat/commit/5ed35a2d0d8d85b05bb9f60fc01fefc39b845c12): Version 0.0.16
- [`3e6cc0f`](https://github.com/pixlcore/xysat/commit/3e6cc0f732ceb3952a0d2eb5c6e84ac87e60c630): Add node-notifier dep
- [`d90d0c0`](https://github.com/pixlcore/xysat/commit/d90d0c06c210cf1d8f950f6b6caf7a9e243fdc3e): Improve plugin exec args
- [`f804eb2`](https://github.com/pixlcore/xysat/commit/f804eb27ea8cc6f03847a119251c88d041784122): Add new ws uninstall conductor command
- [`7928d87`](https://github.com/pixlcore/xysat/commit/7928d87cb9cd775074dd9c0bb4b509408fc78133): Install script changes...
- [`a9d74c1`](https://github.com/pixlcore/xysat/commit/a9d74c184bf04af571d8bbef8b81a120bf340d68): Misc cleanup to win32 service stuff
- [`3a7bedd`](https://github.com/pixlcore/xysat/commit/3a7bedd8588bbf16c18a1879e6c6659b4a3f45dd): Improve error messages
- [`d94c64f`](https://github.com/pixlcore/xysat/commit/d94c64f088bba7422ab75ed8566980cd5bb7c774): Fully implement uninstall command (deletes everything!)
- [`5e6cec0`](https://github.com/pixlcore/xysat/commit/5e6cec0e71296c3f1af749b4efd2a8e3ec47de54): Naming (conductor)
- [`84e31c4`](https://github.com/pixlcore/xysat/commit/84e31c4cb257f1abacaea0ea24724aa72f5400cd): Code cleanup
- [`bbbd545`](https://github.com/pixlcore/xysat/commit/bbbd54524b849ad1daa5627c2cc3fb620cf7e18f): Exponential backoff retry on socket reconnects
- [`000f1f2`](https://github.com/pixlcore/xysat/commit/000f1f2f90663a326825b4d4d3a8e7ce2d30510f): Daily log archive
- [`962ec90`](https://github.com/pixlcore/xysat/commit/962ec90a01be4d51ba122af1536875240cd96b74): Support for windows shell scripts.
- [`6361f07`](https://github.com/pixlcore/xysat/commit/6361f0744640b4bfb60151a03156578f00da79b6): Multiple...
- [`92b9930`](https://github.com/pixlcore/xysat/commit/92b9930a8cbeba8d916552fafd993e2b662a06b0): Multiple...
- [`8d7a71a`](https://github.com/pixlcore/xysat/commit/8d7a71a3a7e868620afff84261a2e9be51e5ff80): Multiple...
- [`60553b8`](https://github.com/pixlcore/xysat/commit/60553b85163daf3e4e33f17bac3a43bc468fead1): Init procCache, and only check psBin on Linux/macOS
- [`6464311`](https://github.com/pixlcore/xysat/commit/646431156534f105697dc6af28e0ff2d2620e410): Leave package.json file as it contains our version
- [`616b0b0`](https://github.com/pixlcore/xysat/commit/616b0b07a916b659a68d348cfee2e4acd9ef9024): Read version from package.json file
- [`293e065`](https://github.com/pixlcore/xysat/commit/293e065dc6714dacb816aee62f7091be42f14efb): Added clause for included software

## Version v0.0.15

> March 23, 2025

- [`97b2322`](https://github.com/pixlcore/xysat/commit/97b232245d4c27b7d6dd19a0e5b8cfcac8648fab): Version 0.0.15
	- Add support for merging in initial config push on first load.

## Version v0.0.14

> March 22, 2025

- [`37ac8c1`](https://github.com/pixlcore/xysat/commit/37ac8c1f2b4bd1bab144633f0162aac3edbc14e1): v0.0.14
- [`d644bd4`](https://github.com/pixlcore/xysat/commit/d644bd47aaa448e3fc577fec89578c7bcf32141a): Support for auth token style handshake with orchestra conductor

## Version v0.0.13

> March 22, 2025

- [`e9c51da`](https://github.com/pixlcore/xysat/commit/e9c51da81cccf7710d925896db63edbccd1e6764): Version 0.0.13
- [`0555ad3`](https://github.com/pixlcore/xysat/commit/0555ad3e95b41b6d9a4002cbad1e1f2d2849cd7c): More misc file cleanup
- [`628e290`](https://github.com/pixlcore/xysat/commit/628e290d5acf1fcdda2d07a4be122ee5c5494ef0): More file cleanup
- [`340824c`](https://github.com/pixlcore/xysat/commit/340824c1244d1f2cee2148803fb7bfbd421a8353): Change plugin loading location.
- [`09cc0a5`](https://github.com/pixlcore/xysat/commit/09cc0a5c4f5c9ce5a80077f85417f039d4c10240): Rename bin/ to plugins/

## Version v0.0.12

> March 22, 2025

- [`8ecc7e3`](https://github.com/pixlcore/xysat/commit/8ecc7e3e7973b50e075caf323e04a1fcfa6410fd): Version 0.0.12
- [`d5aadf7`](https://github.com/pixlcore/xysat/commit/d5aadf7b0dc4b8b808424670fcf73f261f97c775): New windows install handler
- [`83ca88f`](https://github.com/pixlcore/xysat/commit/83ca88f0f9b6cf8600b0fcdaf4ed40cd682233c5): Trying new strat for windows
- [`52d5d9d`](https://github.com/pixlcore/xysat/commit/52d5d9d7c8e42739f20c98156164cb4bc39a8c61): New windows bat files

## Version v0.0.11

> March 19, 2025

- [`9c5b377`](https://github.com/pixlcore/xysat/commit/9c5b377b1b41d9e455516f4e7e998ad3d13a39a3): Trying proper OS names for x64/arm builds.

## Version v0.0.10

> March 19, 2025

- [`39167af`](https://github.com/pixlcore/xysat/commit/39167af91b9455fbcdf5b98be3d2b97f07734197): Trying to use newfangled arch in GH actions

## Version v0.0.9

> March 19, 2025

- [`6e83479`](https://github.com/pixlcore/xysat/commit/6e83479bd3555b5186b599598e8ee4960fcc0c5a): Trying harder to make GitHub happy.

## Version v0.0.8

> March 19, 2025

- [`5b96c48`](https://github.com/pixlcore/xysat/commit/5b96c48badd5992c8fdbc7f70f261032d90d6510): Trying to make GH happy on the release step...

## Version v0.0.7

> March 19, 2025

- [`bca8526`](https://github.com/pixlcore/xysat/commit/bca85263aab38f0cb6a590691510b127d4979e0e): Trying more things to make Windows happy.

## Version v0.0.6

> March 19, 2025

- [`8470551`](https://github.com/pixlcore/xysat/commit/847055121c47b40e2a16d98909f63026ed2dcb86): Trying an alt way of tarring up the dir.

## Version v0.0.5

> March 19, 2025

- [`41101be`](https://github.com/pixlcore/xysat/commit/41101befc83525cadaf447a8f7bc69d286d64a57): Sigh, trying more things.

## Version v0.0.4

> March 19, 2025

- [`950136c`](https://github.com/pixlcore/xysat/commit/950136c3c4e9a1072f00fc690b5f92aa7c323dbd): Tryng new node-pty build with multi-os matrix.

## Version v0.0.3

> March 17, 2025

- [`b50102b`](https://github.com/pixlcore/xysat/commit/b50102bb62f69a4750967e823e1b87ac92fa2c7c): Version 0.0.3
	- More github action troubleshooting.

## Version v0.0.2

> March 17, 2025

- [`7c8b057`](https://github.com/pixlcore/xysat/commit/7c8b05703ca1621bcbde6b90f6cbd63b4ddd20ed): Version 0.0.2
- [`e1ca4f1`](https://github.com/pixlcore/xysat/commit/e1ca4f1dce133d62f5a6b04993aa065c2eb682e9): Typo fix in automation.

## Version v0.0.1

> March 17, 2025

- Initial beta release!
```

## File: `Dockerfile`
```
FROM node:22-bookworm-slim

LABEL org.opencontainers.image.source="https://github.com/pixlcore/xysat"
LABEL org.opencontainers.image.description="Remote satellite worker daemon for xyOps."
LABEL org.opencontainers.image.licenses="BSD-3-Clause"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
	zip unzip xz-utils bzip2 procps lsof \
    iputils-ping \
    dnsutils \
    openssh-client \
    net-tools \
    curl \
    wget \
    vim \
    less \
    sudo \
	iproute2 \
	tzdata \
	build-essential \
	python3 \
	python3-distutils \
    python3-setuptools \
    pkg-config \
	libc6-dev \
	libssl-dev \
	zlib1g-dev \
	libffi-dev \
	git \
	ca-certificates \
	gnupg

# install docker cli
RUN . /etc/os-release; \
  install -m 0755 -d /etc/apt/keyrings; \
  curl -fsSL "https://download.docker.com/linux/$ID/gpg" -o /etc/apt/keyrings/docker.asc; \
  chmod a+r /etc/apt/keyrings/docker.asc; \
  ARCH=$(dpkg --print-architecture); \
  echo "deb [arch=$ARCH signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/$ID ${UBUNTU_CODENAME:-$VERSION_CODENAME} stable" \
  > /etc/apt/sources.list.d/docker.list; \
  apt-get update && apt-get install -y --no-install-recommends docker-ce-cli;

# cleanup apt
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN mv /root/.local/bin/uv /usr/local/bin/uv
RUN mv /root/.local/bin/uvx /usr/local/bin/uvx

WORKDIR /opt/xyops/satellite
COPY . .

ENV NODE_ENV=production

ENV SATELLITE_foreground=true
ENV SATELLITE_echo=true
ENV SATELLITE_debug_level=5

RUN npm install

CMD ["sh", "container-start.sh"]
```

## File: `LICENSE.md`
```markdown
BSD 3-Clause License

Copyright (c) 2019 - 2026 PixlCore LLC & CONTRIBUTORS.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## File: `README.md`
```markdown
# Overview

**xyOps Satellite (xySat)** is a companion to the [xyOps](https://xyops.io) workflow automation and server monitoring platform.  It is both a job runner, and a data collector for server monitoring and alerting.  xySat is designed to be installed on *all* of your servers, so it is lean and mean, and has zero dependencies.

# Installation

See the [xySat Installation Guide](https://docs.xyops.io/hosting/satellite) for details.

## Manual Installation

If you would like to install xySat manually (for e.g. to run it as a non-root user), see below for the steps.

### Linux

<details><summary>Manual Linux Installation</summary>

First, click the "Add Server" button in the sidebar in the xyOps UI.  Select "Linux" as the target platform, and copy the one-line installer command.  It will look something like this:

```sh
curl -s "http://YOUR_XYOPS_SERVER:5522/api/app/satellite/install?t=AUTH_TOKEN" | sudo sh
```

We're not going to run this command as is, but we need the URL.  So copy the full URL, and create two new URLs by swapping out the word "install" like this:

- **Download Tarball:** `http://YOUR_XYOPS_SERVER:5522/api/app/satellite/core?t=AUTH_TOKEN&os=linux&arch=YOUR_ARCH`
- **Download Config:** `http://YOUR_XYOPS_SERVER:5522/api/app/satellite/config?t=AUTH_TOKEN`

Make sure you copy over the auth token *exactly* as it is shown.  In the tarball URL replace `YOUR_ARCH` with either `x64` or `arm64`, depending on your server's architecture.

Now, SSH to the Linux server you want to install xySat on.  Note that it needs to be installed in `/opt/xyops/satellite/` for everything to work correctly.  So you may need to become root to create this directory, but you can then `chown` it to another user before installing.  It is possible to run xySat in a different directory, but it is not recommended.

Here are the commands to get it installed and configured:

```sh
# create base directory and cd into it
mkdir -p /opt/xyops/satellite
cd /opt/xyops/satellite

# download tarball and extract
curl -fsSL "http://YOUR_XYOPS_SERVER:5522/api/app/satellite/core?t=AUTH_TOKEN&os=linux&arch=YOUR_ARCH" | tar zxf -

# Fetch custom config file for satellite
curl -fsSL "http://YOUR_XYOPS_SERVER:5522/api/app/satellite/config?t=AUTH_TOKEN" > config.json
chmod 600 config.json

# Set some permissions
chmod 775 *.sh bin/*

# Start it up (forks a background daemon)
./control.sh start
```

Notably, this installation method will not register xySat as a systemd service, so it is up to you to configure it to auto-start on boot if you want.

</details>

### macOS

<details><summary>Manual macOS Installation</summary>

First, click the "Add Server" button in the sidebar in the xyOps UI.  Select "macOS" as the target platform, and copy the one-line installer command.  It will look something like this:

```sh
curl -s "http://YOUR_XYOPS_SERVER:5522/api/app/satellite/install?t=AUTH_TOKEN&os=macos" | sudo sh
```

We're not going to run this command as is, but we need the URL.  So copy the full URL, and create two new URLs by swapping out the word "install" like this:

- **Download Tarball:** `http://YOUR_XYOPS_SERVER:5522/api/app/satellite/core?t=AUTH_TOKEN&os=macos&arch=YOUR_ARCH`
- **Download Config:** `http://YOUR_XYOPS_SERVER:5522/api/app/satellite/config?t=AUTH_TOKEN`

Make sure you copy over the auth token *exactly* as it is shown.  In the tarball URL replace `YOUR_ARCH` with either `x64` (Intel) or `arm64` (Apple Silicon), depending on your Mac's architecture.

Now, open Terminal.app on the macOS machine you want to install xySat on.  Note that it needs to be installed in the `/opt/xyops/satellite/` directory for everything to work correctly.  So you may need to become root to create this directory, but you can then `chown` it to another user before installing.  It is possible to run xySat in a different directory, but it is not recommended.

Here are the commands to get it installed and configured:

```sh
# create base directory and cd into it
mkdir -p /opt/xyops/satellite
cd /opt/xyops/satellite

# download tarball and extract
curl -fsSL "http://YOUR_XYOPS_SERVER:5522/api/app/satellite/core?t=AUTH_TOKEN&os=macos&arch=YOUR_ARCH" | tar zxf -

# Fetch custom config file for satellite
curl -fsSL "http://YOUR_XYOPS_SERVER:5522/api/app/satellite/config?t=AUTH_TOKEN" > config.json
chmod 600 config.json

# Set some permissions
chmod 775 *.sh bin/*

# Start it up (forks a background daemon)
./control.sh start
```

Notably, this installation method will not register xySat as a [LaunchAgent/LaunchDaemon](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html), so it is up to you to configure it to auto-start on boot if you want.

</details>

### Windows

<details><summary>Manual Windows Installation</summary>

First, click the "Add Server" button in the sidebar in the xyOps UI.  Select "Windows" as the target platform, and copy the one-line installer command.  It will look something like this:

```sh
powershell -Command "IEX (Invoke-WebRequest -UseBasicParsing -Uri 'http://YOUR_XYOPS_SERVER:5522/api/app/satellite/install?t=AUTH_TOKEN&os=windows').Content"
```

We're not going to run this command as is, but we need the URL.  So copy the full URL, and then create two new URLs by swapping out the word "install" like this:

- **Download Tarball:** `http://YOUR_XYOPS_SERVER:5522/api/app/satellite/core?t=AUTH_TOKEN&os=windows&arch=x64`
- **Download Config:** `http://YOUR_XYOPS_SERVER:5522/api/app/satellite/config?t=AUTH_TOKEN`

Make sure you copy over the auth token *exactly* as it is shown.  Note that only Windows on x64 is supported at this time.  Final steps:

1. Create a new folder for xySat to live in on the target Windows machine.
2. Download and decompress the tarball into the new folder.
3. Download the config file and save it in the new folder.  It should be named `config.json`.
4. Start the process as shown below:

Open a command prompt and type these commands:

```
cd C:\PATH\TO\NEW\XYSAT\FOLDER
bin\node.exe main.js --echo --foreground
```

Notably, this installation method will not register xySat as a Windows service, so it is up to you to configure it to auto-start on boot if you want.  Also, you'll need to keep the terminal window open to keep it running (minimized is fine).

</details>

# Configuration

See the [xySat Configuration Guide](https://docs.xyops.io/config/satellite) for details.

# Development

You can install the source code by using [Git](https://en.wikipedia.org/wiki/Git) ([Node.js](https://nodejs.org/) is also required):

```sh
git clone https://github.com/pixlcore/xysat.git
cd xysat
npm install
```

You can then run it in debug mode by issuing this command:

```sh
node --trace-warnings main.js --debug --debug_level 9 --echo
```

# License

See [LICENSE.md](LICENSE.md) in this repository.

## Included Software

This software includes the Node.js runtime engine, which is licensed separately:

https://github.com/nodejs/node/blob/main/LICENSE
```

## File: `SECURITY.md`
```markdown
# Security

## Overview

The xyOps team takes security very seriously. Due to the nature of how xyOps is installed on large server fleets a lot of decisions are made with security being the priority, and we always aim to implement security by design.

## Coordinated vulnerability disclosure

xyOps follows the [coordinated vulnerability disclosure](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure) model when dealing with security vulnerabilities. This was previously known as responsible disclosure. We strongly urge anyone reporting vulnerabilities to xyOps or any other project to follow this model as it is considered as a best practice by many in the security industry.

If you believe you have identified a security vulnerability or security related bug with xyOps please make every effort to contact us privately using one of the contact options below. Please do not open an issue, do not notify us in public, and do not disclose this issue to third parties.

Using this process helps ensure that users affected have an avenue to fixing the issue as close to the issue being made public as possible. This mitigates the increasing the attack surface (via improving attacker knowledge) for diligent administrators simply via the act of disclosing the security issue.

## Contact Options

Several contact options exist however it's important you specifically use a security contact method when reporting a security vulnerability or security related bug. These methods are clearly documented below.

### GitHub Security

Users can utilize GitHub's security vulnerability system to privately [report a vulnerability](https://github.com/pixlcore/xysat/security/advisories/new). This is an easy method for users who have a GitHub account.

### Email

Users can utilize the [security@pixlcore.com](mailto:security@pixlcore.com) email address to privately report a vulnerability. This is an easy method of users who do not have a GitHub account.

This email account is only accessible by members of the core team for the purpose of disclosing security vulnerabilities and issues within the xyOps code base.

## Process

1. The user privately reports a potential vulnerability.
2. The report is acknowledged as received.
3. The report is reviewed to ascertain if additional information is required. If it is required:
   1. The user is informed that the additional information is required.
   2. The user privately adds the additional information.
   3. The process begins at step 3 again, proceeding to step 4 if the additional information provided is sufficient.
4. The vulnerability is reproduced.
5. The vulnerability is patched, and if possible the user reporting the bug is given access to a fixed binary, docker image, and git patch.
6. The patch is confirmed to resolve the vulnerability.
7. The fix is released and users are notified that they should update urgently.
8. The [security advisory](https://github.com/pixlcore/xysat/security/advisories) is published when (whichever happens sooner):
  - The CVE details are published by [MITRE](https://www.mitre.org/), [NIST](https://www.nist.gov/), etc.
  - Roughly 7 days after users have been notified the update is available.

## Credit

Users who report bugs will at their discretion (i.e. they do not have to be if they wish to remain anonymous) be credited for the discovery. Both in the [security advisory](https://github.com/pixlcore/xysat/security/advisories) and in our documentation.
```

## File: `container-start.sh`
```bash
#!/bin/sh
set -e

# add some common path locations
export PATH=$PATH:/usr/bin:/bin:/usr/local/bin:/usr/sbin:/sbin:/usr/local/sbin:$HOME/.local/bin

# check for bootstrap env var, but only on first run
CONFIG_FILE="${XYSAT_config_file:-config.json}"

if [ -n "$XYOPS_setup" ] && [ ! -s "$CONFIG_FILE" ]; then
	echo "Configuring xySat: $XYOPS_setup"
	curl -fsSL --connect-timeout 10 --retry 10 --retry-delay 5 --retry-connrefused --retry-all-errors "$XYOPS_setup" -o "$CONFIG_FILE"
	chmod 600 "$CONFIG_FILE"
fi

# check for foreground
if [ -n "${SATELLITE_foreground:-}" ]; then
    # cleanup pid file
	rm -f pid.txt

	# start xysat, replace current process
	exec node main.js start
else
    echo "ERROR: This script is for containers only."
fi
```

## File: `control.sh`
```bash
#!/bin/bash
#
# Control script designed to allow an easy command line interface
# to controlling any binary.  Written by Marc Slemko, 1997/08/23
# Modified for xySat, Joe Huckaby, 2026/01/17
# 
# The exit codes returned are:
#	0 - operation completed successfully
#	2 - usage error
#	3 - binary could not be started
#	4 - binary could not be stopped
#	8 - configuration syntax error
#
# When multiple arguments are given, only the error from the _last_
# one is reported.  Run "*ctl help" for usage info
#
#
# |||||||||||||||||||| START CONFIGURATION SECTION  ||||||||||||||||||||
# --------------------                              --------------------
#
# add some common path locations
export PATH=$PATH:/usr/bin:/bin:/usr/local/bin:/usr/sbin:/sbin:/usr/local/sbin:/opt/xyops/satellite/bin
# 
# the name of your binary
NAME="xyOps Satellite"
#
# home directory
HOMEDIR="$(cd -- "$(dirname "$0")" && pwd -P)"
cd $HOMEDIR
#
# the path to your binary, including options if necessary
BINARY="node $HOMEDIR/main.js"
#
# the path to your PID file
PIDFILE=$HOMEDIR/pid.txt
#
# --------------------                              --------------------
# ||||||||||||||||||||   END CONFIGURATION SECTION  ||||||||||||||||||||

if [ -n "${SATELLITE_foreground:-}" ]; then
	echo "Error: The control script is not for use in containers." >&2
	exit 1
fi

ERROR=0
ARGV="$@"
if [ "x$ARGV" = "x" ] ; then 
	ARGS="help"
fi

for ARG in $@ $ARGS
do
	# check for pidfile
	if [ -f $PIDFILE ] ; then
		PID=`cat $PIDFILE`
		if [ "x$PID" != "x" ] && kill -0 $PID 2>/dev/null ; then
			# make sure process is actually ours
			PS=`ps -p $PID -o args= | sed 's/[ \t]*$//'`
			
			if [ "$PS" = "$NAME" ] ; then
				STATUS="$NAME running (pid $PID)"
				RUNNING=1
			else
				STATUS="$NAME not running (pid $PID?)"
				RUNNING=0
			fi
			
		else
			STATUS="$NAME not running (pid $PID?)"
			RUNNING=0
		fi
	else
		STATUS="$NAME not running (no pid file)"
		RUNNING=0
	fi

	case $ARG in
	start)
		if [ $RUNNING -eq 1 ]; then
			echo "$ARG: $NAME already running (pid $PID)"
			continue
		fi
		echo "$0 $ARG: Starting up $NAME..."
		if $BINARY ; then
			echo "$0 $ARG: $NAME started"
		else
			echo "$0 $ARG: $NAME could not be started"
			ERROR=3
		fi
	;;
	stop)
		if [ $RUNNING -eq 0 ]; then
			echo "$ARG: $STATUS"
			continue
		fi
		if kill $PID ; then
			while kill -0 "$PID" 2>/dev/null; do
				sleep 1;
			done
			echo "$0 $ARG: $NAME stopped"
		else
			echo "$0 $ARG: $NAME could not be stopped"
			ERROR=4
		fi
	;;
	restart)
		$0 stop start
	;;
	status)
		echo "$ARG: $STATUS"
	;;
	*)
	echo "usage: $0 (start|stop|restart|status|help)"
	cat <<EOF

start      - Starts $NAME.
stop       - Stops $NAME and wait until it actually exits.
restart    - Calls stop, then start (hard restart).
status     - Checks whether $NAME is currently running.
help       - Displays this screen.

EOF
	ERROR=2
	;;

	esac

done

exit $ERROR

## ====================================================================
## The Apache Software License, Version 1.1
##
## Copyright (c) 2000 The Apache Software Foundation.  All rights
## reserved.
##
## Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions
## are met:
##
## 1. Redistributions of source code must retain the above copyright
##    notice, this list of conditions and the following disclaimer.
##
## 2. Redistributions in binary form must reproduce the above copyright
##    notice, this list of conditions and the following disclaimer in
##    the documentation and/or other materials provided with the
##    distribution.
##
## 3. The end-user documentation included with the redistribution,
##    if any, must include the following acknowledgment:
##       "This product includes software developed by the
##        Apache Software Foundation (http://www.apache.org/)."
##    Alternately, this acknowledgment may appear in the software itself,
##    if and wherever such third-party acknowledgments normally appear.
##
## 4. The names "Apache" and "Apache Software Foundation" must
##    not be used to endorse or promote products derived from this
##    software without prior written permission. For written
##    permission, please contact apache@apache.org.
##
## 5. Products derived from this software may not be called "Apache",
##    nor may "Apache" appear in their name, without prior written
##    permission of the Apache Software Foundation.
##
## THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESSED OR IMPLIED
## WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
## OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
## DISCLAIMED.  IN NO EVENT SHALL THE APACHE SOFTWARE FOUNDATION OR
## ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
## USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
## ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
## OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
## OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
## SUCH DAMAGE.
## ====================================================================
##
## This software consists of voluntary contributions made by many
## individuals on behalf of the Apache Software Foundation.  For more
## information on the Apache Software Foundation, please see
## <http://www.apache.org/>.
##
## Portions of this software are based upon public domain software
## originally written at the National Center for Supercomputing Applications,
## University of Illinois, Urbana-Champaign.
##
# 
```

## File: `debug.sh`
```bash
#!/bin/bash

node --trace-warnings main.js --debug --debug_level 9 --echo "$@"
```

## File: `install.sh`
```bash
#!/bin/sh

# Copyright (c) 2019 - 2025 PixlCore LLC
# BSD 3-Clause License -- see LICENSE.md

cd "$(dirname "$0")" || exit 1

# Install and start xyOps Satellite
./bin/node main.js install || exit 1
./bin/node main.js start || exit 1
```

## File: `main.js`
```javascript
#!/usr/bin/env node

// xySat - xyOps Satellite - Main entry point
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

const Path = require('path');
const fs = require('fs');
const cp = require('child_process');
const os = require('os');
const PixlServer = require("pixl-server");
const pkg = require('./package.json');
const self_bin = Path.resolve(process.argv[0]) + ' ' + Path.resolve(process.argv[1]);
const config_file = process.env.XYSAT_config_file || Path.join( __dirname, 'config.json' );
const is_windows = !!process.platform.match(/^win/);

var config = {};
var sample_config = {
	hosts: [ "localhost" ],
	port: 5522,
	secure: false,
	socket_opts: { rejectUnauthorized: false },
	pid_file: "pid.txt",
	log_dir: "logs",
	log_filename: "[component].log",
	log_crashes: true,
	log_archive_path: "logs/archives/[filename]-[yyyy]-[mm]-[dd].log.gz",
	log_archive_keep: "7 days",
	temp_dir: "temp",
	debug_level: 5,
	child_kill_timeout: 10,
	monitoring_enabled: true,
	quickmon_enabled: true
};

const cli = require('pixl-cli');
var Tools = cli.Tools;
var args = cli.args;
cli.global();

// special windows install mode
if ((args.install || args.uninstall || args.stop) && is_windows) {
	// install as a windows service, or uninstall
	process.chdir( __dirname );
	
	// patch out console.log because node-windows dumps debug info to it
	// see: https://github.com/coreybutler/node-windows/issues/382
	console.log = function() {};
	
	var Service = require('node-windows').Service;
	var svc = new Service({
		name: 'xyOps Satellite',
		description: 'xyOps Satellite',
		script: Path.resolve(  __dirname, 'main.js' ),
		execPath: process.execPath,
		scriptOptions: [ '--foreground' ],
		delayedAutoStart: true
	});
	
	if (args.install) {
		svc.on('start', function() {
			print("\nxyOps Satellite has been started successfully.\n\n");
			process.exit(0);
		});
		
		svc.on('error', function(err) {
			print("\nWindows Service Installation Error: " + err + "\n\n");
			process.exit(1);
		});
		
		var installCompleted = function() {
			print("\nxyOps Satellite has been installed successfully.\n");
			
			if (!fs.existsSync(config_file)) {
				config = sample_config;
				var raw_config = JSON.stringify( config, null, "\t" );
				fs.writeFileSync( config_file, raw_config, { mode: 0o600 } );
				print("\nA sample config file has been created: " + config_file + ":\n");
				print( raw_config + "\n" );
				process.exit(0);
			}
			else {
				svc.start();
			}
		};
		svc.on('install', installCompleted);
		svc.on('alreadyinstalled', installCompleted);
		
		svc.install();
	} // install
	
	if (args.uninstall) {
		const task = `xysat-delete-${Date.now()}`;
		const logFile = Path.join(os.tmpdir(), `${task}.log`);
		cli.setLogFile( logFile );
		println("Uninstalling xyOps Satellite...");
		
		var scheduleBackgroundDelete = function() {
			println("Preparing final background deletion process...");
			try { 
				// kill main process if still running
				var pid = parseInt( fs.readFileSync( 'pid.txt', 'utf8' ) ); 
				if (pid) process.kill( pid, 'SIGTERM' );
			} catch (e) {;}
			
			// delete directory in background using schtasks
			const installDir = __dirname;
  			try { process.chdir(os.tmpdir()); } catch {}
			
			const psFile = Path.join(os.tmpdir(), `${task}.ps1`);
			const escPS = (s) => s.replace(/'/g, "''"); // for single-quoted PS strings
			
			const ps = [
				`$log = '${escPS(logFile)}'`,
				`function Log($msg) {`,
				`  $ts = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss.fff')`,
				`  Add-Content -LiteralPath $log -Value ("[$ts] " + $msg)`,
				`}`,
				``,
				`Log "BEGIN self-delete script"`,
				`Log ("Script path: " + $MyInvocation.MyCommand.Path)`,
				`Log ("Target dir:  ${escPS(installDir)}")`,
				`Log "Sleeping for 10 seconds..."`,
				`Start-Sleep -Seconds 10`,
				``,
				`try {`,
				`  if (Test-Path -LiteralPath '${escPS(installDir)}') {`,
				`    Log "Attempting Remove-Item..."`,
				`    $err = $null`,
				`    Remove-Item -LiteralPath '${escPS(installDir)}' -Recurse -Force -ErrorAction SilentlyContinue -ErrorVariable err`,
				`    if (Test-Path -LiteralPath '${escPS(installDir)}') {`,
				`      Log "Remove-Item completed but target still exists."`,
				`      if ($err) { Log ("Remove-Item error: " + ($err | Out-String).Trim()) }`,
				`    } else {`,
				`      Log "SUCCESS: target deleted."`,
				`    }`,
				`  } else {`,
				`    Log "Target did not exist at delete time."`,
				`  }`,
				`} catch {`,
				`  Log ("EXCEPTION: " + $_.Exception.Message)`,
				`}`,
				``,
				`Log "Cleaning up script file..."`,
				`try { Remove-Item -LiteralPath $MyInvocation.MyCommand.Path -Force -ErrorAction SilentlyContinue } catch {}`,
				`Log "END self-delete script"`
			].join('\n') + '\n';
			
			fs.writeFileSync(psFile, ps, 'utf8');
			cli.log("Temp Script: " + psFile);
			
			const tr = `powershell.exe -NoProfile -ExecutionPolicy Bypass -File \\"${psFile}\\"`;
			let cmd = `schtasks /Create /TN "${task}" /SC ONCE /ST 00:00 /SD 01/01/2000 /RU SYSTEM /RL HIGHEST /TR "${tr}"`;
			cmd += ` && schtasks /Run /TN "${task}" && schtasks /Delete /TN "${task}" /F`;
			cli.log("Executing Command: " + cmd);
			
			const child = cp.spawn(cmd, {
				shell: true,
				detached: true,
				stdio: 'ignore',
				windowsHide: true
			});
			child.unref();
			
			print("\nBackground deletion was scheduled successfully.\n\n");
		}; // scheduleBackgroundDelete
		
		scheduleBackgroundDelete();
		
		svc.on('uninstall', function() {
			println("Service 'uninstall' hook has fired.");
		});
		svc.on('alreadyuninstalled', function() {
			println("Service 'alreadyuninstalled' hook has fired.");
		});
		
		svc.on('error', function(err) {
			print("\nWindows Service Error: " + err + "\n\n");
			process.exit(1);
		});
		
		setTimeout( function() { 
			// giving scheduleBackgroundDelete a chance to register the task
			// svc.uninstall seems to kill the current process, so we have to do it last
			println("Calling service uninstall...");
			svc.uninstall();
		}, 1000 );
		
	} // uninstall
	
	if (args.stop) {
		svc.on('stop', function() {
			print("\nxyOps Satellite has been stopped.\n\n");
			process.exit(0);
		});
		
		svc.on('error', function(err) {
			print("\nWindows Service Error: " + err + "\n\n");
			process.exit(1);
		});
		
		svc.stop();
	} // stop
	
	return;
} // windows

// setup pixl-boot for startup service
var boot = require('pixl-boot');
var boot_opts = {
	name: "xysat",
	company: "PixlCore LLC",
	script: self_bin,
	linux_type: "forking",
	linux_after: "network.target",
	linux_wanted_by: "multi-user.target",
	darwin_type: "agent"
};

if (args.install || (args.other && (args.other[0] == 'install'))) {
	// first time install
	process.chdir( __dirname );
	boot.install(boot_opts, function(err) {
		if (err) throw err;
		
		print("\nxyOps Satellite has been installed successfully.\n");
		
		if (!fs.existsSync(config_file)) {
			config = sample_config;
			var raw_config = JSON.stringify( config, null, "\t" );
			fs.writeFileSync( config_file, raw_config, { mode: 0o600 } );
			print("\nA sample config file has been created: " + config_file + ":\n");
			print( raw_config + "\n" );
		}
		
		print("\n");
		process.exit(0);
	} );
}
else if (args.uninstall || (args.other && (args.other[0] == 'uninstall'))) {
	// uninstall satellite
	process.chdir( __dirname );
	boot.uninstall(boot_opts, function(err) {
		try { 
			// kill main process if still running
			var pid = parseInt( fs.readFileSync( 'pid.txt', 'utf8' ) ); 
			if (pid) process.kill( pid, 'SIGTERM' );
		} catch (e) {;}
		
		// delete entire sat directory
		try { Tools.rimraf.sync( __dirname ); }
		catch (e) { die("\nError: Failed to delete folder: " + __dirname + ": " + e + "\n\n"); }
		
		print("\nxyOps Satellite has been removed successfully.\n");
		print("\n");
		process.exit(0);
	} );
}
else if (args.stop || (args.other && (args.other[0] == 'stop'))) {
	// shutdown if running
	process.chdir( __dirname );
	var pid = 0;
	try { pid = parseInt( fs.readFileSync( 'pid.txt', 'utf8' ) ); } catch (e) {;}
	if (!pid) die("\nError: xyOps Satellite is not currently running.\n\n");
	
	try { process.kill( pid, 'SIGTERM' ); }
	catch (err) {
		die("\nError: Failed to stop process: " + err + "\n\n");
	}
	
	// wait for pid to actually exit
	var checkExit = function() {
		try { process.kill(pid, 0); }
		catch (e) { process.exit(0); }
		setTimeout( checkExit, 250 );
	}
	checkExit();
}
else if (args.plugin || (args.other && (args.other[0] == 'plugin') && args.other[1])) {
	// execute plugin
	var plugin_name = Path.basename(args.plugin || args.other[1]);
	var plugin_file = Path.resolve( __dirname, Path.join( 'plugins', plugin_name + '.js' ) );
	if (!fs.existsSync(plugin_file)) die("\nError: Unknown plugin: " + plugin_name + "\n\n");
	
	process.title = plugin_name + '.js';
	require(plugin_file);
}
else {
	// normal startup
	process.chdir( __dirname );
	if (!fs.existsSync(config_file)) {
		// create sample config file if needed (user may have skipped the install step)
		fs.writeFileSync( config_file, JSON.stringify( sample_config, null, "\t" ), { mode: 0o600 } );
	}
	
	// map XYSAT_ env vars to SATELLITE_, for convenience
	for (var key in process.env) {
		if (key.match(/^XYSAT_(.+)$/)) process.env[ 'SATELLITE_' + RegExp.$1 ] = process.env[key];
	}
	
	// merge CLI into config file and save it
	delete args.start;
	delete args.other;
	
	if (Tools.numKeys(args) && !args.debug && !args.echo) {
		var temp_config = Tools.mergeHashes( JSON.parse( fs.readFileSync( config_file, 'utf8' ) ), args );
		fs.writeFileSync( config_file, JSON.stringify(temp_config, null, "\t") + "\n", { mode: 0o600 } );
	}
	
	// start server
	var server = new PixlServer({
		__name: 'Satellite',
		__version: pkg.version,
		
		configFile: config_file,
		
		components: [
			require('./lib/engine.js')
		]
	});
	
	server.startup( function() {
		// server startup complete
		process.title = "xyOps Satellite";
		
		if (server.config.get('auth_token')) {
			server.logDebug(3, "Authentication method: auth_token");
		}
		else if (server.config.get('secret_key')) {
			server.logDebug(3, "Authentication method: secret_key");
		}
		else {
			server.logDebug(1, "ERROR: Both auth_token and secret_key are missing from config. Shutting down.");
			server.shutdown();
		}
	} );
	
	if (is_windows) {
		// hook logger error event for windows event viewer
		var EventLogger = require('node-windows').EventLogger;
		var win_log = new EventLogger('xyOps');
		
		win_log.info( "xyOps Satellite v" + pkg.version + " starting up" );
		
		server.logger.on('row', function(line, cols, args) {
			if (args.category == 'error') win_log.error( line );
			else if ((args.category == 'debug') && (args.code == 1)) win_log.info( line );
		});
	}
	
	// process.once('SIGINT', function() {
	// 	// Note: Doesn't pixl-server take care of this?  Why are we hooking SIGINT in main.js?
	// 	// Ohhhh did this have something to do with the ptty lib?
	// 	server.shutdown();
	// });
}
```

## File: `package.json`
```json
{
	"name": "xysat",
	"version": "1.0.15",
	"private": true,
	"description": "Remote satellite worker daemon for xyOps.",
	"author": "Joseph Huckaby <jhuckaby@pixlcore.com>",
	"homepage": "https://github.com/pixlcore/xysat",
	"license": "BSD-3-Clause",
	"bin": "main.js",
	"main": "main.js",
	"scripts": {
		"changelog": "node tools/changelog.js"
	},
	"repository": {
		"type": "git",
		"url": "https://github.com/pixlcore/xysat"
	},
	"bugs": {
		"url": "https://github.com/pixlcore/xysat/issues"
	},
	"keywords": [
		"xyops",
		"xysat"
	],
	"dependencies": {
		"async": "2.6.4",
		"class-plus": "^1.0.0",
		"node-notifier": "10.0.1",
		"node-pty": "1.1.0",
		"pixl-boot": "^2.0.2",
		"pixl-cli": "^1.0.0",
		"pixl-json-stream": "^1.0.7",
		"pixl-perf": "^1.0.9",
		"pixl-request": "^2.6.1",
		"pixl-server": "^1.0.50",
		"pixl-tools": "^2.0.2",
		"pixl-xml": "^1.0.0",
		"shell-quote": "1.8.2",
		"systeminformation": "5.31.5",
		"ws": "7.5.10"
	}
}
```

## File: `uninstall.sh`
```bash
#!/bin/sh

# Copyright (c) 2019 - 2025 PixlCore LLC
# BSD 3-Clause License -- see LICENSE.md

cd "$(dirname "$0")" || exit 1

# Uninstall xyOps Satellite
./bin/node main.js uninstall || exit 1
```

## File: `lib/comm.js`
```javascript
// xySat - xyOps Satellite - Communication Layer
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

const fs = require('fs');
const Path = require('path');
const cp = require('child_process');
const WebSocket = require('ws');
const Class = require("class-plus");
const Tools = require("pixl-tools");

module.exports = Class({
	
	socket: null,
	tempHost: null
	
},
class Communication {
	
	logComm(level, msg, data) {
		// log debug msg with pseudo-component
		if (this.debugLevel(level)) {
			this.logger.set( 'component', 'Comm' );
			this.logger.print({ category: 'debug', code: level, msg: msg, data: data });
		}
	}
	
	socketInit() {
		// called on startup and config reload
		this.connectTimeoutSec = this.config.get('connect_timeout_sec') || 5;
		this.pingTimeoutSec = this.config.get('ping_timeout_sec') || 60;
		this.sockReconnDelaySec = this.config.get('socket_reconnect_delay_sec') || 1;
		this.sockReconnDelayMax = this.config.get('socket_reconnect_delay_max') || 30;
		this.sockReconnDelayCur = this.sockReconnDelaySec;
	}
	
	socketDisconnect() {
		// kill socket if connected, and prevent auto-reconnect
		if (this.socket) {
			this.socket.forceDisconnect = true;
			this.logComm(9, "Destroying previous socket");
			this.socket.close();
			this.socket = null;
		}
	}
	
	socketConnect() {
		// connect to server via websocket
		var self = this;
		var url = '';
		var host = this.config.get('host') || Tools.randArray(this.config.get('hosts'));
		var port = this.config.get('port');
		delete this.reconnectTimer;
		
		if (this.tempHost && !this.config.get('host')) {
			// one-time connect (i.e. redirect to master)
			host = this.tempHost;
			delete this.tempHost;
		}
		url = (this.config.get('secure') ? 'wss:' : 'ws:') + '//' + host + ':' + port + '/';
		
		// make sure old socket is disconnected
		this.socketDisconnect();
		
		this.logComm(5, "Connecting to WebSocket: " + url);
		
		// custom socket abstraction layer
		var socket = this.socket = {
			host: host,
			port: port,
			url: url,
			secure: !!this.config.get('secure'),
			ws: new WebSocket( url, this.config.get('socket_opts') || {} ),
			
			connected: false,
			disconnected: false,
			
			connectTimer: setTimeout( function() {
				self.logError('comm', "Socket connect timeout (" + self.connectTimeoutSec + " sec)");
				socket.close();
			}, this.connectTimeoutSec * 1000 ),
			
			send: function(cmd, data) {
				self.logComm(10, "Sending socket message: " + cmd, data);
				
				if (this.connected) this.ws.send( JSON.stringify({ cmd: cmd, data: data }) );
				else self.logError('socket', "Socket not connected, message not sent", { cmd, data });
			},
			
			close: function() {
				try { 
					this.ws.close(); 
				} 
				catch(err) {
					this.ws.terminate();
				}
			}
		};
		
		socket.ws.onerror = function(err) {
			// socket error
			if (err.error) err = err.error; // ws weirdness
			self.logError('comm', "Socket Error: " + (err.message || err.code || err), { host: socket.host, url: socket.url } );
		};
		
		socket.ws.onopen = function (event) {
			// socket connected
			if (socket.connectTimer) {
				clearTimeout( socket.connectTimer );
				delete socket.connectTimer;
			}
			
			// reset reconn delay to base level
			self.sockReconnDelayCur = self.sockReconnDelaySec;
			
			socket.connected = true;
			socket.lastPing = Tools.timeNow();
			
			self.logComm(1, "WebSocket connected successfully: " + url);
			
			self.getBasicServerInfo( function(info) {
				// start auth challenge, include basic info like os, cpu, mem
				self.logComm(5, "Sending initial hello message");
				socket.send( 'hello', Tools.mergeHashes( self.config.get('initial') || {}, {
					hostname: self.server.hostname,
					id: self.config.get('server_id') || '',
					info: info
				} ) );
			}); // getBasicServerInfo
		};
		
		socket.ws.onmessage = function (event) {
			// got message from server, parse JSON and handle
			self.logComm(10, "Got message from server: " + event.data);
			var json = null;
			try { 
				json = JSON.parse( event.data ); 
			}
			catch (err) {
				self.logError('comm', "Failed to parse JSON: " + err);
			}
			if (json) self.handleSocketMessage(json);
		};
		
		socket.ws.onclose = function (event) {
			// socket has closed
			var was_connected = socket.connected;
			
			if (was_connected) {
				// socket was connected, and now isn't
				self.logComm(3, "Socket has closed");
			}
			else {
				// socket was already disconnected, so increase retry delay (expon backoff)
				self.sockReconnDelayCur = Math.min( self.sockReconnDelayCur * 2, self.sockReconnDelayMax );
			}
			
			socket.disconnected = true;
			socket.connected = false;
			
			if (socket.connectTimer) {
				clearTimeout( socket.connectTimer );
				delete socket.connectTimer;
			}
			if (socket.forceDisconnect) {
				// deliberate disconnect, stop here
				return;
			}
			
			self.logComm(5, `Will attempt to reconnect in ${self.sockReconnDelayCur} seconds`);
			self.reconnectTimer = setTimeout( function() { self.socketConnect(); }, self.sockReconnDelayCur * 1000 );
			self.socket = null;
			
			if (was_connected) {
				// socket was connected, and now isn't, so log into all job metas
				self.appendMetaLogAllJobs("Lost connection to conductor");
			}
		};
	}
	
	handleSocketMessage(json) {
		// process message from master server
		var self = this;
		var socket = this.socket;
		if (!socket) return; // sanity
		
		var cmd = json.cmd;
		var data = json.data;
		
		switch (cmd) {
			case 'echo':
				// send back same data we got
				socket.lastPing = Tools.timeNow();
				socket.send('echoback', data);
			break;
			
			case 'auth_failure':
				// authentiation failure (should never happen)
				var msg = data.description;
				this.logError('comm', "Authentication failure: " + msg);
				
				// close socket until config reload
				this.logComm(3, "Closing socket until config reload or service restart");
				this.socketDisconnect();
			break;
			
			case 'hello':
				// response to initial hello, should have nonce for us to hash
				self.logComm(5, "Answering auth challenge");
				
				// if we were assigned an ID, save it permanently
				if (data.id && !this.config.get('server_id')) {
					this.logComm(3, "We have been assigned a unique server ID: " + data.id);
					this.updateConfig({
						server_id: data.id
					});
				}
				
				// log partial token or secret + nonce (first 4 chars of each)
				if (this.config.get('auth_token')) {
					this.logComm(5, "Authenticating via auth_token: " + this.config.get('auth_token').substring(0, 4) + '****');
				}
				else {
					this.logComm(5, "Authenticating via secret_key + nonce hash: " + 
						this.config.get('secret_key').substring(0, 4) + '**** + ' + data.nonce.substring(0, 4) + '****');
				}
				
				// continue auth challange
				socket.send('join', {
					token: this.config.get('auth_token') || Tools.digestHex( data.nonce + this.config.get('secret_key'), 'sha256' )
				});
			break;
			
			case 'joined':
				// auth successful
				this.logComm(5, "WebSocket auth successful!");
				socket.auth = true;
				
				this.updateConfig( Tools.mergeHashes( data.config || {}, {
					hosts: data.masterData.masters
				} ) );
				
				// set or update airgapped mode
				this.airgapSetup();
				
				// save current server count for quickmon timing adjust
				this.numServers = data.numServers || 0;
				
				// save stuff for minute monitoring
				this.groups = data.groups || [];
				this.plugins = data.plugins || [];
				this.commands = data.commands || [];
				this.prepPlugins();
				this.checkStartupLogFiles();
				
				// server may tell us what features it supports (xyops v1.0.15+)
				this.conductorFeatures = data.features || {};
				if (data.features) this.logComm(9, "Conductor features", data.features);
				
				if (Tools.numKeys(this.activeJobs)) {
					// if we have active jobs, this is a "reconnect" event
					this.updateAllJobs({
						reconnected: Tools.timeNow()
					});
					this.appendMetaLogAllJobs("Reconnected to conductor server: " + this.socket.host);
				}
				else {
					// fire off initial monitoring pass
					this.runMonitors({ max_sleep_ms: 1 });
				}
			break;
			
			case 'masterData':
				// auth successful
				this.logComm(5, "Received new masterData", data);
				this.updateConfig({
					hosts: data.masters
				});
			break;
			
			case 'redirect':
				// reconnect to new master
				this.logComm(5, "Reconnecting to new master", data);
				this.tempHost = data.host;
				socket.close();
			break;
			
			case 'retry':
				// reconnect after an interval (master not ready yet)
				this.logComm(5, "Master is not ready: will reconnect");
				socket.close();
			break;
			
			case 'launch_job':
				// prep and launch job
				this.prepLaunchJob(data.job, data.details || {}, data.sec || {});
			break;
			
			case 'abort_job':
				// abort job
				this.abortJob(data);
			break;
			
			case 'update':
				// arbitrary data update from master
				// e.g. groups, commands
				Tools.mergeHashInto( this, data );
				this.prepPlugins();
			break;
			
			case 'updateConfig':
				// arbitrary config update (likely new auth token from key rotation)
				this.logComm(5, "Received new config update", { keys: Object.keys(data) });
				this.updateConfig(data);
			break;
			
			case 'upgrade':
				// self upgrade
				this.upgradeSatellite();
			break;
			
			case 'uninstall':
				// full shutdown and uninstall
				this.uninstallSatellite();
			break;
			
			case 'testMonitorPlugin':
				this.testMonitorPlugin(data);
			break;
			
			// more commands here
			
		} // switch cmd
	}
	
	airgapSetup() {
		// setup things for airgapped mode
		var airgap = this.config.get('airgap') || {};
		if (!airgap.enabled) {
			this.request.setWhitelist( false );
			this.request.setBlacklist( false );
			return;
		}
		
		this.logDebug(3, "Setting up airgapped mode", airgap);
		
		if (airgap.whitelist && airgap.whitelist.length) this.request.setWhitelist( airgap.whitelist );
		else this.request.setWhitelist( false );
		
		if (airgap.blacklist && airgap.blacklist.length) this.request.setBlacklist( airgap.blacklist );
		else this.request.setBlacklist( false );
	}
	
	getExtForPlugin(plugin) {
		// get suitable temp file extension for plugin
		if (!this.platform.windows) return '';
		if (plugin.command.match(/\b(powershell|pwsh)\b/i)) return '.ps1';
		if (plugin.command.match(/\b(cmd)\b/i)) return '.bat';
		return '';
	}
	
	prepPlugins() {
		// create temp script files for all event and monitor plugins
		// this is only called on startup and when plugins are updated, so it's okay to use "sync" I/O
		var self = this;
		var plugin_dir = Path.join( this.config.get('temp_dir'), 'plugins' );
		var filenames = {};
		
		// pre-scan dir, so we can compare (if any plugins were deleted)
		Tools.glob.sync( Path.join( plugin_dir, '*' ) ).forEach( function(file) {
			filenames[ Path.basename(file) ] = true;
		} );
		
		this.plugins.forEach( function(plugin) {
			if (plugin.script) {
				var script_file = Path.join( plugin_dir, plugin.id + self.getExtForPlugin(plugin) );
				fs.writeFileSync( script_file, plugin.script + "\n" );
				delete filenames[ Path.basename(script_file) ];
			}
		} );
		
		this.commands.forEach( function(command) {
			if (command.script) {
				var script_file = Path.join( plugin_dir, command.id + self.getExtForPlugin(command) );
				fs.writeFileSync( script_file, command.script + "\n" );
				delete filenames[ Path.basename(script_file) ];
			}
		} );
		
		// delete any leftover files (deleted plugins)
		for (var filename in filenames) {
			var file = Path.join( plugin_dir, filename );
			try { fs.unlinkSync(file); } catch (e) {;}
		}
	}
	
	checkStartupLogFiles() {
		// check special log files, and notify master if found
		var bkgnd_log_file = Path.join( this.config.get('log_dir'), 'background.log' );
		if (fs.existsSync(bkgnd_log_file)) {
			var contents = fs.readFileSync(bkgnd_log_file, 'utf8').trim();
			var details = "**Log Contents:**\n\n```\n" + contents + "\n```\n";
			this.socket.send('notice', { description: `Upgrade completed on worker server: ` + this.server.hostname, details });
			fs.unlinkSync(bkgnd_log_file);
		}
		
		var crash_log_file = Path.join( this.config.get('log_dir'), 'crash.log' );
		if (fs.existsSync(crash_log_file)) {
			var contents = fs.readFileSync(crash_log_file, 'utf8').trim();
			var details = "**Log Contents:**\n\n```\n" + contents + "\n```\n";
			this.socket.send('critical', { description: `Crash log was found on worker server: ` + this.server.hostname, details });
			fs.unlinkSync(crash_log_file);
		}
	}
	
	updateConfig(updates) {
		// update config and save file
		
		// user may only want certain keys to be updated by the conductor
		var managed_keys = this.config.get('managed_keys');
		if (managed_keys && Array.isArray(managed_keys)) {
			for (var key in updates) {
				if (!managed_keys.includes(key)) delete updates[key];
			}
		}
		
		for (var key in updates) {
			this.config.set(key, updates[key]);
		}
		
		// save config safely
		this.logDebug(3, "Saving configuration file: " + this.config.configFile);
		try {
			var temp_config = JSON.parse( fs.readFileSync( this.config.configFile, 'utf8' ) );
			for (var key in updates) {
				temp_config[key] = updates[key];
			}
			
			// special case: remove initial prop (one-time use)
			if (temp_config.initial) delete temp_config.initial;
			
			fs.writeFileSync( this.config.configFile, JSON.stringify(temp_config, null, "\t") + "\n", { mode: 0o600 } );
		}
		catch (err) {
			this.logError('comm', "Failed to save configuration file: " + err);
		}
		
		// prevent auto file reload (pixl-server / pixl-config)
		this.config.mod = fs.statSync(this.config.configFile).mtime.getTime();
	}
	
	socketTick() {
		// called once per second from app.tick()
		// see if we're receiving frequent status updates from server (might be dead socket)
		if (this.socket && this.socket.connected) {
			if (Tools.timeNow() - this.socket.lastPing >= this.pingTimeoutSec) {
				// 5 seconds and no ping = likely dead
				this.logComm(2, "No ping in last " + this.pingTimeoutSec + " seconds, assuming socket is dead");
				this.socket.close(); // should auto-reconnect
				
				// make sure socket is really closed (yanking a cord can cause it to hang open)
				try { this.socket.ws.terminate(); } catch (e) {;}
			}
		}
	}
	
});
```

## File: `lib/engine.js`
```javascript
// xySat - xyOps Satellite - Engine
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

const fs = require('fs');
const os = require('os');
const Path = require('path');
const cp = require('child_process');
const Class = require("class-plus");
const Component = require("pixl-server/component");
const Tools = require("pixl-tools");
const Request = require("pixl-request");

module.exports = Class({
	__mixins: [
		require('./comm.js'),
		require('./monitor.js'),
		require('./job.js'),
		require('./utils.js')
	],
	__events: true,
	__hooks: false,
	__asyncify: false,
		
	defaultConfig: {
		
	},
	
	features: {
		testMonitorPlugin: true
	}
},
class Satellite extends Component {
	
	earlyStart() {
		// early startup to hook logger, to scan for errors
		var self = this;
		
		// basic config validation
		['pid_file', 'log_dir', 'log_filename', 'temp_dir', 'debug_level'].forEach( function(path) {
			if (!self.server.config.getPath(path)) {
				console.error("\nFATAL: Missing required configuration property: " + path + "\n");
				process.exit(1);
			}
		} );
		
		var log_file = Path.join( this.server.config.get('log_dir'), 'Error.log' );
		
		this.server.logger.on('row', function(line, cols, args) {
			if (args.category !== 'error') return; // early exit for non-errors
			
			// dedicated error log
			if (args.sync) fs.appendFileSync(log_file, line);
			else fs.appendFile(log_file, line, function() {});
		}); // row
		
		return true; // continue startup
	}
	
	startup(callback) {
		// start service
		var self = this;
		this.logDebug(2, "xyOps Satellite v" + this.server.__version + " starting up" );
		
		// use global config
		this.config = this.server.config;
		this.debug = this.server.debug;
		this.foreground = this.server.foreground;
		
		// job log dir and temp dir
		Tools.mkdirp.sync( Path.join( this.config.get('log_dir'), 'jobs' ) );
		Tools.mkdirp.sync( Path.join( this.config.get('temp_dir'), 'plugins' ) );
		Tools.mkdirp.sync( Path.join( this.config.get('temp_dir'), 'jobs' ) );
		
		try {
			fs.chmodSync( this.config.get('temp_dir'), 0o777 );
			fs.chmodSync( Path.join( this.config.get('temp_dir'), 'plugins' ), 0o777 );
			fs.chmodSync( Path.join( this.config.get('temp_dir'), 'jobs' ), 0o777 );
		}
		catch (e) {;}
		
		// allow `masters` to override hosts, and split string if needed
		// (i.e. support common environment variable format)
		if (this.config.get('masters')) {
			var masters = this.config.get('masters');
			if (typeof(masters) == 'string') masters = masters.split(/\,\s*/);
			this.config.set('hosts', masters);
			this.config.delete('masters');
		}
		
		// socket connect
		this.socketInit();
		this.socketConnect();
		
		// hook into tick timer
		this.server.on('tick', this.tick.bind(this));
		this.server.on('minute', this.minute.bind(this));
		this.server.on('day', this.day.bind(this));
		
		// reconnect on config reload
		this.config.on('reload', function() {
			self.socketInit();
			if (!self.socket) self.socketConnect();
		});
		
		// create a http request instance for various tasks
		this.request = new Request( "xyOps Satellite v" + this.server.__version );
		this.request.setFollow( 5 );
		this.request.setAutoError( true );
		this.request.setKeepAlive( true );
		
		// compute unique host id, for monitoring time offsets
		this.hostHash = Tools.digestHex( os.hostname(), 'md5' );
		this.hostID = parseInt( this.hostHash.substring(0, 8), 16 ); // 32-bit numerical hash
		this.numServers = 0;
		
		// commands should come over from 'joined'
		this.commands = [];
		
		// prime this for repeated calls (delta)
		this.lastCPU = process.cpuUsage();
		
		// and these
		this.cpuState = {};
		this.numCPUs = os.cpus().length;
		this.procCache = {};
		
		// pre-grab net ifaces
		this.interfaces = os.networkInterfaces();
		this.defaultInterfaceName = Tools.firstKey( this.interfaces );
		
		// sniff platform
		this.platform = {};
		switch (process.platform) {
			case 'linux': this.platform.linux = true; break;
			case 'darwin': this.platform.darwin = true; break;
			case 'freebsd': case 'openbsd': case 'netbsd': this.platform.bsd = true; break;
			case 'win32': this.platform.windows = true; break;
		}
		
		if (this.platform.linux) {
			// pre-calc location of some binaries
			this.psBin = Tools.findBinSync('ps');
			this.ssBin = Tools.findBinSync('ss');
			this.curlBin = Tools.findBinSync('curl');
			this.wgetBin = Tools.findBinSync('wget');
		} // linux
		
		if (this.platform.darwin) {
			// pre-calc location of some binaries
			this.psBin = Tools.findBinSync('ps');
			this.curlBin = Tools.findBinSync('curl');
			
			// determine the default network interface (for fast network speed measurements)
			var route = Tools.findBinSync('route');
			if (route) try {
				var result = cp.execFileSync( route, ['-n', 'get', 'default'] ).toString();
				//   interface: en0
				if (result.match(/\binterface\:\s*(\w+)/)) this.defaultInterfaceName = RegExp.$1;
			}
			catch (e) {;}
			
			// determine the default mem page size
			var sysctl = Tools.findBinSync('sysctl');
			if (sysctl) try {
				var result = cp.execFileSync( sysctl, ['-n', 'vm.pagesize'] ).toString();
				if (result && result.match(/(\d+)/)) this.memPageSize = parseInt( RegExp.$1, 10 );
			}
			catch (e) {
				this.memPageSize = 4096;
			}
		} // darwin
		
		callback();
	}
	
	tick() {
		// called every second from pixl-server
		this.socketTick();
		this.jobTick();
		this.runQuickMonitors();
	}
	
	minute() {
		// called every minute
		this.checkJobLogSizes();
		this.runMonitors();
	}
	
	day() {
		// called every day at midnight
		this.archiveLogs();
	}
	
	shutdown(callback) {
		// stop service
		var self = this;
		
		this.logDebug(1, "Shutting down xyOps Satellite");
		this.abortAllJobs();
		
		this.waitForAllJobs( function() {
			if (self.socket) self.socketDisconnect();
			if (self.reconnectTimer) clearTimeout( self.reconnectTimer );
			callback();
		});
	}
	
});
```

## File: `lib/job.js`
```javascript
// xySat - xyOps Satellite - Job Layer
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

const fs = require('fs');
const cp = require('child_process');
const WebSocket = require('ws');
const Class = require("class-plus");
const Tools = require("pixl-tools");
const os = require('os');
const Path = require('path');
const zlib = require('zlib');
const sqparse = require('shell-quote').parse;
const JSONStream = require('pixl-json-stream');
const async = require('async');
const si = require('systeminformation');

module.exports = Class({
	
	activeJobs: {},
	kids: {},
	connCache: {},
	
},
class Jobs {
	
	logJob(level, msg, data) {
		// log debug msg with pseudo-component
		if (this.debugLevel(level)) {
			this.logger.set( 'component', 'Job' );
			this.logger.print({ category: 'debug', code: level, msg: msg, data: data });
		}
	}
	
	getFileOpts() {
		// get file upload/download specific set of opts for pixl-request, configured separately
		return this.config.get('http_file_opts') || {
			timeout: 300 * 1000,
			idleTimeout: 30 * 1000,
			connectTimeout: 10 * 1000,
			
			retries: 8,
			retryDelay: 50,
			retryDelayMax: 8 * 1000
		};
	}
	
	prepLaunchJob(job, details, sec) {
		// setup temp dir for job, and download any files passed to us
		var self = this;
		
		// make sure we aren't trying to shut down
		if (this.server.shut) {
			job.pid = 0;
			job.code = 1;
			job.description = "Setup Error: Server is shutting down. Job cannot launch.";
			self.logError("job", job.description);
			self.activeJobs[ job.id ] = job;
			self.finishJob( job );
			return;
		}
		
		// each job gets its own unique temp dir
		job.cwd = Path.resolve( Path.join( this.config.get('temp_dir'), 'jobs', job.id ) );
		
		async.series([
			function(callback) {
				// create temp dir for job, full access
				Tools.mkdirp( job.cwd, { mode: 0o777 }, callback );
			},
			function(callback) {
				// download input files to job temp dir if we were given any
				if (!details.input || !details.input.files || !details.input.files.length || job.runner) return callback();
				
				async.eachSeries( details.input.files,
					function(file, callback) {
						var dest_file = Path.join( job.cwd, file.filename );
						var url = (self.socket.secure ? 'https:' : 'http:') + '//' + self.socket.host + ':' + self.socket.port + '/' + file.path;
						var opts = Object.assign( {}, self.config.get('socket_opts') || {}, self.getFileOpts(), {
							download: dest_file
						});
						
						self.logJob(6, "Downloading job file: " + url, { dest_file });
						self.appendMetaLog(job, `Downloading file: ${file.filename} (${Tools.getTextFromBytes(file.size)})`);
						
						self.request.get( url, opts, function(err, resp, data, perf) {
							if (err) {
								return callback( new Error("Failed to download job file: " + file.filename + ": " + (err.message || err)) );
							}
							delete file.path; // no longer needed, only adds user confusion
							callback();
						} ); // request.get
					},
					callback
				); // eachSeries
			}
		],
		function(err) {
			if (err) {
				// something went wrong
				job.pid = 0;
				job.code = 1;
				job.description = "Setup Error: " + err;
				self.logError("job", job.description);
				self.activeJobs[ job.id ] = job;
				self.finishJob( job );
				return;
			}
			
			// launch job for real
			self.launchJob(job, details, sec);
		});
	}
	
	launchJob(job, details, sec) {
		// launch job on this server!
		var self = this;
		var child = null;
		var worker = null;
		var base_url = (this.socket.secure ? 'https:' : 'http:') + '//' + this.socket.host + ':' + this.socket.port;
		
		// remove activity (meta) from this copy of the job, 
		// so our updates don't clobber the meta log which is maintained in master
		delete job.activity;
		
		this.logJob(6, "Launching job: " + job.id, this.debugLevel(9) ? job : null);
		
		// setup optional legacy log that user code can write to
		job.log_file = Path.resolve( Path.join(this.config.get('log_dir'), 'jobs', 'job-' + job.id + '.log') );
		
		// setup environment for child
		var child_opts = {
			cwd: job.cwd,
			env: Object.assign( {},
				this.cleanEnv(),
				this.config.get('job_env') || {},
				job.env || {},
				sec || {}
			)
		};
		
		child_opts.env['XYOPS'] = this.server.__version;
		child_opts.env['JOB_ID'] = job.id;
		child_opts.env['JOB_LOG'] = job.log_file; // legacy
		child_opts.env['JOB_NOW'] = job.now;
		child_opts.env['JOB_BASE_URL'] = base_url;
		child_opts.env['PWD'] = job.cwd;
		
		if (this.config.get('cronicle')) {
			child_opts.env['CRONICLE'] = this.server.__version; // for legacy purposes
			
			// copy all top-level job keys into child env, if number/string/boolean
			for (var key in job) {
				switch (typeof(job[key])) {
					case 'string': 
					case 'number':
						child_opts.env['JOB_' + key.toUpperCase()] = '' + job[key]; 
					break;
					
					case 'boolean':
						child_opts.env['JOB_' + key.toUpperCase()] = job[key] ? 1 : 0;
					break;
				}
			}
		} // cronicle
		
		// get uid / gid info for child env vars
		if (!this.platform.windows) {
			child_opts.uid = job.uid || process.getuid();
			child_opts.gid = process.getgid();
			
			var user_info = Tools.getpwnam( child_opts.uid, true );
			if (user_info) {
				child_opts.uid = user_info.uid;
				child_opts.gid = user_info.gid;
				child_opts.env.USER = child_opts.env.USERNAME = user_info.username;
				child_opts.env.HOME = user_info.dir;
				child_opts.env.SHELL = user_info.shell;
			}
			else if (child_opts.uid != process.getuid()) {
				// user not found
				job.pid = 0;
				job.code = 1;
				job.description = "Plugin Error: User does not exist: " + child_opts.uid;
				this.logError("job", job.description);
				this.activeJobs[ job.id ] = job;
				this.finishJob( job );
				return;
			}
			
			if (job.gid) {
				var grp_info = Tools.getgrnam( job.gid, true );
				if (grp_info) {
					child_opts.gid = grp_info.gid;
				}
				else {
					// gid not found
					job.pid = 0;
					job.code = 1;
					job.description = "Plugin Error: Group does not exist: " + job.gid;
					this.logError("job", job.description);
					this.activeJobs[ job.id ] = job;
					this.finishJob( job );
					return;
				}
			}
			
			child_opts.uid = parseInt( child_opts.uid );
			child_opts.gid = parseInt( child_opts.gid );
		}
		
		// add simple non-object plugin params as env vars, expand $INLINE vars
		if (job.params) {
			for (var key in job.params) {
				if (typeof(job.params[key]) != 'object') {
					child_opts.env[ key.replace(/\W+/g, '_') ] = 
						(''+job.params[key]).replace(/\$(\w+)/g, function(m_all, m_g1) {
						return (m_g1 in child_opts.env) ? child_opts.env[m_g1] : '';
					});
				}
			}
		}
		
		// add workflow params if applicable, and with special workflow_ key prefix
		if (job.workflow && job.workflow.params) {
			for (var key in job.workflow.params) {
				if (typeof(job.workflow.params[key]) != 'object') {
					child_opts.env[ 'workflow_' + key.replace(/\W+/g, '_') ] = 
						(''+job.workflow.params[key]).replace(/\$(\w+)/g, function(m_all, m_g1) {
						return (m_g1 in child_opts.env) ? child_opts.env[m_g1] : '';
					});
				}
			}
		}
		
		// spawn child
		var child_cmd = job.command;
		var child_args = [];
		
		if (child_cmd.match(/^\[([\w\-]+)\]$/)) {
			// special syntax for built-in plugins
			var plugin_name = RegExp.$1;
			if (process.pkg) {
				child_cmd = process.execPath;
				child_args = [ '--plugin', plugin_name ];
			}
			else {
				child_cmd = process.execPath;
				child_args = [ require.main.filename, '--plugin', plugin_name ];
			}
		}
		else if (child_cmd.match(/\s+(.+)$/)) {
			// if command has cli args, parse using shell-quote
			var cargs_raw = RegExp.$1;
			child_cmd = child_cmd.replace(/\s+(.+)$/, '');
			child_args = sqparse( cargs_raw, child_opts.env );
		}
		
		// add plugin script if configured
		if (job.script) {
			var plugin = Tools.findObject( this.plugins, { id: job.plugin } );
			if (!plugin) {
				job.pid = 0;
				job.code = 1;
				job.description = "Plugin not found: " + job.plugin;
				this.logError("job", job.description);
				this.activeJobs[ job.id ] = job;
				this.finishJob( job );
				return;
			}
			child_args.push( Path.resolve( Path.join( this.config.get('temp_dir'), 'plugins', job.plugin + this.getExtForPlugin(plugin) ) ) );
		}
		
		// windows additions
		if (this.platform.windows) {
			child_opts.windowsHide = true;
		}
		
		worker = {};
		
		// attach streams
		child_opts.stdio = ['pipe', 'pipe', 'pipe'];
		
		this.logJob(9, "Spawning child: " + child_cmd, {
			args: child_args, 
			opts: Tools.copyHashRemoveKeys( child_opts, { env: 1 } ) 
		});
		
		// spawn child
		try {
			child = cp.spawn( child_cmd, child_args, child_opts );
			if (!child || !child.pid || !child.stdin || !child.stdout) {
				throw new Error("Child process failed to spawn (Check executable location and permissions?)");
			}
		}
		catch (err) {
			if (child) child.on('error', function() {}); // prevent crash
			job.pid = 0;
			job.code = 1;
			job.description = "Child spawn error: " + child_cmd + ": " + Tools.getErrorDescription(err);
			this.logError("child", job.description);
			this.activeJobs[ job.id ] = job;
			this.finishJob( job );
			return;
		}
		job.pid = child.pid || 0;
		
		this.logJob(3, "Spawned child process: " + job.pid + " for job: " + job.id, child_cmd);
		this.appendMetaLog(job, "Spawned child process: PID " + job.pid);
		
		// connect json stream to child's stdio
		// order reversed deliberately (out, in)
		var stream = new JSONStream( child.stdout, child.stdin );
		stream.recordRegExp = /^\s*\{.+\}\s*$/;
		stream.preserveWhitespace = true;
		stream.maxLineLength = 1024 * 1024 * 32;
		stream.EOL = "\n";
		
		worker.pid = job.pid;
		worker.child = child;
		worker.stream = stream;
		
		// line buffer for flood management
		var lb_lines = [];
		var lb_size = 0;
		var lb_timer = null;
		
		var flushLineBuffer = function() {
			// flush all lines
			if (lb_timer) { clearTimeout(lb_timer); lb_timer = null; }
			if (!lb_lines.length) return;
			self.appendJobLog(job, lb_lines.join(''));
			lb_lines = [];
			lb_size = 0;
		};
		var addToLineBuffer = function(line) {
			lb_lines.push(line);
			lb_size += line.length;
			if (lb_size >= stream.maxLineLength) flushLineBuffer();
			else if (!lb_timer) lb_timer = setTimeout( flushLineBuffer, 50 );
		};
		
		stream.on('json', function(data) {
			// received data from child
			if (!self.handleChildResponse(job, worker, data)) {
				// unrecognized json, emit as raw text
				stream.emit('text', JSON.stringify(data) + "\n");
			}
		} );
		
		stream.on('text', function(line) {
			// received non-json text from child, log it
			if (self.platform.windows) line = line.replace(/\r$/, '');
			addToLineBuffer(line);
		} );
		
		stream.on('error', function(err, text) {
			// Probably a JSON parse error (child emitting garbage)
			self.logError('job', "Child stream error: Job ID " + job.id + ": PID " + job.pid + ": " + err);
			if (text) self.appendJobLog(job, text);
		} );
		
		child.stderr.on('data', function(data) {
			// child printed something to STDERR, capture and pass along to log
			// self.appendJobLog(job, data);
			addToLineBuffer( ''+data );
		});
		
		child.on('error', function (err) {
			// child error
			flushLineBuffer();
			job.code = 1;
			job.description = "Child process error: " + Tools.getErrorDescription(err);
			worker.child_exited = true;
			self.logError("child", job.description);
			self.finishJob( job );
		} );
		
		child.on('close', function (code, signal) {
			// child exited
			flushLineBuffer();
			self.logJob(6, "Child " + job.pid + " exited with code: " + (code || signal || 0));
			self.appendMetaLog(job, "Child exited with code: " + (code || signal || 0));
			worker.child_exited = true;
			
			if (job.complete) {
				// child already reported completion, so finish job now
				self.finishJob( job );
			}
			else {
				// job is not complete but process exited (could be coming in next tick)
				// set timeout just in case something went wrong
				worker.complete_timer = setTimeout( function() {
					job.code = code || 'warning';
					job.description = code ? 
						("Child " + job.pid + " crashed with code: " + (code || signal)) : 
						("Process exited without reporting job completion.");
					if (!code) job.unknown = 1;
					self.finishJob( job );
				}, 1000 );
			}
		} ); // on exit
		
		// possibly include meta data for calling the xyOps API directly (i.e. remote jobs)
		var meta = {
			secrets: sec || {},
			base_url: base_url,
			socket_opts: this.config.get('socket_opts'),
			temp_dir: Path.resolve( this.config.get('temp_dir') ),
			airgap: this.config.get('airgap') || undefined,
			activity: null // overwrite this as it's too verbose and not needed by plugin
		};
		
		if (job.runner) {
			// generate special job-specific file upload auth token, which auto-expires when job completes
			// (low security risk: it can ONLY be used to upload files, and only for this specific active job)
			var job_token = '';
			if (this.config.get('secret_key')) {
				var auth_token = Tools.digestHex( job.server + this.config.get('secret_key'), 'sha256' );
				job_token = Tools.digestHex( job.id + auth_token, 'sha256' );
			}
			else {
				job_token = Tools.digestHex( job.id + this.config.get('auth_token'), 'sha256' );
			}
			meta.auth_token = job_token;
		} // runner
		
		// send initial job + params + details + meta
		delete job.type; // don't clobber our "type":"job" thing
		stream.write({ xy: 1, type: 'event', ...job, ...details, ...meta });
		
		// we're done writing to the child -- don't hold its stdin open
		worker.child.stdin.end();
		
		// track job in our own hash
		this.activeJobs[ job.id ] = job;
		this.kids[ job.pid ] = worker;
	}
	
	appendJobLog(job, msg) {
		// append user-generated output to job log (via socket request)
		if (this.socket && this.socket.connected && this.socket.auth) {
			this.socket.send('job_log', { id: job.id, text: ''+msg } );
		}
		else if (!job.runner) {
			// no socket connection?  log it locally to the legacy job log file (will be uploaded as attachment).
			fs.appendFileSync( job.log_file, ''+msg );
		}
	}
	
	appendMetaLog(job, msg) {
		// append message to special "meta" log inside the job object (via socket request)
		if (this.socket && this.socket.connected && this.socket.auth) {
			this.socket.send('job_meta', { id: job.id, text: msg } );
		}
		this.logJob(6, "Job " + job.id + " Meta: " + msg);
	}
	
	handleChildResponse(job, worker, data) {
		// child sent us some datas (progress or completion)
		var found = false;
		this.logJob(10, "Got job update from child: " + job.pid, data);
		
		if (job.complete) {
			// prevent child from overwriting things when the job has been aborted remotely
			this.logJob(9, "Job is already complete, ignoring child update");
			return true;
		}
		if (job.code === 'abort') {
			this.logJob(9, "Job is being aborted, ignoring child update");
			return true;
		}
		
		// sanity check: if data has reserved property, assume user accidentally printed the entire job object
		if (data.type || data.state) {
			this.logJob(9, "Detected reserved property, ignoring child update");
			return true;
		}
		
		// merge in data
		if (data.xy) {
			// assume success if complete but no code specified
			if (data.complete && !data.code) data.code = 0;
			
			// likewise, if code is specified assume complete
			if (!data.complete && ('code' in data)) data.complete = true;
			
			// new api: provide `xy` key and everything else gets imported
			Tools.mergeHashInto( job, Tools.copyHashRemoveKeys(data, { xy:1 }) );
			found = true;
		}
		else if (this.config.get('cronicle')) {
			// old api: only look for specific keys, to avoid importing junk into RAM
			
			// legacy chain reaction API
			if (data.chain) {
				// legacy, convert to new action
				if (!job.push) job.push = {};
				if (!job.push.actions) job.push.actions = [];
				job.push.actions.push({ condition: 'success', type: 'run_event', event_id: data.chain, params: data.chain_params || {}, enabled: true });
				found = true;
			}
			if (data.chain_error) {
				// legacy, convert to new action
				if (!job.push) job.push = {};
				if (!job.push.actions) job.push.actions = [];
				job.push.actions.push({ condition: 'error', type: 'run_event', event_id: data.chain_error, enabled: true });
				found = true;
			}
			if (data.chain_data) {
				// legacy, convert to new data property
				data.data = data.chain_data;
				delete data.chain_data;
				found = true;
			}
			
			// legacy notification API
			if (data.notify_success) {
				if (!job.push) job.push = {};
				if (!job.push.actions) job.push.actions = [];
				job.push.actions.push({ condition: 'success', type: 'email', email: data.notify_success, enabled: true });
				found = true;
			}
			if (data.notify_fail) {
				if (!job.push) job.push = {};
				if (!job.push.actions) job.push.actions = [];
				job.push.actions.push({ condition: 'error', type: 'email', email: data.notify_fail, enabled: true });
				found = true;
			}
			
			// copy over known keys
			['progress', 'complete', 'code', 'description', 'perf', 'update_event', 'table', 'html', 'files', 'data', 'tags', 'push'].forEach( function(key) {
				if (key in data) { job[key] = data[key]; found = true; }
			} );
		} // legacy
		
		if (found) {
			// if either table or html provided, update a draw checksum token as a hint to the UI
			if (data.table || data.html || data.markdown || data.text || data.perf || job.push || job.status) {
				job.redraw = Tools.generateShortID();
			}
			
			// handle file push in satellite, do not send over to master
			if (job.push && job.push.files) {
				if (!job.files) job.files = [];
				job.files = job.files.concat( job.push.files );
				delete job.push.files;
				if (!Tools.numKeys(job.push)) delete job.push;
			}
		}
		
		if (job.complete && worker.child_exited) {
			// in case this update came in after child exited
			this.finishJob( job );
			found = true;
		}
		
		return found;
	}
	
	waitForHealthCheck(callback) {
		// wait for healthy server, kick off health check if stale
		var self = this;
		
		// if no healthy socket, retry
		if (!this.socket || !this.socket.connected || !this.socket.auth) {
			setTimeout( function() { self.waitForHealthCheck(callback) }, 1000 );
			return;
		}
		
		// early exit if latest check is fresh
		if (this.lastHealthCheck && (Tools.timeNow() - this.lastHealthCheck <= 1.0)) {
			if (this.lastHealthCheckResult) {
				// cached and result was true, so assume healthy
				this.logJob(9, "Health check succeeded (cached).");
				return callback();
			}
			else {
				// cached, but result was false, so assume still unhealthy
				setTimeout( function() { self.waitForHealthCheck(callback) }, 1000 );
				return;
			}
		}
		
		// if health check is in progress, retry quickly
		if (this.healthCheckInProgress) {
			setTimeout( function() { self.waitForHealthCheck(callback) }, 250 );
			return;
		}
		
		this.healthCheckInProgress = true;
		
		var url = (this.socket.secure ? 'https:' : 'http:') + '//' + this.socket.host + ':' + this.socket.port + '/health';
		var opts = Object.assign( {}, this.config.get('socket_opts') || {} );
		this.logJob(9, "Running health check: " + url );
		
		this.request.json( url, false, opts, function(err, resp, data, perf) {
			self.healthCheckInProgress = false;
			self.lastHealthCheck = Tools.timeNow();
			self.lastHealthCheckResult = false;
			
			if (err) {
				self.logJob(5, "Health check failed: " + err + " (will retry)");
				setTimeout( function() { self.waitForHealthCheck(callback) }, 1000 );
				return;
			}
			if (!data || !data.master) {
				// redundant check (bc /health api will 503 if not master) but best to verify anyway
				self.logJob(5, "Health check failed: Not master (will retry)");
				setTimeout( function() { self.waitForHealthCheck(callback) }, 1000 );
				return;
			}
			
			// websocket may have died during healhcheck request, so we need to re-test it here
			if (!self.socket || !self.socket.connected || !self.socket.auth) {
				setTimeout( function() { self.waitForHealthCheck(callback) }, 1000 );
				return;
			}
			
			self.lastHealthCheckResult = true;
			self.logJob(9, "Health check succeeded.");
			callback();
		}); // request.get
	}
	
	finishJob(job) {
		// complete job
		var self = this;
		
		// job may already be removed (sanity check)
		if (!this.activeJobs[ job.id ]) return;
		if (job.state != 'active') return;
		
		// kill completion timer, if set
		var worker = this.kids[ job.pid ] || {};
		if (worker.complete_timer) {
			clearTimeout( worker.complete_timer );
			delete worker.complete_timer;
		}
		if (worker.kill_timer) {
			clearTimeout( worker.kill_timer );
			delete worker.kill_timer;
		}
		
		// only complete if we have a healthy socket connection to master
		if (!this.socket || !this.socket.connected || !this.socket.auth) {
			this.logJob(5, "No socket connection, job is waiting to finish: " + job.id);
			setTimeout( function() { self.finishJob(job); }, 1000 );
			return;
		}
		
		// mark as complete
		job.complete = true;
		job.progress = 1.0;
		
		if (job.code) this.logJob(5, "Job is finishing with code: " + job.code, { job_id: job.id });
		else this.logJob(5, "Job is finishing", { job_id: job.id });
		
		this.appendMetaLog(job, "Job is finishing");
		
		// if non-zero code, we expect a string description
		if (job.code != 0) {
			if (!job.description) job.description = "Unknown Error (no description provided)";
		}
		if (job.description) {
			job.description = '' + job.description;
		}
		
		// cleanup child worker
		if (job.pid) delete self.kids[ job.pid ];
		
		// change state so master knows we're finishing
		job.state = 'finishing';
		
		// send update to conductor right now, instead of waiting for next tick
		self.updateJob(job);
		
		// add legacy job log to files array (glob will remove it if non-existent)
		if (!job.runner) {
			if (!job.files) job.files = [];
			job.files.push({ path: job.log_file, delete: true });
		}
		
		this.waitForHealthCheck( function() {
			self.prepUploadJobFiles(job, function(err) {
				if (err) {
					job.code = err.code || 'upload';
					job.description = "" + (err.message || err);
					job.files = [];
				}
				
				// now we're done with job
				job.state = 'complete';
				self.updateJobFinal(job);
				
			}); // prepUploadJobFiles
		}); // waitForHealthCheck
	}
	
	prepUploadJobFiles(job, callback) {
		// glob all file requests to resolve them to individual files, then upload
		var self = this;
		var to_upload = [];
		if (!job.files || !job.files.length || !Tools.isaArray(job.files)) return callback();
		
		// if job is running remotely, skip file upload
		if (job.runner) return callback();
		
		async.eachSeries( job.files,
			function(file, callback) {
				if (typeof(file) == 'string') {
					file = { path: file };
				}
				else if (Array.isArray(file)) {
					if (file.length == 3) file = { path: file[0], filename: file[1], delete: file[2] };
					else if (file.length == 2) file = { path: file[0], filename: file[1] };
					else file = { path: file[0] };
				}
				
				if (!file.path) return; // sanity
				
				// prepend job cwd if path is not absolute
				if (!Path.isAbsolute(file.path)) file.path = Path.join(job.cwd, file.path);
				
				if (file.filename) {
					// if user specified a custom filename, then do not perform a glob
					to_upload.push(file);
					process.nextTick(callback);
				}
				else Tools.glob( file.path, function(err, files) {
					if (!files) files = [];
					files.forEach( function(path) {
						to_upload.push({ path: path, delete: !!file.delete });
					} );
					callback();
				} );
			},
			function() {
				job.files = to_upload;
				self.uploadJobFiles(job, callback);
			}
		); // eachSeries
	}
	
	uploadJobFiles(job, callback) {
		// upload all job files (from user) if applicable
		var self = this;
		var final_files = [];
		var server_id = this.config.get('server_id');
		if (!job.files || !job.files.length || !Tools.isaArray(job.files)) return callback();
		
		// we may have lost the websocket during prep
		if (!this.socket || !this.socket.connected || !this.socket.auth) {
			setTimeout( function() { self.uploadJobFiles(job, callback) }, 1000 );
			return;
		}
		
		var url = (this.socket.secure ? 'https:' : 'http:') + '//' + this.socket.host + ':' + this.socket.port + '/api/app/upload_job_file';
		
		async.eachSeries( job.files,
			function(file, callback) {
				var filename = Path.basename(file.filename || file.path).replace(/[^\w\-\+\.\,\s\(\)\[\]\{\}\'\"\!\&\^\%\$\#\@\*\?\~]+/g, '_');
				self.logJob(6, "Uploading file for job", { job_id: job.id, file });
				self.appendMetaLog(job, "Uploading file: " + filename);
				
				var opts = Object.assign( {}, self.config.get('socket_opts') || {}, self.getFileOpts(), {
					"files": {
						file1: [file.path, filename]
					},
					"data": {
						id: job.id
					}
				});
				
				if (self.config.get('secret_key')) {
					opts.data.auth = Tools.digestHex( job.id + self.config.get('secret_key'), 'sha256' );
				}
				else {
					opts.data.server = self.config.get('server_id');
					opts.data.auth = self.config.get('auth_token');
				}
				
				self.logJob(6, "Uploading job file", { job_id: job.id, file, url });
				
				self.request.post( url, opts, function(err, resp, data, perf) {
					if (err) {
						if (perf && perf.metrics) self.logJob(9, "Upload perf metrics", perf.metrics());
						return callback( new Error("Failed to upload job file: " + filename + ": " + (err.message || err)) );
					}
					
					var json = null;
					try { json = JSON.parse( data.toString() ); }
					catch (err) { return callback(err); }
					
					if (json.code && json.description) {
						return callback( new Error("Failed to upload job file: " + filename + ": " + json.description) );
					}
					
					self.logJob(8, "File upload complete", { job_id: job.id, key: json.key, size: json.size, perf: perf.metrics() });
					
					// save file metadata
					final_files.push({ 
						id: file.id || Tools.generateShortID('f'),
						date: Tools.timeNow(true),
						filename: filename, 
						path: json.key, 
						size: json.size, 
						server: server_id, 
						job: job.id 
					});
					
					if (file.delete) fs.unlink(file.path, callback);
					else return callback();
				}); // request.post
			},
			function(err) {
				// replace job.files with storage keys
				if (err) {
					self.logError('upload', "" + err);
				}
				else {
					job.files = final_files;
					self.logJob(8, "All files uploaded", job.files);
				}
				callback(err);
			}
		);
	}
	
	updateJob(job) {
		// send separate, single update to master for specific job
		// (do not send procs or conns, as those need to be sent on a tick schedule)
		var self = this;
		if (!this.socket || !this.socket.connected || !this.socket.auth) return;
		
		var jobs = {};
		jobs[ job.id ] = Tools.copyHashRemoveKeys(job, { procs:1, conns:1 });
		
		this.socket.send('jobs', jobs);
		
		// clean up push system
		delete job.push;
	}
	
	updateJobFinal(job) {
		// send final job update, after health check
		var self = this;
		
		var cleanup = function() {
			// perform final cleanup tasks
			delete self.activeJobs[ job.id ];
			
			self.logJob(5, "Job is complete", { job_id: job.id });
			
			// delete temp dir, only log on error
			Tools.rimraf( job.cwd, function(err) {
				if (err) self.logError('fs', `Failed to delete job temp dir: ${job.cwd}: ${err}`);
			} );
			
			// re-check upgrade request if pending
			if (self.upgradeRequest) self.upgradeSatellite();
		}; // cleanup
		
		this.waitForHealthCheck( function() {
			// send via finish_job API if server supports it (xyops v1.0.15+), fallback to legacy websocket API
			if (!self.conductorFeatures.api_finish_job) {
				// use legacy
				self.logJob(9, "Sending final job update via legacy websocket API: " + job.id);
				self.updateJob(job);
				cleanup();
				return;
			}
			
			// use modern finish_job api
			var url = (self.socket.secure ? 'https:' : 'http:') + '//' + self.socket.host + ':' + self.socket.port + '/api/app/finish_job';
			var opts = Object.assign( {}, self.config.get('socket_opts') || {} );
			var data = {
				id: job.id,
				job: Tools.copyHashRemoveKeys(job, { procs:1, conns:1 })
			};
			
			if (self.config.get('secret_key')) {
				data.auth = Tools.digestHex( job.id + self.config.get('secret_key'), 'sha256' );
			}
			else {
				data.server = self.config.get('server_id');
				data.auth = self.config.get('auth_token');
			}
			
			self.logJob(9, "Sending final job update via finish_job API: " + job.id + ": " + url);
			
			self.request.json( url, data, opts, function(err, resp, data, perf) {
				if (err) {
					self.logJob(5, "Job final update failed: " + job.id + ": " + err + " (will retry)");
					setTimeout( function() { self.updateJobFinal(job) }, 1000 );
					return;
				}
				
				self.logJob(9, "Job final update succeeded and verified: " + job.id);
				cleanup();
			}); // request.get
		}); // waitForHealthCheck
	}
	
	measureJobResources(job, pids) {
		// scan process list for all processes that are descendents of job pid
		
		// skip remote runner jobs
		if (job.runner) return;
		
		delete job.procs;
		
		if (pids[ job.pid ]) {
			// add all procs into job
			job.procs = {};
			job.procs[ job.pid ] = pids[ job.pid ];
			
			var info = pids[ job.pid ];
			var cpu = info.cpu;
			var mem = info.memRss;
			
			// also consider children of the child (up to 100 generations deep)
			var levels = 0;
			var family = {};
			family[ job.pid ] = 1;
			
			while (Tools.numKeys(family) && (++levels <= 100)) {
				for (var fpid in family) {
					for (var cpid in pids) {
						if (pids[ cpid ].parentPid == fpid) {
							family[ cpid ] = 1;
							cpu += pids[ cpid ].cpu;
							mem += pids[ cpid ].memRss;
							job.procs[ cpid ] = pids[ cpid ];
						} // matched
					} // cpid loop
					delete family[fpid];
				} // fpid loop
			} // while
			
			if (job.cpu) {
				if (cpu < job.cpu.min) job.cpu.min = cpu;
				if (cpu > job.cpu.max) job.cpu.max = cpu;
				job.cpu.total += cpu;
				job.cpu.count++;
				job.cpu.current = cpu;
			}
			else {
				job.cpu = { min: cpu, max: cpu, total: cpu, count: 1, current: cpu };
			}
			
			if (job.mem) {
				if (mem < job.mem.min) job.mem.min = mem;
				if (mem > job.mem.max) job.mem.max = mem;
				job.mem.total += mem;
				job.mem.count++;
				job.mem.current = mem;
			}
			else {
				job.mem = { min: mem, max: mem, total: mem, count: 1, current: mem };
			}
			
			if (this.debugLevel(10)) {
				this.logJob(10, "Active Job: " + job.pid + ": CPU: " + cpu + "%, Mem: " + Tools.getTextFromBytes(mem));
			}
		} // matched job with pid
	}
	
	measureJobDiskIO(callback) {
		// use linux /proc/PID/io to glean disk r/w per sec per job proc
		var self = this;
		var procs = [];
		
		// zero everything out for non-linux
		for (var job_id in this.activeJobs) {
			var job = this.activeJobs[job_id];
			if (job.procs && !job.runner) {
				for (var pid in job.procs) { job.procs[pid].disk = 0; }
			}
		}
		
		// this trick is linux only
		if (process.platform != 'linux') return process.nextTick( callback );
		
		// get array of all active job procs
		for (var job_id in this.activeJobs) {
			var job = this.activeJobs[job_id];
			if (job.procs && !job.runner) procs = procs.concat( Object.values(job.procs) );
		}
		
		// parallelize this just a smidge, as it can be a lot of reads
		async.eachLimit( procs, 4,
			function(proc, callback) {
				fs.readFile( '/proc/' + proc.pid + '/io', 'utf8', function(err, text) {
					// if (!text) text = "rchar: " + Math.floor( Tools.timeNow(true) * 1024 ); // sample data (for testing)
					if (!text) text = "";
					
					// parse into key/value pairs
					var params = {};
					text.replace( /(\w+)\:\s*(\d+)/g, function(m_all, key, value) {
						params[key] = parseInt(value);
						return m_all;
					} );
					
					// take disk w + r per proc
					proc.disk = (params.rchar || 0) + (params.wchar || 0);
					// proc.disk = (params.read_bytes || 0) + (params.write_bytes || 0);
					
					callback();
				} );
			},
			callback
		); // async.eachLimit
	}
	
	measureJobNetworkIO(callback) {
		// use linux `ss` utility to glean network r/w per sec per job proc
		var self = this;
		
		// zero everything out for non-linux
		for (var job_id in this.activeJobs) {
			var job = this.activeJobs[job_id];
			if (job.procs && !job.runner) {
				for (var pid in job.procs) { 
					job.procs[pid].conns = 0; 
					job.procs[pid].net = 0; 
				}
			}
		}
		
		// this trick is linux only
		if ((process.platform != 'linux') || !this.ssBin) return process.nextTick( callback );
		if (this.config.get('disable_job_network_io')) return process.nextTick( callback );
		
		cp.exec( this.ssBin + ' -nutipaO', { timeout: 1000, maxBuffer: 1024 * 1024 * 32 }, function(err, stdout, stderr) {
			if (err) {
				self.logError('cp', "Failed to launch ss: " + err);
				return callback();
			}
			
			var now = Tools.timeNow(true);
			var lines = stdout.split(/\n/);
			var ids = {};
			
			lines.forEach( function(line) {
				if (line.match(/^(tcp|tcp4|tcp6|udp|udp4|udp6)\s+(\w+)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+.+pid\=(\d+)/)) {
					var type = RegExp.$1, state = RegExp.$2, local_addr = RegExp.$5, remote_addr = RegExp.$6, pid = RegExp.$7;
					
					// clean up some stuff
					pid = parseInt(pid);
					if (state == "ESTAB") state = 'ESTABLISHED';
					if (state == "UNCONN") state = 'UNCONNECTED';
					
					// generate socket "id" key using combo of local + remote
					var id = local_addr + '|' + remote_addr;
					
					if (!self.connCache[id]) self.connCache[id] = { bytes: 0, delta: 0, started: now };
					var conn = self.connCache[id];
					
					conn.type = type;
					conn.state = state;
					conn.local_addr = local_addr;
					conn.remote_addr = remote_addr;
					conn.pid = pid;
					
					var bytes = 0;
					if (line.match(/\bbytes_acked\:(\d+)/)) bytes += parseInt( RegExp.$1 ); // tx
					if (line.match(/\bbytes_received\:(\d+)/)) bytes += parseInt( RegExp.$1 ); // rx
					
					conn.delta = bytes - conn.bytes;
					conn.bytes = bytes;
					
					ids[id] = 1;
				}
			} ); // foreach line
			
			// delete sweep for removed conns
			for (var id in self.connCache) {
				if (!(id in ids)) delete self.connCache[id];
			}
			
			// join up conns with jobs and job procs
			Object.values(self.activeJobs).forEach( function(job) {
				if (!job.procs) return;
				if (job.runner) return;
				
				job.conns = [];
				for (var id in self.connCache) {
					var conn = self.connCache[id];
					if (conn.pid in job.procs) {
						job.conns.push(conn);
						job.procs[conn.pid].conns++;
						job.procs[conn.pid].net += conn.delta;
					}
				}
				
			}); // foreach job
			
			callback();
		} ); // cp.exec
	}
	
	jobTick() {
		// send all active jobs to master
		// called every second
		var self = this;
		if (!this.socket || !this.socket.connected || !this.socket.auth) return;
		
		if (!Tools.numKeys(this.activeJobs)) {
			// no jobs, so clear proc cache if old, to free up memory when no jobs are running
			if (this.procCache.data && (Tools.timeNow() >= this.procCache.expires)) this.procCache = {};
			return;
		}
		
		if (this.jobTickInProgress) return; // no steppy on toesy
		this.jobTickInProgress = true;
		
		// scan all processes on machine
		// si.processes( function(data) {
		this.getProcsCached( function(data) {
			if (!self.socket || !self.socket.connected || !self.socket.auth) {
				self.jobTickInProgress = false;
				return;
			}
			
			// cleanup and convert to hash of pids
			var pids = {};
			data.list.forEach( function(proc) {
				// proc.started = (new Date( proc.started )).getTime() / 1000;
				// proc.memRss = proc.memRss * 1024;
				// proc.memVsz = proc.memVsz * 1024;
				pids[ proc.pid ] = proc;
			} );
			
			for (var job_id in self.activeJobs) {
				var job = self.activeJobs[job_id];
				self.measureJobResources(job, pids);
			}
			
			async.parallel(
				[
					self.measureJobDiskIO.bind(self),
					self.measureJobNetworkIO.bind(self)
				],
				function() {
					if (!self.socket || !self.socket.connected || !self.socket.auth) {
						self.jobTickInProgress = false;
						return;
					}
					
					self.socket.send('jobs', self.activeJobs);
					
					// cleanup push system
					for (var job_id in self.activeJobs) {
						var job = self.activeJobs[job_id];
						delete job.push;
						
						// also cleanup other "one-time" properties here: html, text, table, markdown, perf, etc.
						delete job.table;
						delete job.html;
						delete job.markdown;
						delete job.text;
					}
					
					self.jobTickInProgress = false;
				}
			); // async.parallel
		} ); // si.processes
	}
	
	checkJobLogSizes() {
		// make sure legacy job log sizes don't grow too large
		// called every minute
		var self = this;
		var limited = Object.values(this.activeJobs).filter( function(job) {
			return !job.complete && Tools.findObject( job.limits, { type: 'log', enabled: true } );
		} );
		
		async.eachSeries( limited, function(job, callback) {
			var log_limit = Tools.findObject( job.limits, { type: 'log', enabled: true } );
			
			fs.stat( job.log_file, function(err, stats) {
				if (stats && stats.size && log_limit.amount && (stats.size > log_limit.amount)) {
					// job log file has grown too large!
					job.retry_ok = true; // allow retry even though we're aborting
					self.abortJob({ id: job.id, reason: "Job log file size has exceeded maximum size limit of " + Tools.getTextFromBytes(log_limit.amount) + "." });
				}
				callback();
			} );
		} );
	}
	
	abortJob(stub) {
		// abort job in progress
		var self = this;
		var job = this.activeJobs[ stub.id ];
		
		if (!job) {
			this.logError('job', "Job not found for abort: " + stub.id);
			return;
		}
		if (job.complete) {
			this.logError('job', "Job is already complete, skipping abort request: " + stub.id);
			return;
		}
		
		var worker = this.kids[ job.pid ] || {};
		
		this.logJob(4, "Aborting local job: " + stub.id + ": " + stub.reason, job);
		this.appendMetaLog(job, "Aborting job on server");
		
		job.code = 'abort';
		job.description = stub.reason;
		job.complete = true;
		
		if (worker.child) {
			// kill process(es) or not, depending on abort policy
			if (job.kill === 'none') {
				// kill none, just unref and finish
				worker.child.unref();
				this.finishJob(job);
				return;
			}
			
			worker.kill_timer = setTimeout( function() {
				// child didn't die, kill with prejudice
				if ((job.kill === 'all') && job.procs && Tools.firstKey(job.procs)) {
					// sig-kill ALL job processes
					var pids = Object.keys(job.procs);
					self.appendMetaLog(job, "Children did not exit, killing harder: " + pids.join(', '));
					pids.forEach( function(pid) {
						try { process.kill(pid, 'SIGKILL'); }
						catch(e) {;}
					} );
				}
				else {
					// sig-kill parent only
					self.appendMetaLog(job, "Child did not exit, killing harder: " + job.pid);
					worker.child.kill('SIGKILL');
				}
			}, this.config.get('child_kill_timeout') * 1000 );
			
			// try killing nicely first
			if ((job.kill === 'all') && job.procs && Tools.firstKey(job.procs)) {
				// sig-term ALL job processes
				var pids = Object.keys(job.procs);
				this.appendMetaLog(job, "Killing all job processes: " + pids.join(', '));
				pids.forEach( function(pid) {
					try { process.kill(pid, 'SIGTERM'); }
					catch(e) {;}
				} );
			}
			else {
				// sig-term parent only
				this.appendMetaLog(job, "Killing job process: " + job.pid);
				worker.child.kill('SIGTERM');
			}
		}
		else {
			// no child process, just finish job
			this.finishJob(job);
		}
	}
	
	updateAllJobs(updates) {
		// apply updates to all active jobs (shallow merge)
		for (var job_id in this.activeJobs) {
			Tools.mergeHashInto( this.activeJobs[job_id], updates );
		}
	}
	
	appendMetaLogAllJobs(msg) {
		// append meta message to all active jobs
		for (var job_id in this.activeJobs) {
			this.appendMetaLog( this.activeJobs[job_id], msg );
		}
	}
	
	abortAllJobs() {
		// abort all jobs (for shutdown)
		for (var job_id in this.activeJobs) {
			this.abortJob({ id: job_id, reason: "Server is shutting down." });
		}
	}
	
	waitForAllJobs(callback) {
		// wait for all jobs to finish before proceeding
		var self = this;
		var num_jobs = Tools.numKeys(this.activeJobs);
		
		if (num_jobs) {
			this.logJob(3, "Waiting for " + num_jobs + " jobs to complete", Object.keys(this.activeJobs));
			
			async.whilst(
				function () {
					return (Tools.numKeys(self.activeJobs) > 0);
				},
				function (callback) {
					setTimeout( function() { callback(); }, 250 );
				},
				function() {
					// all jobs gone
					self.logJob(9, "All jobs completed.");
					callback();
				}
			); // whilst
		}
		else callback();
	}
	
});
```

## File: `lib/monitor.js`
```javascript
// xySat - xyOps Satellite - Monitor Layer
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

const fs = require('fs');
const cp = require('child_process');
const os = require('os');
const Class = require("class-plus");
const Tools = require("pixl-tools");
const Path = require('path');
const zlib = require('zlib');
const sqparse = require('shell-quote').parse;
const XML = require('pixl-xml');
const async = require('async');
const si = require('systeminformation');
const Perf = require('pixl-perf');

module.exports = Class({
	
},
class Monitor {
	
	logMonitor(level, msg, data) {
		// log debug msg with pseudo-component
		if (this.debugLevel(level)) {
			this.logger.set( 'component', 'Monitor' );
			this.logger.print({ category: 'debug', code: level, msg: msg, data: data });
		}
	}
	
	getBasicServerInfo(callback) {
		// get basic OS, CPU, Memory info, for hello auth challenge
		var self = this;
		var info = {
			satellite: this.server.__version,
			node: process.versions.node,
			booted: Tools.timeNow(true) - os.uptime(),
			arch: os.arch(),
			platform: os.platform(),
			release: os.release(),
			quickmon: this.config.get('quickmon_enabled') && !this.platform.windows,
			features: this.features
		};
		
		async.series([
			function(callback) {
				// operating system
				self.logMonitor(9, "Calling si.osInfo...");
				si.osInfo( function(data) {
					data.platform = Tools.ucfirst( data.platform );
					info.os = data;
					self.logMonitor(9, "si.osInfo response", data);
					callback();
				} );
			},
			function(callback) {
				// system memory
				self.logMonitor(9, "Calling si.mem...");
				si.mem( function(data) {
					info.memory = data;
					self.logMonitor(9, "si.mem response", data);
					callback();
				} );
			},
			function(callback) {
				// cpu info
				self.logMonitor(9, "Calling si.cpu...");
				si.cpu( function(data) {
					info.cpu = data;
					self.logMonitor(9, "si.cpu response", data);
					callback();
				} );
			},
			function(callback) {
				// detect virtualization
				self.logMonitor(9, "Calling detectVirtualization...");
				self.detectVirtualization( function(data) {
					info.virt = data;
					self.logMonitor(9, "detectVirtualization response", data);
					callback();
				} );
			}
		],
		function() {
			callback(info);
		});
	}
	
	runQuickMonitors(opts = {}, callback = null) {
		// run select monitors every second
		var self = this;
		var info = {};
		if (!callback) callback = function() {};
		if (!this.socket || !this.socket.connected || !this.socket.auth) return callback();
		if (!this.config.get('monitoring_enabled') || !this.config.get('quickmon_enabled')) return callback();
		if (this.platform.windows) return callback();
		
		var perf = new Perf();
		perf.begin();
		
		async.parallel([
			function(callback) {
				// system memory
				// si.mem( function(data) {
				self.logMonitor(10, "Calling getMemFast...");
				perf.begin('mem');
				self.getMemFast( function(data) {
					perf.end('mem');
					info.mem = data;
					self.logMonitor(10, "getMemFast response", data);
					callback();
				} );
			},
			function(callback) {
				// cpu load
				// si.currentLoad( function(data) {
				self.logMonitor(10, "Calling getCPUFast...");
				perf.begin('cpu');
				self.getCPUFast( 'second', function(data) {
					perf.end('cpu');
					info.cpu = data;
					self.logMonitor(10, "getCPUFast response", data);
					callback();
				} );
			},
			function(callback) {
				// filesystem stats
				// si.fsStats( function(data) {
				self.logMonitor(10, "Calling getDiskFast...");
				perf.begin('disk');
				self.getDiskFast( function(data) {
					perf.end('disk');
					info.fs = data;
					self.logMonitor(10, "getDiskFast response", data);
					callback();
				} );
			},
			function(callback) {
				// network stats (first external interface)
				// si.networkStats( function(data) {
				self.logMonitor(10, "Calling getNetFast...");
				perf.begin('net');
				self.getNetFast( function(data) {
					perf.end('net');
					info.net = data;
					self.logMonitor(10, "getNetFast response", data);
					callback();
				} );
			}
		],
		function() {
			// re-check this as the si commands are async
			perf.end();
			var metrics = perf.metrics();
			if (metrics.perf.total > 250) self.logMonitor(9, "QuickMon Perf Warning", metrics);
			
			if (!self.socket || !self.socket.connected || !self.socket.auth) return callback();
			
			// vary max sleep time based on server count (passed to us from conductor), scale up with numServers, max of 1s
			var max_sleep_ms = opts.max_sleep_ms || Tools.clamp(self.numServers, 1, 1000);
			var sleep_ms = 0 + (self.hostID % max_sleep_ms);
			setTimeout( function() { 
				if (!self.socket || !self.socket.connected || !self.socket.auth) return;
				self.socket.send('quickmon', info); 
				callback();
			}, sleep_ms );
		});
	}
	
	runMonitors(opts, callback) {
		// called every minute
		// run full check on all server systems, commands, monitors
		var self = this;
		if (!opts) opts = {};
		if (!callback) callback = function() {};
		if (!this.socket || !this.socket.connected || !this.socket.auth) return callback();
		this.logMonitor(9, "Running monitors...");
		
		var perf = new Perf();
		perf.begin();
		
		// add current server mem/cpu
		var cpu = process.cpuUsage( this.lastCPU );
		this.lastCPU = cpu;
		
		// start building info structure
		var info = {
			version: "1.0",
			date: (new Date()).getTime() / 1000,
			server: this.config.get('server_id'),
			hostname: os.hostname(),
			data: {
				uptime_sec: os.uptime(),
				arch: os.arch(),
				platform: os.platform(),
				release: os.release(),
				load: os.loadavg(),
				// cpus: os.cpus(),
				stats: { io: {}, fs: {} },
				
				jobs: Tools.numKeys(this.activeJobs),
				
				process: {
					pid: process.pid,
					started: this.server.started,
					mem: process.memoryUsage.rss(),
					cpu: ((cpu.user + cpu.system) / 600000000) * 100 // percent of one core
				}
			}
		};
		
		async.series([
			function(callback) {
				// sleep for N seconds based on hash of hostname, scale up with numServers, max of 30s (min of 1s)
				// this is to avoid multiple servers from submitting metrics at the same instant
				var max_sleep_ms = opts.max_sleep_ms || (Tools.clamp(self.numServers, 1, 1000) * 29);
				var sleep_ms = 1000 + (self.hostID % (max_sleep_ms || 1));
				self.logMonitor(9, "Sleeping for " + sleep_ms + " ms");
				perf.begin('sleep');
				setTimeout( function() { perf.end('sleep'); callback(); }, sleep_ms );
			},
			function(callback) {
				// operating system
				self.logMonitor(9, "Calling si.osInfo...");
				perf.begin('si.osInfo');
				si.osInfo( function(data) {
					perf.end('si.osInfo');
					data.platform = Tools.ucfirst( data.platform );
					info.data.os = data;
					self.logMonitor(9, "si.osInfo response", data);
					callback();
				} );
			},
			function(callback) {
				// system memory
				// si.mem( function(data) {
				self.logMonitor(9, "Calling getMemFast...");
				perf.begin('getMemFast');
				self.getMemFast( function(data) {
					perf.end('getMemFast');
					info.data.memory = data;
					self.logMonitor(9, "getMemFast response", data);
					callback();
				} );
			},
			function(callback) {
				// cpu info
				self.logMonitor(9, "Calling si.cpu...");
				perf.begin('si.cpu');
				si.cpu( function(data) {
					perf.end('si.cpu');
					info.data.cpu = data;
					self.logMonitor(9, "si.cpu response", data);
					callback();
				} );
			},
			function(callback) {
				// cpu info
				// si.cpu( function(data) {
				self.logMonitor(9, "Calling getCPUFast...");
				perf.begin('getCPUFast');
				self.getCPUFast( 'minute', function(data) {
					perf.end('getCPUFast');
					Tools.mergeHashInto( info.data.cpu, data );
					self.logMonitor(9, "getCPUFast response", data);
					callback();
				} );
			},
			function(callback) {
				// file systems
				self.logMonitor(9, "Calling si.fsSize...");
				perf.begin('si.fsSize');
				si.fsSize( function(data) {
					perf.end('si.fsSize');
					info.data.mounts = {};
					data.forEach( function(item) {
						var key = item.mount.replace(/^\//, '').replace(/\W+/g, '_') || 'root';
						info.data.mounts[key] = item;
					});
					self.logMonitor(9, "si.fsSize response", data);
					callback();
				} );
			},
			function(callback) {
				// disk IO
				if (self.platform.windows) return callback(); // fails on win32
				self.logMonitor(9, "Calling si.disksIO...");
				perf.begin('si.disksIO');
				si.disksIO( function(data) {
					perf.end('si.disksIO');
					info.data.stats.io = data;
					self.logMonitor(9, "si.disksIO response", data);
					callback();
				} );
			},
			function(callback) {
				// filesystem stats
				if (self.platform.windows) return callback(); // fails on win32
				self.logMonitor(9, "Calling si.fsStats...");
				perf.begin('si.fsStats');
				si.fsStats( function(data) {
					perf.end('si.fsStats');
					info.data.stats.fs = data;
					self.logMonitor(9, "si.fsStats response", data);
					callback();
				} );
			},
			function(callback) {
				// network interfaces
				self.logMonitor(9, "Calling si.networkInterfaces...");
				perf.begin('si.networkInterfaces');
				si.networkInterfaces( function(data) {
					// convert array to hash, keyed by interface name (lo, eth0)
					perf.end('si.networkInterfaces');
					info.data.interfaces = {};
					data.forEach( function(item) {
						info.data.interfaces[ item.iface ] = item;
					} );
					self.logMonitor(9, "si.networkInterfaces response", data);
					callback();
				} );
			},
			function(callback) {
				// network stats
				self.logMonitor(9, "Calling si.networkStats...");
				perf.begin('si.networkStats');
				si.networkStats( '*', function(data) {
					perf.end('si.networkStats');
					self.logMonitor(9, "si.networkStats response", data);
					
					// add up stats from all external interfaces
					info.data.stats.network = {};
					
					// merge stats in with matching interface
					data.forEach( function(item) {
						var iface = info.data.interfaces[ item.iface ];
						if (!iface) return;
						
						if (!iface.internal) {
							// add up external stats
							if (!info.data.stats.network.ifaces) info.data.stats.network.ifaces = [];
							info.data.stats.network.ifaces.push( item.iface );
							
							for (var key in item) {
								if (key.match(/^(rx_|tx_)/)) info.data.stats.network[key] = (info.data.stats.network[key] || 0) + item[key];
							}
						} // is external
						
						// merge stats with matching interface
						Tools.mergeHashInto(iface, item);
					} );
					
					callback();
				} );
			},
			function(callback) {
				// network connections
				self.logMonitor(9, "Calling getNetworkConnections...");
				perf.begin('getNetworkConnections');
				self.getNetworkConnections(info, function(conns) {
					perf.end('getNetworkConnections');
					self.logMonitor(9, "getNetworkConnections response", { conns });
					callback();
				});
			},
			function(callback) {
				// all processes
				// si.processes( function(data) {
				self.logMonitor(9, "Calling getProcsFast...");
				perf.begin('getProcsFast');
				self.getProcsFast( function(data) {
					perf.end('getProcsFast');
					self.logMonitor(9, "getProcsFast response", data);
					// fix up procs a bit
					data.list.forEach( function(proc) {
						// augment job procs with job id, disk, net, conns
						for (var job_id in self.activeJobs) {
							var job = self.activeJobs[job_id];
							
							if (job.procs && !job.runner && job.procs[proc.pid]) {
								var job_proc = job.procs[proc.pid];
								proc.job = job_id;
								proc.disk = job_proc.disk || 0;
								proc.conns = job_proc.conns || 0;
								proc.net = job_proc.net || 0;
							}
						}
					} );
					
					info.data.processes = data;
					callback();
				} );
			},
			function(callback) {
				// custom commands
				if (!self.commands.length) return process.nextTick( callback );
				info.data.commands = {};
				self.logMonitor(9, "Calling custom commands...");
				perf.begin('commands');
				
				// filter commands by server groups
				var commands = self.commands.filter( function(command) {
					return !command.groups.length || Tools.includesAny(command.groups, self.groups);
				} );
				
				async.eachLimit( commands, self.config.get('monitor_plugin_concurrency') || 8,
					function(command, callback) {
						self.logMonitor(9, "Calling custom command: " + command.id, command);
						self.runMonitorCommand(command, function(result) {
							info.data.commands[ command.id ] = result;
							self.logMonitor(9, "Custom command response: " + command.id, { result });
							callback();
						} );
					},
					function() {
						perf.end('commands');
						self.logMonitor(9, "Done with custom commands");
						callback();
					}
				); // async.eachSeries
			},
			function(callback) {
				// all done
				perf.end();
				var metrics = perf.metrics();
				self.logMonitor(9, "Monitoring Perf Metrics", metrics);
				
				// send server metrics over to master
				if (self.config.get('monitoring_enabled') && self.socket && self.socket.connected && self.socket.auth) {
					self.socket.send('monitor', info);
				}
				
				callback(); // end async.series
			}
		],
		function() {
			callback(); // func callback
		}); // async.series
	}
	
	runMonitorCommand(command, callback) {
		// run single monitor, return result
		var self = this;
		if (typeof(command) == 'string') command = Tools.findObject( this.commands, { id: command } );
		if (!command) return callback("Error: Monitor Plugin not found on server");
		if (!command.timeout) command.timeout = 10; // default 10 sec
		
		var child_opts = { 
			// timeout: command.timeout * 1000,
			windowsHide: true,
			cwd: command.cwd || os.tmpdir(),
			env: Object.assign( {}, self.cleanEnv(), command.sec || {} ),
			stdio: ['pipe', 'pipe', 'pipe']
		};
		if (command.uid && (command.uid != 0)) {
			var user_info = Tools.getpwnam( command.uid, true );
			if (user_info) {
				child_opts.uid = parseInt( user_info.uid );
				child_opts.gid = parseInt( user_info.gid );
				child_opts.env.USER = child_opts.env.USERNAME = user_info.username;
				child_opts.env.HOME = user_info.dir;
				child_opts.env.SHELL = user_info.shell;
			}
			else {
				return process.nextTick( function() {
					callback( "Error: Could not determine user information for: " + command.uid );
				} );
			}
		}
		if (command.gid && (command.gid != 0)) {
			var grp_info = Tools.getgrnam( command.gid, true );
			if (grp_info) {
				child_opts.gid = grp_info.gid;
			}
			else {
				return process.nextTick( function() {
					callback( "Error: Could not determine group information for: " + command.gid );
				} );
			}
		}
		
		var child = null;
		var child_cmd = command.command;
		var child_args = [];
		var child_output = '';
		var child_stderr = '';
		var child_timeout_err_msg = '';
		var callback_fired = false;
		
		// if command has cli args, parse using shell-quote
		if (child_cmd.match(/\s+(.+)$/)) {
			var cargs_raw = RegExp.$1;
			child_cmd = child_cmd.replace(/\s+(.+)$/, '');
			child_args = sqparse( cargs_raw, child_opts.env );
		}
		
		// add plugin script if configured
		if (command.script) {
			child_args.push( Path.resolve( Path.join( self.config.get('temp_dir'), 'plugins', command.id + self.getExtForPlugin(command) ) ) );
		}
		
		var child_timer = setTimeout( function() {
			// timed out
			child_timeout_err_msg = "Error: Command timed out after " + command.timeout + " seconds";
			child.kill(); // should fire exit event
		}, command.timeout * 1000 );
		
		// spawn child
		try {
			child = cp.spawn( child_cmd, child_args, child_opts );
		}
		catch (err) {
			clearTimeout( child_timer );
			if (!callback_fired) { 
				callback_fired = true; 
				callback( "Error: Could not execute command: " + child_cmd + ": " + Tools.getErrorDescription(err) ); 
			}
			return;
		}
		
		child.on('error', function (err) {
			// child error
			clearTimeout( child_timer );
			if (!callback_fired) { 
				callback_fired = true; 
				callback( "Error: Could not execute command: " + child_cmd + ": " + Tools.getErrorDescription(err) ); 
			}
		} );
		
		child.on('exit', function (code, signal) {
			// child exited
			clearTimeout( child_timer );
			var result = child_timeout_err_msg || child_output;
			
			// automatically parse JSON or XML
			if ((command.format == 'json') && result.match(/(\{|\[)/)) {
				// attempt to parse JSON
				var json = null;
				try { json = JSON.parse(result); }
				catch (err) { result = 'JSON Parser Error: ' + err; }
				if (json) result = json;
			}
			else if ((command.format == 'xml') && result.match(/\</)) {
				// attempt to parse XML
				var xml = null;
				try { xml = XML.parse(result); }
				catch (err) { result = "XML Parser Error: " + err; }
				if (xml) result = xml;
			}
			else {
				// plain text, trim whitespace
				result = result.trim();
			}
			
			if (!callback_fired) { 
				callback_fired = true; 
				callback( result, child_stderr ); 
			}
		});
		
		if (child.stdout) {
			child.stdout.on('data', function(data) {
				child_output += data.toString();
				if (child_output.length > 1024 * 1024) child.kill(); // sanity e-brake
			});
		}
		if (child.stderr) {
			child.stderr.on('data', function(data) {
				if (child_stderr.length < 1024 * 1024) child_stderr += data.toString();
			});
		}
		
		child.stdin.end();
	}
	
	testMonitorPlugin(data) {
		// test monitor plugin on-demand (ws request from conductor)
		var self = this;
		this.logMonitor(5, "Testing monitor plugin by request", data);
		
		this.runMonitorCommand(data.plugin_id, function(result, stderr) {
			// send back result with request context
			data.result = result;
			data.stderr = stderr;
			if (!self.socket || !self.socket.connected || !self.socket.auth) return;
			self.logMonitor(5, "Sending monitor plugin test result", data);
			self.socket.send('monitorPluginTestResult', data);
		});
	}
	
	getNetworkConnections(info, callback) {
		// get all network connections either using `ss` on linux, or si
		var self = this;
		
		var finish = function(conns) {
			info.data.conns = conns;
				
			info.data.stats.network.conns = conns.length;
			info.data.stats.network.states = { established: 0 };
			
			conns.forEach( function(conn) {
				if (conn.state) {
					var key = conn.state.toString().toLowerCase();
					if (!info.data.stats.network.states[key]) info.data.stats.network.states[key] = 0;
					info.data.stats.network.states[key]++;
				}
			});
			
			callback(conns);
		}; // finish
		
		if (this.ssBin) {
			// linux
			cp.exec( this.ssBin + ' -nutipaO', { timeout: 10000, maxBuffer: 1024 * 1024 * 128 }, function(err, stdout, stderr) {
				var conns = [];
				if (err) {
					self.logError('cp', "Failed to launch ss: " + err);
					return finish(conns);
				}
				
				stdout.split(/\n/).forEach( function(line) {
					if (line.match(/^(tcp|tcp4|tcp6|udp|udp4|udp6)\s+(\w+)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+.+pid\=(\d+)/)) {
						var type = RegExp.$1, state = RegExp.$2, local_addr = RegExp.$5, remote_addr = RegExp.$6, pid = RegExp.$7;
						
						// clean up some stuff
						pid = parseInt(pid);
						if (state == "ESTAB") state = 'ESTABLISHED';
						if (state == "UNCONN") state = 'UNCONNECTED';
						
						var conn = { type, state, local_addr, remote_addr, pid };
						
						conn.bytes_out = line.match(/\bbytes_acked\:(\d+)/) ? parseInt( RegExp.$1 ) : 0;
						conn.bytes_in = line.match(/\bbytes_received\:(\d+)/) ? parseInt( RegExp.$1 ) : 0;
						
						conns.push(conn);
					}
				} ); // foreach line
				
				finish(conns);
			} ); // cp.exec
		} // ss
		else {
			// macos or other
			si.networkConnections( function(si_conns) {
				var conns = [];
				
				// cleanup windows garbage
				if (si_conns[0] && (si_conns[0].protocol == 'proto')) si_conns.shift();
				
				si_conns.forEach( function(conn) {
					conns.push({
						type: conn.protocol,
						state: conn.state || 'unknown',
						local_addr: conn.localAddress + ':' + conn.localPort,
						remote_addr: conn.peerAddress + ':' + conn.peerPort,
						pid: conn.pid || 0
					});
				}); // foreach conn
				
				finish(conns);
			} ); // si.networkConnections
		} // si
	}
	
	getOpenFiles(callback) {
		// use lsof to scan all open files
		var cmd = Tools.findBinSync('lsof');
		if (!cmd) return callback( new Error("Cannot locate lsof binary.") );
		
		// linux only: prevent duplicate files for threads
		if (process.platform == 'linux') cmd += ' -Ki';
		
		// rest of lsof CLI options are universal:
		// machine-readable output, skip blocking ops, formatting opts
		cmd += ' -RPn -F Ttpfn';
		
		cp.exec( cmd, { timeout: 10 * 1000 }, function(err, stdout, stderr) {
			if (err) return callback(err);
			
			// parse lsof output
			var files = [];
			var cur_proc = null;
			var cur_file = null;
			
			stdout.split(/\n/).forEach( function(line) {
				if (!line.match(/^(\w)(.+)$/)) return;
				var code = RegExp.$1;
				var value = RegExp.$2;
				
				switch (code) {
					case 'p':
						// new process
						if (cur_proc && cur_file) files.push( Tools.mergeHashes(cur_proc, cur_file) );
						cur_proc = { pid: parseInt(value) };
						cur_file = null;
					break;
					
					case 'f':
						// new file
						if (cur_proc && cur_file) files.push( Tools.mergeHashes(cur_proc, cur_file) );
						cur_file = { desc: value };
					break;
					
					case 't':
						// file type
						if (cur_file) cur_file.type = value;
					break;
					
					case 'n':
						// file path
						if (cur_file) cur_file.path = value;
					break;
					
					case 'T':
						// TCP socket info (append if applicable)
						if (cur_file && cur_file.path && value.match(/ST\=(.+)$/)) {
							cur_file.path += ' (' + RegExp.$1 + ')';
						}
					break;
				} // switch code
			} ); // foreach line
			
			if (cur_proc && cur_file) files.push( Tools.mergeHashes(cur_proc, cur_file) );
			
			callback(null, files);
		}); // cp.exec
	}
	
	detectVirtualization(callback) {
		// detect virtualization and get details if applicable
		// will produce: false, { vendor }, or { vendor, type, location }
		var self = this;
		var info = false;
		
		// all these checks are linux-only, so skip if we're on another OS
		if (process.platform != 'linux') return callback(info);
		
		if (fs.existsSync('/sys/class/dmi/id/board_vendor')) {
			// public cloud of some kind (AWS, Google, Azure, DigitalOcean)
			try {
				var vendor = fs.readFileSync('/sys/class/dmi/id/board_vendor', 'utf8').trim();
				if (vendor.match(/\S/)) info = { vendor, cloud: true };
			}
			catch (err) {;}
			
			if (info && info.vendor.match(/\b(Amazon|AWS|EC2)\b/)) {
				// amazon ec2
				async.series([
					function(callback) {
						var opts = { timeout: 1000, idleTimeout: 1000, connectTimeout: 1000 };
						self.request.get( 'http://169.254.169.254/latest/meta-data/instance-type', opts, function(err, resp, data, perf) {
							if (!err && data) info.type = data.toString().trim();
							callback();
						} );
					},
					function(callback) {
						var opts = { timeout: 1000, idleTimeout: 1000, connectTimeout: 1000 };
						self.request.get( 'http://169.254.169.254/latest/meta-data/placement/availability-zone', opts, function(err, resp, data, perf) {
							if (!err && data) info.location = data.toString().trim();
							callback();
						} );
					}
				], function() { callback(info); } );
				return;
			} // aws
			else if (info && info.vendor.match(/\b(Google)\b/)) {
				// google compute cloud
				async.series([
					function(callback) {
						var opts = { timeout: 1000, idleTimeout: 1000, connectTimeout: 1000 };
						self.request.get( 'http://metadata.google.internal/computeMetadata/v1/instance/machine-type', opts, function(err, resp, data, perf) {
							if (!err && data) info.type = data.toString().trim().split('/').pop();
							callback();
						} );
					},
					function(callback) {
						var opts = { timeout: 1000, idleTimeout: 1000, connectTimeout: 1000 };
						self.request.get( 'http://metadata.google.internal/computeMetadata/v1/instance/zone', opts, function(err, resp, data, perf) {
							if (!err && data) info.location = data.toString().trim().split('/').pop();
							callback();
						} );
					}
				], function() { callback(info); } );
				return;
			} // google cloud
			else if (info && info.vendor.match(/\b(Microsoft|Azure)\b/)) {
				// microsoft azure cloud
				var opts = { timeout: 1000, idleTimeout: 1000, connectTimeout: 1000, headers: { Metadata: 'true' } };
				self.request.json( 'http://169.254.169.254/metadata/instance?api-version=2020-06-01', false, opts, function(err, resp, data, perf) {
					if (!err && data && data.compute) {
						info.type = data.compute.vmSize;
						info.location = data.compute.location;
					}
					callback(info);
				} ); // request.json
				return;
			} // azure
			else if (info && info.vendor.match(/\b(DigitalOcean)\b/)) {
				// digital ocean droplet
				var opts = { timeout: 1000, idleTimeout: 1000, connectTimeout: 1000 };
				self.request.json( 'http://169.254.169.254/metadata/v1.json', false, opts, function(err, resp, data, perf) {
					if (!err && data && data.region) {
						info.location = data.region;
					}
					callback(info);
				} ); // request.json
				return;
			} // digitalocean
		} // board_vendor
		
		if (!info && fs.existsSync('/sys/class/dmi/id/sys_vendor')) {
			// other vm (Linode, KVM, etc.)
			try {
				var vendor = fs.readFileSync('/sys/class/dmi/id/sys_vendor', 'utf8').trim();
				if (vendor.match(/\S/)) info = { vendor };
			}
			catch (err) {;}
		}
		
		if (!info && fs.existsSync('/sys/class/dmi/id/product_name')) {
			// other vm (QEMU, etc.)
			try {
				var vendor = fs.readFileSync('/sys/class/dmi/id/product_name', 'utf8').trim();
				if (vendor.match(/\S/)) info = { vendor };
			}
			catch (err) {;}
		}
		
		if (!info && fs.existsSync('/.dockerenv')) {
			// docker
			info = { vendor: 'Docker' };
		}
		
		if (!info && fs.existsSync('/proc/self/cgroup')) {
			// another way to detect docker
			try {
				var cgroup = fs.readFileSync('/proc/self/cgroup', 'utf8').trim();
				if (cgroup.match(/\b(docker)\b/i)) info = { vendor: 'Docker' };
			}
			catch (err) {;}
		}
		
		if (!info) {
			// check df for known mounts that might hint the vendor
			var df_bin = Tools.findBinSync('df');
			var df = df_bin ? cp.execSync(df_bin, { timeout: 5000 }).toString() : '';
			if (df.match(/\b(orbstack)\b/)) info = { vendor: 'OrbStack' };
			else if (df.match(/\b(docker)\b/)) info = { vendor: 'Docker' };
			else if (df.match(/\b(kubelet)\b/)) info = { vendor: 'Kubernetes' };
			else if (df.match(/\b(qemu)\b/)) info = { vendor: 'QEMU' };
			else if (df.match(/\b(vboxsf)\b/)) info = { vendor: 'VirtualBox' };
			else if (df.match(/\b(vmhgfs)\b/)) info = { vendor: 'VMWare' };
			else if (df.match(/\b(hyperv)\b/)) info = { vendor: 'Hyper-V' };
		}
		
		if (!info && fs.existsSync('/proc/1/environ')) {
			// LXC
			try {
				var environ = fs.readFileSync('/proc/1/environ', 'utf8').toString().trim();
				if (environ.match(/\b(lxc)\b/i)) info = { vendor: 'LXC' };
			}
			catch (err) {;}
		}
		
		callback(info);
	}
	
});
```

## File: `lib/utils.js`
```javascript
// xySat - xyOps Satellite - Utils
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

const fs = require('fs');
const cp = require('child_process');
const os = require('os');
const Class = require("class-plus");
const Tools = require("pixl-tools");
const Path = require('path');
const zlib = require('zlib');
const sqparse = require('shell-quote').parse;
const async = require('async');
const si = require('systeminformation');

module.exports = Class({
	
},
class Utils {
	
	cleanEnv() {
		// make copy and strip sensitive keys from env, for passing to plugin processes
		var env = Tools.copyHash(process.env);
		
		for (var key in env) {
			if (key.match(/^(XYOPS_|XYSAT_|SATELLITE_)/)) delete env[key];
		}
		
		// add some custom PATHs and set sane defaults (on linux/macos)
		if (!Tools.isWindows) {
			var paths = (env.PATH ? env.PATH.split(/:/) : []).concat([ 
				'/bin', '/sbin', '/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin',
				Path.join( env.HOME || '/root', '.local', 'bin' ),
				Path.join( process.cwd(), 'bin' ),
				Path.join( process.cwd(), 'node_modules', '.bin' )
			]);
			env.PATH = [...new Set(paths)].join(':');
		}
		
		return env;
	}
	
	logMaint(level, msg, data) {
		// log debug msg with pseudo-component
		if (this.debugLevel(level)) {
			this.logger.set( 'component', 'Maint' );
			this.logger.print({ category: 'debug', code: level, msg: msg, data: data });
		}
	}
	
	getCPUFast(skey, callback) {
		// get CPU info fast
		var self = this;
		var info = {
			avgLoad: os.loadavg()[0],
			currentLoad: 0,
			cpus: [],
			totals: { user: 0, nice: 0, system: 0, irq: 0, idle: 100, active: 0, iowait: 0, softirq: 0 }
		};
		
		if (this.platform.linux) {
			// use /proc/stat on linux
			if (!this.cpuState[skey]) this.cpuState[skey] = {};
			var state = this.cpuState[skey];
			
			fs.readFile( '/proc/stat', 'utf8', function(err, data) {
				if (err) return callback(info);
				
				data.trim().split(/\n/).forEach( function(line) {
					if (line.match(/^\s*(cpu\d*)\s+(.+)$/)) {
						var cpu_key = RegExp.$1;
						var cpu_values = RegExp.$2.trim().split(/\s+/).map( function(value) { return parseInt(value); } );
						
						if (cpu_values.length && state.proc_stat && state.proc_stat[cpu_key]) {
							var cpu_deltas = cpu_values.map( function(value, idx) {
								return Math.max( 0, value - state.proc_stat[cpu_key][idx] );
							});
							
							var delta_total = 0;
							cpu_deltas.forEach( function(delta) { delta_total += delta; } );
							if (!delta_total) delta_total = 1; // prevent divide-by-zero
							
							// convert each to percentage of total
							var percents = cpu_deltas.map( function(delta) {
								return Tools.shortFloat( 100 - (100 * ((delta_total - delta) / delta_total)) );
							});
							
							// format for JSON
							var pct_fmt = {
								'user': Tools.clamp(percents[0], 0, 100),
								'nice': Tools.clamp(percents[1], 0, 100),
								'system': Tools.clamp(percents[2], 0, 100),
								'idle': Tools.clamp(percents[3], 0, 100),
								'iowait': Tools.clamp(percents[4], 0, 100),
								'irq': Tools.clamp(percents[5], 0, 100),
								'softirq': Tools.clamp(percents[6], 0, 100),
								'active': 100 - Tools.clamp(percents[3], 0, 100)
							};
							
							if (cpu_key == 'cpu') info.totals = pct_fmt;
							else info.cpus.push(pct_fmt);
						} // found state
						else {
							// fill with zeroes first time through
							var pct_fmt = { user:0, nice:0, system:0, idle:100, iowait:0, irq:0, softirq:0, active:0 };
							if (cpu_key == 'cpu') info.totals = pct_fmt;
							else info.cpus.push(pct_fmt);
						}
						
						if (!state.proc_stat) state.proc_stat = {};
						state.proc_stat[cpu_key] = cpu_values;
					}
				} ); // for each line
				
				info.currentLoad = info.totals.active;
				callback(info);
			} ); // fs.readFile
		}
		else {
			// non-linux, use os.cpus() API
			var cpus = os.cpus().map(cpu => cpu.times);
			var total_idle = 0;
			var total_active = 0;
			
			if (!this.cpuState[skey]) {
				// first call, initialize state, return all zeroes
				for (var idx = 0, len = cpus.length; idx < len; idx++) {
					info.cpus.push({ user: 0, nice: 0, system: 0, irq: 0, idle: 100, active: 0, iowait: 0, softirq: 0 });
				}
				this.cpuState[skey] = cpus;
				return callback(info);
			}
			
			var state = this.cpuState[skey];
			
			cpus.forEach( function(cpu, idx) {
				var prev = state[idx];
				var idle = cpu.idle - prev.idle;
				var active = (cpu.user - prev.user) + (cpu.nice - prev.nice) + (cpu.sys - prev.sys) + (cpu.irq - prev.irq);
				var delta = idle + active;
				
				total_idle += idle;
				total_active += active;
				
				info.cpus.push({
					user: ((cpu.user - prev.user) / delta) * 100,
					nice: ((cpu.nice - prev.nice) / delta) * 100,
					system: ((cpu.sys - prev.sys) / delta) * 100,
					irq: ((cpu.irq - prev.irq) / delta) * 100,
					idle: (idle / delta) * 100,
					active: (active / delta) * 100,
					iowait: 0, // n/a on darwin
					softirq: 0 // n/a on darwin
				});
			} );
			
			var total_time = total_idle + total_active;
			info.currentLoad = (total_active / total_time) * 100;
			
			// add up totals
			info.totals.idle = 0;
			info.cpus.forEach( function(cpu) {
				for (var key in cpu) {
					info.totals[key] += cpu[key];
				}
			} );
			
			// totals should be averages across all CPUs
			for (var key in info.totals) {
				info.totals[key] /= (info.cpus.length || 1);
			}
			
			this.cpuState[skey] = cpus;
			callback(info);
		}
	}
	
	getMemFast(callback) {
		// get memory information fast
		var self = this;
		var info = {
			total: os.totalmem(),
    		free: os.freemem()
		};
		info.used = info.total - info.free;
		info.available = info.free;
		
		if (this.platform.linux) {
			// use /proc/meminfo on linux
			fs.readFile('/proc/meminfo', 'utf8', function (err, data) {
				if (err) return callback(info);
				
				data.trim().split(/\n/).forEach( function(line) {
					// MemAvailable:   15873932 kB
					if (line.match(/^\s*(\w+)\:\s*(.+)$/)) {
						var key = RegExp.$1;
						var value = RegExp.$2;
						info[ key.replace(/^Mem/, '').toLowerCase() ] = Tools.getBytesFromText(value);
					}
				} );
				
				// compute estimate of available mem
				if (!info.available && info.free && info.buffers) info.available = info.free + info.buffers;
				callback(info);
			});
		}
		else if (this.platform.darwin) {
			// use vm_stat on macos
			cp.execFile( '/usr/bin/vm_stat', [], { timeout: 750 }, function(err, stdout, stderr) {
				if (err) return callback(info);
				
				stdout.trim().split(/\n/).forEach( function(line) {
					// Pages free: 2596.
					if (line.trim().match(/^Pages\s+(\w+)\:\s*(\d+)\./)) {
						var key = RegExp.$1;
						var value = RegExp.$2;
						info[ key.toLowerCase() ] = parseInt(value, 10) * self.memPageSize;
					}
					else if (line.match(/File\-backed\s+pages\:\s*(\d+)\./)) {
						info.filemapped = parseInt(RegExp.$1, 10) * self.memPageSize;
					}
					else if (line.match(/Pages\s+stored\s+in\s+compressor\:\s*(\d+)\./)) {
						info.compressed = parseInt(RegExp.$1, 10) * self.memPageSize;
					}
				});
				
				// compute estimate of available mem
				if (info.used && info.active) {
					info.buffers = info.used - info.active;
              		info.available = info.free + info.buffers;
				}
				
				// rough estimate of cached
				info.cached = (info.inactive || 0) + (info.compressed || 0) + (info.filemapped || 0);
				
				callback(info);
			} );
		}
		else callback(info);
	}
	
	getDiskFast(callback) {
		// get disk stats fast
		var self = this;
		var info = { rx: 0, wx: 0 };
		
		if (this.platform.linux) {
			// linux mode, use /proc
			fs.readFile( '/proc/diskstats', 'utf8', function(err, data) {
				if (err) return callback(info);
				
				data.trim().split(/\n/).forEach( function(line) {
					const parts = line.trim().split(/\s+/);
					if (parts.length < 14) return;
					
					// Skip obvious virtual/stacked devices (avoid double-counting)
					const dev = parts[2];
					if (/^(dm-\d+|md\d+|loop\d+|ram\d+|zram\d+|sr\d+|fd\d+)$/i.test(dev)) return;
					if (/^nvme\d+n\d+p\d+$/i.test(dev)) return;
					if (/^mmcblk\d+p\d+$/i.test(dev)) return;
					if (/^(sd[a-z]+|vd[a-z]+|xvd[a-z]+|hd[a-z]+)\d+$/i.test(dev)) return;
					
					info.rx += (parseInt(parts[5], 10) * 512);
					info.wx += (parseInt(parts[9], 10) * 512);
				} );
				callback(info);
			} );
		}
		else if (this.platform.darwin) {
			// macos mode, we need to exec a thing
			cp.execFile( '/usr/sbin/ioreg', ['-c', 'IOBlockStorageDriver', '-k', 'Statistics', '-r', '-w0'], { timeout: 750 }, function(err, stdout, stderr) {
				if (err) return callback(info);
				
				stdout.trim().split(/\n/).forEach( function(line) {
					// "Bytes (Read)"=1367766069248
					// "Bytes (Write)"=899319865344
					if (line.match(/\"Bytes\s*\(Read\)\"\=(\d+)/)) info.rx += parseInt(RegExp.$1, 10);
					if (line.match(/\"Bytes\s*\(Write\)\"\=(\d+)/)) info.wx += parseInt(RegExp.$1, 10);
				});
				
				callback(info);
			} );
		}
		else callback(info);
	}
	
	getNetFast(callback) {
		// get net stats fast
		var self = this;
		var info = { rx: 0, tx: 0 };
		var ifaces = [];
		
		for (var iface in this.interfaces) {
			if (iface.match(/^\w+$/) && this.interfaces[iface][0] && !this.interfaces[iface][0].internal) ifaces.push(iface);
		}
		if (!ifaces.length) return callback(info);
		
		if (this.platform.linux) {
			// use /proc/net/dev for linux (all external interfaces)
			var re = new RegExp("^\\s*(" + ifaces.join('|') + ")\\:" );
			
			fs.readFile( '/proc/net/dev', 'utf8', function(err, data) {
				if (err) return callback(info);
				
				data.trim().split(/\n/).forEach( function(line) {
					if (!line.match(re)) return;
					var parts = line.trim().split(/\s+/);
					info.rx += parseInt(parts[1], 10); // RX bytes
					info.tx += parseInt(parts[9], 10); // TX bytes
				} );
				
				callback(info);
			});
		}
		else if (this.platform.darwin) {
			// use netstat for macos (first external interface only)
			cp.execFile( '/usr/sbin/netstat', ['-bdI', this.defaultInterfaceName], { timeout: 750 }, function(err, stdout, stderr) {
				if (err) return callback(info);
				// Name       Mtu   Network       Address            Ipkts Ierrs     Ibytes    Opkts Oerrs     Obytes  Coll Drop
				// en0        1500  <Link#14>   f4:d4:88:6c:4b:ee 317608715     0 429293416196 52253328     0 11215265711     0 104
				var lines = stdout.trim().split(/\n/);
				if (lines.length < 2) return callback(info);
				
				var headers = lines.shift().trim().split(/\s+/);
				var cols = lines.shift().trim().split(/\s+/);
				
				var data = {};
				for (var idx = 0, len = headers.length; idx < len; idx++) {
					data[ headers[idx] ] = cols[idx];
				}
				
				info.rx += parseInt( data.Ibytes || 0, 10 );
				info.tx += parseInt( data.Obytes || 0, 10 );
				
				callback(info);
			});
		}
		else callback(info);
	}
	
	getProcsCached(callback) {
		// get process information, cached with a dynamic rolling debounce
		// (TTL is based on the previous cache miss elapsed time)
		// (designed to throttle on slower machines, or with thousands of processes)
		var self = this;
		var now = Tools.timeNow();
		var cache = this.procCache;
		
		if (cache.data) {
			if (now < cache.expires) {
				// still fresh
				return callback( Tools.copyHash(cache.data, true) );
			}
		}
		
		this.getProcsFast( function(data) {
			// save cache data
			cache.data = data;
			cache.date = Tools.timeNow();
			cache.elapsed = cache.date - now;
			cache.expires = cache.date + (cache.elapsed * 5);
			callback( Tools.copyHash(cache.data, true) );
		} );
	}
	
	getProcsFast(callback) {
		// get process information fast
		var self = this;
		var now = Tools.timeNow(true);
		
		if (this.platform.windows) {
			return si.processes( function(data) {
				data.list.forEach( function(proc) {
					// convert data to our native format
					try { 
						proc.started = Math.floor( (new Date(proc.started)).getTime() / 1000 );
						proc.age = now - proc.started;
					}
					catch (e) { proc.started = proc.age = 0; }
					
					// some commands are quoted
					proc.command = proc.command.replace(/^\"(.+?)\"/, '$1');
					
					// cleanup state
					proc.state = Tools.ucfirst( proc.state || 'unknown' );
					
					// memory readings are in kilobytes
					proc.memRss *= 1024;
					proc.memVsz *= 1024;
					
					// delete redundant props
					delete proc.path;
					delete proc.params;
				});
				callback(data);
			} );
		} // windows
		
		var info = { list: [] };
		if (!this.psBin) return callback(info);
		
		var ps_args = [];
		var ps_opts = {
			env: Object.assign( {}, process.env ),
			maxBuffer: 1024 * 1024 * 100, 
			timeout: 30000 
		};
		const colMap = {
			ppid: 'parentPid',
			rss: 'memRss',
			vsz: 'memVsz',
			tt: 'tty',
			thcnt: 'threads',
			pri: 'priority',
			ni: 'nice',
			s: 'state',
			stat: 'state',
			elapsed: 'age',
			cls: 'class',
			gid: 'group',
			args: 'command'
		};
		const stateMap = {
			I: 'Idle',
			S: 'Sleeping',
			D: 'Sleeping',
			U: 'Sleeping',
			R: 'Running',
			Z: 'Zombie',
			T: 'Stopped',
			t: 'Stopped',
			W: 'Paged',
			X: 'Dead'
		};
		const classMap = {
			TS: 'Other',
			FF: 'FIFO',
			RR: 'RR',
			B: 'Batch',
			ISO: 'ISO',
			IDL: 'Idle',
			DLN: 'Deadline'
		};
		const filterMap = {
			pid: parseInt,
			parentPid: parseInt,
			priority: parseInt,
			nice: parseInt,
			threads: parseInt,
			time: parseInt,
			
			// cpu: parseFloat,
			mem: parseFloat,
			
			cpu: function(value) {
				// divide by CPU count for real value
				return parseFloat(value) / self.numCPUs;
			},
			
			age: function(value) {
				if (value.match(/^\d+$/)) return parseInt(value);
				if (value.match(/^(\d+)\-(\d+)\:(\d+)\:(\d+)$/)) {
					// DD-HH:MI:SS
					var [ dd, hh, mi, ss ] = [ RegExp.$1, RegExp.$2, RegExp.$3, RegExp.$4 ];
					return ( (parseInt(dd) * 86400) + (parseInt(hh) * 3600) + (parseInt(mi) * 60) + parseInt(ss) );
				}
				if (value.match(/^(\d+)\:(\d+)\:(\d+)$/)) {
					// HH:MI:SS
					var [ hh, mi, ss ] = [ RegExp.$1, RegExp.$2, RegExp.$3 ];
					return ( (parseInt(hh) * 3600) + (parseInt(mi) * 60) + parseInt(ss) );
				}
				if (value.match(/^(\d+)\:(\d+)$/)) {
					// MI:SS
					var [ mi, ss ] = [ RegExp.$1, RegExp.$2 ];
					return ( (parseInt(mi) * 60) + parseInt(ss) );
				}
				return 0;
			},
			memRss: function(value) {
				return parseInt(value) * 1024;
			},
			memVsz: function(value) {
				return parseInt(value) * 1024;
			},
			state: function(value) {
				return stateMap[value.substring(0, 1)] || 'Unknown';
			},
			class: function(value) {
				return classMap[value] || 'Unknown';
			},
			group: function(value) {
				if (value.match(/^\d+$/)) {
					var group = Tools.getgrnam( value, true ); // cached in ram
					if (group && group.name) return group.name;
				}
				return value;
			}
		};
		
		if (this.platform.linux) {
			// PID    PPID USER     %CPU   RSS ELAPSED S PRI  NI    VSZ TT       %MEM CLS GROUP    THCNT     TIME COMMAND
			ps_args = ['-eo', 'pid,ppid,user,%cpu,rss,etimes,state,pri,nice,vsz,tty,%mem,class,group,thcount,times,args'];
			ps_opts.env.LC_ALL = 'C';
		}
		else if (this.platform.darwin) {
			// PID  PPID  %CPU %MEM PRI      VSZ    RSS NI     ELAPSED STAT TTY      USER               GID ARGS
			ps_args = ['-axro', 'pid,ppid,%cpu,%mem,pri,vsz,rss,nice,etime,state,tty,user,group,args'];
		}
		
		cp.execFile( this.psBin, ps_args, ps_opts, function(err, stdout, stderr) {
			if (err) return callback(info);
			
			var lines = stdout.trim().split(/\n/);
			var headers = lines.shift().trim().split(/\s+/).map( function(key) { return key.trim().toLowerCase().replace(/\W+/g, ''); } );
			
			lines.forEach( function(line) {
				var cols = line.trim().split(/\s+/);
				if (cols.length > headers.length) {
					var extras = cols.splice(headers.length);
					cols[ headers.length - 1 ] += ' ' + extras.join(' ');
				}
				var proc = {};
				
				headers.forEach( function(key, idx) {
					key = colMap[key] || key;
					proc[key] = filterMap[key] ? filterMap[key](cols[idx]) : cols[idx];
				} );
				
				proc.started = Math.max(0, now - (proc.age || 0));
				
				// state bookkeeping
				var state = proc.state.toLowerCase();
				info[ state ] = (info[ state ] || 0) + 1;
				info.all = (info.all || 0) + 1;
				
				// filter out ps itself
				if ((proc.parentPid == process.pid) && (proc.command.startsWith(self.psBin))) return;
				
				info.list.push(proc);
			} );
			
			callback(info);
		}); // cp.execFile
	}
	
	archiveLogs() {
		// archive logs and delete old ones, if configured
		var self = this;
		var now = Tools.timeNow(true);
		var src_spec = Path.join( this.config.get('log_dir'), '*.log' );
		var arch_path = this.config.get('log_archive_path');
		if (!arch_path) return;
		
		this.logMaint(5, "Beginning daily log archive to: " + arch_path);
		
		this.logger.archive( src_spec, arch_path, now - 1080, function(err) {
			if (err) self.logError('archive', "Failed to archive logs: " + err);
			else self.logMaint(5, "Log archive complete");
			
			var keep = self.config.get('log_archive_keep');
			if (!keep) return;
			
			keep = Tools.getSecondsFromText(keep);
			if (!keep) return;
			
			Tools.findFiles( Path.dirname(arch_path), {
				filter: function(file, stats) {
					// only include files older than specified
					return (stats.mtimeMs / 1000) < now - keep; 
				}
			},
			function(err, files) {
				if (err) self.logError('archive', "Failed to glob for old logs: " + err);
				if (!files || !files.length) return;
				
				async.eachSeries(files,
					function(file, callback) {
						self.logMaint(6, "Deleting old log archive: " + file);
						fs.unlink( file, function(err) {
							if (err) self.logError('archive', "Failed to delete old log archive: " + file + ": " + err);
							callback();
						} );
					},
					function() {
						self.logMaint(5, "Log archive deletion complete");
					}
				);
			});
		} ); // archive
	}
	
	upgradeSatellite() {
		// received upgrade request from master
		var self = this;
		this.logMaint(1, "Received upgrade request from master");
		
		// sanity
		if (this.debug) {
			this.logError('upgrade', "Cannot self-upgrade in debug mode.");
			return;
		}
		
		// if jobs are active, wait until they complete
		if (Tools.firstKey(this.activeJobs)) {
			if (!this.upgradeRequest) {
				this.logMaint(3, "Jobs still active, upgrade will wait until they all complete");
				this.upgradeRequest = true;
			}
			return;
		}
		delete this.upgradeRequest;
		
		// prep request for upgrade script
		var query = { 
			s: this.config.get('server_id') 
		};
		
		if (this.config.get('secret_key')) {
			query.t = Tools.digestHex( query.s + this.config.get('secret_key'), 'sha256' );
		}
		else {
			query.t = this.config.get('auth_token');
		}
		
		var url = (this.socket.secure ? 'https:' : 'http:') + '//' + this.socket.host + ':' + this.socket.port + '/api/app/satellite/upgrade' + Tools.composeQueryString(query);
		var cmd = '';
		var log_file = Path.resolve( this.config.get('log_dir'), 'background.log' );
		try { fs.unlinkSync(log_file); } catch (e) {;} // log is exclusive
		
		if (this.platform.windows) {
			// special behavior needed for windows (sigh)
			var task = `xyops-upgrade-${Date.now()}`;
			var temp_file = Path.join( os.tmpdir(), `${task}.ps1` );
			
			this.logMaint(5, "Upgrade task ID: " + task);
			this.logMaint(5, "Upgrade temp file: " + temp_file );
			this.logMaint(5, "Upgrade log file: " + log_file );
			
			fs.writeFileSync( temp_file, `Start-Transcript -Path '${log_file}' -Append | Out-Null\nIEX (Invoke-WebRequest -UseBasicParsing -Uri '${url}&os=windows').Content\nRemove-Item -LiteralPath $MyInvocation.MyCommand.Path -Force\nStop-Transcript | Out-Null\n` );
			
			var tr = `powershell.exe -NoProfile -ExecutionPolicy Bypass -File \\"${temp_file}\\"`;
			cmd = `schtasks /Create /TN "${task}" /SC ONCE /ST 00:00 /SD 01/01/2000 /RU SYSTEM /RL HIGHEST /TR "${tr}"`;
			cmd += ` && schtasks /Run /TN "${task}" && schtasks /Delete /TN "${task}" /F`;
		}
		else if (this.curlBin) {
			cmd = `${this.curlBin} -fsSL "${url}" | /bin/sh`;
		}
		else if (this.wgetBin) {
			cmd = `${this.wgetBin} -q -O- "${url}" | /bin/sh`;
		}
		else {
			this.logError('upgrade', "Cannot self-upgrade without curl or wget installed.");
			return;
		}
		
		this.logMaint(3, "Executing self-upgrade command: " + cmd.replace(/([\?\&]t\=)(\w+)/, '$1****'));
		
		// keep raw output log of background command
		var fd = 0;
		if (!this.platform.windows) {
			fd = fs.openSync( log_file, 'a' );
			fs.writeSync( fd, `\nStarting upgrade run at ${(new Date()).toString()}.\n` );
		}
		
		// issue command by shelling out in a detached child
		var child = null;
		try {
			child = cp.spawn( cmd, { 
				cwd: process.cwd(),
				env: Tools.copyHashRemoveKeys( process.env, { __daemon: 1 } ),
				shell: true,
				detached: true,
				stdio: this.platform.windows ? 'ignore' : ['ignore', fd, fd],
				windowsHide: true
			} );
			child.on('error', function(err) {
				self.logError('upgrade', "Failed to upgrade satellite: " + err);
			});
			child.unref();
		}
		catch (err) {
			this.logError('upgrade', "Failed to upgrade satellite: " + err);
		}
		
		if (fd) fs.closeSync(fd); // child keeps a copy
		
		// set unref'd timer in case the background command fails
		var timer = setTimeout( function() {
			if (!self.socket || !self.socket.connected || !self.socket.auth) return;
			try {
				var contents = fs.readFileSync(log_file, 'utf8').trim();
				var details = "**Log Contents:**\n\n```\n" + contents + "\n```\n";
				self.socket.send('critical', { description: `Satellite upgrade did not complete within 60 seconds.`, details });
				fs.unlinkSync(log_file);
			}
			catch (e) {;}
		}, 1000 * 60 );
		
		timer.unref();
	}
	
	uninstallSatellite() {
		// completely shutdown and uninstall satellite -- called from websocket
		var self = this;
		this.logDebug(1, "Received conductor command to uninstall satellite -- goodbye!");
		
		var cmd = process.execPath;
		var args = [ require.main.filename, "--uninstall" ];
		this.logDebug(5, "Spawning background process to perform delete", {
			cmd, args, tmpdir: os.tmpdir()
		});
		
		// issue command by exec'ing our control script in a detached child
		var child = null;
		try {
			child = cp.spawn( cmd, args, { 
				detached: true,
				stdio: ['ignore', 'ignore', 'ignore'],
				windowsHide: true
			} );
			child.on('error', function(err) {
				self.logError('uninstall', "Failed to uninstall satellite: " + err);
			});
			child.unref();
		}
		catch (err) {
			this.logError('uninstall', "Failed to uninstall satellite: " + err);
		}
	}
	
});
```

## File: `plugins/docker-plugin.js`
```javascript
#!/usr/bin/env node

// Docker Plugin for xyOps
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

// Job Params: 
// image_name, image_ver, cont_name, cont_rm, cont_init, cont_cpus, cont_mem, cont_net, cont_extras, run_mode, script, cont_cmd, verbose

const fs = require('fs');
const os = require('os');
const cp = require('child_process');
const Path = require('path');
const Tools = require('pixl-tools');
const sq = require('shell-quote');
const noop = function() {};

const docker_bin = Tools.findBinSync('docker');
if (!docker_bin) {
	console.log( JSON.stringify({ xy: 1, code: 1, description: "Unable to locate docker CLI on " + os.hostname() }) );
	process.exit(1);
}

(async function() {
	// read in data from xyops
	const chunks = [];
	for await (const chunk of process.stdin) { chunks.push(chunk); }
	let job = JSON.parse( chunks.join('') );
	let params = job.params;
	
	// build docker run command
	let child_cmd = docker_bin;
	let child_args = ['run', '-i'];
	if (params.cont_rm) child_args.push('--rm');
	if (params.cont_init) child_args.push('--init');
	if (params.cont_cpus && (params.cont_cpus !== "0")) child_args.push('--cpus', params.cont_cpus);
	if (params.cont_mem && (params.cont_mem !== "0")) child_args.push('--memory', params.cont_mem.replace(/\s+/g, ''));
	if (params.cont_net) child_args.push('--network', params.cont_net);
	if (params.cont_name) child_args.push('--name', params.cont_name);
	if (params.cont_extras) {
		child_args = child_args.concat( sq.parse(params.cont_extras) );
	}
	
	child_args.push( params.image_name + ':' + params.image_ver );
	child_args = child_args.concat( sq.parse(params.cont_cmd) );
	
	let child_opts = {
		stdio: ['pipe', 'inherit', 'inherit'],
		cwd: process.cwd(),
		env: process.env
	};
	
	if (params.verbose && (params.verbose !== "0")) {
		console.log( "Launching docker: " + child_cmd + " " + sq.quote(child_args) );
	}
	
	// spawn child to run it
	let child = null;
	let kill_timer = null;
	
	try {
		child = cp.spawn( child_cmd, child_args, child_opts );
		if (!child || !child.pid || !child.stdin) {
			throw new Error("Docker process failed to spawn (Check executable location and permissions?)");
		}
	}
	catch (err) {
		if (child) child.on('error', function() {}); // prevent crash
		console.log( JSON.stringify({
			xy: 1,
			code: 1,
			description: "Docker spawn error: " + Tools.getErrorDescription(err)
		}));
		return;
	}
	
	child.on('error', function (err) {
		// child error
		console.log( JSON.stringify({
			xy: 1,
			code: 1,
			description: "Docker process failed: " + Tools.getErrorDescription(err)
		}));
	} );
	
	child.on('exit', function (code, signal) {
		// child exited
		if (kill_timer) clearTimeout(kill_timer);
		code = (code || signal || 0);
		
		console.log( JSON.stringify({
			xy: 1,
			code: code,
			description: code ? ("Docker exited with code: " + code) : ""
		}));
	} ); // exit
	
	// silence EPIPE errors on child STDIN
	child.stdin.on('error', noop );
	
	// send job data, or plain script, based on param
	if (params.run_mode.match(/JSON/)) child.stdin.write( JSON.stringify(job) + "\n" );
	else child.stdin.write( params.script + "\n" );
	
	child.stdin.end();
	
	// Handle shutdown
	process.on('SIGTERM', function() { 
		console.log("Caught SIGTERM, killing docker: " + child.pid);
		
		kill_timer = setTimeout( function() {
			// child didn't die, kill with prejudice
			console.log("Docker did not exit, killing harder: " + child.pid);
			child.kill('SIGKILL');
		}, 9 * 1000 );
		
		// try killing nicely first
		child.kill('SIGTERM');
	} );
	
})();
```

## File: `plugins/http-plugin.js`
```javascript
#!/usr/bin/env node

// HTTP Plugin for xyOps
// Invoked via the 'HTTP Client' Plugin
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

// Job Params: 
//		method, url, headers, data, timeout, follow, ssl_cert_bypass, download, success_match, error_match

var fs = require('fs');
var os = require('os');
var cp = require('child_process');
var Path = require('path');
var JSONStream = require('pixl-json-stream');
var Tools = require('pixl-tools');
var Request = require('pixl-request');

// setup stdin / stdout streams 
process.stdin.setEncoding('utf8');
process.stdout.setEncoding('utf8');

var stream = new JSONStream( process.stdin, process.stdout );
stream.EOL = "\n";

stream.on('json', function(job) {
	// got job from parent
	var params = job.params;
	var request = new Request();
	
	// try to scrub secrets from output details (best effort)
	var scrubSecrets = null;
	if (job.secrets && Tools.firstKey(job.secrets)) {
		var sec_re = new RegExp( "\\b(" + 
			Object.values(job.secrets).map( sec => Tools.escapeRegExp(sec) ).join('|') + '|' + 
			Object.values(job.secrets).map( sec => Tools.escapeRegExp( encodeURIComponent(sec) ) ).join('|') + 
			")\\b", 'g' );
		scrubSecrets = function(value) { return String(value).replace( sec_re, '(REDACTED)' ); }
	}
	else {
		scrubSecrets = function(value) { return value; };
	}
	
	var print = function(text) {
		process.stdout.write(text);
	};
	
	// airgapped mode
	if (job.airgap && job.airgap.enabled) {
		if (job.airgap.whitelist && job.airgap.whitelist.length) request.setWhitelist( job.airgap.whitelist );
		if (job.airgap.blacklist && job.airgap.blacklist.length) request.setBlacklist( job.airgap.blacklist );
	}
	
	// timeout
	request.setTimeout( parseInt(params.timeout || 0) * 1000 );
	request.setIdleTimeout( parseInt(params.idle_timeout || params.timeout || 0) * 1000 );
	
	if (!params.url || !params.url.match(/^https?\:\/\/\S+$/i)) {
		stream.write({ xy: 1, complete: true, code: 1, description: "Malformed URL: " + (params.url || '(n/a)') });
		return;
	}
	
	// allow URL to be substituted using [placeholders]
	params.url = Tools.sub( params.url, job );
	
	print("Sending HTTP " + params.method + " to URL:\n" + scrubSecrets(params.url) + "\n");
	
	// headers
	if (params.headers) {
		// allow headers to be substituted using [placeholders]
		params.headers = Tools.sub( params.headers, job );
		
		// print("\nRequest Headers:\n" + params.headers.trim() + "\n");
		params.headers.replace(/\r\n/g, "\n").trim().split(/\n/).forEach( function(pair) {
			if (pair.match(/^([^\:]+)\:\s*(.+)$/)) {
				request.setHeader( RegExp.$1, RegExp.$2 );
			}
		} );
	}
	
	// follow redirects
	if (params.follow) request.setFollow( 32 );
	
	var opts = {
		method: params.method
	};
	
	// ssl cert bypass
	if (params.ssl_cert_bypass) {
		opts.rejectUnauthorized = false;
	}
	
	// post data
	if ((opts.method != 'GET') && (opts.method != 'HEAD')) {
		// allow POST data to be substituted using [placeholders]
		params.data = Tools.sub( params.data, job );
		
		// print("\nPOST Data:\n" + params.data.trim() + "\n");
		opts.data = Buffer.from( params.data || '' );
	}
	
	// download
	if (params.download) {
		opts.download = params.download = Path.join( job.cwd, job.id + '-download.bin' );
	}
	
	// progress
	var prog = { current: 0, len: 0 };
	opts.progress = function(chunk, res) {
		if (res.headers && res.headers['content-length']) {
			if (!prog.len) prog.len = parseInt( res.headers['content-length'] );
			prog.current += chunk.length;
			if (prog.len) stream.write({ xy: 1, progress: prog.current / prog.len });
		}
	};
	
	// matching
	var success_match = new RegExp( params.success_match || '.*' );
	var error_match = new RegExp( params.error_match || '(?!)' );
	
	// send request
	request.request( params.url, opts, function(err, resp, data, perf) {
		// HTTP code out of success range = error
		if (!err && ((resp.statusCode < 200) || (resp.statusCode >= 400))) {
			err = new Error("HTTP " + resp.statusCode + " " + resp.statusMessage);
			err.code = resp.statusCode;
		}
		
		// successmatch?  errormatch?
		var text = (!params.download && data) ? data.toString() : '';
		if (!err) {
			if (text.match(error_match)) {
				err = new Error("Response contains error match: " + params.error_match);
			}
			else if (!text.match(success_match)) {
				err = new Error("Response missing success match: " + params.success_match);
			}
		}
		
		// start building xyops JSON update
		var update = { 
			xy: 1,
			complete: true
		};
		if (err) {
			update.code = err.code || 1;
			update.description = err.message || err;
		}
		else {
			update.code = 0;
			update.description = "Success (HTTP " + resp.statusCode + " " + resp.statusMessage + ")";
		}
		
		print( update.description + "\n" );
		
		// attach file to job for upload
		if (!err && params.download) {
			var filename = Path.basename(params.url) || 'output';
			if (resp.headers && resp.headers['content-disposition']) {
				// grab filename out of CD header, which may or may not have quotes
				if (resp.headers['content-disposition'].toString().match(/filename="(.+?)"/)) filename = RegExp.$1;
				else if (resp.headers['content-disposition'].toString().match(/filename=([^\;]+)/)) filename = RegExp.$1;
			}
			if (!filename.match(/\.\w+$/)) {
				if (resp.headers['content-type']) filename += '.' + Path.basename(resp.headers['content-type']);
				else filename += '.bin';
			}
			update.files = [
				{ path: params.download, filename: filename, delete: true } 
			];
		}
		
		// populate data object with response
		if (resp) update.data = {
			statusCode: resp.statusCode,
			statusMessage: resp.statusMessage,
			headers: resp.headers
		};
		
		// include markdown report of request and response
		var details = '';
		
		details += "### Summary\n";
		details += "- **Method:** " + params.method + "\n";
		details += "- **URL:** " + scrubSecrets(params.url) + "\n";
		details += "- **Redirects:** " + (params.follow ? 'Follow' : 'n/a') + "\n";
		details += "- **Timeout:** " + Tools.getTextFromSeconds(params.timeout, false, false) + "\n";
		if (resp) details += "- **Response:** HTTP " + resp.statusCode + " " + resp.statusMessage + "\n";
		else if (err) details += "- **Error:** " + err + "\n";
		
		if (params.headers.length) {
			details += "\n### Request Headers:\n\n```http\n";
			details += scrubSecrets(params.headers) + "\n";
			details += "```\n";
		}
		
		if (params.data && params.data.length) {
			details += "\n### Request Body:\n\n```\n";
			details += scrubSecrets(params.data.trim()) + "\n```\n";
		}
		
		if (resp && resp.rawHeaders) {
			details += "\n### Response Headers:\n\n```http\n";
			
			for (var idx = 0, len = resp.rawHeaders.length; idx < len; idx += 2) {
				details += resp.rawHeaders[idx] + ": " + scrubSecrets(resp.rawHeaders[idx + 1]) + "\n";
			}
			details += "```\n";
		}
		else if (err) {
			details += "\n### Error:\n\n" + err + "\n";
		}
		
		// add raw response content, if text (and not too long)
		if (text && resp && resp.headers['content-type'] && resp.headers['content-type'].match(/(text|javascript|json|css|html)/i)) {
			if (text.length) {
				details += "\n### Response Body:\n\n```\n";
				if (text.length >= 1024 * 1024) details += "(Too large to display)\n```\n";
				else details += scrubSecrets(text.trim()) + "\n```\n";
			}
			
			// if response was JSON, include parsed data, up to 32 MB
			if ((text.length < 1024 * 1024 * 32) && (resp.headers['content-type'].match(/(application|text)\/json/i) || text.match(/^\s*\{[\S\s]+\}\s*$/))) {
				var json = null;
				try { json = JSON.parse(text); }
				catch (e) {
					print("\nWARNING: Failed to parse JSON response: " + e + " (could not include JSON in job data)\n");
				}
				if (json && update.data) update.data.json = json;
			}
		}
		
		if (perf) details += "\n### Performance Metrics:\n\n```json\n" + JSON.stringify(perf.metrics(), null, "\t") + "\n```\n";
		
		update.markdown = {
			title: "HTTP Request Details",
			content: details
		};
		
		if (perf) {
			// passthru perf to xyops
			update.perf = perf.metrics();
		}
		
		stream.write(update);
	} );
});
```

## File: `plugins/shell-plugin.js`
```javascript
#!/usr/bin/env node

// Shell Script Runner for xyOps
// Invoked via the 'Shell Script' Plugin
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

const fs = require('fs');
const os = require('os');
const cp = require('child_process');
const Path = require('path');
const sqparse = require('shell-quote').parse;
const JSONStream = require('pixl-json-stream');
const Tools = require('pixl-tools');

const is_windows = !!process.platform.match(/^win/);
const RE_SHEBANG = /^\#\!([^\n]+)\n/;

// setup stdin / stdout streams
process.stdin.setEncoding('utf8');
process.stdout.setEncoding('utf8');

var stream = new JSONStream( process.stdin, process.stdout );
stream.EOL = "\n";

stream.once('json', function(job) {
	// got job from parent
	var script_file = Path.join( job.temp_dir, 'xyops-script-temp-' + job.id );
	var child_cmd = Path.resolve(script_file);
	var child_args = [];
	var child_opts = {
		stdio: ['pipe', 'pipe', 'pipe'],
		cwd: process.cwd()
	};
	
	// passthrough all data if desired
	if (job.params.pass && job.input && job.input.data) {
		stream.write({ xy: 1, data: job.input.data });
	}
	
	// convert to unix line endings universally (windows 10+ is fine with this)
	if (job.params.script.match(/\r/)) job.params.script = job.params.script.replace(/\r\n/g, "\n");
	
	if (is_windows) {
		// we have to parse the shebang ourselves
		if (job.params.script.match(RE_SHEBANG)) {
			var shebang = RegExp.$1.trim();
			
			if (shebang.match(/^powershell(\.exe)?$/i)) {
				script_file += '.ps1';
				child_cmd = 'POWERSHELL.EXE';
				child_args = ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', script_file];
			}
			else if (shebang.match(/^pwsh(\.exe)?$/i)) {
				script_file += '.ps1';
				child_cmd = 'PWSH.EXE';
				child_args = ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', script_file];
			}
			else if (shebang.match(/^cmd(\.exe)?$/i)) {
				script_file += '.bat';
				child_cmd = 'CMD.EXE';
				child_args = ['/c', script_file];
			}
			else if (shebang.match(/\b(powershell|pwsh)\b/i)) {
				// powershell with custom exe location and/or CLI arguments
				script_file += '.ps1';
				child_cmd = shebang;
				// if command has cli args, parse using shell-quote
				if (child_cmd.match(/\s+(.+)$/)) {
					var cargs_raw = RegExp.$1;
					child_cmd = child_cmd.replace(/\s+(.+)$/, '');
					child_args = sqparse( cargs_raw, process.env );
				}
				child_args.push( '-File', script_file );
			}
			else if (shebang.match(/\b(cmd)\b/i)) {
				// cmd with custom exe location and/or ClI arguments
				script_file += '.bat';
				child_cmd = shebang;
				// if command has cli args, parse using shell-quote
				if (child_cmd.match(/\s+(.+)$/)) {
					var cargs_raw = RegExp.$1;
					child_cmd = child_cmd.replace(/\s+(.+)$/, '');
					child_args = sqparse( cargs_raw, process.env );
				}
				child_args.push( '/c', script_file );
			}
			else {
				// generic executable
				child_cmd = shebang;
				child_args = [ script_file ];
			}
			
			// remove shebang line
			job.params.script = job.params.script.replace(RE_SHEBANG, "");
		}
		else {
			// no shebang, assume cmd.exe
			script_file += '.bat';
			child_cmd = 'CMD.EXE';
			child_args = ['/c', script_file];
		}
		child_opts.windowsHide = true;
	} // is_windows
	
	// write out temp file containing script code
	fs.writeFileSync( script_file, job.params.script, { mode: 0o775 } );
	
	// spawn child to run it
	var child = cp.spawn( child_cmd, child_args, child_opts );
	
	var kill_timer = null;
	var stderr_buffer = '';
	var sent_html = false;
	
	var cstream = new JSONStream( child.stdout, child.stdin );
	cstream.recordRegExp = /^\s*\{.+\}\s*$/;
	
	cstream.on('json', function(data) {
		// received JSON data from child, pass along to xyOps or log
		stream.write(data);
		if (data.html) sent_html = true;
	} );
	
	cstream.on('text', function(line) {
		// received non-json text from child
		// look for plain number from 0 to 100, treat as progress update
		if (line.match(/^\s*(\d+)\%\s*$/)) {
			var progress = Math.max( 0, Math.min( 100, parseInt( RegExp.$1 ) ) ) / 100;
			stream.write({
				xy: 1,
				progress: progress
			});
		}
		else {
			// otherwise just log it
			if (job.params.annotate) {
				var dargs = Tools.getDateArgs( new Date() );
				line = '[' + dargs.yyyy_mm_dd + ' ' + dargs.hh_mi_ss + '] ' + line;
			}
			process.stdout.write(line);
		}
	} );
	
	cstream.on('error', function(err, text) {
		// Probably a JSON parse error (child emitting garbage)
		if (text) process.stdout.write(text + "\n");
	} );
	
	child.on('error', function (err) {
		// child error
		stream.write({
			xy: 1,
			complete: true,
			code: 1,
			description: "Script failed: " + Tools.getErrorDescription(err)
		});
		
		fs.unlink( script_file, function(err) {;} );
	} );
	
	child.on('exit', function (code, signal) {
		// child exited
		if (kill_timer) clearTimeout(kill_timer);
		code = (code || signal || 0);
		
		var data = {
			xy: 1,
			complete: true,
			code: code,
			description: code ? ("Script exited with code: " + code) : ""
		};
		
		if (stderr_buffer.length && stderr_buffer.match(/\S/)) {
			if (!sent_html) data.html = {
				title: "Error Output",
				content: "<pre>" + stderr_buffer.replace(/</g, '&lt;').trim() + "</pre>"
			};
			
			if (code) {
				// possibly augment description with first line of stderr, if not too insane
				var stderr_line = stderr_buffer.trim().split(/\n/).shift();
				if (stderr_line.length < 256) data.description += ": " + stderr_line;
			}
		}
		
		stream.write(data);
		fs.unlink( script_file, function(err) {;} );
	} ); // exit
	
	// silence EPIPE errors on child STDIN
	child.stdin.on('error', function(err) {
		// ignore
	} );
	
	// track stderr separately for display purposes
	child.stderr.setEncoding('utf8');
	child.stderr.on('data', function(data) {
		// keep first 32K in RAM, but log everything
		if (stderr_buffer.length < 32768) stderr_buffer += data;
		else if (!stderr_buffer.match(/\.\.\.$/)) stderr_buffer += '...';
		
		process.stdout.write(data);
	});
	
	// pass job down to child process (harmless for shell, useful for php/perl/node)
	cstream.write( job );
	child.stdin.end();
	
	// Handle shutdown
	process.on('SIGTERM', function() { 
		console.log("Caught SIGTERM, killing child: " + child.pid);
		
		kill_timer = setTimeout( function() {
			// child didn't die, kill with prejudice
			console.log("Child did not exit, killing harder: " + child.pid);
			child.kill('SIGKILL');
		}, 9 * 1000 );
		
		// try killing nicely first
		child.kill('SIGTERM');
	} );
	
} ); // stream
```

## File: `plugins/test-plugin.js`
```javascript
#!/usr/bin/env node

// Test Plugin for xyOps
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

var fs = require('fs');
var cp = require('child_process');
var os = require('os');
var Path = require('path');
var JSONStream = require('pixl-json-stream');
var Tools = require('pixl-tools');
var Perf = require('pixl-perf');
var Request = require('pixl-request');

var perf = new Perf();
perf.setScale( 1 ); // seconds
perf.begin();

var request = new Request();
request.setTimeout( 300 * 1000 );
request.setFollow( 5 );
request.setAutoError( true );
request.setKeepAlive( false );

var net_url = 'https://github.com/jhuckaby/performa-satellite/releases/latest/download/performa-satellite-linux-x64';
var ac = null;

// setup stdin / stdout streams 
// process.stdin.setEncoding('utf8');
// process.stdout.setEncoding('utf8');

// console.warn("Printed this with console.warn, should go to stderr.");
// console.log("Printed this with console.log, should be ignored as not json.");
console.log("Job start!");

// ANSI escape codes
(function() {
	// ANSI escape codes for text styles
	const RESET = '\x1b[0m';
	const BOLD = '\x1b[1m';
	const DIM = '\x1b[2m';
	const ITALIC = '\x1b[3m';
	const UNDERLINE = '\x1b[4m';
	const INVERSE = '\x1b[7m';
	const STRIKETHROUGH = '\x1b[9m';

	// ANSI escape codes for colors
	const BLACK = '\x1b[30m';
	const RED = '\x1b[31m';
	const GREEN = '\x1b[32m';
	const YELLOW = '\x1b[33m';
	const BLUE = '\x1b[34m';
	const MAGENTA = '\x1b[35m';
	const CYAN = '\x1b[36m';
	const WHITE = '\x1b[37m';
	const GRAY = '\x1b[90m';
	
	console.log(`Testing some ANSI colors and styles: ${BOLD}Bold text${RESET}, ${DIM}Dim text${RESET}, ${ITALIC}Italic text${RESET}, ${UNDERLINE}Underlined text${RESET}, ${INVERSE}Inverse text${RESET}, ${STRIKETHROUGH}Strikethrough text${RESET}, ${BLACK}Black text${RESET}, ${RED}Red text${RESET}, ${GREEN}Green text${RESET}, ${YELLOW}Yellow text${RESET}, ${BLUE}Blue text${RESET}, ${MAGENTA}Magenta text${RESET}, ${CYAN}Cyan text${RESET}, ${WHITE}White text${RESET}, ${GRAY}Gray text${RESET}.`);
})();

if (process.argv.length > 2) console.log("ARGV: " + JSON.stringify(process.argv));

/*process.on('SIGTERM', function() {
	console.warn("Caught SIGTERM and ignoring it!  Hahahahaha!");
} );*/

var stream = new JSONStream( process.stdin, process.stdout );
stream.EOL = "\n";

stream.on('json', function(job) {
	// got job from parent 
	console.log( "Job Params: " + JSON.stringify(job.params) );
	console.log( "The current working directory is: " + process.cwd() );
	console.log( "The current date/time for our job is: " + (new Date(job.now * 1000)).toString() );
	
	// report if we got input
	if (job.input && job.input.data) {
		console.log( "Received input data: " + JSON.stringify(job.input.data) );
	}
	if (job.input && job.input.files && job.input.files.length) {
		console.log( "Received input files: " + JSON.stringify(job.input.files) );
		console.log( "Glob: " + JSON.stringify( Tools.glob.sync('*') ) );
	}
	
	// airgapped mode
	if (job.airgap && job.airgap.enabled) {
		if (job.airgap.whitelist && job.airgap.whitelist.length) request.setWhitelist( job.airgap.whitelist );
		if (job.airgap.blacklist && job.airgap.blacklist.length) request.setBlacklist( job.airgap.blacklist );
	}
	
	// use some memory so we show up on the mem graph
	var buf = null;
	if (job.params.burn) {
		buf = Buffer.alloc( 1024 * 1024 * Math.floor( 128 + (Math.random() * 128) ) );
	}
	
	var start = Tools.timeNow();
	var idx = 0;
	var duration = 0;
	var req_in_progress = false;
	
	if (job.params.duration.toString().match(/^(\d+)\-(\d+)$/)) {
		var low = RegExp.$1;
		var high = RegExp.$2;
		low = parseInt(low);
		high = parseInt(high);
		duration = Math.round( low + (Math.random() * (high - low)) );
		console.log( "Chosen random duration: " + duration + " seconds" );
	}
	else {
		duration = parseInt( job.params.duration );
	}
	
	duration = Math.max(1, duration);
	
	// spawn child process
	if (process.platform == 'win32') cp.exec( 'timeout /t ' + Math.floor(duration - 1) + ' /nobreak >nul', function(err, stdout, stderr) {} );
	else cp.exec( 'sleep ' + Math.floor(duration - 1), function(err, stdout, stderr) {} );
	
	var timer = setInterval( function() {
		var now = Tools.timeNow();
		var elapsed = now - start;
		var progress = Math.min( elapsed / duration, 1.0 );
		
		if (buf) buf.fill( String.fromCharCode( Math.floor( Math.random() * 256 ) ) );
		
		// report progress
		// console.log( "Progress: " + Tools.shortFloat(progress));
		stream.write({
			xy: 1,
			progress: progress
		});
		
		idx++;
		
		if (progress >= 1.0) {
			console.log( "We're done!" );
			perf.end();
			clearTimeout( timer );
			
			// abort network request if still in progress
			if (ac) ac.abort();
			
			// insert some fake random stats into perf
			var max = perf.scale * (duration / 5);
			var rand_range = function(low, high) { return low + (Math.random() * (high - low)); };
			
			perf.perf.db_query = { end: 1, elapsed: rand_range(0, max * 0.3) };
			perf.perf.db_connect = { end: 1, elapsed: rand_range(max * 0.2, max * 0.5) };
			perf.perf.log_read = { end: 1, elapsed: rand_range(max * 0.4, max * 0.7) };
			perf.perf.gzip_data = { end: 1, elapsed: rand_range(max * 0.6, max * 0.9) };
			perf.perf.http_post = { end: 1, elapsed: rand_range(max * 0.8, max * 1) };
			
			perf.count('lines', 52);
			perf.count('db_rows', 81);
			perf.count('db_conns', 8);
			perf.count('errors', 12);
			
			// include a table with some stats
			var table = {
				title: "Sample Job Stats",
				header: [
					"IP Address", "DNS Lookup", "Flag", "Count", "Percentage"
				],
				rows: [
					["62.121.210.2", "directing.com", "MaxEvents-ImpsUserHour-DMZ", 138, "0.0032%" ],
					["97.247.105.50", "hsd2.nm.comcast.net", "MaxEvents-ImpsUserHour-ILUA", 84, "0.0019%" ],
					["21.153.110.51", "grandnetworks.net", "InvalidIP-Basic", 20, "0.00046%" ],
					["95.224.240.69", "hsd6.mi.comcast.net", "MaxEvents-ImpsUserHour-NM", 19, "0.00044%" ],
					["72.129.60.245", "hsd6.nm.comcast.net", "InvalidCat-Domestic", 17, "0.00039%" ],
					["21.239.78.116", "cable.mindsprung.com", "InvalidDog-Exotic", 15, "0.00037%" ]
				],
				caption: "This is an example stats table you can generate from within your Plugin code."
			};
			
			// include a custom html report
			var html = {
				title: "Sample Job Report",
				content: "<pre>This is a sample text report you can generate from within your Plugin code (can be HTML too).\n\n-------------------------------------------------\n          Date/Time | 2015-10-01 6:28:38 AM      \n       Elapsed Time | 1 hour 15 minutes          \n     Total Log Rows | 4,313,619                  \n       Skipped Rows | 15                         \n  Pre-Filtered Rows | 16,847                     \n             Events | 4,296,757                  \n        Impressions | 4,287,421                  \n Backup Impressions | 4,000                      \n             Clicks | 5,309 (0.12%)              \n      Backup Clicks | 27 (0.00062%)              \n       Unique Users | 1,239,502                  \n-------------------------------------------------</pre>",
				caption: ""
			};
			
			if (job.params.upload) {
				var temp_file = 'sample-report-' + job.id + '.txt';
				fs.writeFileSync( temp_file, html.content.replace(/<.+?>/g, '') + "\n" );
				stream.write({
					xy: 1,
					push: {
						files: [ { path: temp_file, delete: true } ]
					}
				});
			}
			
			switch (job.params.action) {
				case 'Success':
					console.log( "Simulating a successful response." );
					stream.write({
						xy: 1,
						complete: true,
						code: 0,
						description: "Success!",
						perf: perf.metrics(),
						table: table,
						html: html,
						data: {
							text: "This is some sample data to pass to the next job!",
							hostname: os.hostname(),
							pid: process.pid,
							random: Tools.shortFloat( Math.random() ),
							obj: { foo: 1, bar: null, bool: true },
							custom: job.params.custom
						}
					});
				break;
				
				case 'Error':
					console.log( "Simulating an error response." );
					stream.write({
						xy: 1,
						complete: true,
						code: 999,
						description: "Simulating an error message here.  Something went wrong!",
						perf: perf.metrics()
					});
				break;
				
				case 'Warning':
					console.log( "Simulating a warning response." );
					stream.write({
						xy: 1,
						complete: true,
						code: 'warning',
						description: "Simulating a warning message here.  Something is concerning!",
						perf: perf.metrics()
					});
				break;
				
				case 'Critical':
					console.log( "Simulating an error response." );
					stream.write({
						xy: 1,
						complete: true,
						code: 'critical',
						description: "Simulating a critical error message here.  Something is VERY wrong!",
						perf: perf.metrics()
					});
				break;
				
				case 'Abort':
					console.log( "Simulating an abort response." );
					stream.write({
						xy: 1,
						complete: true,
						code: 'abort',
						description: "Simulating an abort message here.",
						perf: perf.metrics()
					});
				break;
				
				case 'Crash':
					console.log( "Simulating a crash..." );
					setTimeout( function() { 
						// process.exit(1); 
						throw new Error("Test Crash");
					}, 100 );
				break;
			}
			
			// allow organic exit so stream.writes can complete
			// process.exit(0);
		}
		else {
			// burn up some CPU so we show up on the chart
			if (job.params.burn) {
				var temp = Tools.timeNow();
				while (Tools.timeNow() - temp < 0.10) {
					var x = Math.PI * 32768 / 100.3473847384 * Math.random();
				}
			}
			
			if (job.params.network && !req_in_progress) {
				// repeatedly fetch large file to generate network connections and traffic
				req_in_progress = true;
				ac = new AbortController();
				request.get( net_url, { signal: ac.signal }, function() { req_in_progress = false; ac = null; } );
			}
		}
		
	}, 150 );
	
} );
```

## File: `tools/changelog.js`
```javascript
#!/usr/bin/env node

// Build xySat CHANGELOG.md file

var fs = require('fs');
var Path = require('path');
var cp = require('child_process');
var Tools = require('pixl-tools');

var debug = (process.argv[2] == 'debug');

// make sure we're in the correct dir
process.chdir( Path.dirname( __dirname ) );

// make sure git sandbox is clean
var porcelain = cp.execSync('git status --porcelain', { encoding: 'utf8' }).trim();
if (!debug && porcelain.length) {
	console.error("\nERROR: Git sandbox has local changes.  Please commit these before updating the changelog.\n");
	process.exit(1);
}

// get list of tags
var tags = cp.execSync('git tag --list --sort=version:refname', { encoding: 'utf8' }).trim().split(/\n/).reverse();

var md = '';
md += "# xySat Changelog\n";

var last_tag = tags.pop();
if (!tags.length) {
	console.error("\nERROR: No tags found after popping first one.  Please push another tag before running changelog.\n");
	process.exit(1);
}

tags.forEach( function(tag, idx) {
	var prev_tag = tags[idx + 1] || last_tag;
	md += `\n## Version ${tag}\n\n`;
	
	var cmd = `git log ${prev_tag}..${tag} --no-merges --pretty=format:'%h %H %ad %s%n%n%b%n----PX----' --date=short`;
	var output = cp.execSync(cmd, { encoding: 'utf8' }).trim();
	var commits = output.split('----PX----');
	var first = true;
	
	// 029a96a 029a96aebd721fe565b1b5c8f2b661564c9017f3 2025-12-30 Version 0.9.2
	commits.forEach( function(chunk) {
		var lines = chunk.trim().split(/\n/);
		var line = lines.shift();
		
		var matches = line.trim().match(/^(\w+)\s+(\w+)\s+([\d\-]+)\s+(.+)$/);
		if (!matches) return;
		if (matches[4].match(/\b(CHANGELOG)\b/)) return;
		
		var url = 'https://github.com/pixlcore/xysat/commit/' + matches[2];
		
		if (first) {
			md += `> ` + Tools.formatDate( matches[3] + ' 00:00:00', '[mmmm] [mday], [yyyy]' ) + "\n\n";
			first = false;
		}
		
		md += `- [\`${matches[1]}\`](${url}): ` + matches[4] + "\n";
		
		if (matches[4].match(/^Version/)) lines.forEach( function(extra) {
			if (!extra.match(/\S/)) return;
			extra = extra.trim();
			if (!extra.match(/^\-/)) extra = '- ' + extra;
			md += "\t" + extra + "\n";
		} );
	} );
} );

md += `\n## Version ${last_tag}\n\n> March 17, 2025\n\n- Initial beta release!\n`;

if (debug) {
	console.log(md);
	process.exit(0);
}

fs.writeFileSync( 'CHANGELOG.md', md );

// make sure log has actually changed
porcelain = cp.execSync('git status --porcelain', { encoding: 'utf8' }).trim();
if (!porcelain.length) {
	console.error("\nWarning: Changelog has not changed since last run.  Skipping actions.\n");
	process.exit(1);
}

cp.execSync('git add CHANGELOG.md && git commit -m "Update CHANGELOG" && git push', { stdio: 'inherit' } );
```

## File: `tools/test-monitors.js`
```javascript
#!/usr/bin/env node

// xySat - xyOps Satellite - Monitor Test Run
// Copyright (c) 2019 - 2025 PixlCore LLC
// BSD 3-Clause License -- see LICENSE.md

const PixlServer = require("pixl-server");
const pkg = require('../package.json');

var config = {
	hosts: [ "localhost" ],
	port: 5522,
	secure: false,
	socket_opts: { rejectUnauthorized: false },
	pid_file: "test-pid.txt",
	log_dir: "logs",
	log_filename: "test.log",
	log_crashes: true,
	log_archive_path: "logs/archives/[filename]-[yyyy]-[mm]-[dd].log.gz",
	log_archive_keep: "7 days",
	temp_dir: "temp",
	child_kill_timeout: 10,
	monitoring_enabled: true,
	quickmon_enabled: true,
	
	debug_level: 10,
	echo: true,
	color: true,
	foreground: true
};

const cli = require('pixl-cli');
var Tools = cli.Tools;
var async = Tools.async;
var args = cli.args;
cli.global();

var MockEngine = require('../lib/engine.js');

MockEngine.prototype.socketInit = function() {
	// mock sock
	this.socket = {
		connected: true,
		auth: true,
		send: function(cmd, data) {
			println( "\nMock Socket: " + cmd + ": " + JSON.stringify(data, null, "\t") + "\n" );
		}
	};
};

MockEngine.prototype.socketConnect = function() {};
MockEngine.prototype.socketDisconnect = function() {};

MockEngine.prototype.tick = function() {};
MockEngine.prototype.minute = function() {};
MockEngine.prototype.day = function() {};

MockEngine.prototype.shutdown = function(callback) { callback(); };

println("\n" + bold("Starting monitoring self-test run...") + "\n" );

// chdir to the proper server root dir
process.chdir( require('path').dirname( __dirname ) );

// start server
var server = new PixlServer({
	__name: 'Satellite',
	__version: pkg.version,
	
	config: config,
	
	components: [
		MockEngine
	]
});

server.startup( function() {
	// server startup complete
	process.title = "xySat Test";
	var sat = server.Satellite;
	sat.numServers = 1;
	
	async.series([
		function(callback) {
			// getBasicServerInfo
			println("\n" + bold("Test getBasicServerInfo...") + "\n" );
			sat.getBasicServerInfo( function(info) {
				println("\nServer Info: " + JSON.stringify(info, null, "\t") + "\n");
				callback();
			} );
		},
		function(callback) {
			// runQuickMonitors
			println("\n" + bold("Test runQuickMonitors...") + "\n" );
			sat.runQuickMonitors( { max_sleep_ms: 1 }, function() {
				callback();
			} );
		},
		function(callback) {
			// runMonitors
			println("\n" + bold("Test runMonitors...") + "\n" );
			sat.runMonitors( { max_sleep_ms: 1 }, function() {
				callback();
			} );
		}
	],
	function() {
		println("\n" + bold("All tests complete. Shutting down...") + "\n" );
		server.shutdown();
	});
} );
```

## File: `win/install.bat`
```
@echo off
rem install-service.bat - Installs the xyOps Satellite service
setlocal enabledelayedexpansion

net session >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo This script requires administrative privileges.
    echo Please approve the prompt in the next window.
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

rem Get the directory of the script
set "SCRIPT_DIR=%~dp0"
set "NODE_EXE=%SCRIPT_DIR%bin\node.exe"
set "MAIN_JS=%SCRIPT_DIR%main.js --install"

rem Check if Node.exe exists
if not exist "%NODE_EXE%" (
    echo ERROR: Node executable not found at: %NODE_EXE%
    exit /b 1
)

rem Check if the main script exists
if not exist "%MAIN_JS%" (
    echo ERROR: Satellite main script not found at: %MAIN_JS%
    exit /b 1
)

echo Installing xyOps Satellite...

rem Start the application
"%NODE_EXE%" "%MAIN_JS%"

rem Check if process started successfully
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to install xyOps Satellite. Exit code: %ERRORLEVEL%
    exit /b %ERRORLEVEL%
)

endlocal
exit /b
```

## File: `win/uninstall.bat`
```
@echo off
rem uninstall-service.bat - Remove the xyOps Satellite service
setlocal enabledelayedexpansion

net session >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo This script requires administrative privileges.
    echo Please approve the prompt in the next window.
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

rem Get the directory of the script
set "SCRIPT_DIR=%~dp0"
set "NODE_EXE=%SCRIPT_DIR%bin\node.exe"
set "MAIN_JS=%SCRIPT_DIR%main.js --uninstall"

rem Check if Node.exe exists
if not exist "%NODE_EXE%" (
    echo ERROR: Node executable not found at: %NODE_EXE%
    exit /b 1
)

rem Check if the main script exists
if not exist "%MAIN_JS%" (
    echo ERROR: Satellite main script not found at: %MAIN_JS%
    exit /b 1
)

echo Removing xyOps Satellite...

rem Start the application
"%NODE_EXE%" "%MAIN_JS%"

rem Check if process started successfully
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to remove xyOps Satellite. Exit code: %ERRORLEVEL%
    exit /b %ERRORLEVEL%
)

endlocal
exit /b
```

