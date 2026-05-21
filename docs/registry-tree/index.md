# 注册表位置

按 Windows 原生注册表树组织。这个入口只做路径、hive 来源和 key / value 含义速查。

## 根键

| 根键 | 内容 | 离线来源 |
|---|---|---|
| [HKEY_CLASSES_ROOT](hkcr/index.md) | 文件关联、COM、协议处理器的合并视图。 | `SOFTWARE\Classes` + 用户 `UsrClass.dat` |
| [HKEY_CURRENT_USER](hkcu/index.md) | 当前用户配置，映射到 `HKEY_USERS\<SID>`。 | 用户 `NTUSER.DAT`，部分内容来自 `UsrClass.dat` |
| [HKEY_LOCAL_MACHINE](hklm/index.md) | 机器级配置和系统数据库。 | `SAM`、`SECURITY`、`SOFTWARE`、`SYSTEM`、`BCD` |
| [HKEY_USERS](hku/index.md) | 已加载用户 hive、服务账户 hive 和默认账户 hive。 | `DEFAULT`、用户 `NTUSER.DAT` / `UsrClass.dat` |
| [HKEY_CURRENT_CONFIG](hkcc/index.md) | 当前硬件配置映射。 | `SYSTEM` 中的 Hardware Profiles |

## HKEY_LOCAL_MACHINE

| 路径 | 内容 |
|---|---|
| [HKLM\SAM](hklm/sam.md) | 本地账户和组数据库。 |
| [HKLM\SECURITY](hklm/security.md) | LSA、审计策略、安全策略。 |
| [HKLM\SOFTWARE](hklm/software/index.md) | 软件、策略、ProfileList、Winlogon、Defender、Classes。 |
| [HKLM\SYSTEM](hklm/system/index.md) | ControlSet、服务、驱动、设备、网络、RDP 服务端。 |
| [HKLM\HARDWARE](hklm/hardware.md) | 运行时硬件枚举。 |
| [HKLM\BCD00000000](hklm/bcd.md) | 启动配置数据库映射。 |

## HKLM\SYSTEM 常见分支

| 路径 | 内容 |
|---|---|
| [Select](hklm/system/select.md) | `CurrentControlSet` 到 `ControlSet00x` 的映射。 |
| [ControlSet00x](hklm/system/controlset/index.md) | 真实控制集。 |
| [ControlSet00x\Services](hklm/system/controlset/services/index.md) | 服务、驱动和网络组件配置。 |
| [ControlSet00x\Services\<DriverName>](hklm/system/controlset/services/drivers.md) | 驱动服务配置。 |
| [ControlSet00x\Enum](hklm/system/controlset/enum/index.md) | 设备枚举树。 |
| [ControlSet00x\Enum\USBSTOR](hklm/system/controlset/enum/usbstor.md) | USB 存储设备枚举。 |
| [ControlSet00x\Enum\USB](hklm/system/controlset/enum/usb.md) | USB 总线设备枚举。 |
| [ControlSet00x\Enum\SWD\WPDBUSENUM](hklm/system/controlset/enum/swd-wpdbusenum.md) | WPD / MTP 设备枚举。 |
| [ControlSet00x\Control\DeviceClasses](hklm/system/controlset/control/deviceclasses.md) | 设备接口类注册。 |
| [MountedDevices](hklm/system/mounteddevices.md) | 卷、盘符和设备映射。 |
| [Control\Terminal Server](hklm/system/controlset/control/terminal-server.md) | RDP 服务端配置。 |
| [Control\Print\Monitors](hklm/system/controlset/control/print-monitors.md) | 打印端口监视器配置。 |
| [Services\Tcpip](hklm/system/controlset/services/tcpip.md) | TCP/IP 全局和接口配置。 |
| [Control\TimeZoneInformation](hklm/system/controlset/control/timezone.md) | 时区配置。 |
| [Control\ComputerName](hklm/system/controlset/control/computername.md) | 计算机名配置。 |
| [Control\Lsa](hklm/system/controlset/control/lsa/index.md) | LSA 运行配置。 |
| [Control\Lsa\Security Packages](hklm/system/controlset/control/lsa/security-packages.md) | LSA 安全支持包列表。 |

## HKLM\SOFTWARE 常见分支

