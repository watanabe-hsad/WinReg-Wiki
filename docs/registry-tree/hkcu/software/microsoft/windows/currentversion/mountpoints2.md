# HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2

MountPoints2 保存当前用户 Shell 见过的卷、盘符、可移动介质或网络共享位置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` |
| 用户 SID | `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` |

## 离线位置

`C:\Users\<user>\NTUSER.DAT`

## 作用

记录用户层面见过的卷 GUID、盘符和网络共享。它比机器级 `MountedDevices` 更接近用户视角，但不直接说明文件复制或文件打开。

## 常见子键 / 值

| 名称 | 类型 | 含义 |
|---|---|---|
| `{volume-guid}` | Key | 用户 Shell 见过的卷标识或挂载点线索。 |
| `##server#share` | Key | SMB / UNC 共享访问线索。 |
| `_Autorun` | Key | 自动播放或 Shell 行为相关子项，具体含义视版本和上下文而定。 |
| `Shell` | Key | 与 Shell 动作相关的历史配置或子项。 |

## 默认状态 / 常见状态

普通桌面用户可能有多个卷和共享记录。企业共享盘、同步软件、备份软件、扫描共享和日常 USB 使用都会产生正常记录。

## 版本差异

Windows 版本、设备类型、Shell 使用方式和自动播放配置会影响子键形态。MTP 设备、网络共享和可移动磁盘的表现不同。

## 取证提示

该位置能把卷或共享线索归属到具体用户。文件访问和复制需要结合 LNK、Jump Lists、RecentDocs、ShellBags、文件系统时间线或 EDR removable media 事件。

## 相关场景

- [USB 与外接设备](../../../../../../questions/usb.md)
- [Shell / Explorer 用户行为](../../../../../../questions/shell-explorer.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU Explorer](explorer.md)
- [HKLM MountedDevices](../../../../../hklm/system/mounteddevices.md)
- [USBSTOR](../../../../../hklm/system/controlset/enum/usbstor.md)

