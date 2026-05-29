# HKLM\SYSTEM\Select

`HKLM\SYSTEM\Select` 记录 `CurrentControlSet` 与真实 `ControlSet00x` 的映射关系。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\Select` |
| 离线 | `SYSTEM\Select` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Current` | `REG_DWORD` | 当前启动后映射为 `CurrentControlSet` 的控制集编号。 |
| `Default` | `REG_DWORD` | 下次启动默认使用的控制集编号。 |
| `Failed` | `REG_DWORD` | 最近一次失败启动相关控制集；为 `0` 时通常表示无记录。 |
| `LastKnownGood` | `REG_DWORD` | 上一次已知良好配置对应的控制集编号。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Windows 启动过程。 |
| 注意 | 离线分析时不要直接假设 `ControlSet001` 是当前配置，应先读取 `Select\Current`。 |

## 补充阅读

- [Services](../../../artifacts/persistence/services.md)
- [BAM / DAM](../../../artifacts/execution/bam-dam.md)
- [USBSTOR](../../../artifacts/usb/usbstor.md)

