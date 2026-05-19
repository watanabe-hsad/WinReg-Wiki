---
tags:
  - USB
  - Volume
  - SYSTEM
---

# MountedDevices

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">盘符映射</span>
</div>

`MountedDevices` 保存卷标识和盘符映射线索，常与 USBSTOR 一起用于还原外接存储设备的盘符分配情况。

## Registry Paths

| Hive | Path |
|---|---|
| `HKLM\SYSTEM` | `MountedDevices` |

## Forensic Meaning

value name 可能形如 `\DosDevices\E:` 或 `\??\Volume{GUID}`，value data 中可能包含磁盘签名、卷序列或设备标识信息。

## What It Can Prove

- 系统中存在过某些卷和盘符映射。
- 可辅助关联 USB 设备和盘符。

## What It Cannot Prove

- 设备连接的精确时间。
- 用户访问过盘符中的具体文件。
- 当前盘符一定仍然相同。

## Cross Validation

- [USBSTOR](usbstor.md)
- MountPoints2
- Event Log
- LNK and Jump Lists
- ShellBags

