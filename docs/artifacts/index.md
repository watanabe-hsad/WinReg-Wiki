# 注册表 Artifact

这个入口按 registry artifact 类型组织，用于快速定位具体页面。结构化 YAML 生成的完整表格见 [结构化数据索引](generated-index.md)。

## 程序执行 / 程序存在

| Artifact | 分类 | 注册表根键 | 离线 hive | 证据类型 | 取证价值 | 检测价值 |
|---|---|---|---|---|---|---|
| [UserAssist](execution/userassist.md) | 程序执行 / 用户行为 | `HKCU` | `NTUSER.DAT` | Explorer 相关用户交互 | 高 | 中 |
| [BAM / DAM](execution/bam-dam.md) | 程序执行 / 程序存在 | `HKLM` | `SYSTEM` | SID 维度运行线索 | 高 | 中 |
| [Amcache](execution/amcache.md) | 程序元数据 | `HKLM` | `Amcache.hve` | 程序存在 / 文件元数据 | 高 | 中 |
| [ShimCache / AppCompatCache](execution/shimcache.md) | 程序存在 | `HKLM` | `SYSTEM` | 程序路径缓存 | 中 | 中 |
| [MUICache](execution/muicache.md) | 程序存在 / Shell 缓存 | `HKCU` | `UsrClass.dat`, `NTUSER.DAT` | 程序路径和显示名线索 | 中 | 低 |

## 持久化 / 自启动

| Artifact | 分类 | 注册表根键 | 离线 hive | 证据类型 | 取证价值 | 检测价值 |
|---|---|---|---|---|---|---|
| [Run / RunOnce](persistence/run-keys.md) | 持久化 / 自启动 | `HKCU`, `HKLM` | `NTUSER.DAT`, `SOFTWARE` | 登录启动配置 | 高 | 高 |
| [Active Setup](persistence/active-setup.md) | 用户登录初始化 | `HKLM`, `HKCU` | `SOFTWARE`, `NTUSER.DAT` | 每用户初始化命令 | 高 | 高 |
| [StartupApproved](persistence/startupapproved.md) | 自启动状态 | `HKCU`, `HKLM` | `NTUSER.DAT`, `SOFTWARE` | 启动项启用 / 禁用状态 | 中 | 中 |
| [Services](persistence/services.md) | 服务 / 驱动 | `HKLM` | `SYSTEM` | 服务和驱动配置 | 高 | 高 |
| [Drivers](persistence/drivers.md) | 驱动配置 | `HKLM` | `SYSTEM` | kernel / file system driver 配置 | 高 | 高 |
| [IFEO](persistence/ifeo.md) | 进程启动劫持 | `HKLM` | `SOFTWARE` | Debugger / SilentProcessExit 配置 | 高 | 高 |
| [AppInit_DLLs](persistence/appinit-dlls.md) | DLL 加载链 | `HKLM` | `SOFTWARE` | User32 相关 DLL 加载配置 | 高 | 高 |
| [Winlogon Userinit](persistence/winlogon-userinit.md) | 登录链 | `HKLM` | `SOFTWARE` | `Userinit` 登录初始化配置 | 高 | 高 |
| [Winlogon Shell](persistence/winlogon-shell.md) | 登录 Shell | `HKLM`, `HKCU` | `SOFTWARE`, `NTUSER.DAT` | Shell 替换或追加配置 | 高 | 高 |
| [LSA Authentication Packages](persistence/lsa-authentication-packages.md) | LSASS 加载链 | `HKLM` | `SYSTEM` | 认证包配置 | 高 | 高 |
| [LSA Security Packages](persistence/lsa-security-packages.md) | LSASS SSP 加载链 | `HKLM` | `SYSTEM` | 安全支持包配置 | 高 | 高 |
| [Command Processor AutoRun](persistence/command-processor-autorun.md) | 命令解释器启动钩子 | `HKCU`, `HKLM` | `NTUSER.DAT`, `SOFTWARE` | `cmd.exe` AutoRun 配置 | 高 | 高 |
| [ShellServiceObjectDelayLoad](persistence/shellserviceobjectdelayload.md) | Explorer COM 加载 | `HKLM` | `SOFTWARE` | Shell service object 配置 | 高 | 中 |
| [Print Monitors](persistence/print-monitors.md) | Spooler DLL 加载 | `HKLM` | `SYSTEM` | 打印端口监视器 DLL 配置 | 高 | 高 |

## 用户行为

