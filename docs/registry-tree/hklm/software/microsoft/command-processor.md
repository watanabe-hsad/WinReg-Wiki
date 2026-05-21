# HKLM\SOFTWARE\Microsoft\Command Processor

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Command Processor` |
| 离线 | `SOFTWARE\Microsoft\Command Processor` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存机器级 `cmd.exe` 配置。这里的 `AutoRun` 可在命令处理器启动时运行指定命令，影响范围比 HKCU 用户级配置更大。实际是否触发取决于启动方式、命令行参数和运行上下文。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `AutoRun` | `REG_SZ` / `REG_EXPAND_SZ` | `cmd.exe` 启动时自动执行的机器级命令。 | 默认通常不存在 | 使用 `cmd.exe /D` 可跳过 AutoRun。 |
| `CompletionChar` | `REG_DWORD` | 命令补全字符配置。 | 视配置而定 | 通常不是安全事件。 |
| `DefaultColor` | `REG_DWORD` | 默认控制台颜色。 | 视配置而定 | 影响显示。 |
| `EnableExtensions` | `REG_DWORD` | 命令扩展配置。 | 视配置而定 | 影响命令处理器行为。 |

## 默认状态与版本差异

默认状态通常没有 `AutoRun` value。`cmd.exe` 的 AutoRun 语义长期存在，但具体环境可能受策略、启动参数和终端程序影响。

## 注意事项

- `AutoRun` 存在只能证明机器级命令处理器配置存在，不证明已经触发。
- 机器级值通常需要管理员权限写入；仍需结合写入主体、时间线和进程证据判断。
- 开发工具、运维初始化脚本或终端增强工具可能合法设置该值。

## 取证提示

- 非空 `AutoRun` 指向用户可写目录、脚本解释器、网络路径或下载执行命令时，需要检查进程创建日志。
- 同时检查 HKCU 用户级 Command Processor，避免只看到机器级配置。

## 相关场景

- [自启动与持久化](../../../../questions/persistence.md)
- [程序执行痕迹](../../../../questions/execution.md)
- [反取证与清理痕迹](../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU Command Processor](../../../hkcu/software/microsoft/command-processor.md)
- [HKLM SOFTWARE](../index.md)
- [HKLM Environment](../../system/controlset/control/session-manager/environment.md)

## 补充阅读

- [Command Processor AutoRun artifact](../../../../artifacts/persistence/command-processor-autorun.md)
- [Microsoft Learn: cmd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)
