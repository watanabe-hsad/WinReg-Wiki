---
tags:
  - Persistence
  - Autoruns
  - Winlogon
  - HKLM
---

# Winlogon\Userinit

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">登录流程持久化</span>
</div>

## 摘要

`Winlogon\Userinit` 定义用户登录后由 Winlogon 调用的初始化程序，任何非默认追加命令都应作为高优先级持久化线索调查。

## 注册表路径

| View | Hive / File | Path | Value | Scope |
|---|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Winlogon` | `Userinit` | 机器级 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Winlogon` | `Userinit` | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`，查看 `Userinit` value。默认常见值为 `C:\Windows\system32\userinit.exe,`，注意末尾逗号是正常格式的一部分。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SOFTWARE`。如果存在多套 Windows 目录或离线镜像挂载路径，确认当前系统盘和 `Windows` 目录后再解释路径。

## 字段含义

| Field | Meaning |
|---|---|
| `Userinit` | 登录后执行的用户初始化程序列表，REG_SZ |
| 默认值 | 通常为 `%SystemRoot%\system32\userinit.exe,` 或展开后的 `C:\Windows\system32\userinit.exe,` |
| 追加路径 | 逗号分隔的额外可执行文件可能在登录时被调用 |
| key LastWrite | Winlogon key 最近变化时间，不等于 `Userinit` value 创建时间 |

## 取证含义

该值控制登录初始化链。若默认 `userinit.exe` 后追加了用户可写路径、脚本解释器或异常二进制，通常是高风险持久化。若默认项被替换或删除，可能导致登录异常，也可能是攻击者试图劫持登录流程。

## 可以证明

- 机器级 Winlogon `Userinit` 配置在采集时包含某个命令或路径。
- 配置影响交互式用户登录流程，具备高权限持久化价值。
- key LastWrite 可辅助定位 Winlogon 配置最近变化时间。

## 不能证明

- 不能单独证明该命令已经在某次登录中执行。
- 不能证明是哪个用户或进程修改了该值。
- 不能只凭非默认值判断恶意；某些壳替换、加固或企业软件可能修改登录链。

## 时间戳说明

注册表 value 通常没有独立时间戳。`Winlogon` key LastWrite 可能由 `Shell`、`Userinit`、`AutoAdminLogon` 等任意 value 修改触发。需要结合 Sysmon Event ID 13、Security 4657、EDR registry telemetry 或 hive transaction log 还原具体修改时间。

## 系统版本差异

Windows 7/10/11/Server 默认值通常围绕 `userinit.exe,`，但系统目录、大小写和环境变量展开形式可能不同。未知 build 上不要机械匹配单一字符串，应规范化路径后比较。Server Core 或定制 Shell 环境需结合实际基线。

## 攻击滥用

攻击者可在默认 `userinit.exe,` 后追加恶意程序，例如 `C:\Windows\system32\userinit.exe,C:\Users\Public\svc.exe`，从而在用户登录时触发。也可替换为 wrapper 程序再调用合法 `userinit.exe`，以降低登录异常。

## 检测思路

- `Userinit` 不包含默认 `userinit.exe` 或包含额外逗号分隔路径。
- 追加路径位于用户可写目录、`ProgramData` 非标准目录、网络共享或可疑解释器。
- value data 中出现 `powershell.exe`、`cmd.exe /c`、`wscript.exe`、`mshta.exe`、`rundll32.exe`。
- 监控 `TargetObject` 包含 `\Windows NT\CurrentVersion\Winlogon\Userinit` 的 registry set 事件。

## 常见误报

- 定制 kiosk、VDI、Shell 替换、登录加固或企业管理软件可能合法修改。
- 系统升级或恢复操作可能重写默认值。
- 路径大小写、短路径、环境变量形式差异不应直接作为恶意信号。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" |
      Select-Object Userinit
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit
    ```

=== "Offline"

    ```text
    Load SOFTWARE hive and inspect Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit.
    Preserve SOFTWARE.LOG1 and SOFTWARE.LOG2 when available.
    ```

## 解析工具

- Autoruns：可快速显示 Winlogon autoruns。
- Registry Explorer：适合手工核对 value data 和 LastWrite。
- RECmd：适合批量抽取 Winlogon key。
- KAPE：采集 SOFTWARE、事件日志、Autoruns 输出。
- Velociraptor：适合跨主机 hunting 非默认 Userinit。

## 交叉验证

- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- Security 4624/4634 登录时间线，确认配置后是否有交互式登录。
- Prefetch、BAM、Amcache、文件系统时间线确认追加程序是否存在或执行。
- Autoruns、服务、计划任务排查同一 payload 是否多点持久化。

## 示例结论

- `Userinit` value 为 `C:\Windows\system32\userinit.exe,C:\Users\Public\updater.exe`，追加路径位于公共可写目录；该证据可证明登录初始化链存在机器级异常追加命令，但执行仍需结合登录事件和进程日志确认。
- `Winlogon` key LastWrite 与 Sysmon Event ID 13 时间一致，修改进程为 `reg.exe`，命令行包含 `Userinit`；可支持“该持久化配置在该时间被写入”的判断。

## 相关页面

- 场景：[自启动与持久化](../../questions/persistence.md)
- 注册表位置：[HKLM\SOFTWARE](../../registry-tree/hklm/software/index.md)、[HKEY_LOCAL_MACHINE](../../registry-tree/hklm/index.md)

## 参考资料

- [MITRE ATT&CK: Boot or Logon Autostart Execution - Winlogon Helper DLL](https://attack.mitre.org/techniques/T1547/004/)
- [Microsoft Learn: Winlogon and credential providers](https://learn.microsoft.com/en-us/windows/win32/secauthn/winlogon-and-credential-providers)
