---
tags:
  - USB
  - Device
  - WPD
  - SYSTEM
  - HKLM
---

# Enum SWD WPDBUSENUM

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">Portable device enumeration</span>
</div>

## 摘要

`Enum\SWD\WPDBUSENUM` 记录 Windows Portable Device 枚举信息，常用于补充手机、相机、MTP/PTP 设备和部分 USB 存储设备调查。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Enum\SWD\WPDBUSENUM` | N/A | 机器级 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Enum\SWD\WPDBUSENUM` | N/A | 机器级，需解析 `Select` |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SYSTEM\CurrentControlSet\Enum\SWD\WPDBUSENUM`。子键名称常包含 `_??_USBSTOR#...`、设备 ID 或 WPD 相关实例标识。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SYSTEM`。建议同时采集 `SOFTWARE` hive 中的 `Microsoft\Windows Portable Devices\Devices`。

## 字段含义

| 字段 | 含义 |
|---|---|
| `<instance>` | WPD bus enumerator 设备实例。 |
| `FriendlyName` | 设备友好名称，可能是卷标、设备名或用户可见名称。 |
| `ContainerID` | 设备容器 ID，可用于关联 USB / WPD / portable devices 记录。 |
| `HardwareID` | 设备硬件 ID。 |
| `ClassGUID` | 设备类 GUID。 |

## 取证含义

该 key 对移动设备、MTP/PTP、WPD 暴露的设备尤其有用。它可补足只看 `USBSTOR` 时遗漏的手机、相机或复合设备线索。

## 可以证明

- 系统曾枚举过某个 WPD / portable device 实例。
- 可提取友好名称、ContainerID、instance ID 等关联字段。
- 可与 `Windows Portable Devices\Devices` 建立系统级 portable device 记录。

## 不能证明

- 不能单独证明用户浏览或复制了设备中的文件。
- 不能单独证明设备以 USB mass storage 方式出现。
- 不能仅凭 LastWrite 确定首次连接、最后连接或拔出时间。

## 时间戳说明

子键 LastWrite 是 WPD 枚举记录的更新时间线索。设备连接、安装和移除时间需要结合 `SetupAPI.dev.log`、DeviceSetupManager、DriverFrameworks 和 WPD/MTP 事件。

## 系统版本差异

Windows 10/11 对 WPD/MTP 设备支持较完整。Windows 7/8 也可能存在相关记录，但字段和事件通道差异待验证。

## 攻击滥用

攻击者或内部人员可使用手机、相机或 MTP 设备进行文件搬运。该键只能说明 portable device 枚举，不能直接说明文件传输。

## 检测思路

- 监控 `HKLM\System\CurrentControlSet\Enum\SWD\WPDBUSENUM` 新增或修改。
- 与 `HKLM\SOFTWARE\Microsoft\Windows Portable Devices\Devices` 同时出现的新设备关联。
- 对敏感主机新增手机 / portable device 记录做告警，再结合文件访问和 EDR 事件确认。

## 常见误报

- 手机充电/同步、相机导入、媒体播放器、扫描仪、USB 存储暴露为 WPD。
- 企业移动设备管理、驱动更新、Windows 照片导入或媒体同步工具。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SYSTEM\CurrentControlSet\Enum\SWD\WPDBUSENUM" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Enum\SWD\WPDBUSENUM" /s
    ```

=== "Offline"

    ```text
    Collect SYSTEM and SOFTWARE hives; resolve SYSTEM\Select before parsing.
    ```

## 解析工具

- Registry Explorer
- RECmd
- USB Detective
- KAPE
- Velociraptor

## 交叉验证

- [Portable Devices](portable-devices.md)
- [USB](usb.md)
- [DeviceClasses](deviceclasses.md)
- `Microsoft-Windows-WPD-MTPClassDriver/Operational`
- `DeviceSetupManager/Admin`
- LNK、Jump Lists、USN Journal、文件系统时间线

## 示例结论

- `SWD\WPDBUSENUM` 中出现某手机的 friendly name 和 ContainerID，说明系统曾通过 WPD 枚举该设备；文件是否被复制需结合用户级和文件系统证据。
- 该 WPD instance 与 `Windows Portable Devices\Devices` 条目匹配，可把 SOFTWARE 和 SYSTEM hive 中的 portable device 记录归并为同一设备。

## 参考资料

- [Splunk: Windows WPDBusEnum Registry Key Modification](https://research.splunk.com/endpoint/52b48e8b-eb6e-48b0-b8f1-73273f6b134e/)
- [artefacts.help: Registry - Devices and USB activity](https://artefacts.help/windows_registry_usb_activity.html)
- [Microsoft Learn Q&A: SWD\WPDBUSENUM and WPD components](https://learn.microsoft.com/en-ca/answers/questions/5856589/device-swdwpdbusenum%28%2801300028-3222-11f1-a798-9ceb)

## 相关页面

- 场景：[USB 与外接设备](../../questions/usb.md)
- 注册表位置：[HKLM\SYSTEM\ControlSet00x\Enum\SWD\WPDBUSENUM](../../registry-tree/hklm/system/controlset/enum/swd-wpdbusenum.md)

