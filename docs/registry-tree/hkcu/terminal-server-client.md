# Terminal Server Client

`HKCU\Software\Microsoft\Terminal Server Client` 保存 MSTSC 客户端侧历史。

## 文件

| Live 视图 | 离线文件 |
|---|---|
| `HKCU\Software\Microsoft\Terminal Server Client` | `C:\Users\<user>\NTUSER.DAT` |

## 常用路径

| 路径 | 含义 |
|---|---|
| `Default` | RDP MRU 目标列表。 |
| `Servers\<host>` | 单个目标主机记录，可能包含用户名提示。 |
| `Servers\<host>\UsernameHint` | 用户名提示。 |

## 注意

| 项 | 说明 |
|---|---|
| 客户端侧 | 这里记录本机作为 RDP 客户端的目标，不是服务端登录日志。 |
| 连接成功 | 条目存在不等于 RDP 登录成功。 |
| 服务端证据 | 服务端调查看目标主机 Security.evtx 和 TerminalServices 日志。 |

## 相关 Artifact

[Terminal Server Client](../../artifacts/rdp/terminal-server-client.md)
