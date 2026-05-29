---
tags:
  - RDP
  - RemoteAccess
  - SYSTEM
  - HKLM
---

# fDenyTSConnections

此页保留 `fDenyTSConnections` 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [Terminal Server](../../registry-tree/hklm/system/controlset/control/terminal-server.md) | RDP 服务端允许 / 拒绝配置。 |
| [RDP-Tcp](../../registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp.md) | RDP listener 端口、NLA 和安全层配置。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `fDenyTSConnections` | `REG_DWORD` | `0` 通常表示允许远程桌面连接，`1` 通常表示拒绝。 |

## 采集与工具

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections
```

- Registry Explorer / RECmd：查看 `SYSTEM` hive、ControlSet 和 key LastWrite。
- KAPE / Velociraptor：跨主机枚举 RDP 服务端配置。

## 常见误读

- `fDenyTSConnections=0` 不等于发生过 RDP 登录。
- 该值不证明防火墙已放行、端口正在监听或 TermService 正在运行。
- key LastWrite 是 key 级时间，不是该 value 的独立修改时间。

## 交叉验证

- TerminalServices-RemoteConnectionManager、TerminalServices-LocalSessionManager。
- Security.evtx `4624` LogonType `10`、`4778`、`4779`。
- Windows Firewall rules、TermService 状态、网络 telemetry。

## 相关场景

- [RDP 与远程访问](../../questions/rdp.md)
- [安全策略与防护配置](../../questions/policy-security.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: Enable Remote Desktop](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-allow-access)
- [MITRE ATT&CK: Remote Services - RDP](https://attack.mitre.org/techniques/T1021/001/)
