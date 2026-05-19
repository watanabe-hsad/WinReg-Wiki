# 网络与系统环境

网络配置调查关注代理、DNS、接口、网络 profile、主机名和时区。注册表能说明配置状态与历史 profile，但网络连接事实仍需日志和流量验证。

## 优先级

| 优先级 | Artifact / Path | 主要价值 |
|---|---|---|
| 高 | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles` | 网络 profile 名称、类型和首次/最近连接线索 |
| 高 | `HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters` | 主机名、域、DNS 和 TCP/IP 全局参数 |
| 高 | `HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\<GUID>` | 网卡级 IP、DHCP、DNS 配置 |
| 高 | `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings` | 用户级代理配置：`ProxyEnable`、`ProxyServer`、`AutoConfigURL` |
| 中 | `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` | IE/WinINet 区域映射，影响部分应用安全区域 |

## 高信号特征

- 用户级代理指向本机异常端口、内网未知主机或公网代理。
- `NameServer` 被手工设置为异常 DNS，且与 DHCP 配置冲突。
- 网络 profile 名称、网关、DNS 和连接时间线与入侵窗口一致。
- `AutoConfigURL` 指向可疑 PAC 文件。

## 交叉验证

- DNS Client Operational、DHCP Client Operational、Windows Firewall logs。
- NetFlow、代理日志、EDR network telemetry。
- Browser history、WinINet/WinHTTP 代理配置、PowerShell 网络命令历史。
- `TimeZoneInformation`、`ComputerName`、`Select / CurrentControlSet` 保证时间线和控制集正确。

## 结论写法

- 代理和 DNS 注册表值证明配置存在，不证明流量一定经过该配置。
- DHCP 字段和手工 `NameServer` 字段要分开解释；同一接口可能有历史残留。
