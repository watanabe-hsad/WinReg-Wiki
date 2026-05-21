# HKLM\SYSTEM\ControlSet00x\Enum

`Enum` 保存即插即用设备枚举树，包括 USB、存储、显示、网络等设备类别。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Enum` |
| 离线 | `SYSTEM\ControlSet00x\Enum` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `USB` | Key | USB 设备枚举。 |
| [`USBSTOR`](usbstor.md) | Key | USB mass storage 设备枚举。 |
| `SWD\WPDBUSENUM` | Key | Windows Portable Device 相关枚举。 |
| `DeviceDesc` | `REG_SZ` / `REG_EXPAND_SZ` | 设备描述。 |
| `FriendlyName` | `REG_SZ` | 友好名称。 |
| `HardwareID` | `REG_MULTI_SZ` | 硬件 ID 列表。 |
| `ContainerID` | `REG_SZ` | 设备容器 ID。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Plug and Play Manager、设备驱动。 |
| 注意 | 设备枚举说明系统识别过设备，不等于用户访问过设备中的文件。 |

## 相关场景

- [USB 与外接设备](../../../../../questions/usb.md)
- [常规注册表检查](../../../../../questions/registry-checklist.md)

## 补充阅读

- [USBSTOR](../../../../../artifacts/usb/usbstor.md)
- [USB](../../../../../artifacts/usb/usb.md)
- [Enum SWD WPDBUSENUM](../../../../../artifacts/usb/swd-wpdbusenum.md)
- [DeviceClasses](../../../../../artifacts/usb/deviceclasses.md)
- [MountedDevices](../../../../../artifacts/usb/mounteddevices.md)
- [MountPoints2](../../../../../artifacts/usb/mountpoints2.md)
