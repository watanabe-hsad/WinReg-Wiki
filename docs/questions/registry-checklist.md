<section class="ww-page-header" markdown>
<p class="ww-hero-eyebrow">Registry Checklist</p>
<h1>第一次检查注册表时看哪里</h1>
<p>按主题扫关键路径。每一项只说明检查目标、注册表位置、关注字段和交叉验证来源。</p>
</section>

## 启动与持久化

| 检查项 | 注册表路径 | 关注字段 | 交叉验证 |
|---|---|---|---|
| 机器级登录启动 | [HKLM Run / RunOnce](../registry-tree/hklm/software/microsoft/windows/currentversion/run.md) | `value name`、`value data`、`WOW6432Node` | 登录事件、进程创建、Prefetch、BAM / DAM、EDR |
| 用户级登录启动 | [HKCU Run / RunOnce](../registry-tree/hkcu/software/microsoft/windows/currentversion/run.md) | `value name`、`value data`、用户 SID | 用户登录事件、StartupApproved、Prefetch、EDR |
| 服务和驱动 | [Services](../registry-tree/hklm/system/controlset/services/index.md) | `ImagePath`、`Type`、`Start`、`ObjectName` | System.evtx、Service Control Manager、Autoruns、签名 |
| 登录链 | [Winlogon](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | `Userinit`、`Shell`、`AutoAdminLogon`、`Notify` | Security.evtx、SAM、ProfileList、Autoruns |
| Session Manager | [BootExecute](../registry-tree/hklm/system/controlset/control/session-manager/bootexecute.md) / [AppCertDlls](../registry-tree/hklm/system/controlset/control/session-manager/appcertdlls.md) / [SubSystems](../registry-tree/hklm/system/controlset/control/session-manager/subsystems.md) | 启动项、DLL 路径、`Windows` 子系统参数 | 重启时间线、模块加载、同版本基线 |
| 文件删除队列 | [PendingFileRenameOperations](../registry-tree/hklm/system/controlset/control/session-manager/pending-file-rename-operations.md) | 待重命名 / 删除路径 | 重启记录、文件系统时间线、`$UsnJrnl` |

## 程序执行

| 检查项 | 注册表路径 | 关注字段 | 交叉验证 |
|---|---|---|---|
| Explorer 交互 | [UserAssist](../registry-tree/hkcu/software/microsoft/windows/currentversion/userassist.md) | ROT13 条目、计数、时间字段 | Prefetch、Amcache、BAM / DAM、LNK、EDR |
| 应用路径注册 | [App Paths](../registry-tree/hklm/software/microsoft/windows/currentversion/app-paths.md) | 可执行文件名、默认路径、`Path` | 文件系统、安装记录、进程创建 |
| 命令处理器 | [HKCU Command Processor](../registry-tree/hkcu/software/microsoft/command-processor.md) / [HKLM Command Processor](../registry-tree/hklm/software/microsoft/command-processor.md) | `AutoRun`、扩展、补全配置 | 进程创建、命令行日志、PowerShell / Sysmon |
| IFEO | [Image File Execution Options](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/ifeo.md) | `Debugger`、SilentProcessExit 相关值 | 进程创建、调试器路径、开发工具和 EDR 基线 |

## 用户行为

| 检查项 | 注册表路径 | 关注字段 | 交叉验证 |
|---|---|---|---|
| 运行框输入 | [RunMRU](../registry-tree/hkcu/software/microsoft/windows/currentversion/runmru.md) | `MRUList`、命令字符串 | 进程创建、Shell 事件、用户上下文 |
| 最近文档 | [RecentDocs](../registry-tree/hkcu/software/microsoft/windows/currentversion/recentdocs.md) | MRU 顺序、文件名 | LNK、Jump Lists、文件系统 |
| 文件对话框 | [ComDlg32](../registry-tree/hkcu/software/microsoft/windows/currentversion/comdlg32.md) | OpenSavePidlMRU、LastVisitedPidlMRU | LNK、Jump Lists、ShellBags |
| 用户级策略 | [HKCU Policies](../registry-tree/hkcu/software/microsoft/windows/currentversion/policies.md) / [Explorer Policies](../registry-tree/hkcu/software/microsoft/windows/currentversion/policies/explorer.md) | Explorer 限制、驱动器显示、控制面板限制 | GPO / MDM、用户 SID、Shell 行为 |

## USB / 设备

| 检查项 | 注册表路径 | 关注字段 | 交叉验证 |
|---|---|---|---|
| USB 存储 | [USBSTOR](../registry-tree/hklm/system/controlset/enum/usbstor.md) | 设备类型、厂商、产品、实例 ID、`FriendlyName` | SetupAPI.dev.log、Partition/Diagnostic、LNK、Jump Lists |
| USB 总线 | [USB](../registry-tree/hklm/system/controlset/enum/usb.md) | VID/PID、实例 ID、ContainerID | USBSTOR、DeviceClasses、SetupAPI.dev.log |
| 卷和盘符 | [MountedDevices](../registry-tree/hklm/system/mounteddevices.md) | `\DosDevices\<letter>:`、`\??\Volume{GUID}` | USBSTOR、MountPoints2、卷 GUID、文件系统 |
| 用户见过的卷 | [MountPoints2](../registry-tree/hkcu/software/microsoft/windows/currentversion/mountpoints2.md) | Volume GUID、网络共享、用户 SID | LNK、Jump Lists、ShellBags、文件访问记录 |

## RDP / 远程访问

| 检查项 | 注册表路径 | 关注字段 | 交叉验证 |
|---|---|---|---|
| RDP 服务端开关 | [Terminal Server](../registry-tree/hklm/system/controlset/control/terminal-server.md) | `fDenyTSConnections` | TerminalServices 日志、防火墙、监听端口 |
| RDP listener | [RDP-Tcp](../registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp.md) | `PortNumber`、NLA、安全层 | TerminalServices、Security.evtx、端口监听 |
| CredSSP | [CredSSP](../registry-tree/hklm/system/controlset/control/terminal-server/credssp.md) | NLA / 认证兼容性策略 | 组策略、连接事件、客户端配置 |
| RDP 客户端 | [Terminal Server Client](../registry-tree/hkcu/software/microsoft/terminal-server-client.md) | `Servers`、`Default`、MRU 项 | Jump Lists、LNK、RDP 缓存、用户上下文 |

## 账户 / 登录

| 检查项 | 注册表路径 | 关注字段 | 交叉验证 |
|---|---|---|---|
| 用户映射 | [ProfileList](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist.md) | SID、`ProfileImagePath`、`.bak`、`State` | SAM、域账户、Security.evtx、用户目录 |
| 当前用户 hive | [HKEY_USERS](../registry-tree/hku/index.md) / [NTUSER.DAT](../registry-tree/hku/ntuser.md) | SID、加载状态、用户 hive 文件 | ProfileList、用户目录、登录事件 |
| 登录界面 | [LogonUI](../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/logonui.md) | 最近用户 / SID 显示线索 | Security.evtx、ProfileList、域日志 |
| 凭据组件 | [Credential Providers](../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/credential-providers.md) / [Credential Provider Filters](../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/credential-provider-filters.md) | Provider / Filter CLSID | 安装软件、签名、LogonUI、EDR |

## 安全策略

| 检查项 | 注册表路径 | 关注字段 | 交叉验证 |
|---|---|---|---|
| Defender 策略 | [Defender Policies](../registry-tree/hklm/software/policies/microsoft/windows-defender.md) | `Disable*`、排除项、实时防护相关值 | Defender Operational、Tamper Protection、GPO / MDM |
| 防火墙配置 | [FirewallPolicy](../registry-tree/hklm/system/controlset/services/sharedaccess/firewallpolicy.md) / [WindowsFirewall Policies](../registry-tree/hklm/software/policies/microsoft/windowsfirewall.md) | profile、规则、默认入站 / 出站动作 | Firewall 日志、ActiveStore、GPO / MDM、网络流量 |
| 事件日志配置 | [EventLog](../registry-tree/hklm/system/controlset/services/eventlog.md) | `File`、`MaxSize`、`Retention`、`AutoBackupLogFiles` | 实际 `.evtx` 文件、EventLog 服务、日志截断线索 |
| LSA | [LSA](../registry-tree/hklm/system/controlset/control/lsa/index.md) | 认证包、安全包、LSASS 保护相关值 | LSASS 模块、签名、Security.evtx、EDR |

## 网络

| 检查项 | 注册表路径 | 关注字段 | 交叉验证 |
|---|---|---|---|
| 网络接口 | [Tcpip Interfaces](../registry-tree/hklm/system/controlset/services/tcpip/parameters/interfaces.md) | `EnableDHCP`、IP、DNS、网关、租约时间 | NetworkList、DHCP / DNS 日志、防火墙、EDR 网络 |
| 网络配置文件 | [NetworkList Profiles](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/networklist/profiles.md) | `ProfileName`、`Category`、`DateCreated`、`DateLastConnected` | WLAN / DHCP 日志、网络连接时间线 |
| 代理配置 | [Internet Settings](../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings.md) | `ProxyEnable`、`ProxyServer`、`AutoConfigURL` | 浏览器设置、WinINet 程序、代理日志、EDR 网络 |
| 安全区域 | [ZoneMap](../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings/zonemap.md) | `Domains`、`Ranges`、区域编号 | 浏览器策略、GPO / MDM、访问日志 |

## 常见误判

- Run key、Services、Winlogon、LSA 只能先证明配置存在；是否执行或加载要另证。
- `USBSTOR`、`MountedDevices`、`MountPoints2` 分别回答不同层面的问题，不能互相替代。
- Defender、Firewall、Audit Policy 注册表值可能来自 GPO、MDM、安全产品或本地管理操作。
- key LastWrite 是 key 级变化时间，不是某个 value 的独立创建时间。
