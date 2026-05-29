# HKLM\SYSTEM\ControlSet00x\Control\ComputerName

`ComputerName` 保存计算机名相关配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\ComputerName` |
| 离线 | `SYSTEM\ControlSet00x\Control\ComputerName` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `ComputerName\ComputerName` | `REG_SZ` | 当前计算机名。 |
| `ActiveComputerName\ComputerName` | `REG_SZ` | 当前会话生效的计算机名。 |
| `ComputerName` | Key | 持久化配置。 |
| `ActiveComputerName` | Key | 当前运行状态相关配置。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Windows 安装、系统属性、重命名流程、域加入流程。 |
| 注意 | 改名后可能存在当前值和 active 值不一致；需结合事件日志或系统信息确认。 |

## 补充阅读

- 暂无专门 artifact 页面
- [Terminal Server Client](../../../../../artifacts/rdp/terminal-server-client.md)

