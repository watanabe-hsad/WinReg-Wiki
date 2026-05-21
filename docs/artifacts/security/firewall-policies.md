---
tags:
  - SecurityPolicy
  - Firewall
  - SYSTEM
  - HKLM
---

# Firewall Policies

此页保留 Windows Defender Firewall 配置 artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy](../../registry-tree/hklm/system/controlset/services/sharedaccess/firewallpolicy.md) | 本地 profile、规则和受限服务配置。 |
| [HKLM\SOFTWARE\Policies](../../registry-tree/hklm/software/policies.md) | GPO / MDM 等策略来源可能写入的软件策略位置。 |

## 字段语义

| 子键 / Value | 类型 | 含义 |
|---|---|---|
| `DomainProfile` | Key | 域网络 profile 配置。 |
| `PrivateProfile` | Key | 专用网络 profile 配置。 |
| `PublicProfile` | Key | 公用网络 profile 配置。 |
| `FirewallRules` | Key | 本地防火墙规则集合。 |
| `RestrictedServices` | Key | 服务级网络规则。 |
| `EnableFirewall` | `REG_DWORD` | 对应 profile 的防火墙开关。 |
| `DefaultInboundAction` | `REG_DWORD` | 默认入站行为。 |
| `DefaultOutboundAction` | `REG_DWORD` | 默认出站行为。 |

## 采集与工具

```powershell
Get-NetFirewallProfile
Get-NetFirewallRule -PolicyStore ActiveStore | Select-Object DisplayName, Enabled, Direction, Action
reg query "HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy" /s
```

- Registry Explorer / RECmd：查看规则字符串和 key LastWrite。
- PowerShell NetSecurity cmdlets：live 系统核对有效规则。
- KAPE / Velociraptor：采集 SYSTEM、SOFTWARE、Firewall logs 和策略记录。

## 常见误读

- 规则存在不等于网络连接发生或规则被命中。
- GPO、MDM、安全产品或云初始化脚本可能覆盖本地配置。
- 第三方防火墙或 EDR 网络控制可能影响实际流量。

## 交叉验证

- Windows Firewall logs。
- Security.evtx `5156`、`5157`。
- Sysmon Event ID 3、Event ID 13。
- RDP `PortNumber`、`fDenyTSConnections`、网络流量和 EDR telemetry。

## 相关场景

- [安全策略与防护配置](../../questions/policy-security.md)
- [网络与系统环境](../../questions/network.md)
- [RDP 与远程访问](../../questions/rdp.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: Windows Firewall](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/)
- [Microsoft Learn: Firewall CSP](https://learn.microsoft.com/en-us/windows/client-management/mdm/firewall-csp)
