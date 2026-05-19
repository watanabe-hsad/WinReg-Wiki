# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt

`EMDMgmt` 保存 External Memory Device / ReadyBoost 相关设备元数据。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `<device or volume key>` | Key | 外接存储或 ReadyBoost 相关设备记录。 |
| `FriendlyName` | `REG_SZ` | 友好名称；不一定存在。 |
| `LastUsedTime` | `REG_BINARY` / 待验证 | 某些解析资料提到的时间字段；语义需按工具和版本确认。 |
| `<metadata value>` | `REG_*` | 设备能力、缓存或卷元数据；具体字段随版本变化。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | Windows ReadyBoost / External Memory Device 组件。 |
| 注意 | 该 key 不一定存在；它是辅助线索，不应代替 `USBSTOR`、`MountedDevices`、`MountPoints2`。 |

## 相关 Artifact

- [EMDMgmt](../../../artifacts/usb/emdmgmt.md)
- [MountedDevices](../../../artifacts/usb/mounteddevices.md)
- [MountPoints2](../../../artifacts/usb/mountpoints2.md)

