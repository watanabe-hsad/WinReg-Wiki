# 注册表位置覆盖矩阵

本页用于维护当前覆盖范围和下一阶段补充方向。状态只描述本项目页面覆盖情况，不代表 Windows 注册表完整结构。

## 状态说明

| 状态 | 含义 |
|---|---|
| 已覆盖 | 已有可读页面，包含路径、离线 hive、常见值或子键、注意事项和相关场景。 |
| 需补厚 | 已有页面，但还需要补字段、版本差异、参考来源或相关位置。 |
| 待新增 | 当前还没有独立页面，后续可按场景需求补充。 |

## HKEY_CLASSES_ROOT

| 注册表路径 | 当前页面 | 覆盖状态 | 主题 | 相关场景 | 备注 |
|---|---|---|---|---|---|
| `HKCR` | [HKCR](hkcr/index.md) | 已覆盖 | 软件 / Shell | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | 合并视图，需同时理解 HKLM / HKCU Classes。 |
| `HKCU\Software\Classes` | [HKCU Classes](hkcu/software/classes.md) | 已覆盖 | 软件 / Shell | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | 用户级 Classes 来源。 |
| `HKLM\SOFTWARE\Classes` | [HKLM Classes](hklm/software/classes.md) | 已覆盖 | 软件 / Shell | [软件安装与卸载](../questions/software-install.md) | 机器级 Classes 来源。 |

## HKEY_CURRENT_USER

