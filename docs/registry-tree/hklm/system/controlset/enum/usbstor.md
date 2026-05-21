# HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR

`USBSTOR` 保存 USB Mass Storage 设备枚举信息。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR` |
| 离线 | `SYSTEM\ControlSet00x\Enum\USBSTOR` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

记录系统识别过的 USB 存储设备。子键通常可反映设备类型、厂商、产品、版本和序列号。

## 常见子键 / 值

| 名称 | 类型 | 含义 |
|---|---|---|
| `<DeviceType&Vendor&Product&Revision>` | Key | 设备类别、厂商、产品和版本组合。 |
| `<SerialOrInstanceId>` | Key | 设备序列号或实例 ID。 |
| `FriendlyName` | `REG_SZ` | 设备友好名称。 |
| `ParentIdPrefix` | `REG_SZ` | 与设备实例关联的前缀，部分设备存在。 |
| `ContainerID` | `REG_SZ` | 设备容器 ID，可用于关联同一物理设备的接口。 |

## 默认状态 / 常见状态

没有接入过 USB 存储设备的系统可能为空。正常 U 盘、移动硬盘、读卡器、手机 USB 存储模式和企业加密盘都可能留下记录。

## 版本差异

不同设备是否暴露稳定序列号取决于硬件和驱动。无唯一序列号的设备可能使用 Windows 生成的实例标识。

## 取证提示

该位置说明系统枚举过 USB 存储设备，不等于用户访问过文件，也不等于发生复制。连接时间和盘符关系需要结合 SetupAPI.dev.log、Partition/Diagnostic、MountedDevices、MountPoints2、LNK 和 Jump Lists。

## 相关场景

- [USB 与外接设备](../../../../../questions/usb.md)
- [常规注册表检查](../../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM Enum](index.md)
- [HKLM Enum USB](usb.md)
- [HKLM MountedDevices](../../mounteddevices.md)
- [HKCU MountPoints2](../../../../hkcu/software/microsoft/windows/currentversion/mountpoints2.md)
