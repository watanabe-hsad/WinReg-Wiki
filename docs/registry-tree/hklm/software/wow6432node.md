# HKLM\SOFTWARE\WOW6432Node

`WOW6432Node` 是 64 位 Windows 上 32 位应用的注册表重定向视图。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\WOW6432Node` |
| 离线 | `SOFTWARE\WOW6432Node` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Microsoft\Windows\CurrentVersion\Run` | Key | 32 位视图下的机器级启动项。 |
| `Microsoft\Windows\CurrentVersion\Uninstall` | Key | 32 位软件安装登记。 |
| `Classes` | Key | 32 位 COM / 文件关联相关视图。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | 32 位安装器、32 位应用、WOW64 注册表重定向。 |
| 注意 | 分析 Run、Uninstall、COM 时应同时检查 64 位和 32 位视图。 |

## 补充阅读

- [Run / RunOnce](../../../artifacts/persistence/run-keys.md)
- [IFEO](../../../artifacts/persistence/ifeo.md)
- [Amcache](../../../artifacts/execution/amcache.md)

