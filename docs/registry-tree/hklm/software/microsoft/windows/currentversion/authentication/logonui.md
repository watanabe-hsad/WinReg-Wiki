# HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI` |
| 离线 | `SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存 Windows 登录界面相关配置和状态线索。该位置靠近登录 UI、用户 tile、凭据提供器显示和交互式登录体验，但不等同于登录事件本身。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `UserTile` | Key | 用户 tile 相关映射。 | SID 到图片路径或资源线索 | 需结合 ProfileList。 |
| `LastLoggedOnUser` | `REG_SZ` | 最近显示的登录用户线索。 | 域\用户或 SID 相关格式 | 版本和策略相关。 |
| `LastLoggedOnSAMUser` | `REG_SZ` | 最近显示的 SAM 格式用户。 | `HOST\user` 常见 | 不等于成功登录时间。 |
| `LastLoggedOnDisplayName` | `REG_SZ` | 显示名线索。 | 用户显示名 | 可能为空或由策略控制。 |
| `SelectedUserSID` | `REG_SZ` | 登录 UI 选中用户 SID。 | SID 字符串 | 需要与 ProfileList / SAM 验证。 |

## 默认状态与版本差异

具体 value 随 Windows 版本、域加入状态、隐私策略、登录方式和 Credential Provider 配置变化。某些环境会隐藏最近登录用户。

## 注意事项

- LogonUI 值主要说明登录界面显示或选择状态，不证明登录成功。
- 多用户、域账户、Azure AD、服务账户和临时 profile 场景需要结合 SID 映射。
- 最近显示用户可能被策略、注销、锁屏或远程登录流程影响。

## 取证提示

- 可辅助识别最近登录界面显示过的用户或 SID。
- 应与 Security.evtx 登录事件、ProfileList、SAM / 域记录和用户 hive 时间线交叉验证。

## 相关场景

- [账户与安全](../../../../../../../questions/accounts-security.md)
- [安全策略与防护配置](../../../../../../../questions/policy-security.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [Credential Providers](credential-providers.md)
- [ProfileList](../../../windows-nt/currentversion/profilelist.md)
- [Winlogon](../../../windows-nt/currentversion/winlogon.md)
- [Policies\System](../policies/system.md)

## 补充阅读

- [SpecialAccounts\UserList artifact](../../../../../../../artifacts/security/specialaccounts-userlist.md)