| 注册表路径 | 当前页面 | 覆盖状态 | 主题 | 相关场景 | 备注 |
|---|---|---|---|---|---|
| `HKCU` | [HKCU](hkcu/index.md) | 已覆盖 | 用户配置 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | Live 视图，离线对应 HKU SID。 |
| `HKCU\Environment` | [Environment](hkcu/environment.md) | 已覆盖 | 系统配置 / 持久化 | [自启动与持久化](../questions/persistence.md) | 用户级环境变量。 |
| `HKCU\Printers` | [Printers](hkcu/printers.md) | 已覆盖 | 用户行为 | [常规注册表检查](../questions/registry-checklist.md) | 用户级打印机连接。 |
| `HKCU\Software\Microsoft\Command Processor` | [Command Processor](hkcu/software/microsoft/command-processor.md) | 已覆盖 | 持久化 / 程序执行 | [程序执行](../questions/execution.md) | 用户级 `cmd.exe` 配置。 |
| `HKCU\Software\Microsoft\Terminal Server Client` | [Terminal Server Client](hkcu/software/microsoft/terminal-server-client.md) | 已覆盖 | RDP | [RDP 与远程访问](../questions/rdp.md) | MSTSC 客户端历史。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer` | [Explorer](hkcu/software/microsoft/windows/currentversion/explorer.md) | 已覆盖 | 用户行为 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | Shell 用户行为入口。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` | [UserAssist](hkcu/software/microsoft/windows/currentversion/userassist.md) | 已覆盖 | 程序执行 / 用户行为 | [程序执行](../questions/execution.md) | 需工具解析 ROT13 和二进制数据。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` | [RunMRU](hkcu/software/microsoft/windows/currentversion/runmru.md) | 已覆盖 | 用户行为 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | 输入历史不等于执行成功。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` | [RecentDocs](hkcu/software/microsoft/windows/currentversion/recentdocs.md) | 已覆盖 | 用户行为 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | 文件名线索，不等于内容读取。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32` | [ComDlg32](hkcu/software/microsoft/windows/currentversion/comdlg32.md) | 已覆盖 | 用户行为 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | PIDL 需工具解析。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | [MountPoints2](hkcu/software/microsoft/windows/currentversion/mountpoints2.md) | 已覆盖 | 设备 / 用户行为 | [USB 与外接设备](../questions/usb.md) | 用户见过卷或共享。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced` | 待新增 | 待新增 | 用户行为 / 策略 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | Explorer UI 偏好和显示配置。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths` | 待新增 | 待新增 | 用户行为 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | 地址栏输入历史。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings` | [Internet Settings](hkcu/software/microsoft/windows/currentversion/internet-settings.md) | 已覆盖 | 网络 | [网络与系统环境](../questions/network.md) | 用户级 WinINet 配置。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` | [ZoneMap](hkcu/software/microsoft/windows/currentversion/internet-settings/zonemap.md) | 已覆盖 | 网络 / 策略 | [安全策略与防护配置](../questions/policy-security.md) | URL 安全区域映射。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies` | [Policies](hkcu/software/microsoft/windows/currentversion/policies.md) | 已覆盖 | 策略 | [安全策略与防护配置](../questions/policy-security.md) | 用户级策略父级。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer` | [Policies\Explorer](hkcu/software/microsoft/windows/currentversion/policies/explorer.md) | 已覆盖 | 策略 / Shell | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | Explorer UI 限制策略。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System` | 待新增 | 待新增 | 策略 | [安全策略与防护配置](../questions/policy-security.md) | 用户级系统策略。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Attachments` | 待新增 | 待新增 | 策略 / 用户行为 | [安全策略与防护配置](../questions/policy-security.md) | Attachment Manager 相关策略。 |
| `HKCU\Software\Microsoft\Windows\Shell\BagMRU` | 待新增 | 待新增 | 用户行为 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | ShellBags 用户视图。 |
| `HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU` | 待新增 | 待新增 | 用户行为 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | UsrClass.dat 中常见 ShellBags 路径。 |

## HKLM\SAM

| 注册表路径 | 当前页面 | 覆盖状态 | 主题 | 相关场景 | 备注 |
|---|---|---|---|---|---|
| `HKLM\SAM` | [SAM](hklm/sam.md) | 已覆盖 | 账户 | [账户与安全](../questions/accounts-security.md) | 需要专门工具解析。 |
| `HKLM\SAM\SAM\Domains\Account\Users` | 待新增 | 待新增 | 账户 | [账户与安全](../questions/accounts-security.md) | 可作为后续账户记录页。 |

## HKLM\SECURITY

| 注册表路径 | 当前页面 | 覆盖状态 | 主题 | 相关场景 | 备注 |
|---|---|---|---|---|---|
| `HKLM\SECURITY` | [SECURITY](hklm/security.md) | 已覆盖 | 安全策略 / 账户 | [安全策略与防护配置](../questions/policy-security.md) | LSA Secrets、Policy、Cache 等需工具解析。 |
| `HKLM\SECURITY\Policy\PolAdtEv` | 待新增 | 待新增 | 安全策略 | [安全策略与防护配置](../questions/policy-security.md) | 审计策略解析候选。 |

## HKLM\SOFTWARE

| 注册表路径 | 当前页面 | 覆盖状态 | 主题 | 相关场景 | 备注 |
|---|---|---|---|---|---|
| `HKLM\SOFTWARE` | [SOFTWARE](hklm/software/index.md) | 已覆盖 | 软件 / 策略 | [软件安装与卸载](../questions/software-install.md) | 机器级软件配置父级。 |
| `HKLM\SOFTWARE\Microsoft\Active Setup` | [Active Setup](hklm/software/microsoft/active-setup.md) | 已覆盖 | 持久化 | [自启动与持久化](../questions/persistence.md) | 每用户初始化组件。 |
| `HKLM\SOFTWARE\Microsoft\Command Processor` | [Command Processor](hklm/software/microsoft/command-processor.md) | 已覆盖 | 程序执行 / 持久化 | [程序执行](../questions/execution.md) | 机器级 `cmd.exe` 配置。 |
| `HKLM\SOFTWARE\Microsoft\Windows Defender` | [Windows Defender](hklm/software/microsoft/windows-defender.md) | 已覆盖 | 策略 / 防护 | [安全策略与防护配置](../questions/policy-security.md) | 产品配置和状态线索。 |
| `HKLM\SOFTWARE\Policies` | [Policies](hklm/software/policies.md) | 已覆盖 | 策略 | [安全策略与防护配置](../questions/policy-security.md) | GPO / MDM 常见写入位置。 |
| `HKLM\SOFTWARE\Policies\Microsoft\Windows Defender` | [Defender Policies](hklm/software/policies/microsoft/windows-defender.md) | 已覆盖 | 策略 / 防护 | [反取证与清理痕迹](../questions/anti-forensics.md) | 需结合 Defender 运行时状态。 |
| `HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall` | [WindowsFirewall Policies](hklm/software/policies/microsoft/windowsfirewall.md) | 已覆盖 | 策略 / 网络 | [安全策略与防护配置](../questions/policy-security.md) | 防火墙策略位置。 |
| `HKLM\SOFTWARE\WOW6432Node` | [WOW6432Node](hklm/software/wow6432node.md) | 已覆盖 | 软件 | [软件安装与卸载](../questions/software-install.md) | 32 位注册表视图。 |
| `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths` | [App Paths](hklm/software/microsoft/windows/currentversion/app-paths.md) | 已覆盖 | 软件 / 程序执行 | [程序执行](../questions/execution.md) | 应用路径注册。 |
| `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` | [Run / RunOnce](hklm/software/microsoft/windows/currentversion/run.md) | 已覆盖 | 持久化 | [自启动与持久化](../questions/persistence.md) | 机器级登录启动项。 |
| `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall` | [Uninstall](hklm/software/microsoft/windows/currentversion/uninstall.md) | 已覆盖 | 软件 | [软件安装与卸载](../questions/software-install.md) | 软件安装登记。 |
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList` | [ProfileList](hklm/software/microsoft/windows-nt/currentversion/profilelist.md) | 已覆盖 | 账户 | [账户与安全](../questions/accounts-security.md) | SID 到 profile 映射。 |
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` | [Winlogon](hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | 已覆盖 | 登录 / 持久化 | [账户与安全](../questions/accounts-security.md) | 登录配置父级。 |
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` | [IFEO](hklm/software/microsoft/windows-nt/currentversion/ifeo.md) | 已覆盖 | 程序执行 / 持久化 | [自启动与持久化](../questions/persistence.md) | 按进程名生效。 |
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags` | [AppCompatFlags](hklm/software/microsoft/windows-nt/currentversion/appcompatflags.md) | 已覆盖 | 程序执行 / 软件 | [程序执行](../questions/execution.md) | 机器级应用兼容性入口。 |
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers` | [Layers](hklm/software/microsoft/windows-nt/currentversion/appcompatflags/layers.md) | 已覆盖 | 程序执行 / 软件 | [软件安装与卸载](../questions/software-install.md) | 兼容层配置。 |