| 路径 | 内容 |
|---|---|
| [Microsoft\Active Setup](hklm/software/microsoft/active-setup.md) | 每用户初始化组件定义。 |
| [Windows\CurrentVersion\Run](hklm/software/microsoft/windows/currentversion/run.md) | 机器级登录启动项。 |
| [ProfileList](hklm/software/microsoft/windows-nt/currentversion/profilelist.md) | SID 到 profile 路径映射。 |
| [Winlogon](hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | 交互式登录配置。 |
| [Image File Execution Options](hklm/software/microsoft/windows-nt/currentversion/ifeo.md) | 按进程名生效的启动配置。 |
| [Windows NT\CurrentVersion\Windows](hklm/software/microsoft/windows-nt/currentversion/appinit-dlls.md) | `AppInit_DLLs` 相关配置。 |
| [Windows\CurrentVersion\ShellServiceObjectDelayLoad](hklm/software/microsoft/windows/currentversion/shellserviceobjectdelayload.md) | Explorer Shell COM 延迟加载。 |
| [Microsoft\Windows Portable Devices](hklm/software/microsoft/windows-portable-devices.md) | WPD / MTP 设备元数据。 |
| [Windows NT\CurrentVersion\EMDMgmt](hklm/software/microsoft/windows-nt/currentversion/emdmgmt.md) | EMDMgmt / ReadyBoost 辅助记录。 |
| [Windows Search\VolumeInfoCache](hklm/software/microsoft/windows-search/volumeinfocache.md) | Windows Search 卷信息缓存。 |
| [Policies](hklm/software/policies.md) | 机器级策略写入位置。 |
| [Microsoft\Windows Defender](hklm/software/microsoft/windows-defender.md) | Defender 配置和状态相关项。 |
| [Uninstall](hklm/software/microsoft/windows/currentversion/uninstall.md) | 软件安装登记。 |
| [WOW6432Node](hklm/software/wow6432node.md) | 32 位应用注册表视图。 |
| [Classes](hklm/software/classes.md) | 机器级文件关联和 COM。 |

## HKEY_CURRENT_USER

| 路径 | 内容 |
|---|---|
| [HKCU\Software](hkcu/software/index.md) | 用户软件和应用配置。 |
| [Run / RunOnce](hkcu/software/microsoft/windows/currentversion/run.md) | 用户级登录启动项。 |
| [Explorer](hkcu/software/microsoft/windows/currentversion/explorer.md) | Shell / Explorer 用户级配置入口。 |
| [UserAssist](hkcu/software/microsoft/windows/currentversion/userassist.md) | Explorer 相关程序交互记录。 |
| [ComDlg32](hkcu/software/microsoft/windows/currentversion/comdlg32.md) | Common dialog MRU。 |
| [MountPoints2](hkcu/software/microsoft/windows/currentversion/mountpoints2.md) | 用户见过的卷、盘符或网络共享。 |
| [RunMRU](hkcu/software/microsoft/windows/currentversion/runmru.md) | Win+R 输入历史。 |
| [RecentDocs](hkcu/software/microsoft/windows/currentversion/recentdocs.md) | 最近文档名称和 MRU。 |
| [Internet Settings](hkcu/software/microsoft/windows/currentversion/internet-settings.md) | 用户代理、PAC、WinINet、ZoneMap。 |
| [Terminal Server Client](hkcu/software/microsoft/terminal-server-client.md) | MSTSC 客户端历史。 |
| [Classes](hkcu/software/classes.md) | 用户级文件关联和 COM。 |

## HKEY_USERS

| 路径 | 内容 |
|---|---|
| [.DEFAULT](hku/default.md) | 系统默认账户 hive。 |
| [服务账户 SID](hku/service-sids.md) | `S-1-5-18`、`S-1-5-19`、`S-1-5-20` 等。 |
| [SID 映射](hku/sid-mapping.md) | SID 与 profile 目录对应关系。 |
| [NTUSER.DAT](hku/ntuser.md) | 用户级配置 hive。 |
| [UsrClass.dat](hku/usrclass.md) | 用户级 Classes / Shell 数据 hive。 |

## 映射关系速查

| 映射 | 说明 |
|---|---|
| `HKCU` -> `HKU\<SID>` | live 环境下取决于当前进程上下文。 |
| `HKCR` -> `HKLM\Software\Classes` + `HKCU\Software\Classes` | 合并视图，离线时不要当成单独 hive。 |
| `HKCC` -> `HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current` | 当前硬件 profile 映射。 |
| `CurrentControlSet` -> `ControlSet00x` | 由 `HKLM\SYSTEM\Select\Current` 决定。 |
