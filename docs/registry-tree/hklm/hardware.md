# HKLM\HARDWARE

`HKLM\HARDWARE` 通常由系统启动时动态生成，反映当前硬件检测结果。它更适合 live triage，不是常规离线 hive 调查的主入口。

## Windows 原生视图

在 live 系统中路径为 `HKLM\HARDWARE`，常见子路径包括 `DESCRIPTION`、`DEVICEMAP`、`RESOURCEMAP`。这些内容主要反映当前硬件环境和系统启动时枚举结果。

## 离线 hive 文件来源

| 逻辑视图 | 离线来源 |
|---|---|
| `HKLM\HARDWARE` | 通常没有单独持久 hive；离线分析回到 `SYSTEM` 的 `Enum`、`Services`、Hardware Profiles |

## 典型取证价值

- 在 live 响应中辅助确认当前硬件、串口、磁盘和设备映射。
- 与 `SYSTEM\Enum`、设备日志和驱动信息核对当前状态。

## 典型检测价值

- 常规检测价值低于 `SYSTEM` 中的持久设备与驱动路径。
- 若需要监控硬件变化，优先使用事件日志、EDR 设备事件和 `SYSTEM\Enum`。

## 常见误判

- 把动态硬件视图当作持久证据。
- 用 `HKLM\HARDWARE` 证明历史设备连接，证据强度不足。
- 忽略虚拟机、云主机和热插拔设备对当前视图的影响。

## 重点子路径

| 子路径 | 用途 |
|---|---|
| `DESCRIPTION` | 当前硬件描述 |
| `DEVICEMAP` | 当前设备映射 |
| `RESOURCEMAP` | 硬件资源映射 |

## 关联 artifact 页面

- [USBSTOR](../../artifacts/usb/usbstor.md)
- [MountedDevices](../../artifacts/usb/mounteddevices.md)

## References

- [Microsoft Learn: Registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)