## HKLM\SYSTEM

| 注册表路径 | 当前页面 | 覆盖状态 | 主题 | 相关场景 | 备注 |
|---|---|---|---|---|---|
| `HKLM\SYSTEM` | [SYSTEM](hklm/system/index.md) | 已覆盖 | 系统配置 | [常规注册表检查](../questions/registry-checklist.md) | SYSTEM hive 父级。 |
| `HKLM\SYSTEM\Select` | [Select](hklm/system/select.md) | 已覆盖 | 系统配置 | [常规注册表检查](../questions/registry-checklist.md) | ControlSet 映射入口。 |
| `HKLM\SYSTEM\ControlSet00x` | [ControlSet00x](hklm/system/controlset/index.md) | 已覆盖 | 系统配置 | [常规注册表检查](../questions/registry-checklist.md) | 离线分析需先解析 Select。 |
| `HKLM\SYSTEM\ControlSet00x\Services` | [Services](hklm/system/controlset/services/index.md) | 已覆盖 | 持久化 / 系统配置 | [自启动与持久化](../questions/persistence.md) | 服务和驱动配置。 |
| `HKLM\SYSTEM\ControlSet00x\Services\EventLog` | [EventLog](hklm/system/controlset/services/eventlog.md) | 已覆盖 | 安全策略 | [反取证与清理痕迹](../questions/anti-forensics.md) | 日志配置，不是日志内容。 |
| `HKLM\SYSTEM\ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy` | [FirewallPolicy](hklm/system/controlset/services/sharedaccess/firewallpolicy.md) | 已覆盖 | 网络 / 策略 | [安全策略与防护配置](../questions/policy-security.md) | 本地防火墙 profile 和规则。 |
| `HKLM\SYSTEM\ControlSet00x\Services\Tcpip` | [Tcpip](hklm/system/controlset/services/tcpip.md) | 已覆盖 | 网络 | [网络与系统环境](../questions/network.md) | TCP/IP 父级。 |
| `HKLM\SYSTEM\ControlSet00x\Services\Tcpip\Parameters\Interfaces` | [Interfaces](hklm/system/controlset/services/tcpip/parameters/interfaces.md) | 已覆盖 | 网络 | [网络与系统环境](../questions/network.md) | 接口级 TCP/IP 配置。 |
| `HKLM\SYSTEM\ControlSet00x\Enum` | [Enum](hklm/system/controlset/enum/index.md) | 已覆盖 | 设备 | [USB 与外接设备](../questions/usb.md) | 设备枚举父级。 |
| `HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR` | [USBSTOR](hklm/system/controlset/enum/usbstor.md) | 已覆盖 | 设备 | [USB 与外接设备](../questions/usb.md) | USB 存储设备枚举。 |
| `HKLM\SYSTEM\ControlSet00x\Enum\USB` | [USB](hklm/system/controlset/enum/usb.md) | 已覆盖 | 设备 | [USB 与外接设备](../questions/usb.md) | USB 总线设备枚举。 |
| `HKLM\SYSTEM\ControlSet00x\Enum\SWD\WPDBUSENUM` | [SWD\WPDBUSENUM](hklm/system/controlset/enum/swd-wpdbusenum.md) | 已覆盖 | 设备 | [USB 与外接设备](../questions/usb.md) | WPD / MTP 设备。 |
| `HKLM\SYSTEM\ControlSet00x\Enum\STORAGE` | 待新增 | 待新增 | 设备 | [USB 与外接设备](../questions/usb.md) | 存储设备枚举候选。 |
| `HKLM\SYSTEM\MountedDevices` | [MountedDevices](hklm/system/mounteddevices.md) | 需补厚 | 设备 | [USB 与外接设备](../questions/usb.md) | 已有页面，本轮补强参考和相关位置。 |
| `HKLM\SYSTEM\ControlSet00x\Control\DeviceClasses` | [DeviceClasses](hklm/system/controlset/control/deviceclasses.md) | 已覆盖 | 设备 | [USB 与外接设备](../questions/usb.md) | 设备接口类。 |
| `HKLM\SYSTEM\ControlSet00x\Control\DeviceContainers` | 待新增 | 待新增 | 设备 | [USB 与外接设备](../questions/usb.md) | 设备容器关联候选。 |
| `HKLM\SYSTEM\ControlSet00x\Control\Terminal Server` | [Terminal Server](hklm/system/controlset/control/terminal-server.md) | 已覆盖 | RDP | [RDP 与远程访问](../questions/rdp.md) | RDP 服务端配置。 |
| `HKLM\SYSTEM\ControlSet00x\Control\Terminal Server\WinStations\RDP-Tcp` | [RDP-Tcp](hklm/system/controlset/control/terminal-server/rdp-tcp.md) | 已覆盖 | RDP | [RDP 与远程访问](../questions/rdp.md) | Listener 端口和安全层。 |
| `HKLM\SYSTEM\ControlSet00x\Control\Session Manager` | [Session Manager](hklm/system/controlset/control/session-manager/index.md) | 已覆盖 | 系统配置 / 持久化 | [常规注册表检查](../questions/registry-checklist.md) | 启动早期配置父级。 |
| `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\Environment` | [Environment](hklm/system/controlset/control/session-manager/environment.md) | 已覆盖 | 系统配置 | [自启动与持久化](../questions/persistence.md) | 系统级环境变量。 |
| `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\Memory Management` | [Memory Management](hklm/system/controlset/control/session-manager/memory-management.md) | 已覆盖 | 系统配置 / 反取证 | [反取证与清理痕迹](../questions/anti-forensics.md) | Paging file 相关配置。 |
| `HKLM\SYSTEM\ControlSet00x\Control\Lsa` | [LSA](hklm/system/controlset/control/lsa/index.md) | 已覆盖 | 账户 / 安全 | [账户与安全](../questions/accounts-security.md) | 认证包和 LSASS 相关配置。 |

