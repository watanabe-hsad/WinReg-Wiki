# USB 与外接设备

## 检查目标

判断系统是否识别过 USB / 外接设备、卷和盘符如何映射，以及哪个用户可能见过该卷或共享。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [USBSTOR](../registry-tree/hklm/system/controlset/enum/usbstor.md) | USB 存储设备枚举、厂商、产品、序列号。 | 不证明用户访问文件。 |
| [USB](../registry-tree/hklm/system/controlset/enum/usb.md) | USB 总线设备枚举。 | 覆盖非存储 USB，但语义更偏设备层。 |
| [SWD\WPDBUSENUM](../registry-tree/hklm/system/controlset/enum/swd-wpdbusenum.md) | WPD / MTP 设备枚举。 | 适合手机、相机、便携媒体设备。 |
| [DeviceClasses](../registry-tree/hklm/system/controlset/control/deviceclasses.md) | 设备接口类和实例路径。 | 需要关联具体接口 GUID。 |
| [MountedDevices](../registry-tree/hklm/system/mounteddevices.md) | 卷 GUID、盘符、设备映射。 | 盘符可复用。 |
| [MountPoints2](../registry-tree/hkcu/software/microsoft/windows/currentversion/mountpoints2.md) | 用户见过的卷、盘符或网络共享。 | 用户层记录，不证明复制。 |
| [Portable Devices](../registry-tree/hklm/software/microsoft/windows-portable-devices.md) | Windows Portable Devices 元数据。 | 辅助识别设备显示名和 WPD 关系。 |
| [EMDMgmt](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/emdmgmt.md) | ReadyBoost / 外接存储辅助记录。 | 不应单独作为连接或访问结论。 |
| [VolumeInfoCache](../registry-tree/hklm/software/microsoft/windows-search/volumeinfocache.md) | Windows Search 卷信息缓存。 | 辅助卷信息，需交叉验证。 |

## 判断要点

- 先区分设备枚举、卷映射、用户见过卷和文件访问四类证据。
- USBSTOR、USB、SWD、DeviceClasses 可互相补足设备层关系。
- MountedDevices 可帮助关联卷 GUID 和盘符，但盘符可能复用。
- MountPoints2、LNK、Jump Lists、RecentDocs 更接近用户视角。

## 交叉验证

- `SetupAPI.dev.log`、`Microsoft-Windows-Partition/Diagnostic`。
- `Microsoft-Windows-DriverFrameworks-UserMode/Operational`、Kernel-PnP、DeviceSetupManager。
- LNK、Jump Lists、RecentDocs、ShellBags、MountPoints2。
- `$MFT`、`$UsnJrnl`、文件访问审计、EDR removable media telemetry。

## 常见误判

- 设备枚举不等于文件复制。
- MTP 设备不一定出现在 USBSTOR。
- 同一盘符可能在不同时间指向不同卷。
- 企业加密盘、备份盘、手机、读卡器和同步软件都可能留下正常记录。

## 相关场景

- [Shell / Explorer 用户行为](shell-explorer.md)
- [常规注册表检查](registry-checklist.md)

## 补充阅读

- [USBSTOR artifact](../artifacts/usb/usbstor.md)
- [USB artifact](../artifacts/usb/usb.md)
- [MountedDevices artifact](../artifacts/usb/mounteddevices.md)
- [MountPoints2 artifact](../artifacts/usb/mountpoints2.md)
- [Portable Devices artifact](../artifacts/usb/portable-devices.md)
