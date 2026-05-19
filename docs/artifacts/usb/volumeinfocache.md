---
tags:
  - USB
  - Volume
  - SOFTWARE
  - HKLM
---

# VolumeInfoCache

<div class="rfh-meta" markdown>
<span class="rfh-badge medium">取证价值 中</span>
<span class="rfh-badge low">检测价值 低</span>
<span class="rfh-badge">卷信息缓存</span>
</div>

## 摘要

`VolumeInfoCache` 记录 Windows Search 维护的盘符到卷信息缓存，可用于补充卷标、盘符和最近关联线索。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows Search\VolumeInfoCache` | N/A | 机器级 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows Search\VolumeInfoCache` | N/A | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SOFTWARE\Microsoft\Windows Search\VolumeInfoCache`。常见子键按盘符组织，例如 `C:`、`E:`。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SOFTWARE`。该 artifact 与 Windows Search 相关，不是所有系统或所有盘符都会有完整记录。

## 字段含义

| 字段 | 含义 |
|---|---|
| `<DriveLetter>:` | 盘符子键，例如 `E:`。 |
| `VolumeLabel` | 卷标或 friendly name。 |
| `DriveType` | 驱动器类型；具体数值需结合样本解释。 |
| 其他缓存值 | Windows Search 维护的卷缓存属性，语义待验证。 |

## 取证含义

`VolumeInfoCache` 可帮助回答“某个盘符最近对应过什么卷标”。它适合与 `MountedDevices`、`MountPoints2`、LNK 中的 volume information 交叉使用。

## 可以证明

- Windows Search 记录过某盘符与某卷信息的关联。
- 可辅助还原盘符和卷标关系。
- 可作为外接存储时间线的补充线索。

## 不能证明

- 不能单独证明设备连接、拔出或文件访问。
- 不能保证记录覆盖所有卷或所有 Windows 版本。
- 不能把盘符子键 LastWrite 直接解释为用户访问文件的时间。

## 时间戳说明

盘符子键 LastWrite 可作为该盘符卷信息缓存更新线索。它通常更接近“卷与盘符缓存被更新”的时间，不是文件访问时间。

## 系统版本差异

主要与 Windows Search 行为相关。Windows 7/10/11 具体字段和写入时机待验证；若 Windows Search 被禁用或索引行为不同，记录可能缺失。

## 攻击滥用

攻击者通常不直接使用此 key。该 artifact 主要用于补充外接设备和卷映射调查。

## 检测思路

- 在敏感主机上将新增或变更的非系统盘符缓存与 USB/外接设备记录关联。
- 用 `VolumeLabel` 反查 LNK、Jump Lists、RecentDocs 或文件系统时间线。
- 作为低噪声辅助信号，不建议单独告警。

## 常见误报

- 正常本地磁盘、外接硬盘、USB 闪存盘、网络同步盘、备份盘、VHD/VHDX。
- Windows Search 索引重建或系统维护。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SOFTWARE\Microsoft\Windows Search\VolumeInfoCache" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows Search\VolumeInfoCache" /s
    ```

=== "Offline"

    ```text
    Collect SOFTWARE hive; compare with SYSTEM\MountedDevices and user NTUSER.DAT MountPoints2.
    ```

## 解析工具

- Registry Explorer
- RECmd
- RegRipper
- KAPE
- Velociraptor

## 交叉验证

- [MountedDevices](mounteddevices.md)
- [MountPoints2](mountpoints2.md)
- [USBSTOR](usbstor.md)
- LNK volume information
- Jump Lists
- `$MFT` / `$UsnJrnl`

## 示例结论

- `VolumeInfoCache\E:` 的 `VolumeLabel` 显示 `KINGSTON`，可辅助说明 `E:` 曾与该卷标关联；是否为同一物理设备需结合 `MountedDevices` 和 USB 序列号。
- 该盘符子键 LastWrite 与 `MountedDevices` 变更接近，可作为卷映射时间线的补充，不能单独证明文件访问。

## 参考资料

- [artefacts.help: Registry - Devices and USB activity](https://artefacts.help/windows_registry_usb_activity.html)
- [Microsoft Learn: Troubleshoot Windows Search performance](https://learn.microsoft.com/en-us/troubleshoot/windows-client/shell-experience/windows-search-performance-issues)

## 相关页面

- 场景：[USB 与外接设备](../../questions/usb.md)
- 注册表位置：[HKLM\SOFTWARE\Microsoft\Windows Search\VolumeInfoCache](../../registry-tree/hklm/software/volumeinfocache.md)
