---
tags:
  - SecurityPolicy
  - Firewall
  - SYSTEM
  - HKLM
---

# Firewall Policies

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">防火墙规则与配置</span>
</div>

## Summary

Firewall Policies 记录 Windows Defender Firewall 配置和规则，可证明本机入站/出站访问控制状态，但策略来源可能是本地、GPO、MDM 或安全产品。

## Registry Paths

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy` | 机器级 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy` | 机器级 |
| Policy path | `HKLM\SOFTWARE` | `Policies\Microsoft\WindowsFirewall` | GPO / policy |

## Native Registry View

本地防火墙运行配置常位于 `HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy`。策略路径可位于 `HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall`。离线时必须解析 `SYSTEM\Select`。

## Offline Location

主要来自 `C:\Windows\System32\Config\SYSTEM`，策略来源还可能在 `C:\Windows\System32\Config\SOFTWARE`。调查 GPO 时还应收集 `C:\Windows\System32\GroupPolicy` 和 GroupPolicy Operational 日志。

## Data Meaning

| Field | Meaning |
|---|---|
| `FirewallRules` | 防火墙规则集合，value data 通常是规则字符串 |
| `DomainProfile` / `PublicProfile` / `StandardProfile` | 不同网络 profile 的防火墙状态和默认动作 |
| `EnableFirewall` | 对应 profile 防火墙启用状态 |
| rule data | 包含 action、dir、protocol、local port、app、profile 等字段 |

## Forensic Meaning

Firewall Policies 能说明某端口、程序或 profile 是否被允许或阻断。RDP、SMB、WinRM、RPC、反连端口和远控工具端口是高价值检查点。它证明规则配置存在，不证明连接发生。

## What It Can Prove

- 防火墙规则或 profile 配置在注册表中存在。
- 某端口、程序或方向可能被允许/阻断。
- 防火墙状态是否偏离基线。

## What It Cannot Prove

- 网络连接实际发生。
- 规则实际被命中。
- 配置来源一定是攻击者。
- 本机所有流量都受该规则控制，第三方防火墙和安全产品可能介入。

## Timestamp Notes

FirewallPolicy key LastWrite 是 key 级更新时间。具体规则 value 没有独立注册表时间戳。应结合 NetSecurity cmdlet 输出、Event Logs、Sysmon Event ID 13、Security 5156/5157、防火墙日志和 GPO 记录。

## OS Version Notes

Windows 7/10/11/Server 均有 Windows Firewall / Defender Firewall 配置，但规则字段、profile 名称和策略来源可能不同。GPO、MDM、安全产品和服务器角色会改变基线。

## Attacker Usage

攻击者可能开放 RDP、SMB、WinRM、C2 listener 或隧道端口，也可能关闭防火墙 profile。也可能添加看似系统组件的 allow rule。

## Detection Ideas

- 新增入站 allow rule，开放 `3389`、`5985/5986`、`445`、高危自定义端口。
- 防火墙 profile 被关闭或默认入站动作放宽。
- 规则 `App` 指向用户可写目录、远控工具或未知二进制。
- RDP port 改动与防火墙放行同一端口。

## False Positives

- 软件安装、VPN、远控工具、数据库、开发服务、企业管理代理、GPO 基线、云主机初始化。

## Collection

=== "PowerShell"

    ```powershell
    Get-NetFirewallProfile
    Get-NetFirewallRule -PolicyStore ActiveStore | Select-Object DisplayName, Enabled, Direction, Action
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy" /s
    reg query "HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall" /s
    ```

=== "Offline"

    ```text
    Collect SYSTEM and SOFTWARE hives. Resolve SYSTEM\Select before reading FirewallPolicy.
    ```

## Parsing Tools

- Registry Explorer
- RECmd
- KAPE
- Velociraptor
- PowerShell NetSecurity cmdlets for live systems

## Cross Validation

- Windows Firewall logs
- Security.evtx `5156`, `5157`
- Sysmon Event ID 3
- Sysmon Event ID 13
- RDP `PortNumber`
- `fDenyTSConnections`
- Network telemetry

## Example Findings

- FirewallPolicy contains an enabled inbound allow rule for local port `5001`, and RDP `PortNumber` is also `5001`; this proves matching exposure configuration, not a successful RDP login.
- DomainProfile `EnableFirewall=0` appears after a GPO update event; this should be investigated as a policy change, not immediately attributed to malware.

## References

- [Microsoft Learn: Windows Defender Firewall with Advanced Security](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/)
- [Microsoft Learn: Get-NetFirewallRule](https://learn.microsoft.com/en-us/powershell/module/netsecurity/get-netfirewallrule)
- [MITRE ATT&CK: Impair Defenses](https://attack.mitre.org/techniques/T1562/)

## Related Pages

- 场景：[安全策略与防护配置](../../questions/policy-security.md), [RDP 与远程访问](../../questions/rdp.md)
- 注册表位置：[HKLM\SYSTEM](../../registry-tree/hklm/system.md), [HKLM\SOFTWARE](../../registry-tree/hklm/software.md)
