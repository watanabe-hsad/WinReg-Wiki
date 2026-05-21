# HKLM\SYSTEM\ControlSet00x\Services\EventLog

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Services\EventLog` |
| 离线 | `SYSTEM\ControlSet00x\Services\EventLog` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

保存 Windows Event Log 服务下经典日志通道的注册表配置。这里是日志通道配置，不是 `.evtx` 日志内容本身。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Application` | Key | Application 日志配置。 | 常见通道 | 记录应用和服务事件。 |
| `System` | Key | System 日志配置。 | 常见通道 | 记录系统组件和服务事件。 |
| `Security` | Key | Security 日志配置。 | 常见通道 | 日志内容受审计策略影响。 |
| `File` | `REG_EXPAND_SZ` / `REG_SZ` | 日志文件路径。 | `%SystemRoot%\System32\Winevt\Logs\...` 常见 | 具体路径可被配置。 |
| `MaxSize` | `REG_DWORD` | 日志最大大小。 | 视系统和策略而定 | 值过小可能影响保留时间。 |
| `Retention` | `REG_DWORD` | 保留策略。 | 视配置而定 | 需结合通道实际配置解释。 |
| `AutoBackupLogFiles` | `REG_DWORD` | 自动备份旧日志配置。 | 视配置而定 | 常用于日志满时行为。 |

## 默认状态与版本差异

默认大小和保留策略随 Windows 版本、角色、域策略和安全基线变化。现代 Windows 还存在大量通道配置在其他位置和 `.evtx` 元数据中体现。

## 注意事项

- 这里不是日志内容，不能从该 key 直接判断某个事件是否发生。
- 日志大小和保留策略变化可能来自 GPO、安全基线或管理员配置。
- 离线分析时先用 `SYSTEM\Select` 确认当前控制集。

## 取证提示

- `MaxSize`、`Retention` 或 `AutoBackupLogFiles` 的异常变化可作为日志可见性调查线索。
- 需要结合 Security `1102`、`4719`、日志文件时间线、GPO 和 EDR tamper 事件验证。

## 相关场景

- [安全策略与防护配置](../../../../../questions/policy-security.md)
- [反取证与清理痕迹](../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../questions/registry-checklist.md)

## 相关位置

- [Services](index.md)
- [SECURITY](../../../security.md)
- [Policies](../../../software/policies.md)

## 补充阅读

- [Microsoft Learn: Event logging](https://learn.microsoft.com/en-us/windows/win32/eventlog/event-logging)
