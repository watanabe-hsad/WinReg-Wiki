# HKLM\SYSTEM\ControlSet00x\Control\Terminal Server\WinStations\RDP-Tcp

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp` |
| 离线 | `SYSTEM\ControlSet00x\Control\Terminal Server\WinStations\RDP-Tcp` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

保存 RDP-Tcp listener 的服务端配置，包括监听端口、NLA、连接限制和安全层。它描述远程桌面服务端如何接受连接，不记录连接内容或登录事实。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `PortNumber` | `REG_DWORD` | RDP listener 端口。 | 默认常见为十进制 `3389` / 十六进制 `0x00000d3d` | regedit 显示进制可能造成误读。 |
| `UserAuthentication` | `REG_DWORD` | Network Level Authentication 相关配置。 | 视版本和策略而定 | 需结合系统版本和策略解释。 |
| `SecurityLayer` | `REG_DWORD` | RDP 安全层配置。 | 视版本和策略而定 | 降低安全层需结合基线判断。 |
| `MaxInstanceCount` | `REG_DWORD` | listener 最大连接实例相关配置。 | 视版本和角色而定 | Server / Client 表现不同。 |
| `MinEncryptionLevel` | `REG_DWORD` | 最低加密等级相关配置。 | 视策略而定 | 需结合 RDS 策略。 |

## 默认状态与版本差异

RDP-Tcp 路径在 Windows Client 和 Server 中常见，但默认值会受 SKU、远程桌面角色、域策略、MDM、安全基线和系统补丁影响。端口默认值较稳定，NLA 和安全层需按版本与组织基线解释。

## 注意事项

- `PortNumber` 是 DWORD，报告中应明确十进制值。
- RDP-Tcp 配置存在不等于端口正在监听或防火墙已放行。
- 离线分析必须先通过 `SYSTEM\Select` 确认当前 `ControlSet00x`。

## 取证提示

- 非默认 `PortNumber`、NLA 关闭或安全层降低可作为远程访问配置变化线索。
- 需要与 `TermService` 状态、防火墙规则、TerminalServices 日志和 Security.evtx 登录事件验证。

## 相关场景

- [RDP 与远程访问](../../../../../../questions/rdp.md)
- [安全策略与防护配置](../../../../../../questions/policy-security.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [Terminal Server](../terminal-server.md)
- [FirewallPolicy](../../services/sharedaccess/firewallpolicy.md)
- [Tcpip Interfaces](../../services/tcpip/parameters/interfaces.md)

## 补充阅读

- [RDP-Tcp PortNumber artifact](../../../../../../artifacts/rdp/rdp-tcp-portnumber.md)
- [CredSSP / NLA artifact](../../../../../../artifacts/rdp/credssp-nla.md)
