# HKLM\SYSTEM\ControlSet00x\Control\Print\Monitors

`Print\Monitors` 保存打印端口监视器配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors` |
| 离线 | `SYSTEM\ControlSet00x\Control\Print\Monitors` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `<MonitorName>` | Key | 单个打印端口监视器。 |
| `Driver` | `REG_SZ` | 监视器 DLL 名或路径。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | 打印机驱动、Spooler、打印管理工具、安装程序。 |
| 注意 | 配置存在不等于 DLL 已加载；加载状态需结合 Spooler 运行时证据。 |

## 相关 Artifact

- [Print Monitors](../../../artifacts/persistence/print-monitors.md)
- [Services](../../../artifacts/persistence/services.md)

