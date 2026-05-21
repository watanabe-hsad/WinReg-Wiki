# HKEY_CURRENT_CONFIG

`HKEY_CURRENT_CONFIG`，简称 `HKCC`，是当前硬件 profile 的映射，不是独立 hive。

## 映射关系

| 视图 | 实际来源 |
|---|---|
| `HKCC` | `HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current` |
| 离线来源 | `C:\Windows\System32\Config\SYSTEM` |

离线分析时先通过 `SYSTEM\Select` 解析 `CurrentControlSet` 对应的 `ControlSet00x`。

## 常用路径

| 路径 | 含义 |
|---|---|
| `System\CurrentControlSet\Hardware Profiles\Current` | 当前硬件 profile。 |
| `System\CurrentControlSet\Enum` | 设备枚举，应优先回到 `SYSTEM` 树查看。 |
| `System\CurrentControlSet\Services` | 服务和驱动配置。 |

## 注意

| 项 | 说明 |
|---|---|
| 当前状态 | `HKCC` 主要反映 live 当前硬件 profile。 |
| 历史设备 | 历史设备调查优先看 `SYSTEM\Enum`、事件日志和设备安装日志。 |
| 离线文件 | 不存在单独的 `HKEY_CURRENT_CONFIG` hive。 |

## 相关 Artifact

[Services](../../artifacts/persistence/services.md),
[USBSTOR](../../artifacts/usb/usbstor.md),
[MountedDevices](../../artifacts/usb/mounteddevices.md)
