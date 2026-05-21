# HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings

`Internet Settings` 保存当前用户 WinINet、代理和部分区域相关设置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Internet Settings` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `ProxyEnable` | `REG_DWORD` | 用户代理开关。 |
| `ProxyServer` | `REG_SZ` | 代理服务器配置。 |
| `AutoConfigURL` | `REG_SZ` | PAC URL。 |
| `Connections` | Key | 连接配置，部分数据为二进制 blob。 |
| `ZoneMap` | Key | 安全区域映射。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | 用户 `NTUSER.DAT`。 |
| 常见写入者 | Internet Options、WinINet、浏览器、VPN、代理软件、GPO。 |
| 注意 | 这是用户级配置；系统级代理和 WinHTTP 代理需另查对应位置。 |

## 相关 Artifact

- 暂无专门 artifact 页面
- [Defender Policies](../../../../../../artifacts/security/defender-policies.md)
- [Firewall Policies](../../../../../../artifacts/security/firewall-policies.md)

