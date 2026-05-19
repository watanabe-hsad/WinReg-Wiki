# HKLM\SYSTEM\MountedDevices

`MountedDevices` 保存卷标识、卷 GUID 和 DOS 盘符之间的映射。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\MountedDevices` |
| 离线 | `SYSTEM\MountedDevices` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `\DosDevices\C:` | `REG_BINARY` | DOS 盘符到卷或设备的二进制映射。 |
| `\??\Volume{GUID}` | `REG_BINARY` | 卷 GUID 到设备标识的映射。 |
| `\DosDevices\<letter>:` | `REG_BINARY` | 其他盘符映射。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Mount Manager。 |
| 注意 | 盘符可复用；分析时应同时保留卷 GUID、设备序列和时间线。 |

## 相关 Artifact

- [MountedDevices](../../../artifacts/usb/mounteddevices.md)
- [USBSTOR](../../../artifacts/usb/usbstor.md)
- [MountPoints2](../../../artifacts/usb/mountpoints2.md)

