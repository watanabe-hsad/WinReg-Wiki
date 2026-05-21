---
tags:
  - USB
  - Device
  - SOFTWARE
  - HKLM
---

# EMDMgmt

<div class="rfh-meta" markdown>
<span class="rfh-badge medium">取证价值 中</span>
<span class="rfh-badge low">检测价值 低</span>
<span class="rfh-badge">ReadyBoost / external memory device</span>
</div>

## 摘要

`EMDMgmt` 是 ReadyBoost / External Memory Device 相关记录，可提供部分可移动或非系统存储设备的设备 ID、卷序列号和卷标线索。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\EMDMgmt` | N/A | 机器级 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\EMDMgmt` | N/A | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt`。该 key 与 ReadyBoost 相关，不是所有系统都会有可用记录。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SOFTWARE`，建议同时采集 `SYSTEM` hive 和 `SetupAPI.dev.log` 以确认设备枚举链路。

## 字段含义

| 字段 | 含义 |
|---|---|
| `<device ID / hardware ID>` | 子键名，常包含设备厂商、产品、修订号或路径编码。 |
| `DeviceStatus` | ReadyBoost / EMD 状态相关值，具体语义待版本验证。 |
| `FriendlyName` / volume label 相关值 | 可能出现卷友好名称或卷标，字段名随版本/设备变化。 |
| volume serial 相关值 | 可能包含卷序列号线索，具体 value 名称需按样本验证。 |

## 取证含义

`EMDMgmt` 可作为 USB/外接存储调查的补充来源，尤其当设备不完整出现在 `USBSTOR` 或以非典型存储栈出现时。它常用于通过 device ID、volume serial、volume label 反查设备。

## 可以证明

- 系统中存在 ReadyBoost / EMD 对某个设备的评估或记录。
- 可辅助提取设备 ID、卷标、卷序列号等线索。
- 可补充 `USBSTOR`、`MountedDevices` 和 `VolumeInfoCache` 的映射。

## 不能证明

- 不能单独证明 ReadyBoost 曾实际启用。
- 不能单独证明设备最近连接或文件访问。
- 不存在该 key 不代表设备从未连接；SSD 系统或系统策略可能影响生成。

## 时间戳说明

`EMDMgmt` 子键 LastWrite 可作为 ReadyBoost/EMD 记录变化时间线索，但不能等同设备首次连接或最后连接时间。应与 `SetupAPI.dev.log`、`Enum\USB` 和事件日志交叉验证。

## 系统版本差异

ReadyBoost 从 Windows Vista 引入。部分资料指出 SSD 系统上 ReadyBoost 可能默认禁用；Windows 10/11 行为与字段完整性需按样本验证。

## 攻击滥用

攻击者通常不会利用 `EMDMgmt` 持久化。该 artifact 的实战价值主要是外接设备识别和卷信息补充。

## 检测思路

- 在外接设备调查中搜索与已知设备 ID、卷标或卷序列号匹配的 `EMDMgmt` 子键。
- 将 `EMDMgmt` 的设备 ID 与 `USBSTOR`、`SWD\WPDBUSENUM`、`VolumeInfoCache` 对齐。
- 对敏感主机出现未知外接存储相关 EMD 记录做低噪声补充信号。

## 常见误报

- 正常 USB 闪存盘、SD 卡、eSATA、FireWire、外置硬盘、非系统本地盘。
- ReadyBoost 性能评估、Windows 自动设备评估。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt" /s
    ```

=== "Offline"

    ```text
    Collect SOFTWARE hive and cross-check with SYSTEM hive USB records.
    ```

## 解析工具

- Registry Explorer
- RECmd
- RegRipper
- KAPE
- Velociraptor

## 交叉验证

- [USBSTOR](usbstor.md)
- [MountedDevices](mounteddevices.md)
- [VolumeInfoCache](volumeinfocache.md)
- [Portable Devices](portable-devices.md)
- `SetupAPI.dev.log`
- Partition diagnostic logs

## 示例结论

- `EMDMgmt` 中存在 `Disk&Ven_SanDisk...` 子键及卷标线索，可作为该外接存储曾被系统评估的辅助证据；连接时间需由其他来源确认。
- 该记录中的卷标与 `VolumeInfoCache\E:` 的 `VolumeLabel` 一致，可辅助解释某盘符曾关联的设备。

## 参考资料

- [artefacts.help: Registry - Devices and USB activity](https://artefacts.help/windows_registry_usb_activity.html)
- [Hacking Exposed Computer Forensics Blog: Understanding the artifacts EMDMgmt](https://www.hecfblog.com/2013/08/daily-blog-65-understanding-artifacts.html)

## 相关页面

- 场景：[USB 与外接设备](../../questions/usb.md)
- 注册表位置：[HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt](../../registry-tree/hklm/software/microsoft/windows-nt/currentversion/emdmgmt.md)

