# 常规注册表检查

## 检查目标

在常规排查中快速定位注册表中的自启动、服务、登录链、远程访问、设备、账户和安全策略线索。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 注意 |
|---|---|---|
| [HKCU Run / RunOnce](../registry-tree/hkcu/software/microsoft/windows/currentversion/run.md) | 用户级登录启动项。 | 配置存在不等于执行成功。 |
| [HKLM Run / RunOnce](../registry-tree/hklm/software/microsoft/windows/currentversion/run.md) | 机器级登录启动项。 | 64 位系统还要看 `WOW6432Node`。 |
| [HKCU Environment](../registry-tree/hkcu/environment.md) | 用户级环境变量。 | 已启动进程可能保留旧环境。 |
| [HKLM Environment](../registry-tree/hklm/system/controlset/control/session-manager/environment.md) | 系统级环境变量。 | `Path` 变化不等于命令已执行。 |
| [Command Processor](../registry-tree/hkcu/software/microsoft/command-processor.md) | 用户级 `cmd.exe` 配置和 `AutoRun`。 | `AutoRun` 存在不等于 `cmd.exe` 已启动。 |
| [HKLM Command Processor](../registry-tree/hklm/software/microsoft/command-processor.md) | 机器级 `cmd.exe` 配置和 `AutoRun`。 | 影响范围更大，但仍需进程证据。 |
| [App Paths](../registry-tree/hklm/software/microsoft/windows/currentversion/app-paths.md) | 应用程序注册路径。 | 程序注册不等于执行。 |
| [Services](../registry-tree/hklm/system/controlset/services/index.md) | 服务、驱动、网络组件配置。 | 服务配置存在不等于服务已启动。 |
| [EventLog](../registry-tree/hklm/system/controlset/services/eventlog.md) | 事件日志通道配置。 | 这里不是日志内容。 |
| [Drivers](../registry-tree/hklm/system/controlset/services/drivers.md) | kernel / file system driver 启动配置。 | 需结合驱动加载、签名和 Code Integrity。 |
| [Winlogon](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | `Userinit`、`Shell`、自动登录和隐藏账户相关配置。 | 登录事实要回到 Security.evtx。 |
| [IFEO](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/ifeo.md) | `Debugger`、SilentProcessExit 等进程启动相关配置。 | 正常调试器、开发工具和 EDR 也可能写入。 |
| [LSA](../registry-tree/hklm/system/controlset/control/lsa/index.md) | 认证包、安全包和 LSASS 保护相关配置。 | 未知 DLL 需验证路径、签名和模块加载。 |
| [BootExecute](../registry-tree/hklm/system/controlset/control/session-manager/bootexecute.md) | 启动早期执行项。 | 配置存在不等于已经重启执行。 |
| [KnownDLLs](../registry-tree/hklm/system/controlset/control/session-manager/knowndlls.md) | Known DLL 映射。 | 异常需结合模块加载和基线。 |
| [PendingFileRenameOperations](../registry-tree/hklm/system/controlset/control/session-manager/pending-file-rename-operations.md) | 重启后待处理文件操作。 | 队列存在不等于文件已删除。 |
| [Terminal Server](../registry-tree/hklm/system/controlset/control/terminal-server.md) | RDP 服务端开关、端口和 NLA。 | 允许连接不等于发生登录。 |
| [Terminal Server Client](../registry-tree/hkcu/software/microsoft/terminal-server-client.md) | MSTSC 客户端目标历史。 | 这是客户端侧记录。 |
| [Policies](../registry-tree/hklm/software/policies.md) | GPO / MDM / 本地策略写入位置。 | 注册表值不直接说明策略来源。 |
| [Windows Defender](../registry-tree/hklm/software/microsoft/windows-defender.md) | Defender 本地配置和排除项线索。 | 需结合 Tamper Protection 和 Defender 日志。 |
| [Defender Policies](../registry-tree/hklm/software/policies/microsoft/windows-defender.md) | Defender 策略位置。 | 策略值不等于实际防护状态。 |
| [FirewallPolicy](../registry-tree/hklm/system/controlset/services/sharedaccess/firewallpolicy.md) | Windows Defender Firewall 本地 profile 和规则配置。 | 规则存在不等于连接发生。 |
| [WindowsFirewall Policies](../registry-tree/hklm/software/policies/microsoft/windowsfirewall.md) | Windows Firewall 策略配置。 | 策略值不等于 ActiveStore 状态。 |
| [USBSTOR](../registry-tree/hklm/system/controlset/enum/usbstor.md) | USB 存储设备枚举。 | 不证明文件复制。 |
| [USB](../registry-tree/hklm/system/controlset/enum/usb.md) | USB 总线设备枚举。 | 可覆盖非存储 USB 设备。 |
| [MountedDevices](../registry-tree/hklm/system/mounteddevices.md) | 卷 GUID、盘符和设备映射。 | 盘符可复用。 |
| [MountPoints2](../registry-tree/hkcu/software/microsoft/windows/currentversion/mountpoints2.md) | 用户见过的卷或网络共享。 | 归属到用户，不直接证明访问文件。 |
| [ProfileList](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist.md) | SID 到用户 profile 的映射。 | 多用户分析先做 SID 映射。 |
| [UserAssist](../registry-tree/hkcu/software/microsoft/windows/currentversion/userassist.md) | Explorer 相关程序交互线索。 | 不覆盖所有执行方式。 |
| [RunMRU](../registry-tree/hkcu/software/microsoft/windows/currentversion/runmru.md) | Win+R 输入历史。 | 输入不等于执行成功。 |
| [RecentDocs](../registry-tree/hkcu/software/microsoft/windows/currentversion/recentdocs.md) | 最近文档名称和 MRU 顺序。 | 文件名出现不等于内容被读取。 |
| [Internet Settings](../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings.md) | 用户级 WinINet 代理 / PAC。 | 不代表所有程序都使用该代理。 |
| [ZoneMap](../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings/zonemap.md) | URL 安全区域映射。 | 映射存在不等于访问发生。 |
| [NetworkList Profiles](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/networklist/profiles.md) | 网络配置文件。 | 时间字段需工具解析。 |
| [Tcpip Interfaces](../registry-tree/hklm/system/controlset/services/tcpip/parameters/interfaces.md) | 接口 IP、DNS、DHCP、网关。 | DHCP 字段和静态字段要分开。 |
| [HKCU Printers](../registry-tree/hkcu/printers.md) | 用户级打印机连接和配置。 | 不证明打印过文件。 |

## 判断要点

- 先解析 `HKLM\SYSTEM\Select`，确认离线分析时的当前控制集。
- 先用 `ProfileList` 建立 SID 到用户目录映射，再解释 `HKCU` / `HKU\<SID>` 下的用户线索。
- 对自启动项记录 value name、value data、路径是否存在、签名、目录权限和写入时间线。
- 对 USB 线索区分设备枚举、卷映射、用户见过卷和文件访问证据。
- 对策略线索区分注册表值、策略来源和实际生效状态。
- 对网络线索区分代理配置、DNS / DHCP 配置、网络 profile 和真实网络连接。

## 交叉验证

- 事件日志：Security.evtx、System.evtx、TerminalServices、GroupPolicy、Defender Operational、DriverFrameworks、Partition/Diagnostic。
- 程序执行：Prefetch、Amcache、ShimCache、BAM / DAM、SRUM、Sysmon、EDR。
- 文件系统：`$MFT`、`$UsnJrnl`、LNK、Jump Lists、ShellBags、下载目录、程序文件目录。
- 工具：Autoruns、Registry Explorer、RECmd、KAPE、Velociraptor、Eric Zimmerman 工具集。

## 常见误判

- Run key、Services、Winlogon、LSA 只能先证明配置存在；是否执行或加载要另证。
- `USBSTOR`、`MountedDevices`、`MountPoints2` 分别回答不同层面的问题，不能互相替代。
- Defender、Firewall、Audit Policy 注册表值可能来自 GPO、MDM、安全产品或本地管理操作。
- key LastWrite 是 key 级变化时间，不是某个 value 的独立创建时间。

## 相关场景

- [程序执行痕迹](execution.md)
- [自启动与持久化](persistence.md)
- [USB 与外接设备](usb.md)
- [RDP 与远程访问](rdp.md)
- [账户与安全](accounts-security.md)
- [安全策略与防护配置](policy-security.md)
- [网络与系统环境](network.md)
