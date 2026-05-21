# HKEY_LOCAL_MACHINE

`HKEY_LOCAL_MACHINE`，简称 `HKLM`，保存机器级配置。它不归属于某个用户，适合查系统、服务、设备、策略和本地账户数据库。

## 子树与来源

| 子树 | 离线文件或来源 | 主要内容 |
|---|---|---|
| [HKLM\SAM](sam.md) | `C:\Windows\System32\Config\SAM` | 本地用户、RID、组关系、账户状态。 |
| [HKLM\SECURITY](security.md) | `C:\Windows\System32\Config\SECURITY` | LSA、审计策略、Secret、安全策略。 |
| [HKLM\SOFTWARE](software/index.md) | `C:\Windows\System32\Config\SOFTWARE` | 软件、策略、ProfileList、Winlogon、Defender、Classes。 |
| [HKLM\SYSTEM](system/index.md) | `C:\Windows\System32\Config\SYSTEM` | ControlSet、服务、驱动、设备、网络、RDP 服务端。 |
| [HKLM\HARDWARE](hardware.md) | 运行时生成 | 当前硬件信息。 |
| [HKLM\BCD00000000](bcd.md) | `\Boot\BCD` 或 EFI 分区 BCD | 启动配置。 |

## 常用路径

| 路径 | 含义 |
|---|---|
| [HKLM\SYSTEM\Select](system/select.md) | `CurrentControlSet` 到 `ControlSet00x` 的映射。 |
| [HKLM\SYSTEM\ControlSet00x\Services](system/controlset/services/index.md) | 服务、驱动、网络组件、部分系统组件配置。 |
| [HKLM\SYSTEM\MountedDevices](system/mounteddevices.md) | 卷 GUID、盘符和设备映射。 |
| [HKLM\SYSTEM\ControlSet00x\Enum](system/controlset/enum/index.md) | 设备枚举树。 |
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList](software/microsoft/windows-nt/currentversion/profilelist.md) | SID 到 profile 目录的映射。 |
| [HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run](software/microsoft/windows/currentversion/run.md) | 机器级登录启动项。 |
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon](software/microsoft/windows-nt/currentversion/winlogon.md) | 登录链、Shell、Userinit 等。 |
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options](software/microsoft/windows-nt/currentversion/ifeo.md) | IFEO 和 Debugger 配置。 |
| [HKLM\SOFTWARE\Policies](software/policies.md) | 本地策略、GPO / MDM 写入结果。 |

## 注意

| 项 | 说明 |
|---|---|
| `CurrentControlSet` | live 系统可用；离线分析应先读 `SYSTEM\Select`。 |
| `WOW6432Node` | 64 位系统上的 32 位注册表视图。 |
| `HARDWARE` | 运行时生成，不是常规离线 hive。 |
| `.LOG1` / `.LOG2` | hive transaction log，采集时建议保留。 |

## 相关场景

- [常规注册表检查](../../questions/registry-checklist.md)
- [自启动与持久化](../../questions/persistence.md)
- [USB 与外接设备](../../questions/usb.md)
- [账户与安全](../../questions/accounts-security.md)

## 补充阅读

[Services](../../artifacts/persistence/services.md),
[Run / RunOnce](../../artifacts/persistence/run-keys.md),
[IFEO](../../artifacts/persistence/ifeo.md),
[Winlogon Userinit](../../artifacts/persistence/winlogon-userinit.md),
[Winlogon Shell](../../artifacts/persistence/winlogon-shell.md),
[ProfileList](../../artifacts/security/profilelist.md),
[USBSTOR](../../artifacts/usb/usbstor.md),
[MountedDevices](../../artifacts/usb/mounteddevices.md)
