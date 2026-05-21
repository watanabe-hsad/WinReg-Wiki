---
tags:
  - USB
  - Device
  - WPD
  - SOFTWARE
  - HKLM
---

# Portable Devices

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">Windows Portable Devices</span>
</div>

## 摘要

`Windows Portable Devices` 记录 Windows Portable Device 设备信息，可用于关联手机、相机、MTP/PTP 设备和部分可移动存储设备。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows Portable Devices\Devices` | N/A | 机器级 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows Portable Devices\Devices` | N/A | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SOFTWARE\Microsoft\Windows Portable Devices\Devices`。子键名称可能包含 `SWD#WPDBUSENUM#...` 等编码后的设备实例。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SOFTWARE`。建议同时采集 `SYSTEM` hive 中的 `Enum\SWD\WPDBUSENUM`。

## 字段含义

| 字段 | 含义 |
|---|---|
| `<device instance>` | Portable device 设备实例记录。 |
| `FriendlyName` | 设备友好名称或用户可见名称，具体存在与否取决于设备。 |
| `Icons` / shell 相关值 | 设备显示相关值，取证语义有限。 |
| 其他属性值 | 具体字段随 WPD 设备和 Windows 版本变化，需按样本解析。 |

## 取证含义

该 key 可帮助确认系统曾登记过某个 portable device，并与 `SWD\WPDBUSENUM` 记录互相补强。对于手机和相机类设备，价值通常高于只看 `USBSTOR`。

## 可以证明

- 系统登记过某个 Windows Portable Device。
- 可与 WPD bus enumerator 记录建立设备对应关系。
- 可辅助提取设备友好名称或 instance ID。

## 不能证明

- 不能单独证明设备中的文件被打开或复制。
- 不能单独证明 R/W 权限或访问成功。
- 不能单独给出精确连接时间。

## 时间戳说明

子键 LastWrite 是设备登记项更新时间线索。需要结合 WPD/MTP 事件、DeviceSetupManager、SetupAPI 和用户级文件访问 artifact 确认时间线。

## 系统版本差异

Windows 10/11 的 WPD/MTP 栈较常见。不同设备厂商、驱动和连接模式会影响字段完整性；版本差异待验证。

## 攻击滥用

内部人员或攻击者可能通过手机、相机、媒体播放器进行文件搬运。该 key 只说明 portable device 登记，不直接证明数据移动。

## 检测思路

- 监控 `HKLM\SOFTWARE\Microsoft\Windows Portable Devices\Devices` 新增设备。
- 将新设备与 `SWD\WPDBUSENUM`、LNK、Jump Lists 和文件系统时间线关联。
- 对不允许外接设备的主机，登记新 portable device 可作为调查触发点。

## 常见误报

- 手机连接充电、照片导入、媒体同步、扫描仪、相机、录音笔。
- 企业 MDM、驱动安装、Windows Photos、Media Player 或厂商同步软件。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SOFTWARE\Microsoft\Windows Portable Devices\Devices" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows Portable Devices\Devices" /s
    ```

=== "Offline"

    ```text
    Collect SOFTWARE hive; pair with SYSTEM\ControlSet00x\Enum\SWD\WPDBUSENUM.
    ```

## 解析工具

- Registry Explorer
- RECmd
- KAPE
- Velociraptor
- USB Detective

## 交叉验证

- [Enum SWD WPDBUSENUM](swd-wpdbusenum.md)
- [USB](usb.md)
- `Microsoft-Windows-WPD-MTPClassDriver/Operational`
- `DeviceSetupManager/Admin`
- LNK、Jump Lists、RecentDocs、USN Journal

## 示例结论

- `Windows Portable Devices\Devices` 和 `SWD\WPDBUSENUM` 中出现同一设备实例，说明系统登记并枚举过该 portable device；是否访问文件需用户级和文件系统证据。
- 该设备 friendly name 与用户 LNK 目标卷名称一致，可辅助说明用户可见设备与系统级 portable device 记录属于同一调查对象。

## 参考资料

- [Splunk: Windows WPDBusEnum Registry Key Modification](https://research.splunk.com/endpoint/52b48e8b-eb6e-48b0-b8f1-73273f6b134e/)
- [artefacts.help: Registry - Devices and USB activity](https://artefacts.help/windows_registry_usb_activity.html)

## 相关页面

- 场景：[USB 与外接设备](../../questions/usb.md)
- 注册表位置：[HKLM\SOFTWARE\Microsoft\Windows Portable Devices](../../registry-tree/hklm/software/microsoft/windows-portable-devices.md)

