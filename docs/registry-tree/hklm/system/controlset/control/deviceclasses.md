# HKLM\SYSTEM\ControlSet00x\Control\DeviceClasses

`DeviceClasses` 保存设备接口类和接口实例的注册信息。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\DeviceClasses` |
| 离线 | `SYSTEM\ControlSet00x\Control\DeviceClasses` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `{InterfaceClassGuid}` | Key | 设备接口类 GUID。 |
| `<interface instance>` | Key | 具体接口实例，名称中可能包含设备实例路径。 |
| `DeviceInstance` | `REG_SZ` | 关联设备实例路径；不一定存在。 |
| `SymbolicLink` | `REG_SZ` / Key 名 | 设备接口符号链接或其组成部分。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Plug and Play、驱动安装程序、设备接口注册。 |
| 注意 | 接口类 GUID 本身不是唯一物理设备；需与 `Enum`、`USBSTOR`、`MountedDevices` 关联。 |

## 补充阅读

- [DeviceClasses](../../../../../artifacts/usb/deviceclasses.md)
- [USB](../../../../../artifacts/usb/usb.md)
- [MountedDevices](../../../../../artifacts/usb/mounteddevices.md)

