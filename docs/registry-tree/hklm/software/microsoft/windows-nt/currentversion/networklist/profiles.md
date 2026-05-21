# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存 Windows 识别过的网络配置文件。每个 profile 通常对应一个网络环境，可包含网络名称、类别和连接时间相关字段。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `<ProfileGUID>` | Key | 单个网络 profile。 | GUID 子键 | 需要与接口、日志和网络配置关联。 |
| `ProfileName` | `REG_SZ` | 网络显示名称。 | Wi-Fi SSID、网络名、域网络名 | 名称可重复或变化。 |
| `Description` | `REG_SZ` | 网络描述。 | 视网络类型而定 | 可能与 `ProfileName` 相同。 |
| `Managed` | `REG_DWORD` | 是否由策略或域管理相关状态。 | `0` / `1` 常见 | 需结合环境解释。 |
| `Category` | `REG_DWORD` | 网络类别。 | `0` Public、`1` Private、`2` DomainAuthenticated 常见 | 具体语义视版本而定。 |
| `DateCreated` | `REG_BINARY` | profile 创建时间。 | SYSTEMTIME 结构常见 | 解析需工具支持。 |
| `DateLastConnected` | `REG_BINARY` | 最近连接时间。 | SYSTEMTIME 结构常见 | 不是所有环境都可靠。 |

## 默认状态与版本差异

字段和时间格式随 Windows 版本和网络类型变化。Wi-Fi、有线、VPN、域网络和虚拟网卡可能表现不同。

## 注意事项

- NetworkList profile 说明系统识别过网络 profile，不等于某个进程产生网络连接。
- `DateCreated`、`DateLastConnected` 需要使用可靠工具解析，并记录时区处理方式。
- 网络名称可能由用户、接入点或系统生成，不应单独作为唯一标识。

## 取证提示

- 可辅助确认主机曾处于哪个网络环境，以及网络类别是否可能影响防火墙 profile。
- 与 DHCP、DNS、网关、Windows Firewall logs、NetworkProfile Operational 和 EDR network telemetry 交叉验证。

## 相关场景

- [网络与系统环境](../../../../../../../questions/network.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM SOFTWARE](../../../../../index.md)
- [Tcpip Interfaces](../../../../../system/controlset/services/tcpip/parameters/interfaces.md)
- [FirewallPolicy](../../../../../system/controlset/services/sharedaccess/firewallpolicy.md)

## 补充阅读

- [SANS DFIR posters](https://www.sans.org/posters/)
