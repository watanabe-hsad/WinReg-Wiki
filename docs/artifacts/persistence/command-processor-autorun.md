---
tags:
  - Persistence
  - Autoruns
  - HKCU
  - HKLM
---

# Command Processor\AutoRun

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">cmd.exe 启动钩子</span>
</div>

## 摘要

`Command Processor\AutoRun` 会在 `cmd.exe` 启动时自动执行配置命令，是隐蔽但高信号的用户级或机器级持久化位置。

## 注册表路径

| View | Hive / File | Path | Value | Scope |
|---|---|---|---|---|
| Live path | `HKCU` | `Software\Microsoft\Command Processor` | `AutoRun` | 当前用户 |
| Live path | `HKLM` | `Software\Microsoft\Command Processor` | `AutoRun` | 机器级 |
| Offline hive path | `NTUSER.DAT` | `Software\Microsoft\Command Processor` | `AutoRun` | 用户级 |
| Offline hive path | `SOFTWARE` | `Microsoft\Command Processor` | `AutoRun` | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中检查 `HKCU\Software\Microsoft\Command Processor` 与 `HKLM\Software\Microsoft\Command Processor`。Microsoft `cmd` 文档说明，若启动 `cmd.exe` 时未使用 `/D`，会查找这些 AutoRun 值并执行。

## 离线位置

用户级值在每个用户 `NTUSER.DAT`；机器级值在 `C:\Windows\System32\Config\SOFTWARE`。多用户排查必须枚举所有用户 hive，而不是只查当前 `HKCU`。

## 字段含义

| Field | Meaning |
|---|---|
| `AutoRun` | `cmd.exe` 启动时自动执行的命令，REG_SZ 或 REG_EXPAND_SZ |
| HKLM scope | 影响本机 cmd 启动，具体上下文取决于进程令牌 |
| HKCU scope | 影响指定用户 cmd 启动 |
| `/D` | 启动 `cmd.exe /D` 可禁用 AutoRun 执行 |

## 取证含义

该 value 存在即可证明 cmd 启动链被配置了自动命令。它常被忽略，因为不会出现在传统登录自启动列表中，但只要用户、脚本、管理员工具或服务调用 `cmd.exe`，就可能触发该命令。

## 可以证明

- 某个用户或机器级 cmd AutoRun 配置存在。
- 配置命令可能在未加 `/D` 的 `cmd.exe` 启动时执行。
- 可解释为什么看似正常的 `cmd.exe` 启动后产生额外进程或网络行为。

## 不能证明

- 不能单独证明已经有 cmd 实例触发过该命令。
- 不能证明每次 `cmd.exe` 都会执行；`/D`、策略或替代 shell 可能绕过。
- 不能证明命令成功执行或 payload 存在。

## 时间戳说明

`Command Processor` key LastWrite 只表示该 key 变化，不能精确到 `AutoRun` value 创建。应结合 Sysmon Event ID 13、Security 4657、EDR registry telemetry 和命令行日志确认写入时间。

## 系统版本差异

该机制长期存在于 Windows 客户端和 Server；语义主要由 `cmd.exe` 行为决定。PowerShell、Windows Terminal 或其他 shell 不直接受此 AutoRun 影响，除非它们启动了 `cmd.exe`。未知系统上应用 `cmd /?` 或 Microsoft 文档验证 `/D` 语义。

## 攻击滥用

攻击者可写入 `AutoRun` 执行脚本、设置代理、加载环境、启动反连或劫持管理员常用命令窗口。用户级写入不需要管理员权限，机器级写入通常需要管理员权限。

## 检测思路

- 任意非空 `AutoRun` 都值得审查，尤其是新出现或非基线主机。
- value data 包含 `powershell`、`curl`、`bitsadmin`、`mshta`、`rundll32`、UNC 路径、Base64、下载执行。
- HKCU AutoRun 指向用户可写目录或隐藏路径。
- 监控 `\Software\Microsoft\Command Processor\AutoRun` registry set，并关联后续 `cmd.exe` 子进程。

## 常见误报

- 开发环境、终端增强、企业登录脚本可能设置环境变量或初始化命令。
- 安全工具或运维脚本可能临时写入再清除。
- 合法 AutoRun 通常是短命令、内部脚本路径、有明确所有者和变更记录。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKCU:\Software\Microsoft\Command Processor" -ErrorAction SilentlyContinue |
      Select-Object AutoRun
    Get-ItemProperty "HKLM:\Software\Microsoft\Command Processor" -ErrorAction SilentlyContinue |
      Select-Object AutoRun
    ```

=== "reg.exe"

    ```cmd
    reg query "HKCU\Software\Microsoft\Command Processor" /v AutoRun
    reg query "HKLM\Software\Microsoft\Command Processor" /v AutoRun
    ```

=== "Offline"

    ```text
    Inspect SOFTWARE and every user's NTUSER.DAT for Software\Microsoft\Command Processor\AutoRun.
    ```

## 解析工具

- Autoruns：部分版本可显示 shell-related autoruns，但建议直接查 registry。
- Registry Explorer、RECmd：适合批量读取 value data 和 LastWrite。
- KAPE：采集 registry hives、Sysmon、PowerShell 和 shell 日志。
- Velociraptor：适合跨主机查找非空 AutoRun。

## 交叉验证

- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- Sysmon Event ID 1 / Security 4688：`cmd.exe` 启动后是否产生 AutoRun 命令子进程。
- PowerShell logs、script block logs、网络连接日志。
- 文件系统路径、签名、哈希和 `$UsnJrnl`。

## 示例结论

- `HKCU\S-1-5-21-...\Software\Microsoft\Command Processor\AutoRun` 为 `powershell -w hidden -enc ...`；该证据可证明该用户的 cmd 启动链被配置为执行混淆 PowerShell，但仍需进程日志确认是否触发。
- `HKLM\Software\Microsoft\Command Processor\AutoRun` 指向 `C:\Program Files\DevTools\init.cmd` 且与开发环境基线一致；可标记为正常环境初始化，不作为恶意持久化。

## 相关页面

- 场景：[自启动与持久化](../../questions/persistence.md)
- 注册表位置：[HKCU\Software](../../registry-tree/hkcu/software.md)、[HKLM\SOFTWARE](../../registry-tree/hklm/software.md)

## 参考资料

- [Microsoft Learn: cmd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)
- [MITRE ATT&CK: Command Processor](https://attack.mitre.org/techniques/T1059/003/)
