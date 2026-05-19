---
tags:
  - Persistence
  - Autoruns
  - Winlogon
  - HKLM
  - HKCU
---

# Winlogon\Shell

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">登录 Shell 持久化</span>
</div>

## Summary

`Winlogon\Shell` 指定用户登录后的 Shell 程序，默认通常为 `explorer.exe`；额外命令或替换 Shell 是高风险持久化与 kiosk/VDI 配置分界点。

## Registry Paths

| View | Hive / File | Path | Value | Scope |
|---|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Winlogon` | `Shell` | 机器级 |
| Live path | `HKCU` | `Software\Microsoft\Windows NT\CurrentVersion\Winlogon` | `Shell` | 用户级，需验证生效范围 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Winlogon` | `Shell` | 机器级 |
| Offline hive path | `NTUSER.DAT` | `Software\Microsoft\Windows NT\CurrentVersion\Winlogon` | `Shell` | 用户级 |

## Native Registry View

机器级路径在 `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`。某些持久化会写入用户级 `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell`，调查时应同时查 HKLM 和所有用户 hive。

## Offline Location

机器级值位于 `C:\Windows\System32\Config\SOFTWARE`。用户级值位于各用户 `C:\Users\<user>\NTUSER.DAT`。多用户机器上需要用 [ProfileList](../security/profilelist.md) 映射 SID，不能只检查当前用户。

## Data Meaning

| Field | Meaning |
|---|---|
| `Shell` | 登录后启动的 Shell，REG_SZ |
| 默认值 | 通常为 `explorer.exe` |
| 额外命令 | 逗号或命令行追加可能导致额外程序登录启动 |
| 用户级覆盖 | 若存在，可能只影响对应 SID；实际生效需结合 OS 版本和策略验证 |

## Forensic Meaning

该值可以证明系统或用户配置了登录 Shell。异常 Shell 常用于登录持久化、替换桌面环境、kiosk 或 VDI 场景。对攻击调查而言，高风险信号是默认 `explorer.exe` 被替换、追加可疑程序、或用户级 Shell 指向用户可写目录。

## What It Can Prove

- HKLM 或某个用户 hive 中存在 Shell 配置。
- 配置可能影响登录后启动的桌面 Shell 或额外命令。
- 与登录事件结合可判断异常配置是否有机会被触发。

## What It Cannot Prove

- 不能单独证明该 Shell 已实际启动。
- 不能证明修改者身份。
- 不能在未验证环境基线时把非 `explorer.exe` 一概定为恶意。

## Timestamp Notes

`Winlogon` key LastWrite 反映 key 内容最近变化，可能由 `Shell`、`Userinit` 或其他 Winlogon value 触发。用户级 `Shell` 的 LastWrite 位于对应 `NTUSER.DAT`，机器级位于 `SOFTWARE`，二者要分别解释。

## OS Version Notes

Windows 桌面系统默认通常为 `explorer.exe`。Server Core、kiosk、VDI、Shell Launcher、嵌入式或定制桌面环境可能使用非默认 Shell。用户级 `Shell` 的实际生效行为在不同版本和策略组合下需样本验证；未知时写“配置存在，生效待验证”。

## Attacker Usage

攻击者可把 `Shell` 修改为 `explorer.exe, C:\Users\Public\svc.exe`，或替换为恶意 wrapper 后再启动 Explorer。用户级 Shell 可用于低权限持久化，机器级 Shell 则影响更广且通常需要管理员权限。

## Detection Ideas

- HKLM `Shell` 不等于规范化后的 `explorer.exe`。
- HKCU `Winlogon\Shell` 存在且指向用户可写目录或脚本解释器。
- `Shell` value data 包含逗号、`cmd.exe`、`powershell.exe`、`wscript.exe`、UNC 路径或长混淆命令。
- 监控 `\Windows NT\CurrentVersion\Winlogon\Shell` 的 registry set 事件并关联修改进程。

## False Positives

- Kiosk、VDI、Citrix、Shell Launcher、第三方桌面或设备管理软件。
- 企业硬化脚本可能重写默认 Shell。
- 多语言系统、短路径和环境变量展开形式可能造成字符串差异。

## Collection

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" |
      Select-Object Shell
    Get-ItemProperty "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -ErrorAction SilentlyContinue |
      Select-Object Shell
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell
    reg query "HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell
    ```

=== "Offline"

    ```text
    Inspect SOFTWARE and every user's NTUSER.DAT for Winlogon\Shell.
    Correlate SID to user profile before reporting user-level Shell.
    ```

## Parsing Tools

- Autoruns：可显示 Winlogon Shell 相关 autoruns。
- Registry Explorer、RECmd：适合人工和批量解析。
- KAPE：采集 registry hives、Autoruns、事件日志。
- Velociraptor：适合多主机搜索非默认 Shell。

## Cross Validation

- Winlogon `Userinit`、Run key、Services、Scheduled Tasks。
- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- Security 4624 登录事件、Shell 进程创建日志、Explorer Prefetch。
- Kiosk/VDI/MDM/GPO 基线。

## Example Findings

- `HKCU` 中 `S-1-5-21-...\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell` 为 `explorer.exe,C:\Users\alice\AppData\Roaming\svc.exe`；该证据可证明 alice 用户级登录 Shell 被追加异常程序，是否执行需结合登录后进程创建日志。
- 机器级 `Shell` 为厂商 kiosk shell，路径位于 `C:\Program Files\Vendor\Shell.exe` 且签名有效；在无其他异常证据时应标记为业务基线，而不是恶意持久化。

## Related Pages

- 场景：[自启动与持久化](../../questions/persistence.md)
- 注册表位置：[HKLM\SOFTWARE](../../registry-tree/hklm/software.md)、[NTUSER.DAT](../../registry-tree/hku/ntuser.md)

## References

- [MITRE ATT&CK: Boot or Logon Autostart Execution - Winlogon Helper DLL](https://attack.mitre.org/techniques/T1547/004/)
- [Microsoft Learn: Shell Launcher](https://learn.microsoft.com/en-us/windows/configuration/shell-launcher/)
