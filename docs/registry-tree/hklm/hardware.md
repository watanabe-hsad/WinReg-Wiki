# HKLM\HARDWARE

`HKLM\HARDWARE` 通常由系统启动时动态生成，反映当前硬件枚举结果。

## 来源

| 项 | 说明 |
|---|---|
| Live view | `HKLM\HARDWARE` |
| 离线来源 | 通常没有单独 hive；回到 `SYSTEM\Enum`、`SYSTEM\Services`、Hardware Profiles。 |

## 常用路径

| 路径 | 含义 |
|---|---|
| `DESCRIPTION` | 当前硬件描述。 |
| `DEVICEMAP` | 当前设备映射。 |
| `RESOURCEMAP` | 硬件资源映射。 |

## 注意

| 项 | 说明 |
|---|---|
| 动态视图 | 适合 live triage，不适合作为历史设备连接的主要证据。 |
| 历史设备 | 优先看 `SYSTEM\Enum`、`USBSTOR`、设备安装日志和事件日志。 |

## 相关 Artifact

[USBSTOR](../../artifacts/usb/usbstor.md),
[MountedDevices](../../artifacts/usb/mounteddevices.md)
