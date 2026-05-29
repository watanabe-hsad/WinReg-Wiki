# HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider Filters

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider Filters` |
| 离线 | `SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider Filters` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

注册 Credential Provider Filter。过滤器可影响登录界面中哪些 Credential Provider 被显示或可用，属于登录 UI 和认证体验扩展点。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `{GUID}` | Key | 单个 Credential Provider Filter 注册项。 | CLSID GUID | 需到 Classes / CLSID 解析组件 DLL。 |
| 默认值 | `REG_SZ` | 过滤器名称或描述。 | 视组件而定 | 可能来自第三方身份组件。 |

## 默认状态与版本差异

默认过滤器、第三方过滤器和注册方式随 Windows 版本、Windows Hello、智能卡、MFA、VPN、身份管理软件和企业安全组件变化。

## 注意事项

- Filter 注册存在不等于它在某次登录中生效。
- 第三方身份、MFA、VPN、EDR 和智能卡组件可能合法注册过滤器。
- 需要解析 CLSID、DLL 路径、签名和安装来源。

## 取证提示

- 新增未知过滤器可作为登录界面扩展点变化线索。
- 需要与 Credential Providers、LogonUI、Winlogon、安装日志和模块加载记录一起验证。

## 相关场景

- [账户与安全](../../../../../../../questions/accounts-security.md)
- [安全策略与防护配置](../../../../../../../questions/policy-security.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [Credential Providers](credential-providers.md)
- [LogonUI](logonui.md)
- [HKCR / Classes](../../../../classes.md)

## 补充阅读

- [Microsoft Learn: Credential Providers in Windows](https://learn.microsoft.com/en-us/windows/win32/secauthn/credential-providers-in-windows)
