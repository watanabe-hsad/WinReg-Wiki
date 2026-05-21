# HKLM\SYSTEM\ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy` |
| 离线 | `SYSTEM\ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

保存 Windows Defender Firewall 本地 profile 和规则配置的一部分。策略来源可能是本地配置、GPO、MDM 或安全管理平台。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `DomainProfile` | Key | 域网络 profile 防火墙配置。 | 视环境而定 | 适用于域网络。 |
| `PrivateProfile` | Key | 专用网络 profile 防火墙配置。 | 视环境而定 | 适用于私有网络。 |
| `PublicProfile` | Key | 公用网络 profile 防火墙配置。 | 视环境而定 | 通常更严格。 |
| `FirewallRules` | Key | 本地防火墙规则集合。 | 多个规则 value | 规则数据通常为字符串格式。 |
| `RestrictedServices` | Key | 受限服务规则。 | 视配置而定 | 服务级网络规则。 |
| `EnableFirewall` | `REG_DWORD` | profile 防火墙开关。 | `0` 或 `1` | 是否生效需结合策略和服务状态。 |
| `DefaultInboundAction` | `REG_DWORD` | 默认入站行为。 | 视 profile 而定 | 需结合规则解释。 |
| `DefaultOutboundAction` | `REG_DWORD` | 默认出站行为。 | 视 profile 而定 | 需结合规则解释。 |
| `DisableNotifications` | `REG_DWORD` | 通知开关。 | 视策略而定 | 与防火墙开关不同。 |

## 默认状态与版本差异

默认 profile 配置随 Windows 版本、网络类型、域策略和安全基线变化。Windows 还可能在 `HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall` 下保存策略值。

## 注意事项

- 注册表规则存在不等于对应网络连接发生。
- GPO / MDM 可能覆盖本地配置；需要结合策略结果和运行时防火墙状态。
- 防火墙服务、规则命中和网络流量需要日志或 EDR 验证。

## 取证提示

- 重点看 RDP、SMB、WinRM、远控、异常高端口或全放行规则。
- 与 Windows Firewall logs、Security.evtx、进程创建、网络流量和 GPO 记录交叉验证。

## 相关场景

- [安全策略与防护配置](../../../../../../questions/policy-security.md)
- [网络与系统环境](../../../../../../questions/network.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [Services](../index.md)
- [Tcpip](../tcpip.md)
- [HKLM Policies](../../../../software/policies.md)

## 补充阅读

- [Firewall Policies artifact](../../../../../../artifacts/security/firewall-policies.md)
- [Microsoft Learn: Firewall CSP](https://learn.microsoft.com/en-us/windows/client-management/mdm/firewall-csp)
