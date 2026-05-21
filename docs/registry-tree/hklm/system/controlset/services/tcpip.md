# HKLM\SYSTEM\ControlSet00x\Services\Tcpip

`Services\Tcpip` 保存 TCP/IP 全局参数和网络接口配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Services\Tcpip` |
| 离线 | `SYSTEM\ControlSet00x\Services\Tcpip` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Parameters` | Key | TCP/IP 全局参数。 |
| `Parameters\Hostname` | `REG_SZ` | 主机名相关值，具体使用需结合 ComputerName。 |
| `Parameters\Domain` | `REG_SZ` | DNS domain 相关配置。 |
| [`Parameters\Interfaces\<GUID>`](tcpip/parameters/interfaces.md) | Key | 单个网络接口配置。 |
| `NameServer` | `REG_SZ` | 静态 DNS 服务器。 |
| `DhcpNameServer` | `REG_SZ` | DHCP 下发的 DNS 服务器。 |
| `IPAddress` / `DhcpIPAddress` | `REG_MULTI_SZ` / `REG_SZ` | 静态或 DHCP IP 地址。 |
| `DefaultGateway` / `DhcpDefaultGateway` | `REG_MULTI_SZ` / `REG_SZ` | 网关配置。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | TCP/IP stack、DHCP Client、网络设置、GPO、VPN / EDR / 管理软件。 |
| 注意 | 接口 GUID 需要结合 NetworkList、设备枚举或 live 网络配置确认对应网卡。 |

## 相关场景

- [网络与系统环境](../../../../../questions/network.md)
- [RDP 与远程访问](../../../../../questions/rdp.md)
- [常规注册表检查](../../../../../questions/registry-checklist.md)

## 相关位置

- [Tcpip Interfaces](tcpip/parameters/interfaces.md)
- [NetworkList Profiles](../../../software/microsoft/windows-nt/currentversion/networklist/profiles.md)
- [FirewallPolicy](sharedaccess/firewallpolicy.md)

## 补充阅读

- 暂无专门 artifact 页面
- [Firewall Policies](../../../../../artifacts/security/firewall-policies.md)
- [Defender Policies](../../../../../artifacts/security/defender-policies.md)
