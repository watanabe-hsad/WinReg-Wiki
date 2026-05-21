---
tags:
  - USB
  - Device
  - SYSTEM
  - HKLM
---

# USB

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">USB 设备枚举</span>
</div>

## 摘要

`Enum\USB` 记录 USB 总线层面的设备枚举信息，可用于识别系统曾识别过的 USB 设备及其 VID / PID / instance ID。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Enum\USB` | N/A | 机器级 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Enum\USB` | N/A | 机器级，需解析 `Select` |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SYSTEM\CurrentControlSet\Enum\USB`。离线分析时先用 `HKLM\SYSTEM\Select\Current` 解析当前 `ControlSet00x`。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SYSTEM`，建议同时采集 `SYSTEM.LOG1`、`SYSTEM.LOG2` 和 `C:\Windows\INF\setupapi.dev.log`。

## 字段含义

| 字段 | 含义 |
|---|---|
| `VID_xxxx&PID_yyyy` | USB vendor ID 和 product ID 组合。 |
| `<instance ID>` | 设备实例 ID，可能包含序列号或父级生成 ID。 |
| `DeviceDesc` | 设备描述，常见为驱动 INF 中的描述字符串。 |
| `FriendlyName` | 友好名称；并非所有设备都有。 |
| `HardwareID` | 硬件 ID 列表。 |
| `ContainerID` | 设备容器 ID，可用于关联同一物理设备的多个接口。 |

## 取证含义

`Enum\USB` 是 USB 总线层面的设备记录，范围比 `USBSTOR` 更广，可包含 HID、手机、摄像头、读卡器、复合设备等。它能帮助确认系统曾识别过某个 USB 设备或接口。

## 可以证明

- 系统曾枚举过特定 VID / PID / instance ID 的 USB 设备。
- 可辅助关联同一物理设备的多个接口或功能。
- 可与 `USBSTOR`、`SWD\WPDBUSENUM`、`DeviceClasses` 建立设备链路。

## 不能证明

- 不能单独证明设备是存储设备。
- 不能单独证明用户访问过设备中的文件。
- 不能把 key LastWrite 直接解释为首次插入或最后拔出时间。

## 时间戳说明

设备实例 key 的 LastWrite 反映该 key 最近更新，不是单条 value 的创建时间。USB 首次安装时间更适合从 `setupapi.dev.log`、设备安装事件和 ETW 日志交叉确认。

## 系统版本差异

Windows 7 / 10 / 11 均存在 `Enum\USB`，但子键、属性 value 和设备栈写入行为会随驱动模型和设备类型变化；具体时间语义待按版本验证。

## 攻击滥用

攻击者可使用 USB 设备传输工具、投递 payload 或连接伪装设备。该键本身不记录攻击行为，只记录系统设备枚举结果。

## 检测思路

- 关注敏感主机上新出现的未知 VID / PID / instance ID。
- 关联同一时间窗口内的 `USBSTOR`、`SWD\WPDBUSENUM` 和 `Windows Portable Devices` 变化。
- 将新设备出现时间与文件访问、LNK、Jump Lists、EDR removable media 事件对齐。

## 常见误报

- 键盘、鼠标、摄像头、蓝牙适配器、打印机、手机、读卡器、扩展坞和安全密钥。
- 企业资产管理、驱动更新、虚拟化平台或远程 USB 转发。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SYSTEM\CurrentControlSet\Enum\USB" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Enum\USB" /s
    ```

=== "Offline"

    ```text
    Collect SYSTEM hive, transaction logs, setupapi.dev.log, and relevant event logs.
    Resolve SYSTEM\Select before reading ControlSet00x.
    ```

## 解析工具

- Registry Explorer
- RECmd
- USB Detective
- RegRipper
- KAPE
- Velociraptor

## 交叉验证

- [USBSTOR](usbstor.md)
- [DeviceClasses](deviceclasses.md)
- [Enum SWD WPDBUSENUM](swd-wpdbusenum.md)
- `SetupAPI.dev.log`
- `Microsoft-Windows-DriverFrameworks-UserMode/Operational`
- `Microsoft-Windows-DeviceSetupManager/Admin`

## 示例结论

- `SYSTEM\ControlSet001\Enum\USB` 出现 `VID_0781&PID_5581` 设备实例，说明系统曾枚举该 USB 设备；是否为存储设备和是否访问文件需结合 `USBSTOR`、`MountedDevices` 和用户级 artifact。
- 该设备的 `ContainerID` 与 `SWD\WPDBUSENUM` 条目一致，可辅助把 USB 总线记录和 WPD 记录归为同一物理设备。

## 参考资料

- [Microsoft Learn: HKLM\SYSTEM\CurrentControlSet\Enum Registry Tree](https://learn.microsoft.com/en-ca/windows-hardware/drivers/install/hklm-system-currentcontrolset-enum-registry-tree)
- [artefacts.help: Registry - Devices and USB activity](https://artefacts.help/windows_registry_usb_activity.html)
- [13Cubed Windows Registry Cheat Sheet](https://cdn.13cubed.com/downloads/windows_registry_cheat_sheet.pdf)

## 相关页面

- 场景：[USB 与外接设备](../../questions/usb.md)
- 注册表位置：[HKLM\SYSTEM\ControlSet00x\Enum\USB](../../registry-tree/hklm/system/controlset/enum/usb.md)