| Artifact | 分类 | 注册表根键 | 离线 hive | 证据类型 | 取证价值 | 检测价值 |
|---|---|---|---|---|---|---|
| [RunMRU](user-activity/runmru.md) | Shell 输入历史 | `HKCU` | `NTUSER.DAT` | Run dialog 输入记录 | 中 | 低 |
| [RecentDocs](user-activity/recentdocs.md) | Shell 最近文档 | `HKCU` | `NTUSER.DAT` | 文件名和 MRU 顺序线索 | 中 | 低 |
| [OpenSavePidlMRU](user-activity/opensavepidlmru.md) | Common Dialog | `HKCU` | `NTUSER.DAT` | 打开 / 保存对话框路径线索 | 高 | 低 |
| [LastVisitedPidlMRU](user-activity/lastvisitedpidlmru.md) | Common Dialog | `HKCU` | `NTUSER.DAT` | 应用程序与目录关系 | 高 | 低 |

## USB / 外接设备

| Artifact | 分类 | 注册表根键 | 离线 hive | 证据类型 | 取证价值 | 检测价值 |
|---|---|---|---|---|---|---|
| [USB](usb/usb.md) | USB 设备枚举 | `HKLM` | `SYSTEM` | USB 总线设备实例 | 高 | 中 |
| [USBSTOR](usb/usbstor.md) | USB 存储设备 | `HKLM` | `SYSTEM` | USB 存储枚举 | 高 | 中 |
| [DeviceClasses](usb/deviceclasses.md) | 设备接口类 | `HKLM` | `SYSTEM` | 设备接口注册 | 中 | 低 |
| [Enum SWD WPDBUSENUM](usb/swd-wpdbusenum.md) | WPD / MTP 设备 | `HKLM` | `SYSTEM` | 便携设备枚举 | 高 | 中 |
| [MountedDevices](usb/mounteddevices.md) | 卷 / 盘符 | `HKLM` | `SYSTEM` | 卷 GUID 和盘符映射 | 高 | 中 |
| [MountPoints2](usb/mountpoints2.md) | 用户可见卷 | `HKCU` | `NTUSER.DAT` | 用户见过的卷或共享 | 高 | 低 |
| [EMDMgmt](usb/emdmgmt.md) | 外接存储元数据 | `HKLM` | `SOFTWARE` | ReadyBoost / 外接存储辅助记录 | 中 | 低 |
| [Portable Devices](usb/portable-devices.md) | WPD 元数据 | `HKLM` | `SOFTWARE` | 便携设备元数据 | 中 | 低 |
| [VolumeInfoCache](usb/volumeinfocache.md) | 卷信息缓存 | `HKLM` | `SOFTWARE` | Windows Search 卷缓存 | 中 | 低 |

## RDP / 远程访问

| Artifact | 分类 | 注册表根键 | 离线 hive | 证据类型 | 取证价值 | 检测价值 |
|---|---|---|---|---|---|---|
| [Terminal Server Client](rdp/terminal-server-client.md) | RDP 客户端 | `HKCU` | `NTUSER.DAT` | MSTSC 目标历史 | 高 | 中 |
| [fDenyTSConnections](rdp/fdenytsconnections.md) | RDP 服务端 | `HKLM` | `SYSTEM` | 远程桌面允许 / 拒绝配置 | 高 | 高 |
| [RDP-Tcp PortNumber](rdp/rdp-tcp-portnumber.md) | RDP 服务端 | `HKLM` | `SYSTEM` | RDP listener 端口 | 高 | 高 |
| [CredSSP / NLA](rdp/credssp-nla.md) | RDP 认证策略 | `HKLM` | `SYSTEM`, `SOFTWARE` | NLA / 安全层配置 | 中 | 高 |

## 账户与安全策略

| Artifact | 分类 | 注册表根键 | 离线 hive | 证据类型 | 取证价值 | 检测价值 |
|---|---|---|---|---|---|---|
| [ProfileList](security/profilelist.md) | 用户 profile 映射 | `HKLM` | `SOFTWARE` | SID 到 profile 路径映射 | 高 | 中 |
| [Defender Policies](security/defender-policies.md) | Defender 策略 | `HKLM` | `SOFTWARE` | 安全控制配置 | 高 | 高 |
| [UAC Policies](security/uac-policies.md) | UAC 策略 | `HKLM` | `SOFTWARE` | 权限提升策略 | 高 | 高 |
| [Firewall Policies](security/firewall-policies.md) | 防火墙策略 | `HKLM` | `SYSTEM`, `SOFTWARE` | 防火墙规则与 profile 配置 | 高 | 高 |
| [Audit Policy](security/audit-policy.md) | 审计策略 | `HKLM` | `SECURITY` | 日志可见性配置 | 高 | 高 |
| [SpecialAccounts\UserList](security/specialaccounts-userlist.md) | 账户可见性 | `HKLM` | `SOFTWARE` | 登录界面用户显示配置 | 高 | 中 |
