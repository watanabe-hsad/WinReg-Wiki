# 常规注册表检查

## 检查目标

第一次检查注册表时，快速定位自启动、服务、登录链、远程访问、设备、账户、策略和网络配置线索。

## 核心清单

| 检查目标 | 注册表位置 | 关注字段 | 交叉验证 |
|---|---|---|---|
| 当前控制集 | [HKLM\SYSTEM\Select](../registry-tree/hklm/system/select.md) | `Current`、`Default`、`Failed`、`LastKnownGood` | `SYSTEM` hive、启动日志、多个 `ControlSet00x` 差异 |
| 控制集主体 | [HKLM\SYSTEM\ControlSet00x](../registry-tree/hklm/system/controlset/index.md) | `Control`、`Enum`、`Services` | `Select\Current`、系统版本、驱动和服务基线 |
| 机器级登录启动 | [HKLM Run / RunOnce](../registry-tree/hklm/software/microsoft/windows/currentversion/run.md) | value name、value data、`WOW6432Node` | 登录事件、进程创建、Prefetch、BAM / DAM、EDR |
| 用户级登录启动 | [HKCU Run / RunOnce](../registry-tree/hkcu/software/microsoft/windows/currentversion/run.md) | value name、value data、用户 SID | 用户登录事件、StartupApproved、Prefetch、EDR |
| 服务和驱动 | [Services](../registry-tree/hklm/system/controlset/services/index.md) | `ImagePath`、`Type`、`Start`、`ObjectName` | System.evtx、Service Control Manager、Autoruns、签名和路径 |
| 驱动项 | [Drivers](../registry-tree/hklm/system/controlset/services/drivers.md) | `Type`、`Start`、`ImagePath` | Code Integrity、驱动文件、签名、EDR |
| 登录链 | [Winlogon](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | `Userinit`、`Shell`、`AutoAdminLogon`、`Notify` | Security.evtx、SAM、ProfileList、Autoruns |
| 凭据提供器 | [Credential Providers](../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/credential-providers.md) | Provider CLSID、注册路径 | LogonUI、安装软件、签名、EDR |
| 凭据过滤器 | [Credential Provider Filters](../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/credential-provider-filters.md) | Filter CLSID、注册路径 | LogonUI、身份组件、签名和安装记录 |
| IFEO | [Image File Execution Options](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/ifeo.md) | `Debugger`、SilentProcessExit 相关值 | 进程创建、调试器路径、开发工具和 EDR 基线 |
| Session Manager 执行链 | [BootExecute](../registry-tree/hklm/system/controlset/control/session-manager/bootexecute.md) / [AppCertDlls](../registry-tree/hklm/system/controlset/control/session-manager/appcertdlls.md) / [SubSystems](../registry-tree/hklm/system/controlset/control/session-manager/subsystems.md) | 启动项、DLL 路径、`Windows` 子系统参数 | 重启时间线、模块加载、同版本基线 |
| 文件删除队列 | [PendingFileRenameOperations](../registry-tree/hklm/system/controlset/control/session-manager/pending-file-rename-operations.md) | 待重命名 / 删除路径 | 重启记录、文件系统时间线、`$UsnJrnl` |
| RDP 服务端 | [Terminal Server](../registry-tree/hklm/system/controlset/control/terminal-server.md) / [RDP-Tcp](../registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp.md) | `fDenyTSConnections`、`PortNumber`、NLA 相关值 | TerminalServices 日志、防火墙、监听端口、Security.evtx |
| RDP 客户端 | [Terminal Server Client](../registry-tree/hkcu/software/microsoft/terminal-server-client.md) | `Servers`、`Default`、MRU 项 | Jump Lists、LNK、RDP 缓存、用户登录上下文 |
| LSA | [LSA](../registry-tree/hklm/system/controlset/control/lsa/index.md) | 认证包、安全包、LSASS 保护相关值 | LSASS 模块、签名、Security.evtx、EDR |
| Defender 策略 | [Defender Policies](../registry-tree/hklm/software/policies/microsoft/windows-defender.md) | `Disable*`、排除项、实时防护相关值 | Defender Operational、Tamper Protection、GPO / MDM |
| 防火墙配置 | [FirewallPolicy](../registry-tree/hklm/system/controlset/services/sharedaccess/firewallpolicy.md) / [WindowsFirewall Policies](../registry-tree/hklm/software/policies/microsoft/windowsfirewall.md) | profile、规则、默认入站 / 出站动作 | Firewall 日志、ActiveStore、GPO / MDM、网络流量 |
| 事件日志配置 | [EventLog](../registry-tree/hklm/system/controlset/services/eventlog.md) | `File`、`MaxSize`、`Retention`、`AutoBackupLogFiles` | 实际 `.evtx` 文件、EventLog 服务、日志截断线索 |
| USB 存储 | [USBSTOR](../registry-tree/hklm/system/controlset/enum/usbstor.md) | 设备类型、厂商、产品、实例 ID、`FriendlyName` | SetupAPI.dev.log、Partition/Diagnostic、LNK、Jump Lists |
| 卷和盘符 | [MountedDevices](../registry-tree/hklm/system/mounteddevices.md) | `\DosDevices\<letter>:`、`\??\Volume{GUID}` | USBSTOR、MountPoints2、卷 GUID、文件系统 |
| 用户见过的卷 | [MountPoints2](../registry-tree/hkcu/software/microsoft/windows/currentversion/mountpoints2.md) | Volume GUID、网络共享、用户 SID | LNK、Jump Lists、ShellBags、文件访问记录 |
| 用户映射 | [ProfileList](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist.md) | SID、`ProfileImagePath`、`.bak`、`State` | SAM、域账户、Security.evtx、用户目录 |
| 用户交互 | [UserAssist](../registry-tree/hkcu/software/microsoft/windows/currentversion/userassist.md) | ROT13 条目、计数、时间字段 | Prefetch、Amcache、BAM / DAM、LNK、EDR |
| Shell 历史 | [RunMRU](../registry-tree/hkcu/software/microsoft/windows/currentversion/runmru.md) / [RecentDocs](../registry-tree/hkcu/software/microsoft/windows/currentversion/recentdocs.md) / [ComDlg32](../registry-tree/hkcu/software/microsoft/windows/currentversion/comdlg32.md) | MRUList、文件名、路径片段 | LNK、Jump Lists、ShellBags、文件系统 |
| 代理和区域 | [Internet Settings](../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings.md) / [ZoneMap](../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings/zonemap.md) | `ProxyEnable`、`ProxyServer`、`AutoConfigURL`、区域编号 | 浏览器设置、WinINet 程序、代理日志、EDR 网络 |
| 网络接口 | [Tcpip Interfaces](../registry-tree/hklm/system/controlset/services/tcpip/parameters/interfaces.md) | `EnableDHCP`、IP、DNS、网关、租约时间 | NetworkList、DHCP / DNS 日志、防火墙、EDR 网络 |
| 网络配置文件 | [NetworkList Profiles](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/networklist/profiles.md) | `ProfileName`、`Category`、`DateCreated`、`DateLastConnected` | WLAN / DHCP 日志、网络连接时间线 |
| 用户策略 | [HKCU Policies](../registry-tree/hkcu/software/microsoft/windows/currentversion/policies.md) / [Explorer Policies](../registry-tree/hkcu/software/microsoft/windows/currentversion/policies/explorer.md) | Explorer 限制、控制面板、驱动器显示相关值 | GPO / MDM、用户 SID、Shell 行为 |
| 打印配置 | [HKCU Printers](../registry-tree/hkcu/printers.md) | `Connections`、`DevModePerUser`、`Settings` | 打印事件、Spool 文件、文档文件系统记录 |

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
- [反取证与清理痕迹](anti-forensics.md)
