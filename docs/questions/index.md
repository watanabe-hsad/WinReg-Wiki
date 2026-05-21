# 取证场景

这个入口按调查问题组织。主路径是“场景 -> 注册表位置”：先看相关 key / value 是什么，再用日志、文件系统和工具输出交叉验证。

| 调查问题 | 场景页 | 优先查看的注册表位置 | 辅助验证 |
|---|---|---|---|
| 常规排查先看哪些注册表位置？ | [常规注册表检查](registry-checklist.md) | Run Keys, Services, Winlogon, IFEO, LSA, Terminal Server, USB, ProfileList, Explorer MRU | 事件日志、EDR、文件系统时间线 |
| 程序是否执行过？ | [程序执行](execution.md) | [UserAssist](../registry-tree/hkcu/software/microsoft/windows/currentversion/userassist.md), [Services\bam](../registry-tree/hklm/system/controlset/services/index.md), [Uninstall](../registry-tree/hklm/software/microsoft/windows/currentversion/uninstall.md), [Drivers](../registry-tree/hklm/system/controlset/services/drivers.md) | Prefetch, SRUM, Amcache, ShimCache, Sysmon, EDR |
| 用户是否打开过某文件或目录？ | [Shell / Explorer 用户行为](shell-explorer.md) | [Explorer](../registry-tree/hkcu/software/microsoft/windows/currentversion/explorer.md), [RunMRU](../registry-tree/hkcu/software/microsoft/windows/currentversion/runmru.md), [RecentDocs](../registry-tree/hkcu/software/microsoft/windows/currentversion/recentdocs.md), [ComDlg32](../registry-tree/hkcu/software/microsoft/windows/currentversion/comdlg32.md), [MountPoints2](../registry-tree/hkcu/software/microsoft/windows/currentversion/mountpoints2.md) | LNK, Jump Lists, ShellBags, `$UsnJrnl` |
| 是否存在自启动或持久化？ | [自启动与持久化](persistence.md) | [HKCU Run](../registry-tree/hkcu/software/microsoft/windows/currentversion/run.md), [HKLM Run](../registry-tree/hklm/software/microsoft/windows/currentversion/run.md), [Services](../registry-tree/hklm/system/controlset/services/index.md), [Winlogon](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md), [IFEO](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/ifeo.md), [LSA](../registry-tree/hklm/system/controlset/control/lsa/index.md) | Autoruns, Scheduled Tasks, Startup Folder, Sysmon 12/13/14 |
| 是否插入过 USB / 外接存储？ | [USB 与外接设备](usb.md) | [USBSTOR](../registry-tree/hklm/system/controlset/enum/usbstor.md), [USB](../registry-tree/hklm/system/controlset/enum/usb.md), [SWD\WPDBUSENUM](../registry-tree/hklm/system/controlset/enum/swd-wpdbusenum.md), [MountedDevices](../registry-tree/hklm/system/mounteddevices.md), [MountPoints2](../registry-tree/hkcu/software/microsoft/windows/currentversion/mountpoints2.md) | SetupAPI.dev.log, Partition/Diagnostic, LNK, Jump Lists |
| 是否发生 RDP / 远程访问？ | [RDP 与远程访问](rdp.md) | [Terminal Server Client](../registry-tree/hkcu/software/microsoft/terminal-server-client.md), [Terminal Server](../registry-tree/hklm/system/controlset/control/terminal-server.md), [Firewall / Policies](../registry-tree/hklm/software/policies.md) | Security.evtx, TerminalServices logs, firewall logs |
| 是否存在账户新增、隐藏账户、权限异常？ | [账户与安全](accounts-security.md) | [ProfileList](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist.md), [SAM](../registry-tree/hklm/sam.md), [HKEY_USERS](../registry-tree/hku/index.md), [Winlogon SpecialAccounts](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md), [LSA](../registry-tree/hklm/system/controlset/control/lsa/index.md) | Security 4720/4732/4672, SAM, local groups, domain logs |
| 是否修改过安全策略、UAC、Defender、防火墙？ | [安全策略与防护配置](policy-security.md) | [Policies](../registry-tree/hklm/software/policies.md), [Windows Defender](../registry-tree/hklm/software/microsoft/windows-defender.md), [LSA](../registry-tree/hklm/system/controlset/control/lsa/index.md), [SECURITY](../registry-tree/hklm/security.md), [Drivers](../registry-tree/hklm/system/controlset/services/drivers.md) | Defender logs, GroupPolicy, MDM, Sysmon 13 |
| 是否存在代理、DNS、网络配置异常？ | [网络与系统环境](network.md) | [Tcpip](../registry-tree/hklm/system/controlset/services/tcpip.md), [Internet Settings](../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings.md), [ComputerName](../registry-tree/hklm/system/controlset/control/computername.md), [TimeZoneInformation](../registry-tree/hklm/system/controlset/control/timezone.md) | DNS logs, DHCP logs, firewall, NetFlow, EDR network |
| 是否安装或卸载过软件？ | [软件安装与卸载](software-install.md) | [Uninstall](../registry-tree/hklm/software/microsoft/windows/currentversion/uninstall.md), [HKLM\SOFTWARE](../registry-tree/hklm/software/index.md), [UserAssist](../registry-tree/hkcu/software/microsoft/windows/currentversion/userassist.md), [Run Keys](../registry-tree/hklm/software/microsoft/windows/currentversion/run.md) | MSI logs, Program Files, Prefetch, ShimCache |
| 是否有反取证、清理痕迹或日志策略修改？ | [反取证与清理痕迹](anti-forensics.md) | [Policies](../registry-tree/hklm/software/policies.md), [Windows Defender](../registry-tree/hklm/software/microsoft/windows-defender.md), [SECURITY](../registry-tree/hklm/security.md), [Services](../registry-tree/hklm/system/controlset/services/index.md) | Event log gaps, 1102, PowerShell logs, EDR tamper events |

## 补充索引

| 入口 | 内容 |
|---|---|
| [Artifact 补充索引](../artifacts/index.md) | 保留 artifact 级证据语义、采集、误报和工具说明；不是主要阅读入口。 |
| [结构化数据索引](../artifacts/generated-index.md) | 从 `data/artifacts/*.yml` 生成的内部数据表格。 |
| [检测工程](../detection/index.md) | 注册表检测规则的路径组合、误报和验证思路。 |

## 判断顺序

1. 先确认路径归属：root key、hive、SID、ControlSet、32/64 位视图。
2. 再解释证据语义：配置存在、设备枚举、用户交互、程序存在或策略值存在。
3. 然后用日志、文件系统、工具输出和时间线交叉验证。
4. 最后写清楚“能证明什么 / 不能证明什么”，避免把弱线索写成定案。
