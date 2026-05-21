# HKCU\Software\Microsoft\Command Processor

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Command Processor` |
| 用户 SID | `HKU\<SID>\Software\Microsoft\Command Processor` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Command Processor` |

## 离线位置

`C:\Users\<User>\NTUSER.DAT`

## 作用

保存当前用户的 `cmd.exe` 配置。`AutoRun` 值会在命令处理器启动时执行指定命令；启动 `cmd.exe` 时使用 `/D` 可禁用 AutoRun 处理。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `AutoRun` | `REG_SZ` / `REG_EXPAND_SZ` | `cmd.exe` 启动时自动执行的命令。 | 默认通常不存在 | 用户级持久化或环境初始化线索。 |
| `CompletionChar` | `REG_DWORD` | 文件名补全触发字符。 | 视配置而定 | 影响交互体验。 |
| `DefaultColor` | `REG_DWORD` | 默认控制台颜色。 | 视配置而定 | 通常取证意义有限。 |
| `DelayedExpansion` | `REG_DWORD` | 延迟变量扩展开关。 | 视配置而定 | 也可通过命令行参数控制。 |
| `EnableExtensions` | `REG_DWORD` | 命令扩展开关。 | 视配置而定 | 也可通过命令行参数控制。 |

## 默认状态与版本差异

多数用户没有 `AutoRun` 值。`cmd.exe` 的实际行为还受命令行参数、组策略和机器级同名位置影响。

## 注意事项

- `AutoRun` 配置存在不等于命令已经执行；需要确认是否启动过 `cmd.exe`。
- 该页面是用户级位置；机器级 `HKLM\Software\Microsoft\Command Processor` 也可能存在。
- `AutoRun` 命令可能用于正常环境初始化、开发工具、企业脚本或恶意持久化。

## 取证提示

- 检查 `AutoRun` 是否指向用户可写目录、网络路径、解释器或脚本。
- 与进程创建日志、ConsoleHost / PowerShell 历史、Prefetch、文件系统时间线交叉验证。

## 相关场景

- [自启动与持久化](../../../../questions/persistence.md)
- [程序执行痕迹](../../../../questions/execution.md)
- [反取证与清理痕迹](../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU Software](../index.md)
- [HKCU Environment](../../environment.md)
- [HKLM Run / RunOnce](../../../hklm/software/microsoft/windows/currentversion/run.md)

## 补充阅读

- [Command Processor AutoRun artifact](../../../../artifacts/persistence/command-processor-autorun.md)
- [Microsoft Learn: cmd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)
