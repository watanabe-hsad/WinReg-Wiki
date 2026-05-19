---
tags:
  - USB
  - Device
  - SYSTEM
---

# USBSTOR

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">设备枚举</span>
</div>

`USBSTOR` 记录 USB 存储设备枚举信息，常用于识别某台主机是否识别过特定 USB 存储设备。

## Registry Paths

| Hive | Path |
|---|---|
| `HKLM\SYSTEM` | `ControlSet00x\Enum\USBSTOR` |

## Forensic Meaning

子键通常包含设备类型、厂商、产品、版本和序列号。它能帮助把某个物理设备和主机联系起来。

## What It Can Prove

- 系统曾枚举过某个 USB 存储设备。
- 可提取厂商、产品、版本、序列号等信息。
- 可与 MountedDevices 和事件日志关联盘符与连接时间。

## What It Cannot Prove

- 用户一定访问过设备中的文件。
- 一定发生了文件复制。
- LastWrite 一定等于首次连接或最后连接时间。

## Detection Ideas

- 非授权 USB 存储设备。
- 首次出现时间和敏感文件访问时间接近。
- 同一序列号出现在多台主机。

## Cross Validation

- [MountedDevices](mounteddevices.md)
- `SetupAPI.dev.log`
- Partition diagnostic logs
- LNK and Jump Lists
- `$MFT` and `$UsnJrnl`

