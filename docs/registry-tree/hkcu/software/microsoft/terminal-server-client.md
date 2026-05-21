# HKCU\Software\Microsoft\Terminal Server Client

`Terminal Server Client` 保存当前用户 MSTSC 客户端侧目标历史。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Terminal Server Client` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Terminal Server Client` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Default` | Key | RDP MRU 目标列表。 |
| `Default\MRU0`、`MRU1` ... | `REG_SZ` | 远程主机名、IP 或目标字符串。 |
| `Servers\<host>` | Key | 单个目标主机记录。 |
| `Servers\<host>\UsernameHint` | `REG_SZ` | 用户名提示。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | 用户 `NTUSER.DAT`。 |
| 常见写入者 | Microsoft Remote Desktop Client / `mstsc.exe`。 |
| 注意 | 这是本机作为 RDP 客户端的历史，不是本机作为 RDP 服务端的登录记录。 |

## 相关 Artifact

- [Terminal Server Client](../../../../artifacts/rdp/terminal-server-client.md)
- [fDenyTSConnections](../../../../artifacts/rdp/fdenytsconnections.md)
- [RDP-Tcp PortNumber](../../../../artifacts/rdp/rdp-tcp-portnumber.md)
