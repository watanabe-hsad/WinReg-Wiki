# USB 与外接设备

USB 调查通常要回答三个问题：设备是否出现过、何时连接过、是否发生文件访问或拷贝。注册表主要解决前两个问题的一部分。

## 优先级

| 优先级 | Artifact | 主要价值 |
|---|---|---|
| 高 | [USBSTOR](../artifacts/usb/usbstor.md) | USB 存储设备枚举、厂商、产品、序列号 |
| 高 | [MountedDevices](../artifacts/usb/mounteddevices.md) | 卷标识与盘符映射线索 |
| 高 | [MountPoints2](../artifacts/usb/mountpoints2.md) | 用户 SID 维度见过的卷、盘符或网络位置 |

## 交叉验证

- `Microsoft-Windows-Partition/Diagnostic`
- `Microsoft-Windows-DriverFrameworks-UserMode/Operational`
- `SetupAPI.dev.log`
- LNK、Jump Lists、RecentDocs
- `$MFT`、`$UsnJrnl`、ShellBags

## 结论写法

- `USBSTOR` 更偏设备枚举，`MountedDevices` 更偏卷和盘符映射，`MountPoints2` 更偏用户 Shell 是否见过该卷。
- 要证明文件复制，必须加入 LNK、Jump Lists、RecentDocs、ShellBags、文件系统日志或 EDR removable media 事件。