## HKEY_USERS

| 注册表路径 | 当前页面 | 覆盖状态 | 主题 | 相关场景 | 备注 |
|---|---|---|---|---|---|
| `HKU` | [HKEY_USERS](hku/index.md) | 已覆盖 | 用户配置 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | 已加载用户 hive 集合。 |
| `HKU\.DEFAULT` | [.DEFAULT](hku/default.md) | 已覆盖 | 系统配置 | [常规注册表检查](../questions/registry-checklist.md) | 不是普通用户默认 profile。 |
| `HKU\<SID>` | [SID 映射](hku/sid-mapping.md) | 已覆盖 | 账户 / 用户配置 | [账户与安全](../questions/accounts-security.md) | 需结合 ProfileList。 |
| `NTUSER.DAT` | [NTUSER.DAT](hku/ntuser.md) | 已覆盖 | 用户配置 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | 用户级 hive 文件。 |
| `UsrClass.dat` | [UsrClass.dat](hku/usrclass.md) | 已覆盖 | 用户配置 / Shell | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | Classes 和 Shell 相关数据。 |

## HKEY_CURRENT_CONFIG

| 注册表路径 | 当前页面 | 覆盖状态 | 主题 | 相关场景 | 备注 |
|---|---|---|---|---|---|
| `HKCC` | [HKEY_CURRENT_CONFIG](hkcc/index.md) | 已覆盖 | 系统配置 | [常规注册表检查](../questions/registry-checklist.md) | Current hardware profile 映射视图。 |

## 下一阶段候选

| 注册表路径 | 覆盖状态 | 主题 | 相关场景 | 备注 |
|---|---|---|---|---|
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System` | 待新增 | 策略 | [安全策略与防护配置](../questions/policy-security.md) | 用户级系统策略。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Attachments` | 待新增 | 策略 / 用户行为 | [反取证与清理痕迹](../questions/anti-forensics.md) | Attachment Manager。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Associations` | 待新增 | 策略 / Shell | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | 文件关联策略。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced` | 待新增 | 用户行为 / Shell | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | Explorer 显示和行为偏好。 |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths` | 待新增 | 用户行为 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | Explorer 地址栏输入历史。 |
| `HKCU\Software\Microsoft\Windows\Shell\BagMRU` | 待新增 | 用户行为 | [Shell / Explorer 用户行为](../questions/shell-explorer.md) | ShellBags。 |
| `HKLM\SYSTEM\ControlSet00x\Enum\STORAGE` | 待新增 | 设备 | [USB 与外接设备](../questions/usb.md) | 存储设备枚举。 |
| `HKLM\SYSTEM\ControlSet00x\Control\DeviceContainers` | 待新增 | 设备 | [USB 与外接设备](../questions/usb.md) | 设备容器关联。 |
