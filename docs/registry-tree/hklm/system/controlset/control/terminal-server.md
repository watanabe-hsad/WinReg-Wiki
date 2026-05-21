# HKLM\SYSTEM\ControlSet00x\Control\Terminal Server

`Control\Terminal Server` 保存本机作为 Remote Desktop 服务端的主要配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server` |
| 离线 | `SYSTEM\ControlSet00x\Control\Terminal Server` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `fDenyTSConnections` | `REG_DWORD` | `0` 通常表示允许远程桌面连接，`1` 表示拒绝。 |
| `WinStations\RDP-Tcp` | Key | RDP listener 配置。 |
| `WinStations\RDP-Tcp\PortNumber` | `REG_DWORD` | RDP 监听端口；regedit 可能按十六进制显示。 |
| `WinStations\RDP-Tcp\UserAuthentication` | `REG_DWORD` | NLA 相关配置。 |
| `WinStations\RDP-Tcp\SecurityLayer` | `REG_DWORD` | RDP 安全层相关配置。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | System Properties、Remote Desktop 设置、GPO、管理工具。 |
| 注意 | 这里是服务端配置，不记录客户端连接历史，也不单独证明发生登录。 |

## 相关 Artifact

- [fDenyTSConnections](../../../../../artifacts/rdp/fdenytsconnections.md)
- [RDP-Tcp PortNumber](../../../../../artifacts/rdp/rdp-tcp-portnumber.md)
- [CredSSP / NLA](../../../../../artifacts/rdp/credssp-nla.md)

