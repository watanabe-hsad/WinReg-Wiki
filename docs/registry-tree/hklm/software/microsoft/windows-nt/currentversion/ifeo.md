# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存按可执行文件名生效的进程启动、调试和诊断配置。常见调查重点是 `<ImageName>\Debugger`，它可改变目标程序启动时调用的命令。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `<ImageName>` | Key | 目标可执行文件名。 | `notepad.exe` 等 | 名称仅按映像名匹配。 |
| `Debugger` | `REG_SZ` | 目标进程启动时调用的调试器命令。 | 调试器路径或命令行 | 可用于调试，也可被滥用。 |
| `GlobalFlag` | `REG_DWORD` | 调试 / 诊断标志。 | 视工具而定 | 需结合上下文解释。 |
| `SilentProcessExit` | Key | 静默进程退出监控相关配置。 | 子键和值 | 需结合 MonitorProcess 等字段。 |

## 默认状态与版本差异

普通系统可能存在少量合法 IFEO 项。开发机、测试机、EDR 或诊断工具环境会出现更多配置。具体字段随 Windows 版本和工具变化。

## 注意事项

- IFEO 配置存在不等于目标程序已启动。
- `Debugger` 指向命令不等于命令成功执行。
- 辅助功能程序、浏览器、安全工具和系统工具的 IFEO 项需要重点解释，但仍需排除合法调试/EDR。

## 取证提示

- 关注 `Debugger` 指向用户可写目录、脚本解释器、未知二进制或用于替换安全工具启动的配置。
- 与进程创建日志、registry set telemetry、文件签名和目标程序启动时间线交叉验证。

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [程序执行痕迹](../../../../../../questions/execution.md)
- [反取证与清理痕迹](../../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [AeDebug](aedebug.md)
- [App Paths](../../windows/currentversion/app-paths.md)
- [Policies\System](../../windows/currentversion/policies/system.md)

## 补充阅读

- [IFEO artifact](../../../../../../artifacts/persistence/ifeo.md)
- [MITRE ATT&CK: Image File Execution Options Injection](https://attack.mitre.org/techniques/T1546/012/)
