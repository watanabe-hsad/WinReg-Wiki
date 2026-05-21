# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug` |
| 32 位视图 | `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\AeDebug` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存应用程序错误调试器相关配置。Windows 可在进程崩溃时调用配置的调试器或错误处理组件；该位置更偏崩溃处理和调试，不是普通程序启动项。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Debugger` | `REG_SZ` | 崩溃时调用的调试器命令。 | 视调试器和 WER 配置而定 | 可被开发工具设置。 |
| `Auto` | `REG_SZ` | 是否自动调用调试器相关值。 | `0` / `1` 常见 | 需结合系统配置。 |
| `UserDebuggerHotKey` | `REG_DWORD` | 用户调试热键相关值。 | 视配置而定 | 通常不用于常规调查。 |

## 默认状态与版本差异

AeDebug 行为受 Windows Error Reporting、调试工具、Visual Studio / WinDbg 和系统版本影响。64 位系统上还需检查 WOW6432Node 视图。

## 注意事项

- AeDebug 配置存在不等于调试器已经被调用。
- 触发通常需要目标进程崩溃或异常处理流程。
- 合法开发工具和调试器可能写入该路径。

## 取证提示

- `Debugger` 指向用户可写目录、脚本解释器或未知二进制时，可作为异常崩溃处理链线索。
- 与应用崩溃日志、WER 目录、进程创建、调试器文件时间线和 EDR telemetry 一起验证。

## 相关场景

- [程序执行痕迹](../../../../../../questions/execution.md)
- [自启动与持久化](../../../../../../questions/persistence.md)
- [反取证与清理痕迹](../../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [IFEO](ifeo.md)
- [App Paths](../../windows/currentversion/app-paths.md)
- [WOW6432Node](../../../wow6432node.md)

## 补充阅读

- [Microsoft Learn: Enabling postmortem debugging](https://learn.microsoft.com/en-us/windows/win32/debug/configuring-automatic-debugging)
