# HKCU Terminal Server Client

`HKCU\Software\Microsoft\Terminal Server Client` 记录 MSTSC 客户端侧连接目标和部分用户名提示。它说明“本用户上下文曾保存或出现过 RDP 客户端目标”，不是服务端登录证据。

## Windows 原生视图

Live 路径为 `HKCU\Software\Microsoft\Terminal Server Client`，常见子键为 `Default` 与 `Servers`。离线时读取目标用户 `NTUSER.DAT`。

## 离线 hive 文件来源

| 逻辑路径 | 离线文件 |
|---|---|
| `HKCU\Software\Microsoft\Terminal Server Client` | `C:\Users\<user>\NTUSER.DAT` |

## 典型取证价值

- 还原本机作为 RDP 客户端连接过的主机名、IP 或保存的服务器条目。
- 结合 Jump Lists、凭据管理器、Security.evtx 和网络日志区分“客户端连接目标”和“服务端登录来源”。

## 典型检测价值

- 发现普通办公主机连接到服务器网段、域控或异常公网 RDP。
- 监控新出现的 `Servers\<host>`，结合 `mstsc.exe` 进程执行和网络连接。

## 常见误判

- 条目存在不代表连接成功，也不代表凭据有效。
- 主机名可能来自手工输入、历史保留或自动补全。
- RDP 服务端入站调查应看目标主机事件日志，而不是只看客户端键。

## 重点子路径

| 子路径 | 价值 | 相关 artifact |
|---|---|---|
| `Default` | MRU 目标列表 | [Terminal Server Client](../../artifacts/rdp/terminal-server-client.md) |
| `Servers\<host>` | 每个目标主机记录，可能含用户名提示 | [Terminal Server Client](../../artifacts/rdp/terminal-server-client.md) |

## 关联 artifact 页面

- [Terminal Server Client](../../artifacts/rdp/terminal-server-client.md)
