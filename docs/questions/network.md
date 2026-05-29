# 网络与系统环境

## 检查目标

确认代理、DNS、接口、主机名、时区和控制集映射等系统环境配置，为时间线和网络行为分析提供上下文。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [Tcpip](../registry-tree/hklm/system/controlset/services/tcpip.md) | TCP/IP 全局参数、接口 DNS、DHCP、网关。 | 配置存在不等于连接发生。 |
| [Tcpip Interfaces](../registry-tree/hklm/system/controlset/services/tcpip/parameters/interfaces.md) | 单个接口 IP、DNS、DHCP、网关和租约字段。 | DHCP 租约时间不是会话结束时间。 |
| [Internet Settings](../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings.md) | 用户级代理、PAC、WinINet 配置。 | 只影响使用相关 API 的应用。 |
| [ZoneMap](../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings/zonemap.md) | URL 安全区域映射。 | 区域映射不等于站点访问。 |
| [HKCU Policies](../registry-tree/hkcu/software/microsoft/windows/currentversion/policies.md) | 用户级策略入口。 | 策略来源需结合 GPO / MDM。 |
| [NetworkList Profiles](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/networklist/profiles.md) | 网络 profile 名称、类别和连接时间线索。 | 时间字段需工具和时区处理。 |
| [FirewallPolicy](../registry-tree/hklm/system/controlset/services/sharedaccess/firewallpolicy.md) | 防火墙 profile 和规则配置。 | 规则存在不等于连接发生。 |
| [WindowsFirewall Policies](../registry-tree/hklm/software/policies/microsoft/windowsfirewall.md) | 防火墙策略路径。 | 需与本地 FirewallPolicy 和 ActiveStore 对照。 |
| [ComputerName](../registry-tree/hklm/system/controlset/control/computername.md) | 主机名和环境标识。 | 名称可能变更，需要时间线。 |
| [TimeZoneInformation](../registry-tree/hklm/system/controlset/control/timezone.md) | 时区和 bias。 | 用于时间线归一化。 |
| [Select](../registry-tree/hklm/system/select.md) | CurrentControlSet 映射。 | 离线分析必须先解析。 |

## 判断要点

- 用户级代理指向本机异常端口、内网未知主机或公网代理时，记录 SID 和 profile。
- `NameServer`、DHCP DNS、接口 GUID 需要分开解释。
- `NetworkList\Profiles` 的 `Category` 会影响防火墙 profile 语义；策略路径和本地 FirewallPolicy 需要分开解释。
- `ZoneMap` 说明安全区域映射，不能单独证明用户访问了该站点。
- 时区和主机名用于解释日志和时间线，不是安全事件本身。

## 交叉验证

- DNS Client Operational、DHCP Client Operational、Windows Firewall logs。
- NetFlow、代理日志、EDR network telemetry、浏览器历史。
- WinHTTP 代理配置、PowerShell 网络命令历史、VPN / EDR 日志。
- `TimeZoneInformation`、`ComputerName`、`Select / CurrentControlSet`。

## 常见误判

- 代理和 DNS 注册表值证明配置存在，不证明所有流量经过该配置。
- DHCP 历史残留可能与当前网络状态不同。
- 手工 DNS、PAC 和企业代理可能来自正常管理策略。

## 相关场景

- [RDP 与远程访问](rdp.md)
- [安全策略与防护配置](policy-security.md)
- [常规注册表检查](registry-checklist.md)
