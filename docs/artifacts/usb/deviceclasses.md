---
tags:
  - USB
  - Device
  - SYSTEM
  - HKLM
---

# DeviceClasses

<div class="rfh-meta" markdown>
<span class="rfh-badge medium">取证价值 中</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">设备接口类</span>
</div>

## 摘要

`Control\DeviceClasses` 保存设备接口类实例，可用于把设备实例、接口 GUID 和部分 USB / portable device 记录串起来。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Control\DeviceClasses` | N/A | 机器级 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Control\DeviceClasses` | N/A | 机器级，需解析 `Select` |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SYSTEM\CurrentControlSet\Control\DeviceClasses`。子键通常以设备接口类 GUID 命名。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SYSTEM`。需要解析当前 `ControlSet00x`，并建议与 `Enum\USB`、`USBSTOR`、`SWD\WPDBUSENUM` 一起采集。

## 字段含义

| 字段 | 含义 |
|---|---|
| `{GUID}` | 设备接口类 GUID。 |
| `##?#USB#...` / `##?#STORAGE#...` | 设备接口实例路径，常能反映设备实例 ID。 |
| `DeviceInstance` | 设备实例关联值，具体存在与否取决于设备类。 |
| `SymbolicLink` | 设备符号链接相关信息，待按设备类验证。 |

## 取证含义

`DeviceClasses` 可作为设备接口层证据，帮助把一个设备在 `Enum` 树中的记录与系统暴露给应用的接口关联起来。它通常用于补强设备链路，而不是单独下结论。

## 可以证明

- 系统为某个设备接口类创建过接口实例。
- 可辅助关联 USB 设备、存储设备、WPD 设备和卷信息。
- 可为设备调查提供接口 GUID 和实例路径。

## 不能证明

- 不能单独证明设备连接时间。
- 不能单独证明文件访问或拷贝。
- 不能只凭接口 GUID 判断设备真实用途；需结合 `Enum` 和日志。

## 时间戳说明

接口实例 key 的 LastWrite 是 key 级更新时间。部分研究将其作为设备接口变化线索，但具体时间语义需结合 Windows 版本、设备类型和日志验证。

## 系统版本差异

不同 Windows 版本、驱动类型和设备接口类会造成结构差异；GUID 语义应参考 Microsoft 设备接口类文档或 `devpkey.h` / SetupAPI 输出。

## 攻击滥用

攻击者通常不会直接依赖该 key 持久化，但可通过 USB 设备、伪装设备或外接存储留下接口类记录。分析时重点是设备链路关联。

## 检测思路

- 监控敏感主机中新出现的 removable storage / WPD 相关接口类实例。
- 将 `DeviceClasses` 新增项与 `USBSTOR`、`SWD\WPDBUSENUM` 和 `MountedDevices` 对齐。
- 检测同一设备实例在多个主机出现的横向移动或数据搬运线索。

## 常见误报

- 正常 USB 存储、手机、打印机、摄像头、读卡器、蓝牙设备、虚拟 USB 设备。
- 驱动安装、Windows 更新、企业设备管理软件。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SYSTEM\CurrentControlSet\Control\DeviceClasses" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\DeviceClasses" /s
    ```

=== "Offline"

    ```text
    Collect SYSTEM hive and transaction logs.
    Resolve Select\Current before parsing ControlSet00x.
    ```

## 解析工具

- Registry Explorer
- RECmd
- USB Detective
- KAPE
- Velociraptor

## 交叉验证

- [USB](usb.md)
- [USBSTOR](usbstor.md)
- [Enum SWD WPDBUSENUM](swd-wpdbusenum.md)
- `SetupAPI.dev.log`
- `DriverFrameworks-UserMode/Operational`

## 示例结论

- `DeviceClasses` 中出现与同一 USB instance ID 对应的接口实例，可辅助证明系统为该设备创建过设备接口；连接时间仍需 `SetupAPI.dev.log` 或事件日志确认。
- 某接口类实例的 LastWrite 与 `USBSTOR` 记录接近，可作为设备枚举时间线的辅助证据，不能单独证明文件访问。

## 参考资料

- [Microsoft Learn: HKLM\SYSTEM\CurrentControlSet\Control Registry Tree](https://learn.microsoft.com/en-gb/windows-hardware/drivers/install/hklm-system-currentcontrolset-control-registry-tree)
- [artefacts.help: Registry - Devices and USB activity](https://artefacts.help/windows_registry_usb_activity.html)

## 相关页面

- 场景：[USB 与外接设备](../../questions/usb.md)
- 注册表位置：[HKLM\SYSTEM\ControlSet00x\Control\DeviceClasses](../../registry-tree/hklm/system/controlset/control/deviceclasses.md)

