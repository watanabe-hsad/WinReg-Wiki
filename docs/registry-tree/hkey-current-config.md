# HKEY_CURRENT_CONFIG

`HKEY_CURRENT_CONFIG` 通常是 `HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current` 的映射。它反映当前硬件 profile 的有效配置，不是单独的离线 hive。

## Windows 原生视图

在 `regedit.exe` 中从 `HKEY_CURRENT_CONFIG` 展开。常见内容包括显示、打印、系统当前硬件 profile 相关配置。它适合核对 live 当前状态，但多数 DFIR 问题仍应回到 `HKLM\SYSTEM` 的 ControlSet 结构。

## 离线 hive 文件来源

| 逻辑来源 | 离线文件 | 备注 |
|---|---|---|
| `HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current` | `C:\Windows\System32\Config\SYSTEM` | 离线时先用 `SYSTEM\Select` 确认 CurrentControlSet |

## 典型取证价值

- 辅助判断当前硬件 profile、显示和设备配置状态。
- 在设备、驱动、显示配置异常调查中提供当前视图线索。
- 与 `HKLM\SYSTEM\ControlSet00x\Enum`、`Services` 一起确认设备和驱动状态。

## 典型检测价值

- 价值通常低于 `SYSTEM\Services`、`Enum`、`Control` 等持久路径。
- 可用于发现异常硬件 profile 配置变化，但检测规则应优先监控真实来源路径。

## 常见误判

- 把 `HKCC` 当成独立 hive 文件。
- 只看当前硬件 profile，忽略其他 `ControlSet00x` 或历史 profile。
- 将显示、打印或驱动正常配置调整误判为攻击活动。

## 重点子路径

| 子路径 | 用途 | 调查提示 |
|---|---|---|
| `System\CurrentControlSet\Hardware Profiles\Current` | 当前硬件 profile | 回到 `SYSTEM` hive 核对 |
| `System\CurrentControlSet\Enum` | 设备枚举 | 与 USB、驱动日志交叉验证 |
| `System\CurrentControlSet\Services` | 服务和驱动 | 关注持久化与驱动加载 |

## 关联 artifact 页面

- [Services](../artifacts/persistence/services.md)
- [USBSTOR](../artifacts/usb/usbstor.md)
- [MountedDevices](../artifacts/usb/mounteddevices.md)

## References

- [Microsoft Learn: Registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)
- [Microsoft Learn: Predefined keys](https://learn.microsoft.com/en-us/windows/win32/sysinfo/predefined-keys)
