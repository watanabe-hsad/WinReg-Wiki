---
tags:
  - RDP
  - RemoteAccess
  - SYSTEM
  - HKLM
---

# RDP-Tcp PortNumber

此页保留 `RDP-Tcp\PortNumber` 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [RDP-Tcp](../../registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp.md) | RDP listener 端口、NLA、安全层和连接限制配置。 |
| [Terminal Server](../../registry-tree/hklm/system/controlset/control/terminal-server.md) | RDP 服务端根配置。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `PortNumber` | `REG_DWORD` | RDP-Tcp listener 端口；默认常见为十进制 `3389` / 十六进制 `0x00000d3d`。 |

## 采集与工具

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber
```

- Registry Explorer / RECmd：读取 `SYSTEM` hive 中的 `RDP-Tcp`。
- PowerShell / EDR：live 系统可核对监听端口、服务状态和防火墙规则。

## 常见误读

- `PortNumber` 是 DWORD，报告端口时要确认十六进制 / 十进制。
- 非默认端口不一定恶意，可能来自基线、托管服务或运维策略。
- 端口配置不证明正在监听、已放行或发生过连接。

## 交叉验证

- `fDenyTSConnections`、TermService 状态、Windows Firewall rules。
- `netstat`、EDR network telemetry、TerminalServices logs。
- Security.evtx LogonType `10` 和外部连接记录。

## 相关场景

- [RDP 与远程访问](../../questions/rdp.md)
- [网络与系统环境](../../questions/network.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: Change the listening port for Remote Desktop](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/change-listening-port-remote-desktop)
- [MITRE ATT&CK: Remote Services - RDP](https://attack.mitre.org/techniques/T1021/001/)
