# HKLM\SYSTEM\ControlSet00x\Control\Session Manager\Environment

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment` |
| 离线 | `SYSTEM\ControlSet00x\Control\Session Manager\Environment` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

保存系统级环境变量。用户登录和进程创建时，系统级变量会与用户级变量组合成进程环境。实际进程环境还受父进程、服务账户、登录会话和应用启动方式影响。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Path` | `REG_EXPAND_SZ` / `REG_SZ` | 系统级可执行文件搜索路径。 | 包含 Windows、System32 等路径 | 可能被安装器追加目录。 |
| `ComSpec` | `REG_EXPAND_SZ` / `REG_SZ` | 默认命令解释器路径。 | `%SystemRoot%\system32\cmd.exe` 常见 | 修改需谨慎解释。 |
| `PATHEXT` | `REG_SZ` | 可执行扩展名列表。 | `.COM;.EXE;.BAT;...` 常见 | 影响命令解析。 |
| `TEMP` | `REG_EXPAND_SZ` / `REG_SZ` | 系统级临时目录。 | `%SystemRoot%\TEMP` 常见 | 服务上下文常用。 |
| `TMP` | `REG_EXPAND_SZ` / `REG_SZ` | 系统级临时目录。 | `%SystemRoot%\TEMP` 常见 | 通常与 `TEMP` 一致。 |
| `windir` | `REG_SZ` / `REG_EXPAND_SZ` | Windows 目录。 | `C:\Windows` 常见 | 具体盘符视安装而定。 |

## 默认状态与版本差异

默认值随安装路径、系统版本、语言、角色和已安装软件变化。不要把某个固定 `Path` 当作所有系统的基线。

## 注意事项

- 系统级变量会影响服务、计划任务和普通用户进程，但已经启动的进程可能仍保留旧环境。
- 安装器、开发工具、驱动、EDR、数据库和 VPN 都可能正常追加 `Path`。
- 离线分析时使用 `Select\Current` 确认当前控制集。

## 取证提示

- `Path` 中出现用户可写目录、临时目录、网络路径或不存在目录时，可作为执行环境污染线索。
- 修改 `ComSpec`、`PATHEXT` 或系统临时目录需结合进程创建、文件系统和管理员操作记录。

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [程序执行痕迹](../../../../../../questions/execution.md)
- [反取证与清理痕迹](../../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU Environment](../../../../../hkcu/environment.md)
- [ControlSet00x](../../index.md)
- [Command Processor](../../../../../hkcu/software/microsoft/command-processor.md)

## 补充阅读

- [Microsoft Learn: Recognized environment variables](https://learn.microsoft.com/en-us/windows/deployment/usmt/usmt-recognized-environment-variables)
