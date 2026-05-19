# USB 与外接设备

USB 调查通常要回答三个问题：设备是否出现过、何时连接过、是否发生文件访问或拷贝。注册表主要解决前两个问题的一部分。

## 优先级

| 优先级 | Artifact | 主要价值 |
|---|---|---|
| 高 | [USB](../artifacts/usb/usb.md) | USB 总线层面的设备枚举，覆盖范围比 USBSTOR 更广 |
| 高 | [USBSTOR](../artifacts/usb/usbstor.md) | USB 存储设备枚举、厂商、产品、序列号 |
| 高 | [Enum SWD WPDBUSENUM](../artifacts/usb/swd-wpdbusenum.md) | WPD / MTP 设备枚举，例如手机、相机、便携媒体设备 |
| 高 | [MountedDevices](../artifacts/usb/mounteddevices.md) | 卷标识与盘符映射线索 |
| 高 | [MountPoints2](../artifacts/usb/mountpoints2.md) | 用户 SID 维度见过的卷、盘符或网络位置 |
| 中 | [DeviceClasses](../artifacts/usb/deviceclasses.md) | 设备接口类与实例路径，适合连接 USB / 卷 / WPD 线索 |
| 中 | [Portable Devices](../artifacts/usb/portable-devices.md) | Windows Portable Devices 元数据 |
| 中 | [EMDMgmt](../artifacts/usb/emdmgmt.md) | ReadyBoost / 外接存储辅助记录 |
| 中 | [VolumeInfoCache](../artifacts/usb/volumeinfocache.md) | Windows Search 记录的卷信息缓存 |

## 交叉验证

- `Microsoft-Windows-Partition/Diagnostic`
- `Microsoft-Windows-DriverFrameworks-UserMode/Operational`
- `SetupAPI.dev.log`
- `DeviceSetupManager`、`Kernel-PnP`、Windows Portable Devices 相关日志
- LNK、Jump Lists、RecentDocs
- `$MFT`、`$UsnJrnl`、ShellBags

## 结论写法

- `USBSTOR` 更偏设备枚举，`MountedDevices` 更偏卷和盘符映射，`MountPoints2` 更偏用户 Shell 是否见过该卷。
- `USB` 和 `DeviceClasses` 能补足非存储 USB 或接口关系；`SWD\WPDBUSENUM` 和 `Portable Devices` 更适合手机、相机、MTP 设备。
- `EMDMgmt`、`VolumeInfoCache` 更适合作为辅助线索，不应单独作为 USB 插入或文件访问结论。
- 要证明文件复制，必须加入 LNK、Jump Lists、RecentDocs、ShellBags、文件系统日志或 EDR removable media 事件。
