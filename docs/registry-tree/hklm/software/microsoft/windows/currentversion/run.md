# HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

机器级登录启动项位置，适用于所有用户登录后的自动启动命令。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| Live | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce` |
| 32 位视图 | `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run` |
| 离线 | `SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

`Run` 保存用户登录后自动运行的机器级命令。`RunOnce` 保存一次性登录启动项，执行后通常会被删除或状态变化，具体行为受权限、策略和程序返回状态影响。

## 常见子键 / 值

| 名称 | 类型 | 含义 |
|---|---|---|
| `<value name>` | `REG_SZ` | 启动项名称，通常由软件或安装器自定义。 |
| `<value data>` | `REG_SZ` / `REG_EXPAND_SZ` | 启动命令、程序路径或带参数的命令行。 |
| `RunOnce` | Key | 一次性登录启动项。 |

## 默认状态 / 常见状态

默认可以为空。正常软件常写入更新器、同步客户端、输入法、企业管理代理、显卡或音频辅助组件。

## 版本差异

64 位 Windows 上 32 位程序可能写入 `WOW6432Node` 视图。启动处理细节与登录环境、策略和程序权限有关。

## 取证提示

该位置能说明机器级自启动配置存在，不等于命令已经执行。执行判断需要结合登录事件、进程创建、Prefetch、BAM / DAM、EDR 或文件系统时间线。

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU Run / RunOnce](../../../../../hkcu/software/microsoft/windows/currentversion/run.md)
- [WOW6432Node](../../../wow6432node.md)
- [Winlogon](../../windows-nt/currentversion/winlogon.md)

