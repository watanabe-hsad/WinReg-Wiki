---
tags:
  - SecurityPolicy
  - UAC
  - SOFTWARE
  - HKLM
---

# UAC Policies

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">权限提升策略</span>
</div>

## 摘要

UAC Policies 记录 User Account Control 的关键安全策略，能提示管理员令牌、提示行为和远程本地账户过滤是否被削弱，但不能简单把“UAC 降低”直接等同恶意。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows\CurrentVersion\Policies\System` | 机器级 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows\CurrentVersion\Policies\System` | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`。这些值通常可由本地安全策略、GPO、MDM、基线脚本或管理员手工修改。

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`。需要结合 GroupPolicy Operational、MDM diagnostics、本地安全策略导出和变更日志判断来源。

## 字段含义

| Value | Meaning |
|---|---|
| `EnableLUA` | UAC 总开关相关值；关闭通常会显著改变安全边界，并可能需要重启 |
| `ConsentPromptBehaviorAdmin` | 管理员提升提示行为 |
| `ConsentPromptBehaviorUser` | 标准用户提升提示行为 |
| `PromptOnSecureDesktop` | 是否在 secure desktop 上提示 |
| `LocalAccountTokenFilterPolicy` | 远程本地管理员令牌过滤相关，常影响远程管理横向移动 |
| `EnableInstallerDetection` | 安装程序检测策略 |

## 取证含义

UAC 策略可证明本机权限提升提示和令牌过滤配置状态。攻击者可能降低提示、关闭 UAC 或设置 `LocalAccountTokenFilterPolicy=1` 以便利远程本地管理员操作。结论必须结合环境基线，因为服务器、实验室、老旧软件兼容或企业管理策略可能合法调整。

## 可以证明

- UAC 相关 registry policy 值存在及其采集时状态。
- 配置是否偏离组织安全基线。
- `LocalAccountTokenFilterPolicy` 是否可能影响远程本地管理员令牌行为。

## 不能证明

- 攻击者修改了配置。
- 管理员权限提升实际发生。
- UAC 实际被绕过或恶意利用。
- 策略立即生效，尤其是需要重启的配置。

## 时间戳说明

`Policies\System` key LastWrite 是 key 级时间，可能由多个 policy value 修改触发。具体修改时间应结合 Sysmon Event ID 13、Security 4657、GroupPolicy Operational、MDM 或 EDR telemetry。

## 系统版本差异

Windows 7/10/11/Server 均使用这些 UAC 策略，但默认值、企业基线和安全建议可能随版本变化。`EnableLUA` 修改常需要重启才完整生效。未知版本应对“实际生效”写待验证。

## 攻击滥用

攻击者可能关闭 UAC、降低管理员提示、关闭 secure desktop，或设置 `LocalAccountTokenFilterPolicy=1` 以改善远程本地管理员 token 使用。也可能通过 GPO 滥用批量改变策略。

## 检测思路

- `EnableLUA` 从启用基线改为禁用。
- `ConsentPromptBehaviorAdmin`、`PromptOnSecureDesktop` 降低交互保护。
- `LocalAccountTokenFilterPolicy=1` 出现在非授权主机，随后出现远程服务创建、SMB 管理共享访问或 PsExec 类行为。
- 非 GPO/MDM 进程写入 `Policies\System`。

## 常见误报

- 企业兼容性策略、旧软件、实验室、kiosk、VDI、特殊运维基线、GPO/MDM 正常下发。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    ```

=== "Offline"

    ```text
    Load SOFTWARE hive and inspect Microsoft\Windows\CurrentVersion\Policies\System.
    ```

## 解析工具

- Registry Explorer
- RECmd
- KAPE
- Velociraptor
- RegRipper

## 交叉验证

- Sysmon Event ID 13
- Security Event ID 4657
- GroupPolicy Operational log
- MDM diagnostics
- Security.evtx `4672`, `4624`
- Service creation and remote execution telemetry

## 示例结论

- `LocalAccountTokenFilterPolicy=1` exists on a workstation outside the remote-admin baseline; this proves a configuration that may allow less restricted remote local administrator tokens, but not that remote execution occurred.
- `EnableLUA` was changed to `0` by `reg.exe`, followed by a reboot; this supports a UAC weakening timeline, but the reason and actor require process and account evidence.

## 参考资料

- [Microsoft Learn: User Account Control security policy settings](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/settings-and-configuration)
- [Microsoft Learn: LocalAccountTokenFilterPolicy](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/user-account-control-and-remote-restriction)
- [MITRE ATT&CK: Impair Defenses](https://attack.mitre.org/techniques/T1562/)

## 相关页面

- 场景：[安全策略与防护配置](../../questions/policy-security.md)
- 注册表位置：[HKLM\SOFTWARE](../../registry-tree/hklm/software.md)
