# RDP 与远程访问

## 检查目标

区分本机作为 RDP 客户端连接过目标，还是本机作为 RDP 服务端允许连接、修改端口或调整认证安全配置。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [Terminal Server Client](../registry-tree/hkcu/software/microsoft/terminal-server-client.md) | MSTSC 客户端目标历史和用户名提示。 | 客户端侧记录不能证明本机被登录。 |
| [Terminal Server](../registry-tree/hklm/system/controlset/control/terminal-server.md) | RDP 服务端开关。 | 允许连接不等于连接发生。 |
| [RDP-Tcp](../registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp.md) | RDP listener 端口、NLA、安全层和连接限制。 | 配置存在不等于端口正在监听。 |
| [CredSSP](../registry-tree/hklm/system/controlset/control/terminal-server/credssp.md) | RDP 认证兼容性和 encryption oracle remediation 策略。 | 策略值不等于登录成功。 |
| [Firewall / Policies](../registry-tree/hklm/software/policies.md) | 防火墙策略和远程访问相关策略入口。 | 规则来源需结合 GPO/MDM。 |
| [Tcpip](../registry-tree/hklm/system/controlset/services/tcpip.md) | 主机网络配置、接口和 DNS。 | 网络配置不等于连接事实。 |
| [ComputerName](../registry-tree/hklm/system/controlset/control/computername.md) | 主机名和环境标识。 | 用于关联日志和远程连接记录。 |

## 判断要点

- `Terminal Server Client` 说明某用户 hive 中存在连接目标历史。
- `fDenyTSConnections=0` 通常说明允许远程桌面连接，但仍需检查服务状态、防火墙和组策略。
- `PortNumber` 是 `REG_DWORD`，regedit 可能显示为十六进制。
- NLA / CredSSP 相关值说明服务端认证配置，不等于登录成功或失败。

## 交叉验证

- Security.evtx：`4624`、`4625`、`4634`、`4647`、`4778`、`4779`。
- TerminalServices-LocalSessionManager、TerminalServices-RemoteConnectionManager。
- Windows Firewall logs、网络流量、EDR network telemetry。
- 凭据管理器、Jump Lists、RDP client cache、用户登录会话时间线。

## 常见误判

- 管理员启用 RDP、远程协助、VDI、堡垒机或企业策略会产生正常配置变化。
- 客户端历史中的主机名可能来自手工输入或历史缓存，不一定连接成功。
- RDP 端口变更可能是加固策略，也可能是规避扫描；需要变更来源和网络证据。

## 相关场景

- [账户与安全](accounts-security.md)
- [安全策略与防护配置](policy-security.md)
- [网络与系统环境](network.md)
- [常规注册表检查](registry-checklist.md)

## 补充阅读

- [Terminal Server Client artifact](../artifacts/rdp/terminal-server-client.md)
- [fDenyTSConnections artifact](../artifacts/rdp/fdenytsconnections.md)
- [RDP-Tcp PortNumber artifact](../artifacts/rdp/rdp-tcp-portnumber.md)
- [CredSSP / NLA artifact](../artifacts/rdp/credssp-nla.md)
