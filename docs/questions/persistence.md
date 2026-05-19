# 自启动与持久化

持久化调查关注的是“系统或用户登录时，哪些命令会被自动触发”。注册表是最常见入口之一，但不应忽略计划任务、启动目录、WMI、服务二进制和安全产品策略。

## 优先级

| 优先级 | Artifact | 主要价值 |
|---|---|---|
| 高 | [Run / RunOnce](../artifacts/persistence/run-keys.md) | 用户级和机器级登录启动 |
| 高 | [StartupApproved](../artifacts/persistence/startupapproved.md) | 启动项启用/禁用状态，解释 Run key 是否可能生效 |
| 高 | [Services](../artifacts/persistence/services.md) | 服务和驱动级持久化 |
| 高 | [IFEO](../artifacts/persistence/ifeo.md) | 调试器劫持、可执行文件劫持 |
| 高 | [Winlogon Userinit](../artifacts/persistence/winlogon-userinit.md) | 登录初始化链追加命令 |
| 高 | [Winlogon Shell](../artifacts/persistence/winlogon-shell.md) | 登录 Shell 替换或追加命令 |
| 高 | [LSA Authentication Packages](../artifacts/persistence/lsa-authentication-packages.md) | LSASS 加载链和凭据访问风险 |
| 高 | [Command Processor AutoRun](../artifacts/persistence/command-processor-autorun.md) | `cmd.exe` 启动自动命令 |

## 高信号特征

- 命令指向用户可写目录，例如 `%AppData%`、`%Temp%`、`Downloads`。
- 使用 `powershell.exe`、`wscript.exe`、`mshta.exe`、`rundll32.exe`、`regsvr32.exe`。
- value name 或 service name 伪装成系统组件。
- 路径不存在但注册表项残留。
- 命令行异常长、混淆、编码或包含远程下载。

## 判断边界

- Run key、Winlogon、LSA、Command Processor AutoRun 都首先证明“配置存在”。是否执行要结合登录、重启、cmd 启动、LSASS 模块加载或进程创建日志。
- StartupApproved 证明的是状态，不保存完整命令；必须回到 Run key 或 Startup Folder 查命令内容。
