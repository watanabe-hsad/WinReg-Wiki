---
tags:
  - RDP
  - RemoteAccess
  - NTUSER.DAT
---

# Terminal Server Client

此页保留 `Terminal Server Client` 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKCU\Software\Microsoft\Terminal Server Client](../../registry-tree/hkcu/software/microsoft/terminal-server-client.md) | 当前用户 MSTSC 客户端目标历史和用户名提示。 |
| [HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server](../../registry-tree/hklm/system/controlset/control/terminal-server.md) | 本机作为 RDP 服务端的配置。 |

## 字段语义

| 子键 / Value | 类型 | 含义 |
|---|---|---|
| `Default` | Key | MRU 目标列表。 |
| `Default\MRU0`、`MRU1` ... | `REG_SZ` | 最近输入或选择的 RDP 目标。 |
| `Servers\<host>` | Key | 单个目标主机记录。 |
| `Servers\<host>\UsernameHint` | `REG_SZ` | 连接 UI 中保存的用户名提示。 |

## 采集与工具

```powershell
Get-ItemProperty "HKCU:\Software\Microsoft\Terminal Server Client\Default"
Get-ChildItem "HKCU:\Software\Microsoft\Terminal Server Client\Servers"
```

- Registry Explorer / RECmd：查看用户 hive 中的 MRU、Servers 子键和 LastWrite。
- KAPE：采集 `NTUSER.DAT`、Jump Lists、Credential Manager 相关位置和 RDP 日志。
- Velociraptor：跨用户枚举 RDP client 目标。

## 常见误读

- 客户端历史不能证明 RDP 登录成功。
- 目标主机名或 IP 可能来自输入历史、旧缓存或保存连接，不等于当前仍可访问。
- 该位置说明本机作为客户端的线索，不说明本机是否被远程登录。

## 交叉验证

- Security.evtx `4624`、`4625`、`4778`、`4779`。
- TerminalServices-LocalSessionManager、TerminalServices-RemoteConnectionManager。
- Jump Lists、Credential Manager、RDP cache、Firewall logs。
- 网络流量、EDR network telemetry、目标主机日志。

## 相关场景

- [RDP 与远程访问](../../questions/rdp.md)
- [账户与安全](../../questions/accounts-security.md)
- [网络与系统环境](../../questions/network.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: Remote Desktop clients](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients)
