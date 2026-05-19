# HKLM\SYSTEM\ControlSet00x\Enum\SWD\WPDBUSENUM

`SWD\WPDBUSENUM` 保存 Windows Portable Devices 相关设备枚举记录。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Enum\SWD\WPDBUSENUM` |
| 离线 | `SYSTEM\ControlSet00x\Enum\SWD\WPDBUSENUM` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `<device instance>` | Key | WPD 设备实例。 |
| `FriendlyName` | `REG_SZ` | 设备友好名称。 |
| `ContainerID` | `REG_SZ` | 可与 USB、DeviceClasses、Portable Devices 关联。 |
| `ParentIdPrefix` | `REG_SZ` | 父级 ID 前缀；并非所有设备都有。 |
| `DeviceDesc` | `REG_SZ` | 设备描述。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Windows Portable Devices、MTP/WPD 驱动、Plug and Play。 |
| 注意 | 常见于手机、相机、MTP 设备；不是所有 USB 存储都会出现。 |

## 相关 Artifact

- [Enum SWD WPDBUSENUM](../../../artifacts/usb/swd-wpdbusenum.md)
- [Portable Devices](../../../artifacts/usb/portable-devices.md)
- [USB](../../../artifacts/usb/usb.md)

