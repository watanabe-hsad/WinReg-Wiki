# HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Providers

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Providers` |
| 离线 | `SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Providers` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

注册 Windows 登录界面可枚举的 Credential Provider。Credential Provider 负责在 LogonUI 中提供凭据输入、选择或认证 UI，是登录体验的扩展点。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `{GUID}` | Key | 单个 Credential Provider 注册项。 | CLSID GUID | 需到 `HKCR\CLSID` 或 `SOFTWARE\Classes\CLSID` 解析 DLL。 |
| 默认值 | `REG_SZ` | Provider 显示名称或描述。 | 视组件而定 | 名称可被第三方组件设置。 |
| `Disabled` | `REG_DWORD` | 部分 Provider 可能使用的禁用状态。 | 视版本和组件而定 | 不是所有 Provider 都有该值。 |

## 默认状态与版本差异

Windows 自带多个 Credential Provider，具体 GUID 和组件随版本、登录方式、Windows Hello、智能卡、域加入状态和第三方认证产品变化。第三方 VPN、MFA、EDR、身份管理和智能卡组件也可能注册 Provider。

## 注意事项

- Provider 注册存在不等于它在某次登录中被使用。
- GUID 需要解析 CLSID、DLL 路径、签名和文件来源。
- 合法企业身份组件常注册 Credential Provider，不应仅凭第三方 DLL 判断异常。

## 取证提示

- 新增或异常 Provider 可作为登录链扩展、凭据拦截或身份组件变更线索。
- 需要与 LogonUI、Winlogon、文件签名、安装日志、EDR 模块加载和登录事件一起验证。

## 相关场景

- [账户与安全](../../../../../../../questions/accounts-security.md)
- [安全策略与防护配置](../../../../../../../questions/policy-security.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [Credential Provider Filters](credential-provider-filters.md)
- [LogonUI](logonui.md)
- [Winlogon](../../../windows-nt/currentversion/winlogon.md)
- [HKCR / Classes](../../../../classes.md)

## 补充阅读

- [Microsoft Learn: Credential Providers in Windows](https://learn.microsoft.com/en-us/windows/win32/secauthn/credential-providers-in-windows)
