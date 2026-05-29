# HKLM\SOFTWARE\Microsoft\Windows Portable Devices

`Windows Portable Devices` 保存 WPD / MTP 等便携设备的部分元数据。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows Portable Devices` |
| Live 常见子路径 | `HKLM\SOFTWARE\Microsoft\Windows Portable Devices\Devices` |
| 离线 | `SOFTWARE\Microsoft\Windows Portable Devices` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Devices` | Key | 便携设备记录容器。 |
| `<device ID>` | Key | 单个便携设备记录。 |
| `FriendlyName` | `REG_SZ` | 设备显示名称；不一定存在。 |
| `<metadata value>` | `REG_*` | 具体字段随设备和系统版本变化。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | Windows Portable Devices、MTP/WPD 驱动、设备安装过程。 |
| 注意 | 该位置常与 `SWD\WPDBUSENUM` 互相印证；不能单独证明文件访问。 |

## 补充阅读

- [Portable Devices](../../../../artifacts/usb/portable-devices.md)
- [Enum SWD WPDBUSENUM](../../../../artifacts/usb/swd-wpdbusenum.md)

