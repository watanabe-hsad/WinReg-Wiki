# HKLM\SYSTEM\ControlSet00x

`ControlSet00x` 是 Windows 保存系统控制配置的真实控制集，`CurrentControlSet` 是运行时映射。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet` |
| 离线 | `SYSTEM\ControlSet001`、`SYSTEM\ControlSet002` 等 |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Control` | Key | 系统控制配置，例如 LSA、Terminal Server、TimeZoneInformation、ComputerName。 |
| `Enum` | Key | 设备枚举树。 |
| `Services` | Key | 服务、驱动和网络组件配置。 |
| `Hardware Profiles` | Key | 硬件配置 profile；`HKCC` 通常映射到其中的 current profile。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Windows 启动过程、服务控制管理器、PnP、驱动、系统配置工具。 |
| 注意 | 多个 `ControlSet00x` 可能并存；需要用 `Select\Current` 判断当前控制集。 |

## 相关 Artifact

- [Services](../../../../artifacts/persistence/services.md)
- [fDenyTSConnections](../../../../artifacts/rdp/fdenytsconnections.md)
- [RDP-Tcp PortNumber](../../../../artifacts/rdp/rdp-tcp-portnumber.md)

