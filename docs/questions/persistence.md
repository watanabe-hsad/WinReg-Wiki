# 自启动与持久化

## 检查目标

确认系统启动、用户登录、Shell 加载、服务启动或认证链加载时是否存在自动执行配置。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [HKCU Run / RunOnce](../registry-tree/hkcu/software/microsoft/windows/currentversion/run.md) | 用户级登录启动项。 | 只作用于对应用户 SID。 |
| [HKLM Run / RunOnce](../registry-tree/hklm/software/microsoft/windows/currentversion/run.md) | 机器级登录启动项。 | 32 位视图需看 `WOW6432Node`。 |
| [Command Processor](../registry-tree/hkcu/software/microsoft/command-processor.md) | 用户级 `cmd.exe` `AutoRun`。 | 只在命令处理器启动时触发。 |
| [HKLM Command Processor](../registry-tree/hklm/software/microsoft/command-processor.md) | 机器级 `cmd.exe` `AutoRun`。 | 影响范围更大，但仍需触发证据。 |
| [HKCU Environment](../registry-tree/hkcu/environment.md) | 用户级环境变量和 `Path`。 | 影响进程环境，不等于命令执行。 |
| [HKLM Environment](../registry-tree/hklm/system/controlset/control/session-manager/environment.md) | 系统级环境变量和 `Path`。 | 需要结合具体进程环境。 |
| [BootExecute](../registry-tree/hklm/system/controlset/control/session-manager/bootexecute.md) | 启动早期执行项。 | 需要重启和执行证据。 |
| [AppCertDlls](../registry-tree/hklm/system/controlset/control/session-manager/appcertdlls.md) | AppCert DLL 配置。 | 非空配置需验证模块加载。 |
| [SubSystems](../registry-tree/hklm/system/controlset/control/session-manager/subsystems.md) | Windows 子系统初始化配置。 | 异常需和同版本基线对照。 |
| [KnownDLLs](../registry-tree/hklm/system/controlset/control/session-manager/knowndlls.md) | Known DLL 映射。 | 需结合基线和模块加载。 |
| [Active Setup](../registry-tree/hklm/software/microsoft/active-setup.md) | 每用户初始化命令。 | 需比对 HKLM 组件和 HKCU stub。 |
| [Services](../registry-tree/hklm/system/controlset/services/index.md) | 服务和驱动配置。 | 服务配置存在不等于已启动。 |
| [Drivers](../registry-tree/hklm/system/controlset/services/drivers.md) | kernel / file system driver 启动配置。 | 需验证签名、路径和加载事件。 |
| [IFEO](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/ifeo.md) | `Debugger`、SilentProcessExit 等进程启动相关配置。 | 正常调试和 EDR 也可能使用。 |
| [AppInit_DLLs](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/appinit-dlls.md) | User32 相关 DLL 加载配置。 | 是否加载取决于系统配置和进程类型。 |
| [Winlogon](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | `Userinit`、`Shell`、自动登录和隐藏账户配置。 | 登录事实要靠事件日志。 |
| [Winlogon\Notify](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon/notify.md) | Winlogon notification package。 | 配置存在不等于 DLL 已加载。 |
| [LSA](../registry-tree/hklm/system/controlset/control/lsa/index.md) | 认证包、通知包、安全包配置。 | 未知 DLL 需验证文件和模块加载。 |
| [ShellServiceObjectDelayLoad](../registry-tree/hklm/software/microsoft/windows/currentversion/shellserviceobjectdelayload.md) | Explorer Shell COM 延迟加载。 | COM CLSID 需回到 Classes 解析。 |
| [App Paths](../registry-tree/hklm/software/microsoft/windows/currentversion/app-paths.md) | 应用程序注册路径。 | 可解释短名称解析和搜索路径，不证明执行。 |
| [AppCompatFlags\Layers](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/appcompatflags/layers.md) | 机器级兼容层配置。 | `RUNASADMIN` 等标记不证明执行。 |
| [Print Monitors](../registry-tree/hklm/system/controlset/control/print-monitors.md) | Spooler monitor DLL 配置。 | 打印机驱动和企业打印组件是常见正常来源。 |

## 判断要点

- 记录 value name、value data、命令行、文件路径、签名、文件是否存在和目录权限。
- 命令指向用户可写目录、临时目录、可移动盘、网络共享或解释器时，需补进程和文件时间线。
- LSA、Print Monitors、AppInit_DLLs、ShellServiceObjectDelayLoad 证明加载链配置存在；是否加载需要运行时证据。
- StartupApproved 只解释启动项状态，完整命令仍要回到 Run key 或 Startup Folder。
- 环境变量和 `Path` 修改只说明执行环境变化；要判断实际劫持或执行需结合进程命令行和文件命中路径。

## 交叉验证

- Autoruns、Scheduled Tasks、Startup Folder、服务二进制、WMI 持久化。
- Sysmon 1 / 6 / 7 / 12 / 13 / 14、Security 4688、System 服务事件。
- Prefetch、BAM / DAM、Amcache、文件签名、EDR telemetry。
- GroupPolicy、软件安装日志、管理员操作记录。

## 常见误判

- 正常更新器、同步盘、输入法、VPN、EDR、备份软件、打印驱动会写入自启动位置。
- `RunOnce` 可能已执行并删除，也可能因权限或错误保留。
- 服务项残留不代表服务当前存在或可启动。
- key LastWrite 只说明 key 变化，不说明某个具体 value 的创建时间。

## 相关场景

- [程序执行痕迹](execution.md)
- [安全策略与防护配置](policy-security.md)
- [常规注册表检查](registry-checklist.md)

## 补充阅读

- [Run / RunOnce artifact](../artifacts/persistence/run-keys.md)
- [Services artifact](../artifacts/persistence/services.md)
- [IFEO artifact](../artifacts/persistence/ifeo.md)
- [LSA Authentication Packages artifact](../artifacts/persistence/lsa-authentication-packages.md)
- [Print Monitors artifact](../artifacts/persistence/print-monitors.md)
