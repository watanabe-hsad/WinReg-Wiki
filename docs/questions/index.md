# 按调查场景查

这个入口从真实调查问题出发。每个问题先给高价值注册表 artifact，再提醒必须交叉验证的日志、文件系统和 EDR 证据。

| 调查问题 | 场景页 | 优先查看 | 辅助验证 |
|---|---|---|---|
| 程序是否执行过？ | [程序执行](execution.md) | [UserAssist](../artifacts/execution/userassist.md), [BAM / DAM](../artifacts/execution/bam-dam.md), [Amcache](../artifacts/execution/amcache.md), [ShimCache](../artifacts/execution/shimcache.md), [MUICache](../artifacts/execution/muicache.md) | Prefetch, SRUM, Sysmon, EDR, `$MFT` |
| 用户是否打开过某文件或目录？ | [Shell / Explorer 用户行为](shell-explorer.md) | [UserAssist](../artifacts/execution/userassist.md), [MUICache](../artifacts/execution/muicache.md), [MountPoints2](../artifacts/usb/mountpoints2.md), [RecentDocs](../artifacts/user-activity/recentdocs.md), [OpenSavePidlMRU](../artifacts/user-activity/opensavepidlmru.md), [LastVisitedPidlMRU](../artifacts/user-activity/lastvisitedpidlmru.md) | LNK, Jump Lists, ShellBags, `$UsnJrnl` |
| 是否存在自启动或持久化？ | [自启动与持久化](persistence.md) | [Run / RunOnce](../artifacts/persistence/run-keys.md), [StartupApproved](../artifacts/persistence/startupapproved.md), [Services](../artifacts/persistence/services.md), [Winlogon Userinit](../artifacts/persistence/winlogon-userinit.md), [Winlogon Shell](../artifacts/persistence/winlogon-shell.md), [LSA Authentication Packages](../artifacts/persistence/lsa-authentication-packages.md), [Command Processor AutoRun](../artifacts/persistence/command-processor-autorun.md), [IFEO](../artifacts/persistence/ifeo.md) | Autoruns, Scheduled Tasks, Startup Folder, Sysmon 12/13/14 |
| 是否插入过 USB / 外接存储？ | [USB 与外接设备](usb.md) | [USBSTOR](../artifacts/usb/usbstor.md), [MountedDevices](../artifacts/usb/mounteddevices.md), [MountPoints2](../artifacts/usb/mountpoints2.md) | SetupAPI.dev.log, Partition/Diagnostic, LNK, Jump Lists |
| 是否发生 RDP / 远程访问？ | [RDP 与远程访问](rdp.md) | [Terminal Server Client](../artifacts/rdp/terminal-server-client.md), [fDenyTSConnections](../artifacts/rdp/fdenytsconnections.md), [RDP-Tcp PortNumber](../artifacts/rdp/rdp-tcp-portnumber.md), [CredSSP / NLA](../artifacts/rdp/credssp-nla.md) | Security.evtx, TerminalServices logs, firewall logs |
| 是否存在账户新增、隐藏账户、权限异常？ | [账户与安全](accounts-security.md) | [ProfileList](../artifacts/security/profilelist.md), `SAM\Domains\Account\Users`, [SpecialAccounts\UserList](../artifacts/security/specialaccounts-userlist.md), [LSA Authentication Packages](../artifacts/persistence/lsa-authentication-packages.md) | Security 4720/4732/4672, SAM, local groups, domain logs |
| 是否修改过安全策略、UAC、Defender、防火墙？ | [安全策略与防护配置](policy-security.md) | [Defender Policies](../artifacts/security/defender-policies.md), [UAC Policies](../artifacts/security/uac-policies.md), [Audit Policy](../artifacts/security/audit-policy.md), [Firewall Policies](../artifacts/security/firewall-policies.md), [LSA Authentication Packages](../artifacts/persistence/lsa-authentication-packages.md) | Defender logs, GroupPolicy, MDM, Sysmon 13 |
| 是否存在代理、DNS、网络配置异常？ | [网络与系统环境](network.md) | `NetworkList\Profiles`, `Tcpip\Parameters`, `Interfaces`, `NameServer`, `Internet Settings`, `ProxyServer` | DNS logs, DHCP logs, firewall, NetFlow, EDR network |
| 是否安装或卸载过软件？ | [软件安装与卸载](software-install.md) | `Uninstall`, [Amcache](../artifacts/execution/amcache.md), [MUICache](../artifacts/execution/muicache.md), [UserAssist](../artifacts/execution/userassist.md) | MSI logs, Program Files, Prefetch, ShimCache |
| 是否有反取证、清理痕迹或日志策略修改？ | [反取证与清理痕迹](anti-forensics.md) | [Defender Policies](../artifacts/security/defender-policies.md), `EventLog`, Audit Policy, [StartupApproved](../artifacts/persistence/startupapproved.md) | Event log gaps, 1102, PowerShell logs, EDR tamper events |
| 是否存在 Shell / Explorer 相关用户行为痕迹？ | [Shell / Explorer 用户行为](shell-explorer.md) | [UserAssist](../artifacts/execution/userassist.md), [MUICache](../artifacts/execution/muicache.md), [MountPoints2](../artifacts/usb/mountpoints2.md), [RunMRU](../artifacts/user-activity/runmru.md), [RecentDocs](../artifacts/user-activity/recentdocs.md) | LNK, Jump Lists, ShellBags, file dialogs |

## 调查流程建议

1. 先把问题写成证据语义：配置存在、程序存在、用户交互、程序执行、设备连接、策略削弱。
2. 再查对应 artifact，并记录 hive 文件、SID、ControlSet、工具版本和时区。
3. 然后用日志、文件系统时间线、EDR 和其他 artifact 交叉验证。
4. 最后把结论写成“能证明什么 / 不能证明什么”，不要把弱线索写成定案。
