# HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System` |
| 离线 | `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存 UAC、管理员审批模式、登录提示和部分系统安全策略。这里是本机策略状态的一部分，实际生效还可能受 GPO、MDM、安全基线和系统版本影响。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `EnableLUA` | `REG_DWORD` | UAC 总开关相关值。 | `0` / `1` | 修改后通常需要重启才完整生效。 |
| `ConsentPromptBehaviorAdmin` | `REG_DWORD` | 管理员提权提示行为。 | 视策略而定 | 与管理员审批模式相关。 |
| `ConsentPromptBehaviorUser` | `REG_DWORD` | 标准用户提权提示行为。 | 视策略而定 | 影响凭据提示。 |
| `PromptOnSecureDesktop` | `REG_DWORD` | 是否在安全桌面显示 UAC 提示。 | `0` / `1` | 需结合策略解释。 |
| `LocalAccountTokenFilterPolicy` | `REG_DWORD` | 本地账户远程 UAC 过滤相关值。 | 默认常不存在 | 常用于远程管理语境。 |
| `DisableCAD` | `REG_DWORD` | Ctrl+Alt+Del 登录要求相关策略。 | 视策略而定 | 与交互式登录设置有关。 |

## 默认状态与版本差异

默认值随 Windows 版本、SKU、安全基线和域策略变化。不要只凭单个 value 判断系统整体安全状态。

## 注意事项

- 该路径中的策略值说明配置状态，不直接说明修改来源。
- UAC 相关配置变化不等于已经发生提权或远程执行。
- 域策略、MDM 和安全基线可能覆盖本地配置。

## 取证提示

- `EnableLUA=0`、`PromptOnSecureDesktop=0`、异常 `LocalAccountTokenFilterPolicy` 可作为安全策略变化线索。
- 需要与 GroupPolicy、Security.evtx、管理员操作、远程登录和服务创建记录交叉验证。

## 相关场景

- [安全策略与防护配置](../../../../../../../questions/policy-security.md)
- [账户与安全](../../../../../../../questions/accounts-security.md)
- [RDP 与远程访问](../../../../../../../questions/rdp.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM Policies](../../../../policies.md)
- [LogonUI](../authentication/logonui.md)
- [Winlogon](../../../windows-nt/currentversion/winlogon.md)

## 补充阅读

- [UAC Policies artifact](../../../../../../../artifacts/security/uac-policies.md)
- [Microsoft Learn: User Account Control settings and configuration](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/settings-and-configuration)
