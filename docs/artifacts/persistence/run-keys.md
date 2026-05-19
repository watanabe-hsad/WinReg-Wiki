---
tags:
  - Persistence
  - Autoruns
  - HKCU
  - HKLM
---

# Run / RunOnce

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">用户级 / 机器级</span>
</div>

`Run` 和 `RunOnce` 用于配置登录时自动启动的程序，是恶意软件和正常软件都会频繁使用的持久化位置。

## Registry Paths

| Hive | Path | Scope |
|---|---|---|
| `HKCU` | `Software\Microsoft\Windows\CurrentVersion\Run` | 当前用户 |
| `HKCU` | `Software\Microsoft\Windows\CurrentVersion\RunOnce` | 当前用户 |
| `HKLM` | `Software\Microsoft\Windows\CurrentVersion\Run` | 所有用户 |
| `HKLM` | `Software\Microsoft\Windows\CurrentVersion\RunOnce` | 所有用户 |
| `HKLM` | `Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Run` | 32 位视图 |

## Forensic Meaning

这些键表示某个命令被配置为用户登录时启动。value name 通常是显示名称，value data 通常是可执行文件路径或命令行。

## What It Can Prove

- 程序或命令被配置为自启动。
- 配置范围是用户级还是机器级。
- key 的 LastWrite 可帮助估计该键最近一次变化时间。

## What It Cannot Prove

- 程序一定已经执行。
- 某个 value 的创建时间精确等于 key 的 LastWrite。
- 该启动项一定恶意。

## Timestamp Notes

注册表 value 通常没有独立时间戳。key LastWrite 表示该 key 的直接内容发生变化，不能直接当作某个具体 value 的创建时间。

## Detection Ideas

重点关注：

- 指向用户可写目录的启动项。
- 使用 `powershell.exe`、`wscript.exe`、`mshta.exe`、`rundll32.exe`、`regsvr32.exe`。
- 隐藏窗口、Base64、下载执行、长命令行。
- 伪装成系统组件的 value name。
- HKLM 启动项指向用户 profile。

## Collection

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
    Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"
    ```

=== "reg.exe"

    ```cmd
    reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
    reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\Run"
    ```

## Cross Validation

- Startup folder
- Scheduled Tasks
- Services
- Prefetch
- Sysmon Event ID 1 and 13
- Security logon events

