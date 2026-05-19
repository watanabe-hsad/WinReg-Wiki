# HKLM\SYSTEM\ControlSet00x\Enum\USB

`Enum\USB` 保存 USB 总线层面枚举到的设备实例。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Enum\USB` |
| 离线 | `SYSTEM\ControlSet00x\Enum\USB` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `VID_xxxx&PID_yyyy` | Key | USB vendor ID 和 product ID 分组。 |
| `<instance ID>` | Key | 设备实例，可能包含序列号或父级生成 ID。 |
| `DeviceDesc` | `REG_SZ` | 设备描述字符串。 |
| `FriendlyName` | `REG_SZ` | 友好名称；不一定存在。 |
| `HardwareID` | `REG_MULTI_SZ` | 硬件 ID 列表。 |
| `ContainerID` | `REG_SZ` | 设备容器 ID，可用于关联同一物理设备的多个接口。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Plug and Play、USB 驱动栈、设备安装过程。 |
| 注意 | 该路径不只包含存储设备；存储设备还需看 `USBSTOR`、卷和用户级 artifact。 |

## 相关 Artifact

- [USB](../../../artifacts/usb/usb.md)
- [USBSTOR](../../../artifacts/usb/usbstor.md)
- [Enum SWD WPDBUSENUM](../../../artifacts/usb/swd-wpdbusenum.md)

