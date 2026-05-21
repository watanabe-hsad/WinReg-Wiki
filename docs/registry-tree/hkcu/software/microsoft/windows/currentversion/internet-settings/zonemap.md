# HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` |
| 用户 SID | `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` |

## 离线位置

`C:\Users\<User>\NTUSER.DAT`

## 作用

保存用户级 URL 安全区域映射。该位置会影响 IE / WinINet 相关组件如何把域名、IP 范围或站点归入安全区域。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Domains` | Key | 按域名保存区域映射。 | 子键为域名层级 | 可包含 `http`、`https` 等 value。 |
| `EscDomains` | Key | Enhanced Security Configuration 相关域映射。 | Server 环境更常见 | 视系统角色而定。 |
| `Ranges` | Key | IP 范围映射。 | 子键如 `Range1` | 常见 value 包含 `:Range`。 |
| `ProtocolDefaults` | Key | 协议默认区域。 | 视配置而定 | 具体值需按系统版本确认。 |
| `http` / `https` / `file` | `REG_DWORD` | 协议到区域编号的映射。 | `1`、`2`、`3`、`4` 常见 | 需结合所属子键解释。 |

## 默认状态与版本差异

区域编号常见语义：`0` 本机、`1` Intranet、`2` Trusted Sites、`3` Internet、`4` Restricted Sites。实际是否被应用使用取决于应用、系统版本和安全配置。

## 注意事项

- ZoneMap 说明区域映射配置，不等于用户访问过该站点。
- Trusted Sites 或 Restricted Sites 可能来自 GPO、企业代理、浏览器兼容需求或安全基线。
- 需要区分 `HKCU` 用户级映射和机器级 / 策略映射。

## 取证提示

- 异常域名或 IP 被加入 Trusted Sites 时，可作为 Web 访问、代理或策略调查线索。
- 与浏览器历史、代理日志、DNS、EDR network telemetry 和 GPO 记录交叉验证。

## 相关场景

- [网络与系统环境](../../../../../../../questions/network.md)
- [安全策略与防护配置](../../../../../../../questions/policy-security.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [Internet Settings](../internet-settings.md)
- [HKCU Software](../../../../index.md)
- [HKLM Policies](../../../../../../hklm/software/policies.md)

## 补充阅读

- [Microsoft Learn: URL security zones](https://learn.microsoft.com/en-us/previous-versions/troubleshoot/browsers/security-privacy/ie-security-zones-registry-entries)
