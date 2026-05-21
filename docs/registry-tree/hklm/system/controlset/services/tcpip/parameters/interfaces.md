# HKLM\SYSTEM\ControlSet00x\Services\Tcpip\Parameters\Interfaces

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces` |
| 离线 | `SYSTEM\ControlSet00x\Services\Tcpip\Parameters\Interfaces` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

保存每个网络接口的 TCP/IP 配置。子键通常以接口 GUID 命名，包含 DHCP、静态 IP、DNS、网关和租约时间相关值。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `<InterfaceGUID>` | Key | 单个网络接口配置。 | GUID 子键 | 需要映射到具体网卡。 |
| `EnableDHCP` | `REG_DWORD` | 是否启用 DHCP。 | `0` / `1` | 与静态 IP 字段互相解释。 |
| `DhcpIPAddress` | `REG_SZ` | DHCP 分配的 IP 地址。 | IPv4 字符串 | 历史残留需谨慎。 |
| `IPAddress` | `REG_MULTI_SZ` | 静态 IP 地址。 | IPv4 列表 | 静态配置时更有意义。 |
| `DhcpNameServer` | `REG_SZ` | DHCP 下发 DNS。 | DNS 列表 | 与 `NameServer` 区分。 |
| `NameServer` | `REG_SZ` | 手工 DNS 配置。 | DNS 列表 | 可能覆盖 DHCP DNS。 |
| `DefaultGateway` | `REG_MULTI_SZ` | 静态默认网关。 | 网关列表 | 静态配置字段。 |
| `DhcpDefaultGateway` | `REG_MULTI_SZ` / `REG_SZ` | DHCP 默认网关。 | 网关列表 | DHCP 字段。 |
| `LeaseObtainedTime` | `REG_DWORD` | DHCP 租约获取时间。 | Unix epoch 常见 | 需按工具和时区处理。 |
| `LeaseTerminatesTime` | `REG_DWORD` | DHCP 租约到期时间。 | Unix epoch 常见 | 不等于主机在线结束时间。 |

## 默认状态与版本差异

字段取决于 IPv4/IPv6、DHCP/静态配置、VPN、虚拟网卡和系统版本。某些接口可能只有部分值。

## 注意事项

- DHCP 字段和静态字段要分开解释。
- 接口 GUID 需要结合 NetworkList、设备枚举、live `ipconfig /all` 或日志确认具体网卡。
- 租约时间说明 DHCP 租约，不直接证明某个网络连接行为。

## 取证提示

- 异常 DNS、网关或静态 IP 可作为网络配置调查线索。
- 与 DHCP Client、DNS Client、NetworkProfile、Firewall logs 和 EDR network telemetry 交叉验证。

## 相关场景

- [网络与系统环境](../../../../../../../questions/network.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [Tcpip](../../tcpip.md)
- [NetworkList Profiles](../../../../../software/microsoft/windows-nt/currentversion/networklist/profiles.md)
- [FirewallPolicy](../../sharedaccess/firewallpolicy.md)

## 补充阅读

- [Microsoft Learn: TCP/IP registry values for Microsoft TCP/IP](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/tcpip-and-nbt-configuration-parameters)
