# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

控制部分本地账户是否显示在登录界面用户列表中。它影响 UI 显示，不创建、删除、启用或禁用账户。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `<AccountName>` | `REG_DWORD` | 指定账户在登录界面中的显示控制。 | `0` / `1` | `0` 常被用于隐藏账户显示。 |
| `SpecialAccounts` | Key | Winlogon 下的特殊账户配置容器。 | 可能不存在 | 不存在时通常表示未显式配置。 |
| `UserList` | Key | 账户显示控制列表。 | value name 为账户名 | 账户名需与 SAM / 域记录核对。 |

## 默认状态与版本差异

普通系统上该路径可能不存在。登录界面行为还受域策略、隐私设置、最后登录用户显示策略、系统版本和账户类型影响。

## 注意事项

- `UserList` 隐藏显示不等于账户不存在、被禁用或无法登录。
- value name 是账户名，不是 SID；需要与 SAM、ProfileList 和登录事件关联。
- 管理员、OEM、实验环境和运维脚本也可能使用该位置控制 UI 显示。

## 取证提示

- `AccountName=0` 可作为登录 UI 隐藏账户线索。
- 需要与 SAM 本地账户、Security.evtx 账户创建/登录事件、ProfileList 和 LogonUI 记录交叉验证。

## 相关场景

- [账户与安全](../../../../../../../questions/accounts-security.md)
- [安全策略与防护配置](../../../../../../../questions/policy-security.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [Winlogon](../winlogon.md)
- [LogonUI](../../../windows/currentversion/authentication/logonui.md)
- [ProfileList](../profilelist.md)
- [SAM](../../../../../sam.md)

## 补充阅读

- [SpecialAccounts\UserList artifact](../../../../../../../artifacts/security/specialaccounts-userlist.md)
