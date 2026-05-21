# HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall` |
| 离线 | `SOFTWARE\Policies\Microsoft\WindowsFirewall` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存 Windows Firewall / Windows Defender Firewall 的策略配置位置之一。这里更偏策略来源；运行时和本地规则配置还需要查看 `SYSTEM` hive 下的 FirewallPolicy。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `DomainProfile` | Key | 域网络 profile 策略。 | 视 GPO / MDM 而定 | 适用于域网络环境。 |
| `StandardProfile` | Key | 旧版或标准 profile 策略。 | 视系统版本而定 | 新版本更常见 Private/Public 概念。 |
| `PrivateProfile` | Key | 专用网络 profile 策略。 | 视策略而定 | 是否存在视版本而定。 |
| `PublicProfile` | Key | 公用网络 profile 策略。 | 视策略而定 | 是否存在视版本而定。 |
| `FirewallRules` | Key | 策略规则集合。 | 多个规则 value | 规则字符串需要解析。 |
| `EnableFirewall` | `REG_DWORD` | profile 防火墙开关策略。 | `0` / `1` | 是否生效需结合策略结果。 |
| `DefaultInboundAction` | `REG_DWORD` | 默认入站动作策略。 | 视策略而定 | 需结合 profile 和规则。 |
| `DefaultOutboundAction` | `REG_DWORD` | 默认出站动作策略。 | 视策略而定 | 需结合 profile 和规则。 |
| `DisableNotifications` | `REG_DWORD` | 通知策略。 | 视策略而定 | 不等于关闭防火墙。 |

## 默认状态与版本差异

该路径可能为空或不存在，尤其是未通过 GPO / MDM 配置防火墙策略的系统。不同 Windows 版本、域策略模板和 MDM 配置会影响 profile 名称与 value 集合。

## 注意事项

- 策略路径存在不等于当前 ActiveStore 规则完全相同。
- GPO / MDM / 安全平台可能覆盖本地 FirewallPolicy。
- 防火墙策略说明访问控制配置，不证明网络连接发生。

## 取证提示

- 与 `SYSTEM\...\FirewallPolicy` 对照，可区分本地配置和策略覆盖线索。
- 关注远程管理端口、RDP、SMB、WinRM、全放行规则，以及 profile 被关闭或默认入站动作放宽的情况。

## 相关场景

- [安全策略与防护配置](../../../../../questions/policy-security.md)
- [网络与系统环境](../../../../../questions/network.md)
- [反取证与清理痕迹](../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM Policies](../../policies.md)
- [FirewallPolicy](../../../system/controlset/services/sharedaccess/firewallpolicy.md)
- [NetworkList Profiles](../../microsoft/windows-nt/currentversion/networklist/profiles.md)

## 补充阅读

- [Firewall Policies artifact](../../../../../artifacts/security/firewall-policies.md)
- [Microsoft Learn: Firewall CSP](https://learn.microsoft.com/en-us/windows/client-management/mdm/firewall-csp)
