# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\CachedLogonsCount

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon /v CachedLogonsCount` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon /v CachedLogonsCount` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

`CachedLogonsCount` 控制系统可缓存的域登录凭据数量，用于域控制器不可用时的交互式登录。它是登录策略配置，不包含缓存凭据本体，也不记录登录事件。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `CachedLogonsCount` | `REG_SZ` | 可缓存的域登录次数。 | `0` 到 `50` | `0` 表示不缓存域登录凭据。 |

## 默认状态与版本差异

Microsoft 文档说明 Windows Server 2008 之后默认值为 `10`；Windows Server 2003 默认值为 `25`。客户端和企业基线可能通过本地策略、GPO 或安全模板调整该值；实际位置仍落在 `Winlogon` 配置中。

## 注意事项

- 该值不保存缓存凭据内容。
- `CachedLogonsCount=0` 说明配置为不缓存域登录凭据，不等于历史上没有缓存过。
- 本地账户登录、域登录成功与否需要回到 Security.evtx、SAM / 域记录和登录场景验证。

## 取证提示

- 该值可辅助判断主机是否允许离线域登录。
- 低值或 `0` 可能来自安全基线；高值应结合组织策略解释。

## 相关场景

- [账户与安全](../../../../../../../questions/accounts-security.md)
- [安全策略与防护配置](../../../../../../../questions/policy-security.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [Winlogon](../winlogon.md)
- [Policies\System](../../../windows/currentversion/policies/system.md)
- [SECURITY](../../../../../security.md)

## 补充阅读

- [Microsoft Learn: Cached domain logon information](https://learn.microsoft.com/en-us/troubleshoot/windows-server/user-profiles-and-logon/cached-domain-logon-information)
