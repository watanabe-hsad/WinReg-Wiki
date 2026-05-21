# HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings` |
| 用户 SID | `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Internet Settings` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Internet Settings` |

## 离线位置

`C:\Users\<User>\NTUSER.DAT`

## 作用

保存用户级 WinINet / Internet Options 配置，包括代理、PAC、连接配置和安全区域映射。许多使用 WinINet 的应用会读取这里，但并不是所有程序都会使用该代理配置。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `ProxyEnable` | `REG_DWORD` | 用户代理开关。 | `0` 关闭，`1` 开启 | 仅说明 WinINet 用户代理配置。 |
| `ProxyServer` | `REG_SZ` | 代理服务器。 | `host:port` 或协议分组 | 需要结合 `ProxyEnable`。 |
| `ProxyOverride` | `REG_SZ` | 不走代理的主机列表。 | `<local>`、域名、通配符 | 影响代理绕过行为。 |
| `AutoConfigURL` | `REG_SZ` | PAC 文件 URL。 | URL | 可来自用户设置、脚本或策略。 |
| `Connections` | Key | 连接配置。 | 二进制 blob 常见 | 具体字段需工具解析。 |
| [`ZoneMap`](internet-settings/zonemap.md) | Key | 安全区域映射。 | `Domains`、`Ranges` 等 | 影响 IE / WinINet 区域判断。 |

## 默认状态与版本差异

默认代理通常关闭，但企业代理、VPN、浏览器、PAC、GPO 和 MDM 都可能写入。现代浏览器不一定完全依赖该位置，具体行为视应用和 API 而定。

## 注意事项

- 这里是用户级设置；系统级 WinHTTP 代理不是同一位置。
- 代理值存在不等于流量一定经过代理。
- `AutoConfigURL` 指向 PAC 文件时，需要获取 PAC 内容和网络日志才能解释实际路由。

## 取证提示

- 可用于解释某用户会话的代理、PAC 和安全区域上下文。
- 异常代理、PAC 或绕过列表可与进程、浏览器、DNS、网络流量和 EDR 记录交叉验证。

## 相关场景

- [网络与系统环境](../../../../../../questions/network.md)
- [反取证与清理痕迹](../../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [ZoneMap](internet-settings/zonemap.md)
- [HKCU Software](../../../index.md)
- [Tcpip Interfaces](../../../../../hklm/system/controlset/services/tcpip/parameters/interfaces.md)

## 补充阅读

- [Microsoft Learn: Setting and retrieving internet options](https://learn.microsoft.com/en-us/windows/win32/wininet/setting-and-retrieving-internet-options)

