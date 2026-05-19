# RDP 与远程访问

RDP 调查要区分客户端连接痕迹和服务端登录痕迹。`Terminal Server Client` 更偏向“本机作为客户端连接过哪些目标”。

## 优先级

| 优先级 | Artifact | 主要价值 |
|---|---|---|
| 高 | [Terminal Server Client](../artifacts/rdp/terminal-server-client.md) | MSTSC 客户端连接目标、用户名提示 |
| 高 | [fDenyTSConnections](../artifacts/rdp/fdenytsconnections.md) | 服务端是否允许远程桌面连接 |
| 中 | [RDP-Tcp PortNumber](../artifacts/rdp/rdp-tcp-portnumber.md) | RDP 监听端口配置 |
| 中 | [CredSSP / NLA](../artifacts/rdp/credssp-nla.md) | 网络级身份验证和凭据安全配置 |

## 交叉验证

- Security.evtx：`4624`、`4627`、`4634`、`4647`、`4778`、`4779`
- TerminalServices-LocalSessionManager
- TerminalServices-RemoteConnectionManager
- 防火墙日志与网络流量
- 凭据管理器和 Jump List

## 判断边界

- `Terminal Server Client` 是客户端侧目标历史，不能证明本机被 RDP 登录。
- [fDenyTSConnections](../artifacts/rdp/fdenytsconnections.md) `=0` 只能证明 RDP 允许状态，不能证明实际连接发生。
- 连接成功、失败、断开和重连要回到 Security.evtx 与 TerminalServices 日志。
